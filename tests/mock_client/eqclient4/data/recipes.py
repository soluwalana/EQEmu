"""Tradeskill recipes cached as recipes.jsonl."""

from __future__ import annotations

import json
import os
from collections.abc import Iterable, Iterator
from dataclasses import dataclass, field
from pathlib import Path

from eqclient4.data.cache_builders.common import peq_path
from eqclient4.data.catalog import (
    _BAG_TYPES,
    _apply_recipe_skill,
    _take_recipe,
    _take_recipe_skill,
)

DEFAULT_RECIPES = str(Path.home() / ".eqclient" / "recipes.jsonl")

# Portable kits are item ids; world stations reuse BagType enums (see catalog._BAG_TYPES).
_WORLD_CONTAINER = frozenset(_BAG_TYPES)


def _enabled(value: object) -> int:
    if isinstance(value, int) and not isinstance(value, bool):
        return value
    return 1


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

    def to_row(self) -> dict[str, object]:
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
            enabled=_enabled(row.get("enabled")),
            name=str(row.get("name") or ""),
        )


@dataclass
class RecipeBook:
    by_id: dict[int, Recipe] = field(default_factory=dict)
    by_result: dict[int, list[int]] = field(default_factory=dict)
    by_skill: dict[int, list[int]] = field(default_factory=dict)
    by_container: dict[int, list[int]] = field(default_factory=dict)

    def index(self) -> None:
        """item id → recipe ids that produce it, including multi-result combines."""
        for recipe_id, recipe in self.by_id.items():
            made = {recipe.result}
            made.update(item_id for item_id, _count in recipe.results)
            for item_id in made:
                if item_id > 0:
                    self.by_result.setdefault(item_id, []).append(recipe_id)

            if recipe.skill and recipe.enabled and recipe.components:
                self.by_skill.setdefault(int(recipe.skill), []).append(recipe_id)

            self.by_container.setdefault(recipe.container, []).append(recipe_id)

    def practice(self, skill_id: int, current: int, want: int, skip: int = 0) -> Recipe | None:
        """A moderately hard combine for skillups (EQ: skillups only while skill < trivial).

        Prefer trivial a bit above `current` (challenge window), never already-trivial,
        and never past the goal `want`. `skip` is the recipe this practice is in service
        of, so its components are not burned on the way up.
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
            if skip and recipe.id == skip:
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

        def _rank(recipe: Recipe) -> tuple[int, int, int, int]:
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
        candidates.sort(
            key=lambda recipe: (len(recipe.components), recipe.trivial or 9999, recipe.id)
        )
        return candidates[0]

    def craft_list(self) -> list[tuple[int, int, tuple[tuple[int, int], ...]]]:
        """(result, recipe_id, components) for craft_for — enabled recipes with real ingredients only."""
        out: list[tuple[int, int, tuple[tuple[int, int], ...]]] = []
        for recipe in self.by_id.values():
            if not recipe.enabled or not recipe.result or not recipe.components:
                continue
            out.append((recipe.result, recipe.id, recipe.components))
        return out

    def container_crafts(self, container_id: int) -> list[Recipe]:
        if container_id not in self.by_container:
            return []
        return [self.by_id[recipe_id] for recipe_id in self.by_container[container_id]]


def recipes_from_lines(lines: Iterable[str]) -> list[tuple[int, int, tuple[tuple[int, int], ...]]]:
    """Parse dump INSERT lines into the craft_for tuple list (enabled + has components)."""
    return _book_from_lines(lines).craft_list()


def _book_from_lines(lines: Iterable[str]) -> RecipeBook:
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
            enabled=_enabled(info.get("enabled")),
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
    peq: str | Path | None = None,
    *,
    rebuild: bool = False,
) -> RecipeBook:
    """Load recipes.jsonl, or build once from the peq dump."""
    path = path or os.environ.get("EQEMU_RECIPES", DEFAULT_RECIPES)
    file = Path(path)
    if file.is_file() and not rebuild:
        return read_recipes(path)
    dump = peq_path(peq)
    book = build_recipes(dump) if dump.is_file() else RecipeBook()
    if book.by_id:
        write_recipes(book, path)
    return book


def _lines(path: str) -> Iterator[str]:
    with open(path, encoding="latin1", errors="replace") as handle:
        yield from handle
