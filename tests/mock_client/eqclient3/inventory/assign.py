"""One pass over loose gear. The player upgrades first, then each bot.

An upgrade for the player queues Cursor, which sends OP_MoveItem. An upgrade
for a bot appends Distribute with the worn piece emptied first. A fill appends
Distribute as a give. A leftover no bot can wear, that loses every slot, appends
Sell unless it is a quest id, no-drop, or still on the obtain stack. A cursor
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
from pathlib import Path
from eqclient3.log import log
from eqclient3.actions.cursor import Cursor
from eqclient3.actions.distribute import Distribute
from eqclient3.actions.sell import Sell
from eqclient3.actions.support import CURSOR_SLOT, TOKEN
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
        self.slots = int(raw.get('slots') or 0)
        self.classes = int(raw.get('classes') or 0)
        self.races = int(raw.get('races') or 0)
        self.req_level = int(raw.get('reqlevel') or raw.get('req_level') or 0)
        self.ac = int(raw.get('ac') or 0)
        self.damage = int(raw.get('damage') or 0)
        self.astr = int(raw.get('astr') or 0)
        self.asta = int(raw.get('asta') or 0)
        self.aagi = int(raw.get('aagi') or 0)
        self.adex = int(raw.get('adex') or 0)
        self.awis = int(raw.get('awis') or 0)
        self.aint = int(raw.get('aint') or 0)
        self.acha = int(raw.get('acha') or 0)
        self.hp = int(raw.get('hp') or 0)
        self.mana = int(raw.get('mana') or 0)
        self.nodrop = int(raw.get('nodrop') if raw.get('nodrop') is not None else 255)
        self.slot = int(raw.get('slot') or 0)

def assign(loop: Loop, world: World, journal: Journal | None = None, *, applied: bool=True, graph: QuestGraph | None = None) -> None:
    """Player upgrades, then bot Distribute, then Sell. applied=False does nothing."""
    if not applied:
        return
    loose = _loose(world)
    if not loose:
        return
    character = _character(loop, world)
    protected = _protected(loop, world, journal, character, graph)
    stack = _stack(journal, character)
    player = (int(world.class_id or 1), int(world.race or 1), int(world.level or 1))
    worn = _worn_map(world, journal, character)
    player_worn = worn.setdefault('player', {})
    remaining = list(loose)
    moved = _cursor_busy(loop)
    for held in list(remaining):
        if held.item_id in protected or held.item_id in stack:
            continue
        if not _fits(held, player[0], player[1], player[2]):
            continue
        for slot in _legal_slots(held):
            if _gain(held, player_worn.get(slot)) > 0:
                if not moved:
                    _start_move(loop, world, journal, held.slot, slot)
                    moved = True
                remaining.remove(held)
                player_worn[slot] = held
                break
    bots = _bots(world, journal, character)
    candidates: list[tuple[int, _Piece, str, int, bool]] = []
    for held in remaining:
        for bot_name, class_id, level in bots:
            if not _fits(held, class_id, BOT_RACE, level):
                continue
            bot_worn = worn.get(bot_name, {})
            for slot in _legal_slots(held):
                current = bot_worn.get(slot)
                gain = _gain(held, current)
                if gain <= 0:
                    continue
                candidates.append((gain, held, bot_name, slot, current is not None))
    candidates.sort(key=lambda row: -row[0])
    used: set[tuple[str, int]] = set()
    taken: set[int] = set()
    for _gain_value, held, bot_name, slot, occupied in candidates:
        if id(held) in taken or (bot_name, slot) in used:
            continue
        slots: list[int] = []
        if occupied:
            slots.append(slot)
        if held.slots & _TWO_HAND and slot == PRIMARY:
            slots.append(SECONDARY)
            used.add((bot_name, SECONDARY))
        _append_distribute(loop, world, journal, held.item_id, bot_name, tuple(slots))
        used.add((bot_name, slot))
        taken.add(id(held))
        worn.setdefault(bot_name, {})[slot] = held
        remaining.remove(held)
    sell_ids: list[int] = []
    cursor_id = world.cursor or 0
    for held in remaining:
        if cursor_id and held.item_id == cursor_id:
            continue
        if held.item_id in protected or held.item_id in stack or held.nodrop == 0:
            continue
        anyone = False
        wins = False
        for bot_name, class_id, level in bots:
            if not _fits(held, class_id, BOT_RACE, level):
                continue
            anyone = True
            for slot in _legal_slots(held):
                if _gain(held, worn.get(bot_name, {}).get(slot)) > 0:
                    wins = True
        if not anyone or not wins:
            sell_ids.append(held.item_id)
    if sell_ids:
        _append_sell(loop, world, journal, character, sell_ids)
    release_cursor(loop, world, journal)

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

def release_cursor(loop: Loop, world: World, journal: Journal | None = None) -> None:
    """The cursor is holding an item. One move goes on the queue."""
    item_id = world.cursor or 0
    if not item_id or item_id == TOKEN:
        return
    if _cursor_busy(loop):
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
    if _fits(piece, player[0], player[1], player[2]):
        for slot in _legal_slots(piece):
            if _gain(piece, worn.get(slot)) > 0:
                return slot
    bags = world.bags or {}
    for slot in range(22, 30):
        if not bags.get(slot):
            return slot
    return None

def _start_move(loop: Loop, world: World, journal: Journal | None, src: int, dest: int) -> None:
    if _cursor_busy(loop):
        return
    move = (src, dest)
    action = Cursor(dest, move)
    _put(loop, world, journal, action)
    if not _cursor_busy(loop):
        return
    action.source = f'cursor:{src}:{dest}'
    world.cursor_move = move

def _cursor_busy(loop: Loop) -> bool:
    queue = loop.queue
    if queue is None:
        return False
    for action in list(queue):
        if type(action).__name__ == 'Cursor' and not action.complete:
            return True
    return False

def _worn_map(world: World, journal: Journal, character: str) -> dict[str, dict[int, _Piece]]:
    worn: dict[str, dict[int, _Piece]] = {'player': {}}
    bags = world.bags or {}
    for slot, item in bags.items():
        if int(slot) > 21 or not item:
            continue
        worn['player'][int(slot)] = _piece(item)
    if journal is not None and character:
        for bot_name, _class_id, _level in _bots(world, journal, character):
            slots = journal.worn(character, bot_name)
            worn[bot_name] = {int(slot): _piece(item_id) for slot, item_id in slots.items() if item_id}
    return worn

def _bots(world: World, journal: Journal, character: str) -> list[tuple[str, int, int]]:
    level = int(world.level or 1)
    found: list[tuple[str, int, int]] = []
    for bot in world.bots.roster:
        if isinstance(bot, tuple):
            name, class_id, bot_level = bot[0], bot[1], bot[2] if len(bot) > 2 else level
            if name and class_id:
                found.append((str(name), int(class_id), int(bot_level or level)))
            continue
        if getattr(bot, 'name', None) and getattr(bot, 'class_id', None):
            found.append((bot.name, int(bot.class_id), int(getattr(bot, 'level', None) or level)))
    if found or journal is None or not character:
        return found
    for name, class_id in journal.bots(character):
        found.append((str(name), int(class_id), level))
    return found

def _piece(item: int | object) -> _Piece:
    if isinstance(item, int):
        return _Piece(item, _facts(item))
    item_id = int(getattr(item, 'item_id', 0) or 0)
    facts = dict(_facts(item_id) or {})
    for key in ('slots', 'classes', 'races', 'nodrop', 'ac', 'damage', 'req_level', 'reqlevel', 'hp', 'mana'):
        if hasattr(item, key):
            facts[key] = getattr(item, key)
    return _Piece(item_id, facts)

def _facts(item_id: int) -> dict | None:
    global _ITEMS
    if _ITEMS is None:
        _ITEMS = {}
        path = Path.home() / '.eqclient' / 'items.jsonl'
        if path.is_file():
            with path.open(encoding='utf-8') as handle:
                for line in handle:
                    if '"item"' not in line:
                        continue
                    row = json.loads(line)
                    if row.get('kind') != 'item':
                        continue
                    _ITEMS[int(row.get('item') or 0)] = row
    return _ITEMS.get(int(item_id))

def _gain(candidate: _Piece, worn: _Piece | None) -> int:
    if worn is None:
        return 1
    return _value(candidate) - _value(worn)

def _value(held: _Piece) -> int:
    stats = held.astr + held.asta + held.aagi + held.adex + held.awis + held.aint + held.acha
    vitals = held.hp // 4 + held.mana // 4
    return held.ac + held.damage + stats + vitals

def _legal_slots(held: _Piece) -> list[int]:
    return [slot for slot in WORN if held.slots & 1 << slot]

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

def _protected(loop: Loop, world: World, journal: Journal, character: str, graph: QuestGraph) -> set[int]:
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
        if edge.get('rel') not in {'gives', 'receives', 'needs'}:
            continue
        token = str(edge.get('to') or '')
        if token.startswith('item:'):
            try:
                found.add(int(token.split(':', 1)[1]))
            except ValueError:
                log.error("quest item token failed to parse: %s", token, exc_info=True)
                continue
    for item_id in working:
        found.update(graph.components(int(item_id)))
        edge = graph.gives(int(item_id))
        group = str(edge.get('group') or '') if edge else ''
        found.update((piece for piece, _count in graph.receives_in(group)))
    return found


def _recent_fetches(loop: Loop, journal: Journal, character: str, limit: int = 20) -> list[int]:
    """Item ids from the newest fetches, queue first, then the journal."""
    found: list[int] = []
    seen: set[int] = set()
    queue = getattr(loop, 'queue', None)
    rows = [action for action in list(queue or []) if type(action).__name__ == 'Fetch']
    rows.sort(key=lambda action: int(getattr(action, 'insert', 0) or 0), reverse=True)
    for action in rows:
        _remember(found, seen, int(getattr(action, 'item_id', 0) or 0), limit)
    if journal is not None and character and len(found) < limit:
        for item_id in journal.recent_fetch_ids(character, limit):
            _remember(found, seen, item_id, limit)
    return found


def _remember(found: list[int], seen: set[int], item_id: int, limit: int) -> None:
    if item_id <= 0 or item_id in seen or len(found) >= limit:
        return
    seen.add(item_id)
    found.append(item_id)

def _stack(journal: Journal, character: str) -> set[int]:
    if journal is None or not character:
        return set()
    return {int(item_id) for item_id, _count in journal.load_goals(character)}

def _append_distribute(loop: Loop, world: World, journal: Journal, item_id: int, bot: str, slots: tuple[int, ...]) -> None:
    source = f'distribute:{bot}:{item_id}'
    if _queued(loop, source):
        return
    action = Distribute(item_id, bot, slots)
    action.source = source
    _put(loop, world, journal, action)

def _append_sell(loop: Loop, world: World, journal: Journal, character: str, item_ids: list[int]) -> None:
    source = 'sell:' + ','.join((str(item_id) for item_id in item_ids))
    if _queued(loop, source):
        return
    action = Sell(item_ids)
    action.source = source
    _put(loop, world, journal, action)
    if journal is not None and character:
        for item_id in item_ids:
            journal.mark_sell(character, item_id)

def _queued(loop: Loop, source: str) -> bool:
    queue = loop.queue
    if queue is None:
        return False
    if queue.has_source(source):
        return True
    return any((action.source == source for action in queue))

def _put(loop: Loop, world: World, journal: Journal, action: Action) -> None:
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
