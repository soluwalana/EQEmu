"""Band 0. Camp until the world reaches a level, at whichever open XP camp we are in."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient4.loop import Loop
    from eqclient4.world import World

from eqclient4.action import Action
from eqclient4.actions.kill import Kill
from eqclient4.camps import camp_for_level, zone_reachable, zone_recommended_level
from eqclient4.log import log


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
        if not self._world.zone:
            log.error(f"Not zoned in yet to grind level {self.level}")
            return

        target = int(self.level or 0)
        current_level = self._world.character.level
        if current_level >= target:
            self.complete = True
            return

        self.suspended = False

        if self.camp and self.camp != self._world.zone:
            point = self.next_zoneline(self.camp)
            if not point:
                log.error(f"No zoneline found to grind in {self.camp}")
                self.crash()
                return

            self.move_closer(point)
            return

        zone = camp_for_level(current_level, self._world.zone or "")
        if not zone:
            log.error(f"No zones to grind in for level {current_level}")
            self.crash()
            return

        self.camp = zone.zone

        if self.camp != self._world.zone:
            log.info(f"Moving to zone {self.camp} to grind level {self.level}")
            return

        self.active_path = None
        source = f"{self.source}#kill:{self.camp}"
        k = Kill(camp=self.camp, level=target)
        k.source = source
        self.yield_to(k)
        return

    def report(self) -> str:
        return f"{super().report()} level={self._world.character.level} -> {self.level}  camp={self.camp}"


class LevelHoldAction(Action):
    def hold_for_level(self, zone: str) -> bool:
        """Queue a grind when the zone requires a higher level."""

        if not zone_reachable(zone, self._world.character.level):
            return False

        need = zone_recommended_level(zone)
        g = Grind(self._world, self._loop, need)
        g.source = f"grind:{need}"
        g.priority = self.priority + 1
        return self.yield_to(g)
