# Magician — Epic Quest Walkthrough

Generated directly from quest-graph item rewards. Unresolved dependencies are marked, not inferred.

## Epic 1.0

### "Orb of Mastery" (28034)

<a id="epic-item-28034"></a>

1. Kill "Carreenu Opulaae" (NPC 309054) in `chambersf` and loot "Orb of Mastery" (28034).

## Epic 1.5

### "Staff of Elemental Essence" (19092)

<a id="epic-item-19092"></a>

1. Loot "Ice Burrower Meat" (19022) from "an ice burrower" (NPC 120010) in `westwastes`. Drop cache: 31.0425% chance per kill.
2. cobaltscar/"High Priest Margle", hand "Ice Burrower Meat" (19022).
    - event_trade NPC say: Tiknonmanin awaits your challenge.
      - Event guard: `(qglobals["mage_epic_water1"] == "1" and item_lib.check_turn_in(e.trade, {item1 = 19022, item2 = 19022, item3 = 19022, item4 = 19022}))`
3. Spawns "Tiknonmanin" (npc:117094) after the hand-in.
4. Kill "Tiknonmanin" (NPC 117094) in `cobaltscar` and loot "Elemental Essence of Water" (19086).
5. Spawns "Elemental Essence of Fire" (npc:214127) via `potactics/gnaap guinders#event_waypoint_arrive`.
6. Kill "Elemental Essence of Fire" (NPC 214127) in `potactics` and loot "Elemental Essence of Fire" (16807).
7. Spawns "Elemental Essence of Air" (npc:303100) via `causeway/player#enter`.
8. Kill "Elemental Essence of Air" (NPC 303100) in `causeway` and loot "Elemental Essence of Air" (16773).
9. Spawns "Elemental Essence of Earth" (npc:169127) via `letalis/player#enter`.
10. Kill "Elemental Essence of Earth" (NPC 169127) in `letalis` and loot "Elemental Essence of Earth" (19087).
11. poknowledge/"Bantil Io`Tuv", hand "Elemental Essence of Water" (19086) + "Elemental Essence of Fire" (16807) + "Elemental Essence of Air" (16773) + "Elemental Essence of Earth" (19087). Gives "Staff of Elemental Essence" (19092).
    - event_trade NPC say: Very well done! You have accomplished more than Magi'Kot could have ever imagined.' He then reads a passage from one of the books. The elemental essences begin to glow and take shape. You are blinded for a moment with a flash of light, when your eyes clear he presents you with an ornate staff. 'You should be honored. You have done what few have even dreamed of. In creating this staff, it has become apparent to me that there is still [further] to go.
      - Event guard: `(qglobals["mage_epic"] == "6" and item_lib.check_turn_in(e.trade, {item1=19086,item2=16807,item3=16773,item4=19087}) )`
    - event_trade NPC message: You have gained 5 ability points!

## Epic 2.0

### "Focus of Primal Elements" (19839)

<a id="epic-item-19839"></a>

**Earlier reward routes required by this graph path:** ["Staff of Elemental Essence" (19092)](#epic-item-19092).
Revisit those instructions if another copy of a consumed item is needed.

1. global/"Global Player", say "Recipe:19908". Gives "Globe of Discordant Energy" (47100).
2. poknowledge/"Bantil Io`Tuv", hand "Globe of Discordant Energy" (47100) + "Staff of Elemental Essence" (19092). Gives "Focus of Primal Elements" (19839).
    - event_trade NPC emote: pulls the four essences from his pocket.  He then wraps them around your staff with the binding.  He opens a book and reads a few words in a language that you do not recognize, the staff then begins to radiate with power.  When he hands it back to you it looks very much the same, but appears to be transformed. 'You have done the impossible, we will both be remembered in the history books.  In fact, I have already started writing of our journey together, and all the assitance that you provided me.  I will make sure you get a copy when I am finished.  That you again friend!'
      - Event guard: `(qglobals["mage_epic"] == "11" and item_lib.check_turn_in(e.trade, {item1=47100,item2=19092}) )`
    - event_trade NPC message: You have gained 10 ability points!
