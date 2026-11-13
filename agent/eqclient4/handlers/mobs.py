from eqclient4.handler import Handler
from eqclient4.log import log
from eqclient4.structs import (
    EQStruct,
    OP_ClientUpdate,
    OP_Consider,
    OP_Death,
    OP_DeleteSpawn,
    OP_MobHealth,
    OP_NewSpawn,
    OP_ZoneEntry,
    OP_MobRename,
)
from eqclient4.world import Mob
from eqclient4.utils import FactionStanding

class MobsHandler(Handler):
    opcodes = (
        "OP_NewSpawn",
        "OP_ZoneEntry",
        "OP_DeleteSpawn",
        "OP_MobHealth",
        "OP_Death",
        "OP_ClientUpdate",
        "OP_Consider",
        "OP_MobRename",
    )

    def on(self, opcode: str, payload: EQStruct) -> None:
        match payload:
            case OP_NewSpawn():
                if payload.spawn.name == self.world.character.name:
                    return

                spawn = payload.spawn
                if spawn.spawn_id in self.world.mobs:
                    mob = self.world.mobs[spawn.spawn_id]
                else:
                    mob = Mob(id=spawn.spawn_id)
                
                faction_id : int | None = None
                if self.world.zone:
                    faction_id = self.world.faction_hits.primary(self.world.zone, mob.name)
                
                # Do not normalize the name here, factions normalizes differently than
                # Hailing does.
                mob.name = spawn.name
                mob.position = (spawn.x, spawn.y, spawn.z)
                mob.class_id = spawn.class_id
                mob.race = spawn.race
                mob.level = spawn.level
                mob.last_name = spawn.last_name
                mob.npc = spawn.npc
                mob.faction_id = faction_id
                mob.npc = spawn.npc
                self.world.mobs[spawn.spawn_id] = mob
                return

            case OP_ZoneEntry():
                pass

            case OP_DeleteSpawn():
                if payload.spawn_id not in self.world.mobs:
                    return
                mob = self.world.mobs.pop(payload.spawn_id)
                mob.deleted = True
                return

            case OP_MobHealth():
                pass

            case OP_Death():
                if payload.spawn_id not in self.world.mobs:
                    return
                mob = self.world.mobs[payload.spawn_id]
                mob.dead = True
                return

            case OP_ClientUpdate():
                if payload.spawn_id == self.world.self_id:
                    # Handled by Movement Listener
                    return

                if payload.spawn_id not in self.world.mobs:
                    log.error(f"Client update for unknown spawn: {payload.spawn_id}")
                    return

                mob = self.world.mobs[payload.spawn_id]
                mob.position = (payload.x, payload.y, payload.z)
                mob.heading = payload.heading
                mob.animation = payload.animation
                log.debug(
                    f"Client update for {mob.name} at {mob.position} heading {mob.heading} animation {mob.animation}"
                )
                return

            case OP_Consider():
                if payload.player_id != self.world.self_id:
                    log.error(f"Consider from non-self player: {payload.player_id}")
                    return

                if payload.target_id not in self.world.mobs:
                    log.error(f"Consider for unknown target: {payload.target_id}")
                    return

                mob = self.world.mobs[payload.target_id]
                mob.faction_last_considered = FactionStanding(payload.faction)

                if not mob.faction_id:
                    log.error(f"No faction information for {mob.name}")
                    return

                faction = self.world.faction(mob.faction_id)

                if faction.amount is None:
                    faction.set_estimated_faction_amount(mob.faction_last_considered)

                if not faction.standing or faction.standing != mob.faction_last_considered:
                    faction.standing = FactionStanding(payload.faction)

                return

            case OP_MobHealth():
                if payload.spawn_id not in self.world.mobs:
                    log.error(f"Mob health for unknown spawn: {payload.spawn_id}")
                    return
                
                mob = self.world.mobs[payload.spawn_id]
                mob.hp = payload.percent
                mob.max_hp = 100
                return

            case OP_MobRename():
                for mob in self.world.mobs.values():
                    if mob.name == payload.old_name:
                        mob.name = payload.new_name
                        return
                return

            case _:
                log.error(f"Unknown spawn opcode: {opcode}")
