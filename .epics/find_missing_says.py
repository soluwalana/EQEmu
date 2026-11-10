#!/usr/bin/env python3
"""Audit unexplained SAY inputs using the exact matcher used by the quest graph.

Run with PYTHONPATH=tests/mock_client if this script is outside the package.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

from eqclient4.quests.graph import _speech_mentions


def _turn_mentions(phrase: str, turns: list[dict]) -> bool:
    return any(_speech_mentions(phrase, turn.get("reply") or []) for turn in turns)


def missing_links(path: Path, scope: str, include_hail: bool = False):
    with path.open(encoding="utf-8") as file:
        for line_no, line in enumerate(file, 1):
            if not line.strip():
                continue
            try:
                chain = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"{path}:{line_no}: {exc}") from exc
            if chain.get("kind") != "dialogue":
                continue
            turns = chain.get("turns") or []

            for index, turn in enumerate(turns):
                keyword = str(turn.get("input") or "").strip()
                if not keyword or (not include_hail and keyword.casefold() == "hail"):
                    # Hail is a universal interaction, not a discoverable SAY link.
                    continue
                observed_turns = (
                    [other for j, other in enumerate(turns) if j != index]
                    if scope == "all"
                    else (
                        turns[:index]
                        if scope == "history"
                        else turns[index - 1 : index]
                    )
                )
                # With --scope all, include text from item/trade events.
                # Do not merge those event-gated replies into chronological
                # --scope history/previous conversations.
                context = (chain.get("context_speech") or []) if scope == "all" else []
                event_evidence = (
                    _turn_mentions(keyword, [{"reply": context}]) if context else False
                )
                if index > 0 and not (
                    _turn_mentions(keyword, observed_turns) or event_evidence
                ):
                    prev = turns[index - 1]
                    yield {
                        "source": chain.get("source", ""),
                        "zone": chain.get("zone", ""),
                        "npc": chain.get("npc", ""),
                        "previous_input": prev.get("input", ""),
                        "missing_input": keyword,
                        "previous_reply": "\n".join(
                            str(r.get("text") or "") for r in prev.get("reply") or []
                        ),
                        "scope": scope,
                        "turn_index": index,
                        "guards": turn.get("guards") or [],
                    }


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("graph", type=Path, help="Path to quest_graph.jsonl")
    parser.add_argument(
        "--scope",
        choices=("all", "history", "previous"),
        default="all",
        help="Check all branches, earlier branches, or preceding branch (default: all)",
    )
    parser.add_argument(
        "--include-hail",
        action="store_true",
        help="Include universal hail entry points in missing-link reports",
    )
    parser.add_argument("--format", choices=("csv", "jsonl"), default="csv")
    parser.add_argument(
        "-o", "--output", type=Path, help="Output file (default: stdout)"
    )
    args = parser.parse_args(argv)
    try:
        rows = list(missing_links(args.graph, args.scope, args.include_hail))
    except (OSError, ValueError) as exc:
        parser.error(str(exc))
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        stream = args.output.open("w", encoding="utf-8", newline="")
    else:
        stream = sys.stdout
    try:
        if args.format == "jsonl":
            for row in rows:
                stream.write(json.dumps(row, ensure_ascii=False) + "\n")
        else:
            columns = (
                "source",
                "previous_input",
                "missing_input",
                "previous_reply",
                "scope",
                "turn_index",
                "guards",
            )
            writer = csv.DictWriter(stream, fieldnames=columns, extrasaction="ignore")
            writer.writeheader()
            for row in rows:
                writer.writerow({**row, "guards": json.dumps(row["guards"])})
    finally:
        if args.output:
            stream.close()
    print(
        f"Found {len(rows)} dialogue inputs absent from {args.scope} NPC speech.",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
