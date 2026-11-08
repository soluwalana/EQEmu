# Necromancer

Steps taken from the quest graph only. **Broken** means the graph has no edge for that value or that item.

Flags with writes: `NecroPre`, `Soulwhisper`, `necro_epic`.

## 0. Prerequisites

Each list is the order you obtain that item. Later steps point here instead of repeating the chain.

### "Scythe of the Shadowed Soul" (20544)

1. Loot "Silver Disc" (20938) from "An Azarack" in `airplane`.
2. Loot "Spiroc Feathers" (20782) from "An Avenging Gazer" (NPC 71027) in `airplane`. Drop cache: 10.63% chance per kill.
3. airplane/"A Soul Carrier", on event_death_complete. Triggers `airplane/key master#signal:2`.
4. Starts timer `87`.
5. Spawns "Keeper of Souls" (71075) after `airplane/key master#timer:87`.
6. Loot "Black Silk Cape" (20783) from "Keeper of Souls".
7. airplane/"Jzil Gsix", hand "Spiroc Feathers" (20782) + "Black Silk Cape" (20783) + "Silver Disc" (20938). Gives "Cloak of Spiroc Feathers" (1278).
8. Loot "Eye of Innoruuk" (20656) from "Innoruuk" (NPC 76007) in `hateplane`. Drop cache: 40.73% chance per kill.
9. Loot "Slime Blood of Cazic-Thule" (20655) from "Dread" in `fearplane`.
10. Loot "Slime Blood of Cazic-Thule" (20655) from "Fright" in `fearplane`.
11. Loot "Slime Blood of Cazic-Thule" (20655) from "Terror" in `fearplane`.
12. Kill lakerathe/"A Failed Apprentice". Spawns "A Tortured Soul" (51144).
13. Loot "Symbol of Insanity" (20648) from "A Tortured Soul".
14. timorous/"Drendico Metalbones", hand "Symbol of Insanity" (20648). Gives "Journal of Drendico" (18086).
15. timorous/"Drendico Metalbones", hand "Cloak of Spiroc Feathers" (1278) + "Journal of Drendico" (18086) + "Slime Blood of Cazic-Thule" (20655) + "Eye of Innoruuk" (20656). Gives "Prepared Reagent Box" (20653).
16. lakerathe/"Kazen Fecae", hand "Prepared Reagent Box" (20653). Gives "Tome of Instruction" (18087).
17. airplane/"Gkzzallk", hand "Tome of Instruction" (18087). Gives "Gkzzallk in a Box" (20652).
18. lakerathe/"Kazen Fecae", hand "Gkzzallk in a Box" (20652). Gives "Scythe of the Shadowed Soul" (20544).

### "Orb of Deathspeaking" (15784)

1. Loot "Silver Disc" (20938) from "An Azarack" in `airplane`.
2. Loot "Spiroc Feathers" (20782) from "An Avenging Gazer" (NPC 71027) in `airplane`. Drop cache: 10.63% chance per kill.
3. airplane/"A Soul Carrier", on event_death_complete. Triggers `airplane/key master#signal:2`.
4. Starts timer `87`.
5. Spawns "Keeper of Souls" (71075) after `airplane/key master#timer:87`.
6. Loot "Black Silk Cape" (20783) from "Keeper of Souls".
7. airplane/"Jzil Gsix", hand "Spiroc Feathers" (20782) + "Black Silk Cape" (20783) + "Silver Disc" (20938). Gives "Cloak of Spiroc Feathers" (1278).
8. Loot "Eye of Innoruuk" (20656) from "Innoruuk" (NPC 76007) in `hateplane`. Drop cache: 40.73% chance per kill.
9. Loot "Slime Blood of Cazic-Thule" (20655) from "Dread" in `fearplane`.
10. Loot "Slime Blood of Cazic-Thule" (20655) from "Fright" in `fearplane`.
11. Loot "Slime Blood of Cazic-Thule" (20655) from "Terror" in `fearplane`.
12. Kill lakerathe/"A Failed Apprentice". Spawns "A Tortured Soul" (51144).
13. Loot "Symbol of Insanity" (20648) from "A Tortured Soul".
14. timorous/"Drendico Metalbones", hand "Symbol of Insanity" (20648). Gives "Journal of Drendico" (18086).
15. timorous/"Drendico Metalbones", hand "Cloak of Spiroc Feathers" (1278) + "Journal of Drendico" (18086) + "Slime Blood of Cazic-Thule" (20655) + "Eye of Innoruuk" (20656). Gives "Prepared Reagent Box" (20653).
16. lakerathe/"Kazen Fecae", hand "Prepared Reagent Box" (20653). Gives "Tome of Instruction" (18087).
17. airplane/"Gkzzallk", hand "Tome of Instruction" (18087). Gives "Gkzzallk in a Box" (20652).
18. lakerathe/"Kazen Fecae", hand "Gkzzallk in a Box" (20652). Gives "Scythe of the Shadowed Soul" (20544).
19. lakerathe/"Kazen Fecae", say "Hail". Requires `Soulwhisper` unset. Gives "Note to Biddliss" (9831).
20. steamfont/"Biddliss Sperandu", hand "Note to Biddliss" (9831). Gives "Gleaming Ore Satchel" (9579).
21. Loot "Old Waterlogged Lute" (59025) from "A Shady Treasure Sorter" in `dulak`.
22. Hand "Old Waterlogged Lute" (59025) to torgiran/"A Crazed Miner". Spawns "a crazed miner (KOS)" (226021). Loot "Gleaming Zraxthril Ore" (54006) from "a crazed miner (KOS)".
23. 1 alternative loot source(s) also yield Gleaming Zraxthril Ore (54006).
24. Combine in "Gleaming Ore Satchel" (9579): "Gleaming Zraxthril Ore" (54006). Produces "Sealed Ore Satchel" (27982). The combine does not fail. The recipe must be learned first.
25. steamfont/"Biddliss Sperandu", hand "Sealed Ore Satchel" (27982). Gives "Biddliss's Research Tools" (21799).
26. lakerathe/"Kazen Fecae", hand "Biddliss's Research Tools" (21799). Gives "Drawing of Rune" (22691).
27. poknowledge/"Ruandia", hand "Drawing of Rune" (22691). Gives "Ruandia's Instructions" (10138).
28. poknowledge/"Tebarin", hand "Ruandia's Instructions" (10138). Gives "Intricately Carved Box" (16689).
29. Spawns "An Earthern Crusader" (218027) in `poeartha` on event_combat.
30. Loot "Ball of Elemental Clay" (21720) from "An Earthern Crusader".
31. 1 alternative loot source(s) also yield Ball of Elemental Clay (21720).
32. Combine in "Intricately Carved Box" (16689): "Ball of Elemental Clay" (21720). Produces "Sealed Intricately Carved Box" (27282). The combine does not fail. The recipe must be learned first.
33. poknowledge/"Tebarin", hand "Sealed Intricately Carved Box" (27282). Gives "Strange Smelling Oil" (16799).
34. Loot "Ancient Tome of Lost Lore" (62285) from "An Old Gargoyle" in `hole`.
35. Combine in "Intricately Carved Box" (16689): "Strange Smelling Oil" (16799), "Ancient Tome of Lost Lore" (62285). Produces "Protected Tome" (16759). The combine does not fail. The recipe must be learned first.
36. poknowledge/"Tebarin", hand "Protected Tome" (16759). Gives "Brightly Glowing Tome" (9834).
37. poknowledge/"Tebarin", hand "Brightly Glowing Tome" (9834). Gives "Rune Covered Insert" (11406).
38. Loot "Gnarled Wood" (12081) from "A Gnarled Treant" in `ponightmare`.
39. Loot "Elaborate Hinge" (15835) from "A Scrap Collector" in `poinnovation`.
40. Combine in Forge (17): "Rune Covered Insert" (11406), "Gnarled Wood" (12081), "Elaborate Hinge" (15835). Produces "Glowing Box of Protection" (13620). Requires Blacksmithing 100. The combine does not fail. The recipe must be learned first.
41. poknowledge/"Tebarin", hand "Glowing Box of Protection" (13620). Gives "Paladin Headhunting Satchel" (11517).
42. Loot "Sir Gregon's Head" (11430) from "Sir Gregon Sulltor" in `eastkarana`.
43. Loot "Sir Gerwin's Head" (14344) from "Sir Gerwin Thunderblade" in `northkarana`.
44. Loot "Sir Telian's Head" (22892) from "Sir Telian Mottsworth" in `southkarana`.
45. Loot "Sir Arlindo's Head" (26896) from "Sir Arlindo Goldheart" in `qey2hh1`.
46. Combine in "Paladin Headhunting Satchel" (11517): "Sir Gregon's Head" (11430), "Sir Gerwin's Head" (14344), "Sir Telian's Head" (22892), "Sir Arlindo's Head" (26896). Produces "Full Paladin Headhunting Satchel" (24630). The combine does not fail.
47. poknowledge/"Tebarin", hand "Full Paladin Headhunting Satchel" (24630). Gives "Orb of Deathspeaking" (15784).

### "Soulwhisper" (62581)

1. Loot "Silver Disc" (20938) from "An Azarack" in `airplane`.
2. Loot "Spiroc Feathers" (20782) from "An Avenging Gazer" (NPC 71027) in `airplane`. Drop cache: 10.63% chance per kill.
3. airplane/"A Soul Carrier", on event_death_complete. Triggers `airplane/key master#signal:2`.
4. Starts timer `87`.
5. Spawns "Keeper of Souls" (71075) after `airplane/key master#timer:87`.
6. Loot "Black Silk Cape" (20783) from "Keeper of Souls".
7. airplane/"Jzil Gsix", hand "Spiroc Feathers" (20782) + "Black Silk Cape" (20783) + "Silver Disc" (20938). Gives "Cloak of Spiroc Feathers" (1278).
8. Loot "Eye of Innoruuk" (20656) from "Innoruuk" (NPC 76007) in `hateplane`. Drop cache: 40.73% chance per kill.
9. Loot "Slime Blood of Cazic-Thule" (20655) from "Dread" in `fearplane`.
10. Loot "Slime Blood of Cazic-Thule" (20655) from "Fright" in `fearplane`.
11. Loot "Slime Blood of Cazic-Thule" (20655) from "Terror" in `fearplane`.
12. Kill lakerathe/"A Failed Apprentice". Spawns "A Tortured Soul" (51144).
13. Loot "Symbol of Insanity" (20648) from "A Tortured Soul".
14. timorous/"Drendico Metalbones", hand "Symbol of Insanity" (20648). Gives "Journal of Drendico" (18086).
15. timorous/"Drendico Metalbones", hand "Cloak of Spiroc Feathers" (1278) + "Journal of Drendico" (18086) + "Slime Blood of Cazic-Thule" (20655) + "Eye of Innoruuk" (20656). Gives "Prepared Reagent Box" (20653).
16. lakerathe/"Kazen Fecae", hand "Prepared Reagent Box" (20653). Gives "Tome of Instruction" (18087).
17. airplane/"Gkzzallk", hand "Tome of Instruction" (18087). Gives "Gkzzallk in a Box" (20652).
18. lakerathe/"Kazen Fecae", hand "Gkzzallk in a Box" (20652). Gives "Scythe of the Shadowed Soul" (20544).
19. lakerathe/"Kazen Fecae", say "Hail". Sets `Soulwhisper` to `1`.
20. lakerathe/"Kazen Fecae", say "Hail". Requires `Soulwhisper` unset. Gives "Note to Biddliss" (9831).
21. steamfont/"Biddliss Sperandu", hand "Note to Biddliss" (9831). Gives "Gleaming Ore Satchel" (9579).
22. Loot "Old Waterlogged Lute" (59025) from "A Shady Treasure Sorter" in `dulak`.
23. Hand "Old Waterlogged Lute" (59025) to torgiran/"A Crazed Miner". Spawns "a crazed miner (KOS)" (226021). Loot "Gleaming Zraxthril Ore" (54006) from "a crazed miner (KOS)".
24. 1 alternative loot source(s) also yield Gleaming Zraxthril Ore (54006).
25. Combine in "Gleaming Ore Satchel" (9579): "Gleaming Zraxthril Ore" (54006). Produces "Sealed Ore Satchel" (27982). The combine does not fail. The recipe must be learned first.
26. steamfont/"Biddliss Sperandu", hand "Sealed Ore Satchel" (27982). Gives "Biddliss's Research Tools" (21799).
27. lakerathe/"Kazen Fecae", hand "Biddliss's Research Tools" (21799). Gives "Drawing of Rune" (22691).
28. poknowledge/"Ruandia", hand "Drawing of Rune" (22691). Gives "Ruandia's Instructions" (10138).
29. poknowledge/"Tebarin", hand "Ruandia's Instructions" (10138). Gives "Intricately Carved Box" (16689).
30. Spawns "An Earthern Crusader" (218027) in `poeartha` on event_combat.
31. Loot "Ball of Elemental Clay" (21720) from "An Earthern Crusader".
32. 1 alternative loot source(s) also yield Ball of Elemental Clay (21720).
33. Combine in "Intricately Carved Box" (16689): "Ball of Elemental Clay" (21720). Produces "Sealed Intricately Carved Box" (27282). The combine does not fail. The recipe must be learned first.
34. poknowledge/"Tebarin", hand "Sealed Intricately Carved Box" (27282). Gives "Strange Smelling Oil" (16799).
35. Loot "Ancient Tome of Lost Lore" (62285) from "An Old Gargoyle" in `hole`.
36. Combine in "Intricately Carved Box" (16689): "Strange Smelling Oil" (16799), "Ancient Tome of Lost Lore" (62285). Produces "Protected Tome" (16759). The combine does not fail. The recipe must be learned first.
37. poknowledge/"Tebarin", hand "Protected Tome" (16759). Gives "Brightly Glowing Tome" (9834).
38. poknowledge/"Tebarin", hand "Brightly Glowing Tome" (9834). Gives "Rune Covered Insert" (11406).
39. Loot "Gnarled Wood" (12081) from "A Gnarled Treant" in `ponightmare`.
40. Loot "Elaborate Hinge" (15835) from "A Scrap Collector" in `poinnovation`.
41. Combine in Forge (17): "Rune Covered Insert" (11406), "Gnarled Wood" (12081), "Elaborate Hinge" (15835). Produces "Glowing Box of Protection" (13620). Requires Blacksmithing 100. The combine does not fail. The recipe must be learned first.
42. poknowledge/"Tebarin", hand "Glowing Box of Protection" (13620). Gives "Paladin Headhunting Satchel" (11517).
43. Loot "Sir Gregon's Head" (11430) from "Sir Gregon Sulltor" in `eastkarana`.
44. Loot "Sir Gerwin's Head" (14344) from "Sir Gerwin Thunderblade" in `northkarana`.
45. Loot "Sir Telian's Head" (22892) from "Sir Telian Mottsworth" in `southkarana`.
46. Loot "Sir Arlindo's Head" (26896) from "Sir Arlindo Goldheart" in `qey2hh1`.
47. Combine in "Paladin Headhunting Satchel" (11517): "Sir Gregon's Head" (11430), "Sir Gerwin's Head" (14344), "Sir Telian's Head" (22892), "Sir Arlindo's Head" (26896). Produces "Full Paladin Headhunting Satchel" (24630). The combine does not fail.
48. poknowledge/"Tebarin", hand "Full Paladin Headhunting Satchel" (24630). Gives "Orb of Deathspeaking" (15784).
49. natimbi/"Whiahdi", say "I Want The Staff". Sets `Soulwhisper` to `2`.
50. Say "Hail" to barindu/"Viarglug".
51. Spawns "Viarglug (Active)" (283156).
52. Loot "Whiahdi's Earthly Possessions" (11174) from "Viarglug (Active)".
53. natimbi/"Whiahdi", hand "Whiahdi's Earthly Possessions" (11174). Sets `Soulwhisper` to `3`.
54. natimbi/"Whiahdi", say "Power". Sets `Soulwhisper` to `4`.
55. Say "Hail" to causeway/"Tarlang".
56. Spawns "Tarlang (Active)" (303083).
57. Loot "Tarlang's Head" (55855) from "Tarlang (Active)".
58. natimbi/"Whiahdi", hand "Tarlang's Head" (55855). Requires `Soulwhisper` ==3. Requires `Soulwhisper` set. Gives "Soulwhisper" (62581).

## `NecroPre`

Values written: 1, 2.

### 1. egonis — hand 15523

Zone: `lakerathe`.

Sets `NecroPre` to `1`.

- Turn in x1: Contract of Sale (15523).
In script order:

1. Sets `NecroPre` to `1`.
2. Spawns Ronaiar Skullmoore (51155).
   - Loots Lucidem (35084).
   - Loots Versluierd Fungus (35087).
   - Loots Elaborate Binding Powder (36285).


How the items are reached:

- Contract of Sale (15523)
  - Kill qey2hh1/"A Snarling Werewolf". Spawns "Shady Bandit" (12185).
  - Loot "Contract of Sale" (15523) from "Shady Bandit".

### 2. geboron — hand 20612

Zone: `poknowledge`.

Sets `NecroPre` to `2`.

- Needs `NecroPre` ==1.
- Needs `NecroPre` set.
- Turn in x1: Piece of the Staff (20612).
In script order:

1. Sets `NecroPre` to `2`.
2. Gives Piece of the Staff (20612).


How the items are reached:

- Piece of the Staff (20612)
  - Spawns "Man-eating Freshwater Shark" (51158) in `lakerathe` on event_signal.
  - Loot "Piece of the Staff" (20612) from "Man-eating Freshwater Shark".

### Steps on `NecroPre` that do not change it

- `lakerathe` egonis, say hail needs `NecroPre` ==1.
  - Spawns Ronaiar Skullmoore (51155).
  - Loots Lucidem (35084).
  - Loots Versluierd Fungus (35087).
  - Loots Elaborate Binding Powder (36285).
- `lakerathe` kazen fecae, hand 20612 needs `NecroPre` ==2.
  - Sets `Soulwhisper` to `1`.
  - Turn in Piece of the Staff (20612).
  - Gives Note to Biddliss (9831).
  - Gives Piece of the Staff (20612).
- `poknowledge` geboron, say hail needs `NecroPre` unset.
  - Gives Note to Yuanda (15809).

## `Soulwhisper` 1.5

Values written: 1, 2, 3, 4.

### 1. kazen fecae — say hail

Zone: `lakerathe`.

> It has been a while since we have talked. You have done well in obtaining your Scythe. The time has come however for you to perform another task for me. I do...

Sets `Soulwhisper` to `1`.

- Needs `Soulwhisper` unset.
- Needs Scythe of the Shadowed Soul (20544).
- Needs `Soulwhisper` set.
In script order:

1. Sets `Soulwhisper` to `1`.
2. Gives Note to Biddliss (9831).


How the items are reached:

- Scythe of the Shadowed Soul (20544)
  - Prerequisite: "Scythe of the Shadowed Soul" (20544). See section 0.

Alternative or repeat transition to `Soulwhisper` = `1` (not an additional required stage).

### 1. kazen fecae — hand 20612

Zone: `lakerathe`.

Sets `Soulwhisper` to `1`.

- Needs `NecroPre` ==2.
- Needs `NecroPre` set.
- Turn in x1: Piece of the Staff (20612).
In script order:

1. Sets `Soulwhisper` to `1`.
2. Gives Note to Biddliss (9831).
3. Gives Piece of the Staff (20612).


How the items are reached:

- Piece of the Staff (20612)
  - Spawns "Man-eating Freshwater Shark" (51158) in `lakerathe` on event_signal.
  - Loot "Piece of the Staff" (20612) from "Man-eating Freshwater Shark".

This step also depends on `NecroPre`, shown above.

### 2. whiahdi — say i want the staff

Zone: `natimbi`.

> Yes. I did see a paladin with a staff. Before I give you any more information however. I wish for you to perform a task for me. I need you to travel to Barin...

Sets `Soulwhisper` to `2`.

- Needs `Soulwhisper` ==1.
- Needs `Soulwhisper` set.
- Needs Orb of Deathspeaking (15784).
In script order:

1. Sets `Soulwhisper` to `2`.


How the items are reached:

- Orb of Deathspeaking (15784)
  - Prerequisite: "Orb of Deathspeaking" (15784). See section 0.

### 3. whiahdi — hand 11174

Zone: `natimbi`.

Sets `Soulwhisper` to `3`.

- Needs `Soulwhisper` ==2.
- Needs `Soulwhisper` set.
- Turn in x1: Whiahdi's Earthly Possessions (11174).
In script order:

1. Sets `Soulwhisper` to `3`.


How the items are reached:

- Whiahdi's Earthly Possessions (11174)
  - Say "Hail" to barindu/"Viarglug".
  - Spawns "Viarglug (Active)" (283156).
  - Loot "Whiahdi's Earthly Possessions" (11174) from "Viarglug (Active)".

### 4. whiahdi — say power

Zone: `natimbi`.

> I have come to know many spirits from other realms. They speak of a being known as Tarlang who resides in the Realm of Discord in a area known as the Nobles ...

Sets `Soulwhisper` to `4`.

- Needs `Soulwhisper` ==3.
- Needs `Soulwhisper` set.
- Needs Orb of Deathspeaking (15784).
In script order:

1. Sets `Soulwhisper` to `4`.


How the items are reached:

- Orb of Deathspeaking (15784)
  - Prerequisite: "Orb of Deathspeaking" (15784). See section 0.

Alternative or repeat transition to `Soulwhisper` = `3` (not an additional required stage).

### 3. tarlang — say hail

Zone: `causeway`.

> You dare speak to me? I do not talk to lesser creatures. Prepare for death!

Sets `Soulwhisper` to `3`.

- Needs `Soulwhisper` ==4.
- Needs `Soulwhisper` set.
In script order:

1. Sets `Soulwhisper` to `3`.
2. Spawns Tarlang (Active) (303083).
   - Loots Tarlang's Head (55855).
   - Loots Kyv Tongue (67584).


### Steps on `Soulwhisper` that do not change it

- `barindu` player, on loot needs `Soulwhisper` ==2.
  - Sets `nec_epic_barindu` to `1`.
  - Spawns a chest (283157).
  - Loots Mud Covered Shoulder Pads (71006).
  - Loots Dented Steel Face Guard (71013).
  - Loots Hollowed Bone Plated Mask (71014).
  - Loots Ragged Ruby Veil (71015).
  - Loots Rugged Iron Battle Mask (71016).
  - Loots Slender White Silk Cape (71018).
  - Loots Gleaming Crystal Band (71047).
  - Loots Shattered Bone Stud (71048).
  - Loots Aged Hoop of Battle (71049).
  - Loots Muramite Plate Gloves of War (71055).
  - Loots Muramite Chain Armguards of Battle (71059).
  - Loots Muramite Chain Boots of Battle (71061).
  - Loots Muramite Leather Band of Conflict (71063).
  - Loots Muramite Leather Sleeves of Conflict (71064).
  - Loots Muramite Leather Wraps of Conflict (71065).
  - Loots Muramite Silk Sleeves of Contention (71069).
  - Loots Muramite Silk Gloves of Contention (71070).
- `barindu` taiandao, say muramite killed whiahdi needs `Soulwhisper` set.
  - Spawns Viarglug (Passive) (283158).
- `barindu` viarglug, say hail needs `Soulwhisper` ==2.
  - Spawns Viarglug (Active) (283156).
  - Loots Whiahdi's Earthly Possessions (11174).
  - Loots Mastruq Tongue (67587).
- `causeway` player, on loot needs `Soulwhisper` ==3.
  - Sets `mage_epic_causeway` to `1`.
  - Spawns a chest (Epic 1.5) (283157).
  - Sets `nec_epic_causeway` to `1`.
  - Sets `bard20_chest` to `1`.
  - Spawns a chest (epic 2.0) (893).
  - Sets `warr_chest_causeway` to `1`.
  - Sets `ber_chest_causeway` to `1`.
  - Sets `ench_chest_causeway` to `1`.
  - Loots Mud Covered Shoulder Pads (71006).
  - Loots Dented Steel Face Guard (71013).
  - Loots Hollowed Bone Plated Mask (71014).
  - Loots Ragged Ruby Veil (71015).
  - Loots Rugged Iron Battle Mask (71016).
  - Loots Slender White Silk Cape (71018).
  - Loots Gleaming Crystal Band (71047).
  - Loots Shattered Bone Stud (71048).
  - Loots Aged Hoop of Battle (71049).
  - Loots Muramite Plate Gloves of War (71055).
  - Loots Muramite Chain Armguards of Battle (71059).
  - Loots Muramite Chain Boots of Battle (71061).
  - Loots Muramite Leather Band of Conflict (71063).
  - Loots Muramite Leather Sleeves of Conflict (71064).
  - Loots Muramite Leather Wraps of Conflict (71065).
  - Loots Muramite Silk Sleeves of Contention (71069).
  - Loots Muramite Silk Gloves of Contention (71070).
  - Loots Glyphed Helm of Conflict (71073).
  - Loots Glyphed Vambraces of Conflict (71074).
  - Loots Glyphed Gauntlets of Conflict (71075).
  - Loots Glyphed Boots of Conflict (71076).
  - Loots Glyphed Bracer of Conflict (71077).
  - Loots Lightning Blackened Chain Coif (71078).
  - Loots Lightning Blackened Chain Vambraces (71079).
  - Loots Lightning Blackened Chain Gloves (71080).
  - Loots Lightning Blackened Chain Boots (71081).
  - Loots Lightning Blackened Chain Bracer (71082).
  - Loots Chaos-Imbued Leather Skullcap (71083).
  - Loots Chaos-Imbued Leather Sleeves (71084).
  - Loots Chaos-Imbued Leather Gloves (71085).
  - Loots Chaos-Imbued Leather Boots (71086).
  - Loots Chaos-Imbued Leather Bracer (71087).
  - Loots Discordant Cap of Betrayal (71088).
  - Loots Discordant Sleeves of Betrayal (71089).
  - Loots Discordant Gloves of Betrayal (71090).
  - Loots Discordant Sandals of Betrayal (71091).
  - Loots Discordant Bracer of Betrayal (71092).
  - Loots Glyphed Breastplate of Conflict (71093).
  - Loots Glyphed Greaves of Conflict (71094).
  - Loots Lightning Blackened Chain Links (71095).
  - Loots Lightning Blackened Chain Greaves (71096).
  - Loots Chaos-Imbued Leather Tunic (71097).
  - Loots Chaos-Imbued Leather Leggings (71098).
  - Loots Discordant Robe of Betrayal (71099).
  - Loots Discordant Leggings of Betrayal (71100).
  - Loots Razor-Edged Shield of War (71101).
  - Loots Cracked Shield of Discipline (71102).
  - Loots Chipped Talisman of Peace (71103).
  - Loots Blood-Soaked Champions Scroll (71104).
  - Loots Pitted Shoulderpads of Stone (71105).
  - Loots Mask of Reckless Flame (71106).
  - Loots Cloak of the Corrupted Curate (71107).
  - Loots Belt of Twisted Iron (71108).
  - Loots Mask of Dark Horror (71109).
  - Loots Black Web Mantle (71110).
  - Loots Herb-Wrapped Silk Sash (71111).
  - Loots Dragorn Scale Cloak (71112).
  - Loots Fused Bone Collar (71113).
  - Loots Pauldrons of the Fallen Crusader (71114).
  - Loots Visor of Distorted Vision (71115).
  - Loots Shadowed Amulet of Anarchy (71116).
  - Loots Fractured Champion's Ring (71117).
  - Loots Adorned Earring of Hope (71118).
  - Loots Polished Earring of Animosity (71119).
  - Loots Ring of Black Flame (71120).
- `natimbi` whiahdi, hand 55855 needs `Soulwhisper` ==3.
  - Turn in Tarlang's Head (55855).
  - Gives Soulwhisper (62581).

## `necro_epic` 2.0

Values written: 5, 6.

### 5. whiahdi — say locate the paladin

Zone: `natimbi`.

> I fear for you should you seek the staff, but I promised to help you. I can still hear the staff

Sets `necro_epic` to `5`.

- Needs Soulwhisper (62581).
In script order:

1. Sets `necro_epic` to `5`.


How the items are reached:

- Soulwhisper (62581)
  - Prerequisite: "Soulwhisper" (62581). See section 0.

### 6. whiahdi — hand 47100+55932+55940+62581

Zone: `natimbi`.

Sets `necro_epic` to `6`.

- Turn in x1: Staff Piece Number Two (55940).
- Turn in x1: Staff Piece Number Three (55932).
- Turn in x1: Globe of Discordant Energy (47100).
- Turn in x1: Soulwhisper (62581).
In script order:

1. Sets `necro_epic` to `6`.
2. Gives Deathwhisper (64067).


How the items are reached:

- Staff Piece Number Two (55940)
  - Say "Sanait Sanaiij Tsulum" to dranik/"Discord Fluctuation".
  - Spawns "Arl" (336242).
  - Loot "Staff Piece Number Two" (55940) from "Arl".
- Staff Piece Number Three (55932)
  - Say "Sanait Sanaiij Tsulum" to dranik/"Discord Fluctuation".
  - Spawns "Gor" (336243).
  - Loot "Staff Piece Number Three" (55932) from "Gor".
- Globe of Discordant Energy (47100)
  - Say "Check Lorb" to anguish/"Zone Status".
  - Spawns "Orb of Discordant Energy" (317087).
  - Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy".
  - 4 alternative loot source(s) also yield Globe of Discordant Energy (47100).
- Soulwhisper (62581)
  - Prerequisite: "Soulwhisper" (62581). See section 0.

### Steps on `necro_epic` that do not change it

- `dranik` discord fluctuation, say sanait sanaiij tsulum needs `necro_epic` ==5.
  - Spawns rag (336244).
  - Spawns gor (336243).
  - Spawns arl (336242).
  - Loots Staff Piece Number Three (55932).
  - Loots Staff Piece Number Two (55940).
- `dranik` player, on loot needs `necro_epic` ==5.
  - Sets `warrior_epic_dranik` to `1`.
  - Spawns a chest (Epic 1.5) (283157).
  - Sets `beast_epic_dran` to `1`.
  - Sets `druid_chest_dranik` to `1`.
  - Sets `shaman_chest_dranik` to `1`.
  - Spawns a chest (Epic 2.0) (893).
  - Sets `nec_chest_dranik` to `1`.
  - Sets `sk_chest_dranik` to `1`.
  - Loots Mud Covered Shoulder Pads (71006).
  - Loots Dented Steel Face Guard (71013).
  - Loots Hollowed Bone Plated Mask (71014).
  - Loots Ragged Ruby Veil (71015).
  - Loots Rugged Iron Battle Mask (71016).
  - Loots Slender White Silk Cape (71018).
  - Loots Gleaming Crystal Band (71047).
  - Loots Shattered Bone Stud (71048).
  - Loots Aged Hoop of Battle (71049).
  - Loots Muramite Plate Gloves of War (71055).
  - Loots Muramite Chain Armguards of Battle (71059).
  - Loots Muramite Chain Boots of Battle (71061).
  - Loots Muramite Leather Band of Conflict (71063).
  - Loots Muramite Leather Sleeves of Conflict (71064).
  - Loots Muramite Leather Wraps of Conflict (71065).
  - Loots Muramite Silk Sleeves of Contention (71069).
  - Loots Muramite Silk Gloves of Contention (71070).
  - Loots Glyphed Helm of Conflict (71073).
  - Loots Glyphed Vambraces of Conflict (71074).
  - Loots Glyphed Gauntlets of Conflict (71075).
  - Loots Glyphed Boots of Conflict (71076).
  - Loots Glyphed Bracer of Conflict (71077).
  - Loots Lightning Blackened Chain Coif (71078).
  - Loots Lightning Blackened Chain Vambraces (71079).
  - Loots Lightning Blackened Chain Gloves (71080).
  - Loots Lightning Blackened Chain Boots (71081).
  - Loots Lightning Blackened Chain Bracer (71082).
  - Loots Chaos-Imbued Leather Skullcap (71083).
  - Loots Chaos-Imbued Leather Sleeves (71084).
  - Loots Chaos-Imbued Leather Gloves (71085).
  - Loots Chaos-Imbued Leather Boots (71086).
  - Loots Chaos-Imbued Leather Bracer (71087).
  - Loots Discordant Cap of Betrayal (71088).
  - Loots Discordant Sleeves of Betrayal (71089).
  - Loots Discordant Gloves of Betrayal (71090).
  - Loots Discordant Sandals of Betrayal (71091).
  - Loots Discordant Bracer of Betrayal (71092).
  - Loots Glyphed Breastplate of Conflict (71093).
  - Loots Glyphed Greaves of Conflict (71094).
  - Loots Lightning Blackened Chain Links (71095).
  - Loots Lightning Blackened Chain Greaves (71096).
  - Loots Chaos-Imbued Leather Tunic (71097).
  - Loots Chaos-Imbued Leather Leggings (71098).
  - Loots Discordant Robe of Betrayal (71099).
  - Loots Discordant Leggings of Betrayal (71100).
  - Loots Razor-Edged Shield of War (71101).
  - Loots Cracked Shield of Discipline (71102).
  - Loots Chipped Talisman of Peace (71103).
  - Loots Blood-Soaked Champions Scroll (71104).
  - Loots Pitted Shoulderpads of Stone (71105).
  - Loots Mask of Reckless Flame (71106).
  - Loots Cloak of the Corrupted Curate (71107).
  - Loots Belt of Twisted Iron (71108).
  - Loots Mask of Dark Horror (71109).
  - Loots Black Web Mantle (71110).
  - Loots Herb-Wrapped Silk Sash (71111).
  - Loots Dragorn Scale Cloak (71112).
  - Loots Fused Bone Collar (71113).
  - Loots Pauldrons of the Fallen Crusader (71114).
  - Loots Visor of Distorted Vision (71115).
  - Loots Shadowed Amulet of Anarchy (71116).
  - Loots Fractured Champion's Ring (71117).
  - Loots Adorned Earring of Hope (71118).
  - Loots Polished Earring of Animosity (71119).
  - Loots Ring of Black Flame (71120).

## Other flags touched along the way

- `nec_epic_barindu` set to 1 at barindu/player.
- `nec_epic_causeway` set to 1 at causeway/player.
