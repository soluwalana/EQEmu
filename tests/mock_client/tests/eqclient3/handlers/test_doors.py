"""Opcode coverage for handlers/doors.py."""

import struct

from eqclient3.handlers import doors
from support import Loop, World, door, ground, names


def test_opcodes():
    world = World()
    loop = Loop()
    doors.DoorsHandler().handle("OP_SpawnDoor", door(4, "STONE_DOOR", 1, 2, 3), world, loop)
    assert world.doors[4].name == "STONE_DOOR"
    assert (world.doors[4].x, world.doors[4].y, world.doors[4].z) == (1.0, 2.0, 3.0)
    doors.DoorsHandler().handle("OP_GroundSpawn", ground(11, "Bone", 8, 9, 0), world, loop)
    assert world.ground[11].name == "Bone"
    assert world.ground[11].used is False
    doors.DoorsHandler().handle("OP_MoveDoor", bytes([4]), world, loop)
    assert world.doors[4].opened is True
    doors.DoorsHandler().handle("OP_ClickObject", struct.pack("<II", 11, 7), world, loop)
    assert world.ground[11].used is True
    assert names(loop) == []
    assert loop.sent == []
