"""Opcode coverage for handlers/zoning.py."""

from eqclient3.handlers import zoning
from support import Loop, World, names, new_zone, request_zone, sources, zone_change


class _Session:
    def __init__(self, open=True):
        self.open = open
        self.closed = not open
        self.needs_rezone = False
        self.transfers = 0

    def transfer_zone(self):
        self.transfers += 1


class _Journal:
    def __init__(self, done=False):
        self.done = done

    def tutorial_done(self, character):
        return self.done

    def resolved(self, character, source):
        return False

    def clear_source(self, character, source):
        return None

    def bot_settings(self, character):
        return {}


def test_a_live_client_confirms_the_zone_request():
    from eqclient3.handlers.common import session_open
    from eqclient3.loop import Loop as PlayLoop
    from eqclient3.loop import ScriptedSession
    from eqclient3.net.client import Client

    client = Client()
    client.session = ScriptedSession()
    loop = PlayLoop()
    loop.session = client
    world = World(name="Mockvthree")
    assert session_open(loop) is True
    zoning.ZoningHandler().handle("OP_RequestClientZoneChange", request_zone(45, 10, 20, 30), world, loop)
    assert loop.sent[0][0] == "OP_ZoneChange"
    assert client.session.transfers == 0


def test_opcodes():
    world = World(name="Hero", zone="qeynos", zone_id=1, ground={"old": 1})
    loop = Loop()
    zoning.ZoningHandler().handle("OP_RequestClientZoneChange", request_zone(45, 10, 20, 30), world, loop)
    assert names(loop) == []
    assert loop.sent[0][0] == "OP_ZoneChange"
    assert len(loop.sent[0][1]) == 100

    here = World(name="Hero", zone="qeynos", zone_id=1)
    stayed = Loop()
    zoning.ZoningHandler().handle("OP_RequestClientZoneChange", request_zone(1, 10, 20, 30), here, stayed)
    assert stayed.sent == []
    assert here.position == (10.0, 20.0, 30.0)

    world.position = (12.0, 34.0, 56.0)
    zoning.ZoningHandler().handle("OP_ZoneChange", zone_change(45, 0, 0, 0, success=1), world, loop)
    assert names(loop) == []
    assert len(loop.sent) == 1
    assert loop._transferred is True
    assert world.zone_id == 45
    assert world.position == (12.0, 34.0, 56.0)

    rejected = World(name="Hero", zone="qeynos", zone_id=1)
    stayed = Loop()
    zoning.ZoningHandler().handle("OP_ZoneChange", zone_change(45, 8, 9, 10, success=0), rejected, stayed)
    assert names(stayed) == []
    assert stayed.sent == []
    assert getattr(stayed, "_transferred", False) is False
    assert rejected.zone_id == 1
    assert rejected.position == (8.0, 9.0, 10.0)

    same = World(name="Hero", zone="qeynos", zone_id=1)
    parked = Loop()
    zoning.ZoningHandler().handle("OP_ZoneChange", zone_change(1, 4, 5, 6, success=1), same, parked)
    assert names(parked) == []
    assert getattr(parked, "_transferred", False) is False
    assert same.position == (4.0, 5.0, 6.0)

    closed = Loop()
    closed.session = _Session(open=False)
    zoning.ZoningHandler().handle("OP_ZoneChange", zone_change(45, 1, 2, 3), world, closed)
    assert closed.queue == [] and closed.sent == []
    assert closed.session.transfers == 1

    hole = Loop()
    hole.session = _Session()
    from eqclient3.structs import OP_ReliableHole

    zoning.ZoningHandler().handle("OP_ReliableHole", OP_ReliableHole(), world, hole)
    assert hole.queue == [] and hole.sent == []
    assert hole.session.transfers == 1

    entered = World(ground={"drop": 1})
    formed = Loop()
    zoning.ZoningHandler().handle("OP_NewZone", new_zone("qeynos", 3, 4, 5, zone_id=1), entered, formed)
    assert entered.zone == "qeynos"
    assert entered.safe == (3.0, 4.0, 5.0)
    assert entered.zone_id == 1
    assert entered.ground == {}
    assert names(formed) == ["Form"]
    assert formed.queue[0].priority == 290
    assert formed.queue[0].source == "form:qeynos"
    zoning.ZoningHandler().handle("OP_NewZone", new_zone("qeynos", 3, 4, 5, zone_id=1), entered, formed)
    assert sources(formed) == ["form:qeynos"]

    tutorial = World()
    reading = Loop()
    reading.journal = _Journal(done=False)
    zoning.ZoningHandler().handle("OP_NewZone", new_zone("tutorialb", 1, 2, 3), tutorial, reading)
    assert names(reading) == ["ReadTasks", "Form"]
    assert reading.queue[0].source == "read_tasks:tutorialb"
    assert reading.queue[1].source == "form:tutorialb"

    skipped = Loop()
    skipped.journal = _Journal(done=True)
    zoning.ZoningHandler().handle("OP_NewZone", new_zone("tutorialb", 1, 2, 3), World(name="Hero"), skipped)
    assert names(skipped) == ["Form"]
    assert skipped.queue[0].source == "form:tutorialb"


def test_a_finished_form_is_queued_again_on_the_next_login(tmp_path):
    from eqclient3.actions.bots.form import Form
    from eqclient3.journal import Journal
    from eqclient3.loop import Loop as PlayLoop
    from eqclient3.schedule import Schedule
    from eqclient3.world import World as Sheet

    journal = Journal(tmp_path / "journal-v3.sqlite", character="Hero")
    try:
        done = Form("tutorialb")
        done.source = "form:tutorialb"
        done.complete = True
        journal.resolve_action("Hero", done)
        world = Sheet(name="Hero")
        queue = Schedule()
        loop = PlayLoop()
        loop.character = "Hero"
        loop.journal = journal
        loop.queue = queue
        loop.world = world
        queue.bind(journal, "Hero")
        zoning.ZoningHandler().handle("OP_NewZone", new_zone("tutorialb", 1, 2, 3), world, loop)
        assert [action.source for action in queue if type(action).__name__ == "Form"] == ["form:tutorialb"]
        assert journal.is_resolved("Hero", "form:tutorialb") is False
    finally:
        journal.close()
