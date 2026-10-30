"""Band 410. One step drops every ephemeral action, including work tagged for another zone."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient3.loop import Loop
    from eqclient3.world import World


from eqclient3.action import Action
from eqclient3.actions.support import clear_source


class Death(Action):
    def __init__(self) -> None:
        super().__init__()
        self.priority = 410

    def opcodes(self) -> tuple[str, ...]:
        return ()

    def suspend(self) -> None:
        self.suspended = True

    def step(self, loop: Loop, world: World) -> None:
        self.suspended = False
        queue = loop.queue
        if queue is None:
            self.complete = True
            return
        for action in list(queue):
            if action.insert == self.insert or action.durable:
                continue
            queue.remove(action.insert)
            clear_source(loop, world, action.source)
        self.complete = True
