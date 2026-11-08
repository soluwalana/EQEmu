# Paladin

Steps taken from the quest graph only. **Broken** means the graph has no edge for that value or that item.

Flags with writes: `paladin_epic`.

## 0. Prerequisites

Each list is the order you obtain that item. Later steps point here instead of repeating the chain.

### "Rithnok's Soulstone" (69941)

1. Say "Hail" to skyfire/"Dry Sapara".
2. Spawns "Rithnok the Tormented" (91193).
3. Loot "Rithnok's Soulstone" (69935) from "Rithnok the Tormented".
4. skyfire/"Dry Sapara", hand "Rithnok's Soulstone" (69935). Gives "Rithnok's Soulstone" (69936).
5. Ground spawn of "Soulstone Shard" (69937) in `draniksscar`.
6. Ground spawn of "Soulstone Shard" (69938) in `bloodfields`.
7. Ground spawn of "Soulstone Shard" (69939) in `causeway`.
8. Ground spawn of "Soulstone Shard" (69940) in `dranik`.
9. Combine in "Rithnok's Soulstone" (69936): "Soulstone Shard" (69937), "Soulstone Shard" (69938), "Soulstone Shard" (69939), "Soulstone Shard" (69940). Produces "Rithnok's Soulstone" (69941). The combine does not fail.

### "Drema's Soulstone" (69952)

1. Hand "Enchanted Bone Powder" (69949) to letalis/"Drema Young". Spawns "Drema Young" (169128). Loot "Drema's Soulstone" (69928) from "Drema Young".
2. Loot "Drema's Soulstone" (69928) from "Drema Young".
3. Loot "Drema's Soulstone" (69928) from "Drema Young" in `letalis`.
4. Loot "Soulstone Shard" (69950) from "Coterie Corruptor" in `tenebrous`.
5. Say "Mujaki Death" to ponightmare/"Mujaki".
6. Spawns "Shade of Mujaki the Devourer" (204081).
7. Loot "Soulstone Shard" (69951) from "Shade of Mujaki the Devourer".
8. Combine in "Drema's Soulstone" (69928): "Soulstone Shard" (69950), "Soulstone Shard" (69951). Produces "Drema's Soulstone" (69952). The combine does not fail.

### "Reiya's Soulstone" (69942)

1. freporte/"Brunar Rankin", say "Hail". Sets `paladin_epic` to `3`.
2. global/"Global Player", combine recipe 19880. Sets `paladin_epic` to `8`.
3. Spawns "A Corrupted Koalindl" (69141) in `oot` on event_fish_success.
4. Loot "Corrupted Koalindl's Heart" (69929) from "A Corrupted Koalindl".
5. Spawns "A Corrupted Koalindl" (224432) in `gunthak` on event_fish_success.
6. Loot "Corrupted Koalindl's Heart" (69930) from "A Corrupted Koalindl".
7. Spawns "A Corrupted Koalindl" (93306) in `overthere` on event_fish_success.
8. Loot "Corrupted Koalindl's Heart" (69931) from "A Corrupted Koalindl".
9. Spawns "A Corrupted Koalindl" (182150) in `nedaria` on event_fish_success.
10. Loot "Corrupted Koalindl's Heart" (69932) from "A Corrupted Koalindl".
11. qeynos2/"Enic Ruklin", hand "Corrupted Koalindl's Heart" (69929) + "Corrupted Koalindl's Heart" (69930) + "Corrupted Koalindl's Heart" (69931) + "Corrupted Koalindl's Heart" (69932). Sets `paladin_epic` to `4`.
12. dawnshroud/"Mikhal Young", say "Find Anything". Requires `paladin_epic` ==4. Gives "Drema's Locket" (69945).
13. letalis/"Drema Young", hand "Drema's Locket" (69945). Requires `paladin_epic` set. Requires `paladin_epic` >=4. Gives "Drema's Fingerbone" (69946).
14. dawnshroud/"Mikhal Young", hand "Drema's Fingerbone" (69946). Sets `paladin_epic` to `5`.
15. abysmal/"Lovine Lemise", say "Ingredients". Requires `paladin_epic` ==5. Gives "Lovine's Potion Bag" (69922).
16. No quest step gives Ra`Tuk Screambringer's Jaw (69921). The dump lists it in barindu.
17. Loot "Noc Fleshfeasters Tail" (69920) from "A Noc Fleshfeaster" in `riwwi`.
18. Loot "Mastruq Havocblade Blood" (69919) from "A Mastruq Havocblade" in `qinimi`.
19. Loot "Mastruq Havocblade Blood" (69919) from "A Mastruq Warfiend" in `qinimi`.
20. Loot "Potameid Seaweed Strands" (69918) from "An Entrapped Potameid" in `natimbi`.
21. Combine in "Lovine's Potion Bag" (69922): "Ra'Tuk Screambringer's Jaw" (69921), "Noc Fleshfeasters Tail" (69920), "Mastruq Havocblade Blood" (69919), "Potameid Seaweed Strands" (69918). Produces "Lovine's Potion Bag" (69923). The combine does not fail.
22. abysmal/"Lovine Lemise", hand "Lovine's Potion Bag" (69923). Sets `paladin_epic_reiya` to `1`.
23. Summon "Foldable Medicine Bag" (17770) by casting "Unfold Medicine Bag".
24. Common item: Fine Potion Vial (95846). Listed in 15 zones.
25. Common item: Robust Shadow Essence (96911). Listed in 5 zones.
26. Loot "Sage Leaf" (14215) from "a Di'zok Herbalist" in `chardok`.
27. Loot "Sage Leaf" (14215) from "a Sarnak Herb Collector" in `chardok`.
28. Loot "Sage Leaf" (14215) from "an Apprentice Herbalist" in `chardok`.
29. Loot "Valerian Root" (14230) from "a Di'zok Herbalist" in `chardok`.
30. Loot "Valerian Root" (14230) from "a Sarnak Herb Collector" in `chardok`.
31. Loot "Valerian Root" (14230) from "an Apprentice Herbalist" in `chardok`.
32. Common item: Woundwart (16526). Listed in 9 zones.
33. Combine in "Foldable Medicine Bag" (17770): "Fine Potion Vial" (95846), "Robust Shadow Essence" (96911), "Sage Leaf" (14215), "Valerian Root" (14230), "Woundwart" (16526). Produces "Mist of the Breathless" (96937). Requires Alchemy, trivial 224.
34. abysmal/"Reiya The Pained", hand "Mist of the Breathless" (96937). Requires `paladin_epic_reiya` ==1. Gives "Reiya's Soulstone" (69924).
35. Spawns "Shade of Reiya the Pained" (284104) in `ferubi` on enter.
36. Loot "Soulstone Shard" (69943) from "Shade of Reiya the Pained".
37. Loot "Soulstone Shard" (69944) from "Vuranish Xxuro" in `vxed`.
38. Combine in "Reiya's Soulstone" (69924): "Soulstone Shard" (69943), "Soulstone Shard" (69944). Produces "Reiya's Soulstone" (69942). The combine does not fail.

### "Fiery Defender" (10099)

1. Loot "Tainted Darksteel Sword" (29000) from "Keeper of the Tombs" in `hole`.
2. freeporteast/"Peasant Woman", say "I Will Take It". Gives "Bucket of Water" (29008).
3. freportw/"Peasant Woman", say "I Will Take It". Gives "Bucket of Water" (29008).
4. freeporteast/"Joshua", hand "Bucket of Water" (29008). Gives "Bucket of Pure Water" (29009).
5. freportw/"Joshua", hand "Bucket of Water" (29008). Gives "Bucket of Pure Water" (29009).
6. erudnext/"Reklon Gnallen", hand "Tainted Darksteel Sword" (29000) + "Bucket of Pure Water" (29009). Gives "Gleaming Crested Sword" (29003).
7. Loot "Tainted Darksteel Breastplate" (29001) from "Thought Destroyer" in `hateplaneb`.
8. kaladimb/"Nella Stonebraids", say "Jark". Gives "Cold Plate of Beef and Bread" (29007).
9. kaladimb/"Nella Stonebraids", say "Dinner". Gives "Cold Plate of Beef and Bread" (29007).
10. kaladimb/"Jark", hand "Cold Plate of Beef and Bread" (29007). Gives "Pure Crystal" (29006).
11. erudnext/"Reklon Gnallen", hand "Tainted Darksteel Breastplate" (29001) + "Pure Crystal" (29006). Gives "Gleaming Crested Breastplate" (29004).
12. Loot "Tainted Darksteel Shield" (29002) from "Kirak Vil" in `nektulos`.
13. felwithea/"Elia The Pure", hand "Tainted Darksteel Shield" (29002). Gives "Gleaming Crested Shield" (29005).
14. erudnext/"Reklon Gnallen", hand "Gleaming Crested Sword" (29003) + "Gleaming Crested Breastplate" (29004) + "Gleaming Crested Shield" (29005). Gives "Mark of Atonement" (29010).
15. No quest step gives Drom's Champagne (13829). The dump lists it in freeporteast, freporte, highpasshold.
16. freeporteast/"Tykar Renlin", hand "Drom's Champagne" (13829) + "Drom's Champagne" (13829) + "Drom's Champagne" (13829) + "Drom's Champagne" (13829). Gives "Bunker Cell #1" (12196).
17. freporte/"Tykar Renlin", hand "Drom's Champagne" (13829) + "Drom's Champagne" (13829) + "Drom's Champagne" (13829) + "Drom's Champagne" (13829). Gives "Bunker Cell #1" (12196).
18. Summon "Black Diamond of Nightmares" (29990) by casting "Imbue Nightmare".
19. poknowledge/"Aid Grimel", say "Versed In The Art Of Smithing". Gives "Filthy Breastplate" (15984).
20. Combine in "Mixing Bowl" (17906): "Celestial Solvent" (9731), "Words of Acquisition (Beza)" (11866). Produces "Celestial Essence" (9650). Requires Baking, trivial 15. The combine does not fail.
21. Combine in "Mixing Bowl" (17906): "Celestial Solvent" (9731), "Words of Burnishing" (11862). Produces "Celestial Essence" (9650). Requires Baking, trivial 15. The combine does not fail.
22. 67 other recipes also produce Celestial Essence (9650).
23. Common item: Jar of Acid (22133). Listed in 15 zones.
24. Combine in Brew Barrel (19): "Celestial Essence" (9650), "Jar of Acid" (22133). Produces "Acid Wash" (15987). Requires Brewing, trivial 151.
25. Combine in Forge (17): "Filthy Breastplate" (15984), "Acid Wash" (15987). Produces "Cleansed Breastplate" (15998). Requires Blacksmithing, trivial 227.
26. Common item: Mortar and Pestle (17904). Listed in 12 zones.
27. No quest step gives Sandstorm Pearl (29909). The dump lists it in bothunder.
28. Combine in "Mortar and Pestle" (17904): "Sandstorm Pearl" (29909). Produces "Powdered Sandstorm Pearl" (29520) x4. Requires Make Poison, trivial 255.
29. Common item: Firing Sheet (16906). Listed in 34 zones.
30. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
31. qeynos/"Wolten Grafe", say "Crush The Undead". Gives "Box For Bones" (17941).
32. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `steamfont`.
33. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `tox`.
34. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `toxxulia`.
35. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
36. toxxulia/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
37. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). The combine does not fail.
38. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
39. qeynos2/"Phin Esrinap", say "Supplies". Gives "Message to Konem" (18921).
40. qeytoqrg/"Konem Matse", hand "Message to Konem" (18921). Gives "Grathin's Invoice" (18922).
41. qeynos2/"Phin Esrinap", hand "Grathin's Invoice" (18922). Gives "Water Flask" (13006).
42. Say "Tm Devrak Death" to rujd/"Rujd".
43. Spawns "spawn chest with Heavy Orcish Prison Key" (245241).
44. Loot "Pod of Water" (13044) from "spawn chest with Heavy Orcish Prison Key".
45. Say "Tm Dokorel Death" to rujd/"Rujd".
46. Say "Tm Velrek Death" to rujd/"Rujd".
47. Say "Researcher Death" to rujg/"Rujg".
48. Spawns "A Barrel" (260015).
49. Loot "Pod of Water" (13044) from "A Barrel".
50. 3 other loot steps also yield Pod of Water (13044).
51. Forage "Pod of Water" (13044) in `ruja`.
52. Forage "Pod of Water" (13044) in `uqua`.
53. Forage "Pod of Water" (13044) in `yxtta`.
54. Combine in Brew Barrel (19): "Bottle of Aged Bloodwine" (51163), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aged Bloodwine" (51164). Requires Brewing, trivial 255.
55. Combine in Brew Barrel (19): "Bottle of Aldo's Bitter Ale" (75805), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aldo's Bitter Ale" (75811). Requires Brewing, trivial 15.
56. 17 other recipes also produce Bottle (16598).
57. Combine in Brew Barrel (19): "Pod of Water" (13044), "Bottle" (16598). Produces "Water Flask" (13006). Requires Brewing, trivial 21.
58. Combine in Pottery Wheel (21): "Water Flask" (13006), "Block of Clay" (16901). Produces "Small Block of Clay" (16900) x3. Requires Pottery, trivial 21.
59. Combine in Pottery Wheel (21): "Small Block of Clay" (16900), "Water Flask" (13006). Produces "Block of Clay" (16901). Requires Pottery, trivial 21.
60. Combine in Pottery Wheel (21): "Water Flask" (13006), "Large Block of Clay" (16902). Produces "Block of Clay" (16901) x2. Requires Pottery, trivial 21.
61. Combine in Pottery Wheel (21): "Block of Clay" (16901), "Water Flask" (13006). Produces "Large Block of Clay" (16902). Requires Pottery, trivial 21.
62. Common item: Large Bowl Sketch (16963). Listed in 29 zones.
63. Combine in Pottery Wheel (21): "Large Block of Clay" (16902), "Water Flask" (13006), "Large Bowl Sketch" (16963). Produces "Unfired Mixing Bowl" (16930). Requires Pottery, trivial 128.
64. Combine in Kiln (22): "Firing Sheet" (16906), "Unfired Mixing Bowl" (16930). Produces "Mixing Bowl" (17906). Requires Pottery, trivial 15.
65. Combine in "Mixing Bowl" (17906): "Sandstorm Pearl" (29909). Produces "Powdered Sandstorm Pearl" (29520) x4. Requires Baking. The combine does not fail.
66. Spawns "a Koka'Vor chieftain" (210236) in `postorms` on event_signal.
67. Loot "Storm Rider Blood" (29526) from "a Koka'Vor chieftain".
68. Loot "Storm Rider Blood" (29526) from "A stormrider" in `bothunder`.
69. Loot "Storm Rider Blood" (29526) from "Dolsoj Warrebs" in `bazaar`.
70. Loot "Storm Rider Blood" (29526) from "a Koka'Vor krovian" in `postorms`.
71. Loot "Storm Rider Blood" (29526) from "a Koka'Vor senvar" in `postorms`.
72. No quest step gives Drop of Pure Rain (29904). The dump lists it in bothunder.
73. Combine in Brew Barrel (19): "Powdered Sandstorm Pearl" (29520), "Storm Rider Blood" (29526), "Drop of Pure Rain" (29904). Produces "Hurricane Temper" (29533). Requires Brewing, trivial 135.
74. Combine in Forge (17): "Cleansed Breastplate" (15998), "Hurricane Temper" (29533). Produces "Tempered Breastplate" (15999). Requires Blacksmithing, trivial 229.
75. Combine in Forge (17): "Black Diamond of Nightmares" (29990), "Tempered Breastplate" (15999). Produces "Imbued Breastplate" (15985). Requires Blacksmithing 220. Trivial at 275.
76. poknowledge/"Aid Grimel", hand "Imbued Breastplate" (15985). Gives "Hardened Leather Signet" (16249).
77. poknowledge/"Aid Grimel", say "Skill In Brewing". Gives "Portable Drink Barrel" (17179).
78. Common item: Snake Scales (13070). Listed in 56 zones.
79. Combine in "Portable Drink Barrel" (17179): "Water Flask" (13006), "Snake Scales" (13070), "Bottle" (16598). Produces "Bog Juice" (16581). Requires Brewing, trivial 21.
80. Common item: Spit (17947). Listed in 34 zones.
81. Common item: Fire Beetle Eye (10307). Listed in 24 zones.
82. Spawns "Sepsis Rat" (45113) in `qcat` on event_death.
83. Loot "Rat Ears" (13072) from "Sepsis Rat".
84. Kill steamfont/"Diseased Female Rat". Spawns "A Young Plague Rat" (56086).
85. Loot "Rat Ears" (13072) from "A Young Plague Rat".
86. Kill steamfontmts/"Diseased Female Rat". Spawns "A Young Plague Rat" (448036).
87. Combine in "Spit" (17947): "Fire Beetle Eye" (10307), "Rat Ears" (13072). Produces "Edible Goo" (13498). Requires Baking, trivial 21.
88. freeporteast/"A Prisoner", hand "Bunker Cell #1" (12196) + "Edible Goo" (13498) + "Bog Juice" (16581). Gives "H. K. 102" (12143).
89. freportw/"A Prisoner", hand "Bunker Cell #1" (12196) + "Edible Goo" (13498) + "Bog Juice" (16581). Gives "H. K. 102" (12143).
90. highkeep/"Assistant Kiolna", hand "H. K. 102" (12143). Gives "Sealed Note" (18936).
91. paw/"Brother Hayle", hand "Sealed Note" (18936). Gives "Note" (18937).
92. southkarana/"Brother Hayle", hand "Sealed Note" (18936). Gives "Note" (18937).
93. Kill freportw/"Sir Lucan D-Lere". Spawns "Sir Lucan D'Lere" (9147).
94. Loot "Testimony of Truth" (18827) from "Sir Lucan D'Lere".
95. Loot "Testimony of Truth" (18827) from "Sir Lucan D'Lere" in `freeporteast`.
96. freeportwest/"Valeron Dushire", hand "Testimony of Truth" (18827). Gives "Brilliant Sword of Faith" (13947).
97. freportn/"Valeron Dushire", hand "Testimony of Truth" (18827). Gives "Brilliant Sword of Faith" (13947).
98. Hand "Token of Bravery" (12144) + "Token of Generosity" (13865) to freeportwest/"Merko Quetalis". Spawns "spawns Guard Willia" (383270). Loot "Token of Truth" (13866) from "spawns Guard Willia".
99. Hand "Token of Bravery" (12144) + "Token of Generosity" (13865) to freportn/"Merko Quetalis". Spawns "spawns Guard Willia" (8110). Loot "Token of Truth" (13866) from "spawns Guard Willia".
100. Loot "Token of Truth" (13866) from "Guard Willia".
101. freeportwest/"Merko Quetalis", hand "Token of Truth" (13866). Gives "Testimony" (18828).
102. freportn/"Merko Quetalis", hand "Token of Truth" (13866). Gives "Testimony" (18828).
103. Loot "Glowing Sword Hilt" (12197) from "Xicotl" in `mistmoore`.
104. paw/"Brother Hayle", hand "Glowing Sword Hilt" (12197) + "Brilliant Sword of Faith" (13947) + "Testimony" (18828) + "Note" (18937). Gives "SoulFire" (5504).
105. southkarana/"Brother Hayle", hand "Glowing Sword Hilt" (12197) + "Brilliant Sword of Faith" (13947) + "Testimony" (18828) + "Note" (18937). Gives "SoulFire" (5504).
106. airplane/"Inte Akera", hand "SoulFire" (5504). Gives "Inte's First Blessing" (18033).
107. lavastorm/"Ruathey", say "Bag". Gives "Nobleman's Bag" (17878).
108. Common item: Ghoul's Heart (2410). Listed in 8 zones.
109. No quest step gives Amstaf's Scroll (2411). The dump lists it in highkeep.
110. No quest step gives Blade of Nobility (2412). The dump lists it in butcher.
111. Loot "Hilt of the Nobleman" (2413) from "Ekeros" in `najena`.
112. Loot "Hilt of the Nobleman" (2413) from "A Skeleton" in `najena`.
113. Combine in "Nobleman's Bag" (17878): "Ghoul's Heart" (2410), "Amstaf's Scroll" (2411), "Blade of Nobility" (2412), "Hilt of the Nobleman" (2413). Produces "Ghoulbane" (5403). The combine does not fail.
114. airplane/"Inte Akera", hand "Ghoulbane" (5403). Gives "Inte's Second Blessing" (18034).
115. Hand "Miragul's Phylactery" (19072) to everfrost/"Lich Of Miragul". Spawns "Spawn Miragul" (30094). Loot "Miragul's Head" (19073) from "Spawn Miragul".
116. Loot "Miragul's Head" (19073) from "Miragul".
117. Hand "Miragul's Phylactery" (19072) to everfrost/"Lich Of Miragul". Spawns "Spawn Miragul" (30094). Loot "Miragul's Robe" (1254) from "Spawn Miragul".
118. Loot "Miragul's Robe" (1254) from "Miragul".
119. airplane/"Inte Akera", hand "Miragul's Robe" (1254) + "Inte's First Blessing" (18033) + "Inte's Second Blessing" (18034) + "Miragul's Head" (19073). Gives "Fiery Avenger" (11050).
120. fearplane/"Irak Altil", hand "Fiery Avenger" (11050) + "Mark of Atonement" (29010). Gives "Fiery Defender" (10099).

### "Couragebringer" (69913)

1. povalor/"Baltron Werters", say "Couragebringer". Sets `pre_pal` to `1`.
2. Requires `pre_pal` unset; no setter establishes this state.
3. povalor/"Baltron Werters", say "Couragebringer". Requires `pre_pal` unset. Gives "Baltron's Solvent" (69901).
4. sro/"Gilfal", hand "Baltron's Solvent" (69901). Requires `pre_pal` ==1. Gives "Gilfal's Scabbard" (69902).
5. Spawns "Neffiken Lord Kelek-Vor" (210229) in `postorms` on event_signal.
6. Loot "Broken Sword Piece" (69903) from "Neffiken Lord Kelek-Vor".
7. Loot "Broken Sword Piece" (69903) from "Neffiken Lord of Kelek'Vor".
8. Say "Control Timer" to hateplaneb/"Maestro".
9. Spawns "Maestro of Rancor" (186111).
10. Loot "Broken Sword Piece" (69904) from "Maestro of Rancor".
11. **Broken:** no event trigger found for `hateplaneb/maestro#timer:popmaestro`.
12. Spawns "Maestro of Rancor" (186111) after `hateplaneb/maestro#timer:popmaestro`.
13. Loot "Broken Sword Piece" (69905) from "Kaniz Painbringer" in `potorment`.
14. sro/"Gilfal", hand "Baltron's Solvent" (69901). Sets `pre_pal` to `2`.
15. Ground spawn of "Rune of Xor" (69909) in `potranquility`.
16. Ground spawn of "Rune of Yirno" (69908) in `mistmoore`.
17. Ground spawn of "Rune of Zota" (69907) in `scarlet`.
18. Ground spawn of "Rune Wilun" (69910) in `gunthak`.
19. everfrost/"Rombus", hand "Rune of Zota" (69907) + "Rune of Yirno" (69908) + "Rune of Xor" (69909) + "Rune Wilun" (69910). Requires `pre_pal` ==2. Gives "Broken Sword Piece" (69906).
20. Combine in "Gilfal's Scabbard" (69902): "Broken Sword Piece" (69903), "Broken Sword Piece" (69904), "Broken Sword Piece" (69905), "Broken Sword Piece" (69906). Produces "Fractured Couragebringer" (69911). The combine does not fail.
21. sro/"Gilfal", hand "Fractured Couragebringer" (69911). Sets `pre_pal` to `4`.
22. everfrost/"Rombus", hand "Rune of Zota" (69907) + "Rune of Yirno" (69908) + "Rune of Xor" (69909) + "Rune Wilun" (69910). Sets `pre_pal` to `3`.
23. sro/"Gilfal", hand "Fractured Couragebringer" (69911). Requires `pre_pal` ==3. Gives "Fractured Couragebringer" (69912).
24. povalor/"Baltron Werters", hand "Fractured Couragebringer" (69912). Requires `pre_pal` ==4. Gives "Couragebringer" (69913).

### "Drema's Fingerbone" (69946)

1. freporte/"Brunar Rankin", say "Hail". Sets `paladin_epic` to `3`.
2. global/"Global Player", combine recipe 19880. Sets `paladin_epic` to `8`.
3. Spawns "A Corrupted Koalindl" (69141) in `oot` on event_fish_success.
4. Loot "Corrupted Koalindl's Heart" (69929) from "A Corrupted Koalindl".
5. Spawns "A Corrupted Koalindl" (224432) in `gunthak` on event_fish_success.
6. Loot "Corrupted Koalindl's Heart" (69930) from "A Corrupted Koalindl".
7. Spawns "A Corrupted Koalindl" (93306) in `overthere` on event_fish_success.
8. Loot "Corrupted Koalindl's Heart" (69931) from "A Corrupted Koalindl".
9. Spawns "A Corrupted Koalindl" (182150) in `nedaria` on event_fish_success.
10. Loot "Corrupted Koalindl's Heart" (69932) from "A Corrupted Koalindl".
11. qeynos2/"Enic Ruklin", hand "Corrupted Koalindl's Heart" (69929) + "Corrupted Koalindl's Heart" (69930) + "Corrupted Koalindl's Heart" (69931) + "Corrupted Koalindl's Heart" (69932). Sets `paladin_epic` to `4`.
12. dawnshroud/"Mikhal Young", say "Find Anything". Requires `paladin_epic` ==4. Gives "Drema's Locket" (69945).
13. letalis/"Drema Young", hand "Drema's Locket" (69945). Requires `paladin_epic` set. Requires `paladin_epic` >=4. Gives "Drema's Fingerbone" (69946).

### "Dark and Twisted Sword" (69972)

1. Say "Hail" to skyfire/"Dry Sapara".
2. Spawns "Rithnok the Tormented" (91193).
3. Loot "Rithnok's Soulstone" (69935) from "Rithnok the Tormented".
4. skyfire/"Dry Sapara", hand "Rithnok's Soulstone" (69935). Gives "Rithnok's Soulstone" (69936).
5. Ground spawn of "Soulstone Shard" (69937) in `draniksscar`.
6. Ground spawn of "Soulstone Shard" (69938) in `bloodfields`.
7. Ground spawn of "Soulstone Shard" (69939) in `causeway`.
8. Ground spawn of "Soulstone Shard" (69940) in `dranik`.
9. Combine in "Rithnok's Soulstone" (69936): "Soulstone Shard" (69937), "Soulstone Shard" (69938), "Soulstone Shard" (69939), "Soulstone Shard" (69940). Produces "Rithnok's Soulstone" (69941). The combine does not fail.
10. Hand "Enchanted Bone Powder" (69949) to letalis/"Drema Young". Spawns "Drema Young" (169128). Loot "Drema's Soulstone" (69928) from "Drema Young".
11. Loot "Drema's Soulstone" (69928) from "Drema Young".
12. Loot "Drema's Soulstone" (69928) from "Drema Young" in `letalis`.
13. Loot "Soulstone Shard" (69950) from "Coterie Corruptor" in `tenebrous`.
14. Say "Mujaki Death" to ponightmare/"Mujaki".
15. Spawns "Shade of Mujaki the Devourer" (204081).
16. Loot "Soulstone Shard" (69951) from "Shade of Mujaki the Devourer".
17. Combine in "Drema's Soulstone" (69928): "Soulstone Shard" (69950), "Soulstone Shard" (69951). Produces "Drema's Soulstone" (69952). The combine does not fail.
18. freporte/"Brunar Rankin", say "Hail". Sets `paladin_epic` to `3`.
19. global/"Global Player", combine recipe 19880. Sets `paladin_epic` to `8`.
20. Spawns "A Corrupted Koalindl" (69141) in `oot` on event_fish_success.
21. Loot "Corrupted Koalindl's Heart" (69929) from "A Corrupted Koalindl".
22. Spawns "A Corrupted Koalindl" (224432) in `gunthak` on event_fish_success.
23. Loot "Corrupted Koalindl's Heart" (69930) from "A Corrupted Koalindl".
24. Spawns "A Corrupted Koalindl" (93306) in `overthere` on event_fish_success.
25. Loot "Corrupted Koalindl's Heart" (69931) from "A Corrupted Koalindl".
26. Spawns "A Corrupted Koalindl" (182150) in `nedaria` on event_fish_success.
27. Loot "Corrupted Koalindl's Heart" (69932) from "A Corrupted Koalindl".
28. qeynos2/"Enic Ruklin", hand "Corrupted Koalindl's Heart" (69929) + "Corrupted Koalindl's Heart" (69930) + "Corrupted Koalindl's Heart" (69931) + "Corrupted Koalindl's Heart" (69932). Sets `paladin_epic` to `4`.
29. dawnshroud/"Mikhal Young", say "Find Anything". Requires `paladin_epic` ==4. Gives "Drema's Locket" (69945).
30. letalis/"Drema Young", hand "Drema's Locket" (69945). Requires `paladin_epic` set. Requires `paladin_epic` >=4. Gives "Drema's Fingerbone" (69946).
31. dawnshroud/"Mikhal Young", hand "Drema's Fingerbone" (69946). Sets `paladin_epic` to `5`.
32. abysmal/"Lovine Lemise", say "Ingredients". Requires `paladin_epic` ==5. Gives "Lovine's Potion Bag" (69922).
33. No quest step gives Ra`Tuk Screambringer's Jaw (69921). The dump lists it in barindu.
34. Loot "Noc Fleshfeasters Tail" (69920) from "A Noc Fleshfeaster" in `riwwi`.
35. Loot "Mastruq Havocblade Blood" (69919) from "A Mastruq Havocblade" in `qinimi`.
36. Loot "Mastruq Havocblade Blood" (69919) from "A Mastruq Warfiend" in `qinimi`.
37. Loot "Potameid Seaweed Strands" (69918) from "An Entrapped Potameid" in `natimbi`.
38. Combine in "Lovine's Potion Bag" (69922): "Ra'Tuk Screambringer's Jaw" (69921), "Noc Fleshfeasters Tail" (69920), "Mastruq Havocblade Blood" (69919), "Potameid Seaweed Strands" (69918). Produces "Lovine's Potion Bag" (69923). The combine does not fail.
39. abysmal/"Lovine Lemise", hand "Lovine's Potion Bag" (69923). Sets `paladin_epic_reiya` to `1`.
40. Summon "Foldable Medicine Bag" (17770) by casting "Unfold Medicine Bag".
41. Common item: Fine Potion Vial (95846). Listed in 15 zones.
42. Common item: Robust Shadow Essence (96911). Listed in 5 zones.
43. Loot "Sage Leaf" (14215) from "a Di'zok Herbalist" in `chardok`.
44. Loot "Sage Leaf" (14215) from "a Sarnak Herb Collector" in `chardok`.
45. Loot "Sage Leaf" (14215) from "an Apprentice Herbalist" in `chardok`.
46. Loot "Valerian Root" (14230) from "a Di'zok Herbalist" in `chardok`.
47. Loot "Valerian Root" (14230) from "a Sarnak Herb Collector" in `chardok`.
48. Loot "Valerian Root" (14230) from "an Apprentice Herbalist" in `chardok`.
49. Common item: Woundwart (16526). Listed in 9 zones.
50. Combine in "Foldable Medicine Bag" (17770): "Fine Potion Vial" (95846), "Robust Shadow Essence" (96911), "Sage Leaf" (14215), "Valerian Root" (14230), "Woundwart" (16526). Produces "Mist of the Breathless" (96937). Requires Alchemy, trivial 224.
51. abysmal/"Reiya The Pained", hand "Mist of the Breathless" (96937). Requires `paladin_epic_reiya` ==1. Gives "Reiya's Soulstone" (69924).
52. Spawns "Shade of Reiya the Pained" (284104) in `ferubi` on enter.
53. Loot "Soulstone Shard" (69943) from "Shade of Reiya the Pained".
54. Loot "Soulstone Shard" (69944) from "Vuranish Xxuro" in `vxed`.
55. Combine in "Reiya's Soulstone" (69924): "Soulstone Shard" (69943), "Soulstone Shard" (69944). Produces "Reiya's Soulstone" (69942). The combine does not fail.
56. Loot "Tainted Darksteel Sword" (29000) from "Keeper of the Tombs" in `hole`.
57. freeporteast/"Peasant Woman", say "I Will Take It". Gives "Bucket of Water" (29008).
58. freportw/"Peasant Woman", say "I Will Take It". Gives "Bucket of Water" (29008).
59. freeporteast/"Joshua", hand "Bucket of Water" (29008). Gives "Bucket of Pure Water" (29009).
60. freportw/"Joshua", hand "Bucket of Water" (29008). Gives "Bucket of Pure Water" (29009).
61. erudnext/"Reklon Gnallen", hand "Tainted Darksteel Sword" (29000) + "Bucket of Pure Water" (29009). Gives "Gleaming Crested Sword" (29003).
62. Loot "Tainted Darksteel Breastplate" (29001) from "Thought Destroyer" in `hateplaneb`.
63. kaladimb/"Nella Stonebraids", say "Jark". Gives "Cold Plate of Beef and Bread" (29007).
64. kaladimb/"Nella Stonebraids", say "Dinner". Gives "Cold Plate of Beef and Bread" (29007).
65. kaladimb/"Jark", hand "Cold Plate of Beef and Bread" (29007). Gives "Pure Crystal" (29006).
66. erudnext/"Reklon Gnallen", hand "Tainted Darksteel Breastplate" (29001) + "Pure Crystal" (29006). Gives "Gleaming Crested Breastplate" (29004).
67. Loot "Tainted Darksteel Shield" (29002) from "Kirak Vil" in `nektulos`.
68. felwithea/"Elia The Pure", hand "Tainted Darksteel Shield" (29002). Gives "Gleaming Crested Shield" (29005).
69. erudnext/"Reklon Gnallen", hand "Gleaming Crested Sword" (29003) + "Gleaming Crested Breastplate" (29004) + "Gleaming Crested Shield" (29005). Gives "Mark of Atonement" (29010).
70. No quest step gives Drom's Champagne (13829). The dump lists it in freeporteast, freporte, highpasshold.
71. freeporteast/"Tykar Renlin", hand "Drom's Champagne" (13829) + "Drom's Champagne" (13829) + "Drom's Champagne" (13829) + "Drom's Champagne" (13829). Gives "Bunker Cell #1" (12196).
72. freporte/"Tykar Renlin", hand "Drom's Champagne" (13829) + "Drom's Champagne" (13829) + "Drom's Champagne" (13829) + "Drom's Champagne" (13829). Gives "Bunker Cell #1" (12196).
73. Summon "Black Diamond of Nightmares" (29990) by casting "Imbue Nightmare".
74. poknowledge/"Aid Grimel", say "Versed In The Art Of Smithing". Gives "Filthy Breastplate" (15984).
75. Combine in "Mixing Bowl" (17906): "Celestial Solvent" (9731), "Words of Acquisition (Beza)" (11866). Produces "Celestial Essence" (9650). Requires Baking, trivial 15. The combine does not fail.
76. Combine in "Mixing Bowl" (17906): "Celestial Solvent" (9731), "Words of Burnishing" (11862). Produces "Celestial Essence" (9650). Requires Baking, trivial 15. The combine does not fail.
77. 67 other recipes also produce Celestial Essence (9650).
78. Common item: Jar of Acid (22133). Listed in 15 zones.
79. Combine in Brew Barrel (19): "Celestial Essence" (9650), "Jar of Acid" (22133). Produces "Acid Wash" (15987). Requires Brewing, trivial 151.
80. Combine in Forge (17): "Filthy Breastplate" (15984), "Acid Wash" (15987). Produces "Cleansed Breastplate" (15998). Requires Blacksmithing, trivial 227.
81. Common item: Mortar and Pestle (17904). Listed in 12 zones.
82. No quest step gives Sandstorm Pearl (29909). The dump lists it in bothunder.
83. Combine in "Mortar and Pestle" (17904): "Sandstorm Pearl" (29909). Produces "Powdered Sandstorm Pearl" (29520) x4. Requires Make Poison, trivial 255.
84. Common item: Firing Sheet (16906). Listed in 34 zones.
85. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
86. qeynos/"Wolten Grafe", say "Crush The Undead". Gives "Box For Bones" (17941).
87. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `steamfont`.
88. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `tox`.
89. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `toxxulia`.
90. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
91. toxxulia/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
92. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). The combine does not fail.
93. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
94. qeynos2/"Phin Esrinap", say "Supplies". Gives "Message to Konem" (18921).
95. qeytoqrg/"Konem Matse", hand "Message to Konem" (18921). Gives "Grathin's Invoice" (18922).
96. qeynos2/"Phin Esrinap", hand "Grathin's Invoice" (18922). Gives "Water Flask" (13006).
97. Say "Tm Devrak Death" to rujd/"Rujd".
98. Spawns "spawn chest with Heavy Orcish Prison Key" (245241).
99. Loot "Pod of Water" (13044) from "spawn chest with Heavy Orcish Prison Key".
100. Say "Tm Dokorel Death" to rujd/"Rujd".
101. Say "Tm Velrek Death" to rujd/"Rujd".
102. Say "Researcher Death" to rujg/"Rujg".
103. Spawns "A Barrel" (260015).
104. Loot "Pod of Water" (13044) from "A Barrel".
105. 3 other loot steps also yield Pod of Water (13044).
106. Forage "Pod of Water" (13044) in `ruja`.
107. Forage "Pod of Water" (13044) in `uqua`.
108. Forage "Pod of Water" (13044) in `yxtta`.
109. Combine in Brew Barrel (19): "Bottle of Aged Bloodwine" (51163), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aged Bloodwine" (51164). Requires Brewing, trivial 255.
110. Combine in Brew Barrel (19): "Bottle of Aldo's Bitter Ale" (75805), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aldo's Bitter Ale" (75811). Requires Brewing, trivial 15.
111. 17 other recipes also produce Bottle (16598).
112. Combine in Brew Barrel (19): "Pod of Water" (13044), "Bottle" (16598). Produces "Water Flask" (13006). Requires Brewing, trivial 21.
113. Combine in Pottery Wheel (21): "Water Flask" (13006), "Block of Clay" (16901). Produces "Small Block of Clay" (16900) x3. Requires Pottery, trivial 21.
114. Combine in Pottery Wheel (21): "Small Block of Clay" (16900), "Water Flask" (13006). Produces "Block of Clay" (16901). Requires Pottery, trivial 21.
115. Combine in Pottery Wheel (21): "Water Flask" (13006), "Large Block of Clay" (16902). Produces "Block of Clay" (16901) x2. Requires Pottery, trivial 21.
116. Combine in Pottery Wheel (21): "Block of Clay" (16901), "Water Flask" (13006). Produces "Large Block of Clay" (16902). Requires Pottery, trivial 21.
117. Common item: Large Bowl Sketch (16963). Listed in 29 zones.
118. Combine in Pottery Wheel (21): "Large Block of Clay" (16902), "Water Flask" (13006), "Large Bowl Sketch" (16963). Produces "Unfired Mixing Bowl" (16930). Requires Pottery, trivial 128.
119. Combine in Kiln (22): "Firing Sheet" (16906), "Unfired Mixing Bowl" (16930). Produces "Mixing Bowl" (17906). Requires Pottery, trivial 15.
120. Combine in "Mixing Bowl" (17906): "Sandstorm Pearl" (29909). Produces "Powdered Sandstorm Pearl" (29520) x4. Requires Baking. The combine does not fail.
121. Spawns "a Koka'Vor chieftain" (210236) in `postorms` on event_signal.
122. Loot "Storm Rider Blood" (29526) from "a Koka'Vor chieftain".
123. Loot "Storm Rider Blood" (29526) from "A stormrider" in `bothunder`.
124. Loot "Storm Rider Blood" (29526) from "Dolsoj Warrebs" in `bazaar`.
125. Loot "Storm Rider Blood" (29526) from "a Koka'Vor krovian" in `postorms`.
126. Loot "Storm Rider Blood" (29526) from "a Koka'Vor senvar" in `postorms`.
127. No quest step gives Drop of Pure Rain (29904). The dump lists it in bothunder.
128. Combine in Brew Barrel (19): "Powdered Sandstorm Pearl" (29520), "Storm Rider Blood" (29526), "Drop of Pure Rain" (29904). Produces "Hurricane Temper" (29533). Requires Brewing, trivial 135.
129. Combine in Forge (17): "Cleansed Breastplate" (15998), "Hurricane Temper" (29533). Produces "Tempered Breastplate" (15999). Requires Blacksmithing, trivial 229.
130. Combine in Forge (17): "Black Diamond of Nightmares" (29990), "Tempered Breastplate" (15999). Produces "Imbued Breastplate" (15985). Requires Blacksmithing 220. Trivial at 275.
131. poknowledge/"Aid Grimel", hand "Imbued Breastplate" (15985). Gives "Hardened Leather Signet" (16249).
132. poknowledge/"Aid Grimel", say "Skill In Brewing". Gives "Portable Drink Barrel" (17179).
133. Common item: Snake Scales (13070). Listed in 56 zones.
134. Combine in "Portable Drink Barrel" (17179): "Water Flask" (13006), "Snake Scales" (13070), "Bottle" (16598). Produces "Bog Juice" (16581). Requires Brewing, trivial 21.
135. Common item: Spit (17947). Listed in 34 zones.
136. Common item: Fire Beetle Eye (10307). Listed in 24 zones.
137. Spawns "Sepsis Rat" (45113) in `qcat` on event_death.
138. Loot "Rat Ears" (13072) from "Sepsis Rat".
139. Kill steamfont/"Diseased Female Rat". Spawns "A Young Plague Rat" (56086).
140. Loot "Rat Ears" (13072) from "A Young Plague Rat".
141. Kill steamfontmts/"Diseased Female Rat". Spawns "A Young Plague Rat" (448036).
142. Combine in "Spit" (17947): "Fire Beetle Eye" (10307), "Rat Ears" (13072). Produces "Edible Goo" (13498). Requires Baking, trivial 21.
143. freeporteast/"A Prisoner", hand "Bunker Cell #1" (12196) + "Edible Goo" (13498) + "Bog Juice" (16581). Gives "H. K. 102" (12143).
144. freportw/"A Prisoner", hand "Bunker Cell #1" (12196) + "Edible Goo" (13498) + "Bog Juice" (16581). Gives "H. K. 102" (12143).
145. highkeep/"Assistant Kiolna", hand "H. K. 102" (12143). Gives "Sealed Note" (18936).
146. paw/"Brother Hayle", hand "Sealed Note" (18936). Gives "Note" (18937).
147. southkarana/"Brother Hayle", hand "Sealed Note" (18936). Gives "Note" (18937).
148. Kill freportw/"Sir Lucan D-Lere". Spawns "Sir Lucan D'Lere" (9147).
149. Loot "Testimony of Truth" (18827) from "Sir Lucan D'Lere".
150. Loot "Testimony of Truth" (18827) from "Sir Lucan D'Lere" in `freeporteast`.
151. freeportwest/"Valeron Dushire", hand "Testimony of Truth" (18827). Gives "Brilliant Sword of Faith" (13947).
152. freportn/"Valeron Dushire", hand "Testimony of Truth" (18827). Gives "Brilliant Sword of Faith" (13947).
153. Hand "Token of Bravery" (12144) + "Token of Generosity" (13865) to freeportwest/"Merko Quetalis". Spawns "spawns Guard Willia" (383270). Loot "Token of Truth" (13866) from "spawns Guard Willia".
154. Hand "Token of Bravery" (12144) + "Token of Generosity" (13865) to freportn/"Merko Quetalis". Spawns "spawns Guard Willia" (8110). Loot "Token of Truth" (13866) from "spawns Guard Willia".
155. Loot "Token of Truth" (13866) from "Guard Willia".
156. freeportwest/"Merko Quetalis", hand "Token of Truth" (13866). Gives "Testimony" (18828).
157. freportn/"Merko Quetalis", hand "Token of Truth" (13866). Gives "Testimony" (18828).
158. Loot "Glowing Sword Hilt" (12197) from "Xicotl" in `mistmoore`.
159. paw/"Brother Hayle", hand "Glowing Sword Hilt" (12197) + "Brilliant Sword of Faith" (13947) + "Testimony" (18828) + "Note" (18937). Gives "SoulFire" (5504).
160. southkarana/"Brother Hayle", hand "Glowing Sword Hilt" (12197) + "Brilliant Sword of Faith" (13947) + "Testimony" (18828) + "Note" (18937). Gives "SoulFire" (5504).
161. airplane/"Inte Akera", hand "SoulFire" (5504). Gives "Inte's First Blessing" (18033).
162. lavastorm/"Ruathey", say "Bag". Gives "Nobleman's Bag" (17878).
163. Common item: Ghoul's Heart (2410). Listed in 8 zones.
164. No quest step gives Amstaf's Scroll (2411). The dump lists it in highkeep.
165. No quest step gives Blade of Nobility (2412). The dump lists it in butcher.
166. Loot "Hilt of the Nobleman" (2413) from "Ekeros" in `najena`.
167. Loot "Hilt of the Nobleman" (2413) from "A Skeleton" in `najena`.
168. Combine in "Nobleman's Bag" (17878): "Ghoul's Heart" (2410), "Amstaf's Scroll" (2411), "Blade of Nobility" (2412), "Hilt of the Nobleman" (2413). Produces "Ghoulbane" (5403). The combine does not fail.
169. airplane/"Inte Akera", hand "Ghoulbane" (5403). Gives "Inte's Second Blessing" (18034).
170. Hand "Miragul's Phylactery" (19072) to everfrost/"Lich Of Miragul". Spawns "Spawn Miragul" (30094). Loot "Miragul's Head" (19073) from "Spawn Miragul".
171. Loot "Miragul's Head" (19073) from "Miragul".
172. Hand "Miragul's Phylactery" (19072) to everfrost/"Lich Of Miragul". Spawns "Spawn Miragul" (30094). Loot "Miragul's Robe" (1254) from "Spawn Miragul".
173. Loot "Miragul's Robe" (1254) from "Miragul".
174. airplane/"Inte Akera", hand "Miragul's Robe" (1254) + "Inte's First Blessing" (18033) + "Inte's Second Blessing" (18034) + "Miragul's Head" (19073). Gives "Fiery Avenger" (11050).
175. fearplane/"Irak Altil", hand "Fiery Avenger" (11050) + "Mark of Atonement" (29010). Gives "Fiery Defender" (10099).
176. povalor/"Baltron Werters", say "Couragebringer". Sets `pre_pal` to `1`.
177. Requires `pre_pal` unset; no setter establishes this state.
178. povalor/"Baltron Werters", say "Couragebringer". Requires `pre_pal` unset. Gives "Baltron's Solvent" (69901).
179. sro/"Gilfal", hand "Baltron's Solvent" (69901). Requires `pre_pal` ==1. Gives "Gilfal's Scabbard" (69902).
180. Spawns "Neffiken Lord Kelek-Vor" (210229) in `postorms` on event_signal.
181. Loot "Broken Sword Piece" (69903) from "Neffiken Lord Kelek-Vor".
182. Loot "Broken Sword Piece" (69903) from "Neffiken Lord of Kelek'Vor".
183. Say "Control Timer" to hateplaneb/"Maestro".
184. Spawns "Maestro of Rancor" (186111).
185. Loot "Broken Sword Piece" (69904) from "Maestro of Rancor".
186. **Broken:** no event trigger found for `hateplaneb/maestro#timer:popmaestro`.
187. Spawns "Maestro of Rancor" (186111) after `hateplaneb/maestro#timer:popmaestro`.
188. Loot "Broken Sword Piece" (69905) from "Kaniz Painbringer" in `potorment`.
189. sro/"Gilfal", hand "Baltron's Solvent" (69901). Sets `pre_pal` to `2`.
190. Ground spawn of "Rune of Xor" (69909) in `potranquility`.
191. Ground spawn of "Rune of Yirno" (69908) in `mistmoore`.
192. Ground spawn of "Rune of Zota" (69907) in `scarlet`.
193. Ground spawn of "Rune Wilun" (69910) in `gunthak`.
194. everfrost/"Rombus", hand "Rune of Zota" (69907) + "Rune of Yirno" (69908) + "Rune of Xor" (69909) + "Rune Wilun" (69910). Requires `pre_pal` ==2. Gives "Broken Sword Piece" (69906).
195. Combine in "Gilfal's Scabbard" (69902): "Broken Sword Piece" (69903), "Broken Sword Piece" (69904), "Broken Sword Piece" (69905), "Broken Sword Piece" (69906). Produces "Fractured Couragebringer" (69911). The combine does not fail.
196. sro/"Gilfal", hand "Fractured Couragebringer" (69911). Sets `pre_pal` to `4`.
197. everfrost/"Rombus", hand "Rune of Zota" (69907) + "Rune of Yirno" (69908) + "Rune of Xor" (69909) + "Rune Wilun" (69910). Sets `pre_pal` to `3`.
198. sro/"Gilfal", hand "Fractured Couragebringer" (69911). Requires `pre_pal` ==3. Gives "Fractured Couragebringer" (69912).
199. povalor/"Baltron Werters", hand "Fractured Couragebringer" (69912). Requires `pre_pal` ==4. Gives "Couragebringer" (69913).
200. hohonora/"Irak Altil", say "Hail". Sets `paladin_epic` to `6`.
201. Spawns "Durunal the Cursebearer" (300087) in `wallofslaughter` on enter.
202. Loot "Dark and Twisted Sword" (69971) from "Durunal the Cursebearer".
203. hohonora/"Irak Altil", hand "Dark and Twisted Sword" (69971). Requires `paladin_epic` ==6. Gives "Dark and Twisted Sword" (69972).

### "Redemption" (64031)

1. Say "Hail" to skyfire/"Dry Sapara".
2. Spawns "Rithnok the Tormented" (91193).
3. Loot "Rithnok's Soulstone" (69935) from "Rithnok the Tormented".
4. skyfire/"Dry Sapara", hand "Rithnok's Soulstone" (69935). Gives "Rithnok's Soulstone" (69936).
5. Ground spawn of "Soulstone Shard" (69937) in `draniksscar`.
6. Ground spawn of "Soulstone Shard" (69938) in `bloodfields`.
7. Ground spawn of "Soulstone Shard" (69939) in `causeway`.
8. Ground spawn of "Soulstone Shard" (69940) in `dranik`.
9. Combine in "Rithnok's Soulstone" (69936): "Soulstone Shard" (69937), "Soulstone Shard" (69938), "Soulstone Shard" (69939), "Soulstone Shard" (69940). Produces "Rithnok's Soulstone" (69941). The combine does not fail.
10. Hand "Enchanted Bone Powder" (69949) to letalis/"Drema Young". Spawns "Drema Young" (169128). Loot "Drema's Soulstone" (69928) from "Drema Young".
11. Loot "Drema's Soulstone" (69928) from "Drema Young".
12. Loot "Drema's Soulstone" (69928) from "Drema Young" in `letalis`.
13. Loot "Soulstone Shard" (69950) from "Coterie Corruptor" in `tenebrous`.
14. Say "Mujaki Death" to ponightmare/"Mujaki".
15. Spawns "Shade of Mujaki the Devourer" (204081).
16. Loot "Soulstone Shard" (69951) from "Shade of Mujaki the Devourer".
17. Combine in "Drema's Soulstone" (69928): "Soulstone Shard" (69950), "Soulstone Shard" (69951). Produces "Drema's Soulstone" (69952). The combine does not fail.
18. freporte/"Brunar Rankin", say "Hail". Sets `paladin_epic` to `3`.
19. global/"Global Player", combine recipe 19880. Sets `paladin_epic` to `8`.
20. Spawns "A Corrupted Koalindl" (69141) in `oot` on event_fish_success.
21. Loot "Corrupted Koalindl's Heart" (69929) from "A Corrupted Koalindl".
22. Spawns "A Corrupted Koalindl" (224432) in `gunthak` on event_fish_success.
23. Loot "Corrupted Koalindl's Heart" (69930) from "A Corrupted Koalindl".
24. Spawns "A Corrupted Koalindl" (93306) in `overthere` on event_fish_success.
25. Loot "Corrupted Koalindl's Heart" (69931) from "A Corrupted Koalindl".
26. Spawns "A Corrupted Koalindl" (182150) in `nedaria` on event_fish_success.
27. Loot "Corrupted Koalindl's Heart" (69932) from "A Corrupted Koalindl".
28. qeynos2/"Enic Ruklin", hand "Corrupted Koalindl's Heart" (69929) + "Corrupted Koalindl's Heart" (69930) + "Corrupted Koalindl's Heart" (69931) + "Corrupted Koalindl's Heart" (69932). Sets `paladin_epic` to `4`.
29. dawnshroud/"Mikhal Young", say "Find Anything". Requires `paladin_epic` ==4. Gives "Drema's Locket" (69945).
30. letalis/"Drema Young", hand "Drema's Locket" (69945). Requires `paladin_epic` set. Requires `paladin_epic` >=4. Gives "Drema's Fingerbone" (69946).
31. dawnshroud/"Mikhal Young", hand "Drema's Fingerbone" (69946). Sets `paladin_epic` to `5`.
32. abysmal/"Lovine Lemise", say "Ingredients". Requires `paladin_epic` ==5. Gives "Lovine's Potion Bag" (69922).
33. No quest step gives Ra`Tuk Screambringer's Jaw (69921). The dump lists it in barindu.
34. Loot "Noc Fleshfeasters Tail" (69920) from "A Noc Fleshfeaster" in `riwwi`.
35. Loot "Mastruq Havocblade Blood" (69919) from "A Mastruq Havocblade" in `qinimi`.
36. Loot "Mastruq Havocblade Blood" (69919) from "A Mastruq Warfiend" in `qinimi`.
37. Loot "Potameid Seaweed Strands" (69918) from "An Entrapped Potameid" in `natimbi`.
38. Combine in "Lovine's Potion Bag" (69922): "Ra'Tuk Screambringer's Jaw" (69921), "Noc Fleshfeasters Tail" (69920), "Mastruq Havocblade Blood" (69919), "Potameid Seaweed Strands" (69918). Produces "Lovine's Potion Bag" (69923). The combine does not fail.
39. abysmal/"Lovine Lemise", hand "Lovine's Potion Bag" (69923). Sets `paladin_epic_reiya` to `1`.
40. Summon "Foldable Medicine Bag" (17770) by casting "Unfold Medicine Bag".
41. Common item: Fine Potion Vial (95846). Listed in 15 zones.
42. Common item: Robust Shadow Essence (96911). Listed in 5 zones.
43. Loot "Sage Leaf" (14215) from "a Di'zok Herbalist" in `chardok`.
44. Loot "Sage Leaf" (14215) from "a Sarnak Herb Collector" in `chardok`.
45. Loot "Sage Leaf" (14215) from "an Apprentice Herbalist" in `chardok`.
46. Loot "Valerian Root" (14230) from "a Di'zok Herbalist" in `chardok`.
47. Loot "Valerian Root" (14230) from "a Sarnak Herb Collector" in `chardok`.
48. Loot "Valerian Root" (14230) from "an Apprentice Herbalist" in `chardok`.
49. Common item: Woundwart (16526). Listed in 9 zones.
50. Combine in "Foldable Medicine Bag" (17770): "Fine Potion Vial" (95846), "Robust Shadow Essence" (96911), "Sage Leaf" (14215), "Valerian Root" (14230), "Woundwart" (16526). Produces "Mist of the Breathless" (96937). Requires Alchemy, trivial 224.
51. abysmal/"Reiya The Pained", hand "Mist of the Breathless" (96937). Requires `paladin_epic_reiya` ==1. Gives "Reiya's Soulstone" (69924).
52. Spawns "Shade of Reiya the Pained" (284104) in `ferubi` on enter.
53. Loot "Soulstone Shard" (69943) from "Shade of Reiya the Pained".
54. Loot "Soulstone Shard" (69944) from "Vuranish Xxuro" in `vxed`.
55. Combine in "Reiya's Soulstone" (69924): "Soulstone Shard" (69943), "Soulstone Shard" (69944). Produces "Reiya's Soulstone" (69942). The combine does not fail.
56. Loot "Tainted Darksteel Sword" (29000) from "Keeper of the Tombs" in `hole`.
57. freeporteast/"Peasant Woman", say "I Will Take It". Gives "Bucket of Water" (29008).
58. freportw/"Peasant Woman", say "I Will Take It". Gives "Bucket of Water" (29008).
59. freeporteast/"Joshua", hand "Bucket of Water" (29008). Gives "Bucket of Pure Water" (29009).
60. freportw/"Joshua", hand "Bucket of Water" (29008). Gives "Bucket of Pure Water" (29009).
61. erudnext/"Reklon Gnallen", hand "Tainted Darksteel Sword" (29000) + "Bucket of Pure Water" (29009). Gives "Gleaming Crested Sword" (29003).
62. Loot "Tainted Darksteel Breastplate" (29001) from "Thought Destroyer" in `hateplaneb`.
63. kaladimb/"Nella Stonebraids", say "Jark". Gives "Cold Plate of Beef and Bread" (29007).
64. kaladimb/"Nella Stonebraids", say "Dinner". Gives "Cold Plate of Beef and Bread" (29007).
65. kaladimb/"Jark", hand "Cold Plate of Beef and Bread" (29007). Gives "Pure Crystal" (29006).
66. erudnext/"Reklon Gnallen", hand "Tainted Darksteel Breastplate" (29001) + "Pure Crystal" (29006). Gives "Gleaming Crested Breastplate" (29004).
67. Loot "Tainted Darksteel Shield" (29002) from "Kirak Vil" in `nektulos`.
68. felwithea/"Elia The Pure", hand "Tainted Darksteel Shield" (29002). Gives "Gleaming Crested Shield" (29005).
69. erudnext/"Reklon Gnallen", hand "Gleaming Crested Sword" (29003) + "Gleaming Crested Breastplate" (29004) + "Gleaming Crested Shield" (29005). Gives "Mark of Atonement" (29010).
70. No quest step gives Drom's Champagne (13829). The dump lists it in freeporteast, freporte, highpasshold.
71. freeporteast/"Tykar Renlin", hand "Drom's Champagne" (13829) + "Drom's Champagne" (13829) + "Drom's Champagne" (13829) + "Drom's Champagne" (13829). Gives "Bunker Cell #1" (12196).
72. freporte/"Tykar Renlin", hand "Drom's Champagne" (13829) + "Drom's Champagne" (13829) + "Drom's Champagne" (13829) + "Drom's Champagne" (13829). Gives "Bunker Cell #1" (12196).
73. Summon "Black Diamond of Nightmares" (29990) by casting "Imbue Nightmare".
74. poknowledge/"Aid Grimel", say "Versed In The Art Of Smithing". Gives "Filthy Breastplate" (15984).
75. Combine in "Mixing Bowl" (17906): "Celestial Solvent" (9731), "Words of Acquisition (Beza)" (11866). Produces "Celestial Essence" (9650). Requires Baking, trivial 15. The combine does not fail.
76. Combine in "Mixing Bowl" (17906): "Celestial Solvent" (9731), "Words of Burnishing" (11862). Produces "Celestial Essence" (9650). Requires Baking, trivial 15. The combine does not fail.
77. 67 other recipes also produce Celestial Essence (9650).
78. Common item: Jar of Acid (22133). Listed in 15 zones.
79. Combine in Brew Barrel (19): "Celestial Essence" (9650), "Jar of Acid" (22133). Produces "Acid Wash" (15987). Requires Brewing, trivial 151.
80. Combine in Forge (17): "Filthy Breastplate" (15984), "Acid Wash" (15987). Produces "Cleansed Breastplate" (15998). Requires Blacksmithing, trivial 227.
81. Common item: Mortar and Pestle (17904). Listed in 12 zones.
82. No quest step gives Sandstorm Pearl (29909). The dump lists it in bothunder.
83. Combine in "Mortar and Pestle" (17904): "Sandstorm Pearl" (29909). Produces "Powdered Sandstorm Pearl" (29520) x4. Requires Make Poison, trivial 255.
84. Common item: Firing Sheet (16906). Listed in 34 zones.
85. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
86. qeynos/"Wolten Grafe", say "Crush The Undead". Gives "Box For Bones" (17941).
87. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `steamfont`.
88. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `tox`.
89. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `toxxulia`.
90. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
91. toxxulia/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
92. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). The combine does not fail.
93. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
94. qeynos2/"Phin Esrinap", say "Supplies". Gives "Message to Konem" (18921).
95. qeytoqrg/"Konem Matse", hand "Message to Konem" (18921). Gives "Grathin's Invoice" (18922).
96. qeynos2/"Phin Esrinap", hand "Grathin's Invoice" (18922). Gives "Water Flask" (13006).
97. Say "Tm Devrak Death" to rujd/"Rujd".
98. Spawns "spawn chest with Heavy Orcish Prison Key" (245241).
99. Loot "Pod of Water" (13044) from "spawn chest with Heavy Orcish Prison Key".
100. Say "Tm Dokorel Death" to rujd/"Rujd".
101. Say "Tm Velrek Death" to rujd/"Rujd".
102. Say "Researcher Death" to rujg/"Rujg".
103. Spawns "A Barrel" (260015).
104. Loot "Pod of Water" (13044) from "A Barrel".
105. 3 other loot steps also yield Pod of Water (13044).
106. Forage "Pod of Water" (13044) in `ruja`.
107. Forage "Pod of Water" (13044) in `uqua`.
108. Forage "Pod of Water" (13044) in `yxtta`.
109. Combine in Brew Barrel (19): "Bottle of Aged Bloodwine" (51163), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aged Bloodwine" (51164). Requires Brewing, trivial 255.
110. Combine in Brew Barrel (19): "Bottle of Aldo's Bitter Ale" (75805), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aldo's Bitter Ale" (75811). Requires Brewing, trivial 15.
111. 17 other recipes also produce Bottle (16598).
112. Combine in Brew Barrel (19): "Pod of Water" (13044), "Bottle" (16598). Produces "Water Flask" (13006). Requires Brewing, trivial 21.
113. Combine in Pottery Wheel (21): "Water Flask" (13006), "Block of Clay" (16901). Produces "Small Block of Clay" (16900) x3. Requires Pottery, trivial 21.
114. Combine in Pottery Wheel (21): "Small Block of Clay" (16900), "Water Flask" (13006). Produces "Block of Clay" (16901). Requires Pottery, trivial 21.
115. Combine in Pottery Wheel (21): "Water Flask" (13006), "Large Block of Clay" (16902). Produces "Block of Clay" (16901) x2. Requires Pottery, trivial 21.
116. Combine in Pottery Wheel (21): "Block of Clay" (16901), "Water Flask" (13006). Produces "Large Block of Clay" (16902). Requires Pottery, trivial 21.
117. Common item: Large Bowl Sketch (16963). Listed in 29 zones.
118. Combine in Pottery Wheel (21): "Large Block of Clay" (16902), "Water Flask" (13006), "Large Bowl Sketch" (16963). Produces "Unfired Mixing Bowl" (16930). Requires Pottery, trivial 128.
119. Combine in Kiln (22): "Firing Sheet" (16906), "Unfired Mixing Bowl" (16930). Produces "Mixing Bowl" (17906). Requires Pottery, trivial 15.
120. Combine in "Mixing Bowl" (17906): "Sandstorm Pearl" (29909). Produces "Powdered Sandstorm Pearl" (29520) x4. Requires Baking. The combine does not fail.
121. Spawns "a Koka'Vor chieftain" (210236) in `postorms` on event_signal.
122. Loot "Storm Rider Blood" (29526) from "a Koka'Vor chieftain".
123. Loot "Storm Rider Blood" (29526) from "A stormrider" in `bothunder`.
124. Loot "Storm Rider Blood" (29526) from "Dolsoj Warrebs" in `bazaar`.
125. Loot "Storm Rider Blood" (29526) from "a Koka'Vor krovian" in `postorms`.
126. Loot "Storm Rider Blood" (29526) from "a Koka'Vor senvar" in `postorms`.
127. No quest step gives Drop of Pure Rain (29904). The dump lists it in bothunder.
128. Combine in Brew Barrel (19): "Powdered Sandstorm Pearl" (29520), "Storm Rider Blood" (29526), "Drop of Pure Rain" (29904). Produces "Hurricane Temper" (29533). Requires Brewing, trivial 135.
129. Combine in Forge (17): "Cleansed Breastplate" (15998), "Hurricane Temper" (29533). Produces "Tempered Breastplate" (15999). Requires Blacksmithing, trivial 229.
130. Combine in Forge (17): "Black Diamond of Nightmares" (29990), "Tempered Breastplate" (15999). Produces "Imbued Breastplate" (15985). Requires Blacksmithing 220. Trivial at 275.
131. poknowledge/"Aid Grimel", hand "Imbued Breastplate" (15985). Gives "Hardened Leather Signet" (16249).
132. poknowledge/"Aid Grimel", say "Skill In Brewing". Gives "Portable Drink Barrel" (17179).
133. Common item: Snake Scales (13070). Listed in 56 zones.
134. Combine in "Portable Drink Barrel" (17179): "Water Flask" (13006), "Snake Scales" (13070), "Bottle" (16598). Produces "Bog Juice" (16581). Requires Brewing, trivial 21.
135. Common item: Spit (17947). Listed in 34 zones.
136. Common item: Fire Beetle Eye (10307). Listed in 24 zones.
137. Spawns "Sepsis Rat" (45113) in `qcat` on event_death.
138. Loot "Rat Ears" (13072) from "Sepsis Rat".
139. Kill steamfont/"Diseased Female Rat". Spawns "A Young Plague Rat" (56086).
140. Loot "Rat Ears" (13072) from "A Young Plague Rat".
141. Kill steamfontmts/"Diseased Female Rat". Spawns "A Young Plague Rat" (448036).
142. Combine in "Spit" (17947): "Fire Beetle Eye" (10307), "Rat Ears" (13072). Produces "Edible Goo" (13498). Requires Baking, trivial 21.
143. freeporteast/"A Prisoner", hand "Bunker Cell #1" (12196) + "Edible Goo" (13498) + "Bog Juice" (16581). Gives "H. K. 102" (12143).
144. freportw/"A Prisoner", hand "Bunker Cell #1" (12196) + "Edible Goo" (13498) + "Bog Juice" (16581). Gives "H. K. 102" (12143).
145. highkeep/"Assistant Kiolna", hand "H. K. 102" (12143). Gives "Sealed Note" (18936).
146. paw/"Brother Hayle", hand "Sealed Note" (18936). Gives "Note" (18937).
147. southkarana/"Brother Hayle", hand "Sealed Note" (18936). Gives "Note" (18937).
148. Kill freportw/"Sir Lucan D-Lere". Spawns "Sir Lucan D'Lere" (9147).
149. Loot "Testimony of Truth" (18827) from "Sir Lucan D'Lere".
150. Loot "Testimony of Truth" (18827) from "Sir Lucan D'Lere" in `freeporteast`.
151. freeportwest/"Valeron Dushire", hand "Testimony of Truth" (18827). Gives "Brilliant Sword of Faith" (13947).
152. freportn/"Valeron Dushire", hand "Testimony of Truth" (18827). Gives "Brilliant Sword of Faith" (13947).
153. Hand "Token of Bravery" (12144) + "Token of Generosity" (13865) to freeportwest/"Merko Quetalis". Spawns "spawns Guard Willia" (383270). Loot "Token of Truth" (13866) from "spawns Guard Willia".
154. Hand "Token of Bravery" (12144) + "Token of Generosity" (13865) to freportn/"Merko Quetalis". Spawns "spawns Guard Willia" (8110). Loot "Token of Truth" (13866) from "spawns Guard Willia".
155. Loot "Token of Truth" (13866) from "Guard Willia".
156. freeportwest/"Merko Quetalis", hand "Token of Truth" (13866). Gives "Testimony" (18828).
157. freportn/"Merko Quetalis", hand "Token of Truth" (13866). Gives "Testimony" (18828).
158. Loot "Glowing Sword Hilt" (12197) from "Xicotl" in `mistmoore`.
159. paw/"Brother Hayle", hand "Glowing Sword Hilt" (12197) + "Brilliant Sword of Faith" (13947) + "Testimony" (18828) + "Note" (18937). Gives "SoulFire" (5504).
160. southkarana/"Brother Hayle", hand "Glowing Sword Hilt" (12197) + "Brilliant Sword of Faith" (13947) + "Testimony" (18828) + "Note" (18937). Gives "SoulFire" (5504).
161. airplane/"Inte Akera", hand "SoulFire" (5504). Gives "Inte's First Blessing" (18033).
162. lavastorm/"Ruathey", say "Bag". Gives "Nobleman's Bag" (17878).
163. Common item: Ghoul's Heart (2410). Listed in 8 zones.
164. No quest step gives Amstaf's Scroll (2411). The dump lists it in highkeep.
165. No quest step gives Blade of Nobility (2412). The dump lists it in butcher.
166. Loot "Hilt of the Nobleman" (2413) from "Ekeros" in `najena`.
167. Loot "Hilt of the Nobleman" (2413) from "A Skeleton" in `najena`.
168. Combine in "Nobleman's Bag" (17878): "Ghoul's Heart" (2410), "Amstaf's Scroll" (2411), "Blade of Nobility" (2412), "Hilt of the Nobleman" (2413). Produces "Ghoulbane" (5403). The combine does not fail.
169. airplane/"Inte Akera", hand "Ghoulbane" (5403). Gives "Inte's Second Blessing" (18034).
170. Hand "Miragul's Phylactery" (19072) to everfrost/"Lich Of Miragul". Spawns "Spawn Miragul" (30094). Loot "Miragul's Head" (19073) from "Spawn Miragul".
171. Loot "Miragul's Head" (19073) from "Miragul".
172. Hand "Miragul's Phylactery" (19072) to everfrost/"Lich Of Miragul". Spawns "Spawn Miragul" (30094). Loot "Miragul's Robe" (1254) from "Spawn Miragul".
173. Loot "Miragul's Robe" (1254) from "Miragul".
174. airplane/"Inte Akera", hand "Miragul's Robe" (1254) + "Inte's First Blessing" (18033) + "Inte's Second Blessing" (18034) + "Miragul's Head" (19073). Gives "Fiery Avenger" (11050).
175. fearplane/"Irak Altil", hand "Fiery Avenger" (11050) + "Mark of Atonement" (29010). Gives "Fiery Defender" (10099).
176. povalor/"Baltron Werters", say "Couragebringer". Sets `pre_pal` to `1`.
177. Requires `pre_pal` unset; no setter establishes this state.
178. povalor/"Baltron Werters", say "Couragebringer". Requires `pre_pal` unset. Gives "Baltron's Solvent" (69901).
179. sro/"Gilfal", hand "Baltron's Solvent" (69901). Requires `pre_pal` ==1. Gives "Gilfal's Scabbard" (69902).
180. Spawns "Neffiken Lord Kelek-Vor" (210229) in `postorms` on event_signal.
181. Loot "Broken Sword Piece" (69903) from "Neffiken Lord Kelek-Vor".
182. Loot "Broken Sword Piece" (69903) from "Neffiken Lord of Kelek'Vor".
183. Say "Control Timer" to hateplaneb/"Maestro".
184. Spawns "Maestro of Rancor" (186111).
185. Loot "Broken Sword Piece" (69904) from "Maestro of Rancor".
186. **Broken:** no event trigger found for `hateplaneb/maestro#timer:popmaestro`.
187. Spawns "Maestro of Rancor" (186111) after `hateplaneb/maestro#timer:popmaestro`.
188. Loot "Broken Sword Piece" (69905) from "Kaniz Painbringer" in `potorment`.
189. sro/"Gilfal", hand "Baltron's Solvent" (69901). Sets `pre_pal` to `2`.
190. Ground spawn of "Rune of Xor" (69909) in `potranquility`.
191. Ground spawn of "Rune of Yirno" (69908) in `mistmoore`.
192. Ground spawn of "Rune of Zota" (69907) in `scarlet`.
193. Ground spawn of "Rune Wilun" (69910) in `gunthak`.
194. everfrost/"Rombus", hand "Rune of Zota" (69907) + "Rune of Yirno" (69908) + "Rune of Xor" (69909) + "Rune Wilun" (69910). Requires `pre_pal` ==2. Gives "Broken Sword Piece" (69906).
195. Combine in "Gilfal's Scabbard" (69902): "Broken Sword Piece" (69903), "Broken Sword Piece" (69904), "Broken Sword Piece" (69905), "Broken Sword Piece" (69906). Produces "Fractured Couragebringer" (69911). The combine does not fail.
196. sro/"Gilfal", hand "Fractured Couragebringer" (69911). Sets `pre_pal` to `4`.
197. everfrost/"Rombus", hand "Rune of Zota" (69907) + "Rune of Yirno" (69908) + "Rune of Xor" (69909) + "Rune Wilun" (69910). Sets `pre_pal` to `3`.
198. sro/"Gilfal", hand "Fractured Couragebringer" (69911). Requires `pre_pal` ==3. Gives "Fractured Couragebringer" (69912).
199. povalor/"Baltron Werters", hand "Fractured Couragebringer" (69912). Requires `pre_pal` ==4. Gives "Couragebringer" (69913).
200. hohonora/"Irak Altil", say "Hail". Sets `paladin_epic` to `6`.
201. Spawns "Durunal the Cursebearer" (300087) in `wallofslaughter` on enter.
202. Loot "Dark and Twisted Sword" (69971) from "Durunal the Cursebearer".
203. hohonora/"Irak Altil", hand "Dark and Twisted Sword" (69971). Requires `paladin_epic` ==6. Gives "Dark and Twisted Sword" (69972).
204. Loot "Redis' Soulstone" (69983) from "Shade of Redis Linrok" in `dranikcatacombsa`.
205. Combine in "Dark and Twisted Sword" (69972): "Rithnok's Soulstone" (69941), "Drema's Soulstone" (69952), "Reiya's Soulstone" (69942), "Redis' Soulstone" (69983). Produces "Redemption" (64031). The combine does not fail.

### "Token of Compassion" (69953)

1. qeynos2/"Camlend Serbold", say "Gem". Gives "Unfilled Set of Prayer Beads" (69968).
2. rivervale/"Kaya Cloudfoot", say "Different About It". Gives "Note from Kaya" (69970).
3. rivervale/"Deputy Cheel", hand "Note from Kaya" (69970). Gives "Rivervale Prayer Bead" (69967).
4. **Broken:** nothing in the graph gives, loots, spawns, or combines Ak`anon Prayer Bead (69966).
5. Say "Hail" to skyfire/"Dry Sapara".
6. Spawns "Rithnok the Tormented" (91193).
7. Loot "Rithnok's Soulstone" (69935) from "Rithnok the Tormented".
8. skyfire/"Dry Sapara", hand "Rithnok's Soulstone" (69935). Gives "Rithnok's Soulstone" (69936).
9. Ground spawn of "Soulstone Shard" (69937) in `draniksscar`.
10. Ground spawn of "Soulstone Shard" (69938) in `bloodfields`.
11. Ground spawn of "Soulstone Shard" (69939) in `causeway`.
12. Ground spawn of "Soulstone Shard" (69940) in `dranik`.
13. Combine in "Rithnok's Soulstone" (69936): "Soulstone Shard" (69937), "Soulstone Shard" (69938), "Soulstone Shard" (69939), "Soulstone Shard" (69940). Produces "Rithnok's Soulstone" (69941). The combine does not fail.
14. Hand "Enchanted Bone Powder" (69949) to letalis/"Drema Young". Spawns "Drema Young" (169128). Loot "Drema's Soulstone" (69928) from "Drema Young".
15. Loot "Drema's Soulstone" (69928) from "Drema Young".
16. Loot "Drema's Soulstone" (69928) from "Drema Young" in `letalis`.
17. Loot "Soulstone Shard" (69950) from "Coterie Corruptor" in `tenebrous`.
18. Say "Mujaki Death" to ponightmare/"Mujaki".
19. Spawns "Shade of Mujaki the Devourer" (204081).
20. Loot "Soulstone Shard" (69951) from "Shade of Mujaki the Devourer".
21. Combine in "Drema's Soulstone" (69928): "Soulstone Shard" (69950), "Soulstone Shard" (69951). Produces "Drema's Soulstone" (69952). The combine does not fail.
22. freporte/"Brunar Rankin", say "Hail". Sets `paladin_epic` to `3`.
23. global/"Global Player", combine recipe 19880. Sets `paladin_epic` to `8`.
24. Spawns "A Corrupted Koalindl" (69141) in `oot` on event_fish_success.
25. Loot "Corrupted Koalindl's Heart" (69929) from "A Corrupted Koalindl".
26. Spawns "A Corrupted Koalindl" (224432) in `gunthak` on event_fish_success.
27. Loot "Corrupted Koalindl's Heart" (69930) from "A Corrupted Koalindl".
28. Spawns "A Corrupted Koalindl" (93306) in `overthere` on event_fish_success.
29. Loot "Corrupted Koalindl's Heart" (69931) from "A Corrupted Koalindl".
30. Spawns "A Corrupted Koalindl" (182150) in `nedaria` on event_fish_success.
31. Loot "Corrupted Koalindl's Heart" (69932) from "A Corrupted Koalindl".
32. qeynos2/"Enic Ruklin", hand "Corrupted Koalindl's Heart" (69929) + "Corrupted Koalindl's Heart" (69930) + "Corrupted Koalindl's Heart" (69931) + "Corrupted Koalindl's Heart" (69932). Sets `paladin_epic` to `4`.
33. dawnshroud/"Mikhal Young", say "Find Anything". Requires `paladin_epic` ==4. Gives "Drema's Locket" (69945).
34. letalis/"Drema Young", hand "Drema's Locket" (69945). Requires `paladin_epic` set. Requires `paladin_epic` >=4. Gives "Drema's Fingerbone" (69946).
35. dawnshroud/"Mikhal Young", hand "Drema's Fingerbone" (69946). Sets `paladin_epic` to `5`.
36. abysmal/"Lovine Lemise", say "Ingredients". Requires `paladin_epic` ==5. Gives "Lovine's Potion Bag" (69922).
37. No quest step gives Ra`Tuk Screambringer's Jaw (69921). The dump lists it in barindu.
38. Loot "Noc Fleshfeasters Tail" (69920) from "A Noc Fleshfeaster" in `riwwi`.
39. Loot "Mastruq Havocblade Blood" (69919) from "A Mastruq Havocblade" in `qinimi`.
40. Loot "Mastruq Havocblade Blood" (69919) from "A Mastruq Warfiend" in `qinimi`.
41. Loot "Potameid Seaweed Strands" (69918) from "An Entrapped Potameid" in `natimbi`.
42. Combine in "Lovine's Potion Bag" (69922): "Ra'Tuk Screambringer's Jaw" (69921), "Noc Fleshfeasters Tail" (69920), "Mastruq Havocblade Blood" (69919), "Potameid Seaweed Strands" (69918). Produces "Lovine's Potion Bag" (69923). The combine does not fail.
43. abysmal/"Lovine Lemise", hand "Lovine's Potion Bag" (69923). Sets `paladin_epic_reiya` to `1`.
44. Summon "Foldable Medicine Bag" (17770) by casting "Unfold Medicine Bag".
45. Common item: Fine Potion Vial (95846). Listed in 15 zones.
46. Common item: Robust Shadow Essence (96911). Listed in 5 zones.
47. Loot "Sage Leaf" (14215) from "a Di'zok Herbalist" in `chardok`.
48. Loot "Sage Leaf" (14215) from "a Sarnak Herb Collector" in `chardok`.
49. Loot "Sage Leaf" (14215) from "an Apprentice Herbalist" in `chardok`.
50. Loot "Valerian Root" (14230) from "a Di'zok Herbalist" in `chardok`.
51. Loot "Valerian Root" (14230) from "a Sarnak Herb Collector" in `chardok`.
52. Loot "Valerian Root" (14230) from "an Apprentice Herbalist" in `chardok`.
53. Common item: Woundwart (16526). Listed in 9 zones.
54. Combine in "Foldable Medicine Bag" (17770): "Fine Potion Vial" (95846), "Robust Shadow Essence" (96911), "Sage Leaf" (14215), "Valerian Root" (14230), "Woundwart" (16526). Produces "Mist of the Breathless" (96937). Requires Alchemy, trivial 224.
55. abysmal/"Reiya The Pained", hand "Mist of the Breathless" (96937). Requires `paladin_epic_reiya` ==1. Gives "Reiya's Soulstone" (69924).
56. Spawns "Shade of Reiya the Pained" (284104) in `ferubi` on enter.
57. Loot "Soulstone Shard" (69943) from "Shade of Reiya the Pained".
58. Loot "Soulstone Shard" (69944) from "Vuranish Xxuro" in `vxed`.
59. Combine in "Reiya's Soulstone" (69924): "Soulstone Shard" (69943), "Soulstone Shard" (69944). Produces "Reiya's Soulstone" (69942). The combine does not fail.
60. Loot "Tainted Darksteel Sword" (29000) from "Keeper of the Tombs" in `hole`.
61. freeporteast/"Peasant Woman", say "I Will Take It". Gives "Bucket of Water" (29008).
62. freportw/"Peasant Woman", say "I Will Take It". Gives "Bucket of Water" (29008).
63. freeporteast/"Joshua", hand "Bucket of Water" (29008). Gives "Bucket of Pure Water" (29009).
64. freportw/"Joshua", hand "Bucket of Water" (29008). Gives "Bucket of Pure Water" (29009).
65. erudnext/"Reklon Gnallen", hand "Tainted Darksteel Sword" (29000) + "Bucket of Pure Water" (29009). Gives "Gleaming Crested Sword" (29003).
66. Loot "Tainted Darksteel Breastplate" (29001) from "Thought Destroyer" in `hateplaneb`.
67. kaladimb/"Nella Stonebraids", say "Jark". Gives "Cold Plate of Beef and Bread" (29007).
68. kaladimb/"Nella Stonebraids", say "Dinner". Gives "Cold Plate of Beef and Bread" (29007).
69. kaladimb/"Jark", hand "Cold Plate of Beef and Bread" (29007). Gives "Pure Crystal" (29006).
70. erudnext/"Reklon Gnallen", hand "Tainted Darksteel Breastplate" (29001) + "Pure Crystal" (29006). Gives "Gleaming Crested Breastplate" (29004).
71. Loot "Tainted Darksteel Shield" (29002) from "Kirak Vil" in `nektulos`.
72. felwithea/"Elia The Pure", hand "Tainted Darksteel Shield" (29002). Gives "Gleaming Crested Shield" (29005).
73. erudnext/"Reklon Gnallen", hand "Gleaming Crested Sword" (29003) + "Gleaming Crested Breastplate" (29004) + "Gleaming Crested Shield" (29005). Gives "Mark of Atonement" (29010).
74. No quest step gives Drom's Champagne (13829). The dump lists it in freeporteast, freporte, highpasshold.
75. freeporteast/"Tykar Renlin", hand "Drom's Champagne" (13829) + "Drom's Champagne" (13829) + "Drom's Champagne" (13829) + "Drom's Champagne" (13829). Gives "Bunker Cell #1" (12196).
76. freporte/"Tykar Renlin", hand "Drom's Champagne" (13829) + "Drom's Champagne" (13829) + "Drom's Champagne" (13829) + "Drom's Champagne" (13829). Gives "Bunker Cell #1" (12196).
77. Summon "Black Diamond of Nightmares" (29990) by casting "Imbue Nightmare".
78. poknowledge/"Aid Grimel", say "Versed In The Art Of Smithing". Gives "Filthy Breastplate" (15984).
79. Combine in "Mixing Bowl" (17906): "Celestial Solvent" (9731), "Words of Acquisition (Beza)" (11866). Produces "Celestial Essence" (9650). Requires Baking, trivial 15. The combine does not fail.
80. Combine in "Mixing Bowl" (17906): "Celestial Solvent" (9731), "Words of Burnishing" (11862). Produces "Celestial Essence" (9650). Requires Baking, trivial 15. The combine does not fail.
81. 67 other recipes also produce Celestial Essence (9650).
82. Common item: Jar of Acid (22133). Listed in 15 zones.
83. Combine in Brew Barrel (19): "Celestial Essence" (9650), "Jar of Acid" (22133). Produces "Acid Wash" (15987). Requires Brewing, trivial 151.
84. Combine in Forge (17): "Filthy Breastplate" (15984), "Acid Wash" (15987). Produces "Cleansed Breastplate" (15998). Requires Blacksmithing, trivial 227.
85. Common item: Mortar and Pestle (17904). Listed in 12 zones.
86. No quest step gives Sandstorm Pearl (29909). The dump lists it in bothunder.
87. Combine in "Mortar and Pestle" (17904): "Sandstorm Pearl" (29909). Produces "Powdered Sandstorm Pearl" (29520) x4. Requires Make Poison, trivial 255.
88. Common item: Firing Sheet (16906). Listed in 34 zones.
89. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
90. qeynos/"Wolten Grafe", say "Crush The Undead". Gives "Box For Bones" (17941).
91. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `steamfont`.
92. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `tox`.
93. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `toxxulia`.
94. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
95. toxxulia/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
96. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). The combine does not fail.
97. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
98. qeynos2/"Phin Esrinap", say "Supplies". Gives "Message to Konem" (18921).
99. qeytoqrg/"Konem Matse", hand "Message to Konem" (18921). Gives "Grathin's Invoice" (18922).
100. qeynos2/"Phin Esrinap", hand "Grathin's Invoice" (18922). Gives "Water Flask" (13006).
101. Say "Tm Devrak Death" to rujd/"Rujd".
102. Spawns "spawn chest with Heavy Orcish Prison Key" (245241).
103. Loot "Pod of Water" (13044) from "spawn chest with Heavy Orcish Prison Key".
104. Say "Tm Dokorel Death" to rujd/"Rujd".
105. Say "Tm Velrek Death" to rujd/"Rujd".
106. Say "Researcher Death" to rujg/"Rujg".
107. Spawns "A Barrel" (260015).
108. Loot "Pod of Water" (13044) from "A Barrel".
109. 3 other loot steps also yield Pod of Water (13044).
110. Forage "Pod of Water" (13044) in `ruja`.
111. Forage "Pod of Water" (13044) in `uqua`.
112. Forage "Pod of Water" (13044) in `yxtta`.
113. Combine in Brew Barrel (19): "Bottle of Aged Bloodwine" (51163), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aged Bloodwine" (51164). Requires Brewing, trivial 255.
114. Combine in Brew Barrel (19): "Bottle of Aldo's Bitter Ale" (75805), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aldo's Bitter Ale" (75811). Requires Brewing, trivial 15.
115. 17 other recipes also produce Bottle (16598).
116. Combine in Brew Barrel (19): "Pod of Water" (13044), "Bottle" (16598). Produces "Water Flask" (13006). Requires Brewing, trivial 21.
117. Combine in Pottery Wheel (21): "Water Flask" (13006), "Block of Clay" (16901). Produces "Small Block of Clay" (16900) x3. Requires Pottery, trivial 21.
118. Combine in Pottery Wheel (21): "Small Block of Clay" (16900), "Water Flask" (13006). Produces "Block of Clay" (16901). Requires Pottery, trivial 21.
119. Combine in Pottery Wheel (21): "Water Flask" (13006), "Large Block of Clay" (16902). Produces "Block of Clay" (16901) x2. Requires Pottery, trivial 21.
120. Combine in Pottery Wheel (21): "Block of Clay" (16901), "Water Flask" (13006). Produces "Large Block of Clay" (16902). Requires Pottery, trivial 21.
121. Common item: Large Bowl Sketch (16963). Listed in 29 zones.
122. Combine in Pottery Wheel (21): "Large Block of Clay" (16902), "Water Flask" (13006), "Large Bowl Sketch" (16963). Produces "Unfired Mixing Bowl" (16930). Requires Pottery, trivial 128.
123. Combine in Kiln (22): "Firing Sheet" (16906), "Unfired Mixing Bowl" (16930). Produces "Mixing Bowl" (17906). Requires Pottery, trivial 15.
124. Combine in "Mixing Bowl" (17906): "Sandstorm Pearl" (29909). Produces "Powdered Sandstorm Pearl" (29520) x4. Requires Baking. The combine does not fail.
125. Spawns "a Koka'Vor chieftain" (210236) in `postorms` on event_signal.
126. Loot "Storm Rider Blood" (29526) from "a Koka'Vor chieftain".
127. Loot "Storm Rider Blood" (29526) from "A stormrider" in `bothunder`.
128. Loot "Storm Rider Blood" (29526) from "Dolsoj Warrebs" in `bazaar`.
129. Loot "Storm Rider Blood" (29526) from "a Koka'Vor krovian" in `postorms`.
130. Loot "Storm Rider Blood" (29526) from "a Koka'Vor senvar" in `postorms`.
131. No quest step gives Drop of Pure Rain (29904). The dump lists it in bothunder.
132. Combine in Brew Barrel (19): "Powdered Sandstorm Pearl" (29520), "Storm Rider Blood" (29526), "Drop of Pure Rain" (29904). Produces "Hurricane Temper" (29533). Requires Brewing, trivial 135.
133. Combine in Forge (17): "Cleansed Breastplate" (15998), "Hurricane Temper" (29533). Produces "Tempered Breastplate" (15999). Requires Blacksmithing, trivial 229.
134. Combine in Forge (17): "Black Diamond of Nightmares" (29990), "Tempered Breastplate" (15999). Produces "Imbued Breastplate" (15985). Requires Blacksmithing 220. Trivial at 275.
135. poknowledge/"Aid Grimel", hand "Imbued Breastplate" (15985). Gives "Hardened Leather Signet" (16249).
136. poknowledge/"Aid Grimel", say "Skill In Brewing". Gives "Portable Drink Barrel" (17179).
137. Common item: Snake Scales (13070). Listed in 56 zones.
138. Combine in "Portable Drink Barrel" (17179): "Water Flask" (13006), "Snake Scales" (13070), "Bottle" (16598). Produces "Bog Juice" (16581). Requires Brewing, trivial 21.
139. Common item: Spit (17947). Listed in 34 zones.
140. Common item: Fire Beetle Eye (10307). Listed in 24 zones.
141. Spawns "Sepsis Rat" (45113) in `qcat` on event_death.
142. Loot "Rat Ears" (13072) from "Sepsis Rat".
143. Kill steamfont/"Diseased Female Rat". Spawns "A Young Plague Rat" (56086).
144. Loot "Rat Ears" (13072) from "A Young Plague Rat".
145. Kill steamfontmts/"Diseased Female Rat". Spawns "A Young Plague Rat" (448036).
146. Combine in "Spit" (17947): "Fire Beetle Eye" (10307), "Rat Ears" (13072). Produces "Edible Goo" (13498). Requires Baking, trivial 21.
147. freeporteast/"A Prisoner", hand "Bunker Cell #1" (12196) + "Edible Goo" (13498) + "Bog Juice" (16581). Gives "H. K. 102" (12143).
148. freportw/"A Prisoner", hand "Bunker Cell #1" (12196) + "Edible Goo" (13498) + "Bog Juice" (16581). Gives "H. K. 102" (12143).
149. highkeep/"Assistant Kiolna", hand "H. K. 102" (12143). Gives "Sealed Note" (18936).
150. paw/"Brother Hayle", hand "Sealed Note" (18936). Gives "Note" (18937).
151. southkarana/"Brother Hayle", hand "Sealed Note" (18936). Gives "Note" (18937).
152. Kill freportw/"Sir Lucan D-Lere". Spawns "Sir Lucan D'Lere" (9147).
153. Loot "Testimony of Truth" (18827) from "Sir Lucan D'Lere".
154. Loot "Testimony of Truth" (18827) from "Sir Lucan D'Lere" in `freeporteast`.
155. freeportwest/"Valeron Dushire", hand "Testimony of Truth" (18827). Gives "Brilliant Sword of Faith" (13947).
156. freportn/"Valeron Dushire", hand "Testimony of Truth" (18827). Gives "Brilliant Sword of Faith" (13947).
157. Hand "Token of Bravery" (12144) + "Token of Generosity" (13865) to freeportwest/"Merko Quetalis". Spawns "spawns Guard Willia" (383270). Loot "Token of Truth" (13866) from "spawns Guard Willia".
158. Hand "Token of Bravery" (12144) + "Token of Generosity" (13865) to freportn/"Merko Quetalis". Spawns "spawns Guard Willia" (8110). Loot "Token of Truth" (13866) from "spawns Guard Willia".
159. Loot "Token of Truth" (13866) from "Guard Willia".
160. freeportwest/"Merko Quetalis", hand "Token of Truth" (13866). Gives "Testimony" (18828).
161. freportn/"Merko Quetalis", hand "Token of Truth" (13866). Gives "Testimony" (18828).
162. Loot "Glowing Sword Hilt" (12197) from "Xicotl" in `mistmoore`.
163. paw/"Brother Hayle", hand "Glowing Sword Hilt" (12197) + "Brilliant Sword of Faith" (13947) + "Testimony" (18828) + "Note" (18937). Gives "SoulFire" (5504).
164. southkarana/"Brother Hayle", hand "Glowing Sword Hilt" (12197) + "Brilliant Sword of Faith" (13947) + "Testimony" (18828) + "Note" (18937). Gives "SoulFire" (5504).
165. airplane/"Inte Akera", hand "SoulFire" (5504). Gives "Inte's First Blessing" (18033).
166. lavastorm/"Ruathey", say "Bag". Gives "Nobleman's Bag" (17878).
167. Common item: Ghoul's Heart (2410). Listed in 8 zones.
168. No quest step gives Amstaf's Scroll (2411). The dump lists it in highkeep.
169. No quest step gives Blade of Nobility (2412). The dump lists it in butcher.
170. Loot "Hilt of the Nobleman" (2413) from "Ekeros" in `najena`.
171. Loot "Hilt of the Nobleman" (2413) from "A Skeleton" in `najena`.
172. Combine in "Nobleman's Bag" (17878): "Ghoul's Heart" (2410), "Amstaf's Scroll" (2411), "Blade of Nobility" (2412), "Hilt of the Nobleman" (2413). Produces "Ghoulbane" (5403). The combine does not fail.
173. airplane/"Inte Akera", hand "Ghoulbane" (5403). Gives "Inte's Second Blessing" (18034).
174. Hand "Miragul's Phylactery" (19072) to everfrost/"Lich Of Miragul". Spawns "Spawn Miragul" (30094). Loot "Miragul's Head" (19073) from "Spawn Miragul".
175. Loot "Miragul's Head" (19073) from "Miragul".
176. Hand "Miragul's Phylactery" (19072) to everfrost/"Lich Of Miragul". Spawns "Spawn Miragul" (30094). Loot "Miragul's Robe" (1254) from "Spawn Miragul".
177. Loot "Miragul's Robe" (1254) from "Miragul".
178. airplane/"Inte Akera", hand "Miragul's Robe" (1254) + "Inte's First Blessing" (18033) + "Inte's Second Blessing" (18034) + "Miragul's Head" (19073). Gives "Fiery Avenger" (11050).
179. fearplane/"Irak Altil", hand "Fiery Avenger" (11050) + "Mark of Atonement" (29010). Gives "Fiery Defender" (10099).
180. povalor/"Baltron Werters", say "Couragebringer". Sets `pre_pal` to `1`.
181. Requires `pre_pal` unset; no setter establishes this state.
182. povalor/"Baltron Werters", say "Couragebringer". Requires `pre_pal` unset. Gives "Baltron's Solvent" (69901).
183. sro/"Gilfal", hand "Baltron's Solvent" (69901). Requires `pre_pal` ==1. Gives "Gilfal's Scabbard" (69902).
184. Spawns "Neffiken Lord Kelek-Vor" (210229) in `postorms` on event_signal.
185. Loot "Broken Sword Piece" (69903) from "Neffiken Lord Kelek-Vor".
186. Loot "Broken Sword Piece" (69903) from "Neffiken Lord of Kelek'Vor".
187. Say "Control Timer" to hateplaneb/"Maestro".
188. Spawns "Maestro of Rancor" (186111).
189. Loot "Broken Sword Piece" (69904) from "Maestro of Rancor".
190. **Broken:** no event trigger found for `hateplaneb/maestro#timer:popmaestro`.
191. Spawns "Maestro of Rancor" (186111) after `hateplaneb/maestro#timer:popmaestro`.
192. Loot "Broken Sword Piece" (69905) from "Kaniz Painbringer" in `potorment`.
193. sro/"Gilfal", hand "Baltron's Solvent" (69901). Sets `pre_pal` to `2`.
194. Ground spawn of "Rune of Xor" (69909) in `potranquility`.
195. Ground spawn of "Rune of Yirno" (69908) in `mistmoore`.
196. Ground spawn of "Rune of Zota" (69907) in `scarlet`.
197. Ground spawn of "Rune Wilun" (69910) in `gunthak`.
198. everfrost/"Rombus", hand "Rune of Zota" (69907) + "Rune of Yirno" (69908) + "Rune of Xor" (69909) + "Rune Wilun" (69910). Requires `pre_pal` ==2. Gives "Broken Sword Piece" (69906).
199. Combine in "Gilfal's Scabbard" (69902): "Broken Sword Piece" (69903), "Broken Sword Piece" (69904), "Broken Sword Piece" (69905), "Broken Sword Piece" (69906). Produces "Fractured Couragebringer" (69911). The combine does not fail.
200. sro/"Gilfal", hand "Fractured Couragebringer" (69911). Sets `pre_pal` to `4`.
201. everfrost/"Rombus", hand "Rune of Zota" (69907) + "Rune of Yirno" (69908) + "Rune of Xor" (69909) + "Rune Wilun" (69910). Sets `pre_pal` to `3`.
202. sro/"Gilfal", hand "Fractured Couragebringer" (69911). Requires `pre_pal` ==3. Gives "Fractured Couragebringer" (69912).
203. povalor/"Baltron Werters", hand "Fractured Couragebringer" (69912). Requires `pre_pal` ==4. Gives "Couragebringer" (69913).
204. hohonora/"Irak Altil", say "Hail". Sets `paladin_epic` to `6`.
205. Spawns "Durunal the Cursebearer" (300087) in `wallofslaughter` on enter.
206. Loot "Dark and Twisted Sword" (69971) from "Durunal the Cursebearer".
207. hohonora/"Irak Altil", hand "Dark and Twisted Sword" (69971). Requires `paladin_epic` ==6. Gives "Dark and Twisted Sword" (69972).
208. Loot "Redis' Soulstone" (69983) from "Shade of Redis Linrok" in `dranikcatacombsa`.
209. Combine in "Dark and Twisted Sword" (69972): "Rithnok's Soulstone" (69941), "Drema's Soulstone" (69952), "Reiya's Soulstone" (69942), "Redis' Soulstone" (69983). Produces "Redemption" (64031). The combine does not fail.
210. hohonora/"Irak Altil", say "Tell Me About Your Master". Sets `paladin_epic` to `9`.
211. erudnint/"Josper Kenshed", say "Collect Component". Gives "Empty Bag" (17944).
212. halas/"Lysbith Mcnaff", say "Protect The Pass". Gives "Empty Bag" (17944).
213. Loot "Goblin Ice Necklace" (13897) from "Redwind" in `everfrost`.
214. Loot "Goblin Ice Necklace" (13897) from "An Ice Goblin Scout" in `everfrost`.
215. Loot "Goblin Ice Necklace" (13897) from "An Ice Goblin Whelp" in `everfrost`.
216. Loot "Goblin Ice Necklace" (13897) from "An Icy Orc" in `everfrost`.
217. Loot "Goblin Ice Necklace" (13897) from "Ice Goblin Diver" in `everfrost`.
218. Combine in "Empty Bag" (17944): "Goblin Ice Necklace" (13897). Produces "Bag of Ice Necklaces" (13898). The combine does not fail.
219. halas/"Lysbith Mcnaff", hand "Bag of Ice Necklaces" (13898). Gives "Iron Ration" (13005).
220. Common item: Gnoll Fang (13915). Listed in 5 zones.
221. halas/"Lysbith Mcnaff", hand "Gnoll Fang" (13915) + "Gnoll Fang" (13915) + "Gnoll Fang" (13915). Gives "Iron Ration" (13005).
222. Requires `halloween_draykey_rations` unset; no setter establishes this state.
223. kithicor/"Old Man Draykey", say "Instructions". Requires `halloween_draykey_rations` unset. Gives "Iron Ration" (13005).
224. commons/"Kizdean Gix", say "Messages For Neriak". Gives "Sealed Letter" (18889).
225. neriakc/"Loveal S-Nez", hand "Sealed Letter" (18889). Gives "Iron Ration" (13005).
226. Loot "Cask" (16580) from "Tugog Grigol" in `rathemtn`.
227. Common item: Hops (16591). Listed in 31 zones.
228. Common item: Malt (16595). Listed in 30 zones.
229. Common item: Yeast (16596). Listed in 30 zones.
230. Combine in "Portable Drink Barrel" (17179): "Cask" (16580), "Hops" (16591), "Malt" (16595), "Yeast" (16596). Produces "Mead" (13008). Requires Brewing, trivial 41.
231. erudnext/"Reklon Gnallen", hand "Iron Ration" (13005) + "Mead" (13008). Requires `paladin_epic` ==9. Gives "Erudin Prayer Bead" (69965).
232. Summon "Quiver of Marr" (17307) by casting "Quiver of Marr".
233. rathemtn/"Shin Master Grubbus", hand "Quiver of Marr" (17307). Requires `paladin_epic` ==9. Gives "Gukta Prayer Bead" (69964).
234. Common item: Barley (16590). Listed in 28 zones.
235. Combine in "Medicine Bag" (17901): "Hand-Formed Bottle" (45232), "Ensnaring Concoction V" (45236). Produces "Empty Vial" (10062), "Cork" (16851), "Formed Ensnaring Concoction V" (45258). Requires Alchemy, trivial 41.
236. Combine in Brew Barrel (19): "Bottle of Aged Bloodwine" (51163), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aged Bloodwine" (51164). Requires Brewing, trivial 255.
237. 11 other recipes also produce Cork (16851).
238. Combine in "Portable Drink Barrel" (17179): "Water Flask" (13006), "Celestial Essence" (9650). Produces "Purified Water" (12607). Requires Brewing, trivial 58.
239. Combine in "Tracker's Water Extractor" (17987): "Purification Tablet" (12630), "Water Reed" (12778). Produces "Purified Water" (12607) x3. Requires Pottery. The combine does not fail.
240. 3 other recipes also produce Purified Water (12607).
241. Forage "Sand Verbena" (65582) in `taka`.
242. Forage "Sand Verbena" (65582) in `takb`.
243. Forage "Sand Verbena" (65582) in `takc`.
244. Forage "Sand Verbena" (65582) in `takd`.
245. Forage "Sand Verbena" (65582) in `take`.
246. Forage "Sand Verbena" (65582) in `takf`.
247. Forage "Sand Verbena" (65582) in `takg`.
248. Forage "Sand Verbena" (65582) in `takh`.
249. Forage "Sand Verbena" (65582) in `taki`.
250. Forage "Sand Verbena" (65582) in `takj`.
251. Combine in Brew Barrel (19): "Barley" (16590), "Bottle" (16598), "Cork" (16851), "Hops" (16591), "Purified Water" (12607), "Sand Verbena" (65582), "Yeast" (16596). Produces "Bottle of Double Brewed Double Dry Stout" (51157). Requires Brewing, trivial 226.
252. kaladimb/"Datur Nightseer", hand "Bottle of Double Brewed Double Dry Stout" (51157). Requires `paladin_epic` ==9. Gives "Kaladim Prayer Bead" (69963).
253. felwithea/"General Jyleel", hand platinum:1000. Requires `paladin_epic` ==9. Gives "Felwithe Prayer Bead" (69962).
254. Ground spawn of "Freeport Prayer Bead" (69961) in `freeportwest`.
255. Ground spawn of "Freeport Prayer Bead" (69961) in `freportn`.
256. qeynos2/"Ziska Ironforge", hand platinum:500. Requires `paladin_epic` ==9. Gives "Qeynos Prayer Bead" (69960).
257. Combine in "Unfilled Set of Prayer Beads" (69968): "Rivervale Prayer Bead" (69967), "Ak'anon Prayer Bead" (69966), "Erudin Prayer Bead" (69965), "Gukta Prayer Bead" (69964), "Kaladim Prayer Bead" (69963), "Felwithe Prayer Bead" (69962), "Freeport Prayer Bead" (69961), "Qeynos Prayer Bead" (69960). Produces "Set of Prayer Beads" (69969). The combine does not fail.
258. dranikhollowsc/"Anetal", hand "Set of Prayer Beads" (69969). Sets `paladin_epic_hollowc` to `2`.
259. natimbi/"Kemik Arulon", hand "Set of Prayer Beads" (69969). Sets `paladin_epic_hollowc` to `1`.
260. natimbi/"Kemik Arulon", say "Hail". Requires `paladin_epic_hollowc` ==2. Requires `paladin_epic_hollowc` ==1. Gives "Token of Compassion" (69953).

### "Token of Chivalry" (69954)

1. qeynos2/"Camlend Serbold", say "Gem". Gives "Unfilled Set of Prayer Beads" (69968).
2. rivervale/"Kaya Cloudfoot", say "Different About It". Gives "Note from Kaya" (69970).
3. rivervale/"Deputy Cheel", hand "Note from Kaya" (69970). Gives "Rivervale Prayer Bead" (69967).
4. **Broken:** nothing in the graph gives, loots, spawns, or combines Ak`anon Prayer Bead (69966).
5. Say "Hail" to skyfire/"Dry Sapara".
6. Spawns "Rithnok the Tormented" (91193).
7. Loot "Rithnok's Soulstone" (69935) from "Rithnok the Tormented".
8. skyfire/"Dry Sapara", hand "Rithnok's Soulstone" (69935). Gives "Rithnok's Soulstone" (69936).
9. Ground spawn of "Soulstone Shard" (69937) in `draniksscar`.
10. Ground spawn of "Soulstone Shard" (69938) in `bloodfields`.
11. Ground spawn of "Soulstone Shard" (69939) in `causeway`.
12. Ground spawn of "Soulstone Shard" (69940) in `dranik`.
13. Combine in "Rithnok's Soulstone" (69936): "Soulstone Shard" (69937), "Soulstone Shard" (69938), "Soulstone Shard" (69939), "Soulstone Shard" (69940). Produces "Rithnok's Soulstone" (69941). The combine does not fail.
14. Hand "Enchanted Bone Powder" (69949) to letalis/"Drema Young". Spawns "Drema Young" (169128). Loot "Drema's Soulstone" (69928) from "Drema Young".
15. Loot "Drema's Soulstone" (69928) from "Drema Young".
16. Loot "Drema's Soulstone" (69928) from "Drema Young" in `letalis`.
17. Loot "Soulstone Shard" (69950) from "Coterie Corruptor" in `tenebrous`.
18. Say "Mujaki Death" to ponightmare/"Mujaki".
19. Spawns "Shade of Mujaki the Devourer" (204081).
20. Loot "Soulstone Shard" (69951) from "Shade of Mujaki the Devourer".
21. Combine in "Drema's Soulstone" (69928): "Soulstone Shard" (69950), "Soulstone Shard" (69951). Produces "Drema's Soulstone" (69952). The combine does not fail.
22. freporte/"Brunar Rankin", say "Hail". Sets `paladin_epic` to `3`.
23. global/"Global Player", combine recipe 19880. Sets `paladin_epic` to `8`.
24. Spawns "A Corrupted Koalindl" (69141) in `oot` on event_fish_success.
25. Loot "Corrupted Koalindl's Heart" (69929) from "A Corrupted Koalindl".
26. Spawns "A Corrupted Koalindl" (224432) in `gunthak` on event_fish_success.
27. Loot "Corrupted Koalindl's Heart" (69930) from "A Corrupted Koalindl".
28. Spawns "A Corrupted Koalindl" (93306) in `overthere` on event_fish_success.
29. Loot "Corrupted Koalindl's Heart" (69931) from "A Corrupted Koalindl".
30. Spawns "A Corrupted Koalindl" (182150) in `nedaria` on event_fish_success.
31. Loot "Corrupted Koalindl's Heart" (69932) from "A Corrupted Koalindl".
32. qeynos2/"Enic Ruklin", hand "Corrupted Koalindl's Heart" (69929) + "Corrupted Koalindl's Heart" (69930) + "Corrupted Koalindl's Heart" (69931) + "Corrupted Koalindl's Heart" (69932). Sets `paladin_epic` to `4`.
33. dawnshroud/"Mikhal Young", say "Find Anything". Requires `paladin_epic` ==4. Gives "Drema's Locket" (69945).
34. letalis/"Drema Young", hand "Drema's Locket" (69945). Requires `paladin_epic` set. Requires `paladin_epic` >=4. Gives "Drema's Fingerbone" (69946).
35. dawnshroud/"Mikhal Young", hand "Drema's Fingerbone" (69946). Sets `paladin_epic` to `5`.
36. abysmal/"Lovine Lemise", say "Ingredients". Requires `paladin_epic` ==5. Gives "Lovine's Potion Bag" (69922).
37. No quest step gives Ra`Tuk Screambringer's Jaw (69921). The dump lists it in barindu.
38. Loot "Noc Fleshfeasters Tail" (69920) from "A Noc Fleshfeaster" in `riwwi`.
39. Loot "Mastruq Havocblade Blood" (69919) from "A Mastruq Havocblade" in `qinimi`.
40. Loot "Mastruq Havocblade Blood" (69919) from "A Mastruq Warfiend" in `qinimi`.
41. Loot "Potameid Seaweed Strands" (69918) from "An Entrapped Potameid" in `natimbi`.
42. Combine in "Lovine's Potion Bag" (69922): "Ra'Tuk Screambringer's Jaw" (69921), "Noc Fleshfeasters Tail" (69920), "Mastruq Havocblade Blood" (69919), "Potameid Seaweed Strands" (69918). Produces "Lovine's Potion Bag" (69923). The combine does not fail.
43. abysmal/"Lovine Lemise", hand "Lovine's Potion Bag" (69923). Sets `paladin_epic_reiya` to `1`.
44. Summon "Foldable Medicine Bag" (17770) by casting "Unfold Medicine Bag".
45. Common item: Fine Potion Vial (95846). Listed in 15 zones.
46. Common item: Robust Shadow Essence (96911). Listed in 5 zones.
47. Loot "Sage Leaf" (14215) from "a Di'zok Herbalist" in `chardok`.
48. Loot "Sage Leaf" (14215) from "a Sarnak Herb Collector" in `chardok`.
49. Loot "Sage Leaf" (14215) from "an Apprentice Herbalist" in `chardok`.
50. Loot "Valerian Root" (14230) from "a Di'zok Herbalist" in `chardok`.
51. Loot "Valerian Root" (14230) from "a Sarnak Herb Collector" in `chardok`.
52. Loot "Valerian Root" (14230) from "an Apprentice Herbalist" in `chardok`.
53. Common item: Woundwart (16526). Listed in 9 zones.
54. Combine in "Foldable Medicine Bag" (17770): "Fine Potion Vial" (95846), "Robust Shadow Essence" (96911), "Sage Leaf" (14215), "Valerian Root" (14230), "Woundwart" (16526). Produces "Mist of the Breathless" (96937). Requires Alchemy, trivial 224.
55. abysmal/"Reiya The Pained", hand "Mist of the Breathless" (96937). Requires `paladin_epic_reiya` ==1. Gives "Reiya's Soulstone" (69924).
56. Spawns "Shade of Reiya the Pained" (284104) in `ferubi` on enter.
57. Loot "Soulstone Shard" (69943) from "Shade of Reiya the Pained".
58. Loot "Soulstone Shard" (69944) from "Vuranish Xxuro" in `vxed`.
59. Combine in "Reiya's Soulstone" (69924): "Soulstone Shard" (69943), "Soulstone Shard" (69944). Produces "Reiya's Soulstone" (69942). The combine does not fail.
60. Loot "Tainted Darksteel Sword" (29000) from "Keeper of the Tombs" in `hole`.
61. freeporteast/"Peasant Woman", say "I Will Take It". Gives "Bucket of Water" (29008).
62. freportw/"Peasant Woman", say "I Will Take It". Gives "Bucket of Water" (29008).
63. freeporteast/"Joshua", hand "Bucket of Water" (29008). Gives "Bucket of Pure Water" (29009).
64. freportw/"Joshua", hand "Bucket of Water" (29008). Gives "Bucket of Pure Water" (29009).
65. erudnext/"Reklon Gnallen", hand "Tainted Darksteel Sword" (29000) + "Bucket of Pure Water" (29009). Gives "Gleaming Crested Sword" (29003).
66. Loot "Tainted Darksteel Breastplate" (29001) from "Thought Destroyer" in `hateplaneb`.
67. kaladimb/"Nella Stonebraids", say "Jark". Gives "Cold Plate of Beef and Bread" (29007).
68. kaladimb/"Nella Stonebraids", say "Dinner". Gives "Cold Plate of Beef and Bread" (29007).
69. kaladimb/"Jark", hand "Cold Plate of Beef and Bread" (29007). Gives "Pure Crystal" (29006).
70. erudnext/"Reklon Gnallen", hand "Tainted Darksteel Breastplate" (29001) + "Pure Crystal" (29006). Gives "Gleaming Crested Breastplate" (29004).
71. Loot "Tainted Darksteel Shield" (29002) from "Kirak Vil" in `nektulos`.
72. felwithea/"Elia The Pure", hand "Tainted Darksteel Shield" (29002). Gives "Gleaming Crested Shield" (29005).
73. erudnext/"Reklon Gnallen", hand "Gleaming Crested Sword" (29003) + "Gleaming Crested Breastplate" (29004) + "Gleaming Crested Shield" (29005). Gives "Mark of Atonement" (29010).
74. No quest step gives Drom's Champagne (13829). The dump lists it in freeporteast, freporte, highpasshold.
75. freeporteast/"Tykar Renlin", hand "Drom's Champagne" (13829) + "Drom's Champagne" (13829) + "Drom's Champagne" (13829) + "Drom's Champagne" (13829). Gives "Bunker Cell #1" (12196).
76. freporte/"Tykar Renlin", hand "Drom's Champagne" (13829) + "Drom's Champagne" (13829) + "Drom's Champagne" (13829) + "Drom's Champagne" (13829). Gives "Bunker Cell #1" (12196).
77. Summon "Black Diamond of Nightmares" (29990) by casting "Imbue Nightmare".
78. poknowledge/"Aid Grimel", say "Versed In The Art Of Smithing". Gives "Filthy Breastplate" (15984).
79. Combine in "Mixing Bowl" (17906): "Celestial Solvent" (9731), "Words of Acquisition (Beza)" (11866). Produces "Celestial Essence" (9650). Requires Baking, trivial 15. The combine does not fail.
80. Combine in "Mixing Bowl" (17906): "Celestial Solvent" (9731), "Words of Burnishing" (11862). Produces "Celestial Essence" (9650). Requires Baking, trivial 15. The combine does not fail.
81. 67 other recipes also produce Celestial Essence (9650).
82. Common item: Jar of Acid (22133). Listed in 15 zones.
83. Combine in Brew Barrel (19): "Celestial Essence" (9650), "Jar of Acid" (22133). Produces "Acid Wash" (15987). Requires Brewing, trivial 151.
84. Combine in Forge (17): "Filthy Breastplate" (15984), "Acid Wash" (15987). Produces "Cleansed Breastplate" (15998). Requires Blacksmithing, trivial 227.
85. Common item: Mortar and Pestle (17904). Listed in 12 zones.
86. No quest step gives Sandstorm Pearl (29909). The dump lists it in bothunder.
87. Combine in "Mortar and Pestle" (17904): "Sandstorm Pearl" (29909). Produces "Powdered Sandstorm Pearl" (29520) x4. Requires Make Poison, trivial 255.
88. Common item: Firing Sheet (16906). Listed in 34 zones.
89. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
90. qeynos/"Wolten Grafe", say "Crush The Undead". Gives "Box For Bones" (17941).
91. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `steamfont`.
92. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `tox`.
93. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `toxxulia`.
94. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
95. toxxulia/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
96. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). The combine does not fail.
97. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
98. qeynos2/"Phin Esrinap", say "Supplies". Gives "Message to Konem" (18921).
99. qeytoqrg/"Konem Matse", hand "Message to Konem" (18921). Gives "Grathin's Invoice" (18922).
100. qeynos2/"Phin Esrinap", hand "Grathin's Invoice" (18922). Gives "Water Flask" (13006).
101. Say "Tm Devrak Death" to rujd/"Rujd".
102. Spawns "spawn chest with Heavy Orcish Prison Key" (245241).
103. Loot "Pod of Water" (13044) from "spawn chest with Heavy Orcish Prison Key".
104. Say "Tm Dokorel Death" to rujd/"Rujd".
105. Say "Tm Velrek Death" to rujd/"Rujd".
106. Say "Researcher Death" to rujg/"Rujg".
107. Spawns "A Barrel" (260015).
108. Loot "Pod of Water" (13044) from "A Barrel".
109. 3 other loot steps also yield Pod of Water (13044).
110. Forage "Pod of Water" (13044) in `ruja`.
111. Forage "Pod of Water" (13044) in `uqua`.
112. Forage "Pod of Water" (13044) in `yxtta`.
113. Combine in Brew Barrel (19): "Bottle of Aged Bloodwine" (51163), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aged Bloodwine" (51164). Requires Brewing, trivial 255.
114. Combine in Brew Barrel (19): "Bottle of Aldo's Bitter Ale" (75805), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aldo's Bitter Ale" (75811). Requires Brewing, trivial 15.
115. 17 other recipes also produce Bottle (16598).
116. Combine in Brew Barrel (19): "Pod of Water" (13044), "Bottle" (16598). Produces "Water Flask" (13006). Requires Brewing, trivial 21.
117. Combine in Pottery Wheel (21): "Water Flask" (13006), "Block of Clay" (16901). Produces "Small Block of Clay" (16900) x3. Requires Pottery, trivial 21.
118. Combine in Pottery Wheel (21): "Small Block of Clay" (16900), "Water Flask" (13006). Produces "Block of Clay" (16901). Requires Pottery, trivial 21.
119. Combine in Pottery Wheel (21): "Water Flask" (13006), "Large Block of Clay" (16902). Produces "Block of Clay" (16901) x2. Requires Pottery, trivial 21.
120. Combine in Pottery Wheel (21): "Block of Clay" (16901), "Water Flask" (13006). Produces "Large Block of Clay" (16902). Requires Pottery, trivial 21.
121. Common item: Large Bowl Sketch (16963). Listed in 29 zones.
122. Combine in Pottery Wheel (21): "Large Block of Clay" (16902), "Water Flask" (13006), "Large Bowl Sketch" (16963). Produces "Unfired Mixing Bowl" (16930). Requires Pottery, trivial 128.
123. Combine in Kiln (22): "Firing Sheet" (16906), "Unfired Mixing Bowl" (16930). Produces "Mixing Bowl" (17906). Requires Pottery, trivial 15.
124. Combine in "Mixing Bowl" (17906): "Sandstorm Pearl" (29909). Produces "Powdered Sandstorm Pearl" (29520) x4. Requires Baking. The combine does not fail.
125. Spawns "a Koka'Vor chieftain" (210236) in `postorms` on event_signal.
126. Loot "Storm Rider Blood" (29526) from "a Koka'Vor chieftain".
127. Loot "Storm Rider Blood" (29526) from "A stormrider" in `bothunder`.
128. Loot "Storm Rider Blood" (29526) from "Dolsoj Warrebs" in `bazaar`.
129. Loot "Storm Rider Blood" (29526) from "a Koka'Vor krovian" in `postorms`.
130. Loot "Storm Rider Blood" (29526) from "a Koka'Vor senvar" in `postorms`.
131. No quest step gives Drop of Pure Rain (29904). The dump lists it in bothunder.
132. Combine in Brew Barrel (19): "Powdered Sandstorm Pearl" (29520), "Storm Rider Blood" (29526), "Drop of Pure Rain" (29904). Produces "Hurricane Temper" (29533). Requires Brewing, trivial 135.
133. Combine in Forge (17): "Cleansed Breastplate" (15998), "Hurricane Temper" (29533). Produces "Tempered Breastplate" (15999). Requires Blacksmithing, trivial 229.
134. Combine in Forge (17): "Black Diamond of Nightmares" (29990), "Tempered Breastplate" (15999). Produces "Imbued Breastplate" (15985). Requires Blacksmithing 220. Trivial at 275.
135. poknowledge/"Aid Grimel", hand "Imbued Breastplate" (15985). Gives "Hardened Leather Signet" (16249).
136. poknowledge/"Aid Grimel", say "Skill In Brewing". Gives "Portable Drink Barrel" (17179).
137. Common item: Snake Scales (13070). Listed in 56 zones.
138. Combine in "Portable Drink Barrel" (17179): "Water Flask" (13006), "Snake Scales" (13070), "Bottle" (16598). Produces "Bog Juice" (16581). Requires Brewing, trivial 21.
139. Common item: Spit (17947). Listed in 34 zones.
140. Common item: Fire Beetle Eye (10307). Listed in 24 zones.
141. Spawns "Sepsis Rat" (45113) in `qcat` on event_death.
142. Loot "Rat Ears" (13072) from "Sepsis Rat".
143. Kill steamfont/"Diseased Female Rat". Spawns "A Young Plague Rat" (56086).
144. Loot "Rat Ears" (13072) from "A Young Plague Rat".
145. Kill steamfontmts/"Diseased Female Rat". Spawns "A Young Plague Rat" (448036).
146. Combine in "Spit" (17947): "Fire Beetle Eye" (10307), "Rat Ears" (13072). Produces "Edible Goo" (13498). Requires Baking, trivial 21.
147. freeporteast/"A Prisoner", hand "Bunker Cell #1" (12196) + "Edible Goo" (13498) + "Bog Juice" (16581). Gives "H. K. 102" (12143).
148. freportw/"A Prisoner", hand "Bunker Cell #1" (12196) + "Edible Goo" (13498) + "Bog Juice" (16581). Gives "H. K. 102" (12143).
149. highkeep/"Assistant Kiolna", hand "H. K. 102" (12143). Gives "Sealed Note" (18936).
150. paw/"Brother Hayle", hand "Sealed Note" (18936). Gives "Note" (18937).
151. southkarana/"Brother Hayle", hand "Sealed Note" (18936). Gives "Note" (18937).
152. Kill freportw/"Sir Lucan D-Lere". Spawns "Sir Lucan D'Lere" (9147).
153. Loot "Testimony of Truth" (18827) from "Sir Lucan D'Lere".
154. Loot "Testimony of Truth" (18827) from "Sir Lucan D'Lere" in `freeporteast`.
155. freeportwest/"Valeron Dushire", hand "Testimony of Truth" (18827). Gives "Brilliant Sword of Faith" (13947).
156. freportn/"Valeron Dushire", hand "Testimony of Truth" (18827). Gives "Brilliant Sword of Faith" (13947).
157. Hand "Token of Bravery" (12144) + "Token of Generosity" (13865) to freeportwest/"Merko Quetalis". Spawns "spawns Guard Willia" (383270). Loot "Token of Truth" (13866) from "spawns Guard Willia".
158. Hand "Token of Bravery" (12144) + "Token of Generosity" (13865) to freportn/"Merko Quetalis". Spawns "spawns Guard Willia" (8110). Loot "Token of Truth" (13866) from "spawns Guard Willia".
159. Loot "Token of Truth" (13866) from "Guard Willia".
160. freeportwest/"Merko Quetalis", hand "Token of Truth" (13866). Gives "Testimony" (18828).
161. freportn/"Merko Quetalis", hand "Token of Truth" (13866). Gives "Testimony" (18828).
162. Loot "Glowing Sword Hilt" (12197) from "Xicotl" in `mistmoore`.
163. paw/"Brother Hayle", hand "Glowing Sword Hilt" (12197) + "Brilliant Sword of Faith" (13947) + "Testimony" (18828) + "Note" (18937). Gives "SoulFire" (5504).
164. southkarana/"Brother Hayle", hand "Glowing Sword Hilt" (12197) + "Brilliant Sword of Faith" (13947) + "Testimony" (18828) + "Note" (18937). Gives "SoulFire" (5504).
165. airplane/"Inte Akera", hand "SoulFire" (5504). Gives "Inte's First Blessing" (18033).
166. lavastorm/"Ruathey", say "Bag". Gives "Nobleman's Bag" (17878).
167. Common item: Ghoul's Heart (2410). Listed in 8 zones.
168. No quest step gives Amstaf's Scroll (2411). The dump lists it in highkeep.
169. No quest step gives Blade of Nobility (2412). The dump lists it in butcher.
170. Loot "Hilt of the Nobleman" (2413) from "Ekeros" in `najena`.
171. Loot "Hilt of the Nobleman" (2413) from "A Skeleton" in `najena`.
172. Combine in "Nobleman's Bag" (17878): "Ghoul's Heart" (2410), "Amstaf's Scroll" (2411), "Blade of Nobility" (2412), "Hilt of the Nobleman" (2413). Produces "Ghoulbane" (5403). The combine does not fail.
173. airplane/"Inte Akera", hand "Ghoulbane" (5403). Gives "Inte's Second Blessing" (18034).
174. Hand "Miragul's Phylactery" (19072) to everfrost/"Lich Of Miragul". Spawns "Spawn Miragul" (30094). Loot "Miragul's Head" (19073) from "Spawn Miragul".
175. Loot "Miragul's Head" (19073) from "Miragul".
176. Hand "Miragul's Phylactery" (19072) to everfrost/"Lich Of Miragul". Spawns "Spawn Miragul" (30094). Loot "Miragul's Robe" (1254) from "Spawn Miragul".
177. Loot "Miragul's Robe" (1254) from "Miragul".
178. airplane/"Inte Akera", hand "Miragul's Robe" (1254) + "Inte's First Blessing" (18033) + "Inte's Second Blessing" (18034) + "Miragul's Head" (19073). Gives "Fiery Avenger" (11050).
179. fearplane/"Irak Altil", hand "Fiery Avenger" (11050) + "Mark of Atonement" (29010). Gives "Fiery Defender" (10099).
180. povalor/"Baltron Werters", say "Couragebringer". Sets `pre_pal` to `1`.
181. Requires `pre_pal` unset; no setter establishes this state.
182. povalor/"Baltron Werters", say "Couragebringer". Requires `pre_pal` unset. Gives "Baltron's Solvent" (69901).
183. sro/"Gilfal", hand "Baltron's Solvent" (69901). Requires `pre_pal` ==1. Gives "Gilfal's Scabbard" (69902).
184. Spawns "Neffiken Lord Kelek-Vor" (210229) in `postorms` on event_signal.
185. Loot "Broken Sword Piece" (69903) from "Neffiken Lord Kelek-Vor".
186. Loot "Broken Sword Piece" (69903) from "Neffiken Lord of Kelek'Vor".
187. Say "Control Timer" to hateplaneb/"Maestro".
188. Spawns "Maestro of Rancor" (186111).
189. Loot "Broken Sword Piece" (69904) from "Maestro of Rancor".
190. **Broken:** no event trigger found for `hateplaneb/maestro#timer:popmaestro`.
191. Spawns "Maestro of Rancor" (186111) after `hateplaneb/maestro#timer:popmaestro`.
192. Loot "Broken Sword Piece" (69905) from "Kaniz Painbringer" in `potorment`.
193. sro/"Gilfal", hand "Baltron's Solvent" (69901). Sets `pre_pal` to `2`.
194. Ground spawn of "Rune of Xor" (69909) in `potranquility`.
195. Ground spawn of "Rune of Yirno" (69908) in `mistmoore`.
196. Ground spawn of "Rune of Zota" (69907) in `scarlet`.
197. Ground spawn of "Rune Wilun" (69910) in `gunthak`.
198. everfrost/"Rombus", hand "Rune of Zota" (69907) + "Rune of Yirno" (69908) + "Rune of Xor" (69909) + "Rune Wilun" (69910). Requires `pre_pal` ==2. Gives "Broken Sword Piece" (69906).
199. Combine in "Gilfal's Scabbard" (69902): "Broken Sword Piece" (69903), "Broken Sword Piece" (69904), "Broken Sword Piece" (69905), "Broken Sword Piece" (69906). Produces "Fractured Couragebringer" (69911). The combine does not fail.
200. sro/"Gilfal", hand "Fractured Couragebringer" (69911). Sets `pre_pal` to `4`.
201. everfrost/"Rombus", hand "Rune of Zota" (69907) + "Rune of Yirno" (69908) + "Rune of Xor" (69909) + "Rune Wilun" (69910). Sets `pre_pal` to `3`.
202. sro/"Gilfal", hand "Fractured Couragebringer" (69911). Requires `pre_pal` ==3. Gives "Fractured Couragebringer" (69912).
203. povalor/"Baltron Werters", hand "Fractured Couragebringer" (69912). Requires `pre_pal` ==4. Gives "Couragebringer" (69913).
204. hohonora/"Irak Altil", say "Hail". Sets `paladin_epic` to `6`.
205. Spawns "Durunal the Cursebearer" (300087) in `wallofslaughter` on enter.
206. Loot "Dark and Twisted Sword" (69971) from "Durunal the Cursebearer".
207. hohonora/"Irak Altil", hand "Dark and Twisted Sword" (69971). Requires `paladin_epic` ==6. Gives "Dark and Twisted Sword" (69972).
208. Loot "Redis' Soulstone" (69983) from "Shade of Redis Linrok" in `dranikcatacombsa`.
209. Combine in "Dark and Twisted Sword" (69972): "Rithnok's Soulstone" (69941), "Drema's Soulstone" (69952), "Reiya's Soulstone" (69942), "Redis' Soulstone" (69983). Produces "Redemption" (64031). The combine does not fail.
210. hohonora/"Irak Altil", say "Tell Me About Your Master". Sets `paladin_epic` to `9`.
211. erudnint/"Josper Kenshed", say "Collect Component". Gives "Empty Bag" (17944).
212. halas/"Lysbith Mcnaff", say "Protect The Pass". Gives "Empty Bag" (17944).
213. Loot "Goblin Ice Necklace" (13897) from "Redwind" in `everfrost`.
214. Loot "Goblin Ice Necklace" (13897) from "An Ice Goblin Scout" in `everfrost`.
215. Loot "Goblin Ice Necklace" (13897) from "An Ice Goblin Whelp" in `everfrost`.
216. Loot "Goblin Ice Necklace" (13897) from "An Icy Orc" in `everfrost`.
217. Loot "Goblin Ice Necklace" (13897) from "Ice Goblin Diver" in `everfrost`.
218. Combine in "Empty Bag" (17944): "Goblin Ice Necklace" (13897). Produces "Bag of Ice Necklaces" (13898). The combine does not fail.
219. halas/"Lysbith Mcnaff", hand "Bag of Ice Necklaces" (13898). Gives "Iron Ration" (13005).
220. Common item: Gnoll Fang (13915). Listed in 5 zones.
221. halas/"Lysbith Mcnaff", hand "Gnoll Fang" (13915) + "Gnoll Fang" (13915) + "Gnoll Fang" (13915). Gives "Iron Ration" (13005).
222. Requires `halloween_draykey_rations` unset; no setter establishes this state.
223. kithicor/"Old Man Draykey", say "Instructions". Requires `halloween_draykey_rations` unset. Gives "Iron Ration" (13005).
224. commons/"Kizdean Gix", say "Messages For Neriak". Gives "Sealed Letter" (18889).
225. neriakc/"Loveal S-Nez", hand "Sealed Letter" (18889). Gives "Iron Ration" (13005).
226. Loot "Cask" (16580) from "Tugog Grigol" in `rathemtn`.
227. Common item: Hops (16591). Listed in 31 zones.
228. Common item: Malt (16595). Listed in 30 zones.
229. Common item: Yeast (16596). Listed in 30 zones.
230. Combine in "Portable Drink Barrel" (17179): "Cask" (16580), "Hops" (16591), "Malt" (16595), "Yeast" (16596). Produces "Mead" (13008). Requires Brewing, trivial 41.
231. erudnext/"Reklon Gnallen", hand "Iron Ration" (13005) + "Mead" (13008). Requires `paladin_epic` ==9. Gives "Erudin Prayer Bead" (69965).
232. Summon "Quiver of Marr" (17307) by casting "Quiver of Marr".
233. rathemtn/"Shin Master Grubbus", hand "Quiver of Marr" (17307). Requires `paladin_epic` ==9. Gives "Gukta Prayer Bead" (69964).
234. Common item: Barley (16590). Listed in 28 zones.
235. Combine in "Medicine Bag" (17901): "Hand-Formed Bottle" (45232), "Ensnaring Concoction V" (45236). Produces "Empty Vial" (10062), "Cork" (16851), "Formed Ensnaring Concoction V" (45258). Requires Alchemy, trivial 41.
236. Combine in Brew Barrel (19): "Bottle of Aged Bloodwine" (51163), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aged Bloodwine" (51164). Requires Brewing, trivial 255.
237. 11 other recipes also produce Cork (16851).
238. Combine in "Portable Drink Barrel" (17179): "Water Flask" (13006), "Celestial Essence" (9650). Produces "Purified Water" (12607). Requires Brewing, trivial 58.
239. Combine in "Tracker's Water Extractor" (17987): "Purification Tablet" (12630), "Water Reed" (12778). Produces "Purified Water" (12607) x3. Requires Pottery. The combine does not fail.
240. 3 other recipes also produce Purified Water (12607).
241. Forage "Sand Verbena" (65582) in `taka`.
242. Forage "Sand Verbena" (65582) in `takb`.
243. Forage "Sand Verbena" (65582) in `takc`.
244. Forage "Sand Verbena" (65582) in `takd`.
245. Forage "Sand Verbena" (65582) in `take`.
246. Forage "Sand Verbena" (65582) in `takf`.
247. Forage "Sand Verbena" (65582) in `takg`.
248. Forage "Sand Verbena" (65582) in `takh`.
249. Forage "Sand Verbena" (65582) in `taki`.
250. Forage "Sand Verbena" (65582) in `takj`.
251. Combine in Brew Barrel (19): "Barley" (16590), "Bottle" (16598), "Cork" (16851), "Hops" (16591), "Purified Water" (12607), "Sand Verbena" (65582), "Yeast" (16596). Produces "Bottle of Double Brewed Double Dry Stout" (51157). Requires Brewing, trivial 226.
252. kaladimb/"Datur Nightseer", hand "Bottle of Double Brewed Double Dry Stout" (51157). Requires `paladin_epic` ==9. Gives "Kaladim Prayer Bead" (69963).
253. felwithea/"General Jyleel", hand platinum:1000. Requires `paladin_epic` ==9. Gives "Felwithe Prayer Bead" (69962).
254. Ground spawn of "Freeport Prayer Bead" (69961) in `freeportwest`.
255. Ground spawn of "Freeport Prayer Bead" (69961) in `freportn`.
256. qeynos2/"Ziska Ironforge", hand platinum:500. Requires `paladin_epic` ==9. Gives "Qeynos Prayer Bead" (69960).
257. Combine in "Unfilled Set of Prayer Beads" (69968): "Rivervale Prayer Bead" (69967), "Ak'anon Prayer Bead" (69966), "Erudin Prayer Bead" (69965), "Gukta Prayer Bead" (69964), "Kaladim Prayer Bead" (69963), "Felwithe Prayer Bead" (69962), "Freeport Prayer Bead" (69961), "Qeynos Prayer Bead" (69960). Produces "Set of Prayer Beads" (69969). The combine does not fail.
258. dranikhollowsc/"Anetal", hand "Set of Prayer Beads" (69969). Sets `paladin_epic_hollowc` to `2`.
259. natimbi/"Kemik Arulon", hand "Set of Prayer Beads" (69969). Sets `paladin_epic_hollowc` to `1`.
260. natimbi/"Kemik Arulon", say "Hail". Requires `paladin_epic_hollowc` ==2. Requires `paladin_epic_hollowc` ==1. Gives "Token of Compassion" (69953).
261. Requires `pal_chest_keel` unset; no setter establishes this state.
262. oasis/"Paladin Epic", say "Hail". Requires `pal_chest_keel` unset. Gives "Keelee's Brooch" (69982).
263. oasis/"Paladin Epic", say "Keelee Say". Gives "Keelee's Brooch" (69982).
264. sro/"Instructor Maerceci", hand "Keelee's Brooch" (69982). Gives "Token of Chivalry" (69954).

### "Token of Heroism" (69955)

1. Loot "Valdoon Kel'Novar's Heart" (69981) from "Valdoon Kel'Novar" in `mmcc`.
2. felwithea/"Galrun Starforge", hand "Valdoon Kel'Novar's Heart" (69981). Gives "Token of Cleansing" (69956).
3. provinggrounds/"Pashia Clouddancer", say "Note". Gives "Note from Pashia" (69973).
4. nedaria/"Duram Firechaser", hand "Note from Pashia" (69973). Gives "Token of Heroism" (69955).

### "Token of Cleansing" (69956)

1. Loot "Valdoon Kel'Novar's Heart" (69981) from "Valdoon Kel'Novar" in `mmcc`.
2. felwithea/"Galrun Starforge", hand "Valdoon Kel'Novar's Heart" (69981). Gives "Token of Cleansing" (69956).

### "Scabbard of the Righteous" (69959)

1. qeynos2/"Camlend Serbold", say "Gem". Gives "Unfilled Set of Prayer Beads" (69968).
2. rivervale/"Kaya Cloudfoot", say "Different About It". Gives "Note from Kaya" (69970).
3. rivervale/"Deputy Cheel", hand "Note from Kaya" (69970). Gives "Rivervale Prayer Bead" (69967).
4. **Broken:** nothing in the graph gives, loots, spawns, or combines Ak`anon Prayer Bead (69966).
5. Say "Hail" to skyfire/"Dry Sapara".
6. Spawns "Rithnok the Tormented" (91193).
7. Loot "Rithnok's Soulstone" (69935) from "Rithnok the Tormented".
8. skyfire/"Dry Sapara", hand "Rithnok's Soulstone" (69935). Gives "Rithnok's Soulstone" (69936).
9. Ground spawn of "Soulstone Shard" (69937) in `draniksscar`.
10. Ground spawn of "Soulstone Shard" (69938) in `bloodfields`.
11. Ground spawn of "Soulstone Shard" (69939) in `causeway`.
12. Ground spawn of "Soulstone Shard" (69940) in `dranik`.
13. Combine in "Rithnok's Soulstone" (69936): "Soulstone Shard" (69937), "Soulstone Shard" (69938), "Soulstone Shard" (69939), "Soulstone Shard" (69940). Produces "Rithnok's Soulstone" (69941). The combine does not fail.
14. Hand "Enchanted Bone Powder" (69949) to letalis/"Drema Young". Spawns "Drema Young" (169128). Loot "Drema's Soulstone" (69928) from "Drema Young".
15. Loot "Drema's Soulstone" (69928) from "Drema Young".
16. Loot "Drema's Soulstone" (69928) from "Drema Young" in `letalis`.
17. Loot "Soulstone Shard" (69950) from "Coterie Corruptor" in `tenebrous`.
18. Say "Mujaki Death" to ponightmare/"Mujaki".
19. Spawns "Shade of Mujaki the Devourer" (204081).
20. Loot "Soulstone Shard" (69951) from "Shade of Mujaki the Devourer".
21. Combine in "Drema's Soulstone" (69928): "Soulstone Shard" (69950), "Soulstone Shard" (69951). Produces "Drema's Soulstone" (69952). The combine does not fail.
22. freporte/"Brunar Rankin", say "Hail". Sets `paladin_epic` to `3`.
23. global/"Global Player", combine recipe 19880. Sets `paladin_epic` to `8`.
24. Spawns "A Corrupted Koalindl" (69141) in `oot` on event_fish_success.
25. Loot "Corrupted Koalindl's Heart" (69929) from "A Corrupted Koalindl".
26. Spawns "A Corrupted Koalindl" (224432) in `gunthak` on event_fish_success.
27. Loot "Corrupted Koalindl's Heart" (69930) from "A Corrupted Koalindl".
28. Spawns "A Corrupted Koalindl" (93306) in `overthere` on event_fish_success.
29. Loot "Corrupted Koalindl's Heart" (69931) from "A Corrupted Koalindl".
30. Spawns "A Corrupted Koalindl" (182150) in `nedaria` on event_fish_success.
31. Loot "Corrupted Koalindl's Heart" (69932) from "A Corrupted Koalindl".
32. qeynos2/"Enic Ruklin", hand "Corrupted Koalindl's Heart" (69929) + "Corrupted Koalindl's Heart" (69930) + "Corrupted Koalindl's Heart" (69931) + "Corrupted Koalindl's Heart" (69932). Sets `paladin_epic` to `4`.
33. dawnshroud/"Mikhal Young", say "Find Anything". Requires `paladin_epic` ==4. Gives "Drema's Locket" (69945).
34. letalis/"Drema Young", hand "Drema's Locket" (69945). Requires `paladin_epic` set. Requires `paladin_epic` >=4. Gives "Drema's Fingerbone" (69946).
35. dawnshroud/"Mikhal Young", hand "Drema's Fingerbone" (69946). Sets `paladin_epic` to `5`.
36. abysmal/"Lovine Lemise", say "Ingredients". Requires `paladin_epic` ==5. Gives "Lovine's Potion Bag" (69922).
37. No quest step gives Ra`Tuk Screambringer's Jaw (69921). The dump lists it in barindu.
38. Loot "Noc Fleshfeasters Tail" (69920) from "A Noc Fleshfeaster" in `riwwi`.
39. Loot "Mastruq Havocblade Blood" (69919) from "A Mastruq Havocblade" in `qinimi`.
40. Loot "Mastruq Havocblade Blood" (69919) from "A Mastruq Warfiend" in `qinimi`.
41. Loot "Potameid Seaweed Strands" (69918) from "An Entrapped Potameid" in `natimbi`.
42. Combine in "Lovine's Potion Bag" (69922): "Ra'Tuk Screambringer's Jaw" (69921), "Noc Fleshfeasters Tail" (69920), "Mastruq Havocblade Blood" (69919), "Potameid Seaweed Strands" (69918). Produces "Lovine's Potion Bag" (69923). The combine does not fail.
43. abysmal/"Lovine Lemise", hand "Lovine's Potion Bag" (69923). Sets `paladin_epic_reiya` to `1`.
44. Summon "Foldable Medicine Bag" (17770) by casting "Unfold Medicine Bag".
45. Common item: Fine Potion Vial (95846). Listed in 15 zones.
46. Common item: Robust Shadow Essence (96911). Listed in 5 zones.
47. Loot "Sage Leaf" (14215) from "a Di'zok Herbalist" in `chardok`.
48. Loot "Sage Leaf" (14215) from "a Sarnak Herb Collector" in `chardok`.
49. Loot "Sage Leaf" (14215) from "an Apprentice Herbalist" in `chardok`.
50. Loot "Valerian Root" (14230) from "a Di'zok Herbalist" in `chardok`.
51. Loot "Valerian Root" (14230) from "a Sarnak Herb Collector" in `chardok`.
52. Loot "Valerian Root" (14230) from "an Apprentice Herbalist" in `chardok`.
53. Common item: Woundwart (16526). Listed in 9 zones.
54. Combine in "Foldable Medicine Bag" (17770): "Fine Potion Vial" (95846), "Robust Shadow Essence" (96911), "Sage Leaf" (14215), "Valerian Root" (14230), "Woundwart" (16526). Produces "Mist of the Breathless" (96937). Requires Alchemy, trivial 224.
55. abysmal/"Reiya The Pained", hand "Mist of the Breathless" (96937). Requires `paladin_epic_reiya` ==1. Gives "Reiya's Soulstone" (69924).
56. Spawns "Shade of Reiya the Pained" (284104) in `ferubi` on enter.
57. Loot "Soulstone Shard" (69943) from "Shade of Reiya the Pained".
58. Loot "Soulstone Shard" (69944) from "Vuranish Xxuro" in `vxed`.
59. Combine in "Reiya's Soulstone" (69924): "Soulstone Shard" (69943), "Soulstone Shard" (69944). Produces "Reiya's Soulstone" (69942). The combine does not fail.
60. Loot "Tainted Darksteel Sword" (29000) from "Keeper of the Tombs" in `hole`.
61. freeporteast/"Peasant Woman", say "I Will Take It". Gives "Bucket of Water" (29008).
62. freportw/"Peasant Woman", say "I Will Take It". Gives "Bucket of Water" (29008).
63. freeporteast/"Joshua", hand "Bucket of Water" (29008). Gives "Bucket of Pure Water" (29009).
64. freportw/"Joshua", hand "Bucket of Water" (29008). Gives "Bucket of Pure Water" (29009).
65. erudnext/"Reklon Gnallen", hand "Tainted Darksteel Sword" (29000) + "Bucket of Pure Water" (29009). Gives "Gleaming Crested Sword" (29003).
66. Loot "Tainted Darksteel Breastplate" (29001) from "Thought Destroyer" in `hateplaneb`.
67. kaladimb/"Nella Stonebraids", say "Jark". Gives "Cold Plate of Beef and Bread" (29007).
68. kaladimb/"Nella Stonebraids", say "Dinner". Gives "Cold Plate of Beef and Bread" (29007).
69. kaladimb/"Jark", hand "Cold Plate of Beef and Bread" (29007). Gives "Pure Crystal" (29006).
70. erudnext/"Reklon Gnallen", hand "Tainted Darksteel Breastplate" (29001) + "Pure Crystal" (29006). Gives "Gleaming Crested Breastplate" (29004).
71. Loot "Tainted Darksteel Shield" (29002) from "Kirak Vil" in `nektulos`.
72. felwithea/"Elia The Pure", hand "Tainted Darksteel Shield" (29002). Gives "Gleaming Crested Shield" (29005).
73. erudnext/"Reklon Gnallen", hand "Gleaming Crested Sword" (29003) + "Gleaming Crested Breastplate" (29004) + "Gleaming Crested Shield" (29005). Gives "Mark of Atonement" (29010).
74. No quest step gives Drom's Champagne (13829). The dump lists it in freeporteast, freporte, highpasshold.
75. freeporteast/"Tykar Renlin", hand "Drom's Champagne" (13829) + "Drom's Champagne" (13829) + "Drom's Champagne" (13829) + "Drom's Champagne" (13829). Gives "Bunker Cell #1" (12196).
76. freporte/"Tykar Renlin", hand "Drom's Champagne" (13829) + "Drom's Champagne" (13829) + "Drom's Champagne" (13829) + "Drom's Champagne" (13829). Gives "Bunker Cell #1" (12196).
77. Summon "Black Diamond of Nightmares" (29990) by casting "Imbue Nightmare".
78. poknowledge/"Aid Grimel", say "Versed In The Art Of Smithing". Gives "Filthy Breastplate" (15984).
79. Combine in "Mixing Bowl" (17906): "Celestial Solvent" (9731), "Words of Acquisition (Beza)" (11866). Produces "Celestial Essence" (9650). Requires Baking, trivial 15. The combine does not fail.
80. Combine in "Mixing Bowl" (17906): "Celestial Solvent" (9731), "Words of Burnishing" (11862). Produces "Celestial Essence" (9650). Requires Baking, trivial 15. The combine does not fail.
81. 67 other recipes also produce Celestial Essence (9650).
82. Common item: Jar of Acid (22133). Listed in 15 zones.
83. Combine in Brew Barrel (19): "Celestial Essence" (9650), "Jar of Acid" (22133). Produces "Acid Wash" (15987). Requires Brewing, trivial 151.
84. Combine in Forge (17): "Filthy Breastplate" (15984), "Acid Wash" (15987). Produces "Cleansed Breastplate" (15998). Requires Blacksmithing, trivial 227.
85. Common item: Mortar and Pestle (17904). Listed in 12 zones.
86. No quest step gives Sandstorm Pearl (29909). The dump lists it in bothunder.
87. Combine in "Mortar and Pestle" (17904): "Sandstorm Pearl" (29909). Produces "Powdered Sandstorm Pearl" (29520) x4. Requires Make Poison, trivial 255.
88. Common item: Firing Sheet (16906). Listed in 34 zones.
89. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
90. qeynos/"Wolten Grafe", say "Crush The Undead". Gives "Box For Bones" (17941).
91. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `steamfont`.
92. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `tox`.
93. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `toxxulia`.
94. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
95. toxxulia/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
96. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). The combine does not fail.
97. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
98. qeynos2/"Phin Esrinap", say "Supplies". Gives "Message to Konem" (18921).
99. qeytoqrg/"Konem Matse", hand "Message to Konem" (18921). Gives "Grathin's Invoice" (18922).
100. qeynos2/"Phin Esrinap", hand "Grathin's Invoice" (18922). Gives "Water Flask" (13006).
101. Say "Tm Devrak Death" to rujd/"Rujd".
102. Spawns "spawn chest with Heavy Orcish Prison Key" (245241).
103. Loot "Pod of Water" (13044) from "spawn chest with Heavy Orcish Prison Key".
104. Say "Tm Dokorel Death" to rujd/"Rujd".
105. Say "Tm Velrek Death" to rujd/"Rujd".
106. Say "Researcher Death" to rujg/"Rujg".
107. Spawns "A Barrel" (260015).
108. Loot "Pod of Water" (13044) from "A Barrel".
109. 3 other loot steps also yield Pod of Water (13044).
110. Forage "Pod of Water" (13044) in `ruja`.
111. Forage "Pod of Water" (13044) in `uqua`.
112. Forage "Pod of Water" (13044) in `yxtta`.
113. Combine in Brew Barrel (19): "Bottle of Aged Bloodwine" (51163), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aged Bloodwine" (51164). Requires Brewing, trivial 255.
114. Combine in Brew Barrel (19): "Bottle of Aldo's Bitter Ale" (75805), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aldo's Bitter Ale" (75811). Requires Brewing, trivial 15.
115. 17 other recipes also produce Bottle (16598).
116. Combine in Brew Barrel (19): "Pod of Water" (13044), "Bottle" (16598). Produces "Water Flask" (13006). Requires Brewing, trivial 21.
117. Combine in Pottery Wheel (21): "Water Flask" (13006), "Block of Clay" (16901). Produces "Small Block of Clay" (16900) x3. Requires Pottery, trivial 21.
118. Combine in Pottery Wheel (21): "Small Block of Clay" (16900), "Water Flask" (13006). Produces "Block of Clay" (16901). Requires Pottery, trivial 21.
119. Combine in Pottery Wheel (21): "Water Flask" (13006), "Large Block of Clay" (16902). Produces "Block of Clay" (16901) x2. Requires Pottery, trivial 21.
120. Combine in Pottery Wheel (21): "Block of Clay" (16901), "Water Flask" (13006). Produces "Large Block of Clay" (16902). Requires Pottery, trivial 21.
121. Common item: Large Bowl Sketch (16963). Listed in 29 zones.
122. Combine in Pottery Wheel (21): "Large Block of Clay" (16902), "Water Flask" (13006), "Large Bowl Sketch" (16963). Produces "Unfired Mixing Bowl" (16930). Requires Pottery, trivial 128.
123. Combine in Kiln (22): "Firing Sheet" (16906), "Unfired Mixing Bowl" (16930). Produces "Mixing Bowl" (17906). Requires Pottery, trivial 15.
124. Combine in "Mixing Bowl" (17906): "Sandstorm Pearl" (29909). Produces "Powdered Sandstorm Pearl" (29520) x4. Requires Baking. The combine does not fail.
125. Spawns "a Koka'Vor chieftain" (210236) in `postorms` on event_signal.
126. Loot "Storm Rider Blood" (29526) from "a Koka'Vor chieftain".
127. Loot "Storm Rider Blood" (29526) from "A stormrider" in `bothunder`.
128. Loot "Storm Rider Blood" (29526) from "Dolsoj Warrebs" in `bazaar`.
129. Loot "Storm Rider Blood" (29526) from "a Koka'Vor krovian" in `postorms`.
130. Loot "Storm Rider Blood" (29526) from "a Koka'Vor senvar" in `postorms`.
131. No quest step gives Drop of Pure Rain (29904). The dump lists it in bothunder.
132. Combine in Brew Barrel (19): "Powdered Sandstorm Pearl" (29520), "Storm Rider Blood" (29526), "Drop of Pure Rain" (29904). Produces "Hurricane Temper" (29533). Requires Brewing, trivial 135.
133. Combine in Forge (17): "Cleansed Breastplate" (15998), "Hurricane Temper" (29533). Produces "Tempered Breastplate" (15999). Requires Blacksmithing, trivial 229.
134. Combine in Forge (17): "Black Diamond of Nightmares" (29990), "Tempered Breastplate" (15999). Produces "Imbued Breastplate" (15985). Requires Blacksmithing 220. Trivial at 275.
135. poknowledge/"Aid Grimel", hand "Imbued Breastplate" (15985). Gives "Hardened Leather Signet" (16249).
136. poknowledge/"Aid Grimel", say "Skill In Brewing". Gives "Portable Drink Barrel" (17179).
137. Common item: Snake Scales (13070). Listed in 56 zones.
138. Combine in "Portable Drink Barrel" (17179): "Water Flask" (13006), "Snake Scales" (13070), "Bottle" (16598). Produces "Bog Juice" (16581). Requires Brewing, trivial 21.
139. Common item: Spit (17947). Listed in 34 zones.
140. Common item: Fire Beetle Eye (10307). Listed in 24 zones.
141. Spawns "Sepsis Rat" (45113) in `qcat` on event_death.
142. Loot "Rat Ears" (13072) from "Sepsis Rat".
143. Kill steamfont/"Diseased Female Rat". Spawns "A Young Plague Rat" (56086).
144. Loot "Rat Ears" (13072) from "A Young Plague Rat".
145. Kill steamfontmts/"Diseased Female Rat". Spawns "A Young Plague Rat" (448036).
146. Combine in "Spit" (17947): "Fire Beetle Eye" (10307), "Rat Ears" (13072). Produces "Edible Goo" (13498). Requires Baking, trivial 21.
147. freeporteast/"A Prisoner", hand "Bunker Cell #1" (12196) + "Edible Goo" (13498) + "Bog Juice" (16581). Gives "H. K. 102" (12143).
148. freportw/"A Prisoner", hand "Bunker Cell #1" (12196) + "Edible Goo" (13498) + "Bog Juice" (16581). Gives "H. K. 102" (12143).
149. highkeep/"Assistant Kiolna", hand "H. K. 102" (12143). Gives "Sealed Note" (18936).
150. paw/"Brother Hayle", hand "Sealed Note" (18936). Gives "Note" (18937).
151. southkarana/"Brother Hayle", hand "Sealed Note" (18936). Gives "Note" (18937).
152. Kill freportw/"Sir Lucan D-Lere". Spawns "Sir Lucan D'Lere" (9147).
153. Loot "Testimony of Truth" (18827) from "Sir Lucan D'Lere".
154. Loot "Testimony of Truth" (18827) from "Sir Lucan D'Lere" in `freeporteast`.
155. freeportwest/"Valeron Dushire", hand "Testimony of Truth" (18827). Gives "Brilliant Sword of Faith" (13947).
156. freportn/"Valeron Dushire", hand "Testimony of Truth" (18827). Gives "Brilliant Sword of Faith" (13947).
157. Hand "Token of Bravery" (12144) + "Token of Generosity" (13865) to freeportwest/"Merko Quetalis". Spawns "spawns Guard Willia" (383270). Loot "Token of Truth" (13866) from "spawns Guard Willia".
158. Hand "Token of Bravery" (12144) + "Token of Generosity" (13865) to freportn/"Merko Quetalis". Spawns "spawns Guard Willia" (8110). Loot "Token of Truth" (13866) from "spawns Guard Willia".
159. Loot "Token of Truth" (13866) from "Guard Willia".
160. freeportwest/"Merko Quetalis", hand "Token of Truth" (13866). Gives "Testimony" (18828).
161. freportn/"Merko Quetalis", hand "Token of Truth" (13866). Gives "Testimony" (18828).
162. Loot "Glowing Sword Hilt" (12197) from "Xicotl" in `mistmoore`.
163. paw/"Brother Hayle", hand "Glowing Sword Hilt" (12197) + "Brilliant Sword of Faith" (13947) + "Testimony" (18828) + "Note" (18937). Gives "SoulFire" (5504).
164. southkarana/"Brother Hayle", hand "Glowing Sword Hilt" (12197) + "Brilliant Sword of Faith" (13947) + "Testimony" (18828) + "Note" (18937). Gives "SoulFire" (5504).
165. airplane/"Inte Akera", hand "SoulFire" (5504). Gives "Inte's First Blessing" (18033).
166. lavastorm/"Ruathey", say "Bag". Gives "Nobleman's Bag" (17878).
167. Common item: Ghoul's Heart (2410). Listed in 8 zones.
168. No quest step gives Amstaf's Scroll (2411). The dump lists it in highkeep.
169. No quest step gives Blade of Nobility (2412). The dump lists it in butcher.
170. Loot "Hilt of the Nobleman" (2413) from "Ekeros" in `najena`.
171. Loot "Hilt of the Nobleman" (2413) from "A Skeleton" in `najena`.
172. Combine in "Nobleman's Bag" (17878): "Ghoul's Heart" (2410), "Amstaf's Scroll" (2411), "Blade of Nobility" (2412), "Hilt of the Nobleman" (2413). Produces "Ghoulbane" (5403). The combine does not fail.
173. airplane/"Inte Akera", hand "Ghoulbane" (5403). Gives "Inte's Second Blessing" (18034).
174. Hand "Miragul's Phylactery" (19072) to everfrost/"Lich Of Miragul". Spawns "Spawn Miragul" (30094). Loot "Miragul's Head" (19073) from "Spawn Miragul".
175. Loot "Miragul's Head" (19073) from "Miragul".
176. Hand "Miragul's Phylactery" (19072) to everfrost/"Lich Of Miragul". Spawns "Spawn Miragul" (30094). Loot "Miragul's Robe" (1254) from "Spawn Miragul".
177. Loot "Miragul's Robe" (1254) from "Miragul".
178. airplane/"Inte Akera", hand "Miragul's Robe" (1254) + "Inte's First Blessing" (18033) + "Inte's Second Blessing" (18034) + "Miragul's Head" (19073). Gives "Fiery Avenger" (11050).
179. fearplane/"Irak Altil", hand "Fiery Avenger" (11050) + "Mark of Atonement" (29010). Gives "Fiery Defender" (10099).
180. povalor/"Baltron Werters", say "Couragebringer". Sets `pre_pal` to `1`.
181. Requires `pre_pal` unset; no setter establishes this state.
182. povalor/"Baltron Werters", say "Couragebringer". Requires `pre_pal` unset. Gives "Baltron's Solvent" (69901).
183. sro/"Gilfal", hand "Baltron's Solvent" (69901). Requires `pre_pal` ==1. Gives "Gilfal's Scabbard" (69902).
184. Spawns "Neffiken Lord Kelek-Vor" (210229) in `postorms` on event_signal.
185. Loot "Broken Sword Piece" (69903) from "Neffiken Lord Kelek-Vor".
186. Loot "Broken Sword Piece" (69903) from "Neffiken Lord of Kelek'Vor".
187. Say "Control Timer" to hateplaneb/"Maestro".
188. Spawns "Maestro of Rancor" (186111).
189. Loot "Broken Sword Piece" (69904) from "Maestro of Rancor".
190. **Broken:** no event trigger found for `hateplaneb/maestro#timer:popmaestro`.
191. Spawns "Maestro of Rancor" (186111) after `hateplaneb/maestro#timer:popmaestro`.
192. Loot "Broken Sword Piece" (69905) from "Kaniz Painbringer" in `potorment`.
193. sro/"Gilfal", hand "Baltron's Solvent" (69901). Sets `pre_pal` to `2`.
194. Ground spawn of "Rune of Xor" (69909) in `potranquility`.
195. Ground spawn of "Rune of Yirno" (69908) in `mistmoore`.
196. Ground spawn of "Rune of Zota" (69907) in `scarlet`.
197. Ground spawn of "Rune Wilun" (69910) in `gunthak`.
198. everfrost/"Rombus", hand "Rune of Zota" (69907) + "Rune of Yirno" (69908) + "Rune of Xor" (69909) + "Rune Wilun" (69910). Requires `pre_pal` ==2. Gives "Broken Sword Piece" (69906).
199. Combine in "Gilfal's Scabbard" (69902): "Broken Sword Piece" (69903), "Broken Sword Piece" (69904), "Broken Sword Piece" (69905), "Broken Sword Piece" (69906). Produces "Fractured Couragebringer" (69911). The combine does not fail.
200. sro/"Gilfal", hand "Fractured Couragebringer" (69911). Sets `pre_pal` to `4`.
201. everfrost/"Rombus", hand "Rune of Zota" (69907) + "Rune of Yirno" (69908) + "Rune of Xor" (69909) + "Rune Wilun" (69910). Sets `pre_pal` to `3`.
202. sro/"Gilfal", hand "Fractured Couragebringer" (69911). Requires `pre_pal` ==3. Gives "Fractured Couragebringer" (69912).
203. povalor/"Baltron Werters", hand "Fractured Couragebringer" (69912). Requires `pre_pal` ==4. Gives "Couragebringer" (69913).
204. hohonora/"Irak Altil", say "Hail". Sets `paladin_epic` to `6`.
205. Spawns "Durunal the Cursebearer" (300087) in `wallofslaughter` on enter.
206. Loot "Dark and Twisted Sword" (69971) from "Durunal the Cursebearer".
207. hohonora/"Irak Altil", hand "Dark and Twisted Sword" (69971). Requires `paladin_epic` ==6. Gives "Dark and Twisted Sword" (69972).
208. Loot "Redis' Soulstone" (69983) from "Shade of Redis Linrok" in `dranikcatacombsa`.
209. Combine in "Dark and Twisted Sword" (69972): "Rithnok's Soulstone" (69941), "Drema's Soulstone" (69952), "Reiya's Soulstone" (69942), "Redis' Soulstone" (69983). Produces "Redemption" (64031). The combine does not fail.
210. hohonora/"Irak Altil", say "Tell Me About Your Master". Sets `paladin_epic` to `9`.
211. erudnint/"Josper Kenshed", say "Collect Component". Gives "Empty Bag" (17944).
212. halas/"Lysbith Mcnaff", say "Protect The Pass". Gives "Empty Bag" (17944).
213. Loot "Goblin Ice Necklace" (13897) from "Redwind" in `everfrost`.
214. Loot "Goblin Ice Necklace" (13897) from "An Ice Goblin Scout" in `everfrost`.
215. Loot "Goblin Ice Necklace" (13897) from "An Ice Goblin Whelp" in `everfrost`.
216. Loot "Goblin Ice Necklace" (13897) from "An Icy Orc" in `everfrost`.
217. Loot "Goblin Ice Necklace" (13897) from "Ice Goblin Diver" in `everfrost`.
218. Combine in "Empty Bag" (17944): "Goblin Ice Necklace" (13897). Produces "Bag of Ice Necklaces" (13898). The combine does not fail.
219. halas/"Lysbith Mcnaff", hand "Bag of Ice Necklaces" (13898). Gives "Iron Ration" (13005).
220. Common item: Gnoll Fang (13915). Listed in 5 zones.
221. halas/"Lysbith Mcnaff", hand "Gnoll Fang" (13915) + "Gnoll Fang" (13915) + "Gnoll Fang" (13915). Gives "Iron Ration" (13005).
222. Requires `halloween_draykey_rations` unset; no setter establishes this state.
223. kithicor/"Old Man Draykey", say "Instructions". Requires `halloween_draykey_rations` unset. Gives "Iron Ration" (13005).
224. commons/"Kizdean Gix", say "Messages For Neriak". Gives "Sealed Letter" (18889).
225. neriakc/"Loveal S-Nez", hand "Sealed Letter" (18889). Gives "Iron Ration" (13005).
226. Loot "Cask" (16580) from "Tugog Grigol" in `rathemtn`.
227. Common item: Hops (16591). Listed in 31 zones.
228. Common item: Malt (16595). Listed in 30 zones.
229. Common item: Yeast (16596). Listed in 30 zones.
230. Combine in "Portable Drink Barrel" (17179): "Cask" (16580), "Hops" (16591), "Malt" (16595), "Yeast" (16596). Produces "Mead" (13008). Requires Brewing, trivial 41.
231. erudnext/"Reklon Gnallen", hand "Iron Ration" (13005) + "Mead" (13008). Requires `paladin_epic` ==9. Gives "Erudin Prayer Bead" (69965).
232. Summon "Quiver of Marr" (17307) by casting "Quiver of Marr".
233. rathemtn/"Shin Master Grubbus", hand "Quiver of Marr" (17307). Requires `paladin_epic` ==9. Gives "Gukta Prayer Bead" (69964).
234. Common item: Barley (16590). Listed in 28 zones.
235. Combine in "Medicine Bag" (17901): "Hand-Formed Bottle" (45232), "Ensnaring Concoction V" (45236). Produces "Empty Vial" (10062), "Cork" (16851), "Formed Ensnaring Concoction V" (45258). Requires Alchemy, trivial 41.
236. Combine in Brew Barrel (19): "Bottle of Aged Bloodwine" (51163), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aged Bloodwine" (51164). Requires Brewing, trivial 255.
237. 11 other recipes also produce Cork (16851).
238. Combine in "Portable Drink Barrel" (17179): "Water Flask" (13006), "Celestial Essence" (9650). Produces "Purified Water" (12607). Requires Brewing, trivial 58.
239. Combine in "Tracker's Water Extractor" (17987): "Purification Tablet" (12630), "Water Reed" (12778). Produces "Purified Water" (12607) x3. Requires Pottery. The combine does not fail.
240. 3 other recipes also produce Purified Water (12607).
241. Forage "Sand Verbena" (65582) in `taka`.
242. Forage "Sand Verbena" (65582) in `takb`.
243. Forage "Sand Verbena" (65582) in `takc`.
244. Forage "Sand Verbena" (65582) in `takd`.
245. Forage "Sand Verbena" (65582) in `take`.
246. Forage "Sand Verbena" (65582) in `takf`.
247. Forage "Sand Verbena" (65582) in `takg`.
248. Forage "Sand Verbena" (65582) in `takh`.
249. Forage "Sand Verbena" (65582) in `taki`.
250. Forage "Sand Verbena" (65582) in `takj`.
251. Combine in Brew Barrel (19): "Barley" (16590), "Bottle" (16598), "Cork" (16851), "Hops" (16591), "Purified Water" (12607), "Sand Verbena" (65582), "Yeast" (16596). Produces "Bottle of Double Brewed Double Dry Stout" (51157). Requires Brewing, trivial 226.
252. kaladimb/"Datur Nightseer", hand "Bottle of Double Brewed Double Dry Stout" (51157). Requires `paladin_epic` ==9. Gives "Kaladim Prayer Bead" (69963).
253. felwithea/"General Jyleel", hand platinum:1000. Requires `paladin_epic` ==9. Gives "Felwithe Prayer Bead" (69962).
254. Ground spawn of "Freeport Prayer Bead" (69961) in `freeportwest`.
255. Ground spawn of "Freeport Prayer Bead" (69961) in `freportn`.
256. qeynos2/"Ziska Ironforge", hand platinum:500. Requires `paladin_epic` ==9. Gives "Qeynos Prayer Bead" (69960).
257. Combine in "Unfilled Set of Prayer Beads" (69968): "Rivervale Prayer Bead" (69967), "Ak'anon Prayer Bead" (69966), "Erudin Prayer Bead" (69965), "Gukta Prayer Bead" (69964), "Kaladim Prayer Bead" (69963), "Felwithe Prayer Bead" (69962), "Freeport Prayer Bead" (69961), "Qeynos Prayer Bead" (69960). Produces "Set of Prayer Beads" (69969). The combine does not fail.
258. dranikhollowsc/"Anetal", hand "Set of Prayer Beads" (69969). Sets `paladin_epic_hollowc` to `2`.
259. natimbi/"Kemik Arulon", hand "Set of Prayer Beads" (69969). Sets `paladin_epic_hollowc` to `1`.
260. natimbi/"Kemik Arulon", say "Hail". Requires `paladin_epic_hollowc` ==2. Requires `paladin_epic_hollowc` ==1. Gives "Token of Compassion" (69953).
261. Requires `pal_chest_keel` unset; no setter establishes this state.
262. oasis/"Paladin Epic", say "Hail". Requires `pal_chest_keel` unset. Gives "Keelee's Brooch" (69982).
263. oasis/"Paladin Epic", say "Keelee Say". Gives "Keelee's Brooch" (69982).
264. sro/"Instructor Maerceci", hand "Keelee's Brooch" (69982). Gives "Token of Chivalry" (69954).
265. Loot "Valdoon Kel'Novar's Heart" (69981) from "Valdoon Kel'Novar" in `mmcc`.
266. felwithea/"Galrun Starforge", hand "Valdoon Kel'Novar's Heart" (69981). Gives "Token of Cleansing" (69956).
267. provinggrounds/"Pashia Clouddancer", say "Note". Gives "Note from Pashia" (69973).
268. nedaria/"Duram Firechaser", hand "Note from Pashia" (69973). Gives "Token of Heroism" (69955).
269. Say "Check Lorb" to anguish/"Zone Status".
270. Spawns "Orb of Discordant Energy" (317087).
271. Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy".
272. Say "Check Uorb" to anguish/"Zone Status".
273. Say "Check Amv Chest" to anguish/"Zone Status".
274. Spawns "Ornate Chest" (317112).
275. Loot "Globe of Discordant Energy" (47100) from "Ornate Chest".
276. 2 other loot steps also yield Globe of Discordant Energy (47100).
277. Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy" in `anguish`.
278. Loot "Globe of Discordant Energy" (47100) from "Overlords Chest".
279. airplane/"Inte Akera", hand "Globe of Discordant Energy" (47100). Gives "Scabbard of the Righteous" (69959).

### "Token of Loyalty" (69958)

1. qeynos2/"Camlend Serbold", say "Gem". Gives "Unfilled Set of Prayer Beads" (69968).
2. rivervale/"Kaya Cloudfoot", say "Different About It". Gives "Note from Kaya" (69970).
3. rivervale/"Deputy Cheel", hand "Note from Kaya" (69970). Gives "Rivervale Prayer Bead" (69967).
4. **Broken:** nothing in the graph gives, loots, spawns, or combines Ak`anon Prayer Bead (69966).
5. Say "Hail" to skyfire/"Dry Sapara".
6. Spawns "Rithnok the Tormented" (91193).
7. Loot "Rithnok's Soulstone" (69935) from "Rithnok the Tormented".
8. skyfire/"Dry Sapara", hand "Rithnok's Soulstone" (69935). Gives "Rithnok's Soulstone" (69936).
9. Ground spawn of "Soulstone Shard" (69937) in `draniksscar`.
10. Ground spawn of "Soulstone Shard" (69938) in `bloodfields`.
11. Ground spawn of "Soulstone Shard" (69939) in `causeway`.
12. Ground spawn of "Soulstone Shard" (69940) in `dranik`.
13. Combine in "Rithnok's Soulstone" (69936): "Soulstone Shard" (69937), "Soulstone Shard" (69938), "Soulstone Shard" (69939), "Soulstone Shard" (69940). Produces "Rithnok's Soulstone" (69941). The combine does not fail.
14. Hand "Enchanted Bone Powder" (69949) to letalis/"Drema Young". Spawns "Drema Young" (169128). Loot "Drema's Soulstone" (69928) from "Drema Young".
15. Loot "Drema's Soulstone" (69928) from "Drema Young".
16. Loot "Drema's Soulstone" (69928) from "Drema Young" in `letalis`.
17. Loot "Soulstone Shard" (69950) from "Coterie Corruptor" in `tenebrous`.
18. Say "Mujaki Death" to ponightmare/"Mujaki".
19. Spawns "Shade of Mujaki the Devourer" (204081).
20. Loot "Soulstone Shard" (69951) from "Shade of Mujaki the Devourer".
21. Combine in "Drema's Soulstone" (69928): "Soulstone Shard" (69950), "Soulstone Shard" (69951). Produces "Drema's Soulstone" (69952). The combine does not fail.
22. freporte/"Brunar Rankin", say "Hail". Sets `paladin_epic` to `3`.
23. global/"Global Player", combine recipe 19880. Sets `paladin_epic` to `8`.
24. Spawns "A Corrupted Koalindl" (69141) in `oot` on event_fish_success.
25. Loot "Corrupted Koalindl's Heart" (69929) from "A Corrupted Koalindl".
26. Spawns "A Corrupted Koalindl" (224432) in `gunthak` on event_fish_success.
27. Loot "Corrupted Koalindl's Heart" (69930) from "A Corrupted Koalindl".
28. Spawns "A Corrupted Koalindl" (93306) in `overthere` on event_fish_success.
29. Loot "Corrupted Koalindl's Heart" (69931) from "A Corrupted Koalindl".
30. Spawns "A Corrupted Koalindl" (182150) in `nedaria` on event_fish_success.
31. Loot "Corrupted Koalindl's Heart" (69932) from "A Corrupted Koalindl".
32. qeynos2/"Enic Ruklin", hand "Corrupted Koalindl's Heart" (69929) + "Corrupted Koalindl's Heart" (69930) + "Corrupted Koalindl's Heart" (69931) + "Corrupted Koalindl's Heart" (69932). Sets `paladin_epic` to `4`.
33. dawnshroud/"Mikhal Young", say "Find Anything". Requires `paladin_epic` ==4. Gives "Drema's Locket" (69945).
34. letalis/"Drema Young", hand "Drema's Locket" (69945). Requires `paladin_epic` set. Requires `paladin_epic` >=4. Gives "Drema's Fingerbone" (69946).
35. dawnshroud/"Mikhal Young", hand "Drema's Fingerbone" (69946). Sets `paladin_epic` to `5`.
36. abysmal/"Lovine Lemise", say "Ingredients". Requires `paladin_epic` ==5. Gives "Lovine's Potion Bag" (69922).
37. No quest step gives Ra`Tuk Screambringer's Jaw (69921). The dump lists it in barindu.
38. Loot "Noc Fleshfeasters Tail" (69920) from "A Noc Fleshfeaster" in `riwwi`.
39. Loot "Mastruq Havocblade Blood" (69919) from "A Mastruq Havocblade" in `qinimi`.
40. Loot "Mastruq Havocblade Blood" (69919) from "A Mastruq Warfiend" in `qinimi`.
41. Loot "Potameid Seaweed Strands" (69918) from "An Entrapped Potameid" in `natimbi`.
42. Combine in "Lovine's Potion Bag" (69922): "Ra'Tuk Screambringer's Jaw" (69921), "Noc Fleshfeasters Tail" (69920), "Mastruq Havocblade Blood" (69919), "Potameid Seaweed Strands" (69918). Produces "Lovine's Potion Bag" (69923). The combine does not fail.
43. abysmal/"Lovine Lemise", hand "Lovine's Potion Bag" (69923). Sets `paladin_epic_reiya` to `1`.
44. Summon "Foldable Medicine Bag" (17770) by casting "Unfold Medicine Bag".
45. Common item: Fine Potion Vial (95846). Listed in 15 zones.
46. Common item: Robust Shadow Essence (96911). Listed in 5 zones.
47. Loot "Sage Leaf" (14215) from "a Di'zok Herbalist" in `chardok`.
48. Loot "Sage Leaf" (14215) from "a Sarnak Herb Collector" in `chardok`.
49. Loot "Sage Leaf" (14215) from "an Apprentice Herbalist" in `chardok`.
50. Loot "Valerian Root" (14230) from "a Di'zok Herbalist" in `chardok`.
51. Loot "Valerian Root" (14230) from "a Sarnak Herb Collector" in `chardok`.
52. Loot "Valerian Root" (14230) from "an Apprentice Herbalist" in `chardok`.
53. Common item: Woundwart (16526). Listed in 9 zones.
54. Combine in "Foldable Medicine Bag" (17770): "Fine Potion Vial" (95846), "Robust Shadow Essence" (96911), "Sage Leaf" (14215), "Valerian Root" (14230), "Woundwart" (16526). Produces "Mist of the Breathless" (96937). Requires Alchemy, trivial 224.
55. abysmal/"Reiya The Pained", hand "Mist of the Breathless" (96937). Requires `paladin_epic_reiya` ==1. Gives "Reiya's Soulstone" (69924).
56. Spawns "Shade of Reiya the Pained" (284104) in `ferubi` on enter.
57. Loot "Soulstone Shard" (69943) from "Shade of Reiya the Pained".
58. Loot "Soulstone Shard" (69944) from "Vuranish Xxuro" in `vxed`.
59. Combine in "Reiya's Soulstone" (69924): "Soulstone Shard" (69943), "Soulstone Shard" (69944). Produces "Reiya's Soulstone" (69942). The combine does not fail.
60. Loot "Tainted Darksteel Sword" (29000) from "Keeper of the Tombs" in `hole`.
61. freeporteast/"Peasant Woman", say "I Will Take It". Gives "Bucket of Water" (29008).
62. freportw/"Peasant Woman", say "I Will Take It". Gives "Bucket of Water" (29008).
63. freeporteast/"Joshua", hand "Bucket of Water" (29008). Gives "Bucket of Pure Water" (29009).
64. freportw/"Joshua", hand "Bucket of Water" (29008). Gives "Bucket of Pure Water" (29009).
65. erudnext/"Reklon Gnallen", hand "Tainted Darksteel Sword" (29000) + "Bucket of Pure Water" (29009). Gives "Gleaming Crested Sword" (29003).
66. Loot "Tainted Darksteel Breastplate" (29001) from "Thought Destroyer" in `hateplaneb`.
67. kaladimb/"Nella Stonebraids", say "Jark". Gives "Cold Plate of Beef and Bread" (29007).
68. kaladimb/"Nella Stonebraids", say "Dinner". Gives "Cold Plate of Beef and Bread" (29007).
69. kaladimb/"Jark", hand "Cold Plate of Beef and Bread" (29007). Gives "Pure Crystal" (29006).
70. erudnext/"Reklon Gnallen", hand "Tainted Darksteel Breastplate" (29001) + "Pure Crystal" (29006). Gives "Gleaming Crested Breastplate" (29004).
71. Loot "Tainted Darksteel Shield" (29002) from "Kirak Vil" in `nektulos`.
72. felwithea/"Elia The Pure", hand "Tainted Darksteel Shield" (29002). Gives "Gleaming Crested Shield" (29005).
73. erudnext/"Reklon Gnallen", hand "Gleaming Crested Sword" (29003) + "Gleaming Crested Breastplate" (29004) + "Gleaming Crested Shield" (29005). Gives "Mark of Atonement" (29010).
74. No quest step gives Drom's Champagne (13829). The dump lists it in freeporteast, freporte, highpasshold.
75. freeporteast/"Tykar Renlin", hand "Drom's Champagne" (13829) + "Drom's Champagne" (13829) + "Drom's Champagne" (13829) + "Drom's Champagne" (13829). Gives "Bunker Cell #1" (12196).
76. freporte/"Tykar Renlin", hand "Drom's Champagne" (13829) + "Drom's Champagne" (13829) + "Drom's Champagne" (13829) + "Drom's Champagne" (13829). Gives "Bunker Cell #1" (12196).
77. Summon "Black Diamond of Nightmares" (29990) by casting "Imbue Nightmare".
78. poknowledge/"Aid Grimel", say "Versed In The Art Of Smithing". Gives "Filthy Breastplate" (15984).
79. Combine in "Mixing Bowl" (17906): "Celestial Solvent" (9731), "Words of Acquisition (Beza)" (11866). Produces "Celestial Essence" (9650). Requires Baking, trivial 15. The combine does not fail.
80. Combine in "Mixing Bowl" (17906): "Celestial Solvent" (9731), "Words of Burnishing" (11862). Produces "Celestial Essence" (9650). Requires Baking, trivial 15. The combine does not fail.
81. 67 other recipes also produce Celestial Essence (9650).
82. Common item: Jar of Acid (22133). Listed in 15 zones.
83. Combine in Brew Barrel (19): "Celestial Essence" (9650), "Jar of Acid" (22133). Produces "Acid Wash" (15987). Requires Brewing, trivial 151.
84. Combine in Forge (17): "Filthy Breastplate" (15984), "Acid Wash" (15987). Produces "Cleansed Breastplate" (15998). Requires Blacksmithing, trivial 227.
85. Common item: Mortar and Pestle (17904). Listed in 12 zones.
86. No quest step gives Sandstorm Pearl (29909). The dump lists it in bothunder.
87. Combine in "Mortar and Pestle" (17904): "Sandstorm Pearl" (29909). Produces "Powdered Sandstorm Pearl" (29520) x4. Requires Make Poison, trivial 255.
88. Common item: Firing Sheet (16906). Listed in 34 zones.
89. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
90. qeynos/"Wolten Grafe", say "Crush The Undead". Gives "Box For Bones" (17941).
91. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `steamfont`.
92. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `tox`.
93. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `toxxulia`.
94. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
95. toxxulia/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
96. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). The combine does not fail.
97. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
98. qeynos2/"Phin Esrinap", say "Supplies". Gives "Message to Konem" (18921).
99. qeytoqrg/"Konem Matse", hand "Message to Konem" (18921). Gives "Grathin's Invoice" (18922).
100. qeynos2/"Phin Esrinap", hand "Grathin's Invoice" (18922). Gives "Water Flask" (13006).
101. Say "Tm Devrak Death" to rujd/"Rujd".
102. Spawns "spawn chest with Heavy Orcish Prison Key" (245241).
103. Loot "Pod of Water" (13044) from "spawn chest with Heavy Orcish Prison Key".
104. Say "Tm Dokorel Death" to rujd/"Rujd".
105. Say "Tm Velrek Death" to rujd/"Rujd".
106. Say "Researcher Death" to rujg/"Rujg".
107. Spawns "A Barrel" (260015).
108. Loot "Pod of Water" (13044) from "A Barrel".
109. 3 other loot steps also yield Pod of Water (13044).
110. Forage "Pod of Water" (13044) in `ruja`.
111. Forage "Pod of Water" (13044) in `uqua`.
112. Forage "Pod of Water" (13044) in `yxtta`.
113. Combine in Brew Barrel (19): "Bottle of Aged Bloodwine" (51163), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aged Bloodwine" (51164). Requires Brewing, trivial 255.
114. Combine in Brew Barrel (19): "Bottle of Aldo's Bitter Ale" (75805), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aldo's Bitter Ale" (75811). Requires Brewing, trivial 15.
115. 17 other recipes also produce Bottle (16598).
116. Combine in Brew Barrel (19): "Pod of Water" (13044), "Bottle" (16598). Produces "Water Flask" (13006). Requires Brewing, trivial 21.
117. Combine in Pottery Wheel (21): "Water Flask" (13006), "Block of Clay" (16901). Produces "Small Block of Clay" (16900) x3. Requires Pottery, trivial 21.
118. Combine in Pottery Wheel (21): "Small Block of Clay" (16900), "Water Flask" (13006). Produces "Block of Clay" (16901). Requires Pottery, trivial 21.
119. Combine in Pottery Wheel (21): "Water Flask" (13006), "Large Block of Clay" (16902). Produces "Block of Clay" (16901) x2. Requires Pottery, trivial 21.
120. Combine in Pottery Wheel (21): "Block of Clay" (16901), "Water Flask" (13006). Produces "Large Block of Clay" (16902). Requires Pottery, trivial 21.
121. Common item: Large Bowl Sketch (16963). Listed in 29 zones.
122. Combine in Pottery Wheel (21): "Large Block of Clay" (16902), "Water Flask" (13006), "Large Bowl Sketch" (16963). Produces "Unfired Mixing Bowl" (16930). Requires Pottery, trivial 128.
123. Combine in Kiln (22): "Firing Sheet" (16906), "Unfired Mixing Bowl" (16930). Produces "Mixing Bowl" (17906). Requires Pottery, trivial 15.
124. Combine in "Mixing Bowl" (17906): "Sandstorm Pearl" (29909). Produces "Powdered Sandstorm Pearl" (29520) x4. Requires Baking. The combine does not fail.
125. Spawns "a Koka'Vor chieftain" (210236) in `postorms` on event_signal.
126. Loot "Storm Rider Blood" (29526) from "a Koka'Vor chieftain".
127. Loot "Storm Rider Blood" (29526) from "A stormrider" in `bothunder`.
128. Loot "Storm Rider Blood" (29526) from "Dolsoj Warrebs" in `bazaar`.
129. Loot "Storm Rider Blood" (29526) from "a Koka'Vor krovian" in `postorms`.
130. Loot "Storm Rider Blood" (29526) from "a Koka'Vor senvar" in `postorms`.
131. No quest step gives Drop of Pure Rain (29904). The dump lists it in bothunder.
132. Combine in Brew Barrel (19): "Powdered Sandstorm Pearl" (29520), "Storm Rider Blood" (29526), "Drop of Pure Rain" (29904). Produces "Hurricane Temper" (29533). Requires Brewing, trivial 135.
133. Combine in Forge (17): "Cleansed Breastplate" (15998), "Hurricane Temper" (29533). Produces "Tempered Breastplate" (15999). Requires Blacksmithing, trivial 229.
134. Combine in Forge (17): "Black Diamond of Nightmares" (29990), "Tempered Breastplate" (15999). Produces "Imbued Breastplate" (15985). Requires Blacksmithing 220. Trivial at 275.
135. poknowledge/"Aid Grimel", hand "Imbued Breastplate" (15985). Gives "Hardened Leather Signet" (16249).
136. poknowledge/"Aid Grimel", say "Skill In Brewing". Gives "Portable Drink Barrel" (17179).
137. Common item: Snake Scales (13070). Listed in 56 zones.
138. Combine in "Portable Drink Barrel" (17179): "Water Flask" (13006), "Snake Scales" (13070), "Bottle" (16598). Produces "Bog Juice" (16581). Requires Brewing, trivial 21.
139. Common item: Spit (17947). Listed in 34 zones.
140. Common item: Fire Beetle Eye (10307). Listed in 24 zones.
141. Spawns "Sepsis Rat" (45113) in `qcat` on event_death.
142. Loot "Rat Ears" (13072) from "Sepsis Rat".
143. Kill steamfont/"Diseased Female Rat". Spawns "A Young Plague Rat" (56086).
144. Loot "Rat Ears" (13072) from "A Young Plague Rat".
145. Kill steamfontmts/"Diseased Female Rat". Spawns "A Young Plague Rat" (448036).
146. Combine in "Spit" (17947): "Fire Beetle Eye" (10307), "Rat Ears" (13072). Produces "Edible Goo" (13498). Requires Baking, trivial 21.
147. freeporteast/"A Prisoner", hand "Bunker Cell #1" (12196) + "Edible Goo" (13498) + "Bog Juice" (16581). Gives "H. K. 102" (12143).
148. freportw/"A Prisoner", hand "Bunker Cell #1" (12196) + "Edible Goo" (13498) + "Bog Juice" (16581). Gives "H. K. 102" (12143).
149. highkeep/"Assistant Kiolna", hand "H. K. 102" (12143). Gives "Sealed Note" (18936).
150. paw/"Brother Hayle", hand "Sealed Note" (18936). Gives "Note" (18937).
151. southkarana/"Brother Hayle", hand "Sealed Note" (18936). Gives "Note" (18937).
152. Kill freportw/"Sir Lucan D-Lere". Spawns "Sir Lucan D'Lere" (9147).
153. Loot "Testimony of Truth" (18827) from "Sir Lucan D'Lere".
154. Loot "Testimony of Truth" (18827) from "Sir Lucan D'Lere" in `freeporteast`.
155. freeportwest/"Valeron Dushire", hand "Testimony of Truth" (18827). Gives "Brilliant Sword of Faith" (13947).
156. freportn/"Valeron Dushire", hand "Testimony of Truth" (18827). Gives "Brilliant Sword of Faith" (13947).
157. Hand "Token of Bravery" (12144) + "Token of Generosity" (13865) to freeportwest/"Merko Quetalis". Spawns "spawns Guard Willia" (383270). Loot "Token of Truth" (13866) from "spawns Guard Willia".
158. Hand "Token of Bravery" (12144) + "Token of Generosity" (13865) to freportn/"Merko Quetalis". Spawns "spawns Guard Willia" (8110). Loot "Token of Truth" (13866) from "spawns Guard Willia".
159. Loot "Token of Truth" (13866) from "Guard Willia".
160. freeportwest/"Merko Quetalis", hand "Token of Truth" (13866). Gives "Testimony" (18828).
161. freportn/"Merko Quetalis", hand "Token of Truth" (13866). Gives "Testimony" (18828).
162. Loot "Glowing Sword Hilt" (12197) from "Xicotl" in `mistmoore`.
163. paw/"Brother Hayle", hand "Glowing Sword Hilt" (12197) + "Brilliant Sword of Faith" (13947) + "Testimony" (18828) + "Note" (18937). Gives "SoulFire" (5504).
164. southkarana/"Brother Hayle", hand "Glowing Sword Hilt" (12197) + "Brilliant Sword of Faith" (13947) + "Testimony" (18828) + "Note" (18937). Gives "SoulFire" (5504).
165. airplane/"Inte Akera", hand "SoulFire" (5504). Gives "Inte's First Blessing" (18033).
166. lavastorm/"Ruathey", say "Bag". Gives "Nobleman's Bag" (17878).
167. Common item: Ghoul's Heart (2410). Listed in 8 zones.
168. No quest step gives Amstaf's Scroll (2411). The dump lists it in highkeep.
169. No quest step gives Blade of Nobility (2412). The dump lists it in butcher.
170. Loot "Hilt of the Nobleman" (2413) from "Ekeros" in `najena`.
171. Loot "Hilt of the Nobleman" (2413) from "A Skeleton" in `najena`.
172. Combine in "Nobleman's Bag" (17878): "Ghoul's Heart" (2410), "Amstaf's Scroll" (2411), "Blade of Nobility" (2412), "Hilt of the Nobleman" (2413). Produces "Ghoulbane" (5403). The combine does not fail.
173. airplane/"Inte Akera", hand "Ghoulbane" (5403). Gives "Inte's Second Blessing" (18034).
174. Hand "Miragul's Phylactery" (19072) to everfrost/"Lich Of Miragul". Spawns "Spawn Miragul" (30094). Loot "Miragul's Head" (19073) from "Spawn Miragul".
175. Loot "Miragul's Head" (19073) from "Miragul".
176. Hand "Miragul's Phylactery" (19072) to everfrost/"Lich Of Miragul". Spawns "Spawn Miragul" (30094). Loot "Miragul's Robe" (1254) from "Spawn Miragul".
177. Loot "Miragul's Robe" (1254) from "Miragul".
178. airplane/"Inte Akera", hand "Miragul's Robe" (1254) + "Inte's First Blessing" (18033) + "Inte's Second Blessing" (18034) + "Miragul's Head" (19073). Gives "Fiery Avenger" (11050).
179. fearplane/"Irak Altil", hand "Fiery Avenger" (11050) + "Mark of Atonement" (29010). Gives "Fiery Defender" (10099).
180. povalor/"Baltron Werters", say "Couragebringer". Sets `pre_pal` to `1`.
181. Requires `pre_pal` unset; no setter establishes this state.
182. povalor/"Baltron Werters", say "Couragebringer". Requires `pre_pal` unset. Gives "Baltron's Solvent" (69901).
183. sro/"Gilfal", hand "Baltron's Solvent" (69901). Requires `pre_pal` ==1. Gives "Gilfal's Scabbard" (69902).
184. Spawns "Neffiken Lord Kelek-Vor" (210229) in `postorms` on event_signal.
185. Loot "Broken Sword Piece" (69903) from "Neffiken Lord Kelek-Vor".
186. Loot "Broken Sword Piece" (69903) from "Neffiken Lord of Kelek'Vor".
187. Say "Control Timer" to hateplaneb/"Maestro".
188. Spawns "Maestro of Rancor" (186111).
189. Loot "Broken Sword Piece" (69904) from "Maestro of Rancor".
190. **Broken:** no event trigger found for `hateplaneb/maestro#timer:popmaestro`.
191. Spawns "Maestro of Rancor" (186111) after `hateplaneb/maestro#timer:popmaestro`.
192. Loot "Broken Sword Piece" (69905) from "Kaniz Painbringer" in `potorment`.
193. sro/"Gilfal", hand "Baltron's Solvent" (69901). Sets `pre_pal` to `2`.
194. Ground spawn of "Rune of Xor" (69909) in `potranquility`.
195. Ground spawn of "Rune of Yirno" (69908) in `mistmoore`.
196. Ground spawn of "Rune of Zota" (69907) in `scarlet`.
197. Ground spawn of "Rune Wilun" (69910) in `gunthak`.
198. everfrost/"Rombus", hand "Rune of Zota" (69907) + "Rune of Yirno" (69908) + "Rune of Xor" (69909) + "Rune Wilun" (69910). Requires `pre_pal` ==2. Gives "Broken Sword Piece" (69906).
199. Combine in "Gilfal's Scabbard" (69902): "Broken Sword Piece" (69903), "Broken Sword Piece" (69904), "Broken Sword Piece" (69905), "Broken Sword Piece" (69906). Produces "Fractured Couragebringer" (69911). The combine does not fail.
200. sro/"Gilfal", hand "Fractured Couragebringer" (69911). Sets `pre_pal` to `4`.
201. everfrost/"Rombus", hand "Rune of Zota" (69907) + "Rune of Yirno" (69908) + "Rune of Xor" (69909) + "Rune Wilun" (69910). Sets `pre_pal` to `3`.
202. sro/"Gilfal", hand "Fractured Couragebringer" (69911). Requires `pre_pal` ==3. Gives "Fractured Couragebringer" (69912).
203. povalor/"Baltron Werters", hand "Fractured Couragebringer" (69912). Requires `pre_pal` ==4. Gives "Couragebringer" (69913).
204. hohonora/"Irak Altil", say "Hail". Sets `paladin_epic` to `6`.
205. Spawns "Durunal the Cursebearer" (300087) in `wallofslaughter` on enter.
206. Loot "Dark and Twisted Sword" (69971) from "Durunal the Cursebearer".
207. hohonora/"Irak Altil", hand "Dark and Twisted Sword" (69971). Requires `paladin_epic` ==6. Gives "Dark and Twisted Sword" (69972).
208. Loot "Redis' Soulstone" (69983) from "Shade of Redis Linrok" in `dranikcatacombsa`.
209. Combine in "Dark and Twisted Sword" (69972): "Rithnok's Soulstone" (69941), "Drema's Soulstone" (69952), "Reiya's Soulstone" (69942), "Redis' Soulstone" (69983). Produces "Redemption" (64031). The combine does not fail.
210. hohonora/"Irak Altil", say "Tell Me About Your Master". Sets `paladin_epic` to `9`.
211. erudnint/"Josper Kenshed", say "Collect Component". Gives "Empty Bag" (17944).
212. halas/"Lysbith Mcnaff", say "Protect The Pass". Gives "Empty Bag" (17944).
213. Loot "Goblin Ice Necklace" (13897) from "Redwind" in `everfrost`.
214. Loot "Goblin Ice Necklace" (13897) from "An Ice Goblin Scout" in `everfrost`.
215. Loot "Goblin Ice Necklace" (13897) from "An Ice Goblin Whelp" in `everfrost`.
216. Loot "Goblin Ice Necklace" (13897) from "An Icy Orc" in `everfrost`.
217. Loot "Goblin Ice Necklace" (13897) from "Ice Goblin Diver" in `everfrost`.
218. Combine in "Empty Bag" (17944): "Goblin Ice Necklace" (13897). Produces "Bag of Ice Necklaces" (13898). The combine does not fail.
219. halas/"Lysbith Mcnaff", hand "Bag of Ice Necklaces" (13898). Gives "Iron Ration" (13005).
220. Common item: Gnoll Fang (13915). Listed in 5 zones.
221. halas/"Lysbith Mcnaff", hand "Gnoll Fang" (13915) + "Gnoll Fang" (13915) + "Gnoll Fang" (13915). Gives "Iron Ration" (13005).
222. Requires `halloween_draykey_rations` unset; no setter establishes this state.
223. kithicor/"Old Man Draykey", say "Instructions". Requires `halloween_draykey_rations` unset. Gives "Iron Ration" (13005).
224. commons/"Kizdean Gix", say "Messages For Neriak". Gives "Sealed Letter" (18889).
225. neriakc/"Loveal S-Nez", hand "Sealed Letter" (18889). Gives "Iron Ration" (13005).
226. Loot "Cask" (16580) from "Tugog Grigol" in `rathemtn`.
227. Common item: Hops (16591). Listed in 31 zones.
228. Common item: Malt (16595). Listed in 30 zones.
229. Common item: Yeast (16596). Listed in 30 zones.
230. Combine in "Portable Drink Barrel" (17179): "Cask" (16580), "Hops" (16591), "Malt" (16595), "Yeast" (16596). Produces "Mead" (13008). Requires Brewing, trivial 41.
231. erudnext/"Reklon Gnallen", hand "Iron Ration" (13005) + "Mead" (13008). Requires `paladin_epic` ==9. Gives "Erudin Prayer Bead" (69965).
232. Summon "Quiver of Marr" (17307) by casting "Quiver of Marr".
233. rathemtn/"Shin Master Grubbus", hand "Quiver of Marr" (17307). Requires `paladin_epic` ==9. Gives "Gukta Prayer Bead" (69964).
234. Common item: Barley (16590). Listed in 28 zones.
235. Combine in "Medicine Bag" (17901): "Hand-Formed Bottle" (45232), "Ensnaring Concoction V" (45236). Produces "Empty Vial" (10062), "Cork" (16851), "Formed Ensnaring Concoction V" (45258). Requires Alchemy, trivial 41.
236. Combine in Brew Barrel (19): "Bottle of Aged Bloodwine" (51163), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aged Bloodwine" (51164). Requires Brewing, trivial 255.
237. 11 other recipes also produce Cork (16851).
238. Combine in "Portable Drink Barrel" (17179): "Water Flask" (13006), "Celestial Essence" (9650). Produces "Purified Water" (12607). Requires Brewing, trivial 58.
239. Combine in "Tracker's Water Extractor" (17987): "Purification Tablet" (12630), "Water Reed" (12778). Produces "Purified Water" (12607) x3. Requires Pottery. The combine does not fail.
240. 3 other recipes also produce Purified Water (12607).
241. Forage "Sand Verbena" (65582) in `taka`.
242. Forage "Sand Verbena" (65582) in `takb`.
243. Forage "Sand Verbena" (65582) in `takc`.
244. Forage "Sand Verbena" (65582) in `takd`.
245. Forage "Sand Verbena" (65582) in `take`.
246. Forage "Sand Verbena" (65582) in `takf`.
247. Forage "Sand Verbena" (65582) in `takg`.
248. Forage "Sand Verbena" (65582) in `takh`.
249. Forage "Sand Verbena" (65582) in `taki`.
250. Forage "Sand Verbena" (65582) in `takj`.
251. Combine in Brew Barrel (19): "Barley" (16590), "Bottle" (16598), "Cork" (16851), "Hops" (16591), "Purified Water" (12607), "Sand Verbena" (65582), "Yeast" (16596). Produces "Bottle of Double Brewed Double Dry Stout" (51157). Requires Brewing, trivial 226.
252. kaladimb/"Datur Nightseer", hand "Bottle of Double Brewed Double Dry Stout" (51157). Requires `paladin_epic` ==9. Gives "Kaladim Prayer Bead" (69963).
253. felwithea/"General Jyleel", hand platinum:1000. Requires `paladin_epic` ==9. Gives "Felwithe Prayer Bead" (69962).
254. Ground spawn of "Freeport Prayer Bead" (69961) in `freeportwest`.
255. Ground spawn of "Freeport Prayer Bead" (69961) in `freportn`.
256. qeynos2/"Ziska Ironforge", hand platinum:500. Requires `paladin_epic` ==9. Gives "Qeynos Prayer Bead" (69960).
257. Combine in "Unfilled Set of Prayer Beads" (69968): "Rivervale Prayer Bead" (69967), "Ak'anon Prayer Bead" (69966), "Erudin Prayer Bead" (69965), "Gukta Prayer Bead" (69964), "Kaladim Prayer Bead" (69963), "Felwithe Prayer Bead" (69962), "Freeport Prayer Bead" (69961), "Qeynos Prayer Bead" (69960). Produces "Set of Prayer Beads" (69969). The combine does not fail.
258. dranikhollowsc/"Anetal", hand "Set of Prayer Beads" (69969). Sets `paladin_epic_hollowc` to `2`.
259. natimbi/"Kemik Arulon", hand "Set of Prayer Beads" (69969). Sets `paladin_epic_hollowc` to `1`.
260. natimbi/"Kemik Arulon", say "Hail". Requires `paladin_epic_hollowc` ==2. Requires `paladin_epic_hollowc` ==1. Gives "Token of Compassion" (69953).
261. Requires `pal_chest_keel` unset; no setter establishes this state.
262. oasis/"Paladin Epic", say "Hail". Requires `pal_chest_keel` unset. Gives "Keelee's Brooch" (69982).
263. oasis/"Paladin Epic", say "Keelee Say". Gives "Keelee's Brooch" (69982).
264. sro/"Instructor Maerceci", hand "Keelee's Brooch" (69982). Gives "Token of Chivalry" (69954).
265. Loot "Valdoon Kel'Novar's Heart" (69981) from "Valdoon Kel'Novar" in `mmcc`.
266. felwithea/"Galrun Starforge", hand "Valdoon Kel'Novar's Heart" (69981). Gives "Token of Cleansing" (69956).
267. provinggrounds/"Pashia Clouddancer", say "Note". Gives "Note from Pashia" (69973).
268. nedaria/"Duram Firechaser", hand "Note from Pashia" (69973). Gives "Token of Heroism" (69955).
269. Say "Check Lorb" to anguish/"Zone Status".
270. Spawns "Orb of Discordant Energy" (317087).
271. Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy".
272. Say "Check Uorb" to anguish/"Zone Status".
273. Say "Check Amv Chest" to anguish/"Zone Status".
274. Spawns "Ornate Chest" (317112).
275. Loot "Globe of Discordant Energy" (47100) from "Ornate Chest".
276. 2 other loot steps also yield Globe of Discordant Energy (47100).
277. Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy" in `anguish`.
278. Loot "Globe of Discordant Energy" (47100) from "Overlords Chest".
279. airplane/"Inte Akera", hand "Globe of Discordant Energy" (47100). Gives "Token of Loyalty" (69958).

### "Token of Conviction" (69957)

1. qeynos2/"Camlend Serbold", say "Gem". Gives "Unfilled Set of Prayer Beads" (69968).
2. rivervale/"Kaya Cloudfoot", say "Different About It". Gives "Note from Kaya" (69970).
3. rivervale/"Deputy Cheel", hand "Note from Kaya" (69970). Gives "Rivervale Prayer Bead" (69967).
4. **Broken:** nothing in the graph gives, loots, spawns, or combines Ak`anon Prayer Bead (69966).
5. Say "Hail" to skyfire/"Dry Sapara".
6. Spawns "Rithnok the Tormented" (91193).
7. Loot "Rithnok's Soulstone" (69935) from "Rithnok the Tormented".
8. skyfire/"Dry Sapara", hand "Rithnok's Soulstone" (69935). Gives "Rithnok's Soulstone" (69936).
9. Ground spawn of "Soulstone Shard" (69937) in `draniksscar`.
10. Ground spawn of "Soulstone Shard" (69938) in `bloodfields`.
11. Ground spawn of "Soulstone Shard" (69939) in `causeway`.
12. Ground spawn of "Soulstone Shard" (69940) in `dranik`.
13. Combine in "Rithnok's Soulstone" (69936): "Soulstone Shard" (69937), "Soulstone Shard" (69938), "Soulstone Shard" (69939), "Soulstone Shard" (69940). Produces "Rithnok's Soulstone" (69941). The combine does not fail.
14. Hand "Enchanted Bone Powder" (69949) to letalis/"Drema Young". Spawns "Drema Young" (169128). Loot "Drema's Soulstone" (69928) from "Drema Young".
15. Loot "Drema's Soulstone" (69928) from "Drema Young".
16. Loot "Drema's Soulstone" (69928) from "Drema Young" in `letalis`.
17. Loot "Soulstone Shard" (69950) from "Coterie Corruptor" in `tenebrous`.
18. Say "Mujaki Death" to ponightmare/"Mujaki".
19. Spawns "Shade of Mujaki the Devourer" (204081).
20. Loot "Soulstone Shard" (69951) from "Shade of Mujaki the Devourer".
21. Combine in "Drema's Soulstone" (69928): "Soulstone Shard" (69950), "Soulstone Shard" (69951). Produces "Drema's Soulstone" (69952). The combine does not fail.
22. freporte/"Brunar Rankin", say "Hail". Sets `paladin_epic` to `3`.
23. global/"Global Player", combine recipe 19880. Sets `paladin_epic` to `8`.
24. Spawns "A Corrupted Koalindl" (69141) in `oot` on event_fish_success.
25. Loot "Corrupted Koalindl's Heart" (69929) from "A Corrupted Koalindl".
26. Spawns "A Corrupted Koalindl" (224432) in `gunthak` on event_fish_success.
27. Loot "Corrupted Koalindl's Heart" (69930) from "A Corrupted Koalindl".
28. Spawns "A Corrupted Koalindl" (93306) in `overthere` on event_fish_success.
29. Loot "Corrupted Koalindl's Heart" (69931) from "A Corrupted Koalindl".
30. Spawns "A Corrupted Koalindl" (182150) in `nedaria` on event_fish_success.
31. Loot "Corrupted Koalindl's Heart" (69932) from "A Corrupted Koalindl".
32. qeynos2/"Enic Ruklin", hand "Corrupted Koalindl's Heart" (69929) + "Corrupted Koalindl's Heart" (69930) + "Corrupted Koalindl's Heart" (69931) + "Corrupted Koalindl's Heart" (69932). Sets `paladin_epic` to `4`.
33. dawnshroud/"Mikhal Young", say "Find Anything". Requires `paladin_epic` ==4. Gives "Drema's Locket" (69945).
34. letalis/"Drema Young", hand "Drema's Locket" (69945). Requires `paladin_epic` set. Requires `paladin_epic` >=4. Gives "Drema's Fingerbone" (69946).
35. dawnshroud/"Mikhal Young", hand "Drema's Fingerbone" (69946). Sets `paladin_epic` to `5`.
36. abysmal/"Lovine Lemise", say "Ingredients". Requires `paladin_epic` ==5. Gives "Lovine's Potion Bag" (69922).
37. No quest step gives Ra`Tuk Screambringer's Jaw (69921). The dump lists it in barindu.
38. Loot "Noc Fleshfeasters Tail" (69920) from "A Noc Fleshfeaster" in `riwwi`.
39. Loot "Mastruq Havocblade Blood" (69919) from "A Mastruq Havocblade" in `qinimi`.
40. Loot "Mastruq Havocblade Blood" (69919) from "A Mastruq Warfiend" in `qinimi`.
41. Loot "Potameid Seaweed Strands" (69918) from "An Entrapped Potameid" in `natimbi`.
42. Combine in "Lovine's Potion Bag" (69922): "Ra'Tuk Screambringer's Jaw" (69921), "Noc Fleshfeasters Tail" (69920), "Mastruq Havocblade Blood" (69919), "Potameid Seaweed Strands" (69918). Produces "Lovine's Potion Bag" (69923). The combine does not fail.
43. abysmal/"Lovine Lemise", hand "Lovine's Potion Bag" (69923). Sets `paladin_epic_reiya` to `1`.
44. Summon "Foldable Medicine Bag" (17770) by casting "Unfold Medicine Bag".
45. Common item: Fine Potion Vial (95846). Listed in 15 zones.
46. Common item: Robust Shadow Essence (96911). Listed in 5 zones.
47. Loot "Sage Leaf" (14215) from "a Di'zok Herbalist" in `chardok`.
48. Loot "Sage Leaf" (14215) from "a Sarnak Herb Collector" in `chardok`.
49. Loot "Sage Leaf" (14215) from "an Apprentice Herbalist" in `chardok`.
50. Loot "Valerian Root" (14230) from "a Di'zok Herbalist" in `chardok`.
51. Loot "Valerian Root" (14230) from "a Sarnak Herb Collector" in `chardok`.
52. Loot "Valerian Root" (14230) from "an Apprentice Herbalist" in `chardok`.
53. Common item: Woundwart (16526). Listed in 9 zones.
54. Combine in "Foldable Medicine Bag" (17770): "Fine Potion Vial" (95846), "Robust Shadow Essence" (96911), "Sage Leaf" (14215), "Valerian Root" (14230), "Woundwart" (16526). Produces "Mist of the Breathless" (96937). Requires Alchemy, trivial 224.
55. abysmal/"Reiya The Pained", hand "Mist of the Breathless" (96937). Requires `paladin_epic_reiya` ==1. Gives "Reiya's Soulstone" (69924).
56. Spawns "Shade of Reiya the Pained" (284104) in `ferubi` on enter.
57. Loot "Soulstone Shard" (69943) from "Shade of Reiya the Pained".
58. Loot "Soulstone Shard" (69944) from "Vuranish Xxuro" in `vxed`.
59. Combine in "Reiya's Soulstone" (69924): "Soulstone Shard" (69943), "Soulstone Shard" (69944). Produces "Reiya's Soulstone" (69942). The combine does not fail.
60. Loot "Tainted Darksteel Sword" (29000) from "Keeper of the Tombs" in `hole`.
61. freeporteast/"Peasant Woman", say "I Will Take It". Gives "Bucket of Water" (29008).
62. freportw/"Peasant Woman", say "I Will Take It". Gives "Bucket of Water" (29008).
63. freeporteast/"Joshua", hand "Bucket of Water" (29008). Gives "Bucket of Pure Water" (29009).
64. freportw/"Joshua", hand "Bucket of Water" (29008). Gives "Bucket of Pure Water" (29009).
65. erudnext/"Reklon Gnallen", hand "Tainted Darksteel Sword" (29000) + "Bucket of Pure Water" (29009). Gives "Gleaming Crested Sword" (29003).
66. Loot "Tainted Darksteel Breastplate" (29001) from "Thought Destroyer" in `hateplaneb`.
67. kaladimb/"Nella Stonebraids", say "Jark". Gives "Cold Plate of Beef and Bread" (29007).
68. kaladimb/"Nella Stonebraids", say "Dinner". Gives "Cold Plate of Beef and Bread" (29007).
69. kaladimb/"Jark", hand "Cold Plate of Beef and Bread" (29007). Gives "Pure Crystal" (29006).
70. erudnext/"Reklon Gnallen", hand "Tainted Darksteel Breastplate" (29001) + "Pure Crystal" (29006). Gives "Gleaming Crested Breastplate" (29004).
71. Loot "Tainted Darksteel Shield" (29002) from "Kirak Vil" in `nektulos`.
72. felwithea/"Elia The Pure", hand "Tainted Darksteel Shield" (29002). Gives "Gleaming Crested Shield" (29005).
73. erudnext/"Reklon Gnallen", hand "Gleaming Crested Sword" (29003) + "Gleaming Crested Breastplate" (29004) + "Gleaming Crested Shield" (29005). Gives "Mark of Atonement" (29010).
74. No quest step gives Drom's Champagne (13829). The dump lists it in freeporteast, freporte, highpasshold.
75. freeporteast/"Tykar Renlin", hand "Drom's Champagne" (13829) + "Drom's Champagne" (13829) + "Drom's Champagne" (13829) + "Drom's Champagne" (13829). Gives "Bunker Cell #1" (12196).
76. freporte/"Tykar Renlin", hand "Drom's Champagne" (13829) + "Drom's Champagne" (13829) + "Drom's Champagne" (13829) + "Drom's Champagne" (13829). Gives "Bunker Cell #1" (12196).
77. Summon "Black Diamond of Nightmares" (29990) by casting "Imbue Nightmare".
78. poknowledge/"Aid Grimel", say "Versed In The Art Of Smithing". Gives "Filthy Breastplate" (15984).
79. Combine in "Mixing Bowl" (17906): "Celestial Solvent" (9731), "Words of Acquisition (Beza)" (11866). Produces "Celestial Essence" (9650). Requires Baking, trivial 15. The combine does not fail.
80. Combine in "Mixing Bowl" (17906): "Celestial Solvent" (9731), "Words of Burnishing" (11862). Produces "Celestial Essence" (9650). Requires Baking, trivial 15. The combine does not fail.
81. 67 other recipes also produce Celestial Essence (9650).
82. Common item: Jar of Acid (22133). Listed in 15 zones.
83. Combine in Brew Barrel (19): "Celestial Essence" (9650), "Jar of Acid" (22133). Produces "Acid Wash" (15987). Requires Brewing, trivial 151.
84. Combine in Forge (17): "Filthy Breastplate" (15984), "Acid Wash" (15987). Produces "Cleansed Breastplate" (15998). Requires Blacksmithing, trivial 227.
85. Common item: Mortar and Pestle (17904). Listed in 12 zones.
86. No quest step gives Sandstorm Pearl (29909). The dump lists it in bothunder.
87. Combine in "Mortar and Pestle" (17904): "Sandstorm Pearl" (29909). Produces "Powdered Sandstorm Pearl" (29520) x4. Requires Make Poison, trivial 255.
88. Common item: Firing Sheet (16906). Listed in 34 zones.
89. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
90. qeynos/"Wolten Grafe", say "Crush The Undead". Gives "Box For Bones" (17941).
91. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `steamfont`.
92. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `tox`.
93. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `toxxulia`.
94. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
95. toxxulia/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
96. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). The combine does not fail.
97. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
98. qeynos2/"Phin Esrinap", say "Supplies". Gives "Message to Konem" (18921).
99. qeytoqrg/"Konem Matse", hand "Message to Konem" (18921). Gives "Grathin's Invoice" (18922).
100. qeynos2/"Phin Esrinap", hand "Grathin's Invoice" (18922). Gives "Water Flask" (13006).
101. Say "Tm Devrak Death" to rujd/"Rujd".
102. Spawns "spawn chest with Heavy Orcish Prison Key" (245241).
103. Loot "Pod of Water" (13044) from "spawn chest with Heavy Orcish Prison Key".
104. Say "Tm Dokorel Death" to rujd/"Rujd".
105. Say "Tm Velrek Death" to rujd/"Rujd".
106. Say "Researcher Death" to rujg/"Rujg".
107. Spawns "A Barrel" (260015).
108. Loot "Pod of Water" (13044) from "A Barrel".
109. 3 other loot steps also yield Pod of Water (13044).
110. Forage "Pod of Water" (13044) in `ruja`.
111. Forage "Pod of Water" (13044) in `uqua`.
112. Forage "Pod of Water" (13044) in `yxtta`.
113. Combine in Brew Barrel (19): "Bottle of Aged Bloodwine" (51163), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aged Bloodwine" (51164). Requires Brewing, trivial 255.
114. Combine in Brew Barrel (19): "Bottle of Aldo's Bitter Ale" (75805), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aldo's Bitter Ale" (75811). Requires Brewing, trivial 15.
115. 17 other recipes also produce Bottle (16598).
116. Combine in Brew Barrel (19): "Pod of Water" (13044), "Bottle" (16598). Produces "Water Flask" (13006). Requires Brewing, trivial 21.
117. Combine in Pottery Wheel (21): "Water Flask" (13006), "Block of Clay" (16901). Produces "Small Block of Clay" (16900) x3. Requires Pottery, trivial 21.
118. Combine in Pottery Wheel (21): "Small Block of Clay" (16900), "Water Flask" (13006). Produces "Block of Clay" (16901). Requires Pottery, trivial 21.
119. Combine in Pottery Wheel (21): "Water Flask" (13006), "Large Block of Clay" (16902). Produces "Block of Clay" (16901) x2. Requires Pottery, trivial 21.
120. Combine in Pottery Wheel (21): "Block of Clay" (16901), "Water Flask" (13006). Produces "Large Block of Clay" (16902). Requires Pottery, trivial 21.
121. Common item: Large Bowl Sketch (16963). Listed in 29 zones.
122. Combine in Pottery Wheel (21): "Large Block of Clay" (16902), "Water Flask" (13006), "Large Bowl Sketch" (16963). Produces "Unfired Mixing Bowl" (16930). Requires Pottery, trivial 128.
123. Combine in Kiln (22): "Firing Sheet" (16906), "Unfired Mixing Bowl" (16930). Produces "Mixing Bowl" (17906). Requires Pottery, trivial 15.
124. Combine in "Mixing Bowl" (17906): "Sandstorm Pearl" (29909). Produces "Powdered Sandstorm Pearl" (29520) x4. Requires Baking. The combine does not fail.
125. Spawns "a Koka'Vor chieftain" (210236) in `postorms` on event_signal.
126. Loot "Storm Rider Blood" (29526) from "a Koka'Vor chieftain".
127. Loot "Storm Rider Blood" (29526) from "A stormrider" in `bothunder`.
128. Loot "Storm Rider Blood" (29526) from "Dolsoj Warrebs" in `bazaar`.
129. Loot "Storm Rider Blood" (29526) from "a Koka'Vor krovian" in `postorms`.
130. Loot "Storm Rider Blood" (29526) from "a Koka'Vor senvar" in `postorms`.
131. No quest step gives Drop of Pure Rain (29904). The dump lists it in bothunder.
132. Combine in Brew Barrel (19): "Powdered Sandstorm Pearl" (29520), "Storm Rider Blood" (29526), "Drop of Pure Rain" (29904). Produces "Hurricane Temper" (29533). Requires Brewing, trivial 135.
133. Combine in Forge (17): "Cleansed Breastplate" (15998), "Hurricane Temper" (29533). Produces "Tempered Breastplate" (15999). Requires Blacksmithing, trivial 229.
134. Combine in Forge (17): "Black Diamond of Nightmares" (29990), "Tempered Breastplate" (15999). Produces "Imbued Breastplate" (15985). Requires Blacksmithing 220. Trivial at 275.
135. poknowledge/"Aid Grimel", hand "Imbued Breastplate" (15985). Gives "Hardened Leather Signet" (16249).
136. poknowledge/"Aid Grimel", say "Skill In Brewing". Gives "Portable Drink Barrel" (17179).
137. Common item: Snake Scales (13070). Listed in 56 zones.
138. Combine in "Portable Drink Barrel" (17179): "Water Flask" (13006), "Snake Scales" (13070), "Bottle" (16598). Produces "Bog Juice" (16581). Requires Brewing, trivial 21.
139. Common item: Spit (17947). Listed in 34 zones.
140. Common item: Fire Beetle Eye (10307). Listed in 24 zones.
141. Spawns "Sepsis Rat" (45113) in `qcat` on event_death.
142. Loot "Rat Ears" (13072) from "Sepsis Rat".
143. Kill steamfont/"Diseased Female Rat". Spawns "A Young Plague Rat" (56086).
144. Loot "Rat Ears" (13072) from "A Young Plague Rat".
145. Kill steamfontmts/"Diseased Female Rat". Spawns "A Young Plague Rat" (448036).
146. Combine in "Spit" (17947): "Fire Beetle Eye" (10307), "Rat Ears" (13072). Produces "Edible Goo" (13498). Requires Baking, trivial 21.
147. freeporteast/"A Prisoner", hand "Bunker Cell #1" (12196) + "Edible Goo" (13498) + "Bog Juice" (16581). Gives "H. K. 102" (12143).
148. freportw/"A Prisoner", hand "Bunker Cell #1" (12196) + "Edible Goo" (13498) + "Bog Juice" (16581). Gives "H. K. 102" (12143).
149. highkeep/"Assistant Kiolna", hand "H. K. 102" (12143). Gives "Sealed Note" (18936).
150. paw/"Brother Hayle", hand "Sealed Note" (18936). Gives "Note" (18937).
151. southkarana/"Brother Hayle", hand "Sealed Note" (18936). Gives "Note" (18937).
152. Kill freportw/"Sir Lucan D-Lere". Spawns "Sir Lucan D'Lere" (9147).
153. Loot "Testimony of Truth" (18827) from "Sir Lucan D'Lere".
154. Loot "Testimony of Truth" (18827) from "Sir Lucan D'Lere" in `freeporteast`.
155. freeportwest/"Valeron Dushire", hand "Testimony of Truth" (18827). Gives "Brilliant Sword of Faith" (13947).
156. freportn/"Valeron Dushire", hand "Testimony of Truth" (18827). Gives "Brilliant Sword of Faith" (13947).
157. Hand "Token of Bravery" (12144) + "Token of Generosity" (13865) to freeportwest/"Merko Quetalis". Spawns "spawns Guard Willia" (383270). Loot "Token of Truth" (13866) from "spawns Guard Willia".
158. Hand "Token of Bravery" (12144) + "Token of Generosity" (13865) to freportn/"Merko Quetalis". Spawns "spawns Guard Willia" (8110). Loot "Token of Truth" (13866) from "spawns Guard Willia".
159. Loot "Token of Truth" (13866) from "Guard Willia".
160. freeportwest/"Merko Quetalis", hand "Token of Truth" (13866). Gives "Testimony" (18828).
161. freportn/"Merko Quetalis", hand "Token of Truth" (13866). Gives "Testimony" (18828).
162. Loot "Glowing Sword Hilt" (12197) from "Xicotl" in `mistmoore`.
163. paw/"Brother Hayle", hand "Glowing Sword Hilt" (12197) + "Brilliant Sword of Faith" (13947) + "Testimony" (18828) + "Note" (18937). Gives "SoulFire" (5504).
164. southkarana/"Brother Hayle", hand "Glowing Sword Hilt" (12197) + "Brilliant Sword of Faith" (13947) + "Testimony" (18828) + "Note" (18937). Gives "SoulFire" (5504).
165. airplane/"Inte Akera", hand "SoulFire" (5504). Gives "Inte's First Blessing" (18033).
166. lavastorm/"Ruathey", say "Bag". Gives "Nobleman's Bag" (17878).
167. Common item: Ghoul's Heart (2410). Listed in 8 zones.
168. No quest step gives Amstaf's Scroll (2411). The dump lists it in highkeep.
169. No quest step gives Blade of Nobility (2412). The dump lists it in butcher.
170. Loot "Hilt of the Nobleman" (2413) from "Ekeros" in `najena`.
171. Loot "Hilt of the Nobleman" (2413) from "A Skeleton" in `najena`.
172. Combine in "Nobleman's Bag" (17878): "Ghoul's Heart" (2410), "Amstaf's Scroll" (2411), "Blade of Nobility" (2412), "Hilt of the Nobleman" (2413). Produces "Ghoulbane" (5403). The combine does not fail.
173. airplane/"Inte Akera", hand "Ghoulbane" (5403). Gives "Inte's Second Blessing" (18034).
174. Hand "Miragul's Phylactery" (19072) to everfrost/"Lich Of Miragul". Spawns "Spawn Miragul" (30094). Loot "Miragul's Head" (19073) from "Spawn Miragul".
175. Loot "Miragul's Head" (19073) from "Miragul".
176. Hand "Miragul's Phylactery" (19072) to everfrost/"Lich Of Miragul". Spawns "Spawn Miragul" (30094). Loot "Miragul's Robe" (1254) from "Spawn Miragul".
177. Loot "Miragul's Robe" (1254) from "Miragul".
178. airplane/"Inte Akera", hand "Miragul's Robe" (1254) + "Inte's First Blessing" (18033) + "Inte's Second Blessing" (18034) + "Miragul's Head" (19073). Gives "Fiery Avenger" (11050).
179. fearplane/"Irak Altil", hand "Fiery Avenger" (11050) + "Mark of Atonement" (29010). Gives "Fiery Defender" (10099).
180. povalor/"Baltron Werters", say "Couragebringer". Sets `pre_pal` to `1`.
181. Requires `pre_pal` unset; no setter establishes this state.
182. povalor/"Baltron Werters", say "Couragebringer". Requires `pre_pal` unset. Gives "Baltron's Solvent" (69901).
183. sro/"Gilfal", hand "Baltron's Solvent" (69901). Requires `pre_pal` ==1. Gives "Gilfal's Scabbard" (69902).
184. Spawns "Neffiken Lord Kelek-Vor" (210229) in `postorms` on event_signal.
185. Loot "Broken Sword Piece" (69903) from "Neffiken Lord Kelek-Vor".
186. Loot "Broken Sword Piece" (69903) from "Neffiken Lord of Kelek'Vor".
187. Say "Control Timer" to hateplaneb/"Maestro".
188. Spawns "Maestro of Rancor" (186111).
189. Loot "Broken Sword Piece" (69904) from "Maestro of Rancor".
190. **Broken:** no event trigger found for `hateplaneb/maestro#timer:popmaestro`.
191. Spawns "Maestro of Rancor" (186111) after `hateplaneb/maestro#timer:popmaestro`.
192. Loot "Broken Sword Piece" (69905) from "Kaniz Painbringer" in `potorment`.
193. sro/"Gilfal", hand "Baltron's Solvent" (69901). Sets `pre_pal` to `2`.
194. Ground spawn of "Rune of Xor" (69909) in `potranquility`.
195. Ground spawn of "Rune of Yirno" (69908) in `mistmoore`.
196. Ground spawn of "Rune of Zota" (69907) in `scarlet`.
197. Ground spawn of "Rune Wilun" (69910) in `gunthak`.
198. everfrost/"Rombus", hand "Rune of Zota" (69907) + "Rune of Yirno" (69908) + "Rune of Xor" (69909) + "Rune Wilun" (69910). Requires `pre_pal` ==2. Gives "Broken Sword Piece" (69906).
199. Combine in "Gilfal's Scabbard" (69902): "Broken Sword Piece" (69903), "Broken Sword Piece" (69904), "Broken Sword Piece" (69905), "Broken Sword Piece" (69906). Produces "Fractured Couragebringer" (69911). The combine does not fail.
200. sro/"Gilfal", hand "Fractured Couragebringer" (69911). Sets `pre_pal` to `4`.
201. everfrost/"Rombus", hand "Rune of Zota" (69907) + "Rune of Yirno" (69908) + "Rune of Xor" (69909) + "Rune Wilun" (69910). Sets `pre_pal` to `3`.
202. sro/"Gilfal", hand "Fractured Couragebringer" (69911). Requires `pre_pal` ==3. Gives "Fractured Couragebringer" (69912).
203. povalor/"Baltron Werters", hand "Fractured Couragebringer" (69912). Requires `pre_pal` ==4. Gives "Couragebringer" (69913).
204. hohonora/"Irak Altil", say "Hail". Sets `paladin_epic` to `6`.
205. Spawns "Durunal the Cursebearer" (300087) in `wallofslaughter` on enter.
206. Loot "Dark and Twisted Sword" (69971) from "Durunal the Cursebearer".
207. hohonora/"Irak Altil", hand "Dark and Twisted Sword" (69971). Requires `paladin_epic` ==6. Gives "Dark and Twisted Sword" (69972).
208. Loot "Redis' Soulstone" (69983) from "Shade of Redis Linrok" in `dranikcatacombsa`.
209. Combine in "Dark and Twisted Sword" (69972): "Rithnok's Soulstone" (69941), "Drema's Soulstone" (69952), "Reiya's Soulstone" (69942), "Redis' Soulstone" (69983). Produces "Redemption" (64031). The combine does not fail.
210. hohonora/"Irak Altil", say "Tell Me About Your Master". Sets `paladin_epic` to `9`.
211. erudnint/"Josper Kenshed", say "Collect Component". Gives "Empty Bag" (17944).
212. halas/"Lysbith Mcnaff", say "Protect The Pass". Gives "Empty Bag" (17944).
213. Loot "Goblin Ice Necklace" (13897) from "Redwind" in `everfrost`.
214. Loot "Goblin Ice Necklace" (13897) from "An Ice Goblin Scout" in `everfrost`.
215. Loot "Goblin Ice Necklace" (13897) from "An Ice Goblin Whelp" in `everfrost`.
216. Loot "Goblin Ice Necklace" (13897) from "An Icy Orc" in `everfrost`.
217. Loot "Goblin Ice Necklace" (13897) from "Ice Goblin Diver" in `everfrost`.
218. Combine in "Empty Bag" (17944): "Goblin Ice Necklace" (13897). Produces "Bag of Ice Necklaces" (13898). The combine does not fail.
219. halas/"Lysbith Mcnaff", hand "Bag of Ice Necklaces" (13898). Gives "Iron Ration" (13005).
220. Common item: Gnoll Fang (13915). Listed in 5 zones.
221. halas/"Lysbith Mcnaff", hand "Gnoll Fang" (13915) + "Gnoll Fang" (13915) + "Gnoll Fang" (13915). Gives "Iron Ration" (13005).
222. Requires `halloween_draykey_rations` unset; no setter establishes this state.
223. kithicor/"Old Man Draykey", say "Instructions". Requires `halloween_draykey_rations` unset. Gives "Iron Ration" (13005).
224. commons/"Kizdean Gix", say "Messages For Neriak". Gives "Sealed Letter" (18889).
225. neriakc/"Loveal S-Nez", hand "Sealed Letter" (18889). Gives "Iron Ration" (13005).
226. Loot "Cask" (16580) from "Tugog Grigol" in `rathemtn`.
227. Common item: Hops (16591). Listed in 31 zones.
228. Common item: Malt (16595). Listed in 30 zones.
229. Common item: Yeast (16596). Listed in 30 zones.
230. Combine in "Portable Drink Barrel" (17179): "Cask" (16580), "Hops" (16591), "Malt" (16595), "Yeast" (16596). Produces "Mead" (13008). Requires Brewing, trivial 41.
231. erudnext/"Reklon Gnallen", hand "Iron Ration" (13005) + "Mead" (13008). Requires `paladin_epic` ==9. Gives "Erudin Prayer Bead" (69965).
232. Summon "Quiver of Marr" (17307) by casting "Quiver of Marr".
233. rathemtn/"Shin Master Grubbus", hand "Quiver of Marr" (17307). Requires `paladin_epic` ==9. Gives "Gukta Prayer Bead" (69964).
234. Common item: Barley (16590). Listed in 28 zones.
235. Combine in "Medicine Bag" (17901): "Hand-Formed Bottle" (45232), "Ensnaring Concoction V" (45236). Produces "Empty Vial" (10062), "Cork" (16851), "Formed Ensnaring Concoction V" (45258). Requires Alchemy, trivial 41.
236. Combine in Brew Barrel (19): "Bottle of Aged Bloodwine" (51163), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aged Bloodwine" (51164). Requires Brewing, trivial 255.
237. 11 other recipes also produce Cork (16851).
238. Combine in "Portable Drink Barrel" (17179): "Water Flask" (13006), "Celestial Essence" (9650). Produces "Purified Water" (12607). Requires Brewing, trivial 58.
239. Combine in "Tracker's Water Extractor" (17987): "Purification Tablet" (12630), "Water Reed" (12778). Produces "Purified Water" (12607) x3. Requires Pottery. The combine does not fail.
240. 3 other recipes also produce Purified Water (12607).
241. Forage "Sand Verbena" (65582) in `taka`.
242. Forage "Sand Verbena" (65582) in `takb`.
243. Forage "Sand Verbena" (65582) in `takc`.
244. Forage "Sand Verbena" (65582) in `takd`.
245. Forage "Sand Verbena" (65582) in `take`.
246. Forage "Sand Verbena" (65582) in `takf`.
247. Forage "Sand Verbena" (65582) in `takg`.
248. Forage "Sand Verbena" (65582) in `takh`.
249. Forage "Sand Verbena" (65582) in `taki`.
250. Forage "Sand Verbena" (65582) in `takj`.
251. Combine in Brew Barrel (19): "Barley" (16590), "Bottle" (16598), "Cork" (16851), "Hops" (16591), "Purified Water" (12607), "Sand Verbena" (65582), "Yeast" (16596). Produces "Bottle of Double Brewed Double Dry Stout" (51157). Requires Brewing, trivial 226.
252. kaladimb/"Datur Nightseer", hand "Bottle of Double Brewed Double Dry Stout" (51157). Requires `paladin_epic` ==9. Gives "Kaladim Prayer Bead" (69963).
253. felwithea/"General Jyleel", hand platinum:1000. Requires `paladin_epic` ==9. Gives "Felwithe Prayer Bead" (69962).
254. Ground spawn of "Freeport Prayer Bead" (69961) in `freeportwest`.
255. Ground spawn of "Freeport Prayer Bead" (69961) in `freportn`.
256. qeynos2/"Ziska Ironforge", hand platinum:500. Requires `paladin_epic` ==9. Gives "Qeynos Prayer Bead" (69960).
257. Combine in "Unfilled Set of Prayer Beads" (69968): "Rivervale Prayer Bead" (69967), "Ak'anon Prayer Bead" (69966), "Erudin Prayer Bead" (69965), "Gukta Prayer Bead" (69964), "Kaladim Prayer Bead" (69963), "Felwithe Prayer Bead" (69962), "Freeport Prayer Bead" (69961), "Qeynos Prayer Bead" (69960). Produces "Set of Prayer Beads" (69969). The combine does not fail.
258. dranikhollowsc/"Anetal", hand "Set of Prayer Beads" (69969). Sets `paladin_epic_hollowc` to `2`.
259. natimbi/"Kemik Arulon", hand "Set of Prayer Beads" (69969). Sets `paladin_epic_hollowc` to `1`.
260. natimbi/"Kemik Arulon", say "Hail". Requires `paladin_epic_hollowc` ==2. Requires `paladin_epic_hollowc` ==1. Gives "Token of Compassion" (69953).
261. Requires `pal_chest_keel` unset; no setter establishes this state.
262. oasis/"Paladin Epic", say "Hail". Requires `pal_chest_keel` unset. Gives "Keelee's Brooch" (69982).
263. oasis/"Paladin Epic", say "Keelee Say". Gives "Keelee's Brooch" (69982).
264. sro/"Instructor Maerceci", hand "Keelee's Brooch" (69982). Gives "Token of Chivalry" (69954).
265. Loot "Valdoon Kel'Novar's Heart" (69981) from "Valdoon Kel'Novar" in `mmcc`.
266. felwithea/"Galrun Starforge", hand "Valdoon Kel'Novar's Heart" (69981). Gives "Token of Cleansing" (69956).
267. provinggrounds/"Pashia Clouddancer", say "Note". Gives "Note from Pashia" (69973).
268. nedaria/"Duram Firechaser", hand "Note from Pashia" (69973). Gives "Token of Heroism" (69955).
269. Say "Check Lorb" to anguish/"Zone Status".
270. Spawns "Orb of Discordant Energy" (317087).
271. Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy".
272. Say "Check Uorb" to anguish/"Zone Status".
273. Say "Check Amv Chest" to anguish/"Zone Status".
274. Spawns "Ornate Chest" (317112).
275. Loot "Globe of Discordant Energy" (47100) from "Ornate Chest".
276. 2 other loot steps also yield Globe of Discordant Energy (47100).
277. Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy" in `anguish`.
278. Loot "Globe of Discordant Energy" (47100) from "Overlords Chest".
279. airplane/"Inte Akera", hand "Globe of Discordant Energy" (47100). Gives "Token of Conviction" (69957).

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
  - Loot "Corrupted Koalindl's Heart" (69929) from "A Corrupted Koalindl".
- Corrupted Koalindl's Heart (69930)
  - Spawns "A Corrupted Koalindl" (224432) in `gunthak` on event_fish_success.
  - Loot "Corrupted Koalindl's Heart" (69930) from "A Corrupted Koalindl".
  - Loot "Corrupted Koalindl's Heart" (69930) from "A Corrupted Koalindl".
- Corrupted Koalindl's Heart (69931)
  - Spawns "A Corrupted Koalindl" (93306) in `overthere` on event_fish_success.
  - Loot "Corrupted Koalindl's Heart" (69931) from "A Corrupted Koalindl".
  - Loot "Corrupted Koalindl's Heart" (69931) from "A Corrupted Koalindl".
- Corrupted Koalindl's Heart (69932)
  - Spawns "A Corrupted Koalindl" (182150) in `nedaria` on event_fish_success.
  - Loot "Corrupted Koalindl's Heart" (69932) from "A Corrupted Koalindl".
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
  - Say "Check Lorb" to anguish/"Zone Status".
  - Spawns "Orb of Discordant Energy" (317087).
  - Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy".
  - Say "Check Uorb" to anguish/"Zone Status".
  - Spawns "Orb of Discordant Energy" (317087).
  - Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy".
  - Say "Check Amv Chest" to anguish/"Zone Status".
  - Spawns "Ornate Chest" (317112).
  - Loot "Globe of Discordant Energy" (47100) from "Ornate Chest".
  - 2 other loot steps also yield Globe of Discordant Energy (47100).
  - Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy" in `anguish`.
  - Loot "Globe of Discordant Energy" (47100) from "Ornate Chest".
  - Loot "Globe of Discordant Energy" (47100) from "Overlords Chest".

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
- `qeynos2` ziska ironforge, hand platinum:500 needs `paladin_epic` ==9.
  - Gives Qeynos Prayer Bead (69960).
- `rathemtn` shin master grubbus, hand 17307 needs `paladin_epic` ==9.
  - Turn in Quiver of Marr (17307).
  - Gives Gukta Prayer Bead (69964).
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
