import struct
from dataclasses import dataclass

from eqclient4.structs.wire import EQStruct, need

OP_SESSION_REQUEST_ID = 0x01
OP_SESSION_RESPONSE_ID = 0x02
OP_COMBINED_ID = 0x03
OP_SESSION_DISCONNECT_ID = 0x05
OP_KEEPALIVE_ID = 0x06
OP_SESSION_STAT_REQUEST_ID = 0x07
OP_SESSION_STAT_RESPONSE_ID = 0x08
OP_PACKET_ID = 0x09
OP_FRAGMENT_ID = 0x0D
OP_OUT_OF_ORDER_ACK_ID = 0x11
OP_ACK_ID = 0x15
OP_APP_COMBINED_ID = 0x19
OP_OUTBOUND_PING_ID = 0x1C
OP_OUT_OF_SESSION_ID = 0x1D


@dataclass
class OP_SESSION_REQUEST(EQStruct):
    protocol_version: int = 3
    connect_code: int = 0
    max_packet_size: int = 512

    def serialize(self) -> bytes:
        # common/net/reliable_stream_structs.h:43 ReliableStreamConnect
        return struct.pack(
            ">BBIII",
            0,
            OP_SESSION_REQUEST_ID,
            self.protocol_version & 0xFFFFFFFF,
            self.connect_code & 0xFFFFFFFF,
            self.max_packet_size & 0xFFFFFFFF,
        )

    @classmethod
    def deserialize(cls, data: bytes) -> OP_SESSION_REQUEST:
        need(data, 14, "OP_SESSION_REQUEST")
        _zero, _opcode, version, code, max_size = struct.unpack(">BBIII", data[:14])
        return cls(int(version), int(code), int(max_size))


@dataclass
class OP_SESSION_RESPONSE(EQStruct):
    connect_code: int
    encode_key: int
    crc_bytes: int
    encode_pass1: int
    encode_pass2: int
    max_packet_size: int

    def serialize(self) -> bytes:
        # common/net/reliable_stream_structs.h:63 ReliableStreamConnectReply
        return struct.pack(
            ">BBIIBBBI",
            0,
            OP_SESSION_RESPONSE_ID,
            self.connect_code & 0xFFFFFFFF,
            self.encode_key & 0xFFFFFFFF,
            self.crc_bytes & 0xFF,
            self.encode_pass1 & 0xFF,
            self.encode_pass2 & 0xFF,
            self.max_packet_size & 0xFFFFFFFF,
        )

    @classmethod
    def deserialize(cls, data: bytes) -> OP_SESSION_RESPONSE:
        need(data, 17, "OP_SESSION_RESPONSE")
        _zero, _opcode, code, key, crc_bytes, pass1, pass2, max_size = struct.unpack(
            ">BBIIBBBI", data[:17]
        )
        return cls(int(code), int(key), int(crc_bytes), int(pass1), int(pass2), int(max_size))


@dataclass
class OP_COMBINED(EQStruct):
    parts: tuple[bytes, ...] = ()

    def serialize(self) -> bytes:
        out = bytearray((0, OP_COMBINED_ID))
        for part in self.parts:
            if len(part) > 255:
                raise ValueError(f"combined part is {len(part)} bytes")
            out.append(len(part))
            out += part
        return bytes(out)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_COMBINED:
        parts: list[bytes] = []
        offset = 2
        while offset < len(data):
            length = data[offset]
            offset += 1
            if offset + length > len(data):
                break
            parts.append(data[offset : offset + length])
            offset += length
        return cls(tuple(parts))


@dataclass
class OP_SESSION_DISCONNECT(EQStruct):
    connect_code: int = 0

    def serialize(self) -> bytes:
        # common/net/reliable_stream_structs.h:89 ReliableStreamDisconnect
        return struct.pack(">BBI", 0, OP_SESSION_DISCONNECT_ID, self.connect_code & 0xFFFFFFFF)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_SESSION_DISCONNECT:
        need(data, 6, "OP_SESSION_DISCONNECT")
        _zero, _opcode, code = struct.unpack(">BBI", data[:6])
        return cls(int(code))


@dataclass
class OP_KEEPALIVE(EQStruct):
    def serialize(self) -> bytes:
        return bytes((0, OP_KEEPALIVE_ID))

    @classmethod
    def deserialize(cls, data: bytes) -> OP_KEEPALIVE:
        return cls()


@dataclass
class OP_SESSION_STAT_REQUEST(EQStruct):
    timestamp: int = 0
    stat_ping: int = 0
    avg_ping: int = 0
    min_ping: int = 0
    max_ping: int = 0
    last_ping: int = 0
    packets_sent: int = 0
    packets_recv: int = 0

    def serialize(self) -> bytes:
        # common/net/reliable_stream_structs.h:135 ReliableStreamSessionStatRequest
        return struct.pack(
            ">BBHIIIIIQQ",
            0,
            OP_SESSION_STAT_REQUEST_ID,
            self.timestamp & 0xFFFF,
            self.stat_ping & 0xFFFFFFFF,
            self.avg_ping & 0xFFFFFFFF,
            self.min_ping & 0xFFFFFFFF,
            self.max_ping & 0xFFFFFFFF,
            self.last_ping & 0xFFFFFFFF,
            self.packets_sent & 0xFFFFFFFFFFFFFFFF,
            self.packets_recv & 0xFFFFFFFFFFFFFFFF,
        )

    @classmethod
    def deserialize(cls, data: bytes) -> OP_SESSION_STAT_REQUEST:
        need(data, 40, "OP_SESSION_STAT_REQUEST")
        values = struct.unpack(">BBHIIIIIQQ", data[:40])
        return cls(*(int(value) for value in values[2:]))


@dataclass
class OP_SESSION_STAT_RESPONSE(EQStruct):
    timestamp: int = 0
    our_timestamp: int = 0
    client_sent: int = 0
    client_recv: int = 0
    server_sent: int = 0
    server_recv: int = 0

    def serialize(self) -> bytes:
        # common/net/reliable_stream_structs.h:165 ReliableStreamSessionStatResponse
        return struct.pack(
            ">BBHIQQQQ",
            0,
            OP_SESSION_STAT_RESPONSE_ID,
            self.timestamp & 0xFFFF,
            self.our_timestamp & 0xFFFFFFFF,
            self.client_sent & 0xFFFFFFFFFFFFFFFF,
            self.client_recv & 0xFFFFFFFFFFFFFFFF,
            self.server_sent & 0xFFFFFFFFFFFFFFFF,
            self.server_recv & 0xFFFFFFFFFFFFFFFF,
        )

    @classmethod
    def deserialize(cls, data: bytes) -> OP_SESSION_STAT_RESPONSE:
        need(data, 40, "OP_SESSION_STAT_RESPONSE")
        values = struct.unpack(">BBHIQQQQ", data[:40])
        return cls(*(int(value) for value in values[2:]))


@dataclass
class OP_PACKET(EQStruct):
    stream_id: int
    sequence: int
    payload: bytes

    def serialize(self) -> bytes:
        # common/net/reliable_stream_structs.h:105 ReliableStreamReliableHeader
        header = struct.pack(">BBH", 0, OP_PACKET_ID + (self.stream_id & 3), self.sequence & 0xFFFF)
        return header + self.payload

    @classmethod
    def deserialize(cls, data: bytes) -> OP_PACKET:
        need(data, 4, "OP_PACKET")
        _zero, opcode, sequence = struct.unpack(">BBH", data[:4])
        stream_id = int(opcode) - OP_PACKET_ID
        return cls(stream_id, int(sequence), data[4:])


@dataclass
class OP_FRAGMENT(EQStruct):
    stream_id: int
    sequence: int
    data: bytes
    total_size: int | None = None

    def serialize(self) -> bytes:
        # common/net/reliable_stream_structs.h:105 ReliableStreamReliableHeader
        header = struct.pack(
            ">BBH", 0, OP_FRAGMENT_ID + (self.stream_id & 3), self.sequence & 0xFFFF
        )
        if self.total_size is None:
            return header + self.data
        # common/net/reliable_stream_structs.h:125 ReliableStreamReliableFragmentHeader total_size
        return header + struct.pack(">I", self.total_size & 0xFFFFFFFF) + self.data

    @classmethod
    def deserialize(cls, data: bytes) -> OP_FRAGMENT:
        """Continuation fragment. A first fragment's total size stays in `data`."""
        need(data, 4, "OP_FRAGMENT")
        _zero, opcode, sequence = struct.unpack(">BBH", data[:4])
        return cls(int(opcode) - OP_FRAGMENT_ID, int(sequence), data[4:])


@dataclass
class OP_OUT_OF_ORDER_ACK(EQStruct):
    stream_id: int
    sequence: int

    def serialize(self) -> bytes:
        # common/net/reliable_stream_connection.cpp:1321 SendOutOfOrderAck
        return struct.pack(
            ">BBH", 0, OP_OUT_OF_ORDER_ACK_ID + (self.stream_id & 3), self.sequence & 0xFFFF
        )

    @classmethod
    def deserialize(cls, data: bytes) -> OP_OUT_OF_ORDER_ACK:
        need(data, 4, "OP_OUT_OF_ORDER_ACK")
        _zero, opcode, sequence = struct.unpack(">BBH", data[:4])
        return cls(int(opcode) - OP_OUT_OF_ORDER_ACK_ID, int(sequence))


@dataclass
class OP_ACK(EQStruct):
    stream_id: int
    sequence: int

    def serialize(self) -> bytes:
        # common/net/reliable_stream_structs.h:105 ReliableStreamReliableHeader
        return struct.pack(">BBH", 0, OP_ACK_ID + (self.stream_id & 3), self.sequence & 0xFFFF)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_ACK:
        need(data, 4, "OP_ACK")
        _zero, opcode, sequence = struct.unpack(">BBH", data[:4])
        return cls(int(opcode) - OP_ACK_ID, int(sequence))


@dataclass
class OP_APP_COMBINED(EQStruct):
    parts: tuple[bytes, ...] = ()

    def serialize(self) -> bytes:
        out = bytearray((0, OP_APP_COMBINED_ID))
        for part in self.parts:
            length = len(part)
            if length < 0xFF:
                out.append(length)
            elif length <= 0xFFFF:
                out.append(0xFF)
                # common/net/reliable_stream_connection.cpp:628
                out += struct.pack(">H", length)
            else:
                out += b"\xff\xff\xff"
                # common/net/reliable_stream_connection.cpp:619
                out += struct.pack(">I", length)
            out += part
        return bytes(out)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_APP_COMBINED:
        parts: list[bytes] = []
        offset = 2
        end = len(data)
        while offset < end:
            if data[offset] == 0xFF:
                if offset + 3 > end:
                    break
                if data[offset + 1] == 0xFF and data[offset + 2] == 0xFF:
                    if offset + 7 > end:
                        break
                    length = struct.unpack_from(">I", data, offset + 3)[0]
                    offset += 7
                else:
                    length = struct.unpack_from(">H", data, offset + 1)[0]
                    offset += 3
            else:
                length = data[offset]
                offset += 1
            if offset + length > end:
                break
            parts.append(data[offset : offset + length])
            offset += length
        return cls(tuple(parts))


@dataclass
class OP_OUTBOUND_PING(EQStruct):
    payload: bytes = b""

    def serialize(self) -> bytes:
        return bytes((0, OP_OUTBOUND_PING_ID)) + self.payload

    @classmethod
    def deserialize(cls, data: bytes) -> OP_OUTBOUND_PING:
        return cls(data[2:])


@dataclass
class OP_OUT_OF_SESSION(EQStruct):
    connect_code: int = 0

    def serialize(self) -> bytes:
        # common/net/reliable_stream_structs.h:89 ReliableStreamDisconnect
        return struct.pack(">BBI", 0, OP_OUT_OF_SESSION_ID, self.connect_code & 0xFFFFFFFF)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_OUT_OF_SESSION:
        need(data, 6, "OP_OUT_OF_SESSION")
        _zero, _opcode, code = struct.unpack(">BBI", data[:6])
        return cls(int(code))
