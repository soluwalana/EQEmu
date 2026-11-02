"""LevelUp appends a fetch and a scribe per spell, one train, and one gear fetch."""

import unittest

from harness import fresh, kinds

from eqclient3.actions import fetch as fetch_mod
from eqclient3.actions.level_up import LevelUp
from eqclient3.data.merchants import MerchantBook
from eqclient3.world import Bot


class LevelUpTest(unittest.TestCase):
    def test_appends_scrolls_scribe_train_and_gear(self):
        client, sheet = fresh()
        sheet.level_spells = [
            {"level": 2, "spell_id": 11, "scroll_id": 100, "slot": 22},
            {"level": 2, "spell_id": 12, "scroll_id": 101, "slot": 23},
        ]
        sheet.level_gear = [{"level": 2, "item_id": 50}]
        sheet.guildmaster = 7
        action = LevelUp(2)
        action.step(client, sheet)
        self.assertTrue(action.complete)
        names = kinds(client)
        self.assertEqual(names.count("Fetch"), 3)
        self.assertEqual(names.count("ScribeSpell"), 2)
        self.assertEqual(names.count("Train"), 1)
        self.assertTrue(action.yielding)

    def test_the_mines_do_not_queue_gear(self):
        client, sheet = fresh("tutorialb")
        sheet.level_spells = [{"level": 1, "spell_id": 11, "scroll_id": 100, "slot": 22}]
        sheet.level_gear = [{"level": 1, "item_id": 2010}]
        sheet.guildmaster = 7
        action = LevelUp(1)
        action.step(client, sheet)
        self.assertTrue(action.complete)
        items = [row.item_id for row in client.queue if type(row).__name__ == "Fetch"]
        self.assertIn(100, items)
        self.assertNotIn(2010, items)
        self.assertNotIn("Travel", kinds(client))
        self.assertNotIn("Kill", kinds(client))

    def test_player_and_companion_kits_carry_their_price(self):
        client, sheet = fresh()
        sheet.class_id = 1
        sheet.bots.roster.append(Bot(name="Mira", class_id=2, level=2))
        book = MerchantBook()
        book.by_item[2001] = {"cost": 400}
        saved = (fetch_mod._book, fetch_mod._loaded)
        fetch_mod._book = book
        fetch_mod._loaded = True
        try:
            LevelUp(2).step(client, sheet)
        finally:
            fetch_mod._book, fetch_mod._loaded = saved
        fetches = [row for row in client.queue if type(row).__name__ == "Fetch"]
        items = [row.item_id for row in fetches]
        for item_id in (5013, 2001, 2004, 2008, 2010, 6011, 1001, 1004, 1008, 1010):
            self.assertIn(item_id, items)
        priced = [row for row in fetches if row.item_id == 2001]
        self.assertEqual(priced[0].copper, 400)
        self.assertEqual(priced[0].priority, fetch_mod.GEAR_BAND)


if __name__ == "__main__":
    unittest.main()
