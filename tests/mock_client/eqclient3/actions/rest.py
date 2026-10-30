"""Band 240. Sit until the bar is at 90 percent. Bot mana waits on a silk fetch."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient3.loop import Loop
    from eqclient3.world import World

from eqclient3.action import Action
from eqclient3.structs import OP_SpawnAppearance
from eqclient3.actions.support import SIT, bar_ratio, send_command, silk_fetch_queued


class Rest(Action):

    def __init__(self, who: str | int) -> None:
        super().__init__()
        self.priority = 240
        self.who = who
        self.mana = False

    def opcodes(self) -> tuple[str, ...]:
        return ("OP_HPUpdate", "OP_MobHealth", "OP_ManaChange")

    def suspend(self) -> None:
        self.suspended = True

    def step(self, loop: Loop, world: World) -> None:
        if self._full(world):
            self.complete = True
            return
        self.suspended = False
        if self._bot_mana(world) and silk_fetch_queued(loop):
            return
        who = str(self.who or "")
        mine = str(world.name or "")
        if who and mine and (who.lower() != mine.lower()) and (who != str(world.self_id)):
            send_command(loop, f"^sit on byname {who}")
            return
        loop.send(
            "OP_SpawnAppearance",
            OP_SpawnAppearance(int(world.self_id or 0), 14, SIT).serialize(),
        )

    def _bot_mana(self, world: World) -> bool:
        if self.mana:
            return True
        who = str(self.who or "")
        mine = str(world.name or "")
        return bool(who and mine and (who.lower() != mine.lower()) and world.rest_mana)

    def _full(self, world: World) -> bool:
        message = self.consume("OP_HPUpdate") or self.consume("OP_MobHealth") or self.consume("OP_ManaChange")
        if message is None:
            return False
        if message.opcode == "OP_ManaChange":
            mana = None
            payload = message.payload
            if isinstance(payload, dict):
                mana = payload.get("mana")
            elif isinstance(payload, (bytes, bytearray)) and len(payload) >= 4:
                mana = int.from_bytes(payload[:4], "little")
            maximum = int(world.max_mana or 0)
            return maximum > 0 and mana is not None and (float(mana) / float(maximum) >= 0.9)
        fraction = bar_ratio(message)
        return fraction is not None and fraction >= 0.9
