"""Band 0. One step appends the scrolls, scribes, trainer, and gear this level opened."""

from __future__ import annotations

from typing import TYPE_CHECKING, Protocol, runtime_checkable

if TYPE_CHECKING:
    from eqclient3.loop import Loop
    from eqclient3.world import World

from eqclient3.action import Action
from eqclient3.actions.fetch import GEAR_BAND, Fetch, item_cost
from eqclient3.actions.scribe import ScribeSpell
from eqclient3.actions.support import character_name, in_tutorial, journal_of, yield_to
from eqclient3.actions.train import Train
from eqclient3.quests.produce import _kit_for


class LevelUp(Action):

    def __init__(self, level: int) -> None:
        super().__init__()
        self.priority = 0
        self.durable = True
        self.level = int(level)

    def opcodes(self) -> tuple[str, ...]:
        return ()

    def suspend(self) -> None:
        self.suspended = True

    def step(self, loop: Loop, world: World) -> None:
        self.suspended = False
        level = self.level
        if level is None:
            return
        for spell in _spells(world, level):
            spell_id = _field(spell, "spell_id")
            scroll = _field(spell, "scroll_id")
            slot = _field(spell, "slot")
            if scroll and world.held(scroll) < 1:
                yield_to(
                    self,
                    loop,
                    world,
                    Fetch(scroll, 1, f"scroll {spell_id}"),
                    f"fetch:{scroll}",
                )
            yield_to(self, loop, world, ScribeSpell(spell_id, slot), f"scribe:{spell_id}")
        master = _guildmaster(world)
        if master:
            yield_to(self, loop, world, Train(master), f"train:{master}")
        if not in_tutorial(world):
            queue_level_gear(loop, world, level)
        self.complete = True


def queue_level_gear(loop: Loop, world: World, level: int | None = None) -> None:
    """Buy the kit for this level. The mines have no camp that pays for it, so this waits."""
    if in_tutorial(world):
        return
    reached = level if level is not None else (world.level or 1)
    if reached < 1:
        return
    queue = loop.queue
    if queue is None:
        return
    who = character_name(loop, world)
    journal = journal_of(loop)
    for item_id in _tier(world, reached):
        if world.held(item_id) > 0:
            continue
        fetch = Fetch(item_id, 1, f"gear {item_id}", copper=item_cost(item_id))
        fetch.priority = GEAR_BAND
        fetch.source = f"fetch:{item_id}"
        queue.append(fetch, world, journal, who)


@runtime_checkable
class _Spell(Protocol):
    spell_id: int
    scroll_id: int
    slot: int
    level: int


@runtime_checkable
class _Gear(Protocol):
    item_id: int
    level: int


def _field(row: dict[str, object] | _Spell, name: str) -> int:
    if isinstance(row, dict):
        value = row.get(name)
        return value if isinstance(value, int) else 0
    value = row.spell_id if name == "spell_id" else row.scroll_id if name == "scroll_id" else row.slot
    return value if isinstance(value, int) else 0


def _spells(world: World, level: int) -> list[dict[str, object] | _Spell]:
    rows = world.level_spells
    if not isinstance(rows, list):
        return []
    found: list[dict[str, object] | _Spell] = []
    for row in rows:
        if isinstance(row, dict):
            need = row.get("level")
            if isinstance(need, int) and need <= level:
                found.append(row)
        elif isinstance(row, _Spell) and row.level <= level:
            found.append(row)
    return found


def _tier(world: World, level: int) -> list[int]:
    """Catalog gear at this level, then the kit tier for the player and each companion class."""
    found = _gear(world, level)
    seen = set(found)
    for class_id in _classes(world):
        for item_id in _kit_for(class_id, level):
            if item_id not in seen:
                seen.add(item_id)
                found.append(item_id)
    return found


def _classes(world: World) -> list[int]:
    found: list[int] = []
    if world.class_id:
        found.append(int(world.class_id))
    for bot in world.bots.roster:
        class_id = int(bot.class_id or 0)
        if class_id and class_id not in found:
            found.append(class_id)
    return found


def _gear(world: World, level: int) -> list[int]:
    rows = world.level_gear
    if not isinstance(rows, list):
        return []
    found: list[int] = []
    for row in rows:
        if isinstance(row, int):
            found.append(row)
            continue
        if isinstance(row, dict):
            need = row.get("level")
            item_id = row.get("item_id")
        elif isinstance(row, _Gear):
            need = row.level
            item_id = row.item_id
        else:
            continue
        if isinstance(need, int) and isinstance(item_id, int) and need <= level:
            found.append(item_id)
    return found


def _guildmaster(world: World) -> int:
    master = world.guildmaster
    if master:
        return int(master)
    return 0
