"""Static, read-only zone geometry for the dashboard's WebGL viewer.

Coordinates are EQ (x, y, z), with Z up. No live world/agent lock is needed.
The wire format is little-endian EQG1 + three uint32s (collision vertex count,
nav vertex count, availability flags), or EQG2 with a water vertex count before
the flags. Both are followed by packed float32 XYZ vertices.
Each consecutive group of three vertices is a triangle.
"""

from __future__ import annotations

import re
import struct
import sys
import zlib
from array import array
from functools import lru_cache

from eqclient4.nav.maps import _read_map
from eqclient4.nav.navmesh import load_nav, maps_root
from eqclient4.nav.water import load_water
from eqclient4.scripts.debug_water import water_vertices
from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import Response


@lru_cache(maxsize=2)
def geometry_bytes(zone: str, format: int = 1) -> bytes:
    # The visualizer uses its own parsed snapshots; do not mutate live nav
    # state, visited sets, or the agent's line-of-sight cache.
    root = maps_root()
    if root is None:
        raise FileNotFoundError("Set EQEMU_MAPS to the eqmaps checkout")

    collision = array("f")
    nav = array("f")
    flags = 0
    base_path = root / "base" / f"{zone}.map"
    nav_path = root / "nav" / f"{zone}.nav"
    if base_path.is_file():
        geometry = _read_map(zone)
        if geometry is not None:
            for triangle in geometry.triangles:
                for point in triangle:
                    collision.extend(point)
            flags |= 1
    if nav_path.is_file():
        mesh = load_nav(zone, root=root)
        if mesh is not None:
            for poly in mesh.polys:
                # Detour polygons are convex and already converted to EQ XYZ.
                for index in range(1, len(poly.verts) - 1):
                    for point in (poly.verts[0], poly.verts[index], poly.verts[index + 1]):
                        nav.extend(point)
            flags |= 2
    water = load_water(zone, root=root) if format == 2 else None
    bounds = None
    if water is not None and water.version == 1 and (collision or nav):
        axes = [collision[i::3] + nav[i::3] for i in range(3)]
        bounds = (tuple(min(a) - 1 for a in axes), tuple(max(a) + 1 for a in axes))
    liquid = water_vertices(water, bounds)
    if water is not None:
        flags |= 4
    if not flags:
        raise FileNotFoundError(f"No supported geometry for {zone}")
    if sys.byteorder != "little":
        collision.byteswap()
        nav.byteswap()
        liquid.byteswap()
    if format == 1:
        return (
            struct.pack("<4sIII", b"EQG1", len(collision) // 3, len(nav) // 3, flags)
            + collision.tobytes()
            + nav.tobytes()
        )
    return (
        struct.pack("<4sIIII", b"EQG2", len(collision) // 3, len(nav) // 3, len(liquid) // 3, flags)
        + collision.tobytes()
        + nav.tobytes()
        + liquid.tobytes()
    )


def install_geometry(app: FastAPI) -> None:
    @app.get("/dashboard/geometry/{zone}", response_class=Response)
    def geometry(zone: str, format: int = Query(1, ge=1, le=2)) -> Response:
        if not re.fullmatch(r"[a-zA-Z0-9_]{1,80}", zone):
            raise HTTPException(400, "Invalid zone short name")
        try:
            data = geometry_bytes(zone.lower(), format)
        except FileNotFoundError as exc:
            raise HTTPException(404, str(exc)) from exc
        except (OSError, ValueError, struct.error, zlib.error) as exc:
            raise HTTPException(422, f"Cannot read {zone} geometry: {exc}") from exc
        return Response(
            content=data,
            media_type="application/octet-stream",
            headers={"Cache-Control": "private, max-age=3600"},
        )
