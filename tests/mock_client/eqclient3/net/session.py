"""UDP reliable stream, matching common/net/reliable_stream_connection.cpp.

Session multi-byte fields are big-endian. Application opcodes and bodies are
little-endian and are not part of this module. Login and world leave encode
passes at none. Zone defaults to zlib compression (Network:CompressZoneStream).
"""

from __future__ import annotations

import queue
import random
import select
import socket
import struct
import threading
import time
import zlib
from dataclasses import dataclass, field

from eqclient3.net.crc import crc32
from eqclient3.structs import (
    OP_ACK as Ack,
    OP_APP_COMBINED as AppCombined,
    OP_COMBINED as Combined,
    OP_FRAGMENT as Fragment,
    OP_KEEPALIVE as Keepalive,
    OP_OUT_OF_ORDER_ACK as OutOfOrderAck,
    OP_OUT_OF_SESSION as OutOfSession,
    OP_PACKET as ReliablePacket,
    OP_SESSION_DISCONNECT as SessionDisconnect,
    OP_SESSION_REQUEST as SessionRequest,
    OP_SESSION_RESPONSE as SessionResponse,
    OP_SESSION_STAT_REQUEST as SessionStatRequest,
    OP_SESSION_STAT_RESPONSE as SessionStatResponse,
)

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
RESEND_WINDOW = 30.0
DECODE_FAIL_LIMIT = 8


def gap_needs_rezone(queued_for: float, decode_failures: int) -> bool:
    """A hole that outlived the server resend window, or a run of undecodable datagrams."""
    return queued_for >= RESEND_WINDOW or decode_failures >= DECODE_FAIL_LIMIT

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
    gap_since: float = 0.0


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
        self.open = True
        self._streams = [_Stream() for _ in range(4)]
        self._inbox: list[bytes] = []
        self._cursor = 0
        self._last_send = 0.0
        self._last_recv = 0.0
        self._decode_failures = 0
        self.needs_rezone = False
        self._lock = threading.RLock()
        self._outbound: queue.Queue = queue.Queue()
        self._inbound: queue.Queue = queue.Queue()
        self._io = False
        self._stop = threading.Event()
        self._writer: threading.Thread | None = None
        self._reader: threading.Thread | None = None

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

    def start_channels(self) -> None:
        """Writer and receiver threads. The play loop only sees the two queues.

        Handshake stays on this thread. start_channels runs after zone-in.
        """
        if self._io or self.closed or not self.connected:
            return
        with self._lock:
            pending = self._inbox[self._cursor :]
            self._inbox.clear()
            self._cursor = 0
        for packet in pending:
            self._inbound.put(packet)
        self._stop.clear()
        self._io = True
        self._writer = threading.Thread(target=self._writer_loop, name="eq-writer", daemon=True)
        self._reader = threading.Thread(target=self._reader_loop, name="eq-reader", daemon=True)
        self._writer.start()
        self._reader.start()

    def stop_channels(self) -> None:
        if not self._io:
            return
        self._stop.set()
        self._outbound.put(None)
        writer = self._writer
        reader = self._reader
        if writer is not None:
            writer.join(timeout=1.0)
        if reader is not None:
            reader.join(timeout=1.0)
        self._writer = None
        self._reader = None
        self._io = False

    def close(self) -> None:
        self.stop_channels()
        if self.connected and not self.closed and self._peer is not None:
            packet = SessionDisconnect(self._connect_code).serialize()
            try:
                self._send_bytes(packet, crc=True)
            except OSError:
                pass
        self.closed = True
        self.open = False
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
        if self._io:
            self._outbound.put(body)
            return
        self._send_reliable(0, body)
        self._drain_ready()

    def pump(self, timeout: float) -> list[bytes]:
        """Read for up to timeout seconds. Returns newly arrived app packets."""
        if self._io:
            return self._pump_inbound(timeout)
        if self._cursor:
            del self._inbox[: self._cursor]
            self._cursor = 0
        deadline = time.monotonic() + max(0.0, timeout)
        while True:
            self._resend()
            self._keepalive()
            self._drain_ready()
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                # A zero timeout still takes every datagram already queued.
                while self._recv_once(0):
                    self._drain_ready()
                break
            self._recv_once(min(0.05, remaining))
        fresh = self._inbox[self._cursor :]
        self._cursor = len(self._inbox)
        for stream in self._streams:
            self._check_gap(stream)
        return fresh

    def _pump_inbound(self, timeout: float) -> list[bytes]:
        """App packets the receiver already queued. Does not touch the socket."""
        deadline = time.monotonic() + max(0.0, timeout)
        found: list[bytes] = []
        while True:
            remaining = deadline - time.monotonic()
            if found or remaining <= 0:
                try:
                    found.append(self._inbound.get_nowait())
                    continue
                except queue.Empty:
                    break
            try:
                found.append(self._inbound.get(timeout=remaining))
            except queue.Empty:
                break
        with self._lock:
            for stream in self._streams:
                self._check_gap(stream)
        return found

    def _writer_loop(self) -> None:
        """Sends, resends, and the 5s keepalive. Never reads the socket."""
        while not self._stop.is_set():
            try:
                item = self._outbound.get(timeout=0.05)
            except queue.Empty:
                item = None
            if item is None and self._stop.is_set():
                return
            try:
                with self._lock:
                    if self.closed or not self.connected:
                        return
                    self._resend()
                    self._keepalive()
                    if item is None:
                        continue
                    if isinstance(item, tuple):
                        self._send_bytes(item[1], crc=True)
                    else:
                        self._send_reliable(0, item)
            except (SessionError, OSError):
                self.connected = False
                self.closed = True
                self.needs_rezone = True
                return

    def _reader_loop(self) -> None:
        """Reads the socket and queues app packets. Acks go to the writer."""
        while not self._stop.is_set():
            try:
                readable, _, _ = select.select([self._sock], [], [], 0.05)
            except (OSError, ValueError):
                return
            if not readable:
                continue
            try:
                data, addr = self._sock.recvfrom(65535)
            except (BlockingIOError, OSError):
                continue
            with self._lock:
                if self._peer is None:
                    self._peer = addr
                self._last_recv = time.monotonic()
                self._handle_datagram(data)

    def _session_request(self) -> bytes:
        return SessionRequest(3, self._connect_code, self.max_packet_size).serialize()

    def _send_reliable(self, stream_id: int, payload: bytes) -> None:
        stream = self._streams[stream_id]
        self._wait_for_ack_room(stream)
        packet = ReliablePacket(stream_id, stream.sequence_out, payload).serialize()
        stream.sent[stream.sequence_out & 0xFFFF] = _Sent(packet, time.monotonic())
        stream.sequence_out = (stream.sequence_out + 1) & 0xFFFF
        self._send_bytes(packet, crc=True)

    def _send_ack(self, opcode: int, sequence: int) -> None:
        if OP_OUT_OF_ORDER_ACK <= opcode <= OP_OUT_OF_ORDER_ACK + 3:
            packet = OutOfOrderAck(opcode - OP_OUT_OF_ORDER_ACK, sequence).serialize()
        else:
            packet = Ack(opcode - OP_ACK, sequence).serialize()
        if self._io:
            self._outbound.put(("raw", packet))
            return
        self._send_bytes(packet, crc=True)

    def _wait_for_ack_room(self, stream: _Stream) -> None:
        """Stay inside the server's receive window. Packets read here stay queued."""
        deadline = time.monotonic() + 2.0
        while len(stream.sent) > 30 and time.monotonic() < deadline and self.connected and (not self._stop.is_set()):
            if self._io:
                self._lock.release()
                time.sleep(0.02)
                self._lock.acquire()
                continue
            self._resend()
            self._keepalive()
            self._drain_ready()
            self._recv_once(0.02)

    def _drain_ready(self) -> None:
        while self.connected or self._peer is not None:
            readable, _, _ = select.select([self._sock], [], [], 0)
            if not readable:
                return
            self._recv_once(0)

    def _keepalive(self) -> None:
        if not self.connected:
            return
        now = time.monotonic()
        if now - self._last_send < 5.0:
            return
        self._send_bytes(Keepalive().serialize(), crc=True)

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

    def _recv_once(self, timeout: float) -> bool:
        readable, _, _ = select.select([self._sock], [], [], max(0.0, timeout))
        if not readable:
            return False
        try:
            data, addr = self._sock.recvfrom(65535)
        except BlockingIOError:
            return False
        if self._peer is None:
            self._peer = addr
        self._last_recv = time.monotonic()
        self._handle_datagram(data)
        return True

    def _handle_datagram(self, data: bytes) -> None:
        if len(data) < 2:
            return
        decoded = self._strip_and_decode(data)
        if decoded is None:
            return
        self._decode_failures = 0
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
                self._note_decode_failure()
                return None
            data = body
        try:
            return self._apply_decode(data)
        except zlib.error:
            self._note_decode_failure()
            return None

    def _note_decode_failure(self) -> None:
        self._decode_failures += 1
        if gap_needs_rezone(0.0, self._decode_failures):
            self.needs_rezone = True

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
            self._deliver(data)
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
        elif opcode == OP_OUT_OF_SESSION:
            try:
                OutOfSession.deserialize(data)
            except ValueError:
                return
            self.closed = True
            self.connected = False
        elif opcode == 0:
            if len(data) > 1:
                self._deliver(data[1:])
        elif opcode in (OP_KEEPALIVE, OP_OUTBOUND_PING, OP_SESSION_STAT_RESPONSE):
            return

    def _on_session_response(self, data: bytes) -> None:
        try:
            reply = SessionResponse.deserialize(data)
        except ValueError:
            return
        if reply.connect_code != self._connect_code:
            return
        self.encode_key = reply.encode_key
        self.crc_bytes = reply.crc_bytes
        self.encode_passes = (reply.encode_pass1, reply.encode_pass2)
        self.max_packet_size = reply.max_packet_size or 512
        self.connected = True

    def _on_combined(self, data: bytes) -> None:
        for part in Combined.deserialize(data).parts:
            self._process_decoded(part)

    def _on_app_combined(self, data: bytes) -> None:
        for part in AppCombined.deserialize(data).parts:
            self._process_decoded(part)

    def _on_reliable(self, data: bytes, stream_id: int, fragment: bool) -> None:
        try:
            header = Fragment.deserialize(data) if fragment else ReliablePacket.deserialize(data)
        except ValueError:
            return
        sequence = header.sequence
        stream = self._streams[stream_id]
        order = compare_sequence(stream.sequence_in, sequence)
        if order == SEQ_FUTURE:
            self._send_ack(OP_OUT_OF_ORDER_ACK + stream_id, sequence)
            stream.queue.setdefault(sequence, data)
            if stream.gap_since <= 0.0:
                stream.gap_since = time.monotonic()
            self._check_gap(stream)
            return
        if order == SEQ_PAST:
            self._send_ack(OP_ACK + stream_id, (stream.sequence_in - 1) & 0xFFFF)
            return
        # Deliver in-order frames iteratively — a long catch-up queue must not recurse.
        frame = data
        is_frag = fragment
        while frame is not None and len(frame) >= 4:
            try:
                seq = (Fragment if is_frag else ReliablePacket).deserialize(frame).sequence
            except ValueError:
                break
            stream.queue.pop(seq, None)
            self._send_ack(OP_ACK + stream_id, stream.sequence_in)
            stream.sequence_in = (stream.sequence_in + 1) & 0xFFFF
            if is_frag:
                self._consume_fragment(stream, frame)
            else:
                self._process_decoded(frame[4:])
            frame = stream.queue.pop(stream.sequence_in, None)
            if frame is None or len(frame) < 2 or frame[0] != 0:
                break
            op = frame[1]
            if OP_FRAGMENT <= op <= OP_FRAGMENT + 3:
                is_frag = True
            elif OP_PACKET <= op <= OP_PACKET + 3:
                is_frag = False
            else:
                break
        if stream.sequence_in not in stream.queue and not any(
            compare_sequence(stream.sequence_in, queued) == SEQ_FUTURE for queued in stream.queue
        ):
            stream.gap_since = 0.0

    def _check_gap(self, stream: _Stream) -> None:
        if stream.gap_since <= 0.0:
            return
        queued_for = time.monotonic() - stream.gap_since
        if gap_needs_rezone(queued_for, self._decode_failures):
            self.needs_rezone = True

    def _consume_fragment(self, stream: _Stream, data: bytes) -> None:
        try:
            frag = Fragment.deserialize(data)
        except ValueError:
            return
        if stream.fragment_total == 0:
            if len(frag.data) < 4:
                return
            stream.fragment_total = int.from_bytes(frag.data[:4], "big")
            stream.fragment = bytearray(frag.data[4:])
        else:
            stream.fragment += frag.data
        if stream.fragment_total and len(stream.fragment) >= stream.fragment_total:
            whole = bytes(stream.fragment[: stream.fragment_total])
            stream.fragment = bytearray()
            stream.fragment_total = 0
            self._process_decoded(whole)

    def _on_ack(self, stream_id: int, data: bytes, single: bool) -> None:
        try:
            sequence = (OutOfOrderAck if single else Ack).deserialize(data).sequence
        except ValueError:
            return
        stream = self._streams[stream_id]
        if single:
            stream.sent.pop(sequence, None)
            return
        for seq in list(stream.sent):
            if compare_sequence(sequence, seq) != SEQ_FUTURE:
                stream.sent.pop(seq, None)

    def _on_stat_request(self, data: bytes) -> None:
        if self._peer is None:
            return
        try:
            request = SessionStatRequest.deserialize(data)
        except ValueError:
            return
        raw = SessionStatResponse(
            request.timestamp,
            int(time.monotonic() * 1000) & 0xFFFFFFFF,
            request.packets_sent,
            request.packets_recv,
            0,
            0,
        ).serialize()
        if self._io:
            self._outbound.put(("raw", raw))
            return
        self._send_bytes(raw, crc=True)

    def _deliver(self, packet: bytes) -> None:
        if self._io:
            self._inbound.put(packet)
            return
        self._inbox.append(packet)
