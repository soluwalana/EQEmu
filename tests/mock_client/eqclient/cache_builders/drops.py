"""Build ~/.eqclient/drops.jsonl from a peq dump."""

from __future__ import annotations

import os
from pathlib import Path

from eqclient.cache_builders.common import peq_path
from eqclient.drops import DEFAULT_DROPS, DropBook, build_drops, read_drops, write_drops


def _version_ok(path: str) -> bool:
    from eqclient.drops import _version_ok as check

    return check(path)


def ensure_drops(
    path: str | None = None,
    peq: str | Path | None = None,
    *,
    rebuild: bool = False,
) -> DropBook:
    """Load drops.jsonl, or build once from the peq dump."""
    path = path or os.environ.get("EQEMU_DROPS", DEFAULT_DROPS)
    file = Path(path)
    if file.is_file() and not rebuild and _version_ok(path):
        return read_drops(path)
    dump = peq_path(peq)
    book = build_drops(dump) if dump.is_file() else DropBook()
    if book.by_npc:
        write_drops(book, path)
        return book
    if file.is_file():
        return read_drops(path)
    return book


def main() -> None:
    book = ensure_drops(rebuild=True)
    print(f"drops: {len(book.by_npc)} npcs → {DEFAULT_DROPS}", flush=True)


if __name__ == "__main__":
    main()
