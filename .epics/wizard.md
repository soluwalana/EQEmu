# Wizard

Steps taken from the quest graph only. **Broken** means the graph has no edge for that value or that item.

Flags with writes: `wiz_epic_pre`, `wiz_epic`, `wizepic`, `wizepicA`, `wizepicB`, `wizepicK`, `wiz_epic20`.

## 0. Prerequisites

Shared acquisition steps appear in the first prerequisite chain that needs them. Later sections reference that chain rather than repeating it.

### "Silken Tapestry Satchel" (12596)

1. Summon "Collapsible Sewing Kit" (17165) by casting "Unfold Sewing Kit".
2. Common item: Backpack Pattern (12089). Listed in 40 zones.
3. Common item: Needle Mold (12019). Listed in 32 zones.
4. Common item: Thimble Mold (12057). Listed in 32 zones.
5. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
6. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `steamfont`.
7. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `tox`.
8. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `toxxulia`.
9. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
10. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). The combine does not fail.
11. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
12. **Broken:** nothing in the graph gives, loots, spawns, or combines Notice to Cease and Desist (9590).
13. Hand "Notice to Cease and Desist" (9590) to freeporteast/"Lythe Songbird". Spawns "a Freeport guard" (382255). Loot "Fine Steel Two Handed Sword" (5351) from "a Freeport guard".
14. 10 alternative loot source(s) also yield Fine Steel Two Handed Sword (5351).
15. Combine in Forge (17): "Fine Steel Two Handed Sword" (5351), "Water Flask" (13006). Produces "Small Brick of High Quality Ore" (10468) x2, "Small Piece of High Quality Ore" (22229). Requires Blacksmithing, trivial 21.
16. Combine in Royal Qeynos Forge (40): "Small Piece of High Quality Ore" (22229), "Water Flask" (13006). Produces "High Quality Metal Bits" (22230). Requires Blacksmithing, trivial 20.
17. Combine in Vale Forge (49): "Needle Mold" (12019), "Thimble Mold" (12057), "Water Flask" (13006), "High Quality Metal Bits" (22230). Produces "Vale Sewing Kit" (92882). Requires Blacksmithing, trivial 162.
18. **Broken:** no event trigger found for `misty/misty#timer:Spawn`.
19. Starts timer `Hatch`.
20. Spawns "A Vicious Spider" (33167) after `misty/misty#timer:Hatch`.
21. Loot "Spiderling Silk" (13099) from "A Vicious Spider".
22. Forage "Spiderling Silk" (13099) in `mistmoore`.
23. Forage "Spiderling Silk" (13099) in `mmca`.
24. Forage "Spiderling Silk" (13099) in `mmcb`.
25. Forage "Spiderling Silk" (13099) in `mmcc`.
26. Forage "Spiderling Silk" (13099) in `mmcd`.
27. Forage "Spiderling Silk" (13099) in `mmce`.
28. Forage "Spiderling Silk" (13099) in `mmcf`.
29. Forage "Spiderling Silk" (13099) in `mmcg`.
30. Forage "Spiderling Silk" (13099) in `mmch`.
31. Forage "Spiderling Silk" (13099) in `mmci`.
32. Forage "Spiderling Silk" (13099) in `mmcj`.
33. Combine in "Vale Sewing Kit" (92882): "Spiderling Silk" (13099). Produces "Silk Thread" (16486). Requires Tailoring, trivial 15. The combine does not fail.
34. Combine in "Vale Sewing Kit" (92882): "Silk Thread" (16486). Produces "Silk Cord" (16489). Requires Tailoring, trivial 26.
35. potranquility/"Kalym Rasalan", say "Hail". Gives "Silken Tapestry" (12593).
36. Combine in "Collapsible Sewing Kit" (17165): "Backpack Pattern" (12089), "Silk Cord" (16489), "Silken Tapestry" (12593). Produces "Silken Tapestry Satchel" (12596). Requires Tailoring 128. The combine does not fail.

### "Full Tapestry Satchel" (16753)

1. Acquisition of "Silken Tapestry Satchel" (12596) is documented under "Silken Tapestry Satchel" (12596); obtain another copy if needed.
2. Ground spawn of "Prismatic Crystal" (12599) in `veksar`.
3. Ground spawn of "Prismatic Crystal" (12625) in `timorous`.
4. Ground spawn of "Prismatic Crystal" (12628) in `twilight`.
5. Loot "Prismatic Crystal" (12662) from "Treasure Sorter Neiben" in `dulak`.
6. Loot "Cohesion Gem" (67022) from "A Metallic Slime" (NPC 206031) in `poinnovation`. Drop cache: 34.24% chance per kill.
7. Spawns "Spawn Wiz 1.5; Pure Flame Elemental" (278108) in `soldungc` on event_signal.
8. Loot "Wisp of Pure Flame" (11619) from "Spawn Wiz 1.5; Pure Flame Elemental".
9. lavastorm/"Talwyn Flamecaller", hand "Wisp of Pure Flame" (11619). Sets `wiz_epic_wisp` to `1`.
10. Spawns "Mistress of the Darkwater Quest-only" (125075) in `sirens` on enter.
11. Loot "Shard of Pure Ice" (11599) from "Mistress of the Darkwater Quest-only".
12. Loot "Fluxing Staff" (11445) from "Girplan Guardian" in `wallofslaughter`.
13. lavastorm/"Talwyn Flamecaller", say "Hail". Sets `wiz_epic` to `1`.
14. Say "Gem" to scarlet/"The Gem Guardian".
15. Spawns "Elite Sun Revenant" (175306).
16. Loot "Fluxing Gem" (11448) from "Elite Sun Revenant".
17. Loot "Fluxing Rune" (11474) from "Hobgoblin Horrorfiend" in `ponightmare`.
18. Ground spawn of "Fluxing Chunk of Ore" (11576) in `dranik`.
19. lavastorm/"Talwyn Flamecaller", hand "Fluxing Staff" (11445) + "Fluxing Gem" (11448) + "Fluxing Rune" (11474) + "Fluxing Chunk of Ore" (11576). Gives "Staff of Fluxing Power" (11596).
20. Combine in "Silken Tapestry Satchel" (12596): "Prismatic Crystal" (12599), "Prismatic Crystal" (12625), "Prismatic Crystal" (12628), "Prismatic Crystal" (12662), "Cohesion Gem" (67022), "Shard of Pure Ice" (11599), "Wisp of Pure Flame" (11619), "Staff of Fluxing Power" (11596). Produces "Full Tapestry Satchel" (16753). The combine does not fail.

### "Spell: Electrical Charge" (16623)

1. bazaar/"Caerlyna", hand "Spell Research Kit" (93492). Gives "Spell Research Kit Token" (93667).
2. bazaar/"Caerlyna", hand "Spell Research Kit Token" (93667). Gives "Spell Research Kit" (93492).
3. Loot "Metal Pipe" (12979) from "A Drolvarg Pawbuster" in `karnor`.
4. Loot "Metal Pipe" (12980) from "An Iksar Betrayer" in `chardok`.
5. No quest step gives King's Court Token (66616). The dump lists it in shadowhaven.
6. shadowhaven/"Gralin Silvertooth", hand "King's Court Token" (66616). Gives "Deluxe Sewing Kit" (17966).
7. Loot "Code of Zan Fi" (12316) from "Targin the Rock" in `soldungb`.
8. Loot "Blackburrow Gnoll Pelt" (13027) from "Refugee Splitpaw" (NPC 17023) in `blackburrow`. Drop cache: 55% chance per kill.
9. Loot "Blackburrow Gnoll Skin" (13028) from "The Gnoll High Shaman" (NPC 17042) in `blackburrow`. Drop cache: 55% chance per kill.
10. Loot "Putrid Rib Bone" (13722) from "A Putrid Skeleton" in `qeytoqrg`.
11. Loot "Gnoll Pup Scalp" (13789) from "A Gnoll Pup" in `blackburrow`.
12. Loot "Gnoll Pup Scalp" (13789) from "A Gnoll Pup" in `everfrost`.
13. Loot "Gnoll Pup Scalp" (13789) from "A Gnoll Pup" in `qeynos2`.
14. Loot "Gnoll Pup Scalp" (13789) from "A Gnoll Pup" in `qeytoqrg`.
15. qeynos2/"Phin Esrinap", hand "Gnoll Pup Scalp" (13789) + "Gnoll Pup Scalp" (13789) + "Gnoll Pup Scalp" (13789) + "Gnoll Pup Scalp" (13789). Gives "White Headband" (10110).
16. qeynos2/"Phin Esrinap", hand "White Headband" (10110) + "Putrid Rib Bone" (13722) + "Putrid Rib Bone" (13722) + "Putrid Rib Bone" (13722). Gives "Yellow Headband" (10111).
17. qeynos2/"Phin Esrinap", hand "Yellow Headband" (10111) + "Blackburrow Gnoll Pelt" (13027) + "Blackburrow Gnoll Pelt" (13027) + "Blackburrow Gnoll Skin" (13028). Gives "Orange Headband" (10112).
18. Loot "Head of Ghanex Drah" (13165) from "Ghanex Drah" in `southkarana`.
19. Loot "Dareb's Skull" (13166) from "High Shaman Phido" in `southkarana`.
20. Loot "Dareb's Skull" (13166) from "An Undead Cyclops" in `southkarana`.
21. Loot "Head of Shen" (13167) from "High Shaman Grisok" in `southkarana`.
22. qeynos2/"Togahn Sorast", hand "Orange Headband" (10112) + "Head of Ghanex Drah" (13165) + "Dareb's Skull" (13166) + "Head of Shen" (13167). Gives "Red Headband" (10113).
23. Loot "Skull of Jhen'Tra" (13168) from "A Gnoll Embalmer" in `lakerathe`.
24. Loot "Dagger of Marnek" (13169) from "The Fabled Thaumaturgist".
25. Loot "Dagger of Marnek" (13169) from "The Thaumaturgist" in `befallen`.
26. Loot "Zaharn's Coronet" (3000) from "High Priest Zaharn" in `permafrost`.
27. qeynos2/"Togahn Sorast", hand "Zaharn's Coronet" (3000) + "Red Headband" (10113) + "Skull of Jhen'Tra" (13168) + "Dagger of Marnek" (13169). Gives "Purple Headband" (10114).
28. southkarana/"Brother Qwinn", hand "Purple Headband" (10114) + "Code of Zan Fi" (12316). Gives "Needle of the Void" (12314).
29. Loot "The Idol" (12317) from "Raster of Guk" in `gukbottom`.
30. Loot "Blackened Wand" (13237) from "Priest Amiaz" in `befallen`.
31. Loot "Blackened Sapphire" (13238) from "Ekeros" in `najena`.
32. Loot "Greater Lightstone" (10400) from "A Windwillow Wisp" (NPC 397070) in `mesa`. Drop cache: 32.8% chance per kill.
33. Loot "Cutthroat Insignia Ring" (1903) from "a Dervish Cutthroat" (NPC 457074) in `oldcommons`. Drop cache: 55.56% chance per kill.
34. Loot "Legionnaire's Bracer" (2299) from "Orc Legionnaire" (NPC 21119) in `commons`. Drop cache: 84% chance per kill.
35. Loot "Deathfist Pawn Scalp" (13794) from "Orc Pawn" (NPC 415088) in `mistythicket`. Drop cache: 50% chance per kill.
36. Loot "Snake Fang" (13067) from "A Giant Briar Snake" (NPC 414061) in `toxxulia`. Drop cache: 58.21% chance per kill.
37. Acquisition of "Bone Chips" (13073) is documented under "Silken Tapestry Satchel" (12596); obtain another copy if needed.
38. freeportwest/"Velan Torresk", hand "Snake Fang" (13067) + "Bone Chips" (13073) + "Deathfist Pawn Scalp" (13794) + "Deathfist Pawn Scalp" (13794). Gives "White Training Sash" (10130).
39. Loot "Giant Snake Rattle" (13058) from "A Darkweed Snake" (NPC 457018) in `oldcommons`. Drop cache: 43.94% chance per kill.
40. misty/"Misty", on event signal:33161.
41. Starts timer `Adds`.
42. Spawns "A Scarecrow" (33168) after `misty/misty#timer:Adds`.
43. Loot "Deathfist Slashed Belt" (13916) from "A Scarecrow".
44. Loot "Desert Tarantula Chitin" (20901) from "A Dune Tarantula" (NPC 392086) in `northro`. Drop cache: 45.56% chance per kill.
45. freeportwest/"Velan Torresk", hand "White Training Sash" (10130) + "Giant Snake Rattle" (13058) + "Deathfist Slashed Belt" (13916) + "Desert Tarantula Chitin" (20901). Gives "Yellow Sash of Order" (10131).
46. freeportwest/"Reyia Beslin", hand "Cutthroat Insignia Ring" (1903) + "Legionnaire's Bracer" (2299) + "Yellow Sash of Order" (10131) + "Greater Lightstone" (10400). Gives "Orange Sash of Order" (10132).
47. freeportwest/"Reyia Beslin", hand "Orange Sash of Order" (10132) + "Blackened Wand" (13237) + "Blackened Sapphire" (13238). Gives "Red Sash of Order" (10133).
48. rathemtn/"Brother Zephyl", hand "Red Sash of Order" (10133) + "The Idol" (12317). Gives "Rare Robe Pattern" (12315).
49. Common item: Song: Jonthan's Whistling Warsong (15734). Listed in 8 zones.
50. Acquisition of "Vale Sewing Kit" (92882) is documented under "Silken Tapestry Satchel" (12596); obtain another copy if needed.
51. Loot "Shadow Wolf Pelt" (13779) from "A Shadow Wolf" (NPC 408093) in `commonlands`. Drop cache: 7.64% chance per kill.
52. Common item: Spell: Gather Shadows (15522). Listed in 13 zones.
53. Forage "Spider Silk" (13041) in `mistmoore`.
54. Forage "Spider Silk" (13041) in `mmca`.
55. Forage "Spider Silk" (13041) in `mmcb`.
56. Forage "Spider Silk" (13041) in `mmcc`.
57. Forage "Spider Silk" (13041) in `mmcd`.
58. Forage "Spider Silk" (13041) in `mmce`.
59. Forage "Spider Silk" (13041) in `mmcf`.
60. Forage "Spider Silk" (13041) in `mmcg`.
61. Forage "Spider Silk" (13041) in `mmch`.
62. Forage "Spider Silk" (13041) in `mmci`.
63. Forage "Spider Silk" (13041) in `mmcj`.
64. Combine in "Vale Sewing Kit" (92882): "Spider Silk" (13041). Produces "Silk Swatch" (16482). Requires Tailoring, trivial 15. The combine does not fail.
65. Combine in "Vale Sewing Kit" (92882): "Shadow Wolf Pelt" (13779), "Spell: Gather Shadows" (15522), "Silk Swatch" (16482). Produces "Shadow Silk" (16483). Requires Tailoring, trivial 36.
66. Combine in "Deluxe Sewing Kit" (17966): "Needle of the Void" (12314), "Rare Robe Pattern" (12315), "Song: Jonthan's Whistling Warsong" (15734), "Shadow Silk" (16483). Produces "Robe of the Lost Circle" (12256). Requires Tailoring. The combine does not fail.
67. dreadlands/"Brother Balatin", hand "Robe of the Lost Circle" (12256) + "Metal Pipe" (12979) + "Metal Pipe" (12980). Gives "Robe of the Whistling Fists" (12970).
68. Loot "Immortals" (18195) from "Faerie of Dismay" (NPC 91012) in `skyfire`. Drop cache: 35% chance per kill.
69. erudnext/"Tomekeeper Danl", hand "Immortals" (18195). Gives "Danl's Reference" (1682).
70. timorous/"Lheao", hand "Danl's Reference" (1682) + "Robe of the Whistling Fists" (12970). Gives "Celestial Fists" (1683).
71. Hand "Celestial Fists" (1683) to trakanon/"Kaiaren". Spawns "Kaiaren (True)" (95183). Loot "Rune of Cascade" (65270) from "Kaiaren (True)".
72. 4 alternative loot source(s) also yield Rune of Cascade (65270).
73. Say "Spawnwave" to cazicthule/"Avatar Of Fear".
74. Spawns "a Tentacle Terror" (48252).
75. Loot "Rune of Coruscation" (16631) from "a Tentacle Terror".
76. **Broken:** no event trigger found for `qinimi/execution#timer:startevent`.
77. Spawns "A Kyv Bloodhunter" (281139) after `qinimi/execution#timer:startevent`.
78. Loot "Rune of Flash" (65279) from "A Kyv Bloodhunter".
79. 19 alternative loot source(s) also yield Rune of Flash (65279).
80. lavastorm/"Talwyn Flamecaller", say "Hail". Sets `wiz_epic_pre` to `1`.
81. lavastorm/"Talwyn Flamecaller", say "Test Of Intelligence". Sets `wiz_test_intel` to `1`.
82. Ground spawn of "Empty Jug" (11425) in `katta`.
83. lavastorm/"Talwyn Flamecaller", hand "Empty Jug" (11425). Sets `wiz_test_intel` to `2`.
84. Ground spawn of "Emerald-Tipped Staff" (11419) in `beholder`.
85. lavastorm/"Talwyn Flamecaller", hand "Emerald-Tipped Staff" (11419). Sets `wiz_test_intel` to `3`.
86. Ground spawn of "Meditation Basket" (11282) in `warslikswood`.
87. lavastorm/"Talwyn Flamecaller", hand "Meditation Basket" (11282). Sets `wiz_test_intel` to `4`.
88. Ground spawn of "Platinum Token" (11433) in `pojustice`.
89. lavastorm/"Talwyn Flamecaller", hand "Platinum Token" (11433). Sets `wiz_test_intel` to `5`.
90. Ground spawn of "White Sash" (11413) in `letalis`.
91. lavastorm/"Talwyn Flamecaller", hand "White Sash" (11413). Sets `wiz_test_intel` to `6`.
92. Ground spawn of "Golden Dagger" (11424) in `skyfire`.
93. lavastorm/"Talwyn Flamecaller", hand "Golden Dagger" (11424). Sets `wiz_test_intel` to `7`.
94. Ground spawn of "Ivory Bone" (11436) in `gunthak`.
95. lavastorm/"Talwyn Flamecaller", hand "Ivory Bone" (11436). Sets `wiz_test_intel` to `8`.
96. Ground spawn of "Red Cloth" (11418) in `maiden`.
97. lavastorm/"Talwyn Flamecaller", hand "Red Cloth" (11418). Sets `wiz_test_intel` to `9`.
98. Fish "Worn Turban" (11299) in `potranquility`.
99. lavastorm/"Talwyn Flamecaller", hand "Worn Turban" (11299). Sets `wiz_test_intel` to `10`.
100. Ground spawn of "Old Pipe" (11412) in `cauldron`.
101. lavastorm/"Talwyn Flamecaller", hand "Old Pipe" (11412). Requires `wiz_test_intel` ==10. Gives "Rune of Greater Desiccation" (11439).
102. Kill citymist/"A Black Reaver". Spawns "A Black Reaver" (90004).
103. Loot "Rune of Glint" (65281) from "A Black Reaver".
104. 5 alternative loot source(s) also yield Rune of Glint (65281).
105. Ground spawn of "Icon of the High Scale" (1671) in `citymist`.
106. Hand "Icon of the High Scale" (1671) to hole/"High Scale Kirn". Spawns "High Scale Kirn" (39083). Loot "Engraved Ring" (1681) from "High Scale Kirn".
107. Hand "Engraved Ring" (1681) to citymist/"Neh-Ashiir". Spawns "Neh'Ashir" (90181). Loot "Rune of Impulse" (65282) from "Neh'Ashir".
108. 32 alternative loot source(s) also yield Rune of Impulse (65282).
109. Say "Spawn Devastating Pookas" to tipt/"Rikabi The Riddler".
110. Spawns "A Devastating Pooka" (289037).
111. Loot "Rune of Synergy" (65289) from "A Devastating Pooka".
112. 1 alternative loot source(s) also yield Rune of Synergy (65289).
113. Spawns "a Tae Ew Justicar" (48029) in `cazicthule` on event_spawn.
114. Loot "Rune of Tempest" (65291) from "a Tae Ew Justicar".
115. 9 alternative loot source(s) also yield Rune of Tempest (65291).
116. Spawns "An Ooze" (48004) in `cazicthule` on event_hp.
117. Loot "Rune of Vortex" (65293) from "An Ooze".
118. 2 alternative loot source(s) also yield Rune of Vortex (65293).
119. Loot "Rune of Greater Conflagration" (11442) from "Shar Vinitras" in `akheva`.
120. Combine in "Spell Research Kit" (93492): "Rune of Cascade" (65270), "Rune of Coruscation" (16631), "Rune of Flash" (65279), "Rune of Greater Desiccation" (11439), "Rune of Glint" (65281), "Rune of Impulse" (65282), "Rune of Synergy" (65289), "Rune of Tempest" (65291), "Rune of Vortex" (65293), "Rune of Greater Conflagration" (11442). Produces "Spell: Electrical Charge" (16623). Requires Research, trivial 190. The combine does not fail.

### "Arantir's Ring" (14335)

1. halas/"Arantir Karondor", say "Hail". Gives "Arantir's Ring" (14334).
2. felwithea/"Challice", hand "Arantir's Ring" (14334). Gives "Arantir's Ring" (14335).

### "Note to Arantir" (18168)

1. halas/"Arantir Karondor", say "Gnome". Gives "Note from Arantir" (18169).
2. butcher/"Kandin Firepot", hand "Note from Arantir" (18169). Sets `wizepicK` to `1`.
3. butcher/"Kandin Firepot", say "What Oil". Requires `wizepicK` set. Gives "Golem Sprocket" (14319).
4. Hand "Golem Sprocket" (14319) to fearplane/"A Broken Golem". Spawns "An Enraged Golem" (72106). Loot "Green Oil" (14349) from "An Enraged Golem".
5. butcher/"Kandin Firepot", hand "Green Oil" (14349). Gives "Note to Arantir" (18168).

## `wiz_epic_pre`

Values written: 1, 2, 3, 4.

### 1. talwyn flamecaller — say hail

Zone: `lavastorm`.

> The fire of destruction burns within you, does it not? I can see that your affinity for destructive magic has served you well in your travels. It has served ...

Sets `wiz_epic_pre` to `1`.

- Needs `wiz_epic` unset.
- Needs `wiz_epic_pre` unset.
In script order:

1. Sets `wiz_epic_pre` to `1`.


Subquest `wiz_epic`:

#### `wiz_epic`

Values written: 1, 2, 3, 4, 5.

##### 1. talwyn flamecaller — say hail

Zone: `lavastorm`.

> The fire of destruction burns within you, does it not? I can see that your affinity for destructive magic has served you well in your travels. It has served ...

Sets `wiz_epic` to `1`.

- Needs `wiz_epic` unset.
In script order:

1. Sets `wiz_epic` to `1`.


Alternative or repeat transition to `wiz_epic` = `1` (not an additional required stage).

##### 1. talwyn flamecaller — say hail

Zone: `lavastorm`.

> The fire of destruction burns within you, does it not? I can see that your affinity for destructive magic has served you well in your travels. It has served ...

Sets `wiz_epic` to `1`.

- Needs `wiz_epic_pre` ==5.
In script order:

1. Sets `wiz_epic` to `1`.


This step also depends on `wiz_epic_pre`, shown above.

##### 2. talwyn flamecaller — hand 11445+11448+11474+11576

Zone: `lavastorm`.

Sets `wiz_epic` to `2`.

- Turn in x1: Fluxing Staff (11445).
- Turn in x1: Fluxing Gem (11448).
- Turn in x1: Fluxing Rune (11474).
- Turn in x1: Fluxing Chunk of Ore (11576).
In script order:

1. Sets `wiz_epic` to `2`.
2. Gives Staff of Fluxing Power (11596).


How the items are reached:

- Fluxing Staff (11445)
  - Loot "Fluxing Staff" (11445) from "Girplan Guardian" in `wallofslaughter`.
- Fluxing Gem (11448)
  - Say "Gem" to scarlet/"The Gem Guardian".
  - Spawns "Elite Sun Revenant" (175306).
  - Loot "Fluxing Gem" (11448) from "Elite Sun Revenant".
- Fluxing Rune (11474)
  - Loot "Fluxing Rune" (11474) from "Hobgoblin Horrorfiend" in `ponightmare`.
- Fluxing Chunk of Ore (11576)
  - Ground spawn of "Fluxing Chunk of Ore" (11576) in `dranik`.

##### 3. kalym rasalan — say hail

Zone: `potranquility`.

> Hello

Sets `wiz_epic` to `3`.

In script order:

1. Sets `wiz_epic` to `3`.
2. Gives Silken Tapestry (12593).


##### 4. talwyn flamecaller — hand 12596

Zone: `lavastorm`.

Sets `wiz_epic` to `4`.

- Turn in x1: Silken Tapestry Satchel (12596).
In script order:

1. Sets `wiz_epic_satchel` to `1`.
2. Sets `wiz_epic` to `4`.
3. Gives Silken Tapestry Satchel (12596).


How the items are reached:

- Silken Tapestry Satchel (12596)
  - Prerequisite: "Silken Tapestry Satchel" (12596). See section 0.

##### 5. talwyn flamecaller — hand 16753

Zone: `lavastorm`.

Sets `wiz_epic` to `5`.

- Turn in x1: Full Tapestry Satchel (16753).
In script order:

1. Sets `wiz_epic` to `5`.
2. Gives Staff of Prismatic Power (12665).


How the items are reached:

- Full Tapestry Satchel (16753)
  - Prerequisite: "Full Tapestry Satchel" (16753). See section 0.

##### Steps on `wiz_epic` that do not change it

- `lavastorm` talwyn flamecaller, say hail needs `wiz_epic` unset.
  - Sets `wiz_epic_pre` to `1`.
- `ponightmare` player, on loot needs `wiz_epic` ==1.
  - Sets `wiz_pon_chest` to `1`.
  - Spawns a chest (283157).
- `scarlet` player, on loot needs `wiz_epic` ==1.
  - Sets `wiz_scarlet_chest` to `1`.
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
- `scarlet` the gem guardian, say gem needs `wiz_epic` ==1.
  - Spawns Elite Sun Revenant (175306).
  - Loots Fire Powder (5677).
  - Loots Fluxing Gem (11448).
- `wallofslaughter` player, on loot needs `wiz_epic` ==1.
  - Sets `wiz_wos_chest` to `1`.
  - Spawns a chest (Epic 1.5) (283157).

### 2. talwyn flamecaller — hand 11412

Zone: `lavastorm`.

Sets `wiz_epic_pre` to `2`.

- Needs `wiz_test_intel` ==10.
- Turn in x1: Old Pipe (11412).
In script order:

1. Sets `wiz_epic_pre` to `2`.
2. Gives Rune of Greater Desiccation (11439).


How the items are reached:

- Old Pipe (11412)
  - Ground spawn of "Old Pipe" (11412) in `cauldron`.

Subquest `wiz_test_intel`:

#### `wiz_test_intel`

Values written: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10.

##### 1. talwyn flamecaller — say test of intelligence

Zone: `lavastorm`.

> Through the intelligent use of magic, we are able to become more efficient at what we do. To prove to me that you have this gift, I will need you to work you...

Sets `wiz_test_intel` to `1`.

- Needs `wiz_epic_pre` ==1.
- Needs `wiz_test_intel` unset.
In script order:

1. Sets `wiz_test_intel` to `1`.
2. Gives Old Parchment (11197).


This step also depends on `wiz_epic_pre`, shown above.

##### 2. talwyn flamecaller — hand 11425

Zone: `lavastorm`.

Sets `wiz_test_intel` to `2`.

- Needs `wiz_test_intel` ==1.
- Turn in x1: Empty Jug (11425).
In script order:

1. Sets `wiz_test_intel` to `2`.
2. Gives Old Parchment (11179).


How the items are reached:

- Empty Jug (11425)
  - Ground spawn of "Empty Jug" (11425) in `katta`.

##### 3. talwyn flamecaller — hand 11419

Zone: `lavastorm`.

Sets `wiz_test_intel` to `3`.

- Needs `wiz_test_intel` ==2.
- Turn in x1: Emerald-Tipped Staff (11419).
In script order:

1. Sets `wiz_test_intel` to `3`.
2. Gives Old Parchment (11044).


How the items are reached:

- Emerald-Tipped Staff (11419)
  - Ground spawn of "Emerald-Tipped Staff" (11419) in `beholder`.

##### 4. talwyn flamecaller — hand 11282

Zone: `lavastorm`.

Sets `wiz_test_intel` to `4`.

- Needs `wiz_test_intel` ==3.
- Turn in x1: Meditation Basket (11282).
In script order:

1. Sets `wiz_test_intel` to `4`.
2. Gives Old Parchment (11200).


How the items are reached:

- Meditation Basket (11282)
  - Ground spawn of "Meditation Basket" (11282) in `warslikswood`.

##### 5. talwyn flamecaller — hand 11433

Zone: `lavastorm`.

Sets `wiz_test_intel` to `5`.

- Needs `wiz_test_intel` ==4.
- Turn in x1: Platinum Token (11433).
In script order:

1. Sets `wiz_test_intel` to `5`.
2. Gives Old Parchment (11148).


How the items are reached:

- Platinum Token (11433)
  - Ground spawn of "Platinum Token" (11433) in `pojustice`.

##### 6. talwyn flamecaller — hand 11413

Zone: `lavastorm`.

Sets `wiz_test_intel` to `6`.

- Needs `wiz_test_intel` ==5.
- Turn in x1: White Sash (11413).
In script order:

1. Sets `wiz_test_intel` to `6`.
2. Gives Old Parchment (11194).


How the items are reached:

- White Sash (11413)
  - Ground spawn of "White Sash" (11413) in `letalis`.

##### 7. talwyn flamecaller — hand 11424

Zone: `lavastorm`.

Sets `wiz_test_intel` to `7`.

- Needs `wiz_test_intel` ==6.
- Turn in x1: Golden Dagger (11424).
In script order:

1. Sets `wiz_test_intel` to `7`.
2. Gives Old Parchment (11279).


How the items are reached:

- Golden Dagger (11424)
  - Ground spawn of "Golden Dagger" (11424) in `skyfire`.

##### 8. talwyn flamecaller — hand 11436

Zone: `lavastorm`.

Sets `wiz_test_intel` to `8`.

- Needs `wiz_test_intel` ==7.
- Turn in x1: Ivory Bone (11436).
In script order:

1. Sets `wiz_test_intel` to `8`.
2. Gives Old Parchment (11166).


How the items are reached:

- Ivory Bone (11436)
  - Ground spawn of "Ivory Bone" (11436) in `gunthak`.

##### 9. talwyn flamecaller — hand 11418

Zone: `lavastorm`.

Sets `wiz_test_intel` to `9`.

- Needs `wiz_test_intel` ==8.
- Turn in x1: Red Cloth (11418).
In script order:

1. Sets `wiz_test_intel` to `9`.
2. Gives Old Parchment (11095).


How the items are reached:

- Red Cloth (11418)
  - Ground spawn of "Red Cloth" (11418) in `maiden`.

##### 10. talwyn flamecaller — hand 11299

Zone: `lavastorm`.

Sets `wiz_test_intel` to `10`.

- Needs `wiz_test_intel` ==9.
- Turn in x1: Worn Turban (11299).
In script order:

1. Sets `wiz_test_intel` to `10`.
2. Gives Old Parchment (11102).


How the items are reached:

- Worn Turban (11299)
  - Fish "Worn Turban" (11299) in `potranquility`.

##### Steps on `wiz_test_intel` that do not change it

- `lavastorm` talwyn flamecaller, hand 11412 needs `wiz_test_intel` ==10.
  - Sets `wiz_epic_pre` to `2`.
  - Turn in Old Pipe (11412).
  - Gives Rune of Greater Desiccation (11439).

### 3. talwyn flamecaller — hand 16675

Zone: `lavastorm`.

Sets `wiz_epic_pre` to `3`.

- Needs `wiz_epic_pre` ==2.
- Turn in x1: Cursed Talisman (16675).
In script order:

1. Sets `wiz_epic_pre` to `3`.
2. Gives Cursed Talisman (16675).


How the items are reached:

- Cursed Talisman (16675)
  - Kill lakeofillomen/. Spawns "A Scorpion Hatchling" (85240).
  - Loot "Cursed Talisman" (16675) from "A Scorpion Hatchling".

### 4. talwyn flamecaller — hand 16623

Zone: `lavastorm`.

Sets `wiz_epic_pre` to `4`.

- Needs `wiz_epic_pre` ==3.
- Needs `wiz_epic_pre` ==4.
- Turn in x1: Spell: Electrical Charge (16623).
In script order:

1. Sets `wiz_epic_pre` to `4`.
2. Gives Spell: Electrical Charge (16623).


How the items are reached:

- Spell: Electrical Charge (16623)
  - Prerequisite: "Spell: Electrical Charge" (16623). See section 0.

### Steps on `wiz_epic_pre` that do not change it

- `lavastorm` talwyn flamecaller, say hail needs `wiz_epic_pre` ==5.
  - Sets `wiz_epic` to `1`.
- `lavastorm` talwyn flamecaller, say test of intelligence needs `wiz_epic_pre` ==1.
  - Sets `wiz_test_intel` to `1`.
  - Gives Old Parchment (11197).

## `wiz_epic`

See `wiz_epic` earlier in this file.

## `wizepic`

Values written: 1.

### 1. camin — hand platinum:1000

Zone: `erudnext`.

Sets `wizepic` to `1`.

- Turn in 1000 platinum.
In script order:

1. Sets `wizepic` to `1`.


### Steps on `wizepic` that do not change it

- `erudnext` camin, hand 14330 needs `wizepic` ==1.
  - Turn in Ro's Breath (14330).
  - Gives Ro's Breath (14331).

## `wizepicA`

Values written: 1.

### 1. arantir karondor — hand 14335

Zone: `halas`.

Sets `wizepicA` to `1`.

- Turn in x1: Arantir's Ring (14335).
In script order:

1. Sets `wizepicA` to `1`.


How the items are reached:

- Arantir's Ring (14335)
  - Prerequisite: "Arantir's Ring" (14335). See section 0.

Alternative or repeat transition to `wizepicA` = `1` (not an additional required stage).

### 1. dargon — hand 14335

Zone: `halas`.

Sets `wizepicA` to `1`.

- Turn in x1: Arantir's Ring (14335).
In script order:

1. Sets `wizepicA` to `1`.
2. Spawns Arantir Karondor (29089).


How the items are reached:

- Arantir's Ring (14335)
  - Prerequisite: "Arantir's Ring" (14335). See section 0.

## `wizepicB`

Values written: 1.

### 1. arantir karondor — hand 18168

Zone: `halas`.

Sets `wizepicB` to `1`.

- Turn in x1: Note to Arantir (18168).
In script order:

1. Sets `wizepicB` to `1`.


How the items are reached:

- Note to Arantir (18168)
  - Prerequisite: "Note to Arantir" (18168). See section 0.

Alternative or repeat transition to `wizepicB` = `1` (not an additional required stage).

### 1. dargon — hand 18168

Zone: `halas`.

Sets `wizepicB` to `1`.

- Turn in x1: Note to Arantir (18168).
In script order:

1. Sets `wizepicB` to `1`.
2. Spawns Arantir Karondor (29089).


How the items are reached:

- Note to Arantir (18168)
  - Prerequisite: "Note to Arantir" (18168). See section 0.

## `wizepicK`

Values written: 1.

### 1. kandin firepot — hand 18169

Zone: `butcher`.

Sets `wizepicK` to `1`.

- Turn in x1: Note from Arantir (18169).
In script order:

1. Sets `wizepicK` to `1`.


How the items are reached:

- Note from Arantir (18169)
  - Given by halas/"Arantir Karondor", say "Gnome".

### Steps on `wizepicK` that do not change it

- `butcher` kandin firepot, say what oil needs `wizepicK` set.
  - Gives Golem Sprocket (14319).

## `wiz_epic20`

Values written: 1, 2, 3, 4.

### 1. talwyn flamecaller — say hail

Zone: `lavastorm`.

> The fire of destruction burns within you, does it not? I can see that your affinity for destructive magic has served you well in your travels. It has served ...

Sets `wiz_epic20` to `1`.

- Needs `wiz_epic20` unset.
In script order:

1. Sets `wiz_epic20` to `1`.


### 2. grathnok gilforgan — say intricate horn of galien

Zone: `draniksscar`.

> This precious artifact was placed on our largest tower, where its resonating voice stretched across the planes and through the mountains to rally our troops ...

Sets `wiz_epic20` to `2`.

- Needs `wiz_epic20` ==1.
- Needs `wiz_epic20` set.
- Needs `wiz_epic20` >=1.
In script order:

1. Sets `wiz_epic20` to `2`.


### 3. grathnok gilforgan — hand 15825

Zone: `draniksscar`.

Sets `wiz_epic20` to `3`.

- Needs `wiz_epic20` ==2.
- Turn in x1: Intricate Horn of Galien (15825).
In script order:

1. Sets `wiz_epic20` to `3`.


How the items are reached:

- Intricate Horn of Galien (15825)
  - Loot "Intricate Horn of Galien" (15825) from "Lightningcaller Vhalek" in `provinggrounds`.

### 4. talwyn flamecaller — hand 47100

Zone: `lavastorm`.

Sets `wiz_epic20` to `4`.

- Needs `wiz_epic20` set.
- Needs `wiz_epic20` >=3.
- Turn in x1: Globe of Discordant Energy (47100).
In script order:

1. Sets `wiz_epic20` to `4`.
2. Gives Broken Orb of Discordant Energy (15836).
3. Gives Broken Orb of Discordant Energy (16147).


How the items are reached:

- Globe of Discordant Energy (47100)
  - Say "Check Lorb" to anguish/"Zone Status".
  - Spawns "Orb of Discordant Energy" (317087).
  - Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy".
  - 4 alternative loot source(s) also yield Globe of Discordant Energy (47100).

### Steps on `wiz_epic20` that do not change it

- `lavastorm` talwyn flamecaller, hand 12665+16334+16451 needs `wiz_epic20` ==4.
  - Turn in Infused Orb of Discordant Energy (16451).
  - Turn in Infused Orb of Discordant Energy (16334).
  - Turn in Staff of Prismatic Power (12665).
  - Gives Staff of Phenomenal Power (16576).
- `provinggrounds` player, on loot needs `wiz_epic20` set.
  - Sets `wiz20_mpg_chest` to `1`.
  - Spawns a chest (epic 2.0) (893).

## Other flags touched along the way

- `wiz20_mpg_chest` set to 1 at provinggrounds/player.
- `wiz_epic_satchel` set to 1 at lavastorm/talwyn flamecaller.
- `wiz_epic_shard` set to 1 at lavastorm/talwyn flamecaller.
- `wiz_epic_wisp` set to 1 at lavastorm/talwyn flamecaller.
