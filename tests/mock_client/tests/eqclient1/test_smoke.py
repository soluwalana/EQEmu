"""Live smoke test. Skipped unless a server and an account are configured."""

import os

import pytest

from eqclient.client import connect

pytestmark = pytest.mark.skipif(
    not (os.environ.get("EQEMU_USER") and os.environ.get("EQEMU_PASS") and os.environ.get("EQEMU_CHAR")),
    reason="Set EQEMU_USER, EQEMU_PASS, and EQEMU_CHAR to run against a live server",
)


def test_say_is_echoed():
    client = connect()
    try:
        text = "integration smoke"
        client.say(text)
        echo = client.wait_message(text, timeout=10)
        assert text in echo
    finally:
        client.close()
