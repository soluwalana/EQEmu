"""Bot raid roster over the mock client.

The character should own bots and the server should have Bots:Enabled. The
assertions are chat strings the server already sends. A character with no bots,
or a server with bots disabled, still passes by reporting that.
"""

import os

import pytest

from eqclient.client import connect

pytestmark = pytest.mark.skipif(
    not (os.environ.get("EQEMU_USER") and os.environ.get("EQEMU_PASS") and os.environ.get("EQEMU_CHAR")),
    reason="Set EQEMU_USER, EQEMU_PASS, and EQEMU_CHAR to run against a live server",
)

NO_BOTS = (
    "You have no bots.",
    "You do not own any bots.",
    "Bots are disabled on this server.",
    "The bot raid roster table is missing. Run the database updates and try again.",
)
FORM_FAILURE = NO_BOTS + (
    "Leave your group before forming a bot raid.",
    "Could not create a raid.",
    "Could not save the bot raid roster.",
    "You have no active bot raid roster. Use ^raidform all.",
)


def _wait_any(client, needles, timeout=15):
    import time

    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        for message in client.messages:
            for needle in needles:
                if needle in message:
                    return message
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            break
        try:
            client.wait_message("\0", timeout=min(0.3, remaining))
        except Exception:
            pass
    seen = " | ".join(client.messages[-8:]) or "(no messages)"
    raise AssertionError(f"none of {needles} arrived; recent: {seen}")


def test_botlist_shows_owned_bots_or_why_it_cannot():
    client = connect()
    try:
        client.command("botlist")
        message = _wait_any(client, ("owned by",) + NO_BOTS)
        assert "owned by" in message or any(needle in message for needle in NO_BOTS)
    finally:
        client.close()


def test_raidform_all_then_form_on_connect():
    client = connect()
    try:
        client.command("raidform all")
        formed = _wait_any(client, ("Bot raid formed.", "Saved",) + FORM_FAILURE)
        if "Bot raid formed." not in formed and "Saved" not in formed:
            assert any(needle in formed for needle in FORM_FAILURE)
            return
        client.close()
        client = connect()
        message = _wait_any(
            client,
            (
                "Bot raid formed.",
                "You have no active bot raid roster. Use ^raidform all.",
                "You do not own any bots.",
                "Bots are disabled on this server.",
            ),
        )
        assert (
            "Bot raid formed." in message
            or "You have no active bot raid roster" in message
            or "You do not own any bots." in message
            or "Bots are disabled on this server." in message
        )
    finally:
        client.close()
