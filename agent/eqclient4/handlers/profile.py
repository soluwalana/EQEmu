"""Bags, the cursor token, merchant window, and one assign pass."""

from eqclient4.handler import Handler
from eqclient4.structs.wire import EQStruct


class ProfileHandler(Handler):
    opcodes = (
        "OP_NewSpawn",
        "OP_PlayerProfile",
        "OP_SkillUpdate",
        "OP_Stamina",
        "OP_MoneyUpdate",
        "OP_ExpUpdate",
        "OP_LevelUpdate",
        "OP_HPUpdate",
        "OP_MobHealth",
        "OP_ManaUpdate",
        "OP_EnduranceUpdate",
        "OP_ManaChange",
        "OP_Buff",
        "OP_BuffCreate",
        "OP_RespondAA",
        "OP_SendAATable",
        "OP_AAExpUpdate",
        "OP_ShopPlayerBuy",
    )

    def on(self, opcode: str, payload: EQStruct) -> None:
        char = self.world.character
        char.on(opcode, payload)
