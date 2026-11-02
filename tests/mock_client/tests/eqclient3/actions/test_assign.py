"""Sell skips a recent fetch and a piece the current quest graph requires."""

import struct
import unittest

from harness import fresh, inbox

from eqclient3.actions.distribute import Distribute
from eqclient3.actions.fetch import Fetch
from eqclient3.actions.sell import Sell
from eqclient3.inventory import assign as assign_mod
from eqclient3.inventory.assign import assign
from eqclient3.quests.graph import QuestGraph
from eqclient3.world import Bot


class AssignTest(unittest.TestCase):
    def test_recent_fetch_and_graph_need_stay_out_of_the_vendor_list(self):
        client, sheet = fresh()
        sheet.bags = {23: 21, 24: 50, 25: 99}
        client.queue.append(Fetch(21, 1, "hide"), sheet, client.journal, "Hero")
        client.journal.save_goals("Hero", [(80, 1)])
        graph = QuestGraph()
        graph.edges = [{"rel": "needs", "to": "item:80", "from": "item:50", "group": "quest"}]
        graph.index()
        assign(client, sheet, client.journal, graph=graph)
        sold = [action.item_ids for action in client.queue if isinstance(action, Sell)]
        self.assertEqual(sold, [])

    def test_a_cursor_upgrade_sends_move_item(self):
        client, sheet = fresh()
        saved = assign_mod._ITEMS
        assign_mod._ITEMS = {
            67104: {
                "slots": 128,
                "classes": 65535,
                "races": 65535,
                "ac": 8,
                "item": 67104,
            }
        }
        try:
            sheet.cursor = 67104
            sheet.class_id = 1
            sheet.race = 1
            sheet.level = 1
            assign(client, sheet, client.journal)
        finally:
            assign_mod._ITEMS = saved
        queued = [action for action in client.queue if type(action).__name__ == "Cursor"]
        self.assertEqual(len(queued), 1)
        self.assertEqual(queued[0].move, (30, 7))
        self.assertEqual(queued[0].source, "cursor:30:7")
        queued[0].step(client, sheet)
        self.assertEqual(client.outbound[0][0], "OP_MoveItem")
        src, dest = (
            struct.unpack_from("<hh", client.outbound[0][1], 4)[0],
            struct.unpack_from("<h", client.outbound[0][1], 16)[0],
        )
        self.assertEqual((src, dest), (33, 7))

    def test_a_player_upgrade_stays_put_while_a_trade_holds_the_cursor(self):
        from eqclient3.actions.trade import Trade

        client, sheet = fresh()
        saved = assign_mod._ITEMS
        assign_mod._ITEMS = {54226: {"slots": 4096, "classes": 65535, "races": 65535, "ac": 2, "item": 54226}}
        try:
            sheet.class_id = 3
            sheet.race = 1
            sheet.level = 7
            sheet.bags[22] = 54226
            sheet.bots.roster = [Bot(name="Entwar", class_id=1, level=7)]
            client.queue.append(Trade(1, 9), sheet)
            assign(client, sheet, client.journal)
        finally:
            assign_mod._ITEMS = saved
        self.assertEqual([action for action in client.queue if isinstance(action, Distribute)], [])
        self.assertEqual([action for action in client.queue if type(action).__name__ == "Cursor"], [])

    def test_a_spell_scroll_on_the_cursor_is_scribed(self):
        from eqclient3.actions.scribe import ScribeSpell
        from eqclient3.handlers.items import Held

        client, sheet = fresh()
        sheet.cursor = 59964
        sheet.class_id = 12
        sheet.items[59964] = Held(59964, "Spell: Numbing Cold", 20, 1, 374)
        assign(client, sheet, client.journal)
        moves = [action for action in client.queue if type(action).__name__ == "Cursor"]
        scribes = [action for action in client.queue if isinstance(action, ScribeSpell)]
        self.assertEqual(moves, [])
        self.assertEqual(len(scribes), 1)
        self.assertEqual((scribes[0].spell_id, scribes[0].slot, scribes[0].priority), (374, 0, 340))

    def test_a_named_scroll_without_an_effect_still_scribes(self):
        import eqclient3.actions.scribe as scribe_mod
        from eqclient3.actions.scribe import ScribeSpell
        from eqclient3.handlers.items import Held

        client, sheet = fresh()
        sheet.cursor = 59964
        sheet.class_id = 12
        sheet.items[59964] = Held(59964, "Spell: Numbing Cold", 20, 1, 0)
        previous = scribe_mod._NAMED
        scribe_mod._NAMED = {(12, "numbing cold"): 374}
        try:
            assign(client, sheet, client.journal)
        finally:
            scribe_mod._NAMED = previous
        scribes = [action for action in client.queue if isinstance(action, ScribeSpell)]
        self.assertEqual([action.spell_id for action in scribes], [374])

    def test_bracers_go_on_a_wrist_and_a_tome_is_not_sold(self):
        client, sheet = fresh()
        saved = assign_mod._ITEMS
        assign_mod._ITEMS = {
            2009: {"slots": 1536, "classes": 65535, "races": 65535, "ac": 3, "item": 2009},
            59973: {"slots": 0, "classes": 65535, "races": 65535, "item": 59973},
        }
        try:
            sheet.cursor = 2009
            sheet.bags[23] = 59973
            sheet.class_id = 1
            sheet.race = 1
            sheet.level = 1
            assign(client, sheet, client.journal)
        finally:
            assign_mod._ITEMS = saved
        queued = [action for action in client.queue if type(action).__name__ == "Cursor"]
        self.assertEqual(queued[0].move, (30, 9))
        sold = [action.item_ids for action in client.queue if isinstance(action, Sell)]
        self.assertEqual(sold, [])

    def test_a_refused_wrist_is_not_recorded_and_the_other_wrist_is_used(self):
        client, sheet = fresh()
        saved = assign_mod._ITEMS
        assign_mod._ITEMS = {2009: {"slots": 1536, "classes": 65535, "races": 65535, "ac": 3, "item": 2009}}
        try:
            sheet.cursor = 2009
            sheet.class_id = 1
            sheet.race = 1
            sheet.level = 1
            assign(client, sheet, client.journal)
            move = next(action for action in client.queue if type(action).__name__ == "Cursor")
            move.step(client, sheet)
            inbox(move, "OP_ItemPacket", {"slot": 30, "item_id": 2009})
            move.step(client, sheet)
            self.assertTrue(move.complete)
            self.assertNotIn(9, sheet.bags)
            self.assertEqual(sheet.cursor, 2009)
            self.assertIn(9, sheet.refused_slots)
            assign(client, sheet, client.journal)
        finally:
            assign_mod._ITEMS = saved
        moves = [action.move for action in client.queue if type(action).__name__ == "Cursor" and action.move]
        self.assertIn((30, 10), moves)
        self.assertNotIn((30, 7), moves)

    def test_a_loser_is_marked_and_sold_only_when_the_bags_are_full(self):
        client, sheet = fresh()
        saved = assign_mod._ITEMS
        assign_mod._ITEMS = {
            1: {"slots": 8192, "classes": 65535, "races": 65535, "ac": 10, "nodrop": 1, "item": 1},
            2: {"slots": 8192, "classes": 65535, "races": 65535, "ac": 1, "nodrop": 1, "item": 2},
        }
        try:
            sheet.class_id = 1
            sheet.race = 1
            sheet.level = 1
            sheet.bags[13] = 1
            sheet.bags[23] = 2
            sheet.empty_slots = 4
            assign(client, sheet, client.journal)
            self.assertEqual([action.item_ids for action in client.queue if isinstance(action, Sell)], [])
            self.assertIn(2, client.journal.sell_marks(sheet.name))
            sheet.empty_slots = 0
            assign(client, sheet, client.journal)
        finally:
            assign_mod._ITEMS = saved
        sold = [action for action in client.queue if isinstance(action, Sell)]
        self.assertEqual(len(sold), 1)
        self.assertEqual(sold[0].item_ids, [2])
        self.assertEqual(sold[0].priority, 60)

    def test_a_replaced_piece_falls_to_the_next_companion_and_the_last_is_sold(self):
        client, sheet = fresh()
        saved = assign_mod._ITEMS
        assign_mod._ITEMS = {
            10: {"slots": 8192, "classes": 65535, "races": 65535, "ac": 10, "nodrop": 1, "item": 10},
            6: {"slots": 8192, "classes": 65535, "races": 65535, "ac": 6, "nodrop": 1, "item": 6},
            1: {"slots": 8192, "classes": 65535, "races": 65535, "ac": 1, "nodrop": 1, "item": 1},
            3: {"slots": 8192, "classes": 65535, "races": 65535, "ac": 3, "nodrop": 1, "item": 3},
        }
        try:
            sheet.class_id = 1
            sheet.race = 1
            sheet.level = 1
            sheet.cursor = 10
            sheet.bags[13] = 6
            sheet.bots.roster = [
                Bot(name="Macwara", class_id=1, level=1),
                Bot(name="Macclra", class_id=1, level=1),
            ]
            client.journal.set_worn(sheet.name, "Macwara", 13, 1)
            client.journal.set_worn(sheet.name, "Macclra", 13, 3)
            assign(client, sheet, client.journal)
        finally:
            assign_mod._ITEMS = saved
        moves = [action.move for action in client.queue if type(action).__name__ == "Cursor"]
        self.assertEqual(moves, [(30, 13)])
        handed = [action for action in client.queue if isinstance(action, Distribute)]
        self.assertEqual([(action.bot, action.item, action.slots) for action in handed], [("Macwara", 6, [13, 14])])
        self.assertIn(1, client.journal.sell_marks(sheet.name))
        self.assertNotIn(6, client.journal.sell_marks(sheet.name))
        self.assertNotIn(3, client.journal.sell_marks(sheet.name))

    def test_food_water_and_bandages_move_into_a_backpack(self):
        client, sheet = fresh()
        saved = assign_mod._ITEMS
        assign_mod._ITEMS = {
            17005: {"bagslots": 8, "itemtype": 11, "name": "Backpack", "item": 17005},
            13005: {"itemtype": 14, "name": "Iron Ration", "item": 13005},
            13006: {"itemtype": 15, "name": "Water Flask", "item": 13006},
            13009: {"itemtype": 18, "name": "Bandages", "item": 13009},
        }
        try:
            sheet.bags[22] = 17005
            sheet.bags[23] = 13005
            sheet.bags[24] = 13006
            sheet.bags[25] = 13009
            assign(client, sheet, client.journal)
        finally:
            assign_mod._ITEMS = saved
        moves = [action.move for action in client.queue if type(action).__name__ == "Cursor"]
        self.assertEqual(moves, [(23, 251)])

    def test_a_filled_bag_stays_out_of_another_bag(self):
        client, sheet = fresh()
        from eqclient3.inventory.assign import open_slot_for_kit

        saved = assign_mod._ITEMS
        assign_mod._ITEMS = {
            17005: {"bagslots": 8, "itemtype": 11, "name": "Backpack", "item": 17005},
            92882: {"bagslots": 10, "itemtype": 11, "name": "Vale Sewing Kit", "item": 92882},
            9: {"itemtype": 0, "name": "a rock", "item": 9},
        }
        try:
            sheet.cursor = 92882
            sheet.bags[22] = 17005
            sheet.bags[251] = 13009
            sheet.bags[23] = 17005
            for slot in range(24, 30):
                sheet.bags[slot] = 9
            move = open_slot_for_kit(sheet, 92882)
        finally:
            assign_mod._ITEMS = saved
        self.assertEqual(move, (23, 252))


if __name__ == "__main__":
    unittest.main()
