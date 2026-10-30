"""Band 230, ahead of a seat. Accept the rez once. OP_DeleteSpawn finishes it."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient3.loop import Loop
    from eqclient3.world import World


from eqclient3.action import Action
from eqclient3.structs import OP_RezzAnswer, OP_RezzRequest
from eqclient3.actions.support import spawn_of


class Rez(Action):
    def __init__(self, corpse_id: int, payload: OP_RezzRequest | bytes | None = None) -> None:
        super().__init__()
        self.priority = 230
        self.durable = True
        self.corpse_id = int(corpse_id)
        self.payload = _request(payload)
        self.accepted = False

    def opcodes(self) -> tuple[object, ...]:
        return ("OP_DeleteSpawn",)

    def suspend(self) -> None:
        self.suspended = True

    @staticmethod
    def key(action: Action) -> tuple[object, ...]:
        return (0,)

    def step(self, loop: Loop, world: World) -> None:
        if self.consume("OP_DeleteSpawn", lambda message: spawn_of(message) in (0, self.corpse_id)):
            self.complete = True
            return
        self.suspended = False
        if self.accepted:
            return
        try:
            request = _request(self.payload)
            answer = OP_RezzAnswer(
                request.zone_id,
                request.instance_id,
                request.x,
                request.y,
                request.z,
                request.your_name,
                request.unknown88,
                request.rezzer_name,
                request.spell_id,
                request.corpse_name,
                1,
                request.unknown00,
            )
        except (ValueError, AttributeError):
            answer = OP_RezzAnswer()
            answer.action = 1
        loop.send("OP_RezzAnswer", answer.serialize())
        self.accepted = True


def _request(payload: OP_RezzRequest | bytes | None) -> OP_RezzRequest:
    """The request fields. Stored bytes from an older journal still parse."""
    if isinstance(payload, OP_RezzRequest):
        return payload
    if isinstance(payload, (bytes, bytearray)) and payload:
        try:
            return OP_RezzRequest.deserialize(bytes(payload))
        except ValueError:
            return OP_RezzRequest()
    return OP_RezzRequest()
