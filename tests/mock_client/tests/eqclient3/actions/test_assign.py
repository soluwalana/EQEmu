"""Sell skips a recent fetch and a piece the current quest graph requires."""

import struct
import unittest

from harness import fresh

from eqclient3.actions.fetch import Fetch
from eqclient3.actions.sell import Sell
from eqclient3.inventory import assign as assign_mod
from eqclient3.inventory.assign import assign
from eqclient3.quests.graph import QuestGraph


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
        self.assertEqual(sold, [[99]])

    def test_a_cursor_upgrade_sends_move_item(self):
        client, sheet = fresh()
        saved = assign_mod._ITEMS
        assign_mod._ITEMS = {67104: {"slots": 128, "classes": 65535, "races": 65535, "ac": 8, "item": 67104}}
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
        src, dest, _count = struct.unpack("<III", client.outbound[0][1])
        self.assertEqual((src, dest), (30, 7))


if __name__ == "__main__":
    unittest.main()
