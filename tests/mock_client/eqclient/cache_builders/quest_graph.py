"""Build ~/.eqclient/quest_graph.jsonl from quest scripts."""

from __future__ import annotations

import os
from pathlib import Path

from eqclient.quests import build_graph, read_graph, write_graph

DEFAULT_GRAPH = str(Path.home() / ".eqclient" / "quest_graph.jsonl")


def quests_root(root: str | None = None) -> str:
    return root or os.environ.get("EQEMU_QUESTS", "")


def ensure_graph(root: str | None = None, path: str | None = None, *, rebuild: bool = False):
    """Load quest_graph.jsonl, or build once from EQEMU_QUESTS."""
    path = path or os.environ.get("EQEMU_GRAPH", DEFAULT_GRAPH)
    file = Path(path)
    if file.is_file() and not rebuild:
        return read_graph(path)
    source = quests_root(root)
    if not source:
        raise SystemExit("EQEMU_QUESTS (or --root) is required to build the quest graph")
    graph = build_graph(source)
    write_graph(graph, path)
    return graph


def main() -> None:
    path = os.environ.get("EQEMU_GRAPH", DEFAULT_GRAPH)
    graph = ensure_graph(rebuild=True, path=path)
    nodes = sum(len(group) for group in graph.nodes.values()) if graph.nodes else 0
    print(f"quest_graph: {nodes} nodes → {path}", flush=True)


if __name__ == "__main__":
    main()
