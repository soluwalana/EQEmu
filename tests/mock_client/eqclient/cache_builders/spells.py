"""Build ~/.eqclient/spells.jsonl from a peq dump."""

from __future__ import annotations

import os
from pathlib import Path

from eqclient.cache_builders.common import peq_path
from eqclient.spells import DEFAULT_SPELLS, SpellBook, build_spells, read_spells, write_spells


def ensure_spells(
    path: str | None = None,
    peq: str | Path | None = None,
    *,
    rebuild: bool = False,
) -> SpellBook:
    """Load spells.jsonl, or build once from the peq dump."""
    path = path or os.environ.get("EQEMU_SPELLS", DEFAULT_SPELLS)
    file = Path(path)
    if file.is_file() and not rebuild:
        return read_spells(path)
    dump = peq_path(peq)
    book = build_spells(dump) if dump.is_file() else SpellBook()
    if book.rows:
        write_spells(book, path)
    return book


def main() -> None:
    book = ensure_spells(rebuild=True)
    print(f"spells: {len(book.rows)} scrolls → {DEFAULT_SPELLS}", flush=True)


if __name__ == "__main__":
    main()
