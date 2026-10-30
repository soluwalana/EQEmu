"""Band 0. Move the scroll, write it, load the gem. The learned line finishes it."""
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eqclient3.loop import Loop
    from eqclient3.world import World

from eqclient3.action import Action
from eqclient3.actions.support import CURSOR_SLOT, message_text
from eqclient3.structs import OP_MemorizeSpell, OP_MoveItem, OP_ReadBook

class ScribeSpell(Action):

    def __init__(self, spell_id: int, slot: int) -> None:
        super().__init__()
        self.priority = 0
        self.durable = True
        self.spell_id = int(spell_id)
        self.slot = int(slot)
        self.wrote = False

    def opcodes(self) -> tuple[str, ...]:
        return ('OP_MemorizeSpell', 'OP_SpecialMesg')

    def suspend(self) -> None:
        self.suspended = True

    def step(self, loop: Loop, world: World) -> None:
        if self.waiting_for('SCRIBE') and (not self.messages):
            return
        if self._learned(world):
            self.unwait('SCRIBE')
            self.complete = True
            return
        self.suspended = False
        scroll = _scroll_id(world, self.spell_id, self.slot)
        if scroll and world.cursor != scroll:
            loop.send('OP_MoveItem', OP_MoveItem(int(self.slot), CURSOR_SLOT).serialize())
            return
        if self.spell_id in set(world.tomes or ()):
            loop.send('OP_ReadBook', OP_ReadBook(int(self.spell_id)).serialize())
        else:
            loop.send('OP_MemorizeSpell', OP_MemorizeSpell(int(self.slot), int(self.spell_id), 0).serialize())
        gem = int(world.gem_slot or 0)
        loop.send('OP_MemorizeSpell', OP_MemorizeSpell(gem, int(self.spell_id), 1).serialize())
        self.wrote = True
        self.wait('SCRIBE')

    def _learned(self, world: World) -> bool:
        name = _spell_name(world, self.spell_id)
        learned = lambda message: _learned_line(message_text(message), name)
        if self.consume('OP_SpecialMesg', learned):
            return True
        memo = self.consume('OP_MemorizeSpell')
        if memo is not None and self.spell_id in set((world.spells or {}).values()):
            return True
        return False

def _scroll_id(world: World, spell_id: int, slot: int) -> int:
    scrolls = world.scrolls or {}
    if spell_id in scrolls:
        return int(scrolls[spell_id])
    item = (world.bags or {}).get(slot)
    return int(item) if item else 0

def _learned_line(text: str, name: str) -> bool:
    lowered = (text or '').lower()
    if name and f'you have learned {name.lower()}!' in lowered:
        return True
    return 'you have learned' in lowered and (not name or name.lower() in lowered)

def _spell_name(world: World, spell_id: int) -> str:
    names = world.spell_names or {}
    info = (world.spell_info or {}).get(spell_id)
    if spell_id in names:
        return str(names[spell_id])
    if info is not None and info.name:
        return str(info.name)
    return ''
