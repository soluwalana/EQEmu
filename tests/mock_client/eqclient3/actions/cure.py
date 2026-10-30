"""Band 250. One cure line. OP_Buff clears it. String 251 on our corpse reclaims."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient3.loop import Loop
    from eqclient3.world import World


from eqclient3.action import Action
from eqclient3.actions.support import effect_gone, own_corpse, reclaim_if_ours, send_command


class Cure(Action):
    def __init__(self, entity: str | int, effect: str) -> None:
        super().__init__()
        self.priority = 250
        self.entity = entity
        self.effect = effect
        self.cast_target = 0
        self.sent = False

    def opcodes(self) -> tuple[object, ...]:
        return ("OP_Buff", "OP_SimpleMessage")

    def suspend(self) -> None:
        self.suspended = True

    def step(self, loop: Loop, world: World) -> None:
        if self.waiting_for("CURE") and not self.messages:
            return
        buff = self.consume("OP_Buff")
        if buff is not None and effect_gone(buff, world, self.effect):
            self.unwait("CURE")
            self.complete = True
            return
        if self._corpse(loop, world):
            return
        if self.sent:
            return
        self.suspended = False
        if isinstance(self.entity, str) and self.entity:
            line = f"^cast cures byname {self.entity}"
        else:
            line = "^cast cures"
        send_command(loop, line)
        self.cast_target = int(self.entity) if isinstance(self.entity, int) else own_corpse(loop, world)
        self.sent = True
        self.wait("CURE")

    def _corpse(self, loop: Loop, world: World) -> bool:
        if not reclaim_if_ours(self, loop, world, int(self.cast_target or 0)):
            return False
        self.complete = True
        return True
