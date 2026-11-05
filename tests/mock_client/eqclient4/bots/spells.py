"""Bot AI spells from bot_spells_entries (npc_spells_id = 3000 + class).

Entries come from bots bootstrap (`INSERT INTO bot_spells_entries` — same rows as the
live bot lists). List labels and spell names are mapped from the peq dump
(`npc_spells`, `spells_new`).

Docs:
  https://docs.eqemu.dev/server/spells/bot-spell-list-ids/
  https://docs.eqemu.dev/server/bots/bot-spell-types/
  https://docs.eqemu.dev/server/bots/bot-spell-settings/

Bootstrap still stores legacy SpellType_* bitmasks; live DBs remapped those to
BotSpellTypes sequential ids (Nuke=0, RegularHeal=1, …). We remap on load.
"""

import json
import os
from collections.abc import Iterable, Sequence
from dataclasses import dataclass, field
from pathlib import Path
from typing import Protocol

from eqclient4.data.cache_builders.common import peq_path
from eqclient4.data.catalog import _tuple
from eqclient4.log import log

# Bot::Create / docs: Warrior 3001 … Berserker 3016.
CLASS_SPELL_LIST = {
    1: 3001,
    2: 3002,
    3: 3003,
    4: 3004,
    5: 3005,
    6: 3006,
    7: 3007,
    8: 3008,
    9: 3009,
    10: 3010,
    11: 3011,
    12: 3012,
    13: 3013,
    14: 3014,
    15: 3015,
    16: 3016,
}

# Docs BotSpellTypes (post-remap).
TYPE_NUKE = 0
TYPE_REGULAR_HEAL = 1
TYPE_ROOT = 2
TYPE_BUFF = 3
TYPE_ESCAPE = 4
TYPE_PET = 5
TYPE_LIFETAP = 6
TYPE_SNARE = 7
TYPE_DOT = 8
TYPE_DISPEL = 9
TYPE_INCOMBAT_BUFF = 10
TYPE_MEZ = 11
TYPE_CHARM = 12
TYPE_SLOW = 13
TYPE_DEBUFF = 14
TYPE_CURE = 15
TYPE_RESURRECT = 16
TYPE_COMPLETE_HEAL = 26
TYPE_FAST_HEAL = 27
TYPE_VERY_FAST_HEAL = 28
TYPE_GROUP_HEAL = 29
TYPE_GROUP_COMPLETE_HEAL = 30
TYPE_GROUP_HOT = 31
TYPE_HOT = 32
TYPE_AE_NUKE = 33
TYPE_AE_RAIN = 34
TYPE_AE_MEZ = 35
TYPE_PBAE_NUKE = 46

HEAL_TYPES = frozenset(
    {
        TYPE_REGULAR_HEAL,
        TYPE_COMPLETE_HEAL,
        TYPE_FAST_HEAL,
        TYPE_VERY_FAST_HEAL,
        TYPE_GROUP_HEAL,
        TYPE_GROUP_COMPLETE_HEAL,
        TYPE_GROUP_HOT,
        TYPE_HOT,
    }
)
NUKE_TYPES = frozenset({TYPE_NUKE, TYPE_AE_NUKE, TYPE_AE_RAIN, TYPE_PBAE_NUKE})
MEZ_TYPES = frozenset({TYPE_MEZ, TYPE_AE_MEZ})
DOT_TYPES = frozenset({TYPE_DOT})
DEBUFF_TYPES = frozenset({TYPE_DEBUFF, TYPE_SLOW, TYPE_SNARE, TYPE_ROOT, TYPE_DISPEL})

# Legacy SpellType_* bitmasks → BotSpellTypes (migration 9047).
_BITMASK_TO_TYPE = {
    1: 0,
    2: 1,
    4: 2,
    8: 3,
    16: 4,
    32: 5,
    64: 6,
    128: 7,
    256: 8,
    512: 9,
    1024: 10,
    2048: 11,
    4096: 12,
    8192: 13,
    16384: 14,
    32768: 15,
    65536: 16,
    131072: 17,
    262144: 18,
    524288: 19,
    1048576: 20,
    2097152: 21,
}

ROLE_TYPES = {
    "heal": HEAL_TYPES,
    "nuke": NUKE_TYPES,
    "mez": MEZ_TYPES,
    "dot": DOT_TYPES,
    "debuff": DEBUFF_TYPES,
    "buff": frozenset({TYPE_BUFF, TYPE_INCOMBAT_BUFF}),
    "pet": frozenset({TYPE_PET}),
    "lifetap": frozenset({TYPE_LIFETAP}),
    "cure": frozenset({TYPE_CURE}),
}

DEFAULT_BOT_SPELLS = str(Path.home() / ".eqclient" / "bot_spells.jsonl")
_BOOTSTRAP = Path(__file__).resolve().parents[4] / "utils" / "sql" / "bot_tables_bootstrap.sql"
_BOT_LIST_LO = 3001
_BOT_LIST_HI = 3016


@dataclass(frozen=True)
class BotSpellEntry:
    npc_spells_id: int
    spell_id: int
    type: int
    minlevel: int
    maxlevel: int
    priority: int = 0
    name: str = ""
    list_name: str = ""

    def to_row(self) -> dict:
        return {
            "list": self.npc_spells_id,
            "list_name": self.list_name,
            "spell": self.spell_id,
            "name": self.name,
            "type": self.type,
            "min": self.minlevel,
            "max": self.maxlevel,
            "priority": self.priority,
        }

    @staticmethod
    def from_row(row: dict) -> BotSpellEntry:
        return BotSpellEntry(
            int(row.get("list") or 0),
            int(row.get("spell") or 0),
            int(row.get("type") or 0),
            int(row.get("min") or 0),
            int(row.get("max") or 255),
            int(row.get("priority") or 0),
            str(row.get("name") or ""),
            str(row.get("list_name") or ""),
        )


@dataclass
class BotSpellBook:
    rows: list[BotSpellEntry] = field(default_factory=list)
    by_list: dict[int, list[BotSpellEntry]] = field(default_factory=dict)
    list_names: dict[int, str] = field(default_factory=dict)
    spell_names: dict[int, str] = field(default_factory=dict)

    def index(self) -> None:
        self.by_list = {}
        self.spell_names = {}
        for row in self.rows:
            if row.spell_id <= 0:
                continue
            self.by_list.setdefault(row.npc_spells_id, []).append(row)
            if row.name:
                self.spell_names.setdefault(row.spell_id, row.name)
            if row.list_name:
                self.list_names.setdefault(row.npc_spells_id, row.list_name)
        for rows in self.by_list.values():
            rows.sort(key=lambda r: (r.minlevel, -r.priority, r.spell_id))

    def for_class(self, class_id: int) -> list[BotSpellEntry]:
        list_id = CLASS_SPELL_LIST.get(class_id) or 0
        return list(self.by_list.get(list_id, ()))

    def available(
        self,
        class_id: int,
        level: int,
        *,
        since_level: int = 0,
        types: frozenset[int] | None = None,
    ) -> list[BotSpellEntry]:
        """Entries usable at `level`. If since_level>0, only newly unlocked (minlevel > since)."""
        found: list[BotSpellEntry] = []
        seen: set[int] = set()
        for row in self.for_class(class_id):
            if level < row.minlevel or level > row.maxlevel:
                continue
            if since_level > 0 and row.minlevel <= since_level:
                continue
            if types is not None and row.type not in types:
                continue
            if row.spell_id in seen:
                continue
            seen.add(row.spell_id)
            found.append(row)
        return found

    def roles_available(
        self,
        class_id: int,
        level: int,
        roles: set[str],
        *,
        since_level: int = 0,
    ) -> list[BotSpellEntry]:
        wanted: set[int] = set()
        for role in roles:
            wanted |= ROLE_TYPES.get(role, frozenset())
        if not wanted:
            return []
        return self.available(class_id, level, since_level=since_level, types=frozenset(wanted))


_CASTERS = {2, 3, 4, 6, 8, 10, 11, 12, 13, 14, 15}
_BOT_ROLES = {
    2: {"heal", "cure"},
    3: {"heal"},
    4: {"nuke"},
    5: {"lifetap"},
    6: {"heal", "nuke"},
    8: {"debuff"},
    10: {"heal", "debuff"},
    11: {"nuke", "dot", "pet"},
    12: {"nuke"},
    13: {"pet", "nuke"},
    14: {"mez"},
    15: {"pet", "debuff"},
}


class _SpellEntry(Protocol):
    priority: int
    spell_id: int


class _BotBook(Protocol):
    def roles_available(
        self, class_id: int, level: int, roles: set[str]
    ) -> Iterable[_SpellEntry]: ...


class _BotWorld(Protocol):
    level: int


class _SpellState(Protocol):
    bot_spell_left: list[str] | None
    queue: object
    bot_spells: _BotBook | None
    bots: Sequence[tuple[object, ...]]
    world: _BotWorld


def next_spell_line(state: _SpellState) -> str:
    """One bot spell command. Empty once the list for this roster has been sent."""
    left = state.bot_spell_left
    if left is None:
        state.bot_spell_left = left = _spell_lines(state)
    if not left:
        return ""
    return left.pop(0)


def spell_due(state: _SpellState) -> bool:
    if state.queue or state.bot_spells is None or not state.bots:
        return False
    left = state.bot_spell_left
    if left is None:
        return bool(_spell_lines(state))
    return bool(left)


def _spell_lines(state: _SpellState) -> list[str]:
    book = state.bot_spells
    if book is None or not state.bots:
        return []
    level = state.world.level or 1
    lines = ["^spellholds 0 0 spawned"]
    for bot in state.bots:
        if len(bot) < 2 or not isinstance(bot[0], str) or not isinstance(bot[1], int):
            continue
        name, class_id = bot[0], bot[1]
        if class_id in _CASTERS:
            lines.append(f"^botstance 7 byname {name}")
        roles = _BOT_ROLES.get(class_id)
        if not roles:
            continue
        for entry in book.roles_available(class_id, level, roles):
            priority = entry.priority if entry.priority > 0 else 1
            lines.append(f"^spellsettingsadd {entry.spell_id} {priority} 0 100")
    return lines


def _remap_type(raw: int) -> int:
    return _BITMASK_TO_TYPE.get(raw, raw)


def _take_entry(book: BotSpellBook, chunk: str) -> None:
    fields = _tuple(chunk)
    if len(fields) < 9:
        return
    try:
        npc_id = int(fields[1])
        spell_id = int(fields[2])
        type_id = _remap_type(int(fields[3]))
        min_l = int(fields[4])
        max_l = int(fields[5])
        priority = int(fields[8]) if fields[8].lstrip("-").isdigit() else 0
    except ValueError:
        log.error("bot spell row failed to parse", exc_info=True)
        return
    if npc_id <= 0 or spell_id <= 0:
        return
    book.rows.append(BotSpellEntry(npc_id, spell_id, type_id, min_l, max_l, priority))


def spells_from_bootstrap(path: str | Path | None = None) -> BotSpellBook:
    """Parse INSERT INTO bot_spells_entries; remap legacy bitmasks to BotSpellTypes."""
    file = Path(path) if path else _BOOTSTRAP
    book = BotSpellBook()
    if not file.is_file():
        return book
    mode = False
    for raw in file.read_text(encoding="latin1", errors="replace").splitlines():
        line = raw.strip()
        if line.startswith("INSERT INTO `bot_spells_entries`"):
            mode = True
            for chunk in _split_tuples(line):
                _take_entry(book, chunk)
            continue
        if not mode:
            continue
        if line.startswith("INSERT INTO `") and "bot_spells_entries" not in line:
            break
        if line.startswith("UNLOCK") or line.startswith("/*!") or line.startswith("--"):
            if line.startswith("UNLOCK"):
                break
            continue
        if "(" not in line:
            continue
        for chunk in _split_tuples(line):
            _take_entry(book, chunk)
    book.index()
    return book


def _peq_spell_names(peq: Path) -> dict[int, str]:
    """spell_id → name from spells_new in the peq dump."""
    names: dict[int, str] = {}
    mode = False
    with peq.open(encoding="latin1", errors="replace") as handle:
        for raw in handle:
            line = raw.strip()
            if line.startswith("INSERT INTO `spells_new`"):
                mode = True
                continue
            if not mode:
                continue
            if line.startswith("INSERT INTO `") and "spells_new" not in line:
                break
            if line.startswith("UNLOCK") or "ENABLE KEYS" in line:
                break
            if not line.startswith("("):
                continue
            for chunk in _split_tuples(line):
                fields = _tuple(chunk)
                if len(fields) < 2 or not fields[0].isdigit() or not fields[1]:
                    continue
                names[int(fields[0])] = fields[1]
    return names


def _peq_list_names(peq: Path) -> dict[int, str]:
    """npc_spells_id → list name for bot lists 3001–3016."""
    names: dict[int, str] = {}
    mode = False
    needed = _BOT_LIST_HI - _BOT_LIST_LO + 1
    with peq.open(encoding="latin1", errors="replace") as handle:
        for raw in handle:
            line = raw.strip()
            if line.startswith("INSERT INTO `npc_spells`"):
                mode = True
                for chunk in _split_tuples(line):
                    _take_list_name(names, chunk)
                continue
            if not mode:
                continue
            if line.startswith("INSERT INTO `") and "npc_spells" not in line:
                break
            if line.startswith("UNLOCK") or "ENABLE KEYS" in line:
                break
            if not line.startswith("("):
                continue
            for chunk in _split_tuples(line):
                _take_list_name(names, chunk)
            if len(names) >= needed:
                return names
    return names


def _take_list_name(names: dict[int, str], chunk: str) -> None:
    fields = _tuple(chunk)
    if len(fields) < 2 or not fields[0].isdigit():
        return
    list_id = int(fields[0])
    if list_id < _BOT_LIST_LO or list_id > _BOT_LIST_HI:
        return
    name = fields[1]
    if name:
        names[list_id] = name


def enrich_from_peq(book: BotSpellBook, peq: str | Path) -> BotSpellBook:
    """Attach spells_new names and npc_spells list labels onto bootstrap entries."""
    dump = Path(peq)
    if not dump.is_file() or not book.rows:
        return book
    spell_names = _peq_spell_names(dump)
    list_names = _peq_list_names(dump)
    enriched = BotSpellBook(list_names=dict(list_names))
    for row in book.rows:
        enriched.rows.append(
            BotSpellEntry(
                row.npc_spells_id,
                row.spell_id,
                row.type,
                row.minlevel,
                row.maxlevel,
                row.priority,
                spell_names.get(row.spell_id, row.name),
                list_names.get(row.npc_spells_id, row.list_name),
            )
        )
    enriched.index()
    return enriched


def build_bot_spells(
    peq: str | Path | None = None,
    bootstrap: str | Path | None = None,
) -> BotSpellBook:
    """bot_spells_entries from bootstrap, names/lists from peq dump."""
    book = spells_from_bootstrap(bootstrap)
    if peq is not None:
        book = enrich_from_peq(book, peq)
    return book


def _split_tuples(line: str) -> list[str]:
    out: list[str] = []
    start = -1
    depth = 0
    for i, ch in enumerate(line):
        if ch == "(":
            if depth == 0:
                start = i
            depth += 1
        elif ch == ")":
            depth -= 1
            if depth == 0 and start >= 0:
                out.append(line[start : i + 1] + ",")
                start = -1
    return out


def write_bot_spells(book: BotSpellBook, path: str | None = None) -> None:
    destination = Path(path or DEFAULT_BOT_SPELLS)
    destination.parent.mkdir(parents=True, exist_ok=True)
    lines = [json.dumps(row.to_row(), ensure_ascii=True) for row in book.rows]
    destination.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")


def read_bot_spells(path: str | None = None) -> BotSpellBook:
    book = BotSpellBook()
    file = Path(path or os.environ.get("EQEMU_BOT_SPELLS", DEFAULT_BOT_SPELLS))
    if not file.is_file():
        return book
    for line in file.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        row = BotSpellEntry.from_row(json.loads(line))
        if row.npc_spells_id and row.spell_id:
            book.rows.append(row)
    book.index()
    return book


def ensure_bot_spells(
    path: str | None = None,
    peq: str | Path | None = None,
    bootstrap: str | Path | None = None,
    *,
    rebuild: bool = False,
) -> BotSpellBook:
    """Prefer cache_builders.bot_spells.ensure_bot_spells from agent code."""
    destination = path or os.environ.get("EQEMU_BOT_SPELLS", DEFAULT_BOT_SPELLS)
    if not rebuild:
        existing = read_bot_spells(destination)
        if existing.rows:
            return existing
    try:
        dump = peq_path(peq)
        peq_arg: str | Path | None = dump if dump.is_file() else None
    except Exception:
        log.error("bot spell dump path failed", exc_info=True)
        peq_arg = peq
    book = build_bot_spells(peq_arg, bootstrap)
    if book.rows:
        write_bot_spells(book, destination)
    return book
