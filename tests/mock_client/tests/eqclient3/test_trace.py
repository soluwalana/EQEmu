"""Bus trace file: one opcode line, and one line per handler that runs."""

from eqclient3.bus import Bus
from eqclient3.handler import Handler
from eqclient3.structs import OP_Assist


class Ping(Handler):
    opcodes = ("OP_Ping",)

    def on(self, opcode, payload):
        self.opcode = opcode
        self.payload = payload


def test_each_opcode_and_handler_is_one_line(tmp_path, monkeypatch):
    path = tmp_path / "bus.log"
    monkeypatch.setenv("EQEMU_BUS_LOG", str(path))
    bus = Bus(autoload=False)
    handler = Ping()
    bus.register(handler)
    bus.publish("OP_Ping", b"abcd")
    bus.publish("OP_Other", b"")
    text = path.read_text()
    assert "opcode OP_Ping bytes=4" in text
    assert "handler " not in text
    assert "opcode OP_Other bytes=0" in text
    assert not hasattr(handler, "opcode")
    bus.publish("OP_Ping", OP_Assist(1))
    text = path.read_text()
    assert "handler Ping OP_Ping" in text
    assert text.count("handler ") == 1
    assert handler.opcode == "OP_Ping"
