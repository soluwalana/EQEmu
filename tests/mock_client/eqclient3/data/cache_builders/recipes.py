"""Build ~/.eqclient/recipes.jsonl from a peq dump."""

from __future__ import annotations

import os
from pathlib import Path

from eqclient3.data.cache_builders.common import peq_path


def _conduct():
    # quests.conduct is not in this tree.
    from eqclient3.quests.conduct import (
        DEFAULT_RECIPES,
        RecipeBook,
        build_recipes,
        read_recipes,
        write_recipes,
    )
    return DEFAULT_RECIPES, RecipeBook, build_recipes, read_recipes, write_recipes


def ensure_recipes(
    path: str | None = None,
    peq: str | Path | None = None,
    *,
    rebuild: bool = False,
):
    """Load recipes.jsonl, or build once from the peq dump."""
    DEFAULT_RECIPES, RecipeBook, build_recipes, read_recipes, write_recipes = _conduct()
    path = path or os.environ.get("EQEMU_RECIPES", DEFAULT_RECIPES)
    file = Path(path)
    if file.is_file() and not rebuild:
        return read_recipes(path)
    dump = peq_path(peq)
    book = build_recipes(dump) if dump.is_file() else RecipeBook()
    if book.by_id:
        write_recipes(book, path)
    return book


def main() -> None:
    default, *_ = _conduct()
    book = ensure_recipes(rebuild=True)
    print(f"recipes: {len(book.by_id)} → {default}", flush=True)


if __name__ == "__main__":
    main()
