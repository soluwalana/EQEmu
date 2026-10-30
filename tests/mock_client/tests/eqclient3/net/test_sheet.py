"""build fills the sheet before any packet leaves."""

from __future__ import annotations

import socket

import pytest

from eqclient3.net.sheet import CharacterError, build


def test_build_fills_stats_deity_and_home_city():
    human = build(1, 1, 0)
    elf = build(6, 1, 0)
    assert human.stats == (110, 85, 80, 75, 75, 75, 75)
    assert human.deity == 396
    assert human.start_zone == 1
    assert elf.race_name == "dark elf"
    assert elf.stats == (95, 75, 95, 75, 83, 99, 60)
    assert elf.deity == 206
    assert elf.start_zone == 5


def test_env_defaults(monkeypatch):
    monkeypatch.setenv("EQEMU_RACE", "6")
    monkeypatch.setenv("EQEMU_CLASS", "1")
    monkeypatch.setenv("EQEMU_GENDER", "1")
    monkeypatch.setenv("EQEMU_DEITY", "201")
    monkeypatch.setenv("EQEMU_START_ZONE", "9")
    sheet = build()
    assert (sheet.race, sheet.class_id, sheet.gender) == (6, 1, 1)
    assert sheet.deity == 201
    assert sheet.start_zone == 9


def test_illegal_pair_raises_before_a_packet(monkeypatch):
    opened: list = []
    real = socket.socket

    def track(*args, **kwargs):
        opened.append(args)
        return real(*args, **kwargs)

    monkeypatch.setattr(socket, "socket", track)
    with pytest.raises(CharacterError, match="dark elf cannot be a paladin"):
        build(6, 3, 0)
    from eqclient3.net.client import connect

    with pytest.raises(CharacterError, match="dark elf cannot be a paladin"):
        connect(
            {
                "host": "127.0.0.1",
                "user": "tester",
                "password": "secret",
                "character": "Velkyn",
                "race": 6,
                "class_id": 3,
                "gender": 0,
            }
        )
    assert opened == []
