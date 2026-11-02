"""Distribute empties worn slots, then one give. The bag leaving the item finishes it."""

import struct
import unittest

from harness import commands, fresh, inbox

from eqclient3.actions.distribute import Distribute
from eqclient3.inventory import assign as assign_mod


class DistributeTest(unittest.TestCase):
    def test_remove_then_give_then_bag(self):
        client, sheet = fresh()
        client.journal.set_worn("Hero", "Cleric", 13, 9)
        sheet.bags[22] = 50
        action = Distribute(50, "Cleric", [13])
        action.step(client, sheet)
        self.assertEqual(commands(client), ["^inventoryremove 13 byname Cleric"])
        inbox(action, "OP_DeleteItem", struct.pack("<I", 13))
        action.step(client, sheet)
        self.assertEqual(client.journal.worn("Hero", "Cleric").get(13), 0)
        self.assertEqual(commands(client)[-1], "^inventorygive byname Cleric")
        sheet.bags.pop(22)
        action.step(client, sheet)
        self.assertTrue(action.complete)
        self.assertEqual(client.journal.worn("Hero", "Cleric").get(13), 50)

    def test_a_give_is_not_repeated_and_acceptance_finishes_it(self):
        client, sheet = fresh()
        sheet.bags[22] = 50
        action = Distribute(50, "Cleric", [])
        action.step(client, sheet)
        action.step(client, sheet)
        self.assertEqual(commands(client), ["^inventorygive byname Cleric"])
        self.assertFalse(action.complete)
        inbox(action, "OP_SpecialMesg", {"speaker": "Cleric", "message": "I have accepted a sword."})
        action.step(client, sheet)
        self.assertTrue(action.complete)

    def test_a_player_piece_is_taken_back_once(self):
        client, sheet = fresh()
        saved = assign_mod._ITEMS
        assign_mod._ITEMS = {54226: {"slots": 4096, "classes": 65535, "races": 65535, "ac": 2, "item": 54226}}
        try:
            sheet.class_id = 3
            sheet.race = 1
            sheet.level = 7
            action = Distribute(54226, "Entwar", [])
            action.step(client, sheet)
            action.step(client, sheet)
            self.assertEqual(commands(client), ["^inventoryremove 12 byname Entwar"])
            inbox(
                action,
                "OP_SpecialMesg",
                {"speaker": "Entwar", "message": "I have unequipped the gloves from my Hands (Slot 12)."},
            )
            action.step(client, sheet)
            self.assertTrue(action.complete)
        finally:
            assign_mod._ITEMS = saved


if __name__ == "__main__":
    unittest.main()
