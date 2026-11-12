"""Opcode bus. One opcode can have many handlers. Subscription does not swallow the packet."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient4.loop import Loop, Schedule
    from eqclient4.world import World

from eqclient4.handler import Handler
from eqclient4.log import log, note_comms
from eqclient4.structs import EQStruct, bytes_to_eqstruct, hexdump


class Bus:

    def __init__(
        self,
        queue: Schedule,
        world: World,
        loop: Loop,
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

    def publish(self, opcode: str, payload: bytes | bytearray) -> None:
        """Handlers first, then movement when the opcode is in its list, then actions.

        Bytes for a known opcode are deserialized once. Handlers, movement, and
        the mailbox see that struct. A failed decode does not call them. An
        exclusive opcode still claims the packet. An int or an unknown opcode
        stays off the handlers and the mailbox.
        """
        if self._autoload:
            self.load()

        note_comms("incomming bus", opcode, payload, False)

        parsed = bytes_to_eqstruct(opcode, payload)
        if not parsed:
            log.error(f"Opcode {opcode} is not a struct\n{hexdump(payload)}")
            return

        claimed = False

        for handler in self._handlers:
            if opcode not in handler.opcodes:
                continue

            handler_name = type(handler).__name__
            note_comms(f"handler {handler_name}", opcode, parsed, False)
            handler.handle(opcode, parsed, self.world, self.loop)
            if opcode in handler.exclusive:
                claimed = True

        _movement(self.world, opcode, parsed)

        if claimed:
            log.debug(f"Exclusively claimed opcode {opcode}")
            return

        for action in self.queue:
            if opcode in action.opcodes():
                action.add_message(parsed)


def _movement(world: World, opcode: str, payload: EQStruct) -> None:
    mover = world.movement
    if opcode not in mover.opcodes():
        return
    note_comms("movement", opcode, payload, False)
    mover.handle(opcode, payload)
