"""Offline EverQuest lore search with bounded hybrid retrieval and optional reranking.

Build a fresh v2 index:
    python eq_lore_lookup.py build everquest_lore.jsonl --db lore_v2.db
Search:
    python eq_lore_lookup.py search 'hate corruption' --db lore_v2.db
    python eq_lore_lookup.py search 'hate' --db lore_v2.db

"""

import argparse
import hashlib
import html
import json
import re
import sqlite3
from collections import defaultdict
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any, TypedDict

import numpy as np
from sentence_transformers import CrossEncoder, SentenceTransformer

DEFAULT_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
DEFAULT_RERANKER = "cross-encoder/ms-marco-MiniLM-L-6-v2"
NAV_RE = re.compile(
    r"^(?:Up Next:.*|Top Guide Sections|Was this guide helpful\?|In This Guide|ADVERTISEMENT)$",
    re.I,
)
HEADING_RE = re.compile(r"(?m)^\s*##\s+([^\n]+)\s*$")
FILLER_TITLES = {
    "EverQuest Guide",
    "Lore",
    "Zones",
    "General/Basics",
    "Expansion Packs",
    "World Map",
    "Top Contributors",
}
STOP_WORDS = {
    "and",
    "or",
    "the",
    "of",
    "a",
    "an",
    "to",
    "in",
    "about",
    "related",
    "was",
    "were",
    "that",
    "have",
    "has",
    "with",
    "from",
    "into",
    "those",
    "who",
    "them",
    "their",
    "they",
    "upon",
    "both",
    "are",
    "for",
    "you",
    "his",
    "her",
    "its",
    "but",
    "this",
    "once",
    "looks",
    "sighs",
}

class Chunk(TypedDict):
    id: str
    entity: str
    category: str
    source_title: str
    url: str
    text: str
    searchable: str


class Entity(TypedDict):
    id: str
    name: str
    category: str
    aliases: list[str]
    summary: str
    evidence: list[str]


class EntityResult(TypedDict):
    entity: str
    category: str
    aliases: list[str]
    summary: str
    score: float
    sources: list[dict[str, str]]


class LoreEntry(TypedDict):
    entity: str
    category: str
    source_title: str
    url: str
    passage: str
    score: float
    passage_id: str


def page_category(title: str) -> str:
    if title == "Deities":
        return "deity"
    if title.startswith("NPC "):
        return "npc"  # NPC index includes guilds and factions, too.
    if title == "Races":
        return "race"
    if title == "Norrathian Timeline":
        return "history"
    if title.endswith(" Zones"):
        return "location"
    if title == "Classes":
        return "class"
    if title in ("The Art of Magic", "Weapons"):
        return "lore"
    return "other"


def _split_long(text: str, max_chars: int) -> list[str]:
    """Use paragraph and sentence boundaries, falling back to hard splits."""
    pieces: list[str] = []
    current = ""
    for paragraph in re.split(r"\n\s*\n", text):
        paragraph = paragraph.strip()
        if not paragraph:
            continue
        sentences = (
            [paragraph]
            if len(paragraph) <= max_chars
            else re.split(r"(?<=[.!?])\s+(?=[A-Z\"'])", paragraph)
        )
        for sentence in sentences:
            for start in range(0, len(sentence), max_chars):
                fragment = sentence[start : start + max_chars]
                separator = "\n\n" if len(sentences) == 1 else " "
                if current and len(current) + len(separator) + len(fragment) > max_chars:
                    pieces.append(current)
                    current = ""
                current = (current + separator + fragment).strip()
    if current:
        pieces.append(current)
    return pieces


def chunks_from_article(article: dict[str, Any], max_chars: int = 900) -> list[Chunk]:
    title = html.unescape(str(article.get("title", ""))).strip()
    url = str(article.get("url", ""))
    raw = html.unescape(str(article.get("content", "")))
    matches = list(HEADING_RE.finditer(raw))
    chunks: list[Chunk] = []
    for i, match in enumerate(matches):
        heading = re.sub(r"\s+", " ", match.group(1)).strip()
        if NAV_RE.match(heading):
            break
        end = matches[i + 1].start() if i + 1 < len(matches) else len(raw)
        section = raw[match.end() : end].strip()
        if not section or (heading == title and i == 0):
            continue
        section = re.sub(r"[ \t]+", " ", section)
        section = re.sub(r"\n{3,}", "\n\n", section)
        for j, piece in enumerate(_split_long(section, max_chars)):
            if len(piece) < 35:
                continue
            entity = heading if heading != title else title
            category = page_category(title)
            searchable = f"{entity}. {category}. {piece}"
            uid = hashlib.sha1(f"{url}|{heading}|{j}|{piece}".encode()).hexdigest()[:20]
            chunks.append(
                Chunk(
                    id=uid,
                    entity=entity,
                    category=category,
                    source_title=title,
                    url=url,
                    text=piece,
                    searchable=searchable,
                )
            )
    return chunks


def read_chunks(
    jsonl: str | Path, max_chars: int = 900, include_guides: bool = False
) -> list[Chunk]:
    chunks: list[Chunk] = []
    with open(jsonl, encoding="utf-8") as stream:
        for line in stream:
            if not line.strip():
                continue
            article: dict[str, Any] = json.loads(line)
            title = str(article.get("title", ""))
            if title in FILLER_TITLES:
                continue
            if not include_guides and page_category(title) == "other":
                continue
            chunks.extend(chunks_from_article(article, max_chars))
    return chunks


# These are syntactic patterns, not a vocabulary of EverQuest facts.
# Every extracted name and connection must be supported by original text.
NAME = r"[A-Z][A-Za-z'`-]{2,}(?:\s+(?:(?:of|the)\s+)?[A-Z][A-Za-z'`-]{2,}){0,2}"
NAMED_ROLE = re.compile(
    rf"\b(?i:avatar|servant|follower|followers|worshippers|priests)\s+"
    rf"(?i:of)\s+({NAME})",
)
APPOSITION = re.compile(
    rf"\b(?i:god|goddess|prince|lord|deity)\s+(?i:of)\s+"
    rf"([A-Za-z -]{{3,40}}),\s*({NAME})",
)
TITLE_NAME = re.compile(r"^([^:]{3,70}):\s*(.+)$")
SENTENCES = re.compile(r"(?<=[.!?])\s+(?=[A-Z\"'])")


def _name_key(name: str) -> str:
    return re.sub(r"[^a-z0-9]", "", name.casefold())


def _name_match(a: str, b: str) -> bool:
    ka, kb = _name_key(a), _name_key(b)
    if ka == kb:
        return True
    if min(len(ka), len(kb)) < 6 or abs(len(ka) - len(kb)) > 2:
        return False
    if ka[:3] != kb[:3]:
        return False
    return SequenceMatcher(None, ka, kb).ratio() >= 0.85


def _sentences(text: str) -> list[str]:
    return [s.strip() for s in SENTENCES.split(text.replace("\n", " ")) if s.strip()]


def discover_entities(chunks: list[Chunk]) -> list[Entity]:
    """Discover entity-centric evidence solely from article headings and prose.

    Conservative by design: named headings and explicit named-role constructions
    provide anchors. Alias merging uses spelling similarity only, never lore rules.
    """
    names: dict[str, tuple[str, str]] = {}
    for chunk in chunks:
        heading = chunk["entity"]
        category = chunk["category"]
        root = TITLE_NAME.match(heading)
        main = root.group(1).strip() if root else heading
        if main and main != chunk["source_title"]:
            names.setdefault(_name_key(main), (main, category))
        for sentence in [heading, *_sentences(chunk["text"])]:
            for match in APPOSITION.finditer(sentence):
                candidate = match.group(2).strip()
                if len(candidate.split()) <= 3:
                    names.setdefault(_name_key(candidate), (candidate, "deity"))
            for match in NAMED_ROLE.finditer(sentence):
                candidate = match.group(1).strip()
                if len(candidate.split()) <= 3 and (
                    len(candidate.split()) > 1
                    or sum(candidate.casefold() in c["text"].casefold() for c in chunks) > 1
                    or any(candidate.casefold() in c["entity"].casefold() for c in chunks)
                ):
                    # A role target might be a deity or person; don't assert a
                    # type without independent evidence from a heading/context.
                    names.setdefault(_name_key(candidate), (candidate, "entity"))

    # Heading names have priority over incidental mentions for canonical spelling.
    ordered = sorted(names.values(), key=lambda item: (item[1] == "entity", -len(item[0])))
    groups: list[list[str]] = []
    categories: list[str] = []
    for name, category in ordered:
        for i, group in enumerate(groups):
            if any(_name_match(name, existing) for existing in group):
                if name not in group:
                    group.append(name)
                if categories[i] == "entity" and category != "entity":
                    categories[i] = category
                break
        else:
            groups.append([name])
            categories.append(category)

    entities: list[Entity] = []
    for aliases, category in zip(groups, categories):
        # The heading-first sorting determines preferred spelling.
        canonical = aliases[0]
        patterns = [re.compile(r"(?<!\w)" + re.escape(alias) + r"(?!\w)", re.I) for alias in aliases]
        evidence: list[tuple[int, str, str]] = []
        for chunk in chunks:
            for sentence in _sentences(chunk["text"]):
                if any(pattern.search(sentence) for pattern in patterns):
                    # Prefer explicit definitional/domain statements and passages
                    # where this entity is the subject; never invent predicates.
                    score = (2 if re.search(r"\b(?:god|goddess|deity|created|plane|worship|avatar|lord|prince)\b", sentence, re.I) else 0)
                    score += (2 if sentence.casefold().startswith(canonical.casefold()) else 0)
                    score += (5 if any(
                        match.group(2).casefold() in {alias.casefold() for alias in aliases}
                        for match in APPOSITION.finditer(sentence)
                    ) else 0)
                    score += (1 if chunk["entity"] in aliases else 0)
                    evidence.append((score, chunk["id"], sentence))
        
        if not evidence:
            continue
        
        evidence.sort(key=lambda item: (-item[0], len(item[2])))
        selected: list[tuple[str, str]] = []
        used_passages: set[str] = set()
        for _, pid, sentence in evidence:
            if pid not in used_passages:
                selected.append((pid, sentence))
                used_passages.add(pid)
            if len(selected) >= 6:
                break
        summary = f"{canonical}. " + " ".join(sentence[:350] for _, sentence in selected)
        uid = hashlib.sha1(_name_key(canonical).encode()).hexdigest()[:20]
        entities.append(Entity(id=uid, name=canonical, category=category,
                               aliases=aliases, summary=summary,
                               evidence=[pid for pid, _ in selected]))
    return entities


def encode_texts(texts: list[str], model: str, batch_size: int = 32) -> np.ndarray:
    encoder = SentenceTransformer(model, device="cpu")
    vectors = encoder.encode(
        texts,
        batch_size=batch_size,
        normalize_embeddings=True,
        show_progress_bar=len(texts) > 100,
        convert_to_numpy=True,
    )
    return np.asarray(vectors, dtype=np.float32)


def build(
    jsonl: str | Path,
    db: str | Path,
    model: str = DEFAULT_MODEL,
    include_guides: bool = False,
    max_chars: int = 900,
) -> dict[str, int | str]:
    chunks = read_chunks(jsonl, max_chars=max_chars, include_guides=include_guides)
    if not chunks:
        raise ValueError("No usable lore sections found")
    entities = discover_entities(chunks)
    path = Path(db).expanduser()
    path.parent.mkdir(parents=True, exist_ok=True)
    # Build vectors before modifying an existing database.
    vectors = encode_texts([c["searchable"] for c in chunks], model)
    entity_vectors = encode_texts([e["summary"] for e in entities], model)
    with sqlite3.connect(path) as con:
        con.executescript(
            """
            DROP TABLE IF EXISTS passages_fts;
            DROP TABLE IF EXISTS passages;
            DROP TABLE IF EXISTS metadata;
            DROP TABLE IF EXISTS entities;
            DROP TABLE IF EXISTS entity_fts;
            DROP TABLE IF EXISTS entity_evidence;
            DROP TABLE IF EXISTS entity_links;
            CREATE TABLE passages (
                id TEXT PRIMARY KEY, entity TEXT NOT NULL,
                category TEXT NOT NULL, source_title TEXT NOT NULL,
                url TEXT NOT NULL, text TEXT NOT NULL,
                searchable TEXT NOT NULL, embedding BLOB
            );
            CREATE VIRTUAL TABLE passages_fts USING fts5(
                id UNINDEXED, entity, searchable,
                tokenize='unicode61 remove_diacritics 2'
            );
            CREATE TABLE metadata (key TEXT PRIMARY KEY, value TEXT NOT NULL);
            CREATE TABLE entities (
                id TEXT PRIMARY KEY, name TEXT NOT NULL, category TEXT NOT NULL,
                aliases TEXT NOT NULL, summary TEXT NOT NULL, embedding BLOB NOT NULL
            );
            CREATE VIRTUAL TABLE entity_fts USING fts5(
                id UNINDEXED, name, summary, tokenize='unicode61 remove_diacritics 2'
            );
            CREATE TABLE entity_evidence (
                entity_id TEXT NOT NULL, passage_id TEXT NOT NULL,
                PRIMARY KEY (entity_id, passage_id)
            );
            CREATE TABLE entity_links (
                source_entity_id TEXT NOT NULL, target_entity_id TEXT NOT NULL,
                passage_id TEXT NOT NULL,
                relation TEXT NOT NULL DEFAULT 'co_mentioned',
                PRIMARY KEY (source_entity_id, target_entity_id, passage_id)
            );
            """
        )
        for i, chunk in enumerate(chunks):
            embedding = vectors[i].tobytes()
            con.execute(
                "INSERT INTO passages VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                (
                    chunk["id"], chunk["entity"], chunk["category"],
                    chunk["source_title"], chunk["url"], chunk["text"],
                    chunk["searchable"], embedding,
                ),
            )
            con.execute(
                "INSERT INTO passages_fts(id, entity, searchable) VALUES (?, ?, ?)",
                (chunk["id"], chunk["entity"], chunk["searchable"]),
            )
        for entity, vector in zip(entities, entity_vectors):
            con.execute(
                "INSERT INTO entities VALUES (?, ?, ?, ?, ?, ?)",
                (entity["id"], entity["name"], entity["category"],
                 json.dumps(entity["aliases"]), entity["summary"], vector.tobytes()),
            )
            con.execute("INSERT INTO entity_fts VALUES (?, ?, ?)",
                        (entity["id"], entity["name"], entity["summary"]))
            for pid in entity["evidence"]:
                con.execute("INSERT INTO entity_evidence VALUES (?, ?)", (entity["id"], pid))
        # Corpus-derived, provenance-backed association graph. A link means
        # two indexed entities appear in the same passage, not a claimed
        # causal or family relationship.
        passage_entities: dict[str, set[str]] = defaultdict(set)
        for entity in entities:
            for pid in entity["evidence"]:
                passage_entities[pid].add(entity["id"])
        for pid, ids in passage_entities.items():
            for source in sorted(ids):
                for target in sorted(ids):
                    if source != target:
                        con.execute(
                            "INSERT INTO entity_links VALUES (?, ?, ?, 'co_mentioned')",
                            (source, target, pid),
                        )
        con.execute("INSERT INTO metadata VALUES (?, ?)", ("model", model))
        con.execute(
            "INSERT INTO metadata VALUES (?, ?)",
            ("dimensions", str(vectors.shape[1])),
        )
        con.execute("INSERT INTO metadata VALUES (?, ?)", ("schema_version", "3"))
    return {
        "articles": len({c["url"] for c in chunks}),
        "passages": len(chunks),
        "entities": len(entities),
        "db": str(path),
    }


def _terms(query: str) -> list[str]:
    return [
        term.lower()
        for term in re.findall(r"[^\W_]+", query, flags=re.UNICODE)
        if len(term) > 2 and term.lower() not in STOP_WORDS
    ]


def _focused_query(query: str) -> str:
    """Retain named lore concepts plus salient words from dialogue.

    This deliberately does not invent a causal explanation or an NPC name.
    """
    terms = _terms(query)
    if len(terms) <= 12:
        return query.strip()
    # Preserve first mentions and eliminate repetition from long dialogue.
    return " ".join(dict.fromkeys(terms[:40]))


class LoreLookup:
    """Read-only lookup; load models once per agent process.

    Reranking is optional because it incurs an extra model and CPU work.
    """

    def __init__(
        self,
        db: str | Path,
        model: str | None = None,
        reranker: str = DEFAULT_RERANKER,
    ) -> None:
        path = Path(db).expanduser().resolve()
        self.con = sqlite3.connect(f"file:{path}?mode=ro", uri=True)
        self.con.row_factory = sqlite3.Row
        meta = dict(self.con.execute("SELECT key, value FROM metadata").fetchall())
        self.records: list[sqlite3.Row] = self.con.execute(
            "SELECT * FROM passages ORDER BY rowid"
        ).fetchall()
        self.by_id: dict[str, sqlite3.Row] = {r["id"]: r for r in self.records}
        if meta.get("schema_version") != "3":
            raise ValueError("Requires schema v3; rebuild the lore database")
        self.entities: list[sqlite3.Row] = self.con.execute(
            "SELECT * FROM entities ORDER BY rowid"
        ).fetchall()
        self.entity_by_id: dict[str, sqlite3.Row] = {r["id"]: r for r in self.entities}
        self.entity_matrix = np.vstack([
            np.frombuffer(row["embedding"], dtype=np.float32)
            for row in self.entities
        ])
        self.evidence: dict[str, list[str]] = defaultdict(list)
        for entity_id, passage_id in self.con.execute(
            "SELECT entity_id, passage_id FROM entity_evidence ORDER BY rowid"
        ):
            self.evidence[str(entity_id)].append(str(passage_id))
        if not self.records:
            raise ValueError("Lore index is empty; rebuild with the build command")
        embeddings = [r["embedding"] for r in self.records]
        if any(blob is None for blob in embeddings):
            raise ValueError("Lore index has missing embeddings; rebuild the index")
        self.matrix = np.vstack(
            [np.frombuffer(blob, dtype=np.float32) for blob in embeddings]
        )
        if self.matrix.shape[1] != int(meta["dimensions"]):
            raise ValueError("Stored vector dimension mismatch")
        stored_model = str(meta.get("model", DEFAULT_MODEL))
        if model is not None and model != stored_model:
            raise ValueError("Query model differs from index model; rebuild the index")
        self.encoder = SentenceTransformer(stored_model, device="cpu", local_files_only=True)
        self.reranker = CrossEncoder(reranker, device="cpu", local_files_only=True)

    def close(self) -> None:
        self.con.close()

    def __enter__(self) -> LoreLookup:
        return self

    def __exit__(self, *args: object) -> None:
        self.close()

    def _semantic(self, query: str, limit: int) -> list[str]:
        vector = self.encoder.encode(
            [query], normalize_embeddings=True, convert_to_numpy=True
        )[0]
        similarity = self.matrix @ vector
        order = np.argsort(-similarity)[:limit]
        return [str(self.records[int(i)]["id"]) for i in order]

    def _entity_semantic(self, query: str, limit: int) -> list[str]:
        vector = self.encoder.encode(
            [query], normalize_embeddings=True, convert_to_numpy=True
        )[0]
        order = np.argsort(-(self.entity_matrix @ vector))[:limit]
        return [str(self.entities[int(i)]["id"]) for i in order]

    def _entity_lexical(self, query: str, limit: int) -> list[str]:
        terms = list(dict.fromkeys(_terms(query)))
        if not terms:
            return []
        match = " OR ".join(f'"{term}"' for term in terms[:16])
        return [str(row["id"]) for row in self.con.execute(
            "SELECT id FROM entity_fts WHERE entity_fts MATCH ? "
            "ORDER BY bm25(entity_fts, 0, 6.0, 1.0) LIMIT ?", (match, limit)
        )]

    def search_entities(
        self, query: str, top_k: int = 8
    ) -> list[EntityResult]:
        """Rank corpus-discovered entities, retaining supporting source passages."""
        if not query.strip() or top_k <= 0:
            return []
        focused = _focused_query(query)
        rankings = [
            self._entity_semantic(focused, max(40, top_k * 4)),
            self._entity_lexical(focused, max(20, top_k * 2)),
        ]
        scores: dict[str, float] = defaultdict(float)
        for weight, ids in zip((1.0, 0.75), rankings):
            for rank, eid in enumerate(ids, 1):
                scores[eid] += weight / (60 + rank)
        candidates = sorted(scores, key=lambda eid: -scores[eid])[:max(40, top_k * 4)]
        if candidates:
            pairs = [(focused, str(self.entity_by_id[eid]["summary"])) for eid in candidates]
            values = np.asarray(self.reranker.predict(pairs), dtype=np.float64).reshape(-1)
            ranked = sorted(zip(candidates, values), key=lambda item: -float(item[1]))
        else:
            ranked = [(eid, scores[eid]) for eid in candidates]
        results: list[EntityResult] = []
        for eid, score in ranked[:top_k]:
            entity = self.entity_by_id[eid]
            sources = [
                {
                    "passage_id": pid,
                    "source_title": str(self.by_id[pid]["source_title"]),
                    "url": str(self.by_id[pid]["url"]),
                    "passage": str(self.by_id[pid]["text"]),
                }
                for pid in self.evidence[eid]
            ]
            results.append(EntityResult(
                entity=str(entity["name"]),
                category=str(entity["category"]),
                aliases=json.loads(str(entity["aliases"])),
                summary=str(entity["summary"]),
                score=round(float(score), 6),
                sources=sources,
            ))
        return results

    def _lexical(self, query: str, limit: int) -> list[str]:
        terms = list(dict.fromkeys(_terms(query)))
        if not terms:
            return []
        # FTS tokenizer handles alphanumerics; quoting prevents operator injection.
        fts_query = " OR ".join(f'"{term}"' for term in terms[:16])
        rows = self.con.execute(
            "SELECT id FROM passages_fts WHERE passages_fts MATCH ? "
            "ORDER BY bm25(passages_fts, 0, 8.0, 1.0) LIMIT ?",
            (fts_query, limit),
        )
        return [str(row["id"]) for row in rows]

    def search(
        self,
        query: str,
        top_k: int = 8,
        categories: list[str] | None = None,
        candidate_limit: int = 50,
        per_entity: int = 2,
    ) -> list[LoreEntry]:
        """Rank source-backed passages, returning relative (not probability) scores."""
        if not query.strip() or top_k <= 0:
            return []
        limit = max(candidate_limit, top_k * 3)
        focused = _focused_query(query)
        rankings = [
            self._semantic(focused, limit),
            self._lexical(focused, min(limit, 30)),
        ]
        # Entity records provide a second retrieval surface for individuals
        # mentioned inside passages but absent from wiki section headings.
        entity_ranks = [
            self._entity_semantic(focused, min(limit, 30)),
            self._entity_lexical(focused, min(limit, 20)),
        ]
        entity_fused: dict[str, float] = defaultdict(float)
        for weight, ranking in zip((1.0, 0.75), entity_ranks):
            for rank, eid in enumerate(ranking, start=1):
                entity_fused[eid] += weight / (60 + rank)
        fused: dict[str, float] = defaultdict(float)
        for weight, ranking in zip((1.0, 0.75), rankings):
            for rank, pid in enumerate(ranking, start=1):
                fused[pid] += weight / (60 + rank)
        # Project entity relevance to its original source passages.
        # The named entity remains visible in returned results; evidence is
        # always real source text, never a generated summary.
        entity_for_passage: dict[str, tuple[str, str, float]] = {}
        for eid, score in sorted(entity_fused.items(), key=lambda item: -item[1])[:20]:
            entity = self.entity_by_id[eid]
            for rank, pid in enumerate(self.evidence[eid], start=1):
                contribution = 1.5 * score / (1 + 0.1 * (rank - 1))
                fused[pid] += contribution
                existing = entity_for_passage.get(pid)
                if existing is None or contribution > existing[2]:
                    entity_for_passage[pid] = (
                        str(entity["name"]), str(entity["category"]), contribution
                    )
        allowed = set(categories) if categories else None
        candidates = [
            pid
            for pid, _ in sorted(fused.items(), key=lambda pair: -pair[1])
            if allowed is None
            or self.by_id[pid]["category"] in allowed
            or (pid in entity_for_passage and entity_for_passage[pid][1] in allowed)
        ]
        # Rerank more than top_k, but not the entire indexed corpus.
        candidates = candidates[: max(limit, top_k)]
        if candidates:
            pairs = [
                (focused, str(self.by_id[pid]["searchable"])) for pid in candidates
            ]
            raw = np.asarray(self.reranker.predict(pairs), dtype=np.float64).reshape(-1)
            ranked = sorted(
                zip(candidates, raw), key=lambda pair: float(pair[1]), reverse=True
            )
        else:
            ranked = sorted(
                ((pid, score) for pid, score in fused.items() if pid in candidates),
                key=lambda pair: -pair[1],
            )
        counts: dict[tuple[str, str], int] = defaultdict(int)
        results: list[LoreEntry] = []
        for pid, score in ranked:
            row = self.by_id[pid]
            derived = entity_for_passage.get(pid)
            result_entity = derived[0] if derived else str(row["entity"])
            result_category = derived[1] if derived else str(row["category"])
            key = (str(row["source_title"]), result_entity)
            if counts[key] >= per_entity:
                continue
            counts[key] += 1
            results.append(
                LoreEntry(
                    entity=result_entity,
                    category=result_category,
                    source_title=str(row["source_title"]),
                    url=str(row["url"]),
                    passage=str(row["text"]),
                    score=round(float(score), 6),
                    passage_id=pid,
                )
            )
            if len(results) >= top_k:
                break
        return results


def main() -> None:
    parser = argparse.ArgumentParser(description="EverQuest lore retrieval v3")
    sub = parser.add_subparsers(dest="command", required=True)
    b = sub.add_parser("build")
    b.add_argument("jsonl")
    b.add_argument("--db", default="everquest_lore_v3.db")
    b.add_argument("--model", default=DEFAULT_MODEL)
    b.add_argument("--include-guides", action="store_true")
    b.add_argument("--max-chars", type=int, default=900)
    s = sub.add_parser("search")
    s.add_argument("query")
    s.add_argument("--db", default="everquest_lore_v3.db")
    s.add_argument("--top-k", type=int, default=8)
    s.add_argument("--category", action="append", default=None)
    s.add_argument("--candidate-limit", type=int, default=50)
    s.add_argument("--per-entity", type=int, default=2)
    s.add_argument("--entities", action="store_true", help="Return entity profiles")
    args = parser.parse_args()
    if args.command == "build":
        print(
            json.dumps(
                build(
                    args.jsonl,
                    args.db,
                    model=args.model,
                    include_guides=args.include_guides,
                    max_chars=args.max_chars,
                ),
                indent=2,
            )
        )
    else:
        with LoreLookup(
            args.db, reranker=DEFAULT_RERANKER
        ) as lookup:
            print(
                json.dumps(
                    (lookup.search_entities(args.query, top_k=args.top_k)
                     if args.entities else lookup.search(
                        args.query,
                        top_k=args.top_k,
                        categories=args.category,
                        candidate_limit=args.candidate_limit,
                        per_entity=args.per_entity,
                        rerank=not args.no_rerank,
                    )),
                    ensure_ascii=False,
                    indent=2,
                )
            )


if __name__ == "__main__":
    main()
