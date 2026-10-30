"""OP_Consider writes consider on that Mob and appends nothing."""

from __future__ import annotations

from eqclient3.handler import Handler
from eqclient3.handlers.common import find_mob
from eqclient3.structs import EQStruct, OP_Consider
from eqclient3.world import Consider

# Server standing after the RoF2 6↔9 / 7↔8 swap is undone.
STANDING = {
    1: "ally",
    2: "warmly",
    3: "kindly",
    4: "amiably",
    5: "indifferent",
    6: "apprehensive",
    7: "dubious",
    8: "threatening",
    9: "scowls",
}


class ConsiderHandler(Handler):
    opcodes = ("OP_Consider",)

    def on(self, opcode: str, payload: EQStruct) -> None:
        del opcode
        if not isinstance(payload, OP_Consider):
            return
        mob = find_mob(self.world, payload.target_id)
        if not mob:
            return
        row = Consider(payload.faction, payload.level)
        row.name = STANDING.get(row.standing, "")
        mob.consider = row
