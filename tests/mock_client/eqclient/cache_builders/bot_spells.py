"""Build ~/.eqclient/bot_spells.jsonl from bots bootstrap + peq dump.

bot_spells_entries (npc_spells_id 3001–3016) come from bot_tables_bootstrap.sql.
Spell names and list labels are mapped from peq `spells_new` / `npc_spells`.
"""

from __future__ import annotations

import os
from pathlib import Path

from eqclient.bot_spells import (
    DEFAULT_BOT_SPELLS,
    BotSpellBook,
    build_bot_spells,
    read_bot_spells,
    write_bot_spells,
)
from eqclient.cache_builders.common import peq_path


def ensure_bot_spells(
    path: str | None = None,
    peq: str | Path | None = None,
    bootstrap: str | Path | None = None,
    *,
    rebuild: bool = False,
) -> BotSpellBook:
    """Load bot_spells.jsonl, or build once from bootstrap + peq."""
    path = path or os.environ.get("EQEMU_BOT_SPELLS", DEFAULT_BOT_SPELLS)
    file = Path(path)
    if file.is_file() and not rebuild:
        return read_bot_spells(path)
    dump = peq_path(peq)
    book = build_bot_spells(dump if dump.is_file() else None, bootstrap)
    if book.rows:
        write_bot_spells(book, path)
    return book


def main() -> None:
    book = ensure_bot_spells(rebuild=True)
    named = sum(1 for row in book.rows if row.name)
    lists = sorted(book.list_names.items())
    print(
        f"bot_spells: {len(book.rows)} entries ({named} named), "
        f"{len(book.by_list)} lists → {DEFAULT_BOT_SPELLS}",
        flush=True,
    )
    for list_id, name in lists:
        print(f"  {list_id} {name}: {len(book.by_list.get(list_id, ()))}", flush=True)


if __name__ == "__main__":
    main()
