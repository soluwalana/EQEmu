"""Log in, zone in, and pulse until the zone session closes.

From the agent directory, or with it on PYTHONPATH:

    EQEMU_USER=... EQEMU_PASS=... EQEMU_CHAR=Hero python -m eqclient4

EQEMU_HOST defaults to 127.0.0.1. EQEMU_LOGIN_PORT defaults to 5999 and
EQEMU_WORLD_PORT to 9000. A name the server does not have yet is created
from EQEMU_RACE, EQEMU_CLASS, EQEMU_GENDER, EQEMU_DEITY, and EQEMU_START_ZONE.
LOG_LEVEL defaults to INFO. DEBUG also prints movement packets.
"""

import os
from dataclasses import replace

from eqclient4.loop import Loop
from eqclient4.net.client import Login
from eqclient4.net.sheet import build
from eqclient4.world import World


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

    world = World(name)

    loop = Loop(world, Login(character=name, user=user, password=password), creation)

    if not loop.client:
        raise SystemExit("login did not open a zone session")

    loop.warm()
    loop.play()
