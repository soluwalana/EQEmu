"""ScribeSpell: move the scroll, write, and complete on the learned line."""

import unittest

from harness import fresh, inbox, opcodes

from eqclient3.actions.scribe import ScribeSpell


class ScribeSteps(unittest.TestCase):
    def test_move_write_learned(self):
        client, sheet = fresh()
        sheet.bags[22] = 100
        sheet.spell_names = {11: "Minor Healing"}
        action = ScribeSpell(11, 22)
        action.step(client, sheet)
        self.assertEqual(opcodes(client), ["OP_MoveItem"])
        sheet.cursor = 100
        action.step(client, sheet)
        self.assertGreaterEqual(opcodes(client).count("OP_MemorizeSpell"), 1)
        self.assertEqual(action.waiting, ["SCRIBE"])
        action.step(client, sheet)
        self.assertFalse(action.complete)
        inbox(action, "OP_SpecialMesg", {"text": "You have learned Minor Healing!"})
        action.step(client, sheet)
        self.assertTrue(action.complete)


if __name__ == "__main__":
    unittest.main()
