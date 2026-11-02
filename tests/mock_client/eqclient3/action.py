"""The action superclass. The scheduler and the bus only know this type."""

from __future__ import annotations

from collections.abc import Callable
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient3.loop import Loop
    from eqclient3.nav.path import Path
    from eqclient3.world import Mob, World

from eqclient3.structs import EQStruct, OP_Consider, OP_TargetMouse



def _consider_id(message: Message) -> int:
    payload = message.payload
    if isinstance(payload, OP_Consider):
        return int(payload.target_id)
    return 0


class Message:
    """One opcode in an action mailbox. opcode is the struct's class name."""

    __slots__ = ("payload",)

    def __init__(self, payload: EQStruct) -> None:
        self.payload = payload

    @property
    def opcode(self) -> str:
        return type(self.payload).__name__


class Action:
    def __init__(self) -> None:
        self.source = ""
        self.priority = 0
        self.insert = 0
        self.level: int | None = None
        self.started = 0.0
        self._world: World | None = None
        self.corpse_id: int | None = None
        self.where: tuple[float, float, float] | None = None
        self.partner = 0
        self.merchant_id = 0
        self.merchant_zone = ""
        self.merchant_point: tuple[float, float, float] | None = None
        self.count = 0
        self.zone = ""
        self.durable = False
        self.complete = False
        self.suspended = True
        self.yielding = False
        self.messages: list[Message] = []
        self.waiting: list[str] = []
        self.target_id = 0
        self.item_id = 0
        self.spawn_id: int | None = None
        self.task_text = ""
        self.name = ""
        self.description = ""
        self.active_path: Path | None = None
        self._gem_recast: dict[int, int] = {}
        self.limit: int | None = None
        self.consider_sent = False
        self.target_sent = False
        self.mob_targeted = 0

    def _hear(self, loop: Loop, world: World) -> None:
        return

    def step(self, loop: Loop, world: World) -> None:
        if not self.target_id:
            return

        mob = world.mobs.get(self.target_id)
        if not mob:
            return

        if self.mob_targeted != self.target_id:
            self.wait("TARGET")

        if not self.can_see_mob(world, loop, mob):
            return

        if not self.target_sent:
            loop.send("OP_TargetMouse", OP_TargetMouse(int(self.target_id) & 65535).serialize())
            self.target_sent = True
            return

        if not self.consider_sent:
            spawn = int(world.self_id or 0)
            loop.send(
                "OP_Consider", 
                OP_Consider(spawn, int(mob.id)).serialize(),
            )
            self.consider_sent = True
            return

        message = self.consume(
            "OP_Consider",
            lambda message: _consider_id(message) == int(self.target_id),
        )
        if message:
            mob.targeted = True
            self.mob_targeted = self.target_id  
            self.unwait("TARGET")
            self.consider_sent = False
            self.target_sent = False
            return

    def can_see_mob(self, world: World, loop: Loop, mob: Mob) -> bool:
        if world.line_of_sight(mob):
            return True
        
        if not self.active_path:
            self.active_path = world.movement.plan(mob, "run")
        
        world.movement.advance(loop, world, self.active_path)
        return False

    def wait(self, kind: str) -> None:
        pending = self._pending()
        if kind not in pending:
            pending.append(kind)

    def unwait(self, kind: str) -> None:
        pending = self._pending()
        if kind in pending:
            pending.remove(kind)

    def waiting_for(self, kind: str) -> bool:
        return kind in self._pending()

    def wait_label(self) -> str:
        return ",".join(self._pending())

    def _pending(self) -> list[str]:
        pending = self.waiting
        if isinstance(pending, list):
            return pending
        if isinstance(pending, str) and pending:
            self.waiting = [pending]
            return self.waiting
        self.waiting = []
        return self.waiting

    def consume(self, opcode: str, match: Callable[[Message], bool] | None = None) -> Message | None:
        for index, message in enumerate(self.messages):
            if message.opcode != opcode:
                continue
            if match and not match(message):
                continue
            return self.messages.pop(index)
        return None

    @property
    def completed(self) -> bool:
        return self.complete

    def add_message(self, message: Message) -> None:
        self.messages.append(message)

    def suspend(self) -> None:
        self.suspended = True

    def opcodes(self) -> tuple[str, ...]:
        return ()

    @staticmethod
    def key(action: Action) -> tuple[object, ...]:
        # Within one band, smaller runs first. Newest insert is the default.
        return (-action.insert,)
