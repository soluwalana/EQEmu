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
        if door.tried and door.opentype == 5:
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
    level: int = 0
    class_id: int = 1
    race_id: int = 1
    points: int = 0
    gender: int = 0
    deity: int = 0
    zone_id: int = 0
    hp: int = 0
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
        """Where we asked to stand. The next server update for us overwrites this."""
        self.x, self.y, self.z = x, y, z
        self.have_position = True
        self.server_position = False
        self._mirror_self()

    def apply_server_position(self, x: float, y: float, z: float) -> None:
        """The server's coordinates for this character."""
        changed = self.have_position and (
            abs(self.x - x) > 0.5 or abs(self.y - y) > 0.5 or abs(self.z - z) > 0.5
        )
        self.x, self.y, self.z = x, y, z
        self.have_position = True
        self.server_position = True
        if changed:
            self.moved_by_server = True
        self._mirror_self()

    def consume_server_move(self) -> bool:
        """True when a server packet moved us off the position we were using."""
        moved = self.moved_by_server
        self.moved_by_server = False
        return moved

    def next_sequence(self) -> int:
        self.sequence = (self.sequence + 1) & 0xFFFF
        return self.sequence

    def on_new_zone(self, payload: bytes) -> None:
        from eqclient.packets import new_zone

        short, x, y, z = new_zone(payload)
        if self.zone and short.lower() != self.zone.lower():
            self.changed_zone = True
            self.spawns.clear()
            self.doors.clear()
            self.ground.clear()
            self.self_id = 0
            self.have_position = False
            self.needs_corpse = False
            self.own_corpse_id = 0
            self.own_corpse_at = None
            self.own_corpse_count = 0
            self.own_corpse_missing = 0
        self.zone = short
        self.safe = (x, y, z)
        if not self.have_position:
            self.x, self.y, self.z = x, y, z
            self.have_position = True

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
            if name.lower() == self.character.lower() and npc == 2:
                self._note_own_corpse(spawn_id, x, y, z)
            elif name.lower() == self.character.lower():
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

        _zone_id, x, y, z = request_zone_change(payload)
        self.apply_server_position(x, y, z)

    def on_zone_change(self, payload: bytes) -> None:
        from eqclient.packets import zone_change_position

        x, y, z = zone_change_position(payload)
        self.apply_server_position(x, y, z)

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

    def corpse_reclaimed(self) -> None:
        self.needs_corpse = False
        self.own_corpse_id = 0
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
