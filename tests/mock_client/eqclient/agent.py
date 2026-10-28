"""Zone-agnostic quest loop. The same steps run in the mine and in whatever zone comes next."""

from __future__ import annotations

import math
import os
import re
import struct
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path

from eqclient.client import Client, connect
from eqclient.session import SessionError
from eqclient.explore import (
    AreaSearch,
    Survey,
    bearing,
    is_stair,
    next_length,
    other_step,
    refused,
    _step_height,
    signature_of,
)
from eqclient.items import (
    BACKPACK_ITEM,
    BAG_SLOT_COUNT,
    CURSOR,
    GENERAL,
    PRIMARY,
    SECONDARY,
    TRADE,
    TRAIN_SKILLS,
    WORN,
    WORN_NAMES,
    Inventory,
    bags_buyable,
    bags_short,
    content_slot,
    held_stats_tip,
    is_wearable_gear,
    bot_usable_loot_slots,
    can_receive,
    equip_move,
    fits,
    coin_loot_slots,
    has_loot_room,
    is_vendor_trash,
    loot_picks,
    missing_entries,
    server_slot,
    stack_totals,
    stow_move,
    trash_slots,
    upgrade_loot_slots,
    _upgrade_slot,
)
from eqclient.gear import BOT_RACE, gear_tier, seed_gear_goals
from eqclient.journal import Journal
from eqclient.maps import ZoneMap, load_map
from eqclient.navmesh import NavMesh, load_nav
from eqclient.opcodes import require
from eqclient.water import WaterMap, load_water, swim_height
from eqclient.packets import (
    client_position,
    eq_heading,
    find_destination,
    find_path,
    find_person_request,
    guide_from,
    movement_history,
    popup_message,
    popup_response,
    saylink_words,
)
from eqclient.builds import build_for, held_gear_value, next_train
from eqclient.cache_builders.faction_list import DEFAULT_FACTION_LIST, read_faction_list
from eqclient.conduct import (
    DEFAULT_RECIPES,
    ability_for,
    ability_reuse,
    bar_needed,
    craft_for,
    farm_target,
    order_of,
    read_recipes,
    role_of,
)
from eqclient.packets import (
    cast_packet,
    channel_number,
    channel_sender,
    consume_packet,
    group_follow,
    group_invite,
    memorize_packet,
    profile_spells,
    who_request,
)
from eqclient.protect import is_protected, protected_ids
from eqclient.drops import read_drops
from eqclient.factions import read_factions
from eqclient.merchants import ensure_merchants, _norm_name as _merchant_norm
from eqclient.item_stats import ensure_items
from eqclient.cache_builders.bot_spells import ensure_bot_spells
from eqclient.spells import MEMORIZE, SCRIBE, apply_spell_goals, gem_for, open_book_slot, read_spells
from eqclient.tactics import fight_tactic, may_melee, opener
from eqclient.plan import (
    SAFE_RANGE,
    Intention,
    Lesson,
    _is_mine_mob,
    _mine_target,
    _names_match,
    _script,
    _task_needs,
    guide,
    lesson_from,
    recover,
)
from eqclient.campaign import (
    FISH_BAIT,
    FISH_BAIT_WANT,
    FISH_POLE,
    ITEM_FISHING_BAIT,
    ITEM_FISHING_POLE,
    Campaign,
    CampaignStep,
    stack_faction_ids,
)
from eqclient.camps import camp_for_level, nearest_soulbinder, needs_level
from eqclient.epics import default_epic20_item
from eqclient.party import PartyBuilder
from eqclient.travel import DEFAULT_ZONE_GRAPH, first_leg, read_zone_graph
from eqclient.quests import ZoneQuests, load_zone, read_graph, reply_order
from eqclient.sheet import Character, build
from eqclient.tasks import KILL, TaskBook
from eqclient.world import ZoneModel, blocks_step, doors_along

# Strides per ClientUpdate. Animation is SpeedRun (~28), not a 1/2 walk/run flag.
# 30% slower than classic 20/28 so bots can close after an early threat spot.
STEP = 14.0
STEP_LOS = 19.6  # Full-run stride for Find / LOS chase (was 28).
STEP_WALK = STEP / 3.0  # Near-corpse: 1/3 speed + walk anim (avoids LoS misses).
STEP_CREEP = STEP / 6.0  # Reclaim melee approach — bots engage while we ease in.
_RECLAIM_WALK_RANGE = 500.0  # Within this of a corpse, walk at STEP_WALK.
_RECLAIM_CREEP_RANGE = 45.0  # Within this of a reclaim foe, creep (slower than walk).
ANIM_STAND = 0
ANIM_WALK = 12
ANIM_RUN = 20  # Match slowed stride (was 28).
TICK = 0.10
# Melee / interact distances. Fight must match task_kill — a wider fight range
# starts OP_AutoAttack and bot ^attack while still walking in, so bots pull first.
_MELEE_RANGE = 5.0
# Beyond this, a clear outdoor ray is not "in sight" — Find to the spawn instead.
_SIGHT_RANGE = 225.0
# Corpse-run caution: fight LOS hostiles within this before walking on (one at a time).
# Override with EQEMU_THREAT_RANGE (yards). Larger = see aggro sooner, wait on bots.
_RECLAIM_CAUTION = float(os.environ.get("EQEMU_THREAT_RANGE", "200") or 200)
# Near the body, also clear hostiles clustered on the corpse pad.
_RECLAIM_CORPSE_CLEAR = 55.0
# Abandon a leftover "finish" swing once the live mob is this far (stale after reclaim).
_FINISH_MAX_DIST = 200.0
# Bot-first pull: send ^attack near threat-spot range so the raid engages first.
_BOT_SEND_RANGE = 150.0
_BOT_HOLD_RANGE = 70.0
# Soft reissue window while waiting for first bot hit (we still hold until bots_on).
_BOT_ENGAGE_WAIT = 20.0
# Grind cycle: scan LOS → chase; else walk spawn ≥ this long → scan again.
# Far pads need a longer commit so we don't re-Find / retarget every few seconds.
_GRIND_WALK_SECS = 12.0
_GRIND_WALK_SECS_FAR = 30.0
_GRIND_WALK_FAR_YD = 400.0
_GRIND_PAD_CELL = 25.0  # yards — same cell = same spawn pad
_GRIND_PAD_REACH = 12.0  # close enough to count as standing on the pad
_GRIND_PAD_MEMORY = 5  # do not revisit these many pads in a row
_ACT_RANGE = {
    "task_kill": 4.0,
    "fight": 4.0,
    "loot": 15.0,
    "reclaim": 15.0,
    "train": 15.0,
    "shop": 20.0,
    "task_talk": 25.0,
    "hail": 25.0,
    "talk": 25.0,
    "soulbind": 25.0,
    "hand_in": 8.0,
    "fetch": 8.0,
    "search": 8.0,
}
_MERCHANT_WORDS = ("merchant", "vendor", "shopkeeper", "shop ")


@dataclass
class Score:
    activities: int = 0
    fetched: int = 0
    hails: int = 0
    keywords: int = 0
    doors: int = 0
    kills: int = 0
    zone: str = ""
    zones: list[str] = field(default_factory=list)

    def line(self) -> str:
        return (
            f"score activities={self.activities} fetched={self.fetched} hails={self.hails} "
            f"keywords={self.keywords} doors={self.doors} kills={self.kills} zone={self.zone}"
        )


# Titanium world tradeskill container. Contents sit at WORLD_CONTENTS.
WORLD_COMBINE = 1000
WORLD_CONTENTS = 4000


def station_words(bag_type: int) -> tuple[str, ...]:
    """Name fragments for a world forge, oven, kiln, or pottery wheel."""
    from eqclient.catalog import _BAG_TYPES

    label = (_BAG_TYPES.get(int(bag_type)) or "").lower()
    return tuple(word for word in label.split() if len(word) > 3)


def pick_station(bag_type: int, doors, grounds, here):
    """Nearest door or ground object whose name matches the station."""
    words = station_words(bag_type)
    if not words:
        return None
    best = None
    best_d = 1e18
    for door in doors:
        if not any(word in door.name.lower() for word in words):
            continue
        dist = (here[0] - door.x) ** 2 + (here[1] - door.y) ** 2
        if dist < best_d:
            best, best_d = ("door", door), dist
    for drop in grounds:
        if not any(word in drop.name.lower() for word in words):
            continue
        dist = (here[0] - drop.x) ** 2 + (here[1] - drop.y) ** 2
        if dist < best_d:
            best, best_d = ("ground", drop), dist
    return best


def _turn_ids(text: str, item_id: int) -> list[int]:
    """Items in a hand-in. `work|1+2+3` keeps the keyword in front of the ids."""
    body = text.split("|", 1)[-1] if "|" in (text or "") else (text or "")
    ids = [int(part) for part in body.replace(" ", "").split("+") if part.isdigit()]
    if ids:
        return ids
    return [item_id] if item_id else []


@dataclass(frozen=True)
class AgentSpec:
    """One character. A second agent is a second spec, not a change to the environment."""

    character: str
    user: str | None = None
    password: str | None = None
    race: int = 1
    class_id: int = 1
    gender: int = 0
    deity: int | None = None
    start_zone: int | None = None
    bot_prefix: str | None = None
    journal_path: str | None = None
    form_raid: bool = False
    form_group: bool = True
    goal_item: int | None = None

    def sheet(self) -> Character:
        return build(self.race, self.class_id, self.gender, self.deity, self.start_zone)

    @classmethod
    def from_environ(cls) -> AgentSpec:
        deity = os.environ.get("EQEMU_DEITY")
        start = os.environ.get("EQEMU_START_ZONE")
        goal_raw = os.environ.get("EQEMU_GOAL_ITEM")
        form_raid = os.environ.get("EQEMU_FORM_RAID", "").lower() in {"1", "true", "yes"}
        form_group = os.environ.get("EQEMU_FORM_GROUP", "1").lower() not in {"0", "false", "no"}
        character = os.environ.get("EQEMU_CHAR", "Mockone")
        # New agents that have not cleared Gloomingdeep start in the mines (189).
        start_zone = int(start) if start else None
        if start_zone is None:
            journal_path = os.environ.get("EQEMU_JOURNAL", str(Path.home() / ".eqclient" / "journal.sqlite"))
            try:
                from eqclient.journal import Journal

                if not Journal(journal_path).tutorial_done(character):
                    start_zone = 189  # tutorialb
            except Exception:
                start_zone = 189
        return cls(
            character,
            os.environ.get("EQEMU_USER"),
            os.environ.get("EQEMU_PASS"),
            int(os.environ.get("EQEMU_RACE", "1")),
            int(os.environ.get("EQEMU_CLASS", "1")),
            int(os.environ.get("EQEMU_GENDER", "0")),
            int(deity) if deity else None,
            start_zone,
            os.environ.get("EQEMU_BOT_PREFIX"),
            os.environ.get("EQEMU_JOURNAL"),
            form_raid,
            form_group and not form_raid,
            int(goal_raw) if goal_raw else None,
        )


class Agent:
    def __init__(
        self,
        client: Client,
        form_raid: bool = False,
        form_group: bool = True,
        goal_item: int | None = None,
    ) -> None:
        self.client = client
        self.form_raid = form_raid
        self.form_group = form_group and not form_raid
        # Remember preferred bot party mode so a PC invite can pause and restore it.
        self._want_form_raid = self.form_raid
        self._want_form_group = self.form_group
        self.model = ZoneModel(client._character)
        self.tasks = TaskBook()
        self.inventory = Inventory()
        self.party = PartyBuilder(
            client._character,
            getattr(client, "_bot_prefix", None),
            raid=form_raid,
        )
        self.quests = ZoneQuests("")
        self.nav: NavMesh | None = None
        self.zone_map: ZoneMap | None = None
        self.water: WaterMap | None = None
        self.score = Score()
        self.path: list[tuple[float, float, float]] = []
        self.survey = Survey()
        self.search = AreaSearch()
        self._pending: tuple[tuple[float, float, float], tuple[float, float, float]] | None = None
        self.refused_dirs: set[int] = set()
        self.step_length = STEP
        self.turn_offset = 0.0
        self._swimming = False
        self._breath_at = 0.0
        self._surfaced_warn = False
        self._fish_stashed: int = 0  # primary weapon item_id removed for the pole
        self._fish_facing = False
        self._answered: set[tuple[str, tuple]] = set()
        self.lesson: Lesson | None = None
        self._listed_tasks = False
        self._focus = 0
        self._pursuit = 0
        self._too_far = False
        self._swing_id = 0
        self._swing_at = 0.0
        self._bot_order_at = 0.0
        self._bot_summon_at = 0.0
        self._bot_respawn_at = 0.0  # cooldown for rest-time ^botspawn of downed bots
        self._cleric_respawn_at = 0.0  # tighter cooldown for dead clerics
        self._bot_attack_for = 0  # spawn_id we already ordered bots to attack (log once)
        self._bot_attack_fail_for = 0
        self._bot_attack_fail_at = 0.0
        self._threat_bot_id = 0  # bot entity we assist to lock their target
        self._assist_reply = 0  # entity id from last OP_Assist response
        self._locking_attack_target = False  # block cure/heal from retargeting self mid-^attack
        self._bot_pull_at = 0.0  # when ^attack was first sent for current swing
        self._bot_pull_logged = 0  # spawn_id we logged "pull hold" for
        self._progress_at = 0.0
        self._landed = False
        self._swing_hp = -1
        self._reacquire_i = 0
        self._reacquire_at = 0.0
        self._hold_melee_until = 0.0  # after Find/scan, try swings before backing up again
        self._hp_at_swing = 0
        self._party_hp: dict[int, int] = {}  # spawn_id → last hp% from group MobHealth
        self._faction_focus = ""
        self._sitting = False
        self._sat_at = 0.0
        self._skills: dict[int, int] = {}
        self._languages: dict[int, int] = {}  # language_id → skill (from OP_SkillUpdate 100+)
        self._practice_i = 0
        self._sneaking = False
        self._sneak_on_at = 0.0
        self._bind_at = 0.0
        self._lang_at = 0.0
        self._orders: list = []
        self._leader = ""
        self._grouped = False
        self._group_loot_set = False  # autosplit off — agent keeps 100% coin/loot
        self._gems: dict[str, tuple[int, int]] = {}
        self._rooted = False
        self._snared = False
        self._slowed = False
        self._known_names: set[str] = set()
        self._trainer_open = False
        self._threat = 0
        self._bot_threats: set[int] = set()  # mobs that hit (or are hit by) bots — clear before walk
        self._reclaim_held_for = 0  # spawn_id we already logged reclaim→clear for
        self._reclaim_rest_logged = ""  # last reclaim→rest why printed (dedupe spam)
        self._corpse_drag_at = 0.0  # last OP_CorpseDrag attempt
        self._corpse_drag_for = 0  # spawn_id we last dragged
        self._loot_too_far_at = 0.0  # throttle TooFar (response=5) retries
        self._cleric_mana: float | None = None  # 0..1 from ^botreport; None = unknown
        self._cleric_medding = False  # med until ~90% after mana dropped ≤25%
        self._bot_report_at = 0.0
        self._gave_up: dict[int, float] = {}  # spawn_id -> monotonic expiry
        self.guide: list[tuple[float, float, float]] = []
        self._guide_for = 0
        self._find_for = 0
        self._find_at = 0.0
        self._find_empty: set[int] = set()
        self._find_arrived: set[int] = set()  # Find path walked to the end — mesh the last yards
        self._roam: tuple[float, float, float] | None = None
        self._roam_name = ""
        self._roam_at = 0.0
        self.skipped_ground: set[int] = set()
        self.skipped_corpses: set[int] = set()
        self.said: set[tuple[str, str]] = set()
        self.handed: set[tuple[str, str]] = set()
        self.attacked: set[int] = set()
        self._killed: set[int] = set()
        self._ability_ready: dict[str, float] = {}
        self._ability_last = ""
        self._stuck_target = 0
        self._stuck_pos: tuple[float, float, float] | None = None
        self._stuck_at = 0.0
        self._stuck_ticks = 0
        self._stuck_check_at = 0.0
        # Explore / Find walks: same no-move clock, but never abandon the Find target.
        self._walk_stuck_key = ""
        self._walk_stuck_pos: tuple[float, float, float] | None = None
        self._walk_stuck_at = 0.0
        self._walk_stuck_ticks = 0
        self._chase_best_dist: dict[int, float] = {}  # spawn_id → best dist this chase
        self._grind_to = 0  # campaign level gate
        self._grind_label = ""  # full why= label from the active campaign grind
        self._grind_walk_until = 0.0  # commit to spawn-walk until this time, then rescan
        self._grind_mode = ""  # "chase" | "walk"
        self._grind_pads: list[tuple[int, int]] = []  # recent pad cells (max 5)
        self._stack_faction_ids: set[int] = set()
        self._stack_faction_key: tuple[int, ...] = ()
        journal_path = getattr(client, "_journal_path", None) or os.environ.get(
            "EQEMU_JOURNAL", str(Path.home() / ".eqclient" / "journal.sqlite")
        )
        self.journal = Journal(journal_path)
        graph_path = os.environ.get("EQEMU_GRAPH", str(Path.home() / ".eqclient" / "quest_graph.jsonl"))
        self.graph = read_graph(graph_path) if Path(graph_path).is_file() else None
        spell_path = os.environ.get("EQEMU_SPELLS") or str(Path(graph_path).with_name("spells.jsonl"))
        self.spells = read_spells(spell_path)
        bot_spell_path = os.environ.get("EQEMU_BOT_SPELLS") or str(Path(graph_path).with_name("bot_spells.jsonl"))
        self.bot_spells = ensure_bot_spells(bot_spell_path)
        if self.bot_spells.rows:
            print(f"bot_spells {len(self.bot_spells.rows)}", flush=True)
        merchant_path = os.environ.get("EQEMU_MERCHANTS") or str(Path(graph_path).with_name("merchants.jsonl"))
        self.merchants = ensure_merchants(merchant_path)
        if self.merchants.by_npc:
            print(f"merchants {len(self.merchants.by_npc)}", flush=True)
        item_path = os.environ.get("EQEMU_ITEMS") or str(Path(graph_path).with_name("items.jsonl"))
        self.item_stats = ensure_items(item_path)
        if self.item_stats.by_id:
            print(f"items {len(self.item_stats.by_id)}", flush=True)
        print(
            f"combat threat={_RECLAIM_CAUTION:.0f}yd sight={_SIGHT_RANGE:.0f}yd "
            f"step={STEP:.1f}/{STEP_LOS:.1f} bot_send={_BOT_SEND_RANGE:.0f}yd "
            f"(EQEMU_THREAT_RANGE)",
            flush=True,
        )
        recipe_path = os.environ.get("EQEMU_RECIPES") or str(Path(graph_path).with_name("recipes.jsonl"))
        self.recipes = read_recipes(recipe_path)
        drop_path = os.environ.get("EQEMU_DROPS") or str(Path(graph_path).with_name("drops.jsonl"))
        self.drops = read_drops(drop_path)
        faction_path = os.environ.get("EQEMU_FACTIONS") or str(Path(graph_path).with_name("faction_hits.jsonl"))
        self.factions = read_factions(faction_path)
        self._book_known = False
        # Zone connectivity (door coords + dest + key/lockpick/expansion gates).
        zone_path = os.environ.get("EQEMU_ZONE_GRAPH", DEFAULT_ZONE_GRAPH)
        self.zone_graph = read_zone_graph(zone_path)
        self.zone_graph.remember_all()
        if self.graph is not None:
            self.zone_graph.apply_to_quest_graph(self.graph)
        sheet = getattr(client, "_sheet", None)
        if sheet is not None:
            self.model.class_id = sheet.class_id
            self.model.race_id = sheet.race
        played = getattr(client, "_played", None)
        if played is not None:
            self.model.apply_played(played)
        self.campaign = Campaign(self.model.class_id or 1, self.model.race_id or 0)
        self._opcodes = {name: require(client._opcodes, name) for name in _WATCHED if name in client._opcodes}
        self._by_opcode = {value: name for name, value in self._opcodes.items()}
        self._messages = 0
        self._trade_with = 0
        self._seen_done: dict[tuple[int, int], int] = {}
        self._retired_skills: set[int] = set()
        self._skill_index = 0
        self._trained = False
        self._loot_open = 0
        self._loot_spawn_id = 0  # corpse currently being looted (for coin logs)
        self._loot_coin_copper = 0  # coin reported on this open (MoneyOnCorpse)
        self._pending_rezz: bytes | None = None  # last OP_RezzRequest payload
        self._pull_cleared = True
        self._deliver_to = ""
        self._deliver_item = 0
        self._deliver_count = 0
        self._deliver_told = False
        self._pc_party = False  # grouped with a real PC; do not rebuild bot party
        self._awaiting_pc_join = False  # True after invite/accept until a PC lands in group
        self._awaiting_pc_since = 0.0
        self._camped_for_pc = ""  # bot name camped to free a seat for a PC
        self._heal_rotation_set = False  # cleric healrotation create/save/reload/start done
        self._heal_rotation_at = 0.0  # last create attempt (retry backoff)
        self._caster_nukes_set = False  # spellholds off + nuke settings for casters
        self._emergency_heal_at = 0.0  # last ^cast regularheals while critically low
        self._cure_spells: dict[int, int] = {}  # spell_id → counters (disease/poison/curse)
        self._cure_at = 0.0  # last ^cast cures / groupcures
        self._gear_tier_seeded = ""  # last beginner/mid/late band we pushed kits for
        self._bot_spell_settings_done: set[tuple[str, int]] = set()  # (bot, spell_id) already added
        self._bot_spell_stack_pruned = False  # one-shot drop of old bot-scroll campaign junk
        self._bot_given: set[tuple[str, int]] = set()  # (bot_name, item_id) already handed off
        # Local bot equipment: bot_name → {worn_slot → item_id}. Missing slot = empty.
        # Listed once via ^inventorylist; updated locally on inventorygive (no re-ask).
        self._bot_worn: dict[str, dict[int, int]] = {}
        self._bot_worn_listed: set[str] = set()
        self._gear_settle_gave = False  # inventorygive succeeded this settle pass
        self._gear_reclaim_stall = 0  # settle attempts while deferring reclaim
        self._gear_reclaim_skip = False  # True after max stall — do not block corpses again
        self._soulbind_at = 0.0  # last "bind my soul" attempt
        self._pending_inviter = ""
        # Journal stack first so a PC farm assign survives restarts and is not wiped by epic default.
        saved, saved_counts = self.journal.load_goal_stack(self.model.character)
        if saved:
            self.campaign.load_stack(saved, saved_counts)
        deliver_to, deliver_item, deliver_count = self.journal.load_goal_deliver(self.model.character)
        if deliver_to and deliver_item:
            self._deliver_to = deliver_to
            self._deliver_item = deliver_item
            self._deliver_count = deliver_count
            self._known_names.add(_key(deliver_to))
        env_goal_raw = os.environ.get("EQEMU_GOAL_ITEM")
        root_goal = goal_item
        if root_goal is None:
            root_goal = int(env_goal_raw) if env_goal_raw else default_epic20_item(self.model.class_id or 0)
        self._tutorial_done = self.journal.tutorial_done(self.model.character)
        # Journal empty → seed epic/env as the sole root. Otherwise keep saved stack;
        # an explicit constructor/env goal is assigned on top without erasing prior work.
        # Campaign goals stay stored while the tutorial is unfinished; the planner defers them.
        if not saved and root_goal:
            self.campaign.set_goal(root_goal, graph=self.graph)
            self._persist_goals()
        elif saved and root_goal and root_goal != self.campaign.peek():
            self.campaign.assign_goal(root_goal, graph=self.graph)
            self._persist_goals()
        if not self._tutorial_done:
            print("tutorial: pending (campaign deferred)", flush=True)
        elif self.campaign.peek():
            print(f"campaign stack={list(self.campaign.stack)}", flush=True)

    def attach(self) -> None:
        self.client.listen(self.on_packet)

    def on_packet(self, opcode: int, payload: bytes) -> None:
        name = self._by_opcode.get(opcode)
        if name == "OP_NewZone":
            self.model.on_new_zone(payload)
            if self.model.zone and self.model.zone_id:
                self.journal.remember_zone(self.model.zone, self.model.zone_id)
            self.tasks.set_here(self.model.zone, self.model.zone_id)
            self._enter_zone()
        elif name == "OP_ZoneSpawns" or name == "OP_NewSpawn":
            self.model.on_spawns(payload)
        elif name == "OP_DeleteSpawn":
            spawn_id = self.model.on_delete_spawn(payload)
            if spawn_id and (spawn_id in self.attacked or spawn_id == self._swing_id):
                self._retire(spawn_id)
                self.attacked.discard(spawn_id)
        elif name == "OP_SpawnDoor":
            self.model.on_doors(payload)
        elif name == "OP_GroundSpawn":
            self.model.on_ground(payload)
        elif name == "OP_ClickObject":
            self.model.on_click_object(payload)
        elif name == "OP_ClientUpdate":
            self.model.on_client_update(payload)
        elif name == "OP_RequestClientZoneChange":
            # Confirm only — cross-zone success is OP_ZoneChange, which reconnects.
            self._confirm_zone(payload)
        elif name == "OP_ZoneChange":
            if self.model.on_zone_change(payload):
                dest = self.model.zone_id
                print(f"zone transfer id={dest}", flush=True)
                try:
                    self.client.transfer_zone()
                except Exception as exc:
                    print(f"zone transfer failed: {exc}", flush=True)
                    return
                # OP_NewZone during zone_in already ran _enter_zone and set the short name.
                if self.model.zone and self.model.zone_id:
                    self.journal.remember_zone(self.model.zone, self.model.zone_id)
                self.tasks.set_here(self.model.zone, self.model.zone_id)
                self.model.changed_zone = False
        elif name == "OP_Death":
            if self.model.on_death(payload):
                spot = self.model.own_corpse_at or self.model.position
                zone = self.model.own_corpse_zone or self.model.zone or "?"
                x, y, z = spot
                print(f"death zone={zone} pos=({x:.0f}, {y:.0f}, {z:.0f})", flush=True)
                self.journal.remember_corpse(self.model.character, zone, *spot)
                pending = self.journal.outstanding_corpses(self.model.character)
                self.inventory.clear()
                # Drop combat so swing/pursuit cannot override corpse reclaim.
                self._swing_id = 0
                self._pursuit = 0
                self._threat = 0
                self._focus = 0
                self._bot_threats.clear()
                self.attacked.clear()
                self._killed.clear()
                # Server moves purse onto the corpse — stop counting it as carried.
                if self.model.coin_known:
                    print(f"death purse was {self.model.coin_line()} → on corpse", flush=True)
                    self.model.set_coin(0, 0, 0, 0)
                print(
                    f"reclaim pending {pending} corpse(s); latest at ({x:.0f}, {y:.0f}, {z:.0f})",
                    flush=True,
                )
        elif name == "OP_PlayerProfile":
            from eqclient.packets import player_profile

            played = player_profile(payload)
            if played is not None:
                self.model.apply_played(played)
            if self.model.coin_known:
                print(self.model.coin_line(), flush=True)
            book, gems = profile_spells(payload)
            self.inventory.book.update(book)
            self.inventory.scribed.update(book.values())
            self.inventory.memorized.update(gems)
            for spell_id in gems.values():
                self._bind_gem(spell_id)
            self._book_known = True
        elif name == "OP_LevelUpdate":
            if len(payload) >= 8:
                level, old = struct.unpack_from("<II", payload)
                self.model.grant_levels(level, old)
                # Titanium LevelUpdate.exp is the same 0–330 bar (often 0 after a ding).
                if len(payload) >= 12:
                    self.model.exp_bar = max(0, min(330, struct.unpack_from("<I", payload, 8)[0]))
                print(self._xp_line(), flush=True)
                # Companion spellsettings recheck is journal-gated in _seek_bot_spells (runs each tick after ding).
        elif name == "OP_MoneyUpdate" and len(payload) >= 16:
            before = self.model.coin if self.model.coin_known else None
            self.model.set_coin(*struct.unpack_from("<IIII", payload))
            if before != self.model.coin:
                print(self.model.coin_line(), flush=True)
        elif name in ("OP_GroupInvite", "OP_GroupInvite2") and len(payload) >= 128:
            # Server invite to us: invitee at 0, inviter at 64.
            invitee = payload[:64].split(b"\x00", 1)[0].decode("latin1", "replace")
            inviter = payload[64:128].split(b"\x00", 1)[0].decode("latin1", "replace")
            me = (self.model.character or "").lower()
            if invitee.lower() == me or not invitee:
                self._pending_inviter = inviter
                print(f"party invite from {inviter}", flush=True)
        elif name in ("OP_GroupUpdate", "OP_RaidUpdate", "OP_RaidJoin") and len(payload) >= 4:
            action = struct.unpack_from("<I", payload)[0]
            names = [
                part.decode("latin1", "replace")
                for part in payload[4:].split(b"\x00")
                if 1 < len(part) < 40 and all(32 <= byte < 127 for byte in part)
            ][:8]
            print(f"party act={action} {names}", flush=True)
            self._note_group_update(action, names)
        elif name == "OP_ExpUpdate" and len(payload) >= 4:
            # Titanium: current bar ratio 0–330 for this level (not XP gained).
            bar = max(0, min(330, struct.unpack_from("<I", payload)[0]))
            self.model.exp_bar = bar
            print(self._xp_line(), flush=True)
        elif name == "OP_SkillUpdate" and len(payload) >= 8:
            skill_id, value = struct.unpack_from("<II", payload)
            # Languages are reported as skillId = 100 + language_id.
            if skill_id >= 100:
                self._languages[skill_id - 100] = value
            else:
                self._skills[skill_id] = value
            self._trained = True
        elif name == "OP_Stamina" and len(payload) >= 8:
            self.model.food, self.model.water = struct.unpack_from("<II", payload)
        elif name == "OP_ChannelMessage" and len(payload) >= 136:
            self._on_channel(payload)
        elif name == "OP_TradeRequest" and len(payload) >= 4:
            other = struct.unpack_from("<I", payload)[0]
            spawn = self.model.spawns.get(other)
            if spawn is not None and spawn.npc == 0 and _key(spawn.name) in self._known_names:
                self.client.send("OP_TradeRequestAck", payload[:8])
            elif spawn is not None and spawn.npc == 0:
                self.client.send("OP_CancelTrade", b"")
        elif name == "OP_RezzRequest" and len(payload) >= 4:
            # Echo this buffer back on OP_RezzAnswer with action=ACCEPT (last u32).
            self._pending_rezz = bytes(payload)
            print("rez offer received", flush=True)
        elif name == "OP_Assist" and len(payload) >= 4:
            # Server echoes Assist with the assistee's target (or 0 if none/out of range).
            self._assist_reply = struct.unpack_from("<I", payload)[0] & 0xFFFF
        elif name == "OP_Buff" and len(payload) >= 32:
            self._on_buff_packet(payload)
        elif name == "OP_MoneyOnCorpse" and payload:
            self._loot_open = payload[0]
            # Titanium moneyOnCorpseStruct: response@0, plat/gold/silver/copper @4.
            # Server AddMoneyToPP already granted cash; we only track it.
            if len(payload) >= 20:
                plat, gold, silver, copper = struct.unpack_from("<IIII", payload, 4)
                who = self._loot_corpse_tip()
                if payload[0] in (1, 3):
                    self._loot_coin_copper = (
                        int(plat) * 1000 + int(gold) * 100 + int(silver) * 10 + int(copper)
                    )
                    gained = self.model.add_coin(plat, gold, silver, copper)
                    print(
                        f"loot coin {who}response={payload[0]} {plat}p {gold}g {silver}s {copper}c "
                        f"gained={gained} → {self.model.coin_line()}",
                        flush=True,
                    )
                else:
                    print(
                        f"loot coin blocked {who}response={payload[0]} "
                        f"({plat}p {gold}g {silver}s {copper}c on corpse)",
                        flush=True,
                    )
        elif name == "OP_BecomeCorpse":
            self.model.on_become_corpse(payload)
            if len(payload) >= 4:
                spawn_id = struct.unpack_from("<I", payload)[0]
                # Poison/DoT packets keep the corpse's entity id as source — never
                # treat a corpse as an attacker (false retaliate).
                self._forget_combat_spawn(spawn_id)
                # Cleric bot died — ^botspawn before reclaim parks on "cleric missing".
                if spawn_id and spawn_id not in (self.model.self_id, 0):
                    self._note_bot_corpse(spawn_id)
                if spawn_id in (self.model.self_id, 0):
                    spot = self.model.own_corpse_at or self.model.position
                    zone = self.model.own_corpse_zone or self.model.zone or "?"
                    x, y, z = spot
                    print(f"death corpse zone={zone} pos=({x:.0f}, {y:.0f}, {z:.0f})", flush=True)
                elif spawn_id and (
                    spawn_id in self.attacked
                    or spawn_id == self._swing_id
                    or spawn_id == self._focus
                ):
                    # Prefer _retire (HP 0); BecomeCorpse is a backup if that missed.
                    self._retire(spawn_id)
                elif spawn_id:
                    # Party / off-target kill — loot every NPC corpse bots drop for us.
                    spawn = self.model.spawns.get(spawn_id)
                    if spawn is not None and spawn.npc != 0:
                        self._retire(spawn_id)
        elif name == "OP_Consider":
            self.model.on_consider(payload)
            self._note_consider(payload)
        elif name == "OP_MoveDoor":
            door_id = self.model.on_move_door(payload)
            if door_id:
                self.score.doors += 1
        elif name == "OP_CharInventory":
            for held in self.inventory.load_inventory(payload, self._wanted_ids()):
                self._enrich_held(held)
                print(f"inv {held.slot} {held.name}", flush=True)
                if held.scroll_spell:
                    self._bind_gem(held.scroll_spell)
            self._char_inventory_at = time.monotonic()
            self._failed_equips = set()
            self._failed_stow_dests = set()
            self._failed_stow_at = {}
            # Trailing ItemPackets (cursor/bags) often arrive right after CharInventory.
            self._inventory_bootstrapped = False
            self._inventory_dumped = False
            self._inv_settle_attempts = 0
        elif name == "OP_ItemPacket":
            held = self.inventory.on_packet(payload, self._wanted_ids())
            if held is not None and held.slot not in self.inventory.corpse_slots:
                self._enrich_held(held)
                print(f"inv {held.slot} {held.name}", flush=True)
                if held.scroll_spell:
                    self._bind_gem(held.scroll_spell)
                # New cursor gear invalidates prior failed equip attempts.
                if held.slot == CURSOR:
                    self._failed_equips = set()
        elif name == "OP_DeleteItem" and len(payload) >= 4:
            # SwapItemResync / empty-slot repair — clear local slot (Titanium ids).
            slot = struct.unpack_from("<I", payload)[0]
            if slot in self.inventory.slots:
                gone = self.inventory.slots.pop(slot)
                print(f"inv del {slot} {gone.name}", flush=True)
            else:
                self.inventory.slots.pop(slot, None)
        elif name == "OP_MemorizeSpell" and len(payload) >= 16:
            self._on_memorize(payload)
        elif name == "OP_TaskSelectWindow":
            self.tasks.on_select_window(payload)
            self._restore_battle()
            if self.tasks.offer is not None and self.tasks.offer.task_id in self.tasks.completed:
                self.tasks.offer = None
            accept = self.tasks.accept_bytes()
            if accept:
                self.client.send("OP_AcceptNewTask", accept)
        elif name == "OP_TaskActivity":
            before = _done_map(self.tasks)
            self.tasks.on_activity(payload)
            self._note_progress(before)
        elif name == "OP_TaskActivityComplete":
            before = _done_map(self.tasks)
            self.tasks.on_complete(payload)
            self._note_progress(before)
        elif name == "OP_OnLevelMessage":
            title, text, popup_id = popup_message(payload)
            print(f"popup {title}: {text}", flush=True)
            self.client.send("OP_PopupResponse", popup_response(popup_id))
            lesson = lesson_from(text)
            if lesson is not None:
                if self.lesson != lesson:
                    self.guide = []
                    self._guide_for = 0
                    self._find_for = 0
                self.lesson = lesson
                print(f"next {lesson.kind} {lesson.name} {lesson.text}".rstrip(), flush=True)
        elif name == "OP_SimpleMessage" and len(payload) >= 8:
            string_id = struct.unpack_from("<I", payload, 4)[0]
            if string_id == 124:
                self._too_far = True
                print("too far", flush=True)
        elif name == "OP_HPUpdate" and len(payload) >= 10:
            # Titanium cur_hp is sent signed in practice; unsigned unpack wraps deaths
            # into 4e9 and hides "he died" (and breaks needs_rest).
            # spawn_id here is our entity id — ZoneSpawns often never sets self_id.
            cur, max_hp, spawn_id = struct.unpack_from("<iiH", payload)
            if spawn_id:
                self.model.self_id = int(spawn_id) & 0xFFFF
            if max_hp > 0:
                before = self.model.needs_rest(False)
                self.model.max_hp = max_hp
                self.model.hp = max(0, min(cur, max_hp))
                if not before and self.model.needs_rest(False):
                    print(f"health {self.model.hp}/{self.model.max_hp}", flush=True)
                if self.model.max_hp > 0 and self.model.hp * 100 < self.model.max_hp * 55:
                    self._maybe_emergency_heal()
        elif name == "OP_MobHealth" and len(payload) >= 3:
            # Titanium group HP uses CreateHPPacket → OP_MobHealth (spawn_id, hp%).
            entity, hp = struct.unpack_from("<hB", payload)
            hp = max(0, min(100, int(hp)))
            self._note_party_health(entity & 0xFFFF, hp)
            if self._swing_id and (self._swing_id & 0xFFFF) == (entity & 0xFFFF):
                if hp != self._swing_hp:
                    if self._swing_hp < 0 or hp < self._swing_hp:
                        self._progress_at = time.monotonic()
                    spawn = self.model.spawns.get(self._swing_id)
                    print(f"hp {spawn.name if spawn else entity} {hp}", flush=True)
                self._swing_hp = hp
                if hp == 0:
                    self._retire(self._swing_id)
        elif name == "OP_Damage" and len(payload) >= 11:
            target, source = struct.unpack_from("<HH", payload)
            # Titanium CombatDamage_Struct: type@4, spellid@5, damage@7.
            dmg_type = payload[4]
            spell_id = struct.unpack_from("<H", payload, 5)[0] if len(payload) >= 7 else 0
            # Wire damage is uint32 but miss/block/riposte often arrive as negative
            # (e.g. -4 → 4294967292). Treat as signed; clamp display to >= 0.
            raw_damage = struct.unpack_from("<i", payload, 7)[0]
            damage = max(0, raw_damage)
            me = self.model.self_id & 0xFFFF
            source_spawn = self._spawn_by_entity(source)
            target_spawn = self._spawn_by_entity(target)
            # Poison/DoT keeps firing with the dead entity id after BecomeCorpse —
            # never promote a corpse into bot-threat / retaliate.
            if self._is_corpse_spawn(source_spawn) or (
                target != me and self._is_corpse_spawn(target_spawn)
            ):
                pass
            else:
                bot_ids = {spawn.spawn_id & 0xFFFF for spawn in self._bot_spawns()}

                def _live_npc(short: int):
                    spawn = self._spawn_by_entity(short)
                    if spawn is None or spawn.npc != 1 or self._is_corpse_spawn(spawn):
                        return None
                    return spawn

                if source == me:
                    self._landed = True
                    print(f"hit {damage}", flush=True)
                elif source in bot_ids:
                    # Bot landed a hit — they have a fight; do not walk off and leave them.
                    victim = _live_npc(target)
                    if victim is not None and not self._has_gave_up(victim.spawn_id):
                        self._note_bot_threat(
                            victim, f"bot-hit dmg={damage}", bot_id=source
                        )
                elif source and source != me and (target == me or target in bot_ids):
                    # Only credit a live NPC source — never "nearest mob" guesswork
                    # (that turned poison-on-corpse into a false retaliate).
                    attacker = _live_npc(source)
                    if attacker is not None and not self._has_gave_up(attacker.spawn_id):
                        who = "us" if target == me else "bot"
                        # Spell DoT ticks (type 231) from far casters — common after
                        # ghoul disease — must not yank reclaim into a chase loop.
                        spell_dot = dmg_type == 231 and spell_id not in (0, 0xFFFF)
                        far = (
                            _horiz(
                                self.model.position,
                                (attacker.x, attacker.y, attacker.z),
                            )
                            > 45.0
                        )
                        if not (spell_dot and (far or self._cure_spells)):
                            bot_id = target if target in bot_ids else 0
                            self._note_bot_threat(
                                attacker, f"dmg={damage} on={who}", bot_id=bot_id
                            )
                    if target == me and damage > 0:
                        self._maybe_emergency_heal()
                        if dmg_type == 231 and spell_id not in (0, 0xFFFF):
                            self._maybe_cure()
        elif name == "OP_FindPersonReply":
            route = guide_from(find_path(payload), self.model.position)
            self._guide_for = self._find_for
            self.guide = route
            self._find_arrived.discard(self._find_for)
            # Find.dest is the NPC's server position — keep spawn.where honest for chase.
            dest = find_destination(payload)
            if dest is not None and self._find_for:
                spawn = self.model.spawns.get(self._find_for)
                if spawn is not None:
                    spawn.x, spawn.y, spawn.z = dest
                    self.model.last_seen[spawn.name.lower()] = (self.model.zone, *dest)
            if route:
                self._find_empty.discard(self._find_for)
                end = route[-1]
                print(f"path {len(route)} -> ({end[0]:.0f}, {end[1]:.0f}, {end[2]:.0f})", flush=True)
            else:
                # Empty glow means either "already there" or "too far" — distance decides.
                dist = 1e9
                spawn = self.model.spawns.get(self._find_for)
                if spawn is not None:
                    dist = _horiz(self.model.position, (spawn.x, spawn.y, spawn.z))
                chasing = self._grind_mode == "chase" and self._find_for in (
                    self._swing_id,
                    self._pursuit,
                    self._threat,
                )
                if dist <= max(_ACT_RANGE.get("shop", 20.0), 40.0):
                    if chasing:
                        # Stale pad + empty Find during chase — keep reacquiring, do not seal.
                        print(f"path empty (chase {dist:.0f})", flush=True)
                    else:
                        self._find_arrived.add(self._find_for)
                        self._find_empty.discard(self._find_for)
                        print(f"path empty (here {dist:.0f})", flush=True)
                else:
                    self._find_empty.add(self._find_for)
                    print(f"path empty (far {dist:.0f})", flush=True)

    def run(self, seconds: float | None = None, stop_on_zone: bool = False) -> Score:
        limit = seconds if seconds is not None else float(os.environ.get("EQEMU_AGENT_SECONDS", "180"))
        stop_on_zone = stop_on_zone or os.environ.get("EQEMU_AGENT_STOP_ON_ZONE") == "1"
        started_zone = self.model.zone
        if stop_on_zone and started_zone and started_zone.lower() != "tutorialb":
            print(f"zone {started_zone}", flush=True)
            self.score.zone = started_zone
            print(self.score.line())
            return self.score
        deadline = time.monotonic() + limit
        next_report = 0.0
        # Group mode: drop any leftover raid and clear the saved roster so
        # FormOnConnect does not keep spawning a 10-bot raid over our group.
        if not self.form_raid:
            self._clear_bot_raid_roster()
            self._leave_raid(camp=not self.form_group)
        while time.monotonic() < deadline:
            self.client.pump(TICK)
            if self.model.consume_server_move():
                self.path = []
            self._settle_move()
            self._send_history()
            self._party_messages()
            # Inventory first — never form/reclaim/loot on an unsettled cursor.
            if not getattr(self, "_inventory_bootstrapped", False):
                if not self._bootstrap_inventory():
                    self.client.pump(0.2)
                    continue
                self._inventory_bootstrapped = True
            if stop_on_zone and self.model.changed_zone and self.model.zone and self.model.zone != started_zone:
                break
            if self._pending_inviter:
                if self._under_fire():
                    # Finish the fight before accepting — invite pumps used to wipe us.
                    pass
                else:
                    inviter = self._pending_inviter
                    self._pending_inviter = ""
                    self._accept_party_invite(inviter)
                    continue
            # Invite tell with no accept — do not park the campaign forever.
            if (
                self._pc_party
                and self._awaiting_pc_join
                and self._awaiting_pc_since
                and time.monotonic() - self._awaiting_pc_since > 90.0
            ):
                self._resume_after_pc_party(why="invite-timeout")
            if self._deliver_to and self._deliver_item:
                delivered = self._try_deliver()
                if delivered:
                    continue
            # Rebuild bots even on a corpse run — solo reclaim at ecommons undead is a wipe.
            # Form to completion before reclaim/shop; only pause for close combat.
            if (
                (self.form_raid or self.form_group)
                and not self._pc_party
                and not self.party.formed
            ):
                # Camp/spawn refuse while raid/group engaged — leave raid, fight, then retry.
                if getattr(self.party, "blocked", False):
                    if not self.form_raid:
                        self._leave_raid(camp=False)
                    if self._forming_under_fire():
                        next_report = self._report(
                            next_report, Intention("form_party"), force=False
                        )
                        # Fall through — close fight only; reclaim stays gated below.
                    else:
                        self.party.clear_block()
                        next_report = self._report(
                            next_report, Intention("form_party"), force=False
                        )
                        self._form_party()
                        continue
                elif self._forming_under_fire():
                    # Close fight interrupted invite/camp — defend, then resume form.
                    next_report = self._report(
                        next_report, Intention("form_party"), force=False
                    )
                else:
                    next_report = self._report(
                        next_report, Intention("form_party"), force=False
                    )
                    self._form_party()
                    continue
            if (
                (self.form_raid or self.form_group)
                and not self._pc_party
                and self.party.formed
                and not self._group_loot_set
            ):
                self._apply_group_loot_settings()
            if (
                (self.form_raid or self.form_group)
                and not self._pc_party
                and self.party.formed
                and not self._heal_rotation_set
                and time.monotonic() - self._heal_rotation_at >= 30.0
            ):
                self._setup_bot_heal()
            # Inventory cache after heal setup — listing all bots first kills create replies.
            if (
                self.party.formed
                and self._heal_rotation_set
                and len(self._bot_worn_listed) < len(self.party.spawned)
            ):
                self._cache_all_bot_worn()
            reclaiming_now = bool(
                self.model.needs_corpse
                or self.journal.outstanding_corpses(self.model.character) > 0
            )
            if (
                not reclaiming_now
                and self.inventory.tome() is None
                and (self.lesson is None or self.lesson.kind != "equip")
            ):
                self._settle_gear()
            if self.model.have_position:
                before = self.survey.signature
                self.survey.note(
                    self.model.position,
                    (self.model.level, signature_of(self.tasks.activities)),
                )
                if self.survey.signature != before:
                    self.search.reset()
            if not self._listed_tasks and self.tasks.activities:
                self._listed_tasks = True
                for activity in self.tasks.activities:
                    print(
                        f"obj {activity.task_id}/{activity.activity_id} step={activity.step} "
                        f"kind={activity.kind} {activity.target_name or '-'} {activity.done}/{activity.goal}"
                        f"{' optional' if activity.optional else ''}",
                        flush=True,
                    )
            self._restore_battle()
            before_stack = list(self.campaign.stack)
            if not self._tutorial_done and self.journal.tutorial_done(self.model.character):
                self._tutorial_done = True
                print("tutorial: done", flush=True)
            self._seek_spells()
            self._seek_bot_spells()
            # Never inventorygive / equip churn while mobs are on us — trade pumps
            # used to lock the tick through aggro (lantern → Mocwiz spin).
            # Also skip bag→bot churn while corpse coin is outstanding.
            reclaiming_now = bool(
                self.model.needs_corpse
                or self.journal.outstanding_corpses(self.model.character) > 0
            )
            if not self._under_fire() and not self._engaged() and not reclaiming_now:
                self._settle_gear()
                self._seek_gear()
            elif self.inventory.cursor() is not None:
                # Free hands for combat — stow once, do not re-offer to bots.
                self._stow_cursor(timeout=0.3)
            self._refresh_corpse_backlog()
            self._seek_bags()
            intention = guide(
                self.model,
                self.tasks,
                self.quests,
                self.inventory,
                True,
                self.skipped_ground,
                self.skipped_corpses,
                self.said,
                self.handed,
                self.lesson,
                self.journal.hubs(self.model.character, self.model.zone or ""),
                self.journal.flag_values(self.model.character),
                self.graph,
                self.journal.said_everywhere(self.model.character),
                self.campaign,
                tutorial_done=self._tutorial_done,
                merchants=self.merchants,
                recipes=self.recipes,
                drops=self.drops,
                factions=self.factions,
                skills=self._skills,
            )
            if list(self.campaign.stack) != before_stack:
                self._persist_goals()
            # Fight first — invite/follow in _conduct used to pump while mobs killed us.
            early_retaliate = self._retaliate_intention() if self._under_fire() else None
            if early_retaliate is not None:
                # Always order bots+pet on retaliate — threat is set before ^attack,
                # so do not wait for reclaim-only rally.
                why = (
                    "reclaim threat"
                    if (
                        self.model.needs_corpse
                        or self.journal.outstanding_corpses(self.model.character) > 0
                    )
                    else "retaliate"
                )
                self._rally_bots(
                    force=True,
                    why=why,
                    attack_target=early_retaliate.target,
                )
                intention = early_retaliate
            else:
                intention = self._conduct(intention)
            intention = self._resolve_zone_travel(intention)
            intention = self._maybe_soulbind(intention)
            self._maybe_bot_report()
            self._maybe_cure()
            # Never corpse-walk / shop while the raid is still forming.
            if (
                (self.form_raid or self.form_group)
                and not self._pc_party
                and not self.party.formed
                and not self._forming_under_fire()
            ):
                next_report = self._report(
                    next_report, Intention("form_party"), force=False
                )
                self._form_party()
                continue
            # Corpse reclaim (coin) outranks grind — but never walk through open aggro.
            reclaiming = intention is not None and intention.kind == "reclaim"
            if reclaiming:
                hold = self._reclaim_support_hold()
                if hold is not None:
                    # Dead cleric: spawn immediately — rally alone cannot summon a corpse.
                    if "cleric missing" in hold or hold == "no cleric spawned":
                        self._ensure_clerics_spawned()
                    # Critical / missing support only — never pause the walk for follow lag.
                    self._rally_bots(force=True, why="reclaim support")
                    if self._reclaim_rest_logged != hold:
                        print(f"reclaim hold → {hold}", flush=True)
                        self._reclaim_rest_logged = hold
                    intention = Intention("rest", name="party")
                    reclaiming = False
            # Long corpse walk: drop a *stale* leftover swing so finish can't yank us.
            # Never drop the active reclaim clear / threat — we hold from threat range
            # (~150yd) while bots make first contact.
            if reclaiming and self._swing_id:
                swinging = self.model.spawns.get(self._swing_id)
                if swinging is None or swinging.npc != 1:
                    self._swing_id = 0
                else:
                    sid = self._swing_id
                    active_clear = sid in (
                        self._threat,
                        self._pursuit,
                        self._reclaim_held_for,
                    )
                    sdist = _horiz(
                        self.model.position, (swinging.x, swinging.y, swinging.z)
                    )
                    if not active_clear and sdist > max(80.0, _RECLAIM_CAUTION):
                        print(
                            f"combat drop swing {swinging.name} (reclaim far {sdist:.0f})",
                            flush=True,
                        )
                        self._chase_best_dist.pop(sid, None)
                        self._swing_id = 0
                        self.client.send("OP_AutoAttack", b"\x00\x00\x00\x00")
            # Feet-loot between pulls (and on the reclaim walk): don't skip a fresh kill.
            looting = False
            if intention is not None and intention.kind == "loot":
                looting = True
                reclaiming = False
            else:
                foot = self._nearby_loot_intention()
                if foot is not None:
                    intention = foot
                    looting = True
                    reclaiming = False
            retaliate = self._retaliate_intention()
            # Cautious corpse run: pause for LOS hostiles one-at-a-time (do not train).
            # Skip while feet-looting — don't abandon the corpse for a distant sight pull.
            path_clear = False
            if reclaiming and retaliate is None and not self._engaged():
                corpse_at = intention.where if intention is not None else None
                blocker = self._reclaim_path_foe(corpse_at)
                if blocker is not None:
                    path_clear = True
                    self._pursuit = blocker.spawn_id
                    self._threat = blocker.spawn_id
                    retaliate = Intention(
                        "task_kill",
                        target=blocker.spawn_id,
                        name=blocker.name,
                        where=(blocker.x, blocker.y, blocker.z),
                        text="retaliate",
                    )
            clear_aggro = retaliate is not None and (self._must_clear_aggro() or path_clear)
            if retaliate is not None and (clear_aggro or (not reclaiming and not looting)):
                if (reclaiming or looting) and self._reclaim_held_for != retaliate.target:
                    # Drop corpse Find — fight one foe, then resume reclaim after.
                    self._reclaim_held_for = retaliate.target
                    self.guide = []
                    self._guide_for = 0
                    self._find_for = 0
                    why = "sight" if path_clear else "aggro"
                    print(f"reclaim hold → clear {retaliate.name} ({why})", flush=True)
                    # One summon if far; attack once they're here — never spam.
                    self._rally_bots(
                        force=True,
                        why="reclaim threat",
                        attack_target=retaliate.target,
                    )
                    # Spot early, then wait for the raid before we close — don't solo-charge.
                    if not self._bots_close(100):
                        spawn = self.model.spawns.get(retaliate.target or 0)
                        if spawn is not None:
                            dist = _horiz(
                                self.model.position, (spawn.x, spawn.y, spawn.z)
                            )
                            print(
                                f"reclaim wait bots → {retaliate.name} "
                                f"dist={dist:.0f} threat={_RECLAIM_CAUTION:.0f}yd",
                                flush=True,
                            )
                intention = retaliate
                reclaiming = False
                looting = False
            else:
                if reclaiming or looting:
                    self._reclaim_held_for = 0
                else:
                    self._reclaim_rest_logged = ""
                # Rest outranks grind AND corpse reclaim — but loot beats rest so a
                # fresh kill is bagged before medding. Aggro clear above still wins.
                from eqclient.camps import zone_recommended_level

                at_safe = _horiz(self.model.position, self.model.safe) <= SAFE_RANGE
                # Zones under recommended L30: sit where we are (ecommons, etc.).
                sit_here = zone_recommended_level(self.model.zone or "") < 30
                hurt = (
                    self.model.needs_rest(self._sitting)
                    or self._needs_mana_rest()
                    or self._party_needs_rest()
                )
                # Feet-loot / explicit loot keeps priority over sit.
                decision = None if looting else recover(
                    hurt,
                    self._engaged(),
                    at_safe,
                    sit_here=sit_here,
                )
                if decision == "safe":
                    if reclaiming and self._reclaim_rest_logged != "safe":
                        print("reclaim hold → safe (rest)", flush=True)
                        self._reclaim_rest_logged = "safe"
                    intention = Intention("explore", name="safe", where=self.model.safe)
                    self._break_off()
                    reclaiming = False
                elif decision == "rest":
                    if self._needs_mana_rest() and not self.model.needs_rest(self._sitting) and not self._party_needs_rest():
                        why = "mana"
                        self._cleric_medding = True
                    elif self._party_needs_rest() and not self.model.needs_rest(self._sitting):
                        why = "party"
                    else:
                        why = "health"
                    if reclaiming:
                        tip = why
                        if why == "mana" and self._cleric_mana is not None:
                            tip = f"{why} clr={self._cleric_mana * 100:.0f}%"
                        if self._reclaim_rest_logged != tip:
                            print(f"reclaim hold → rest {tip}", flush=True)
                            self._reclaim_rest_logged = tip
                    # Healrotation locks onto the lowest-HP target; out of range = no casts.
                    # Gather first so the cleric can actually land heals, then sit.
                    if why == "party" and not self._bots_close(40):
                        self._rally_bots(why="gather")
                        anchor = self._bot_anchor()
                        if anchor is not None and _horiz(self.model.position, anchor) > 20:
                            intention = Intention("explore", name="party_heal", where=anchor)
                            self._break_off(keep_pursuit=True)
                        else:
                            intention = Intention("rest", name="party")
                            self._break_off(keep_pursuit=True)
                    else:
                        intention = Intention("rest", name=why)
                        # Keep grind walk pursuit — clearing it re-prints Find every sit.
                        self._break_off(keep_pursuit=True)
                    reclaiming = False
                    looting = False
                elif (
                    not reclaiming
                    and not looting
                    and intention is not None
                    and intention.kind == "fight"
                    and not self._engaged()
                    and not self._swing_id
                    and not self._live_bot_threats()
                ):
                    # Scan LOS → chase L..L+2; else walk closest spawn ≥5s → rescan.
                    # Never rescan while a swing is still live — that abandoned
                    # rattlesnakes mid-close for a beetle 800 yd away.
                    # Never walk off while bots still have open aggro fights.
                    intention = self._grind_cycle(intention)
            # Finish the pull we already opened before any new grind pick.
            # Never abandon corpse reclaim / feet-loot for a leftover swing from before death.
            if (
                not reclaiming
                and not looting
                and self._swing_id
                and not self._has_gave_up(self._swing_id)
            ):
                swinging = self.model.spawns.get(self._swing_id)
                if swinging is not None and self._is_companion_pet(swinging):
                    print(f"combat drop pet swing {swinging.name}", flush=True)
                    self._mark_gave_up(self._swing_id, 120.0)
                    self._bot_threats.discard(self._swing_id)
                    self._swing_id = 0
                    if self._pursuit == swinging.spawn_id:
                        self._pursuit = 0
                    if self._threat == swinging.spawn_id:
                        self._threat = 0
                    self.client.send("OP_AutoAttack", b"\x00\x00\x00\x00")
                elif swinging is not None and swinging.npc == 1:
                    dist = _horiz(
                        self.model.position, (swinging.x, swinging.y, swinging.z)
                    )
                    # Stale swing after a corpse hike — don't cross the zone "finishing".
                    if dist > _FINISH_MAX_DIST:
                        print(
                            f"combat drop finish {swinging.name} id={self._swing_id} "
                            f"(far {dist:.0f})",
                            flush=True,
                        )
                        self._mark_gave_up(self._swing_id, 60.0)
                        self._bot_threats.discard(self._swing_id)
                        self._chase_best_dist.pop(self._swing_id, None)
                        self._swing_id = 0
                        if self._pursuit == swinging.spawn_id:
                            self._pursuit = 0
                        if self._threat == swinging.spawn_id:
                            self._threat = 0
                        self.client.send("OP_AutoAttack", b"\x00\x00\x00\x00")
                    else:
                        intention = Intention(
                            "task_kill",
                            target=swinging.spawn_id,
                            name=swinging.name,
                            where=(swinging.x, swinging.y, swinging.z),
                            text="finish",
                        )
                        self._pursuit = swinging.spawn_id
            held = self.model.spawns.get(self._pursuit)
            if held is not None and self._is_companion_pet(held):
                self._bot_threats.discard(held.spawn_id)
                self._mark_gave_up(held.spawn_id, 120.0)
                if self._pursuit == held.spawn_id:
                    self._pursuit = 0
                if self._threat == held.spawn_id:
                    self._threat = 0
                held = None
            held_dist = _horiz(self.model.position, (held.x, held.y, held.z)) if held is not None else 1e9
            # Follow a mob he is already hitting. Do not hike after one that is still a walk away.
            hold_reach = 45 if self._swing_id == self._pursuit else 20
            threat = held is not None and held.spawn_id == self._threat and held_dist <= 40
            if (
                not reclaiming
                and not looting
                and retaliate is None
                and held is not None
                and held.npc == 1
                and not self._has_gave_up(held.spawn_id)
                and held_dist <= hold_reach
                and (not self.tasks.local_work_left() or _kill_still_wanted(self.tasks, held.name) or threat)
            ):
                intention = Intention(
                    "task_kill",
                    target=held.spawn_id,
                    name=held.name,
                    where=(held.x, held.y, held.z),
                )
            elif intention is not None and intention.kind == "task_kill" and self._has_gave_up(intention.target):
                if self.tasks.local_work_left():
                    other = self._other_kill(intention.name) or self._next_wanted()
                    intention = other if other is not None else Intention("explore", name=intention.name)
                else:
                    nxt = _mine_target(self.model, self._gave_up_skip())
                    if nxt is not None:
                        intention = Intention(
                            "task_kill",
                            target=nxt.spawn_id,
                            name=nxt.name,
                            where=(nxt.x, nxt.y, nxt.z),
                        )
                    else:
                        intention = Intention("explore", name="mine")
            elif intention is not None and intention.kind == "fight" and self._has_gave_up(intention.target):
                intention = self._next_grind_fight() or Intention(
                    "grind", name=self.model.zone or "xp", text=self._grind_why()
                )
            focus = self.model.spawns.get(self._focus)
            if (
                not reclaiming
                and not looting
                and focus is not None
                and focus.npc == 1
                and not self._has_gave_up(focus.spawn_id)
                and _kill_still_wanted(self.tasks, focus.name)
            ):
                focus_dist = _horiz(self.model.position, (focus.x, focus.y, focus.z))
                chosen_dist = 1e9
                if intention is not None and intention.kind == "task_kill" and intention.where is not None:
                    chosen_dist = _horiz(self.model.position, intention.where)
                if focus_dist <= chosen_dist + 8:
                    intention = Intention(
                        "task_kill",
                        target=focus.spawn_id,
                        name=focus.name,
                        where=(focus.x, focus.y, focus.z),
                    )
                else:
                    self._focus = 0
            elif intention is not None and intention.kind in ("task_kill", "fight"):
                self._focus = intention.target
            else:
                self._focus = 0
            if reclaiming or looting:
                self._pursuit = 0
            elif intention is not None and intention.kind in ("task_kill", "fight"):
                self._pursuit = intention.target
            elif intention is not None and intention.kind == "rest":
                pass  # keep pursuit across sits so grind walk does not re-Find
            else:
                self._pursuit = 0
            # A fight that is not dropping means the raid is not on it. Break off
            # and collect the bots — only once we have actually landed hits in melee.
            # Stale spawn coords (standing on the pad, mob already gone) must not regroup.
            if (
                self._swing_id
                and self._swing_at
                and self._landed
                and time.monotonic() - self._swing_at > 20
                and (self._swing_hp < 0 or self._swing_hp > 75)
            ):
                swinging = self.model.spawns.get(self._swing_id)
                in_melee = (
                    swinging is not None
                    and swinging.npc == 1
                    and _horiz(self.model.position, (swinging.x, swinging.y, swinging.z))
                    <= _MELEE_RANGE + 8
                )
                if in_melee:
                    print("regroup", flush=True)
                    self._swing_id = 0
                    self._focus = 0
                    self._pursuit = 0
                    self._grind_mode = ""
            # Tunnel task kills: wait for bots. Never break an active grind chase for this.
            if (
                self._swing_id == 0
                and intention is not None
                and intention.kind == "task_kill"
                and self._grind_mode not in ("chase", "walk")
                and _kill_still_wanted(self.tasks, intention.name or "")
                and not self._bots_close()
            ):
                anchor = self._bot_anchor()
                if anchor is not None:
                    intention = Intention("explore", name="bots", where=anchor)
            if (
                not reclaiming
                and not looting
                and (self.model.needs_rest(self._sitting) or self._needs_mana_rest() or self._party_needs_rest())
                and self._engaged()
            ):
                foe = self.model.spawns.get(self._swing_id) or self.model.spawns.get(self._threat)
                if foe is not None:
                    intention = Intention(
                        "task_kill",
                        target=foe.spawn_id,
                        name=foe.name,
                        where=(foe.x, foe.y, foe.z),
                    )
                    self._pursuit = foe.spawn_id
            elif (
                self._sitting
                and not self.model.needs_rest(True)
                and not self._needs_mana_rest()
                and not self._party_needs_rest()
            ):
                self._stand()
            elif (
                self._sitting
                and intention is not None
                and intention.kind not in ("rest", "loot")
            ):
                # Still regenerating HP/mana/party — do not walk/grind until stood up above.
                # Loot at feet still wins so kills are not left on the ground.
                if self._needs_mana_rest():
                    why = "mana"
                elif self._party_needs_rest():
                    why = "party"
                else:
                    why = "health"
                intention = Intention("rest", name=why)
            if intention is None:
                continue
            # Mobs walk — keep fight/kill goto on the live spawn every tick.
            intention = self._with_live_where(intention)
            label = _intention_label(intention, self.item_stats)
            changed = label != getattr(self, "_last_act", "")
            next_report = self._report(next_report, intention, force=changed)
            self._act(intention)
        self.score.zone = self.model.zone
        print(self.score.line())
        return self.score

    def _report(self, next_report: float, intention: Intention, force: bool) -> float:
        """Print zone, position, sit/HP, and full intention when it changes (and every few seconds)."""
        now = time.monotonic()
        if not force and now < next_report:
            return next_report
        # Rest lines must reflect a real sit — stand status on "intent rest" is a lie.
        if intention.kind == "rest" and not self._sitting:
            self._rest()
        label = _intention_label(intention, self.item_stats)
        self._last_act = label
        zone = self.model.zone or "?"
        x, y, z = self.model.position
        posture = "sit" if self._sitting else "stand"
        hp = f"hp={self.model.hp}/{self.model.max_hp}"
        party = self._lowest_party_hp_tip()
        extra = f" {party}" if party else ""
        print(
            f"zone {zone} pos=({x:.0f}, {y:.0f}, {z:.0f}) {posture} {hp} intent {label}{extra}",
            flush=True,
        )
        return now + 5.0

    def _lowest_party_hp_tip(self) -> str:
        """Lowest bot/PC group member hp% for zone lines when under safe (75%)."""
        self._prune_party_hp()
        if not self._party_hp:
            return ""
        worst_id = min(self._party_hp, key=self._party_hp.get)
        pct = self._party_hp[worst_id]
        if pct > 75:
            return ""
        member = self._party_member_spawn(worst_id)
        name = member.name if member is not None else str(worst_id)
        return f"party_low={name}:{pct}%"

    def _enter_zone(self) -> None:
        zone = self.model.zone
        if zone and zone not in self.score.zones:
            self.score.zones.append(zone)
        self.score.zone = zone
        self.quests = load_zone(zone)
        if self.graph is not None:
            self.graph.apply(self.quests)
        self.nav = load_nav(zone)
        self.zone_map = load_map(zone)
        self.water = load_water(zone)
        self._swimming = False
        self.path = []
        self._pending = None
        self.refused_dirs.clear()
        self.step_length = STEP
        self.turn_offset = 0.0
        # Snap to NewZone safe on a real zone hop — never keep 0,0,0 from ZTZ success.
        safe = self.model.safe
        here = self.model.position
        hopped = bool(self.model.changed_zone)
        at_origin = abs(here[0]) + abs(here[1]) < 1.0
        safe_ok = safe is not None and abs(safe[0]) + abs(safe[1]) > 50.0
        if hopped and safe is not None:
            self.model.reset_position(*safe)
        elif at_origin and safe_ok:
            self.model.reset_position(*safe)
        elif self.model.have_position and self.model.server_position:
            self.model.clear_step()
        elif safe is not None:
            self.model.reset_position(*safe)
        else:
            self.model.clear_step()
        # Drop ClientUpdate/spawn echoes at 0,0,0 for a few seconds after enter.
        self.model._ignore_origin_until = time.monotonic() + 8.0
        x, y, z = self.model.position
        print(f"zone enter {zone} pos=({x:.0f}, {y:.0f}, {z:.0f})", flush=True)
        if self.water is not None:
            print(f"water map {zone} v{self.water.version}", flush=True)
        self._answered.clear()
        self.lesson = None
        self.guide = []
        self._guide_for = 0
        self._find_for = 0
        self._roam = None
        self._roam_name = ""
        self.survey.reset()
        self.search.reset()
        self.skipped_ground.clear()
        self.skipped_corpses.clear()
        self.attacked.clear()
        self._killed.clear()
        self._gave_up.clear()
        self._clear_walk_stuck()
        self._find_arrived.clear()
        self.said = self.journal.said(self.model.character, zone)
        self.handed = self.journal.handed(self.model.character, zone)
        # Same dynamic zone often keeps bots spawned — reform leads with botsummon.
        if (self.form_group or self.form_raid) and not self._pc_party:
            # Saved ^raidform roster auto-spawns a 10-bot raid on connect and
            # then our leave_raid tears it down — clear it in group mode so
            # FormOnConnect stops winning over OP_GroupInvite.
            if self.form_group and not self.form_raid:
                self._clear_bot_raid_roster()
            self.party.on_zone_enter()
            self._grouped = False
            self._group_loot_set = False
            self._heal_rotation_set = False
            # spellsettings/stance/holds persist on the bot — do not re-spam every zone
            print(f"party: reform in {zone} (summon first)", flush=True)
        # Respawn / NewZone can drop the in-memory corpse flag — restore closest body.
        pending = self.journal.outstanding_corpses(self.model.character)
        if pending > 0:
            here = self.model.position
            remembered = self.journal.corpse(
                self.model.character,
                zone=zone or self.model.zone or "",
                x=here[0],
                y=here[1],
                z=here[2],
            )
            if remembered is not None:
                czone, cx, cy, cz = remembered
                self.model.needs_corpse = True
                self.model.own_corpse_zone = czone
                self.model.own_corpse_at = (cx, cy, cz)
                self.model.own_corpse_id = 0
                print(
                    f"reclaim restore {pending} corpse(s); next zone={czone} pos=({cx:.0f}, {cy:.0f}, {cz:.0f})",
                    flush=True,
                )
        self._restore_battle()

    def _act(self, intention: Intention) -> None:
        kind = intention.kind
        tip = str(intention.text or "")
        if tip.startswith("faction:") or tip.startswith("faction-check"):
            self._faction_focus = tip
        if kind == "fish":
            self._fish(intention)
            return
        self._unfish()
        if kind == "rest":
            self._rest()
            return
        if kind == "soulbind":
            self._do_soulbind(intention)
            return
        if kind == "tell":
            who = self._leader or next(iter(self._known_names), "")
            if who and intention.name == "summon":
                self.client.tell(who, "summon")
                self.client.send("OP_Consent", who.encode("latin1")[:64].ljust(64, b"\x00"))
            return
        if kind == "eat":
            self._eat(1 if intention.name == "food" else 2)
            return
        if kind == "cast":
            self._cast_role(intention.name, intention.target)
            return
        if kind == "ability":
            self._ability(intention.name)
            return
        if kind == "who":
            self.client.send("OP_WhoAllRequest", who_request(intention.name))
            return
        if kind == "track":
            self.client.send("OP_Track", b"")
            if intention.target:
                self.client.send("OP_TrackTarget", struct.pack("<I", intention.target))
            return
        if kind == "read":
            name = (intention.name or "book").encode("latin1")[:63]
            self.client.send("OP_ReadBook", bytes([0xFF, 1]) + name + b"\x00")
            return
        if kind == "inspect":
            self.client.send("OP_InspectRequest", struct.pack("<I", intention.target))
            return
        if kind == "shop":
            spawn = self._shop_spawn(intention)
            if spawn is None:
                where = intention.where
                if where is not None:
                    self._approach(where, intention.target)
                return
            where = (spawn.x, spawn.y, spawn.z)
            if _horiz(self.model.position, where) > _ACT_RANGE["shop"]:
                self._approach(where, spawn.spawn_id)
                return
            # Find path finished / in range — target and open the merchant window.
            if not self._target(spawn.spawn_id):
                self._approach(where, spawn.spawn_id)
                return
            self._shop(
                Intention(
                    "shop",
                    target=spawn.spawn_id,
                    name=spawn.name,
                    item_id=intention.item_id,
                    where=where,
                    text=intention.text,
                )
            )
            return
        if kind == "craft":
            tip = str(intention.text or "")
            skill_up = tip[: tip.find("@")].isdigit() if "@" in tip else False
            if self._combine(intention.target, skill_up=skill_up) is False:
                where = self._far_poly(self.nav) if self.nav is not None else None
                if where is not None:
                    self._step(where)
            return
        if kind == "bank":
            self._bank(intention)
            return
        if kind == "forage":
            self.client.send("OP_Forage", b"")
            return
        if kind == "pick_lock":
            if intention.target:
                self._use_door(intention.target, retry=True)
            return
        if self._sitting:
            self._stand()
        if kind == "explore" and intention.name == "hub" and intention.target:
            spawn = self.model.spawns.get(intention.target)
            if spawn is not None and _horiz(self.model.position, (spawn.x, spawn.y, spawn.z)) <= 20:
                self._hail(spawn.spawn_id, spawn.name)
                self.journal.record(self.model.character, self.model.zone or "", _key(spawn.name), "hub", "hail")
                return
        if kind == "explore" and str(intention.text or "").startswith("faction-check"):
            spawn = self.model.spawns.get(intention.target) if intention.target else None
            if spawn is None and intention.name:
                spawn = self._spawn_named(intention.name)
            if spawn is not None:
                here = self.model.position
                if _horiz(here, (spawn.x, spawn.y, spawn.z)) > 20:
                    self._step((spawn.x, spawn.y, spawn.z))
                    return
                self.client.send(
                    "OP_Consider",
                    struct.pack("<IIIIIIBBBB", self.model.self_id, spawn.spawn_id, 0, 0, 0, 0, 0, 0, 0, 0),
                )
                self.client.pump(0.3)
                self._journal_primary_standing(spawn)
                return
        if kind in ("explore", "grind"):
            # Sell/buy seek: once the cached seller is spawned, Find-path to them.
            if kind == "explore" and intention.text in ("sell", "buy") and intention.name and intention.name.lower() != "merchant":
                spawn = self._spawn_named(intention.name)
                if spawn is None:
                    spawn = self._nearest_merchant(item_id=intention.item_id)
                if spawn is not None:
                    self._approach((spawn.x, spawn.y, spawn.z), spawn.spawn_id)
                    return
            # Foreign zone name → leave door if first_leg has a hop; else roam while path finds.
            dest = (intention.name or "").lower().strip()
            here = (self.model.zone or "").lower()
            if dest and dest != here and self._is_zone_dest(dest):
                travel = self._travel_intention(dest, text=intention.text or "", item_id=intention.item_id or 0)
                if travel is not None and travel.kind == "leave":
                    print(
                        f"travel {here}->{dest} leave door={travel.target} next={travel.name}",
                        flush=True,
                    )
                    self._use_door(travel.target, retry=True, where=travel.where)
                    return
            where = intention.where
            label = f"explore:{intention.name or intention.text or kind}"
            if where is None and self.nav is not None:
                here = self.model.position
                keep = (
                    self._roam is not None
                    and self._roam_name == (intention.name or "")
                    and _horiz(here, self._roam) > 8
                    and time.monotonic() - self._roam_at < 40
                    and not self._walk_is_stuck(label)
                )
                if keep:
                    where = self._roam
                else:
                    where = self._far_poly() if intention.name else self.nav.unvisited(here)
                    self._roam = where
                    self._roam_name = intention.name or ""
                    self._roam_at = time.monotonic()
            if where is not None and self._walk_is_stuck(label):
                where = self._unstick_walk(where, label=label) or where
                self._roam = where
                self._roam_at = time.monotonic()
            if where is not None:
                # AreaSearch backtracks dead ends; bare _step pathing does not.
                if self.nav is not None:
                    self._approach(where, 0)
                else:
                    self._step(where)
            return
        if kind == "leave":
            where = intention.where
            label = f"leave:{intention.name or intention.target}"
            if where is not None and self._walk_is_stuck(label):
                where = self._unstick_walk(where, label=label) or where
                intention = Intention(
                    "leave",
                    target=intention.target,
                    name=intention.name,
                    where=where,
                    text=intention.text,
                    item_id=intention.item_id,
                )
            self._use_door(intention.target, retry=True, where=intention.where)
            return
        if kind == "equip":
            self._wear_return()
            return
        if kind == "learn":
            self._learn()
            return
        if kind == "scribe":
            self._scribe(intention.item_id)
            return
        if kind == "memorize":
            self._memorize(intention.item_id, intention.name)
            return
        if kind == "reclaim" and (self.model.zone or "").lower() != "tutorialb" and intention.target:
            self.client.send("OP_ConsiderCorpse", struct.pack("<I", intention.target))
        if kind == "reclaim" and not intention.target:
            # Journal-only aim (no spawn id): mesh/Find via _approach so walk-stuck
            # recovery runs. Raw _step here froze us off the WC cliff walking to a
            # stale Freeport-side journal ghost at (554,-220).
            if intention.where is not None:
                if self._prune_missing_journal_corpse(intention.where):
                    return
                self._discover_zone_corpses()
                self._refresh_corpse_backlog()
                # Live body elsewhere? Drop journal aim so plan retargets next tick.
                from eqclient.plan import _find_own_corpse_spawn

                live = _find_own_corpse_spawn(self.model, self.skipped_corpses)
                if live is not None:
                    self.model.own_corpse_id = live.spawn_id
                    self.model.own_corpse_at = (live.x, live.y, live.z)
                    self.model.own_corpse_zone = self.model.zone or self.model.own_corpse_zone
                    print(
                        f"reclaim retarget live {live.name} id={live.spawn_id} "
                        f"at ({live.x:.0f},{live.y:.0f},{live.z:.0f})",
                        flush=True,
                    )
                    return
                near = _horiz(self.model.position, intention.where) <= _RECLAIM_WALK_RANGE
                self._approach(intention.where, 0, walk=near)
            return
        if kind == "rezz":
            self._accept_pending_rezz()
            return
        where = self._live_where(intention)
        if where is None:
            return
        reach = _ACT_RANGE.get(kind, 8.0)
        in_range = _horiz(self.model.position, where) <= reach
        # Find is an NPC path. A ground drop id is not an entity, and an empty reply just stalls the step.
        guide_id = 0 if kind in ("fetch", "search") else intention.target
        if in_range and kind in ("fetch", "search"):
            pass
        elif in_range and kind in ("task_talk", "hail", "talk", "hand_in"):
            if self._can_see(where) or not self.survey.looping():
                pass
            else:
                self._approach(where, guide_id)
                return
        elif not in_range:
            if kind in ("task_kill", "fight") and self._grind_stuck(intention.target):
                return
            retaliating = (intention.text or "") == "retaliate" or intention.target == self._threat
            # Being hit with LoS: force swing. No LoS → mesh/Find around the blocker
            # (same as grind lost-sight) — never park at hold range spamming ^attack.
            if retaliating and kind in ("fight", "task_kill") and self._in_sight(where):
                self._attack(intention.target, force=True, grind=False)
            elif kind == "fight" and self._grind_mode == "chase" and self._in_sight(where):
                self._chase_visible(intention.target, grind=True)
            elif kind in ("fight", "task_kill") and self._in_sight(where):
                self._grind_mode = "chase"
                self._chase_visible(intention.target, grind=kind == "fight")
            elif kind == "reclaim":
                # Walk from farther out; creep near the pad so bots can lead.
                near = _horiz(self.model.position, where) <= _RECLAIM_WALK_RANGE
                self._approach(where, guide_id, walk=near)
            else:
                # Walk phase / lost LoS (retaliate, finish, task_kill): Find / mesh.
                if kind == "fight":
                    self._grind_mode = "walk"
                self._approach(where, guide_id)
            return
        elif kind in ("task_talk", "hail", "talk", "fetch", "search", "hand_in") and not self._can_see(where):
            self._approach(where, guide_id)
            return
        if kind in ("task_talk", "hail"):
            self._hail(intention.target, intention.name)
            self._keyword(intention)
        elif kind == "talk":
            self._say_keyword(intention.target, intention.name, intention.text)
        elif kind in ("task_kill", "fight"):
            retaliating = (intention.text or "") == "retaliate" or intention.target == self._threat
            if retaliating and self._in_sight(where):
                self._clear_stuck()
                self._attack(intention.target, force=True, grind=False)
                return
            # Lost sight mid-fight / finish / retaliate — mesh around the blocker.
            if self._too_far or not self._in_sight(where):
                self._too_far = False
                if self._grind_stuck(intention.target):
                    return
                if kind == "fight":
                    self._grind_mode = "walk"
                self._approach(where, guide_id)
                return
            self._clear_stuck()
            # Grind: hostiles / wary only — never indifferent (city guards).
            self._attack(intention.target, force=kind == "task_kill", grind=kind == "fight")
        elif kind == "reclaim":
            self._drag_corpse_if_close(intention.target)
            self._loot(intention.target, take_all=True)
        elif kind == "train":
            self._train(intention.target)
        elif kind == "loot":
            self._drag_corpse_if_close(intention.target)
            self._loot(intention.target)
        elif kind in ("fetch", "search"):
            self._pickup(intention.target)
        elif kind == "hand_in":
            self._keyword(intention)
            self._hand_in(intention.target, intention.item_id, intention.text)

    def _live_where(self, intention: Intention) -> tuple[float, float, float] | None:
        """Spawn coordinates from the latest packet. An NPC does not stay on its first point."""
        spawn = self.model.spawns.get(intention.target)
        if spawn is not None and intention.kind in (
            "task_talk", "hail", "talk", "task_kill", "fight", "train", "hand_in", "shop",
            "reclaim", "loot",
        ):
            return (spawn.x, spawn.y, spawn.z)
        return intention.where

    def _with_live_where(self, intention: Intention) -> Intention:
        """Rewrite intention.where from the live spawn so goto/chase track movers."""
        spawn = self.model.spawns.get(intention.target)
        if spawn is None or intention.kind not in (
            "task_talk", "hail", "talk", "task_kill", "fight", "train", "hand_in", "shop",
            "reclaim", "loot",
        ):
            return intention
        live = (spawn.x, spawn.y, spawn.z)
        if intention.where == live:
            return intention
        intention.where = live
        return intention

    def _melee_goal(
        self,
        where: tuple[float, float, float],
        reach: float = _MELEE_RANGE - 0.5,
    ) -> tuple[float, float, float] | None:
        """Point on the melee ring around `where` — never stand on the pad (breaks LOS/^attack)."""
        here = self.model.position
        dist = _horiz(here, where)
        # Already on the ring (not stacked, not far).
        if abs(dist - reach) <= 0.45:
            return None
        if dist < 0.15:
            # Coincident with the mob — step off on a fixed axis.
            return (where[0] + reach, where[1], where[2])
        # Too close → back out; too far → close in. Same formula either way.
        t = reach / dist
        return (
            where[0] + (here[0] - where[0]) * t,
            where[1] + (here[1] - where[1]) * t,
            where[2],
        )

    def _chase_visible(self, spawn_id: int, *, grind: bool = False) -> None:
        """LOS chase — with a group, enter `_attack` at send range so bots pull first."""
        spawn = self.model.spawns.get(spawn_id)
        if spawn is None:
            return
        where = (spawn.x, spawn.y, spawn.z)
        # Drop Find/path to the DB pad — it will not follow a moving NPC.
        if self._guide_for == spawn_id or self._find_for == spawn_id:
            self.guide = []
            self._guide_for = 0
        self.path = []
        self.search.aim = None
        # Soft target every tick; full TargetCommand when close enough to swing.
        self.client.send("OP_TargetMouse", struct.pack("<I", spawn_id))
        self._face(where, force=True)
        dist = _horiz(self.model.position, where)
        grouped = bool(self.party.formed and self.party.spawned)
        if dist <= _MELEE_RANGE + 1.0 or (grouped and dist <= _BOT_SEND_RANGE):
            self._attack(spawn_id, force=not grind, grind=grind)
            return
        # Still far: close toward the bot-hold ring (not all the way into melee).
        reach = _BOT_HOLD_RANGE if grouped else (_MELEE_RANGE - 0.5)
        goal = self._melee_goal(where, reach=reach)
        if goal is not None:
            self._step(goal, direct=True, length=STEP_LOS)

    def _approach(
        self,
        goal: tuple[float, float, float],
        entity_id: int = 0,
        *,
        walk: bool = False,
    ) -> None:
        """Out of reach, ask Find for the glowing path and walk that. The mesh is the fallback.

        Empty Find = target too far — mesh in and retry Find later. Path walked to the end
        = mesh the last yards / interact. Never abandon the Find target on stall; backtrack.
        `walk=True` (near-corpse): 1/3 stride + walk anim so LoS checks keep up.
        """
        label = f"find:{entity_id}" if entity_id else f"walk:{int(goal[0])},{int(goal[1])}"
        stride = STEP_WALK if walk else (STEP_LOS if entity_id else STEP)
        if self._walk_is_stuck(label):
            detour = self._unstick_walk(goal, entity_id=entity_id, label=label)
            if detour is not None:
                self._step(detour, direct=True, length=stride)
                return
        if entity_id and not walk:
            point = self._guide_step(entity_id)
            if point is not None:
                # Find glow is a chase — full run, not the short explore step.
                self._step(point, direct=True, length=STEP_LOS)
                return
            if entity_id in self._find_arrived:
                # At the Find destination (empty because close, or glow walked out) — interact / mesh.
                pass
            elif entity_id in self._find_empty:
                # Empty because too far — mesh in; retry Find as distance drops.
                self._maybe_retry_find(entity_id, goal)
            elif self._guide_for != entity_id:
                self._ask_find(entity_id)
                # Keep walking spawn coords while Find replies — do not stand still.
            elif not self.guide and time.monotonic() - self._find_at < 1.0:
                # Brief wait only; then mesh toward spawn coords.
                pass
        elif entity_id and walk and self._guide_for == entity_id and self.guide:
            # Still follow Find glow, but at walk speed near the body.
            point = self._guide_step(entity_id)
            if point is not None:
                self._step(point, direct=True, length=STEP_WALK)
                return
        here = self.model.position
        dist = _horiz(here, goal)
        combat = bool(
            entity_id
            and not walk
            and entity_id
            in (self._swing_id, self._pursuit, self._focus, self._threat)
        )
        if combat:
            best = self._chase_best_dist.get(entity_id)
            if best is None or dist < best:
                self._chase_best_dist[entity_id] = dist
            elif dist > best + 50.0 and dist > 80.0:
                # Mesh/Find took a wrong corridor — dump it and aim at the live mob.
                print(
                    f"chase repath id={entity_id} dist={dist:.0f} (best {best:.0f})",
                    flush=True,
                )
                self.guide = []
                self._guide_for = 0
                self.path = []
                self.search.aim = None
                self._chase_best_dist[entity_id] = dist
                self._find_empty.discard(entity_id)
                self._find_arrived.discard(entity_id)
                self._step(goal, length=stride)
                return
        # Known combat goal + Find failed/arrived: path at the mob, don't polygon-wander.
        if combat and (
            entity_id in self._find_empty or entity_id in self._find_arrived
        ):
            self._step(goal, length=stride)
            return
        if self.nav is None:
            self._step(goal, length=stride)
            return
        aim = self.search.advance(self.model.position, goal, self.nav.locate, self.nav.links, self.nav.center)
        if self._near(aim) and not self._near(goal):
            # The last yard of this polygon. Stepping at the far goal turns him around.
            if _horiz(self.model.position, aim) <= 0.3:
                poly = self.nav.locate(aim)
                if poly is not None:
                    self.search.visited.add(poly)
                self.search.aim = None
                return
            self._step(aim, direct=True, length=stride)
            return
        self._step(aim, direct=True, length=stride)

    def _maybe_retry_find(self, entity_id: int, goal: tuple[float, float, float]) -> None:
        """After Find said too far, ask again only once we've moved closer or enough time passed."""
        now = time.monotonic()
        # Grind chases retry Find sooner — mesh-only walks miss nearby spawns.
        grind = entity_id and (
            entity_id == self._pursuit or entity_id == self._swing_id or entity_id == self._focus
        )
        wait = 8.0 if grind else 12.0
        if now - self._find_at < wait:
            return
        here = self.model.position
        dist = _horiz(here, goal)
        # Far Find always empties — mesh until inside Find range, then retry.
        if dist > 400:
            far_wait = 45.0 if grind else 60.0
            if now - self._find_at < far_wait:
                return
        self._find_empty.discard(entity_id)
        self._ask_find(entity_id)

    def _ask_find(self, entity_id: int) -> None:
        now = time.monotonic()
        if self.guide and self._guide_for == entity_id:
            return
        grind = entity_id and (
            entity_id == self._pursuit or entity_id == self._swing_id or entity_id == self._focus
        )
        if self._find_for == entity_id and now - self._find_at < (1.25 if grind else 3.0):
            return
        self._find_for = entity_id
        self._find_at = now
        x, y, z = self.model.position
        self.client.send("OP_FindPersonRequest", find_person_request(entity_id, x, y, z))
        spawn = self.model.spawns.get(entity_id)
        print(f"find {spawn.name if spawn is not None else entity_id}", flush=True)

    def _guide_step(self, entity_id: int) -> tuple[float, float, float] | None:
        if entity_id != self._guide_for:
            return None
        if not self.guide:
            if entity_id:
                self._find_arrived.add(entity_id)
            return None
        here = self.model.position
        while self.guide and _horiz(here, self.guide[0]) <= 1.0:
            self.guide.pop(0)
        if not self.guide:
            # Walked every Find waypoint — stop re-asking and finish on mesh / interact.
            self._find_arrived.add(entity_id)
            print(f"path end id={entity_id}", flush=True)
            return None
        dest = self.guide[-1]
        while len(self.guide) > 1 and _behind(here, self.guide[0], dest):
            self.guide.pop(0)
        return self.guide[0]

    def _near(self, goal: tuple[float, float, float]) -> bool:
        return _horiz(self.model.position, goal) <= 1.0

    def _step(
        self,
        goal: tuple[float, float, float],
        avoid: bool = True,
        direct: bool = False,
        length: float | None = None,
    ) -> None:
        """One step from the server's latest coordinates toward goal.

        `length` overrides the usual stride — LOS chases use STEP_LOS to close faster.
        """
        here = self.model.position
        if _on_spot(here, goal, 0.3 if direct else 1.0):
            return
        if not self.model.step_ready():
            return
        goal = self._breath_goal(here, goal)
        swimming = self._should_swim(here, goal)
        if swimming and not self._swimming:
            print("swim", flush=True)
        self._swimming = swimming
        if direct or swimming:
            self.path = [goal]
        if not self.path or _horiz(self.path[-1], goal) > 5.0:
            blocked = self.survey.avoid if avoid else None
            self.path = self.nav.path(here, goal, blocked) if self.nav is not None else [here, goal]
        while self.path and _on_spot(here, self.path[0], 1.0):
            if (direct or swimming) and len(self.path) == 1 and _horiz(here, self.path[0]) > 0.3:
                break
            self.path.pop(0)
        if not self.path:
            if _on_spot(here, goal, 1.0):
                return
            nxt = goal
        else:
            while len(self.path) > 1 and _behind(here, self.path[0], goal):
                self.path.pop(0)
            nxt = self.path[0]
        step = self._choose_step(here, nxt, length=length)
        if step is None:
            return
        step = self._on_floor(here, step, self.path, goal=goal, swimming=swimming)
        for door in doors_along(self.model.doors.values(), here, step, set(self.quests.exits)):
            self._click_door(door.door_id)
        spawn_id = self.model.self_id
        self._send_history()
        # SpeedRun value drives server move rate; near-corpse / reclaim creep = walk anim.
        travel = _horiz(here, step)
        slow = length is not None and length <= STEP_WALK + 1e-6
        if travel < 0.5 and abs(step[2] - here[2]) < 0.5:
            anim = ANIM_STAND
        elif slow:
            anim = ANIM_WALK
        elif length is not None and length >= STEP_LOS - 1e-6:
            anim = ANIM_RUN
        elif travel >= 2.0 or abs(step[2] - here[2]) >= 1.5:
            anim = ANIM_RUN
        else:
            anim = ANIM_WALK
        self.client.send(
            "OP_ClientUpdate",
            client_position(
                spawn_id,
                self.model.next_sequence(),
                step[0],
                step[1],
                step[2],
                here[0],
                here[1],
                here[2],
                heading=eq_heading(here[0], here[1], step[0], step[1]),
                animation=anim,
            ),
        )
        self.model.arm_step(here, step)
        self._pending = (here, step)

    def _should_swim(self, here: tuple[float, float, float], goal: tuple[float, float, float]) -> bool:
        if self.water is None:
            return False
        if self.water.in_liquid(*here) or self.water.in_liquid(*goal):
            return True
        if self._swimming and self.water.surface_z(here[0], here[1]) is not None:
            return True
        return self.water.crosses(here, goal)

    def _underwater(self, here: tuple[float, float, float]) -> bool:
        if self.water is None or not self.water.in_liquid(*here):
            return False
        surf = self.water.surface_z(here[0], here[1])
        return surf is not None and here[2] < surf - 1.5

    def _tick_breath(self, here: tuple[float, float, float]) -> None:
        """Spend air underwater; refill on the surface. Local estimate — profile air is Titanium-only."""
        now = time.monotonic()
        dt = 0.0 if not self._breath_at else min(3.0, now - self._breath_at)
        self._breath_at = now
        if self._underwater(here):
            before = self.model.air
            self.model.air = max(0, int(self.model.air - max(1.0, dt)))
            if before > 15 >= self.model.air and not self._surfaced_warn:
                print(f"breath {self.model.air}s — surfacing", flush=True)
                self._surfaced_warn = True
        else:
            self.model.air = min(60, int(self.model.air + max(2.0, dt * 3)))
            self._surfaced_warn = False

    def _breath_goal(
        self, here: tuple[float, float, float], goal: tuple[float, float, float]
    ) -> tuple[float, float, float]:
        """When air is low, climb to the water surface before the real goal."""
        self._tick_breath(here)
        if self.model.air > 15 or self.water is None:
            return goal
        surf = self.water.surface_z(here[0], here[1])
        if surf is None:
            return goal
        if here[2] >= surf - 1.0:
            return goal
        return (here[0], here[1], surf + 1.0)

    def _choose_step(
        self,
        here: tuple[float, float, float],
        nxt: tuple[float, float, float],
        length: float | None = None,
    ) -> tuple[float, float, float] | None:
        # One-shot length (LOS sprint) does not permanently shorten the normal stride.
        use = float(length) if length is not None else self.step_length
        for _ in range(8):
            step = other_step(here, nxt, self.refused_dirs, use, self.turn_offset)
            if step is None:
                break
            name = self._step_blocked_by(here, step)
            if name is None:
                return step
            print(f"around {name}", flush=True)
            self.refused_dirs.add(bearing(here, step))
        step = None
        if length is not None:
            # LOS stride blocked — fall back to a normal step this tick only.
            use = min(use, STEP)
            self.refused_dirs.clear()
            step = other_step(here, nxt, self.refused_dirs, use, self.turn_offset)
            if step is not None and self._step_blocked_by(here, step) is None:
                return step
            return None
        shorter = next_length(self.step_length)
        self.refused_dirs.clear()
        if shorter is not None:
            self.step_length = shorter
        else:
            self.turn_offset = (self.turn_offset + 22.5) % 360.0
            self.search.block(nxt)
            self.search.aim = None
            self.path = []
        print(f"shorter {self.step_length:.1f}", flush=True)
        step = other_step(here, nxt, self.refused_dirs, self.step_length, self.turn_offset)
        if step is not None and self._step_blocked_by(here, step) is not None:
            return None
        return step

    def _on_floor(self, here, step, path=None, goal=None, swimming: bool = False):
        """Use the navmesh under this step. In water, follow the surface / dive target instead."""
        if swimming and self.water is not None:
            return self._swim_floor(here, step, goal if goal is not None else step)
        # Outdoor zoneline volumes are a Z slab (often above the navmesh). Keep the
        # line height when the goal / step XY is painted RegionTypeZoneLine.
        if self.water is not None and goal is not None and self.water.in_zone_line(*goal):
            if self.water.in_zone_line(step[0], step[1], goal[2]):
                return (step[0], step[1], goal[2])
        mesh = self._mesh_z(step[0], step[1], z_hint=(goal[2] if goal is not None else None))
        # Prefer navmesh floor; if it stays on our flat while the goal is clearly
        # elevated (ramp/hill not picked as nearest), climb toward the goal Z.
        if mesh is None:
            target_z = goal[2] if goal is not None else step[2]
        elif (
            goal is not None
            and abs(goal[2] - mesh) > 4.0
            and abs(mesh - here[2]) < 2.0
            and abs(goal[2] - here[2]) > 3.0
        ):
            target_z = goal[2]
        else:
            target_z = mesh
        centers = list(path or [])
        sample = [(here[0], here[1], here[2]), (step[0], step[1], target_z), *centers[:4]]
        stair = is_stair(sample)
        travel = max(_horiz(here, step), 1.0)
        return (step[0], step[1], _step_height(here[2], target_z, travel, stair))

    def _swim_floor(self, here, step, goal):
        """Hold the water surface, or dive when the goal is deeper than the surface."""
        assert self.water is not None
        surf = self.water.surface_z(step[0], step[1])
        if surf is None:
            # Leaving the water column — snap back toward land mesh if we have one.
            mesh = self._mesh_z(step[0], step[1])
            if mesh is not None:
                return (step[0], step[1], swim_height(here[2], mesh))
            return (step[0], step[1], swim_height(here[2], goal[2]))
        target = goal[2]
        if not self.water.in_liquid(goal[0], goal[1], goal[2]):
            target = surf
        elif goal[2] > surf:
            target = surf
        # Entering from the bank: drop into the surface before crossing.
        if not self.water.in_liquid(*here) and here[2] > surf + 1.0:
            target = surf
        return (step[0], step[1], swim_height(here[2], target))

    def _mesh_z(self, x: float, y: float, z_hint: float | None = None) -> float | None:
        if self.nav is None:
            return None
        # Bias toward the climb target so layered/ramp polys win over the flat we stand on.
        hint = self.model.z if z_hint is None else z_hint
        poly = self.nav.nearest((x, y, hint))
        if poly is None or _horiz((x, y, 0.0), poly.center) > 18.0:
            return None
        return poly.center[2]

    def _step_blocked_by(self, here, step) -> str | None:
        """A box or other ground object standing on this step."""
        for obj in self.model.ground.values():
            if abs(obj.z - here[2]) > 15.0:
                continue
            if blocks_step((obj.x, obj.y), here, step):
                return obj.name or "object"
        for door in self.model.doors.values():
            if door.opened or door.door_id in self.quests.exits:
                continue
            if abs(door.z - here[2]) > 15.0:
                continue
            if blocks_step((door.x, door.y), here, step):
                return door.name or "door"
        return None

    def _settle_move(self) -> None:
        pending = self._pending
        if pending is None:
            return
        origin, asked = pending
        here = self.model.position
        if self.model.step_state == "wait" and not self.model.step_timed_out():
            return
        self._pending = None
        if self.model.step_state == "refused":
            self.model.step_state = ""
            self.refused_dirs.add(bearing(origin, asked))
            self.path = []
            print(
                f"blocked ({asked[0]:.0f}, {asked[1]:.0f}, {asked[2]:.0f}) "
                f"server stayed ({here[0]:.0f}, {here[1]:.0f}, {here[2]:.0f})",
                flush=True,
            )
            return
        # A timeout, or the server still standing on a step we already committed,
        # is not a wall. The point we asked for is where the next step starts.
        if self.model.step_state != "confirmed":
            self.model.commit_step()
            if refused(origin, asked, here):
                self.model.predict(*asked)
            here = self.model.position
        if self.search.aim is None or _horiz(here, self.search.aim) <= 1.5:
            self.refused_dirs.clear()
            self.step_length = STEP
            self.turn_offset = 0.0

    def _send_history(self) -> None:
        """OP_FloatListThing. Without it the zone logs MQGhost on the next move."""
        if not self.model.have_position:
            return
        x, y, z = self.model.position
        self.client.send("OP_FloatListThing", movement_history(x, y, z, int(time.time() * 1000)))

    def _hail(self, spawn_id: int, name: str) -> None:
        token = (_key(name), signature_of(self.tasks.activities), self.model.level)
        if token in self._answered:
            return
        if not self._target(spawn_id):
            return
        before = len(self.client.messages)
        self.client.say("hail")
        self.client.pump(0.3)
        replies = self.client.messages[before:]
        if not replies:
            return
        self.score.hails += 1
        self._remember(name, "say", "hail")
        self._answered.add(token)
        if self.lesson is not None and self.lesson.kind == "talk" and _names_match(name, self.lesson.name):
            self.lesson = None
        self._answer(spawn_id, name, replies)

    def _answer(self, spawn_id: int, name: str, replies: list[str], depth: int = 0) -> None:
        """Pick one option he offered, then answer whatever that reply asks next."""
        if depth > 8:
            return
        offered: list[str] = []
        for reply in replies:
            offered.extend(saylink_words(reply))
        said = {detail for npc, detail in self.said if npc == _key(name)}
        open_steps = {
            (activity.task_id, activity.activity_id)
            for activity in self.tasks.activities
            if not activity.finished and not activity.optional
        }
        for word in reply_order(offered, _script(self.quests, name), open_steps, said):
            signature = signature_of(self.tasks.activities)
            before = len(self.client.messages)
            self._say_keyword(spawn_id, name, word)
            self._answer(spawn_id, name, self.client.messages[before:], depth + 1)
            if signature_of(self.tasks.activities) != signature:
                return

    def _say_keyword(self, spawn_id: int, name: str, keyword: str) -> None:
        if not keyword:
            return
        if not self._target(spawn_id):
            return
        before = len(self.client.messages)
        self.client.say(keyword)
        self.client.pump(0.3)
        self._remember(name, "say", keyword.lower())
        if (
            self.lesson is not None
            and self.lesson.kind == "say"
            and keyword.lower() == self.lesson.text.lower()
        ):
            self.lesson = None
        if len(self.client.messages) > before:
            self.score.keywords += 1

    def _far_poly(self) -> tuple[float, float, float] | None:
        """A distant unvisited polygon, so a search leaves the corner he is pacing."""
        if self.nav is None:
            return None
        here = self.model.position
        self.nav.visited.add(self.nav.locate(here) or (-1, -1))
        fresh = [
            poly.center
            for poly in self.nav.polys
            if (poly.tile, poly.index) not in self.nav.visited and _horiz(poly.center, here) > 30
        ]
        if not fresh:
            self.nav.visited.clear()
            return self.nav.unvisited(here)
        return max(fresh, key=lambda point: _horiz(point, here))

    def _any_mine_mob(self) -> Intention | None:
        best = None
        best_dist = 1e9
        for spawn in self.model.spawns.values():
            if spawn.npc != 1 or self._has_gave_up(spawn.spawn_id) or not _is_mine_mob(spawn.name):
                continue
            dist = _horiz(self.model.position, (spawn.x, spawn.y, spawn.z))
            if dist < best_dist:
                best = spawn
                best_dist = dist
        if best is None:
            return Intention("explore")
        return Intention("task_kill", target=best.spawn_id, name=best.name, where=(best.x, best.y, best.z))

    def _retire(self, spawn_id: int) -> None:
        """A killing blow. The corpse often stays flagged as a live npc."""
        if not spawn_id or spawn_id == self.model.self_id:
            return
        spawn = self.model.spawns.get(spawn_id)
        name = spawn.name if spawn is not None else str(spawn_id)
        if spawn_id not in self._killed:
            self._killed.add(spawn_id)
            print(f"kill {name} id={spawn_id}", flush=True)
            self.score.kills += 1
        self._mark_gave_up(spawn_id, 20.0)
        self._clear_stuck()
        if spawn is not None:
            # 3 = NPC corpse (lootable). 2 = PC corpse — marking 2 hid kills from loot.
            spawn.npc = 3
        self._bot_threats.discard(spawn_id)
        if self._pursuit == spawn_id:
            self._pursuit = 0
        if self._threat == spawn_id:
            self._threat = 0
            self._threat_bot_id = 0
        if self._focus == spawn_id:
            self._focus = 0
        if self._swing_id == spawn_id:
            self._swing_id = 0

    # Stuck / unreachable targets expire so a later approach (new angle, mob moved) can retry.
    GIVE_UP_SECONDS = 45.0

    def _mark_gave_up(self, spawn_id: int, seconds: float | None = None) -> None:
        if not spawn_id:
            return
        wait = self.GIVE_UP_SECONDS if seconds is None else seconds
        self._gave_up[spawn_id] = time.monotonic() + max(0.0, wait)

    def _has_gave_up(self, spawn_id: int) -> bool:
        exp = self._gave_up.get(spawn_id)
        if exp is None:
            return False
        if time.monotonic() >= exp:
            self._gave_up.pop(spawn_id, None)
            self._find_empty.discard(spawn_id)
            return False
        return True

    def _gave_up_skip(self) -> set[int]:
        now = time.monotonic()
        expired = [sid for sid, exp in self._gave_up.items() if now >= exp]
        for sid in expired:
            del self._gave_up[sid]
            self._find_empty.discard(sid)
        return set(self._gave_up)

    def _clear_stuck(self) -> None:
        self._stuck_target = 0
        self._stuck_pos = None
        self._stuck_at = 0.0
        self._stuck_ticks = 0
        self._stuck_check_at = 0.0

    def _clear_walk_stuck(self) -> None:
        self._walk_stuck_key = ""
        self._walk_stuck_pos = None
        self._walk_stuck_at = 0.0
        self._walk_stuck_ticks = 0

    def _walk_is_stuck(self, key: str) -> bool:
        """True when an explore/Find walk has not advanced — target is kept."""
        if not key:
            return False
        here = self.model.position
        now = time.monotonic()
        if key != self._walk_stuck_key:
            self._walk_stuck_key = key
            self._walk_stuck_pos = here
            self._walk_stuck_at = now
            self._walk_stuck_ticks = 0
            return False
        moved = _horiz(here, self._walk_stuck_pos) if self._walk_stuck_pos is not None else 999.0
        if moved > 3.0:
            self._walk_stuck_pos = here
            self._walk_stuck_at = now
            self._walk_stuck_ticks = 0
            return False
        self._walk_stuck_ticks += 1
        return self._walk_stuck_ticks >= 8 or now - self._walk_stuck_at >= 10.0

    def _unstick_walk(
        self,
        goal: tuple[float, float, float] | None,
        *,
        entity_id: int = 0,
        label: str = "",
    ) -> tuple[float, float, float] | None:
        """Backtrack the walk and pick another heading. Find/merchant target stays."""
        here = self.model.position
        tip = label or self._walk_stuck_key or "walk"
        print(f"stuck backtrack {tip} ticks={self._walk_stuck_ticks}", flush=True)
        # Seal the dead heading / waypoint so AreaSearch will not re-pick it.
        if self.search.aim is not None:
            self.search.block(self.search.aim)
        if self.path:
            self.search.block(self.path[0])
            self.refused_dirs.add(bearing(here, self.path[0]))
        if self.guide:
            self.search.block(self.guide[0])
            self.refused_dirs.add(bearing(here, self.guide[0]))
            self.guide.pop(0)
        if goal is not None:
            self.refused_dirs.add(bearing(here, goal))
        self.path = []
        self.search.aim = None
        self.turn_offset = (self.turn_offset + 45.0) % 360.0
        self.step_length = STEP
        # Drop the current polygon so advance() pops the stack and opens a sibling.
        if self.search.stack:
            self.search.stack.pop()
        # Find stays on the same entity — clear empty so a new angle can re-query.
        if entity_id:
            self._find_empty.discard(entity_id)
            self._find_arrived.discard(entity_id)
            self._guide_for = 0
            if not self.guide:
                self._ask_find(entity_id)
        detour = None
        if goal is not None:
            detour = self.survey.new_approach(here, goal)
            if detour is None and self.nav is not None:
                detour = self.search.advance(
                    here, goal, self.nav.locate, self.nav.links, self.nav.center
                )
        if detour is None:
            detour = self._far_poly()
        self._walk_stuck_pos = here
        self._walk_stuck_at = time.monotonic()
        self._walk_stuck_ticks = 0
        return detour

    def _pull_holding(self, target_id: int) -> bool:
        """True while parked waiting for bots to draw first aggro."""
        if not target_id or not self.party.formed or not self.party.spawned:
            return False
        if self._bot_attack_for != target_id or self._bot_pull_at <= 0:
            return False
        if target_id in self._bot_threats:
            return False
        # Being chewed — owner may break the hold.
        max_hp = self.model.max_hp or 0
        if max_hp > 0 and self.model.hp * 100 < max_hp * 98:
            return False
        spawn = self.model.spawns.get(target_id)
        if spawn is None or spawn.npc != 1:
            return False
        dist = _horiz(self.model.position, (spawn.x, spawn.y, spawn.z))
        return dist <= _BOT_SEND_RANGE + 10.0

    def _grind_stuck(self, target_id: int) -> bool:
        """True when a grind chase hasn't moved — abandon and repath.

        Sitting still to regen is not stuck — freeze the clock across rests.
        """
        if not target_id:
            return False
        here = self.model.position
        now = time.monotonic()
        if self._sitting:
            # Slide the window so held time excludes the sit.
            if self._stuck_at > 0 and self._stuck_check_at > 0:
                self._stuck_at += now - self._stuck_check_at
            self._stuck_check_at = now
            return False
        # Bot-first pull: standing at hold range waiting for ^attack engage is not stuck.
        if self._pull_holding(target_id):
            if self._stuck_at > 0 and self._stuck_check_at > 0:
                self._stuck_at += now - self._stuck_check_at
            self._stuck_check_at = now
            self._stuck_ticks = 0
            return False
        if target_id != self._stuck_target or self._stuck_at <= 0:
            self._stuck_target = target_id
            self._stuck_pos = here
            self._stuck_at = now
            self._stuck_ticks = 0
            self._stuck_check_at = now
            return False
        moved = _horiz(here, self._stuck_pos) if self._stuck_pos is not None else 999.0
        if moved > 4.0:
            self._stuck_pos = here
            self._stuck_at = now
            self._stuck_ticks = 0
            self._stuck_check_at = now
            return False
        # Same pad after a rest gap: keep wall-clock, just count this resume tick.
        self._stuck_ticks += 1
        self._stuck_check_at = now
        spawn = self.model.spawns.get(target_id)
        dist = _horiz(here, (spawn.x, spawn.y, spawn.z)) if spawn is not None else 0.0
        # In melee (or still being chewed on) is not "stuck" — finish the swing.
        if dist <= _MELEE_RANGE + 10:
            self._stuck_pos = here
            self._stuck_at = now
            self._stuck_ticks = 0
            return False
        if self._swing_id == target_id and self.model.hp < max(1, self._hp_at_swing - 1):
            self._stuck_at = now
            self._stuck_ticks = 0
            return False
        # Parked on purpose for bot-first pull — not stuck.
        if self._pull_holding(target_id) or (
            self.party.formed
            and target_id not in self._bot_threats
            and target_id in (self._threat, self._pursuit, self._reclaim_held_for)
        ):
            self._stuck_pos = here
            self._stuck_at = now
            self._stuck_ticks = 0
            return False
        finding = self._guide_for == target_id or self._find_for == target_id
        if dist > _SIGHT_RANGE or finding:
            need_ticks, need_time = 40, 45.0
        else:
            need_ticks, need_time = 12, 18.0
        if self._stuck_ticks < need_ticks and now - self._stuck_at < need_time:
            return False
        name = spawn.name if spawn is not None else str(target_id)
        print(
            f"stuck leave {name} id={target_id} ticks={self._stuck_ticks} "
            f"dist={dist:.0f} held={now - self._stuck_at:.0f}s",
            flush=True,
        )
        self._mark_gave_up(target_id)
        self._focus = 0
        self._pursuit = 0
        self._swing_id = 0
        self._grind_mode = ""
        self._grind_walk_until = 0.0
        self.path = []
        self.guide = []
        self._guide_for = 0
        self._find_for = 0
        self._find_empty.add(target_id)
        self._clear_stuck()
        return True

    def _xp_line(self) -> str:
        """OP_ExpUpdate is a 0–330 bar through the current level — show %, level, bar."""
        level = int(self.model.level or 0)
        bar = max(0, min(330, int(getattr(self.model, "exp_bar", 0) or 0)))
        pct = 100.0 * bar / 330.0
        return f"xp L{level} {pct:.1f}% ({bar}/330)"

    def _grind_why(self) -> str:
        """Active campaign grind goal — level gate or farm item. Never goal-less."""
        if self._grind_label:
            return self._grind_label
        from eqclient.plan import grind_why

        if self._grind_to:
            return grind_why(self._grind_to)
        return "grind"

    def _note_grind_goal(self, text: str = "", item_id: int = 0) -> None:
        raw = str(text or "").strip()
        if raw.startswith("grind to") or raw.startswith("farm") or raw.startswith("grind for"):
            self._grind_label = raw
        tip = raw
        if tip.lower().startswith("grind to l"):
            tip = tip[10:]
        elif tip.lower().startswith("grind to "):
            tip = tip[9:]
        tip = tip.strip().lstrip("Ll").split()[0] if tip.strip() else ""
        if tip.isdigit():
            self._grind_to = int(tip)
            if not self._grind_label:
                from eqclient.plan import grind_why

                self._grind_label = grind_why(self._grind_to, item_id=item_id)
        elif item_id and not self._grind_label:
            from eqclient.plan import grind_why

            self._grind_label = grind_why("farm", item_id=item_id, kind="farm")

    def _next_grind_fight(self) -> Intention | None:
        from eqclient.plan import _xp_foe

        foe = _xp_foe(
            self.model,
            skip=self._gave_up_skip() | self._protected_spawn_ids(),
            can_see=self._in_sight,
        )
        if foe is None:
            return None
        return Intention(
            "fight",
            target=foe.spawn_id,
            name=foe.name,
            where=(foe.x, foe.y, foe.z),
            text=self._grind_why(),
        )

    @staticmethod
    def _pad_key(x: float, y: float) -> tuple[int, int]:
        return (int(x // _GRIND_PAD_CELL), int(y // _GRIND_PAD_CELL))

    def _note_grind_pad(self, x: float, y: float) -> None:
        """Remember a spawn pad so we do not bounce back within the last five."""
        key = self._pad_key(x, y)
        if self._grind_pads and self._grind_pads[-1] == key:
            return
        self._grind_pads.append(key)
        while len(self._grind_pads) > _GRIND_PAD_MEMORY:
            self._grind_pads.pop(0)

    def _pad_recent(self, x: float, y: float) -> bool:
        return self._pad_key(x, y) in self._grind_pads

    def _grind_skip_pads(self) -> set[int]:
        """Spawn ids whose live/pad coords sit on a recently visited pad cell."""
        skip: set[int] = set()
        if not self._grind_pads:
            return skip
        recent = set(self._grind_pads)
        for spawn in self.model.spawns.values():
            if spawn.npc != 1:
                continue
            if self._pad_key(spawn.x, spawn.y) in recent:
                skip.add(spawn.spawn_id)
        return skip

    def _on_spawn_pad(self, spawn) -> bool:
        return _horiz(self.model.position, (spawn.x, spawn.y, spawn.z)) <= _GRIND_PAD_REACH

    def _grind_fight_of(self, foe, *, text: str | None = None) -> Intention:
        return Intention(
            "fight",
            target=foe.spawn_id,
            name=foe.name,
            where=(foe.x, foe.y, foe.z),
            text=text or self._grind_why(),
        )

    def _grind_walk_commit(self, dist: float) -> float:
        """How long to stay on a spawn-walk before the next LOS rescan."""
        if dist >= _GRIND_WALK_FAR_YD:
            return _GRIND_WALK_SECS_FAR
        return _GRIND_WALK_SECS

    def _grind_cycle(self, intention: Intention) -> Intention:
        """Scan 8-LOS → chase; else walk closest spawn; empty pad → next pad.

        LOS always runs (even mid-walk) so nearby fights are not invisible.
        Walk commit only skips re-picking a far pad / re-asking Find.
        """
        from eqclient.plan import _xp_foe

        now = time.monotonic()
        why = intention.text or self._grind_why()
        skip = self._gave_up_skip() | self._protected_spawn_ids()
        walking = self._grind_mode == "walk" and self._grind_walk_until > now

        # --- Sight first: interrupt walk when something in-band is actually visible ---
        seen = _xp_foe(
            self.model,
            skip=skip,
            can_see=self._in_sight,
            sight_only=True,
        )
        if seen is not None:
            same = self._grind_mode == "chase" and self._pursuit == seen.spawn_id
            if not same:
                print(
                    f"grind los hit {seen.name} id={seen.spawn_id} "
                    f"L{int(getattr(seen, 'level', 0) or 0)} "
                    f"dist={_horiz(self.model.position, (seen.x, seen.y, seen.z)):.0f}",
                    flush=True,
                )
            self._grind_mode = "chase"
            self._grind_walk_until = 0.0
            self._pursuit = seen.spawn_id
            self.guide = []
            self._guide_for = 0
            self._find_arrived.discard(seen.spawn_id)
            self._find_empty.discard(seen.spawn_id)
            self.path = []
            return self._grind_fight_of(seen, text=why)

        # --- Committed walk: keep the same pad without re-logging ---
        cur = self.model.spawns.get(self._pursuit) if self._pursuit else None
        if walking and cur is not None and cur.npc == 1 and cur.spawn_id not in skip:
            if self._on_spawn_pad(cur) and not self._in_sight((cur.x, cur.y, cur.z)):
                self._note_grind_pad(cur.x, cur.y)
                self._grind_walk_until = 0.0
                print(
                    f"grind empty pad {cur.name} id={cur.spawn_id} "
                    f"at ({cur.x:.0f},{cur.y:.0f})",
                    flush=True,
                )
            else:
                if self._grind_stuck(cur.spawn_id):
                    return intention
                return self._grind_fight_of(cur, text=why)

        # Renew existing walk target after commit expired / rest, without Find spam.
        if (
            cur is not None
            and cur.npc == 1
            and cur.spawn_id not in skip
            and self._grind_mode == "walk"
        ):
            if self._on_spawn_pad(cur) and not self._in_sight((cur.x, cur.y, cur.z)):
                self._note_grind_pad(cur.x, cur.y)
                self._grind_walk_until = 0.0
                print(
                    f"grind empty pad {cur.name} id={cur.spawn_id} "
                    f"at ({cur.x:.0f},{cur.y:.0f})",
                    flush=True,
                )
            else:
                dist = _horiz(self.model.position, (cur.x, cur.y, cur.z))
                self._grind_walk_until = now + self._grind_walk_commit(dist)
                if self._grind_stuck(cur.spawn_id):
                    return intention
                return self._grind_fight_of(cur, text=why)

        # --- Pick a walk target (only log / Find when the id actually changes) ---
        pad_skip = self._grind_skip_pads()
        foe = _xp_foe(self.model, skip=skip | pad_skip, can_see=None)
        if foe is None and pad_skip:
            if self._grind_pads:
                self._grind_pads.pop(0)
            pad_skip = self._grind_skip_pads()
            foe = _xp_foe(self.model, skip=skip | pad_skip, can_see=None)
        if foe is None:
            foe = _xp_foe(self.model, skip=skip, can_see=None)
        if foe is None:
            return intention

        new_target = self._pursuit != foe.spawn_id
        dist = _horiz(self.model.position, (foe.x, foe.y, foe.z))
        self._grind_mode = "walk"
        self._pursuit = foe.spawn_id
        self._grind_walk_until = now + self._grind_walk_commit(dist)
        if new_target:
            self.guide = []
            self._guide_for = 0
            self._find_arrived.discard(foe.spawn_id)
            self._find_empty.discard(foe.spawn_id)
            self.path = []
            self._clear_stuck()
            self._ask_find(foe.spawn_id)
            print(
                f"grind walk {foe.name} id={foe.spawn_id} "
                f"L{int(getattr(foe, 'level', 0) or 0)} "
                f"dist={dist:.0f} "
                f"pads={len(self._grind_pads)}",
                flush=True,
            )
        elif (
            foe.spawn_id not in self._find_empty
            and foe.spawn_id not in self._find_arrived
            and not self.guide
            and self._find_for != foe.spawn_id
            and now - self._find_at >= 8.0
        ):
            # Rare Find refresh only — never every few seconds on the same pad.
            self._ask_find(foe.spawn_id)
        if self._grind_stuck(foe.spawn_id):
            return intention
        return self._grind_fight_of(foe, text=why)

    def _lootable_corpse(self):
        """Nearest NPC corpse we or the bots dropped — never our own PC corpse."""
        from eqclient.plan import _grind_corpse

        here = self.model.position
        me = (self.model.character or "").lower()
        best = None
        best_dist = 80.0
        for spawn_id in self.attacked | self._killed:
            if spawn_id in self.skipped_corpses:
                continue
            spawn = self.model.spawns.get(spawn_id)
            # npc==3 NPC corpse; skip PC corpses (2) — those are reclaim-only.
            if spawn is None or spawn.npc != 3:
                continue
            if me and me in (spawn.name or "").lower():
                continue
            dist = _horiz(here, (spawn.x, spawn.y, spawn.z))
            if dist < best_dist:
                best = spawn
                best_dist = dist
        if best is not None:
            return best
        # Bots may drop corpses we never swung on — loot any nearby NPC corpse.
        return _grind_corpse(self.model, self.skipped_corpses)

    def _nearby_loot_intention(self) -> Intention | None:
        """Loot a corpse within reach before rest/reclaim/retaliate.

        Skip if we are mid-swing on a live mob in melee — finish that hit first.
        Always attempt for coin — bag space only limits item picks inside `_loot`.
        """
        corpse = self._lootable_corpse()
        if corpse is None:
            return None
        here = self.model.position
        # Recent kills: a bit more reach so we bag before medding/reclaim.
        reach = 40.0 if corpse.spawn_id in self._killed else 25.0
        if _horiz(here, (corpse.x, corpse.y, corpse.z)) > reach:
            return None
        if self._swing_id:
            swinging = self.model.spawns.get(self._swing_id)
            if (
                swinging is not None
                and swinging.npc == 1
                and _horiz(here, (swinging.x, swinging.y, swinging.z)) <= 20.0
            ):
                return None
        return Intention(
            "loot",
            target=corpse.spawn_id,
            name=corpse.name,
            where=(corpse.x, corpse.y, corpse.z),
            text=self._grind_why(),
        )

    def _bot_spawns(self) -> list:
        """Live roster bots only — corpses (npc 2/3 or name) must not count as party."""
        me = (self.model.character or "").lower()
        live = []
        for spawn in self.model.spawns.values():
            if spawn.npc != 0:
                continue
            namel = (spawn.name or "").lower()
            if "corpse" in namel or namel == me or not namel.startswith("moc"):
                continue
            live.append(spawn)
        return live

    def _spawn_by_entity(self, entity_id: int):
        if not entity_id:
            return None
        short = entity_id & 0xFFFF
        spawn = self.model.spawns.get(entity_id) or self.model.spawns.get(short)
        if spawn is not None:
            return spawn
        return next(
            (
                s
                for s in self.model.spawns.values()
                if (s.spawn_id & 0xFFFF) == short
            ),
            None,
        )

    def _is_corpse_spawn(self, spawn) -> bool:
        if spawn is None:
            return False
        if spawn.npc in (2, 3):
            return True
        return "corpse" in (spawn.name or "").lower()

    def _forget_combat_spawn(self, spawn_id: int) -> None:
        """Drop swing/threat interest when an entity becomes a corpse."""
        if not spawn_id:
            return
        short = spawn_id & 0xFFFF
        for sid in (spawn_id, short):
            self._bot_threats.discard(sid)
            self.attacked.discard(sid)
            if self._threat == sid:
                self._threat = 0
                self._threat_bot_id = 0
            if self._pursuit == sid:
                self._pursuit = 0
            if self._swing_id == sid:
                self._swing_id = 0
            if self._focus == sid:
                self._focus = 0
            if self._bot_attack_for == sid:
                self._bot_attack_for = 0

    def _party_member_spawn(self, spawn_id: int):
        """Live PC/bot group member for this spawn id, else None."""
        me = self.model.self_id & 0xFFFF
        if not spawn_id or (spawn_id & 0xFFFF) == me:
            return None
        spawn = self.model.spawns.get(spawn_id) or next(
            (
                s
                for s in self.model.spawns.values()
                if (s.spawn_id & 0xFFFF) == (spawn_id & 0xFFFF)
            ),
            None,
        )
        if spawn is None or spawn.npc in (1, 2, 3):
            return None
        name = spawn.name or ""
        key = _key(name)
        if key in self._known_names or name.lower().startswith("moc"):
            return spawn
        if name in getattr(self.party, "spawned", ()):
            return spawn
        return None

    def _note_party_health(self, spawn_id: int, hp_pct: int) -> None:
        """Group CreateHPPacket → OP_MobHealth. Print when a member goes critical."""
        member = self._party_member_spawn(spawn_id)
        if member is None:
            return
        prev = self._party_hp.get(spawn_id)
        self._party_hp[spawn_id] = hp_pct
        # Critical band matches healrotation critical=50% / safe=75%.
        if hp_pct <= 50 and (prev is None or prev > 50):
            print(f"party critical {member.name} hp={hp_pct}%", flush=True)
        elif hp_pct <= 75 and (prev is None or prev > 75) and hp_pct > 50:
            print(f"party low {member.name} hp={hp_pct}%", flush=True)
        elif prev is not None and prev <= 50 and hp_pct > 75:
            print(f"party ok {member.name} hp={hp_pct}%", flush=True)

    def _cleric_bot_name(self) -> str:
        """Roster cleric name (Mocclr), else empty."""
        for name, class_id in self.party.roster:
            if class_id == 2 and name in self.party.spawned:
                return name
        return next((name for name, class_id in self.party.roster if class_id == 2), "")

    def _needs_mana_rest(self) -> bool:
        """Pause when cleric mana ≤25%; stay parked until nearly full (mirrors HP rest).

        Arm `_cleric_medding` as soon as mana trips low — even before we sit — so a
        mid-walk botreport of 26% cannot cancel rest and resume reclaim.
        """
        if self._cleric_mana is None:
            return False
        if self._cleric_mana <= 0.25:
            self._cleric_medding = True
        if self._cleric_medding or self._sitting:
            if self._cleric_mana >= 0.9:
                self._cleric_medding = False
                return False
            return True
        return False

    def _prune_party_hp(self) -> None:
        """Drop MobHealth rows for despawned ids (stale 19% ghosts keep us resting forever)."""
        dead = [sid for sid in self._party_hp if self._party_member_spawn(sid) is None]
        for sid in dead:
            del self._party_hp[sid]

    # Cleric + pure casters (healrotation / no-melee set). Druids heal too — treat as support.
    _RECLAIM_CASTER_CLASSES = frozenset({2, 6, 10, 11, 12, 13, 14})

    def _bot_hp_pct(self, name: str) -> int | None:
        """Last known hp% for a roster bot, or None if unseen."""
        spawn = self._bot_spawn_named(name) or self._spawn_named(name)
        if spawn is None:
            return None
        sid = spawn.spawn_id
        if sid in self._party_hp:
            return self._party_hp[sid]
        short = sid & 0xFFFF
        return self._party_hp.get(short)

    def _reclaim_support_hold(self) -> str | None:
        """Hard-stop reclaim only for missing or critical support.

        Distance/leash no longer pauses the corpse walk — on sight/aggro we
        `botsummon` instead of waiting for follow.
        """
        if not self.party.formed:
            return None
        clerics = [n for n, c in self.party.roster if c == 2 and n in self.party.spawned]
        if not clerics:
            return "no cleric spawned"
        for name in clerics:
            spawn = self._bot_spawn_named(name) or self._spawn_named(name)
            if spawn is None:
                return f"cleric missing {name}"
            hp = self._bot_hp_pct(name)
            if hp is not None and hp <= 50:
                return f"cleric critical {name} {hp}%"
        for name, cid in self.party.roster:
            if cid not in self._RECLAIM_CASTER_CLASSES or cid == 2:
                continue
            if name not in self.party.spawned:
                continue
            hp = self._bot_hp_pct(name)
            if hp is not None and hp <= 50:
                return f"caster critical {name} {hp}%"
        return None

    def _party_needs_rest(self) -> bool:
        """True while any live grouped member is at/under healrotation critical (50%).

        Sit until nobody is critical so the cleric can catch up before the next pull.
        """
        self._prune_party_hp()
        if not self._party_hp:
            return False
        return any(hp <= 50 for hp in self._party_hp.values())

    def _on_buff_packet(self, payload: bytes) -> None:
        """Track disease/poison/curse counters on us or our bots (OP_Buff)."""
        # Titanium SpellBuffPacket_Struct: entity@0, buff@4 (20 bytes), slot@24, fade@28.
        entity = struct.unpack_from("<I", payload, 0)[0] & 0xFFFF
        spell_id = struct.unpack_from("<I", payload, 8)[0]
        counters = struct.unpack_from("<I", payload, 16)[0]
        bufffade = struct.unpack_from("<I", payload, 28)[0]
        if not spell_id or spell_id == 0xFFFFFFFF:
            return
        me = (self.model.self_id or 0) & 0xFFFF
        bot_ids = {spawn.spawn_id & 0xFFFF for spawn in self._bot_spawns()}
        if entity not in {me} | bot_ids:
            return
        # Counters > 0 → disease/poison/curse (rune also uses counters; cure no-ops).
        if bufffade or counters <= 0:
            if spell_id in self._cure_spells:
                self._cure_spells.pop(spell_id, None)
                print(f"cure cleared spell={spell_id}", flush=True)
            return
        before = spell_id in self._cure_spells
        self._cure_spells[spell_id] = counters
        if not before:
            who = "self" if entity == me else f"id={entity}"
            print(f"diseased {who} spell={spell_id} counters={counters}", flush=True)
            self._maybe_cure(force=True)

    def _maybe_cure(self, *, force: bool = False) -> None:
        """Have clerics ^cast groupcures/cures when disease/poison/curse is up."""
        if not self._cure_spells or not self.party.formed or self.model.hp <= 0:
            return
        # Never TargetMouse self while locking an enemy for ^attack.
        if self._locking_attack_target:
            return
        now = time.monotonic()
        if not force and now - self._cure_at < 5.0:
            return
        clr = self._cleric_bot_name()
        if not clr or clr not in self.party.spawned:
            return
        if self._cleric_mana is not None and self._cleric_mana < 0.10:
            return
        me_id = (self.model.self_id or 0) & 0xFFFF
        if not me_id:
            return
        self._cure_at = now
        if not self._bots_close(60):
            self.client.command("botsummon spawned")
            self.client.pump(0.3)
        self.client.send("OP_TargetMouse", struct.pack("<I", me_id))
        self.client.pump(0.15)
        # Group cure first (diseased bots + us), then single-target cure on self.
        mark = len(self.client.messages)
        self.client.command("cast groupcures")
        self.client.pump(0.35)
        self.client.command(f"cast cures byname {clr}")
        self.client.pump(0.5)
        self._party_messages()
        blob = " ".join(self.client.messages[mark:]).lower()
        spells = ",".join(str(s) for s in sorted(self._cure_spells))
        if "doesn't have anything that needs to be cured" in blob:
            self._cure_spells.clear()
            print(f"cure none needed (cleared {spells})", flush=True)
            return
        print(f"cure requested {clr} spells=[{spells}]", flush=True)

    def _maybe_emergency_heal(self) -> None:
        """Commanded RegularHeal when HR is silent and we are critically low.

        ^cast ignores holds/delays/thresholds. Target self so the heal lands on us.
        """
        if not self.party.formed or self.model.hp <= 0:
            return
        if self._locking_attack_target:
            return
        max_hp = self.model.max_hp or 0
        if max_hp <= 0 or self.model.hp * 100 >= max_hp * 55:
            return
        now = time.monotonic()
        if now - self._emergency_heal_at < 2.5:
            return
        clr = self._cleric_bot_name()
        if not clr or clr not in self.party.spawned:
            return
        # Don't spam ^cast while the cleric is OOM — "No bots are capable" noise.
        if self._cleric_mana is not None and self._cleric_mana < 0.15:
            return
        if self._cleric_medding:
            return
        me_id = (self.model.self_id or 0) & 0xFFFF
        if not me_id:
            return
        self._emergency_heal_at = now
        # Pull cleric into range if they drifted; then force a heal on us.
        if not self._bots_close(60):
            self.client.command("botsummon spawned")
            self.client.pump(0.3)
        self.client.send("OP_TargetMouse", struct.pack("<I", me_id))
        self.client.pump(0.15)
        # Bare ^cast 17 is spell *type* Hate Reduction — not Light Healing (spells_new #17).
        # Prefer type RegularHeal; spellid is the explicit spells_new path.
        self.client.command(f"cast regularheals byname {clr}")
        self.client.pump(0.1)
        self.client.command(f"cast spellid 17 byname {clr}")
        print(
            f"emergency heal {clr} → self hp={self.model.hp}/{max_hp} (regularheals + spellid 17)",
            flush=True,
        )
        # Keep tanks locked on the mob so they can peel aggro off us.
        if self._swing_id:
            self.client.send("OP_TargetMouse", struct.pack("<I", self._swing_id & 0xFFFF))
            self.client.pump(0.1)
            for name, cid in self.party.roster:
                if cid not in (1, 3) or name not in self.party.spawned:
                    continue
                self.client.command(f"attack byname {name}")
                self.client.pump(0.05)
            self._enable_tank_taunt()

    def _maybe_bot_report(self) -> None:
        """Periodic ^botreport: cleric mana always; all bots while party-resting (live HP%)."""
        if not self.party.formed:
            return
        clr = self._cleric_bot_name()
        if not clr:
            return
        now = time.monotonic()
        # Faster polls while medding / mana-low / party-crit; otherwise every ~20s.
        last = getattr(self, "_last_act", "") or ""
        party_hurt = self._party_needs_rest() or (self._sitting and last.startswith("rest party"))
        mana_low = self._needs_mana_rest() or (self._sitting and last.startswith("rest mana"))
        wait = 5.0 if (self._sitting or self._cleric_medding or party_hurt or mana_low) else 20.0
        if now - self._bot_report_at < wait:
            return
        self._bot_report_at = now
        # spawned = live HP for every bot (MobHealth often goes quiet during sit regen).
        cmd = "botreport spawned" if party_hurt else f"botreport byname {clr}"
        try:
            self.client.command(cmd)
        except Exception:
            return
        self.client.pump(0.4)
        self._party_messages()

    def _bots_close(self, radius: float = 30) -> bool:
        bots = self._bot_spawns()
        if len(bots) < 3:
            return True
        here = self.model.position
        near = sum(1 for bot in bots if _horiz(here, (bot.x, bot.y, bot.z)) <= radius)
        return near >= 3

    def _bot_anchor(self) -> tuple[float, float, float] | None:
        """The nearest bot, so a split raid does not average out to an empty tunnel."""
        bots = self._bot_spawns()
        if not bots:
            return None
        here = self.model.position
        bot = min(bots, key=lambda spawn: _horiz(here, (spawn.x, spawn.y, spawn.z)))
        return (bot.x, bot.y, bot.z)

    def _next_wanted(self) -> Intention | None:
        """Nearest live mob named by any open kill step."""
        best = None
        best_dist = 1e9
        for spawn in self.model.spawns.values():
            if spawn.npc != 1 or self._has_gave_up(spawn.spawn_id):
                continue
            if not _kill_still_wanted(self.tasks, spawn.name):
                continue
            dist = _horiz(self.model.position, (spawn.x, spawn.y, spawn.z))
            if dist < best_dist:
                best = spawn
                best_dist = dist
        if best is None:
            return None
        return Intention("task_kill", target=best.spawn_id, name=best.name, where=(best.x, best.y, best.z))

    def _other_kill(self, name: str) -> Intention | None:
        """Another live mob for this kill step, after the last one was counted."""
        best = None
        best_dist = 1e9
        for spawn in self.model.spawns.values():
            if spawn.npc != 1 or self._has_gave_up(spawn.spawn_id) or not _names_match(spawn.name, name):
                continue
            dist = _horiz(self.model.position, (spawn.x, spawn.y, spawn.z))
            if dist < best_dist:
                best = spawn
                best_dist = dist
        if best is None:
            return None
        return Intention("task_kill", target=best.spawn_id, name=best.name, where=(best.x, best.y, best.z))

    def _under_fire(self) -> bool:
        """True when something is hitting us / bots — social invites must wait."""
        if self.model.hp <= 0:
            return True
        if self._live_bot_threats():
            return True
        if self._engaged():
            return True
        max_hp = self.model.max_hp or 0
        if max_hp > 0 and self.model.hp * 100 < max_hp * 98:
            return True
        return False

    def _conduct(self, intention: Intention | None) -> Intention | None:
        """Tells, hunger, and a class opener. A fight already chosen stays a fight."""
        if intention is not None and intention.kind in ("fight", "grind", "loot"):
            self._note_grind_goal(intention.text, intention.item_id)
        # Never follow a PC while mobs are chewing on us.
        if self._leader and not self._under_fire():
            leader = self._spawn_named(self._leader)
            if leader is not None and not self._engaged():
                return Intention("explore", name="follow", target=leader.spawn_id, where=(leader.x, leader.y, leader.z))
        if self._orders:
            peek = self._orders[0]
            # Invite/camp pumps used to eat the whole tick while zombies finished us.
            if peek.verb in {"invite", "join", "group", "party"} and self._under_fire():
                print(f"invite defer (under fire) {peek.sender}", flush=True)
            else:
                ordered = self._order_intention(self._orders.pop(0))
                if ordered is not None:
                    return ordered
        if not self._engaged() and not self._under_fire():
            if intention is not None and intention.kind == "reclaim":
                hold = self._reclaim_support_hold()
                if hold is not None:
                    self._rally_bots(force=True, why="reclaim support")
                    print(f"reclaim hold → {hold}", flush=True)
                    return Intention("rest", name="party")
                # Corpse coin first — never park reclaim on inventorygive churn.
                # Free the cursor only; bag→bot gear waits until after reclaim.
                if self.inventory.cursor() is not None:
                    self._settle_gear(passes=2)
                self._gear_reclaim_stall = 0
                self._gear_reclaim_skip = False
                return intention
            # Equip / inventorygive before vendors / grind (not while reclaiming).
            self._settle_gear()
        elif self.inventory.cursor() is not None and (self._engaged() or self._under_fire()):
            self._stow_cursor(timeout=0.3)
            if self.model.needs_corpse or self.journal.outstanding_corpses(self.model.character) > 0:
                if intention is not None and intention.kind in ("shop", "bank"):
                    intention = None
                # Fall through: feet-loot / reclaim coords still win below when guide lost the flag.
            else:
                # Sell junk before loot when full, or when general slots hold trash instead of bags.
                if self._inventory_needs_sell():
                    sold = self._sell_trash_intent()
                    if sold is not None:
                        return sold
                # Only buy backpacks into a free general slot (never with a full bag bar).
                bagged = self._bag_intent()
                if bagged is not None:
                    return bagged
            corpse = self._lootable_corpse()
            if (
                corpse is not None
                and (intention is None or intention.kind in ("fight", "grind", "explore", "loot", "rest", "reclaim", "shop"))
            ):
                why = (
                    intention.text
                    if intention is not None and str(intention.text or "").startswith("grind")
                    else self._grind_why()
                )
                return Intention(
                    "loot",
                    target=corpse.spawn_id,
                    name=corpse.name,
                    where=(corpse.x, corpse.y, corpse.z),
                    text=why,
                )
            need = bar_needed(self.model.food, self.model.water)
            if need and self._stack(need) is not None:
                return Intention("eat", name=need)
            # After pulls: bags full → stow (rate-limited), sell trash, or nearby bank.
            if not has_loot_room(self.inventory):
                now = time.monotonic()
                if now - getattr(self, "_stow_try_at", 0.0) >= 2.0:
                    self._stow_try_at = now
                    self._make_room_for_loot()
                if not has_loot_room(self.inventory):
                    sold = self._sell_trash_intent()
                    if sold is not None:
                        return sold
                    banker = self._spawn_by_substring("bank")
                    if banker is not None and _horiz(self.model.position, (banker.x, banker.y, banker.z)) < 80:
                        return Intention("bank", target=banker.spawn_id, name=banker.name, where=(banker.x, banker.y, banker.z))
        if (
            intention is not None
            and intention.target
            and intention.target not in self.model.spawns
            and self._skills.get(53, 0) > 0
        ):
            return Intention("track", name=intention.name, target=intention.target, where=intention.where)
        needed = self._needed_items()
        if needed and not self._engaged():
            book = self._recipe_book()
            recipe_id = craft_for(needed, self._held_counts(), book.craft_list(), book=book)
            if recipe_id and not self._recipe_deferred(recipe_id):
                return Intention("craft", target=recipe_id)
        if intention is not None and intention.kind in ("task_kill", "fight"):
            tactic = fight_tactic(self.model.class_id, bool(self._grouped or self._leader))
            role = opener(tactic)
            if role in self._gems:
                return Intention("cast", name=role, target=intention.target, where=intention.where)
            if not may_melee(tactic, self._rooted, self._snared, self._slowed, self._hp_ratio()):
                return Intention("explore", name="kite", where=self._away(intention.where))
        if intention is None or intention.kind in ("explore", "grind", "rest", "task_kill", "fight"):
            ability = ability_for(
                self.model.class_id,
                self._skills,
                hungry=bool(bar_needed(self.model.food, self.model.water)) and self._stack("food") is None,
                in_fight=self._engaged(),
                leaving=intention is not None and intention.name == "safe",
                broke=self.model.points < 0,
            )
            if ability:
                self._ability(ability)
            # Passive skill-ups on the grind (forage / sense / track / languages / …).
            self._practice_skills(
                resting=intention is not None and intention.kind == "rest",
                fighting=self._engaged(),
            )
        if intention is not None and intention.kind == "rest":
            self._stack_coin()
            self._tidy()
        return intention

    def _order_intention(self, order) -> Intention | None:
        sender = order.sender
        self._known_names.add(_key(sender))
        if order.verb in {"invite", "join", "group", "party"}:
            target = order.rest.strip() if order.verb == "invite" and order.rest.strip() else sender
            self._invite_player(target)
            return None
        if order.verb in {"farm", "goal", "get", "obtain"}:
            parsed = farm_target(order.rest)
            if parsed is None:
                self.client.tell(sender, "usage: farm <item_id> [count]")
                return None
            item_id, count = parsed
            # Push on top — never wipe the prior epic / nested stack.
            if not self.campaign.assign_goal(item_id, count, graph=self.graph):
                self.client.tell(sender, f"cannot obtain {item_id}")
                return None
            self._deliver_to = sender
            self._deliver_item = item_id
            self._deliver_count = count
            self._deliver_told = False
            self._persist_goals()
            self.client.tell(sender, f"farming {item_id} x{count}")
            print(f"goal {item_id} x{count} for {sender} stack={self.campaign.stack}", flush=True)
            return None
        if order.verb in ("follow", "come"):
            self._leader = sender
            self._pc_party = True
            return None
        if order.verb == "camp":
            return Intention("explore", name="safe", where=self.model.safe)
        if order.verb == "attack":
            spawn = self._spawn_named(order.rest)
            if spawn is not None:
                return Intention("task_kill", target=spawn.spawn_id, name=spawn.name, where=(spawn.x, spawn.y, spawn.z))
        if order.verb == "summon" and self.model.class_id == 11 and "summon" in self._gems:
            spawn = self._spawn_named(sender)
            return Intention("cast", name="summon", target=0 if spawn is None else spawn.spawn_id)
        return None

    def _on_channel(self, payload: bytes) -> None:
        channel = channel_number(payload)
        if channel not in (2, 7):
            return
        sender = channel_sender(payload)
        if not sender or _key(sender) == _key(self.model.character or ""):
            return
        text = payload[148:].split(b"\x00", 1)[0].decode("latin1", "replace")
        order = order_of(sender, text)
        if order is None:
            return
        # Tells (7): accept farm / party orders from any PC. Group chat keeps known filter for combat orders.
        farmish = order.verb in {"farm", "goal", "get", "obtain", "join", "group", "party", "invite"}
        if channel == 7 or farmish or _key(sender) in self._known_names:
            self._orders.append(order)
            print(f"tell {sender}: {order.verb} {order.rest}".strip(), flush=True)

    def _note_group_update(self, action: int, names: list[str]) -> None:
        """Track PC vs bot group membership. Disband/leave resumes campaign bots."""
        me = _key(self.model.character or "")
        others = [n for n in names if _key(n) != me]
        # groupActJoin=0, Leave=1, Disband=6, Update=7, MakeLeader=8, InviteInitial=9
        if action in (0, 7, 9) and names:
            self._grouped = True
            for name_part in names:
                self._known_names.add(_key(name_part))
            # A real PC (non-bot roster stem) landed — invite settled.
            if self._pc_party and others and not all(self._is_our_bot_name(n) for n in others):
                self._awaiting_pc_join = False
            return
        if action == 6:
            # Bot disband while waiting for a PC invite must not resume campaign yet.
            if self._pc_party and self._awaiting_pc_join:
                self._grouped = False
                return
            if self._pc_party or self._leader:
                self._resume_after_pc_party(why="disband")
            else:
                self._grouped = False
            return
        if action == 1:
            left = _key(names[0]) if names else ""
            alone = left == me or not others
            if alone and (self._pc_party or self._leader) and not self._awaiting_pc_join:
                self._resume_after_pc_party(why="leave")
            elif alone:
                self._grouped = False
            else:
                self._grouped = True
                for name_part in names:
                    self._known_names.add(_key(name_part))

    def _is_our_bot_name(self, name: str) -> bool:
        """True when name matches our bot roster (Mocwar, Mocclr, …)."""
        key = _key(name)
        if not key:
            return False
        for roster_name, _class_id in getattr(self.party, "roster", ()) or ():
            if key == _key(roster_name) or key.startswith(_key(roster_name)):
                return True
        return False

    def _player_class_id(self, name: str) -> int:
        spawn = self._spawn_named(name)
        if spawn is not None and int(getattr(spawn, "class_id", 0) or 0) > 0:
            return int(spawn.class_id)
        return 0

    def _pick_bot_to_camp_for_class(self, class_id: int) -> str | None:
        """Same-class bot first; else camp DPS before tank/healer."""
        live: list[tuple[str, int]] = []
        for name, cid in self.party.roster:
            spawned = name in self.party.spawned
            if not spawned and self._spawn_named(name) is None and self._bot_spawn_named(name) is None:
                continue
            live.append((name, cid))
        if not live:
            return None
        if class_id:
            for name, cid in live:
                if cid == class_id:
                    return name
        # Lower = camp first (dps / utility before war/clr).
        rank = {16: 0, 8: 1, 13: 2, 12: 3, 9: 4, 7: 5, 10: 6, 6: 7, 14: 8, 3: 9, 1: 10, 2: 11}
        live.sort(key=lambda nc: rank.get(nc[1], 50))
        return live[0][0]

    def _make_room_for_player(self, pc_name: str = "") -> None:
        """Free one group seat for a PC — camp same-class bot when possible.

        Keeps the rest of the bot group. Does not touch the campaign stack.
        """
        self._pc_party = True
        self._awaiting_pc_join = True
        self._awaiting_pc_since = time.monotonic()
        class_id = self._player_class_id(pc_name) if pc_name else 0
        bot = self._pick_bot_to_camp_for_class(class_id)
        if not bot:
            print(f"party seat open (no bot to camp) for {pc_name or 'pc'}", flush=True)
            return
        self._camped_for_pc = bot
        spawn = self._spawn_named(bot) or self._bot_spawn_named(bot)
        if spawn is not None:
            self._target(spawn.spawn_id)
        me = self.model.character or "Mockone"
        # name1 = member to remove (server GroupDisband bot path).
        self.client.send("OP_GroupDisband", group_invite(bot, me))
        self.client.pump(0.15)
        try:
            self.client.command(f"botcamp byname {bot}")
            self.client.pump(0.2)
        except Exception:
            pass
        self.party.spawned.discard(bot)
        print(f"party seat → camp {bot} class={class_id} for {pc_name or 'pc'}", flush=True)

    def _resume_after_pc_party(self, *, why: str = "") -> None:
        """PC left — clear follow lock, restore form prefs, respawn the camped seat."""
        was_pc = self._pc_party or bool(self._leader)
        camped = self._camped_for_pc
        self._grouped = True if self.party.formed else False
        self._pc_party = False
        self._awaiting_pc_join = False
        self._awaiting_pc_since = 0.0
        self._leader = ""
        self._camped_for_pc = ""
        self.form_group = self._want_form_group
        self.form_raid = self._want_form_raid
        if not was_pc:
            return
        tip = self.campaign.peek()
        print(
            f"party resume ({why}) bots form_group={self.form_group} tip={tip}",
            flush=True,
        )
        if camped and self.form_group and not self.form_raid:
            try:
                self.client.command(f"botspawn byname {camped}")
                self.client.pump(0.4)
                self._party_messages()
                self.client.send(
                    "OP_GroupInvite",
                    group_invite(camped, self.model.character or ""),
                )
                self.party.spawned.add(camped)
                print(f"party seat → restore {camped}", flush=True)
            except Exception:
                # Fall back to a full reform next tick.
                self.party.formed = False

    def _accept_party_invite(self, inviter: str) -> None:
        if not inviter:
            return
        self._make_room_for_player(inviter)
        me = self.model.character or ""
        self.client.send("OP_GroupFollow", group_follow(inviter, me))
        self.client.pump(0.3)
        self._grouped = True
        self._pc_party = True
        self._leader = inviter
        self._known_names.add(_key(inviter))
        print(f"joined {inviter}", flush=True)

    def _invite_player(self, name: str) -> None:
        if not name:
            return
        # Keep bots; free one seat. Campaign stack untouched.
        self._make_room_for_player(name)
        spawn = self._spawn_named(name)
        if spawn is not None:
            self.client.send("OP_InspectRequest", struct.pack("<II", spawn.spawn_id, self.model.self_id))
        else:
            self.client.send("OP_WhoAllRequest", who_request(name))
        self.client.send("OP_GroupInvite", group_invite(name, self.model.character))
        self._grouped = True
        self._pc_party = True
        self._known_names.add(_key(name))
        print(f"invited {name}", flush=True)

    def _try_deliver(self) -> bool:
        """When a tell-farm goal is held, notify the PC and trade the stack for free."""
        if not self._deliver_to or not self._deliver_item:
            return False
        item_id = self._deliver_item
        need = self._deliver_count
        have = self._held_counts().get(item_id, 0)
        if have < need:
            return False
        if not self._deliver_told:
            self.client.tell(self._deliver_to, f"have {item_id} x{have}")
            self._deliver_told = True
        spawn = self._spawn_named(self._deliver_to)
        if spawn is None:
            return True
        if _horiz(self.model.position, (spawn.x, spawn.y, spawn.z)) > 20:
            self._step((spawn.x, spawn.y, spawn.z))
            return True
        from eqclient.items import CURSOR, TRADE

        moved = 0
        for slot, held in list(self.inventory.slots.items()):
            if held.item_id != item_id or moved >= need:
                continue
            take = min(held.stack or 1, need - moved)
            if slot != CURSOR:
                self._move(slot, CURSOR)
                self.client.pump(0.2)
            if not self._target(spawn.spawn_id):
                break
            self.client.send("OP_TradeRequest", struct.pack("<II", spawn.spawn_id, self.model.self_id))
            self.client.pump(0.4)
            self._move(CURSOR, TRADE)
            self.client.pump(0.2)
            self.client.send("OP_TradeAcceptClick", b"")
            self.client.pump(0.6)
            moved += take
        self.client.tell(self._deliver_to, "traded")
        self._deliver_to = ""
        self._deliver_item = 0
        self._deliver_count = 0
        self._deliver_told = False
        while self.campaign.stack and self.campaign.held_enough(self.campaign.stack[-1], self._held_counts()):
            self.campaign.pop()
        self._persist_goals()
        return True

    def _seek_spells(self) -> None:
        """Push one scroll item per spell this class can use and has not scribed."""
        book = getattr(self, "spells", None)
        if not self._book_known or not self._tutorial_done or book is None:
            return
        held = {item.item_id for item in self.inventory.slots.values()}
        changed = apply_spell_goals(
            self.campaign,
            book,
            self.model.class_id or 0,
            self.model.level or 0,
            self.inventory.scribed,
            held,
            graph=self.graph,
            merchants=self.merchants,
            recipes=self.recipes,
            drops=self.drops,
        )
        if changed is None:
            return
        dropped, names = changed
        if names:
            print(f"spells L{self.model.level}: {', '.join(names)}", flush=True)
        elif dropped:
            print(f"spells L{self.model.level}: {dropped} already scribed", flush=True)
        self._persist_goals()

    def _bot_spell_roles(self, class_id: int) -> set[str]:
        """Roles to enable via spellsettings — heals for clerics; nukes + build gems for casters."""
        if class_id == 2:
            return {"heal"}
        build = build_for(class_id)
        roles = set(build.gems) if build is not None and build.gems else set()
        # Pure + hybrid casters must keep nukes on the settings list.
        if class_id in (6, 10, 11, 12, 13, 14):  # dru, shm, nec, wiz, mag, enc
            roles.add("nuke")
        if class_id in (6, 10, 11):  # dru/shm/nec dots
            roles.add("dot")
        if class_id in (11, 13):  # nec/mag pets
            roles.add("pet")
        return roles

    def _prune_bot_spell_noise(self) -> int:
        """One-shot: drop leftover bot-scroll obtain goals from older runs."""
        book = getattr(self, "spells", None)
        if book is None or not self.campaign.stack:
            return 0
        party_spell_items: set[int] = set()
        for class_id in {cid for _n, cid in self.party.roster}:
            for row in book.by_class.get(class_id, ()):
                party_spell_items.add(row.item_id)
        names: dict[int, str] = {}
        for rows in book.by_class.values():
            for row in rows:
                names.setdefault(row.item_id, row.name)
        kept: list[int] = []
        dropped = 0
        for item_id in self.campaign.stack:
            name = (names.get(item_id) or "").lower()
            if name.startswith("illusion") or item_id in party_spell_items:
                dropped += 1
                continue
            kept.append(item_id)
        if dropped:
            counts = {item_id: self.campaign.counts.get(item_id, 1) for item_id in kept}
            self.campaign.load_stack(kept, counts)
            self._persist_goals()
            print(f"bot spells prune {dropped} scroll goals", flush=True)
        return dropped

    def _seek_bot_spells(self) -> None:
        """Enable companion spells from bot_spells_entries; journal gates the missing-spell check.

        Runs once per owner level: if journal bot_spells stamp >= current level, skip.
        On first party form (stamp 0) and every ding (stamp < level), add missing role
        spellsettings by spell id, then stamp the journal. Caster holds/stance once
        per process (spellsettings already journal-gated above).
        """
        if not self._tutorial_done or not self.party.formed:
            return
        if not self._bot_spell_stack_pruned:
            self._prune_bot_spell_noise()
            self._bot_spell_stack_pruned = True
        level = self.model.level or 0
        if level <= 0:
            return
        synced = self.journal.bot_spells_level(self.model.character)
        if synced < level:
            self._sync_bot_spell_settings(since_level=synced)
            self.journal.mark_bot_spells(self.model.character, level)
            print(f"bot spells journal L{level} (was L{synced})", flush=True)
        if not self._caster_nukes_set:
            self._ensure_caster_nukes(settings=synced < level or synced <= 0)

    def _bot_spell_label(self, spell_id: int, fallback: str = "") -> str:
        if fallback:
            return fallback
        bot_book = getattr(self, "bot_spells", None)
        if bot_book is not None:
            name = bot_book.spell_names.get(spell_id) or ""
            if name:
                return name
        name = self.inventory.spell_names.get(spell_id) or ""
        if name:
            return name
        return str(spell_id)

    def _sync_bot_spell_settings(self, *, since_level: int = 0) -> None:
        """botupdate, then spellsettingsadd for bot_spells_entries missing at owner level.

        Spell ids are from npc_spells lists (3000+class), not the player scroll book.
        since_level=0 → all role spells in the current window; else only newly unlocked.
        See docs.eqemu.dev/server/bots/bot-spell-settings/
        """
        book = getattr(self, "bot_spells", None)
        level = self.model.level or 0
        if book is None or not book.rows or level <= 0 or not self.party.formed:
            return
        self.client.command("botupdate")
        self.client.pump(0.6)
        for bot_name, class_id in self.party.roster:
            if bot_name not in self.party.spawned:
                continue
            roles = self._bot_spell_roles(class_id)
            if not roles:
                continue
            entries = book.roles_available(class_id, level, roles, since_level=since_level)
            if not entries:
                continue
            spawn = self._bot_spawn_named(bot_name)
            if spawn is None:
                continue
            self.client.send("OP_TargetMouse", struct.pack("<I", spawn.spawn_id & 0xFFFF))
            self.client.pump(0.3)
            bot_added = 0
            for entry in entries:
                key = (bot_name, entry.spell_id)
                if key in self._bot_spell_settings_done:
                    continue
                before = len(self.client.messages)
                priority = entry.priority if entry.priority > 0 else 1
                self.client.command(f"spellsettingsadd {entry.spell_id} {priority} 0 100")
                self.client.pump(0.3)
                msgs = list(self.client.messages[before:])
                if any("successfully added spell setting" in m.lower() for m in msgs):
                    bot_added += 1
                    self._bot_spell_settings_done.add(key)
                    label = self._bot_spell_label(entry.spell_id, entry.name)
                    print(
                        f"bot spell +{label} ({entry.spell_id} t{entry.type}) → {bot_name}",
                        flush=True,
                    )
                elif any("already has a spell setting" in m.lower() for m in msgs):
                    self._bot_spell_settings_done.add(key)
            if bot_added:
                print(f"bot spells L{level} {bot_name}: +{bot_added}", flush=True)

    def _ensure_caster_nukes(self, *, settings: bool = True) -> None:
        """Unhold nukes/DoTs and (optionally) spellsettings so casters spend mana.

        Holds/stance/enforce persist on the bot after Save; spellsettings live in
        `bot_spell_settings`. Only rewrite settings when `settings` is True
        (first sync / ding) — never re-update rows that already exist.
        """
        if not self.party.formed:
            return
        caster_classes = (6, 10, 11, 12, 13, 14)  # dru shm nec wiz mag enc
        # Type ids: Nuke=0, DOT=8, AENukes=33, PBAENuke=46 (bot_spells.py / BotSpellTypes).
        for type_id in (0, 8, 33, 46):
            try:
                self.client.command(f"spellholds {type_id} 0 spawned")
                self.client.pump(0.25)
            except Exception:
                pass
            try:
                self.client.command(f"spellmaxthresholds {type_id} 100 spawned")
                self.client.pump(0.2)
            except Exception:
                pass
        # Optional list — cast default book spells too when not in settings.
        for class_id in caster_classes:
            try:
                self.client.command(f"enforcespellsettings false byclass {class_id}")
                self.client.pump(0.2)
            except Exception:
                pass
        # Stance::Burn=7 — nukes not held (Assist holds Nuke by default).
        for class_id in (11, 12, 13, 14):
            try:
                self.client.command(f"botstance 7 byclass {class_id}")
                self.client.pump(0.25)
            except Exception:
                pass
        enabled = 0
        if settings:
            book = getattr(self, "bot_spells", None)
            level = self.model.level or 0
            if book is not None and book.rows and level > 0:
                for bot_name, class_id in self.party.roster:
                    if class_id not in caster_classes or bot_name not in self.party.spawned:
                        continue
                    roles = self._bot_spell_roles(class_id)
                    entries = book.roles_available(class_id, level, roles, since_level=0)
                    nukes = [e for e in entries if e.type in (0, 8, 33, 46)]
                    if not nukes:
                        continue
                    spawn = self._bot_spawn_named(bot_name)
                    if spawn is None:
                        continue
                    self.client.send("OP_TargetMouse", struct.pack("<I", spawn.spawn_id & 0xFFFF))
                    self.client.pump(0.2)
                    for entry in nukes[:6]:
                        key = (bot_name, entry.spell_id)
                        if key in self._bot_spell_settings_done:
                            continue
                        priority = entry.priority if entry.priority > 0 else 1
                        before = len(self.client.messages)
                        self.client.command(
                            f"spellsettingsadd {entry.spell_id} {priority} 0 100"
                        )
                        self.client.pump(0.25)
                        msgs = list(self.client.messages[before:])
                        blob = " ".join(msgs).lower()
                        if "successfully added spell setting" in blob:
                            self._bot_spell_settings_done.add(key)
                            enabled += 1
                            label = self._bot_spell_label(entry.spell_id, entry.name)
                            print(
                                f"bot nuke +{label} ({entry.spell_id}) → {bot_name}",
                                flush=True,
                            )
                        elif "already has a spell setting" in blob:
                            # Already in bot_spell_settings — do not update/toggle spam.
                            self._bot_spell_settings_done.add(key)
        self._caster_nukes_set = True
        print(f"caster nukes ready (+{enabled} settings)", flush=True)

    def _undergeared(self) -> bool:
        """True when few worn slots are filled — grind should not outrun buying kits."""
        worn = sum(1 for slot in WORN if slot in self.inventory.slots)
        # Weapon + a couple armor pieces counts as geared enough to keep grinding.
        return worn < 3

    def _seek_gear(self) -> None:
        """Seed kits and keep missing self-kit pieces above the epic grind tip."""
        if not self._tutorial_done:
            return
        from eqclient.gear import kit_for

        level = self.model.level or 1
        tier = gear_tier(level)
        party = [(n, c) for n, c in self.party.roster] if self.party.formed else []
        held = {item.item_id for item in self.inventory.slots.values()}
        # Prefer current tier kit, fall back to beginner so L5 still buys leather.
        want = list(kit_for(self.model.class_id or 0, tier))
        for item_id in kit_for(self.model.class_id or 0, "beginner"):
            if item_id not in want:
                want.append(item_id)
        missing = [
            item_id
            for item_id in want
            if item_id not in held and item_id not in self.campaign.skipped
        ]
        tip = self.campaign.peek()
        tip_is_kit = tip in want if tip else False
        naked = self._undergeared()
        stamp = (
            f"{tier}:{'|'.join(n for n, _ in party)}:"
            f"{'naked' if naked else 'ok'}:{','.join(str(i) for i in missing)}"
        )
        if self._gear_tier_seeded == stamp:
            return
        labels = seed_gear_goals(
            self.campaign,
            self.model.class_id or 0,
            level,
            held,
            party=party,
            graph=self.graph,
        )
        # Epic components keep re-pushing above buried kits — re-surface missing
        # self gear whenever the tip is not already a kit buy.
        if missing and (naked or not tip_is_kit):
            for item_id in missing:
                self.campaign.push(item_id, 1)
                label = f"top:self:{item_id}"
                if label not in labels:
                    labels.append(label)
        self._gear_tier_seeded = stamp
        if labels:
            print(f"gear {tier}: {', '.join(labels[:12])}", flush=True)
            self._persist_goals()

    def _backpack_id(self) -> int:
        """Classic vendor backpack, or another merchant backpack if 17005 is unstocked."""
        merchants = getattr(self, "merchants", None)
        if merchants is not None and merchants.sells(BACKPACK_ITEM):
            return BACKPACK_ITEM
        best_id = BACKPACK_ITEM
        best_cost: int | None = None
        graph_items = (getattr(self.graph, "items", None) or {}) if self.graph is not None else {}
        for item_id, row in (getattr(merchants, "by_item", None) or {}).items():
            name = str((graph_items.get(int(item_id)) or {}).get("name") or "").lower()
            if "backpack" not in name:
                continue
            cost = int(row.get("cost") or 0)
            if best_cost is None or (0 < cost < best_cost):
                best_id = int(item_id)
                best_cost = cost
        return best_id

    def _refresh_corpse_backlog(self) -> None:
        """Keep needs_corpse true; aim at the closest outstanding body (not FIFO)."""
        pending = self.journal.outstanding_corpses(self.model.character)
        if pending <= 0:
            return
        here = self.model.position
        remembered = self.journal.corpse(
            self.model.character,
            zone=self.model.zone or "",
            x=here[0],
            y=here[1],
            z=here[2],
        )
        if remembered is None:
            return
        czone, cx, cy, cz = remembered
        # Retarget when a closer journal corpse appears (or we had no aim).
        cur = self.model.own_corpse_at
        if (
            self.model.needs_corpse
            and cur is not None
            and (self.model.own_corpse_zone or "").lower() == czone.lower()
        ):
            if abs(cur[0] - cx) + abs(cur[1] - cy) + abs(cur[2] - cz) < 1.0:
                return
            # Keep current aim if it is still outstanding and not farther than the pick.
            cur_d = _horiz(here, cur)
            new_d = _horiz(here, (cx, cy, cz))
            if cur_d <= new_d + 1.0:
                return
        self.model.needs_corpse = True
        self.model.own_corpse_zone = czone
        self.model.own_corpse_at = (cx, cy, cz)
        self.model.own_corpse_id = 0

    def _clear_bag_goal(self, *, reason: str = "") -> None:
        """Drop a stuck backpack obtain tip so shop cannot spin forever."""
        item_id = self._backpack_id()
        if self.campaign.stack and self.campaign.stack[-1] == item_id:
            self.campaign.pop()
            self._persist_goals()
        self._bag_goal = False
        tip = f" ({reason})" if reason else ""
        print(f"bags clear goal{tip}", flush=True)

    def _seek_bags(self) -> None:
        """Push backpack goals only when an empty general slot can receive one."""
        if not self._tutorial_done:
            return
        # Corpse reclaim first — don't nest a bag buy on the obtain stack mid-backlog.
        if self.model.needs_corpse or self.journal.outstanding_corpses(self.model.character) > 0:
            return
        item_id = self._backpack_id()
        buyable = bags_buyable(self.inventory)
        short = bags_short(self.inventory)
        if buyable <= 0:
            # No free slot → cannot buy. Drop a stuck bag tip so shop doesn't spin.
            if getattr(self, "_bag_goal", False) and self.campaign.stack and self.campaign.stack[-1] == item_id:
                self.campaign.pop()
                self._bag_goal = False
                self._persist_goals()
                print("bags defer (no empty general slot)", flush=True)
            elif short <= 0 and getattr(self, "_bag_goal", False) and self.campaign.stack and self.campaign.stack[-1] == item_id:
                self.campaign.pop()
                self._bag_goal = False
                self._persist_goals()
                print("bags full set", flush=True)
            return
        have = self.inventory.count(item_id)
        want = have + buyable
        if item_id in self.campaign.stack:
            self.campaign.counts[item_id] = max(self.campaign.counts.get(item_id, 1), want)
            self._bag_goal = True
            return
        if self.campaign.assign_goal(item_id, want, graph=self.graph):
            self._bag_goal = True
            print(f"bags need {buyable} (item {item_id})", flush=True)
            self._persist_goals()

    def _inventory_needs_sell(self) -> bool:
        """True only when there is vendor trash and room pressure (or general slots waste)."""
        keep = self._protected_items()
        junk = trash_slots(self.inventory, keep)
        cursor = self.inventory.cursor()
        has_junk = bool(junk) or (cursor is not None and is_vendor_trash(cursor, keep))
        if not has_junk:
            return False
        if not has_loot_room(self.inventory) or not can_receive(self.inventory):
            return True
        for slot in GENERAL:
            held = self.inventory.slots.get(slot)
            if held is not None and not held.bag_slots and is_vendor_trash(held, keep):
                return True
        return bags_short(self.inventory) > 0

    def _sell_trash_intent(self) -> Intention | None:
        """Vendor junk so loot and backpacks have somewhere to land — skip if nothing to sell."""
        keep = self._protected_items()
        if trash_slots(self.inventory, keep):
            return self._merchant_intent(text="sell")
        cursor = self.inventory.cursor()
        if cursor is not None and is_vendor_trash(cursor, keep):
            return self._merchant_intent(text="sell")
        return None

    def _bag_intent(self) -> Intention | None:
        """Buy a backpack into an empty general slot when short."""
        if bags_buyable(self.inventory) <= 0:
            return None
        if self.model.needs_corpse or self.journal.outstanding_corpses(self.model.character) > 0:
            return None
        # Don't buy while general junk still occupies pack slots — sell first.
        keep = self._protected_items()
        if any(
            held is not None and not held.bag_slots and is_vendor_trash(held, keep)
            for held in (self.inventory.slots.get(slot) for slot in GENERAL)
        ):
            return None
        item_id = self._backpack_id()
        cost = self.merchants.cost(item_id) if self.merchants is not None else 0
        # Need at least one bag's price on hand — don't walk the merchant broke.
        if self.model.coin_known and cost > 0 and self.model.coin < cost:
            return None
        return self._merchant_intent(text="buy", item_id=item_id)

    def _merchant_intent(self, *, text: str, item_id: int = 0) -> Intention | None:
        """Shop a live merchant, or walk/find toward a cached seller name in this zone."""
        merchant = self._nearest_merchant(item_id=item_id)
        if merchant is not None:
            return Intention(
                "shop",
                target=merchant.spawn_id,
                name=merchant.name,
                where=(merchant.x, merchant.y, merchant.z),
                item_id=item_id,
                text=text,
            )
        seller = self._cached_seller(item_id=item_id)
        if seller is not None:
            seen = (self.model.last_seen.get(seller.name.lower())
                    or self.model.last_seen.get(_merchant_norm(seller.name)))
            where = None
            if seen and len(seen) >= 4 and str(seen[0] or "").lower() in (
                (self.model.zone or "").lower(),
                seller.zone,
            ):
                where = (float(seen[1]), float(seen[2]), float(seen[3]))
            return Intention("explore", name=seller.name, item_id=item_id, where=where, text=text)
        return Intention("explore", name="merchant", item_id=item_id, text=text)

    def _persist_goals(self) -> None:
        self.journal.save_goal_stack(
            self.model.character,
            list(self.campaign.stack),
            dict(self.campaign.counts),
            deliver_to=self._deliver_to,
            deliver_item=self._deliver_item,
            deliver_count=self._deliver_count,
        )

    def _spawn_named(self, name: str):
        wanted = _key(name)
        for spawn in self.model.spawns.values():
            if _key(spawn.name) == wanted:
                return spawn
        return None

    def _stack(self, kind: str) -> int | None:
        words = (
            ("bread", "ration", "meat", "cheese", "pie", "stew", "mushroom", "patty", "fish")
            if kind == "food"
            else ("water", "drink", "ale", "wine", "milk", "cider", "tea")
        )
        for slot, held in self.inventory.slots.items():
            if any(word in held.name.lower() for word in words):
                return slot
        return None

    def _eat(self, kind: int) -> None:
        slot = self._stack("food" if kind == 1 else "water")
        if slot is None or self._engaged():
            return
        self.client.send("OP_Consume", consume_packet(slot, kind))

    def _cast_role(self, role: str, target: int) -> None:
        gem = self._gems.get(role)
        if gem is None or gem[1] <= 0:
            return
        slot, spell_id = gem
        if getattr(self, "_spell_set", None) != self.model.zone:
            self._spell_set = self.model.zone
            self.client.send("OP_LoadSpellSet", struct.pack("<I", 0))
        self.client.send("OP_CastSpell", cast_packet(slot, spell_id, target))
        if role == "root":
            self._rooted = True
        elif role == "snare":
            self._snared = True
        elif role == "slow":
            self._slowed = True

    def _ability_ready_now(self, name: str) -> bool:
        return time.monotonic() >= self._ability_ready.get(name, 0.0)

    def _mark_ability(self, name: str, reuse: float | None = None) -> None:
        wait = ability_reuse(name) if reuse is None else reuse
        self._ability_last = name
        self._ability_ready[name] = time.monotonic() + max(0.0, wait)

    def _ability(self, opcode: str) -> None:
        if not opcode or not self._ability_ready_now(opcode):
            return
        self._mark_ability(opcode)
        self.client.send(opcode, b"")

    def _stack_coin(self) -> None:
        """Collapse coin piles so bags stay usable (smarter plan: OP_MoveCoin)."""
        try:
            self.client.send("OP_MoveCoin", struct.pack("<IIII", 0, 1, 0, 0))
        except Exception:
            pass

    def _bandolier(self, index: int = 0) -> None:
        try:
            self.client.send("OP_Bandolier", struct.pack("<I", index))
        except Exception:
            pass

    def _potion_belt(self) -> None:
        try:
            self.client.send("OP_PotionBelt", b"\x00")
        except Exception:
            pass

    def _friends_who(self, name: str) -> None:
        if not name:
            return
        try:
            self.client.send("OP_FriendsWho", name.encode("latin1")[:64].ljust(64, b"\x00"))
        except Exception:
            self.client.send("OP_WhoAllRequest", who_request(name))

    def _protected_items(self) -> set[int]:
        return protected_ids(self.graph, self.campaign, self.quests)

    def _tidy(self) -> None:
        """Destroy one unprotected trash piece once bags are full and nothing will vendor."""
        if has_loot_room(self.inventory):
            return
        keep = self._protected_items()
        for slot in trash_slots(self.inventory, keep):
            self.client.send("OP_DeleteItem", struct.pack("<I", slot))
            self.inventory.slots.pop(slot, None)
            return
        cursor = self.inventory.cursor()
        if cursor is not None and is_vendor_trash(cursor, keep):
            self.client.send("OP_DeleteItem", struct.pack("<I", CURSOR))
            self.inventory.slots.pop(CURSOR, None)

    def _shop_spawn(self, intention: Intention):
        """Live merchant for this shop intent — by id, then name, then nearest known seller."""
        spawn = self.model.spawns.get(intention.target) if intention.target else None
        if spawn is not None and spawn.npc == 1:
            return spawn
        if intention.name:
            spawn = self._spawn_named(intention.name)
            if spawn is not None:
                return spawn
        return self._nearest_merchant(item_id=intention.item_id)

    def _shop(self, intention: Intention) -> None:
        if not intention.target:
            return
        who = intention.name or str(intention.target)
        print(f"shop {who} why={intention.text or '-'}", flush=True)
        self.client.send("OP_ShopRequest", struct.pack("<III", intention.target, self.model.self_id, 1))
        self.client.pump(0.4)
        sold = 0
        bought = 0
        if intention.text == "buy" and intention.item_id:
            # Merchant inventory appears as temporary slots in some builds; buy by item id when listed.
            backpack = intention.item_id == self._backpack_id()
            if backpack and bags_buyable(self.inventory) <= 0:
                print("buy skip backpack (no empty general slot)", flush=True)
                self._clear_bag_goal(reason="no slot")
            else:
                want = max(1, bags_buyable(self.inventory) if backpack else 1)
                for slot, held in list(self.inventory.slots.items()):
                    if held.item_id != intention.item_id:
                        continue
                    qty = max(1, held.stack or 1)
                    print(f"buy {held.name} x{qty} slot={slot}", flush=True)
                    self.client.send(
                        "OP_ShopPlayerBuy",
                        struct.pack("<IIII", intention.target, slot, qty, 0),
                    )
                    self.client.pump(0.3)
                    self._make_room_for_loot()
                    bought += 1
                    if bought >= want:
                        break
                if bought == 0:
                    print(f"buy miss item={intention.item_id}", flush=True)
                    if backpack:
                        self._clear_bag_goal(reason="buy miss")
        elif intention.text == "sell" and intention.item_id:
            # Targeted sell (practice products / "Sell X from inventory").
            for slot, held in list(self.inventory.slots.items()):
                if held.item_id != intention.item_id:
                    continue
                qty = max(1, held.stack or 1)
                print(f"sell {held.name} x{qty} slot={slot}", flush=True)
                self.client.send("OP_ShopPlayerSell", struct.pack("<IIII", intention.target, slot, qty, 0))
                self.client.pump(0.2)
                sold += 1
            if sold == 0:
                print(f"sell miss item={intention.item_id}", flush=True)
        else:
            # Dump vendor trash — bags themselves stay. Sell a whole visit's worth.
            keep = self._protected_items()
            junk = trash_slots(self.inventory, keep)[:24]
            cursor = self.inventory.cursor()
            if not junk and (cursor is None or not is_vendor_trash(cursor, keep)):
                print("sell skip (no trash)", flush=True)
                self.client.send("OP_ShopEnd", b"")
                return
            for slot in junk:
                held = self.inventory.slots.get(slot)
                if held is None:
                    continue
                qty = max(1, held.stack or 1)
                print(f"sell {held.name} x{qty} slot={slot}", flush=True)
                self.client.send(
                    "OP_ShopPlayerSell",
                    struct.pack("<IIII", intention.target, slot, qty, 0),
                )
                self.client.pump(0.15)
                sold += 1
            cursor = self.inventory.cursor()
            # Same trash rules as bag junk — never delete food, gear, bags, or stack goals.
            if cursor is not None and is_vendor_trash(cursor, keep):
                print(f"sell drop cursor {cursor.name}", flush=True)
                self.client.send("OP_DeleteItem", struct.pack("<I", CURSOR))
                self.inventory.slots.pop(CURSOR, None)
                self.client.pump(0.1)
        if intention.text == "buy":
            print(f"shop done buy={bought}", flush=True)
        else:
            print(f"shop done sell={sold}", flush=True)
        self.client.send("OP_ShopEnd", b"")

    def _bank(self, intention: Intention) -> None:
        """Open banker and dump non-equipped keepers when bags are tight."""
        if not intention.target:
            return
        self._target(intention.target)
        self.client.send("OP_ClickDoor", struct.pack("<I", intention.target))
        self.client.pump(0.3)
        # Deposit general-slot junk that is not protected / campaign.
        keep = self._protected_items()
        for slot, held in list(self.inventory.slots.items()):
            if slot < 22 or held.item_id in keep:
                continue
            if held.bag_slots or held.ac or held.damage:
                continue
            self.client.send("OP_MoveItem", struct.pack("<IIII", slot, 2000 + (slot % 30), held.stack or 1, 0))
            self.client.pump(0.15)

    def _bag_signature(self) -> tuple[tuple[int, int], ...]:
        """Inventory bags that can affect whether a combine succeeds later."""
        return tuple(
            sorted((slot, held.item_id) for slot, held in self.inventory.slots.items() if held.bag_slots)
        )

    def _recipe_deferred(self, recipe_id: int) -> bool:
        """True while a recent craft failure is cooling down for this recipe."""
        bags = self._bag_signature()
        if bags != getattr(self, "_recipe_bags", None):
            self._recipe_bags = bags
            self._recipe_retry_at = {}
        until = getattr(self, "_recipe_retry_at", {}).get(recipe_id)
        return until is not None and time.monotonic() < until

    def _defer_recipe(self, recipe_id: int, seconds: float = 180.0) -> None:
        """Pause retries; cleared when bags change or the timer expires."""
        retry = getattr(self, "_recipe_retry_at", None)
        if retry is None:
            self._recipe_retry_at = retry = {}
        retry[recipe_id] = time.monotonic() + seconds
        self._recipe_bags = self._bag_signature()
        print(f"defer craft {recipe_id} {seconds:.0f}s", flush=True)

    def _combine(self, recipe_id: int, *, skill_up: bool = False) -> bool:
        """True when this tick combined, approached a station, or waited. False when the zone has no station yet."""
        if recipe_id <= 0:
            return True
        if self._recipe_deferred(recipe_id):
            return True
        recipe = self._recipe_book().by_id.get(recipe_id)
        components: list[tuple[int, int]] = list(recipe.components) if recipe else []
        if not components and self.graph is not None:
            source = f"recipe:{recipe_id}"
            for edge in self.graph.edges:
                if edge.get("rel") == "consumes" and edge.get("from") == source:
                    components.append((int(str(edge.get("to")).split(":")[-1]), int(edge.get("count") or 1)))
        container = recipe.container if recipe else 0
        bag_slot = self._container_slot(container)
        world = False
        if bag_slot is None:
            from eqclient.conduct import _WORLD_CONTAINER

            if container in _WORLD_CONTAINER:
                picked = pick_station(container, self.model.doors.values(), self.model.ground.values(), self.model.position)
                if picked is None:
                    return False
                kind, station = picked
                goal = (station.x, station.y, station.z)
                if _horiz(self.model.position, goal) > 8:
                    self._step(goal)
                    return True
                if kind == "door":
                    self._click_door(station.door_id)
                else:
                    self.client.send("OP_ClickObject", struct.pack("<I", station.drop_id))
                self.client.pump(0.3)
                bag_slot = WORLD_COMBINE
                world = True
            else:
                self._defer_recipe(recipe_id)
                return True
        dest = WORLD_CONTENTS
        for item_id, count in components:
            moved = 0
            for slot, held in list(self.inventory.slots.items()):
                if held.item_id != item_id or moved >= count:
                    continue
                if world:
                    if dest > WORLD_CONTENTS + 9:
                        break
                    self._move(server_slot(slot), dest)
                    dest += 1
                else:
                    self._move(slot, bag_slot)
                moved += 1
                self.client.pump(0.1)
        mark = len(self.client.messages)
        self.client.send("OP_TradeSkillCombine", struct.pack("<hh", bag_slot, 0))
        self.client.pump(0.4)
        news = " ".join(self.client.messages[mark:]).lower()
        if "does not recognize" in news or "tradeskill container" in news or "cannot combine" in news:
            self._defer_recipe(recipe_id)
        return True

    def _container_slot(self, container_id: int) -> int | None:
        """Inventory slot of the recipe's portable kit, if held."""
        if container_id <= 0:
            return None
        for slot, held in self.inventory.slots.items():
            if held.item_id == container_id and held.bag_slots:
                return slot
        return None

    def _slot_of_type(self, item_type: int) -> int | None:
        for slot, held in self.inventory.slots.items():
            if held.item_type == item_type:
                return slot
        return None

    def _count_of_type(self, item_type: int) -> int:
        total = 0
        for held in self.inventory.slots.values():
            if held.item_type == item_type:
                total += max(1, held.stack or 1)
        return total

    def _fish(self, intention: Intention) -> None:
        """Pole + bait (item-id obtain) → shore → face water → cast."""
        pole_slot = self._slot_of_type(ITEM_FISHING_POLE)
        if pole_slot is None:
            if FISH_POLE not in self.campaign.stack:
                self.campaign.push(FISH_POLE, 1)
            return
        if self._count_of_type(ITEM_FISHING_BAIT) < 1:
            if FISH_BAIT not in self.campaign.stack:
                self.campaign.push(FISH_BAIT, FISH_BAIT_WANT)
            return
        primary = self.inventory.slots.get(PRIMARY)
        if primary is None or primary.item_type != ITEM_FISHING_POLE:
            if primary is not None and primary.item_type != ITEM_FISHING_POLE:
                bag = self.inventory.empty_general()
                if bag is None:
                    return
                if not self._fish_stashed:
                    self._fish_stashed = primary.item_id
                self._move(PRIMARY, bag)
                self.client.pump(0.1)
                return
            if pole_slot != PRIMARY:
                self._move(pole_slot, PRIMARY)
                self.client.pump(0.1)
            return
        here = self.model.position
        if self.water is not None and not self.water.can_fish_at(*here):
            spot = self.water.fish_spot(*here)
            if spot is not None and _horiz(here, spot) > 2.0:
                self._step(spot)
                self._fish_facing = False
                return
            if spot is None:
                # No shore nearby — wander; zone travel already handled by campaign.
                return
            here = spot
        if self.water is not None and not self._fish_facing:
            aim = self.water.fish_aim(*here)
            if aim is not None:
                self._face(aim)
                self._fish_facing = True
                return
        self.client.send("OP_Fishing", b"")

    def _unfish(self) -> None:
        """Put the stashed primary weapon back after fishing."""
        self._fish_facing = False
        if not self._fish_stashed:
            return
        primary = self.inventory.slots.get(PRIMARY)
        weapon_slot = None
        for slot, held in self.inventory.slots.items():
            if held.item_id == self._fish_stashed and slot != PRIMARY:
                weapon_slot = slot
                break
        if weapon_slot is None:
            self._fish_stashed = 0
            return
        if primary is not None and primary.item_type == ITEM_FISHING_POLE:
            bag = self.inventory.empty_general()
            if bag is None:
                # Swap via cursor if bags are tight.
                self._move(PRIMARY, CURSOR)
                self.client.pump(0.1)
                self._move(weapon_slot, PRIMARY)
                self.client.pump(0.1)
                self._clear_cursor()
            else:
                self._move(PRIMARY, bag)
                self.client.pump(0.1)
                self._move(weapon_slot, PRIMARY)
                self.client.pump(0.1)
        elif primary is None:
            self._move(weapon_slot, PRIMARY)
            self.client.pump(0.1)
        self._fish_stashed = 0

    def _face(self, where: tuple[float, float, float], *, force: bool = False) -> None:
        """Turn in place toward a point. force=True for melee (skip step gate)."""
        here = self.model.position
        if not force and not self.model.step_ready():
            return
        spawn_id = self.model.self_id
        self._send_history()
        self.client.send(
            "OP_ClientUpdate",
            client_position(
                spawn_id,
                self.model.next_sequence(),
                here[0],
                here[1],
                here[2],
                here[0],
                here[1],
                here[2],
                heading=eq_heading(here[0], here[1], where[0], where[1]),
                animation=0,
            ),
        )
        if not force:
            self.model.arm_step(here, here)

    def _needed_items(self) -> set[int]:
        needed: set[int] = set()
        for script in self.quests.scripts.values():
            for need in script.needs:
                if self.inventory.count(need.item_id) < need.count:
                    needed.add(need.item_id)
        return needed

    def _held_counts(self) -> dict[int, int]:
        counts: dict[int, int] = {}
        for held in self.inventory.slots.values():
            counts[held.item_id] = counts.get(held.item_id, 0) + (held.stack or 1)
        return counts

    def _recipe_book(self):
        book = getattr(self, "recipes", None)
        if book is not None:
            return book
        cached = getattr(self, "_recipes", None)
        if cached is not None:
            return cached
        path = os.environ.get("EQEMU_RECIPES", DEFAULT_RECIPES)
        self._recipes = read_recipes(path)
        return self._recipes

    def _hp_ratio(self) -> float:
        if self.model.max_hp <= 0:
            return 1.0
        return self.model.hp / self.model.max_hp

    def _away(self, where):
        here = self.model.position
        if where is None:
            return None
        dx, dy = here[0] - where[0], here[1] - where[1]
        length = math.hypot(dx, dy)
        if length < 0.5:
            # Standing on the point — pick a compass backstep (coincident has no radial).
            angle = math.radians((self._reacquire_i * 45.0) % 360.0)
            return (here[0] + math.cos(angle) * 12.0, here[1] + math.sin(angle) * 12.0, here[2])
        return (here[0] + dx / length * 12, here[1] + dy / length * 12, here[2])

    def _reacquire_foe(self, spawn_id: int) -> None:
        """Re-find a mob we cannot see — scan in place first, then back off + Find.

        Do not charge back onto the Find pad in the same call (that erased the backup).
        After a Find, `_hold_melee_until` forces swing attempts before another backup.
        """
        spawn = self.model.spawns.get(spawn_id)
        if spawn is None:
            return
        now = time.monotonic()
        if now - self._reacquire_at < 1.5:
            return
        self._reacquire_at = now
        self._reacquire_i += 1
        here = self.model.position
        where = (spawn.x, spawn.y, spawn.z)
        dist = _horiz(here, where)
        angle = (self._reacquire_i * 45.0) % 360.0
        rad = math.radians(angle)
        look = (here[0] + math.cos(rad) * 50.0, here[1] + math.sin(rad) * 50.0, here[2])
        self.client.send("OP_TargetMouse", struct.pack("<I", spawn_id))
        self._grind_mode = "chase"
        # Phases 1–4: stay put, spin the camera, keep AutoAttack on (snake may already be chewing).
        if self._reacquire_i % 8 < 5:
            print(
                f"reacquire scan {spawn.name} id={spawn_id} angle={angle:.0f} dist={dist:.1f}",
                flush=True,
            )
            self._face(look, force=True)
            self.client.send("OP_AutoAttack", b"\x01\x00\x00\x00")
            self._hold_melee_until = now + 2.0
            return
        # Phases 5–8: back off + Find. Next ticks close to melee ring, not this tick.
        back_x = here[0] + math.cos(rad) * 16.0
        back_y = here[1] + math.sin(rad) * 16.0
        if self._reacquire_i % 2:
            back_x -= math.sin(rad) * 8.0
            back_y += math.cos(rad) * 8.0
        back = (back_x, back_y, here[2])
        print(
            f"reacquire back {spawn.name} id={spawn_id} angle={angle:.0f} dist={dist:.1f}",
            flush=True,
        )
        self.client.send("OP_AutoAttack", b"\x00\x00\x00\x00")
        self._step(back, direct=True, length=STEP)
        self._face(look, force=True)
        self._find_arrived.discard(spawn_id)
        self._find_empty.discard(spawn_id)
        self._guide_for = 0
        self.guide = []
        self._ask_find(spawn_id)
        self._hold_melee_until = now + 3.0

    def _engaged(self) -> bool:
        """True while a live mob is still in the fight he has already started.

        A started swing sticks until corpse / gave-up / regroup — do not drop a
        mid-close (combat start at 37 yd) for a fresh grind walk across the zone.
        Threat without a swing still uses a range gate so we do not kite forever.
        """
        for spawn_id in (self._swing_id, self._threat):
            if not spawn_id:
                continue
            spawn = self.model.spawns.get(spawn_id)
            if spawn is None or spawn.npc != 1:
                continue
            if spawn_id == self._swing_id and self._swing_hp == 0:
                continue
            if self._has_gave_up(spawn.spawn_id) and spawn_id != self._threat:
                continue
            if spawn_id == self._swing_id:
                return True
            if _horiz(self.model.position, (spawn.x, spawn.y, spawn.z)) <= 50:
                return True
        return False

    def _active_fight_spawn(self):
        """Current stick target if still a live fight — prefer swing, then threat/pursuit."""
        for spawn_id in (self._swing_id, self._threat, self._pursuit):
            if not spawn_id:
                continue
            spawn = self.model.spawns.get(spawn_id)
            if spawn is None or spawn.npc != 1:
                continue
            if spawn_id == self._swing_id and self._swing_hp == 0:
                continue
            if self._has_gave_up(spawn.spawn_id):
                continue
            if self._is_companion_pet(spawn):
                continue
            return spawn
        return None

    def _fight_hp_pct(self, spawn) -> int | None:
        """Known HP% for the active swing target; None if we have not seen MobHealth."""
        if spawn is None or not self._swing_id:
            return None
        if (spawn.spawn_id & 0xFFFF) != (self._swing_id & 0xFFFF):
            return None
        if self._swing_hp < 0:
            return None
        return int(self._swing_hp)

    def _finish_current_kill(self, spawn) -> bool:
        """True when current target is low enough that a higher-level switch is wasteful."""
        hp = self._fight_hp_pct(spawn)
        return hp is not None and hp < 40

    def _note_bot_threat(self, spawn, why: str, *, bot_id: int = 0) -> None:
        """Mark a mob the bots are fighting — clear it before any grind walk.

        Do not retarget off an active fight when another mob also hits — that
        ping-pongs ^attack / chase between pack members.
        """
        if spawn is None or spawn.npc != 1:
            return
        if self._is_companion_pet(spawn):
            return
        fresh = spawn.spawn_id not in self._bot_threats
        self._bot_threats.add(spawn.spawn_id)
        stuck = self._active_fight_spawn()
        if stuck is not None and stuck.spawn_id != spawn.spawn_id:
            # Higher-level add — retarget so bots pull/hold the dangerous one,
            # unless the current kill is already under 40% HP or the add has no LoS
            # (^attack / TargetMouse fails through walls and ping-pongs focus).
            can_focus = (
                (spawn.level or 0) > (stuck.level or 0)
                and not self._finish_current_kill(stuck)
                and self._in_sight((spawn.x, spawn.y, spawn.z))
            )
            if can_focus:
                if fresh:
                    print(
                        f"aggro {spawn.name} L{spawn.level or 0} {why} "
                        f"(focus over {stuck.name} L{stuck.level or 0})",
                        flush=True,
                    )
                self._pursuit = spawn.spawn_id
                self._threat = spawn.spawn_id
                if bot_id:
                    self._threat_bot_id = bot_id & 0xFFFF
                self._grind_mode = "chase"
                self._grind_walk_until = 0.0
                return
            # Same/lower level, no LoS, or current nearly dead — queue; finish kill first.
            if fresh:
                hp = self._fight_hp_pct(stuck)
                hold = (
                    f"(hold {stuck.name} L{stuck.level or 0}"
                    + (f" {hp}%" if hp is not None else "")
                    + ")"
                )
                print(
                    f"aggro +{spawn.name} L{spawn.level or 0} {why} {hold}",
                    flush=True,
                )
            if bot_id and not self._threat_bot_id:
                self._threat_bot_id = bot_id & 0xFFFF
            return
        self._pursuit = spawn.spawn_id
        self._threat = spawn.spawn_id
        if bot_id:
            self._threat_bot_id = bot_id & 0xFFFF
        self._grind_mode = "chase"
        self._grind_walk_until = 0.0
        if fresh:
            print(f"aggro {spawn.name} L{spawn.level or 0} {why}", flush=True)

    def _live_bot_threats(self) -> list:
        """Live NPCs still on the bot-aggro list (drops corpses / despawns)."""
        live = []
        for spawn_id in list(self._bot_threats):
            spawn = self.model.spawns.get(spawn_id)
            if (
                spawn is None
                or spawn.npc != 1
                or self._has_gave_up(spawn_id)
                or self._is_companion_pet(spawn)
            ):
                self._bot_threats.discard(spawn_id)
                if self._threat == spawn_id:
                    self._threat = 0
                    self._threat_bot_id = 0
                continue
            live.append(spawn)
        return live

    def _reclaim_path_foe(self, corpse_where: tuple[float, float, float] | None = None):
        """Nearest LOS hostile on the corpse run — clear one before walking further.

        Prefers mobs between us and the corpse (path-aligned) so we do not train a
        pack into the body. Companion pets and non-camp trash are ignored.
        """
        from eqclient.plan import _camp_mob
        import math

        here = self.model.position
        protected = self._protected_spawn_ids()
        toward = None
        corpse_dist = 1e9
        if corpse_where is not None:
            dx = corpse_where[0] - here[0]
            dy = corpse_where[1] - here[1]
            corpse_dist = math.hypot(dx, dy)
            if corpse_dist > 1.0:
                toward = (dx / corpse_dist, dy / corpse_dist)

        # Finish the foe we already paused reclaim for before picking another.
        for hold_id in (self._reclaim_held_for, self._threat, self._swing_id, self._pursuit):
            if not hold_id or hold_id in protected:
                continue
            held = self.model.spawns.get(hold_id)
            if (
                held is None
                or held.npc != 1
                or self._has_gave_up(hold_id)
                or self._is_companion_pet(held)
            ):
                continue
            if not _camp_mob(held):
                continue
            hwhere = (held.x, held.y, held.z)
            hdist = _horiz(here, hwhere)
            if hdist <= _RECLAIM_CAUTION and self._in_sight(hwhere):
                return held

        best = None
        best_score = None
        for spawn in self.model.spawns.values():
            if spawn.npc != 1 or spawn.spawn_id in protected:
                continue
            if self._has_gave_up(spawn.spawn_id) or self._is_companion_pet(spawn):
                continue
            if not _camp_mob(spawn):
                continue
            where = (spawn.x, spawn.y, spawn.z)
            dist = _horiz(here, where)
            if dist > _RECLAIM_CAUTION or dist < 2.0:
                # Near the body: also take hostiles sitting on the corpse pad.
                if (
                    corpse_where is None
                    or corpse_dist > 160.0
                    or _horiz(where, corpse_where) > _RECLAIM_CORPSE_CLEAR
                ):
                    continue
                if dist > _SIGHT_RANGE:
                    continue
            if not self._in_sight(where):
                continue
            # Path score: on-corridor first, then nearest.
            if toward is not None:
                mx = spawn.x - here[0]
                my = spawn.y - here[1]
                along = mx * toward[0] + my * toward[1]
                side = abs(mx * toward[1] - my * toward[0])
                on_path = 0 if (along > -10.0 and along < corpse_dist + 25.0 and side < 55.0) else 1
                score = (on_path, side if on_path == 0 else dist, dist)
            else:
                score = (0, dist, dist)
            if best_score is None or score < best_score:
                best = spawn
                best_score = score
        return best

    def _must_clear_aggro(self) -> bool:
        """True when reclaim/loot must yield — something is hitting us or the bots."""
        if self._live_bot_threats():
            return True
        if self._engaged():
            return True
        max_hp = self.model.max_hp or 0
        if max_hp > 0 and self.model.hp * 100 < max_hp * 98:
            return True
        if self._threat:
            spawn = self.model.spawns.get(self._threat)
            if spawn is not None and spawn.npc == 1:
                if _horiz(self.model.position, (spawn.x, spawn.y, spawn.z)) <= 60:
                    return True
        return False

    def _retaliate_intention(self) -> Intention | None:
        """Fight mobs beating on us or the bots — do not walk off and leave them.

        Prefer any LoS foe over a higher-level add we cannot see. Among LoS (or among
        blind if none have sight), highest level wins; nearer breaks ties.
        """
        bot_foes = self._live_bot_threats()
        foe_ids = {s.spawn_id for s in bot_foes}
        here = self.model.position

        def _kill_intent(spawn) -> Intention:
            self._pursuit = spawn.spawn_id
            self._threat = spawn.spawn_id
            return Intention(
                "task_kill",
                target=spawn.spawn_id,
                name=spawn.name,
                where=(spawn.x, spawn.y, spawn.z),
                text="retaliate",
            )

        def _sight_ok(spawn) -> bool:
            return self._in_sight((spawn.x, spawn.y, spawn.z))

        def _priority(spawn) -> tuple:
            # LoS before level — never select a wall-blocked higher add over a clear kill.
            return (
                1 if _sight_ok(spawn) else 0,
                spawn.level or 0,
                -_horiz(here, (spawn.x, spawn.y, spawn.z)),
            )

        best_foe = max(bot_foes, key=_priority) if bot_foes else None

        # Active fight: keep it unless a higher-level LoS add is on the board.
        stuck = self._active_fight_spawn()
        if stuck is not None and (stuck.spawn_id in foe_ids or stuck.spawn_id == self._swing_id):
            switch_to = None
            if (
                best_foe is not None
                and best_foe.spawn_id != stuck.spawn_id
                and _sight_ok(best_foe)
                and (best_foe.level or 0) > (stuck.level or 0)
                and not self._finish_current_kill(stuck)
            ):
                switch_to = best_foe
            if switch_to is None:
                return _kill_intent(stuck)
            if getattr(self, "_aggro_focus_logged", 0) != switch_to.spawn_id:
                self._aggro_focus_logged = switch_to.spawn_id
                print(
                    f"aggro focus {switch_to.name} L{switch_to.level or 0} "
                    f"(over {stuck.name} L{stuck.level or 0})",
                    flush=True,
                )
            return _kill_intent(switch_to)

        if best_foe is not None:
            return _kill_intent(best_foe)

        for spawn_id in (self._threat, self._swing_id, self._pursuit):
            if not spawn_id:
                continue
            spawn = self.model.spawns.get(spawn_id)
            if spawn is None or spawn.npc != 1:
                continue
            if spawn_id == self._swing_id and self._swing_hp == 0:
                continue
            if self._has_gave_up(spawn.spawn_id) and spawn_id != self._threat:
                continue
            if _horiz(self.model.position, (spawn.x, spawn.y, spawn.z)) > 50:
                continue
            # task_kill so _act forces the swing even if faction/sight is murky.
            return _kill_intent(spawn)
        return None

    def _break_off(self, *, keep_pursuit: bool = False) -> None:
        """Drop the next target. The current swing stays until the fight is over."""
        if not keep_pursuit:
            self._pursuit = 0
        self._focus = 0
        if not keep_pursuit:
            self.guide = []
            self._guide_for = 0
        if self._swing_id and not self._engaged():
            self.client.send("OP_AutoAttack", b"\x00\x00\x00\x00")
            self._swing_id = 0

    def _rest(self) -> None:
        """Sit. He only gets here after the fight and after he is back at the safe point."""
        now = time.monotonic()
        # Party heals need range — gather first. Mana med: summon once, then sit so
        # follow spam does not yank the cleric off med forever.
        if self._party_needs_rest() and not self._bots_close(40):
            self._rally_bots(now, why="rest")
            if self._sitting:
                self._stand()
            return
        if self._needs_mana_rest() and not self._bots_close(40) and not self._sitting:
            self._rally_bots(now, why="rest")
            # Fall through and sit — bots arrive via summon; owner parking lets them med.
        # Downed bots stay on the roster — ^botspawn them back while we park.
        self._respawn_missing_bots()
        if self._sitting and now - self._sat_at < 2:
            self._practice_skills(resting=True, fighting=False)
            return
        if not self._sitting:
            mana = f" clr={self._cleric_mana * 100:.0f}%" if self._cleric_mana is not None else ""
            party = " party-crit" if self._party_needs_rest() else ""
            print(f"sit {self.model.hp}/{self.model.max_hp}{mana}{party}", flush=True)
            if self._needs_mana_rest():
                self._cleric_medding = True
            # Fresh mana read while parking — bots med via sitmanapercent.
            self._bot_report_at = 0.0
        if self._sneaking and self._ability_ready_now("OP_Sneak"):
            self._ability("OP_Sneak")  # toggle off before sit — sneak needs motion
        self._sneaking = False
        self._appearance(110)
        self._sitting = True
        self._sat_at = now
        self._practice_skills(resting=True, fighting=False)

    def _ensure_clerics_spawned(self) -> list[str]:
        """^botspawn any roster cleric not in the zone (death/despawn). Returns names spawned."""
        now = time.monotonic()
        if now - float(getattr(self, "_cleric_respawn_at", 0.0)) < 3.0:
            return []
        missing = [
            name
            for name, cid in self.party.roster
            if cid == 2 and self._bot_spawn_named(name) is None
        ]
        if not missing:
            return []
        self._cleric_respawn_at = now
        spawned: list[str] = []
        for name in missing:
            try:
                self.client.command(f"botspawn {name}")
                self.client.pump(0.5)
                self._party_messages()
                self.party.spawned.add(name)
                self.party.owned.add(name)
                spawned.append(name)
                print(f"bot respawn {name} (cleric)", flush=True)
            except Exception:
                continue
        if not spawned:
            return []
        try:
            self.client.command("botsummon spawned")
            self.client.pump(0.3)
            order = self.party.combat_order("follow") or "follow reset spawned"
            self.client.command(order)
            self.client.pump(0.2)
            # Fresh spawn — re-seat heal rotation next tick if needed.
            # Caster spellsettings stay on the bot DB across camp/respawn.
            self._heal_rotation_set = False
            self._heal_rotation_at = 0.0
            print(f"bots botsummon+follow after cleric respawn x{len(spawned)}", flush=True)
        except Exception:
            pass
        return spawned

    def _note_bot_corpse(self, spawn_id: int) -> None:
        """If a roster cleric just died, ^botspawn them immediately."""
        spawn = self.model.spawns.get(spawn_id)
        if spawn is None:
            return
        stem = (spawn.name or "").rstrip("0123456789")
        for name, cid in self.party.roster:
            if cid != 2:
                continue
            if name == stem or name == (spawn.name or "") or stem.startswith(name):
                self._ensure_clerics_spawned()
                return

    def _respawn_missing_bots(self) -> None:
        """^botspawn roster bots that died/despawned. Keeps party.spawned; no prune."""
        if not self.party.formed:
            return
        # Clerics first — heal/reclaim cannot wait for the rest-time sweep.
        self._ensure_clerics_spawned()
        now = time.monotonic()
        if now - float(getattr(self, "_bot_respawn_at", 0.0)) < 8.0:
            return
        missing = [
            name
            for name, cid in self.party.roster
            if cid != 2
            and name in self.party.spawned
            and self._bot_spawn_named(name) is None
        ]
        if not missing:
            return
        self._bot_respawn_at = now
        for name in missing:
            try:
                self.client.command(f"botspawn {name}")
                self.client.pump(0.45)
                self._party_messages()
                print(f"bot respawn {name} (rest)", flush=True)
            except Exception:
                continue
        try:
            self.client.command("botsummon spawned")
            self.client.pump(0.3)
            order = self.party.combat_order("follow") or "follow reset spawned"
            self.client.command(order)
            self.client.pump(0.2)
            self._enable_tank_taunt()
            # New spawns may not be in the worn cache yet — list only unknowns.
            self._cache_all_bot_worn()
            print(f"bots botsummon+follow after respawn x{len(missing)}", flush=True)
        except Exception:
            pass

    def _target_enemy(self, spawn_id: int, *, via_bot_id: int = 0) -> bool:
        """Lock GetTarget for ^attack / pet attack via OP_TargetMouse.

        Always TargetMouse the known enemy. Do **not** Assist a bot to pick their
        target — AssistNoTargetSelf / stale bot ids / corpses leave GetTarget on
        self or a bot, and ^attack then fails with "must <target> an enemy".
        (Damage chat already gives us the NPC id; Assist was only causing misses.)

        `via_bot_id` is accepted for call-site compat but ignored.

        OP_TargetCommand validates clip range and *clears* GetTarget past maxclip —
        never use it before ^attack. Entity id is 16-bit on the wire.
        """
        del via_bot_id  # kept so callers need not change
        if not spawn_id:
            return False
        spawn = self.model.spawns.get(spawn_id) or self._spawn_by_entity(spawn_id)
        if spawn is None or spawn.npc != 1 or self._is_corpse_spawn(spawn):
            return False
        eid = spawn.spawn_id & 0xFFFF
        # Clear sticky self/bot target, then lock the foe (same pattern as self-rez).
        try:
            self.client.send("OP_TargetMouse", struct.pack("<I", 0))
            self.client.pump(0.05)
            self.client.send("OP_TargetMouse", struct.pack("<I", eid))
            self.client.pump(0.15)
        except Exception:
            return False
        return True

    def _pet_attack(self, spawn_id: int, *, why: str = "") -> None:
        """Send Titanium OP_PetCommands attack so the owner's pet joins the pull.

        Bot pets pick up hate from ^attack (SetOwnerTarget); this covers Mag/Nec/BST
        owner pets and any charm pet on Mockone.
        Titanium window 'Attack' = command 7 → server PetCommand::Attack.
        """
        if not spawn_id:
            return
        spawn = self.model.spawns.get(spawn_id) or self._spawn_by_entity(spawn_id)
        if spawn is None or spawn.npc != 1:
            return
        tag = f" ({why})" if why else ""
        eid = spawn.spawn_id & 0xFFFF
        # Assume _bots_attack already locked GetTarget; re-assert without long pump.
        self.client.send("OP_TargetMouse", struct.pack("<I", eid))
        try:
            # command=7 (Titanium attack), target=entity id
            self.client.send(
                "OP_PetCommands",
                struct.pack("<II", 7, eid),
            )
            self.client.pump(0.15)
            print(f"pet attack → {spawn.name}{tag}", flush=True)
        except Exception:
            return

    def _bots_attack(self, spawn_id: int, *, why: str = "") -> bool:
        """Hard-target a foe, then ^attack (+ pet). Never fire without GetTarget set.

        Returns True only when the order landed. LoS / target fails leave
        `_bot_attack_for` unset so pull-hold never parks on a blocked shot.
        """
        if not spawn_id or not self.party.formed:
            return False
        spawn = self.model.spawns.get(spawn_id) or self._spawn_by_entity(spawn_id)
        if spawn is None or spawn.npc != 1:
            return False
        spawn_id = spawn.spawn_id
        now = time.monotonic()
        # Dedupe reissues only — do not skip because spawn is in _bot_threats.
        # Retaliate marks threat from damage *before* the first ^attack / pet order.
        if self._bot_attack_for == spawn_id and now - self._bot_order_at < 4.0:
            return True
        if (
            getattr(self, "_bot_attack_fail_for", 0) == spawn_id
            and now - float(getattr(self, "_bot_attack_fail_at", 0)) < 2.5
        ):
            return False
        dist = _horiz(self.model.position, (spawn.x, spawn.y, spawn.z))
        # Too far for a reliable target lock — wait until send range.
        if dist > _BOT_SEND_RANGE + 15.0:
            return False
        tag = f" ({why})" if why else ""

        def _order_failed(msgs: list[str]) -> str:
            """Empty = ok/unknown; else short reason. LoS counts as real failure."""
            if any("attacking" in m and ("bot" in m or m.startswith("attacking ")) for m in msgs):
                return ""
            if any("line of sight" in m for m in msgs):
                return "need LoS"
            if any("must <target> an enemy" in m for m in msgs):
                return "need enemy target"
            return ""

        self._locking_attack_target = True
        try:
            if not self._target_enemy(spawn_id):
                self._bot_attack_fail_for = spawn_id
                self._bot_attack_fail_at = now
                print(f"bots attack skip {spawn.name} (no target lock){tag}", flush=True)
                return False
            # Re-assert TargetMouse immediately before ^attack — a prior pump can
            # process cure/heal which TargetMouse's *self* and clears the enemy.
            eid = spawn_id & 0xFFFF
            self.client.send("OP_TargetMouse", struct.pack("<I", eid))
            self.client.pump(0.05)
            order = self.party.combat_order("attack") or "attack"
            mark = len(self.client.messages)
            try:
                self.client.command(order)
                self.client.pump(0.35)
            except Exception:
                return False
            new_msgs = [m.lower() for m in self.client.messages[mark:]]
            fail = _order_failed(new_msgs)
            if fail == "need enemy target":
                # One retry: clear + hard TargetMouse the known foe (never Assist).
                if not self._target_enemy(spawn_id):
                    self._bot_attack_fail_for = spawn_id
                    self._bot_attack_fail_at = now
                    print(f"bots attack fail {spawn.name} (need enemy target){tag}", flush=True)
                    return False
                self.client.send("OP_TargetMouse", struct.pack("<I", eid))
                self.client.pump(0.05)
                mark = len(self.client.messages)
                try:
                    self.client.command(order)
                    self.client.pump(0.35)
                except Exception:
                    return False
                new_msgs = [m.lower() for m in self.client.messages[mark:]]
                fail = _order_failed(new_msgs)
            if fail:
                # Do not mark ordered / pull-hold — caller must approach for LoS.
                self._bot_attack_fail_for = spawn_id
                self._bot_attack_fail_at = now
                print(f"bots attack fail {spawn.name} ({fail}){tag}", flush=True)
                return False
            self._pet_attack(spawn_id, why=why or "with bots")
            self._bot_attack_for = spawn_id
            self._bot_order_at = now
            self._bot_pull_at = now
            self._bot_attack_fail_for = 0
            print(f"bots {order} → {spawn.name}{tag}", flush=True)
            return True
        finally:
            self._locking_attack_target = False

    def _rally_bots(
        self,
        now: float | None = None,
        *,
        force: bool = False,
        why: str = "",
        attack_target: int | None = None,
    ) -> None:
        """Summon at most once when bots are far; never re-summon when nearby.

        `force` still respects proximity and the summon cooldown — it only means
        "we need bots for a fight now" (reclaim/retaliate), not "spam botsummon".
        After a summon, wait for the zone/chat catch-up, then ^attack + pet.
        """
        if not self.party.formed:
            return
        now = time.monotonic() if now is None else now
        tag = f" ({why})" if why else ""
        foe = attack_target or self._swing_id or self._threat or 0
        # Already on us — re-summon breaks target locks. Just attack (+ pet).
        if self._bots_close(100):
            if foe:
                self._bots_attack(foe, why=why or "nearby")
            elif force and now - self._bot_order_at >= 8.0:
                order = self.party.combat_order("follow") or "follow reset spawned"
                try:
                    self.client.command(order)
                    self._bot_order_at = now
                    print(f"bots {order}{tag}", flush=True)
                except Exception:
                    pass
            return
        summon_at = float(getattr(self, "_bot_summon_at", 0.0))
        if now - summon_at < 12.0:
            # Last summon still settling — do not spam; attack if spawns already visible.
            if foe and self._bot_spawns():
                self._bots_attack(foe, why=why or "summon pending")
            return
        if not force and now - self._bot_order_at < 8.0:
            return
        self._bot_summon_at = now
        self._bot_order_at = now
        try:
            self.client.command("botsummon spawned")
            print(f"bots botsummon spawned{tag}", flush=True)
            # One summon, then wait for chat/spawns — do not reissue.
            deadline = time.monotonic() + 2.5
            while time.monotonic() < deadline:
                self.client.pump(0.2)
                self._party_messages()
                msgs = " ".join(self.client.messages[-6:]).lower()
                if "summoned" in msgs and "bot" in msgs:
                    break
                if self._bots_close(100):
                    break
            order = self.party.combat_order("follow") or "follow reset spawned"
            self.client.command(order)
            print(f"bots {order}{tag}", flush=True)
            if foe:
                self.client.pump(0.25)
                self._bots_attack(foe, why=why)
        except Exception:
            return

    def _has_bandages(self) -> bool:
        return any(
            getattr(held, "item_type", 0) == 18 or held.item_id in (13009, 13081)
            for held in self.inventory.slots.values()
        )

    def _bind_wound(self) -> None:
        """OP_Bind_Wound (8-byte BindWound_Struct). Needs a bandage; 10s server timer."""
        if self._skills.get(9, 0) <= 0:
            return
        now = time.monotonic()
        if now - self._bind_at < 10.5:
            return
        if not self._has_bandages():
            return
        # Prefer a critical party member in range, else self (cap ~50–70% HP).
        target_id = self.model.self_id
        here = self.model.position
        for sid, hp in self._party_hp.items():
            if hp > 70:
                continue
            member = self._party_member_spawn(sid)
            if member is None:
                continue
            if _horiz(here, (member.x, member.y, member.z)) <= 18:
                target_id = member.spawn_id
                break
        else:
            if self.model.max_hp > 0 and self.model.hp * 100 // self.model.max_hp > 70:
                return
        self._bind_at = now
        # to, pad, type, pad — type 0 starts the bandage.
        self.client.send(
            "OP_Bind_Wound",
            struct.pack("<HHHH", target_id & 0xFFFF, 0, 0, 0),
        )
        who = self.model.spawns.get(target_id)
        print(f"bind wound → {who.name if who else target_id}", flush=True)

    def _practice_skills(self, *, resting: bool, fighting: bool) -> None:
        """Fire every grind-time practice that is off cooldown (forage, sense, hide, …)."""
        if fighting and not resting:
            # Keep melee clean — only sense heading is harmless mid-fight.
            self._sneaking = False  # combat breaks sneak server-side
            if self._skills.get(40, 0) > 0 and self._ability_ready_now("OP_SenseHeading"):
                self._ability("OP_SenseHeading")
            return
        if self._skills.get(27, 0) > 0 and self._ability_ready_now("OP_Forage"):
            self._ability("OP_Forage")
        if self._skills.get(40, 0) > 0 and self._ability_ready_now("OP_SenseHeading"):
            self._ability("OP_SenseHeading")
        if self._skills.get(29, 0) > 0 and self._ability_ready_now("OP_Hide"):
            self._ability("OP_Hide")
        # Sneak is a toggle and only skills while moving — never while sitting/resting.
        if not resting and not fighting and not self._sitting:
            self._practice_sneak()
        if self._skills.get(53, 0) > 0 and self._ability_ready_now("OP_Track"):
            self._mark_ability("OP_Track", 20.0)
            self.client.send("OP_Track", b"")
            if self._pursuit:
                self.client.send("OP_TrackTarget", struct.pack("<I", self._pursuit))
            print("practice track", flush=True)
        if resting and self._skills.get(9, 0) > 0:
            self._bind_wound()
        if self.party.formed or self._grouped:
            self._practice_language()

    def _practice_sneak(self) -> None:
        """Toggle sneak while walking: skill-up only on activate; hold on, then off to retry."""
        if self._skills.get(42, 0) <= 0 or not self._ability_ready_now("OP_Sneak"):
            return
        now = time.monotonic()
        if self._sneaking:
            if now - self._sneak_on_at < 12.0:
                return
            self._ability("OP_Sneak")  # toggle off (no skill check)
            self._sneaking = False
            return
        self._ability("OP_Sneak")
        self._sneaking = True
        self._sneak_on_at = now
        print("practice sneak", flush=True)

    def _practice_language(self) -> None:
        """Group-say in a non-mastered tongue so SelfLanguageLearning / listeners skill up."""
        now = time.monotonic()
        if now - self._lang_at < 12.0:
            return
        # Skip Common (0); pick the lowest unfinished foreign language (1–24).
        candidates = []
        for lang_id in range(1, 25):
            skill = self._languages.get(lang_id, 0)
            if skill < 100:
                candidates.append((skill, lang_id))
        if not candidates:
            return
        candidates.sort()
        skill, lang_id = candidates[0]
        self._lang_at = now
        # Claimed skill for the packet; server uses real PP skill for ups.
        self.client.group_say(
            f"... ({lang_id})",
            language=lang_id,
            lang_skill=max(1, min(100, skill + 1)),
        )

    def _stand(self) -> None:
        if not self._sitting:
            return
        mana = f" clr={self._cleric_mana * 100:.0f}%" if self._cleric_mana is not None else ""
        print(f"stand {self.model.hp}/{self.model.max_hp}{mana}", flush=True)
        self._appearance(100)
        self._sitting = False
        # Keep medding latch if still short — next tick must re-sit, not reclaim.
        if self._cleric_mana is None or self._cleric_mana >= 0.9:
            self._cleric_medding = False

    def _appearance(self, parameter: int) -> None:
        spawn_id = self.model.self_id & 0xFFFF
        if not spawn_id:
            return
        # type 14 is Animation. 110 sits, 100 stands.
        self.client.send("OP_SpawnAppearance", struct.pack("<HHI", spawn_id, 14, parameter))

    def _refresh_stack_factions(self) -> set[int]:
        """Faction ids gated on the obtain stack — never attack NPCs of these."""
        key = tuple(int(item_id) for item_id in (self.campaign.stack if self.campaign else ()))
        if key == self._stack_faction_key:
            return self._stack_faction_ids
        self._stack_faction_key = key
        self._stack_faction_ids = stack_faction_ids(self.campaign, self.graph)
        if self._stack_faction_ids:
            print(
                f"protect factions {sorted(self._stack_faction_ids)}",
                flush=True,
            )
        return self._stack_faction_ids

    def _faction_protected(self, spawn) -> bool:
        """True when this NPC's primary faction is still needed by the stack."""
        needed = self._refresh_stack_factions()
        if not needed or self.factions is None or spawn is None:
            return False
        primary = self.factions.primary(self.model.zone or "", spawn.name or "")
        return bool(primary and primary in needed)

    def _owned_bot_keys(self) -> set[str]:
        keys: set[str] = set()
        for name in getattr(self.party, "owned", ()) or ():
            keys.add(_key(name))
        for name in getattr(self.party, "spawned", ()) or ():
            keys.add(_key(name))
        for name, _cid in getattr(self.party, "roster", ()) or ():
            keys.add(_key(name))
        for spawn in self._bot_spawns():
            keys.add(_key(spawn.name))
        return {k for k in keys if k}

    def _is_companion_pet(self, spawn) -> bool:
        """True for pets belonging to us or our bots (e.g. Mocmag`s_pet000)."""
        if spawn is None or spawn.npc != 1:
            return False
        raw = (spawn.name or "").lower()
        name = raw.replace("#", "")
        owner = ""
        for sep in ("`s_pet", "'s_pet", "`s pet", "'s pet"):
            if sep in name:
                owner = name.split(sep, 1)[0]
                break
        if not owner:
            return False
        owner_key = _key(owner)
        me = _key(self.model.character or "")
        if me and (owner_key == me or owner_key.startswith(me)):
            return True
        for bot in self._owned_bot_keys():
            if owner_key == bot or owner_key.startswith(bot) or bot.startswith(owner_key):
                return True
        return False

    def _protected_spawn_ids(self) -> set[int]:
        """Live spawn ids we must never grind: stack factions + companion pets."""
        out: set[int] = set()
        for spawn in self.model.spawns.values():
            if spawn.npc != 1:
                continue
            if self._is_companion_pet(spawn):
                out.add(spawn.spawn_id)
        needed = self._refresh_stack_factions()
        if needed and self.factions is not None:
            zone = self.model.zone or ""
            for spawn in self.model.spawns.values():
                if spawn.npc != 1:
                    continue
                primary = self.factions.primary(zone, spawn.name or "")
                if primary and primary in needed:
                    out.add(spawn.spawn_id)
        return out

    def _attack(self, spawn_id: int, force: bool, grind: bool = False) -> None:
        spawn = self.model.spawns.get(spawn_id)
        if spawn is None:
            return
        from eqclient.packets import is_enemy_faction

        # Hard deny: never swing on our bots' pets (or our own).
        if self._is_companion_pet(spawn):
            print(f"combat spare pet {spawn.name} id={spawn_id}", flush=True)
            self._mark_gave_up(spawn_id, 120.0)
            if self._pursuit == spawn_id:
                self._pursuit = 0
            if self._swing_id == spawn_id:
                self._swing_id = 0
            if self._threat == spawn_id:
                self._threat = 0
            self._bot_threats.discard(spawn_id)
            self.client.send("OP_AutoAttack", b"\x00\x00\x00\x00")
            return

        # Hard deny: never hit NPCs of factions the obtain stack still needs.
        if self._faction_protected(spawn):
            print(
                f"combat spare {spawn.name} id={spawn_id} "
                f"(stack faction {self.factions.primary(self.model.zone or '', spawn.name or '') if self.factions else 0})",
                flush=True,
            )
            self._mark_gave_up(spawn_id, 60.0)
            if self._pursuit == spawn_id:
                self._pursuit = 0
            if self._swing_id == spawn_id:
                self._swing_id = 0
            if self._threat == spawn_id:
                self._threat = 0
            self.client.send("OP_AutoAttack", b"\x00\x00\x00\x00")
            return
        faction = self.model.faction.get(spawn_id)
        if faction is None:
            self.client.send("OP_Consider", struct.pack("<IIIIIIBBBB", self.model.self_id, spawn_id, 0, 0, 0, 0, 0, 0, 0, 0))
            self.client.pump(0.2)
            faction = self.model.faction.get(spawn_id)
        # Friendly / indifferent (1–5): never for grind — Qeynos/Freeport guards con 5.
        # Non-grind needs scowling/threatening unless force (retaliate / task kill / finish).
        if not force:
            if faction is not None and faction <= 5:
                if grind or self._grind_mode in ("chase", "walk"):
                    print(f"combat skip {spawn.name} id={spawn_id} con={faction}", flush=True)
                    self._mark_gave_up(spawn_id, 90.0)
                    if self._pursuit == spawn_id:
                        self._pursuit = 0
                    if self._swing_id == spawn_id:
                        self._swing_id = 0
                    self._grind_mode = ""
                return
            if grind:
                if faction is not None and faction < 6:
                    return
            elif not is_enemy_faction(faction or 0):
                return
        here = self.model.position
        now = time.monotonic()
        where = (spawn.x, spawn.y, spawn.z)
        dist = _horiz(here, where)
        if self._swing_id != spawn_id:
            self._swing_id = spawn_id
            self._swing_at = now
            self._progress_at = now
            self._landed = False
            self._swing_hp = -1
            self._hp_at_swing = self.model.hp
            self._bot_attack_for = 0  # allow one fresh ^attack for this foe
            self._bot_attack_fail_for = 0
            self._bot_attack_fail_at = 0.0
            self._bot_pull_at = 0.0
            self._bot_pull_logged = 0
            self._chase_best_dist[spawn_id] = dist
            print(f"combat start {spawn.name} id={spawn_id} dist={dist:.1f}", flush=True)
        elif dist <= _MELEE_RANGE + 8 and now - self._progress_at > 25:
            # In melee and nothing is landing — give up.
            self._mark_gave_up(spawn_id)
            self._focus = 0
            self._swing_id = 0
            print(f"combat leave {spawn.name} id={spawn_id}", flush=True)
            return
        elif dist > _MELEE_RANGE + 8 and now - self._swing_at > 90:
            # Chased too long without ever sticking — do not kite forever.
            self._mark_gave_up(spawn_id)
            self._focus = 0
            self._swing_id = 0
            print(f"combat leave {spawn.name} id={spawn_id} (chase)", flush=True)
            return
        # Snake chewing on us = stay aggressive. Still close if outside melee reach.
        being_hit = self.model.hp < self._hp_at_swing - 1
        if being_hit:
            self._progress_at = now
            self._hold_melee_until = max(self._hold_melee_until, now + 1.5)
        holding = now < self._hold_melee_until
        on_pad = dist <= _MELEE_RANGE + 2.0
        stacked = dist < 2.5  # on top of the mob — LOS/^attack breaks here
        # Face every tick — server skips melee without IsFacingMob.
        self._face(where, force=True)
        self.client.pump(0.05)
        # Soft target for our swing — TargetMouse only (TargetCommand clears past clip).
        self.client.send("OP_TargetMouse", struct.pack("<I", spawn_id & 0xFFFF))
        grouped = bool(self.party.formed and self.party.spawned)
        bots_on = spawn_id in self._bot_threats
        reclaiming = self._is_reclaiming()

        def _close_stride(d: float) -> float:
            """Reclaim: walk then creep into melee so bots engage first."""
            if not reclaiming:
                return STEP_LOS if d > _BOT_SEND_RANGE else STEP
            if d <= _RECLAIM_CREEP_RANGE:
                return STEP_CREEP
            if d <= _BOT_HOLD_RANGE + 30.0:
                return STEP_WALK
            return STEP

        # Early reclaim/sight pull: stand until the raid is up (unless already chewing us).
        # Reclaim: even under fire, wait for bots nearby before the owner charges.
        if (
            grouped
            and force
            and (not being_hit or reclaiming)
            and not bots_on
            and not self._bots_close(int(_BOT_SEND_RANGE))
            and dist > _BOT_HOLD_RANGE
        ):
            self.client.send("OP_AutoAttack", b"\x00\x00\x00\x00")
            if self._bot_pull_logged != spawn_id:
                self._bot_pull_logged = spawn_id
                print(
                    f"pull hold {spawn.name} dist={dist:.0f} waiting raid up",
                    flush=True,
                )
            # Still close toward send range so ^attack can land once bots are up.
            if dist > _BOT_SEND_RANGE:
                goal = self._melee_goal(where, reach=_BOT_HOLD_RANGE)
                if goal is not None:
                    self._step(goal, direct=True, length=_close_stride(dist))
            return
        # Throttle ^attack until we have LoS (BotsRequireLoS). Being hit / bots
        # already chewing still force the order. No sight → mesh/Find, no pull-hold.
        can_see = self._in_sight(where)
        if (
            grouped
            and dist <= _BOT_SEND_RANGE
            and self.model.hp > 0
            and not can_see
            and not being_hit
            and not bots_on
        ):
            self.client.send("OP_AutoAttack", b"\x00\x00\x00\x00")
            if self._bot_pull_logged != spawn_id:
                self._bot_pull_logged = spawn_id
                print(
                    f"pull hold {spawn.name} dist={dist:.0f} need LoS",
                    flush=True,
                )
            self._approach(where, spawn_id, walk=reclaiming)
            return
        # Send bots+pet in send range. Gate on recent order, not bots_on — retaliate
        # puts the mob in _bot_threats before the first ^attack / pet command.
        if grouped and dist <= _BOT_SEND_RANGE and self.model.hp > 0 and (can_see or being_hit or bots_on):
            # Prior LoS fail cooldown must not block once we have a clear shot again.
            if can_see and self._bot_attack_fail_for == spawn_id:
                self._bot_attack_fail_for = 0
            tip = "pull" if self._bot_attack_for != spawn_id else "reissue"
            if force and tip == "reissue":
                tip = "retaliate"
            before = self._bot_attack_for
            ok = self._bots_attack(spawn_id, why=f"{tip} {dist:.0f}")
            if not ok and not being_hit and not bots_on:
                # Server LoS/target fail — do not pull-hold; close/mesh for a clear shot.
                self.client.send("OP_AutoAttack", b"\x00\x00\x00\x00")
                self._approach(where, spawn_id, walk=reclaiming)
                return
            if self._bot_attack_for == spawn_id and before != spawn_id:
                self._enable_tank_taunt()

        bots_sent = self._bot_attack_for == spawn_id
        ordered = bots_sent and now - self._bot_order_at < 8.0
        # Hold owner AutoAttack until bots have been ^attack'd. Reclaim also waits
        # for first contact; grind waits for contact unless already being chewed.
        waiting_bots = (
            grouped
            and not bots_on
            and dist <= _BOT_SEND_RANGE + 15.0
            and (
                not bots_sent
                or (ordered and (reclaiming or not being_hit))
            )
        )
        if waiting_bots:
            self.client.send("OP_AutoAttack", b"\x00\x00\x00\x00")
            if self._bot_pull_logged != spawn_id:
                self._bot_pull_logged = spawn_id
                tip = "bots send" if not bots_sent else "bots first contact"
                print(
                    f"pull hold {spawn.name} dist={dist:.0f} {tip}",
                    flush=True,
                )
            # Close to hold ring so ^attack LOS works; never into melee.
            reach = _BOT_HOLD_RANGE
            if dist > reach + 2.0 or dist < reach - 4.0:
                goal = self._melee_goal(where, reach=reach)
                if goal is not None:
                    self._step(goal, direct=True, length=_close_stride(dist))
            return

        # Too far, or stacked on the hitbox — move to the melee ring (not the pad).
        # Being hit at 9yd used to freeze in place with AutoAttack on but out of range.
        if dist > _MELEE_RANGE + 1.0 or (stacked and not holding):
            if not being_hit and dist > _MELEE_RANGE + 1.0:
                self.client.send("OP_AutoAttack", b"\x00\x00\x00\x00")
            self._grind_mode = "chase"
            reach = _MELEE_RANGE - 0.5
            goal = self._melee_goal(where, reach=reach)
            if goal is not None:
                self._step(goal, direct=True, length=_close_stride(dist))
            if not being_hit and dist > _MELEE_RANGE + 1.0:
                return
            # Under fire / bots on it: keep closing AND fall through to AutoAttack.

        targeted = True if (being_hit or holding) else self._target(spawn_id)
        if not targeted and not being_hit and not holding:
            # Blind on the pad and nothing is biting — scan / Find (rate-limited).
            if on_pad and not self._landed and now - self._swing_at > 2.5:
                self._reacquire_foe(spawn_id)
            else:
                self.client.send("OP_AutoAttack", b"\x00\x00\x00\x00")
                goal = self._melee_goal(where)
                if goal is not None:
                    self._step(goal, direct=True, length=STEP_LOS)
            return
        # Still no ^attack order — never solo-swing aggro (esp. reclaim).
        if grouped and not bots_sent and not bots_on:
            self.client.send("OP_AutoAttack", b"\x00\x00\x00\x00")
            if dist <= _BOT_SEND_RANGE and self.model.hp > 0:
                self._bots_attack(spawn_id, why=f"pre-swing {dist:.0f}")
            return
        self.attacked.add(spawn_id)
        self._rooted = False
        self._snared = False
        tactic = fight_tactic(self.model.class_id, bool(self._grouped or self._leader))
        if not may_melee(tactic, self._rooted, self._snared, self._slowed, self._hp_ratio()):
            self._cast_role(opener(tactic), spawn_id)
            return
        # Drop Find once we're on the mob — stuck leave must not treat Find as "still walking".
        if self._guide_for == spawn_id or self._find_for == spawn_id:
            self.guide = []
            self._guide_for = 0
        # Bots already ordered (or on the mob) — now the owner may swing.
        self.client.send("OP_AutoAttack", b"\x01\x00\x00\x00")
        self._combat_specials(spawn_id, tactic)
        # Dead owner / no HP — don't spam ^attack (LOS fails on corpse/stack).
        if self.model.hp <= 0:
            return
        if not self._pull_cleared:
            guard = self.party.combat_order("guard")
            if guard and now - self._bot_order_at < 0.5:
                self.client.command(guard)
        self._refresh_pull_cleared(spawn_id)

    def _combat_specials(self, spawn_id: int, tactic: str = "") -> None:
        """Taunt / Kick / Bash on reuse. SkillUpdate may omit a skill until first use — class gates then."""
        # Taunt/Kick/Bash: server reuse ~5–8s. Spamming every tick → recovery chat.
        # Owner only: skip taunt on corpse runs (bot tanks keep ^taunt on).
        if (
            tactic == "tank"
            and self._ability_ready_now("taunt")
            and not self._is_reclaiming()
        ):
            self.client.send("OP_Taunt", struct.pack("<I", spawn_id))
            self._mark_ability("taunt")
        # Kick=30, Bash=10 (common/skills.h). Secondary/shield slot = 14.
        if self._can_combat_skill(30) and self._ability_ready_now("kick"):
            self.client.send("OP_CombatAbility", struct.pack("<III", spawn_id, 0, 30))
            self._mark_ability("kick")
        if self._can_combat_skill(10) and self._ability_ready_now("bash"):
            # Bash needs a shield (or 2H on some rules); server rejects quietly if illegal.
            secondary = self.inventory.slots.get(14)
            primary = self.inventory.slots.get(PRIMARY)
            twohand = bool(primary and (getattr(primary, "slots", 0) & 0x2000))
            if secondary is not None or twohand or self._skills.get(10, 0) > 0:
                self.client.send("OP_CombatAbility", struct.pack("<III", spawn_id, 0, 10))
                self._mark_ability("bash")

    def _can_combat_skill(self, skill_id: int) -> bool:
        """True when SkillUpdate trained it, or class has the skill and packet never arrived."""
        if skill_id in self._skills:
            return self._skills[skill_id] > 0
        class_id = self.model.class_id or 0
        # Kick: War/Pal/Rng/SK/Mnk/Brd/Rog/Bst/Ber
        if skill_id == 30:
            return class_id in {1, 3, 4, 5, 7, 8, 9, 15, 16}
        # Bash: War/Pal/SK
        if skill_id == 10:
            return class_id in {1, 3, 5}
        return False

    def _refresh_pull_cleared(self, focus_id: int = 0) -> None:
        """One pull at a time: cleared when no extra hostiles sit on the fight."""
        from eqclient.packets import is_enemy_faction

        here = self.model.position
        extras = 0
        for spawn in self.model.spawns.values():
            if spawn.npc != 1 or spawn.spawn_id == focus_id:
                continue
            if not is_enemy_faction(self.model.faction.get(spawn.spawn_id) or 0):
                continue
            if _horiz(here, (spawn.x, spawn.y, spawn.z)) <= 40:
                extras += 1
        self._pull_cleared = extras == 0

    def _accept_pending_rezz(self) -> bool:
        """Accept the last OP_RezzRequest (full Resurrect_Struct, action=1)."""
        raw = self._pending_rezz
        if not raw or len(raw) < 4:
            return False
        payload = bytearray(raw)
        struct.pack_into("<I", payload, len(payload) - 4, 1)
        self.client.send("OP_RezzAnswer", bytes(payload))
        self._pending_rezz = None
        self.client.pump(0.8)
        print("rez accepted", flush=True)
        return True

    def _rez_own_corpse_before_bury(self) -> None:
        """L10+: ^rez me while corpse still exists, then accept — bury is LootComplete."""
        self._pending_rezz = None
        # Pull healers onto the body so RezRange can succeed.
        self.client.command("botsummon spawned")
        self.client.pump(1.0)
        before = len(self.client.messages)
        self.client.command("rez me")
        print("rez me (before bury)", flush=True)
        deadline = time.monotonic() + 14.0
        while time.monotonic() < deadline:
            self.client.pump(0.4)
            if self._pending_rezz is not None:
                self._accept_pending_rezz()
                return
            blob = " ".join(self.client.messages[before:]).lower()
            if "no corpse here" in blob:
                print("rez me: no corpse", flush=True)
                return
            if "no cleric or druid" in blob:
                print("rez me: no healer in range", flush=True)
                return
            if "already has a resurrection" in blob or "already coming" in blob:
                # Offer may still arrive; keep waiting briefly.
                continue
        if self._pending_rezz is not None:
            self._accept_pending_rezz()
        else:
            print("rez me: no offer before bury", flush=True)

    def _corpse_drag_payload(self, corpse_name: str) -> bytes:
        """Titanium CorpseDrag_Struct: CorpseName[64] + DraggerName[64] + pad[24]."""
        me = self.model.character or ""
        body = (corpse_name or "").encode("latin1", "replace")[:63].ljust(64, b"\x00")
        drag = me.encode("latin1", "replace")[:63].ljust(64, b"\x00")
        return body + drag + bytes(24)

    def _drag_corpse_if_close(self, spawn_id: int) -> bool:
        """Summon own/consent corpse to our feet before loot (fixes underground pads).

        Server Summon allows ≤100yd XY, but loot only allows ≤25yd. Only drag once
        we are already inside loot range so a silent CorpseDrag failure cannot
        optimistic-snap the pad and make us open from 50–95yd away (response=5).
        """
        from eqclient.plan import _is_corpse

        if not spawn_id:
            return False
        spawn = self.model.spawns.get(spawn_id) or self._spawn_by_entity(spawn_id)
        if spawn is None or not _is_corpse(spawn.npc):
            return False
        # Player corpses only — NPC CorpseDrag is a silent no-op on the server.
        if spawn.npc not in (2, 3):
            return False
        here = self.model.position
        where = (spawn.x, spawn.y, spawn.z)
        # Stay inside loot DistanceSquaredNoZ ≤ 625 so open works even if Summon
        # is silent (MessageString is OP_FormattedMessage — we often miss it).
        if _horiz(here, where) > 20.0:
            return False
        now = time.monotonic()
        if self._corpse_drag_for == spawn_id and now - self._corpse_drag_at < 4.0:
            return False
        raw = (spawn.name or "").strip()
        # Wire name is "Name's corpseN" (space); some paths underscore.
        names = [raw]
        if " " in raw:
            names.append(raw.replace(" ", "_"))
        if "_" in raw:
            names.append(raw.replace("_", " "))
        seen: set[str] = set()
        candidates = []
        for n in names:
            if n and n not in seen:
                seen.add(n)
                candidates.append(n)
        self._corpse_drag_at = now
        self._corpse_drag_for = spawn_id
        for name in candidates:
            try:
                self.client.send("OP_CorpseDrag", self._corpse_drag_payload(name))
                self.client.pump(0.4)
            except Exception:
                continue
            # Do not snap local coords — false snaps caused TooFar loot opens.
            # Summon (when it lands) moves the body on the server; we are already
            # within 20yd so OP_LootRequest succeeds either way.
            print(f"corpse drag {name}", flush=True)
            return True
        return False

    def _loot(self, spawn_id: int, take_all: bool = False) -> None:
        from eqclient.plan import _is_corpse

        if not spawn_id:
            return
        spawn = self.model.spawns.get(spawn_id)
        if spawn is None or not _is_corpse(spawn.npc):
            self._finish_corpse(spawn_id, reason="missing")
            return
        # Bodies previously skipped on TooFar (open=5) — retry now that drag snap is fixed.
        self.skipped_corpses.discard(spawn_id)
        here = self.model.position
        where = (spawn.x, spawn.y, spawn.z)
        if _horiz(here, where) > 20.0:
            # Never open outside loot range — approach first (avoids response=5).
            return
        now = time.monotonic()
        if now - self._loot_too_far_at < 1.5 and self._loot_spawn_id == spawn_id:
            return
        # Prefer empty cursor; still open for coin even when bags are full.
        self._make_room_for_loot()
        from eqclient.items import has_loot_room

        room = has_loot_room(self.inventory)
        if self.inventory.cursor() is not None and not room and not take_all:
            # Cursor stuck and no room — still try open for MoneyOnCorpse, skip items.
            print("loot coin-only (cursor busy)", flush=True)

        before = stack_totals(self.inventory.slots)
        self.inventory.clear_corpse()
        self._loot_open = 0
        self._loot_coin_copper = 0
        self._loot_spawn_id = spawn_id
        self._target(spawn_id)
        self.client.send("OP_LootRequest", struct.pack("<I", spawn_id))
        # Give MoneyOnCorpse time to land before we decide the body is empty.
        self.client.pump(0.85)
        # 1 and 3 open the window. 5 = TooFar (≤25yd XY). Do not bury/skip on 5 —
        # keep approaching; a prior false drag-snap used to leave bodies forever.
        if self._loot_open not in (1, 3):
            if self._loot_open == 5:
                self._loot_too_far_at = now
                print(
                    f"loot too far {self._loot_corpse_tip(spawn_id)}— approach closer",
                    flush=True,
                )
                self._loot_spawn_id = 0
                return
            # 0 = SomeoneElse / ent missing (ghost spawn). 2 = Forbidden.
            # Drop local ghost so reclaim does not keep chasing a dead entity id.
            if self._loot_open in (0, 2):
                tip = self._loot_corpse_tip(spawn_id)
                gone = self.model.spawns.pop(spawn_id, None)
                where = (
                    (gone.x, gone.y, gone.z)
                    if gone is not None
                    else self.model.own_corpse_at
                )
                print(
                    f"loot ghost {tip}open={self._loot_open} — drop local spawn",
                    flush=True,
                )
                self._loot_spawn_id = 0
                self.skipped_corpses.add(spawn_id)
                # open=0 is often a temporary miss — only prune journal when we are
                # literally on the pad and no other own corpse exists in-zone.
                if take_all and where is not None:
                    self._prune_missing_journal_corpse(where, arrive=12.0)
                return
            self.client.send("OP_EndLootRequest", struct.pack("<I", spawn_id))
            self.client.pump(0.2)
            self._finish_corpse(spawn_id, reason=f"open={self._loot_open}")
            return

        # Last journaled body found — scan the zone for siblings before we clear it.
        if take_all and self.journal.outstanding_corpses(self.model.character) <= 1:
            added = self._discover_zone_corpses(skip_id=spawn_id)
            if added:
                print(
                    f"reclaim last found → +{added} more in zone; "
                    f"{self.journal.outstanding_corpses(self.model.character)} outstanding",
                    flush=True,
                )

        took = False
        seen: set[int] = set()
        # Bags come off first so the rest of the corpse has somewhere to go.
        ordered = sorted(self.inventory.corpse_slots.items(), key=lambda pair: pair[1].bag_slots == 0)
        picks: set[int] = set()
        bot_picks: set[int] = set()
        # Re-check room after open — MoneyOnCorpse already applied; items need space.
        room = has_loot_room(self.inventory)
        if not take_all:
            # Always take coin piles (even when bags are full).
            picks.update(coin_loot_slots(dict(ordered)))
            if room:
                protect = self._wanted_ids()
                build = build_for(self.model.class_id)
                score = (lambda item: held_gear_value(build, item)) if build is not None else None
                picks.update(
                    upgrade_loot_slots(
                        dict(ordered),
                        self.inventory,
                        self.model.class_id,
                        self.model.race_id,
                        self.model.level or 1,
                        protect,
                        score,
                    )
                )
                if self.tasks.local_work_left():
                    picks.update(
                        loot_picks(
                            [(slot, held.item_id, held.stack or 1) for slot, held in ordered],
                            self._held_counts(),
                            self._shortfalls(),
                        )
                    )
                # Gear a spawned bot can wear — take it so we can inventorygive after.
                if self.party.formed:
                    bot_classes = [cid for name, cid in self.party.roster if name in self.party.spawned]
                    bot_picks.update(
                        bot_usable_loot_slots(
                            dict(ordered),
                            bot_classes,
                            BOT_RACE,
                            self.model.level or 1,
                            protect,
                            skip_slots=picks,
                        )
                    )
                    picks.update(bot_picks)
            elif ordered:
                print("loot coin-only (bags full)", flush=True)
        cursor_blocked = False
        for slot, held in ordered:
            if slot in seen:
                continue
            if not take_all and slot not in picks:
                continue
            if not self._ensure_cursor_clear(why="loot"):
                cursor_blocked = True
                break
            tag = " (bot)" if slot in bot_picks else ""
            print(f"loot {held.name} slot={slot}{tag}", flush=True)
            mark = len(self.client.messages)
            self.client.send(
                "OP_LootItem",
                struct.pack("<IIH2sI", spawn_id, self.model.self_id, slot, b"\x00\x00", 0),
            )
            seen.add(slot)
            self.client.pump(0.2)
            msgs = " ".join(self.client.messages[mark:]).lower()
            if "may not loot" in msgs and "cursor" in msgs:
                # Server still holds a ghost/prior cursor item our model missed.
                tip = self._cursor_name() or "desync/unknown"
                print(f"loot blocked by cursor ({tip}) — clearing", flush=True)
                if not self._ensure_cursor_clear(why="retry", force_pump=True):
                    cursor_blocked = True
                    break
                mark = len(self.client.messages)
                self.client.send(
                    "OP_LootItem",
                    struct.pack("<IIH2sI", spawn_id, self.model.self_id, slot, b"\x00\x00", 0),
                )
                self.client.pump(0.2)
                msgs = " ".join(self.client.messages[mark:]).lower()
                if "may not loot" in msgs and "cursor" in msgs:
                    print(
                        f"loot miss {held.name} (cursor still {self._cursor_name() or 'busy'})",
                        flush=True,
                    )
                    cursor_blocked = True
                    break
            # Wait for the loot to hit the cursor, then stow before the next take.
            if not self._await_cursor(True, timeout=1.2):
                if self.inventory.cursor() is not None:
                    pass
                elif self.inventory.count(held.item_id) > before.get(held.item_id, 0):
                    took = True
                    continue
                else:
                    print(f"loot miss {held.name}", flush=True)
                    break
            if not self._stow_cursor(timeout=1.0):
                tip = self._cursor_name() or held.name
                print(f"loot cursor stuck {tip}", flush=True)
                cursor_blocked = True
                break
            took = True
        # Cursor desync mid-loot: do not journal-clear / finish. Close the window so
        # we can retry, but never treat the body as reclaimed (coin/gear may remain).
        if cursor_blocked:
            print(
                f"loot defer {self._loot_corpse_tip(spawn_id)}cursor — keep corpse",
                flush=True,
            )
            self.client.send("OP_EndLootRequest", struct.pack("<I", spawn_id))
            self.client.pump(0.2)
            self.inventory.clear_corpse()
            self._make_room_for_loot()
            # Own corpse: leave needs_corpse / journal aim so we come back.
            if take_all:
                self.model.needs_corpse = True
                self.model.own_corpse_id = spawn_id
                if spawn is not None:
                    self.model.own_corpse_at = (spawn.x, spawn.y, spawn.z)
            return
        # EndLoot deletes empty corpses — rez first while the body still exists.
        # Client→server is OP_EndLootRequest(entity); OP_LootComplete is server→client.
        if take_all and (self.model.level or 0) >= 10:
            self._rez_own_corpse_before_bury()
        if take_all:
            expected = [held for _slot, held in ordered]
            missing = missing_entries(before, stack_totals(self.inventory.slots), expected)
            self.model.note_corpse_contents(len(expected), missing)
            # Items still on the body — close window but leave journal aim intact.
            if missing > 0:
                self.client.send("OP_EndLootRequest", struct.pack("<I", spawn_id))
                self.client.pump(0.3)
                self.inventory.clear_corpse()
                print(
                    f"reclaim partial missing={missing}/{len(expected)} "
                    f"coin={self._loot_coin_copper}c — leave corpse",
                    flush=True,
                )
                return
            self.client.send("OP_EndLootRequest", struct.pack("<I", spawn_id))
            self.client.pump(0.3)
            self.inventory.clear_corpse()
            self._make_room_for_loot()
            self.score.fetched += len(expected)
            # Empty husk stays in the spawn list — skip it or we reclaim forever.
            self._finish_corpse(spawn_id, reason="reclaimed")
            remaining = self.journal.collect_corpse(
                self.model.character,
                self.model.zone or self.model.own_corpse_zone or "",
                spawn.x,
                spawn.y,
                spawn.z,
            )
            # Last (or any) reclaim: pick up other bodies still in this zone that
            # death packets missed / never hit the journal.
            added = self._discover_zone_corpses(skip_id=spawn_id)
            if added:
                remaining = self.journal.outstanding_corpses(self.model.character)
            if remaining > 0:
                # Closest outstanding body from here — never FIFO (that yanked us
                # across ecommons to a stale (554,-220) while standing on WC hills).
                self.model.needs_corpse = True
                self.model.own_corpse_id = 0
                self.model.own_corpse_at = None
                self._refresh_corpse_backlog()
                extra = f" (+{added} found in zone)" if added else ""
                aim = self.model.own_corpse_at
                tip = (
                    f" next=({aim[0]:.0f},{aim[1]:.0f},{aim[2]:.0f})"
                    if aim is not None
                    else ""
                )
                coin = f" coin={self._loot_coin_copper}c" if self._loot_coin_copper else ""
                print(
                    f"reclaim done (coin + gear){coin}; {remaining} corpse(s) still outstanding{extra}{tip}",
                    flush=True,
                )
            else:
                self.model.corpse_reclaimed()
                coin = f" coin={self._loot_coin_copper}c" if self._loot_coin_copper else ""
                print(f"reclaim done (coin + gear){coin}; 0 outstanding", flush=True)
        else:
            self.client.send("OP_EndLootRequest", struct.pack("<I", spawn_id))
            self.client.pump(0.3)
            self.inventory.clear_corpse()
            self._make_room_for_loot()
            # One pass per corpse while grinding — don't sit re-trying Bone Chips forever.
            self._finish_corpse(spawn_id, reason="done" if took else "empty")
            if took:
                self.score.fetched += 1
                self._equip()
                self._distribute_bot_gear()

    def _journal_has_corpse_near(
        self, zone: str, x: float, y: float, z: float, *, radius: float = 30.0
    ) -> bool:
        """True when an outstanding journal corpse is already at this spot."""
        want = (zone or "").lower()
        r2 = radius * radius
        for czone, cx, cy, cz, _detail in self.journal.corpses(self.model.character):
            if czone.lower() != want:
                continue
            if (cx - x) ** 2 + (cy - y) ** 2 + (cz - z) ** 2 <= r2:
                return True
        return False

    def _prune_missing_journal_corpse(
        self, where: tuple[float, float, float], *, arrive: float = 12.0
    ) -> bool:
        """Drop a journal ghost only when we are on its pad and no own body exists in-zone.

        Aggressive prune used to erase journal entries for corpses that still had coin
        (dragged / off-mesh / not yet streamed). Prefer leaving a stale aim over burying money.
        """
        from eqclient.plan import _find_own_corpse_spawn, _is_corpse, _is_own_corpse_name

        if _horiz(self.model.position, where) > arrive:
            return False
        me = self.model.character or ""
        # Any own corpse near the aim pad (wide) — do not prune.
        for spawn in self.model.spawns.values():
            if spawn.spawn_id in self.skipped_corpses:
                continue
            if not _is_corpse(spawn.npc) or not _is_own_corpse_name(me, spawn.name):
                continue
            if _horiz(where, (spawn.x, spawn.y, spawn.z)) <= 80.0:
                return False
        # Any own corpse still in the zone — retarget; never prune this pad yet.
        if _find_own_corpse_spawn(self.model, self.skipped_corpses) is not None:
            return False
        for spawn in self.model.spawns.values():
            if spawn.spawn_id in self.skipped_corpses:
                continue
            if _is_corpse(spawn.npc) and _is_own_corpse_name(me, spawn.name):
                return False
        zone = self.model.zone or self.model.own_corpse_zone or ""
        before = self.journal.outstanding_corpses(me)
        remaining = self.journal.collect_corpse(me, zone, where[0], where[1], where[2])
        if remaining >= before:
            return False
        print(
            f"reclaim prune ghost at ({where[0]:.0f},{where[1]:.0f},{where[2]:.0f}); "
            f"{remaining} outstanding",
            flush=True,
        )
        self.model.own_corpse_id = 0
        self.model.own_corpse_at = None
        if remaining > 0:
            self.model.needs_corpse = True
            self._refresh_corpse_backlog()
        else:
            self.model.needs_corpse = False
            self.model.own_corpse_zone = ""
        return True

    def _discover_zone_corpses(self, *, skip_id: int = 0) -> int:
        """Journal any of our PC corpses still spawned here that are not outstanding yet."""
        from eqclient.plan import _is_corpse, _is_own_corpse_name

        me = self.model.character or ""
        zone = self.model.zone or ""
        if not me or not zone:
            return 0
        added = 0
        for spawn in self.model.spawns.values():
            if spawn.spawn_id == skip_id or spawn.spawn_id in self.skipped_corpses:
                continue
            if not _is_corpse(spawn.npc) or not _is_own_corpse_name(me, spawn.name):
                continue
            if self._journal_has_corpse_near(zone, spawn.x, spawn.y, spawn.z):
                continue
            self.journal.remember_corpse(me, zone, spawn.x, spawn.y, spawn.z)
            added += 1
            print(
                f"reclaim found extra {spawn.name} id={spawn.spawn_id} "
                f"at ({spawn.x:.0f},{spawn.y:.0f},{spawn.z:.0f})",
                flush=True,
            )
        return added

    def _loot_corpse_tip(self, spawn_id: int | None = None) -> str:
        """`name id=N ` for loot logs, or empty if unknown."""
        sid = spawn_id if spawn_id is not None else self._loot_spawn_id
        if not sid:
            return ""
        spawn = self.model.spawns.get(sid)
        name = spawn.name if spawn is not None else "?"
        return f"{name} id={sid} "

    def _finish_corpse(self, spawn_id: int, reason: str = "") -> None:
        if not spawn_id:
            return
        self.skipped_corpses.add(spawn_id)
        self.attacked.discard(spawn_id)
        self._killed.discard(spawn_id)
        if self._loot_spawn_id == spawn_id:
            self._loot_spawn_id = 0
        if reason:
            print(f"loot skip {self._loot_corpse_tip(spawn_id)}{reason}", flush=True)

    def _cursor_name(self) -> str:
        held = self.inventory.cursor()
        return held.name if held is not None else ""

    def _ensure_cursor_clear(self, *, why: str = "", force_pump: bool = False) -> bool:
        """Stow whatever is on the cursor. False if it will not clear."""
        if force_pump:
            self.client.pump(0.4)
        self._make_room_for_loot()
        if self.inventory.cursor() is None:
            return True
        tip = self._cursor_name() or "?"
        tag = f" ({why})" if why else ""
        print(f"loot stop cursor full {tip}{tag}", flush=True)
        # One more longer stow pass — bags may free after prior moves land.
        if self._stow_cursor(timeout=1.5):
            return True
        # Bags full / bots refused — drop junk (incl. leftover weapons) so loot continues.
        if self._resolve_stuck_cursor():
            return True
        print(f"loot cursor uncleared {self._cursor_name() or tip}", flush=True)
        return False

    def _make_room_for_loot(self) -> None:
        """Stow cursor / loose items into bags so the next loot can land."""
        self._stow(limit=8)
        self._stow_cursor(timeout=1.0)
        self._stow(limit=4)
        self._stow_cursor(timeout=0.5)

    def _await_cursor(self, want: bool, timeout: float = 0.2) -> bool:
        """Pump until cursor matches want (True=occupied, False=empty)."""
        deadline = time.monotonic() + timeout
        while time.monotonic() < deadline:
            has = self.inventory.cursor() is not None
            if has == want:
                return True
            self.client.pump(0.05)
        return (self.inventory.cursor() is not None) == want

    def _stow_cursor(self, timeout: float = 0.25) -> bool:
        """Keep placing the cursor item into a bag pocket or general until clear."""
        deadline = time.monotonic() + timeout
        while self.inventory.cursor() is not None and time.monotonic() < deadline:
            if not self._clear_cursor():
                return False
            self.client.pump(0.05)
        return self.inventory.cursor() is None

    def _stow(self, limit: int = 1) -> None:
        """Move a bag onto a general slot, then loose items into its pockets."""
        for _ in range(limit):
            move = stow_move(self.inventory)
            if move is None:
                return
            if not self._move(*move):
                return

    def _train(self, spawn_id: int) -> None:
        skill = self._next_skill()
        if skill is None or self.model.points <= 0:
            self.model.points = 0
            self.client.send("OP_GMEndTraining", struct.pack("<II", spawn_id, self.model.self_id))
            return
        self._trained = False
        if not self._trainer_open:
            window = bytearray(448)
            struct.pack_into("<II", window, 0, spawn_id, self.model.self_id)
            self.client.send("OP_GMTraining", bytes(window))
            self._trainer_open = True
        # GMSkillChange_Struct: npc id, pad, skill bank 0, pad, skill id, pad.
        self.client.send("OP_GMTrainSkill", struct.pack("<H2sH2sH2s", spawn_id & 0xFFFF, b"\x00\x00", 0, b"\x00\x00", skill, b"\x00\x00"))
        self.client.pump(0.4)
        text = " ".join(self.client.messages[-4:]).lower()
        if self._trained:
            self.model.points = max(0, self.model.points - 1)
        elif "more skilled" in text:
            self._retired_skills.add(skill)
        else:
            self._retired_skills.add(skill)

    def _next_skill(self) -> int | None:
        build = build_for(self.model.class_id)
        if build is not None:
            return next_train(build, self._skills, self.model.level or 1, self._retired_skills)
        for _ in range(len(TRAIN_SKILLS)):
            skill = TRAIN_SKILLS[self._skill_index % len(TRAIN_SKILLS)]
            self._skill_index += 1
            if skill not in self._retired_skills:
                return skill
        return None


    def _held_dump_line(self, held) -> str:
        """`Item Name (ac=…)` or `-` when the slot is empty."""
        if held is None:
            return "-"
        tip = held_stats_tip(held)
        name = held.name or str(held.item_id)
        return f"{name} ({tip})" if tip else name

    def _dump_inventory(self, *, why: str = "start") -> None:
        """Print worn / pack / cursor / bag pockets in a readable layout."""
        count = len(self.inventory.slots)
        last = int(getattr(self, "_inventory_dump_count", -1))
        # Dedup only identical start dumps; always allow ready / growth re-prints.
        if why == "start" and getattr(self, "_inventory_dumped", False) and count <= last:
            return
        for held in list(self.inventory.slots.values()):
            self._enrich_held(held)
        print(f"inventory ({why}):", flush=True)
        self._inventory_dump_count = count
        print("Worn", flush=True)
        for slot, label in enumerate(WORN_NAMES):
            print(f"  {label}: {self._held_dump_line(self.inventory.slots.get(slot))}", flush=True)
        print("Inventory", flush=True)
        bags: list[tuple[int, object]] = []
        for index, slot in enumerate(GENERAL, start=1):
            held = self.inventory.slots.get(slot)
            print(f"  slot {index}: {self._held_dump_line(held)}", flush=True)
            if held is not None and held.bag_slots:
                bags.append((index, held))
        print("Cursor:", flush=True)
        print(f"  {self._held_dump_line(self.inventory.slots.get(CURSOR))}", flush=True)
        for bag_index, bag in bags:
            pockets = min(int(bag.bag_slots), BAG_SLOT_COUNT)
            print(f"Bag {bag_index} ({bag.name or bag.item_id}):", flush=True)
            parent = GENERAL.start + bag_index - 1
            for pocket in range(pockets):
                held = self.inventory.slots.get(content_slot(parent, pocket))
                print(f"  slot {pocket + 1}: {self._held_dump_line(held)}", flush=True)
        if why == "start":
            self._inventory_dumped = True

    def _enrich_held(self, held) -> None:
        """Overlay peq-cache AC/stats when the ItemPacket left them at 0."""
        book = getattr(self, "item_stats", None)
        if book is not None:
            book.enrich(held)

    def _gear_score(self):
        build = build_for(self.model.class_id)
        if build is None:
            return None
        return lambda item: held_gear_value(build, item)

    def _equip(self) -> None:
        for slot, held in list(self.inventory.slots.items()):
            if "augment" in held.name.lower():
                self.client.send("OP_AugmentItem", struct.pack("<h2sI", slot, b"\x00\x00", 0))
        protect: set[int] = set()
        for script in self.quests.scripts.values():
            for need in script.needs:
                protect.add(need.item_id)
        for need in _task_needs(self.tasks, self.quests, self.inventory):
            protect.add(need.item_id)
        build = build_for(self.model.class_id)
        score = (lambda item: held_gear_value(build, item)) if build is not None else None
        move = equip_move(self.inventory, self.model.class_id, self.model.race_id, self.model.level or 1, protect, score)
        failed = getattr(self, "_failed_equips", set())
        self._failed_equips = failed
        if move is None:
            return
        # Desync repair invalidates prior failed moves — retry upgrades.
        if any("desync" in m.lower() for m in self.client.messages[-8:]):
            failed.clear()
        if move in failed:
            return
        from_slot, to_slot = move
        held = self.inventory.slots.get(from_slot)
        tip = held.name if held is not None else f"{from_slot}→{to_slot}"
        print(f"equip {tip} → {to_slot}", flush=True)
        mark = len(self.client.messages)
        ok = self._move(from_slot, to_slot)
        self.client.pump(0.15)
        msgs = [text.lower() for text in self.client.messages[mark:]]
        # Only blacklist hard restrictions — transient "invalid" often means desync.
        if any("class, deity" in text or "sufficient level" in text for text in msgs):
            failed.add(move)
        elif not ok and any("invalid" in text or "desync" in text for text in msgs):
            failed.add(move)

    def _inventory_fatal(self, why: str) -> None:
        """Dump state and abort — inventory bugs must not be papered over."""
        print(f"inventory FATAL: {why}", flush=True)
        try:
            self._dump_inventory(why="fatal")
        except Exception as exc:
            print(f"inventory FATAL dump failed: {exc}", flush=True)
        sys.exit(-1)

    def _bootstrap_inventory(self) -> bool:
        """Block until inventory is synced and settled, then dump once.

        Print only the post-settle layout (greaves on legs, cursor empty, food in bag).
        Hard-exits if settle cannot clear the cursor.
        """
        if not getattr(self, "_char_inventory_at", 0):
            if not self.inventory.slots:
                return False
            # Inventory arrived via ItemPackets only (rare) — treat as synced.
            self._char_inventory_at = time.monotonic()
        # Allow bag/cursor ItemPackets that trail CharInventory to land.
        age = time.monotonic() - float(self._char_inventory_at)
        if age < 0.8:
            self.client.pump(0.15)
            return False
        self.client.pump(0.3)
        for held in list(self.inventory.slots.values()):
            self._enrich_held(held)
        attempts = int(getattr(self, "_inv_settle_attempts", 0))
        self._settle_gear(passes=12)
        self._inv_settle_attempts = attempts + 1
        cursor = self.inventory.cursor()
        if cursor is not None:
            tip = cursor.name or str(cursor.item_id)
            print(
                f"inventory sync waiting on cursor {tip} "
                f"(attempt {self._inv_settle_attempts}/5)",
                flush=True,
            )
            if self._inv_settle_attempts >= 5:
                self._inventory_fatal(
                    f"could not settle cursor item {tip} after "
                    f"{self._inv_settle_attempts} attempts"
                )
            return False
        self._dump_inventory(why="start")
        print("inventory sync ready", flush=True)
        return True

    def _pickup(self, drop_id: int) -> None:
        if self.inventory.cursor_blocks(self._wanted_ids()):
            self._clear_cursor()
            return
        print(f"click {drop_id}", flush=True)
        before = set(self.inventory.slots)
        self.client.send("OP_ClickObject", struct.pack("<II", drop_id, self.model.self_id))
        self.client.pump(0.5)
        if set(self.inventory.slots) == before:
            self.skipped_ground.add(drop_id)
        else:
            self.score.fetched += 1

    def _keyword(self, intention: Intention) -> None:
        """Say the quest word after hail. A plain hail, or a list of item ids, is not a word."""
        raw = (intention.text or "").split("|", 1)[0].strip()
        if not raw or raw.lower() == "hail" or raw[:1].isdigit() or raw.lower().startswith("hand:"):
            return
        self._say_keyword(intention.target, intention.name, raw)

    def _hand_in(self, spawn_id: int, item_id: int, text: str = "") -> None:
        """Put every item this script takes into the trade window, then accept once."""
        ids = _turn_ids(text, item_id)
        if not ids:
            return
        before = {item.item_id for item in self.inventory.slots.values()}
        spawn = self.model.spawns.get(spawn_id)
        name = spawn.name if spawn is not None else str(spawn_id)
        if not self._target(spawn_id):
            return
        self.client.send("OP_TradeRequest", struct.pack("<II", spawn_id, self.model.self_id))
        self.client.pump(0.4)
        placed: list[int] = []
        for index, give_id in enumerate(ids[:4]):
            if not self._offer(name, give_id, TRADE + index):
                return
            placed.append(give_id)
        if not placed:
            return
        mark = len(self.client.messages)
        self.client.send("OP_TradeAcceptClick", b"")
        self.client.pump(0.8)
        if self._move_rejected(mark):
            return
        for trade_slot in range(TRADE, TRADE + 4):
            self.inventory.slots.pop(trade_slot, None)
        returned = self.inventory.cursor()
        if returned is not None and returned.item_id not in before:
            print(f"back {returned.name}", flush=True)
        self._remember(name, "handin", "+".join(str(item) for item in placed))
        for give_id in placed:
            self._apply_handin_flags(name, give_id)
        if self.lesson is not None and self.lesson.kind == "hand_in" and _names_match(name, self.lesson.name):
            self.lesson = None

    def _offer(self, name: str, item_id: int, trade_slot: int) -> bool:
        slot = self.inventory.slot_of(item_id) if item_id else None
        held = self.inventory.slots.get(slot) if slot is not None else None
        if held is None:
            return False
        print(f"give {name} {held.name}", flush=True)
        mark = len(self.client.messages)
        blocker = self.inventory.cursor()
        if blocker is not None and blocker.item_id != item_id:
            self._clear_cursor()
            self.client.pump(0.3)
        if held.slot != CURSOR:
            self._move(held.slot, CURSOR)
            self.client.pump(0.3)
        giving = self.inventory.cursor()
        if giving is None or giving.item_id != item_id or self._move_rejected(mark):
            return False
        self._move(CURSOR, trade_slot)
        self.client.pump(0.3)
        offered = self.inventory.slots.get(trade_slot)
        return offered is not None and offered.item_id == item_id

    def _apply_handin_flags(self, npc: str, item_id: int) -> None:
        """When inventory lost a hand-in item, journal graph `sets` (never a live qglobals read)."""
        if self.graph is None or item_id <= 0:
            return
        if item_id in {held.item_id for held in self.inventory.slots.values()}:
            return
        npc_key = _key(npc)
        groups: set[str] = set()
        for edge in self.graph.edges:
            if edge.get("rel") not in {"receives", "needs"}:
                continue
            if str(edge.get("to") or "") != f"item:{item_id}":
                continue
            group = str(edge.get("group") or edge.get("from") or "")
            if npc_key in _key(group) or _key(group.split("/")[-1].split("#")[0]) == npc_key:
                groups.add(group)
        for edge in self.graph.edges:
            if edge.get("rel") != "sets":
                continue
            group = str(edge.get("group") or edge.get("from") or "")
            if groups and group not in groups:
                continue
            if not groups and npc_key not in _key(group) and _key(group.split("/")[-1].split("#")[0]) != npc_key:
                continue
            flag = str(edge.get("flag") or "")
            if not flag and str(edge.get("to") or "").startswith("flag:"):
                flag = str(edge.get("to")).split(":", 1)[1]
            if not flag:
                continue
            try:
                value = int(edge.get("value") or 1)
            except (TypeError, ValueError):
                value = 1
            self.journal.set_flag(self.model.character, flag, value)

    def _can_see(self, where: tuple[float, float, float]) -> bool:
        if self.zone_map is None:
            return True
        # Eight compass peeks so a center ray clipping a corner still counts as seen.
        return self.zone_map.clear(self.model.position, where, headings=8)

    def _in_sight(self, where: tuple[float, float, float]) -> bool:
        """True when the point is close enough to chase and the map ray is clear.

        Far outdoor clears are not sight — fall back to Find / spawn coords instead.
        """
        if _horiz(self.model.position, where) > _SIGHT_RANGE:
            return False
        return self._can_see(where)

    def _use_door(self, door_id: int, retry: bool, where: tuple[float, float, float] | None = None) -> None:
        door = self.model.doors.get(door_id)
        if door is not None and door.tried and not retry and not door.opened:
            return
        # Planner `where` is the zone_point/stone. Live door_id often collides with a
        # city door (freportw id 12 ≠ ecommons exit), so never let that override where.
        transit = self.zone_graph.transit_at(self.model.zone or "", door_id) if self.zone_graph else None
        via = (transit.via if transit is not None else "") or "door"
        # Outdoor exits: the server checks watermap InZoneLine(GetPosition()) then the
        # closest zone_points row for that dest (zone.cpp GetClosestZonePoint). Stand on
        # the painted line (correct Z) before OP_ZoneChange — mesh Z alone is often below it.
        if via == "point" and transit is not None:
            goal = self._zoneline_goal(transit) or where or (transit.x, transit.y, transit.z)
        else:
            goal = where if where is not None else ((door.x, door.y, door.z) if door is not None else None)
        here = self.model.position
        if via == "point" or (
            where is not None
            and (door is None or _horiz((door.x, door.y, door.z), where) > 30)
        ):
            dest_id = int(transit.dest_id or 0) if transit is not None else 0
            dest = (transit.dest if transit is not None else "") or ""
            on_line = self.water is not None and self.water.in_zone_line(*here)
            if goal is not None and (not on_line or _horiz(here, goal) > 12):
                # XY close but sunk under the zoneline slab (e.g. mesh z=-30, line z≥-27).
                if goal is not None and _horiz(here, goal) <= 20 and not on_line:
                    lift = (here[0], here[1], goal[2])
                    if self.water is not None and self.water.in_zone_line(*lift):
                        print(
                            f"zonepoint lift z {here[2]:.0f}->{goal[2]:.0f} "
                            f"at ({here[0]:.0f}, {here[1]:.0f})",
                            flush=True,
                        )
                        self._step(lift, direct=True, length=min(STEP, 6.0))
                        return
                self._approach(goal)
                return
            line = f" line=({goal[0]:.0f},{goal[1]:.0f},{goal[2]:.0f})" if goal is not None else ""
            print(
                f"zonepoint {door_id} -> {dest or dest_id} at "
                f"({here[0]:.0f}, {here[1]:.0f}, {here[2]:.0f}){line}"
                f"{' on_line' if on_line else ''}",
                flush=True,
            )
            # Server uses GetPosition() for InZoneLine — send ZoneChange from here only on the line.
            if on_line:
                self._zone_via_point(dest_id, here)
            if goal is not None:
                self._nudge_zonepoint(goal, transit)
            return
        if goal is not None and _horiz(here, goal) > 12:
            self._approach(goal)
            return
        if door is not None:
            print(f"click {door_id} at ({here[0]:.0f}, {here[1]:.0f})", flush=True)
            self._click_door(door_id)
            return
        # After a zone swap, OP_SpawnDoor may still be in flight — wait, don't spam.
        if not self.model.doors:
            if not getattr(self, "_missing_door_wait", 0.0) or time.monotonic() - self._missing_door_wait > 5.0:
                self._missing_door_wait = time.monotonic()
                print(f"waiting doors for {door_id}", flush=True)
            return
        print(f"missing door {door_id}", flush=True)

    def _zoneline_goal(self, transit) -> tuple[float, float, float] | None:
        """Watermap zoneline sample near this outdoor zone_points exit."""
        if self.water is None or transit is None:
            return None
        if (getattr(transit, "via", "") or "") != "point":
            return None
        here = self.model.position
        anchor = (float(transit.x), float(transit.y), float(transit.z))
        hit = self.water.nearest_zone_line(here[0], here[1], here[2], anchor=anchor)
        if hit is not None:
            return hit
        if self.water.in_zone_line(*anchor):
            return anchor
        return None

    def _zone_via_point(self, dest_zone_id: int, where: tuple[float, float, float]) -> None:
        """Unsolicited OP_ZoneChange — Titanium outdoor line cross (server: InZoneLine + zone_points)."""
        if not dest_zone_id:
            return
        now = time.monotonic()
        if now - getattr(self, "_zonepoint_at", 0.0) < 2.0:
            return
        self._zonepoint_at = now
        # Server InZoneLine uses GetPosition() — settle any in-flight step, stand on the
        # line, pump so the ClientUpdate lands, then request the zone (not same-tick).
        deadline = now + 0.6
        while not self.model.step_ready() and time.monotonic() < deadline:
            self.client.pump(0.05)
            self._settle_move()
        here = self.model.position
        if _horiz(here, where) > 2.0 or abs(here[2] - where[2]) > 1.5:
            self._step(where, direct=True, length=min(STEP, 4.0))
            self.client.pump(0.45)
            self._settle_move()
        else:
            # Re-assert current on-line coords so the zone check sees them.
            self._step(where, direct=True, length=min(2.0, STEP))
            self.client.pump(0.35)
            self._settle_move()
        here = self.model.position
        if self.water is not None and not self.water.in_zone_line(*here):
            print(
                f"OP_ZoneChange skip — not on_line at ({here[0]:.0f},{here[1]:.0f},{here[2]:.0f})",
                flush=True,
            )
            return
        name = (self.model.character or "Mockone").encode("latin1")[:63]
        x, y, z = here
        packet = bytearray(88)
        packet[: len(name)] = name
        struct.pack_into("<HH", packet, 64, int(dest_zone_id) & 0xFFFF, 0)
        struct.pack_into("<fff", packet, 68, y, x, z)  # wire order y, x, z
        struct.pack_into("<Ii", packet, 80, 0, 0)  # reason=0, success=0 (client→server)
        print(f"OP_ZoneChange dest={dest_zone_id} from=({x:.0f},{y:.0f},{z:.0f})", flush=True)
        self.client.send("OP_ZoneChange", bytes(packet))
        self.client.pump(0.5)

    def _nudge_zonepoint(self, where: tuple[float, float, float], transit) -> None:
        """Keep walking on the zoneline (outbound) so server InZoneLine stays true."""
        here = self.model.position
        safe = self.model.safe if getattr(self.model, "safe", None) else None
        # Outbound: away from zone safe / interior through the line.
        if safe is not None:
            vx, vy = where[0] - safe[0], where[1] - safe[1]
        else:
            vx, vy = where[0] - here[0], where[1] - here[1]
        if abs(vx) + abs(vy) < 1:
            heading = float(getattr(transit, "heading", 0) or 0) if transit is not None else 0.0
            rad = (heading / 512.0) * 2.0 * math.pi
            vx, vy = math.sin(rad), math.cos(rad)
        length = (vx * vx + vy * vy) ** 0.5 or 1.0
        vx, vy = vx / length, vy / length
        z = where[2]
        if self.water is not None:
            best = None
            best_score = -1.0
            for dist in (15.0, 25.0, 40.0):
                for deg in range(0, 360, 45):
                    rad = math.radians(deg)
                    dx, dy = math.sin(rad), math.cos(rad)
                    # Prefer the outbound half-plane.
                    if dx * vx + dy * vy < -0.15:
                        continue
                    nxt = (here[0] + dx * dist, here[1] + dy * dist, z)
                    if not self.water.in_zone_line(*nxt):
                        continue
                    score = dx * vx + dy * vy
                    if score > best_score:
                        best_score = score
                        best = nxt
            if best is not None:
                self._zonepoint_from = here
                self._step(best, direct=True, length=STEP)
                return
        self._zonepoint_from = here
        self._step((here[0] + vx * 25.0, here[1] + vy * 25.0, z), direct=True, length=STEP)

    def _click_door(self, door_id: int) -> None:
        door = self.model.doors.get(door_id)
        if door is not None:
            door.tried = True
        packet = bytearray(16)
        packet[0] = door_id & 0xFF
        self.client.send("OP_ClickDoor", bytes(packet))

    def _target(self, spawn_id: int) -> bool:
        """Set the server target, then hail only if that NPC is in view.

        OP_TargetMouse is what stores GetTarget. OP_TargetCommand only checks
        range and answers "I don't see anyone by that name" when it fails.
        """
        if not spawn_id:
            return False
        target = struct.pack("<I", spawn_id)
        self.client.send("OP_TargetMouse", target)
        self.client.pump(0.2)
        before = len(self.client.messages)
        self.client.send("OP_TargetCommand", target)
        self.client.pump(0.2)
        for text in self.client.messages[before:]:
            if "don't see" in text.lower():
                return False
        return True

    def _bind_gem(self, spell_id: int) -> None:
        role = role_of(self.inventory.spell_names.get(spell_id, ""))
        if not role:
            return
        for slot, memorized in self.inventory.memorized.items():
            if memorized == spell_id:
                self._gems[role] = (slot, spell_id)

    def _on_memorize(self, payload: bytes) -> None:
        slot, spell_id, scribing, _reduction = struct.unpack_from("<IIII", payload)
        if spell_id in (0, 0xFFFFFFFF):
            return
        if scribing == SCRIBE:
            self.inventory.book[slot] = spell_id
            self.inventory.scribed.add(spell_id)
            cursor = self.inventory.cursor()
            if cursor is not None and cursor.scroll_spell == spell_id:
                if cursor.stack > 1:
                    cursor.stack -= 1
                else:
                    self.inventory.slots.pop(CURSOR, None)
            print(f"scribed {self.inventory.spell_names.get(spell_id, spell_id)}", flush=True)
        elif scribing == MEMORIZE:
            self.inventory.memorized[slot] = spell_id
            self._bind_gem(spell_id)
            print(f"gem {slot} {self.inventory.spell_names.get(spell_id, spell_id)}", flush=True)

    def _scribe(self, spell_id: int) -> None:
        """Put the scroll on the cursor, then write it into the next book slot."""
        if spell_id in self.inventory.scribed or spell_id in self.inventory.failed_scrolls:
            return
        held = next((item for item in self.inventory.slots.values() if item.scroll_spell == spell_id), None)
        if held is None:
            return
        tried = getattr(self, "_scribe_at", {})
        self._scribe_at = tried
        if time.monotonic() - tried.get(spell_id, 0) < 2:
            return
        tried[spell_id] = time.monotonic()
        cursor = self.inventory.cursor()
        if cursor is not None and cursor.scroll_spell != spell_id:
            self._clear_cursor()
            self.client.pump(0.3)
        if held.slot != CURSOR:
            self._move(held.slot, CURSOR)
            self.client.pump(0.3)
        held = self.inventory.cursor()
        if held is None or held.scroll_spell != spell_id:
            return
        slot = open_book_slot(self.inventory.book)
        if slot is None:
            return
        before = len(self.client.messages)
        print(f"scribe {held.name}", flush=True)
        self.client.send("OP_MemorizeSpell", memorize_packet(slot, spell_id, SCRIBE))
        self.client.pump(0.4)
        news = " ".join(self.client.messages[before:]).lower()
        if "scribing" in news or "does not exist" in news or "too low" in news:
            self.inventory.failed_scrolls.add(spell_id)

    def _memorize(self, spell_id: int, role: str) -> None:
        """A gem only accepts a spell that is already written in the book."""
        if spell_id not in self.inventory.scribed:
            return
        if spell_id in self.inventory.memorized.values():
            self._bind_gem(spell_id)
            return
        build = build_for(self.model.class_id)
        roles = build.gems if build is not None else ()
        slot = gem_for(role, roles, self.inventory.memorized)
        if slot is None:
            return
        print(f"memorize {self.inventory.spell_names.get(spell_id, spell_id)}", flush=True)
        self.client.send("OP_MemorizeSpell", memorize_packet(slot, spell_id, MEMORIZE))

    def _learn(self) -> None:
        """Right-click the tome. That is the click that learns the combat ability."""
        held = self.inventory.tome()
        if held is None:
            return
        tried = getattr(self, "_tried_learn", set())
        self._tried_learn = tried
        slots = []
        for slot in (server_slot(held.slot), held.slot):
            if slot not in slots:
                slots.append(slot)
        if slots and all(slot in tried for slot in slots):
            self.inventory.failed_tomes.add(held.slot)
            print(f"skip {held.name}", flush=True)
            return
        for slot in slots:
            if slot in tried:
                continue
            tried.add(slot)
            print(f"learn {held.name}", flush=True)
            before = len(self.client.messages)
            self.client.send("OP_ItemVerifyRequest", struct.pack("<iI", slot, 0))
            self.client.pump(0.5)
            news = " ".join(self.client.messages[before:]).lower()
            if "learned a new discipline" in news:
                self.inventory.slots.pop(held.slot, None)
                if self.lesson is not None and self.lesson.kind == "learn":
                    self.lesson = None
                print(f"learned {held.name}", flush=True)
                return
            if "not found" not in news and "empty slot" not in news and "invalid" not in news:
                return
        if all(slot in tried for slot in slots):
            self.inventory.failed_tomes.add(held.slot)
            print(f"skip {held.name}", flush=True)

    def _wear_return(self) -> None:
        """The center inventory icon is the primary slot. The popup says to drop it there."""
        held = self.inventory.cursor()
        if held is not None:
            print(f"equip {held.name}", flush=True)
            self._move(CURSOR, PRIMARY)
        elif PRIMARY not in self.inventory.slots:
            return
        if self.lesson is not None and self.lesson.kind == "equip":
            self.lesson = None

    def _move_rejected(self, mark: int) -> bool:
        return any("desync" in text.lower() for text in self.client.messages[mark:])

    def _move(self, from_slot: int, to_slot: int) -> bool:
        """Count 0 moves the whole item. A non-stackable item with a count is rejected.

        Titanium clients apply the move locally when they send OP_MoveItem — the server
        does not ItemPacket the destination on success. Predict with note_move (swap).
        On desync the server SwapItemResync (Copper Coin token → real/DeleteItem) is
        authoritative — never restore a pre-move snapshot over those packets (that
        planted a phantom cursor item and ping-ponged stow forever).
        """
        from eqclient.items import RESYNC_TOKEN_ID

        held = self.inventory.slots.get(from_slot)
        if held is None:
            return False
        displacing = to_slot in self.inventory.slots and (
            self.inventory.slots[to_slot].item_id != RESYNC_TOKEN_ID
        )
        mark = len(self.client.messages)
        self.client.send("OP_MoveItem", struct.pack("<III", from_slot, to_slot, 0))
        self.inventory.note_move(from_slot, to_slot)
        self.client.pump(0.25)
        bad = any(
            tip in text.lower()
            for text in self.client.messages[mark:]
            for tip in ("invalid", "desync", "insufficient", "not allowed", "may not equip")
        )
        if bad:
            # Absorb Coin → real/DeleteItem for both slots; keep whatever that wrote.
            self.client.pump(0.5)
            at = getattr(self, "_failed_stow_at", None)
            if at is None:
                self._failed_stow_at = at = {}
            at[to_slot] = time.monotonic()
            self._failed_stow_dests = set(at)
            # Phantom cursor move (server source empty): resync DeleteItem'd cursor —
            # drop any leftover local cursor item so we do not stow-spam every pocket.
            if from_slot == CURSOR and any("desync" in t.lower() for t in self.client.messages[mark:]):
                if self.inventory.cursor() is not None:
                    self.inventory.slots.pop(CURSOR, None)
                    print("stow desync → drop phantom cursor", flush=True)
            return False
        # Cursor must match server after any cursor put/clear.
        if from_slot == CURSOR or to_slot == CURSOR:
            if from_slot == CURSOR:
                # Empty dest → cursor clears; occupied dest → displaced item on cursor.
                want = displacing
            else:
                want = True
            if not self._await_cursor(want, timeout=1.0):
                # Soft miss — keep prediction; next ItemPacket / CharInventory repairs.
                print(
                    f"move cursor resync pending {from_slot}→{to_slot} "
                    f"(want={'full' if want else 'empty'})",
                    flush=True,
                )
        return True

    def _destroy_cursor(self, why: str = "") -> bool:
        """Delete the cursor item on the server. Used when bags are full / bots refuse."""
        held = self.inventory.cursor()
        if held is None:
            return True
        tag = f" ({why})" if why else ""
        print(f"cursor drop {held.name}{tag}", flush=True)
        try:
            self.client.send("OP_DeleteItem", struct.pack("<I", CURSOR))
        except Exception:
            pass
        self.inventory.slots.pop(CURSOR, None)
        self.client.pump(0.2)
        return self.inventory.cursor() is None

    def _stow_room(self, held) -> list[int]:
        """Every place this cursor/item can go right now (generals, bag pockets, empty primary)."""
        from eqclient.items import empty_bag_pockets

        if held is None:
            return []
        if held.bag_slots:
            return list(self.inventory.empty_generals())
        dests = list(self.inventory.empty_generals())
        dests.extend(empty_bag_pockets(self.inventory, held))
        if PRIMARY not in self.inventory.slots and (
            held.slots == 0 or held.slots & (1 << PRIMARY)
        ):
            dests.append(PRIMARY)
        return dests

    def _free_twohand_secondary(self) -> None:
        """2H primary + secondary is illegal — park the offhand via cursor → bag/general.

        Direct secondary→general swaps fail with "selected slot was invalid" when the
        local empty slot is occupied on the server (swap would put food into secondary).
        """
        primary = self.inventory.slots.get(PRIMARY)
        secondary = self.inventory.slots.get(SECONDARY)
        if primary is None or secondary is None:
            return
        if not (getattr(primary, "slots", 0) & 0x2000):
            return
        now = time.monotonic()
        if now - float(getattr(self, "_free_2h_at", 0.0)) < 3.0:
            return
        self._free_2h_at = now
        name = secondary.name
        tip = primary.name
        # Unequip to cursor first — never swap secondary with a "empty" general.
        if self.inventory.cursor() is not None:
            if not self._stow_cursor(timeout=0.5):
                print(f"gear free secondary defer {name} (cursor busy)", flush=True)
                return
        print(f"gear free secondary {name} → cursor (2H {tip})", flush=True)
        if not self._move(SECONDARY, CURSOR):
            print(f"gear free secondary fail {name} → cursor", flush=True)
            return
        if self.inventory.slots.get(SECONDARY) is not None:
            # Move rejected / rolled weird — stop so equip cannot ping-pong.
            return
        if self.inventory.cursor() is None:
            return
        # Prefer bag pockets, then generals.
        from eqclient.items import empty_bag_pockets

        held = self.inventory.cursor()
        dests = empty_bag_pockets(self.inventory, held) + list(self.inventory.empty_generals())
        for dest in dests:
            print(f"gear free secondary {name} → {dest} (2H {tip})", flush=True)
            if self._move(CURSOR, dest) and self.inventory.cursor() is None:
                return
            if any("invalid" in m.lower() or "desync" in m.lower() for m in self.client.messages[-4:]):
                continue
        if self.inventory.cursor() is not None:
            self._stow_cursor(timeout=0.8)

    def _resolve_stuck_cursor(self) -> bool:
        """Unstick a cursor item that cannot be stowed or given. True if cleared."""
        held = self.inventory.cursor()
        if held is None:
            return True
        # Always clear the desync blacklist — it used to hide free generals
        # (only the first empty slot was tried, then blacklisted → "nowhere").
        self._failed_stow_dests = set()
        self._failed_stow_at = {}
        if self._stow_cursor(timeout=1.0):
            return True
        held = self.inventory.cursor()
        if held is None:
            return True
        room = self._stow_room(held)
        if room:
            # Space exists — MoveItem is failing (desync/phantom). Never destroy.
            now = time.monotonic()
            if now - float(getattr(self, "_stuck_cursor_log_at", 0.0)) >= 8.0:
                self._stuck_cursor_log_at = now
                print(
                    f"cursor park {held.name} "
                    f"(room={room[:6]}{'…' if len(room) > 6 else ''}, moves failing)",
                    flush=True,
                )
            return False
        protect = self._wanted_ids()
        if held.item_id in protect:
            now = time.monotonic()
            if now - float(getattr(self, "_stuck_cursor_log_at", 0.0)) >= 8.0:
                self._stuck_cursor_log_at = now
                print(f"cursor stuck protected {held.name}", flush=True)
            return False
        from eqclient.items import is_vendor_trash

        # Truly full — drop trash / refused gear so loot/reclaim can continue.
        if is_vendor_trash(held, protect) or is_wearable_gear(held):
            return self._destroy_cursor("bags full")
        return self._destroy_cursor("bags full")

    def _clear_cursor(self) -> bool:
        """Put the cursor item into a bag pocket or general slot. False if nowhere to go."""
        from eqclient.items import RESYNC_TOKEN_ID

        held = self.inventory.cursor()
        if held is None:
            return True
        # Resync token on cursor — wait for DeleteItem / real item, do not stow it.
        if held.item_id == RESYNC_TOKEN_ID:
            self.client.pump(0.3)
            held = self.inventory.cursor()
            if held is None or held.item_id == RESYNC_TOKEN_ID:
                self.inventory.slots.pop(CURSOR, None)
                return True
        now = time.monotonic()
        # Expire dest blacklists quickly — permanent skips made empty packs look full.
        raw_fail = getattr(self, "_failed_stow_at", None) or {}
        self._failed_stow_at = {
            slot: at for slot, at in raw_fail.items() if now - at < 2.5
        }
        skip = set(self._failed_stow_at)
        self._failed_stow_dests = skip
        destinations = [d for d in self._stow_room(held) if d not in skip]
        if not destinations:
            # All room blacklisted briefly — try the free slots anyway.
            destinations = self._stow_room(held)
            self._failed_stow_at = {}
            self._failed_stow_dests = set()
        if not destinations:
            if now - float(getattr(self, "_stuck_cursor_log_at", 0.0)) >= 5.0:
                self._stuck_cursor_log_at = now
                print(f"stow nowhere {held.name}", flush=True)
            return False
        for dest in destinations:
            held = self.inventory.cursor()
            if held is None:
                return True
            print(f"stow {held.name} → {dest}", flush=True)
            if self._move(CURSOR, dest) and self.inventory.cursor() is None:
                return True
            # Desync cleared a phantom cursor — stop; more dests only multiply desyncs.
            if self.inventory.cursor() is None:
                return True
            if any("desync" in m.lower() for m in self.client.messages[-6:]):
                print(f"stow fail {held.name} → {dest} (desync, stop)", flush=True)
                return self.inventory.cursor() is None
            print(f"stow fail {held.name} → {dest}", flush=True)
        return self.inventory.cursor() is None

    def _clear_bot_raid_roster(self) -> None:
        """Stop FormOnConnect from re-making a saved 10-bot raid every zone-in."""
        try:
            self.client.command("raidform clear")
            self.client.pump(0.3)
            self._party_messages()
            print("party: raidform clear (group mode)", flush=True)
        except Exception:
            pass

    def _leave_raid(self, *, camp: bool = False) -> None:
        """RaidCommandDisband (5) so group-mode botcamp is allowed."""
        who = (self.model.character or "Mockone").encode("latin1")[:63]
        field = who + b"\x00" * (64 - len(who))
        # Titanium RaidGeneral_Struct: action, player, leader, parameter.
        self.client.send(
            "OP_RaidInvite",
            struct.pack("<I", 5) + field + field + struct.pack("<I", 0),
        )
        self.client.pump(0.5)
        self._party_messages()
        if camp:
            self.client.command("botcamp spawned")
            self.client.pump(0.5)
            self._party_messages()

    def _forming_under_fire(self) -> bool:
        """True when form_party must yield for a *close* fight.

        Long-range reclaim pulls and mild HP scratches used to fall through into
        corpse-walk and never finish spawning the raid — a wipe on the pad.
        """
        here = self.model.position
        # Being chewed now — defend.
        max_hp = self.model.max_hp or 0
        if max_hp > 0 and self.model.hp * 100 < max_hp * 92:
            if self._swing_id or self._live_bot_threats() or self._engaged():
                return True
        # Live foe only counts if we're in hold/send range (not 150yd pull-park).
        for spawn_id in (self._swing_id, self._threat, self._pursuit):
            if not spawn_id:
                continue
            spawn = self.model.spawns.get(spawn_id)
            if spawn is None or spawn.npc != 1:
                continue
            if self._has_gave_up(spawn.spawn_id) and spawn_id != self._threat:
                continue
            if _horiz(here, (spawn.x, spawn.y, spawn.z)) <= _BOT_HOLD_RANGE + 15.0:
                return True
        for spawn in self._live_bot_threats():
            if _horiz(here, (spawn.x, spawn.y, spawn.z)) <= _BOT_SEND_RANGE:
                return True
        return False

    def _form_party(self) -> None:
        if not self.form_raid and getattr(self.party, "phase", "") == "camp":
            # Leftover raid from a prior run blocks botcamp while engaged.
            self._clear_bot_raid_roster()
            self._leave_raid(camp=False)
        was_formed = self.party.formed
        command = self.party.poll()
        if not command:
            return
        if command.startswith("groupinvite "):
            # XP share requires each bot in our group via OP_GroupInvite (not ^chat).
            want = command.split(" ", 1)[1]
            spawn = self._spawn_named(want) or self._bot_spawn_named(want)
            live = spawn.name if spawn is not None else want
            if spawn is not None:
                # Some rulesets require the invitee on target before OP_GroupInvite.
                self._target(spawn.spawn_id)
            print(f"group invite {live}", flush=True)
            self.client.send("OP_GroupInvite", group_invite(live, self.model.character or ""))
            self._grouped = True
            self.client.pump(0.6)
            self._party_messages()
            return
        self.client.command(command)
        if command == "botsummon spawned":
            # Zone-in lead: pull existing bots, then skip create/spawn when all live.
            self._bot_summon_at = time.monotonic()
            self._bot_order_at = self._bot_summon_at
            deadline = time.monotonic() + 2.5
            while time.monotonic() < deadline:
                self.client.pump(0.2)
                self._party_messages()
                msgs = " ".join(self.client.messages[-6:]).lower()
                if "summoned" in msgs and "bot" in msgs:
                    break
                if self._bots_close(100):
                    break
            self._sync_live_roster_bots()
            if len(self.party.spawned) >= len(self.party.roster) and self.party.spawned:
                self.party.phase = self.party._form_phase()
                print(
                    f"bots botsummon spawned (form) live={len(self.party.spawned)} → {self.party.phase}",
                    flush=True,
                )
            else:
                print(
                    f"bots botsummon spawned (form) live={len(self.party.spawned)}/{len(self.party.roster)}",
                    flush=True,
                )
        else:
            wait = 2.5 if command == "botlist" else 3.0
            deadline = time.monotonic() + wait
            while time.monotonic() < deadline and (command == "botlist" or self.party.waiting):
                self.client.pump(0.2)
                self._party_messages()
                if getattr(self.party, "blocked", False):
                    break
                if command == "botlist" and self.party.waiting != "botlist":
                    break
        # If the summary line never arrived, commit whatever botlist rows we got.
        if command == "botlist" and self.party.waiting == "botlist" and not getattr(self.party, "blocked", False):
            self.party._finish_list()
        if self.party.formed and not was_formed:
            if not self.form_raid:
                self._camp_extra_bots()
            self._space_bot_follow()
            self._enable_tank_taunt()
            # Do NOT inventorylist-all here — 30× lists starve healrotationcreate.

    def _is_reclaiming(self) -> bool:
        """True while we still owe corpse coin — bots-first aggro, owner taunt off."""
        return bool(
            self.model.needs_corpse
            or self.journal.outstanding_corpses(self.model.character) > 0
        )

    def _enable_tank_taunt(self) -> None:
        """Turn taunt on for every spawned warrior (1) and paladin (3)."""
        if not self.party.formed:
            return
        for class_id, label in ((1, "war"), (3, "pal")):
            names = [
                name
                for name, cid in self.party.roster
                if cid == class_id and name in self.party.spawned
            ]
            if not names:
                continue
            try:
                self.client.command(f"taunt on byclass {class_id}")
                self.client.pump(0.25)
            except Exception:
                for name in names:
                    try:
                        self.client.command(f"taunt on byname {name}")
                        self.client.pump(0.1)
                    except Exception:
                        pass
            print(f"bots taunt on {label} x{len(names)}", flush=True)

    def _space_bot_follow(self) -> None:
        """Stagger follow distances so the group does not stack on one point."""
        # Tight rings behind owner — 1yd steps (was 4); melee close, casters a bit out.
        by_class = {
            1: 3,    # war
            3: 4,    # pal
            16: 5,   # ber
            9: 6,    # rog
            7: 7,    # mnk
            2: 8,    # clr
            10: 9,   # shm
            6: 10,   # dru
            8: 11,   # brd
            14: 12,  # enc
            13: 13,  # mag
            11: 14,  # nec
            12: 15,  # wiz
        }
        used: set[int] = set()
        for index, (name, class_id) in enumerate(self.party.roster):
            if name not in self.party.spawned:
                continue
            dist = int(by_class.get(class_id, 5 + index))
            # Keep unique rings if two bots share a class.
            while dist in used:
                dist += 1
            used.add(dist)
            try:
                self.client.command(f"botfollowdistance set {dist} byname {name}")
                self.client.pump(0.15)
            except Exception:
                continue
            print(f"bots followdist {name}={dist}", flush=True)

    def _camp_extra_bots(self) -> None:
        """Camp owned bots outside the group roster (leftover raid companions)."""
        from eqclient.plan import _is_own_corpse_name

        roster = {name.lower() for name, _cid in self.party.roster}
        owned = {n.lower() for n in getattr(self.party, "owned", ()) or ()}
        me = self.model.character or ""
        extras: list[str] = []
        for spawn in self.model.spawns.values():
            # Bots are client-like (npc==0). Never camp PC/NPC corpses or our body —
            # "Mockone's corpse" used to match bot prefix "Moc" and get botcamp'd.
            if spawn.npc != 0:
                continue
            raw = spawn.name or ""
            if "corpse" in raw.lower() or _is_own_corpse_name(me, raw):
                continue
            if _key(raw) == _key(me):
                continue
            stem = raw.rstrip("0123456789")
            key = stem.lower()
            if key in roster or len(stem) < 5:
                continue
            # Exact botlist name only — never a short prefix (Moc → Mockone's corpse).
            if key not in owned and not any(
                key == o or (key.startswith(o) and key[len(o) :].isdigit()) for o in owned
            ):
                continue
            extras.append(stem)
        for name in sorted(set(extras)):
            print(f"camp extra bot {name}", flush=True)
            self.client.command(f"botcamp byname {name}")
            self.client.pump(0.4)
            self._party_messages()

    def _apply_group_loot_settings(self) -> None:
        """Autosplit off so corpse coin/loot stays on the agent (group leader)."""
        spawn_id = self.model.self_id & 0xFFFF
        if spawn_id:
            # AppearanceType::Split = 28; parameter 0 = no autosplit.
            self.client.send("OP_SpawnAppearance", struct.pack("<HHI", spawn_id, 28, 0))
            self.client.pump(0.2)
        self._group_loot_set = True
        print("group loot: autosplit off (agent keeps coin)", flush=True)

    def _cache_all_bot_worn(self) -> None:
        """One-shot ^inventorylist for every spawned bot not already cached."""
        listed = 0
        for name, _cid in self.party.roster:
            if name not in self.party.spawned:
                continue
            if name in self._bot_worn_listed:
                continue
            self._refresh_bot_worn(name)
            listed += 1
        if listed:
            print(f"bots inventory cached x{listed}", flush=True)

    def _refresh_bot_worn(self, bot_name: str, *, force: bool = False) -> dict[int, int]:
        """Load bot worn slots via ^inventorylist once. slot → item_id; absent = empty.

        After the first list, decisions use the local map; successful inventorygive
        updates it in place. force=True re-asks (e.g. unexpected bot return).
        """
        cached = self._bot_worn.get(bot_name)
        if not force and bot_name in self._bot_worn_listed and cached is not None:
            return cached
        before = len(self.client.messages)
        try:
            self.client.command(f"inventorylist byname {bot_name}")
            self.client.pump(0.7)
        except Exception:
            worn = dict(cached) if cached is not None else {}
            self._bot_worn[bot_name] = worn
            self._bot_worn_listed.add(bot_name)
            return worn
        worn: dict[int, int] = {}
        slot_re = re.compile(
            r"Slot\s+(\d+)\s+\([^)]+\)\s*\|\s*(.+)",
            re.IGNORECASE,
        )
        for msg in self.client.messages[before:]:
            match = slot_re.search(msg)
            if not match:
                continue
            slot = int(match.group(1))
            if slot < 0 or slot > 22:
                continue
            rest = match.group(2).strip()
            if rest.lower().startswith("empty"):
                continue
            name = rest.split("|", 1)[0].strip()
            if not name or name.lower() == "empty":
                continue
            item_id = 1
            for held in self.inventory.slots.values():
                if (held.name or "").lower() == name.lower():
                    item_id = held.item_id
                    break
            worn[slot] = item_id
        self._bot_worn[bot_name] = worn
        self._bot_worn_listed.add(bot_name)
        filled = len(worn)
        print(f"bots inventory {bot_name} {filled} worn", flush=True)
        return worn

    def _bot_empty_slot(self, held, worn: dict[int, int]) -> int | None:
        """First empty worn slot this item can fill (no replaces → no bot returns)."""
        choices = [slot for slot in WORN if held.slots & (1 << slot)]
        if not choices:
            return None
        two_hand = bool(held.slots & 0x2000)
        for slot in choices:
            if worn.get(slot, 0):
                continue
            # 2H into primary kicks secondary — only if offhand is empty too.
            if slot == PRIMARY and two_hand and worn.get(SECONDARY, 0):
                continue
            # Offhand under unknown primary: skip if primary filled (may be 2H).
            if slot == SECONDARY and worn.get(PRIMARY, 0):
                continue
            return slot
        return None

    def _inventory_give(self, bot_name: str, slot: int | None = None) -> bool:
        """Hand the cursor item to a bot via ^inventorygive byname [slot]."""
        held = self.inventory.cursor()
        if held is None or not bot_name:
            return False
        if self._under_fire() or self._engaged():
            print(
                f"inventorygive abort {held.name} → {bot_name} (under fire)",
                flush=True,
            )
            self._stow_cursor(timeout=0.25)
            return False
        if slot is None:
            worn = self._refresh_bot_worn(bot_name)
            slot = self._bot_empty_slot(held, worn)
            if slot is None:
                self._bot_given.add((bot_name, held.item_id))
                print(
                    f"inventorygive skip {held.name} → {bot_name} (no empty slot)",
                    flush=True,
                )
                self._stow_cursor(timeout=0.25)
                return False
        before = len(self.client.messages)
        item_id = held.item_id
        name = held.name
        self.client.command(f"inventorygive byname {bot_name} {slot}")
        self.client.pump(0.8)
        if self._under_fire() or self._engaged():
            print(
                f"inventorygive abort {name} → {bot_name} (aggro mid-trade)",
                flush=True,
            )
            self._bot_given.add((bot_name, item_id))
            self._stow_cursor(timeout=0.25)
            return False
        msgs = [m.lower() for m in self.client.messages[before:]]
        accepted = any("accept" in m for m in msgs)
        returned = any("returned" in m for m in msgs)
        cursor = self.inventory.cursor()
        gone = cursor is None or cursor.item_id != item_id
        ok = gone or accepted or any(
            tip in m for m in msgs for tip in ("gave ", "equip", "received")
        )
        if ok:
            self._bot_given.add((bot_name, item_id))
            self._gear_settle_gave = True
            # Update local worn map — empty-slot give should not return gear.
            worn = self._bot_worn.setdefault(bot_name, {})
            worn[slot] = item_id
            if held.slots & 0x2000:
                worn.pop(SECONDARY, None)
            print(f"inventorygive {name} → {bot_name} slot={slot}", flush=True)
            cursor = self.inventory.cursor()
            if cursor is not None and cursor.item_id == item_id and accepted:
                self.inventory.slots.pop(CURSOR, None)
                print(f"inventorygive cursor clear {name} (accepted)", flush=True)
            elif cursor is not None:
                self._stow_cursor(timeout=0.5)
            if returned:
                # Unexpected replace — one re-list for this bot only.
                self._bot_worn_listed.discard(bot_name)
                self._refresh_bot_worn(bot_name, force=True)
            return True
        self._bot_given.add((bot_name, item_id))
        self._bot_worn_listed.discard(bot_name)
        print(f"inventorygive fail {name} → {bot_name}", flush=True)
        self._stow_cursor(timeout=0.25)
        return False

    def _bot_for_gear(self, held) -> tuple[str, int] | None:
        """Pick a spawned bot with an empty slot this item can fill."""
        level = self.model.level or 1
        candidates: list[tuple[int, str, int]] = []
        for bot_name, class_id in self.party.roster:
            if bot_name not in self.party.spawned:
                continue
            if (bot_name, held.item_id) in self._bot_given:
                continue
            if not fits(held, class_id, BOT_RACE, level):
                continue
            worn = self._refresh_bot_worn(bot_name)
            slot = self._bot_empty_slot(held, worn)
            if slot is None:
                continue
            score = 0
            if held.damage > 0:
                score += 2
            if held.ac > 0:
                score += 1
            # Prefer emptier bots so gear spreads.
            score += max(0, 8 - len(worn))
            candidates.append((score, bot_name, slot))
        if not candidates:
            return None
        candidates.sort(reverse=True)
        _score, bot_name, slot = candidates[0]
        return bot_name, slot

    def _gear_pending(self) -> bool:
        """True when cursor/bags still hold armor/weapons to equip or give."""
        protect = self._wanted_ids()
        level = self.model.level or 1
        agent_class = self.model.class_id or 0
        agent_race = self.model.race_id or 0
        build = build_for(agent_class)
        score = (lambda item: held_gear_value(build, item)) if build is not None else None
        for slot, held in list(self.inventory.slots.items()):
            if held.bag_slots or held.item_id in protect or slot in WORN:
                continue
            if not is_wearable_gear(held):
                continue
            if fits(held, agent_class, agent_race, level) and _upgrade_slot(self.inventory, held, score) is not None:
                return True
            if self.party.formed and self._bot_for_gear(held) is not None:
                return True
        return False

    def _settle_gear(self, *, passes: int = 8) -> bool:
        """Wear upgrades, stow junk, inventorygive leftovers before reclaim/shop/grind.

        Returns True when something moved (worn set / cursor / bag count changed).
        Always resolves a non-empty cursor (food → bag, upgrades → worn, junk → bots).
        """
        self._gear_settle_progress = False
        self._gear_settle_gave = False
        if self.inventory.tome() is not None:
            return False
        if self.lesson is not None and self.lesson.kind == "equip":
            return False
        if self._under_fire() or self._engaged():
            if self.inventory.cursor() is not None:
                self._stow_cursor(timeout=0.3)
            return False
        for held in list(self.inventory.slots.values()):
            self._enrich_held(held)
        self._free_twohand_secondary()
        moved = False
        for _ in range(passes):
            if self._under_fire() or self._engaged():
                if self.inventory.cursor() is not None:
                    self._stow_cursor(timeout=0.3)
                break
            primary = self.inventory.slots.get(PRIMARY)
            if primary is not None and primary.item_type == ITEM_FISHING_POLE:
                break
            gave_before = self._gear_settle_gave
            before = (
                self.inventory.cursor().item_id if self.inventory.cursor() else 0,
                len(self.inventory.slots),
                tuple(sorted((s, h.item_id) for s, h in self.inventory.slots.items() if s in WORN)),
            )
            # Cursor first: equip upgrade, else give wearable, else stow (bread etc.).
            cursor = self.inventory.cursor()
            if cursor is not None:
                self._enrich_held(cursor)
                if is_wearable_gear(cursor):
                    self._equip()
                    cursor = self.inventory.cursor()
                if cursor is not None and is_wearable_gear(cursor):
                    self._distribute_bot_gear()
                    cursor = self.inventory.cursor()
                if cursor is not None:
                    self._stow_cursor(timeout=1.0)
                # Still stuck after stow/give — drop junk so reclaim is not blocked.
                if self.inventory.cursor() is not None:
                    self._resolve_stuck_cursor()
            self._equip()
            self._distribute_bot_gear()
            # Stow any displaced starter junk still on the cursor (burlap after greaves).
            if self.inventory.cursor() is not None:
                cursor = self.inventory.cursor()
                if cursor is not None and is_wearable_gear(cursor):
                    self._distribute_bot_gear()
                if self.inventory.cursor() is not None:
                    self._stow_cursor(timeout=1.0)
                if self.inventory.cursor() is not None:
                    self._resolve_stuck_cursor()
            else:
                self._stow()
            after = (
                self.inventory.cursor().item_id if self.inventory.cursor() else 0,
                len(self.inventory.slots),
                tuple(sorted((s, h.item_id) for s, h in self.inventory.slots.items() if s in WORN)),
            )
            # Give+bot-return is often net-zero on slot count — still real progress.
            if after != before or self._gear_settle_gave != gave_before:
                moved = True
                self._gear_settle_progress = True
            else:
                break
        return moved

    def _distribute_bot_gear(self) -> None:
        """Equip player upgrades, then inventorygive leftover gear to bots."""
        if not self.party.formed:
            return
        if self._under_fire() or self._engaged():
            if self.inventory.cursor() is not None:
                self._stow_cursor(timeout=0.25)
            return
        protect = self._wanted_ids()
        level = self.model.level or 1
        agent_class = self.model.class_id or 0
        agent_race = self.model.race_id or 0
        build = build_for(agent_class)
        score = (lambda item: held_gear_value(build, item)) if build is not None else None

        def _keep_for_self(held) -> bool:
            if not fits(held, agent_class, agent_race, level):
                return False
            return _upgrade_slot(self.inventory, held, score) is not None

        # Cursor first — a stuck greave used to abort the whole pass via early return.
        cursor = self.inventory.cursor()
        if cursor is not None and cursor.item_id not in protect and is_wearable_gear(cursor):
            if _keep_for_self(cursor):
                self._equip()
                cursor = self.inventory.cursor()
            if cursor is not None and not _keep_for_self(cursor):
                offer = self._bot_for_gear(cursor)
                if offer is not None:
                    self._inventory_give(offer[0], offer[1])
                elif not self._stow_cursor(timeout=0.4):
                    stuck = self.inventory.cursor()
                    if stuck is not None:
                        now = time.monotonic()
                        if now - float(getattr(self, "_stuck_cursor_log_at", 0.0)) >= 5.0:
                            self._stuck_cursor_log_at = now
                            print(f"gear cursor stuck {stuck.name}", flush=True)
                        self._resolve_stuck_cursor()

        for slot, held in list(self.inventory.slots.items()):
            if self._under_fire() or self._engaged():
                if self.inventory.cursor() is not None:
                    self._stow_cursor(timeout=0.25)
                return
            if slot in WORN or slot == CURSOR or held.bag_slots:
                continue
            if held.item_id in protect:
                continue
            if not is_wearable_gear(held):
                continue
            if _keep_for_self(held):
                continue
            offer = self._bot_for_gear(held)
            if offer is None:
                continue
            bot_name, dest_slot = offer
            if self.inventory.cursor() is not None and not self._stow_cursor(timeout=0.25):
                stuck = self.inventory.cursor()
                if stuck is not None:
                    alt = self._bot_for_gear(stuck)
                    if alt is not None:
                        self._inventory_give(alt[0], alt[1])
                if self.inventory.cursor() is not None:
                    break
            if not self._move(slot, CURSOR):
                continue
            if not self._await_cursor(True, timeout=0.5):
                continue
            self._inventory_give(bot_name, dest_slot)

    def _setup_bot_heal(self) -> None:
        """Cleric healrotation: load saved if good, else rebuild once.

        `healrotationcreate` auto-loads the DB save onto a new instance. Prefer that
        path — full delete/rebuild (30 targets + armor loops) stalls reclaim badly.
        """
        clr = next((name for name, class_id in self.party.roster if class_id == 2), "")
        if not clr or clr not in self.party.spawned:
            return
        me = self.model.character or ""
        if not me:
            return
        clerics = [
            name
            for name, cid in self.party.roster
            if cid == 2 and name in self.party.spawned
        ]

        def _bot(cmd: str, wait: float = 0.8) -> list[str]:
            before = len(self.client.messages)
            self.client.command(cmd)
            self.client.pump(wait)
            self._party_messages()
            return list(self.client.messages[before:])

        def _dump(label: str, msgs: list[str]) -> None:
            if not msgs:
                print(f"healrotation {label}: (no server reply)", flush=True)
                return
            for msg in msgs:
                shown = "".join(ch if 32 <= ord(ch) < 127 else "?" for ch in msg)
                if len(shown) > 160:
                    shown = shown[:160] + "..."
                print(f"healrotation {label}: {shown}", flush=True)

        def _has(msgs: list[str], *needles: str) -> bool:
            blob = " ".join(msgs).lower()
            return any(n.lower() in blob for n in needles)

        def _parse_list(msgs: list[str]) -> dict:
            members: list[str] = []
            targets: list[str] = []
            section = ""
            fast = adaptive = override = False
            active = False
            name_re = re.compile(r"^\((\d+)\)\s+(\S+)")
            for raw in msgs:
                line = "".join(ch if 32 <= ord(ch) < 127 else " " for ch in raw).strip()
                low = line.lower()
                if "heal rotation members" in low:
                    section = "members"
                    continue
                if "heal rotation targets" in low:
                    section = "targets"
                    continue
                if "heal rotation settings" in low or low.startswith("current state:"):
                    section = "settings"
                if "fast heals:" in low and "'on'" in low:
                    fast = True
                if "adaptive targeting:" in low and "'on'" in low:
                    adaptive = True
                if "casting override:" in low and "'on'" in low:
                    override = True
                if "current state: active" in low:
                    active = True
                match = name_re.match(line)
                if match and section == "members":
                    members.append(match.group(2))
                elif match and section == "targets":
                    targets.append(match.group(2))
            return {
                "members": members,
                "targets": targets,
                "fast": fast,
                "adaptive": adaptive,
                "override": override,
                "active": active,
            }

        def _usable(info: dict) -> bool:
            """Good enough to heal — owner targeted and at least the lead cleric seated."""
            targets_l = {t.lower() for t in info.get("targets") or []}
            members_l = {m.lower() for m in info.get("members") or []}
            if me.lower() not in targets_l:
                return False
            if not targets_l or "(0) none" in targets_l:
                return False
            return clr.lower() in members_l or bool(members_l)

        def _needs_full_rebuild(info: dict) -> bool:
            """Only wipe when the rotation cannot heal the owner at all."""
            return not _usable(info)

        def _patch_rotation(info: dict) -> bool:
            """Add missing clerics / flags / start — never delete a working pool."""
            members_l = {m.lower() for m in info.get("members") or []}
            for name in clerics:
                if name == clr or name.lower() in members_l:
                    continue
                msgs = _bot(f"healrotationaddmember {name} {clr}", 0.7)
                if _has(msgs, "successfully added", "already a current member"):
                    print(f"heal member +{name}", flush=True)
                else:
                    print(f"heal member skip {name}", flush=True)
            if not info.get("fast"):
                _bot(f"healrotationfastheals {clr} on", 0.35)
            if not info.get("adaptive"):
                _bot(f"healrotationadaptivetargeting {clr} on", 0.35)
            if not info.get("override"):
                _bot(f"healrotationcastingoverride {clr} on", 0.35)
            if not _start_rotation(have_me=True):
                return False
            _bot(f"healrotationsave {clr}", 0.5)
            return True

        def _start_rotation(*, have_me: bool) -> bool:
            started = _bot(f"healrotationstart {clr}", 1.0)
            ok = _has(started, "now active") or (
                have_me and _has(started, "already active")
            )
            if _has(started, "failed to start"):
                ok = False
            if ok:
                print(f"healrotation {clr} active", flush=True)
            else:
                print(f"healrotation {clr} start failed", flush=True)
                _dump("start", started)
            return ok

        def _finish_support() -> None:
            """Spell thresholds / caster prefs — not part of HR save, still needed."""
            me_spawn = self._spawn_named(me)
            if me_spawn is not None and not self.model.self_id:
                self.model.self_id = me_spawn.spawn_id
            if not self.model.self_id:
                deadline = time.monotonic() + 3.0
                while not self.model.self_id and time.monotonic() < deadline:
                    self.client.pump(0.2)
                    self._party_messages()
            me_id = (self.model.self_id or (me_spawn.spawn_id if me_spawn else 0)) & 0xFFFF
            if me_id:
                for spell_type in (1, 26, 27, 28):
                    self.client.send("OP_TargetMouse", struct.pack("<I", 0))
                    self.client.pump(0.1)
                    self.client.send("OP_TargetMouse", struct.pack("<I", me_id))
                    self.client.pump(0.2)
                    _bot(f"spellmaxthresholds {spell_type} 95", 0.45)
                print(f"heal thresholds self_id={me_id}", flush=True)
            for spell_type in (1, 26, 27, 28):
                _bot(f"spellmaxthresholds {spell_type} 95 spawned", 0.3)
            if clr_spawn is not None:
                self._target(clr_spawn.spawn_id & 0xFFFF)
                for spell_id, label in ((17, "Light Healing"), (200, "Minor Healing")):
                    before = len(self.client.messages)
                    self.client.command(f"spellsettingsupdate {spell_id} 1 0 100")
                    self.client.pump(0.35)
                    msgs = list(self.client.messages[before:])
                    if _has(msgs, "successfully updated", "successfully added", "already has a spell setting"):
                        print(f"heal spell ok {label} ({spell_id})", flush=True)
                    else:
                        self.client.command(f"spellsettingsadd {spell_id} 1 0 100")
                        self.client.pump(0.35)
                        print(f"heal spell add {label} ({spell_id})", flush=True)
                _bot("enforcespellsettings false", 0.35)
            _bot(f"sitmanapercent 90 byname {clr}", 0.35)
            _caster_no_melee = {2, 6, 10, 11, 12, 13, 14}
            for name, cid in self.party.roster:
                if cid not in _caster_no_melee or name not in self.party.spawned:
                    continue
                _bot(f"botstopmeleelevel 1 byname {name}", 0.25)
            self._enable_tank_taunt()
            self._rally_bots(force=True, why="heal")
            self._heal_rotation_set = True
            self._bot_report_at = 0.0
            self._maybe_bot_report()
            self._seek_bot_spells()

        def _add_target(name: str) -> bool:
            msgs = _bot(f"healrotationaddtarget {name} {clr}", 0.7)
            if _has(msgs, "successfully added heal target"):
                print(f"heal target +{name}", flush=True)
                return True
            if _has(msgs, "failed to add heal target"):
                _bot(f"healrotationremovetarget {name} {clr}", 0.45)
                msgs = _bot(f"healrotationaddtarget {name} {clr}", 0.7)
                if _has(msgs, "successfully added heal target"):
                    print(f"heal target +{name} (readd)", flush=True)
                    return True
                print(f"heal target fail {name}", flush=True)
                return False
            if _has(msgs, "no target exists"):
                print(f"heal target miss {name}", flush=True)
                return False
            return False

        def _rebuild() -> bool:
            """Wipe and build members/targets/limits from scratch, then save."""
            _bot(f"healrotationstop {clr}", 0.45)
            _bot(f"healrotationcleartargets {clr}", 0.45)
            _bot(f"healrotationremovemember {clr}", 0.45)
            _bot(f"healrotationdelete {clr}", 0.6)
            created = _bot(f"healrotationcreate {clr} 3 on on on", 1.2)
            _dump("create", created)
            if not _has(created, "successfully added", "successfully loaded"):
                _bot(f"healrotationremovemember {clr}", 0.45)
                created = _bot(f"healrotationcreate {clr} 3 on on on", 1.2)
                _dump("create-retry", created)
            if not _has(
                created,
                "successfully added",
                "successfully loaded",
                "already a current member",
            ):
                return False
            for name in clerics:
                if name == clr:
                    continue
                msgs = _bot(f"healrotationaddmember {name} {clr}", 0.7)
                if _has(msgs, "successfully added", "already a current member"):
                    print(f"heal member +{name}", flush=True)
                else:
                    print(f"heal member fail {name}", flush=True)
            targets: list[str] = [me]
            for name, _cid in self.party.roster:
                if name not in self.party.spawned:
                    continue
                if name not in targets:
                    targets.append(name)
            print(
                f"healrotation {clr} build → {', '.join(targets)} critical=50% safe=75%",
                flush=True,
            )
            _bot(f"healrotationcleartargets {clr}", 0.45)
            have_me = _add_target(me) or _add_target(me)
            for name in targets:
                if name == me:
                    continue
                _add_target(name)
            if not have_me:
                print(f"healrotation {clr} no owner target — abort rebuild", flush=True)
                return False
            for armor in range(5):
                _bot(f"healrotationadjustsafe {armor} 75 {clr}", 0.3)
            for armor in range(5):
                _bot(f"healrotationadjustcritical {armor} 50 {clr}", 0.3)
            _bot(f"healrotationfastheals {clr} on", 0.35)
            _bot(f"healrotationadaptivetargeting {clr} on", 0.35)
            _bot(f"healrotationcastingoverride {clr} on", 0.35)
            if not _start_rotation(have_me=True):
                return False
            _bot(f"healrotationsave {clr}", 0.8)
            return True

        clr_spawn = self._bot_spawn_named(clr)
        if clr_spawn is not None:
            self._target(clr_spawn.spawn_id & 0xFFFF)

        # Fast path: create (auto-loads DB save) or list if already a member.
        created = _bot(f"healrotationcreate {clr} 3 on on on", 1.2)
        _dump("create", created)
        loaded = _has(created, "successfully loaded", "already a current member")
        fresh = _has(created, "successfully added") and not loaded
        listed = _bot(f"healrotationlist {clr}", 1.2)
        info = _parse_list(listed)
        if not _has(listed, "heal rotation settings") and not loaded and not fresh:
            print(f"healrotation {clr} create failed — retry later", flush=True)
            self._heal_rotation_at = time.monotonic()
            return

        have_me = me.lower() in {t.lower() for t in info.get("targets") or []}
        if _usable(info):
            missing = [
                n for n in clerics if n.lower() not in {m.lower() for m in info["members"]}
            ]
            tip = "loaded ok" if not missing else f"patch +{','.join(missing)}"
            print(
                f"healrotation {clr} {tip} "
                f"members={len(info['members'])} targets={len(info['targets'])}",
                flush=True,
            )
            if not _patch_rotation(info):
                # Usable pool — do not delete; accept and move on so we never hard-lock.
                print(f"healrotation {clr} patch/start soft-fail — keep going", flush=True)
                _bot(f"healrotationstart {clr}", 0.8)
            _finish_support()
            return

        if not _needs_full_rebuild(info):
            print(f"healrotation {clr} unexpected state — patch", flush=True)
            if _patch_rotation(info):
                _finish_support()
            else:
                self._heal_rotation_at = time.monotonic()
            return

        why = "empty" if fresh else "broken"
        print(
            f"healrotation {clr} {why} "
            f"(members={info.get('members')} has_me={have_me}) — rebuild",
            flush=True,
        )
        if not _rebuild():
            # Never spin forever after a wipe — accept whatever is left and continue.
            print(f"healrotation {clr} rebuild failed — continue without lock", flush=True)
            self._heal_rotation_set = True
            self._heal_rotation_at = time.monotonic()
            return
        _finish_support()

    def _sync_live_roster_bots(self) -> None:
        """Mark roster bots already in the zone as owned+spawned (same-zone re-login)."""
        for name, _cid in self.party.roster:
            spawn = self._bot_spawn_named(name)
            if spawn is None:
                continue
            self.party.owned.add(name)
            self.party.spawned.add(name)

    def _bot_spawn_named(self, name: str):
        """Find a spawned bot whose name matches roster stem (Mocwar → Mocwar000)."""
        wanted = _key(name).replace(" ", "")
        best = None
        for spawn in self.model.spawns.values():
            if spawn.npc != 0:
                continue
            stem = _key(spawn.name).replace(" ", "")
            # Strip trailing instance digits the client appends to duplicates.
            base = stem.rstrip("0123456789")
            if base == wanted or stem == wanted:
                if best is None or len(stem) < len(_key(best.name).replace(" ", "")):
                    best = spawn
        return best

    def set_goal_item(self, item_id: int, count: int = 1, *, replace: bool = False) -> bool:
        """Assign an item goal. Default pushes on top; replace=True clears prior stack."""
        ok = (
            self.campaign.set_goal(item_id, count, graph=self.graph)
            if replace
            else self.campaign.assign_goal(item_id, count, graph=self.graph)
        )
        if ok:
            self._persist_goals()
        return ok

    def _maybe_soulbind(self, intention: Intention | None) -> Intention | None:
        """Before grinding a camp, bind at the nearest soulbinder unless journal says we already did."""
        if intention is None:
            return None
        grind_zone = ""
        why = str(intention.text or "")
        if intention.kind == "grind":
            grind_zone = (intention.name or self.model.zone or "").lower()
        elif intention.kind in ("fight", "task_kill") and why.startswith("grind"):
            grind_zone = (self.model.zone or "").lower()
        elif intention.kind == "leave" and why.startswith("grind"):
            # Still traveling to the camp — bind after we arrive.
            return intention
        elif intention.kind == "soulbind":
            return intention
        else:
            return intention
        if not grind_zone:
            return intention
        binder = nearest_soulbinder(grind_zone)
        if binder is None:
            return intention
        bound = (self.journal.soulbind_zone(self.model.character) or "").lower()
        if bound == binder.zone or bound == grind_zone:
            return intention
        here = (self.model.zone or "").lower()
        if binder.zone != here:
            travel = self._travel_intention(binder.zone, text=f"soulbind for {grind_zone}")
            return travel if travel is not None else intention
        spawn = self._spawn_by_substring("soulbinder") or self._spawn_named(binder.name)
        if spawn is not None:
            return Intention(
                "soulbind",
                target=spawn.spawn_id,
                name=spawn.name,
                where=(spawn.x, spawn.y, spawn.z),
                text=grind_zone,
            )
        return Intention(
            "soulbind",
            name=binder.name,
            where=(binder.x, binder.y, binder.z),
            text=grind_zone,
        )

    def _do_soulbind(self, intention: Intention) -> None:
        """Walk to the soulbinder, hail, say bind my soul; journal on success chat."""
        spawn = self.model.spawns.get(intention.target) if intention.target else None
        if spawn is None:
            spawn = self._spawn_by_substring("soulbinder") or self._spawn_named(intention.name or "")
        where = (
            (spawn.x, spawn.y, spawn.z)
            if spawn is not None
            else intention.where
        )
        if where is None:
            return
        if _horiz(self.model.position, where) > _ACT_RANGE.get("soulbind", 25.0):
            self._approach(where, spawn.spawn_id if spawn is not None else 0)
            return
        now = time.monotonic()
        if now - self._soulbind_at < 3.0:
            return
        self._soulbind_at = now
        spawn_id = spawn.spawn_id if spawn is not None else intention.target
        name = (spawn.name if spawn is not None else intention.name) or "Soulbinder"
        if spawn_id and not self._target(spawn_id):
            return
        print(f"soulbind ask {name} for {(intention.text or self.model.zone or '?')}", flush=True)
        self.client.say("hail")
        self.client.pump(0.5)
        before = len(self.client.messages)
        self.client.say("bind my soul")
        self.client.pump(1.0)
        for message in self.client.messages[before:]:
            if "bind to the area" in message.lower():
                self._note_soulbind(intention.text or self.model.zone or "")
                return

    def _note_soulbind(self, zone: str = "") -> None:
        """Persist current soulbind zone so the next grind can skip."""
        short = (zone or self.model.zone or "").lower().strip()
        if not short:
            return
        prev = self.journal.soulbind_zone(self.model.character)
        self.journal.set_soulbind(self.model.character, short)
        if self.model.zone_id:
            self.model.home_zone_id = self.model.zone_id
        if prev != short:
            print(f"soulbind {short}" + (f" (was {prev})" if prev else ""), flush=True)

    def _is_zone_dest(self, name: str) -> bool:
        """True when `name` is a known short zone (graph / camps / remembered)."""
        from eqclient.zones import canonical_zone, zone_id_of, ZONE_ALIASES
        from eqclient.camps import XP_CAMPS

        n = canonical_zone(name)
        if not n:
            return False
        if (name or "").lower().strip() in ZONE_ALIASES:
            return True
        zg = self.zone_graph
        if zg is not None and n in getattr(zg, "zones", {}):
            return True
        if zone_id_of(n):
            return True
        return any(c.zone == n for c in XP_CAMPS)

    def _travel_intention(self, dest: str, text: str = "", item_id: int = 0) -> Intention | None:
        """Leave via first_leg when dest is another zone; else explore toward dest."""
        from eqclient.zones import canonical_zone

        dest = canonical_zone(dest)
        here = (self.model.zone or "").lower()
        if not dest or dest == here:
            return None
        held = {held.item_id for held in self.inventory.slots.values()}
        lockpick = int(self._skills.get(35, 0) or 0)
        travel_graph = self.zone_graph or self.graph
        # Do not filter by live OP_Doors ids — zone_point numbers collide with
        # city door ids and gating drops outdoor exits (e.g. freportw→ecommons).
        leg = (
            first_leg(
                travel_graph,
                here,
                dest,
                inventory_ids=held,
                lockpick_skill=lockpick,
                flags=self.journal.flag_values(self.model.character),
            )
            if travel_graph
            else None
        )
        if leg is not None and here == leg.zone:
            transit = self.zone_graph.transit_at(leg.zone, leg.door_id) if self.zone_graph else None
            if transit is not None and (transit.x or transit.y or transit.z):
                spot = self._zoneline_goal(transit) or (transit.x, transit.y, transit.z)
                return Intention(
                    "leave",
                    target=leg.door_id,
                    name=leg.dest,
                    where=spot,
                    text=transit.name or text or dest,
                    item_id=item_id,
                )
            door = self.model.doors.get(leg.door_id)
            if door is not None:
                return Intention(
                    "leave",
                    target=door.door_id,
                    name=leg.dest,
                    where=(door.x, door.y, door.z),
                    text=text or dest,
                    item_id=item_id,
                )
            return Intention("leave", target=leg.door_id, name=leg.dest, text=text or dest, item_id=item_id)
        return Intention("explore", name=dest, text=text or "travel", item_id=item_id)

    def _resolve_zone_travel(self, intention: Intention | None) -> Intention | None:
        """Rewrite grind/explore named for another zone into leave/explore travel."""
        if intention is None or intention.kind not in ("explore", "grind"):
            return intention
        dest = (intention.name or "").lower().strip()
        here = (self.model.zone or "").lower()
        if not dest or dest == here or not self._is_zone_dest(dest):
            return intention
        travel = self._travel_intention(dest, text=intention.text or "", item_id=intention.item_id or 0)
        return travel if travel is not None else intention

    def _campaign_intention(self, step: CampaignStep) -> Intention | None:
        """Map a campaign step onto an Intention the act loop already knows."""
        if step.kind == "done":
            return None
        if step.kind in {"safe", "sell", "bank"}:
            if step.kind == "sell":
                merchant = self._nearest_merchant()
                if merchant is not None:
                    return Intention(
                        "shop",
                        target=merchant.spawn_id,
                        name=merchant.name,
                        where=(merchant.x, merchant.y, merchant.z),
                        item_id=step.item_id,
                        text="sell",
                    )
            if step.kind == "bank":
                banker = self._spawn_named("banker") or self._spawn_by_substring("bank")
                if banker is not None:
                    return Intention("bank", target=banker.spawn_id, name=banker.name, where=(banker.x, banker.y, banker.z))
            return Intention("explore", name="safe", where=self.model.safe)
        if step.kind == "travel" and step.zone:
            return self._travel_intention(step.zone, text=step.npc or "", item_id=step.item_id) or Intention(
                "explore", name=step.zone, text=step.npc
            )
        if step.kind == "craft" and step.recipe_id:
            return Intention("craft", target=step.recipe_id, item_id=step.item_id)
        if step.kind == "buy":
            if step.item_id and bags_buyable(self.inventory) <= 0:
                name = str((getattr(self.graph, "items", None) or {}).get(int(step.item_id), {}).get("name") or "").lower()
                if step.item_id == BACKPACK_ITEM or "backpack" in name:
                    return None
            spawn = self._spawn_named(step.npc) if step.npc else self._nearest_merchant(item_id=step.item_id)
            if spawn is not None:
                return Intention("shop", target=spawn.spawn_id, name=spawn.name, item_id=step.item_id, where=(spawn.x, spawn.y, spawn.z), text="buy")
            return Intention("explore", name=step.npc or "merchant")
        if step.kind in {"hail", "hand"} and step.npc:
            spawn = self._spawn_named(step.npc)
            if spawn is not None:
                kind = "hand_in" if step.kind == "hand" else "task_talk"
                intent = Intention(kind, spawn.spawn_id, spawn.name, step.item_id, (spawn.x, spawn.y, spawn.z), text=step.word or "Hail")
                return intent
            if step.zone and (self.model.zone or "").lower() != step.zone.lower():
                return Intention("explore", name=step.zone, text=step.npc)
            return Intention("explore", name=step.npc)
        if step.kind in {"kill", "loot"} and step.npc:
            spawn = self._spawn_named(step.npc)
            if spawn is not None:
                return Intention("task_kill", target=spawn.spawn_id, name=spawn.name, where=(spawn.x, spawn.y, spawn.z), item_id=step.item_id)
            return Intention("explore", name=step.npc or step.zone)
        if step.kind == "forage":
            return Intention("forage", item_id=step.item_id, name=step.zone)
        if step.kind == "fish":
            return Intention("fish", item_id=step.item_id, name=step.zone)
        if step.kind == "pick_lock":
            door_id = int(step.text or 0) if str(step.text or "").isdigit() else 0
            return Intention("pick_lock", target=door_id, item_id=step.item_id, name=step.zone)
        if step.kind == "skill":
            from eqclient.plan import _skill_intention

            return _skill_intention(step, self.recipes)
        if step.kind == "faction":
            # Raise via densest +faction zone — never kill the gated quest NPC.
            from eqclient.plan import _faction_intention

            return _faction_intention(self.model, step, self.factions)
        if step.kind in {"encounter", "boss", "chest", "instance", "key"}:
            if step.text and "lockout" in step.text.lower():
                self.journal.set_flag(self.model.character, f"lockout:{step.zone or step.npc}", 1)
            spawn = self._spawn_named(step.npc) if step.npc else None
            if spawn is not None:
                kind = "loot" if step.kind == "chest" else "task_kill"
                return Intention(kind, target=spawn.spawn_id, name=spawn.name, where=(spawn.x, spawn.y, spawn.z), item_id=step.item_id)
            return Intention("explore", name=step.npc or step.zone, text=step.kind)
        if step.kind == "level":
            from eqclient.plan import _grind_corpse, _xp_foe, grind_why

            why = grind_why(step.text, item_id=step.item_id, kind="level")
            self._note_grind_goal(why, step.item_id)
            camp = camp_for_level(self.model.level or 1, self.model.zone or "")
            if camp and (self.model.zone or "").lower() != camp.zone:
                return self._travel_intention(camp.zone, text=why, item_id=step.item_id) or Intention(
                    "explore", name=camp.zone, text=why, item_id=step.item_id
                )
            corpse = self._lootable_corpse() or _grind_corpse(self.model, self.skipped_corpses)
            if corpse is not None:
                return Intention(
                    "loot",
                    target=corpse.spawn_id,
                    name=corpse.name,
                    where=(corpse.x, corpse.y, corpse.z),
                    text=why,
                    item_id=step.item_id,
                )
            foe = _xp_foe(
                self.model,
                skip=self._gave_up_skip() | self._protected_spawn_ids(),
                can_see=self._in_sight,
            )
            if foe is not None:
                return Intention(
                    "fight",
                    target=foe.spawn_id,
                    name=foe.name,
                    where=(foe.x, foe.y, foe.z),
                    text=why,
                    item_id=step.item_id,
                )
            return Intention("grind", name=camp.zone if camp else "xp", text=why, item_id=step.item_id)
        if step.kind == "blocked":
            return Intention("explore", name=step.zone or step.npc or "blocked", text=step.text)
        return None

    def _cached_seller(self, item_id: int = 0):
        """Preferred merchant-book seller for this zone (item stock first, else any local)."""
        book = getattr(self, "merchants", None)
        if book is None or not book.by_npc:
            return None
        zone = self.model.zone or ""
        if item_id:
            found = book.best(item_id, zone)
            if found is not None:
                seller, _cost = found
                return seller
        local = book.in_zone(zone)
        return local[0] if local else None

    def _nearest_merchant(self, item_id: int = 0):
        """Closest live spawn that is a known seller (cache names), else keyword vendor."""
        book = getattr(self, "merchants", None)
        zone = self.model.zone or ""
        known = book.names_in(zone) if book is not None and book.by_npc else set()
        want = ""
        if item_id and book is not None:
            found = book.best(item_id, zone)
            if found is not None:
                want = _merchant_norm(found[0].name)
        best = None
        best_dist = 1e9
        best_rank = 3
        here = self.model.position
        for spawn in self.model.spawns.values():
            if spawn.npc != 1:
                continue
            folded = _merchant_norm(spawn.name)
            name = (spawn.name or "").lower()
            if want and folded == want:
                rank = 0
            elif folded in known or (book is not None and book.is_merchant_name(spawn.name, zone)):
                rank = 1
            elif any(word in name for word in _MERCHANT_WORDS):
                rank = 2
            else:
                continue
            dist = _horiz(here, (spawn.x, spawn.y, spawn.z))
            if rank < best_rank or (rank == best_rank and dist < best_dist):
                best = spawn
                best_dist = dist
                best_rank = rank
        return best

    def _spawn_by_substring(self, needle: str):
        needle = needle.lower()
        for spawn in self.model.spawns.values():
            if spawn.npc == 1 and needle in (spawn.name or "").lower():
                return spawn
        return None

    def _note_consider(self, payload: bytes) -> None:
        """Journal primary (1–9) standing after a consider reply."""
        if len(payload) < 12:
            return
        target = struct.unpack_from("<I", payload, 4)[0]
        spawn = self.model.spawns.get(target)
        if spawn is None or spawn.npc != 1:
            return
        self._journal_primary_standing(spawn)

    def _journal_primary_standing(self, spawn) -> None:
        from eqclient.campaign import _standing_key

        standing = self.model.faction.get(spawn.spawn_id)
        if standing is None:
            return
        zone = (self.model.zone or "").lower()
        key = _standing_key("primary", zone, spawn.name or "")
        self.journal.set_flag(self.model.character, key, int(standing))
        print(f"faction {key}={standing}", flush=True)

    def _note_faction_chat(self, message: str) -> None:
        """Bump journaled numeric faction from server standing lines."""
        import re

        from eqclient.campaign import _parse_faction_spec

        lowered = message.lower()
        adjusted = re.search(
            r"faction standing with (.+?) has been adjusted by ([+-]?\d+)",
            lowered,
        )
        better = "got better" in lowered or "could not possibly get any better" in lowered
        worse = "got worse" in lowered or "could not possibly get any worse" in lowered
        name = ""
        delta = 0
        if adjusted:
            name = adjusted.group(1).strip()
            delta = int(adjusted.group(2))
        elif better or worse:
            m = re.search(r"faction standing with (.+?) (?:got |could not)", lowered)
            name = m.group(1).strip() if m else ""
            if "could not possibly" in lowered:
                delta = 0
            else:
                delta = 1 if better else -1
        if not name or delta == 0:
            return
        fac_id = _faction_id_named(name)
        if fac_id is None:
            tip = getattr(self, "_faction_focus", "") or ""
            if tip.startswith("faction-check:"):
                tip = tip.split(":", 1)[1]
            if tip:
                fid, _at = _parse_faction_spec(tip if tip.startswith("faction:") else f"faction:{tip}")
                if fid.isdigit():
                    fac_id = int(fid)
        if fac_id is None:
            return
        key = f"faction:{fac_id}"
        current = int(self.journal.flag_values(self.model.character).get(key) or 0)
        self.journal.set_flag(self.model.character, key, current + delta)
        print(f"faction {key}={current + delta} ({name})", flush=True)

    def _party_messages(self) -> None:
        clr = self._cleric_bot_name().lower()
        for message in self.client.messages[self._messages :]:
            self.party.push(message)
            lowered = message.lower()
            # ^botreport: "Cleric Mocclr reports: 100.0% health: 45.2% mana"
            if "reports:" in lowered and "% health" in lowered:
                m_hp = re.search(r"reports:\s*([\d.]+)\s*%\s*health", lowered)
                if m_hp:
                    pct = int(float(m_hp.group(1)))
                    # Match roster stem in the line → live spawn id for _party_hp.
                    for name, _cid in self.party.roster:
                        if name.lower() in lowered:
                            spawn = self._bot_spawn_named(name) or self._spawn_named(name)
                            if spawn is not None:
                                self._note_party_health(spawn.spawn_id & 0xFFFF, pct)
                            break
                if "% mana" in lowered and (not clr or clr in lowered):
                    m_mana = re.search(r"([\d.]+)\s*%\s*mana", lowered)
                    if m_mana:
                        self._cleric_mana = max(0.0, min(1.0, float(m_mana.group(1)) / 100.0))
            # Faction chat does not name the victim. Only retire a mob we are actually
            # fighting — never _focus/_pursuit (grind walk targets), or a bot orc kill
            # gets logged as "kill <far beetle>" and the real Death Fist hits look orphaned.
            if "faction standing" in lowered:
                victim = self._swing_id
                if victim and victim in self.attacked:
                    self._retire(victim)
                self._note_faction_chat(message)
            if "ability recovery time not yet met" in lowered and self._ability_last:
                # Server rejected us — push that ability out another couple seconds.
                self._ability_ready[self._ability_last] = max(
                    self._ability_ready.get(self._ability_last, 0.0),
                    time.monotonic() + 2.0,
                )
            # Lockouts / instance timers are server chat only — never a DB read.
            if "lockout" in lowered or "you cannot enter" in lowered or "you must wait" in lowered:
                label = "".join(ch if ch.isalnum() or ch in "_-" else "_" for ch in lowered)[:48]
                self.journal.set_flag(self.model.character, f"lockout:{label}", 1)
            if "bind to the area" in lowered:
                self._note_soulbind()
            # Flag value updates after a successful hand-in when chat echoes the set.
            if "your flag" in lowered or "quest flag" in lowered:
                pass
        self._messages = len(self.client.messages)

    def _confirm_zone(self, payload: bytes) -> None:
        """Answer OP_RequestClientZoneChange; success arrives as OP_ZoneChange."""
        if len(payload) < 16:
            return
        zone_id, instance_id = struct.unpack_from("<HH", payload)
        y, x, z = struct.unpack_from("<fff", payload, 4)
        if not zone_id or zone_id == 189:
            return
        name = (self.model.character or "Mockone").encode("latin1")[:63]
        packet = bytearray(88)
        packet[: len(name)] = name
        struct.pack_into("<HH", packet, 64, zone_id, instance_id)
        struct.pack_into("<fff", packet, 68, y, x, z)
        print(f"OP_ZoneChange confirm dest={zone_id} from=({x:.0f},{y:.0f},{z:.0f})", flush=True)
        self.client.send("OP_ZoneChange", bytes(packet))

    def _restore_battle(self) -> None:
        """The finished battle is not resent. The journal is what keeps him on the exit."""
        zone = self.model.zone or ""
        if not self.journal.has(self.model.character, zone, "guard hobart", "task", "5102"):
            return
        rows = [
            activity
            for activity in self.tasks.activities
            if activity.task_id == 5102 and not activity.optional
        ]
        if rows and not all(activity.finished for activity in rows):
            return
        self.tasks.completed.add(5102)
        self.journal.mark_tutorial_done(self.model.character)
        self._tutorial_done = True

    def _remember(self, npc: str, kind: str, detail: str) -> None:
        npc_key = _key(npc)
        self.journal.record(self.model.character, self.model.zone or "", npc_key, kind, detail)
        if kind == "say":
            self.said.add((npc_key, detail))
        elif kind == "handin":
            self.handed.add((npc_key, detail))

    def _shortfalls(self) -> dict[int, int]:
        """How many more of each item a hand-in, a task, or the obtain stack still needs."""
        short: dict[int, int] = {}

        def bump(item_id: int, gap: int) -> None:
            if item_id > 0 and gap > 0:
                short[item_id] = max(short.get(item_id, 0), gap)

        for script in self.quests.scripts.values():
            for need in script.needs:
                bump(need.item_id, need.count - self.inventory.count(need.item_id))
        for need in _task_needs(self.tasks, self.quests, self.inventory):
            bump(need.item_id, need.count - self.inventory.count(need.item_id))
        campaign = getattr(self, "campaign", None)
        if campaign is not None:
            held = self._held_counts()
            for item_id in campaign.stack:
                if item_id <= 0:
                    continue
                bump(item_id, campaign.counts.get(item_id, 1) - held.get(item_id, 0))
        return short

    def _wanted_ids(self) -> set[int]:
        """Item ids still short: this zone's hand-ins, the open task, and the obtain stack."""
        return set(self._shortfalls())

    def _note_progress(self, before: dict[tuple[int, int], int]) -> None:
        for activity in self.tasks.activities:
            key = (activity.task_id, activity.activity_id)
            if activity.done > before.get(key, 0):
                if activity.kind == KILL:
                    self._progress_at = time.monotonic()
                    if self._focus:
                        self._mark_gave_up(self._focus, 20.0)
                    self._focus = 0
                    self._swing_id = 0
                if activity.done >= activity.goal:
                    self.score.activities += 1
                    if activity.task_id == 5102 and self.tasks.task_finished(5102):
                        self.journal.mark_tutorial_done(self.model.character)
                        self._tutorial_done = True
                print(
                    f"task {activity.task_id} {activity.target_name} {activity.done}/{activity.goal}",
                    flush=True,
                )


def _kill_still_wanted(tasks: TaskBook, name: str) -> bool:
    """Stay on this mob only while a kill step still names it."""
    return any(
        activity.kind == KILL
        and not activity.finished
        and not activity.optional
        and _names_match(name, activity.target_name)
        for activity in tasks.activities
    )


def _done_map(tasks: TaskBook) -> dict[tuple[int, int], int]:
    return {(activity.task_id, activity.activity_id): activity.done for activity in tasks.activities}


def _move(here, goal, step: float) -> tuple[float, float, float]:
    dx, dy = goal[0] - here[0], goal[1] - here[1]
    dist = _horiz(here, goal)
    if dist <= step:
        return goal
    scale = step / dist
    return (here[0] + dx * scale, here[1] + dy * scale, goal[2])


def _horiz(a, b) -> float:
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5


def _on_spot(here, goal, reach: float) -> bool:
    """Close in the horizontal, and on the same floor. Above the roof does not count."""
    return _horiz(here, goal) <= reach and abs(here[2] - goal[2]) <= 6.0


def _behind(here, point, goal) -> bool:
    """A path point in the opposite half from the goal. Walking there is a step back."""
    vx, vy = point[0] - here[0], point[1] - here[1]
    gx, gy = goal[0] - here[0], goal[1] - here[1]
    if gx * gx + gy * gy < 1.0:
        return False
    return vx * gx + vy * gy < 0.0


def _key(name: str) -> str:
    return " ".join(name.lower().replace("_", " ").replace("#", " ").split())


def _item_tip(item_id: int, item_stats=None) -> str:
    """Log tip: `item=Leather Gloves (2010)` when the name is known."""
    if not item_id:
        return ""
    name = ""
    if item_stats is not None:
        row = item_stats.get(int(item_id))
        if row is not None and getattr(row, "name", ""):
            name = str(row.name).strip()
    if name:
        return f"item={name} ({item_id})"
    return f"item={item_id}"


def _intention_label(intention: Intention, item_stats=None) -> str:
    """Compact intention for logs: kind, name/target, why (text), goal where."""
    parts = [intention.kind]
    if intention.name:
        parts.append(intention.name)
    elif intention.target:
        parts.append(str(intention.target))
    if intention.item_id:
        parts.append(_item_tip(intention.item_id, item_stats))
    if intention.text:
        text = intention.text
        # Expand bare item=N in why= (e.g. grind for item=2010).
        text = re.sub(
            r"\bitem=(\d+)\b",
            lambda m: _item_tip(int(m.group(1)), item_stats),
            text,
        )
        parts.append(f"why={text}")
    if intention.where is not None:
        wx, wy, wz = intention.where
        parts.append(f"goto=({wx:.0f},{wy:.0f},{wz:.0f})")
    return " ".join(parts)


_FACTION_NAMES: dict[str, int] | None = None


def _faction_id_named(name: str) -> int | None:
    """Resolve a standing-chat faction name to an id (lazy faction_list.jsonl)."""
    global _FACTION_NAMES
    key = " ".join((name or "").lower().split())
    if not key:
        return None
    if _FACTION_NAMES is None:
        path = os.environ.get("EQEMU_FACTION_LIST", DEFAULT_FACTION_LIST)
        _FACTION_NAMES = read_faction_list(path)
    return _FACTION_NAMES.get(key)


_WATCHED = (
    "OP_NewZone",
    "OP_ZoneSpawns",
    "OP_NewSpawn",
    "OP_DeleteSpawn",
    "OP_SpawnDoor",
    "OP_GroundSpawn",
    "OP_ClickObject",
    "OP_ClientUpdate",
    "OP_RequestClientZoneChange",
    "OP_ZoneChange",
    "OP_BecomeCorpse",
    "OP_Death",
    "OP_PlayerProfile",
    "OP_MemorizeSpell",
    "OP_LevelUpdate",
    "OP_ExpUpdate",
    "OP_GroupInvite",
    "OP_GroupInvite2",
    "OP_GroupUpdate",
    "OP_RaidUpdate",
    "OP_RaidJoin",
    "OP_SkillUpdate",
    "OP_MoneyOnCorpse",
    "OP_MoneyUpdate",
    "OP_Consider",
    "OP_SimpleMessage",
    "OP_Damage",
    "OP_HPUpdate",
    "OP_MobHealth",
    "OP_Buff",
    "OP_RezzRequest",
    "OP_Assist",
    "OP_MoveDoor",
    "OP_ItemPacket",
    "OP_DeleteItem",
    "OP_CharInventory",
    "OP_TaskSelectWindow",
    "OP_TaskActivity",
    "OP_TaskActivityComplete",
    "OP_OnLevelMessage",
    "OP_FindPersonReply",
    "OP_Stamina",
    "OP_TradeRequest",
    "OP_ChannelMessage",
)


def main() -> None:
    run_spec(AgentSpec.from_environ())


def run_spec(spec: AgentSpec) -> Score:
    """Log one character in with its own race, class, and quest journal."""
    started = time.monotonic()
    limit = float(os.environ.get("EQEMU_AGENT_SECONDS", "180"))
    last: Score | None = None
    while time.monotonic() - started < limit:
        holder: dict[str, Agent] = {}

        def before(client: Client) -> None:
            agent = Agent(
                client,
                form_raid=spec.form_raid,
                form_group=spec.form_group,
                goal_item=spec.goal_item,
            )
            agent.attach()
            holder["agent"] = agent

        client: Client | None = None
        try:
            client = connect(
                user=spec.user,
                password=spec.password,
                character=spec.character,
                before_zone=before,
                sheet=spec.sheet(),
                bot_prefix=spec.bot_prefix,
                journal_path=spec.journal_path,
            )
            last = holder["agent"].run(seconds=max(1.0, limit - (time.monotonic() - started)))
            return last
        except SessionError as exc:
            print(f"session dropped: {exc}", flush=True)
            time.sleep(2.0)
        finally:
            if client is not None:
                client.close()
    if last is None:
        raise SessionError("session dropped before the agent could start")
    return last
