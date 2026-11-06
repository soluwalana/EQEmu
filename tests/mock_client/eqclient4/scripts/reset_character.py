"""Clear one character's queue and the tutorial and quest started marks.

From the mock_client directory:

    python -m eqclient4.scripts.reset_character Mockvthree
"""

from __future__ import annotations

import sys

from eqclient4.journal import Journal
from eqclient4.world import World


def main(argv: list[str] | None = None) -> None:
    args = list(sys.argv[1:] if argv is None else argv)
    if not args:
        raise SystemExit("python -m eqclient4.reset_character NAME")
    character = args[0]
    world = World(character)
    journal = Journal(character, world)
    try:
        print("\n".join(report(reset(journal), character)))
    finally:
        journal.close()


def reset(journal: Journal) -> dict[str, int]:
    """Drop the queue, the quest goals, the tutorial-done row, and both started flags."""
    counts = {
        "actions": journal.clear_actions(),
        "goals": journal.clear_goals(),
    }
    journal.set_flag("tutorial_state", 0)
    journal.set_flag("quest_started", 0)
    return counts


def report(counts: dict[str, int], character: str) -> list[str]:
    return [
        f"{character}",
        f"actions {counts['actions']}",
        f"goals {counts['goals']}",
        "tutorial_started 0",
        "quest_started 0",
    ]


if __name__ == "__main__":
    main()
