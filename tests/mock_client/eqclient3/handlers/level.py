"""Experience, level, and the level-up popup. Fetches and the trainer are LevelUp's step."""

from __future__ import annotations

from eqclient3.actions.level_up import LevelUp
from eqclient3.handlers.common import enqueue_once
from eqclient3.structs import (
    EQStruct,
    OP_ExpUpdate,
    OP_LevelUpdate,
    OP_OnLevelMessage,
    OP_PopupResponse,
)
from eqclient3.handler import Handler


class LevelHandler(Handler):
    opcodes = ("OP_ExpUpdate", "OP_LevelUpdate", "OP_OnLevelMessage")

    def on(self, opcode: str, payload: EQStruct) -> None:
        del opcode
        if isinstance(payload, OP_ExpUpdate):
            self.world.exp = payload.exp
        elif isinstance(payload, OP_LevelUpdate):
            self.level(payload)
        elif isinstance(payload, OP_OnLevelMessage):
            self.popup(payload)

    def level(self, row: OP_LevelUpdate) -> None:
        world = self.world
        level, old, exp = row.level, row.level_old, row.exp
        if level > old:
            world.points = world.points + 5 * (level - old)
        if level > world.level:
            world.level = level
            enqueue_once(self.loop, world, LevelUp(level), f"level:{level}")
        world.exp = exp

    def popup(self, row: OP_OnLevelMessage) -> None:
        popup_id = row.popup_id
        self.loop.send("OP_PopupResponse", OP_PopupResponse(popup_id).serialize())
        level = self.world.level
        enqueue_once(self.loop, self.world, LevelUp(level), f"level:{level}")
