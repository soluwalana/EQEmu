"""^botsummon spawned, then the channel line that the bots arrived."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient3.loop import Loop
    from eqclient3.world import World


from eqclient3.action import Action
from eqclient3.actions.support import message_text, send_command


class Summon(Action):
    def __init__(self, priority: int) -> None:
        super().__init__()
        self.priority = priority
        self.sent = False
        self.limit = 10

    def opcodes(self) -> tuple[str, ...]:
        return ("OP_ChannelMessage",)

    def suspend(self) -> None:
        self.suspended = True

    def step(self, loop: Loop, world: World) -> None:
        if self.waiting_for("SUMMON"):
            message = self.consume("OP_ChannelMessage", lambda message: _summoned(message_text(message)))
            if message:
                self.unwait("SUMMON")
                self.waited = 0
                self.complete = True
                return
            self.waited += 1
            limit = self.limit
            if limit is None or self.waited < limit:
                return
            self.waited = 0
            self.sent = False
            self.unwait("SUMMON")
        send_command(loop, "^botsummon spawned")
        self.sent = True
        self.wait("SUMMON")
        self.suspended = False


def _summoned(text: str) -> bool:
    lowered = (text or "").lower()
    return "summoned" in lowered and "bots to you" in lowered
