"""Shared paths for offline cache builders."""

from __future__ import annotations

import os
from pathlib import Path

CACHE_DIR = Path.home() / ".eqclient"
# cache_builders/ → data/ → eqclient3/ → mock_client/ → tests/ → EQEmu/
DEFAULT_PEQ = Path(__file__).resolve().parents[5] / "peq-dump" / "create_tables_content.sql"


def peq_path(peq: str | Path | None = None) -> Path:
    raw = peq or os.environ.get("EQEMU_PEQ", "") or str(DEFAULT_PEQ)
    return Path(raw)


def cache_path(name: str, override: str | None = None) -> Path:
    if override:
        return Path(override)
    return CACHE_DIR / name


def lines(path: str | Path):
    with open(path, encoding="latin1", errors="replace") as handle:
        yield from handle
