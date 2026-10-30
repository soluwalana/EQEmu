"""Movement strides, consider, doors, water, and mesh routes."""

import struct
import pytest
from eqclient3.movement import Movement, MovementAnnotatedMob, pack_server_position
from eqclient3.nav.navmesh import NavMesh, _Poly
from eqclient3.nav.path import STRIDE


class Loop:

    def __init__(self):
        self.outbound = []
        self.tick = 0
        self.active = None

    def send(self, opcode, payload):
        self.outbound.append((opcode, payload))


class Faction:

    def __init__(self, amount, maxed=None, changed=False):
        self.amount = amount
        self.maxed = maxed
        self.changed = changed


class Mob:

    def __init__(self, spawn_id, x, y, z, **kwargs):
        self.spawn_id = spawn_id
        self.id = spawn_id
        self.x = x
        self.y = y
        self.z = z
        self.distance = kwargs.get("distance")
        self.direction = kwargs.get("direction")
        self.consider = kwargs.get("consider")
        self.targeted = kwargs.get("targeted", False)
        self.faction_id = kwargs.get("faction_id", 0)
        self.faction_last_considered = kwargs.get("faction_last_considered", None)
        self._consider_sent = False
        self._consider_change_sent = False


class Door:

    def __init__(self, door_id, x, y, z, opened=False):
        self.id = door_id
        self.door_id = door_id
        self.x = x
        self.y = y
        self.z = z
        self.opened = opened


class Water:

    def __init__(self, surface=30.0):
        self.surface = surface

    def in_liquid(self, x, y, z):
        return True

    def surface_z(self, x, y):
        return self.surface


class World:

    def __init__(self):
        self.self_id = 1
        self.zone = ""
        self.position = (0.0, 0.0, 0.0)
        self.mobs = {}
        self.doors = {}
        self.factions = {}
        self.skills = {}
        self.water = None
        self.water_map = None
        self.active = None
        self.movement = Movement(self)

    def line_of_sight(self, mob):
        del mob
        return True

    def nearby(self, yards):
        here = self.movement.position
        found = []
        for mob in self.mobs.values():
            dist = ((mob.x - here[0]) ** 2 + (mob.y - here[1]) ** 2) ** 0.5
            if dist <= yards:
                found.append(mob)
        found.sort(key=lambda mob: (mob.x - here[0]) ** 2 + (mob.y - here[1]) ** 2)
        return found


class Reclaim:
    pass


class Talk:
    pass


@pytest.fixture(autouse=True)
def _fresh():
    yield


def _ops(loop, name):
    return [payload for opcode, payload in loop.outbound if opcode == name]


def _update(payload):
    spawn = struct.unpack_from("<H", payload, 2)[0]
    delta_x = struct.unpack_from("<f", payload, 10)[0]
    heading = struct.unpack_from("<I", payload, 14)[0] & 0xFFF
    x = struct.unpack_from("<f", payload, 18)[0]
    delta_z = struct.unpack_from("<f", payload, 22)[0]
    z = struct.unpack_from("<f", payload, 26)[0]
    y = struct.unpack_from("<f", payload, 30)[0]
    animation = struct.unpack_from("<I", payload, 34)[0] & 1023
    delta_y = struct.unpack_from("<f", payload, 38)[0]
    return {
        "spawn": spawn,
        "y": y,
        "dz": delta_z,
        "dx": delta_x,
        "dy": delta_y,
        "anim": animation,
        "x": x,
        "z": z,
        "heading": heading // 4,
    }


def _place(world, point=(0.0, 0.0, 0.0)):
    world.movement.bind(world)
    world.movement.handle("OP_ClientUpdate", pack_server_position(world.self_id, *point), world)


def test_stride_lengths_and_anims():
    world = World()
    _place(world)
    cases = {
        "run": (STRIDE["run"][0], 20),
        "walk": (STRIDE["walk"][0], 12),
        "los": (STRIDE["los"][0], 20),
        "creep": (STRIDE["creep"][0], 12),
        "hold": (0.0, 0),
    }
    assert cases["run"] == pytest.approx((10.5, 20))
    assert cases["walk"][0] == pytest.approx(3.5)
    assert cases["los"][0] == pytest.approx(14.7)
    assert cases["creep"][0] == pytest.approx(1.75)
    for mode, (length, anim) in cases.items():
        world.movement.reset()
        _place(world)
        before = world.position
        loop = Loop()
        path = world.movement.plan((100.0, 0.0, 0.0), mode, world=world, loop=loop)
        assert loop.outbound == []
        assert world.position == before
        assert world.movement.position == before
        world.movement.advance(loop, world, path)
        updates = _ops(loop, "OP_ClientUpdate")
        assert len(updates) == 1
        step = _update(updates[0])
        assert step["anim"] == anim
        assert (step["dx"] ** 2 + step["dy"] ** 2) ** 0.5 == pytest.approx(length)
        assert step["x"] == pytest.approx(length)
        assert step["y"] == pytest.approx(0.0)
        assert step["z"] == pytest.approx(0.0)
        assert world.position == before


def test_plan_and_distance_send_no_consider():
    world = World()
    _place(world)
    world.mobs[2] = Mob(2, 10.0, 0.0, 0.0, faction_id=5)
    world.factions[5] = Faction(10)
    loop = Loop()
    path = world.movement.plan((80.0, 0.0, 0.0), "run", world=world, loop=loop)
    yards = path.distance
    assert yards == pytest.approx(80.0)
    assert _ops(loop, "OP_Consider") == []
    assert _ops(loop, "OP_ClientUpdate") == []
    assert world.movement.position == (
        pytest.approx(0.0),
        pytest.approx(0.0),
        pytest.approx(0.0),
    )


def test_advance_consider_once_then_on_faction_change_not_when_maxed():
    world = World()
    _place(world)
    near = Mob(2, 10.0, 0.0, 0.0, faction_id=5)
    also = Mob(3, 12.0, 1.0, 0.0, faction_id=6)
    hidden = Mob(4, 8.0, 0.0, 0.0, faction_id=7)
    far = Mob(5, 800.0, 0.0, 0.0, faction_id=8)
    world.mobs = {mob.spawn_id: mob for mob in (near, also, hidden, far)}
    world.factions = {5: Faction(10), 6: Faction(3), 7: Faction(1), 8: Faction(1)}

    def line_of_sight(mob):
        return mob is not hidden

    world.line_of_sight = line_of_sight
    loop = Loop()
    path = world.movement.plan((100.0, 0.0, 0.0), "run", world=world)
    world.movement.advance(loop, world, path)
    targets = [struct.unpack_from("<II", payload)[1] for payload in _ops(loop, "OP_Consider")]
    assert sorted(targets) == [2, 3]
    assert near.faction_last_considered == 10
    assert also.faction_last_considered == 3
    assert hidden.faction_last_considered is None
    assert far.faction_last_considered is None
    world.movement.advance(loop, world, path)
    assert len(_ops(loop, "OP_Consider")) == 2
    world.factions[5].amount = 12
    world.movement.advance(loop, world, path)
    targets = [struct.unpack_from("<II", payload)[1] for payload in _ops(loop, "OP_Consider")]
    assert targets.count(2) == 2
    assert near.faction_last_considered == 12
    world.factions[5].amount = 40
    world.factions[5].maxed = 1
    world.factions[6].amount = -40
    world.factions[6].maxed = -1
    world.movement.advance(loop, world, path)
    assert len(_ops(loop, "OP_Consider")) == 3


def test_reclaim_sends_no_consider():
    world = World()
    _place(world)
    world.mobs[2] = Mob(2, 10.0, 0.0, 0.0, faction_id=5)
    world.factions[5] = Faction(10)
    path = world.movement.plan((50.0, 0.0, 0.0), "run", world=world)
    loop = Loop()
    world.movement.advance(loop, world, path, sender=Reclaim())
    assert _ops(loop, "OP_Consider") == []
    loop.active = Reclaim()
    world.movement.advance(loop, world, path)
    assert _ops(loop, "OP_Consider") == []
    loop.active = Talk()
    world.movement.advance(loop, world, path, sender=Talk())
    assert len(_ops(loop, "OP_Consider")) == 1


def test_visible_mobs_and_mobs_on_path_send_nothing_and_copy_fields():
    world = World()
    _place(world)
    mob = Mob(
        9,
        5.0,
        0.0,
        0.0,
        distance=4.0,
        direction=90,
        consider=8,
        targeted=True,
        faction_id=5,
    )
    aside = Mob(10, 5.0, 400.0, 0.0, distance=400.0, direction=1, consider=2, targeted=False)
    world.mobs = {9: mob, 10: aside}
    world.factions[5] = Faction(1)
    loop = Loop()
    path = world.movement.plan((40.0, 0.0, 0.0), "run", world=world, loop=loop)
    seen = world.movement.visible_mobs(world, loop=loop)
    assert mob in seen and aside in seen
    assert _ops(loop, "OP_Consider") == []
    world.movement.advance(loop, world, path)
    on_path = world.movement.mobs_on_path([mob, aside], loop=loop)
    assert on_path is not None
    assert len(on_path) == 1
    assert isinstance(on_path[0], MovementAnnotatedMob)
    assert on_path[0].mob is mob
    assert on_path[0].distance == 4.0
    assert on_path[0].direction == 90
    assert on_path[0].consider == 8
    assert on_path[0].targeted is True
    assert world.movement.mobs_on_path([aside], loop=loop) is None
    assert len(_ops(loop, "OP_Consider")) == 1
    assert len(_ops(loop, "OP_ClientUpdate")) == 1


def test_only_client_update_was_queued_by_advance():
    world = World()
    _place(world)
    loop = Loop()
    path = world.movement.plan((30.0, 0.0, 0.0), "run", world=world, loop=loop)
    _ = path.distance
    world.movement.visible_mobs(loop=loop)
    world.movement.mobs_on_path([], loop=loop)
    assert _ops(loop, "OP_ClientUpdate") == []
    world.movement.advance(loop, world, path)
    assert len(_ops(loop, "OP_ClientUpdate")) == 1
    assert _update(_ops(loop, "OP_ClientUpdate")[0])["anim"] == 20


def test_closed_door_clicks_once_and_next_stride_waits():
    world = World()
    _place(world)
    door = Door(7, 4.0, 0.0, 0.0, opened=False)
    world.doors = {7: door}
    loop = Loop()
    path = world.movement.plan((40.0, 0.0, 0.0), "run", world=world)
    assert path.door is door
    assert path.next_point[0] == pytest.approx(4.0)
    world.movement.advance(loop, world, path)
    clicks = _ops(loop, "OP_ClickDoor")
    assert len(clicks) == 1
    assert len(clicks[0]) == 16
    assert clicks[0][0] == 7
    assert world.movement.asked[0] == pytest.approx(4.0)
    names = [opcode for opcode, _payload in loop.outbound]
    assert names.index("OP_ClickDoor") < names.index("OP_ClientUpdate")
    world.movement.handle(
        "OP_ClientUpdate",
        pack_server_position(world.self_id, *world.movement.asked),
        world,
    )
    assert world.movement.stride_committed
    world.movement.advance(loop, world, path)
    assert len(_ops(loop, "OP_ClickDoor")) == 1
    assert world.movement.asked[0] == pytest.approx(4.0)
    assert len(_ops(loop, "OP_ClientUpdate")) == 1
    world.movement.handle("OP_MoveDoor", bytes([7]), world)
    assert door.opened
    world.movement.advance(loop, world, path)
    assert world.movement.asked[0] > 4.5
    assert len(_ops(loop, "OP_ClickDoor")) == 1


def test_water_point_and_swim_changes_only_z():
    world = World()
    world.water_map = Water(surface=30.0)
    world.water = world.water_map
    _place(world)
    reported = world.movement.plan((0.0, 0.0, -5.0), "run", world=world)
    assert reported.in_water
    world.movement.plan((0.0, 0.0, 0.0), "walk", world=world)
    path = world.movement.plan((0.0, 0.0, 30.0), "swim", world=world)
    assert path.in_water
    assert path.z_only
    loop = Loop()
    before = world.movement.position
    world.movement.advance(loop, world, path)
    step = _update(_ops(loop, "OP_ClientUpdate")[0])
    assert step["x"] == pytest.approx(before[0])
    assert step["y"] == pytest.approx(before[1])
    assert step["dx"] == pytest.approx(0.0)
    assert step["dy"] == pytest.approx(0.0)
    assert step["z"] == pytest.approx(STRIDE["walk"][0])
    assert step["anim"] == 12
    assert world.movement.position == before


def test_other_spawn_is_ignored_and_new_zone_sets_safe_point():
    world = World()
    _place(world, (1.0, 2.0, 3.0))
    world.movement.handle("OP_ClientUpdate", pack_server_position(99, 9.0, 9.0, 9.0), world)
    world.movement.handle("OP_MobUpdate", pack_server_position(99, 8.0, 8.0, 8.0), world)
    assert world.movement.position[0] == pytest.approx(1.0)
    assert world.position[0] == pytest.approx(1.0)
    from eqclient3.structs import OP_NewZone

    world.movement.handle("OP_NewZone", OP_NewZone("qeynos", 5.0, 6.0, 7.0).serialize(), world)
    assert world.movement.asked is None
    assert world.movement.stride_committed
    assert world.movement.position == pytest.approx((5.0, 6.0, 7.0))
    assert world.position == pytest.approx((5.0, 6.0, 7.0))
    assert world.zone == "qeynos"


def test_hold_if_idle_sends_one_hold_when_advance_was_not_called():
    world = World()
    _place(world, (2.0, 3.0, 4.0))
    loop = Loop()
    world.movement.hold_if_idle(loop, world)
    step = _update(_ops(loop, "OP_ClientUpdate")[0])
    assert step["anim"] == 0
    assert step["x"] == pytest.approx(2.0)
    assert step["y"] == pytest.approx(3.0)
    assert step["z"] == pytest.approx(4.0)
    assert step["dx"] == pytest.approx(0.0)
    assert step["dy"] == pytest.approx(0.0)
    path = world.movement.plan((20.0, 3.0, 4.0), "run", world=world)
    world.movement.advance(loop, world, path)
    before = len(_ops(loop, "OP_ClientUpdate"))
    world.movement.hold_if_idle(loop)
    assert len(_ops(loop, "OP_ClientUpdate")) == before


def test_find_and_track_and_reply_waypoints():
    world = World()
    _place(world)
    far = Mob(15, 500.0, 0.0, 0.0)
    near = Mob(16, 10.0, 0.0, 0.0)
    world.mobs = {15: far, 16: near}
    loop = Loop()
    assert world.movement.find(loop, world, far) is True
    assert [opcode for opcode, _payload in loop.outbound] == ["OP_FindPersonRequest"]
    assert world.movement.find(loop, world, near) is False
    assert len(loop.outbound) == 1
    path = world.movement.plan((500.0, 0.0, 0.0), "run", world=world)
    world.line_of_sight = lambda mob: False
    reply = struct.pack("<fff", 0.0, 400.0, 0.0)
    reply += struct.pack("<fff", 80.0, 0.0, 0.0)
    reply += struct.pack("<fff", 0.0, 400.0, 0.0)
    world.movement.handle("OP_FindPersonReply", reply, world)
    assert path.find_waypoints
    assert path.points[0] == pytest.approx((0.0, 80.0, 0.0))
    world.movement.advance(loop, world, path)
    step = _update(_ops(loop, "OP_ClientUpdate")[0])
    assert step["y"] == pytest.approx(STRIDE["run"][0])
    assert step["x"] == pytest.approx(0.0)
    world.skills = {}
    assert world.movement.track(loop, world, far) is False
    world.skills = {53: 1}
    before = len(loop.outbound)
    assert world.movement.track(loop, world, far) is True
    assert [opcode for opcode, _payload in loop.outbound[before:]] == [
        "OP_Track",
        "OP_TrackTarget",
    ]
    assert struct.unpack("<I", loop.outbound[-1][1])[0] == 15
    assert world.movement.track(loop, world, near) is False
    assert 15 in world.mobs and len(world.mobs) == 2
    assert not any((isinstance(item, MovementAnnotatedMob) for item in world.mobs.values()))


def test_two_point_fallback_does_not_count_as_success():
    triangle = lambda ox, oy: [(ox, oy, 0.0), (ox + 2.0, oy, 0.0), (ox, oy + 2.0, 0.0)]
    start_poly = _Poly(0, 0, (0.5, 0.5, 0.0), triangle(0.0, 0.0), [])
    goal_poly = _Poly(0, 1, (100.5, 0.5, 0.0), triangle(100.0, 0.0), [])
    mesh = NavMesh("tiny", 2, [start_poly, goal_poly])
    start = (0.2, 0.2, 0.0)
    goal = (100.2, 0.2, 0.0)
    points = mesh.path(start, goal)
    assert points[0] == start and points[1] == goal
    assert mesh.reaches(start, goal) is False
    same = (0.4, 0.3, 0.0)
    assert mesh.reaches(start, same) is True
    same_points = mesh.path(start, same)
    assert same_points[0] == start and same_points[1] == same


def test_qeynos_zone_points_reach_on_the_mesh():
    from pathlib import Path

    mesh_file = Path("/Users/samo/work/EQEmu/maps/nav/qeynos.nav")
    if not mesh_file.is_file():
        pytest.skip(f"{mesh_file} is not present")
    graph_file = Path.home() / ".eqclient" / "zone_graph.jsonl"
    if not graph_file.is_file():
        pytest.skip(f"{graph_file} is not present, so qeynos zone points cannot be loaded")
    try:
        from eqclient3.nav.navmesh import load_nav
        from eqclient3.nav.travel import read_zone_graph
    except ImportError as exc:
        pytest.skip(f"qeynos mesh dependency is missing: {exc}")
    try:
        mesh = load_nav("qeynos", root=Path("/Users/samo/work/EQEmu/maps"))
    except (OSError, ValueError) as exc:
        pytest.skip(f"qeynos.nav could not be loaded: {exc}")
    if mesh is None:
        pytest.skip("qeynos.nav could not be loaded")
    try:
        graph = read_zone_graph(str(graph_file))
    except (OSError, ValueError) as exc:
        pytest.skip(f"zone graph could not be read: {exc}")
    points = []
    seen = set()
    for transit in graph.transits_from("qeynos"):
        if (transit.via or "") != "point":
            continue
        key = (
            round(float(transit.x), 1),
            round(float(transit.y), 1),
            round(float(transit.z), 1),
        )
        if key in seen:
            continue
        seen.add(key)
        points.append((float(transit.x), float(transit.y), float(transit.z)))
    if len(points) < 2:
        pytest.skip("qeynos zone points are not in the zone graph")
    for start in points:
        for goal in points:
            if start == goal:
                continue
            assert mesh.reaches(start, goal), f"no mesh route {start} -> {goal}"
