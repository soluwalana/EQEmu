#!/usr/bin/env python3
"""Inspect EQ client bus captures (SQLite), optionally decoding EQStruct packets.

Examples:
    python eq_packet_viewer.py ~/.eqclient/logs/MyChar/bus.sqlite3 \
        --registry eqclient3.protocol:OPCODE_TO_STRUCT --last 100

    python eq_packet_viewer.py bus.sqlite3 --registry mypkg.structs:OPCODE_TO_STRUCT \
        --only OP_Consider,OP_Spawn* --exclude OP_KeepAlive \
        --start 2026-11-02T09:00 --end 2026-11-02T09:30 --direction recv

    python eq_packet_viewer.py bus.sqlite3 --registry mypkg.structs:OPCODE_TO_STRUCT -i

Registry is any dict/mapping from opcode name to an EQStruct subclass whose
class method deserialize(payload: bytes) returns an instance. Unknown opcodes
and failed decodes are displayed as hex/ASCII instead of crashing the viewer.
"""

from __future__ import annotations

import argparse
import cmd
from dataclasses import fields, is_dataclass
from datetime import date, datetime, timedelta
from enum import Enum
from pathlib import Path
import pprint
import re
import shlex
import sqlite3
from typing import Any, Mapping
from urllib.parse import quote

from eqclient3.structs import OPERATIONS

# Each end value includes the entire unit the user specified. For instance,
# --end 2026-11-02T10:30 includes packets up to 10:30:59.999999.
_DAY = re.compile(r"^\d{4}-\d{2}-\d{2}$")
_TIME = re.compile(r"^\d{4}-\d{2}-\d{2}[T ]\d{2}:\d{2}(?::\d{2}(?:\.\d{1,6})?)?$")


def timestamp_bound(value: str, *, end: bool) -> str:
    value = value.strip()
    if _DAY.fullmatch(value):
        dt = datetime.combine(date.fromisoformat(value), datetime.min.time())
        step = timedelta(days=1)
    elif _TIME.fullmatch(value):
        dt = datetime.fromisoformat(value)
        timepart = value[11:]
        if len(timepart) == 5:
            step = timedelta(minutes=1)
        elif "." not in timepart:
            step = timedelta(seconds=1)
        else:
            digits = len(timepart.split(".", 1)[1])
            step = timedelta(microseconds=10 ** (6 - digits))
    else:
        raise ValueError("expected YYYY-MM-DD or YYYY-MM-DDTHH:MM[:SS[.ffffff]]")
    if end:
        dt += step
    # Compare fixed-width, local-time timestamps lexically with the stored
    # datetime.now().isoformat(timespec='microseconds') strings.
    return dt.isoformat(timespec="microseconds")


def split_patterns(values: list[str]) -> list[str]:
    return [part.strip() for arg in values for part in arg.split(",") if part.strip()]


def opcode_name(value: Any) -> str:
    if isinstance(value, Enum):
        return value.name
    return str(value)


def view_value(value: Any, seen: set[int] | None = None) -> Any:
    """Turn nested decoded data into safe, readable Python literals."""
    if seen is None:
        seen = set()
    if isinstance(value, (str, int, float, bool, type(None))):
        return value
    if isinstance(value, Enum):
        return f"{type(value).__name__}.{value.name} ({value.value})"
    if isinstance(value, (bytes, bytearray, memoryview)):
        data = bytes(value)
        return f"0x{data.hex(' ')}"
    ident = id(value)
    if ident in seen:
        return "<recursive reference>"
    seen.add(ident)
    try:
        if is_dataclass(value) and not isinstance(value, type):
            return {f.name: view_value(getattr(value, f.name), seen) for f in fields(value)}
        if isinstance(value, Mapping):
            return {str(k): view_value(v, seen) for k, v in value.items()}
        if isinstance(value, (list, tuple, set, frozenset)):
            return [view_value(v, seen) for v in value]
        if hasattr(value, "__dict__"):
            return {k: view_value(v, seen) for k, v in vars(value).items() if not k.startswith("_")}
        return repr(value)
    finally:
        seen.remove(ident)


def hexdump(payload: bytes, max_bytes: int) -> str:
    shown = payload[:max_bytes] if max_bytes > 0 else payload
    lines: list[str] = []
    for pos in range(0, len(shown), 16):
        chunk = shown[pos : pos + 16]
        hexcol = " ".join(f"{b:02x}" for b in chunk)
        ascii_col = "".join(chr(b) if 32 <= b <= 126 else "." for b in chunk)
        lines.append(f"  {pos:06x}  {hexcol:<47}  |{ascii_col}|")
    if not lines:
        lines.append("  <empty payload>")
    if len(payload) > len(shown):
        lines.append(f"  ... {len(payload) - len(shown)} more bytes (use --max-bytes 0 for all)")
    return "\n".join(lines)


class Viewer:
    def __init__(self, database: Path) -> None:
        # Read-only: does not interfere with the running recorder or modify schema.
        uri = "file:" + quote(str(database.resolve()), safe="/") + "?mode=ro"
        self.db = sqlite3.connect(uri, uri=True, timeout=5)
        self.db.row_factory = sqlite3.Row
        self.db.execute("PRAGMA query_only=ON")
        self.only: list[str] = []
        self.exclude: list[str] = []
        self.start: str | None = None
        self.end: str | None = None
        self.character: str | None = None
        self.direction: str | None = None
        self.last: int = 100
        self.max_bytes: int = 256
        self.show_hex: bool = False

    def close(self) -> None:
        self.db.close()

    def rows(self) -> list[sqlite3.Row]:
        tests: list[str] = []
        args: list[Any] = []
        if self.character:
            tests.append('"Character" = ?')
            args.append(self.character)
        if self.direction:
            tests.append('"Direction" = ?')
            args.append(self.direction)
        if self.start:
            tests.append('"TimeSeen" >= ?')
            args.append(self.start)
        if self.end:
            tests.append('"TimeSeen" < ?')
            args.append(self.end)
        if self.only:
            tests.append("(" + " OR ".join('"Op_Code" GLOB ?' for _ in self.only) + ")")
            args.extend(self.only)
        if self.exclude:
            tests.extend('"Op_Code" NOT GLOB ?' for _ in self.exclude)
            args.extend(self.exclude)
        where = " WHERE " + " AND ".join(tests) if tests else ""
        select = 'SELECT rowid AS _id, "TimeSeen", "Character", "Op_Code", "Direction", "Bytes" FROM packets'
        if self.last:
            # Take the newest N *matching* rows, then display oldest-to-newest.
            query = (
                f'SELECT * FROM ({select}{where} ORDER BY "TimeSeen" DESC, _id DESC LIMIT ?) '
                'ORDER BY "TimeSeen", _id'
            )
            args.append(self.last)
        else:
            query = f'{select}{where} ORDER BY "TimeSeen", _id'
        return self.db.execute(query, args).fetchall()

    def print_packets(self) -> None:
        rows = self.rows()
        print(f"\n{len(rows)} packet(s) shown (oldest first); registry has {len(OPERATIONS)} opcode(s).")
        for row in rows:
            payload = bytes(row["Bytes"])
            code = str(row["Op_Code"])
            struct_type = OPERATIONS.get(code)
            print(
                f'\n[{row["_id"]}] {row["TimeSeen"]}  '
                f'{row["Direction"]:>4}  {row["Character"]}  {code}  ({len(payload)} bytes)'
            )
            if struct_type is None:
                print("  [no decoder registered]")
                print(hexdump(payload, self.max_bytes))
                continue
            try:
                decoded = struct_type.deserialize(payload)
                name = getattr(struct_type, "__name__", str(struct_type))
                formatted = pprint.pformat(view_value(decoded), indent=2, width=110, sort_dicts=False)
                print(f"  {name}:\n" + "\n".join("    " + line for line in formatted.splitlines()))
            except Exception as exc:
                print(f"  [decode error: {type(exc).__name__}: {exc}]")
                print(hexdump(payload, self.max_bytes))
                continue
            if self.show_hex:
                print(hexdump(payload, self.max_bytes))
        print()

    def show_filters(self) -> None:
        print(
            f"only={self.only or '*'}  exclude={self.exclude or '-'}\n"
            f"start={self.start or '-'}  end(exclusive)={self.end or '-'}\n"
            f"character={self.character or '*'}  direction={self.direction or '*'}  "
            f"last={self.last or 'all'}  hex={'on' if self.show_hex else 'off'}  "
            f"max_bytes={self.max_bytes or 'all'}"
        )


class Shell(cmd.Cmd):
    intro = "EQ capture viewer. Type help for commands. Type show to refresh packets."
    prompt = "eqcap> "

    def __init__(self, viewer: Viewer):
        super().__init__()
        self.v = viewer

    def do_show(self, arg: str) -> None:
        """show                         Display matching packets, oldest first."""
        self.v.print_packets()

    def do_only(self, arg: str) -> None:
        """only OP_Consider,OP_Spawn*     Include matching opcode(s); 'only all' clears."""
        self.v.only = [] if arg.strip().lower() in ("all", "off", "-") else split_patterns([arg])
        self.v.show_filters()

    def do_exclude(self, arg: str) -> None:
        """exclude OP_KeepAlive,OP_Foo  Exclude opcode(s); 'exclude all' clears."""
        self.v.exclude = [] if arg.strip().lower() in ("all", "off", "-") else split_patterns([arg])
        self.v.show_filters()

    def do_start(self, arg: str) -> None:
        """start YYYY-MM-DD[THH:MM]    Set lower timestamp; 'start off' clears."""
        if arg.strip().lower() in ("off", "all", "-"):
            self.v.start = None
        else:
            self.v.start = timestamp_bound(arg, end=False)
        self.v.show_filters()

    def do_end(self, arg: str) -> None:
        """end YYYY-MM-DD[THH:MM]      Set inclusive upper timestamp; 'end off' clears."""
        if arg.strip().lower() in ("off", "all", "-"):
            self.v.end = None
        else:
            self.v.end = timestamp_bound(arg, end=True)
        self.v.show_filters()

    def do_direction(self, arg: str) -> None:
        """direction recv|send|all      Filter by direction."""
        value = arg.strip().lower()
        if value not in ("recv", "send", "all", "off"):
            raise ValueError("choose recv, send, or all")
        self.v.direction = value if value in ("recv", "send") else None
        self.v.show_filters()

    def do_character(self, arg: str) -> None:
        """character Name|all           Filter by character (case sensitive)."""
        self.v.character = None if arg.strip().lower() in ("all", "off", "-") else arg.strip()
        self.v.show_filters()

    def do_last(self, arg: str) -> None:
        """last N                       Show newest N matches in time order; 0 shows all."""
        self.v.last = nonnegative_int(arg.strip())
        self.v.show_filters()

    def do_hex(self, arg: str) -> None:
        """hex on|off                   Also show hex dumps for decoded packets."""
        value = arg.strip().lower()
        if value not in ("on", "off"):
            raise ValueError("choose on or off")
        self.v.show_hex = value == "on"
        self.v.show_filters()

    def do_filters(self, arg: str) -> None:
        """filters                      Print current filters."""
        self.v.show_filters()

    def do_clear(self, arg: str) -> None:
        """clear                        Clear all opcode/date/character/direction filters."""
        self.v.only = []
        self.v.exclude = []
        self.v.start = self.v.end = self.v.character = self.v.direction = None
        self.v.show_filters()

    def do_quit(self, arg: str) -> bool:
        """quit                         Exit."""
        return True

    do_exit = do_quit

    def do_EOF(self, arg: str) -> bool:
        print()
        return True

    def emptyline(self) -> bool:
        return False

    def onecmd(self, line: str) -> bool:
        # Keep invalid interactive commands from terminating the viewer.
        try:
            return super().onecmd(line)
        except (ValueError, sqlite3.Error) as exc:
            print(f"Error: {exc}")
            return False


def nonnegative_int(value: str) -> int:
    result = int(value)
    if result < 0:
        raise ValueError("must be >= 0")
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("database", type=Path, help="Path to bus.sqlite3")
    parser.add_argument(
        "--only", action="append", default=[], help="Include opcodes (comma-separated, * wildcards); repeatable"
    )
    parser.add_argument(
        "--exclude", action="append", default=[], help="Exclude opcodes (comma-separated, * wildcards); repeatable"
    )
    parser.add_argument("--start", help="Lower bound: YYYY-MM-DD or YYYY-MM-DDTHH:MM[:SS[.ffffff]]")
    parser.add_argument("--end", help="Inclusive end date/time, at the entered precision")
    parser.add_argument("--character", help="Only this character")
    parser.add_argument("--direction", choices=["send", "recv"], help="Only sent or received packets")
    parser.add_argument(
        "--last",
        type=nonnegative_int,
        default=100,
        metavar="N",
        help="Newest N matching packets, displayed oldest first (0=all; default 100)",
    )
    parser.add_argument(
        "--max-bytes",
        type=nonnegative_int,
        default=256,
        metavar="N",
        help="Max bytes in each hexdump (0=all; default 256)",
    )
    parser.add_argument("--hex", action="store_true", help="Show hex dump even for successfully decoded packets")
    parser.add_argument("-i", "--interactive", action="store_true", help="Interactive filter/refresh shell")
    args = parser.parse_args()

    try:
        viewer = Viewer(args.database)
    except (ValueError, TypeError, ImportError, AttributeError, sqlite3.Error, OSError) as exc:
        parser.error(str(exc))

    try:
        viewer.only = split_patterns(args.only)
        viewer.exclude = split_patterns(args.exclude)
        viewer.start = timestamp_bound(args.start, end=False) if args.start else None
        viewer.end = timestamp_bound(args.end, end=True) if args.end else None
        viewer.character = args.character
        viewer.direction = args.direction
        viewer.last = args.last
        viewer.max_bytes = args.max_bytes
        viewer.show_hex = args.hex
        if viewer.start and viewer.end and viewer.start >= viewer.end:
            parser.error("--start must be before the end of --end's interval")
        viewer.print_packets()
        if args.interactive:
            Shell(viewer).cmdloop()
    except (ValueError, sqlite3.Error) as exc:
        parser.error(str(exc))
    finally:
        viewer.close()


if __name__ == "__main__":
    main()
