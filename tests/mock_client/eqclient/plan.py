"""Pick one next action from the world, the task list, and this zone's scripts.

`choose` stays inside the current zone. `guide` sits above it and leaves for the
zone a remaining step names, or for the bind point when the book is empty.
"""

from __future__ import annotations

import math
import re
from dataclasses import dataclass

from eqclient.camps import camp_for_level
from eqclient.items import PRIMARY, Inventory, can_receive
from eqclient.quests import Need, ZoneQuests, next_node
from eqclient.spells import spell_step
from eqclient.tasks import DELIVER, KILL, LOOT, SPEAK, Activity, TaskBook
from eqclient.world import ZoneModel
from eqclient.zones import zone_id_of

_IDS = re.compile(r"\d+")
ATTACK_RANGE = 25.0
LEAVE_LEVEL = 5
SAFE_RANGE = 20.0
CITY_ZONES = {202}
_TRAINER_OFFSET = 19


@dataclass(frozen=True)
class Lesson:
    """What a quest popup told him to do next."""

    kind: str
    name: str
    text: str = ""


def recover(hurt: bool, engaged: bool, at_safe: bool, *, sit_here: bool = False) -> str | None:
    """Low health finishes the current fight, then sits (or walks to safe first).

    None keeps the current plan. "safe" walks to the zone safe point. "rest" sits.
    Low-level zones (sit_here) sit in place — no hike to the safe point.
    """
    if not hurt or engaged:
        return None
    return "rest" if at_safe or sit_here else "safe"


def lesson_from(text: str) -> Lesson | None:
    """The action in a popup. 'Press OK' is the button, not the instruction."""
    if not text:
        return None
    ask = re.search(r"\bask\s+([A-Za-z][\w']+(?:\s+[A-Za-z][\w']+)*)\s+to\s+'([^']+)'", text, re.IGNORECASE)
    if ask:
        return Lesson("say", ask.group(1).strip(), ask.group(2).strip())
    give = re.search(r"\bgive your\b.+?\bto\s+([A-Za-z][\w']+)", text, re.IGNORECASE)
    if give:
        return Lesson("hand_in", give.group(1))
    if re.search(r"right click", text, re.IGNORECASE) and re.search(r"\btome\b", text, re.IGNORECASE):
        return Lesson("learn", "tome")
    click = re.search(r"\bclick on\s+([A-Z][\w']+)'s\b", text)
    if click:
        return Lesson("talk", click.group(1))
    hail = re.search(r"\b[Hh]ail\s+([A-Z][\w']+(?:\s+[A-Z][\w']+)*)", text)
    if hail:
        return Lesson("talk", hail.group(1).strip())
    respond = re.search(r"\brespond to\s+(.+?)'s dialogue", text, re.IGNORECASE)
    if respond:
        return Lesson("talk", respond.group(1).strip())
    if re.search(r"rectangular icon|auto-equip", text, re.IGNORECASE):
        return Lesson("equip", "primary")
    deliver = re.search(r"\bdeliver it to\s+([A-Z][\w']+)", text)
    if deliver:
        found = re.search(r"\bfind the\s+([A-Z][^.<\n]+)", text)
        return Lesson("fetch", deliver.group(1), found.group(1).strip() if found else "")
    if re.search(r"escape to norrath", text, re.IGNORECASE):
        return Lesson("leave", "")
    return None


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
    lesson: Lesson | None = None,
    flags: set[str] | None = None,
) -> Intention | None:
    skipped_ground = skipped_ground or set()
    flags = flags or set()
    skipped_corpses = skipped_corpses or set()
    said = said or set()
    handed = handed or set()
    if not party_ready:
        return Intention("form_party")

    corpse = _own_corpse(world, quests, skipped_corpses)
    if corpse is not None:
        return corpse

    if not tasks.local_work_left():
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

    guided = _lesson_step(world, lesson, inventory)
    if guided is not None:
        return guided

    tome = inventory.tome()
    if tome is not None:
        return Intention("learn", name=tome.name, item_id=tome.item_id)

    spell = spell_step(inventory, world.class_id)
    if spell is not None:
        kind, spell_id, label = spell
        return Intention(kind, name=label, item_id=spell_id)

    scripted = _script_goal(world, tasks, quests, inventory, said, skipped_ground)
    if scripted is not None:
        return scripted

    tutorial = _tutorial_next(world, tasks, said, quests)
    if tutorial is not None:
        return tutorial
    if (world.zone or "").lower() == "tutorialb" and _mines_cleared(tasks) and quests.exits and not world.needs_corpse:
        door = _exit_door(world, quests.exits)
        if door is not None:
            return _at(world, "leave", door.door_id, door.name, door.x, door.y, door.z)

    owed = _promised(world, quests, inventory, said, handed)
    if owed is not None:
        return owed

    step = _task_step(world, tasks, quests, inventory, skipped_corpses, skipped_ground, said)
    if step is not None:
        return step
    grind = _grind(world, tasks)
    if grind is not None:
        return grind

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

    chain = _graph_step(world, quests, said, flags, inventory)
    if chain is not None:
        return chain

    talk = _quest_talk(world, tasks, quests, said)
    if talk is not None:
        return talk

    if (
        (world.zone or "").lower() == "tutorialb"
        and not tasks.local_work_left()
        and quests.exits
        and _ready_to_leave(world)
    ):
        door = _exit_door(world, quests.exits)
        if door is not None:
            return _at(world, "leave", door.door_id, door.name, door.x, door.y, door.z)
        return Intention("leave", target=quests.exits[0])
    if world.level and world.level < LEAVE_LEVEL and not tasks.local_work_left():
        enemy = _nearest(
            world,
            [
                spawn
                for spawn in world.spawns.values()
                if spawn.npc == 1 and world.faction.get(spawn.spawn_id) in (8, 9)
            ],
        )
        if enemy is not None:
            return _at(world, "fight", enemy.spawn_id, enemy.name, enemy.x, enemy.y, enemy.z)
    return Intention("explore")


def guide(
    world: ZoneModel,
    tasks: TaskBook,
    quests: ZoneQuests,
    inventory: Inventory,
    party_ready: bool,
    skipped_ground: set[int] | None = None,
    skipped_corpses: set[int] | None = None,
    said: set[tuple[str, str]] | None = None,
    handed: set[tuple[str, str]] | None = None,
    lesson: Lesson | None = None,
    visited_hubs: set[str] | None = None,
    flags: set[str] | dict[str, int] | None = None,
    graph=None,
    said_all: set[tuple[str, str, str]] | None = None,
    campaign=None,
    tutorial_done: bool = True,
    merchants=None,
    recipes=None,
    drops=None,
    factions=None,
    skills: dict[int, int] | None = None,
) -> Intention | None:
    """Zone choice above the task planner.

    An open step in this zone is still `choose`. When this zone's list is done,
    the next step's zone is the destination. An empty book walks home once the
    in-zone planner has nothing left but wandering. A door is taken only when
    this zone's scripts move through it to that zone. A campaign obtain-stack
    sits above aimless hub wander when tasks are idle.

    Until the Gloomingdeep tutorial is finished, campaign goals stay deferred
    and the agent stays on (or returns toward) tutorialb.
    """
    if world.zone_id:
        tasks.here_id = world.zone_id
    # Own corpse (coin + gear) outranks campaign grind — otherwise every death
    # bleeds platinum while we chase the next scarab. Always reclaim (take_all);
    # do not gate on bag space or we walk away from coin on the body.
    skipped_corpses = skipped_corpses or set()
    corpse = _own_corpse(world, quests, skipped_corpses)
    if corpse is not None:
        return corpse
    # New / unfinished characters: clear the mines before any epic/farm campaign.
    if not tutorial_done:
        if (world.zone or "").lower() != "tutorialb":
            return Intention("explore", name="tutorialb", text="tutorial")
        campaign = None
    # A scroll already in a bag is written before the next obtain goal, or the
    # campaign pops the goal for holding it and never comes back to scribe.
    if tutorial_done:
        spell = spell_step(inventory, world.class_id)
        if spell is not None and spell[0] == "scribe":
            kind, spell_id, label = spell
            return Intention(kind, name=label, item_id=spell_id)
    # Epic / farm obtain stack outranks open tasks once the tutorial is done.
    campaign_act = _campaign_intention(
        world,
        inventory,
        flags,
        graph,
        campaign,
        merchants,
        recipes,
        drops,
        factions,
        skills,
        skipped_ground,
        skipped_corpses,
    )
    if campaign_act is not None:
        return campaign_act
    if tasks.local_work_left() or tasks.pending or tasks.offer is not None:
        return choose(
            world, tasks, quests, inventory, party_ready, skipped_ground, skipped_corpses, said, handed, lesson, flags
        )
    destination = tasks.away_zone_id()
    if destination and destination != world.zone_id:
        door = _door_to(world, quests, destination)
        if door is not None:
            return _at(world, "leave", door.door_id, f"zone {destination}", door.x, door.y, door.z)
    local = choose(
        world, tasks, quests, inventory, party_ready, skipped_ground, skipped_corpses, said, handed, lesson, flags
    )
    if (
        not tasks.has_open_work()
        and world.home_zone_id
        and world.home_zone_id != world.zone_id
        and (local is None or (local.kind == "explore" and not local.name))
    ):
        door = _door_to(world, quests, world.home_zone_id)
        if door is not None:
            return _at(world, "leave", door.door_id, f"zone {world.home_zone_id}", door.x, door.y, door.z)
    if (
        graph is not None
        and not tasks.has_open_work()
        and (local is None or (local.kind == "explore" and not local.name))
    ):
        flag_arg = flags if isinstance(flags, set) else set(flags or ())
        away = graph.continuation(
            world.zone or "",
            said_all or set(),
            flag_arg,
            world.class_id,
            {held.item_id for held in inventory.slots.values()},
        )
        if away is not None:
            dest = zone_id_of(away.zone)
            door = _door_to(world, quests, dest) if dest else None
            if door is not None:
                return _at(world, "leave", door.door_id, away.zone, door.x, door.y, door.z)
            return Intention("explore", name=away.zone, text=away.npc)
    if (
        _is_city(world)
        and not tasks.has_open_work()
        and (local is None or (local.kind == "explore" and not local.name))
    ):
        return hub_goal(world, quests, visited_hubs or set())
    return local


def _campaign_intention(
    world,
    inventory,
    flags,
    graph,
    campaign,
    merchants=None,
    recipes=None,
    drops=None,
    factions=None,
    skills: dict[int, int] | None = None,
    skipped_ground: set[int] | None = None,
    skipped_corpses: set[int] | None = None,
) -> Intention | None:
    """Map the obtain-stack tip to an Intention, or None when idle/blocked/done."""
    if campaign is None or graph is None or not getattr(campaign, "stack", None):
        return None

    skipped_corpses = skipped_corpses or set()
    counts: dict[int, int] = {}
    for held in inventory.slots.values():
        counts[held.item_id] = counts.get(held.item_id, 0) + (held.stack or 1)
    flag_values = flags if isinstance(flags, dict) else {name: 1 for name in (flags or ())}
    bag_full = inventory.empty_general() is None and inventory.cursor() is not None
    step = campaign.next_step(
        graph,
        counts,
        flag_values,
        world.level or 0,
        world.zone or "",
        bag_full=bag_full,
        copper=world.coin if getattr(world, "coin_known", False) else None,
        merchants=merchants,
        recipes=recipes,
        drops=drops,
        factions=factions,
        skills=skills,
    )
    if step.kind in {"done", "blocked"}:
        return None
    if step.kind == "travel" and step.zone:
        return _zone_travel(world, graph, inventory, step.zone, text=step.npc or step.kind, item_id=step.item_id)
    if step.kind == "sell":
        spawn, zone = _vendor(world, merchants, step.item_id)
        if spawn is not None:
            return Intention("shop", spawn.spawn_id, spawn.name, step.item_id, (spawn.x, spawn.y, spawn.z), text="sell")
        if zone and zone != (world.zone or "").lower():
            return Intention("explore", name=zone, item_id=step.item_id, text="sell")
        return Intention("explore", name="merchant", item_id=step.item_id, text="sell")
    if step.kind in {"safe", "bank"}:
        return Intention("explore", name="safe", where=world.safe, text=step.kind)
    if step.kind == "craft" and step.recipe_id:
        return Intention("craft", target=step.recipe_id, item_id=step.item_id)
    if step.kind == "farm":
        why = grind_why("farm", item_id=step.item_id, kind="farm")
        camp = camp_for_level(world.level or 1, world.zone or "")
        if camp and (world.zone or "").lower() != camp.zone:
            return _zone_travel(world, graph, inventory, camp.zone, text=why, item_id=step.item_id)
        corpse = _grind_corpse(world, skipped_corpses)
        if corpse is not None:
            return _at(
                world,
                "loot",
                corpse.spawn_id,
                corpse.name,
                corpse.x,
                corpse.y,
                corpse.z,
                item_id=step.item_id,
                text=why,
            )
        foe = _xp_foe(world)
        if foe is not None:
            return _at(
                world,
                "fight",
                foe.spawn_id,
                foe.name,
                foe.x,
                foe.y,
                foe.z,
                item_id=step.item_id,
                text=why,
            )
        return Intention("grind", name=camp.zone if camp else "farm", text=why, item_id=step.item_id)

    if step.kind == "buy":
        from eqclient.items import BACKPACK_ITEM, bags_buyable

        if step.item_id:
            name = str((getattr(graph, "items", None) or {}).get(int(step.item_id), {}).get("name") or "").lower()
            if (step.item_id == BACKPACK_ITEM or "backpack" in name) and bags_buyable(inventory) <= 0:
                return None
        spawn = None
        for candidate in world.spawns.values():
            if candidate.npc == 1 and _norm(candidate.name) == _norm(step.npc):
                spawn = candidate
                break
        if spawn is not None:
            return Intention("shop", spawn.spawn_id, spawn.name, step.item_id, (spawn.x, spawn.y, spawn.z), text="buy")
        if step.zone and (world.zone or "").lower() != step.zone.lower():
            return Intention("explore", name=step.zone, text=step.npc or "buy")
        return Intention("explore", name=step.npc or "merchant", item_id=step.item_id, text="buy")
    if step.kind in {"hail", "hand"} and step.npc:
        spawn = None
        for candidate in world.spawns.values():
            if candidate.npc == 1 and _norm(candidate.name) == _norm(step.npc):
                spawn = candidate
                break
        if spawn is not None:
            kind = "hand_in" if step.kind == "hand" else "task_talk"
            text = step.text if step.kind == "hand" and step.text else (step.word or "Hail")
            return Intention(kind, spawn.spawn_id, spawn.name, step.item_id, (spawn.x, spawn.y, spawn.z), text=text)
        return Intention("explore", name=step.npc, text=step.zone)
    if step.kind in {"kill", "loot"} and (step.npc or step.zone):
        return _hunt(world, step, skipped_ground)
    if step.kind in {"forage", "fish"}:
        return Intention(step.kind, item_id=step.item_id, name=step.zone, text=step.text)
    if step.kind == "pick_lock":
        door = _door_for(world, step)
        if door is not None:
            return _at(world, "pick_lock", door.door_id, step.zone or door.name, door.x, door.y, door.z, step.item_id)
        return Intention("pick_lock", item_id=step.item_id, name=step.zone, text=step.text)
    if step.kind == "skill":
        return _skill_intention(step, recipes)
    if step.kind == "faction":
        return _faction_intention(world, step, factions)
    if step.kind in {"encounter", "boss"}:
        return _hunt(world, step, skipped_ground)
    if step.kind == "chest":
        drop = _ground_drop(world, step, skipped_ground)
        if drop is not None:
            return Intention("fetch", drop.drop_id, drop.name, step.item_id, (drop.x, drop.y, drop.z), text="ground")
        return _hunt(world, step, skipped_ground)
    if step.kind == "key":
        door = _door_for(world, step)
        if door is not None:
            return _at(world, "pick_lock", door.door_id, step.zone or door.name, door.x, door.y, door.z, step.item_id)
        return Intention("explore", name=step.npc or step.zone or "door", item_id=step.item_id, text="key")
    if step.kind == "instance":
        if step.zone and (world.zone or "").lower() != step.zone.lower():
            return Intention("explore", name=step.zone, item_id=step.item_id, text="instance")
        door = _door_for(world, step)
        if door is not None:
            return _at(world, "leave", door.door_id, step.zone or door.name, door.x, door.y, door.z, step.item_id)
        live = _named(world, step.npc, corpses=False) if step.npc else None
        if live is not None:
            return _at(world, "task_talk", live.spawn_id, live.name, live.x, live.y, live.z, step.item_id)
        return Intention("explore", name=step.npc or step.zone, item_id=step.item_id, text="instance")
    if step.kind == "level":
        why = grind_why(step.text, item_id=step.item_id, kind="level")
        camp = camp_for_level(world.level or 1, world.zone or "")
        if camp and (world.zone or "").lower() != camp.zone:
            return _zone_travel(world, graph, inventory, camp.zone, text=why, item_id=step.item_id)
        corpse = _grind_corpse(world, skipped_corpses)
        if corpse is not None:
            return _at(
                world,
                "loot",
                corpse.spawn_id,
                corpse.name,
                corpse.x,
                corpse.y,
                corpse.z,
                item_id=step.item_id,
                text=why,
            )
        foe = _xp_foe(world)
        if foe is not None:
            return _at(
                world,
                "fight",
                foe.spawn_id,
                foe.name,
                foe.x,
                foe.y,
                foe.z,
                item_id=step.item_id,
                text=why,
            )
        return Intention("grind", name=camp.zone if camp else "xp", text=why, item_id=step.item_id)
    return None


def _hunt(world, step, skipped_ground=None) -> Intention:
    """Kill or loot a named target. Ground objects are clicked. A down camp is cleared."""
    if step.text == "ground" or step.kind == "chest":
        drop = _ground_drop(world, step, skipped_ground)
        if drop is not None:
            return Intention("fetch", drop.drop_id, drop.name, step.item_id, (drop.x, drop.y, drop.z), text="ground")
        if step.text == "ground":
            return Intention("explore", name=step.zone or step.npc or "ground", item_id=step.item_id, text="ground")
    if step.npc:
        corpse = _named(world, step.npc, corpses=True)
        if corpse is not None:
            return _at(world, "loot", corpse.spawn_id, corpse.name, corpse.x, corpse.y, corpse.z, step.item_id)
        live = _named(world, step.npc, corpses=False)
        if live is not None:
            return _at(world, "task_kill", live.spawn_id, live.name, live.x, live.y, live.z, step.item_id)
        foe = _other_foe(world)
        if foe is not None:
            intent = _at(world, "fight", foe.spawn_id, foe.name, foe.x, foe.y, foe.z, step.item_id)
            intent.text = "respawn"
            return intent
    return Intention("explore", name=step.npc or step.zone, item_id=step.item_id, text=step.kind)


def _ground_drop(world, step, skipped_ground):
    skipped = skipped_ground or set()
    want = _norm(getattr(step, "npc", "") or "")
    best = None
    best_d = 1e18
    here = world.position
    for drop in world.ground.values():
        if drop.drop_id in skipped:
            continue
        if want and want != _norm(drop.name) and want not in _norm(drop.name):
            continue
        dist = (here[0] - drop.x) ** 2 + (here[1] - drop.y) ** 2
        if dist < best_d:
            best, best_d = drop, dist
    return best


def _door_for(world, step):
    """A door id on the step, else the nearest door whose name matches the step."""
    token = str(getattr(step, "text", "") or "")
    if token.isdigit():
        door = world.doors.get(int(token))
        if door is not None:
            return door
    wants = [name for name in (_norm(getattr(step, "npc", "") or ""), _norm(getattr(step, "zone", "") or "")) if name]
    if not wants:
        return None
    best = None
    best_d = 1e18
    here = world.position
    for door in world.doors.values():
        name = _norm(door.name)
        if not any(want == name or want in name for want in wants):
            continue
        dist = (here[0] - door.x) ** 2 + (here[1] - door.y) ** 2
        if dist < best_d:
            best, best_d = door, dist
    return best


def _vendor(world, merchants, item_id: int):
    """A spawned shopkeeper from the merchant cache (or keyword), else their zone."""
    from eqclient.merchants import _norm_name

    zone = world.zone or ""
    known = merchants.names_in(zone) if merchants is not None and getattr(merchants, "by_npc", None) else set()
    want = ""
    seller_zone = ""
    if merchants is not None and item_id:
        found = merchants.best(item_id, zone)
        if found is not None:
            seller, _cost = found
            want = _norm_name(seller.name)
            seller_zone = seller.zone
    best = None
    best_rank = 3
    for spawn in world.spawns.values():
        if spawn.npc != 1:
            continue
        folded = _norm_name(spawn.name)
        name = (spawn.name or "").lower()
        if want and folded == want:
            rank = 0
        elif folded in known:
            rank = 1
        elif any(word in name for word in ("merchant", "vendor", "shopkeeper")):
            rank = 2
        else:
            continue
        if best is None or rank < best_rank:
            best = spawn
            best_rank = rank
            if rank == 0:
                break
    if best is not None:
        return best, ""
    if seller_zone:
        return None, seller_zone
    if merchants is not None and item_id:
        found = merchants.best(item_id, zone)
        if found is not None:
            return None, found[0].zone
    return None, ""


def _skill_intention(step, recipes=None) -> Intention:
    """Fish/forage loops, or a practice combine toward the recipe trivial."""
    body = str(step.text or "")
    skill_id = 0
    if "@" in body:
        raw, _, _want = body.partition("@")
        if raw.isdigit():
            skill_id = int(raw)
    # EQ skill ids: 27 forage, 55 fishing.
    if skill_id == 55:
        return Intention("fish", item_id=step.item_id, text=body)
    if skill_id == 27:
        return Intention("forage", item_id=step.item_id, text=body)
    if step.recipe_id:
        # Practice recipe may still need components — campaign nests those via need_item.
        return Intention("craft", target=step.recipe_id, item_id=step.item_id, text=body)
    return Intention("explore", name="skill", text=body)


def _faction_intention(world, step, factions=None) -> Intention:
    """Farm NPCs that award the needed faction — never the gated quest NPC.

    Campaign sends the densest +faction zone in step.zone and a kill name in
    step.npc. Prefer those named hits; only then fall back to scowling mobs.
    """
    from eqclient.campaign import _parse_faction_spec

    spec = step.text or "faction"
    if step.zone and (world.zone or "").lower() != step.zone.lower():
        return Intention("explore", name=step.zone, text=spec)
    # word="@zone/quest npc" names the gated NPC; step.npc is then the farm kill target.
    quest_zone = ""
    quest_name = ""
    if str(step.word or "").startswith("@"):
        place = str(step.word)[1:]
        quest_zone, _, quest_name = place.partition("/")
        if not quest_name:
            quest_name = quest_zone
            quest_zone = ""
    protect = {_norm(quest_name)} if quest_name else set()
    # Legacy bare faction step: npc is the quest NPC — do not attack them.
    farming = bool(quest_name) or (factions is not None and str(step.text or "").startswith("faction:"))
    if not quest_name and step.npc and "primary" in spec:
        protect.add(_norm(step.npc))

    quest_spawn = None
    if quest_name:
        for candidate in world.spawns.values():
            if candidate.npc == 1 and _norm(candidate.name) == _norm(quest_name):
                quest_spawn = candidate
                break
    if quest_spawn is not None and "primary" in spec:
        standing = world.faction.get(quest_spawn.spawn_id)
        if standing is None:
            return Intention(
                "explore",
                target=quest_spawn.spawn_id,
                name=quest_spawn.name,
                where=(quest_spawn.x, quest_spawn.y, quest_spawn.z),
                text=f"faction-check:{spec}",
            )

    farm_names: set[str] = set()
    fac_id = 0
    fid, _need = _parse_faction_spec(spec)
    if factions is not None:
        if fid == "primary" and (quest_name or step.npc):
            fac_id = int(factions.primary(quest_zone or step.zone or "", quest_name or step.npc) or 0)
        elif fid.isdigit():
            fac_id = int(fid)
        if fac_id:
            farm_names = factions.farm_names(fac_id, world.zone or step.zone or "")

    # Prefer NPCs known to award this faction (cache), even if not scowling yet.
    named = [
        spawn
        for spawn in world.spawns.values()
        if spawn.npc == 1 and _norm(spawn.name) in farm_names and _norm(spawn.name) not in protect
    ]
    foe = _nearest(world, named)
    if foe is None and not farm_names:
        # No cache for this faction — only then fall back to scowling hostiles.
        foes = [
            spawn
            for spawn in world.spawns.values()
            if spawn.npc == 1 and world.faction.get(spawn.spawn_id) in (8, 9) and _norm(spawn.name) not in protect
        ]
        foe = _nearest(world, foes)
    if foe is not None:
        intent = _at(world, "fight", foe.spawn_id, foe.name, foe.x, foe.y, foe.z)
        intent.text = spec
        return intent
    # Hunt the named farm NPC when the densest zone has no live spawn yet.
    if farming and step.npc and _norm(step.npc) not in protect:
        return Intention("explore", name=step.npc, text=spec)
    return Intention("explore", name=step.zone or step.npc or "faction", text=spec)


def _is_city(world: ZoneModel) -> bool:
    return world.zone_id in CITY_ZONES or (world.zone or "").lower() == "poknowledge"


def hub_goal(world: ZoneModel, quests: ZoneQuests, visited: set[str]) -> Intention:
    """A named place in a city, or the safe point once every scripted NPC has been hailed."""
    spawn = _hub_spawn(world, quests, visited)
    if spawn is not None:
        return _at(world, "explore", spawn.spawn_id, "hub", spawn.x, spawn.y, spawn.z)
    if _horiz_safe(world) > SAFE_RANGE:
        return Intention("explore", name="safe", where=world.safe)
    return Intention("rest", name="health")


def _hub_spawn(world: ZoneModel, quests: ZoneQuests, visited: set[str]):
    trainer = _trainer(world)
    if trainer is not None and _norm(trainer.name) not in visited and _script(quests, trainer.name) is not None:
        return trainer
    scripted = [
        spawn
        for spawn in world.spawns.values()
        if spawn.npc == 1 and _norm(spawn.name) not in visited and _script(quests, spawn.name) is not None
    ]
    if not scripted:
        return None
    return min(scripted, key=lambda spawn: _dist(world, spawn.x, spawn.y))


def _horiz_safe(world: ZoneModel) -> float:
    return _dist(world, world.safe[0], world.safe[1])


def _ready_to_leave(world: ZoneModel) -> bool:
    """The mines are about level 5 by the time the exit is the right next step."""
    return not world.needs_corpse and (world.level == 0 or world.level >= LEAVE_LEVEL)


def _corpse_camped(world: ZoneModel) -> bool:
    """An enemy standing on the body. Walking there is how he dies again."""
    spot = world.own_corpse_at
    if spot is None or (world.zone or "").lower() == "tutorialb":
        return False
    for spawn in world.spawns.values():
        if spawn.npc != 1:
            continue
        if world.faction.get(spawn.spawn_id) not in (8, 9):
            continue
        if _span_spawn(spawn, spot) <= 25:
            return True
    return False


def _span_spawn(spawn, spot) -> float:
    return math.hypot(spawn.x - spot[0], spawn.y - spot[1])


def _is_own_corpse_name(character: str, spawn_name: str) -> bool:
    me = (character or "").lower()
    name = (spawn_name or "").lower()
    if not me or not name:
        return False
    return name == me or name.startswith(f"{me}'s corpse") or (me in name and "corpse" in name)


def _find_own_corpse_spawn(world: ZoneModel, skipped: set[int] | None = None):
    """Closest unreclaimed PC corpse to the player (not FIFO / not stuck on own_corpse_id)."""
    skipped = skipped or set()
    me = world.character or ""
    if not me:
        return None
    best = None
    best_dist = 1e18
    for spawn in world.spawns.values():
        if spawn.spawn_id in skipped or spawn.npc == 1:
            continue
        if not _is_own_corpse_name(me, spawn.name):
            continue
        if not _is_corpse(spawn.npc):
            continue
        d = _dist(world, spawn.x, spawn.y)
        if d < best_dist:
            best = spawn
            best_dist = d
    return best


def _own_corpse(
    world: ZoneModel,
    quests: ZoneQuests | None = None,
    skipped_corpses: set[int] | None = None,
) -> Intention | None:
    """Reclaim outstanding bodies closest-first until none remain."""
    skipped = skipped_corpses or set()
    # Emptied this husk — clear id and keep going for the next outstanding corpse.
    if world.own_corpse_id and world.own_corpse_id in skipped:
        world.own_corpse_id = 0
    if not world.needs_corpse:
        return None
    if world.own_corpse_zone and world.zone and world.own_corpse_zone.lower() != world.zone.lower():
        if quests is not None:
            door = _door_to(world, quests, zone_id_of(world.own_corpse_zone))
            if door is not None:
                return _at(world, "leave", door.door_id, world.own_corpse_zone, door.x, door.y, door.z)
        return Intention("explore", name="corpse", text=world.own_corpse_zone)
    if _corpse_camped(world):
        if _horiz_safe(world) > SAFE_RANGE:
            return Intention("explore", name="safe", where=world.safe)
        return Intention("tell", name="summon", text="summon")
    spawn = _find_own_corpse_spawn(world, skipped)
    if spawn is not None:
        world.own_corpse_id = spawn.spawn_id
        world.own_corpse_at = (spawn.x, spawn.y, spawn.z)
        world.own_corpse_zone = world.zone or world.own_corpse_zone
        return _at(world, "reclaim", spawn.spawn_id, spawn.name, spawn.x, spawn.y, spawn.z)
    if world.own_corpse_at is not None:
        x, y, z = world.own_corpse_at
        return Intention("reclaim", name=world.character, where=(x, y, z), distance=_dist(world, x, y))
    # Flag set but no body/coords yet — keep needs_corpse; agent re-seeds from journal.
    return None


def _trainer(world: ZoneModel):
    if not world.class_id:
        return None
    want = world.class_id + _TRAINER_OFFSET
    return _nearest(
        world,
        [spawn for spawn in world.spawns.values() if spawn.npc == 1 and spawn.class_id == want],
    )


def _tutorial_next(world, tasks, said, quests=None) -> Intention | None:
    """Once Basic Training leaves the window, Rahtiz and then Hobart assign the rest."""
    if _task_open(tasks, 1448) or _task_open(tasks, 5166) or _task_open(tasks, 5102):
        return None
    if tasks.task_finished(5102):
        return None
    # Level 4+ in the mines keeps looking for Hobart, but yield when another scripted
    # NPC in zone still has an unsaid keyword (e.g. Arias) so those chains can run.
    if world.level >= 4 and (
        _named(world, "Guard Hobart", corpses=False) is not None
        or ((world.zone or "").lower() == "tutorialb" and not _pending_script_keywords(world, quests, said))
    ):
        return _seek(world, "Guard Hobart")
    seen = {activity.task_id for activity in tasks.activities} | tasks.completed
    if not seen.intersection({1448, 5032, 5102, 5166}):
        return None
    if not _was_said(said, "Guard Rahtiz", "hail"):
        return _seek(world, "Guard Rahtiz")
    if not _was_said(said, "Guard Hobart", "hail"):
        return _seek(world, "Guard Hobart")
    return None


def _pending_script_keywords(world, quests, said) -> bool:
    if quests is None:
        return False
    for spawn in world.spawns.values():
        if spawn.npc != 1:
            continue
        script = _script(quests, spawn.name)
        if script is None:
            continue
        key = _norm(spawn.name)
        for keyword in script.keywords:
            if (key, keyword.lower()) not in said:
                return True
    return False


def _is_mine_mob(name: str) -> bool:
    text = name.lower()
    if any(skip in text for skip in ("barrel", "crate", "box", "campfire", "torch", "warden", "grunt", "spiritweaver")):
        return False
    return text.startswith(("a_gloom_spider", "a_gloomfang", "a_cave_rat", "a_cave_bat", "a_kobold"))


def _mine_target(world, skip: set[int] | None = None):
    """A creature that still gives experience. A same-level one nearby beats a grey bat."""
    skip = skip or set()
    hostiles = [
        spawn
        for spawn in world.spawns.values()
        if spawn.npc == 1 and spawn.spawn_id not in skip and _is_mine_mob(spawn.name)
    ]
    if not hostiles:
        return None
    floor = max(1, (world.level or 1) - 1)
    worthy = [spawn for spawn in hostiles if spawn.level >= floor]
    return _nearest(world, worthy or hostiles)


def _grind(world, tasks) -> Intention | None:
    """Level 4 is the battle. Keep fighting the mine's creatures until then."""
    if not world.level or world.level >= 4 or tasks.task_finished(5102):
        return None
    if _task_open(tasks, 1448) or _task_open(tasks, 5166) or _task_open(tasks, 5102):
        return None
    enemy = _mine_target(world)
    if enemy is None:
        return None
    return _at(world, "task_kill", enemy.spawn_id, enemy.name, enemy.x, enemy.y, enemy.z)


def _task_open(tasks, task_id: int) -> bool:
    return any(
        activity.task_id == task_id and not activity.finished and not activity.optional for activity in tasks.activities
    )


def _mines_cleared(tasks) -> bool:
    if _task_open(tasks, 1448) or _task_open(tasks, 5166) or _task_open(tasks, 5102):
        return False
    return tasks.task_finished(5102)


def _seek(world, name: str) -> Intention:
    spawn = _named(world, name, corpses=False)
    if spawn is not None:
        return _at(world, "task_talk", spawn.spawn_id, spawn.name, spawn.x, spawn.y, spawn.z)
    return _explore_name(world, name)


def _script_goal(world, tasks, quests, inventory, said, skipped_ground) -> Intention | None:
    """The line a script checks off, which is not always the name in the quest window."""
    said = said or set()
    pending = [activity for activity in tasks.current() if not activity.finished and not activity.optional]
    pending.sort(key=lambda activity: (activity.task_id, activity.activity_id))
    for activity in pending:
        key = (activity.task_id, activity.activity_id)
        for script in quests.scripts.values():
            for word, hits in script.advances.items():
                if key not in hits or (word != "hail" and _was_said(said, script.npc, word)):
                    continue
                spawn = _named(world, script.npc, corpses=False)
                if spawn is None:
                    return _explore_name(world, script.npc)
                if word != "hail" and _was_said(said, script.npc, "hail"):
                    intent = _at(world, "talk", spawn.spawn_id, spawn.name, spawn.x, spawn.y, spawn.z)
                    intent.text = word
                    return intent
                return _at(world, "task_talk", spawn.spawn_id, spawn.name, spawn.x, spawn.y, spawn.z)
            for item_id, hits in script.delivers.items():
                if key not in hits:
                    continue
                spawn = _named(world, script.npc, corpses=False)
                if inventory.count(item_id) > 0 and spawn is not None:
                    return _at(world, "hand_in", spawn.spawn_id, spawn.name, spawn.x, spawn.y, spawn.z, item_id=item_id)
                found = _known_ground(world, inventory, [Need(item_id, 1, script.npc)], skipped_ground)
                if found is not None:
                    return found
                return _nearest_ground(world, skipped_ground, item_id)
    return None


def _nearest_ground(world, skipped, item_id: int) -> Intention | None:
    objects = [obj for obj in world.ground.values() if obj.drop_id not in skipped]
    if not objects:
        return None
    obj = min(objects, key=lambda item: _dist(world, item.x, item.y))
    return _at(world, "fetch", obj.drop_id, obj.name, obj.x, obj.y, obj.z, item_id=item_id)


def _task_step(world, tasks, quests, inventory, skipped_corpses, skipped_ground, said=None) -> Intention | None:
    said = said or set()
    activities = [activity for activity in tasks.current() if not _hail_already_failed(activity, said, quests)]
    if not activities:
        return None
    options = [
        _one_activity(world, tasks, quests, inventory, activity, skipped_corpses, skipped_ground, said)
        for activity in activities
    ]
    concrete = [item for item in options if item.kind != "explore"]
    pool = concrete or options
    return min(pool, key=lambda item: item.distance)


def _hail_already_failed(activity: Activity, said: set[tuple[str, str]], quests=None) -> bool:
    """Skip a hail that was already said and does not check this step off."""
    if activity.kind != SPEAK or activity.finished or not _was_said(said, activity.target_name, "hail"):
        return False
    if quests is not None:
        pair = (activity.task_id, activity.activity_id)
        for script in quests.scripts.values():
            if pair in script.advances.get("hail", set()) and _names_match(script.npc, activity.target_name):
                return False
    return True


def _one_activity(
    world, tasks, quests, inventory, activity: Activity, skipped_corpses, skipped_ground, said=None
) -> Intention:
    said = said or set()
    if activity.kind == DELIVER and not _was_said(said, activity.target_name, "hail"):
        spawn = _named(world, activity.target_name, corpses=False)
        if spawn is not None:
            return _at(world, "task_talk", spawn.spawn_id, spawn.name, spawn.x, spawn.y, spawn.z)
        return _explore_name(world, activity.target_name)
    if activity.kind == SPEAK:
        spawn = _named(world, activity.target_name, corpses=False)
        if spawn is not None:
            return _at(world, "task_talk", spawn.spawn_id, spawn.name, spawn.x, spawn.y, spawn.z)
        return _explore_name(world, activity.target_name)
    if activity.kind == KILL:
        live = _named(world, activity.target_name, corpses=False)
        if live is not None:
            return _at(world, "task_kill", live.spawn_id, live.name, live.x, live.y, live.z)
        return _explore_name(world, activity.target_name)
    if activity.kind == LOOT:
        corpse = _named(world, activity.target_name, corpses=True, skip=skipped_corpses)
        if corpse is not None:
            return _at(world, "loot", corpse.spawn_id, corpse.name, corpse.x, corpse.y, corpse.z)
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
    known = _known_ground(
        world, inventory, [need for need in needs if inventory.count(need.item_id) < need.count], skipped_ground
    )
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


def _promised(world, quests, inventory, said: set[tuple[str, str]], handed: set[tuple[str, str]]) -> Intention | None:
    """An NPC already hailed, who accepts an item the login inventory shows we hold."""
    ready: list[tuple[Need, object]] = []
    for script in quests.scripts.values():
        if not _was_said(said, script.npc, "hail"):
            continue
        for need in script.needs:
            if _was_said(handed, need.npc, str(need.item_id)):
                continue
            if inventory.count(need.item_id) < need.count:
                continue
            spawn = _named(world, script.npc, corpses=False)
            if spawn is not None:
                ready.append((need, spawn))
    if not ready:
        return None
    need, spawn = min(ready, key=lambda pair: _dist(world, pair[1].x, pair[1].y))
    return _at(world, "hand_in", spawn.spawn_id, spawn.name, spawn.x, spawn.y, spawn.z, item_id=need.item_id)


def _was_said(records: set[tuple[str, str]], npc: str, detail: str) -> bool:
    return any(item == detail and _names_match(who, npc) for who, item in records)


def _turn_in(world, tasks, quests, inventory, handed: set[tuple[str, str]]) -> Intention | None:
    ready: list[tuple[Need, object]] = []
    for need in _script_needs(quests, Inventory()):  # counts from zero, so every script need
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


def _graph_step(world, quests, said, flags, inventory) -> Intention | None:
    """The next say or hand-in on a parsed chain, not the first keyword in the file."""
    items = {held.item_id for held in inventory.slots.values()}
    nearest = None
    nearest_dist = 1e9
    for spawn in world.spawns.values():
        if spawn.npc != 1:
            continue
        nodes = quests.chains.get(_norm(spawn.name), [])
        if not nodes:
            continue
        said_words = {detail.lower() for npc, detail in said if _norm(npc) == _norm(spawn.name)}
        node = next_node(nodes, said_words, flags, world.class_id, items)
        if node is None:
            continue
        dist = _dist(world, spawn.x, spawn.y)
        if dist < nearest_dist:
            nearest = (spawn, node)
            nearest_dist = dist
    if nearest is None:
        return None
    spawn, node = nearest
    if node.kind == "hand":
        return _at(world, "hand_in", spawn.spawn_id, spawn.name, spawn.x, spawn.y, spawn.z, item_id=node.item_id)
    intent = _at(world, "task_talk", spawn.spawn_id, spawn.name, spawn.x, spawn.y, spawn.z)
    return Intention(intent.kind, intent.target, intent.name, intent.item_id, intent.where, intent.distance, node.word)


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


def _door_to(world, quests: ZoneQuests, zone_id: int):
    """The nearest visible door whose script moves into this zone id."""
    matches = [door_id for door_id, zones in quests.destinations.items() if zone_id in zones]
    return _exit_door(world, matches)


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


def _lesson_step(world, lesson: Lesson | None, inventory: Inventory) -> Intention | None:
    if lesson is None:
        return None
    if lesson.kind == "leave":
        return Intention("leave", name="exit")
    if lesson.kind == "equip":
        return Intention("equip", name="primary")
    if lesson.kind == "learn":
        held = inventory.tome()
        if held is None:
            return None
        return Intention("learn", name=held.name)
    if lesson.kind == "fetch":
        return _explore_name(world, lesson.text or lesson.name)
    spawn = _named(world, lesson.name, corpses=False)
    if spawn is None:
        return _explore_name(world, lesson.name)
    if lesson.kind == "say":
        intent = _at(world, "talk", spawn.spawn_id, spawn.name, spawn.x, spawn.y, spawn.z)
        intent.text = lesson.text
        return intent
    if lesson.kind == "hand_in":
        held = inventory.slots.get(PRIMARY)
        item_id = held.item_id if held is not None else 0
        return _at(world, "hand_in", spawn.spawn_id, spawn.name, spawn.x, spawn.y, spawn.z, item_id=item_id)
    return _at(world, "hail", spawn.spawn_id, spawn.name, spawn.x, spawn.y, spawn.z)


def _explore_name(world, name: str) -> Intention:
    spawn = _named(world, name, corpses=False)
    if spawn is not None:
        return _at(world, "task_talk", spawn.spawn_id, spawn.name, spawn.x, spawn.y, spawn.z)
    seen = world.last_seen.get(name.lower()) or world.last_seen.get(_norm(name))
    if seen is None:
        for key, value in world.last_seen.items():
            if _names_match(key, name):
                seen = value
                break
    if seen is not None and seen[0] == world.zone:
        return Intention(
            "explore", name=name, where=(seen[1], seen[2], seen[3]), distance=_dist(world, seen[1], seen[2])
        )
    return Intention("explore", name=name, distance=1e9)


def _names_match(spawn_name: str, target: str) -> bool:
    left = _norm(spawn_name)
    right = _norm(target)
    if not left or not right:
        return False
    if left == right or right in left or left in right:
        return True
    words = [word for word in right.split() if word not in ("a", "an", "the")]
    return bool(words) and all(word.rstrip("s") in left for word in words)


def _norm(name: str) -> str:
    return " ".join(name.lower().replace("_", " ").replace("#", " ").split())


def _is_corpse(npc: int) -> bool:
    return npc in (2, 3)


def _other_foe(world):
    """Nearest hostile while the drop mob is down. An empty camp means keep roaming."""
    return _xp_foe(world, unknown=False)


def _camp_mob(spawn) -> bool:
    """Outdoor trash: a_/an_ names, undead/animal body, or known hostile types — not vendors."""
    if getattr(spawn, "class_id", 0) in (40, 41, 59, 60, 61, 63, 66, 67, 71):
        return False
    name = (spawn.name or "").lower().replace("#", "")
    # City non-combatants that still use a_ names (Freeport prisoners, etc.).
    if any(
        tip in name
        for tip in (
            "prisoner",
            "guard",
            "merchant",
            "banker",
            "vendor",
            "shopkeeper",
            "citizen",
            "militia",
            "knight_of",
            "phineas",
        )
    ):
        return False
    if name.startswith("a_") or name.startswith("an_"):
        return True
    # Undead / animal / monster / summoned body types.
    if getattr(spawn, "body", 0) in (3, 21, 22, 25, 28):
        return True
    return any(
        tip in name
        for tip in (
            "skeleton",
            "deathfist",
            "orc_",
            "gnoll",
            "kobold",
            "bandit",
            "dervish",
            "mummy",
            "zombie",
            "ghoul",
        )
    )


def _grind_corpse(world, skipped_corpses=None):
    """Nearest NPC corpse within a short walk — loot bot and agent kills alike.

    Never pick a PC corpse here (npc==2). Our own body is handled by _own_corpse
    reclaim so coin is taken; treating it as grind loot skips the reclaim path.
    """
    skipped = skipped_corpses or set()
    me = (world.character or "").lower()
    corpses = [
        spawn
        for spawn in world.spawns.values()
        if spawn.npc == 3  # NPC corpse only (2 = PC corpse)
        and spawn.spawn_id not in skipped
        and (not me or me not in (spawn.name or "").lower())
    ]
    corpse = _nearest(world, corpses)
    if corpse is None or _dist(world, corpse.x, corpse.y) > 80:
        return None
    return corpse


def _xp_level_band(lvl: int, me: int) -> int:
    """Lower is better. Grind only L..L+2 (skip greens and L+3+)."""
    if not lvl:
        return 3  # unknown — last resort only
    if lvl == me:
        return 0
    if lvl == me + 1:
        return 1
    if lvl == me + 2:
        return 2
    if lvl < me:
        return 4  # green / grey — never grind
    return 5  # me+3+ — never grind


def _xp_foe(
    world,
    *,
    unknown: bool = True,
    skip: set[int] | None = None,
    can_see=None,
    sight_only: bool = False,
):
    """Grind target: LOS + level in [me, me+2], else closest spawn in that band.

    `can_see(where)` — when set, line-of-sight mobs beat Find/spawn-pad hikes.
    `sight_only` — return None unless something is in sight (scan phase).
    """
    from eqclient.packets import is_enemy_faction

    skip = skip or set()
    me = max(int(world.level or 1), 1)

    def ok(spawn) -> bool:
        return spawn.npc == 1 and spawn.spawn_id not in skip and _camp_mob(spawn)

    def in_band(spawn) -> bool:
        lvl = int(getattr(spawn, "level", 0) or 0)
        return bool(lvl) and me <= lvl <= me + 2

    def score(spawn) -> tuple:
        """Lower is better.

        Sight scan: LOS, then level (same-level first), then distance.
        Walk pick: distance bucket first so a me+2 1900yd away never beats a
        fightable spawn across the yard — Find empties on far pads otherwise.
        """
        lvl = int(getattr(spawn, "level", 0) or 0)
        band = _xp_level_band(lvl, me)
        dist = _dist(world, spawn.x, spawn.y)
        if can_see is not None:
            los = 1
            try:
                los = 0 if can_see((spawn.x, spawn.y, spawn.z)) else 1
            except Exception:
                los = 1
            return (los, band, dist)
        # Walk: prefer close pads. Buckets keep band meaningful inside a range.
        near = 0 if dist <= 250.0 else (1 if dist <= 600.0 else 2)
        return (near, band, dist)

    def pick(spawns):
        if not spawns:
            return None
        # Hard bound: only L..L+2. Unknown levels only if nothing known-in-band exists.
        pool = [s for s in spawns if in_band(s)]
        if not pool and unknown:
            pool = [s for s in spawns if not int(getattr(s, "level", 0) or 0)]
        if not pool:
            return None
        if can_see is not None:
            seen = [s for s in pool if score(s)[0] == 0]
            if seen:
                pool = seen
            elif sight_only:
                return None
            else:
                near = [s for s in pool if score(s)[2] <= 200.0]
                if near:
                    pool = near
        elif sight_only:
            return None
        else:
            # Walk phase: never start a cross-zone hike if anything local exists.
            for limit in (250.0, 600.0, 1200.0):
                near = [s for s in pool if score(s)[2] <= limit]
                if near:
                    pool = near
                    break
        return min(pool, key=score)

    hostiles = [
        spawn
        for spawn in world.spawns.values()
        if ok(spawn) and is_enemy_faction(world.faction.get(spawn.spawn_id) or 0)
    ]
    foe = pick(hostiles)
    if foe is not None:
        return foe
    # Dubious / apprehensive (6–7) only — never indifferent (5). City guards often
    # con indifferent; hitting them ruins Qeynos/Freeport standing for later visits.
    wary = [spawn for spawn in world.spawns.values() if ok(spawn) and world.faction.get(spawn.spawn_id) in (6, 7)]
    foe = pick(wary)
    if foe is not None or not unknown:
        return foe
    unchecked = [spawn for spawn in world.spawns.values() if ok(spawn) and spawn.spawn_id not in world.faction]
    return pick(unchecked)


def _nearest(world, spawns):
    if not spawns:
        return None
    return min(spawns, key=lambda spawn: _dist(world, spawn.x, spawn.y))


def _dist(world, x: float, y: float) -> float:
    return math.hypot(world.x - x, world.y - y)


def grind_why(
    target: int | str | None = None,
    *,
    item_id: int = 0,
    kind: str = "level",
) -> str:
    """Log label for a campaign grind — always a goal: level gate or farm item."""
    if kind == "farm" or str(target or "").strip().lower() == "farm":
        return f"farm item={item_id}" if item_id else "farm"
    raw = str(target or "").strip()
    if raw.lower().startswith("grind to l"):
        return raw
    if raw.lower().startswith("farm"):
        return raw
    digits = raw.lstrip("Ll")
    if digits.isdigit():
        label = f"grind to L{int(digits)}"
        return f"{label} item={item_id}" if item_id else label
    if item_id:
        return f"grind for item={item_id}"
    return "grind"


def _zone_travel(world, graph, inventory, dest: str, text: str = "", item_id: int = 0) -> Intention:
    """When dest is another zone, push leave via the first transit leg (else explore toward it)."""
    from eqclient.travel import first_leg
    from eqclient.zones import canonical_zone

    dest = canonical_zone(dest)
    here = (world.zone or "").lower()
    if not dest or dest == here:
        return Intention("explore", name=dest or here, text=text, item_id=item_id)
    held = {h.item_id for h in inventory.slots.values()}
    # Prefer graph edge coords (zone_point) over live door id — ids collide with city doors.
    leg = first_leg(graph, here, dest, inventory_ids=held) if graph else None
    if leg is not None and here == leg.zone:
        for edge in getattr(graph, "edges", ()) or ():
            if edge.get("rel") != "travel":
                continue
            if str(edge.get("from") or "").lower() != leg.zone or int(edge.get("door") or 0) != leg.door_id:
                continue
            if edge.get("x") is not None and (float(edge["x"]) or float(edge["y"]) or float(edge["z"])):
                return _at(
                    world,
                    "leave",
                    leg.door_id,
                    leg.dest,
                    float(edge["x"]),
                    float(edge["y"]),
                    float(edge["z"]),
                    item_id=item_id,
                    text=text,
                )
        door = world.doors.get(leg.door_id) if hasattr(world, "doors") else None
        if door is None:
            for candidate in (getattr(world, "doors", None) or {}).values():
                if candidate.door_id == leg.door_id:
                    door = candidate
                    break
        if door is not None:
            return _at(world, "leave", door.door_id, leg.dest, door.x, door.y, door.z, item_id=item_id, text=text)
        return Intention("leave", target=leg.door_id, name=leg.dest, text=text, item_id=item_id)
    return Intention("explore", name=dest, text=text or "travel", item_id=item_id)


def _at(world, kind, target, name, x, y, z, item_id: int = 0, text: str = "") -> Intention:
    return Intention(kind, target, name, item_id, (x, y, z), _dist(world, x, y), text=text)
