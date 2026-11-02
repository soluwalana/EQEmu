"""The nearest merchant this level can reach, and the ones saved for later."""

import unittest
from types import SimpleNamespace

from harness import fresh

from eqclient3.actions.fetch import Fetch
from eqclient3.actions.shop import choose_offer
from eqclient3.actions.travel import Travel
from eqclient3.data.factions import ensure_factions
from eqclient3.data.merchants import MerchantBook


def _book(sellers: dict[int, str], cost: int = 500) -> MerchantBook:
    book = MerchantBook()
    book.by_item[50] = {"cost": cost, "npcs": list(sellers)}
    for npc_id, zone in sellers.items():
        book.by_npc[npc_id] = {"zone": 1, "where": zone, "name": f"Seller {npc_id}"}
    book.index()
    return book


class ShopTest(unittest.TestCase):
    def test_nearest_open_seller_wins(self):
        _client, sheet = fresh()
        sheet.zone = "ecommons"
        sheet.level = 6
        offer = choose_offer(sheet, 50, _book({8: "qeynos", 9: "ecommons"}))
        self.assertIsNotNone(offer)
        assert offer is not None
        self.assertEqual(offer.zone, "ecommons")
        self.assertEqual(offer.hops, 0)

    def test_a_hostile_merchant_is_skipped(self):
        _client, sheet = fresh()
        sheet.zone = "qeynos"
        sheet.level = 6
        factions = ensure_factions()
        saved = factions.primary_of.get("seller 8")
        factions.primary_of["seller 8"] = 4242
        sheet.faction(4242).amount = -50
        try:
            offer = choose_offer(sheet, 50, _book({8: "qeynos"}))
        finally:
            if saved is None:
                factions.primary_of.pop("seller 8", None)
            else:
                factions.primary_of["seller 8"] = saved
        self.assertIsNone(offer)
        self.assertNotIn(50, sheet.later_shops)

    def test_a_high_zone_on_the_walk_is_remembered(self):
        _client, sheet = fresh()
        sheet.zone = "ecommons"
        sheet.level = 6
        offer = choose_offer(sheet, 50, _book({8: "draniksscar"}, cost=100))
        self.assertIsNone(offer)
        later = sheet.later_shops[50]
        self.assertEqual(later.blocked_zone, "draniksscar")

    def test_short_on_coin_farms_money_and_a_level_gate_farms_xp(self):
        client, sheet = fresh()
        from eqclient3.actions import fetch as fetch_mod

        book = _book({8: "draniksscar"}, cost=500)
        saved = (fetch_mod._book, fetch_mod._loaded)
        fetch_mod._book = book
        fetch_mod._loaded = True
        try:
            sheet.zone = "ecommons"
            sheet.level = 6
            short = Fetch(50, 1, "gear 50")
            short.step(client, sheet)
            self.assertIn("Kill", [type(row).__name__ for row in client.queue])
            self.assertFalse(any(isinstance(row, Travel) and row.destination == "draniksscar" for row in client.queue))
            sheet.set_coin(1, 0, 0, 0)
            sheet.later_shops.clear()
            paid = Fetch(50, 1, "gear 50")
            paid.step(client, sheet)
        finally:
            fetch_mod._book, fetch_mod._loaded = saved
        self.assertIn("Grind", [type(row).__name__ for row in client.queue])

    def test_a_drop_near_this_level_is_farmed_instead_of_bought(self):
        client, sheet = fresh()
        from eqclient3.actions import fetch as fetch_mod

        saved = (fetch_mod._book, fetch_mod._loaded)
        fetch_mod._book = _book({8: "qeynos"})
        fetch_mod._loaded = True
        try:
            sheet.zone = "ecommons"
            sheet.level = 6
            sheet.set_coin(1, 0, 0, 0)
            client.journal.set_soulbind(sheet.name, "ecommons")
            sheet.plans = {
                50: SimpleNamespace(drop=SimpleNamespace(zone="ecommons", above_level=False, level=6, spawns=[3]))
            }
            Fetch(50, 1, "gear 50").step(client, sheet)
        finally:
            fetch_mod._book, fetch_mod._loaded = saved
        kinds = [type(row).__name__ for row in client.queue]
        self.assertIn("Kill", kinds)
        self.assertNotIn("Travel", kinds)

    def test_the_tutorial_exit_queues_a_crafted_pack_and_two_bought_ones(self):
        client, sheet = fresh()
        from eqclient3.actions.craft import Craft
        from eqclient3.quests.produce import BACKPACK_BAND, _queue_backpacks

        _queue_backpacks(client, sheet, client.journal)
        fetches = {row.item_id: row for row in client.queue if isinstance(row, Fetch)}
        made = [row for row in client.queue if isinstance(row, Craft)]
        self.assertEqual(fetches[17005].count, 3)
        self.assertEqual(fetches[17046].count, 3)
        self.assertEqual(len(made), 1)
        self.assertEqual(made[0].recipe.result, 17969)
        self.assertIn(12089, {item_id for item_id, _count in made[0].recipe.components})
        self.assertEqual(made[0].count, 2)
        self.assertEqual({row.priority for row in client.queue}, {BACKPACK_BAND})
        self.assertIs(client.queue.winner(), made[0])
