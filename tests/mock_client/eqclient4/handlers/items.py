"""Bags, the cursor token, merchant window, and one assign pass."""

from eqclient4.handler import Handler
from eqclient4.log import log
from eqclient4.structs import (
    ITEM_MERCHANT,
    EQStruct,
    OP_CancelTrade,
    OP_CharInventory,
    OP_DeleteItem,
    OP_FinishTrade,
    OP_ItemPacket,
    OP_ShopDelItem,
    OP_ShopEndConfirm,
    OP_ShopPlayerBuy,
    OP_ShopPlayerSell,
    OP_ShopRequest,
)
from eqclient4.inventory import Merchant


class ItemsHandler(Handler):
    opcodes = (
        "OP_CharInventory",
        "OP_ItemPacket",
        "OP_DeleteItem",
        "OP_ShopDelItem",
        "OP_CancelTrade",
        "OP_FinishTrade",
        "OP_ShopEnd",
        "OP_ShopEndConfirm",
        "OP_ShopPlayerBuy",
        "OP_ShopPlayerSell",
        "OP_ShopRequest",
    )

    def on(self, opcode: str, payload: EQStruct) -> None:
        match payload:
            case OP_CharInventory() | OP_DeleteItem() | OP_CancelTrade() | OP_FinishTrade():
                event = self.world.inventory.apply(payload, True)
                if event.changed:
                    log.info(f"Inventory: {event}")

            case OP_ItemPacket() as item:
                if item.kind == ITEM_MERCHANT:
                    self.manage_shop(item)
                    return

                event = self.world.inventory.apply(payload, False)
                if event.changed:
                    log.info(f"Inventory: {event}")

            case OP_ShopRequest():
                if payload.npc_id not in self.world.active_merchants:
                    self.world.active_merchants[payload.npc_id] = Merchant(npc_id=payload.npc_id, is_open=True, items={},)
                else:
                    self.world.active_merchants[payload.npc_id].is_open = True

            case OP_ShopEndConfirm() | OP_ShopDelItem() | OP_ShopPlayerBuy() | OP_ShopPlayerSell():
                self.manage_shop(payload)

            case _:
                log.error("Unknown item opcode: %s", payload)

    def manage_shop(self, payload: EQStruct) -> None:
        active = self.world.active_merchant()
        if not active:
            log.error(f"Shop management arrived for a merchant that is not open {payload}")
            return

        match payload:
            case OP_ItemPacket():
                active.items[payload.item.slot] = payload.item

            case OP_ShopDelItem():
                active.items.pop(payload.slot, None)

            case OP_ShopPlayerBuy():
                self.world.character.deduct_coins(payload.coins)

            case OP_ShopPlayerSell():
                self.world.character.add_coins(payload.coins)

            case OP_ShopEndConfirm():
                active.is_open = False

            case _:
                log.error("Unknown shop opcode: %s", payload)
