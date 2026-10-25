"""UDP reliable stream, matching common/net/reliable_stream_connection.cpp.

Session multi-byte fields are big-endian. Application opcodes and bodies are
little-endian and are not part of this module. Login and world leave encode
passes at none. Zone defaults to zlib compression (Network:CompressZoneStream).
"""

from __future__ import annotations

import random
import select
import socket
import struct
import time
import zlib
from dataclasses import dataclass, field

from eqclient.crc import crc32

OP_SESSION_REQUEST = 0x01
OP_SESSION_RESPONSE = 0x02
OP_COMBINED = 0x03
OP_SESSION_DISCONNECT = 0x05
OP_KEEPALIVE = 0x06
OP_SESSION_STAT_REQUEST = 0x07
OP_SESSION_STAT_RESPONSE = 0x08
OP_PACKET = 0x09
OP_FRAGMENT = 0x0D
OP_OUT_OF_ORDER_ACK = 0x11
OP_ACK = 0x15
OP_APP_COMBINED = 0x19
OP_OUTBOUND_PING = 0x1C
OP_OUT_OF_SESSION = 0x1D

ENCODE_NONE = 0
ENCODE_COMPRESSION = 1
ENCODE_XOR = 4

SEQ_CURRENT = 0
SEQ_FUTURE = 1
SEQ_PAST = 2

_NO_CRC = {OP_SESSION_REQUEST, OP_SESSION_RESPONSE, OP_OUT_OF_SESSION}


class SessionError(RuntimeError):
    pass


def compare_sequence(expected: int, actual: int) -> int:
    diff = int(actual) - int(expected)
    if diff == 0:
        return SEQ_CURRENT
    if diff > 0:
        return SEQ_PAST if diff > 10000 else SEQ_FUTURE
    return SEQ_FUTURE if diff < -10000 else SEQ_PAST


def _compress(payload: bytes) -> bytes:
    if len(payload) > 30:
        compressed = zlib.compress(payload, 1)
        if len(compressed) <= len(payload):
            return bytes([0x5A]) + compressed
    return bytes([0xA5]) + payload


def _decompress(payload: bytes) -> bytes:
    if len(payload) < 2:
        return payload
    if payload[0] == 0x5A:
        return zlib.decompress(payload[1:])
    if payload[0] == 0xA5:
        return payload[1:]
    raise SessionError(f"unknown compression marker {payload[0]:#x}")


def _xor(payload: bytes, key: int, encode: bool) -> bytes:
    """Rolling 4-byte XOR from ReliableStreamConnection::Encode/Decode."""
    key &= 0xFFFFFFFF
    out = bytearray(payload)
    i = 0
    while i + 4 <= len(out):
        word = struct.unpack_from("<I", out, i)[0]
        mixed = (word ^ key) & 0xFFFFFFFF
        struct.pack_into("<I", out, i, mixed)
        key = mixed if encode else word
        i += 4
    kc = key & 0xFF
    for j in range(i, len(out)):
        out[j] ^= kc
    return bytes(out)


@dataclass
class _Sent:
    packet: bytes
    last_sent: float
    resend_delay: float = 0.15


@dataclass
class _Stream:
    sequence_in: int = 0
    sequence_out: int = 0
    queue: dict[int, bytes] = field(default_factory=dict)
    sent: dict[int, _Sent] = field(default_factory=dict)
    fragment: bytearray = field(default_factory=bytearray)
    fragment_total: int = 0


class Session:
    def __init__(self) -> None:
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._sock.setblocking(False)
        self._peer: tuple[str, int] | None = None
        self._connect_code = random.randrange(1, 0x7FFFFFFF)
        self.encode_key = 0
        self.crc_bytes = 0
        self.max_packet_size = 512
        self.encode_passes = (ENCODE_NONE, ENCODE_NONE)
        self.connected = False
        self.closed = False
        self._streams = [_Stream() for _ in range(4)]
        self._inbox: list[bytes] = []
        self._last_send = 0.0
        self._last_recv = 0.0

    def connect(self, host: str, port: int, timeout: float = 5.0) -> None:
        infos = socket.getaddrinfo(host, port, socket.AF_INET, socket.SOCK_DGRAM)
        if not infos:
            raise SessionError(f"could not resolve {host}")
        self._peer = (infos[0][4][0], port)
        deadline = time.monotonic() + timeout
        next_send = 0.0
        while time.monotonic() < deadline:
            now = time.monotonic()
            if now >= next_send:
                self._send_bytes(self._session_request(), crc=False)
                next_send = now + 0.5
            self._recv_once(min(0.2, deadline - time.monotonic()))
            if self.connected:
                return
        raise SessionError(f"session to {host}:{port} was not accepted")

    def close(self) -> None:
        if self.connected and not self.closed and self._peer is not None:
            packet = struct.pack(">BBI", 0, OP_SESSION_DISCONNECT, self._connect_code)
            try:
                self._send_bytes(packet, crc=True)
            except OSError:
                pass
        self.closed = True
        self.connected = False
        try:
            self._sock.close()
        except OSError:
            pass

    def send_app(self, packet: bytes) -> None:
        """Send one application datagram (opcode bytes already included)."""
        if not self.connected:
            raise SessionError("session is not connected")
        body = b"\x00" + packet if packet and packet[0] == 0 else packet
        self._send_reliable(0, body)
        self._recv_once(0)

    def pump(self, timeout: float) -> list[bytes]:
        """Read for up to timeout seconds. Returns newly arrived app packets."""
        deadline = time.monotonic() + timeout
        start = len(self._inbox)
        while time.monotonic() < deadline:
            self._resend()
            self._keepalive()
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                break
            self._recv_once(min(0.05, remaining))
        fresh = self._inbox[start:]
        return fresh

    def _session_request(self) -> bytes:
        return struct.pack(
            ">BBIII",
            0,
            OP_SESSION_REQUEST,
            3,
            self._connect_code,
            self.max_packet_size,
        )

    def _send_reliable(self, stream_id: int, payload: bytes) -> None:
        stream = self._streams[stream_id]
        header = struct.pack(">BBH", 0, OP_PACKET + stream_id, stream.sequence_out & 0xFFFF)
        packet = header + payload
        stream.sent[stream.sequence_out & 0xFFFF] = _Sent(packet, time.monotonic())
        stream.sequence_out = (stream.sequence_out + 1) & 0xFFFF
        self._send_bytes(packet, crc=True)

    def _send_ack(self, opcode: int, sequence: int) -> None:
        packet = struct.pack(">BBH", 0, opcode, sequence & 0xFFFF)
        self._send_bytes(packet, crc=True)

    def _keepalive(self) -> None:
        if not self.connected:
            return
        now = time.monotonic()
        if now - self._last_send < 5.0:
            return
        self._send_bytes(bytes((0, OP_KEEPALIVE)), crc=True)

    def _resend(self) -> None:
        now = time.monotonic()
        for stream in self._streams:
            for sent in list(stream.sent.values()):
                if now - sent.last_sent < sent.resend_delay:
                    continue
                self._send_bytes(sent.packet, crc=True)
                sent.last_sent = now
                sent.resend_delay = min(sent.resend_delay * 2, 5.0)

    def _send_bytes(self, packet: bytes, crc: bool) -> None:
        if self._peer is None:
            raise SessionError("session has no peer")
        out = packet
        if self.connected and any(self.encode_passes):
            out = self._apply_encode(out)
        if crc and self.crc_bytes:
            digest = crc32(out, self.encode_key)
            if self.crc_bytes == 2:
                out += struct.pack(">H", digest & 0xFFFF)
            elif self.crc_bytes == 4:
                out += struct.pack(">I", digest)
        self._sock.sendto(out, self._peer)
        self._last_send = time.monotonic()

    def _recv_once(self, timeout: float) -> None:
        readable, _, _ = select.select([self._sock], [], [], max(0.0, timeout))
        if not readable:
            return
        try:
            data, addr = self._sock.recvfrom(65535)
        except BlockingIOError:
            return
        if self._peer is None:
            self._peer = addr
        self._last_recv = time.monotonic()
        self._handle_datagram(data)

    def _handle_datagram(self, data: bytes) -> None:
        if len(data) < 2:
            return
        decoded = self._strip_and_decode(data)
        if decoded is None:
            return
        self._process_decoded(decoded)

    def _strip_and_decode(self, data: bytes) -> bytes | None:
        if not self._can_encode(data):
            return data
        if self.crc_bytes:
            if len(data) < self.crc_bytes:
                return None
            body = data[: -self.crc_bytes]
            actual = struct.unpack_from(">H" if self.crc_bytes == 2 else ">I", data, len(body))[0]
            expected = crc32(body, self.encode_key) & (0xFFFF if self.crc_bytes == 2 else 0xFFFFFFFF)
            if actual != expected:
                return None
            data = body
        try:
            return self._apply_decode(data)
        except zlib.error:
            return None

    def _can_encode(self, data: bytes) -> bool:
        if len(data) < 2 or not self.connected:
            return False
        if data[0] == 0 and data[1] in _NO_CRC:
            return False
        return True

    def _apply_encode(self, data: bytes) -> bytes:
        out = data
        for encode in self.encode_passes:
            out = self._apply_pass(out, encode, encode=True)
        return out

    def _apply_decode(self, data: bytes) -> bytes:
        out = data
        for encode in reversed(self.encode_passes):
            out = self._apply_pass(out, encode, encode=False)
        return out

    def _apply_pass(self, data: bytes, kind: int, encode: bool) -> bytes:
        if kind == ENCODE_NONE or len(data) < 2:
            return data
        offset = 2 if data[0] == 0 else 1
        head, payload = data[:offset], data[offset:]
        if kind == ENCODE_COMPRESSION:
            payload = _compress(payload) if encode else _decompress(payload)
        elif kind == ENCODE_XOR:
            payload = _xor(payload, self.encode_key, encode)
        return head + payload

    def _process_decoded(self, data: bytes) -> None:
        if not data:
            return
        if data[0] != 0:
            self._inbox.append(data)
            return
        if len(data) < 2:
            return
        opcode = data[1]
        if opcode == OP_SESSION_RESPONSE:
            self._on_session_response(data)
        elif opcode == OP_COMBINED:
            self._on_combined(data)
        elif opcode == OP_APP_COMBINED:
            self._on_app_combined(data)
        elif OP_PACKET <= opcode <= OP_PACKET + 3:
            self._on_reliable(data, opcode - OP_PACKET, fragment=False)
        elif OP_FRAGMENT <= opcode <= OP_FRAGMENT + 3:
            self._on_reliable(data, opcode - OP_FRAGMENT, fragment=True)
        elif OP_ACK <= opcode <= OP_ACK + 3:
            self._on_ack(opcode - OP_ACK, data, single=False)
        elif OP_OUT_OF_ORDER_ACK <= opcode <= OP_OUT_OF_ORDER_ACK + 3:
            self._on_ack(opcode - OP_OUT_OF_ORDER_ACK, data, single=True)
        elif opcode == OP_SESSION_STAT_REQUEST:
            self._on_stat_request(data)
        elif opcode == OP_SESSION_DISCONNECT:
            self.closed = True
            self.connected = False
        elif opcode == 0:
            if len(data) > 1:
                self._inbox.append(data[1:])
        elif opcode in (OP_KEEPALIVE, OP_OUTBOUND_PING, OP_SESSION_STAT_RESPONSE):
            return

    def _on_session_response(self, data: bytes) -> None:
        if len(data) < 17:
            return
        _zero, _op, code, key, crc_bytes, pass1, pass2, max_size = struct.unpack(">BBIIBBBI", data[:17])
        if code != self._connect_code:
            return
        self.encode_key = key
        self.crc_bytes = crc_bytes
        self.encode_passes = (pass1, pass2)
        self.max_packet_size = max_size or 512
        self.connected = True

    def _on_combined(self, data: bytes) -> None:
        offset = 2
        while offset < len(data):
            length = data[offset]
            offset += 1
            if offset + length > len(data):
                return
            self._process_decoded(data[offset : offset + length])
            offset += length

    def _on_app_combined(self, data: bytes) -> None:
        offset = 2
        end = len(data)
        while offset < end:
            if data[offset] == 0xFF:
                if offset + 3 > end:
                    return
                if data[offset + 1] == 0xFF and data[offset + 2] == 0xFF:
                    if offset + 7 > end:
                        return
                    length = struct.unpack_from(">I", data, offset + 3)[0]
                    offset += 7
                else:
                    length = struct.unpack_from(">H", data, offset + 1)[0]
                    offset += 3
            else:
                length = data[offset]
                offset += 1
            if offset + length > end:
                return
            self._process_decoded(data[offset : offset + length])
            offset += length

    def _on_reliable(self, data: bytes, stream_id: int, fragment: bool) -> None:
        if len(data) < 4:
            return
        sequence = struct.unpack_from(">H", data, 2)[0]
        stream = self._streams[stream_id]
        order = compare_sequence(stream.sequence_in, sequence)
        if order == SEQ_FUTURE:
            self._send_ack(OP_OUT_OF_ORDER_ACK + stream_id, sequence)
            stream.queue.setdefault(sequence, data)
            return
        if order == SEQ_PAST:
            self._send_ack(OP_ACK + stream_id, (stream.sequence_in - 1) & 0xFFFF)
            return
        stream.queue.pop(sequence, None)
        self._send_ack(OP_ACK + stream_id, stream.sequence_in)
        stream.sequence_in = (stream.sequence_in + 1) & 0xFFFF
        if fragment:
            self._consume_fragment(stream, data)
        else:
            self._process_decoded(data[4:])
        queued = stream.queue.pop(stream.sequence_in, None)
        if queued is not None:
            self._process_decoded(queued)

    def _consume_fragment(self, stream: _Stream, data: bytes) -> None:
        if stream.fragment_total == 0:
            if len(data) < 8:
                return
            stream.fragment_total = struct.unpack_from(">I", data, 4)[0]
            stream.fragment = bytearray(data[8:])
        else:
            stream.fragment += data[4:]
        if stream.fragment_total and len(stream.fragment) >= stream.fragment_total:
            whole = bytes(stream.fragment[: stream.fragment_total])
            stream.fragment = bytearray()
            stream.fragment_total = 0
            self._process_decoded(whole)

    def _on_ack(self, stream_id: int, data: bytes, single: bool) -> None:
        if len(data) < 4:
            return
        sequence = struct.unpack_from(">H", data, 2)[0]
        stream = self._streams[stream_id]
        if single:
            stream.sent.pop(sequence, None)
            return
        for seq in list(stream.sent):
            if compare_sequence(sequence, seq) != SEQ_FUTURE:
                stream.sent.pop(seq, None)

    def _on_stat_request(self, data: bytes) -> None:
        if len(data) < 40 or self._peer is None:
            return
        # Echo the request header and zero the counters. The server only uses this for stats.
        reply = bytearray(data[:40])
        reply[1] = OP_SESSION_STAT_RESPONSE
        self._send_bytes(bytes(reply), crc=True)
