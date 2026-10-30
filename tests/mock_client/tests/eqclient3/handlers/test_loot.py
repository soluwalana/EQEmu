"""Opcode coverage for handlers/loot.py."""

import struct

from eqclient3.handlers import loot
from eqclient3.world import Mob
from support import Loop, World, become_corpse, names


def test_opcodes():
    world = World(self_id=7, name="Hero")
    world.mobs[9] = Mob(9, "a bat", npc=1)
    world.mobs[7] = Mob(7, "Hero", npc=1)
    loop = Loop()
    loot.LootHandler().handle("OP_BecomeCorpse", become_corpse(9, 3, 4, 5), world, loop)
    assert names(loop) == []
    world.fought.add(9)
    loot.LootHandler().handle("OP_BecomeCorpse", become_corpse(9, 3, 4, 5), world, loop)
    assert names(loop) == ["LootMob"]
    assert loop.queue[0].priority == 270
    assert loop.queue[0].source == "loot_mob:9"
    assert loop.queue[0].corpse_id == 9
    assert loop.queue[0].where == (3.0, 4.0, 5.0)
    loot.LootHandler().handle("OP_BecomeCorpse", become_corpse(9, 3, 4, 5), world, loop)
    assert names(loop) == ["LootMob"]
    loot.LootHandler().handle("OP_BecomeCorpse", become_corpse(7, 1, 1, 1), world, loop)
    assert "Reclaim" not in names(loop)
    assert names(loop) == ["LootMob"]

    remembered = Loop()
    remembered.append(type("Attack", (), {"spawn_id": 11})())
    sheet = World(self_id=7)
    loot.LootHandler().handle("OP_BecomeCorpse", become_corpse(11, 1, 2, 3), sheet, remembered)
    assert names(remembered) == ["Attack", "LootMob"]
    stranger = Loop()
    loot.LootHandler().handle("OP_BecomeCorpse", become_corpse(12, 1, 2, 3), World(self_id=7), stranger)
    assert stranger.queue == []

    before = len(loop.queue)
    loot.LootHandler().handle("OP_MoneyOnCorpse", struct.pack("<BBBBIIII", 1, 0x5A, 0x40, 0, 1, 2, 3, 4), world, loop)
    assert world.coin == (1, 2, 3, 4)
    assert len(loop.queue) == before
    loot.LootHandler().handle("OP_MoneyOnCorpse", struct.pack("<BBBBIIII", 5, 0x5A, 0x40, 0, 9, 0, 0, 0), world, loop)
    assert world.coin == (1, 2, 3, 4)
