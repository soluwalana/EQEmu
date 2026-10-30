"""Attack: out of range, inside 15, one ability, then the corpse. Heal once."""

import struct
import unittest

from harness import commands, fresh, inbox, mob, movement, opcodes

from eqclient3.actions.attack import Attack


class AttackSteps(unittest.TestCase):
    def test_range_ability_then_corpse(self):
        client, sheet = fresh()
        body = mob(sheet, 8, distance=40, level=6, targeted=True)
        sheet.skills[30] = 1
        action = Attack(8)
        action.step(client, sheet)
        self.assertEqual(movement().advances[-1].mode, "los")
        body.position = (10.0, 0.0, 0.0)
        action.step(client, sheet)
        self.assertEqual(commands(client), ["^attack", "^pet_attack"])
        self.assertIn("OP_AutoAttack", opcodes(client))
        self.assertIn("OP_CombatAbility", opcodes(client))
        client.outbound.clear()
        action.step(client, sheet)
        self.assertEqual(commands(client), [])
        inbox(action, "OP_BecomeCorpse", struct.pack("<I", 8))
        action.step(client, sheet)
        self.assertTrue(action.complete)
        found = [row for row in client.queue if type(row).__name__ == "Reconstitute"]
        self.assertEqual(found[0].priority, 241)

    def test_heal_once_until_the_bar_returns(self):
        client, sheet = fresh()
        mob(sheet, 8, distance=10, targeted=True)
        sheet.hp = 10
        sheet.max_hp = 100
        sheet.mana = 80
        sheet.gems[1] = 40
        sheet.spell_info = {40: type("S", (), {"mana": 10, "recast": 6, "heal": True, "combat": False, "cure": None})()}
        action = Attack(8)
        action.step(client, sheet)
        self.assertEqual(opcodes(client).count("OP_CastSpell"), 1)
        self.assertTrue(action.heal_requested)
        client.outbound.clear()
        action.step(client, sheet)
        self.assertNotIn("OP_CastSpell", opcodes(client))
        self.assertTrue(action.heal_requested)
        inbox(action, "OP_HPUpdate", struct.pack("<IiH", 80, 100, 1))
        action.step(client, sheet)
        self.assertFalse(action.heal_requested)


if __name__ == "__main__":
    unittest.main()
