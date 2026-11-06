"""RoF2 native inventory numbering and flat bag-cell IDs."""

import unittest

from eqclient4.inventory import CharacterInventory
from eqclient4.structs.constants import CURSOR_SLOT, GENERAL_SLOTS, WORN
from eqclient4.structs.items import ITEM_INVENTORY, Item, OP_MoveItem
from eqclient4.structs.wire import (
    InventorySlot,
    TypelessInventorySlot,
    client_slot,
    inventory_wire,
    pack_inventory_slot,
    unpack_inventory_slot,
)


class NativeInventorySlotsTest(unittest.TestCase):
    def test_boundaries(self) -> None:
        self.assertEqual((WORN.start, WORN.stop), (0, 23))
        self.assertEqual(list(GENERAL_SLOTS), list(range(23, 33)))
        self.assertEqual(CURSOR_SLOT, 33)

    def test_top_level_packet_round_trip(self) -> None:
        for slot in (0, 20, 21, 22, 23, 29, 30, 31, 32, 33):
            with self.subTest(slot=slot):
                packed = pack_inventory_slot(slot)
                self.assertEqual(unpack_inventory_slot(packed, 0), slot)
                self.assertEqual(InventorySlot.unpack(packed).client_slot, slot)
                self.assertEqual(TypelessInventorySlot.for_client(slot).client_slot, slot)

    def test_flat_bag_cells(self) -> None:
        for slot, parent, sub in (
            (251, 23, 0),
            (260, 23, 9),
            (261, 24, 0),
            (340, 31, 9),
            (341, 32, 0),
            (350, 32, 9),
            (351, 33, 0),
            (360, 33, 9),
        ):
            with self.subTest(slot=slot):
                self.assertEqual(inventory_wire(slot), (parent, sub))
                self.assertEqual(client_slot(0, parent, sub), slot)
                self.assertEqual(unpack_inventory_slot(pack_inventory_slot(slot), 0), slot)

    def test_move_and_render_general_ten(self) -> None:
        packet = OP_MoveItem(from_slot=33, to_slot=32)
        decoded = OP_MoveItem.deserialize(packet.serialize())
        self.assertEqual((decoded.from_slot, decoded.to_slot), (33, 32))
        inv = CharacterInventory()
        inv.slots[InventorySlot.for_client(0, 32)] = Item(
            ITEM_INVENTORY, 32, "Skin of Milk", "", 9990, stack=20
        )
        rendered = inv.render(show_empty=False)
        self.assertIn("General 10 (32)", rendered)
        self.assertNotIn("[OTHER / UNATTACHED]", rendered)


if __name__ == "__main__":
    unittest.main()
