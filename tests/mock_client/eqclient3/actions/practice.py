"""Combine practice recipes until a tradeskill reaches the goal recipe's trivial.

Skill only rises while it is below the combine's trivial. The goal recipe is
skipped so its pattern and components stay for the real combine. Each drill
makes one result, which is marked to sell unless the goal still needs it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Protocol, runtime_checkable

if TYPE_CHECKING:
    from eqclient3.loop import Loop
    from eqclient3.world import World

from eqclient3.action import Action
from eqclient3.data.recipes import DEFAULT_RECIPES, Recipe, RecipeBook, read_recipes
from eqclient3.actions.support import character_name, journal_of, yield_to

_BOOK: RecipeBook | None = None


class Practice(Action):

    def __init__(self, skill_id: int, want: int, skip: int = 0, protect: tuple[int, ...] = ()) -> None:
        super().__init__()
        self.priority = 0
        self.durable = True
        self.skill_id = skill_id
        self.want = want
        self.skip = skip
        self.protect = protect

    def __setstate__(self, state: dict[str, object]) -> None:
        self.__dict__.update(state)
        if "skip" not in self.__dict__:
            self.skip = 0
        if "protect" not in self.__dict__:
            self.protect = ()

    def opcodes(self) -> tuple[str, ...]:
        return ("OP_SkillUpdate",)

    def suspend(self) -> None:
        self.suspended = True

    def step(self, loop: Loop, world: World) -> None:
        if world.skills.get(self.skill_id, 0) >= self.want:
            self.complete = True
            return
        if _drill_open(loop):
            self.yielding = True
            return
        book = load_book()
        recipe = book.practice(self.skill_id, world.skills.get(self.skill_id, 0), self.want, self.skip)
        if recipe is None:
            self.complete = True
            return
        self.suspended = False
        _mark_result(loop, world, recipe, self.protect)
        # Craft imports Practice. The drill class is loaded only when a combine is queued.
        from eqclient3.actions.craft import Craft

        drill = Craft(recipe, 1)
        drill.practicing = True
        drill.priority = self.priority
        yield_to(self, loop, world, drill, "")


def load_book() -> RecipeBook:
    """The recipe cache. Tests replace `_BOOK` before a step."""
    global _BOOK
    if _BOOK is None:
        _BOOK = read_recipes(DEFAULT_RECIPES)
    return _BOOK


@runtime_checkable
class _Drill(Protocol):
    practicing: bool
    complete: bool


def _drill_open(loop: Loop) -> bool:
    queue = loop.queue
    if queue is None:
        return False
    return any(isinstance(action, _Drill) and action.practicing and not action.complete for action in queue)


def _mark_result(loop: Loop, world: World, recipe: Recipe, protect: tuple[int, ...]) -> None:
    result = recipe.result
    if result in protect:
        return
    journal = journal_of(loop)
    who = character_name(loop, world)
    if not journal or not who:
        return
    journal.mark_sell(who, result)
