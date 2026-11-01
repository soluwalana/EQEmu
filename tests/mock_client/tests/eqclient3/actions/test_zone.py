"""Zone sends one request and completes on OP_NewZone."""

import unittest

from harness import commands, fresh, inbox, kinds, opcodes

from eqclient3.actions.zone import Zone


class ZoneTest(unittest.TestCase):
    def test_a_zone_request_is_not_durable(self):
        self.assertFalse(Zone("freportw").durable)

    def test_one_request_then_new_zone(self):
        client, sheet = fresh()
        action = Zone("freportw")
        self.assertNotIn("OP_Assist", action.opcodes())
        action.step(client, sheet)
        self.assertEqual(opcodes(client), ["OP_ZoneChange"])
        self.assertEqual(len(client.outbound[0][1]), 100)
        self.assertEqual(action.waiting, ["ZONE"])
        self.assertNotIn("Form", kinds(client))
        action.step(client, sheet)
        self.assertEqual(opcodes(client), ["OP_ZoneChange"])
        inbox(action, "OP_NewZone", {"zone": "freportw"})
        action.step(client, sheet)
        self.assertTrue(action.complete)
        self.assertEqual(action.waiting, [])

    def test_closed_session_sends_nothing(self):
        client, sheet = fresh()
        client.session.closed = True
        action = Zone("freportw")
        action.step(client, sheet)
        self.assertEqual(client.outbound, [])
        self.assertFalse(action.complete)
        self.assertEqual(commands(client), [])

    def test_below_the_zone_floor_grinds_first(self):
        client, sheet = fresh()
        sheet.level = 10
        action = Zone("unrest")
        action.step(client, sheet)
        self.assertEqual(opcodes(client), [])
        self.assertEqual(kinds(client), ["Grind"])
        self.assertEqual(client.queue[0].level, 11)
        self.assertFalse(action.complete)


if __name__ == "__main__":
    unittest.main()
