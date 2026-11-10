"""Generate item-target quest benchmarks using the existing epic acquisition engine.

Run adjacent to .epics/write_epics.py. The synthetic terminal objective is kept
out of the rendered quest: it only makes the existing writer resolve the item.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
import tempfile
from collections import defaultdict
from pathlib import Path


def load_writer(path: Path):
    spec = importlib.util.spec_from_file_location("_epic_writer_for_items", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot import writer at {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def parse_first_step(markdown: str) -> dict:
    """Select an initiatory NPC dialogue when present, otherwise first concrete action.

    Generic supply acquisition is rarely the right initial TaskAgent decision.
    This is a *candidate* start, not proof that every prerequisite is ready.
    """
    candidates = []
    for match in re.finditer(r"^\d+\.\s+(.+)$", markdown, re.MULTILINE):
        step = match.group(1).strip()
        if not step or step.startswith(
            (
                "**Broken:**",
                "Unresolved",
                "Acquisition of ",
                "Alternative:",
                "Common item:",
                "No quest step ",
            )
        ):
            continue
        action = {"instruction": step, "kind": "other"}
        npc = re.match(
            r'(?P<zone>[^/\s]+)/"(?P<npc>[^"]+)",\s*(?P<verb>say|hand)\s+(?P<rest>.+)',
            step,
            re.I,
        )
        if npc:
            action.update(zone=npc["zone"], npc=npc["npc"], kind=npc["verb"].lower())
            if npc["verb"].lower() == "say":
                said = re.match(r'"([^"]+)"', npc["rest"])
                if said:
                    action["utterance"] = said.group(1)
        elif step.startswith(
            (
                "Loot ",
                "Forage ",
                "Buy ",
                "Combine ",
                "Kill ",
                "Spawns ",
                "Ground spawn ",
            )
        ):
            action["kind"] = step.split(" ", 1)[0].lower()
        candidates.append(action)
    for candidate in candidates:
        if candidate["kind"] not in ("other", "combine"):
            return candidate
    return (
        candidates[0]
        if candidates
        else {"kind": "unresolved", "instruction": "No grounded starting action found"}
    )


def render(writer, target: int, graph: Path, verbose: bool) -> tuple[str, dict]:
    writer.GRAPH = graph
    items, edges, says, world, dialogues = writer.load()
    if target not in items:
        raise ValueError(f"Item {target} is absent from {graph}")

    # Add a synthetic objective to reuse the same tested prerequisite expansion.
    # Only indexes local to this invocation are changed; the graph is untouched.
    flag = f"benchmark_target_{target}"
    origin = f"benchmark/goal#complete:{target}"
    edges.extend(
        [
            {
                "kind": "edge",
                "rel": "sets",
                "from": origin,
                "to": f"flag:{flag}",
                "flag": flag,
                "value": "1",
                "group": origin,
            },
            {
                "kind": "edge",
                "rel": "receives",
                "from": "benchmark/goal",
                "to": f"item:{target}",
                "count": 1,
                "group": origin,
            },
        ]
    )
    indexes = writer.indexes(edges, world)
    by_from, by_group, sets_of, gives, loots, grounds, produces, recipe = indexes
    writer.edges_needing = defaultdict(list)
    for edge in edges:
        if edge.get("rel") == "needs" and edge.get("flag"):
            writer.edges_needing[edge["flag"]].append(edge)
    ctx = (items, says, *indexes, dialogues)
    title = writer.item_name(items, target)
    with tempfile.TemporaryDirectory(prefix="eq_item_benchmark_") as tmp:
        old_out = writer.OUT
        try:
            writer.OUT = Path(tmp)
            path, _ = writer.write_class(
                "benchmark", title, [flag], (), ctx, verbose=verbose
            )
            generated = path.read_text(encoding="utf-8")
        finally:
            writer.OUT = old_out

    # Remove the synthetic state flag. Only actual graph-derived acquisition
    # steps and its original dialogue remain in the public benchmark output.
    section = generated.split("## 0. Prerequisites", 1)
    if len(section) == 2:
        text = section[1].split(f"## `{flag}`", 1)[0]
        text = re.sub(
            r"^Shared acquisition steps[^\n]*\n", "", text, count=1, flags=re.M
        ).strip()
        text = re.sub(r"^###\s+[^\n]+\n", "", text, count=1).strip()
    else:
        # A leaf item can legitimately have no full prerequisite chain.
        # Use the writer's own fallback text emitted in the synthetic stage.
        stage = generated.split(f"## `{flag}`", 1)[-1]
        kept = []
        for line in stage.splitlines():
            if re.match(
                r"^\s*- (?:Loot |Buy |Forage |Common item: |No quest step |Ground spawn |Summon |\*\*Broken:)",
                line,
            ):
                kept.append(line.strip().lstrip("- ").strip())
        text = "\n".join(
            f"{idx}. {line}" for idx, line in enumerate(dict.fromkeys(kept), 1)
        )
        if not text:
            text = "1. **Broken:** No acquisition path established by the quest graph."

    # Numbered actionable steps in the first section, preserving writer output.
    first = parse_first_step(text)
    # The dialogue graph may begin before the first quest-reward keyword.
    # Preserve the earliest actual player input when the script extracted it.
    if first.get("kind") == "say" and first.get("zone") and first.get("npc"):
        key = f"{first['zone']}/{first['npc'].lower()}"
        for chain in dialogues.get(key, ()):
            turns = chain.get("turns") or ()
            if turns and str(turns[0].get("input") or "").strip():
                utterance = str(turns[0]["input"]).strip()
                first["utterance"] = utterance
                first["instruction"] = (
                    f"{first['zone']}/\"{first['npc']}\", " f'say "{utterance}".'
                )
                first["source"] = "dialogue_chain_start"
                break
    header = (
        f"# {title}\n\n"
        f"Target item: `{target}`. Source: `quest_graph.jsonl`.\n\n"
        "## Acquisition walkthrough\n\n"
    )
    markdown = header + text + "\n"
    return markdown, first


def main(argv=None):
    p = argparse.ArgumentParser(
        description="Render an item acquisition quest and its TaskAgent starting step"
    )
    p.add_argument("--item", "-i", type=int, required=True, help="Target item ID")
    p.add_argument(
        "--graph", type=Path, default=Path.home() / ".eqclient/quest_graph.jsonl"
    )
    p.add_argument(
        "--writer", type=Path, default=Path(__file__).with_name("write_epics.py")
    )
    p.add_argument(
        "--out", type=Path, default=Path(__file__).resolve().parent / "item_quests"
    )
    p.add_argument(
        "--first-step",
        action="store_true",
        help="Write/print the first action as a structured benchmark",
    )
    p.add_argument(
        "--start-only",
        action="store_true",
        help="Print only first action JSON (implies --first-step)",
    )
    p.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Include graph dialogue as in the epic writer",
    )
    a = p.parse_args(argv)
    if a.item <= 0:
        p.error("--item must be a positive integer")
    if not a.graph.is_file() or not a.writer.is_file():
        p.error("The quest graph and .epics/write_epics.py must both exist")
    writer = load_writer(a.writer)
    md, first = render(writer, a.item, a.graph, a.verbose)
    incomplete = any(
        token in md
        for token in (
            "**Broken:**",
            "No quest step gives",
            "Unresolved",
            "Unresolved cyclic",
        )
    )
    task = {
        "target_item_id": a.item,
        "goal": f"Obtain item {a.item}",
        "start": first,
        "success": {"inventory_contains_item_id": a.item},
        "source": "quest_graph.jsonl",
        "status": (
            "unresolved"
            if first["kind"] == "unresolved"
            else "partial_graph_coverage" if incomplete else "candidate"
        ),
        "graph_warnings": incomplete,
    }
    a.out.mkdir(parents=True, exist_ok=True)
    mdpath = a.out / f"{a.item}.md"
    if not a.start_only:
        mdpath.write_text(md, encoding="utf-8")
        print(mdpath)
    if a.first_step or a.start_only:
        jpath = a.out / f"{a.item}.start.json"
        jpath.write_text(
            json.dumps(task, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )
        print(json.dumps(task, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
