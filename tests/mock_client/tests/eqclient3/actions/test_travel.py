"""Travel walks to the next zoneline and completes when the world zone matches."""

import unittest

from harness import fresh, movement, opcodes

from eqclient3.actions.travel import Travel


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


if __name__ == "__main__":
    unittest.main()
