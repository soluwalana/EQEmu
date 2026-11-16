"""Read-only dashboard projections; mutations use the existing debug API."""

from __future__ import annotations

import inspect
import math
import struct
import threading
import time
import zlib
from pathlib import Path
from typing import Any, get_type_hints

from eqclient4.nav.maps import ZoneMap, _read_map
from eqclient4.nav.water import WaterMap
from eqclient4.structs import Door
from eqclient4.structs.constants import _WORN, CLASS_ID_TO_NAME, RACE_ID_TO_NAME
from eqclient4.world import Mob
from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import TypeAdapter

# Keep resource/combat traffic out of the general wire log. Unknown opcodes
# remain visible there, and the original capture is never filtered or altered.
COMBAT = frozenset(
    {
        "OP_MobHealth",
        "OP_HPUpdate",
        "OP_MobManaUpdate",
        "OP_MobEnduranceUpdate",
        "OP_ManaUpdate",
        "OP_EnduranceUpdate",
        "OP_ManaChange",
        "OP_Damage",
        "OP_CombatDamage",
        "OP_Death",
        "OP_Buff",
        "OP_BuffCreate",
        "OP_BuffFadeMsg",
        "OP_BeginCast",
        "OP_CastSpell",
        "OP_Action",
        "OP_Action2",
        "OP_InterruptCast",
        "OP_SpellEffect",
        "OP_EnvironmentalDamage",
        "OP_Animation",
        "OP_Consider",
        "OP_TargetBuffs",
        "OP_CombatAbility",
        "OP_AutoAttack",
        "OP_Taunt",
        "OP_BuffRemoveRequest",
        "OP_Stun",
        "OP_HealDamage",
    }
)


def install_dashboard(
    app: FastAPI,
    with_loop,
    query,
    character: str,
    item_snapshot,
    action_snapshot,
    json_value,
    decode_packet,
    action_modules,
) -> None:
    root = Path(__file__).with_name("debug_ui")
    app.mount("/dashboard/assets", StaticFiles(directory=root), name="dashboard-assets")
    from eqclient4.scripts.debug_geometry import install_geometry

    install_geometry(app)

    # The dashboard uses the same exact size-aware collision test as
    # World.line_of_sight, but never modifies the agent's spatial/ray caches.
    # All expensive work happens after releasing DebugLoop.state_lock.
    los_lock = threading.Lock()
    los_zone: str | None = None
    los_source: ZoneMap | None = None
    los_mesh: ZoneMap | None = None
    los_error = False
    los_results: dict[tuple, bool] = {}
    los_cursor = 0
    # Build the model index once per loaded item book, not on every UI poll.
    weapon_model_book = None
    weapon_models: frozenset[str] = frozenset()

    def annotate_los(data: dict, source: ZoneMap | None, water: WaterMap | None) -> dict:
        nonlocal los_zone, los_source, los_mesh, los_error, los_cursor
        with los_lock:
            zone = (data["zone"] or "").lower()
            if zone != los_zone or source is not los_source:
                los_zone, los_source = zone, source
                los_results.clear()
                los_cursor = 0
                los_error = False
                try:
                    # Collision triangles are immutable zone data. Give the
                    # dashboard its own ZoneMap index; no shared mutable cache.
                    los_mesh = ZoneMap(source.triangles) if source is not None else _read_map(zone)
                except (OSError, ValueError, struct.error, zlib.error):
                    los_mesh = None
                    los_error = True
            origin = tuple(data["position"])
            watcher_size = data["character"]["size"]
            pending = []
            # Bots first, then nearest mobs. Cache exact XYZ and entity sizes.
            for row in (*data["bots"], *data["mobs"]):
                row["los"] = None
                point = row["position"]
                if (
                    point is None
                    or row.get("dead")
                    or len(point) != 3
                    or not all(isinstance(v, (int, float)) and math.isfinite(v) for v in point)
                ):
                    continue
                if los_error:
                    continue
                if water is not None and not water.los_clear(origin, tuple(point)):
                    row["los"] = False
                    continue
                if los_mesh is None:
                    # Same missing-map fallback as World.line_of_sight.
                    row["los"] = True
                    continue
                key = (origin, tuple(point), watcher_size, row["size"])
                if key in los_results:
                    row["los"] = los_results[key]
                else:
                    pending.append((row, key))
            # Bound work per HTTP snapshot. Unchecked entities stay unknown,
            # not falsely blocked. Rotate through misses while moving.
            deadline = time.monotonic() + 0.025
            if pending and los_mesh is not None:
                start = los_cursor % len(pending)
                checked = 0
                for index in range(len(pending)):
                    if index and time.monotonic() >= deadline:
                        break
                    row, key = pending[(start + index) % len(pending)]
                    result = los_results.get(key)
                    if result is None:
                        result = los_mesh.clear(*key)
                        los_results[key] = result
                    row["los"] = result
                    checked += 1
                los_cursor = start + checked if checked < len(pending) else 0
            if len(los_results) > 32768:
                los_results.clear()
            data["los_map"] = los_mesh is not None
            data["los_error"] = los_error
        return data

    @app.get("/", include_in_schema=False)
    @app.get("/dashboard", include_in_schema=False)
    def dashboard():
        return FileResponse(root / "index.html")

    @app.get("/dashboard/state")
    def state():
        def collect(loop):
            nonlocal weapon_model_book, weapon_models
            w = loop.world
            if weapon_model_book is not w.item_book:
                weapon_model_book = w.item_book
                weapon_models = frozenset(
                    Door.normalize_model(item.id_file)
                    for item in w.item_book.by_id.values()
                    if item.id_file and item.damage > 0 and item.delay > 0
                )
            c = w.character
            pos = w.position
            move = w.movement
            exit_doors = w.exit_doors.get((w.zone or "").lower(), {})

            def distance(point):
                return math.dist(pos, point)

            def mob_row(m):
                return {
                    "id": m.spawn_id,
                    "name": m.spoken_name or m.name,
                    "raw_name": m.name,
                    "level": m.level,
                    "npc": m.npc,
                    "class_id": m.class_id,
                    "hp": m.hp,
                    "mana": m.mana,
                    "endurance": m.endurance,
                    "position": m.position,
                    "size": m.size,
                    "heading": m.heading,
                    "distance": distance(m.position),
                    "dead": m.dead,
                    "aggro": m.spawn_id in w.aggro_mobs,
                    "targeted": m.targeted,
                }

            bots = [
                {
                    "id": b.spawn_id,
                    "bot_id": b.id,
                    "name": b.name,
                    "class_id": b.class_id,
                    "level": b.level,
                    "hp": b.hp,
                    "mana": b.mana,
                    "endurance": b.endurance,
                    "position": b.position if b.spawned else None,
                    "size": b.size,
                    "distance": distance(b.position) if b.spawned else None,
                    "heading": b.heading,
                    "spawned": b.spawned,
                    "alive": b.alive,
                    "grouped": b.spawn_id in w.active_group,
                }
                for b in w.bot_roster.all_bots()
            ]
            mobs = sorted((mob_row(m) for m in w.mobs.values()), key=lambda m: m["distance"])
            # Light inventory projection avoids serializing full item definitions
            # and repeated bag children every 200 ms. Clicks use /item/{id}.
            slots = [
                {
                    "address": json_value(a),
                    "client_slot": a.client_slot,
                    "item": {
                        "item_id": i.item_id,
                        "name": i.name,
                        "stack": i.stack,
                        "charges": i.charges,
                        "attuned": i.attuned,
                        "bag_slots": i.bag_slots,
                    },
                }
                for a, i in w.inventory.items()
            ]
            # These are item contributions, not the server's computed AC/ATK.
            gear_fields = (
                "ac",
                "attack",
                "haste",
                "resist_magic",
                "resist_fire",
                "resist_cold",
                "resist_poison",
                "resist_disease",
                "resist_corruption",
            )
            gear = {k: 0 for k in gear_fields}
            for address, item in w.inventory.items():
                if (
                    address.type == 0
                    and 0 <= address.main_slot < len(_WORN)
                    and address.sub_index == -1
                ):
                    for key in gear_fields:
                        gear[key] += getattr(item, key, 0)
            path = move.path
            water = w.get_water_map(w.zone or "") if w.water_match_required_for_los else None
            return w.mesh, water, json_value(
                {
                    "ready": loop.commands.ready.is_set(),
                    "tick": loop.tick,
                    "sent": loop.sent_count,
                    "received": loop.recv_count,
                    "zone": w.zone,
                    "zone_id": w.zone_id,
                    "instance": c.zone_instance,
                    "party_mode": w.party_mode,
                    "self_id": w.self_id,
                    "position": pos,
                    "heading": move.heading,
                    "safe": w.safe,
                    "water": w.at_water,
                    "character": {
                        **{
                            k: getattr(c, k)
                            for k in (
                                "name",
                                "level",
                                "race",
                                "size",
                                "class_id",
                                "hp",
                                "max_hp",
                                "hp_percent",
                                "mana",
                                "max_mana",
                                "endurance",
                                "max_endurance",
                                "strength",
                                "stamina",
                                "agility",
                                "dexterity",
                                "wisdom",
                                "intelligence",
                                "charisma",
                                "exp",
                                "aa_points",
                                "aa_points_spent",
                                "food",
                                "water",
                                "buffs",
                                "buff_icons",
                                "loaded",
                            )
                        },
                        "coin": c.coin,
                        "class_name": CLASS_ID_TO_NAME.get(c.class_id, str(c.class_id)),
                        "race_name": RACE_ID_TO_NAME.get(c.race, str(c.race)),
                    },
                    "inventory": {
                        "loaded": w.inventory.loaded,
                        "slots": slots,
                        "gear": gear,
                        "worn": list(_WORN),
                    },
                    "tasks": [
                        {
                            "task": task,
                            "activities": sorted(
                                w.tasks.activities.get(task.task_id, {}).values(),
                                key=lambda activity: activity.activity_id,
                            ),
                        }
                        for task in w.tasks.sequenced_tasks()
                    ],
                    "bots": bots,
                    "mobs": mobs,
                    "doors": [
                        {
                            "id": d.id,
                            "name": d.name,
                            "position": d.position,
                            "opened": d.opened,
                            "open_type": d.open_type,
                            "kind": (
                                "door" if d.id in exit_doors else d.classify(weapon_models).value
                            ),
                            "is_exit": d.id in exit_doors,
                            "exit_destinations": exit_doors.get(d.id, []),
                            "model_key": d.model_key,
                            "heading": d.heading,
                            "incline": d.incline,
                            "size": d.size,
                            "invert_state": d.invert_state,
                            "door_param": d.door_param,
                        }
                        for d in w.doors.values()
                    ],
                    "ground_spawns": [
                        {
                            "drop_id": g.instance_id,
                            "item_id": g.item_id,
                            "name": (
                                item.name
                                if (item := w.item_book.get(g.item_id))
                                else f"Item #{g.item_id}"
                            ),
                            "position": (g.observed_x, g.observed_y, g.observed_z),
                        }
                        for spawns in w.ground_spawns.values()
                        for g in spawns
                    ],
                    "path": (
                        None
                        if path is None
                        else {
                            k: getattr(path, k)
                            for k in (
                                "points",
                                "origin",
                                "destination",
                                "next_point",
                                "distance",
                                "mode",
                                "fallback",
                                "in_water",
                                "find_waypoints",
                            )
                        }
                    ),
                    "movement": {
                        "asked": move.asked,
                        "committed": move.committed,
                        "refused": move.refused,
                    },
                    "actions": {
                        "active": loop.active.insert if loop.active else None,
                        "queue": [action_snapshot(a) for a in loop.queue],
                        "runs": [r.snapshot() for r in list(loop.action_runs.values())[-100:]],
                    },
                }
            )

        source, water, data = with_loop(collect)
        return annotate_los(data, source, water)

    @app.get("/dashboard/action/{module}/{class_name}")
    def describe_action(module: str, class_name: str):
        """Supply actual constructor schemas to the UI, including dataclasses."""
        loaded = action_modules.load(module)
        cls = loaded.classes().get(class_name)
        if cls is None:
            raise HTTPException(404, f"Unknown action class: {class_name}")
        signature = inspect.signature(cls)
        try:
            hints = get_type_hints(cls.__init__)
        except Exception:
            hints = {}
        parameters = []
        for name, param in signature.parameters.items():
            if name in ("world", "loop"):
                continue
            annotation = hints.get(name, param.annotation)
            schema: dict[str, Any] = {}
            if annotation is Mob:
                schema = {"type": "integer", "x-eq-spawn": True}
            elif annotation is not inspect.Parameter.empty:
                try:
                    schema = TypeAdapter(annotation).json_schema()
                except Exception:
                    pass  # Unsupported annotations retain the explicit JSON editor.
            required = param.default is inspect.Parameter.empty
            parameters.append(
                {
                    "name": name,
                    "required": required,
                    "schema": schema,
                    "annotation": str(annotation),
                    **({} if required else {"default": json_value(param.default)}),
                }
            )
        return {
            "parameters": parameters,
            "compatible": {"world", "loop"} <= signature.parameters.keys(),
            "signature": str(signature),
        }

    @app.get("/dashboard/items")
    def items(q: str = Query(min_length=1, max_length=100), limit: int = Query(50, ge=1, le=100)):
        def search(loop):
            book = loop.world.item_book
            if q.isdecimal():
                item = book.get(int(q))
                return [item_snapshot(item)] if item else []
            term = q.casefold()
            found = []
            for item in book.by_id.values():
                if term in item.name.casefold():
                    found.append(
                        {"item_id": item.item_id, "name": item.name, "bag_slots": item.bag_slots}
                    )
                    if len(found) >= limit:
                        break
            return found

        return with_loop(search)

    def packet_clause(stream: str, direction: str, include: list[str], exclude: list[str]):
        ops = sorted(COMBAT)
        clause = "Character = ? AND Op_Code " + ("IN" if stream == "combat" else "NOT IN")
        clause += " (" + ",".join("?" for _ in ops) + ")"
        args: list[str | int] = [character, *ops]
        if direction != "all":
            clause += " AND Direction = ?"
            args.append(direction)
        # Exact opcodes and terminal-* prefixes, case-insensitive. Bind every
        # value; underscores in opcode names are literal, not LIKE wildcards.
        for terms, negate in ((include, False), (exclude, True)):
            keys = sorted({term.strip().lower() for term in terms if term.strip()})
            exact = [key for key in keys if not key.endswith("*")]
            predicates = []
            if exact:
                predicates.append("lower(Op_Code) IN (" + ",".join("?" for _ in exact) + ")")
                args.extend(exact)
            for key in keys:
                if key.endswith("*"):
                    prefix = key[:-1]
                    predicates.append("substr(lower(Op_Code), 1, ?) = ?")
                    args.extend((len(prefix), prefix))
            if predicates:
                clause += " AND " + ("NOT " if negate else "") + "(" + " OR ".join(predicates) + ")"
        return clause, args

    def packet_row(r, stream: str, *, decode_all: bool = False) -> dict:
        raw = bytes(r["Bytes"])
        payload = None
        # High-volume movement packets need only metadata in the live view.
        if (
            decode_all
            or stream == "combat"
            or r["Op_Code"]
            in {
                "OP_ChannelMessage",
                "OP_SpecialMesg",
                "OP_SimpleMessage",
            }
        ):
            try:
                parsed = decode_packet(r["Op_Code"], raw)
                payload = json_value(parsed) if parsed is not None else None
            except Exception:
                pass
        chat_text = None
        if r["Op_Code"] == "OP_SimpleMessage" and isinstance(payload, dict):
            import re

            from eqclient4.data.strings import EQ_STRS

            string_id = payload.get("string_id") or 0
            args = payload.get("texts") or []
            template = EQ_STRS.get(string_id)
            if template is None:
                chat_text = f"[String #{string_id}]" + (" " + " ".join(args) if args else "")
            else:
                # EQ localized strings use numbered substitutions. Leave missing
                # arguments visible rather than silently dropping them.
                chat_text = re.sub(
                    r"%([1-9][0-9]*)",
                    lambda m: args[int(m[1]) - 1] if int(m[1]) <= len(args) else m[0],
                    template,
                )
        return {
            "id": r["id"],
            "timestamp": r["TimeSeen"],
            "opcode": r["Op_Code"],
            "direction": r["Direction"],
            "size": len(raw),
            "payload": payload,
            "chat_text": chat_text,
        }

    @app.get("/dashboard/packets/cursor")
    def packet_cursor():
        # A shared high-water mark for both streams, captured at page startup.
        # Filter changes replay from this mark, not from the latest tail.
        high = query("SELECT COALESCE(MAX(rowid), 0) AS high FROM packets", [])[0]["high"]
        return {"cursor": high}

    @app.get("/dashboard/packets")
    def packets(
        after: int = Query(-1, ge=-1),
        limit: int = Query(250, ge=1, le=1000),
        stream: str = Query("wire", pattern="^(wire|combat)$"),
        direction: str = Query("all", pattern="^(all|recv|send)$"),
        include: list[str] = Query(default=[]),
        exclude: list[str] = Query(default=[]),
    ):
        # Filter before LIMIT so excluded floods never consume the live buffer.
        clause, args = packet_clause(stream, direction, include, exclude)
        high = query("SELECT COALESCE(MAX(rowid), 0) AS high FROM packets", [])[0]["high"]
        reset = after > high
        if reset:
            # The capture was truncated/replaced. Start the new capture at 0.
            after = 0
        if after == -1:
            rows = query(
                "SELECT rowid AS id, TimeSeen, Op_Code, Direction, Bytes FROM packets WHERE "
                + clause
                + " AND rowid <= ? ORDER BY rowid DESC LIMIT ?",
                [*args, high, limit],
            )
            rows = list(reversed(rows))
            cursor = high
        else:
            rows = query(
                "SELECT rowid AS id, TimeSeen, Op_Code, Direction, Bytes FROM packets WHERE "
                + clause
                + " AND rowid > ? AND rowid <= ? ORDER BY rowid LIMIT ?",
                [*args, after, high, limit + 1],
            )
            cursor = rows[limit - 1]["id"] if len(rows) > limit else high
        return {
            "packets": [packet_row(r, stream) for r in rows[:limit]],
            "next": cursor,
            "has_more": len(rows) > limit,
            "reset": reset,
        }

    @app.get("/dashboard/packets/history")
    def packet_history(
        before: int | None = Query(None, ge=1),
        limit: int = Query(250, ge=1, le=1000),
        stream: str = Query("wire", pattern="^(wire|combat)$"),
        direction: str = Query("all", pattern="^(all|recv|send)$"),
        include: list[str] = Query(default=[]),
        exclude: list[str] = Query(default=[]),
        q: str = Query("", max_length=4096),
    ):
        # Historical pages use an exclusive rowid cursor, never the live cursor.
        # Decode/search bounded batches, advancing past *scanned* rows even
        # when none match. A sparse search can continue with Load older.
        import json

        clause, args = packet_clause(stream, direction, include, exclude)
        high = query("SELECT COALESCE(MAX(rowid), 0) AS high FROM packets", [])[0]["high"]
        cursor = min(before, high + 1) if before is not None else high + 1
        needle = q.strip().lower()
        scan_limit = max(limit, 2000) if needle else limit
        rows = query(
            "SELECT rowid AS id, TimeSeen, Op_Code, Direction, Bytes FROM packets WHERE "
            + clause
            + " AND rowid < ? ORDER BY rowid DESC LIMIT ?",
            [*args, cursor, scan_limit + 1],
        )
        result = []
        scanned = 0
        for r in rows[:scan_limit]:
            cursor = r["id"]
            scanned += 1
            packet = packet_row(r, stream, decode_all=bool(needle))
            if needle:
                haystack = (
                    str(packet["opcode"])
                    + " "
                    + json.dumps(packet["payload"], ensure_ascii=False, default=str)
                )
                if needle not in haystack.lower():
                    continue
            result.append(packet)
            if len(result) == limit:
                break
        return {
            "packets": list(reversed(result)),
            "next_before": cursor,
            "has_more": scanned < len(rows),
            "scanned": scanned,
        }

    @app.get("/dashboard/packet/{packet_id}")
    def packet(packet_id: int):
        rows = query(
            "SELECT rowid AS id, TimeSeen, Op_Code, Direction, Bytes FROM packets "
            "WHERE Character = ? AND rowid = ?",
            [character, packet_id],
        )
        if not rows:
            raise HTTPException(404, "Unknown packet")
        r = rows[0]
        raw = bytes(r["Bytes"])
        try:
            parsed = decode_packet(r["Op_Code"], raw)
            payload = json_value(parsed) if parsed is not None else None
        except Exception:
            payload = None
        return {
            "id": packet_id,
            "timestamp": r["TimeSeen"],
            "opcode": r["Op_Code"],
            "direction": r["Direction"],
            "size": len(raw),
            "payload": payload,
            "payload_hex": raw.hex(),
        }
