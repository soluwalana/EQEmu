"""Say keywords and item counts from a zone's Perl and Lua quest scripts."""

from __future__ import annotations

import os
import re
from dataclasses import dataclass, field
from pathlib import Path

_SAY = re.compile(
    r"""\$text\s*=~\s*/([^/]+)/i|findi\(\s*["']([^"']+)["']\s*\)""",
    re.IGNORECASE,
)
_HANDIN = re.compile(r"(\d+)\s*=>\s*(\d+)")
_ITEMCOUNT = re.compile(r"\$itemcount\{(\d+)\}")
_LUA_ITEM = re.compile(r"item\d+\s*=\s*(\d+)")
_SUMMON = re.compile(r"(?:quest::summonitem|eq\.summon_item)\s*\(\s*(\d+)")
_EXIT_DOOR = re.compile(
    r"if\s*\(\s*\$(?:d_id|doorid)\s*==\s*(\d+)\s*\)\s*\{",
    re.IGNORECASE,
)
_ZONE_OUT = re.compile(r"(?:quest::movepc|quest::zone|quest::movezone|e\.self:MovePC)\b", re.IGNORECASE)


@dataclass
class Need:
    item_id: int
    count: int
    npc: str


@dataclass
class NpcScript:
    npc: str
    keywords: list[str] = field(default_factory=list)
    needs: list[Need] = field(default_factory=list)


@dataclass
class ZoneQuests:
    """Scripts and exit doors for one zone. The next zone replaces this whole object."""

    zone: str
    scripts: dict[str, NpcScript] = field(default_factory=dict)
    exits: list[int] = field(default_factory=list)


def npc_name(filename: str) -> str:
    stem = Path(filename).stem
    if stem.startswith("#"):
        stem = stem[1:]
    return stem.replace("_", " ")


def parse_script(text: str, filename: str) -> NpcScript:
    """Keywords from EVENT_SAY / event_say. Hand-in ids are needs. summonitem is a reward."""
    npc = npc_name(filename)
    keywords: list[str] = []
    seen: set[str] = set()
    for match in _SAY.finditer(text):
        word = (match.group(1) or match.group(2) or "").strip()
        key = word.lower()
        if word and key not in seen:
            seen.add(key)
            keywords.append(word)
    rewards = {int(match.group(1)) for match in _SUMMON.finditer(text)}
    needs: list[Need] = []

    def add(item_id: int, count: int) -> None:
        if item_id in rewards:
            return
        # Several counts of the same id (1 or 3 silk) are one need: the smallest count.
        for need in needs:
            if need.item_id == item_id:
                need.count = min(need.count, count)
                return
        needs.append(Need(item_id, count, npc))

    for match in _HANDIN.finditer(text):
        add(int(match.group(1)), int(match.group(2)))
    for match in _ITEMCOUNT.finditer(text):
        add(int(match.group(1)), 1)
    for match in _LUA_ITEM.finditer(text):
        add(int(match.group(1)), 1)
    return NpcScript(npc, keywords, needs)


def exit_doors(text: str) -> list[int]:
    """Door ids whose click handler zones the character out. The id comes from the script."""
    doors: list[int] = []
    for match in _EXIT_DOOR.finditer(text):
        body = _brace_block(text, match.end())
        if _ZONE_OUT.search(body):
            door_id = int(match.group(1))
            if door_id not in doors:
                doors.append(door_id)
    return doors


def _brace_block(text: str, start: int) -> str:
    depth = 1
    index = start
    while index < len(text) and depth:
        if text[index] == "{":
            depth += 1
        elif text[index] == "}":
            depth -= 1
        index += 1
    return text[start:index]


def load_zone(zone: str, root: str | None = None) -> ZoneQuests:
    """EQEMU_QUESTS/<zone>/. An empty tree means the agent only hails and fights."""
    quests = ZoneQuests(zone)
    base = root if root is not None else os.environ.get("EQEMU_QUESTS", "")
    if not base or not zone:
        return quests
    folder = Path(base) / zone
    if not folder.is_dir():
        return quests
    for path in sorted(folder.iterdir()):
        if path.suffix.lower() not in {".pl", ".lua"} or not path.is_file():
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        script = parse_script(text, path.name)
        quests.scripts[script.npc.lower()] = script
        for door_id in exit_doors(text):
            if door_id not in quests.exits:
                quests.exits.append(door_id)
    return quests


def all_needs(scripts: dict[str, NpcScript]) -> list[Need]:
    needs: list[Need] = []
    for script in scripts.values():
        needs.extend(script.needs)
    return needs
