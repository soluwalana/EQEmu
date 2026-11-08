# Monk

Steps taken from the quest graph only. **Broken** means the graph has no edge for that value or that item.

Flags with writes: `MnkPre`, `monk_epic`, `mnk_epic20`.

## 0. Prerequisites

Shared acquisition steps appear in the first prerequisite chain that needs them. Later sections reference that chain rather than repeating it.

### "Letter to Stremstin" (48128)

1. bazaar/"Eryke Stremstin", hand "Letter to Stremstin" (48128). Sets `monk_epic` to `6`.
2. Loot "Sunless Nectar" (48117) from "An Ancient Shrieker" (NPC 164049) in `thedeep`. Drop cache: 11.17% chance per kill.
3. Buy "Spices" (13425) from "Pincia Brownloe" (NPC 9088) in `freportw`. Base price: 7 copper.
4. Buy "High Quality Firing Sheet" (16908) from "Winn Greenbane" (NPC 5059) in `highpass`. Base price: 40 copper.
5. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
6. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `steamfont`.
7. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `tox`.
8. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `toxxulia`.
9. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
10. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). The combine does not fail.
11. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
12. Combine in Pottery Wheel (21): "Water Flask" (13006), "Block of Clay" (16901). Produces "Small Block of Clay" (16900) x3. Requires Pottery, trivial 21.
13. Combine in Pottery Wheel (21): "Small Block of Clay" (16900), "Water Flask" (13006). Produces "Block of Clay" (16901). Requires Pottery, trivial 21.
14. Buy "Pie Tin Sketch" (16958) from "Min Greyeagle" (NPC 5057) in `highpass`. Base price: 490 copper.
15. Combine in Pottery Wheel (21): "Block of Clay" (16901), "Water Flask" (13006), "Pie Tin Sketch" (16958). Produces "Unfired Pie Tin" (16926). Requires Pottery, trivial 115.
16. Combine in Kiln (22): "High Quality Firing Sheet" (16908), "Unfired Pie Tin" (16926). Produces "Pie Tin" (13438). Requires Pottery, trivial 15.
17. Combine in Oven (15): "Sunless Nectar" (48117), "Spices" (13425), "Pie Tin" (13438). Produces "Sugar and Spice Nectar Pie" (48119). Requires Baking, trivial 176.
18. Buy "Spit" (17947) from "Frannie" (NPC 3020) in `qrg`. Base price: 200 copper.
19. Buy "Firing Sheet" (16906) from "Winn Greenbane" (NPC 5059) in `highpass`. Base price: 10 copper.
20. Combine in Pottery Wheel (21): "Block of Clay" (16901), "Water Flask" (13006). Produces "Large Block of Clay" (16902). Requires Pottery, trivial 21.
21. Buy "Large Bowl Sketch" (16963) from "Min Greyeagle" (NPC 5057) in `highpass`. Base price: 760 copper.
22. Combine in Pottery Wheel (21): "Large Block of Clay" (16902), "Water Flask" (13006), "Large Bowl Sketch" (16963). Produces "Unfired Mixing Bowl" (16930). Requires Pottery, trivial 128.
23. Combine in Kiln (22): "Firing Sheet" (16906), "Unfired Mixing Bowl" (16930). Produces "Mixing Bowl" (17906). Requires Pottery, trivial 15.
24. Spawns "Disciple Okarote" (100133) in `stonebrunt` on event_waypoint_arrive.
25. Loot "Bottle of Milk" (13087) from "Disciple Okarote".
26. Loot "Snake Egg" (13088) from "A Female Razorback" (NPC 403032) in `sunderock`. Drop cache: 75.06% chance per kill.
27. Buy "Cup of Flour" (13193) from "Karn Tassen" (NPC 1110) in `qeynos`. Base price: 1 copper.
28. Combine in "Mixing Bowl" (17906): "Bottle of Milk" (13087), "Snake Egg" (13088), "Cup of Flour" (13193). Produces "Clump of Dough" (13090). Requires Baking, trivial 17.
29. Buy "Bread Tin Mold" (12025) from "Frannie" (NPC 3020) in `qrg`. Base price: 400 copper.
30. kaladimb/"Jeet", say "Collect The Gnome Profit". Gives "Scrubber Key" (12164).
31. akanon/"Clockwork Scrubber", hand "Scrubber Key" (12164). Gives "Gnome Take" (12167).
32. kaladimb/"Jeet", hand "Gnome Take" (12167). Gives "Small Piece of Ore" (10500).
33. Combine in Forge (17): "Small Piece of Ore" (10500), "Water Flask" (13006). Produces "Metal Bits" (16905) x2. Requires Blacksmithing, trivial 18.
34. Buy "Quality Firing Sheet" (16907) from "Winn Greenbane" (NPC 5059) in `highpass`. Base price: 20 copper.
35. Buy "Ceramic Lining Sketch" (16964) from "Min Greyeagle" (NPC 5057) in `highpass`. Base price: 25 copper.
36. Combine in Pottery Wheel (21): "Water Flask" (13006), "Small Block of Clay" (16900), "Ceramic Lining Sketch" (16964). Produces "Unfired Ceramic Lining" (16946). Requires Pottery, trivial 36.
37. Combine in Kiln (22): "Quality Firing Sheet" (16907), "Unfired Ceramic Lining" (16946). Produces "Ceramic Lining" (16947). Requires Pottery, trivial 17.
38. Combine in Forge (17): "Bread Tin Mold" (12025), "Water Flask" (13006), "Metal Bits" (16905), "Ceramic Lining" (16947). Produces "Bread Tin" (13440). Requires Blacksmithing, trivial 38.
39. Combine in "Spit" (17947): "Clump of Dough" (13090), "Bread Tin" (13440). Hands back "Bread Tin" (13440). Produces "Loaf of Bread" (13015). Requires Baking, trivial 115.
40. Buy "Cheese" (8160) from "A Goblin Bartender" (NPC 11071) in `runnyeye`. Base price: 15 copper.
41. potranquility/"Elder Fuirstel", say "Hail". Sets `pop_cod_final` to `1`.
42. poknowledge/"Aid Grimel", say "Skill In Brewing". Requires `pop_cod_final` ==1. Requires `pop_cod_final` set. Gives "Portable Drink Barrel" (17179).
43. Buy "Lettuce" (13976) from "Cleet Miller Jr" (NPC 12029) in `qey2hh1`. Base price: 25 copper.
44. rivervale/"Ilscent Tagglefoot", say "Jumjum Juice". Gives "Case of Jumjum Juice" (13411).
45. northkarana/"Xanuusus", hand "Case of Jumjum Juice" (13411). Gives "Carrot" (13977).
46. Buy "Turnip" (13979) from "Cleet Miller Jr" (NPC 12029) in `qey2hh1`. Base price: 25 copper.
47. Combine in "Mixing Bowl" (17906): "Lettuce" (13976), "Carrot" (13977), "Turnip" (13979). Produces "Vegetables" (13419). Requires Baking, trivial 15. The combine does not fail.
48. Combine in "Portable Drink Barrel" (17179): "Water Flask" (13006), "Vegetables" (13419). Produces "Vegetable Oil" (20386). Requires Brewing, trivial 102.
49. Buy "Garlic" (58280) from "Culkin Ironstove" (NPC 202092) in `poknowledge`. Base price: 10 copper.
50. Combine in Brew Barrel (19): "Vegetable Oil" (20386), "Garlic" (58280). Produces "Grilling Sauce" (58265). Requires Brewing, trivial 54.
51. Loot "Aged Piece of Meat" (48118) from "Ancient Nobleman" in `veksar`.
52. Combine in Oven (15): "Loaf of Bread" (13015), "Cheese" (8160), "Grilling Sauce" (58265), "Aged Piece of Meat" (48118). Produces "Aged Meat and Cheese Sandwich" (48120). Requires Baking, trivial 176.
53. oceanoftears/"Kaiaren", hand "Sugar and Spice Nectar Pie" (48119) + "Aged Meat and Cheese Sandwich" (48120). Sets `mnk_epic20` to `2`.
54. potranquility/"Vortix", hand "Initiate's Sash of the Celestial Order" (48127). Sets `monk_epic` to `7`.
55. Loot "Kaiaren's Mind" (48137) from "Kragsmash" in `bloodfields`.
56. Loot "Kaiaren's Body" (48138) from "Windrush" in `harbingers`.
57. potranquility/"Vortix", hand "Kaiaren's Mind" (48137) + "Kaiaren's Body" (48138). Sets `monk_epic` to `8`.
58. Loot "Scribed Note" (20435) from "The Keeper" in `bloodfields`.
59. potranquility/"Vortix", hand "Scribed Note" (20435). Sets `monk_epic` to `9`.
60. Unresolved cyclic prerequisite: `mnk_epic20` >=5.
61. oceanoftears/"Kaiaren", on event_death_complete. Sets `mnk_epic20` to `5`.
62. Say "Check Lorb" to anguish/"Zone Status".
63. Spawns "Orb of Discordant Energy" (317087).
64. Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy".
65. Alternative: Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy" (NPC 317087) in `anguish`; trigger: anguish/"Zone Status", say "Check Uorb".
66. Alternative: Loot "Globe of Discordant Energy" (47100) from "Ornate Chest" (NPC 317112) in `anguish`; trigger: anguish/"Zone Status", say "Check Amv Chest".
67. Alternative: Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy" (NPC 317087) in `anguish`; trigger: anguish/"Zone Status", on event_signal.
68. Alternative: Loot "Globe of Discordant Energy" (47100) from "Overlords Chest" (NPC 317124) in `anguish`; trigger: anguish/"Zone Status", on event_signal.
69. potranquility/"Vortix", hand "Globe of Discordant Energy" (47100). Sets `mnk_epic20` to `6`.
70. oceanoftears/"Kaiaren", say "Choose To Continue". Requires `mnk_epic20` ==2. Requires `mnk_epic20` set. Requires `monk_epic` ==9. Requires `mnk_epic20` >=2. Gives "Initiate's Sash of the Celestial Order" (48127).
71. lakerathe/"Vortix", say "Diary". Sets `monk_epic` to `4`.
72. Loot "1/2 of Kaiaren's Diary" (48109) from "Wygrish" in `sirens`.
73. Loot "1/2 of Kaiaren's Diary" (48110) from "Quigli" in `dulak`.
74. potranquility/"Vortix", hand "1/2 of Kaiaren's Diary" (48109) + "1/2 of Kaiaren's Diary" (48110). Sets `monk_epic` to `5`.
75. Spawns "Disciple of Moon" (120138) in `westwastes` on enter.
76. Loot "Symbol of Moon" (48111) from "Disciple of Moon".
77. potranquility/"Vortix", say "Hail". Requires `monk_epic` >=5. Gives "Letter to Stremstin" (48128).

### "Polished Symbol of Focus" (48129)

1. Buy "Glaze Mortar" (17882) from "Winn Greenbane" (NPC 5059) in `highpass`. Base price: 1,000 copper.
2. Acquisition of "Water Flask" (13006) is documented under "Letter to Stremstin" (48128); obtain another copy if needed.
3. Acquisition of "Mixing Bowl" (17906) is documented under "Letter to Stremstin" (48128); obtain another copy if needed.
4. Buy "Limestone" (16844) from "Myre" (NPC 67016) in `kaladimb`. Base price: 400 copper.
5. Buy "Lead Sulphide" (16845) from "Myre" (NPC 67016) in `kaladimb`. Base price: 450 copper.
6. Combine in "Mixing Bowl" (17906): "Limestone" (16844), "Lead Sulphide" (16845). Produces "White Lead" (16558). Requires Baking, trivial 15. The combine does not fail.
7. Ground spawn of "Permafrost Crystals" (22121) in `permafrost`.
8. Kill citymist/"A Black Reaver". Spawns "A Black Reaver" (90004).
9. Loot "Iron Oxide" (22124) from "A Black Reaver".
10. Alternative: Loot "Iron Oxide" (22124) from "A Black Reaver" (NPC 90005) in `citymist`; trigger: citymist/"A Black Reaver", on event_death_complete.
11. Alternative: Loot "Iron Oxide" (22124) from "A Black Reaver" (NPC 90192) in `citymist`; trigger: citymist/"A Black Reaver", on event_death_complete.
12. Alternative: Loot "Iron Oxide" (22124) from "A Boulder Fiend" (NPC 171063) in `thegrey`; trigger: thegrey/"A Creature", on enter.
13. Alternative: Loot "Iron Oxide" (22124) from "A Stone Beast" (NPC 171051) in `thegrey`; trigger: thegrey/"A Creature", on enter.
14. Ground spawn of "Iron Oxide" (22124) in `steamfont`.
15. Combine in "Glaze Mortar" (17882): "Water Flask" (13006), "White Lead" (16558), "Permafrost Crystals" (22121), "Iron Oxide" (22124). Produces "Divine Crystalline Glaze" (16578). Requires Pottery. The combine does not fail.
16. Loot "Symbol of Focus" (48115) from "Disciple of Focus" in `tenebrous`.
17. Combine in Kiln (22): "Divine Crystalline Glaze" (16578), "Symbol of Focus" (48115). Produces "Polished Symbol of Focus" (48129). Requires Pottery, trivial 138.

### "Polished Symbol of Tranquility" (48130)

1. Acquisition of "Divine Crystalline Glaze" (16578) is documented under "Polished Symbol of Focus" (48129); obtain another copy if needed.
2. Loot "Symbol of Tranquility" (48114) from "Disciple of Tranquility" in `povalor`.
3. Combine in Kiln (22): "Divine Crystalline Glaze" (16578), "Symbol of Tranquility" (48114). Produces "Polished Symbol of Tranquility" (48130). Requires Pottery, trivial 138.

### "Aged Meat and Cheese Sandwich" (48120)

1. Acquisition of "Aged Meat and Cheese Sandwich" (48120) is documented under "Letter to Stremstin" (48128); obtain another copy if needed.

### "Danl's Missing Book" (48132)

1. Ground spawn of "Section of Parchment" (48104) in `gunthak`.
2. Ground spawn of "Section of Parchment" (48105) in `hole`.
3. Ground spawn of "Section of Parchment" (48106) in `charasis`.
4. Ground spawn of "Section of Parchment" (48107) in `akheva`.
5. shadowhaven/"Researcher Relreom", hand "Section of Parchment" (48104) + "Section of Parchment" (48105) + "Section of Parchment" (48106) + "Section of Parchment" (48107). Gives "Danl's Missing Book" (48132).

### "Celestial Fists" (10652)

1. Kill lakeofillomen/"Vorash". Spawns "Xenevorash" (85208).
2. Loot "Demon Fangs" (1688) from "Xenevorash".
3. Loot "Metal Pipe" (12979) from "A Drolvarg Pawbuster" in `karnor`.
4. Loot "Metal Pipe" (12980) from "An Iksar Betrayer" in `chardok`.
5. Buy "King's Court Token" (66616) from "Keiya Oakwood" (NPC 150311) in `shadowhaven`. Base price: 95,239 copper.
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
32. Buy "Greater Lightstone" (10400) from "Gliblixl Rocktok" (NPC 151204) in `bazaar`. Base price: 4,500 copper.
33. Loot "Cutthroat Insignia Ring" (1903) from "a Dervish Cutthroat" (NPC 457074) in `oldcommons`. Drop cache: 55.56% chance per kill.
34. Loot "Legionnaire's Bracer" (2299) from "Orc Legionnaire" (NPC 21119) in `commons`. Drop cache: 84% chance per kill.
35. Loot "Deathfist Pawn Scalp" (13794) from "Orc Pawn" (NPC 415088) in `mistythicket`. Drop cache: 50% chance per kill.
36. Loot "Snake Fang" (13067) from "A Giant Briar Snake" (NPC 414061) in `toxxulia`. Drop cache: 58.21% chance per kill.
37. Acquisition of "Bone Chips" (13073) is documented under "Letter to Stremstin" (48128); obtain another copy if needed.
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
49. Buy "Song: Jonthan's Whistling Warsong" (15734) from "Lysric Loresinger" (NPC 1035) in `qeynos`. Base price: 43 copper.
50. Buy "Needle Mold" (12019) from "Dyona Rossook" (NPC 5065) in `highpass`. Base price: 180 copper.
51. Buy "Thimble Mold" (12057) from "Dyona Rossook" (NPC 5065) in `highpass`. Base price: 180 copper.
52. Acquisition of "Water Flask" (13006) is documented under "Letter to Stremstin" (48128); obtain another copy if needed.
53. **Broken:** nothing in the graph gives, loots, spawns, or combines Notice to Cease and Desist (9590).
54. Hand "Notice to Cease and Desist" (9590) to freeporteast/"Lythe Songbird". Spawns "a Freeport guard" (382255). Loot "Fine Steel Two Handed Sword" (5351) from "a Freeport guard".
55. Alternative: Loot "Fine Steel Two Handed Sword" (5351) from "a seasoned Freeport guard" (NPC 382256) in `freeporteast`; trigger: freeporteast/"Lythe Songbird", hand "Notice to Cease and Desist" (9590).
56. Alternative: Loot "Fine Steel Two Handed Sword" (5351) from "a Freeport guard" (NPC 382255) in `freportw`; trigger: freportw/"Lythe Songbird", hand "Notice to Cease and Desist" (9590).
57. Alternative: Loot "Fine Steel Two Handed Sword" (5351) from "a seasoned Freeport guard" (NPC 382256) in `freportw`; trigger: freportw/"Lythe Songbird", hand "Notice to Cease and Desist" (9590).
58. Alternative: Loot "Fine Steel Two Handed Sword" (5351) from "a minion of Meldrath" (NPC 56173) in `steamfont`; trigger: steamfont/"Meldraths Paige", say "We Shall Never Surrender".
59. Alternative: Loot "Fine Steel Two Handed Sword" (5351) from "Meldrath's melded minions" (NPC 56174) in `steamfont`; trigger: steamfont/"Meldraths Paige", say "Your Forces Are Deafeated".
60. Alternative: Loot "Fine Steel Two Handed Sword" (5351) from "Arnold the Gnomeinator" (NPC 56175) in `steamfont`; trigger: steamfont/"Meldraths Paige", say "You Shall Not Break Our Defense".
61. Alternative: Loot "Fine Steel Two Handed Sword" (5351) from "a Freeport guard" (NPC 382255) in `freeporteast`; trigger: freeporteast/"Lythe Songbird", on timer guard.
62. Alternative: Loot "Fine Steel Two Handed Sword" (5351) from "a seasoned Freeport guard" (NPC 382256) in `freeporteast`; trigger: freeporteast/"Lythe Songbird", on timer guard.
63. Alternative: Loot "Fine Steel Two Handed Sword" (5351) from "a Freeport guard" (NPC 382255) in `freportw`; trigger: freportw/"Lythe Songbird", on timer guard.
64. Alternative: Loot "Fine Steel Two Handed Sword" (5351) from "a seasoned Freeport guard" (NPC 382256) in `freportw`; trigger: freportw/"Lythe Songbird", on timer guard.
65. Combine in Forge (17): "Fine Steel Two Handed Sword" (5351), "Water Flask" (13006). Produces "Small Brick of High Quality Ore" (10468) x2, "Small Piece of High Quality Ore" (22229). Requires Blacksmithing, trivial 21.
66. Combine in Royal Qeynos Forge (40): "Small Piece of High Quality Ore" (22229), "Water Flask" (13006). Produces "High Quality Metal Bits" (22230). Requires Blacksmithing, trivial 20.
67. Combine in Vale Forge (49): "Needle Mold" (12019), "Thimble Mold" (12057), "Water Flask" (13006), "High Quality Metal Bits" (22230). Produces "Vale Sewing Kit" (92882). Requires Blacksmithing, trivial 162.
68. Loot "Shadow Wolf Pelt" (13779) from "A Shadow Wolf" (NPC 408093) in `commonlands`. Drop cache: 7.64% chance per kill.
69. Buy "Spell: Gather Shadows" (15522) from "Tagus Wunne" (NPC 10030) in `freporte`. Base price: 43 copper.
70. Forage "Spider Silk" (13041) in `mistmoore`.
71. Forage "Spider Silk" (13041) in `mmca`.
72. Forage "Spider Silk" (13041) in `mmcb`.
73. Forage "Spider Silk" (13041) in `mmcc`.
74. Forage "Spider Silk" (13041) in `mmcd`.
75. Forage "Spider Silk" (13041) in `mmce`.
76. Forage "Spider Silk" (13041) in `mmcf`.
77. Forage "Spider Silk" (13041) in `mmcg`.
78. Forage "Spider Silk" (13041) in `mmch`.
79. Forage "Spider Silk" (13041) in `mmci`.
80. Forage "Spider Silk" (13041) in `mmcj`.
81. Combine in "Vale Sewing Kit" (92882): "Spider Silk" (13041). Produces "Silk Swatch" (16482). Requires Tailoring, trivial 15. The combine does not fail.
82. Combine in "Vale Sewing Kit" (92882): "Shadow Wolf Pelt" (13779), "Spell: Gather Shadows" (15522), "Silk Swatch" (16482). Produces "Shadow Silk" (16483). Requires Tailoring, trivial 36.
83. Combine in "Deluxe Sewing Kit" (17966): "Needle of the Void" (12314), "Rare Robe Pattern" (12315), "Song: Jonthan's Whistling Warsong" (15734), "Shadow Silk" (16483). Produces "Robe of the Lost Circle" (12256). Requires Tailoring. The combine does not fail.
84. dreadlands/"Brother Balatin", hand "Robe of the Lost Circle" (12256) + "Metal Pipe" (12979) + "Metal Pipe" (12980). Gives "Robe of the Whistling Fists" (12970).
85. Loot "Immortals" (18195) from "Faerie of Dismay" (NPC 91012) in `skyfire`. Drop cache: 35% chance per kill.
86. erudnext/"Tomekeeper Danl", hand "Immortals" (18195). Gives "Danl's Reference" (1682).
87. timorous/"Lheao", hand "Danl's Reference" (1682) + "Robe of the Whistling Fists" (12970). Gives "Celestial Fists" (1683).
88. trakanon/"Kaiaren", hand "Celestial Fists" (1683). Gives "Book of Celestial Fists" (1689).
89. trakanon/"Kaiaren", hand "Demon Fangs" (1688) + "Book of Celestial Fists" (1689). Gives "Celestial Fists" (10652).

### "Sugar and Spice Nectar Pie" (48119)

1. Acquisition of "Sugar and Spice Nectar Pie" (48119) is documented under "Letter to Stremstin" (48128); obtain another copy if needed.

### "Initiate's Sash of the Celestial Order" (48127)

1. Acquisition of "Initiate's Sash of the Celestial Order" (48127) is documented under "Letter to Stremstin" (48128); obtain another copy if needed.

## `MnkPre`

Values written: 1, 2, 3.

### 1. a fallen student — say hail

Zone: `lakerathe`.

> Eh? There is nothing I can help you with. I have nothing for myself anymore... except these [

Sets `MnkPre` to `1`.

- Needs `MnkPre` unset.
- Needs `monk_epic` unset.
In script order:

1. Sets `MnkPre` to `1`.


Subquest `monk_epic`:

#### `monk_epic`

Values written: 1, 2, 3, 4, 5, 6, 7, 8, 9.

##### 1. a fallen student — say hail

Zone: `lakerathe`.

> Eh? There is nothing I can help you with. I have nothing for myself anymore... except these [

Sets `monk_epic` to `1`.

- Needs `monk_epic` unset.
- One of: `MnkPre` ==3; Celestial Fists (10652).
In script order:

1. Sets `monk_epic` to `1`.


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
  - Sets `monk_epic_bloodfield` to `1`.
  - Spawns a chest (Epic 1.5) (283157).
- `bloodfields` player, on loot needs `monk_epic` set.
  - Sets `monk_epic_keeper` to `1`.
  - Spawns a chest (Epic 1.5) (283157).
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
- `lakerathe` a fallen student, say hail needs `monk_epic` unset.
  - Sets `MnkPre` to `1`.
- `lakerathe` a fallen student, say vortix needs `monk_epic` ==3.
  - Spawns Vortix (203433).
- `oceanoftears` kaiaren, say choose to continue needs `monk_epic` ==9.
  - Sets `mnk_epic20` to `3`.
- `oceanoftears` kaiaren, say choose to continue needs `monk_epic` ==9.
  - Gives Initiate's Sash of the Celestial Order (48127).
- `oceanoftears` kaiaren, say menace needs `monk_epic` ==9.
  - Sets `mnk_epic20` to `1`.
- `oot` kaiaren, say choose to continue needs `monk_epic` ==9.
  - Sets `mnk_epic20` to `3`.
- `oot` kaiaren, say choose to continue needs `monk_epic` ==9.
  - Gives Initiate's Sash of the Celestial Order (48127).
- `oot` kaiaren, say menace needs `monk_epic` ==9.
  - Sets `mnk_epic20` to `1`.
- `potranquility` vortix, say hail needs `monk_epic` >=5.
  - Gives Letter to Stremstin (48128).
- `westwastes` disciple of moon trap, on enter needs `monk_epic` ==5.
  - Spawns Disciple of Moon (120138).
  - Loots Symbol of Moon (48111).

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
  - Alternative: Loot "Medal of Identity" (48102) from "Mirror Reflection" (NPC 111190) in `frozenshadow`; trigger: frozenshadow/"You", on event_proximity_say.

### Steps on `MnkPre` that do not change it

- `lakerathe` a fallen student, say hail needs `MnkPre` ==3.
  - Sets `monk_epic` to `1`.

## `monk_epic`

See `monk_epic` earlier in this file.

## `mnk_epic20`

Values written: 1, 2, 3, 4, 5, 6.

### 1. kaiaren — say menace

Zones: `oceanoftears`, `oot`.

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

Zones: `oceanoftears`, `oot`.

> As I thought you would; you will find them as you did the others, in their natural essence. You will find the Disciple of Focus in the hills and mountains tr...

Sets `mnk_epic20` to `3`.

- Needs `mnk_epic20` >=2.
- Needs `mnk_epic20` set.
- Needs `monk_epic` ==9.
In script order:

1. Sets `mnk_epic20` to `3`.


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
  - Alternative: Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy" (NPC 317087) in `anguish`; trigger: anguish/"Zone Status", say "Check Uorb".
  - Alternative: Loot "Globe of Discordant Energy" (47100) from "Ornate Chest" (NPC 317112) in `anguish`; trigger: anguish/"Zone Status", say "Check Amv Chest".
  - Alternative: Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy" (NPC 317087) in `anguish`; trigger: anguish/"Zone Status", on event_signal.
  - Alternative: Loot "Globe of Discordant Energy" (47100) from "Overlords Chest" (NPC 317124) in `anguish`; trigger: anguish/"Zone Status", on event_signal.

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
