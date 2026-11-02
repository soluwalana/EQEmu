"""Kill walks to the spawn and completes on that spawn's corpse."""

import struct
import unittest

from harness import fresh, inbox, kinds, mob, movement

from eqclient3.actions.kill import Kill


class KillTest(unittest.TestCase):
    def test_in_range_appends_attack(self):
        client, sheet = fresh()
        client.journal.set_soulbind("Hero", "qeynos")
        mob(sheet, 8, distance=5, targeted=True)
        action = Kill(spawn_id=8)
        self.assertNotIn("OP_Assist", action.opcodes())
        action.step(client, sheet)
        self.assertIn("Attack", kinds(client))
        self.assertTrue(action.yielding)
        self.assertFalse(action.complete)

    def test_out_of_range_walks(self):
        client, sheet = fresh()
        client.journal.set_soulbind("Hero", "qeynos")
        mob(sheet, 8, distance=40, targeted=True)
        action = Kill(spawn_id=8)
        action.step(client, sheet)
        self.assertEqual(movement().advances[-1].mode, "run")
        self.assertNotIn("Attack", kinds(client))

    def test_corpse_completes(self):
        client, sheet = fresh()
        client.journal.set_soulbind("Hero", "qeynos")
        mob(sheet, 8, distance=5, targeted=True)
        action = Kill(spawn_id=8)
        inbox(action, "OP_BecomeCorpse", struct.pack("<I", 8))
        action.step(client, sheet)
        self.assertTrue(action.complete)
        self.assertNotIn("Attack", kinds(client))

    def test_plural_task_name_matches_one_spawn(self):
        client, sheet = fresh()
        client.journal.set_soulbind("Hero", "qeynos")
        mob(sheet, 8, distance=40, name="a_gloomfang_lurker")
        action = Kill(camp="Gloomfang Lurkers")
        action.step(client, sheet)
        self.assertEqual(action.spawn_id, 8)

    def test_named_camp_walks_to_the_living_mob(self):
        client, sheet = fresh()
        client.journal.set_soulbind("Hero", "qeynos")
        mob(sheet, 8, distance=40, name="a_spider")
        action = Kill(camp="spider")
        action.step(client, sheet)
        self.assertEqual(action.spawn_id, 8)
        self.assertEqual(movement().advances[-1].mode, "run")
        self.assertNotIn("Attack", kinds(client))

    def test_a_find_item_cycles_to_the_next_listed_mob(self):
        client, sheet = fresh()
        client.journal.set_soulbind("Hero", "qeynos")
        mob(sheet, 8, distance=10, name="a_gloom_spider")
        mob(sheet, 9, distance=30, name="a_gloom_spiderling")
        action = Kill(camp="Gloom Spiders")
        action.until_item = 54234
        action.mobs = ("a gloom spider", "a gloom spiderling")
        action.prey_loaded = True
        action.skipped.add(8)
        action.step(client, sheet)
        self.assertEqual(action.spawn_id, 9)

    def test_a_find_item_walks_the_next_spawn_when_none_are_up(self):
        client, sheet = fresh()
        client.journal.set_soulbind("Hero", "qeynos")
        action = Kill(camp="Gloom Spiders")
        action.until_item = 54234
        action.mobs = ("a gloom spider",)
        action.posts = ((40.0, 0.0, 0.0), (80.0, 0.0, 0.0))
        action.prey_loaded = True
        action.step(client, sheet)
        self.assertEqual(action.where, (40.0, 0.0, 0.0))
        self.assertEqual(movement().advances[-1].mode, "run")
        sheet.x = 40.0
        action.where = (40.0, 0.0, 0.0)
        action.step(client, sheet)
        self.assertEqual(action.where, (80.0, 0.0, 0.0))

    def test_camp_level_met_completes(self):
        client, sheet = fresh()
        client.journal.set_soulbind("Hero", "qeynos")
        sheet.level = 20
        action = Kill(camp=(1.0, 2.0, 3.0), level=20)
        action.step(client, sheet)
        self.assertTrue(action.complete)
        self.assertEqual(movement().advances, [])


if __name__ == "__main__":
    unittest.main()
