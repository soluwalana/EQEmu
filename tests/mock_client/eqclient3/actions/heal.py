"""Band 260. One heal cast. The bar coming back, or string 251 on our corpse, finishes it."""
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient3.loop import Loop
    from eqclient3.world import World

from eqclient3.action import Action
from eqclient3.actions.support import bar_ratio, cast_spell, memorized, ready_gem, reclaim_if_ours, send_command

class Heal(Action):

    def __init__(self, who: str | int) -> None:
        super().__init__()
        self.priority = 260
        self.who = who
        self.cast = False
        self.cast_target = 0
        self._gem_recast = {}

    def opcodes(self) -> tuple[object, ...]:
        return ('OP_HPUpdate', 'OP_MobHealth', 'OP_SimpleMessage')

    def suspend(self) -> None:
        self.suspended = True

    def step(self, loop: Loop, world: World) -> None:
        if self.waiting_for('HEAL') and (not self.messages):
            return
        if self._bar_up():
            self.unwait('HEAL')
            self.complete = True
            return
        if self._corpse(loop, world):
            return
        if self.cast:
            return
        self.suspended = False
        target = self.who if isinstance(self.who, int) else int(world.self_id or 0)
        gem = next((row for row in memorized(world, self) if row.heal), None)
        if gem is not None and ready_gem(world, gem):
            cast_spell(loop, gem, target)
        else:
            send_command(loop, f'^cast heal {self.who}')
        self.cast_target = int(target)
        self.cast = True
        self.wait('HEAL')

    def _bar_up(self) -> bool:
        message = self.consume('OP_HPUpdate') or self.consume('OP_MobHealth')
        if message is None:
            return False
        fraction = bar_ratio(message)
        return fraction is not None and fraction > 0.5

    def _corpse(self, loop: Loop, world: World) -> bool:
        who = int(self.who) if isinstance(self.who, int) else 0
        if not reclaim_if_ours(self, loop, world, who, int(self.cast_target or 0)):
            return False
        self.complete = True
        return True
