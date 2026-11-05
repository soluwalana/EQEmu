import re
import time
import types
from collections.abc import Callable, Iterator
from dataclasses import replace

from eqclient4.action import Action
from eqclient4.bus import Bus
from eqclient4.journal import Journal
from eqclient4.log import log, note_comms, open_capture
from eqclient4.nav.maps import load_map
from eqclient4.nav.navmesh import load_nav
from eqclient4.nav.travel import ensure_zone_graph
from eqclient4.nav.water import load_water
from eqclient4.nav.zones import zone_name_of
from eqclient4.net import transfer_zone
from eqclient4.net.client import Client, Login, connect, enter
from eqclient4.net.session import SessionError
from eqclient4.net.sheet import CreateCharacter
from eqclient4.structs import EQStruct, OP_NewZone
from eqclient4.world import World

PULSE = 0.1


class Schedule:

    def __init__(self, world: World, journal: Journal, character: str) -> None:
        self.world = world
        self._next = 0
        self._actions: list = []
        self.journal: Journal = journal
        self.character = character

    def __iter__(self) -> Iterator[Action]:
        return iter(list(self._actions))

    def __len__(self) -> int:
        return len(self._actions)

    def __getitem__(self, index: int) -> Action:
        return self._actions[index]

    def has_source(self, source: str) -> bool:
        if not source:
            return False
        return any((action.source == source for action in self._actions))

    def append(
        self,
        action: Action,
    ) -> bool:
        """Stamp insert, started, and zone. A known source is not queued twice.

        A source already on this queue, or already resolved in the journal, is
        refused. An empty source is always queued and is not written to the journal.
        """
        source = str(action.source or "")
        if source:
            if self.has_source(source):
                return False
            if self.journal.is_resolved(source):
                return False
            if self.journal.is_open(source):
                return False
        self._next += 1
        action.insert = self._next
        action.started = time.time()
        action.zone = str(self.world.zone or "")
        action._world = self.world
        if source and not self.journal.open_action(action):
            return False
        self._actions.append(action)
        return True

    def source_open(self, source: str) -> bool:
        return any(action.source == source and not action.completed for action in self._actions)

    def source_resolved(self, source: str) -> bool:
        return self.journal.resolved(source)

    def enqueue_once(self, action: Action, source: str) -> Action | None:
        """Append when this source is neither open nor already resolved."""
        if self.source_open(source) or self.source_resolved(source):
            return None

        action.source = source
        if not action.zone:
            action.zone = self.world.zone or ""
        action._world = self.world

        self.append(action)
        return action

    def restore(self, action: Action) -> bool:
        """Put a journal row back. Keeps zone and started. Stamps insert when it is 0."""
        source = str(action.source or "")
        if source and self.has_source(source):
            return False
        if action.insert:
            self._next = max(self._next, int(action.insert))
        else:
            self._next += 1
            action.insert = self._next
        if not action.started:
            action.started = time.time()
        self._actions.append(action)
        return True

    def remove(self, insert: int) -> None:
        self._actions = [action for action in self._actions if action.insert != insert]

    def winner(self) -> Action | None:
        if not self._actions:
            return None
        return min(
            self._actions,
            key=lambda action: (-action.priority, type(action).key(action)),
        )

    def suspend_loser(self, winner: Action | None) -> None:
        """A higher band suspends the action that was running. The subject stays."""
        if winner is None:
            return
        for action in self._actions:
            if action is winner or action.suspended:
                continue
            if winner.priority > action.priority:
                action.suspend()

    def head(self) -> Action | None:
        chosen = self.winner()
        self.suspend_loser(chosen)
        return chosen


class Loop:

    def __init__(self, world: World, login: Login, creation: CreateCharacter) -> None:
        self.world = world
        self.character = creation.name
        self.journal: Journal = Journal(self.character, self.world)
        self.queue = Schedule(self.world, self.journal, self.character)
        self.bus = Bus(self.queue, self.world, self)
        self.login = login
        self.creation = creation

        self.client = self.start(login, creation)
        if not self.client:
            raise ConnectionError("Failed to create client")

        self.outbound: list[tuple[str, EQStruct | bytes]] = []
        self.flushed: list[tuple[str, EQStruct | bytes]] = []
        self.capture = open_capture(self.character)

        self.active: Action | None = None

        self.sent_count: int = 0
        self.recv_count: int = 0
        self.closed: bool = False

        self.tick: int = 0
        self._status = ""

    def start(self, login: Login, creation: CreateCharacter) -> Client:
        for action in self.journal.load_actions():
            self.queue.restore(action)

        session = connect(login, creation)
        if not session:
            raise ConnectionError("Failed to connect to server")

        client = enter(session, creation)
        if not client:
            raise ConnectionError("Failed to enter server")

        return client

    def send(self, opcode: str, payload: EQStruct | bytes) -> None:
        """Queue one outbound. The pulse flushes the list after step."""
        self.outbound.append((opcode, payload))

    def append(self, action: Action) -> bool:
        """Queue an action from a handler. Stamps insert, started, and zone."""
        return bool(self.queue.append(action))

    @property
    def sent(self) -> list[tuple]:
        return self.outbound

    def warm(self) -> None:
        """Read zone files and the quest graph before the first pulse.

        Pathing and line of sight otherwise decompress those files on the pulse that
        should be sending movement.
        """
        zone = self._inbox_zone() or self.world.zone or None
        if not zone and self.client.played:
            zone = zone_name_of(self.client.played.zone_id)

        if zone:
            self.world.zone = zone
            nav = _quiet(load_nav, zone)
            water = _quiet(load_water, zone)
            zone_map = _quiet(load_map, zone)
            log.info(
                f"loaded {zone} nav={nav} water={water} map={zone_map}",
            )

        graph = self.world.zone_graph
        self.world.exit_doors = graph.doors

        edges = len(graph.edges)
        log.info(
            "loaded quest graph edges=%s zones=%s transits=%s exits=%s",
            edges,
            len(self.world.zone_graph.zones),
            len(self.world.zone_graph.transits),
            len(self.world.exit_doors),
        )

    def play(self) -> None:
        """One Loop for the whole session. Each pulse pumps, steps, and flushes."""
        self.client.start_io()
        try:
            while True:
                self.run_once()
                if not self.client.closed:
                    continue
                # The disconnect often arrives after this pulse already flushed.
                # The next pulse is the one that reconnects. Still closed after that
                # means the new session did not come up.
                self.run_once()
                if self.client.closed:
                    log.info("session closed")
                    break
        except KeyboardInterrupt:
            return
        finally:
            self.capture.close()
            self.client.close()

    def session_open(self) -> bool:
        return not self.client.closed and not self.client.needs_rezone

    def run_once(self) -> Action | None:
        """Step the winner once, including while it is waiting. Returns that action."""
        self.tick += 1

        if self.session_open():
            self._transferred = False

        for packet in self.client.pump(PULSE):
            match packet:
                case (str() as opcode, bytes() as payload):
                    self.recv_count += 1
                    self.capture.record("recv", opcode, payload)
                    self.bus.publish(opcode, payload)
                case _:
                    log.error("unknown packet: %s", packet)
                    raise RuntimeError("unknown packet")

        winner = self.queue.head()
        if winner is None:
            self._note(None)
            self._finish()
            return None

        self._note(winner)
        winner.yielding = False
        winner.step()

        self._note(winner)
        if winner.yielding:
            if winner.completed:
                self.drop(winner)
            else:
                winner.suspend()
            self._finish()
            return winner

        if winner.completed:
            self.drop(winner)
            self._finish()
            return winner

        nxt = self.queue.winner()
        if nxt and nxt != winner and (nxt.priority > winner.priority):
            winner.suspend()

            self._note(nxt)
            nxt.yielding = False
            nxt.step()

            self._note(nxt)
            if nxt.completed:
                self.drop(nxt)
            elif nxt.yielding:
                nxt.suspend()
            self._finish()
            return nxt
        self._finish()
        return winner

    def drop(self, action: Action) -> None:
        queue = self.queue
        queue.remove(action.insert)

        if not action.source:
            return
        self.journal.resolve_action(action)

    def forget(self, action: Action) -> None:
        # Drop an action without resolving it, so a later step can queue it again.
        if action.insert:
            self.queue.remove(action.insert)

        if action.source:
            self.journal.clear_source(action.source)

    def _inbox_zone(self) -> str:
        number = self.client.opcodes.get("OP_NewZone", 0)
        if not number:
            return ""
        for opcode, payload in self.client._inbox:
            if opcode != number:
                continue
            try:
                short = OP_NewZone.deserialize(payload).short_name
            except ValueError:
                log.error("new zone packet failed to parse", exc_info=True)
                continue
            if short:
                return short
        return ""

    def _finish(self) -> None:
        self.world.movement.hold_if_idle(self)
        self._flush()
        self._report()
        self.capture.commit()

    def _flush(self) -> None:
        batch = list(self.outbound)
        self.outbound.clear()
        if self.client.closed or self.client.needs_rezone:
            self.flushed = []
            self._transfer_once()
            return
        self.flushed = batch
        for opcode, payload in batch:
            try:
                if isinstance(payload, EQStruct):
                    serialized = payload.serialize()
                else:
                    serialized = payload
                note_comms("outbound loop", opcode, payload, True)
                self.client.send(opcode, serialized)
                self.capture.record("send", opcode, serialized)
            except SessionError:
                point = self.world.position
                log.info(
                    "zone socket closed sending %s pos (%.1f, %.1f, %.1f) sent=%s recv=%s",
                    opcode,
                    point[0],
                    point[1],
                    point[2],
                    self.sent_count,
                    self.recv_count,
                )
                self.flushed = []
                self._transfer_once()
                return
            self.sent_count += 1

    def _report(self) -> None:
        """World position, packet counts, and the active wait list, once every 20 pulses."""
        if self.tick % 20:
            return
        point = self.world.position
        wait_list = self.active.wait_label() if self.active else "[]"
        log.info(
            "cycle %s %s waiting=%s pos (%.1f, %.1f, %.1f) sent=%s recv=%s%s",
            self.tick,
            self._action_name(self.active),
            wait_list,
            point[0],
            point[1],
            point[2],
            self.sent_count,
            self.recv_count,
            self._target_note(self.active),
        )

    def _transfer_once(self) -> None:
        if self._transferred:
            return

        self._transferred = True

        # The zone-in that follows is a new entrance. A same-zone weather refresh
        # does not come through here, so the party has to be built again.
        self.world.zone_formed = None
        transfer_zone(self.client)

    def _note(self, action: Action | None) -> None:
        """Remember the action this pulse is stepping, and log when it changes.

        A change is a different action, or the same action moving to a new wait.
        """
        label = self._action_label(action)
        if action is self.active and label == self._status:
            return
        previous = self._status or self._action_label(self.active)
        self.active = action
        self.current = action
        self.head = action
        self._status = label
        log.info("action %s -> %s", previous, label)

    def _action_name(self, action: Action | None) -> str:
        if action is None:
            return "idle"
        kind = type(action).__name__
        source = action.source
        base = kind if not source else f"{kind} {source}"
        named = self._item_suffix(action)
        return base if not named else f"{base} {named}"

    def _action_label(self, action: Action | None) -> str:
        label = self._action_name(action)
        if action is not None and action.waiting:
            label = f"{label} wait={action.wait_label()}"
        return label

    def _item_suffix(self, action: Action) -> str:
        """Cache name and item number for each item this action is working on.

        A cursor line also names the item sitting on each slot of the move.
        """
        parts: list[str] = []
        source = action.source or ""
        for item_id in _item_ids(action):
            parts.append(self._named_item(item_id, source))
        return " ".join(part for part in parts if part)

    def _named_item(self, item_id: int, source: str) -> str:
        row = self.world.item_book.get(item_id)
        name = row.name if row else ""
        if name:
            return f"{name} ({item_id})"
        if f":{item_id}" in source or f"={item_id}" in source:
            return ""
        return f"({item_id})"

    def _target_note(self, action: Action | None) -> str:
        """Distance and hit points for the spawn an Attack is standing on."""
        if action is None or type(action).__name__ != "Attack":
            return ""
        spawn = action.spawn_id or 0
        mob = self.world.mobs.get(spawn)
        if mob is None:
            return f" target={spawn} missing"
        return f" target={mob.spoken_name()} d={mob.distance:.0f} hp={mob.hp}"


def _quiet[T](load: Callable[[str], T], zone: str) -> T | None:
    try:
        return load(zone)
    except (OSError, ValueError):
        name = load.__name__ if isinstance(load, types.FunctionType) else "map"
        log.error("%s failed to load for %s", name, zone, exc_info=True)
        return None


_ITEM_KEY = re.compile(r"(?:fetch|trade|sell|camp):(\d+(?:,\d+)*)|item=(\d+)|distribute:[^:#\s]+:(\d+)")


def _item_ids(action: Action) -> list[int]:
    found: list[int] = []
    if action.item_id:
        found.append(action.item_id)
    if hasattr(action, "item") and action.item and action.item not in found:
        found.append(action.item)
    if hasattr(action, "item_ids") and action.item_ids:
        for item_id in action.item_ids:
            if item_id and item_id not in found:
                found.append(item_id)
    for match in _ITEM_KEY.finditer(action.source or ""):
        raw = match.group(1) or match.group(2) or match.group(3) or ""
        for part in raw.split(","):
            if not part.isdigit():
                continue
            item_id = int(part)
            if item_id not in found:
                found.append(item_id)
    return found
