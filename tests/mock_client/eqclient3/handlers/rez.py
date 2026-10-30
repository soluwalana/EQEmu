"""Bind reclaim, and a rez request that keeps its payload."""

from __future__ import annotations

from eqclient3.actions.reclaim import Reclaim
from eqclient3.actions.rez import Rez
from eqclient3.handlers.common import character_name, mobs_map, enqueue_once
from eqclient3.structs import EQStruct, OP_RezzRequest, OP_ZonePlayerToBind
from eqclient3.handler import Handler


class RezHandler(Handler):
    opcodes = ("OP_ZonePlayerToBind", "OP_RezzRequest")

    def on(self, opcode: str, payload: EQStruct) -> None:
        del opcode
        if isinstance(payload, OP_ZonePlayerToBind):
            self.bind()
        elif isinstance(payload, OP_RezzRequest):
            self.rezz(payload)

    def bind(self) -> None:
        """Queue a Reclaim when none is waiting. The queue is the list of our bodies."""
        queue = self.loop.queue
        if queue is None or any(type(action).__name__ == "Reclaim" for action in queue):
            return
        corpse_id = self.fallback_corpse()
        if not corpse_id:
            return
        world = self.world
        where = (world.x, world.y, world.z)
        enqueue_once(self.loop, world, Reclaim(corpse_id, where), f"reclaim:{corpse_id}")

    def our_corpse(self) -> int:
        last = 0
        queue = self.loop.queue
        if queue is None:
            return last
        for action in queue:
            if type(action).__name__ == "Reclaim" and action.corpse_id is not None:
                last = action.corpse_id
        if last:
            return last
        return self.fallback_corpse()

    def fallback_corpse(self) -> int:
        world = self.world
        if world.pending_death:
            return world.pending_death
        if world.self_id:
            return world.self_id
        return 0

    def rezz(self, row: OP_RezzRequest) -> None:
        world = self.world
        name = row.corpse_name
        corpse_id = 0
        if name:
            want = name.lower()
            me = character_name(self.loop, world).lower()
            for mob in mobs_map(world).values():
                if (mob.name or "").lower() == want:
                    corpse_id = mob.id
                    break
            if not corpse_id and me and want.startswith(me):
                corpse_id = self.our_corpse()
        elif self.our_corpse():
            corpse_id = self.our_corpse()
        label = name or str(corpse_id)
        action = Rez(corpse_id, row)
        enqueue_once(self.loop, world, action, f"rez:{label}")
