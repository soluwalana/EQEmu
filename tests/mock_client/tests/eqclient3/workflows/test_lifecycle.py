"""Lifecycle pulses. A missing action or handler module skips that test."""

from __future__ import annotations

import importlib
import struct
from types import SimpleNamespace

import pytest

NAME = "Mockone"


def _need(*modules: str):
    try:
        loaded = [importlib.import_module(name) for name in modules]
    except ImportError as exc:
        pytest.skip(str(exc))
    return loaded


def _net():
    import net.test_connection as connection

    return connection


class _Named:
    """A frozen sheet plus the character name loop.start reads."""

    def __init__(self, sheet, name: str) -> None:
        object.__setattr__(self, "_sheet", sheet)
        object.__setattr__(self, "name", name)

    def __getattr__(self, item):
        return getattr(self._sheet, item)


class _Tape:
    def __init__(self) -> None:
        self.sent: list[tuple] = []
        self.inbox: list[tuple] = []
        self.closed = False
        self.needs_rezone = False

    def pump(self, timeout: float = 0.0):
        del timeout
        batch = list(self.inbox)
        self.inbox.clear()
        return batch


class _Roster(list):
    def __init__(self) -> None:
        super().__init__()
        self.roster: list = []
        self.rotation: list = []
        self.reconstituted_at = 0


def _new_zone(name: str) -> bytes:
    from eqclient3.structs import OP_NewZone

    return OP_NewZone(name, 1.0, 2.0, 3.0).serialize()


def _task_window() -> bytes:
    """One kill activity. In tutorialb the handler stores it and appends nothing."""
    from eqclient3.structs import OP_TaskSelectWindow, TaskChoice, TaskElement

    element = TaskElement(1, 2, 0, "a trainee", "", 1, 0, 0, 0, "kill the trainee")
    choice = TaskChoice(7, 0, 0, "Mine", "kill the trainee", [element])
    return OP_TaskSelectWindow(0, 0, [choice]).serialize()


def _kinds(queue) -> list[str]:
    return [type(action).__name__ for action in queue]


def test_empty_journal_holds_position(tmp_path):
    Loop, Journal, Schedule, Bus, World, movement, build = _need(
        "eqclient3.loop",
        "eqclient3.journal",
        "eqclient3.schedule",
        "eqclient3.bus",
        "eqclient3.world",
        "eqclient3.movement",
        "eqclient3.net.sheet",
    )
    Loop, Journal, Schedule, Bus, World, movement, sheet_mod = (
        Loop,
        Journal,
        Schedule,
        Bus,
        World,
        movement,
        build,
    )
    net = _net()
    login, world, zone = net.Peer(), net.Peer(), net.Peer()
    client = None
    try:
        world_ops, login_ops = net._opcodes()
        net._login_script(login, login_ops)
        net._zone_script(zone, world_ops)
        charinfo = net.require(world_ops, "OP_SendCharInfo")
        enter_op = net.require(world_ops, "OP_EnterWorld")
        info = net.require(world_ops, "OP_ZoneServerInfo")
        world.once(
            net.require(world_ops, "OP_SendLoginInfo"),
            lambda peer, _payload: peer.reply(charinfo, net._char_select(NAME)),
        )
        world.once(enter_op, lambda peer, _payload: peer.reply(info, net._zone_info(zone.port)))
        journal = Journal.Journal(tmp_path / "journal-v3.sqlite")
        queue = Schedule.Schedule()
        loop = Loop.Loop()
        sheet = _Named(sheet_mod.build(1, 1, 0), NAME)
        client = loop.start(net._connection(login, world), sheet, queue, journal)
        assert client is not None
        assert list(queue) == []
        assert journal.load_actions(NAME) == []
        tables = {row[0] for row in journal._db.execute("SELECT name FROM sqlite_master WHERE type = 'table'")}
        assert "actions" in tables
        loop.run_once(client, World.World(), queue, Bus.Bus(autoload=False))
        assert any(opcode == "OP_ClientUpdate" for opcode, _payload in loop.flushed)
    finally:
        if client is not None:
            client.close()
        zone.stop()
        world.stop()
        login.stop()


def test_open_fetch_reloads_and_a_resolved_source_does_not(tmp_path):
    Loop, Journal, Schedule, Fetch = _need(
        "eqclient3.loop",
        "eqclient3.journal",
        "eqclient3.schedule",
        "eqclient3.actions.fetch",
    )
    journal = Journal.Journal(tmp_path / "journal-v3.sqlite")
    open_fetch = Fetch.Fetch(5, 1, "silk")
    open_fetch.source = "fetch:5"
    done = Fetch.Fetch(6, 1, "done")
    done.source = "fetch:6"
    assert journal.open_action(NAME, open_fetch)
    assert journal.open_action(NAME, done)
    journal.resolve_action(NAME, done)
    queue = Schedule.Schedule()
    loop = Loop.Loop()
    loop.start(None, SimpleNamespace(name=NAME), queue, journal)
    assert [action.source for action in queue] == ["fetch:5"]
    assert all(type(action).__name__ == "Fetch" for action in queue)


def test_same_band_yield_appends_one_kill():
    Loop, Schedule, Bus, World, Fetch, Mob = _need(
        "eqclient3.loop",
        "eqclient3.schedule",
        "eqclient3.bus",
        "eqclient3.world",
        "eqclient3.actions.fetch",
        "eqclient3.world",
    )
    world = World.World()
    world.zone = "qeynos"
    world.soulbound = True
    world.name = NAME
    world.plans = {99: SimpleNamespace(drop=SimpleNamespace(zone="qeynos", spawns=[7], above_level=False))}
    world.mobs[7] = Mob.Mob(7, name="a rat", position=(0.0, 0.0, 0.0))
    queue = Schedule.Schedule()
    fetch = Fetch.Fetch(99, 1, "band")
    fetch.source = "fetch:99"
    assert queue.append(fetch, world, None, NAME)
    loop = Loop.Loop()
    loop.character = NAME
    tape = _Tape()
    bus = Bus.Bus(autoload=False)
    first = loop.run_once(tape, world, queue, bus)
    assert type(first).__name__ == "Fetch"
    assert first.yielding
    kills = [action for action in queue if type(action).__name__ == "Kill"]
    assert len(kills) == 1
    assert kills[0].spawn_id == 7
    second = loop.run_once(tape, world, queue, bus)
    assert type(second).__name__ == "Kill"
    assert len([action for action in queue if type(action).__name__ == "Kill"]) == 1


def test_in_combat_heal_is_one_command():
    Loop, Schedule, Bus, World, Attack, Mob = _need(
        "eqclient3.loop",
        "eqclient3.schedule",
        "eqclient3.bus",
        "eqclient3.world",
        "eqclient3.actions.attack",
        "eqclient3.world",
    )
    world = World.World()
    world.zone = "qeynos"
    world.name = NAME
    world.self_id = 1
    world.hp = 40
    world.max_hp = 100
    world.mana = 50
    world.gems = {0: 9}
    world.spell_info = {9: SimpleNamespace(mana=5, recast=0, heal=True, combat=False, cure=None)}
    mob = Mob.Mob(7, name="a rat", position=(0.0, 0.0, 0.0), level=2)
    mob.targeted = True
    world.mobs[7] = mob
    attack = Attack.Attack(7)
    attack.source = "attack:7"
    queue = Schedule.Schedule()
    assert queue.append(attack, world, None, NAME)
    loop = Loop.Loop()
    loop.character = NAME
    tape = _Tape()
    bus = Bus.Bus(autoload=False)

    loop.run_once(tape, world, queue, bus)
    casts = [opcode for opcode, _payload in loop.flushed if opcode == "OP_CastSpell"]
    assert casts == ["OP_CastSpell"]
    assert attack.heal_requested

    loop.run_once(tape, world, queue, bus)
    assert "OP_CastSpell" not in [opcode for opcode, _payload in loop.flushed]
    assert attack.heal_requested

    world.hp = 90
    tape.inbox.append(("OP_HPUpdate", struct.pack("<HIi", 1, 90, 100)))
    loop.run_once(tape, world, queue, bus)
    assert attack.heal_requested is False


def test_reliable_hole_calls_transfer_zone_without_a_zone_request():
    Loop, Schedule, Bus, World, Zone, opcodes = _need(
        "eqclient3.loop",
        "eqclient3.schedule",
        "eqclient3.bus",
        "eqclient3.world",
        "eqclient3.actions.zone",
        "eqclient3.net.opcodes",
    )
    net = _net()
    login, world_peer, zone = net.Peer(), net.Peer(), net.Peer()
    client = None
    try:
        world_ops, login_ops = net._opcodes()
        net._login_script(login, login_ops)
        net._zone_script(zone, world_ops)
        charinfo = net.require(world_ops, "OP_SendCharInfo")
        enter_op = net.require(world_ops, "OP_EnterWorld")
        info_op = net.require(world_ops, "OP_ZoneServerInfo")
        login_info = net.require(world_ops, "OP_SendLoginInfo")
        change = net.require(world_ops, "OP_ZoneChange")

        def on_login(peer, payload):
            if payload[188:189] == b"\x01":
                peer.reply(enter_op, b"")
                return
            peer.reply(charinfo, net._char_select(NAME))

        world_peer.always(login_info, on_login)
        world_peer.always(
            enter_op,
            lambda peer, _payload: peer.reply(info_op, net._zone_info(zone.port)),
        )
        sheet = net.build(1, 1, 0)
        client = net.connect(net._connection(login, world_peer), sheet)
        net.enter(client, sheet)
        client.session.needs_rezone = True
        game = World.World()
        game.zone = "qeynos"
        queue = Schedule.Schedule()
        zone_action = Zone.Zone("freportw")
        zone_action.source = "zone:freportw"
        queue.append(zone_action, game, None, NAME)
        loop = Loop.Loop()
        loop.character = NAME
        before = len(world_peer.apps)
        loop.run_once(client, game, queue, Bus.Bus(autoload=False))
        assert loop.flushed == []
        assert change not in {opcode for opcode, _payload in zone.apps}
        fresh = world_peer.apps[before:]
        sent = net._names(
            fresh,
            world_ops,
            "OP_SendLoginInfo",
            "OP_EnterWorld",
            "OP_ApproveName",
            "OP_CharacterCreate",
        )
        assert sent == ["OP_SendLoginInfo", "OP_EnterWorld"]
        info = next(payload for opcode, payload in fresh if opcode == login_info)
        assert info[188] == 1
        del opcodes
    finally:
        if client is not None:
            client.close()
        zone.stop()
        world_peer.stop()
        login.stop()


def test_tutorial_zone_in_reads_tasks_and_an_empty_queue_does_not_finish(tmp_path):
    Loop, Schedule, Bus, World, Journal = _need(
        "eqclient3.loop",
        "eqclient3.schedule",
        "eqclient3.bus",
        "eqclient3.world",
        "eqclient3.journal",
    )
    from eqclient3.structs import OP_ChannelMessage

    world = World.World()
    world.name = NAME
    world.zone = "tutorialb"
    world.bots = _Roster()
    journal = Journal.Journal(tmp_path / "journal-v3.sqlite")
    queue = Schedule.Schedule()
    loop = Loop.Loop()
    loop.character = NAME
    loop.journal = journal
    loop.queue = queue
    loop.world = world
    queue.bind(journal, NAME)
    tape = _Tape()
    bus = Bus.Bus(autoload=True)
    tape.inbox.append(("OP_NewZone", _new_zone("tutorialb")))
    tape.inbox.append(("OP_TaskSelectWindow", _task_window()))
    loop.run_once(tape, world, queue, bus)
    assert "ReadTasks" in _kinds(queue)
    assert "Form" not in _kinds(queue)
    assert not any(type(action).__name__ == "Talk" for action in queue)
    assert any(type(action).__name__ == "Kill" and str(action.source).startswith("task:") for action in queue)

    tape.inbox.append(
        (
            "OP_ChannelMessage",
            OP_ChannelMessage("", "a trainer", text="kill the rat").serialize(),
        )
    )
    loop.run_once(tape, world, queue, bus)
    assert any(getattr(action, "source", "") == "chat:kill:rat" for action in queue)

    saved = list(queue)
    reading = next(action for action in saved if type(action).__name__ == "ReadTasks")
    for action in saved:
        queue.remove(action.insert)
    loop.run_once(tape, world, queue, bus)
    assert journal.tutorial_done(NAME) is False
    assert list(queue) == []
    queue.restore(reading)
    tape.inbox.append(("OP_NewZone", _new_zone("qeynos")))
    done = False
    for _pulse in range(4):
        loop.run_once(tape, world, queue, bus)
        if journal.tutorial_done(NAME) and reading.complete:
            done = True
            break
    assert done
