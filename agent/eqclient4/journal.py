"""Memory the server will not resend. One directory per character,
~/.eqclient/journal/characters.json lists each character.
~/.eqclient/journal/<character>/journal-v3.sqlite3 holds that character's rows.
Pickled actions stay in the database. Two characters do not share a lock.
Open action rows reload onto the queue. A resolved source is not appended again.
Death clears a removed source so it is neither open nor resolved.
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient4.world import World

import json
import os
import pickle
import sqlite3
from pathlib import Path

from eqclient4.action import Action
from eqclient4.log import log

JOURNAL_ROOT = Path.home() / ".eqclient" / "journal"
JOURNAL_ROOT.mkdir(parents=True, exist_ok=True)
DB_NAME = "journal-v4.sqlite3"
catalog = JOURNAL_ROOT / "characters.json"


def characters() -> dict[str, dict[str, str]]:
    if not catalog.is_file():
        return {}
    with catalog.open() as handle:
        return json.load(handle)


_SCHEMA = """
CREATE TABLE IF NOT EXISTS says (
    character TEXT NOT NULL, 
    zone TEXT NOT NULL, 
    npc TEXT NOT NULL, 
    text TEXT NOT NULL,
    PRIMARY KEY (character, zone, npc, text)
);

CREATE TABLE IF NOT EXISTS handins (
    character TEXT NOT NULL, 
    zone TEXT NOT NULL, 
    npc TEXT NOT NULL,
    item_id INTEGER NOT NULL, 
    count INTEGER NOT NULL,
    PRIMARY KEY (character, zone, npc, item_id)
);

CREATE TABLE IF NOT EXISTS flags (
    character TEXT NOT NULL, 
    name TEXT NOT NULL, 
    value INTEGER NOT NULL,
    PRIMARY KEY (character, name)
);

CREATE TABLE IF NOT EXISTS soulbind (
    character TEXT PRIMARY KEY, 
    zone TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS tutorial (
    character TEXT PRIMARY KEY    
);

CREATE TABLE IF NOT EXISTS corpses (
    character TEXT NOT NULL, 
    corpse_id INTEGER NOT NULL,
    zone TEXT NOT NULL, 
    x REAL NOT NULL, 
    y REAL NOT NULL, 
    z REAL NOT NULL,
    collected INTEGER NOT NULL DEFAULT 0,
    PRIMARY KEY (character, corpse_id)
);

CREATE TABLE IF NOT EXISTS goals (
    character TEXT NOT NULL, 
    position INTEGER NOT NULL,
    item_id INTEGER NOT NULL,
    count INTEGER NOT NULL,
    PRIMARY KEY (character, position)
);

CREATE TABLE IF NOT EXISTS actions (
    character TEXT NOT NULL, 
    position INTEGER NOT NULL,
    kind TEXT NOT NULL, 
    source TEXT NOT NULL,
    zone TEXT NOT NULL, 
    priority INTEGER NOT NULL DEFAULT 0,
    durable INTEGER NOT NULL DEFAULT 0, 
    payload TEXT NOT NULL DEFAULT '{}',
    resolved INTEGER NOT NULL DEFAULT 0,
    PRIMARY KEY (character, position)
);

CREATE TABLE IF NOT EXISTS bot_worn (
    character TEXT NOT NULL, 
    bot_name TEXT NOT NULL, 
    slot INTEGER NOT NULL, 
    item_id INTEGER NOT NULL,
    PRIMARY KEY (character, bot_name, slot)
);

CREATE TABLE IF NOT EXISTS bot_settings (
    character TEXT NOT NULL, 
    bot_name TEXT NOT NULL, 
    kind TEXT NOT NULL, 
    value TEXT NOT NULL,
    PRIMARY KEY (character, bot_name, kind)
);

CREATE TABLE IF NOT EXISTS bots (
    character TEXT NOT NULL, 
    bot_name TEXT NOT NULL, 
    class_id INTEGER NOT NULL DEFAULT 0,
    PRIMARY KEY (character, bot_name)
);

CREATE TABLE IF NOT EXISTS sell_marks (
    character TEXT NOT NULL,
    item_id INTEGER NOT NULL,
    PRIMARY KEY (character, item_id)
);

CREATE TABLE IF NOT EXISTS book_texts (
    character TEXT NOT NULL,
    book_id INTEGER NOT NULL,
    text TEXT NOT NULL,
    PRIMARY KEY (character, book_id)
);

"""


class Journal:

    def __init__(self, character: str, world: World, path: str | os.PathLike | None = None) -> None:
        self.character = character
        self.db_path = path or os.environ.get("EQEMU_JOURNAL_V3")
        self.world = world
        if not self.db_path:
            found = characters()
            if character not in found:
                found[character] = {"database": f"{JOURNAL_ROOT }/{character}/{DB_NAME}"}
                with catalog.open("w") as handle:
                    json.dump(found, handle, indent=2)
                    handle.write("\n")
            self.db_path = JOURNAL_ROOT / found[character]["database"]

        if self.db_path != ":memory:":
            Path(self.db_path).parent.mkdir(parents=True, exist_ok=True)

        self._db = sqlite3.connect(self.db_path, timeout=5.0)
        if self.db_path != ":memory:":
            self._db.execute("PRAGMA journal_mode=WAL")

        self._db.executescript(_SCHEMA)
        self._db.commit()
        self._drop_ephemeral()

    def close(self) -> None:
        self._db.close()

    def remember_say(self, zone: str, npc: str, text: str) -> None:
        self._db.execute(
            "INSERT OR IGNORE INTO says (character, zone, npc, text) VALUES (?, ?, ?, ?)",
            (self.character, zone, npc, text),
        )
        self._db.commit()

    def said(self, zone: str) -> set[tuple[str, str]]:
        rows = self._db.execute(
            "SELECT npc, text FROM says WHERE character = ? AND zone = ?",
            (self.character, zone),
        )
        return {(npc, text) for npc, text in rows}

    def remember_handin(self, zone: str, npc: str, item_id: int, count: int = 1) -> None:
        self._db.execute(
            "INSERT INTO handins (character, zone, npc, item_id, count) VALUES (?, ?, ?, ?, ?) ON CONFLICT(character, zone, npc, item_id) DO UPDATE SET count = excluded.count",
            (self.character, zone, npc, int(item_id), int(count)),
        )
        self._db.commit()

    def set_flag(self, name: str, value: int) -> None:
        self._db.execute(
            "INSERT INTO flags (character, name, value) VALUES (?, ?, ?) ON CONFLICT(character, name) DO UPDATE SET value = excluded.value",
            (self.character, name, int(value)),
        )
        self._db.commit()

    def delete_flag(self, name: str) -> None:
        self._db.execute(
            "DELETE FROM flags WHERE character = ? AND name = ?",
            (self.character, name),
        )
        self._db.commit()

    def get_flag(self, name: str) -> int | None:
        row = self._db.execute(
            "SELECT value FROM flags WHERE character = ? AND name = ?", (self.character, name)
        ).fetchone()
        if not row:
            return None
        return int(row[0])

    def flag_values(self) -> dict[str, int]:
        rows = self._db.execute(
            "SELECT name, value FROM flags WHERE character = ?", (self.character,)
        )
        return {name: int(value) for name, value in rows}

    def soulbind_zone(self) -> str:
        row = self._db.execute(
            "SELECT zone FROM soulbind WHERE character = ?", (self.character,)
        ).fetchone()
        return "" if row is None else str(row[0])

    def set_soulbind(self, zone: str) -> None:
        self._db.execute(
            "INSERT INTO soulbind (character, zone) VALUES (?, ?) ON CONFLICT(character) DO UPDATE SET zone = excluded.zone",
            (self.character, zone),
        )
        self._db.commit()

    def clear_actions(self) -> int:
        """Drop the queue, open and resolved, for this character."""
        cur = self._db.execute("DELETE FROM actions WHERE character = ?", (self.character,))
        self._db.commit()
        return int(cur.rowcount)

    def clear_goals(self) -> int:
        cur = self._db.execute("DELETE FROM goals WHERE character = ?", (self.character,))
        self._db.commit()
        return int(cur.rowcount)

    def remember_corpse(self, corpse_id: int, zone: str, x: float, y: float, z: float) -> None:
        self._db.execute(
            "INSERT INTO corpses (character, corpse_id, zone, x, y, z, collected) VALUES (?, ?, ?, ?, ?, ?, 0) ON CONFLICT(character, corpse_id) DO UPDATE SET zone = excluded.zone, x = excluded.x, y = excluded.y, z = excluded.z",
            (self.character, int(corpse_id), zone, float(x), float(y), float(z)),
        )
        self._db.commit()

    def open_corpse(self) -> tuple[int, str, float, float, float] | None:
        row = self._db.execute(
            "SELECT corpse_id, zone, x, y, z FROM corpses WHERE character = ? AND collected = 0 ORDER BY corpse_id LIMIT 1",
            (self.character,),
        ).fetchone()
        if row is None:
            return None
        corpse_id, zone, x, y, z = row
        return (int(corpse_id), str(zone), float(x), float(y), float(z))

    def collect_corpse(self, corpse_id: int) -> bool:
        cur = self._db.execute(
            "UPDATE corpses SET collected = 1 WHERE character = ? AND corpse_id = ? AND collected = 0",
            (self.character, int(corpse_id)),
        )
        self._db.commit()
        return cur.rowcount > 0

    def save_goals(self, goals: list[tuple[int, int]]) -> None:
        self._db.execute("DELETE FROM goals WHERE character = ?", (self.character,))
        self._db.executemany(
            "INSERT INTO goals (character, position, item_id, count) VALUES (?, ?, ?, ?)",
            [
                (self.character, index, int(item_id), int(count))
                for index, (item_id, count) in enumerate(goals)
            ],
        )
        self._db.commit()

    def load_goals(self) -> list[tuple[int, int]]:
        rows = self._db.execute(
            "SELECT item_id, count FROM goals WHERE character = ? ORDER BY position",
            (self.character,),
        )
        return [(int(item_id), int(count)) for item_id, count in rows]

    def push_goal(self, item_id: int, count: int) -> None:
        goals = self.load_goals()
        goals.append((int(item_id), int(count)))
        self.save_goals(goals)

    def pop_goal(self) -> tuple[int, int] | None:
        goals = self.load_goals()
        if not goals:
            return None
        top = goals.pop()
        self.save_goals(goals)
        return top

    def _drop_ephemeral(self) -> None:
        """Drop open actions that are not durable, and rows whose pickle will not open.

        A resolved source stays, so it is not appended again. An open Zone is
        dropped too: the server wipes a zone request on disconnect.
        """
        self._db.execute("DELETE FROM actions WHERE durable = 0 AND resolved = 0")
        self._db.execute(
            "DELETE FROM actions WHERE resolved = 0 AND kind = 'eqclient3.actions.zone:Zone'"
        )
        rows = list(self._db.execute("SELECT character, position, payload FROM actions"))
        for character, position, payload in rows:
            if self._thaw(payload) is None:
                log.error("ephemeral action failed to load, dropping from database", exc_info=True)
                self._db.execute(
                    "DELETE FROM actions WHERE character = ? AND position = ?",
                    (character, position),
                )
        self._db.commit()

    def open_action(self, action: Action) -> bool:
        """Insert one open durable row. A resolved or already-open source is not written again.

        An action that is not durable is left off the journal. The caller may still run it.
        """
        source = str(action.source or "")
        if not source:
            return False
        if not action.durable:
            return True
        if self.is_resolved(source) or self.is_open(source):
            return False
        self._insert(action, resolved=0)
        return True

    def load_actions(self) -> list[Action]:
        """Open durable rows, in journal order. A resolved source is not reloaded."""
        rows = self._db.execute(
            "SELECT position, source, zone, priority, durable, payload FROM actions WHERE character = ? AND resolved = 0 AND durable = 1 ORDER BY position",
            (self.character,),
        )
        found: list[Action] = []
        for position, source, zone, priority, durable, payload in rows:
            action = self._thaw(payload)
            if action is None:
                self._db.execute(
                    "DELETE FROM actions WHERE character = ? AND position = ?",
                    (self.character, position),
                )
                self._db.commit()
                continue
            action.source = str(source or "")
            action.zone = str(zone or "")
            action.priority = int(priority)
            action.durable = bool(durable)
            found.append(action)
        return found

    def is_open(self, source: str) -> bool:
        if not source:
            return False
        row = self._db.execute(
            "SELECT 1 FROM actions WHERE character = ? AND source = ? AND resolved = 0 AND durable = 1 LIMIT 1",
            (self.character, source),
        ).fetchone()
        return row is not None

    def resolved(self, source: str) -> bool:
        return self.is_resolved(source)

    def is_resolved(self, source: str) -> bool:
        if not source:
            return False
        row = self._db.execute(
            "SELECT 1 FROM actions WHERE character = ? AND source = ? AND resolved = 1 LIMIT 1",
            (self.character, source),
        ).fetchone()
        return row is not None

    def resolved_sources(self) -> set[str]:
        rows = self._db.execute(
            "SELECT source FROM actions WHERE character = ? AND resolved = 1",
            (self.character,),
        )
        return {str(source) for source, in rows}

    def resolve_action(self, action: Action) -> None:
        """Mark the source resolved. A missing row is inserted already resolved."""
        source = str(action.source or "")
        if not source:
            return
        found = self._db.execute(
            "SELECT 1 FROM actions WHERE character = ? AND source = ? LIMIT 1",
            (self.character, source),
        ).fetchone()
        if found is not None:
            self._db.execute(
                "UPDATE actions SET resolved = 1 WHERE character = ? AND source = ?",
                (self.character, source),
            )
            self._db.commit()
            return
        self._insert(action, resolved=1)

    def clear_source(self, source: str) -> None:
        """Delete the source. It is neither open nor resolved, so it can be appended again."""
        if not source:
            return
        self._db.execute(
            "DELETE FROM actions WHERE character = ? AND source = ?",
            (self.character, source),
        )
        self._db.commit()

    def remember_bot(self, bot_name: str, class_id: int = 0) -> None:
        self._db.execute(
            "INSERT INTO bots (character, bot_name, class_id) VALUES (?, ?, ?) ON CONFLICT(character, bot_name) DO UPDATE SET class_id = excluded.class_id",
            (self.character, bot_name, int(class_id)),
        )
        self._db.commit()

    def bots(self) -> list[tuple[str, int]]:
        rows = self._db.execute(
            "SELECT bot_name, class_id FROM bots WHERE character = ? ORDER BY bot_name",
            (self.character,),
        )
        return [(str(name), int(class_id)) for name, class_id in rows]

    def forget_bot(self, bot_name: str) -> None:
        self._db.execute(
            "DELETE FROM bots WHERE character = ? AND bot_name = ?",
            (self.character, bot_name),
        )
        self._db.commit()

    def set_bot_setting(self, bot_name: str, kind: str, value: str) -> None:
        self._db.execute(
            "INSERT INTO bot_settings (character, bot_name, kind, value) VALUES (?, ?, ?, ?) ON CONFLICT(character, bot_name, kind) DO UPDATE SET value = excluded.value",
            (self.character, bot_name, kind, value),
        )
        self._db.commit()

    def bot_settings(self) -> dict[str, dict[str, str]]:
        rows = self._db.execute(
            "SELECT bot_name, kind, value FROM bot_settings WHERE character = ?",
            (self.character,),
        )
        found: dict[str, dict[str, str]] = {}
        for name, kind, value in rows:
            found.setdefault(str(name), {})[str(kind)] = str(value)
        return found

    def mark_sell(self, item_id: int) -> None:
        self._db.execute(
            "INSERT OR IGNORE INTO sell_marks (character, item_id) VALUES (?, ?)",
            (self.character, int(item_id)),
        )
        self._db.commit()

    def clear_sell(self, item_id: int) -> None:
        self._db.execute(
            "DELETE FROM sell_marks WHERE character = ? AND item_id = ?",
            (self.character, int(item_id)),
        )
        self._db.commit()

    def sell_marks(self) -> set[int]:
        rows = self._db.execute(
            "SELECT item_id FROM sell_marks WHERE character = ?", (self.character,)
        )
        return {int(item_id) for item_id, in rows}

    def recent_fetch_ids(self, limit: int = 20) -> list[int]:
        """Newest fetch item ids, including ones already resolved."""
        rows = self._db.execute(
            "SELECT payload FROM actions WHERE character = ? AND kind LIKE '%:Fetch' AND durable = 1 ORDER BY position DESC",
            (self.character,),
        )
        found: list[int] = []
        seen: set[int] = set()
        for (payload,) in rows:
            action = self._thaw(payload)
            if action is None:
                continue
            item_id = int(getattr(action, "item_id", 0) or 0)
            if item_id <= 0 or item_id in seen:
                continue
            seen.add(item_id)
            found.append(item_id)
            if len(found) >= limit:
                break
        return found

    def _insert(self, action: Action, *, resolved: int) -> None:
        position = self._db.execute(
            "SELECT COALESCE(MAX(position), -1) + 1 FROM actions WHERE character = ?",
            (self.character,),
        ).fetchone()
        self._db.execute(
            "INSERT INTO actions (character, position, kind, source, zone, priority, durable, payload, resolved) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (
                self.character,
                int(position[0]),
                _kind(action),
                str(action.source),
                str(action.zone or ""),
                int(action.priority),
                1 if action.durable else 0,
                _dump(action),
                int(resolved),
            ),
        )
        self._db.commit()

    def _thaw(self, payload: object) -> Action | None:
        if isinstance(payload, memoryview):
            payload = payload.tobytes()
        if not isinstance(payload, (bytes, bytearray)) or not payload:
            return None
        try:
            action = pickle.loads(bytes(payload))
        except (
            pickle.UnpicklingError,
            EOFError,
            AttributeError,
            ImportError,
            ModuleNotFoundError,
            TypeError,
            ValueError,
        ):
            log.error("saved action failed to load", exc_info=True)
            return None
        if not isinstance(action, Action):
            return None
        action.messages = []
        action.active_path = None
        action._world = self.world
        action.suspended = True
        action.yielding = False
        action.complete = False
        return action


def _kind(action: Action) -> str:
    cls = type(action)
    return f"{cls.__module__}:{cls.__qualname__}"


_HELD = ("messages", "active_path", "_world")


def _dump(action: Action) -> bytes:
    """Pickle the action. The live mailbox, path, and world stay on the running object."""
    held: dict[str, object] = {}
    for key in _HELD:
        if key in action.__dict__:
            held[key] = action.__dict__.pop(key)
    try:
        return pickle.dumps(action, protocol=pickle.HIGHEST_PROTOCOL)
    finally:
        action.__dict__.update(held)
