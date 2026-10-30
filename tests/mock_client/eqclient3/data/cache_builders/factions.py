"""Build ~/.eqclient/faction_hits.jsonl from a peq dump."""

from __future__ import annotations

import os
from pathlib import Path

from eqclient3.data.cache_builders.common import peq_path
from eqclient3.data.factions import (
    DEFAULT_FACTIONS,
    FactionBook,
    build_factions,
    read_factions,
    write_factions,
)


def ensure_factions(
    path: str | None = None,
    peq: str | Path | None = None,
    *,
    rebuild: bool = False,
) -> FactionBook:
    """Load faction_hits.jsonl, or build once from the peq dump."""
    path = path or os.environ.get("EQEMU_FACTIONS", DEFAULT_FACTIONS)
    file = Path(path)
    if file.is_file() and not rebuild:
        return read_factions(path)
    dump = peq_path(peq)
    book = build_factions(dump) if dump.is_file() else FactionBook()
    if book.by_faction or book.primary_of:
        write_factions(book, path)
    return book


def main() -> None:
    book = ensure_factions(rebuild=True)
    print(
        f"faction_hits: {len(book.by_faction)} factions, "
        f"{len(book.primary_of)} primaries → {DEFAULT_FACTIONS}",
        flush=True,
    )


if __name__ == "__main__":
    main()
