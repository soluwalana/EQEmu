"""Band 200. One eat, forage, fish, or bandage. An empty forage at water starts fishing."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient3.loop import Loop
    from eqclient3.world import World

from eqclient3.action import Action
from eqclient3.actions.support import at_water, yield_to
from eqclient3.structs import OP_Bind_Wound, OP_Consume, OP_Fishing, OP_Forage


class Field(Action):

    def __init__(self, kind: str, slot: int | None = None) -> None:
        super().__init__()
        self.priority = 200
        self.kind = kind
        self.slot = slot

    def opcodes(self) -> tuple[str, ...]:
        return ()

    def suspend(self) -> None:
        self.suspended = True

    def step(self, loop: Loop, world: World) -> None:
        self.suspended = False
        opcode, payload = _packet(self.kind, world, self.slot)
        loop.send(opcode, payload)
        if self.kind == "forage" and world.forage_found is False and at_water(world):
            yield_to(self, loop, world, Field("fish"), "field:fish")
        self.complete = True


def _packet(kind: str, world: World, slot: int | None) -> tuple[str, bytes]:
    if kind == "eat":
        return ("OP_Consume", OP_Consume(slot or 0, 1).serialize())
    if kind == "forage":
        return ("OP_Forage", OP_Forage().serialize())
    if kind == "fish":
        return ("OP_Fishing", OP_Fishing().serialize())
    if kind == "bandage":
        return ("OP_Bind_Wound", OP_Bind_Wound(int(world.self_id or 0)).serialize())
    return ("OP_Forage", OP_Forage().serialize())
