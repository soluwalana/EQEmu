"""Reclaim: run, walk inside 250, drag inside 45, request, every slot, bury."""

import unittest

from harness import fresh, inbox, movement, opcodes

from eqclient3.actions.reclaim import Reclaim
from eqclient3.world import Mob


def wolf(yards):
    body = Mob(9, "wolf", level=4, position=(float(yards), 0.0, 0.0))
    body.distance = float(yards)
    body.consider = type("C", (), {"standing": 9})()
    return body


class ReclaimSteps(unittest.TestCase):
    def test_run_walk_drag_loot_bury(self):
        client, sheet = fresh()
        sheet.level = 10
        fake = movement()
        fake.distance = 300
        action = Reclaim(7, (300.0, 0.0, 0.0))
        action.step(client, sheet)
        self.assertEqual(fake.advances[-1].mode, "run")
        fake.distance = 200
        fake.visible = [wolf(200)]
        action.active_path = None
        action.step(client, sheet)
        self.assertEqual(fake.advances[-1].mode, "walk")
        fake.distance = 20
        fake.visible = []
        action.step(client, sheet)
        self.assertIn("OP_CorpseDrag", opcodes(client))
        action.step(client, sheet)
        self.assertEqual(opcodes(client)[-1], "OP_LootRequest")
        inbox(action, "OP_ItemPacket", {"slot": 1, "item_id": 1001, "stack": 1})
        inbox(action, "OP_ItemPacket", {"slot": 2, "item_id": 1002, "stack": 1})
        inbox(action, "OP_MoneyOnCorpse", bytes([1]))
        action.step(client, sheet)
        action.step(client, sheet)
        action.step(client, sheet)
        self.assertEqual(opcodes(client)[-1], "OP_EndLootRequest")
        self.assertTrue(action.complete)
        self.assertNotIn("OP_Consider", opcodes(client))
        looted = [opcode for opcode in opcodes(client) if opcode == "OP_LootItem"]
        self.assertEqual(len(looted), 2)


if __name__ == "__main__":
    unittest.main()
