"""Fill a graph-edge goal that has no steps, and the work that follows the tutorial.

ReadTasks calls this as the character leaves tutorialb. A Fetch whose item is a
quest reward calls it too. It appends the epic graph, one Fetch per kit piece,
a Kill, and a level camp. A resolved source is skipped. Nothing is appended
while the tutorial ReadTasks is still open in tutorialb.

This module does not import the loop. The caller passes the loop, and new work
goes on loop.queue.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterator
    from eqclient3.action import Action
    from eqclient3.journal import Journal
    from eqclient3.loop import Loop
    from eqclient3.world import World

from eqclient3.log import log
from eqclient3.actions.craft import Craft
from eqclient3.actions.fetch import Fetch, item_cost
from eqclient3.data.recipes import DEFAULT_RECIPES, Recipe, read_recipes
from eqclient3.actions.kill import Kill
from eqclient3.camps import camp_for_level
from eqclient3.quests.expand import expand, produced
from eqclient3.quests.graph import QuestGraph, load_graph

_EPIC = {
    1: 60329,
    2: 20076,
    3: 64031,
    4: 62649,
    5: 48136,
    6: 62863,
    7: 67742,
    8: 77640,
    9: 52348,
    10: 57405,
    11: 64067,
    12: 16576,
    13: 19839,
    14: 52952,
    15: 52911,
    16: 18609,
}
_CLOTH = (1001, 1004, 1008, 1010)
_LEATHER = (2001, 2004, 2008, 2010)
_BANDED = (3053, 3056, 3060, 3063)
_WEAPON = {
    1: 5013,
    2: 6011,
    3: 5013,
    4: 5013,
    5: 5013,
    6: 6011,
    8: 7007,
    9: 7007,
    10: 6011,
    11: 7007,
    12: 7007,
    13: 7007,
    14: 7007,
    15: 5013,
    16: 5023,
}
_CLOTH_CLASSES = {2, 11, 12, 13, 14}
_LEATHER_CLASSES = {4, 7, 8, 9, 15}
_graph: QuestGraph | None = None


def produce(
    loop: Loop,
    world: World,
    journal: Journal | None = None,
    *,
    item_id: int | None = None,
    graph: QuestGraph | None = None,
    leaving_tutorial: bool = False,
) -> None:
    """Append the next quest work. An open ReadTasks in tutorialb returns immediately."""
    if _tutorial_open(loop, world, journal):
        return
    book = graph if graph is not None else _cached_graph()
    character = _character(loop, world)
    if leaving_tutorial or (item_id is not None and _is_reward(book, int(item_id))):
        _after_tutorial(loop, world, journal, book, character)
    if item_id is not None:
        _fill_item(loop, world, journal, book, character, int(item_id))
    _fill_goals(loop, world, journal, book, character)


def _after_tutorial(
    loop: Loop, world: World, journal: Journal | None, graph: QuestGraph | None, character: str
) -> None:
    _queue_backpacks(loop, world, journal)
    world.quest_started = True
    if journal is not None and character:
        journal.set_flag(character, "quest_started", 1)
    class_id = int(world.class_id or 0)
    level = int(world.level or 1)
    here = str(world.zone or "")
    epic_id = _EPIC.get(class_id, 0)
    if epic_id and _can_obtain(epic_id, class_id, int(world.race or 0), graph):
        _fill_item(
            loop,
            world,
            journal,
            graph,
            character,
            epic_id,
            source=f"goal:item={epic_id}",
        )
    held = _held(world)
    for piece in _kit_ids(world, class_id, level):
        if piece in held:
            continue
        _append_fetch(loop, world, journal, piece, f"gear:{piece}")
    camp = camp_for_level(level, here)
    camp_zone = camp.zone if camp is not None else here or "qeynos"
    _append_kill(loop, world, journal, camp=camp_zone, level=None, source="kill:after_tutorial")
    _append_kill(
        loop,
        world,
        journal,
        camp=camp_zone,
        level=max(level, 1) + 1,
        source=f"level:{camp_zone}",
    )


def _fill_goals(loop: Loop, world: World, journal: Journal | None, graph: QuestGraph | None, character: str) -> None:
    if journal is None or not character:
        return
    goals = journal.load_goals(character)
    if not goals:
        return
    item_id = int(goals[-1][0])
    _fill_item(loop, world, journal, graph, character, item_id, source=f"goal:item={item_id}")


def _fill_item(
    loop: Loop,
    world: World,
    journal: Journal | None,
    graph: QuestGraph | None,
    character: str,
    item_id: int,
    source: str = "",
) -> None:
    if graph is None:
        return
    edge = graph.gives(item_id) or produced(graph, item_id)
    if edge is None:
        return
    label = source or f"goal:item={item_id}"
    if _already(loop, journal, character, label):
        return
    here = str(world.zone or "")
    for action in expand(edge, here=here, graph=graph, source=label):
        if _skipped(loop, journal, character, action.source):
            continue
        _put(loop, world, journal, action)


# One container in each general slot. The handmade pack is crafted. The other two are bought.
# Counts are 2 + 3 + 3. Normal fetches are 0, so these sit one above them.
BACKPACK_BAND = 1
GENERAL_SLOTS = 8
HANDMADE = 17969
BACKPACKS = (
    (HANDMADE, 2),
    (17005, 3),
    (17046, 3),
)
_HANDMADE: Recipe | None = None
_HANDMADE_TRIED = False


def _queue_backpacks(loop: Loop, world: World, journal: Journal | None) -> None:
    free = _free_general(world)
    if free <= 0:
        return
    planned: list[tuple[int, int]] = []
    for item_id, want in BACKPACKS:
        need = min(free, max(0, want - world.held(item_id)))
        if need <= 0:
            continue
        planned.append((item_id, need))
        free -= need
    buys = [(item_id, count) for item_id, count in planned if item_id != HANDMADE]
    made = [(item_id, count) for item_id, count in planned if item_id == HANDMADE]
    for item_id, count in buys:
        _queue_buy(loop, world, journal, item_id, count)
    for _item_id, count in made:
        _queue_handmade(loop, world, journal, count)


def _queue_buy(loop: Loop, world: World, journal: Journal | None, item_id: int, count: int) -> None:
    source = f"backpack:{item_id}"
    if _skipped(loop, journal, _character(loop, world), source):
        return
    action = Fetch(item_id, count, f"backpack {item_id}", copper=item_cost(item_id))
    action.source = source
    action.priority = BACKPACK_BAND
    _put(loop, world, journal, action)


def _queue_handmade(loop: Loop, world: World, journal: Journal | None, count: int) -> None:
    source = f"backpack:{HANDMADE}"
    if _skipped(loop, journal, _character(loop, world), source):
        return
    recipe = _handmade_recipe()
    if recipe is None:
        _queue_buy(loop, world, journal, HANDMADE, count)
        return
    action = Craft(recipe, count)
    action.source = source
    action.priority = BACKPACK_BAND
    _put(loop, world, journal, action)


def _handmade_recipe() -> Recipe | None:
    global _HANDMADE, _HANDMADE_TRIED
    if _HANDMADE_TRIED:
        return _HANDMADE
    _HANDMADE_TRIED = True
    _HANDMADE = read_recipes(DEFAULT_RECIPES).for_item(HANDMADE)
    return _HANDMADE


def _free_general(world: World) -> int:
    bags = world.bags or {}
    used = sum(1 for slot in range(22, 22 + GENERAL_SLOTS) if bags.get(slot))
    return GENERAL_SLOTS - used


def _append_fetch(loop: Loop, world: World, journal: Journal | None, item_id: int, source: str) -> None:
    if _skipped(loop, journal, _character(loop, world), source):
        return
    action = Fetch(item_id, 1, str(item_id))
    action.source = source
    _put(loop, world, journal, action)


def _append_kill(
    loop: Loop,
    world: World,
    journal: Journal | None,
    *,
    camp: str,
    level: int | None,
    source: str,
) -> None:
    if _skipped(loop, journal, _character(loop, world), source):
        return
    action = Kill(camp=camp, level=level)
    action.source = source
    _put(loop, world, journal, action)


def _put(loop: Loop, world: World, journal: Journal | None, action: Action) -> None:
    queue = loop.queue
    if queue is None:
        return
    character = _character(loop, world)
    try:
        queue.append(action, world, journal, character)
    except TypeError:
        queue.append(action, world)


def _tutorial_open(loop: Loop, world: World, journal: Journal | None) -> bool:
    zone = str(world.zone or "").lower()
    if zone != "tutorialb":
        return False
    for action in _actions(loop):
        if action.complete:
            continue
        if type(action).__name__ == "ReadTasks" or action.source == "read_tasks:tutorialb":
            return True
    character = _character(loop, world)
    if journal is not None and character:
        return bool(journal.is_open(character, "read_tasks:tutorialb"))
    return False


def _already(loop: Loop, journal: Journal | None, character: str, source: str) -> bool:
    """True when this goal already has a step queued or the source itself is resolved."""
    if _skipped(loop, journal, character, source):
        return True
    prefix = source + "#"
    for action in _actions(loop):
        current = str(action.source or "")
        if current == source or current.startswith(prefix):
            return True
    if journal is not None and character:
        for done in journal.resolved_sources(character):
            if done == source or str(done).startswith(prefix):
                return True
    return False


def _skipped(loop: Loop, journal: Journal | None, character: str, source: str) -> bool:
    if not source:
        return False
    for action in _actions(loop):
        if action.source == source:
            return True
    if journal is None or not character:
        return False
    if journal.is_resolved(character, source):
        return True
    if journal.is_open(character, source):
        return True
    return False


def _actions(loop: Loop) -> Iterator[Action]:
    queue = loop.queue
    if queue is None:
        return
    current = getattr(loop, "current", None)
    if current is not None:
        yield current
    yield from queue


def _character(loop: Loop, world: World) -> str:
    from eqclient3.actions.support import character_name

    return character_name(loop, world)


def _held(world: World) -> set[int]:
    found = {int(item) for item in world.bags.values() if item}
    cursor = world.cursor
    if cursor:
        found.add(int(cursor))
    return found


def _is_reward(graph: QuestGraph | None, item_id: int) -> bool:
    return graph is not None and graph.gives(item_id) is not None


def _can_obtain(item_id: int, class_id: int, race_id: int, graph: QuestGraph | None) -> bool:
    if item_id <= 0 or class_id <= 0:
        return False
    if graph is None:
        return True
    info = graph.items.get(item_id) or {}
    classes = info.get("classes") or ()
    races = info.get("races") or ()
    if classes and int(class_id) not in {int(c) for c in classes}:
        return False
    if races and race_id and (int(race_id) not in {int(r) for r in races}):
        return False
    return True


def _kit_ids(world: World, class_id: int, level: int) -> list[int]:
    classes = [class_id]
    roster = world.bots.roster or ()
    for bot in roster:
        if isinstance(bot, tuple) and len(bot) > 1:
            classes.append(int(bot[1]))
        else:
            cid = bot.class_id
            if cid:
                classes.append(int(cid))
    found: list[int] = []
    seen: set[int] = set()
    for cid in classes:
        if cid in seen or cid <= 0:
            continue
        seen.add(cid)
        for item_id in _kit_for(cid, level):
            if item_id not in found:
                found.append(item_id)
    return found


def _kit_for(class_id: int, level: int) -> list[int]:
    items: list[int] = []
    weapon = _WEAPON.get(class_id, 0)
    if weapon:
        items.append(weapon)
    if level >= 31:
        armor = _BANDED
    elif class_id in _CLOTH_CLASSES:
        armor = _CLOTH
    elif class_id in _LEATHER_CLASSES or level < 11:
        armor = _LEATHER
    else:
        armor = _BANDED if level >= 11 else _LEATHER
    items.extend(armor[:4])
    return items


def _cached_graph() -> QuestGraph | None:
    global _graph
    if _graph is None:
        try:
            _graph = load_graph()
        except OSError:
            log.error("quest graph failed to load", exc_info=True)
            return None
    return _graph
