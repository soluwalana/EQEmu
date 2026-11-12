"""Band 400. One zone request, then wait for OP_NewZone. A closed session sends nothing.

The request is not durable. A disconnect wipes it, and the server's success
packet is the reconnect, not a second OP_ZoneChange.
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient4.loop import Loop
    from eqclient4.world import World

from eqclient4.actions.grind import LevelHoldAction
from eqclient4.structs import OP_ZoneChange


class Zone(LevelHoldAction):
    def __init__(self, world: World, loop: Loop, destination: str) -> None:
        super().__init__(world, loop)
        self.priority = 400
        self.durable = False
        self.destination = destination
        self.asked = False

    def opcodes(self) -> tuple[str, ...]:
        return ("OP_NewZone",)

    def suspend(self) -> None:
        self.suspended = True

    def step(self) -> None:
        if self.waiting_for("ZONE"):
            if self.consume("OP_NewZone"):
                self.waited = 0
                self.unwait("ZONE")
                self.complete = True
            return

        if not self._loop.session_open():
            return

        if self.hold_for_level(self.destination):
            self.priority = 0
            return

        self.priority = 400

        point = self._world.position
        zone_id = self._world.zone_graph.zones.get(self.destination, 0)
        self._loop.send(
            "OP_ZoneChange",
            OP_ZoneChange(
                self.destination,
                int(zone_id),
                float(point[0]),
                float(point[1]),
                float(point[2]),
            ).serialize(),
        )
        self.asked = True
        self.wait("ZONE")
        self.suspended = False

    def report(self) -> str:
        return f"{super().report()} destination={self.destination} asked_for_zone={self.asked}"
