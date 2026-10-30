"""Cure sends one line. OP_Buff clears it."""

import unittest

from harness import commands, fresh, inbox

from eqclient3.actions.cure import Cure


class CureTest(unittest.TestCase):
    def test_one_line_then_buff(self):
        client, sheet = fresh()
        action = Cure("Cleric", "poison")
        self.assertEqual(action.priority, 250)
        action.step(client, sheet)
        self.assertEqual(commands(client), ["^cast cures byname Cleric"])
        self.assertEqual(action.waiting, ["CURE"])
        action.step(client, sheet)
        self.assertEqual(len(commands(client)), 1)
        inbox(action, "OP_Buff", {"fade": 1, "effect": "poison"})
        action.step(client, sheet)
        self.assertTrue(action.complete)


if __name__ == "__main__":
    unittest.main()
