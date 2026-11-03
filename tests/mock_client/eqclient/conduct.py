"""Decisions that are not a task step: hunger, a tell, a class ability, a recipe.

The planner still picks the quest. This module answers the packets around it.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path

from eqclient.catalog import _BAG_TYPES, _apply_recipe_skill, _take_recipe, _take_recipe_skill

ORDERS = (
    "invite",
    "follow",
    "camp",
    "attack",
    "come",
    "summon",
    "farm",
    "goal",
    "get",
    "obtain",
    "join",
    "group",
    "party",
)
# Tell phrases that mean "add me to your group" when the first word is not an ORDER.
_JOIN_PHRASES = (
    "invite me",
    "add me",
    "group me",
    "party me",
    "join me",
    "invite please",
    "group please",
    "add to group",
    "add to party",
)
FOOD_WORDS = ("bread", "ration", "meat", "cheese", "pie", "stew", "mushroom", "patty", "fish")
DRINK_WORDS = ("water", "drink", "ale", "wine", "milk", "cider", "tea")
ROLES = (
    "heal",
    "root",
    "snare",
    "slow",
    "mez",
    "stun",
    "dot",
    "nuke",
    "pet",
    "haste",
    "rez",
    "summon",
    "lifetap",
    "port",
    "buff",
    "shield",
    "mend",
)


@dataclass
class Order:
    verb: str
    sender: str
    rest: str = ""


def order_of(sender: str, text: str) -> Order | None:
    words = text.lower().split()
    if not words:
        return None
    lowered = " ".join(words)
    # "invite me" / "group me" mean join-the-PC, not "invite <other>".
    if any(phrase in lowered for phrase in _JOIN_PHRASES):
        return Order("join", sender, "")
    if words[0] in ORDERS:
        return Order(words[0], sender, " ".join(words[1:]))
    return None


def farm_target(rest: str) -> tuple[int, int] | None:
    """Parse '1001', '1001 5', or '1001 x5' into (item_id, count)."""
    words = (rest or "").lower().replace("x", " ").split()
    if not words:
        return None
    try:
        item_id = int(words[0])
    except ValueError:
        return None
    count = 1
    if len(words) >= 2:
        try:
            count = max(1, int(words[1]))
        except ValueError:
            count = 1
    return item_id, count


def bar_needed(food: int, water: int) -> str:
    """Half of 127. A full bar is not a reason to eat."""
    if 0 < food < 64:
        return "food"
    if 0 < water < 64:
        return "water"
    return ""


# Classic DD / AE names rarely contain the word "nuke".
_NUKE_HINTS = (
    "shock of",
    "blast of",
    "burst of",
    "fire bolt",
    "frost bolt",
    "lava bolt",
    "lightning bolt",
    "fire flux",
    "fingers of fire",
    "chaotic feedback",
    "chaos flux",
    "color flux",
    "shallow breath",
    "whirl till",
    "suffocating sphere",
    "force strike",
    "flame bolt",
    "ignite",
    "scorch",
    "ice comet",
    "column of",
    "rain of",
)


def role_of(name: str) -> str:
    text = name.lower()
    for role in ROLES:
        if role in text:
            return role
    if "complete heal" in text or text.endswith(" heal") or " healing" in text:
        return "heal"
    if any(hint in text for hint in _NUKE_HINTS) or text.endswith(" bolt"):
        return "nuke"
    return ""


DEFAULT_RECIPES = str(Path.home() / ".eqclient" / "recipes.jsonl")

# Portable kits are item ids; world stations reuse BagType enums (see catalog._BAG_TYPES).
_WORLD_CONTAINER = frozenset(_BAG_TYPES)


@dataclass(frozen=True)
class Recipe:
    id: int
    result: int
    components: tuple[tuple[int, int], ...]
    container: int = 0
    results: tuple[tuple[int, int], ...] = ()
    skill: int = 0
    skillneeded: int = 0
    trivial: int = 0
    enabled: int = 1
    name: str = ""

    def to_row(self) -> dict:
        return {
            "id": self.id,
            "result": self.result,
            "components": [list(pair) for pair in self.components],
            "container": self.container,
            "results": [list(pair) for pair in self.results],
            "skill": self.skill,
            "skillneeded": self.skillneeded,
            "trivial": self.trivial,
            "enabled": self.enabled,
            "name": self.name,
        }

    @classmethod
    def from_row(cls, row: dict) -> Recipe:
        components = tuple((int(a), int(b)) for a, b in (row.get("components") or ()))
        results = tuple((int(a), int(b)) for a, b in (row.get("results") or ()))
        return cls(
            id=int(row.get("id") or 0),
            result=int(row.get("result") or 0),
            components=components,
            container=int(row.get("container") or 0),
            results=results,
            skill=int(row.get("skill") or 0),
            skillneeded=int(row.get("skillneeded") or 0),
            trivial=int(row.get("trivial") or 0),
            enabled=int(row.get("enabled") if row.get("enabled") is not None else 1),
            name=str(row.get("name") or ""),
        )


@dataclass
class RecipeBook:
    by_id: dict[int, Recipe] = field(default_factory=dict)
    by_result: dict[int, list[int]] = field(default_factory=dict)
    by_skill: dict[int, list[int]] = field(default_factory=dict)

    def index(self) -> None:
        """item id → recipe ids that produce it, including multi-result combines."""
        found: dict[int, list[int]] = {}
        by_skill: dict[int, list[int]] = {}
        for recipe_id, recipe in self.by_id.items():
            made = {recipe.result}
            made.update(item_id for item_id, _count in recipe.results)
            for item_id in made:
                if item_id > 0:
                    found.setdefault(item_id, []).append(recipe_id)
            if recipe.skill and recipe.enabled and recipe.components:
                by_skill.setdefault(int(recipe.skill), []).append(recipe_id)
        self.by_result = found
        self.by_skill = by_skill

    def practice(self, skill_id: int, current: int, want: int) -> Recipe | None:
        """A moderately hard combine for skillups (EQ: skillups only while skill < trivial).

        Prefer trivial a bit above `current` (challenge window), never already-trivial,
        and never past the goal `want`. Result item is what the campaign stacks in bulk.
        """
        candidates: list[Recipe] = []
        current = int(current or 0)
        want = int(want or 0)
        # Sweet spot: hard enough to skill, not a wall of fails.
        sweet_lo = current + 5
        sweet_hi = current + 40
        if want > 0:
            sweet_hi = min(sweet_hi, want)
        sweet_lo = max(current + 1, min(sweet_lo, sweet_hi))
        for recipe_id in self.by_skill.get(int(skill_id), ()):
            recipe = self.by_id.get(recipe_id)
            if recipe is None or not recipe.enabled or not recipe.components:
                continue
            if not recipe.result:
                continue
            trivial = int(recipe.trivial or 0)
            needed = int(recipe.skillneeded or 0)
            if trivial <= 0 or trivial <= current:
                continue
            if needed > current:
                continue
            if want and trivial > want:
                continue
            # Skip refund/recombine (result also consumed).
            inputs = {comp for comp, _count in recipe.components}
            if recipe.container and recipe.container not in _WORLD_CONTAINER:
                inputs.add(recipe.container)
            if recipe.result in inputs:
                continue
            if recipe.container in _WORLD_CONTAINER:
                continue
            candidates.append(recipe)
        if not candidates:
            return None

        def _rank(recipe: Recipe) -> tuple:
            trivial = int(recipe.trivial or 0)
            in_sweet = 0 if sweet_lo <= trivial <= sweet_hi else 1
            # Prefer in-window, then closest to mid-window, then fewer ingredients.
            mid = (sweet_lo + sweet_hi) // 2
            return (in_sweet, abs(trivial - mid), len(recipe.components), recipe.id)

        candidates.sort(key=_rank)
        return candidates[0]

    def for_item(self, item_id: int) -> Recipe | None:
        """An enabled combine that creates this item and does not consume it."""
        candidates: list[Recipe] = []
        for recipe_id in self.by_result.get(item_id, ()):
            recipe = self.by_id.get(recipe_id)
            if recipe is None or not recipe.enabled or not recipe.components:
                continue
            inputs = {comp for comp, _count in recipe.components}
            if recipe.container and recipe.container not in _WORLD_CONTAINER:
                inputs.add(recipe.container)
            if item_id in inputs:
                continue
            candidates.append(recipe)
        if not candidates:
            return None
        candidates.sort(key=lambda recipe: (len(recipe.components), recipe.trivial or 9999, recipe.id))
        return candidates[0]

    def craft_list(self) -> list[tuple[int, int, tuple[tuple[int, int], ...]]]:
        """(result, recipe_id, components) for craft_for — enabled recipes with real ingredients only."""
        out: list[tuple[int, int, tuple[tuple[int, int], ...]]] = []
        for recipe in self.by_id.values():
            if not recipe.enabled or not recipe.result or not recipe.components:
                continue
            out.append((recipe.result, recipe.id, recipe.components))
        return out


def load_recipes(path: str) -> list[tuple[int, int, tuple[tuple[int, int], ...]]]:
    """Result item, recipe id, and components. Prefers a recipes.jsonl cache; else peq dump."""
    file = Path(path)
    if file.suffix == ".jsonl" or file.name == "recipes.jsonl":
        return read_recipes(str(file)).craft_list()
    return recipes_from_lines(_lines(path))


def recipes_from_lines(lines) -> list[tuple[int, int, tuple[tuple[int, int], ...]]]:
    """Parse dump INSERT lines into the craft_for tuple list (enabled + has components)."""
    return _book_from_lines(lines).craft_list()


def _book_from_lines(lines) -> RecipeBook:
    recipes: dict[int, dict] = {}
    skill: dict[int, dict] = {}
    mode = ""
    for line in lines:
        if line.startswith("INSERT INTO `tradeskill_recipe`"):
            mode = "recipe"
            continue
        if line.startswith("INSERT INTO `tradeskill_recipe_entries`"):
            mode = "entries"
            continue
        if line.startswith("INSERT INTO `"):
            mode = ""
            continue
        if not line.startswith("("):
            continue
        if mode == "recipe":
            _take_recipe_skill(line, skill)
        elif mode == "entries":
            _take_recipe(line, recipes)
    _apply_recipe_skill(recipes, skill)
    book = RecipeBook()
    for recipe_id, info in recipes.items():
        result = int(info.get("result") or 0)
        components = tuple((int(a), int(b)) for a, b in (info.get("components") or ()))
        results = tuple((int(a), int(b)) for a, b in (info.get("results") or ()))
        book.by_id[int(recipe_id)] = Recipe(
            id=int(recipe_id),
            result=result,
            components=components,
            container=int(info.get("container") or 0),
            results=results,
            skill=int(info.get("skill") or 0),
            skillneeded=int(info.get("skillneeded") or 0),
            trivial=int(info.get("trivial") or 0),
            enabled=int(info.get("enabled") if info.get("enabled") is not None else 1),
            name=str(info.get("name") or info.get("skill_name") or ""),
        )
    book.index()
    return book


def build_recipes(peq: str | Path) -> RecipeBook:
    """Build the book from a local peq dump. No live DB query."""
    return _book_from_lines(_lines(str(peq)))


def write_recipes(book: RecipeBook, path: str) -> None:
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        json.dumps(recipe.to_row(), ensure_ascii=True)
        for recipe_id, recipe in sorted(book.by_id.items())
        if recipe_id > 0
    ]
    destination.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")


def read_recipes(path: str) -> RecipeBook:
    book = RecipeBook()
    file = Path(path)
    if not file.is_file():
        return book
    for line in file.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        recipe = Recipe.from_row(json.loads(line))
        if recipe.id:
            book.by_id[recipe.id] = recipe
    book.index()
    return book


def ensure_recipes(
    path: str | None = None,
    peq: str | None = None,
    *,
    rebuild: bool = False,
) -> RecipeBook:
    """Build/load via cache_builders. Prefer read_recipes at runtime."""
    from eqclient.cache_builders.recipes import ensure_recipes as _ensure

    return _ensure(path, peq, rebuild=rebuild)


def _lines(path: str):
    with open(path, encoding="latin1", errors="replace") as handle:
        yield from handle


def craft_for(
    needs: set[int],
    held: dict[int, int],
    recipes: list[tuple[int, int, tuple[tuple[int, int], ...]]] | RecipeBook,
    *,
    book: RecipeBook | None = None,
) -> int:
    """Recipe id whose result is still needed, ingredients are held, and a usable container is available."""
    if isinstance(recipes, RecipeBook):
        book = recipes
        rows = recipes.craft_list()
    else:
        rows = recipes
    for result_id, recipe_id, components in rows:
        if result_id not in needs or not components:
            continue
        if not recipe_ready(result_id, components, held):
            continue
        recipe = None
        if book is not None:
            recipe = book.by_id.get(recipe_id)
        if recipe is not None:
            if not recipe.enabled:
                continue
            # World stations (forge/oven/…) need to be clicked in-zone; skip until we hold a kit.
            if recipe.container in _WORLD_CONTAINER:
                continue
            if recipe.container > 0 and held.get(recipe.container, 0) < 1:
                continue
        return recipe_id
    return 0


def recipe_ready(result_id: int, components: tuple[tuple[int, int], ...], held: dict[int, int]) -> bool:
    """True when every component is already in the bags and the recipe has ingredients."""
    if result_id <= 0 or not components:
        return False
    return all(held.get(item_id, 0) >= count for item_id, count in components)


# Server reuse from common/features.h (seconds). Agent gates sends with these.
ABILITY_REUSE: dict[str, float] = {
    "taunt": 5.0,
    "kick": 5.0,
    "bash": 5.0,
    "OP_Taunt": 5.0,
    "OP_Forage": 10.0,
    "OP_Fishing": 10.0,
    "OP_Begging": 8.0,
    "OP_Mend": 360.0,
    "OP_Sneak": 7.0,
    "OP_Hide": 8.0,
    "OP_FeignDeath": 8.0,
    "OP_SenseHeading": 0.0,  # no server recovery timer
    "OP_SenseTraps": 9.0,
    "OP_DisarmTraps": 9.0,
    "OP_Disarm": 8.0,
    "OP_PickPocket": 8.0,
    "OP_ApplyPoison": 8.0,
    "OP_AutoFire": 0.0,
}


def ability_reuse(name: str) -> float:
    return float(ABILITY_REUSE.get(name, 8.0))


def ability_for(
    class_id: int, skills: dict[int, int], *, hungry: bool, in_fight: bool, leaving: bool, broke: bool = False
) -> str:
    """The opcode name to send, or empty. A skill of zero means this class does not have it."""

    def has(skill: int) -> bool:
        return skills.get(skill, 0) > 0

    if hungry and has(27):
        return "OP_Forage"
    if hungry and has(55):
        return "OP_Fishing"
    if broke and not in_fight and has(67):
        return "OP_Begging"
    if not in_fight and has(32):
        return "OP_Mend"
    # Sneak/Hide are toggles (sneak needs motion) — practiced explicitly, not via this picker.
    if not in_fight and has(29):
        return "OP_Hide"
    if leaving and class_id == 7 and has(25):
        return "OP_FeignDeath"
    if not in_fight and has(40):
        return "OP_SenseHeading"
    if has(62):
        return "OP_SenseTraps"
    if has(17):
        return "OP_DisarmTraps"
    if in_fight and has(16):
        return "OP_Disarm"
    if in_fight and class_id == 9 and has(48):
        return "OP_PickPocket"
    if in_fight and class_id == 9 and has(6):
        return "OP_ApplyPoison"
    if in_fight and class_id == 4 and has(7):
        return "OP_AutoFire"
    return ""
