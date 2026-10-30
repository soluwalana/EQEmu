"""LootMob picks queued fetches, newest first, and stops at empty slots minus 2."""

import struct
import unittest

from harness import fresh, inbox, opcodes

from eqclient3.actions.fetch import Fetch
from eqclient3.actions.loot_mob import LootMob
from eqclient3.world import Mob


def slot_of(payload):
    return struct.unpack_from("<H", payload, 8)[0]


class LootMobTest(unittest.TestCase):
    def test_missing_corpse_completes_without_a_request(self):
        client, sheet = fresh()
        action = LootMob(9, (0.0, 0.0, 0.0))
        action.step(client, sheet)
        self.assertTrue(action.complete)
        self.assertNotIn("OP_LootRequest", opcodes(client))

    def test_walks_then_picks_fetches_in_recent_order(self):
        client, sheet = fresh()
        body = Mob(9, "a corpse", npc=3, position=(80.0, 0.0, 0.0))
        body.targeted = True
        sheet.mobs[9] = body
        sheet.empty_slots = 4
        older = Fetch(20, 1, "older")
        newer = Fetch(21, 1, "newer")
        client.queue.append(older, sheet, client.journal, "Hero")
        client.queue.append(newer, sheet, client.journal, "Hero")
        action = LootMob(9, (80.0, 0.0, 0.0))
        action.step(client, sheet)
        self.assertEqual(movement_mode(), "run")
        sheet.position = (80.0, 0.0, 0.0)
        action.step(client, sheet)
        self.assertEqual(opcodes(client)[-1], "OP_LootRequest")
        self.assertEqual(action.waiting, ["LOOT"])
        inbox(action, "OP_ItemPacket", {"slot": 1, "item_id": 20, "stack": 1})
        inbox(action, "OP_ItemPacket", {"slot": 2, "item_id": 21, "stack": 1})
        inbox(action, "OP_ItemPacket", {"slot": 3, "item_id": 99, "stack": 1})
        inbox(action, "OP_MoneyOnCorpse", bytes([3]))
        action.step(client, sheet)
        first = slot_of(client.outbound[-1][1])
        action.step(client, sheet)
        second = slot_of(client.outbound[-1][1])
        self.assertEqual((first, second), (2, 1))
        action.step(client, sheet)
        self.assertEqual(opcodes(client)[-1], "OP_EndLootRequest")
        self.assertTrue(action.complete)
        sent = [slot_of(payload) for opcode, payload in client.outbound if opcode == "OP_LootItem"]
        self.assertNotIn(3, sent)
        self.assertEqual(LootMob.key(action), (movement_distance(),))

    def test_stops_when_empty_slots_minus_two_are_used(self):
        client, sheet = fresh()
        body = Mob(9, "a corpse", npc=3, position=(0.0, 0.0, 0.0))
        body.targeted = True
        sheet.mobs[9] = body
        sheet.empty_slots = 3
        client.queue.append(Fetch(20, 1, "older"), sheet, client.journal, "Hero")
        client.queue.append(Fetch(21, 1, "newer"), sheet, client.journal, "Hero")
        action = LootMob(9, (0.0, 0.0, 0.0))
        action.requested = True
        action.opened = True
        action.slots = [
            type("S", (), {"slot": 1, "item_id": 20, "stack": 1, "name": ""})(),
            type("S", (), {"slot": 2, "item_id": 21, "stack": 1, "name": ""})(),
        ]
        action.step(client, sheet)
        action.step(client, sheet)
        sent = [slot_of(payload) for opcode, payload in client.outbound if opcode == "OP_LootItem"]
        self.assertEqual(sent, [2])
        self.assertEqual(opcodes(client)[-1], "OP_EndLootRequest")

    def test_full_pack_still_opens_and_takes_the_coin(self):
        client, sheet = fresh()
        body = Mob(9, "a corpse", npc=3, position=(0.0, 0.0, 0.0))
        body.targeted = True
        sheet.mobs[9] = body
        sheet.empty_slots = 0
        client.queue.append(Fetch(21, 1, "hide"), sheet, client.journal, "Hero")
        action = LootMob(9, (0.0, 0.0, 0.0))
        action.step(client, sheet)
        self.assertEqual(opcodes(client)[-1], "OP_LootRequest")
        inbox(
            action,
            "OP_ItemPacket",
            {"slot": 1, "item_id": 21, "stack": 1, "name": "Gnoll Fur"},
        )
        inbox(
            action,
            "OP_ItemPacket",
            {"slot": 4, "item_id": 500, "stack": 1, "name": "Platinum"},
        )
        inbox(action, "OP_MoneyOnCorpse", bytes([1]))
        action.step(client, sheet)
        sent = [slot_of(payload) for opcode, payload in client.outbound if opcode == "OP_LootItem"]
        self.assertEqual(sent, [4])
        action.step(client, sheet)
        self.assertEqual(opcodes(client)[-1], "OP_EndLootRequest")
        self.assertTrue(action.complete)


def movement_mode():
    from harness import movement

    return movement().advances[-1].mode


def movement_distance():
    from harness import movement

    return movement().distance


if __name__ == "__main__":
    unittest.main()
