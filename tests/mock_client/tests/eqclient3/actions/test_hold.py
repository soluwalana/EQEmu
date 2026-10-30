"""Hold does not swing. The spawn's corpse finishes it."""

import struct
import unittest

from harness import fresh, inbox, opcodes

from eqclient3.actions.hold import Hold


class HoldTest(unittest.TestCase):
    def test_no_swing_until_the_corpse(self):
        client, sheet = fresh()
        action = Hold(8)
        action.step(client, sheet)
        self.assertEqual(client.outbound, [])
        self.assertFalse(action.complete)
        inbox(action, "OP_BecomeCorpse", struct.pack("<I", 8))
        action.step(client, sheet)
        self.assertTrue(action.complete)
        self.assertNotIn("OP_AutoAttack", opcodes(client))


if __name__ == "__main__":
    unittest.main()
