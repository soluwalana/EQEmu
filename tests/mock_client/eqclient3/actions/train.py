"""Band 0. Walk to the guildmaster, open the window, spend one point, wait for the answer."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient3.loop import Loop
    from eqclient3.world import World

from eqclient3.action import Action
from eqclient3.structs import OP_GMEndTraining, OP_GMTrainSkill, OP_GMTraining
from eqclient3.actions.support import INTERACT, walk, yards


class Train(Action):

    def __init__(self, guildmaster: int) -> None:
        super().__init__()
        self.priority = 0
        self.durable = True
        self.guildmaster = guildmaster
        self.active_path = None
        self.window = False
        self.point_sent = False

    def opcodes(self) -> tuple[str, ...]:
        return ("OP_GMTrainSkill", "OP_GMEndTraining")

    def suspend(self) -> None:
        self.active_path = None
        self.suspended = True

    def step(self, loop: Loop, world: World) -> None:
        if self.waiting_for("TRAIN") and (not self.messages):
            return
        if self.consume("OP_GMTrainSkill") or self.consume("OP_GMEndTraining"):
            self.point_sent = False
            self.unwait("TRAIN")
        self.suspended = False
        if int(world.training_points or 0) <= 0:
            if self.window:
                self._end(loop, world)
            self.complete = True
            return
        dest = _point(world, self.guildmaster)
        if dest is not None and yards(world, dest) > INTERACT:
            walk(self, loop, world, dest, "run")
            return
        if not self.window:
            loop.send(
                "OP_GMTraining",
                OP_GMTraining(int(self.guildmaster), int(world.self_id or 0)).serialize(),
            )
            self.window = True
            return
        skill = int(world.train_skill or 0)
        loop.send(
            "OP_GMTrainSkill",
            OP_GMTrainSkill(int(self.guildmaster), int(skill)).serialize(),
        )
        self.point_sent = True
        self.wait("TRAIN")

    def _end(self, loop: Loop, world: World) -> None:
        loop.send(
            "OP_GMEndTraining",
            OP_GMEndTraining(int(self.guildmaster), int(world.self_id or 0)).serialize(),
        )


def _point(world: World, guildmaster: int) -> tuple[float, float, float] | None:
    if isinstance(guildmaster, int) and guildmaster in world.mobs:
        return world.mobs[guildmaster].position
    return world.trainer_point
