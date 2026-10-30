"""OP_Consider writes consider on that Mob and appends nothing."""

from __future__ import annotations

from eqclient3.handlers.common import find_mob
from eqclient3.structs import EQStruct, OP_Consider
from eqclient3.handler import Handler


# Server standing after the Titanium 6↔9 / 7↔8 swap is undone.
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


class Consider:
    """Standing and level color. The standing is not a faction id."""

    def __init__(self, standing: int, level_color: int) -> None:
        self.standing = standing
        self.level_color = level_color
        self.name = STANDING.get(self.standing, "")


class ConsiderHandler(Handler):
    opcodes = ("OP_Consider",)

    def on(self, opcode: str, payload: EQStruct) -> None:
        del opcode
        if not isinstance(payload, OP_Consider):
            return
        mob = find_mob(self.world, payload.target_id)
        if not mob:
            return
        mob.consider = Consider(payload.faction, payload.level)
