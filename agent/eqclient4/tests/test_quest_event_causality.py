"""Regression tests for per-signal Perl encounter provenance."""

import unittest

from eqclient4.quests.graph import (
    QuestGraph,
    _link_event_causality,
    _outgoing_signals,
    link_script,
)


class QuestEventCausalityTests(unittest.TestCase):
    def test_signal_without_explicit_value_defaults_to_zero(self) -> None:
        script = "sub EVENT_SPAWN { quest::signal(51138); }"
        self.assertEqual(
            _outgoing_signals(script, "lakerathe/shmendrik lavawalker"),
            [("lakerathe/shmendrik lavawalker#event_spawn", 51138, 0)],
        )

    def test_spawn_signal_chain_reaches_hand_in(self) -> None:
        shmendrik = r"""
sub EVENT_ITEM {
    if (plugin::check_handin(\%itemcount, 28044 => 1)) {
        quest::spawn2(51138, 0, 0, 111, 3627, 51, 384); # NPC: Natasha Whitewater
    }
}
sub EVENT_SIGNAL {
    if ($signal == 99) {
        quest::signalwith(51138, 1);
    }
}
# EOF zone: lakerathe ID: 51012
"""
        natasha = r"""
sub EVENT_SPAWN {
    quest::signalwith(51012, 99);
}
sub EVENT_SIGNAL {
    if ($signal == 1) {
        quest::spawn2(51145, 0, 0, 100, 100, 0, 0); # NPC: a spirit of flame
    }
}
# EOF zone: lakerathe ID: 51138
"""
        scripts = [
            ("lakerathe", "lakerathe/shmendrik lavawalker", shmendrik),
            ("lakerathe", "lakerathe/natasha whitewater", natasha),
        ]
        graph = QuestGraph()
        for zone, npc, source in scripts:
            graph.edges.extend(link_script(source, npc.split("/")[-1] + ".pl", zone))
        _link_event_causality(graph, scripts)
        edges = {(e.get("rel"), e.get("from"), e.get("to")) for e in graph.edges}
        self.assertIn(("spawns", "lakerathe/natasha whitewater#signal:1", "npc:51145"), edges)
        self.assertIn(
            (
                "triggers",
                "lakerathe/shmendrik lavawalker#hand:28044",
                "lakerathe/natasha whitewater#event_spawn",
            ),
            edges,
        )
        self.assertIn(
            (
                "triggers",
                "lakerathe/natasha whitewater#event_spawn",
                "lakerathe/shmendrik lavawalker#signal:99",
            ),
            edges,
        )
        self.assertIn(
            (
                "triggers",
                "lakerathe/shmendrik lavawalker#signal:99",
                "lakerathe/natasha whitewater#signal:1",
            ),
            edges,
        )


if __name__ == "__main__":
    unittest.main()
