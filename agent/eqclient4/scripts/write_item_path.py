#!/usr/bin/env python3
"""Generate item acquisition walkthroughs using write_epics_v2's planner.

Unlike v1, this does not inject a synthetic quest objective or parse an epic
walkthrough. It plans directly toward an item ID, using the same acquisition,
dialogue and prerequisite logic as write_epics_v2.py.
"""

import argparse
import json
from pathlib import Path

from eqclient4.scripts.write_epics_v2 import (
    AcquisitionCatalog,
    Graph,
    Planner,
    Step,
    speech_for_step,
)


def first_action(steps: list[Step]) -> dict:
    """Return the first actionable step from the planner's structured output."""
    for step in steps:
        if step.action not in ("say", "hand") and not step.text.startswith(
            (
                "Loot ",
                "Forage ",
                "Fish ",
                "Collect ",
                "Buy ",
                "Combine ",
                "Learn ",
                "Summon ",
                "Open ",
                "Kill ",
            )
        ):
            continue
        kind = step.action or step.text.split(" ", 1)[0].lower()
        result: dict = {"kind": kind, "instruction": step.text}
        if step.actor:
            zone, _, npc = step.actor.partition("/")
            result.update(zone=zone, npc=npc)
        if step.utterance:
            result["utterance"] = step.utterance
        if step.payload:
            result["item_ids"] = list(step.payload)
        return result
    return {"kind": "unresolved", "instruction": "No grounded starting action found"}


def render(graph: Graph, target: int, catalog: AcquisitionCatalog) -> tuple[str, dict]:
    planner = Planner(graph, catalog)
    steps = planner.plan(target)
    verified = any(target in step.produced_items for step in steps)
    first = first_action(steps)

    lines = [
        f"# {graph.name(target)}",
        "",
        f"Target item: `{target}`. Source: `quest_graph.jsonl`.",
        "",
        "## Acquisition walkthrough",
        "",
    ]
    for number, step in enumerate(steps, 1):
        lines.append(f"{number}. {step.text}")
        lines.extend(speech_for_step(graph, step))

    if planner.errors:
        lines.extend(["", "**Unresolved graph dependencies:**"])
        lines.extend(f"- {error}" for error in dict.fromkeys(planner.errors))
    if not verified:
        lines.extend(["", f"**Unverified final reward:** {graph.name(target)}"])

    unresolved = bool(planner.errors) or not verified
    task = {
        "target_item_id": target,
        "goal": f"Obtain item {target}",
        "start": first,
        "success": {"inventory_contains_item_id": target},
        "source": "quest_graph.jsonl",
        "status": (
            "unresolved"
            if first["kind"] == "unresolved" or not verified
            else "partial_graph_coverage" if unresolved else "candidate"
        ),
        "graph_warnings": unresolved,
    }
    return "\n".join(lines).rstrip() + "\n", task


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--item", "-i", type=int, required=True)
    parser.add_argument(
        "--graph", type=Path, default=Path.home() / ".eqclient" / "quest_graph.jsonl"
    )
    parser.add_argument("--out", type=Path, default=Path(__file__).resolve().parent / "item_quests")
    parser.add_argument("--drops", type=Path, help="Explicit drops cache")
    parser.add_argument("--merchants", type=Path, help="Explicit merchants cache")
    parser.add_argument("--recipes", type=Path, help="Explicit recipes cache")
    parser.add_argument("--first-step", action="store_true")
    parser.add_argument("--start-only", action="store_true")
    args = parser.parse_args(argv)

    if args.item <= 0:
        parser.error("--item must be a positive integer")
    if not args.graph.is_file():
        parser.error(f"Quest graph not found: {args.graph}")

    graph = Graph(args.graph)
    catalog = AcquisitionCatalog(args.drops, args.merchants, args.recipes)
    markdown, task = render(graph, args.item, catalog)
    args.out.mkdir(parents=True, exist_ok=True)

    if not args.start_only:
        path = args.out / f"{args.item}.md"
        path.write_text(markdown, encoding="utf-8")
        print(f"{path} ({len(markdown.splitlines())} lines)")

    if args.first_step or args.start_only:
        path = args.out / f"{args.item}.start.json"
        path.write_text(json.dumps(task, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(json.dumps(task, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
