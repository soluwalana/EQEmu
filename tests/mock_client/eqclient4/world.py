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
from collections import defaultdict
from dataclasses import dataclass
from typing import Literal

from eqclient4.data.ground import GroundSpawnBook, ensure_ground_spawns
from eqclient4.data.items import ItemBook, ensure_items
from eqclient4.data.merchants import MerchantBook, ensure_merchants
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
from eqclient4.nav.path import is_nearby, mob_point, route
from eqclient4.nav.path import track as path_track
from eqclient4.nav.path import trim_points
from eqclient4.nav.travel import ZoneGraph, ensure_zone_graph
from eqclient4.nav.water import WaterMap, load_water
from eqclient4.quests.graph import QuestGraph, load_graph
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
class GroundSpawn:
    id: int
    name: str
    x: float
    y: float
    z: float
    used: bool = False


@dataclass
class Bot:
    name: str = ""
    class_id: int = 0
    level: int = 0
    hp: int = 0
    max_hp: int = 0
    mana: int = 0
    max_mana: int = 0
    id: int = 0
    alive: bool = True


@dataclass
class Consider:
    standing: int = 0
    level_color: int = 0
    name: str = ""


class Abilities:
    """Skills and the gear that lets bash fire. Owned by Character."""

    def __init__(self) -> None:
        self.skills: dict[int, int] = {}
        self.can_bash: bool = False
        self.shield: bool = False
        self.two_hand: bool = False


class Character:
    """The player this sheet is showing. name is the journal key.

    Stats, inventory, and whether the tutorial and the quest have started live here.
    """

    def __init__(self, name: str = "") -> None:
        self.name: str = name
        self.abilities: Abilities = Abilities()
        self.tutorial_started: bool = False
        self.quest_started: bool = False
        self.self_id: int = 0
        self.class_id: int = 0
        self.race: int = 0
        self.gender: int = 0
        self.deity: int = 0
        self.level: int = 0
        self.exp: int = 0
        self.training_points: int = 0
        self.points: int = 0
        self.hp: int = 0
        self.max_hp: int = 0
        self.mana: int = 0
        self.max_mana: int = 0
        self.food: int = 0
        self.water: int = 0
        self.strength: int = 0
        self.stamina: int = 0
        self.agility: int = 0
        self.dexterity: int = 0
        self.wisdom: int = 0
        self.intelligence: int = 0
        self.charisma: int = 0
        self.coin: tuple[int, int, int, int] = (0, 0, 0, 0)

    def ability_known(self, skill_id: int) -> bool:
        skills = self.abilities.skills
        return int(skills.get(skill_id, 0)) > 0

    @property
    def coin(self) -> tuple[int, int, int, int]:
        return self.coin

    @coin.setter
    def coin(self, value: tuple[int, int, int, int]) -> None:
        self.coin = value

    def set_coin(self, platinum: int, gold: int, silver: int, copper: int) -> None:
        """Replace the four denominations. None meant the profile had not arrived."""
        self.coin = (int(platinum), int(gold), int(silver), int(copper))

    def add_coins(self, platinum: int, gold: int, silver: int, copper: int) -> None:
        """Add each denomination. Unknown coin starts at zero."""
        self.coin[0] += int(platinum)
        self.coin[1] += int(gold)
        self.coin[2] += int(silver)
        self.coin[3] += int(copper)

    def add_coin(
        self,
        coin: int,
    ) -> None:
        plat, gold, silver, copper = self.coin
        p, coin = divmod(coin, 1000)
        g, coin = divmod(coin, 100)
        s, c = divmod(coin, 10)
        self.set_coin(plat + p, gold + g, silver + s, copper + c)

    def deduct_coins(
        self,
        price: int,
    ) -> tuple[int, int, int, int] | None:
        """Deduct copper-denominated price, matching EQEmu's TakeMoneyFromPP."""
        plat, gold, silver, copper = self.coin

        if price < 0:
            raise ValueError("Negative price")

        total = plat * 1000 + gold * 100 + silver * 10 + copper
        if price > total:
            return None  # Insufficient funds

        if copper >= price:
            return plat, gold, silver, copper - price

        price -= copper
        copper = 0

        if silver * 10 >= price:
            silver, copper = divmod(silver * 10 - price, 10)
            return plat, gold, silver, copper

        price -= silver * 10
        silver = 0

        if gold * 100 >= price:
            gold, remainder = divmod(gold * 100 - price, 100)
            silver, copper = divmod(remainder, 10)
            return plat, gold, silver, copper

        price -= gold * 100
        gold = 0

        plat, remainder = divmod(plat * 1000 - price, 1000)
        gold, remainder = divmod(remainder, 100)
        silver, copper = divmod(remainder, 10)

        return plat, gold, silver, copper


class GroupRoster:
    """Members and leader. mode is party or raid."""

    def __init__(self, mode: RosterMode) -> None:
        self.mode: RosterMode = mode
        self.members: list[str] = []
        self.leader: str = ""
        self.bots: list[Bot] = []


class Bots:
    """Roster and heal rotation. reconstituted_at is the loop tick of the last reconstitute."""

    def __init__(self) -> None:
        self.reconstituted_at: int = 0
        self.roster: list[Bot] = []
        self.rotation: list[str] = []


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
    def x(self) -> float:
        return self._position[0]

    @x.setter
    def x(self, value: float) -> None:
        self.position = (float(value), self._position[1], self._position[2])

    @property
    def y(self) -> float:
        return self._position[1]

    @y.setter
    def y(self, value: float) -> None:
        self.position = (self._position[0], float(value), self._position[2])

    @property
    def z(self) -> float:
        return self._position[2]

    @z.setter
    def z(self, value: float) -> None:
        self.position = (self._position[0], self._position[1], float(value))

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
        self.character = Character(name)
        self.self_id = 0
        self.level = 0
        self.exp = 0
        self.training_points = 0
        self.points = 0
        self.factions: dict[int, Faction] = {}
        self.zone: str | None = None
        self.zone_id = -1
        self.zone_formed: str | None = None
        self.home_zone_id = 0
        self.safe: tuple[float, float, float] | None = None
        self._x = float(0)
        self._y = float(0)
        self._z = float(0)
        self.mobs = MobMap(self)
        self.doors: dict[int, Door] = {}
        self.ground: dict[int, GroundSpawn] = {}
        self.water_maps: dict[str, WaterMap] = {}
        self.group = GroupRoster("party")
        self.raid = GroupRoster("raid")
        self.bots = Bots()
        self.spells: dict[int, int] = {}
        self.gems: dict[int, int] = {}
        self.buffs: dict[tuple[int, int], object] = {}
        self.tasks: TaskBook = TaskBook()
        self.item_book: ItemBook = ensure_items()
        self.quest_graph: QuestGraph = _cached_graph()
        self.zone_graph: ZoneGraph = ensure_zone_graph()
        self.merchants: MerchantBook = ensure_merchants()
        self.ground_book: GroundSpawnBook = ensure_ground_spawns()
        self.mesh: ZoneMap | None = None
        self.exit_doors: dict[str, dict[int, list[int]]] = {}
        self.aggro_mobs: dict[int, Mob] = {}
        self.spell_book: dict = {}
        self.spell_info: dict = {}
        self.spell_names: dict = {}
        self.scrolls: dict = {}
        self.tomes: dict = {}
        self.soulbinder = None
        self.soulbound = ""
        self.afflictions: list = []
        self.at_water = False
        self.trainer_point: tuple[float, float, float] | None = None
        self.train_skill = 0
        self.zone_names: dict = {}
        self.faction_names: dict = {}
        self.faction_quests: list = []
        self.faction_npcs: list = []
        self.leader_point: tuple[float, float, float] | None = None
        self.camps: dict = {}
        self.level_spells: list = []
        self.level_gear: list = []
        self.guildmaster = 0
        self.quest_items: set = set()
        self.movement = Movement(self)

        self.inventory: CharacterInventory = CharacterInventory()
        self.active_merchants: dict[int, Merchant] = defaultdict(Merchant)

    def active_merchant(self) -> Merchant | None:
        for npc_id, merchant in self.active_merchants.items():
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

    @property
    def x(self) -> float:
        return self._x

    @x.setter
    def x(self, value: float) -> None:
        self._x = float(value)
        for mob in self.mobs.values():
            self.measure(mob)

    @property
    def y(self) -> float:
        return self._y

    @y.setter
    def y(self, value: float) -> None:
        self._y = float(value)
        for mob in self.mobs.values():
            self.measure(mob)

    @property
    def z(self) -> float:
        return self._z

    @z.setter
    def z(self, value: float) -> None:
        self._z = float(value)
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
        found = self.factions.get(faction_id)
        if not found:
            found = Faction()
            self.factions[faction_id] = found
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
        if self.asked is not None and (not self.committed):
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
        if key is None:
            return None
        found = self._routes.get((zone, key))
        if found is None:
            return None
        if found.find_waypoints and not _same(found.origin, origin, tol=1.0):
            self._routes.pop((zone, key), None)
            return None
        if not _on_polyline(origin, found):
            self._routes.pop((zone, key), None)
            return None
        followed = self._follow(found, origin, mode, length, anim)
        if followed is None:
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
        if ahead is None:
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
        if key is None:
            return
        self._routes[(zone, key)] = path

    def _keep_find_path(self, built: Path) -> Path | None:
        current = self.path
        if current is None or not current.find_waypoints:
            return None
        if not _same(current.destination, built.destination):
            return None
        if not _same(current.origin, self.position, tol=1.0):
            return None
        return current

    def _drop_find(self, path: Path) -> None:
        mob = self.find_mob
        if mob is None or not path.find_waypoints:
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
        if ground is not None:
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
        roster = doors.values() if isinstance(doors, dict) else doors
        for door in roster:
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
        origin = self.position
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
        heading = row.heading if isinstance(row, OP_ClientUpdate) and not row.server else None
        if self.world.self_id != spawn_id:
            return
        point = (x, y, z)
        if self.asked is not None and (not self.committed):
            if _same(point, self.asked, tol=_COMMIT_TOLERANCE):
                self.committed = True
                self.refused = False
            elif _horiz(point, self.position) <= 0.8 and (
                _horiz(self.position, self.asked) > 0.4
                or abs(self.position[2] - self.asked[2]) > 0.4
            ):
                self.refused = True
        self.position = point
        if heading is not None:
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
    if a is None or b is None:
        return False
    return abs(a[0] - b[0]) <= tol and abs(a[1] - b[1]) <= tol and (abs(a[2] - b[2]) <= tol)


def pack_server_position(spawn_id: int, x: float, y: float, z: float) -> bytes:
    """RoF2 server position, so a test can commit a stride."""
    return OP_MobUpdate(spawn_id, x, y, z).serialize()


def _cached_graph() -> QuestGraph:
    try:
        return load_graph()
    except OSError:
        log.error("quest graph failed to load", exc_info=True)
        raise RuntimeError("quest graph failed to load")
