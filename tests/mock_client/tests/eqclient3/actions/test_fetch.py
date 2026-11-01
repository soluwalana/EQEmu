"""Fetch obtains an item. A drop in another zone is Travel, not Zone."""

import unittest
from types import SimpleNamespace

from harness import fresh, kinds

from eqclient3.actions.fetch import Fetch
from eqclient3.actions.support import FetchPlan, gear_vendor_trip
from eqclient3.actions.travel import Travel
from eqclient3.actions.zone import Zone


class FetchTest(unittest.TestCase):
    def setUp(self):
        self.client, self.sheet = fresh()
        self.client.journal.set_soulbind("Hero", "qeynos")

    def test_held_count_completes(self):
        self.sheet.bags[22] = 7
        action = Fetch(7, 1, "silk")
        action.step(self.client, self.sheet)
        self.assertTrue(action.complete)
        self.assertEqual(kinds(self.client), [])

    def test_drop_here_appends_one_kill_per_spawn(self):
        self.sheet.plans = {7: SimpleNamespace(drop=SimpleNamespace(zone="qeynos", above_level=False, spawns=[3, 4]))}
        action = Fetch(7, 1, "drop")
        action.step(self.client, self.sheet)
        kills = [row for row in self.client.queue if type(row).__name__ == "Kill"]
        self.assertEqual([row.spawn_id for row in kills], [3, 4])
        self.assertTrue(action.yielding)
        self.assertEqual(self.client.queue.winner().spawn_id, 4)
        action.step(self.client, self.sheet)
        self.assertEqual(len(kills), 2)

    def test_drop_above_level_appends_the_camp(self):
        self.sheet.plans = {
            7: SimpleNamespace(
                drop=SimpleNamespace(
                    zone="qeynos",
                    above_level=True,
                    camp=(1, 2, 3),
                    level=20,
                    spawns=[3],
                )
            )
        }
        Fetch(7, 1, "drop").step(self.client, self.sheet)
        kills = [row for row in self.client.queue if type(row).__name__ == "Kill"]
        self.assertEqual(len(kills), 1)
        self.assertEqual(kills[0].camp, (1, 2, 3))
        self.assertIsNone(kills[0].spawn_id)

    def test_drop_elsewhere_is_travel_not_zone(self):
        self.sheet.plans = {7: SimpleNamespace(drop=SimpleNamespace(zone="gfaydark", above_level=False, spawns=[3]))}
        Fetch(7, 1, "drop").step(self.client, self.sheet)
        self.assertIn("Travel", kinds(self.client))
        self.assertNotIn("Zone", kinds(self.client))

    def test_merchant_here_appends_trade(self):
        self.sheet.plans = {7: SimpleNamespace(merchant=SimpleNamespace(npc=8, zone="qeynos"))}
        Fetch(7, 1, "buy").step(self.client, self.sheet)
        self.assertIn("Trade", kinds(self.client))

    def test_ground_here_appends_pickup(self):
        self.sheet.plans = {7: SimpleNamespace(ground=SimpleNamespace(drop_id=4, point=(1, 0, 0), zone="qeynos"))}
        Fetch(7, 1, "ground").step(self.client, self.sheet)
        self.assertIn("Pickup", kinds(self.client))

    def test_vendor_in_another_zone_appends_zone(self):
        self.sheet.plans = {7: SimpleNamespace(vendor_zone="freportw")}
        Fetch(7, 1, "vendor").step(self.client, self.sheet)
        self.assertIn("Zone", kinds(self.client))
        self.assertNotIn("Travel", kinds(self.client))

    def test_gold_fetch_kills_at_an_open_camp_until_the_coin_is_held(self):
        self.sheet.zone = "freportw"
        self.sheet.level = 2
        action = Fetch(0, 1, "gold", gold=500)
        action.step(self.client, self.sheet)
        self.assertFalse(action.complete)
        kills = [row for row in self.client.queue if type(row).__name__ == "Kill"]
        self.assertEqual(len(kills), 1)
        self.assertEqual(kills[0].camp, "freportw")
        self.assertEqual(kills[0].level, 3)
        self.sheet.set_coin(1, 0, 0, 0)
        action.step(self.client, self.sheet)
        self.assertTrue(action.complete)

    def test_gear_short_on_coin_earns_before_it_buys(self):
        self.sheet.zone = "qeynos"
        self.sheet.level = 2
        self.sheet.plans = {50: SimpleNamespace(merchant=SimpleNamespace(npc=8, zone="qeynos"))}
        action = Fetch(50, 1, "gear 50", gold=500)
        action.step(self.client, self.sheet)
        self.assertNotIn("Trade", kinds(self.client))
        self.assertIn("Kill", kinds(self.client))
        self.sheet.set_coin(1, 0, 0, 0)
        action.step(self.client, self.sheet)
        self.assertIn("Trade", kinds(self.client))

    def test_the_mines_do_not_grind_for_gear_coin(self):
        self.sheet.zone = "tutorialb"
        self.sheet.level = 1
        self.sheet.plans = {2010: FetchPlan(vendor_zone="poknowledge")}
        gear = Fetch(2010, 1, "gear 2010", gold=1800)
        gear.source = "fetch:2010"
        self.client.queue.append(gear, self.sheet, self.client.journal, "Hero")
        exit_zone = Zone("poknowledge")
        exit_zone.source = "task:1448:9"
        self.assertFalse(gear_vendor_trip(self.client, self.sheet, "poknowledge", exit_zone.source))
        gear.step(self.client, self.sheet)
        self.assertNotIn(gear, list(self.client.queue))
        self.assertFalse(self.client.journal.is_resolved("Hero", gear.source))
        self.assertNotIn("Kill", kinds(self.client))
        self.assertNotIn("Travel", kinds(self.client))

        travel = Travel("qeynos")
        travel.source = "fetch:2010#gold:travel:qeynos"
        self.client.queue.append(travel, self.sheet, self.client.journal, "Hero")
        travel.step(self.client, self.sheet)
        self.assertNotIn(travel, list(self.client.queue))
        self.assertFalse(self.client.journal.is_resolved("Hero", travel.source))

        self.client.queue.append(gear, self.sheet, self.client.journal, "Hero")
        zone = Zone("poknowledge")
        zone.source = "zone:poknowledge"
        self.client.queue.append(zone, self.sheet, self.client.journal, "Hero")
        zone.step(self.client, self.sheet)
        self.assertNotIn(zone, list(self.client.queue))
        self.assertFalse(self.client.journal.is_resolved("Hero", zone.source))
        self.assertEqual(self.client.outbound, [])


if __name__ == "__main__":
    unittest.main()
