"""Distribute empties worn slots, then one give. The bag leaving the item finishes it."""

import struct
import unittest

from harness import commands, fresh, inbox

from eqclient3.actions.distribute import Distribute


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


if __name__ == "__main__":
    unittest.main()
