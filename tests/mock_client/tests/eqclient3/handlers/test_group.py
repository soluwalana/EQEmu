"""Opcode coverage for handlers/group.py."""

from eqclient3.handlers import group
from eqclient3.structs import OP_GroupInvite
from support import Loop, World, group_update, names


def test_opcodes():
    world = World(name="Hero")
    loop = Loop()
    group.GroupHandler().handle("OP_GroupUpdate", group_update("Hero", ["Guard"], "Guard"), world, loop)
    assert world.group.mode == "party"
    assert world.raid.mode == "raid"
    assert world.group.leader == "Guard"
    assert "Hero" in world.group.members and "Guard" in world.group.members

    group.GroupHandler().handle("OP_GroupInvite", OP_GroupInvite("Mage", "Hero").serialize(), world, loop)
    assert names(loop) == ["Seat"]
    assert loop.queue[0].name == "Mage"
    assert loop.queue[0].priority == 230
    assert loop.queue[0].source == "seat:Mage"
    assert any(command.startswith("invite ") for command in loop.queue[0].commands)

    accepted = Loop()
    group.GroupHandler().handle("OP_GroupInvite2", OP_GroupInvite("Hero", "Guard").serialize(), world, accepted)
    assert accepted.queue[0].name == "Guard"
    assert any(command.startswith("follow ") for command in accepted.queue[0].commands)
