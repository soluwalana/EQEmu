"""Zone-agnostic quest loop. The same steps run in the mine and in whatever zone comes next."""

from __future__ import annotations

import os
import struct
import time
from dataclasses import dataclass, field
from pathlib import Path

from eqclient.client import Client, connect
from eqclient.items import (
    CURSOR,
    PRIMARY,
    TRADE,
    TRAIN_SKILLS,
    Inventory,
    equip_move,
    missing_entries,
    stack_totals,
    stow_move,
)
from eqclient.journal import Journal
from eqclient.maps import ZoneMap, load_map
from eqclient.navmesh import NavMesh, load_nav
from eqclient.opcodes import require
from eqclient.packets import client_position
from eqclient.plan import Intention, _task_needs, choose
from eqclient.party import PartyBuilder
from eqclient.quests import ZoneQuests, load_zone
from eqclient.sheet import Character, build
from eqclient.tasks import TaskBook
from eqclient.world import ZoneModel, doors_along

STEP = 8.0
_ACT_RANGE = {
    "task_kill": 18.0,
    "fight": 18.0,
    "loot": 15.0,
    "reclaim": 15.0,
    "train": 15.0,
    "task_talk": 25.0,
    "hail": 25.0,
    "talk": 25.0,
    "hand_in": 15.0,
    "fetch": 8.0,
    "search": 8.0,
}


@dataclass
class Score:
    activities: int = 0
    fetched: int = 0
    hails: int = 0
    keywords: int = 0
    doors: int = 0
    kills: int = 0
    zone: str = ""
    zones: list[str] = field(default_factory=list)

    def line(self) -> str:
        return (
            f"score activities={self.activities} fetched={self.fetched} hails={self.hails} "
            f"keywords={self.keywords} doors={self.doors} kills={self.kills} zone={self.zone}"
        )


@dataclass(frozen=True)
class AgentSpec:
    """One character. A second agent is a second spec, not a change to the environment."""

    character: str
    user: str | None = None
    password: str | None = None
    race: int = 1
    class_id: int = 1
    gender: int = 0
    deity: int | None = None
    start_zone: int | None = None
    bot_prefix: str | None = None
    journal_path: str | None = None

    def sheet(self) -> Character:
        return build(self.race, self.class_id, self.gender, self.deity, self.start_zone)

    @classmethod
    def from_environ(cls) -> AgentSpec:
        deity = os.environ.get("EQEMU_DEITY")
        start = os.environ.get("EQEMU_START_ZONE")
        return cls(
            os.environ["EQEMU_CHAR"],
            os.environ.get("EQEMU_USER"),
            os.environ.get("EQEMU_PASS"),
            int(os.environ.get("EQEMU_RACE", "1")),
            int(os.environ.get("EQEMU_CLASS", "1")),
            int(os.environ.get("EQEMU_GENDER", "0")),
            int(deity) if deity else None,
            int(start) if start else None,
            os.environ.get("EQEMU_BOT_PREFIX"),
            os.environ.get("EQEMU_JOURNAL"),
        )


class Agent:
    def __init__(self, client: Client) -> None:
        self.client = client
        self.model = ZoneModel(client._character)
        self.tasks = TaskBook()
        self.inventory = Inventory()
        self.party = PartyBuilder(client._character, getattr(client, "_bot_prefix", None))
        self.quests = ZoneQuests("")
        self.nav: NavMesh | None = None
        self.zone_map: ZoneMap | None = None
        self.score = Score()
        self.path: list[tuple[float, float, float]] = []
        self.skipped_ground: set[int] = set()
        self.skipped_corpses: set[int] = set()
        self.said: set[tuple[str, str]] = set()
        self.handed: set[tuple[str, str]] = set()
        self.attacked: set[int] = set()
        journal_path = getattr(client, "_journal_path", None) or os.environ.get(
            "EQEMU_JOURNAL", str(Path.home() / ".eqclient" / "journal.sqlite")
        )
        self.journal = Journal(journal_path)
        sheet = getattr(client, "_sheet", None)
        if sheet is not None:
            self.model.class_id = sheet.class_id
            self.model.race_id = sheet.race
        played = getattr(client, "_played", None)
        if played is not None:
            self.model.apply_played(played)
        self._opcodes = {name: require(client._opcodes, name) for name in _WATCHED if name in client._opcodes}
        self._by_opcode = {value: name for name, value in self._opcodes.items()}
        self._messages = 0
        self._trade_with = 0
        self._seen_done: dict[tuple[int, int], int] = {}
        self._retired_skills: set[int] = set()
        self._skill_index = 0
        self._trained = False
        self._loot_open = 0

    def attach(self) -> None:
        self.client.listen(self.on_packet)

    def on_packet(self, opcode: int, payload: bytes) -> None:
        name = self._by_opcode.get(opcode)
        if name == "OP_NewZone":
            self.model.on_new_zone(payload)
            self.tasks.set_here(self.model.zone)
            self._enter_zone()
        elif name == "OP_ZoneSpawns" or name == "OP_NewSpawn":
            self.model.on_spawns(payload)
        elif name == "OP_DeleteSpawn":
            spawn_id = self.model.on_delete_spawn(payload)
            if spawn_id in self.attacked:
                self.score.kills += 1
                self.attacked.discard(spawn_id)
        elif name == "OP_SpawnDoor":
            self.model.on_doors(payload)
        elif name == "OP_GroundSpawn":
            self.model.on_ground(payload)
        elif name == "OP_ClickObject":
            self.model.on_click_object(payload)
        elif name == "OP_ClientUpdate":
            self.model.on_client_update(payload)
        elif name == "OP_RequestClientZoneChange":
            self.model.on_request_zone_change(payload)
        elif name == "OP_ZoneChange":
            self.model.on_zone_change(payload)
        elif name == "OP_Death":
            if self.model.on_death(payload):
                self.inventory.clear()
        elif name == "OP_PlayerProfile":
            from eqclient.packets import player_profile

            played = player_profile(payload)
            if played is not None:
                self.model.apply_played(played)
        elif name == "OP_LevelUpdate":
            if len(payload) >= 8:
                level, old = struct.unpack_from("<II", payload)
                self.model.grant_levels(level, old)
        elif name == "OP_SkillUpdate":
            self._trained = True
        elif name == "OP_MoneyOnCorpse" and payload:
            self._loot_open = payload[0]
        elif name == "OP_BecomeCorpse":
            self.model.on_become_corpse(payload)
            if len(payload) >= 4:
                spawn_id = struct.unpack_from("<I", payload)[0]
                if spawn_id in self.attacked:
                    self.score.kills += 1
        elif name == "OP_Consider":
            self.model.on_consider(payload)
        elif name == "OP_MoveDoor":
            door_id = self.model.on_move_door(payload)
            if door_id:
                self.score.doors += 1
        elif name == "OP_ItemPacket":
            self.inventory.on_packet(payload, self._wanted_ids())
        elif name == "OP_TaskSelectWindow":
            self.tasks.on_select_window(payload)
            accept = self.tasks.accept_bytes()
            if accept:
                self.client.send("OP_AcceptNewTask", accept)
        elif name == "OP_TaskActivity":
            before = _done_map(self.tasks)
            self.tasks.on_activity(payload)
            self._note_progress(before)
        elif name == "OP_TaskActivityComplete":
            before = _done_map(self.tasks)
            self.tasks.on_complete(payload)
            self._note_progress(before)

    def run(self, seconds: float | None = None, stop_on_zone: bool = False) -> Score:
        limit = seconds if seconds is not None else float(os.environ.get("EQEMU_AGENT_SECONDS", "180"))
        stop_on_zone = stop_on_zone or os.environ.get("EQEMU_AGENT_STOP_ON_ZONE") == "1"
        started_zone = self.model.zone
        deadline = time.monotonic() + limit
        next_report = 0.0
        while time.monotonic() < deadline:
            self.client.pump(0.4)
            if self.model.consume_server_move():
                self.path = []
            self._party_messages()
            if stop_on_zone and self.model.changed_zone and self.model.zone and self.model.zone != started_zone:
                break
            if not self.party.formed:
                next_report = self._report(next_report, "form_party", force=False)
                self._form_party()
                continue
            self._equip()
            self._stow()
            intention = choose(
                self.model,
                self.tasks,
                self.quests,
                self.inventory,
                True,
                self.skipped_ground,
                self.skipped_corpses,
                self.said,
                self.handed,
            )
            if intention is None:
                continue
            label = f"{intention.kind} {intention.name or intention.target}".strip()
            changed = label != getattr(self, "_last_act", "")
            next_report = self._report(next_report, label, force=changed)
            self._act(intention)
        self.score.zone = self.model.zone
        print(self.score.line())
        return self.score

    def _report(self, next_report: float, label: str, force: bool) -> float:
        """Print when the goal changes, and where he is every few seconds."""
        now = time.monotonic()
        if not force and now < next_report:
            return next_report
        self._last_act = label
        x, y, z = self.model.position
        print(
            f"act {self.model.zone} L{self.model.level} pts={self.model.points} "
            f"({x:.0f}, {y:.0f}, {z:.0f}) {label}",
            flush=True,
        )
        return now + 5.0

    def _enter_zone(self) -> None:
        zone = self.model.zone
        if zone and zone not in self.score.zones:
            self.score.zones.append(zone)
        self.score.zone = zone
        self.quests = load_zone(zone)
        self.nav = load_nav(zone)
        self.zone_map = load_map(zone)
        self.path = []
        self.skipped_ground.clear()
        self.skipped_corpses.clear()
        self.said = self.journal.said(self.model.character, zone)
        self.handed = self.journal.handed(self.model.character, zone)

    def _act(self, intention: Intention) -> None:
        kind = intention.kind
        if kind == "explore":
            where = intention.where
            if where is None and self.nav is not None:
                where = self.nav.unvisited(self.model.position)
            if where is not None:
                self._step(where)
            return
        if kind == "leave":
            self._use_door(intention.target, retry=True)
            return
        if kind == "reclaim" and not intention.target:
            if intention.where is not None:
                self._step(intention.where)
            return
        if intention.where is None:
            return
        if _horiz(self.model.position, intention.where) > _ACT_RANGE.get(kind, 8.0):
            self._step(intention.where)
            return
        if kind in ("task_talk", "hail", "talk", "fetch", "search", "hand_in") and not self._can_see(intention.where):
            self._step(intention.where)
            return
        if kind in ("task_talk", "hail"):
            self._hail(intention.target, intention.name)
        elif kind == "talk":
            self._say_keyword(intention.target, intention.name, intention.text)
        elif kind in ("task_kill", "fight"):
            self._attack(intention.target, force=kind == "task_kill")
        elif kind == "reclaim":
            self._loot(intention.target, take_all=True)
        elif kind == "train":
            self._train(intention.target)
        elif kind == "loot":
            self._loot(intention.target)
        elif kind in ("fetch", "search"):
            self._pickup(intention.target)
        elif kind == "hand_in":
            self._hand_in(intention.target, intention.item_id)

    def _near(self, goal: tuple[float, float, float]) -> bool:
        return _horiz(self.model.position, goal) <= 4.0

    def _step(self, goal: tuple[float, float, float]) -> None:
        """One step from the server's latest coordinates toward goal."""
        here = self.model.position
        if self._near(goal):
            return
        if not self.path or _horiz(self.path[-1], goal) > 5.0:
            self.path = self.nav.path(here, goal) if self.nav is not None else [here, goal]
        while self.path and _horiz(here, self.path[0]) < 3.0:
            self.path.pop(0)
        if not self.path:
            return
        nxt = self.path[0]
        step = _move(here, nxt, STEP)
        for door in doors_along(self.model.doors.values(), here, step, set(self.quests.exits)):
            self._click_door(door.door_id)
        self.model.predict(*step)
        spawn_id = self.model.self_id
        self.client.send(
            "OP_ClientUpdate",
            client_position(spawn_id, self.model.next_sequence(), step[0], step[1], step[2]),
        )

    def _hail(self, spawn_id: int, name: str) -> None:
        self._target(spawn_id)
        before = len(self.client.messages)
        self.client.say("hail")
        self.client.pump(0.3)
        if len(self.client.messages) > before:
            self.score.hails += 1
        self._remember(name, "say", "hail")

    def _say_keyword(self, spawn_id: int, name: str, keyword: str) -> None:
        if not keyword:
            return
        self._target(spawn_id)
        before = len(self.client.messages)
        self.client.say(keyword)
        self.client.pump(0.3)
        self._remember(name, "say", keyword.lower())
        if len(self.client.messages) > before:
            self.score.keywords += 1

    def _attack(self, spawn_id: int, force: bool) -> None:
        spawn = self.model.spawns.get(spawn_id)
        if spawn is None:
            return
        faction = self.model.faction.get(spawn_id)
        if faction is None:
            self.client.send("OP_Consider", struct.pack("<IIIIIIBBBB", self.model.self_id, spawn_id, 0, 0, 0, 0, 0, 0, 0, 0))
            self.client.pump(0.2)
            faction = self.model.faction.get(spawn_id)
        if not force and faction not in (8, 9):
            return
        self._target(spawn_id)
        self.attacked.add(spawn_id)
        self.client.command("attack")
        self.client.send("OP_AutoAttack", b"\x01\x00\x00\x00")

    def _loot(self, spawn_id: int, take_all: bool = False) -> None:
        before = stack_totals(self.inventory.slots)
        self.inventory.clear_corpse()
        self._loot_open = 0
        self._target(spawn_id)
        self.client.send("OP_LootRequest", struct.pack("<I", spawn_id))
        self.client.pump(0.6)
        # 1 and 3 open the window. 5 means we are still too far, so the corpse stays where it is.
        if take_all and self._loot_open not in (1, 3):
            return
        wanted = self._wanted_ids()
        took = False
        seen: set[int] = set()
        # Bags come off first so the rest of the corpse has somewhere to go.
        ordered = sorted(self.inventory.corpse_slots.items(), key=lambda pair: pair[1].bag_slots == 0)
        for slot, held in ordered:
            if slot in seen:
                continue
            if not take_all and held.item_id not in wanted:
                continue
            if take_all:
                self._stow(limit=6)
                if self.inventory.cursor() is not None:
                    break
            self.client.send("OP_LootItem", struct.pack("<IIH2sI", spawn_id, self.model.self_id, slot, b"\x00\x00", 0))
            seen.add(slot)
            took = True
            self.client.pump(0.2)
        self.client.send("OP_LootComplete", b"")
        self.client.pump(0.3)
        self.inventory.clear_corpse()
        if take_all:
            expected = [held for _slot, held in ordered]
            missing = missing_entries(before, stack_totals(self.inventory.slots), expected)
            self.model.note_corpse_contents(len(expected), missing)
            if missing == 0:
                self.score.fetched += len(expected)
        elif not took:
            self.skipped_corpses.add(spawn_id)
        else:
            self.score.fetched += 1

    def _stow(self, limit: int = 1) -> None:
        """Move a bag onto a general slot, then loose items into its pockets."""
        for _ in range(limit):
            move = stow_move(self.inventory)
            if move is None:
                return
            self._move(*move)
            self.client.pump(0.15)

    def _train(self, spawn_id: int) -> None:
        skill = self._next_skill()
        if skill is None or self.model.points <= 0:
            self.model.points = 0
            self.client.send("OP_GMEndTraining", struct.pack("<II", spawn_id, self.model.self_id))
            return
        self._trained = False
        # GMSkillChange_Struct: npc id, pad, skill bank 0, pad, skill id, pad.
        self.client.send("OP_GMTrainSkill", struct.pack("<H2sH2sH2s", spawn_id & 0xFFFF, b"\x00\x00", 0, b"\x00\x00", skill, b"\x00\x00"))
        self.client.pump(0.4)
        text = " ".join(self.client.messages[-4:]).lower()
        if self._trained:
            self.model.points = max(0, self.model.points - 1)
        elif "more skilled" in text:
            self._retired_skills.add(skill)
        else:
            self._retired_skills.add(skill)

    def _next_skill(self) -> int | None:
        for _ in range(len(TRAIN_SKILLS)):
            skill = TRAIN_SKILLS[self._skill_index % len(TRAIN_SKILLS)]
            self._skill_index += 1
            if skill not in self._retired_skills:
                return skill
        return None

    def _equip(self) -> None:
        protect: set[int] = set()
        for script in self.quests.scripts.values():
            for need in script.needs:
                protect.add(need.item_id)
        for need in _task_needs(self.tasks, self.quests, self.inventory):
            protect.add(need.item_id)
        move = equip_move(self.inventory, self.model.class_id, self.model.race_id, self.model.level or 1, protect)
        if move is not None:
            self._move(*move)

    def _pickup(self, drop_id: int) -> None:
        if self.inventory.cursor_blocks(self._wanted_ids()):
            self._clear_cursor()
            return
        before = set(self.inventory.slots)
        self.client.send("OP_ClickObject", struct.pack("<II", drop_id, self.model.self_id))
        self.client.pump(0.5)
        if set(self.inventory.slots) == before:
            self.skipped_ground.add(drop_id)
        else:
            self.score.fetched += 1

    def _hand_in(self, spawn_id: int, item_id: int) -> None:
        slot = self.inventory.slot_of(item_id)
        if slot is None:
            return
        if slot != CURSOR:
            self._move(slot, CURSOR)
            self.client.pump(0.3)
        self.client.send("OP_TradeRequest", struct.pack("<II", spawn_id, self.model.self_id))
        self.client.pump(0.4)
        self._move(CURSOR, TRADE)
        self.client.send("OP_TradeAcceptClick", b"")
        self.client.pump(0.3)
        spawn = self.model.spawns.get(spawn_id)
        self._remember(spawn.name if spawn is not None else "", "handin", str(item_id))

    def _can_see(self, where: tuple[float, float, float]) -> bool:
        if self.zone_map is None:
            return True
        return self.zone_map.clear(self.model.position, where)

    def _use_door(self, door_id: int, retry: bool) -> None:
        door = self.model.doors.get(door_id)
        if door is not None and door.tried and not retry and not door.opened:
            return
        if door is not None and not self._near((door.x, door.y, door.z)):
            self._step((door.x, door.y, door.z))
            return
        self._click_door(door_id)

    def _click_door(self, door_id: int) -> None:
        door = self.model.doors.get(door_id)
        if door is not None:
            door.tried = True
        packet = bytearray(16)
        packet[0] = door_id & 0xFF
        self.client.send("OP_ClickDoor", bytes(packet))

    def _target(self, spawn_id: int) -> None:
        self.client.send("OP_TargetCommand", struct.pack("<I", spawn_id))

    def _move(self, from_slot: int, to_slot: int) -> None:
        self.client.send("OP_MoveItem", struct.pack("<III", from_slot, to_slot, 1))
        self.inventory.note_move(from_slot, to_slot)

    def _clear_cursor(self) -> None:
        held = self.inventory.cursor()
        if held is None:
            return
        if PRIMARY not in self.inventory.slots:
            self._move(CURSOR, PRIMARY)
            return
        slot = self.inventory.empty_general()
        if slot is not None:
            self._move(CURSOR, slot)

    def _form_party(self) -> None:
        command = self.party.poll()
        if not command:
            return
        self.client.command(command)
        wait = 1.0 if command == "botlist" else 3.0
        deadline = time.monotonic() + wait
        while time.monotonic() < deadline and (command == "botlist" or self.party.waiting):
            self.client.pump(0.2)
            self._party_messages()
            if command == "botlist" and time.monotonic() > deadline - 0.2:
                break

    def _party_messages(self) -> None:
        for message in self.client.messages[self._messages :]:
            self.party.push(message)
        self._messages = len(self.client.messages)

    def _remember(self, npc: str, kind: str, detail: str) -> None:
        npc_key = _key(npc)
        self.journal.record(self.model.character, self.model.zone or "", npc_key, kind, detail)
        if kind == "say":
            self.said.add((npc_key, detail))
        elif kind == "handin":
            self.handed.add((npc_key, detail))

    def _wanted_ids(self) -> set[int]:
        """Item ids still short: this zone's hand-ins, and the open task's deliver or loot list."""
        wanted: set[int] = set()
        for script in self.quests.scripts.values():
            for need in script.needs:
                if self.inventory.count(need.item_id) < need.count:
                    wanted.add(need.item_id)
        for need in _task_needs(self.tasks, self.quests, self.inventory):
            wanted.add(need.item_id)
        return wanted

    def _note_progress(self, before: dict[tuple[int, int], int]) -> None:
        for activity in self.tasks.activities:
            key = (activity.task_id, activity.activity_id)
            if activity.done > before.get(key, 0) and activity.done >= activity.goal:
                self.score.activities += 1


def _done_map(tasks: TaskBook) -> dict[tuple[int, int], int]:
    return {(activity.task_id, activity.activity_id): activity.done for activity in tasks.activities}


def _move(here, goal, step: float) -> tuple[float, float, float]:
    dx, dy = goal[0] - here[0], goal[1] - here[1]
    dist = _horiz(here, goal)
    if dist <= step:
        return goal
    scale = step / dist
    return (here[0] + dx * scale, here[1] + dy * scale, goal[2])


def _horiz(a, b) -> float:
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5


def _key(name: str) -> str:
    return " ".join(name.lower().replace("_", " ").replace("#", " ").split())


_WATCHED = (
    "OP_NewZone",
    "OP_ZoneSpawns",
    "OP_NewSpawn",
    "OP_DeleteSpawn",
    "OP_SpawnDoor",
    "OP_GroundSpawn",
    "OP_ClickObject",
    "OP_ClientUpdate",
    "OP_RequestClientZoneChange",
    "OP_ZoneChange",
    "OP_BecomeCorpse",
    "OP_Death",
    "OP_PlayerProfile",
    "OP_LevelUpdate",
    "OP_SkillUpdate",
    "OP_MoneyOnCorpse",
    "OP_Consider",
    "OP_MoveDoor",
    "OP_ItemPacket",
    "OP_TaskSelectWindow",
    "OP_TaskActivity",
    "OP_TaskActivityComplete",
)


def main() -> None:
    run_spec(AgentSpec.from_environ())


def run_spec(spec: AgentSpec) -> Score:
    """Log one character in with its own race, class, and quest journal."""
    holder: dict[str, Agent] = {}

    def before(client: Client) -> None:
        agent = Agent(client)
        agent.attach()
        holder["agent"] = agent

    client = connect(
        user=spec.user,
        password=spec.password,
        character=spec.character,
        before_zone=before,
        sheet=spec.sheet(),
        bot_prefix=spec.bot_prefix,
        journal_path=spec.journal_path,
    )
    try:
        return holder["agent"].run()
    finally:
        client.close()
