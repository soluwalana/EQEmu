"""Standalone regression for graph.py JSONL -> cross-NPC SQLite index."""
from __future__ import annotations
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from eqclient4.quests import quest_index as index


def dialogue(source, turns, context=()):
    zone, npc = source.split('/', 1)
    return {'kind': 'dialogue', 'source': source, 'zone': zone, 'npc': npc,
            'turns': [{'input': inp, 'source': f'{source}#{inp.lower()}', 'reply': [{'text': rep, 'channel': 'say', 'guards': [], 'links': []}], 'guards': [], 'effects': []}
                      for inp, rep in turns],
            'transitions': [{'from': 'hail', 'to': 'Ganelorn Oast', 'basis': 'prompt_response', 'prompt_pattern': 'named_person', 'evidence': 'Ganelorn Oast'}] if source.endswith('devin ashwood') else [],
            'context_speech': [{'event': 'event_trade', 'text': s, 'channel': 'say', 'links': [], 'guards': []} for s in context]}


class CrossNpcIndexTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.graph = self.root / 'graph.jsonl'
        self.db = self.root / 'index.sqlite3'
        records = [
            dialogue('gfaydark/lily ashwood', [('hail', 'Are you a ranger?'),
                ('i am a ranger', "I think one day Ganelorn Oast will ask me to marry him.")]),
            dialogue('gfaydark/devin ashwood', [('marry', "Why would Ganelorn Oast ask you to marry him?"),
                ('Ganelorn Oast', 'Ganelorn Oast trains rangers. Lily Ashwood likes him.'),
                ('I will take him the letter', 'Lily Ashwood says thank you.')]),
            dialogue('echo/an archer', [('hail', 'I am an archer.')]),
            dialogue('gfaydark/unrelated ranger', [('hail', 'A strong ranger is here, and I will marry one day.')]),
            dialogue('eastkarana/ganelorn oast', [('hail', 'I am tracking a poacher.'),
                ('poacher', 'I am tracking a poacher.')],
                     ['You must have gotten this letter from Lily.']),
            {'kind': 'edge', 'rel': 'gives', 'from': 'gfaydark/devin ashwood',
             'to': 'item:20876', 'group': 'gfaydark/devin ashwood#i will take him the letter'},
            {'kind': 'edge', 'rel': 'receives', 'from': 'eastkarana/ganelorn oast',
             'to': 'item:20876', 'count': 1, 'group': 'eastkarana/ganelorn oast#hand:20876'},
            {'kind': 'edge', 'rel': 'gives', 'from': 'gfaydark/lily ashwood',
             'to': 'item:1', 'group': 'gfaydark/lily ashwood#test'},
            {'kind': 'edge', 'rel': 'receives', 'from': 'gfaydark/lily ashwood',
             'to': 'item:1', 'group': 'gfaydark/lily ashwood#hand:1'},
        ]
        self.graph.write_text('\n'.join(json.dumps(r) for r in records) + '\n', encoding='utf-8')

    def test_index_and_provenance(self):
        result = index.build(self.graph, self.db)
        self.assertEqual(result['npc'], 5)
        self.assertEqual(result['dialogue'], 9)
        self.assertEqual(result['dialogue_transition'], 1)
        self.assertEqual(index.query_npc(self.db, 'gfaydark/devin ashwood')['transitions'][0]['basis'], 'prompt_response')
        self.assertTrue(index.query_npc(self.db, 'gfaydark/devin ashwood'))
        self.assertEqual(index.query_npc(self.db, 'gfaydark/nonexistent'), {})
        events = index.query_item(self.db, 20876)
        self.assertEqual({(e['action'], e['npc_id']) for e in events}, {
            ('gives', 'gfaydark/devin ashwood'), ('receives', 'eastkarana/ganelorn oast')})
        with index.connect(self.db) as con:
            hand = con.execute("SELECT * FROM quest_edge WHERE relation='item_handoff'").fetchall()
            self.assertEqual(len(hand), 1)
            self.assertEqual(hand[0]['from_npc'], 'gfaydark/devin ashwood')
            self.assertEqual(hand[0]['to_npc'], 'eastkarana/ganelorn oast')
            self.assertEqual(hand[0]['confidence'], 'strong')
            self.assertIn('#hand:20876', hand[0]['target_event'])
            ref = con.execute("SELECT * FROM quest_edge WHERE relation='npc_reference' AND from_npc='gfaydark/lily ashwood'").fetchall()
            self.assertEqual(len(ref), 1)
            self.assertEqual(ref[0]['to_npc'], 'eastkarana/ganelorn oast')
            self.assertEqual(ref[0]['confidence'], 'context')
            self.assertEqual(con.execute('SELECT count(*) FROM quest_edge WHERE from_npc=to_npc').fetchone()[0], 0)
            lily = con.execute('''SELECT * FROM quest_edge WHERE relation='cross_npc_dialogue'
                AND from_npc='gfaydark/lily ashwood' AND to_npc='gfaydark/devin ashwood'
                AND matched_input='marry' ''').fetchone()
            self.assertIsNotNone(lily)
            self.assertEqual(lily['source_event'], 'gfaydark/lily ashwood#i am a ranger')
            self.assertEqual(lily['target_event'], 'gfaydark/devin ashwood#marry')
            self.assertEqual(lily['basis'], 'explicit_mention')
            self.assertEqual(lily['relationship_basis'], 'reverse_npc_reference')
            self.assertEqual(lily['confidence'], 'strong_context')
            # Sharing a zone and matching `ranger`/`marry` is insufficient.
            self.assertEqual(con.execute("""SELECT count(*) FROM quest_edge
                WHERE relation='cross_npc_dialogue'
                  AND (from_npc='gfaydark/unrelated ranger'
                       OR to_npc='gfaydark/unrelated ranger')""").fetchone()[0], 0)
            # The same speech names Ganelorn but does not mention his trigger
            # "poacher"; cross-zone name references are not automatic links.
            self.assertEqual(con.execute('''SELECT count(*) FROM quest_edge
                WHERE relation='cross_npc_dialogue' AND from_npc='gfaydark/lily ashwood'
                  AND to_npc='eastkarana/ganelorn oast' ''').fetchone()[0], 0)
            self.assertEqual(con.execute("SELECT count(*) FROM quest_edge WHERE to_npc='echo/an archer' AND relation='npc_reference'").fetchone()[0], 0)
            self.assertEqual(con.execute("SELECT count(*) FROM quest_edge WHERE relation='cross_npc_dialogue' AND matched_input='hail'").fetchone()[0], 0)
        output = self.root / 'cross.jsonl'
        self.assertGreater(index.export(self.db, output), 0)
        assert all(json.loads(l)['kind'] == 'cross_npc_edge' for l in output.read_text().splitlines())
        # Rebuild is idempotent.
        index.build(self.graph, self.db)
        self.assertEqual(index.stats(self.db)['quest_edge'], result['quest_edge'])

    def test_schema_v1_rebuild(self):
        index.build(self.graph, self.db)
        with index.connect(self.db) as con:
            con.execute('ALTER TABLE quest_edge RENAME TO quest_edge_old')
            con.execute('''CREATE TABLE quest_edge (
                id INTEGER PRIMARY KEY, from_npc TEXT, to_npc TEXT,
                relation TEXT, confidence TEXT, evidence TEXT, item_id INTEGER,
                source_event TEXT, target_event TEXT, speech_id INTEGER)''')
            con.execute('DROP TABLE quest_edge_old')
        index.build(self.graph, self.db)
        with index.connect(self.db) as con:
            cols = {r['name'] for r in con.execute('PRAGMA table_info(quest_edge)')}
            self.assertTrue({'matched_input', 'basis', 'relationship_basis'} <= cols)

    def test_invalid_json(self):
        self.graph.write_text('{bad}\n')
        with self.assertRaisesRegex(ValueError, 'graph.jsonl:1'):
            index.build(self.graph, self.db)


if __name__ == '__main__':
    unittest.main()
