"""Build ~/.eqclient/recipes.jsonl from a peq dump."""

from __future__ import annotations

import os
from pathlib import Path

from eqclient4.data.cache_builders.common import peq_path
from eqclient4.data.recipes import (
    DEFAULT_RECIPES,
    RecipeBook,
    build_recipes,
    read_recipes,
    write_recipes,
)


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
    if not dump.is_file():
        raise FileNotFoundError(f"PEQ file not found: {dump}")
    book = build_recipes(dump)
    write_recipes(book, path)
    return book


def main() -> None:
    book = ensure_recipes(rebuild=True)
    print(f"recipes: {len(book.by_id)} → {DEFAULT_RECIPES}", flush=True)


if __name__ == "__main__":
    main()
