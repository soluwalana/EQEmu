"""Water map load + swim height helpers."""

from eqclient.navmesh import maps_root
from eqclient.water import load_water, swim_height


def test_swim_height_steps_toward_target():
    assert swim_height(0.0, 2.0) == 2.0
    assert swim_height(0.0, 20.0) == 4.0
    assert swim_height(10.0, 0.0) == 6.0


def test_lakerathe_water_map_detects_liquid():
    root = maps_root()
    if root is None or not (root / "water" / "lakerathe.wtr").is_file():
        return
    water = load_water("lakerathe", root)
    assert water is not None and water.version == 1
    # Known liquid column from the BSP probe near the lake.
    assert water.in_liquid(1225.0, 3975.0, -50.0)
    assert not water.in_liquid(1213.0, 4183.0, 3.0)  # safe point on land
    surf = water.surface_z(1225.0, 3975.0)
    assert surf is not None and surf <= -40.0
    assert water.crosses((1213.0, 4183.0, 3.0), (1225.0, 3975.0, -50.0))
    # Shore near the lake should be a fishable stand.
    spot = water.fish_spot(1213.0, 4183.0, 3.0, radius=200.0)
    assert spot is not None
    assert water.can_fish_at(*spot)
    assert water.fish_aim(*spot) is not None


def test_tutorialb_water_map_loads_v2():
    root = maps_root()
    if root is None or not (root / "water" / "tutorialb.wtr").is_file():
        return
    water = load_water("tutorialb", root)
    assert water is not None and water.version == 2
    assert len(water.regions) >= 1
