# Enchanter

Steps taken from the quest graph only. **Broken** means the graph has no edge for that value or that item.

Flags with writes: `EnchPre`, `ench_epic`.

## 0. Prerequisites

Shared acquisition steps appear in the first prerequisite chain that needs them. Later sections reference that chain rather than repeating it.

### "Illegible Tome" (52947)

1. Loot "Dragon Boneshard" (65574) from "A Curate" (NPC 109068) in `veksar`. Drop cache: 10% chance per kill.
2. Hand "Dragon Boneshard" (65574) to veksar/"Spirit Of Garudon". Spawns "Garudon" (109107). Loot "Garudon's Statue" (52941) from "Garudon".
3. lakeofillomen/"A Bloodgill Mimic", hand "Garudon's Statue" (52941). Sets `EnchPre` to `1`.
4. Loot "Crumbling Tome" (54313) from "A Shissar Lorekeeper" in `ssratemple`.
5. ssratemple/"A Soriz Imitator", hand "Crumbling Tome" (54313). Requires `EnchPre` ==1. Gives "Illegible Tome" (52947).

### "Gnomish Translating Device" (52945)

1. Acquisition of "Illegible Tome" (52947) is documented under "Illegible Tome" (52947); obtain another copy if needed.
2. akanon/"Rilgor Plegnog", say "Insidious". Gives "Compacting Satchel" (54303).
3. Loot "Fine Insidious Halo" (54384) from "A Forsaken Revenant" (NPC 186146) in `hateplaneb`. Drop cache: 2% chance per kill.
4. Loot "Fine Insidious Sleeves" (54385) from "A Forsaken Revenant" (NPC 186146) in `hateplaneb`. Drop cache: 2.08% chance per kill.
5. Loot "Fine Insidious Manacle" (54386) from "A Forsaken Revenant" (NPC 186146) in `hateplaneb`. Drop cache: 2.09% chance per kill.
6. Loot "Fine Insidious Gloves" (54387) from "A Forsaken Revenant" (NPC 186146) in `hateplaneb`. Drop cache: 2.24% chance per kill.
7. Loot "Fine Insidious Pantaloons" (54388) from "A Forsaken Revenant" (NPC 186146) in `hateplaneb`. Drop cache: 2.23% chance per kill.
8. Loot "Fine Insidious Slippers" (54389) from "A Forsaken Revenant" (NPC 186146) in `hateplaneb`. Drop cache: 2.07% chance per kill.
9. Combine in "Compacting Satchel" (54303): "Fine Insidious Halo" (54384), "Fine Insidious Sleeves" (54385), "Fine Insidious Manacle" (54386), "Fine Insidious Gloves" (54387), "Fine Insidious Pantaloons" (54388), "Fine Insidious Slippers" (54389). Produces "Insidious Bundle" (54317). The combine does not fail.
10. akanon/"Rilgor Plegnog", hand "Insidious Bundle" (54317). Gives "Gnomish Translating Device" (52945).

### "Complete Illegible Tome" (54267)

1. Acquisition of "Illegible Tome" (52947) is documented under "Illegible Tome" (52947); obtain another copy if needed.
2. Acquisition of "Gnomish Translating Device" (52945) is documented under "Gnomish Translating Device" (52945); obtain another copy if needed.
3. burningwood/"A Sarnak Imitator", hand "Gnomish Translating Device" (52945) + "Illegible Tome" (52947). Sets `EnchPre` to `2`.
4. burningwood/"A Sarnak Imitator", say "Hail". Sets `ench_epic` to `1`.
5. burningwood/"A Sarnak Imitator", say "Prepared". Requires `ench_epic` set. Requires `ench_epic` >=1. Gives "Tattered Illegible Tome" (57918).
6. Ground spawn of "Cryptic Page" (52933) in `charasis`.
7. Ground spawn of "Cryptic Page" (52934) in `sebilis`.
8. Ground spawn of "Cryptic Page" (52935) in `cazicthule`.
9. Ground spawn of "Cryptic Page" (52936) in `crystal`.
10. Ground spawn of "Cryptic Page" (52937) in `skyshrine`.
11. Ground spawn of "Cryptic Page" (52938) in `velketor`.
12. Ground spawn of "Cryptic Page" (52939) in `nadox`.
13. Ground spawn of "Cryptic Page" (54308) in `najena`.
14. Ground spawn of "Cryptic Page" (57916) in `fungusgrove`.
15. Ground spawn of "Cryptic Page" (57923) in `oot`.
16. Combine in "Tattered Illegible Tome" (57918): "Cryptic Page" (52933), "Cryptic Page" (52934), "Cryptic Page" (52935), "Cryptic Page" (52936), "Cryptic Page" (52937), "Cryptic Page" (52938), "Cryptic Page" (52939), "Cryptic Page" (54308), "Cryptic Page" (57916), "Cryptic Page" (57923). Produces "Complete Illegible Tome" (54267). The combine does not fail.

### "Sealed Documents" (52959)

1. Acquisition of "Complete Illegible Tome" (54267) is documented under "Complete Illegible Tome" (54267); obtain another copy if needed.
2. burningwood/"A Sarnak Imitator", hand "Complete Illegible Tome" (54267). Sets `ench_epic` to `2`.
3. poknowledge/"Grand Librarian Maelin", say "Jeb Lumsed Sent Me". Requires `ench_epic` ==2. Gives "Note to Lobaen" (52950).
4. poknowledge/"Illusionist Lobaen", hand "Note to Lobaen" (52950). Gives "Sealed Documents" (52959).

### "Latched Ornate Chest" (52966)

1. global/"Global Player", combine recipe 19919. Sets `ench_epic` to `9`.
2. burningwood/"A Sarnak Imitator", say "Chest". Requires `ench_epic` set. Requires `ench_epic` >=3. Gives "Ornate Staff Chest" (52960).
3. Ground spawn of "Taste of Enticement" (52964) in `mistmoore`.
4. frozenshadow/"Advisor Svartmane", hand "Taste of Enticement" (52964). Gives "1st Piece of the Staff" (54289).
5. Loot "2nd Piece of the Staff" (54310) from "The Yrendan Scarab" in `pojustice`.
6. Loot "3rd Piece of the Staff" (54299) from "Chavoor the Trickster" in `vxed`.
7. Loot "3rd Piece of the Staff" (54299) from "Ikaav Firecaller" in `vxed`.
8. Loot "3rd Piece of the Staff" (54299) from "Kyv Hunter" in `vxed`.
9. Loot "3rd Piece of the Staff" (54299) from "Ukun Bloodbeast" in `vxed`.
10. Loot "3rd Piece of the Staff" (54299) from "Umbiki" in `vxed`.
11. Loot "3rd Piece of the Staff" (54299) from "misguided beludu Creque" in `vxed`.
12. **Broken:** no event trigger found for `bloodfields/war#timer:reset`.
13. Spawns "War Caller Kaavi" (301042) after `bloodfields/war#timer:reset`.
14. Loot "4th Piece of the Staff" (54284) from "War Caller Kaavi".
15. Loot "Ornate Staff Topper" (52961) from "Faleniel of Darkwater" in `sirens`.
16. Loot "All-Seeing Eye" (54293) from "All-Seeing Eye" in `mischiefplane`.
17. potranquility/"Elder Fuirstel", say "Hail". Sets `pop_cod_final` to `1`.
18. poknowledge/"Aid Grimel", say "Skill In Brewing". Requires `pop_cod_final` ==1. Requires `pop_cod_final` set. Gives "Portable Drink Barrel" (17179).
19. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
20. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `steamfont`.
21. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `tox`.
22. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `toxxulia`.
23. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
24. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). The combine does not fail.
25. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
26. Forage "Dragon Egg" (19139) in `templeveeshan`.
27. Forage "Dragon Egg" (19139) in `westwastes`.
28. Combine in "Portable Drink Barrel" (17179): "Water Flask" (13006), "Dragon Egg" (19139). Produces "Dragon Egg Oil" (9664). Requires Brewing, trivial 150.
29. Loot "Glimmering Oil" (52942) from "A Greasy Clockwork" in `poinnovation`.
30. bazaar/"Caerlyna", hand "Spell Research Kit" (93492). Gives "Spell Research Kit Token" (93667).
31. bazaar/"Caerlyna", hand "Spell Research Kit Token" (93667). Gives "Spell Research Kit" (93492).
32. Common item: Firing Sheet (16906). Listed in 34 zones.
33. Combine in Pottery Wheel (21): "Water Flask" (13006), "Block of Clay" (16901). Produces "Small Block of Clay" (16900) x3. Requires Pottery, trivial 21.
34. Combine in Pottery Wheel (21): "Small Block of Clay" (16900), "Water Flask" (13006). Produces "Block of Clay" (16901). Requires Pottery, trivial 21.
35. Combine in Pottery Wheel (21): "Block of Clay" (16901), "Water Flask" (13006). Produces "Large Block of Clay" (16902). Requires Pottery, trivial 21.
36. Common item: Large Bowl Sketch (16963). Listed in 29 zones.
37. Combine in Pottery Wheel (21): "Large Block of Clay" (16902), "Water Flask" (13006), "Large Bowl Sketch" (16963). Produces "Unfired Mixing Bowl" (16930). Requires Pottery, trivial 128.
38. Combine in Kiln (22): "Firing Sheet" (16906), "Unfired Mixing Bowl" (16930). Produces "Mixing Bowl" (17906). Requires Pottery, trivial 15.
39. Common item: Celestial Solvent (9731). Listed in 13 zones.
40. Loot "Fetid Skin" (13150) from "A Fetid Fiend" (NPC 72059) in `fearplane`. Drop cache: 35% chance per kill.
41. Loot "Scare Straw" (13152) from "A Samhain" in `fearplane`.
42. Loot "Turmoil Warts" (8331) from "A Turmoil Toad" in `fearplane`.
43. Spawns "Grimling" (154129) in `acrylia` on event_spawn.
44. Loot "Pearl" (10024) from "Grimling".
45. 14 alternative loot source(s) also yield Pearl (10024).
46. neriaka/"X-Ta Tompi", hand "Turmoil Warts" (8331) + "Pearl" (10024) + "Fetid Skin" (13150) + "Scare Straw" (13152). Gives "Words of Acquisition (Beza)" (11866).
47. Combine in "Mixing Bowl" (17906): "Celestial Solvent" (9731), "Words of Acquisition (Beza)" (11866). Produces "Celestial Essence" (9650). Requires Baking, trivial 15. The combine does not fail.
48. Loot "Coalesced Mana" (97042) from "Assistant Gareth" (NPC 371049) in `skylance`. Drop cache: 66.67% chance per kill.
49. Loot "White Wolf Skin" (13768) from "A Snow Wolf" in `everfrost`.
50. Loot "White Wolf Skin" (13768) from "A White Wolf" in `everfrost`.
51. Common item: Vial Sketch (16968). Listed in 30 zones.
52. Combine in Pottery Wheel (21): "Water Flask" (13006), "White Wolf Skin" (13768), "Small Block of Clay" (16900), "Vial Sketch" (16968). Produces "Unfired Poison Vial" (16885). Requires Pottery, trivial 148.
53. Common item: High Quality Firing Sheet (16908). Listed in 34 zones.
54. Combine in Kiln (22): "Unfired Poison Vial" (16885), "High Quality Firing Sheet" (16908). Produces "Poison Vial" (16965). Requires Pottery, trivial 17.
55. Spawns "Pxet Elite Blademaster" (284039) in `ferubi` on event_signal.
56. Loot "Broken Sword Blade" (67521) from "Pxet Elite Blademaster".
57. Spawns "Pxet Elite Spearmaster" (284091) in `ferubi` on event_signal.
58. Loot "Jagged Spear Tip" (67522) from "Pxet Elite Spearmaster".
59. Spawns "Pxet Elite Brawler" (284088) in `ferubi` on event_signal.
60. Loot "Tarnished Knuckles" (67523) from "Pxet Elite Brawler".
61. Spawns "Pxet Elite Hammermaster" (284090) in `ferubi` on event_signal.
62. Loot "Chipped Hammer Head" (67524) from "Pxet Elite Hammermaster".
63. Hand "Broken Sword Blade" (67521) + "Jagged Spear Tip" (67522) + "Tarnished Knuckles" (67523) + "Chipped Hammer Head" (67524) to ferubi/"Smith Rondo". Spawns "Master's Apprentice" (284093). Loot "Ruby" (10035) from "Master's Apprentice".
64. 107 alternative loot source(s) also yield Ruby (10035).
65. Combine in "Spell Research Kit" (93492): "Celestial Essence" (9650), "Coalesced Mana" (97042), "Poison Vial" (16965), "Ruby" (10035). Produces "Vial of Purified Mana" (10254). Requires Research, trivial 200.
66. Forage "Glow Lichen" (14925) in `nektulos`.
67. Loot "Essence of Sunlight" (22527) from "A Faerie Dragon" (NPC 119073) in `wakening`. Drop cache: 55% chance per kill.
68. Ground spawn of "Abysmal Moonwater" (54298) in `abysmal`.
69. Combine in Brew Barrel (19): "Vial of Purified Mana" (10254), "Glow Lichen" (14925), "Essence of Sunlight" (22527), "Abysmal Moonwater" (54298). Produces "Glowing Concoction" (52943). Requires Brewing, trivial 116.
70. Common item: Medicine Bag (17901). Listed in 33 zones.
71. Common item: Glaze Lacquer (29355). Listed in 5 zones.
72. No quest step gives Prism Shard (65469). The dump lists it in crescent, gunthak, poknowledge.
73. Combine in "Medicine Bag" (17901): "Glaze Lacquer" (29355), "Prism Shard" (65469). Produces "Prismatic Dye" (65472). Requires Alchemy, trivial 54.
74. Combine in Brew Barrel (19): "Dragon Egg Oil" (9664), "Glimmering Oil" (52942), "Glowing Concoction" (52943), "Prismatic Dye" (65472). Produces "Incandescent Oil" (57924). Requires Brewing, trivial 116. The combine does not fail.
75. Acquisition of "Sealed Documents" (52959) is documented under "Sealed Documents" (52959); obtain another copy if needed.
76. burningwood/"A Sarnak Imitator", hand "Sealed Documents" (52959). Gives "Assembling the Staff" (54286).
77. Loot "Sullied Gold Filigree" (52963) from "An Enticing Potameid" in `natimbi`.
78. hohonora/"Anthone Chapin", hand "Sullied Gold Filigree" (52963). Gives "Purified Gold Filigree" (52953).
79. Combine in "Ornate Staff Chest" (52960): "1st Piece of the Staff" (54289), "2nd Piece of the Staff" (54310), "3rd Piece of the Staff" (54299), "4th Piece of the Staff" (54284), "Ornate Staff Topper" (52961), "All-Seeing Eye" (54293), "Incandescent Oil" (57924), "Purified Gold Filigree" (52953). Produces "Latched Ornate Chest" (52966). The combine does not fail.

### "Oculus of Persuasion" (52952)

1. Acquisition of "Latched Ornate Chest" (52966) is documented under "Latched Ornate Chest" (52966); obtain another copy if needed.
2. burningwood/"A Sarnak Imitator", hand "Latched Ornate Chest" (52966). Gives "Oculus of Persuasion" (52952).

### "Purifying Crystal" (52954)

1. No quest step gives Planar Jeweler's Kit (17764). The dump lists it in abysmal, poknowledge.
2. Acquisition of "Oculus of Persuasion" (52952) is documented under "Oculus of Persuasion" (52952); obtain another copy if needed.
3. Loot "Heart of a Twisted Stoneservant" (54239) from "A Twisted Stoneservant" in `riwwi`.
4. Hand "Heart of a Twisted Stoneservant" (54239) to wakening/"Alaurin". Spawns "A Luminescent Geonid" (119184). Loot "Luminescent Crystal" (52949) from "A Luminescent Geonid".
5. wakening/"Alaurin", hand "Luminescent Crystal" (52949). Gives "Purifying Crystal Fragment" (52955).
6. Loot "Volatile Vampyre Blood" (52965) from "a Coterie insatiate" in `tenebrous`.
7. westwastes/"Vohnkare", hand "Volatile Vampyre Blood" (52965). Gives "Purifying Crystal Fragment" (52956).
8. No quest step gives Gnomish Candy (52944). The dump lists it in akanon.
9. No quest step gives Koada`Dal Silk (52948). The dump lists it in felwithea, felwitheb.
10. No quest step gives Feir`Dal Champagne (52940). The dump lists it in gfaydark, katta, rivervale.
11. No quest step gives Dwarven Steel (57921). The dump lists it in kaladima.
12. lfaydark/"A Brownie Noble", hand "Feir'Dal Champagne" (52940) + "Gnomish Candy" (52944) + "Koada'Dal Silk" (52948) + "Dwarven Steel" (57921). Sets `ench_epic` to `8`.
13. Loot "Harnessing Stone" (52946) from "Miriku the Chaotic" in `kael`.
14. lfaydark/"A Brownie Noble", hand "Harnessing Stone" (52946). Requires `ench_epic` ==8. Gives "Purifying Crystal Fragment" (52957).
15. Say "Spawn Devastating Pookas" to tipt/"Rikabi The Riddler".
16. Spawns "A Devastating Pooka" (289037).
17. Loot "Mountain Pooka Meat" (54240) from "A Devastating Pooka".
18. Hand "Mountain Pooka Meat" (54240) to jaggedpine/"Chef Brargus". Spawns "Firwyn" (181226). Loot "Dryad Necklace" (57917) from "Firwyn".
19. gfaydark/"Feyana Lightwing", hand "Dryad Necklace" (57917). Gives "Purifying Crystal Fragment" (52958).
20. Combine in "Planar Jeweler's Kit" (17764): "Purifying Crystal Fragment" (52955), "Purifying Crystal Fragment" (52956), "Purifying Crystal Fragment" (52957), "Purifying Crystal Fragment" (52958). Produces "Purifying Crystal" (52954). Requires Jewelry Making. The combine does not fail.

### "Channeling Crystal" (57920)

1. Loot "Tattered Incantation" (57919) from "Cipheron" in `wallofslaughter`.
2. Loot "Noxious Secretion" (52951) from "Withering Murkglider" in `causeway`.
3. nedaria/"Priestess Rakhu", hand "Noxious Secretion" (52951) + "Tattered Incantation" (57919). Requires `ench_epic` ==9. Gives "Channeling Crystal" (57920).

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
  - No quest step gives Gnomish Candy (52944). The dump lists it in akanon.
- Koada`Dal Silk (52948)
  - No quest step gives Koada`Dal Silk (52948). The dump lists it in felwithea, felwitheb.
- Feir`Dal Champagne (52940)
  - No quest step gives Feir`Dal Champagne (52940). The dump lists it in gfaydark, katta, rivervale.
- Dwarven Steel (57921)
  - No quest step gives Dwarven Steel (57921). The dump lists it in kaladima.

### 9. global player — combine recipe 19919

Zone: `global`.

Sets `ench_epic` to `9`.

In script order:

1. Sets `ench_epic` to `9`.


Combine:

- `recipe:19919` is combined in Planar Jeweler's Kit (17764).
  - No quest step gives Planar Jeweler's Kit (17764). The dump lists it in abysmal, poknowledge.
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
    - 4 alternative loot source(s) also yield Globe of Discordant Energy (47100).
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
