"""Opcode coverage for handlers/items.py."""

import struct

from eqclient3.actions.loot_mob import LootMob
from eqclient3.actions.trade import Trade
from eqclient3.handlers import items
from support import Loop, World, item_blob, names


def test_opcodes():
    world = World()
    loop = Loop()
    items.ItemsHandler().handle("OP_CharInventory", item_blob(None, 5, 100, name="Sword"), world, loop)
    assert world.bags[5] == 100
    assert world.items[100].name == "Sword"
    assert names(loop) == []

    items.ItemsHandler().handle("OP_ItemPacket", item_blob(0x69, 30, 22292, name="Token"), world, loop)
    assert names(loop) == ["Cursor"]
    assert loop.queue[0].slot == 30
    assert loop.queue[0].priority == 350
    assert loop.queue[0].source == "cursor:30"
    assert 22292 not in world.bags.values()

    shop = Trade(5, 50)
    loop.append(shop)
    items.ItemsHandler().handle("OP_ItemPacket", item_blob(0x64, 1, 50, name="Ration", price=12), world, loop)
    assert shop.slots[1] == (50, 12)
    items.ItemsHandler().handle("OP_ShopDelItem", struct.pack("<III", 0, 0, 1), world, loop)
    assert 1 not in shop.slots

    opened = LootMob(3, (0.0, 0.0, 0.0))
    loop.append(opened)
    items.ItemsHandler().handle("OP_ItemPacket", item_blob(0x66, 2, 77, name="Coin"), world, loop)
    assert opened.slots == []
    assert 77 not in world.bags.values()
