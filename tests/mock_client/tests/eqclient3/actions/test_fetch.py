"""Fetch obtains an item. A drop in another zone is Travel, not Zone."""

import unittest
from types import SimpleNamespace

from harness import fresh, kinds

from eqclient3.actions.fetch import Fetch


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


if __name__ == "__main__":
    unittest.main()
