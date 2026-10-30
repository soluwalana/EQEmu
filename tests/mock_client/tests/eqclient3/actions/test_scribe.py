"""ScribeSpell moves the scroll, writes it, and completes on the learned line."""

import unittest

from harness import fresh, inbox, opcodes

from eqclient3.actions.scribe import ScribeSpell


class ScribeSpellTest(unittest.TestCase):
    def test_move_write_and_learned_line(self):
        client, sheet = fresh()
        sheet.bags[22] = 100
        sheet.spell_names = {11: "Minor Healing"}
        sheet.gem_slot = 0
        action = ScribeSpell(11, 22)
        action.step(client, sheet)
        self.assertEqual(opcodes(client), ["OP_MoveItem"])
        sheet.cursor = 100
        action.step(client, sheet)
        self.assertEqual(opcodes(client).count("OP_MemorizeSpell"), 2)
        self.assertEqual(action.waiting, ["SCRIBE"])
        action.step(client, sheet)
        self.assertFalse(action.complete)
        inbox(action, "OP_SpecialMesg", {"text": "You have learned Minor Healing!"})
        action.step(client, sheet)
        self.assertTrue(action.complete)


if __name__ == "__main__":
    unittest.main()
