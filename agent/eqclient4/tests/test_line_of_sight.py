"""Collision parity with the zone server's CheckLosFN / LoadV2."""

import struct
import tempfile
import unittest
import zlib
from pathlib import Path
from unittest.mock import patch

from eqclient4.nav.maps import ZoneMap, _cells_crossed, _read_map, _triangles
from eqclient4.nav.water import (
    REGION_LAVA,
    REGION_NORMAL,
    REGION_SLIME,
    REGION_VWATER,
    REGION_WATER,
    WaterMap,
)
from eqclient4.structs.mobs import Spawn


def wall(
    x: float, ymin: float = -0.25, ymax: float = 0.25, zmin: float = -10.0, zmax: float = 10.0
) -> ZoneMap:
    a, b = (x, ymin, zmin), (x, ymax, zmin)
    c, d = (x, ymax, zmax), (x, ymin, zmax)
    return ZoneMap([(a, b, c), (a, c, d)])


class LineOfSightTest(unittest.TestCase):
    def test_no_corner_peeks_or_coarse_cache(self) -> None:
        mesh = wall(5)
        self.assertTrue(mesh.clear((0, 1, 0), (10, 1, 0)))
        self.assertFalse(mesh.clear((0, 0, 0), (10, 0, 0)))
        self.assertTrue(mesh.clear((0, 1, 0), (10, 1, 0)))

    def test_near_endpoint_collisions(self) -> None:
        for x in (0.5, 99.5):
            with self.subTest(x=x):
                mesh = wall(x)
                self.assertFalse(mesh.clear((0, 0, 0), (100, 0, 0)))
                self.assertFalse(mesh.clear((100, 0, 0), (0, 0, 0)))
        self.assertTrue(wall(101).clear((0, 0, 0), (100, 0, 0)))

    def test_actual_sizes(self) -> None:
        mesh = wall(5, zmin=1.8, zmax=2.4)
        self.assertFalse(mesh.clear((0, 0, 0), (10, 0, 0)))
        self.assertTrue(mesh.clear((0, 0, 0), (10, 0, 0), 6, 18))
        self.assertTrue(mesh.clear((0, 0, 0), (10, 0, 0), 2, 6))
        self.assertFalse(mesh.clear((0, 0, 0), (10, 0, 0), 0, 0))

    def test_grid_corner_and_endpoint(self) -> None:
        cells = _cells_crossed((31, 33, 0), (33, 31, 0))
        self.assertIn((1, 1), cells)
        self.assertIn((0, 0), cells)
        self.assertEqual(_cells_crossed((33, 31, 0), (32, 32, 0))[-1], (1, 1))

    def test_v2_models_placements_groups_and_terrain(self) -> None:
        # One collidable base triangle and one non-collidable triangle.
        base = struct.pack("<9f3I", 0, 0, -20, 1, 0, -20, 0, 1, -20, 0, 1, 2)
        noncollidable = struct.pack("<9f3I", 0, 0, 20, 1, 0, 20, 0, 1, 20, 0, 1, 2)
        model = b"wall\0" + struct.pack("<II9f", 3, 2, 0, 0, -5, 0, 2, -5, 0, 0, 5)
        model += struct.pack("<IIIBIIIB", 0, 1, 2, 1, 0, 2, 1, 0)
        placement = b"wall\0" + struct.pack("<9f", 2, 5, 0, 0, 0, 0, 1, 1, 1)
        group = struct.pack("<12fI", 100, 200, 300, 90, 0, 90, 2, 3, 4, 10, 20, 30, 1)
        group += b"wall\0" + struct.pack("<9f", 2, 3, 4, 0, 0, 0, 1, 1, 1)
        flat = struct.pack("<Bfff", 1, 1000, 1000, 10)
        terrain = struct.pack("<Bff4B9f", 0, 2000, 2000, 0, 1, 0, 0, *range(9))
        data = struct.pack("<9If", 3, 3, 3, 3, 1, 1, 1, 2, 2, 3)
        data += base + noncollidable + model + placement + group + flat + terrain
        triangles = _triangles(data)
        self.assertEqual(len(triangles), 11)  # 1 base + 2 model + 2 flat + 6 terrain
        self.assertEqual(triangles[1], ((5, 2, -5), (7, 2, -5), (5, 2, 5)))
        for got, expected in zip(triangles[2][0], (226, 108, 342)):
            self.assertAlmostEqual(got, expected, places=3)
        mesh = ZoneMap(triangles)
        self.assertFalse(mesh.clear((5.5, 0, 0), (5.5, 4, 0)))
        self.assertEqual(mesh.ground((1002, 1002, 10)), 10)
        self.assertIsNone(mesh.ground((2001, 2004, 0)))  # omitted terrain quad
        self.assertIsNotNone(mesh.ground((2001, 2001, 0)))
        # Exercise the actual compressed file header as well.
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "base").mkdir()
            compressed = zlib.compress(data)
            (root / "base" / "test.map").write_bytes(
                struct.pack("<III", 0x02000000, len(compressed), len(data)) + compressed
            )
            with patch("eqclient4.nav.maps.maps_root", return_value=root):
                loaded = _read_map("test")
                self.assertIsNotNone(loaded)
                assert loaded is not None
                self.assertEqual(loaded.triangles, triangles)

    def test_v1_faces(self) -> None:
        data = struct.pack(
            "<IIHI13f", 0x01000000, 1, 0, 0, 5, -10, -10, 5, 10, -10, 5, 0, 10, 0, 0, 0, 0
        )
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "base").mkdir()
            (root / "base" / "test.map").write_bytes(data)
            with patch("eqclient4.nav.maps.maps_root", return_value=root):
                mesh = _read_map("test")
                self.assertIsNotNone(mesh)
                assert mesh is not None
                self.assertFalse(mesh.clear((0, 0, 0), (10, 0, 0)))

    def test_water_rule_matches_map_version(self) -> None:
        class Regions(WaterMap):
            def region(self, x: float, y: float, z: float) -> int:
                return int(x)

        dry = (REGION_NORMAL, 0, 0)
        for version in (1, 2):
            water = Regions("test", version)
            self.assertFalse(water.los_clear(dry, (REGION_WATER, 0, 0)))
            self.assertTrue(water.los_clear((REGION_WATER, 0, 0), (REGION_LAVA, 0, 0)))
            self.assertEqual(water.los_clear(dry, (REGION_VWATER, 0, 0)), version == 1)
            self.assertTrue(water.los_clear(dry, (REGION_SLIME, 0, 0)))

    def test_spawn_preserves_size(self) -> None:
        spawn = Spawn(42, "a_cavern_spider000", 1, 10, 1, 1, 2, 3, 1, 36, size=12.5)
        self.assertAlmostEqual(Spawn.deserialize(spawn.serialize()).size, 12.5)


if __name__ == "__main__":
    unittest.main()
