"""ScribeSpell moves the scroll, writes it, and completes on the learned line."""

import unittest

from harness import fresh, inbox, opcodes

from eqclient3.actions.scribe import ScribeSpell


class ScribeSpellTest(unittest.TestCase):
    def test_move_write_and_learned_line(self):
        client, sheet = fresh()
        sheet.bags[22] = 100
        sheet.items[100] = _scroll(11, 100)
        sheet.spell_names = {11: "Minor Healing"}
        sheet.gem_slot = 0
        action = ScribeSpell(11, 22)
        action.step(client, sheet)
        self.assertEqual(opcodes(client), ["OP_MoveItem"])
        sheet.cursor = 100
        sheet.bags.pop(22, None)
        action.step(client, sheet)
        self.assertEqual(opcodes(client).count("OP_MemorizeSpell"), 2)
        self.assertEqual(action.waiting, ["SCRIBE"])
        action.step(client, sheet)
        self.assertFalse(action.complete)
        inbox(action, "OP_SpecialMesg", {"text": "You have learned Minor Healing!"})
        action.step(client, sheet)
        self.assertTrue(action.complete)

    def test_a_scroll_already_on_the_cursor_is_scribed_in_place(self):
        client, sheet = fresh()
        sheet.cursor = 59964
        sheet.items[59964] = _scroll(374, 59964)
        sheet.class_id = 12
        action = ScribeSpell(374, 0)
        action.step(client, sheet)
        self.assertEqual(opcodes(client), ["OP_MemorizeSpell", "OP_MemorizeSpell"])
        from eqclient3.structs import OP_MemorizeSpell

        wrote = OP_MemorizeSpell.deserialize(client.outbound[0][1])
        self.assertEqual((wrote.slot, wrote.spell_id, wrote.scribing), (0, 374, 0))


def _scroll(effect: int, item_id: int = 59964):
    from eqclient3.handlers.items import Held

    return Held(item_id, "Spell: Numbing Cold", 20, 1, effect)


if __name__ == "__main__":
    unittest.main()
