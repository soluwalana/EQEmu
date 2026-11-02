"""Fetch the container and the components, combine, and try again when it fails.

A kit combine moves each component into the kit first. The server eats those
components before it rolls the skill. The empty OP_TradeSkillCombine is only
the acknowledgement. String 336 is the failure. The result in hand is the success.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient3.action import Message
    from eqclient3.loop import Loop
    from eqclient3.world import World

from eqclient3.action import Action
from eqclient3.actions.practice import Practice
from eqclient3.data.recipes import Recipe, _WORLD_CONTAINER
from eqclient3.structs import OP_MoveItem, OP_SimpleMessage, OP_TradeSkillCombine
from eqclient3.actions.support import CURSOR_SLOT, yield_to

# A world station combines in this slot. A kit combines in the bag slot that holds it.
WORLD_COMBINE = 1000
# RoF2 first general-bag slot, and how many slots each general bag occupies.
_BAGS_BEGIN = 251
_BAG_STRIDE = 200
_GENERAL = 22
_SUBSLOTS = 10
# zone/string_ids.h TRADESKILL_FAILED. The success line is a formatted message.
_FAILED = 336


class Craft(Action):

    def __init__(self, recipe: Recipe, count: int = 1) -> None:
        super().__init__()
        self.priority = 0
        self.durable = True
        self.recipe = recipe
        self.count = count
        self.active_path = None
        self.sent = False
        self.based = False
        self.origin = 0
        self.saw_ack = False
        self.practicing = False

    def __setstate__(self, state: dict[str, object]) -> None:
        self.__dict__.update(state)
        if "count" not in self.__dict__:
            self.count = 1
        if "based" not in self.__dict__:
            self.based = False
        if "origin" not in self.__dict__:
            self.origin = 0
        if "saw_ack" not in self.__dict__:
            self.saw_ack = False
        if "practicing" not in self.__dict__:
            self.practicing = False

    def opcodes(self) -> tuple[str, ...]:
        return ("OP_TradeSkillCombine", "OP_SimpleMessage", "OP_ItemPacket", "OP_DeleteItem")

    def suspend(self) -> None:
        self.active_path = None
        self.suspended = True

    def step(self, loop: Loop, world: World) -> None:
        if not self.based:
            self.origin = world.held(self.recipe.result)
            self.based = True
        if world.held(self.recipe.result) >= self.origin + self.count:
            self.complete = True
            return
        if self.waiting_for("CRAFT"):
            failed = self.consume("OP_SimpleMessage", _failed) is not None
            acked = self.consume("OP_TradeSkillCombine") is not None
            if world.held(self.recipe.result) >= self.origin + self.count:
                self.complete = True
                return
            if failed:
                self.saw_ack = False
                self.unwait("CRAFT")
                self.sent = False
            elif acked and not self.saw_ack:
                self.saw_ack = True
                return
            elif self.saw_ack:
                self.saw_ack = False
                self.unwait("CRAFT")
                self.sent = False
            else:
                return
        if self.waiting_for("MOVE"):
            if self.consume("OP_ItemPacket") is None and self.consume("OP_DeleteItem") is None:
                return
            self.unwait("MOVE")
        self.suspended = False
        if not self.practicing and _practice_first(self, loop, world):
            return
        if self.recipe.container and self.recipe.container not in _WORLD_CONTAINER:
            # assign imports Craft, so the kit check waits until this step runs.
            from eqclient3.inventory.assign import open_slot_for_kit

            opening = open_slot_for_kit(world, self.recipe.container)
            if opening is not None:
                loop.send("OP_MoveItem", OP_MoveItem(opening[0], opening[1]).serialize())
                self.wait("MOVE")
                self.suspended = False
                return
            if world.held(self.recipe.container) and not _kit_on_general(world, self.recipe.container):
                return
        missing = _missing(world, self.recipe)
        if missing is not None:
            item_id, count = missing
            # Fetch imports the talk chain, and that chain imports inventory, which imports Craft.
            from eqclient3.actions.fetch import Fetch

            fetch = Fetch(item_id, count, f"craft {item_id}")
            fetch.priority = self.priority
            yield_to(self, loop, world, fetch, f"craft:{self.recipe.id}:{item_id}")
            return
        move = _place(world, self.recipe)
        if move is not None:
            loop.send("OP_MoveItem", OP_MoveItem(move[0], move[1]).serialize())
            self.wait("MOVE")
            self.suspended = False
            return
        loop.send(
            "OP_TradeSkillCombine",
            OP_TradeSkillCombine(_combine_slot(world, self.recipe)).serialize(),
        )
        self.sent = True
        self.wait("CRAFT")


def _practice_first(action: Craft, loop: Loop, world: World) -> bool:
    """Queue practice when this combine is still below its trivial. The drill does not."""
    short = _skill_short(world, action.recipe)
    if short is None:
        return False
    skill_id, want = short
    practice = Practice(skill_id, want, action.recipe.id, _protect(action.recipe))
    practice.priority = action.priority
    source = f"practice:{action.recipe.id}"
    if yield_to(action, loop, world, practice, source):
        return True
    queue = loop.queue
    if queue is not None and queue.has_source(source):
        action.yielding = True
        return True
    return False


def _skill_short(world: World, recipe: Recipe) -> tuple[int, int] | None:
    skill = recipe.skill
    if not skill:
        return None
    want = max(recipe.skillneeded, recipe.trivial)
    if want <= 0:
        return None
    if world.skills.get(skill, 0) >= want:
        return None
    return (skill, want)


def _protect(recipe: Recipe) -> tuple[int, ...]:
    kept = [item_id for item_id, _count in recipe.components]
    kept.append(recipe.result)
    if recipe.container:
        kept.append(recipe.container)
    return tuple(kept)


def _failed(message: Message) -> bool:
    return _string_id(message) == _FAILED


def _string_id(message: Message | None) -> int:
    if message is None:
        return 0
    payload = message.payload
    if not isinstance(payload, OP_SimpleMessage):
        return 0
    return int(payload.string_id)


def _missing(world: World, recipe: Recipe) -> tuple[int, int] | None:
    """The container, then the first component we are short, including the pattern."""
    container = recipe.container
    if container and container not in _WORLD_CONTAINER and world.held(container) < 1:
        return (container, 1)
    for item_id, count in recipe.components:
        if world.held(item_id) < count:
            return (item_id, count)
    return None


def _combine_slot(world: World, recipe: Recipe) -> int:
    if recipe.container in _WORLD_CONTAINER:
        return WORLD_COMBINE
    if not recipe.container:
        return 0
    found = 0
    for slot, item_id in world.bags.items():
        if int(item_id) != recipe.container:
            continue
        slot_id = int(slot)
        if _GENERAL <= slot_id < _GENERAL + 8:
            return slot_id
        found = slot_id
    return found


def _kit_on_general(world: World, container_id: int) -> bool:
    bags = world.bags or {}
    return any(int(bags.get(slot) or 0) == container_id for slot in range(_GENERAL, _GENERAL + 8))


def _place(world: World, recipe: Recipe) -> tuple[int, int] | None:
    """Move one component into the kit. None when the kit is ready or this is not a kit."""
    container = recipe.container
    if not container or container in _WORLD_CONTAINER:
        return None
    parent = _combine_slot(world, recipe)
    if parent < _GENERAL or parent >= _GENERAL + 8:
        return None
    inside = _subslots(parent)
    for item_id, count in recipe.components:
        if _count(world, inside, item_id) >= count:
            continue
        source = _outside(world, inside, item_id)
        dest = _free(world, inside)
        if source is None or dest is None:
            return None
        return (source, dest)
    return None


def _subslots(parent: int) -> range:
    start = _BAGS_BEGIN + (parent - _GENERAL) * _BAG_STRIDE
    return range(start, start + _SUBSLOTS)


def _count(world: World, slots: range, item_id: int) -> int:
    return sum(1 for slot in slots if world.bags.get(slot) == item_id)


def _outside(world: World, slots: range, item_id: int) -> int | None:
    held = set(slots)
    for slot, found in world.bags.items():
        if found == item_id and int(slot) not in held:
            return int(slot)
    if world.cursor == item_id:
        return CURSOR_SLOT
    return None


def _free(world: World, slots: range) -> int | None:
    for slot in slots:
        if not world.bags.get(slot):
            return slot
    return None
