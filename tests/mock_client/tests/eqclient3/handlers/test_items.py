"""Opcode coverage for handlers/items.py."""

import struct

from eqclient3.actions.loot_mob import LootMob
from eqclient3.actions.trade import Trade
from eqclient3.handlers import items, mobs
from eqclient3.inventory import assign as assign_mod
from eqclient3.structs import OP_ClientUpdate, OP_ShopDelItem
from support import Loop, World, item_blob, names


def test_a_bag_move_names_the_parent_and_the_cursor_stays_in_inventory():
    from eqclient3.structs import ITEM_INVENTORY, Item, OP_CharInventory, OP_MoveItem

    sent = OP_MoveItem(30, 851).serialize()
    back = OP_MoveItem.deserialize(sent)
    assert (back.from_slot, back.to_slot) == (30, 851)
    assert struct.unpack_from("<hh", sent, 4) == (33, -1)
    assert struct.unpack_from("<hh", sent, 16) == (26, 0)

    packet = OP_CharInventory(
        [
            Item(ITEM_INVENTORY, 13, "Short Sword*", "", 9998),
            Item(ITEM_INVENTORY, 30, "Skin of Milk", "", 9990, 20),
        ]
    ).serialize()
    parsed = OP_CharInventory.deserialize(packet)
    assert [(item.slot, item.item_id, item.name) for item in parsed.items] == [
        (13, 9998, "Short Sword*"),
        (30, 9990, "Skin of Milk"),
    ]


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
    removed = OP_ShopDelItem(0, 0, 1).serialize()
    assert len(removed) == 16
    items.ItemsHandler().handle("OP_ShopDelItem", removed, world, loop)
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
        items.ItemsHandler().handle(
            "OP_CharInventory",
            item_blob(None, 30, 67104, name="Vambraces"),
            world,
            loop,
        )
        assert world.cursor == 67104
        assert names(loop) == ["Cursor"]
        assert loop.queue[0].move == (30, 7)
        loop.queue[0].step(loop, world)
        src = struct.unpack_from("<h", loop.sent[0][1], 4)[0]
        dest = struct.unpack_from("<h", loop.sent[0][1], 16)[0]
        assert (src, dest) == (33, 7)

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


def test_a_bag_write_is_stored_for_the_queue_report(tmp_path):
    from eqclient3.journal import Journal
    from eqclient3.scripts.journal_queue import report

    journal = Journal(tmp_path / "journal-v3.sqlite")
    world = World(name="Hero")
    loop = Loop()
    loop.journal = journal
    loop.character = "Hero"
    try:
        items.ItemsHandler().handle("OP_CharInventory", item_blob(None, 13, 501, name="Short Sword"), world, loop)
        lines = report(journal, "Hero")
    finally:
        journal.close()
    assert "  primary: Short Sword (501)" in lines
