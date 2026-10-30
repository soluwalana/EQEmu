"""Opcode coverage for handlers/profile.py."""

import struct
from types import SimpleNamespace

from eqclient3.handlers import profile
from support import Loop, World, names, profile as profile_packet


def test_opcodes():
    world = World()
    loop = Loop()
    profile.ProfileHandler().handle(
        "OP_PlayerProfile",
        profile_packet(name="Hero", level=4, skill=(27, 12)),
        world,
        loop,
    )
    assert world.name == "Hero"
    assert world.level == 4
    assert world.skills[27] == 12
    assert 0 not in world.skills or world.skills[0] == 0
    assert world.coin == (1, 2, 3, 4)

    profile.ProfileHandler().handle("OP_SkillUpdate", struct.pack("<II", 27, 40), world, loop)
    assert world.skills[27] == 40
    bare = World()
    profile.ProfileHandler().handle("OP_SkillUpdate", struct.pack("<II", 0, 5), bare, loop)
    assert bare.skills == {0: 5}

    hungry = World()
    hungry.bags = {23: 100}
    hungry.items = {100: SimpleNamespace(item_type=14)}
    profile.ProfileHandler().handle("OP_Stamina", struct.pack("<II", 10, 127), hungry, loop)
    assert hungry.food == 10 and hungry.water == 127
    assert names(loop) == ["Field"]
    assert loop.queue[0].kind == "eat" and loop.queue[0].slot == 23
    assert loop.queue[0].source == "field:eat" and loop.queue[0].priority == 200

    forage = World()
    forage.skills = {27: 8}
    forage.bags = {}
    second = Loop()
    profile.ProfileHandler().handle("OP_Stamina", struct.pack("<II", 0, 127), forage, second)
    assert names(second) == ["Field"]
    assert second.queue[0].kind == "forage" and second.queue[0].source == "field:forage"

    profile.ProfileHandler().handle("OP_MoneyUpdate", struct.pack("<iiii", 2, 0, 0, 5), world, loop)
    assert world.coin == (2, 0, 0, 5)
    profile.ProfileHandler().handle("OP_ManaChange", struct.pack("<I", 90), world, loop)
    assert world.mana == 90
    profile.ProfileHandler().handle("OP_MemorizeSpell", struct.pack("<III", 1, 55, 0), world, loop)
    assert world.spell_book[1] == 55
    profile.ProfileHandler().handle("OP_MemorizeSpell", struct.pack("<III", 2, 66, 1), world, loop)
    assert world.gems[2] == 66
