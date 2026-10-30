"""Craft fetches a missing component, then waits on inbound OP_TradeSkillCombine."""

import unittest

from harness import fresh, inbox, kinds, opcodes

from eqclient3.actions.craft import WORLD_COMBINE, Craft
from eqclient3.data.recipes import Recipe
from eqclient3.structs import OP_TradeSkillCombine


class CraftTest(unittest.TestCase):
    def test_missing_component_appends_fetch(self):
        client, sheet = fresh()
        recipe = Recipe(id=1, result=8, components=((7, 1),))
        action = Craft(recipe)
        self.assertNotIn("OP_Assist", action.opcodes())
        action.step(client, sheet)
        self.assertIn("Fetch", kinds(client))
        self.assertTrue(action.yielding)
        self.assertNotIn("CRAFT", action.waiting)

    def test_combine_then_the_reply_completes(self):
        client, sheet = fresh()
        sheet.bags[22] = 7
        recipe = Recipe(id=1, result=8, components=((7, 1),))
        action = Craft(recipe)
        action.step(client, sheet)
        self.assertEqual(opcodes(client)[-1], "OP_TradeSkillCombine")
        self.assertEqual(action.waiting, ["CRAFT"])
        action.step(client, sheet)
        self.assertFalse(action.complete)
        inbox(action, "OP_TradeSkillCombine", b"")
        action.step(client, sheet)
        self.assertTrue(action.complete)

    def test_world_station_combines_in_the_station_slot(self):
        client, sheet = fresh()
        sheet.bags[22] = 7
        recipe = Recipe(id=1, result=8, components=((7, 1),), container=17)
        Craft(recipe).step(client, sheet)
        sent = OP_TradeSkillCombine.deserialize(client.outbound[-1][1])
        self.assertEqual(sent.container_slot, WORLD_COMBINE)

    def test_kit_combines_in_the_bag_slot(self):
        client, sheet = fresh()
        sheet.bags[22] = 7
        sheet.bags[23] = 99
        recipe = Recipe(id=1, result=8, components=((7, 1),), container=99)
        Craft(recipe).step(client, sheet)
        sent = OP_TradeSkillCombine.deserialize(client.outbound[-1][1])
        self.assertEqual(sent.container_slot, 23)


if __name__ == "__main__":
    unittest.main()
