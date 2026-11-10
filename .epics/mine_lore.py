#!/usr/bin/env python3
"""Mine nonliteral dialogue transitions from ProjectEQ quest scripts.

Install at tests/mock_client/eqclient4/quests/mine_lore.py, or run it from
anywhere with PYTHONPATH=tests/mock_client. Uses graph.dialogue_chains() for
Perl/Lua parsing and does not alter the quest graph.

Outputs:
  lore_candidates.jsonl: *possible* response -> follow-up links, with evidence
  lore_book.jsonl:       only explicitly reviewed/model-accepted lore relations
  lore_stats.json:        coverage and classifier counts

A script's elseif order is NOT necessarily a conversation path. Thus the
candidate file is not a set of true links, and without --llm the lore book is
empty. No deity/name associations are hardcoded here.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from urllib import request

from eqclient4.quests.graph import dialogue_chains, DialogueChain, DialogueTurn

WORD = re.compile(r"[a-z][a-z'-]{2,}", re.I)
COMMON = frozenset("""the and this that with from have your you are was were will would
could they them their there here those these into not for but she her his him has
had who what when where why how all our one two said says say tell told which
been about more much some can just then than did does its it's out now after
after before over very back need keep again near through comes come take give
look see things thing something someone every people many other only upon
may even also know like good any get got don't isn't doesn't isn't well
""".split())
SENTENCE = re.compile(r"(?<=[.!?])\s+|\n+")


def tokens(text: str) -> set[str]:
    return {w for w in WORD.findall(text.lower()) if len(w) > 3 and w not in COMMON}


def literal_mention(keyword: str, message: str) -> bool:
    return bool(
        re.search(r"(?<!\w)" + re.escape(keyword.strip()) + r"(?!\w)", message, re.I)
    )


def speech_text(turn: DialogueTurn) -> str:
    return " ".join(
        str(r.get("text", "")) for r in turn.get("reply", ()) if r.get("text")
    )


def iter_scripts(root: Path):
    for path in sorted(root.rglob("*")):
        if path.is_file() and path.suffix.lower() in (".lua", ".pl"):
            yield path


def load_dialogues(root: Path, limit: int = 0) -> tuple[list[DialogueChain], Counter]:
    records: list[DialogueChain] = []
    stats: Counter = Counter()
    for path in iter_scripts(root):
        if limit and stats["files"] >= limit:
            break
        stats["files"] += 1
        try:
            src = path.read_text(encoding="utf-8", errors="replace")
            # Include instances/v1 etc in provenance. The graph's zone key is
            # still the parent zone, matching build_graph's convention.
            rel = path.relative_to(root)
            zone = rel.parts[0].lower()
            for dialogue in dialogue_chains(src, path.name, zone):
                dialogue["file"] = str(rel)
                records.append(dialogue)
                stats["chains"] += 1
                stats["turns"] += len(dialogue.get("turns", ()))
        except Exception as exc:
            stats["failed_files"] += 1
            print(f"WARN {path}: {exc}", file=sys.stderr)
    return records, stats


@dataclass(frozen=True)
class Passage:
    source: str
    file: str
    keyword: str
    text: str
    terms: frozenset[str]


def evidence_index(dialogues: list[DialogueChain]):
    """Index independent script speech for corroborating facts.

    This index proves only that words co-occur in a script passage. It does
    *not* by itself prove semantic equivalence or a conversational transition.
    """
    by_term: dict[str, list[Passage]] = defaultdict(list)
    for dialogue in dialogues:
        for turn in dialogue.get("turns", ()):
            for reply in turn.get("reply", ()):
                text = str(reply.get("text", ""))
                if not text:
                    continue
                for sentence in SENTENCE.split(text):
                    sentence = sentence.strip()
                    terms = frozenset(tokens(sentence))
                    if not terms:
                        continue
                    passage = Passage(
                        dialogue["source"],
                        dialogue.get("file") or "",
                        str(turn.get("input", "")),
                        sentence,
                        terms,
                    )
                    for term in terms:
                        by_term[term].append(passage)
    return by_term


def corroborate(
    keyword: str, context: str, by_term, current_source: str, max_count: int = 4
) -> list[dict]:
    key = tokens(keyword)
    surrounding = tokens(context) - key
    if not key or not surrounding:
        return []
    matches: list[tuple[int, Passage]] = []
    seen: set[tuple[str, str]] = set()
    for term in key:
        for passage in by_term.get(term, ()):
            ident = (passage.file, passage.text)
            if ident in seen or passage.source == current_source:
                continue
            seen.add(ident)
            overlap = surrounding.intersection(passage.terms)
            if overlap:
                matches.append((len(overlap), passage))
    matches.sort(key=lambda pair: (-pair[0], pair[1].file, pair[1].text))
    return [
        {
            "file": p.file,
            "npc": p.source,
            "text": p.text,
            "shared_terms": sorted(surrounding & p.terms),
        }
        for _score, p in matches[:max_count]
    ]


def candidates(dialogues: list[DialogueChain], by_term, lookback: int) -> list[dict]:
    out: list[dict] = []
    for chain in dialogues:
        turns = chain.get("turns", [])
        for j in range(1, len(turns)):
            target = turns[j]
            keyword = str(target.get("input") or "").strip()
            if not keyword:
                continue
            # Consider prior turns, but do not treat textual branch adjacency
            # as proof the player actually followed that route.
            for i in range(max(0, j - lookback), j):
                prior = turns[i]
                utterance = speech_text(prior)
                if not utterance or literal_mention(keyword, utterance):
                    continue
                # Exclude suggestions that explicitly occur in quoted saylinks
                # as they are not nonobvious transitions.
                record = {
                    "kind": "lore_candidate",
                    "from": {
                        "zone": chain["zone"],
                        "npc": chain["npc"],
                        "input": prior.get("input"),
                        "response": utterance,
                    },
                    "to": {"input": keyword, "response": speech_text(target)},
                    "source": {
                        "file": chain.get("file") or "",
                        "npc": chain["source"],
                        "from_offset": prior.get("order"),
                        "to_offset": target.get("order"),
                    },
                    "script_distance": j - i,
                    "relationship": "candidate_only",
                    "corroboration": corroborate(
                        keyword, utterance, by_term, chain["source"]
                    ),
                }
                out.append(record)
    return out


SYSTEM_PROMPT = """You are extracting EverQuest world knowledge from Perl/Lua
quest scripts to build a lore book used by a game-playing agent.
Decide whether the SECOND player utterance can reasonably be inferred from the
FIRST NPC response, without relying on script order. Distinguish:
- semantic_lore: a world-knowledge connection (e.g. deity, place, faction, title)
- contextual: ordinary pragmatic inference from the dialogue
- unrelated_branch: separate dialogue option with no causal connection
- insufficient: cannot establish a plausible connection
Return ONE JSON object: {"classification": one of the above,
 "confidence": number from 0 to 1, "cue": short verbatim span FROM first response,
 "fact": concise generalizable statement or empty string,
 "reason": brief explanation, "support": "script" | "corroborated" | "model_knowledge" | "none"}.
Do not invent verbatim evidence. Corroboration excerpts are excerpts, not
verification of any fact. If you rely on your own EverQuest knowledge, label
support model_knowledge. An unsupported guess must not become a lore fact.
Do not blindly infer links between successive elseif branches."""


def ask_local_model(
    candidate: dict, api_base: str, model: str, timeout: int, temperature: float = 0.0
) -> dict:
    prompt = {
        "prior_player": candidate["from"]["input"],
        "npc_response": candidate["from"]["response"],
        "proposed_next_player": candidate["to"]["input"],
        "next_npc_response": candidate["to"]["response"],
        "independent_script_excerpts": candidate["corroboration"],
    }
    url = api_base.rstrip("/")
    if not url.endswith("/chat/completions"):
        url = url.removesuffix("/v1") + "/v1/chat/completions"
    payload = {
        "model": model,
        "temperature": temperature,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": json.dumps(prompt, ensure_ascii=False)},
        ],
        "max_tokens": 250,
    }
    req = request.Request(
        url,
        data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"},
    )
    with request.urlopen(req, timeout=timeout) as response:
        result = json.load(response)
    raw = result["choices"][0]["message"]["content"].strip()
    # Some local servers wrap JSON in fences even when prompted not to.
    if raw.startswith("```"):
        raw = re.sub(r"^```(?:json)?\s*|\s*```$", "", raw).strip()
    parsed = json.loads(raw)
    allowed = {"semantic_lore", "contextual", "unrelated_branch", "insufficient"}
    if parsed.get("classification") not in allowed:
        raise ValueError(f"unexpected classification: {parsed!r}")
    parsed["confidence"] = max(0.0, min(1.0, float(parsed.get("confidence", 0))))
    if (
        parsed.get("cue")
        and parsed["cue"].lower() not in candidate["from"]["response"].lower()
    ):
        raise ValueError("fabricated cue: not present in source NPC response")
    if parsed.get("support") not in {
        "script",
        "corroborated",
        "model_knowledge",
        "none",
    }:
        raise ValueError("invalid support")
    return parsed


def dump_jsonl(path: Path, records: list[dict]):
    with path.open("w", encoding="utf-8") as stream:
        for record in records:
            stream.write(json.dumps(record, ensure_ascii=False) + "\n")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--quests",
        type=Path,
        required=True,
        help="path to ProjectEQ/projecteqquests checkout",
    )
    parser.add_argument("--out", type=Path, default=Path.home() / ".eqclient")
    parser.add_argument(
        "--lookback",
        type=int,
        default=2,
        help="number of prior turns to consider per response (default 2)",
    )
    parser.add_argument(
        "--limit-files",
        type=int,
        default=0,
        help="debug: process at most N script files",
    )
    parser.add_argument(
        "--llm", action="store_true", help="classify with local Qwen server"
    )
    parser.add_argument(
        "--model",
        default="Qwen3.5-9B",
        help="model identifier exposed by local OpenAI-compatible server",
    )
    parser.add_argument("--api-base", default="http://127.0.0.1:8000/v1")
    parser.add_argument("--timeout", type=int, default=90)
    parser.add_argument(
        "--max-infer",
        type=int,
        default=0,
        help="limit model calls for development; 0 = all",
    )
    parser.add_argument("--min-confidence", type=float, default=0.8)
    args = parser.parse_args(argv)
    if not args.quests.is_dir():
        parser.error(f"no quest scripts at {args.quests}")
    if args.lookback < 1:
        parser.error("--lookback must be at least 1")
    args.out.mkdir(parents=True, exist_ok=True)
    dialogues, stats = load_dialogues(args.quests, args.limit_files)
    index = evidence_index(dialogues)
    rows = candidates(dialogues, index, args.lookback)
    # Always keep all raw candidates for reprocessing after model upgrades.
    candidate_path = args.out / "lore_candidates.jsonl"
    dump_jsonl(candidate_path, rows)
    print(
        f"Scanned {stats['files']} files, {stats['chains']} dialogue handlers, "
        f"{stats['turns']} turns, {len(rows)} nonliteral candidates",
        flush=True,
    )
    book: list[dict] = []
    results = Counter()
    if args.llm:
        for i, entry in enumerate(rows[: args.max_infer or None]):
            try:
                inference = ask_local_model(
                    entry, args.api_base, args.model, args.timeout
                )
            except Exception as exc:
                results["inference_error"] += 1
                print(f"WARN candidate {i}: {exc}", file=sys.stderr)
                continue
            entry["review"] = inference
            results[inference["classification"]] += 1
            if (
                inference["classification"] == "semantic_lore"
                and inference["confidence"] >= args.min_confidence
                and inference.get("fact")
                and inference.get("cue")
            ):
                book.append(
                    {
                        "kind": "lore_relation",
                        "cue": inference["cue"],
                        "concept": entry["to"]["input"],
                        "fact": inference["fact"],
                        "confidence": inference["confidence"],
                        "support": inference["support"],
                        "provenance": entry["source"],
                        "evidence": entry["from"]["response"],
                        "corroboration": entry["corroboration"],
                        "review_status": "model_proposed",  # not human verified
                    }
                )
        dump_jsonl(args.out / "lore_reviews.jsonl", rows)
    dump_jsonl(args.out / "lore_book.jsonl", book)
    summary: dict = dict(stats)
    summary.update(
        {
            "candidates": len(rows),
            "proposed_lore": len(book),
            "review_counts": dict(results),
        }
    )
    (args.out / "lore_stats.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(f"{len(book)} model-proposed lore relations. Files in {args.out}")


if __name__ == "__main__":
    main()
