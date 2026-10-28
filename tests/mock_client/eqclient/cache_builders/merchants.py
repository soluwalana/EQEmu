"""Build ~/.eqclient/merchants.jsonl from a peq dump."""

from __future__ import annotations

import os
from pathlib import Path

from eqclient.cache_builders.common import peq_path
from eqclient.merchants import (
    DEFAULT_MERCHANTS,
    MerchantBook,
    build_merchants,
    read_merchants,
    write_merchants,
)


def ensure_merchants(
    path: str | None = None,
    peq: str | Path | None = None,
    *,
    rebuild: bool = False,
) -> MerchantBook:
    """Load merchants.jsonl, or build once from the peq dump."""
    path = path or os.environ.get("EQEMU_MERCHANTS", DEFAULT_MERCHANTS)
    file = Path(path)
    if file.is_file() and not rebuild:
        return read_merchants(path)
    dump = peq_path(peq)
    book = build_merchants(dump) if dump.is_file() else MerchantBook()
    if book.by_npc:
        write_merchants(book, path)
    return book


def main() -> None:
    book = ensure_merchants(rebuild=True)
    print(f"merchants: {len(book.by_npc)} npcs → {DEFAULT_MERCHANTS}", flush=True)


if __name__ == "__main__":
    main()
