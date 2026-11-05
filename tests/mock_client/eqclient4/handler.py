"""The handler superclass. The bus only knows this type.

A subclass in eqclient4.handlers lists its opcodes and joins the bus when the
handlers package is imported. One opcode may belong to more than one handler.
"""

import importlib
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient4.loop import Loop
    from eqclient4.world import World

from eqclient4.handlers import MODULES
from eqclient4.log import log
from eqclient4.structs import EQStruct


class Handler:
    opcodes: tuple[str, ...] = ()
    # Opcodes this handler owns. The bus does not also mail them to subscribers.
    exclusive: tuple[str, ...] = ()
    _kinds: list[type[Handler]] = []

    world: World
    loop: Loop

    def __init_subclass__(cls, **kwargs: object) -> None:
        super().__init_subclass__(**kwargs)
        if not cls.opcodes:
            return
        if not cls.__module__.startswith("eqclient4.handlers."):
            return
        if cls in Handler._kinds:
            return
        Handler._kinds.append(cls)

    def handle(
        self,
        opcode: str,
        payload: EQStruct,
        world: World,
        loop: Loop,
    ) -> None:
        """Store the sheet and call on. Bytes for a known opcode are decoded here so a direct call sees the struct."""
        self.world = world
        self.loop = loop
        self.on(opcode, payload)

    def on(self, opcode: str, payload: EQStruct) -> None:
        return

    def deliver_waiters(self, payload: EQStruct) -> None:
        """The struct goes to every subscriber, and to the active action once."""
        opcode = type(payload).__name__
        sent: set[int] = set()
        for action in self.loop.queue:
            listed = action.opcodes()
            if opcode not in listed:
                continue
            action.add_message(payload)
            sent.add(id(action))

        active = self.loop.active
        if active and id(active) not in sent:
            active.add_message(payload)

    @classmethod
    def registered(cls) -> list[type[Handler]]:
        """Handler classes in bus order. Importing the package is what registers them."""
        for name in MODULES:
            importlib.import_module(f"eqclient4.handlers.{name}")
        by_module = {kind.__module__.rsplit(".", 1)[-1]: kind for kind in cls._kinds}
        return [by_module[name] for name in MODULES if name in by_module]
