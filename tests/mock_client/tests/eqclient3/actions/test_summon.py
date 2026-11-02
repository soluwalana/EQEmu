"""Summon waits ten empty steps, then sends ^botsummon spawned again."""

import unittest

from harness import commands, fresh, inbox, kinds

from eqclient3.actions.bots.summon import Summon


class SummonTest(unittest.TestCase):
    def test_ten_empty_steps_resend(self):
        client, sheet = fresh()
        action = Summon(271)
        self.assertEqual(action.priority, 271)
        self.assertNotIn("OP_Assist", action.opcodes())
        action.step(client, sheet)
        self.assertEqual(commands(client), ["^botsummon spawned"])
        self.assertEqual(action.waiting, ["SUMMON"])
        for _ in range(9):
            action.step(client, sheet)
        self.assertEqual(commands(client), ["^botsummon spawned"])
        action.step(client, sheet)
        self.assertEqual(commands(client), ["^botsummon spawned", "^botsummon spawned"])

    def test_summoned_line_completes(self):
        client, sheet = fresh()
        action = Summon(271)
        action.step(client, sheet)
        inbox(action, "OP_SpecialMesg", {"text": "Summoned 5 bots to you."})
        action.step(client, sheet)
        self.assertTrue(action.complete)
        self.assertEqual(action.waiting, [])

    def test_no_spawned_bots_forms_the_party(self):
        client, sheet = fresh("tutorialb")
        sheet.form_return = True
        action = Summon(271)
        action.step(client, sheet)
        inbox(
            action,
            "OP_SpecialMesg",
            {"text": "You have no spawned bots meeting this criteria - type: 'spawned', name: ''"},
        )
        action.step(client, sheet)
        self.assertTrue(action.complete)
        self.assertEqual(commands(client), ["^botsummon spawned"])
        self.assertIn("Form", kinds(client))


if __name__ == "__main__":
    unittest.main()
