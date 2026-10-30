"""Band 0. One step appends the scrolls, scribes, trainer, and gear this level opened."""
from __future__ import annotations

from typing import TYPE_CHECKING

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
        for spell in _spells(world, self.level):
            spell_id = int(spell['spell_id'] if isinstance(spell, dict) else spell.spell_id)
            scroll = int(spell['scroll_id'] if isinstance(spell, dict) else spell.scroll_id or 0)
            slot = int(spell['slot'] if isinstance(spell, dict) else spell.slot or 0)
            if scroll and world.held(scroll) < 1:
                yield_to(self, loop, world, Fetch(scroll, 1, f'scroll {spell_id}'), f'fetch:{scroll}')
            yield_to(self, loop, world, ScribeSpell(spell_id, slot), f'scribe:{spell_id}')
        master = _guildmaster(world)
        if master:
            yield_to(self, loop, world, Train(master), f'train:{master}')
        for item_id in _gear(world, self.level):
            if world.held(int(item_id)) > 0:
                continue
            yield_to(self, loop, world, Fetch(int(item_id), 1, f'gear {item_id}'), f'fetch:{item_id}')
        self.complete = True

def _spells(world: World, level: int) -> list[object]:
    rows = world.level_spells
    if rows is not None:
        return [row for row in rows if int(row['level'] if isinstance(row, dict) else row.level) <= level]
    return []

def _gear(world: World, level: int) -> list[object]:
    rows = world.level_gear
    if rows is None:
        return []
    found = []
    for row in rows:
        if isinstance(row, int):
            found.append(row)
            continue
        need = int(row['level'] if isinstance(row, dict) else row.level)
        if need <= level:
            found.append(int(row['item_id'] if isinstance(row, dict) else row.item_id))
    return found

def _guildmaster(world: World) -> int:
    master = world.guildmaster
    if master:
        return int(master)
    return 0
