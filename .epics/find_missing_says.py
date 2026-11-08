#!/usr/bin/env python3
"""List dialogue inputs not literally mentioned in earlier NPC replies.

Reads `kind: dialogue` rows from the quest graph produced by graph.py;
no quest-script parsing, LLM, or lore dictionary.

Example:
    python find_missing_say_links.py ~/.eqclient/quest_graph.jsonl
    python find_missing_say_links.py ~/.eqclient/quest_graph.jsonl --scope previous
    python find_missing_say_links.py ~/.eqclient/quest_graph.jsonl --format jsonl -o missing.jsonl

By default, checks all other NPC responses in each dialogue handler (all).
Use --scope history to require a cue in a preceding source-code branch.
`--scope previous` checks only the immediately preceding source-code branch.
The *full input phrase* must occur literally, ignoring case, punctuation,
underscores, and whitespace. First turns are excluded because there is no
preceding conversation to compare against.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path


_LIST = re.compile(
    r"(?P<first>\b[\w]+(?:\s+(?:of|the|a|an|to|for|in|on|with)\s+[\w]+)+)"
    r"(?P<rest>(?:\s*,\s*(?!(?:or|and)\b)[\w]+)+(?:\s*,?\s*(?:or|and)\s+[\w]+)?)",
    re.IGNORECASE,
)

_QUERY_PREFIXES = (
    ("what",), ("who",), ("where",), ("which",),
    ("what", "is"), ("what", "are"), ("tell", "me", "about"),
    ("a",), ("an",), ("the",),
)


def _lex_tokens(value: str) -> list[str]:
    return re.findall(r"[\w]+", value.casefold().replace("_", " "))


def _lex_variants(token: str) -> set[str]:
    """Small inflection set for singular/plural player triggers.

    This intentionally does not do arbitrary stemming or substring matches.
    """
    variants = {token}
    if len(token) > 4:
        if token.endswith("ies") and len(token) > 5:
            variants.add(token[:-3] + "y")
        if token.endswith("es") and token[-3:-2] in {"s", "x", "z"}:
            variants.add(token[:-2])
        if token.endswith("s") and not token.endswith("ss"):
            variants.add(token[:-1])
    return variants


def _lex_equiv(a: str, b: str) -> bool:
    return bool(_lex_variants(a) & _lex_variants(b))


def _lex_sequence(needle: list[str], haystack: list[str]) -> bool:
    return any(
        all(_lex_equiv(a, b) for a, b in zip(needle, haystack[start:start + len(needle)]))
        for start in range(len(haystack) - len(needle) + 1)
    )


def _lex_queries(value: str) -> list[list[str]]:
    words = _lex_tokens(value)
    candidates = [words]
    for prefix in _QUERY_PREFIXES:
        if words[:len(prefix)] == list(prefix) and len(words) > len(prefix):
            candidates.append(words[len(prefix):])
    # A quest script may test `make the shaft` after the NPC explicitly
    # lists the weapon's parts as `shaft, blade, fittings, hilt`.
    if words[:2] == ["make", "the"] and len(words) > 2:
        candidates.append(words[2:])
    return candidates


def _answer_to_question(phrase: str, reply: str) -> bool:
    """Ground `am a smith` / `not a smith` in `Are you a smith?`.

    This is a yes/no response to an explicit question, not a generic
    removal of negation or of the words `am` and `not`.
    """
    words = _lex_tokens(phrase)
    if len(words) < 3 or words[0] not in {"am", "not"} or words[1] not in {"a", "an"}:
        return False
    profession = words[2:]
    for question in re.findall(r"[^?]*\?", reply):
        tokens = _lex_tokens(question)
        for i in range(len(tokens) - 2):
            if tokens[i:i + 3] in (["are", "you", "a"], ["are", "you", "an"]):
                if _lex_sequence(profession, tokens[i + 3:]):
                    return True
    return False


def _lex_mentioned(phrase: str, replies: list[str]) -> bool:
    """Match the player's expression to spoken offers, without lore inference.

    Covers leading player-question words, inflected plural terms, and shared
    prefixes in comma-separated lists. Checks any earlier reply, not just an
    adjacent sibling branch.
    """
    queries = _lex_queries(phrase)
    if not queries or not queries[0]:
        return False
    for reply in replies:
        tokens = _lex_tokens(reply)
        if _answer_to_question(phrase, reply):
            return True
        if any(_lex_sequence(query, tokens) for query in queries):
            return True
        for match in _LIST.finditer(reply):
            first = _lex_tokens(match.group("first"))
            if len(first) < 3:
                continue
            for option in _lex_tokens(match.group("rest")):
                if option in {"and", "or"}:
                    continue
                for start in range(len(first) - 1):
                    expansion = first[start:-1] + [option]
                    if any(len(query) == len(expansion) and
                           all(_lex_equiv(a, b) for a, b in zip(query, expansion))
                           for query in queries):
                        return True
    return False


def mentioned(phrase: str, replies: list[str]) -> bool:
    return _lex_mentioned(phrase, replies)


def _turn_mentions(phrase: str, turns: list[dict]) -> bool:
    for turn in turns:
        replies = turn.get('reply') or []
        if mentioned(phrase, [str(reply.get('text') or '') for reply in replies]):
            return True
        # A say_link may show a readable alias different from the actual
        # input command used by the EQ client.
        for reply in replies:
            for link in reply.get('links') or []:
                if _lex_mentioned(phrase, [str(link.get('target') or '')]):
                    return True
    return False
 

def missing_links(path: Path, scope: str):
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
                if not keyword:
                    continue
                observed_turns = (
                    [other for j, other in enumerate(turns) if j != index]
                    if scope == "all" else
                    turns[:index] if scope == "history" else turns[index - 1:index]
                )
                # With --scope all, include text from item/trade events.
                # Do not merge those event-gated replies into chronological
                # --scope history/previous conversations.
                context = (chain.get('context_speech') or []) if scope == 'all' else []
                event_evidence = _turn_mentions(keyword, [{'reply': context}]) if context else False
                if index > 0 and not (_turn_mentions(keyword, observed_turns) or event_evidence):
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
    parser.add_argument("--scope", choices=("all", "history", "previous"), default="all",
                        help="Check all branches, earlier branches, or preceding branch (default: all)")
    parser.add_argument("--format", choices=("csv", "jsonl"), default="csv")
    parser.add_argument("-o", "--output", type=Path, help="Output file (default: stdout)")
    args = parser.parse_args(argv)
    try:
        rows = list(missing_links(args.graph, args.scope))
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
            columns = ("source", "previous_input", "missing_input", "previous_reply",
                       "scope", "turn_index", "guards")
            writer = csv.DictWriter(stream, fieldnames=columns, extrasaction="ignore")
            writer.writeheader()
            for row in rows:
                writer.writerow({**row, "guards": json.dumps(row["guards"])})
    finally:
        if args.output:
            stream.close()
    print(f"Found {len(rows)} dialogue inputs absent from {args.scope} NPC speech.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
