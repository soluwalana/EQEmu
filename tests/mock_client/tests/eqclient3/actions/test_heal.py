"""Heal sends one cast and completes when the bar comes back."""

import struct
import unittest

from harness import commands, fresh, inbox, opcodes

from eqclient3.actions.heal import Heal


class HealTest(unittest.TestCase):
    def test_one_cast_then_the_bar(self):
        client, sheet = fresh()
        action = Heal("Hero")
        self.assertEqual(action.priority, 260)
        self.assertNotIn("OP_Assist", action.opcodes())
        action.step(client, sheet)
        self.assertEqual(commands(client), ["^cast heal Hero"])
        self.assertEqual(action.waiting, ["HEAL"])
        action.step(client, sheet)
        self.assertEqual(commands(client), ["^cast heal Hero"])
        inbox(action, "OP_HPUpdate", struct.pack("<HIi", 1, 90, 100))
        action.step(client, sheet)
        self.assertTrue(action.complete)
        self.assertNotIn("OP_CastSpell", opcodes(client))


if __name__ == "__main__":
    unittest.main()
