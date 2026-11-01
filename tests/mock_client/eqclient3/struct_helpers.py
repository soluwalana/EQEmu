"""Text and channel helpers that are not opcode bodies."""

from __future__ import annotations

import math
import re

from eqclient3.structs import SAY_CHANNEL

_SAYLINK = re.compile(r"\x12(.{56})([^\x12]+?)\x12")
_QUEST_ITEM = "FFFFF"


def channel_bucket(channel: int) -> str:
    """says, tell, or gm. Other channels are not one of those."""
    if channel in (7, 14):
        return "tell"
    if channel in (11, 18):
        return "gm"
    if channel == SAY_CHANNEL:
        return "says"
    return ""


def special_bucket(msg_type: int) -> str:
    """Say and tell colors stay in those buckets. Every other special line is the server."""
    if msg_type in (10, 256, 307):
        return "says"
    if msg_type in (257, 308):
        return "tell"
    return "server"


def saylink_words(text: str) -> list[str]:
    """Quest saylinks. An item link uses the same brackets and is not something to say."""
    words: list[str] = []
    for match in _SAYLINK.finditer(text or ""):
        body, word = match.group(1), match.group(2).strip()
        if len(body) < 6 or body[1:6].upper() != _QUEST_ITEM:
            continue
        if word and word.lower() not in {item.lower() for item in words}:
            words.append(word)
    return words


def saylink_plain(text: str) -> str:
    """Replace item-link blobs with their visible names for chat logs."""
    if "\x12" not in text:
        return text
    return _SAYLINK.sub(lambda m: m.group(2), text)


def eq_heading(x1: float, y1: float, x2: float, y2: float) -> int:
    """0-512 heading, the same quadrants the server uses for IsFacingMob."""
    x_diff = abs(x1 - x2)
    y_diff = abs(y1 - y2) or 1e-9
    angle = math.atan2(x_diff, y_diff) * 180.0 * 0.3183099014828645
    if y1 >= y2:
        degrees = (90.0 - angle + 90.0) if x2 >= x1 else (angle + 180.0)
    elif y1 > y2 or x2 > x1:
        degrees = angle
    else:
        degrees = 90.0 - angle + 270.0
    return int(degrees * 511.5 * 0.0027777778) & 0xFFF
