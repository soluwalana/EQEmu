"""Clear one character's queue and the tutorial and quest started marks.

From the mock_client directory:

    python -m eqclient3.reset_character Mockvthree
"""
from __future__ import annotations

import sys

from eqclient3.journal import Journal


def main(argv: list[str] | None = None) -> None:
    args = list(sys.argv[1:] if argv is None else argv)
    if not args:
        raise SystemExit("python -m eqclient3.reset_character NAME")
    character = args[0]
    journal = Journal()
    try:
        print("\n".join(report(reset(journal, character), character)))
    finally:
        journal.close()


def reset(journal: Journal, character: str) -> dict[str, int]:
    """Drop the queue, the quest goals, the tutorial-done row, and both started flags."""
    counts = {
        "actions": journal.clear_actions(character),
        "goals": journal.clear_goals(character),
        "tutorial": journal.clear_tutorial(character),
    }
    journal.set_flag(character, "tutorial_started", 0)
    journal.set_flag(character, "quest_started", 0)
    return counts


def report(counts: dict[str, int], character: str) -> list[str]:
    return [
        f"{character}",
        f"actions {counts['actions']}",
        f"goals {counts['goals']}",
        f"tutorial {counts['tutorial']}",
        "tutorial_started 0",
        "quest_started 0",
    ]


if __name__ == "__main__":
    main()
