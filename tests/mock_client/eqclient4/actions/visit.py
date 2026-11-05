"""Band 0. Walk into an explore box and wait for the server to mark it done."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient4.loop import Loop
    from eqclient4.world import World

from eqclient4.action import Action
from eqclient4.actions.support import task_activities, walk, yards

_INSIDE = 5.0


class Visit(Action):

    def __init__(self, task_id: int, activity_id: int, point: tuple[float, float, float]) -> None:
        super().__init__()
        self.priority = 0
        self.task_id = task_id
        self.activity_id = activity_id
        self.point = point
        self.active_path = None

    def suspend(self) -> None:
        self.active_path = None
        self.suspended = True

    def step(self, loop: Loop, world: World) -> None:
        for activity in task_activities(world):
            if (
                int(activity.task_id) != self.task_id
                or int(activity.activity_id) != self.activity_id
            ):
                continue
            if activity.finished:
                self.complete = True
                return
        self.suspended = False
        if yards(world, self.point) <= _INSIDE:
            self.active_path = None
            return
        walk(self, loop, world, self.point, "run")
