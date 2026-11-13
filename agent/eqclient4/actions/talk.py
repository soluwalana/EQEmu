"""Navigate to an NPC, target them, say the specified text, wait for a few moments, then return."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient4.loop import Loop
    from eqclient4.world import Mob, World

from eqclient4.action import Action
from eqclient4.log import log
from eqclient4.structs import (
    SAY_CHANNEL,
    EQStruct,
    OP_ChannelMessage,
    OP_SimpleMessage,
    OP_SpecialMesg,
)


class Talk(Action):

    def __init__(
        self,
        world: World,
        loop: Loop,
        npc_id: int,
        task_text: str,
        priority: int = 0,
    ) -> None:
        super().__init__(world, loop)
        self.priority = priority
        self.npc_id = npc_id
        self.npc: Mob | None = self._world.mobs.find_mob(npc_id)
        self.active_path = None
        self.sent = False
        self.task_text = task_text
        self.received = []
        self.ticks_after_send = 0

    def opcodes(self) -> tuple[str, ...]:
        return super().opcodes() + (
            "OP_ChannelMessage",
            "OP_SpecialMesg",
            "OP_SimpleMessage",
            "OP_TaskActivity",
        )

    def suspend(self) -> None:
        self.active_path = None
        self.suspended = True

    def step(self) -> None:
        super().step()

        if not self.npc:
            log.error(f"NPC not found: {self.npc_id}")
            self.complete = True
            return

        if not self.active_path:
            self.active_path = self._world.movement.plan(self.npc, "run")
            self.move_closer(self.active_path.destination, "run")
            return

        self._world.measure(self.npc)

        if self.npc.distance > 10:
            self.move_closer(self.active_path.destination, "run")
            return

        # Don't set target_id until after we are closs enough to talk
        if self.mob_targeted != self.npc.id:
            self.target_id = self.npc.id
            return

        if not self.sent:
            self._loop.send(
                "OP_ChannelMessage",
                OP_ChannelMessage(
                    self.npc.spoken_name,
                    self._world.character.name,
                    100,
                    SAY_CHANNEL,
                    0,
                    0,
                    100,
                    self.task_text,
                ).serialize(),
            )
            self.sent = True
            return

        def from_target(payload: EQStruct) -> bool:
            if not self.npc:
                return False

            match payload:
                case OP_ChannelMessage():
                    return payload.sender == self.npc.spoken_name
                case OP_SpecialMesg():
                    return payload.speaker == self.npc.spoken_name
                case _:
                    return False

        message = self.consume(
            ("OP_ChannelMessage", "OP_SpecialMesg", "OP_SimpleMessage"), from_target
        )
        if message:
            log.info(f"Received message: {message}")
            self.received.append(message)

        self.ticks_after_send += 1
        if self.ticks_after_send > 40:
            self.complete = True
