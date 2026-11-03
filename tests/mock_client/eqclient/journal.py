"""SQLite memory of quest triggers this character has already fired.

A script can hail, then ask for a keyword, then take an item. The task packets
remember kills and deliveries. They do not remember which line was said, so the
next session would hail again and never reach the later trigger.
"""

from __future__ import annotations

import sqlite3
import time
from pathlib import Path

from eqclient.zones import KNOWN, remember


class Journal:
    def __init__(self, path: str) -> None:
        if path != ":memory:":
            Path(path).parent.mkdir(parents=True, exist_ok=True)
        self._db = sqlite3.connect(path, timeout=5.0)
        if path != ":memory:":
            self._db.execute("PRAGMA journal_mode=WAL")
        self._db.execute("""
            CREATE TABLE IF NOT EXISTS zones (
                name TEXT PRIMARY KEY,
                zone_id INTEGER NOT NULL
            )
            """)
        self._db.execute("""
            CREATE TABLE IF NOT EXISTS events (
                character TEXT NOT NULL,
                zone TEXT NOT NULL,
                npc TEXT NOT NULL,
                kind TEXT NOT NULL,
                detail TEXT NOT NULL,
                created TEXT NOT NULL DEFAULT (datetime('now')),
                PRIMARY KEY (character, zone, npc, kind, detail)
            )
            """)
        self._db.commit()
        for name, zone_id in self._db.execute("SELECT name, zone_id FROM zones"):
            remember(name, zone_id)

    def remember_zone(self, name: str, zone_id: int) -> None:
        """A short name and the id from the zone we just entered."""
        short = (name or "").lower()
        remember(short, zone_id)
        if short not in KNOWN:
            return
        self._db.execute(
            "INSERT INTO zones (name, zone_id) VALUES (?, ?) ON CONFLICT(name) DO UPDATE SET zone_id = excluded.zone_id",
            (short, int(zone_id)),
        )
        self._db.commit()

    def zones(self) -> dict[str, int]:
        rows = self._db.execute("SELECT name, zone_id FROM zones").fetchall()
        return {name: zone_id for name, zone_id in rows}

    def record(self, character: str, zone: str, npc: str, kind: str, detail: str) -> None:
        self._db.execute(
            "INSERT OR IGNORE INTO events (character, zone, npc, kind, detail) VALUES (?, ?, ?, ?, ?)",
            (character, zone, npc, kind, detail),
        )
        self._db.commit()

    def has(self, character: str, zone: str, npc: str, kind: str, detail: str) -> bool:
        row = self._db.execute(
            "SELECT 1 FROM events WHERE character = ? AND zone = ? AND npc = ? AND kind = ? AND detail = ?",
            (character, zone, npc, kind, detail),
        ).fetchone()
        return row is not None

    def triggers(self, character: str, zone: str, npc: str) -> list[tuple[str, str]]:
        """Kind and detail, in the order they were first recorded."""
        rows = self._db.execute(
            "SELECT kind, detail FROM events WHERE character = ? AND zone = ? AND npc = ? ORDER BY rowid",
            (character, zone, npc),
        ).fetchall()
        return [(kind, detail) for kind, detail in rows]

    def said_everywhere(self, character: str) -> set[tuple[str, str, str]]:
        """Zone, npc, and word for every say, so a chain started in another zone still counts."""
        rows = self._db.execute(
            "SELECT zone, npc, detail FROM events WHERE character = ? AND kind = 'say'",
            (character,),
        ).fetchall()
        return {(zone, npc, detail.lower()) for zone, npc, detail in rows}

    def said(self, character: str, zone: str) -> set[tuple[str, str]]:
        rows = self._db.execute(
            "SELECT npc, detail FROM events WHERE character = ? AND zone = ? AND kind = 'say'",
            (character, zone),
        ).fetchall()
        return {(npc, detail) for npc, detail in rows}

    def handed(self, character: str, zone: str) -> set[tuple[str, str]]:
        rows = self._db.execute(
            "SELECT npc, detail FROM events WHERE character = ? AND zone = ? AND kind = 'handin'",
            (character, zone),
        ).fetchall()
        return {(npc, detail) for npc, detail in rows}

    def hubs(self, character: str, zone: str) -> set[str]:
        rows = self._db.execute(
            "SELECT npc FROM events WHERE character = ? AND zone = ? AND kind = 'hub'",
            (character, zone),
        ).fetchall()
        return {npc for (npc,) in rows}

    def set_flag(self, character: str, name: str, value: int) -> None:
        """Record a qglobal-style flag from a server-visible signal. detail is name=value."""
        key = f"{name}={int(value)}"
        # Drop older values for the same flag name so flag_values stays current.
        rows = self._db.execute(
            "SELECT detail FROM events WHERE character = ? AND kind = 'flag' AND detail LIKE ?",
            (character, f"{name}=%"),
        ).fetchall()
        for (detail,) in rows:
            self._db.execute(
                "DELETE FROM events WHERE character = ? AND kind = 'flag' AND detail = ?",
                (character, detail),
            )
        self._db.execute(
            "INSERT OR IGNORE INTO events (character, zone, npc, kind, detail) VALUES (?, ?, ?, ?, ?)",
            (character, "", name, "flag", key),
        )
        self._db.commit()

    def set_soulbind(self, character: str, zone: str) -> None:
        """Remember the zone we last soulbound at — one current bind per character."""
        short = (zone or "").lower().strip()
        if not short:
            return
        self._db.execute(
            "DELETE FROM events WHERE character = ? AND kind = 'soulbind' AND npc = 'current'",
            (character,),
        )
        self._db.execute(
            "INSERT OR IGNORE INTO events (character, zone, npc, kind, detail) VALUES (?, ?, ?, ?, ?)",
            (character, short, "current", "soulbind", short),
        )
        self._db.commit()

    def soulbind_zone(self, character: str) -> str:
        """Short zone name of the current soulbind, or empty when never bound."""
        row = self._db.execute(
            "SELECT zone FROM events WHERE character = ? AND kind = 'soulbind' AND npc = 'current'",
            (character,),
        ).fetchone()
        return (row[0] if row else "") or ""

    def flag_values(self, character: str) -> dict[str, int]:
        """Flag name → int. Missing means unset. Legacy rows that are bare names count as 1."""
        rows = self._db.execute(
            "SELECT detail FROM events WHERE character = ? AND kind = 'flag'",
            (character,),
        ).fetchall()
        found: dict[str, int] = {}
        for (detail,) in rows:
            if "=" in detail:
                name, _, raw = detail.partition("=")
                try:
                    found[name] = int(raw)
                except ValueError:
                    found[name] = 1
            elif detail:
                found[detail] = 1
        return found

    def flags(self, character: str) -> set[str]:
        """Flag names present (compat). Prefer flag_values for comparisons."""
        return set(self.flag_values(character))

    @staticmethod
    def _corpse_detail(x: float, y: float, z: float, seq: str = "") -> str:
        # seq keeps same-spot deaths unique under the events PRIMARY KEY.
        base = f"{x:.1f},{y:.1f},{z:.1f}"
        return f"{base}@{seq}" if seq else base

    @staticmethod
    def _parse_corpse_detail(detail: str) -> tuple[float, float, float] | None:
        # Accept "x,y,z" (legacy) and "x,y,z@seq".
        coords = (detail or "").split("@", 1)[0]
        parts = coords.split(",")
        if len(parts) != 3:
            return None
        try:
            return float(parts[0]), float(parts[1]), float(parts[2])
        except ValueError:
            return None

    def remember_corpse(self, character: str, zone: str, x: float, y: float, z: float) -> None:
        """Append one outstanding corpse for this death (collections must match)."""
        detail = self._corpse_detail(x, y, z, f"{time.time():.3f}")
        self.record(character, zone, character, "corpse", detail)

    def corpses(self, character: str) -> list[tuple[str, float, float, float, str]]:
        """Outstanding corpses oldest-first: (zone, x, y, z, detail)."""
        rows = self._db.execute(
            "SELECT zone, detail FROM events WHERE character = ? AND kind = 'corpse' ORDER BY rowid ASC",
            (character,),
        ).fetchall()
        out: list[tuple[str, float, float, float, str]] = []
        for zone, detail in rows:
            parsed = self._parse_corpse_detail(detail)
            if parsed is None:
                continue
            x, y, z = parsed
            out.append((zone, x, y, z, detail))
        return out

    def outstanding_corpses(self, character: str) -> int:
        return len(self.corpses(character))

    def corpse(
        self,
        character: str,
        *,
        zone: str = "",
        x: float | None = None,
        y: float | None = None,
        z: float | None = None,
    ) -> tuple[str, float, float, float] | None:
        """Next outstanding corpse: closest to (zone,x,y,z) when given, else oldest."""
        rows = self.corpses(character)
        if not rows:
            return None
        if zone and x is not None and y is not None and z is not None:
            want = zone.lower()
            best = None
            best_d = 1e18
            # Prefer same-zone bodies; fall back to any zone by XY if none here.
            for czone, cx, cy, cz, _detail in rows:
                if czone.lower() != want:
                    continue
                d = (cx - x) ** 2 + (cy - y) ** 2 + (cz - z) ** 2
                if d < best_d:
                    best_d = d
                    best = (czone, cx, cy, cz)
            if best is not None:
                return best
            for czone, cx, cy, cz, _detail in rows:
                d = (cx - x) ** 2 + (cy - y) ** 2
                if d < best_d:
                    best_d = d
                    best = (czone, cx, cy, cz)
            if best is not None:
                return best
        zone0, x0, y0, z0, _detail = rows[0]
        return zone0, x0, y0, z0

    def collect_corpse(
        self,
        character: str,
        zone: str = "",
        x: float | None = None,
        y: float | None = None,
        z: float | None = None,
    ) -> int:
        """Remove one outstanding corpse (nearest match if coords given). Returns remaining count."""
        rows = self.corpses(character)
        if not rows:
            return 0
        pick = rows[0]
        if zone and x is not None and y is not None and z is not None:
            want_zone = zone.lower()
            best_i = None
            best_d = 1e18
            for i, (czone, cx, cy, cz, _detail) in enumerate(rows):
                if czone.lower() != want_zone:
                    continue
                d = (cx - x) ** 2 + (cy - y) ** 2 + (cz - z) ** 2
                if d < best_d:
                    best_d = d
                    best_i = i
            if best_i is not None:
                pick = rows[best_i]
        _zone, _x, _y, _z, detail = pick
        self._db.execute(
            "DELETE FROM events WHERE rowid = ("
            "SELECT rowid FROM events WHERE character = ? AND kind = 'corpse' AND detail = ? "
            "ORDER BY rowid ASC LIMIT 1)",
            (character, detail),
        )
        self._db.commit()
        return self.outstanding_corpses(character)

    def forget_corpse(self, character: str) -> None:
        """Drop every outstanding corpse (tests / force-clear). Prefer collect_corpse."""
        self._db.execute("DELETE FROM events WHERE character = ? AND kind = 'corpse'", (character,))
        self._db.commit()

    def tutorial_done(self, character: str) -> bool:
        """True once The Battle of Gloomingdeep (5102) is journaled — mines are finished."""
        if self.has(character, "tutorialb", "guard hobart", "task", "5102"):
            return True
        # Also accept a dedicated marker so later zones can record the same fact.
        return self.has(character, "", "tutorial", "tutorial", "done")

    def mark_tutorial_done(self, character: str) -> None:
        self.record(character, "tutorialb", "guard hobart", "task", "5102")
        self.record(character, "", "tutorial", "tutorial", "done")

    def bot_spells_level(self, character: str) -> int:
        """Owner level at which companion bot spellsettings were last synced (0 = never)."""
        row = self._db.execute(
            "SELECT detail FROM events WHERE character = ? AND kind = 'bot_spells' AND npc = 'level'",
            (character,),
        ).fetchone()
        if row is None:
            return 0
        try:
            return max(0, int(row[0]))
        except (TypeError, ValueError):
            return 0

    def mark_bot_spells(self, character: str, level: int) -> None:
        """Stamp that companion spellsettings were synced through this owner level."""
        self._db.execute(
            "DELETE FROM events WHERE character = ? AND kind = 'bot_spells' AND npc = 'level'",
            (character,),
        )
        self._db.execute(
            "INSERT OR IGNORE INTO events (character, zone, npc, kind, detail) VALUES (?, ?, ?, ?, ?)",
            (character, "", "level", "bot_spells", str(max(0, int(level)))),
        )
        self._db.commit()

    def save_goal_stack(
        self,
        character: str,
        stack: list[int],
        counts: dict[int, int] | None = None,
        *,
        deliver_to: str = "",
        deliver_item: int = 0,
        deliver_count: int = 0,
    ) -> None:
        """Persist the full obtain stack so a PC assign cannot wipe prior goals across restarts."""
        counts = counts or {}
        self._db.execute(
            "DELETE FROM events WHERE character = ? AND kind IN ('goal', 'goal_deliver')",
            (character,),
        )
        for index, item_id in enumerate(stack):
            count = max(1, int(counts.get(item_id, 1)))
            self._db.execute(
                "INSERT INTO events (character, zone, npc, kind, detail) VALUES (?, ?, ?, ?, ?)",
                (character, "", str(index), "goal", f"{int(item_id)}={count}"),
            )
        if deliver_to and deliver_item:
            self._db.execute(
                "INSERT INTO events (character, zone, npc, kind, detail) VALUES (?, ?, ?, ?, ?)",
                (
                    character,
                    "",
                    deliver_to,
                    "goal_deliver",
                    f"{int(deliver_item)}={max(1, int(deliver_count))}",
                ),
            )
        self._db.commit()

    def load_goal_stack(self, character: str) -> tuple[list[int], dict[int, int]]:
        """Ordered item ids (bottom→top) and required counts."""
        rows = self._db.execute(
            "SELECT npc, detail FROM events WHERE character = ? AND kind = 'goal' ORDER BY CAST(npc AS INTEGER), rowid",
            (character,),
        ).fetchall()
        stack: list[int] = []
        counts: dict[int, int] = {}
        for _index, detail in rows:
            raw_id, _, raw_count = detail.partition("=")
            try:
                item_id = int(raw_id)
                count = max(1, int(raw_count or "1"))
            except ValueError:
                continue
            stack.append(item_id)
            counts[item_id] = count
        return stack, counts

    def load_goal_deliver(self, character: str) -> tuple[str, int, int]:
        """Who to free-trade the farm result to: (name, item_id, count). Empty name when unset."""
        row = self._db.execute(
            "SELECT npc, detail FROM events WHERE character = ? AND kind = 'goal_deliver' ORDER BY rowid DESC LIMIT 1",
            (character,),
        ).fetchone()
        if row is None:
            return "", 0, 0
        name, detail = row
        raw_id, _, raw_count = detail.partition("=")
        try:
            return name, int(raw_id), max(1, int(raw_count or "1"))
        except ValueError:
            return name, 0, 0

    def close(self) -> None:
        self._db.close()
