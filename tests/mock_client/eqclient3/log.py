"""Shared logger and a one-line writer.

LOG_LEVEL names the level: DEBUG, INFO, WARNING, ERROR, or CRITICAL.
The default is INFO. Each line starts with the date and time.
"""

from __future__ import annotations

import logging
import os
import sys
from typing import TextIO

log = logging.getLogger("eqclient3")

_LEVELS = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR,
    "CRITICAL": logging.CRITICAL,
}


def configure() -> None:
    """Apply LOG_LEVEL and a timestamp to every line."""
    level = _LEVELS.get(os.environ.get("LOG_LEVEL", "INFO").strip().upper(), logging.INFO)
    log.setLevel(level)
    logging.basicConfig(
        level=level,
        format="%(asctime)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        stream=sys.stderr,
    )


configure()


def write(message: str, stream: TextIO | None = None) -> None:
    """Write one line. Embedded newlines become spaces."""
    target = sys.stderr if stream is None else stream
    line = " ".join(str(message).splitlines())
    target.write(line + "\n")
    target.flush()
