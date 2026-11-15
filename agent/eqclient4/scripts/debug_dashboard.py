"""Read-only dashboard projections; mutations use the existing debug API."""

from __future__ import annotations

import inspect
import math
from pathlib import Path
from typing import Any, get_type_hints

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

    @app.get("/", include_in_schema=False)
    @app.get("/dashboard", include_in_schema=False)
    def dashboard():
        return FileResponse(root / "index.html")

    @app.get("/dashboard/state")
    def state():
        def collect(loop):
            w = loop.world
            c = w.character
            pos = w.position
            move = w.movement

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
            return json_value(
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
                    "bots": bots,
                    "mobs": mobs,
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

        return with_loop(collect)

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

    @app.get("/dashboard/packets")
    def packets(
        after: int = Query(-1, ge=-1),
        limit: int = Query(250, ge=1, le=1000),
        stream: str = Query("wire", pattern="^(wire|combat)$"),
    ):
        # Separate cursors let combat remain responsive during packet floods.
        # Initial request tails the capture rather than replaying login history.
        ops = sorted(COMBAT)
        clause = "Character = ? AND Op_Code " + ("IN" if stream == "combat" else "NOT IN")
        clause += " (" + ",".join("?" for _ in ops) + ")"
        args = [character, *ops]
        # Snapshot the high-water mark first. If a sparse stream has no new
        # matching rows, advance to this mark instead of rescanning history.
        # The upper bound prevents races with new commits between queries.
        high = query("SELECT COALESCE(MAX(rowid), 0) AS high FROM packets", [])[0]["high"]
        if after > high:  # capture was replaced/truncated
            after = -1
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
        result = []
        for r in rows[:limit]:
            raw = bytes(r["Bytes"])
            payload = None
            # High-volume movement packets need only metadata until inspected.
            if stream == "combat" or r["Op_Code"] in {
                "OP_ChannelMessage",
                "OP_SpecialMesg",
                "OP_SimpleMessage",
            }:
                try:
                    parsed = decode_packet(r["Op_Code"], raw)
                    payload = json_value(parsed) if parsed is not None else None
                except Exception:
                    pass
            result.append(
                {
                    "id": r["id"],
                    "timestamp": r["TimeSeen"],
                    "opcode": r["Op_Code"],
                    "direction": r["Direction"],
                    "size": len(raw),
                    "payload": payload,
                }
            )
        return {"packets": result, "next": cursor, "has_more": len(rows) > limit}

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
