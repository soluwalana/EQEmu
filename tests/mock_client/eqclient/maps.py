"""Line of sight against maps/base/<zone>.map. A missing file means the shot is clear."""

from __future__ import annotations

import struct
import zlib
from dataclasses import dataclass

from eqclient.navmesh import maps_root

_EYE = 2.7  # (default size 6 / 2) * 0.9, where this character looks from
_SEE = 1.5  # (default size 6 / 2) * 0.5, where the other character is seen


@dataclass
class ZoneMap:
    triangles: list[tuple[tuple[float, float, float], tuple[float, float, float], tuple[float, float, float]]]

    def clear(self, start: tuple[float, float, float], end: tuple[float, float, float]) -> bool:
        """True when no collidable triangle sits between the two eye points."""
        origin = (start[0], start[1], start[2] + _EYE)
        target = (end[0], end[1], end[2] + _SEE)
        for triangle in self.triangles:
            if _hits(origin, target, triangle):
                return False
        return True


def load_map(zone: str) -> ZoneMap | None:
    root = maps_root()
    if root is None or not zone:
        return None
    path = root / "base" / f"{zone.lower()}.map"
    if not path.is_file():
        return None
    data = path.read_bytes()
    if len(data) < 16:
        return None
    version = struct.unpack_from("<I", data)[0]
    if version != 0x02000000:
        return None
    data_size, _buffer_size = struct.unpack_from("<II", data, 4)
    inflated = zlib.decompress(data[12 : 12 + data_size])
    if len(inflated) < 40:
        return None
    return ZoneMap(_triangles(inflated))


def _triangles(buf: bytes):
    counts = struct.unpack_from("<9I", buf)
    vert_count, ind_count = counts[0], counts[1]
    offset = 36 + 4  # nine uint32 counts and the units-per-vertex float
    verts = []
    for _ in range(vert_count):
        verts.append(struct.unpack_from("<fff", buf, offset))
        offset += 12
    indices = []
    for _ in range(ind_count):
        indices.append(struct.unpack_from("<I", buf, offset)[0])
        offset += 4
    triangles = []
    for index in range(0, len(indices) - 2, 3):
        a, b, c = indices[index], indices[index + 1], indices[index + 2]
        if a >= len(verts) or b >= len(verts) or c >= len(verts):
            continue
        triangles.append((verts[a], verts[b], verts[c]))
    return triangles


def _hits(start, end, triangle) -> bool:
    """Möller–Trumbore. A hit between the eyes blocks the shot."""
    (ax, ay, az), (bx, by, bz), (cx, cy, cz) = triangle
    edge1 = (bx - ax, by - ay, bz - az)
    edge2 = (cx - ax, cy - ay, cz - az)
    direction = (end[0] - start[0], end[1] - start[1], end[2] - start[2])
    p = _cross(direction, edge2)
    det = _dot(edge1, p)
    if abs(det) < 1e-8:
        return False
    inverse = 1.0 / det
    tvec = (start[0] - ax, start[1] - ay, start[2] - az)
    u = _dot(tvec, p) * inverse
    if u < 0.0 or u > 1.0:
        return False
    q = _cross(tvec, edge1)
    v = _dot(direction, q) * inverse
    if v < 0.0 or u + v > 1.0:
        return False
    t = _dot(edge2, q) * inverse
    return 0.02 < t < 0.98


def _dot(a, b) -> float:
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def _cross(a, b):
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )
