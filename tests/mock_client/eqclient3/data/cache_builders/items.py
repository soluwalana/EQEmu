"""Build ~/.eqclient/items.jsonl from a peq dump (AC + primary stats)."""

from __future__ import annotations

import os
from pathlib import Path

from eqclient3.data.cache_builders.common import peq_path


def _stats():
    # inventory.item_stats is not in this tree.
    from eqclient3.inventory.item_stats import (
        DEFAULT_ITEMS,
        ItemBook,
        build_items,
        read_items,
        write_items,
    )
    return DEFAULT_ITEMS, ItemBook, build_items, read_items, write_items


def ensure_items(
    path: str | None = None,
    peq: str | Path | None = None,
    *,
    rebuild: bool = False,
):
    """Load items.jsonl, or build once from the peq dump."""
    DEFAULT_ITEMS, ItemBook, build_items, read_items, write_items = _stats()
    path = path or os.environ.get("EQEMU_ITEMS", DEFAULT_ITEMS)
    file = Path(path)
    if file.is_file() and not rebuild:
        return read_items(path)
    dump = peq_path(peq)
    book = build_items(dump) if dump.is_file() else ItemBook()
    if book.by_id:
        write_items(book, path)
    return book


def main() -> None:
    default, *_ = _stats()
    book = ensure_items(rebuild=True)
    print(f"items: {len(book.by_id)} → {default}", flush=True)


if __name__ == "__main__":
    main()
