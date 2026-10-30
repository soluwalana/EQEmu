"""The client packages live next to this tree, under mock_client."""

from __future__ import annotations

import sys
from pathlib import Path

TESTS = Path(__file__).resolve().parent
MOCK = TESTS.parent
for path in (
    TESTS / "eqclient1",
    TESTS / "eqclient3",
    MOCK,
):
    text = str(path)
    if text not in sys.path:
        sys.path.insert(0, text)
