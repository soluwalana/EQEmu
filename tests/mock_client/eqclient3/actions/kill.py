"""Band 0. A task kill or a level camp. OP_BecomeCorpse for this spawn finishes it."""
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient3.loop import Loop
    from eqclient3.world import World

from eqclient3.action import Action
from eqclient3.actions.attack import Attack
from eqclient3.actions.support import INTERACT, has_soulbind, yield_to, spawn_of, walk, yards
from eqclient3.actions.talk import append_soulbind

class Kill(Action):

    def __init__(self, spawn_id: int | None = None, camp: str | None = None, level: int | None = None) -> None:
        super().__init__()
        self.priority = 0
        self.spawn_id = spawn_id or None
        self.camp = camp
        self.level = level
        self.active_path = None

    def opcodes(self) -> tuple[str, ...]:
        return ('OP_BecomeCorpse',)

    def suspend(self) -> None:
        self.active_path = None
        self.suspended = True

    def step(self, loop: Loop, world: World) -> None:
        if self.spawn_id and self._corpse():
            self.complete = True
            return
        self.suspended = False
        if not has_soulbind(loop, world) and (not any((str(a.source).startswith('soulbind:') for a in loop.queue))):
            if append_soulbind(self, loop, world):
                return
        if self.spawn_id is None and self.level is not None and (int(world.level or 0) >= int(self.level)):
            self.complete = True
            return
        dest = self._dest(world)
        if dest is None:
            return
        if yards(world, dest) > INTERACT:
            walk(self, loop, world, dest, 'run')
            return
        if self.spawn_id and (not any((type(action).__name__ == 'Attack' and action.spawn_id == self.spawn_id for action in loop.queue))):
            attack = Attack(self.spawn_id)
            world.note_fight(self.spawn_id)
            mob = world.mobs.get(self.spawn_id)
            if mob is not None:
                attack.level = int(mob.level or 0)
            yield_to(self, loop, world, attack, f'kill:{self.spawn_id}')

    def _corpse(self) -> bool:
        return self.consume('OP_BecomeCorpse', lambda message: spawn_of(message) in (0, self.spawn_id)) is not None

    def _dest(self, world: World) -> tuple[float, float, float] | None:
        if self.spawn_id and self.spawn_id in world.mobs:
            return world.mobs[self.spawn_id].position
        if isinstance(self.camp, (tuple, list)):
            return tuple(self.camp)
        camp = world.camps or {}
        if self.camp in camp:
            return camp[self.camp]
        return self.camp if isinstance(self.camp, tuple) else None
