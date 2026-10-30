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
