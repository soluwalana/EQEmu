# Ranger

Steps taken from the quest graph only. **Broken** means the graph has no edge for that value or that item.

Flags with writes: `ranger_epic`, `ranger_epic15_pre`.

## 0. Prerequisites

Shared acquisition steps appear in the first prerequisite chain that needs them. Later sections reference that chain rather than repeating it.

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
27. Alternative: Loot "Jade Reaver" (5664) from "A Black Reaver" (NPC 90005) in `citymist`; trigger: citymist/"A Black Reaver", on event_death_complete.
28. Alternative: Loot "Jade Reaver" (5664) from "A Black Reaver" (NPC 90192) in `citymist`; trigger: citymist/"A Black Reaver", on event_death_complete.
29. kaladimb/"Kinlo Strongarm", hand "Jade Reaver" (5664). Gives "Enchanted Clay" (20455).
30. Forage "Rose of Firiona" (12774) in `firiona`.
31. qrg/"Merdan Fleetfoot", hand "Rose of Firiona" (12774). Gives "Wood Painting" (20475).
32. frontiermtns/"A Human Skeleton", hand "Wood Painting" (20475). Gives "Silver Chained Locket" (20476).
33. qrg/"Niera Farbreeze", hand "Silver Chained Locket" (20476). Gives "Platinum Speckled Powder" (20456).
34. Combine in Pottery Wheel (21): "Ancient Pattern" (18960), "Enchanted Clay" (20455), "Platinum Speckled Powder" (20456). Produces "Runecrested Bowl" (20460). Requires Pottery. The combine does not fail.
35. misty/"Ella Foodcrafter", hand "Runecrested Bowl" (20460) + "Hardened Mixture" (20473). Gives "Softly Glowing Stone" (20462).
36. Common item: Spell: Resurrection (15392). Listed in 14 zones.
37. Hand "Spell: Resurrection" (15392) to karnor/"Spirit Of Venril Sathir". Spawns "Venril Sathir" (102126). Loot "Pulsing Green Stone" (20461) from "Venril Sathir".
38. firiona/"Foloal Stormforest", hand "Pulsing Green Stone" (20461) + "Softly Glowing Stone" (20462). Gives "Warmly Glowing Stone" (20468).
39. burningwood/"Telin Darkforest", hand "Warmly Glowing Stone" (20468). Gives "Ancient Longsword" (20477).
40. kaladimb/"Usbak The Old", hand "Ancient Longsword" (20477). Gives "Refined Ancient Sword" (20481).
41. burningwood/"Faelin Bloodbriar", hand "Refined Ancient Sword" (20481). Gives "Swiftwind" (20487).

### "Earthcaller" (20488)

1. Acquisition of "Shiny Tin Bowl" (17860) is documented under "Swiftwind" (20487); obtain another copy if needed.
2. Hand "Shiny Tin Bowl" (17860) to hole/"Jaeil The Wretched". Spawns "Jaeil the Insane" (39154). Loot "Soulbound Hammer" (20478) from "Jaeil the Insane".
3. erudnint/"Mairee Silentone", hand "Soulbound Hammer" (20478). Gives "Dwarven Smiths Hammer" (20479).
4. Kill airplane/"An Essence Carrier". Spawns "An Essence Tamer" (71071).
5. Loot "Swirling Sphere of Color" (20494) from "An Essence Tamer".
6. erudnint/"Mairee Silentone", hand "Dwarven Smiths Hammer" (20479) + "Swirling Sphere of Color" (20494). Gives "Hammer of the Ancients" (20485).
7. kaladimb/"Kinlo Strongarm", hand "Hammer of the Ancients" (20485). Gives "Small bit of Mithril Ore" (20482).
8. kaladimb/"Kinlo Strongarm", hand "Small bit of Mithril Ore" (20482). Gives "Refined Mithril Blade" (20483).
9. Encounter starts when NPC 186201 spawns in `hateplaneb`.
10. Starts timer `popinny`.
11. Kill NPC 186158.
12. Starts timer `text`.
13. Starts timer `text2`.
14. Starts timer `spawninny`.
15. Spawns "Innoruuk" (186107) after `hateplaneb/inny#timer:spawninny`.
16. Loot "Shattered Emerald of Corruption" (20484) from "Innoruuk".
17. Alternative: Loot "Shattered Emerald of Corruption" (20484) from "Maestro of Rancor" (NPC 186111) in `hateplaneb`; trigger: hateplaneb/"Maestro", on timer popmaestro.
18. northkarana/"Xanuusus", hand "Refined Mithril Blade" (20483) + "Shattered Emerald of Corruption" (20484). Gives "Earthcaller" (20488).

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

### "Sound Capture Jar" (62637)

1. nedaria/"Targen Stonefall", say "Impurities". Sets `ranger_epic15_pre` to `6`.
2. Acquisition of "Polished Blasted Stone" (62603) is documented under "Polished Blasted Stone" (62603); obtain another copy if needed.
3. northkarana/"Xanuusus", hand "Polished Blasted Stone" (62603). Sets `ranger_epic15_pre` to `7`.
4. Loot "Taskmaster's Cutlass" (62631) from "Taskmaster Waggad Brokenskull" in `torgiran`.
5. torgiran/"Player", on loot. Sets `ranger_epic15_pre` to `8`.
6. Say "Ready" to northkarana/"Xanuusus".
7. Spawns "A Tainted Beast" (13131).
8. Loot "Stone of Winde" (62604) from "A Tainted Beast".
9. northkarana/"Xanuusus", hand "Stone of Winde" (62604). Sets `ranger_epic15_pre` to `9`.
10. steamfont/"Godbin Strumharp", hand platinum:30. Requires `ranger_epic15_pre` ==9. Gives "Sound Capture Jar" (62637).

### "Closed Sample Cloth" (62641)

1. Acquisition of "Closed Sample Cloth" (62641) is documented under "Polished Blasted Stone" (62603); obtain another copy if needed.

### "Stone of Winde" (62604)

1. Acquisition of "Stone of Winde" (62604) is documented under "Sound Capture Jar" (62637); obtain another copy if needed.

### "Corun's Notes" (62617)

1. Forage "Sickly Maiden's Hair" (62810) in `rathemtn`.
2. eastkarana/"Althele", hand "Sickly Maiden's Hair" (62810). Gives "Tuft of Sickly Maiden's Hair" (62811).
3. qrg/"Corun Finisc", hand "Tuft of Sickly Maiden's Hair" (62811). Gives "Borrowed Medicine Bag" (62605).
4. eastkarana/"Althele", say "Hail". Sets `ranger_epic` to `1`.
5. Spawns "An Asteatotic Highborn" (109907) in `veksar` on enter.
6. Loot "Asteatotic Veksar Blood" (35100) from "An Asteatotic Highborn".
7. Spawns "A Neuralgic Huntress" (120136) in `westwastes` on enter.
8. Loot "Neuralgic Wyvern Blood" (72605) from "A Neuralgic Huntress".
9. Summon "Collapsible Fletching Kit" (17189) by casting "Unfold Fletching Kit".
10. qrg/"Corun Finisc", hand "Tuft of Sickly Maiden's Hair" (62811). Gives "Magical Sample Vial" (62657).
11. cazicthule/"A Sickly Mosquito", on event hp.
12. Starts timer `check`.
13. No quest step gives Planar Fletching Kit (17762). The dump lists it in poknowledge.
14. Common item: Whittling Knife (62608). Listed in 4 zones.
15. Forage "Fallen Tree Branch" (62652) in `dranik`.
16. Forage "Fallen Tree Branch" (62652) in `draniksscar`.
17. Combine in "Planar Fletching Kit" (17762): "Whittling Knife" (62608), "Fallen Tree Branch" (62652). Produces "Long Net Pole" (62607). Requires Fletching 100. Trivial at 15. The combine does not fail.
18. Spawns "A Phase Spider" (123190) in `necropolis` on event_combat.
19. Loot "Phase Spider Silk" (55303) from "A Phase Spider".
20. Forage "Pine Sap" (62650) in `jaggedpine`.
21. Forage "Pine Sap" (62650) in `nedaria`.
22. Forage "Pine Sap" (62650) in `qrg`.
23. Combine in "Planar Fletching Kit" (17762): "Phase Spider Silk" (55303), "Pine Sap" (62650). Produces "Phase Netting" (62651). Requires Fletching 100. Trivial at 15. The combine does not fail.
24. Combine in "Planar Fletching Kit" (17762): "Long Net Pole" (62607), "Phase Netting" (62651). Produces "Large Butterfly Net" (62646). Requires Fletching 100. Trivial at 15. The combine does not fail.
25. Equip "Large Butterfly Net" (62646) in primary slot.
26. cazicthule/"A Sickly Mosquito", on timer check. Gives "Captured Mosquito" (62642).
27. Combine in "Collapsible Fletching Kit" (17189): "Magical Sample Vial" (62657), "Captured Mosquito" (62642). Produces "Sickly Mosquito Blood Sample" (62611). Requires Fletching. The combine does not fail.
28. sirens/"A Twitching Swordfish", on event hp.
29. Starts timer `check`.
30. Equip "Large Butterfly Net" (62646) in primary slot.
31. sirens/"A Twitching Swordfish", on timer check. Gives "Captured Swordfish" (62643).
32. Combine in "Collapsible Fletching Kit" (17189): "Magical Sample Vial" (62657), "Captured Swordfish" (62643). Produces "Twitching Swordfish Blood Sample" (62612). Requires Fletching. The combine does not fail.
33. chardokb/"A Leprous Chokidai", on event hp.
34. Starts timer `check`.
35. Common item: Hinge Mold (12027). Listed in 25 zones.
36. Common item: Container Base Mold (12062). Listed in 14 zones.
37. Common item: Container Lid Mold (12069). Listed in 14 zones.
38. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
39. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `steamfont`.
40. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `tox`.
41. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `toxxulia`.
42. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
43. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). The combine does not fail.
44. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
45. No quest step gives Small Brick of Steel (66168). The dump lists it in qrg.
46. qrg/"Qaelin Hailstorm", say "Need A Mark". Gives "Mark of Karana" (66172).
47. Combine in Forge (17): "Hinge Mold" (12027), "Container Base Mold" (12062), "Container Lid Mold" (12069), "Water Flask" (13006), "Small Brick of Steel" (66168), "Mark of Karana" (66172). Hands back "Mark of Karana" (66172). Produces "Surefall Fletching Kit" (66163). Requires Blacksmithing, trivial 163.
48. Loot "Smithy Hammer" (10489) from "Gliblixl Rocktok" in `bazaar`.
49. Forage "Golanda Nut" (62610) in `causeway`.
50. Forage "Golanda Nut" (62610) in `dranik`.
51. Forage "Golanda Nut" (62610) in `draniksscar`.
52. Forage "Golanda Nut" (62610) in `provinggrounds`.
53. Forage "Golanda Nut" (62610) in `riftseekers`.
54. Forage "Golanda Nut" (62610) in `wallofslaughter`.
55. Combine in "Surefall Fletching Kit" (66163): "Smithy Hammer" (10489), "Golanda Nut" (62610). Hands back "Smithy Hammer" (10489). Produces "Fibrous Rope" (62609). Requires Fletching 100. Trivial at 15. The combine does not fail.
56. Combine in "Surefall Fletching Kit" (66163): "Fibrous Rope" (62609). Produces "Eight-loop Lasso" (62648). Requires Fletching 100. Trivial at 15. The combine does not fail.
57. Equip "Eight-loop Lasso" (62648) in primary slot.
58. chardokb/"A Leprous Chokidai", on timer check. Gives "Captured Chokidai" (62645).
59. Combine in "Collapsible Fletching Kit" (17189): "Magical Sample Vial" (62657), "Captured Chokidai" (62645). Produces "Leprous Chokidai Blood Sample" (62614). Requires Fletching. The combine does not fail.
60. droga/"A Bloated Drogan Spider", on event hp.
61. Starts timer `check`.
62. Equip "Eight-loop Lasso" (62648) in primary slot.
63. droga/"A Bloated Drogan Spider", on timer check. Gives "Captured Spider" (62644).
64. Combine in "Collapsible Fletching Kit" (17189): "Magical Sample Vial" (62657), "Captured Spider" (62644). Produces "Bloated Drogan Spider Blood Sample" (62613). Requires Fletching. The combine does not fail.
65. Combine in "Borrowed Medicine Bag" (62605): "Asteatotic Veksar Blood" (35100), "Neuralgic Wyvern Blood" (72605), "Sickly Mosquito Blood Sample" (62611), "Twitching Swordfish Blood Sample" (62612), "Leprous Chokidai Blood Sample" (62614), "Bloated Drogan Spider Blood Sample" (62613). Produces "Full Medicine Bag" (62616). The combine does not fail.
66. qrg/"Corun Finisc", hand "Full Medicine Bag" (62616). Gives "Corun's Notes" (62617).

### "Block of Purest Silver" (62625)

1. global/"Global Player", combine recipe 13412. Sets `ranger_epic` to `3`.
2. jaggedpine/"Red Dogwood Treant", say "Hail". Requires `ranger_epic` ==3. Gives "Spring Dogwood Seed" (62624).
3. qrg/"Corun Finisc", hand "Spring Dogwood Seed" (62624). Gives "Block of Purest Silver" (62625).

### "Wind-blessed Heartwood" (62626)

1. jaggedpine/"Red Dogwood Treant", say "Hail". Requires `ranger_epic` ==3. Gives "Red Dogwood Heartwood" (62623).
2. dranik/"Ranger 1 5", hand "Red Dogwood Heartwood" (62623). Requires `ranger_dranik_chest` unset. Gives "Wind-blessed Heartwood" (62626).

### "Heated Loadstone" (62628)

1. global/"Global Player", combine recipe 13413. Sets `ranger_epic` to `5`.
2. nedaria/"A Wayfarers Brotherhood Officer", say "Hail". Sets `ranger_epic` to `6`.
3. causeway/"Siflu", say "Adventurers". Requires `ranger_epic` ==6. Gives "Heated Loadstone" (62628).

### "Elemental Ice Spirit Cage" (62647)

1. Loot "Crooked Cage" (32042) from "a Broken Skull bruiser" in `torgiran`.
2. Acquisition of "Earthcaller" (20488) is documented under "Earthcaller" (20488); obtain another copy if needed.
3. Acquisition of "Swiftwind" (20487) is documented under "Swiftwind" (20487); obtain another copy if needed.
4. Loot "Living Fragment of Fire" (28294) from "A Jopal Mystic" (NPC 217026) in `pofire`. Drop cache: 5.04% chance per kill.
5. Loot "Living Fragment of Water" (28293) from "A Triloun Diviner" in `powater`.
6. Loot "Living Fragment of Water" (28293) from "A Triloun Keeper" in `powater`.
7. Loot "Living Fragment of Water" (28293) from "A Triloun Water Guardian" in `powater`.
8. Acquisition of "Heated Loadstone" (62628) is documented under "Heated Loadstone" (62628); obtain another copy if needed.
9. Spawns "A Mangled Muramite Captain" (300069) in `wallofslaughter` on enter.
10. Loot "Spirit Manacles" (72340) from "A Mangled Muramite Captain".
11. Combine in "Crooked Cage" (32042): "Earthcaller" (20488), "Swiftwind" (20487), "Living Fragment of Fire" (28294), "Living Fragment of Water" (28293), "Heated Loadstone" (62628), "Spirit Manacles" (72340). Hands back "Earthcaller" (20488), "Swiftwind" (20487). Produces "Spirit Cage" (62656). The combine does not fail.
12. global/"Global Player", combine recipe 19914. Sets `ranger_epic` to `8`.
13. Spawns "Craftmaster Tieranu" (334087) in `riftseekers` on enter.
14. Loot "Ring of Warmth" (11427) from "Craftmaster Tieranu".
15. Spawns "Herrian Warfrost" (300057) in `wallofslaughter` on enter.
16. Loot "Hoarfrost Wand" (76999) from "Herrian Warfrost".
17. Combine in "Spirit Cage" (62656): "Ring of Warmth" (11427), "Hoarfrost Wand" (76999). Produces "Elemental Ice Spirit Cage" (62647). The combine does not fail.

### "Heartwood Blade" (62627)

1. Acquisition of "Planar Fletching Kit" (17762) is documented under "Corun's Notes" (62617); obtain another copy if needed.
2. Acquisition of "Wind-blessed Heartwood" (62626) is documented under "Wind-blessed Heartwood" (62626); obtain another copy if needed.
3. Acquisition of "Block of Purest Silver" (62625) is documented under "Block of Purest Silver" (62625); obtain another copy if needed.
4. Combine in "Planar Fletching Kit" (17762): "Wind-blessed Heartwood" (62626), "Block of Purest Silver" (62625). Produces "Heartwood Blade" (62627). Requires Fletching. The combine does not fail.

### "Senvial's Blessing" (62621)

1. Spawns "An Ancient Thought Horror" (164122) in `thedeep` on enter.
2. Loot "Thick Spinal Fluid" (40420) from "An Ancient Thought Horror".
3. Acquisition of "Corun's Notes" (62617) is documented under "Corun's Notes" (62617); obtain another copy if needed.
4. freeportwest/"Shana Liskia", hand "Corun's Notes" (62617). Gives "Corun's Notes - annotated" (62654).
5. freeportwest/"Shana Liskia", hand "Thick Spinal Fluid" (40420) + "Corun's Notes - annotated" (62654). Gives "Mind Crystal" (62846).
6. eastkarana/"Tholris", say "You Are Diseased". Gives "Red Crystal" (62618).
7. eastkarana/"Tholris", say "You Are Diseased". Gives "Violet Crystal" (62619).
8. freeportwest/"Shana Liskia", hand "Red Crystal" (62618) + "Violet Crystal" (62619). Gives "Letter to Corun" (62655).
9. qrg/"Corun Finisc", hand "Letter to Corun" (62655) + "Mind Crystal" (62846). Gives "Red Dogwood Seed" (62844).
10. freeportwest/"Shana Liskia", hand "Corun's Notes" (62617). Sets `ranger_epic` to `2`.
11. natimbi/"Ranger 1 5", say "Hail". Requires `ranger_epic` set. Requires `ranger_epic` ==2. Gives "Senvial's Blessing" (62621).

### "Grinbik's Blessing" (62622)

1. Acquisition of "Red Dogwood Seed" (62844) is documented under "Senvial's Blessing" (62621); obtain another copy if needed.
2. bloodfields/"Ranger 1 5", say "Hail". Requires `ranger_epic` ==2. Gives "Grinbik's Blessing" (62622).

### "Red Dogwood Seed" (62844)

1. Acquisition of "Red Dogwood Seed" (62844) is documented under "Senvial's Blessing" (62621); obtain another copy if needed.

## `ranger_epic`

Values written: 1, 2, 3, 5, 6, 7.

### 1. althele — say hail

Zone: `eastkarana`.

> Hello, friend. Beautiful is what I would call such a day normally, but lately? I sense that something is [

Sets `ranger_epic` to `1`.

- Needs `ranger_epic` unset.
In script order:

1. Sets `ranger_epic` to `1`.


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
- `bloodfields` ranger 1 5, say hail needs `ranger_epic` ==2.
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
- `jaggedpine` red dogwood treant, say hail needs `ranger_epic` ==3.
  - Gives Red Dogwood Heartwood (62623).
  - Gives Spring Dogwood Seed (62624).
- `natimbi` ranger 1 5, say hail needs `ranger_epic` set.
  - Gives Senvial's Blessing (62621).
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
- `natimbi` trenzar trap, on enter needs `ranger_epic` ==2.
  - Sets `ranger_epic_natimbi` to `1`.
  - Spawns Spiritbinder Trenzar (280084).
  - Spawns a bound earth spirit (280085).
  - Spawns a bound fire spirit (280086).
- `thedeep` player, on enter needs `ranger_epic` ==2.
  - Sets `ranger_epic_deep` to `1`.
  - Spawns ancient thought horror trap (164123).
- `veksar` player, on enter needs `ranger_epic` ==1.
  - Sets `ranger_epic_veks` to `1`.
  - Spawns an asteatotic highborn (109907).
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
    - Alternative: Loot "Living Fragment of Earth" (28295) from "A Vekerchiki Warrior" (NPC 218025) in `poeartha`; trigger: poeartha/"Vekerchiki Trap", on event_combat.
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
  - Alternative: Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy" (NPC 317087) in `anguish`; trigger: anguish/"Zone Status", say "Check Uorb".
  - Alternative: Loot "Globe of Discordant Energy" (47100) from "Ornate Chest" (NPC 317112) in `anguish`; trigger: anguish/"Zone Status", say "Check Amv Chest".
  - Alternative: Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy" (NPC 317087) in `anguish`; trigger: anguish/"Zone Status", on event_signal.
  - Alternative: Loot "Globe of Discordant Energy" (47100) from "Overlords Chest" (NPC 317124) in `anguish`; trigger: anguish/"Zone Status", on event_signal.
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
  - Sets `rng_spawn_wos` to `1`.
  - Spawns Herrian Warfrost (300057).
  - Spawns an excited builder (300058).
  - Loots Gelidran Blood (72073).
  - Loots Hoarfrost Wand (76999).
  - Loots Polished Blue Softstone (80030).
  - Loots Sunshard Powder (35088).
  - Loots Platinum Etched Reinforced Rod (37046).
  - Loots Raw Crimson Nihilite (58067).
- `wallofslaughter` player, on loot needs `ranger_epic` ==8.
  - Sets `rng_wos_chest` to `1`.
  - Spawns a chest (Epic 1.5) (893).

## Other flags touched along the way

- `ranger_epic_bloodfield` set to 1 at bloodfields/marshall trap.
- `ranger_epic_deep` set to 1 at thedeep/player.
- `ranger_epic_dranik` set to 1 at dranik/sverins trap.
- `ranger_epic_natimbi` set to 1 at natimbi/trenzar trap.
- `ranger_epic_veks` set to 1 at veksar/player.
- `ranger_epic_wyv` set to 1 at westwastes/player.
