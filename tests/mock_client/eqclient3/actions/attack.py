"""Band 300. One spawn. Heal and cure once, then engaged spells, then melee.

A meditating class sits when mana is below the floor. The gem bar keeps the
strongest scribed spell of each build role, and a gem waits out its recast.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient3.loop import Loop
    from eqclient3.world import Mob, World

from eqclient3.action import Action
from eqclient3.actions.casting import (
    ONCE,
    fill_bar,
    next_offense,
    sit_for_mana,
    stand,
    tick_recasts,
)
from eqclient3.log import log
from eqclient3.nav.path import STRIDE, straight
from eqclient3.structs import OP_AutoAttack, OP_CombatAbility, OP_Taunt
from eqclient3.actions.bots.reconstitute import Reconstitute
from eqclient3.actions.support import (
    BASH,
    KICK,
    MELEE,
    TAUNT,
    afflictions,
    arm_recast,
    bar_ratio,
    buff_faded,
    cast_spell,
    character_name,
    cures,
    known,
    lowest_hurt,
    memorized,
    queued,
    ready_gem,
    reclaim_if_ours,
    send_command,
    spawn_of,
    walk,
    yield_to,
)


def _apart(a: tuple[float, float, float], b: tuple[float, float, float]) -> float:
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5


def _treasure(mob: Mob | None) -> bool:
    """An LDoN object. Melee does not credit it. Opening it does."""
    if mob is None:
        return False
    if int(mob.class_id or 0) == 62:
        return True
    return "vermin nest" in (mob.name or "").lower()


class Attack(Action):

    def __init__(self, spawn_id: int, *, cautious: bool = False) -> None:
        super().__init__()
        self.priority = 300
        self.spawn_id = spawn_id
        self.target_id = spawn_id
        self.active_path = None
        self.suspended = True
        self.opened = False
        self.casting = False
        self.heal_requested = False
        self.cure_requested = False
        self.ability_ready: dict[str, int] = {}
        self.cautious = bool(cautious)
        self.level = 0
        self.cast_target = 0
        self._gem_recast: dict[int, int] = {}
        self.landed: set[str] = set()
        self.resting = False
        self.anchor: tuple[float, float] | None = None
        self.still = 0
        self.target_tries = 0
        self.closed = False
        self.attacking = False
        self.planned: tuple[float, float, float] | None = None
        self.swing_hp = -1
        self.swing_still = 0
        self.misses = 0
        self.zero_hp = 0

    def __setstate__(self, state: dict[str, object]) -> None:
        self.__dict__.update(state)
        if "landed" not in self.__dict__:
            self.landed = set()
        if "resting" not in self.__dict__:
            self.resting = False
        if "target_tries" not in self.__dict__:
            self.target_tries = 0
        if "closed" not in self.__dict__:
            self.closed = False
        if "attacking" not in self.__dict__:
            self.attacking = False
        if "planned" not in self.__dict__:
            self.planned = None
        if "swing_hp" not in self.__dict__:
            self.swing_hp = -1
        if "swing_still" not in self.__dict__:
            self.swing_still = 0
        if "misses" not in self.__dict__:
            self.misses = 0
        if "zero_hp" not in self.__dict__:
            self.zero_hp = 0

    def opcodes(self) -> tuple[str, ...]:
        return (
            "OP_Consider",
            "OP_BecomeCorpse",
            "OP_HPUpdate",
            "OP_MobHealth",
            "OP_Buff",
            "OP_SimpleMessage",
        )

    def suspend(self) -> None:
        self.active_path = None
        self.opened = False
        self.attacking = False
        self.suspended = True

    @staticmethod
    def key(action: Action) -> tuple[int, int]:
        return (-int(action.level or 0), int(action.insert))

    def step(self, loop: Loop, world: World) -> None:
        super().step(loop, world)
        spawn = self.spawn_id
        mob = world.mobs.get(spawn) if spawn is not None else None
        if mob is not None:
            self.level = int(mob.level or 0)
        if self._become_corpse(loop, world):
            return
        tick_recasts(self)
        self._bars(world)
        self._cure_flag(world)
        self._string_251(loop, world)
        if not self.waiting_for("CAST") and fill_bar(loop, world):
            return
        self._request_heal(loop, world)
        self._request_cure(loop, world)
        if self.waiting_for("CAST") or self.casting:
            if not self.messages:
                return
            self.unwait("CAST")
            self.casting = False
        if mob is not None and _treasure(mob) and float(mob.distance) <= 25:
            # Opening uses the current target. Consider never answers an object,
            # and the nest is often out of the mesh's line of sight, so neither
            # of those waits can gate the open. The server only checks distance.
            if not mob.targeted:
                self.target_mob(loop, world)
            loop.send("OP_LDoNOpen", b"")
            return
        if self.waiting_for("TARGET"):
            # A treasure object answers consider with its name and no packet.
            self.target_tries += 1
            if self.target_tries < 30:
                return
            self.unwait("TARGET")
            self.target_tries = 0
        else:
            self.target_tries = 0
        if mob is None or mob.dead:
            if mob is not None and mob.dead:
                self._reconstitute(loop, world)
            self.complete = True
            return
        if int(mob.hp or 0) == 0 and not _treasure(mob):
            self.zero_hp += 1
            if self.zero_hp >= 10:
                target = self.spawn_id
                if target is not None:
                    log.info("attack dead spawn=%s", target)
                    world.skip_spawn(target)
                self.complete = True
                return
        else:
            self.zero_hp = 0
        sees = world.line_of_sight(mob)
        if self.closed and not sees:
            self.closed = False
        if not self.closed and (float(mob.distance) > MELEE or not sees):
            if self._stuck(world):
                if float(mob.distance) <= 25 and sees:
                    self.closed = True
                elif float(mob.distance) <= 25:
                    self.attacking = False
                    self.active_path = None
                    self.planned = None
                    walk(self, loop, world, mob.position, "los")
                    return
                else:
                    target = self.spawn_id
                    if target is not None:
                        log.info("attack unstick spawn=%s d=%.0f", target, mob.distance)
                        world.skip_spawn(target)
                    self.complete = True
                    return
            else:
                self.attacking = False
                point = mob.position
                planned = self.planned
                if planned is None or _apart(planned, point) > 15:
                    self.active_path = None
                    self.planned = point
                if sees and float(mob.distance) <= 35:
                    length = STRIDE["los"][0]
                    path = straight((world.x, world.y, world.z), point, length)
                    self.active_path = path
                    world.movement.advance(loop, world, path)
                    return
                mode = "walk" if self.cautious else "los"
                walk(self, loop, world, point, mode)
                return
        self.still = 0
        self.anchor = None
        if self._hp_stuck(mob):
            self.misses += 1
            self.attacking = False
            self.closed = False
            self.active_path = None
            self.planned = None
            if self.misses >= 3:
                target = self.spawn_id
                if target is not None:
                    log.info("attack no damage spawn=%s d=%.0f", target, mob.distance)
                    world.skip_spawn(target)
                self._reconstitute(loop, world)
                self.complete = True
                return
            walk(self, loop, world, mob.position, "los")
            return
        world.movement.face(loop, world, mob.position)
        # Class 62 is an LDoN object. Melee never puts the player on its hate list,
        # so the kill does not credit a task. Opening it does.
        if _treasure(mob):
            loop.send("OP_LDoNOpen", b"")
            return
        if not self.opened:
            send_command(loop, "^attack")
            self.opened = True
        self.suspended = False
        if self._combat_spell(loop, world):
            self.attacking = False
            return
        # Each OP_AutoAttack(1) restarts the swing timer. Send it once per engagement.
        if not self.attacking:
            loop.send("OP_AutoAttack", OP_AutoAttack(1).serialize())
            self.attacking = True
        self._ability(loop, world)

    def _hp_stuck(self, mob: Mob) -> bool:
        """True when melee has not moved the target's health."""
        hp = int(mob.hp or 0)
        if hp != self.swing_hp:
            self.swing_hp = hp
            self.swing_still = 0
            return False
        self.swing_still += 1
        if self.swing_still < 40:
            return False
        self.swing_still = 0
        return True

    def _stuck(self, world: World) -> bool:
        """True after five seconds on the same spot, still out of melee."""
        here = (round(world.x, 1), round(world.y, 1))
        if here == self.anchor:
            self.still += 1
        else:
            self.anchor = here
            self.still = 0
        if self.still < 50:
            return False
        self.active_path = None
        self.still = 0
        return True

    def _become_corpse(self, loop: Loop, world: World) -> bool:
        corpse = self.consume("OP_BecomeCorpse", lambda message: spawn_of(message) in (0, self.spawn_id))
        if corpse is None:
            return False
        self._reconstitute(loop, world)
        self.complete = True
        return True

    def _reconstitute(self, loop: Loop, world: World) -> None:
        """The party is rebuilt before anyone sits. A resolved row from the last fight can run again."""
        source = f"reconstitute:{int(self.spawn_id or 0)}"
        journal = loop.journal
        who = character_name(loop, world)
        if journal is not None and who:
            journal.clear_source(who, source)
        yield_to(self, loop, world, Reconstitute(241), source)

    def _bars(self, world: World) -> None:
        message = self.consume("OP_HPUpdate") or self.consume("OP_MobHealth")
        if message is None:
            return
        fraction = bar_ratio(message)
        if fraction is not None and fraction > 0.5:
            self.heal_requested = False

    def _cure_flag(self, world: World) -> None:
        message = self.consume("OP_Buff")
        if message is None:
            return
        if buff_faded(message) or not afflictions(world):
            self.cure_requested = False

    def _string_251(self, loop: Loop, world: World) -> None:
        if reclaim_if_ours(self, loop, world, int(self.cast_target or 0)):
            self.heal_requested = False
            self.cure_requested = False

    def _request_heal(self, loop: Loop, world: World) -> None:
        if self.heal_requested:
            return
        target = lowest_hurt(world)
        if target is None:
            return
        gem = next((row for row in memorized(world, self) if row.heal), None)
        if gem is None or not ready_gem(world, gem):
            return
        cast_spell(loop, gem, target)
        self.cast_target = int(target)
        self.heal_requested = True
        arm_recast(self, gem)

    def _request_cure(self, loop: Loop, world: World) -> None:
        if self.cure_requested:
            return
        rows = afflictions(world)
        if not rows:
            return
        effect = rows[0][1] if isinstance(rows[0], tuple) else rows[0].effect
        entity = rows[0][0] if isinstance(rows[0], tuple) else rows[0].entity
        gem = next((row for row in memorized(world, self) if cures(row, effect)), None)
        if gem is None or not ready_gem(world, gem):
            return
        cast_spell(loop, gem, int(entity or 0))
        self.cast_target = int(entity or 0)
        self.cure_requested = True
        arm_recast(self, gem)

    def _combat_spell(self, loop: Loop, world: World) -> bool:
        if sit_for_mana(loop, world):
            self.resting = True
            return True
        if self.resting:
            stand(loop, world)
            self.resting = False
        choice = next_offense(world, self, self.landed)
        if choice is None:
            return False
        cast_spell(loop, choice.gem, choice.target)
        self.cast_target = choice.target
        self.casting = True
        self.wait("CAST")
        arm_recast(self, choice.gem)
        if choice.role in ONCE:
            self.landed.add(choice.role)
        return True

    def _ability(self, loop: Loop, world: World) -> None:
        spawn = self.spawn_id
        if not spawn:
            return
        tick = int(loop.tick or 0)
        reclaiming = queued(loop, "Reclaim")
        if not reclaiming and self.ability_ready.get("taunt", 0) <= tick and known(world, TAUNT):
            loop.send("OP_Taunt", OP_Taunt(spawn).serialize())
            self.ability_ready["taunt"] = tick + 60
            return
        if self.ability_ready.get("kick", 0) <= tick and known(world, KICK):
            loop.send(
                "OP_CombatAbility",
                OP_CombatAbility(spawn, skill=KICK).serialize(),
            )
            self.ability_ready["kick"] = tick + 60
            return
        abilities = world.character.abilities
        if (
            self.ability_ready.get("bash", 0) <= tick
            and known(world, BASH)
            and (abilities.can_bash or abilities.shield or abilities.two_hand)
        ):
            loop.send(
                "OP_CombatAbility",
                OP_CombatAbility(spawn, skill=BASH).serialize(),
            )
            self.ability_ready["bash"] = tick + 60
