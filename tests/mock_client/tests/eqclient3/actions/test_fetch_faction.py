"""FetchFaction takes the largest reachable quest, else one nearby NPC kill."""

import unittest
from types import SimpleNamespace

from harness import fresh, kinds

from eqclient3.actions.fetch_faction import FetchFaction
from eqclient3.actions.talk import Talk


class FetchFactionTest(unittest.TestCase):
    def test_skips_an_unreachable_chain(self):
        client, sheet = fresh()
        far = SimpleNamespace(
            faction_id=5,
            value=100,
            start="unloaded",
            zones=("unloaded",),
            actions=[Talk(1, "hail", "far")],
            source="faction:5:far",
        )
        near = SimpleNamespace(
            faction_id=5,
            value=40,
            start="qeynos",
            zones=("qeynos",),
            actions=[Talk(2, "hail", "near")],
            source="faction:5",
        )
        sheet.reachable = {"qeynos"}
        sheet.faction_quests = [far, near]
        action = FetchFaction(5)
        action.step(client, sheet)
        self.assertTrue(action.complete)
        talks = [row for row in client.queue if type(row).__name__ == "Talk"]
        self.assertEqual(len(talks), 1)
        self.assertEqual(talks[0].task_text, "near")

    def test_second_line_does_not_append_while_the_source_is_open(self):
        client, sheet = fresh()
        quest = SimpleNamespace(
            faction_id=5,
            value=10,
            start="qeynos",
            zones=("qeynos",),
            actions=[Talk(2, "hail", "deed")],
            source="faction:5",
        )
        sheet.reachable = {"qeynos"}
        sheet.faction_quests = [quest]
        FetchFaction(5).step(client, sheet)
        before = len(client.queue)
        FetchFaction(5).step(client, sheet)
        self.assertEqual(len(client.queue), before)
        self.assertEqual(kinds(client).count("Talk"), 1)

    def test_no_quest_appends_one_kill(self):
        client, sheet = fresh()
        sheet.level = 10
        sheet.faction_npcs = [
            SimpleNamespace(spawn_id=8, level=12, value=5),
            SimpleNamespace(spawn_id=9, level=40, value=50),
            SimpleNamespace(spawn_id=10, level=11, value=20),
        ]
        FetchFaction(5).step(client, sheet)
        kills = [row for row in client.queue if type(row).__name__ == "Kill"]
        self.assertEqual(len(kills), 1)
        self.assertEqual(kills[0].spawn_id, 10)


if __name__ == "__main__":
    unittest.main()
