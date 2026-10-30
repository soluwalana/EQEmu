"""Queue, sheet, and net helpers shared by handlers. Handlers do not touch the socket."""

from __future__ import annotations

from typing import TYPE_CHECKING, Protocol, runtime_checkable

if TYPE_CHECKING:
    from eqclient3.loop import Loop
    from eqclient3.world import Bot, Mob, World

from eqclient3.log import log, write
from eqclient3.action import Action, Message
from eqclient3.actions.support import character_name, session_open
from eqclient3.bots.form import form_commands as build_form_commands
from eqclient3.data.factions import ensure_factions
from eqclient3.inventory.assign import assign as run_inventory_assign
from eqclient3.nav.zones import zone_name_of
from eqclient3.loop import ScriptedSession
from eqclient3.net.client import Client, transfer_zone
from eqclient3.structs import EQStruct, _cstring

HEAL_LINE = 0.5
SIT_LINE = 0.5
MANA_SIT = 0.25
FOLLOW_YARDS = 15.0
SPELL_DAMAGE = 231
FORAGE_SKILL = 27
FOOD_TYPE = 14
DRINK_TYPE = 15
FULL_BAR = 127


def queue_of(loop: Loop) -> list:
    queue = loop.queue
    if queue is None:
        return []
    if isinstance(queue, list):
        return queue
    return list(queue)


def is_a(action: Action, cls: type[Action], name: str) -> bool:
    return isinstance(action, cls) or type(action).__name__ == name


def find_actions(loop: Loop, cls: type[Action], name: str) -> list[Action]:
    return [action for action in queue_of(loop) if is_a(action, cls, name)]


def source_open(loop: Loop, source: str) -> bool:
    return any(action.source == source for action in queue_of(loop) if isinstance(action, Action))


def source_resolved(loop: Loop, world: World, source: str) -> bool:
    journal = loop.journal
    if journal is None:
        return False
    return journal.resolved(character_name(loop, world), source)


def enqueue_once(loop: Loop, world: World, action: Action, source: str) -> Action | None:
    """Append when this source is neither open nor already resolved."""
    if source_open(loop, source) or source_resolved(loop, world, source):
        return None
    action.source = source
    if not action.zone:
        action.zone = str(world.zone or "")
    loop.world = world
    loop.append(action)
    return action


def mark_fight(world: World, spawn_id: int) -> None:
    """Record a spawn we attacked, or that attacked us."""
    world.note_fight(spawn_id)


def has_open(loop: Loop, cls: type[Action], name: str) -> bool:
    return any((not action.complete for action in find_actions(loop, cls, name)))


def attack_for(loop: Loop, attack_cls: type[Action], spawn_id: int) -> Action | None:
    for action in find_actions(loop, attack_cls, "Attack"):
        if action.spawn_id == spawn_id:
            return action
    return None


def deliver(action: Action, payload: EQStruct) -> None:
    add = action.add_message
    if callable(add):
        add(Message(payload))


@runtime_checkable
class _ZoneTransfer(Protocol):
    def transfer_zone(self) -> None: ...


def call_transfer(loop: Loop) -> bool:
    """A closed session or a reliable hole calls net.transfer_zone. No zone request is sent."""
    session = loop.session if loop.session is not None else loop.client
    loop._transferred = True
    if isinstance(session, (Client, ScriptedSession)):
        transfer_zone(session)
        return True
    if isinstance(session, _ZoneTransfer):
        session.transfer_zone()
        return True
    return False


def cstrings(payload: bytes, offset: int) -> list[str]:
    found = []
    while offset < len(payload):
        try:
            text, offset = _cstring(payload, offset)
        except ValueError:
            break
        if text:
            found.append(text)
        else:
            break
    return found


def primary_faction(zone: str, name: str) -> int:
    try:
        book = ensure_factions()
    except Exception:
        log.error("primary faction lookup failed", exc_info=True)
        return 0
    primary = book.primary
    if not callable(primary):
        return 0
    return int(primary(zone, name) or 0)


def zone_name(world: World, zone_id: int) -> str:
    names = world.zone_names or {}
    if zone_id in names:
        return str(names[zone_id])
    return str(zone_name_of(zone_id) or zone_id or "")


def write_log(line: str) -> None:
    write(line)


def run_assign(loop: Loop, world: World) -> None:
    try:
        run_inventory_assign(loop, world)
    except TypeError:
        log.error("inventory assign failed", exc_info=True)
        return


def form_commands(world: World, loop: Loop) -> list[str]:
    bots = [(str(bot.name), bot.class_id) for bot in world.bots.roster]
    settings: dict[str, dict[str, str]] = {}
    journal = loop.journal
    if journal is not None:
        settings = journal.bot_settings(character_name(loop, world))
    return list(build_form_commands(bots, settings) or [])


def tutorial_done(loop: Loop, world: World) -> bool:
    journal = loop.journal
    if not journal:
        return False
    return bool(journal.tutorial_done(character_name(loop, world)))


def mobs_map(world: World) -> dict:
    mobs = world.mobs
    if mobs is None:
        mobs = {}
        world.mobs = mobs
    return mobs


def find_mob(world: World, spawn_id: int) -> Mob | None:
    mobs = mobs_map(world)
    if spawn_id in mobs:
        return mobs[spawn_id]
    short = spawn_id & 65535
    for mob in mobs.values():
        mob_id = mob.id
        if mob_id == spawn_id or (short and mob_id & 65535 == short):
            return mob
    return None


def mob_named(world: World, name: str) -> Mob | None:
    want = " ".join((name or "").replace("_", " ").lower().split())
    if not want:
        return None
    exact = None
    partial = None
    for mob in mobs_map(world).values():
        found = mob.spoken_name().lower()
        if found == want:
            exact = mob
            break
        if want in found and not partial:
            partial = mob
    return exact or partial


def _same_spawn(left: int, right: int) -> bool:
    if not left or not right:
        return False
    return left == right or left & 65535 == right & 65535


def is_ours(world: World, spawn_id: int, mob: Mob | None = None, loop: Loop | None = None) -> bool:
    if _same_spawn(spawn_id, world.self_id):
        return True
    if loop:
        for action in queue_of(loop):
            if type(action).__name__ == "Reclaim" and _same_spawn(spawn_id, action.corpse_id):
                return True
    if _same_spawn(spawn_id, world.pending_death or 0):
        return True
    me = character_name(loop, world).lower()
    if mob and me:
        name = (mob.name or "").lower()
        if name == me or name.startswith(f"{me}'s corpse"):
            return True
    return False


def bot_rows(world: World) -> list[Bot]:
    return [*world.bots.roster, *world.group.bots]


def bot_names(world: World) -> set[str]:
    return {bot.name.lower() for bot in bot_rows(world) if bot.name}


def has_cleric(world: World) -> bool:
    for bot in bot_rows(world):
        if bot.class_id == 2:
            return True
    grouped = set()
    group = world.group
    if group:
        grouped = {str(name).lower() for name in group.members or []}
    for mob in mobs_map(world).values():
        if (mob.name or "").lower() in grouped and mob.class_id == 2:
            return True
    return False


def our_side(world: World, spawn_id: int) -> bool:
    if is_ours(world, spawn_id):
        return True
    mob = find_mob(world, spawn_id)
    if not mob:
        return False
    return (mob.name or "").lower() in bot_names(world)


def place(mob: Mob, x: float, y: float, z: float, world: World) -> None:
    """Set the spawn point. measure writes 3D distance and heading."""
    mob.position = (float(x), float(y), float(z))
    world.measure(mob)


def active_action(loop: Loop) -> Action | None:
    if loop.active:
        return loop.active
    if loop.current:
        return loop.current
    return loop.head
