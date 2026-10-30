"""Spawns, position for other ids, bars, damage, corpses, find, and track.

Our OP_ClientUpdate is movement's packet. This handler does not write it.
"""
from __future__ import annotations

from eqclient3.actions.attack import Attack
from eqclient3.actions.support import ratio
from eqclient3.actions.follow import Follow
from eqclient3.actions.heal import Heal
from eqclient3.actions.hold import Hold
from eqclient3.actions.rest import Rest
from eqclient3.handlers.common import FOLLOW_YARDS, HEAL_LINE, MANA_SIT, SIT_LINE, SPELL_DAMAGE, attack_for, bot_names, character_name, deliver, find_mob, has_cleric, has_open, is_ours, mark_fight, mobs_map, our_side, place, primary_faction, enqueue_once, source_open
from eqclient3.handlers.death import claim_pending
from eqclient3.structs import EQStruct, OP_Assist, OP_BecomeCorpse, OP_ClientUpdate, OP_Damage, OP_DeleteSpawn, OP_HPUpdate, OP_MobHealth, OP_MobUpdate, OP_NewSpawn, OP_Track, OP_ZoneSpawns
from eqclient3.world import Mob
from eqclient3.handler import Handler

class MobsHandler(Handler):
    opcodes = ('OP_NewSpawn', 'OP_ZoneSpawns', 'OP_DeleteSpawn', 'OP_ClientUpdate', 'OP_MobUpdate', 'OP_HPUpdate', 'OP_MobHealth', 'OP_Damage', 'OP_BecomeCorpse', 'OP_FindPersonReply', 'OP_Track', 'OP_Assist')

    def on(self, opcode: str, payload: EQStruct) -> None:
        if isinstance(payload, (OP_NewSpawn, OP_ZoneSpawns)):
            self.spawns(payload)
        elif isinstance(payload, OP_DeleteSpawn):
            self.delete(payload)
        elif isinstance(payload, (OP_ClientUpdate, OP_MobUpdate)):
            self.position(payload)
        elif isinstance(payload, OP_HPUpdate):
            self.hp(payload)
        elif isinstance(payload, OP_MobHealth):
            self.mob_health(payload)
        elif isinstance(payload, OP_Damage):
            self.damage(opcode, payload)
        elif isinstance(payload, OP_BecomeCorpse):
            self.corpse(payload)
        elif isinstance(payload, OP_Track):
            self.track(payload)
        elif isinstance(payload, OP_Assist):
            self.assist(payload)

    def spawns(self, row: OP_NewSpawn | OP_ZoneSpawns) -> None:
        found = [row.spawn] if isinstance(row, OP_NewSpawn) else row.spawns
        if not found:
            return
        world = self.world
        mobs = mobs_map(world)
        me = character_name(self.loop, world).lower()
        for spawn in found:
            spawn_id, name, npc, level, body_type, x, y, z, class_id, race = (
                spawn.spawn_id, spawn.name, spawn.npc, spawn.level, spawn.body, spawn.x, spawn.y, spawn.z, spawn.class_id, spawn.race,
            )
            mob = Mob(spawn_id, name, npc=npc, level=level, position=(x, y, z))
            mob.body = body_type
            mob.class_id = class_id
            mob.race = race
            mob.faction_id = primary_faction(world.zone or '', name)
            previous = mobs.get(spawn_id)
            if previous:
                mob.consider = previous.consider
                mob.faction_last_considered = previous.faction_last_considered
                mob.targeted = previous.targeted
                mob.hp = previous.hp
                mob.max_hp = previous.max_hp
                mob.dead = previous.dead
            mobs[spawn_id] = mob
            place(mob, x, y, z, world)
            if me and name.lower() == me and npc not in (2, 3):
                world.self_id = spawn_id
                self.claim_death()

    def delete(self, row: OP_DeleteSpawn) -> None:
        mobs_map(self.world).pop(row.spawn_id, None)

    def position(self, row: OP_ClientUpdate | OP_MobUpdate) -> None:
        spawn_id, x, y, z = row.spawn_id, row.x, row.y, row.z
        world = self.world
        if spawn_id == 0 or spawn_id == world.self_id:
            return
        mob = find_mob(world, spawn_id)
        if not mob:
            return
        place(mob, x, y, z, world)
        self.follow(mob)

    def follow(self, mob: Mob) -> None:
        world = self.world
        group = world.group
        leader = str(group.leader or '')
        if not leader or (mob.name or '').lower() != leader.lower():
            return
        if mob.distance <= FOLLOW_YARDS:
            return
        loop = self.loop
        if source_open(loop, f'follow:{leader}'):
            return
        action = Follow(leader)
        action.point = mob.position
        enqueue_once(loop, world, action, f'follow:{leader}')

    def hp(self, row: OP_HPUpdate) -> None:
        spawn_id, cur, max_hp = row.spawn_id, row.cur_hp, row.max_hp
        world = self.world
        if spawn_id == 0:
            return
        mob = find_mob(world, spawn_id)
        if mob:
            mob.hp = cur
            if max_hp:
                mob.max_hp = max_hp
        if world.self_id == 0 and self.hp_names_us(spawn_id, mob):
            world.self_id = spawn_id
            self.claim_death()
        if spawn_id == world.self_id:
            world.hp = cur
            if max_hp:
                world.max_hp = max_hp
            self.claim_death()
            self.our_bars()
            return
        self.other_bars(mob)

    def hp_names_us(self, spawn_id: int, mob: Mob | None) -> bool:
        del spawn_id
        if not mob:
            return True
        me = character_name(self.loop, self.world).lower()
        return bool(me) and (mob.name or '').lower() == me

    def claim_death(self) -> None:
        claim_pending(self.loop, self.world)

    def mob_health(self, row: OP_MobHealth) -> None:
        spawn_id, percent = row.spawn_id, row.percent
        world = self.world
        spawn_id = spawn_id & 65535
        self_id = world.self_id & 65535
        if not spawn_id or spawn_id == self_id:
            if spawn_id and spawn_id == self_id:
                if not world.max_hp:
                    world.max_hp = 100
                    world.hp = percent
                self.our_bars()
            return
        mob = find_mob(world, spawn_id)
        if not mob:
            return
        percent = max(0, min(100, percent))
        if mob.max_hp <= 0 or mob.max_hp == 100:
            mob.max_hp = 100
            mob.hp = percent
        else:
            mob.hp = percent * mob.max_hp // 100
        self.other_bars(mob)

    def our_bars(self) -> None:
        world = self.world
        current = ratio(world.hp, world.max_hp)
        if not current:
            return
        loop = self.loop
        fighting = has_open(loop, Attack, 'Attack')
        if current < HEAL_LINE and (not fighting):
            enqueue_once(loop, world, Heal('self'), 'heal:self')
        if current < SIT_LINE and (not fighting) and (not source_open(loop, 'heal:self')):
            enqueue_once(loop, world, Rest('self'), 'rest:self')

    def other_bars(self, mob: Mob | None) -> None:
        if not mob:
            return
        world = self.world
        name = mob.name or ''
        if name.lower() not in bot_names(world):
            return
        loop = self.loop
        fighting = has_open(loop, Attack, 'Attack')
        current = ratio(mob.hp, mob.max_hp)
        if current and current < HEAL_LINE and has_cleric(world) and (not fighting):
            enqueue_once(loop, world, Heal(name), f'heal:{name}')
        mana = ratio(mob.mana, mob.max_mana)
        if mana and mana < MANA_SIT:
            enqueue_once(loop, world, Rest(name), f'rest:{name}')

    def damage(self, opcode: str, row: OP_Damage) -> None:
        target, source, dmg_type, spell_id, amount = row.target, row.source, row.type, row.spell_id, row.amount
        world = self.world
        loop = self.loop
        if amount <= 0 or our_side(world, source):
            return
        if not is_ours(world, target, loop=loop) and (not self.is_bot(target)):
            return
        mob = find_mob(world, source)
        spell_tick = dmg_type == SPELL_DAMAGE and spell_id not in (0, 65535)
        corpse = not mob or mob.dead or mob.npc in (2, 3)
        if corpse:
            return
        if mob.npc != 1:
            return
        mark_fight(world, mob.id)
        existing = attack_for(loop, Attack, mob.id)
        if spell_tick:
            if not existing:
                enqueue_once(loop, world, Hold(mob.id), f'hold:{mob.id}')
            return
        if not existing:
            existing = enqueue_once(loop, world, Attack(mob.id), f'aggro:{mob.id}')
        if existing:
            deliver(existing, row)

    def is_bot(self, spawn_id: int) -> bool:
        mob = find_mob(self.world, spawn_id)
        if not mob:
            return False
        return (mob.name or '').lower() in bot_names(self.world)

    def corpse(self, row: OP_BecomeCorpse) -> None:
        world = self.world
        spawn_id, x, y, z = row.spawn_id, row.x, row.y, row.z
        mob = find_mob(world, spawn_id)
        if mob:
            mob.dead = True
            if not is_ours(world, spawn_id, mob, self.loop):
                mob.npc = 3
            place(mob, x, y, z, world)
        attack = attack_for(self.loop, Attack, spawn_id)
        if attack:
            attack.complete = True

    def track(self, row: OP_Track) -> None:
        for entity, distance in row.entries:
            mob = find_mob(self.world, entity)
            if not mob:
                continue
            mob.distance = distance

    def assist(self, row: OP_Assist) -> None:
        target = row.entity_id
        for mob in mobs_map(self.world).values():
            mob.targeted = mob.id == target
