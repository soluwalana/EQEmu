"""The sheet the server is showing us. Handlers write it. Actions read it.

The player stats, inventory, and tutorial and quest started flags live on character.
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient4.action import Action
    from eqclient4.loop import Loop
    from eqclient4.nav.water import WaterMap

import math
import time
import random
import os
import json
from pathlib import Path as FSPath
from collections import defaultdict
from dataclasses import dataclass
from typing import Literal

from eqclient4.bots import Bot
from eqclient4.structs.constants import (
    CREATE_COMBINATIONS_RACE_TO_BITMASK,
    RACE_ID_TO_BIT,
    GOOD_ALIGNED_RACES,
    CLASS_ID_TO_CODE,
    CLASS_NAME_TO_ID,
    TANK_CLASSES,
    HEALER_CLASSES,
    DPS_CLASSES,
)
from eqclient4.character import Character
from eqclient4.data.bot_spells import BotSpellBook, ensure_bot_spells
from eqclient4.data.drops import DropBook, MappedDrops, ensure_drops
from eqclient4.data.factions import FactionBook, ensure_factions
from eqclient4.data.ground import GroundSpawnBook, LiveGroundSpawn, ensure_ground_spawns
from eqclient4.data.items import ItemBook, ensure_items
from eqclient4.data.locations import LocationBook, MappedLocations, ensure_locations
from eqclient4.data.merchants import MerchantBook, ensure_merchants
from eqclient4.data.npcs import NPC, ensure_npcs
from eqclient4.data.recipes import RecipeBook, ensure_recipes
from eqclient4.data.spells import SpellBook, ensure_spells
from eqclient4.inventory import CharacterInventory, Merchant
from eqclient4.log import log
from eqclient4.nav.maps import ZoneMap, load_map
from eqclient4.nav.navmesh import NavMesh, load_nav
from eqclient4.nav.path import (
    NEARBY_YARDS,
    STRIDE,
    Path,
    along,
    cut_to_step,
    doors_on_stride,
)
from eqclient4.nav.path import find as path_find
from eqclient4.nav.path import is_nearby, iter_doors, mob_point, route
from eqclient4.nav.path import track as path_track
from eqclient4.nav.path import trim_points
from eqclient4.nav.travel import ZoneGraph, ensure_zone_graph
from eqclient4.nav.water import WaterMap, load_water
from eqclient4.quests.graph import QuestGraph, ensure_graph
from eqclient4.structs import (
    EQStruct,
    OP_ClickDoor,
    OP_ClientUpdate,
    OP_Consider,
    OP_FindPersonReply,
    OP_FloatListThing,
    OP_MobUpdate,
    OP_MoveDoor,
    OP_NewZone,
    OP_TaskActivity,
    OP_TaskDescription,
)
from eqclient4.utils import eq_heading

RosterMode = Literal["party", "raid"]


class Faction:
    """One faction. amount stays None until a server message confirms it.

    maxed is 1 when the faction cannot get better, -1 when it cannot get worse,
    and 0 otherwise. changed is set when better or worse arrives with no number.
    """

    def __init__(self, amount: int | None = None, maxed: int = 0, changed: bool = False) -> None:
        self.amount = amount
        self.maxed = maxed
        self.changed = changed


@dataclass
class Door:
    id: int
    name: str
    x: float
    y: float
    z: float
    open_type: int = 0
    opened: bool = False


@dataclass
class Consider:
    standing: int = 0
    level_color: int = 0
    name: str = ""



class Roster:

    def __init__(self, item_book: ItemBook, character: str) -> None:
        self.item_book = item_book
        self.character = character
        self.group_size = 5
        self.raid_size = 30
        self.raid: list[Bot] = []
        self.group: list[Bot] = []

    def serialize(self) -> dict:
        return {
            "raid": {
                b.name: {
                    "owner": b.owner,
                    "name": b.name,
                    "race": b.race,
                    "class_id": b.class_id,
                    "gender": b.gender,
                    "created": b.created,
                }
                for b in self.raid
            },
            "group": {
                b.name: {
                    "owner": b.owner,
                    "name": b.name,
                    "race": b.race,
                    "class_id": b.class_id,
                    "gender": b.gender,
                    "created": b.created,
                }
                for b in self.group
            },
        }


def race_for_class(class_id: int) -> int:
    acceptable_combos = CREATE_COMBINATIONS_RACE_TO_BITMASK[class_id]
    acceptable_races = []
    for race, bitmask in RACE_ID_TO_BIT.items():
        if bitmask & acceptable_combos and race in GOOD_ALIGNED_RACES:
            acceptable_races.append(race)
    return random.choice(acceptable_races)


_ROSTER: Roster | None = None


def get_roster(item_book: ItemBook, character: str) -> Roster:
    global _ROSTER
    if _ROSTER:
        return _ROSTER

    cache_path = FSPath.home() / ".eqclient" / "v4" / character / "raid_roster.json"
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    if os.path.exists(cache_path):
        data = json.load(open(cache_path))
        _ROSTER = Roster(item_book, character)
        _ROSTER.raid = [Bot(item_book, **b) for b in data["raid"].values()]
        _ROSTER.group = [Bot(item_book, **b) for b in data["group"].values()]
        return _ROSTER

    class_tracker = defaultdict(int)

    def generate_bot(class_id: int) -> Bot:
        class_tracker[class_id] += 1
        suffix = ""
        if class_tracker[class_id] > 1:
            suffix = str(chr(ord("a") + class_tracker[class_id] - 2))
            if suffix in "aeiou":
                suffix = f"x{suffix}"

        short = CLASS_ID_TO_CODE[class_id]
        if short == "ENCH":  # no duplicate vowels allowed
            short = f"x{short}"

        name = f"{character[3]}" + f"{short}{suffix}".lower()

        return Bot(
            item_book,
            owner=character,
            name=name,
            race=race_for_class(class_id),
            class_id=class_id,
            gender=1,
        )

    _ROSTER = Roster(item_book, character)
    _ROSTER.group.append(generate_bot(CLASS_NAME_TO_ID["Cleric"]))
    _ROSTER.group.append(generate_bot(random.choice(list(TANK_CLASSES))))
    _ROSTER.group.append(generate_bot(random.choice(list(HEALER_CLASSES))))
    _ROSTER.group.append(generate_bot(random.choice(list(DPS_CLASSES))))
    _ROSTER.group.append(generate_bot(random.choice(list(DPS_CLASSES))))

    for _ in range(30):
        tank = random.choice(list(TANK_CLASSES))
        _ROSTER.raid.append(generate_bot(tank))
        healer = random.choice(list(HEALER_CLASSES))
        _ROSTER.raid.append(generate_bot(healer))
        other = random.choice(list(CLASS_ID_TO_CODE.keys()))
        _ROSTER.raid.append(generate_bot(other))

    open(cache_path, "w").write(json.dumps(_ROSTER.serialize(), indent=2))
    return _ROSTER


class Mob:
    """One spawn. distance and direction are refreshed from our position."""

    def __init__(
        self,
        id: int,
        name: str = "",
        npc: int = 0,
        level: int = 0,
        position: tuple[float, float, float] = (0.0, 0.0, 0.0),
        hp: int = 0,
        last_name: str = "",
    ) -> None:
        self.id = id
        self.name = name
        self.last_name = last_name or ""
        self.npc = npc
        self.level = level
        self.body = 0
        self.class_id = 0
        self.race = 0
        self.hp: int = hp
        self.max_hp: int = 0
        self.mana: int | None = None
        self.max_mana: int | None = None
        self.consider: Consider | None = None
        self.faction_id = 0
        self.faction_last_considered: int | None = None
        self.targeted = False
        self.dead = False
        self._consider_sent = False
        self._consider_change_sent = False
        self.distance = 0.0
        self.direction = 0
        self._position = (0.0, 0.0, 0.0)
        self.position = position

    def spoken_name(self) -> str:
        """The name you hail. A trailing 000 is the unique suffix, and the last name is his title."""
        kept = []
        for ch in (self.name or "").replace("_", " "):
            if ch.isalpha() or ch in " '-`":
                kept.append(ch)
            else:
                kept.append(" ")
        return " ".join("".join(kept).split())

    @property
    def spawn_id(self) -> int:
        return self.id

    @property
    def position(self) -> tuple[float, float, float]:
        return self._position

    @position.setter
    def position(self, point: tuple[float, float, float]) -> None:
        self._position = (float(point[0]), float(point[1]), float(point[2]))

    @property
    def is_treasure(self) -> bool:
        """An LDoN object. Melee does not credit it. Opening it does."""
        if int(self.class_id or 0) == 62:
            return True
        return False


class MobMap(dict[int, Mob]):
    """mobs[id] = Mob. Assigning a mob attaches it and measures distance."""

    def __init__(self, world: World) -> None:
        super().__init__()
        self._world = world

    def __setitem__(self, key: int, mob: Mob) -> None:
        super().__setitem__(key, mob)
        self._world.measure(mob)

    def mob_named(self, name: str) -> Mob | None:
        want = " ".join((name or "").replace("_", " ").lower().split())
        if not want:
            return None
        exact = None
        partial = None
        for mob in self.values():
            found = mob.spoken_name().lower()
            if found == want:
                exact = mob
                break
            if want in found and not partial:
                partial = mob
        return exact or partial

    def find_mob(self, spawn_id: int) -> Mob | None:
        for mob_id, mob in self.items():
            if mob_id == spawn_id or mob.id == spawn_id:
                return mob
            short = spawn_id & 65535
            if short == (mob_id & 65535) or short == (mob.id & 65535):
                return mob
        return None


class TaskBook:
    def __init__(self) -> None:
        self.tasks: dict[int, OP_TaskDescription] = {}
        self.activities: dict[int, dict[int, OP_TaskActivity]] = defaultdict(defaultdict)

    def sequenced_tasks(self) -> list[OP_TaskDescription]:
        return sorted(self.tasks.values(), key=lambda x: x.sequence)

    def pending_activities(self) -> list[OP_TaskActivity]:
        activities: list[OP_TaskActivity] = []
        for task in self.tasks.values():
            for activity in self.activities[task.task_id].values():
                if activity.done < activity.goal:
                    activities.append(activity)
        return activities


class World:

    def __init__(self, name: str) -> None:

        self.self_id = 0

        # <Character Management>
        self.character = Character(name)
        # Total faction standing isn't knowable,
        # just what can be gleaned from considerations
        self.discovered_factions: dict[int, Faction] = {}

        # Inventory
        self.inventory: CharacterInventory = CharacterInventory()
        # </Character Management>

        # <Caches>
        self.tasks: TaskBook = TaskBook()
        self.item_book: ItemBook = ensure_items()
        self.quest_graph: QuestGraph = ensure_graph()
        self.zone_graph: ZoneGraph = ensure_zone_graph()
        self.merchants: MerchantBook = ensure_merchants()
        self.ground_book: GroundSpawnBook = ensure_ground_spawns()
        self.faction_hits: FactionBook = ensure_factions()
        self.recipes: RecipeBook = ensure_recipes()
        self.item_locations: LocationBook | MappedLocations = ensure_locations()
        self.spells: SpellBook = ensure_spells()
        self.bot_spells: BotSpellBook = ensure_bot_spells()
        self.npcs: NPCCache = NPCCache(self.quest_graph)
        self.drops: MappedDrops | DropBook = ensure_drops()
        # </Caches>

        # Group Rosters and Bots
        self.bot_roster = get_roster(self.item_book, self.character.name)

        # <Volatile Data>
        # Volatile Data should be cleared on Zone Change

        #   Current Zone
        self.zone: str | None = None
        self.zone_id = -1
        self.zone_formed: str | None = None

        #   Active mesh
        self.mesh: ZoneMap | None = None

        #   Zone in point, considered safe normally
        self.safe: tuple[float, float, float] | None = None
        self.exit_doors: dict[str, dict[int, list[int]]] = {}
        self.at_water = False

        #   Water Maps loaded from zoning in this session
        self.water_maps: dict[str, WaterMap] = {}

        # Live Ground Spawns in this Zone
        self.ground_spawns: dict[int, list[LiveGroundSpawn]] = {}

        # Mobs in the zone
        self.mobs = MobMap(self)
        # tracking pending mobs that have attacked us
        self.aggro_mobs: dict[int, Mob] = {}

        # Live Doors in this zone
        self.doors: dict[int, Door] = {}
        # Merchants
        self.active_merchants: dict[int, Merchant] = {}

        #   Current Position during Gameplay
        self._x = float(0)
        self._y = float(0)
        self._z = float(0)

        # Movement and Position
        self.movement = Movement(self)

        # </Volatile Data>

    def active_merchant(self) -> Merchant | None:
        for merchant in self.active_merchants.values():
            if merchant.is_open:
                return merchant
        return None

    @property
    def self_id(self) -> int:
        return self.character.self_id

    @self_id.setter
    def self_id(self, value: int) -> None:
        self.character.self_id = int(value or 0)

    @property
    def position(self) -> tuple[float, float, float]:
        return (self._x, self._y, self._z)

    @position.setter
    def position(self, point: tuple[float, float, float]) -> None:
        self._x, self._y, self._z = (float(point[0]), float(point[1]), float(point[2]))
        for mob in self.mobs.values():
            self.measure(mob)

    def note_fight(self, spawn_id: int, mob: Mob) -> None:
        """This spawn attacked us, or we attacked it. Loot uses the set."""
        if spawn_id:
            self.aggro_mobs[spawn_id] = mob

    def measure(self, mob: Mob) -> None:
        """Refresh distance (3D yards) and direction (0-512 heading from us to the mob)."""
        origin = self.position
        point = mob.position
        dx = point[0] - origin[0]
        dy = point[1] - origin[1]
        dz = point[2] - origin[2]
        mob.distance = math.sqrt(dx * dx + dy * dy + dz * dz)
        mob.direction = eq_heading(origin[0], origin[1], point[0], point[1])

    def nearby(self, yards: float) -> list[Mob]:
        """Mobs within yards, nearest first."""
        found = [mob for mob in self.mobs.values() if mob.distance <= yards]
        found.sort(key=lambda mob: (mob.distance, mob.id))
        return found

    def line_of_sight(self, mob: Mob) -> bool:
        """True when the mesh can see mob from our position.

        world.mesh.clear(start, end) is used when a mesh is set. With no mesh,
        nav.maps.load_map(zone) is used when that module exists. A missing mesh
        means the shot is clear.
        """
        start = self.position
        end = mob.position
        mesh = self.mesh
        if not mesh:
            mesh = load_map(self.zone or "")

        if not mesh:
            return True

        return mesh.clear(start, end)

    def consider_mobs(self) -> list[Mob]:
        return [mob for mob in self.nearby(NEARBY_YARDS) if not mob.id != self.self_id]

    def needs_consider(self, mob: Mob) -> bool:
        faction = self.faction(mob.faction_id)
        amount = faction.amount
        maxed = faction.maxed
        changed = faction.changed
        sent = mob._consider_sent or mob.faction_last_considered is not None
        if not sent:
            return True

        if maxed:
            return False

        if changed and not mob._consider_change_sent:
            return True

        return amount != mob.faction_last_considered

    def remember_consider(self, mob: Mob) -> None:
        faction = self.faction(mob.faction_id)
        amount = faction.amount
        changed = faction.changed
        mob.faction_last_considered = amount
        mob._consider_sent = True
        mob._consider_change_sent = changed

    def faction(self, faction_id: int) -> Faction:
        found = self.discovered_factions.get(faction_id)
        if not found:
            found = Faction()
            self.discovered_factions[faction_id] = found
        return found

    def get_water_map(self, zone: str) -> WaterMap | None:
        """World-supplied map, else the zone file. A missing file is no water."""
        if zone in self.water_maps:
            return self.water_maps[zone]

        if not zone:
            return None

        water = load_water(zone)
        if not water:
            return None
        self.water_maps[zone] = water
        return water


class NPCCache:
    def __init__(self, quest_graph: QuestGraph) -> None:
        self.npc_cache: dict[int, NPC] = ensure_npcs()
        for zone, npc_ids in quest_graph.spawned_npcs().items():
            for npc_id in npc_ids:
                if npc_id not in self.npc_cache:
                    log.warning(f"NPC {npc_id} not found in NPC cache - zone {zone}")
                    continue

                self.npc_cache[npc_id].zones.append(zone)

    def get_npc(self, npc_id: int) -> NPC | None:
        return self.npc_cache.get(npc_id)


STRIDE_TIMEOUT = 3
STRIDE_MOB_RADIUS = 2.0
_COMMIT_TOLERANCE = 0.35


@dataclass
class MovementAnnotatedMob:
    """A mob already on the current stride. Values are copied off the Mob."""

    mob: Mob
    distance: float | None = None
    direction: float | None = None
    consider: Consider | None = None
    targeted: bool = False


class Movement:
    """Position, the stride in flight, and the packets that move us."""

    def __init__(self, world: World) -> None:
        self.world = world
        self.position: tuple = (0.0, 0.0, 0.0)
        self.heading: int = 0
        self.asked: tuple | None = None
        self.asked_tick: int = 0
        self.anim: int = 0
        self.committed: bool = True
        self.refused: bool = False
        self.sequence: int = 0
        self.caller_mode: str = "run"
        self.advanced: bool = False
        self.path: Path | None = None
        self.clicked: set = set()
        self.open_ids: set = set()
        self.find_mob: Mob | None = None
        self._nav: NavMesh | None = None
        self._nav_zone: str | None = None
        self._routes: dict[tuple[str, str], Path] = {}

    @property
    def stride_committed(self) -> bool:
        return self.committed

    def opcodes(self) -> tuple[str, ...]:
        """Opcodes the bus should deliver to handle()."""
        return (
            "OP_ClientUpdate",
            "OP_MobUpdate",
            "OP_NewZone",
            "OP_MoveDoor",
            "OP_FindPersonReply",
        )

    def reset(self, origin: tuple[float, float, float] = (0.0, 0.0, 0.0)) -> None:
        """Clear stride state. A new session calls this. OP_NewZone clears a zone entry."""
        point = (float(origin[0]), float(origin[1]), float(origin[2]))
        self.position = point
        self.heading = 0
        self.asked = None
        self.asked_tick = 0
        self.anim = 0
        self.committed = True
        self.refused = False
        self.sequence = 0
        self.caller_mode = "run"
        self.advanced = False
        self.path = None
        self._routes = {}
        self.clicked = set()
        self.open_ids = set()
        self.find_mob = None

    def snap(self, point: tuple[float, float, float]) -> None:
        """The server moved us inside this zone. Drop the stride and take the point."""
        self.asked = None
        self.asked_tick = 0
        self.anim = 0
        self.committed = True
        self.refused = False
        self.path = None
        self._routes = {}
        self.position = (float(point[0]), float(point[1]), float(point[2]))
        self.write_world(point)

    def write_world(self, point: tuple[float, float, float]) -> None:
        self.world.position = (float(point[0]), float(point[1]), float(point[2]))

    def handle(self, opcode: str, payload: EQStruct) -> None:
        """Bus entry. Our position, a zone entry, an opened door, or find waypoints."""

        match payload:
            case OP_ClientUpdate() | OP_MobUpdate():
                self._on_position(payload)
            case OP_NewZone():
                self._on_new_zone(payload)
            case OP_MoveDoor():
                self._on_move_door(payload)
            case OP_FindPersonReply():
                self._on_find_reply(payload)
            case _:
                log.error(f"Unknown movement opcode: {opcode}")

    def plan(
        self,
        destination: tuple[float, float, float] | Mob,
        mode: str,
    ) -> Path:
        """Return a Path. Does not send OP_Consider and does not write a position.

        ``loop`` is accepted and ignored so a distance read cannot send.
        ``mode`` is run, los, walk, creep, hold, or swim. Swim keeps the stride
        of the last mode (run, until one was planned) and changes only z.
        """
        mode = mode or "run"
        if mode not in STRIDE and mode != "swim":
            mode = "run"

        base = self.caller_mode if mode == "swim" else mode
        if base not in STRIDE:
            base = "run"

        length, anim = STRIDE[base]
        if mode != "swim":
            self.caller_mode = mode

        origin = self.position

        zone = self.world.zone or ""
        water = self.world.get_water_map(zone)
        if mode != "swim":
            reused = self._reused_route(origin, destination, mode, length, anim, zone)
            if reused is not None:
                return reused
        built = route(
            origin,
            destination,
            zone=zone,
            doors=self.world.doors,
            water=water,
            length=length,
            mode=mode,
        )
        built.stride_length = length
        built.anim = anim
        built.mode = mode

        if mode == "swim":
            target_z = _surface_z(origin, built.destination, water)
            built.z_only = True
            built.swim_z = target_z
            built.next_point = _z_step(origin, target_z, length)
            built.in_water = (
                built.in_water
                or _liquid(water, built.next_point)
                or _liquid(water, built.destination)
            )

        kept = self._keep_find_path(built)
        chosen = built if kept is None else kept
        if kept is None:
            self.path = built

        self.remember_route(zone, destination, chosen)
        return chosen

    def face(self, loop: Loop, point: tuple[float, float, float]) -> None:
        """Turn toward a point and tell the server. Melee misses when the heading is wrong."""
        here = self.position
        want = eq_heading(here[0], here[1], point[0], point[1])
        gap = abs(int(self.heading) - want) % 512
        if min(gap, 512 - gap) < 24:
            return
        self.heading = want
        self._emit(loop, here, 0, "face")

    def advance(self, loop: Loop, path: Path, sender: Action | None = None) -> None:
        """One stride. The only builder of OP_ClientUpdate and the only door click.

        While the last stride is not committed and the short timeout has not
        fired, the same asked point is sent again. A closed door on the stride
        is clicked once. The stride that would pass that door waits for OP_MoveDoor.
        """
        self.advanced = True
        self.path = path
        self._drop_find(path)

        self._send_considers(loop, sender)
        here = self.position
        tick = loop.tick
        doors = self._click_doors(path)
        if self.asked and not self.committed:
            if tick - self.asked_tick < STRIDE_TIMEOUT:
                self._click_if_needed(loop, self._blocking(here, self.asked, doors))
                self._emit(loop, self.asked, self.anim, "stride")
                return
            self._settle_timeout()
            here = self.position

        nxt = self._aim(path, here)
        blocking = self._blocking(here, nxt, doors)
        if blocking:
            self._click_if_needed(loop, blocking)
            spot = (float(blocking.x), float(blocking.y), float(blocking.z))
            door_on = doors_on_stride(here, nxt, [blocking])
            if _horiz(here, spot) > 1.0 and door_on:
                nxt = self._on_floor(here, spot)
            else:
                return

        log.debug(f"start stride here {here} nxt {nxt} anim {path.anim} tick {tick}")
        log.debug(f"path.points {path.points} - destination {path.destination}")
        self._start_stride(loop, here, nxt, int(path.anim or 0), tick)

    def hold_if_idle(self, loop: Loop) -> None:
        """One hold update when this pulse did not call advance."""
        if self.advanced:
            self.advanced = False
            return

        self._emit(loop, self.position, 0, "hold")

    def visible_mobs(self, yards: float) -> list[Mob]:
        """Mobs in line of sight from the committed position. Does not send OP_Consider.

        ``yards`` skips anyone farther than that before a ray is cast. The sweep
        uses one ray. Heading peeks stay on a targeted line_of_sight call.
        """
        origin = self.position
        seen = []
        for mob in self.world.mobs.values():
            if mob.id == self.world.self_id:
                continue
            if mob.distance and float(mob.distance) > yards:
                continue
            if _sweep_visible(self.world, origin, mob):
                seen.append(mob)

        return seen

    def mobs_on_path(self, mobs: list[Mob]) -> list[MovementAnnotatedMob]:
        """Mobs on the current stride, or None. Does not send OP_Consider.

        Each result is a MovementAnnotatedMob. distance, direction, consider, and
        targeted are the values already on the Mob.
        """
        if not mobs:
            return []

        here = self.position
        end = self.asked
        if not end and self.path:
            end = self.path.next_point

        if not end:
            return []

        found = []
        for mob in mobs:
            if not _mob_on_stride(here, end, mob):
                continue

            found.append(
                MovementAnnotatedMob(
                    mob=mob,
                    distance=mob.distance,
                    direction=mob.direction,
                    consider=mob.consider,
                    targeted=bool(mob.targeted),
                )
            )
        return found

    def find(self, loop: Loop, mob: Mob) -> bool:
        """OP_FindPersonRequest when the mob is not nearby and the mesh has no route."""
        sent = path_find(loop, self.world, mob, origin=self.position)
        if sent:
            self.find_mob = mob
        return sent

    def track(self, loop: Loop, mob: Mob) -> bool:
        """OP_Track then OP_TrackTarget. Does not create a Mob."""
        return bool(path_track(loop, self.world, mob, origin=self.position))

    def _settle_timeout(self) -> None:
        """The zone does not echo our ClientUpdate. Take the asked point unless it refused us."""
        asked = self.asked
        refused = self.refused
        self.refused = False
        self.committed = True
        self.asked = None
        if refused or asked is None:
            return

        if _horiz(self.position, asked) <= 0.4 and abs(self.position[2] - asked[2]) <= 0.4:
            return

        self.position = (float(asked[0]), float(asked[1]), float(asked[2]))
        self.write_world(self.position)

    def _reused_route(
        self,
        origin: tuple[float, float, float],
        destination: tuple[float, float, float] | Mob,
        mode: str,
        length: float,
        anim: int,
        zone: str,
    ) -> Path | None:
        """The polyline already searched for this goal, measured from where we stand now."""
        key = _dest_key(destination)
        if not key:
            return None

        found = self._routes.get((zone, key))
        if not found:
            return None

        if found.find_waypoints and not _same(found.origin, origin, tol=1.0):
            self._routes.pop((zone, key), None)
            return None

        if not _on_polyline(origin, found):
            self._routes.pop((zone, key), None)
            return None

        followed = self._follow(found, origin, mode, length, anim)
        if not followed:
            self._routes.pop((zone, key), None)
            return None

        return followed

    def _follow(
        self,
        found: Path,
        origin: tuple[float, float, float],
        mode: str,
        length: float,
        anim: int,
    ) -> Path | None:
        if (
            _same(found.origin, origin, tol=0.5)
            and found.mode == mode
            and found.stride_length == length
        ):
            self.path = found
            return found

        ahead = _ahead(origin, found)
        if not ahead:
            return None

        points, remain = ahead
        found.points = points
        found.origin = origin
        found.mode = mode
        found.stride_length = length
        found.anim = anim
        found.distance = remain
        goal = found.destination
        nxt = along(origin, points or [goal], length)
        doors = self.world.doors
        live = doors_on_stride(origin, nxt, doors)

        if live:
            door = live[0]
            found.door = door
            nxt = (float(door.x), float(door.y), float(door.z))

        found.next_point = nxt
        self.path = found
        return found

    def remember_route(
        self,
        zone: str,
        destination: tuple[float, float, float] | Mob,
        path: Path,
    ) -> None:
        key = _dest_key(destination)
        if not key:
            return

        self._routes[(zone, key)] = path

    def _keep_find_path(self, built: Path) -> Path | None:
        current = self.path

        if not current or not current.find_waypoints:
            return None

        if not _same(current.destination, built.destination):
            return None

        if not _same(current.origin, self.position, tol=1.0):
            return None

        return current

    def _drop_find(self, path: Path) -> None:
        mob = self.find_mob
        if not mob or not path.find_waypoints:
            return

        origin = self.position
        if not (is_nearby(self.world, mob, origin) or self.world.line_of_sight(mob)):
            return

        path.find_waypoints = False
        zone = self.world.zone or ""
        fresh = route(
            origin,
            path.destination,
            zone=zone,
            doors=self.world.doors,
            water=self.world.get_water_map(zone),
            length=path.stride_length,
            mode=path.mode,
        )
        path.points = fresh.points
        path.door = fresh.door
        path.in_water = fresh.in_water
        path.fallback = fresh.fallback
        path.next_point = fresh.next_point
        path.origin = origin

    def _aim(self, path: Path, here: tuple[float, float, float]) -> tuple[float, float, float]:
        if path.z_only:
            target = path.swim_z if path.swim_z is not None else path.destination[2]
            return _z_step(here, target, path.stride_length)

        points = trim_points(path.points, here)
        nxt = along(here, points or [path.destination], path.stride_length)
        path.points = cut_to_step(points, nxt) if points else points
        return self._on_floor(here, nxt)

    def _on_floor(
        self,
        here: tuple[float, float, float],
        step: tuple[float, float, float],
    ) -> tuple[float, float, float]:
        """Keep the step on the floor. A stride climbs a ramp; it does not teleport in Z."""
        target_z = step[2]
        ground = self._ground((step[0], step[1], here[2]))
        if ground:
            target_z = ground

        else:
            mesh = self._mesh()
            if mesh:
                poly = mesh.nearest((step[0], step[1], here[2]))
                if (
                    poly
                    and _horiz((step[0], step[1], 0.0), (poly.center[0], poly.center[1], 0.0))
                    <= 18.0
                ):
                    target_z = poly.center[2]

        gap = target_z - here[2]
        travel = max(_horiz(here, step), 0.5)
        budget = min(10.0, max(2.0, travel * 1.5))
        if abs(gap) > budget:
            target_z = here[2] + (budget if gap > 0 else -budget)

        return (step[0], step[1], target_z)

    def _ground(self, point: tuple[float, float, float]) -> float | None:
        """Collision floor at this step. None when the zone has no map."""
        world = self.world
        zone = world.zone if world else ""
        if not zone:
            return None

        zone_map = load_map(zone)
        if not zone_map:
            return None

        return zone_map.ground(point)

    def _mesh(self) -> NavMesh | None:
        world = self.world
        zone = world.zone if world is not None else ""

        if not zone:
            return None

        if self._nav is not None and self._nav_zone == zone:
            return self._nav

        try:
            mesh = load_nav(zone)
        except (OSError, ValueError):
            log.error("nav mesh for %s failed to load", zone, exc_info=True)
            mesh = None

        self._nav = mesh
        self._nav_zone = zone
        return mesh

    def _start_stride(
        self,
        loop: Loop,
        here: tuple[float, float, float],
        nxt: tuple[float, float, float],
        anim: int,
        tick: int,
    ) -> None:
        self._emit(loop, nxt, anim, "stride")
        self.asked = nxt
        self.asked_tick = tick
        self.anim = anim
        self.committed = False
        self.refused = False
        if _horiz(here, nxt) > 0.05 or abs(nxt[2] - here[2]) > 0.05:
            self.heading = eq_heading(here[0], here[1], nxt[0], nxt[1])

    def _emit(
        self,
        loop: Loop,
        point: tuple[float, float, float],
        anim: int,
        label: str,
    ) -> None:
        self.sequence = (self.sequence + 1) & 65535
        here = self.position
        # 0 is this client. A nonzero id that is not GetID() updates a boat and the player stays put.
        spawn = 0
        stamp = int(time.time() * 1000) & 4294967295

        log.debug(
            "move %s OP_FloatListThing OP_ClientUpdate (%.1f, %.1f, %.1f) -> (%.1f, %.1f, %.1f) seq=%s anim=%s",
            label,
            here[0],
            here[1],
            here[2],
            point[0],
            point[1],
            point[2],
            self.sequence,
            anim,
        )
        loop.send(
            "OP_FloatListThing",
            OP_FloatListThing(here[0], here[1], here[2], stamp).serialize(),
        )
        loop.send(
            "OP_ClientUpdate",
            OP_ClientUpdate(
                spawn,
                point[0],
                point[1],
                point[2],
                self.sequence,
                self.heading,
                anim,
                point[0] - here[0],
                point[1] - here[1],
            ).serialize(),
        )

    def _click_if_needed(self, loop: Loop, door: Door | None) -> None:
        if not door:
            return

        ident = door.id
        if ident in self.clicked or ident in self.open_ids:
            return

        if door.opened:
            return

        self.clicked.add(ident)
        loop.send("OP_ClickDoor", OP_ClickDoor(ident).serialize())

    def _click_doors(self, path: Path) -> list[Door]:
        doors = list(self.world.doors.values())
        extra = path.door
        if isinstance(extra, Door):
            doors.append(extra)
        return doors

    def _blocking(
        self,
        here: tuple[float, float, float],
        nxt: tuple[float, float, float],
        doors: dict[int, Door] | list[Door],
    ) -> Door | None:
        for door in doors_on_stride(here, nxt, doors):
            if door.id in self.open_ids:
                continue
            if door.opened:
                continue
            return door

        for door in iter_doors(doors):

            if door.opened:
                continue

            if door.id in self.open_ids:
                continue
            spot = (float(door.x), float(door.y), float(door.z))

            if (
                _horiz(here, spot) <= 1.5
                and abs(here[2] - spot[2]) <= 20.0
                and (_horiz(here, nxt) > 1.0)
            ):
                return door

        return None

    def _send_considers(self, loop: Loop, sender: Action | None = None) -> None:
        if _is_reclaim(loop, sender):
            return

        for mob in self.world.consider_mobs():
            if not self.world.line_of_sight(mob):
                continue
            if not self.world.needs_consider(mob):
                continue
            spawn = int(self.world.self_id or 0)
            loop.send("OP_Consider", OP_Consider(spawn, mob.id).serialize())
            self.world.remember_consider(mob)

    def _on_position(self, row: OP_ClientUpdate | OP_MobUpdate) -> None:
        spawn_id = int(row.spawn_id)
        x, y, z = float(row.x), float(row.y), float(row.z)
        heading = None

        if isinstance(row, OP_ClientUpdate) and not row.server:
            heading = row.heading

        if self.world.self_id != spawn_id:
            return

        point = (x, y, z)
        if self.asked and not self.committed:
            if _same(point, self.asked, tol=_COMMIT_TOLERANCE):
                self.committed = True
                self.refused = False

            elif _horiz(point, self.position) <= 0.8 and (
                _horiz(self.position, self.asked) > 0.4
                or abs(self.position[2] - self.asked[2]) > 0.4
            ):
                self.refused = True

        self.position = point
        if heading:
            self.heading = heading

        self.write_world(point)

    def _on_new_zone(self, row: OP_NewZone) -> None:
        _short = row.short_name
        safe = (row.x, row.y, row.z)
        self.asked = None
        self.asked_tick = 0
        self.anim = 0
        self.committed = True
        self.refused = False
        self.position = safe
        self.path = None
        self._routes = {}
        self.clicked = set()
        self.open_ids = set()
        self.find_mob = None
        self.write_world(safe)
        if _short:
            self.world.zone = _short

    def _on_move_door(self, row: OP_MoveDoor) -> None:
        door_id = row.door_id
        self.open_ids.add(door_id)
        self.clicked.discard(door_id)
        mem_door = self.world.doors.get(door_id)
        if mem_door:
            mem_door.opened = True

    def _on_find_reply(self, row: OP_FindPersonReply) -> None:
        points = list(row.points)
        path = self.path
        if not path or not points:
            return
        path.points = points
        path.find_waypoints = True
        path.next_point = points[0]
        path.fallback = False


def _z_step(
    here: tuple[float, float, float], target_z: float, length: float
) -> tuple[float, float, float]:
    gap = float(target_z) - here[2]
    if abs(gap) <= length:
        nz = float(target_z)
    else:
        nz = here[2] + (length if gap > 0.0 else -length)
    return (here[0], here[1], nz)


def _surface_z(
    here: tuple[float, float, float],
    destination: tuple[float, float, float],
    water: WaterMap | None,
) -> float:
    if water:
        try:
            surf = water.surface_z(here[0], here[1])
        except (TypeError, ValueError):
            log.error("water surface lookup failed", exc_info=True)
            surf = None
        if surf:
            return float(surf)
    return float(destination[2])


def _liquid(water: WaterMap | None, point: tuple[float, float, float]) -> bool:
    if not water or not point:
        return False
    try:
        return water.in_liquid(point[0], point[1], point[2])
    except (TypeError, ValueError):
        log.error("liquid check failed", exc_info=True)
        return False


def _is_reclaim(loop: Loop, sender: Action | None) -> bool:
    current = loop.active
    for obj in (sender, current):
        if obj and type(obj).__name__ == "Reclaim":
            return True
    return False


def _sweep_visible(world: World, origin: tuple[float, float, float], mob: Mob) -> bool:
    """One cached ray. A miss falls back to line_of_sight, which peeks headings."""
    mapped = _zone_map(world)
    if mapped is None:
        return world.line_of_sight(mob)
    end = mob_point(mob)
    if end is None:
        return False
    return bool(mapped.clear(origin, end, headings=1))


def _zone_map(world: World) -> ZoneMap | None:
    mesh = world.mesh
    if mesh is not None:
        return mesh
    zone = world.zone or ""
    if not zone:
        return None
    return load_map(zone)


def _mob_on_stride(
    here: tuple[float, float, float], end: tuple[float, float, float], mob: Mob
) -> bool:
    point = mob_point(mob)

    if not point:
        return False

    if abs(point[2] - here[2]) > 20.0 and abs(point[2] - end[2]) > 20.0:
        return False

    dx, dy = (end[0] - here[0], end[1] - here[1])
    length = dx * dx + dy * dy

    if length <= 1e-06:
        return False

    tee = ((point[0] - here[0]) * dx + (point[1] - here[1]) * dy) / length
    if tee <= 0.0 or tee > 1.0:
        return False

    along_yards = math.sqrt(tee * tee * length)
    if along_yards < 1.0:
        return False

    nearest = (here[0] + tee * dx, here[1] + tee * dy)
    return math.hypot(point[0] - nearest[0], point[1] - nearest[1]) <= STRIDE_MOB_RADIUS


def _horiz(a: tuple[float, float, float], b: tuple[float, float, float]) -> float:
    return math.hypot(a[0] - b[0], a[1] - b[1])


def _dest_key(destination: tuple[float, float, float] | Mob) -> str | None:
    match destination:

        case [float(), float(), float()]:
            return f"p:{round(float(destination[0]), 1)}:{round(float(destination[1]), 1)}:{round(float(destination[2]), 1)}"

        case Mob() as mob:
            point = mob_point(mob)
            if point is None:
                return None
            return f"m:{mob.id}:{round(point[0], 1)}:{round(point[1], 1)}:{round(point[2], 1)}"

        case _:
            return None


def _ahead(
    here: tuple[float, float, float], path: Path, limit: float = 12.0
) -> tuple[list[tuple[float, float, float]], float] | None:
    """Points still in front of us, and the yards left along them.

    The first corridor segment we are still standing on wins, so a later bend
    that passes nearby does not skip the walk between.
    """
    goal = path.destination
    chain = [path.origin, *path.points]
    if not chain or _horiz(chain[-1], goal) > 0.5:
        chain.append(goal)

    for index in range(1, len(chain)):
        gap, tee = _segment_project(here, chain[index - 1], chain[index])
        if gap > limit:
            continue
        start = chain[index - 1]
        end = chain[index]
        proj = (
            start[0] + (end[0] - start[0]) * tee,
            start[1] + (end[1] - start[1]) * tee,
            end[2],
        )
        rest = chain[index:]
        return rest, _route_length(proj, rest, goal)

    return None


def _on_polyline(here: tuple[float, float, float], path: Path, limit: float = 18.0) -> bool:
    goal = path.destination
    points = [path.origin, *path.points]
    if not points or _horiz(points[-1], goal) > 0.5:
        points.append(goal)

    for index in range(1, len(points)):
        if _segment_gap(here, points[index - 1], points[index]) <= limit:
            return True

    return _horiz(here, goal) <= limit


def _segment_project(
    here: tuple[float, float, float],
    start: tuple[float, float, float],
    end: tuple[float, float, float],
) -> tuple[float, float]:
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    length = dx * dx + dy * dy
    if length <= 1e-06:
        return _horiz(here, start), 0.0

    tee = ((here[0] - start[0]) * dx + (here[1] - start[1]) * dy) / length
    if tee < 0.0:
        tee = 0.0
    elif tee > 1.0:
        tee = 1.0

    nearest = (start[0] + tee * dx, start[1] + tee * dy)
    return math.hypot(here[0] - nearest[0], here[1] - nearest[1]), tee


def _segment_gap(
    here: tuple[float, float, float],
    start: tuple[float, float, float],
    end: tuple[float, float, float],
) -> float:
    gap, _tee = _segment_project(here, start, end)
    return gap


def _route_length(
    origin: tuple[float, float, float],
    points: list[tuple[float, float, float]],
    goal: tuple[float, float, float],
) -> float:
    total = 0.0
    prev = origin
    chain = list(points)
    if not chain or _horiz(chain[-1], goal) > 0.5:
        chain.append(goal)

    for point in chain:
        total += _horiz(prev, point)
        prev = point

    return total


def _same(a: tuple[float, float, float], b: tuple[float, float, float], tol: float = 0.05) -> bool:
    return abs(a[0] - b[0]) <= tol and abs(a[1] - b[1]) <= tol and (abs(a[2] - b[2]) <= tol)
