"""Say keywords and item counts from a zone's Perl and Lua quest scripts.

build_graph walks those scripts. read_graph and load_graph read quest_graph.jsonl.
"""

from __future__ import annotations

import json
import os
import re
from dataclasses import dataclass, field
from pathlib import Path

from eqclient4.data.catalog import Catalog, named_items, load_catalog
from eqclient4.log import log
from eqclient4.nav.travel import ensure_zone_graph
from eqclient4.quests.speech_expr import iter_speech_calls

_SAY = re.compile(
    r"""\$text\s*=~\s*/([^/]+)/i|findi\(\s*["']([^"']+)["']\s*\)""",
    re.IGNORECASE,
)
_UPDATE = re.compile(r"updatetaskactivity\s*\(\s*(\d+)\s*,\s*(\d+)", re.IGNORECASE)
_HANDIN = re.compile(r"(\d+)\s*=>\s*(\d+)")
_ITEMCOUNT = re.compile(r"\$itemcount\{(\d+)\}")
_LUA_ITEM = re.compile(r"item\d+\s*=\s*(\d+)")
_EXIT_DOOR = re.compile(
    r"if\s*\(\s*\$(?:d_id|doorid)\s*==\s*(\d+)\s*\)\s*\{",
    re.IGNORECASE,
)
_ZONE_OUT = re.compile(
    r"(?:quest::movepc|quest::zone|quest::movezone|e\.self:MovePC)\b", re.IGNORECASE
)
_MOVEPC = re.compile(
    r"(?:quest::movepc|eq\.movepc|e\.self:MovePC)\s*\(\s*(\d+)",
    re.IGNORECASE,
)


@dataclass
class Need:
    item_id: int
    count: int
    npc: str


_GLOBAL = re.compile(
    r"(?:setglobal|eq\.set_global|eq\.target_global|target_global)\s*\(\s*[\"']([^\"']+)[\"']\s*,\s*[\"']?([^,\"']+)",
    re.IGNORECASE,
)
# Character zone flags (HasZoneFlag / set_zone_flag) — plane / GoD entry, distinct from qglobals.
_ZONE_FLAG_SET = re.compile(
    r"(?:quest::set_zone_flag|(?:e\.self:)?SetZoneFlag)\s*\(\s*(\d+)\s*\)",
    re.IGNORECASE,
)
_ZONE_FLAG_HAS = re.compile(
    r"(?:quest::has_zone_flag|(?:e\.self:)?HasZoneFlag)\s*\(\s*(\d+)\s*\)\s*(!=|==)\s*([01])",
    re.IGNORECASE,
)
_ZONE_FLAG_HAS_BARE = re.compile(
    r"(?:not\s+)?(?:quest::has_zone_flag|(?:e\.self:)?HasZoneFlag)\s*\(\s*(\d+)\s*\)",
    re.IGNORECASE,
)
_SPOKEN = re.compile(
    r"""(?:quest::say|quest::emote|e\.self:Say|e\.self:Emote|eq\.say)\s*\(\s*
        (?:"((?:\\.|[^"\\])*)"|'((?:\\.|[^'\\])*)')""",
    re.IGNORECASE | re.VERBOSE,
)

_FLAG_LUA = re.compile(
    r"""qglobals\[\s*["']([A-Za-z0-9_]+)["']\s*\]\s*(~=|==|>=|<=|>|<)\s*(nil|"?\d+"?)""",
)
_FLAG_PERL = re.compile(
    r"""\$qglobals\{\s*["']?([A-Za-z0-9_]+)["']?\s*\}\s*(==|>=|<=|>|<)\s*["']?(\d+)""",
)
_FLAG_DEFINED = re.compile(
    r"""(?P<neg>!\s*|\bnot\s+)?\bdefined\s*\(?\s*
        \$qglobals\{\s*["']?(?P<name>[A-Za-z0-9_]+)["']?\s*\}\s*\)?""",
    re.IGNORECASE | re.VERBOSE,
)
_FLAG_GET = re.compile(
    r"""GetGlobal\(\s*["']([A-Za-z0-9_]+)["']\s*\)\s*(==|>=|<=|>|<)\s*(undef|nil|\d+)""",
    re.IGNORECASE,
)
# EVENT_SAY $faction is the NPC's consider standing (1 ally … 9 scowls).
_FACTION_STANDING = re.compile(r"\$faction\s*(<=|>=|<|>|==)\s*(\d+)")
# Named GetCharacterFactionLevel / GetModCharacterFactionLevel comparisons.
_FACTION_GET_CMP = re.compile(
    r"""Get(?:Mod)?CharacterFactionLevel\s*\(\s*(\d+)\s*\)\s*(<=|>=|<|>|==)\s*(\d+)""",
    re.IGNORECASE,
)
_FACTION_ASSIGN = re.compile(
    r"""\$([A-Za-z_][A-Za-z0-9_]*)\s*=\s*\$client->Get(?:Mod)?CharacterFactionLevel\s*\(\s*(\d+)\s*\)""",
    re.IGNORECASE,
)
_FACTION_VAR_CMP = re.compile(r"\$([A-Za-z_][A-Za-z0-9_]*)\s*(<=|>=|<|>|==)\s*(\d+)")
# quest::faction(id, delta) / eq.faction — standing gained or lost on this step.
_FACTION_GAIN = re.compile(
    r"""(?:quest::faction|eq\.faction)\s*\(\s*["']?(\d+)["']?\s*,\s*(-?\d+)""",
    re.IGNORECASE,
)
_SUMMON_OPEN = re.compile(
    # quest::summonitem, eq.summon_item, e.other:SummonItem, or GetClientByName(...)->SummonItem.
    # The argument may be an id or ChooseRandom(...).
    r"""(?:quest::summonitem|eq\.summon_item|(?::|->)SummonItem)\s*\(""",
    re.IGNORECASE,
)
_QUEST_REWARD = re.compile(r"(?:QuestReward|quest::questreward)\s*\(", re.IGNORECASE)
_REWARD_ITEM = re.compile(r"itemid\s*=\s*(\d+)", re.IGNORECASE)
_HASITEM = re.compile(r"check_hasitem\s*\([^,]+,\s*(\d+)\s*\)", re.IGNORECASE)
_HELD_CALL = re.compile(r"HasItem\s*\(\s*(\d+)\s*\)", re.IGNORECASE)
_GROUND = re.compile(r"create_ground_object\s*\(\s*(\d+)", re.IGNORECASE)
_LOOT_ID = re.compile(r"GetID\s*\(\s*\)\s*==\s*(\d+)", re.IGNORECASE)
_SPAWN = re.compile(
    r"(?<![\w])(?:unique_spawn|spawn2|spawn)\s*\(\s*\$?(\d+|[A-Za-z_][A-Za-z0-9_]*)",
    re.IGNORECASE,
)
_LOCAL = re.compile(
    r"(?m)^[ \t]*(?:local[ \t]+|my[ \t]+)?\$?([A-Za-z_][A-Za-z0-9_]*)[ \t]*=[ \t]*(\d+)\b"
)
_CHOOSE = re.compile(r"ChooseRandom\s*\(([^)]*)\)", re.IGNORECASE)
_ADDITEM = re.compile(r"AddItem\s*\(\s*(\d+)", re.IGNORECASE)
_NPC_TYPE_ID = re.compile(r"GetNPCTypeID\s*\(\s*\)\s*==\s*(\d+)", re.IGNORECASE)
_SET_TIMER = re.compile(r"(?:set_timer|settimer)\s*\(\s*[\"']([^\"']+)[\"']", re.IGNORECASE)
_TIMER_IS = re.compile(r"""(?:e\.timer\s*==\s*|\$timer\s*eq\s*)["']([^"']+)["']""", re.IGNORECASE)
_COIN = re.compile(r"\b(platinum|gold|silver|copper)\s*(?:=>|=)\s*(\d+)", re.IGNORECASE)
_COIN_CMP = re.compile(
    r"(?:\$|\b)(platinum|gold|silver|copper)\b\s*(?:>=|>)\s*(\d+)",
    re.IGNORECASE,
)
_RECIPE = re.compile(r"recipe_id\s*==\s*(\d+)", re.IGNORECASE)
_CLASS_CALL = re.compile(r"""Class\(\)\s*==\s*["']([A-Za-z ]+)["']""", re.IGNORECASE)
_OR = re.compile(r"\|\||\bor\b", re.IGNORECASE)
_AND = re.compile(r"&&|\band\b", re.IGNORECASE)
_TURN = re.compile(
    r"(?:check_handin|check_turn_in|takeitems|take_items|\bhandin)\s*\(",
    re.IGNORECASE,
)
# Lua eq.handin({[28051] = 1}) or {[28051]=1,[28052]=1}
_LUA_TABLE_ITEM = re.compile(r"\[\s*(\d+)\s*\]\s*=\s*(\d+)")
# A local set in the hand-in branch and checked later: morechampagne = 1 then if morechampagne == 1
_LOCAL_SET = re.compile(r"\b([A-Za-z_][A-Za-z0-9_]*)\s*=\s*1\b")
_LOCAL_IF = re.compile(
    r"\bif\s*\(\s*([A-Za-z_][A-Za-z0-9_]*)\s*==\s*1\s*\)",
    re.IGNORECASE,
)
_CLASS_EQ = re.compile(r"\$class\s*==\s*(\d+)|\$class\s*eq\s*[\"']([A-Za-z ]+)[\"']", re.IGNORECASE)
_CLASS_IDS = {
    "warrior": 1,
    "cleric": 2,
    "paladin": 3,
    "ranger": 4,
    "shadow knight": 5,
    "shadowknight": 5,
    "druid": 6,
    "monk": 7,
    "bard": 8,
    "rogue": 9,
    "shaman": 10,
    "necromancer": 11,
    "wizard": 12,
    "magician": 13,
    "enchanter": 14,
    "beastlord": 15,
    "berserker": 16,
}


@dataclass
class QuestNode:
    """One say or hand-in, after the words and flags that have to come first."""

    npc: str
    kind: str
    word: str = ""
    item_id: int = 0
    requires: tuple[str, ...] = ()
    grants: tuple[str, ...] = ()
    zone_id: int = 0
    classes: tuple[int, ...] = ()
    zone: str = ""
    text: str = ""


@dataclass
class NpcScript:
    npc: str
    keywords: list[str] = field(default_factory=list)
    needs: list[Need] = field(default_factory=list)
    advances: dict[str, set[tuple[int, int]]] = field(default_factory=dict)
    delivers: dict[int, set[tuple[int, int]]] = field(default_factory=dict)


@dataclass
class ZoneQuests:
    """Scripts and exit doors for one zone. The next zone replaces this whole object."""

    zone: str
    scripts: dict[str, NpcScript] = field(default_factory=dict)
    exits: list[int] = field(default_factory=list)
    destinations: dict[int, list[int]] = field(default_factory=dict)
    chains: dict[str, list["QuestNode"]] = field(default_factory=dict)


def npc_name(filename: str, catalog: Catalog | None = None) -> str:
    stem = Path(filename).stem
    if stem.startswith("#"):
        stem = stem[1:]
    # citymist/90005.lua is a_black_reaver in the dump.
    if stem.isdigit() and catalog:
        named = catalog.npc_names.get(int(stem))
        if named:
            return named
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
    rewards = {item_id for _pos, item_id in _summon_items(text)}
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
    advances: dict[str, set[tuple[int, int]]] = {}
    delivers: dict[int, set[tuple[int, int]]] = {}
    for match in _HANDIN.finditer(text):
        brace = text.find("{", match.end())
        block = _brace_block(text, brace + 1) if brace >= 0 else ""
        for task_id, activity_id in _UPDATE.findall(block):
            delivers.setdefault(int(match.group(1)), set()).add((int(task_id), int(activity_id)))
    for match in _SAY.finditer(text):
        word = (match.group(1) or match.group(2) or "").strip().lower()
        if not word:
            continue
        brace = text.find("{", match.end())
        block = _brace_block(text, brace + 1) if brace >= 0 else ""
        for task_id, activity_id in _UPDATE.findall(block):
            advances.setdefault(word, set()).add((int(task_id), int(activity_id)))
    return NpcScript(npc, keywords, needs, advances, delivers)


def parse_chain(text: str, filename: str, zone: str = "") -> list[QuestNode]:
    """Say and hand-in steps in file order. Each one waits on the step before it."""
    npc = npc_name(filename)
    home = zone.lower()
    nodes: list[QuestNode] = []
    previous = ""
    for match in _SAY.finditer(text):
        word = (match.group(1) or match.group(2) or "").strip()
        if not word:
            continue
        cond, block = _branch_at(text, match.start())
        if not block:
            block = _following(text, match.end())
        nodes.append(
            QuestNode(
                npc,
                "say",
                word=word,
                requires=(previous,) if previous else (),
                grants=tuple(name for name, _value in _all_flag_sets(block)),
                zone_id=_zone_of(block),
                classes=_class_gate(cond + "\n" + block),
                zone=home,
                text=_spoken(block),
            )
        )
        previous = word.lower()
    for match in _HANDIN.finditer(text):
        cond, block = _branch_at(text, match.start())
        if not block:
            block = _following(text, match.end())
        nodes.append(
            QuestNode(
                npc,
                "hand",
                item_id=int(match.group(1)),
                requires=(previous,) if previous else (),
                grants=tuple(name for name, _value in _all_flag_sets(block)),
                zone_id=_zone_of(block),
                classes=_class_gate(cond + "\n" + block),
                zone=home,
            )
        )
    return nodes


def next_node(
    nodes: list[QuestNode],
    said: set[str],
    flags: set[str] | dict[str, int],
    class_id: int,
    items: set[int],
) -> QuestNode | None:
    """The first step this class can do with what he has already said and is holding."""
    flag_names = set(flags) if not isinstance(flags, dict) else set(flags)
    for node in nodes:
        if node.classes and class_id not in node.classes:
            continue
        if any(req not in said and req not in flag_names for req in node.requires):
            continue
        if node.kind == "say" and node.word.lower() in said:
            continue
        if node.kind == "hand" and node.item_id not in items:
            continue
        return node
    return None


def _skip_quote(text: str, start: int) -> int:
    quote = text[start]
    index = start + 1
    limit = len(text)
    while index < limit:
        if text[index] == "\\":
            index += 2
            continue
        if text[index] == quote:
            return index + 1
        index += 1
    return limit


def _compute_branches(
    text: str,
) -> tuple[list[tuple[int, int, int, int]], list[tuple[str, int, int]]]:
    """One span per if, elsif, and elseif: condition start, condition end, body start, body end.

    Perl opens the body with a brace. Lua opens it with then and closes a branch at
    elseif, else, or end. A brace inside a call is not a body.
    """
    branches: list[tuple[int, int, int, int]] = []
    functions: list[tuple[str, int, int]] = []
    stack: list[dict] = []
    paren = 0
    index = 0
    limit = len(text)
    # A Perl comment starts at #. Lua uses # as the length operator, so only Perl gets every #.
    perl = ("quest::" in text or "plugin::" in text or "$qglobals" in text or "$text" in text) and (
        "function event_" not in text
    )

    def close_branch(at: int) -> None:
        frame = stack.pop()
        if frame["kind"] == "if" and frame["body"] >= 0:
            branches.append((frame["cond"], frame["cond_hi"], frame["body"], at))
        elif frame["kind"] == "function" and frame.get("fname"):
            functions.append((frame["fname"], frame["body"], at))

    while index < limit:
        char = text[index]
        if perl and char == "/" and text[max(0, index - 12):index].rstrip().endswith(("=~", "!~")):
            # Skip regex bodies: words such as "do" or "end" are not syntax.
            pos = index + 1
            while pos < limit:
                if text[pos] == "\\":
                    pos += 2
                elif text[pos] == "/":
                    pos += 1
                    while pos < limit and text[pos].isalpha():
                        pos += 1
                    break
                else:
                    pos += 1
            index = pos
            continue
        if char in "\"'":
            index = _skip_quote(text, index)
            continue
        if text.startswith("--[[", index):
            end = text.find("]]", index + 4)
            index = limit if end < 0 else end + 2
            continue
        if text.startswith("--", index):
            end = text.find("\n", index)
            index = limit if end < 0 else end + 1
            continue
        if text.startswith("[[", index):
            end = text.find("]]", index + 2)
            index = limit if end < 0 else end + 2
            continue
        if char == "#" and (perl or (index + 1 < limit and text[index + 1] in " \t")):
            end = text.find("\n", index)
            index = limit if end < 0 else end + 1
            continue
        if char == "(":
            frame = stack[-1] if stack else None
            if frame and frame.get("await_name"):
                frame["await_name"] = False
            paren += 1
            index += 1
            continue
        if char == ")":
            paren = max(0, paren - 1)
            frame = stack[-1] if stack else None
            # A callback written inside ForeachHateList( keeps the caller's parenthesis open.
            # The function body is not inside that call, so its if/then pairs parse on their own.
            if (
                frame
                and frame.get("kind") == "function"
                and frame.get("closer") != "brace"
                and not frame.get("args_done")
                and paren == frame.get("paren_floor", -1)
            ):
                frame["args_done"] = True
                paren = 0
            index += 1
            continue
        if char == "{":
            frame = stack[-1] if stack else None
            if paren == 0 and frame and frame["kind"] == "function" and frame["body"] < 0:
                frame["body"] = index + 1
                frame["closer"] = "brace"
                frame["braces"] = 1
            elif paren == 0 and frame and frame["kind"] == "if" and frame["body"] < 0:
                frame["body"] = index + 1
                frame["cond_hi"] = index
                frame["closer"] = "brace"
                frame["braces"] = 1
            elif frame and frame.get("closer") == "brace":
                frame["braces"] += 1
            index += 1
            continue
        if char == "}":
            frame = stack[-1] if stack else None
            if frame and frame.get("closer") == "brace":
                frame["braces"] -= 1
                if frame["braces"] <= 0:
                    close_branch(index)
            index += 1
            continue
        if char.isalpha() or char == "_":
            end = index + 1
            while end < limit and (text[end].isalnum() or text[end] == "_"):
                end += 1
            word = text[index:end].lower()
            frame = stack[-1] if stack else None
            if frame and frame.get("await_name"):
                frame["fname"] = word
                frame["await_name"] = False
                index = end
                continue
            if word in {"elseif", "elsif"}:
                frame = stack[-1] if stack else None
                if (
                    frame
                    and frame["kind"] == "if"
                    and frame["body"] >= 0
                    and frame.get("closer") != "brace"
                ):
                    close_branch(index)
                stack.append(
                    {
                        "kind": "if",
                        "cond": end,
                        "cond_hi": end,
                        "body": -1,
                        "closer": "",
                        "braces": 0,
                    }
                )
            elif word == "if":
                stack.append(
                    {
                        "kind": "if",
                        "cond": end,
                        "cond_hi": end,
                        "body": -1,
                        "closer": "",
                        "braces": 0,
                    }
                )
            elif (
                word == "then"
                and paren == 0
                and stack
                and stack[-1]["kind"] == "if"
                and stack[-1]["body"] < 0
            ):
                stack[-1]["body"] = end
                stack[-1]["cond_hi"] = index
                stack[-1]["closer"] = "end"
            elif word == "else":
                frame = stack[-1] if stack else None
                if (
                    frame
                    and frame["kind"] == "if"
                    and frame["body"] >= 0
                    and frame.get("closer") != "brace"
                ):
                    close_branch(index)
                    stack.append(
                        {
                            "kind": "if",
                            "cond": end,
                            "cond_hi": end,
                            "body": end,
                            "closer": "end",
                            "braces": 0,
                        }
                    )
                else:
                    stack.append(
                        {
                            "kind": "if",
                            "cond": end,
                            "cond_hi": end,
                            "body": -1,
                            "closer": "",
                            "braces": 0,
                        }
                    )
            elif word == "end":
                if stack and stack[-1].get("closer") != "brace":
                    frame = stack.pop()
                    if frame["kind"] == "function":
                        if frame.get("args_done"):
                            paren = frame.get("paren_floor", 0)
                        if frame.get("fname"):
                            functions.append((frame["fname"], frame["body"], index))
                    if frame["kind"] == "if" and frame["body"] >= 0:
                        branches.append((frame["cond"], frame["cond_hi"], frame["body"], index))
            elif word == "sub" and paren == 0:
                stack.append(
                    {
                        "kind": "function",
                        "cond": end,
                        "cond_hi": end,
                        "body": -1,
                        "closer": "",
                        "braces": 0,
                        "fname": "",
                        "await_name": True,
                    }
                )
            elif word in {"while", "for", "function", "repeat"}:
                stack.append(
                    {
                        "kind": word,
                        "cond": end,
                        "cond_hi": end,
                        "body": -1 if word in {"while", "for"} else end,
                        "closer": "until" if word == "repeat" else "end",
                        "braces": 0,
                        "fname": "",
                        "await_name": word == "function",
                        "paren_floor": paren,
                        "args_done": False,
                    }
                )
            elif word == "do":
                frame = stack[-1] if stack else None
                if frame and frame["kind"] in {"while", "for"} and frame["body"] < 0:
                    frame["body"] = end
                    frame["closer"] = "end"
                else:
                    stack.append(
                        {
                            "kind": "do",
                            "cond": end,
                            "cond_hi": end,
                            "body": end,
                            "closer": "end",
                            "braces": 0,
                        }
                    )
            elif word == "until" and stack and stack[-1]["kind"] == "repeat":
                stack.pop()
            index = end
            continue
        index += 1
    return branches, functions


class _BranchIndex:
    def __init__(self) -> None:
        self.source: str | None = None
        self.found: list[tuple[int, int, int, int]] = []
        self.functions: list[tuple[str, int, int]] = []

    def __call__(self, text: str) -> list[tuple[int, int, int, int]]:
        if self.source is text:
            return self.found
        found, functions = _compute_branches(text)
        self.source = text
        self.found = found
        self.functions = functions
        return found


_branch_index = _BranchIndex()


def _functions(text: str) -> list[tuple[str, int, int]]:
    _branch_index(text)
    return _branch_index.functions


def _chosen_branch(text: str, pos: int) -> tuple[int, int, int, int] | None:
    found = [branch for branch in _branch_index(text) if branch[0] <= pos < branch[3]]
    if not found:
        return None
    gated = [branch for branch in found if branch[0] <= pos < branch[1]]
    return min(gated or found, key=lambda branch: branch[3] - branch[0])


def _branch_at(text: str, pos: int) -> tuple[str, str]:
    """Condition and body of the if that holds this offset. Lua then/end and Perl braces both count."""
    span = _chosen_branch(text, pos)
    if not span:
        return "", ""
    cond_lo, cond_hi, body_lo, body_hi = span
    return text[cond_lo:cond_hi], text[body_lo:body_hi]


def _following(text: str, end: int) -> str:
    _cond, body = _branch_at(text, max(0, end - 1))
    if body:
        return body
    brace = text.find("{", end)
    if brace < 0 or brace - end > 200:
        return ""
    return _brace_block(text, brace + 1)


def _zone_of(block: str) -> int:
    found = _MOVEPC.findall(block)
    return int(found[0]) if found else 0


def _spoken(block: str) -> str:
    return next((event["text"] for event in iter_speech_calls(block)), "")


def _speech_events(text: str, span: tuple[int, int, int, int]) -> list[dict]:
    """Full Say/Emote expressions, including nested saylink labels and guards."""
    body_lo, body_hi = span[2], span[3]
    branches = _branch_index(text)
    events = []
    for event in iter_speech_calls(text, body_lo, body_hi):
        at = event["offset"]
        nested = sorted(
            (b for b in branches
             if body_lo <= b[0] and b[0] <= at < b[3] and b != span),
            key=lambda b: b[0],
        )
        events.append({**event, "guards": [text[b[0]:b[1]].strip() for b in nested]})
    return events


_OPTION_LIST = re.compile(
    r"(?P<first>\b[\w]+(?:\s+(?:of|the|a|an|to|for|in|on|with)\s+[\w]+)+)"
    r"(?P<rest>(?:\s*,\s*(?!(?:or|and)\b)[\w]+)+(?:\s*,?\s*(?:or|and)\s+[\w]+)?)",
    re.IGNORECASE,
)


_QUERY_PREFIXES = (
    ("what",), ("who",), ("where",), ("which",),
    ("what", "is"), ("what", "are"), ("tell", "me", "about"),
    ("a",), ("an",), ("the",),
)


def _lex_tokens(value: str) -> list[str]:
    return re.findall(r"[\w]+", value.casefold().replace("_", " "))


def _lex_variants(token: str) -> set[str]:
    """Small inflection set for singular/plural player triggers.

    This intentionally does not do arbitrary stemming or substring matches.
    """
    variants = {token}
    if len(token) > 4:
        if token.endswith("ies") and len(token) > 5:
            variants.add(token[:-3] + "y")
        if token.endswith("es") and token[-3:-2] in {"s", "x", "z"}:
            variants.add(token[:-2])
        if token.endswith("s") and not token.endswith("ss"):
            variants.add(token[:-1])
    return variants


def _lex_equiv(a: str, b: str) -> bool:
    return bool(_lex_variants(a) & _lex_variants(b))


def _lex_sequence(needle: list[str], haystack: list[str]) -> bool:
    return any(
        all(_lex_equiv(a, b) for a, b in zip(needle, haystack[start:start + len(needle)]))
        for start in range(len(haystack) - len(needle) + 1)
    )


def _lex_queries(value: str) -> list[list[str]]:
    words = _lex_tokens(value)
    candidates = [words]
    for prefix in _QUERY_PREFIXES:
        if words[:len(prefix)] == list(prefix) and len(words) > len(prefix):
            candidates.append(words[len(prefix):])
    return candidates


def _lex_mentioned(phrase: str, replies: list[str]) -> bool:
    """Match the player's expression to spoken offers, without lore inference.

    Covers leading player-question words, inflected plural terms, and shared
    prefixes in comma-separated lists. Checks any earlier reply, not just an
    adjacent sibling branch.
    """
    queries = _lex_queries(phrase)
    if not queries or not queries[0]:
        return False
    for reply in replies:
        tokens = _lex_tokens(reply)
        if any(_lex_sequence(query, tokens) for query in queries):
            return True
        for match in _OPTION_LIST.finditer(reply):
            first = _lex_tokens(match.group("first"))
            if len(first) < 3:
                continue
            for option in _lex_tokens(match.group("rest")):
                if option in {"and", "or"}:
                    continue
                for start in range(len(first) - 1):
                    expansion = first[start:-1] + [option]
                    if any(len(query) == len(expansion) and
                           all(_lex_equiv(a, b) for a, b in zip(query, expansion))
                           for query in queries):
                        return True
    return False


def _speech_mentions(word: str, speech: list[dict]) -> bool:
    # Link *targets* are executable player inputs, even when the visible
    # label differs. Also recognize naturally phrased visible options.
    return (any(_lex_mentioned(word, [str(link.get("target") or "")])
                for event in speech for link in event.get("links", ()))
            or _lex_mentioned(word, [str(event.get("text") or "") for event in speech]))


def _non_say_speech(text: str) -> list[dict]:
    """Quest dialogue unlocked by item hand-ins, not by player /say.

    Preserve event names and guards; do not invent a preceding SAY turn.
    Restrict to player-facing item/trade events, rather than all NPC events.
    """
    found = []
    branches = _branch_index(text)
    for name, lo, hi in _functions(text):
        event = name.lower()
        if event not in {"event_item", "event_trade"}:
            continue
        for speech in iter_speech_calls(text, lo, hi):
            at = speech["offset"]
            ancestry = sorted(
                (branch for branch in branches
                 if lo <= branch[0] and branch[0] <= at < branch[3]),
                key=lambda branch: (branch[0], -branch[3]),
            )
            found.append({
                "event": event,
                "channel": speech["channel"],
                "text": speech["text"],
                "links": speech["links"],
                "guards": [text[b[0]:b[1]].strip() for b in ancestry],
                "order": at,
            })
    return found


def dialogue_chains(text: str, filename: str, zone: str) -> list[dict]:
    """Extract complete EVENT_SAY conversations with response-grounded transitions.

    Script order is a potential dialogue path, NOT proof that the player has
    heard a particular keyword. Explicit and lore-based cues are annotated;
    other transitions remain candidates for downstream semantic evaluation.
    """
    npc = npc_name(filename)
    home = zone.lower()
    source = f"{home}/{npc.lower()}"
    branches = _branch_index(text)
    context_speech = _non_say_speech(text)
    chains = []
    for function_name, lo, hi in _functions(text):
        if function_name.lower() != "event_say":
            continue
        turns = []
        for match in _SAY.finditer(text, lo, hi):
            input_text = (match.group(1) or match.group(2) or "").strip()
            if not input_text:
                continue
            span = _chosen_branch(text, match.start())
            if not span or not (lo <= span[0] and span[3] <= hi):
                continue
            # All ancestor conditions apply, including the external faction gate.
            parents = sorted(
                (b for b in branches if lo <= b[0] <= span[0]
                 and span[3] <= b[3] and b != span),
                key=lambda b: (b[0], -b[3]),
            )
            guards = [text[b[0]:b[1]].strip() for b in parents]
            guards.append(text[span[0]:span[1]].strip())
            speech = _speech_events(text, span)
            # Restrict effects to this SAY branch, including any nested guards.
            branch_events = _body_events(text[span[2]:span[3]], span[2])
            effects = [dict(event) for _at, event in branch_events
                       if event['rel'] in {'gives', 'sets', 'spawns'}]
            turns.append({
                'input': input_text,
                'source': f'{source}#{input_text.lower()}',
                'reply': [{k: event[k] for k in ('channel', 'text', 'guards', 'links')}
                          for event in speech],
                'guards': guards,
                'effects': effects,
                'order': match.start(),
            })
        if not turns:
            continue
        transitions = []
        # for earlier, later in zip(turns, turns[1:]):
        #     utterances = [event['text'] for event in earlier['reply']]
        #     target = later['input'].lower()
        #     basis = 'conversation_sequence'
        #     evidence = ''
        #     for utterance in utterances:
        #         if re.search(r'(?<!\w)' + re.escape(target) + r'(?!\w)', utterance, re.I):
        #             basis = 'explicit_mention'
        #             evidence = utterance
        #             break
        #     transitions.append({
        #         'from': earlier['input'], 'to': later['input'],
        #         'basis': basis, 'evidence': evidence,
        #     })

        # A SAY handler is a set of possible choices, not a linear conversation.
        # Search all earlier replies for an explicit cue. A later sibling is
        # often prompted by an earlier shared parent (hail -> three tests).
        for index, target in enumerate(turns):
            found = False

            for parent_index, parent in enumerate(turns):
                if parent_index == index:
                    continue
                if _speech_mentions(target['input'], parent['reply']):
                    transitions.append({
                        'from': parent['input'], 'to': target['input'],
                        'basis': 'explicit_mention',
                        'evidence': '\n'.join(r['text'] for r in parent['reply']),
                        'source_order': 'earlier' if parent_index < index else 'later',
                    })
                    found = True

            # Event-triggered dialogue (a completed item hand-in, for example)
            # can supply the first choice. This is not a SAY-to-SAY edge.
            for speech in context_speech:
                if _speech_mentions(target['input'], [speech]):
                    transitions.append({
                        'from': speech['event'], 'to': target['input'],
                        'basis': 'external_event_mention',
                        'event': speech['event'],
                        'guards': speech['guards'],
                        'evidence': speech['text'],
                    })
                    found = True

            if not found and index:
                transitions.append({
                    'from': turns[index - 1]['input'], 'to': target['input'],
                    'basis': 'conversation_sequence', 'evidence': '',
                })

        chains.append({
            'kind': 'dialogue', 'zone': home, 'npc': npc,
            'source': source, 'handler': function_name,
            'turns': turns, 'transitions': transitions,
            'context_speech': context_speech,
        })
    return chains


def _zoneflag_name(zone_id: int | str) -> str:
    return f"zoneflag:{int(zone_id)}"


def _flags(text: str) -> list[tuple[str, str]]:
    """Quest identifier and the comparison, such as cleric_epic >= 3."""
    found: list[tuple[str, str]] = []
    for name, op, value in _FLAG_LUA.findall(text):
        if value == "nil":
            if op == "~=":
                found.append((name, "set"))
            elif op == "==":
                found.append((name, "unset"))
            continue
        found.append((name, f"{op}{value.strip(chr(34))}"))
    for name, op, value in _FLAG_PERL.findall(text):
        found.append((name, f"{op}{value}"))

    for match in _FLAG_DEFINED.finditer(text):
        found.append((
            match.group("name"),
            "unset" if match.group("neg") else "set",
        ))
    for name, op, value in _FLAG_GET.findall(text):
        if value.lower() in {"undef", "nil"}:
            if op == "==":
                found.append((name, "unset"))
            continue
        found.append((name, f"{op}{value}"))
    for zone_id, op, value in _ZONE_FLAG_HAS.findall(text):
        name = _zoneflag_name(zone_id)
        if (op == "==" and value == "1") or (op == "!=" and value == "0"):
            found.append((name, "set"))
        elif (op == "!=" and value == "1") or (op == "==" and value == "0"):
            found.append((name, "unset"))
    # Bare HasZoneFlag / not HasZoneFlag when no ==/!= was matched for that id.
    seen_zf = {name for name, _at in found if name.startswith("zoneflag:")}
    for match in _ZONE_FLAG_HAS_BARE.finditer(text):
        name = _zoneflag_name(match.group(1))
        if name in seen_zf:
            continue
        negated = match.group(0).lower().lstrip().startswith("not")
        found.append((name, "unset" if negated else "set"))
        seen_zf.add(name)

    return list(dict.fromkeys(found))


def _zone_flag_sets(text: str) -> list[tuple[str, str]]:
    """set_zone_flag(id) → (zoneflag:id, '1')."""
    return [(_zoneflag_name(zone_id), "1") for zone_id in _ZONE_FLAG_SET.findall(text)]


def _all_flag_sets(text: str) -> list[tuple[str, str]]:
    """qglobal set_global plus character set_zone_flag writes."""
    return list(_GLOBAL.findall(text)) + _zone_flag_sets(text)


def _faction_needs(gate: str, script: str | None = None) -> list[tuple[str, str]]:
    """Faction gates on a branch: ('primary', '<=3') or ('404', '>=43').

    Assignments often sit above the `if` (full `script`); comparisons live in `gate`.
    """
    found: list[tuple[str, str]] = []
    seen: set[tuple[str, str]] = set()
    assign_src = script if script is not None else gate
    assigned = {
        name.lower(): faction_id for name, faction_id in _FACTION_ASSIGN.findall(assign_src)
    }
    # Bare $faction is NPC consider standing unless assigned from GetCharacterFactionLevel.
    standing_id = assigned.get("faction", "primary")
    for op, value in _FACTION_STANDING.findall(gate):
        key = (standing_id, f"{op}{value}")
        if key not in seen:
            seen.add(key)
            found.append(key)
    for faction_id, op, value in _FACTION_GET_CMP.findall(gate):
        key = (faction_id, f"{op}{value}")
        if key not in seen:
            seen.add(key)
            found.append(key)
    for name, op, value in _FACTION_VAR_CMP.findall(gate):
        if name.lower() == "faction":
            continue  # handled by _FACTION_STANDING
        faction_id = assigned.get(name.lower())
        if not faction_id:
            continue
        key = (faction_id, f"{op}{value}")
        if key not in seen:
            seen.add(key)
            found.append(key)
    return found


def _faction_gains(text: str) -> list[tuple[str, int]]:
    """quest::faction(id, delta) rewards on this branch."""
    found: list[tuple[str, int]] = []
    seen: set[tuple[str, int]] = set()
    for faction_id, delta in _FACTION_GAIN.findall(text):
        key = (faction_id, int(delta))
        if key not in seen:
            seen.add(key)
            found.append(key)
    return found


def _emit_faction_needs(
    edges: list[dict],
    source: str,
    gate: str,
    group: str = "",
    script: str | None = None,
) -> None:
    for faction_id, at in _faction_needs(gate, script):
        edge = {
            "kind": "edge",
            "rel": "needs",
            "from": source,
            "to": f"faction:{faction_id}",
            "faction": faction_id,
            "at": at,
        }
        if group:
            edge["group"] = group
        edges.append(edge)


def _emit_faction_gains(edges: list[dict], source: str, text: str, group: str = "") -> None:
    for faction_id, delta in _faction_gains(text):
        edge = {
            "kind": "edge",
            "rel": "sets",
            "from": source,
            "to": f"faction:{faction_id}",
            "faction": faction_id,
            "value": delta,
        }
        if group:
            edge["group"] = group
        edges.append(edge)


def _quest_reward_items(body: str) -> list[int]:
    """Named `itemid =`, or the fifth number of QuestReward(self, copper, silver, gold, platinum, item, exp)."""
    named = [int(item) for item in _REWARD_ITEM.findall(body)]
    if named:
        return named
    numbers = [int(piece) for piece in re.findall(r"\d+", body)]
    if len(numbers) >= 5 and numbers[4] > 0:
        return [numbers[4]]
    return []


def _summon_ids(body: str) -> list[int]:
    """Item ids a summon call hands over. ChooseRandom is every distinct id in the list."""
    groups = _CHOOSE.findall(body)
    if groups:
        found: list[int] = []
        seen: set[int] = set()
        for group in groups:
            for number in re.findall(r"\d+", group):
                item_id = int(number)
                if item_id not in seen:
                    seen.add(item_id)
                    found.append(item_id)
        return found
    direct = re.match(r"""\s*["']?(\d+)["']?""", body)
    if direct:
        return [int(direct.group(1))]
    return []


def _summon_items(text: str) -> list[tuple[int, int]]:
    """(call offset, item id) for each summoned item."""
    found: list[tuple[int, int]] = []
    for match in _SUMMON_OPEN.finditer(text):
        body, _end = _paren(text, match.end() - 1)
        for item_id in _summon_ids(body):
            found.append((match.start(), item_id))
    return found


def _reward_ids(block: str) -> list[int]:
    found = [item_id for _pos, item_id in _summon_items(block)]
    for match in _QUEST_REWARD.finditer(block):
        body, _end = _paren(block, match.end() - 1)
        found.extend(_quest_reward_items(body))
    return found


def _item_gates(block: str) -> list[tuple[int, str]]:
    """Items a branch requires him to already hold. An or-list is one choice, not every item."""
    matches = list(_HASITEM.finditer(block)) + list(_HELD_CALL.finditer(block))
    matches.sort(key=lambda match: match.start())
    if not matches:
        return []
    snippet = block[matches[0].start() : matches[-1].end()]
    op = "or" if len(matches) > 1 and _OR.search(snippet) and not _AND.search(snippet) else ""
    return [(int(match.group(1)), op) for match in matches]


def _paren(text: str, open_at: int) -> tuple[str, int]:
    depth = 0
    index = open_at
    while index < len(text):
        if text[index] == "(":
            depth += 1
        elif text[index] == ")":
            depth -= 1
            if depth == 0:
                return text[open_at + 1 : index], index + 1
        index += 1
    return "", open_at


def _after_call(text: str, end: int) -> str:
    window = text[end : end + 80]
    if "{" in window:
        return _following(text, end)
    stop = text.find("\nend", end)
    if stop < 0:
        return text[end : end + 400]
    return text[end:stop]


def _comment_name(line: str) -> str:
    """The NPC name a script leaves at the end of a spawn line."""
    comment = ""
    if "--" in line:
        comment = line.split("--", 1)[1]
    else:
        mark = re.search(r"(?:;|\s)#\s*(.*)$", line)
        if mark:
            comment = mark.group(1)
    comment = re.sub(r"^NPC:\s*", "", comment.strip(), flags=re.IGNORECASE).lstrip("#").strip()
    # Scripts often write "#Innoruuk (186107) real" — keep the name, drop the id note.
    comment = re.sub(r"\s*\(\d+\)\s*.*$", "", comment).strip()
    comment = comment.replace("_", " ")
    if not comment or not comment[0].isalpha():
        return ""
    return comment


def _numeric_locals(text: str) -> dict[str, int]:
    """A name assigned one integer in this script. A spawn may pass that name."""
    found: dict[str, set[int]] = {}
    for match in _LOCAL.finditer(text):
        found.setdefault(match.group(1).lower(), set()).add(int(match.group(2)))
    return {name: next(iter(values)) for name, values in found.items() if len(values) == 1}


class _SpawnCalls:
    def __init__(self) -> None:
        self.constants: dict[str, int] = {}

    def __call__(self, snippet: str) -> list[tuple[int, str]]:
        constants = self.constants
        found: list[tuple[int, str]] = []
        seen: set[int] = set()
        for match in _SPAWN.finditer(snippet):
            token = match.group(1)
            if token.isdigit():
                npc_type = int(token)
            else:
                found_id = constants.get(token.lower())
                if found_id is None:
                    continue
                npc_type = found_id
            line_end = snippet.find("\n", match.start())
            line = snippet[match.start() : line_end if line_end >= 0 else len(snippet)]
            seen.add(npc_type)
            found.append((npc_type, _comment_name(line)))
        if re.search(r"(?<![\w])(?:unique_spawn|spawn2|spawn)\s*\(", snippet, re.IGNORECASE):
            for group in _CHOOSE.findall(snippet):
                for npc in re.findall(r"\d{3,}", group):
                    npc_type = int(npc)
                    if npc_type not in seen:
                        seen.add(npc_type)
                        found.append((npc_type, ""))
        return found


_spawn_calls = _SpawnCalls()


def _without(text: str, start: int, stop: int, holes: list[tuple[int, int]]) -> str:
    """The branch body, with nested branches blanked so their spawns stay on their own step."""
    chars = list(text[start:stop])
    for lo, hi in holes:
        for index in range(max(lo, start) - start, min(hi, stop) - start):
            chars[index] = " "
    return "".join(chars)


class _TimerSpawns:
    """NPCs a named timer creates. The say or hand-in that starts the timer is the step."""

    def __init__(self) -> None:
        self.source: str | None = None
        self.found: dict[str, list[tuple[int, str]]] = {}

    def __call__(self, text: str) -> dict[str, list[tuple[int, str]]]:
        if self.source is text:
            return self.found
        found: dict[str, list[tuple[int, str]]] = {}
        for branch in _branch_index(text):
            names = _TIMER_IS.findall(text[branch[0] : branch[1]])
            if not names:
                continue
            holes = [(child[0], child[3]) for child in _immediate(text, branch)]
            spawned = _spawn_calls(_without(text, branch[2], branch[3], holes))
            for name in names:
                found.setdefault(name, []).extend(spawned)
        self.source = text
        self.found = found
        return found


_timer_spawns = _TimerSpawns()


def _caused_spawns(text: str, block: str) -> list[tuple[int, str]]:
    spawned = list(_spawn_calls(block))
    seen = {npc_type for npc_type, _name in spawned}
    for timer in _SET_TIMER.findall(block):
        for npc_type, name in _timer_spawns(text).get(timer, []):
            if npc_type not in seen:
                seen.add(npc_type)
                spawned.append((npc_type, name))
    return spawned


def _spawn_edge(source: str, npc_type: int, name: str, group: str = "") -> dict:
    edge = {
        "kind": "edge",
        "rel": "spawns",
        "from": source,
        "to": f"npc:{npc_type}",
        "npc": npc_type,
    }
    if name:
        edge["name"] = name
    if group:
        edge["group"] = group
    return edge


def _deferred_rewards(text: str, block: str, hand_at: int) -> list[int]:
    """A hand-in that only sets a local, then summons later: morechampagne = 1 / if morechampagne == 1."""
    assigned = {name for name in _LOCAL_SET.findall(block) if name.lower() not in {"true", "false"}}
    if not assigned:
        return []
    found: list[int] = []
    seen: set[int] = set()
    for match in _LOCAL_IF.finditer(text):
        if match.start() <= hand_at or match.group(1) not in assigned:
            continue
        # Branch spans start at the '(', not at 'if'.
        _cond, body = _branch_at(text, match.end() - 1)
        if not body:
            continue
        for item_id in _reward_ids(body):
            if item_id not in seen:
                seen.add(item_id)
                found.append(item_id)
    return found


def turn_ins(text: str) -> list[dict]:
    """One hand-in: the items he gives, the item he gets back, and the flag that gates it."""
    found: list[dict] = []
    for match in _TURN.finditer(text):
        body, end = _paren(text, match.end() - 1)
        pairs = [(int(item), int(count)) for item, count in _HANDIN.findall(body)]
        if not pairs:
            pairs = [(int(item), 1) for item in _LUA_ITEM.findall(body)]
        if not pairs:
            pairs = [(int(item), int(count)) for item, count in _LUA_TABLE_ITEM.findall(body)]
        coins = [(name.lower(), int(amount)) for name, amount in _COIN.findall(body)]
        if not pairs and not coins:
            continue
        cond, block = _branch_at(text, match.start())
        if not block:
            block = _after_call(text, end)
            cond = text[max(0, match.start() - 240) : match.start()]
        gate = cond + "\n" + block
        rewards = _reward_ids(block)
        if not rewards:
            rewards = _deferred_rewards(text, block, match.start())
        found.append(
            {
                "items": pairs,
                "coins": coins,
                "rewards": rewards,
                "needs": _flags(gate),
                "factions": _faction_needs(gate, text),
                "sets": _all_flag_sets(block),
                "faction_gains": _faction_gains(block),
                "holds": _item_gates(gate),
                "spawns": _caused_spawns(text, block),
            }
        )
    found.extend(_coin_gates(text))
    return found


def _coin_gates(text: str) -> list[dict]:
    """`$platinum >= 2000` is a hand-in even though it is not written as `platinum => 2000`."""
    found: list[dict] = []
    seen: set[str] = set()
    for match in _COIN_CMP.finditer(text):
        cond, block = _branch_at(text, match.start())
        if not block or block in seen or _TURN.search(cond) or _COIN.search(cond):
            continue
        seen.add(block)
        rewards = _reward_ids(block)
        sets = _all_flag_sets(block)
        if not rewards and not sets:
            continue
        gate = cond + "\n" + block
        found.append(
            {
                "items": [],
                "coins": [(name.lower(), int(amount)) for name, amount in _COIN_CMP.findall(cond)],
                "rewards": rewards,
                "needs": _flags(gate),
                "factions": _faction_needs(gate, text),
                "sets": sets,
                "faction_gains": _faction_gains(block),
                "holds": _item_gates(gate),
                "spawns": _caused_spawns(text, block),
            }
        )
    return found


def link_script(
    text: str, filename: str, zone: str, catalog: Catalog | None = None
) -> list[dict[str, object]]:
    """Edges between a say, the next say, the items the sentence names, and a hand-in."""
    npc = npc_name(filename, catalog)
    home = zone.lower()
    npc_id = f"{home}/{npc.lower()}"
    edges: list[dict] = []
    _spawn_calls.constants = _numeric_locals(text)
    previous = ""
    for match in _SAY.finditer(text):
        word = (match.group(1) or match.group(2) or "").strip()
        if not word:
            continue
        cond, block = _branch_at(text, match.start())
        if not block:
            block = _following(text, match.end())
        gate = cond + "\n" + block
        say_id = f"{home}/{npc.lower()}#{word.lower()}"
        span = _chosen_branch(text, match.start())
        speech = _speech_events(text, span) if span else []
        if previous:
            prior = f"{home}/{npc.lower()}#{previous}"
            # File order is not proof of dialogue causality. Keep the weak
            # sequence edge, but emit a separate grounded cue when the NPC
            # actually uttered the next player's keyword.
            edges.append({
                "kind": "edge", "rel": "then", "from": prior,
                "to": say_id, "basis": "script_order",
            })
        # The reply is associated with the player input that elicited it.
        # Include every Emote/Say call, not just the first one.
        for event in speech:
            edges.append({
                "kind": "edge", "rel": "speaks", "from": say_id,
                "to": f"speech:{say_id}:{event['offset']}",
                "group": f"{say_id}#branch:{span[0]}",
                "channel": event['channel'], "text": event['text'],
                "links": event.get('links', []),
                "guards": event['guards'], "order": event['offset'],
            })
        spoken = _spoken(block)
        if catalog and spoken:
            for item_id in named_items(spoken, catalog):
                edges.append(
                    {
                        "kind": "edge",
                        "rel": "names",
                        "from": say_id,
                        "to": f"item:{item_id}",
                    }
                )
        span = _chosen_branch(text, match.start())
        if not span:
            for name, at in _flags(gate):
                edges.append(
                    {
                        "kind": "edge",
                        "rel": "needs",
                        "from": say_id,
                        "to": f"flag:{name}",
                        "flag": name,
                        "at": at,
                    }
                )
            _emit_faction_needs(edges, say_id, gate, say_id, script=text)
            for item_id, op in _item_gates(gate):
                edge = {
                    "kind": "edge",
                    "rel": "needs",
                    "from": say_id,
                    "to": f"item:{item_id}",
                    "item": item_id,
                }
                if op:
                    edge["op"] = op
                edges.append(edge)
            for name, value in _all_flag_sets(block):
                edges.append(
                    {
                        "kind": "edge",
                        "rel": "sets",
                        "from": say_id,
                        "to": f"flag:{name}",
                        "flag": name,
                        "value": value,
                    }
                )
            _emit_faction_gains(edges, say_id, block, say_id)
            for reward in _reward_ids(block):
                edges.append(
                    {
                        "kind": "edge",
                        "rel": "gives",
                        "from": npc_id,
                        "to": f"item:{reward}",
                        "group": say_id,
                    }
                )
        else:
            outer = tuple(
                branch
                for branch in _branch_index(text)
                if branch[0] <= span[0] and span[3] <= branch[3] and branch != span
            )
            _emit_span(edges, text, span, say_id, npc_id, outer)
        previous = word.lower()
    # Resolve ALL lexical follow-ups in the same event_say function, not
    # merely adjacent elseif branches. Weak script-order links remain tagged.
    say_turns = []
    say_ranges = [span for name, lo, hi in _functions(text) if name == 'event_say'
                  for span in [(lo, hi)]]
    for match in _SAY.finditer(text):
        if say_ranges and not any(lo <= match.start() < hi for lo, hi in say_ranges):
            continue
        key = (match.group(1) or match.group(2) or '').strip().lower()
        branch = _chosen_branch(text, match.start())
        if key and branch:
            say_turns.append((key, match.start(), _speech_events(text, branch)))
    for i, (word, at, speech) in enumerate(say_turns):

        for j, (other, _other_at, _reply) in enumerate(say_turns):
            if i == j or not _speech_mentions(other, speech):
                continue
            edges.append({
                'kind': 'edge', 'rel': 'suggests',
                'from': f'{npc_id}#{word}', 'to': f'{npc_id}#{other}',
                'word': other, 'basis': 'spoken_text',
                'source_order': 'earlier' if i < j else 'later',
            })

    # Source is an external event, never the previous player SAY branch.
    # Event guards remain attached so the graph does not imply unconditional
    # access to these dialogue options.
    for speech in _non_say_speech(text):
        origin = f"{npc_id}#{speech['event']}"
        for word, _at, _reply in say_turns:
            if _speech_mentions(word, [speech]):
                edges.append({
                    'kind': 'edge', 'rel': 'suggests',
                    'from': origin, 'to': f'{npc_id}#{word}',
                    'word': word, 'basis': 'external_event_speech',
                    'event': speech['event'], 'guards': speech['guards'],
                    'evidence': speech['text'],
                })

    for turn in turn_ins(text):
        ids = tuple(sorted(item for item, _count in turn["items"]))
        coins = tuple(turn.get("coins") or ())
        if ids:
            group = f"{npc_id}#hand:{'+'.join(str(item) for item in ids)}"
        else:
            group = f"{npc_id}#hand:" + "+".join(f"{name}:{amount}" for name, amount in coins)
        for item_id, count in turn["items"]:
            edges.append(
                {
                    "kind": "edge",
                    "rel": "receives",
                    "from": npc_id,
                    "to": f"item:{item_id}",
                    "count": count,
                    "group": group,
                }
            )
        for name, amount in coins:
            edges.append(
                {
                    "kind": "edge",
                    "rel": "receives",
                    "from": npc_id,
                    "to": f"coin:{name}",
                    "count": amount,
                    "group": group,
                }
            )
        for reward in turn["rewards"]:
            edges.append(
                {
                    "kind": "edge",
                    "rel": "gives",
                    "from": npc_id,
                    "to": f"item:{reward}",
                    "group": group,
                }
            )
        for name, at in turn["needs"]:
            edges.append(
                {
                    "kind": "edge",
                    "rel": "needs",
                    "from": group,
                    "to": f"flag:{name}",
                    "flag": name,
                    "at": at,
                }
            )
        for faction_id, at in turn.get("factions", []):
            edges.append(
                {
                    "kind": "edge",
                    "rel": "needs",
                    "from": group,
                    "to": f"faction:{faction_id}",
                    "faction": faction_id,
                    "at": at,
                    "group": group,
                }
            )
        for name, value in turn["sets"]:
            edges.append(
                {
                    "kind": "edge",
                    "rel": "sets",
                    "from": group,
                    "to": f"flag:{name}",
                    "flag": name,
                    "value": value,
                }
            )
        for faction_id, delta in turn.get("faction_gains", []):
            edges.append(
                {
                    "kind": "edge",
                    "rel": "sets",
                    "from": group,
                    "to": f"faction:{faction_id}",
                    "faction": faction_id,
                    "value": delta,
                    "group": group,
                }
            )
        for item_id, op in turn.get("holds", []):
            edge = {
                "kind": "edge",
                "rel": "needs",
                "from": group,
                "to": f"item:{item_id}",
                "item": item_id,
            }
            if op:
                edge["op"] = op
            edges.append(edge)
        for npc_type, name in turn.get("spawns", []):
            edges.append(_spawn_edge(group, npc_type, name))
    done: set[tuple[int, int]] = set()
    for match in _RECIPE.finditer(text):
        span = _chosen_branch(text, match.start())
        if not span:
            continue
        recipe_id = int(match.group(1))
        if (recipe_id, span[2]) in done:
            continue
        done.add((recipe_id, span[2]))
        cond = text[span[0] : span[1]]
        block = text[span[2] : span[3]]
        events = _body_events(block, span[2])
        if not events:
            continue
        source = f"{npc_id}#recipe:{recipe_id}"
        for name, at in _flags(cond):
            edges.append(
                {
                    "kind": "edge",
                    "rel": "needs",
                    "from": source,
                    "to": f"flag:{name}",
                    "flag": name,
                    "at": at,
                    "group": source,
                }
            )
        _emit_body(edges, events, source, npc_id)
    _zone_events(edges, text, npc_id)
    _spawn_calls.constants = {}
    return edges


def _children(text: str, span: tuple[int, int, int, int]) -> list[tuple[int, int, int, int]]:
    """Branches nested in this body. A grandchild is included."""
    return [
        branch
        for branch in _branch_index(text)
        if branch != span and span[2] <= branch[0] and branch[3] <= span[3]
    ]


def _immediate(text: str, span: tuple[int, int, int, int]) -> list[tuple[int, int, int, int]]:
    children = _children(text, span)
    return [
        child
        for child in children
        if not any(
            other[0] <= child[0] and child[3] <= other[3] and other != child for other in children
        )
    ]


def _in_span(start: int, holes: list[tuple[int, int]]) -> bool:
    return any(lo <= start < hi for lo, hi in holes)


def _emit_span(
    edges: list[dict],
    text: str,
    span: tuple[int, int, int, int],
    say_id: str,
    npc_id: str,
    ancestors: tuple[tuple[int, int, int, int], ...] = (),
) -> None:
    """Sets and held items stay on the branch that checks them, not the whole hail."""
    children = _immediate(text, span)
    holes = [(child[0], child[3]) for child in children]
    cond = text[span[0] : span[1]]
    holds = _item_gates(cond)
    flags = _flags(cond)
    either = bool(_OR.search(cond) and not _AND.search(cond) and (holds or len(flags) > 1))
    group = f"{say_id}#branch:{span[0]}"
    for name, at in flags:
        edge: dict[str, object] = {
            "kind": "edge",
            "rel": "needs",
            "from": say_id,
            "to": f"flag:{name}",
            "flag": name,
            "at": at,
        }
        edge["group"] = group
        if either:
            edge["op"] = "or"
        edges.append(edge)
    for faction_id, at in _faction_needs(cond, text):
        edge = {
            "kind": "edge",
            "rel": "needs",
            "from": say_id,
            "to": f"faction:{faction_id}",
            "faction": faction_id,
            "at": at,
            "group": group,
        }
        edges.append(edge)
    for item_id, op in holds:
        edge = {
            "kind": "edge",
            "rel": "needs",
            "from": say_id,
            "to": f"item:{item_id}",
            "item": item_id,
            "group": group,
        }
        if op or either:
            edge["op"] = op or "or"
        edges.append(edge)
    sets_here = []
    for match in _GLOBAL.finditer(text):
        if span[2] <= match.start() < span[3] and not _in_span(match.start(), holes):
            sets_here.append(match)
    summoned = [
        (pos, item_id)
        for pos, item_id in _summon_items(text)
        if span[2] <= pos < span[3] and not _in_span(pos, holes)
    ]
    quest_rewards = [
        match
        for match in _QUEST_REWARD.finditer(text)
        if span[2] <= match.start() < span[3] and not _in_span(match.start(), holes)
    ]
    grounds = [
        match
        for match in _GROUND.finditer(text)
        if span[2] <= match.start() < span[3] and not _in_span(match.start(), holes)
    ]
    if sets_here or summoned or quest_rewards or grounds:
        seen = {item_id for item_id, _op in holds}
        seen.update(
            item
            for edge in edges
            if edge.get("rel") == "needs" and edge.get("from") == say_id
            if isinstance(item := edge.get("item"), int)
        )
        for ancestor in ancestors:
            for item_id, op in _item_gates(text[ancestor[0] : ancestor[1]]):
                if item_id in seen:
                    continue
                seen.add(item_id)
                edge = {
                    "kind": "edge",
                    "rel": "needs",
                    "from": say_id,
                    "to": f"item:{item_id}",
                    "item": item_id,
                    "group": group,
                }
                if op:
                    edge["op"] = op
                edges.append(edge)
        # A reward in an inner SAY branch also requires the enclosing guards.
        # Example: Llara's `ruathey` branch is nested under
        # `qglobals["Llara"] ~= nil`; item 2417 must not become a leaf.
        # Restrict propagation to effect-bearing branches to avoid attaching
        # unrelated outer conditions to every SAY keyword in the file.
        seen_flags = {(name, at) for name, at in flags}
        for ancestor in ancestors:
            for name, at in _flags(text[ancestor[0] : ancestor[1]]):
                if (name, at) in seen_flags:
                    continue
                seen_flags.add((name, at))
                edge = {
                    "kind": "edge",
                    "rel": "needs",
                    "from": say_id,
                    "to": f"flag:{name}",
                    "flag": name,
                    "at": at,
                }
                edge["group"] = group
                edges.append(edge)
    for match in sets_here:
        edge = {
            "kind": "edge",
            "rel": "sets",
            "from": say_id,
            "to": f"flag:{match.group(1)}",
            "flag": match.group(1),
            "value": match.group(2),
            "group": group,
        }
        edges.append(edge)
    body = text[span[2] : span[3]]
    _emit_faction_gains(edges, say_id, body, group)
    for _pos, item_id in summoned:
        edges.append(
            {
                "kind": "edge",
                "rel": "gives",
                "from": npc_id,
                "to": f"item:{item_id}",
                "group": group,
            }
        )
    for match in _QUEST_REWARD.finditer(text):
        if span[2] <= match.start() < span[3] and not _in_span(match.start(), holes):
            body, _end = _paren(text, match.end() - 1)
            for item_id in _quest_reward_items(body):
                edges.append(
                    {
                        "kind": "edge",
                        "rel": "gives",
                        "from": npc_id,
                        "to": f"item:{item_id}",
                        "group": group,
                    }
                )
    for match in grounds:
        edges.append(
            {
                "kind": "edge",
                "rel": "grounds",
                "from": say_id,
                "to": f"item:{int(match.group(1))}",
                "group": group,
                "zone": say_id.split("/", 1)[0],
            }
        )
    direct = _without(text, span[2], span[3], holes)
    for npc_type, name in _caused_spawns(text, direct):
        edges.append(_spawn_edge(say_id, npc_type, name, group))
    for child in children:
        _emit_span(edges, text, child, say_id, npc_id, ancestors + (span,))


def _zone_events(edges: list[dict], text: str, npc_id: str) -> None:
    """A zone enter or a loot that checks an item or a flag. The check is the edge."""
    branches = _branch_index(text)
    for name, start, stop in _functions(text):
        if name not in {
            "event_enter_zone",
            "event_enter",
            "event_loot",
            "event_killed_merit",
        }:
            continue
        if "loot" in name:
            kind = "loot"
        elif "kill" in name:
            kind = "kill"
        else:
            kind = "enter"
        source = f"{npc_id}#{kind}"
        inside = [branch for branch in branches if start <= branch[0] and branch[3] <= stop]
        leaves = [
            branch
            for branch in inside
            if not any(
                branch[2] <= other[0] and other[3] <= branch[3] and other != branch
                for other in inside
            )
        ]
        # A proximity trap with no if still spawns on enter (thegrey/a_creature.pl).
        spans = leaves or [(-1, -1, start, stop)]
        for span in spans:
            ancestors = [
                branch for branch in inside if branch[0] <= span[0] and branch[3] >= span[3]
            ]
            conds = "\n".join(text[branch[0] : branch[1]] for branch in ancestors)
            holds = _item_gates(conds)
            flags = _flags(conds)
            loot_ids = [int(item) for item in _LOOT_ID.findall(conds)]
            body = text[span[2] : span[3]]
            spawns = _spawn_calls(body)
            added = [int(item) for item in _ADDITEM.findall(body)]
            sets = _all_flag_sets(body)
            if not holds and not flags and not loot_ids and not spawns and not added and not sets:
                continue
            # A single Player event may contain independent Warrior, Ranger,
            # etc. branches. The source identifies the callback, while group
            # identifies the actual condition/effect branch.
            group = f"{source}#branch:{span[0]}"
            for item_id, op in holds:
                edge = {
                    "kind": "edge",
                    "rel": "needs",
                    "from": source,
                    "to": f"item:{item_id}",
                    "item": item_id,
                    "group": group,
                }
                if op:
                    edge["op"] = op
                edges.append(edge)
            for flag, at in flags:
                edge = {
                    "kind": "edge",
                    "rel": "needs",
                    "from": source,
                    "to": f"flag:{flag}",
                    "flag": flag,
                    "at": at,
                    "group": group,
                }
                edges.append(edge)
            # GetID() == N on event_loot means the player already looted N (a gate), not a source.
            for item_id in loot_ids:
                edges.append(
                    {
                        "kind": "edge",
                        "rel": "needs",
                        "from": source,
                        "to": f"item:{item_id}",
                        "item": item_id,
                        "group": group,
                    }
                )
            for item_id in added:
                edges.append(
                    {
                        "kind": "edge",
                        "rel": "loots",
                        "from": source,
                        "to": f"item:{item_id}",
                        "group": group,
                        "zone": npc_id.split("/", 1)[0],
                    }
                )
            for name, value in sets:
                edges.append(
                    {
                        "kind": "edge",
                        "rel": "sets",
                        "from": source,
                        "to": f"flag:{name}",
                        "flag": name,
                        "value": value,
                        "group": group,
                    }
                )
            for npc_type, spawn_name in spawns:
                edges.append(_spawn_edge(source, npc_type, spawn_name, group))
    _other_summons(edges, text, npc_id)


def _recipe_owner(
    text: str,
    span: tuple[int, int, int, int],
    branches: list[tuple[int, int, int, int]],
) -> int:
    """The recipe_id check that wraps this branch, including an if nested inside the combine."""
    owners = [span]
    owners.extend(
        branch
        for branch in branches
        if branch != span and branch[0] <= span[0] and span[3] <= branch[3]
    )
    for branch in owners:
        found = _RECIPE.search(text[branch[0] : branch[1]])
        if found:
            return int(found.group(1))
    return 0


def _body_events(block: str, origin: int) -> list[tuple[int, dict]]:
    """Gives, spawns, and flag writes in the order they appear in this branch."""
    found: list[tuple[int, dict]] = []
    for pos, item_id in _summon_items(block):
        found.append((origin + pos, {"rel": "gives", "item": item_id}))
    for match in _QUEST_REWARD.finditer(block):
        body, _end = _paren(block, match.end() - 1)
        for offset, item_id in enumerate(_quest_reward_items(body)):
            found.append((origin + match.start() + offset, {"rel": "gives", "item": item_id}))
    for match in _GLOBAL.finditer(block):
        found.append(
            (
                origin + match.start(),
                {"rel": "sets", "flag": match.group(1), "value": match.group(2)},
            )
        )
    for match in _ZONE_FLAG_SET.finditer(block):
        found.append(
            (
                origin + match.start(),
                {"rel": "sets", "flag": _zoneflag_name(match.group(1)), "value": "1"},
            )
        )
    for match in _GROUND.finditer(block):
        found.append((origin + match.start(), {"rel": "grounds", "item": int(match.group(1))}))
    spawned: set[int] = set()
    constants: dict[str, int] = _spawn_calls.constants
    for match in _SPAWN.finditer(block):
        token = match.group(1)
        if token.isdigit():
            npc_type = int(token)
        else:
            npc_type = constants.get(token.lower()) or 0
        if not npc_type or npc_type in spawned:
            continue
        spawned.add(npc_type)
        line_end = block.find("\n", match.start())
        line = block[match.start() : line_end if line_end >= 0 else len(block)]
        found.append(
            (
                origin + match.start(),
                {"rel": "spawns", "npc": npc_type, "name": _comment_name(line)},
            )
        )
    for npc_type, name in _spawn_calls(block):
        if npc_type in spawned:
            continue
        spawned.add(npc_type)
        found.append((origin + len(block), {"rel": "spawns", "npc": npc_type, "name": name}))
    found.sort(key=lambda item: item[0])
    return found


def _emit_body(edges: list[dict], events: list[tuple[int, dict]], source: str, npc_id: str) -> None:
    for pos, event in events:
        rel = event["rel"]
        if rel == "sets":
            edges.append(
                {
                    "kind": "edge",
                    "rel": "sets",
                    "from": source,
                    "to": f"flag:{event['flag']}",
                    "flag": event["flag"],
                    "value": event["value"],
                    "group": source,
                    "order": pos,
                }
            )
        elif rel == "gives":
            edges.append(
                {
                    "kind": "edge",
                    "rel": "gives",
                    "from": npc_id,
                    "to": f"item:{event['item']}",
                    "group": source,
                    "order": pos,
                }
            )
        elif rel == "grounds":
            edges.append(
                {
                    "kind": "edge",
                    "rel": "grounds",
                    "from": source,
                    "to": f"item:{event['item']}",
                    "zone": npc_id.split("/", 1)[0],
                    "group": source,
                    "order": pos,
                }
            )
        elif rel == "spawns":
            edge = _spawn_edge(source, event["npc"], event.get("name") or "", source)
            edge["order"] = pos
            edges.append(edge)


def _other_summons(edges: list[dict], text: str, npc_id: str) -> None:
    """A summon, spawn, or flag write outside a say, such as a timer, a death, or a Perl helper."""
    skip = {
        "event_say",
        "event_trade",
        "event_item",
        "event_enter_zone",
        "event_enter",
        "event_loot",
        "event_killed_merit",
        "event_timer",  # linked through named timer triggers instead
    }
    branches = _branch_index(text)
    registered = {callback for _kind, _npc, callback in _registered_npc_events(text)}
    for name, start, stop in _functions(text):
        if name in skip or start < 0:
            continue
        # Encounter handlers like Uisima_Trade already feed turn_ins. Do not also emit as a say.
        if _TURN.search(text[start:stop]):
            continue
        inside = [branch for branch in branches if start <= branch[0] and branch[3] <= stop]
        owned = [branch for branch in inside if _recipe_owner(text, branch, inside)]
        spans = [(start, stop, [(branch[0], branch[3]) for branch in inside])]
        for span in inside:
            if span in owned:
                continue
            holes = [
                (other[0], other[3])
                for other in inside
                if other != span and span[2] <= other[0] and other[3] <= span[3]
            ]
            spans.append((span[2], span[3], holes))
        group = f"{npc_id}#{name}"
        for lo, hi, holes in spans:
            snippet = _without(text, lo, hi, holes)
            for item_id in _reward_ids(snippet):
                edges.append(
                    {
                        "kind": "edge",
                        "rel": "gives",
                        "from": npc_id,
                        "to": f"item:{item_id}",
                        "group": group,
                    }
                )
            for match in _GROUND.finditer(snippet):
                edges.append(
                    {
                        "kind": "edge",
                        "rel": "grounds",
                        "from": group,
                        "to": f"item:{int(match.group(1))}",
                        "zone": npc_id.split("/", 1)[0],
                    }
                )
            # Registered encounter handlers are owned by an NPC/event. Their
            # spawns are emitted by _link_event_causality with that ownership.
            if name not in registered:
                for npc_type, spawn_name in _spawn_calls(snippet):
                    edges.append(_spawn_edge(group, npc_type, spawn_name, group))
            for flag, value in _all_flag_sets(snippet):
                edges.append(
                    {
                        "kind": "edge",
                        "rel": "sets",
                        "from": group,
                        "to": f"flag:{flag}",
                        "flag": flag,
                        "value": value,
                        "group": group,
                    }
                )
        # AddItem may sit in a nested for/if while the spawn sits in the parent. Use the whole function.
        window = text[start:stop]
        spawned = {npc for npc, _name in _spawn_calls(window)}
        typed = {int(match) for match in _NPC_TYPE_ID.findall(window)}
        owners = typed or spawned
        for item_id in {int(match) for match in _ADDITEM.findall(window)}:
            if owners:
                for npc_type in owners:
                    edges.append(
                        {
                            "kind": "edge",
                            "rel": "loots",
                            "from": group,
                            "to": f"item:{item_id}",
                            "group": group,
                            "npc": npc_type,
                            "zone": npc_id.split("/", 1)[0],
                        }
                    )
            else:
                edges.append(
                    {
                        "kind": "edge",
                        "rel": "loots",
                        "from": group,
                        "to": f"item:{item_id}",
                        "group": group,
                        "zone": npc_id.split("/", 1)[0],
                    }
                )


def _class_gate(block: str) -> tuple[int, ...]:
    found: list[int] = []
    for match in _CLASS_EQ.finditer(block):
        if match.group(1):
            found.append(int(match.group(1)))
        else:
            class_id = _CLASS_IDS.get(match.group(2).lower().strip())
            if class_id and class_id not in found:
                found.append(class_id)
    for match in _CLASS_CALL.finditer(block):
        class_id = _CLASS_IDS.get(match.group(1).lower().strip())
        if class_id and class_id not in found:
            found.append(class_id)
    return tuple(found)


def reply_order(
    offered: list[str],
    script: NpcScript | None,
    open_steps: set[tuple[int, int]],
    said: set[str],
) -> list[str]:
    """Options from one reply. A word that finishes an open step comes first."""
    pending: list[str] = []
    seen: set[str] = set()
    for word in offered:
        key = word.lower()
        if not key or key == "hail" or key in said or key in seen:
            continue
        seen.add(key)
        pending.append(word)

    def rank(word: str) -> tuple[int, int]:
        hits = script.advances.get(word.lower(), set()) if script else set()
        return (0 if hits & open_steps else 1, pending.index(word))

    return sorted(pending, key=rank)


def exit_doors(text: str) -> list[int]:
    """Door ids whose click handler zones the character out. The id comes from the script."""
    return list(door_destinations(text))


def door_destinations(text: str) -> dict[int, list[int]]:
    """Door id to the zone ids that door's click handler moves the character into."""
    found: dict[int, list[int]] = {}
    for match in _EXIT_DOOR.finditer(text):
        body = _brace_block(text, match.end())
        if not _ZONE_OUT.search(body):
            continue
        door_id = int(match.group(1))
        zones = found.setdefault(door_id, [])
        for zone_id in _MOVEPC.findall(body):
            number = int(zone_id)
            if number not in zones:
                zones.append(number)
    return found


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
    for path in _quest_scripts(folder):
        text = path.read_text(encoding="utf-8", errors="replace")
        script = parse_script(text, path.name)
        quests.scripts[script.npc.lower()] = script
        for door_id, zones in door_destinations(text).items():
            if door_id not in quests.exits:
                quests.exits.append(door_id)
            known = quests.destinations.setdefault(door_id, [])
            for zone_id in zones:
                if zone_id not in known:
                    known.append(zone_id)
    return quests


_SKIP_DIRS = {"plugins", "lua_modules"}


def _quest_scripts(folder: Path) -> list[Path]:
    """Every Perl and Lua script under a zone, including encounters and version folders."""
    files = []
    for path in folder.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in {".pl", ".lua"}:
            continue
        if any(part in _SKIP_DIRS for part in path.parts):
            continue
        files.append(path)
    return sorted(files)


@dataclass
class QuestGraph:
    """Says, the items they name, and the hand-off that takes or gives each item.

    A say is still a node. An edge is the link: the next line, a named item,
    a flag such as cleric_epic, or the NPC who receives and rewards the item.
    """

    nodes: dict[tuple[str, str], list[QuestNode]] = field(default_factory=dict)
    doors: dict[str, dict[int, list[int]]] = field(default_factory=dict)
    edges: list[dict] = field(default_factory=list)
    dialogues: list[dict] = field(default_factory=list)
    items: dict[int, dict] = field(default_factory=dict)
    world: dict[int, dict] = field(default_factory=dict)
    by_zone: dict[str, dict[str, list[QuestNode]]] = field(default_factory=dict)
    edges_to: dict[str, tuple] = field(default_factory=dict)
    _indexed: bool = False

    def index(self) -> None:
        """Zone → that zone's NPC chains, and edge target → the edges that arrive there."""
        zones: dict[str, dict[str, list[QuestNode]]] = {}
        for (zone, npc), nodes in self.nodes.items():
            zones.setdefault(zone, {})[npc] = nodes
        arriving: dict[str, list[dict]] = {}
        for edge in self.edges:
            arriving.setdefault(str(edge.get("to") or ""), []).append(edge)
        self.by_zone = zones
        self.edges_to = {token: tuple(rows) for token, rows in arriving.items()}
        self._indexed = True

    def to_item(self, item_id: int) -> tuple:
        token = f"item:{item_id}"
        if self._indexed:
            return self.edges_to.get(token, ())
        return tuple(edge for edge in self.edges if str(edge.get("to") or "") == token)

    def gives(self, item_id: int) -> dict | None:
        for edge in self.to_item(item_id):
            if edge.get("rel") == "gives":
                return edge
        return None

    def drops(self, item_id: int) -> list[dict]:
        return [edge for edge in self.to_item(item_id) if edge.get("rel") in {"loots", "grounds"}]

    def receives_in(self, group: str) -> list[tuple[int, int]]:
        found: list[tuple[int, int]] = []
        if not group:
            return found
        for edge in self.edges:
            if edge.get("rel") != "receives" or edge.get("group") != group:
                continue
            token = edge.get("to")
            if not isinstance(token, str):
                continue
            item_id = _item_id(token)
            if item_id:
                found.append((item_id, max(1, int(edge.get("count") or 1))))
        return found

    def components(self, item_id: int) -> list[int]:
        """Item ids this reward needs, consumes, or requires."""
        found: list[int] = []
        for edge in self.to_item(item_id):
            if edge.get("rel") not in {"needs", "requires", "consumes"}:
                continue
            origin = str(edge.get("from") or "")
            if not origin.startswith("item:"):
                continue
            piece = _item_id(origin)
            if piece and piece not in found:
                found.append(piece)
        return found

    def chains_in(self, zone: str) -> dict[str, list[QuestNode]]:
        home = (zone or "").lower()
        if self._indexed:
            return dict(self.by_zone.get(home, {}))
        return {npc: nodes for (found, npc), nodes in self.nodes.items() if found == home}

    def apply(self, quests: ZoneQuests) -> None:
        """The saved graph replaces a chain parsed from only the current zone."""
        quests.chains = self.chains_in(quests.zone)
        for door_id, destinations in self.doors.get((quests.zone or "").lower(), {}).items():
            if door_id not in quests.exits:
                quests.exits.append(door_id)
            known = quests.destinations.setdefault(door_id, [])
            for zone_id in destinations:
                if zone_id not in known:
                    known.append(zone_id)

    def continuation(
        self,
        here: str,
        said: set[tuple[str, str, str]],
        flags: set[str],
        class_id: int,
        items: set[int],
    ) -> QuestNode | None:
        """A later step whose NPC lives in another zone. A first hail is not a reason to travel."""
        home = (here or "").lower()
        found: list[QuestNode] = []
        for (zone, npc), nodes in self.nodes.items():
            if zone == home:
                continue
            words = {
                detail
                for said_zone, said_npc, detail in said
                if said_zone.lower() == zone and said_npc == npc
            }
            node = next_node(nodes, words, flags, class_id, items)
            if not node or not node.requires:
                continue
            found.append(node)
        if not found:
            return None
        return sorted(found, key=lambda node: (node.zone, node.npc, node.word, node.item_id))[0]


# Event causality. A direct spawn in EVENT_TIMER is not a quest entry point:
# find who starts the timer, including signals sent by a different NPC script.
_NPC_FOOTER = re.compile(
    r"(?im)^\s*(?:#\s*EOF\s+zone:|--\s*(?:END\s+of\s+FILE|EOF)\s+Zone:)"
    r"[^\n]*?\bID:\s*(\d+)"
)
_SIGNAL_WITH = re.compile(r"(?:quest::signalwith|eq\.signal)\s*\(\s*(\d+)\s*,\s*(\d+)", re.I)
_SIGNAL_NPC = re.compile(r"\$(\w+)\s*->\s*SignalNPC\s*\(\s*(\d+)\s*\)", re.I)
_MOB_LOOKUP = re.compile(r"\$(\w+)\s*=\s*\$entity_list->GetMobByNpcTypeID\s*\(\s*(\d+)\s*\)", re.I)
_CAST_NPC = re.compile(r"\$(\w+)\s*=\s*\$(\w+)\s*->CastToNPC\s*\(\s*\)", re.I)
_SIGNAL_CONDITION = re.compile(r"(?:\$signal|e\.signal)\s*==\s*(\d+)", re.I)


def _event_functions(text: str, name: str) -> tuple[int, int] | None:
    return next(((lo, hi) for func, lo, hi in _functions(text) if func == name), None)


def _signal_origin(text: str, offset: int, npc_id: str) -> str:
    """Attribute a signal to its enclosing hand-in, if one exists."""
    function = next(((func, lo, hi) for func, lo, hi in _functions(text)
                     if lo <= offset < hi), None)
    if function is None:
        return npc_id
    func, lo, _hi = function
    if func in {"event_item", "event_trade"}:
        # The innermost hand-in branch contains the signal call.
        candidates = [branch for branch in _branch_index(text)
                      if branch[2] <= offset < branch[3] and lo <= branch[0]]
        for branch in sorted(candidates, key=lambda b: b[3] - b[2]):
            ids = sorted({int(item) for item, _n in _HANDIN.findall(text[branch[0]:branch[1]])})
            if ids:
                return f"{npc_id}#hand:{'+'.join(map(str, ids))}"
    return f"{npc_id}#{func}"


def _outgoing_signals(text: str, npc_id: str) -> list[tuple[str, int, int]]:
    """(origin group, recipient NPC type, signal value)."""
    found = []
    for match in _SIGNAL_WITH.finditer(text):
        found.append((_signal_origin(text, match.start(), npc_id),
                      int(match.group(1)), int(match.group(2))))
    # Resolve $a = GetMobByNpcTypeID(id); $b = $a->CastToNPC(); $b->SignalNPC(n).
    for match in _SIGNAL_NPC.finditer(text):
        func = next(((lo, hi) for _name, lo, hi in _functions(text) if lo <= match.start() < hi), None)
        if func is None:
            continue
        prefix = text[func[0]:match.start()]
        lookup = {name: int(npc) for name, npc in _MOB_LOOKUP.findall(prefix)}
        aliases = {cast: source for cast, source in _CAST_NPC.findall(prefix)}
        var = match.group(1)
        target = lookup.get(var) or lookup.get(aliases.get(var, ""))
        if target is not None:
            found.append((_signal_origin(text, match.start(), npc_id), target, int(match.group(2))))
    return list(dict.fromkeys(found))


def _signal_body(text: str, signal: int) -> str:
    """The matching Perl EVENT_SIGNAL branch, including its final else fallback."""
    scope = _event_functions(text, "event_signal")
    if scope is None:
        return ""
    lo, hi = scope
    fragment = text[lo:hi]
    branches = [b for b in _branch_index(text) if lo <= b[0] and b[3] <= hi]
    for branch in branches:
        cond = text[branch[0]:branch[1]]
        if signal in (int(n) for n in _SIGNAL_CONDITION.findall(cond)):
            return text[branch[2]:branch[3]]
    # Only use a fallback if none of the explicit signal comparisons matched.
    # Perl else after the signal if/elsif chain (not an unrelated nested else).
    if re.search(r"\$signal\s*==", fragment):
        matches = list(re.finditer(r"\belse\s*\{", fragment))
        if matches:
            open_at = lo + matches[-1].end() - 1
            return _brace_block(text, open_at + 1)
    return ""


# Encounter Lua scripts register arbitrary callback names for specific NPCs.
# Unlike EVENT_TIMER, callback names such as Evangelist_Timer are NOT dialogue.
_REGISTER_EVENT = re.compile(
    r"eq\.register_npc_event\s*\(\s*['\"][^'\"]+['\"]\s*,\s*"
    r"Event\.(\w+)\s*,\s*(\d+)\s*,\s*(\w+)\s*\)", re.I,
)


def _registered_npc_events(text: str) -> list[tuple[str, int, str]]:
    return [(kind.lower(), int(npc), callback.lower())
            for kind, npc, callback in _REGISTER_EVENT.findall(text)]


def _callback_timer_bodies(text: str, callback: str) -> list[tuple[str, str]]:
    """(timer name, body) for each direct conditional in an event timer callback."""
    scope = _event_functions(text, callback)
    if not scope:
        return []
    lo, hi = scope
    result = []
    for b in _branch_index(text):
        if lo <= b[0] and b[3] <= hi:
            for timer in _TIMER_IS.findall(text[b[0]:b[1]]):
                result.append((timer, text[b[2]:b[3]]))
    return result


def _link_registered_encounter(graph: QuestGraph, npc_id: str, text: str) -> None:
    """Event callback ownership, named timers and spawned-NPC lifecycle links."""
    registrations = _registered_npc_events(text)
    if not registrations:
        return
    zone = npc_id.split('/', 1)[0]
    registered = {(kind, npc): callback for kind, npc, callback in registrations}

    def trigger(source: str, target: str, **detail: object) -> None:
        graph.edges.append({"kind": "edge", "rel": "triggers",
                            "from": source, "to": target, **detail})

    for (kind, npc), callback in registered.items():
        scope = _event_functions(text, callback)
        if not scope:
            continue
        body = text[scope[0]:scope[1]]
        if kind == 'timer':
            for timer, branch_body in _callback_timer_bodies(text, callback):
                source = f'{npc_id}#timer:{timer}'
                # Child timers are created only after this named timer fires.
                for following in dict.fromkeys(_SET_TIMER.findall(branch_body)):
                    trigger(source, f'{npc_id}#timer:{following}', timer=following)
                for spawned, name in _spawn_calls(branch_body):
                    graph.edges.append(_spawn_edge(source, spawned, name, source))
        elif kind in {'spawn', 'death_complete', 'signal'}:
            event = f'{npc_id}#event:{kind}:{npc}'
            # Ignore nested conditional bodies here only if the condition is
            # signal-specific; for spawn/death use the entire callback.
            for timer in dict.fromkeys(_SET_TIMER.findall(body)):
                trigger(event, f'{npc_id}#timer:{timer}', timer=timer)
            for spawned, name in _spawn_calls(body):
                graph.edges.append(_spawn_edge(event, spawned, name, event))

    # An NPC spawned by a timer or death callback invokes its Event.spawn.
    # A death callback is *not* automatic: killing the NPC is mandatory.
    spawns = [row for row in graph.edges if row.get('rel') == 'spawns'
              and str(row.get('from', '')).startswith(zone + '/')]
    seen = set()
    for edge in spawns:
        npc = int(edge['npc'])
        origin = str(edge['from'])
        for kind in ('spawn', 'death_complete'):
            if (kind, npc) not in registered:
                continue
            if kind == 'spawn':
                target = f'{npc_id}#event:spawn:{npc}'
                pairs = [(origin, target)]
            else:
                kill = f'{npc_id}#kill:{npc}'
                target = f'{npc_id}#event:death_complete:{npc}'
                pairs = [(origin, kill), (kill, target)]
            for src, dst in pairs:
                if src == dst or (src, dst) in seen:
                    continue
                seen.add((src, dst))
                trigger(src, dst, npc=npc)

# Event-timer rewards are distinct from timer spawns.  The generic _other_summons
# intentionally skips event_timer; capture each reward on its named timer instead.
_EQUIPPED_ITEM = re.compile(
    r"GetItemIDAt\s*\(\s*Slot\.([A-Za-z_]+)\s*\)\s*==\s*(\d+)", re.I
)


def _timer_rewards(graph: QuestGraph, npc_id: str, text: str) -> None:
    """SummonItem in a timer callback, including nested Lua ForeachHateList."""
    scope = _event_functions(text, "event_timer")
    if scope is None:
        return
    lo, hi = scope
    branches = _branch_index(text)
    for pos, item_id in _summon_items(text):
        if not lo <= pos < hi:
            continue
        parents = [branch for branch in branches
                   if lo <= branch[0] and branch[2] <= pos < branch[3] and branch[3] <= hi]
        timers = [(branch, timer)
                  for branch in parents
                  for timer in _TIMER_IS.findall(text[branch[0]:branch[1]])]
        if not timers:
            # No matching named timer: don't pretend this reward is available unconditionally.
            continue
        timer = min(timers, key=lambda pair: pair[0][3] - pair[0][0])[1]
        source = f"{npc_id}#timer:{timer}"
        graph.edges.append({"kind": "edge", "rel": "gives", "from": npc_id,
                            "to": f"item:{item_id}", "group": source})
        conditions = "\n".join(text[b[0]:b[1]] for b in parents)
        for slot, required in dict.fromkeys(_EQUIPPED_ITEM.findall(conditions)):
            graph.edges.append({"kind": "edge", "rel": "needs", "from": source,
                                "to": f"item:{required}", "item": int(required),
                                "slot": slot.lower(), "equipped": True})
        if re.search(r"(?:->|:)IsSitting\s*\(\s*\)", conditions, re.I):
            graph.edges.append({"kind": "edge", "rel": "needs", "from": source,
                                "to": "state:sitting", "state": "sitting"})


def _timer_starters(graph: QuestGraph, npc_id: str, text: str) -> None:
    """Attribute named set_timer calls to the event or dialogue that starts them."""
    functions = _functions(text)
    branches = _branch_index(text)
    for match in _SET_TIMER.finditer(text):
        timer = match.group(1)
        owner = next(((name, lo, hi) for name, lo, hi in functions
                      if lo <= match.start() < hi), None)
        if owner is None:
            continue
        name, lo, hi = owner
        if name == 'event_timer':
            enclosing = sorted((b for b in branches
                                if lo <= b[0] and b[2] <= match.start() < b[3]),
                               key=lambda b: b[3] - b[0])
            running = [timer for b in enclosing
                       for timer in _TIMER_IS.findall(text[b[0]:b[1]])]
            if not running:
                continue
            origin = f"{npc_id}#timer:{running[0]}"
        elif name in {'event_say', 'event_trade', 'event_item'}:
            enclosing = sorted((b for b in branches
                                if lo <= b[0] and b[2] <= match.start() < b[3]),
                               key=lambda b: b[3] - b[0])
            if name == 'event_say':
                words = [word for b in enclosing
                         for word in (m.group(1) or m.group(2) for m in _SAY.finditer(text[b[0]:b[1]]))]
                if not words:
                    continue
                origin = f"{npc_id}#{words[-1].lower()}"
            else:
                ids = [int(item) for b in enclosing
                       for item, _count in _HANDIN.findall(text[b[0]:b[1]])]
                origin = (f"{npc_id}#hand:{'+'.join(map(str, sorted(set(ids))))}"
                          if ids else f"{npc_id}#{name}")
        elif name == 'event_signal':
            enclosing = sorted((b for b in branches
                                if lo <= b[0] and b[2] <= match.start() < b[3]),
                               key=lambda b: b[3] - b[0])
            signals = [value for b in enclosing
                       for value in _SIGNAL_CONDITION.findall(text[b[0]:b[1]])]
            if not signals:
                continue
            origin = f"{npc_id}#signal:{signals[0]}"
        else:
            origin = f"{npc_id}#{name}"
            if name.startswith('event_'):
                origin = f"{npc_id}#event:{name[6:]}"
        destination = f"{npc_id}#timer:{timer}"
        if origin != destination:
            graph.edges.append({"kind": "edge", "rel": "triggers",
                                "from": origin, "to": destination, "timer": timer})


def _link_event_causality(graph: QuestGraph, scripts: list[tuple[str, str, str]]) -> None:
    """Resolve per-zone NPC-type signals and named timers across scripts."""
    receivers: dict[tuple[str, int], tuple[str, str]] = {}
    for zone, npc_id, text in scripts:
        footer = _NPC_FOOTER.search(text)
        if footer:
            receivers[(zone, int(footer.group(1)))] = (npc_id, text)

    # Record each timer's spawns even if the initiating event is unresolved.
    # An orphan timer is an unresolved event dependency, not a free-world spawn.
    for _zone, npc_id, text in scripts:
        if _registered_npc_events(text):
            _link_registered_encounter(graph, npc_id, text)
            continue
        for timer, spawns in _timer_spawns(text).items():
            timer_id = f"{npc_id}#timer:{timer}"
            for npc_type, name in spawns:
                graph.edges.append(_spawn_edge(timer_id, npc_type, name, timer_id))
        _timer_rewards(graph, npc_id, text)
        _timer_starters(graph, npc_id, text)

    named_receivers = {
        (zone, re.sub(r"[_\s]+", " ", npc_id.split("/", 1)[-1]).strip().lower()): (npc_id, body)
        for zone, npc_id, body in scripts
    }
    sent = set()
    for zone, origin_npc, text in scripts:
        for source, target, signal in _outgoing_signals(text, origin_npc):
            receiver = receivers.get((zone, target))
            if receiver is None:
                # A signal may use the live NPC type while an old converted
                # Lua quest footer still contains an obsolete ID. Its sender
                # frequently documents the target via `-- NPC: Name`.
                pattern = re.compile(
                    r"(?:quest::signalwith|eq\.signal)\s*\(\s*" + str(target)
                    + r"\s*,\s*" + str(signal) + r"(?:\s*[,)]|\s*\))[^\n]*?"
                    + r"(?:#|--)\s*NPC:\s*([^\r\n]+)", re.I,
                )
                for match in pattern.finditer(text):
                    name = re.sub(r"[_\s]+", " ", match.group(1)).strip().lower()
                    receiver = named_receivers.get((zone, name))
                    if receiver is not None:
                        break
            if receiver is None:
                continue
            npc_id, receiver_text = receiver
            event = f"{npc_id}#signal:{signal}"
            sent.add((npc_id, signal))
            graph.edges.append({"kind": "edge", "rel": "triggers", "from": source,
                                "to": event, "signal": signal, "npc": target})

    for npc_id, signal in sorted(sent):
        receiver_text = next(text for _zone, name, text in scripts if name == npc_id)
        body = _signal_body(receiver_text, signal)
        for timer in dict.fromkeys(_SET_TIMER.findall(body)):
            event = f"{npc_id}#signal:{signal}"
            timer_id = f"{npc_id}#timer:{timer}"
            graph.edges.append({"kind": "edge", "rel": "triggers", "from": event,
                                "to": timer_id, "timer": timer})


def build_graph(root: str, catalog: Catalog | None = None) -> QuestGraph:
    """Walk every zone folder under projecteqquests. Plugins are not zones."""
    graph = QuestGraph()
    base = Path(root)
    if not base.is_dir():
        graph.index()
        return graph
    item_ids: set[int] = set()
    scripts: list[tuple[str, str, str]] = []
    for folder in sorted(
        path for path in base.iterdir() if path.is_dir() and path.name not in _SKIP_DIRS
    ):
        zone = folder.name.lower()
        for path in _quest_scripts(folder):
            text = path.read_text(encoding="utf-8", errors="replace")
            scripts.append((zone, f"{zone}/{npc_name(path.name, catalog).lower()}", text))
            graph.dialogues.extend(dialogue_chains(text, path.name, zone))
            nodes = parse_chain(text, path.name, zone)
            if nodes:
                graph.nodes[(zone, nodes[0].npc.lower())] = nodes
                item_ids.update(node.item_id for node in nodes if node.item_id)
            for edge in link_script(text, path.name, zone, catalog):
                graph.edges.append(edge)
                token = edge.get("to", "")
                if isinstance(token, str) and token.startswith("item:"):
                    item_ids.add(int(token.split(":", 1)[1]))
            for door_id, destinations in door_destinations(text).items():
                known = graph.doors.setdefault(zone, {}).setdefault(door_id, [])
                for zone_id in destinations:
                    if zone_id not in known:
                        known.append(zone_id)
    _link_event_causality(graph, scripts)
    # Event-linked rewards are added after per-file link_script(); include them
    # in the catalog metadata emitted for the graph.
    item_ids.update(int(str(edge['to']).split(':', 1)[1])
                    for edge in graph.edges if str(edge.get('to', '')).startswith('item:'))
    _add_spawn_loot(graph, catalog, item_ids)
    _add_recipes(graph, catalog, item_ids)
    ground_zones: dict[int, list[str]] = {}
    spawn_zones: dict[int, list[str]] = {}
    for edge in graph.edges:
        token = edge.get("to", "")
        if not isinstance(token, str) or not token.startswith("item:"):
            continue
        item_id = int(token.split(":", 1)[1])
        if edge.get("rel") == "grounds" or edge.get("zone"):
            zone = str(edge.get("zone") or "")
            if zone and zone not in ground_zones.setdefault(item_id, []):
                ground_zones[item_id].append(zone)
        elif edge.get("rel") == "loots" and edge.get("npc"):
            origin = edge.get("from", "")
            zone = origin.split("/", 1)[0] if isinstance(origin, str) else ""
            if zone and zone not in spawn_zones.setdefault(item_id, []):
                spawn_zones[item_id].append(zone)
    for item_id in sorted(item_ids):
        if not item_id:
            continue
        if catalog:
            label = catalog.labels.get(item_id, "")
            zones = list(catalog.zones.get(item_id, ()))
            sources = list(catalog.sources.get(item_id, ()))
            classes = catalog.item_classes
            races = catalog.item_races
        else:
            label = ""
            zones = []
            sources = []
            classes = {}
            races = {}
        for zone in ground_zones.get(item_id, ()):
            if zone not in zones:
                zones.append(zone)
        for zone in spawn_zones.get(item_id, ()):
            if zone not in zones:
                zones.append(zone)
        meta: dict = {"name": label, "zones": zones, "sources": sources}
        if item_id in classes:
            meta["classes"] = list(classes[item_id])
        if item_id in races:
            meta["races"] = list(races[item_id])
        graph.items[item_id] = meta
    _bake_travel(graph, catalog)
    graph.index()
    return graph


def _bake_travel(graph: QuestGraph, catalog: Catalog | None) -> None:
    """Merge the saved zone graph (doors + coords + gates) into the quest graph."""
    try:
        zone_graph = ensure_zone_graph(quest_doors=graph.doors)
    except Exception:
        return
    zone_graph.apply_to_quest_graph(graph)


def _add_spawn_loot(graph: QuestGraph, catalog: Catalog | None, item_ids: set[int]) -> None:
    """A quest-spawned NPC keeps the loot on its npc_types row even though it has no spawn2 row."""
    if not catalog:
        return
    drops = catalog.npc_drops
    names = catalog.npc_names
    if not drops and not names:
        return
    seen: set[tuple[str, int, int]] = set()
    extra: list[dict] = []
    for edge in graph.edges:
        if edge.get("rel") != "spawns" or not edge.get("npc"):
            continue
        npc = int(edge["npc"])
        if names and not edge.get("name") and names.get(npc):
            edge["name"] = names[npc]
        if not drops:
            continue
        for item_id in drops.get(npc, ()):
            key = (str(edge.get("from")), npc, item_id)
            if key in seen:
                continue
            seen.add(key)
            loot = {
                "kind": "edge",
                "rel": "loots",
                "from": edge["from"],
                "to": f"item:{item_id}",
                "group": edge.get("group") or edge["from"],
                "npc": npc,
            }
            if edge.get("name"):
                loot["name"] = edge["name"]
            extra.append(loot)
            item_ids.add(item_id)
    graph.edges.extend(extra)


def _result_pairs(info: dict) -> list[tuple[int, int]]:
    """Items a successful combine returns. Older recipe rows stored a single result."""
    rows = info.get("results") or []
    found = [(int(item_id), int(count or 1)) for item_id, count in rows if item_id]
    if found:
        return found
    one = info.get("result") or 0
    return [(int(one), 1)] if one else []


def _result_ids(info: dict) -> list[int]:
    return [item_id for item_id, _count in _result_pairs(info)]


def _disabled(info: dict) -> bool:
    return info.get("enabled", 1) == 0


def _stamp_recipe(edge: dict, info: dict) -> None:
    """The skill a combine requires. skillneeded blocks the attempt. trivial is where it stops failing."""
    if "skill" not in info and "trivial" not in info:
        return
    for key in (
        "skill",
        "skill_name",
        "skillneeded",
        "trivial",
        "nofail",
        "must_learn",
    ):
        if key in info:
            edge[key] = info[key]


def _add_recipes(graph: QuestGraph, catalog: Catalog | None, item_ids: set[int]) -> None:
    """Combines from the dump. A recipe is included when a quest names it or its result."""
    if not catalog or not catalog.recipes:
        return
    recipes = catalog.recipes
    wanted: set[int] = set()
    for edge in graph.edges:
        source = str(edge.get("from", ""))
        if "#recipe:" in source:
            tail = source.rsplit(":", 1)[-1]
            if tail.isdigit():
                wanted.add(int(tail))
    world = catalog.world_containers
    known = set(item_ids)
    changed = True
    while changed:
        changed = False
        for recipe_id in list(wanted):
            info = recipes.get(recipe_id)
            if not info:
                continue
            if _disabled(info):
                continue
            pieces = [item for item, _count in info["components"]]
            container = info.get("container") or 0
            if container and container not in world:
                pieces.append(container)
            pieces.extend(_result_ids(info))
            for item_id in pieces:
                if item_id and item_id not in known:
                    known.add(item_id)
                    changed = True
        for recipe_id, info in recipes.items():
            if _disabled(info) or recipe_id in wanted:
                continue
            if any(item_id in known for item_id in _result_ids(info)):
                wanted.add(recipe_id)
                changed = True
    for recipe_id in sorted(wanted):
        info = recipes.get(recipe_id)
        if not info or _disabled(info):
            continue
        source = f"recipe:{recipe_id}"
        for item_id, count in info["components"]:
            edge = {
                "kind": "edge",
                "rel": "consumes",
                "from": source,
                "to": f"item:{item_id}",
                "count": count,
            }
            _stamp_recipe(edge, info)
            graph.edges.append(edge)
            known.add(item_id)
        container = info.get("container") or 0
        if container in world:
            graph.world[container] = world[container]
            edge = {
                "kind": "edge",
                "rel": "container",
                "from": source,
                "to": f"world:{container}",
            }
            _stamp_recipe(edge, info)
            graph.edges.append(edge)
        elif container:
            edge = {
                "kind": "edge",
                "rel": "container",
                "from": source,
                "to": f"item:{container}",
            }
            _stamp_recipe(edge, info)
            graph.edges.append(edge)
            known.add(container)
        for item_id, count in _result_pairs(info):
            edge = {
                "kind": "edge",
                "rel": "produces",
                "from": source,
                "to": f"item:{item_id}",
                "count": count,
            }
            _stamp_recipe(edge, info)
            graph.edges.append(edge)
            known.add(item_id)
    item_ids.update(known)


def write_graph(graph: QuestGraph, path: str) -> None:
    """One JSON object per line. A step names its zone. A door line has no npc."""
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    lines: list[str] = []
    for (zone, _npc), nodes in sorted(graph.nodes.items()):
        for node in nodes:
            lines.append(
                json.dumps(
                    {
                        "zone": zone,
                        "npc": node.npc,
                        "kind": node.kind,
                        "word": node.word,
                        "text": node.text,
                        "item": node.item_id,
                        "requires": list(node.requires),
                        "grants": list(node.grants),
                        "to": node.zone_id,
                        "classes": list(node.classes),
                    },
                    ensure_ascii=True,
                )
            )
    for edge in graph.edges:
        lines.append(json.dumps(edge, ensure_ascii=True))
    for dialogue in graph.dialogues:
        lines.append(json.dumps(dialogue, ensure_ascii=True))
    for type_id, info in sorted(graph.world.items()):
        lines.append(
            json.dumps(
                {
                    "kind": "world",
                    "id": type_id,
                    "name": info.get("name", ""),
                    "zones": list(info.get("zones") or []),
                },
                ensure_ascii=True,
            )
        )
    for item_id, info in sorted(graph.items.items()):
        row = {
            "kind": "item",
            "item": item_id,
            "name": info.get("name", ""),
            "zones": info.get("zones", []),
        }
        if info.get("sources"):
            row["sources"] = info["sources"]
        if info.get("classes"):
            row["classes"] = list(info["classes"])
        if info.get("races"):
            row["races"] = list(info["races"])
        lines.append(json.dumps(row, ensure_ascii=True))
    for zone, doors in sorted(graph.doors.items()):
        for door_id, destinations in sorted(doors.items()):
            lines.append(
                json.dumps(
                    {"zone": zone, "door": door_id, "to": destinations},
                    ensure_ascii=True,
                )
            )
    destination.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")


def read_graph(path: str | os.PathLike) -> QuestGraph:
    graph = QuestGraph()
    file = Path(path)
    if not file.is_file():
        graph.index()
        return graph
    grouped: dict[tuple[str, str], list[QuestNode]] = {}
    for line in file.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        kind = row.get("kind", "")
        if kind == "edge":
            graph.edges.append(row)
            continue
        if kind == "dialogue":
            graph.dialogues.append(row)
            continue
        if kind == "world":
            graph.world[int(row["id"])] = {
                "name": row.get("name", ""),
                "zones": list(row.get("zones") or []),
            }
            continue
        if kind == "item":
            item_id = int(row.get("item") or 0)
            if not item_id:
                continue
            graph.items[item_id] = {
                "name": row.get("name", ""),
                "zones": list(row.get("zones") or []),
                "sources": list(row.get("sources") or []),
                "classes": list(row.get("classes") or []),
                "races": list(row.get("races") or []),
            }
            continue
        zone = str(row.get("zone", "")).lower()
        if "door" in row and "npc" not in row:
            graph.doors.setdefault(zone, {})[int(row["door"])] = [
                int(zone_id) for zone_id in row.get("to", [])
            ]
            continue
        node = QuestNode(
            npc=row.get("npc", ""),
            kind=row.get("kind", "say"),
            word=row.get("word", ""),
            item_id=int(row.get("item", 0)),
            requires=tuple(row.get("requires", ())),
            grants=tuple(row.get("grants", ())),
            zone_id=int(row.get("to", 0)),
            classes=tuple(int(class_id) for class_id in row.get("classes", ())),
            zone=zone,
            text=row.get("text", ""),
        )
        grouped.setdefault((zone, node.npc.lower()), []).append(node)
    graph.nodes = grouped
    graph.index()
    return graph


_graph: QuestGraph | None = None


def ensure_graph(
    root: str | None = None, path: str | None = None, *, rebuild: bool = False
) -> QuestGraph:
    """Load quest_graph.jsonl, or build once from EQEMU_QUESTS."""
    global _graph
    if _graph:
        return _graph
    path = path or os.environ.get(
        "EQEMU_GRAPH", str(Path.home() / ".eqclient" / "quest_graph.jsonl")
    )
    file = Path(path)
    if file.is_file() and not rebuild:
        _graph = read_graph(path)
        return _graph
    source = root or os.environ.get("EQEMU_QUESTS", "")
    if not source:
        raise SystemExit("EQEMU_QUESTS (or --root) is required to build the quest graph")
    built = build_graph(source, load_catalog("/Users/samo/work/EQEmu/peq-dump/create_tables_content.sql"))
    write_graph(built, path)
    _graph = built
    return _graph


def load_graph(path: str | os.PathLike | None = None) -> QuestGraph:
    chosen = (
        path
        or os.environ.get("EQEMU_GRAPH")
        or str(Path.home() / ".eqclient" / "quest_graph.jsonl")
    )
    return read_graph(chosen)


def split_npc(origin: str) -> tuple[str, str]:
    """'zone/npc#step' is the zone and the npc name."""
    zone, _, rest = origin.partition("/")
    npc = rest.split("#", 1)[0].strip()
    return zone.strip(), npc


def _item_id(token: str) -> int:
    if not token.startswith("item:"):
        return 0
    try:
        return int(token.split(":", 1)[1])
    except ValueError:
        log.error("item token failed to parse: %s", token, exc_info=True)
        return 0


def all_needs(scripts: dict[str, NpcScript]) -> list[Need]:
    needs: list[Need] = []
    for script in scripts.values():
        needs.extend(script.needs)
    return needs
