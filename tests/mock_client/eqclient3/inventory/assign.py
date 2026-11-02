"""One pass over loose gear. The player upgrades first, then each bot.

An upgrade for the player queues Cursor, which sends OP_MoveItem. An upgrade
for a bot appends Distribute with the worn piece emptied first. A fill appends
Distribute as a give. A wearable piece that loses every slot is marked disposable unless it is a quest id,
no-drop, or still on the obtain stack. A scroll, a tome, and a slot the server
just refused stay. A cursor
that is still holding an item is queued the same way. Call this when loot
completes or an inventory packet has been applied. An empty pulse passes
applied=False and appends nothing.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient3.action import Action
    from eqclient3.journal import Journal
    from eqclient3.loop import Loop
    from eqclient3.quests.graph import QuestGraph
    from eqclient3.world import World

import json
from dataclasses import dataclass
from pathlib import Path
from eqclient3.log import log
from eqclient3.actions.craft import Craft
from eqclient3.actions.cursor import Cursor
from eqclient3.actions.distribute import Distribute
from eqclient3.actions.scribe import SCRIBE_BAND, ScribeSpell, book_slot, held_scroll, known_spell
from eqclient3.actions.sell import Sell
from eqclient3.actions.trade import Trade
from eqclient3.actions.support import CURSOR_SLOT, TOKEN, empty_slots

PRIMARY = 13
SECONDARY = 14
WORN = range(22)
BOT_RACE = 1
_TWO_HAND = 8192
_ITEMS: dict[int, dict] | None = None


class _Piece:

    def __init__(self, item_id: int, facts: dict | None = None) -> None:
        raw = facts or {}
        self.item_id = int(item_id)
        self.slots = int(raw.get("slots") or 0)
        self.classes = int(raw.get("classes") or 0)
        self.races = int(raw.get("races") or 0)
        self.req_level = int(raw.get("reqlevel") or raw.get("req_level") or 0)
        self.ac = int(raw.get("ac") or 0)
        self.damage = int(raw.get("damage") or 0)
        self.astr = int(raw.get("astr") or 0)
        self.asta = int(raw.get("asta") or 0)
        self.aagi = int(raw.get("aagi") or 0)
        self.adex = int(raw.get("adex") or 0)
        self.awis = int(raw.get("awis") or 0)
        self.aint = int(raw.get("aint") or 0)
        self.acha = int(raw.get("acha") or 0)
        self.hp = int(raw.get("hp") or 0)
        self.mana = int(raw.get("mana") or 0)
        nodrop = raw.get("nodrop")
        self.nodrop = nodrop if isinstance(nodrop, int) else 255
        self.slot = int(raw.get("slot") or 0)


def assign(
    loop: Loop,
    world: World,
    journal: Journal | None = None,
    *,
    applied: bool = True,
    graph: QuestGraph | None = None,
) -> None:
    """Player upgrade, then each displaced piece down the companions. The last loser is marked for sale."""
    if not applied:
        return
    if _stow_supplies(loop, world, journal):
        return
    if _offer_scribe(loop, world, journal):
        return
    loose = _loose(world)
    if not loose:
        return
    character = _character(loop, world)
    protected = _protected(loop, world, journal, character, graph)
    stack = _stack(journal, character)
    player = (int(world.class_id or 1), int(world.race or 1), int(world.level or 1))
    worn = _worn_map(world, journal, character)
    player_worn = worn.setdefault("player", {})
    remaining = list(loose)
    moved = _cursor_busy(loop)
    for held in list(remaining):
        if held.item_id in protected or held.item_id in stack:
            continue
        if not _fits(held, player[0], player[1], player[2]):
            continue
        for slot in _legal_slots(held, world.refused_slots):
            current = player_worn.get(slot)
            if _gain(held, current) <= 0:
                continue
            if moved:
                remaining.remove(held)
                break
            _start_move(loop, world, journal, held.slot, slot)
            moved = True
            remaining.remove(held)
            player_worn[slot] = held
            if current is not None:
                remaining.append(current)
            break
    bots = _bots(world, journal, character)
    tried: set[tuple[int, str, int]] = set()
    for rank in range(32):
        choice = _best_handoff(remaining, worn, bots, world.refused_slots, tried)
        if choice is None:
            break
        emptied: list[int] = []
        displaced: list[_Piece] = []
        if choice.displaced is not None:
            emptied.append(choice.slot)
            displaced.append(choice.displaced)
        bot_worn = worn.setdefault(choice.bot, {})
        if choice.piece.slots & _TWO_HAND and choice.slot == PRIMARY:
            off = bot_worn.get(SECONDARY)
            emptied.append(SECONDARY)
            if off is not None and off is not choice.displaced:
                displaced.append(off)
            bot_worn.pop(SECONDARY, None)
        _append_distribute(loop, world, journal, choice.piece.item_id, choice.bot, tuple(emptied), rank)
        bot_worn[choice.slot] = choice.piece
        remaining.remove(choice.piece)
        tried.add((id(choice.piece), choice.bot, choice.slot))
        for old in displaced:
            remaining.append(old)
    cursor_id = world.cursor or 0
    for held in remaining:
        if cursor_id and held.item_id == cursor_id:
            continue
        if held.item_id in protected or held.item_id in stack or held.nodrop == 0:
            continue
        legal = _legal_slots(held, set())
        if not legal or any(slot in world.refused_slots for slot in legal):
            continue
        wins = False
        if _fits(held, player[0], player[1], player[2]):
            for slot in legal:
                if _gain(held, player_worn.get(slot)) > 0:
                    wins = True
        for bot_name, class_id, level in bots:
            if not _fits(held, class_id, BOT_RACE, level):
                continue
            for slot in legal:
                if _gain(held, worn.get(bot_name, {}).get(slot)) > 0:
                    wins = True
        if not wins and journal is not None and character:
            journal.mark_sell(character, held.item_id)
    sell_when_full(loop, world, journal, character)
    release_cursor(loop, world, journal)


def player_upgrade_slot(world: World, journal: Journal | None, character: str, item_id: int) -> int | None:
    """A worn slot where this piece is an upgrade for the player. None when a companion should have it."""
    held = _piece(item_id)
    player = (int(world.class_id or 0), int(world.race or 0), int(world.level or 1))
    if not _fits(held, player[0], player[1], player[2]):
        return None
    worn = _worn_map(world, journal, character).get("player", {})
    for slot in _legal_slots(held, world.refused_slots):
        if _gain(held, worn.get(slot)) > 0:
            return slot
    return None


def _loose(world: World) -> list[_Piece]:
    bags = world.bags or {}
    found: list[_Piece] = []
    for slot, item in bags.items():
        if int(slot) < 22:
            continue
        piece = _piece(item)
        piece.slot = slot
        if piece.item_id:
            found.append(piece)
    cursor = world.cursor
    if cursor:
        piece = _piece(cursor)
        piece.slot = CURSOR_SLOT
        if piece.item_id:
            found.append(piece)
    return found


def _offer_scribe(loop: Loop, world: World, journal: Journal | None) -> bool:
    """A spell scroll is written from the cursor. It is not parked in a bag."""
    if _cursor_busy(loop):
        return False
    spell_id, where = held_scroll(world)
    if not spell_id or known_spell(world, spell_id):
        return False
    slot = book_slot(world, where)
    if slot is None:
        return False
    source = f"scribe:{spell_id}"
    queue = loop.queue
    if queue is not None:
        for action in queue:
            if isinstance(action, ScribeSpell) and action.spell_id == spell_id and not action.complete:
                action.priority = SCRIBE_BAND
                return True
    action = ScribeSpell(spell_id, slot)
    action.priority = SCRIBE_BAND
    action.source = source
    _put(loop, world, journal, action)
    if queue is None:
        return False
    return any(isinstance(row, ScribeSpell) and row.spell_id == spell_id and not row.complete for row in queue)


def release_cursor(loop: Loop, world: World, journal: Journal | None = None) -> None:
    """The cursor is holding an item. A scroll is scribed. Anything else gets one move."""
    item_id = world.cursor or 0
    if not item_id or item_id == TOKEN:
        return
    if _cursor_busy(loop):
        return
    if _offer_scribe(loop, world, journal):
        return
    if journal is None:
        journal = loop.journal
    dest = _cursor_dest(world, _piece(item_id))
    if dest is None:
        return
    _start_move(loop, world, journal, CURSOR_SLOT, dest)


def _cursor_dest(world: World, piece: _Piece) -> int | None:
    player = (world.class_id or 1, world.race or 1, world.level or 1)
    worn: dict[int, _Piece] = {}
    for slot, item in (world.bags or {}).items():
        if slot <= 21 and item:
            worn[slot] = _piece(item)
    refused = world.refused_slots
    if _fits(piece, player[0], player[1], player[2]):
        for slot in _legal_slots(piece, refused):
            if _gain(piece, worn.get(slot)) > 0:
                return slot
    packed = _supply_slot(world, piece.item_id)
    if packed is not None:
        return packed
    bags = world.bags or {}
    for slot in range(22, 30):
        if slot in refused or bags.get(slot):
            continue
        return slot
    return None


FOOD = 14
DRINK = 15
BANDAGE = 18
_GENERAL_LO = 22
_GENERAL_HI = 30
_BAGS_BEGIN = 251
_BAG_STRIDE = 200
_SUBSLOTS = 10


def _stow_supplies(loop: Loop, world: World, journal: Journal | None) -> bool:
    """Food, water, and bandages leave the general slots once a backpack has room."""
    if _cursor_busy(loop):
        return False
    move = _supply_move(world, _craft_kits(loop))
    if move is None:
        return False
    _start_move(loop, world, journal, move[0], move[1])
    return _cursor_busy(loop)


def open_slot_for_kit(world: World, container_id: int) -> tuple[int, int] | None:
    """Put the combine kit on a general slot. A filled bag is never moved into another bag."""
    if container_id <= 0 or _kit_on_general(world, container_id):
        return None
    bags = world.bags or {}
    kit_slot = CURSOR_SLOT if world.cursor == container_id else 0
    if not kit_slot:
        for slot, item_id in bags.items():
            if int(item_id) == container_id:
                kit_slot = int(slot)
                break
    if not kit_slot:
        return None
    free = _open_general(world)
    if free is None:
        return _clear_general(world, container_id)
    if _GENERAL_LO <= kit_slot < _GENERAL_HI:
        return None
    return (kit_slot, free)


def _kit_on_general(world: World, container_id: int) -> bool:
    bags = world.bags or {}
    return any(int(bags.get(slot) or 0) == container_id for slot in range(_GENERAL_LO, _GENERAL_HI))


def _supply_move(world: World, kits: set[int]) -> tuple[int, int] | None:
    bags = world.bags or {}
    dest = _backpack_slot(world, kits)
    if dest is None:
        return None
    for slot in range(_GENERAL_LO, _GENERAL_HI):
        item_id = int(bags.get(slot) or 0)
        if _is_supply(item_id):
            return (slot, dest)
    if world.cursor and _is_supply(int(world.cursor)):
        return (CURSOR_SLOT, dest)
    return None


def _supply_slot(world: World, item_id: int, kits: set[int] | None = None) -> int | None:
    """A free slot inside a backpack. Kits and filled containers are not backpacks."""
    if not _is_supply(item_id):
        return None
    return _backpack_slot(world, kits or set())


def _backpack_slot(world: World, kits: set[int]) -> int | None:
    bags = world.bags or {}
    for parent in range(_GENERAL_LO, _GENERAL_HI):
        held = int(bags.get(parent) or 0)
        if held in kits or not _is_storage(held):
            continue
        dest = _free_subslot(world, parent)
        if dest is not None:
            return dest
    return None


def _clear_general(world: World, keep: int) -> tuple[int, int] | None:
    """Free a general slot. A container that already holds something stays where it is."""
    moved = _supply_move(world, {keep})
    if moved is not None and int((world.bags or {}).get(moved[0]) or 0) != keep:
        return moved
    bags = world.bags or {}
    for parent in range(_GENERAL_LO, _GENERAL_HI):
        parent_id = int(bags.get(parent) or 0)
        if parent_id == keep or parent_id <= 0 or _holds_items(world, parent):
            continue
        if not _is_storage(parent_id):
            continue
        for other in range(_GENERAL_LO, _GENERAL_HI):
            if other == parent:
                continue
            other_id = int(bags.get(other) or 0)
            if not _is_storage(other_id):
                continue
            dest = _free_subslot(world, other)
            if dest is not None:
                return (parent, dest)
    return None


def _open_general(world: World) -> int | None:
    bags = world.bags or {}
    for slot in range(_GENERAL_LO, _GENERAL_HI):
        if not bags.get(slot):
            return slot
    return None


def _free_subslot(world: World, parent: int) -> int | None:
    bags = world.bags or {}
    capacity = min(_bag_slots(int(bags.get(parent) or 0)), _SUBSLOTS)
    if capacity <= 0:
        return None
    start = _BAGS_BEGIN + (parent - _GENERAL_LO) * _BAG_STRIDE
    for slot in range(start, start + capacity):
        if not bags.get(slot):
            return slot
    return None


def _holds_items(world: World, parent: int) -> bool:
    if parent < _GENERAL_LO or parent >= _GENERAL_HI:
        return False
    if _bag_slots(int((world.bags or {}).get(parent) or 0)) <= 0:
        return False
    bags = world.bags or {}
    start = _BAGS_BEGIN + (parent - _GENERAL_LO) * _BAG_STRIDE
    return any(bags.get(slot) for slot in range(start, start + _SUBSLOTS))


def _craft_kits(loop: Loop) -> set[int]:
    found: set[int] = set()
    queue = loop.queue
    if queue is None:
        return found
    for action in queue:
        if not isinstance(action, Craft) or action.complete:
            continue
        container = int(action.recipe.container)
        if container:
            found.add(container)
    return found


def _is_supply(item_id: int) -> bool:
    return _item_type(item_id) in (FOOD, DRINK, BANDAGE)


def _is_storage(item_id: int) -> bool:
    return _bag_slots(item_id) > 0 and not _is_kit(item_id)


def _is_kit(item_id: int) -> bool:
    row = _facts(item_id) or {}
    return "kit" in str(row.get("name") or "").lower()


def _bag_slots(item_id: int) -> int:
    row = _facts(item_id) or {}
    return int(row.get("bagslots") or 0)


def _item_type(item_id: int) -> int:
    row = _facts(item_id) or {}
    return int(row.get("itemtype") or 0)


def _start_move(loop: Loop, world: World, journal: Journal | None, src: int, dest: int) -> None:
    if _cursor_busy(loop):
        return
    move = (src, dest)
    action = Cursor(dest, move)
    _put(loop, world, journal, action)
    if not _cursor_busy(loop):
        return
    action.source = f"cursor:{src}:{dest}"
    world.cursor_move = move


def _cursor_busy(loop: Loop) -> bool:
    queue = loop.queue
    if queue is None:
        return False
    for action in list(queue):
        if action.complete:
            continue
        if isinstance(action, (Cursor, Trade)):
            return True
    return False


def _worn_map(world: World, journal: Journal | None, character: str) -> dict[str, dict[int, _Piece]]:
    worn: dict[str, dict[int, _Piece]] = {"player": {}}
    bags = world.bags or {}
    for slot, item in bags.items():
        if int(slot) > 21 or not item:
            continue
        worn["player"][int(slot)] = _piece(item)
    if journal is not None and character:
        for bot_name, _class_id, _level in _bots(world, journal, character):
            slots = journal.worn(character, bot_name)
            worn[bot_name] = {int(slot): _piece(item_id) for slot, item_id in slots.items() if item_id}
    return worn


def _bots(world: World, journal: Journal | None, character: str) -> list[tuple[str, int, int]]:
    level = int(world.level or 1)
    found: list[tuple[str, int, int]] = []
    for bot in world.bots.roster:
        if isinstance(bot, tuple):
            name, class_id, bot_level = (
                bot[0],
                bot[1],
                bot[2] if len(bot) > 2 else level,
            )
            if name and class_id:
                found.append((str(name), int(class_id), int(bot_level or level)))
            continue
        if getattr(bot, "name", None) and getattr(bot, "class_id", None):
            found.append((bot.name, int(bot.class_id), int(getattr(bot, "level", None) or level)))
    if found or journal is None or not character:
        return found
    for name, class_id in journal.bots(character):
        found.append((str(name), int(class_id), level))
    return found


def _piece(item: int | object) -> _Piece:
    if isinstance(item, int):
        return _Piece(item, _facts(item))
    item_id = int(getattr(item, "item_id", 0) or 0)
    facts = dict(_facts(item_id) or {})
    for key in (
        "slots",
        "classes",
        "races",
        "nodrop",
        "ac",
        "damage",
        "req_level",
        "reqlevel",
        "hp",
        "mana",
        "slots",
    ):
        if hasattr(item, key):
            facts[key] = getattr(item, key)
    return _Piece(item_id, facts)


def _facts(item_id: int) -> dict | None:
    global _ITEMS
    if _ITEMS is None:
        _ITEMS = {}
        path = Path.home() / ".eqclient" / "items.jsonl"
        if path.is_file():
            with path.open(encoding="utf-8") as handle:
                for line in handle:
                    if '"item"' not in line:
                        continue
                    row = json.loads(line)
                    if row.get("kind") != "item":
                        continue
                    _ITEMS[int(row.get("item") or 0)] = row
    return _ITEMS.get(int(item_id))


def _gain(candidate: _Piece, worn: _Piece | None) -> int:
    if worn is None:
        return 1
    return _value(candidate) - _value(worn)


def _value(held: _Piece) -> int:
    stats = held.astr + held.asta + held.aagi + held.adex + held.awis + held.aint + held.acha
    vitals = held.hp // 4 + held.mana // 4
    return held.ac + held.damage + stats + vitals


def _legal_slots(held: _Piece, refused: set[int]) -> list[int]:
    return [slot for slot in WORN if slot not in refused and held.slots & (1 << slot)]


def _fits(held: _Piece, class_id: int, race_id: int, level: int) -> bool:
    if held.req_level and level < held.req_level:
        return False
    if not _allowed(held.classes, class_id) or not _allowed(held.races, race_id):
        return False
    return any((held.slots & 1 << slot for slot in WORN))


def _allowed(mask: int, index: int) -> bool:
    if index <= 0:
        return True
    if mask in (0, 65535, 32767, 4294967295):
        return mask != 0
    return bool(mask & 1 << index - 1)


def _protected(loop: Loop, world: World, journal: Journal | None, character: str, graph: QuestGraph | None) -> set[int]:
    """Quest ids, the obtain stack, the last 20 fetches, and what those fetches require."""
    found = set(_stack(journal, character))
    extra = world.quest_items or ()
    found.update((int(item) for item in extra))
    working = set(found)
    working.update(_recent_fetches(loop, journal, character))
    found.update(working)
    if graph is None:
        return found
    for edge in graph.edges or ():
        if edge.get("rel") not in {"gives", "receives", "needs"}:
            continue
        token = str(edge.get("to") or "")
        if token.startswith("item:"):
            try:
                found.add(int(token.split(":", 1)[1]))
            except ValueError:
                log.error("quest item token failed to parse: %s", token, exc_info=True)
                continue
    for item_id in working:
        found.update(graph.components(int(item_id)))
        given = graph.gives(int(item_id))
        group = str(given.get("group") or "") if given else ""
        found.update((piece for piece, _count in graph.receives_in(group)))
    return found


def _recent_fetches(loop: Loop, journal: Journal | None, character: str, limit: int = 20) -> list[int]:
    """Item ids from the newest fetches, queue first, then the journal."""
    found: list[int] = []
    seen: set[int] = set()
    queue = getattr(loop, "queue", None)
    rows = [action for action in list(queue or []) if type(action).__name__ == "Fetch"]
    rows.sort(key=lambda action: int(getattr(action, "insert", 0) or 0), reverse=True)
    for action in rows:
        _remember(found, seen, int(getattr(action, "item_id", 0) or 0), limit)
    if journal is not None and character and len(found) < limit:
        for item_id in journal.recent_fetch_ids(character, limit):
            _remember(found, seen, item_id, limit)
    return found


def _remember(found: list[int], seen: set[int], item_id: int, limit: int) -> None:
    if item_id <= 0 or item_id in seen or len(found) >= limit:
        return
    seen.add(item_id)
    found.append(item_id)


def _stack(journal: Journal | None, character: str) -> set[int]:
    if journal is None or not character:
        return set()
    return {int(item_id) for item_id, _count in journal.load_goals(character)}


@dataclass(frozen=True)
class _Handoff:
    piece: _Piece
    bot: str
    slot: int
    displaced: _Piece | None
    gain: int


def _best_handoff(
    remaining: list[_Piece],
    worn: dict[str, dict[int, _Piece]],
    bots: list[tuple[str, int, int]],
    refused: set[int],
    tried: set[tuple[int, str, int]],
) -> _Handoff | None:
    """The loose piece that most improves a companion. The piece it replaces is handed on."""
    best: _Handoff | None = None
    for held in remaining:
        for bot_name, class_id, level in bots:
            if not _fits(held, class_id, BOT_RACE, level):
                continue
            bot_worn = worn.get(bot_name, {})
            for slot in _legal_slots(held, refused):
                if (id(held), bot_name, slot) in tried:
                    continue
                current = bot_worn.get(slot)
                gain = _gain(held, current)
                if gain <= 0:
                    continue
                if best is not None and gain <= best.gain:
                    continue
                best = _Handoff(held, bot_name, slot, current, gain)
    return best


def _append_distribute(
    loop: Loop,
    world: World,
    journal: Journal | None,
    item_id: int,
    bot: str,
    slots: tuple[int, ...],
    rank: int = 0,
) -> None:
    source = f"distribute:{bot}:{item_id}"
    if _queued(loop, source):
        return
    action = Distribute(item_id, bot, slots)
    action.source = source
    action.priority = 220 - rank
    _put(loop, world, journal, action)


def mark_coin_loot(loop: Loop, world: World, journal: Journal | None, character: str, item_id: int) -> None:
    """A coin run keeps upgrades and quest pieces. Everything else is sold."""
    if journal is None or not character or item_id <= 0:
        return
    if item_id in _protected(loop, world, journal, character, None):
        return
    if _piece(item_id).nodrop == 0:
        return
    if improves_party(world, item_id, journal, character):
        return
    journal.mark_sell(character, item_id)


def improves_party(world: World, item_id: int, journal: Journal | None = None, character: str = "") -> bool:
    """True when the piece beats a worn slot for the player or a companion."""
    held = _piece(item_id)
    legal = _legal_slots(held, set())
    if not legal:
        return False
    worn = _worn_map(world, journal, character)
    player = (int(world.class_id or 0), int(world.race or 0), int(world.level or 1))
    if _fits(held, player[0], player[1], player[2]):
        for slot in legal:
            if _gain(held, worn.get("player", {}).get(slot)) > 0:
                return True
    for bot_name, class_id, level in _bots(world, journal, character):
        if not _fits(held, class_id, BOT_RACE, level):
            continue
        bot_worn = worn.get(bot_name, {})
        for slot in legal:
            if _gain(held, bot_worn.get(slot)) > 0:
                return True
    return False


def sell_when_full(loop: Loop, world: World, journal: Journal | None, character: str) -> bool:
    """Queue disposable stacks, and the extra copies of a queued combine, once the bags are full."""
    if empty_slots(world) > 0 or journal is None or not character:
        return False
    keep: dict[int, int] = {}
    item_ids: list[int] = []
    for item_id in sorted(journal.sell_marks(character)):
        if world.held(item_id) <= 0:
            continue
        item_ids.append(item_id)
        keep[item_id] = 0
    for item_id, need in _component_need(loop).items():
        if world.held(item_id) <= need:
            continue
        if item_id not in item_ids:
            item_ids.append(item_id)
        keep[item_id] = need
    if not item_ids:
        return False
    _append_sell(loop, world, journal, character, item_ids, keep)
    return True


def _component_need(loop: Loop) -> dict[int, int]:
    need: dict[int, int] = {}
    queue = loop.queue
    if queue is None:
        return need
    for action in queue:
        if not isinstance(action, Craft):
            continue
        for item_id, count in action.recipe.components:
            need[item_id] = need.get(item_id, 0) + count
    return need


def _append_sell(
    loop: Loop,
    world: World,
    journal: Journal | None,
    character: str,
    item_ids: list[int],
    keep: dict[int, int],
) -> None:
    source = "sell:" + ",".join((str(item_id) for item_id in item_ids))
    if _queued(loop, source):
        return
    action = Sell(item_ids, keep)
    action.source = source
    _put(loop, world, journal, action)


def _queued(loop: Loop, source: str) -> bool:
    queue = loop.queue
    if queue is None:
        return False
    if queue.has_source(source):
        return True
    return any((action.source == source for action in queue))


def _put(loop: Loop, world: World, journal: Journal | None, action: Action) -> None:
    queue = loop.queue
    if queue is None:
        return
    character = _character(loop, world)
    if isinstance(queue, list):
        queue.append(action)
        return
    try:
        queue.append(action, world, journal, character)
    except TypeError:
        log.error("queue append failed", exc_info=True)
        queue.append(action, world)


def _character(loop: Loop, world: World) -> str:
    from eqclient3.actions.support import character_name

    return character_name(loop, world)
