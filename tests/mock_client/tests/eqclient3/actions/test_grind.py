"""Grind camps at any open XP zone until the target level."""

import unittest

from harness import fresh, kinds, movement

from eqclient3.actions.grind import Grind


class GrindTest(unittest.TestCase):
    def test_kills_at_the_camp_we_are_already_in(self):
        client, sheet = fresh("freportw")
        sheet.level = 2
        action = Grind(4)
        action.step(client, sheet)
        self.assertFalse(action.complete)
        kills = [row for row in client.queue if type(row).__name__ == "Kill"]
        self.assertEqual(len(kills), 1)
        self.assertEqual(kills[0].camp, "freportw")
        self.assertEqual(kills[0].level, 4)
        sheet.zone = "qeynos"
        other = Grind(4)
        other.step(client, sheet)
        camps = [row.camp for row in client.queue if type(row).__name__ == "Kill"]
        self.assertEqual(camps, ["freportw", "qeynos"])

    def test_walks_to_an_open_camp_when_this_zone_is_not_one(self):
        client, sheet = fresh("tutorialb")
        sheet.level = 2
        sheet.zoneline = (40.0, 0.0, 0.0)
        action = Grind(4)
        action.step(client, sheet)
        self.assertEqual(kinds(client), [])
        self.assertEqual(action.camp, "qeynos")
        self.assertEqual(movement().advances[-1].dest, (40.0, 0.0, 0.0))

    def test_completes_once_the_level_is_reached(self):
        client, sheet = fresh()
        sheet.level = 4
        action = Grind(4)
        action.step(client, sheet)
        self.assertTrue(action.complete)
        self.assertEqual(kinds(client), [])


if __name__ == "__main__":
    unittest.main()
