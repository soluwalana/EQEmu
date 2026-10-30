"""Band 400. One zone request, then wait for OP_NewZone. A closed session sends nothing."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient3.loop import Loop
    from eqclient3.world import World


from eqclient3.action import Action
from eqclient3.actions.support import session_open, zone_id, zone_packet


class Zone(Action):
    def __init__(self, destination: str) -> None:
        super().__init__()
        self.priority = 400
        self.durable = True
        self.destination = destination
        self.asked = False

    def opcodes(self) -> tuple[str, ...]:
        return ("OP_NewZone",)

    def suspend(self) -> None:
        self.suspended = True

    def step(self, loop: Loop, world: World) -> None:
        if self.waiting_for("ZONE"):
            if self.consume("OP_NewZone"):
                self.waited = 0
                self.unwait("ZONE")
                self.complete = True
            return
        if not session_open(loop):
            return
        point = world.position
        loop.send(
            "OP_ZoneChange",
            zone_packet(
                self.destination,
                zone_id(self.destination),
                point[0],
                point[1],
                point[2],
            ),
        )
        self.asked = True
        self.wait("ZONE")
        self.suspended = False
