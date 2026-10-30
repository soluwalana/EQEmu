"""Opcode coverage for handlers/consider.py."""

from eqclient3.handlers import consider
from support import Loop, World, consider as consider_packet, spawn
from eqclient3.handlers import mobs


def test_opcodes():
    world = World(name="Hero")
    loop = Loop()
    mobs.MobsHandler().handle("OP_NewSpawn", spawn(9, "a bat"), world, loop)
    consider.ConsiderHandler().handle("OP_Consider", consider_packet(7, 9, 5, 2), world, loop)
    row = world.mobs[9].consider
    assert row.standing == 5
    assert row.level_color == 2
    assert row.name == "indifferent"
    assert loop.queue == []
    consider.ConsiderHandler().handle("OP_Consider", consider_packet(7, 9, 6, 4), world, loop)
    assert world.mobs[9].consider.standing == 9
    assert loop.queue == []
