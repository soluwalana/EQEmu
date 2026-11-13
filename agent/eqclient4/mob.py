from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient4.world import World

from eqclient4.utils import normalize_mob_name,  FactionStanding

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
        class_id: int = 0,
        race: int = 0,
    ) -> None:
        self.id = id
        self.name = name
        self.last_name = last_name or ""
        self.npc = npc
        self.level = level
        self.body = 0
        self.class_id = class_id
        self.race = race
        self.hp: int = hp
        self.max_hp: int = 0
        self.mana: int | None = None
        self.max_mana: int | None = None
        self.heading: float = 0.0
        self.animation: int = 0
        self.faction_id: int | None = None
        self.faction_last_considered: FactionStanding | None = None
        self.targeted = False
        self.dead = False
        self.deleted = False
        self.distance = 0.0
        self.direction = 0
        self._position = (0.0, 0.0, 0.0)
        self.position = position

    @property
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
    
    @property
    def kos(self) -> bool:
        return self.faction_last_considered in (
            FactionStanding.SCOWLS,
            FactionStanding.THREATENINGLY,
        )

    @property
    def friendly(self) -> bool:
        return self.faction_last_considered in (
            FactionStanding.ALLY,
            FactionStanding.WARMLY,
            FactionStanding.KINDLY,
            FactionStanding.AMIABLY,
        )


class MobMap(dict[int, Mob]):
    """mobs[id] = Mob. Assigning a mob attaches it and measures distance."""

    def __init__(self, world: World) -> None:
        super().__init__()
        self._world = world

    def __setitem__(self, key: int, mob: Mob) -> None:
        super().__setitem__(key, mob)
        self._world.measure(mob)

    def mob_named(self, name: str) -> Mob | None:
        want = normalize_mob_name(name)
        if not want:
            return None

        partial = None
        for mob in self.values():
            found = normalize_mob_name(mob.name)
            if found == want:
                return mob
            if want in found and partial is None:
                partial = mob

        return partial

    def find_mob(self, spawn_id: int) -> Mob | None:
        for mob_id, mob in self.items():
            if mob_id == spawn_id or mob.id == spawn_id:
                return mob
            short = spawn_id & 65535
            if short == (mob_id & 65535) or short == (mob.id & 65535):
                return mob
        return None
