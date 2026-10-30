"""Action mailbox, waiting list, and target step."""

import struct
import types

from eqclient3.action import Action, Message
from eqclient3.loop import Loop
from eqclient3.structs import OP_Assist, OP_Consider, OP_HPUpdate
from eqclient3.world import Mob, World


class _Open:
    def clear(self, start, end):
        return True


class _Blocked:
    def clear(self, start, end):
        return False


def test_consume_removes_only_that_opcode():
    action = Action()
    action.add_message(Message(OP_Assist(1)))
    action.add_message(Message(OP_HPUpdate(2, 0, 0)))
    action.add_message(Message(OP_Assist(3)))

    got = action.consume("OP_Assist")

    assert got.payload.entity_id == 1
    assert [
        (
            message.opcode,
            (message.payload.entity_id if message.opcode == "OP_Assist" else message.payload.cur_hp),
        )
        for message in action.messages
    ] == [
        ("OP_HPUpdate", 2),
        ("OP_Assist", 3),
    ]
    assert action.consume("OP_Missing") is None
    assert len(action.messages) == 2


def test_waiting_starts_empty_and_target_clears_on_consider():
    action = Action()
    assert action.waiting == []
    assert action.suspended is True
    assert action.yielding is False
    assert action.completed is False
    assert action.limit is None
    assert action.target_id == 0
    assert action.consider_due is False

    world, mob = _world(targeted=False)
    loop = Loop()
    action.target_id = mob.id
    action.step(loop, world)

    assert action.waiting == ["TARGET"]
    assert action.consider_due is True
    assert loop.outbound == [("OP_TargetMouse", struct.pack("<I", mob.id & 65535))]

    action.step(loop, world)

    assert action.waiting == ["TARGET"]
    assert action.consider_due is False
    assert loop.outbound[-1] == ("OP_Consider", _consider(0, mob.id))

    action.add_message(Message(OP_Consider(0, mob.id)))
    action.add_message(Message(OP_HPUpdate(9, 0, 0)))
    action.step(loop, world)

    assert action.waiting == []
    assert action.waited == 0
    assert mob.targeted is True
    assert [message.opcode for message in action.messages] == ["OP_HPUpdate"]


def test_consider_is_sent_again_after_ten_silent_ticks():
    world, mob = _world(targeted=False)
    action = Action()
    action.target_id = mob.id
    loop = Loop()

    action.step(loop, world)
    action.step(loop, world)
    assert loop.outbound[-1] == ("OP_Consider", _consider(0, mob.id))
    loop.outbound.clear()

    for _ in range(9):
        action.step(loop, world)
        assert loop.outbound == []
    assert action.waited == 9
    assert action.waiting == ["TARGET"]

    action.step(loop, world)
    assert action.waited == 0
    assert loop.outbound == [("OP_Consider", _consider(0, mob.id))]
    assert action.waiting == ["TARGET"]


def test_out_of_sight_plans_and_does_not_send():
    movement = types.ModuleType("eqclient3.movement")
    movement.calls = []

    def plan(mob, mode="run"):
        movement.calls.append(("plan", mob.id, mode))
        return ("path", mob.id)

    def advance(loop, world, path):
        movement.calls.append(("advance", path))

    movement.plan = plan
    movement.advance = advance
    world, mob = _world(targeted=False)
    world.mesh = _Blocked()
    world.movement = movement
    action = Action()
    action.target_id = mob.id
    loop = Loop()

    action.step(loop, world)

    assert action.waiting == ["TARGET"]
    assert loop.outbound == []
    assert action.active_path == ("path", mob.id)
    assert movement.calls == [("plan", mob.id, "run"), ("advance", action.active_path)]

    action.step(loop, world)
    assert movement.calls == [
        ("plan", mob.id, "run"),
        ("advance", action.active_path),
        ("advance", action.active_path),
    ]


def _consider(player, target):
    return OP_Consider(player, target).serialize()


def _world(targeted):
    world = World()
    world.mesh = _Open()
    mob = Mob(id=7, name="a rat", npc=1, level=2, position=(1.0, 0.0, 0.0))
    mob.targeted = targeted
    world.mobs[mob.id] = mob
    return world, mob
