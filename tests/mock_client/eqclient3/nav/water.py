"""Zone water maps (`maps/water/<zone>.wtr`). Used to swim instead of walking the shore."""

from __future__ import annotations

import math
import struct
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from eqclient3.nav.navmesh import maps_root

# Matches zone/water_map.h WaterRegionType.
REGION_NORMAL = 0
REGION_WATER = 1
REGION_LAVA = 2
REGION_ZONE_LINE = 3
REGION_PVP = 4
REGION_SLIME = 5
REGION_ICE = 6
REGION_VWATER = 7

_LIQUID = {REGION_WATER, REGION_LAVA, REGION_VWATER, REGION_SLIME}


@dataclass
class _BspNode:
    normal: tuple[float, float, float]
    split: float
    special: int
    left: int
    right: int


@dataclass
class _ObbRegion:
    kind: int
    # Transformed AABB in box space after inverse transform of EQ (y,x,z) point.
    min_x: float
    max_x: float
    min_y: float
    max_y: float
    min_z: float
    max_z: float
    inv: tuple[tuple[float, float, float, float], ...]  # 4x4 row-major


@dataclass
class WaterMap:
    zone: str
    version: int
    nodes: list[_BspNode] = field(default_factory=list)
    regions: list[_ObbRegion] = field(default_factory=list)
    _surface: dict[tuple[int, int], float | None] = field(default_factory=dict)
    # Cached zoneline sample clouds keyed by rounded anchor + reach/step.
    _zoneline_samples: dict[tuple[int, int, int, int], list[tuple[float, float, float]]] = field(
        default_factory=dict
    )

    def region(self, x: float, y: float, z: float) -> int:
        """Region type at EQ (x, y, z). Internally maps query as (y, x, z) like the zone server."""
        if self.version == 1 and self.nodes:
            return self._bsp(1, y, x, z)
        if self.version == 2 and self.regions:
            return self._obb(y, x, z)
        return REGION_NORMAL

    def in_zone_line(self, x: float, y: float, z: float) -> bool:
        return self.region(x, y, z) == REGION_ZONE_LINE

    def nearest_zone_line(
        self,
        x: float,
        y: float,
        z: float,
        *,
        anchor: tuple[float, float, float] | None = None,
        reach: float = 250.0,
        step: float = 15.0,
        near: float = 100.0,
    ) -> tuple[float, float, float] | None:
        """Closest watermap zoneline sample to (x, y) for this outdoor exit.

        `anchor` is the zone_points row (one point on the painted line). The server
        accepts OP_ZoneChange when GetPosition() is InZoneLine (watermap region 3)
        and the closest zone_points row targets that zone — so samples must stay
        on the real line near that exit, not drift hundreds of yards along a long strip.
        """
        ax, ay, az = anchor if anchor is not None else (x, y, z)
        key = (int(ax) // 20, int(ay) // 20, int(reach), int(step))
        samples = self._zoneline_samples.get(key)
        if samples is None:
            samples = []
            r = int(reach)
            s = max(5, int(step))
            # Z matter: freportw line is roughly z∈[-27,19]; mesh often sits at -30 (not in line).
            z_probes = (az, az + 4.0, az + 8.0, az - 4.0, -24.0, -20.0, -16.0, 0.0, z)
            for dx in range(-r, r + 1, s):
                for dy in range(-r, r + 1, s):
                    px, py = ax + dx, ay + dy
                    for zz in z_probes:
                        if self.region(px, py, float(zz)) == REGION_ZONE_LINE:
                            samples.append((float(px), float(py), float(zz)))
                            break
            self._zoneline_samples[key] = samples
        if not samples:
            return None
        # Prefer the band around the zone_points anchor so we don't hike the strip.
        near2 = float(near) * float(near)
        local = [p for p in samples if (p[0] - ax) ** 2 + (p[1] - ay) ** 2 <= near2]
        pool = local or samples
        return min(pool, key=lambda p: (p[0] - x) ** 2 + (p[1] - y) ** 2)

    def in_liquid(self, x: float, y: float, z: float) -> bool:
        return self.region(x, y, z) in _LIQUID

    def can_fish_at(self, x: float, y: float, z: float, rod: float = 30.0, line: float = 100.0) -> bool:
        """True when a cast from (x,y,z) can reach water (server FishingRodLength ~30)."""
        if self.region(x, y, z) == REGION_LAVA:
            return False
        for deg in range(0, 360, 30):
            rad = math.radians(deg)
            rx = x + rod * math.sin(rad)
            ry = y + rod * math.cos(rad)
            for drop in (2.0, 5.0, 10.0, 20.0, 40.0, 60.0, 80.0, line):
                if drop > line:
                    break
                kind = self.region(rx, ry, z - drop)
                if kind == REGION_LAVA:
                    return False
                if kind in {REGION_WATER, REGION_VWATER}:
                    return True
            surf = self.surface_z(rx, ry)
            if surf is not None and 0.0 <= (z - surf) <= line:
                return True
        return False

    def fish_spot(
        self,
        x: float,
        y: float,
        z: float,
        radius: float = 120.0,
        step: float = 10.0,
    ) -> tuple[float, float, float] | None:
        """Nearest shore stand where can_fish_at is true (prefer not standing in liquid)."""
        if self.can_fish_at(x, y, z) and not self.in_liquid(x, y, z):
            return (x, y, z)
        best: tuple[float, float, float] | None = None
        best_d = 1e9
        r = int(radius)
        s = max(4, int(step))
        for dx in range(-r, r + 1, s):
            for dy in range(-r, r + 1, s):
                px, py = x + dx, y + dy
                if self.in_liquid(px, py, z):
                    continue
                if not self.can_fish_at(px, py, z):
                    continue
                dist = math.hypot(dx, dy)
                if dist < best_d:
                    best_d = dist
                    best = (px, py, z)
        if best is not None:
            return best
        # Fall back to a liquid-adjacent column if no dry shore in range.
        if self.can_fish_at(x, y, z):
            return (x, y, z)
        return None

    def fish_aim(self, x: float, y: float, z: float, rod: float = 30.0) -> tuple[float, float, float] | None:
        """A point over water to face while casting, or None when no water in reach."""
        for deg in range(0, 360, 15):
            rad = math.radians(deg)
            rx = x + rod * math.sin(rad)
            ry = y + rod * math.cos(rad)
            for drop in (5.0, 20.0, 40.0, 80.0):
                kind = self.region(rx, ry, z - drop)
                if kind in {REGION_WATER, REGION_VWATER}:
                    return (rx, ry, z - drop)
            surf = self.surface_z(rx, ry)
            if surf is not None:
                return (rx, ry, surf)
        return None

    def surface_z(self, x: float, y: float, lo: float = -1000.0, hi: float = 1000.0) -> float | None:
        """Highest liquid z at (x, y), or None when this column has no water."""
        key = (int(x) // 4, int(y) // 4)
        if key in self._surface:
            return self._surface[key]
        hit: float | None = None
        for z in range(int(hi), int(lo) - 1, -20):
            if self.in_liquid(x, y, float(z)):
                hit = float(z)
                break
        if hit is None:
            for z in range(int(hi), int(lo) - 1, -5):
                if self.in_liquid(x, y, float(z)):
                    hit = float(z)
                    break
        if hit is None:
            self._surface[key] = None
            return None
        # Walk up from a known liquid sample to the surface.
        top = hit
        probe = hit + 5.0
        while probe <= hi and self.in_liquid(x, y, probe):
            top = probe
            probe += 5.0
        low, high = top, min(hi, top + 5.0)
        for _ in range(16):
            mid = (low + high) * 0.5
            if self.in_liquid(x, y, mid):
                low = mid
            else:
                high = mid
        self._surface[key] = low
        return low

    def crosses(self, a: tuple[float, float, float], b: tuple[float, float, float], samples: int = 6) -> bool:
        """True when the straight XY run crosses a water column (shore-to-shore lakes)."""
        if math.hypot(b[0] - a[0], b[1] - a[1]) < 8.0:
            return self.in_liquid(*a) or self.in_liquid(*b)
        water_hits = 0
        for i in range(samples + 1):
            t = i / samples if samples else 0.0
            x = a[0] + (b[0] - a[0]) * t
            y = a[1] + (b[1] - a[1]) * t
            z = a[2] + (b[2] - a[2]) * t
            if self.in_liquid(x, y, z):
                return True
            surf = self.surface_z(x, y)
            if surf is None:
                continue
            # Already at the surface, or the column sits under this XY (lake crossing).
            if surf - 2.0 <= z <= surf + 12.0:
                return True
            if z > surf:
                water_hits += 1
        # Enough of the straight line sits over water — swim instead of skirting the shore.
        return water_hits >= max(2, (samples + 2) // 3)

    def _bsp(self, node_number: int, x: float, y: float, z: float) -> int:
        guard = 0
        while guard < 10000:
            guard += 1
            node = self.nodes[node_number - 1]
            if node.left == 0 and node.right == 0:
                return node.special
            dist = x * node.normal[0] + y * node.normal[1] + z * node.normal[2] + node.split
            if dist > 0.0:
                if node.left == 0:
                    return REGION_NORMAL
                node_number = node.left
            else:
                if node.right == 0:
                    return REGION_NORMAL
                node_number = node.right
        return REGION_NORMAL

    def _obb(self, x: float, y: float, z: float) -> int:
        for region in self.regions:
            bx, by, bz = _transform_point(region.inv, x, y, z)
            if (
                region.min_x <= bx <= region.max_x
                and region.min_y <= by <= region.max_y
                and region.min_z <= bz <= region.max_z
            ):
                return region.kind
        return REGION_NORMAL


_LOADED: dict[str, WaterMap | None] = {}

def load_water(zone: str, root: Path | None = None) -> WaterMap | None:
    key = (zone or "").lower()
    if root is None and key in _LOADED:
        return _LOADED[key]
    water = _read_water(key, root)
    if root is None:
        _LOADED[key] = water
    return water

def _read_water(zone: str, root: Path | None) -> WaterMap | None:
    base = root or maps_root()
    if base is None or not zone:
        return None
    path = base / "water" / f"{zone}.wtr"
    if not path.is_file():
        return None
    data = path.read_bytes()
    if len(data) < 14 or data[:10] != b"EQEMUWATER":
        return None
    version = struct.unpack_from("<I", data, 10)[0]
    if version == 1:
        return _load_v1(zone.lower(), data)
    if version == 2:
        return _load_v2(zone.lower(), data)
    return None


def _load_v1(zone: str, data: bytes) -> WaterMap | None:
    count = struct.unpack_from("<I", data, 14)[0]
    need = 18 + count * 36
    if len(data) < need or count <= 0:
        return None
    nodes: list[_BspNode] = []
    off = 18
    for _ in range(count):
        _nn, nx, ny, nz, split, _region, special, left, right = struct.unpack_from("<i4f4i", data, off)
        nodes.append(_BspNode((nx, ny, nz), split, special, left, right))
        off += 36
    return WaterMap(zone=zone, version=1, nodes=nodes)


def _load_v2(zone: str, data: bytes) -> WaterMap | None:
    count = struct.unpack_from("<I", data, 14)[0]
    off = 18
    regions: list[_ObbRegion] = []
    for _ in range(count):
        if off + 52 > len(data):
            return None
        kind = struct.unpack_from("<I", data, off)[0]
        off += 4
        x, y, z, x_rot, y_rot, z_rot, x_scale, y_scale, z_scale, x_ext, y_ext, z_ext = struct.unpack_from(
            "<12f", data, off
        )
        off += 48
        min_x, max_x = sorted((-x_ext, x_ext))
        min_y, max_y = sorted((-y_ext, y_ext))
        min_z, max_z = sorted((-z_ext, z_ext))
        matrix = _obb_matrix(x, y, z, x_rot, y_rot, z_rot, x_scale, y_scale, z_scale)
        inv = _invert4(matrix)
        if inv is None:
            continue
        regions.append(_ObbRegion(kind, min_x, max_x, min_y, max_y, min_z, max_z, inv))
    return WaterMap(zone=zone, version=2, regions=regions)


def _obb_matrix(
    tx: float,
    ty: float,
    tz: float,
    rx: float,
    ry: float,
    rz: float,
    sx: float,
    sy: float,
    sz: float,
) -> tuple[tuple[float, float, float, float], ...]:
    """4x4 matching zone/oriented_bounding_box.cpp: translate * scale * (rot_z * rot_y * rot_x)."""
    ax, ay, az = math.radians(rx), math.radians(ry), math.radians(rz)
    cx, sax = math.cos(ax), math.sin(ax)
    cy, say = math.cos(ay), math.sin(ay)
    cz, saz = math.cos(az), math.sin(az)
    # rot_z * rot_y * rot_x
    r00 = cz * cy
    r01 = cz * say * sax - saz * cx
    r02 = cz * say * cx + saz * sax
    r10 = saz * cy
    r11 = saz * say * sax + cz * cx
    r12 = saz * say * cx - cz * sax
    r20 = -say
    r21 = cy * sax
    r22 = cy * cx
    # scale * rotate, then translation in last column
    return (
        (r00 * sx, r01 * sx, r02 * sx, tx),
        (r10 * sy, r11 * sy, r12 * sy, ty),
        (r20 * sz, r21 * sz, r22 * sz, tz),
        (0.0, 0.0, 0.0, 1.0),
    )


def _invert4(m: tuple[tuple[float, float, float, float], ...]) -> tuple[tuple[float, float, float, float], ...] | None:
    """Invert a 4x4 affine matrix. None when singular."""
    a = [list(row) for row in m]
    inv = [[1.0 if i == j else 0.0 for j in range(4)] for i in range(4)]
    for col in range(4):
        pivot = max(range(col, 4), key=lambda r: abs(a[r][col]))
        if abs(a[pivot][col]) < 1e-12:
            return None
        a[col], a[pivot] = a[pivot], a[col]
        inv[col], inv[pivot] = inv[pivot], inv[col]
        div = a[col][col]
        a[col] = [v / div for v in a[col]]
        inv[col] = [v / div for v in inv[col]]
        for row in range(4):
            if row == col:
                continue
            factor = a[row][col]
            a[row] = [a[row][c] - factor * a[col][c] for c in range(4)]
            inv[row] = [inv[row][c] - factor * inv[col][c] for c in range(4)]
    return tuple(tuple(row) for row in inv)


def _transform_point(
    inv: tuple[tuple[float, float, float, float], ...], x: float, y: float, z: float
) -> tuple[float, float, float]:
    return (
        inv[0][0] * x + inv[0][1] * y + inv[0][2] * z + inv[0][3],
        inv[1][0] * x + inv[1][1] * y + inv[1][2] * z + inv[1][3],
        inv[2][0] * x + inv[2][1] * y + inv[2][2] * z + inv[2][3],
    )


def water_map(state: object) -> Any:
    """The zone water map, or a map the test already placed on the tick."""
    forced = state.water
    if forced is not None:
        return forced
    zone = state.world.zone
    if state.water_zone == zone:
        return state.water_map
    state.water_zone = zone
    try:
        state.water_map = load_water(zone) if zone else None
    except (OSError, ValueError):
        state.water_map = None
    return state.water_map


def float_step(state: object, step: tuple[float, float, float]) -> tuple[float, float, float]:
    """Lift a ground step onto the surface when that column is liquid."""
    water = water_map(state)
    if water is None or not water.in_liquid(step[0], step[1], step[2]):
        return step
    surface = water.surface_z(step[0], step[1])
    if surface is None:
        return step
    return (step[0], step[1], swim_height(state.world.z, surface - 1.0))


def swim_height(here_z: float, target_z: float, max_dz: float = 4.0) -> float:
    """Move vertically toward the swim target without leaping."""
    gap = target_z - here_z
    if abs(gap) <= max_dz:
        return target_z
    return here_z + (max_dz if gap > 0 else -max_dz)
