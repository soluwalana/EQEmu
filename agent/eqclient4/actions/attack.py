"""Band 300. One spawn. Heal and cure once, then engaged spells, then melee.

A meditating class sits when mana is below the floor. The gem bar keeps the
strongest scribed spell of each build role, and a gem waits out its recast.
"""

import time
from functools import partial
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient4.loop import Loop
    from eqclient4.world import Mob, World

from eqclient4.action import Action, Command, SEND_COMMANDS, TARGET
from eqclient4.actions.form import FormParty
from eqclient4.actions.constants import MELEE_RANGE, SPELL_RANGE, HOSTILE_CLOSE_RANGE
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
from eqclient4.structs.constants import CASTER_CLASSES



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
from eqclient4.structs.constants import MELEE, CombatSkill


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
        cautious: bool = False,
    ) -> None:
        super().__init__(world, loop)
        self.priority = 300
        self.target_id = target_id

        self.ability_ready: dict[CombatSkill, float] = {}
        self.cautious = bool(cautious)

        self.mob: Mob | None = None
        self.bots_sent = False
        self.attacking = False

    def opcodes(self) -> tuple[str, ...]:
        return super().opcodes() + (
            "OP_BecomeCorpse",
            "OP_HPUpdate",
            "OP_Buff",
            "OP_SimpleMessage",
        )

    def suspend(self) -> None:
        self.active_path = None
        self.loop.send("OP_AutoAttack", OP_AutoAttack(0).serialize())
        self.attacking = False
        self.suspended = True
        self.bots_sent = False

    @staticmethod
    def key(action: Action) -> tuple[int, int]:
        if isinstance(action, Attack):
            mob = action.mob
            if not mob:
                return (0, int(action.insert))
            return ((-mob.level or 0), action.insert)
        return (0, int(action.insert))

    def command_sent(self, text: str) -> bool:
        for command in self.commands:
            if command.text == text and command.sent_at is not None:
                return True
        return False

    def completed_command(self, text: str, remove: bool = True) -> Command | None:
        """Pop and return the first command that was sent and completed."""
        pop_idx = None
        ret_command = None
        for idx, command in enumerate(self.commands):
            if command.text != text:
                continue
            if command.sent_at and command.recv_response or command.failure_msg:
                pop_idx = idx
                ret_command = command
                break

        if pop_idx is not None and remove:
            command = self.commands.pop(pop_idx)
            return command

        return ret_command

    def step(self) -> None:
        super().step()
        if self.waiting_for(TARGET, SEND_COMMANDS):
            return

        if not self.mob:
            self.mob = self.world.mobs.get(self.target_id)
            if not self.mob:
                log.error(f"attack target={self.target_id} missing")
                self.complete = True
                return

        self.face(self.mob.position)

        if not self.world.line_of_sight(self.mob):
            self.move_closer(self.mob.position)
            return

        if self.mob and self.mob.is_treasure:
            if float(self.mob.distance) <= 25:
                self.loop.send("OP_LDoNOpen", OP_LDoNOpen().serialize())
                return
            self.move_closer(self.mob.position)
            return

        if not self.mob or self.mob.dead:
            # if mob and mob.dead:
            #     loop.append(Reconstitute(241))
            self.complete = True
            return

        if self.mob.hp == 0 and not self.mob.is_treasure:
            self.zero_hp += 1
            if self.zero_hp >= 10:
                log.info(f"attack zero hp spawn={self.target_id}")
                self.complete = True
                return

        if self.mob.distance > HOSTILE_CLOSE_RANGE:
            self.move_closer(self.mob.position)
            return

        if not self.bots_sent:
            # "usage: <enemy_target> %s [actionable: byname | ownergroup | ownerraid | namesgroup | healrotation | mmr | byclass | byrace | default: spawned] ([actionable_name])"
            cmd = Command(
                text="^attack",
                response_pattern=r"(?:Attacking (.*?)\.|\d+ of your bots are attacking (.*?)\.)",
                failure_patterns=[
                    r"You must <target> an enemy to use this command",
                    r"You must have Line of Sight to use this command",
                    r"None of your bots are capable of attacking",
                    r"You have no spawned bots meeting this criteria - type: 'spawned'",
                ],
            )
            cmd.success_callback=partial(self.handle_bots_attacking, cmd)
            cmd.failure_callback=partial(self.handle_bots_failure, cmd)
            self.commands.append(cmd)
            self.wait(SEND_COMMANDS)
            return

        command_response = self.completed_command("^attack", remove=False)
        if not command_response:
            log.error(f"attack failure=no command send had no failure or success")
            log.error("Critical failure")
            self.complete = True
            return

        if command_response.failure_msg:
            log.error(f"attack failure={command_response.failure_msg}")
            return

        if self.world.character.class_id in CASTER_CLASSES:
            if self.mob.distance > SPELL_RANGE:
                self.move_closer(self.mob.position)
                return
        else:
            if self.mob.distance > MELEE_RANGE:
                self.move_closer(self.mob.position)
                return
        
        if not self.attacking:
            log.info("attack autoattack")
            self.loop.send("OP_AutoAttack", OP_AutoAttack(1).serialize())
            self.attacking = True
            return

        if self.attacking:
            log.info("in combat")
            return
        
        log.error("Should not be here yet")
        # if self._become_corpse():
        #     return

        # tick_recasts(self)
        self._bars()
        self._cure_flag()
        # self._string_251()
        # if not self.waiting_for("CAST") and fill_bar(loop, world):
        #     return

        # self._request_heal()
        # self._request_cure()

        if self.waiting_for("CAST") or self.casting:
            if not self.messages:
                return
            self.unwait("CAST")
            self.casting = False

        sees = self.world.line_of_sight(self.mob)
        if self.closed and not sees:
            self.closed = False

        if not self.closed and (float(self.mob.distance) > MELEE or not sees):
            if self._stuck():
                if float(self.mob.distance) <= 25 and sees:
                    self.closed = True
                elif float(self.mob.distance) <= 25:
                    self.attacking = False
                    self.active_path = None
                    self.planned = None
                    self.move_closer(self.mob.position, "los")
                    return
                else:
                    if self.target_id:
                        log.info(
                            "attack unstick spawn=%s d=%.0f", self.target_id, self.mob.distance
                        )
                        # self.world.skip_spawn(target)  # skip things that are already dead
                    self.complete = True
                    return
            else:
                self.attacking = False
                point = self.mob.position
                planned = self.planned
                if not planned or _apart(planned, point) > 15:
                    self.active_path = None
                    self.planned = point

                if sees and float(self.mob.distance) <= 35:
                    length = STRIDE["los"][0]
                    path = straight(
                        self.world.position,
                        point,
                        length,
                    )
                    self.active_path = path
                    self.active_path_dest = point
                    self.world.movement.advance(self.loop, path)
                    return

                mode = "walk" if self.cautious else "los"
                self.move_closer(point, mode)
                return

        self.still = 0
        self.anchor = None
        if self._hp_stuck(self.mob):
            self.misses += 1
            self.attacking = False
            self.closed = False
            self.active_path = None
            self.planned = None
            if self.misses >= 3:

                if not self.target_id:
                    log.info(
                        f"attack no damage spawn={self.target_id} d={self.mob.distance:.0f}",
                    )
                    # self.world.skip_spawn(target)  # skip things that are already dead
                # loop.append(Reconstitute(241))
                self.complete = True
                return
            self.move_closer(self.mob, "los")
            return


        # if self._combat_spell():
        #     self.attacking = False
        #     return

        self._ability()

    def handle_bots_attacking(self, cmd: Command) -> None:
        self.bots_sent = True
        assert cmd.recv_response
        log.info(f"bots attacking {cmd.recv_response.group(1)}")
        return

    def handle_bots_failure(self, cmd: Command) -> None:
        self.bots_sent = False
        assert cmd.failure_msg
        log.error(f"bots failure={cmd.failure_msg}")
        # no bots are capable or timeout because there are no bots
        positioning_failures = (
            "You must <target> an enemy to use this command",
            "You must have Line of Sight to use this command",
        )
        if not any((f in cmd.failure_msg for f in positioning_failures)):
            self.yield_to(FormParty(self.world, self.loop, self.world.party_mode ==  "raid",))
            return
        self.complete = True
        return

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
        here = (round(self.world.position[0], 1), round(self.world.position[1], 1))
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
                    return message.spawn_id in (0, self.world.self_id)
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

    # def _string_251(self) -> None:
    #     if self.reclaim_if_ours(int(self.cast_target or 0)):
    #         self.heal_requested = False
    #         self.cure_requested = False

    # def _request_heal(self) -> None:
    #     if self.heal_requested:
    #         return
    #     # target = lowest_hurt(world)
    #     # if target is None:
    #     #     return
    #     # gem = next((row for row in memorized(world, self) if row.heal), None)
    #     # if gem is None or not ready_gem(world, gem):
    #     #     return
    #     # cast_spell(loop, gem, target)
    #     # self.cast_target = int(target)
    #     # self.heal_requested = True
    #     # arm_recast(self, gem)

    # def _request_cure(self) -> None:
    #     if self.cure_requested:
    #         return
    #     # rows = afflictions(world)
    #     # if not rows:
    #     #     return
    #     # effect = rows[0][1] if isinstance(rows[0], tuple) else rows[0].effect
    #     # entity = rows[0][0] if isinstance(rows[0], tuple) else rows[0].entity
    #     # gem = next((row for row in memorized(world, self) if cures(row, effect)), None)
    #     # if gem is None or not ready_gem(world, gem):
    #     #     return
    #     # cast_spell(loop, gem, int(entity or 0))
    #     # self.cast_target = int(entity or 0)
    #     # self.cure_requested = True
    #     # arm_recast(self, gem)

    # def _combat_spell(self) -> bool:
    #     # if sit_for_mana(loop, world):
    #     #     self.resting = True
    #     #     return True
    #     # if self.resting:
    #     #     stand(loop, world)
    #     #     self.resting = False
    #     # choice = next_offense(world, self, self.landed)
    #     # if choice is None:
    #     #     return False
    #     # cast_spell(loop, choice.gem, choice.target)
    #     # self.cast_target = choice.target
    #     # self.casting = True
    #     # self.wait("CAST")
    #     # arm_recast(self, choice.gem)
    #     # if choice.role in ONCE:
    #     #     self.landed.add(choice.role)
    #     return True

    def _ability(self) -> None:
        # reclaiming = queued(loop, "Reclaim")
        should_taunt = False  # check reclaiming a corpse (naked)
        now = time.time()

        for skill, duration in REUSE_TIMES.items():
            has_skill = self.world.character.abilities.combat_skill_known(skill)
            if not has_skill:
                continue

            if skill in self.ability_ready:
                if self.ability_ready[skill] > now:
                    continue

            self.ability_ready[skill] = now + float(duration)

            if skill == CombatSkill.TAUNT:
                if not should_taunt:
                    continue
                self.loop.send("OP_Taunt", OP_Taunt(self.target_id).serialize())
            else:
                self.loop.send(
                    "OP_CombatAbility",
                    OP_CombatAbility(self.target_id, skill=skill).serialize(),
                )

    def report(self) -> str:
        if self.mob:
            return f"{super().report()} target={self.mob.spoken_name} d={self.mob.distance:.0f} hp={self.mob.hp}"
        return f"{super().report()} targeting={self.target_id}"
