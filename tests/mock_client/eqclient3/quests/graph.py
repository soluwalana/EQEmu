"""A quest-graph reader. Edges are the gives, receives, and drops produce expands.

This loads quest_graph.jsonl. It does not parse Perl and it does not import the loop.
"""

from __future__ import annotations

import json
import os
from pathlib import Path


class QuestGraph:
    """Edges arriving at an item, and the item rows stored beside them."""

    def __init__(self) -> None:
        self.edges: list[dict] = []
        self.items: dict[int, dict] = {}
        self.edges_to: dict[str, tuple] = {}
        self._indexed = False

    def index(self) -> None:
        arriving: dict[str, list[dict]] = {}
        for edge in self.edges:
            arriving.setdefault(str(edge.get("to") or ""), []).append(edge)
        self.edges_to = {token: tuple(rows) for token, rows in arriving.items()}
        self._indexed = True

    def to_item(self, item_id: int) -> tuple:
        token = f"item:{int(item_id)}"
        if self._indexed:
            return self.edges_to.get(token, ())
        return tuple(edge for edge in self.edges if str(edge.get("to") or "") == token)

    def gives(self, item_id: int) -> dict | None:
        for edge in self.to_item(item_id):
            if edge.get("rel") == "gives":
                return edge
        return None

    def drops(self, item_id: int) -> list[dict]:
        return [edge for edge in self.to_item(item_id) if edge.get("rel") in {"loots", "grounds"}]

    def receives_in(self, group: str) -> list[tuple[int, int]]:
        found: list[tuple[int, int]] = []
        if not group:
            return found
        for edge in self.edges:
            if edge.get("rel") != "receives" or edge.get("group") != group:
                continue
            item_id = _item_id(edge.get("to"))
            if item_id:
                found.append((item_id, max(1, int(edge.get("count") or 1))))
        return found

    def components(self, item_id: int) -> list[int]:
        """Item ids this reward needs, consumes, or requires."""
        found: list[int] = []
        for edge in self.to_item(item_id):
            if edge.get("rel") not in {"needs", "requires", "consumes"}:
                continue
            origin = str(edge.get("from") or "")
            if not origin.startswith("item:"):
                continue
            piece = _item_id(origin)
            if piece and piece not in found:
                found.append(piece)
        return found


def read_graph(path: str | os.PathLike) -> QuestGraph:
    graph = QuestGraph()
    file = Path(path)
    if not file.is_file():
        graph.index()
        return graph
    with file.open(encoding="utf-8") as handle:
        for line in handle:
            if not line.strip():
                continue
            row = json.loads(line)
            kind = row.get("kind", "")
            if kind == "edge":
                graph.edges.append(row)
                continue
            if kind == "item":
                item_id = int(row.get("item") or 0)
                if not item_id:
                    continue
                graph.items[item_id] = {
                    "name": row.get("name", ""),
                    "zones": list(row.get("zones") or []),
                    "sources": list(row.get("sources") or []),
                    "classes": list(row.get("classes") or []),
                    "races": list(row.get("races") or []),
                }
    graph.index()
    return graph


def load_graph(path: str | os.PathLike | None = None) -> QuestGraph:
    chosen = path or os.environ.get("EQEMU_GRAPH") or str(Path.home() / ".eqclient" / "quest_graph.jsonl")
    return read_graph(chosen)


def split_npc(origin: str) -> tuple[str, str]:
    """'zone/npc#step' is the zone and the npc name."""
    zone, _, rest = str(origin or "").partition("/")
    npc = rest.split("#", 1)[0].strip()
    return zone.strip(), npc


def _item_id(token: str) -> int:
    text = str(token or "")
    if not text.startswith("item:"):
        return 0
    try:
        return int(text.split(":", 1)[1])
    except ValueError:
        return 0
