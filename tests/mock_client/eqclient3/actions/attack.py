"""Band 300. One spawn. Heal and cure once, then melee inside 15 yards."""
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient3.loop import Loop
    from eqclient3.world import World

from eqclient3.action import Action
from eqclient3.structs import OP_AutoAttack, OP_CombatAbility, OP_Taunt
from eqclient3.actions.bots.reconstitute import Reconstitute
from eqclient3.actions.support import BASH, KICK, MELEE, TAUNT, afflictions, arm_recast, bar_ratio, buff_faded, cast_spell, cures, known, lowest_hurt, memorized, queued, ready_gem, reclaim_if_ours, send_command, spawn_of, walk, yield_to

class Attack(Action):

    def __init__(self, spawn_id: int, *, cautious: bool=False) -> None:
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
        self.ability_ready = {}
        self.cautious = bool(cautious)
        self.level = 0
        self.cast_target = 0
        self._gem_recast = {}

    def opcodes(self) -> tuple[object, ...]:
        return ('OP_Consider', 'OP_BecomeCorpse', 'OP_HPUpdate', 'OP_MobHealth', 'OP_Buff', 'OP_SimpleMessage')

    def suspend(self) -> None:
        self.active_path = None
        self.opened = False
        self.suspended = True

    @staticmethod
    def key(action: Action) -> tuple:
        return (-int(action.level or 0), int(action.insert))

    def step(self, loop: Loop, world: World) -> None:
        super().step(loop, world)
        mob = world.mobs.get(self.spawn_id)
        if mob is not None:
            self.level = int(mob.level or 0)
        if self._become_corpse(loop, world):
            return
        self._bars(world)
        self._cure_flag(world)
        self._string_251(loop, world)
        self._request_heal(loop, world)
        self._request_cure(loop, world)
        if self.waiting_for('CAST') or self.casting:
            if not self.messages:
                return
            self.unwait('CAST')
            self.casting = False
        if self.waiting_for('TARGET'):
            return
        if mob is None:
            return
        if float(mob.distance) > MELEE:
            mode = 'walk' if self.cautious else 'los'
            walk(self, loop, world, mob.position, mode)
            return
        if not self.opened:
            send_command(loop, '^attack')
            send_command(loop, '^pet_attack')
            self.opened = True
        self.suspended = False
        if self._combat_spell(loop, world):
            return
        loop.send('OP_AutoAttack', OP_AutoAttack(1).serialize())
        self._ability(loop, world)

    def _become_corpse(self, loop: Loop, world: World) -> bool:
        corpse = self.consume('OP_BecomeCorpse', lambda message: spawn_of(message) in (0, self.spawn_id))
        if corpse is None:
            return False
        yield_to(self, loop, world, Reconstitute(241), f'reconstitute:{self.spawn_id}')
        self.complete = True
        return True

    def _bars(self, world: World) -> None:
        message = self.consume('OP_HPUpdate') or self.consume('OP_MobHealth')
        if message is None:
            return
        fraction = bar_ratio(message)
        if fraction is not None and fraction > 0.5:
            self.heal_requested = False

    def _cure_flag(self, world: World) -> None:
        message = self.consume('OP_Buff')
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
        gem = next((row for row in memorized(world, self) if row.combat), None)
        if gem is None or not ready_gem(world, gem):
            return False
        cast_spell(loop, gem, self.spawn_id)
        self.cast_target = self.spawn_id
        self.casting = True
        self.wait('CAST')
        arm_recast(self, gem)
        return True

    def _ability(self, loop: Loop, world: World) -> None:
        tick = int(loop.tick or 0)
        reclaiming = queued(loop, 'Reclaim')
        if not reclaiming and self.ability_ready.get('taunt', 0) <= tick and known(world, TAUNT):
            loop.send('OP_Taunt', OP_Taunt(self.spawn_id).serialize())
            self.ability_ready['taunt'] = tick + 60
            return
        if self.ability_ready.get('kick', 0) <= tick and known(world, KICK):
            loop.send('OP_CombatAbility', OP_CombatAbility(self.spawn_id, skill=KICK).serialize())
            self.ability_ready['kick'] = tick + 60
            return
        abilities = world.character.abilities
        if self.ability_ready.get('bash', 0) <= tick and known(world, BASH) and (abilities.can_bash or abilities.shield or abilities.two_hand):
            loop.send('OP_CombatAbility', OP_CombatAbility(self.spawn_id, skill=BASH).serialize())
            self.ability_ready['bash'] = tick + 60
