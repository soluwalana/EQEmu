"""Log in, zone in, and pulse until the zone session closes.

From the mock_client directory, or with it on PYTHONPATH:

    EQEMU_USER=... EQEMU_PASS=... EQEMU_CHAR=Hero python -m eqclient3

EQEMU_HOST defaults to 127.0.0.1. EQEMU_LOGIN_PORT defaults to 5999 and
EQEMU_WORLD_PORT to 9000. A name the server does not have yet is created
from EQEMU_RACE, EQEMU_CLASS, EQEMU_GENDER, EQEMU_DEITY, and EQEMU_START_ZONE.
LOG_LEVEL defaults to INFO. DEBUG also prints movement packets.
"""

from __future__ import annotations

import os
import types
from collections.abc import Callable
from dataclasses import replace

from eqclient3.bus import Bus
from eqclient3.log import log
from eqclient3.loop import Loop
from eqclient3.nav.maps import load_map
from eqclient3.nav.navmesh import load_nav
from eqclient3.nav.water import load_water
from eqclient3.nav.zones import zone_name_of
from eqclient3.net.client import Client, Login
from eqclient3.structs import OP_NewZone
from eqclient3.net.sheet import build
from eqclient3.quests.produce import _cached_graph
from eqclient3.schedule import Schedule
from eqclient3.world import World


def main() -> None:
    name = os.environ.get("EQEMU_CHAR", "").strip()
    user = os.environ.get("EQEMU_USER", "").strip()
    password = os.environ.get("EQEMU_PASS", "")
    missing = [
        key
        for key, value in (
            ("EQEMU_USER", user),
            ("EQEMU_PASS", password),
            ("EQEMU_CHAR", name),
        )
        if not value
    ]
    if missing:
        raise SystemExit("set " + ", ".join(missing))
    creation = replace(build(), name=name)
    world = World(name=name)
    world.race = creation.race
    world.class_id = creation.class_id
    world.gender = creation.gender
    world.deity = creation.deity
    queue = Schedule()
    loop = Loop()
    client = loop.start(
        Login(character=name, user=user, password=password),
        creation,
        queue,
    )
    if not isinstance(client, Client):
        raise SystemExit("login did not open a zone session")

    flags = loop.journal.flag_values(name) if loop.journal is not None else {}
    world.tutorial_started = bool(flags.get("tutorial_started"))
    world.quest_started = bool(flags.get("quest_started"))
    _warm(client, world)
    log.info("playing %s", name)
    play(loop, client, world, queue)


def _warm(client: Client, world: World) -> None:
    """Read zone files and the quest graph before the first pulse.

    Pathing and line of sight otherwise decompress those files on the pulse that
    should be sending movement.
    """
    zone = _inbox_zone(client) or str(world.zone or "")
    if not zone and client.played is not None:
        zone = zone_name_of(int(client.played.zone_id or 0))
    if zone:
        nav = _quiet(load_nav, zone)
        water = _quiet(load_water, zone)
        zone_map = _quiet(load_map, zone)
        if water is not None:
            world.water_map = water
        log.info(
            "loaded %s nav=%s water=%s map=%s",
            zone,
            nav is not None,
            water is not None,
            zone_map is not None,
        )
    graph = _cached_graph()
    edges = 0 if graph is None else len(graph.edges)
    log.info("loaded quest graph edges=%s", edges)


def _inbox_zone(client: Client) -> str:
    number = client.opcodes.get("OP_NewZone", 0)
    if not number:
        return ""
    for opcode, payload in client._inbox:
        if opcode != number:
            continue
        try:
            short = OP_NewZone.deserialize(payload).short_name
        except ValueError:
            log.error("new zone packet failed to parse", exc_info=True)
            continue
        if short:
            return short
    return ""


def _quiet[T](load: Callable[[str], T], zone: str) -> T | None:
    try:
        return load(zone)
    except (OSError, ValueError):
        name = load.__name__ if isinstance(load, types.FunctionType) else "map"
        log.error("%s failed to load for %s", name, zone, exc_info=True)
        return None


def play(loop: Loop, client: Client, world: World, queue: Schedule) -> None:
    """One Loop for the whole session. Each pulse pumps, steps, and flushes."""
    bus = Bus(queue, world, loop)
    client.start_io()
    try:
        while True:
            loop.run_once(client, world, queue, bus)
            if client.closed:
                break
    except KeyboardInterrupt:
        return
    finally:
        client.close()


if __name__ == "__main__":
    main()
