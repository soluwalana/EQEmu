"""Band 0. A task kill or a level camp. OP_BecomeCorpse for this spawn finishes it."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient4.loop import Loop
    from eqclient4.world import World

from eqclient4.action import Action
from eqclient4.actions.attack import Attack

# from eqclient4.actions.support import (
#     INTERACT,
#     has_soulbind,
#     spawn_of,
#     standing_of,
#     walk,
#     yards,
#     yield_to,
# )
# from eqclient4.actions.talk import append_soulbind
from eqclient4.actions.travel import Travel
from eqclient4.log import log
from eqclient4.nav.navmesh import load_nav
from eqclient4.nav.path import STRIDE, straight
from eqclient4.world import Mob


class Kill(Action):

    def __init__(
        self,
        world: World,
        loop: Loop,
        spawn_id: int | None = None,
        camp: str | tuple[int, ...] | None = None,
        level: int | None = None,
    ) -> None:
        super().__init__()
        self.priority = 0
        self.spawn_id = spawn_id or None
        self.camp = camp
        self.level = level
        self.roaming = False
        self.anchor: tuple[float, float] | None = None
        self.still = 0
        self.skipped: set[int] = set()
        self.until_item = 0
        self.until_count = 0
        self.turns = 0
        # Spoken names of the mobs that drop until_item, and their spawn points.
        self.mobs: tuple[str, ...] = ()
        self.posts: tuple[tuple[float, float, float], ...] = ()
        self.cursor = 0
        self.post = 0
        self.prey_loaded = False
        self.force = False

    def __setstate__(self, state: dict[str, object]) -> None:
        self.__dict__.update(state)
        if "turns" not in self.__dict__:
            self.turns = 0
        if "mobs" not in self.__dict__:
            self.mobs = ()
        if "posts" not in self.__dict__:
            self.posts = ()
        if "cursor" not in self.__dict__:
            self.cursor = 0
        if "post" not in self.__dict__:
            self.post = 0
        if "prey_loaded" not in self.__dict__:
            self.prey_loaded = False
        if "force" not in self.__dict__:
            self.force = False

    def opcodes(self) -> tuple[str, ...]:
        return super().opcodes() + ("OP_BecomeCorpse",)

    def step(self, loop: Loop, world: World) -> None:
        if self.spawn_id and self._corpse():
            self.complete = True
            return
        if self.until_item and world.held(self.until_item) >= max(self.until_count, 1):
            self.complete = True
            return
        if self._elsewhere(loop, world):
            return
        if str(self.source).startswith("find:"):
            self.priority = -1
            self._share_book(loop)
        self.suspended = False
        queue = loop.queue
        if queue is None:
            return
        if not has_soulbind(loop, world) and (
            not any((str(a.source).startswith("soulbind:") for a in queue))
        ):
            if append_soulbind(self, loop, world):
                return
        if (
            self.spawn_id is None
            and self.level is not None
            and (int(world.level or 0) >= int(self.level))
        ):
            self.complete = True
            return
        self._unstick(world)
        before = self.spawn_id
        previous = self.where
        dest = self._dest(world)
        if dest is None:
            return
        if self.spawn_id != before or self.where != previous:
            self.active_path = None
        if yards(world, dest) > INTERACT:
            mob = world.mobs.get(self.spawn_id) if self.spawn_id else None
            close = mob is not None and yards(world, dest) <= 35 and world.line_of_sight(mob)
            if self.force or close:
                self.force = False
                length = STRIDE["los"][0]
                path = straight((world.x, world.y, world.z), dest, length)
                self.active_path = path
                world.movement.advance(loop, world, path)
                return
            walk(self, loop, world, dest, "run")
            return
        if self.spawn_id and (
            not any(
                (
                    type(action).__name__ == "Attack" and action.spawn_id == self.spawn_id
                    for action in queue
                )
            )
        ):
            attack = Attack(self.spawn_id)
            world.note_fight(self.spawn_id)
            mob = world.mobs.get(self.spawn_id)
            if mob is not None:
                attack.level = int(mob.level or 0)
            yield_to(self, loop, world, attack, f"kill:{self.spawn_id}")

    def _elsewhere(self, loop: Loop, world: World) -> bool:
        """A camp that names another zone is a trip, not a mob in this one."""
        camp = self.camp if isinstance(self.camp, str) else ""
        here = str(world.zone or "").lower()
        if not camp or camp.lower() == here or not _is_zone(camp):
            self.priority = 0
            return False
        source = f"{self.source}#travel"
        queue = loop.queue
        if queue is not None and any(
            action.source == source and not action.complete for action in queue
        ):
            self.priority = -1
            self.yielding = True
            return True
        if yield_to(self, loop, world, Travel(camp), source):
            self.priority = -1
            return True
        return False

    def _corpse(self) -> bool:
        return (
            self.consume(
                "OP_BecomeCorpse",
                lambda message: spawn_of(message) in (0, self.spawn_id),
            )
            is not None
        )

    def _dest(self, world: World) -> tuple[float, float, float] | None:
        """The live target, a camp point, or the next unvisited patch of this zone."""
        self.roaming = False
        if self.spawn_id and self.spawn_id in world.unreachable:
            self.skipped.add(int(self.spawn_id))
            self.spawn_id = None
        if self.spawn_id and self.spawn_id in world.mobs and not world.mobs[self.spawn_id].dead:
            return world.mobs[self.spawn_id].position
        self.spawn_id = None
        avoid = self.skipped | world.unreachable
        if self.until_item:
            self._ensure_prey(world)
        if self.mobs:
            found = _one_of(world, self.mobs, self.cursor, avoid)
            if found is not None:
                chosen, index = found
                self.cursor = (index + 1) % len(self.mobs)
                self.spawn_id = int(chosen.id)
                self.where = None
                return chosen.position
            return self._next_post(world)
        name = self.camp if isinstance(self.camp, str) else ""
        here = str(world.zone or "").lower()
        if name and name.lower() != here:
            mob = _named(world, name, avoid)
            if mob is not None:
                self.spawn_id = int(mob.id)
                self.where = None
                return mob.position
        elif name and name.lower() == here:
            mob = _prey(world, avoid)
            if mob is not None:
                self.spawn_id = int(mob.id)
                self.where = None
                return mob.position
        point = _camp_point(self.camp)
        if point is not None:
            return point
        camps = world.camps or {}
        if name and name in camps:
            return camps[name]
        if not name:
            return None
        return self._roam(world)

    def _ensure_prey(self, world: World) -> None:
        """The mobs and spawn points that drop until_item in this zone."""
        if self.prey_loaded or not world.zone:
            return
        self.prey_loaded = True
        here = str(world.zone).lower()
        names: list[str] = list(self.mobs)
        posts: list[tuple[float, float, float]] = []
        for row in read_locations().points(int(self.until_item)):
            if str(row.get("zone") or "").lower() != here:
                continue
            name = str(row.get("name") or "")
            if name and name not in names:
                names.append(name)
            posts.append(
                (float(row.get("x") or 0.0), float(row.get("y") or 0.0), float(row.get("z") or 0.0))
            )
        posts.sort(key=lambda point: (point[0] - world.x) ** 2 + (point[1] - world.y) ** 2)
        self.mobs = tuple(names)
        self.posts = tuple(posts)

    def _next_post(self, world: World) -> tuple[float, float, float] | None:
        """The next spawn point of the droppers. None of them are up right now."""
        posts = self.posts
        if not posts:
            return None
        if self.where is not None and yards(world, self.where) > INTERACT:
            self.roaming = True
            return self.where
        count = len(posts)
        for _ in range(count):
            point = posts[self.post % count]
            self.post += 1
            if yards(world, point) > INTERACT:
                self.where = point
                self.roaming = True
                return point
        return None

    def _roam(self, world: World) -> tuple[float, float, float] | None:
        if self.where is not None and yards(world, self.where) > INTERACT:
            self.roaming = True
            return self.where
        mesh = load_nav(str(world.zone or ""))
        point = None if mesh is None else mesh.unvisited(world.position)
        if point is None:
            return self.where
        if self.where is None:
            log.info("kill search %s", self.camp)
        self.where = point
        self.roaming = True
        return point

    def _unstick(self, world: World) -> None:
        """A path that is not moving is dropped so the next target can be chosen."""
        here = (round(world.x, 1), round(world.y, 1))
        if here == self.anchor:
            self.still += 1
        else:
            self.anchor = here
            self.still = 0
        if self.still < 50:
            return
        mesh = load_nav(str(world.zone or ""))
        point = self.where
        if mesh is not None and point is not None:
            spot = mesh.locate(point)
            if spot is not None:
                mesh.visited.add(spot)
        mob = world.mobs.get(self.spawn_id) if self.spawn_id else None
        distance = 0.0 if mob is None else mob.distance
        log.info("kill unstick %s spawn=%s d=%.0f", self.camp, self.spawn_id, distance)
        self.force = True
        if self.spawn_id:
            self.skipped.add(int(self.spawn_id))
        self.spawn_id = None
        self.where = None
        self.active_path = None
        self.still = 0

    def _share_book(self, loop: Loop) -> None:
        """A side hunt sits under the task book and lets that book look again."""
        self.turns += 1
        if self.turns % 40:
            return
        queue = loop.queue
        if queue is None:
            return
        for action in queue:
            if str(action.source).startswith("read_tasks:") and action.priority < 0:
                action.priority = 0


def _is_zone(name: str) -> bool:
    graph = ensure_zone_graph()
    if graph is None:
        return False
    return name.lower() in graph.zones


def _fold_name(name: str) -> str:
    """Task targets are plural titles. Spawns are 'a gloomfang lurker'."""
    text = " ".join(name.replace("_", " ").lower().split())
    if text.startswith("a "):
        text = text[2:]
    elif text.startswith("an "):
        text = text[3:]
    if text.endswith("s") and not text.endswith("ss"):
        text = text[:-1]
    return text


def _one_of(
    world: World, names: tuple[str, ...], cursor: int, skip: set[int]
) -> tuple[Mob, int] | None:
    """The next listed mob that is alive. cursor is where the previous pick left off."""
    folded = [_fold_name(name) for name in names]
    if not folded:
        return None
    start = cursor % len(folded)
    for offset in range(len(folded)):
        index = (start + offset) % len(folded)
        want = folded[index]
        chosen: Mob | None = None
        chosen_d = 0.0
        for mob in world.mobs.values():
            if mob.dead or int(mob.id) in skip:
                continue
            if _fold_name(mob.spoken_name()) != want:
                continue
            if chosen is None or mob.distance < chosen_d:
                chosen = mob
                chosen_d = mob.distance
        if chosen is not None:
            return (chosen, index)
    return None


def _named(world: World, name: str, skip: set[int]) -> Mob | None:
    """Nearest living mob whose spoken name matches. Corpses stay out."""
    want = _fold_name(name)
    if not want:
        return None
    exact = None
    exact_d = 0.0
    partial = None
    partial_d = 0.0
    for mob in world.mobs.values():
        if mob.dead or int(mob.id) in skip:
            continue
        found = _fold_name(mob.spoken_name())
        if found == want:
            if exact is None or mob.distance < exact_d:
                exact = mob
                exact_d = mob.distance
        elif want in found or found in want:
            if partial is None or mob.distance < partial_d:
                partial = mob
                partial_d = mob.distance
    return exact or partial


def _prey(world: World, skip: set[int]) -> Mob | None:
    """Nearest creature that will fight, else the nearest 'a …' mob in camp."""
    hostile = None
    hostile_d = 0.0
    creature = None
    creature_d = 0.0
    for mob in world.mobs.values():
        if mob.dead or mob.id == world.self_id or int(mob.id) in skip:
            continue
        if standing_of(mob) in (8, 9):
            if hostile is None or mob.distance < hostile_d:
                hostile = mob
                hostile_d = mob.distance
            continue
        spoken = mob.spoken_name().lower()
        if spoken.startswith("a ") or spoken.startswith("an "):
            if creature is None or mob.distance < creature_d:
                creature = mob
                creature_d = mob.distance
    return hostile or creature


def _camp_point(camp: str | tuple[int, ...] | None) -> tuple[float, float, float] | None:
    if not isinstance(camp, tuple) or len(camp) != 3:
        return None
    return (float(camp[0]), float(camp[1]), float(camp[2]))
