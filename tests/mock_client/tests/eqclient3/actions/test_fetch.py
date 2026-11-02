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
        action = Fetch(0, 1, "gold", copper=500)
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
        action = Fetch(50, 1, "gear 50", copper=500)
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
        gear = Fetch(2010, 1, "gear 2010", copper=1800)
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

    def test_gear_walks_to_its_merchant(self):
        from harness import mob

        from eqclient3.actions import fetch as fetch_mod
        from eqclient3.data.merchants import MerchantBook

        book = MerchantBook()
        book.by_item[50] = {"cost": 500, "npcs": [8]}
        book.by_npc[8] = {"zone": 1, "where": "qeynos", "name": "Smythe"}
        book.index()
        saved = (fetch_mod._book, fetch_mod._loaded)
        fetch_mod._book = book
        fetch_mod._loaded = True
        try:
            self.sheet.zone = "ecommons"
            self.sheet.set_coin(1, 0, 0, 0)
            action = Fetch(50, 1, "gear 50", copper=500)
            action.source = "fetch:50"
            action.step(self.client, self.sheet)
            trips = [row for row in self.client.queue if type(row).__name__ == "Travel"]
            self.assertEqual([row.destination for row in trips], ["qeynos"])
            self.assertEqual(action.priority, 0)
            self.sheet.zone = "qeynos"
            mob(self.sheet, 12, name="Smythe")
            action.step(self.client, self.sheet)
            trades = [row for row in self.client.queue if type(row).__name__ == "Trade"]
            self.assertEqual([row.partner for row in trades], [12])
        finally:
            fetch_mod._book, fetch_mod._loaded = saved

    def test_an_empty_plan_walks_to_the_ground_spawn(self):
        from eqclient3.actions import fetch as fetch_mod

        saved = fetch_mod.ground_at
        fetch_mod.ground_at = lambda _item_id, _zone_id, _zone: ((-53.6, -187.9, 15.2),)
        try:
            self.sheet.zone = "tutorialb"
            self.sheet.zone_id = 189
            action = Fetch(59955, 1, "Hail Xenaida")
            action.source = "task:1448:3"
            action.step(self.client, self.sheet)
            self.assertEqual(self.sheet.movement.plans, [((-53.6, -187.9, 15.2), "run")])
        finally:
            fetch_mod.ground_at = saved

    def test_a_ground_spawn_on_that_point_is_picked_up(self):
        from eqclient3.actions import fetch as fetch_mod
        from eqclient3.world import GroundSpawn

        saved = fetch_mod.ground_at
        fetch_mod.ground_at = lambda _item_id, _zone_id, _zone: ((-53.6, -187.9, 15.2),)
        try:
            self.sheet.zone = "tutorialb"
            self.sheet.zone_id = 189
            self.sheet.ground[4] = GroundSpawn(4, "IT401_ACTORDEF", -53.6, -187.9, 15.2)
            action = Fetch(59955, 1, "Hail Xenaida")
            action.source = "task:1448:3"
            action.step(self.client, self.sheet)
            picks = [row for row in self.client.queue if type(row).__name__ == "Pickup"]
            self.assertEqual([row.drop_id for row in picks], [4])
            self.assertEqual(picks[0].item_id, 59955)
        finally:
            fetch_mod.ground_at = saved


class GroundSpawnParseTest(unittest.TestCase):
    def test_a_point_box_is_the_spawn(self):
        from eqclient3.data.ground import read_ground

        rows = [
            "INSERT INTO `zone` VALUES",
            "('tutorialb',415,'','The Mines of Gloomingdeep',NULL,18,-147,20,0,0,0,255,0,189);",
            "INSERT INTO `ground_spawns` VALUES",
            "(62,189,0,-53.6,-187.9,15.2,-53.6,-187.9,0,'IT401_ACTORDEF',59955,1,'Gloom Musrooms',30,-1,-1,NULL,NULL),",
        ]
        spots, names = read_ground(rows)
        self.assertEqual(names[189], "tutorialb")
        self.assertEqual(spots[59955][0].zone_id, 189)
        self.assertEqual((spots[59955][0].x, spots[59955][0].y, spots[59955][0].z), (-53.6, -187.9, 15.2))


if __name__ == "__main__":
    unittest.main()
