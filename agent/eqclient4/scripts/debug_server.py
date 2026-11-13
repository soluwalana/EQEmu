"""Manual RoF2 packet debugging over HTTP. Run from agent/:

    EQEMU_USER=... EQEMU_PASS=... EQEMU_CHAR=Hero \
        python -m eqclient4.scripts.debug_server

Requires FastAPI, Pydantic >= 2 and uvicorn. The API binds to loopback only.
The normal login/zone handshake runs before the HTTP listener starts.
"""

from __future__ import annotations

import argparse
import math
import os
import sqlite3
import struct
import threading
import time
from dataclasses import dataclass, fields, is_dataclass, replace
from datetime import datetime
from functools import lru_cache
from pathlib import Path
from queue import Empty, Full, Queue
from typing import Annotated, Any, Callable
from uuid import uuid4

import uvicorn
from fastapi import Body, FastAPI, HTTPException, Query
from pydantic import TypeAdapter, ValidationError

from eqclient4.log import log
from eqclient4.loop import Loop, PULSE
from eqclient4.net.client import Client, Login, connect, enter
from eqclient4.net.sheet import CreateCharacter, build
from eqclient4.structs import EQStruct, OPERATIONS, bytes_to_eqstruct
from eqclient4.world import Mob, World
from eqclient4.structs.items import Item


@dataclass
class Command:
    id: str
    packet: EQStruct
    payload: bytes
    state: str = "queued"
    error: str | None = None


class Commands:
    def __init__(self) -> None:
        self.pending: Queue[Command] = Queue(maxsize=256)
        self._commands: dict[str, Command] = {}
        self._lock = threading.Lock()
        self.ready = threading.Event()

    def submit(self, packet: EQStruct, payload: bytes) -> dict[str, Any]:
        with self._lock:
            if not self.ready.is_set():
                raise HTTPException(503, "Zone session is not ready")
            command = Command(uuid4().hex, packet, payload)
            try:
                self.pending.put_nowait(command)
            except Full as exc:
                raise HTTPException(503, "Command queue is full") from exc
            self._commands[command.id] = command
            # Keep the latest 4096 completed commands, in addition to pending ones.
            if len(self._commands) > 4352:
                for key, old in list(self._commands.items()):
                    if len(self._commands) <= 4096:
                        break
                    if old.state in ("sent", "failed"):
                        del self._commands[key]
            return self._snapshot(command)

    def status(self, command_id: str) -> dict[str, Any]:
        with self._lock:
            command = self._commands.get(command_id)
            if command is None:
                raise HTTPException(404, "Unknown command ID")
            return self._snapshot(command)

    def finish(self, command: Command, state: str, error: str | None = None) -> None:
        with self._lock:
            command.state = state
            command.error = error

    def stop(self) -> None:
        with self._lock:
            self.ready.clear()
            while True:
                try:
                    command = self.pending.get_nowait()
                except Empty:
                    break
                command.state = "failed"
                command.error = "Debug loop stopped before dispatch"

    @staticmethod
    def _snapshot(command: Command) -> dict[str, Any]:
        return {"id": command.id, "opcode": command.packet.opcode,
                "state": command.state, "error": command.error}


class DebugLoop(Loop):
    """Use the real session and bus, but never restore or step gameplay actions."""

    def __init__(self, world: World, login: Login, creation: CreateCharacter,
                 commands: Commands) -> None:
        self.commands = commands
        self.state_lock = threading.Lock()
        super().__init__(world, login, creation)
        self._transferred = False
        # Client.pump normally drops unrecognized wire numbers. Capture at
        # on_app instead, including the zone-in inbox already accumulated by enter.
        for number, payload in self.client._inbox:
            self._record_inbound(number, payload)
        self.client.listen(self._record_inbound)

    def _record_inbound(self, number: int, payload: bytes) -> None:
        name = self.client._opcode_name(number) or f"UNKNOWN_0x{number:04x}"
        self.capture.record("recv", name, payload)

    def start(self, login: Login, creation: CreateCharacter) -> Client:
        # Loop.start also restores durable actions. Deliberately skip that part.
        session = connect(login, creation)
        if not session:
            raise ConnectionError("Failed to connect to server")
        client = enter(session, creation)
        if not client:
            raise ConnectionError("Failed to enter server")
        return client

    def run_once(self) -> None:
        with self.state_lock:
            self._debug_pulse()

    def _debug_pulse(self) -> None:
        self.tick += 1
        if self.session_open():
            self._transferred = False
        else:
            self.commands.ready.clear()

        # Same bus path as Loop.run_once. The on_app listener captures raw packets.
        for opcode, payload in self.client.pump(PULSE):
            self.recv_count += 1
            self.world.inventory.tick = self.recv_count
            self.bus.publish(opcode, payload)

        # Flush protocol responses first (e.g. server-requested zone changes).
        # No action stepping or automatic idle movement.
        self._flush()
        if self.session_open() and not self._transferred:
            self.commands.ready.set()
            self._dispatch()
        else:
            self.commands.ready.clear()
        self.capture.commit()

    def _dispatch(self) -> None:
        # One command per pulse; inbound traffic always gets another turn.
        try:
            command = self.commands.pending.get_nowait()
        except Empty:
            return
        before = self.sent_count
        try:
            # Already validated and serialized by the HTTP endpoint. Use Loop's
            # real outbound queue, not Client.send or the socket directly.
            self.send(command.packet.opcode, command.payload)
            self._flush()
            self.capture.commit()
            if self.sent_count == before + 1:
                self.commands.finish(command, "sent")
            else:
                self.commands.finish(command, "failed", "Session closed before send completed")
        except Exception as exc:
            self.commands.finish(command, "failed", str(exc))
            raise


@lru_cache(maxsize=None)
def adapter(opcode: str) -> TypeAdapter:
    return TypeAdapter(OPERATIONS[opcode])


def json_value(value: Any) -> Any:
    """Lossless representation of bytes, including nested packet records."""
    if isinstance(value, (bytes, bytearray, memoryview)):
        return {"hex": bytes(value).hex()}
    if is_dataclass(value) and not isinstance(value, type):
        return {f.name: json_value(getattr(value, f.name)) for f in fields(value)}
    if isinstance(value, dict):
        return {str(k): json_value(v) for k, v in value.items()}
    if isinstance(value, (tuple, list, set, frozenset)):
        return [json_value(v) for v in value]
    if isinstance(value, float) and not math.isfinite(value):
        return str(value)
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    return str(value)


def input_value(value: Any) -> Any:
    """Accept arbitrary binary fields as {"hex": "..."}, not just UTF-8 strings."""
    if isinstance(value, dict):
        if value.keys() == {"hex"} and isinstance(value["hex"], str):
            return bytes.fromhex(value["hex"])
        return {key: input_value(item) for key, item in value.items()}
    if isinstance(value, list):
        return [input_value(item) for item in value]
    return value


def timestamp(value: datetime) -> str:
    # Capture uses local naive datetime.now(), not UTC. Normalize explicit
    # offsets to local time before using its ISO timestamp index.
    if value.tzinfo is not None:
        value = value.astimezone().replace(tzinfo=None)
    return value.isoformat(timespec="microseconds")


def item_snapshot(item: Item) -> dict[str, Any]:
    # The inventory index supplies the current location. Do not repeat the
    # received header/address, recursive children, or original wire buffers.
    return {
        **{f.name: json_value(getattr(item, f.name)) for f in fields(item)
           if not f.name.startswith("_") and f.name not in {"children", "address", "slot"}},
        "classes": item.classes,
    }


def mob_snapshot(mob: Mob) -> dict[str, Any]:
    return json_value({
        **{key: value for key, value in vars(mob).items() if not key.startswith("_")},
        "spawn_id": mob.spawn_id,
        "position": mob.position,
        "spoken_name": mob.spoken_name(),
        "is_treasure": mob.is_treasure,
    })


def world_snapshot(world: World) -> dict[str, Any]:
    return json_value({
        "zone": world.zone,
        "zone_id": world.zone_id,
        "zone_formed": world.zone_formed,
        "self_id": world.self_id,
        "position": world.position,
        "safe": world.safe,
        "at_water": world.at_water,
        "mobs": {key: mob_snapshot(mob) for key, mob in world.mobs.items()},
        "aggro_mobs": list(world.aggro_mobs),
        "doors": world.doors,
        "ground_spawns": world.ground_spawns,
        "active_merchants": {
            key: {"npc_id": merchant.npc_id, "is_open": merchant.is_open,
                  "items": {slot: item_snapshot(item) for slot, item in merchant.items.items()}}
            for key, merchant in world.active_merchants.items()
        },
        "tasks": world.tasks.tasks,
        "task_activities": world.tasks.activities,
        "discovered_factions": {key: vars(value) for key, value in world.discovered_factions.items()},
    })


def inventory_snapshot(world: World) -> dict[str, Any]:
    inventory = world.inventory
    return {
        "loaded": inventory.loaded,
        "dirty": inventory.dirty,
        "tick": inventory.tick,
        "slots": [
            {"address": json_value(address), "client_slot": address.client_slot,
             "item": item_snapshot(item)}
            for address, item in inventory.items()
        ],
    }


def character_snapshot(world: World, include_aa_ranks: bool = False) -> dict[str, Any]:
    character = world.character
    excluded = {"abilities", "changes"}
    if not include_aa_ranks:
        excluded.add("aa_ranks")
    return json_value({
        **{key: value for key, value in vars(character).items()
           if not key.startswith("_") and key not in excluded},
        "coin": dict(zip(("platinum", "gold", "silver", "copper"), character.coin)),
        "total_copper": character.total_copper,
        "skills": character.abilities.skills,
        "zone": world.zone,
        "position": world.position,
    })


def create_app(commands: Commands, capture: Path, character: str,
               opcodes: dict[str, int], loop: DebugLoop | None = None) -> FastAPI:
    app = FastAPI(title="EQClient4 packet debugger")
    available = {name for name, cls in OPERATIONS.items()
                 if opcodes.get(name) and is_dataclass(cls)}

    def check_opcode(opcode: str) -> None:
        if opcode not in available:
            raise HTTPException(404, f"No registered RoF2 application struct for {opcode}")

    def query(sql: str, values: list[Any]) -> list[sqlite3.Row]:
        # Each HTTP request opens its own read-only connection; the capture's
        # writer and its sqlite connection remain on the EQ loop thread.
        db = sqlite3.connect(capture.resolve().as_uri() + "?mode=ro", uri=True, timeout=5)
        try:
            db.row_factory = sqlite3.Row
            return db.execute(sql, values).fetchall()
        finally:
            db.close()

    def where(direction: str, opcode: list[str] | None, since: datetime | None,
              until: datetime | None, after_id: int = 0) -> tuple[str, list[Any]]:
        clauses = ["Character = ?", "rowid > ?"]
        values: list[Any] = [character, after_id]
        if direction not in ("recv", "send", "all"):
            raise HTTPException(422, "direction must be recv, send or all")
        if direction != "all":
            clauses.append("Direction = ?")
            values.append(direction)
        if opcode:
            clauses.append("Op_Code IN (" + ",".join("?" for _ in opcode) + ")")
            values.extend(opcode)
        if since is not None:
            clauses.append("TimeSeen >= ?")
            values.append(timestamp(since))
        if until is not None:
            clauses.append("TimeSeen <= ?")
            values.append(timestamp(until))
        if since is not None and until is not None and timestamp(since) > timestamp(until):
            raise HTTPException(422, "since must not be after until")
        return " WHERE " + " AND ".join(clauses), values

    @app.get("/health")
    def health() -> dict[str, Any]:
        return {"character": character, "ready": commands.ready.is_set(),
                "pending": commands.pending.qsize(), "capture": str(capture)}

    def snapshot(build_snapshot: Callable[[World], Any]) -> Any:
        if loop is None:
            raise HTTPException(503, "World state is not available")
        # The EQ loop is the only writer. Copy to detached JSON-compatible
        # data under the lock; FastAPI encodes the response after releasing it.
        if not loop.state_lock.acquire(timeout=2.0):
            raise HTTPException(503, "World state busy (possibly zoning)")
        try:
            return build_snapshot(loop.world)
        finally:
            loop.state_lock.release()

    @app.get("/world")
    def get_world() -> dict[str, Any]:
        return snapshot(world_snapshot)

    @app.get("/world/mobs")
    def get_mobs(name: str | None = None, npc: bool | None = None,
                 distance: Annotated[float | None, Query(ge=0)] = None) -> list[dict[str, Any]]:
        def select(world: World) -> list[dict[str, Any]]:
            return [mob_snapshot(mob) for mob in world.mobs.values()
                    if (name is None or name.casefold() in mob.name.casefold()
                        or name.casefold() in mob.spoken_name().casefold())
                    and (npc is None or bool(mob.npc) == npc)
                    and (distance is None or mob.distance <= distance)]
        return snapshot(select)

    @app.get("/world/mobs/{spawn_id}")
    def get_mob(spawn_id: int) -> dict[str, Any]:
        def select(world: World) -> dict[str, Any]:
            mob = world.mobs.get(spawn_id)
            if mob is None:
                raise HTTPException(404, "Unknown spawn ID")
            return mob_snapshot(mob)
        return snapshot(select)

    @app.get("/inventory")
    def get_inventory() -> dict[str, Any]:
        return snapshot(inventory_snapshot)

    @app.get("/item")
    @app.get("/item/{item_id}")
    def get_item(item_id: int) -> dict[str, Any]:
        def select(world: World) -> dict[str, Any]:
            item = world.item_book.get(item_id)
            if item is None:
                raise HTTPException(404, f"Unknown item ID: {item_id}")
            return item_snapshot(item)
        return snapshot(select)

    @app.get("/character")
    def get_character(include_aa_ranks: bool = False) -> dict[str, Any]:
        return snapshot(lambda world: character_snapshot(world, include_aa_ranks))

    @app.get("/schemas")
    def schemas() -> list[str]:
        return sorted(available)

    @app.get("/schemas/{opcode}")
    def schema(opcode: str) -> dict[str, Any]:
        check_opcode(opcode)
        try:
            return adapter(opcode).json_schema()
        except Exception as exc:
            raise HTTPException(422, f"Cannot generate schema for {opcode}: {exc}") from exc

    @app.post("/send/{opcode}", status_code=202)
    def send(opcode: str, payload: Annotated[dict[str, Any], Body()]) -> dict[str, Any]:
        check_opcode(opcode)
        cls = OPERATIONS[opcode]
        if not is_dataclass(cls):
            raise HTTPException(422, f"{opcode} is not a dataclass")
        allowed = {f.name for f in fields(cls) if f.init}
        extra = payload.keys() - allowed
        if extra:
            raise HTTPException(422, f"Unknown fields: {', '.join(sorted(extra))}")
        try:
            packet = adapter(opcode).validate_python(input_value(payload))
            raw = packet.serialize()
            if not isinstance(raw, bytes):
                raise TypeError("Packet serializer did not return bytes")
        except ValidationError as exc:
            raise HTTPException(422, exc.errors(include_context=False, include_url=False,
                                               include_input=False)) from exc
        except (ValueError, TypeError, OverflowError, struct.error) as exc:
            raise HTTPException(422, f"Invalid {opcode} payload: {exc}") from exc
        return commands.submit(packet, raw)

    @app.get("/commands/{command_id}")
    def command_status(command_id: str) -> dict[str, Any]:
        return commands.status(command_id)

    @app.get("/opcodes")
    def received_opcodes(direction: str = "recv", since: datetime | None = None,
                         until: datetime | None = None) -> list[dict[str, Any]]:
        clause, values = where(direction, None, since, until)
        rows = query("SELECT Op_Code AS opcode, count(*) AS count, "
                     "min(TimeSeen) AS first_seen, max(TimeSeen) AS last_seen "
                     "FROM packets" + clause + " GROUP BY Op_Code ORDER BY Op_Code", values)
        return [dict(row) for row in rows]

    @app.get("/packets")
    def packets(
        opcode: Annotated[list[str] | None, Query()] = None,
        direction: str = "recv",
        since: datetime | None = None,
        until: datetime | None = None,
        after_id: Annotated[int, Query(ge=0)] = 0,
        limit: Annotated[int, Query(ge=1, le=1000)] = 100,
        decode: bool = True,
        raw: bool = True,
    ) -> dict[str, Any]:
        clause, values = where(direction, opcode, since, until, after_id)
        rows = query("SELECT rowid AS id, TimeSeen, Op_Code, Direction, Bytes "
                     "FROM packets" + clause + " ORDER BY rowid LIMIT ?", [*values, limit + 1])
        records: list[dict[str, Any]] = []
        for row in rows[:limit]:
            body = bytes(row["Bytes"])
            record: dict[str, Any] = {
                "id": row["id"], "timestamp": row["TimeSeen"],
                "opcode": row["Op_Code"], "direction": row["Direction"], "size": len(body),
            }
            if raw:
                record["payload_hex"] = body.hex()
            if decode:
                try:
                    parsed = bytes_to_eqstruct(row["Op_Code"], body)
                    record["payload"] = json_value(parsed) if parsed is not None else None
                    if parsed is None:
                        record["decode_error"] = "No struct or decode failed"
                except Exception as exc:
                    record["payload"] = None
                    record["decode_error"] = str(exc)
            records.append(record)
        return {"packets": records, "next_after_id": records[-1]["id"] if records else after_id,
                "has_more": len(rows) > limit}

    return app


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=8765)
    parser.add_argument("--capture", type=Path, help="New SQLite capture file (default: per-run)")
    args = parser.parse_args()
    name = os.environ.get("EQEMU_CHAR", "").strip()
    user = os.environ.get("EQEMU_USER", "").strip()
    password = os.environ.get("EQEMU_PASS", "")
    if not (name and user and password):
        parser.error("set EQEMU_USER, EQEMU_PASS and EQEMU_CHAR")
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S-%f")
    capture = (args.capture or Path.home() / ".eqclient" / "logs" / name /
               f"debug-{stamp}.sqlite3").expanduser().resolve()
    journal = capture.with_suffix(".journal.sqlite3")
    if capture.exists() or journal.exists():
        parser.error("--capture must name a new file to keep sessions separate")
    capture.parent.mkdir(parents=True, exist_ok=True)
    os.environ["EQEMU_CAPTURE"] = str(capture)
    # Protocol handlers may update journal flags; keep debug state separate.
    os.environ["EQEMU_JOURNAL_V3"] = str(journal)
    commands = Commands()
    creation = replace(build(), name=name)
    loop = DebugLoop(World(name), Login(character=name, user=user, password=password),
                     creation, commands)
    server: uvicorn.Server | None = None
    thread: threading.Thread | None = None
    try:
        loop.warm()
        loop.client.start_io()
        loop.run_once()
        app = create_app(commands, capture, name, dict(loop.client.opcodes), loop)
        server = uvicorn.Server(uvicorn.Config(app, host="127.0.0.1", port=args.port))
        thread = threading.Thread(target=server.run, name="eq-debug-http", daemon=True)
        thread.start()
        log.info("debug HTTP: http://127.0.0.1:%d/docs", args.port)
        while thread.is_alive():
            loop.run_once()
            if loop.client.closed:
                loop.run_once()
                if loop.client.closed:
                    log.info("debug session closed")
                    break
            # Client.pump may return immediately when disconnected or rezoning.
            if not loop.session_open():
                time.sleep(PULSE)
        if not server.started and not thread.is_alive():
            raise SystemExit("HTTP server failed to start")
    except KeyboardInterrupt:
        pass
    finally:
        commands.stop()
        if server is not None:
            server.should_exit = True
        try:
            loop.capture.close()
        finally:
            try:
                loop.client.close()
            finally:
                loop.journal.close()
        if thread is not None:
            thread.join(timeout=5)


if __name__ == "__main__":
    main()
