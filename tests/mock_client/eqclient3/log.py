"""One line writer."""

from __future__ import annotations

from typing import TextIO
import sys


def write(message: str, stream: TextIO | None = None) -> None:
    """Write one line. Embedded newlines become spaces."""
    target = sys.stderr if stream is None else stream
    line = " ".join(str(message).splitlines())
    target.write(line + "\n")
    target.flush()
