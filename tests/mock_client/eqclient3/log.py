"""Shared logger and a one-line writer.

LOG_LEVEL names the level: DEBUG, INFO, WARNING, ERROR, or CRITICAL.
The default is INFO. Each line starts with the date and time.

A character session also appends to ~/.eqclient/logs/<character>/agent.log.
"""

from __future__ import annotations

import logging
import os
import sys
from pathlib import Path
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
    """Apply LOG_LEVEL and a timestamp to every line, and the character log file."""
    level = _LEVELS.get(os.environ.get("LOG_LEVEL", "INFO").strip().upper(), logging.INFO)
    log.setLevel(level)
    logging.basicConfig(
        level=level,
        format="%(asctime)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        stream=sys.stderr,
    )
    _character_file(level)


def _character_file(level: int) -> None:
    """Append the same lines to the character log. Tests and a nameless run skip this."""
    if os.environ.get("PYTEST_CURRENT_TEST"):
        return
    name = os.environ.get("EQEMU_CHAR", "").strip()
    if not name:
        return
    path = Path.home() / ".eqclient" / "logs" / name / "agent.log"
    path.parent.mkdir(parents=True, exist_ok=True)
    for handler in log.handlers:
        if isinstance(handler, logging.FileHandler) and Path(handler.baseFilename) == path:
            return
    handle = logging.FileHandler(path, encoding="utf-8")
    handle.setLevel(level)
    handle.setFormatter(logging.Formatter("%(asctime)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S"))
    log.addHandler(handle)


configure()


def write(message: str, stream: TextIO | None = None) -> None:
    """Write one line. Embedded newlines become spaces."""
    target = sys.stderr if stream is None else stream
    line = " ".join(str(message).splitlines())
    target.write(line + "\n")
    target.flush()
