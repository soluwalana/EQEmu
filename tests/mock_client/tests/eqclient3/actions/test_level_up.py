"""LevelUp appends a fetch and a scribe per spell, one train, and one gear fetch."""

import unittest
from unittest.mock import patch

from harness import fresh, kinds

from eqclient3.actions import fetch as fetch_mod
from eqclient3.actions.level_up import LevelUp
from eqclient3.data.merchants import MerchantBook
from eqclient3.quests.produce import _BURLAP
from eqclient3.world import Bot


class LevelUpTest(unittest.TestCase):
    def setUp(self) -> None:
        self._burlap = patch("eqclient3.quests.produce._BURLAP", ())
        self._rewarded = patch("eqclient3.actions.level_up._rewarded", return_value=False)
        self._burlap.start()
        self._rewarded.start()

    def tearDown(self) -> None:
        self._rewarded.stop()
        self._burlap.stop()

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
        self.assertIn(2010, items)
        self.assertNotIn("Travel", kinds(client))
        self.assertNotIn("Kill", kinds(client))

    def test_level_one_burlap_is_produced_inside_the_mine(self):
        client, sheet = fresh("tutorialb")
        sheet.class_id = 3
        produced: list[int] = []

        def rewarded(item_id: int) -> bool:
            return item_id in _BURLAP

        def fake_produce(
            loop: object,
            world: object,
            journal: object = None,
            *,
            item_id: int | None = None,
            graph: object = None,
            leaving_tutorial: bool = False,
        ) -> None:
            del loop, world, journal, graph, leaving_tutorial
            if item_id is not None:
                produced.append(item_id)

        with (
            patch("eqclient3.quests.produce._BURLAP", _BURLAP),
            patch("eqclient3.actions.level_up._rewarded", rewarded),
            patch("eqclient3.actions.level_up.produce", fake_produce),
        ):
            LevelUp(1).step(client, sheet)
        self.assertEqual(sorted(produced), sorted(_BURLAP))
        fetches = [row.item_id for row in client.queue if type(row).__name__ == "Fetch"]
        for item_id in _BURLAP:
            self.assertNotIn(item_id, fetches)

    def test_burlap_is_the_kit_through_level_ten(self):
        from eqclient3.quests.produce import kit_for

        with patch("eqclient3.quests.produce._BURLAP", _BURLAP):
            low = kit_for(3, 10)
            high = kit_for(3, 11)
        for item_id in _BURLAP:
            self.assertIn(item_id, low)
            self.assertNotIn(item_id, high)

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
