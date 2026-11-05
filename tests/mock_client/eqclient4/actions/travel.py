"""Band 0. Walk to the next zoneline. Completes when the world zone is the destination."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient4.loop import Loop
    from eqclient4.world import World

from eqclient4.actions.grind import LevelHoldAction
from eqclient4.log import log
from eqclient4.structs import OP_ZoneChange


class Travel(LevelHoldAction):
    def __init__(self, destination: str) -> None:
        super().__init__()
        self.priority = 0
        self.durable = True
        self.destination = destination
        self.active_path = None

    def opcodes(self) -> tuple[str, ...]:
        return ("OP_NewZone",)

    def suspend(self) -> None:
        self.active_path = None
        self.suspended = True

    def step(self, loop: Loop, world: World) -> None:
        if world.zone == self.destination:
            self.complete = True
            return

        if self.hold_for_level(self.destination):
            return

        in_tutorial = self._world.zone == "tutorialb"

        source = self.source or ""

        if in_tutorial and "#gold:" in source:
            self._loop.forget(self)
            return

        self.suspended = False

        point = self.next_zoneline(self.destination)
        if point is None:
            return

        if self.exit_kind(self.destination) == "point":
            painted = self.painted_line(point)
            if painted is not None:
                point = painted
            if self._crossing(point):
                return
        self._drop_stale_path(point)
        if not self.active_path:
            self.move_closer(point, "run")
            return
        self.suspended = False
        self._world.movement.advance(self._loop, self.active_path)

    def _drop_stale_path(self, point: tuple[float, float, float]) -> None:
        path = self.active_path
        if path is None:
            return
        dest = path.destination
        if (dest[0] - point[0]) ** 2 + (dest[1] - point[1]) ** 2 > 400.0:
            self.active_path = None

    def _crossing(self, point: tuple[float, float, float]) -> bool:
        """A zone point zones when we ask from the painted line. Doors do not."""
        if self.waiting_for("ZONE"):
            if self._world.zone == self.destination or self.consume("OP_NewZone"):
                self.complete = True
                return True
            self.waited += 1
            if self.waited < 40:
                return True
            self.unwait("ZONE")
            self.waited = 0
        here = self._world.position
        if (here[0] - point[0]) ** 2 + (here[1] - point[1]) ** 2 > 625.0:
            return False
        if not self._loop.session_open():
            return True

        dest_id = self._world.zone_graph.zones.get(self.destination)
        if not dest_id:
            return False

        log.info(
            "zone line %s -> %s (%s) at (%.0f, %.0f, %.0f)",
            self._world.zone,
            self.destination,
            dest_id,
            here[0],
            here[1],
            here[2],
        )
        self._loop.send(
            "OP_ZoneChange",
            OP_ZoneChange(
                self.destination,
                int(dest_id),
                float(here[0]),
                float(here[1]),
                float(here[2]),
            ).serialize(),
        )
        self.wait("ZONE")
        self.waited = 0
        self.active_path = None
        return True
