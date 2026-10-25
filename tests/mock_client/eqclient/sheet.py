"""Character creation from the race and class the agent was asked to play.

Titanium checks the total of the seven stats and rejects a race that cannot be
that class. A dark elf paladin never gets as far as the zone. The point pool
goes on the earliest class stat that shares the highest bonus, which is strength
for a warrior.
"""

from __future__ import annotations

from dataclasses import dataclass

# STR, STA, AGI, DEX, WIS, INT, CHA. Index is race id minus one, except the four
# races whose ids are not sequential.
_RACE_STATS = (
    (75, 75, 75, 75, 75, 75, 75),
    (103, 95, 82, 70, 70, 60, 55),
    (60, 70, 70, 70, 83, 107, 70),
    (65, 65, 95, 80, 80, 75, 75),
    (55, 65, 85, 70, 95, 92, 80),
    (60, 65, 90, 75, 83, 99, 60),
    (70, 70, 90, 85, 60, 75, 75),
    (90, 90, 70, 90, 83, 60, 45),
    (108, 109, 83, 75, 60, 52, 40),
    (130, 122, 70, 70, 67, 60, 37),
    (70, 75, 95, 90, 80, 67, 50),
    (60, 70, 85, 85, 67, 98, 60),
    (70, 70, 90, 85, 80, 75, 55),
    (90, 75, 90, 70, 70, 65, 65),
    (70, 80, 100, 100, 75, 75, 50),
    (70, 80, 85, 75, 80, 85, 75),
)

# The eighth number is the point pool.
_CLASS_STATS = (
    (10, 10, 5, 0, 0, 0, 0, 25),
    (5, 5, 0, 0, 10, 0, 0, 30),
    (10, 5, 0, 0, 5, 0, 10, 20),
    (5, 10, 10, 0, 5, 0, 0, 20),
    (10, 5, 0, 0, 0, 10, 5, 20),
    (0, 10, 0, 0, 10, 0, 0, 30),
    (5, 5, 10, 10, 0, 0, 0, 20),
    (5, 0, 0, 10, 0, 0, 10, 25),
    (0, 0, 10, 10, 0, 0, 0, 30),
    (0, 5, 0, 0, 10, 0, 5, 30),
    (0, 0, 0, 10, 0, 10, 0, 30),
    (0, 10, 0, 0, 0, 10, 0, 30),
    (0, 10, 0, 0, 0, 10, 0, 30),
    (0, 0, 0, 0, 0, 10, 10, 30),
    (0, 10, 5, 0, 10, 0, 5, 20),
    (10, 5, 0, 10, 0, 0, 0, 25),
)

# Columns follow the race table: human through gnome, then iksar, vah shir, froglok, drakkin.
_ALLOWED = (
    "1101011111111111",
    "1010110100010011",
    "1010101100010011",
    "1000101000010001",
    "1010001010001011",
    "1000101000010001",
    "1000000000001001",
    "1000101000000101",
    "1101011100010101",
    "0100000011001010",
    "1010010000001011",
    "1010110000000011",
    "1010110000000001",
    "1010110000000001",
    "0100000011001000",
    "0100000111000100",
)

_CLASS_NAMES = (
    "warrior",
    "cleric",
    "paladin",
    "ranger",
    "shadow knight",
    "druid",
    "monk",
    "bard",
    "rogue",
    "shaman",
    "necromancer",
    "wizard",
    "magician",
    "enchanter",
    "beastlord",
    "berserker",
)

# race id, table index, name, titanium start-city index, deity.
# Drakkin has no titanium home city; Qeynos is a city the default switch accepts.
_RACES = {
    1: (0, "human", 1, 396),
    2: (1, "barbarian", 2, 214),
    3: (2, "erudite", 0, 210),
    4: (3, "wood elf", 9, 215),
    5: (4, "high elf", 10, 215),
    6: (5, "dark elf", 5, 206),
    7: (6, "half elf", 1, 396),
    8: (7, "dwarf", 8, 202),
    9: (8, "troll", 6, 203),
    10: (9, "ogre", 7, 211),
    11: (10, "halfling", 3, 205),
    12: (11, "gnome", 11, 202),
    128: (12, "iksar", 12, 203),
    130: (13, "vah shir", 13, 396),
    330: (14, "froglok", 14, 208),
    522: (15, "drakkin", 1, 396),
}


class CharacterError(ValueError):
    pass


@dataclass(frozen=True)
class Character:
    race: int
    class_id: int
    gender: int
    deity: int
    start_zone: int
    stats: tuple[int, int, int, int, int, int, int]
    race_name: str
    class_name: str


def build(
    race: int = 1,
    class_id: int = 1,
    gender: int = 0,
    deity: int | None = None,
    start_zone: int | None = None,
) -> Character:
    """Stats, deity, and starting city for this race and class."""
    row = _RACES.get(race)
    if row is None:
        raise CharacterError(f"race {race} is not a player race")
    if class_id < 1 or class_id > len(_CLASS_NAMES):
        raise CharacterError(f"class {class_id} is not a player class")
    index, race_name, home, home_deity = row
    class_name = _CLASS_NAMES[class_id - 1]
    if _ALLOWED[class_id - 1][index] != "1":
        raise CharacterError(f"a {race_name} cannot be a {class_name}")
    race_stats = _RACE_STATS[index]
    class_stats = _CLASS_STATS[class_id - 1]
    base = [race_stats[i] + class_stats[i] for i in range(7)]
    points = class_stats[7]
    favored = max(range(7), key=lambda i: (class_stats[i], -i))
    base[favored] += points
    return Character(
        race,
        class_id,
        gender,
        home_deity if deity is None else deity,
        home if start_zone is None else start_zone,
        (base[0], base[1], base[2], base[3], base[4], base[5], base[6]),
        race_name,
        class_name,
    )
