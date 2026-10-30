"""LootMob: walk, request, fetches newest first, stop at empty minus 2, end."""

import struct
import unittest

from harness import fresh, inbox, opcodes

from eqclient3.actions.fetch import Fetch
from eqclient3.actions.loot_mob import LootMob
from eqclient3.world import Mob


def slot_of(payload):
    return struct.unpack_from("<H", payload, 8)[0]


class LootMobSteps(unittest.TestCase):
    def test_walk_request_recent_fetches_then_end(self):
        client, sheet = fresh()
        body = Mob(9, "a corpse", npc=3, position=(40.0, 0.0, 0.0))
        body.targeted = True
        sheet.mobs[9] = body
        sheet.empty_slots = 4
        client.queue.append(Fetch(20, 1, "older"), sheet, client.journal, "Hero")
        client.queue.append(Fetch(21, 1, "newer"), sheet, client.journal, "Hero")
        action = LootMob(9, (40.0, 0.0, 0.0))
        action.step(client, sheet)
        sheet.position = (40.0, 0.0, 0.0)
        action.step(client, sheet)
        self.assertEqual(opcodes(client)[-1], "OP_LootRequest")
        inbox(action, "OP_ItemPacket", {"slot": 1, "item_id": 20, "stack": 1})
        inbox(action, "OP_ItemPacket", {"slot": 2, "item_id": 21, "stack": 1})
        inbox(action, "OP_ItemPacket", {"slot": 3, "item_id": 99, "stack": 1})
        inbox(action, "OP_MoneyOnCorpse", bytes([1]))
        action.step(client, sheet)
        action.step(client, sheet)
        sent = [slot_of(payload) for opcode, payload in client.outbound if opcode == "OP_LootItem"]
        self.assertEqual(sent, [2, 1])
        action.step(client, sheet)
        self.assertEqual(opcodes(client)[-1], "OP_EndLootRequest")
        self.assertTrue(action.complete)
        self.assertNotIn(3, sent)


if __name__ == "__main__":
    unittest.main()
