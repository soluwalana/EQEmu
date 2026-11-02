"""The epic slice of the quest graph stays the same after a parser change.

The fixture was taken from ~/.eqclient/quest_graph.jsonl before ChooseRandom
rewards were recorded. Regenerating the graph must reproduce these lines.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

import pytest

_EPICS = Path(__file__).resolve().parents[5] / ".epics"
_GRAPH = Path.home() / ".eqclient" / "quest_graph.jsonl"
_FIXTURE = Path(__file__).with_name("epic_graph.jsonl")


def epic_flags() -> set[str]:
    flags: set[str] = set()
    for path in sorted(_EPICS.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        head = re.search(r"Flags with writes:\s*(.+)", text)
        if head:
            flags.update(re.findall(r"`([^`]+)`", head.group(1)))
        flags.update(re.findall(r"Sets `([^`]+)`", text))
        flags.update(re.findall(r"- `([^`]+)` set to", text))
    return flags


def epic_lines(graph_path: Path) -> list[str]:
    flags = epic_flags()
    steps: set[str] = set()
    npcs: set[str] = set()
    with graph_path.open(encoding="utf-8") as handle:
        for line in handle:
            if '"flag"' not in line and '"to": "flag:' not in line:
                continue
            row = json.loads(line)
            flag = str(row.get("flag") or "")
            token = str(row.get("to") or "")
            name = flag or (token[5:] if token.startswith("flag:") else "")
            if name not in flags:
                continue
            origin = str(row.get("from") or "")
            group = str(row.get("group") or "")
            if origin:
                steps.add(origin)
            if group:
                steps.add(group)
            npc = origin.split("#", 1)[0]
            if npc:
                npcs.add(npc)

    def keep(row: dict[str, object]) -> bool:
        origin = str(row.get("from") or "")
        group = str(row.get("group") or "")
        if origin in steps or group in steps:
            return True
        if row.get("kind") != "edge" and "npc" in row and "zone" in row:
            npc = f"{row['zone']}/{str(row['npc']).lower()}"
            word = f"{npc}#{str(row.get('word') or '').lower()}"
            return npc in npcs and (
                (row.get("kind") == "say" and word in steps)
                or (row.get("kind") == "hand" and any(step.startswith(npc + "#") for step in steps))
            )
        return False

    kept: list[str] = []
    with graph_path.open(encoding="utf-8") as handle:
        for line in handle:
            if '"from"' not in line and '"npc"' not in line:
                continue
            row = json.loads(line)
            if keep(row):
                kept.append(json.dumps(row, ensure_ascii=True, sort_keys=True))
    kept.sort()
    return kept


def test_epic_graph_matches_the_cached_slice() -> None:
    if not _GRAPH.is_file():
        pytest.skip("quest graph is not built")
    if not _FIXTURE.is_file():
        pytest.skip("epic graph cache is missing")
    expected = _FIXTURE.read_text(encoding="utf-8").splitlines()
    actual = epic_lines(_GRAPH)
    assert actual == expected
