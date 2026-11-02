"""Print one character's open queue in the order the scheduler would run it.

Each character has their own database. From the mock_client directory:

    python -m eqclient3.scripts.journal_queue Mockvthree
"""

from __future__ import annotations

import sys
from datetime import datetime

from eqclient3.action import Action
from eqclient3.journal import Journal, characters
from eqclient3.log import log


def main(argv: list[str] | None = None) -> None:
    args = list(sys.argv[1:] if argv is None else argv)
    names = [args[0]] if args else sorted(characters())
    if not names:
        print("no journal actions")
        return
    blocks: list[str] = []
    for name in names:
        journal = Journal(character=name)
        try:
            blocks.append("\n".join(report(journal, name)))
        finally:
            journal.close()
    print("\n\n".join(blocks))


def report(journal: Journal, character: str = "") -> list[str]:
    names = [character] if character else _characters(journal)
    if not names:
        return ["no journal actions"]
    lines: list[str] = []
    for name in names:
        if lines:
            lines.append("")
        lines.extend(_character(journal, name))
    return lines


def _characters(journal: Journal) -> list[str]:
    rows = journal._db.execute("SELECT DISTINCT character FROM actions ORDER BY character")
    return [str(name) for name, in rows]


def _character(journal: Journal, character: str) -> list[str]:
    open_rows = _ordered(journal.load_actions(character))
    resolved = journal._db.execute(
        "SELECT kind, source, zone, priority FROM actions WHERE character = ? AND resolved = 1 ORDER BY position",
        (character,),
    ).fetchall()
    lines = [f"{character}  open {len(open_rows)}"]
    if not open_rows:
        lines.append("  (empty)")
    for rank, action in enumerate(open_rows, start=1):
        lines.append(_line(rank, action))
    lines.extend(_inventory(journal, character))
    lines.append(f"resolved {len(resolved)}")
    for kind, source, zone, priority in resolved:
        short = str(kind).rsplit(":", 1)[-1]
        lines.append(f"     p{int(priority):<4}  {short:<12} {source:<28} {zone or '-'}")
    return lines


_WORN = (
    "charm",
    "ear1",
    "head",
    "face",
    "ear2",
    "neck",
    "shoulders",
    "arms",
    "back",
    "wrist1",
    "wrist2",
    "range",
    "hands",
    "primary",
    "secondary",
    "finger1",
    "finger2",
    "chest",
    "legs",
    "feet",
    "waist",
    "ammo",
)


def _inventory(journal: Journal, character: str) -> list[str]:
    slots = journal.inventory(character)
    lines = [f"inventory {len(slots)}"]
    if not slots:
        lines.append("  (empty)")
        return lines
    for row in slots:
        count = f" x{row.stack}" if row.stack > 1 else ""
        name = row.name or str(row.item_id)
        lines.append(f"  {_slot_label(row.slot)}: {name}{count} ({row.item_id})")
    return lines


def _slot_label(slot: int) -> str:
    if 0 <= slot < len(_WORN):
        return _WORN[slot]
    if 22 <= slot <= 29:
        return f"pack {slot - 21}"
    if slot == 30:
        return "cursor"
    return f"slot {slot}"


def _ordered(actions: list) -> list:
    stamped = 0
    for action in actions:
        if int(action.insert or 0):
            stamped = max(stamped, int(action.insert))
            continue
        stamped += 1
        action.insert = stamped
    return sorted(actions, key=_order_key)


def _order_key(action: Action) -> tuple[object, ...]:
    try:
        detail = tuple(type(action).key(action))
        failed = 0
    except Exception as error:
        log.error("action key failed", exc_info=True)
        detail = (str(error),)
        failed = 1
    return (-int(action.priority or 0), failed, detail)


def _line(rank: int, action: Action) -> str:
    started = ""
    if action.started:
        started = datetime.fromtimestamp(float(action.started)).strftime("%H:%M:%S")
    detail = _detail(action)
    zone = action.zone or "-"
    return f"{rank:2}  p{int(action.priority):<4}  {type(action).__name__:<12} {action.source:<28} {zone:<12} {started}  {detail}".rstrip()


def _detail(action: Action) -> str:
    skip = {
        "source",
        "zone",
        "priority",
        "durable",
        "insert",
        "started",
        "complete",
        "suspended",
        "yielding",
        "messages",
        "active_path",
        "waited",
        "limit",
    }
    bits: list[str] = []
    if action.waiting:
        bits.append(f"wait={action.wait_label()}")
    for key, value in action.__dict__.items():
        if key in skip or key.startswith("_"):
            continue
        if value in (0, "", None, False, [], {}):
            continue
        bits.append(f"{key}={value}")
    return " ".join(bits)


if __name__ == "__main__":
    main()
