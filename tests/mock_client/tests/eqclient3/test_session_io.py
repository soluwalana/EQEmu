"""Send and receive use separate queues. The loop only sees the queues."""

import socket

from eqclient3.net.session import Session


def test_queued_send_does_not_read_and_pump_reads_the_receiver_queue():
    session = Session()
    session.connected = True
    session._peer = ("127.0.0.1", 9)
    session._io = True
    sent = []
    session._send_bytes = lambda packet, crc: sent.append(packet)

    session.send_app(b"\x01\x02hi")

    assert sent == []
    assert session._outbound.qsize() == 1
    session._inbound.put(b"\x99hello")
    assert session.pump(0) == [b"\x99hello"]
    session._io = False
    session.close()


def test_writer_and_reader_run_on_separate_threads():
    session = Session()
    other = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    other.bind(("127.0.0.1", 0))
    session._peer = other.getsockname()
    session.connected = True
    try:
        session.start_channels()
        session.send_app(b"\x34ping")
        other.settimeout(1.0)
        outbound, addr = other.recvfrom(65535)
        assert outbound
        other.sendto(b"\x34pong", addr)
        inbound = session.pump(1.0)
        assert any(packet.endswith(b"pong") or b"pong" in packet for packet in inbound)
    finally:
        session.close()
        other.close()
