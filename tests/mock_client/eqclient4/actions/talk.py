from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient4.world import Mob

from eqclient4.action import Action
from eqclient4.structs.tasks import OP_TaskActivity


class Talk(Action):

    def __init__(
        self, npc: Mob, task_text: str, priority: int = 0, activity: OP_TaskActivity | None = None
    ) -> None:
        super().__init__()
        self.priority = priority
        self.npc = npc
        self.active_path = None
        self.sent = False
        self.activity = activity
        self.followups = []

    def opcodes(self) -> tuple[str, ...]:
        return (
            "OP_Consider",
            "OP_ChannelMessage",
            "OP_SpecialMesg",
            "OP_SimpleMessage",
            "OP_TaskActivity",
        )

    def suspend(self) -> None:
        self.active_path = None
        self.suspended = True

    def step(self) -> None:

        if self.active_path is None:
            self.active_path = self._world.movement.plan(self.npc, "run")
            self._world.movement.advance(self.active_path)
        else:
            self._world.movement.advance(self.active_path)
