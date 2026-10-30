"""The handler superclass. The bus only knows this type.

A subclass in eqclient3.handlers lists its opcodes and joins the bus when the
handlers package is imported. One opcode may belong to more than one handler.
"""

from __future__ import annotations

import importlib
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient3.loop import Loop
    from eqclient3.world import World

from eqclient3.log import log
from eqclient3.handlers import MODULES
from eqclient3.handlers.common import active_action, deliver, queue_of
from eqclient3.net.decode import body
from eqclient3.structs import EQStruct


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
        if not cls.__module__.startswith("eqclient3.handlers."):
            return
        if cls in Handler._kinds:
            return
        Handler._kinds.append(cls)

    def handle(
        self,
        opcode: str,
        payload: EQStruct | bytes | bytearray,
        world: World,
        loop: Loop,
    ) -> None:
        """Store the sheet and call on. Bytes for a known opcode are decoded here so a direct call sees the struct."""
        self.world = world
        self.loop = loop
        if isinstance(payload, (bytes, bytearray)):
            parsed = body(opcode, payload)
            if not isinstance(parsed, EQStruct):
                return
            payload = parsed
        elif not isinstance(payload, EQStruct):
            return
        self.on(opcode, payload)

    def on(self, opcode: str, payload: EQStruct) -> None:
        return

    def deliver_waiters(self, payload: EQStruct) -> None:
        """The struct goes to every subscriber, and to the active action once."""
        loop = self.loop
        opcode = type(payload).__name__
        sent: set[int] = set()
        for action in queue_of(loop):
            try:
                listed = action.opcodes()
            except AttributeError:
                log.error("queued action has no opcodes", exc_info=True)
                continue
            if opcode not in listed:
                continue
            deliver(action, payload)
            sent.add(id(action))
        active = active_action(loop)
        if active is not None and id(active) not in sent:
            deliver(active, payload)

    @classmethod
    def registered(cls) -> list[type[Handler]]:
        """Handler classes in bus order. Importing the package is what registers them."""
        for name in MODULES:
            importlib.import_module(f"eqclient3.handlers.{name}")
        by_module = {kind.__module__.rsplit(".", 1)[-1]: kind for kind in cls._kinds}
        return [by_module[name] for name in MODULES if name in by_module]
