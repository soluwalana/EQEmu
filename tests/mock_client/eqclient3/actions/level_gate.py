"""Hold Travel or Zone until a grind covers the destination's level floor.

Grind's module imports Kill, and that chain imports Zone while it is still
loading. Zone imports this module, so Grind is imported when the gate runs.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient3.action import Action
    from eqclient3.actions.grind import Grind
    from eqclient3.loop import Loop
    from eqclient3.world import World

from eqclient3.actions.support import yield_to
from eqclient3.camps import zone_reachable


def hold_for_level(action: Action, loop: Loop, world: World, zone: str) -> bool:
    """Queue a grind when `zone` is above this level. True means the parent must wait."""
    reason = zone_reachable(zone, int(world.level or 0))
    if not reason.startswith("level:"):
        return False
    need = int(reason.split(":", 1)[1])
    source = f"grind:{need}"
    if _open(loop, source):
        action.yielding = True
        return True
    grind = _grind(need)
    return yield_to(action, loop, world, grind, source)


def _grind(level: int) -> Grind:
    from eqclient3.actions.grind import Grind as Camp

    return Camp(level)


def _open(loop: Loop, source: str) -> bool:
    queue = loop.queue
    if queue is None:
        return False
    for queued in queue:
        if queued.source == source and not queued.complete:
            return True
    return False
