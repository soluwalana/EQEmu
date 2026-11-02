"""Attack heals once, then melee inside 15 yards."""

import struct
import unittest

from harness import commands, fresh, inbox, kinds, mob, movement, opcodes

from eqclient3.actions.attack import Attack
from eqclient3.structs import OP_CastSpell, OP_MemorizeSpell


class AttackTest(unittest.TestCase):
    def test_out_of_range_plans_los_or_walk(self):
        client, sheet = fresh()
        body = mob(sheet, 8, distance=40, targeted=True)
        action = Attack(8)
        self.assertIn("OP_Consider", action.opcodes())
        action.step(client, sheet)
        self.assertEqual(movement().advances[-1].mode, "los")
        self.assertNotIn("OP_Consider", opcodes(client))
        self.assertNotIn("OP_TargetMouse", opcodes(client))
        action.suspend()
        movement().reset()
        action.cautious = True
        body.position = (40.0, 0.0, 0.0)
        action.step(client, sheet)
        self.assertEqual(movement().advances[-1].mode, "walk")

    def test_inside_15_sends_attack_once_and_again_after_suspend(self):
        client, sheet = fresh()
        body = mob(sheet, 8, distance=10, targeted=False)
        action = Attack(8)
        action.step(client, sheet)
        self.assertEqual(action.waiting, ["TARGET"])
        self.assertEqual(opcodes(client), ["OP_TargetMouse"])
        self.assertEqual(commands(client), [])
        action.step(client, sheet)
        self.assertEqual(opcodes(client), ["OP_TargetMouse", "OP_Consider"])
        inbox(
            action,
            "OP_Consider",
            struct.pack("<IIIIIIBBBB", 0, body.id, 0, 0, 0, 0, 0, 0, 0, 0),
        )
        action.step(client, sheet)
        self.assertEqual(commands(client), ["^attack"])
        self.assertIn("OP_AutoAttack", opcodes(client))
        self.assertEqual(opcodes(client).count("OP_TargetMouse"), 1)
        sent = len(commands(client))
        action.step(client, sheet)
        self.assertEqual(len(commands(client)), sent)
        action.suspend()
        action.step(client, sheet)
        self.assertEqual(commands(client), ["^attack", "^attack"])

    def test_casting_empty_inbox_returns(self):
        client, sheet = fresh()
        mob(sheet, 8, distance=10, targeted=True)
        action = Attack(8)
        action.casting = True
        action.waiting = ["CAST"]
        action.step(client, sheet)
        self.assertEqual(client.outbound, [])
        self.assertEqual(action.waiting, ["CAST"])

    def test_combat_spell_sets_cast(self):
        client, sheet = fresh()
        mob(sheet, 8, distance=10, targeted=True)
        sheet.gems[2] = 50
        sheet.spell_info = {
            50: type(
                "S",
                (),
                {"mana": 10, "recast": 6, "combat": True, "heal": False, "cure": None},
            )()
        }
        sheet.mana = 100
        action = Attack(8)
        action.step(client, sheet)
        self.assertEqual(action.waiting, ["CAST"])
        self.assertIn("OP_CastSpell", opcodes(client))
        self.assertNotIn("OP_AutoAttack", opcodes(client))

    def test_heal_once_then_bar_clears_the_flag(self):
        client, sheet = fresh()
        mob(sheet, 8, distance=10, targeted=True)
        sheet.hp = 10
        sheet.max_hp = 100
        sheet.mana = 100
        sheet.gems[1] = 40
        sheet.spell_info = {
            40: type(
                "S",
                (),
                {"mana": 10, "recast": 6, "heal": True, "combat": False, "cure": None},
            )()
        }
        action = Attack(8)
        action.step(client, sheet)
        self.assertEqual(opcodes(client).count("OP_CastSpell"), 1)
        self.assertTrue(action.heal_requested)
        client.outbound.clear()
        action.step(client, sheet)
        self.assertNotIn("OP_CastSpell", opcodes(client))
        inbox(action, "OP_HPUpdate", struct.pack("<HIi", 1, 80, 100))
        action.step(client, sheet)
        self.assertFalse(action.heal_requested)

    def test_cure_once_then_buff_clears_the_flag(self):
        client, sheet = fresh()
        mob(sheet, 8, distance=10, targeted=True)
        sheet.afflictions = [(1, "poison")]
        sheet.mana = 100
        sheet.gems[3] = 41
        sheet.spell_info = {
            41: type(
                "S",
                (),
                {
                    "mana": 10,
                    "recast": 6,
                    "heal": False,
                    "combat": False,
                    "cure": "poison",
                },
            )()
        }
        action = Attack(8)
        action.step(client, sheet)
        self.assertTrue(action.cure_requested)
        self.assertEqual(opcodes(client).count("OP_CastSpell"), 1)
        inbox(action, "OP_Buff", {"fade": 1})
        action.step(client, sheet)
        self.assertFalse(action.cure_requested)

    def test_abilities_taunt_kick_and_bash(self):
        client, sheet = fresh()
        mob(sheet, 8, distance=10, targeted=True)
        sheet.skills[73] = 1
        action = Attack(8)
        action.step(client, sheet)
        self.assertIn("OP_Taunt", opcodes(client))
        client.outbound.clear()
        sheet.skills.pop(73)
        sheet.skills[30] = 1
        action.ability_ready["taunt"] = 999
        action.opened = True
        action.step(client, sheet)
        _spawn, _zero, skill = struct.unpack("<III", client.outbound[-1][1])
        self.assertEqual(client.outbound[-1][0], "OP_CombatAbility")
        self.assertEqual(skill, 30)
        client.outbound.clear()
        action.ability_ready["kick"] = 999
        sheet.skills[10] = 1
        sheet.shield = True
        action.step(client, sheet)
        _spawn, _zero, skill = struct.unpack("<III", client.outbound[-1][1])
        self.assertEqual(skill, 10)

    def test_taunt_skipped_while_reclaim_is_queued(self):
        client, sheet = fresh()
        mob(sheet, 8, distance=10, targeted=True)
        sheet.skills[73] = 1
        from eqclient3.actions.reclaim import Reclaim

        client.queue.append(Reclaim(3, (0, 0, 0)), sheet, client.journal, "Hero")
        action = Attack(8)
        action.step(client, sheet)
        self.assertNotIn("OP_Taunt", opcodes(client))

    def test_string_251_on_our_corpse_appends_reclaim(self):
        client, sheet = fresh()
        mob(sheet, 8, distance=10, targeted=True)
        body = mob(sheet, 4, name="Hero's corpse", distance=1)
        body.dead = True
        action = Attack(8)
        action.cast_target = 4
        inbox(action, "OP_SimpleMessage", {"string_id": 1})
        inbox(action, "OP_SimpleMessage", {"string_id": 251})
        inbox(action, "OP_SimpleMessage", {"string_id": 251})
        action.step(client, sheet)
        self.assertEqual([message.payload.string_id for message in action.messages], [1])
        self.assertIn("Reclaim", kinds(client))
        self.assertFalse(action.complete)
        self.assertTrue(action.yielding)

    def test_become_corpse_appends_reconstitute(self):
        client, sheet = fresh()
        mob(sheet, 8, distance=10, targeted=True)
        action = Attack(8)
        inbox(action, "OP_BecomeCorpse", struct.pack("<I", 8))
        action.step(client, sheet)
        self.assertTrue(action.complete)
        found = [row for row in client.queue if type(row).__name__ == "Reconstitute"]
        self.assertEqual(len(found), 1)
        self.assertEqual(found[0].priority, 241)

    def test_a_wizard_sits_instead_of_nuking_on_a_low_pool(self):
        client, sheet = fresh()
        mob(sheet, 8, distance=10, targeted=True)
        sheet.class_id = 12
        sheet.mana = 10
        sheet.max_mana = 100
        sheet.gems[0] = 50
        sheet.spell_info = {50: _spell(mana=20, combat=True)}
        action = Attack(8)
        action.step(client, sheet)
        self.assertTrue(action.resting)
        self.assertIn("OP_SpawnAppearance", opcodes(client))
        self.assertNotIn("OP_CastSpell", opcodes(client))

    def test_slow_lands_before_the_nuke(self):
        client, sheet = fresh()
        mob(sheet, 8, distance=10, targeted=True)
        sheet.mana = 100
        sheet.gems[0] = 1
        sheet.gems[1] = 2
        sheet.spell_names = {1: "Ensnaring Slow", 2: "Shock of Fire"}
        sheet.spell_info = {1: _spell(), 2: _spell(combat=True)}
        action = Attack(8)
        action.step(client, sheet)
        cast = _cast(client)
        self.assertEqual(cast.spell_id, 1)
        self.assertIn("slow", action.landed)
        action.unwait("CAST")
        action.casting = False
        client.outbound.clear()
        action.step(client, sheet)
        self.assertEqual(_cast(client).spell_id, 2)

    def test_a_nuke_waits_out_its_recast(self):
        client, sheet = fresh()
        mob(sheet, 8, distance=10, targeted=True)
        sheet.mana = 100
        sheet.gems[2] = 50
        sheet.spell_info = {50: _spell(mana=10, recast=6, combat=True)}
        action = Attack(8)
        action.step(client, sheet)
        self.assertEqual(action.waiting, ["CAST"])
        action.unwait("CAST")
        action.casting = False
        client.outbound.clear()
        action.step(client, sheet)
        self.assertNotIn("OP_CastSpell", opcodes(client))
        self.assertIn("OP_AutoAttack", opcodes(client))

    def test_a_weaker_heal_is_cleared_for_the_higher_one(self):
        import eqclient3.actions.casting as casting

        client, sheet = fresh()
        mob(sheet, 8, distance=10, targeted=True)
        sheet.class_id = 2
        sheet.spell_book = {0: 201, 1: 202}
        sheet.spell_names = {201: "Minor Healing", 202: "Greater Healing"}
        sheet.spell_info = {201: _spell(mana=10, heal=True), 202: _spell(mana=40, heal=True)}
        sheet.gems[0] = 201
        previous = casting._LEVELS
        casting._LEVELS = {}
        try:
            action = Attack(8)
            action.step(client, sheet)
            cleared = OP_MemorizeSpell.deserialize(client.outbound[-1][1])
            self.assertEqual((cleared.slot, cleared.spell_id, cleared.scribing), (0, 201, 2))
            client.outbound.clear()
            action.step(client, sheet)
            loaded = OP_MemorizeSpell.deserialize(client.outbound[-1][1])
            self.assertEqual((loaded.slot, loaded.spell_id, loaded.scribing), (0, 202, 1))
            self.assertEqual(sheet.gems[0], 202)
        finally:
            casting._LEVELS = previous


def _spell(**fields: object):
    values = {"mana": 10, "recast": 0, "heal": False, "combat": False, "cure": None}
    values.update(fields)
    return type("S", (), values)()


def _cast(client) -> OP_CastSpell:
    payload = next(body for opcode, body in reversed(client.outbound) if opcode == "OP_CastSpell")
    return OP_CastSpell.deserialize(payload)


if __name__ == "__main__":
    unittest.main()
