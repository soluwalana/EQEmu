"""Deliver hands the item. A missing item completes it. It never appends Fetch."""

import unittest

from harness import fresh, kinds

from eqclient3.actions.deliver import Deliver


class DeliverTest(unittest.TestCase):
    def test_missing_item_completes_without_fetch(self):
        client, sheet = fresh()
        action = Deliver(9, 3)
        action.step(client, sheet)
        self.assertTrue(action.complete)
        self.assertNotIn("Fetch", kinds(client))

    def test_held_item_appends_talk_not_fetch(self):
        client, sheet = fresh()
        sheet.bags[22] = 9
        action = Deliver(9, 3)
        action.step(client, sheet)
        self.assertFalse(action.complete)
        self.assertTrue(action.handed)
        self.assertIn("Talk", kinds(client))
        self.assertNotIn("Fetch", kinds(client))
        action.step(client, sheet)
        self.assertTrue(action.complete)
        self.assertNotIn("Fetch", kinds(client))


if __name__ == "__main__":
    unittest.main()
