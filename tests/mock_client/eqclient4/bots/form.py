"""The command list a zone entry hands to Form.

Create, spawn, invite, then Aggressive stance once for a tank. Spell settings,
sit mana, stop-melee, and follow distance are left off when the journal already
records them. Heal rotation is included only when no rotation is saved. ^taunt
is never in the list.
"""

TANK_CLASSES = {1, 3, 5}
AGGRESSIVE = "5"


def form_commands(
    bots: list[tuple],
    settings: dict[str, dict[str, str]] | None = None,
    *,
    healer: str = "",
    heal_target: str = "",
    members: tuple[str, ...] = (),
    rotation_saved: bool = False,
    spell_lines: dict[str, list[str]] | None = None,
    owned: set[str] | None = None,
    spawned: set[str] | None = None,
) -> list[str]:
    settings = settings or {}
    owned = set(owned or ())
    spawned = set(spawned or ())
    spell_lines = spell_lines or {}
    commands: list[str] = []
    roster = [(str(bot[0]), int(bot[1])) for bot in bots]
    for name, class_id in roster:
        if name not in owned:
            commands.append(f"^botcreate {name} {class_id} 1 0")
        if name not in spawned:
            commands.append(f"^botspawn {name}")
        commands.append(f"groupinvite {name}")
    for name, class_id in roster:
        saved = settings.get(name, {})
        if class_id in TANK_CLASSES and saved.get("stance") != AGGRESSIVE:
            commands.append(f"^botstance {AGGRESSIVE} byname {name}")
        if "spells" not in saved:
            commands.extend(spell_lines.get(name, []))
        if "sit" not in saved:
            commands.append(f"^sitmanapercent 90 byname {name}")
        if "stop_melee" not in saved:
            commands.append(f"^botstopmeleelevel 1 byname {name}")
        if "follow" not in saved:
            commands.append(f"^botfollowdistance set 10 byname {name}")
    saved_rotation = rotation_saved or (healer and settings.get(healer, {}).get("heal") == "1")
    if healer and not saved_rotation:
        commands.extend(_heal_rotation(healer, heal_target, members))
    return [line for line in commands if not line.startswith("^taunt")]


def _heal_rotation(healer: str, target: str, members: tuple[str, ...]) -> list[str]:
    commands = [f"^healrotationcreate {healer}"]
    for name in members:
        if name and name != healer:
            commands.append(f"^healrotationaddmember {name} {healer}")
    if target:
        commands.append(f"^healrotationaddtarget {target} {healer}")
    commands.extend(
        [
            f"^healrotationfastheals {healer} on",
            f"^healrotationadaptivetargeting {healer} on",
            f"^healrotationcastingoverride {healer} on",
            f"^healrotationstart {healer}",
        ]
    )
    return commands
