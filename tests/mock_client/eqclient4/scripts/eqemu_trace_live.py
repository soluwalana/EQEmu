#!/usr/bin/env python3
"""Read EQEmu PacketTrace files and follow new traces as they appear.

Examples:
  uv run python -m eqclient4.scripts.eqemu_trace_live /tmp/traces
  uv run python -m eqclient4.scripts.eqemu_trace_live /tmp/traces --pattern 'trace*.bin'
  uv run python -m eqclient4.scripts.eqemu_trace_live /tmp/traces --max-age 30
  uv run python -m eqclient4.scripts.eqemu_trace_live /tmp/eqtrace.1234.bin

Each trace has one reader thread. One consumer owns the decoders, output, and
per-file CharacterInventory instances, so prints never interleave.
"""

import argparse
import fnmatch
import os
import pprint
import struct
import threading
import time
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from queue import Empty, Full, Queue
from typing import BinaryIO, Iterator, NamedTuple

from eqclient4.inventory import CharacterInventory
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
    OP_ShopPlayerBuy,
    OP_ShopPlayerSell,
)

FRAME = struct.Struct("<QBBHHI")
LENGTH = struct.Struct("<I")
MAX_RECORD = 8 * 1024 * 1024 + 131090


class Frame(NamedTuple):
    unix_us: int
    direction: int
    stage: int
    opcode: str
    peer: str
    payload: bytes


def read_frames(
    file: BinaryIO, follow: bool, stop: threading.Event | None = None
) -> Iterator[Frame]:
    """Read complete, length-delimited records; never consume a partial record.

    On follow, wait for incomplete appends. If the file is truncated in place,
    rewind to its beginning.
    """
    while stop is None or not stop.is_set():
        offset = file.tell()
        head = file.read(LENGTH.size)
        if len(head) < LENGTH.size:
            if not follow:
                return
            file.seek(0, 2)
            file_size = file.tell()
            file.seek(0 if file_size < offset else offset)
            if stop is not None:
                stop.wait(0.1)
            else:
                time.sleep(0.1)
            continue

        (length,) = LENGTH.unpack(head)
        if not FRAME.size <= length <= MAX_RECORD:
            raise ValueError(f"invalid frame length {length} at offset {offset}")
        raw = file.read(length)
        if len(raw) < length:
            if not follow:
                return
            file.seek(0, 2)
            file_size = file.tell()
            file.seek(0 if file_size < offset else offset)
            if stop is not None:
                stop.wait(0.1)
            else:
                time.sleep(0.1)
            continue

        unix_us, direction, stage, name_len, peer_len, data_len = FRAME.unpack_from(raw)
        if FRAME.size + name_len + peer_len + data_len != length:
            raise ValueError(f"bad frame structure at offset {offset}")
        start = FRAME.size
        opcode = raw[start : start + name_len].decode("utf-8", "replace")
        start += name_len
        peer = raw[start : start + peer_len].decode("utf-8", "replace")
        start += peer_len
        payload = raw[start : start + data_len]
        yield Frame(unix_us, direction, stage, opcode, peer, payload)


def matches(op: str, patterns: list[str]) -> bool:
    return any(fnmatch.fnmatchcase(op.casefold(), pat.casefold()) for pat in patterns)


@dataclass(frozen=True)
class Source:
    path: Path
    identity: tuple[int, int]  # device and inode; distinguish rotated files


@dataclass(frozen=True)
class PacketEvent:
    source: Source
    frame: Frame


@dataclass(frozen=True)
class ErrorEvent:
    source: Source
    error: str


Event = PacketEvent | ErrorEvent


@dataclass
class Watcher:
    source: Source
    stop: threading.Event
    thread: threading.Thread


def enqueue(events: Queue[Event], event: Event, stop: threading.Event) -> None:
    while not stop.is_set():
        try:
            events.put(event, timeout=0.25)
            return
        except Full:
            continue


def read_trace(
    source: Source,
    events: Queue[Event],
    stop: threading.Event,
    *,
    follow: bool,
    from_end: bool,
    max_age: float,
) -> None:
    try:
        with source.path.open("rb") as file:
            st = os.fstat(file.fileno())
            if (st.st_dev, st.st_ino) != source.identity:
                return  # rotated between directory scan and open
            if from_end:
                file.seek(0, 2)
            for frame in read_frames(file, follow, stop):
                if max_age > 0:
                    age_us = int(max_age * 1_000_000)
                    if frame.unix_us < time.time_ns() // 1_000 - age_us:
                        continue
                enqueue(events, PacketEvent(source, frame), stop)
    except (OSError, ValueError, struct.error) as exc:
        enqueue(events, ErrorEvent(source, f"{type(exc).__name__}: {exc}"), stop)


def new_watcher(
    source: Source, events: Queue[Event], *, follow: bool, from_end: bool, max_age: float
) -> Watcher:
    stop = threading.Event()
    thread = threading.Thread(
        target=read_trace,
        args=(source, events, stop),
        kwargs={"follow": follow, "from_end": from_end, "max_age": max_age},
        name=f"trace:{source.path.name}:{source.identity[1]}",
        daemon=True,
    )
    thread.start()
    return Watcher(source, stop, thread)


def discover(
    root: Path,
    directory_mode: bool,
    pattern: str,
    watchers: dict[Path, Watcher],
    events: Queue[Event],
    *,
    follow: bool,
    from_end: bool,
    max_age: float,
) -> None:
    if directory_mode:
        paths = sorted(root.glob(pattern))
    else:
        paths = [root]
    present: set[Path] = set()
    for path in paths:
        try:
            if not path.is_file():
                continue
            st = path.stat()
        except OSError:
            continue
        present.add(path)
        identity = (st.st_dev, st.st_ino)
        old = watchers.get(path)
        if old is not None and old.source.identity == identity:
            continue
        if old is not None:
            old.stop.set()
        source = Source(path, identity)
        watchers[path] = new_watcher(
            source, events, follow=follow, from_end=from_end, max_age=max_age
        )

    # A removed file may still have an open descriptor; stop its reader.
    for path in list(watchers):
        if path not in present:
            watchers.pop(path).stop.set()


def display_event(
    event: Event,
    args: argparse.Namespace,
    only: list[str],
    exclude: list[str],
    start: str | None,
    end: str | None,
    inventories: dict[Source, CharacterInventory],
    *,
    directory_mode: bool,
) -> None:
    if isinstance(event, ErrorEvent):
        print(f"[{event.source.path.name}] READ FAILED: {event.error}", flush=True)
        return

    unix_us, direction, stage, opcode, peer, payload = event.frame
    dt = datetime.fromtimestamp(unix_us / 1_000_000)
    stamp = dt.isoformat(timespec="microseconds")
    if (start and stamp < start) or (end and stamp >= end):
        return
    way = "recv" if direction == 0 else "send"
    layer = "client" if stage == 1 else "emu"
    if (args.direction and way != args.direction) or (args.stage and layer != args.stage):
        return
    if (only and not matches(opcode, only)) or (exclude and matches(opcode, exclude)):
        return

    source_label = f" [{event.source.path.name}]" if directory_mode else ""
    print(
        f"[{stamp}]{source_label} {way:4} {layer:6} " f"{peer} {opcode} ({len(payload)} bytes)",
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
                    | OP_ShopPlayerSell()
                    | OP_ShopPlayerBuy()
                ):
                    inventory = inventories.setdefault(event.source, CharacterInventory())
                    change = inventory.apply(obj)
                    if change.changed:
                        print(inventory.render_change(change), flush=True)
                    print(inventory.render(show_empty=False), flush=True)
                case _:
                    pass
        except Exception as exc:
            print(f"  DECODE FAILED: {type(exc).__name__}: {exc}", flush=True)
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


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("file", type=Path, help="trace file or directory of trace files")
    p.add_argument("--pattern", default="*trace*.bin", help="directory filename glob")
    p.add_argument("--registry", metavar="MODULE:DICT")  # retained for CLI compatibility
    p.add_argument("--only", action="append", default=[], metavar="OPCODES")
    p.add_argument("--exclude", action="append", default=[], metavar="OPCODES")
    p.add_argument("--start", help="YYYY-MM-DD or ISO timestamp")
    p.add_argument("--end", help="YYYY-MM-DD or ISO timestamp, inclusive precision")
    p.add_argument("--direction", choices=("send", "recv"))
    p.add_argument("--stage", choices=("emu", "client"))
    p.add_argument("--max-bytes", type=int, default=128)
    p.add_argument("--hex", action="store_true")
    p.add_argument("--from-end", action="store_true", help="skip existing bytes in each file")
    p.add_argument("--no-follow", action="store_true", help="read current snapshot then exit")
    p.add_argument(
        "--max-age",
        type=float,
        default=None,
        metavar="SECONDS",
        help="skip records older than N seconds; 0 disables (directory default: 120, file: 0)",
    )
    p.add_argument("--poll-interval", type=float, default=0.5, metavar="SECONDS")
    p.add_argument("--queue-size", type=int, default=128, metavar="RECORDS")
    args = p.parse_args()

    root = args.file.expanduser().resolve()
    if not root.exists():
        p.error(f"path does not exist: {root}")
    directory_mode = root.is_dir()
    if not directory_mode and not root.is_file():
        p.error(f"not a regular file or directory: {root}")
    if args.poll_interval <= 0 or args.queue_size < 1:
        p.error("--poll-interval and --queue-size must be positive")
    max_age = (120.0 if directory_mode else 0.0) if args.max_age is None else args.max_age
    if max_age < 0:
        p.error("--max-age must be nonnegative")

    only = split_patterns(args.only)
    exclude = split_patterns(args.exclude)
    start = timestamp_bound(args.start, end=False) if args.start else None
    end = timestamp_bound(args.end, end=True) if args.end else None

    events: Queue[Event] = Queue(maxsize=args.queue_size)
    watchers: dict[Path, Watcher] = {}
    inventories: dict[Source, CharacterInventory] = {}
    follow = not args.no_follow
    next_scan = 0.0
    try:
        while True:
            now = time.monotonic()
            if now >= next_scan:
                discover(
                    root,
                    directory_mode,
                    args.pattern,
                    watchers,
                    events,
                    follow=follow,
                    from_end=args.from_end,
                    max_age=max_age,
                )
                next_scan = now + args.poll_interval

            try:
                event = events.get(timeout=min(0.2, max(0.01, next_scan - time.monotonic())))
            except Empty:
                pass
            else:
                display_event(
                    event,
                    args,
                    only,
                    exclude,
                    start,
                    end,
                    inventories,
                    directory_mode=directory_mode,
                )
                events.task_done()

            if (
                not follow
                and all(not w.thread.is_alive() for w in watchers.values())
                and events.empty()
            ):
                break
    except KeyboardInterrupt:
        pass
    finally:
        for watcher in watchers.values():
            watcher.stop.set()
        for watcher in watchers.values():
            watcher.thread.join(timeout=1.0)


if __name__ == "__main__":
    main()
