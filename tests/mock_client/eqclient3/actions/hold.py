"""Band 100. Do not swing at this spawn. Its corpse finishes the hold."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient3.loop import Loop
    from eqclient3.world import World


from eqclient3.action import Action
from eqclient3.actions.support import spawn_of


class Hold(Action):
    def __init__(self, spawn_id: int) -> None:
        super().__init__()
        self.priority = 100
        self.spawn_id = spawn_id

    def opcodes(self) -> tuple[str, ...]:
        return ("OP_BecomeCorpse",)

    def suspend(self) -> None:
        self.suspended = True

    def step(self, loop: Loop, world: World) -> None:
        corpse = self.consume("OP_BecomeCorpse", lambda message: spawn_of(message) in (0, self.spawn_id))
        if corpse:
            self.complete = True
            return
        self.suspended = False
