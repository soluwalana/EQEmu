"""Band 270. Our corpse: drag inside 45 yards, then loot, then bury."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient3.loop import Loop
    from eqclient3.world import Mob, World

from eqclient3.action import Action
from eqclient3.log import log
from eqclient3.structs import Item, OP_EndLootRequest, OP_LootRequest
from eqclient3.actions.bots.summon import Summon
from eqclient3.actions.rez import Rez
from eqclient3.actions.support import (
    CORPSE_NEAR,
    HOSTILE_CLOSE,
    HOSTILE_FAR,
    corpse_drag,
    corpse_name,
    hostiles_within,
    in_tutorial,
    ingest_corpse_mail,
    loot_packet,
    message_text,
    queued,
    walk,
    yield_to,
)
from eqclient3.inventory.assign import assign as run_assign


class Reclaim(Action):

    def __init__(self, corpse_id: int, where: tuple[float, float, float]) -> None:
        super().__init__()
        self.priority = 270
        self.durable = True
        self.corpse_id = corpse_id
        self.target_id = corpse_id
        self.where = where
        self._world: World | None = None
        self.active_path = None
        self.requested = False
        self.opened = False
        self.dragged = False
        self.slots: list[Item] = []
        self.quiet = 0
        self.tries = 0
        self.anchor: tuple[float, float] | None = None
        self.still = 0

    def __setstate__(self, state: dict[str, object]) -> None:
        self.__dict__.update(state)
        if "quiet" not in self.__dict__:
            self.quiet = 0
        if "tries" not in self.__dict__:
            self.tries = 0
        if "anchor" not in self.__dict__:
            self.anchor = None
        if "still" not in self.__dict__:
            self.still = 0

    def opcodes(self) -> tuple[str, ...]:
        return (
            "OP_Consider",
            "OP_ItemPacket",
            "OP_MoneyOnCorpse",
            "OP_ChannelMessage",
            "OP_SpecialMesg",
            "OP_SimpleMessage",
        )

    @staticmethod
    def key(action: Action) -> tuple[float, ...]:
        if isinstance(action, Reclaim):
            return (action.distance,)
        return (0.0,)

    @property
    def distance(self) -> float:
        world = self._world
        corpse_id = self.corpse_id
        if not world or not corpse_id:
            return 0.0
        spot = _corpse_spot(world, corpse_id, self.where)
        if spot is None:
            return 0.0
        return world.movement.plan(spot).distance

    def suspend(self) -> None:
        self.active_path = None
        self.suspended = True

    def step(self, loop: Loop, world: World) -> None:
        # A corpse in the mine is behind the task book. Chasing it walks into the camp.
        if in_tutorial(world):
            self.priority = -1
            return
        self.priority = 270
        self._world = world
        self._inbox()
        if self._gone():
            self.complete = True
            return
        if self.waiting_for("LOOT"):
            self.waited += 1
            if self.waited < 30:
                return
            # The corpse was not lootable yet, or we asked from the bind point.
            self.waited = 0
            self.requested = False
            self.opened = False
            self.unwait("LOOT")
        corpse_id = self.corpse_id
        if corpse_id is None:
            return
        if world.level > 10 and (not queued(loop, "Rez", corpse_id=corpse_id)):
            payload = world.rezz_payload or b""
            yield_to(self, loop, world, Rez(corpse_id, payload), f"rez:{corpse_id}")
        spot = _corpse_spot(world, corpse_id, self.where)
        if spot is None or world.movement.plan(spot).distance > CORPSE_NEAR:
            # Left the ring. The next time we are inside 45 yards, drag again.
            self.dragged = False
            self._approach(loop, world, spot)
            return
        if not self.dragged:
            # OP_CorpseDrag is Corpse::Summon. It pulls the body to our feet.
            loop.send(
                "OP_CorpseDrag",
                corpse_drag(corpse_name(world, corpse_id), world.name),
            )
            self.dragged = True
            self.suspended = False
            return
        if not self.requested:
            loop.send("OP_LootRequest", OP_LootRequest(corpse_id).serialize())
            self.requested = True
            self.wait("LOOT")
            self.suspended = False
            return
        self.suspended = False
        if self.slots:
            slot = self.slots.pop(0)
            loop.send("OP_LootItem", loot_packet(corpse_id, world.self_id, slot.slot))
            return
        if not self.opened:
            # A request that never opened the window would spin here forever.
            self.quiet += 1
            if self.quiet < 20:
                return
            self.quiet = 0
            self.tries += 1
            if self.tries >= 4:
                log.info("reclaim no window corpse=%s", corpse_id)
                self.complete = True
                return
            # The summon is what lets the window open. Ask for the body again.
            self.requested = False
            self.dragged = False
            return
        loop.send("OP_EndLootRequest", OP_EndLootRequest(corpse_id).serialize())
        run_assign(loop, world)
        self.complete = True

    def _inbox(self) -> None:
        ingest_corpse_mail(self)

    def _gone(self) -> bool:
        """The id is not a corpse, or the corpse has left the zone.

        Standing on the old point will not bring it back. The server says
        "Corpse not found" for a despawned id and "not a corpse" when that id
        is now something else.
        """
        while True:
            message = (
                self.consume("OP_ChannelMessage") or self.consume("OP_SpecialMesg") or self.consume("OP_SimpleMessage")
            )
            if message is None:
                return False
            if _missing(message_text(message)):
                return True

    def _approach(self, loop: Loop, world: World, spot: tuple[float, float, float] | None) -> None:
        here = (round(world.x, 1), round(world.y, 1))
        if here == self.anchor:
            self.still += 1
        else:
            self.anchor = here
            self.still = 0
        if self.still >= 40:
            log.info("reclaim unstick corpse=%s", self.corpse_id)
            self.active_path = None
            self.complete = True
            return
        mover = world.movement
        seen = mover.visible_mobs(yards=HOSTILE_FAR)
        on_path = mover.mobs_on_path(seen) or []
        close = hostiles_within(seen, HOSTILE_CLOSE) + hostiles_within(on_path, HOSTILE_CLOSE)
        far = hostiles_within(seen, HOSTILE_FAR) + hostiles_within(on_path, HOSTILE_FAR)
        if close and (not queued(loop, "Summon")):
            yield_to(self, loop, world, Summon(271), f"summon:{self.corpse_id}")
            return
        if close:
            hostile = close[0]
            walk(self, loop, world, hostile.position, "walk")
            if world.line_of_sight(hostile):
                self._cautious_attack(loop, world, hostile)
            self.suspended = False
            return
        if spot is None:
            return
        mode = "walk" if far else "run"
        walk(self, loop, world, spot, mode)

    def _cautious_attack(self, loop: Loop, world: World, mob: Mob) -> None:
        # Attack constructs Reclaim, so this import stays in the method.
        from eqclient3.actions.attack import Attack
        from eqclient3.handlers.common import attack_for, mark_fight

        spawn = int(mob.id or 0)
        if not spawn or attack_for(loop, Attack, spawn):
            return
        attack = Attack(spawn, cautious=True)
        mark_fight(world, spawn)
        attack.level = int(mob.level or 0)
        yield_to(self, loop, world, attack, f"aggro:{spawn}")


def _corpse_spot(
    world: World, corpse_id: int, saved: tuple[float, float, float] | None
) -> tuple[float, float, float] | None:
    """The live body when we can see it, otherwise the point saved at death."""
    mob = world.mobs.get(corpse_id)
    if mob is not None:
        return mob.position
    return saved


def _missing(text: str) -> bool:
    lowered = text.lower()
    return "corpse not found" in lowered or "not a corpse" in lowered
