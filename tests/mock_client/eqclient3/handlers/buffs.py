"""OP_Buff writes the effect. A disease, poison, or curse appends Cure when no Attack is queued."""
from __future__ import annotations

from eqclient3.actions.attack import Attack
from eqclient3.actions.cure import Cure
from eqclient3.handlers.common import has_open, is_ours, our_side, enqueue_once
from eqclient3.structs import EQStruct, OP_Buff
from eqclient3.handler import Handler

class Effect:

    def __init__(self, entity: int, spell_id: int, counters: int, fade: int) -> None:
        self.entity = entity
        self.spell_id = spell_id
        self.counters = counters
        self.fade = fade

    @property
    def affliction(self) -> str:
        if self.fade or self.counters <= 0 or self.spell_id in (0, 4294967295):
            return ''
        return 'disease'

class BuffsHandler(Handler):
    opcodes = ('OP_Buff',)

    def on(self, opcode: str, payload: EQStruct) -> None:
        del opcode
        if not isinstance(payload, OP_Buff):
            return
        effect = Effect(payload.entity_id, payload.buff.spell_id, payload.buff.counters, payload.fade)
        book = self.buffs()
        key = (effect.entity, effect.spell_id)
        if not effect.spell_id or effect.spell_id == 4294967295 or effect.fade or (effect.counters <= 0):
            book.pop(key, None)
            return
        book[key] = effect
        if not effect.affliction:
            return
        world = self.world
        loop = self.loop
        if not is_ours(world, effect.entity, loop=loop) and (not our_side(world, effect.entity)):
            return
        if has_open(loop, Attack, 'Attack'):
            return
        enqueue_once(loop, world, Cure(effect.entity, effect.spell_id), f'cure:{effect.spell_id}')

    def buffs(self) -> dict[tuple[int, int], object]:
        buffs = self.world.buffs
        if not buffs:
            buffs = {}
            self.world.buffs = buffs
        return buffs
