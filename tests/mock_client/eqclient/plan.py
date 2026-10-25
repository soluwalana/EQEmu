"""Pick one next action from the world, the task list, and this zone's scripts.

Nothing here is specific to a zone. Task packets and the quest files decide the
targets. A new zone is a new script set and the same rules.
"""

from __future__ import annotations

import math
import re
from dataclasses import dataclass

from eqclient.items import Inventory, can_receive
from eqclient.quests import Need, ZoneQuests
from eqclient.tasks import DELIVER, KILL, LOOT, SPEAK, Activity, TaskBook
from eqclient.world import ZoneModel

_IDS = re.compile(r"\d+")
ATTACK_RANGE = 25.0
LEAVE_LEVEL = 5
_TRAINER_OFFSET = 19


@dataclass
class Intention:
    kind: str
    target: int = 0
    name: str = ""
    item_id: int = 0
    where: tuple[float, float, float] | None = None
    distance: float = 0.0
    text: str = ""


def choose(
    world: ZoneModel,
    tasks: TaskBook,
    quests: ZoneQuests,
    inventory: Inventory,
    party_ready: bool,
    skipped_ground: set[int] | None = None,
    skipped_corpses: set[int] | None = None,
    said: set[tuple[str, str]] | None = None,
    handed: set[tuple[str, str]] | None = None,
) -> Intention | None:
    skipped_ground = skipped_ground or set()
    skipped_corpses = skipped_corpses or set()
    said = said or set()
    handed = handed or set()
    if not party_ready:
        return Intention("form_party")

    corpse = _own_corpse(world)
    if corpse is not None and can_receive(inventory):
        return corpse

    threat = _nearest(
        world,
        [
            spawn
            for spawn in world.spawns.values()
            if spawn.npc == 1 and world.faction.get(spawn.spawn_id) in (8, 9)
        ],
    )
    if threat is not None and _dist(world, threat.x, threat.y) <= ATTACK_RANGE:
        return _at(world, "fight", threat.spawn_id, threat.name, threat.x, threat.y, threat.z)

    trainer = _trainer(world)
    if world.points > 0 and trainer is not None:
        return _at(world, "train", trainer.spawn_id, trainer.name, trainer.x, trainer.y, trainer.z)

    step = _task_step(world, tasks, quests, inventory, skipped_corpses, skipped_ground)
    if step is not None:
        return step

    giver = _next_giver(world, tasks)
    if giver is not None:
        return giver

    task_needs = _task_needs(tasks, quests, inventory)
    known = _known_ground(world, inventory, task_needs, skipped_ground)
    if known is not None:
        return known
    # A script item sitting on the ground is worth picking up. One we cannot see is not a hunt.
    known = _known_ground(world, inventory, _script_needs(quests, inventory), skipped_ground)
    if known is not None:
        return known

    if task_needs:
        corpse = _nearest(
            world,
            [
                spawn
                for spawn in world.spawns.values()
                if _is_corpse(spawn.npc) and spawn.spawn_id not in skipped_corpses
            ],
        )
        if corpse is not None:
            return _at(world, "loot", corpse.spawn_id, corpse.name, corpse.x, corpse.y, corpse.z)
        unknown = _nearest(
            world,
            [
                obj
                for obj in world.ground.values()
                if obj.drop_id not in skipped_ground and not _ground_known(obj.name, inventory)
            ],
        )
        if unknown is not None:
            return _at(world, "search", unknown.drop_id, unknown.name, unknown.x, unknown.y, unknown.z)

    turn_in = _turn_in(world, tasks, quests, inventory, handed)
    if turn_in is not None:
        return turn_in

    talk = _quest_talk(world, tasks, quests, said)
    if talk is not None:
        return talk

    if not tasks.local_work_left() and quests.exits and _ready_to_leave(world):
        door = _exit_door(world, quests.exits)
        if door is not None:
            return _at(world, "leave", door.door_id, door.name, door.x, door.y, door.z)
        return Intention("leave", target=quests.exits[0])
    if world.level and world.level < LEAVE_LEVEL and not tasks.local_work_left():
        enemy = _nearest(
            world,
            [spawn for spawn in world.spawns.values() if spawn.npc == 1 and world.faction.get(spawn.spawn_id) in (8, 9)],
        )
        if enemy is not None:
            return _at(world, "fight", enemy.spawn_id, enemy.name, enemy.x, enemy.y, enemy.z)
    return Intention("explore")


def _ready_to_leave(world: ZoneModel) -> bool:
    """The mines are about level 5 by the time the exit is the right next step."""
    return not world.needs_corpse and (world.level == 0 or world.level >= LEAVE_LEVEL)


def _own_corpse(world: ZoneModel) -> Intention | None:
    if not world.needs_corpse:
        return None
    if world.own_corpse_zone and world.zone and world.own_corpse_zone != world.zone:
        return None
    spawn = world.spawns.get(world.own_corpse_id)
    if spawn is not None:
        return _at(world, "reclaim", spawn.spawn_id, spawn.name, spawn.x, spawn.y, spawn.z)
    if world.own_corpse_at is not None:
        x, y, z = world.own_corpse_at
        return Intention("reclaim", name=world.character, where=(x, y, z), distance=_dist(world, x, y))
    return None


def _trainer(world: ZoneModel):
    if not world.class_id:
        return None
    want = world.class_id + _TRAINER_OFFSET
    return _nearest(
        world,
        [spawn for spawn in world.spawns.values() if spawn.npc == 1 and spawn.class_id == want],
    )


def _task_step(world, tasks, quests, inventory, skipped_corpses, skipped_ground) -> Intention | None:
    activities = tasks.current()
    if not activities:
        return None
    options = [
        _one_activity(world, tasks, quests, inventory, activity, skipped_corpses, skipped_ground)
        for activity in activities
    ]
    concrete = [item for item in options if item.kind != "explore"]
    pool = concrete or options
    return min(pool, key=lambda item: item.distance)


def _one_activity(world, tasks, quests, inventory, activity: Activity, skipped_corpses, skipped_ground) -> Intention:
    if activity.kind == SPEAK:
        spawn = _named(world, activity.target_name, corpses=False)
        if spawn is not None:
            return _at(world, "task_talk", spawn.spawn_id, spawn.name, spawn.x, spawn.y, spawn.z)
        return _explore_name(world, activity.target_name)
    if activity.kind in (KILL, LOOT):
        corpse = _named(world, activity.target_name, corpses=True, skip=skipped_corpses)
        if corpse is not None:
            return _at(world, "loot", corpse.spawn_id, corpse.name, corpse.x, corpse.y, corpse.z)
        if activity.kind == KILL:
            live = _named(world, activity.target_name, corpses=False)
            if live is not None:
                return _at(world, "task_kill", live.spawn_id, live.name, live.x, live.y, live.z)
        return _explore_name(world, activity.target_name)
    # Deliver: hold the item, then hand it to the named NPC. Otherwise loot or fetch it.
    needs = _needs_for(activity, quests)
    if needs and all(inventory.count(need.item_id) >= need.count for need in needs):
        spawn = _named(world, activity.target_name, corpses=False)
        if spawn is not None:
            return _at(
                world, "hand_in", spawn.spawn_id, spawn.name, spawn.x, spawn.y, spawn.z, item_id=needs[0].item_id
            )
        return _explore_name(world, activity.target_name)
    known = _known_ground(world, inventory, [need for need in needs if inventory.count(need.item_id) < need.count], skipped_ground)
    if known is not None:
        return known
    corpse = _nearest(
        world,
        [spawn for spawn in world.spawns.values() if _is_corpse(spawn.npc) and spawn.spawn_id not in skipped_corpses],
    )
    if corpse is not None:
        return _at(world, "loot", corpse.spawn_id, corpse.name, corpse.x, corpse.y, corpse.z)
    return _explore_name(world, activity.target_name)


def _needs_for(activity: Activity, quests: ZoneQuests) -> list[Need]:
    ids = [int(part) for part in _IDS.findall(activity.item_list or "")]
    if ids:
        return [Need(item_id, max(activity.goal, 1), activity.target_name) for item_id in ids]
    script = _script(quests, activity.target_name)
    if script is None:
        return []
    return list(script.needs)


def _task_needs(tasks: TaskBook, quests: ZoneQuests, inventory: Inventory) -> list[Need]:
    short: list[Need] = []
    for activity in tasks.activities:
        if activity.optional or activity.finished or activity.kind not in (DELIVER, LOOT):
            continue
        if not tasks.in_zone(activity.task_id):
            continue
        for need in _needs_for(activity, quests):
            if inventory.count(need.item_id) < need.count:
                short.append(need)
    return short


def _script_needs(quests: ZoneQuests, inventory: Inventory) -> list[Need]:
    short: list[Need] = []
    for script in quests.scripts.values():
        for need in script.needs:
            if inventory.count(need.item_id) < need.count:
                short.append(need)
    return short


def _turn_in(world, tasks, quests, inventory, handed: set[tuple[str, str]]) -> Intention | None:
    ready: list[tuple[Need, object]] = []
    for need in _script_needs(quests, Inventory()) :  # counts from zero, so every script need
        if (_norm(need.npc), str(need.item_id)) in handed:
            continue
        if inventory.count(need.item_id) >= need.count:
            spawn = _named(world, need.npc, corpses=False)
            if spawn is not None:
                ready.append((need, spawn))
    for need in _task_needs(tasks, quests, Inventory()):
        if inventory.count(need.item_id) >= need.count:
            spawn = _named(world, need.npc, corpses=False)
            if spawn is not None:
                ready.append((need, spawn))
    if not ready:
        return None
    need, spawn = min(ready, key=lambda pair: _dist(world, pair[1].x, pair[1].y))
    return _at(world, "hand_in", spawn.spawn_id, spawn.name, spawn.x, spawn.y, spawn.z, item_id=need.item_id)


def _next_giver(world, tasks: TaskBook) -> Intention | None:
    if tasks.local_work_left() or not tasks.pending:
        return None
    for task_id in tasks.pending:
        giver = tasks.givers.get(task_id)
        spawn = world.spawns.get(giver or 0)
        if spawn is not None and not _is_corpse(spawn.npc):
            return _at(world, "task_talk", spawn.spawn_id, spawn.name, spawn.x, spawn.y, spawn.z)
    return None


def _quest_talk(world, tasks, quests, said) -> Intention | None:
    waiting = {
        _norm(activity.target_name)
        for activity in tasks.activities
        if activity.kind == SPEAK and not activity.finished and tasks.in_zone(activity.task_id)
    }
    current_names = {_norm(activity.target_name) for activity in tasks.current() if activity.kind == SPEAK}
    choices = []
    for spawn in world.spawns.values():
        if spawn.npc != 1:
            continue
        script = _script(quests, spawn.name)
        if script is None:
            continue
        key = _norm(spawn.name)
        if key in waiting and key not in current_names:
            continue
        for keyword in script.keywords:
            if (key, keyword.lower()) in said:
                continue
            choices.append((spawn, keyword))
            break
    if not choices:
        return None
    spawn, keyword = min(choices, key=lambda pair: _dist(world, pair[0].x, pair[0].y))
    intent = _at(world, "talk", spawn.spawn_id, spawn.name, spawn.x, spawn.y, spawn.z)
    intent.text = keyword
    return intent


def _known_ground(world, inventory, needs, skipped) -> Intention | None:
    if not needs:
        return None
    choices = []
    for obj in world.ground.values():
        if obj.drop_id in skipped:
            continue
        for need in needs:
            idfile = inventory.idfile.get(need.item_id, "")
            if idfile and obj.name.startswith(idfile):
                choices.append((obj, need))
    if not choices:
        return None
    obj, need = min(choices, key=lambda pair: _dist(world, pair[0].x, pair[0].y))
    return _at(world, "fetch", obj.drop_id, obj.name, obj.x, obj.y, obj.z, item_id=need.item_id)


def _ground_known(object_name: str, inventory: Inventory) -> bool:
    return any(idfile and object_name.startswith(idfile) for idfile in inventory.idfile.values())


def _exit_door(world, exits: list[int]):
    doors = [door for door in world.doors.values() if door.door_id in exits]
    if not doors:
        return None
    return min(doors, key=lambda door: _dist(world, door.x, door.y))


def _script(quests: ZoneQuests, name: str):
    key = _norm(name)
    if key in quests.scripts:
        return quests.scripts[key]
    for script_name, script in quests.scripts.items():
        if key == script_name or key in script_name or script_name in key:
            return script
    return None


def _named(world, target: str, corpses: bool, skip: set[int] | None = None):
    skip = skip or set()
    found = []
    for spawn in world.spawns.values():
        if spawn.spawn_id in skip or not _names_match(spawn.name, target):
            continue
        if corpses and not _is_corpse(spawn.npc):
            continue
        if not corpses and _is_corpse(spawn.npc):
            continue
        if not corpses and spawn.npc == 0 and _norm(spawn.name) != _norm(world.character):
            continue
        found.append(spawn)
    return _nearest(world, found)


def _explore_name(world, name: str) -> Intention:
    seen = world.last_seen.get(name.lower()) or world.last_seen.get(_norm(name))
    if seen is None:
        for key, value in world.last_seen.items():
            if _names_match(key, name):
                seen = value
                break
    if seen is not None and seen[0] == world.zone:
        return Intention("explore", name=name, where=(seen[1], seen[2], seen[3]), distance=_dist(world, seen[1], seen[2]))
    return Intention("explore", name=name, distance=1e9)


def _names_match(spawn_name: str, target: str) -> bool:
    left = _norm(spawn_name)
    right = _norm(target)
    if not left or not right:
        return False
    return left == right or right in left or left in right


def _norm(name: str) -> str:
    return " ".join(name.lower().replace("_", " ").replace("#", " ").split())


def _is_corpse(npc: int) -> bool:
    return npc in (2, 3)


def _nearest(world, spawns):
    if not spawns:
        return None
    return min(spawns, key=lambda spawn: _dist(world, spawn.x, spawn.y))


def _dist(world, x: float, y: float) -> float:
    return math.hypot(world.x - x, world.y - y)


def _at(world, kind, target, name, x, y, z, item_id: int = 0) -> Intention:
    return Intention(kind, target, name, item_id, (x, y, z), _dist(world, x, y))
