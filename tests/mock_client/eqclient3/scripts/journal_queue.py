"""Print one character's open queue in the order the scheduler would run it.

From the mock_client directory:

    python -m eqclient3.journal_queue
    python -m eqclient3.journal_queue Mockvthree
"""
from __future__ import annotations

import sys
from datetime import datetime

from eqclient3.journal import Journal


def main(argv: list[str] | None = None) -> None:
    args = list(sys.argv[1:] if argv is None else argv)
    character = args[0] if args else ""
    journal = Journal()
    try:
        print("\n".join(report(journal, character)))
    finally:
        journal.close()


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
    lines.append(f"resolved {len(resolved)}")
    for kind, source, zone, priority in resolved:
        short = str(kind).rsplit(":", 1)[-1]
        lines.append(f"     p{int(priority):<4}  {short:<12} {source:<28} {zone or '-'}")
    return lines


def _ordered(actions: list) -> list:
    stamped = 0
    for action in actions:
        if int(action.insert or 0):
            stamped = max(stamped, int(action.insert))
            continue
        stamped += 1
        action.insert = stamped
    return sorted(actions, key=_order_key)


def _order_key(action) -> tuple:
    try:
        detail = tuple(type(action).key(action))
        failed = 0
    except Exception as error:
        detail = (str(error),)
        failed = 1
    return (-int(action.priority or 0), failed, detail)


def _line(rank: int, action) -> str:
    started = ""
    if action.started:
        started = datetime.fromtimestamp(float(action.started)).strftime("%H:%M:%S")
    detail = _detail(action)
    zone = action.zone or "-"
    return f"{rank:2}  p{int(action.priority):<4}  {type(action).__name__:<12} {action.source:<28} {zone:<12} {started}  {detail}".rstrip()


def _detail(action) -> str:
    skip = {
        "source", "zone", "priority", "durable", "insert", "started",
        "complete", "suspended", "yielding", "messages", "active_path",
        "waited", "limit",
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
