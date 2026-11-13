"""Manual RoF2 packet debugging over HTTP. Run from agent/:

    EQEMU_USER=... EQEMU_PASS=... EQEMU_CHAR=Hero \
        python -m eqclient4.scripts.debug_server

Requires FastAPI, Pydantic >= 2 and uvicorn. The API binds to loopback only.
The normal login/zone handshake runs before the HTTP listener starts.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib
import importlib.util
import inspect
import math
import os
import sqlite3
import struct
import sys
import threading
import time
from collections import deque
from dataclasses import dataclass, fields, is_dataclass, replace
from datetime import datetime
from functools import lru_cache
from pathlib import Path
from queue import Empty, Full, Queue
from types import ModuleType
from typing import Annotated, Any, Callable, get_type_hints
from uuid import uuid4

import uvicorn
from eqclient4.action import Action
from eqclient4.log import Capture, Direction, log
from eqclient4.loop import PULSE, Loop
from eqclient4.net.client import Client, Login, connect, enter
from eqclient4.net.sheet import CreateCharacter, build
from eqclient4.scripts.eqemu_trace_live import (
    Frame,
    PacketEvent,
    Source,
    display_event,
    split_patterns,
)
from eqclient4.structs import OPERATIONS, EQStruct, bytes_to_eqstruct
from eqclient4.structs.items import Item
from eqclient4.world import Mob, World
from fastapi import Body, FastAPI, HTTPException, Query
from pydantic import TypeAdapter, ValidationError


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
        return {
            "id": command.id,
            "opcode": command.packet.opcode,
            "state": command.state,
            "error": command.error,
        }


@dataclass(frozen=True)
class ActionModule:
    module: ModuleType
    version: str

    def classes(self) -> dict[str, type[Action]]:
        return {
            name: value
            for name, value in vars(self.module).items()
            if inspect.isclass(value)
            and value is not Action
            and issubclass(value, Action)
            and value.__module__ == self.module.__name__
            and not inspect.isabstract(value)
        }

    def describe(self) -> dict[str, Any]:
        return {
            "version": self.version,
            "generation": self.module.__name__,
            "classes": {
                name: {
                    "signature": str(inspect.signature(cls)),
                    "parameters": [
                        {
                            "name": p.name,
                            "annotation": str(p.annotation),
                            "required": p.default is inspect.Parameter.empty,
                            "injected": p.name in ("world", "loop"),
                        }
                        for p in inspect.signature(cls).parameters.values()
                    ],
                }
                for name, cls in self.classes().items()
            },
        }


class ActionModules:
    """Load local, trusted source into a fresh namespace for each changed version.

    Never mutate an existing module's globals or reload the persistent runtime.
    Dependencies imported by an action use their ordinary, canonical modules.
    """

    def __init__(self, root: Path | None = None) -> None:
        self.root = (root or Path(__file__).resolve().parents[1] / "actions").resolve()
        self._lock = threading.Lock()
        self._current: dict[str, ActionModule] = {}

    def names(self) -> list[str]:
        return sorted(
            p.stem
            for p in self.root.glob("*.py")
            if p.stem.isidentifier() and not p.stem.startswith("_")
        )

    def load(self, name: str, force: bool = False) -> ActionModule:
        if not name.isidentifier() or name.startswith("_"):
            raise HTTPException(404, "Unknown action module")
        path = (self.root / f"{name}.py").resolve()
        if path.parent != self.root or not path.is_file():
            raise HTTPException(404, f"Unknown action module: {name}")
        with self._lock:
            try:
                source = path.read_bytes()
                version = hashlib.sha256(source).hexdigest()[:16]
                current = self._current.get(name)
                if not force and current is not None and current.version == version:
                    return current
                importlib.import_module("eqclient4.actions")
                # A unique name also allows a reverted file or a forced reload
                # without replacing any old class's module namespace.
                qualified = f"eqclient4.actions._debug_{name}_{version}_{uuid4().hex[:8]}"
                spec = importlib.util.spec_from_file_location(qualified, path)
                if spec is None:
                    raise ImportError(f"Cannot load {path}")
                module = importlib.util.module_from_spec(spec)
                # The action modules use TYPE_CHECKING imports for these types.
                # Supply them only in the fresh debug namespace, so both eager
                # and deferred constructor annotations remain introspectable.
                module.__dict__.update(World=World, Loop=Loop, Mob=Mob)
                # dataclasses and typing need their module present during exec.
                sys.modules[qualified] = module
                try:
                    exec(compile(source, str(path), "exec"), module.__dict__)
                except BaseException:
                    sys.modules.pop(qualified, None)
                    raise
                result = ActionModule(module, version)
                self._current[name] = result
                return result
            except (Exception, SystemExit) as exc:
                raise HTTPException(
                    422, f"Cannot load {name}: {type(exc).__name__}: {exc}"
                ) from exc


@dataclass
class ActionRun:
    id: str
    module: str
    name: str
    version: str
    cls: type[Action]
    params: dict[str, Any]
    action: Action | None = None
    state: str = "queued"
    error: str | None = None
    cancel_requested: bool = False

    def snapshot(self, mailbox: bool = False) -> dict[str, Any]:
        result: dict[str, Any] = {
            "id": self.id,
            "module": self.module,
            "class_name": self.name,
            "version": self.version,
            "generation": self.cls.__module__,
            "state": self.state,
            "error": self.error,
            "params": json_value(self.params),
        }
        if self.action is not None:
            result.update(action_snapshot(self.action, mailbox))
        return result


def action_snapshot(action: Action, mailbox: bool = False) -> dict[str, Any]:
    result: dict[str, Any] = {
        "insert": action.insert,
        "class_name": type(action).__name__,
        "source": action.source,
        "priority": action.priority,
        "started": action.started,
        "zone": action.zone,
        "completed": action.completed,
        "suspended": action.suspended,
        "yielding": action.yielding,
        "waiting": json_value(action.waiting),
        "mailbox_size": len(action.messages),
    }
    if mailbox:
        result["messages"] = [
            {"opcode": msg.opcode, "payload": json_value(msg)} for msg in action.messages
        ]
    return result


def construct_action(run: ActionRun, world: World, loop: Loop) -> Action:
    """Resolve constructor arguments on the EQ owner thread, not an HTTP thread."""
    cls = run.cls
    signature = inspect.signature(cls)
    params = dict(run.params)
    if params.keys() & {"world", "loop"}:
        raise ValueError("world and loop are injected by the server")
    for name, value in (("world", world), ("loop", loop)):
        if name in signature.parameters:
            params[name] = value
    bound = signature.bind(**params)
    # Existing modules put these imports behind TYPE_CHECKING. Resolve them
    # explicitly for postponed annotations without changing the action source.
    hints = get_type_hints(cls.__init__, localns={"World": World, "Loop": Loop, "Mob": Mob})
    for name in run.params:
        annotation = hints.get(name)
        value = bound.arguments[name]
        if annotation is Mob:
            if not isinstance(value, int) or isinstance(value, bool):
                raise ValueError(f"{name} must be a live spawn ID")

            mob = world.mobs.get(value)
            if mob is None:
                raise ValueError(f"Unknown live spawn ID: {value}")
            bound.arguments[name] = mob
        elif annotation is not None:
            bound.arguments[name] = TypeAdapter(annotation).validate_python(input_value(value))
    action = cls(*bound.args, **bound.kwargs)
    if getattr(action, "_world", None) is not world or getattr(action, "_loop", None) is not loop:
        raise TypeError("Action must initialize its base with the live world and loop")
    return action


class VerboseCapture(Capture):
    """Keep SQLite capture authoritative; render live traces off the EQ thread."""

    def __init__(self, path: Path, character: str) -> None:
        super().__init__(path, character)
        self._events: Queue[PacketEvent] = Queue(maxsize=256)
        self._stop = threading.Event()
        self._dropped = 0
        self._source = Source(path, (0, 0))
        self._only = (
            split_patterns([os.environ["EQ_TRACE_ONLY"]]) if os.environ.get("EQ_TRACE_ONLY") else []
        )
        self._exclude = (
            split_patterns([os.environ["EQ_TRACE_EXCLUDE"]])
            if os.environ.get("EQ_TRACE_EXCLUDE")
            else []
        )
        self._args = argparse.Namespace(direction=None, stage="client", max_bytes=128, hex=False)
        self._thread = threading.Thread(target=self._render, name="eq-debug-trace", daemon=True)
        self._thread.start()

    def record(self, direction: Direction, opcode: str, payload: bytes) -> None:
        super().record(direction, opcode, payload)
        frame = Frame(
            time.time_ns() // 1000,
            0 if direction == "recv" else 1,
            1,
            opcode,
            self.character,
            payload,
        )
        try:
            self._events.put_nowait(PacketEvent(self._source, frame))
        except Full:
            self._dropped += 1
            if self._dropped == 1:
                log.warning("live trace output overloaded; SQLite still captures every packet")

    def _render(self) -> None:
        from eqclient4.character import Character
        from eqclient4.inventory import CharacterInventory

        inventories: dict[Source, CharacterInventory] = {}
        profiles: dict[Source, Character] = {}
        while not self._stop.is_set() or not self._events.empty():
            try:
                event = self._events.get(timeout=0.1)
            except Empty:
                continue
            try:
                display_event(
                    event,
                    self._args,
                    self._only,
                    self._exclude,
                    None,
                    None,
                    inventories,
                    profiles,
                    False,
                )
            except Exception:
                log.exception("live trace rendering failed for %s", event.frame.opcode)
            finally:
                self._events.task_done()

    def close(self) -> None:
        try:
            super().close()
        finally:
            self._stop.set()
            self._thread.join(timeout=2)
            if self._dropped:
                log.warning("live trace skipped %d packets; see SQLite capture", self._dropped)
            if self._thread.is_alive():
                log.warning("live trace output did not drain before shutdown")


class DebugLoop(Loop):
    """Use the real session, bus and scheduler, without restoring old actions."""

    def __init__(
        self, world: World, login: Login, creation: CreateCharacter, commands: Commands
    ) -> None:
        self.commands = commands
        self.state_lock = threading.Lock()
        self.action_runs: dict[str, ActionRun] = {}
        self.pending_actions: deque[ActionRun] = deque()
        self._failed_actions: set[int] = set()
        self._action_movement = False
        super().__init__(world, login, creation)
        self._transferred = False
        if os.environ.get("EQ_TRACE", "").strip().upper() == "VERBOSE":
            # Loop creates its capture after login. Swap before the first pulse,
            # so queued zone-in packets and all later traffic are traced once.
            if isinstance(self.capture, Capture):
                path = self.capture.path
                self.capture.close()
                self.capture = VerboseCapture(path, self.character)
        # Loop.run_once captures named packets. The listener preserves only
        # unknown wire numbers, which Client.pump would otherwise discard.
        for number, payload in self.client._inbox:
            self._record_inbound(number, payload)
        self.client.listen(self._record_inbound)

    def _record_inbound(self, number: int, payload: bytes) -> None:
        if not self.client._opcode_name(number):
            self.capture.record("recv", f"UNKNOWN_0x{number:04x}", payload)

    def start(self, login: Login, creation: CreateCharacter) -> Client:
        # Loop.start also restores durable actions. Deliberately skip that part.
        session = connect(login, creation)
        if not session:
            raise ConnectionError("Failed to connect to server")
        client = enter(session, creation)
        if not client:
            raise ConnectionError("Failed to enter server")
        return client

    def run_once(self) -> Action | None:
        with self.state_lock:
            if not self.session_open():
                self.commands.ready.clear()
            self._apply_action_requests()
            # Do not duplicate the production scheduler: same priority,
            # yielding, mailbox delivery and completion behavior as the agent.
            winner = super().run_once()
            self._refresh_actions()
            if self.session_open() and not self._transferred:
                self.commands.ready.set()
                self._dispatch()
            else:
                self.commands.ready.clear()
            self.capture.commit()
            return winner

    def _finish(self) -> None:
        # Packet-only mode stays quiet. During action execution use the real
        # movement hold logic, including one final idle pulse after completion.
        active = self.active is not None
        if self.session_open() and (active or self._action_movement):
            self.world.movement.hold_if_idle(self)
        self._action_movement = active
        self._flush()
        self._report()
        self.capture.commit()

    def _step_action(self, action: Action) -> None:
        if not self.session_open() or self._transferred:
            return
        start = len(self.outbound)
        try:
            super()._step_action(action)
        except Exception as exc:
            # Drop packets queued by the failed step before the flush. This
            # does not undo earlier packets, game changes or child actions.
            del self.outbound[start:]
            log.exception("debug action %s failed", type(action).__name__)
            self._failed_actions.add(action.insert)
            for run in self.action_runs.values():
                if run.action is action:
                    run.state = "failed"
                    run.error = f"{type(exc).__name__}: {exc}"
                    break
            action.complete = True

    def drop(self, action: Action) -> None:
        if action.insert in self._failed_actions:
            self._failed_actions.discard(action.insert)
            self.queue.remove(action.insert)
            if action.source:
                self.journal.clear_source(action.source)
            return
        super().drop(action)

    def submit_action(self, run: ActionRun) -> dict[str, Any]:
        # Caller holds state_lock. Only record a request here: constructors and
        # scheduler mutations must run on the EQ thread.
        if not self.commands.ready.is_set():
            raise HTTPException(503, "Zone session is not ready")
        if len(self.pending_actions) >= 256:
            raise HTTPException(503, "Action request queue is full")
        self.pending_actions.append(run)
        self.action_runs[run.id] = run
        return run.snapshot()

    def _apply_action_requests(self) -> None:
        for run in self.action_runs.values():
            if not run.cancel_requested:
                continue
            run.cancel_requested = False
            try:
                if run.action is not None:
                    try:
                        run.action.suspend()
                    finally:
                        self.queue.remove(run.action.insert)
                        if run.action.source:
                            self.journal.clear_source(run.action.source)
                run.state = "cancelled"
            except Exception as exc:
                run.state = "failed"
                run.error = f"Cancellation cleanup failed: {exc}"
        if not self.session_open() or not self.pending_actions:
            return
        run = self.pending_actions.popleft()
        if run.state != "queued":
            return
        start = len(self.outbound)
        try:
            run.action = construct_action(run, self.world, self)
            if not self.append(run.action):
                raise ValueError("Schedule rejected action (duplicate or resolved source)")
            run.state = "scheduled"
        except Exception as exc:
            del self.outbound[start:]
            log.exception("debug action %s construction failed", run.name)
            run.state = "failed"
            run.error = f"{type(exc).__name__}: {exc}"

    def _refresh_actions(self) -> None:
        queued = {id(action) for action in self.queue}
        for run in self.action_runs.values():
            action = run.action
            if action is None or run.state in ("failed", "cancelled", "removed", "completed"):
                continue
            if action.completed:
                run.state = "completed"
            elif id(action) not in queued:
                run.state = "removed"
            elif action is self.active:
                run.state = "running"
            else:
                run.state = "suspended" if action.suspended else "scheduled"

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
        **{
            f.name: json_value(getattr(item, f.name))
            for f in fields(item)
            if not f.name.startswith("_") and f.name not in {"children", "address", "slot"}
        },
        "classes": item.classes,
    }


def mob_snapshot(mob: Mob) -> dict[str, Any]:
    return json_value(
        {
            **{key: value for key, value in vars(mob).items() if not key.startswith("_")},
            "spawn_id": mob.spawn_id,
            "position": mob.position,
            "spoken_name": mob.spoken_name,
            "is_treasure": mob.is_treasure,
        }
    )


def world_snapshot(world: World) -> dict[str, Any]:
    return json_value(
        {
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
                key: {
                    "npc_id": merchant.npc_id,
                    "is_open": merchant.is_open,
                    "items": {slot: item_snapshot(item) for slot, item in merchant.items.items()},
                }
                for key, merchant in world.active_merchants.items()
            },
            "tasks": world.tasks.tasks,
            "task_activities": world.tasks.activities,
            "discovered_factions": {
                key: vars(value) for key, value in world.discovered_factions.items()
            },
        }
    )


def inventory_snapshot(world: World) -> dict[str, Any]:
    inventory = world.inventory
    return {
        "loaded": inventory.loaded,
        "dirty": inventory.dirty,
        "tick": inventory.tick,
        "slots": [
            {
                "address": json_value(address),
                "client_slot": address.client_slot,
                "item": item_snapshot(item),
            }
            for address, item in inventory.items()
        ],
    }


def character_snapshot(world: World, include_aa_ranks: bool = False) -> dict[str, Any]:
    character = world.character
    excluded = {"abilities", "changes"}
    if not include_aa_ranks:
        excluded.add("aa_ranks")
    return json_value(
        {
            **{
                key: value
                for key, value in vars(character).items()
                if not key.startswith("_") and key not in excluded
            },
            "coin": dict(zip(("platinum", "gold", "silver", "copper"), character.coin)),
            "total_copper": character.total_copper,
            "skills": character.abilities.skills,
            "zone": world.zone,
            "position": world.position,
        }
    )


def create_app(
    commands: Commands,
    capture: Path,
    character: str,
    opcodes: dict[str, int],
    loop: DebugLoop | None = None,
) -> FastAPI:
    app = FastAPI(title="EQClient4 packet and action debugger")
    action_modules = ActionModules()
    available = {
        name for name, cls in OPERATIONS.items() if opcodes.get(name) and is_dataclass(cls)
    }

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

    def where(
        direction: str,
        opcode: list[str] | None,
        since: datetime | None,
        until: datetime | None,
        after_id: int = 0,
    ) -> tuple[str, list[Any]]:
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
        return {
            "character": character,
            "ready": commands.ready.is_set(),
            "pending": commands.pending.qsize(),
            "capture": str(capture),
        }

    def with_loop(fn: Callable[[DebugLoop], Any]) -> Any:
        if loop is None:
            raise HTTPException(503, "World state is not available")
        if not loop.state_lock.acquire(timeout=2.0):
            raise HTTPException(503, "World state busy (possibly zoning)")
        try:
            return fn(loop)
        finally:
            loop.state_lock.release()

    def snapshot(build_snapshot: Callable[[World], Any]) -> Any:
        return with_loop(lambda current: build_snapshot(current.world))

    @app.get("/actions/modules")
    def list_action_modules() -> list[str]:
        return action_modules.names()

    @app.get("/actions/modules/{module}")
    def describe_action_module(module: str) -> dict[str, Any]:
        return action_modules.load(module).describe()

    @app.post("/actions/reload/{module}")
    def reload_action_module(module: str) -> dict[str, Any]:
        return action_modules.load(module, force=True).describe()

    @app.post("/actions/{module}/{class_name}", status_code=202)
    def submit_action(
        module: str, class_name: str, params: Annotated[dict[str, Any], Body()]
    ) -> dict[str, Any]:
        loaded = action_modules.load(module)
        cls = loaded.classes().get(class_name)
        if cls is None:
            raise HTTPException(404, f"Unknown action class: {class_name}")
        if params.keys() & {"world", "loop"}:
            raise HTTPException(422, "world and loop are injected by the server")
        run = ActionRun(uuid4().hex, module, class_name, loaded.version, cls, params)
        return with_loop(lambda current: current.submit_action(run))

    @app.get("/actions")
    def list_actions() -> dict[str, Any]:
        return with_loop(
            lambda current: {
                "active": current.active.insert if current.active is not None else None,
                "queue": [action_snapshot(action) for action in current.queue],
                "runs": [run.snapshot() for run in current.action_runs.values()],
            }
        )

    def find_run(current: DebugLoop, action_id: str) -> ActionRun:
        run = current.action_runs.get(action_id)
        if run is None:
            raise HTTPException(404, "Unknown action ID")
        return run

    @app.get("/actions/{action_id}")
    def get_action(action_id: str) -> dict[str, Any]:
        return with_loop(lambda current: find_run(current, action_id).snapshot(mailbox=True))

    @app.delete("/actions/{action_id}", status_code=202)
    def cancel_action(action_id: str) -> dict[str, Any]:
        def cancel(current: DebugLoop) -> dict[str, Any]:
            run = find_run(current, action_id)
            if run.state not in ("completed", "failed", "cancelled", "removed"):
                run.cancel_requested = True
                run.state = "cancel_requested"
            return run.snapshot()

        return with_loop(cancel)

    @app.get("/world")
    def get_world() -> dict[str, Any]:
        return snapshot(world_snapshot)

    @app.get("/world/mobs")
    def get_mobs(
        name: str | None = None,
        npc: bool | None = None,
        distance: Annotated[float | None, Query(ge=0)] = None,
    ) -> list[dict[str, Any]]:
        def select(world: World) -> list[dict[str, Any]]:

            mobs = []
            for mob in world.mobs.values():
                name_check = (
                    not name
                    or name.casefold() in mob.name.casefold()
                    or name.casefold() in mob.spoken_name.casefold()
                )
                npc_check = not npc or bool(mob.npc) == npc
                distance_check = not distance or mob.distance <= distance
                if name_check and npc_check and distance_check:
                    mobs.append(mob_snapshot(mob))

            return mobs

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
            raise HTTPException(
                422, exc.errors(include_context=False, include_url=False, include_input=False)
            ) from exc
        except (ValueError, TypeError, OverflowError, struct.error) as exc:
            raise HTTPException(422, f"Invalid {opcode} payload: {exc}") from exc
        return commands.submit(packet, raw)

    @app.get("/commands/{command_id}")
    def command_status(command_id: str) -> dict[str, Any]:
        return commands.status(command_id)

    @app.get("/opcodes")
    def received_opcodes(
        direction: str = "recv", since: datetime | None = None, until: datetime | None = None
    ) -> list[dict[str, Any]]:
        clause, values = where(direction, None, since, until)
        rows = query(
            "SELECT Op_Code AS opcode, count(*) AS count, "
            "min(TimeSeen) AS first_seen, max(TimeSeen) AS last_seen "
            "FROM packets" + clause + " GROUP BY Op_Code ORDER BY Op_Code",
            values,
        )
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
        rows = query(
            "SELECT rowid AS id, TimeSeen, Op_Code, Direction, Bytes "
            "FROM packets" + clause + " ORDER BY rowid LIMIT ?",
            [*values, limit + 1],
        )
        records: list[dict[str, Any]] = []
        for row in rows[:limit]:
            body = bytes(row["Bytes"])
            record: dict[str, Any] = {
                "id": row["id"],
                "timestamp": row["TimeSeen"],
                "opcode": row["Op_Code"],
                "direction": row["Direction"],
                "size": len(body),
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
        return {
            "packets": records,
            "next_after_id": records[-1]["id"] if records else after_id,
            "has_more": len(rows) > limit,
        }

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
    capture = (
        (args.capture or Path.home() / ".eqclient" / "logs" / name / f"debug-{stamp}.sqlite3")
        .expanduser()
        .resolve()
    )
    journal = capture.with_suffix(".journal.sqlite3")
    if capture.exists() or journal.exists():
        parser.error("--capture must name a new file to keep sessions separate")
    capture.parent.mkdir(parents=True, exist_ok=True)
    os.environ["EQEMU_CAPTURE"] = str(capture)
    # Protocol handlers may update journal flags; keep debug state separate.
    os.environ["EQEMU_JOURNAL_V3"] = str(journal)
    commands = Commands()
    creation = replace(build(), name=name)
    loop = DebugLoop(
        World(name), Login(character=name, user=user, password=password), creation, commands
    )
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
