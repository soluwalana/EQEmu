"""Build ~/.eqclient/zone_graph.jsonl from a peq dump."""

from __future__ import annotations

from eqclient4.nav.travel import DEFAULT_ZONE_GRAPH
from eqclient4.nav.travel import ensure_zone_graph as ensure_zone_graph


def main() -> None:
    graph = ensure_zone_graph(rebuild=True)
    print(
        f"zone_graph: {len(graph.zones)} zones, {len(graph.transits)} transits → {DEFAULT_ZONE_GRAPH}",
        flush=True,
    )


if __name__ == "__main__":
    main()
