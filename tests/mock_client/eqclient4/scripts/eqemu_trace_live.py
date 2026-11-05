#!/usr/bin/env pyq  Aw132`  thon3
"""Follow EQEmu PacketTrace binary records and pretty-print with EQStruct.

Requires eq_packet_viewer.py beside this file for the same registry/formatting.
Example:
  python eqemu_trace_live.py /tmp/eqtrace.1234.bin --only 'OP_Consider,OP_Spawn*'
"""

import argparse
import fnmatch
import pprint
import struct
import time
from datetime import datetime
from pathlib import Path
from typing import IO, Generator

from eqclient4.scripts.eq_packet_viewer import (
    hexdump,
    split_patterns,
    timestamp_bound,
    view_value,
)
from eqclient4.structs import (
    OPERATIONS,
    OP_CancelTrade,
    OP_CharInventory,
    OP_DeleteItem,
    OP_FinishTrade,
    OP_ItemPacket,
    OP_MoveItem,
)
from eqclient4.structs.inventory import CharacterInventory

FRAME = struct.Struct(
    "<QBBHHI"
)  # unix microseconds, direction, stage, name len, peer len, data len
LENGTH = struct.Struct("<I")
MAX_RECORD = 8 * 1024 * 1024 + 131090


def read_frames(file: IO, follow: bool) -> Generator:
    while True:
        offset = file.tell()
        head = file.read(4)
        if len(head) < 4:
            if not follow:
                return
            file.seek(offset)
            time.sleep(0.1)
            continue
        (length,) = LENGTH.unpack(head)
        if not FRAME.size <= length <= MAX_RECORD:
            raise ValueError(f"invalid frame length {length} at offset {offset}")
        raw = file.read(length)
        if len(raw) < length:
            if not follow:
                return
            file.seek(offset)
            time.sleep(0.1)
            continue
        unix_us, direction, stage, name_len, peer_len, data_len = FRAME.unpack_from(raw)
        if FRAME.size + name_len + peer_len + data_len != length:
            raise ValueError(f"bad frame structure at offset {offset}")
        start = FRAME.size
        op = raw[start : start + name_len].decode("utf-8", "replace")
        start += name_len
        peer = raw[start : start + peer_len].decode("utf-8", "replace")
        start += peer_len
        payload = raw[start : start + data_len]
        yield unix_us, direction, stage, op, peer, payload


def matches(op: str, patterns: list[str]) -> bool:
    return any(fnmatch.fnmatchcase(op.casefold(), pat.casefold()) for pat in patterns)


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("file", type=Path)
    p.add_argument("--registry", metavar="MODULE:DICT")
    p.add_argument("--only", action="append", default=[], metavar="OPCODES")
    p.add_argument("--exclude", action="append", default=[], metavar="OPCODES")
    p.add_argument("--start", help="YYYY-MM-DD or ISO timestamp")
    p.add_argument("--end", help="YYYY-MM-DD or ISO timestamp, inclusive precision")
    p.add_argument(
        "--direction", choices=("send", "recv"), help="direction from CLIENT perspective"
    )
    p.add_argument("--stage", choices=("emu", "client"))
    p.add_argument("--max-bytes", type=int, default=128)
    p.add_argument("--hex", action="store_true")
    p.add_argument(
        "--from-end", action="store_true", help="ignore existing data, follow new records"
    )
    p.add_argument("--no-follow", action="store_true")
    args = p.parse_args()
    only = split_patterns(args.only)
    exclude = split_patterns(args.exclude)
    start = timestamp_bound(args.start, end=False) if args.start else None
    end = timestamp_bound(args.end, end=True) if args.end else None

    inventory = CharacterInventory()

    with args.file.open("rb") as f:
        if args.from_end:
            f.seek(0, 2)
        try:
            for unix_us, direction, stage, opcode, peer, payload in read_frames(
                f, not args.no_follow
            ):
                dt = datetime.fromtimestamp(unix_us / 1_000_000)
                stamp = dt.isoformat(timespec="microseconds")
                if start and stamp < start or end and stamp >= end:
                    continue
                way = "recv" if direction == 0 else "send"
                layer = "client" if stage == 1 else "emu"
                if args.direction and way != args.direction or args.stage and layer != args.stage:
                    continue
                if only and not matches(opcode, only) or exclude and matches(opcode, exclude):
                    continue

                print(
                    f"[{stamp}] {way:4} {layer:6} {peer} {opcode} ({len(payload)} bytes)",
                    flush=True,
                )
                cls = OPERATIONS.get(opcode)
                if cls and layer == "client":
                    try:
                        obj = cls.deserialize(payload)
                        print(pprint.pformat(view_value(obj), sort_dicts=False), flush=True)
                        match obj:
                            case (
                                OP_CharInventory()
                                | OP_ItemPacket()
                                | OP_MoveItem()
                                | OP_DeleteItem()
                                | OP_FinishTrade()
                                | OP_CancelTrade()
                            ):
                                event = inventory.apply(obj)
                                if event.changed:
                                    print(inventory.render_change(event), flush=True)
                                print(inventory.render(show_empty=False), flush=True)
                            case _:
                                pass
                    except Exception as e:
                        print(f"  DECODE FAILED: {type(e).__name__}: {e}", flush=True)
                        print(hexdump(payload, args.max_bytes), flush=True)
                else:
                    if cls and layer == "emu":
                        print(
                            "  [Emulator layout; client-version EQStruct decoder not attempted]",
                            flush=True,
                        )
                    if args.hex or not cls or layer == "emu":
                        print(hexdump(payload, args.max_bytes), flush=True)
                print(flush=True)
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    main()
