"""World enter on UDP 9000, and the nearby-entity model once the zone session is up."""

from __future__ import annotations

import logging
import struct
import time
from dataclasses import dataclass, field

from eqclient.opcodes import require, titanium_opcodes
from eqclient.packets import (
    character_select_names,
    char_create,
    enter_world,
    login_info,
    name_approval,
    zone_server_info,
)
from eqclient.session import Session, SessionError
from eqclient.sheet import Character, build


def _horiz_xy(x1: float, y1: float, x2: float, y2: float) -> float:
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def _split(packet: bytes) -> tuple[int, bytes]:
    if len(packet) < 2:
        return 0, b""
    return struct.unpack_from("<H", packet)[0], packet[2:]


def doors_along(doors, start, end, skip: set[int], reach: float = 15.0):
    """Doors whose position lies on this step. Exit doors are left for the leave action."""
    hits = []
    for door in doors:
        if door.door_id in skip or door.opened:
            continue
        if door.tried:
            continue
        if abs(door.z - start[2]) > 20.0:
            continue
        if _segment_distance((door.x, door.y), (start[0], start[1]), (end[0], end[1])) <= reach:
            hits.append(door)
    return hits


def _segment_distance(point, start, end) -> float:
    dx, dy = end[0] - start[0], end[1] - start[1]
    length = dx * dx + dy * dy
    if length <= 1e-6:
        return ((point[0] - start[0]) ** 2 + (point[1] - start[1]) ** 2) ** 0.5
    t = max(0.0, min(1.0, ((point[0] - start[0]) * dx + (point[1] - start[1]) * dy) / length))
    nearest = (start[0] + t * dx, start[1] + t * dy)
    return ((point[0] - nearest[0]) ** 2 + (point[1] - nearest[1]) ** 2) ** 0.5


def blocks_step(point, start, end, radius: float = 2.0) -> bool:
    """True when point sits on the step, ahead of his feet, close enough to stop him."""
    dx, dy = end[0] - start[0], end[1] - start[1]
    length = dx * dx + dy * dy
    if length <= 1e-6:
        return False
    t = ((point[0] - start[0]) * dx + (point[1] - start[1]) * dy) / length
    if t <= 0.0 or t > 1.0:
        return False
    if (t * t * length) ** 0.5 < 1.0:
        return False
    nearest = (start[0] + t * dx, start[1] + t * dy)
    return ((point[0] - nearest[0]) ** 2 + (point[1] - nearest[1]) ** 2) ** 0.5 <= radius


def enter(
    host: str,
    port: int,
    account_id: int,
    key: str,
    character: str,
    timeout: float = 15.0,
    sheet: Character | None = None,
) -> tuple[Session, str, int, object]:
    """Leave the world session open. World drops the client, and its zone auth, when it closes."""
    opcodes = titanium_opcodes()
    session = Session()
    try:
        session.connect(host, port, timeout=min(timeout, 5.0))
        deadline = time.monotonic() + timeout
        info = login_info(account_id, key)
        session.send_app(struct.pack("<H", require(opcodes, "OP_SendLoginInfo")) + info)
        # World identifies Titanium from this packet, then sends char select.
        select = _wait_opcode(session, require(opcodes, "OP_SendCharInfo"), deadline)
        from eqclient.packets import character_by_name

        played = character_by_name(select, character)
        if played is None:
            select = _create_character(session, opcodes, character, deadline, sheet or build())
            played = character_by_name(select, character)
        session.send_app(struct.pack("<H", require(opcodes, "OP_EnterWorld")) + enter_world(character))
        zone = _wait_opcode(session, require(opcodes, "OP_ZoneServerInfo"), deadline)
        zone_host, zone_port = zone_server_info(zone)
        if not zone_host or zone_host == "0.0.0.0":
            zone_host = host
        if zone_port == 0:
            raise SessionError("world returned zone port 0")
        return session, zone_host, zone_port, played
    except Exception:
        session.close()
        raise


def rezone(
    host: str,
    port: int,
    account_id: int,
    key: str,
    character: str,
    timeout: float = 15.0,
) -> tuple[Session, str, int]:
    """World reconnect after a successful cross-zone OP_ZoneChange.

    LoginInfo.zoning=1 skips character select; world Clearance(1)s into the zone
    already saved by DoZoneSuccess / SetZone.
    """
    opcodes = titanium_opcodes()
    session = Session()
    try:
        session.connect(host, port, timeout=min(timeout, 5.0))
        deadline = time.monotonic() + timeout
        info = login_info(account_id, key, zoning=True)
        session.send_app(struct.pack("<H", require(opcodes, "OP_SendLoginInfo")) + info)
        enter_op = require(opcodes, "OP_EnterWorld")
        zsi_op = require(opcodes, "OP_ZoneServerInfo")
        # World may push OP_EnterWorld with the live name; wait briefly then answer.
        prompt_deadline = min(deadline, time.monotonic() + 2.0)
        while time.monotonic() < prompt_deadline:
            for packet in session.pump(0.2):
                got, _payload = _split(packet)
                if got == enter_op:
                    prompt_deadline = time.monotonic()
                    break
            else:
                continue
            break
        session.send_app(struct.pack("<H", enter_op) + enter_world(character))
        zone = _wait_opcode(session, zsi_op, deadline)
        zone_host, zone_port = zone_server_info(zone)
        if not zone_host or zone_host == "0.0.0.0":
            zone_host = host
        if zone_port == 0:
            raise SessionError("world returned zone port 0 after transfer")
        return session, zone_host, zone_port
    except Exception:
        session.close()
        raise


def _create_character(
    session: Session,
    opcodes: dict[str, int],
    name: str,
    deadline: float,
    sheet: Character,
) -> bytes:
    """Approve the name, then send this race and class. World replies with a fresh char select."""
    approve = require(opcodes, "OP_ApproveName")
    session.send_app(struct.pack("<H", approve) + name_approval(name, sheet.race, sheet.class_id))
    reply = _wait_opcode(session, approve, deadline)
    if not reply or reply[0] != 1:
        raise SessionError(f"world rejected the name {name!r}")
    created = char_create(sheet.class_id, sheet.race, sheet.gender, sheet.deity, sheet.start_zone, sheet.stats)
    session.send_app(struct.pack("<H", require(opcodes, "OP_CharacterCreate")) + created)
    select = _wait_opcode(session, require(opcodes, "OP_SendCharInfo"), deadline)
    if name not in character_select_names(select):
        raise SessionError(f"world did not list {name!r} after character create")
    return select


def _wait_opcode(session: Session, opcode: int, deadline: float) -> bytes:
    while time.monotonic() < deadline:
        for packet in session.pump(0.2):
            got, payload = _split(packet)
            if got == opcode:
                return payload
    raise SessionError(f"timed out waiting for world opcode {opcode:#06x}")


log = logging.getLogger("eqclient.world")


@dataclass
class Spawn:
    spawn_id: int
    name: str
    npc: int
    level: int
    body: int
    x: float
    y: float
    z: float
    class_id: int = 0
    race_id: int = 0


@dataclass
class Door:
    door_id: int
    name: str
    x: float
    y: float
    z: float
    opentype: int
    opened: bool = False
    tried: bool = False


@dataclass
class Ground:
    drop_id: int
    name: str
    x: float
    y: float
    z: float
    tried: bool = False


@dataclass
class ZoneModel:
    """Positions of everything the client can see, including this character.

    A step we send is only a prediction. OP_ClientUpdate for our spawn id,
    OP_RequestClientZoneChange, and OP_ZoneChange are the server's coordinates
    and replace that prediction.
    """

    character: str
    zone: str = ""
    changed_zone: bool = False
    spawns: dict[int, Spawn] = field(default_factory=dict)
    doors: dict[int, Door] = field(default_factory=dict)
    ground: dict[int, Ground] = field(default_factory=dict)
    last_seen: dict[str, tuple[str, float, float, float]] = field(default_factory=dict)
    faction: dict[int, int] = field(default_factory=dict)
    self_id: int = 0
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0
    have_position: bool = False
    server_position: bool = False
    moved_by_server: bool = False
    safe: tuple[float, float, float] = (0.0, 0.0, 0.0)
    sequence: int = 0
    step_origin: tuple[float, float, float] | None = None
    step_asked: tuple[float, float, float] | None = None
    step_sent_at: float = 0.0
    step_state: str = ""
    level: int = 0
    exp_bar: int = 0  # OP_ExpUpdate: 0–330 through the current level
    class_id: int = 1
    race_id: int = 1
    points: int = 0
    gender: int = 0
    deity: int = 0
    zone_id: int = 0
    home_zone_id: int = 0
    hp: int = 0
    max_hp: int = 0
    food: int = 127
    water: int = 127
    coin: int = 0  # carried copper (plat * 1000 + gold * 100 + silver * 10 + copper)
    coin_known: bool = False
    air: int = 60  # seconds of breath; refill on the surface
    mana: int = 0
    strength: int = 0
    stamina: int = 0
    agility: int = 0
    dexterity: int = 0
    wisdom: int = 0
    intelligence: int = 0
    charisma: int = 0
    needs_corpse: bool = False
    own_corpse_id: int = 0
    own_corpse_at: tuple[float, float, float] | None = None
    own_corpse_zone: str = ""
    own_corpse_count: int = 0
    own_corpse_missing: int = 0

    @property
    def position(self) -> tuple[float, float, float]:
        return (self.x, self.y, self.z)

    def predict(self, x: float, y: float, z: float) -> None:
        """Where we asked to stand. A later server update may confirm or refuse it."""
        self.x, self.y, self.z = x, y, z
        self.have_position = True
        self.server_position = False
        self._mirror_self()

    def clear_step(self) -> None:
        """Drop any in-flight ClientUpdate so a zone snap is not treated as a late echo."""
        self.step_origin = None
        self.step_asked = None
        self.step_sent_at = 0.0
        self.step_state = ""

    def reset_position(self, x: float, y: float, z: float) -> None:
        """Hard snap after zoning — no predict/step carryover from the previous zone."""
        self.clear_step()
        self.x, self.y, self.z = x, y, z
        self.have_position = True
        self.server_position = True
        self.moved_by_server = True
        self._mirror_self()

    def arm_step(self, origin: tuple[float, float, float], asked: tuple[float, float, float]) -> None:
        """One step is in flight. The next one waits until this one is settled."""
        self.step_origin = origin
        self.step_asked = asked
        self.step_sent_at = time.monotonic()
        self.step_state = "wait"

    def step_ready(self) -> bool:
        return self.step_state != "wait"

    def commit_step(self) -> None:
        """The server never answered. The point we asked for stands."""
        if self.step_state == "wait":
            self.step_state = "committed"

    def step_timed_out(self) -> bool:
        # ~one TICK — waiting 200ms capped us well under NPC chase speed outdoors.
        return self.step_state == "wait" and time.monotonic() - self.step_sent_at >= 0.1

    def apply_server_position(self, x: float, y: float, z: float) -> None:
        """The server's coordinates for this character.

        A packet from before this step, still sitting behind it, is not a
        correction. Accepting it is what walks him back to where he just was.
        """
        # Right after a zone hop, ignore origin junk (ZoneChange success zeros / bad spawn).
        ignore_until = float(getattr(self, "_ignore_origin_until", 0.0) or 0.0)
        if ignore_until and time.monotonic() < ignore_until:
            safe = self.safe
            if abs(x) + abs(y) < 1.0 and abs(safe[0]) + abs(safe[1]) > 50.0:
                return
        if self._drop_late_echo(x, y):
            return
        kind = self._echo_kind(x, y)
        if kind == "confirmed" and self.step_asked is not None and abs(z - self.step_asked[2]) > 6.0:
            z = self.step_asked[2]
        changed = self.have_position and (abs(self.x - x) > 0.5 or abs(self.y - y) > 0.5 or abs(self.z - z) > 0.5)
        self.x, self.y, self.z = x, y, z
        self.have_position = True
        self.server_position = True
        if kind == "refused":
            self.step_state = "refused"
            self.moved_by_server = True
        elif kind == "confirmed":
            self.step_state = "confirmed"
        elif changed:
            self.moved_by_server = True
        self._mirror_self()

    def _drop_late_echo(self, x: float, y: float) -> bool:
        origin, asked = self.step_origin, self.step_asked
        if origin is None or asked is None or not self.step_state:
            return False
        if _horiz_xy(self.x, self.y, x, y) > 40.0:
            return False
        if _horiz_xy(x, y, asked[0], asked[1]) <= 1.25:
            return False
        if _horiz_xy(x, y, origin[0], origin[1]) <= 0.8:
            age = time.monotonic() - self.step_sent_at
            return not (self.step_state == "wait" and age >= 0.12)
        return True

    def _echo_kind(self, x: float, y: float) -> str:
        origin, asked = self.step_origin, self.step_asked
        if self.step_state != "wait" or origin is None or asked is None:
            return ""
        if _horiz_xy(x, y, origin[0], origin[1]) <= 0.8:
            return "refused"
        if _horiz_xy(x, y, asked[0], asked[1]) <= 1.25:
            return "confirmed"
        return ""

    def _on_step(self, x: float, y: float) -> bool:
        origin, asked = self.step_origin, self.step_asked
        if origin is None or asked is None:
            return False
        dx, dy = asked[0] - origin[0], asked[1] - origin[1]
        length = dx * dx + dy * dy
        if length <= 1e-6:
            return False
        t = ((x - origin[0]) * dx + (y - origin[1]) * dy) / length
        if t <= 0.05 or t > 1.0:
            return False
        nearest_x = origin[0] + t * dx
        nearest_y = origin[1] + t * dy
        return _horiz_xy(x, y, nearest_x, nearest_y) <= 1.5

    def consume_server_move(self) -> bool:
        """True when a server packet moved us off the position we were using."""
        moved = self.moved_by_server
        self.moved_by_server = False
        return moved

    def next_sequence(self) -> int:
        self.sequence = (self.sequence + 1) & 0xFFFF
        return self.sequence

    def on_new_zone(self, payload: bytes) -> None:
        from eqclient.packets import new_zone, new_zone_id
        from eqclient.zones import remember, zone_id_of

        short, x, y, z = new_zone(payload)
        found = new_zone_id(payload) or zone_id_of(short)
        if found:
            self.zone_id = found
            remember(short, found)
        kept_corpse = (
            self.needs_corpse,
            self.own_corpse_id,
            self.own_corpse_at,
            self.own_corpse_zone,
            self.own_corpse_count,
            self.own_corpse_missing,
        )
        zone_changed = bool(self.zone) and short.lower() != self.zone.lower()
        if zone_changed:
            self.changed_zone = True
            self.spawns.clear()
            self.doors.clear()
            self.ground.clear()
            self.self_id = 0
        # Always restore corpse run across NewZone (same-zone death respawn included).
        if kept_corpse[0]:
            (
                self.needs_corpse,
                self.own_corpse_id,
                self.own_corpse_at,
                self.own_corpse_zone,
                self.own_corpse_count,
                self.own_corpse_missing,
            ) = kept_corpse
        self.zone = short
        self.safe = (x, y, z)
        # Always snap on NewZone — keeping the previous zone's predict causes MQWarp.
        if zone_changed or not self.have_position:
            self.reset_position(x, y, z)

    def on_spawns(self, payload: bytes) -> None:
        from eqclient.packets import SPAWN_SIZE, parse_spawn

        if not payload or len(payload) % SPAWN_SIZE:
            log.warning("spawn packet length %s is not a multiple of %s", len(payload), SPAWN_SIZE)
            return
        for offset in range(0, len(payload), SPAWN_SIZE):
            spawn_id, name, npc, level, body, x, y, z, class_id, race_id = parse_spawn(
                payload[offset : offset + SPAWN_SIZE]
            )
            self.spawns[spawn_id] = Spawn(spawn_id, name, npc, level, body, x, y, z, class_id, race_id)
            self.last_seen[name.lower()] = (self.zone, x, y, z)
            namel = name.lower()
            me = (self.character or "").lower()
            own_husk = me and (namel == me or namel.startswith(f"{me}'s corpse") or (me in namel and "corpse" in namel))
            # Bind id/coords only while a corpse run is already active — do not
            # start a new run from every leftover husk in the zone.
            if own_husk and npc in (2, 3) and self.needs_corpse:
                self._note_own_corpse(spawn_id, x, y, z)
            elif namel == me and npc not in (2, 3):
                self.self_id = spawn_id
                self.class_id = class_id or self.class_id
                self.race_id = race_id or self.race_id
                if self.level == 0:
                    self.level = level
                self.apply_server_position(x, y, z)

    def on_delete_spawn(self, payload: bytes) -> int:
        if len(payload) < 4:
            return 0
        spawn_id = struct.unpack_from("<I", payload)[0]
        spawn = self.spawns.pop(spawn_id, None)
        if spawn is not None:
            self.last_seen[spawn.name.lower()] = (self.zone, spawn.x, spawn.y, spawn.z)
        self.faction.pop(spawn_id, None)
        return spawn_id

    def on_doors(self, payload: bytes) -> None:
        from eqclient.packets import DOOR_SIZE, parse_door

        if not payload or len(payload) % DOOR_SIZE:
            log.warning("door packet length %s is not a multiple of %s", len(payload), DOOR_SIZE)
            return
        for offset in range(0, len(payload), DOOR_SIZE):
            door_id, name, x, y, z, opentype = parse_door(payload[offset : offset + DOOR_SIZE])
            previous = self.doors.get(door_id)
            door = Door(door_id, name, x, y, z, opentype)
            if previous is not None:
                door.opened = previous.opened
                door.tried = previous.tried
            self.doors[door_id] = door

    def on_ground(self, payload: bytes) -> None:
        from eqclient.packets import parse_ground

        try:
            drop_id, name, x, y, z = parse_ground(payload)
        except ValueError as exc:
            log.warning("%s", exc)
            return
        self.ground[drop_id] = Ground(drop_id, name, x, y, z)

    def on_click_object(self, payload: bytes) -> None:
        if len(payload) < 8:
            return
        drop_id, player_id = struct.unpack_from("<II", payload)
        if player_id == 0:
            self.ground.pop(drop_id, None)

    def on_client_update(self, payload: bytes) -> None:
        from eqclient.packets import server_position

        try:
            spawn_id, x, y, z = server_position(payload)
        except ValueError as exc:
            log.warning("%s", exc)
            return
        if self._is_self(spawn_id):
            self.self_id = spawn_id or self.self_id
            self.apply_server_position(x, y, z)
            return
        spawn = self.spawns.get(spawn_id)
        if spawn is not None:
            spawn.x, spawn.y, spawn.z = x, y, z
            self.last_seen[spawn.name.lower()] = (self.zone, x, y, z)

    def on_request_zone_change(self, payload: bytes) -> None:
        from eqclient.packets import request_zone_change

        from eqclient.zones import zone_name_of

        zone_id, x, y, z = request_zone_change(payload)
        if zone_id and zone_id != self.zone_id:
            self.changed_zone = True
            self.zone_id = zone_id
            known = zone_name_of(zone_id)
            # Same wipe as OP_NewZone — otherwise we keep the old zone's doors/spawns
            # and never reload water/nav until the next full login.
            if known and known.lower() != (self.zone or "").lower():
                self.spawns.clear()
                self.doors.clear()
                self.ground.clear()
                self.self_id = 0
                self.zone = known
                self.reset_position(x, y, z)
                return
        self.clear_step()
        self.apply_server_position(x, y, z)

    def on_zone_change(self, payload: bytes) -> bool:
        """Apply an in-zone cancel / MovePC. Returns True when the client must rezone."""
        from eqclient.packets import zone_change
        from eqclient.zones import zone_name_of

        zone_id, _instance_id, x, y, z, success = zone_change(payload)
        if success == 1 and zone_id and zone_id != self.zone_id:
            known = zone_name_of(zone_id) or str(zone_id)
            print(
                f"OP_ZoneChange success → {known} " f"from={self.zone or self.zone_id} pos=({x:.0f},{y:.0f},{z:.0f})",
                flush=True,
            )
            # Keep self.zone as the egress short name until OP_NewZone wipes spawns.
            # Do NOT snap to packet xyz — Titanium ZTZ success leaves x/y/z as 0,0,0
            # and applying that poisons the next zone (walk from origin, z=0 forever).
            self.zone_id = zone_id
            self.changed_zone = True
            self.clear_step()
            return True
        if success != 1:
            print(f"OP_ZoneChange rejected success={success} zone={zone_id}", flush=True)
        # Cancel / same-zone success — snap where the server put us.
        self.reset_position(x, y, z)
        return False

    def on_become_corpse(self, payload: bytes) -> None:
        """OP_BecomeCorpse. Floats are y, x, z. That spawn is now a corpse at the server's spot."""
        if len(payload) < 16:
            return
        spawn_id, y, x, z = struct.unpack_from("<Ifff", payload)
        if spawn_id == self.self_id or spawn_id == 0:
            # This is where we fell. The lootable body arrives as its own spawn.
            self.needs_corpse = True
            self.own_corpse_at = (x, y, z)
            self.own_corpse_zone = self.zone
            return
        spawn = self.spawns.get(spawn_id)
        if spawn is None:
            return
        spawn.npc = 3
        spawn.x, spawn.y, spawn.z = x, y, z
        self.last_seen[spawn.name.lower()] = (self.zone, x, y, z)

    def on_death(self, payload: bytes) -> bool:
        """True when this death is ours. The body is back where we fell."""
        if len(payload) < 4:
            return False
        spawn_id = struct.unpack_from("<I", payload)[0]
        if spawn_id not in (self.self_id, 0):
            return False
        self.needs_corpse = True
        self.own_corpse_zone = self.zone
        self.own_corpse_count = 0
        self.own_corpse_missing = 0
        if self.own_corpse_at is None:
            self.own_corpse_at = self.position
        return True

    def grant_levels(self, level: int, old: int) -> None:
        """Five skill points per level gained. The trainer spends them."""
        if level > old:
            self.points += 5 * (level - old)
        if level > self.level:
            self.level = level

    def set_coin(self, platinum: int, gold: int, silver: int, copper: int) -> None:
        """Carried coin, in copper. One platinum is 1000."""
        self.coin = platinum * 1000 + gold * 100 + silver * 10 + copper
        self.coin_known = True

    def add_coin(self, platinum: int, gold: int, silver: int, copper: int) -> int:
        """Add corpse cash (already granted by the server). Returns copper gained."""
        gained = platinum * 1000 + gold * 100 + silver * 10 + copper
        if gained <= 0:
            return 0
        self.coin = (self.coin if self.coin_known else 0) + gained
        self.coin_known = True
        return gained

    def coin_line(self) -> str:
        """Human purse line from tracked copper (empty until first profile/update)."""
        if not self.coin_known:
            return "coin unknown"
        total = max(0, int(self.coin))
        plat, rem = divmod(total, 1000)
        gold, rem = divmod(rem, 100)
        silver, copper = divmod(rem, 10)
        return f"coin {plat}p {gold}g {silver}s {copper}c ({total})"

    def _note_own_corpse(self, spawn_id: int, x: float, y: float, z: float) -> None:
        self.needs_corpse = True
        self.own_corpse_id = spawn_id
        self.own_corpse_at = (x, y, z)
        self.own_corpse_zone = self.zone

    def note_corpse_contents(self, found: int, missing: int) -> None:
        """found is the number of items the window listed. missing is how many are not back yet."""
        self.own_corpse_count = found
        self.own_corpse_missing = missing
        if missing == 0:
            self.corpse_reclaimed()

    def apply_played(self, played) -> None:
        """Char select, then the profile, replace whatever the creation sheet guessed."""
        if played.name:
            self.character = played.name
        self.race_id = played.race or self.race_id
        self.class_id = played.class_id or self.class_id
        self.level = played.level or self.level
        self.gender = played.gender
        self.deity = played.deity
        self.zone_id = played.zone_id or self.zone_id
        if played.home_zone_id:
            self.home_zone_id = played.home_zone_id
        if getattr(played, "coin_known", False):
            self.set_coin(played.platinum, played.gold, played.silver, played.copper)
        if played.points:
            self.points = played.points
        if played.hp:
            self.hp = played.hp
        if played.mana:
            self.mana = played.mana
        if played.strength:
            self.strength = played.strength
            self.stamina = played.stamina
            self.agility = played.agility
            self.dexterity = played.dexterity
            self.wisdom = played.wisdom
            self.intelligence = played.intelligence
            self.charisma = played.charisma

    def needs_rest(self, sitting: bool) -> bool:
        """Sit at healrotation critical (50%); stay down until nearly full.

        Zero HP means the bar is unknown or he is dead — do not sit for that.
        """
        if self.max_hp <= 0 or self.hp <= 0:
            return False
        ratio = self.hp / self.max_hp
        if sitting:
            return ratio < 0.9
        return ratio <= 0.50

    def corpse_reclaimed(self) -> None:
        self.needs_corpse = False
        self.own_corpse_id = 0
        self.own_corpse_at = None
        self.own_corpse_zone = ""
        self.own_corpse_count = 0
        self.own_corpse_missing = 0

    def on_consider(self, payload: bytes) -> None:
        from eqclient.packets import consider_faction

        if len(payload) < 8:
            return
        target = struct.unpack_from("<I", payload, 4)[0]
        self.faction[target] = consider_faction(payload)

    def on_move_door(self, payload: bytes) -> int:
        if not payload:
            return 0
        door_id = payload[0]
        door = self.doors.get(door_id)
        if door is not None:
            door.opened = True
        return door_id

    def _is_self(self, spawn_id: int) -> bool:
        if spawn_id and spawn_id == self.self_id:
            return True
        spawn = self.spawns.get(spawn_id)
        return bool(spawn and spawn.name.lower() == self.character.lower())

    def _mirror_self(self) -> None:
        spawn = self.spawns.get(self.self_id)
        if spawn is not None:
            spawn.x, spawn.y, spawn.z = self.x, self.y, self.z
