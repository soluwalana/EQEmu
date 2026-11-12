"""Rebuild one or all ~/.eqclient caches.

Examples:
  python -m eqclient4.data.cache_builders
  python -m eqclient4.data.cache_builders faction_list spells
"""

from __future__ import annotations

import importlib
import os
import sys

from eqclient4.data.cache_builders import BUILDERS


def main(argv: list[str] | None = None) -> None:
    names = list(argv if argv is not None else sys.argv[1:])
    if not names or names == ["all"]:
        names = [name for name in BUILDERS if name != "quest_graph"]
        # quest_graph needs EQEMU_QUESTS; include only when set or asked for.
        if os.environ.get("EQEMU_QUESTS"):
            names.append("quest_graph")
    unknown = [name for name in names if name not in BUILDERS]
    if unknown:
        raise SystemExit(
            f"unknown builders: {', '.join(unknown)}; choose from {', '.join(BUILDERS)}"
        )
    for name in names:
        module = importlib.import_module(f"eqclient4.data.cache_builders.{name}")
        module.main()


if __name__ == "__main__":
    main()
