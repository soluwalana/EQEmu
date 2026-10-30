"""Build ~/.eqclient/zone_graph.jsonl from a peq dump."""

from __future__ import annotations

import os
from pathlib import Path

from eqclient3.data.cache_builders.common import peq_path
from eqclient3.nav.travel import (
    DEFAULT_ZONE_GRAPH,
    ZoneGraph,
    build_zone_graph,
    read_zone_graph,
    write_zone_graph,
)


def ensure_zone_graph(
    path: str | None = None,
    peq: str | Path | None = None,
    quest_doors: dict[str, dict[int, list[int]]] | None = None,
    *,
    rebuild: bool = False,
) -> ZoneGraph:
    """Load zone_graph.jsonl, or build once from the peq dump."""
    path = path or os.environ.get("EQEMU_ZONE_GRAPH", DEFAULT_ZONE_GRAPH)
    file = Path(path)
    if file.is_file() and not rebuild:
        return read_zone_graph(path)
    dump = peq_path(peq)
    graph = build_zone_graph(dump, quest_doors) if dump.is_file() else ZoneGraph()
    if graph.zones or graph.transits:
        write_zone_graph(graph, path)
    return graph


def main() -> None:
    graph = ensure_zone_graph(rebuild=True)
    print(
        f"zone_graph: {len(graph.zones)} zones, {len(graph.transits)} transits → {DEFAULT_ZONE_GRAPH}",
        flush=True,
    )


if __name__ == "__main__":
    main()
