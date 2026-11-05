"""Build ~/.eqclient/quest_graph.jsonl from quest scripts."""

from __future__ import annotations

import os
from pathlib import Path

from eqclient4.data.cache_builders.common import peq_path
from eqclient4.data.catalog import load_catalog
from eqclient4.quests.graph import QuestGraph, build_graph, read_graph, write_graph

DEFAULT_GRAPH = str(Path.home() / ".eqclient" / "quest_graph.jsonl")


def quests_root(root: str | None = None) -> str:
    return root or os.environ.get("EQEMU_QUESTS", "")


def ensure_graph(root: str | None = None, path: str | None = None, *, rebuild: bool = False) -> QuestGraph:
    """Load quest_graph.jsonl, or build once from EQEMU_QUESTS."""
    path = path or os.environ.get("EQEMU_GRAPH", DEFAULT_GRAPH)
    file = Path(path)
    if file.is_file() and not rebuild:
        return read_graph(path)
    source = quests_root(root)
    if not source:
        raise SystemExit("EQEMU_QUESTS (or --root) is required to build the quest graph")
    graph = build_graph(source, load_catalog(str(peq_path()), source))
    write_graph(graph, path)
    return graph


def main() -> None:
    path = os.environ.get("EQEMU_GRAPH", DEFAULT_GRAPH)
    graph = ensure_graph(rebuild=True, path=path)
    print(f"quest_graph: {len(graph.edges)} edges → {path}", flush=True)


if __name__ == "__main__":
    main()
