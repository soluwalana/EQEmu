"""Band 0. Click, load, or combine, then wait. OP_TradeSkillCombine completes it."""
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient3.loop import Loop
    from eqclient3.world import World

from eqclient3.action import Action
from eqclient3.structs import OP_ClickObject, OP_MoveItem, OP_TradeSkillCombine
from eqclient3.actions.fetch import Fetch
from eqclient3.actions.support import INTERACT, yield_to, walk, yards
from eqclient3.actions.zone import Zone

class Craft(Action):

    def __init__(self, recipe: object) -> None:
        super().__init__()
        self.priority = 0
        self.durable = True
        self.recipe = recipe
        self.active_path = None
        self.sent = False
        self.clicked = False
        self.loaded = False

    def opcodes(self) -> tuple[object, ...]:
        return ('OP_TradeSkillCombine',)

    def suspend(self) -> None:
        self.active_path = None
        self.suspended = True

    def step(self, loop: Loop, world: World) -> None:
        if self.consume('OP_TradeSkillCombine'):
            self.unwait('CRAFT')
            self.complete = True
            return
        if self.waiting_for('CRAFT') and (not self.messages):
            return
        self.suspended = False
        missing = _missing(world, self.recipe)
        if missing is not None:
            item_id, count = missing
            yield_to(self, loop, world, Fetch(item_id, count, f'craft {item_id}'), f'fetch:{item_id}')
            return
        station_zone = getattr(self.recipe, "zone", None) or getattr(self.recipe, "station_zone", None)
        if station_zone and station_zone != world.zone:
            yield_to(self, loop, world, Zone(station_zone), f'zone:{station_zone}')
            return
        point = getattr(self.recipe, "point", None)
        if point is not None and yards(world, point) > INTERACT:
            walk(self, loop, world, tuple(point), 'run')
            return
        if self._send(loop):
            self.sent = True
            self.wait('CRAFT')

    def _send(self, loop: Loop) -> bool:
        """Click and load return for the next pulse. The combine is the wait."""
        if getattr(self.recipe, "needs_click", False) and (not self.clicked):
            drop = int(getattr(self.recipe, "drop_id", 0) or 0)
            loop.send('OP_ClickObject', OP_ClickObject(int(drop)).serialize())
            self.clicked = True
            return False
        if getattr(self.recipe, "needs_load", False) and (not self.loaded):
            src = int(getattr(self.recipe, "load_src", 0) or 0)
            dest = int(getattr(self.recipe, "load_dest", 0) or 0)
            loop.send('OP_MoveItem', OP_MoveItem(int(src), int(dest)).serialize())
            self.loaded = True
            return False
        slot = int(self.recipe.combine_slot or 0)
        loop.send('OP_TradeSkillCombine', OP_TradeSkillCombine(int(slot)).serialize())
        return True

def _missing(world: World, recipe: object) -> tuple[object, ...] | None:
    for row in recipe.components or ():
        item_id, count = (int(row[0]), int(row[1]))
        if world.held(item_id) < count:
            return (item_id, count)
    return None
