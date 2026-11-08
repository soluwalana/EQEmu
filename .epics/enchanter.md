# Enchanter

Steps taken from the quest graph only. **Broken** means the graph has no edge for that value or that item.

Flags with writes: `EnchPre`, `ench_epic`.

## 0. Prerequisites

Shared acquisition steps appear in the first prerequisite chain that needs them. Later sections reference that chain rather than repeating it.

### "Purifying Crystal" (52954)

1. Buy "Planar Jeweler's Kit" (17764) from "Noirin Khalen" (NPC 202084) in `poknowledge`. Base price: 1,000 copper.
2. global/"Global Player", combine recipe 19919. Sets `ench_epic` to `9`.
3. burningwood/"A Sarnak Imitator", say "Chest". Requires `ench_epic` set. Requires `ench_epic` >=3. Gives "Ornate Staff Chest" (52960).
4. Ground spawn of "Taste of Enticement" (52964) in `mistmoore`.
5. frozenshadow/"Advisor Svartmane", hand "Taste of Enticement" (52964). Gives "1st Piece of the Staff" (54289).
6. Loot "2nd Piece of the Staff" (54310) from "The Yrendan Scarab" in `pojustice`.
7. Loot "3rd Piece of the Staff" (54299) from "Chavoor the Trickster" in `vxed`.
8. Loot "3rd Piece of the Staff" (54299) from "Ikaav Firecaller" in `vxed`.
9. Loot "3rd Piece of the Staff" (54299) from "Kyv Hunter" in `vxed`.
10. Loot "3rd Piece of the Staff" (54299) from "Ukun Bloodbeast" in `vxed`.
11. Loot "3rd Piece of the Staff" (54299) from "Umbiki" in `vxed`.
12. Loot "3rd Piece of the Staff" (54299) from "misguided beludu Creque" in `vxed`.
13. **Broken:** no event trigger found for `bloodfields/war#timer:reset`.
14. Spawns "War Caller Kaavi" (301042) after `bloodfields/war#timer:reset`.
15. Loot "4th Piece of the Staff" (54284) from "War Caller Kaavi".
16. Loot "Ornate Staff Topper" (52961) from "Faleniel of Darkwater" in `sirens`.
17. Loot "All-Seeing Eye" (54293) from "All-Seeing Eye" in `mischiefplane`.
18. potranquility/"Elder Fuirstel", say "Hail". Sets `pop_cod_final` to `1`.
19. poknowledge/"Aid Grimel", say "Skill In Brewing". Requires `pop_cod_final` ==1. Requires `pop_cod_final` set. Gives "Portable Drink Barrel" (17179).
20. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
21. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `steamfont`.
22. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `tox`.
23. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `toxxulia`.
24. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
25. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). The combine does not fail.
26. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
27. Forage "Dragon Egg" (19139) in `templeveeshan`.
28. Forage "Dragon Egg" (19139) in `westwastes`.
29. Combine in "Portable Drink Barrel" (17179): "Water Flask" (13006), "Dragon Egg" (19139). Produces "Dragon Egg Oil" (9664). Requires Brewing, trivial 150.
30. Loot "Glimmering Oil" (52942) from "A Greasy Clockwork" in `poinnovation`.
31. bazaar/"Caerlyna", hand "Spell Research Kit" (93492). Gives "Spell Research Kit Token" (93667).
32. bazaar/"Caerlyna", hand "Spell Research Kit Token" (93667). Gives "Spell Research Kit" (93492).
33. Buy "Firing Sheet" (16906) from "Winn Greenbane" (NPC 5059) in `highpass`. Base price: 10 copper.
34. Combine in Pottery Wheel (21): "Water Flask" (13006), "Block of Clay" (16901). Produces "Small Block of Clay" (16900) x3. Requires Pottery, trivial 21.
35. Combine in Pottery Wheel (21): "Small Block of Clay" (16900), "Water Flask" (13006). Produces "Block of Clay" (16901). Requires Pottery, trivial 21.
36. Combine in Pottery Wheel (21): "Block of Clay" (16901), "Water Flask" (13006). Produces "Large Block of Clay" (16902). Requires Pottery, trivial 21.
37. Buy "Large Bowl Sketch" (16963) from "Min Greyeagle" (NPC 5057) in `highpass`. Base price: 760 copper.
38. Combine in Pottery Wheel (21): "Large Block of Clay" (16902), "Water Flask" (13006), "Large Bowl Sketch" (16963). Produces "Unfired Mixing Bowl" (16930). Requires Pottery, trivial 128.
39. Combine in Kiln (22): "Firing Sheet" (16906), "Unfired Mixing Bowl" (16930). Produces "Mixing Bowl" (17906). Requires Pottery, trivial 15.
40. Buy "Celestial Solvent" (9731) from "A Goblin Bartender" (NPC 11117) in `runnyeye`. Base price: 120 copper.
41. Loot "Fetid Skin" (13150) from "A Fetid Fiend" (NPC 72059) in `fearplane`. Drop cache: 35% chance per kill.
42. Loot "Scare Straw" (13152) from "A Samhain" in `fearplane`.
43. Loot "Turmoil Warts" (8331) from "A Turmoil Toad" in `fearplane`.
44. Spawns "Grimling" (154129) in `acrylia` on event_spawn.
45. Loot "Pearl" (10024) from "Grimling".
46. Alternative: Loot "Pearl" (10024) from "Grimling" (NPC 154129) in `acrylia`; trigger: acrylia/"Raidman", on event_spawn.
47. Alternative: Loot "Pearl" (10024) from "Needs Heading Validation" (NPC 154129) in `acrylia`; trigger: acrylia/"Khati Sha The Twisted", on event_signal.
48. Alternative: Loot "Pearl" (10024) from "a Grelian firelunger" (NPC 337063) in `broodlands`; trigger: broodlands/"Grel Strongboom", on event_spawn.
49. Alternative: Loot "Pearl" (10024) from "a Grelian woundmender" (NPC 337112) in `broodlands`; trigger: broodlands/"Grel Strongboom", on event_spawn.
50. Alternative: Loot "Pearl" (10024) from "a Delve spellbinder" (NPC 341091) in `delvea`; trigger: delvea/"A Drake Egg", on event_death_complete.
51. Alternative: Loot "Pearl" (10024) from "a Delve diviner" (NPC 341085) in `delvea`; trigger: delvea/"A Drake Egg", on event_death_complete.
52. Alternative: Loot "Pearl" (10024) from "a Delve evoker" (NPC 341092) in `delvea`; trigger: delvea/"A Drake Egg", on event_death_complete.
53. Alternative: Loot "Pearl" (10024) from "a Delve drake" (NPC 341087) in `delvea`; trigger: delvea/"A Drake Egg", on event_death_complete.
54. Alternative: Loot "Pearl" (10024) from "Drake Matriarch" (NPC 341149) in `delvea`; trigger: delvea/"The Drake Menace", say "Zone Death".
55. Alternative: Loot "Pearl" (10024) from "a Delve spellbinder" (NPC 341091) in `delvea`; trigger: delvea/"Lava Rock", on event_death.
56. Alternative: Loot "Pearl" (10024) from "a Delve diviner" (NPC 341085) in `delvea`; trigger: delvea/"Lava Rock", on event_death.
57. Alternative: Loot "Pearl" (10024) from "a Delve evoker" (NPC 341092) in `delvea`; trigger: delvea/"Lava Rock", on event_death.
58. Alternative: Loot "Pearl" (10024) from "a Delve drake" (NPC 341087) in `delvea`; trigger: delvea/"Lava Rock", on event_death.
59. Alternative: Loot "Pearl" (10024) from "A Tar Goo" (NPC 119122) in `wakening`; trigger: wakening/"A Tar Goo", on event_death_complete.
60. neriaka/"X-Ta Tompi", hand "Turmoil Warts" (8331) + "Pearl" (10024) + "Fetid Skin" (13150) + "Scare Straw" (13152). Gives "Words of Acquisition (Beza)" (11866).
61. Combine in "Mixing Bowl" (17906): "Celestial Solvent" (9731), "Words of Acquisition (Beza)" (11866). Produces "Celestial Essence" (9650). Requires Baking, trivial 15. The combine does not fail.
62. Loot "Coalesced Mana" (97042) from "Assistant Gareth" (NPC 371049) in `skylance`. Drop cache: 66.67% chance per kill.
63. Loot "White Wolf Skin" (13768) from "A Snow Wolf" in `everfrost`.
64. Loot "White Wolf Skin" (13768) from "A White Wolf" in `everfrost`.
65. Buy "Vial Sketch" (16968) from "Winn Greenbane" (NPC 5059) in `highpass`. Base price: 300 copper.
66. Combine in Pottery Wheel (21): "Water Flask" (13006), "White Wolf Skin" (13768), "Small Block of Clay" (16900), "Vial Sketch" (16968). Produces "Unfired Poison Vial" (16885). Requires Pottery, trivial 148.
67. Buy "High Quality Firing Sheet" (16908) from "Winn Greenbane" (NPC 5059) in `highpass`. Base price: 40 copper.
68. Combine in Kiln (22): "Unfired Poison Vial" (16885), "High Quality Firing Sheet" (16908). Produces "Poison Vial" (16965). Requires Pottery, trivial 17.
69. Spawns "Pxet Elite Blademaster" (284039) in `ferubi` on event_signal.
70. Loot "Broken Sword Blade" (67521) from "Pxet Elite Blademaster".
71. Spawns "Pxet Elite Spearmaster" (284091) in `ferubi` on event_signal.
72. Loot "Jagged Spear Tip" (67522) from "Pxet Elite Spearmaster".
73. Spawns "Pxet Elite Brawler" (284088) in `ferubi` on event_signal.
74. Loot "Tarnished Knuckles" (67523) from "Pxet Elite Brawler".
75. Spawns "Pxet Elite Hammermaster" (284090) in `ferubi` on event_signal.
76. Loot "Chipped Hammer Head" (67524) from "Pxet Elite Hammermaster".
77. Hand "Broken Sword Blade" (67521) + "Jagged Spear Tip" (67522) + "Tarnished Knuckles" (67523) + "Chipped Hammer Head" (67524) to ferubi/"Smith Rondo". Spawns "Master's Apprentice" (284093). Loot "Ruby" (10035) from "Master's Apprentice".
78. Alternative: Loot "Ruby" (10035) from "The Broodqueen" (NPC 337254) in `broodlands`; trigger: broodlands/"Brood Drone", on event_death_complete.
79. Alternative: Loot "Ruby" (10035) from "A parasitic murkglider" (NPC 303121) in `causeway`; trigger: causeway/"Withering Murkglider", on event_hp.
80. Alternative: Loot "Ruby" (10035) from "a Reanimated Berserker" (NPC 103093) in `chardok`; trigger: chardok/"The Earth", on enter.
81. Alternative: Loot "Ruby" (10035) from "a Delve spellbinder" (NPC 341091) in `delvea`; trigger: delvea/"A Drake Egg", on event_death_complete.
82. Alternative: Loot "Ruby" (10035) from "a Delve diviner" (NPC 341085) in `delvea`; trigger: delvea/"A Drake Egg", on event_death_complete.
83. Alternative: Loot "Ruby" (10035) from "a Delve evoker" (NPC 341092) in `delvea`; trigger: delvea/"A Drake Egg", on event_death_complete.
84. Alternative: Loot "Ruby" (10035) from "a Delve drake" (NPC 341087) in `delvea`; trigger: delvea/"A Drake Egg", on event_death_complete.
85. Alternative: Loot "Ruby" (10035) from "Drake Matriarch" (NPC 341149) in `delvea`; trigger: delvea/"The Drake Menace", say "Zone Death".
86. Alternative: Loot "Ruby" (10035) from "a Delve spellbinder" (NPC 341091) in `delvea`; trigger: delvea/"Lava Rock", on event_death.
87. Alternative: Loot "Ruby" (10035) from "a Delve diviner" (NPC 341085) in `delvea`; trigger: delvea/"Lava Rock", on event_death.
88. Alternative: Loot "Ruby" (10035) from "a Delve evoker" (NPC 341092) in `delvea`; trigger: delvea/"Lava Rock", on event_death.
89. Alternative: Loot "Ruby" (10035) from "a Delve drake" (NPC 341087) in `delvea`; trigger: delvea/"Lava Rock", on event_death.
90. Alternative: Loot "Ruby" (10035) from "Master's Apprentice" (NPC 284094) in `ferubi`; trigger: ferubi/"Smith Rondo", hand "Broken Sword Blade" (67521) + "Jagged Spear Tip" (67522) + "Tarnished Knuckles" (67523) + "Chipped Hammer Head" (67524).
91. Alternative: Loot "Ruby" (10035) from "Master's Apprentice" (NPC 284095) in `ferubi`; trigger: ferubi/"Smith Rondo", hand "Broken Sword Blade" (67521) + "Jagged Spear Tip" (67522) + "Tarnished Knuckles" (67523) + "Chipped Hammer Head" (67524).
92. Alternative: Loot "Ruby" (10035) from "Master's Apprentice" (NPC 284096) in `ferubi`; trigger: ferubi/"Smith Rondo", hand "Broken Sword Blade" (67521) + "Jagged Spear Tip" (67522) + "Tarnished Knuckles" (67523) + "Chipped Hammer Head" (67524).
93. Alternative: Loot "Ruby" (10035) from "Pxet Elite Spearmaster" (NPC 284091) in `ferubi`; trigger: ferubi/"Event Spawner", on event_signal.
94. Alternative: Loot "Ruby" (10035) from "A Soldier Of Madness" (NPC 163185) in `griegsend`; trigger: griegsend/"Trapman", on event_combat.
95. Alternative: Loot "Ruby" (10035) from "A Shadowy Figure" (NPC 163190) in `griegsend`; trigger: griegsend/"Trapman Two", on event_combat.
96. Alternative: Loot "Ruby" (10035) from "Servant Of The Magistrate" (NPC 163189) in `griegsend`; trigger: griegsend/"Trapman Two", on event_combat.
97. Alternative: Loot "Ruby" (10035) from "A Dragorn Sycophant" (NPC 335023) in `harbingers`; trigger: harbingers/"Attendant Spawner", on event_spawn.
98. Alternative: Loot "Ruby" (10035) from "Prison Guard Talkor" (NPC 245290) in `rujd`; trigger: rujd/"Rujd", hand "Heavy Orcish Prison Key" (59571).
99. Alternative: Loot "Ruby" (10035) from "Warden" (NPC 245296) in `rujd`; trigger: rujd/"Rujd", say "Zs Timer".
100. Alternative: Loot "Ruby" (10035) from "Shaman" (NPC 245284) in `rujd`; trigger: rujd/"Rujd", say "Zs Timer".
101. Alternative: Loot "Ruby" (10035) from "A Spirit Keeper" (NPC 338169) in `stillmoona`; trigger: stillmoona/"The Keeper Of Strength", hand "Scroll of the Ox" (49007) + "Scroll of the Boar" (49008) + "Scroll of the Dragon" (49009) + "Scroll of the Tiger" (49010).
102. Alternative: Loot "Ruby" (10035) from "Dark Reign Contact" (NPC 338422) in `stillmoona`; trigger: stillmoona/"Best Laid Plans", hand "Temple Plans" (36214).
103. Alternative: Loot "Ruby" (10035) from "Dark Reign assistant" (NPC 338421) in `stillmoona`; trigger: stillmoona/"Best Laid Plans", hand "Temple Plans" (36214).
104. Alternative: Loot "Ruby" (10035) from "Dark Reign Contact" (NPC 338422) in `stillmoona`; trigger: stillmoona/"Best Laid Plans", say "Player Loot".
105. Alternative: Loot "Ruby" (10035) from "A Drake Conspirator" (NPC 338424) in `stillmoona`; trigger: stillmoona/"Scales Of Justice", hand "Small sack of Koi Food" (36215).
106. Alternative: Loot "Ruby" (10035) from "Nethran" (NPC 338404) in `stillmoona`; trigger: stillmoona/"Sickness Of The Spirit", say "Wave Proximity".
107. Alternative: Loot "Ruby" (10035) from "A Goblin Poison Master" (NPC 338425) in `stillmoona`; trigger: stillmoona/"Tea For Thy Master", say "Hail".
108. Alternative: Loot "Ruby" (10035) from "A Poison Assistant" (NPC 338384) in `stillmoona`; trigger: stillmoona/"Tea For Thy Master", say "Hail".
109. Alternative: Loot "Ruby" (10035) from "A Goblin Poison Master" (NPC 338425) in `stillmoona`; trigger: stillmoona/"Tea For Thy Master", say "Tea Master Say".
110. Alternative: Loot "Ruby" (10035) from "A Poison Assistant" (NPC 338384) in `stillmoona`; trigger: stillmoona/"Tea For Thy Master", say "Tea Master Say".
111. Alternative: Loot "Ruby" (10035) from "Lair Mistress" (NPC 339296) in `stillmoonb`; trigger: stillmoonb/"Death Comes Swiftly", say "Zone Death".
112. Alternative: Loot "Ruby" (10035) from "a Goblin Guard" (NPC 339114) in `stillmoonb`; trigger: stillmoonb/"Drake Eggs", say "Drake Death".
113. Alternative: Loot "Ruby" (10035) from "Pixtt Riel Tavas" (NPC 298032) in `tacvi`; trigger: tacvi/"Zone Status", say "Spawn Prt".
114. Alternative: Loot "Ruby" (10035) from "Zun'Muram Mordl Delt" (NPC 298020) in `tacvi`; trigger: tacvi/"Zone Status", say "Spawn Zmmd".
115. Alternative: Loot "Ruby" (10035) from "A Blizzard Seeker" (NPC 340029) in `thundercrest`; trigger: thundercrest/"An End To The Storms", say "Yar Timer".
116. Alternative: Loot "Ruby" (10035) from "Furious Sentry" (NPC 340006) in `thundercrest`; trigger: thundercrest/"The Creator", say "Zone Death".
117. Alternative: Loot "Ruby" (10035) from "Creator Kro'val" (NPC 340007) in `thundercrest`; trigger: thundercrest/"The Creator", say "Player Cast On".
118. Alternative: Loot "Ruby" (10035) from "A Stone Sentinel" (NPC 340521) in `thundercrest`; trigger: thundercrest/"The Creator", say "Player Cast On".
119. Alternative: Loot "Ruby" (10035) from "A Ra'Tuk Decimator" (NPC 289004) in `tipt`; trigger: tipt/"Zone Status", say "Spawn Keyroom".
120. Alternative: Loot "Ruby" (10035) from "a Broken Skull treasurer" (NPC 226208) in `torgiran`; trigger: torgiran/"The Room", on event_signal.
121. Alternative: Loot "Ruby" (10035) from "A Frenzied Luggald Abomination" (NPC 226214) in `torgiran`; trigger: torgiran/"A Water Spirit", say "Frenzy".
122. Alternative: Loot "Ruby" (10035) from "A Berserk Luggald Abomination" (NPC 226215) in `torgiran`; trigger: torgiran/"A Water Spirit", say "Berserk".
123. Alternative: Loot "Ruby" (10035) from "A Furious Luggald Abomination" (NPC 226216) in `torgiran`; trigger: torgiran/"A Water Spirit", say "Fury".
124. Alternative: Loot "Ruby" (10035) from "An Enraged Luggald Abomination" (NPC 226217) in `torgiran`; trigger: torgiran/"A Water Spirit", say "Rage".
125. Alternative: Loot "Ruby" (10035) from "A Trusik Ritualist" (NPC 292010) in `uqua`; trigger: uqua/"Gas Chamber 1", on event_signal.
126. Alternative: Loot "Ruby" (10035) from "A Trusik Stalker" (NPC 292007) in `uqua`; trigger: uqua/"Gas Chamber 1", on event_signal.
127. Alternative: Loot "Ruby" (10035) from "A Trusik Anchorite" (NPC 292029) in `uqua`; trigger: uqua/"Trap Uqua 1", on enter.
128. Alternative: Loot "Ruby" (10035) from "A Trusik Ritualist" (NPC 292005) in `uqua`; trigger: uqua/"Trap Uqua 1", on enter.
129. Alternative: Loot "Ruby" (10035) from "A Trusik Stalker" (NPC 292006) in `uqua`; trigger: uqua/"Trap Uqua 1", on enter.
130. Alternative: Loot "Ruby" (10035) from "A Trusik Summoner" (NPC 292002) in `uqua`; trigger: uqua/"Trap Uqua 1", on enter.
131. Alternative: Loot "Ruby" (10035) from "A Trusik Anchorite" (NPC 292029) in `uqua`; trigger: uqua/"Trap Uqua 2", on enter.
132. Alternative: Loot "Ruby" (10035) from "A Trusik Ritualist" (NPC 292005) in `uqua`; trigger: uqua/"Trap Uqua 2", on enter.
133. Alternative: Loot "Ruby" (10035) from "A Trusik Stalker" (NPC 292006) in `uqua`; trigger: uqua/"Trap Uqua 2", on enter.
134. Alternative: Loot "Ruby" (10035) from "A Trusik Summoner" (NPC 292002) in `uqua`; trigger: uqua/"Trap Uqua 2", on enter.
135. Alternative: Loot "Ruby" (10035) from "A Trusik Anchorite" (NPC 292029) in `uqua`; trigger: uqua/"Trap Uqua 3", on enter.
136. Alternative: Loot "Ruby" (10035) from "A Trusik Ritualist" (NPC 292005) in `uqua`; trigger: uqua/"Trap Uqua 3", on enter.
137. Alternative: Loot "Ruby" (10035) from "A Trusik Stalker" (NPC 292006) in `uqua`; trigger: uqua/"Trap Uqua 3", on enter.
138. Alternative: Loot "Ruby" (10035) from "A Trusik Summoner" (NPC 292002) in `uqua`; trigger: uqua/"Trap Uqua 3", on enter.
139. Alternative: Loot "Ruby" (10035) from "A Trusik Anchorite" (NPC 292029) in `uqua`; trigger: uqua/"Trap Uqua 4", on enter.
140. Alternative: Loot "Ruby" (10035) from "A Trusik Ritualist" (NPC 292005) in `uqua`; trigger: uqua/"Trap Uqua 4", on enter.
141. Alternative: Loot "Ruby" (10035) from "A Trusik Stalker" (NPC 292006) in `uqua`; trigger: uqua/"Trap Uqua 4", on enter.
142. Alternative: Loot "Ruby" (10035) from "A Trusik Summoner" (NPC 292002) in `uqua`; trigger: uqua/"Trap Uqua 4", on enter.
143. Alternative: Loot "Ruby" (10035) from "A Trusik Anchorite" (NPC 292029) in `uqua`; trigger: uqua/"Trap Uqua 5", on enter.
144. Alternative: Loot "Ruby" (10035) from "A Trusik Ritualist" (NPC 292005) in `uqua`; trigger: uqua/"Trap Uqua 5", on enter.
145. Alternative: Loot "Ruby" (10035) from "A Trusik Stalker" (NPC 292006) in `uqua`; trigger: uqua/"Trap Uqua 5", on enter.
146. Alternative: Loot "Ruby" (10035) from "A Trusik Summoner" (NPC 292002) in `uqua`; trigger: uqua/"Trap Uqua 5", on enter.
147. Alternative: Loot "Ruby" (10035) from "A Trusik Anchorite" (NPC 292029) in `uqua`; trigger: uqua/"Trap Uqua 6", on enter.
148. Alternative: Loot "Ruby" (10035) from "A Trusik Ritualist" (NPC 292005) in `uqua`; trigger: uqua/"Trap Uqua 6", on enter.
149. Alternative: Loot "Ruby" (10035) from "A Trusik Stalker" (NPC 292006) in `uqua`; trigger: uqua/"Trap Uqua 6", on enter.
150. Alternative: Loot "Ruby" (10035) from "A Trusik Summoner" (NPC 292002) in `uqua`; trigger: uqua/"Trap Uqua 6", on enter.
151. Alternative: Loot "Ruby" (10035) from "A Trusik Anchorite" (NPC 292029) in `uqua`; trigger: uqua/"Trap Uqua 7", on enter.
152. Alternative: Loot "Ruby" (10035) from "A Trusik Ritualist" (NPC 292005) in `uqua`; trigger: uqua/"Trap Uqua 7", on enter.
153. Alternative: Loot "Ruby" (10035) from "A Trusik Stalker" (NPC 292006) in `uqua`; trigger: uqua/"Trap Uqua 7", on enter.
154. Alternative: Loot "Ruby" (10035) from "A Trusik Summoner" (NPC 292002) in `uqua`; trigger: uqua/"Trap Uqua 7", on enter.
155. Alternative: Loot "Ruby" (10035) from "A Trusik Anchorite" (NPC 292029) in `uqua`; trigger: uqua/"Trap Uqua 8", on enter.
156. Alternative: Loot "Ruby" (10035) from "A Trusik Ritualist" (NPC 292005) in `uqua`; trigger: uqua/"Trap Uqua 8", on enter.
157. Alternative: Loot "Ruby" (10035) from "A Trusik Stalker" (NPC 292006) in `uqua`; trigger: uqua/"Trap Uqua 8", on enter.
158. Alternative: Loot "Ruby" (10035) from "A Trusik Summoner" (NPC 292002) in `uqua`; trigger: uqua/"Trap Uqua 8", on enter.
159. Alternative: Loot "Ruby" (10035) from "Master's Apprentice" (NPC 284093) in `ferubi`; trigger: ferubi/"Weapon Master Vtiink Vzaan", on timer repop1.
160. Alternative: Loot "Ruby" (10035) from "Master's Apprentice" (NPC 284094) in `ferubi`; trigger: ferubi/"Weapon Master Vtiink Vzaan", on timer repop2.
161. Alternative: Loot "Ruby" (10035) from "Master's Apprentice" (NPC 284095) in `ferubi`; trigger: ferubi/"Weapon Master Vtiink Vzaan", on timer repop3.
162. Alternative: Loot "Ruby" (10035) from "Master's Apprentice" (NPC 284096) in `ferubi`; trigger: ferubi/"Weapon Master Vtiink Vzaan", on timer repop4.
163. Alternative: Loot "Ruby" (10035) from "a blade of the First" (NPC 249090) in `guke`; trigger: guke/"Guke", on timer adds_on_granos.
164. Alternative: Loot "Ruby" (10035) from "A Risen Acolyte" (NPC 249152) in `guke`; trigger: guke/"Guke", on timer spawn_adds.
165. Alternative: Loot "Ruby" (10035) from "A Risen Champion" (NPC 249154) in `guke`; trigger: guke/"Guke", on timer spawn_adds.
166. Alternative: Loot "Ruby" (10035) from "A Risen Death Knight" (NPC 249157) in `guke`; trigger: guke/"Guke", on timer spawn_adds.
167. Alternative: Loot "Ruby" (10035) from "A Risen Deceiver" (NPC 249161) in `guke`; trigger: guke/"Guke", on timer spawn_adds.
168. Alternative: Loot "Ruby" (10035) from "A Risen Fire Caller" (NPC 249164) in `guke`; trigger: guke/"Guke", on timer spawn_adds.
169. Alternative: Loot "Ruby" (10035) from "A Risen Partisan" (NPC 249169) in `guke`; trigger: guke/"Guke", on timer spawn_adds.
170. Alternative: Loot "Ruby" (10035) from "A Risen Stalker" (NPC 249178) in `guke`; trigger: guke/"Guke", on timer spawn_adds.
171. Alternative: Loot "Ruby" (10035) from "A Risen Witch Doctor" (NPC 249183) in `guke`; trigger: guke/"Guke", on timer spawn_adds.
172. Alternative: Loot "Ruby" (10035) from "A Malicious Force" (NPC 249128) in `guke`; trigger: guke/"Guke", on timer depop.
173. Alternative: Loot "Ruby" (10035) from "A Moaning Banshee" (NPC 186193) in `hateplaneb`; trigger: hateplaneb/"Maestro", on event signal:186111.
174. Alternative: Loot "Ruby" (10035) from "A Screeching Banshee" (NPC 186192) in `hateplaneb`; trigger: hateplaneb/"Maestro", on event signal:186111.
175. Alternative: Loot "Ruby" (10035) from "A Wailing Banshee" (NPC 186194) in `hateplaneb`; trigger: hateplaneb/"Maestro", on event signal:186111.
176. Alternative: Loot "Ruby" (10035) from "NPC: ##Pixtt Priest Summoner" (NPC 293220) in `kodtaz`; trigger: kodtaz/"Totd", on event death_complete:293210.
177. Alternative: Loot "Ruby" (10035) from "Zun'Muram Mordl Delt" (NPC 298020) in `tacvi`; trigger: tacvi/"Zmmd", on timer wipecheck.
178. Alternative: Loot "Ruby" (10035) from "A Blizzard Seeker" (NPC 340029) in `thundercrest`; trigger: thundercrest/"An End To The Storms", on timer Seekers.
179. Alternative: Loot "Ruby" (10035) from "Tiv Prayer Chanter" (NPC 297066) in `txevu`; trigger: txevu/"Highpriest", on event spawn:297199.
180. Alternative: Loot "Ruby" (10035) from "Tiv Prayer Chanter" (NPC 297062) in `txevu`; trigger: txevu/"Highpriest", on event spawn:297061.
181. Alternative: Loot "Ruby" (10035) from "Tiv Prayer Chanter" (NPC 297063) in `txevu`; trigger: txevu/"Highpriest", on event spawn:297197.
182. Alternative: Loot "Ruby" (10035) from "Tiv Prayer Chanter" (NPC 297064) in `txevu`; trigger: txevu/"Highpriest", on event spawn:297059.
183. Alternative: Loot "Ruby" (10035) from "Tiv Prayer Chanter" (NPC 297065) in `txevu`; trigger: txevu/"Highpriest", on event spawn:297057.
184. Alternative: Loot "Ruby" (10035) from "A Murk Hatchling" (NPC 300084) in `wallofslaughter`; trigger: wallofslaughter/"A Quivering Egg", on timer hatch.
185. Combine in "Spell Research Kit" (93492): "Celestial Essence" (9650), "Coalesced Mana" (97042), "Poison Vial" (16965), "Ruby" (10035). Produces "Vial of Purified Mana" (10254). Requires Research, trivial 200.
186. Forage "Glow Lichen" (14925) in `nektulos`.
187. Loot "Essence of Sunlight" (22527) from "A Faerie Dragon" (NPC 119073) in `wakening`. Drop cache: 55% chance per kill.
188. Ground spawn of "Abysmal Moonwater" (54298) in `abysmal`.
189. Combine in Brew Barrel (19): "Vial of Purified Mana" (10254), "Glow Lichen" (14925), "Essence of Sunlight" (22527), "Abysmal Moonwater" (54298). Produces "Glowing Concoction" (52943). Requires Brewing, trivial 116.
190. Buy "Medicine Bag" (17901) from "Rendallen Ironforge" (NPC 2071) in `qeynos2`. Base price: 1,000 copper.
191. Buy "Glaze Lacquer" (29355) from "Elisha Dirtyshoes" (NPC 202134) in `poknowledge`. Base price: 8,000 copper.
192. Buy "Prism Shard" (65469) from "Elisha Dirtyshoes" (NPC 202134) in `poknowledge`. Base price: 5,000 copper.
193. Combine in "Medicine Bag" (17901): "Glaze Lacquer" (29355), "Prism Shard" (65469). Produces "Prismatic Dye" (65472). Requires Alchemy, trivial 54.
194. Combine in Brew Barrel (19): "Dragon Egg Oil" (9664), "Glimmering Oil" (52942), "Glowing Concoction" (52943), "Prismatic Dye" (65472). Produces "Incandescent Oil" (57924). Requires Brewing, trivial 116. The combine does not fail.
195. Loot "Dragon Boneshard" (65574) from "A Curate" (NPC 109068) in `veksar`. Drop cache: 10% chance per kill.
196. Hand "Dragon Boneshard" (65574) to veksar/"Spirit Of Garudon". Spawns "Garudon" (109107). Loot "Garudon's Statue" (52941) from "Garudon".
197. lakeofillomen/"A Bloodgill Mimic", hand "Garudon's Statue" (52941). Sets `EnchPre` to `1`.
198. Loot "Crumbling Tome" (54313) from "A Shissar Lorekeeper" in `ssratemple`.
199. ssratemple/"A Soriz Imitator", hand "Crumbling Tome" (54313). Requires `EnchPre` ==1. Gives "Illegible Tome" (52947).
200. akanon/"Rilgor Plegnog", say "Insidious". Gives "Compacting Satchel" (54303).
201. Loot "Fine Insidious Halo" (54384) from "A Forsaken Revenant" (NPC 186146) in `hateplaneb`. Drop cache: 2% chance per kill.
202. Loot "Fine Insidious Sleeves" (54385) from "A Forsaken Revenant" (NPC 186146) in `hateplaneb`. Drop cache: 2.08% chance per kill.
203. Loot "Fine Insidious Manacle" (54386) from "A Forsaken Revenant" (NPC 186146) in `hateplaneb`. Drop cache: 2.09% chance per kill.
204. Loot "Fine Insidious Gloves" (54387) from "A Forsaken Revenant" (NPC 186146) in `hateplaneb`. Drop cache: 2.24% chance per kill.
205. Loot "Fine Insidious Pantaloons" (54388) from "A Forsaken Revenant" (NPC 186146) in `hateplaneb`. Drop cache: 2.23% chance per kill.
206. Loot "Fine Insidious Slippers" (54389) from "A Forsaken Revenant" (NPC 186146) in `hateplaneb`. Drop cache: 2.07% chance per kill.
207. Combine in "Compacting Satchel" (54303): "Fine Insidious Halo" (54384), "Fine Insidious Sleeves" (54385), "Fine Insidious Manacle" (54386), "Fine Insidious Gloves" (54387), "Fine Insidious Pantaloons" (54388), "Fine Insidious Slippers" (54389). Produces "Insidious Bundle" (54317). The combine does not fail.
208. akanon/"Rilgor Plegnog", hand "Insidious Bundle" (54317). Gives "Gnomish Translating Device" (52945).
209. burningwood/"A Sarnak Imitator", hand "Gnomish Translating Device" (52945) + "Illegible Tome" (52947). Sets `EnchPre` to `2`.
210. burningwood/"A Sarnak Imitator", say "Hail". Sets `ench_epic` to `1`.
211. burningwood/"A Sarnak Imitator", say "Prepared". Requires `ench_epic` set. Requires `ench_epic` >=1. Gives "Tattered Illegible Tome" (57918).
212. Ground spawn of "Cryptic Page" (52933) in `charasis`.
213. Ground spawn of "Cryptic Page" (52934) in `sebilis`.
214. Ground spawn of "Cryptic Page" (52935) in `cazicthule`.
215. Ground spawn of "Cryptic Page" (52936) in `crystal`.
216. Ground spawn of "Cryptic Page" (52937) in `skyshrine`.
217. Ground spawn of "Cryptic Page" (52938) in `velketor`.
218. Ground spawn of "Cryptic Page" (52939) in `nadox`.
219. Ground spawn of "Cryptic Page" (54308) in `najena`.
220. Ground spawn of "Cryptic Page" (57916) in `fungusgrove`.
221. Ground spawn of "Cryptic Page" (57923) in `oot`.
222. Combine in "Tattered Illegible Tome" (57918): "Cryptic Page" (52933), "Cryptic Page" (52934), "Cryptic Page" (52935), "Cryptic Page" (52936), "Cryptic Page" (52937), "Cryptic Page" (52938), "Cryptic Page" (52939), "Cryptic Page" (54308), "Cryptic Page" (57916), "Cryptic Page" (57923). Produces "Complete Illegible Tome" (54267). The combine does not fail.
223. burningwood/"A Sarnak Imitator", hand "Complete Illegible Tome" (54267). Sets `ench_epic` to `2`.
224. poknowledge/"Grand Librarian Maelin", say "Jeb Lumsed Sent Me". Requires `ench_epic` ==2. Gives "Note to Lobaen" (52950).
225. poknowledge/"Illusionist Lobaen", hand "Note to Lobaen" (52950). Gives "Sealed Documents" (52959).
226. burningwood/"A Sarnak Imitator", hand "Sealed Documents" (52959). Gives "Assembling the Staff" (54286).
227. Loot "Sullied Gold Filigree" (52963) from "An Enticing Potameid" in `natimbi`.
228. hohonora/"Anthone Chapin", hand "Sullied Gold Filigree" (52963). Gives "Purified Gold Filigree" (52953).
229. Combine in "Ornate Staff Chest" (52960): "1st Piece of the Staff" (54289), "2nd Piece of the Staff" (54310), "3rd Piece of the Staff" (54299), "4th Piece of the Staff" (54284), "Ornate Staff Topper" (52961), "All-Seeing Eye" (54293), "Incandescent Oil" (57924), "Purified Gold Filigree" (52953). Produces "Latched Ornate Chest" (52966). The combine does not fail.
230. burningwood/"A Sarnak Imitator", hand "Latched Ornate Chest" (52966). Gives "Oculus of Persuasion" (52952).
231. Loot "Heart of a Twisted Stoneservant" (54239) from "A Twisted Stoneservant" in `riwwi`.
232. Hand "Heart of a Twisted Stoneservant" (54239) to wakening/"Alaurin". Spawns "A Luminescent Geonid" (119184). Loot "Luminescent Crystal" (52949) from "A Luminescent Geonid".
233. wakening/"Alaurin", hand "Luminescent Crystal" (52949). Gives "Purifying Crystal Fragment" (52955).
234. Loot "Volatile Vampyre Blood" (52965) from "a Coterie insatiate" in `tenebrous`.
235. westwastes/"Vohnkare", hand "Volatile Vampyre Blood" (52965). Gives "Purifying Crystal Fragment" (52956).
236. Buy "Gnomish Candy" (52944) from "Clockwork Merchant" (NPC 55308) in `akanon`. Base price: 125,000 copper.
237. Buy "Koada'Dal Silk" (52948) from "Merchant Tyslin" (NPC 61044) in `felwithea`. Base price: 125,000 copper.
238. Buy "Feir'Dal Champagne" (52940) from "Innkeep" (NPC 19084) in `rivervale`. Base price: 125,000 copper.
239. Buy "Dwarven Steel" (57921) from "Gretta Mottle" (NPC 60000) in `kaladima`. Base price: 125,000 copper.
240. lfaydark/"A Brownie Noble", hand "Feir'Dal Champagne" (52940) + "Gnomish Candy" (52944) + "Koada'Dal Silk" (52948) + "Dwarven Steel" (57921). Sets `ench_epic` to `8`.
241. Loot "Harnessing Stone" (52946) from "Miriku the Chaotic" in `kael`.
242. lfaydark/"A Brownie Noble", hand "Harnessing Stone" (52946). Requires `ench_epic` ==8. Gives "Purifying Crystal Fragment" (52957).
243. Say "Spawn Devastating Pookas" to tipt/"Rikabi The Riddler".
244. Spawns "A Devastating Pooka" (289037).
245. Loot "Mountain Pooka Meat" (54240) from "A Devastating Pooka".
246. Hand "Mountain Pooka Meat" (54240) to jaggedpine/"Chef Brargus". Spawns "Firwyn" (181226). Loot "Dryad Necklace" (57917) from "Firwyn".
247. gfaydark/"Feyana Lightwing", hand "Dryad Necklace" (57917). Gives "Purifying Crystal Fragment" (52958).
248. Combine in "Planar Jeweler's Kit" (17764): "Purifying Crystal Fragment" (52955), "Purifying Crystal Fragment" (52956), "Purifying Crystal Fragment" (52957), "Purifying Crystal Fragment" (52958). Produces "Purifying Crystal" (52954). Requires Jewelry Making. The combine does not fail.

### "Oculus of Persuasion" (52952)

1. Acquisition of "Oculus of Persuasion" (52952) is documented under "Purifying Crystal" (52954); obtain another copy if needed.

### "Latched Ornate Chest" (52966)

1. Acquisition of "Latched Ornate Chest" (52966) is documented under "Purifying Crystal" (52954); obtain another copy if needed.

### "Channeling Crystal" (57920)

1. Loot "Tattered Incantation" (57919) from "Cipheron" in `wallofslaughter`.
2. Loot "Noxious Secretion" (52951) from "Withering Murkglider" in `causeway`.
3. nedaria/"Priestess Rakhu", hand "Noxious Secretion" (52951) + "Tattered Incantation" (57919). Requires `ench_epic` ==9. Gives "Channeling Crystal" (57920).

### "Gnomish Translating Device" (52945)

1. Acquisition of "Gnomish Translating Device" (52945) is documented under "Purifying Crystal" (52954); obtain another copy if needed.

### "Illegible Tome" (52947)

1. Acquisition of "Illegible Tome" (52947) is documented under "Purifying Crystal" (52954); obtain another copy if needed.

### "Sealed Documents" (52959)

1. Acquisition of "Sealed Documents" (52959) is documented under "Purifying Crystal" (52954); obtain another copy if needed.

### "Complete Illegible Tome" (54267)

1. Acquisition of "Complete Illegible Tome" (54267) is documented under "Purifying Crystal" (52954); obtain another copy if needed.

## `EnchPre`

Values written: 1, 2.

### 1. a bloodgill mimic — hand 52941

Zone: `lakeofillomen`.

Sets `EnchPre` to `1`.

- Turn in x1: Garudon's Statue (52941).
In script order:

1. Sets `EnchPre` to `1`.


How the items are reached:

- Garudon's Statue (52941)
  - Hand "Dragon Boneshard" (65574) to veksar/"Spirit Of Garudon". Spawns "Garudon" (109107). Loot "Garudon's Statue" (52941) from "Garudon".

### 2. a sarnak imitator — hand 52945+52947

Zone: `burningwood`.

Sets `EnchPre` to `2`.

- Turn in x1: Illegible Tome (52947).
- Turn in x1: Gnomish Translating Device (52945).
In script order:

1. Sets `EnchPre` to `2`.
2. Gives Tattered Illegible Tome (57918).


How the items are reached:

- Illegible Tome (52947)
  - Prerequisite: "Illegible Tome" (52947). See section 0.
- Gnomish Translating Device (52945)
  - Prerequisite: "Gnomish Translating Device" (52945). See section 0.

### Steps on `EnchPre` that do not change it

- `burningwood` a sarnak imitator, say hail needs `EnchPre` ==2.
  - Sets `ench_epic` to `1`.
- `ssratemple` a soriz imitator, hand 54313 needs `EnchPre` ==1.
  - Turn in Crumbling Tome (54313).
  - Gives Illegible Tome (52947).

## `ench_epic`

Values written: 1, 2, 3, 7, 8, 9, 10.

### 1. a sarnak imitator — say hail

Zone: `burningwood`.

> Much time has passed since the creation of the Staff of the Serpent. The power of discord is seeping into our fair world, and only the most powerful of us sh...

Sets `ench_epic` to `1`.

- Needs `ench_epic` unset.
- Needs `EnchPre` ==2.
In script order:

1. Sets `ench_epic` to `1`.


This step also depends on `EnchPre`, shown above.

### 2. a sarnak imitator — hand 54267

Zone: `burningwood`.

Sets `ench_epic` to `2`.

- Turn in x1: Complete Illegible Tome (54267).
In script order:

1. Sets `ench_epic` to `2`.


How the items are reached:

- Complete Illegible Tome (54267)
  - Prerequisite: "Complete Illegible Tome" (54267). See section 0.

### 3. a sarnak imitator — hand 52959

Zone: `burningwood`.

Sets `ench_epic` to `3`.

- Turn in x1: Sealed Documents (52959).
In script order:

1. Sets `ench_epic` to `3`.
2. Gives Assembling the Staff (54286).


How the items are reached:

- Sealed Documents (52959)
  - Prerequisite: "Sealed Documents" (52959). See section 0.

### 7. a sarnak imitator — hand 52966

Zone: `burningwood`.

Sets `ench_epic` to `7`.

- Turn in x1: Latched Ornate Chest (52966).
In script order:

1. Sets `ench_epic` to `7`.
2. Gives Oculus of Persuasion (52952).


How the items are reached:

- Latched Ornate Chest (52966)
  - Prerequisite: "Latched Ornate Chest" (52966). See section 0.

### 8. a brownie noble — hand 52940+52944+52948+57921

Zone: `lfaydark`.

Sets `ench_epic` to `8`.

- Needs Oculus of Persuasion (52952).
- Turn in x1: Gnomish Candy (52944).
- Turn in x1: Koada`Dal Silk (52948).
- Turn in x1: Feir`Dal Champagne (52940).
- Turn in x1: Dwarven Steel (57921).
In script order:

1. Sets `ench_epic` to `8`.


How the items are reached:

- Oculus of Persuasion (52952)
  - Prerequisite: "Oculus of Persuasion" (52952). See section 0.
- Gnomish Candy (52944)
  - Buy "Gnomish Candy" (52944) from "Clockwork Merchant" (NPC 55308) in `akanon`. Base price: 125,000 copper.
- Koada`Dal Silk (52948)
  - Buy "Koada'Dal Silk" (52948) from "Merchant Tyslin" (NPC 61044) in `felwithea`. Base price: 125,000 copper.
- Feir`Dal Champagne (52940)
  - Buy "Feir'Dal Champagne" (52940) from "Innkeep" (NPC 19084) in `rivervale`. Base price: 125,000 copper.
- Dwarven Steel (57921)
  - Buy "Dwarven Steel" (57921) from "Gretta Mottle" (NPC 60000) in `kaladima`. Base price: 125,000 copper.

### 9. global player — combine recipe 19919

Zone: `global`.

Sets `ench_epic` to `9`.

In script order:

1. Sets `ench_epic` to `9`.


Combine:

- `recipe:19919` is combined in Planar Jeweler's Kit (17764).
  - Buy "Planar Jeweler's Kit" (17764) from "Noirin Khalen" (NPC 202084) in `poknowledge`. Base price: 1,000 copper.
  - Put in x1: Oculus of Persuasion (52952).
    - Prerequisite: "Oculus of Persuasion" (52952). See section 0.
  - Put in x1: Purifying Crystal (52954).
    - Prerequisite: "Purifying Crystal" (52954). See section 0.
  - Hands back Oculus of Persuasion (52952).
  - Produces no new item.
  - Requires Jewelry Making. The combine does not fail.

### 10. global player — combine recipe 19920

Zone: `global`.

Sets `ench_epic` to `10`.

In script order:

1. Sets `ench_epic` to `10`.


Combine:

- `recipe:19920` is combined in Channeling Crystal (57920).
  - Prerequisite: "Channeling Crystal" (57920). See section 0.
  - Put in x1: Globe of Discordant Energy (47100).
    - Say "Check Lorb" to anguish/"Zone Status".
    - Spawns "Orb of Discordant Energy" (317087).
    - Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy".
    - Alternative: Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy" (NPC 317087) in `anguish`; trigger: anguish/"Zone Status", say "Check Uorb".
    - Alternative: Loot "Globe of Discordant Energy" (47100) from "Ornate Chest" (NPC 317112) in `anguish`; trigger: anguish/"Zone Status", say "Check Amv Chest".
    - Alternative: Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy" (NPC 317087) in `anguish`; trigger: anguish/"Zone Status", on event_signal.
    - Alternative: Loot "Globe of Discordant Energy" (47100) from "Overlords Chest" (NPC 317124) in `anguish`; trigger: anguish/"Zone Status", on event_signal.
  - Put in x1: Oculus of Persuasion (52952).
    - Prerequisite: "Oculus of Persuasion" (52952). See section 0.
  - Produces Staff of Eternal Eloquence (52962).
  - The combine does not fail.

### Steps on `ench_epic` that do not change it

- `burningwood` a sarnak imitator, say chest needs `ench_epic` set.
  - Gives Ornate Staff Chest (52960).
- `burningwood` a sarnak imitator, say prepared needs `ench_epic` set.
  - Gives Tattered Illegible Tome (57918).
- `causeway` player, on loot needs `ench_epic` ==9.
  - Sets `ench_chest_causeway` to `1`.
  - Spawns a chest (epic 2.0) (893).
- `lfaydark` a brownie noble, hand 52946 needs `ench_epic` ==8.
  - Turn in Harnessing Stone (52946).
  - Gives Purifying Crystal Fragment (52957).
- `mischiefplane` player, on loot needs `ench_epic` >=3.
  - Sets `ench_epic_pom` to `1`.
  - Spawns a chest (Epic 1.5) (283157).
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
- `nedaria` priestess rakhu, hand 52951+57919 needs `ench_epic` ==9.
  - Turn in Tattered Incantation (57919).
  - Turn in Noxious Secretion (52951).
  - Gives Channeling Crystal (57920).
- `poknowledge` grand librarian maelin, say jeb lumsed sent me needs `ench_epic` ==2.
  - Gives Note to Lobaen (52950).
- `sirens` player, on loot needs `ench_epic` set.
  - Sets `ench_epic_sirens` to `1`.
  - Spawns a chest (Epic 1.5) (283157).
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
- `wallofslaughter` player, on loot needs `ench_epic` ==9.
  - Sets `ench_wos_chest` to `1`.
  - Spawns a chest (Epic 1.5) (893).

## Other flags touched along the way

- `ench_epic_pom` set to 1 at mischiefplane/player.
- `ench_epic_sirens` set to 1 at sirens/player.
