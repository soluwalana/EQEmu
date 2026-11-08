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
19. Combine in Forge (17): "Filthy Breastplate" (15984), "Acid Wash" (15987). Produces "Cleansed Breastplate" (15998). Requires Blacksmithing, trivial 227.
20. Combine in Brew Barrel (19): "Powdered Sandstorm Pearl" (29520), "Storm Rider Blood" (29526), "Drop of Pure Rain" (29904). Produces "Hurricane Temper" (29533). Requires Brewing, trivial 135.
21. Combine in Forge (17): "Cleansed Breastplate" (15998), "Hurricane Temper" (29533). Produces "Tempered Breastplate" (15999). Requires Blacksmithing, trivial 229.
22. Combine in Forge (17): "Black Diamond of Nightmares" (29990), "Tempered Breastplate" (15999). Produces "Imbued Breastplate" (15985). Requires Blacksmithing 220. Trivial at 275.
23. poknowledge/"Aid Grimel", hand "Imbued Breastplate" (15985). Gives "Hardened Leather Signet" (16249).
24. poknowledge/"Aid Grimel", say "Skill In Brewing". Gives "Portable Drink Barrel" (17179).
25. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
26. qeynos/"Wolten Grafe", say "Crush The Undead". Gives "Box For Bones" (17941).
27. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `steamfont`.
28. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `tox`.
29. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `toxxulia`.
30. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
31. toxxulia/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
32. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). The combine does not fail.
33. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
34. qeynos2/"Phin Esrinap", say "Supplies". Gives "Message to Konem" (18921).
35. qeytoqrg/"Konem Matse", hand "Message to Konem" (18921). Gives "Grathin's Invoice" (18922).
36. qeynos2/"Phin Esrinap", hand "Grathin's Invoice" (18922). Gives "Water Flask" (13006).
37. Say "Tm Devrak Death" to rujd/"Rujd".
38. Spawns "spawn chest with Heavy Orcish Prison Key" (245241).
39. Loot "Pod of Water" (13044) from "spawn chest with Heavy Orcish Prison Key".
40. Say "Tm Dokorel Death" to rujd/"Rujd".
41. Say "Tm Velrek Death" to rujd/"Rujd".
42. Say "Researcher Death" to rujg/"Rujg".
43. Spawns "A Barrel" (260015).
44. Loot "Pod of Water" (13044) from "A Barrel".
45. 3 other loot steps also yield Pod of Water (13044).
46. Forage "Pod of Water" (13044) in `ruja`.
47. Forage "Pod of Water" (13044) in `uqua`.
48. Forage "Pod of Water" (13044) in `yxtta`.
49. Combine in Brew Barrel (19): "Bottle of Aged Bloodwine" (51163), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aged Bloodwine" (51164). Requires Brewing, trivial 255.
50. Combine in Brew Barrel (19): "Bottle of Aldo's Bitter Ale" (75805), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aldo's Bitter Ale" (75811). Requires Brewing, trivial 15.
51. 17 other recipes also produce Bottle (16598).
52. Combine in Brew Barrel (19): "Pod of Water" (13044), "Bottle" (16598). Produces "Water Flask" (13006). Requires Brewing, trivial 21.
53. Common item: Snake Scales (13070). Listed in 56 zones.
54. Combine in "Portable Drink Barrel" (17179): "Water Flask" (13006), "Snake Scales" (13070), "Bottle" (16598). Produces "Bog Juice" (16581). Requires Brewing, trivial 21.
55. Common item: Spit (17947). Listed in 34 zones.
56. Common item: Fire Beetle Eye (10307). Listed in 24 zones.
57. Spawns "Sepsis Rat" (45113) in `qcat` on event_death.
58. Loot "Rat Ears" (13072) from "Sepsis Rat".
59. Kill steamfont/"Diseased Female Rat". Spawns "A Young Plague Rat" (56086).
60. Loot "Rat Ears" (13072) from "A Young Plague Rat".
61. Kill steamfontmts/"Diseased Female Rat". Spawns "A Young Plague Rat" (448036).
62. Combine in "Spit" (17947): "Fire Beetle Eye" (10307), "Rat Ears" (13072). Produces "Edible Goo" (13498). Requires Baking, trivial 21.
63. freeporteast/"A Prisoner", hand "Bunker Cell #1" (12196) + "Edible Goo" (13498) + "Bog Juice" (16581). Gives "H. K. 102" (12143).
64. freportw/"A Prisoner", hand "Bunker Cell #1" (12196) + "Edible Goo" (13498) + "Bog Juice" (16581). Gives "H. K. 102" (12143).
65. highkeep/"Assistant Kiolna", hand "H. K. 102" (12143). Gives "Sealed Note" (18936).
66. paw/"Brother Hayle", hand "Sealed Note" (18936). Gives "Note" (18937).
67. southkarana/"Brother Hayle", hand "Sealed Note" (18936). Gives "Note" (18937).
68. Kill freportw/"Sir Lucan D-Lere". Spawns "Sir Lucan D'Lere" (9147).
69. Loot "Testimony of Truth" (18827) from "Sir Lucan D'Lere".
70. Loot "Testimony of Truth" (18827) from "Sir Lucan D'Lere" in `freeporteast`.
71. freeportwest/"Valeron Dushire", hand "Testimony of Truth" (18827). Gives "Brilliant Sword of Faith" (13947).
72. freportn/"Valeron Dushire", hand "Testimony of Truth" (18827). Gives "Brilliant Sword of Faith" (13947).
73. Hand "Token of Bravery" (12144) + "Token of Generosity" (13865) to freeportwest/"Merko Quetalis". Spawns "spawns Guard Willia" (383270). Loot "Token of Truth" (13866) from "spawns Guard Willia".
74. Hand "Token of Bravery" (12144) + "Token of Generosity" (13865) to freportn/"Merko Quetalis". Spawns "spawns Guard Willia" (8110). Loot "Token of Truth" (13866) from "spawns Guard Willia".
75. Loot "Token of Truth" (13866) from "Guard Willia".
76. freeportwest/"Merko Quetalis", hand "Token of Truth" (13866). Gives "Testimony" (18828).
77. freportn/"Merko Quetalis", hand "Token of Truth" (13866). Gives "Testimony" (18828).
78. Loot "Glowing Sword Hilt" (12197) from "Xicotl" in `mistmoore`.
79. paw/"Brother Hayle", hand "Glowing Sword Hilt" (12197) + "Brilliant Sword of Faith" (13947) + "Testimony" (18828) + "Note" (18937). Gives "SoulFire" (5504).
80. southkarana/"Brother Hayle", hand "Glowing Sword Hilt" (12197) + "Brilliant Sword of Faith" (13947) + "Testimony" (18828) + "Note" (18937). Gives "SoulFire" (5504).
81. airplane/"Inte Akera", hand "SoulFire" (5504). Gives "Inte's First Blessing" (18033).
82. lavastorm/"Ruathey", say "Bag". Gives "Nobleman's Bag" (17878).
83. Common item: Ghoul's Heart (2410). Listed in 8 zones.
84. No quest step gives Amstaf's Scroll (2411). The dump lists it in highkeep.
85. No quest step gives Blade of Nobility (2412). The dump lists it in butcher.
86. Loot "Hilt of the Nobleman" (2413) from "Ekeros" in `najena`.
87. Loot "Hilt of the Nobleman" (2413) from "A Skeleton" in `najena`.
88. Combine in "Nobleman's Bag" (17878): "Ghoul's Heart" (2410), "Amstaf's Scroll" (2411), "Blade of Nobility" (2412), "Hilt of the Nobleman" (2413). Produces "Ghoulbane" (5403). The combine does not fail.
89. airplane/"Inte Akera", hand "Ghoulbane" (5403). Gives "Inte's Second Blessing" (18034).
90. Hand "Miragul's Phylactery" (19072) to everfrost/"Lich Of Miragul". Spawns "Spawn Miragul" (30094). Loot "Miragul's Head" (19073) from "Spawn Miragul".
91. Loot "Miragul's Head" (19073) from "Miragul".
92. Hand "Miragul's Phylactery" (19072) to everfrost/"Lich Of Miragul". Spawns "Spawn Miragul" (30094). Loot "Miragul's Robe" (1254) from "Spawn Miragul".
93. Loot "Miragul's Robe" (1254) from "Miragul".
94. airplane/"Inte Akera", hand "Miragul's Robe" (1254) + "Inte's First Blessing" (18033) + "Inte's Second Blessing" (18034) + "Miragul's Head" (19073). Gives "Fiery Avenger" (11050).
95. fearplane/"Irak Altil", hand "Fiery Avenger" (11050) + "Mark of Atonement" (29010). Gives "Fiery Defender" (10099).

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
74. Combine in Forge (17): "Cleansed Breastplate" (15998), "Hurricane Temper" (29533). Produces "Tempered Breastplate" (15999). Requires Blacksmithing, trivial 229.
75. Combine in Forge (17): "Black Diamond of Nightmares" (29990), "Tempered Breastplate" (15999). Produces "Imbued Breastplate" (15985). Requires Blacksmithing 220. Trivial at 275.
76. poknowledge/"Aid Grimel", hand "Imbued Breastplate" (15985). Gives "Hardened Leather Signet" (16249).
77. poknowledge/"Aid Grimel", say "Skill In Brewing". Gives "Portable Drink Barrel" (17179).
78. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
79. qeynos/"Wolten Grafe", say "Crush The Undead". Gives "Box For Bones" (17941).
80. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `steamfont`.
81. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `tox`.
82. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `toxxulia`.
83. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
84. toxxulia/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
85. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). The combine does not fail.
86. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
87. qeynos2/"Phin Esrinap", say "Supplies". Gives "Message to Konem" (18921).
88. qeytoqrg/"Konem Matse", hand "Message to Konem" (18921). Gives "Grathin's Invoice" (18922).
89. qeynos2/"Phin Esrinap", hand "Grathin's Invoice" (18922). Gives "Water Flask" (13006).
90. Say "Tm Devrak Death" to rujd/"Rujd".
91. Spawns "spawn chest with Heavy Orcish Prison Key" (245241).
92. Loot "Pod of Water" (13044) from "spawn chest with Heavy Orcish Prison Key".
93. Say "Tm Dokorel Death" to rujd/"Rujd".
94. Say "Tm Velrek Death" to rujd/"Rujd".
95. Say "Researcher Death" to rujg/"Rujg".
96. Spawns "A Barrel" (260015).
97. Loot "Pod of Water" (13044) from "A Barrel".
98. 3 other loot steps also yield Pod of Water (13044).
99. Forage "Pod of Water" (13044) in `ruja`.
100. Forage "Pod of Water" (13044) in `uqua`.
101. Forage "Pod of Water" (13044) in `yxtta`.
102. Combine in Brew Barrel (19): "Bottle of Aged Bloodwine" (51163), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aged Bloodwine" (51164). Requires Brewing, trivial 255.
103. Combine in Brew Barrel (19): "Bottle of Aldo's Bitter Ale" (75805), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aldo's Bitter Ale" (75811). Requires Brewing, trivial 15.
104. 17 other recipes also produce Bottle (16598).
105. Combine in Brew Barrel (19): "Pod of Water" (13044), "Bottle" (16598). Produces "Water Flask" (13006). Requires Brewing, trivial 21.
106. Common item: Snake Scales (13070). Listed in 56 zones.
107. Combine in "Portable Drink Barrel" (17179): "Water Flask" (13006), "Snake Scales" (13070), "Bottle" (16598). Produces "Bog Juice" (16581). Requires Brewing, trivial 21.
108. Common item: Spit (17947). Listed in 34 zones.
109. Common item: Fire Beetle Eye (10307). Listed in 24 zones.
110. Spawns "Sepsis Rat" (45113) in `qcat` on event_death.
111. Loot "Rat Ears" (13072) from "Sepsis Rat".
112. Kill steamfont/"Diseased Female Rat". Spawns "A Young Plague Rat" (56086).
113. Loot "Rat Ears" (13072) from "A Young Plague Rat".
114. Kill steamfontmts/"Diseased Female Rat". Spawns "A Young Plague Rat" (448036).
115. Combine in "Spit" (17947): "Fire Beetle Eye" (10307), "Rat Ears" (13072). Produces "Edible Goo" (13498). Requires Baking, trivial 21.
116. freeporteast/"A Prisoner", hand "Bunker Cell #1" (12196) + "Edible Goo" (13498) + "Bog Juice" (16581). Gives "H. K. 102" (12143).
117. freportw/"A Prisoner", hand "Bunker Cell #1" (12196) + "Edible Goo" (13498) + "Bog Juice" (16581). Gives "H. K. 102" (12143).
118. highkeep/"Assistant Kiolna", hand "H. K. 102" (12143). Gives "Sealed Note" (18936).
119. paw/"Brother Hayle", hand "Sealed Note" (18936). Gives "Note" (18937).
120. southkarana/"Brother Hayle", hand "Sealed Note" (18936). Gives "Note" (18937).
121. Kill freportw/"Sir Lucan D-Lere". Spawns "Sir Lucan D'Lere" (9147).
122. Loot "Testimony of Truth" (18827) from "Sir Lucan D'Lere".
123. Loot "Testimony of Truth" (18827) from "Sir Lucan D'Lere" in `freeporteast`.
124. freeportwest/"Valeron Dushire", hand "Testimony of Truth" (18827). Gives "Brilliant Sword of Faith" (13947).
125. freportn/"Valeron Dushire", hand "Testimony of Truth" (18827). Gives "Brilliant Sword of Faith" (13947).
126. Hand "Token of Bravery" (12144) + "Token of Generosity" (13865) to freeportwest/"Merko Quetalis". Spawns "spawns Guard Willia" (383270). Loot "Token of Truth" (13866) from "spawns Guard Willia".
127. Hand "Token of Bravery" (12144) + "Token of Generosity" (13865) to freportn/"Merko Quetalis". Spawns "spawns Guard Willia" (8110). Loot "Token of Truth" (13866) from "spawns Guard Willia".
128. Loot "Token of Truth" (13866) from "Guard Willia".
129. freeportwest/"Merko Quetalis", hand "Token of Truth" (13866). Gives "Testimony" (18828).
130. freportn/"Merko Quetalis", hand "Token of Truth" (13866). Gives "Testimony" (18828).
131. Loot "Glowing Sword Hilt" (12197) from "Xicotl" in `mistmoore`.
132. paw/"Brother Hayle", hand "Glowing Sword Hilt" (12197) + "Brilliant Sword of Faith" (13947) + "Testimony" (18828) + "Note" (18937). Gives "SoulFire" (5504).
133. southkarana/"Brother Hayle", hand "Glowing Sword Hilt" (12197) + "Brilliant Sword of Faith" (13947) + "Testimony" (18828) + "Note" (18937). Gives "SoulFire" (5504).
134. airplane/"Inte Akera", hand "SoulFire" (5504). Gives "Inte's First Blessing" (18033).
135. lavastorm/"Ruathey", say "Bag". Gives "Nobleman's Bag" (17878).
136. Common item: Ghoul's Heart (2410). Listed in 8 zones.
137. No quest step gives Amstaf's Scroll (2411). The dump lists it in highkeep.
138. No quest step gives Blade of Nobility (2412). The dump lists it in butcher.
139. Loot "Hilt of the Nobleman" (2413) from "Ekeros" in `najena`.
140. Loot "Hilt of the Nobleman" (2413) from "A Skeleton" in `najena`.
141. Combine in "Nobleman's Bag" (17878): "Ghoul's Heart" (2410), "Amstaf's Scroll" (2411), "Blade of Nobility" (2412), "Hilt of the Nobleman" (2413). Produces "Ghoulbane" (5403). The combine does not fail.
142. airplane/"Inte Akera", hand "Ghoulbane" (5403). Gives "Inte's Second Blessing" (18034).
143. Hand "Miragul's Phylactery" (19072) to everfrost/"Lich Of Miragul". Spawns "Spawn Miragul" (30094). Loot "Miragul's Head" (19073) from "Spawn Miragul".
144. Loot "Miragul's Head" (19073) from "Miragul".
145. Hand "Miragul's Phylactery" (19072) to everfrost/"Lich Of Miragul". Spawns "Spawn Miragul" (30094). Loot "Miragul's Robe" (1254) from "Spawn Miragul".
146. Loot "Miragul's Robe" (1254) from "Miragul".
147. airplane/"Inte Akera", hand "Miragul's Robe" (1254) + "Inte's First Blessing" (18033) + "Inte's Second Blessing" (18034) + "Miragul's Head" (19073). Gives "Fiery Avenger" (11050).
148. fearplane/"Irak Altil", hand "Fiery Avenger" (11050) + "Mark of Atonement" (29010). Gives "Fiery Defender" (10099).
149. povalor/"Baltron Werters", say "Couragebringer". Sets `pre_pal` to `1`.
150. Requires `pre_pal` unset; no setter establishes this state.
151. povalor/"Baltron Werters", say "Couragebringer". Requires `pre_pal` unset. Gives "Baltron's Solvent" (69901).
152. sro/"Gilfal", hand "Baltron's Solvent" (69901). Requires `pre_pal` ==1. Gives "Gilfal's Scabbard" (69902).
153. Spawns "Neffiken Lord Kelek-Vor" (210229) in `postorms` on event_signal.
154. Loot "Broken Sword Piece" (69903) from "Neffiken Lord Kelek-Vor".
155. Loot "Broken Sword Piece" (69903) from "Neffiken Lord of Kelek'Vor".
156. Say "Control Timer" to hateplaneb/"Maestro".
157. Spawns "Maestro of Rancor" (186111).
158. Loot "Broken Sword Piece" (69904) from "Maestro of Rancor".
159. **Broken:** no event trigger found for `hateplaneb/maestro#timer:popmaestro`.
160. Spawns "Maestro of Rancor" (186111) after `hateplaneb/maestro#timer:popmaestro`.
161. Loot "Broken Sword Piece" (69905) from "Kaniz Painbringer" in `potorment`.
162. sro/"Gilfal", hand "Baltron's Solvent" (69901). Sets `pre_pal` to `2`.
163. Ground spawn of "Rune of Xor" (69909) in `potranquility`.
164. Ground spawn of "Rune of Yirno" (69908) in `mistmoore`.
165. Ground spawn of "Rune of Zota" (69907) in `scarlet`.
166. Ground spawn of "Rune Wilun" (69910) in `gunthak`.
167. everfrost/"Rombus", hand "Rune of Zota" (69907) + "Rune of Yirno" (69908) + "Rune of Xor" (69909) + "Rune Wilun" (69910). Requires `pre_pal` ==2. Gives "Broken Sword Piece" (69906).
168. Combine in "Gilfal's Scabbard" (69902): "Broken Sword Piece" (69903), "Broken Sword Piece" (69904), "Broken Sword Piece" (69905), "Broken Sword Piece" (69906). Produces "Fractured Couragebringer" (69911). The combine does not fail.
169. sro/"Gilfal", hand "Fractured Couragebringer" (69911). Sets `pre_pal` to `4`.
170. everfrost/"Rombus", hand "Rune of Zota" (69907) + "Rune of Yirno" (69908) + "Rune of Xor" (69909) + "Rune Wilun" (69910). Sets `pre_pal` to `3`.
171. sro/"Gilfal", hand "Fractured Couragebringer" (69911). Requires `pre_pal` ==3. Gives "Fractured Couragebringer" (69912).
172. povalor/"Baltron Werters", hand "Fractured Couragebringer" (69912). Requires `pre_pal` ==4. Gives "Couragebringer" (69913).
173. hohonora/"Irak Altil", say "Hail". Sets `paladin_epic` to `6`.
174. Spawns "Durunal the Cursebearer" (300087) in `wallofslaughter` on enter.
175. Loot "Dark and Twisted Sword" (69971) from "Durunal the Cursebearer".
176. hohonora/"Irak Altil", hand "Dark and Twisted Sword" (69971). Requires `paladin_epic` ==6. Gives "Dark and Twisted Sword" (69972).

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
73. Combine in Forge (17): "Black Diamond of Nightmares" (29990), "Tempered Breastplate" (15999). Produces "Imbued Breastplate" (15985). Requires Blacksmithing 220. Trivial at 275.
74. poknowledge/"Aid Grimel", hand "Imbued Breastplate" (15985). Gives "Hardened Leather Signet" (16249).
75. poknowledge/"Aid Grimel", say "Skill In Brewing". Gives "Portable Drink Barrel" (17179).
76. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
77. qeynos/"Wolten Grafe", say "Crush The Undead". Gives "Box For Bones" (17941).
78. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
79. toxxulia/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
80. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). The combine does not fail.
81. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
82. qeynos2/"Phin Esrinap", say "Supplies". Gives "Message to Konem" (18921).
83. qeytoqrg/"Konem Matse", hand "Message to Konem" (18921). Gives "Grathin's Invoice" (18922).
84. qeynos2/"Phin Esrinap", hand "Grathin's Invoice" (18922). Gives "Water Flask" (13006).
85. Say "Tm Devrak Death" to rujd/"Rujd".
86. Spawns "spawn chest with Heavy Orcish Prison Key" (245241).
87. Loot "Pod of Water" (13044) from "spawn chest with Heavy Orcish Prison Key".
88. Say "Tm Dokorel Death" to rujd/"Rujd".
89. Say "Tm Velrek Death" to rujd/"Rujd".
90. Say "Researcher Death" to rujg/"Rujg".
91. Spawns "A Barrel" (260015).
92. Loot "Pod of Water" (13044) from "A Barrel".
93. 3 other loot steps also yield Pod of Water (13044).
94. Forage "Pod of Water" (13044) in `ruja`.
95. Forage "Pod of Water" (13044) in `uqua`.
96. Forage "Pod of Water" (13044) in `yxtta`.
97. Combine in Brew Barrel (19): "Bottle of Aged Bloodwine" (51163), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aged Bloodwine" (51164). Requires Brewing, trivial 255.
98. Combine in Brew Barrel (19): "Bottle of Aldo's Bitter Ale" (75805), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aldo's Bitter Ale" (75811). Requires Brewing, trivial 15.
99. 17 other recipes also produce Bottle (16598).
100. Combine in Brew Barrel (19): "Pod of Water" (13044), "Bottle" (16598). Produces "Water Flask" (13006). Requires Brewing, trivial 21.
101. Common item: Snake Scales (13070). Listed in 56 zones.
102. Combine in "Portable Drink Barrel" (17179): "Water Flask" (13006), "Snake Scales" (13070), "Bottle" (16598). Produces "Bog Juice" (16581). Requires Brewing, trivial 21.
103. Common item: Spit (17947). Listed in 34 zones.
104. Common item: Fire Beetle Eye (10307). Listed in 24 zones.
105. Spawns "Sepsis Rat" (45113) in `qcat` on event_death.
106. Loot "Rat Ears" (13072) from "Sepsis Rat".
107. Kill steamfont/"Diseased Female Rat". Spawns "A Young Plague Rat" (56086).
108. Loot "Rat Ears" (13072) from "A Young Plague Rat".
109. Kill steamfontmts/"Diseased Female Rat". Spawns "A Young Plague Rat" (448036).
110. Combine in "Spit" (17947): "Fire Beetle Eye" (10307), "Rat Ears" (13072). Produces "Edible Goo" (13498). Requires Baking, trivial 21.
111. freeporteast/"A Prisoner", hand "Bunker Cell #1" (12196) + "Edible Goo" (13498) + "Bog Juice" (16581). Gives "H. K. 102" (12143).
112. freportw/"A Prisoner", hand "Bunker Cell #1" (12196) + "Edible Goo" (13498) + "Bog Juice" (16581). Gives "H. K. 102" (12143).
113. highkeep/"Assistant Kiolna", hand "H. K. 102" (12143). Gives "Sealed Note" (18936).
114. paw/"Brother Hayle", hand "Sealed Note" (18936). Gives "Note" (18937).
115. southkarana/"Brother Hayle", hand "Sealed Note" (18936). Gives "Note" (18937).
116. Kill freportw/"Sir Lucan D-Lere". Spawns "Sir Lucan D'Lere" (9147).
117. Loot "Testimony of Truth" (18827) from "Sir Lucan D'Lere".
118. Loot "Testimony of Truth" (18827) from "Sir Lucan D'Lere" in `freeporteast`.
119. freeportwest/"Valeron Dushire", hand "Testimony of Truth" (18827). Gives "Brilliant Sword of Faith" (13947).
120. freportn/"Valeron Dushire", hand "Testimony of Truth" (18827). Gives "Brilliant Sword of Faith" (13947).
121. Hand "Token of Bravery" (12144) + "Token of Generosity" (13865) to freeportwest/"Merko Quetalis". Spawns "spawns Guard Willia" (383270). Loot "Token of Truth" (13866) from "spawns Guard Willia".
122. Hand "Token of Bravery" (12144) + "Token of Generosity" (13865) to freportn/"Merko Quetalis". Spawns "spawns Guard Willia" (8110). Loot "Token of Truth" (13866) from "spawns Guard Willia".
123. Loot "Token of Truth" (13866) from "Guard Willia".
124. freeportwest/"Merko Quetalis", hand "Token of Truth" (13866). Gives "Testimony" (18828).
125. freportn/"Merko Quetalis", hand "Token of Truth" (13866). Gives "Testimony" (18828).
126. Loot "Glowing Sword Hilt" (12197) from "Xicotl" in `mistmoore`.
127. paw/"Brother Hayle", hand "Glowing Sword Hilt" (12197) + "Brilliant Sword of Faith" (13947) + "Testimony" (18828) + "Note" (18937). Gives "SoulFire" (5504).
128. southkarana/"Brother Hayle", hand "Glowing Sword Hilt" (12197) + "Brilliant Sword of Faith" (13947) + "Testimony" (18828) + "Note" (18937). Gives "SoulFire" (5504).
129. airplane/"Inte Akera", hand "SoulFire" (5504). Gives "Inte's First Blessing" (18033).
130. lavastorm/"Ruathey", say "Bag". Gives "Nobleman's Bag" (17878).
131. Common item: Ghoul's Heart (2410). Listed in 8 zones.
132. No quest step gives Amstaf's Scroll (2411). The dump lists it in highkeep.
133. No quest step gives Blade of Nobility (2412). The dump lists it in butcher.
134. Loot "Hilt of the Nobleman" (2413) from "Ekeros" in `najena`.
135. Loot "Hilt of the Nobleman" (2413) from "A Skeleton" in `najena`.
136. Combine in "Nobleman's Bag" (17878): "Ghoul's Heart" (2410), "Amstaf's Scroll" (2411), "Blade of Nobility" (2412), "Hilt of the Nobleman" (2413). Produces "Ghoulbane" (5403). The combine does not fail.
137. airplane/"Inte Akera", hand "Ghoulbane" (5403). Gives "Inte's Second Blessing" (18034).
138. Hand "Miragul's Phylactery" (19072) to everfrost/"Lich Of Miragul". Spawns "Spawn Miragul" (30094). Loot "Miragul's Head" (19073) from "Spawn Miragul".
139. Loot "Miragul's Head" (19073) from "Miragul".
140. Hand "Miragul's Phylactery" (19072) to everfrost/"Lich Of Miragul". Spawns "Spawn Miragul" (30094). Loot "Miragul's Robe" (1254) from "Spawn Miragul".
141. Loot "Miragul's Robe" (1254) from "Miragul".
142. airplane/"Inte Akera", hand "Miragul's Robe" (1254) + "Inte's First Blessing" (18033) + "Inte's Second Blessing" (18034) + "Miragul's Head" (19073). Gives "Fiery Avenger" (11050).
143. fearplane/"Irak Altil", hand "Fiery Avenger" (11050) + "Mark of Atonement" (29010). Gives "Fiery Defender" (10099).
144. povalor/"Baltron Werters", say "Couragebringer". Sets `pre_pal` to `1`.
145. Requires `pre_pal` unset; no setter establishes this state.
146. povalor/"Baltron Werters", say "Couragebringer". Requires `pre_pal` unset. Gives "Baltron's Solvent" (69901).
147. sro/"Gilfal", hand "Baltron's Solvent" (69901). Requires `pre_pal` ==1. Gives "Gilfal's Scabbard" (69902).
148. Spawns "Neffiken Lord Kelek-Vor" (210229) in `postorms` on event_signal.
149. Loot "Broken Sword Piece" (69903) from "Neffiken Lord Kelek-Vor".
150. Loot "Broken Sword Piece" (69903) from "Neffiken Lord of Kelek'Vor".
151. Say "Control Timer" to hateplaneb/"Maestro".
152. Spawns "Maestro of Rancor" (186111).
153. Loot "Broken Sword Piece" (69904) from "Maestro of Rancor".
154. **Broken:** no event trigger found for `hateplaneb/maestro#timer:popmaestro`.
155. Spawns "Maestro of Rancor" (186111) after `hateplaneb/maestro#timer:popmaestro`.
156. Loot "Broken Sword Piece" (69905) from "Kaniz Painbringer" in `potorment`.
157. sro/"Gilfal", hand "Baltron's Solvent" (69901). Sets `pre_pal` to `2`.
158. Ground spawn of "Rune of Xor" (69909) in `potranquility`.
159. Ground spawn of "Rune of Yirno" (69908) in `mistmoore`.
160. Ground spawn of "Rune of Zota" (69907) in `scarlet`.
161. Ground spawn of "Rune Wilun" (69910) in `gunthak`.
162. everfrost/"Rombus", hand "Rune of Zota" (69907) + "Rune of Yirno" (69908) + "Rune of Xor" (69909) + "Rune Wilun" (69910). Requires `pre_pal` ==2. Gives "Broken Sword Piece" (69906).
163. Combine in "Gilfal's Scabbard" (69902): "Broken Sword Piece" (69903), "Broken Sword Piece" (69904), "Broken Sword Piece" (69905), "Broken Sword Piece" (69906). Produces "Fractured Couragebringer" (69911). The combine does not fail.
164. sro/"Gilfal", hand "Fractured Couragebringer" (69911). Sets `pre_pal` to `4`.
165. everfrost/"Rombus", hand "Rune of Zota" (69907) + "Rune of Yirno" (69908) + "Rune of Xor" (69909) + "Rune Wilun" (69910). Sets `pre_pal` to `3`.
166. sro/"Gilfal", hand "Fractured Couragebringer" (69911). Requires `pre_pal` ==3. Gives "Fractured Couragebringer" (69912).
167. povalor/"Baltron Werters", hand "Fractured Couragebringer" (69912). Requires `pre_pal` ==4. Gives "Couragebringer" (69913).
168. hohonora/"Irak Altil", say "Hail". Sets `paladin_epic` to `6`.
169. Spawns "Durunal the Cursebearer" (300087) in `wallofslaughter` on enter.
170. Loot "Dark and Twisted Sword" (69971) from "Durunal the Cursebearer".
171. hohonora/"Irak Altil", hand "Dark and Twisted Sword" (69971). Requires `paladin_epic` ==6. Gives "Dark and Twisted Sword" (69972).
172. Loot "Redis' Soulstone" (69983) from "Shade of Redis Linrok" in `dranikcatacombsa`.
173. Combine in "Dark and Twisted Sword" (69972): "Rithnok's Soulstone" (69941), "Drema's Soulstone" (69952), "Reiya's Soulstone" (69942), "Redis' Soulstone" (69983). Produces "Redemption" (64031). The combine does not fail.

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
74. freeporteast/"Tykar Renlin", hand "Drom's Champagne" (13829) + "Drom's Champagne" (13829) + "Drom's Champagne" (13829) + "Drom's Champagne" (13829). Gives "Bunker Cell #1" (12196).
75. freporte/"Tykar Renlin", hand "Drom's Champagne" (13829) + "Drom's Champagne" (13829) + "Drom's Champagne" (13829) + "Drom's Champagne" (13829). Gives "Bunker Cell #1" (12196).
76. Combine in "Portable Drink Barrel" (17179): "Water Flask" (13006), "Snake Scales" (13070), "Bottle" (16598). Produces "Bog Juice" (16581). Requires Brewing, trivial 21.
77. Combine in "Spit" (17947): "Fire Beetle Eye" (10307), "Rat Ears" (13072). Produces "Edible Goo" (13498). Requires Baking, trivial 21.
78. freeporteast/"A Prisoner", hand "Bunker Cell #1" (12196) + "Edible Goo" (13498) + "Bog Juice" (16581). Gives "H. K. 102" (12143).
79. freportw/"A Prisoner", hand "Bunker Cell #1" (12196) + "Edible Goo" (13498) + "Bog Juice" (16581). Gives "H. K. 102" (12143).
80. highkeep/"Assistant Kiolna", hand "H. K. 102" (12143). Gives "Sealed Note" (18936).
81. paw/"Brother Hayle", hand "Sealed Note" (18936). Gives "Note" (18937).
82. southkarana/"Brother Hayle", hand "Sealed Note" (18936). Gives "Note" (18937).
83. Kill freportw/"Sir Lucan D-Lere". Spawns "Sir Lucan D'Lere" (9147).
84. Loot "Testimony of Truth" (18827) from "Sir Lucan D'Lere".
85. Loot "Testimony of Truth" (18827) from "Sir Lucan D'Lere" in `freeporteast`.
86. freeportwest/"Valeron Dushire", hand "Testimony of Truth" (18827). Gives "Brilliant Sword of Faith" (13947).
87. freportn/"Valeron Dushire", hand "Testimony of Truth" (18827). Gives "Brilliant Sword of Faith" (13947).
88. Hand "Token of Bravery" (12144) + "Token of Generosity" (13865) to freeportwest/"Merko Quetalis". Spawns "spawns Guard Willia" (383270). Loot "Token of Truth" (13866) from "spawns Guard Willia".
89. Hand "Token of Bravery" (12144) + "Token of Generosity" (13865) to freportn/"Merko Quetalis". Spawns "spawns Guard Willia" (8110). Loot "Token of Truth" (13866) from "spawns Guard Willia".
90. Loot "Token of Truth" (13866) from "Guard Willia".
91. freeportwest/"Merko Quetalis", hand "Token of Truth" (13866). Gives "Testimony" (18828).
92. freportn/"Merko Quetalis", hand "Token of Truth" (13866). Gives "Testimony" (18828).
93. Loot "Glowing Sword Hilt" (12197) from "Xicotl" in `mistmoore`.
94. paw/"Brother Hayle", hand "Glowing Sword Hilt" (12197) + "Brilliant Sword of Faith" (13947) + "Testimony" (18828) + "Note" (18937). Gives "SoulFire" (5504).
95. southkarana/"Brother Hayle", hand "Glowing Sword Hilt" (12197) + "Brilliant Sword of Faith" (13947) + "Testimony" (18828) + "Note" (18937). Gives "SoulFire" (5504).
96. airplane/"Inte Akera", hand "SoulFire" (5504). Gives "Inte's First Blessing" (18033).
97. lavastorm/"Ruathey", say "Bag". Gives "Nobleman's Bag" (17878).
98. Common item: Ghoul's Heart (2410). Listed in 8 zones.
99. No quest step gives Amstaf's Scroll (2411). The dump lists it in highkeep.
100. No quest step gives Blade of Nobility (2412). The dump lists it in butcher.
101. Loot "Hilt of the Nobleman" (2413) from "Ekeros" in `najena`.
102. Loot "Hilt of the Nobleman" (2413) from "A Skeleton" in `najena`.
103. Combine in "Nobleman's Bag" (17878): "Ghoul's Heart" (2410), "Amstaf's Scroll" (2411), "Blade of Nobility" (2412), "Hilt of the Nobleman" (2413). Produces "Ghoulbane" (5403). The combine does not fail.
104. airplane/"Inte Akera", hand "Ghoulbane" (5403). Gives "Inte's Second Blessing" (18034).
105. Hand "Miragul's Phylactery" (19072) to everfrost/"Lich Of Miragul". Spawns "Spawn Miragul" (30094). Loot "Miragul's Head" (19073) from "Spawn Miragul".
106. Loot "Miragul's Head" (19073) from "Miragul".
107. Hand "Miragul's Phylactery" (19072) to everfrost/"Lich Of Miragul". Spawns "Spawn Miragul" (30094). Loot "Miragul's Robe" (1254) from "Spawn Miragul".
108. Loot "Miragul's Robe" (1254) from "Miragul".
109. airplane/"Inte Akera", hand "Miragul's Robe" (1254) + "Inte's First Blessing" (18033) + "Inte's Second Blessing" (18034) + "Miragul's Head" (19073). Gives "Fiery Avenger" (11050).
110. fearplane/"Irak Altil", hand "Fiery Avenger" (11050) + "Mark of Atonement" (29010). Gives "Fiery Defender" (10099).
111. povalor/"Baltron Werters", say "Couragebringer". Sets `pre_pal` to `1`.
112. Requires `pre_pal` unset; no setter establishes this state.
113. povalor/"Baltron Werters", say "Couragebringer". Requires `pre_pal` unset. Gives "Baltron's Solvent" (69901).
114. sro/"Gilfal", hand "Baltron's Solvent" (69901). Requires `pre_pal` ==1. Gives "Gilfal's Scabbard" (69902).
115. Spawns "Neffiken Lord Kelek-Vor" (210229) in `postorms` on event_signal.
116. Loot "Broken Sword Piece" (69903) from "Neffiken Lord Kelek-Vor".
117. Loot "Broken Sword Piece" (69903) from "Neffiken Lord of Kelek'Vor".
118. Say "Control Timer" to hateplaneb/"Maestro".
119. Spawns "Maestro of Rancor" (186111).
120. Loot "Broken Sword Piece" (69904) from "Maestro of Rancor".
121. **Broken:** no event trigger found for `hateplaneb/maestro#timer:popmaestro`.
122. Spawns "Maestro of Rancor" (186111) after `hateplaneb/maestro#timer:popmaestro`.
123. Loot "Broken Sword Piece" (69905) from "Kaniz Painbringer" in `potorment`.
124. sro/"Gilfal", hand "Baltron's Solvent" (69901). Sets `pre_pal` to `2`.
125. Ground spawn of "Rune of Xor" (69909) in `potranquility`.
126. Ground spawn of "Rune of Yirno" (69908) in `mistmoore`.
127. Ground spawn of "Rune of Zota" (69907) in `scarlet`.
128. Ground spawn of "Rune Wilun" (69910) in `gunthak`.
129. everfrost/"Rombus", hand "Rune of Zota" (69907) + "Rune of Yirno" (69908) + "Rune of Xor" (69909) + "Rune Wilun" (69910). Requires `pre_pal` ==2. Gives "Broken Sword Piece" (69906).
130. Combine in "Gilfal's Scabbard" (69902): "Broken Sword Piece" (69903), "Broken Sword Piece" (69904), "Broken Sword Piece" (69905), "Broken Sword Piece" (69906). Produces "Fractured Couragebringer" (69911). The combine does not fail.
131. sro/"Gilfal", hand "Fractured Couragebringer" (69911). Sets `pre_pal` to `4`.
132. everfrost/"Rombus", hand "Rune of Zota" (69907) + "Rune of Yirno" (69908) + "Rune of Xor" (69909) + "Rune Wilun" (69910). Sets `pre_pal` to `3`.
133. sro/"Gilfal", hand "Fractured Couragebringer" (69911). Requires `pre_pal` ==3. Gives "Fractured Couragebringer" (69912).
134. povalor/"Baltron Werters", hand "Fractured Couragebringer" (69912). Requires `pre_pal` ==4. Gives "Couragebringer" (69913).
135. hohonora/"Irak Altil", say "Hail". Sets `paladin_epic` to `6`.
136. Spawns "Durunal the Cursebearer" (300087) in `wallofslaughter` on enter.
137. Loot "Dark and Twisted Sword" (69971) from "Durunal the Cursebearer".
138. hohonora/"Irak Altil", hand "Dark and Twisted Sword" (69971). Requires `paladin_epic` ==6. Gives "Dark and Twisted Sword" (69972).
139. Loot "Redis' Soulstone" (69983) from "Shade of Redis Linrok" in `dranikcatacombsa`.
140. Combine in "Dark and Twisted Sword" (69972): "Rithnok's Soulstone" (69941), "Drema's Soulstone" (69952), "Reiya's Soulstone" (69942), "Redis' Soulstone" (69983). Produces "Redemption" (64031). The combine does not fail.
141. hohonora/"Irak Altil", say "Tell Me About Your Master". Sets `paladin_epic` to `9`.
142. erudnint/"Josper Kenshed", say "Collect Component". Gives "Empty Bag" (17944).
143. halas/"Lysbith Mcnaff", say "Protect The Pass". Gives "Empty Bag" (17944).
144. Loot "Goblin Ice Necklace" (13897) from "Redwind" in `everfrost`.
145. Loot "Goblin Ice Necklace" (13897) from "An Ice Goblin Scout" in `everfrost`.
146. Loot "Goblin Ice Necklace" (13897) from "An Ice Goblin Whelp" in `everfrost`.
147. Loot "Goblin Ice Necklace" (13897) from "An Icy Orc" in `everfrost`.
148. Loot "Goblin Ice Necklace" (13897) from "Ice Goblin Diver" in `everfrost`.
149. Combine in "Empty Bag" (17944): "Goblin Ice Necklace" (13897). Produces "Bag of Ice Necklaces" (13898). The combine does not fail.
150. halas/"Lysbith Mcnaff", hand "Bag of Ice Necklaces" (13898). Gives "Iron Ration" (13005).
151. Common item: Gnoll Fang (13915). Listed in 5 zones.
152. halas/"Lysbith Mcnaff", hand "Gnoll Fang" (13915) + "Gnoll Fang" (13915) + "Gnoll Fang" (13915). Gives "Iron Ration" (13005).
153. Requires `halloween_draykey_rations` unset; no setter establishes this state.
154. kithicor/"Old Man Draykey", say "Instructions". Requires `halloween_draykey_rations` unset. Gives "Iron Ration" (13005).
155. commons/"Kizdean Gix", say "Messages For Neriak". Gives "Sealed Letter" (18889).
156. neriakc/"Loveal S-Nez", hand "Sealed Letter" (18889). Gives "Iron Ration" (13005).
157. Summon "Black Diamond of Nightmares" (29990) by casting "Imbue Nightmare".
158. poknowledge/"Aid Grimel", say "Versed In The Art Of Smithing". Gives "Filthy Breastplate" (15984).
159. Combine in "Mixing Bowl" (17906): "Celestial Solvent" (9731), "Words of Acquisition (Beza)" (11866). Produces "Celestial Essence" (9650). Requires Baking, trivial 15. The combine does not fail.
160. Combine in "Mixing Bowl" (17906): "Celestial Solvent" (9731), "Words of Burnishing" (11862). Produces "Celestial Essence" (9650). Requires Baking, trivial 15. The combine does not fail.
161. 67 other recipes also produce Celestial Essence (9650).
162. Common item: Jar of Acid (22133). Listed in 15 zones.
163. Combine in Brew Barrel (19): "Celestial Essence" (9650), "Jar of Acid" (22133). Produces "Acid Wash" (15987). Requires Brewing, trivial 151.
164. Combine in Forge (17): "Filthy Breastplate" (15984), "Acid Wash" (15987). Produces "Cleansed Breastplate" (15998). Requires Blacksmithing, trivial 227.
165. Common item: Mortar and Pestle (17904). Listed in 12 zones.
166. No quest step gives Sandstorm Pearl (29909). The dump lists it in bothunder.
167. Combine in "Mortar and Pestle" (17904): "Sandstorm Pearl" (29909). Produces "Powdered Sandstorm Pearl" (29520) x4. Requires Make Poison, trivial 255.
168. Common item: Firing Sheet (16906). Listed in 34 zones.
169. Combine in Pottery Wheel (21): "Block of Clay" (16901), "Water Flask" (13006). Produces "Large Block of Clay" (16902). Requires Pottery, trivial 21.
170. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
171. qeynos2/"Phin Esrinap", hand "Grathin's Invoice" (18922). Gives "Water Flask" (13006).
172. Combine in Brew Barrel (19): "Pod of Water" (13044), "Bottle" (16598). Produces "Water Flask" (13006). Requires Brewing, trivial 21.
173. Common item: Large Bowl Sketch (16963). Listed in 29 zones.
174. Combine in Pottery Wheel (21): "Large Block of Clay" (16902), "Water Flask" (13006), "Large Bowl Sketch" (16963). Produces "Unfired Mixing Bowl" (16930). Requires Pottery, trivial 128.
175. Combine in Kiln (22): "Firing Sheet" (16906), "Unfired Mixing Bowl" (16930). Produces "Mixing Bowl" (17906). Requires Pottery, trivial 15.
176. Combine in "Mixing Bowl" (17906): "Sandstorm Pearl" (29909). Produces "Powdered Sandstorm Pearl" (29520) x4. Requires Baking. The combine does not fail.
177. Spawns "a Koka'Vor chieftain" (210236) in `postorms` on event_signal.
178. Loot "Storm Rider Blood" (29526) from "a Koka'Vor chieftain".
179. Loot "Storm Rider Blood" (29526) from "A stormrider" in `bothunder`.
180. Loot "Storm Rider Blood" (29526) from "Dolsoj Warrebs" in `bazaar`.
181. Loot "Storm Rider Blood" (29526) from "a Koka'Vor krovian" in `postorms`.
182. Loot "Storm Rider Blood" (29526) from "a Koka'Vor senvar" in `postorms`.
183. No quest step gives Drop of Pure Rain (29904). The dump lists it in bothunder.
184. Combine in Brew Barrel (19): "Powdered Sandstorm Pearl" (29520), "Storm Rider Blood" (29526), "Drop of Pure Rain" (29904). Produces "Hurricane Temper" (29533). Requires Brewing, trivial 135.
185. Combine in Forge (17): "Cleansed Breastplate" (15998), "Hurricane Temper" (29533). Produces "Tempered Breastplate" (15999). Requires Blacksmithing, trivial 229.
186. Combine in Forge (17): "Black Diamond of Nightmares" (29990), "Tempered Breastplate" (15999). Produces "Imbued Breastplate" (15985). Requires Blacksmithing 220. Trivial at 275.
187. poknowledge/"Aid Grimel", hand "Imbued Breastplate" (15985). Gives "Hardened Leather Signet" (16249).
188. poknowledge/"Aid Grimel", say "Skill In Brewing". Gives "Portable Drink Barrel" (17179).
189. Loot "Cask" (16580) from "Tugog Grigol" in `rathemtn`.
190. Common item: Hops (16591). Listed in 31 zones.
191. Common item: Malt (16595). Listed in 30 zones.
192. Common item: Yeast (16596). Listed in 30 zones.
193. Combine in "Portable Drink Barrel" (17179): "Cask" (16580), "Hops" (16591), "Malt" (16595), "Yeast" (16596). Produces "Mead" (13008). Requires Brewing, trivial 41.
194. erudnext/"Reklon Gnallen", hand "Iron Ration" (13005) + "Mead" (13008). Requires `paladin_epic` ==9. Gives "Erudin Prayer Bead" (69965).
195. Summon "Quiver of Marr" (17307) by casting "Quiver of Marr".
196. rathemtn/"Shin Master Grubbus", hand "Quiver of Marr" (17307). Requires `paladin_epic` ==9. Gives "Gukta Prayer Bead" (69964).
197. Common item: Barley (16590). Listed in 28 zones.
198. Combine in Brew Barrel (19): "Bottle of Aged Bloodwine" (51163), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aged Bloodwine" (51164). Requires Brewing, trivial 255.
199. Combine in Brew Barrel (19): "Bottle of Aldo's Bitter Ale" (75805), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aldo's Bitter Ale" (75811). Requires Brewing, trivial 15.
200. 17 other recipes also produce Bottle (16598).
201. Combine in "Medicine Bag" (17901): "Hand-Formed Bottle" (45232), "Ensnaring Concoction V" (45236). Produces "Empty Vial" (10062), "Cork" (16851), "Formed Ensnaring Concoction V" (45258). Requires Alchemy, trivial 41.
202. Combine in Brew Barrel (19): "Bottle of Aged Bloodwine" (51163), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aged Bloodwine" (51164). Requires Brewing, trivial 255.
203. 11 other recipes also produce Cork (16851).
204. Combine in "Portable Drink Barrel" (17179): "Water Flask" (13006), "Celestial Essence" (9650). Produces "Purified Water" (12607). Requires Brewing, trivial 58.
205. Combine in "Tracker's Water Extractor" (17987): "Purification Tablet" (12630), "Water Reed" (12778). Produces "Purified Water" (12607) x3. Requires Pottery. The combine does not fail.
206. 3 other recipes also produce Purified Water (12607).
207. Forage "Sand Verbena" (65582) in `taka`.
208. Forage "Sand Verbena" (65582) in `takb`.
209. Forage "Sand Verbena" (65582) in `takc`.
210. Forage "Sand Verbena" (65582) in `takd`.
211. Forage "Sand Verbena" (65582) in `take`.
212. Forage "Sand Verbena" (65582) in `takf`.
213. Forage "Sand Verbena" (65582) in `takg`.
214. Forage "Sand Verbena" (65582) in `takh`.
215. Forage "Sand Verbena" (65582) in `taki`.
216. Forage "Sand Verbena" (65582) in `takj`.
217. Combine in Brew Barrel (19): "Barley" (16590), "Bottle" (16598), "Cork" (16851), "Hops" (16591), "Purified Water" (12607), "Sand Verbena" (65582), "Yeast" (16596). Produces "Bottle of Double Brewed Double Dry Stout" (51157). Requires Brewing, trivial 226.
218. kaladimb/"Datur Nightseer", hand "Bottle of Double Brewed Double Dry Stout" (51157). Requires `paladin_epic` ==9. Gives "Kaladim Prayer Bead" (69963).
219. felwithea/"General Jyleel", hand platinum:1000. Requires `paladin_epic` ==9. Gives "Felwithe Prayer Bead" (69962).
220. Ground spawn of "Freeport Prayer Bead" (69961) in `freeportwest`.
221. Ground spawn of "Freeport Prayer Bead" (69961) in `freportn`.
222. qeynos2/"Ziska Ironforge", hand platinum:500. Requires `paladin_epic` ==9. Gives "Qeynos Prayer Bead" (69960).
223. Combine in "Unfilled Set of Prayer Beads" (69968): "Rivervale Prayer Bead" (69967), "Ak'anon Prayer Bead" (69966), "Erudin Prayer Bead" (69965), "Gukta Prayer Bead" (69964), "Kaladim Prayer Bead" (69963), "Felwithe Prayer Bead" (69962), "Freeport Prayer Bead" (69961), "Qeynos Prayer Bead" (69960). Produces "Set of Prayer Beads" (69969). The combine does not fail.
224. dranikhollowsc/"Anetal", hand "Set of Prayer Beads" (69969). Sets `paladin_epic_hollowc` to `2`.
225. natimbi/"Kemik Arulon", hand "Set of Prayer Beads" (69969). Sets `paladin_epic_hollowc` to `1`.
226. natimbi/"Kemik Arulon", say "Hail". Requires `paladin_epic_hollowc` ==2. Requires `paladin_epic_hollowc` ==1. Gives "Token of Compassion" (69953).

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
74. highkeep/"Assistant Kiolna", hand "H. K. 102" (12143). Gives "Sealed Note" (18936).
75. paw/"Brother Hayle", hand "Sealed Note" (18936). Gives "Note" (18937).
76. southkarana/"Brother Hayle", hand "Sealed Note" (18936). Gives "Note" (18937).
77. Kill freportw/"Sir Lucan D-Lere". Spawns "Sir Lucan D'Lere" (9147).
78. Loot "Testimony of Truth" (18827) from "Sir Lucan D'Lere".
79. Loot "Testimony of Truth" (18827) from "Sir Lucan D'Lere" in `freeporteast`.
80. freeportwest/"Valeron Dushire", hand "Testimony of Truth" (18827). Gives "Brilliant Sword of Faith" (13947).
81. freportn/"Valeron Dushire", hand "Testimony of Truth" (18827). Gives "Brilliant Sword of Faith" (13947).
82. Hand "Token of Bravery" (12144) + "Token of Generosity" (13865) to freeportwest/"Merko Quetalis". Spawns "spawns Guard Willia" (383270). Loot "Token of Truth" (13866) from "spawns Guard Willia".
83. Hand "Token of Bravery" (12144) + "Token of Generosity" (13865) to freportn/"Merko Quetalis". Spawns "spawns Guard Willia" (8110). Loot "Token of Truth" (13866) from "spawns Guard Willia".
84. Loot "Token of Truth" (13866) from "Guard Willia".
85. freeportwest/"Merko Quetalis", hand "Token of Truth" (13866). Gives "Testimony" (18828).
86. freportn/"Merko Quetalis", hand "Token of Truth" (13866). Gives "Testimony" (18828).
87. Loot "Glowing Sword Hilt" (12197) from "Xicotl" in `mistmoore`.
88. paw/"Brother Hayle", hand "Glowing Sword Hilt" (12197) + "Brilliant Sword of Faith" (13947) + "Testimony" (18828) + "Note" (18937). Gives "SoulFire" (5504).
89. southkarana/"Brother Hayle", hand "Glowing Sword Hilt" (12197) + "Brilliant Sword of Faith" (13947) + "Testimony" (18828) + "Note" (18937). Gives "SoulFire" (5504).
90. airplane/"Inte Akera", hand "SoulFire" (5504). Gives "Inte's First Blessing" (18033).
91. lavastorm/"Ruathey", say "Bag". Gives "Nobleman's Bag" (17878).
92. Common item: Ghoul's Heart (2410). Listed in 8 zones.
93. No quest step gives Amstaf's Scroll (2411). The dump lists it in highkeep.
94. No quest step gives Blade of Nobility (2412). The dump lists it in butcher.
95. Loot "Hilt of the Nobleman" (2413) from "Ekeros" in `najena`.
96. Loot "Hilt of the Nobleman" (2413) from "A Skeleton" in `najena`.
97. Combine in "Nobleman's Bag" (17878): "Ghoul's Heart" (2410), "Amstaf's Scroll" (2411), "Blade of Nobility" (2412), "Hilt of the Nobleman" (2413). Produces "Ghoulbane" (5403). The combine does not fail.
98. airplane/"Inte Akera", hand "Ghoulbane" (5403). Gives "Inte's Second Blessing" (18034).
99. Hand "Miragul's Phylactery" (19072) to everfrost/"Lich Of Miragul". Spawns "Spawn Miragul" (30094). Loot "Miragul's Head" (19073) from "Spawn Miragul".
100. Loot "Miragul's Head" (19073) from "Miragul".
101. Hand "Miragul's Phylactery" (19072) to everfrost/"Lich Of Miragul". Spawns "Spawn Miragul" (30094). Loot "Miragul's Robe" (1254) from "Spawn Miragul".
102. Loot "Miragul's Robe" (1254) from "Miragul".
103. airplane/"Inte Akera", hand "Miragul's Robe" (1254) + "Inte's First Blessing" (18033) + "Inte's Second Blessing" (18034) + "Miragul's Head" (19073). Gives "Fiery Avenger" (11050).
104. fearplane/"Irak Altil", hand "Fiery Avenger" (11050) + "Mark of Atonement" (29010). Gives "Fiery Defender" (10099).
105. povalor/"Baltron Werters", say "Couragebringer". Sets `pre_pal` to `1`.
106. Requires `pre_pal` unset; no setter establishes this state.
107. povalor/"Baltron Werters", say "Couragebringer". Requires `pre_pal` unset. Gives "Baltron's Solvent" (69901).
108. sro/"Gilfal", hand "Baltron's Solvent" (69901). Requires `pre_pal` ==1. Gives "Gilfal's Scabbard" (69902).
109. Spawns "Neffiken Lord Kelek-Vor" (210229) in `postorms` on event_signal.
110. Loot "Broken Sword Piece" (69903) from "Neffiken Lord Kelek-Vor".
111. Loot "Broken Sword Piece" (69903) from "Neffiken Lord of Kelek'Vor".
112. Say "Control Timer" to hateplaneb/"Maestro".
113. Spawns "Maestro of Rancor" (186111).
114. Loot "Broken Sword Piece" (69904) from "Maestro of Rancor".
115. **Broken:** no event trigger found for `hateplaneb/maestro#timer:popmaestro`.
116. Spawns "Maestro of Rancor" (186111) after `hateplaneb/maestro#timer:popmaestro`.
117. Loot "Broken Sword Piece" (69905) from "Kaniz Painbringer" in `potorment`.
118. sro/"Gilfal", hand "Baltron's Solvent" (69901). Sets `pre_pal` to `2`.
119. Ground spawn of "Rune of Xor" (69909) in `potranquility`.
120. Ground spawn of "Rune of Yirno" (69908) in `mistmoore`.
121. Ground spawn of "Rune of Zota" (69907) in `scarlet`.
122. Ground spawn of "Rune Wilun" (69910) in `gunthak`.
123. everfrost/"Rombus", hand "Rune of Zota" (69907) + "Rune of Yirno" (69908) + "Rune of Xor" (69909) + "Rune Wilun" (69910). Requires `pre_pal` ==2. Gives "Broken Sword Piece" (69906).
124. Combine in "Gilfal's Scabbard" (69902): "Broken Sword Piece" (69903), "Broken Sword Piece" (69904), "Broken Sword Piece" (69905), "Broken Sword Piece" (69906). Produces "Fractured Couragebringer" (69911). The combine does not fail.
125. sro/"Gilfal", hand "Fractured Couragebringer" (69911). Sets `pre_pal` to `4`.
126. everfrost/"Rombus", hand "Rune of Zota" (69907) + "Rune of Yirno" (69908) + "Rune of Xor" (69909) + "Rune Wilun" (69910). Sets `pre_pal` to `3`.
127. sro/"Gilfal", hand "Fractured Couragebringer" (69911). Requires `pre_pal` ==3. Gives "Fractured Couragebringer" (69912).
128. povalor/"Baltron Werters", hand "Fractured Couragebringer" (69912). Requires `pre_pal` ==4. Gives "Couragebringer" (69913).
129. hohonora/"Irak Altil", say "Hail". Sets `paladin_epic` to `6`.
130. Spawns "Durunal the Cursebearer" (300087) in `wallofslaughter` on enter.
131. Loot "Dark and Twisted Sword" (69971) from "Durunal the Cursebearer".
132. hohonora/"Irak Altil", hand "Dark and Twisted Sword" (69971). Requires `paladin_epic` ==6. Gives "Dark and Twisted Sword" (69972).
133. Loot "Redis' Soulstone" (69983) from "Shade of Redis Linrok" in `dranikcatacombsa`.
134. Combine in "Dark and Twisted Sword" (69972): "Rithnok's Soulstone" (69941), "Drema's Soulstone" (69952), "Reiya's Soulstone" (69942), "Redis' Soulstone" (69983). Produces "Redemption" (64031). The combine does not fail.
135. hohonora/"Irak Altil", say "Tell Me About Your Master". Sets `paladin_epic` to `9`.
136. erudnint/"Josper Kenshed", say "Collect Component". Gives "Empty Bag" (17944).
137. halas/"Lysbith Mcnaff", say "Protect The Pass". Gives "Empty Bag" (17944).
138. Loot "Goblin Ice Necklace" (13897) from "Redwind" in `everfrost`.
139. Loot "Goblin Ice Necklace" (13897) from "An Ice Goblin Scout" in `everfrost`.
140. Loot "Goblin Ice Necklace" (13897) from "An Ice Goblin Whelp" in `everfrost`.
141. Loot "Goblin Ice Necklace" (13897) from "An Icy Orc" in `everfrost`.
142. Loot "Goblin Ice Necklace" (13897) from "Ice Goblin Diver" in `everfrost`.
143. Combine in "Empty Bag" (17944): "Goblin Ice Necklace" (13897). Produces "Bag of Ice Necklaces" (13898). The combine does not fail.
144. halas/"Lysbith Mcnaff", hand "Bag of Ice Necklaces" (13898). Gives "Iron Ration" (13005).
145. Common item: Gnoll Fang (13915). Listed in 5 zones.
146. halas/"Lysbith Mcnaff", hand "Gnoll Fang" (13915) + "Gnoll Fang" (13915) + "Gnoll Fang" (13915). Gives "Iron Ration" (13005).
147. Requires `halloween_draykey_rations` unset; no setter establishes this state.
148. kithicor/"Old Man Draykey", say "Instructions". Requires `halloween_draykey_rations` unset. Gives "Iron Ration" (13005).
149. commons/"Kizdean Gix", say "Messages For Neriak". Gives "Sealed Letter" (18889).
150. neriakc/"Loveal S-Nez", hand "Sealed Letter" (18889). Gives "Iron Ration" (13005).
151. Summon "Black Diamond of Nightmares" (29990) by casting "Imbue Nightmare".
152. poknowledge/"Aid Grimel", say "Versed In The Art Of Smithing". Gives "Filthy Breastplate" (15984).
153. Combine in "Mixing Bowl" (17906): "Celestial Solvent" (9731), "Words of Acquisition (Beza)" (11866). Produces "Celestial Essence" (9650). Requires Baking, trivial 15. The combine does not fail.
154. Combine in "Mixing Bowl" (17906): "Celestial Solvent" (9731), "Words of Burnishing" (11862). Produces "Celestial Essence" (9650). Requires Baking, trivial 15. The combine does not fail.
155. 67 other recipes also produce Celestial Essence (9650).
156. Common item: Jar of Acid (22133). Listed in 15 zones.
157. Combine in Brew Barrel (19): "Celestial Essence" (9650), "Jar of Acid" (22133). Produces "Acid Wash" (15987). Requires Brewing, trivial 151.
158. Combine in Forge (17): "Filthy Breastplate" (15984), "Acid Wash" (15987). Produces "Cleansed Breastplate" (15998). Requires Blacksmithing, trivial 227.
159. Common item: Mortar and Pestle (17904). Listed in 12 zones.
160. No quest step gives Sandstorm Pearl (29909). The dump lists it in bothunder.
161. Combine in "Mortar and Pestle" (17904): "Sandstorm Pearl" (29909). Produces "Powdered Sandstorm Pearl" (29520) x4. Requires Make Poison, trivial 255.
162. Combine in Kiln (22): "Firing Sheet" (16906), "Unfired Mixing Bowl" (16930). Produces "Mixing Bowl" (17906). Requires Pottery, trivial 15.
163. Combine in "Mixing Bowl" (17906): "Sandstorm Pearl" (29909). Produces "Powdered Sandstorm Pearl" (29520) x4. Requires Baking. The combine does not fail.
164. Spawns "a Koka'Vor chieftain" (210236) in `postorms` on event_signal.
165. Loot "Storm Rider Blood" (29526) from "a Koka'Vor chieftain".
166. Loot "Storm Rider Blood" (29526) from "A stormrider" in `bothunder`.
167. Loot "Storm Rider Blood" (29526) from "Dolsoj Warrebs" in `bazaar`.
168. Loot "Storm Rider Blood" (29526) from "a Koka'Vor krovian" in `postorms`.
169. Loot "Storm Rider Blood" (29526) from "a Koka'Vor senvar" in `postorms`.
170. No quest step gives Drop of Pure Rain (29904). The dump lists it in bothunder.
171. Combine in Brew Barrel (19): "Powdered Sandstorm Pearl" (29520), "Storm Rider Blood" (29526), "Drop of Pure Rain" (29904). Produces "Hurricane Temper" (29533). Requires Brewing, trivial 135.
172. Combine in Forge (17): "Cleansed Breastplate" (15998), "Hurricane Temper" (29533). Produces "Tempered Breastplate" (15999). Requires Blacksmithing, trivial 229.
173. Combine in Forge (17): "Black Diamond of Nightmares" (29990), "Tempered Breastplate" (15999). Produces "Imbued Breastplate" (15985). Requires Blacksmithing 220. Trivial at 275.
174. poknowledge/"Aid Grimel", hand "Imbued Breastplate" (15985). Gives "Hardened Leather Signet" (16249).
175. poknowledge/"Aid Grimel", say "Skill In Brewing". Gives "Portable Drink Barrel" (17179).
176. Loot "Cask" (16580) from "Tugog Grigol" in `rathemtn`.
177. Common item: Hops (16591). Listed in 31 zones.
178. Common item: Malt (16595). Listed in 30 zones.
179. Common item: Yeast (16596). Listed in 30 zones.
180. Combine in "Portable Drink Barrel" (17179): "Cask" (16580), "Hops" (16591), "Malt" (16595), "Yeast" (16596). Produces "Mead" (13008). Requires Brewing, trivial 41.
181. erudnext/"Reklon Gnallen", hand "Iron Ration" (13005) + "Mead" (13008). Requires `paladin_epic` ==9. Gives "Erudin Prayer Bead" (69965).
182. Summon "Quiver of Marr" (17307) by casting "Quiver of Marr".
183. rathemtn/"Shin Master Grubbus", hand "Quiver of Marr" (17307). Requires `paladin_epic` ==9. Gives "Gukta Prayer Bead" (69964).
184. Common item: Barley (16590). Listed in 28 zones.
185. Combine in Brew Barrel (19): "Bottle of Aged Bloodwine" (51163), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aged Bloodwine" (51164). Requires Brewing, trivial 255.
186. Combine in Brew Barrel (19): "Bottle of Aldo's Bitter Ale" (75805), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aldo's Bitter Ale" (75811). Requires Brewing, trivial 15.
187. 17 other recipes also produce Bottle (16598).
188. Combine in "Medicine Bag" (17901): "Hand-Formed Bottle" (45232), "Ensnaring Concoction V" (45236). Produces "Empty Vial" (10062), "Cork" (16851), "Formed Ensnaring Concoction V" (45258). Requires Alchemy, trivial 41.
189. Combine in Brew Barrel (19): "Bottle of Aged Bloodwine" (51163), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aged Bloodwine" (51164). Requires Brewing, trivial 255.
190. 11 other recipes also produce Cork (16851).
191. Combine in "Portable Drink Barrel" (17179): "Water Flask" (13006), "Celestial Essence" (9650). Produces "Purified Water" (12607). Requires Brewing, trivial 58.
192. Combine in "Tracker's Water Extractor" (17987): "Purification Tablet" (12630), "Water Reed" (12778). Produces "Purified Water" (12607) x3. Requires Pottery. The combine does not fail.
193. 3 other recipes also produce Purified Water (12607).
194. Forage "Sand Verbena" (65582) in `taka`.
195. Forage "Sand Verbena" (65582) in `takb`.
196. Forage "Sand Verbena" (65582) in `takc`.
197. Forage "Sand Verbena" (65582) in `takd`.
198. Forage "Sand Verbena" (65582) in `take`.
199. Forage "Sand Verbena" (65582) in `takf`.
200. Forage "Sand Verbena" (65582) in `takg`.
201. Forage "Sand Verbena" (65582) in `takh`.
202. Forage "Sand Verbena" (65582) in `taki`.
203. Forage "Sand Verbena" (65582) in `takj`.
204. Combine in Brew Barrel (19): "Barley" (16590), "Bottle" (16598), "Cork" (16851), "Hops" (16591), "Purified Water" (12607), "Sand Verbena" (65582), "Yeast" (16596). Produces "Bottle of Double Brewed Double Dry Stout" (51157). Requires Brewing, trivial 226.
205. kaladimb/"Datur Nightseer", hand "Bottle of Double Brewed Double Dry Stout" (51157). Requires `paladin_epic` ==9. Gives "Kaladim Prayer Bead" (69963).
206. felwithea/"General Jyleel", hand platinum:1000. Requires `paladin_epic` ==9. Gives "Felwithe Prayer Bead" (69962).
207. Ground spawn of "Freeport Prayer Bead" (69961) in `freeportwest`.
208. Ground spawn of "Freeport Prayer Bead" (69961) in `freportn`.
209. qeynos2/"Ziska Ironforge", hand platinum:500. Requires `paladin_epic` ==9. Gives "Qeynos Prayer Bead" (69960).
210. Combine in "Unfilled Set of Prayer Beads" (69968): "Rivervale Prayer Bead" (69967), "Ak'anon Prayer Bead" (69966), "Erudin Prayer Bead" (69965), "Gukta Prayer Bead" (69964), "Kaladim Prayer Bead" (69963), "Felwithe Prayer Bead" (69962), "Freeport Prayer Bead" (69961), "Qeynos Prayer Bead" (69960). Produces "Set of Prayer Beads" (69969). The combine does not fail.
211. dranikhollowsc/"Anetal", hand "Set of Prayer Beads" (69969). Sets `paladin_epic_hollowc` to `2`.
212. natimbi/"Kemik Arulon", hand "Set of Prayer Beads" (69969). Sets `paladin_epic_hollowc` to `1`.
213. natimbi/"Kemik Arulon", say "Hail". Requires `paladin_epic_hollowc` ==2. Requires `paladin_epic_hollowc` ==1. Gives "Token of Compassion" (69953).
214. Requires `pal_chest_keel` unset; no setter establishes this state.
215. oasis/"Paladin Epic", say "Hail". Requires `pal_chest_keel` unset. Gives "Keelee's Brooch" (69982).
216. oasis/"Paladin Epic", say "Keelee Say". Gives "Keelee's Brooch" (69982).
217. sro/"Instructor Maerceci", hand "Keelee's Brooch" (69982). Gives "Token of Chivalry" (69954).

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
74. freeporteast/"A Prisoner", hand "Bunker Cell #1" (12196) + "Edible Goo" (13498) + "Bog Juice" (16581). Gives "H. K. 102" (12143).
75. freportw/"A Prisoner", hand "Bunker Cell #1" (12196) + "Edible Goo" (13498) + "Bog Juice" (16581). Gives "H. K. 102" (12143).
76. highkeep/"Assistant Kiolna", hand "H. K. 102" (12143). Gives "Sealed Note" (18936).
77. paw/"Brother Hayle", hand "Sealed Note" (18936). Gives "Note" (18937).
78. southkarana/"Brother Hayle", hand "Sealed Note" (18936). Gives "Note" (18937).
79. Kill freportw/"Sir Lucan D-Lere". Spawns "Sir Lucan D'Lere" (9147).
80. Loot "Testimony of Truth" (18827) from "Sir Lucan D'Lere".
81. Loot "Testimony of Truth" (18827) from "Sir Lucan D'Lere" in `freeporteast`.
82. freeportwest/"Valeron Dushire", hand "Testimony of Truth" (18827). Gives "Brilliant Sword of Faith" (13947).
83. freportn/"Valeron Dushire", hand "Testimony of Truth" (18827). Gives "Brilliant Sword of Faith" (13947).
84. Hand "Token of Bravery" (12144) + "Token of Generosity" (13865) to freeportwest/"Merko Quetalis". Spawns "spawns Guard Willia" (383270). Loot "Token of Truth" (13866) from "spawns Guard Willia".
85. Hand "Token of Bravery" (12144) + "Token of Generosity" (13865) to freportn/"Merko Quetalis". Spawns "spawns Guard Willia" (8110). Loot "Token of Truth" (13866) from "spawns Guard Willia".
86. Loot "Token of Truth" (13866) from "Guard Willia".
87. freeportwest/"Merko Quetalis", hand "Token of Truth" (13866). Gives "Testimony" (18828).
88. freportn/"Merko Quetalis", hand "Token of Truth" (13866). Gives "Testimony" (18828).
89. Loot "Glowing Sword Hilt" (12197) from "Xicotl" in `mistmoore`.
90. paw/"Brother Hayle", hand "Glowing Sword Hilt" (12197) + "Brilliant Sword of Faith" (13947) + "Testimony" (18828) + "Note" (18937). Gives "SoulFire" (5504).
91. southkarana/"Brother Hayle", hand "Glowing Sword Hilt" (12197) + "Brilliant Sword of Faith" (13947) + "Testimony" (18828) + "Note" (18937). Gives "SoulFire" (5504).
92. airplane/"Inte Akera", hand "SoulFire" (5504). Gives "Inte's First Blessing" (18033).
93. lavastorm/"Ruathey", say "Bag". Gives "Nobleman's Bag" (17878).
94. Common item: Ghoul's Heart (2410). Listed in 8 zones.
95. No quest step gives Amstaf's Scroll (2411). The dump lists it in highkeep.
96. No quest step gives Blade of Nobility (2412). The dump lists it in butcher.
97. Loot "Hilt of the Nobleman" (2413) from "Ekeros" in `najena`.
98. Loot "Hilt of the Nobleman" (2413) from "A Skeleton" in `najena`.
99. Combine in "Nobleman's Bag" (17878): "Ghoul's Heart" (2410), "Amstaf's Scroll" (2411), "Blade of Nobility" (2412), "Hilt of the Nobleman" (2413). Produces "Ghoulbane" (5403). The combine does not fail.
100. airplane/"Inte Akera", hand "Ghoulbane" (5403). Gives "Inte's Second Blessing" (18034).
101. Hand "Miragul's Phylactery" (19072) to everfrost/"Lich Of Miragul". Spawns "Spawn Miragul" (30094). Loot "Miragul's Head" (19073) from "Spawn Miragul".
102. Loot "Miragul's Head" (19073) from "Miragul".
103. Hand "Miragul's Phylactery" (19072) to everfrost/"Lich Of Miragul". Spawns "Spawn Miragul" (30094). Loot "Miragul's Robe" (1254) from "Spawn Miragul".
104. Loot "Miragul's Robe" (1254) from "Miragul".
105. airplane/"Inte Akera", hand "Miragul's Robe" (1254) + "Inte's First Blessing" (18033) + "Inte's Second Blessing" (18034) + "Miragul's Head" (19073). Gives "Fiery Avenger" (11050).
106. fearplane/"Irak Altil", hand "Fiery Avenger" (11050) + "Mark of Atonement" (29010). Gives "Fiery Defender" (10099).
107. povalor/"Baltron Werters", say "Couragebringer". Sets `pre_pal` to `1`.
108. Requires `pre_pal` unset; no setter establishes this state.
109. povalor/"Baltron Werters", say "Couragebringer". Requires `pre_pal` unset. Gives "Baltron's Solvent" (69901).
110. sro/"Gilfal", hand "Baltron's Solvent" (69901). Requires `pre_pal` ==1. Gives "Gilfal's Scabbard" (69902).
111. Spawns "Neffiken Lord Kelek-Vor" (210229) in `postorms` on event_signal.
112. Loot "Broken Sword Piece" (69903) from "Neffiken Lord Kelek-Vor".
113. Loot "Broken Sword Piece" (69903) from "Neffiken Lord of Kelek'Vor".
114. Say "Control Timer" to hateplaneb/"Maestro".
115. Spawns "Maestro of Rancor" (186111).
116. Loot "Broken Sword Piece" (69904) from "Maestro of Rancor".
117. **Broken:** no event trigger found for `hateplaneb/maestro#timer:popmaestro`.
118. Spawns "Maestro of Rancor" (186111) after `hateplaneb/maestro#timer:popmaestro`.
119. Loot "Broken Sword Piece" (69905) from "Kaniz Painbringer" in `potorment`.
120. sro/"Gilfal", hand "Baltron's Solvent" (69901). Sets `pre_pal` to `2`.
121. Ground spawn of "Rune of Xor" (69909) in `potranquility`.
122. Ground spawn of "Rune of Yirno" (69908) in `mistmoore`.
123. Ground spawn of "Rune of Zota" (69907) in `scarlet`.
124. Ground spawn of "Rune Wilun" (69910) in `gunthak`.
125. everfrost/"Rombus", hand "Rune of Zota" (69907) + "Rune of Yirno" (69908) + "Rune of Xor" (69909) + "Rune Wilun" (69910). Requires `pre_pal` ==2. Gives "Broken Sword Piece" (69906).
126. Combine in "Gilfal's Scabbard" (69902): "Broken Sword Piece" (69903), "Broken Sword Piece" (69904), "Broken Sword Piece" (69905), "Broken Sword Piece" (69906). Produces "Fractured Couragebringer" (69911). The combine does not fail.
127. sro/"Gilfal", hand "Fractured Couragebringer" (69911). Sets `pre_pal` to `4`.
128. everfrost/"Rombus", hand "Rune of Zota" (69907) + "Rune of Yirno" (69908) + "Rune of Xor" (69909) + "Rune Wilun" (69910). Sets `pre_pal` to `3`.
129. sro/"Gilfal", hand "Fractured Couragebringer" (69911). Requires `pre_pal` ==3. Gives "Fractured Couragebringer" (69912).
130. povalor/"Baltron Werters", hand "Fractured Couragebringer" (69912). Requires `pre_pal` ==4. Gives "Couragebringer" (69913).
131. hohonora/"Irak Altil", say "Hail". Sets `paladin_epic` to `6`.
132. Spawns "Durunal the Cursebearer" (300087) in `wallofslaughter` on enter.
133. Loot "Dark and Twisted Sword" (69971) from "Durunal the Cursebearer".
134. hohonora/"Irak Altil", hand "Dark and Twisted Sword" (69971). Requires `paladin_epic` ==6. Gives "Dark and Twisted Sword" (69972).
135. Loot "Redis' Soulstone" (69983) from "Shade of Redis Linrok" in `dranikcatacombsa`.
136. Combine in "Dark and Twisted Sword" (69972): "Rithnok's Soulstone" (69941), "Drema's Soulstone" (69952), "Reiya's Soulstone" (69942), "Redis' Soulstone" (69983). Produces "Redemption" (64031). The combine does not fail.
137. hohonora/"Irak Altil", say "Tell Me About Your Master". Sets `paladin_epic` to `9`.
138. erudnint/"Josper Kenshed", say "Collect Component". Gives "Empty Bag" (17944).
139. halas/"Lysbith Mcnaff", say "Protect The Pass". Gives "Empty Bag" (17944).
140. Loot "Goblin Ice Necklace" (13897) from "Redwind" in `everfrost`.
141. Loot "Goblin Ice Necklace" (13897) from "An Ice Goblin Scout" in `everfrost`.
142. Loot "Goblin Ice Necklace" (13897) from "An Ice Goblin Whelp" in `everfrost`.
143. Loot "Goblin Ice Necklace" (13897) from "An Icy Orc" in `everfrost`.
144. Loot "Goblin Ice Necklace" (13897) from "Ice Goblin Diver" in `everfrost`.
145. Combine in "Empty Bag" (17944): "Goblin Ice Necklace" (13897). Produces "Bag of Ice Necklaces" (13898). The combine does not fail.
146. halas/"Lysbith Mcnaff", hand "Bag of Ice Necklaces" (13898). Gives "Iron Ration" (13005).
147. Common item: Gnoll Fang (13915). Listed in 5 zones.
148. halas/"Lysbith Mcnaff", hand "Gnoll Fang" (13915) + "Gnoll Fang" (13915) + "Gnoll Fang" (13915). Gives "Iron Ration" (13005).
149. Requires `halloween_draykey_rations` unset; no setter establishes this state.
150. kithicor/"Old Man Draykey", say "Instructions". Requires `halloween_draykey_rations` unset. Gives "Iron Ration" (13005).
151. commons/"Kizdean Gix", say "Messages For Neriak". Gives "Sealed Letter" (18889).
152. neriakc/"Loveal S-Nez", hand "Sealed Letter" (18889). Gives "Iron Ration" (13005).
153. Summon "Black Diamond of Nightmares" (29990) by casting "Imbue Nightmare".
154. poknowledge/"Aid Grimel", say "Versed In The Art Of Smithing". Gives "Filthy Breastplate" (15984).
155. Combine in "Mixing Bowl" (17906): "Celestial Solvent" (9731), "Words of Acquisition (Beza)" (11866). Produces "Celestial Essence" (9650). Requires Baking, trivial 15. The combine does not fail.
156. Combine in "Mixing Bowl" (17906): "Celestial Solvent" (9731), "Words of Burnishing" (11862). Produces "Celestial Essence" (9650). Requires Baking, trivial 15. The combine does not fail.
157. 67 other recipes also produce Celestial Essence (9650).
158. Common item: Jar of Acid (22133). Listed in 15 zones.
159. Combine in Brew Barrel (19): "Celestial Essence" (9650), "Jar of Acid" (22133). Produces "Acid Wash" (15987). Requires Brewing, trivial 151.
160. Combine in Forge (17): "Filthy Breastplate" (15984), "Acid Wash" (15987). Produces "Cleansed Breastplate" (15998). Requires Blacksmithing, trivial 227.
161. Common item: Mortar and Pestle (17904). Listed in 12 zones.
162. No quest step gives Sandstorm Pearl (29909). The dump lists it in bothunder.
163. Combine in "Mortar and Pestle" (17904): "Sandstorm Pearl" (29909). Produces "Powdered Sandstorm Pearl" (29520) x4. Requires Make Poison, trivial 255.
164. Common item: Firing Sheet (16906). Listed in 34 zones.
165. Combine in Pottery Wheel (21): "Large Block of Clay" (16902), "Water Flask" (13006), "Large Bowl Sketch" (16963). Produces "Unfired Mixing Bowl" (16930). Requires Pottery, trivial 128.
166. Combine in Kiln (22): "Firing Sheet" (16906), "Unfired Mixing Bowl" (16930). Produces "Mixing Bowl" (17906). Requires Pottery, trivial 15.
167. Combine in "Mixing Bowl" (17906): "Sandstorm Pearl" (29909). Produces "Powdered Sandstorm Pearl" (29520) x4. Requires Baking. The combine does not fail.
168. Spawns "a Koka'Vor chieftain" (210236) in `postorms` on event_signal.
169. Loot "Storm Rider Blood" (29526) from "a Koka'Vor chieftain".
170. Loot "Storm Rider Blood" (29526) from "A stormrider" in `bothunder`.
171. Loot "Storm Rider Blood" (29526) from "Dolsoj Warrebs" in `bazaar`.
172. Loot "Storm Rider Blood" (29526) from "a Koka'Vor krovian" in `postorms`.
173. Loot "Storm Rider Blood" (29526) from "a Koka'Vor senvar" in `postorms`.
174. No quest step gives Drop of Pure Rain (29904). The dump lists it in bothunder.
175. Combine in Brew Barrel (19): "Powdered Sandstorm Pearl" (29520), "Storm Rider Blood" (29526), "Drop of Pure Rain" (29904). Produces "Hurricane Temper" (29533). Requires Brewing, trivial 135.
176. Combine in Forge (17): "Cleansed Breastplate" (15998), "Hurricane Temper" (29533). Produces "Tempered Breastplate" (15999). Requires Blacksmithing, trivial 229.
177. Combine in Forge (17): "Black Diamond of Nightmares" (29990), "Tempered Breastplate" (15999). Produces "Imbued Breastplate" (15985). Requires Blacksmithing 220. Trivial at 275.
178. poknowledge/"Aid Grimel", hand "Imbued Breastplate" (15985). Gives "Hardened Leather Signet" (16249).
179. poknowledge/"Aid Grimel", say "Skill In Brewing". Gives "Portable Drink Barrel" (17179).
180. Loot "Cask" (16580) from "Tugog Grigol" in `rathemtn`.
181. Common item: Hops (16591). Listed in 31 zones.
182. Common item: Malt (16595). Listed in 30 zones.
183. Common item: Yeast (16596). Listed in 30 zones.
184. Combine in "Portable Drink Barrel" (17179): "Cask" (16580), "Hops" (16591), "Malt" (16595), "Yeast" (16596). Produces "Mead" (13008). Requires Brewing, trivial 41.
185. erudnext/"Reklon Gnallen", hand "Iron Ration" (13005) + "Mead" (13008). Requires `paladin_epic` ==9. Gives "Erudin Prayer Bead" (69965).
186. Summon "Quiver of Marr" (17307) by casting "Quiver of Marr".
187. rathemtn/"Shin Master Grubbus", hand "Quiver of Marr" (17307). Requires `paladin_epic` ==9. Gives "Gukta Prayer Bead" (69964).
188. Common item: Barley (16590). Listed in 28 zones.
189. Combine in Brew Barrel (19): "Bottle of Aged Bloodwine" (51163), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aged Bloodwine" (51164). Requires Brewing, trivial 255.
190. Combine in Brew Barrel (19): "Bottle of Aldo's Bitter Ale" (75805), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aldo's Bitter Ale" (75811). Requires Brewing, trivial 15.
191. 17 other recipes also produce Bottle (16598).
192. Combine in "Medicine Bag" (17901): "Hand-Formed Bottle" (45232), "Ensnaring Concoction V" (45236). Produces "Empty Vial" (10062), "Cork" (16851), "Formed Ensnaring Concoction V" (45258). Requires Alchemy, trivial 41.
193. Combine in Brew Barrel (19): "Bottle of Aged Bloodwine" (51163), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aged Bloodwine" (51164). Requires Brewing, trivial 255.
194. 11 other recipes also produce Cork (16851).
195. Combine in "Portable Drink Barrel" (17179): "Water Flask" (13006), "Celestial Essence" (9650). Produces "Purified Water" (12607). Requires Brewing, trivial 58.
196. Combine in "Tracker's Water Extractor" (17987): "Purification Tablet" (12630), "Water Reed" (12778). Produces "Purified Water" (12607) x3. Requires Pottery. The combine does not fail.
197. 3 other recipes also produce Purified Water (12607).
198. Forage "Sand Verbena" (65582) in `taka`.
199. Forage "Sand Verbena" (65582) in `takb`.
200. Forage "Sand Verbena" (65582) in `takc`.
201. Forage "Sand Verbena" (65582) in `takd`.
202. Forage "Sand Verbena" (65582) in `take`.
203. Forage "Sand Verbena" (65582) in `takf`.
204. Forage "Sand Verbena" (65582) in `takg`.
205. Forage "Sand Verbena" (65582) in `takh`.
206. Forage "Sand Verbena" (65582) in `taki`.
207. Forage "Sand Verbena" (65582) in `takj`.
208. Combine in Brew Barrel (19): "Barley" (16590), "Bottle" (16598), "Cork" (16851), "Hops" (16591), "Purified Water" (12607), "Sand Verbena" (65582), "Yeast" (16596). Produces "Bottle of Double Brewed Double Dry Stout" (51157). Requires Brewing, trivial 226.
209. kaladimb/"Datur Nightseer", hand "Bottle of Double Brewed Double Dry Stout" (51157). Requires `paladin_epic` ==9. Gives "Kaladim Prayer Bead" (69963).
210. felwithea/"General Jyleel", hand platinum:1000. Requires `paladin_epic` ==9. Gives "Felwithe Prayer Bead" (69962).
211. Ground spawn of "Freeport Prayer Bead" (69961) in `freeportwest`.
212. Ground spawn of "Freeport Prayer Bead" (69961) in `freportn`.
213. qeynos2/"Ziska Ironforge", hand platinum:500. Requires `paladin_epic` ==9. Gives "Qeynos Prayer Bead" (69960).
214. Combine in "Unfilled Set of Prayer Beads" (69968): "Rivervale Prayer Bead" (69967), "Ak'anon Prayer Bead" (69966), "Erudin Prayer Bead" (69965), "Gukta Prayer Bead" (69964), "Kaladim Prayer Bead" (69963), "Felwithe Prayer Bead" (69962), "Freeport Prayer Bead" (69961), "Qeynos Prayer Bead" (69960). Produces "Set of Prayer Beads" (69969). The combine does not fail.
215. dranikhollowsc/"Anetal", hand "Set of Prayer Beads" (69969). Sets `paladin_epic_hollowc` to `2`.
216. natimbi/"Kemik Arulon", hand "Set of Prayer Beads" (69969). Sets `paladin_epic_hollowc` to `1`.
217. natimbi/"Kemik Arulon", say "Hail". Requires `paladin_epic_hollowc` ==2. Requires `paladin_epic_hollowc` ==1. Gives "Token of Compassion" (69953).
218. Requires `pal_chest_keel` unset; no setter establishes this state.
219. oasis/"Paladin Epic", say "Hail". Requires `pal_chest_keel` unset. Gives "Keelee's Brooch" (69982).
220. oasis/"Paladin Epic", say "Keelee Say". Gives "Keelee's Brooch" (69982).
221. sro/"Instructor Maerceci", hand "Keelee's Brooch" (69982). Gives "Token of Chivalry" (69954).
222. Loot "Valdoon Kel'Novar's Heart" (69981) from "Valdoon Kel'Novar" in `mmcc`.
223. felwithea/"Galrun Starforge", hand "Valdoon Kel'Novar's Heart" (69981). Gives "Token of Cleansing" (69956).
224. provinggrounds/"Pashia Clouddancer", say "Note". Gives "Note from Pashia" (69973).
225. nedaria/"Duram Firechaser", hand "Note from Pashia" (69973). Gives "Token of Heroism" (69955).
226. Say "Check Lorb" to anguish/"Zone Status".
227. Spawns "Orb of Discordant Energy" (317087).
228. Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy".
229. Say "Check Uorb" to anguish/"Zone Status".
230. Say "Check Amv Chest" to anguish/"Zone Status".
231. Spawns "Ornate Chest" (317112).
232. Loot "Globe of Discordant Energy" (47100) from "Ornate Chest".
233. 2 other loot steps also yield Globe of Discordant Energy (47100).
234. Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy" in `anguish`.
235. Loot "Globe of Discordant Energy" (47100) from "Overlords Chest".
236. airplane/"Inte Akera", hand "Globe of Discordant Energy" (47100). Gives "Scabbard of the Righteous" (69959).

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
74. freeporteast/"A Prisoner", hand "Bunker Cell #1" (12196) + "Edible Goo" (13498) + "Bog Juice" (16581). Gives "H. K. 102" (12143).
75. freportw/"A Prisoner", hand "Bunker Cell #1" (12196) + "Edible Goo" (13498) + "Bog Juice" (16581). Gives "H. K. 102" (12143).
76. highkeep/"Assistant Kiolna", hand "H. K. 102" (12143). Gives "Sealed Note" (18936).
77. paw/"Brother Hayle", hand "Sealed Note" (18936). Gives "Note" (18937).
78. southkarana/"Brother Hayle", hand "Sealed Note" (18936). Gives "Note" (18937).
79. Kill freportw/"Sir Lucan D-Lere". Spawns "Sir Lucan D'Lere" (9147).
80. Loot "Testimony of Truth" (18827) from "Sir Lucan D'Lere".
81. Loot "Testimony of Truth" (18827) from "Sir Lucan D'Lere" in `freeporteast`.
82. freeportwest/"Valeron Dushire", hand "Testimony of Truth" (18827). Gives "Brilliant Sword of Faith" (13947).
83. freportn/"Valeron Dushire", hand "Testimony of Truth" (18827). Gives "Brilliant Sword of Faith" (13947).
84. Hand "Token of Bravery" (12144) + "Token of Generosity" (13865) to freeportwest/"Merko Quetalis". Spawns "spawns Guard Willia" (383270). Loot "Token of Truth" (13866) from "spawns Guard Willia".
85. Hand "Token of Bravery" (12144) + "Token of Generosity" (13865) to freportn/"Merko Quetalis". Spawns "spawns Guard Willia" (8110). Loot "Token of Truth" (13866) from "spawns Guard Willia".
86. Loot "Token of Truth" (13866) from "Guard Willia".
87. freeportwest/"Merko Quetalis", hand "Token of Truth" (13866). Gives "Testimony" (18828).
88. freportn/"Merko Quetalis", hand "Token of Truth" (13866). Gives "Testimony" (18828).
89. Loot "Glowing Sword Hilt" (12197) from "Xicotl" in `mistmoore`.
90. paw/"Brother Hayle", hand "Glowing Sword Hilt" (12197) + "Brilliant Sword of Faith" (13947) + "Testimony" (18828) + "Note" (18937). Gives "SoulFire" (5504).
91. southkarana/"Brother Hayle", hand "Glowing Sword Hilt" (12197) + "Brilliant Sword of Faith" (13947) + "Testimony" (18828) + "Note" (18937). Gives "SoulFire" (5504).
92. airplane/"Inte Akera", hand "SoulFire" (5504). Gives "Inte's First Blessing" (18033).
93. lavastorm/"Ruathey", say "Bag". Gives "Nobleman's Bag" (17878).
94. Common item: Ghoul's Heart (2410). Listed in 8 zones.
95. No quest step gives Amstaf's Scroll (2411). The dump lists it in highkeep.
96. No quest step gives Blade of Nobility (2412). The dump lists it in butcher.
97. Loot "Hilt of the Nobleman" (2413) from "Ekeros" in `najena`.
98. Loot "Hilt of the Nobleman" (2413) from "A Skeleton" in `najena`.
99. Combine in "Nobleman's Bag" (17878): "Ghoul's Heart" (2410), "Amstaf's Scroll" (2411), "Blade of Nobility" (2412), "Hilt of the Nobleman" (2413). Produces "Ghoulbane" (5403). The combine does not fail.
100. airplane/"Inte Akera", hand "Ghoulbane" (5403). Gives "Inte's Second Blessing" (18034).
101. Hand "Miragul's Phylactery" (19072) to everfrost/"Lich Of Miragul". Spawns "Spawn Miragul" (30094). Loot "Miragul's Head" (19073) from "Spawn Miragul".
102. Loot "Miragul's Head" (19073) from "Miragul".
103. Hand "Miragul's Phylactery" (19072) to everfrost/"Lich Of Miragul". Spawns "Spawn Miragul" (30094). Loot "Miragul's Robe" (1254) from "Spawn Miragul".
104. Loot "Miragul's Robe" (1254) from "Miragul".
105. airplane/"Inte Akera", hand "Miragul's Robe" (1254) + "Inte's First Blessing" (18033) + "Inte's Second Blessing" (18034) + "Miragul's Head" (19073). Gives "Fiery Avenger" (11050).
106. fearplane/"Irak Altil", hand "Fiery Avenger" (11050) + "Mark of Atonement" (29010). Gives "Fiery Defender" (10099).
107. povalor/"Baltron Werters", say "Couragebringer". Sets `pre_pal` to `1`.
108. Requires `pre_pal` unset; no setter establishes this state.
109. povalor/"Baltron Werters", say "Couragebringer". Requires `pre_pal` unset. Gives "Baltron's Solvent" (69901).
110. sro/"Gilfal", hand "Baltron's Solvent" (69901). Requires `pre_pal` ==1. Gives "Gilfal's Scabbard" (69902).
111. Spawns "Neffiken Lord Kelek-Vor" (210229) in `postorms` on event_signal.
112. Loot "Broken Sword Piece" (69903) from "Neffiken Lord Kelek-Vor".
113. Loot "Broken Sword Piece" (69903) from "Neffiken Lord of Kelek'Vor".
114. Say "Control Timer" to hateplaneb/"Maestro".
115. Spawns "Maestro of Rancor" (186111).
116. Loot "Broken Sword Piece" (69904) from "Maestro of Rancor".
117. **Broken:** no event trigger found for `hateplaneb/maestro#timer:popmaestro`.
118. Spawns "Maestro of Rancor" (186111) after `hateplaneb/maestro#timer:popmaestro`.
119. Loot "Broken Sword Piece" (69905) from "Kaniz Painbringer" in `potorment`.
120. sro/"Gilfal", hand "Baltron's Solvent" (69901). Sets `pre_pal` to `2`.
121. Ground spawn of "Rune of Xor" (69909) in `potranquility`.
122. Ground spawn of "Rune of Yirno" (69908) in `mistmoore`.
123. Ground spawn of "Rune of Zota" (69907) in `scarlet`.
124. Ground spawn of "Rune Wilun" (69910) in `gunthak`.
125. everfrost/"Rombus", hand "Rune of Zota" (69907) + "Rune of Yirno" (69908) + "Rune of Xor" (69909) + "Rune Wilun" (69910). Requires `pre_pal` ==2. Gives "Broken Sword Piece" (69906).
126. Combine in "Gilfal's Scabbard" (69902): "Broken Sword Piece" (69903), "Broken Sword Piece" (69904), "Broken Sword Piece" (69905), "Broken Sword Piece" (69906). Produces "Fractured Couragebringer" (69911). The combine does not fail.
127. sro/"Gilfal", hand "Fractured Couragebringer" (69911). Sets `pre_pal` to `4`.
128. everfrost/"Rombus", hand "Rune of Zota" (69907) + "Rune of Yirno" (69908) + "Rune of Xor" (69909) + "Rune Wilun" (69910). Sets `pre_pal` to `3`.
129. sro/"Gilfal", hand "Fractured Couragebringer" (69911). Requires `pre_pal` ==3. Gives "Fractured Couragebringer" (69912).
130. povalor/"Baltron Werters", hand "Fractured Couragebringer" (69912). Requires `pre_pal` ==4. Gives "Couragebringer" (69913).
131. hohonora/"Irak Altil", say "Hail". Sets `paladin_epic` to `6`.
132. Spawns "Durunal the Cursebearer" (300087) in `wallofslaughter` on enter.
133. Loot "Dark and Twisted Sword" (69971) from "Durunal the Cursebearer".
134. hohonora/"Irak Altil", hand "Dark and Twisted Sword" (69971). Requires `paladin_epic` ==6. Gives "Dark and Twisted Sword" (69972).
135. Loot "Redis' Soulstone" (69983) from "Shade of Redis Linrok" in `dranikcatacombsa`.
136. Combine in "Dark and Twisted Sword" (69972): "Rithnok's Soulstone" (69941), "Drema's Soulstone" (69952), "Reiya's Soulstone" (69942), "Redis' Soulstone" (69983). Produces "Redemption" (64031). The combine does not fail.
137. hohonora/"Irak Altil", say "Tell Me About Your Master". Sets `paladin_epic` to `9`.
138. erudnint/"Josper Kenshed", say "Collect Component". Gives "Empty Bag" (17944).
139. halas/"Lysbith Mcnaff", say "Protect The Pass". Gives "Empty Bag" (17944).
140. Loot "Goblin Ice Necklace" (13897) from "Redwind" in `everfrost`.
141. Loot "Goblin Ice Necklace" (13897) from "An Ice Goblin Scout" in `everfrost`.
142. Loot "Goblin Ice Necklace" (13897) from "An Ice Goblin Whelp" in `everfrost`.
143. Loot "Goblin Ice Necklace" (13897) from "An Icy Orc" in `everfrost`.
144. Loot "Goblin Ice Necklace" (13897) from "Ice Goblin Diver" in `everfrost`.
145. Combine in "Empty Bag" (17944): "Goblin Ice Necklace" (13897). Produces "Bag of Ice Necklaces" (13898). The combine does not fail.
146. halas/"Lysbith Mcnaff", hand "Bag of Ice Necklaces" (13898). Gives "Iron Ration" (13005).
147. Common item: Gnoll Fang (13915). Listed in 5 zones.
148. halas/"Lysbith Mcnaff", hand "Gnoll Fang" (13915) + "Gnoll Fang" (13915) + "Gnoll Fang" (13915). Gives "Iron Ration" (13005).
149. Requires `halloween_draykey_rations` unset; no setter establishes this state.
150. kithicor/"Old Man Draykey", say "Instructions". Requires `halloween_draykey_rations` unset. Gives "Iron Ration" (13005).
151. commons/"Kizdean Gix", say "Messages For Neriak". Gives "Sealed Letter" (18889).
152. neriakc/"Loveal S-Nez", hand "Sealed Letter" (18889). Gives "Iron Ration" (13005).
153. Summon "Black Diamond of Nightmares" (29990) by casting "Imbue Nightmare".
154. poknowledge/"Aid Grimel", say "Versed In The Art Of Smithing". Gives "Filthy Breastplate" (15984).
155. Combine in "Mixing Bowl" (17906): "Celestial Solvent" (9731), "Words of Acquisition (Beza)" (11866). Produces "Celestial Essence" (9650). Requires Baking, trivial 15. The combine does not fail.
156. Combine in "Mixing Bowl" (17906): "Celestial Solvent" (9731), "Words of Burnishing" (11862). Produces "Celestial Essence" (9650). Requires Baking, trivial 15. The combine does not fail.
157. 67 other recipes also produce Celestial Essence (9650).
158. Common item: Jar of Acid (22133). Listed in 15 zones.
159. Combine in Brew Barrel (19): "Celestial Essence" (9650), "Jar of Acid" (22133). Produces "Acid Wash" (15987). Requires Brewing, trivial 151.
160. Combine in Forge (17): "Filthy Breastplate" (15984), "Acid Wash" (15987). Produces "Cleansed Breastplate" (15998). Requires Blacksmithing, trivial 227.
161. Common item: Mortar and Pestle (17904). Listed in 12 zones.
162. No quest step gives Sandstorm Pearl (29909). The dump lists it in bothunder.
163. Combine in "Mortar and Pestle" (17904): "Sandstorm Pearl" (29909). Produces "Powdered Sandstorm Pearl" (29520) x4. Requires Make Poison, trivial 255.
164. Common item: Firing Sheet (16906). Listed in 34 zones.
165. Combine in Pottery Wheel (21): "Large Block of Clay" (16902), "Water Flask" (13006), "Large Bowl Sketch" (16963). Produces "Unfired Mixing Bowl" (16930). Requires Pottery, trivial 128.
166. Combine in Kiln (22): "Firing Sheet" (16906), "Unfired Mixing Bowl" (16930). Produces "Mixing Bowl" (17906). Requires Pottery, trivial 15.
167. Combine in "Mixing Bowl" (17906): "Sandstorm Pearl" (29909). Produces "Powdered Sandstorm Pearl" (29520) x4. Requires Baking. The combine does not fail.
168. Spawns "a Koka'Vor chieftain" (210236) in `postorms` on event_signal.
169. Loot "Storm Rider Blood" (29526) from "a Koka'Vor chieftain".
170. Loot "Storm Rider Blood" (29526) from "A stormrider" in `bothunder`.
171. Loot "Storm Rider Blood" (29526) from "Dolsoj Warrebs" in `bazaar`.
172. Loot "Storm Rider Blood" (29526) from "a Koka'Vor krovian" in `postorms`.
173. Loot "Storm Rider Blood" (29526) from "a Koka'Vor senvar" in `postorms`.
174. No quest step gives Drop of Pure Rain (29904). The dump lists it in bothunder.
175. Combine in Brew Barrel (19): "Powdered Sandstorm Pearl" (29520), "Storm Rider Blood" (29526), "Drop of Pure Rain" (29904). Produces "Hurricane Temper" (29533). Requires Brewing, trivial 135.
176. Combine in Forge (17): "Cleansed Breastplate" (15998), "Hurricane Temper" (29533). Produces "Tempered Breastplate" (15999). Requires Blacksmithing, trivial 229.
177. Combine in Forge (17): "Black Diamond of Nightmares" (29990), "Tempered Breastplate" (15999). Produces "Imbued Breastplate" (15985). Requires Blacksmithing 220. Trivial at 275.
178. poknowledge/"Aid Grimel", hand "Imbued Breastplate" (15985). Gives "Hardened Leather Signet" (16249).
179. poknowledge/"Aid Grimel", say "Skill In Brewing". Gives "Portable Drink Barrel" (17179).
180. Loot "Cask" (16580) from "Tugog Grigol" in `rathemtn`.
181. Common item: Hops (16591). Listed in 31 zones.
182. Common item: Malt (16595). Listed in 30 zones.
183. Common item: Yeast (16596). Listed in 30 zones.
184. Combine in "Portable Drink Barrel" (17179): "Cask" (16580), "Hops" (16591), "Malt" (16595), "Yeast" (16596). Produces "Mead" (13008). Requires Brewing, trivial 41.
185. erudnext/"Reklon Gnallen", hand "Iron Ration" (13005) + "Mead" (13008). Requires `paladin_epic` ==9. Gives "Erudin Prayer Bead" (69965).
186. Summon "Quiver of Marr" (17307) by casting "Quiver of Marr".
187. rathemtn/"Shin Master Grubbus", hand "Quiver of Marr" (17307). Requires `paladin_epic` ==9. Gives "Gukta Prayer Bead" (69964).
188. Common item: Barley (16590). Listed in 28 zones.
189. Combine in Brew Barrel (19): "Bottle of Aged Bloodwine" (51163), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aged Bloodwine" (51164). Requires Brewing, trivial 255.
190. Combine in Brew Barrel (19): "Bottle of Aldo's Bitter Ale" (75805), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aldo's Bitter Ale" (75811). Requires Brewing, trivial 15.
191. 17 other recipes also produce Bottle (16598).
192. Combine in "Medicine Bag" (17901): "Hand-Formed Bottle" (45232), "Ensnaring Concoction V" (45236). Produces "Empty Vial" (10062), "Cork" (16851), "Formed Ensnaring Concoction V" (45258). Requires Alchemy, trivial 41.
193. Combine in Brew Barrel (19): "Bottle of Aged Bloodwine" (51163), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aged Bloodwine" (51164). Requires Brewing, trivial 255.
194. 11 other recipes also produce Cork (16851).
195. Combine in "Portable Drink Barrel" (17179): "Water Flask" (13006), "Celestial Essence" (9650). Produces "Purified Water" (12607). Requires Brewing, trivial 58.
196. Combine in "Tracker's Water Extractor" (17987): "Purification Tablet" (12630), "Water Reed" (12778). Produces "Purified Water" (12607) x3. Requires Pottery. The combine does not fail.
197. 3 other recipes also produce Purified Water (12607).
198. Forage "Sand Verbena" (65582) in `taka`.
199. Forage "Sand Verbena" (65582) in `takb`.
200. Forage "Sand Verbena" (65582) in `takc`.
201. Forage "Sand Verbena" (65582) in `takd`.
202. Forage "Sand Verbena" (65582) in `take`.
203. Forage "Sand Verbena" (65582) in `takf`.
204. Forage "Sand Verbena" (65582) in `takg`.
205. Forage "Sand Verbena" (65582) in `takh`.
206. Forage "Sand Verbena" (65582) in `taki`.
207. Forage "Sand Verbena" (65582) in `takj`.
208. Combine in Brew Barrel (19): "Barley" (16590), "Bottle" (16598), "Cork" (16851), "Hops" (16591), "Purified Water" (12607), "Sand Verbena" (65582), "Yeast" (16596). Produces "Bottle of Double Brewed Double Dry Stout" (51157). Requires Brewing, trivial 226.
209. kaladimb/"Datur Nightseer", hand "Bottle of Double Brewed Double Dry Stout" (51157). Requires `paladin_epic` ==9. Gives "Kaladim Prayer Bead" (69963).
210. felwithea/"General Jyleel", hand platinum:1000. Requires `paladin_epic` ==9. Gives "Felwithe Prayer Bead" (69962).
211. Ground spawn of "Freeport Prayer Bead" (69961) in `freeportwest`.
212. Ground spawn of "Freeport Prayer Bead" (69961) in `freportn`.
213. qeynos2/"Ziska Ironforge", hand platinum:500. Requires `paladin_epic` ==9. Gives "Qeynos Prayer Bead" (69960).
214. Combine in "Unfilled Set of Prayer Beads" (69968): "Rivervale Prayer Bead" (69967), "Ak'anon Prayer Bead" (69966), "Erudin Prayer Bead" (69965), "Gukta Prayer Bead" (69964), "Kaladim Prayer Bead" (69963), "Felwithe Prayer Bead" (69962), "Freeport Prayer Bead" (69961), "Qeynos Prayer Bead" (69960). Produces "Set of Prayer Beads" (69969). The combine does not fail.
215. dranikhollowsc/"Anetal", hand "Set of Prayer Beads" (69969). Sets `paladin_epic_hollowc` to `2`.
216. natimbi/"Kemik Arulon", hand "Set of Prayer Beads" (69969). Sets `paladin_epic_hollowc` to `1`.
217. natimbi/"Kemik Arulon", say "Hail". Requires `paladin_epic_hollowc` ==2. Requires `paladin_epic_hollowc` ==1. Gives "Token of Compassion" (69953).
218. Requires `pal_chest_keel` unset; no setter establishes this state.
219. oasis/"Paladin Epic", say "Hail". Requires `pal_chest_keel` unset. Gives "Keelee's Brooch" (69982).
220. oasis/"Paladin Epic", say "Keelee Say". Gives "Keelee's Brooch" (69982).
221. sro/"Instructor Maerceci", hand "Keelee's Brooch" (69982). Gives "Token of Chivalry" (69954).
222. Loot "Valdoon Kel'Novar's Heart" (69981) from "Valdoon Kel'Novar" in `mmcc`.
223. felwithea/"Galrun Starforge", hand "Valdoon Kel'Novar's Heart" (69981). Gives "Token of Cleansing" (69956).
224. provinggrounds/"Pashia Clouddancer", say "Note". Gives "Note from Pashia" (69973).
225. nedaria/"Duram Firechaser", hand "Note from Pashia" (69973). Gives "Token of Heroism" (69955).
226. Say "Check Lorb" to anguish/"Zone Status".
227. Spawns "Orb of Discordant Energy" (317087).
228. Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy".
229. Say "Check Uorb" to anguish/"Zone Status".
230. Say "Check Amv Chest" to anguish/"Zone Status".
231. Spawns "Ornate Chest" (317112).
232. Loot "Globe of Discordant Energy" (47100) from "Ornate Chest".
233. 2 other loot steps also yield Globe of Discordant Energy (47100).
234. Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy" in `anguish`.
235. Loot "Globe of Discordant Energy" (47100) from "Overlords Chest".
236. airplane/"Inte Akera", hand "Globe of Discordant Energy" (47100). Gives "Token of Loyalty" (69958).

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
74. freeporteast/"A Prisoner", hand "Bunker Cell #1" (12196) + "Edible Goo" (13498) + "Bog Juice" (16581). Gives "H. K. 102" (12143).
75. freportw/"A Prisoner", hand "Bunker Cell #1" (12196) + "Edible Goo" (13498) + "Bog Juice" (16581). Gives "H. K. 102" (12143).
76. highkeep/"Assistant Kiolna", hand "H. K. 102" (12143). Gives "Sealed Note" (18936).
77. paw/"Brother Hayle", hand "Sealed Note" (18936). Gives "Note" (18937).
78. southkarana/"Brother Hayle", hand "Sealed Note" (18936). Gives "Note" (18937).
79. Kill freportw/"Sir Lucan D-Lere". Spawns "Sir Lucan D'Lere" (9147).
80. Loot "Testimony of Truth" (18827) from "Sir Lucan D'Lere".
81. Loot "Testimony of Truth" (18827) from "Sir Lucan D'Lere" in `freeporteast`.
82. freeportwest/"Valeron Dushire", hand "Testimony of Truth" (18827). Gives "Brilliant Sword of Faith" (13947).
83. freportn/"Valeron Dushire", hand "Testimony of Truth" (18827). Gives "Brilliant Sword of Faith" (13947).
84. Hand "Token of Bravery" (12144) + "Token of Generosity" (13865) to freeportwest/"Merko Quetalis". Spawns "spawns Guard Willia" (383270). Loot "Token of Truth" (13866) from "spawns Guard Willia".
85. Hand "Token of Bravery" (12144) + "Token of Generosity" (13865) to freportn/"Merko Quetalis". Spawns "spawns Guard Willia" (8110). Loot "Token of Truth" (13866) from "spawns Guard Willia".
86. Loot "Token of Truth" (13866) from "Guard Willia".
87. freeportwest/"Merko Quetalis", hand "Token of Truth" (13866). Gives "Testimony" (18828).
88. freportn/"Merko Quetalis", hand "Token of Truth" (13866). Gives "Testimony" (18828).
89. Loot "Glowing Sword Hilt" (12197) from "Xicotl" in `mistmoore`.
90. paw/"Brother Hayle", hand "Glowing Sword Hilt" (12197) + "Brilliant Sword of Faith" (13947) + "Testimony" (18828) + "Note" (18937). Gives "SoulFire" (5504).
91. southkarana/"Brother Hayle", hand "Glowing Sword Hilt" (12197) + "Brilliant Sword of Faith" (13947) + "Testimony" (18828) + "Note" (18937). Gives "SoulFire" (5504).
92. airplane/"Inte Akera", hand "SoulFire" (5504). Gives "Inte's First Blessing" (18033).
93. lavastorm/"Ruathey", say "Bag". Gives "Nobleman's Bag" (17878).
94. Common item: Ghoul's Heart (2410). Listed in 8 zones.
95. No quest step gives Amstaf's Scroll (2411). The dump lists it in highkeep.
96. No quest step gives Blade of Nobility (2412). The dump lists it in butcher.
97. Loot "Hilt of the Nobleman" (2413) from "Ekeros" in `najena`.
98. Loot "Hilt of the Nobleman" (2413) from "A Skeleton" in `najena`.
99. Combine in "Nobleman's Bag" (17878): "Ghoul's Heart" (2410), "Amstaf's Scroll" (2411), "Blade of Nobility" (2412), "Hilt of the Nobleman" (2413). Produces "Ghoulbane" (5403). The combine does not fail.
100. airplane/"Inte Akera", hand "Ghoulbane" (5403). Gives "Inte's Second Blessing" (18034).
101. Hand "Miragul's Phylactery" (19072) to everfrost/"Lich Of Miragul". Spawns "Spawn Miragul" (30094). Loot "Miragul's Head" (19073) from "Spawn Miragul".
102. Loot "Miragul's Head" (19073) from "Miragul".
103. Hand "Miragul's Phylactery" (19072) to everfrost/"Lich Of Miragul". Spawns "Spawn Miragul" (30094). Loot "Miragul's Robe" (1254) from "Spawn Miragul".
104. Loot "Miragul's Robe" (1254) from "Miragul".
105. airplane/"Inte Akera", hand "Miragul's Robe" (1254) + "Inte's First Blessing" (18033) + "Inte's Second Blessing" (18034) + "Miragul's Head" (19073). Gives "Fiery Avenger" (11050).
106. fearplane/"Irak Altil", hand "Fiery Avenger" (11050) + "Mark of Atonement" (29010). Gives "Fiery Defender" (10099).
107. povalor/"Baltron Werters", say "Couragebringer". Sets `pre_pal` to `1`.
108. Requires `pre_pal` unset; no setter establishes this state.
109. povalor/"Baltron Werters", say "Couragebringer". Requires `pre_pal` unset. Gives "Baltron's Solvent" (69901).
110. sro/"Gilfal", hand "Baltron's Solvent" (69901). Requires `pre_pal` ==1. Gives "Gilfal's Scabbard" (69902).
111. Spawns "Neffiken Lord Kelek-Vor" (210229) in `postorms` on event_signal.
112. Loot "Broken Sword Piece" (69903) from "Neffiken Lord Kelek-Vor".
113. Loot "Broken Sword Piece" (69903) from "Neffiken Lord of Kelek'Vor".
114. Say "Control Timer" to hateplaneb/"Maestro".
115. Spawns "Maestro of Rancor" (186111).
116. Loot "Broken Sword Piece" (69904) from "Maestro of Rancor".
117. **Broken:** no event trigger found for `hateplaneb/maestro#timer:popmaestro`.
118. Spawns "Maestro of Rancor" (186111) after `hateplaneb/maestro#timer:popmaestro`.
119. Loot "Broken Sword Piece" (69905) from "Kaniz Painbringer" in `potorment`.
120. sro/"Gilfal", hand "Baltron's Solvent" (69901). Sets `pre_pal` to `2`.
121. Ground spawn of "Rune of Xor" (69909) in `potranquility`.
122. Ground spawn of "Rune of Yirno" (69908) in `mistmoore`.
123. Ground spawn of "Rune of Zota" (69907) in `scarlet`.
124. Ground spawn of "Rune Wilun" (69910) in `gunthak`.
125. everfrost/"Rombus", hand "Rune of Zota" (69907) + "Rune of Yirno" (69908) + "Rune of Xor" (69909) + "Rune Wilun" (69910). Requires `pre_pal` ==2. Gives "Broken Sword Piece" (69906).
126. Combine in "Gilfal's Scabbard" (69902): "Broken Sword Piece" (69903), "Broken Sword Piece" (69904), "Broken Sword Piece" (69905), "Broken Sword Piece" (69906). Produces "Fractured Couragebringer" (69911). The combine does not fail.
127. sro/"Gilfal", hand "Fractured Couragebringer" (69911). Sets `pre_pal` to `4`.
128. everfrost/"Rombus", hand "Rune of Zota" (69907) + "Rune of Yirno" (69908) + "Rune of Xor" (69909) + "Rune Wilun" (69910). Sets `pre_pal` to `3`.
129. sro/"Gilfal", hand "Fractured Couragebringer" (69911). Requires `pre_pal` ==3. Gives "Fractured Couragebringer" (69912).
130. povalor/"Baltron Werters", hand "Fractured Couragebringer" (69912). Requires `pre_pal` ==4. Gives "Couragebringer" (69913).
131. hohonora/"Irak Altil", say "Hail". Sets `paladin_epic` to `6`.
132. Spawns "Durunal the Cursebearer" (300087) in `wallofslaughter` on enter.
133. Loot "Dark and Twisted Sword" (69971) from "Durunal the Cursebearer".
134. hohonora/"Irak Altil", hand "Dark and Twisted Sword" (69971). Requires `paladin_epic` ==6. Gives "Dark and Twisted Sword" (69972).
135. Loot "Redis' Soulstone" (69983) from "Shade of Redis Linrok" in `dranikcatacombsa`.
136. Combine in "Dark and Twisted Sword" (69972): "Rithnok's Soulstone" (69941), "Drema's Soulstone" (69952), "Reiya's Soulstone" (69942), "Redis' Soulstone" (69983). Produces "Redemption" (64031). The combine does not fail.
137. hohonora/"Irak Altil", say "Tell Me About Your Master". Sets `paladin_epic` to `9`.
138. erudnint/"Josper Kenshed", say "Collect Component". Gives "Empty Bag" (17944).
139. halas/"Lysbith Mcnaff", say "Protect The Pass". Gives "Empty Bag" (17944).
140. Loot "Goblin Ice Necklace" (13897) from "Redwind" in `everfrost`.
141. Loot "Goblin Ice Necklace" (13897) from "An Ice Goblin Scout" in `everfrost`.
142. Loot "Goblin Ice Necklace" (13897) from "An Ice Goblin Whelp" in `everfrost`.
143. Loot "Goblin Ice Necklace" (13897) from "An Icy Orc" in `everfrost`.
144. Loot "Goblin Ice Necklace" (13897) from "Ice Goblin Diver" in `everfrost`.
145. Combine in "Empty Bag" (17944): "Goblin Ice Necklace" (13897). Produces "Bag of Ice Necklaces" (13898). The combine does not fail.
146. halas/"Lysbith Mcnaff", hand "Bag of Ice Necklaces" (13898). Gives "Iron Ration" (13005).
147. Common item: Gnoll Fang (13915). Listed in 5 zones.
148. halas/"Lysbith Mcnaff", hand "Gnoll Fang" (13915) + "Gnoll Fang" (13915) + "Gnoll Fang" (13915). Gives "Iron Ration" (13005).
149. Requires `halloween_draykey_rations` unset; no setter establishes this state.
150. kithicor/"Old Man Draykey", say "Instructions". Requires `halloween_draykey_rations` unset. Gives "Iron Ration" (13005).
151. commons/"Kizdean Gix", say "Messages For Neriak". Gives "Sealed Letter" (18889).
152. neriakc/"Loveal S-Nez", hand "Sealed Letter" (18889). Gives "Iron Ration" (13005).
153. Summon "Black Diamond of Nightmares" (29990) by casting "Imbue Nightmare".
154. poknowledge/"Aid Grimel", say "Versed In The Art Of Smithing". Gives "Filthy Breastplate" (15984).
155. Combine in "Mixing Bowl" (17906): "Celestial Solvent" (9731), "Words of Acquisition (Beza)" (11866). Produces "Celestial Essence" (9650). Requires Baking, trivial 15. The combine does not fail.
156. Combine in "Mixing Bowl" (17906): "Celestial Solvent" (9731), "Words of Burnishing" (11862). Produces "Celestial Essence" (9650). Requires Baking, trivial 15. The combine does not fail.
157. 67 other recipes also produce Celestial Essence (9650).
158. Common item: Jar of Acid (22133). Listed in 15 zones.
159. Combine in Brew Barrel (19): "Celestial Essence" (9650), "Jar of Acid" (22133). Produces "Acid Wash" (15987). Requires Brewing, trivial 151.
160. Combine in Forge (17): "Filthy Breastplate" (15984), "Acid Wash" (15987). Produces "Cleansed Breastplate" (15998). Requires Blacksmithing, trivial 227.
161. Common item: Mortar and Pestle (17904). Listed in 12 zones.
162. No quest step gives Sandstorm Pearl (29909). The dump lists it in bothunder.
163. Combine in "Mortar and Pestle" (17904): "Sandstorm Pearl" (29909). Produces "Powdered Sandstorm Pearl" (29520) x4. Requires Make Poison, trivial 255.
164. Common item: Firing Sheet (16906). Listed in 34 zones.
165. Combine in Pottery Wheel (21): "Large Block of Clay" (16902), "Water Flask" (13006), "Large Bowl Sketch" (16963). Produces "Unfired Mixing Bowl" (16930). Requires Pottery, trivial 128.
166. Combine in Kiln (22): "Firing Sheet" (16906), "Unfired Mixing Bowl" (16930). Produces "Mixing Bowl" (17906). Requires Pottery, trivial 15.
167. Combine in "Mixing Bowl" (17906): "Sandstorm Pearl" (29909). Produces "Powdered Sandstorm Pearl" (29520) x4. Requires Baking. The combine does not fail.
168. Spawns "a Koka'Vor chieftain" (210236) in `postorms` on event_signal.
169. Loot "Storm Rider Blood" (29526) from "a Koka'Vor chieftain".
170. Loot "Storm Rider Blood" (29526) from "A stormrider" in `bothunder`.
171. Loot "Storm Rider Blood" (29526) from "Dolsoj Warrebs" in `bazaar`.
172. Loot "Storm Rider Blood" (29526) from "a Koka'Vor krovian" in `postorms`.
173. Loot "Storm Rider Blood" (29526) from "a Koka'Vor senvar" in `postorms`.
174. No quest step gives Drop of Pure Rain (29904). The dump lists it in bothunder.
175. Combine in Brew Barrel (19): "Powdered Sandstorm Pearl" (29520), "Storm Rider Blood" (29526), "Drop of Pure Rain" (29904). Produces "Hurricane Temper" (29533). Requires Brewing, trivial 135.
176. Combine in Forge (17): "Cleansed Breastplate" (15998), "Hurricane Temper" (29533). Produces "Tempered Breastplate" (15999). Requires Blacksmithing, trivial 229.
177. Combine in Forge (17): "Black Diamond of Nightmares" (29990), "Tempered Breastplate" (15999). Produces "Imbued Breastplate" (15985). Requires Blacksmithing 220. Trivial at 275.
178. poknowledge/"Aid Grimel", hand "Imbued Breastplate" (15985). Gives "Hardened Leather Signet" (16249).
179. poknowledge/"Aid Grimel", say "Skill In Brewing". Gives "Portable Drink Barrel" (17179).
180. Loot "Cask" (16580) from "Tugog Grigol" in `rathemtn`.
181. Common item: Hops (16591). Listed in 31 zones.
182. Common item: Malt (16595). Listed in 30 zones.
183. Common item: Yeast (16596). Listed in 30 zones.
184. Combine in "Portable Drink Barrel" (17179): "Cask" (16580), "Hops" (16591), "Malt" (16595), "Yeast" (16596). Produces "Mead" (13008). Requires Brewing, trivial 41.
185. erudnext/"Reklon Gnallen", hand "Iron Ration" (13005) + "Mead" (13008). Requires `paladin_epic` ==9. Gives "Erudin Prayer Bead" (69965).
186. Summon "Quiver of Marr" (17307) by casting "Quiver of Marr".
187. rathemtn/"Shin Master Grubbus", hand "Quiver of Marr" (17307). Requires `paladin_epic` ==9. Gives "Gukta Prayer Bead" (69964).
188. Common item: Barley (16590). Listed in 28 zones.
189. Combine in Brew Barrel (19): "Bottle of Aged Bloodwine" (51163), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aged Bloodwine" (51164). Requires Brewing, trivial 255.
190. Combine in Brew Barrel (19): "Bottle of Aldo's Bitter Ale" (75805), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aldo's Bitter Ale" (75811). Requires Brewing, trivial 15.
191. 17 other recipes also produce Bottle (16598).
192. Combine in "Medicine Bag" (17901): "Hand-Formed Bottle" (45232), "Ensnaring Concoction V" (45236). Produces "Empty Vial" (10062), "Cork" (16851), "Formed Ensnaring Concoction V" (45258). Requires Alchemy, trivial 41.
193. Combine in Brew Barrel (19): "Bottle of Aged Bloodwine" (51163), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aged Bloodwine" (51164). Requires Brewing, trivial 255.
194. 11 other recipes also produce Cork (16851).
195. Combine in "Portable Drink Barrel" (17179): "Water Flask" (13006), "Celestial Essence" (9650). Produces "Purified Water" (12607). Requires Brewing, trivial 58.
196. Combine in "Tracker's Water Extractor" (17987): "Purification Tablet" (12630), "Water Reed" (12778). Produces "Purified Water" (12607) x3. Requires Pottery. The combine does not fail.
197. 3 other recipes also produce Purified Water (12607).
198. Forage "Sand Verbena" (65582) in `taka`.
199. Forage "Sand Verbena" (65582) in `takb`.
200. Forage "Sand Verbena" (65582) in `takc`.
201. Forage "Sand Verbena" (65582) in `takd`.
202. Forage "Sand Verbena" (65582) in `take`.
203. Forage "Sand Verbena" (65582) in `takf`.
204. Forage "Sand Verbena" (65582) in `takg`.
205. Forage "Sand Verbena" (65582) in `takh`.
206. Forage "Sand Verbena" (65582) in `taki`.
207. Forage "Sand Verbena" (65582) in `takj`.
208. Combine in Brew Barrel (19): "Barley" (16590), "Bottle" (16598), "Cork" (16851), "Hops" (16591), "Purified Water" (12607), "Sand Verbena" (65582), "Yeast" (16596). Produces "Bottle of Double Brewed Double Dry Stout" (51157). Requires Brewing, trivial 226.
209. kaladimb/"Datur Nightseer", hand "Bottle of Double Brewed Double Dry Stout" (51157). Requires `paladin_epic` ==9. Gives "Kaladim Prayer Bead" (69963).
210. felwithea/"General Jyleel", hand platinum:1000. Requires `paladin_epic` ==9. Gives "Felwithe Prayer Bead" (69962).
211. Ground spawn of "Freeport Prayer Bead" (69961) in `freeportwest`.
212. Ground spawn of "Freeport Prayer Bead" (69961) in `freportn`.
213. qeynos2/"Ziska Ironforge", hand platinum:500. Requires `paladin_epic` ==9. Gives "Qeynos Prayer Bead" (69960).
214. Combine in "Unfilled Set of Prayer Beads" (69968): "Rivervale Prayer Bead" (69967), "Ak'anon Prayer Bead" (69966), "Erudin Prayer Bead" (69965), "Gukta Prayer Bead" (69964), "Kaladim Prayer Bead" (69963), "Felwithe Prayer Bead" (69962), "Freeport Prayer Bead" (69961), "Qeynos Prayer Bead" (69960). Produces "Set of Prayer Beads" (69969). The combine does not fail.
215. dranikhollowsc/"Anetal", hand "Set of Prayer Beads" (69969). Sets `paladin_epic_hollowc` to `2`.
216. natimbi/"Kemik Arulon", hand "Set of Prayer Beads" (69969). Sets `paladin_epic_hollowc` to `1`.
217. natimbi/"Kemik Arulon", say "Hail". Requires `paladin_epic_hollowc` ==2. Requires `paladin_epic_hollowc` ==1. Gives "Token of Compassion" (69953).
218. Requires `pal_chest_keel` unset; no setter establishes this state.
219. oasis/"Paladin Epic", say "Hail". Requires `pal_chest_keel` unset. Gives "Keelee's Brooch" (69982).
220. oasis/"Paladin Epic", say "Keelee Say". Gives "Keelee's Brooch" (69982).
221. sro/"Instructor Maerceci", hand "Keelee's Brooch" (69982). Gives "Token of Chivalry" (69954).
222. Loot "Valdoon Kel'Novar's Heart" (69981) from "Valdoon Kel'Novar" in `mmcc`.
223. felwithea/"Galrun Starforge", hand "Valdoon Kel'Novar's Heart" (69981). Gives "Token of Cleansing" (69956).
224. provinggrounds/"Pashia Clouddancer", say "Note". Gives "Note from Pashia" (69973).
225. nedaria/"Duram Firechaser", hand "Note from Pashia" (69973). Gives "Token of Heroism" (69955).
226. Say "Check Lorb" to anguish/"Zone Status".
227. Spawns "Orb of Discordant Energy" (317087).
228. Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy".
229. Say "Check Uorb" to anguish/"Zone Status".
230. Say "Check Amv Chest" to anguish/"Zone Status".
231. Spawns "Ornate Chest" (317112).
232. Loot "Globe of Discordant Energy" (47100) from "Ornate Chest".
233. 2 other loot steps also yield Globe of Discordant Energy (47100).
234. Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy" in `anguish`.
235. Loot "Globe of Discordant Energy" (47100) from "Overlords Chest".
236. airplane/"Inte Akera", hand "Globe of Discordant Energy" (47100). Gives "Token of Conviction" (69957).

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
