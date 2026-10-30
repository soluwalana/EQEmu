"""Opcode coverage for handlers/items.py."""

import struct

from eqclient3.actions.loot_mob import LootMob
from eqclient3.actions.trade import Trade
from eqclient3.handlers import items, mobs
from eqclient3.inventory import assign as assign_mod
from eqclient3.structs import OP_ClientUpdate
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


def test_inventory_and_client_update_queue_an_occupied_cursor():
    saved = assign_mod._ITEMS
    assign_mod._ITEMS = {67104: {"slots": 128, "classes": 65535, "races": 65535, "ac": 8, "item": 67104}}
    try:
        world = World()
        loop = Loop()
        world.class_id = 1
        items.ItemsHandler().handle("OP_CharInventory", item_blob(None, 30, 67104, name="Vambraces"), world, loop)
        assert world.cursor == 67104
        assert names(loop) == ["Cursor"]
        assert loop.queue[0].move == (30, 7)
        loop.queue[0].step(loop, world)
        src, dest, _count = struct.unpack("<III", loop.sent[0][1])
        assert (src, dest) == (30, 7)

        held = World()
        held.cursor = 67104
        held.class_id = 1
        quiet = Loop()
        mobs.MobsHandler().handle("OP_ClientUpdate", OP_ClientUpdate(0, 1.0, 2.0, 3.0), held, quiet)
        assert names(quiet) == ["Cursor"]
        assert quiet.queue[0].move == (30, 7)
        mobs.MobsHandler().handle("OP_ClientUpdate", OP_ClientUpdate(0, 1.0, 2.0, 3.0), held, quiet)
        assert names(quiet) == ["Cursor"]

        hail = World()
        hail.class_id = 1
        packet = Loop()
        items.ItemsHandler().handle("OP_ItemPacket", item_blob(0x6A, 30, 67104, name="Vambraces"), hail, packet)
        assert hail.cursor == 67104
        assert names(packet) == ["Cursor"]
        assert packet.queue[0].move == (30, 7)
    finally:
        assign_mod._ITEMS = saved
