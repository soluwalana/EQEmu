# Necromancer

Acquisition paths traced backwards from the 1.0, 1.5 and 2.0 epic rewards. Flags are dependencies, not the definition of an epic. **Broken** indicates missing graph provenance.

## Epic 1.0

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
    - Dialogue with airplane/"Gkzzallk":
      - Player: "Hail"
        - NPC say: Greetings, would you care for some tea?
        - Condition: `(e.message:findi("hail"))`
      - Player: "Tea" (link: explicit mention)
        - NPC say: The fairies should be bringing me some tea soon.
        - Condition: `(e.message:findi("tea"))`
18. lakerathe/"Kazen Fecae", hand "Gkzzallk in a Box" (20652). Gives "Scythe of the Shadowed Soul" (20544).

## Epic 1.5

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
24. Alternative: Loot "Gleaming Zraxthril Ore" (54006) from "a Broken Skull hoarder" (NPC 226210) in `torgiran`; trigger: torgiran/"The Room", on event_signal.
25. Combine in "Gleaming Ore Satchel" (9579): "Gleaming Zraxthril Ore" (54006). Produces "Sealed Ore Satchel" (27982). The combine does not fail. The recipe must be learned first.
26. steamfont/"Biddliss Sperandu", hand "Sealed Ore Satchel" (27982). Gives "Biddliss's Research Tools" (21799).
27. lakerathe/"Kazen Fecae", hand "Biddliss's Research Tools" (21799). Gives "Drawing of Rune" (22691).
28. poknowledge/"Ruandia", hand "Drawing of Rune" (22691). Gives "Ruandia's Instructions" (10138).
    - Dialogue with poknowledge/"Ruandia":
      - Player: "Hail"
        - NPC say: Hello, $name.
        - Condition: `($text=~/hail/i)`
29. poknowledge/"Tebarin", hand "Ruandia's Instructions" (10138). Gives "Intricately Carved Box" (16689).
    - Dialogue with poknowledge/"Tebarin":
      - Player: "Hail"
        - NPC say: Hello, $name.
        - Condition: `($text=~/hail/i)`
      - Player: "Special Box" (link: external event mention)
        - Prompted by `event_item`:
          - NPC say: tries to follow them into the portal but it disappears. 'This cannot be!' cries Tebarin. 'We must ensure this tome does not also fall into the hands of the paladins. The tome is our only hope of recovering the staff before the paladins destroy it. We must build a [special box] that will protect the tome. Take this rune-covered insert. You will use it to construct the box.'
          - Event guard: `(plugin::check_handin(\%itemcount, 9834 => 1))`
        - NPC say: I must have a box made to protect the tome from these thieves! In addition to the rune-covered insert I have given you, you will also need one piece of gnarled wood, and one elaborate hinge. Find those items and combine them in a forge to make the box. If you fail, Kazen and I will not be pleased. Now go!
        - Condition: `(($text=~/special box/i) && plugin::check_hasitem($client, 11406))`
30. Spawns "An Earthern Crusader" (218027) in `poeartha` on event_combat.
31. Loot "Ball of Elemental Clay" (21720) from "An Earthern Crusader".
32. Alternative: Loot "Ball of Elemental Clay" (21720) from "A Dust Devotee" (NPC 218064) in `poeartha`; trigger: poeartha/"Rings", on event death_complete:218022.
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
    - Dialogue with natimbi/"Whiahdi":
      - Player: "Locate The Paladin" (link: external event mention)
        - Prompted by `event_item`:
          - NPC say: You found my possessions! I am most greatful. The paladin you seek did walk by here some time ago. I believe he was on his way to Qinimi. He had a curious staff with him that seemed to whisper dark tidings. That staff seemed to have a very evil presence about it. I would advise you to let the paladin destroy it. I have in my possession another staff of great [power]. I can tell you about if you give up your quest for the paladin and the dark staff. However if you wish to [locate the paladin] I will help you since you did help me.
          - Event guard: `((defined($qglobals{Soulwhisper}) && ($qglobals{Soulwhisper} == 2)) && plugin::check_handin(\%itemcount, 11174 => 1))`
        - NPC say: I fear for you should you seek the staff, but I promised to help you. I can still hear the staff's dark whispers. It appears that the paladin wielding the staff has been killed and the staff returned to its master. The staff's master has broken the staff into three pieces. two of the pieces have been given to his most trusted minions, and the third piece, a globe of discordant energy, resides in a location known as Anguish, in the Realm of Discord. If you wish to somehow rebuild the staff you must find these three pieces. I can still hear the staff begging for its master. The staff tells me the only way the minions will appear is if a certain phrase is uttered at a place where the power of discord seeks to engulf all. The phrase is, 'Sanait Sanaiij Tsulum'. I don't know what it means or where this place of great discord is however. I'm sorry that's all the staff has told me. If you find all three staff pieces, return them to me along with Soulwhisper and I will see if I can reform the staff for you.
        - Condition: `(plugin::check_hasitem($client,62581))`
        - Condition: `($text=~/locate the paladin/i)`
        - Sets `necro_epic` to `5`.
      - Player: "Hail" (link: conversation sequence)
        - NPC say: You speak to the dead? Not many have that talent. What is it you want from me, mortal?
        - Condition: `(plugin::check_hasitem($client,15784))`
        - Condition: `($text=~/hail/i)`
      - Player: "I Want The Staff" (link: conversation sequence)
        - NPC say: Yes. I did see a paladin with a staff. Before I give you any more information however. I wish for you to perform a task for me. I need you to travel to Barindu and find my most precious possessions from when I was once alive. A muramite in Barindu killed me and took all I owned. If you can get my earthly possessions back, I will help you in regards to the location of the paladin. Find my brother, Taiandao in Barindu. He is still among the living, but is a slave of the vile muramites. Ask him if he knows of the muramite that killed me.
        - Condition: `(plugin::check_hasitem($client,15784))`
        - Condition: `(($text=~/i want the staff/i) && (defined($qglobals{Soulwhisper}) && ($qglobals{Soulwhisper} == 1)))`
        - Sets `Soulwhisper` to `2`.
      - Player: "Power" (link: explicit mention)
        - Prompted by player input: "Locate The Paladin"
        - NPC say: I have come to know many spirits from other realms. They speak of a being known as Tarlang who resides in the Realm of Discord in a area known as the Nobles Causeway. He has wronged many of my kin and I wish to see him pay for what he has done. If you bring me his head. I will reward you with a weapon of great power. He believes himself to be indestructible, but he is not. In fact I think you have what it takes to destroy him.
        - Condition: `(plugin::check_hasitem($client,15784))`
        - Condition: `(($text=~/power/i) && (defined($qglobals{Soulwhisper}) && ($qglobals{Soulwhisper} == 3)))`
        - Sets `Soulwhisper` to `4`.
50. Say "Hail" to barindu/"Viarglug".
51. Spawns "Viarglug (Active)" (283156).
52. Loot "Whiahdi's Earthly Possessions" (11174) from "Viarglug (Active)".
53. natimbi/"Whiahdi", hand "Whiahdi's Earthly Possessions" (11174). Sets `Soulwhisper` to `3`.
54. natimbi/"Whiahdi", say "Power". Sets `Soulwhisper` to `4`.
55. Say "Hail" to causeway/"Tarlang".
56. Spawns "Tarlang (Active)" (303083).
57. Loot "Tarlang's Head" (55855) from "Tarlang (Active)".
58. natimbi/"Whiahdi", hand "Tarlang's Head" (55855). Requires `Soulwhisper` ==3. Requires `Soulwhisper` set. Gives "Soulwhisper" (62581).

## Epic 2.0

### "Deathwhisper" (64067)

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
24. Alternative: Loot "Gleaming Zraxthril Ore" (54006) from "a Broken Skull hoarder" (NPC 226210) in `torgiran`; trigger: torgiran/"The Room", on event_signal.
25. Combine in "Gleaming Ore Satchel" (9579): "Gleaming Zraxthril Ore" (54006). Produces "Sealed Ore Satchel" (27982). The combine does not fail. The recipe must be learned first.
26. steamfont/"Biddliss Sperandu", hand "Sealed Ore Satchel" (27982). Gives "Biddliss's Research Tools" (21799).
27. lakerathe/"Kazen Fecae", hand "Biddliss's Research Tools" (21799). Gives "Drawing of Rune" (22691).
28. poknowledge/"Ruandia", hand "Drawing of Rune" (22691). Gives "Ruandia's Instructions" (10138).
29. poknowledge/"Tebarin", hand "Ruandia's Instructions" (10138). Gives "Intricately Carved Box" (16689).
30. Spawns "An Earthern Crusader" (218027) in `poeartha` on event_combat.
31. Loot "Ball of Elemental Clay" (21720) from "An Earthern Crusader".
32. Alternative: Loot "Ball of Elemental Clay" (21720) from "A Dust Devotee" (NPC 218064) in `poeartha`; trigger: poeartha/"Rings", on event death_complete:218022.
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
59. natimbi/"Whiahdi", say "Locate The Paladin". Sets `necro_epic` to `5`.
60. Say "Sanait Sanaiij Tsulum" to dranik/"Discord Fluctuation".
61. Spawns "Arl" (336242).
62. Loot "Staff Piece Number Two" (55940) from "Arl".
63. Say "Sanait Sanaiij Tsulum" to dranik/"Discord Fluctuation".
64. Spawns "Gor" (336243).
65. Loot "Staff Piece Number Three" (55932) from "Gor".
66. Say "Check Lorb" to anguish/"Zone Status".
67. Spawns "Orb of Discordant Energy" (317087).
68. Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy".
69. Alternative: Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy" (NPC 317087) in `anguish`; trigger: anguish/"Zone Status", say "Check Uorb".
70. Alternative: Loot "Globe of Discordant Energy" (47100) from "Ornate Chest" (NPC 317112) in `anguish`; trigger: anguish/"Zone Status", say "Check Amv Chest".
71. Alternative: Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy" (NPC 317087) in `anguish`; trigger: anguish/"Zone Status", on event_signal.
72. Alternative: Loot "Globe of Discordant Energy" (47100) from "Overlords Chest" (NPC 317124) in `anguish`; trigger: anguish/"Zone Status", on event_signal.
73. natimbi/"Whiahdi", hand "Globe of Discordant Energy" (47100) + "Staff Piece Number Three" (55932) + "Staff Piece Number Two" (55940) + "Soulwhisper" (62581). Gives "Deathwhisper" (64067).

## Quest-state progression

## 0. Prerequisites

Shared acquisition steps appear in the first prerequisite chain that needs them. Later sections reference that chain rather than repeating it.

### "Orb of Deathspeaking" (15784)

1. Loot "Silver Disc" (20938) from "An Azarack" in `airplane`.
2. Loot "Spiroc Feathers" (20782) from "An Avenging Gazer" (NPC 71027) in `airplane`. Drop cache: 10.63% chance per kill.
3. airplane/"A Soul Carrier", on event_death_complete. Triggers `airplane/key master#signal:2`.
4. Starts timer `87`.
5. Spawns "Keeper of Souls" (71075) after `airplane/key master#timer:87`.
6. Loot "Black Silk Cape" (20783) from "Keeper of Souls".
7. airplane/"Jzil Gsix", hand "Spiroc Feathers" (20782) + "Black Silk Cape" (20783) + "Silver Disc" (20938). Gives "Cloak of Spiroc Feathers" (1278).
    - Dialogue with airplane/"Jzil Gsix":
      - Player: "Hail"
        - NPC say: Ah, so you have come to be tested. Many fine things can be your reward. There are three tests which I can administer. Shall you take the test of flight, power, or mind?
        - Condition: `(e.message:findi("hail"))`
      - Player: "Flight" (link: explicit mention)
        - NPC say: So, you wish the test of flight? So be it. You must return to me a Verdant Tessera, an Ebon Shard, and a Griffons Beak to reap your rewards. May the darkness guide your steps.
        - Condition: `(e.message:findi("flight"))`
      - Player: "Test Of Power" (link: explicit mention)
        - Prompted by player input: "Hail"
        - NPC say: The test of power it is. Prove yourself worthy of power and bring me a silver disc, spiroc feathers, and a black silk cape. Only then will you know true power.
        - Condition: `(e.message:findi("test of power"))`
      - Player: "Mind" (link: explicit mention)
        - Prompted by player input: "Hail"
        - NPC say: So, the test of mind it shall be. You must return to me, from this place of air and mist a Rogous Globe, some Djinni Blood, and some Fine Cloth Raiments. Then, and only then, you shall have the reward that you deserve!
        - Condition: `(e.message:findi("mind"))`
8. Loot "Eye of Innoruuk" (20656) from "Innoruuk" (NPC 76007) in `hateplane`. Drop cache: 40.73% chance per kill.
9. Loot "Slime Blood of Cazic-Thule" (20655) from "Dread" in `fearplane`.
10. Loot "Slime Blood of Cazic-Thule" (20655) from "Fright" in `fearplane`.
11. Loot "Slime Blood of Cazic-Thule" (20655) from "Terror" in `fearplane`.
12. Kill lakerathe/"A Failed Apprentice". Spawns "A Tortured Soul" (51144).
13. Loot "Symbol of Insanity" (20648) from "A Tortured Soul".
14. timorous/"Drendico Metalbones", hand "Symbol of Insanity" (20648). Gives "Journal of Drendico" (18086).
    - Dialogue with timorous/"Drendico Metalbones":
      - Player: "Hail"
        - NPC say: The hills ears keep spinning the wonders of wells. Twisting twisting fly in water scar hot horses. Teach me! Bring floating water islands of doom!
        - Condition: `($text=~/hail/i)`
15. timorous/"Drendico Metalbones", hand "Cloak of Spiroc Feathers" (1278) + "Journal of Drendico" (18086) + "Slime Blood of Cazic-Thule" (20655) + "Eye of Innoruuk" (20656). Gives "Prepared Reagent Box" (20653).
16. lakerathe/"Kazen Fecae", hand "Prepared Reagent Box" (20653). Gives "Tome of Instruction" (18087).
17. airplane/"Gkzzallk", hand "Tome of Instruction" (18087). Gives "Gkzzallk in a Box" (20652).
18. lakerathe/"Kazen Fecae", hand "Gkzzallk in a Box" (20652). Gives "Scythe of the Shadowed Soul" (20544).
19. lakerathe/"Kazen Fecae", say "Hail". Requires `Soulwhisper` unset. Gives "Note to Biddliss" (9831).
20. steamfont/"Biddliss Sperandu", hand "Note to Biddliss" (9831). Gives "Gleaming Ore Satchel" (9579).
    - Dialogue with steamfont/"Biddliss Sperandu":
      - Player: "Hail"
        - NPC say: Go away before I sic the clockworks on ya!
        - Condition: `($text=~/hail/i)`
21. Loot "Old Waterlogged Lute" (59025) from "A Shady Treasure Sorter" in `dulak`.
22. Hand "Old Waterlogged Lute" (59025) to torgiran/"A Crazed Miner". Spawns "a crazed miner (KOS)" (226021). Loot "Gleaming Zraxthril Ore" (54006) from "a crazed miner (KOS)".
23. Alternative: Loot "Gleaming Zraxthril Ore" (54006) from "a Broken Skull hoarder" (NPC 226210) in `torgiran`; trigger: torgiran/"The Room", on event_signal.
24. Combine in "Gleaming Ore Satchel" (9579): "Gleaming Zraxthril Ore" (54006). Produces "Sealed Ore Satchel" (27982). The combine does not fail. The recipe must be learned first.
25. steamfont/"Biddliss Sperandu", hand "Sealed Ore Satchel" (27982). Gives "Biddliss's Research Tools" (21799).
26. lakerathe/"Kazen Fecae", hand "Biddliss's Research Tools" (21799). Gives "Drawing of Rune" (22691).
27. poknowledge/"Ruandia", hand "Drawing of Rune" (22691). Gives "Ruandia's Instructions" (10138).
28. poknowledge/"Tebarin", hand "Ruandia's Instructions" (10138). Gives "Intricately Carved Box" (16689).
29. Spawns "An Earthern Crusader" (218027) in `poeartha` on event_combat.
30. Loot "Ball of Elemental Clay" (21720) from "An Earthern Crusader".
31. Alternative: Loot "Ball of Elemental Clay" (21720) from "A Dust Devotee" (NPC 218064) in `poeartha`; trigger: poeartha/"Rings", on event death_complete:218022.
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

### "Scythe of the Shadowed Soul" (20544)

1. Acquisition of "Scythe of the Shadowed Soul" (20544) is documented under "Orb of Deathspeaking" (15784); obtain another copy if needed.

### "Soulwhisper" (62581)

1. Acquisition of "Scythe of the Shadowed Soul" (20544) is documented under "Orb of Deathspeaking" (15784); obtain another copy if needed.
2. lakerathe/"Kazen Fecae", say "Hail". Sets `Soulwhisper` to `1`.
3. Acquisition of "Orb of Deathspeaking" (15784) is documented under "Orb of Deathspeaking" (15784); obtain another copy if needed.
4. natimbi/"Whiahdi", say "I Want The Staff". Sets `Soulwhisper` to `2`.
5. Say "Hail" to barindu/"Viarglug".
6. Spawns "Viarglug (Active)" (283156).
7. Loot "Whiahdi's Earthly Possessions" (11174) from "Viarglug (Active)".
8. natimbi/"Whiahdi", hand "Whiahdi's Earthly Possessions" (11174). Sets `Soulwhisper` to `3`.
9. natimbi/"Whiahdi", say "Power". Sets `Soulwhisper` to `4`.
10. Say "Hail" to causeway/"Tarlang".
11. Spawns "Tarlang (Active)" (303083).
12. Loot "Tarlang's Head" (55855) from "Tarlang (Active)".
13. natimbi/"Whiahdi", hand "Tarlang's Head" (55855). Requires `Soulwhisper` ==3. Requires `Soulwhisper` set. Gives "Soulwhisper" (62581).

### `NecroPre`

Values written: 1, 2.

1. lakerathe/"Egonis", hand "Contract of Sale" (15523). Sets `NecroPre` to `1`.
    - Hand in x1: "Contract of Sale" (15523).
    - Kill qey2hh1/"A Snarling Werewolf". Spawns "Shady Bandit" (12185).
    - Loot "Contract of Sale" (15523) from "Shady Bandit".
    - Spawns Ronaiar Skullmoore (51155).
    - Dialogue with lakerathe/"Egonis":
      - Player: "Hail"
        - NPC say: So the foolish brigand sold the staff to Ronaiar, eh? Who is Ronaiar? He is an insane necromancer that makes his home somewhere near the lake. I had a feeling he would try to get his hands on the staff. That is why I came out here. I must inform Kazen of this turn of events and you must destroy that decrepit fool, Ronaiar. If you find the staff, give it to Geboron.
          - Reply guard: `(defined($qglobals{NecroPre}) && ($qglobals{NecroPre} == 1) && !plugin::check_hasitem($client, 20612))`
        - NPC say: The lake's depths hold so many secrets. Unless you have a reason to be bothering me, I would suggest you leave, before you become another 'secret'.
          - Reply guard: ``
        - Condition: `($text=~/hail/i)`
        - Spawns NPC 51155.

2. poknowledge/"Geboron", hand "Piece of the Staff" (20612). Sets `NecroPre` to `2`.
    - Requires `NecroPre` ==1.
    - Requires `NecroPre` set.
    - Hand in x1: "Piece of the Staff" (20612).
    - Spawns "Man-eating Freshwater Shark" (51158) in `lakerathe` on event_signal.
    - Loot "Piece of the Staff" (20612) from "Man-eating Freshwater Shark".
    - Gives "Piece of the Staff" (20612).
    - Dialogue with poknowledge/"Geboron":
      - Player: "Hail"
        - NPC say: 'Yes. . . $name is it? I have heard of you. I am Geboron, assistant to Kazen. It is most fortunate for you that you happened upon me. I have a task that is of the utmost importance and I believe I can trust you with it. There has been talk recently among my brethren of a most powerful staff that was recently discovered in the realm of discord and is now in the hands of a group of paladins. However my undead servants have informed me that the paladins were transporting the staff through the Karanas and suddenly disappeared without a trace. I want you to find my contact, Yuanda in West Karana and give her this note. It says you are working for me now. Find out what happened to those paladins and the staff! If you find out anything, talk to my assistant, Egonis in Lake Rathe.
        - Condition: `(($text=~/hail/i) && $class eq "Necromancer" && !defined($qglobals{NecroPre}) && !defined($qglobals{SoulWhisper}))`
        - Gives Note to Yuanda (15809).

#### Steps on `NecroPre` that do not change it

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

### `Soulwhisper` 1.5

Values written: 1, 2, 3, 4.

1. lakerathe/"Kazen Fecae", say "Hail". Sets `Soulwhisper` to `1`.
    - Requires `Soulwhisper` unset.
    - Requires "Scythe of the Shadowed Soul" (20544).
    - Prerequisite: "Scythe of the Shadowed Soul" (20544). See section 0.
    - Gives "Note to Biddliss" (9831).
    - Dialogue with lakerathe/"Kazen Fecae":
      - Player: "Hail"
        - NPC say: It has been a while since we have talked. You have done well in obtaining your Scythe. The time has come however for you to perform another task for me. I do not wish to waste time, so in short, I want you to collect a most powerful staff for me. I only have a piece of it as the rest has mysteriously disappeared.
          - Reply guard: `((plugin::check_hasitem($client, 20544)) && !defined($qglobals{Soulwhisper}))`
        - NPC say: I wish to research this staff piece but first I need some special research tools. Take this note and travel to Steamfont. Find a gnome named Biddliss Sperandu and give him the note. When you obtain the research tools hand them to me.
          - Reply guard: `((plugin::check_hasitem($client, 20544)) && !defined($qglobals{Soulwhisper}))`
        - NPC say: Don't you have a task to complete?
          - Reply guard: `(defined($qglobals{Soulwhisper}))`
        - NPC emote: 's eyes seem to glow as he turns to you and says, 'Leave me be if you have no reason to be here, mortal!'
          - Reply guard: ``
        - Condition: `($text=~/hail/i)`
        - Gives Note to Biddliss (9831).
        - Sets `Soulwhisper` to `1`.
      - Player: "Dark Arts" (link: conversation sequence)
        - NPC emote: looks you up and down, his eyes glowing with a soft red light. After a moment he begins to speak though his lips do not move. 'You wish to study under me? Perhaps, if you prove yourself to follow the twisted path. If you prove to be as coldhearted as I then I will let you become my servant.'
          - Reply guard: `($class eq "Necromancer" && $ulevel >= 50)`
        - NPC say: Ha! You call yourself a Necromancer? Come back when you have tortured a few more souls!
          - Reply guard: ``
        - Condition: `($text=~/dark arts/i)`
      - Player: "Prove" (link: explicit mention)
        - NPC say: The wandering knight, Sir Edwin Motte, recently slew one of my lesser servants. This foolish knave travels from town to town pretending to be good. Separate his head from his body and return it to me so I may work my magics upon it. This fool will become another plaything for me, even in death.
        - Condition: `($text=~/prove/i)`
      - Player: "Advance"
        - NPC say: I share great secrets with my more powerful servants who show me they are willing to serve without question. Tell my servant the name of any symbol he gives you and he will instruct you. If I give you a symbol, speak its name to me so I may instruct you.
        - Condition: `($text=~/advance/i)`
      - Player: "Symbol Of Apprentice" (link: conversation sequence)
        - NPC say: You have a long way to go before I teach you the true secrets of life and death. Visit Venenzi Oberendi in the Nektulos Forest and show her the symbol. She is collecting reagents for one of my experiments and is taking far too long. I do not wish her dead, yet, I simply need the reagents soon. Retrieve the reagents and give them to my assistant Emkel Kabae. I do not wish to handle them myself.
        - Condition: `($text=~/symbol of apprentice/i)`
      - Player: "Reagents" (link: explicit mention)
        - NPC say: 'The reagents are the same types the great sorcerer Miragul used to cheat death and become a lich. I do not wish to become a lich as Miragul did, I have greater aspirations than to simply live forever as a hollow shell. I will rise up a being of pirit only, with a will off my own.' Kazen's eyes glow sickly red as he stared off toward the horizon.
        - Condition: `($text=~/reagents/i)`
      - Player: "Symbol Of Testing" (link: conversation sequence)
        - NPC say: Show me that you can overcome larger obstacles and manipulate servants. Gather a force for of mercenaries if you like, or so-called friends, if you desire, and prepare for battle, my promising young student. Return to me with the symbol of testing when you are prepared for battle with my creations. Have no fear, I will not slay you myself. If you do live, tell me the name of the symbol you receive.
        - Condition: `($text=~/symbol of testing/i)`
      - Player: "Symbol Of Insanity" (link: conversation sequence)
        - NPC say: It is time for you to meet my partner, so to speak. Drendico Metalbones is his name and I assure you he is quite mad. His mind has been rended by fright, dread, and terror in his trips to the planes and his heart is full of hatred now. He has a tome which I wish you to use. Show him your symbol slowly and listen to his rantings well, they hide great knowledge.
        - Condition: `($text=~/symbol of insanity/i)`

Alternative or repeat transition to `Soulwhisper` = `1` (not an additional required stage).

1. lakerathe/"Kazen Fecae", hand "Piece of the Staff" (20612). Sets `Soulwhisper` to `1`.
    - Requires `NecroPre` ==2.
    - Requires `NecroPre` set.
    - Hand in x1: "Piece of the Staff" (20612).
    - Spawns "Man-eating Freshwater Shark" (51158) in `lakerathe` on event_signal.
    - Loot "Piece of the Staff" (20612) from "Man-eating Freshwater Shark".
    - Gives "Note to Biddliss" (9831).
    - Gives "Piece of the Staff" (20612).

    - Subquest `NecroPre` documented earlier.
2. natimbi/"Whiahdi", say "I Want The Staff". Sets `Soulwhisper` to `2`.
    - Requires `Soulwhisper` ==1.
    - Requires `Soulwhisper` set.
    - Requires "Orb of Deathspeaking" (15784).
    - Prerequisite: "Orb of Deathspeaking" (15784). See section 0.

3. natimbi/"Whiahdi", hand "Whiahdi's Earthly Possessions" (11174). Sets `Soulwhisper` to `3`.
    - Requires `Soulwhisper` ==2.
    - Requires `Soulwhisper` set.
    - Hand in x1: "Whiahdi's Earthly Possessions" (11174).
    - Say "Hail" to barindu/"Viarglug".
    - Spawns "Viarglug (Active)" (283156).
    - Loot "Whiahdi's Earthly Possessions" (11174) from "Viarglug (Active)".

4. natimbi/"Whiahdi", say "Power". Sets `Soulwhisper` to `4`.
    - Requires `Soulwhisper` ==3.
    - Requires `Soulwhisper` set.
    - Requires "Orb of Deathspeaking" (15784).
    - Prerequisite: "Orb of Deathspeaking" (15784). See section 0.

Alternative or repeat transition to `Soulwhisper` = `3` (not an additional required stage).

3. causeway/"Tarlang", say "Hail". Sets `Soulwhisper` to `3`.
    - Requires `Soulwhisper` ==4.
    - Requires `Soulwhisper` set.
    - Spawns Tarlang (Active) (303083).
    - Dialogue with causeway/"Tarlang":
      - Player: "Hail"
        - NPC say: You dare speak to me? I do not talk to lesser creatures. Prepare for death!
        - Condition: `(($text=~/hail/i) && (defined($qglobals{Soulwhisper}) && ($qglobals{Soulwhisper} == 4)))`
        - Sets `Soulwhisper` to `3`.
        - Spawns NPC 303083.

#### Steps on `Soulwhisper` that do not change it

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
  - Sets `nec_epic_causeway` to `1`.
  - Spawns a chest (Epic 1.5) (283157).
- `natimbi` whiahdi, hand 55855 needs `Soulwhisper` ==3.
  - Turn in Tarlang's Head (55855).
  - Gives Soulwhisper (62581).

### `necro_epic` 2.0

Values written: 5, 6.

5. natimbi/"Whiahdi", say "Locate The Paladin". Sets `necro_epic` to `5`.
    - Requires "Soulwhisper" (62581).
    - Prerequisite: "Soulwhisper" (62581). See section 0.

6. natimbi/"Whiahdi", hand "Globe of Discordant Energy" (47100) + "Staff Piece Number Three" (55932) + "Staff Piece Number Two" (55940) + "Soulwhisper" (62581). Sets `necro_epic` to `6`.
    - Hand in x1: "Staff Piece Number Two" (55940).
    - Hand in x1: "Staff Piece Number Three" (55932).
    - Hand in x1: "Globe of Discordant Energy" (47100).
    - Hand in x1: "Soulwhisper" (62581).
    - Say "Sanait Sanaiij Tsulum" to dranik/"Discord Fluctuation".
    - Spawns "Arl" (336242).
    - Loot "Staff Piece Number Two" (55940) from "Arl".
    - Say "Sanait Sanaiij Tsulum" to dranik/"Discord Fluctuation".
    - Spawns "Gor" (336243).
    - Loot "Staff Piece Number Three" (55932) from "Gor".
    - Say "Check Lorb" to anguish/"Zone Status".
    - Spawns "Orb of Discordant Energy" (317087).
    - Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy".
    - Alternative: Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy" (NPC 317087) in `anguish`; trigger: anguish/"Zone Status", say "Check Uorb".
    - Alternative: Loot "Globe of Discordant Energy" (47100) from "Ornate Chest" (NPC 317112) in `anguish`; trigger: anguish/"Zone Status", say "Check Amv Chest".
    - Alternative: Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy" (NPC 317087) in `anguish`; trigger: anguish/"Zone Status", on event_signal.
    - Alternative: Loot "Globe of Discordant Energy" (47100) from "Overlords Chest" (NPC 317124) in `anguish`; trigger: anguish/"Zone Status", on event_signal.
    - Prerequisite: "Soulwhisper" (62581). See section 0.
    - Gives "Deathwhisper" (64067).

#### Steps on `necro_epic` that do not change it

- `dranik` discord fluctuation, say sanait sanaiij tsulum needs `necro_epic` ==5.
  - Spawns rag (336244).
  - Spawns gor (336243).
  - Spawns arl (336242).
  - Loots Staff Piece Number Three (55932).
  - Loots Staff Piece Number Two (55940).
- `dranik` player, on loot needs `necro_epic` ==5.
  - Sets `nec_chest_dranik` to `1`.
  - Spawns a chest (Epic 2.0) (893).

### Other flags touched along the way

- `nec_epic_barindu` set to 1 at barindu/player.
- `nec_epic_causeway` set to 1 at causeway/player.
