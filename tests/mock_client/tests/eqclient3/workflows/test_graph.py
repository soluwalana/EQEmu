"""A few Perl lines become a gives edge that survives write and read."""

from __future__ import annotations

from pathlib import Path

from eqclient3.quests.graph import build_graph, read_graph, write_graph

SCRIPT = """
sub EVENT_ITEM {
  if (plugin::check_handin(\\%itemcount, 1001 => 1)) {
    quest::summonitem(2002);
  }
}
"""


def test_build_write_read_gives(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.setenv("EQEMU_ZONE_GRAPH", str(tmp_path / "missing-zone-graph.jsonl"))
    monkeypatch.setenv("EQEMU_PEQ", str(tmp_path / "missing.sql"))
    zone = tmp_path / "qeynos"
    zone.mkdir()
    (zone / "a_guard.pl").write_text(SCRIPT, encoding="utf-8")

    graph = build_graph(str(tmp_path))
    edge = graph.gives(2002)
    assert edge
    assert edge["from"] == "qeynos/a guard"
    graph.items[2002]["classes"] = [1]
    graph.items[2002]["races"] = [2]

    path = tmp_path / "quest_graph.jsonl"
    write_graph(graph, str(path))
    loaded = read_graph(path)
    loaded_edge = loaded.gives(2002)
    assert loaded_edge
    assert loaded_edge["rel"] == "gives"
    assert loaded.items[2002]["classes"] == [1]
    assert loaded.items[2002]["races"] == [2]
