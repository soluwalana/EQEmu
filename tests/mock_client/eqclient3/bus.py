"""Opcode bus. One opcode can have many handlers. Subscription does not swallow the packet."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient3.loop import Loop
    from eqclient3.schedule import Schedule
    from eqclient3.world import World

from eqclient3.action import Message
from eqclient3.handler import Handler
from eqclient3.net.decode import body
from eqclient3.structs import EQStruct, ZONE_ENTRY_SIZE
from eqclient3.trace import note_comms
from eqclient3.log import log


class Bus:

    def __init__(
        self,
        queue: Schedule | None = None,
        world: World | None = None,
        loop: Loop | None = None,
        autoload: bool = True,
    ) -> None:
        self.queue = queue
        self.world = world
        self.loop = loop
        self._autoload = autoload
        self._handlers_loaded = False
        self._handlers: list[Handler] = []

    def register(self, handler: Handler) -> None:
        self._handlers.append(handler)

    def load(self) -> None:
        """Register one instance of every handler class, in package order."""
        if self._handlers_loaded:
            return
        self._handlers_loaded = True
        for kind in Handler.registered():
            self.register(kind())

    def publish(self, opcode: str, payload: object) -> None:
        """Handlers first, then movement when the opcode is in its list, then actions.

        Bytes for a known opcode are deserialized once. Handlers, movement, and
        the mailbox see that struct. A failed decode does not call them. An
        exclusive opcode still claims the packet. An int or an unknown opcode
        stays off the handlers and the mailbox.
        """
        if self._autoload:
            self.load()
        note_comms("incomming bus", opcode, payload, False)
        if opcode == "OP_ZoneEntry" and isinstance(payload, (bytes, bytearray)) and len(payload) > ZONE_ENTRY_SIZE:
            log.debug("OP_ZoneEntry is too big, converting to OP_NewSpawn")
            opcode = "OP_NewSpawn"
        parsed = _struct(opcode, payload)
        claimed = False
        world = self.world
        loop = self.loop
        for handler in self._handlers:
            if opcode not in handler.opcodes:
                continue
            if isinstance(parsed, EQStruct) and world is not None and loop is not None:
                handler_name = type(handler).__name__
                note_comms(f"handler {handler_name}", opcode, parsed, False)
                handler.handle(opcode, parsed, world, loop)
            if opcode in handler.exclusive:
                claimed = True
        if isinstance(parsed, EQStruct):
            _movement(self.world, opcode, parsed)

        if claimed:
            log.debug(f"Exclusively claimed opcode {opcode}")
            return

        if not isinstance(parsed, EQStruct):
            log.debug(f"Opcode {opcode} wasn't a struct")
            return
        
        queue = self.queue
        if not queue:
            log.debug("No queue skipping OPCode -> action distribution")
            return
        
        for action in queue:
            if opcode in action.opcodes():
                action.add_message(Message(parsed))


def _struct(opcode: str, payload: object) -> EQStruct | None:
    """The one decode for this publish. None means this publish is not a struct."""
    if isinstance(payload, EQStruct):
        return payload
    return body(opcode, payload)


def _movement(world: World | None, opcode: str, payload: EQStruct) -> None:
    mover = world.movement if world else None
    if mover is None:
        return
    if opcode not in mover.opcodes():
        return
    note_comms("movement", opcode, payload, False)
    mover.handle(opcode, payload, world)
