"""Summon: ten empty steps resend ^botsummon spawned. The summoned line completes it."""

import unittest

from harness import commands, fresh, inbox

from eqclient3.actions.bots.summon import Summon


class SummonSteps(unittest.TestCase):
    def test_ten_empty_steps_then_the_summoned_line(self):
        client, sheet = fresh()
        action = Summon(271)
        action.step(client, sheet)
        self.assertEqual(commands(client), ["^botsummon spawned"])
        for _ in range(9):
            action.step(client, sheet)
            self.assertEqual(len(commands(client)), 1)
            self.assertEqual(action.waiting, ["SUMMON"])
        action.step(client, sheet)
        self.assertEqual(commands(client), ["^botsummon spawned", "^botsummon spawned"])
        inbox(action, "OP_ChannelMessage", {"text": "You have summoned your bots to you."})
        action.step(client, sheet)
        self.assertTrue(action.complete)


if __name__ == "__main__":
    unittest.main()
