"""Bags, the cursor token, merchant window, and one assign pass."""

# from eqclient4.actions.cursor import Cursor
# from eqclient4.actions.sell import Sell
# from eqclient4.actions.trade import Trade
from eqclient4.handler import Handler
from eqclient4.journal import InventorySlot
from eqclient4.log import log
from eqclient4.structs import (
    ITEM_LOOT,
    ITEM_MERCHANT,
    EQStruct,
    Item,
    OP_CharInventory,
    OP_DeleteItem,
    OP_ItemPacket,
    OP_ShopDelItem,
)
from eqclient4.structs.constants import CURSOR_SLOT, TOKEN


class Held:

    def __init__(self, item_id: int, name: str, item_type: int, stack: int, scroll_effect: int = 0) -> None:
        self.item_id = item_id
        self.name = name
        self.item_type = item_type
        self.stack = stack
        self.scroll_effect = scroll_effect


def _held_slot(slot: int, item_id: int, items: dict[int, Held]) -> InventorySlot:
    held = items.get(item_id)
    if held is None:
        return InventorySlot(slot, item_id, "", 1)
    stack = held.stack if held.stack else 1
    return InventorySlot(slot, item_id, held.name, stack)


class ItemsHandler(Handler):
    opcodes = ("OP_CharInventory", "OP_ItemPacket", "OP_DeleteItem", "OP_ShopDelItem")

    def on(self, opcode: str, payload: EQStruct) -> None:
        wrote_bags = False
        match payload:
            case OP_CharInventory():
                # replaces the inventory with a new list of items
                for item in payload.items:

                    if self.remember(item):
                        wrote_bags = True
                    if item.slot == CURSOR_SLOT:
                        release_cursor(self.loop, self.world)
            case OP_ItemPacket():
                wrote_bags = self.item(payload)
            case OP_DeleteItem():
                slot = payload.from_slot
                self.bags().pop(slot, None)
                if slot == CURSOR_SLOT:
                    self.world.cursor = None
                wrote_bags = True
            case OP_ShopDelItem():
                self.shop_del(payload)
            case _:
                log.error("Unknown item opcode: %s", payload)

    def item(self, row: OP_ItemPacket) -> bool:
        item = row.item
        if item.kind == ITEM_MERCHANT:
            for action in self.open_shops():
                action.slots[item.slot] = (item.item_id, item.price)
            return False
        if item.kind == ITEM_LOOT:
            return False
        return self.remember(item)

    def remember(self, item: Item) -> bool:
        slot = item.slot
        item_id = item.item_id
        if item_id == TOKEN:
            enqueue_once(self.loop, self.world, Cursor(slot), f"cursor:{slot}")
            return False
        stack = item.stack if item.stack > 0 else 1
        self.items()[item_id] = Held(item_id, item.name, item.item_type, stack, item.scroll_effect)
        if item.kind == ITEM_LOOT:
            return False
        self.write_bag(slot, item_id)
        return True

    def write_bag(self, slot: int, item_id: int) -> None:
        if slot < 0:
            return
        world = self.world
        bags = self.bags()
        previous = bags.get(slot)
        swap = world.pending_swap
        if isinstance(swap, (tuple, list)) and len(swap) == 2 and (slot in swap):
            other = int(swap[0] if int(swap[1]) == slot else swap[1])
            bags.pop(other, None)
            world.pending_swap = None
        elif previous != item_id:
            if slot != CURSOR_SLOT and bags.get(CURSOR_SLOT) == item_id:
                bags.pop(CURSOR_SLOT, None)
                world.cursor = None
            elif slot == CURSOR_SLOT:
                for other, held in list(bags.items()):
                    if other != slot and held == item_id:
                        bags.pop(other, None)
                        break
        if slot == CURSOR_SLOT:
            world.cursor = item_id
        else:
            bags[slot] = item_id
            if world.cursor == item_id and bags.get(CURSOR_SLOT) != item_id:
                world.cursor = None

    def shop_del(self, row: OP_ShopDelItem) -> None:
        slot = row.slot
        for action in self.open_shops():
            action.slots.pop(slot, None)

    def open_shops(self) -> list[Trade | Sell]:
        """Trade and Sell actions that are still open. An empty list means the window is dropped."""
        opened: list[Trade | Sell] = []
        for action in queue_of(self.loop):
            if action.complete:
                continue
            if isinstance(action, (Trade, Sell)):
                opened.append(action)
        return opened

    def _save_inventory(self) -> None:
        journal = self.loop.journal
        who = character_name(self.loop, self.world)
        if journal is None or not who:
            return
        rows: list[InventorySlot] = []
        seen: set[int] = set()
        items: dict[int, Held] = {}
        for key, value in self.items().items():
            if isinstance(key, int) and isinstance(value, Held):
                items[key] = value
        for slot, item_id in self.bags().items():
            rows.append(_held_slot(int(slot), int(item_id), items))
            seen.add(int(slot))
        cursor = self.world.cursor
        if cursor and CURSOR_SLOT not in seen:
            rows.append(_held_slot(CURSOR_SLOT, int(cursor), items))
        journal.replace_inventory(who, rows)

    def bags(self) -> dict:
        bags = self.world.bags
        if not bags:
            bags = {}
            self.world.bags = bags
        return bags

    def items(self) -> dict:
        items = self.world.items
        if not items:
            items = {}
            self.world.items = items
        return items
