"""Spell scrolls are written into the book before a gem can hold them.

The spell id comes from the scroll. A gem packet for a spell that is not in
the book is rejected by the server, so that send is not offered.

Which spells a class can use, and the scroll item that teaches each one, is
cached beside the quest graph as ~/.eqclient/spells.jsonl. A level change
pushes one of those item ids per spell still missing from the book.
"""

from __future__ import annotations

import json
import os
from dataclasses import dataclass, field
from pathlib import Path

from eqclient3.data.builds import build_for
from eqclient3.data.cache_builders.common import peq_path
from eqclient3.data.catalog import _table, _tuple
from eqclient3.net.decode import body
from eqclient3.structs import OP_MemorizeSpell, OP_MoveItem

CURSOR = 30

ITEM_SPELL = 20
SCRIBE = 0
MEMORIZE = 1
BOOK_SLOTS = 400
GEM_SLOTS = 8
EMPTY = {0, 0xFFFFFFFF}


def is_scroll(name: str, item_type: int, effect: int) -> bool:
    """A spell scroll. A skill tome uses the same item type and is not one."""
    if item_type != ITEM_SPELL or effect <= 0:
        return False
    lowered = name.lower()
    return not lowered.startswith("tome of ") and not lowered.startswith("skill:")


def book_from(words) -> dict[int, int]:
    return {index: spell for index, spell in enumerate(words) if spell not in EMPTY}


def open_book_slot(book: dict[int, int]) -> int | None:
    for slot in range(BOOK_SLOTS):
        if slot not in book:
            return slot
    return None


def gem_for(role: str, roles: tuple[str, ...], gems: dict[int, int]) -> int | None:
    """The build's gem for this role, or the next open gem when that one is taken."""
    if role and role in roles:
        slot = roles.index(role)
        if slot < GEM_SLOTS and slot not in gems:
            return slot
    for slot in range(GEM_SLOTS):
        if slot not in gems:
            return slot
    return None


def _role_of(name: str) -> str:
    # quests.conduct is not in this tree.
    from eqclient3.quests.conduct import role_of
    return role_of(name)


def spell_step(inventory, class_id: int) -> tuple[str, int, str] | None:
    """Scribe a scroll he is holding. Memorize only after that spell is in the book."""
    scroll = inventory.scroll()
    if scroll is not None:
        return ("scribe", scroll.scroll_spell, scroll.name)
    build = build_for(class_id)
    roles = build.gems if build is not None else ()
    if not roles:
        return None
    for spell_id in inventory.scribed:
        if spell_id in inventory.memorized.values():
            continue
        role = _role_of(inventory.spell_names.get(spell_id, ""))
        if role not in roles:
            continue
        if gem_for(role, roles, inventory.memorized) is None:
            continue
        return ("memorize", spell_id, role)
    return None


def scribe_due(state: State) -> bool:
    return _tick_scroll(state) is not None or _tick_gem(state) is not None


def scribe_actions(state: State) -> list:
    """Move a scroll to the cursor, write the book, then load the gem."""
    found = _tick_scroll(state)
    if found is not None:
        slot, held = found
        if slot != CURSOR:
            return [("op", "OP_MoveItem", OP_MoveItem(int(slot), CURSOR).serialize())]
        book_slot = open_book_slot(state.book)
        if book_slot is None:
            return []
        return [("op", "OP_MemorizeSpell", OP_MemorizeSpell(int(book_slot), int(held.scroll_spell), SCRIBE).serialize())]
    waiting = _tick_gem(state)
    if waiting is None:
        return []
    slot, spell_id, _role = waiting
    return [("op", "OP_MemorizeSpell", OP_MemorizeSpell(int(slot), int(spell_id), MEMORIZE).serialize())]


def note_memorize(state: State, payload: bytes) -> None:
    row = body("OP_MemorizeSpell", payload)
    if row is None:
        return
    slot, spell_id, scribing = row.slot, row.spell_id, row.scribing
    if int(scribing) == SCRIBE:
        state.book[int(slot)] = int(spell_id)
        state.scribed.add(int(spell_id))
    elif int(scribing) == MEMORIZE:
        state.memorized[int(slot)] = int(spell_id)


def _tick_scroll(state: State):
    for slot, item_id in state.slots.items():
        held = state.by_id.get(int(item_id))
        if held is None or held.scroll_spell <= 0 or held.item_type != 20:
            continue
        if held.scroll_spell in state.scribed:
            continue
        lowered = (held.name or "").lower()
        if lowered.startswith("tome of ") or lowered.startswith("skill:"):
            continue
        return int(slot), held
    return None


def _tick_gem(state: State):
    build = build_for(state.world.class_id or 1)
    roles = build.gems if build is not None else ()
    for spell_id in state.scribed:
        if spell_id in state.memorized.values():
            continue
        role = _role_of(state.spell_names.get(spell_id, ""))
        if role not in roles:
            continue
        slot = gem_for(role, roles, state.memorized)
        if slot is None:
            continue
        return slot, spell_id, role
    return None


# spells_new.classes1 is column 104 (warrior). items.itemtype is 82, scrolleffect is 159.
_CLASS_LEVEL = 104
_CLASS_COUNT = 16
_ITEM_TYPE = 82
_SCROLL_EFFECT = 159
_UNUSABLE = 255
DEFAULT_SPELLS = str(Path.home() / ".eqclient" / "spells.jsonl")


@dataclass(frozen=True)
class SpellScroll:
    """One spell a class can scribe, and the scroll item that teaches it."""

    class_id: int
    level: int
    name: str
    spell_id: int
    item_id: int

    def to_row(self) -> dict:
        return {
            "class": self.class_id,
            "level": self.level,
            "name": self.name,
            "spell": self.spell_id,
            "item": self.item_id,
        }

    @staticmethod
    def from_row(row: dict) -> SpellScroll:
        return SpellScroll(
            int(row.get("class") or 0),
            int(row.get("level") or 0),
            str(row.get("name") or ""),
            int(row.get("spell") or 0),
            int(row.get("item") or 0),
        )


@dataclass
class SpellBook:
    """Spells keyed by class, then the level that class can first use them."""

    rows: list[SpellScroll] = field(default_factory=list)
    by_class: dict[int, list[SpellScroll]] = field(default_factory=dict)
    item_spell: dict[int, int] = field(default_factory=dict)

    def index(self) -> None:
        self.by_class = {}
        self.item_spell = {}
        for row in self.rows:
            self.by_class.setdefault(row.class_id, []).append(row)
            self.item_spell[row.item_id] = row.spell_id
        for rows in self.by_class.values():
            rows.sort(key=lambda row: (row.level, row.name.lower(), row.spell_id))

    def missing(self, class_id: int, level: int, scribed: set[int], skip_items: set[int]) -> list[SpellScroll]:
        """Spells this class can use by `level` that are not in the book and not already queued or held."""
        if class_id <= 0 or level <= 0:
            return []
        found: list[SpellScroll] = []
        for row in self.by_class.get(class_id, ()):
            if row.level > level:
                break
            if row.spell_id in scribed or row.item_id in skip_items:
                continue
            found.append(row)
        return found


def spells_from_lines(lines) -> SpellBook:
    """Class, level, and name for every spell that has a scroll in the dump."""
    mode = ""
    spells: dict[int, tuple[str, tuple[int, ...]]] = {}
    scrolls: dict[int, tuple[int, str]] = {}
    for raw in lines:
        line = raw.strip()
        if line.startswith("INSERT INTO `"):
            mode = _table(line)
            continue
        if not line.startswith("("):
            continue
        if mode == "spells_new":
            _take_spell_levels(line, spells)
        elif mode == "items":
            _take_scroll_item(line, scrolls)
    book = SpellBook()
    for spell_id, (name, levels) in spells.items():
        scroll = scrolls.get(spell_id)
        if scroll is None:
            continue
        item_id, _item_name = scroll
        for class_id, level in enumerate(levels, start=1):
            if level <= 0 or level >= _UNUSABLE:
                continue
            book.rows.append(SpellScroll(class_id, level, name, spell_id, item_id))
    book.rows.sort(key=lambda row: (row.class_id, row.level, row.name.lower(), row.spell_id))
    book.index()
    return book


def _take_spell_levels(line: str, spells: dict[int, tuple[str, tuple[int, ...]]]) -> None:
    fields = _tuple(line)
    if len(fields) < _CLASS_LEVEL + _CLASS_COUNT or not fields[0].isdigit() or not fields[1]:
        return
    levels: list[int] = []
    for offset in range(_CLASS_COUNT):
        raw = fields[_CLASS_LEVEL + offset]
        levels.append(int(raw) if raw.lstrip("-").isdigit() else _UNUSABLE)
    if all(level <= 0 or level >= _UNUSABLE for level in levels):
        return
    spells[int(fields[0])] = (fields[1], tuple(levels))


def _take_scroll_item(line: str, scrolls: dict[int, tuple[int, str]]) -> None:
    fields = _tuple(line)
    if len(fields) <= _SCROLL_EFFECT or not fields[0].isdigit():
        return
    if not fields[_ITEM_TYPE].lstrip("-").isdigit() or int(fields[_ITEM_TYPE]) != ITEM_SPELL:
        return
    effect = fields[_SCROLL_EFFECT]
    if not effect.isdigit() or int(effect) <= 0:
        return
    name = fields[2] if len(fields) > 2 else ""
    lowered = name.lower()
    if lowered.startswith("tome of ") or lowered.startswith("skill:"):
        return
    spell_id = int(effect)
    item_id = int(fields[0])
    current = scrolls.get(spell_id)
    if current is None or _better_scroll(item_id, name, current):
        scrolls[spell_id] = (item_id, name)


def _better_scroll(item_id: int, name: str, current: tuple[int, str]) -> bool:
    """Prefer a row named Spell:, then the lower item id."""
    current_id, current_name = current
    named = name.lower().startswith("spell:")
    current_named = current_name.lower().startswith("spell:")
    if named != current_named:
        return named
    return item_id < current_id


def build_spells(peq: str | Path) -> SpellBook:
    """Read spells_new and scroll items from a local peq dump. No live query."""
    return spells_from_lines(_lines(str(peq)))


def write_spells(book: SpellBook, path: str) -> None:
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    lines = [json.dumps(row.to_row(), ensure_ascii=True) for row in book.rows]
    destination.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")


def read_spells(path: str) -> SpellBook:
    book = SpellBook()
    file = Path(path)
    if not file.is_file():
        return book
    for line in file.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        row = SpellScroll.from_row(json.loads(line))
        if row.class_id and row.spell_id and row.item_id and row.level:
            book.rows.append(row)
    book.index()
    return book


def ensure_spells(
    path: str | None = None,
    peq: str | Path | None = None,
    *,
    rebuild: bool = False,
) -> SpellBook:
    """Load spells.jsonl, or build once from the peq dump."""
    path = path or os.environ.get("EQEMU_SPELLS", DEFAULT_SPELLS)
    file = Path(path)
    if file.is_file() and not rebuild:
        return read_spells(path)
    dump = peq_path(peq)
    book = build_spells(dump) if dump.is_file() else SpellBook()
    if book.rows:
        write_spells(book, path)
    return book


_SEEK_SOURCE = ("forage:", "fishing:", "ground:", "loot:")
_SEEK_EDGE = {"gives", "loots", "grounds", "produces", "buys", "sells"}


def _graph_can_seek(graph, item_id: int, merchants=None, recipes=None, drops=None) -> bool:
    """True when the obtain stack has a giver, a recipe, a drop, or a vendor for this scroll."""
    if merchants is not None and merchants.sells(item_id):
        return True
    if recipes is not None and recipes.for_item(item_id) is not None:
        return True
    if drops is not None and drops.drops(item_id):
        return True
    if graph is None:
        return True
    info = (getattr(graph, "items", None) or {}).get(item_id) or {}
    if any(str(source).startswith(_SEEK_SOURCE) for source in info.get("sources") or ()):
        return True
    token = f"item:{item_id}"
    if getattr(graph, "_indexed", False):
        return any(edge.get("rel") in _SEEK_EDGE for edge in graph.edges_to.get(token, ()))
    for edge in getattr(graph, "edges", ()) or ():
        if str(edge.get("to")) == token and edge.get("rel") in _SEEK_EDGE:
            return True
    return False


def _lines(path: str):
    with open(path, encoding="latin1", errors="replace") as handle:
        yield from handle


def apply_spell_goals(
    campaign,
    book: SpellBook,
    class_id: int,
    level: int,
    scribed: set[int],
    held: set[int],
    graph=None,
    merchants=None,
    recipes=None,
    drops=None,
) -> tuple[int, list[str]] | None:
    """Drop scrolls for spells already in the book, and push one item id per spell still missing.

    Lower levels are pushed first, so the newest spell is the top of the stack.
    Returns (dropped count, names pushed), or None when the stack did not change.
    """
    if book is None or not book.by_class:
        return None
    known_items = {item_id for item_id, spell_id in book.item_spell.items() if spell_id in scribed}
    dropped = 0
    if known_items:
        kept = [item_id for item_id in campaign.stack if item_id not in known_items]
        if len(kept) != len(campaign.stack):
            dropped = len(campaign.stack) - len(kept)
            counts = {item_id: campaign.counts.get(item_id, 1) for item_id in kept}
            campaign.load_stack(kept, counts)
    skip = set(campaign.stack) | set(held)
    names: list[str] = []
    for row in book.missing(class_id, level, scribed, skip):
        # A scroll the graph cannot give, loot, or buy would sit on top and stall every goal under it.
        if not _graph_can_seek(graph, row.item_id, merchants, recipes, drops):
            continue
        if campaign.assign_goal(row.item_id, graph=graph):
            skip.add(row.item_id)
            names.append(row.name)
    if not dropped and not names:
        return None
    return dropped, names
