"""Craft fetches a missing component, then waits on inbound OP_TradeSkillCombine."""

import unittest

from harness import fresh, inbox, kinds, opcodes

from eqclient3.actions.craft import WORLD_COMBINE, Craft
from eqclient3.data.recipes import Recipe
from eqclient3.structs import OP_MoveItem, OP_SimpleMessage, OP_TradeSkillCombine


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
        inbox(action, "OP_TradeSkillCombine", b"")
        action.step(client, sheet)
        self.assertFalse(action.complete)
        sheet.cursor = 8
        action.step(client, sheet)
        self.assertTrue(action.complete)

    def test_a_failed_combine_fetches_the_components_again(self):
        client, sheet = fresh()
        sheet.bags[22] = 7
        recipe = Recipe(id=1, result=8, components=((7, 1),))
        action = Craft(recipe)
        action.step(client, sheet)
        sheet.bags.pop(22)
        inbox(action, "OP_SimpleMessage", OP_SimpleMessage(336))
        action.step(client, sheet)
        self.assertFalse(action.complete)
        self.assertIn("Fetch", kinds(client))
        fetched = next(row for row in client.queue if type(row).__name__ == "Fetch")
        self.assertEqual(fetched.item_id, 7)

    def test_world_station_combines_in_the_station_slot(self):
        client, sheet = fresh()
        sheet.bags[22] = 7
        recipe = Recipe(id=1, result=8, components=((7, 1),), container=17)
        Craft(recipe).step(client, sheet)
        sent = OP_TradeSkillCombine.deserialize(client.outbound[-1][1])
        self.assertEqual(sent.container_slot, WORLD_COMBINE)

    def test_kit_moves_the_component_in_then_combines(self):
        client, sheet = fresh()
        sheet.bags[22] = 7
        sheet.bags[23] = 99
        recipe = Recipe(id=1, result=8, components=((7, 1),), container=99)
        action = Craft(recipe)
        action.step(client, sheet)
        sent = OP_MoveItem.deserialize(client.outbound[-1][1])
        self.assertEqual((sent.from_slot, sent.to_slot), (22, 451))
        sheet.bags.pop(22)
        sheet.bags[451] = 7
        inbox(action, "OP_ItemPacket", {"slot": 451, "item_id": 7})
        action.step(client, sheet)
        combined = OP_TradeSkillCombine.deserialize(client.outbound[-1][1])
        self.assertEqual(combined.container_slot, 23)

    def test_the_kit_moves_to_a_general_slot_before_the_combine(self):
        client, sheet = fresh()
        sheet.bags[22] = 17005
        sheet.bags[251] = 99
        sheet.bags[23] = 7
        recipe = Recipe(id=1, result=8, components=((7, 1),), container=99)
        Craft(recipe).step(client, sheet)
        sent = OP_MoveItem.deserialize(client.outbound[-1][1])
        self.assertEqual((sent.from_slot, sent.to_slot), (251, 24))
        self.assertNotIn("OP_TradeSkillCombine", opcodes(client))

    def test_the_handmade_backpack_practices_before_it_combines(self):
        client, sheet = fresh()
        sheet.skills[61] = 0
        Craft(_handmade()).step(client, sheet)
        self.assertEqual(kinds(client), ["Practice"])
        practice = client.queue[-1]
        self.assertEqual((practice.skill_id, practice.want, practice.skip), (61, 88, 2685))
        self.assertNotIn("OP_TradeSkillCombine", opcodes(client))

    def test_tailoring_at_trivial_combines_the_backpack(self):
        client, sheet = fresh()
        sheet.skills[61] = 88
        sheet.bags[22] = 2787
        sheet.bags[23] = 12089
        sheet.bags[24] = 92882
        Craft(_handmade()).step(client, sheet)
        self.assertNotIn("Practice", kinds(client))
        self.assertIn("OP_MoveItem", opcodes(client))

    def test_practice_drills_a_lower_combine_and_marks_it_to_sell(self):
        import eqclient3.actions.practice as practice_mod

        client, sheet = fresh()
        sheet.skills[61] = 0
        drill = Recipe(id=2, result=9, components=((3, 1),), skill=61, trivial=20, enabled=1)
        book = _book(drill, _handmade())
        previous = practice_mod._BOOK
        practice_mod._BOOK = book
        try:
            action = practice_mod.Practice(61, 88, skip=2685, protect=(17969, 2787, 12089, 92882))
            action.step(client, sheet)
        finally:
            practice_mod._BOOK = previous
        queued = [row for row in client.queue if type(row).__name__ == "Craft"]
        self.assertEqual(len(queued), 1)
        self.assertEqual(queued[0].recipe.id, 2)
        self.assertTrue(queued[0].practicing)
        self.assertIn(9, client.journal.sell_marks("Hero"))
        self.assertNotIn(17969, client.journal.sell_marks("Hero"))

    def test_practice_stops_when_the_skill_reaches_trivial(self):
        client, sheet = fresh()
        sheet.skills[61] = 88
        from eqclient3.actions.practice import Practice

        action = Practice(61, 88, skip=2685)
        action.step(client, sheet)
        self.assertTrue(action.complete)
        self.assertEqual(kinds(client), [])


def _handmade() -> Recipe:
    return Recipe(
        id=2685,
        result=17969,
        components=((2787, 1), (12089, 1)),
        container=92882,
        skill=61,
        trivial=88,
        enabled=1,
    )


def _book(*recipes: Recipe):
    from eqclient3.data.recipes import RecipeBook

    book = RecipeBook()
    for recipe in recipes:
        book.by_id[recipe.id] = recipe
    book.index()
    return book


if __name__ == "__main__":
    unittest.main()
