"""^botsummon spawned, then the special line that the bots arrived.

The server sends that line with Client::Message, which is OP_SpecialMesg.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient3.action import Message
    from eqclient3.loop import Loop
    from eqclient3.world import World


from eqclient3.action import Action
from eqclient3.actions.bots.form import queue_form
from eqclient3.actions.support import message_text, send_command


class Summon(Action):
    def __init__(self, priority: int) -> None:
        super().__init__()
        self.priority = priority
        self.sent = False
        self.limit = 10
        self.asks = 0

    def opcodes(self) -> tuple[str, ...]:
        return ("OP_SpecialMesg", "OP_ChannelMessage")

    def suspend(self) -> None:
        self.suspended = True

    def step(self, loop: Loop, world: World) -> None:
        if self.waiting_for("SUMMON"):
            message = self._arrived()
            if message:
                self.unwait("SUMMON")
                self.waited = 0
                self.complete = True
                return
            if self._none_spawned():
                self._form(loop, world)
                return
            self.waited += 1
            limit = self.limit
            if limit is None or self.waited < limit:
                return
            self.waited = 0
            self.sent = False
            self.unwait("SUMMON")
            self.asks += 1
            if self.asks >= 3:
                self._form(loop, world)
                return
        send_command(loop, "^botsummon spawned")
        self.sent = True
        self.wait("SUMMON")
        self.suspended = False

    def _arrived(self) -> Message | None:
        special = self.consume("OP_SpecialMesg", lambda message: _summoned(message_text(message)))
        if special:
            return special
        return self.consume("OP_ChannelMessage", lambda message: _summoned(message_text(message)))

    def _none_spawned(self) -> bool:
        """^botsummon spawned only moves bots that are already up."""
        special = self.consume("OP_SpecialMesg", lambda message: _none(message_text(message)))
        if special:
            return True
        return self.consume("OP_ChannelMessage", lambda message: _none(message_text(message))) is not None

    def _form(self, loop: Loop, world: World) -> None:
        """Nobody is spawned, so the summon cannot land. Spawn the party by name."""
        self.unwait("SUMMON")
        self.waited = 0
        world.formed_for = ""
        queue_form(loop, world)
        self.complete = True


def _none(text: str) -> bool:
    return "no spawned bots" in (text or "").lower()


def _summoned(text: str) -> bool:
    lowered = (text or "").lower()
    return "summoned" in lowered and "bots to you" in lowered
