"""Craft fetches a missing component, then waits on inbound OP_TradeSkillCombine."""

import unittest
from types import SimpleNamespace

from harness import fresh, inbox, kinds, opcodes

from eqclient3.actions.craft import Craft


class CraftTest(unittest.TestCase):
    def test_missing_component_appends_fetch(self):
        client, sheet = fresh()
        recipe = SimpleNamespace(components=((7, 1),), combine_slot=9)
        action = Craft(recipe)
        self.assertNotIn("OP_Assist", action.opcodes())
        action.step(client, sheet)
        self.assertIn("Fetch", kinds(client))
        self.assertTrue(action.yielding)
        self.assertNotIn("CRAFT", action.waiting)

    def test_combine_then_the_reply_completes(self):
        client, sheet = fresh()
        sheet.bags[22] = 7
        recipe = SimpleNamespace(components=((7, 1),), combine_slot=9, needs_click=True, drop_id=4)
        action = Craft(recipe)
        action.step(client, sheet)
        self.assertEqual(opcodes(client)[-1], "OP_ClickObject")
        self.assertNotIn("CRAFT", action.waiting)
        action.step(client, sheet)
        self.assertEqual(opcodes(client)[-1], "OP_TradeSkillCombine")
        self.assertEqual(action.waiting, ["CRAFT"])
        action.step(client, sheet)
        self.assertFalse(action.complete)
        inbox(action, "OP_TradeSkillCombine", b"")
        action.step(client, sheet)
        self.assertTrue(action.complete)

    def test_station_in_another_zone_appends_zone(self):
        client, sheet = fresh()
        sheet.bags[22] = 7
        recipe = SimpleNamespace(components=((7, 1),), zone="freportw", combine_slot=9)
        Craft(recipe).step(client, sheet)
        self.assertIn("Zone", kinds(client))


if __name__ == "__main__":
    unittest.main()
