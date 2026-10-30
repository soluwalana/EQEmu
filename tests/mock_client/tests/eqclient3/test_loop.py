"""Loop pulse: yield, a higher band, a closed session, and the bus."""

import logging

from eqclient3.action import Action
from eqclient3.bus import Bus
from eqclient3.handler import Handler
from eqclient3.journal import Journal
from eqclient3.loop import PULSE, Loop
from eqclient3.schedule import Schedule
from eqclient3.structs import OP_Assist
from eqclient3.world import World


class Session:
    def __init__(self, packets=()):
        self.packets = list(packets)
        self.sent = []
        self.closed = False
        self.needs_rezone = False

    def pump(self, timeout):
        found = list(self.packets)
        self.packets.clear()
        return found

    def send(self, opcode, payload):
        self.sent.append((opcode, payload))


def test_pulse_is_a_tenth_of_a_second():
    assert PULSE == 0.1


def test_waiting_action_is_stepped_every_pulse():
    world = World()
    queue = Schedule()
    session = Session()
    loop = Loop()

    class Hail(Action):
        def __init__(self):
            super().__init__()
            self.pulses = 0
            self.waiting = ["HAIL"]

        def step(self, loop, world):
            self.pulses += 1
            self.was_cleared = self.yielding

    hail = Hail()
    hail.yielding = True
    queue.append(hail, world)

    assert loop.run_once(session, world, queue, Bus(queue)) is hail
    assert loop.run_once(session, world, queue, Bus(queue)) is hail
    assert loop.active is hail
    assert hail.pulses == 2
    assert hail.waiting == ["HAIL"]
    assert hail.was_cleared is False
    assert len(queue) == 1


def test_active_action_is_logged_when_it_changes(caplog):
    caplog.set_level(logging.INFO, logger="eqclient3")
    world = World()
    queue = Schedule()
    session = Session()
    loop = Loop()

    class Hail(Action):
        def __init__(self):
            super().__init__()
            self.source = "talk:guard"

        def step(self, loop, world):
            self.yielding = True

    class Attack(Action):
        def __init__(self):
            super().__init__()
            self.source = "kill:rat"
            self.priority = 500

        def step(self, loop, world):
            self.complete = True

    hail = Hail()
    queue.append(hail, world)
    loop.run_once(session, world, queue, Bus(queue))
    assert "action idle -> Hail talk:guard" in caplog.text

    attack = Attack()
    queue.append(attack, world)
    caplog.clear()
    stepped = loop.run_once(session, world, queue, Bus(queue))
    assert stepped is attack
    assert "action Hail talk:guard -> Attack kill:rat" in caplog.text


def test_yielding_ends_the_pulse_and_the_next_runs_the_new_insert():
    world = World()
    queue = Schedule()
    session = Session()
    loop = Loop()
    ran = []

    class High(Action):
        def step(self, loop, world):
            ran.append(self.insert)
            self.complete = True

    class Low(Action):
        def step(self, loop, world):
            nxt = High()
            loop.queue.append(nxt, world)
            self.yielding = True

    low = Low()
    queue.append(low, world)
    first = loop.run_once(session, world, queue, Bus(queue))

    assert first is low
    assert ran == []
    assert low.suspended is True
    assert len(queue) == 2

    second = loop.run_once(session, world, queue, Bus(queue))
    assert isinstance(second, High)
    assert ran == [second.insert]
    assert second.insert > low.insert
    assert [action.source for action in queue] == [""]


def test_higher_band_appended_without_yield_runs_in_the_same_pulse():
    world = World()
    queue = Schedule()
    session = Session()
    loop = Loop()

    class High(Action):
        def __init__(self):
            super().__init__()
            self.priority = 40

        def step(self, loop, world):
            loop.send("OP_High", 1)
            self.complete = True

    class Low(Action):
        def step(self, loop, world):
            loop.queue.append(High(), world)

    low = Low()
    queue.append(low, world)
    ran = loop.run_once(session, world, queue, Bus(queue))

    assert isinstance(ran, High)
    assert _work(session.sent) == [("OP_High", 1)]
    assert loop.outbound == []
    assert low.suspended is True
    assert [type(action) for action in queue] == [Low]


class _Ping(Action):
    def step(self, loop, world):
        loop.send("OP_Ping", 1)
        self.complete = True


def test_completed_action_is_dropped_and_resolved(tmp_path):
    world = World()
    journal = Journal(tmp_path / "journal-v3.sqlite")
    queue = Schedule()
    session = Session()
    loop = Loop()
    loop.journal = journal
    loop.character = "Hero"

    try:
        done = _Ping()
        done.source = "ping:1"
        queue.append(done, world)
        assert loop.run_once(session, world, queue, Bus(queue)) is done
        assert _work(session.sent) == [("OP_Ping", 1)]
        assert len(queue) == 0
        assert journal.is_resolved("Hero", "ping:1") is True
        assert journal.load_actions("Hero") == []
    finally:
        journal.close()


def test_closed_session_sends_no_zone_request():
    world = World()
    queue = Schedule()
    session = Session()
    session.closed = True
    loop = Loop()

    class Zoner(Action):
        def step(self, loop, world):
            loop.send("OP_ZoneChange", b"north")
            loop.send("OP_Ping", 1)
            self.complete = True

    queue.append(Zoner(), world)
    loop.run_once(session, world, queue, Bus(queue))

    assert session.sent == []
    assert loop.flushed == []


def test_zone_socket_lost_during_flush_transfers():
    from eqclient3.net.client import Client
    from eqclient3.net.session import SessionError
    import eqclient3.loop as loop_mod

    world = World()
    queue = Schedule()
    client = Client()
    transferred = []

    def send(opcode, payload):
        raise SessionError("client is not in a zone")

    client.send = send
    loop = Loop()

    class Zoner(Action):
        def step(self, loop, world):
            loop.send("OP_ZoneChange", b"north")
            self.complete = True

    def fake_transfer(session, *args, **kwargs):
        transferred.append(session)
        return session

    queue.append(Zoner(), world)
    original = loop_mod.transfer_zone
    loop_mod.transfer_zone = fake_transfer
    try:
        loop.run_once(client, world, queue, Bus(queue))
    finally:
        loop_mod.transfer_zone = original

    assert transferred == [client]
    assert loop.flushed == []


def test_open_session_flushes_after_step():
    world = World()
    queue = Schedule()
    session = Session()
    loop = Loop()

    class Zoner(Action):
        def step(self, loop, world):
            loop.send("OP_ZoneChange", b"north")
            self.complete = True

    queue.append(Zoner(), world)
    loop.run_once(session, world, queue, Bus(queue))

    assert _work(session.sent) == [("OP_ZoneChange", b"north")]
    assert loop.outbound == []


def test_bus_delivers_one_opcode_to_every_listener():
    world = World()
    queue = Schedule()
    order = []
    seen = []

    class Listener(Handler):
        opcodes = ("OP_Assist",)

        def __init__(self, name):
            self.name = name

        def handle(self, opcode, payload, world, loop):
            order.append(self.name)
            seen.append(payload)

    class Spell(Action):
        def opcodes(self):
            return ("OP_Assist",)

        def add_message(self, message):
            order.append("action")
            super().add_message(message)

    class Move:
        def opcodes(self):
            return ("OP_Assist",)

        def handle(self, opcode, payload, world=None):
            order.append("movement")

    world.movement = Move()
    spell = Spell()
    queue.append(spell, world)
    bus = Bus(queue, world, Loop(), autoload=False)
    bus.register(Listener("first"))
    bus.register(Listener("second"))
    bus.publish("OP_Assist", OP_Assist(8))

    assert order == ["first", "second", "movement", "action"]
    assert [row.entity_id for row in seen] == [8, 8]
    assert spell.messages[0].opcode == "OP_Assist"
    assert spell.messages[0].payload.entity_id == 8


def test_handler_appended_action_receives_the_same_packet():
    world = World()
    queue = Schedule()
    session = Session([("OP_Assist", OP_Assist(4))])
    loop = Loop()

    class Spawned(Action):
        def __init__(self):
            super().__init__()
            self.priority = 1
            self.source = "aggro:1"

        def opcodes(self):
            return ("OP_Assist",)

    class Damage(Handler):
        opcodes = ("OP_Assist",)

        def handle(self, opcode, payload, world, loop):
            loop.queue.append(Spawned(), world)

    bus = Bus(queue, autoload=False)
    bus.register(Damage())
    loop.run_once(session, world, queue, bus)

    assert len(queue) == 1
    action = queue.winner()
    assert action.source == "aggro:1"
    assert action.messages[0].opcode == "OP_Assist"
    assert action.messages[0].payload.entity_id == 4


def test_higher_action_from_a_handler_is_stepped_instead():
    world = World()
    queue = Schedule()
    session = Session([("OP_Assist", OP_Assist(1))])
    loop = Loop()
    ran = []

    class High(Action):
        def __init__(self):
            super().__init__()
            self.priority = 300

        def step(self, loop, world):
            ran.append("high")

    class Low(Action):
        def step(self, loop, world):
            ran.append("low")

    class Damage(Handler):
        opcodes = ("OP_Assist",)

        def handle(self, opcode, payload, world, loop):
            loop.queue.append(High(), world)

    low = Low()
    queue.append(low, world)
    low.suspended = False
    bus = Bus(queue, autoload=False)
    bus.register(Damage())
    stepped = loop.run_once(session, world, queue, bus)

    assert isinstance(stepped, High)
    assert ran == ["high"]
    assert low.suspended is True


def test_start_reloads_open_actions_and_skips_a_resolved_source(tmp_path):
    journal = Journal(tmp_path / "journal-v3.sqlite")
    try:
        open_row = Action()
        open_row.source = "fetch:9"
        open_row.zone = "gfaydark"
        open_row.priority = 0
        open_row.durable = True
        journal.open_action("Hero", open_row)
        done = Action()
        done.source = "task:done"
        done.zone = "qeynos"
        done.durable = True
        journal.resolve_action("Hero", done)

        loop = Loop()
        queue = Schedule()
        world = World()
        world.zone = "freporte"
        assert loop.start(None, "Hero", queue, journal=journal) is None
        assert loop.character == "Hero"
        assert [action.source for action in queue] == ["fetch:9"]
        assert queue.winner().zone == "gfaydark"

        fresh = Action()
        fresh.source = "task:done"
        assert queue.append(fresh, world) is False
        assert len(queue) == 1
    finally:
        journal.close()


def _work(sent):
    """Action sends, without the idle hold movement queues after the step."""
    hold = {"OP_ClientUpdate", "OP_FloatListThing"}
    return [item for item in sent if item[0] not in hold]
