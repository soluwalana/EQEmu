"""Bus bytes land in a capture database, ordered by character, time, and opcode."""

from eqclient3.action import Action
from eqclient3.bus import Bus
from eqclient3.capture import Capture, capture_path, open_capture
from eqclient3.loop import Loop, ScriptedSession
from eqclient3.schedule import Schedule
from eqclient3.world import World


def test_rows_are_stored_by_character_time_and_opcode(tmp_path):
    path = tmp_path / "bus.sqlite3"
    capture = Capture(path, "Entoen")
    try:
        capture.record("recv", "OP_ChannelMessage", b"hail")
        capture.record("send", "OP_ChannelMessage", b"^botsummon")
        capture.record("recv", "OP_SpecialMesg", b"Summoned 5 bots to you.")
        capture.record("send", "OP_ClientUpdate", 1)
        capture.commit()
        stored = capture.packets()
        assert [row.direction for row in stored] == ["recv", "send", "recv"]
        assert stored[0].payload == b"hail"
        assert stored[1].opcode == "OP_ChannelMessage"
        channel = capture.packets("OP_ChannelMessage")
        assert [row.direction for row in channel] == ["recv", "send"]
        assert capture.packets("OP_SpecialMesg")[0].payload == b"Summoned 5 bots to you."
    finally:
        capture.close()

    again = Capture(path, "Entoen")
    try:
        assert [row.opcode for row in again.packets()] == [
            "OP_ChannelMessage",
            "OP_ChannelMessage",
            "OP_SpecialMesg",
        ]
    finally:
        again.close()


def test_a_pulse_records_the_recv_and_the_send(tmp_path):
    world = World(name="Entoen")
    queue = Schedule()
    session = ScriptedSession([("OP_SpecialMesg", b"arrived")])
    loop = Loop()
    capture = Capture(tmp_path / "bus.sqlite3", "Entoen")
    loop.capture = capture

    class Send(Action):
        def step(self, loop: Loop, world: World) -> None:
            loop.send("OP_ChannelMessage", b"^follow")
            self.complete = True

    queue.append(Send(), world)
    try:
        loop.run_once(session, world, queue, Bus(queue))
        rows = capture.packets()
    finally:
        loop.close_capture()
    assert rows[0].direction == "recv"
    assert rows[0].opcode == "OP_SpecialMesg"
    assert rows[0].payload == b"arrived"
    sent = [row for row in rows if row.direction == "send" and row.opcode == "OP_ChannelMessage"]
    assert [row.payload for row in sent] == [b"^follow"]


def test_the_default_file_sits_next_to_the_bus_log(tmp_path, monkeypatch):
    monkeypatch.delenv("EQEMU_CAPTURE", raising=False)
    monkeypatch.delenv("EQEMU_BUS_LOG", raising=False)
    monkeypatch.setenv("HOME", str(tmp_path))
    assert capture_path("Entoen") == tmp_path / ".eqclient" / "logs" / "Entoen" / "bus.sqlite3"
    monkeypatch.setenv("EQEMU_BUS_LOG", str(tmp_path / "logs" / "bus.log"))
    assert capture_path("Entoen") == tmp_path / "logs" / "bus.sqlite3"


def test_a_test_run_does_not_open_the_home_file(monkeypatch):
    monkeypatch.delenv("EQEMU_CAPTURE", raising=False)
    assert open_capture("Entoen") is None


def test_an_explicit_path_opens_during_a_test(tmp_path, monkeypatch):
    monkeypatch.setenv("EQEMU_CAPTURE", str(tmp_path / "bus.sqlite3"))
    capture = open_capture("Entoen")
    assert capture is not None
    capture.close()
