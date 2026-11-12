#!/usr/bin/env python3
"""Generate a static Python InnateSkill/AASkill enum module from EQEmu headers.

Usage from EQEmu/agent:
    python scripts/generate_eq_skill_enums.py \
        --repo-root ../.. \
        --output eqclient4/structs/skill_enums.py

The generated AASkill constants are the *rank IDs* in zone/aa.h's aaID
enumeration (not aa_ability.id and not conventional SkillType IDs).
"""

import argparse
import re
from pathlib import Path


def enum_constants(path: Path, enum_name: str) -> dict[str, int]:
    source = path.read_text(encoding="utf-8")
    # Eliminate C++ comments before scanning so commented-out identifiers
    # cannot accidentally become enum members.
    source = re.sub(r"/\*.*?\*/", "", source, flags=re.DOTALL)
    source = re.sub(r"//[^\n]*", "", source)
    found = re.search(r"\benum\s+" + re.escape(enum_name) + r"\s*\{([^}]*)\}", source, re.DOTALL)
    if found is None:
        raise ValueError(f"Could not find enum {enum_name} in {path}")

    out: dict[str, int] = {}
    # Source entries are explicit integers, except aaHighestID (an implicit
    # sentinel, which is not an AA skill and should not be included).
    for part in found.group(1).split(","):
        entry = part.strip()
        match = re.fullmatch(r"([A-Za-z_]\w*)\s*=\s*(\d+)", entry)
        if match:
            out[match[1]] = int(match[2])
        elif entry and entry != "aaHighestID":
            raise ValueError(f"Unrecognized enum entry in {path}: {entry!r}")
    return out


def snake(name: str) -> str:
    """PascalCase to upper snake, keeping numeric-leading AA identifiers valid."""
    name = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", name)
    name = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", name)
    name = re.sub(r"([A-Za-z])([0-9])", r"\1_\2", name)
    name = re.sub(r"([0-9])([A-Za-z])", r"\1_\2", name)
    name = re.sub(r"[^0-9A-Za-z_]+", "_", name).upper()
    if name[0].isdigit():
        name = "AA_" + name
    return name


def make_source(innate: dict[str, int], aa: dict[str, int]) -> str:
    states = {key: innate[key] for key in ("InnateEnabled", "InnateDisabled")}
    size = innate["InnateSkillMax"]
    known_slots = {
        value: snake(name.removeprefix("Innate"))
        for name, value in innate.items()
        if name not in ("InnateEnabled", "InnateDisabled", "InnateSkillMax")
    }
    if not all(0 <= slot < size for slot in known_slots):
        raise ValueError("Innate slot out of bounds")
    lines = [
        '"""EQEmu innate slot IDs and AA rank IDs. AUTO-GENERATED; do not edit.\n',
        "From zone/client.h (eInnateSkill) and zone/aa.h (aaID).",
        '"""',
        "",
        "from enum import IntEnum",
        "",
        "",
        "class InnateSkill(IntEnum):",
        '    """Index of OP_PlayerProfile.innate_skills (25 entries)."""',
    ]
    for slot in range(size):
        name = known_slots.get(slot, f"UNKNOWN_{slot:02}")
        lines.append(f"    {name} = {slot}")
    lines.extend(
        [
            "",
            "",
            "class InnateState(IntEnum):",
            '    """Value stored at a particular innate skill slot."""',
            f'    ENABLED = {states["InnateEnabled"]}',
            f'    DISABLED = {states["InnateDisabled"]}',
            "",
            "",
            "class AASkill(IntEnum):",
            '    """EQEmu legacy aaID enumeration: named AA RANK IDs, not ability IDs."""',
        ]
    )
    used: dict[str, str] = {}
    for cpp_name, value in aa.items():
        if not cpp_name.startswith("aa"):
            raise ValueError(f"Unexpected AA identifier: {cpp_name}")
        name = snake(cpp_name[2:])
        if name in used:
            raise ValueError(f"AA name collision: {cpp_name} and {used[name]} -> {name}")
        used[name] = cpp_name
        lines.append(f"    {name} = {value}")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path("../.."))
    parser.add_argument("--output", type=Path, default=Path("eqclient4/structs/skill_enums.py"))
    args = parser.parse_args()
    innate = enum_constants(args.repo_root / "zone/client.h", "eInnateSkill")
    aa = enum_constants(args.repo_root / "zone/aa.h", "aaID")
    if not 0 < len(innate) < 30 or len(aa) < 1000:
        raise ValueError(f"Unexpected enum sizes: innate={len(innate)}, AA={len(aa)}")
    source = make_source(innate, aa)
    compile(source, str(args.output), "exec")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(source, encoding="utf-8")
    print(
        f"Wrote {len(aa)} AA rank IDs and {innate['InnateSkillMax']} innate slots to {args.output}"
    )


if __name__ == "__main__":
    main()
