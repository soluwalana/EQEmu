"""Additional RoF2 application packet bodies for eqclient3.

Place in eqclient3/structs/rof2_additional.py and import it from the
package __init__.py. Importing registers the OP_* types in wire.OPERATIONS.

Opaque classes deliberately retain unverified payloads byte-for-byte. They
are placeholders, NOT assertions that the packets have no structure.
"""

from __future__ import annotations

import struct
from dataclasses import dataclass, field
from typing import ClassVar

from eqclient3.structs.wire import EQStruct, _need, _fixed, _put_fixed


def _exact(data: bytes, size: int, op: str) -> None:
    _need(data, size, op)
    if len(data) != size:
        raise ValueError(f"{op}: expected exactly {size} bytes, got {len(data)}")


def _string_bytes(value: str, size: int) -> bytes:
    out = bytearray(size)
    _put_fixed(out, 0, value, size)
    return bytes(out)


@dataclass
class OP_Untargetable(EQStruct):
    """Untargetable_Struct (8 bytes): targetable_flag >= 1 is targetable."""

    id: int
    targetable_flag: int

    def serialize(self) -> bytes:
        return struct.pack("<II", self.id, self.targetable_flag)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_Untargetable:
        _exact(data, 8, cls.__name__)
        return cls(*struct.unpack("<II", data))


@dataclass
class OP_WearChange(EQStruct):
    """RoF2 WearChange_Struct, packed (27 bytes)."""

    spawn_id: int
    material: int
    unknown06: int = 0
    elite_material: int = 0
    hero_forge_model: int = 0
    unknown18: int = 0
    color: int = 0  # raw Tint_Struct.Color uint32
    wear_slot_id: int = 0

    _FMT: ClassVar[str] = "<HIIIIIIB"

    def serialize(self) -> bytes:
        return struct.pack(
            self._FMT,
            self.spawn_id,
            self.material,
            self.unknown06,
            self.elite_material,
            self.hero_forge_model,
            self.unknown18,
            self.color,
            self.wear_slot_id,
        )

    @classmethod
    def deserialize(cls, data: bytes) -> OP_WearChange:
        _exact(data, struct.calcsize(cls._FMT), cls.__name__)
        return cls(*struct.unpack(cls._FMT, data))


@dataclass
class OP_Action(EQStruct):
    """RoF2 ActionAlt_Struct (56 bytes), NOT the 39-byte Action_Struct."""

    target: int
    source: int
    level: int = 0
    unknown06: int = 0
    instrument_mod: float = 1.0
    force: float = 0.0
    hit_heading: float = 0.0
    hit_pitch: float = 0.0
    type: int = 0
    damage: int = 0
    unknown31: int = 0
    spell: int = 0
    spell_level: int = 0
    effect_flag: int = 0
    spell_gem: int = 0
    inventory_slot_raw: bytes = b"\xff\xff\x00\x00\xff\xff\xff\xff\xff\xff\x00\x00"
    item_cast_type: int = 0

    _FMT: ClassVar[str] = "<HHHIffffBIHIBBB12sI"

    def serialize(self) -> bytes:
        if len(self.inventory_slot_raw) != 12:
            raise ValueError("OP_Action.inventory_slot_raw must be 12 bytes")
        return struct.pack(
            self._FMT,
            self.target,
            self.source,
            self.level,
            self.unknown06,
            self.instrument_mod,
            self.force,
            self.hit_heading,
            self.hit_pitch,
            self.type,
            self.damage,
            self.unknown31,
            self.spell,
            self.spell_level,
            self.effect_flag,
            self.spell_gem,
            self.inventory_slot_raw,
            self.item_cast_type,
        )

    @classmethod
    def deserialize(cls, data: bytes) -> OP_Action:
        _exact(data, 56, cls.__name__)
        return cls(*struct.unpack(cls._FMT, data))

    @property
    def inventory_slot_fields(self) -> tuple[int, int, int, int, int, int]:
        """Raw RoF2 InventorySlot_Struct: type, unknown, slot, sub, aug, unknown."""
        return struct.unpack("<hhhhhh", self.inventory_slot_raw)


@dataclass
class OP_FormattedMessage(EQStruct):
    """12-byte header plus <=9 null-terminated substitution strings."""

    unknown0: int
    string_id: int
    type: int
    arguments: list[str] = field(default_factory=list)
    trailing: bytes = b""
    terminated: bool = True

    def serialize(self) -> bytes:
        if len(self.arguments) > 9:
            raise ValueError("OP_FormattedMessage can carry at most 9 arguments")
        out = bytearray(struct.pack("<III", self.unknown0, self.string_id, self.type))
        for value in self.arguments:
            out += value.encode("latin1", errors="replace") + b"\0"
        if self.terminated:
            out += b"\0"
        return bytes(out) + self.trailing

    @classmethod
    def deserialize(cls, data: bytes) -> OP_FormattedMessage:
        _need(data, 12, cls.__name__)
        header = struct.unpack_from("<III", data)
        args: list[str] = []
        i = 12
        terminated = False
        while i < len(data) and len(args) < 9:
            end = data.find(b"\x00", i)
            if end < 0:
                args.append(data[i:].decode("latin1"))
                i = len(data)
                break
            if end == i:
                i += 1
                terminated = True
                break
            args.append(data[i:end].decode("latin1"))
            i = end + 1
        # When all nine substitution slots are populated, the final NUL is
        # after the ninth string rather than an empty slot in the loop.
        if len(args) == 9 and i < len(data) and data[i] == 0:
            terminated = True
            i += 1
        return cls(header[0], header[1], header[2], args, data[i:], terminated)


@dataclass
class OP_ManaUpdate(EQStruct):
    """common/eq_packet_structs.h ManaUpdate_Struct, packed (10 bytes)."""

    cur_mana: int
    max_mana: int
    spawn_id: int

    def serialize(self) -> bytes:
        return struct.pack("<IIH", self.cur_mana, self.max_mana, self.spawn_id)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_ManaUpdate:
        _exact(data, 10, cls.__name__)
        return cls(*struct.unpack("<IIH", data))


@dataclass
class OP_EnduranceUpdate(EQStruct):
    """RoF2's actual named opcode; 10-byte EnduranceUpdate_Struct."""

    cur_end: int
    max_end: int
    spawn_id: int

    def serialize(self) -> bytes:
        return struct.pack("<IIH", self.cur_end, self.max_end, self.spawn_id)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_EnduranceUpdate:
        _exact(data, 10, cls.__name__)
        return cls(*struct.unpack("<IIH", data))


class OP_Endurance(OP_EnduranceUpdate):
    """Compatibility alias: RoF2 patch_RoF2.conf calls this OP_EnduranceUpdate."""


@dataclass
class OP_BeginCast(EQStruct):
    """RoF2 BeginCast_Struct, packed (10 bytes): spell, caster, cast ms."""

    spell_id: int
    caster_id: int
    cast_time: int

    def serialize(self) -> bytes:
        return struct.pack("<IHI", self.spell_id, self.caster_id, self.cast_time)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_BeginCast:
        _exact(data, 10, cls.__name__)
        return cls(*struct.unpack("<IHI", data))


@dataclass
class XTargetEntry:
    slot: int  # uint32
    status: int  # uint8: 0 empty, 1 entity present, 2 named PC slot
    entity_id: int  # uint32
    name: str  # NUL-terminated, latin1


@dataclass
class OP_XTargetResponse(EQStruct):
    """zone/client.cpp: SendXTargetPacket/SendXTargetUpdates/SetMaxXTargets.

    Header: max_xtargets:u32, count:u32. Count=0 gives a header-only
    capacity change (8 bytes). Count>0 has `count` entries of:
      slot:u32, status:u8, entity_id:u32, name:cstring.
    """

    max_xtargets: int
    entry_count: int = 0
    entries: list[XTargetEntry] = field(default_factory=list)
    trailing: bytes = b""

    def serialize(self) -> bytes:
        if self.entries and self.entry_count not in (0, len(self.entries)):
            raise ValueError("OP_XTargetResponse entry_count disagrees with entries")
        if self.entry_count and not self.entries:
            raise ValueError("OP_XTargetResponse nonzero entry_count requires entries")
        count = len(self.entries)
        out = bytearray(struct.pack("<II", self.max_xtargets, count))
        for entry in self.entries:
            if "\x00" in entry.name:
                raise ValueError("OP_XTargetResponse name cannot contain NUL")
            out += struct.pack("<IBI", entry.slot, entry.status, entry.entity_id)
            out += entry.name.encode("latin1", errors="replace") + b"\x00"
        return bytes(out) + self.trailing

    @classmethod
    def deserialize(cls, data: bytes) -> OP_XTargetResponse:
        _need(data, 8, cls.__name__)
        max_xtargets, count = struct.unpack_from("<II", data)
        offset = 8
        if count > (len(data) - offset) // 10:
            raise ValueError("truncated OP_XTargetResponse entries")
        entries = []
        for _ in range(count):
            _need(data[offset:], 10, cls.__name__)
            slot, status, entity_id = struct.unpack_from("<IBI", data, offset)
            offset += 9
            end = data.find(b"\x00", offset)
            if end < 0:
                raise ValueError("unterminated OP_XTargetResponse entry name")
            name = data[offset:end].decode("latin1")
            offset = end + 1
            entries.append(XTargetEntry(slot, status, entity_id, name))
        return cls(max_xtargets, count, entries, data[offset:])


@dataclass
class OP_PlayerStateAdd(EQStruct):
    """PlayerState_Struct: uint32 spawn_id, uint32 state bitfield."""

    spawn_id: int
    state: int

    def serialize(self) -> bytes:
        return struct.pack("<II", self.spawn_id, self.state)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_PlayerStateAdd:
        _exact(data, 8, cls.__name__)
        return cls(*struct.unpack("<II", data))


class OP_PlayerStateRemove(OP_PlayerStateAdd):
    """Same PlayerState_Struct layout, clears instead of sets state flags."""


@dataclass
class OP_Animation(EQStruct):
    """RoF2 animation: action at offset 2, speed at offset 3."""

    spawnid: int
    action: int
    speed: int

    def serialize(self) -> bytes:
        return struct.pack("<HBB", self.spawnid, self.action, self.speed)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_Animation:
        _exact(data, 4, cls.__name__)
        return cls(*struct.unpack("<HBB", data))


@dataclass
class AAEntry:
    index: int  # position in fixed RoF2 AA array
    aa: int
    value: int
    charges: int


@dataclass
class OP_RespondAA(EQStruct):
    """RoF2 AATable_Struct: 6 u32 + 300 (AA, value, charges) triples = 3624 bytes.

    Only nonzero AA entries are stored in `entries` to keep debug output small.
    Array indexes are preserved for exact serialization of sparse tables.
    """

    aa_spent: int
    aapoints_assigned: int = 0
    aa_spent_general: int = 0
    aa_spent_archetype: int = 0
    aa_spent_class: int = 0
    aa_spent_special: int = 0
    entries: list[AAEntry] = field(default_factory=list)

    def serialize(self) -> bytes:
        out = bytearray(
            struct.pack(
                "<6I",
                self.aa_spent,
                self.aapoints_assigned,
                self.aa_spent_general,
                self.aa_spent_archetype,
                self.aa_spent_class,
                self.aa_spent_special,
            )
        )
        out += bytes(300 * 12)
        used: set[int] = set()
        for entry in self.entries:
            if not 0 <= entry.index < 300 or entry.index in used:
                raise ValueError("invalid or duplicated AA entry index")
            used.add(entry.index)
            struct.pack_into("<III", out, 24 + 12 * entry.index, entry.aa, entry.value, entry.charges)
        return bytes(out)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_RespondAA:
        _exact(data, 3624, cls.__name__)
        header = struct.unpack_from("<6I", data)
        entries = []
        for index in range(300):
            aa, value, charges = struct.unpack_from("<III", data, 24 + index * 12)
            if aa or value or charges:
                entries.append(AAEntry(index, aa, value, charges))
        return cls(
            header[0],
            header[1],
            header[2],
            header[3],
            header[4],
            header[5],
            entries,
        )


@dataclass
class OP_MobRename(EQStruct):
    """common/eq_packet_structs.h MobRename_Struct, packed 200 bytes."""

    old_name: str
    old_name_again: str
    new_name: str
    unknown192: int = 0
    unknown196: int = 1

    def serialize(self) -> bytes:
        return (
            _string_bytes(self.old_name, 64)
            + _string_bytes(self.old_name_again, 64)
            + _string_bytes(self.new_name, 64)
            + struct.pack("<II", self.unknown192, self.unknown196)
        )

    @classmethod
    def deserialize(cls, data: bytes) -> OP_MobRename:
        _exact(data, 200, cls.__name__)
        return cls(
            _fixed(data, 0, 64), _fixed(data, 64, 64), _fixed(data, 128, 64), *struct.unpack_from("<II", data, 192)
        )


@dataclass
class AltCurrencyEntry:
    currency_number: int
    unknown00: int
    currency_number2: int
    item_id: int
    item_icon: int
    stack_size: int
    display: int


@dataclass
class AltCurrencyBalance:
    name: str
    currency_number: int
    unknown072: int
    amount: int
    unknown080: int = 0
    unknown084: int = 0


@dataclass
class OP_AltCurrency(EQStruct):
    """RoF2 submodes 8 (populate) and 7 (balance update).

    Unrecognized modes remain raw, preventing fabricated field mappings.
    """

    mode: int
    entries: list[AltCurrencyEntry] = field(default_factory=list)
    balance: AltCurrencyBalance | None = None
    unknown_payload: bytes = b""

    def serialize(self) -> bytes:
        if self.mode == 8:
            out = bytearray(struct.pack("<II", 8, len(self.entries)))
            for e in self.entries:
                out += struct.pack(
                    "<IIIIIIB",
                    e.currency_number,
                    e.unknown00,
                    e.currency_number2,
                    e.item_id,
                    e.item_icon,
                    e.stack_size,
                    e.display,
                )
            return bytes(out) + self.unknown_payload
        if self.mode == 7 and self.balance is not None:
            b = self.balance
            return (
                struct.pack("<I", 7)
                + _string_bytes(b.name, 64)
                + struct.pack("<IIIII", b.currency_number, b.unknown072, b.amount, b.unknown080, b.unknown084)
                + self.unknown_payload
            )
        return struct.pack("<I", self.mode) + self.unknown_payload

    @classmethod
    def deserialize(cls, data: bytes) -> OP_AltCurrency:
        _need(data, 4, cls.__name__)
        mode = struct.unpack_from("<I", data)[0]
        if mode == 8:
            _need(data, 8, cls.__name__)
            count = struct.unpack_from("<I", data, 4)[0]
            if count > (len(data) - 8) // 25:
                raise ValueError("truncated OP_AltCurrency populate entries")
            entries = []
            for index in range(count):
                entries.append(AltCurrencyEntry(*struct.unpack_from("<IIIIIIB", data, 8 + index * 25)))
            return cls(mode, entries, None, data[8 + count * 25 :])
        if mode == 7:
            _need(data, 88, cls.__name__)
            name = _fixed(data, 4, 64)
            balance = AltCurrencyBalance(name, *struct.unpack_from("<IIIII", data, 68))
            return cls(mode, [], balance, data[88:])
        return cls(mode, [], None, data[4:])


@dataclass
class OP_SendFindableNPCs(EQStruct):
    """common/eq_packet_structs.h FindableNPC_Struct: one NPC per packet (112 bytes)."""

    action: int
    entity_id: int
    name: str
    last_name: str = ""
    race: int = 0
    class_: int = 0
    unknown109: int = 0x16
    unknown110: int = 0x06
    unknown111: int = 0x24

    def serialize(self) -> bytes:
        return (
            struct.pack("<II", self.action, self.entity_id)
            + _string_bytes(self.name, 64)
            + _string_bytes(self.last_name, 32)
            + struct.pack("<IBBBB", self.race, self.class_, self.unknown109, self.unknown110, self.unknown111)
        )

    @classmethod
    def deserialize(cls, data: bytes) -> OP_SendFindableNPCs:
        _exact(data, 112, cls.__name__)
        action, entity_id = struct.unpack_from("<II", data)
        return cls(
            action, entity_id, _fixed(data, 8, 64), _fixed(data, 72, 32), *struct.unpack_from("<IBBBB", data, 104)
        )


@dataclass
class CompletedTask:
    task_id: int
    title: str
    completed_time: int  # Unix seconds


@dataclass
class OP_CompletedTasks(EQStruct):
    """zone/task_manager.cpp: uint32 count; repeated (id:u32,title:cstring,time:u32)."""

    tasks: list[CompletedTask] = field(default_factory=list)
    trailing: bytes = b""

    def serialize(self) -> bytes:
        out = bytearray(struct.pack("<I", len(self.tasks)))
        for task in self.tasks:
            out += struct.pack("<I", task.task_id)
            out += task.title.encode("latin1", errors="replace") + b"\x00"
            out += struct.pack("<I", task.completed_time)
        return bytes(out) + self.trailing

    @classmethod
    def deserialize(cls, data: bytes) -> OP_CompletedTasks:
        _need(data, 4, cls.__name__)
        count = struct.unpack_from("<I", data)[0]
        cursor = 4
        tasks = []
        if count > len(data) // 9:
            raise ValueError(f"{cls.__name__}: impossible task count {count}")
        for _ in range(count):
            if cursor + 4 > len(data):
                raise ValueError("truncated completed task id")
            task_id = struct.unpack_from("<I", data, cursor)[0]
            cursor += 4
            end = data.find(b"\x00", cursor)
            if end < 0 or end + 5 > len(data):
                raise ValueError("truncated completed task title/time")
            title = data[cursor:end].decode("latin1")
            completed_time = struct.unpack_from("<I", data, end + 1)[0]
            tasks.append(CompletedTask(task_id, title, completed_time))
            cursor = end + 5
        return cls(tasks, data[cursor:])


@dataclass
class OP_AggroMeterTargetInfo(EQStruct):
    """zone/client.cpp ProcessAggroMeter: lock target, current target (8 bytes)."""

    lock_target_id: int
    target_id: int

    def serialize(self) -> bytes:
        return struct.pack("<II", self.lock_target_id, self.target_id)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_AggroMeterTargetInfo:
        _exact(data, 8, cls.__name__)
        return cls(*struct.unpack("<II", data))


@dataclass
class AggroEntry:
    type: int
    percent: int


@dataclass
class OP_AggroMeterUpdate(EQStruct):
    """zone/client.cpp ProcessAggroMeter: [flag:u8] [optional secondary_id:u32]
    [count:u8] then count * (aggro_type:u8, percentage:u16).
    """

    secondary_changed: bool = False
    secondary_id: int | None = None
    entries: list[AggroEntry] = field(default_factory=list)
    trailing: bytes = b""

    def serialize(self) -> bytes:
        if len(self.entries) > 255:
            raise ValueError("too many aggro meter entries")
        out = bytearray(struct.pack("<B", int(self.secondary_changed)))
        if self.secondary_changed:
            out += struct.pack("<I", self.secondary_id or 0)
        out += struct.pack("<B", len(self.entries))
        for entry in self.entries:
            out += struct.pack("<BH", entry.type, entry.percent)
        return bytes(out) + self.trailing

    @classmethod
    def deserialize(cls, data: bytes) -> OP_AggroMeterUpdate:
        _need(data, 2, cls.__name__)
        flag = data[0]
        cursor = 1
        secondary = None
        if flag:
            _need(data, 6, cls.__name__)
            secondary = struct.unpack_from("<I", data, cursor)[0]
            cursor += 4
        count = data[cursor]
        cursor += 1
        if cursor + count * 3 > len(data):
            raise ValueError("truncated aggro meter entries")
        entries = [AggroEntry(*struct.unpack_from("<BH", data, cursor + i * 3)) for i in range(count)]
        cursor += count * 3
        return cls(bool(flag), secondary, entries, data[cursor:])


@dataclass(repr=False)
class _Opaque(EQStruct):
    """Lossless packet body when a reliable RoF2 field schema isn't established."""

    payload: bytes = b""

    def serialize(self) -> bytes:
        return self.payload

    @classmethod
    def deserialize(cls, data: bytes) -> _Opaque:
        return cls(bytes(data))

    def __repr__(self) -> str:
        preview = self.payload[:64].hex(" ")
        suffix = " ..." if len(self.payload) > 64 else ""
        return f"{type(self).__name__}(size={len(self.payload)}, hex={preview}{suffix})"


class OP_Jump(_Opaque):
    """Jump notification. The zone handler reads no payload fields."""


class OP_KeyRing(_Opaque):
    """Client request for the key-ring list; server responds through chat."""


@dataclass
class OP_LDoNButton(EQStruct):
    """Adventure accept/cancel response. The handler reads bool at byte 0.

    Retains trailing bytes (if present) rather than discarding them.
    """

    accepted: int = 0
    trailing: bytes = b""

    def serialize(self) -> bytes:
        return struct.pack("<B", self.accepted) + self.trailing

    @classmethod
    def deserialize(cls, data: bytes) -> OP_LDoNButton:
        _need(data, 1, cls.__name__)
        return cls(data[0], data[1:])


class OP_LDoNDisarmTraps(_Opaque):
    """LDoN disarm request; RoF2 maps it through OP_DisarmTraps."""


class OP_LDoNInspect(_Opaque):
    """Inspect targeted LDoN treasure; handler reads no payload fields."""


class OP_LDoNOpen(_Opaque):
    """Open targeted LDoN chest; handler reads no payload fields."""


class OP_LDoNPickLock(_Opaque):
    """Pick lock on targeted LDoN chest; handler reads no payload fields."""


class OP_LDoNSenseTraps(_Opaque):
    """Sense traps on targeted chest; not separately mapped in RoF2 conf."""


@dataclass
class OP_TargetHoTT(EQStruct):
    """Target-of-target id, common ClientTarget_Struct (4 bytes)."""

    new_target: int

    def serialize(self) -> bytes:
        return struct.pack("<I", self.new_target)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_TargetHoTT:
        _exact(data, 4, cls.__name__)
        return cls(struct.unpack("<I", data)[0])


@dataclass
class OP_RestState(EQStruct):
    """Rest / combat indicator from zone/client.cpp (1 or 5 bytes).

    state=1 interrupts rest (enter combat), no timer.
    state=0 starts or updates the rest countdown; timer_seconds is a u32.
    """

    state: int
    timer_seconds: int | None = None

    def serialize(self) -> bytes:
        if self.timer_seconds is None:
            return struct.pack("<B", self.state)
        return struct.pack("<BI", self.state, self.timer_seconds)

    @classmethod
    def deserialize(cls, data: bytes) -> OP_RestState:
        if len(data) == 1:
            return cls(data[0], None)
        if len(data) == 5:
            state, timer = struct.unpack("<BI", data)
            return cls(state, timer)
        raise ValueError(f"{cls.__name__}: expected 1 or 5 bytes, got {len(data)}")


class OP_AutoAttack2(_Opaque):
    """Opaque: EQEmu's handler ignores the body; don't assume bool/u32."""
