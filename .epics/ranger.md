# Ranger

Steps taken from the quest graph only. **Broken** means the graph has no edge for that value or that item.

Flags with writes: `ranger_epic`, `ranger_epic15_pre`.

## 0. Prerequisites

Each list is the order you obtain that item. Later steps point here instead of repeating the chain.

### "Earthcaller" (20488)

1. burningwood/"Telin Darkforest", say "Action". Gives "Worn Note" (20472).
2. gfaydark/"Faelin Bloodbriar", hand "Worn Note" (20472). Gives "Faelin's Ring" (20446).
3. kithicor/"Giz X-Tin", hand "Faelin's Ring" (20446). Gives "Dark Metal Coin" (20447).
4. burningwood/"Telin Darkforest", hand "Dark Metal Coin" (20447). Gives "Worn Dark Metal Coin" (20448).
5. eastkarana/"Althele", hand "Worn Dark Metal Coin" (20448). Gives "Braided Grass Amulet" (20450).
6. eastkarana/"Sionae", hand "Braided Grass Amulet" (20450). Gives "Frayed Braided Grass Amulet" (20451).
7. eastkarana/"Teloa", hand "Frayed Braided Grass Amulet" (20451). Triggers `eastkarana/althele#signal:1`.
8. Starts timer `attack`.
9. Spawns "Corruptor" (15153) after `eastkarana/althele#timer:attack`.
10. Loot "Fleshbound Tome" (20452) from "Corruptor".
11. eastkarana/"Althele", hand "Fleshbound Tome" (20452). Gives "Earth Stained Note" (18959).
12. misty/"Ella Foodcrafter", hand "Earth Stained Note" (18959). Sets `shiny_tin_bowl` to `1`.
13. misty/"Ella Foodcrafter", say "Two Tasks". Requires `shiny_tin_bowl` set. Gives "Shiny Tin Bowl" (17860).
14. Hand "Shiny Tin Bowl" (17860) to hole/"Jaeil The Wretched". Spawns "Jaeil the Insane" (39154). Loot "Soulbound Hammer" (20478) from "Jaeil the Insane".
15. erudnint/"Mairee Silentone", hand "Soulbound Hammer" (20478). Gives "Dwarven Smiths Hammer" (20479).
16. Kill airplane/"An Essence Carrier". Spawns "An Essence Tamer" (71071).
17. Loot "Swirling Sphere of Color" (20494) from "An Essence Tamer".
18. erudnint/"Mairee Silentone", hand "Dwarven Smiths Hammer" (20479) + "Swirling Sphere of Color" (20494). Gives "Hammer of the Ancients" (20485).
19. kaladimb/"Kinlo Strongarm", hand "Hammer of the Ancients" (20485). Gives "Small bit of Mithril Ore" (20482).
20. kaladimb/"Kinlo Strongarm", hand "Small bit of Mithril Ore" (20482). Gives "Refined Mithril Blade" (20483).
21. Encounter starts when NPC 186201 spawns in `hateplaneb`.
22. Starts timer `popinny`.
23. Kill NPC 186158.
24. Starts timer `text`.
25. Starts timer `text2`.
26. Starts timer `spawninny`.
27. Spawns "Innoruuk" (186107) after `hateplaneb/inny#timer:spawninny`.
28. Loot "Shattered Emerald of Corruption" (20484) from "Innoruuk".
29. 1 alternative loot source(s) also yield Shattered Emerald of Corruption (20484).
30. northkarana/"Xanuusus", hand "Refined Mithril Blade" (20483) + "Shattered Emerald of Corruption" (20484). Gives "Earthcaller" (20488).

### "Essence of Earth and Wind" (62600)

1. nedaria/"Targen Stonefall", say "Native Stones". Sets `ranger_epic15_pre` to `1`.
2. Forage "Blasted Stone" (62601) in `bloodfields`.
3. nedaria/"Targen Stonefall", hand "Blasted Stone" (62601). Sets `ranger_epic15_pre` to `2`.
4. nedaria/"Targen Stonefall", say "Odus". Sets `ranger_epic15_pre` to `3`.
5. Spawns "Stone Collector" (39168) in `hole` on enter.
6. Loot "Dusty Stone" (62653) from "Stone Collector".
7. hole/"Player", on loot. Sets `ranger_epic15_pre` to `4`.
8. nedaria/"Targen Stonefall", say "Bloodfields". Requires `ranger_epic15_pre` ==2. Gives "Sample Cloth" (62640).
9. nedaria/"Targen Stonefall", say "Bloodfields". Requires `ranger_epic15_pre` ==2. Gives "Targen's Emulsion" (62639).
10. Combine in "Sample Cloth" (62640): "Targen's Emulsion" (62639), "Dusty Stone" (62653). Produces "Rock of Odus" (62606). The combine does not fail.
11. nedaria/"Targen Stonefall", hand "Blasted Stone" (62601). Requires `ranger_epic15_pre` ==1. Gives "Washed Blasted Stone" (62602).
12. Combine in "Sample Cloth" (62640): "Rock of Odus" (62606), "Washed Blasted Stone" (62602). Produces "Closed Sample Cloth" (62641). The combine does not fail.
13. nedaria/"Targen Stonefall", hand "Closed Sample Cloth" (62641). Sets `ranger_epic15_pre` to `5`.
14. nedaria/"Targen Stonefall", say "Impurities". Sets `ranger_epic15_pre` to `6`.
15. nedaria/"Targen Stonefall", say "Impurities". Requires `ranger_epic15_pre` ==5. Gives "Polished Blasted Stone" (62603).
16. northkarana/"Xanuusus", hand "Polished Blasted Stone" (62603). Sets `ranger_epic15_pre` to `7`.
17. Loot "Taskmaster's Cutlass" (62631) from "Taskmaster Waggad Brokenskull" in `torgiran`.
18. torgiran/"Player", on loot. Sets `ranger_epic15_pre` to `8`.
19. northkarana/"Xanuusus", hand "Polished Blasted Stone" (62603). Requires `ranger_epic15_pre` ==6. Gives "Poem of the Storms" (62632).
20. misty/"A Tired Farmer", hand "Poem of the Storms" (62632). Gives "Tear-stained Poem of the Storms" (62633).
21. Say "Ready" to northkarana/"Xanuusus".
22. Spawns "A Tainted Beast" (13131).
23. Loot "Stone of Winde" (62604) from "A Tainted Beast".
24. northkarana/"Xanuusus", hand "Stone of Winde" (62604). Sets `ranger_epic15_pre` to `9`.
25. Unresolved cyclic prerequisite: `ranger_epic15_pre` ==10.
26. steamfont/"Godbin Strumharp", hand platinum:30. Requires `ranger_epic15_pre` ==9. Gives "Sound Capture Jar" (62637).
27. charasis/"Ghost Of Mera", hand "Sound Capture Jar" (62637). Sets `ranger_epic15_pre` to `10`.
28. Spawns "Ghost of Mera" (105290) in `charasis` on event_enterzone.
29. Hand "Sound Capture Jar" (62637) to charasis/"Ghost Of Mera". Sets `ranger_epic15_pre` to `10`.
30. Loot "Echoing Jar" (62638) from "Ghost of Mera".
31. erudnint/"Mairee Silentone", hand "Stone of Winde" (62604) + "Echoing Jar" (62638). Requires `ranger_epic15_pre` ==10. Gives "Essence of Earth and Wind" (62600).

### "Corun's Notes" (62617)

1. qrg/"Corun Finisc", hand "Closed Medicine Bag" (62615). Gives "Sickly Mosquito Blood Sample" (62611).
2. Summon "Collapsible Fletching Kit" (17189) by casting "Unfold Fletching Kit".
3. Forage "Sickly Maiden's Hair" (62810) in `rathemtn`.
4. eastkarana/"Althele", hand "Sickly Maiden's Hair" (62810). Gives "Tuft of Sickly Maiden's Hair" (62811).
5. qrg/"Corun Finisc", hand "Tuft of Sickly Maiden's Hair" (62811). Gives "Magical Sample Vial" (62657).
6. cazicthule/"A Sickly Mosquito", on event hp.
7. Starts timer `check`.
8. No quest step gives Planar Fletching Kit (17762). The dump lists it in poknowledge.
9. Common item: Whittling Knife (62608). Listed in 4 zones.
10. Forage "Fallen Tree Branch" (62652) in `dranik`.
11. Forage "Fallen Tree Branch" (62652) in `draniksscar`.
12. Combine in "Planar Fletching Kit" (17762): "Whittling Knife" (62608), "Fallen Tree Branch" (62652). Produces "Long Net Pole" (62607). Requires Fletching 100. Trivial at 15. The combine does not fail.
13. Spawns "A Phase Spider" (123190) in `necropolis` on event_combat.
14. Loot "Phase Spider Silk" (55303) from "A Phase Spider".
15. Forage "Pine Sap" (62650) in `jaggedpine`.
16. Forage "Pine Sap" (62650) in `nedaria`.
17. Forage "Pine Sap" (62650) in `qrg`.
18. Combine in "Planar Fletching Kit" (17762): "Phase Spider Silk" (55303), "Pine Sap" (62650). Produces "Phase Netting" (62651). Requires Fletching 100. Trivial at 15. The combine does not fail.
19. Combine in "Planar Fletching Kit" (17762): "Long Net Pole" (62607), "Phase Netting" (62651). Produces "Large Butterfly Net" (62646). Requires Fletching 100. Trivial at 15. The combine does not fail.
20. Equip "Large Butterfly Net" (62646) in primary slot.
21. cazicthule/"A Sickly Mosquito", on timer check. Gives "Captured Mosquito" (62642).
22. Combine in "Collapsible Fletching Kit" (17189): "Magical Sample Vial" (62657), "Captured Mosquito" (62642). Produces "Sickly Mosquito Blood Sample" (62611). Requires Fletching. The combine does not fail.
23. qrg/"Corun Finisc", hand "Closed Medicine Bag" (62615). Gives "Twitching Swordfish Blood Sample" (62612).
24. sirens/"A Twitching Swordfish", on event hp.
25. Starts timer `check`.
26. Equip "Large Butterfly Net" (62646) in primary slot.
27. sirens/"A Twitching Swordfish", on timer check. Gives "Captured Swordfish" (62643).
28. Combine in "Collapsible Fletching Kit" (17189): "Magical Sample Vial" (62657), "Captured Swordfish" (62643). Produces "Twitching Swordfish Blood Sample" (62612). Requires Fletching. The combine does not fail.
29. qrg/"Corun Finisc", hand "Closed Medicine Bag" (62615). Gives "Bloated Drogan Spider Blood Sample" (62613).
30. droga/"A Bloated Drogan Spider", on event hp.
31. Starts timer `check`.
32. Common item: Hinge Mold (12027). Listed in 25 zones.
33. Common item: Container Base Mold (12062). Listed in 14 zones.
34. Common item: Container Lid Mold (12069). Listed in 14 zones.
35. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
36. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `steamfont`.
37. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `tox`.
38. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `toxxulia`.
39. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
40. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). The combine does not fail.
41. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
42. Say "Tm Devrak Death" to rujd/"Rujd".
43. Spawns "spawn chest with Heavy Orcish Prison Key" (245241).
44. Loot "Pod of Water" (13044) from "spawn chest with Heavy Orcish Prison Key".
45. 6 alternative loot source(s) also yield Pod of Water (13044).
46. Forage "Pod of Water" (13044) in `ruja`.
47. Forage "Pod of Water" (13044) in `uqua`.
48. Forage "Pod of Water" (13044) in `yxtta`.
49. Combine in Brew Barrel (19): "Bottle of Aged Bloodwine" (51163), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aged Bloodwine" (51164). Requires Brewing, trivial 255.
50. Combine in Brew Barrel (19): "Bottle of Aldo's Bitter Ale" (75805), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aldo's Bitter Ale" (75811). Requires Brewing, trivial 15.
51. 17 other recipes also produce Bottle (16598).
52. Combine in Brew Barrel (19): "Pod of Water" (13044), "Bottle" (16598). Produces "Water Flask" (13006). Requires Brewing, trivial 21.
53. No quest step gives Small Brick of Steel (66168). The dump lists it in qrg.
54. qrg/"Qaelin Hailstorm", say "Need A Mark". Gives "Mark of Karana" (66172).
55. Combine in Forge (17): "Hinge Mold" (12027), "Container Base Mold" (12062), "Container Lid Mold" (12069), "Water Flask" (13006), "Small Brick of Steel" (66168), "Mark of Karana" (66172). Hands back "Mark of Karana" (66172). Produces "Surefall Fletching Kit" (66163). Requires Blacksmithing, trivial 163.
56. Loot "Smithy Hammer" (10489) from "Gliblixl Rocktok" in `bazaar`.
57. Forage "Golanda Nut" (62610) in `causeway`.
58. Forage "Golanda Nut" (62610) in `dranik`.
59. Forage "Golanda Nut" (62610) in `draniksscar`.
60. Forage "Golanda Nut" (62610) in `provinggrounds`.
61. Forage "Golanda Nut" (62610) in `riftseekers`.
62. Forage "Golanda Nut" (62610) in `wallofslaughter`.
63. Combine in "Surefall Fletching Kit" (66163): "Smithy Hammer" (10489), "Golanda Nut" (62610). Hands back "Smithy Hammer" (10489). Produces "Fibrous Rope" (62609). Requires Fletching 100. Trivial at 15. The combine does not fail.
64. Combine in "Surefall Fletching Kit" (66163): "Fibrous Rope" (62609). Produces "Eight-loop Lasso" (62648). Requires Fletching 100. Trivial at 15. The combine does not fail.
65. Equip "Eight-loop Lasso" (62648) in primary slot.
66. droga/"A Bloated Drogan Spider", on timer check. Gives "Captured Spider" (62644).
67. Combine in "Collapsible Fletching Kit" (17189): "Magical Sample Vial" (62657), "Captured Spider" (62644). Produces "Bloated Drogan Spider Blood Sample" (62613). Requires Fletching. The combine does not fail.
68. qrg/"Corun Finisc", hand "Closed Medicine Bag" (62615). Gives "Leprous Chokidai Blood Sample" (62614).
69. chardokb/"A Leprous Chokidai", on event hp.
70. Starts timer `check`.
71. Equip "Eight-loop Lasso" (62648) in primary slot.
72. chardokb/"A Leprous Chokidai", on timer check. Gives "Captured Chokidai" (62645).
73. Combine in "Collapsible Fletching Kit" (17189): "Magical Sample Vial" (62657), "Captured Chokidai" (62645). Produces "Leprous Chokidai Blood Sample" (62614). Requires Fletching. The combine does not fail.
74. Combine in "Borrowed Medicine Bag" (62605): "Sickly Mosquito Blood Sample" (62611), "Twitching Swordfish Blood Sample" (62612), "Bloated Drogan Spider Blood Sample" (62613), "Leprous Chokidai Blood Sample" (62614). Produces "Closed Medicine Bag" (62615). The combine does not fail.
75. qrg/"Corun Finisc", hand "Closed Medicine Bag" (62615). Gives "Borrowed Medicine Bag" (62605).
76. Unresolved cyclic prerequisite: `warrior_epic_gulak` ==1.
77. Unresolved cyclic prerequisite: `warrior_epic` ==17.
78. Ground spawn of "Frozen Pestle" (60323) in `iceclad`.
79. iceclad/"Fazzle Thumpkin", hand "Frozen Pestle" (60323). Sets `warrior_epic` to `18`.
80. Loot "Kreljnok's Muddled Rage" (60322) from "Possessed Brute" in `provinggrounds`.
81. draniksscar/"Korbuk Brimblade", hand "Kreljnok's Muddled Rage" (60322). Sets `warrior_epic` to `17`.
82. firiona/"Corfia Nultethen", say "Galuk Drek". Sets `warrior_epic_veksar` to `1`.
83. burningwood/"Telin Darkforest", say "Action". Gives "Worn Note" (20472).
84. gfaydark/"Faelin Bloodbriar", hand "Worn Note" (20472). Gives "Faelin's Ring" (20446).
85. kithicor/"Giz X-Tin", hand "Faelin's Ring" (20446). Gives "Dark Metal Coin" (20447).
86. burningwood/"Telin Darkforest", hand "Dark Metal Coin" (20447). Gives "Worn Dark Metal Coin" (20448).
87. eastkarana/"Althele", hand "Worn Dark Metal Coin" (20448). Gives "Braided Grass Amulet" (20450).
88. eastkarana/"Sionae", hand "Braided Grass Amulet" (20450). Gives "Frayed Braided Grass Amulet" (20451).
89. eastkarana/"Teloa", hand "Frayed Braided Grass Amulet" (20451). Triggers `eastkarana/althele#signal:1`.
90. Starts timer `attack`.
91. Spawns "Corruptor" (15153) after `eastkarana/althele#timer:attack`.
92. Loot "Fleshbound Tome" (20452) from "Corruptor".
93. eastkarana/"Althele", hand "Fleshbound Tome" (20452). Gives "Earth Stained Note" (18959).
94. misty/"Ella Foodcrafter", hand "Earth Stained Note" (18959). Sets `shiny_tin_bowl` to `1`.
95. misty/"Ella Foodcrafter", say "Two Tasks". Requires `shiny_tin_bowl` set. Gives "Shiny Tin Bowl" (17860).
96. Hand "Shiny Tin Bowl" (17860) to hole/"Jaeil The Wretched". Spawns "Jaeil the Insane" (39154). Loot "Soulbound Hammer" (20478) from "Jaeil the Insane".
97. erudnint/"Mairee Silentone", hand "Soulbound Hammer" (20478). Gives "Dwarven Smiths Hammer" (20479).
98. Kill airplane/"An Essence Carrier". Spawns "An Essence Tamer" (71071).
99. Loot "Swirling Sphere of Color" (20494) from "An Essence Tamer".
100. erudnint/"Mairee Silentone", hand "Dwarven Smiths Hammer" (20479) + "Swirling Sphere of Color" (20494). Gives "Hammer of the Ancients" (20485).
101. kaladimb/"Kinlo Strongarm", hand "Hammer of the Ancients" (20485). Gives "Small bit of Mithril Ore" (20482).
102. kaladimb/"Kinlo Strongarm", hand "Small bit of Mithril Ore" (20482). Gives "Refined Mithril Blade" (20483).
103. Encounter starts when NPC 186201 spawns in `hateplaneb`.
104. Starts timer `popinny`.
105. Kill NPC 186158.
106. Starts timer `text`.
107. Starts timer `text2`.
108. Starts timer `spawninny`.
109. Spawns "Innoruuk" (186107) after `hateplaneb/inny#timer:spawninny`.
110. Loot "Shattered Emerald of Corruption" (20484) from "Innoruuk".
111. 1 alternative loot source(s) also yield Shattered Emerald of Corruption (20484).
112. northkarana/"Xanuusus", hand "Refined Mithril Blade" (20483) + "Shattered Emerald of Corruption" (20484). Gives "Earthcaller" (20488).
113. eastkarana/"Althele", say "Hail". Sets `ranger_epic` to `1`.
114. veksar/"Player", on enter. Sets `warrior_epic_gulak` to `1`.
115. Spawns "An Asteatotic Highborn" (109907) in `veksar` on enter.
116. Loot "Asteatotic Veksar Blood" (35100) from "An Asteatotic Highborn".
117. Spawns "A Neuralgic Huntress" (120136) in `westwastes` on enter.
118. Loot "Neuralgic Wyvern Blood" (72605) from "A Neuralgic Huntress".
119. Combine in "Borrowed Medicine Bag" (62605): "Asteatotic Veksar Blood" (35100), "Neuralgic Wyvern Blood" (72605), "Sickly Mosquito Blood Sample" (62611), "Twitching Swordfish Blood Sample" (62612), "Leprous Chokidai Blood Sample" (62614), "Bloated Drogan Spider Blood Sample" (62613). Produces "Full Medicine Bag" (62616). The combine does not fail.
120. qrg/"Corun Finisc", hand "Full Medicine Bag" (62616). Gives "Corun's Notes" (62617).

### "Senvial's Blessing" (62621)

1. Forage "Sickly Maiden's Hair" (62810) in `rathemtn`.
2. eastkarana/"Althele", hand "Sickly Maiden's Hair" (62810). Gives "Tuft of Sickly Maiden's Hair" (62811).
3. qrg/"Niera Farbreeze", hand "Tuft of Sickly Maiden's Hair" (62811). Gives "Waterproof Collection Bag" (62812).
4. Say "King Timer" to frontiermtns/"Druid 1 5".
5. Spawns npc 92202 (92202).
6. Loot "Bag of Diseased Maiden's Hair" (62826) from npc 92202.
7. burningwood/"Telin Darkforest", say "Action". Gives "Worn Note" (20472).
8. gfaydark/"Faelin Bloodbriar", hand "Worn Note" (20472). Gives "Faelin's Ring" (20446).
9. kithicor/"Giz X-Tin", hand "Faelin's Ring" (20446). Gives "Dark Metal Coin" (20447).
10. burningwood/"Telin Darkforest", hand "Dark Metal Coin" (20447). Gives "Worn Dark Metal Coin" (20448).
11. eastkarana/"Althele", hand "Worn Dark Metal Coin" (20448). Gives "Braided Grass Amulet" (20450).
12. eastkarana/"Sionae", hand "Braided Grass Amulet" (20450). Gives "Frayed Braided Grass Amulet" (20451).
13. eastkarana/"Teloa", hand "Frayed Braided Grass Amulet" (20451). Triggers `eastkarana/althele#signal:1`.
14. Starts timer `attack`.
15. Spawns "Corruptor" (15153) after `eastkarana/althele#timer:attack`.
16. Loot "Fleshbound Tome" (20452) from "Corruptor".
17. eastkarana/"Althele", hand "Fleshbound Tome" (20452). Gives "Earth Stained Note" (18959).
18. misty/"Ella Foodcrafter", hand "Earth Stained Note" (18959). Sets `shiny_tin_bowl` to `1`.
19. misty/"Ella Foodcrafter", say "Two Tasks". Requires `shiny_tin_bowl` set. Gives "Shiny Tin Bowl" (17860).
20. Hand "Shiny Tin Bowl" (17860) to hole/"Jaeil The Wretched". Spawns "Jaeil the Insane" (39154). Loot "Soulbound Hammer" (20478) from "Jaeil the Insane".
21. erudnint/"Mairee Silentone", hand "Soulbound Hammer" (20478). Gives "Dwarven Smiths Hammer" (20479).
22. Kill airplane/"An Essence Carrier". Spawns "An Essence Tamer" (71071).
23. Loot "Swirling Sphere of Color" (20494) from "An Essence Tamer".
24. erudnint/"Mairee Silentone", hand "Dwarven Smiths Hammer" (20479) + "Swirling Sphere of Color" (20494). Gives "Hammer of the Ancients" (20485).
25. kaladimb/"Kinlo Strongarm", hand "Hammer of the Ancients" (20485). Gives "Small bit of Mithril Ore" (20482).
26. kaladimb/"Kinlo Strongarm", hand "Small bit of Mithril Ore" (20482). Gives "Refined Mithril Blade" (20483).
27. Encounter starts when NPC 186201 spawns in `hateplaneb`.
28. Starts timer `popinny`.
29. Kill NPC 186158.
30. Starts timer `text`.
31. Starts timer `text2`.
32. Starts timer `spawninny`.
33. Spawns "Innoruuk" (186107) after `hateplaneb/inny#timer:spawninny`.
34. Loot "Shattered Emerald of Corruption" (20484) from "Innoruuk".
35. 1 alternative loot source(s) also yield Shattered Emerald of Corruption (20484).
36. northkarana/"Xanuusus", hand "Refined Mithril Blade" (20483) + "Shattered Emerald of Corruption" (20484). Gives "Earthcaller" (20488).
37. eastkarana/"Althele", say "Hail". Sets `ranger_epic` to `1`.
38. Loot "Froglok Essence" (20696) from "Ulump Pujluk" in `swampofnohope`.
39. Kill emeraldjungle/"Tainted Gorilla". Spawns "Corrupted Gorilla" (94140).
40. Loot "Green Tree Bark" (20686) from "Corrupted Gorilla".
41. Kill lakeofillomen/"Tainted Barracuda". Spawns "Corrupted Barracuda" (85224).
42. Loot "Pure Lakewater" (20685) from "Corrupted Barracuda".
43. Hand "Froglok Essence" (20696) to timorous/"Dolgin Codslayer". Spawns "Faydedar" (96073). Loot "Pod of Seawater" (20687) from "Faydedar".
44. overthere/"Nekexin Virulence", hand "Pure Lakewater" (20685) + "Green Tree Bark" (20686) + "Pod of Seawater" (20687) + "Froglok Essence" (20696). Gives "Cleansed Spirit of Kunark" (20699).
45. Kill kedge/"Tainted Seahorse". Spawns "Corrupted Seahorse" (64050).
46. Loot "Kedge Cave Crystals" (20691) from "Corrupted Seahorse".
47. Kill oceanoftears/"Tainted Seafury Cyclops". Spawns "Corrupted Seafury Cyclops" (69142).
48. Loot "Ocean of Tears Seavines" (20692) from "Corrupted Seafury Cyclops".
49. 1 alternative loot source(s) also yield Ocean of Tears Seavines (20692).
50. Kill lfaydark/"Tainted Brownie". Spawns "Corrupted Brownie" (57117).
51. Loot "Green Heartwood Branch" (20693) from "Corrupted Brownie".
52. lfaydark/"Pained Unicorn", hand "Kedge Cave Crystals" (20691) + "Ocean of Tears Seavines" (20692) + "Green Heartwood Branch" (20693). Gives "Gleaming Unicorn Horn" (20694).
53. akanon/"Silox Azrix", hand "Gleaming Unicorn Horn" (20694). Gives "Cleansed Spirit of Faydwer" (20697).
54. Loot "Ring of the Ancients" (12268) from "The Fabled Ancient Cyclops" in `sro`.
55. Loot "Ring of the Ancients" (12268) from "An Ancient Cyclops".
56. Loot "Ring of the Ancients" (12268) from "An Ancient Cyclops" in `oot`.
57. Loot "Ring of the Ancients" (12268) from "An Ancient Cyclops" in `sro`.
58. Kill rathemtn/"Ytyrs The Reborn". Spawns "Ytyrs Reborn" (50346).
59. Loot "Shadowed Rapier" (7100) from "Ytyrs Reborn".
60. rathemtn/"Hasten Bootstrutter", hand "Shadowed Rapier" (7100) + "Ring of the Ancients" (12268). Gives "Journeyman's Boots" (2300).
61. northkarana/"Triathalon Token", hand "Journeyman's Boots" (2300). Gives "Warm Pulsing Treant Heart" (20695).
62. southkarana/"Yeka Ias", hand "Warm Pulsing Treant Heart" (20695). Gives "Cleansed Spirit of Antonica" (20698).
63. Forage "Ripened Heartfruit" (20464) in `gfaydark`.
64. Forage "Sweetened Mudroot" (20465) in `misty`.
65. Forage "Sweetened Mudroot" (20465) in `mistythicket`.
66. Forage "Speckled Molded Mushroom" (20466) in `innothule`.
67. Forage "Chilled Tundra Root" (20467) in `everfrost`.
68. Combine in "Shiny Tin Bowl" (17860): "Ripened Heartfruit" (20464), "Sweetened Mudroot" (20465), "Speckled Molded Mushroom" (20466), "Chilled Tundra Root" (20467). Produces "Hardened Mixture" (20473). Requires Pottery. The combine does not fail.
69. timorous/"Alrik Farsight", say "Take The Artifact". Gives "Crushed Pot" (20457).
70. felwitheb/"Farios Elianos", hand "Crushed Pot" (20457). Gives "Grocery List" (20458).
71. felwithea/"Merchant Nora", hand "Grocery List" (20458). Gives "Bag of Provisions" (20459).
72. felwitheb/"Farios Elianos", hand "Bag of Provisions" (20459). Gives "Receipt" (20474).
73. timorous/"Alrik Farsight", hand "Receipt" (20474). Gives "Ancient Pattern" (18960).
74. Kill citymist/"A Black Reaver". Spawns "A Black Reaver" (90004).
75. Loot "Jade Reaver" (5664) from "A Black Reaver".
76. 2 alternative loot source(s) also yield Jade Reaver (5664).
77. kaladimb/"Kinlo Strongarm", hand "Jade Reaver" (5664). Gives "Enchanted Clay" (20455).
78. Forage "Rose of Firiona" (12774) in `firiona`.
79. qrg/"Merdan Fleetfoot", hand "Rose of Firiona" (12774). Gives "Wood Painting" (20475).
80. frontiermtns/"A Human Skeleton", hand "Wood Painting" (20475). Gives "Silver Chained Locket" (20476).
81. qrg/"Niera Farbreeze", hand "Silver Chained Locket" (20476). Gives "Platinum Speckled Powder" (20456).
82. Combine in Pottery Wheel (21): "Ancient Pattern" (18960), "Enchanted Clay" (20455), "Platinum Speckled Powder" (20456). Produces "Runecrested Bowl" (20460). Requires Pottery. The combine does not fail.
83. misty/"Ella Foodcrafter", hand "Runecrested Bowl" (20460) + "Hardened Mixture" (20473). Gives "Softly Glowing Stone" (20462).
84. Common item: Spell: Resurrection (15392). Listed in 14 zones.
85. Hand "Spell: Resurrection" (15392) to karnor/"Spirit Of Venril Sathir". Spawns "Venril Sathir" (102126). Loot "Pulsing Green Stone" (20461) from "Venril Sathir".
86. firiona/"Foloal Stormforest", hand "Pulsing Green Stone" (20461) + "Softly Glowing Stone" (20462). Gives "Warmly Glowing Stone" (20468).
87. misty/"Ella Foodcrafter", hand "Warmly Glowing Stone" (20468). Gives "Elaborate Scimitar" (20440).
88. northkarana/"Xanuusus", hand "Elaborate Scimitar" (20440) + "Cleansed Spirit of Faydwer" (20697) + "Cleansed Spirit of Antonica" (20698) + "Cleansed Spirit of Kunark" (20699). Gives "Nature Walkers Scimitar" (20490).
89. eastkarana/"Althele", say "Out Of Balance". Sets `druid_epic` to `1`.
90. Spawns "A Bloodgill Forager" (85234) in `lakeofillomen` on enter.
91. Loot "Handful of Diseased Maiden's Hair" (62825) from "A Bloodgill Forager".
92. Common item: Tackle Box (17048). Listed in 11 zones.
93. Spawns "Ulthork Raider" (116608) in `eastwastes` on enter.
94. Loot "Carved Prexus Totem" (62821) from "Ulthork Raider".
95. cobaltscar/"Blumblum Swigwater", hand "Carved Prexus Totem" (62821). Gives "Small Trigger Fish" (62820).
96. Common item: Gutting Knife (62823). Listed in 4 zones.
97. Combine in "Tackle Box" (17048): "Small Trigger Fish" (62820), "Gutting Knife" (62823). Hands back "Gutting Knife" (62823). Produces "Soggy Maiden's Hair" (62824). Requires Fishing, trivial 20. The combine does not fail.
98. Spawns "spawn #Swamp Terror" (47208) in `feerrott` on enter.
99. Loot "Partially Digested Maiden's Hair" (62819) from "spawn #Swamp Terror".
100. Combine in "Waterproof Collection Bag" (62812): "Bag of Diseased Maiden's Hair" (62826), "Handful of Diseased Maiden's Hair" (62825), "Soggy Maiden's Hair" (62824), "Partially Digested Maiden's Hair" (62819). Produces "Sealed Collection Bag" (62813). The combine does not fail.
101. qrg/"Niera Farbreeze", hand "Sealed Collection Bag" (62813). Gives "Wash Cloth" (62847).
102. Spawns "spawn #Swamp Terror" (47208) in `feerrott` on enter.
103. Loot "Mangled Head" (62818) from "spawn #Swamp Terror".
104. Combine in "Wash Cloth" (62847): "Mangled Head" (62818). Produces "Wrapped Mangled Head" (62848). The combine does not fail.
105. qrg/"Niera Farbreeze", hand "Wrapped Mangled Head" (62848). Gives "Mangled Head" (62827).
106. qrg/"Niera Farbreeze", hand "Wrapped Mangled Head" (62848). Sets `druid_epic` to `2`.
107. poknowledge/"Pathfinder Arelat", say "Worth It". Requires `druid_epic` ==2. Gives "Fresh Awakenings vol. 1" (62839).
108. poknowledge/"Pathfinder Arelat", say "Worth It". Requires `druid_epic` ==2. Gives "Fresh Awakenings vol. 2" (62840).
109. poknowledge/"Pathfinder Arelat", say "Worth It". Requires `druid_epic` ==2. Gives "Fresh Awakenings vol. 3" (62841).
110. poknowledge/"Gravelady Beddia", hand "Fresh Awakenings vol. 1" (62839) + "Fresh Awakenings vol. 2" (62840) + "Fresh Awakenings vol. 3" (62841). Gives "Healing Plants" (62842).
111. qrg/"Niera Farbreeze", hand "Healing Plants" (62842). Sets `druid_epic` to `3`.
112. feerrott/"Corrupted Spirit", say "Show It". Requires `druid_epic` ==3. Gives "Disease Rune" (62837).
113. tox/"A Skeleton", say "I Will Do It". Triggers `tox/a skeleton#timer:pathback`.
114. Starts timer `pathbacktwo`.
115. Starts timer `pathbackthree`.
116. Starts timer `giveitem`.
117. tox/"A Skeleton", on timer giveitem. Gives "Animating Heads" (62828).
118. Combine in "Mangled Head" (62827): "Disease Rune" (62837), "Animating Heads" (62828). Produces "Runed Skull" (62838). The combine does not fail.
119. qrg/"Niera Farbreeze", hand "Healing Plants" (62842). Gives "Niera's Healing Notes" (62849).
120. qrg/"Niera Farbreeze", hand "Runed Skull" (62838) + "Niera's Healing Notes" (62849). Sets `druid_epic` to `4`.
121. qrg/"Niera Farbreeze", hand "Runed Skull" (62838) + "Niera's Healing Notes" (62849). Gives "Niera's Research Notes" (62843).
122. pojustice/"Great Bear", hand "Niera's Research Notes" (62843). Requires `druid_epic` ==4. Gives "Red Dogwood Seed" (62844).
123. qrg/"Corun Finisc", hand "Closed Medicine Bag" (62615). Gives "Sickly Mosquito Blood Sample" (62611).
124. Summon "Collapsible Fletching Kit" (17189) by casting "Unfold Fletching Kit".
125. qrg/"Corun Finisc", hand "Tuft of Sickly Maiden's Hair" (62811). Gives "Magical Sample Vial" (62657).
126. cazicthule/"A Sickly Mosquito", on event hp.
127. Starts timer `check`.
128. No quest step gives Planar Fletching Kit (17762). The dump lists it in poknowledge.
129. Common item: Whittling Knife (62608). Listed in 4 zones.
130. Forage "Fallen Tree Branch" (62652) in `dranik`.
131. Forage "Fallen Tree Branch" (62652) in `draniksscar`.
132. Combine in "Planar Fletching Kit" (17762): "Whittling Knife" (62608), "Fallen Tree Branch" (62652). Produces "Long Net Pole" (62607). Requires Fletching 100. Trivial at 15. The combine does not fail.
133. Spawns "A Phase Spider" (123190) in `necropolis` on event_combat.
134. Loot "Phase Spider Silk" (55303) from "A Phase Spider".
135. Forage "Pine Sap" (62650) in `jaggedpine`.
136. Forage "Pine Sap" (62650) in `nedaria`.
137. Forage "Pine Sap" (62650) in `qrg`.
138. Combine in "Planar Fletching Kit" (17762): "Phase Spider Silk" (55303), "Pine Sap" (62650). Produces "Phase Netting" (62651). Requires Fletching 100. Trivial at 15. The combine does not fail.
139. Combine in "Planar Fletching Kit" (17762): "Long Net Pole" (62607), "Phase Netting" (62651). Produces "Large Butterfly Net" (62646). Requires Fletching 100. Trivial at 15. The combine does not fail.
140. Equip "Large Butterfly Net" (62646) in primary slot.
141. cazicthule/"A Sickly Mosquito", on timer check. Gives "Captured Mosquito" (62642).
142. Combine in "Collapsible Fletching Kit" (17189): "Magical Sample Vial" (62657), "Captured Mosquito" (62642). Produces "Sickly Mosquito Blood Sample" (62611). Requires Fletching. The combine does not fail.
143. qrg/"Corun Finisc", hand "Closed Medicine Bag" (62615). Gives "Twitching Swordfish Blood Sample" (62612).
144. sirens/"A Twitching Swordfish", on event hp.
145. Starts timer `check`.
146. Equip "Large Butterfly Net" (62646) in primary slot.
147. sirens/"A Twitching Swordfish", on timer check. Gives "Captured Swordfish" (62643).
148. Combine in "Collapsible Fletching Kit" (17189): "Magical Sample Vial" (62657), "Captured Swordfish" (62643). Produces "Twitching Swordfish Blood Sample" (62612). Requires Fletching. The combine does not fail.
149. qrg/"Corun Finisc", hand "Closed Medicine Bag" (62615). Gives "Bloated Drogan Spider Blood Sample" (62613).
150. droga/"A Bloated Drogan Spider", on event hp.
151. Starts timer `check`.
152. Common item: Hinge Mold (12027). Listed in 25 zones.
153. Common item: Container Base Mold (12062). Listed in 14 zones.
154. Common item: Container Lid Mold (12069). Listed in 14 zones.
155. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
156. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `steamfont`.
157. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `tox`.
158. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `toxxulia`.
159. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
160. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). The combine does not fail.
161. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
162. Say "Tm Devrak Death" to rujd/"Rujd".
163. Spawns "spawn chest with Heavy Orcish Prison Key" (245241).
164. Loot "Pod of Water" (13044) from "spawn chest with Heavy Orcish Prison Key".
165. 6 alternative loot source(s) also yield Pod of Water (13044).
166. Forage "Pod of Water" (13044) in `ruja`.
167. Forage "Pod of Water" (13044) in `uqua`.
168. Forage "Pod of Water" (13044) in `yxtta`.
169. Combine in Brew Barrel (19): "Bottle of Aged Bloodwine" (51163), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aged Bloodwine" (51164). Requires Brewing, trivial 255.
170. Combine in Brew Barrel (19): "Bottle of Aldo's Bitter Ale" (75805), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aldo's Bitter Ale" (75811). Requires Brewing, trivial 15.
171. 17 other recipes also produce Bottle (16598).
172. Combine in Brew Barrel (19): "Pod of Water" (13044), "Bottle" (16598). Produces "Water Flask" (13006). Requires Brewing, trivial 21.
173. No quest step gives Small Brick of Steel (66168). The dump lists it in qrg.
174. qrg/"Qaelin Hailstorm", say "Need A Mark". Gives "Mark of Karana" (66172).
175. Combine in Forge (17): "Hinge Mold" (12027), "Container Base Mold" (12062), "Container Lid Mold" (12069), "Water Flask" (13006), "Small Brick of Steel" (66168), "Mark of Karana" (66172). Hands back "Mark of Karana" (66172). Produces "Surefall Fletching Kit" (66163). Requires Blacksmithing, trivial 163.
176. Loot "Smithy Hammer" (10489) from "Gliblixl Rocktok" in `bazaar`.
177. Forage "Golanda Nut" (62610) in `causeway`.
178. Forage "Golanda Nut" (62610) in `dranik`.
179. Forage "Golanda Nut" (62610) in `draniksscar`.
180. Forage "Golanda Nut" (62610) in `provinggrounds`.
181. Forage "Golanda Nut" (62610) in `riftseekers`.
182. Forage "Golanda Nut" (62610) in `wallofslaughter`.
183. Combine in "Surefall Fletching Kit" (66163): "Smithy Hammer" (10489), "Golanda Nut" (62610). Hands back "Smithy Hammer" (10489). Produces "Fibrous Rope" (62609). Requires Fletching 100. Trivial at 15. The combine does not fail.
184. Combine in "Surefall Fletching Kit" (66163): "Fibrous Rope" (62609). Produces "Eight-loop Lasso" (62648). Requires Fletching 100. Trivial at 15. The combine does not fail.
185. Equip "Eight-loop Lasso" (62648) in primary slot.
186. droga/"A Bloated Drogan Spider", on timer check. Gives "Captured Spider" (62644).
187. Combine in "Collapsible Fletching Kit" (17189): "Magical Sample Vial" (62657), "Captured Spider" (62644). Produces "Bloated Drogan Spider Blood Sample" (62613). Requires Fletching. The combine does not fail.
188. qrg/"Corun Finisc", hand "Closed Medicine Bag" (62615). Gives "Leprous Chokidai Blood Sample" (62614).
189. chardokb/"A Leprous Chokidai", on event hp.
190. Starts timer `check`.
191. Equip "Eight-loop Lasso" (62648) in primary slot.
192. chardokb/"A Leprous Chokidai", on timer check. Gives "Captured Chokidai" (62645).
193. Combine in "Collapsible Fletching Kit" (17189): "Magical Sample Vial" (62657), "Captured Chokidai" (62645). Produces "Leprous Chokidai Blood Sample" (62614). Requires Fletching. The combine does not fail.
194. Combine in "Borrowed Medicine Bag" (62605): "Sickly Mosquito Blood Sample" (62611), "Twitching Swordfish Blood Sample" (62612), "Bloated Drogan Spider Blood Sample" (62613), "Leprous Chokidai Blood Sample" (62614). Produces "Closed Medicine Bag" (62615). The combine does not fail.
195. qrg/"Corun Finisc", hand "Closed Medicine Bag" (62615). Gives "Borrowed Medicine Bag" (62605).
196. Unresolved cyclic prerequisite: `warrior_epic_gulak` ==1.
197. Unresolved cyclic prerequisite: `warrior_epic` ==17.
198. Ground spawn of "Frozen Pestle" (60323) in `iceclad`.
199. iceclad/"Fazzle Thumpkin", hand "Frozen Pestle" (60323). Sets `warrior_epic` to `18`.
200. Loot "Kreljnok's Muddled Rage" (60322) from "Possessed Brute" in `provinggrounds`.
201. draniksscar/"Korbuk Brimblade", hand "Kreljnok's Muddled Rage" (60322). Sets `warrior_epic` to `17`.
202. firiona/"Corfia Nultethen", say "Galuk Drek". Sets `warrior_epic_veksar` to `1`.
203. veksar/"Player", on enter. Sets `warrior_epic_gulak` to `1`.
204. Spawns "An Asteatotic Highborn" (109907) in `veksar` on enter.
205. Loot "Asteatotic Veksar Blood" (35100) from "An Asteatotic Highborn".
206. Spawns "A Neuralgic Huntress" (120136) in `westwastes` on enter.
207. Loot "Neuralgic Wyvern Blood" (72605) from "A Neuralgic Huntress".
208. Combine in "Borrowed Medicine Bag" (62605): "Asteatotic Veksar Blood" (35100), "Neuralgic Wyvern Blood" (72605), "Sickly Mosquito Blood Sample" (62611), "Twitching Swordfish Blood Sample" (62612), "Leprous Chokidai Blood Sample" (62614), "Bloated Drogan Spider Blood Sample" (62613). Produces "Full Medicine Bag" (62616). The combine does not fail.
209. qrg/"Corun Finisc", hand "Full Medicine Bag" (62616). Gives "Corun's Notes" (62617).
210. freeportwest/"Shana Liskia", hand "Corun's Notes" (62617). Sets `ranger_epic` to `2`.
211. natimbi/"Ranger 1 5", say "Hail". Requires `ranger_epic` set. Requires `ranger_epic` ==2. Requires `ranger_natimbi_chest` unset. Gives "Senvial's Blessing" (62621).

### "Grinbik's Blessing" (62622)

1. Forage "Sickly Maiden's Hair" (62810) in `rathemtn`.
2. eastkarana/"Althele", hand "Sickly Maiden's Hair" (62810). Gives "Tuft of Sickly Maiden's Hair" (62811).
3. qrg/"Niera Farbreeze", hand "Tuft of Sickly Maiden's Hair" (62811). Gives "Waterproof Collection Bag" (62812).
4. Say "King Timer" to frontiermtns/"Druid 1 5".
5. Spawns npc 92202 (92202).
6. Loot "Bag of Diseased Maiden's Hair" (62826) from npc 92202.
7. burningwood/"Telin Darkforest", say "Action". Gives "Worn Note" (20472).
8. gfaydark/"Faelin Bloodbriar", hand "Worn Note" (20472). Gives "Faelin's Ring" (20446).
9. kithicor/"Giz X-Tin", hand "Faelin's Ring" (20446). Gives "Dark Metal Coin" (20447).
10. burningwood/"Telin Darkforest", hand "Dark Metal Coin" (20447). Gives "Worn Dark Metal Coin" (20448).
11. eastkarana/"Althele", hand "Worn Dark Metal Coin" (20448). Gives "Braided Grass Amulet" (20450).
12. eastkarana/"Sionae", hand "Braided Grass Amulet" (20450). Gives "Frayed Braided Grass Amulet" (20451).
13. eastkarana/"Teloa", hand "Frayed Braided Grass Amulet" (20451). Triggers `eastkarana/althele#signal:1`.
14. Starts timer `attack`.
15. Spawns "Corruptor" (15153) after `eastkarana/althele#timer:attack`.
16. Loot "Fleshbound Tome" (20452) from "Corruptor".
17. eastkarana/"Althele", hand "Fleshbound Tome" (20452). Gives "Earth Stained Note" (18959).
18. misty/"Ella Foodcrafter", hand "Earth Stained Note" (18959). Sets `shiny_tin_bowl` to `1`.
19. misty/"Ella Foodcrafter", say "Two Tasks". Requires `shiny_tin_bowl` set. Gives "Shiny Tin Bowl" (17860).
20. Hand "Shiny Tin Bowl" (17860) to hole/"Jaeil The Wretched". Spawns "Jaeil the Insane" (39154). Loot "Soulbound Hammer" (20478) from "Jaeil the Insane".
21. erudnint/"Mairee Silentone", hand "Soulbound Hammer" (20478). Gives "Dwarven Smiths Hammer" (20479).
22. Kill airplane/"An Essence Carrier". Spawns "An Essence Tamer" (71071).
23. Loot "Swirling Sphere of Color" (20494) from "An Essence Tamer".
24. erudnint/"Mairee Silentone", hand "Dwarven Smiths Hammer" (20479) + "Swirling Sphere of Color" (20494). Gives "Hammer of the Ancients" (20485).
25. kaladimb/"Kinlo Strongarm", hand "Hammer of the Ancients" (20485). Gives "Small bit of Mithril Ore" (20482).
26. kaladimb/"Kinlo Strongarm", hand "Small bit of Mithril Ore" (20482). Gives "Refined Mithril Blade" (20483).
27. Encounter starts when NPC 186201 spawns in `hateplaneb`.
28. Starts timer `popinny`.
29. Kill NPC 186158.
30. Starts timer `text`.
31. Starts timer `text2`.
32. Starts timer `spawninny`.
33. Spawns "Innoruuk" (186107) after `hateplaneb/inny#timer:spawninny`.
34. Loot "Shattered Emerald of Corruption" (20484) from "Innoruuk".
35. 1 alternative loot source(s) also yield Shattered Emerald of Corruption (20484).
36. northkarana/"Xanuusus", hand "Refined Mithril Blade" (20483) + "Shattered Emerald of Corruption" (20484). Gives "Earthcaller" (20488).
37. eastkarana/"Althele", say "Hail". Sets `ranger_epic` to `1`.
38. Loot "Froglok Essence" (20696) from "Ulump Pujluk" in `swampofnohope`.
39. Kill emeraldjungle/"Tainted Gorilla". Spawns "Corrupted Gorilla" (94140).
40. Loot "Green Tree Bark" (20686) from "Corrupted Gorilla".
41. Kill lakeofillomen/"Tainted Barracuda". Spawns "Corrupted Barracuda" (85224).
42. Loot "Pure Lakewater" (20685) from "Corrupted Barracuda".
43. Hand "Froglok Essence" (20696) to timorous/"Dolgin Codslayer". Spawns "Faydedar" (96073). Loot "Pod of Seawater" (20687) from "Faydedar".
44. overthere/"Nekexin Virulence", hand "Pure Lakewater" (20685) + "Green Tree Bark" (20686) + "Pod of Seawater" (20687) + "Froglok Essence" (20696). Gives "Cleansed Spirit of Kunark" (20699).
45. Kill kedge/"Tainted Seahorse". Spawns "Corrupted Seahorse" (64050).
46. Loot "Kedge Cave Crystals" (20691) from "Corrupted Seahorse".
47. Kill oceanoftears/"Tainted Seafury Cyclops". Spawns "Corrupted Seafury Cyclops" (69142).
48. Loot "Ocean of Tears Seavines" (20692) from "Corrupted Seafury Cyclops".
49. 1 alternative loot source(s) also yield Ocean of Tears Seavines (20692).
50. Kill lfaydark/"Tainted Brownie". Spawns "Corrupted Brownie" (57117).
51. Loot "Green Heartwood Branch" (20693) from "Corrupted Brownie".
52. lfaydark/"Pained Unicorn", hand "Kedge Cave Crystals" (20691) + "Ocean of Tears Seavines" (20692) + "Green Heartwood Branch" (20693). Gives "Gleaming Unicorn Horn" (20694).
53. akanon/"Silox Azrix", hand "Gleaming Unicorn Horn" (20694). Gives "Cleansed Spirit of Faydwer" (20697).
54. Loot "Ring of the Ancients" (12268) from "The Fabled Ancient Cyclops" in `sro`.
55. Loot "Ring of the Ancients" (12268) from "An Ancient Cyclops".
56. Loot "Ring of the Ancients" (12268) from "An Ancient Cyclops" in `oot`.
57. Loot "Ring of the Ancients" (12268) from "An Ancient Cyclops" in `sro`.
58. Kill rathemtn/"Ytyrs The Reborn". Spawns "Ytyrs Reborn" (50346).
59. Loot "Shadowed Rapier" (7100) from "Ytyrs Reborn".
60. rathemtn/"Hasten Bootstrutter", hand "Shadowed Rapier" (7100) + "Ring of the Ancients" (12268). Gives "Journeyman's Boots" (2300).
61. northkarana/"Triathalon Token", hand "Journeyman's Boots" (2300). Gives "Warm Pulsing Treant Heart" (20695).
62. southkarana/"Yeka Ias", hand "Warm Pulsing Treant Heart" (20695). Gives "Cleansed Spirit of Antonica" (20698).
63. Forage "Ripened Heartfruit" (20464) in `gfaydark`.
64. Forage "Sweetened Mudroot" (20465) in `misty`.
65. Forage "Sweetened Mudroot" (20465) in `mistythicket`.
66. Forage "Speckled Molded Mushroom" (20466) in `innothule`.
67. Forage "Chilled Tundra Root" (20467) in `everfrost`.
68. Combine in "Shiny Tin Bowl" (17860): "Ripened Heartfruit" (20464), "Sweetened Mudroot" (20465), "Speckled Molded Mushroom" (20466), "Chilled Tundra Root" (20467). Produces "Hardened Mixture" (20473). Requires Pottery. The combine does not fail.
69. timorous/"Alrik Farsight", say "Take The Artifact". Gives "Crushed Pot" (20457).
70. felwitheb/"Farios Elianos", hand "Crushed Pot" (20457). Gives "Grocery List" (20458).
71. felwithea/"Merchant Nora", hand "Grocery List" (20458). Gives "Bag of Provisions" (20459).
72. felwitheb/"Farios Elianos", hand "Bag of Provisions" (20459). Gives "Receipt" (20474).
73. timorous/"Alrik Farsight", hand "Receipt" (20474). Gives "Ancient Pattern" (18960).
74. Kill citymist/"A Black Reaver". Spawns "A Black Reaver" (90004).
75. Loot "Jade Reaver" (5664) from "A Black Reaver".
76. 2 alternative loot source(s) also yield Jade Reaver (5664).
77. kaladimb/"Kinlo Strongarm", hand "Jade Reaver" (5664). Gives "Enchanted Clay" (20455).
78. Forage "Rose of Firiona" (12774) in `firiona`.
79. qrg/"Merdan Fleetfoot", hand "Rose of Firiona" (12774). Gives "Wood Painting" (20475).
80. frontiermtns/"A Human Skeleton", hand "Wood Painting" (20475). Gives "Silver Chained Locket" (20476).
81. qrg/"Niera Farbreeze", hand "Silver Chained Locket" (20476). Gives "Platinum Speckled Powder" (20456).
82. Combine in Pottery Wheel (21): "Ancient Pattern" (18960), "Enchanted Clay" (20455), "Platinum Speckled Powder" (20456). Produces "Runecrested Bowl" (20460). Requires Pottery. The combine does not fail.
83. misty/"Ella Foodcrafter", hand "Runecrested Bowl" (20460) + "Hardened Mixture" (20473). Gives "Softly Glowing Stone" (20462).
84. Common item: Spell: Resurrection (15392). Listed in 14 zones.
85. Hand "Spell: Resurrection" (15392) to karnor/"Spirit Of Venril Sathir". Spawns "Venril Sathir" (102126). Loot "Pulsing Green Stone" (20461) from "Venril Sathir".
86. firiona/"Foloal Stormforest", hand "Pulsing Green Stone" (20461) + "Softly Glowing Stone" (20462). Gives "Warmly Glowing Stone" (20468).
87. misty/"Ella Foodcrafter", hand "Warmly Glowing Stone" (20468). Gives "Elaborate Scimitar" (20440).
88. northkarana/"Xanuusus", hand "Elaborate Scimitar" (20440) + "Cleansed Spirit of Faydwer" (20697) + "Cleansed Spirit of Antonica" (20698) + "Cleansed Spirit of Kunark" (20699). Gives "Nature Walkers Scimitar" (20490).
89. eastkarana/"Althele", say "Out Of Balance". Sets `druid_epic` to `1`.
90. Spawns "A Bloodgill Forager" (85234) in `lakeofillomen` on enter.
91. Loot "Handful of Diseased Maiden's Hair" (62825) from "A Bloodgill Forager".
92. Common item: Tackle Box (17048). Listed in 11 zones.
93. Spawns "Ulthork Raider" (116608) in `eastwastes` on enter.
94. Loot "Carved Prexus Totem" (62821) from "Ulthork Raider".
95. cobaltscar/"Blumblum Swigwater", hand "Carved Prexus Totem" (62821). Gives "Small Trigger Fish" (62820).
96. Common item: Gutting Knife (62823). Listed in 4 zones.
97. Combine in "Tackle Box" (17048): "Small Trigger Fish" (62820), "Gutting Knife" (62823). Hands back "Gutting Knife" (62823). Produces "Soggy Maiden's Hair" (62824). Requires Fishing, trivial 20. The combine does not fail.
98. Spawns "spawn #Swamp Terror" (47208) in `feerrott` on enter.
99. Loot "Partially Digested Maiden's Hair" (62819) from "spawn #Swamp Terror".
100. Combine in "Waterproof Collection Bag" (62812): "Bag of Diseased Maiden's Hair" (62826), "Handful of Diseased Maiden's Hair" (62825), "Soggy Maiden's Hair" (62824), "Partially Digested Maiden's Hair" (62819). Produces "Sealed Collection Bag" (62813). The combine does not fail.
101. qrg/"Niera Farbreeze", hand "Sealed Collection Bag" (62813). Gives "Wash Cloth" (62847).
102. Spawns "spawn #Swamp Terror" (47208) in `feerrott` on enter.
103. Loot "Mangled Head" (62818) from "spawn #Swamp Terror".
104. Combine in "Wash Cloth" (62847): "Mangled Head" (62818). Produces "Wrapped Mangled Head" (62848). The combine does not fail.
105. qrg/"Niera Farbreeze", hand "Wrapped Mangled Head" (62848). Gives "Mangled Head" (62827).
106. qrg/"Niera Farbreeze", hand "Wrapped Mangled Head" (62848). Sets `druid_epic` to `2`.
107. poknowledge/"Pathfinder Arelat", say "Worth It". Requires `druid_epic` ==2. Gives "Fresh Awakenings vol. 1" (62839).
108. poknowledge/"Pathfinder Arelat", say "Worth It". Requires `druid_epic` ==2. Gives "Fresh Awakenings vol. 2" (62840).
109. poknowledge/"Pathfinder Arelat", say "Worth It". Requires `druid_epic` ==2. Gives "Fresh Awakenings vol. 3" (62841).
110. poknowledge/"Gravelady Beddia", hand "Fresh Awakenings vol. 1" (62839) + "Fresh Awakenings vol. 2" (62840) + "Fresh Awakenings vol. 3" (62841). Gives "Healing Plants" (62842).
111. qrg/"Niera Farbreeze", hand "Healing Plants" (62842). Sets `druid_epic` to `3`.
112. feerrott/"Corrupted Spirit", say "Show It". Requires `druid_epic` ==3. Gives "Disease Rune" (62837).
113. tox/"A Skeleton", say "I Will Do It". Triggers `tox/a skeleton#timer:pathback`.
114. Starts timer `pathbacktwo`.
115. Starts timer `pathbackthree`.
116. Starts timer `giveitem`.
117. tox/"A Skeleton", on timer giveitem. Gives "Animating Heads" (62828).
118. Combine in "Mangled Head" (62827): "Disease Rune" (62837), "Animating Heads" (62828). Produces "Runed Skull" (62838). The combine does not fail.
119. qrg/"Niera Farbreeze", hand "Healing Plants" (62842). Gives "Niera's Healing Notes" (62849).
120. qrg/"Niera Farbreeze", hand "Runed Skull" (62838) + "Niera's Healing Notes" (62849). Sets `druid_epic` to `4`.
121. qrg/"Niera Farbreeze", hand "Runed Skull" (62838) + "Niera's Healing Notes" (62849). Gives "Niera's Research Notes" (62843).
122. pojustice/"Great Bear", hand "Niera's Research Notes" (62843). Requires `druid_epic` ==4. Gives "Red Dogwood Seed" (62844).
123. qrg/"Corun Finisc", hand "Closed Medicine Bag" (62615). Gives "Sickly Mosquito Blood Sample" (62611).
124. Summon "Collapsible Fletching Kit" (17189) by casting "Unfold Fletching Kit".
125. qrg/"Corun Finisc", hand "Tuft of Sickly Maiden's Hair" (62811). Gives "Magical Sample Vial" (62657).
126. cazicthule/"A Sickly Mosquito", on event hp.
127. Starts timer `check`.
128. No quest step gives Planar Fletching Kit (17762). The dump lists it in poknowledge.
129. Common item: Whittling Knife (62608). Listed in 4 zones.
130. Forage "Fallen Tree Branch" (62652) in `dranik`.
131. Forage "Fallen Tree Branch" (62652) in `draniksscar`.
132. Combine in "Planar Fletching Kit" (17762): "Whittling Knife" (62608), "Fallen Tree Branch" (62652). Produces "Long Net Pole" (62607). Requires Fletching 100. Trivial at 15. The combine does not fail.
133. Spawns "A Phase Spider" (123190) in `necropolis` on event_combat.
134. Loot "Phase Spider Silk" (55303) from "A Phase Spider".
135. Forage "Pine Sap" (62650) in `jaggedpine`.
136. Forage "Pine Sap" (62650) in `nedaria`.
137. Forage "Pine Sap" (62650) in `qrg`.
138. Combine in "Planar Fletching Kit" (17762): "Phase Spider Silk" (55303), "Pine Sap" (62650). Produces "Phase Netting" (62651). Requires Fletching 100. Trivial at 15. The combine does not fail.
139. Combine in "Planar Fletching Kit" (17762): "Long Net Pole" (62607), "Phase Netting" (62651). Produces "Large Butterfly Net" (62646). Requires Fletching 100. Trivial at 15. The combine does not fail.
140. Equip "Large Butterfly Net" (62646) in primary slot.
141. cazicthule/"A Sickly Mosquito", on timer check. Gives "Captured Mosquito" (62642).
142. Combine in "Collapsible Fletching Kit" (17189): "Magical Sample Vial" (62657), "Captured Mosquito" (62642). Produces "Sickly Mosquito Blood Sample" (62611). Requires Fletching. The combine does not fail.
143. qrg/"Corun Finisc", hand "Closed Medicine Bag" (62615). Gives "Twitching Swordfish Blood Sample" (62612).
144. sirens/"A Twitching Swordfish", on event hp.
145. Starts timer `check`.
146. Equip "Large Butterfly Net" (62646) in primary slot.
147. sirens/"A Twitching Swordfish", on timer check. Gives "Captured Swordfish" (62643).
148. Combine in "Collapsible Fletching Kit" (17189): "Magical Sample Vial" (62657), "Captured Swordfish" (62643). Produces "Twitching Swordfish Blood Sample" (62612). Requires Fletching. The combine does not fail.
149. qrg/"Corun Finisc", hand "Closed Medicine Bag" (62615). Gives "Bloated Drogan Spider Blood Sample" (62613).
150. droga/"A Bloated Drogan Spider", on event hp.
151. Starts timer `check`.
152. Common item: Hinge Mold (12027). Listed in 25 zones.
153. Common item: Container Base Mold (12062). Listed in 14 zones.
154. Common item: Container Lid Mold (12069). Listed in 14 zones.
155. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
156. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `steamfont`.
157. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `tox`.
158. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `toxxulia`.
159. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
160. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). The combine does not fail.
161. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
162. Say "Tm Devrak Death" to rujd/"Rujd".
163. Spawns "spawn chest with Heavy Orcish Prison Key" (245241).
164. Loot "Pod of Water" (13044) from "spawn chest with Heavy Orcish Prison Key".
165. 6 alternative loot source(s) also yield Pod of Water (13044).
166. Forage "Pod of Water" (13044) in `ruja`.
167. Forage "Pod of Water" (13044) in `uqua`.
168. Forage "Pod of Water" (13044) in `yxtta`.
169. Combine in Brew Barrel (19): "Bottle of Aged Bloodwine" (51163), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aged Bloodwine" (51164). Requires Brewing, trivial 255.
170. Combine in Brew Barrel (19): "Bottle of Aldo's Bitter Ale" (75805), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aldo's Bitter Ale" (75811). Requires Brewing, trivial 15.
171. 17 other recipes also produce Bottle (16598).
172. Combine in Brew Barrel (19): "Pod of Water" (13044), "Bottle" (16598). Produces "Water Flask" (13006). Requires Brewing, trivial 21.
173. No quest step gives Small Brick of Steel (66168). The dump lists it in qrg.
174. qrg/"Qaelin Hailstorm", say "Need A Mark". Gives "Mark of Karana" (66172).
175. Combine in Forge (17): "Hinge Mold" (12027), "Container Base Mold" (12062), "Container Lid Mold" (12069), "Water Flask" (13006), "Small Brick of Steel" (66168), "Mark of Karana" (66172). Hands back "Mark of Karana" (66172). Produces "Surefall Fletching Kit" (66163). Requires Blacksmithing, trivial 163.
176. Loot "Smithy Hammer" (10489) from "Gliblixl Rocktok" in `bazaar`.
177. Forage "Golanda Nut" (62610) in `causeway`.
178. Forage "Golanda Nut" (62610) in `dranik`.
179. Forage "Golanda Nut" (62610) in `draniksscar`.
180. Forage "Golanda Nut" (62610) in `provinggrounds`.
181. Forage "Golanda Nut" (62610) in `riftseekers`.
182. Forage "Golanda Nut" (62610) in `wallofslaughter`.
183. Combine in "Surefall Fletching Kit" (66163): "Smithy Hammer" (10489), "Golanda Nut" (62610). Hands back "Smithy Hammer" (10489). Produces "Fibrous Rope" (62609). Requires Fletching 100. Trivial at 15. The combine does not fail.
184. Combine in "Surefall Fletching Kit" (66163): "Fibrous Rope" (62609). Produces "Eight-loop Lasso" (62648). Requires Fletching 100. Trivial at 15. The combine does not fail.
185. Equip "Eight-loop Lasso" (62648) in primary slot.
186. droga/"A Bloated Drogan Spider", on timer check. Gives "Captured Spider" (62644).
187. Combine in "Collapsible Fletching Kit" (17189): "Magical Sample Vial" (62657), "Captured Spider" (62644). Produces "Bloated Drogan Spider Blood Sample" (62613). Requires Fletching. The combine does not fail.
188. qrg/"Corun Finisc", hand "Closed Medicine Bag" (62615). Gives "Leprous Chokidai Blood Sample" (62614).
189. chardokb/"A Leprous Chokidai", on event hp.
190. Starts timer `check`.
191. Equip "Eight-loop Lasso" (62648) in primary slot.
192. chardokb/"A Leprous Chokidai", on timer check. Gives "Captured Chokidai" (62645).
193. Combine in "Collapsible Fletching Kit" (17189): "Magical Sample Vial" (62657), "Captured Chokidai" (62645). Produces "Leprous Chokidai Blood Sample" (62614). Requires Fletching. The combine does not fail.
194. Combine in "Borrowed Medicine Bag" (62605): "Sickly Mosquito Blood Sample" (62611), "Twitching Swordfish Blood Sample" (62612), "Bloated Drogan Spider Blood Sample" (62613), "Leprous Chokidai Blood Sample" (62614). Produces "Closed Medicine Bag" (62615). The combine does not fail.
195. qrg/"Corun Finisc", hand "Closed Medicine Bag" (62615). Gives "Borrowed Medicine Bag" (62605).
196. Unresolved cyclic prerequisite: `warrior_epic_gulak` ==1.
197. Unresolved cyclic prerequisite: `warrior_epic` ==17.
198. Ground spawn of "Frozen Pestle" (60323) in `iceclad`.
199. iceclad/"Fazzle Thumpkin", hand "Frozen Pestle" (60323). Sets `warrior_epic` to `18`.
200. Loot "Kreljnok's Muddled Rage" (60322) from "Possessed Brute" in `provinggrounds`.
201. draniksscar/"Korbuk Brimblade", hand "Kreljnok's Muddled Rage" (60322). Sets `warrior_epic` to `17`.
202. firiona/"Corfia Nultethen", say "Galuk Drek". Sets `warrior_epic_veksar` to `1`.
203. veksar/"Player", on enter. Sets `warrior_epic_gulak` to `1`.
204. Spawns "An Asteatotic Highborn" (109907) in `veksar` on enter.
205. Loot "Asteatotic Veksar Blood" (35100) from "An Asteatotic Highborn".
206. Spawns "A Neuralgic Huntress" (120136) in `westwastes` on enter.
207. Loot "Neuralgic Wyvern Blood" (72605) from "A Neuralgic Huntress".
208. Combine in "Borrowed Medicine Bag" (62605): "Asteatotic Veksar Blood" (35100), "Neuralgic Wyvern Blood" (72605), "Sickly Mosquito Blood Sample" (62611), "Twitching Swordfish Blood Sample" (62612), "Leprous Chokidai Blood Sample" (62614), "Bloated Drogan Spider Blood Sample" (62613). Produces "Full Medicine Bag" (62616). The combine does not fail.
209. qrg/"Corun Finisc", hand "Full Medicine Bag" (62616). Gives "Corun's Notes" (62617).
210. freeportwest/"Shana Liskia", hand "Corun's Notes" (62617). Sets `ranger_epic` to `2`.
211. bloodfields/"Ranger 1 5", say "Hail". Requires `ranger_epic` ==2. Requires `ranger_bloodfield_chest` unset. Gives "Grinbik's Blessing" (62622).

### "Red Dogwood Seed" (62844)

1. Forage "Sickly Maiden's Hair" (62810) in `rathemtn`.
2. eastkarana/"Althele", hand "Sickly Maiden's Hair" (62810). Gives "Tuft of Sickly Maiden's Hair" (62811).
3. qrg/"Niera Farbreeze", hand "Tuft of Sickly Maiden's Hair" (62811). Gives "Waterproof Collection Bag" (62812).
4. Say "King Timer" to frontiermtns/"Druid 1 5".
5. Spawns npc 92202 (92202).
6. Loot "Bag of Diseased Maiden's Hair" (62826) from npc 92202.
7. burningwood/"Telin Darkforest", say "Action". Gives "Worn Note" (20472).
8. gfaydark/"Faelin Bloodbriar", hand "Worn Note" (20472). Gives "Faelin's Ring" (20446).
9. kithicor/"Giz X-Tin", hand "Faelin's Ring" (20446). Gives "Dark Metal Coin" (20447).
10. burningwood/"Telin Darkforest", hand "Dark Metal Coin" (20447). Gives "Worn Dark Metal Coin" (20448).
11. eastkarana/"Althele", hand "Worn Dark Metal Coin" (20448). Gives "Braided Grass Amulet" (20450).
12. eastkarana/"Sionae", hand "Braided Grass Amulet" (20450). Gives "Frayed Braided Grass Amulet" (20451).
13. eastkarana/"Teloa", hand "Frayed Braided Grass Amulet" (20451). Triggers `eastkarana/althele#signal:1`.
14. Starts timer `attack`.
15. Spawns "Corruptor" (15153) after `eastkarana/althele#timer:attack`.
16. Loot "Fleshbound Tome" (20452) from "Corruptor".
17. eastkarana/"Althele", hand "Fleshbound Tome" (20452). Gives "Earth Stained Note" (18959).
18. misty/"Ella Foodcrafter", hand "Earth Stained Note" (18959). Sets `shiny_tin_bowl` to `1`.
19. misty/"Ella Foodcrafter", say "Two Tasks". Requires `shiny_tin_bowl` set. Gives "Shiny Tin Bowl" (17860).
20. Hand "Shiny Tin Bowl" (17860) to hole/"Jaeil The Wretched". Spawns "Jaeil the Insane" (39154). Loot "Soulbound Hammer" (20478) from "Jaeil the Insane".
21. erudnint/"Mairee Silentone", hand "Soulbound Hammer" (20478). Gives "Dwarven Smiths Hammer" (20479).
22. Kill airplane/"An Essence Carrier". Spawns "An Essence Tamer" (71071).
23. Loot "Swirling Sphere of Color" (20494) from "An Essence Tamer".
24. erudnint/"Mairee Silentone", hand "Dwarven Smiths Hammer" (20479) + "Swirling Sphere of Color" (20494). Gives "Hammer of the Ancients" (20485).
25. kaladimb/"Kinlo Strongarm", hand "Hammer of the Ancients" (20485). Gives "Small bit of Mithril Ore" (20482).
26. kaladimb/"Kinlo Strongarm", hand "Small bit of Mithril Ore" (20482). Gives "Refined Mithril Blade" (20483).
27. Encounter starts when NPC 186201 spawns in `hateplaneb`.
28. Starts timer `popinny`.
29. Kill NPC 186158.
30. Starts timer `text`.
31. Starts timer `text2`.
32. Starts timer `spawninny`.
33. Spawns "Innoruuk" (186107) after `hateplaneb/inny#timer:spawninny`.
34. Loot "Shattered Emerald of Corruption" (20484) from "Innoruuk".
35. 1 alternative loot source(s) also yield Shattered Emerald of Corruption (20484).
36. northkarana/"Xanuusus", hand "Refined Mithril Blade" (20483) + "Shattered Emerald of Corruption" (20484). Gives "Earthcaller" (20488).
37. eastkarana/"Althele", say "Hail". Sets `ranger_epic` to `1`.
38. Loot "Froglok Essence" (20696) from "Ulump Pujluk" in `swampofnohope`.
39. Kill emeraldjungle/"Tainted Gorilla". Spawns "Corrupted Gorilla" (94140).
40. Loot "Green Tree Bark" (20686) from "Corrupted Gorilla".
41. Kill lakeofillomen/"Tainted Barracuda". Spawns "Corrupted Barracuda" (85224).
42. Loot "Pure Lakewater" (20685) from "Corrupted Barracuda".
43. Hand "Froglok Essence" (20696) to timorous/"Dolgin Codslayer". Spawns "Faydedar" (96073). Loot "Pod of Seawater" (20687) from "Faydedar".
44. overthere/"Nekexin Virulence", hand "Pure Lakewater" (20685) + "Green Tree Bark" (20686) + "Pod of Seawater" (20687) + "Froglok Essence" (20696). Gives "Cleansed Spirit of Kunark" (20699).
45. Kill kedge/"Tainted Seahorse". Spawns "Corrupted Seahorse" (64050).
46. Loot "Kedge Cave Crystals" (20691) from "Corrupted Seahorse".
47. Kill oceanoftears/"Tainted Seafury Cyclops". Spawns "Corrupted Seafury Cyclops" (69142).
48. Loot "Ocean of Tears Seavines" (20692) from "Corrupted Seafury Cyclops".
49. 1 alternative loot source(s) also yield Ocean of Tears Seavines (20692).
50. Kill lfaydark/"Tainted Brownie". Spawns "Corrupted Brownie" (57117).
51. Loot "Green Heartwood Branch" (20693) from "Corrupted Brownie".
52. lfaydark/"Pained Unicorn", hand "Kedge Cave Crystals" (20691) + "Ocean of Tears Seavines" (20692) + "Green Heartwood Branch" (20693). Gives "Gleaming Unicorn Horn" (20694).
53. akanon/"Silox Azrix", hand "Gleaming Unicorn Horn" (20694). Gives "Cleansed Spirit of Faydwer" (20697).
54. Loot "Ring of the Ancients" (12268) from "The Fabled Ancient Cyclops" in `sro`.
55. Loot "Ring of the Ancients" (12268) from "An Ancient Cyclops".
56. Loot "Ring of the Ancients" (12268) from "An Ancient Cyclops" in `oot`.
57. Loot "Ring of the Ancients" (12268) from "An Ancient Cyclops" in `sro`.
58. Kill rathemtn/"Ytyrs The Reborn". Spawns "Ytyrs Reborn" (50346).
59. Loot "Shadowed Rapier" (7100) from "Ytyrs Reborn".
60. rathemtn/"Hasten Bootstrutter", hand "Shadowed Rapier" (7100) + "Ring of the Ancients" (12268). Gives "Journeyman's Boots" (2300).
61. northkarana/"Triathalon Token", hand "Journeyman's Boots" (2300). Gives "Warm Pulsing Treant Heart" (20695).
62. southkarana/"Yeka Ias", hand "Warm Pulsing Treant Heart" (20695). Gives "Cleansed Spirit of Antonica" (20698).
63. Forage "Ripened Heartfruit" (20464) in `gfaydark`.
64. Forage "Sweetened Mudroot" (20465) in `misty`.
65. Forage "Sweetened Mudroot" (20465) in `mistythicket`.
66. Forage "Speckled Molded Mushroom" (20466) in `innothule`.
67. Forage "Chilled Tundra Root" (20467) in `everfrost`.
68. Combine in "Shiny Tin Bowl" (17860): "Ripened Heartfruit" (20464), "Sweetened Mudroot" (20465), "Speckled Molded Mushroom" (20466), "Chilled Tundra Root" (20467). Produces "Hardened Mixture" (20473). Requires Pottery. The combine does not fail.
69. timorous/"Alrik Farsight", say "Take The Artifact". Gives "Crushed Pot" (20457).
70. felwitheb/"Farios Elianos", hand "Crushed Pot" (20457). Gives "Grocery List" (20458).
71. felwithea/"Merchant Nora", hand "Grocery List" (20458). Gives "Bag of Provisions" (20459).
72. felwitheb/"Farios Elianos", hand "Bag of Provisions" (20459). Gives "Receipt" (20474).
73. timorous/"Alrik Farsight", hand "Receipt" (20474). Gives "Ancient Pattern" (18960).
74. Kill citymist/"A Black Reaver". Spawns "A Black Reaver" (90004).
75. Loot "Jade Reaver" (5664) from "A Black Reaver".
76. 2 alternative loot source(s) also yield Jade Reaver (5664).
77. kaladimb/"Kinlo Strongarm", hand "Jade Reaver" (5664). Gives "Enchanted Clay" (20455).
78. Forage "Rose of Firiona" (12774) in `firiona`.
79. qrg/"Merdan Fleetfoot", hand "Rose of Firiona" (12774). Gives "Wood Painting" (20475).
80. frontiermtns/"A Human Skeleton", hand "Wood Painting" (20475). Gives "Silver Chained Locket" (20476).
81. qrg/"Niera Farbreeze", hand "Silver Chained Locket" (20476). Gives "Platinum Speckled Powder" (20456).
82. Combine in Pottery Wheel (21): "Ancient Pattern" (18960), "Enchanted Clay" (20455), "Platinum Speckled Powder" (20456). Produces "Runecrested Bowl" (20460). Requires Pottery. The combine does not fail.
83. misty/"Ella Foodcrafter", hand "Runecrested Bowl" (20460) + "Hardened Mixture" (20473). Gives "Softly Glowing Stone" (20462).
84. Common item: Spell: Resurrection (15392). Listed in 14 zones.
85. Hand "Spell: Resurrection" (15392) to karnor/"Spirit Of Venril Sathir". Spawns "Venril Sathir" (102126). Loot "Pulsing Green Stone" (20461) from "Venril Sathir".
86. firiona/"Foloal Stormforest", hand "Pulsing Green Stone" (20461) + "Softly Glowing Stone" (20462). Gives "Warmly Glowing Stone" (20468).
87. misty/"Ella Foodcrafter", hand "Warmly Glowing Stone" (20468). Gives "Elaborate Scimitar" (20440).
88. northkarana/"Xanuusus", hand "Elaborate Scimitar" (20440) + "Cleansed Spirit of Faydwer" (20697) + "Cleansed Spirit of Antonica" (20698) + "Cleansed Spirit of Kunark" (20699). Gives "Nature Walkers Scimitar" (20490).
89. eastkarana/"Althele", say "Out Of Balance". Sets `druid_epic` to `1`.
90. Spawns "A Bloodgill Forager" (85234) in `lakeofillomen` on enter.
91. Loot "Handful of Diseased Maiden's Hair" (62825) from "A Bloodgill Forager".
92. Common item: Tackle Box (17048). Listed in 11 zones.
93. Spawns "Ulthork Raider" (116608) in `eastwastes` on enter.
94. Loot "Carved Prexus Totem" (62821) from "Ulthork Raider".
95. cobaltscar/"Blumblum Swigwater", hand "Carved Prexus Totem" (62821). Gives "Small Trigger Fish" (62820).
96. Common item: Gutting Knife (62823). Listed in 4 zones.
97. Combine in "Tackle Box" (17048): "Small Trigger Fish" (62820), "Gutting Knife" (62823). Hands back "Gutting Knife" (62823). Produces "Soggy Maiden's Hair" (62824). Requires Fishing, trivial 20. The combine does not fail.
98. Spawns "spawn #Swamp Terror" (47208) in `feerrott` on enter.
99. Loot "Partially Digested Maiden's Hair" (62819) from "spawn #Swamp Terror".
100. Combine in "Waterproof Collection Bag" (62812): "Bag of Diseased Maiden's Hair" (62826), "Handful of Diseased Maiden's Hair" (62825), "Soggy Maiden's Hair" (62824), "Partially Digested Maiden's Hair" (62819). Produces "Sealed Collection Bag" (62813). The combine does not fail.
101. qrg/"Niera Farbreeze", hand "Sealed Collection Bag" (62813). Gives "Wash Cloth" (62847).
102. Spawns "spawn #Swamp Terror" (47208) in `feerrott` on enter.
103. Loot "Mangled Head" (62818) from "spawn #Swamp Terror".
104. Combine in "Wash Cloth" (62847): "Mangled Head" (62818). Produces "Wrapped Mangled Head" (62848). The combine does not fail.
105. qrg/"Niera Farbreeze", hand "Wrapped Mangled Head" (62848). Gives "Mangled Head" (62827).
106. qrg/"Niera Farbreeze", hand "Wrapped Mangled Head" (62848). Sets `druid_epic` to `2`.
107. poknowledge/"Pathfinder Arelat", say "Worth It". Requires `druid_epic` ==2. Gives "Fresh Awakenings vol. 1" (62839).
108. poknowledge/"Pathfinder Arelat", say "Worth It". Requires `druid_epic` ==2. Gives "Fresh Awakenings vol. 2" (62840).
109. poknowledge/"Pathfinder Arelat", say "Worth It". Requires `druid_epic` ==2. Gives "Fresh Awakenings vol. 3" (62841).
110. poknowledge/"Gravelady Beddia", hand "Fresh Awakenings vol. 1" (62839) + "Fresh Awakenings vol. 2" (62840) + "Fresh Awakenings vol. 3" (62841). Gives "Healing Plants" (62842).
111. qrg/"Niera Farbreeze", hand "Healing Plants" (62842). Sets `druid_epic` to `3`.
112. feerrott/"Corrupted Spirit", say "Show It". Requires `druid_epic` ==3. Gives "Disease Rune" (62837).
113. tox/"A Skeleton", say "I Will Do It". Triggers `tox/a skeleton#timer:pathback`.
114. Starts timer `pathbacktwo`.
115. Starts timer `pathbackthree`.
116. Starts timer `giveitem`.
117. tox/"A Skeleton", on timer giveitem. Gives "Animating Heads" (62828).
118. Combine in "Mangled Head" (62827): "Disease Rune" (62837), "Animating Heads" (62828). Produces "Runed Skull" (62838). The combine does not fail.
119. qrg/"Niera Farbreeze", hand "Healing Plants" (62842). Gives "Niera's Healing Notes" (62849).
120. qrg/"Niera Farbreeze", hand "Runed Skull" (62838) + "Niera's Healing Notes" (62849). Sets `druid_epic` to `4`.
121. qrg/"Niera Farbreeze", hand "Runed Skull" (62838) + "Niera's Healing Notes" (62849). Gives "Niera's Research Notes" (62843).
122. pojustice/"Great Bear", hand "Niera's Research Notes" (62843). Requires `druid_epic` ==4. Gives "Red Dogwood Seed" (62844).

### "Wind-blessed Heartwood" (62626)

1. global/"Global Player", combine recipe 13412. Sets `ranger_epic` to `3`.
2. jaggedpine/"Red Dogwood Treant", say "Hail". Requires `ranger_epic` ==3. Gives "Red Dogwood Heartwood" (62623).
3. dranik/"Ranger 1 5", hand "Red Dogwood Heartwood" (62623). Requires `ranger_dranik_chest` unset. Gives "Wind-blessed Heartwood" (62626).

### "Block of Purest Silver" (62625)

1. global/"Global Player", combine recipe 13412. Sets `ranger_epic` to `3`.
2. jaggedpine/"Red Dogwood Treant", say "Hail". Requires `ranger_epic` ==3. Gives "Spring Dogwood Seed" (62624).
3. qrg/"Corun Finisc", hand "Spring Dogwood Seed" (62624). Gives "Block of Purest Silver" (62625).

### "Closed Sample Cloth" (62641)

1. nedaria/"Targen Stonefall", say "Native Stones". Sets `ranger_epic15_pre` to `1`.
2. Forage "Blasted Stone" (62601) in `bloodfields`.
3. nedaria/"Targen Stonefall", hand "Blasted Stone" (62601). Sets `ranger_epic15_pre` to `2`.
4. nedaria/"Targen Stonefall", say "Bloodfields". Requires `ranger_epic15_pre` ==2. Gives "Sample Cloth" (62640).
5. nedaria/"Targen Stonefall", say "Bloodfields". Requires `ranger_epic15_pre` ==2. Gives "Targen's Emulsion" (62639).
6. nedaria/"Targen Stonefall", say "Odus". Sets `ranger_epic15_pre` to `3`.
7. Spawns "Stone Collector" (39168) in `hole` on enter.
8. Loot "Dusty Stone" (62653) from "Stone Collector".
9. Combine in "Sample Cloth" (62640): "Targen's Emulsion" (62639), "Dusty Stone" (62653). Produces "Rock of Odus" (62606). The combine does not fail.
10. nedaria/"Targen Stonefall", hand "Blasted Stone" (62601). Requires `ranger_epic15_pre` ==1. Gives "Washed Blasted Stone" (62602).
11. Combine in "Sample Cloth" (62640): "Rock of Odus" (62606), "Washed Blasted Stone" (62602). Produces "Closed Sample Cloth" (62641). The combine does not fail.

### "Polished Blasted Stone" (62603)

1. nedaria/"Targen Stonefall", say "Native Stones". Sets `ranger_epic15_pre` to `1`.
2. Forage "Blasted Stone" (62601) in `bloodfields`.
3. nedaria/"Targen Stonefall", hand "Blasted Stone" (62601). Sets `ranger_epic15_pre` to `2`.
4. nedaria/"Targen Stonefall", say "Odus". Sets `ranger_epic15_pre` to `3`.
5. Spawns "Stone Collector" (39168) in `hole` on enter.
6. Loot "Dusty Stone" (62653) from "Stone Collector".
7. hole/"Player", on loot. Sets `ranger_epic15_pre` to `4`.
8. nedaria/"Targen Stonefall", say "Bloodfields". Requires `ranger_epic15_pre` ==2. Gives "Sample Cloth" (62640).
9. nedaria/"Targen Stonefall", say "Bloodfields". Requires `ranger_epic15_pre` ==2. Gives "Targen's Emulsion" (62639).
10. Combine in "Sample Cloth" (62640): "Targen's Emulsion" (62639), "Dusty Stone" (62653). Produces "Rock of Odus" (62606). The combine does not fail.
11. nedaria/"Targen Stonefall", hand "Blasted Stone" (62601). Requires `ranger_epic15_pre` ==1. Gives "Washed Blasted Stone" (62602).
12. Combine in "Sample Cloth" (62640): "Rock of Odus" (62606), "Washed Blasted Stone" (62602). Produces "Closed Sample Cloth" (62641). The combine does not fail.
13. nedaria/"Targen Stonefall", hand "Closed Sample Cloth" (62641). Sets `ranger_epic15_pre` to `5`.
14. nedaria/"Targen Stonefall", say "Impurities". Requires `ranger_epic15_pre` ==5. Gives "Polished Blasted Stone" (62603).

### "Stone of Winde" (62604)

1. nedaria/"Targen Stonefall", say "Native Stones". Sets `ranger_epic15_pre` to `1`.
2. Forage "Blasted Stone" (62601) in `bloodfields`.
3. nedaria/"Targen Stonefall", hand "Blasted Stone" (62601). Sets `ranger_epic15_pre` to `2`.
4. nedaria/"Targen Stonefall", say "Odus". Sets `ranger_epic15_pre` to `3`.
5. Spawns "Stone Collector" (39168) in `hole` on enter.
6. Loot "Dusty Stone" (62653) from "Stone Collector".
7. hole/"Player", on loot. Sets `ranger_epic15_pre` to `4`.
8. nedaria/"Targen Stonefall", say "Bloodfields". Requires `ranger_epic15_pre` ==2. Gives "Sample Cloth" (62640).
9. nedaria/"Targen Stonefall", say "Bloodfields". Requires `ranger_epic15_pre` ==2. Gives "Targen's Emulsion" (62639).
10. Combine in "Sample Cloth" (62640): "Targen's Emulsion" (62639), "Dusty Stone" (62653). Produces "Rock of Odus" (62606). The combine does not fail.
11. nedaria/"Targen Stonefall", hand "Blasted Stone" (62601). Requires `ranger_epic15_pre` ==1. Gives "Washed Blasted Stone" (62602).
12. Combine in "Sample Cloth" (62640): "Rock of Odus" (62606), "Washed Blasted Stone" (62602). Produces "Closed Sample Cloth" (62641). The combine does not fail.
13. nedaria/"Targen Stonefall", hand "Closed Sample Cloth" (62641). Sets `ranger_epic15_pre` to `5`.
14. nedaria/"Targen Stonefall", say "Impurities". Sets `ranger_epic15_pre` to `6`.
15. nedaria/"Targen Stonefall", say "Impurities". Requires `ranger_epic15_pre` ==5. Gives "Polished Blasted Stone" (62603).
16. northkarana/"Xanuusus", hand "Polished Blasted Stone" (62603). Sets `ranger_epic15_pre` to `7`.
17. Loot "Taskmaster's Cutlass" (62631) from "Taskmaster Waggad Brokenskull" in `torgiran`.
18. torgiran/"Player", on loot. Sets `ranger_epic15_pre` to `8`.
19. northkarana/"Xanuusus", hand "Polished Blasted Stone" (62603). Requires `ranger_epic15_pre` ==6. Gives "Poem of the Storms" (62632).
20. misty/"A Tired Farmer", hand "Poem of the Storms" (62632). Gives "Tear-stained Poem of the Storms" (62633).
21. Say "Ready" to northkarana/"Xanuusus".
22. Spawns "A Tainted Beast" (13131).
23. Loot "Stone of Winde" (62604) from "A Tainted Beast".

### "Sound Capture Jar" (62637)

1. nedaria/"Targen Stonefall", say "Native Stones". Sets `ranger_epic15_pre` to `1`.
2. Forage "Blasted Stone" (62601) in `bloodfields`.
3. nedaria/"Targen Stonefall", hand "Blasted Stone" (62601). Sets `ranger_epic15_pre` to `2`.
4. nedaria/"Targen Stonefall", say "Odus". Sets `ranger_epic15_pre` to `3`.
5. Spawns "Stone Collector" (39168) in `hole` on enter.
6. Loot "Dusty Stone" (62653) from "Stone Collector".
7. hole/"Player", on loot. Sets `ranger_epic15_pre` to `4`.
8. nedaria/"Targen Stonefall", say "Bloodfields". Requires `ranger_epic15_pre` ==2. Gives "Sample Cloth" (62640).
9. nedaria/"Targen Stonefall", say "Bloodfields". Requires `ranger_epic15_pre` ==2. Gives "Targen's Emulsion" (62639).
10. Combine in "Sample Cloth" (62640): "Targen's Emulsion" (62639), "Dusty Stone" (62653). Produces "Rock of Odus" (62606). The combine does not fail.
11. nedaria/"Targen Stonefall", hand "Blasted Stone" (62601). Requires `ranger_epic15_pre` ==1. Gives "Washed Blasted Stone" (62602).
12. Combine in "Sample Cloth" (62640): "Rock of Odus" (62606), "Washed Blasted Stone" (62602). Produces "Closed Sample Cloth" (62641). The combine does not fail.
13. nedaria/"Targen Stonefall", hand "Closed Sample Cloth" (62641). Sets `ranger_epic15_pre` to `5`.
14. nedaria/"Targen Stonefall", say "Impurities". Sets `ranger_epic15_pre` to `6`.
15. nedaria/"Targen Stonefall", say "Impurities". Requires `ranger_epic15_pre` ==5. Gives "Polished Blasted Stone" (62603).
16. northkarana/"Xanuusus", hand "Polished Blasted Stone" (62603). Sets `ranger_epic15_pre` to `7`.
17. Loot "Taskmaster's Cutlass" (62631) from "Taskmaster Waggad Brokenskull" in `torgiran`.
18. torgiran/"Player", on loot. Sets `ranger_epic15_pre` to `8`.
19. northkarana/"Xanuusus", hand "Polished Blasted Stone" (62603). Requires `ranger_epic15_pre` ==6. Gives "Poem of the Storms" (62632).
20. misty/"A Tired Farmer", hand "Poem of the Storms" (62632). Gives "Tear-stained Poem of the Storms" (62633).
21. Say "Ready" to northkarana/"Xanuusus".
22. Spawns "A Tainted Beast" (13131).
23. Loot "Stone of Winde" (62604) from "A Tainted Beast".
24. northkarana/"Xanuusus", hand "Stone of Winde" (62604). Sets `ranger_epic15_pre` to `9`.
25. steamfont/"Godbin Strumharp", hand platinum:30. Requires `ranger_epic15_pre` ==9. Gives "Sound Capture Jar" (62637).

### "Swiftwind" (20487)

1. burningwood/"Telin Darkforest", say "Action". Gives "Worn Note" (20472).
2. gfaydark/"Faelin Bloodbriar", hand "Worn Note" (20472). Gives "Faelin's Ring" (20446).
3. kithicor/"Giz X-Tin", hand "Faelin's Ring" (20446). Gives "Dark Metal Coin" (20447).
4. burningwood/"Telin Darkforest", hand "Dark Metal Coin" (20447). Gives "Worn Dark Metal Coin" (20448).
5. eastkarana/"Althele", hand "Worn Dark Metal Coin" (20448). Gives "Braided Grass Amulet" (20450).
6. eastkarana/"Sionae", hand "Braided Grass Amulet" (20450). Gives "Frayed Braided Grass Amulet" (20451).
7. eastkarana/"Teloa", hand "Frayed Braided Grass Amulet" (20451). Triggers `eastkarana/althele#signal:1`.
8. Starts timer `attack`.
9. Spawns "Corruptor" (15153) after `eastkarana/althele#timer:attack`.
10. Loot "Fleshbound Tome" (20452) from "Corruptor".
11. eastkarana/"Althele", hand "Fleshbound Tome" (20452). Gives "Earth Stained Note" (18959).
12. misty/"Ella Foodcrafter", hand "Earth Stained Note" (18959). Sets `shiny_tin_bowl` to `1`.
13. misty/"Ella Foodcrafter", say "Two Tasks". Requires `shiny_tin_bowl` set. Gives "Shiny Tin Bowl" (17860).
14. Forage "Ripened Heartfruit" (20464) in `gfaydark`.
15. Forage "Sweetened Mudroot" (20465) in `misty`.
16. Forage "Sweetened Mudroot" (20465) in `mistythicket`.
17. Forage "Speckled Molded Mushroom" (20466) in `innothule`.
18. Forage "Chilled Tundra Root" (20467) in `everfrost`.
19. Combine in "Shiny Tin Bowl" (17860): "Ripened Heartfruit" (20464), "Sweetened Mudroot" (20465), "Speckled Molded Mushroom" (20466), "Chilled Tundra Root" (20467). Produces "Hardened Mixture" (20473). Requires Pottery. The combine does not fail.
20. timorous/"Alrik Farsight", say "Take The Artifact". Gives "Crushed Pot" (20457).
21. felwitheb/"Farios Elianos", hand "Crushed Pot" (20457). Gives "Grocery List" (20458).
22. felwithea/"Merchant Nora", hand "Grocery List" (20458). Gives "Bag of Provisions" (20459).
23. felwitheb/"Farios Elianos", hand "Bag of Provisions" (20459). Gives "Receipt" (20474).
24. timorous/"Alrik Farsight", hand "Receipt" (20474). Gives "Ancient Pattern" (18960).
25. Kill citymist/"A Black Reaver". Spawns "A Black Reaver" (90004).
26. Loot "Jade Reaver" (5664) from "A Black Reaver".
27. 2 alternative loot source(s) also yield Jade Reaver (5664).
28. kaladimb/"Kinlo Strongarm", hand "Jade Reaver" (5664). Gives "Enchanted Clay" (20455).
29. Forage "Rose of Firiona" (12774) in `firiona`.
30. qrg/"Merdan Fleetfoot", hand "Rose of Firiona" (12774). Gives "Wood Painting" (20475).
31. frontiermtns/"A Human Skeleton", hand "Wood Painting" (20475). Gives "Silver Chained Locket" (20476).
32. qrg/"Niera Farbreeze", hand "Silver Chained Locket" (20476). Gives "Platinum Speckled Powder" (20456).
33. Combine in Pottery Wheel (21): "Ancient Pattern" (18960), "Enchanted Clay" (20455), "Platinum Speckled Powder" (20456). Produces "Runecrested Bowl" (20460). Requires Pottery. The combine does not fail.
34. misty/"Ella Foodcrafter", hand "Runecrested Bowl" (20460) + "Hardened Mixture" (20473). Gives "Softly Glowing Stone" (20462).
35. Common item: Spell: Resurrection (15392). Listed in 14 zones.
36. Hand "Spell: Resurrection" (15392) to karnor/"Spirit Of Venril Sathir". Spawns "Venril Sathir" (102126). Loot "Pulsing Green Stone" (20461) from "Venril Sathir".
37. firiona/"Foloal Stormforest", hand "Pulsing Green Stone" (20461) + "Softly Glowing Stone" (20462). Gives "Warmly Glowing Stone" (20468).
38. burningwood/"Telin Darkforest", hand "Warmly Glowing Stone" (20468). Gives "Ancient Longsword" (20477).
39. kaladimb/"Usbak The Old", hand "Ancient Longsword" (20477). Gives "Refined Ancient Sword" (20481).
40. burningwood/"Faelin Bloodbriar", hand "Refined Ancient Sword" (20481). Gives "Swiftwind" (20487).

### "Heated Loadstone" (62628)

1. global/"Global Player", combine recipe 13413. Sets `ranger_epic` to `5`.
2. nedaria/"A Wayfarers Brotherhood Officer", say "Hail". Sets `ranger_epic` to `6`.
3. causeway/"Siflu", say "Adventurers". Requires `ranger_epic` ==6. Gives "Heated Loadstone" (62628).

### "Elemental Ice Spirit Cage" (62647)

1. Loot "Crooked Cage" (32042) from "a Broken Skull bruiser" in `torgiran`.
2. burningwood/"Telin Darkforest", say "Action". Gives "Worn Note" (20472).
3. gfaydark/"Faelin Bloodbriar", hand "Worn Note" (20472). Gives "Faelin's Ring" (20446).
4. kithicor/"Giz X-Tin", hand "Faelin's Ring" (20446). Gives "Dark Metal Coin" (20447).
5. burningwood/"Telin Darkforest", hand "Dark Metal Coin" (20447). Gives "Worn Dark Metal Coin" (20448).
6. eastkarana/"Althele", hand "Worn Dark Metal Coin" (20448). Gives "Braided Grass Amulet" (20450).
7. eastkarana/"Sionae", hand "Braided Grass Amulet" (20450). Gives "Frayed Braided Grass Amulet" (20451).
8. eastkarana/"Teloa", hand "Frayed Braided Grass Amulet" (20451). Triggers `eastkarana/althele#signal:1`.
9. Starts timer `attack`.
10. Spawns "Corruptor" (15153) after `eastkarana/althele#timer:attack`.
11. Loot "Fleshbound Tome" (20452) from "Corruptor".
12. eastkarana/"Althele", hand "Fleshbound Tome" (20452). Gives "Earth Stained Note" (18959).
13. misty/"Ella Foodcrafter", hand "Earth Stained Note" (18959). Sets `shiny_tin_bowl` to `1`.
14. misty/"Ella Foodcrafter", say "Two Tasks". Requires `shiny_tin_bowl` set. Gives "Shiny Tin Bowl" (17860).
15. Hand "Shiny Tin Bowl" (17860) to hole/"Jaeil The Wretched". Spawns "Jaeil the Insane" (39154). Loot "Soulbound Hammer" (20478) from "Jaeil the Insane".
16. erudnint/"Mairee Silentone", hand "Soulbound Hammer" (20478). Gives "Dwarven Smiths Hammer" (20479).
17. Kill airplane/"An Essence Carrier". Spawns "An Essence Tamer" (71071).
18. Loot "Swirling Sphere of Color" (20494) from "An Essence Tamer".
19. erudnint/"Mairee Silentone", hand "Dwarven Smiths Hammer" (20479) + "Swirling Sphere of Color" (20494). Gives "Hammer of the Ancients" (20485).
20. kaladimb/"Kinlo Strongarm", hand "Hammer of the Ancients" (20485). Gives "Small bit of Mithril Ore" (20482).
21. kaladimb/"Kinlo Strongarm", hand "Small bit of Mithril Ore" (20482). Gives "Refined Mithril Blade" (20483).
22. Encounter starts when NPC 186201 spawns in `hateplaneb`.
23. Starts timer `popinny`.
24. Kill NPC 186158.
25. Starts timer `text`.
26. Starts timer `text2`.
27. Starts timer `spawninny`.
28. Spawns "Innoruuk" (186107) after `hateplaneb/inny#timer:spawninny`.
29. Loot "Shattered Emerald of Corruption" (20484) from "Innoruuk".
30. 1 alternative loot source(s) also yield Shattered Emerald of Corruption (20484).
31. northkarana/"Xanuusus", hand "Refined Mithril Blade" (20483) + "Shattered Emerald of Corruption" (20484). Gives "Earthcaller" (20488).
32. Forage "Ripened Heartfruit" (20464) in `gfaydark`.
33. Forage "Sweetened Mudroot" (20465) in `misty`.
34. Forage "Sweetened Mudroot" (20465) in `mistythicket`.
35. Forage "Speckled Molded Mushroom" (20466) in `innothule`.
36. Forage "Chilled Tundra Root" (20467) in `everfrost`.
37. Combine in "Shiny Tin Bowl" (17860): "Ripened Heartfruit" (20464), "Sweetened Mudroot" (20465), "Speckled Molded Mushroom" (20466), "Chilled Tundra Root" (20467). Produces "Hardened Mixture" (20473). Requires Pottery. The combine does not fail.
38. timorous/"Alrik Farsight", say "Take The Artifact". Gives "Crushed Pot" (20457).
39. felwitheb/"Farios Elianos", hand "Crushed Pot" (20457). Gives "Grocery List" (20458).
40. felwithea/"Merchant Nora", hand "Grocery List" (20458). Gives "Bag of Provisions" (20459).
41. felwitheb/"Farios Elianos", hand "Bag of Provisions" (20459). Gives "Receipt" (20474).
42. timorous/"Alrik Farsight", hand "Receipt" (20474). Gives "Ancient Pattern" (18960).
43. Kill citymist/"A Black Reaver". Spawns "A Black Reaver" (90004).
44. Loot "Jade Reaver" (5664) from "A Black Reaver".
45. 2 alternative loot source(s) also yield Jade Reaver (5664).
46. kaladimb/"Kinlo Strongarm", hand "Jade Reaver" (5664). Gives "Enchanted Clay" (20455).
47. Forage "Rose of Firiona" (12774) in `firiona`.
48. qrg/"Merdan Fleetfoot", hand "Rose of Firiona" (12774). Gives "Wood Painting" (20475).
49. frontiermtns/"A Human Skeleton", hand "Wood Painting" (20475). Gives "Silver Chained Locket" (20476).
50. qrg/"Niera Farbreeze", hand "Silver Chained Locket" (20476). Gives "Platinum Speckled Powder" (20456).
51. Combine in Pottery Wheel (21): "Ancient Pattern" (18960), "Enchanted Clay" (20455), "Platinum Speckled Powder" (20456). Produces "Runecrested Bowl" (20460). Requires Pottery. The combine does not fail.
52. misty/"Ella Foodcrafter", hand "Runecrested Bowl" (20460) + "Hardened Mixture" (20473). Gives "Softly Glowing Stone" (20462).
53. Common item: Spell: Resurrection (15392). Listed in 14 zones.
54. Hand "Spell: Resurrection" (15392) to karnor/"Spirit Of Venril Sathir". Spawns "Venril Sathir" (102126). Loot "Pulsing Green Stone" (20461) from "Venril Sathir".
55. firiona/"Foloal Stormforest", hand "Pulsing Green Stone" (20461) + "Softly Glowing Stone" (20462). Gives "Warmly Glowing Stone" (20468).
56. burningwood/"Telin Darkforest", hand "Warmly Glowing Stone" (20468). Gives "Ancient Longsword" (20477).
57. kaladimb/"Usbak The Old", hand "Ancient Longsword" (20477). Gives "Refined Ancient Sword" (20481).
58. burningwood/"Faelin Bloodbriar", hand "Refined Ancient Sword" (20481). Gives "Swiftwind" (20487).
59. Loot "Living Fragment of Fire" (28294) from "A Jopal Mystic" (NPC 217026) in `pofire`. Drop cache: 5.04% chance per kill.
60. Loot "Living Fragment of Water" (28293) from "A Triloun Diviner" in `powater`.
61. Loot "Living Fragment of Water" (28293) from "A Triloun Keeper" in `powater`.
62. Loot "Living Fragment of Water" (28293) from "A Triloun Water Guardian" in `powater`.
63. global/"Global Player", combine recipe 13413. Sets `ranger_epic` to `5`.
64. nedaria/"A Wayfarers Brotherhood Officer", say "Hail". Sets `ranger_epic` to `6`.
65. causeway/"Siflu", say "Adventurers". Requires `ranger_epic` ==6. Gives "Heated Loadstone" (62628).
66. Spawns "A Mangled Muramite Captain" (300069) in `wallofslaughter` on enter.
67. Loot "Spirit Manacles" (72340) from "A Mangled Muramite Captain".
68. Combine in "Crooked Cage" (32042): "Earthcaller" (20488), "Swiftwind" (20487), "Living Fragment of Fire" (28294), "Living Fragment of Water" (28293), "Heated Loadstone" (62628), "Spirit Manacles" (72340). Hands back "Earthcaller" (20488), "Swiftwind" (20487). Produces "Spirit Cage" (62656). The combine does not fail.
69. Spawns "A Vekerchiki Drone" (218047) in `poeartha` on event_combat.
70. Loot "Living Fragment of Earth" (28295) from "A Vekerchiki Drone".
71. 1 alternative loot source(s) also yield Living Fragment of Earth (28295).
72. Loot "Living Fragment of Air" (28292) from "A Temple Guardian".
73. Loot "Living Fragment of Air" (28292) from "A Temple Guardian" in `poair`.
74. Combine in "Crooked Cage" (32042): "Living Fragment of Fire" (28294), "Living Fragment of Water" (28293), "Heated Loadstone" (62628), "Spirit Manacles" (72340), "Living Fragment of Earth" (28295), "Living Fragment of Air" (28292). Produces "Spirit Cage" (62656). The combine does not fail.
75. global/"Global Player", combine recipe 19914. Sets `ranger_epic` to `8`.
76. Spawns "Craftmaster Tieranu" (334087) in `riftseekers` on enter.
77. Loot "Ring of Warmth" (11427) from "Craftmaster Tieranu".
78. Loot "Top Section of an Engraved Signet" (9956) from "An Ikaav Miragenist" (NPC 301015) in `bloodfields`. Drop cache: 6.08% chance per kill.
79. Loot "Bottom Section of an Engraved Signet" (10399) from "An Ikaav Castigator" (NPC 301003) in `bloodfields`. Drop cache: 4% chance per kill.
80. Loot "Center Section of an Engraved Signet" (10235) from "An Ikaav Deathbeckoner" (NPC 301008) in `bloodfields`. Drop cache: 5.13% chance per kill.
81. bloodfields/"Cryssa", hand "Top Section of an Engraved Signet" (9956) + "Center Section of an Engraved Signet" (10235) + "Bottom Section of an Engraved Signet" (10399). Gives "Enchanted Signet of the Disciples" (12080).
82. bloodfields/"Cryssa", hand "Top Section of an Engraved Signet" (9956) + "Center Section of an Engraved Signet" (10235) + "Bottom Section of an Engraved Signet" (10399). Sets `cleric20_darkdisciples` to `1`.
83. Spawns "A Corrupted Koalindl" (69141) in `oot` on event_fish_success.
84. Loot "Corrupted Koalindl's Heart" (69929) from "A Corrupted Koalindl".
85. Spawns "A Corrupted Koalindl" (224432) in `gunthak` on event_fish_success.
86. Loot "Corrupted Koalindl's Heart" (69930) from "A Corrupted Koalindl".
87. Spawns "A Corrupted Koalindl" (93306) in `overthere` on event_fish_success.
88. Loot "Corrupted Koalindl's Heart" (69931) from "A Corrupted Koalindl".
89. Spawns "A Corrupted Koalindl" (182150) in `nedaria` on event_fish_success.
90. Loot "Corrupted Koalindl's Heart" (69932) from "A Corrupted Koalindl".
91. qeynos2/"Enic Ruklin", hand "Corrupted Koalindl's Heart" (69929) + "Corrupted Koalindl's Heart" (69930) + "Corrupted Koalindl's Heart" (69931) + "Corrupted Koalindl's Heart" (69932). Sets `paladin_epic` to `4`.
92. qeynos2/"Enic Ruklin", hand "Corrupted Koalindl's Heart" (69929) + "Corrupted Koalindl's Heart" (69930) + "Corrupted Koalindl's Heart" (69931) + "Corrupted Koalindl's Heart" (69932). Gives "Seal of Enic" (69933).
93. Say "Hail" to skyfire/"Dry Sapara".
94. Spawns "Rithnok the Tormented" (91193).
95. Loot "Rithnok's Soulstone" (69935) from "Rithnok the Tormented".
96. skyfire/"Dry Sapara", hand "Rithnok's Soulstone" (69935). Gives "Rithnok's Soulstone" (69936).
97. Ground spawn of "Soulstone Shard" (69937) in `draniksscar`.
98. Ground spawn of "Soulstone Shard" (69938) in `bloodfields`.
99. Ground spawn of "Soulstone Shard" (69939) in `causeway`.
100. Ground spawn of "Soulstone Shard" (69940) in `dranik`.
101. Combine in "Rithnok's Soulstone" (69936): "Soulstone Shard" (69937), "Soulstone Shard" (69938), "Soulstone Shard" (69939), "Soulstone Shard" (69940). Produces "Rithnok's Soulstone" (69941). The combine does not fail.
102. dawnshroud/"Mikhal Young", hand "Drema's Fingerbone" (69946). Sets `paladin_epic` to `5`.
103. dawnshroud/"Mikhal Young", say "Find Anything". Requires `paladin_epic` ==4. Gives "Drema's Locket" (69945).
104. letalis/"Drema Young", hand "Drema's Locket" (69945). Requires `paladin_epic` set. Requires `paladin_epic` >=4. Gives "Drema's Fingerbone" (69946).
105. dawnshroud/"Denns Rootenpaw", hand "Drema's Fingerbone" (69946). Requires `paladin_epic` ==5. Gives "Bone Collector's Bag" (69947).
106. Loot "Dark Skeleton Remains" (69927) from "A Sun Revenant" in `thegrey`.
107. Loot "Dark Skeleton Remains" (69926) from "Disturbed Elysian Remains" (NPC 176016) in `umbral`. Drop cache: 2.58% chance per kill.
108. Loot "Dark Skeleton Remains" (69925) from "A Soriz Slave" (NPC 162029) in `ssratemple`. Drop cache: 35% chance per kill.
109. Combine in "Bone Collector's Bag" (69947): "Dark Skeleton Remains" (69927), "Dark Skeleton Remains" (69926), "Dark Skeleton Remains" (69925). Produces "Bone Collector's Bag" (69948). The combine does not fail.
110. dawnshroud/"Denns Rootenpaw", hand "Bone Collector's Bag" (69948). Requires `paladin_epic` ==5. Gives "Enchanted Bone Powder" (69949).
111. Hand "Enchanted Bone Powder" (69949) to letalis/"Drema Young". Spawns "Drema Young" (169128). Loot "Drema's Soulstone" (69928) from "Drema Young".
112. Loot "Soulstone Shard" (69950) from "Coterie Corruptor" in `tenebrous`.
113. Spawns "Shade of Mujaki the Devourer" (204081) in `ponightmare` on event death_complete:204080.
114. Loot "Soulstone Shard" (69951) from "Shade of Mujaki the Devourer".
115. Combine in "Drema's Soulstone" (69928): "Soulstone Shard" (69950), "Soulstone Shard" (69951). Produces "Drema's Soulstone" (69952). The combine does not fail.
116. abysmal/"Lovine Lemise", say "Ingredients". Requires `paladin_epic` ==5. Gives "Lovine's Potion Bag" (69922).
117. Loot "Ra'Tuk Screambringer's Jaw" (69921) from "A Ra'Tuk Screambringer" (NPC 283104) in `barindu`. Drop cache: 4.06% chance per kill.
118. Loot "Noc Fleshfeasters Tail" (69920) from "A Noc Fleshfeaster" in `riwwi`.
119. Loot "Mastruq Havocblade Blood" (69919) from "A Mastruq Havocblade" in `qinimi`.
120. Loot "Mastruq Havocblade Blood" (69919) from "A Mastruq Warfiend" in `qinimi`.
121. Loot "Potameid Seaweed Strands" (69918) from "An Entrapped Potameid" in `natimbi`.
122. Combine in "Lovine's Potion Bag" (69922): "Ra'Tuk Screambringer's Jaw" (69921), "Noc Fleshfeasters Tail" (69920), "Mastruq Havocblade Blood" (69919), "Potameid Seaweed Strands" (69918). Produces "Lovine's Potion Bag" (69923). The combine does not fail.
123. abysmal/"Lovine Lemise", hand "Lovine's Potion Bag" (69923). Sets `paladin_epic_reiya` to `1`.
124. Summon "Foldable Medicine Bag" (17770) by casting "Unfold Medicine Bag".
125. Common item: Fine Potion Vial (95846). Listed in 15 zones.
126. Loot "Robust Shadow Essence" (96911) from "Qua Senshali Xakra" (NPC 158020) in `vexthal`. Drop cache: 28.72% chance per kill.
127. Loot "Sage Leaf" (14215) from "a Di'zok Herbalist" in `chardok`.
128. Loot "Sage Leaf" (14215) from "a Sarnak Herb Collector" in `chardok`.
129. Loot "Sage Leaf" (14215) from "an Apprentice Herbalist" in `chardok`.
130. Loot "Valerian Root" (14230) from "a Di'zok Herbalist" in `chardok`.
131. Loot "Valerian Root" (14230) from "a Sarnak Herb Collector" in `chardok`.
132. Loot "Valerian Root" (14230) from "an Apprentice Herbalist" in `chardok`.
133. Common item: Woundwart (16526). Listed in 9 zones.
134. Combine in "Foldable Medicine Bag" (17770): "Fine Potion Vial" (95846), "Robust Shadow Essence" (96911), "Sage Leaf" (14215), "Valerian Root" (14230), "Woundwart" (16526). Produces "Mist of the Breathless" (96937). Requires Alchemy, trivial 224.
135. abysmal/"Reiya The Pained", hand "Mist of the Breathless" (96937). Requires `paladin_epic_reiya` ==1. Gives "Reiya's Soulstone" (69924).
136. Unresolved cyclic prerequisite: `mage_epic` >=9.
137. draniksscar/"Iilivina", say "Primals". Sets `mage_epic` to `10`.
138. Spawns "Shade of Reiya the Pained" (284104) in `ferubi` on enter.
139. Loot "Soulstone Shard" (69943) from "Shade of Reiya the Pained".
140. Loot "Soulstone Shard" (69944) from "Vuranish Xxuro" in `vxed`.
141. Combine in "Reiya's Soulstone" (69924): "Soulstone Shard" (69943), "Soulstone Shard" (69944). Produces "Reiya's Soulstone" (69942). The combine does not fail.
142. Loot "Redis' Soulstone" (69983) from "Shade of Redis Linrok" in `dranikcatacombsa`.
143. Spawns "Herrian Warfrost" (300057) in `wallofslaughter` on enter.
144. Loot "Hoarfrost Wand" (76999) from "Herrian Warfrost".
145. Combine in "Spirit Cage" (62656): "Ring of Warmth" (11427), "Hoarfrost Wand" (76999). Produces "Elemental Ice Spirit Cage" (62647). The combine does not fail.

### "Heartwood Blade" (62627)

1. No quest step gives Planar Fletching Kit (17762). The dump lists it in poknowledge.
2. global/"Global Player", combine recipe 13412. Sets `ranger_epic` to `3`.
3. jaggedpine/"Red Dogwood Treant", say "Hail". Requires `ranger_epic` ==3. Gives "Red Dogwood Heartwood" (62623).
4. dranik/"Ranger 1 5", hand "Red Dogwood Heartwood" (62623). Requires `ranger_dranik_chest` unset. Gives "Wind-blessed Heartwood" (62626).
5. jaggedpine/"Red Dogwood Treant", say "Hail". Requires `ranger_epic` ==3. Gives "Spring Dogwood Seed" (62624).
6. qrg/"Corun Finisc", hand "Spring Dogwood Seed" (62624). Gives "Block of Purest Silver" (62625).
7. Combine in "Planar Fletching Kit" (17762): "Wind-blessed Heartwood" (62626), "Block of Purest Silver" (62625). Produces "Heartwood Blade" (62627). Requires Fletching. The combine does not fail.

## `ranger_epic`

Values written: 1, 2, 3, 5, 6, 7.

### 1. althele — say hail

Zone: `eastkarana`.

> Hello, friend. Beautiful is what I would call such a day normally, but lately? I sense that something is [

Sets `ranger_epic` to `1`.

- Needs `ranger_epic` unset.
- One of: Earthcaller (20488); Essence of Earth and Wind (62600).
In script order:

1. Sets `ranger_epic` to `1`.


How the items are reached:

- Earthcaller (20488)
  - Prerequisite: "Earthcaller" (20488). See section 0.
- Essence of Earth and Wind (62600)
  - Prerequisite: "Essence of Earth and Wind" (62600). See section 0.

### 2. shana liskia — hand 62617

Zones: `freeportwest`, `freportw`.

Sets `ranger_epic` to `2`.

- Turn in x1: Corun's Notes (62617).
In script order:

1. Sets `ranger_epic` to `2`.
2. Gives Corun's Notes - annotated (62654).


How the items are reached:

- Corun's Notes (62617)
  - Prerequisite: "Corun's Notes" (62617). See section 0.

### 3. global player — combine recipe 13412

Zone: `global`.

Sets `ranger_epic` to `3`.

In script order:

1. Sets `ranger_epic` to `3`.


Combine:

- `recipe:13412` is combined in Fertile Earth (72091).
  - Ground spawn of "Fertile Earth" (72091) in `jaggedpine`.
  - Put in x1: Senvial's Blessing (62621).
    - Prerequisite: "Senvial's Blessing" (62621). See section 0.
  - Put in x1: Grinbik's Blessing (62622).
    - Prerequisite: "Grinbik's Blessing" (62622). See section 0.
  - Put in x1: Red Dogwood Seed (62844).
    - Prerequisite: "Red Dogwood Seed" (62844). See section 0.
  - Spawns Red Dogwood Treant (181222).
    - Loots Plant Shoot (8154).
    - Loots Treant Finger (8268).
  - The combine does not fail.

### 5. global player — combine recipe 13413

Zone: `global`.

Sets `ranger_epic` to `5`.

In script order:

1. Sets `ranger_epic` to `5`.


Combine:

- `recipe:13413` is combined in Planar Fletching Kit (17762).
  - No quest step gives Planar Fletching Kit (17762). The dump lists it in poknowledge.
  - Put in x1: Wind-blessed Heartwood (62626).
    - Prerequisite: "Wind-blessed Heartwood" (62626). See section 0.
  - Put in x1: Block of Purest Silver (62625).
    - Prerequisite: "Block of Purest Silver" (62625). See section 0.
  - Produces Heartwood Blade (62627).
  - Requires Fletching. The combine does not fail.

### 6. a wayfarers brotherhood officer — say hail

Zone: `nedaria`.

> Hello. I can tell that you are a great hunter and tracker. I wanted to pass on to you some information, act on it as you will. A group of adventurers stopped...

Sets `ranger_epic` to `6`.

- Needs `ranger_epic` ==5.
In script order:

1. Sets `ranger_epic` to `6`.


### 7. a wayfarers brotherhood officer — hand 62629

Zone: `nedaria`.

Sets `ranger_epic` to `7`.

- Needs `ranger_epic` ==6.
- Turn in x1: Traveler's Journal (62629).
In script order:

1. Sets `ranger_epic` to `7`.


How the items are reached:

- Traveler's Journal (62629)
  - Spawns "A Mangled Muramite Captain" (300069) in `wallofslaughter` on enter.
  - Loot "Traveler's Journal" (62629) from "A Mangled Muramite Captain".

### Steps on `ranger_epic` that do not change it

- `bloodfields` marshall trap, on enter needs `ranger_epic` ==2.
  - Sets `ranger_epic_bloodfield` to `1`.
  - Spawns Marshal Histent (301065).
  - Spawns Grinbik the Fertile (301066).
  - Spawns an enslaved earthmover (301067).
  - Spawns an eager student (301068).
- `bloodfields` ranger 1 5, say hail needs `ranger_epic` ==2.
  - Sets `ranger_bloodfield_chest` to `1`.
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
  - Gives Grinbik's Blessing (62622).
- `causeway` rng trap, on enter needs `ranger_epic` ==6.
  - Spawns Siflu (303091).
- `causeway` siflu, say adventurers needs `ranger_epic` ==6.
  - Gives Heated Loadstone (62628).
- `dranik` sverins trap, on enter needs `ranger_epic` ==3.
  - Sets `ranger_epic_dranik` to `1`.
  - Spawns Sverins Fireskin (336002).
  - Spawns Uisima Lord of the Depths (336001).
  - Spawns a fireskin acolyte (336230).
  - Loots Decaying Book (36520).
  - Loots Earring of Ethical Uncertainty (70191).
  - Loots Dragorn Greatblade (71184).
  - Loots Discordant Scoriae (72086).
  - Loots Bloodroot (72157).
  - Loots Slugworms (72162).
  - Loots Bloodflow Stone (72650).
  - Loots Starflow Stone (72651).
  - Loots Boneflow Stone (72652).
  - Loots Fireflow Stone (72653).
  - Loots Waterflow Stone (72654).
  - Loots Mudflow Stone (72655).
  - Loots Voidflow Stone (72657).
  - Loots Emberflow Stone (72658).
  - Loots Stormflow Stone (72659).
  - Loots Mossflow Stone (72660).
  - Loots Shadowflow Stone (72661).
  - Loots Journal of Ramel the Strategist (77703).
  - Loots The Darkening Compendium Page 1 (77714).
- `eastkarana` althele, say out of balance needs `ranger_epic` ==1.
  - Sets `druid_epic` to `1`.
- `jaggedpine` red dogwood treant, say hail needs `ranger_epic` ==3.
  - Gives Red Dogwood Heartwood (62623).
  - Gives Spring Dogwood Seed (62624).
- `natimbi` ranger 1 5, say hail needs `ranger_epic` set.
  - Sets `ranger_natimbi_chest` to `1`.
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
  - Gives Senvial's Blessing (62621).
- `natimbi` trenzar trap, on enter needs `ranger_epic` ==2.
  - Sets `ranger_epic_natimbi` to `1`.
  - Spawns Spiritbinder Trenzar (280084).
  - Spawns a bound earth spirit (280085).
  - Spawns a bound fire spirit (280086).
- `thedeep` player, on enter needs `ranger_epic` ==2.
  - Sets `ranger_epic_deep` to `1`.
  - Spawns ancient thought horror trap (164123).
- `veksar` player, on enter needs `ranger_epic` ==1.
  - Sets `warrior_epic_gulak` to `1`.
  - Spawns Decaying Lord Galuk Drek, not be in db yet (109906).
  - Sets `ranger_epic_veks` to `1`.
  - Spawns an asteatotic highborn (109907).
  - Loots Skeletal Tome of Galuk Drek (60310).
  - Loots Rune of Coruscation (16631).
  - Loots Phosphorous Powder (24082).
  - Loots Fused Loam (34883).
  - Loots Excellent Spinneret Fluid (34910).
  - Loots Superb Spinneret Fluid (34911).
  - Loots Asteatotic Veksar Blood (35100).
  - Loots Uncut Amethyst (37844).
  - Loots Uncut Combine Star (37845).
  - Loots Uncut Black Sapphire (37846).
  - Loots Uncut Alexandrite (37847).
  - Loots Uncut Goshenite (37848).
  - Loots Uncut Morganite (37849).
  - Loots Uncut Jacinth (37850).
  - Loots Uncut Demantoid (37851).
  - Loots Uncut Rubellite (37852).
  - Loots Raw Indigo Nihilite (37858).
  - Loots Raw Amber Nihilite (37859).
  - Loots Exquisite Gem Dusted Rune (38699).
  - Loots Exquisite Gold Gem Dusted Rune (38702).
  - Loots Velium Gem Dusted Rune (38706).
  - Loots Complex Velium Gem Dusted Rune (38707).
  - Loots Exquisite Velium Gem Dusted Rune (38708).
  - Loots Velium Gemmed Rune (38709).
  - Loots Raw Crimson Nihilite (58067).
  - Loots Raw Shimmering Nihilite (58068).
  - Loots Words of Retention (65325).
  - Loots Words of Torment (65331).
  - Loots Words of Aptitude (65346).
  - Loots Words of Potence (65350).
  - Loots Part of Yaeth's Compendium Pg. 118 (65371).
  - Loots Part of Yaeth's Compendium Pg. 26 (65392).
  - Loots Prestidigitase (97001).
  - Loots Staurolite (97002).
  - Loots Harmonagate (97003).
  - Loots Taaffeite (97286).
- `wallofslaughter` rng trap, on enter needs `ranger_epic` ==6.
  - Spawns a mangled muramite captain (300069).
  - Spawns aged ukun (300070).
  - Loots Curzon (35085).
  - Loots Platinum Etched Reinforced Rod (37046).
  - Loots Noc Blood (55850).
  - Loots Traveler's Journal (62629).
  - Loots Spirit Manacles (72340).
  - Loots Ukun Guts (55847).
  - Loots Broken Ukun Leash (55848).
  - Loots Polished Blue Softstone (80030).
- `westwastes` player, on enter needs `ranger_epic` ==1.
  - Sets `ranger_epic_wyv` to `1`.
  - Spawns a neuralgic huntress (120136).
  - Loots Unrefined Diamond (8887).
  - Loots Unrefined Sapphire (8888).
  - Loots Unrefined Emerald (8889).
  - Loots Phosphorous Powder (24082).
  - Loots Sunshard Pebble (33791).
  - Loots Complex Gold Gem Dusted Rune (38701).
  - Loots Exquisite Gold Gem Dusted Rune (38702).
  - Loots Part of Toharon's Memoir Pg. 15 (65377).
  - Loots Neuralgic Wyvern Blood (72605).

## `ranger_epic15_pre`

Values written: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11.

### 1. targen stonefall — say native stones

Zone: `nedaria`.

> Just about any of them, really. I

Sets `ranger_epic15_pre` to `1`.

- Needs `ranger_epic15_pre` unset.
In script order:

1. Sets `ranger_epic15_pre` to `1`.


### 2. targen stonefall — hand 62601

Zone: `nedaria`.

Sets `ranger_epic15_pre` to `2`.

- Needs `ranger_epic15_pre` ==1.
- Turn in x1: Blasted Stone (62601).
In script order:

1. Sets `ranger_epic15_pre` to `2`.
2. Gives Washed Blasted Stone (62602).


How the items are reached:

- Blasted Stone (62601)
  - Forage "Blasted Stone" (62601) in `bloodfields`.

### 3. targen stonefall — say odus

Zone: `nedaria`.

> It

Sets `ranger_epic15_pre` to `3`.

- Needs `ranger_epic15_pre` ==2.
In script order:

1. Sets `ranger_epic15_pre` to `3`.


### 4. player — on loot

Zone: `hole`.

Sets `ranger_epic15_pre` to `4`.

- Needs `ranger_epic15_pre` ==3.
- Needs Dusty Stone (62653).
In script order:

1. Sets `ranger_epic15_pre` to `4`.


How the items are reached:

- Dusty Stone (62653)
  - Spawns "Stone Collector" (39168) in `hole` on enter.
  - Loot "Dusty Stone" (62653) from "Stone Collector".

### 5. targen stonefall — hand 62641

Zone: `nedaria`.

Sets `ranger_epic15_pre` to `5`.

- Needs `ranger_epic15_pre` ==4.
- Turn in x1: Closed Sample Cloth (62641).
In script order:

1. Sets `ranger_epic15_pre` to `5`.


How the items are reached:

- Closed Sample Cloth (62641)
  - Prerequisite: "Closed Sample Cloth" (62641). See section 0.

### 6. targen stonefall — say impurities

Zone: `nedaria`.

> A large portion of this stone is infused with material native to this place. I call those impurities because to me the real stone here is the stuff that seem...

Sets `ranger_epic15_pre` to `6`.

- Needs `ranger_epic15_pre` ==5.
In script order:

1. Sets `ranger_epic15_pre` to `6`.
2. Gives Polished Blasted Stone (62603).


### 7. xanuusus — hand 62603

Zone: `northkarana`.

Sets `ranger_epic15_pre` to `7`.

- Needs `ranger_epic15_pre` ==6.
- Turn in x1: Polished Blasted Stone (62603).
In script order:

1. Sets `ranger_epic15_pre` to `7`.
2. Gives Polished Blasted Stone (62603).
3. Gives Poem of the Storms (62632).


How the items are reached:

- Polished Blasted Stone (62603)
  - Prerequisite: "Polished Blasted Stone" (62603). See section 0.

### 8. player — on loot

Zone: `torgiran`.

Sets `ranger_epic15_pre` to `8`.

- Needs `ranger_epic15_pre` ==7.
- Needs Taskmaster's Cutlass (62631).
In script order:

1. Sets `ranger_epic15_pre` to `8`.


How the items are reached:

- Taskmaster's Cutlass (62631)
  - Loot "Taskmaster's Cutlass" (62631) from "Taskmaster Waggad Brokenskull" in `torgiran`.

### 9. xanuusus — hand 62604

Zone: `northkarana`.

Sets `ranger_epic15_pre` to `9`.

- Needs `ranger_epic15_pre` ==8.
- Turn in x1: Stone of Winde (62604).
In script order:

1. Sets `ranger_epic15_pre` to `9`.
2. Gives Stone of Winde (62604).


How the items are reached:

- Stone of Winde (62604)
  - Prerequisite: "Stone of Winde" (62604). See section 0.

### 10. ghost of mera — hand 62637

Zone: `charasis`.

Sets `ranger_epic15_pre` to `10`.

- Needs `ranger_epic15_pre` ==9.
- Needs `ranger_epic15_pre` ==10.
- Turn in x1: Sound Capture Jar (62637).
In script order:

1. Sets `ranger_epic15_pre` to `10`.


How the items are reached:

- Sound Capture Jar (62637)
  - Prerequisite: "Sound Capture Jar" (62637). See section 0.

### 11. mairee silentone — hand 62604+62638

Zone: `erudnint`.

Sets `ranger_epic15_pre` to `11`.

- Needs `ranger_epic15_pre` ==10.
- Turn in x1: Echoing Jar (62638).
- Turn in x1: Stone of Winde (62604).
In script order:

1. Sets `ranger_epic15_pre` to `11`.
2. Gives Essence of Earth and Wind (62600).


How the items are reached:

- Echoing Jar (62638)
  - Spawns "Ghost of Mera" (105290) in `charasis` on event_enterzone.
  - Hand "Sound Capture Jar" (62637) to charasis/"Ghost Of Mera". Sets `ranger_epic15_pre` to `10`.
  - Loot "Echoing Jar" (62638) from "Ghost of Mera".
- Stone of Winde (62604)
  - Prerequisite: "Stone of Winde" (62604). See section 0.

### Steps on `ranger_epic15_pre` that do not change it

- `hole` player, on enter needs `ranger_epic15_pre` ==3.
  - Spawns Stone Collector (39168).
  - Loots Dusty Stone (62653).
- `nedaria` targen stonefall, say bloodfields needs `ranger_epic15_pre` ==2.
  - Gives Targen's Emulsion (62639).
  - Gives Sample Cloth (62640).
- `northkarana` xanuusus, say hail needs `ranger_epic15_pre` ==7.
  - Gives Polished Blasted Stone (62603).
- `northkarana` xanuusus, say ready needs `ranger_epic15_pre` ==8.
  - Spawns A Tainted Beast (13131).
  - Loots Stone of Winde (62604).
- `steamfont` godbin strumharp, hand platinum:30 needs `ranger_epic15_pre` ==9.
  - Gives Sound Capture Jar (62637).
- `steamfontmts` godbin strumharp, hand platinum:30 needs `ranger_epic15_pre` ==9.
  - Gives Sound Capture Jar (62637).

## `ranger_epic` 2.0

Values written: 8, 9.

### 8. global player — combine recipe 19914

Zone: `global`.

Sets `ranger_epic` to `8`.

In script order:

1. Sets `ranger_epic` to `8`.


Combine:

- `recipe:19914` is combined in Crooked Cage (32042).
  - Loot "Crooked Cage" (32042) from "a Broken Skull bruiser" in `torgiran`.
  - Put in x1: Earthcaller (20488).
    - Prerequisite: "Earthcaller" (20488). See section 0.
  - Put in x1: Swiftwind (20487).
    - Prerequisite: "Swiftwind" (20487). See section 0.
  - Put in x1: Living Fragment of Fire (28294).
    - Loot "Living Fragment of Fire" (28294) from "A Jopal Mystic" (NPC 217026) in `pofire`. Drop cache: 5.04% chance per kill.
  - Put in x1: Living Fragment of Water (28293).
    - Loot "Living Fragment of Water" (28293) from "A Triloun Diviner" in `powater`.
    - Loot "Living Fragment of Water" (28293) from "A Triloun Keeper" in `powater`.
    - Loot "Living Fragment of Water" (28293) from "A Triloun Water Guardian" in `powater`.
  - Put in x1: Heated Loadstone (62628).
    - Prerequisite: "Heated Loadstone" (62628). See section 0.
  - Put in x1: Spirit Manacles (72340).
    - Spawns "A Mangled Muramite Captain" (300069) in `wallofslaughter` on enter.
    - Loot "Spirit Manacles" (72340) from "A Mangled Muramite Captain".
  - Hands back Earthcaller (20488), Swiftwind (20487).
  - Produces Spirit Cage (62656).
  - The combine does not fail.

Alternative or repeat transition to `ranger_epic` = `8` (not an additional required stage).

### 8. global player — combine recipe 19915

Zone: `global`.

Sets `ranger_epic` to `8`.

In script order:

1. Sets `ranger_epic` to `8`.


Combine:

- `recipe:19915` is combined in Crooked Cage (32042).
  - Loot "Crooked Cage" (32042) from "a Broken Skull bruiser" in `torgiran`.
  - Put in x1: Living Fragment of Fire (28294).
    - Loot "Living Fragment of Fire" (28294) from "A Jopal Mystic" (NPC 217026) in `pofire`. Drop cache: 5.04% chance per kill.
  - Put in x1: Living Fragment of Water (28293).
    - Loot "Living Fragment of Water" (28293) from "A Triloun Diviner" in `powater`.
    - Loot "Living Fragment of Water" (28293) from "A Triloun Keeper" in `powater`.
    - Loot "Living Fragment of Water" (28293) from "A Triloun Water Guardian" in `powater`.
  - Put in x1: Heated Loadstone (62628).
    - Prerequisite: "Heated Loadstone" (62628). See section 0.
  - Put in x1: Spirit Manacles (72340).
    - Spawns "A Mangled Muramite Captain" (300069) in `wallofslaughter` on enter.
    - Loot "Spirit Manacles" (72340) from "A Mangled Muramite Captain".
  - Put in x1: Living Fragment of Earth (28295).
    - Spawns "A Vekerchiki Drone" (218047) in `poeartha` on event_combat.
    - Loot "Living Fragment of Earth" (28295) from "A Vekerchiki Drone".
    - 1 alternative loot source(s) also yield Living Fragment of Earth (28295).
  - Put in x1: Living Fragment of Air (28292).
    - Loot "Living Fragment of Air" (28292) from "A Temple Guardian".
    - Loot "Living Fragment of Air" (28292) from "A Temple Guardian" in `poair`.
  - Produces Spirit Cage (62656).
  - The combine does not fail.

### 9. oshimai spirit of the high air — hand 47100+62627+62647

Zone: `anguish`.

Sets `ranger_epic` to `9`.

- Needs `ranger_epic` ==8.
- Turn in x1: Elemental Ice Spirit Cage (62647).
- Turn in x1: Globe of Discordant Energy (47100).
- Turn in x1: Heartwood Blade (62627).
In script order:

1. Sets `ranger_epic` to `9`.
2. Gives Aurora, the Heartwood Blade (62649).


How the items are reached:

- Elemental Ice Spirit Cage (62647)
  - Prerequisite: "Elemental Ice Spirit Cage" (62647). See section 0.
- Globe of Discordant Energy (47100)
  - Say "Check Lorb" to anguish/"Zone Status".
  - Spawns "Orb of Discordant Energy" (317087).
  - Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy".
  - 4 alternative loot source(s) also yield Globe of Discordant Energy (47100).
- Heartwood Blade (62627)
  - Prerequisite: "Heartwood Blade" (62627). See section 0.

### Steps on `ranger_epic` that do not change it

- `riftseekers` player, on enter needs `ranger_epic` ==8.
  - Sets `rng_spawn_rss` to `1`.
  - Spawns Craftmaster Tieranu (334087).
  - Loots Ring of Warmth (11427).
- `riftseekers` player, on loot needs `ranger_epic` ==8.
  - Sets `rng_rss_chest` to `1`.
  - Spawns a chest (Epic 2.0) (893).
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
- `wallofslaughter` player, on enter needs `ranger_epic` ==8.
  - Sets `paladin_wos` to `1`.
  - Spawns Durunal the Cursebearer (300087).
  - Sets `rng_spawn_wos` to `1`.
  - Spawns Herrian Warfrost (300057).
  - Spawns an excited builder (300058).
  - Loots Dark and Twisted Sword (69971).
  - Loots Gelidran Blood (72073).
  - Loots Hoarfrost Wand (76999).
  - Loots Polished Blue Softstone (80030).
  - Loots Sunshard Powder (35088).
  - Loots Platinum Etched Reinforced Rod (37046).
  - Loots Raw Crimson Nihilite (58067).
- `wallofslaughter` player, on loot needs `ranger_epic` ==8.
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

- `ranger_epic_bloodfield` set to 1 at bloodfields/marshall trap.
- `ranger_epic_deep` set to 1 at thedeep/player.
- `ranger_epic_dranik` set to 1 at dranik/sverins trap.
- `ranger_epic_natimbi` set to 1 at natimbi/trenzar trap.
- `ranger_epic_veks` set to 1 at veksar/player.
- `ranger_epic_wyv` set to 1 at westwastes/player.
