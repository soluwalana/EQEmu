"""Band 0. One step appends the scrolls, scribes, trainer, and gear this level opened."""

from __future__ import annotations

from typing import TYPE_CHECKING, Protocol, runtime_checkable

if TYPE_CHECKING:
    from eqclient3.loop import Loop
    from eqclient3.world import World

from eqclient3.action import Action
from eqclient3.actions.fetch import Fetch
from eqclient3.actions.scribe import ScribeSpell
from eqclient3.actions.support import yield_to
from eqclient3.actions.train import Train


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
        for item_id in _gear(world, level):
            if world.held(item_id) > 0:
                continue
            yield_to(
                self,
                loop,
                world,
                Fetch(item_id, 1, f"gear {item_id}"),
                f"fetch:{item_id}",
            )
        self.complete = True


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
