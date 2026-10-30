"""Opcode coverage for handlers/level.py."""

import struct

from eqclient3.handlers import level
from support import Loop, World, level_popup, names


def test_opcodes():
    world = World(level=1, points=0, exp=0)
    loop = Loop()
    level.LevelHandler().handle("OP_ExpUpdate", struct.pack("<I", 40), world, loop)
    assert world.exp == 40
    level.LevelHandler().handle("OP_LevelUpdate", struct.pack("<III", 3, 1, 80), world, loop)
    assert world.level == 3
    assert world.points == 10
    assert world.exp == 80
    level.LevelHandler().handle("OP_OnLevelMessage", level_popup(77), world, loop)
    assert names(loop) == ["LevelUp"]
    assert loop.queue[0].level == 3
    assert loop.queue[0].source == "level:3"
    assert loop.queue[0].priority == 0
    assert loop.sent[0][0] == "OP_PopupResponse"
    assert loop.sent[0][1] == struct.pack("<II", 0, 77)
    level.LevelHandler().handle("OP_OnLevelMessage", level_popup(77), world, loop)
    assert names(loop) == ["LevelUp"]
    assert "Fetch" not in names(loop)
