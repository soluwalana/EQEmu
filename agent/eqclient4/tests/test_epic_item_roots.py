"""Regression checks for item-rooted epic generation.

Run with: python -m unittest discover -s .epics -p 'test_epic_item_roots.py'
Requires ~/.eqclient/quest_graph.jsonl and the generated caches for integration tests.
"""

from __future__ import annotations

import ast
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WRITER = ROOT / "scripts" / "write_epics_v2.py"
GRAPH = Path.home() / ".eqclient" / "quest_graph.jsonl"


def epic_items() -> dict[str, dict[str, tuple[int, ...]]]:
    module = ast.parse(WRITER.read_text(encoding="utf-8"))
    for statement in module.body:
        if isinstance(statement, ast.AnnAssign) and isinstance(statement.target, ast.Name):
            if statement.target.id == "EPIC_ITEMS":
                return ast.literal_eval(str(statement.value))
    raise AssertionError("EPIC_ITEMS is missing")


class EpicRootsTest(unittest.TestCase):
    def test_roots_cover_every_class_and_tier(self) -> None:
        roots = epic_items()
        self.assertEqual(len(roots), 16)
        for name, eras in roots.items():
            with self.subTest(name=name):
                self.assertEqual(set(eras), {"1.0", "1.5", "2.0"})
                self.assertTrue(all(eras[era] for era in eras))
        self.assertEqual(roots["ranger"]["1.0"], (20487, 20488))
        self.assertEqual(roots["cleric"]["1.0"], (5532,))

    @unittest.skipUnless(GRAPH.is_file(), "quest graph not built")
    def test_roots_present_in_graph(self) -> None:
        wanted = {
            item_id for eras in epic_items().values() for ids in eras.values() for item_id in ids
        }
        found = set()
        with GRAPH.open(encoding="utf-8") as stream:
            for line in stream:
                row = json.loads(line)
                if row.get("kind") == "item" and row.get("item") in wanted:
                    found.add(row["item"])
        self.assertEqual(wanted - found, set())

    @unittest.skipUnless(GRAPH.is_file(), "quest graph not built")
    def test_ranger_and_cleric_outputs(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            for name in ("ranger", "cleric"):
                subprocess.run(
                    [
                        sys.executable,
                        str(WRITER),
                        "--class",
                        name,
                        "--graph",
                        str(GRAPH),
                        "--out",
                        directory,
                    ],
                    cwd=ROOT,
                    check=True,
                )
            ranger = (output / "ranger.md").read_text(encoding="utf-8")
            cleric = (output / "cleric.md").read_text(encoding="utf-8")
            for text in (ranger, cleric):
                for era in ("1.0", "1.5", "2.0"):
                    self.assertIn(f"## Epic {era}", text)
            # The regression is the *item chain*, not merely a flag section.
            for required in (
                "Swiftwind",
                "Earthcaller",
                "Heartwood Blade",
                "Aurora, the Heartwood Blade",
                "Worn Note",
                "Faelin Bloodbriar",
                "Xanuusus",
                "Corun's Notes",
                "Targen Stonefall",
                "Oshimai Spirit Of The High Air",
                "ranger_epic15_pre",
                "ranger_epic",
            ):
                self.assertIn(required, ranger)
            for required in (
                "Water Sprinkler of Nem Ankh",
                "Avatar of Water",
                "Harmony of the Soul",
                "Aegis of Superior Divinity",
            ):
                self.assertIn(required, cleric)


if __name__ == "__main__":
    unittest.main()
