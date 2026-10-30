"""Zone: one request, an empty inbox, then OP_NewZone. A closed session sends nothing."""

import unittest

from harness import fresh, inbox, opcodes

from eqclient3.actions.zone import Zone


class ZoneSteps(unittest.TestCase):
    def test_open_session_then_new_zone(self):
        client, sheet = fresh()
        action = Zone("freportw")
        action.step(client, sheet)
        self.assertEqual(opcodes(client), ["OP_ZoneChange"])
        action.step(client, sheet)
        self.assertEqual(opcodes(client), ["OP_ZoneChange"])
        inbox(action, "OP_NewZone", {"zone": "freportw"})
        action.step(client, sheet)
        self.assertTrue(action.complete)

    def test_closed_session_sends_nothing(self):
        client, sheet = fresh()
        client.session.closed = True
        Zone("freportw").step(client, sheet)
        self.assertEqual(client.outbound, [])


if __name__ == "__main__":
    unittest.main()
