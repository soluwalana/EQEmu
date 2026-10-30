"""Opcode handlers. Each module defines one Handler subclass.

Importing this package does not import every handler. Handler.registered() does,
and that is what puts them on the bus.
"""

from __future__ import annotations

MODULES = (
    "mobs",
    "consider",
    "zoning",
    "death",
    "rez",
    "messages",
    "level",
    "profile",
    "items",
    "loot",
    "group",
    "buffs",
    "doors",
    "tasks",
    "trade",
)
