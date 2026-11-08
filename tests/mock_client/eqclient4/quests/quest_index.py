"""SQLite second-pass index and cross-NPC linker for ProjectEQ quest graphs.

Consumes graph.py's JSONL output without modifying or reparsing graph.py.
Run after rebuilding the project-wide quest graph.

    python -m eqclient4.quests.quest_index build ~/.eqclient/quest_graph.jsonl
    python -m eqclient4.quests.quest_index stats
    python -m eqclient4.quests.quest_index npc 'gfaydark/devin ashwood'
    python -m eqclient4.quests.quest_index item 20876
    python -m eqclient4.quests.quest_index export -o ~/.eqclient/quest_links.jsonl

Default database is quests/quest_index.sqlite3 beside this module. Use --db to relocate.
Uses existing graph.py matching rules. All evidence preserves source event and provenance.
"""
from __future__ import annotations

import argparse
import collections
import json
import re
import sqlite3
from pathlib import Path
from typing import Iterator

from eqclient4.quests.graph import (
    _speech_mentions, _lex_queries, _lex_tokens, _lex_variants,
    _prompt_response, _reply_intent, _answer_to_question,
)

DEFAULT_DB = Path(__file__).resolve().with_name('quest_index.sqlite3')
SCHEMA = """
PRAGMA foreign_keys = ON;
CREATE TABLE IF NOT EXISTS metadata (key TEXT PRIMARY KEY, value TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS npc (
    id TEXT PRIMARY KEY, zone TEXT NOT NULL, name TEXT NOT NULL,
    normalized_name TEXT NOT NULL, script_path TEXT NOT NULL DEFAULT ''
);
CREATE INDEX IF NOT EXISTS npc_name_idx ON npc(normalized_name);
CREATE TABLE IF NOT EXISTS dialogue (
    id INTEGER PRIMARY KEY, npc_id TEXT NOT NULL REFERENCES npc(id),
    input TEXT NOT NULL, say_source TEXT NOT NULL, ordinal INTEGER NOT NULL,
    guards_json TEXT NOT NULL, effects_json TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS dialogue_npc_idx ON dialogue(npc_id);
CREATE TABLE IF NOT EXISTS dialogue_transition (
    id INTEGER PRIMARY KEY, npc_id TEXT NOT NULL REFERENCES npc(id),
    from_input TEXT NOT NULL, to_input TEXT NOT NULL, basis TEXT NOT NULL,
    prompt_pattern TEXT NOT NULL DEFAULT '', source_order TEXT NOT NULL DEFAULT '',
    evidence TEXT NOT NULL, details_json TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS dialogue_transition_npc_idx ON dialogue_transition(npc_id);
CREATE TABLE IF NOT EXISTS speech (
    id INTEGER PRIMARY KEY, npc_id TEXT NOT NULL REFERENCES npc(id),
    event_type TEXT NOT NULL, event_key TEXT NOT NULL,
    dialogue_id INTEGER REFERENCES dialogue(id), text TEXT NOT NULL,
    channel TEXT NOT NULL, guards_json TEXT NOT NULL, links_json TEXT NOT NULL,
    script_offset INTEGER, source_line INTEGER
);
CREATE INDEX IF NOT EXISTS speech_npc_idx ON speech(npc_id);
CREATE TABLE IF NOT EXISTS item_event (
    id INTEGER PRIMARY KEY, npc_id TEXT NOT NULL REFERENCES npc(id),
    item_id INTEGER NOT NULL, action TEXT NOT NULL CHECK(action IN ('gives','receives')),
    event_group TEXT NOT NULL, source_event TEXT NOT NULL,
    item_count INTEGER NOT NULL DEFAULT 1
);
CREATE INDEX IF NOT EXISTS item_event_lookup ON item_event(item_id, action);
CREATE TABLE IF NOT EXISTS npc_reference (
    id INTEGER PRIMARY KEY, speech_id INTEGER NOT NULL REFERENCES speech(id),
    from_npc TEXT NOT NULL REFERENCES npc(id), to_npc TEXT NOT NULL REFERENCES npc(id),
    matched_name TEXT NOT NULL, ambiguous INTEGER NOT NULL DEFAULT 0
);
CREATE INDEX IF NOT EXISTS npc_ref_to ON npc_reference(to_npc);
CREATE TABLE IF NOT EXISTS quest_edge (
    id INTEGER PRIMARY KEY, from_npc TEXT NOT NULL REFERENCES npc(id),
    to_npc TEXT NOT NULL REFERENCES npc(id), relation TEXT NOT NULL,
    confidence TEXT NOT NULL, evidence TEXT NOT NULL,
    item_id INTEGER, source_event TEXT NOT NULL, target_event TEXT NOT NULL,
    speech_id INTEGER REFERENCES speech(id),
    matched_input TEXT NOT NULL DEFAULT '', basis TEXT NOT NULL DEFAULT '',
    UNIQUE(from_npc, to_npc, relation, item_id, source_event, target_event, speech_id)
);
CREATE INDEX IF NOT EXISTS quest_edge_from ON quest_edge(from_npc);
CREATE INDEX IF NOT EXISTS quest_edge_to ON quest_edge(to_npc);
CREATE INDEX IF NOT EXISTS quest_edge_relation ON quest_edge(relation);
"""


def _json(data: object) -> str:
    return json.dumps(data, ensure_ascii=False, sort_keys=True)


def _norm(value: str) -> str:
    return ' '.join(re.findall(r'\w+', value.casefold().replace('_', ' ')))


def _npc_id(value: str) -> str:
    """Graph endpoints can be NPC IDs or NPC#say/hand identifiers."""
    return value.split('#', 1)[0] if '/' in value else ''


def _item_id(value: object) -> int | None:
    if isinstance(value, str) and value.startswith('item:') and value[5:].isdigit():
        return int(value[5:])
    return None


def connect(path: Path = DEFAULT_DB) -> sqlite3.Connection:
    path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    conn.execute('PRAGMA foreign_keys = ON')
    return conn


def _add_npc(conn: sqlite3.Connection, key: str, zone: str = '', name: str = '') -> None:
    if not key or '/' not in key:
        return
    zone = zone or key.partition('/')[0]
    name = name or key.partition('/')[2].replace('_', ' ')
    conn.execute('INSERT OR IGNORE INTO npc (id,zone,name,normalized_name) VALUES (?,?,?,?)',
                 (key, zone, name, _norm(name)))


def _add_speech(conn: sqlite3.Connection, npc: str, event: str, key: str,
                record: dict, dialogue_id: int | None = None) -> int:
    cur = conn.execute('''INSERT INTO speech
        (npc_id,event_type,event_key,dialogue_id,text,channel,guards_json,links_json,script_offset,source_line)
        VALUES (?,?,?,?,?,?,?,?,?,?)''',
        (npc, event, key, dialogue_id, str(record.get('text') or ''),
         str(record.get('channel') or 'say'), _json(record.get('guards') or []),
         _json(record.get('links') or []), record.get('order') or record.get('offset'),
         record.get('line')))
    return cur.lastrowid


def build(graph_file: Path, db_file: Path = DEFAULT_DB) -> dict[str, int]:
    """Rebuild atomically; existing DB remains usable if ingest fails."""
    conn = connect(db_file)
    try:
        # DDL executes outside the rebuild transaction; all data replacement is
        # transactional, leaving the previous index intact if ingestion fails.
        conn.executescript(SCHEMA)
        # Older indexes are rebuilt in place; retain backward compatibility
        # with schema v1 rather than requiring deletion of the database.
        edge_columns = {row['name'] for row in conn.execute('PRAGMA table_info(quest_edge)')}
        for column in ('matched_input', 'basis'):
            if column not in edge_columns:
                conn.execute(f"ALTER TABLE quest_edge ADD COLUMN {column} TEXT NOT NULL DEFAULT ''")
        with conn:
            for table in ('quest_edge', 'npc_reference', 'item_event', 'speech', 'dialogue_transition', 'dialogue', 'npc', 'metadata'):
                conn.execute(f'DELETE FROM {table}')
            totals: collections.Counter[str] = collections.Counter()
            with graph_file.open(encoding='utf-8') as stream:
                for line_number, line in enumerate(stream, 1):
                    if not line.strip():
                        continue
                    try:
                        record = json.loads(line)
                    except json.JSONDecodeError as exc:
                        raise ValueError(f'{graph_file}:{line_number}: {exc}') from exc
                    if not isinstance(record, dict):
                        continue
                    kind = record.get('kind')
                    if kind == 'dialogue':
                        npc = _npc_id(str(record.get('source') or ''))
                        if not npc:
                            continue
                        _add_npc(conn, npc, record.get('zone') or '', record.get('npc') or '')
                        for ordinal, turn in enumerate(record.get('turns') or []):
                            source = str(turn.get('source') or f'{npc}#{turn.get("input", "").lower()}')
                            cur = conn.execute('''INSERT INTO dialogue
                                (npc_id,input,say_source,ordinal,guards_json,effects_json)
                                VALUES (?,?,?,?,?,?)''',
                                (npc, turn.get('input') or '', source, ordinal,
                                 _json(turn.get('guards') or []), _json(turn.get('effects') or [])))
                            for reply in turn.get('reply') or []:
                                _add_speech(conn, npc, 'event_say', source, reply, cur.lastrowid)
                                totals['speech'] += 1
                            totals['dialogue'] += 1
                        for transition in record.get('transitions') or []:
                            conn.execute('''INSERT INTO dialogue_transition
                                (npc_id,from_input,to_input,basis,prompt_pattern,source_order,evidence,details_json)
                                VALUES (?,?,?,?,?,?,?,?)''',
                                (npc, str(transition.get('from') or ''), str(transition.get('to') or ''),
                                 str(transition.get('basis') or ''),
                                 str(transition.get('prompt_pattern') or ''),
                                 str(transition.get('source_order') or ''),
                                 str(transition.get('evidence') or ''), _json(transition)))
                            totals['dialogue_transition'] += 1
                        for msg in record.get('context_speech') or []:
                            _add_speech(conn, npc, str(msg.get('event') or 'event_item'),
                                        f'{npc}#{msg.get("event") or "event_item"}', msg)
                            totals['speech'] += 1
                    elif kind == 'edge':
                        relation = record.get('rel')
                        if relation not in ('gives', 'receives'):
                            continue
                        iid = _item_id(record.get('to'))
                        source = _npc_id(str(record.get('from') or ''))
                        if iid is None or not source:
                            continue
                        _add_npc(conn, source)
                        group = str(record.get('group') or record.get('from') or source)
                        if '#hand:' in group or '#event_item' in group or '#event_trade' in group:
                            source_event = 'handin'
                        elif '#' in group:
                            source_event = 'event_say'
                        else:
                            source_event = 'unknown'
                        conn.execute('''INSERT INTO item_event
                            (npc_id,item_id,action,event_group,source_event,item_count)
                            VALUES (?,?,?,?,?,?)''',
                            (source, iid, relation, group, source_event, int(record.get('count') or 1)))
                        totals['item_event'] += 1
                    totals['rows'] += 1
            _index_references(conn)
            _link_items(conn)
            _link_references(conn)
            _link_dialogue(conn)
            conn.execute('INSERT INTO metadata VALUES (?,?)', ('graph_file', str(graph_file)))
            conn.execute('INSERT INTO metadata VALUES (?,?)', ('schema_version', '2'))
            totals['npc'] = conn.execute('SELECT count(*) FROM npc').fetchone()[0]
            totals['npc_reference'] = conn.execute('SELECT count(*) FROM npc_reference').fetchone()[0]
            totals['quest_edge'] = conn.execute('SELECT count(*) FROM quest_edge').fetchone()[0]
        return dict(totals)
    finally:
        conn.close()


def _index_references(conn: sqlite3.Connection) -> None:
    """Exact named-entity matches only; no fuzzy name guessing.

    Multi-token NPC names are indexed as consecutive words. Singleton names are
    deliberately excluded to avoid massive ambiguity from names like 'Guard'.
    """
    names: dict[tuple[str, ...], list[str]] = collections.defaultdict(list)
    for npc in conn.execute('SELECT id, normalized_name FROM npc'):
        tokens = tuple(npc['normalized_name'].split())
        if 2 <= len(tokens) <= 6 and tokens[0] not in {'a', 'an', 'the', 'some', 'one', 'my', 'your', 'his', 'her', 'our', 'their'}:
            names[tokens].append(npc['id'])
    widths = set(map(len, names))
    batches = []
    for msg in conn.execute('SELECT id,npc_id,text FROM speech WHERE text != ""'):
        words = _norm(msg['text']).split()
        found = set()
        for width in widths:
            for start in range(len(words) - width + 1):
                term = tuple(words[start:start + width])
                matches = names.get(term, ())
                for dest in matches:
                    if dest != msg['npc_id']:
                        found.add((dest, term, len(matches) > 1))
        for dest, term, ambiguous in found:
            batches.append((msg['id'], msg['npc_id'], dest, ' '.join(term), int(ambiguous)))
        if len(batches) >= 10000:
            conn.executemany('''INSERT INTO npc_reference
                (speech_id,from_npc,to_npc,matched_name,ambiguous) VALUES (?,?,?,?,?)''', batches)
            batches.clear()
    if batches:
        conn.executemany('''INSERT INTO npc_reference
            (speech_id,from_npc,to_npc,matched_name,ambiguous) VALUES (?,?,?,?,?)''', batches)


def _link_items(conn: sqlite3.Connection) -> None:
    """Join grant to consumption; exclude self-links and very common items.

    Mechanically grounded is NOT equivalent to temporally required; retain
    exact source/target event groups so the agent can verify progression.
    """
    for iid, n_givers, n_receivers in conn.execute('''
        SELECT item_id,
        count(DISTINCT CASE WHEN action='gives' THEN npc_id END),
        count(DISTINCT CASE WHEN action='receives' THEN npc_id END)
        FROM item_event GROUP BY item_id'''):
        if not n_givers or not n_receivers or n_givers * n_receivers > 100:
            continue
        grants = list(conn.execute('SELECT DISTINCT npc_id,event_group FROM item_event WHERE item_id=? AND action="gives"', (iid,)))
        accepts = list(conn.execute('SELECT DISTINCT npc_id,event_group FROM item_event WHERE item_id=? AND action="receives"', (iid,)))
        for grant in grants:
            for accept in accepts:
                if grant['npc_id'] == accept['npc_id']:
                    continue
                unique = n_givers == 1 and n_receivers == 1
                conn.execute('''INSERT OR IGNORE INTO quest_edge
                    (from_npc,to_npc,relation,confidence,evidence,item_id,source_event,target_event)
                    VALUES (?,?,?,?,?,?,?,?)''',
                    (grant['npc_id'], accept['npc_id'], 'item_handoff',
                     'strong' if unique else 'candidate',
                     f'Item {iid}: grant {grant["event_group"]} -> hand-in {accept["event_group"]}',
                     iid, grant['event_group'], accept['event_group']))


def _link_references(conn: sqlite3.Connection) -> None:
    """An NPC name spoken by another is contextual evidence, not a quest prerequisite."""
    rows = conn.execute('''
        SELECT r.from_npc,r.to_npc,r.speech_id,r.matched_name,r.ambiguous,
               s.text,s.event_key FROM npc_reference AS r
        JOIN speech AS s ON s.id=r.speech_id''')
    for r in rows:
        conn.execute('''INSERT OR IGNORE INTO quest_edge
            (from_npc,to_npc,relation,confidence,evidence,item_id,source_event,target_event,speech_id)
            VALUES (?,?,?,?,?,?,?,?,?)''',
            (r['from_npc'], r['to_npc'], 'npc_reference',
             'ambiguous' if r['ambiguous'] else 'context',
             r['text'], None, r['event_key'], r['to_npc'], r['speech_id']))



# Do not emit unbounded single-word links for universal conversation commands.
# Longer phrases are still required to pass the original graph matcher.
_GENERIC_SAY_INPUTS = {
    'hail', 'hello', 'hi', 'yes', 'no', 'ready', 'help', 'continue',
    'more', 'thanks', 'thank you', 'goodbye', 'bye',
}
_ANCHOR_STOPWORDS = {
    'i', 'me', 'my', 'you', 'your', 'we', 'our', 'he', 'she', 'him', 'her',
    'a', 'an', 'the', 'is', 'are', 'am', 'was', 'were', 'to', 'of', 'in',
    'do', 'does', 'did', 'what', 'who', 'where', 'which', 'how', 'can',
    'will', 'would', 'not', 'and', 'or', 'it', 'for', 'with', 'on', 'about',
    'want', 'need', 'tell', 'say', 'ask', 'have', 'has', 'be',
}


def _dialogue_anchors(phrase: str) -> set[str]:
    '''Candidate generation only. The final check is graph._speech_mentions.

    Preserve inflections, but never try all NPC pairs. Context-only dialogue
    (e.g. answering an implicit question without shared words) is left for
    semantic analysis instead of silently manufacturing an edge.
    '''
    anchors: set[str] = set()
    for query in _lex_queries(phrase):
        for word in query:
            if len(word) >= 3 and word not in _ANCHOR_STOPWORDS:
                anchors.update(_lex_variants(word))
    return anchors


def _link_dialogue(conn: sqlite3.Connection) -> None:
    '''Connect speech at NPC A to a SAY trigger on NPC B.

    Same-zone targets are eligible. Different-zone targets require that the
    utterance itself identifies the destination NPC by name. Every edge keeps
    its originating speech row and its exact destination SAY event; these are
    *possible* player actions, not proven quest prerequisites.
    '''
    # A word -> eligible SAY branches inverted index avoids a quadratic join.
    by_zone: dict[str, dict[str, set[int]]] = collections.defaultdict(lambda: collections.defaultdict(set))
    anchors_by_id: dict[int, set[str]] = {}
    targets: dict[int, sqlite3.Row] = {}
    for row in conn.execute('''SELECT d.id,d.npc_id,d.input,d.say_source,n.zone
                               FROM dialogue d JOIN npc n ON n.id=d.npc_id'''):
        if _norm(row['input']) in _GENERIC_SAY_INPUTS:
            continue
        anchors = _dialogue_anchors(row['input'])
        if not anchors:
            continue
        targets[row['id']] = row
        anchors_by_id[row['id']] = anchors
        for token in anchors:
            by_zone[row['zone']][token].add(row['id'])

    by_npc: dict[str, set[int]] = collections.defaultdict(set)
    for target_id, row in targets.items():
        by_npc[row['npc_id']].add(target_id)

    named_targets: dict[int, set[str]] = collections.defaultdict(set)
    for row in conn.execute('''SELECT speech_id,to_npc FROM npc_reference
                               WHERE ambiguous=0'''):
        named_targets[row['speech_id']].add(row['to_npc'])

    inserts = []
    for speech in conn.execute('''SELECT s.id,s.npc_id,s.event_key,s.text,s.links_json,
                                       n.zone FROM speech s JOIN npc n ON n.id=s.npc_id'''):
        links = json.loads(speech['links_json'])
        words = set(_lex_tokens(speech['text']))
        for link in links:
            words.update(_lex_tokens(str(link.get('target') or '')))
        # Plural/singular variants help find candidates, but graph.py still
        # makes the authoritative equivalence decision.
        variants = set(words)
        for word in words:
            variants.update(_lex_variants(word))
        candidates: set[int] = set()
        for word in variants:
            candidates.update(by_zone[speech['zone']].get(word, ()))

        # Cross-zone dialogue only if this speech actually names the NPC.
        # Destination lookup is indexed by NPC ID, not by every utterance.
        named = named_targets.get(speech['id'], set())
        if named:
            for named_npc in named:
                for target_id in by_npc.get(named_npc, ()):
                    if anchors_by_id[target_id] & variants:
                        candidates.add(target_id)

        msg = [{'text': speech['text'], 'links': links}]
        for target_id in candidates:
            target = targets[target_id]
            if speech['npc_id'] == target['npc_id']:
                continue
            if not _speech_mentions(target['input'], msg):
                continue
            utterance = speech['text']
            inferred = any(check(target['input'], utterance) for check in
                           (_prompt_response, _reply_intent, _answer_to_question))
            basis = 'prompt_response' if inferred else 'explicit_mention'
            inserts.append((speech['npc_id'], target['npc_id'],
                            'cross_npc_dialogue', 'context', utterance, None,
                            speech['event_key'], target['say_source'], speech['id'],
                            target['input'], basis))
        if len(inserts) >= 10000:
            conn.executemany('''INSERT OR IGNORE INTO quest_edge
                (from_npc,to_npc,relation,confidence,evidence,item_id,
                 source_event,target_event,speech_id,matched_input,basis)
                VALUES (?,?,?,?,?,?,?,?,?,?,?)''', inserts)
            inserts.clear()
    if inserts:
        conn.executemany('''INSERT OR IGNORE INTO quest_edge
            (from_npc,to_npc,relation,confidence,evidence,item_id,
             source_event,target_event,speech_id,matched_input,basis)
            VALUES (?,?,?,?,?,?,?,?,?,?,?)''', inserts)


def query_npc(db: Path, npc: str) -> dict:
    with connect(db) as conn:
        obj = conn.execute('SELECT * FROM npc WHERE id=?', (npc.casefold(),)).fetchone()
        if obj is None:
            return {}
        return {
            'npc': dict(obj),
            'dialogue': [dict(r) for r in conn.execute('SELECT * FROM dialogue WHERE npc_id=? ORDER BY ordinal', (npc.casefold(),))],
            'transitions': [dict(r) for r in conn.execute('SELECT * FROM dialogue_transition WHERE npc_id=? ORDER BY id', (npc.casefold(),))],
            'outgoing': [dict(r) for r in conn.execute('SELECT * FROM quest_edge WHERE from_npc=? ORDER BY relation,to_npc', (npc.casefold(),))],
            'incoming': [dict(r) for r in conn.execute('SELECT * FROM quest_edge WHERE to_npc=? ORDER BY relation,from_npc', (npc.casefold(),))],
        }


def query_item(db: Path, item: int) -> list[dict]:
    with connect(db) as conn:
        return [dict(r) for r in conn.execute('SELECT * FROM item_event WHERE item_id=? ORDER BY action,npc_id', (item,))]


def stats(db: Path) -> dict:
    with connect(db) as conn:
        return {name: conn.execute(f'SELECT count(*) FROM {name}').fetchone()[0]
                for name in ('npc', 'dialogue', 'dialogue_transition', 'speech', 'item_event', 'npc_reference', 'quest_edge')}


def export(db: Path, path: Path) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    with connect(db) as conn, path.open('w', encoding='utf-8') as output:
        n = 0
        for row in conn.execute('SELECT * FROM quest_edge ORDER BY from_npc,to_npc,relation,id'):
            output.write(_json({'kind': 'cross_npc_edge', **dict(row)}) + '\n')
            n += 1
    return n


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--db', type=Path, default=DEFAULT_DB,
                        help=f'Separate quest database (default: {DEFAULT_DB})')
    commands = parser.add_subparsers(dest='command', required=True)
    p = commands.add_parser('build', help='Rebuild global index from graph.py JSONL')
    p.add_argument('graph', type=Path)
    commands.add_parser('stats', help='Count indexed records and cross-NPC relationships')
    p = commands.add_parser('npc', help='Inspect an NPC and its cross-NPC connections')
    p.add_argument('npc_id')
    p = commands.add_parser('item', help='Inspect all grants and hand-ins of an item')
    p.add_argument('item_id', type=int)
    p = commands.add_parser('export', help='Export cross-NPC edges as JSONL')
    p.add_argument('-o', '--output', type=Path, required=True)
    args = parser.parse_args(argv)
    if args.command == 'build':
        value = build(args.graph, args.db)
    elif args.command == 'stats':
        value = stats(args.db)
    elif args.command == 'npc':
        value = query_npc(args.db, args.npc_id)
    elif args.command == 'item':
        value = query_item(args.db, args.item_id)
    else:
        value = {'exported': export(args.db, args.output), 'path': str(args.output)}
    print(json.dumps(value, indent=2, ensure_ascii=False))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
