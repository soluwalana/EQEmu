"""Reclaim drags inside 45 yards, loots, and buries. Hostiles come from movement."""

import struct
import unittest
from types import SimpleNamespace

from harness import fresh, inbox, kinds, movement, opcodes

from eqclient3.actions.reclaim import Reclaim
from eqclient3.world import Mob


def hostile(spawn_id, yards, standing=9):
    body = Mob(spawn_id, "wolf", level=12, position=(float(yards), 0.0, 0.0))
    body.distance = float(yards)
    body.consider = SimpleNamespace(standing=standing)
    return body


class ReclaimTest(unittest.TestCase):
    def test_farther_than_250_runs_and_sends_no_consider(self):
        client, sheet = fresh()
        movement().distance = 300
        action = Reclaim(7, (300.0, 0.0, 0.0))
        action.step(client, sheet)
        self.assertEqual(movement().advances[-1].mode, "run")
        self.assertIn(("visible", None), movement().plans)
        self.assertIn(("on_path", None), movement().plans)
        self.assertNotIn("OP_Consider", opcodes(client))
        self.assertNotIn("OP_Assist", [row for row in ()])
        self.assertIn("OP_Consider", action.opcodes())

    def test_inside_250_walks(self):
        client, sheet = fresh()
        movement().distance = 200
        movement().visible = [hostile(9, 200)]
        action = Reclaim(7, (200.0, 0.0, 0.0))
        action.step(client, sheet)
        self.assertEqual(movement().advances[-1].mode, "walk")
        self.assertNotIn("OP_Consider", opcodes(client))

    def test_hostile_within_150_summons_then_cautious_attack(self):
        client, sheet = fresh()
        sheet.level = 10
        movement().distance = 120
        movement().visible = [hostile(9, 100)]
        action = Reclaim(7, (120.0, 0.0, 0.0))
        action.step(client, sheet)
        self.assertIn("Summon", kinds(client))
        self.assertNotIn("Rez", kinds(client))
        self.assertFalse(action.complete)
        self.assertEqual(movement().advances, [])
        action.yielding = False
        action.step(client, sheet)
        self.assertEqual(movement().advances[-1].mode, "walk")
        attacks = [row for row in client.queue if type(row).__name__ == "Attack"]
        self.assertEqual(len(attacks), 1)
        self.assertTrue(attacks[0].cautious)

    def test_within_45_drags_loots_and_buries(self):
        client, sheet = fresh()
        sheet.level = 10
        movement().distance = 20
        action = Reclaim(7, (10.0, 0.0, 0.0))
        action.step(client, sheet)
        self.assertEqual(opcodes(client), ["OP_CorpseDrag"])
        self.assertEqual(len(client.outbound[0][1]), 152)
        self.assertIn(b"Hero", client.outbound[0][1])
        action.step(client, sheet)
        self.assertEqual(opcodes(client)[-1], "OP_LootRequest")
        self.assertEqual(action.waiting, ["LOOT"])
        inbox(action, "OP_ItemPacket", {"slot": 1, "item_id": 1001, "stack": 1})
        inbox(action, "OP_MoneyOnCorpse", bytes([1]))
        action.step(client, sheet)
        self.assertEqual(opcodes(client)[-1], "OP_LootItem")
        action.step(client, sheet)
        self.assertEqual(opcodes(client)[-1], "OP_EndLootRequest")
        self.assertTrue(action.complete)
        self.assertNotIn("OP_Consider", opcodes(client))

    def test_above_level_10_appends_rez(self):
        client, sheet = fresh()
        sheet.level = 11
        movement().distance = 20
        action = Reclaim(7, (10.0, 0.0, 0.0))
        action.step(client, sheet)
        self.assertIn("Rez", kinds(client))
        self.assertIn("OP_CorpseDrag", opcodes(client))
        self.assertFalse(action.complete)

    def test_too_far_clears_requested(self):
        client, sheet = fresh()
        movement().distance = 120
        action = Reclaim(7, (120.0, 0.0, 0.0))
        action.dragged = True
        action.requested = True
        action.waiting = ["LOOT"]
        inbox(action, "OP_MoneyOnCorpse", bytes([5]))
        action.step(client, sheet)
        self.assertFalse(action.requested)
        self.assertEqual(action.waiting, [])
        self.assertNotIn("OP_LootRequest", opcodes(client))

    def test_distance_key_reads_plan_and_sends_nothing(self):
        _client, sheet = fresh()
        movement().distance = 12
        action = Reclaim(7, (12.0, 0.0, 0.0))
        action._world = sheet
        self.assertEqual(action.distance, 12)
        self.assertEqual(Reclaim.key(action), (12,))
        self.assertEqual(movement().plans[-1][0], (12.0, 0.0, 0.0))


if __name__ == "__main__":
    unittest.main()
