"""Band 230, behind Rez. Camp one bot, disband that bot, follow or invite the player."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient3.loop import Loop
    from eqclient3.world import World


from eqclient3.action import Action
from eqclient3.actions.support import send_command


class Seat(Action):
    def __init__(self, name: str, commands: list[str]) -> None:
        super().__init__()
        self.priority = 230
        self.durable = True
        self.name = name
        self.commands = list(commands)

    def opcodes(self) -> tuple[object, ...]:
        return ()

    def suspend(self) -> None:
        self.suspended = True

    @staticmethod
    def key(action: Action) -> tuple[object, ...]:
        return (1,)

    def step(self, loop: Loop, world: World) -> None:
        self.suspended = False
        if not self.commands:
            self.complete = True
            return
        send_command(loop, self.commands.pop(0))
