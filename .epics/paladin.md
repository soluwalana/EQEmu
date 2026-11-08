# Paladin

Steps taken from the quest graph only. **Broken** means the graph has no edge for that value or that item.

Flags with writes: `paladin_epic`.

## 0. Prerequisites

Each list is the order you obtain that item. Later steps point here instead of repeating the chain.

### "Rithnok's Soulstone" (69941)

1. Spawns "A Corrupted Koalindl" (69141) in `oot` on event_fish_success.
2. Loot "Corrupted Koalindl's Heart" (69929) from "A Corrupted Koalindl".
3. Spawns "A Corrupted Koalindl" (224432) in `gunthak` on event_fish_success.
4. Loot "Corrupted Koalindl's Heart" (69930) from "A Corrupted Koalindl".
5. Spawns "A Corrupted Koalindl" (93306) in `overthere` on event_fish_success.
6. Loot "Corrupted Koalindl's Heart" (69931) from "A Corrupted Koalindl".
7. Spawns "A Corrupted Koalindl" (182150) in `nedaria` on event_fish_success.
8. Loot "Corrupted Koalindl's Heart" (69932) from "A Corrupted Koalindl".
9. qeynos2/"Enic Ruklin", hand "Corrupted Koalindl's Heart" (69929) + "Corrupted Koalindl's Heart" (69930) + "Corrupted Koalindl's Heart" (69931) + "Corrupted Koalindl's Heart" (69932). Sets `paladin_epic` to `4`.
10. qeynos2/"Enic Ruklin", hand "Corrupted Koalindl's Heart" (69929) + "Corrupted Koalindl's Heart" (69930) + "Corrupted Koalindl's Heart" (69931) + "Corrupted Koalindl's Heart" (69932). Gives "Seal of Enic" (69933).
11. Say "Hail" to skyfire/"Dry Sapara".
12. Spawns "Rithnok the Tormented" (91193).
13. Loot "Rithnok's Soulstone" (69935) from "Rithnok the Tormented".
14. skyfire/"Dry Sapara", hand "Rithnok's Soulstone" (69935). Gives "Rithnok's Soulstone" (69936).
15. Ground spawn of "Soulstone Shard" (69937) in `draniksscar`.
16. Ground spawn of "Soulstone Shard" (69938) in `bloodfields`.
17. Ground spawn of "Soulstone Shard" (69939) in `causeway`.
18. Ground spawn of "Soulstone Shard" (69940) in `dranik`.
19. Combine in "Rithnok's Soulstone" (69936): "Soulstone Shard" (69937), "Soulstone Shard" (69938), "Soulstone Shard" (69939), "Soulstone Shard" (69940). Produces "Rithnok's Soulstone" (69941). The combine does not fail.

### "Drema's Soulstone" (69952)

1. Spawns "A Corrupted Koalindl" (69141) in `oot` on event_fish_success.
2. Loot "Corrupted Koalindl's Heart" (69929) from "A Corrupted Koalindl".
3. Spawns "A Corrupted Koalindl" (224432) in `gunthak` on event_fish_success.
4. Loot "Corrupted Koalindl's Heart" (69930) from "A Corrupted Koalindl".
5. Spawns "A Corrupted Koalindl" (93306) in `overthere` on event_fish_success.
6. Loot "Corrupted Koalindl's Heart" (69931) from "A Corrupted Koalindl".
7. Spawns "A Corrupted Koalindl" (182150) in `nedaria` on event_fish_success.
8. Loot "Corrupted Koalindl's Heart" (69932) from "A Corrupted Koalindl".
9. qeynos2/"Enic Ruklin", hand "Corrupted Koalindl's Heart" (69929) + "Corrupted Koalindl's Heart" (69930) + "Corrupted Koalindl's Heart" (69931) + "Corrupted Koalindl's Heart" (69932). Sets `paladin_epic` to `4`.
10. dawnshroud/"Mikhal Young", hand "Drema's Fingerbone" (69946). Sets `paladin_epic` to `5`.
11. dawnshroud/"Mikhal Young", say "Find Anything". Requires `paladin_epic` ==4. Gives "Drema's Locket" (69945).
12. letalis/"Drema Young", hand "Drema's Locket" (69945). Requires `paladin_epic` set. Requires `paladin_epic` >=4. Gives "Drema's Fingerbone" (69946).
13. dawnshroud/"Denns Rootenpaw", hand "Drema's Fingerbone" (69946). Requires `paladin_epic` ==5. Gives "Bone Collector's Bag" (69947).
14. Loot "Dark Skeleton Remains" (69927) from "A Sun Revenant" in `thegrey`.
15. Loot "Dark Skeleton Remains" (69926) from "Disturbed Elysian Remains" (NPC 176016) in `umbral`. Drop cache: 2.58% chance per kill.
16. Loot "Dark Skeleton Remains" (69925) from "A Soriz Slave" (NPC 162029) in `ssratemple`. Drop cache: 35% chance per kill.
17. Combine in "Bone Collector's Bag" (69947): "Dark Skeleton Remains" (69927), "Dark Skeleton Remains" (69926), "Dark Skeleton Remains" (69925). Produces "Bone Collector's Bag" (69948). The combine does not fail.
18. dawnshroud/"Denns Rootenpaw", hand "Bone Collector's Bag" (69948). Requires `paladin_epic` ==5. Gives "Enchanted Bone Powder" (69949).
19. Hand "Enchanted Bone Powder" (69949) to letalis/"Drema Young". Spawns "Drema Young" (169128). Loot "Drema's Soulstone" (69928) from "Drema Young".
20. Loot "Soulstone Shard" (69950) from "Coterie Corruptor" in `tenebrous`.
21. Spawns "Shade of Mujaki the Devourer" (204081) in `ponightmare` on event death_complete:204080.
22. Loot "Soulstone Shard" (69951) from "Shade of Mujaki the Devourer".
23. Combine in "Drema's Soulstone" (69928): "Soulstone Shard" (69950), "Soulstone Shard" (69951). Produces "Drema's Soulstone" (69952). The combine does not fail.

### "Reiya's Soulstone" (69942)

1. Spawns "A Corrupted Koalindl" (69141) in `oot` on event_fish_success.
2. Loot "Corrupted Koalindl's Heart" (69929) from "A Corrupted Koalindl".
3. Spawns "A Corrupted Koalindl" (224432) in `gunthak` on event_fish_success.
4. Loot "Corrupted Koalindl's Heart" (69930) from "A Corrupted Koalindl".
5. Spawns "A Corrupted Koalindl" (93306) in `overthere` on event_fish_success.
6. Loot "Corrupted Koalindl's Heart" (69931) from "A Corrupted Koalindl".
7. Spawns "A Corrupted Koalindl" (182150) in `nedaria` on event_fish_success.
8. Loot "Corrupted Koalindl's Heart" (69932) from "A Corrupted Koalindl".
9. qeynos2/"Enic Ruklin", hand "Corrupted Koalindl's Heart" (69929) + "Corrupted Koalindl's Heart" (69930) + "Corrupted Koalindl's Heart" (69931) + "Corrupted Koalindl's Heart" (69932). Sets `paladin_epic` to `4`.
10. dawnshroud/"Mikhal Young", hand "Drema's Fingerbone" (69946). Sets `paladin_epic` to `5`.
11. dawnshroud/"Mikhal Young", say "Find Anything". Requires `paladin_epic` ==4. Gives "Drema's Locket" (69945).
12. letalis/"Drema Young", hand "Drema's Locket" (69945). Requires `paladin_epic` set. Requires `paladin_epic` >=4. Gives "Drema's Fingerbone" (69946).
13. abysmal/"Lovine Lemise", say "Ingredients". Requires `paladin_epic` ==5. Gives "Lovine's Potion Bag" (69922).
14. Loot "Ra'Tuk Screambringer's Jaw" (69921) from "A Ra'Tuk Screambringer" (NPC 283104) in `barindu`. Drop cache: 4.06% chance per kill.
15. Loot "Noc Fleshfeasters Tail" (69920) from "A Noc Fleshfeaster" in `riwwi`.
16. Loot "Mastruq Havocblade Blood" (69919) from "A Mastruq Havocblade" in `qinimi`.
17. Loot "Mastruq Havocblade Blood" (69919) from "A Mastruq Warfiend" in `qinimi`.
18. Loot "Potameid Seaweed Strands" (69918) from "An Entrapped Potameid" in `natimbi`.
19. Combine in "Lovine's Potion Bag" (69922): "Ra'Tuk Screambringer's Jaw" (69921), "Noc Fleshfeasters Tail" (69920), "Mastruq Havocblade Blood" (69919), "Potameid Seaweed Strands" (69918). Produces "Lovine's Potion Bag" (69923). The combine does not fail.
20. abysmal/"Lovine Lemise", hand "Lovine's Potion Bag" (69923). Sets `paladin_epic_reiya` to `1`.
21. Summon "Foldable Medicine Bag" (17770) by casting "Unfold Medicine Bag".
22. Common item: Fine Potion Vial (95846). Listed in 15 zones.
23. Loot "Robust Shadow Essence" (96911) from "Qua Senshali Xakra" (NPC 158020) in `vexthal`. Drop cache: 28.72% chance per kill.
24. Loot "Sage Leaf" (14215) from "a Di'zok Herbalist" in `chardok`.
25. Loot "Sage Leaf" (14215) from "a Sarnak Herb Collector" in `chardok`.
26. Loot "Sage Leaf" (14215) from "an Apprentice Herbalist" in `chardok`.
27. Loot "Valerian Root" (14230) from "a Di'zok Herbalist" in `chardok`.
28. Loot "Valerian Root" (14230) from "a Sarnak Herb Collector" in `chardok`.
29. Loot "Valerian Root" (14230) from "an Apprentice Herbalist" in `chardok`.
30. Common item: Woundwart (16526). Listed in 9 zones.
31. Combine in "Foldable Medicine Bag" (17770): "Fine Potion Vial" (95846), "Robust Shadow Essence" (96911), "Sage Leaf" (14215), "Valerian Root" (14230), "Woundwart" (16526). Produces "Mist of the Breathless" (96937). Requires Alchemy, trivial 224.
32. abysmal/"Reiya The Pained", hand "Mist of the Breathless" (96937). Requires `paladin_epic_reiya` ==1. Gives "Reiya's Soulstone" (69924).
33. Unresolved cyclic prerequisite: `mage_epic` >=9.
34. draniksscar/"Iilivina", say "Primals". Sets `mage_epic` to `10`.
35. Spawns "Shade of Reiya the Pained" (284104) in `ferubi` on enter.
36. Loot "Soulstone Shard" (69943) from "Shade of Reiya the Pained".
37. Loot "Soulstone Shard" (69944) from "Vuranish Xxuro" in `vxed`.
38. Combine in "Reiya's Soulstone" (69924): "Soulstone Shard" (69943), "Soulstone Shard" (69944). Produces "Reiya's Soulstone" (69942). The combine does not fail.

### "Fiery Defender" (10099)

1. Loot "Tainted Darksteel Sword" (29000) from "Keeper of the Tombs" in `hole`.
2. freeporteast/"Peasant Woman", say "I Will Take It". Gives "Bucket of Water" (29008).
3. freeporteast/"Joshua", hand "Bucket of Water" (29008). Gives "Bucket of Pure Water" (29009).
4. erudnext/"Reklon Gnallen", hand "Tainted Darksteel Sword" (29000) + "Bucket of Pure Water" (29009). Gives "Gleaming Crested Sword" (29003).
5. Loot "Tainted Darksteel Breastplate" (29001) from "Thought Destroyer" in `hateplaneb`.
6. kaladimb/"Nella Stonebraids", say "Dinner". Gives "Cold Plate of Beef and Bread" (29007).
7. kaladimb/"Jark", hand "Cold Plate of Beef and Bread" (29007). Gives "Pure Crystal" (29006).
8. erudnext/"Reklon Gnallen", hand "Tainted Darksteel Breastplate" (29001) + "Pure Crystal" (29006). Gives "Gleaming Crested Breastplate" (29004).
9. Loot "Tainted Darksteel Shield" (29002) from "Kirak Vil" in `nektulos`.
10. felwithea/"Elia The Pure", hand "Tainted Darksteel Shield" (29002). Gives "Gleaming Crested Shield" (29005).
11. erudnext/"Reklon Gnallen", hand "Gleaming Crested Sword" (29003) + "Gleaming Crested Breastplate" (29004) + "Gleaming Crested Shield" (29005). Gives "Mark of Atonement" (29010).
12. No quest step gives Drom's Champagne (13829). The dump lists it in freeporteast, freporte, highpasshold.
13. freeporteast/"Tykar Renlin", hand "Drom's Champagne" (13829) + "Drom's Champagne" (13829) + "Drom's Champagne" (13829) + "Drom's Champagne" (13829). Gives "Bunker Cell #1" (12196).
14. Summon "Black Diamond of Nightmares" (29990) by casting "Imbue Nightmare".
15. potranquility/"Elder Fuirstel", say "Hail". Sets `pop_cod_final` to `1`.
16. poknowledge/"Aid Grimel", say "Versed In The Art Of Smithing". Requires `pop_cod_final` ==1. Requires `pop_cod_final` set. Gives "Filthy Breastplate" (15984).
17. Combine in "Mixing Bowl" (17906): "Celestial Solvent" (9731), "Words of Acquisition (Beza)" (11866). Produces "Celestial Essence" (9650). Requires Baking, trivial 15. The combine does not fail.
18. Combine in "Mixing Bowl" (17906): "Celestial Solvent" (9731), "Words of Burnishing" (11862). Produces "Celestial Essence" (9650). Requires Baking, trivial 15. The combine does not fail.
19. 67 other recipes also produce Celestial Essence (9650).
20. Common item: Jar of Acid (22133). Listed in 15 zones.
21. Combine in Brew Barrel (19): "Celestial Essence" (9650), "Jar of Acid" (22133). Produces "Acid Wash" (15987). Requires Brewing, trivial 151.
22. Combine in Forge (17): "Filthy Breastplate" (15984), "Acid Wash" (15987). Produces "Cleansed Breastplate" (15998). Requires Blacksmithing, trivial 227.
23. Common item: Mortar and Pestle (17904). Listed in 12 zones.
24. Loot "Sandstorm Pearl" (29909) from "Rorek Steelthorn" (NPC 209081) in `bothunder`. Drop cache: 5.33% chance per kill.
25. Combine in "Mortar and Pestle" (17904): "Sandstorm Pearl" (29909). Produces "Powdered Sandstorm Pearl" (29520) x4. Requires Make Poison, trivial 255.
26. Common item: Firing Sheet (16906). Listed in 34 zones.
27. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
28. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `steamfont`.
29. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `tox`.
30. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `toxxulia`.
31. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
32. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). The combine does not fail.
33. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
34. Say "Tm Devrak Death" to rujd/"Rujd".
35. Spawns "spawn chest with Heavy Orcish Prison Key" (245241).
36. Loot "Pod of Water" (13044) from "spawn chest with Heavy Orcish Prison Key".
37. 6 alternative loot source(s) also yield Pod of Water (13044).
38. Forage "Pod of Water" (13044) in `ruja`.
39. Forage "Pod of Water" (13044) in `uqua`.
40. Forage "Pod of Water" (13044) in `yxtta`.
41. Combine in Brew Barrel (19): "Bottle of Aged Bloodwine" (51163), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aged Bloodwine" (51164). Requires Brewing, trivial 255.
42. Combine in Brew Barrel (19): "Bottle of Aldo's Bitter Ale" (75805), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aldo's Bitter Ale" (75811). Requires Brewing, trivial 15.
43. 17 other recipes also produce Bottle (16598).
44. Combine in Brew Barrel (19): "Pod of Water" (13044), "Bottle" (16598). Produces "Water Flask" (13006). Requires Brewing, trivial 21.
45. Combine in Pottery Wheel (21): "Water Flask" (13006), "Block of Clay" (16901). Produces "Small Block of Clay" (16900) x3. Requires Pottery, trivial 21.
46. Combine in Pottery Wheel (21): "Small Block of Clay" (16900), "Water Flask" (13006). Produces "Block of Clay" (16901). Requires Pottery, trivial 21.
47. Combine in Pottery Wheel (21): "Water Flask" (13006), "Large Block of Clay" (16902). Produces "Block of Clay" (16901) x2. Requires Pottery, trivial 21.
48. Combine in Pottery Wheel (21): "Block of Clay" (16901), "Water Flask" (13006). Produces "Large Block of Clay" (16902). Requires Pottery, trivial 21.
49. Common item: Large Bowl Sketch (16963). Listed in 29 zones.
50. Combine in Pottery Wheel (21): "Large Block of Clay" (16902), "Water Flask" (13006), "Large Bowl Sketch" (16963). Produces "Unfired Mixing Bowl" (16930). Requires Pottery, trivial 128.
51. Combine in Kiln (22): "Firing Sheet" (16906), "Unfired Mixing Bowl" (16930). Produces "Mixing Bowl" (17906). Requires Pottery, trivial 15.
52. Combine in "Mixing Bowl" (17906): "Sandstorm Pearl" (29909). Produces "Powdered Sandstorm Pearl" (29520) x4. Requires Baking. The combine does not fail.
53. Spawns "a Koka'Vor chieftain" (210236) in `postorms` on event_signal.
54. Loot "Storm Rider Blood" (29526) from "a Koka'Vor chieftain".
55. Loot "Drop of Pure Rain" (29904) from "A vann stav" (NPC 209018) in `bothunder`. Drop cache: 4% chance per kill.
56. Combine in Brew Barrel (19): "Powdered Sandstorm Pearl" (29520), "Storm Rider Blood" (29526), "Drop of Pure Rain" (29904). Produces "Hurricane Temper" (29533). Requires Brewing, trivial 135.
57. Combine in Forge (17): "Cleansed Breastplate" (15998), "Hurricane Temper" (29533). Produces "Tempered Breastplate" (15999). Requires Blacksmithing, trivial 229.
58. Combine in Forge (17): "Black Diamond of Nightmares" (29990), "Tempered Breastplate" (15999). Produces "Imbued Breastplate" (15985). Requires Blacksmithing 220. Trivial at 275.
59. poknowledge/"Aid Grimel", hand "Imbued Breastplate" (15985). Gives "Hardened Leather Signet" (16249).
60. poknowledge/"Aid Grimel", say "Skill In Brewing". Requires `pop_cod_final` ==1. Requires `pop_cod_final` set. Gives "Portable Drink Barrel" (17179).
61. Loot "Snake Scales" (13070) from "A Kerra Snake" (NPC 98017) in `erudsxing`. Drop cache: 59.23% chance per kill.
62. Combine in "Portable Drink Barrel" (17179): "Water Flask" (13006), "Snake Scales" (13070), "Bottle" (16598). Produces "Bog Juice" (16581). Requires Brewing, trivial 21.
63. Common item: Spit (17947). Listed in 34 zones.
64. Loot "Fire Beetle Eye" (10307) from "A Klicnik Drone" (NPC 2021) in `qeynos2`. Drop cache: 100% chance per kill.
65. Spawns "Sepsis Rat" (45113) in `qcat` on event_death.
66. Loot "Rat Ears" (13072) from "Sepsis Rat".
67. 2 alternative loot source(s) also yield Rat Ears (13072).
68. Combine in "Spit" (17947): "Fire Beetle Eye" (10307), "Rat Ears" (13072). Produces "Edible Goo" (13498). Requires Baking, trivial 21.
69. freeporteast/"A Prisoner", hand "Bunker Cell #1" (12196) + "Edible Goo" (13498) + "Bog Juice" (16581). Gives "H. K. 102" (12143).
70. highkeep/"Assistant Kiolna", hand "H. K. 102" (12143). Gives "Sealed Note" (18936).
71. paw/"Brother Hayle", hand "Sealed Note" (18936). Gives "Note" (18937).
72. Kill freportw/"Sir Lucan D-Lere". Spawns "Sir Lucan D'Lere" (9147).
73. Loot "Testimony of Truth" (18827) from "Sir Lucan D'Lere".
74. freeportwest/"Valeron Dushire", hand "Testimony of Truth" (18827). Gives "Brilliant Sword of Faith" (13947).
75. Loot "Spider Venom Sac" (14018) from "Stone Spider" (NPC 32057) in `soldungb`. Drop cache: 51% chance per kill.
76. freeportwest/"Merko Quetalis", hand "Spider Venom Sac" (14018). Gives "Token of Bravery" (12144).
77. **Broken:** nothing in the graph gives, loots, spawns, or combines Blackbox XIVD (13344).
78. akanon/"Baxok Curhunter", hand "Blackbox XIVD" (13344). Gives "Cloth Shirt" (1004).
79. commonlands/"Altunic Jartin", hand "Cloth Shirt" (1004). Gives "Token of Generosity" (13865).
80. Hand "Token of Bravery" (12144) + "Token of Generosity" (13865) to freeportwest/"Merko Quetalis". Spawns "spawns Guard Willia" (383270). Loot "Token of Truth" (13866) from "spawns Guard Willia".
81. 1 alternative loot source(s) also yield Token of Truth (13866).
82. freeportwest/"Merko Quetalis", hand "Token of Truth" (13866). Gives "Testimony" (18828).
83. Loot "Glowing Sword Hilt" (12197) from "Xicotl" in `mistmoore`.
84. paw/"Brother Hayle", hand "Glowing Sword Hilt" (12197) + "Brilliant Sword of Faith" (13947) + "Testimony" (18828) + "Note" (18937). Gives "SoulFire" (5504).
85. airplane/"Inte Akera", hand "SoulFire" (5504). Gives "Inte's First Blessing" (18033).
86. neriakc/"Selzar L-Crit", say "Armor". Gives "Note to Kanthuk" (2416).
87. butcher/"Kanthuk Ogrebane", hand "Note to Kanthuk" (2416). Sets `Kanthuk` to `ghoul`.
88. butcher/"Kanthuk Ogrebane", say "Strange Image". Requires `Kanthuk` set. Gives "Pendant" (2414).
89. cauldron/"Llara", hand "Pendant" (2414). Sets `Llara` to `ghoul`.
90. cauldron/"Llara", say "Ruathey". Requires `Llara` set. Gives "Note to Ruathey" (2417).
91. lavastorm/"Ruathey", hand "Note to Ruathey" (2417). Sets `Ruathey` to `ghoul`.
92. lavastorm/"Ruathey", hand "Note to Ruathey" (2417). Sets `ruathey_note` to `1`.
93. lavastorm/"Ruathey", say "Bag". Requires `Ruathey` set. Requires `ruathey_note` ==1. Requires `ruathey_note` set. Gives "Nobleman's Bag" (17878).
94. Loot "Ghoul's Heart" (2410) from "A Ghoul" (NPC 63011) in `unrest`. Drop cache: 25% chance per kill.
95. Loot "Amstaf's Scroll" (2411) from "A Goblin Thief" (NPC 6150) in `highkeep`. Drop cache: 35% chance per kill.
96. Loot "Blade of Nobility" (2412) from "A Crazed Goblin" (NPC 68162) in `butcher`. Drop cache: 10.57% chance per kill.
97. Loot "Hilt of the Nobleman" (2413) from "Ekeros" in `najena`.
98. Loot "Hilt of the Nobleman" (2413) from "A Skeleton" in `najena`.
99. Combine in "Nobleman's Bag" (17878): "Ghoul's Heart" (2410), "Amstaf's Scroll" (2411), "Blade of Nobility" (2412), "Hilt of the Nobleman" (2413). Produces "Ghoulbane" (5403). The combine does not fail.
100. airplane/"Inte Akera", hand "Ghoulbane" (5403). Gives "Inte's Second Blessing" (18034).
101. Loot "Torn, Burnt Book" (19071) from "Lord Nagafen" in `soldungb`.
102. Loot "Torn, Burnt Book" (19071) from "Melalafen" in `westwastes`.
103. Loot "Torn, Burnt Book" (19071) from "Severilous" in `emeraldjungle`.
104. Loot "Torn, Burnt Book" (19071) from "Talendor" in `skyfire`.
105. Loot "Torn, Burnt Book" (19071) from "The Fabled Severilous".
106. Loot "Torn, Frost-covered Book" (19070) from "Faydedar" in `timorous`.
107. Loot "Torn, Frost-covered Book" (19070) from "Gorenaire" in `dreadlands`.
108. Loot "Torn, Frost-covered Book" (19070) from "Lady Vox" in `permafrost`.
109. neriakb/"Rysva To-Biath", hand "Torn, Frost-covered Book" (19070) + "Torn, Burnt Book" (19071). Gives "Book of Scale" (18302).
110. oceanoftears/"Oracle Of K-Arnon", hand "Book of Scale" (18302). Gives "Miragul's Phylactery" (19072).
111. Hand "Miragul's Phylactery" (19072) to everfrost/"Lich Of Miragul". Spawns "Spawn Miragul" (30094). Loot "Miragul's Head" (19073) from "Spawn Miragul".
112. Hand "Miragul's Phylactery" (19072) to everfrost/"Lich Of Miragul". Spawns "Spawn Miragul" (30094). Loot "Miragul's Robe" (1254) from "Spawn Miragul".
113. airplane/"Inte Akera", hand "Miragul's Robe" (1254) + "Inte's First Blessing" (18033) + "Inte's Second Blessing" (18034) + "Miragul's Head" (19073). Gives "Fiery Avenger" (11050).
114. fearplane/"Irak Altil", hand "Fiery Avenger" (11050) + "Mark of Atonement" (29010). Gives "Fiery Defender" (10099).

### "Couragebringer" (69913)

1. povalor/"Baltron Werters", say "Couragebringer". Sets `pre_pal` to `1`.
2. povalor/"Baltron Werters", say "Couragebringer". Requires `pre_pal` unset. Gives "Baltron's Solvent" (69901).
3. sro/"Gilfal", hand "Baltron's Solvent" (69901). Sets `pre_pal` to `2`.
4. Ground spawn of "Rune of Xor" (69909) in `potranquility`.
5. Ground spawn of "Rune of Yirno" (69908) in `mistmoore`.
6. Ground spawn of "Rune of Zota" (69907) in `scarlet`.
7. Ground spawn of "Rune Wilun" (69910) in `gunthak`.
8. everfrost/"Rombus", hand "Rune of Zota" (69907) + "Rune of Yirno" (69908) + "Rune of Xor" (69909) + "Rune Wilun" (69910). Sets `pre_pal` to `3`.
9. sro/"Gilfal", hand "Baltron's Solvent" (69901). Requires `pre_pal` ==1. Gives "Gilfal's Scabbard" (69902).
10. Spawns "Neffiken Lord Kelek-Vor" (210229) in `postorms` on event_signal.
11. Loot "Broken Sword Piece" (69903) from "Neffiken Lord Kelek-Vor".
12. Encounter starts when NPC 186196 spawns in `hateplaneb`.
13. Starts timer `popmaestro`.
14. Spawns "Maestro of Rancor" (186111) after `hateplaneb/maestro#timer:popmaestro`.
15. Loot "Broken Sword Piece" (69904) from "Maestro of Rancor".
16. Loot "Broken Sword Piece" (69905) from "Kaniz Painbringer" in `potorment`.
17. everfrost/"Rombus", hand "Rune of Zota" (69907) + "Rune of Yirno" (69908) + "Rune of Xor" (69909) + "Rune Wilun" (69910). Requires `pre_pal` ==2. Gives "Broken Sword Piece" (69906).
18. Combine in "Gilfal's Scabbard" (69902): "Broken Sword Piece" (69903), "Broken Sword Piece" (69904), "Broken Sword Piece" (69905), "Broken Sword Piece" (69906). Produces "Fractured Couragebringer" (69911). The combine does not fail.
19. sro/"Gilfal", hand "Fractured Couragebringer" (69911). Sets `pre_pal` to `4`.
20. sro/"Gilfal", hand "Fractured Couragebringer" (69911). Requires `pre_pal` ==3. Gives "Fractured Couragebringer" (69912).
21. povalor/"Baltron Werters", hand "Fractured Couragebringer" (69912). Requires `pre_pal` ==4. Gives "Couragebringer" (69913).

### "Drema's Fingerbone" (69946)

1. Spawns "A Corrupted Koalindl" (69141) in `oot` on event_fish_success.
2. Loot "Corrupted Koalindl's Heart" (69929) from "A Corrupted Koalindl".
3. Spawns "A Corrupted Koalindl" (224432) in `gunthak` on event_fish_success.
4. Loot "Corrupted Koalindl's Heart" (69930) from "A Corrupted Koalindl".
5. Spawns "A Corrupted Koalindl" (93306) in `overthere` on event_fish_success.
6. Loot "Corrupted Koalindl's Heart" (69931) from "A Corrupted Koalindl".
7. Spawns "A Corrupted Koalindl" (182150) in `nedaria` on event_fish_success.
8. Loot "Corrupted Koalindl's Heart" (69932) from "A Corrupted Koalindl".
9. qeynos2/"Enic Ruklin", hand "Corrupted Koalindl's Heart" (69929) + "Corrupted Koalindl's Heart" (69930) + "Corrupted Koalindl's Heart" (69931) + "Corrupted Koalindl's Heart" (69932). Sets `paladin_epic` to `4`.
10. dawnshroud/"Mikhal Young", hand "Drema's Fingerbone" (69946). Sets `paladin_epic` to `5`.
11. dawnshroud/"Mikhal Young", say "Find Anything". Requires `paladin_epic` ==4. Gives "Drema's Locket" (69945).
12. letalis/"Drema Young", hand "Drema's Locket" (69945). Requires `paladin_epic` set. Requires `paladin_epic` >=4. Gives "Drema's Fingerbone" (69946).

### "Dark and Twisted Sword" (69972)

1. Spawns "A Corrupted Koalindl" (69141) in `oot` on event_fish_success.
2. Loot "Corrupted Koalindl's Heart" (69929) from "A Corrupted Koalindl".
3. Spawns "A Corrupted Koalindl" (224432) in `gunthak` on event_fish_success.
4. Loot "Corrupted Koalindl's Heart" (69930) from "A Corrupted Koalindl".
5. Spawns "A Corrupted Koalindl" (93306) in `overthere` on event_fish_success.
6. Loot "Corrupted Koalindl's Heart" (69931) from "A Corrupted Koalindl".
7. Spawns "A Corrupted Koalindl" (182150) in `nedaria` on event_fish_success.
8. Loot "Corrupted Koalindl's Heart" (69932) from "A Corrupted Koalindl".
9. qeynos2/"Enic Ruklin", hand "Corrupted Koalindl's Heart" (69929) + "Corrupted Koalindl's Heart" (69930) + "Corrupted Koalindl's Heart" (69931) + "Corrupted Koalindl's Heart" (69932). Sets `paladin_epic` to `4`.
10. qeynos2/"Enic Ruklin", hand "Corrupted Koalindl's Heart" (69929) + "Corrupted Koalindl's Heart" (69930) + "Corrupted Koalindl's Heart" (69931) + "Corrupted Koalindl's Heart" (69932). Gives "Seal of Enic" (69933).
11. Say "Hail" to skyfire/"Dry Sapara".
12. Spawns "Rithnok the Tormented" (91193).
13. Loot "Rithnok's Soulstone" (69935) from "Rithnok the Tormented".
14. skyfire/"Dry Sapara", hand "Rithnok's Soulstone" (69935). Gives "Rithnok's Soulstone" (69936).
15. Ground spawn of "Soulstone Shard" (69937) in `draniksscar`.
16. Ground spawn of "Soulstone Shard" (69938) in `bloodfields`.
17. Ground spawn of "Soulstone Shard" (69939) in `causeway`.
18. Ground spawn of "Soulstone Shard" (69940) in `dranik`.
19. Combine in "Rithnok's Soulstone" (69936): "Soulstone Shard" (69937), "Soulstone Shard" (69938), "Soulstone Shard" (69939), "Soulstone Shard" (69940). Produces "Rithnok's Soulstone" (69941). The combine does not fail.
20. dawnshroud/"Mikhal Young", hand "Drema's Fingerbone" (69946). Sets `paladin_epic` to `5`.
21. dawnshroud/"Mikhal Young", say "Find Anything". Requires `paladin_epic` ==4. Gives "Drema's Locket" (69945).
22. letalis/"Drema Young", hand "Drema's Locket" (69945). Requires `paladin_epic` set. Requires `paladin_epic` >=4. Gives "Drema's Fingerbone" (69946).
23. dawnshroud/"Denns Rootenpaw", hand "Drema's Fingerbone" (69946). Requires `paladin_epic` ==5. Gives "Bone Collector's Bag" (69947).
24. Loot "Dark Skeleton Remains" (69927) from "A Sun Revenant" in `thegrey`.
25. Loot "Dark Skeleton Remains" (69926) from "Disturbed Elysian Remains" (NPC 176016) in `umbral`. Drop cache: 2.58% chance per kill.
26. Loot "Dark Skeleton Remains" (69925) from "A Soriz Slave" (NPC 162029) in `ssratemple`. Drop cache: 35% chance per kill.
27. Combine in "Bone Collector's Bag" (69947): "Dark Skeleton Remains" (69927), "Dark Skeleton Remains" (69926), "Dark Skeleton Remains" (69925). Produces "Bone Collector's Bag" (69948). The combine does not fail.
28. dawnshroud/"Denns Rootenpaw", hand "Bone Collector's Bag" (69948). Requires `paladin_epic` ==5. Gives "Enchanted Bone Powder" (69949).
29. Hand "Enchanted Bone Powder" (69949) to letalis/"Drema Young". Spawns "Drema Young" (169128). Loot "Drema's Soulstone" (69928) from "Drema Young".
30. Loot "Soulstone Shard" (69950) from "Coterie Corruptor" in `tenebrous`.
31. Spawns "Shade of Mujaki the Devourer" (204081) in `ponightmare` on event death_complete:204080.
32. Loot "Soulstone Shard" (69951) from "Shade of Mujaki the Devourer".
33. Combine in "Drema's Soulstone" (69928): "Soulstone Shard" (69950), "Soulstone Shard" (69951). Produces "Drema's Soulstone" (69952). The combine does not fail.
34. abysmal/"Lovine Lemise", say "Ingredients". Requires `paladin_epic` ==5. Gives "Lovine's Potion Bag" (69922).
35. Loot "Ra'Tuk Screambringer's Jaw" (69921) from "A Ra'Tuk Screambringer" (NPC 283104) in `barindu`. Drop cache: 4.06% chance per kill.
36. Loot "Noc Fleshfeasters Tail" (69920) from "A Noc Fleshfeaster" in `riwwi`.
37. Loot "Mastruq Havocblade Blood" (69919) from "A Mastruq Havocblade" in `qinimi`.
38. Loot "Mastruq Havocblade Blood" (69919) from "A Mastruq Warfiend" in `qinimi`.
39. Loot "Potameid Seaweed Strands" (69918) from "An Entrapped Potameid" in `natimbi`.
40. Combine in "Lovine's Potion Bag" (69922): "Ra'Tuk Screambringer's Jaw" (69921), "Noc Fleshfeasters Tail" (69920), "Mastruq Havocblade Blood" (69919), "Potameid Seaweed Strands" (69918). Produces "Lovine's Potion Bag" (69923). The combine does not fail.
41. abysmal/"Lovine Lemise", hand "Lovine's Potion Bag" (69923). Sets `paladin_epic_reiya` to `1`.
42. Summon "Foldable Medicine Bag" (17770) by casting "Unfold Medicine Bag".
43. Common item: Fine Potion Vial (95846). Listed in 15 zones.
44. Loot "Robust Shadow Essence" (96911) from "Qua Senshali Xakra" (NPC 158020) in `vexthal`. Drop cache: 28.72% chance per kill.
45. Loot "Sage Leaf" (14215) from "a Di'zok Herbalist" in `chardok`.
46. Loot "Sage Leaf" (14215) from "a Sarnak Herb Collector" in `chardok`.
47. Loot "Sage Leaf" (14215) from "an Apprentice Herbalist" in `chardok`.
48. Loot "Valerian Root" (14230) from "a Di'zok Herbalist" in `chardok`.
49. Loot "Valerian Root" (14230) from "a Sarnak Herb Collector" in `chardok`.
50. Loot "Valerian Root" (14230) from "an Apprentice Herbalist" in `chardok`.
51. Common item: Woundwart (16526). Listed in 9 zones.
52. Combine in "Foldable Medicine Bag" (17770): "Fine Potion Vial" (95846), "Robust Shadow Essence" (96911), "Sage Leaf" (14215), "Valerian Root" (14230), "Woundwart" (16526). Produces "Mist of the Breathless" (96937). Requires Alchemy, trivial 224.
53. abysmal/"Reiya The Pained", hand "Mist of the Breathless" (96937). Requires `paladin_epic_reiya` ==1. Gives "Reiya's Soulstone" (69924).
54. Unresolved cyclic prerequisite: `mage_epic` >=9.
55. draniksscar/"Iilivina", say "Primals". Sets `mage_epic` to `10`.
56. Spawns "Shade of Reiya the Pained" (284104) in `ferubi` on enter.
57. Loot "Soulstone Shard" (69943) from "Shade of Reiya the Pained".
58. Loot "Soulstone Shard" (69944) from "Vuranish Xxuro" in `vxed`.
59. Combine in "Reiya's Soulstone" (69924): "Soulstone Shard" (69943), "Soulstone Shard" (69944). Produces "Reiya's Soulstone" (69942). The combine does not fail.
60. Loot "Tainted Darksteel Sword" (29000) from "Keeper of the Tombs" in `hole`.
61. freeporteast/"Peasant Woman", say "I Will Take It". Gives "Bucket of Water" (29008).
62. freeporteast/"Joshua", hand "Bucket of Water" (29008). Gives "Bucket of Pure Water" (29009).
63. erudnext/"Reklon Gnallen", hand "Tainted Darksteel Sword" (29000) + "Bucket of Pure Water" (29009). Gives "Gleaming Crested Sword" (29003).
64. Loot "Tainted Darksteel Breastplate" (29001) from "Thought Destroyer" in `hateplaneb`.
65. kaladimb/"Nella Stonebraids", say "Dinner". Gives "Cold Plate of Beef and Bread" (29007).
66. kaladimb/"Jark", hand "Cold Plate of Beef and Bread" (29007). Gives "Pure Crystal" (29006).
67. erudnext/"Reklon Gnallen", hand "Tainted Darksteel Breastplate" (29001) + "Pure Crystal" (29006). Gives "Gleaming Crested Breastplate" (29004).
68. Loot "Tainted Darksteel Shield" (29002) from "Kirak Vil" in `nektulos`.
69. felwithea/"Elia The Pure", hand "Tainted Darksteel Shield" (29002). Gives "Gleaming Crested Shield" (29005).
70. erudnext/"Reklon Gnallen", hand "Gleaming Crested Sword" (29003) + "Gleaming Crested Breastplate" (29004) + "Gleaming Crested Shield" (29005). Gives "Mark of Atonement" (29010).
71. No quest step gives Drom's Champagne (13829). The dump lists it in freeporteast, freporte, highpasshold.
72. freeporteast/"Tykar Renlin", hand "Drom's Champagne" (13829) + "Drom's Champagne" (13829) + "Drom's Champagne" (13829) + "Drom's Champagne" (13829). Gives "Bunker Cell #1" (12196).
73. Summon "Black Diamond of Nightmares" (29990) by casting "Imbue Nightmare".
74. potranquility/"Elder Fuirstel", say "Hail". Sets `pop_cod_final` to `1`.
75. poknowledge/"Aid Grimel", say "Versed In The Art Of Smithing". Requires `pop_cod_final` ==1. Requires `pop_cod_final` set. Gives "Filthy Breastplate" (15984).
76. Combine in "Mixing Bowl" (17906): "Celestial Solvent" (9731), "Words of Acquisition (Beza)" (11866). Produces "Celestial Essence" (9650). Requires Baking, trivial 15. The combine does not fail.
77. Combine in "Mixing Bowl" (17906): "Celestial Solvent" (9731), "Words of Burnishing" (11862). Produces "Celestial Essence" (9650). Requires Baking, trivial 15. The combine does not fail.
78. 67 other recipes also produce Celestial Essence (9650).
79. Common item: Jar of Acid (22133). Listed in 15 zones.
80. Combine in Brew Barrel (19): "Celestial Essence" (9650), "Jar of Acid" (22133). Produces "Acid Wash" (15987). Requires Brewing, trivial 151.
81. Combine in Forge (17): "Filthy Breastplate" (15984), "Acid Wash" (15987). Produces "Cleansed Breastplate" (15998). Requires Blacksmithing, trivial 227.
82. Common item: Mortar and Pestle (17904). Listed in 12 zones.
83. Loot "Sandstorm Pearl" (29909) from "Rorek Steelthorn" (NPC 209081) in `bothunder`. Drop cache: 5.33% chance per kill.
84. Combine in "Mortar and Pestle" (17904): "Sandstorm Pearl" (29909). Produces "Powdered Sandstorm Pearl" (29520) x4. Requires Make Poison, trivial 255.
85. Common item: Firing Sheet (16906). Listed in 34 zones.
86. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
87. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `steamfont`.
88. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `tox`.
89. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `toxxulia`.
90. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
91. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). The combine does not fail.
92. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
93. Say "Tm Devrak Death" to rujd/"Rujd".
94. Spawns "spawn chest with Heavy Orcish Prison Key" (245241).
95. Loot "Pod of Water" (13044) from "spawn chest with Heavy Orcish Prison Key".
96. 6 alternative loot source(s) also yield Pod of Water (13044).
97. Forage "Pod of Water" (13044) in `ruja`.
98. Forage "Pod of Water" (13044) in `uqua`.
99. Forage "Pod of Water" (13044) in `yxtta`.
100. Combine in Brew Barrel (19): "Bottle of Aged Bloodwine" (51163), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aged Bloodwine" (51164). Requires Brewing, trivial 255.
101. Combine in Brew Barrel (19): "Bottle of Aldo's Bitter Ale" (75805), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aldo's Bitter Ale" (75811). Requires Brewing, trivial 15.
102. 17 other recipes also produce Bottle (16598).
103. Combine in Brew Barrel (19): "Pod of Water" (13044), "Bottle" (16598). Produces "Water Flask" (13006). Requires Brewing, trivial 21.
104. Combine in Pottery Wheel (21): "Water Flask" (13006), "Block of Clay" (16901). Produces "Small Block of Clay" (16900) x3. Requires Pottery, trivial 21.
105. Combine in Pottery Wheel (21): "Small Block of Clay" (16900), "Water Flask" (13006). Produces "Block of Clay" (16901). Requires Pottery, trivial 21.
106. Combine in Pottery Wheel (21): "Water Flask" (13006), "Large Block of Clay" (16902). Produces "Block of Clay" (16901) x2. Requires Pottery, trivial 21.
107. Combine in Pottery Wheel (21): "Block of Clay" (16901), "Water Flask" (13006). Produces "Large Block of Clay" (16902). Requires Pottery, trivial 21.
108. Common item: Large Bowl Sketch (16963). Listed in 29 zones.
109. Combine in Pottery Wheel (21): "Large Block of Clay" (16902), "Water Flask" (13006), "Large Bowl Sketch" (16963). Produces "Unfired Mixing Bowl" (16930). Requires Pottery, trivial 128.
110. Combine in Kiln (22): "Firing Sheet" (16906), "Unfired Mixing Bowl" (16930). Produces "Mixing Bowl" (17906). Requires Pottery, trivial 15.
111. Combine in "Mixing Bowl" (17906): "Sandstorm Pearl" (29909). Produces "Powdered Sandstorm Pearl" (29520) x4. Requires Baking. The combine does not fail.
112. Spawns "a Koka'Vor chieftain" (210236) in `postorms` on event_signal.
113. Loot "Storm Rider Blood" (29526) from "a Koka'Vor chieftain".
114. Loot "Drop of Pure Rain" (29904) from "A vann stav" (NPC 209018) in `bothunder`. Drop cache: 4% chance per kill.
115. Combine in Brew Barrel (19): "Powdered Sandstorm Pearl" (29520), "Storm Rider Blood" (29526), "Drop of Pure Rain" (29904). Produces "Hurricane Temper" (29533). Requires Brewing, trivial 135.
116. Combine in Forge (17): "Cleansed Breastplate" (15998), "Hurricane Temper" (29533). Produces "Tempered Breastplate" (15999). Requires Blacksmithing, trivial 229.
117. Combine in Forge (17): "Black Diamond of Nightmares" (29990), "Tempered Breastplate" (15999). Produces "Imbued Breastplate" (15985). Requires Blacksmithing 220. Trivial at 275.
118. poknowledge/"Aid Grimel", hand "Imbued Breastplate" (15985). Gives "Hardened Leather Signet" (16249).
119. poknowledge/"Aid Grimel", say "Skill In Brewing". Requires `pop_cod_final` ==1. Requires `pop_cod_final` set. Gives "Portable Drink Barrel" (17179).
120. Loot "Snake Scales" (13070) from "A Kerra Snake" (NPC 98017) in `erudsxing`. Drop cache: 59.23% chance per kill.
121. Combine in "Portable Drink Barrel" (17179): "Water Flask" (13006), "Snake Scales" (13070), "Bottle" (16598). Produces "Bog Juice" (16581). Requires Brewing, trivial 21.
122. Common item: Spit (17947). Listed in 34 zones.
123. Loot "Fire Beetle Eye" (10307) from "A Klicnik Drone" (NPC 2021) in `qeynos2`. Drop cache: 100% chance per kill.
124. Spawns "Sepsis Rat" (45113) in `qcat` on event_death.
125. Loot "Rat Ears" (13072) from "Sepsis Rat".
126. 2 alternative loot source(s) also yield Rat Ears (13072).
127. Combine in "Spit" (17947): "Fire Beetle Eye" (10307), "Rat Ears" (13072). Produces "Edible Goo" (13498). Requires Baking, trivial 21.
128. freeporteast/"A Prisoner", hand "Bunker Cell #1" (12196) + "Edible Goo" (13498) + "Bog Juice" (16581). Gives "H. K. 102" (12143).
129. highkeep/"Assistant Kiolna", hand "H. K. 102" (12143). Gives "Sealed Note" (18936).
130. paw/"Brother Hayle", hand "Sealed Note" (18936). Gives "Note" (18937).
131. Kill freportw/"Sir Lucan D-Lere". Spawns "Sir Lucan D'Lere" (9147).
132. Loot "Testimony of Truth" (18827) from "Sir Lucan D'Lere".
133. freeportwest/"Valeron Dushire", hand "Testimony of Truth" (18827). Gives "Brilliant Sword of Faith" (13947).
134. Loot "Spider Venom Sac" (14018) from "Stone Spider" (NPC 32057) in `soldungb`. Drop cache: 51% chance per kill.
135. freeportwest/"Merko Quetalis", hand "Spider Venom Sac" (14018). Gives "Token of Bravery" (12144).
136. **Broken:** nothing in the graph gives, loots, spawns, or combines Blackbox XIVD (13344).
137. akanon/"Baxok Curhunter", hand "Blackbox XIVD" (13344). Gives "Cloth Shirt" (1004).
138. commonlands/"Altunic Jartin", hand "Cloth Shirt" (1004). Gives "Token of Generosity" (13865).
139. Hand "Token of Bravery" (12144) + "Token of Generosity" (13865) to freeportwest/"Merko Quetalis". Spawns "spawns Guard Willia" (383270). Loot "Token of Truth" (13866) from "spawns Guard Willia".
140. 1 alternative loot source(s) also yield Token of Truth (13866).
141. freeportwest/"Merko Quetalis", hand "Token of Truth" (13866). Gives "Testimony" (18828).
142. Loot "Glowing Sword Hilt" (12197) from "Xicotl" in `mistmoore`.
143. paw/"Brother Hayle", hand "Glowing Sword Hilt" (12197) + "Brilliant Sword of Faith" (13947) + "Testimony" (18828) + "Note" (18937). Gives "SoulFire" (5504).
144. airplane/"Inte Akera", hand "SoulFire" (5504). Gives "Inte's First Blessing" (18033).
145. neriakc/"Selzar L-Crit", say "Armor". Gives "Note to Kanthuk" (2416).
146. butcher/"Kanthuk Ogrebane", hand "Note to Kanthuk" (2416). Sets `Kanthuk` to `ghoul`.
147. butcher/"Kanthuk Ogrebane", say "Strange Image". Requires `Kanthuk` set. Gives "Pendant" (2414).
148. cauldron/"Llara", hand "Pendant" (2414). Sets `Llara` to `ghoul`.
149. cauldron/"Llara", say "Ruathey". Requires `Llara` set. Gives "Note to Ruathey" (2417).
150. lavastorm/"Ruathey", hand "Note to Ruathey" (2417). Sets `Ruathey` to `ghoul`.
151. lavastorm/"Ruathey", hand "Note to Ruathey" (2417). Sets `ruathey_note` to `1`.
152. lavastorm/"Ruathey", say "Bag". Requires `Ruathey` set. Requires `ruathey_note` ==1. Requires `ruathey_note` set. Gives "Nobleman's Bag" (17878).
153. Loot "Ghoul's Heart" (2410) from "A Ghoul" (NPC 63011) in `unrest`. Drop cache: 25% chance per kill.
154. Loot "Amstaf's Scroll" (2411) from "A Goblin Thief" (NPC 6150) in `highkeep`. Drop cache: 35% chance per kill.
155. Loot "Blade of Nobility" (2412) from "A Crazed Goblin" (NPC 68162) in `butcher`. Drop cache: 10.57% chance per kill.
156. Loot "Hilt of the Nobleman" (2413) from "Ekeros" in `najena`.
157. Loot "Hilt of the Nobleman" (2413) from "A Skeleton" in `najena`.
158. Combine in "Nobleman's Bag" (17878): "Ghoul's Heart" (2410), "Amstaf's Scroll" (2411), "Blade of Nobility" (2412), "Hilt of the Nobleman" (2413). Produces "Ghoulbane" (5403). The combine does not fail.
159. airplane/"Inte Akera", hand "Ghoulbane" (5403). Gives "Inte's Second Blessing" (18034).
160. Loot "Torn, Burnt Book" (19071) from "Lord Nagafen" in `soldungb`.
161. Loot "Torn, Burnt Book" (19071) from "Melalafen" in `westwastes`.
162. Loot "Torn, Burnt Book" (19071) from "Severilous" in `emeraldjungle`.
163. Loot "Torn, Burnt Book" (19071) from "Talendor" in `skyfire`.
164. Loot "Torn, Burnt Book" (19071) from "The Fabled Severilous".
165. Loot "Torn, Frost-covered Book" (19070) from "Faydedar" in `timorous`.
166. Loot "Torn, Frost-covered Book" (19070) from "Gorenaire" in `dreadlands`.
167. Loot "Torn, Frost-covered Book" (19070) from "Lady Vox" in `permafrost`.
168. neriakb/"Rysva To-Biath", hand "Torn, Frost-covered Book" (19070) + "Torn, Burnt Book" (19071). Gives "Book of Scale" (18302).
169. oceanoftears/"Oracle Of K-Arnon", hand "Book of Scale" (18302). Gives "Miragul's Phylactery" (19072).
170. Hand "Miragul's Phylactery" (19072) to everfrost/"Lich Of Miragul". Spawns "Spawn Miragul" (30094). Loot "Miragul's Head" (19073) from "Spawn Miragul".
171. Hand "Miragul's Phylactery" (19072) to everfrost/"Lich Of Miragul". Spawns "Spawn Miragul" (30094). Loot "Miragul's Robe" (1254) from "Spawn Miragul".
172. airplane/"Inte Akera", hand "Miragul's Robe" (1254) + "Inte's First Blessing" (18033) + "Inte's Second Blessing" (18034) + "Miragul's Head" (19073). Gives "Fiery Avenger" (11050).
173. fearplane/"Irak Altil", hand "Fiery Avenger" (11050) + "Mark of Atonement" (29010). Gives "Fiery Defender" (10099).
174. hohonora/"Irak Altil", say "Hail". Sets `paladin_epic` to `6`.
175. Loot "Top Section of an Engraved Signet" (9956) from "An Ikaav Miragenist" (NPC 301015) in `bloodfields`. Drop cache: 6.08% chance per kill.
176. Loot "Bottom Section of an Engraved Signet" (10399) from "An Ikaav Castigator" (NPC 301003) in `bloodfields`. Drop cache: 4% chance per kill.
177. Loot "Center Section of an Engraved Signet" (10235) from "An Ikaav Deathbeckoner" (NPC 301008) in `bloodfields`. Drop cache: 5.13% chance per kill.
178. bloodfields/"Cryssa", hand "Top Section of an Engraved Signet" (9956) + "Center Section of an Engraved Signet" (10235) + "Bottom Section of an Engraved Signet" (10399). Gives "Enchanted Signet of the Disciples" (12080).
179. bloodfields/"Cryssa", hand "Top Section of an Engraved Signet" (9956) + "Center Section of an Engraved Signet" (10235) + "Bottom Section of an Engraved Signet" (10399). Sets `cleric20_darkdisciples` to `1`.
180. Loot "Redis' Soulstone" (69983) from "Shade of Redis Linrok" in `dranikcatacombsa`.
181. global/"Global Player", combine recipe 19914. Sets `ranger_epic` to `8`.
182. Spawns "Durunal the Cursebearer" (300087) in `wallofslaughter` on enter.
183. Loot "Dark and Twisted Sword" (69971) from "Durunal the Cursebearer".
184. hohonora/"Irak Altil", hand "Dark and Twisted Sword" (69971). Requires `paladin_epic` ==6. Gives "Dark and Twisted Sword" (69972).

### "Redemption" (64031)

1. Spawns "A Corrupted Koalindl" (69141) in `oot` on event_fish_success.
2. Loot "Corrupted Koalindl's Heart" (69929) from "A Corrupted Koalindl".
3. Spawns "A Corrupted Koalindl" (224432) in `gunthak` on event_fish_success.
4. Loot "Corrupted Koalindl's Heart" (69930) from "A Corrupted Koalindl".
5. Spawns "A Corrupted Koalindl" (93306) in `overthere` on event_fish_success.
6. Loot "Corrupted Koalindl's Heart" (69931) from "A Corrupted Koalindl".
7. Spawns "A Corrupted Koalindl" (182150) in `nedaria` on event_fish_success.
8. Loot "Corrupted Koalindl's Heart" (69932) from "A Corrupted Koalindl".
9. qeynos2/"Enic Ruklin", hand "Corrupted Koalindl's Heart" (69929) + "Corrupted Koalindl's Heart" (69930) + "Corrupted Koalindl's Heart" (69931) + "Corrupted Koalindl's Heart" (69932). Sets `paladin_epic` to `4`.
10. qeynos2/"Enic Ruklin", hand "Corrupted Koalindl's Heart" (69929) + "Corrupted Koalindl's Heart" (69930) + "Corrupted Koalindl's Heart" (69931) + "Corrupted Koalindl's Heart" (69932). Gives "Seal of Enic" (69933).
11. Say "Hail" to skyfire/"Dry Sapara".
12. Spawns "Rithnok the Tormented" (91193).
13. Loot "Rithnok's Soulstone" (69935) from "Rithnok the Tormented".
14. skyfire/"Dry Sapara", hand "Rithnok's Soulstone" (69935). Gives "Rithnok's Soulstone" (69936).
15. Ground spawn of "Soulstone Shard" (69937) in `draniksscar`.
16. Ground spawn of "Soulstone Shard" (69938) in `bloodfields`.
17. Ground spawn of "Soulstone Shard" (69939) in `causeway`.
18. Ground spawn of "Soulstone Shard" (69940) in `dranik`.
19. Combine in "Rithnok's Soulstone" (69936): "Soulstone Shard" (69937), "Soulstone Shard" (69938), "Soulstone Shard" (69939), "Soulstone Shard" (69940). Produces "Rithnok's Soulstone" (69941). The combine does not fail.
20. dawnshroud/"Mikhal Young", hand "Drema's Fingerbone" (69946). Sets `paladin_epic` to `5`.
21. dawnshroud/"Mikhal Young", say "Find Anything". Requires `paladin_epic` ==4. Gives "Drema's Locket" (69945).
22. letalis/"Drema Young", hand "Drema's Locket" (69945). Requires `paladin_epic` set. Requires `paladin_epic` >=4. Gives "Drema's Fingerbone" (69946).
23. dawnshroud/"Denns Rootenpaw", hand "Drema's Fingerbone" (69946). Requires `paladin_epic` ==5. Gives "Bone Collector's Bag" (69947).
24. Loot "Dark Skeleton Remains" (69927) from "A Sun Revenant" in `thegrey`.
25. Loot "Dark Skeleton Remains" (69926) from "Disturbed Elysian Remains" (NPC 176016) in `umbral`. Drop cache: 2.58% chance per kill.
26. Loot "Dark Skeleton Remains" (69925) from "A Soriz Slave" (NPC 162029) in `ssratemple`. Drop cache: 35% chance per kill.
27. Combine in "Bone Collector's Bag" (69947): "Dark Skeleton Remains" (69927), "Dark Skeleton Remains" (69926), "Dark Skeleton Remains" (69925). Produces "Bone Collector's Bag" (69948). The combine does not fail.
28. dawnshroud/"Denns Rootenpaw", hand "Bone Collector's Bag" (69948). Requires `paladin_epic` ==5. Gives "Enchanted Bone Powder" (69949).
29. Hand "Enchanted Bone Powder" (69949) to letalis/"Drema Young". Spawns "Drema Young" (169128). Loot "Drema's Soulstone" (69928) from "Drema Young".
30. Loot "Soulstone Shard" (69950) from "Coterie Corruptor" in `tenebrous`.
31. Spawns "Shade of Mujaki the Devourer" (204081) in `ponightmare` on event death_complete:204080.
32. Loot "Soulstone Shard" (69951) from "Shade of Mujaki the Devourer".
33. Combine in "Drema's Soulstone" (69928): "Soulstone Shard" (69950), "Soulstone Shard" (69951). Produces "Drema's Soulstone" (69952). The combine does not fail.
34. abysmal/"Lovine Lemise", say "Ingredients". Requires `paladin_epic` ==5. Gives "Lovine's Potion Bag" (69922).
35. Loot "Ra'Tuk Screambringer's Jaw" (69921) from "A Ra'Tuk Screambringer" (NPC 283104) in `barindu`. Drop cache: 4.06% chance per kill.
36. Loot "Noc Fleshfeasters Tail" (69920) from "A Noc Fleshfeaster" in `riwwi`.
37. Loot "Mastruq Havocblade Blood" (69919) from "A Mastruq Havocblade" in `qinimi`.
38. Loot "Mastruq Havocblade Blood" (69919) from "A Mastruq Warfiend" in `qinimi`.
39. Loot "Potameid Seaweed Strands" (69918) from "An Entrapped Potameid" in `natimbi`.
40. Combine in "Lovine's Potion Bag" (69922): "Ra'Tuk Screambringer's Jaw" (69921), "Noc Fleshfeasters Tail" (69920), "Mastruq Havocblade Blood" (69919), "Potameid Seaweed Strands" (69918). Produces "Lovine's Potion Bag" (69923). The combine does not fail.
41. abysmal/"Lovine Lemise", hand "Lovine's Potion Bag" (69923). Sets `paladin_epic_reiya` to `1`.
42. Summon "Foldable Medicine Bag" (17770) by casting "Unfold Medicine Bag".
43. Common item: Fine Potion Vial (95846). Listed in 15 zones.
44. Loot "Robust Shadow Essence" (96911) from "Qua Senshali Xakra" (NPC 158020) in `vexthal`. Drop cache: 28.72% chance per kill.
45. Loot "Sage Leaf" (14215) from "a Di'zok Herbalist" in `chardok`.
46. Loot "Sage Leaf" (14215) from "a Sarnak Herb Collector" in `chardok`.
47. Loot "Sage Leaf" (14215) from "an Apprentice Herbalist" in `chardok`.
48. Loot "Valerian Root" (14230) from "a Di'zok Herbalist" in `chardok`.
49. Loot "Valerian Root" (14230) from "a Sarnak Herb Collector" in `chardok`.
50. Loot "Valerian Root" (14230) from "an Apprentice Herbalist" in `chardok`.
51. Common item: Woundwart (16526). Listed in 9 zones.
52. Combine in "Foldable Medicine Bag" (17770): "Fine Potion Vial" (95846), "Robust Shadow Essence" (96911), "Sage Leaf" (14215), "Valerian Root" (14230), "Woundwart" (16526). Produces "Mist of the Breathless" (96937). Requires Alchemy, trivial 224.
53. abysmal/"Reiya The Pained", hand "Mist of the Breathless" (96937). Requires `paladin_epic_reiya` ==1. Gives "Reiya's Soulstone" (69924).
54. Unresolved cyclic prerequisite: `mage_epic` >=9.
55. draniksscar/"Iilivina", say "Primals". Sets `mage_epic` to `10`.
56. Spawns "Shade of Reiya the Pained" (284104) in `ferubi` on enter.
57. Loot "Soulstone Shard" (69943) from "Shade of Reiya the Pained".
58. Loot "Soulstone Shard" (69944) from "Vuranish Xxuro" in `vxed`.
59. Combine in "Reiya's Soulstone" (69924): "Soulstone Shard" (69943), "Soulstone Shard" (69944). Produces "Reiya's Soulstone" (69942). The combine does not fail.
60. Loot "Tainted Darksteel Sword" (29000) from "Keeper of the Tombs" in `hole`.
61. freeporteast/"Peasant Woman", say "I Will Take It". Gives "Bucket of Water" (29008).
62. freeporteast/"Joshua", hand "Bucket of Water" (29008). Gives "Bucket of Pure Water" (29009).
63. erudnext/"Reklon Gnallen", hand "Tainted Darksteel Sword" (29000) + "Bucket of Pure Water" (29009). Gives "Gleaming Crested Sword" (29003).
64. Loot "Tainted Darksteel Breastplate" (29001) from "Thought Destroyer" in `hateplaneb`.
65. kaladimb/"Nella Stonebraids", say "Dinner". Gives "Cold Plate of Beef and Bread" (29007).
66. kaladimb/"Jark", hand "Cold Plate of Beef and Bread" (29007). Gives "Pure Crystal" (29006).
67. erudnext/"Reklon Gnallen", hand "Tainted Darksteel Breastplate" (29001) + "Pure Crystal" (29006). Gives "Gleaming Crested Breastplate" (29004).
68. Loot "Tainted Darksteel Shield" (29002) from "Kirak Vil" in `nektulos`.
69. felwithea/"Elia The Pure", hand "Tainted Darksteel Shield" (29002). Gives "Gleaming Crested Shield" (29005).
70. erudnext/"Reklon Gnallen", hand "Gleaming Crested Sword" (29003) + "Gleaming Crested Breastplate" (29004) + "Gleaming Crested Shield" (29005). Gives "Mark of Atonement" (29010).
71. No quest step gives Drom's Champagne (13829). The dump lists it in freeporteast, freporte, highpasshold.
72. freeporteast/"Tykar Renlin", hand "Drom's Champagne" (13829) + "Drom's Champagne" (13829) + "Drom's Champagne" (13829) + "Drom's Champagne" (13829). Gives "Bunker Cell #1" (12196).
73. Summon "Black Diamond of Nightmares" (29990) by casting "Imbue Nightmare".
74. potranquility/"Elder Fuirstel", say "Hail". Sets `pop_cod_final` to `1`.
75. poknowledge/"Aid Grimel", say "Versed In The Art Of Smithing". Requires `pop_cod_final` ==1. Requires `pop_cod_final` set. Gives "Filthy Breastplate" (15984).
76. Combine in "Mixing Bowl" (17906): "Celestial Solvent" (9731), "Words of Acquisition (Beza)" (11866). Produces "Celestial Essence" (9650). Requires Baking, trivial 15. The combine does not fail.
77. Combine in "Mixing Bowl" (17906): "Celestial Solvent" (9731), "Words of Burnishing" (11862). Produces "Celestial Essence" (9650). Requires Baking, trivial 15. The combine does not fail.
78. 67 other recipes also produce Celestial Essence (9650).
79. Common item: Jar of Acid (22133). Listed in 15 zones.
80. Combine in Brew Barrel (19): "Celestial Essence" (9650), "Jar of Acid" (22133). Produces "Acid Wash" (15987). Requires Brewing, trivial 151.
81. Combine in Forge (17): "Filthy Breastplate" (15984), "Acid Wash" (15987). Produces "Cleansed Breastplate" (15998). Requires Blacksmithing, trivial 227.
82. Common item: Mortar and Pestle (17904). Listed in 12 zones.
83. Loot "Sandstorm Pearl" (29909) from "Rorek Steelthorn" (NPC 209081) in `bothunder`. Drop cache: 5.33% chance per kill.
84. Combine in "Mortar and Pestle" (17904): "Sandstorm Pearl" (29909). Produces "Powdered Sandstorm Pearl" (29520) x4. Requires Make Poison, trivial 255.
85. Common item: Firing Sheet (16906). Listed in 34 zones.
86. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
87. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `steamfont`.
88. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `tox`.
89. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `toxxulia`.
90. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
91. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). The combine does not fail.
92. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
93. Say "Tm Devrak Death" to rujd/"Rujd".
94. Spawns "spawn chest with Heavy Orcish Prison Key" (245241).
95. Loot "Pod of Water" (13044) from "spawn chest with Heavy Orcish Prison Key".
96. 6 alternative loot source(s) also yield Pod of Water (13044).
97. Forage "Pod of Water" (13044) in `ruja`.
98. Forage "Pod of Water" (13044) in `uqua`.
99. Forage "Pod of Water" (13044) in `yxtta`.
100. Combine in Brew Barrel (19): "Bottle of Aged Bloodwine" (51163), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aged Bloodwine" (51164). Requires Brewing, trivial 255.
101. Combine in Brew Barrel (19): "Bottle of Aldo's Bitter Ale" (75805), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aldo's Bitter Ale" (75811). Requires Brewing, trivial 15.
102. 17 other recipes also produce Bottle (16598).
103. Combine in Brew Barrel (19): "Pod of Water" (13044), "Bottle" (16598). Produces "Water Flask" (13006). Requires Brewing, trivial 21.
104. Combine in Pottery Wheel (21): "Water Flask" (13006), "Block of Clay" (16901). Produces "Small Block of Clay" (16900) x3. Requires Pottery, trivial 21.
105. Combine in Pottery Wheel (21): "Small Block of Clay" (16900), "Water Flask" (13006). Produces "Block of Clay" (16901). Requires Pottery, trivial 21.
106. Combine in Pottery Wheel (21): "Water Flask" (13006), "Large Block of Clay" (16902). Produces "Block of Clay" (16901) x2. Requires Pottery, trivial 21.
107. Combine in Pottery Wheel (21): "Block of Clay" (16901), "Water Flask" (13006). Produces "Large Block of Clay" (16902). Requires Pottery, trivial 21.
108. Common item: Large Bowl Sketch (16963). Listed in 29 zones.
109. Combine in Pottery Wheel (21): "Large Block of Clay" (16902), "Water Flask" (13006), "Large Bowl Sketch" (16963). Produces "Unfired Mixing Bowl" (16930). Requires Pottery, trivial 128.
110. Combine in Kiln (22): "Firing Sheet" (16906), "Unfired Mixing Bowl" (16930). Produces "Mixing Bowl" (17906). Requires Pottery, trivial 15.
111. Combine in "Mixing Bowl" (17906): "Sandstorm Pearl" (29909). Produces "Powdered Sandstorm Pearl" (29520) x4. Requires Baking. The combine does not fail.
112. Spawns "a Koka'Vor chieftain" (210236) in `postorms` on event_signal.
113. Loot "Storm Rider Blood" (29526) from "a Koka'Vor chieftain".
114. Loot "Drop of Pure Rain" (29904) from "A vann stav" (NPC 209018) in `bothunder`. Drop cache: 4% chance per kill.
115. Combine in Brew Barrel (19): "Powdered Sandstorm Pearl" (29520), "Storm Rider Blood" (29526), "Drop of Pure Rain" (29904). Produces "Hurricane Temper" (29533). Requires Brewing, trivial 135.
116. Combine in Forge (17): "Cleansed Breastplate" (15998), "Hurricane Temper" (29533). Produces "Tempered Breastplate" (15999). Requires Blacksmithing, trivial 229.
117. Combine in Forge (17): "Black Diamond of Nightmares" (29990), "Tempered Breastplate" (15999). Produces "Imbued Breastplate" (15985). Requires Blacksmithing 220. Trivial at 275.
118. poknowledge/"Aid Grimel", hand "Imbued Breastplate" (15985). Gives "Hardened Leather Signet" (16249).
119. poknowledge/"Aid Grimel", say "Skill In Brewing". Requires `pop_cod_final` ==1. Requires `pop_cod_final` set. Gives "Portable Drink Barrel" (17179).
120. Loot "Snake Scales" (13070) from "A Kerra Snake" (NPC 98017) in `erudsxing`. Drop cache: 59.23% chance per kill.
121. Combine in "Portable Drink Barrel" (17179): "Water Flask" (13006), "Snake Scales" (13070), "Bottle" (16598). Produces "Bog Juice" (16581). Requires Brewing, trivial 21.
122. Common item: Spit (17947). Listed in 34 zones.
123. Loot "Fire Beetle Eye" (10307) from "A Klicnik Drone" (NPC 2021) in `qeynos2`. Drop cache: 100% chance per kill.
124. Spawns "Sepsis Rat" (45113) in `qcat` on event_death.
125. Loot "Rat Ears" (13072) from "Sepsis Rat".
126. 2 alternative loot source(s) also yield Rat Ears (13072).
127. Combine in "Spit" (17947): "Fire Beetle Eye" (10307), "Rat Ears" (13072). Produces "Edible Goo" (13498). Requires Baking, trivial 21.
128. freeporteast/"A Prisoner", hand "Bunker Cell #1" (12196) + "Edible Goo" (13498) + "Bog Juice" (16581). Gives "H. K. 102" (12143).
129. highkeep/"Assistant Kiolna", hand "H. K. 102" (12143). Gives "Sealed Note" (18936).
130. paw/"Brother Hayle", hand "Sealed Note" (18936). Gives "Note" (18937).
131. Kill freportw/"Sir Lucan D-Lere". Spawns "Sir Lucan D'Lere" (9147).
132. Loot "Testimony of Truth" (18827) from "Sir Lucan D'Lere".
133. freeportwest/"Valeron Dushire", hand "Testimony of Truth" (18827). Gives "Brilliant Sword of Faith" (13947).
134. Loot "Spider Venom Sac" (14018) from "Stone Spider" (NPC 32057) in `soldungb`. Drop cache: 51% chance per kill.
135. freeportwest/"Merko Quetalis", hand "Spider Venom Sac" (14018). Gives "Token of Bravery" (12144).
136. **Broken:** nothing in the graph gives, loots, spawns, or combines Blackbox XIVD (13344).
137. akanon/"Baxok Curhunter", hand "Blackbox XIVD" (13344). Gives "Cloth Shirt" (1004).
138. commonlands/"Altunic Jartin", hand "Cloth Shirt" (1004). Gives "Token of Generosity" (13865).
139. Hand "Token of Bravery" (12144) + "Token of Generosity" (13865) to freeportwest/"Merko Quetalis". Spawns "spawns Guard Willia" (383270). Loot "Token of Truth" (13866) from "spawns Guard Willia".
140. 1 alternative loot source(s) also yield Token of Truth (13866).
141. freeportwest/"Merko Quetalis", hand "Token of Truth" (13866). Gives "Testimony" (18828).
142. Loot "Glowing Sword Hilt" (12197) from "Xicotl" in `mistmoore`.
143. paw/"Brother Hayle", hand "Glowing Sword Hilt" (12197) + "Brilliant Sword of Faith" (13947) + "Testimony" (18828) + "Note" (18937). Gives "SoulFire" (5504).
144. airplane/"Inte Akera", hand "SoulFire" (5504). Gives "Inte's First Blessing" (18033).
145. neriakc/"Selzar L-Crit", say "Armor". Gives "Note to Kanthuk" (2416).
146. butcher/"Kanthuk Ogrebane", hand "Note to Kanthuk" (2416). Sets `Kanthuk` to `ghoul`.
147. butcher/"Kanthuk Ogrebane", say "Strange Image". Requires `Kanthuk` set. Gives "Pendant" (2414).
148. cauldron/"Llara", hand "Pendant" (2414). Sets `Llara` to `ghoul`.
149. cauldron/"Llara", say "Ruathey". Requires `Llara` set. Gives "Note to Ruathey" (2417).
150. lavastorm/"Ruathey", hand "Note to Ruathey" (2417). Sets `Ruathey` to `ghoul`.
151. lavastorm/"Ruathey", hand "Note to Ruathey" (2417). Sets `ruathey_note` to `1`.
152. lavastorm/"Ruathey", say "Bag". Requires `Ruathey` set. Requires `ruathey_note` ==1. Requires `ruathey_note` set. Gives "Nobleman's Bag" (17878).
153. Loot "Ghoul's Heart" (2410) from "A Ghoul" (NPC 63011) in `unrest`. Drop cache: 25% chance per kill.
154. Loot "Amstaf's Scroll" (2411) from "A Goblin Thief" (NPC 6150) in `highkeep`. Drop cache: 35% chance per kill.
155. Loot "Blade of Nobility" (2412) from "A Crazed Goblin" (NPC 68162) in `butcher`. Drop cache: 10.57% chance per kill.
156. Loot "Hilt of the Nobleman" (2413) from "Ekeros" in `najena`.
157. Loot "Hilt of the Nobleman" (2413) from "A Skeleton" in `najena`.
158. Combine in "Nobleman's Bag" (17878): "Ghoul's Heart" (2410), "Amstaf's Scroll" (2411), "Blade of Nobility" (2412), "Hilt of the Nobleman" (2413). Produces "Ghoulbane" (5403). The combine does not fail.
159. airplane/"Inte Akera", hand "Ghoulbane" (5403). Gives "Inte's Second Blessing" (18034).
160. Loot "Torn, Burnt Book" (19071) from "Lord Nagafen" in `soldungb`.
161. Loot "Torn, Burnt Book" (19071) from "Melalafen" in `westwastes`.
162. Loot "Torn, Burnt Book" (19071) from "Severilous" in `emeraldjungle`.
163. Loot "Torn, Burnt Book" (19071) from "Talendor" in `skyfire`.
164. Loot "Torn, Burnt Book" (19071) from "The Fabled Severilous".
165. Loot "Torn, Frost-covered Book" (19070) from "Faydedar" in `timorous`.
166. Loot "Torn, Frost-covered Book" (19070) from "Gorenaire" in `dreadlands`.
167. Loot "Torn, Frost-covered Book" (19070) from "Lady Vox" in `permafrost`.
168. neriakb/"Rysva To-Biath", hand "Torn, Frost-covered Book" (19070) + "Torn, Burnt Book" (19071). Gives "Book of Scale" (18302).
169. oceanoftears/"Oracle Of K-Arnon", hand "Book of Scale" (18302). Gives "Miragul's Phylactery" (19072).
170. Hand "Miragul's Phylactery" (19072) to everfrost/"Lich Of Miragul". Spawns "Spawn Miragul" (30094). Loot "Miragul's Head" (19073) from "Spawn Miragul".
171. Hand "Miragul's Phylactery" (19072) to everfrost/"Lich Of Miragul". Spawns "Spawn Miragul" (30094). Loot "Miragul's Robe" (1254) from "Spawn Miragul".
172. airplane/"Inte Akera", hand "Miragul's Robe" (1254) + "Inte's First Blessing" (18033) + "Inte's Second Blessing" (18034) + "Miragul's Head" (19073). Gives "Fiery Avenger" (11050).
173. fearplane/"Irak Altil", hand "Fiery Avenger" (11050) + "Mark of Atonement" (29010). Gives "Fiery Defender" (10099).
174. hohonora/"Irak Altil", say "Hail". Sets `paladin_epic` to `6`.
175. Loot "Top Section of an Engraved Signet" (9956) from "An Ikaav Miragenist" (NPC 301015) in `bloodfields`. Drop cache: 6.08% chance per kill.
176. Loot "Bottom Section of an Engraved Signet" (10399) from "An Ikaav Castigator" (NPC 301003) in `bloodfields`. Drop cache: 4% chance per kill.
177. Loot "Center Section of an Engraved Signet" (10235) from "An Ikaav Deathbeckoner" (NPC 301008) in `bloodfields`. Drop cache: 5.13% chance per kill.
178. bloodfields/"Cryssa", hand "Top Section of an Engraved Signet" (9956) + "Center Section of an Engraved Signet" (10235) + "Bottom Section of an Engraved Signet" (10399). Gives "Enchanted Signet of the Disciples" (12080).
179. bloodfields/"Cryssa", hand "Top Section of an Engraved Signet" (9956) + "Center Section of an Engraved Signet" (10235) + "Bottom Section of an Engraved Signet" (10399). Sets `cleric20_darkdisciples` to `1`.
180. Loot "Redis' Soulstone" (69983) from "Shade of Redis Linrok" in `dranikcatacombsa`.
181. global/"Global Player", combine recipe 19914. Sets `ranger_epic` to `8`.
182. Spawns "Durunal the Cursebearer" (300087) in `wallofslaughter` on enter.
183. Loot "Dark and Twisted Sword" (69971) from "Durunal the Cursebearer".
184. hohonora/"Irak Altil", hand "Dark and Twisted Sword" (69971). Requires `paladin_epic` ==6. Gives "Dark and Twisted Sword" (69972).
185. Combine in "Dark and Twisted Sword" (69972): "Rithnok's Soulstone" (69941), "Drema's Soulstone" (69952), "Reiya's Soulstone" (69942), "Redis' Soulstone" (69983). Produces "Redemption" (64031). The combine does not fail.

### "Token of Compassion" (69953)

1. Spawns "A Corrupted Koalindl" (69141) in `oot` on event_fish_success.
2. Loot "Corrupted Koalindl's Heart" (69929) from "A Corrupted Koalindl".
3. Spawns "A Corrupted Koalindl" (224432) in `gunthak` on event_fish_success.
4. Loot "Corrupted Koalindl's Heart" (69930) from "A Corrupted Koalindl".
5. Spawns "A Corrupted Koalindl" (93306) in `overthere` on event_fish_success.
6. Loot "Corrupted Koalindl's Heart" (69931) from "A Corrupted Koalindl".
7. Spawns "A Corrupted Koalindl" (182150) in `nedaria` on event_fish_success.
8. Loot "Corrupted Koalindl's Heart" (69932) from "A Corrupted Koalindl".
9. qeynos2/"Enic Ruklin", hand "Corrupted Koalindl's Heart" (69929) + "Corrupted Koalindl's Heart" (69930) + "Corrupted Koalindl's Heart" (69931) + "Corrupted Koalindl's Heart" (69932). Sets `paladin_epic` to `4`.
10. qeynos2/"Enic Ruklin", hand "Corrupted Koalindl's Heart" (69929) + "Corrupted Koalindl's Heart" (69930) + "Corrupted Koalindl's Heart" (69931) + "Corrupted Koalindl's Heart" (69932). Gives "Seal of Enic" (69933).
11. Say "Hail" to skyfire/"Dry Sapara".
12. Spawns "Rithnok the Tormented" (91193).
13. Loot "Rithnok's Soulstone" (69935) from "Rithnok the Tormented".
14. skyfire/"Dry Sapara", hand "Rithnok's Soulstone" (69935). Gives "Rithnok's Soulstone" (69936).
15. Ground spawn of "Soulstone Shard" (69937) in `draniksscar`.
16. Ground spawn of "Soulstone Shard" (69938) in `bloodfields`.
17. Ground spawn of "Soulstone Shard" (69939) in `causeway`.
18. Ground spawn of "Soulstone Shard" (69940) in `dranik`.
19. Combine in "Rithnok's Soulstone" (69936): "Soulstone Shard" (69937), "Soulstone Shard" (69938), "Soulstone Shard" (69939), "Soulstone Shard" (69940). Produces "Rithnok's Soulstone" (69941). The combine does not fail.
20. dawnshroud/"Mikhal Young", hand "Drema's Fingerbone" (69946). Sets `paladin_epic` to `5`.
21. dawnshroud/"Mikhal Young", say "Find Anything". Requires `paladin_epic` ==4. Gives "Drema's Locket" (69945).
22. letalis/"Drema Young", hand "Drema's Locket" (69945). Requires `paladin_epic` set. Requires `paladin_epic` >=4. Gives "Drema's Fingerbone" (69946).
23. dawnshroud/"Denns Rootenpaw", hand "Drema's Fingerbone" (69946). Requires `paladin_epic` ==5. Gives "Bone Collector's Bag" (69947).
24. Loot "Dark Skeleton Remains" (69927) from "A Sun Revenant" in `thegrey`.
25. Loot "Dark Skeleton Remains" (69926) from "Disturbed Elysian Remains" (NPC 176016) in `umbral`. Drop cache: 2.58% chance per kill.
26. Loot "Dark Skeleton Remains" (69925) from "A Soriz Slave" (NPC 162029) in `ssratemple`. Drop cache: 35% chance per kill.
27. Combine in "Bone Collector's Bag" (69947): "Dark Skeleton Remains" (69927), "Dark Skeleton Remains" (69926), "Dark Skeleton Remains" (69925). Produces "Bone Collector's Bag" (69948). The combine does not fail.
28. dawnshroud/"Denns Rootenpaw", hand "Bone Collector's Bag" (69948). Requires `paladin_epic` ==5. Gives "Enchanted Bone Powder" (69949).
29. Hand "Enchanted Bone Powder" (69949) to letalis/"Drema Young". Spawns "Drema Young" (169128). Loot "Drema's Soulstone" (69928) from "Drema Young".
30. Loot "Soulstone Shard" (69950) from "Coterie Corruptor" in `tenebrous`.
31. Spawns "Shade of Mujaki the Devourer" (204081) in `ponightmare` on event death_complete:204080.
32. Loot "Soulstone Shard" (69951) from "Shade of Mujaki the Devourer".
33. Combine in "Drema's Soulstone" (69928): "Soulstone Shard" (69950), "Soulstone Shard" (69951). Produces "Drema's Soulstone" (69952). The combine does not fail.
34. abysmal/"Lovine Lemise", say "Ingredients". Requires `paladin_epic` ==5. Gives "Lovine's Potion Bag" (69922).
35. Loot "Ra'Tuk Screambringer's Jaw" (69921) from "A Ra'Tuk Screambringer" (NPC 283104) in `barindu`. Drop cache: 4.06% chance per kill.
36. Loot "Noc Fleshfeasters Tail" (69920) from "A Noc Fleshfeaster" in `riwwi`.
37. Loot "Mastruq Havocblade Blood" (69919) from "A Mastruq Havocblade" in `qinimi`.
38. Loot "Mastruq Havocblade Blood" (69919) from "A Mastruq Warfiend" in `qinimi`.
39. Loot "Potameid Seaweed Strands" (69918) from "An Entrapped Potameid" in `natimbi`.
40. Combine in "Lovine's Potion Bag" (69922): "Ra'Tuk Screambringer's Jaw" (69921), "Noc Fleshfeasters Tail" (69920), "Mastruq Havocblade Blood" (69919), "Potameid Seaweed Strands" (69918). Produces "Lovine's Potion Bag" (69923). The combine does not fail.
41. abysmal/"Lovine Lemise", hand "Lovine's Potion Bag" (69923). Sets `paladin_epic_reiya` to `1`.
42. Summon "Foldable Medicine Bag" (17770) by casting "Unfold Medicine Bag".
43. Common item: Fine Potion Vial (95846). Listed in 15 zones.
44. Loot "Robust Shadow Essence" (96911) from "Qua Senshali Xakra" (NPC 158020) in `vexthal`. Drop cache: 28.72% chance per kill.
45. Loot "Sage Leaf" (14215) from "a Di'zok Herbalist" in `chardok`.
46. Loot "Sage Leaf" (14215) from "a Sarnak Herb Collector" in `chardok`.
47. Loot "Sage Leaf" (14215) from "an Apprentice Herbalist" in `chardok`.
48. Loot "Valerian Root" (14230) from "a Di'zok Herbalist" in `chardok`.
49. Loot "Valerian Root" (14230) from "a Sarnak Herb Collector" in `chardok`.
50. Loot "Valerian Root" (14230) from "an Apprentice Herbalist" in `chardok`.
51. Common item: Woundwart (16526). Listed in 9 zones.
52. Combine in "Foldable Medicine Bag" (17770): "Fine Potion Vial" (95846), "Robust Shadow Essence" (96911), "Sage Leaf" (14215), "Valerian Root" (14230), "Woundwart" (16526). Produces "Mist of the Breathless" (96937). Requires Alchemy, trivial 224.
53. abysmal/"Reiya The Pained", hand "Mist of the Breathless" (96937). Requires `paladin_epic_reiya` ==1. Gives "Reiya's Soulstone" (69924).
54. Unresolved cyclic prerequisite: `mage_epic` >=9.
55. draniksscar/"Iilivina", say "Primals". Sets `mage_epic` to `10`.
56. Spawns "Shade of Reiya the Pained" (284104) in `ferubi` on enter.
57. Loot "Soulstone Shard" (69943) from "Shade of Reiya the Pained".
58. Loot "Soulstone Shard" (69944) from "Vuranish Xxuro" in `vxed`.
59. Combine in "Reiya's Soulstone" (69924): "Soulstone Shard" (69943), "Soulstone Shard" (69944). Produces "Reiya's Soulstone" (69942). The combine does not fail.
60. Loot "Tainted Darksteel Sword" (29000) from "Keeper of the Tombs" in `hole`.
61. freeporteast/"Peasant Woman", say "I Will Take It". Gives "Bucket of Water" (29008).
62. freeporteast/"Joshua", hand "Bucket of Water" (29008). Gives "Bucket of Pure Water" (29009).
63. erudnext/"Reklon Gnallen", hand "Tainted Darksteel Sword" (29000) + "Bucket of Pure Water" (29009). Gives "Gleaming Crested Sword" (29003).
64. Loot "Tainted Darksteel Breastplate" (29001) from "Thought Destroyer" in `hateplaneb`.
65. kaladimb/"Nella Stonebraids", say "Dinner". Gives "Cold Plate of Beef and Bread" (29007).
66. kaladimb/"Jark", hand "Cold Plate of Beef and Bread" (29007). Gives "Pure Crystal" (29006).
67. erudnext/"Reklon Gnallen", hand "Tainted Darksteel Breastplate" (29001) + "Pure Crystal" (29006). Gives "Gleaming Crested Breastplate" (29004).
68. Loot "Tainted Darksteel Shield" (29002) from "Kirak Vil" in `nektulos`.
69. felwithea/"Elia The Pure", hand "Tainted Darksteel Shield" (29002). Gives "Gleaming Crested Shield" (29005).
70. erudnext/"Reklon Gnallen", hand "Gleaming Crested Sword" (29003) + "Gleaming Crested Breastplate" (29004) + "Gleaming Crested Shield" (29005). Gives "Mark of Atonement" (29010).
71. No quest step gives Drom's Champagne (13829). The dump lists it in freeporteast, freporte, highpasshold.
72. freeporteast/"Tykar Renlin", hand "Drom's Champagne" (13829) + "Drom's Champagne" (13829) + "Drom's Champagne" (13829) + "Drom's Champagne" (13829). Gives "Bunker Cell #1" (12196).
73. Summon "Black Diamond of Nightmares" (29990) by casting "Imbue Nightmare".
74. potranquility/"Elder Fuirstel", say "Hail". Sets `pop_cod_final` to `1`.
75. poknowledge/"Aid Grimel", say "Versed In The Art Of Smithing". Requires `pop_cod_final` ==1. Requires `pop_cod_final` set. Gives "Filthy Breastplate" (15984).
76. Combine in "Mixing Bowl" (17906): "Celestial Solvent" (9731), "Words of Acquisition (Beza)" (11866). Produces "Celestial Essence" (9650). Requires Baking, trivial 15. The combine does not fail.
77. Combine in "Mixing Bowl" (17906): "Celestial Solvent" (9731), "Words of Burnishing" (11862). Produces "Celestial Essence" (9650). Requires Baking, trivial 15. The combine does not fail.
78. 67 other recipes also produce Celestial Essence (9650).
79. Common item: Jar of Acid (22133). Listed in 15 zones.
80. Combine in Brew Barrel (19): "Celestial Essence" (9650), "Jar of Acid" (22133). Produces "Acid Wash" (15987). Requires Brewing, trivial 151.
81. Combine in Forge (17): "Filthy Breastplate" (15984), "Acid Wash" (15987). Produces "Cleansed Breastplate" (15998). Requires Blacksmithing, trivial 227.
82. Common item: Mortar and Pestle (17904). Listed in 12 zones.
83. Loot "Sandstorm Pearl" (29909) from "Rorek Steelthorn" (NPC 209081) in `bothunder`. Drop cache: 5.33% chance per kill.
84. Combine in "Mortar and Pestle" (17904): "Sandstorm Pearl" (29909). Produces "Powdered Sandstorm Pearl" (29520) x4. Requires Make Poison, trivial 255.
85. Common item: Firing Sheet (16906). Listed in 34 zones.
86. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
87. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `steamfont`.
88. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `tox`.
89. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `toxxulia`.
90. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
91. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). The combine does not fail.
92. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
93. Say "Tm Devrak Death" to rujd/"Rujd".
94. Spawns "spawn chest with Heavy Orcish Prison Key" (245241).
95. Loot "Pod of Water" (13044) from "spawn chest with Heavy Orcish Prison Key".
96. 6 alternative loot source(s) also yield Pod of Water (13044).
97. Forage "Pod of Water" (13044) in `ruja`.
98. Forage "Pod of Water" (13044) in `uqua`.
99. Forage "Pod of Water" (13044) in `yxtta`.
100. Combine in Brew Barrel (19): "Bottle of Aged Bloodwine" (51163), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aged Bloodwine" (51164). Requires Brewing, trivial 255.
101. Combine in Brew Barrel (19): "Bottle of Aldo's Bitter Ale" (75805), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aldo's Bitter Ale" (75811). Requires Brewing, trivial 15.
102. 17 other recipes also produce Bottle (16598).
103. Combine in Brew Barrel (19): "Pod of Water" (13044), "Bottle" (16598). Produces "Water Flask" (13006). Requires Brewing, trivial 21.
104. Combine in Pottery Wheel (21): "Water Flask" (13006), "Block of Clay" (16901). Produces "Small Block of Clay" (16900) x3. Requires Pottery, trivial 21.
105. Combine in Pottery Wheel (21): "Small Block of Clay" (16900), "Water Flask" (13006). Produces "Block of Clay" (16901). Requires Pottery, trivial 21.
106. Combine in Pottery Wheel (21): "Water Flask" (13006), "Large Block of Clay" (16902). Produces "Block of Clay" (16901) x2. Requires Pottery, trivial 21.
107. Combine in Pottery Wheel (21): "Block of Clay" (16901), "Water Flask" (13006). Produces "Large Block of Clay" (16902). Requires Pottery, trivial 21.
108. Common item: Large Bowl Sketch (16963). Listed in 29 zones.
109. Combine in Pottery Wheel (21): "Large Block of Clay" (16902), "Water Flask" (13006), "Large Bowl Sketch" (16963). Produces "Unfired Mixing Bowl" (16930). Requires Pottery, trivial 128.
110. Combine in Kiln (22): "Firing Sheet" (16906), "Unfired Mixing Bowl" (16930). Produces "Mixing Bowl" (17906). Requires Pottery, trivial 15.
111. Combine in "Mixing Bowl" (17906): "Sandstorm Pearl" (29909). Produces "Powdered Sandstorm Pearl" (29520) x4. Requires Baking. The combine does not fail.
112. Spawns "a Koka'Vor chieftain" (210236) in `postorms` on event_signal.
113. Loot "Storm Rider Blood" (29526) from "a Koka'Vor chieftain".
114. Loot "Drop of Pure Rain" (29904) from "A vann stav" (NPC 209018) in `bothunder`. Drop cache: 4% chance per kill.
115. Combine in Brew Barrel (19): "Powdered Sandstorm Pearl" (29520), "Storm Rider Blood" (29526), "Drop of Pure Rain" (29904). Produces "Hurricane Temper" (29533). Requires Brewing, trivial 135.
116. Combine in Forge (17): "Cleansed Breastplate" (15998), "Hurricane Temper" (29533). Produces "Tempered Breastplate" (15999). Requires Blacksmithing, trivial 229.
117. Combine in Forge (17): "Black Diamond of Nightmares" (29990), "Tempered Breastplate" (15999). Produces "Imbued Breastplate" (15985). Requires Blacksmithing 220. Trivial at 275.
118. poknowledge/"Aid Grimel", hand "Imbued Breastplate" (15985). Gives "Hardened Leather Signet" (16249).
119. poknowledge/"Aid Grimel", say "Skill In Brewing". Requires `pop_cod_final` ==1. Requires `pop_cod_final` set. Gives "Portable Drink Barrel" (17179).
120. Loot "Snake Scales" (13070) from "A Kerra Snake" (NPC 98017) in `erudsxing`. Drop cache: 59.23% chance per kill.
121. Combine in "Portable Drink Barrel" (17179): "Water Flask" (13006), "Snake Scales" (13070), "Bottle" (16598). Produces "Bog Juice" (16581). Requires Brewing, trivial 21.
122. Common item: Spit (17947). Listed in 34 zones.
123. Loot "Fire Beetle Eye" (10307) from "A Klicnik Drone" (NPC 2021) in `qeynos2`. Drop cache: 100% chance per kill.
124. Spawns "Sepsis Rat" (45113) in `qcat` on event_death.
125. Loot "Rat Ears" (13072) from "Sepsis Rat".
126. 2 alternative loot source(s) also yield Rat Ears (13072).
127. Combine in "Spit" (17947): "Fire Beetle Eye" (10307), "Rat Ears" (13072). Produces "Edible Goo" (13498). Requires Baking, trivial 21.
128. freeporteast/"A Prisoner", hand "Bunker Cell #1" (12196) + "Edible Goo" (13498) + "Bog Juice" (16581). Gives "H. K. 102" (12143).
129. highkeep/"Assistant Kiolna", hand "H. K. 102" (12143). Gives "Sealed Note" (18936).
130. paw/"Brother Hayle", hand "Sealed Note" (18936). Gives "Note" (18937).
131. Kill freportw/"Sir Lucan D-Lere". Spawns "Sir Lucan D'Lere" (9147).
132. Loot "Testimony of Truth" (18827) from "Sir Lucan D'Lere".
133. freeportwest/"Valeron Dushire", hand "Testimony of Truth" (18827). Gives "Brilliant Sword of Faith" (13947).
134. Loot "Spider Venom Sac" (14018) from "Stone Spider" (NPC 32057) in `soldungb`. Drop cache: 51% chance per kill.
135. freeportwest/"Merko Quetalis", hand "Spider Venom Sac" (14018). Gives "Token of Bravery" (12144).
136. **Broken:** nothing in the graph gives, loots, spawns, or combines Blackbox XIVD (13344).
137. akanon/"Baxok Curhunter", hand "Blackbox XIVD" (13344). Gives "Cloth Shirt" (1004).
138. commonlands/"Altunic Jartin", hand "Cloth Shirt" (1004). Gives "Token of Generosity" (13865).
139. Hand "Token of Bravery" (12144) + "Token of Generosity" (13865) to freeportwest/"Merko Quetalis". Spawns "spawns Guard Willia" (383270). Loot "Token of Truth" (13866) from "spawns Guard Willia".
140. 1 alternative loot source(s) also yield Token of Truth (13866).
141. freeportwest/"Merko Quetalis", hand "Token of Truth" (13866). Gives "Testimony" (18828).
142. Loot "Glowing Sword Hilt" (12197) from "Xicotl" in `mistmoore`.
143. paw/"Brother Hayle", hand "Glowing Sword Hilt" (12197) + "Brilliant Sword of Faith" (13947) + "Testimony" (18828) + "Note" (18937). Gives "SoulFire" (5504).
144. airplane/"Inte Akera", hand "SoulFire" (5504). Gives "Inte's First Blessing" (18033).
145. neriakc/"Selzar L-Crit", say "Armor". Gives "Note to Kanthuk" (2416).
146. butcher/"Kanthuk Ogrebane", hand "Note to Kanthuk" (2416). Sets `Kanthuk` to `ghoul`.
147. butcher/"Kanthuk Ogrebane", say "Strange Image". Requires `Kanthuk` set. Gives "Pendant" (2414).
148. cauldron/"Llara", hand "Pendant" (2414). Sets `Llara` to `ghoul`.
149. cauldron/"Llara", say "Ruathey". Requires `Llara` set. Gives "Note to Ruathey" (2417).
150. lavastorm/"Ruathey", hand "Note to Ruathey" (2417). Sets `Ruathey` to `ghoul`.
151. lavastorm/"Ruathey", hand "Note to Ruathey" (2417). Sets `ruathey_note` to `1`.
152. lavastorm/"Ruathey", say "Bag". Requires `Ruathey` set. Requires `ruathey_note` ==1. Requires `ruathey_note` set. Gives "Nobleman's Bag" (17878).
153. Loot "Ghoul's Heart" (2410) from "A Ghoul" (NPC 63011) in `unrest`. Drop cache: 25% chance per kill.
154. Loot "Amstaf's Scroll" (2411) from "A Goblin Thief" (NPC 6150) in `highkeep`. Drop cache: 35% chance per kill.
155. Loot "Blade of Nobility" (2412) from "A Crazed Goblin" (NPC 68162) in `butcher`. Drop cache: 10.57% chance per kill.
156. Loot "Hilt of the Nobleman" (2413) from "Ekeros" in `najena`.
157. Loot "Hilt of the Nobleman" (2413) from "A Skeleton" in `najena`.
158. Combine in "Nobleman's Bag" (17878): "Ghoul's Heart" (2410), "Amstaf's Scroll" (2411), "Blade of Nobility" (2412), "Hilt of the Nobleman" (2413). Produces "Ghoulbane" (5403). The combine does not fail.
159. airplane/"Inte Akera", hand "Ghoulbane" (5403). Gives "Inte's Second Blessing" (18034).
160. Loot "Torn, Burnt Book" (19071) from "Lord Nagafen" in `soldungb`.
161. Loot "Torn, Burnt Book" (19071) from "Melalafen" in `westwastes`.
162. Loot "Torn, Burnt Book" (19071) from "Severilous" in `emeraldjungle`.
163. Loot "Torn, Burnt Book" (19071) from "Talendor" in `skyfire`.
164. Loot "Torn, Burnt Book" (19071) from "The Fabled Severilous".
165. Loot "Torn, Frost-covered Book" (19070) from "Faydedar" in `timorous`.
166. Loot "Torn, Frost-covered Book" (19070) from "Gorenaire" in `dreadlands`.
167. Loot "Torn, Frost-covered Book" (19070) from "Lady Vox" in `permafrost`.
168. neriakb/"Rysva To-Biath", hand "Torn, Frost-covered Book" (19070) + "Torn, Burnt Book" (19071). Gives "Book of Scale" (18302).
169. oceanoftears/"Oracle Of K-Arnon", hand "Book of Scale" (18302). Gives "Miragul's Phylactery" (19072).
170. Hand "Miragul's Phylactery" (19072) to everfrost/"Lich Of Miragul". Spawns "Spawn Miragul" (30094). Loot "Miragul's Head" (19073) from "Spawn Miragul".
171. Hand "Miragul's Phylactery" (19072) to everfrost/"Lich Of Miragul". Spawns "Spawn Miragul" (30094). Loot "Miragul's Robe" (1254) from "Spawn Miragul".
172. airplane/"Inte Akera", hand "Miragul's Robe" (1254) + "Inte's First Blessing" (18033) + "Inte's Second Blessing" (18034) + "Miragul's Head" (19073). Gives "Fiery Avenger" (11050).
173. fearplane/"Irak Altil", hand "Fiery Avenger" (11050) + "Mark of Atonement" (29010). Gives "Fiery Defender" (10099).
174. hohonora/"Irak Altil", say "Hail". Sets `paladin_epic` to `6`.
175. Loot "Top Section of an Engraved Signet" (9956) from "An Ikaav Miragenist" (NPC 301015) in `bloodfields`. Drop cache: 6.08% chance per kill.
176. Loot "Bottom Section of an Engraved Signet" (10399) from "An Ikaav Castigator" (NPC 301003) in `bloodfields`. Drop cache: 4% chance per kill.
177. Loot "Center Section of an Engraved Signet" (10235) from "An Ikaav Deathbeckoner" (NPC 301008) in `bloodfields`. Drop cache: 5.13% chance per kill.
178. bloodfields/"Cryssa", hand "Top Section of an Engraved Signet" (9956) + "Center Section of an Engraved Signet" (10235) + "Bottom Section of an Engraved Signet" (10399). Gives "Enchanted Signet of the Disciples" (12080).
179. bloodfields/"Cryssa", hand "Top Section of an Engraved Signet" (9956) + "Center Section of an Engraved Signet" (10235) + "Bottom Section of an Engraved Signet" (10399). Sets `cleric20_darkdisciples` to `1`.
180. Loot "Redis' Soulstone" (69983) from "Shade of Redis Linrok" in `dranikcatacombsa`.
181. global/"Global Player", combine recipe 19914. Sets `ranger_epic` to `8`.
182. Spawns "Durunal the Cursebearer" (300087) in `wallofslaughter` on enter.
183. Loot "Dark and Twisted Sword" (69971) from "Durunal the Cursebearer".
184. hohonora/"Irak Altil", hand "Dark and Twisted Sword" (69971). Requires `paladin_epic` ==6. Gives "Dark and Twisted Sword" (69972).
185. Combine in "Dark and Twisted Sword" (69972): "Rithnok's Soulstone" (69941), "Drema's Soulstone" (69952), "Reiya's Soulstone" (69942), "Redis' Soulstone" (69983). Produces "Redemption" (64031). The combine does not fail.
186. hohonora/"Irak Altil", say "Tell Me About Your Master". Sets `paladin_epic` to `9`.
187. qeynos2/"Camlend Serbold", say "Gem". Requires `paladin_epic` ==9. Gives "Unfilled Set of Prayer Beads" (69968).
188. rivervale/"Kaya Cloudfoot", say "Different About It". Requires `paladin_epic` ==9. Gives "Note from Kaya" (69970).
189. rivervale/"Deputy Cheel", hand "Note from Kaya" (69970). Gives "Rivervale Prayer Bead" (69967).
190. akanon/"Lewis Reldnok", say "Blessed Gem". Triggers `akanon/lewis reldnok#timer:check_sit`.
191. Sit before the NPC while its timer checks your posture.
192. akanon/"Lewis Reldnok", on timer check_sit. Gives "Ak'anon Prayer Bead" (69966).
193. erudnint/"Josper Kenshed", say "Collect Component". Gives "Empty Bag" (17944).
194. Loot "Goblin Ice Necklace" (13897) from "Redwind" in `everfrost`.
195. Loot "Goblin Ice Necklace" (13897) from "An Ice Goblin Scout" in `everfrost`.
196. Loot "Goblin Ice Necklace" (13897) from "An Ice Goblin Whelp" in `everfrost`.
197. Loot "Goblin Ice Necklace" (13897) from "An Icy Orc" in `everfrost`.
198. Loot "Goblin Ice Necklace" (13897) from "Ice Goblin Diver" in `everfrost`.
199. Combine in "Empty Bag" (17944): "Goblin Ice Necklace" (13897). Produces "Bag of Ice Necklaces" (13898). The combine does not fail.
200. halas/"Lysbith Mcnaff", hand "Bag of Ice Necklaces" (13898). Gives "Iron Ration" (13005).
201. Loot "Cask" (16580) from "Tugog Grigol" in `rathemtn`.
202. Common item: Hops (16591). Listed in 31 zones.
203. Common item: Malt (16595). Listed in 30 zones.
204. Common item: Yeast (16596). Listed in 30 zones.
205. Combine in "Portable Drink Barrel" (17179): "Cask" (16580), "Hops" (16591), "Malt" (16595), "Yeast" (16596). Produces "Mead" (13008). Requires Brewing, trivial 41.
206. erudnext/"Reklon Gnallen", hand "Iron Ration" (13005) + "Mead" (13008). Requires `paladin_epic` ==9. Gives "Erudin Prayer Bead" (69965).
207. Summon "Quiver of Marr" (17307) by casting "Quiver of Marr".
208. rathemtn/"Shin Master Grubbus", hand "Quiver of Marr" (17307). Requires `paladin_epic` ==9. Gives "Gukta Prayer Bead" (69964).
209. Common item: Barley (16590). Listed in 28 zones.
210. Combine in "Medicine Bag" (17901): "Hand-Formed Bottle" (45232), "Ensnaring Concoction V" (45236). Produces "Empty Vial" (10062), "Cork" (16851), "Formed Ensnaring Concoction V" (45258). Requires Alchemy, trivial 41.
211. Combine in Brew Barrel (19): "Bottle of Aged Bloodwine" (51163), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aged Bloodwine" (51164). Requires Brewing, trivial 255.
212. 11 other recipes also produce Cork (16851).
213. Combine in "Portable Drink Barrel" (17179): "Water Flask" (13006), "Celestial Essence" (9650). Produces "Purified Water" (12607). Requires Brewing, trivial 58.
214. Combine in "Tracker's Water Extractor" (17987): "Purification Tablet" (12630), "Water Reed" (12778). Produces "Purified Water" (12607) x3. Requires Pottery. The combine does not fail.
215. 3 other recipes also produce Purified Water (12607).
216. Forage "Sand Verbena" (65582) in `taka`.
217. Forage "Sand Verbena" (65582) in `takb`.
218. Forage "Sand Verbena" (65582) in `takc`.
219. Forage "Sand Verbena" (65582) in `takd`.
220. Forage "Sand Verbena" (65582) in `take`.
221. Forage "Sand Verbena" (65582) in `takf`.
222. Forage "Sand Verbena" (65582) in `takg`.
223. Forage "Sand Verbena" (65582) in `takh`.
224. Forage "Sand Verbena" (65582) in `taki`.
225. Forage "Sand Verbena" (65582) in `takj`.
226. Combine in Brew Barrel (19): "Barley" (16590), "Bottle" (16598), "Cork" (16851), "Hops" (16591), "Purified Water" (12607), "Sand Verbena" (65582), "Yeast" (16596). Produces "Bottle of Double Brewed Double Dry Stout" (51157). Requires Brewing, trivial 226.
227. kaladimb/"Datur Nightseer", hand "Bottle of Double Brewed Double Dry Stout" (51157). Requires `paladin_epic` ==9. Gives "Kaladim Prayer Bead" (69963).
228. felwithea/"General Jyleel", hand platinum:1000. Requires `paladin_epic` ==9. Gives "Felwithe Prayer Bead" (69962).
229. Ground spawn of "Freeport Prayer Bead" (69961) in `freeportwest`.
230. Ground spawn of "Freeport Prayer Bead" (69961) in `freportn`.
231. qeynos2/"Ziska Ironforge", hand platinum:500. Requires `paladin_epic` ==9. Gives "Qeynos Prayer Bead" (69960).
232. Combine in "Unfilled Set of Prayer Beads" (69968): "Rivervale Prayer Bead" (69967), "Ak'anon Prayer Bead" (69966), "Erudin Prayer Bead" (69965), "Gukta Prayer Bead" (69964), "Kaladim Prayer Bead" (69963), "Felwithe Prayer Bead" (69962), "Freeport Prayer Bead" (69961), "Qeynos Prayer Bead" (69960). Produces "Set of Prayer Beads" (69969). The combine does not fail.
233. dranikhollowsc/"Anetal", hand "Set of Prayer Beads" (69969). Sets `paladin_epic_hollowc` to `2`.
234. natimbi/"Kemik Arulon", hand "Set of Prayer Beads" (69969). Sets `paladin_epic_hollowc` to `1`.
235. natimbi/"Kemik Arulon", say "Hail". Requires `paladin_epic_hollowc` ==2. Requires `paladin_epic` ==9. Requires `paladin_epic_hollowc` ==1. Gives "Token of Compassion" (69953).

### "Token of Chivalry" (69954)

1. Spawns "A Corrupted Koalindl" (69141) in `oot` on event_fish_success.
2. Loot "Corrupted Koalindl's Heart" (69929) from "A Corrupted Koalindl".
3. Spawns "A Corrupted Koalindl" (224432) in `gunthak` on event_fish_success.
4. Loot "Corrupted Koalindl's Heart" (69930) from "A Corrupted Koalindl".
5. Spawns "A Corrupted Koalindl" (93306) in `overthere` on event_fish_success.
6. Loot "Corrupted Koalindl's Heart" (69931) from "A Corrupted Koalindl".
7. Spawns "A Corrupted Koalindl" (182150) in `nedaria` on event_fish_success.
8. Loot "Corrupted Koalindl's Heart" (69932) from "A Corrupted Koalindl".
9. qeynos2/"Enic Ruklin", hand "Corrupted Koalindl's Heart" (69929) + "Corrupted Koalindl's Heart" (69930) + "Corrupted Koalindl's Heart" (69931) + "Corrupted Koalindl's Heart" (69932). Sets `paladin_epic` to `4`.
10. qeynos2/"Enic Ruklin", hand "Corrupted Koalindl's Heart" (69929) + "Corrupted Koalindl's Heart" (69930) + "Corrupted Koalindl's Heart" (69931) + "Corrupted Koalindl's Heart" (69932). Gives "Seal of Enic" (69933).
11. Say "Hail" to skyfire/"Dry Sapara".
12. Spawns "Rithnok the Tormented" (91193).
13. Loot "Rithnok's Soulstone" (69935) from "Rithnok the Tormented".
14. skyfire/"Dry Sapara", hand "Rithnok's Soulstone" (69935). Gives "Rithnok's Soulstone" (69936).
15. Ground spawn of "Soulstone Shard" (69937) in `draniksscar`.
16. Ground spawn of "Soulstone Shard" (69938) in `bloodfields`.
17. Ground spawn of "Soulstone Shard" (69939) in `causeway`.
18. Ground spawn of "Soulstone Shard" (69940) in `dranik`.
19. Combine in "Rithnok's Soulstone" (69936): "Soulstone Shard" (69937), "Soulstone Shard" (69938), "Soulstone Shard" (69939), "Soulstone Shard" (69940). Produces "Rithnok's Soulstone" (69941). The combine does not fail.
20. dawnshroud/"Mikhal Young", hand "Drema's Fingerbone" (69946). Sets `paladin_epic` to `5`.
21. dawnshroud/"Mikhal Young", say "Find Anything". Requires `paladin_epic` ==4. Gives "Drema's Locket" (69945).
22. letalis/"Drema Young", hand "Drema's Locket" (69945). Requires `paladin_epic` set. Requires `paladin_epic` >=4. Gives "Drema's Fingerbone" (69946).
23. dawnshroud/"Denns Rootenpaw", hand "Drema's Fingerbone" (69946). Requires `paladin_epic` ==5. Gives "Bone Collector's Bag" (69947).
24. Loot "Dark Skeleton Remains" (69927) from "A Sun Revenant" in `thegrey`.
25. Loot "Dark Skeleton Remains" (69926) from "Disturbed Elysian Remains" (NPC 176016) in `umbral`. Drop cache: 2.58% chance per kill.
26. Loot "Dark Skeleton Remains" (69925) from "A Soriz Slave" (NPC 162029) in `ssratemple`. Drop cache: 35% chance per kill.
27. Combine in "Bone Collector's Bag" (69947): "Dark Skeleton Remains" (69927), "Dark Skeleton Remains" (69926), "Dark Skeleton Remains" (69925). Produces "Bone Collector's Bag" (69948). The combine does not fail.
28. dawnshroud/"Denns Rootenpaw", hand "Bone Collector's Bag" (69948). Requires `paladin_epic` ==5. Gives "Enchanted Bone Powder" (69949).
29. Hand "Enchanted Bone Powder" (69949) to letalis/"Drema Young". Spawns "Drema Young" (169128). Loot "Drema's Soulstone" (69928) from "Drema Young".
30. Loot "Soulstone Shard" (69950) from "Coterie Corruptor" in `tenebrous`.
31. Spawns "Shade of Mujaki the Devourer" (204081) in `ponightmare` on event death_complete:204080.
32. Loot "Soulstone Shard" (69951) from "Shade of Mujaki the Devourer".
33. Combine in "Drema's Soulstone" (69928): "Soulstone Shard" (69950), "Soulstone Shard" (69951). Produces "Drema's Soulstone" (69952). The combine does not fail.
34. abysmal/"Lovine Lemise", say "Ingredients". Requires `paladin_epic` ==5. Gives "Lovine's Potion Bag" (69922).
35. Loot "Ra'Tuk Screambringer's Jaw" (69921) from "A Ra'Tuk Screambringer" (NPC 283104) in `barindu`. Drop cache: 4.06% chance per kill.
36. Loot "Noc Fleshfeasters Tail" (69920) from "A Noc Fleshfeaster" in `riwwi`.
37. Loot "Mastruq Havocblade Blood" (69919) from "A Mastruq Havocblade" in `qinimi`.
38. Loot "Mastruq Havocblade Blood" (69919) from "A Mastruq Warfiend" in `qinimi`.
39. Loot "Potameid Seaweed Strands" (69918) from "An Entrapped Potameid" in `natimbi`.
40. Combine in "Lovine's Potion Bag" (69922): "Ra'Tuk Screambringer's Jaw" (69921), "Noc Fleshfeasters Tail" (69920), "Mastruq Havocblade Blood" (69919), "Potameid Seaweed Strands" (69918). Produces "Lovine's Potion Bag" (69923). The combine does not fail.
41. abysmal/"Lovine Lemise", hand "Lovine's Potion Bag" (69923). Sets `paladin_epic_reiya` to `1`.
42. Summon "Foldable Medicine Bag" (17770) by casting "Unfold Medicine Bag".
43. Common item: Fine Potion Vial (95846). Listed in 15 zones.
44. Loot "Robust Shadow Essence" (96911) from "Qua Senshali Xakra" (NPC 158020) in `vexthal`. Drop cache: 28.72% chance per kill.
45. Loot "Sage Leaf" (14215) from "a Di'zok Herbalist" in `chardok`.
46. Loot "Sage Leaf" (14215) from "a Sarnak Herb Collector" in `chardok`.
47. Loot "Sage Leaf" (14215) from "an Apprentice Herbalist" in `chardok`.
48. Loot "Valerian Root" (14230) from "a Di'zok Herbalist" in `chardok`.
49. Loot "Valerian Root" (14230) from "a Sarnak Herb Collector" in `chardok`.
50. Loot "Valerian Root" (14230) from "an Apprentice Herbalist" in `chardok`.
51. Common item: Woundwart (16526). Listed in 9 zones.
52. Combine in "Foldable Medicine Bag" (17770): "Fine Potion Vial" (95846), "Robust Shadow Essence" (96911), "Sage Leaf" (14215), "Valerian Root" (14230), "Woundwart" (16526). Produces "Mist of the Breathless" (96937). Requires Alchemy, trivial 224.
53. abysmal/"Reiya The Pained", hand "Mist of the Breathless" (96937). Requires `paladin_epic_reiya` ==1. Gives "Reiya's Soulstone" (69924).
54. Unresolved cyclic prerequisite: `mage_epic` >=9.
55. draniksscar/"Iilivina", say "Primals". Sets `mage_epic` to `10`.
56. Spawns "Shade of Reiya the Pained" (284104) in `ferubi` on enter.
57. Loot "Soulstone Shard" (69943) from "Shade of Reiya the Pained".
58. Loot "Soulstone Shard" (69944) from "Vuranish Xxuro" in `vxed`.
59. Combine in "Reiya's Soulstone" (69924): "Soulstone Shard" (69943), "Soulstone Shard" (69944). Produces "Reiya's Soulstone" (69942). The combine does not fail.
60. Loot "Tainted Darksteel Sword" (29000) from "Keeper of the Tombs" in `hole`.
61. freeporteast/"Peasant Woman", say "I Will Take It". Gives "Bucket of Water" (29008).
62. freeporteast/"Joshua", hand "Bucket of Water" (29008). Gives "Bucket of Pure Water" (29009).
63. erudnext/"Reklon Gnallen", hand "Tainted Darksteel Sword" (29000) + "Bucket of Pure Water" (29009). Gives "Gleaming Crested Sword" (29003).
64. Loot "Tainted Darksteel Breastplate" (29001) from "Thought Destroyer" in `hateplaneb`.
65. kaladimb/"Nella Stonebraids", say "Dinner". Gives "Cold Plate of Beef and Bread" (29007).
66. kaladimb/"Jark", hand "Cold Plate of Beef and Bread" (29007). Gives "Pure Crystal" (29006).
67. erudnext/"Reklon Gnallen", hand "Tainted Darksteel Breastplate" (29001) + "Pure Crystal" (29006). Gives "Gleaming Crested Breastplate" (29004).
68. Loot "Tainted Darksteel Shield" (29002) from "Kirak Vil" in `nektulos`.
69. felwithea/"Elia The Pure", hand "Tainted Darksteel Shield" (29002). Gives "Gleaming Crested Shield" (29005).
70. erudnext/"Reklon Gnallen", hand "Gleaming Crested Sword" (29003) + "Gleaming Crested Breastplate" (29004) + "Gleaming Crested Shield" (29005). Gives "Mark of Atonement" (29010).
71. No quest step gives Drom's Champagne (13829). The dump lists it in freeporteast, freporte, highpasshold.
72. freeporteast/"Tykar Renlin", hand "Drom's Champagne" (13829) + "Drom's Champagne" (13829) + "Drom's Champagne" (13829) + "Drom's Champagne" (13829). Gives "Bunker Cell #1" (12196).
73. Summon "Black Diamond of Nightmares" (29990) by casting "Imbue Nightmare".
74. potranquility/"Elder Fuirstel", say "Hail". Sets `pop_cod_final` to `1`.
75. poknowledge/"Aid Grimel", say "Versed In The Art Of Smithing". Requires `pop_cod_final` ==1. Requires `pop_cod_final` set. Gives "Filthy Breastplate" (15984).
76. Combine in "Mixing Bowl" (17906): "Celestial Solvent" (9731), "Words of Acquisition (Beza)" (11866). Produces "Celestial Essence" (9650). Requires Baking, trivial 15. The combine does not fail.
77. Combine in "Mixing Bowl" (17906): "Celestial Solvent" (9731), "Words of Burnishing" (11862). Produces "Celestial Essence" (9650). Requires Baking, trivial 15. The combine does not fail.
78. 67 other recipes also produce Celestial Essence (9650).
79. Common item: Jar of Acid (22133). Listed in 15 zones.
80. Combine in Brew Barrel (19): "Celestial Essence" (9650), "Jar of Acid" (22133). Produces "Acid Wash" (15987). Requires Brewing, trivial 151.
81. Combine in Forge (17): "Filthy Breastplate" (15984), "Acid Wash" (15987). Produces "Cleansed Breastplate" (15998). Requires Blacksmithing, trivial 227.
82. Common item: Mortar and Pestle (17904). Listed in 12 zones.
83. Loot "Sandstorm Pearl" (29909) from "Rorek Steelthorn" (NPC 209081) in `bothunder`. Drop cache: 5.33% chance per kill.
84. Combine in "Mortar and Pestle" (17904): "Sandstorm Pearl" (29909). Produces "Powdered Sandstorm Pearl" (29520) x4. Requires Make Poison, trivial 255.
85. Common item: Firing Sheet (16906). Listed in 34 zones.
86. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
87. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `steamfont`.
88. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `tox`.
89. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `toxxulia`.
90. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
91. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). The combine does not fail.
92. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
93. Say "Tm Devrak Death" to rujd/"Rujd".
94. Spawns "spawn chest with Heavy Orcish Prison Key" (245241).
95. Loot "Pod of Water" (13044) from "spawn chest with Heavy Orcish Prison Key".
96. 6 alternative loot source(s) also yield Pod of Water (13044).
97. Forage "Pod of Water" (13044) in `ruja`.
98. Forage "Pod of Water" (13044) in `uqua`.
99. Forage "Pod of Water" (13044) in `yxtta`.
100. Combine in Brew Barrel (19): "Bottle of Aged Bloodwine" (51163), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aged Bloodwine" (51164). Requires Brewing, trivial 255.
101. Combine in Brew Barrel (19): "Bottle of Aldo's Bitter Ale" (75805), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aldo's Bitter Ale" (75811). Requires Brewing, trivial 15.
102. 17 other recipes also produce Bottle (16598).
103. Combine in Brew Barrel (19): "Pod of Water" (13044), "Bottle" (16598). Produces "Water Flask" (13006). Requires Brewing, trivial 21.
104. Combine in Pottery Wheel (21): "Water Flask" (13006), "Block of Clay" (16901). Produces "Small Block of Clay" (16900) x3. Requires Pottery, trivial 21.
105. Combine in Pottery Wheel (21): "Small Block of Clay" (16900), "Water Flask" (13006). Produces "Block of Clay" (16901). Requires Pottery, trivial 21.
106. Combine in Pottery Wheel (21): "Water Flask" (13006), "Large Block of Clay" (16902). Produces "Block of Clay" (16901) x2. Requires Pottery, trivial 21.
107. Combine in Pottery Wheel (21): "Block of Clay" (16901), "Water Flask" (13006). Produces "Large Block of Clay" (16902). Requires Pottery, trivial 21.
108. Common item: Large Bowl Sketch (16963). Listed in 29 zones.
109. Combine in Pottery Wheel (21): "Large Block of Clay" (16902), "Water Flask" (13006), "Large Bowl Sketch" (16963). Produces "Unfired Mixing Bowl" (16930). Requires Pottery, trivial 128.
110. Combine in Kiln (22): "Firing Sheet" (16906), "Unfired Mixing Bowl" (16930). Produces "Mixing Bowl" (17906). Requires Pottery, trivial 15.
111. Combine in "Mixing Bowl" (17906): "Sandstorm Pearl" (29909). Produces "Powdered Sandstorm Pearl" (29520) x4. Requires Baking. The combine does not fail.
112. Spawns "a Koka'Vor chieftain" (210236) in `postorms` on event_signal.
113. Loot "Storm Rider Blood" (29526) from "a Koka'Vor chieftain".
114. Loot "Drop of Pure Rain" (29904) from "A vann stav" (NPC 209018) in `bothunder`. Drop cache: 4% chance per kill.
115. Combine in Brew Barrel (19): "Powdered Sandstorm Pearl" (29520), "Storm Rider Blood" (29526), "Drop of Pure Rain" (29904). Produces "Hurricane Temper" (29533). Requires Brewing, trivial 135.
116. Combine in Forge (17): "Cleansed Breastplate" (15998), "Hurricane Temper" (29533). Produces "Tempered Breastplate" (15999). Requires Blacksmithing, trivial 229.
117. Combine in Forge (17): "Black Diamond of Nightmares" (29990), "Tempered Breastplate" (15999). Produces "Imbued Breastplate" (15985). Requires Blacksmithing 220. Trivial at 275.
118. poknowledge/"Aid Grimel", hand "Imbued Breastplate" (15985). Gives "Hardened Leather Signet" (16249).
119. poknowledge/"Aid Grimel", say "Skill In Brewing". Requires `pop_cod_final` ==1. Requires `pop_cod_final` set. Gives "Portable Drink Barrel" (17179).
120. Loot "Snake Scales" (13070) from "A Kerra Snake" (NPC 98017) in `erudsxing`. Drop cache: 59.23% chance per kill.
121. Combine in "Portable Drink Barrel" (17179): "Water Flask" (13006), "Snake Scales" (13070), "Bottle" (16598). Produces "Bog Juice" (16581). Requires Brewing, trivial 21.
122. Common item: Spit (17947). Listed in 34 zones.
123. Loot "Fire Beetle Eye" (10307) from "A Klicnik Drone" (NPC 2021) in `qeynos2`. Drop cache: 100% chance per kill.
124. Spawns "Sepsis Rat" (45113) in `qcat` on event_death.
125. Loot "Rat Ears" (13072) from "Sepsis Rat".
126. 2 alternative loot source(s) also yield Rat Ears (13072).
127. Combine in "Spit" (17947): "Fire Beetle Eye" (10307), "Rat Ears" (13072). Produces "Edible Goo" (13498). Requires Baking, trivial 21.
128. freeporteast/"A Prisoner", hand "Bunker Cell #1" (12196) + "Edible Goo" (13498) + "Bog Juice" (16581). Gives "H. K. 102" (12143).
129. highkeep/"Assistant Kiolna", hand "H. K. 102" (12143). Gives "Sealed Note" (18936).
130. paw/"Brother Hayle", hand "Sealed Note" (18936). Gives "Note" (18937).
131. Kill freportw/"Sir Lucan D-Lere". Spawns "Sir Lucan D'Lere" (9147).
132. Loot "Testimony of Truth" (18827) from "Sir Lucan D'Lere".
133. freeportwest/"Valeron Dushire", hand "Testimony of Truth" (18827). Gives "Brilliant Sword of Faith" (13947).
134. Loot "Spider Venom Sac" (14018) from "Stone Spider" (NPC 32057) in `soldungb`. Drop cache: 51% chance per kill.
135. freeportwest/"Merko Quetalis", hand "Spider Venom Sac" (14018). Gives "Token of Bravery" (12144).
136. **Broken:** nothing in the graph gives, loots, spawns, or combines Blackbox XIVD (13344).
137. akanon/"Baxok Curhunter", hand "Blackbox XIVD" (13344). Gives "Cloth Shirt" (1004).
138. commonlands/"Altunic Jartin", hand "Cloth Shirt" (1004). Gives "Token of Generosity" (13865).
139. Hand "Token of Bravery" (12144) + "Token of Generosity" (13865) to freeportwest/"Merko Quetalis". Spawns "spawns Guard Willia" (383270). Loot "Token of Truth" (13866) from "spawns Guard Willia".
140. 1 alternative loot source(s) also yield Token of Truth (13866).
141. freeportwest/"Merko Quetalis", hand "Token of Truth" (13866). Gives "Testimony" (18828).
142. Loot "Glowing Sword Hilt" (12197) from "Xicotl" in `mistmoore`.
143. paw/"Brother Hayle", hand "Glowing Sword Hilt" (12197) + "Brilliant Sword of Faith" (13947) + "Testimony" (18828) + "Note" (18937). Gives "SoulFire" (5504).
144. airplane/"Inte Akera", hand "SoulFire" (5504). Gives "Inte's First Blessing" (18033).
145. neriakc/"Selzar L-Crit", say "Armor". Gives "Note to Kanthuk" (2416).
146. butcher/"Kanthuk Ogrebane", hand "Note to Kanthuk" (2416). Sets `Kanthuk` to `ghoul`.
147. butcher/"Kanthuk Ogrebane", say "Strange Image". Requires `Kanthuk` set. Gives "Pendant" (2414).
148. cauldron/"Llara", hand "Pendant" (2414). Sets `Llara` to `ghoul`.
149. cauldron/"Llara", say "Ruathey". Requires `Llara` set. Gives "Note to Ruathey" (2417).
150. lavastorm/"Ruathey", hand "Note to Ruathey" (2417). Sets `Ruathey` to `ghoul`.
151. lavastorm/"Ruathey", hand "Note to Ruathey" (2417). Sets `ruathey_note` to `1`.
152. lavastorm/"Ruathey", say "Bag". Requires `Ruathey` set. Requires `ruathey_note` ==1. Requires `ruathey_note` set. Gives "Nobleman's Bag" (17878).
153. Loot "Ghoul's Heart" (2410) from "A Ghoul" (NPC 63011) in `unrest`. Drop cache: 25% chance per kill.
154. Loot "Amstaf's Scroll" (2411) from "A Goblin Thief" (NPC 6150) in `highkeep`. Drop cache: 35% chance per kill.
155. Loot "Blade of Nobility" (2412) from "A Crazed Goblin" (NPC 68162) in `butcher`. Drop cache: 10.57% chance per kill.
156. Loot "Hilt of the Nobleman" (2413) from "Ekeros" in `najena`.
157. Loot "Hilt of the Nobleman" (2413) from "A Skeleton" in `najena`.
158. Combine in "Nobleman's Bag" (17878): "Ghoul's Heart" (2410), "Amstaf's Scroll" (2411), "Blade of Nobility" (2412), "Hilt of the Nobleman" (2413). Produces "Ghoulbane" (5403). The combine does not fail.
159. airplane/"Inte Akera", hand "Ghoulbane" (5403). Gives "Inte's Second Blessing" (18034).
160. Loot "Torn, Burnt Book" (19071) from "Lord Nagafen" in `soldungb`.
161. Loot "Torn, Burnt Book" (19071) from "Melalafen" in `westwastes`.
162. Loot "Torn, Burnt Book" (19071) from "Severilous" in `emeraldjungle`.
163. Loot "Torn, Burnt Book" (19071) from "Talendor" in `skyfire`.
164. Loot "Torn, Burnt Book" (19071) from "The Fabled Severilous".
165. Loot "Torn, Frost-covered Book" (19070) from "Faydedar" in `timorous`.
166. Loot "Torn, Frost-covered Book" (19070) from "Gorenaire" in `dreadlands`.
167. Loot "Torn, Frost-covered Book" (19070) from "Lady Vox" in `permafrost`.
168. neriakb/"Rysva To-Biath", hand "Torn, Frost-covered Book" (19070) + "Torn, Burnt Book" (19071). Gives "Book of Scale" (18302).
169. oceanoftears/"Oracle Of K-Arnon", hand "Book of Scale" (18302). Gives "Miragul's Phylactery" (19072).
170. Hand "Miragul's Phylactery" (19072) to everfrost/"Lich Of Miragul". Spawns "Spawn Miragul" (30094). Loot "Miragul's Head" (19073) from "Spawn Miragul".
171. Hand "Miragul's Phylactery" (19072) to everfrost/"Lich Of Miragul". Spawns "Spawn Miragul" (30094). Loot "Miragul's Robe" (1254) from "Spawn Miragul".
172. airplane/"Inte Akera", hand "Miragul's Robe" (1254) + "Inte's First Blessing" (18033) + "Inte's Second Blessing" (18034) + "Miragul's Head" (19073). Gives "Fiery Avenger" (11050).
173. fearplane/"Irak Altil", hand "Fiery Avenger" (11050) + "Mark of Atonement" (29010). Gives "Fiery Defender" (10099).
174. hohonora/"Irak Altil", say "Hail". Sets `paladin_epic` to `6`.
175. Loot "Top Section of an Engraved Signet" (9956) from "An Ikaav Miragenist" (NPC 301015) in `bloodfields`. Drop cache: 6.08% chance per kill.
176. Loot "Bottom Section of an Engraved Signet" (10399) from "An Ikaav Castigator" (NPC 301003) in `bloodfields`. Drop cache: 4% chance per kill.
177. Loot "Center Section of an Engraved Signet" (10235) from "An Ikaav Deathbeckoner" (NPC 301008) in `bloodfields`. Drop cache: 5.13% chance per kill.
178. bloodfields/"Cryssa", hand "Top Section of an Engraved Signet" (9956) + "Center Section of an Engraved Signet" (10235) + "Bottom Section of an Engraved Signet" (10399). Gives "Enchanted Signet of the Disciples" (12080).
179. bloodfields/"Cryssa", hand "Top Section of an Engraved Signet" (9956) + "Center Section of an Engraved Signet" (10235) + "Bottom Section of an Engraved Signet" (10399). Sets `cleric20_darkdisciples` to `1`.
180. Loot "Redis' Soulstone" (69983) from "Shade of Redis Linrok" in `dranikcatacombsa`.
181. global/"Global Player", combine recipe 19914. Sets `ranger_epic` to `8`.
182. Spawns "Durunal the Cursebearer" (300087) in `wallofslaughter` on enter.
183. Loot "Dark and Twisted Sword" (69971) from "Durunal the Cursebearer".
184. hohonora/"Irak Altil", hand "Dark and Twisted Sword" (69971). Requires `paladin_epic` ==6. Gives "Dark and Twisted Sword" (69972).
185. Combine in "Dark and Twisted Sword" (69972): "Rithnok's Soulstone" (69941), "Drema's Soulstone" (69952), "Reiya's Soulstone" (69942), "Redis' Soulstone" (69983). Produces "Redemption" (64031). The combine does not fail.
186. hohonora/"Irak Altil", say "Tell Me About Your Master". Sets `paladin_epic` to `9`.
187. qeynos2/"Camlend Serbold", say "Gem". Requires `paladin_epic` ==9. Gives "Unfilled Set of Prayer Beads" (69968).
188. rivervale/"Kaya Cloudfoot", say "Different About It". Requires `paladin_epic` ==9. Gives "Note from Kaya" (69970).
189. rivervale/"Deputy Cheel", hand "Note from Kaya" (69970). Gives "Rivervale Prayer Bead" (69967).
190. akanon/"Lewis Reldnok", say "Blessed Gem". Triggers `akanon/lewis reldnok#timer:check_sit`.
191. Sit before the NPC while its timer checks your posture.
192. akanon/"Lewis Reldnok", on timer check_sit. Gives "Ak'anon Prayer Bead" (69966).
193. erudnint/"Josper Kenshed", say "Collect Component". Gives "Empty Bag" (17944).
194. Loot "Goblin Ice Necklace" (13897) from "Redwind" in `everfrost`.
195. Loot "Goblin Ice Necklace" (13897) from "An Ice Goblin Scout" in `everfrost`.
196. Loot "Goblin Ice Necklace" (13897) from "An Ice Goblin Whelp" in `everfrost`.
197. Loot "Goblin Ice Necklace" (13897) from "An Icy Orc" in `everfrost`.
198. Loot "Goblin Ice Necklace" (13897) from "Ice Goblin Diver" in `everfrost`.
199. Combine in "Empty Bag" (17944): "Goblin Ice Necklace" (13897). Produces "Bag of Ice Necklaces" (13898). The combine does not fail.
200. halas/"Lysbith Mcnaff", hand "Bag of Ice Necklaces" (13898). Gives "Iron Ration" (13005).
201. Loot "Cask" (16580) from "Tugog Grigol" in `rathemtn`.
202. Common item: Hops (16591). Listed in 31 zones.
203. Common item: Malt (16595). Listed in 30 zones.
204. Common item: Yeast (16596). Listed in 30 zones.
205. Combine in "Portable Drink Barrel" (17179): "Cask" (16580), "Hops" (16591), "Malt" (16595), "Yeast" (16596). Produces "Mead" (13008). Requires Brewing, trivial 41.
206. erudnext/"Reklon Gnallen", hand "Iron Ration" (13005) + "Mead" (13008). Requires `paladin_epic` ==9. Gives "Erudin Prayer Bead" (69965).
207. Summon "Quiver of Marr" (17307) by casting "Quiver of Marr".
208. rathemtn/"Shin Master Grubbus", hand "Quiver of Marr" (17307). Requires `paladin_epic` ==9. Gives "Gukta Prayer Bead" (69964).
209. Common item: Barley (16590). Listed in 28 zones.
210. Combine in "Medicine Bag" (17901): "Hand-Formed Bottle" (45232), "Ensnaring Concoction V" (45236). Produces "Empty Vial" (10062), "Cork" (16851), "Formed Ensnaring Concoction V" (45258). Requires Alchemy, trivial 41.
211. Combine in Brew Barrel (19): "Bottle of Aged Bloodwine" (51163), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aged Bloodwine" (51164). Requires Brewing, trivial 255.
212. 11 other recipes also produce Cork (16851).
213. Combine in "Portable Drink Barrel" (17179): "Water Flask" (13006), "Celestial Essence" (9650). Produces "Purified Water" (12607). Requires Brewing, trivial 58.
214. Combine in "Tracker's Water Extractor" (17987): "Purification Tablet" (12630), "Water Reed" (12778). Produces "Purified Water" (12607) x3. Requires Pottery. The combine does not fail.
215. 3 other recipes also produce Purified Water (12607).
216. Forage "Sand Verbena" (65582) in `taka`.
217. Forage "Sand Verbena" (65582) in `takb`.
218. Forage "Sand Verbena" (65582) in `takc`.
219. Forage "Sand Verbena" (65582) in `takd`.
220. Forage "Sand Verbena" (65582) in `take`.
221. Forage "Sand Verbena" (65582) in `takf`.
222. Forage "Sand Verbena" (65582) in `takg`.
223. Forage "Sand Verbena" (65582) in `takh`.
224. Forage "Sand Verbena" (65582) in `taki`.
225. Forage "Sand Verbena" (65582) in `takj`.
226. Combine in Brew Barrel (19): "Barley" (16590), "Bottle" (16598), "Cork" (16851), "Hops" (16591), "Purified Water" (12607), "Sand Verbena" (65582), "Yeast" (16596). Produces "Bottle of Double Brewed Double Dry Stout" (51157). Requires Brewing, trivial 226.
227. kaladimb/"Datur Nightseer", hand "Bottle of Double Brewed Double Dry Stout" (51157). Requires `paladin_epic` ==9. Gives "Kaladim Prayer Bead" (69963).
228. felwithea/"General Jyleel", hand platinum:1000. Requires `paladin_epic` ==9. Gives "Felwithe Prayer Bead" (69962).
229. Ground spawn of "Freeport Prayer Bead" (69961) in `freeportwest`.
230. Ground spawn of "Freeport Prayer Bead" (69961) in `freportn`.
231. qeynos2/"Ziska Ironforge", hand platinum:500. Requires `paladin_epic` ==9. Gives "Qeynos Prayer Bead" (69960).
232. Combine in "Unfilled Set of Prayer Beads" (69968): "Rivervale Prayer Bead" (69967), "Ak'anon Prayer Bead" (69966), "Erudin Prayer Bead" (69965), "Gukta Prayer Bead" (69964), "Kaladim Prayer Bead" (69963), "Felwithe Prayer Bead" (69962), "Freeport Prayer Bead" (69961), "Qeynos Prayer Bead" (69960). Produces "Set of Prayer Beads" (69969). The combine does not fail.
233. dranikhollowsc/"Anetal", hand "Set of Prayer Beads" (69969). Sets `paladin_epic_hollowc` to `2`.
234. natimbi/"Kemik Arulon", hand "Set of Prayer Beads" (69969). Sets `paladin_epic_hollowc` to `1`.
235. natimbi/"Kemik Arulon", say "Hail". Requires `paladin_epic_hollowc` ==2. Requires `paladin_epic` ==9. Requires `paladin_epic_hollowc` ==1. Gives "Token of Compassion" (69953).
236. oasis/"Paladin Epic", say "Hail". Requires `pal_chest_keel` unset. Gives "Keelee's Brooch" (69982).
237. sro/"Instructor Maerceci", hand "Keelee's Brooch" (69982). Gives "Token of Chivalry" (69954).

### "Token of Heroism" (69955)

1. Loot "Valdoon Kel'Novar's Heart" (69981) from "Valdoon Kel'Novar" in `mmcc`.
2. felwithea/"Galrun Starforge", hand "Valdoon Kel'Novar's Heart" (69981). Gives "Token of Cleansing" (69956).
3. provinggrounds/"Pashia Clouddancer", say "Note". Gives "Note from Pashia" (69973).
4. nedaria/"Duram Firechaser", hand "Note from Pashia" (69973). Gives "Token of Heroism" (69955).

### "Token of Cleansing" (69956)

1. Loot "Valdoon Kel'Novar's Heart" (69981) from "Valdoon Kel'Novar" in `mmcc`.
2. felwithea/"Galrun Starforge", hand "Valdoon Kel'Novar's Heart" (69981). Gives "Token of Cleansing" (69956).

### "Scabbard of the Righteous" (69959)

1. Spawns "A Corrupted Koalindl" (69141) in `oot` on event_fish_success.
2. Loot "Corrupted Koalindl's Heart" (69929) from "A Corrupted Koalindl".
3. Spawns "A Corrupted Koalindl" (224432) in `gunthak` on event_fish_success.
4. Loot "Corrupted Koalindl's Heart" (69930) from "A Corrupted Koalindl".
5. Spawns "A Corrupted Koalindl" (93306) in `overthere` on event_fish_success.
6. Loot "Corrupted Koalindl's Heart" (69931) from "A Corrupted Koalindl".
7. Spawns "A Corrupted Koalindl" (182150) in `nedaria` on event_fish_success.
8. Loot "Corrupted Koalindl's Heart" (69932) from "A Corrupted Koalindl".
9. qeynos2/"Enic Ruklin", hand "Corrupted Koalindl's Heart" (69929) + "Corrupted Koalindl's Heart" (69930) + "Corrupted Koalindl's Heart" (69931) + "Corrupted Koalindl's Heart" (69932). Sets `paladin_epic` to `4`.
10. qeynos2/"Enic Ruklin", hand "Corrupted Koalindl's Heart" (69929) + "Corrupted Koalindl's Heart" (69930) + "Corrupted Koalindl's Heart" (69931) + "Corrupted Koalindl's Heart" (69932). Gives "Seal of Enic" (69933).
11. Say "Hail" to skyfire/"Dry Sapara".
12. Spawns "Rithnok the Tormented" (91193).
13. Loot "Rithnok's Soulstone" (69935) from "Rithnok the Tormented".
14. skyfire/"Dry Sapara", hand "Rithnok's Soulstone" (69935). Gives "Rithnok's Soulstone" (69936).
15. Ground spawn of "Soulstone Shard" (69937) in `draniksscar`.
16. Ground spawn of "Soulstone Shard" (69938) in `bloodfields`.
17. Ground spawn of "Soulstone Shard" (69939) in `causeway`.
18. Ground spawn of "Soulstone Shard" (69940) in `dranik`.
19. Combine in "Rithnok's Soulstone" (69936): "Soulstone Shard" (69937), "Soulstone Shard" (69938), "Soulstone Shard" (69939), "Soulstone Shard" (69940). Produces "Rithnok's Soulstone" (69941). The combine does not fail.
20. dawnshroud/"Mikhal Young", hand "Drema's Fingerbone" (69946). Sets `paladin_epic` to `5`.
21. dawnshroud/"Mikhal Young", say "Find Anything". Requires `paladin_epic` ==4. Gives "Drema's Locket" (69945).
22. letalis/"Drema Young", hand "Drema's Locket" (69945). Requires `paladin_epic` set. Requires `paladin_epic` >=4. Gives "Drema's Fingerbone" (69946).
23. dawnshroud/"Denns Rootenpaw", hand "Drema's Fingerbone" (69946). Requires `paladin_epic` ==5. Gives "Bone Collector's Bag" (69947).
24. Loot "Dark Skeleton Remains" (69927) from "A Sun Revenant" in `thegrey`.
25. Loot "Dark Skeleton Remains" (69926) from "Disturbed Elysian Remains" (NPC 176016) in `umbral`. Drop cache: 2.58% chance per kill.
26. Loot "Dark Skeleton Remains" (69925) from "A Soriz Slave" (NPC 162029) in `ssratemple`. Drop cache: 35% chance per kill.
27. Combine in "Bone Collector's Bag" (69947): "Dark Skeleton Remains" (69927), "Dark Skeleton Remains" (69926), "Dark Skeleton Remains" (69925). Produces "Bone Collector's Bag" (69948). The combine does not fail.
28. dawnshroud/"Denns Rootenpaw", hand "Bone Collector's Bag" (69948). Requires `paladin_epic` ==5. Gives "Enchanted Bone Powder" (69949).
29. Hand "Enchanted Bone Powder" (69949) to letalis/"Drema Young". Spawns "Drema Young" (169128). Loot "Drema's Soulstone" (69928) from "Drema Young".
30. Loot "Soulstone Shard" (69950) from "Coterie Corruptor" in `tenebrous`.
31. Spawns "Shade of Mujaki the Devourer" (204081) in `ponightmare` on event death_complete:204080.
32. Loot "Soulstone Shard" (69951) from "Shade of Mujaki the Devourer".
33. Combine in "Drema's Soulstone" (69928): "Soulstone Shard" (69950), "Soulstone Shard" (69951). Produces "Drema's Soulstone" (69952). The combine does not fail.
34. abysmal/"Lovine Lemise", say "Ingredients". Requires `paladin_epic` ==5. Gives "Lovine's Potion Bag" (69922).
35. Loot "Ra'Tuk Screambringer's Jaw" (69921) from "A Ra'Tuk Screambringer" (NPC 283104) in `barindu`. Drop cache: 4.06% chance per kill.
36. Loot "Noc Fleshfeasters Tail" (69920) from "A Noc Fleshfeaster" in `riwwi`.
37. Loot "Mastruq Havocblade Blood" (69919) from "A Mastruq Havocblade" in `qinimi`.
38. Loot "Mastruq Havocblade Blood" (69919) from "A Mastruq Warfiend" in `qinimi`.
39. Loot "Potameid Seaweed Strands" (69918) from "An Entrapped Potameid" in `natimbi`.
40. Combine in "Lovine's Potion Bag" (69922): "Ra'Tuk Screambringer's Jaw" (69921), "Noc Fleshfeasters Tail" (69920), "Mastruq Havocblade Blood" (69919), "Potameid Seaweed Strands" (69918). Produces "Lovine's Potion Bag" (69923). The combine does not fail.
41. abysmal/"Lovine Lemise", hand "Lovine's Potion Bag" (69923). Sets `paladin_epic_reiya` to `1`.
42. Summon "Foldable Medicine Bag" (17770) by casting "Unfold Medicine Bag".
43. Common item: Fine Potion Vial (95846). Listed in 15 zones.
44. Loot "Robust Shadow Essence" (96911) from "Qua Senshali Xakra" (NPC 158020) in `vexthal`. Drop cache: 28.72% chance per kill.
45. Loot "Sage Leaf" (14215) from "a Di'zok Herbalist" in `chardok`.
46. Loot "Sage Leaf" (14215) from "a Sarnak Herb Collector" in `chardok`.
47. Loot "Sage Leaf" (14215) from "an Apprentice Herbalist" in `chardok`.
48. Loot "Valerian Root" (14230) from "a Di'zok Herbalist" in `chardok`.
49. Loot "Valerian Root" (14230) from "a Sarnak Herb Collector" in `chardok`.
50. Loot "Valerian Root" (14230) from "an Apprentice Herbalist" in `chardok`.
51. Common item: Woundwart (16526). Listed in 9 zones.
52. Combine in "Foldable Medicine Bag" (17770): "Fine Potion Vial" (95846), "Robust Shadow Essence" (96911), "Sage Leaf" (14215), "Valerian Root" (14230), "Woundwart" (16526). Produces "Mist of the Breathless" (96937). Requires Alchemy, trivial 224.
53. abysmal/"Reiya The Pained", hand "Mist of the Breathless" (96937). Requires `paladin_epic_reiya` ==1. Gives "Reiya's Soulstone" (69924).
54. Unresolved cyclic prerequisite: `mage_epic` >=9.
55. draniksscar/"Iilivina", say "Primals". Sets `mage_epic` to `10`.
56. Spawns "Shade of Reiya the Pained" (284104) in `ferubi` on enter.
57. Loot "Soulstone Shard" (69943) from "Shade of Reiya the Pained".
58. Loot "Soulstone Shard" (69944) from "Vuranish Xxuro" in `vxed`.
59. Combine in "Reiya's Soulstone" (69924): "Soulstone Shard" (69943), "Soulstone Shard" (69944). Produces "Reiya's Soulstone" (69942). The combine does not fail.
60. Loot "Tainted Darksteel Sword" (29000) from "Keeper of the Tombs" in `hole`.
61. freeporteast/"Peasant Woman", say "I Will Take It". Gives "Bucket of Water" (29008).
62. freeporteast/"Joshua", hand "Bucket of Water" (29008). Gives "Bucket of Pure Water" (29009).
63. erudnext/"Reklon Gnallen", hand "Tainted Darksteel Sword" (29000) + "Bucket of Pure Water" (29009). Gives "Gleaming Crested Sword" (29003).
64. Loot "Tainted Darksteel Breastplate" (29001) from "Thought Destroyer" in `hateplaneb`.
65. kaladimb/"Nella Stonebraids", say "Dinner". Gives "Cold Plate of Beef and Bread" (29007).
66. kaladimb/"Jark", hand "Cold Plate of Beef and Bread" (29007). Gives "Pure Crystal" (29006).
67. erudnext/"Reklon Gnallen", hand "Tainted Darksteel Breastplate" (29001) + "Pure Crystal" (29006). Gives "Gleaming Crested Breastplate" (29004).
68. Loot "Tainted Darksteel Shield" (29002) from "Kirak Vil" in `nektulos`.
69. felwithea/"Elia The Pure", hand "Tainted Darksteel Shield" (29002). Gives "Gleaming Crested Shield" (29005).
70. erudnext/"Reklon Gnallen", hand "Gleaming Crested Sword" (29003) + "Gleaming Crested Breastplate" (29004) + "Gleaming Crested Shield" (29005). Gives "Mark of Atonement" (29010).
71. No quest step gives Drom's Champagne (13829). The dump lists it in freeporteast, freporte, highpasshold.
72. freeporteast/"Tykar Renlin", hand "Drom's Champagne" (13829) + "Drom's Champagne" (13829) + "Drom's Champagne" (13829) + "Drom's Champagne" (13829). Gives "Bunker Cell #1" (12196).
73. Summon "Black Diamond of Nightmares" (29990) by casting "Imbue Nightmare".
74. potranquility/"Elder Fuirstel", say "Hail". Sets `pop_cod_final` to `1`.
75. poknowledge/"Aid Grimel", say "Versed In The Art Of Smithing". Requires `pop_cod_final` ==1. Requires `pop_cod_final` set. Gives "Filthy Breastplate" (15984).
76. Combine in "Mixing Bowl" (17906): "Celestial Solvent" (9731), "Words of Acquisition (Beza)" (11866). Produces "Celestial Essence" (9650). Requires Baking, trivial 15. The combine does not fail.
77. Combine in "Mixing Bowl" (17906): "Celestial Solvent" (9731), "Words of Burnishing" (11862). Produces "Celestial Essence" (9650). Requires Baking, trivial 15. The combine does not fail.
78. 67 other recipes also produce Celestial Essence (9650).
79. Common item: Jar of Acid (22133). Listed in 15 zones.
80. Combine in Brew Barrel (19): "Celestial Essence" (9650), "Jar of Acid" (22133). Produces "Acid Wash" (15987). Requires Brewing, trivial 151.
81. Combine in Forge (17): "Filthy Breastplate" (15984), "Acid Wash" (15987). Produces "Cleansed Breastplate" (15998). Requires Blacksmithing, trivial 227.
82. Common item: Mortar and Pestle (17904). Listed in 12 zones.
83. Loot "Sandstorm Pearl" (29909) from "Rorek Steelthorn" (NPC 209081) in `bothunder`. Drop cache: 5.33% chance per kill.
84. Combine in "Mortar and Pestle" (17904): "Sandstorm Pearl" (29909). Produces "Powdered Sandstorm Pearl" (29520) x4. Requires Make Poison, trivial 255.
85. Common item: Firing Sheet (16906). Listed in 34 zones.
86. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
87. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `steamfont`.
88. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `tox`.
89. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `toxxulia`.
90. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
91. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). The combine does not fail.
92. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
93. Say "Tm Devrak Death" to rujd/"Rujd".
94. Spawns "spawn chest with Heavy Orcish Prison Key" (245241).
95. Loot "Pod of Water" (13044) from "spawn chest with Heavy Orcish Prison Key".
96. 6 alternative loot source(s) also yield Pod of Water (13044).
97. Forage "Pod of Water" (13044) in `ruja`.
98. Forage "Pod of Water" (13044) in `uqua`.
99. Forage "Pod of Water" (13044) in `yxtta`.
100. Combine in Brew Barrel (19): "Bottle of Aged Bloodwine" (51163), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aged Bloodwine" (51164). Requires Brewing, trivial 255.
101. Combine in Brew Barrel (19): "Bottle of Aldo's Bitter Ale" (75805), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aldo's Bitter Ale" (75811). Requires Brewing, trivial 15.
102. 17 other recipes also produce Bottle (16598).
103. Combine in Brew Barrel (19): "Pod of Water" (13044), "Bottle" (16598). Produces "Water Flask" (13006). Requires Brewing, trivial 21.
104. Combine in Pottery Wheel (21): "Water Flask" (13006), "Block of Clay" (16901). Produces "Small Block of Clay" (16900) x3. Requires Pottery, trivial 21.
105. Combine in Pottery Wheel (21): "Small Block of Clay" (16900), "Water Flask" (13006). Produces "Block of Clay" (16901). Requires Pottery, trivial 21.
106. Combine in Pottery Wheel (21): "Water Flask" (13006), "Large Block of Clay" (16902). Produces "Block of Clay" (16901) x2. Requires Pottery, trivial 21.
107. Combine in Pottery Wheel (21): "Block of Clay" (16901), "Water Flask" (13006). Produces "Large Block of Clay" (16902). Requires Pottery, trivial 21.
108. Common item: Large Bowl Sketch (16963). Listed in 29 zones.
109. Combine in Pottery Wheel (21): "Large Block of Clay" (16902), "Water Flask" (13006), "Large Bowl Sketch" (16963). Produces "Unfired Mixing Bowl" (16930). Requires Pottery, trivial 128.
110. Combine in Kiln (22): "Firing Sheet" (16906), "Unfired Mixing Bowl" (16930). Produces "Mixing Bowl" (17906). Requires Pottery, trivial 15.
111. Combine in "Mixing Bowl" (17906): "Sandstorm Pearl" (29909). Produces "Powdered Sandstorm Pearl" (29520) x4. Requires Baking. The combine does not fail.
112. Spawns "a Koka'Vor chieftain" (210236) in `postorms` on event_signal.
113. Loot "Storm Rider Blood" (29526) from "a Koka'Vor chieftain".
114. Loot "Drop of Pure Rain" (29904) from "A vann stav" (NPC 209018) in `bothunder`. Drop cache: 4% chance per kill.
115. Combine in Brew Barrel (19): "Powdered Sandstorm Pearl" (29520), "Storm Rider Blood" (29526), "Drop of Pure Rain" (29904). Produces "Hurricane Temper" (29533). Requires Brewing, trivial 135.
116. Combine in Forge (17): "Cleansed Breastplate" (15998), "Hurricane Temper" (29533). Produces "Tempered Breastplate" (15999). Requires Blacksmithing, trivial 229.
117. Combine in Forge (17): "Black Diamond of Nightmares" (29990), "Tempered Breastplate" (15999). Produces "Imbued Breastplate" (15985). Requires Blacksmithing 220. Trivial at 275.
118. poknowledge/"Aid Grimel", hand "Imbued Breastplate" (15985). Gives "Hardened Leather Signet" (16249).
119. poknowledge/"Aid Grimel", say "Skill In Brewing". Requires `pop_cod_final` ==1. Requires `pop_cod_final` set. Gives "Portable Drink Barrel" (17179).
120. Loot "Snake Scales" (13070) from "A Kerra Snake" (NPC 98017) in `erudsxing`. Drop cache: 59.23% chance per kill.
121. Combine in "Portable Drink Barrel" (17179): "Water Flask" (13006), "Snake Scales" (13070), "Bottle" (16598). Produces "Bog Juice" (16581). Requires Brewing, trivial 21.
122. Common item: Spit (17947). Listed in 34 zones.
123. Loot "Fire Beetle Eye" (10307) from "A Klicnik Drone" (NPC 2021) in `qeynos2`. Drop cache: 100% chance per kill.
124. Spawns "Sepsis Rat" (45113) in `qcat` on event_death.
125. Loot "Rat Ears" (13072) from "Sepsis Rat".
126. 2 alternative loot source(s) also yield Rat Ears (13072).
127. Combine in "Spit" (17947): "Fire Beetle Eye" (10307), "Rat Ears" (13072). Produces "Edible Goo" (13498). Requires Baking, trivial 21.
128. freeporteast/"A Prisoner", hand "Bunker Cell #1" (12196) + "Edible Goo" (13498) + "Bog Juice" (16581). Gives "H. K. 102" (12143).
129. highkeep/"Assistant Kiolna", hand "H. K. 102" (12143). Gives "Sealed Note" (18936).
130. paw/"Brother Hayle", hand "Sealed Note" (18936). Gives "Note" (18937).
131. Kill freportw/"Sir Lucan D-Lere". Spawns "Sir Lucan D'Lere" (9147).
132. Loot "Testimony of Truth" (18827) from "Sir Lucan D'Lere".
133. freeportwest/"Valeron Dushire", hand "Testimony of Truth" (18827). Gives "Brilliant Sword of Faith" (13947).
134. Loot "Spider Venom Sac" (14018) from "Stone Spider" (NPC 32057) in `soldungb`. Drop cache: 51% chance per kill.
135. freeportwest/"Merko Quetalis", hand "Spider Venom Sac" (14018). Gives "Token of Bravery" (12144).
136. **Broken:** nothing in the graph gives, loots, spawns, or combines Blackbox XIVD (13344).
137. akanon/"Baxok Curhunter", hand "Blackbox XIVD" (13344). Gives "Cloth Shirt" (1004).
138. commonlands/"Altunic Jartin", hand "Cloth Shirt" (1004). Gives "Token of Generosity" (13865).
139. Hand "Token of Bravery" (12144) + "Token of Generosity" (13865) to freeportwest/"Merko Quetalis". Spawns "spawns Guard Willia" (383270). Loot "Token of Truth" (13866) from "spawns Guard Willia".
140. 1 alternative loot source(s) also yield Token of Truth (13866).
141. freeportwest/"Merko Quetalis", hand "Token of Truth" (13866). Gives "Testimony" (18828).
142. Loot "Glowing Sword Hilt" (12197) from "Xicotl" in `mistmoore`.
143. paw/"Brother Hayle", hand "Glowing Sword Hilt" (12197) + "Brilliant Sword of Faith" (13947) + "Testimony" (18828) + "Note" (18937). Gives "SoulFire" (5504).
144. airplane/"Inte Akera", hand "SoulFire" (5504). Gives "Inte's First Blessing" (18033).
145. neriakc/"Selzar L-Crit", say "Armor". Gives "Note to Kanthuk" (2416).
146. butcher/"Kanthuk Ogrebane", hand "Note to Kanthuk" (2416). Sets `Kanthuk` to `ghoul`.
147. butcher/"Kanthuk Ogrebane", say "Strange Image". Requires `Kanthuk` set. Gives "Pendant" (2414).
148. cauldron/"Llara", hand "Pendant" (2414). Sets `Llara` to `ghoul`.
149. cauldron/"Llara", say "Ruathey". Requires `Llara` set. Gives "Note to Ruathey" (2417).
150. lavastorm/"Ruathey", hand "Note to Ruathey" (2417). Sets `Ruathey` to `ghoul`.
151. lavastorm/"Ruathey", hand "Note to Ruathey" (2417). Sets `ruathey_note` to `1`.
152. lavastorm/"Ruathey", say "Bag". Requires `Ruathey` set. Requires `ruathey_note` ==1. Requires `ruathey_note` set. Gives "Nobleman's Bag" (17878).
153. Loot "Ghoul's Heart" (2410) from "A Ghoul" (NPC 63011) in `unrest`. Drop cache: 25% chance per kill.
154. Loot "Amstaf's Scroll" (2411) from "A Goblin Thief" (NPC 6150) in `highkeep`. Drop cache: 35% chance per kill.
155. Loot "Blade of Nobility" (2412) from "A Crazed Goblin" (NPC 68162) in `butcher`. Drop cache: 10.57% chance per kill.
156. Loot "Hilt of the Nobleman" (2413) from "Ekeros" in `najena`.
157. Loot "Hilt of the Nobleman" (2413) from "A Skeleton" in `najena`.
158. Combine in "Nobleman's Bag" (17878): "Ghoul's Heart" (2410), "Amstaf's Scroll" (2411), "Blade of Nobility" (2412), "Hilt of the Nobleman" (2413). Produces "Ghoulbane" (5403). The combine does not fail.
159. airplane/"Inte Akera", hand "Ghoulbane" (5403). Gives "Inte's Second Blessing" (18034).
160. Loot "Torn, Burnt Book" (19071) from "Lord Nagafen" in `soldungb`.
161. Loot "Torn, Burnt Book" (19071) from "Melalafen" in `westwastes`.
162. Loot "Torn, Burnt Book" (19071) from "Severilous" in `emeraldjungle`.
163. Loot "Torn, Burnt Book" (19071) from "Talendor" in `skyfire`.
164. Loot "Torn, Burnt Book" (19071) from "The Fabled Severilous".
165. Loot "Torn, Frost-covered Book" (19070) from "Faydedar" in `timorous`.
166. Loot "Torn, Frost-covered Book" (19070) from "Gorenaire" in `dreadlands`.
167. Loot "Torn, Frost-covered Book" (19070) from "Lady Vox" in `permafrost`.
168. neriakb/"Rysva To-Biath", hand "Torn, Frost-covered Book" (19070) + "Torn, Burnt Book" (19071). Gives "Book of Scale" (18302).
169. oceanoftears/"Oracle Of K-Arnon", hand "Book of Scale" (18302). Gives "Miragul's Phylactery" (19072).
170. Hand "Miragul's Phylactery" (19072) to everfrost/"Lich Of Miragul". Spawns "Spawn Miragul" (30094). Loot "Miragul's Head" (19073) from "Spawn Miragul".
171. Hand "Miragul's Phylactery" (19072) to everfrost/"Lich Of Miragul". Spawns "Spawn Miragul" (30094). Loot "Miragul's Robe" (1254) from "Spawn Miragul".
172. airplane/"Inte Akera", hand "Miragul's Robe" (1254) + "Inte's First Blessing" (18033) + "Inte's Second Blessing" (18034) + "Miragul's Head" (19073). Gives "Fiery Avenger" (11050).
173. fearplane/"Irak Altil", hand "Fiery Avenger" (11050) + "Mark of Atonement" (29010). Gives "Fiery Defender" (10099).
174. hohonora/"Irak Altil", say "Hail". Sets `paladin_epic` to `6`.
175. Loot "Top Section of an Engraved Signet" (9956) from "An Ikaav Miragenist" (NPC 301015) in `bloodfields`. Drop cache: 6.08% chance per kill.
176. Loot "Bottom Section of an Engraved Signet" (10399) from "An Ikaav Castigator" (NPC 301003) in `bloodfields`. Drop cache: 4% chance per kill.
177. Loot "Center Section of an Engraved Signet" (10235) from "An Ikaav Deathbeckoner" (NPC 301008) in `bloodfields`. Drop cache: 5.13% chance per kill.
178. bloodfields/"Cryssa", hand "Top Section of an Engraved Signet" (9956) + "Center Section of an Engraved Signet" (10235) + "Bottom Section of an Engraved Signet" (10399). Gives "Enchanted Signet of the Disciples" (12080).
179. bloodfields/"Cryssa", hand "Top Section of an Engraved Signet" (9956) + "Center Section of an Engraved Signet" (10235) + "Bottom Section of an Engraved Signet" (10399). Sets `cleric20_darkdisciples` to `1`.
180. Loot "Redis' Soulstone" (69983) from "Shade of Redis Linrok" in `dranikcatacombsa`.
181. global/"Global Player", combine recipe 19914. Sets `ranger_epic` to `8`.
182. Spawns "Durunal the Cursebearer" (300087) in `wallofslaughter` on enter.
183. Loot "Dark and Twisted Sword" (69971) from "Durunal the Cursebearer".
184. hohonora/"Irak Altil", hand "Dark and Twisted Sword" (69971). Requires `paladin_epic` ==6. Gives "Dark and Twisted Sword" (69972).
185. Combine in "Dark and Twisted Sword" (69972): "Rithnok's Soulstone" (69941), "Drema's Soulstone" (69952), "Reiya's Soulstone" (69942), "Redis' Soulstone" (69983). Produces "Redemption" (64031). The combine does not fail.
186. hohonora/"Irak Altil", say "Tell Me About Your Master". Sets `paladin_epic` to `9`.
187. qeynos2/"Camlend Serbold", say "Gem". Requires `paladin_epic` ==9. Gives "Unfilled Set of Prayer Beads" (69968).
188. rivervale/"Kaya Cloudfoot", say "Different About It". Requires `paladin_epic` ==9. Gives "Note from Kaya" (69970).
189. rivervale/"Deputy Cheel", hand "Note from Kaya" (69970). Gives "Rivervale Prayer Bead" (69967).
190. akanon/"Lewis Reldnok", say "Blessed Gem". Triggers `akanon/lewis reldnok#timer:check_sit`.
191. Sit before the NPC while its timer checks your posture.
192. akanon/"Lewis Reldnok", on timer check_sit. Gives "Ak'anon Prayer Bead" (69966).
193. erudnint/"Josper Kenshed", say "Collect Component". Gives "Empty Bag" (17944).
194. Loot "Goblin Ice Necklace" (13897) from "Redwind" in `everfrost`.
195. Loot "Goblin Ice Necklace" (13897) from "An Ice Goblin Scout" in `everfrost`.
196. Loot "Goblin Ice Necklace" (13897) from "An Ice Goblin Whelp" in `everfrost`.
197. Loot "Goblin Ice Necklace" (13897) from "An Icy Orc" in `everfrost`.
198. Loot "Goblin Ice Necklace" (13897) from "Ice Goblin Diver" in `everfrost`.
199. Combine in "Empty Bag" (17944): "Goblin Ice Necklace" (13897). Produces "Bag of Ice Necklaces" (13898). The combine does not fail.
200. halas/"Lysbith Mcnaff", hand "Bag of Ice Necklaces" (13898). Gives "Iron Ration" (13005).
201. Loot "Cask" (16580) from "Tugog Grigol" in `rathemtn`.
202. Common item: Hops (16591). Listed in 31 zones.
203. Common item: Malt (16595). Listed in 30 zones.
204. Common item: Yeast (16596). Listed in 30 zones.
205. Combine in "Portable Drink Barrel" (17179): "Cask" (16580), "Hops" (16591), "Malt" (16595), "Yeast" (16596). Produces "Mead" (13008). Requires Brewing, trivial 41.
206. erudnext/"Reklon Gnallen", hand "Iron Ration" (13005) + "Mead" (13008). Requires `paladin_epic` ==9. Gives "Erudin Prayer Bead" (69965).
207. Summon "Quiver of Marr" (17307) by casting "Quiver of Marr".
208. rathemtn/"Shin Master Grubbus", hand "Quiver of Marr" (17307). Requires `paladin_epic` ==9. Gives "Gukta Prayer Bead" (69964).
209. Common item: Barley (16590). Listed in 28 zones.
210. Combine in "Medicine Bag" (17901): "Hand-Formed Bottle" (45232), "Ensnaring Concoction V" (45236). Produces "Empty Vial" (10062), "Cork" (16851), "Formed Ensnaring Concoction V" (45258). Requires Alchemy, trivial 41.
211. Combine in Brew Barrel (19): "Bottle of Aged Bloodwine" (51163), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aged Bloodwine" (51164). Requires Brewing, trivial 255.
212. 11 other recipes also produce Cork (16851).
213. Combine in "Portable Drink Barrel" (17179): "Water Flask" (13006), "Celestial Essence" (9650). Produces "Purified Water" (12607). Requires Brewing, trivial 58.
214. Combine in "Tracker's Water Extractor" (17987): "Purification Tablet" (12630), "Water Reed" (12778). Produces "Purified Water" (12607) x3. Requires Pottery. The combine does not fail.
215. 3 other recipes also produce Purified Water (12607).
216. Forage "Sand Verbena" (65582) in `taka`.
217. Forage "Sand Verbena" (65582) in `takb`.
218. Forage "Sand Verbena" (65582) in `takc`.
219. Forage "Sand Verbena" (65582) in `takd`.
220. Forage "Sand Verbena" (65582) in `take`.
221. Forage "Sand Verbena" (65582) in `takf`.
222. Forage "Sand Verbena" (65582) in `takg`.
223. Forage "Sand Verbena" (65582) in `takh`.
224. Forage "Sand Verbena" (65582) in `taki`.
225. Forage "Sand Verbena" (65582) in `takj`.
226. Combine in Brew Barrel (19): "Barley" (16590), "Bottle" (16598), "Cork" (16851), "Hops" (16591), "Purified Water" (12607), "Sand Verbena" (65582), "Yeast" (16596). Produces "Bottle of Double Brewed Double Dry Stout" (51157). Requires Brewing, trivial 226.
227. kaladimb/"Datur Nightseer", hand "Bottle of Double Brewed Double Dry Stout" (51157). Requires `paladin_epic` ==9. Gives "Kaladim Prayer Bead" (69963).
228. felwithea/"General Jyleel", hand platinum:1000. Requires `paladin_epic` ==9. Gives "Felwithe Prayer Bead" (69962).
229. Ground spawn of "Freeport Prayer Bead" (69961) in `freeportwest`.
230. Ground spawn of "Freeport Prayer Bead" (69961) in `freportn`.
231. qeynos2/"Ziska Ironforge", hand platinum:500. Requires `paladin_epic` ==9. Gives "Qeynos Prayer Bead" (69960).
232. Combine in "Unfilled Set of Prayer Beads" (69968): "Rivervale Prayer Bead" (69967), "Ak'anon Prayer Bead" (69966), "Erudin Prayer Bead" (69965), "Gukta Prayer Bead" (69964), "Kaladim Prayer Bead" (69963), "Felwithe Prayer Bead" (69962), "Freeport Prayer Bead" (69961), "Qeynos Prayer Bead" (69960). Produces "Set of Prayer Beads" (69969). The combine does not fail.
233. dranikhollowsc/"Anetal", hand "Set of Prayer Beads" (69969). Sets `paladin_epic_hollowc` to `2`.
234. natimbi/"Kemik Arulon", hand "Set of Prayer Beads" (69969). Sets `paladin_epic_hollowc` to `1`.
235. natimbi/"Kemik Arulon", say "Hail". Requires `paladin_epic_hollowc` ==2. Requires `paladin_epic` ==9. Requires `paladin_epic_hollowc` ==1. Gives "Token of Compassion" (69953).
236. oasis/"Paladin Epic", say "Hail". Requires `pal_chest_keel` unset. Gives "Keelee's Brooch" (69982).
237. sro/"Instructor Maerceci", hand "Keelee's Brooch" (69982). Gives "Token of Chivalry" (69954).
238. Loot "Valdoon Kel'Novar's Heart" (69981) from "Valdoon Kel'Novar" in `mmcc`.
239. felwithea/"Galrun Starforge", hand "Valdoon Kel'Novar's Heart" (69981). Gives "Token of Cleansing" (69956).
240. provinggrounds/"Pashia Clouddancer", say "Note". Gives "Note from Pashia" (69973).
241. nedaria/"Duram Firechaser", hand "Note from Pashia" (69973). Gives "Token of Heroism" (69955).
242. Say "Check Lorb" to anguish/"Zone Status".
243. Spawns "Orb of Discordant Energy" (317087).
244. Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy".
245. 4 alternative loot source(s) also yield Globe of Discordant Energy (47100).
246. airplane/"Inte Akera", hand "Globe of Discordant Energy" (47100). Gives "Scabbard of the Righteous" (69959).

### "Token of Loyalty" (69958)

1. Spawns "A Corrupted Koalindl" (69141) in `oot` on event_fish_success.
2. Loot "Corrupted Koalindl's Heart" (69929) from "A Corrupted Koalindl".
3. Spawns "A Corrupted Koalindl" (224432) in `gunthak` on event_fish_success.
4. Loot "Corrupted Koalindl's Heart" (69930) from "A Corrupted Koalindl".
5. Spawns "A Corrupted Koalindl" (93306) in `overthere` on event_fish_success.
6. Loot "Corrupted Koalindl's Heart" (69931) from "A Corrupted Koalindl".
7. Spawns "A Corrupted Koalindl" (182150) in `nedaria` on event_fish_success.
8. Loot "Corrupted Koalindl's Heart" (69932) from "A Corrupted Koalindl".
9. qeynos2/"Enic Ruklin", hand "Corrupted Koalindl's Heart" (69929) + "Corrupted Koalindl's Heart" (69930) + "Corrupted Koalindl's Heart" (69931) + "Corrupted Koalindl's Heart" (69932). Sets `paladin_epic` to `4`.
10. qeynos2/"Enic Ruklin", hand "Corrupted Koalindl's Heart" (69929) + "Corrupted Koalindl's Heart" (69930) + "Corrupted Koalindl's Heart" (69931) + "Corrupted Koalindl's Heart" (69932). Gives "Seal of Enic" (69933).
11. Say "Hail" to skyfire/"Dry Sapara".
12. Spawns "Rithnok the Tormented" (91193).
13. Loot "Rithnok's Soulstone" (69935) from "Rithnok the Tormented".
14. skyfire/"Dry Sapara", hand "Rithnok's Soulstone" (69935). Gives "Rithnok's Soulstone" (69936).
15. Ground spawn of "Soulstone Shard" (69937) in `draniksscar`.
16. Ground spawn of "Soulstone Shard" (69938) in `bloodfields`.
17. Ground spawn of "Soulstone Shard" (69939) in `causeway`.
18. Ground spawn of "Soulstone Shard" (69940) in `dranik`.
19. Combine in "Rithnok's Soulstone" (69936): "Soulstone Shard" (69937), "Soulstone Shard" (69938), "Soulstone Shard" (69939), "Soulstone Shard" (69940). Produces "Rithnok's Soulstone" (69941). The combine does not fail.
20. dawnshroud/"Mikhal Young", hand "Drema's Fingerbone" (69946). Sets `paladin_epic` to `5`.
21. dawnshroud/"Mikhal Young", say "Find Anything". Requires `paladin_epic` ==4. Gives "Drema's Locket" (69945).
22. letalis/"Drema Young", hand "Drema's Locket" (69945). Requires `paladin_epic` set. Requires `paladin_epic` >=4. Gives "Drema's Fingerbone" (69946).
23. dawnshroud/"Denns Rootenpaw", hand "Drema's Fingerbone" (69946). Requires `paladin_epic` ==5. Gives "Bone Collector's Bag" (69947).
24. Loot "Dark Skeleton Remains" (69927) from "A Sun Revenant" in `thegrey`.
25. Loot "Dark Skeleton Remains" (69926) from "Disturbed Elysian Remains" (NPC 176016) in `umbral`. Drop cache: 2.58% chance per kill.
26. Loot "Dark Skeleton Remains" (69925) from "A Soriz Slave" (NPC 162029) in `ssratemple`. Drop cache: 35% chance per kill.
27. Combine in "Bone Collector's Bag" (69947): "Dark Skeleton Remains" (69927), "Dark Skeleton Remains" (69926), "Dark Skeleton Remains" (69925). Produces "Bone Collector's Bag" (69948). The combine does not fail.
28. dawnshroud/"Denns Rootenpaw", hand "Bone Collector's Bag" (69948). Requires `paladin_epic` ==5. Gives "Enchanted Bone Powder" (69949).
29. Hand "Enchanted Bone Powder" (69949) to letalis/"Drema Young". Spawns "Drema Young" (169128). Loot "Drema's Soulstone" (69928) from "Drema Young".
30. Loot "Soulstone Shard" (69950) from "Coterie Corruptor" in `tenebrous`.
31. Spawns "Shade of Mujaki the Devourer" (204081) in `ponightmare` on event death_complete:204080.
32. Loot "Soulstone Shard" (69951) from "Shade of Mujaki the Devourer".
33. Combine in "Drema's Soulstone" (69928): "Soulstone Shard" (69950), "Soulstone Shard" (69951). Produces "Drema's Soulstone" (69952). The combine does not fail.
34. abysmal/"Lovine Lemise", say "Ingredients". Requires `paladin_epic` ==5. Gives "Lovine's Potion Bag" (69922).
35. Loot "Ra'Tuk Screambringer's Jaw" (69921) from "A Ra'Tuk Screambringer" (NPC 283104) in `barindu`. Drop cache: 4.06% chance per kill.
36. Loot "Noc Fleshfeasters Tail" (69920) from "A Noc Fleshfeaster" in `riwwi`.
37. Loot "Mastruq Havocblade Blood" (69919) from "A Mastruq Havocblade" in `qinimi`.
38. Loot "Mastruq Havocblade Blood" (69919) from "A Mastruq Warfiend" in `qinimi`.
39. Loot "Potameid Seaweed Strands" (69918) from "An Entrapped Potameid" in `natimbi`.
40. Combine in "Lovine's Potion Bag" (69922): "Ra'Tuk Screambringer's Jaw" (69921), "Noc Fleshfeasters Tail" (69920), "Mastruq Havocblade Blood" (69919), "Potameid Seaweed Strands" (69918). Produces "Lovine's Potion Bag" (69923). The combine does not fail.
41. abysmal/"Lovine Lemise", hand "Lovine's Potion Bag" (69923). Sets `paladin_epic_reiya` to `1`.
42. Summon "Foldable Medicine Bag" (17770) by casting "Unfold Medicine Bag".
43. Common item: Fine Potion Vial (95846). Listed in 15 zones.
44. Loot "Robust Shadow Essence" (96911) from "Qua Senshali Xakra" (NPC 158020) in `vexthal`. Drop cache: 28.72% chance per kill.
45. Loot "Sage Leaf" (14215) from "a Di'zok Herbalist" in `chardok`.
46. Loot "Sage Leaf" (14215) from "a Sarnak Herb Collector" in `chardok`.
47. Loot "Sage Leaf" (14215) from "an Apprentice Herbalist" in `chardok`.
48. Loot "Valerian Root" (14230) from "a Di'zok Herbalist" in `chardok`.
49. Loot "Valerian Root" (14230) from "a Sarnak Herb Collector" in `chardok`.
50. Loot "Valerian Root" (14230) from "an Apprentice Herbalist" in `chardok`.
51. Common item: Woundwart (16526). Listed in 9 zones.
52. Combine in "Foldable Medicine Bag" (17770): "Fine Potion Vial" (95846), "Robust Shadow Essence" (96911), "Sage Leaf" (14215), "Valerian Root" (14230), "Woundwart" (16526). Produces "Mist of the Breathless" (96937). Requires Alchemy, trivial 224.
53. abysmal/"Reiya The Pained", hand "Mist of the Breathless" (96937). Requires `paladin_epic_reiya` ==1. Gives "Reiya's Soulstone" (69924).
54. Unresolved cyclic prerequisite: `mage_epic` >=9.
55. draniksscar/"Iilivina", say "Primals". Sets `mage_epic` to `10`.
56. Spawns "Shade of Reiya the Pained" (284104) in `ferubi` on enter.
57. Loot "Soulstone Shard" (69943) from "Shade of Reiya the Pained".
58. Loot "Soulstone Shard" (69944) from "Vuranish Xxuro" in `vxed`.
59. Combine in "Reiya's Soulstone" (69924): "Soulstone Shard" (69943), "Soulstone Shard" (69944). Produces "Reiya's Soulstone" (69942). The combine does not fail.
60. Loot "Tainted Darksteel Sword" (29000) from "Keeper of the Tombs" in `hole`.
61. freeporteast/"Peasant Woman", say "I Will Take It". Gives "Bucket of Water" (29008).
62. freeporteast/"Joshua", hand "Bucket of Water" (29008). Gives "Bucket of Pure Water" (29009).
63. erudnext/"Reklon Gnallen", hand "Tainted Darksteel Sword" (29000) + "Bucket of Pure Water" (29009). Gives "Gleaming Crested Sword" (29003).
64. Loot "Tainted Darksteel Breastplate" (29001) from "Thought Destroyer" in `hateplaneb`.
65. kaladimb/"Nella Stonebraids", say "Dinner". Gives "Cold Plate of Beef and Bread" (29007).
66. kaladimb/"Jark", hand "Cold Plate of Beef and Bread" (29007). Gives "Pure Crystal" (29006).
67. erudnext/"Reklon Gnallen", hand "Tainted Darksteel Breastplate" (29001) + "Pure Crystal" (29006). Gives "Gleaming Crested Breastplate" (29004).
68. Loot "Tainted Darksteel Shield" (29002) from "Kirak Vil" in `nektulos`.
69. felwithea/"Elia The Pure", hand "Tainted Darksteel Shield" (29002). Gives "Gleaming Crested Shield" (29005).
70. erudnext/"Reklon Gnallen", hand "Gleaming Crested Sword" (29003) + "Gleaming Crested Breastplate" (29004) + "Gleaming Crested Shield" (29005). Gives "Mark of Atonement" (29010).
71. No quest step gives Drom's Champagne (13829). The dump lists it in freeporteast, freporte, highpasshold.
72. freeporteast/"Tykar Renlin", hand "Drom's Champagne" (13829) + "Drom's Champagne" (13829) + "Drom's Champagne" (13829) + "Drom's Champagne" (13829). Gives "Bunker Cell #1" (12196).
73. Summon "Black Diamond of Nightmares" (29990) by casting "Imbue Nightmare".
74. potranquility/"Elder Fuirstel", say "Hail". Sets `pop_cod_final` to `1`.
75. poknowledge/"Aid Grimel", say "Versed In The Art Of Smithing". Requires `pop_cod_final` ==1. Requires `pop_cod_final` set. Gives "Filthy Breastplate" (15984).
76. Combine in "Mixing Bowl" (17906): "Celestial Solvent" (9731), "Words of Acquisition (Beza)" (11866). Produces "Celestial Essence" (9650). Requires Baking, trivial 15. The combine does not fail.
77. Combine in "Mixing Bowl" (17906): "Celestial Solvent" (9731), "Words of Burnishing" (11862). Produces "Celestial Essence" (9650). Requires Baking, trivial 15. The combine does not fail.
78. 67 other recipes also produce Celestial Essence (9650).
79. Common item: Jar of Acid (22133). Listed in 15 zones.
80. Combine in Brew Barrel (19): "Celestial Essence" (9650), "Jar of Acid" (22133). Produces "Acid Wash" (15987). Requires Brewing, trivial 151.
81. Combine in Forge (17): "Filthy Breastplate" (15984), "Acid Wash" (15987). Produces "Cleansed Breastplate" (15998). Requires Blacksmithing, trivial 227.
82. Common item: Mortar and Pestle (17904). Listed in 12 zones.
83. Loot "Sandstorm Pearl" (29909) from "Rorek Steelthorn" (NPC 209081) in `bothunder`. Drop cache: 5.33% chance per kill.
84. Combine in "Mortar and Pestle" (17904): "Sandstorm Pearl" (29909). Produces "Powdered Sandstorm Pearl" (29520) x4. Requires Make Poison, trivial 255.
85. Common item: Firing Sheet (16906). Listed in 34 zones.
86. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
87. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `steamfont`.
88. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `tox`.
89. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `toxxulia`.
90. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
91. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). The combine does not fail.
92. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
93. Say "Tm Devrak Death" to rujd/"Rujd".
94. Spawns "spawn chest with Heavy Orcish Prison Key" (245241).
95. Loot "Pod of Water" (13044) from "spawn chest with Heavy Orcish Prison Key".
96. 6 alternative loot source(s) also yield Pod of Water (13044).
97. Forage "Pod of Water" (13044) in `ruja`.
98. Forage "Pod of Water" (13044) in `uqua`.
99. Forage "Pod of Water" (13044) in `yxtta`.
100. Combine in Brew Barrel (19): "Bottle of Aged Bloodwine" (51163), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aged Bloodwine" (51164). Requires Brewing, trivial 255.
101. Combine in Brew Barrel (19): "Bottle of Aldo's Bitter Ale" (75805), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aldo's Bitter Ale" (75811). Requires Brewing, trivial 15.
102. 17 other recipes also produce Bottle (16598).
103. Combine in Brew Barrel (19): "Pod of Water" (13044), "Bottle" (16598). Produces "Water Flask" (13006). Requires Brewing, trivial 21.
104. Combine in Pottery Wheel (21): "Water Flask" (13006), "Block of Clay" (16901). Produces "Small Block of Clay" (16900) x3. Requires Pottery, trivial 21.
105. Combine in Pottery Wheel (21): "Small Block of Clay" (16900), "Water Flask" (13006). Produces "Block of Clay" (16901). Requires Pottery, trivial 21.
106. Combine in Pottery Wheel (21): "Water Flask" (13006), "Large Block of Clay" (16902). Produces "Block of Clay" (16901) x2. Requires Pottery, trivial 21.
107. Combine in Pottery Wheel (21): "Block of Clay" (16901), "Water Flask" (13006). Produces "Large Block of Clay" (16902). Requires Pottery, trivial 21.
108. Common item: Large Bowl Sketch (16963). Listed in 29 zones.
109. Combine in Pottery Wheel (21): "Large Block of Clay" (16902), "Water Flask" (13006), "Large Bowl Sketch" (16963). Produces "Unfired Mixing Bowl" (16930). Requires Pottery, trivial 128.
110. Combine in Kiln (22): "Firing Sheet" (16906), "Unfired Mixing Bowl" (16930). Produces "Mixing Bowl" (17906). Requires Pottery, trivial 15.
111. Combine in "Mixing Bowl" (17906): "Sandstorm Pearl" (29909). Produces "Powdered Sandstorm Pearl" (29520) x4. Requires Baking. The combine does not fail.
112. Spawns "a Koka'Vor chieftain" (210236) in `postorms` on event_signal.
113. Loot "Storm Rider Blood" (29526) from "a Koka'Vor chieftain".
114. Loot "Drop of Pure Rain" (29904) from "A vann stav" (NPC 209018) in `bothunder`. Drop cache: 4% chance per kill.
115. Combine in Brew Barrel (19): "Powdered Sandstorm Pearl" (29520), "Storm Rider Blood" (29526), "Drop of Pure Rain" (29904). Produces "Hurricane Temper" (29533). Requires Brewing, trivial 135.
116. Combine in Forge (17): "Cleansed Breastplate" (15998), "Hurricane Temper" (29533). Produces "Tempered Breastplate" (15999). Requires Blacksmithing, trivial 229.
117. Combine in Forge (17): "Black Diamond of Nightmares" (29990), "Tempered Breastplate" (15999). Produces "Imbued Breastplate" (15985). Requires Blacksmithing 220. Trivial at 275.
118. poknowledge/"Aid Grimel", hand "Imbued Breastplate" (15985). Gives "Hardened Leather Signet" (16249).
119. poknowledge/"Aid Grimel", say "Skill In Brewing". Requires `pop_cod_final` ==1. Requires `pop_cod_final` set. Gives "Portable Drink Barrel" (17179).
120. Loot "Snake Scales" (13070) from "A Kerra Snake" (NPC 98017) in `erudsxing`. Drop cache: 59.23% chance per kill.
121. Combine in "Portable Drink Barrel" (17179): "Water Flask" (13006), "Snake Scales" (13070), "Bottle" (16598). Produces "Bog Juice" (16581). Requires Brewing, trivial 21.
122. Common item: Spit (17947). Listed in 34 zones.
123. Loot "Fire Beetle Eye" (10307) from "A Klicnik Drone" (NPC 2021) in `qeynos2`. Drop cache: 100% chance per kill.
124. Spawns "Sepsis Rat" (45113) in `qcat` on event_death.
125. Loot "Rat Ears" (13072) from "Sepsis Rat".
126. 2 alternative loot source(s) also yield Rat Ears (13072).
127. Combine in "Spit" (17947): "Fire Beetle Eye" (10307), "Rat Ears" (13072). Produces "Edible Goo" (13498). Requires Baking, trivial 21.
128. freeporteast/"A Prisoner", hand "Bunker Cell #1" (12196) + "Edible Goo" (13498) + "Bog Juice" (16581). Gives "H. K. 102" (12143).
129. highkeep/"Assistant Kiolna", hand "H. K. 102" (12143). Gives "Sealed Note" (18936).
130. paw/"Brother Hayle", hand "Sealed Note" (18936). Gives "Note" (18937).
131. Kill freportw/"Sir Lucan D-Lere". Spawns "Sir Lucan D'Lere" (9147).
132. Loot "Testimony of Truth" (18827) from "Sir Lucan D'Lere".
133. freeportwest/"Valeron Dushire", hand "Testimony of Truth" (18827). Gives "Brilliant Sword of Faith" (13947).
134. Loot "Spider Venom Sac" (14018) from "Stone Spider" (NPC 32057) in `soldungb`. Drop cache: 51% chance per kill.
135. freeportwest/"Merko Quetalis", hand "Spider Venom Sac" (14018). Gives "Token of Bravery" (12144).
136. **Broken:** nothing in the graph gives, loots, spawns, or combines Blackbox XIVD (13344).
137. akanon/"Baxok Curhunter", hand "Blackbox XIVD" (13344). Gives "Cloth Shirt" (1004).
138. commonlands/"Altunic Jartin", hand "Cloth Shirt" (1004). Gives "Token of Generosity" (13865).
139. Hand "Token of Bravery" (12144) + "Token of Generosity" (13865) to freeportwest/"Merko Quetalis". Spawns "spawns Guard Willia" (383270). Loot "Token of Truth" (13866) from "spawns Guard Willia".
140. 1 alternative loot source(s) also yield Token of Truth (13866).
141. freeportwest/"Merko Quetalis", hand "Token of Truth" (13866). Gives "Testimony" (18828).
142. Loot "Glowing Sword Hilt" (12197) from "Xicotl" in `mistmoore`.
143. paw/"Brother Hayle", hand "Glowing Sword Hilt" (12197) + "Brilliant Sword of Faith" (13947) + "Testimony" (18828) + "Note" (18937). Gives "SoulFire" (5504).
144. airplane/"Inte Akera", hand "SoulFire" (5504). Gives "Inte's First Blessing" (18033).
145. neriakc/"Selzar L-Crit", say "Armor". Gives "Note to Kanthuk" (2416).
146. butcher/"Kanthuk Ogrebane", hand "Note to Kanthuk" (2416). Sets `Kanthuk` to `ghoul`.
147. butcher/"Kanthuk Ogrebane", say "Strange Image". Requires `Kanthuk` set. Gives "Pendant" (2414).
148. cauldron/"Llara", hand "Pendant" (2414). Sets `Llara` to `ghoul`.
149. cauldron/"Llara", say "Ruathey". Requires `Llara` set. Gives "Note to Ruathey" (2417).
150. lavastorm/"Ruathey", hand "Note to Ruathey" (2417). Sets `Ruathey` to `ghoul`.
151. lavastorm/"Ruathey", hand "Note to Ruathey" (2417). Sets `ruathey_note` to `1`.
152. lavastorm/"Ruathey", say "Bag". Requires `Ruathey` set. Requires `ruathey_note` ==1. Requires `ruathey_note` set. Gives "Nobleman's Bag" (17878).
153. Loot "Ghoul's Heart" (2410) from "A Ghoul" (NPC 63011) in `unrest`. Drop cache: 25% chance per kill.
154. Loot "Amstaf's Scroll" (2411) from "A Goblin Thief" (NPC 6150) in `highkeep`. Drop cache: 35% chance per kill.
155. Loot "Blade of Nobility" (2412) from "A Crazed Goblin" (NPC 68162) in `butcher`. Drop cache: 10.57% chance per kill.
156. Loot "Hilt of the Nobleman" (2413) from "Ekeros" in `najena`.
157. Loot "Hilt of the Nobleman" (2413) from "A Skeleton" in `najena`.
158. Combine in "Nobleman's Bag" (17878): "Ghoul's Heart" (2410), "Amstaf's Scroll" (2411), "Blade of Nobility" (2412), "Hilt of the Nobleman" (2413). Produces "Ghoulbane" (5403). The combine does not fail.
159. airplane/"Inte Akera", hand "Ghoulbane" (5403). Gives "Inte's Second Blessing" (18034).
160. Loot "Torn, Burnt Book" (19071) from "Lord Nagafen" in `soldungb`.
161. Loot "Torn, Burnt Book" (19071) from "Melalafen" in `westwastes`.
162. Loot "Torn, Burnt Book" (19071) from "Severilous" in `emeraldjungle`.
163. Loot "Torn, Burnt Book" (19071) from "Talendor" in `skyfire`.
164. Loot "Torn, Burnt Book" (19071) from "The Fabled Severilous".
165. Loot "Torn, Frost-covered Book" (19070) from "Faydedar" in `timorous`.
166. Loot "Torn, Frost-covered Book" (19070) from "Gorenaire" in `dreadlands`.
167. Loot "Torn, Frost-covered Book" (19070) from "Lady Vox" in `permafrost`.
168. neriakb/"Rysva To-Biath", hand "Torn, Frost-covered Book" (19070) + "Torn, Burnt Book" (19071). Gives "Book of Scale" (18302).
169. oceanoftears/"Oracle Of K-Arnon", hand "Book of Scale" (18302). Gives "Miragul's Phylactery" (19072).
170. Hand "Miragul's Phylactery" (19072) to everfrost/"Lich Of Miragul". Spawns "Spawn Miragul" (30094). Loot "Miragul's Head" (19073) from "Spawn Miragul".
171. Hand "Miragul's Phylactery" (19072) to everfrost/"Lich Of Miragul". Spawns "Spawn Miragul" (30094). Loot "Miragul's Robe" (1254) from "Spawn Miragul".
172. airplane/"Inte Akera", hand "Miragul's Robe" (1254) + "Inte's First Blessing" (18033) + "Inte's Second Blessing" (18034) + "Miragul's Head" (19073). Gives "Fiery Avenger" (11050).
173. fearplane/"Irak Altil", hand "Fiery Avenger" (11050) + "Mark of Atonement" (29010). Gives "Fiery Defender" (10099).
174. hohonora/"Irak Altil", say "Hail". Sets `paladin_epic` to `6`.
175. Loot "Top Section of an Engraved Signet" (9956) from "An Ikaav Miragenist" (NPC 301015) in `bloodfields`. Drop cache: 6.08% chance per kill.
176. Loot "Bottom Section of an Engraved Signet" (10399) from "An Ikaav Castigator" (NPC 301003) in `bloodfields`. Drop cache: 4% chance per kill.
177. Loot "Center Section of an Engraved Signet" (10235) from "An Ikaav Deathbeckoner" (NPC 301008) in `bloodfields`. Drop cache: 5.13% chance per kill.
178. bloodfields/"Cryssa", hand "Top Section of an Engraved Signet" (9956) + "Center Section of an Engraved Signet" (10235) + "Bottom Section of an Engraved Signet" (10399). Gives "Enchanted Signet of the Disciples" (12080).
179. bloodfields/"Cryssa", hand "Top Section of an Engraved Signet" (9956) + "Center Section of an Engraved Signet" (10235) + "Bottom Section of an Engraved Signet" (10399). Sets `cleric20_darkdisciples` to `1`.
180. Loot "Redis' Soulstone" (69983) from "Shade of Redis Linrok" in `dranikcatacombsa`.
181. global/"Global Player", combine recipe 19914. Sets `ranger_epic` to `8`.
182. Spawns "Durunal the Cursebearer" (300087) in `wallofslaughter` on enter.
183. Loot "Dark and Twisted Sword" (69971) from "Durunal the Cursebearer".
184. hohonora/"Irak Altil", hand "Dark and Twisted Sword" (69971). Requires `paladin_epic` ==6. Gives "Dark and Twisted Sword" (69972).
185. Combine in "Dark and Twisted Sword" (69972): "Rithnok's Soulstone" (69941), "Drema's Soulstone" (69952), "Reiya's Soulstone" (69942), "Redis' Soulstone" (69983). Produces "Redemption" (64031). The combine does not fail.
186. hohonora/"Irak Altil", say "Tell Me About Your Master". Sets `paladin_epic` to `9`.
187. qeynos2/"Camlend Serbold", say "Gem". Requires `paladin_epic` ==9. Gives "Unfilled Set of Prayer Beads" (69968).
188. rivervale/"Kaya Cloudfoot", say "Different About It". Requires `paladin_epic` ==9. Gives "Note from Kaya" (69970).
189. rivervale/"Deputy Cheel", hand "Note from Kaya" (69970). Gives "Rivervale Prayer Bead" (69967).
190. akanon/"Lewis Reldnok", say "Blessed Gem". Triggers `akanon/lewis reldnok#timer:check_sit`.
191. Sit before the NPC while its timer checks your posture.
192. akanon/"Lewis Reldnok", on timer check_sit. Gives "Ak'anon Prayer Bead" (69966).
193. erudnint/"Josper Kenshed", say "Collect Component". Gives "Empty Bag" (17944).
194. Loot "Goblin Ice Necklace" (13897) from "Redwind" in `everfrost`.
195. Loot "Goblin Ice Necklace" (13897) from "An Ice Goblin Scout" in `everfrost`.
196. Loot "Goblin Ice Necklace" (13897) from "An Ice Goblin Whelp" in `everfrost`.
197. Loot "Goblin Ice Necklace" (13897) from "An Icy Orc" in `everfrost`.
198. Loot "Goblin Ice Necklace" (13897) from "Ice Goblin Diver" in `everfrost`.
199. Combine in "Empty Bag" (17944): "Goblin Ice Necklace" (13897). Produces "Bag of Ice Necklaces" (13898). The combine does not fail.
200. halas/"Lysbith Mcnaff", hand "Bag of Ice Necklaces" (13898). Gives "Iron Ration" (13005).
201. Loot "Cask" (16580) from "Tugog Grigol" in `rathemtn`.
202. Common item: Hops (16591). Listed in 31 zones.
203. Common item: Malt (16595). Listed in 30 zones.
204. Common item: Yeast (16596). Listed in 30 zones.
205. Combine in "Portable Drink Barrel" (17179): "Cask" (16580), "Hops" (16591), "Malt" (16595), "Yeast" (16596). Produces "Mead" (13008). Requires Brewing, trivial 41.
206. erudnext/"Reklon Gnallen", hand "Iron Ration" (13005) + "Mead" (13008). Requires `paladin_epic` ==9. Gives "Erudin Prayer Bead" (69965).
207. Summon "Quiver of Marr" (17307) by casting "Quiver of Marr".
208. rathemtn/"Shin Master Grubbus", hand "Quiver of Marr" (17307). Requires `paladin_epic` ==9. Gives "Gukta Prayer Bead" (69964).
209. Common item: Barley (16590). Listed in 28 zones.
210. Combine in "Medicine Bag" (17901): "Hand-Formed Bottle" (45232), "Ensnaring Concoction V" (45236). Produces "Empty Vial" (10062), "Cork" (16851), "Formed Ensnaring Concoction V" (45258). Requires Alchemy, trivial 41.
211. Combine in Brew Barrel (19): "Bottle of Aged Bloodwine" (51163), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aged Bloodwine" (51164). Requires Brewing, trivial 255.
212. 11 other recipes also produce Cork (16851).
213. Combine in "Portable Drink Barrel" (17179): "Water Flask" (13006), "Celestial Essence" (9650). Produces "Purified Water" (12607). Requires Brewing, trivial 58.
214. Combine in "Tracker's Water Extractor" (17987): "Purification Tablet" (12630), "Water Reed" (12778). Produces "Purified Water" (12607) x3. Requires Pottery. The combine does not fail.
215. 3 other recipes also produce Purified Water (12607).
216. Forage "Sand Verbena" (65582) in `taka`.
217. Forage "Sand Verbena" (65582) in `takb`.
218. Forage "Sand Verbena" (65582) in `takc`.
219. Forage "Sand Verbena" (65582) in `takd`.
220. Forage "Sand Verbena" (65582) in `take`.
221. Forage "Sand Verbena" (65582) in `takf`.
222. Forage "Sand Verbena" (65582) in `takg`.
223. Forage "Sand Verbena" (65582) in `takh`.
224. Forage "Sand Verbena" (65582) in `taki`.
225. Forage "Sand Verbena" (65582) in `takj`.
226. Combine in Brew Barrel (19): "Barley" (16590), "Bottle" (16598), "Cork" (16851), "Hops" (16591), "Purified Water" (12607), "Sand Verbena" (65582), "Yeast" (16596). Produces "Bottle of Double Brewed Double Dry Stout" (51157). Requires Brewing, trivial 226.
227. kaladimb/"Datur Nightseer", hand "Bottle of Double Brewed Double Dry Stout" (51157). Requires `paladin_epic` ==9. Gives "Kaladim Prayer Bead" (69963).
228. felwithea/"General Jyleel", hand platinum:1000. Requires `paladin_epic` ==9. Gives "Felwithe Prayer Bead" (69962).
229. Ground spawn of "Freeport Prayer Bead" (69961) in `freeportwest`.
230. Ground spawn of "Freeport Prayer Bead" (69961) in `freportn`.
231. qeynos2/"Ziska Ironforge", hand platinum:500. Requires `paladin_epic` ==9. Gives "Qeynos Prayer Bead" (69960).
232. Combine in "Unfilled Set of Prayer Beads" (69968): "Rivervale Prayer Bead" (69967), "Ak'anon Prayer Bead" (69966), "Erudin Prayer Bead" (69965), "Gukta Prayer Bead" (69964), "Kaladim Prayer Bead" (69963), "Felwithe Prayer Bead" (69962), "Freeport Prayer Bead" (69961), "Qeynos Prayer Bead" (69960). Produces "Set of Prayer Beads" (69969). The combine does not fail.
233. dranikhollowsc/"Anetal", hand "Set of Prayer Beads" (69969). Sets `paladin_epic_hollowc` to `2`.
234. natimbi/"Kemik Arulon", hand "Set of Prayer Beads" (69969). Sets `paladin_epic_hollowc` to `1`.
235. natimbi/"Kemik Arulon", say "Hail". Requires `paladin_epic_hollowc` ==2. Requires `paladin_epic` ==9. Requires `paladin_epic_hollowc` ==1. Gives "Token of Compassion" (69953).
236. oasis/"Paladin Epic", say "Hail". Requires `pal_chest_keel` unset. Gives "Keelee's Brooch" (69982).
237. sro/"Instructor Maerceci", hand "Keelee's Brooch" (69982). Gives "Token of Chivalry" (69954).
238. Loot "Valdoon Kel'Novar's Heart" (69981) from "Valdoon Kel'Novar" in `mmcc`.
239. felwithea/"Galrun Starforge", hand "Valdoon Kel'Novar's Heart" (69981). Gives "Token of Cleansing" (69956).
240. provinggrounds/"Pashia Clouddancer", say "Note". Gives "Note from Pashia" (69973).
241. nedaria/"Duram Firechaser", hand "Note from Pashia" (69973). Gives "Token of Heroism" (69955).
242. Say "Check Lorb" to anguish/"Zone Status".
243. Spawns "Orb of Discordant Energy" (317087).
244. Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy".
245. 4 alternative loot source(s) also yield Globe of Discordant Energy (47100).
246. airplane/"Inte Akera", hand "Globe of Discordant Energy" (47100). Gives "Token of Loyalty" (69958).

### "Token of Conviction" (69957)

1. Spawns "A Corrupted Koalindl" (69141) in `oot` on event_fish_success.
2. Loot "Corrupted Koalindl's Heart" (69929) from "A Corrupted Koalindl".
3. Spawns "A Corrupted Koalindl" (224432) in `gunthak` on event_fish_success.
4. Loot "Corrupted Koalindl's Heart" (69930) from "A Corrupted Koalindl".
5. Spawns "A Corrupted Koalindl" (93306) in `overthere` on event_fish_success.
6. Loot "Corrupted Koalindl's Heart" (69931) from "A Corrupted Koalindl".
7. Spawns "A Corrupted Koalindl" (182150) in `nedaria` on event_fish_success.
8. Loot "Corrupted Koalindl's Heart" (69932) from "A Corrupted Koalindl".
9. qeynos2/"Enic Ruklin", hand "Corrupted Koalindl's Heart" (69929) + "Corrupted Koalindl's Heart" (69930) + "Corrupted Koalindl's Heart" (69931) + "Corrupted Koalindl's Heart" (69932). Sets `paladin_epic` to `4`.
10. qeynos2/"Enic Ruklin", hand "Corrupted Koalindl's Heart" (69929) + "Corrupted Koalindl's Heart" (69930) + "Corrupted Koalindl's Heart" (69931) + "Corrupted Koalindl's Heart" (69932). Gives "Seal of Enic" (69933).
11. Say "Hail" to skyfire/"Dry Sapara".
12. Spawns "Rithnok the Tormented" (91193).
13. Loot "Rithnok's Soulstone" (69935) from "Rithnok the Tormented".
14. skyfire/"Dry Sapara", hand "Rithnok's Soulstone" (69935). Gives "Rithnok's Soulstone" (69936).
15. Ground spawn of "Soulstone Shard" (69937) in `draniksscar`.
16. Ground spawn of "Soulstone Shard" (69938) in `bloodfields`.
17. Ground spawn of "Soulstone Shard" (69939) in `causeway`.
18. Ground spawn of "Soulstone Shard" (69940) in `dranik`.
19. Combine in "Rithnok's Soulstone" (69936): "Soulstone Shard" (69937), "Soulstone Shard" (69938), "Soulstone Shard" (69939), "Soulstone Shard" (69940). Produces "Rithnok's Soulstone" (69941). The combine does not fail.
20. dawnshroud/"Mikhal Young", hand "Drema's Fingerbone" (69946). Sets `paladin_epic` to `5`.
21. dawnshroud/"Mikhal Young", say "Find Anything". Requires `paladin_epic` ==4. Gives "Drema's Locket" (69945).
22. letalis/"Drema Young", hand "Drema's Locket" (69945). Requires `paladin_epic` set. Requires `paladin_epic` >=4. Gives "Drema's Fingerbone" (69946).
23. dawnshroud/"Denns Rootenpaw", hand "Drema's Fingerbone" (69946). Requires `paladin_epic` ==5. Gives "Bone Collector's Bag" (69947).
24. Loot "Dark Skeleton Remains" (69927) from "A Sun Revenant" in `thegrey`.
25. Loot "Dark Skeleton Remains" (69926) from "Disturbed Elysian Remains" (NPC 176016) in `umbral`. Drop cache: 2.58% chance per kill.
26. Loot "Dark Skeleton Remains" (69925) from "A Soriz Slave" (NPC 162029) in `ssratemple`. Drop cache: 35% chance per kill.
27. Combine in "Bone Collector's Bag" (69947): "Dark Skeleton Remains" (69927), "Dark Skeleton Remains" (69926), "Dark Skeleton Remains" (69925). Produces "Bone Collector's Bag" (69948). The combine does not fail.
28. dawnshroud/"Denns Rootenpaw", hand "Bone Collector's Bag" (69948). Requires `paladin_epic` ==5. Gives "Enchanted Bone Powder" (69949).
29. Hand "Enchanted Bone Powder" (69949) to letalis/"Drema Young". Spawns "Drema Young" (169128). Loot "Drema's Soulstone" (69928) from "Drema Young".
30. Loot "Soulstone Shard" (69950) from "Coterie Corruptor" in `tenebrous`.
31. Spawns "Shade of Mujaki the Devourer" (204081) in `ponightmare` on event death_complete:204080.
32. Loot "Soulstone Shard" (69951) from "Shade of Mujaki the Devourer".
33. Combine in "Drema's Soulstone" (69928): "Soulstone Shard" (69950), "Soulstone Shard" (69951). Produces "Drema's Soulstone" (69952). The combine does not fail.
34. abysmal/"Lovine Lemise", say "Ingredients". Requires `paladin_epic` ==5. Gives "Lovine's Potion Bag" (69922).
35. Loot "Ra'Tuk Screambringer's Jaw" (69921) from "A Ra'Tuk Screambringer" (NPC 283104) in `barindu`. Drop cache: 4.06% chance per kill.
36. Loot "Noc Fleshfeasters Tail" (69920) from "A Noc Fleshfeaster" in `riwwi`.
37. Loot "Mastruq Havocblade Blood" (69919) from "A Mastruq Havocblade" in `qinimi`.
38. Loot "Mastruq Havocblade Blood" (69919) from "A Mastruq Warfiend" in `qinimi`.
39. Loot "Potameid Seaweed Strands" (69918) from "An Entrapped Potameid" in `natimbi`.
40. Combine in "Lovine's Potion Bag" (69922): "Ra'Tuk Screambringer's Jaw" (69921), "Noc Fleshfeasters Tail" (69920), "Mastruq Havocblade Blood" (69919), "Potameid Seaweed Strands" (69918). Produces "Lovine's Potion Bag" (69923). The combine does not fail.
41. abysmal/"Lovine Lemise", hand "Lovine's Potion Bag" (69923). Sets `paladin_epic_reiya` to `1`.
42. Summon "Foldable Medicine Bag" (17770) by casting "Unfold Medicine Bag".
43. Common item: Fine Potion Vial (95846). Listed in 15 zones.
44. Loot "Robust Shadow Essence" (96911) from "Qua Senshali Xakra" (NPC 158020) in `vexthal`. Drop cache: 28.72% chance per kill.
45. Loot "Sage Leaf" (14215) from "a Di'zok Herbalist" in `chardok`.
46. Loot "Sage Leaf" (14215) from "a Sarnak Herb Collector" in `chardok`.
47. Loot "Sage Leaf" (14215) from "an Apprentice Herbalist" in `chardok`.
48. Loot "Valerian Root" (14230) from "a Di'zok Herbalist" in `chardok`.
49. Loot "Valerian Root" (14230) from "a Sarnak Herb Collector" in `chardok`.
50. Loot "Valerian Root" (14230) from "an Apprentice Herbalist" in `chardok`.
51. Common item: Woundwart (16526). Listed in 9 zones.
52. Combine in "Foldable Medicine Bag" (17770): "Fine Potion Vial" (95846), "Robust Shadow Essence" (96911), "Sage Leaf" (14215), "Valerian Root" (14230), "Woundwart" (16526). Produces "Mist of the Breathless" (96937). Requires Alchemy, trivial 224.
53. abysmal/"Reiya The Pained", hand "Mist of the Breathless" (96937). Requires `paladin_epic_reiya` ==1. Gives "Reiya's Soulstone" (69924).
54. Unresolved cyclic prerequisite: `mage_epic` >=9.
55. draniksscar/"Iilivina", say "Primals". Sets `mage_epic` to `10`.
56. Spawns "Shade of Reiya the Pained" (284104) in `ferubi` on enter.
57. Loot "Soulstone Shard" (69943) from "Shade of Reiya the Pained".
58. Loot "Soulstone Shard" (69944) from "Vuranish Xxuro" in `vxed`.
59. Combine in "Reiya's Soulstone" (69924): "Soulstone Shard" (69943), "Soulstone Shard" (69944). Produces "Reiya's Soulstone" (69942). The combine does not fail.
60. Loot "Tainted Darksteel Sword" (29000) from "Keeper of the Tombs" in `hole`.
61. freeporteast/"Peasant Woman", say "I Will Take It". Gives "Bucket of Water" (29008).
62. freeporteast/"Joshua", hand "Bucket of Water" (29008). Gives "Bucket of Pure Water" (29009).
63. erudnext/"Reklon Gnallen", hand "Tainted Darksteel Sword" (29000) + "Bucket of Pure Water" (29009). Gives "Gleaming Crested Sword" (29003).
64. Loot "Tainted Darksteel Breastplate" (29001) from "Thought Destroyer" in `hateplaneb`.
65. kaladimb/"Nella Stonebraids", say "Dinner". Gives "Cold Plate of Beef and Bread" (29007).
66. kaladimb/"Jark", hand "Cold Plate of Beef and Bread" (29007). Gives "Pure Crystal" (29006).
67. erudnext/"Reklon Gnallen", hand "Tainted Darksteel Breastplate" (29001) + "Pure Crystal" (29006). Gives "Gleaming Crested Breastplate" (29004).
68. Loot "Tainted Darksteel Shield" (29002) from "Kirak Vil" in `nektulos`.
69. felwithea/"Elia The Pure", hand "Tainted Darksteel Shield" (29002). Gives "Gleaming Crested Shield" (29005).
70. erudnext/"Reklon Gnallen", hand "Gleaming Crested Sword" (29003) + "Gleaming Crested Breastplate" (29004) + "Gleaming Crested Shield" (29005). Gives "Mark of Atonement" (29010).
71. No quest step gives Drom's Champagne (13829). The dump lists it in freeporteast, freporte, highpasshold.
72. freeporteast/"Tykar Renlin", hand "Drom's Champagne" (13829) + "Drom's Champagne" (13829) + "Drom's Champagne" (13829) + "Drom's Champagne" (13829). Gives "Bunker Cell #1" (12196).
73. Summon "Black Diamond of Nightmares" (29990) by casting "Imbue Nightmare".
74. potranquility/"Elder Fuirstel", say "Hail". Sets `pop_cod_final` to `1`.
75. poknowledge/"Aid Grimel", say "Versed In The Art Of Smithing". Requires `pop_cod_final` ==1. Requires `pop_cod_final` set. Gives "Filthy Breastplate" (15984).
76. Combine in "Mixing Bowl" (17906): "Celestial Solvent" (9731), "Words of Acquisition (Beza)" (11866). Produces "Celestial Essence" (9650). Requires Baking, trivial 15. The combine does not fail.
77. Combine in "Mixing Bowl" (17906): "Celestial Solvent" (9731), "Words of Burnishing" (11862). Produces "Celestial Essence" (9650). Requires Baking, trivial 15. The combine does not fail.
78. 67 other recipes also produce Celestial Essence (9650).
79. Common item: Jar of Acid (22133). Listed in 15 zones.
80. Combine in Brew Barrel (19): "Celestial Essence" (9650), "Jar of Acid" (22133). Produces "Acid Wash" (15987). Requires Brewing, trivial 151.
81. Combine in Forge (17): "Filthy Breastplate" (15984), "Acid Wash" (15987). Produces "Cleansed Breastplate" (15998). Requires Blacksmithing, trivial 227.
82. Common item: Mortar and Pestle (17904). Listed in 12 zones.
83. Loot "Sandstorm Pearl" (29909) from "Rorek Steelthorn" (NPC 209081) in `bothunder`. Drop cache: 5.33% chance per kill.
84. Combine in "Mortar and Pestle" (17904): "Sandstorm Pearl" (29909). Produces "Powdered Sandstorm Pearl" (29520) x4. Requires Make Poison, trivial 255.
85. Common item: Firing Sheet (16906). Listed in 34 zones.
86. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
87. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `steamfont`.
88. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `tox`.
89. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `toxxulia`.
90. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
91. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). The combine does not fail.
92. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
93. Say "Tm Devrak Death" to rujd/"Rujd".
94. Spawns "spawn chest with Heavy Orcish Prison Key" (245241).
95. Loot "Pod of Water" (13044) from "spawn chest with Heavy Orcish Prison Key".
96. 6 alternative loot source(s) also yield Pod of Water (13044).
97. Forage "Pod of Water" (13044) in `ruja`.
98. Forage "Pod of Water" (13044) in `uqua`.
99. Forage "Pod of Water" (13044) in `yxtta`.
100. Combine in Brew Barrel (19): "Bottle of Aged Bloodwine" (51163), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aged Bloodwine" (51164). Requires Brewing, trivial 255.
101. Combine in Brew Barrel (19): "Bottle of Aldo's Bitter Ale" (75805), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aldo's Bitter Ale" (75811). Requires Brewing, trivial 15.
102. 17 other recipes also produce Bottle (16598).
103. Combine in Brew Barrel (19): "Pod of Water" (13044), "Bottle" (16598). Produces "Water Flask" (13006). Requires Brewing, trivial 21.
104. Combine in Pottery Wheel (21): "Water Flask" (13006), "Block of Clay" (16901). Produces "Small Block of Clay" (16900) x3. Requires Pottery, trivial 21.
105. Combine in Pottery Wheel (21): "Small Block of Clay" (16900), "Water Flask" (13006). Produces "Block of Clay" (16901). Requires Pottery, trivial 21.
106. Combine in Pottery Wheel (21): "Water Flask" (13006), "Large Block of Clay" (16902). Produces "Block of Clay" (16901) x2. Requires Pottery, trivial 21.
107. Combine in Pottery Wheel (21): "Block of Clay" (16901), "Water Flask" (13006). Produces "Large Block of Clay" (16902). Requires Pottery, trivial 21.
108. Common item: Large Bowl Sketch (16963). Listed in 29 zones.
109. Combine in Pottery Wheel (21): "Large Block of Clay" (16902), "Water Flask" (13006), "Large Bowl Sketch" (16963). Produces "Unfired Mixing Bowl" (16930). Requires Pottery, trivial 128.
110. Combine in Kiln (22): "Firing Sheet" (16906), "Unfired Mixing Bowl" (16930). Produces "Mixing Bowl" (17906). Requires Pottery, trivial 15.
111. Combine in "Mixing Bowl" (17906): "Sandstorm Pearl" (29909). Produces "Powdered Sandstorm Pearl" (29520) x4. Requires Baking. The combine does not fail.
112. Spawns "a Koka'Vor chieftain" (210236) in `postorms` on event_signal.
113. Loot "Storm Rider Blood" (29526) from "a Koka'Vor chieftain".
114. Loot "Drop of Pure Rain" (29904) from "A vann stav" (NPC 209018) in `bothunder`. Drop cache: 4% chance per kill.
115. Combine in Brew Barrel (19): "Powdered Sandstorm Pearl" (29520), "Storm Rider Blood" (29526), "Drop of Pure Rain" (29904). Produces "Hurricane Temper" (29533). Requires Brewing, trivial 135.
116. Combine in Forge (17): "Cleansed Breastplate" (15998), "Hurricane Temper" (29533). Produces "Tempered Breastplate" (15999). Requires Blacksmithing, trivial 229.
117. Combine in Forge (17): "Black Diamond of Nightmares" (29990), "Tempered Breastplate" (15999). Produces "Imbued Breastplate" (15985). Requires Blacksmithing 220. Trivial at 275.
118. poknowledge/"Aid Grimel", hand "Imbued Breastplate" (15985). Gives "Hardened Leather Signet" (16249).
119. poknowledge/"Aid Grimel", say "Skill In Brewing". Requires `pop_cod_final` ==1. Requires `pop_cod_final` set. Gives "Portable Drink Barrel" (17179).
120. Loot "Snake Scales" (13070) from "A Kerra Snake" (NPC 98017) in `erudsxing`. Drop cache: 59.23% chance per kill.
121. Combine in "Portable Drink Barrel" (17179): "Water Flask" (13006), "Snake Scales" (13070), "Bottle" (16598). Produces "Bog Juice" (16581). Requires Brewing, trivial 21.
122. Common item: Spit (17947). Listed in 34 zones.
123. Loot "Fire Beetle Eye" (10307) from "A Klicnik Drone" (NPC 2021) in `qeynos2`. Drop cache: 100% chance per kill.
124. Spawns "Sepsis Rat" (45113) in `qcat` on event_death.
125. Loot "Rat Ears" (13072) from "Sepsis Rat".
126. 2 alternative loot source(s) also yield Rat Ears (13072).
127. Combine in "Spit" (17947): "Fire Beetle Eye" (10307), "Rat Ears" (13072). Produces "Edible Goo" (13498). Requires Baking, trivial 21.
128. freeporteast/"A Prisoner", hand "Bunker Cell #1" (12196) + "Edible Goo" (13498) + "Bog Juice" (16581). Gives "H. K. 102" (12143).
129. highkeep/"Assistant Kiolna", hand "H. K. 102" (12143). Gives "Sealed Note" (18936).
130. paw/"Brother Hayle", hand "Sealed Note" (18936). Gives "Note" (18937).
131. Kill freportw/"Sir Lucan D-Lere". Spawns "Sir Lucan D'Lere" (9147).
132. Loot "Testimony of Truth" (18827) from "Sir Lucan D'Lere".
133. freeportwest/"Valeron Dushire", hand "Testimony of Truth" (18827). Gives "Brilliant Sword of Faith" (13947).
134. Loot "Spider Venom Sac" (14018) from "Stone Spider" (NPC 32057) in `soldungb`. Drop cache: 51% chance per kill.
135. freeportwest/"Merko Quetalis", hand "Spider Venom Sac" (14018). Gives "Token of Bravery" (12144).
136. **Broken:** nothing in the graph gives, loots, spawns, or combines Blackbox XIVD (13344).
137. akanon/"Baxok Curhunter", hand "Blackbox XIVD" (13344). Gives "Cloth Shirt" (1004).
138. commonlands/"Altunic Jartin", hand "Cloth Shirt" (1004). Gives "Token of Generosity" (13865).
139. Hand "Token of Bravery" (12144) + "Token of Generosity" (13865) to freeportwest/"Merko Quetalis". Spawns "spawns Guard Willia" (383270). Loot "Token of Truth" (13866) from "spawns Guard Willia".
140. 1 alternative loot source(s) also yield Token of Truth (13866).
141. freeportwest/"Merko Quetalis", hand "Token of Truth" (13866). Gives "Testimony" (18828).
142. Loot "Glowing Sword Hilt" (12197) from "Xicotl" in `mistmoore`.
143. paw/"Brother Hayle", hand "Glowing Sword Hilt" (12197) + "Brilliant Sword of Faith" (13947) + "Testimony" (18828) + "Note" (18937). Gives "SoulFire" (5504).
144. airplane/"Inte Akera", hand "SoulFire" (5504). Gives "Inte's First Blessing" (18033).
145. neriakc/"Selzar L-Crit", say "Armor". Gives "Note to Kanthuk" (2416).
146. butcher/"Kanthuk Ogrebane", hand "Note to Kanthuk" (2416). Sets `Kanthuk` to `ghoul`.
147. butcher/"Kanthuk Ogrebane", say "Strange Image". Requires `Kanthuk` set. Gives "Pendant" (2414).
148. cauldron/"Llara", hand "Pendant" (2414). Sets `Llara` to `ghoul`.
149. cauldron/"Llara", say "Ruathey". Requires `Llara` set. Gives "Note to Ruathey" (2417).
150. lavastorm/"Ruathey", hand "Note to Ruathey" (2417). Sets `Ruathey` to `ghoul`.
151. lavastorm/"Ruathey", hand "Note to Ruathey" (2417). Sets `ruathey_note` to `1`.
152. lavastorm/"Ruathey", say "Bag". Requires `Ruathey` set. Requires `ruathey_note` ==1. Requires `ruathey_note` set. Gives "Nobleman's Bag" (17878).
153. Loot "Ghoul's Heart" (2410) from "A Ghoul" (NPC 63011) in `unrest`. Drop cache: 25% chance per kill.
154. Loot "Amstaf's Scroll" (2411) from "A Goblin Thief" (NPC 6150) in `highkeep`. Drop cache: 35% chance per kill.
155. Loot "Blade of Nobility" (2412) from "A Crazed Goblin" (NPC 68162) in `butcher`. Drop cache: 10.57% chance per kill.
156. Loot "Hilt of the Nobleman" (2413) from "Ekeros" in `najena`.
157. Loot "Hilt of the Nobleman" (2413) from "A Skeleton" in `najena`.
158. Combine in "Nobleman's Bag" (17878): "Ghoul's Heart" (2410), "Amstaf's Scroll" (2411), "Blade of Nobility" (2412), "Hilt of the Nobleman" (2413). Produces "Ghoulbane" (5403). The combine does not fail.
159. airplane/"Inte Akera", hand "Ghoulbane" (5403). Gives "Inte's Second Blessing" (18034).
160. Loot "Torn, Burnt Book" (19071) from "Lord Nagafen" in `soldungb`.
161. Loot "Torn, Burnt Book" (19071) from "Melalafen" in `westwastes`.
162. Loot "Torn, Burnt Book" (19071) from "Severilous" in `emeraldjungle`.
163. Loot "Torn, Burnt Book" (19071) from "Talendor" in `skyfire`.
164. Loot "Torn, Burnt Book" (19071) from "The Fabled Severilous".
165. Loot "Torn, Frost-covered Book" (19070) from "Faydedar" in `timorous`.
166. Loot "Torn, Frost-covered Book" (19070) from "Gorenaire" in `dreadlands`.
167. Loot "Torn, Frost-covered Book" (19070) from "Lady Vox" in `permafrost`.
168. neriakb/"Rysva To-Biath", hand "Torn, Frost-covered Book" (19070) + "Torn, Burnt Book" (19071). Gives "Book of Scale" (18302).
169. oceanoftears/"Oracle Of K-Arnon", hand "Book of Scale" (18302). Gives "Miragul's Phylactery" (19072).
170. Hand "Miragul's Phylactery" (19072) to everfrost/"Lich Of Miragul". Spawns "Spawn Miragul" (30094). Loot "Miragul's Head" (19073) from "Spawn Miragul".
171. Hand "Miragul's Phylactery" (19072) to everfrost/"Lich Of Miragul". Spawns "Spawn Miragul" (30094). Loot "Miragul's Robe" (1254) from "Spawn Miragul".
172. airplane/"Inte Akera", hand "Miragul's Robe" (1254) + "Inte's First Blessing" (18033) + "Inte's Second Blessing" (18034) + "Miragul's Head" (19073). Gives "Fiery Avenger" (11050).
173. fearplane/"Irak Altil", hand "Fiery Avenger" (11050) + "Mark of Atonement" (29010). Gives "Fiery Defender" (10099).
174. hohonora/"Irak Altil", say "Hail". Sets `paladin_epic` to `6`.
175. Loot "Top Section of an Engraved Signet" (9956) from "An Ikaav Miragenist" (NPC 301015) in `bloodfields`. Drop cache: 6.08% chance per kill.
176. Loot "Bottom Section of an Engraved Signet" (10399) from "An Ikaav Castigator" (NPC 301003) in `bloodfields`. Drop cache: 4% chance per kill.
177. Loot "Center Section of an Engraved Signet" (10235) from "An Ikaav Deathbeckoner" (NPC 301008) in `bloodfields`. Drop cache: 5.13% chance per kill.
178. bloodfields/"Cryssa", hand "Top Section of an Engraved Signet" (9956) + "Center Section of an Engraved Signet" (10235) + "Bottom Section of an Engraved Signet" (10399). Gives "Enchanted Signet of the Disciples" (12080).
179. bloodfields/"Cryssa", hand "Top Section of an Engraved Signet" (9956) + "Center Section of an Engraved Signet" (10235) + "Bottom Section of an Engraved Signet" (10399). Sets `cleric20_darkdisciples` to `1`.
180. Loot "Redis' Soulstone" (69983) from "Shade of Redis Linrok" in `dranikcatacombsa`.
181. global/"Global Player", combine recipe 19914. Sets `ranger_epic` to `8`.
182. Spawns "Durunal the Cursebearer" (300087) in `wallofslaughter` on enter.
183. Loot "Dark and Twisted Sword" (69971) from "Durunal the Cursebearer".
184. hohonora/"Irak Altil", hand "Dark and Twisted Sword" (69971). Requires `paladin_epic` ==6. Gives "Dark and Twisted Sword" (69972).
185. Combine in "Dark and Twisted Sword" (69972): "Rithnok's Soulstone" (69941), "Drema's Soulstone" (69952), "Reiya's Soulstone" (69942), "Redis' Soulstone" (69983). Produces "Redemption" (64031). The combine does not fail.
186. hohonora/"Irak Altil", say "Tell Me About Your Master". Sets `paladin_epic` to `9`.
187. qeynos2/"Camlend Serbold", say "Gem". Requires `paladin_epic` ==9. Gives "Unfilled Set of Prayer Beads" (69968).
188. rivervale/"Kaya Cloudfoot", say "Different About It". Requires `paladin_epic` ==9. Gives "Note from Kaya" (69970).
189. rivervale/"Deputy Cheel", hand "Note from Kaya" (69970). Gives "Rivervale Prayer Bead" (69967).
190. akanon/"Lewis Reldnok", say "Blessed Gem". Triggers `akanon/lewis reldnok#timer:check_sit`.
191. Sit before the NPC while its timer checks your posture.
192. akanon/"Lewis Reldnok", on timer check_sit. Gives "Ak'anon Prayer Bead" (69966).
193. erudnint/"Josper Kenshed", say "Collect Component". Gives "Empty Bag" (17944).
194. Loot "Goblin Ice Necklace" (13897) from "Redwind" in `everfrost`.
195. Loot "Goblin Ice Necklace" (13897) from "An Ice Goblin Scout" in `everfrost`.
196. Loot "Goblin Ice Necklace" (13897) from "An Ice Goblin Whelp" in `everfrost`.
197. Loot "Goblin Ice Necklace" (13897) from "An Icy Orc" in `everfrost`.
198. Loot "Goblin Ice Necklace" (13897) from "Ice Goblin Diver" in `everfrost`.
199. Combine in "Empty Bag" (17944): "Goblin Ice Necklace" (13897). Produces "Bag of Ice Necklaces" (13898). The combine does not fail.
200. halas/"Lysbith Mcnaff", hand "Bag of Ice Necklaces" (13898). Gives "Iron Ration" (13005).
201. Loot "Cask" (16580) from "Tugog Grigol" in `rathemtn`.
202. Common item: Hops (16591). Listed in 31 zones.
203. Common item: Malt (16595). Listed in 30 zones.
204. Common item: Yeast (16596). Listed in 30 zones.
205. Combine in "Portable Drink Barrel" (17179): "Cask" (16580), "Hops" (16591), "Malt" (16595), "Yeast" (16596). Produces "Mead" (13008). Requires Brewing, trivial 41.
206. erudnext/"Reklon Gnallen", hand "Iron Ration" (13005) + "Mead" (13008). Requires `paladin_epic` ==9. Gives "Erudin Prayer Bead" (69965).
207. Summon "Quiver of Marr" (17307) by casting "Quiver of Marr".
208. rathemtn/"Shin Master Grubbus", hand "Quiver of Marr" (17307). Requires `paladin_epic` ==9. Gives "Gukta Prayer Bead" (69964).
209. Common item: Barley (16590). Listed in 28 zones.
210. Combine in "Medicine Bag" (17901): "Hand-Formed Bottle" (45232), "Ensnaring Concoction V" (45236). Produces "Empty Vial" (10062), "Cork" (16851), "Formed Ensnaring Concoction V" (45258). Requires Alchemy, trivial 41.
211. Combine in Brew Barrel (19): "Bottle of Aged Bloodwine" (51163), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aged Bloodwine" (51164). Requires Brewing, trivial 255.
212. 11 other recipes also produce Cork (16851).
213. Combine in "Portable Drink Barrel" (17179): "Water Flask" (13006), "Celestial Essence" (9650). Produces "Purified Water" (12607). Requires Brewing, trivial 58.
214. Combine in "Tracker's Water Extractor" (17987): "Purification Tablet" (12630), "Water Reed" (12778). Produces "Purified Water" (12607) x3. Requires Pottery. The combine does not fail.
215. 3 other recipes also produce Purified Water (12607).
216. Forage "Sand Verbena" (65582) in `taka`.
217. Forage "Sand Verbena" (65582) in `takb`.
218. Forage "Sand Verbena" (65582) in `takc`.
219. Forage "Sand Verbena" (65582) in `takd`.
220. Forage "Sand Verbena" (65582) in `take`.
221. Forage "Sand Verbena" (65582) in `takf`.
222. Forage "Sand Verbena" (65582) in `takg`.
223. Forage "Sand Verbena" (65582) in `takh`.
224. Forage "Sand Verbena" (65582) in `taki`.
225. Forage "Sand Verbena" (65582) in `takj`.
226. Combine in Brew Barrel (19): "Barley" (16590), "Bottle" (16598), "Cork" (16851), "Hops" (16591), "Purified Water" (12607), "Sand Verbena" (65582), "Yeast" (16596). Produces "Bottle of Double Brewed Double Dry Stout" (51157). Requires Brewing, trivial 226.
227. kaladimb/"Datur Nightseer", hand "Bottle of Double Brewed Double Dry Stout" (51157). Requires `paladin_epic` ==9. Gives "Kaladim Prayer Bead" (69963).
228. felwithea/"General Jyleel", hand platinum:1000. Requires `paladin_epic` ==9. Gives "Felwithe Prayer Bead" (69962).
229. Ground spawn of "Freeport Prayer Bead" (69961) in `freeportwest`.
230. Ground spawn of "Freeport Prayer Bead" (69961) in `freportn`.
231. qeynos2/"Ziska Ironforge", hand platinum:500. Requires `paladin_epic` ==9. Gives "Qeynos Prayer Bead" (69960).
232. Combine in "Unfilled Set of Prayer Beads" (69968): "Rivervale Prayer Bead" (69967), "Ak'anon Prayer Bead" (69966), "Erudin Prayer Bead" (69965), "Gukta Prayer Bead" (69964), "Kaladim Prayer Bead" (69963), "Felwithe Prayer Bead" (69962), "Freeport Prayer Bead" (69961), "Qeynos Prayer Bead" (69960). Produces "Set of Prayer Beads" (69969). The combine does not fail.
233. dranikhollowsc/"Anetal", hand "Set of Prayer Beads" (69969). Sets `paladin_epic_hollowc` to `2`.
234. natimbi/"Kemik Arulon", hand "Set of Prayer Beads" (69969). Sets `paladin_epic_hollowc` to `1`.
235. natimbi/"Kemik Arulon", say "Hail". Requires `paladin_epic_hollowc` ==2. Requires `paladin_epic` ==9. Requires `paladin_epic_hollowc` ==1. Gives "Token of Compassion" (69953).
236. oasis/"Paladin Epic", say "Hail". Requires `pal_chest_keel` unset. Gives "Keelee's Brooch" (69982).
237. sro/"Instructor Maerceci", hand "Keelee's Brooch" (69982). Gives "Token of Chivalry" (69954).
238. Loot "Valdoon Kel'Novar's Heart" (69981) from "Valdoon Kel'Novar" in `mmcc`.
239. felwithea/"Galrun Starforge", hand "Valdoon Kel'Novar's Heart" (69981). Gives "Token of Cleansing" (69956).
240. provinggrounds/"Pashia Clouddancer", say "Note". Gives "Note from Pashia" (69973).
241. nedaria/"Duram Firechaser", hand "Note from Pashia" (69973). Gives "Token of Heroism" (69955).
242. Say "Check Lorb" to anguish/"Zone Status".
243. Spawns "Orb of Discordant Energy" (317087).
244. Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy".
245. 4 alternative loot source(s) also yield Globe of Discordant Energy (47100).
246. airplane/"Inte Akera", hand "Globe of Discordant Energy" (47100). Gives "Token of Conviction" (69957).

## `paladin_epic`

Values written: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11.

### 1. irak altil — say hail

Zone: `hohonora`.

> Ah

Sets `paladin_epic` to `1`.

- Needs Rithnok's Soulstone (69941).
- Needs Drema's Soulstone (69952).
- Needs Reiya's Soulstone (69942).
- Needs `paladin_epic` unset.
- One of: Fiery Defender (10099); Couragebringer (69913).
In script order:

1. Sets `paladin_epic` to `6`.
2. Sets `paladin_epic` to `1`.


How the items are reached:

- Rithnok's Soulstone (69941)
  - Prerequisite: "Rithnok's Soulstone" (69941). See section 0.
- Drema's Soulstone (69952)
  - Prerequisite: "Drema's Soulstone" (69952). See section 0.
- Reiya's Soulstone (69942)
  - Prerequisite: "Reiya's Soulstone" (69942). See section 0.
- Fiery Defender (10099)
  - Prerequisite: "Fiery Defender" (10099). See section 0.
- Couragebringer (69913)
  - Prerequisite: "Couragebringer" (69913). See section 0.

### 2. enic ruklin — say track down

Zone: `qeynos2`.

> Very well,

Sets `paladin_epic` to `2`.

- Needs `paladin_epic` ==1.
In script order:

1. Sets `paladin_epic` to `2`.


### 3. brunar rankin — say hail

Zone: `freporte`.

> How are you? Please excuse my stench. I fish all day and night just to feed my large family. You look like an adventurer. That must be exciting. I am but a h...

Sets `paladin_epic` to `3`.

- Needs `paladin_epic` >=2.
In script order:

1. Sets `paladin_epic` to `3`.
2. Gives Iksar's Note (69934).


### 4. enic ruklin — hand 69929+69930+69931+69932

Zone: `qeynos2`.

Sets `paladin_epic` to `4`.

- Turn in x1: Corrupted Koalindl's Heart (69929).
- Turn in x1: Corrupted Koalindl's Heart (69930).
- Turn in x1: Corrupted Koalindl's Heart (69931).
- Turn in x1: Corrupted Koalindl's Heart (69932).
In script order:

1. Sets `paladin_epic` to `4`.
2. Gives Seal of Enic (69933).


How the items are reached:

- Corrupted Koalindl's Heart (69929)
  - Spawns "A Corrupted Koalindl" (69141) in `oot` on event_fish_success.
  - Loot "Corrupted Koalindl's Heart" (69929) from "A Corrupted Koalindl".
- Corrupted Koalindl's Heart (69930)
  - Spawns "A Corrupted Koalindl" (224432) in `gunthak` on event_fish_success.
  - Loot "Corrupted Koalindl's Heart" (69930) from "A Corrupted Koalindl".
- Corrupted Koalindl's Heart (69931)
  - Spawns "A Corrupted Koalindl" (93306) in `overthere` on event_fish_success.
  - Loot "Corrupted Koalindl's Heart" (69931) from "A Corrupted Koalindl".
- Corrupted Koalindl's Heart (69932)
  - Spawns "A Corrupted Koalindl" (182150) in `nedaria` on event_fish_success.
  - Loot "Corrupted Koalindl's Heart" (69932) from "A Corrupted Koalindl".

### 5. mikhal young — hand 69946

Zone: `dawnshroud`.

Sets `paladin_epic` to `5`.

- Needs `paladin_epic` ==4.
- Turn in x1: Drema's Fingerbone (69946).
In script order:

1. Sets `paladin_epic` to `5`.
2. Gives Drema's Fingerbone (69946).


How the items are reached:

- Drema's Fingerbone (69946)
  - Prerequisite: "Drema's Fingerbone" (69946). See section 0.

### 6. irak altil — say hail

Zone: `hohonora`.

> Ah

Sets `paladin_epic` to `6`.

- Needs Rithnok's Soulstone (69941).
- Needs Drema's Soulstone (69952).
- Needs Reiya's Soulstone (69942).
- Needs `paladin_epic` unset.
- One of: Fiery Defender (10099); Couragebringer (69913).
In script order:

1. Sets `paladin_epic` to `6`.
2. Sets `paladin_epic` to `1`.


How the items are reached:

- Rithnok's Soulstone (69941)
  - Prerequisite: "Rithnok's Soulstone" (69941). See section 0.
- Drema's Soulstone (69952)
  - Prerequisite: "Drema's Soulstone" (69952). See section 0.
- Reiya's Soulstone (69942)
  - Prerequisite: "Reiya's Soulstone" (69942). See section 0.
- Fiery Defender (10099)
  - Prerequisite: "Fiery Defender" (10099). See section 0.
- Couragebringer (69913)
  - Prerequisite: "Couragebringer" (69913). See section 0.

### 7. irak altil — hand 69971

Zone: `hohonora`.

Sets `paladin_epic` to `7`.

- Needs `paladin_epic` ==6.
- Turn in x1: Dark and Twisted Sword (69971).
In script order:

1. Sets `paladin_epic` to `7`.
2. Gives Dark and Twisted Sword (69972).


How the items are reached:

- Dark and Twisted Sword (69971)
  - Spawns "Durunal the Cursebearer" (300087) in `wallofslaughter` on enter.
  - Loot "Dark and Twisted Sword" (69971) from "Durunal the Cursebearer".

### 8. global player — combine recipe 19880

Zone: `global`.

Sets `paladin_epic` to `8`.

In script order:

1. Sets `paladin_epic` to `8`.


Combine:

- `recipe:19880` is combined in Dark and Twisted Sword (69972).
  - Prerequisite: "Dark and Twisted Sword" (69972). See section 0.
  - Put in x1: Rithnok's Soulstone (69941).
    - Prerequisite: "Rithnok's Soulstone" (69941). See section 0.
  - Put in x1: Drema's Soulstone (69952).
    - Prerequisite: "Drema's Soulstone" (69952). See section 0.
  - Put in x1: Reiya's Soulstone (69942).
    - Prerequisite: "Reiya's Soulstone" (69942). See section 0.
  - Put in x1: Redis' Soulstone (69983).
    - Loot "Redis' Soulstone" (69983) from "Shade of Redis Linrok" in `dranikcatacombsa`.
  - Produces Redemption (64031).
  - The combine does not fail.

### 9. irak altil — say tell me about your master

Zone: `hohonora`.

> Yes, this was my final master, the one who rarely taught knights. You have proven yourself to be a powerful and honorable paladin, and you have surpassed any...

Sets `paladin_epic` to `9`.

- Needs Redemption (64031).
In script order:

1. Sets `paladin_epic` to `9`.


How the items are reached:

- Redemption (64031)
  - Prerequisite: "Redemption" (64031). See section 0.

### 10. inte akera — hand 47100

Zone: `airplane`.

Sets `paladin_epic` to `10`.

- Needs Token of Compassion (69953).
- Needs Token of Chivalry (69954).
- Needs Token of Heroism (69955).
- Needs Token of Cleansing (69956).
- Turn in x1: Globe of Discordant Energy (47100).
In script order:

1. Sets `paladin_epic` to `10`.
2. Gives Token of Conviction (69957).
3. Gives Token of Loyalty (69958).
4. Gives Scabbard of the Righteous (69959).


How the items are reached:

- Token of Compassion (69953)
  - Prerequisite: "Token of Compassion" (69953). See section 0.
- Token of Chivalry (69954)
  - Prerequisite: "Token of Chivalry" (69954). See section 0.
- Token of Heroism (69955)
  - Prerequisite: "Token of Heroism" (69955). See section 0.
- Token of Cleansing (69956)
  - Prerequisite: "Token of Cleansing" (69956). See section 0.
- Globe of Discordant Energy (47100)
  - Say "Check Lorb" to anguish/"Zone Status".
  - Spawns "Orb of Discordant Energy" (317087).
  - Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy".
  - 4 alternative loot source(s) also yield Globe of Discordant Energy (47100).

### 11. global player — combine recipe 19925

Zone: `global`.

Sets `paladin_epic` to `11`.

In script order:

1. Sets `paladin_epic` to `11`.


Combine:

- `recipe:19925` is combined in Scabbard of the Righteous (69959).
  - Prerequisite: "Scabbard of the Righteous" (69959). See section 0.
  - Put in x1: Token of Loyalty (69958).
    - Prerequisite: "Token of Loyalty" (69958). See section 0.
  - Put in x1: Token of Conviction (69957).
    - Prerequisite: "Token of Conviction" (69957). See section 0.
  - Put in x1: Token of Cleansing (69956).
    - Prerequisite: "Token of Cleansing" (69956). See section 0.
  - Put in x1: Token of Heroism (69955).
    - Prerequisite: "Token of Heroism" (69955). See section 0.
  - Put in x1: Token of Chivalry (69954).
    - Prerequisite: "Token of Chivalry" (69954). See section 0.
  - Put in x1: Token of Compassion (69953).
    - Prerequisite: "Token of Compassion" (69953). See section 0.
  - Put in x1: Redemption (64031).
    - Prerequisite: "Redemption" (64031). See section 0.
  - Produces Nightbane, Sword of the Valiant (48147).
  - The combine does not fail.

### Steps on `paladin_epic` that do not change it

- `abysmal` lovine lemise, hand 69923 needs `paladin_epic` ==5.
  - Sets `paladin_epic_reiya` to `1`.
  - Turn in Lovine's Potion Bag (69923).
- `abysmal` lovine lemise, say ingredients needs `paladin_epic` ==5.
  - Gives Lovine's Potion Bag (69922).
- `crushbone` player, on enter needs `paladin_epic` ==9.
  - Sets `paladin_epic_crushbone` to `1`.
  - Spawns Orc Messenger (58060).
  - Loots Sunshard Ore (33792).
  - Loots Orcish Battle Plans (69977).
  - Loots Steamfont Geysers (87563).
  - Loots Staurolite (97002).
- `dawnshroud` denns rootenpaw, hand 69946 needs `paladin_epic` ==5.
  - Turn in Drema's Fingerbone (69946).
  - Gives Bone Collector's Bag (69947).
- `dawnshroud` denns rootenpaw, hand 69948 needs `paladin_epic` ==5.
  - Turn in Bone Collector's Bag (69948).
  - Gives Enchanted Bone Powder (69949).
- `dawnshroud` mikhal young, say find anything needs `paladin_epic` ==4.
  - Gives Drema's Locket (69945).
- `erudnext` reklon gnallen, hand 13005+13008 needs `paladin_epic` ==9.
  - Turn in Iron Ration (13005).
  - Turn in Mead (13008).
  - Gives Erudin Prayer Bead (69965).
- `felwithea` galrun starforge, say explained needs `paladin_epic` ==9.
  - Gives Galrun's bag (69975).
- `felwithea` galrun starforge, hand 69976 needs `paladin_epic` ==9.
  - Sets `paladin_epic_mmcc` to `1`.
  - Turn in Galrun's bag (69976).
- `felwithea` general jyleel, hand platinum:1000 needs `paladin_epic` ==9.
  - Gives Felwithe Prayer Bead (69962).
- `felwithea` general jyleel, hand platinum:500 needs `paladin_epic` ==9.
- `kaladimb` datur nightseer, hand 51157 needs `paladin_epic` ==9.
  - Turn in Bottle of Double Brewed Double Dry Stout (51157).
  - Gives Kaladim Prayer Bead (69963).
- `letalis` drema young, hand 69945 needs `paladin_epic` set.
  - Turn in Drema's Locket (69945).
  - Gives Drema's Fingerbone (69946).
- `letalis` drema young, hand 69949 needs `paladin_epic` set.
  - Spawns Drema Young (169128).
  - Loots Drema's Soulstone (69928).
  - Turn in Enchanted Bone Powder (69949).
- `natimbi` kemik arulon, say hail needs `paladin_epic` ==9.
  - Gives Token of Compassion (69953).
- `ponightmare` player, on loot needs `paladin_epic` >=5.
  - Sets `paladin_epic_pon` to `1`.
  - Spawns a chest (283157).
  - Sets `wiz_pon_chest` to `1`.
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
- `qeynos2` camlend serbold, say gem needs `paladin_epic` ==9.
  - Gives Unfilled Set of Prayer Beads (69968).
- `qeynos2` ziska ironforge, hand platinum:500 needs `paladin_epic` ==9.
  - Gives Qeynos Prayer Bead (69960).
- `rathemtn` shin master grubbus, hand 17307 needs `paladin_epic` ==9.
  - Turn in Quiver of Marr (17307).
  - Gives Gukta Prayer Bead (69964).
- `rivervale` kaya cloudfoot, say different about it needs `paladin_epic` ==9.
  - Gives Note from Kaya (69970).
- `skyfire` dry sapara, say hail needs `paladin_epic` ==4.
  - Spawns Rithnok the Tormented (91193).
  - Loots Rithnok's Soulstone (69935).
- `steamfont` bigilam wantilans, hand 9181 needs `paladin_epic` ==9.
  - Turn in Mana Battery - Class Six (9181).
  - Gives Slain Vampire's Heart (69979).
- `steamfontmts` bigilam wantilans, hand 9181 needs `paladin_epic` ==9.
  - Turn in Mana Battery - Class Six (9181).
  - Gives Slain Vampire's Heart (69979).
- `vxed` player, on loot needs `paladin_epic` >=5.
  - Sets `paladin_epic_vxed` to `1`.
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
- `wallofslaughter` player, on loot needs `paladin_epic` ==6.
  - Sets `warr_epic_wos` to `1`.
  - Spawns a chest (Epic 1.5) (283157).
  - Sets `wiz_wos_chest` to `1`.
  - Sets `paladin_epic_wos` to `1`.
  - Sets `shaman_epic_wos` to `1`.
  - Spawns a chest (Epic 1.5) (893).
  - Sets `druid_epic_wos` to `1`.
  - Sets `rng_wos_chest` to `1`.
  - Sets `ench_wos_chest` to `1`.
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

- `paladin_epic_crushbone` set to 1 at crushbone/player.
- `paladin_epic_ferubi` set to 1 at ferubi/player.
- `paladin_epic_hollowc` set to 1, 2 at dranikhollowsc/anetal, natimbi/kemik arulon.
- `paladin_epic_mmcc` set to 1 at felwithea/galrun starforge.
- `paladin_epic_mmcc_chest` set to 1 at mmcc/player.
- `paladin_epic_pon` set to 1 at ponightmare/player.
- `paladin_epic_reiya` set to 1 at abysmal/lovine lemise.
- `paladin_epic_vxed` set to 1 at vxed/player.
- `paladin_epic_wos` set to 1 at wallofslaughter/player.
