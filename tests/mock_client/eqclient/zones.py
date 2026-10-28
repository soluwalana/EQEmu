"""Short name to zone id, filled as the client enters each zone.

The journal is the record. This map is the copy the planner reads. It starts
empty and grows when a NewZone packet pairs a short name with its id.
"""

KNOWN: dict[str, int] = {}

# Guide / camp names → peq short_name used by the zone graph.
ZONE_ALIASES: dict[str, str] = {
    "westkarana": "qey2hh1",
    "westernkarana": "qey2hh1",
    "west_karana": "qey2hh1",
}


def canonical_zone(name: str) -> str:
    """Resolve a zone nickname to the peq short name the travel graph uses."""
    short = (name or "").lower().strip()
    return ZONE_ALIASES.get(short, short)


def remember(name: str, zone_id: int) -> None:
    short = (name or "").lower()
    if not short or not zone_id:
        return
    if short.startswith("zone") and short[4:].isdigit():
        return
    KNOWN[short] = int(zone_id)


def zone_id_of(name: str) -> int:
    return KNOWN.get((name or "").lower(), 0)


def zone_name_of(zone_id: int) -> str:
    for name, found in KNOWN.items():
        if found == zone_id:
            return name
    return ""
