"""Build ~/.eqclient/faction_list.jsonl from a peq dump."""

from __future__ import annotations

import json
import re
from pathlib import Path

from eqclient3.data.cache_builders.common import cache_path, lines, peq_path

DEFAULT_FACTION_LIST = str(cache_path("faction_list.jsonl"))
_SEED = {
    "truespirit": 404,
    "call of the wild": 404,
}


def build_faction_list(peq: str | Path) -> dict[str, int]:
    """Parse faction_list INSERT rows into name → id."""
    found = dict(_SEED)
    mode = False
    for line in lines(peq):
        if line.startswith("INSERT INTO `faction_list`"):
            mode = True
            continue
        if mode and line.startswith("INSERT INTO `"):
            # Another faction_list block can follow; keep scanning for it.
            mode = line.startswith("INSERT INTO `faction_list`")
            continue
        if not mode:
            continue
        # Rows like (404,'Truespirit',0),
        for match in re.finditer(r"\((\d+),'((?:\\'|[^'])*)'", line):
            fac_id = int(match.group(1))
            name = match.group(2).replace("\\'", "'").lower()
            if name and fac_id:
                found[name] = fac_id
    return found


def write_faction_list(names: dict[str, int], path: str | Path) -> None:
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    rows = [
        json.dumps({"id": fac_id, "name": name}, ensure_ascii=True)
        for name, fac_id in sorted(names.items(), key=lambda pair: (pair[1], pair[0]))
        if name and fac_id
    ]
    destination.write_text("\n".join(rows) + ("\n" if rows else ""), encoding="utf-8")


def read_faction_list(path: str | Path | None = None) -> dict[str, int]:
    """Load name → id from the jsonl cache (no peq fallback)."""
    found = dict(_SEED)
    file = Path(path) if path else Path(DEFAULT_FACTION_LIST)
    if not file.is_file():
        return found
    for line in file.open(encoding="utf-8", errors="replace"):
        line = line.strip()
        if not line:
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError:
            continue
        name = str(row.get("name") or "").lower()
        try:
            fac_id = int(row.get("id") or 0)
        except (TypeError, ValueError):
            continue
        if name and fac_id:
            found[name] = fac_id
    return found


def ensure_faction_list(
    path: str | None = None,
    peq: str | Path | None = None,
    *,
    rebuild: bool = False,
) -> dict[str, int]:
    """Write faction_list.jsonl from peq when missing (or rebuild=True)."""
    out = str(path or DEFAULT_FACTION_LIST)
    file = Path(out)
    if file.is_file() and not rebuild:
        return read_faction_list(out)
    dump = peq_path(peq)
    names = build_faction_list(dump) if dump.is_file() else dict(_SEED)
    if names:
        write_faction_list(names, out)
    return names


def main() -> None:
    names = ensure_faction_list(rebuild=True)
    print(f"faction_list: {len(names)} names → {DEFAULT_FACTION_LIST}", flush=True)


if __name__ == "__main__":
    main()
