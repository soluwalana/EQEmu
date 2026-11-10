"""Band 300. One spawn. Heal and cure once, then engaged spells, then melee.

A meditating class sits when mana is below the floor. The gem bar keeps the
strongest scribed spell of each build role, and a gem waits out its recast.
"""

import time
from enum import IntEnum
from typing import TYPE_CHECKING, Callable

if TYPE_CHECKING:
    from eqclient4.loop import Loop
    from eqclient4.world import Mob, World

from eqclient4.action import Action
from eqclient4.log import log
from eqclient4.nav.path import STRIDE, straight
from eqclient4.structs import (
    EQStruct,
    OP_AutoAttack,
    OP_BecomeCorpse,
    OP_CombatAbility,
    OP_LDoNOpen,
    OP_Taunt,
    simple_id_matcher,
)

# from eqclient4.actions.bots.reconstitute import Reconstitute
# from eqclient4.actions.casting import (
#     ONCE,
#     fill_bar,
#     next_offense,
#     sit_for_mana,
#     stand,
#     tick_recasts,
# )
# from eqclient4.actions.support import (
#     BASH,
#     KICK,
#     MELEE,
#     TAUNT,
#     afflictions,
#     arm_recast,
#     bar_ratio,
#     buff_faded,
#     cast_spell,
#     cures,
#     known,
#     lowest_hurt,
#     memorized,
#     queued,
#     ready_gem,
#     reclaim_if_ours,
#     send_command,
#     spawn_of,
#     walk,
# )
from eqclient4.structs.constants import MELEE, CombatAASkill, CombatSkill, Skill


def _apart(a: tuple[float, float, float], b: tuple[float, float, float]) -> float:
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5


# Reuse times for various skills, here for convenience, in sec
# set to 0 to disable server side checking of timers.
# from features.h
REUSE_TIMES: dict[CombatSkill, int] = {
    CombatSkill.FEIGN_DEATH: 9,
    CombatSkill.HIDE: 8,
    CombatSkill.TAUNT: 5,
    CombatSkill.BASH: 5,
    CombatSkill.BACKSTAB: 9,
    CombatSkill.KICK: 5,
    CombatSkill.TAIL_RAKE: 6,
    CombatSkill.EAGLE_STRIKE: 5,
    CombatSkill.ROUND_KICK: 9,
    CombatSkill.TIGER_CLAW: 6,
    CombatSkill.FLYING_KICK: 7,
    CombatSkill.FRENZY: 10,
    CombatSkill.INTIMIDATION: 9,
}

# Non combat skills that we need to practice elsewhere
# Skill.SNEAK: 7,
# Skill.FORAGE: 50,
# Skill.MEND: 360,
# Skill.SENSE_TRAPS: 9,
# Skill.DISARM_TRAPS: 9,

# Special skills that we don't handle yet
# Skill.HARM_TOUCH: 4300,
# Skill.LAY_ON_HANDS: 4300,


class Attack(Action):

    def __init__(
        self,
        world: World,
        loop: Loop,
        target_id: int,
        *,
        cautious: bool = False,
    ) -> None:
        super().__init__(world, loop)
        self.priority = 300
        self.target_id = target_id
        self.active_path = None
        self.opened = False
        self.casting = False
        self.heal_requested = False
        self.cure_requested = False
        self.ability_ready: dict[CombatSkill, float] = {}
        self.cautious = bool(cautious)

        self.mob: Mob | None = None
        self.cast_target = 0
        self._gem_recast: dict[int, int] = {}
        self.landed: set[str] = set()
        self.resting = False
        self.anchor: tuple[float, float] | None = None
        self.still = 0

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
        return super().opcodes() + (
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
        self._loop.send("OP_AutoAttack", OP_AutoAttack(0).serialize())
        self.attacking = False
        self.suspended = True

    @staticmethod
    def key(action: Action) -> tuple[int, int]:
        if isinstance(action, Attack):
            return ((-action.level or 0), action.insert)
        return (0, int(action.insert))

    def step(self) -> None:
        super().step()
        if self.waiting_for("TARGET"):
            return

        spawn = self.target_id
        if not self.mob:
            mob = self._world.mobs.get(spawn)
            if not mob:
                log.error("attack target=%s missing", spawn)
                self.complete = True
                return

            self.mob = mob

        if self._become_corpse():
            return

        # tick_recasts(self)
        self._bars()
        self._cure_flag()
        self._string_251()
        # if not self.waiting_for("CAST") and fill_bar(loop, world):
        #     return

        self._request_heal()
        self._request_cure()

        if self.waiting_for("CAST") or self.casting:
            if not self.messages:
                return
            self.unwait("CAST")
            self.casting = False

        if mob and mob.is_treasure and float(mob.distance) <= 25:
            self._loop.send("OP_LDoNOpen", OP_LDoNOpen().serialize())
            return

        if not mob or mob.dead:
            # if mob and mob.dead:
            #     loop.append(Reconstitute(241))
            self.complete = True
            return

        if int(mob.hp or 0) == 0 and not mob.is_treasure:
            self.zero_hp += 1
            if self.zero_hp >= 10:
                if not self.target_id:
                    log.info("attack dead spawn=%s", self.target_id)
                    # self._world.skip_spawn(target)  # skip things that are already dead
                self.complete = True
                return
        else:
            self.zero_hp = 0
        sees = self._world.line_of_sight(mob)
        if self.closed and not sees:
            self.closed = False

        if not self.closed and (float(mob.distance) > MELEE or not sees):
            if self._stuck():
                if float(mob.distance) <= 25 and sees:
                    self.closed = True
                elif float(mob.distance) <= 25:
                    self.attacking = False
                    self.active_path = None
                    self.planned = None
                    self.move_closer(mob.position, "los")
                    return
                else:
                    if self.target_id:
                        log.info("attack unstick spawn=%s d=%.0f", self.target_id, mob.distance)
                        # self._world.skip_spawn(target)  # skip things that are already dead
                    self.complete = True
                    return
            else:
                self.attacking = False
                point = mob.position
                planned = self.planned
                if not planned or _apart(planned, point) > 15:
                    self.active_path = None
                    self.planned = point

                if sees and float(mob.distance) <= 35:
                    length = STRIDE["los"][0]
                    path = straight(
                        self._world.position,
                        point,
                        length,
                    )
                    self.active_path = path
                    self.active_path_dest = point
                    self._world.movement.advance(self._loop, path)
                    return

                mode = "walk" if self.cautious else "los"
                self.move_closer(point, mode)
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

                if not self.target_id:
                    log.info("attack no damage spawn=%s d=%.0f", self.target_id, mob.distance)
                    # self._world.skip_spawn(target)  # skip things that are already dead
                # loop.append(Reconstitute(241))
                self.complete = True
                return
            self.move_closer(mob, "los")
            return

        self.face(mob.position)

        # Class 62 is an LDoN object. Melee never puts the player on its hate list,
        # so the kill does not credit a task. Opening it does.
        if mob.is_treasure:
            self._loop.send("OP_LDoNOpen", OP_LDoNOpen().serialize())
            return

        if not self.opened:
            # send_command(loop, "^attack")
            self.opened = True

        self.suspended = False
        if self._combat_spell():
            self.attacking = False
            return

        # Each OP_AutoAttack(1) restarts the swing timer. Send it once per engagement.
        if not self.attacking:
            self._loop.send("OP_AutoAttack", OP_AutoAttack(1).serialize())
            self.attacking = True

        self._ability()

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

    def _stuck(self) -> bool:
        """True after five seconds on the same spot, still out of melee."""
        here = (round(self._world.position[0], 1), round(self._world.position[1], 1))
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

    def _become_corpse(self) -> bool:

        def matcher(message: EQStruct) -> bool:
            match message:
                case OP_BecomeCorpse():
                    return message.spawn_id in (0, self.spawn_id)
                case _:
                    return False

        corpse = self.consume("OP_BecomeCorpse", matcher)
        if corpse is None:
            return False

        # loop.append(Reconstitute(241))
        self.complete = True
        return True

    def _bars(self) -> None:
        message = self.consume("OP_HPUpdate") or self.consume("OP_MobHealth")
        if message is None:
            return
        # fraction = bar_ratio(message)
        # if fraction is not None and fraction > 0.5:
        #     self.heal_requested = False

    def _cure_flag(self) -> None:
        message = self.consume("OP_Buff")
        if message is None:
            return
        # if buff_faded(message) or not afflictions(world):
        #     self.cure_requested = False

    def reclaim_if_ours(self, *targets: int) -> bool:
        """Consume string 251 for one of targets and queue Reclaim. True when a match was handled."""
        matched = False
        wanted = {int(target) for target in targets if target}
        log.info(f"reclaim_if_ours wanted={wanted}")

        while self.consume("OP_SimpleMessage", simple_id_matcher(251)):
            # corpse = own_corpse(loop, world)
            # if not corpse or int(corpse) not in wanted:
            #     continue
            # if not queued(loop, "Reclaim", corpse_id=corpse):
            #     where = corpse_where(loop, world, corpse, (world.x, world.y, world.z))
            #     from eqclient3.actions.reclaim import Reclaim

            #     yield_to(parent, loop, world, Reclaim(corpse, where), f"reclaim:{corpse}")

            matched = True
        return matched

    def _string_251(self) -> None:
        if self.reclaim_if_ours(int(self.cast_target or 0)):
            self.heal_requested = False
            self.cure_requested = False

    def _request_heal(self) -> None:
        if self.heal_requested:
            return
        # target = lowest_hurt(world)
        # if target is None:
        #     return
        # gem = next((row for row in memorized(world, self) if row.heal), None)
        # if gem is None or not ready_gem(world, gem):
        #     return
        # cast_spell(loop, gem, target)
        # self.cast_target = int(target)
        # self.heal_requested = True
        # arm_recast(self, gem)

    def _request_cure(self) -> None:
        if self.cure_requested:
            return
        # rows = afflictions(world)
        # if not rows:
        #     return
        # effect = rows[0][1] if isinstance(rows[0], tuple) else rows[0].effect
        # entity = rows[0][0] if isinstance(rows[0], tuple) else rows[0].entity
        # gem = next((row for row in memorized(world, self) if cures(row, effect)), None)
        # if gem is None or not ready_gem(world, gem):
        #     return
        # cast_spell(loop, gem, int(entity or 0))
        # self.cast_target = int(entity or 0)
        # self.cure_requested = True
        # arm_recast(self, gem)

    def _combat_spell(self) -> bool:
        # if sit_for_mana(loop, world):
        #     self.resting = True
        #     return True
        # if self.resting:
        #     stand(loop, world)
        #     self.resting = False
        # choice = next_offense(world, self, self.landed)
        # if choice is None:
        #     return False
        # cast_spell(loop, choice.gem, choice.target)
        # self.cast_target = choice.target
        # self.casting = True
        # self.wait("CAST")
        # arm_recast(self, choice.gem)
        # if choice.role in ONCE:
        #     self.landed.add(choice.role)
        return True

    def _ability(self) -> None:
        # reclaiming = queued(loop, "Reclaim")
        should_taunt = False  # check reclaiming a corpse (naked)
        now = time.time()

        for skill, duration in REUSE_TIMES.items():
            has_skill = self._world.character.abilities.combat_skill_known(skill)
            if not has_skill:
                continue

            if skill in self.ability_ready:
                if self.ability_ready[skill] > now:
                    continue

            self.ability_ready[skill] = now + float(duration)

            if skill == CombatSkill.TAUNT:
                if not should_taunt:
                    continue
                self._loop.send("OP_Taunt", OP_Taunt(self.target_id).serialize())
            else:
                self._loop.send(
                    "OP_CombatAbility",
                    OP_CombatAbility(self.target_id, skill=skill).serialize(),
                )

    def report(self) -> str:
        if self.mob:
            return f"{super().report()} target={self.mob.spoken_name()} d={self.mob.distance:.0f} hp={self.mob.hp}"
        return f"{super().report()} targeting={self.target_id}"
