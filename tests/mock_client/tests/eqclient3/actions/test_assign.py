"""Sell skips a recent fetch and a piece the current quest graph requires."""

import unittest

from harness import fresh

from eqclient3.actions.fetch import Fetch
from eqclient3.actions.sell import Sell
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


if __name__ == "__main__":
    unittest.main()
