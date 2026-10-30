"""One pulse. Pump, publish, step the winner, flush.

A pulse is 0.1 seconds. yielding ends the pulse. A higher band appended by the
step itself is stepped once in that same pulse. send queues until after the step.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Protocol, runtime_checkable

if TYPE_CHECKING:
    from collections.abc import Iterator
    from eqclient3.action import Action
    from eqclient3.bus import Bus
    from eqclient3.schedule import Schedule

from .actions.support import character_name
from .net.sheet import Character as Creation
from .journal import Journal
from .log import log
from .trace import note_opcode
from .world import World
from . import net
from .net.client import Client, Login
from .net.session import Session, SessionError

PULSE = 0.1
_HEARD = ("OP_ChannelMessage", "OP_SpecialMesg", "OP_SimpleMessage")


def _hear_waiting(queue: Schedule, loop: Loop, world: World) -> None:
    """A line that names work is heard on the pulse it arrives.

    ReadTasks stays in the queue while a same-band step is the winner. The
    mailbox already holds the parsed line. Hearing it here appends the work
    without waiting for that action to win the band.
    """
    for action in list(queue):
        if not action.messages:
            continue
        if any(message.opcode in _HEARD for message in action.messages):
            action._hear(loop, world)


class ScriptedSession:
    """A test socket. pump returns scripted packets. send records loop.send."""

    def __init__(self, packets: tuple[object, ...] = ()) -> None:
        self.packets = list(packets)
        self.sent: list[tuple] = []
        self.closed = False
        self.needs_rezone = False
        self.open = True
        self.connected = True
        self.client: Client | None = None
        self.decode = None
        self.transfers = 0

    def pump(self, timeout: float = 0.0) -> list:
        found = list(self.packets)
        self.packets.clear()
        return found

    def send(self, opcode: str, payload: object | None = None) -> None:
        self.sent.append((opcode, payload))

    def transfer_zone(self) -> None:
        self.transfers += 1


class Loop:

    def __init__(self) -> None:
        self.outbound: list[tuple[str, object | None]] = []
        self.flushed: list[tuple[str, object | None]] = []
        self.queue: Schedule | None = None
        self.world: World | None = None
        self.session: Client | Session | ScriptedSession | None = None
        self.journal: Journal | None = None
        self.character: str = ""
        self.tick: int = 0
        self.sent_count: int = 0
        self.recv_count: int = 0
        self.closed: bool = False
        self.client: Client | Login | None = None
        self.active: Action | None = None
        self.action: Action | None = None
        self.current: Action | None = None
        self.head: Action | None = None
        self.produce: object | None = None
        self.assign: object | None = None
        self._transferred = False

    def send(self, opcode: str, payload: object | None = None) -> None:
        """Queue one outbound. The pulse flushes the list after step."""
        self.outbound.append((opcode, payload))

    @property
    def sent(self) -> list[tuple]:
        return self.outbound

    def append(self, action: Action) -> bool:
        """Queue an action from a handler. Stamps insert, started, and zone."""
        queue = self.queue
        world = self.world
        if queue is None or world is None:
            return False
        return bool(queue.append(action, world, self.journal, self.character))

    def run_once(
        self,
        session: Client | Session | ScriptedSession,
        world: World,
        queue: Schedule,
        bus: Bus,
    ) -> Action | None:
        """Step the winner once, including while it is waiting. Returns that action."""
        self.queue = queue
        self.world = world
        self.session = session
        self.tick += 1
        world.movement.bind(world)
        if session is not None and (not _session_closed(session)):
            self._transferred = False
        bus.queue = queue
        bus.loop = self
        bus.world = world
        for opcode, payload in _incoming(session):
            self.recv_count += 1
            bus.publish(opcode, payload)
        _hear_waiting(queue, self, world)
        winner = queue.head()
        if winner is None:
            self._note(None)
            self._finish(session, world)
            return None
        self._note(winner)
        self._step(winner, world)
        if winner.yielding:
            if winner.completed:
                self._drop(winner)
            else:
                winner.suspend()
            self._finish(session, world)
            return winner
        if winner.completed:
            self._drop(winner)
            self._finish(session, world)
            return winner
        nxt = queue.winner()
        if nxt is not None and nxt is not winner and (nxt.priority > winner.priority):
            winner.suspend()
            self._note(nxt)
            self._step(nxt, world)
            if nxt.completed:
                self._drop(nxt)
            elif nxt.yielding:
                nxt.suspend()
            self._finish(session, world)
            return nxt
        self._finish(session, world)
        return winner

    def start(
        self,
        connection: Login | Client | None,
        sheet: World | Creation | str,
        queue: Schedule,
        journal: Journal | None = None,
    ) -> Client | Login | None:
        """Create journal tables, reload open actions, then connect when net exists.

        A closed session calls transfer_zone and does not send a zone request.
        connection None reloads the journal and does not open a socket.
        """
        self.queue = queue
        self.character = _character_name(sheet)
        self.journal = journal or Journal(character=self.character)
        queue.bind(self.journal, self.character)
        if self.character:
            for action in self.journal.load_actions(self.character):
                queue.restore(action)

        if connection is None:
            return None

        if isinstance(connection, Client) and (connection.closed or connection.needs_rezone):
            transfer_zone(connection)
            return connection

        creation = sheet if isinstance(sheet, Creation) else None
        record: Login | dict[str, object] | None
        if isinstance(connection, Login):
            record = connection
        elif isinstance(connection, dict):
            record = connection
        else:
            record = None
        session = net.connect(record, creation)
        return net.enter(session, creation)

    def _note(self, action: Action | None) -> None:
        """Remember the action this pulse is stepping, and log when it changes."""
        if action is self.active:
            return
        previous = self.active
        self.active = action
        self.current = action
        self.head = action
        log.info("action %s -> %s", _action_label(previous), _action_label(action))

    def _step(self, action: Action, world: World) -> None:
        action.yielding = False
        action.step(self, world)

    def _drop(self, action: Action) -> None:
        queue = self.queue
        if queue is None:
            return
        queue.remove(action.insert)
        journal = self.journal
        if journal is None or not self.character or (not action.source):
            return
        journal.resolve_action(self.character, action)

    def _finish(self, session: Client | Session | ScriptedSession, world: World) -> None:
        self._hold(world)
        self._flush(session)
        self._report(world)

    def _hold(self, world: World) -> None:
        """One hold update after the step, unless this pulse already advanced.

        When this pulse already called advance, hold_if_idle sends nothing.
        """
        world.movement.hold_if_idle(self, world)

    def _flush(self, session: Client | Session | ScriptedSession) -> None:
        batch = list(self.outbound)
        self.outbound.clear()
        if _session_closed(session):
            self.flushed = []
            self._transfer_once(session)
            return
        self.flushed = batch
        for opcode, payload in batch:
            try:
                note_opcode(opcode, payload, True)
                _send(session, opcode, payload)
            except SessionError:
                point = _position(self.world)
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
                self._transfer_once(session)
                return
            self.sent_count += 1

    def _report(self, world: World) -> None:
        """World position, packet counts, and the active wait list, once every 20 pulses."""
        if self.tick % 20:
            return
        point = _position(world)
        log.info(
            "cycle %s %s waiting=%s pos (%.1f, %.1f, %.1f) sent=%s recv=%s",
            self.tick,
            _action_name(self.active),
            _wait_list(self.active),
            point[0],
            point[1],
            point[2],
            self.sent_count,
            self.recv_count,
        )

    def _transfer_once(self, session: Client | Session | ScriptedSession) -> None:
        if self._transferred:
            return
        self._transferred = True
        transfer_zone(session)


def run_once(session: Client | Session | ScriptedSession, world: World, queue: Schedule, bus: Bus) -> Action | None:
    """One pulse on a fresh loop. Keep a Loop when ticks must accumulate."""
    return Loop().run_once(session, world, queue, bus)


def connect(connection: Login, sheet: Creation | None = None) -> Client:
    """Login. eqclient3.net.connect implements this."""
    return net.connect(connection, sheet)


def enter(session: Client, sheet: Creation | None = None) -> Client:
    """OP_SendLoginInfo through zone-in. eqclient3.net.enter implements this."""
    return net.enter(session, sheet)


def transfer_zone(session: Client | Session | ScriptedSession, *args: object, **kwargs: object) -> Client | None:
    """Closed session or a reliable-stream hole. Does not send a zone request.

    eqclient3.net.transfer_zone implements the reconnect.
    """
    return net.transfer_zone(session, *args, **kwargs)


def _position(world: World | None) -> tuple[float, float, float]:
    if world is None:
        return (0.0, 0.0, 0.0)
    point = world.position
    return (float(point[0]), float(point[1]), float(point[2]))


def _wait_list(action: Action | None) -> str:
    if action is None:
        return "[]"
    return "[" + action.wait_label() + "]"


def _action_name(action: Action | None) -> str:
    if action is None:
        return "idle"
    kind = type(action).__name__
    source = action.source
    return kind if not source else f"{kind} {source}"


def _action_label(action: Action | None) -> str:
    label = _action_name(action)
    if action is not None and action.waiting:
        label = f"{label} wait={action.wait_label()}"
    return label


def _session_closed(session: Client | Session | ScriptedSession) -> bool:
    return session.closed or session.needs_rezone


@runtime_checkable
class _Sender(Protocol):
    def send(self, opcode: str, payload: object | None = None) -> None: ...


def _send(session: Client | Session | ScriptedSession, opcode: str, payload: object | None) -> None:
    if isinstance(session, Client):
        if isinstance(payload, (bytes, bytearray)):
            session.send(opcode, bytes(payload))
        return
    if isinstance(session, _Sender):
        session.send(opcode, payload)


def _incoming(session: Client | Session | ScriptedSession) -> Iterator[tuple[str, object]]:
    for packet in session.pump(PULSE):
        named = _named(session, packet)
        if named is not None:
            yield named


def _named(session: Client | Session | ScriptedSession, packet: object) -> tuple[str, object] | None:
    """A pump item is (opcode, payload), or session.decode(packet) returns that pair."""
    if isinstance(packet, tuple) and len(packet) >= 2 and isinstance(packet[0], str):
        return (packet[0], packet[1])
    if not isinstance(session, ScriptedSession) or session.decode is None:
        return None
    decoder = session.decode
    if not callable(decoder):
        return None
    named = decoder(packet)
    if isinstance(named, tuple) and len(named) >= 2 and isinstance(named[0], str):
        return (named[0], named[1])
    return None


def _character_name(sheet: World | Creation | str | None) -> str:
    if isinstance(sheet, str):
        return sheet
    if isinstance(sheet, World):
        return character_name(None, sheet)
    if sheet is None:
        return ""
    return sheet.name
