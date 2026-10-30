"""A corpse we attacked, or that aggroed us, appends LootMob. Our corpse does not. Coin is written here."""

from __future__ import annotations

from eqclient3.actions.loot_mob import LootMob
from eqclient3.handlers.common import find_mob, is_ours, enqueue_once, queue_of
from eqclient3.structs import EQStruct, OP_BecomeCorpse, OP_MoneyOnCorpse
from eqclient3.handler import Handler

NORMAL = (1, 3)


class LootHandler(Handler):
    opcodes = ("OP_BecomeCorpse", "OP_MoneyOnCorpse")

    def on(self, opcode: str, payload: EQStruct) -> None:
        del opcode
        if isinstance(payload, OP_BecomeCorpse):
            self.corpse(payload)
        elif isinstance(payload, OP_MoneyOnCorpse):
            self.coin(payload)

    def corpse(self, row: OP_BecomeCorpse) -> None:
        world = self.world
        spawn_id, x, y, z = row.spawn_id, row.x, row.y, row.z
        mob = find_mob(world, spawn_id)
        if is_ours(world, spawn_id, mob, self.loop):
            return
        if not self.fought(spawn_id):
            return
        if mob and mob.npc == 0 and (not mob.dead):
            return
        where = (x, y, z)
        enqueue_once(self.loop, world, LootMob(spawn_id, where), f"loot_mob:{spawn_id}")

    def fought(self, spawn_id: int) -> bool:
        """True when we attacked this spawn, or it dealt aggro to us."""
        if spawn_id in self.world.fought:
            return True
        for action in queue_of(self.loop):
            if type(action).__name__ not in ("Attack", "Hold"):
                continue
            if action.spawn_id == spawn_id:
                return True
        return False

    def coin(self, row: OP_MoneyOnCorpse) -> None:
        if row.response not in NORMAL:
            return
        if not (row.platinum or row.gold or row.silver or row.copper):
            return
        self.world.add_coin(row.platinum, row.gold, row.silver, row.copper)
