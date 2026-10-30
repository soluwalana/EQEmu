"""A UDP peer that speaks the session handshake the client actually uses."""

from __future__ import annotations

import struct
import threading

OP_SESSION_REQUEST = 0x01
OP_SESSION_RESPONSE = 0x02
OP_SESSION_DISCONNECT = 0x05
OP_PACKET = 0x09
OP_ACK = 0x15


class Peer:
    def __init__(self) -> None:
        import socket

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(("127.0.0.1", 0))
        self.port = self.sock.getsockname()[1]
        self.apps: list[tuple[int, bytes]] = []
        self.disconnects = 0
        self._peer = None
        self._seq = 0
        self._once: dict[int, list] = {}
        self._always: dict[int, list] = {}
        self._lock = threading.Lock()
        self._running = True
        self.sock.settimeout(0.05)
        self._thread = threading.Thread(target=self._loop, daemon=True)
        self._thread.start()

    def once(self, opcode: int, fn) -> None:
        self._once.setdefault(opcode, []).append(fn)

    def always(self, opcode: int, fn) -> None:
        self._always.setdefault(opcode, []).append(fn)

    def reply(self, opcode: int, payload: bytes) -> None:
        if self._peer is None:
            return
        app = struct.pack("<H", opcode) + payload
        if app[:1] == b"\x00":
            app = b"\x00" + app
        packet = struct.pack(">BBH", 0, OP_PACKET, self._seq & 0xFFFF) + app
        self._seq = (self._seq + 1) & 0xFFFF
        self._send(packet)

    def stop(self) -> None:
        self._running = False
        try:
            self.sock.close()
        except OSError:
            pass
        self._thread.join(timeout=1.0)

    def _send(self, packet: bytes) -> None:
        if not self._running or self._peer is None:
            return
        try:
            self.sock.sendto(packet, self._peer)
        except OSError:
            return

    def _loop(self) -> None:
        while self._running:
            try:
                data, addr = self.sock.recvfrom(65535)
            except (TimeoutError, OSError):
                continue
            self._handle(data, addr)

    def _handle(self, data: bytes, addr) -> None:
        if len(data) < 2 or data[0] != 0:
            return
        opcode = data[1]
        if opcode == OP_SESSION_DISCONNECT:
            with self._lock:
                self.disconnects += 1
            return
        self._peer = addr
        if opcode == OP_SESSION_REQUEST and len(data) >= 14:
            _zero, _op, _unk, code, _max = struct.unpack(">BBIII", data[:14])
            self._seq = 0
            self._send(_response(code))
            return
        if opcode != OP_PACKET or len(data) < 4:
            return
        sequence = struct.unpack_from(">H", data, 2)[0]
        self._send(struct.pack(">BBH", 0, OP_ACK, sequence))
        app = data[4:]
        if app[:1] == b"\x00" and len(app) > 2:
            app = app[1:]
        if len(app) < 2:
            return
        app_op = struct.unpack_from("<H", app)[0]
        payload = app[2:]
        with self._lock:
            self.apps.append((app_op, payload))
        for fn in self._always.get(app_op, ()):
            fn(self, payload)
        waiting = self._once.get(app_op)
        if waiting:
            fn = waiting.pop(0)
            fn(self, payload)


def _response(code: int) -> bytes:
    return struct.pack(">BBIIBBBI", 0, OP_SESSION_RESPONSE, code, 0, 0, 0, 0, 4096)
