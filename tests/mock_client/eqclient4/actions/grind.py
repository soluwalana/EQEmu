"""Band 0. Camp until the world reaches a level, at whichever open XP camp we are in."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient4.loop import Loop
    from eqclient4.world import World

from eqclient4.action import Action
from eqclient4.actions.kill import Kill
from eqclient4.camps import grind_zones, zone_reachable


class Grind(Action):
    def __init__(self, world: World, loop: Loop, level: int) -> None:
        super().__init__(world, loop)
        self.priority = 0
        self.durable = True
        self.level = int(level)
        self.camp = ""
        self.active_path = None

    def opcodes(self) -> tuple[str, ...]:
        return ()

    def suspend(self) -> None:
        self.active_path = None
        self.suspended = True

    def step(self) -> None:
        target = int(self.level or 0)
        if int(self._world.level or 0) >= target:
            self.complete = True
            return

        self.suspended = False
        zones = grind_zones(int(self._world.level or 1))
        if not zones:
            return

        here = (self._world.zone or "").lower()
        if here in zones:
            self.camp = here
            self.active_path = None
            source = f"{self.source}#kill:{here}"
            if self._loop.source_open(source):
                self.yielding = True
                return
            self.yield_to(Kill(camp=here, level=target), source)
            return

        zone = zones[0]
        if self.camp != zone:
            self.camp = zone
            self.active_path = None

        point = self.next_zoneline(zone)
        if not point:
            return

        if not self.active_path:
            self.move_closer(point)
            return

        self._world.movement.advance(self._loop, self.active_path)


class LevelHoldAction(Action):
    def hold_for_level(self, zone: str) -> bool:
        """Queue a grind when the zone requires a higher level."""
        reason = zone_reachable(zone, int(self._world.level or 0))

        if not reason.startswith("level:"):
            return False

        need = int(reason.split(":", 1)[1])
        source = f"grind:{need}"

        if self._loop.source_open(source):
            self.yielding = True
            return True

        return self.yield_to(Grind(need), source)
