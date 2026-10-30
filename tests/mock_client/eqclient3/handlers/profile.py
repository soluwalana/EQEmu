"""Profile, one skill, food and water, coin, mana, and the spell book."""

from __future__ import annotations

from typing import Protocol, runtime_checkable

from eqclient3.actions.field import Field
from eqclient3.handlers.common import DRINK_TYPE, FOOD_TYPE, FORAGE_SKILL, enqueue_once
from eqclient3.structs import (
    EQStruct,
    OP_ManaChange,
    OP_MemorizeSpell,
    OP_MoneyUpdate,
    OP_PlayerProfile,
    OP_SkillUpdate,
    OP_Stamina,
)
from eqclient3.handler import Handler

HALF = 64


class ProfileHandler(Handler):
    opcodes = (
        "OP_PlayerProfile",
        "OP_SkillUpdate",
        "OP_Stamina",
        "OP_MoneyUpdate",
        "OP_ManaChange",
        "OP_MemorizeSpell",
    )

    def on(self, opcode: str, payload: EQStruct) -> None:
        del opcode
        if isinstance(payload, OP_PlayerProfile):
            self.profile(payload)
        elif isinstance(payload, OP_SkillUpdate):
            self.skill(payload)
        elif isinstance(payload, OP_Stamina):
            self.stamina(payload)
        elif isinstance(payload, OP_MoneyUpdate):
            self.money(payload)
        elif isinstance(payload, OP_ManaChange):
            self.mana(payload)
        elif isinstance(payload, OP_MemorizeSpell):
            self.memorize(payload)

    def profile(self, played: OP_PlayerProfile) -> None:
        self.apply_played(played)
        if played.spell_book:
            self.world.spell_book = dict(played.spell_book)
        if played.gems:
            self.world.gems = dict(played.gems)

    def apply_played(self, played: OP_PlayerProfile) -> None:
        world = self.world
        if played.name:
            world.name = played.name
        if played.race:
            world.race = played.race
        if played.class_id:
            world.class_id = played.class_id
        world.gender = played.gender
        if played.level:
            world.level = played.level
        world.deity = played.deity
        if played.home_zone_id:
            world.home_zone_id = played.home_zone_id
        if played.points:
            world.points = played.points
        if played.hp:
            world.hp = played.hp
        if played.mana:
            world.mana = played.mana
        world.strength = played.strength
        world.stamina = played.stamina
        world.agility = played.agility
        world.dexterity = played.dexterity
        world.wisdom = played.wisdom
        world.intelligence = played.intelligence
        world.charisma = played.charisma
        if played.skills is not None:
            world.skills = played.skills
        if played.coin_known:
            self.set_coin(played.platinum, played.gold, played.silver, played.copper)

    def skill(self, row: OP_SkillUpdate) -> None:
        self.world.skills[row.skill_id] = row.value

    def stamina(self, row: OP_Stamina) -> None:
        food, water = row.food, row.water
        world = self.world
        world.food = food
        world.water = water
        food_slot = self.slot_of_type(FOOD_TYPE)
        drink_slot = self.slot_of_type(DRINK_TYPE)
        if 0 < food < HALF and food_slot is not None:
            enqueue_once(self.loop, world, Field("eat", food_slot), "field:eat")
        elif 0 < water < HALF and drink_slot is not None:
            enqueue_once(self.loop, world, Field("eat", drink_slot), "field:eat")
        elif _hungry(food) and food_slot is None and self.forage_known():
            enqueue_once(self.loop, world, Field("forage"), "field:forage")

    def forage_known(self) -> bool:
        skills = self.world.skills
        if not isinstance(skills, dict) or FORAGE_SKILL not in skills:
            return False
        return skills[FORAGE_SKILL] > 0

    def slot_of_type(self, item_type: int) -> int | None:
        world = self.world
        items = world.items or {}
        bags = world.bags or {}
        for slot, item_id in bags.items():
            row = items.get(item_id)
            found = _item_type(row)
            if found == item_type:
                return slot
        return None

    def money(self, row: OP_MoneyUpdate) -> None:
        self.set_coin(row.platinum, row.gold, row.silver, row.copper)

    def set_coin(self, platinum: int, gold: int, silver: int, copper: int) -> None:
        self.world.set_coin(platinum, gold, silver, copper)

    def mana(self, row: OP_ManaChange) -> None:
        world = self.world
        world.mana = row.new_mana
        if world.mana > world.max_mana:
            world.max_mana = world.mana

    def memorize(self, row: OP_MemorizeSpell) -> None:
        world = self.world
        slot, spell_id, scribing = row.slot, row.spell_id, row.scribing
        if scribing == 1:
            gems = world.gems
            if not gems:
                gems = {}
                world.gems = gems
            gems[slot] = spell_id
            return
        if scribing == 2:
            gems = world.gems or {}
            gems.pop(slot, None)
            return
        book = world.spell_book
        if not book:
            book = {}
            world.spell_book = book
        book[slot] = spell_id


def _hungry(food: int) -> bool:
    return food == 0 or 0 < food < HALF


@runtime_checkable
class _TypedItem(Protocol):
    item_type: int


def _item_type(row: object) -> int:
    if isinstance(row, dict):
        value = row.get("item_type", -1)
        return value if isinstance(value, int) else -1
    if isinstance(row, _TypedItem):
        return row.item_type
    return -1
