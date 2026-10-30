"""Seat sends its command list, then completes. Rez stays ahead of it in the band."""

import unittest

from harness import commands, fresh

from eqclient3.actions.rez import Rez
from eqclient3.actions.seat import Seat


class SeatTest(unittest.TestCase):
    def test_commands_then_complete(self):
        client, sheet = fresh()
        action = Seat("Cleric", ["^botcamp Cleric", "^disband Cleric"])
        self.assertEqual(Seat.key(action), (1,))
        self.assertLess(Rez.key(Rez(1, b"")), Seat.key(action))
        action.step(client, sheet)
        action.step(client, sheet)
        action.step(client, sheet)
        self.assertEqual(commands(client), ["^botcamp Cleric", "^disband Cleric"])
        self.assertTrue(action.complete)


if __name__ == "__main__":
    unittest.main()
