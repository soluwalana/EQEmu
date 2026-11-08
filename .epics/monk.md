# Monk

Steps taken from the quest graph only. **Broken** means the graph has no edge for that value or that item.

Flags with writes: `MnkPre`, `monk_epic`, `mnk_epic20`.

## 0. Prerequisites

Each list is the order you obtain that item. Later steps point here instead of repeating the chain.

### "Celestial Fists" (10652)

1. Kill lakeofillomen/"Vorash". Spawns "Xenevorash" (85208).
2. Loot "Demon Fangs" (1688) from "Xenevorash".
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
37. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `steamfont`.
38. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `tox`.
39. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `toxxulia`.
40. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
41. freeportwest/"Velan Torresk", hand "Snake Fang" (13067) + "Bone Chips" (13073) + "Deathfist Pawn Scalp" (13794) + "Deathfist Pawn Scalp" (13794). Gives "White Training Sash" (10130).
42. Loot "Giant Snake Rattle" (13058) from "A Darkweed Snake" (NPC 457018) in `oldcommons`. Drop cache: 43.94% chance per kill.
43. misty/"Misty", on event signal:33161.
44. Starts timer `Adds`.
45. Spawns "A Scarecrow" (33168) after `misty/misty#timer:Adds`.
46. Loot "Deathfist Slashed Belt" (13916) from "A Scarecrow".
47. Loot "Desert Tarantula Chitin" (20901) from "A Dune Tarantula" (NPC 392086) in `northro`. Drop cache: 45.56% chance per kill.
48. freeportwest/"Velan Torresk", hand "White Training Sash" (10130) + "Giant Snake Rattle" (13058) + "Deathfist Slashed Belt" (13916) + "Desert Tarantula Chitin" (20901). Gives "Yellow Sash of Order" (10131).
49. freeportwest/"Reyia Beslin", hand "Cutthroat Insignia Ring" (1903) + "Legionnaire's Bracer" (2299) + "Yellow Sash of Order" (10131) + "Greater Lightstone" (10400). Gives "Orange Sash of Order" (10132).
50. freeportwest/"Reyia Beslin", hand "Orange Sash of Order" (10132) + "Blackened Wand" (13237) + "Blackened Sapphire" (13238). Gives "Red Sash of Order" (10133).
51. rathemtn/"Brother Zephyl", hand "Red Sash of Order" (10133) + "The Idol" (12317). Gives "Rare Robe Pattern" (12315).
52. Common item: Song: Jonthan's Whistling Warsong (15734). Listed in 8 zones.
53. Common item: Needle Mold (12019). Listed in 32 zones.
54. Common item: Thimble Mold (12057). Listed in 32 zones.
55. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
56. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). The combine does not fail.
57. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
58. Combine in Forge (17): "Fine Steel Two Handed Sword" (5351), "Water Flask" (13006). Produces "Small Brick of High Quality Ore" (10468) x2, "Small Piece of High Quality Ore" (22229). Requires Blacksmithing, trivial 21.
59. Combine in Forge (17): "Smithing Chisel" (7052), "Small Brick of High Quality Ore" (10468). Hands back "Smithing Chisel" (7052). Produces "Small Piece of High Quality Ore" (22229) x2. Requires Blacksmithing, trivial 27.
60. 4 other recipes also produce Small Piece of High Quality Ore (22229).
61. Combine in Royal Qeynos Forge (40): "Small Piece of High Quality Ore" (22229), "Water Flask" (13006). Produces "High Quality Metal Bits" (22230). Requires Blacksmithing, trivial 20.
62. Combine in Vale Forge (49): "Needle Mold" (12019), "Thimble Mold" (12057), "Water Flask" (13006), "High Quality Metal Bits" (22230). Produces "Vale Sewing Kit" (92882). Requires Blacksmithing, trivial 162.
63. Loot "Shadow Wolf Pelt" (13779) from "A Shadow Wolf" (NPC 408093) in `commonlands`. Drop cache: 7.64% chance per kill.
64. Common item: Spell: Gather Shadows (15522). Listed in 13 zones.
65. Forage "Spider Silk" (13041) in `mistmoore`.
66. Forage "Spider Silk" (13041) in `mmca`.
67. Forage "Spider Silk" (13041) in `mmcb`.
68. Forage "Spider Silk" (13041) in `mmcc`.
69. Forage "Spider Silk" (13041) in `mmcd`.
70. Forage "Spider Silk" (13041) in `mmce`.
71. Forage "Spider Silk" (13041) in `mmcf`.
72. Forage "Spider Silk" (13041) in `mmcg`.
73. Forage "Spider Silk" (13041) in `mmch`.
74. Forage "Spider Silk" (13041) in `mmci`.
75. Forage "Spider Silk" (13041) in `mmcj`.
76. Combine in "Vale Sewing Kit" (92882): "Spider Silk" (13041). Produces "Silk Swatch" (16482). Requires Tailoring, trivial 15. The combine does not fail.
77. Combine in "Vale Sewing Kit" (92882): "Shadow Wolf Pelt" (13779), "Spell: Gather Shadows" (15522), "Silk Swatch" (16482). Produces "Shadow Silk" (16483). Requires Tailoring, trivial 36.
78. Combine in "Deluxe Sewing Kit" (17966): "Needle of the Void" (12314), "Rare Robe Pattern" (12315), "Song: Jonthan's Whistling Warsong" (15734), "Shadow Silk" (16483). Produces "Robe of the Lost Circle" (12256). Requires Tailoring. The combine does not fail.
79. dreadlands/"Brother Balatin", hand "Robe of the Lost Circle" (12256) + "Metal Pipe" (12979) + "Metal Pipe" (12980). Gives "Robe of the Whistling Fists" (12970).
80. Loot "Immortals" (18195) from "Faerie of Dismay" (NPC 91012) in `skyfire`. Drop cache: 35% chance per kill.
81. erudnext/"Tomekeeper Danl", hand "Immortals" (18195). Gives "Danl's Reference" (1682).
82. timorous/"Lheao", hand "Danl's Reference" (1682) + "Robe of the Whistling Fists" (12970). Gives "Celestial Fists" (1683).
83. trakanon/"Kaiaren", hand "Celestial Fists" (1683). Gives "Book of Celestial Fists" (1689).
84. trakanon/"Kaiaren", hand "Demon Fangs" (1688) + "Book of Celestial Fists" (1689). Gives "Celestial Fists" (10652).

### "Danl's Missing Book" (48132)

1. Ground spawn of "Section of Parchment" (48104) in `gunthak`.
2. Ground spawn of "Section of Parchment" (48105) in `hole`.
3. Ground spawn of "Section of Parchment" (48106) in `charasis`.
4. Ground spawn of "Section of Parchment" (48107) in `akheva`.
5. shadowhaven/"Researcher Relreom", hand "Section of Parchment" (48104) + "Section of Parchment" (48105) + "Section of Parchment" (48106) + "Section of Parchment" (48107). Gives "Danl's Missing Book" (48132).

### "Letter to Stremstin" (48128)

1. bazaar/"Eryke Stremstin", hand "Letter to Stremstin" (48128). Sets `monk_epic` to `6`.
2. Loot "Sunless Nectar" (48117) from "An Ancient Shrieker" (NPC 164049) in `thedeep`. Drop cache: 11.17% chance per kill.
3. Common item: Spices (13425). Listed in 39 zones.
4. Common item: Pie Tin Mold (12021). Listed in 23 zones.
5. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
6. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `steamfont`.
7. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `tox`.
8. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `toxxulia`.
9. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
10. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). The combine does not fail.
11. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
12. kaladimb/"Jeet", say "Collect The Gnome Profit". Gives "Scrubber Key" (12164).
13. akanon/"Clockwork Scrubber", hand "Scrubber Key" (12164). Gives "Gnome Take" (12167).
14. kaladimb/"Jeet", hand "Gnome Take" (12167). Gives "Small Piece of Ore" (10500).
15. Combine in Forge (17): "Small Piece of Ore" (10500), "Water Flask" (13006). Produces "Metal Bits" (16905) x2. Requires Blacksmithing, trivial 18.
16. Common item: Quality Firing Sheet (16907). Listed in 32 zones.
17. Combine in Pottery Wheel (21): "Small Block of Clay" (16900), "Water Flask" (13006). Produces "Block of Clay" (16901). Requires Pottery, trivial 21.
18. Combine in Pottery Wheel (21): "Block of Clay" (16901), "Water Flask" (13006). Produces "Large Block of Clay" (16902). Requires Pottery, trivial 21.
19. Combine in Pottery Wheel (21): "Water Flask" (13006), "Large Block of Clay" (16902). Produces "Block of Clay" (16901) x2. Requires Pottery, trivial 21.
20. Combine in Pottery Wheel (21): "Water Flask" (13006), "Block of Clay" (16901). Produces "Small Block of Clay" (16900) x3. Requires Pottery, trivial 21.
21. Common item: Ceramic Lining Sketch (16964). Listed in 40 zones.
22. Combine in Pottery Wheel (21): "Water Flask" (13006), "Small Block of Clay" (16900), "Ceramic Lining Sketch" (16964). Produces "Unfired Ceramic Lining" (16946). Requires Pottery, trivial 36.
23. Combine in Kiln (22): "Quality Firing Sheet" (16907), "Unfired Ceramic Lining" (16946). Produces "Ceramic Lining" (16947). Requires Pottery, trivial 17.
24. Combine in Forge (17): "Pie Tin Mold" (12021), "Water Flask" (13006), "Metal Bits" (16905), "Ceramic Lining" (16947). Produces "Pie Tin" (13438). Requires Blacksmithing, trivial 35.
25. Common item: High Quality Firing Sheet (16908). Listed in 34 zones.
26. Common item: Pie Tin Sketch (16958). Listed in 29 zones.
27. Combine in Pottery Wheel (21): "Block of Clay" (16901), "Water Flask" (13006), "Pie Tin Sketch" (16958). Produces "Unfired Pie Tin" (16926). Requires Pottery, trivial 115.
28. Combine in Kiln (22): "High Quality Firing Sheet" (16908), "Unfired Pie Tin" (16926). Produces "Pie Tin" (13438). Requires Pottery, trivial 15.
29. Combine in Oven (15): "Sunless Nectar" (48117), "Spices" (13425), "Pie Tin" (13438). Produces "Sugar and Spice Nectar Pie" (48119). Requires Baking, trivial 176.
30. Common item: Spit (17947). Listed in 34 zones.
31. Combine in "Mixing Bowl" (17906): "Bottle of Milk" (13087), "Snake Egg" (13088), "Cup of Flour" (13193). Produces "Clump of Dough" (13090). Requires Baking, trivial 17.
32. Combine in "Mixing Bowl" (17906): "Bottle of Milk" (13087), "Cup of Flour" (13193), "Aviak Eggs" (14968). Produces "Clump of Dough" (13090) x5. Requires Baking, trivial 17.
33. 10 other recipes also produce Clump of Dough (13090).
34. Common item: Bread Tin Mold (12025). Listed in 23 zones.
35. Combine in Forge (17): "Bread Tin Mold" (12025), "Water Flask" (13006), "Metal Bits" (16905), "Ceramic Lining" (16947). Produces "Bread Tin" (13440). Requires Blacksmithing, trivial 38.
36. Combine in "Spit" (17947): "Clump of Dough" (13090), "Bread Tin" (13440). Hands back "Bread Tin" (13440). Produces "Loaf of Bread" (13015). Requires Baking, trivial 115.
37. Common item: Cheese (8160). Listed in 9 zones.
38. Combine in "Spit" (17947): "Loaf of Bread" (13015), "Frosting" (13429), "Berry Ice Cream" (75818). Produces "Vegetable Oil" (20386) x2, "Berry Ice Cream Crunch" (75828). Requires Baking, trivial 162.
39. Combine in "Spit" (17947): "Loaf of Bread" (13015), "Frosting" (13429), "Berry Walnut Ice Cream" (75822). Produces "Vegetable Oil" (20386) x2, "Berry Walnut Crunch" (75832). Requires Baking, trivial 162.
40. 7 other recipes also produce Vegetable Oil (20386).
41. Common item: Garlic (58280). Listed in 5 zones.
42. Combine in Brew Barrel (19): "Vegetable Oil" (20386), "Garlic" (58280). Produces "Grilling Sauce" (58265). Requires Brewing, trivial 54.
43. Loot "Aged Piece of Meat" (48118) from "Ancient Nobleman" in `veksar`.
44. Combine in Oven (15): "Loaf of Bread" (13015), "Cheese" (8160), "Grilling Sauce" (58265), "Aged Piece of Meat" (48118). Produces "Aged Meat and Cheese Sandwich" (48120). Requires Baking, trivial 176.
45. oceanoftears/"Kaiaren", hand "Sugar and Spice Nectar Pie" (48119) + "Aged Meat and Cheese Sandwich" (48120). Sets `mnk_epic20` to `2`.
46. potranquility/"Vortix", hand "Initiate's Sash of the Celestial Order" (48127). Sets `monk_epic` to `7`.
47. Loot "Kaiaren's Mind" (48137) from "Kragsmash" in `bloodfields`.
48. Loot "Kaiaren's Body" (48138) from "Windrush" in `harbingers`.
49. potranquility/"Vortix", hand "Kaiaren's Mind" (48137) + "Kaiaren's Body" (48138). Sets `monk_epic` to `8`.
50. Loot "Scribed Note" (20435) from "The Keeper" in `bloodfields`.
51. potranquility/"Vortix", hand "Scribed Note" (20435). Sets `monk_epic` to `9`.
52. Unresolved cyclic prerequisite: `mnk_epic20` >=2.
53. oceanoftears/"Kaiaren", say "Choose To Continue". Sets `mnk_epic20` to `3`.
54. oceanoftears/"Kaiaren", say "Choose To Continue". Requires `mnk_epic20` ==2. Requires `mnk_epic20` set. Requires `monk_epic` ==9. Requires `mnk_epic20` >=2. Gives "Initiate's Sash of the Celestial Order" (48127).
55. lakerathe/"Vortix", say "Diary". Sets `monk_epic` to `4`.
56. Loot "1/2 of Kaiaren's Diary" (48109) from "Wygrish" in `sirens`.
57. Loot "1/2 of Kaiaren's Diary" (48110) from "Quigli" in `dulak`.
58. potranquility/"Vortix", hand "1/2 of Kaiaren's Diary" (48109) + "1/2 of Kaiaren's Diary" (48110). Sets `monk_epic` to `5`.
59. Spawns "Disciple of Moon" (120138) in `westwastes` on enter.
60. Loot "Symbol of Moon" (48111) from "Disciple of Moon".
61. potranquility/"Vortix", say "Hail". Requires `monk_epic` >=5. Gives "Letter to Stremstin" (48128).

### "Initiate's Sash of the Celestial Order" (48127)

1. Loot "Sunless Nectar" (48117) from "An Ancient Shrieker" (NPC 164049) in `thedeep`. Drop cache: 11.17% chance per kill.
2. Common item: Spices (13425). Listed in 39 zones.
3. Common item: Pie Tin Mold (12021). Listed in 23 zones.
4. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
5. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `steamfont`.
6. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `tox`.
7. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `toxxulia`.
8. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
9. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). The combine does not fail.
10. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
11. kaladimb/"Jeet", say "Collect The Gnome Profit". Gives "Scrubber Key" (12164).
12. akanon/"Clockwork Scrubber", hand "Scrubber Key" (12164). Gives "Gnome Take" (12167).
13. kaladimb/"Jeet", hand "Gnome Take" (12167). Gives "Small Piece of Ore" (10500).
14. Combine in Forge (17): "Small Piece of Ore" (10500), "Water Flask" (13006). Produces "Metal Bits" (16905) x2. Requires Blacksmithing, trivial 18.
15. Common item: Quality Firing Sheet (16907). Listed in 32 zones.
16. Combine in Pottery Wheel (21): "Small Block of Clay" (16900), "Water Flask" (13006). Produces "Block of Clay" (16901). Requires Pottery, trivial 21.
17. Combine in Pottery Wheel (21): "Block of Clay" (16901), "Water Flask" (13006). Produces "Large Block of Clay" (16902). Requires Pottery, trivial 21.
18. Combine in Pottery Wheel (21): "Water Flask" (13006), "Large Block of Clay" (16902). Produces "Block of Clay" (16901) x2. Requires Pottery, trivial 21.
19. Combine in Pottery Wheel (21): "Water Flask" (13006), "Block of Clay" (16901). Produces "Small Block of Clay" (16900) x3. Requires Pottery, trivial 21.
20. Common item: Ceramic Lining Sketch (16964). Listed in 40 zones.
21. Combine in Pottery Wheel (21): "Water Flask" (13006), "Small Block of Clay" (16900), "Ceramic Lining Sketch" (16964). Produces "Unfired Ceramic Lining" (16946). Requires Pottery, trivial 36.
22. Combine in Kiln (22): "Quality Firing Sheet" (16907), "Unfired Ceramic Lining" (16946). Produces "Ceramic Lining" (16947). Requires Pottery, trivial 17.
23. Combine in Forge (17): "Pie Tin Mold" (12021), "Water Flask" (13006), "Metal Bits" (16905), "Ceramic Lining" (16947). Produces "Pie Tin" (13438). Requires Blacksmithing, trivial 35.
24. Common item: High Quality Firing Sheet (16908). Listed in 34 zones.
25. Common item: Pie Tin Sketch (16958). Listed in 29 zones.
26. Combine in Pottery Wheel (21): "Block of Clay" (16901), "Water Flask" (13006), "Pie Tin Sketch" (16958). Produces "Unfired Pie Tin" (16926). Requires Pottery, trivial 115.
27. Combine in Kiln (22): "High Quality Firing Sheet" (16908), "Unfired Pie Tin" (16926). Produces "Pie Tin" (13438). Requires Pottery, trivial 15.
28. Combine in Oven (15): "Sunless Nectar" (48117), "Spices" (13425), "Pie Tin" (13438). Produces "Sugar and Spice Nectar Pie" (48119). Requires Baking, trivial 176.
29. Common item: Spit (17947). Listed in 34 zones.
30. Combine in "Mixing Bowl" (17906): "Bottle of Milk" (13087), "Snake Egg" (13088), "Cup of Flour" (13193). Produces "Clump of Dough" (13090). Requires Baking, trivial 17.
31. Combine in "Mixing Bowl" (17906): "Bottle of Milk" (13087), "Cup of Flour" (13193), "Aviak Eggs" (14968). Produces "Clump of Dough" (13090) x5. Requires Baking, trivial 17.
32. 10 other recipes also produce Clump of Dough (13090).
33. Common item: Bread Tin Mold (12025). Listed in 23 zones.
34. Combine in Forge (17): "Bread Tin Mold" (12025), "Water Flask" (13006), "Metal Bits" (16905), "Ceramic Lining" (16947). Produces "Bread Tin" (13440). Requires Blacksmithing, trivial 38.
35. Combine in "Spit" (17947): "Clump of Dough" (13090), "Bread Tin" (13440). Hands back "Bread Tin" (13440). Produces "Loaf of Bread" (13015). Requires Baking, trivial 115.
36. Common item: Cheese (8160). Listed in 9 zones.
37. Combine in "Spit" (17947): "Loaf of Bread" (13015), "Frosting" (13429), "Berry Ice Cream" (75818). Produces "Vegetable Oil" (20386) x2, "Berry Ice Cream Crunch" (75828). Requires Baking, trivial 162.
38. Combine in "Spit" (17947): "Loaf of Bread" (13015), "Frosting" (13429), "Berry Walnut Ice Cream" (75822). Produces "Vegetable Oil" (20386) x2, "Berry Walnut Crunch" (75832). Requires Baking, trivial 162.
39. 7 other recipes also produce Vegetable Oil (20386).
40. Common item: Garlic (58280). Listed in 5 zones.
41. Combine in Brew Barrel (19): "Vegetable Oil" (20386), "Garlic" (58280). Produces "Grilling Sauce" (58265). Requires Brewing, trivial 54.
42. Loot "Aged Piece of Meat" (48118) from "Ancient Nobleman" in `veksar`.
43. Combine in Oven (15): "Loaf of Bread" (13015), "Cheese" (8160), "Grilling Sauce" (58265), "Aged Piece of Meat" (48118). Produces "Aged Meat and Cheese Sandwich" (48120). Requires Baking, trivial 176.
44. oceanoftears/"Kaiaren", hand "Sugar and Spice Nectar Pie" (48119) + "Aged Meat and Cheese Sandwich" (48120). Sets `mnk_epic20` to `2`.
45. bazaar/"Eryke Stremstin", hand "Letter to Stremstin" (48128). Sets `monk_epic` to `6`.
46. potranquility/"Vortix", hand "Initiate's Sash of the Celestial Order" (48127). Sets `monk_epic` to `7`.
47. Loot "Kaiaren's Mind" (48137) from "Kragsmash" in `bloodfields`.
48. Loot "Kaiaren's Body" (48138) from "Windrush" in `harbingers`.
49. potranquility/"Vortix", hand "Kaiaren's Mind" (48137) + "Kaiaren's Body" (48138). Sets `monk_epic` to `8`.
50. Loot "Scribed Note" (20435) from "The Keeper" in `bloodfields`.
51. potranquility/"Vortix", hand "Scribed Note" (20435). Sets `monk_epic` to `9`.
52. lakerathe/"Vortix", say "Diary". Sets `monk_epic` to `4`.
53. Loot "1/2 of Kaiaren's Diary" (48109) from "Wygrish" in `sirens`.
54. Loot "1/2 of Kaiaren's Diary" (48110) from "Quigli" in `dulak`.
55. potranquility/"Vortix", hand "1/2 of Kaiaren's Diary" (48109) + "1/2 of Kaiaren's Diary" (48110). Sets `monk_epic` to `5`.
56. Spawns "Disciple of Moon" (120138) in `westwastes` on enter.
57. Loot "Symbol of Moon" (48111) from "Disciple of Moon".
58. potranquility/"Vortix", say "Hail". Requires `monk_epic` >=5. Gives "Letter to Stremstin" (48128).
59. Unresolved cyclic prerequisite: `mnk_epic20` >=2.
60. oceanoftears/"Kaiaren", say "Choose To Continue". Sets `mnk_epic20` to `3`.
61. oceanoftears/"Kaiaren", say "Choose To Continue". Requires `mnk_epic20` ==2. Requires `mnk_epic20` set. Requires `monk_epic` ==9. Requires `mnk_epic20` >=2. Gives "Initiate's Sash of the Celestial Order" (48127).

### "Sugar and Spice Nectar Pie" (48119)

1. Loot "Sunless Nectar" (48117) from "An Ancient Shrieker" (NPC 164049) in `thedeep`. Drop cache: 11.17% chance per kill.
2. Common item: Spices (13425). Listed in 39 zones.
3. Common item: Pie Tin Mold (12021). Listed in 23 zones.
4. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
5. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `steamfont`.
6. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `tox`.
7. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `toxxulia`.
8. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
9. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). The combine does not fail.
10. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
11. kaladimb/"Jeet", say "Collect The Gnome Profit". Gives "Scrubber Key" (12164).
12. akanon/"Clockwork Scrubber", hand "Scrubber Key" (12164). Gives "Gnome Take" (12167).
13. kaladimb/"Jeet", hand "Gnome Take" (12167). Gives "Small Piece of Ore" (10500).
14. Combine in Forge (17): "Small Piece of Ore" (10500), "Water Flask" (13006). Produces "Metal Bits" (16905) x2. Requires Blacksmithing, trivial 18.
15. Common item: Quality Firing Sheet (16907). Listed in 32 zones.
16. Combine in Pottery Wheel (21): "Small Block of Clay" (16900), "Water Flask" (13006). Produces "Block of Clay" (16901). Requires Pottery, trivial 21.
17. Combine in Pottery Wheel (21): "Block of Clay" (16901), "Water Flask" (13006). Produces "Large Block of Clay" (16902). Requires Pottery, trivial 21.
18. Combine in Pottery Wheel (21): "Water Flask" (13006), "Large Block of Clay" (16902). Produces "Block of Clay" (16901) x2. Requires Pottery, trivial 21.
19. Combine in Pottery Wheel (21): "Water Flask" (13006), "Block of Clay" (16901). Produces "Small Block of Clay" (16900) x3. Requires Pottery, trivial 21.
20. Common item: Ceramic Lining Sketch (16964). Listed in 40 zones.
21. Combine in Pottery Wheel (21): "Water Flask" (13006), "Small Block of Clay" (16900), "Ceramic Lining Sketch" (16964). Produces "Unfired Ceramic Lining" (16946). Requires Pottery, trivial 36.
22. Combine in Kiln (22): "Quality Firing Sheet" (16907), "Unfired Ceramic Lining" (16946). Produces "Ceramic Lining" (16947). Requires Pottery, trivial 17.
23. Combine in Forge (17): "Pie Tin Mold" (12021), "Water Flask" (13006), "Metal Bits" (16905), "Ceramic Lining" (16947). Produces "Pie Tin" (13438). Requires Blacksmithing, trivial 35.
24. Common item: High Quality Firing Sheet (16908). Listed in 34 zones.
25. Common item: Pie Tin Sketch (16958). Listed in 29 zones.
26. Combine in Pottery Wheel (21): "Block of Clay" (16901), "Water Flask" (13006), "Pie Tin Sketch" (16958). Produces "Unfired Pie Tin" (16926). Requires Pottery, trivial 115.
27. Combine in Kiln (22): "High Quality Firing Sheet" (16908), "Unfired Pie Tin" (16926). Produces "Pie Tin" (13438). Requires Pottery, trivial 15.
28. Combine in Oven (15): "Sunless Nectar" (48117), "Spices" (13425), "Pie Tin" (13438). Produces "Sugar and Spice Nectar Pie" (48119). Requires Baking, trivial 176.

### "Aged Meat and Cheese Sandwich" (48120)

1. Common item: Spit (17947). Listed in 34 zones.
2. Combine in "Mixing Bowl" (17906): "Bottle of Milk" (13087), "Snake Egg" (13088), "Cup of Flour" (13193). Produces "Clump of Dough" (13090). Requires Baking, trivial 17.
3. Combine in "Mixing Bowl" (17906): "Bottle of Milk" (13087), "Cup of Flour" (13193), "Aviak Eggs" (14968). Produces "Clump of Dough" (13090) x5. Requires Baking, trivial 17.
4. 10 other recipes also produce Clump of Dough (13090).
5. Common item: Bread Tin Mold (12025). Listed in 23 zones.
6. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
7. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `steamfont`.
8. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `tox`.
9. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `toxxulia`.
10. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
11. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). The combine does not fail.
12. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
13. kaladimb/"Jeet", say "Collect The Gnome Profit". Gives "Scrubber Key" (12164).
14. akanon/"Clockwork Scrubber", hand "Scrubber Key" (12164). Gives "Gnome Take" (12167).
15. kaladimb/"Jeet", hand "Gnome Take" (12167). Gives "Small Piece of Ore" (10500).
16. Combine in Forge (17): "Small Piece of Ore" (10500), "Water Flask" (13006). Produces "Metal Bits" (16905) x2. Requires Blacksmithing, trivial 18.
17. Common item: Quality Firing Sheet (16907). Listed in 32 zones.
18. Combine in Pottery Wheel (21): "Small Block of Clay" (16900), "Water Flask" (13006). Produces "Block of Clay" (16901). Requires Pottery, trivial 21.
19. Combine in Pottery Wheel (21): "Block of Clay" (16901), "Water Flask" (13006). Produces "Large Block of Clay" (16902). Requires Pottery, trivial 21.
20. Combine in Pottery Wheel (21): "Water Flask" (13006), "Large Block of Clay" (16902). Produces "Block of Clay" (16901) x2. Requires Pottery, trivial 21.
21. Combine in Pottery Wheel (21): "Water Flask" (13006), "Block of Clay" (16901). Produces "Small Block of Clay" (16900) x3. Requires Pottery, trivial 21.
22. Common item: Ceramic Lining Sketch (16964). Listed in 40 zones.
23. Combine in Pottery Wheel (21): "Water Flask" (13006), "Small Block of Clay" (16900), "Ceramic Lining Sketch" (16964). Produces "Unfired Ceramic Lining" (16946). Requires Pottery, trivial 36.
24. Combine in Kiln (22): "Quality Firing Sheet" (16907), "Unfired Ceramic Lining" (16946). Produces "Ceramic Lining" (16947). Requires Pottery, trivial 17.
25. Combine in Forge (17): "Bread Tin Mold" (12025), "Water Flask" (13006), "Metal Bits" (16905), "Ceramic Lining" (16947). Produces "Bread Tin" (13440). Requires Blacksmithing, trivial 38.
26. Combine in "Spit" (17947): "Clump of Dough" (13090), "Bread Tin" (13440). Hands back "Bread Tin" (13440). Produces "Loaf of Bread" (13015). Requires Baking, trivial 115.
27. Common item: Cheese (8160). Listed in 9 zones.
28. Combine in "Spit" (17947): "Loaf of Bread" (13015), "Frosting" (13429), "Berry Ice Cream" (75818). Produces "Vegetable Oil" (20386) x2, "Berry Ice Cream Crunch" (75828). Requires Baking, trivial 162.
29. Combine in "Spit" (17947): "Loaf of Bread" (13015), "Frosting" (13429), "Berry Walnut Ice Cream" (75822). Produces "Vegetable Oil" (20386) x2, "Berry Walnut Crunch" (75832). Requires Baking, trivial 162.
30. 7 other recipes also produce Vegetable Oil (20386).
31. Common item: Garlic (58280). Listed in 5 zones.
32. Combine in Brew Barrel (19): "Vegetable Oil" (20386), "Garlic" (58280). Produces "Grilling Sauce" (58265). Requires Brewing, trivial 54.
33. Loot "Aged Piece of Meat" (48118) from "Ancient Nobleman" in `veksar`.
34. Combine in Oven (15): "Loaf of Bread" (13015), "Cheese" (8160), "Grilling Sauce" (58265), "Aged Piece of Meat" (48118). Produces "Aged Meat and Cheese Sandwich" (48120). Requires Baking, trivial 176.

### "Polished Symbol of Focus" (48129)

1. Common item: Glaze Mortar (17882). Listed in 30 zones.
2. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
3. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `steamfont`.
4. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `tox`.
5. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `toxxulia`.
6. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
7. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). The combine does not fail.
8. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
9. Common item: Mortar and Pestle (17904). Listed in 12 zones.
10. Common item: Limestone (16844). Listed in 4 zones.
11. Common item: Lead Sulphide (16845). Listed in 4 zones.
12. Combine in "Mortar and Pestle" (17904): "Limestone" (16844), "Lead Sulphide" (16845). Produces "White Lead" (16558). Requires Make Poison. The combine does not fail.
13. Common item: Firing Sheet (16906). Listed in 34 zones.
14. Combine in Pottery Wheel (21): "Water Flask" (13006), "Block of Clay" (16901). Produces "Small Block of Clay" (16900) x3. Requires Pottery, trivial 21.
15. Combine in Pottery Wheel (21): "Small Block of Clay" (16900), "Water Flask" (13006). Produces "Block of Clay" (16901). Requires Pottery, trivial 21.
16. Combine in Pottery Wheel (21): "Water Flask" (13006), "Large Block of Clay" (16902). Produces "Block of Clay" (16901) x2. Requires Pottery, trivial 21.
17. Combine in Pottery Wheel (21): "Block of Clay" (16901), "Water Flask" (13006). Produces "Large Block of Clay" (16902). Requires Pottery, trivial 21.
18. Common item: Large Bowl Sketch (16963). Listed in 29 zones.
19. Combine in Pottery Wheel (21): "Large Block of Clay" (16902), "Water Flask" (13006), "Large Bowl Sketch" (16963). Produces "Unfired Mixing Bowl" (16930). Requires Pottery, trivial 128.
20. Combine in Kiln (22): "Firing Sheet" (16906), "Unfired Mixing Bowl" (16930). Produces "Mixing Bowl" (17906). Requires Pottery, trivial 15.
21. Combine in "Mixing Bowl" (17906): "Limestone" (16844), "Lead Sulphide" (16845). Produces "White Lead" (16558). Requires Baking, trivial 15. The combine does not fail.
22. Ground spawn of "Permafrost Crystals" (22121) in `permafrost`.
23. Kill citymist/"A Black Reaver". Spawns "A Black Reaver" (90004).
24. Loot "Iron Oxide" (22124) from "A Black Reaver".
25. 4 alternative loot source(s) also yield Iron Oxide (22124).
26. Ground spawn of "Iron Oxide" (22124) in `steamfont`.
27. Combine in "Glaze Mortar" (17882): "Water Flask" (13006), "White Lead" (16558), "Permafrost Crystals" (22121), "Iron Oxide" (22124). Produces "Divine Crystalline Glaze" (16578). Requires Pottery. The combine does not fail.
28. Loot "Symbol of Focus" (48115) from "Disciple of Focus" in `tenebrous`.
29. Combine in Kiln (22): "Divine Crystalline Glaze" (16578), "Symbol of Focus" (48115). Produces "Polished Symbol of Focus" (48129). Requires Pottery, trivial 138.

### "Polished Symbol of Tranquility" (48130)

1. Common item: Glaze Mortar (17882). Listed in 30 zones.
2. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
3. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `steamfont`.
4. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `tox`.
5. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `toxxulia`.
6. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
7. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). The combine does not fail.
8. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
9. Common item: Mortar and Pestle (17904). Listed in 12 zones.
10. Common item: Limestone (16844). Listed in 4 zones.
11. Common item: Lead Sulphide (16845). Listed in 4 zones.
12. Combine in "Mortar and Pestle" (17904): "Limestone" (16844), "Lead Sulphide" (16845). Produces "White Lead" (16558). Requires Make Poison. The combine does not fail.
13. Common item: Firing Sheet (16906). Listed in 34 zones.
14. Combine in Pottery Wheel (21): "Water Flask" (13006), "Block of Clay" (16901). Produces "Small Block of Clay" (16900) x3. Requires Pottery, trivial 21.
15. Combine in Pottery Wheel (21): "Small Block of Clay" (16900), "Water Flask" (13006). Produces "Block of Clay" (16901). Requires Pottery, trivial 21.
16. Combine in Pottery Wheel (21): "Water Flask" (13006), "Large Block of Clay" (16902). Produces "Block of Clay" (16901) x2. Requires Pottery, trivial 21.
17. Combine in Pottery Wheel (21): "Block of Clay" (16901), "Water Flask" (13006). Produces "Large Block of Clay" (16902). Requires Pottery, trivial 21.
18. Common item: Large Bowl Sketch (16963). Listed in 29 zones.
19. Combine in Pottery Wheel (21): "Large Block of Clay" (16902), "Water Flask" (13006), "Large Bowl Sketch" (16963). Produces "Unfired Mixing Bowl" (16930). Requires Pottery, trivial 128.
20. Combine in Kiln (22): "Firing Sheet" (16906), "Unfired Mixing Bowl" (16930). Produces "Mixing Bowl" (17906). Requires Pottery, trivial 15.
21. Combine in "Mixing Bowl" (17906): "Limestone" (16844), "Lead Sulphide" (16845). Produces "White Lead" (16558). Requires Baking, trivial 15. The combine does not fail.
22. Ground spawn of "Permafrost Crystals" (22121) in `permafrost`.
23. Kill citymist/"A Black Reaver". Spawns "A Black Reaver" (90004).
24. Loot "Iron Oxide" (22124) from "A Black Reaver".
25. 4 alternative loot source(s) also yield Iron Oxide (22124).
26. Ground spawn of "Iron Oxide" (22124) in `steamfont`.
27. Combine in "Glaze Mortar" (17882): "Water Flask" (13006), "White Lead" (16558), "Permafrost Crystals" (22121), "Iron Oxide" (22124). Produces "Divine Crystalline Glaze" (16578). Requires Pottery. The combine does not fail.
28. Loot "Symbol of Tranquility" (48114) from "Disciple of Tranquility" in `povalor`.
29. Combine in Kiln (22): "Divine Crystalline Glaze" (16578), "Symbol of Tranquility" (48114). Produces "Polished Symbol of Tranquility" (48130). Requires Pottery, trivial 138.

## `MnkPre`

Values written: 1, 2, 3.

### 2. a fallen student — hand 48100+48101

Zone: `lakerathe`.

Sets `MnkPre` to `2`.

- Turn in x1: Seal of Cedrick (48100).
- Turn in x1: Seal of Mystik (48101).
In script order:

1. Sets `MnkPre` to `2`.


How the items are reached:

- Seal of Cedrick (48100)
  - Loot "Seal of Cedrick" (48100) from "Cedrick" in `cobaltscar`.
- Seal of Mystik (48101)
  - Loot "Seal of Mystik" (48101) from "Mystik" in `qey2hh1`.

### 3. a fallen student — hand 48102

Zone: `lakerathe`.

Sets `MnkPre` to `3`.

- Turn in x1: Medal of Identity (48102).
In script order:

1. Sets `MnkPre` to `3`.


How the items are reached:

- Medal of Identity (48102)
  - Say "I Am Ready To Be Tested" to frozenshadow/"You".
  - Spawns "Mirror Reflection" (111190).
  - Loot "Medal of Identity" (48102) from "Mirror Reflection".
  - 1 alternative loot source(s) also yield Medal of Identity (48102).

### 1. a fallen student — say hail

Zone: `lakerathe`.

> Eh? There is nothing I can help you with. I have nothing for myself anymore... except these [

Sets `MnkPre` to `1`.

- Needs `monk_epic` unset.
- Needs `MnkPre` unset.
- Needs `monk_epic` ==1.
- One of: `MnkPre` ==3; Celestial Fists (10652).
In script order:

1. Sets `monk_epic` to `1`.
2. Sets `MnkPre` to `1`.


How the items are reached:

- Celestial Fists (10652)
  - Prerequisite: "Celestial Fists" (10652). See section 0.

Subquest `monk_epic`:

#### `monk_epic`

Values written: 1, 2, 3, 4, 5, 6, 7, 8, 9.

##### 1. a fallen student — say hail

Zone: `lakerathe`.

> Eh? There is nothing I can help you with. I have nothing for myself anymore... except these [

Sets `monk_epic` to `1`.

- Needs `monk_epic` unset.
- Needs `MnkPre` unset.
- Needs `monk_epic` ==1.
- One of: `MnkPre` ==3; Celestial Fists (10652).
In script order:

1. Sets `monk_epic` to `1`.
2. Sets `MnkPre` to `1`.


How the items are reached:

- Celestial Fists (10652)
  - Prerequisite: "Celestial Fists" (10652). See section 0.

This step also depends on `MnkPre`, shown above.

##### 2. a fallen student — hand 48122

Zone: `lakerathe`.

Sets `monk_epic` to `2`.

- Turn in x1: Muramite Sand (48122).
In script order:

1. Sets `monk_epic` to `2`.


How the items are reached:

- Muramite Sand (48122)
  - Spawns "A Dragorn Sycophant" (335023) in `harbingers` on event_spawn.
  - Loot "Muramite Sand" (48122) from "A Dragorn Sycophant".

##### 3. tomekeeper danl — hand 48132

Zone: `erudnext`.

Sets `monk_epic` to `3`.

- Needs `monk_epic` set.
- Needs `monk_epic` >=2.
- Turn in x1: Danl's Missing Book (48132).
In script order:

1. Sets `monk_epic` to `3`.


How the items are reached:

- Danl's Missing Book (48132)
  - Prerequisite: "Danl's Missing Book" (48132). See section 0.

##### 4. vortix — say diary

Zone: `lakerathe`.

> Kaiaren

Sets `monk_epic` to `4`.

In script order:

1. Sets `monk_epic` to `4`.


##### 5. vortix — hand 48109+48110

Zone: `potranquility`.

Sets `monk_epic` to `5`.

- Needs `monk_epic` ==4.
- Turn in x1: 1/2 of Kaiaren's Diary (48109).
- Turn in x1: 1/2 of Kaiaren's Diary (48110).
In script order:

1. Sets `monk_epic` to `5`.


How the items are reached:

- 1/2 of Kaiaren's Diary (48109)
  - Loot "1/2 of Kaiaren's Diary" (48109) from "Wygrish" in `sirens`.
- 1/2 of Kaiaren's Diary (48110)
  - Loot "1/2 of Kaiaren's Diary" (48110) from "Quigli" in `dulak`.

##### 6. eryke stremstin — hand 48128

Zone: `bazaar`.

Sets `monk_epic` to `6`.

- Turn in x1: Letter to Stremstin (48128).
In script order:

1. Sets `monk_epic` to `6`.


How the items are reached:

- Letter to Stremstin (48128)
  - Prerequisite: "Letter to Stremstin" (48128). See section 0.

##### 7. vortix — hand 48127

Zone: `potranquility`.

Sets `monk_epic` to `7`.

- Needs `monk_epic` ==6.
- Turn in x1: Initiate's Sash of the Celestial Order (48127).
In script order:

1. Sets `monk_epic` to `7`.
2. Gives Initiate's Sash of the Celestial Order (48127).


How the items are reached:

- Initiate's Sash of the Celestial Order (48127)
  - Prerequisite: "Initiate's Sash of the Celestial Order" (48127). See section 0.

##### 8. vortix — hand 48137+48138

Zone: `potranquility`.

Sets `monk_epic` to `8`.

- Needs `monk_epic` ==7.
- Turn in x1: Kaiaren's Mind (48137).
- Turn in x1: Kaiaren's Body (48138).
In script order:

1. Sets `monk_epic` to `8`.


How the items are reached:

- Kaiaren's Mind (48137)
  - Loot "Kaiaren's Mind" (48137) from "Kragsmash" in `bloodfields`.
- Kaiaren's Body (48138)
  - Loot "Kaiaren's Body" (48138) from "Windrush" in `harbingers`.

##### 9. vortix — hand 20435

Zone: `potranquility`.

Sets `monk_epic` to `9`.

- Needs `monk_epic` ==8.
- Turn in x1: Scribed Note (20435).
In script order:

1. Sets `monk_epic` to `9`.
2. Gives Fistwraps of Celestial Discipline (61025).


How the items are reached:

- Scribed Note (20435)
  - Loot "Scribed Note" (20435) from "The Keeper" in `bloodfields`.

##### Steps on `monk_epic` that do not change it

- `bazaar` eryke stremstin, hand platinum:1000 needs `monk_epic` set.
  - Gives Celestial Thread (48123).
- `bloodfields` player, on loot needs `monk_epic` set.
  - Sets `warr_epic_bloodfield` to `1`.
  - Spawns a chest (Epic 1.5) (283157).
  - Sets `monk_epic_bloodfield` to `1`.
  - Sets `monk_epic_keeper` to `1`.
  - Sets `bst_chest_causeway` to `1`.
  - Spawns a chest (epic 2.0) (893).
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
- `dulak` quigli, say defeat needs `monk_epic` set.
  - Spawns a lackey of Quigli (225380).
  - Spawns a swabby of Quigli (225381).
  - Spawns a scallywag of Quigli (225382).
- `harbingers` player, on loot needs `monk_epic` >=7.
  - Sets `monk_epic_harbinger` to `1`.
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
- `lakerathe` a fallen student, say vortix needs `monk_epic` ==3.
  - Spawns Vortix (203433).
- `oceanoftears` kaiaren, say choose to continue needs `monk_epic` ==9.
  - Sets `mnk_epic20` to `3`.
- `oceanoftears` kaiaren, say choose to continue needs `monk_epic` ==9.
  - Sets `mnk_epic20` to `3`.
  - Gives Initiate's Sash of the Celestial Order (48127).
- `oceanoftears` kaiaren, say menace needs `monk_epic` ==9.
  - Sets `mnk_epic20` to `1`.
- `oot` kaiaren, say choose to continue needs `monk_epic` ==9.
  - Sets `mnk_epic20` to `3`.
- `oot` kaiaren, say choose to continue needs `monk_epic` ==9.
  - Sets `mnk_epic20` to `3`.
  - Gives Initiate's Sash of the Celestial Order (48127).
- `oot` kaiaren, say menace needs `monk_epic` ==9.
  - Sets `mnk_epic20` to `1`.
- `potranquility` vortix, say hail needs `monk_epic` >=5.
  - Gives Letter to Stremstin (48128).
- `westwastes` disciple of moon trap, on enter needs `monk_epic` ==5.
  - Spawns Disciple of Moon (120138).
  - Loots Symbol of Moon (48111).

### Steps on `MnkPre` that do not change it

- `lakerathe` a fallen student, say hail needs `MnkPre` ==3.
  - Sets `monk_epic` to `1`.

## `monk_epic`

See `monk_epic` earlier in this file.

## `mnk_epic20`

Values written: 1, 2, 3, 4, 5, 6.

### 1. kaiaren — say menace

Zone: `oceanoftears`.

> What menace? For sure Vortix has mentioned to you his dreams? His dreams provide a rare gift of forsight into what lies ahead. There is a dark threat that lo...

Sets `mnk_epic20` to `1`.

- Needs `mnk_epic20` unset.
- Needs `monk_epic` ==9.
In script order:

1. Sets `mnk_epic20` to `1`.


This step also depends on `monk_epic`, shown above.

Alternative or repeat transition to `mnk_epic20` = `1` (not an additional required stage).

### 1. kaiaren — say menace

Zone: `oot`.

> What menace? For sure Vortix has mentioned to you his dreams? His dreams provide a rare gift of forsight into what lies ahead. There is a dark threat that lo...

Sets `mnk_epic20` to `1`.

- Needs `mnk_epic20` unset.
- Needs `monk_epic` ==9.
In script order:

1. Sets `mnk_epic20` to `1`.


This step also depends on `monk_epic`, shown above.

### 2. kaiaren — hand 48119+48120

Zones: `oceanoftears`, `oot`.

Sets `mnk_epic20` to `2`.

- Turn in x1: Sugar and Spice Nectar Pie (48119).
- Turn in x1: Aged Meat and Cheese Sandwich (48120).
In script order:

1. Sets `mnk_epic20` to `2`.


How the items are reached:

- Sugar and Spice Nectar Pie (48119)
  - Prerequisite: "Sugar and Spice Nectar Pie" (48119). See section 0.
- Aged Meat and Cheese Sandwich (48120)
  - Prerequisite: "Aged Meat and Cheese Sandwich" (48120). See section 0.

### 3. kaiaren — say choose to continue

Zone: `oceanoftears`.

> As I thought you would; you will find them as you did the others, in their natural essence. You will find the Disciple of Focus in the hills and mountains tr...

Sets `mnk_epic20` to `3`.

- Needs `mnk_epic20` >=2.
- Needs `mnk_epic20` set.
- Needs `monk_epic` ==9.
- Needs `mnk_epic20` ==2.
- Needs Initiate's Sash of the Celestial Order (48127).
In script order:

1. Sets `mnk_epic20` to `3`.


How the items are reached:

- Initiate's Sash of the Celestial Order (48127)
  - Prerequisite: "Initiate's Sash of the Celestial Order" (48127). See section 0.

This step also depends on `monk_epic`, shown above.

Alternative or repeat transition to `mnk_epic20` = `3` (not an additional required stage).

### 3. kaiaren — say choose to continue

Zone: `oot`.

> As I thought you would; you will find them as you did the others, in their natural essence. You will find the Disciple of Focus in the hills and mountains tr...

Sets `mnk_epic20` to `3`.

- Needs `mnk_epic20` >=2.
- Needs `mnk_epic20` set.
- Needs `monk_epic` ==9.
- Needs `mnk_epic20` ==2.
- Needs Initiate's Sash of the Celestial Order (48127).
In script order:

1. Sets `mnk_epic20` to `3`.


How the items are reached:

- Initiate's Sash of the Celestial Order (48127)
  - Prerequisite: "Initiate's Sash of the Celestial Order" (48127). See section 0.

This step also depends on `monk_epic`, shown above.

### 4. kaiaren — hand 48127+48129+48130

Zones: `oceanoftears`, `oot`.

Sets `mnk_epic20` to `4`.

- Needs `mnk_epic20` >=3.
- Turn in x1: Polished Symbol of Focus (48129).
- Turn in x1: Polished Symbol of Tranquility (48130).
- Turn in x1: Initiate's Sash of the Celestial Order (48127).
In script order:

1. Sets `mnk_epic20` to `4`.


How the items are reached:

- Polished Symbol of Focus (48129)
  - Prerequisite: "Polished Symbol of Focus" (48129). See section 0.
- Polished Symbol of Tranquility (48130)
  - Prerequisite: "Polished Symbol of Tranquility" (48130). See section 0.
- Initiate's Sash of the Celestial Order (48127)
  - Prerequisite: "Initiate's Sash of the Celestial Order" (48127). See section 0.

### 5. kaiaren — on event_death_complete

Zones: `oceanoftears`, `oot`.

Sets `mnk_epic20` to `5`.

In script order:

1. Spawns a chest (epic 2.0) (893).
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
2. Sets `mnk20_oot_chest` to `1`.
3. Sets `mnk_epic20` to `5`.


### 6. vortix — hand 47100

Zone: `potranquility`.

Sets `mnk_epic20` to `6`.

- Needs `mnk_epic20` >=5.
- Needs `mnk_epic20` ==5.
- Turn in x1: Globe of Discordant Energy (47100).
In script order:

1. Sets `mnk_epic20` to `6`.
2. Gives Globe of Discordant Energy (47100).


How the items are reached:

- Globe of Discordant Energy (47100)
  - Say "Check Lorb" to anguish/"Zone Status".
  - Spawns "Orb of Discordant Energy" (317087).
  - Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy".
  - 4 alternative loot source(s) also yield Globe of Discordant Energy (47100).

### Steps on `mnk_epic20` that do not change it

- `oceanoftears` kaiaren, say choose to continue needs `mnk_epic20` ==2.
  - Gives Initiate's Sash of the Celestial Order (48127).
- `oot` kaiaren, say choose to continue needs `mnk_epic20` ==2.
  - Gives Initiate's Sash of the Celestial Order (48127).
- `poknowledge` sebast muckle, hand 47100+61025 needs `mnk_epic20` ==6.
  - Turn in Globe of Discordant Energy (47100).
  - Turn in Fistwraps of Celestial Discipline (61025).
  - Gives Transcended Fistwraps of Immortality (67742).

## Other flags touched along the way

- `monk_epic_bloodfield` set to 1 at bloodfields/player.
- `monk_epic_harbinger` set to 1 at harbingers/player.
- `monk_epic_keeper` set to 1 at bloodfields/player.
- `monk_epic_scarlet` set to 1 at scarlet/a sun reaver, scarlet/a sun revenant.
