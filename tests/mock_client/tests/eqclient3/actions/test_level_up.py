"""LevelUp appends a fetch and a scribe per spell, one train, and one gear fetch."""

import unittest

from harness import fresh, kinds

from eqclient3.actions.level_up import LevelUp


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


if __name__ == "__main__":
    unittest.main()
