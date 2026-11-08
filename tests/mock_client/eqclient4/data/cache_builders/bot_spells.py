"""Build ~/.eqclient/bot_spells.jsonl from bots bootstrap + peq dump.

bot_spells_entries (npc_spells_id 3001–3016) come from bot_tables_bootstrap.sql.
Spell names and list labels are mapped from peq `spells_new` / `npc_spells`.
"""

from eqclient4.data.bot_spells import DEFAULT_BOT_SPELLS, ensure_bot_spells


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
