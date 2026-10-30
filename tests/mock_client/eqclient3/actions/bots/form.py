"""Band 290. Send the command list one line per step."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient3.loop import Loop
    from eqclient3.world import World


from eqclient3.action import Action
from eqclient3.actions.support import send_command


class Form(Action):
    def __init__(self, zone: str, commands: list[str]) -> None:
        super().__init__()
        self.priority = 290
        self.zone = zone
        self.commands = list(commands)

    def opcodes(self) -> tuple[str, ...]:
        return ()

    def suspend(self) -> None:
        self.suspended = True

    def step(self, loop: Loop, world: World) -> None:
        self.suspended = False
        if not self.commands:
            self.complete = True
            return
        send_command(loop, self.commands.pop(0))
