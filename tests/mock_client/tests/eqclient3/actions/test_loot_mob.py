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
    def test_an_occupied_cursor_is_filed_before_loot(self):
        client, sheet = fresh()
        body = Mob(9, "a corpse", npc=3, position=(0.0, 0.0, 0.0))
        sheet.mobs[9] = body
        sheet.cursor = 9990
        action = LootMob(9, (0.0, 0.0, 0.0))
        action.step(client, sheet)
        self.assertTrue(action.yielding)
        self.assertNotIn("OP_LootRequest", opcodes(client))
        moves = [item for item in client.queue if type(item).__name__ == "Cursor"]
        self.assertEqual(moves[0].move, (30, 22))

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

    def test_a_hunt_item_on_the_corpse_is_looted(self):
        from eqclient3.actions.kill import Kill

        client, sheet = fresh()
        body = Mob(9, "a corpse", npc=3, position=(0.0, 0.0, 0.0))
        body.targeted = True
        sheet.mobs[9] = body
        sheet.empty_slots = 6
        hunt = Kill(camp="Gloom Spiders")
        hunt.until_item = 54234
        hunt.until_count = 1
        client.queue.append(hunt, sheet, client.journal, "Hero")
        action = LootMob(9, (0.0, 0.0, 0.0))
        action.requested = True
        action.opened = True
        action.slots = [type("S", (), {"slot": 3, "item_id": 54234, "stack": 1, "name": "Gloomingdeep Silk"})()]
        action.step(client, sheet)
        sent = [slot_of(payload) for opcode, payload in client.outbound if opcode == "OP_LootItem"]
        self.assertEqual(sent, [3])

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

    def test_an_upgrade_for_an_empty_slot_is_looted(self):
        client, sheet = fresh()
        from eqclient3.inventory import assign as assign_mod

        saved = assign_mod._ITEMS
        assign_mod._ITEMS = {40: {"slots": 8192, "classes": 65535, "races": 65535, "ac": 4, "item": 40}}
        try:
            body = Mob(9, "a corpse", npc=3, position=(0.0, 0.0, 0.0))
            body.targeted = True
            sheet.mobs[9] = body
            sheet.class_id = 1
            sheet.race = 1
            sheet.level = 1
            sheet.empty_slots = 6
            action = LootMob(9, (0.0, 0.0, 0.0))
            action.requested = True
            action.opened = True
            action.slots = [type("S", (), {"slot": 1, "item_id": 40, "stack": 1, "name": "a sword"})()]
            action.step(client, sheet)
        finally:
            assign_mod._ITEMS = saved
        sent = [slot_of(payload) for opcode, payload in client.outbound if opcode == "OP_LootItem"]
        self.assertEqual(sent, [1])

    def test_a_coin_run_loots_junk_and_marks_it_for_sale(self):
        client, sheet = fresh()
        body = Mob(9, "a corpse", npc=3, position=(0.0, 0.0, 0.0))
        body.targeted = True
        sheet.mobs[9] = body
        sheet.class_id = 1
        sheet.race = 1
        sheet.level = 1
        sheet.empty_slots = 6
        client.queue.append(Fetch(0, 1, "gold", copper=500), sheet, client.journal, sheet.name)
        action = LootMob(9, (0.0, 0.0, 0.0))
        action.requested = True
        action.opened = True
        action.slots = [
            type("S", (), {"slot": 1, "item_id": 99, "stack": 1, "name": "a rag"})(),
            type("S", (), {"slot": 2, "item_id": 40, "stack": 1, "name": "a sword"})(),
        ]
        from eqclient3.inventory import assign as assign_mod

        saved = assign_mod._ITEMS
        assign_mod._ITEMS = {
            40: {"slots": 8192, "classes": 65535, "races": 65535, "ac": 4, "nodrop": 1, "item": 40},
            99: {"slots": 0, "nodrop": 1, "item": 99},
        }
        try:
            action.step(client, sheet)
            action.step(client, sheet)
        finally:
            assign_mod._ITEMS = saved
        sent = [slot_of(payload) for opcode, payload in client.outbound if opcode == "OP_LootItem"]
        self.assertEqual(sorted(sent), [1, 2])
        self.assertIn(99, client.journal.sell_marks(sheet.name))
        self.assertNotIn(40, client.journal.sell_marks(sheet.name))


def movement_mode():
    from harness import movement

    return movement().advances[-1].mode


def movement_distance():
    from harness import movement

    return movement().distance


if __name__ == "__main__":
    unittest.main()
