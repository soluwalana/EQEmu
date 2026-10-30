"""Level-band XP zones. Static data, no database. Prefer graph-reachable shorts."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class XpCamp:
    zone: str
    min_level: int
    max_level: int
    note: str = ""


# Class-agnostic outdoor / dungeon bands from eqprogression zone leveling guide.
# Agent returns to safe to sell/bank between pulls.
# tutorialb is not an XP camp — unfinished mines are routed by the tutorial gate only.
XP_CAMPS: tuple[XpCamp, ...] = (
    XpCamp("qeynos", 1, 3, "city rats"),
    XpCamp("freporte", 1, 3, "city"),
    XpCamp("freportw", 1, 3, "city"),
    XpCamp("freportn", 1, 3, "city"),
    # Freeport-side fields (ecommons is the freportw gate; commons = West Commonlands).
    XpCamp("ecommons", 1, 6, "east commons"),
    XpCamp("commons", 5, 15, "west commons"),
    XpCamp("qey2hh1", 5, 15, "west karana"),  # peq short; Qeynos-side, not Freeport
    XpCamp("crushbone", 3, 13, "faydwer"),
    # >10 — guide player-level bands (outdoor preferred)
    XpCamp("eastkarana", 10, 20, "field"),
    XpCamp("unrest", 11, 25, "faydwer"),
    XpCamp("southkarana", 15, 30, "field"),
    XpCamp("lakeofillomen", 15, 28, "kunark"),
    XpCamp("soldunga", 20, 30, "sola"),
    XpCamp("mistmoore", 21, 35, "faydwer"),
    XpCamp("dawnshroud", 25, 42, "luclin"),
    XpCamp("gukbottom", 28, 43, "dungeon"),
    XpCamp("dreadlands", 32, 40, "kunark"),
    XpCamp("soldungb", 35, 48, "solb"),
    XpCamp("scarlet", 38, 46, "luclin"),
    XpCamp("chardok", 44, 60, "kunark"),
    XpCamp("pojustice", 50, 56, "pop t1"),
    XpCamp("ponightmare", 52, 62, "pop t1"),
    XpCamp("povalor", 60, 65, "pop t2"),
    XpCamp("wallofslaughter", 63, 67, "oow"),
    XpCamp("powater", 65, 70, "pop t4"),
)

# Recommended floor from https://www.eqprogression.com/zone-leveling-guide/
# (lowest listed player-level band). Cities/hubs not on that guide stay at 1.
# Campaign travel below this returns a level step. Zones absent here are ungated (0).
ZONE_LEVEL: dict[str, int] = {
    "abysmal": 1,
    "akanon": 1,
    "bazaar": 1,
    "butcher": 1,
    "cabeast": 1,
    "cabwest": 1,
    "erudnext": 1,
    "erudnint": 1,
    "everfrost": 1,
    "feerrott": 1,
    "felwithea": 1,
    "felwitheb": 1,
    "fieldofbone": 1,
    "freeporteast": 1,
    "freporte": 1,
    "freportn": 1,
    "freportw": 1,
    "gfaydark": 1,
    "grobb": 1,
    "guildhall": 1,
    "guildlobby": 1,
    "halas": 1,
    "innothule": 1,
    "innothuleb": 1,
    "kaladima": 1,
    "kaladimb": 1,
    "lakeofillomen": 1,
    "misty": 1,
    "mistythicket": 1,
    "nektulos": 1,
    "neriaka": 1,
    "neriakb": 1,
    "neriakc": 1,
    "nexus": 1,
    "northro": 1,
    "nro": 1,
    "oggok": 1,
    "paineel": 1,
    "poknowledge": 1,
    "potranquility": 1,
    "qeynos": 1,
    "qeynos2": 1,
    "qeytoqrg": 1,
    "qrg": 1,
    "rathemtn": 1,
    "rivervale": 1,
    "shadeweaver": 1,
    "shadowhaven": 1,
    "sharvahl": 1,
    "steamfont": 1,
    "steamfontmts": 1,
    "swampofnohope": 1,
    "thurgadina": 1,
    "tox": 1,
    "toxxulia": 1,
    "tutorialb": 1,
    "blackburrow": 4,
    "warrens": 4,
    "westkarana": 4,
    "qey2hh1": 4,
    "crushbone": 5,
    "kithicor": 5,
    "befallen": 6,
    "commonlands": 6,
    "commons": 6,
    "ecommons": 6,
    "oldcommons": 6,
    "erudsxing": 7,
    "kurn": 7,
    "northkarana": 7,
    "paludal": 7,
    "eastkarana": 8,
    "lfaydark": 8,
    "southro": 8,
    "sro": 8,
    "lakerathe": 9,
    "lavastorm": 10,
    "oceanoftears": 10,
    "oot": 10,
    "runnyeye": 10,
    "najena": 11,
    "unrest": 11,
    "beholder": 12,
    "overthere": 14,
    "permafrost": 14,
    "stonebrunt": 14,
    "hollowshade": 15,
    "southkarana": 15,
    "guktop": 16,
    "netherbian": 17,
    "timorous": 17,
    "cauldron": 18,
    "cazicthule": 20,
    "highpass": 20,
    "highpasshold": 20,
    "soldunga": 20,
    "warslikswood": 20,
    "mistmoore": 21,
    "mseru": 22,
    "twilight": 22,
    "nedaria": 23,
    "dawnshroud": 25,
    "dalnir": 26,
    "highkeep": 26,
    "crystal": 27,
    "firiona": 27,
    "frontiermtns": 27,
    "greatdivide": 27,
    "frozenshadow": 28,
    "gukbottom": 28,
    "iceclad": 28,
    "gunthak": 30,
    "kaesora": 30,
    "paw": 30,
    "dreadlands": 32,
    "emeraldjungle": 32,
    "trakanon": 32,
    "eastwastes": 33,
    "grimling": 33,
    "tenebrous": 33,
    "echo": 34,
    "kael": 34,
    "soldungb": 35,
    "letalis": 36,
    "burningwood": 37,
    "citymist": 37,
    "dulak": 37,
    "nurga": 37,
    "hole": 38,
    "kedge": 38,
    "scarlet": 38,
    "wakening": 38,
    "cobaltscar": 39,
    "karnor": 41,
    "charasis": 42,
    "draniksscar": 42,
    "thegrey": 42,
    "skyfire": 43,
    "torgiran": 43,
    "acrylia": 44,
    "chardok": 44,
    "velketor": 44,
    "natimbi": 45,
    "veksar": 45,
    "maiden": 46,
    "nadox": 47,
    "sebilis": 47,
    "sseru": 47,
    "droga": 48,
    "necropolis": 48,
    "thedeep": 49,
    "fungusgrove": 50,
    "poinnovation": 50,
    "pojustice": 50,
    "akheva": 51,
    "qinimi": 51,
    "chardokb": 52,
    "griegsend": 52,
    "harbingers": 52,
    "hatesfury": 52,
    "podisease": 52,
    "ponightmare": 52,
    "sirens": 52,
    "ssratemple": 52,
    "bloodfields": 53,
    "soldungc": 53,
    "riwwi": 54,
    "umbral": 55,
    "barindu": 58,
    "bothunder": 60,
    "causeway": 60,
    "codecay": 60,
    "hohonora": 60,
    "postorms": 60,
    "potactics": 60,
    "potorment": 60,
    "povalor": 60,
    "wallofslaughter": 63,
    "dranik": 65,
    "ferubi": 65,
    "hohonorb": 65,
    "kodtaz": 65,
    "poair": 65,
    "poeartha": 65,
    "poearthb": 65,
    "pofire": 65,
    "powater": 65,
    "qvic": 65,
    "solrotower": 65,
    "tipt": 65,
    "vxed": 65,
    "yxtta": 65,
    "provinggrounds": 67,
    "riftseekers": 69,
}


# Zones whose routes often cross water. The agent swims using maps/water/*.wtr.
SWIM_ZONES: frozenset[str] = frozenset(
    {
        "lakerathe",
        "oot",
        "oceanoftears",
        "oasis",
        "kedge",
        "dulak",
        "gunthak",
        "nadox",
        "hatesfury",
    }
)


# One-hop outdoor neighbors so Freeport stays on commons, not PoK→Karana.
_CAMP_NEAR: dict[str, tuple[str, ...]] = {
    "freportw": ("ecommons", "commons", "freporte", "freportn", "nro"),
    "freporte": ("freportw", "nro", "ecommons"),
    "freportn": ("freportw", "ecommons"),
    "ecommons": ("commons", "freportw", "nro", "kithicor", "nektulos"),
    "commons": ("ecommons", "kithicor", "befallen"),
    "qeynos": ("qeynos2", "qeytoqrg", "qey2hh1"),
    "qeynos2": ("qeynos", "qeytoqrg", "qey2hh1"),
    "qeytoqrg": ("qey2hh1", "qeynos2", "qrg", "blackburrow"),
    "qey2hh1": ("northkarana", "qeytoqrg"),
    "northkarana": ("qey2hh1", "eastkarana", "southkarana"),
    "crushbone": ("gfaydark", "crushbone"),
}


# Soulbinder spawn pads (zone → display name, x, y, z). Prefer same-zone, else nearest hop.
SOULBINDERS: dict[str, tuple[str, float, float, float]] = {
    "abysmal": ("Soulbinder Jerlin", 186.0, -120.0, 129.0),
    "akanon": ("Soulbinder Toglonoit", 38.0, 500.0, -26.0),
    "arena": ("Soulbinder Gendal", 167.6, -1020.7, 49.1),
    "butcher": ("Soulbinder Tania", -2524.0, -1118.0, -1.5),
    "cabeast": ("Soulbinder Shakar", -27.0, 720.0, 3.8),
    "commonlands": ("Soulbinder Jubbl", -2712.0, -1735.0, 35.9),
    "crescent": ("Priestess Aelea", -1447.0, -1262.0, -88.0),
    "ecommons": ("Soulbinder Jubbl", -202.0, -1509.0, 3.1),
    "erudnext": ("Soulbinder Altira Mamar", -55.0, -115.0, 39.8),
    "everfrost": ("Soulbinder Garnog", -5041.0, 1776.0, -60.1),
    "felwithea": ("Soulbinder Elendalira", -225.0, 0.0, 3.8),
    "firiona": ("Soulbinder Tardon", 1235.0, -3950.0, -103.0),
    "freeporteast": ("Soulbinder Grunson", -23.0, -1242.0, 8.1),
    "freporte": ("Soulbinder Grunson", -649.0, -34.0, -51.2),
    "gfaydark": ("Soulbinder Oakstout", -382.0, -348.0, 117.5),
    "grobb": ("Soulbinder Snog", 87.7, 62.3, 4.8),
    "guildlobby": ("High Priest of Luclin", -307.8, 412.0, 0.0),
    "gunthak": ("Soulbinder Karyin", -214.0, 1420.0, 4.8),
    "halas": ("Soulbinder Jarle", 340.0, 295.0, 4.4),
    "iceclad": ("Soulbinder Cubnitskin", 396.0, 5352.0, -18.0),
    "kaladima": ("Soulbinder Torvald", 215.0, 210.0, 2.5),
    "neriaka": ("Soulbinder Nola Z`Ret", -95.0, 205.0, 3.1),
    "northro": ("Soulbinder Ragni", -538.0, 7836.0, 97.9),
    "nro": ("Soulbinder Ragni", 893.0, 2750.0, -24.8),
    "oggok": ("Soulbinder Trurg", 655.0, 500.0, 5.6),
    "overthere": ("Soulbinder Kardin", 2775.0, 3070.0, -153.5),
    "paineel": ("Soulbinder Tomas", 563.0, 665.0, -94.1),
    "poknowledge": ("Soulbinder Jera", -54.0, -222.0, -157.1),
    "potranquility": ("Soulbinder Derith", -1631.0, 768.0, -890.6),
    "qeynos": ("Soulbinder Novalu", -470.0, 287.0, 3.4),
    "rivervale": ("Soulbinder Hoggle Grubbytoe", -100.0, 160.0, 2.1),
    "shadowhaven": ("Soulbinder Nansin", 1644.0, 243.0, -55.1),
    "sharvahl": ("Soulbinder Ghula", 488.0, 52.0, -163.5),
    "southro": ("Soulbinder Silandra", -321.0, -166.0, 107.9),
    "sro": ("Soulbinder Silandra", 1003.0, -1419.0, -23.0),
    "tutorialb": ("Rashere", -130.5, -28.8, 16.5),
}


@dataclass(frozen=True)
class Soulbinder:
    zone: str
    name: str
    x: float
    y: float
    z: float


def nearest_soulbinder(grind_zone: str) -> Soulbinder | None:
    """Soulbinder in the grind zone, else the closest one-hop (then BFS) neighbor that has one."""
    home = (grind_zone or "").lower()
    if not home:
        return None
    hit = SOULBINDERS.get(home)
    if hit is not None:
        name, x, y, z = hit
        return Soulbinder(home, name, x, y, z)
    seen = {home}
    queue = list(_CAMP_NEAR.get(home, ()))
    while queue:
        zone = queue.pop(0)
        if zone in seen:
            continue
        seen.add(zone)
        hit = SOULBINDERS.get(zone)
        if hit is not None:
            name, x, y, z = hit
            return Soulbinder(zone, name, x, y, z)
        queue.extend(z for z in _CAMP_NEAR.get(zone, ()) if z not in seen)
    # Last resort: any binder (PoK) so death is not tutorialb forever.
    pok = SOULBINDERS.get("poknowledge")
    if pok is not None:
        name, x, y, z = pok
        return Soulbinder("poknowledge", name, x, y, z)
    return None


def camp_for_level(level: int, here: str = "") -> XpCamp | None:
    """XP camp for `level`. Prefer current zone, then a one-hop neighbor, else band[0]."""
    band = [camp for camp in XP_CAMPS if camp.min_level <= max(level, 1) <= camp.max_level]
    if not band:
        return XP_CAMPS[-1]
    home = (here or "").lower()
    if home:
        for camp in band:
            if camp.zone == home:
                return camp
        near = set(_CAMP_NEAR.get(home, ()))
        if near:
            for camp in band:
                if camp.zone in near:
                    return camp
    return band[0]


def needs_level(current: int, required: int) -> bool:
    return required > 0 and current < required


def zone_recommended_level(zone: str) -> int:
    """Outdoor floor for `zone`, or 0 when unknown (no gate)."""
    return int(ZONE_LEVEL.get((zone or "").lower(), 0) or 0)


def zone_needs_swim(zone: str) -> bool:
    return (zone or "").lower() in SWIM_ZONES


def zone_reachable(zone: str, level: int) -> str:
    """Empty when travel is fine; otherwise a gate reason such as 'level:N'."""
    home = (zone or "").lower()
    if not home:
        return ""
    need = zone_recommended_level(home)
    if need and level < need:
        return f"level:{need}"
    return ""
