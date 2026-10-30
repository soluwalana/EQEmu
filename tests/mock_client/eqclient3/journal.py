"""Memory the server will not resend. One sqlite file, separate from v1 and v2.

Open action rows reload onto the queue. A resolved source is not appended again.
Death clears a removed source so it is neither open nor resolved.
"""
from __future__ import annotations
import base64
import importlib
import json
import os
import sqlite3
from pathlib import Path
from .action import Action
DEFAULT_PATH = str(Path.home() / '.eqclient' / 'journal-v3.sqlite')
_SKIP = {'messages', 'active_path', 'yielding', 'suspended', 'complete', 'insert', 'source', 'zone', 'priority', 'durable'}
_SCHEMA = "\nCREATE TABLE IF NOT EXISTS says (\n    character TEXT NOT NULL, zone TEXT NOT NULL, npc TEXT NOT NULL, text TEXT NOT NULL,\n    PRIMARY KEY (character, zone, npc, text)\n);\nCREATE TABLE IF NOT EXISTS handins (\n    character TEXT NOT NULL, zone TEXT NOT NULL, npc TEXT NOT NULL,\n    item_id INTEGER NOT NULL, count INTEGER NOT NULL,\n    PRIMARY KEY (character, zone, npc, item_id)\n);\nCREATE TABLE IF NOT EXISTS flags (\n    character TEXT NOT NULL, name TEXT NOT NULL, value INTEGER NOT NULL,\n    PRIMARY KEY (character, name)\n);\nCREATE TABLE IF NOT EXISTS soulbind (\n    character TEXT PRIMARY KEY, zone TEXT NOT NULL\n);\nCREATE TABLE IF NOT EXISTS tutorial (\n    character TEXT PRIMARY KEY\n);\nCREATE TABLE IF NOT EXISTS corpses (\n    character TEXT NOT NULL, corpse_id INTEGER NOT NULL,\n    zone TEXT NOT NULL, x REAL NOT NULL, y REAL NOT NULL, z REAL NOT NULL,\n    collected INTEGER NOT NULL DEFAULT 0,\n    PRIMARY KEY (character, corpse_id)\n);\nCREATE TABLE IF NOT EXISTS goals (\n    character TEXT NOT NULL, position INTEGER NOT NULL,\n    item_id INTEGER NOT NULL, count INTEGER NOT NULL,\n    PRIMARY KEY (character, position)\n);\nCREATE TABLE IF NOT EXISTS actions (\n    character TEXT NOT NULL, position INTEGER NOT NULL,\n    kind TEXT NOT NULL, source TEXT NOT NULL,\n    zone TEXT NOT NULL, priority INTEGER NOT NULL DEFAULT 0,\n    durable INTEGER NOT NULL DEFAULT 0, payload TEXT NOT NULL DEFAULT '{}',\n    resolved INTEGER NOT NULL DEFAULT 0,\n    PRIMARY KEY (character, position)\n);\nCREATE TABLE IF NOT EXISTS bot_worn (\n    character TEXT NOT NULL, bot_name TEXT NOT NULL, slot INTEGER NOT NULL, item_id INTEGER NOT NULL,\n    PRIMARY KEY (character, bot_name, slot)\n);\nCREATE TABLE IF NOT EXISTS bot_settings (\n    character TEXT NOT NULL, bot_name TEXT NOT NULL, kind TEXT NOT NULL, value TEXT NOT NULL,\n    PRIMARY KEY (character, bot_name, kind)\n);\nCREATE TABLE IF NOT EXISTS bots (\n    character TEXT NOT NULL, bot_name TEXT NOT NULL, class_id INTEGER NOT NULL DEFAULT 0,\n    PRIMARY KEY (character, bot_name)\n);\nCREATE TABLE IF NOT EXISTS sell_marks (\n    character TEXT NOT NULL, item_id INTEGER NOT NULL,\n    PRIMARY KEY (character, item_id)\n);\n"

class Journal:
    DEFAULT_PATH = DEFAULT_PATH

    def __init__(self, path: str | os.PathLike | None = None) -> None:
        chosen = str(path or os.environ.get('EQEMU_JOURNAL_V3', DEFAULT_PATH))
        if Path(chosen).name in {'journal.sqlite', 'journal-v2.sqlite'}:
            raise ValueError('v3 journal does not open the v1 or v2 database')
        if chosen != ':memory:':
            Path(chosen).parent.mkdir(parents=True, exist_ok=True)
        self.path = chosen
        self._db = sqlite3.connect(chosen, timeout=5.0)
        if chosen != ':memory:':
            self._db.execute('PRAGMA journal_mode=WAL')
        self._db.executescript(_SCHEMA)
        self._db.commit()

    def close(self) -> None:
        self._db.close()

    def remember_say(self, character: str, zone: str, npc: str, text: str) -> None:
        self._db.execute('INSERT OR IGNORE INTO says (character, zone, npc, text) VALUES (?, ?, ?, ?)', (character, zone, npc, text))
        self._db.commit()

    def said(self, character: str, zone: str) -> set[tuple[str, str]]:
        rows = self._db.execute('SELECT npc, text FROM says WHERE character = ? AND zone = ?', (character, zone))
        return {(npc, text) for npc, text in rows}

    def remember_handin(self, character: str, zone: str, npc: str, item_id: int, count: int=1) -> None:
        self._db.execute('INSERT INTO handins (character, zone, npc, item_id, count) VALUES (?, ?, ?, ?, ?) ON CONFLICT(character, zone, npc, item_id) DO UPDATE SET count = excluded.count', (character, zone, npc, int(item_id), int(count)))
        self._db.commit()

    def set_flag(self, character: str, name: str, value: int) -> None:
        self._db.execute('INSERT INTO flags (character, name, value) VALUES (?, ?, ?) ON CONFLICT(character, name) DO UPDATE SET value = excluded.value', (character, name, int(value)))
        self._db.commit()

    def flag_values(self, character: str) -> dict[str, int]:
        rows = self._db.execute('SELECT name, value FROM flags WHERE character = ?', (character,))
        return {name: int(value) for name, value in rows}

    def soulbind_zone(self, character: str) -> str:
        row = self._db.execute('SELECT zone FROM soulbind WHERE character = ?', (character,)).fetchone()
        return '' if row is None else str(row[0])

    def set_soulbind(self, character: str, zone: str) -> None:
        self._db.execute('INSERT INTO soulbind (character, zone) VALUES (?, ?) ON CONFLICT(character) DO UPDATE SET zone = excluded.zone', (character, zone))
        self._db.commit()

    def clear_actions(self, character: str) -> int:
        """Drop the queue, open and resolved, for this character."""
        cur = self._db.execute('DELETE FROM actions WHERE character = ?', (character,))
        self._db.commit()
        return int(cur.rowcount)

    def clear_goals(self, character: str) -> int:
        cur = self._db.execute('DELETE FROM goals WHERE character = ?', (character,))
        self._db.commit()
        return int(cur.rowcount)

    def clear_tutorial(self, character: str) -> int:
        cur = self._db.execute('DELETE FROM tutorial WHERE character = ?', (character,))
        self._db.commit()
        return int(cur.rowcount)

    def mark_tutorial_done(self, character: str) -> None:
        self._db.execute('INSERT OR IGNORE INTO tutorial (character) VALUES (?)', (character,))
        self._db.commit()

    def tutorial_done(self, character: str) -> bool:
        row = self._db.execute('SELECT 1 FROM tutorial WHERE character = ?', (character,)).fetchone()
        return row is not None

    def remember_corpse(self, character: str, corpse_id: int, zone: str, x: float, y: float, z: float) -> None:
        self._db.execute('INSERT INTO corpses (character, corpse_id, zone, x, y, z, collected) VALUES (?, ?, ?, ?, ?, ?, 0) ON CONFLICT(character, corpse_id) DO UPDATE SET zone = excluded.zone, x = excluded.x, y = excluded.y, z = excluded.z', (character, int(corpse_id), zone, float(x), float(y), float(z)))
        self._db.commit()

    def open_corpse(self, character: str) -> tuple[int, str, float, float, float] | None:
        row = self._db.execute('SELECT corpse_id, zone, x, y, z FROM corpses WHERE character = ? AND collected = 0 ORDER BY corpse_id LIMIT 1', (character,)).fetchone()
        if row is None:
            return None
        corpse_id, zone, x, y, z = row
        return (int(corpse_id), str(zone), float(x), float(y), float(z))

    def collect_corpse(self, character: str, corpse_id: int) -> bool:
        cur = self._db.execute('UPDATE corpses SET collected = 1 WHERE character = ? AND corpse_id = ? AND collected = 0', (character, int(corpse_id)))
        self._db.commit()
        return cur.rowcount > 0

    def save_goals(self, character: str, goals: list[tuple[int, int]]) -> None:
        self._db.execute('DELETE FROM goals WHERE character = ?', (character,))
        self._db.executemany('INSERT INTO goals (character, position, item_id, count) VALUES (?, ?, ?, ?)', [(character, index, int(item_id), int(count)) for index, (item_id, count) in enumerate(goals)])
        self._db.commit()

    def load_goals(self, character: str) -> list[tuple[int, int]]:
        rows = self._db.execute('SELECT item_id, count FROM goals WHERE character = ? ORDER BY position', (character,))
        return [(int(item_id), int(count)) for item_id, count in rows]

    def push_goal(self, character: str, item_id: int, count: int) -> None:
        goals = self.load_goals(character)
        goals.append((int(item_id), int(count)))
        self.save_goals(character, goals)

    def pop_goal(self, character: str) -> tuple[int, int] | None:
        goals = self.load_goals(character)
        if not goals:
            return None
        top = goals.pop()
        self.save_goals(character, goals)
        return top

    def open_action(self, character: str, action: Action) -> bool:
        """Insert one open row. A resolved or already-open source is not written again."""
        source = str(action.source or '')
        if not source:
            return False
        if self.is_resolved(character, source) or self.is_open(character, source):
            return False
        self._insert(character, action, resolved=0)
        return True

    def load_actions(self, character: str) -> list[Action]:
        """Open rows only, in journal order. A resolved source is not reloaded."""
        rows = self._db.execute('SELECT kind, source, zone, priority, durable, payload FROM actions WHERE character = ? AND resolved = 0 ORDER BY position', (character,))
        return [_rehydrate(*row) for row in rows]

    def is_open(self, character: str, source: str) -> bool:
        if not source:
            return False
        row = self._db.execute('SELECT 1 FROM actions WHERE character = ? AND source = ? AND resolved = 0 LIMIT 1', (character, source)).fetchone()
        return row is not None

    def resolved(self, character: str, source: str) -> bool:
        return self.is_resolved(character, source)

    def is_resolved(self, character: str, source: str) -> bool:
        if not source:
            return False
        row = self._db.execute('SELECT 1 FROM actions WHERE character = ? AND source = ? AND resolved = 1 LIMIT 1', (character, source)).fetchone()
        return row is not None

    def resolved_sources(self, character: str) -> set[str]:
        rows = self._db.execute('SELECT source FROM actions WHERE character = ? AND resolved = 1', (character,))
        return {str(source) for source, in rows}

    def resolve_action(self, character: str, action: Action) -> None:
        """Mark the source resolved. A missing row is inserted already resolved."""
        source = str(action.source or '')
        if not source:
            return
        found = self._db.execute('SELECT 1 FROM actions WHERE character = ? AND source = ? LIMIT 1', (character, source)).fetchone()
        if found is not None:
            self._db.execute('UPDATE actions SET resolved = 1 WHERE character = ? AND source = ?', (character, source))
            self._db.commit()
            return
        self._insert(character, action, resolved=1)

    def clear_source(self, character: str, source: str) -> None:
        """Delete the source. It is neither open nor resolved, so it can be appended again."""
        if not source:
            return
        self._db.execute('DELETE FROM actions WHERE character = ? AND source = ?', (character, source))
        self._db.commit()

    def set_worn(self, character: str, bot_name: str, slot: int, item_id: int) -> None:
        self._db.execute('INSERT INTO bot_worn (character, bot_name, slot, item_id) VALUES (?, ?, ?, ?) ON CONFLICT(character, bot_name, slot) DO UPDATE SET item_id = excluded.item_id', (character, bot_name, int(slot), int(item_id)))
        self._db.commit()

    def worn(self, character: str, bot_name: str) -> dict[int, int]:
        rows = self._db.execute('SELECT slot, item_id FROM bot_worn WHERE character = ? AND bot_name = ? ORDER BY slot', (character, bot_name))
        return {int(slot): int(item_id) for slot, item_id in rows}

    def remember_bot(self, character: str, bot_name: str, class_id: int=0) -> None:
        self._db.execute('INSERT INTO bots (character, bot_name, class_id) VALUES (?, ?, ?) ON CONFLICT(character, bot_name) DO UPDATE SET class_id = excluded.class_id', (character, bot_name, int(class_id)))
        self._db.commit()

    def bots(self, character: str) -> list[tuple[str, int]]:
        rows = self._db.execute('SELECT bot_name, class_id FROM bots WHERE character = ? ORDER BY bot_name', (character,))
        return [(str(name), int(class_id)) for name, class_id in rows]

    def forget_bot(self, character: str, bot_name: str) -> None:
        self._db.execute('DELETE FROM bots WHERE character = ? AND bot_name = ?', (character, bot_name))
        self._db.commit()

    def set_bot_setting(self, character: str, bot_name: str, kind: str, value: str) -> None:
        self._db.execute('INSERT INTO bot_settings (character, bot_name, kind, value) VALUES (?, ?, ?, ?) ON CONFLICT(character, bot_name, kind) DO UPDATE SET value = excluded.value', (character, bot_name, kind, value))
        self._db.commit()

    def bot_settings(self, character: str) -> dict[str, dict[str, str]]:
        rows = self._db.execute('SELECT bot_name, kind, value FROM bot_settings WHERE character = ?', (character,))
        found: dict[str, dict[str, str]] = {}
        for name, kind, value in rows:
            found.setdefault(str(name), {})[str(kind)] = str(value)
        return found

    def mark_sell(self, character: str, item_id: int) -> None:
        self._db.execute('INSERT OR IGNORE INTO sell_marks (character, item_id) VALUES (?, ?)', (character, int(item_id)))
        self._db.commit()

    def clear_sell(self, character: str, item_id: int) -> None:
        self._db.execute('DELETE FROM sell_marks WHERE character = ? AND item_id = ?', (character, int(item_id)))
        self._db.commit()

    def sell_marks(self, character: str) -> set[int]:
        rows = self._db.execute('SELECT item_id FROM sell_marks WHERE character = ?', (character,))
        return {int(item_id) for item_id, in rows}

    def recent_fetch_ids(self, character: str, limit: int = 20) -> list[int]:
        """Newest fetch item ids, including ones already resolved."""
        rows = self._db.execute("SELECT payload FROM actions WHERE character = ? AND kind LIKE '%:Fetch' ORDER BY position DESC", (character,))
        found: list[int] = []
        seen: set[int] = set()
        for (payload,) in rows:
            try:
                data = json.loads(payload or '{}')
            except json.JSONDecodeError:
                continue
            item_id = int((data or {}).get('item_id') or 0) if isinstance(data, dict) else 0
            if item_id <= 0 or item_id in seen:
                continue
            seen.add(item_id)
            found.append(item_id)
            if len(found) >= limit:
                break
        return found

    def _insert(self, character: str, action: Action, *, resolved: int) -> None:
        position = self._db.execute('SELECT COALESCE(MAX(position), -1) + 1 FROM actions WHERE character = ?', (character,)).fetchone()
        self._db.execute('INSERT INTO actions (character, position, kind, source, zone, priority, durable, payload, resolved) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', (character, int(position[0]), _kind(action), str(action.source), str(action.zone or ''), int(action.priority), 1 if action.durable else 0, _payload(action), int(resolved)))
        self._db.commit()

def _kind(action: Action) -> str:
    cls = type(action)
    return f'{cls.__module__}:{cls.__qualname__}'

def _payload(action: Action) -> str:
    """Every field on the action, except the columns and the live mailbox."""
    raw: dict[str, object] = {}
    seen: set[int] = set()
    for key, value in action.__dict__.items():
        if key in _SKIP or key.startswith('_'):
            continue
        try:
            raw[key] = _encode(value, seen)
        except TypeError as error:
            raise TypeError(f'cannot store {type(action).__name__}.{key}: {error}') from error
    return json.dumps(raw)

def _encode(value: object, seen: set[int]) -> object:
    """JSON, plus tags for tuple, bytes, a non-string map, a set, and a plain object."""
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    mark = id(value)
    if mark in seen:
        raise TypeError('cycle')
    seen.add(mark)
    try:
        if isinstance(value, (bytes, bytearray)):
            return {'$': 'bytes', 'v': base64.b64encode(bytes(value)).decode('ascii')}
        if isinstance(value, tuple):
            return {'$': 'tuple', 'v': [_encode(item, seen) for item in value]}
        if isinstance(value, list):
            return [_encode(item, seen) for item in value]
        if isinstance(value, set):
            return {'$': 'set', 'v': [_encode(item, seen) for item in value]}
        if isinstance(value, dict):
            if all(isinstance(key, str) and (not str(key).startswith('$')) for key in value):
                return {key: _encode(item, seen) for key, item in value.items()}
            return {'$': 'map', 'v': [[_encode(key, seen), _encode(item, seen)] for key, item in value.items()]}
        return _encode_object(value, seen)
    finally:
        seen.discard(mark)

def _encode_object(value: object, seen: set[int]) -> dict[str, object]:
    cls = type(value)
    if isinstance(value, Action):
        raise TypeError('nested action')
    if cls.__module__.startswith(('eqclient3.world', 'eqclient3.loop', 'eqclient3.net', 'eqclient3.nav', 'eqclient3.schedule', 'eqclient3.journal', 'eqclient3.bus')):
        raise TypeError(f'{cls.__module__}.{cls.__qualname__}')
    try:
        state = value.__dict__
    except AttributeError:
        raise TypeError(f'{cls.__module__}.{cls.__qualname__}') from None
    fields: dict[str, object] = {}
    for key, item in state.items():
        if key.startswith('_'):
            continue
        fields[key] = _encode(item, seen)
    return {'$': 'obj', 't': f'{cls.__module__}:{cls.__qualname__}', 'v': fields}

def _load_class(kind: str) -> type:
    module_name, _, qual = kind.partition(':')
    if not qual:
        module_name, _, qual = kind.rpartition('.')
    if not module_name or not qual:
        raise ValueError(kind)
    obj: object = importlib.import_module(module_name)
    for part in qual.split('.'):
        if not part:
            raise ValueError(kind)
        obj = obj.__dict__[part]
    if not isinstance(obj, type):
        raise TypeError(kind)
    return obj

def _kind_class(kind: str) -> type[Action]:
    try:
        cls = _load_class(kind)
    except (ImportError, AttributeError, ValueError, KeyError, TypeError):
        return Action
    if not issubclass(cls, Action):
        return Action
    return cls

def _decode(value: object) -> object:
    if isinstance(value, list):
        return [_decode(item) for item in value]
    if not isinstance(value, dict):
        return value
    tag = value.get('$')
    if tag == 'tuple':
        inner = value['v']
        if not isinstance(inner, list):
            raise TypeError('tuple payload is not a list')
        return tuple(_decode(item) for item in inner)
    if tag == 'bytes':
        return base64.b64decode(str(value['v']))
    if tag == 'set':
        inner = value['v']
        if not isinstance(inner, list):
            raise TypeError('set payload is not a list')
        return {_decode(item) for item in inner}
    if tag == 'map':
        inner = value['v']
        if not isinstance(inner, list):
            raise TypeError('map payload is not a list')
        found: dict[object, object] = {}
        for pair in inner:
            if not isinstance(pair, list) or len(pair) != 2:
                raise TypeError('map entry is not a pair')
            found[_decode(pair[0])] = _decode(pair[1])
        return found
    if tag == 'obj':
        return _decode_object(value)
    return {str(key): _decode(item) for key, item in value.items()}

def _decode_object(value: dict) -> object:
    kind = str(value.get('t') or '')
    cls = _load_class(kind)
    try:
        obj = cls.__new__(cls)
    except TypeError:
        obj = object.__new__(cls)
    fields = value.get('v') or {}
    if not isinstance(fields, dict):
        raise TypeError(f'{kind} fields are not an object')
    try:
        state = obj.__dict__
    except AttributeError:
        raise TypeError(f'{kind} has no fields') from None
    state.update({str(key): _decode(item) for key, item in fields.items()})
    return obj

def _decode_into(action: Action, data: dict) -> None:
    for key, value in data.items():
        if key in _SKIP or str(key).startswith('_'):
            continue
        action.__dict__[key] = _decode(value)

def _wait_list(value: object) -> list[str]:
    """A stored wait used to be one string. Open rows still carry that shape."""
    if isinstance(value, list):
        return [str(item) for item in value if item]
    if isinstance(value, str) and value:
        return [value]
    return []

def _rehydrate(kind: str, source: str, zone: str, priority: int, durable: int, payload: str) -> Action:
    cls = _kind_class(kind)
    action = object.__new__(cls)
    Action.__init__(action)
    data = json.loads(payload or '{}')
    if isinstance(data, dict):
        _decode_into(action, data)
    action.source = str(source or '')
    action.zone = str(zone or '')
    action.priority = int(priority)
    action.durable = bool(durable)
    action.messages = []
    action.active_path = None
    action.waiting = _wait_list(action.waiting)
    action.suspended = True
    action.yielding = False
    action.complete = False
    action.insert = 0
    return action
