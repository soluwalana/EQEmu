"""Travel walks to the next zoneline and completes when the world zone matches."""

import unittest

from harness import fresh, kinds, movement, opcodes

from eqclient3.actions.travel import Travel
from eqclient3.nav.travel import Transit, ZoneGraph
from eqclient3.world import Door


class TravelTest(unittest.TestCase):
    def test_walks_the_zoneline_and_does_not_zone(self):
        client, sheet = fresh()
        sheet.zoneline = (40.0, 0.0, 0.0)
        action = Travel("freportw")
        action.step(client, sheet)
        self.assertEqual(movement().advances[-1].dest, (40.0, 0.0, 0.0))
        self.assertNotIn("OP_ZoneChange", opcodes(client))
        sheet.zone = "freportw"
        action.step(client, sheet)
        self.assertTrue(action.complete)

    def test_below_the_zone_floor_grinds_first(self):
        client, sheet = fresh()
        sheet.level = 10
        sheet.zoneline = (40.0, 0.0, 0.0)
        action = Travel("unrest")
        action.step(client, sheet)
        self.assertFalse(action.complete)
        self.assertEqual(kinds(client), ["Grind"])
        self.assertEqual(client.queue[0].level, 11)
        self.assertEqual(movement().advances, [])
        action.step(client, sheet)
        self.assertEqual(kinds(client), ["Grind"])

    def test_walks_the_scripted_exit_when_the_graph_has_no_hop(self):
        client, sheet = fresh("tutorialb")
        graph = ZoneGraph()
        graph.index()
        sheet.zone_graph = graph
        sheet.exit_doors = {"tutorialb": {11: [9, 202]}}
        sheet.doors[11] = Door(11, "OBJ_CAVE_ENTRY_DARK", -164.1, 151.2, 25.0)
        action = Travel("qeynos")
        action.step(client, sheet)
        self.assertEqual(movement().advances[-1].dest, (-164.1, 151.2, 25.0))
        self.assertNotIn("OP_ZoneChange", opcodes(client))

    def test_walks_the_graph_transit(self):
        client, sheet = fresh("qeynos2")
        graph = ZoneGraph(zones={"qeynos2": 2, "qeynos": 1})
        graph.transits.append(Transit(zone="qeynos2", door_id=7, dest="qeynos", dest_id=1, x=-5.0, y=-151.0, z=1.5))
        graph.index()
        sheet.zone_graph = graph
        action = Travel("qeynos")
        action.step(client, sheet)
        self.assertEqual(movement().advances[-1].dest, (-5.0, -151.0, 1.5))


if __name__ == "__main__":
    unittest.main()
