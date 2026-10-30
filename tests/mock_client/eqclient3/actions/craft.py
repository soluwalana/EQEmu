"""Band 0. Fetch missing components, then combine. OP_TradeSkillCombine completes it."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient3.loop import Loop
    from eqclient3.world import World

from eqclient3.action import Action
from eqclient3.data.recipes import Recipe, _WORLD_CONTAINER
from eqclient3.structs import OP_TradeSkillCombine
from eqclient3.actions.fetch import Fetch
from eqclient3.actions.support import yield_to

# A world station combines in this slot. A kit combines in the bag slot that holds it.
WORLD_COMBINE = 1000


class Craft(Action):

    def __init__(self, recipe: Recipe) -> None:
        super().__init__()
        self.priority = 0
        self.durable = True
        self.recipe = recipe
        self.active_path = None
        self.sent = False

    def opcodes(self) -> tuple[str, ...]:
        return ("OP_TradeSkillCombine",)

    def suspend(self) -> None:
        self.active_path = None
        self.suspended = True

    def step(self, loop: Loop, world: World) -> None:
        if self.consume("OP_TradeSkillCombine"):
            self.unwait("CRAFT")
            self.complete = True
            return
        if self.waiting_for("CRAFT") and (not self.messages):
            return
        self.suspended = False
        missing = _missing(world, self.recipe)
        if missing is not None:
            item_id, count = missing
            yield_to(
                self,
                loop,
                world,
                Fetch(item_id, count, f"craft {item_id}"),
                f"fetch:{item_id}",
            )
            return
        loop.send(
            "OP_TradeSkillCombine",
            OP_TradeSkillCombine(_combine_slot(world, self.recipe)).serialize(),
        )
        self.sent = True
        self.wait("CRAFT")


def _missing(world: World, recipe: Recipe) -> tuple[int, int] | None:
    for item_id, count in recipe.components:
        if world.held(item_id) < count:
            return (item_id, count)
    return None


def _combine_slot(world: World, recipe: Recipe) -> int:
    if recipe.container in _WORLD_CONTAINER:
        return WORLD_COMBINE
    if not recipe.container:
        return 0
    for slot, item_id in world.bags.items():
        if item_id == recipe.container:
            return slot
    return 0
