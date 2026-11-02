"""Move a scroll onto the cursor, write it, and load the gem.

The server only scribes the item on the cursor, and the spell id has to be
that item's scroll effect. A scroll already on the cursor is written in
place. The learned line finishes it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Protocol, runtime_checkable

if TYPE_CHECKING:
    from eqclient3.loop import Loop
    from eqclient3.world import World

from eqclient3.action import Action
from eqclient3.actions.support import CURSOR_SLOT, message_text
from eqclient3.data.spells import DEFAULT_SPELLS, ITEM_SPELL, open_book_slot, read_spells
from eqclient3.structs import OP_MemorizeSpell, OP_MoveItem, OP_ReadBook

# Above quest talk and under the cursor band until the scroll is on the cursor.
# The write itself sits above the cursor so the scroll is not filed away mid-scribe.
SCRIBE_BAND = 340
_ABOVE_CURSOR = 360
_GENERAL = range(22, 30)
_NAMED: dict[tuple[int, str], int] | None = None


class ScribeSpell(Action):

    def __init__(self, spell_id: int, slot: int) -> None:
        super().__init__()
        self.priority = 0
        self.durable = True
        self.spell_id = int(spell_id)
        self.slot = int(slot)
        self.wrote = False

    def opcodes(self) -> tuple[str, ...]:
        return ("OP_MemorizeSpell", "OP_SpecialMesg")

    def suspend(self) -> None:
        self.suspended = True

    def step(self, loop: Loop, world: World) -> None:
        if self._learned(world) or known_spell(world, self.spell_id):
            self.unwait("SCRIBE")
            self.unwait("MOVE")
            self.complete = True
            return
        while self.consume("OP_SpecialMesg") or self.consume("OP_MemorizeSpell"):
            pass
        self.suspended = False
        if _teaches(world, self.spell_id):
            self.unwait("MOVE")
            self.priority = _ABOVE_CURSOR
            if self.waiting_for("SCRIBE"):
                return
            self._send(loop, world)
            return
        if self.waiting_for("SCRIBE"):
            self.unwait("SCRIBE")
        if self.waiting_for("MOVE"):
            self.waited += 1
            if self.waited < 10:
                return
            self.unwait("MOVE")
            self.waited = 0
        where = _holding(world, self.spell_id, self.slot)
        if not where:
            self.priority = 0
            self.yielding = True
            return
        self.priority = SCRIBE_BAND
        if world.cursor and where != CURSOR_SLOT:
            free = _open_general(world, where)
            if free is None:
                self.yielding = True
                return
            loop.send("OP_MoveItem", OP_MoveItem(CURSOR_SLOT, free).serialize())
            self._arm_move()
            return
        if where and where != CURSOR_SLOT:
            loop.send("OP_MoveItem", OP_MoveItem(where, CURSOR_SLOT).serialize())
            self._arm_move()
            return
        self.yielding = True

    def _arm_move(self) -> None:
        self.waited = 0
        self.wait("MOVE")

    def _send(self, loop: Loop, world: World) -> None:
        if self.spell_id in set(world.tomes or ()):
            loop.send("OP_ReadBook", OP_ReadBook(int(self.spell_id)).serialize())
        else:
            loop.send(
                "OP_MemorizeSpell",
                OP_MemorizeSpell(int(self.slot), int(self.spell_id), 0).serialize(),
            )
        gem = int(world.gem_slot or 0)
        loop.send("OP_MemorizeSpell", OP_MemorizeSpell(gem, int(self.spell_id), 1).serialize())
        self.wrote = True
        self.wait("SCRIBE")

    def _learned(self, world: World) -> bool:
        name = _spell_name(world, self.spell_id)
        learned = lambda message: _learned_line(message_text(message), name)
        if self.consume("OP_SpecialMesg", learned):
            return True
        memo = self.consume("OP_MemorizeSpell")
        if memo is not None and self.spell_id in set((world.spells or {}).values()):
            return True
        return False


def _holding(world: World, spell_id: int, slot: int) -> int:
    """Inventory slot of the scroll for this spell. The cursor wins when it is sitting there."""
    if _teaches(world, spell_id):
        return CURSOR_SLOT
    bags = world.bags or {}
    for held_slot, item_id in bags.items():
        if _spell_of(world, int(item_id or 0)) == spell_id:
            return int(held_slot)
    item_id = int(bags.get(slot) or 0)
    if item_id and slot != CURSOR_SLOT:
        return int(slot)
    return 0


def _open_general(world: World, keep: int) -> int | None:
    bags = world.bags or {}
    for slot in _GENERAL:
        if slot == keep or bags.get(slot):
            continue
        return slot
    return None


def _scroll_id(world: World, spell_id: int, slot: int) -> int:
    scrolls = world.scrolls or {}
    if spell_id in scrolls:
        return int(scrolls[spell_id])
    item = (world.bags or {}).get(slot)
    return int(item) if item else 0


def _learned_line(text: str, name: str) -> bool:
    lowered = (text or "").lower()
    if name and f"you have learned {name.lower()}!" in lowered:
        return True
    return "you have learned" in lowered and (not name or name.lower() in lowered)


@runtime_checkable
class _ScrollItem(Protocol):
    name: str
    item_type: int
    scroll_effect: int


def held_scroll(world: World) -> tuple[int, int]:
    """The spell id and the slot of a scroll on the cursor or in a general slot."""
    cursor = int(world.cursor or 0)
    spell_id = _spell_of(world, cursor)
    if spell_id:
        return (spell_id, CURSOR_SLOT)
    bags = world.bags or {}
    for slot in _GENERAL:
        spell_id = _spell_of(world, int(bags.get(slot) or 0))
        if spell_id:
            return (spell_id, slot)
    return (0, 0)


def book_slot(world: World, where: int) -> int | None:
    """A general slot is where the scroll sits. The cursor uses the next open book slot."""
    if where != CURSOR_SLOT:
        return where
    return open_book_slot(_book(world))


def known_spell(world: World, spell_id: int) -> bool:
    return spell_id in _book(world).values()


def _teaches(world: World, spell_id: int) -> bool:
    return _spell_of(world, int(world.cursor or 0)) == spell_id


def _spell_of(world: World, item_id: int) -> int:
    if item_id <= 0:
        return 0
    row = _row(world, item_id)
    if row is None:
        return 0
    name = row.name
    lowered = name.lower()
    if lowered.startswith("tome of ") or lowered.startswith("skill:"):
        return 0
    if row.item_type and row.item_type != ITEM_SPELL:
        return 0
    if row.scroll_effect > 0:
        return row.scroll_effect
    if row.item_type != ITEM_SPELL and not lowered.startswith("spell:"):
        return 0
    return _named(name, world.class_id)


def _row(world: World, item_id: int) -> _ScrollItem | None:
    items = world.items
    if not isinstance(items, dict):
        return None
    row = items.get(item_id)
    if isinstance(row, _ScrollItem):
        return row
    return None


def _book(world: World) -> dict[int, int]:
    found: dict[int, int] = {}
    for raw in (world.spell_book, world.spells):
        if not isinstance(raw, dict):
            continue
        for slot, spell_id in raw.items():
            if isinstance(slot, int) and isinstance(spell_id, int) and not isinstance(spell_id, bool) and spell_id > 0:
                found[slot] = spell_id
    return found


def _named(name: str, class_id: int) -> int:
    plain = name.lower().removeprefix("spell:").strip()
    if not plain:
        return 0
    table = _names()
    return table.get((class_id, plain), 0)


def _names() -> dict[tuple[int, str], int]:
    global _NAMED
    if _NAMED is not None:
        return _NAMED
    found: dict[tuple[int, str], int] = {}
    for row in read_spells(DEFAULT_SPELLS).rows:
        found.setdefault((row.class_id, row.name.lower()), row.spell_id)
    _NAMED = found
    return found


def _spell_name(world: World, spell_id: int) -> str:
    names = world.spell_names or {}
    info = (world.spell_info or {}).get(spell_id)
    if spell_id in names:
        return str(names[spell_id])
    if info is not None and info.name:
        return str(info.name)
    return ""
