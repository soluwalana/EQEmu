"""The sheet the server is showing us. Handlers write it. Actions read it.

Our bodies are Reclaim actions on the queue. NPC bodies are LootMob actions.
The player stats, inventory, and tutorial and quest started flags live on character.
"""
from __future__ import annotations
import math
from dataclasses import dataclass
from typing import Literal

from eqclient3.struct_helpers import eq_heading
from .log import log

from .nav.maps import load_map as _load_zone_map

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
        self.coin: tuple[int, int, int, int] | None = None
        self.bags: dict[int, int] = {}
        self.cursor: int | None = None
        self.items: dict = {}


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

    def __init__(self, id: int, name: str='', npc: int=0, level: int=0, position: tuple[float, float, float]=(0.0, 0.0, 0.0), hp: int=0) -> None:
        self.id = id
        self.name = name
        self.npc = npc
        self.level = level
        self.body = 0
        self.class_id = 0
        self.race = 0
        self.hp = hp
        self.max_hp = 0
        self.mana: int | None = None
        self.max_mana: int | None = None
        self.consider: Consider | None = None
        self.faction_id = 0
        self.faction_last_considered = None
        self.targeted = False
        self.dead = False
        self._consider_sent = False
        self._consider_change_sent = False
        self.distance = 0.0
        self.direction = 0
        self._world: World | None = None
        self._position = (0.0, 0.0, 0.0)
        self.position = position

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
        if self._world is not None:
            self._world.measure(self)

class MobMap(dict[int, Mob]):
    """mobs[id] = Mob. Assigning a mob attaches it and measures distance."""

    def __init__(self, world: World) -> None:
        super().__init__()
        self._world = world

    def __setitem__(self, key: int, mob: Mob) -> None:
        mob._world = self._world
        super().__setitem__(key, mob)
        self._world.measure(mob)

class World:

    def __init__(
        self,
        *,
        name: str = "",
        zone: str = "",
        zone_id: int = 0,
        self_id: int = 0,
        level: int = 0,
        exp: int = 0,
        points: int = 0,
        x: float = 0.0,
        y: float = 0.0,
        z: float = 0.0,
        ground: dict[int, GroundSpawn] | None = None,
    ) -> None:
        self.character = Character(name)
        self.self_id = self_id
        self.level = level
        self.exp = exp
        self.training_points = points
        self.points = points
        self.factions: dict[int, Faction] = {}
        self.zone = zone
        self.zone_id = zone_id
        self.home_zone_id = 0
        self.safe: tuple[float, float, float] | None = None
        self._x = float(x)
        self._y = float(y)
        self._z = float(z)
        self.mobs = MobMap(self)
        self.doors: dict[int, Door] = {}
        self.ground: dict[int, GroundSpawn] = {} if ground is None else ground
        self.water_map = None
        self.group = GroupRoster("party")
        self.leader = ""
        self.raid = GroupRoster("raid")
        self.bots = Bots()
        self.spells: dict[int, int] = {}
        self.gems: dict[int, int] = {}
        self.buffs: dict[tuple[int, int], object] = {}
        self.task_book = None
        self.tasks = None
        self.pending_death: int | None = None
        self.pending_corpse: int = 0
        self.pending_where: tuple[float, float, float] | None = None
        self.fought: set[int] = set()
        self.spell_book: dict = {}
        self.spell_info: dict = {}
        self.spell_names: dict = {}
        self.scrolls: dict = {}
        self.tomes: dict = {}
        self.gem_slot: int | None = None
        self.plans: dict = {}
        self.soulbinder = None
        self.soulbound = ""
        self.afflictions: list = []
        self.at_water = False
        self.zoneline = None
        self.zone_graph = None
        self.follow_up = None
        self.trainer_point: tuple[float, float, float] | None = None
        self.train_skill = 0
        self.empty_slots: int | None = None
        self.zone_names: dict = {}
        self.faction_names: dict = {}
        self.faction_quests: list = []
        self.faction_npcs: list = []
        self.reachable: set = set()
        self.forage_found = False
        self.leader_point: tuple[float, float, float] | None = None
        self.camps: dict = {}
        self.level_spells: list = []
        self.level_gear: list = []
        self.guildmaster = 0
        self.rezz_payload = None
        self.rest_mana = False
        self.cursor_move = None
        self.pending_swap = None
        self.quest_items: set = set()
        self.station = None
        self.mesh = None
        from eqclient3.movement import Movement
        self.movement = Movement(self)

    @property
    def self_id(self) -> int:
        return self.character.self_id

    @self_id.setter
    def self_id(self, value: int) -> None:
        self.character.self_id = int(value or 0)

    @property
    def class_id(self) -> int:
        return self.character.class_id

    @class_id.setter
    def class_id(self, value: int) -> None:
        self.character.class_id = int(value or 0)

    @property
    def race(self) -> int:
        return self.character.race

    @race.setter
    def race(self, value: int) -> None:
        self.character.race = int(value or 0)

    @property
    def gender(self) -> int:
        return self.character.gender

    @gender.setter
    def gender(self, value: int) -> None:
        self.character.gender = int(value or 0)

    @property
    def deity(self) -> int:
        return self.character.deity

    @deity.setter
    def deity(self, value: int) -> None:
        self.character.deity = int(value or 0)

    @property
    def level(self) -> int:
        return self.character.level

    @level.setter
    def level(self, value: int) -> None:
        self.character.level = int(value or 0)

    @property
    def exp(self) -> int:
        return self.character.exp

    @exp.setter
    def exp(self, value: int) -> None:
        self.character.exp = int(value or 0)

    @property
    def training_points(self) -> int:
        return self.character.training_points

    @training_points.setter
    def training_points(self, value: int) -> None:
        self.character.training_points = int(value or 0)

    @property
    def points(self) -> int:
        return self.character.points

    @points.setter
    def points(self, value: int) -> None:
        self.character.points = int(value or 0)

    @property
    def hp(self) -> int:
        return self.character.hp

    @hp.setter
    def hp(self, value: int) -> None:
        self.character.hp = int(value or 0)

    @property
    def max_hp(self) -> int:
        return self.character.max_hp

    @max_hp.setter
    def max_hp(self, value: int) -> None:
        self.character.max_hp = int(value or 0)

    @property
    def mana(self) -> int:
        return self.character.mana

    @mana.setter
    def mana(self, value: int) -> None:
        self.character.mana = int(value or 0)

    @property
    def max_mana(self) -> int:
        return self.character.max_mana

    @max_mana.setter
    def max_mana(self, value: int) -> None:
        self.character.max_mana = int(value or 0)

    @property
    def food(self) -> int:
        return self.character.food

    @food.setter
    def food(self, value: int) -> None:
        self.character.food = int(value or 0)

    @property
    def water(self) -> int:
        return self.character.water

    @water.setter
    def water(self, value: int) -> None:
        self.character.water = int(value or 0)

    @property
    def strength(self) -> int:
        return self.character.strength

    @strength.setter
    def strength(self, value: int) -> None:
        self.character.strength = int(value or 0)

    @property
    def stamina(self) -> int:
        return self.character.stamina

    @stamina.setter
    def stamina(self, value: int) -> None:
        self.character.stamina = int(value or 0)

    @property
    def agility(self) -> int:
        return self.character.agility

    @agility.setter
    def agility(self, value: int) -> None:
        self.character.agility = int(value or 0)

    @property
    def dexterity(self) -> int:
        return self.character.dexterity

    @dexterity.setter
    def dexterity(self, value: int) -> None:
        self.character.dexterity = int(value or 0)

    @property
    def wisdom(self) -> int:
        return self.character.wisdom

    @wisdom.setter
    def wisdom(self, value: int) -> None:
        self.character.wisdom = int(value or 0)

    @property
    def intelligence(self) -> int:
        return self.character.intelligence

    @intelligence.setter
    def intelligence(self, value: int) -> None:
        self.character.intelligence = int(value or 0)

    @property
    def charisma(self) -> int:
        return self.character.charisma

    @charisma.setter
    def charisma(self, value: int) -> None:
        self.character.charisma = int(value or 0)

    @property
    def coin(self) -> tuple[int, int, int, int] | None:
        return self.character.coin

    @coin.setter
    def coin(self, value: tuple[int, int, int, int] | None) -> None:
        self.character.coin = value

    def set_coin(self, platinum: int, gold: int, silver: int, copper: int) -> None:
        """Replace the four denominations. None meant the profile had not arrived."""
        self.character.coin = (int(platinum), int(gold), int(silver), int(copper))

    def add_coin(self, platinum: int, gold: int, silver: int, copper: int) -> None:
        """Add each denomination. Unknown coin starts at zero."""
        current = self.character.coin or (0, 0, 0, 0)
        self.character.coin = (
            current[0] + int(platinum),
            current[1] + int(gold),
            current[2] + int(silver),
            current[3] + int(copper),
        )

    @property
    def bags(self) -> dict[int, int]:
        return self.character.bags

    @bags.setter
    def bags(self, value: dict[int, int]) -> None:
        self.character.bags = value

    @property
    def cursor(self) -> int | None:
        return self.character.cursor

    @cursor.setter
    def cursor(self, value: int | None) -> None:
        self.character.cursor = None if value is None else int(value)

    @property
    def items(self) -> dict:
        return self.character.items

    @items.setter
    def items(self, value: dict) -> None:
        self.character.items = value

    @property
    def tutorial_started(self) -> bool:
        return self.character.tutorial_started

    @tutorial_started.setter
    def tutorial_started(self, value: bool) -> None:
        self.character.tutorial_started = bool(value)

    @property
    def quest_started(self) -> bool:
        return self.character.quest_started

    @quest_started.setter
    def quest_started(self, value: bool) -> None:
        self.character.quest_started = bool(value)

    @property
    def name(self) -> str:
        return self.character.name

    @name.setter
    def name(self, value: str) -> None:
        self.character.name = str(value or "")

    @property
    def skills(self) -> dict[int, int]:
        return self.character.abilities.skills

    @skills.setter
    def skills(self, value: dict[int, int]) -> None:
        self.character.abilities.skills = dict(value)

    @property
    def can_bash(self) -> bool:
        return self.character.abilities.can_bash

    @can_bash.setter
    def can_bash(self, value: bool) -> None:
        self.character.abilities.can_bash = bool(value)

    @property
    def shield(self) -> bool:
        return self.character.abilities.shield

    @shield.setter
    def shield(self, value: bool) -> None:
        self.character.abilities.shield = bool(value)

    @property
    def two_hand(self) -> bool:
        return self.character.abilities.two_hand

    @two_hand.setter
    def two_hand(self, value: bool) -> None:
        self.character.abilities.two_hand = bool(value)

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

    def note_fight(self, spawn_id: int) -> None:
        """This spawn attacked us, or we attacked it. Loot uses the set."""
        if spawn_id:
            self.fought.add(spawn_id)

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
        end = tuple(mob.position)
        mesh = self.mesh if self.mesh is not None else _zone_mesh(self.zone)
        if mesh is None:
            return True
        return bool(mesh.clear(start, end))

    def faction(self, faction_id: int) -> Faction:
        found = self.factions.get(faction_id)
        if found is None:
            found = Faction()
            self.factions[faction_id] = found
        return found

    def held(self, item_id: int) -> int:
        """How many bag slots, plus the cursor, hold this item id."""
        total = sum((1 for item in self.bags.values() if item == item_id))
        if self.cursor == item_id:
            total += 1
        return total

_loaded: dict[str, object | None] = {}

def _zone_mesh(zone: str) -> object | None:
    """The zone mesh, or None when the zone file cannot be read. A miss is tried again later."""
    if not zone:
        return None
    if zone in _loaded:
        return _loaded[zone]
    try:
        mesh = _load_zone_map(zone)
    except (OSError, ValueError):
        log.error("zone mesh for %s failed to load", zone, exc_info=True)
        mesh = None
    _loaded[zone] = mesh
    return mesh
