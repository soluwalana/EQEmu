"""Shared packet shapes and queue pushes. Subclasses keep their own step."""
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types import ModuleType
    from eqclient3.action import Action, Message
    from eqclient3.loop import Loop
    from eqclient3.world import Mob

from dataclasses import dataclass
from eqclient3.nav.travel import first_leg
from eqclient3.nav.zones import zone_id_of
from eqclient3.structs import (
    OP_Assist,
    OP_BecomeCorpse,
    OP_Buff,
    OP_CastSpell,
    OP_ChannelMessage,
    OP_ClientUpdate,
    OP_CorpseDrag,
    OP_Death,
    OP_DeleteItem,
    OP_DeleteSpawn,
    OP_EndLootRequest,
    OP_FindPersonRequest,
    OP_HPUpdate,
    OP_ItemPacket,
    OP_LootItem,
    OP_LootRequest,
    OP_MobHealth,
    OP_MobUpdate,
    OP_MoneyOnCorpse,
    OP_NewZone,
    OP_SimpleMessage,
    OP_SpecialMesg,
    OP_SpawnAppearance,
    OP_TargetMouse,
    OP_Taunt,
    OP_TrackTarget,
    OP_ZoneChange,
    SAY_CHANNEL,
)
from eqclient3.world import World

@dataclass
class FetchPlan:
    """How to obtain one item. Missing parts stay empty."""

    drop: object | None = None
    quest: object | None = None
    merchant: object | None = None
    ground: object | None = None
    vendor_zone: str = ""
    station_zone: str = ""
    station: tuple[float, float, float] | None = None


TOKEN = 22292
CURSOR_SLOT = 30
MELEE = 15
HAIL = 20
INTERACT = 20
LOOT_RANGE = 20
CORPSE_NEAR = 45
HOSTILE_CLOSE = 150
HOSTILE_FAR = 250
SIT = 110
TAUNT = 73
KICK = 30
BASH = 10
SILK = 54234
NORMAL_LOOT = (1, 3)
TOO_FAR = 5
SPEAK, KILL, LOOT, DELIVER = (4, 2, 3, 1)


def character_name(loop: Loop | None, world: World) -> str:
    """Journal key. loop.character wins, then the sheet."""
    if loop is not None:
        name = str(getattr(loop, 'character', None) or '')
        if name:
            return name
    who = getattr(world, 'character', None)
    if isinstance(who, str):
        return who or str(getattr(world, 'name', None) or '')
    if who is not None and getattr(who, 'name', None):
        return str(who.name)
    return str(getattr(world, 'name', None) or '')

def journal_of(loop: Loop) -> Journal | None:
    journal = loop.journal
    if journal is not None:
        return journal
    queue = loop.queue
    return queue.journal

def session_open(loop: Loop) -> bool:
    session = loop.session
    if session is None:
        return not bool(loop.closed)
    if session.closed or session.needs_rezone:
        return False
    return bool(session.open)

def yield_to(parent: Action, loop: Loop, world: World, new: Action, source: str='') -> bool:
    """Queue the next piece of work. Same-band handoff waits until the next pulse."""
    if source:
        new.source = source
    queue = loop.queue
    if queue is None:
        return False
    journal = journal_of(loop)
    who = character_name(loop, world)
    try:
        ok = queue.append(new, world, journal, who)
    except TypeError:
        queue.append(new)
        ok = True
    if ok:
        parent.yielding = True
    return bool(ok)

def queued(loop: Loop, kind: str, corpse_id: int | None = None, spawn_id: int | None = None) -> bool:
    for action in loop.queue:
        if type(action).__name__ != kind:
            continue
        if corpse_id is not None and int(getattr(action, 'corpse_id', -1) or -1) != int(corpse_id):
            continue
        if spawn_id is not None and int(getattr(action, 'spawn_id', -1) or -1) != int(spawn_id):
            continue
        return True
    return False

def send_command(loop: Loop, text: str) -> None:
    who = str(loop.character or '')
    loop.send('OP_ChannelMessage', OP_ChannelMessage('', who, channel=SAY_CHANNEL, text=text).serialize())

def message_text(message: Message) -> str:
    payload = message.payload
    if isinstance(payload, OP_SimpleMessage):
        return ' '.join(payload.texts)
    if isinstance(payload, OP_ChannelMessage):
        return str(payload.text or '')
    if isinstance(payload, OP_SpecialMesg):
        return str(payload.message or '')
    text = getattr(payload, 'text', None)
    if isinstance(text, str):
        return text
    return ''

def line_of(payload: object) -> tuple[str, str]:
    """Speaker and text for a channel or special line. A simple line has no speaker."""
    if isinstance(payload, OP_ChannelMessage):
        return (str(payload.sender or ''), str(payload.text or ''))
    if isinstance(payload, OP_SpecialMesg):
        return (str(payload.speaker or ''), str(payload.message or ''))
    if isinstance(payload, OP_SimpleMessage):
        return ('', ' '.join(payload.texts))
    return ('', '')

def payload_get(message: Message, name: str, default: object | None = None) -> object:
    payload = message.payload
    values = vars(payload)
    if name in values:
        return values[name]
    return default

def wont_sell(message: Message) -> bool:
    """Merchant refused the sale. Strings 1154-1165."""
    return 1154 <= simple_id(message) < 1166

def take_refusal(action: Action) -> bool:
    """Pop a merchant refusal if one is waiting. Other simple lines stay in the mailbox."""
    for index, message in enumerate(action.messages):
        if message.opcode == "OP_SimpleMessage" and wont_sell(message):
            action.messages.pop(index)
            return True
    return False

_SPAWN_ROWS = (
    OP_BecomeCorpse,
    OP_ClientUpdate,
    OP_Death,
    OP_DeleteSpawn,
    OP_EndLootRequest,
    OP_HPUpdate,
    OP_LootRequest,
    OP_MobHealth,
    OP_MobUpdate,
    OP_SpawnAppearance,
    OP_TargetMouse,
    OP_Taunt,
)
_ENTITY_ROWS = (OP_Assist, OP_Buff, OP_FindPersonRequest, OP_TrackTarget)

def simple_id(message: Message) -> int:
    payload = message.payload
    if isinstance(payload, OP_SimpleMessage):
        return int(payload.string_id)
    return 0

def spawn_of(message: Message) -> int:
    payload = message.payload
    if isinstance(payload, _SPAWN_ROWS):
        return int(payload.spawn_id)
    if isinstance(payload, _ENTITY_ROWS):
        return int(payload.entity_id)
    return 0

def bar_ratio(message: Message) -> float | None:
    """Fraction on an HP or mob-health packet. None when the packet has no bar."""
    payload = message.payload
    if isinstance(payload, OP_MobHealth):
        return float(payload.percent) / 100.0
    if isinstance(payload, OP_HPUpdate) and payload.max_hp:
        return float(payload.cur_hp) / float(payload.max_hp)
    return None

def item_of(message: Message) -> object | None:
    payload = message.payload
    if isinstance(payload, OP_ItemPacket):
        item = payload.item
        if not item.stack:
            item.stack = 1
        return item
    return None

def loot_response(message: Message) -> int:
    payload = message.payload
    if isinstance(payload, OP_MoneyOnCorpse):
        return int(payload.response)
    return 0

def delete_slot(message: Message) -> int:
    payload = message.payload
    if isinstance(payload, OP_DeleteItem):
        return int(payload.from_slot)
    return -1

def yards(world: World, point: tuple[float, float, float]) -> float:
    if point is None:
        return 0.0
    dx = float(point[0]) - float(world.x)
    dy = float(point[1]) - float(world.y)
    dz = float(point[2]) - float(world.z) if len(point) > 2 else 0.0
    return (dx * dx + dy * dy + dz * dz) ** 0.5

def standing_of(mob: Mob | None) -> int:
    if mob is None or mob.consider is None:
        return 0
    return int(mob.consider.standing)

def hostiles_within(items: list[Mob], yards_limit: float) -> list:
    found = []
    for item in items or []:
        mob = item.mob if hasattr(item, 'mob') else item
        dist = item.distance
        if dist is None:
            dist = mob.distance
        stand = standing_of(item if item.consider is not None else mob)
        if stand in (8, 9) and dist is not None and (float(dist) <= yards_limit):
            found.append(mob)
    return found

def walk(action: Action, loop: Loop, world: World, dest: tuple[float, float, float], mode: str) -> None:
    if not action.active_path:
        action.active_path = world.movement.plan(dest, mode)
    action.suspended = False
    world.movement.advance(loop, world, action.active_path)

def known(world: World, skill_id: int) -> bool:
    skills = world.character.abilities.skills
    if skill_id not in skills:
        return False
    return int(skills[skill_id]) > 0

def ratio(current: int, maximum: int) -> float | None:
    """Bar fraction. None when the maximum has not arrived."""
    maximum = int(maximum or 0)
    current = int(current or 0)
    if maximum <= 0:
        return None
    return current / maximum

def lowest_hurt(world: World) -> int | None:
    best = None
    best_ratio = 0.5
    mine = ratio(world.hp, world.max_hp)
    if mine is not None and mine < 0.5:
        best = int(world.self_id or 0)
        best_ratio = mine
    for bot in world.bots.roster or []:
        bot_ratio = ratio(bot.hp, bot.max_hp)
        if bot_ratio is not None and bot_ratio < best_ratio:
            best = int(bot.id or 0)
            best_ratio = bot_ratio
    return best

@dataclass
class SpellInfo:
    mana: int = 0
    recast: float = 0.0
    heal: bool = False
    cure: str | None = None
    combat: bool = False


def _spell_info(meta: object) -> SpellInfo:
    if isinstance(meta, SpellInfo):
        return meta
    if isinstance(meta, dict):
        return SpellInfo(
            mana=int(meta.get("mana") or 0),
            recast=float(meta.get("recast") or 0),
            heal=bool(meta.get("heal", False)),
            cure=meta.get("cure"),
            combat=bool(meta.get("combat", False)),
        )
    if not meta:
        return SpellInfo()
    return SpellInfo(
        mana=meta.mana,
        recast=meta.recast,
        heal=bool(meta.heal),
        cure=meta.cure,
        combat=bool(meta.combat),
    )


class GemView:

    def __init__(self, slot: int, spell_id: int, info: SpellInfo, recast_ticks: int) -> None:
        self.slot = slot
        self.spell_id = spell_id
        self.recast_ticks = recast_ticks
        self.mana = info.mana
        self.recast = info.recast
        self.heal = info.heal
        self.cure = info.cure
        self.combat = info.combat

def memorized(world: World, action: Action) -> list:
    raw = world.gems or {}
    info = world.spell_info or {}
    recast = action._gem_recast or {}
    gems = []
    pairs = raw.items() if isinstance(raw, dict) else enumerate(raw)
    for slot, value in pairs:
        if isinstance(value, int):
            spell_id = value
            meta = info.get(spell_id)
        else:
            spell_id = int(value.spell_id or 0)
            meta = value
        gems.append(GemView(slot, spell_id, _spell_info(meta), recast.get(slot, 0)))
    return gems

def arm_recast(action: Action, gem: GemView) -> None:
    ticks = int(float(gem.recast or 0) / 0.1) if gem.recast else 0
    action._gem_recast[gem.slot] = ticks
    gem.recast_ticks = ticks

def ready_gem(world: World, gem: GemView) -> bool:
    return gem.recast_ticks <= 0 and world.mana >= gem.mana

def cast_spell(loop: Loop, gem: GemView, target: int) -> None:
    loop.send('OP_CastSpell', OP_CastSpell(gem.slot, gem.spell_id, target & 65535).serialize())

def own_corpse(loop: Loop, world: World) -> int:
    """The body we would reclaim. A queued Reclaim wins. Otherwise a dead spawn that is ours."""
    last = 0
    for action in loop.queue:
        if type(action).__name__ == 'Reclaim':
            last = int(action.corpse_id)
    if last:
        return last
    # handlers.common imports assign, which imports Sell, which imports support.
    from eqclient3.handlers.common import is_ours
    for mob in world.mobs.values():
        if mob.dead and is_ours(world, int(mob.id), mob):
            return int(mob.id)
    return 0

def corpse_here(world: World, corpse_id: int) -> bool:
    return corpse_id in world.mobs

def corpse_name(world: World, corpse_id: int) -> str:
    mob = world.mobs.get(corpse_id)
    if mob is not None and mob.name:
        return str(mob.name)
    return str(world.name or 'corpse')

def corpse_where(loop: Loop, world: World, corpse_id: int, fallback: tuple[float, float, float]) -> tuple[float, float, float]:
    for action in loop.queue:
        if type(action).__name__ not in ('Reclaim', 'LootMob'):
            continue
        if int(action.corpse_id) != int(corpse_id):
            continue
        where = action.where
        return (float(where[0]), float(where[1]), float(where[2]))
    mob = world.mobs.get(corpse_id)
    if mob is not None:
        return mob.position
    return fallback

def corpse_drag(corpse: str, dragger: str) -> bytes:
    return OP_CorpseDrag(corpse, dragger).serialize()

def loot_packet(corpse_id: int, player_id: int, slot: int) -> bytes:
    return OP_LootItem(int(corpse_id), int(player_id), int(slot)).serialize()

def zone_packet(destination: str, zone_id: int, x: float, y: float, z: float) -> bytes:
    return OP_ZoneChange(destination or '', int(zone_id), float(x), float(y), float(z)).serialize()

def zone_id(name: str) -> int:
    try:
        return int(zone_id_of(name) or 0)
    except Exception:
        return 0

def empty_slots(world: World) -> int:
    explicit = world.empty_slots
    if explicit is not None:
        return int(explicit)
    return max(0, 10 - len(world.bags or {}))

def bag_slot(world: World, item_id: int) -> int | None:
    for slot, item in (world.bags or {}).items():
        if int(item) == int(item_id):
            return int(slot)
    return None

def merchant_offer(action: Action, item_id: int) -> tuple[object, ...] | None:
    """Slot and price for item_id on the open Trade or Sell window."""
    for slot, row in action.slots.items():
        listed, price = row
        if int(listed) == int(item_id):
            return (int(slot), int(price))
    return None

def has_soulbind(loop: Loop, world: World) -> bool:
    journal = journal_of(loop)
    who = character_name(loop, world)
    if journal is not None and who:
        return bool(journal.soulbind_zone(who))
    return bool(world.soulbound)

def soulbinder(world: World) -> object | None:
    binder = world.soulbinder
    if binder is not None:
        return binder
    from eqclient3.camps import nearest_soulbinder
    return nearest_soulbinder(world.zone or '')

def clear_source(loop: Loop, world: World, source: str) -> None:
    journal = journal_of(loop)
    who = character_name(loop, world)
    if journal is None or not who or not source:
        return
    journal.clear_source(who, source)

def mark_tutorial(loop: Loop, world: World) -> None:
    journal = journal_of(loop)
    who = character_name(loop, world)
    if journal is None or not who:
        return
    journal.mark_tutorial_done(who)

def task_activities(world: World) -> list:
    book = world.task_book or world.tasks
    if book is None:
        return []
    return list(book.activities or [])

def new_zone_name(message: Message, world: World) -> str:
    if message is None:
        return str(world.zone or '')
    payload = message.payload
    if isinstance(payload, OP_NewZone) and payload.short_name:
        return payload.short_name
    return str(world.zone or '')

def is_silk(action: Action) -> bool:
    if type(action).__name__ != 'Fetch':
        return False
    if int(action.item_id or 0) == SILK:
        return True
    text = f'{action.task_text} {action.name}'.lower()
    return 'silk' in text

def silk_fetch_queued(loop: Loop) -> bool:
    return any((action.durable and is_silk(action) for action in loop.queue))

def buff_faded(message: Message) -> bool:
    """The buff packet says the effect left, or its counters hit zero."""
    if payload_get(message, 'gone') or payload_get(message, 'fade'):
        return True
    counters = payload_get(message, 'counters')
    if counters is not None and int(counters) <= 0:
        return True
    payload = message.payload
    if isinstance(payload, OP_Buff) and (payload.fade or payload.buff.counters <= 0):
        return True
    return False

def effect_gone(message: Message, world: World, effect: str) -> bool:
    if buff_faded(message):
        return True
    afflictions = world.afflictions
    if afflictions is None:
        return False
    return not any((_afflicted(row, effect) for row in afflictions))

def _afflicted(row: object, effect: str) -> bool:
    if isinstance(row, tuple) and len(row) >= 2:
        return str(row[1]) == str(effect)
    return str(row.effect) == str(effect)

def afflictions(world: World) -> list:
    rows = world.afflictions
    if rows is not None:
        return list(rows)
    found = []
    book = world.buffs or {}
    rows = book.values() if isinstance(book, dict) else book
    for buff in rows:
        effect = buff.effect
        if effect in ('disease', 'poison', 'curse'):
            found.append(buff)
    return found

def cures(gem: GemView, effect: str) -> bool:
    cure = gem.cure
    if cure is None:
        return False
    if isinstance(cure, (set, list, tuple)):
        return effect in cure
    return str(cure) == str(effect)

def worn_map(loop: Loop, world: World, bot: str) -> dict:
    journal = journal_of(loop)
    who = character_name(loop, world)
    if journal is not None and who:
        return journal.worn(who, bot)
    return {}

def set_worn(loop: Loop, world: World, bot: str, slot: int, item_id: int) -> None:
    journal = journal_of(loop)
    who = character_name(loop, world)
    if journal is not None and who:
        journal.set_worn(who, bot, int(slot), int(item_id))

def at_water(world: World) -> bool:
    if world.at_water:
        return True
    water = world.water_map
    if water is None:
        return False
    contains = water.contains
    if contains is None:
        return False
    try:
        return bool(contains(world.x, world.y, world.z))
    except Exception:
        return False

def fetch_plan(world: World, item_id: int) -> FetchPlan:
    plans = world.plans or {}
    plan = plans.get(int(item_id))
    if isinstance(plan, FetchPlan):
        return plan
    fields = vars(plan) if plan is not None else {}
    return FetchPlan(
        drop=fields.get("drop"),
        quest=fields.get("quest"),
        merchant=fields.get("merchant"),
        ground=fields.get("ground"),
        vendor_zone=str(fields.get("vendor_zone") or ""),
        station_zone=str(fields.get("station_zone") or ""),
        station=fields.get("station"),
    )

def next_zoneline(world: World, destination: str) -> tuple[float, float, float] | None:
    point = world.zoneline
    if point is not None:
        return point
    graph = world.zone_graph
    if graph is None:
        return None
    leg = first_leg(graph, world.zone, destination)
    if leg is None:
        return None
    transit = None
    at = graph.transit_at
    if callable(at):
        transit = at(leg.zone, leg.door_id)
    if transit is None:
        return None
    return (float(transit.x), float(transit.y), float(transit.z))

def reclaim_if_ours(parent: Action, loop: Loop, world: World, *targets: int) -> bool:
    """Consume string 251 for one of targets and queue Reclaim. True when a match was handled."""
    matched = False
    wanted = {int(target) for target in targets if target}
    while parent.consume('OP_SimpleMessage', lambda message: simple_id(message) == 251):
        corpse = own_corpse(loop, world)
        if not corpse or int(corpse) not in wanted:
            continue
        if not queued(loop, 'Reclaim', corpse_id=corpse):
            where = corpse_where(loop, world, corpse, (world.x, world.y, world.z))
            from eqclient3.actions.reclaim import Reclaim
            yield_to(parent, loop, world, Reclaim(corpse, where), f'reclaim:{corpse}')
        matched = True
    return matched

def ingest_corpse_mail(action: Action, *, default_stack: bool = False) -> None:
    """Drain corpse item packets and the money line into action.slots."""
    while True:
        item = action.consume('OP_ItemPacket')
        if item is None:
            break
        parsed = item_of(item)
        item_id = int(getattr(parsed, 'item_id', 0) or 0) if parsed is not None else 0
        if parsed is None or item_id == TOKEN:
            continue
        if default_stack and not getattr(parsed, 'stack', 0):
            parsed.stack = 1
        action.slots.append(parsed)
    money = action.consume('OP_MoneyOnCorpse')
    if money is None:
        return
    response = loot_response(money)
    if response in NORMAL_LOOT:
        action.opened = True
        action.unwait('LOOT')
        return
    if response == TOO_FAR:
        action.requested = False
        action.opened = False
        action.unwait('LOOT')
