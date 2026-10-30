"""Band 210. Walk to the leader's last point. Spawn updates refresh it."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient3.action import Message
    from eqclient3.loop import Loop
    from eqclient3.world import World

from eqclient3.action import Action
from eqclient3.actions.support import payload_get, walk


class Follow(Action):

    def __init__(self, leader: str) -> None:
        super().__init__()
        self.priority = 210
        self.leader = leader
        self.active_path = None
        self.point: tuple[float, float, float] | None = None

    def opcodes(self) -> tuple[str, ...]:
        return ("OP_ClientUpdate", "OP_MobUpdate")

    def add_message(self, message: Message) -> None:
        super().add_message(message)
        if self._moves_leader(message):
            self.point = _point(message)
            self.active_path = None

    def suspend(self) -> None:
        self.active_path = None
        self.suspended = True

    def step(self, loop: Loop, world: World) -> None:
        if self.point is None:
            self.point = _leader_point(world, self.leader)
        if self.point is None:
            return
        walk(self, loop, world, self.point, "run")

    def _moves_leader(self, message: Message) -> bool:
        spawn = payload_get(message, "spawn_id")
        name = payload_get(message, "name")
        if isinstance(self.leader, int) and spawn is not None and (int(spawn) == int(self.leader)):
            return True
        if name and str(name).lower() == str(self.leader).lower():
            return True
        return payload_get(message, "leader", False) is True


def _point(message: Message) -> tuple[float, float, float] | None:
    x = payload_get(message, "x")
    y = payload_get(message, "y")
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        return None
    z = payload_get(message, "z", 0.0)
    height = z if isinstance(z, (int, float)) else 0.0
    return (float(x), float(y), float(height))


def _leader_point(world: World, leader: str) -> tuple[float, float, float] | None:
    if isinstance(leader, int) and leader in world.mobs:
        return world.mobs[leader].position
    for mob in world.mobs.values():
        if str(mob.name).lower() == str(leader).lower():
            return mob.position
    return world.leader_point
