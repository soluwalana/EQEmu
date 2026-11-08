# Druid

Steps taken from the quest graph only. **Broken** means the graph has no edge for that value or that item.

Flags with writes: `druid_epic`.

## 0. Prerequisites

Shared acquisition steps appear in the first prerequisite chain that needs them. Later sections reference that chain rather than repeating it.

### "Runed Skull" (62838)

1. Forage "Sickly Maiden's Hair" (62810) in `rathemtn`.
2. eastkarana/"Althele", hand "Sickly Maiden's Hair" (62810). Gives "Tuft of Sickly Maiden's Hair" (62811).
3. qrg/"Niera Farbreeze", hand "Tuft of Sickly Maiden's Hair" (62811). Gives "Waterproof Collection Bag" (62812).
4. Say "King Timer" to frontiermtns/"Druid 1 5".
5. Spawns npc 92202 (92202).
6. Loot "Bag of Diseased Maiden's Hair" (62826) from npc 92202.
7. eastkarana/"Althele", say "Out Of Balance". Sets `druid_epic` to `1`.
8. Spawns "A Bloodgill Forager" (85234) in `lakeofillomen` on enter.
9. Loot "Handful of Diseased Maiden's Hair" (62825) from "A Bloodgill Forager".
10. Common item: Tackle Box (17048). Listed in 11 zones.
11. Spawns "Ulthork Raider" (116608) in `eastwastes` on enter.
12. Loot "Carved Prexus Totem" (62821) from "Ulthork Raider".
13. cobaltscar/"Blumblum Swigwater", hand "Carved Prexus Totem" (62821). Gives "Small Trigger Fish" (62820).
14. Common item: Gutting Knife (62823). Listed in 4 zones.
15. Combine in "Tackle Box" (17048): "Small Trigger Fish" (62820), "Gutting Knife" (62823). Hands back "Gutting Knife" (62823). Produces "Soggy Maiden's Hair" (62824). Requires Fishing, trivial 20. The combine does not fail.
16. Spawns "spawn #Swamp Terror" (47208) in `feerrott` on enter.
17. Loot "Partially Digested Maiden's Hair" (62819) from "spawn #Swamp Terror".
18. Combine in "Waterproof Collection Bag" (62812): "Bag of Diseased Maiden's Hair" (62826), "Handful of Diseased Maiden's Hair" (62825), "Soggy Maiden's Hair" (62824), "Partially Digested Maiden's Hair" (62819). Produces "Sealed Collection Bag" (62813). The combine does not fail.
19. qrg/"Niera Farbreeze", hand "Sealed Collection Bag" (62813). Gives "Wash Cloth" (62847).
20. Spawns "spawn #Swamp Terror" (47208) in `feerrott` on enter.
21. Loot "Mangled Head" (62818) from "spawn #Swamp Terror".
22. Combine in "Wash Cloth" (62847): "Mangled Head" (62818). Produces "Wrapped Mangled Head" (62848). The combine does not fail.
23. qrg/"Niera Farbreeze", hand "Wrapped Mangled Head" (62848). Gives "Mangled Head" (62827).
24. qrg/"Niera Farbreeze", hand "Wrapped Mangled Head" (62848). Sets `druid_epic` to `2`.
25. poknowledge/"Pathfinder Arelat", say "Worth It". Requires `druid_epic` ==2. Gives "Fresh Awakenings vol. 1" (62839).
26. poknowledge/"Pathfinder Arelat", say "Worth It". Requires `druid_epic` ==2. Gives "Fresh Awakenings vol. 2" (62840).
27. poknowledge/"Pathfinder Arelat", say "Worth It". Requires `druid_epic` ==2. Gives "Fresh Awakenings vol. 3" (62841).
28. poknowledge/"Gravelady Beddia", hand "Fresh Awakenings vol. 1" (62839) + "Fresh Awakenings vol. 2" (62840) + "Fresh Awakenings vol. 3" (62841). Gives "Healing Plants" (62842).
29. qrg/"Niera Farbreeze", hand "Healing Plants" (62842). Sets `druid_epic` to `3`.
30. feerrott/"Corrupted Spirit", say "Show It". Requires `druid_epic` ==3. Gives "Disease Rune" (62837).
31. tox/"A Skeleton", say "I Will Do It". Triggers `tox/a skeleton#timer:pathback`.
32. Starts timer `pathbacktwo`.
33. Starts timer `pathbackthree`.
34. Starts timer `giveitem`.
35. tox/"A Skeleton", on timer giveitem. Gives "Animating Heads" (62828).
36. Combine in "Mangled Head" (62827): "Disease Rune" (62837), "Animating Heads" (62828). Produces "Runed Skull" (62838). The combine does not fail.

### "Healing Plants" (62842)

1. Acquisition of "Healing Plants" (62842) is documented under "Runed Skull" (62838); obtain another copy if needed.

### "Mind Crystal" (62846)

1. Acquisition of "Runed Skull" (62838) is documented under "Runed Skull" (62838); obtain another copy if needed.
2. Acquisition of "Healing Plants" (62842) is documented under "Runed Skull" (62838); obtain another copy if needed.
3. qrg/"Niera Farbreeze", hand "Healing Plants" (62842). Gives "Niera's Healing Notes" (62849).
4. qrg/"Niera Farbreeze", hand "Runed Skull" (62838) + "Niera's Healing Notes" (62849). Sets `druid_epic` to `4`.
5. qrg/"Niera Farbreeze", hand "Runed Skull" (62838) + "Niera's Healing Notes" (62849). Gives "Niera's Research Notes" (62843).
6. pojustice/"Great Bear", hand "Niera's Research Notes" (62843). Requires `druid_epic` ==4. Gives "Red Dogwood Seed" (62844).
7. pojustice/"Great Bear", hand "Niera's Research Notes" (62843). Requires `druid_epic` ==4. Gives "Living Brambles Seed" (62845).
8. qrg/"Niera Farbreeze", hand "Red Dogwood Seed" (62844) + "Living Brambles Seed" (62845). Requires `druid_epic` ==4. Gives "Mind Crystal" (62846).

### "Wrapped Mangled Head" (62848)

1. Acquisition of "Wrapped Mangled Head" (62848) is documented under "Runed Skull" (62838); obtain another copy if needed.

### "Niera's Healing Notes" (62849)

1. Acquisition of "Niera's Healing Notes" (62849) is documented under "Mind Crystal" (62846); obtain another copy if needed.

### "Living Brambles Seed" (62850)

1. Acquisition of "Red Dogwood Seed" (62844) is documented under "Mind Crystal" (62846); obtain another copy if needed.
2. Acquisition of "Living Brambles Seed" (62845) is documented under "Mind Crystal" (62846); obtain another copy if needed.
3. qrg/"Niera Farbreeze", hand "Red Dogwood Seed" (62844) + "Living Brambles Seed" (62845). Requires `druid_epic` ==4. Gives "Living Brambles Seed" (62850).

### "Clear Mind Crystal" (62857)

1. Loot "Crystal Fragment" (62852) from "Finnelzi Springworthy" in `southkarana`.
2. Loot "Crystal Fragment" (62852) from "Rendolf Deathbringer" in `southkarana`.
3. Loot "Crystal Fragment" (62852) from "Tehana Elsent" in `southkarana`.
4. freportw/"Shana Liskia", hand "Crystal Fragment" (62852) + "Crystal Fragment" (62852) + "Crystal Fragment" (62852). Gives "Small Padded Bag" (62853).
5. freportw/"Shana Liskia", hand "Crystal Fragment" (62852) + "Crystal Fragment" (62852) + "Crystal Fragment" (62852). Sets `druid_epic` to `5`.
6. Spawns "Azibelle Spavin" (335064) in `harbingers` on enter.
7. Loot "Bohab's Crystal Fragment" (62886) from "Azibelle Spavin".
8. Spawns "Azibelle Spavin" (335064) in `harbingers` on enter.
9. Loot "Azibelle's Crystal Fragment" (62887) from "Azibelle Spavin".
10. Spawns "Glenfire Telzir" (335065) in `harbingers` on enter.
11. Loot "Glenfire's Crystal Fragment" (62888) from "Glenfire Telzir".
12. Combine in "Small Padded Bag" (62853): "Bohab's Crystal Fragment" (62886), "Azibelle's Crystal Fragment" (62887), "Glenfire's Crystal Fragment" (62888), "Crystal Fragment" (62852). Produces "Full Padded Bag" (62854). The combine does not fail.
13. freportw/"Shana Liskia", hand "Full Padded Bag" (62854). Gives "Bowl of Foul-smelling Liquid" (62855).
14. Spawns "Noc Juggernaut" (280091) in `natimbi` on event spawn:280090.
15. Loot "Energized Noc Blood" (62889) from "Noc Juggernaut".
16. Alternative: Loot "Energized Noc Blood" (62889) from "Noc Juggernaut" (NPC 280091) in `natimbi`; trigger: natimbi/"Druid 1 5", on event death_complete:280069.
17. Forage "Emerald Moss" (62856) in `emeraldjungle`.
18. Acquisition of "Mind Crystal" (62846) is documented under "Mind Crystal" (62846); obtain another copy if needed.
19. Combine in "Bowl of Foul-smelling Liquid" (62855): "Energized Noc Blood" (62889), "Emerald Moss" (62856), "Mind Crystal" (62846). Produces "Clear Mind Crystal" (62857). The combine does not fail.

### "Reinforced Aerated Pot" (62861)

1. Acquisition of "Clear Mind Crystal" (62857) is documented under "Clear Mind Crystal" (62857); obtain another copy if needed.
2. abysmal/"Silanda Leafdew", hand "Clear Mind Crystal" (62857). Sets `druid_epic` to `7`.
3. Spawns "A Cracked Earthshaker" (336214) in `dranik` on enter.
4. Loot "Chunk of Energized Clay" (62859) from "A Cracked Earthshaker".
5. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
6. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `steamfont`.
7. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `tox`.
8. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `toxxulia`.
9. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
10. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). The combine does not fail.
11. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
12. Combine in Pottery Wheel (21): "Water Flask" (13006), "Block of Clay" (16901). Produces "Small Block of Clay" (16900) x3. Requires Pottery, trivial 21.
13. Combine in Pottery Wheel (21): "Small Block of Clay" (16900), "Water Flask" (13006). Produces "Block of Clay" (16901). Requires Pottery, trivial 21.
14. Common item: Aerated Pot Sketch (62858). Listed in 4 zones.
15. Combine in Pottery Wheel (21): "Water Flask" (13006), "Block of Clay" (16901), "Aerated Pot Sketch" (62858). Produces "Aerated Pot Shell" (62860). Requires Pottery, trivial 68.
16. Combine in Kiln (22): "Chunk of Energized Clay" (62859), "Aerated Pot Shell" (62860). Produces "Reinforced Aerated Pot" (62861). Requires Pottery, trivial 100. The combine does not fail.

### "Staff of Living Brambles" (62863)

1. Acquisition of "Reinforced Aerated Pot" (62861) is documented under "Reinforced Aerated Pot" (62861); obtain another copy if needed.
2. Acquisition of "Living Brambles Seed" (62850) is documented under "Living Brambles Seed" (62850); obtain another copy if needed.
3. Acquisition of "Clear Mind Crystal" (62857) is documented under "Clear Mind Crystal" (62857); obtain another copy if needed.
4. Kill kithicor/"Blackened Tree Limb". Spawns "Blackened Dryad" (20301).
5. Loot "Blackened Earth" (62862) from "Blackened Dryad".
6. Combine in "Reinforced Aerated Pot" (62861): "Living Brambles Seed" (62850), "Clear Mind Crystal" (62857), "Blackened Earth" (62862). Produces "Staff of Living Brambles" (62863). The combine does not fail.

### "Rune of Yuisaha" (62868)

1. Acquisition of "Staff of Living Brambles" (62863) is documented under "Staff of Living Brambles" (62863); obtain another copy if needed.
2. abysmal/"Reyfin Malakwa", say "Hail". Gives "Ragged Cloth Bag" (62881).
3. qinimi/"A Broken Ritesdancer", say "What About The Rune Fragments?". Gives "Threadbare Cloth Bag" (62890).
4. qinimi/"A Broken Ritesdancer", say "What About The Rune Fragments?". Gives "Undamaged Noc Fang" (62864).
5. Combine in "Threadbare Cloth Bag" (62890): "Undamaged Noc Fang" (62864). Produces "Closed Cloth Bag" (62891). The combine does not fail.
6. qinimi/"A Broken Ritesdancer", hand "Closed Cloth Bag" (62891). Gives "Rune Fragment" (62867).
7. Forage "Rune Fragment" (62866) in `barindu`.
8. Forage "Rune Fragment" (62866) in `ferubi`.
9. Forage "Rune Fragment" (62866) in `riwwi`.
10. Forage "Rune Fragment" (62865) in `barindu`.
11. Forage "Rune Fragment" (62865) in `ferubi`.
12. Forage "Rune Fragment" (62865) in `riwwi`.
13. Combine in "Ragged Cloth Bag" (62881): "Rune Fragment" (62867), "Rune Fragment" (62866), "Rune Fragment" (62865). Produces "Wrapped Cloth Bag" (62882). The combine does not fail.
14. abysmal/"Reyfin Malakwa", hand "Wrapped Cloth Bag" (62882). Gives "Rune of Yuisaha" (62868).

### "Insulated Container" (62876)

1. Acquisition of "Wrapped Cloth Bag" (62882) is documented under "Rune of Yuisaha" (62868); obtain another copy if needed.
2. abysmal/"Reyfin Malakwa", hand "Wrapped Cloth Bag" (62882). Sets `druid_epic` to `10`.
3. nedaria/"Historian Finrazel", say "Plan To Find". Requires `druid_epic` ==10. Gives "Thick Leather Bag" (62884).
4. Kill wallofslaughter/"A Nervous Guardian". Spawns "Lightning Lord" (300098).
5. Loot "Rain Shard" (62872) from "Lightning Lord".
6. Loot "Frost Shard" (62871) from "Bazu Scavenger" in `causeway`.
7. Spawns "Mastruq Commander Gorlakt" (281089) in `qinimi` on enter.
8. Loot "Spirit Shard" (62870) from "Mastruq Commander Gorlakt".
9. Spawns "Tranlinor the Maimed" (302086) in `draniksscar` on enter.
10. Loot "Wind Shard" (62873) from "Tranlinor the Maimed".
11. Combine in "Thick Leather Bag" (62884): "Rain Shard" (62872), "Frost Shard" (62871), "Spirit Shard" (62870), "Wind Shard" (62873). Produces "Synched Leather Bag" (62885). The combine does not fail.
12. abysmal/"Reyfin Malakwa", hand "Synched Leather Bag" (62885). Sets `druid_epic` to `12`.
13. abysmal/"Silanda Leafdew", hand "Synched Leather Bag" (62885). Requires `druid_epic` set. Requires `druid_epic` ==12. Gives "Insulated Container Sketch" (62875).
14. Loot "Faded-Glyph Tablet" (60224) from "Pixtt Condemner" in `ikkinz`.
15. Loot "Runed Glyph: Aktek" (60221) from "Visionary of Glory" in `ikkinz`.
16. Loot "Runed Glyph: Fexika" (60222) from "Visionary of Glory" in `ikkinz`.
17. Loot "Runed Glyph: Niliktek" (60223) from "Visionary of Glory" in `ikkinz`.
18. Combine in "Faded-Glyph Tablet" (60224): "Runed Glyph: Aktek" (60221), "Runed Glyph: Fexika" (60222), "Runed Glyph: Niliktek" (60223). Produces "Axtekilitek" (60225). Requires Research, trivial 100. The combine does not fail.
19. Loot "Runed Glyph: Kruxek" (60226) from "Sentinel of Glorification" in `ikkinz`.
20. Combine in "Faded-Glyph Tablet" (60224): "Axtekilitek" (60225), "Runed Glyph: Kruxek" (60226). Produces "Kruxilitek" (60227). Requires Research, trivial 100. The combine does not fail.
21. Hand "Kruxilitek" (60227) to ikkinz/"Guardian Of Glorification". Spawns "Guardian of Glorification" (294582). Loot "Chunk of Broken Ancient Stone Worker" (58026) from "Guardian of Glorification".
22. Alternative: Loot "Chunk of Broken Ancient Stone Worker" (58026) from "Guardian of Glorification" (NPC 294583) in `ikkinz`; trigger: ikkinz/"Guardian Of Glorification", on event_hp.
23. Alternative: Loot "Chunk of Broken Ancient Stone Worker" (58026) from "A Clay Monolith" (NPC 296002) in `inktuta`; trigger: inktuta/"Zone Status", say "Spawn Golems".
24. Alternative: Loot "Chunk of Broken Ancient Stone Worker" (58026) from "A Clay Monolith" (NPC 296049) in `inktuta`; trigger: inktuta/"Zone Status", say "Spawn Golems".
25. Alternative: Loot "Chunk of Broken Ancient Stone Worker" (58026) from "A Clay Monolith" (NPC 296050) in `inktuta`; trigger: inktuta/"Zone Status", say "Spawn Golems".
26. Alternative: Loot "Chunk of Broken Ancient Stone Worker" (58026) from "A Clay Monolith" (NPC 296051) in `inktuta`; trigger: inktuta/"Zone Status", say "Spawn Golems".
27. Alternative: Loot "Chunk of Broken Ancient Stone Worker" (58026) from "A Freed Rockbearer" (NPC 291131) in `yxtta`; trigger: yxtta/"Player", say "Stone Attack".
28. abysmal/"Hiloan O-Yviania", hand "Chunk of Broken Ancient Stone Worker" (58026). Gives "Clump of Refined Ancient Taelosian Clay" (58031).
29. Combine in Kiln (22): "Insulated Container Sketch" (62875), "Clump of Refined Ancient Taelosian Clay" (58031). Produces "Insulated Container" (62876). Requires Pottery 100. The combine does not fail.

### "Wrapped Cloth Bag" (62882)

1. Acquisition of "Wrapped Cloth Bag" (62882) is documented under "Rune of Yuisaha" (62868); obtain another copy if needed.

### "Synched Leather Bag" (62885)

1. Acquisition of "Synched Leather Bag" (62885) is documented under "Insulated Container" (62876); obtain another copy if needed.

## `druid_epic`

Values written: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13.

### 1. althele — say out of balance

Zone: `eastkarana`.

> I don

Sets `druid_epic` to `1`.

- Needs `druid_epic` unset.
In script order:

1. Sets `druid_epic` to `1`.


### 2. niera farbreeze — hand 62848

Zone: `qrg`.

Sets `druid_epic` to `2`.

- Turn in x1: Wrapped Mangled Head (62848).
In script order:

1. Sets `druid_epic` to `2`.
2. Gives Mangled Head (62827).


How the items are reached:

- Wrapped Mangled Head (62848)
  - Prerequisite: "Wrapped Mangled Head" (62848). See section 0.

### 3. niera farbreeze — hand 62842

Zone: `qrg`.

Sets `druid_epic` to `3`.

- Turn in x1: Healing Plants (62842).
In script order:

1. Sets `druid_epic` to `3`.
2. Gives Niera's Healing Notes (62849).


How the items are reached:

- Healing Plants (62842)
  - Prerequisite: "Healing Plants" (62842). See section 0.

### 4. niera farbreeze — hand 62838+62849

Zone: `qrg`.

Sets `druid_epic` to `4`.

- Turn in x1: Runed Skull (62838).
- Turn in x1: Niera's Healing Notes (62849).
In script order:

1. Sets `druid_epic` to `4`.
2. Gives Niera's Research Notes (62843).


How the items are reached:

- Runed Skull (62838)
  - Prerequisite: "Runed Skull" (62838). See section 0.
- Niera's Healing Notes (62849)
  - Prerequisite: "Niera's Healing Notes" (62849). See section 0.

### 5. shana liskia — hand 62852+62852+62852

Zone: `freportw`.

Sets `druid_epic` to `5`.

- Turn in x1: Crystal Fragment (62852).
In script order:

1. Sets `druid_epic` to `5`.
2. Gives Crystal Fragment (62852).
3. Gives Small Padded Bag (62853).


How the items are reached:

- Crystal Fragment (62852)
  - Loot "Crystal Fragment" (62852) from "Finnelzi Springworthy" in `southkarana`.
  - Loot "Crystal Fragment" (62852) from "Rendolf Deathbringer" in `southkarana`.
  - Loot "Crystal Fragment" (62852) from "Tehana Elsent" in `southkarana`.

### 6. silanda leafdew — hand 62846

Zone: `abysmal`.

Sets `druid_epic` to `6`.

- Turn in x1: Mind Crystal (62846).
In script order:

1. Sets `druid_epic` to `6`.
2. Gives Mind Crystal (62846).


How the items are reached:

- Mind Crystal (62846)
  - Prerequisite: "Mind Crystal" (62846). See section 0.

### 7. silanda leafdew — hand 62857

Zone: `abysmal`.

Sets `druid_epic` to `7`.

- Turn in x1: Clear Mind Crystal (62857).
In script order:

1. Sets `druid_epic` to `7`.
2. Gives Clear Mind Crystal (62857).


How the items are reached:

- Clear Mind Crystal (62857)
  - Prerequisite: "Clear Mind Crystal" (62857). See section 0.

### 8. global player — combine recipe 19892

Zone: `global`.

Sets `druid_epic` to `8`.

In script order:

1. Sets `druid_epic` to `8`.


Combine:

- `recipe:19892` is combined in Reinforced Aerated Pot (62861).
  - Prerequisite: "Reinforced Aerated Pot" (62861). See section 0.
  - Put in x1: Living Brambles Seed (62850).
    - Prerequisite: "Living Brambles Seed" (62850). See section 0.
  - Put in x1: Clear Mind Crystal (62857).
    - Prerequisite: "Clear Mind Crystal" (62857). See section 0.
  - Put in x1: Blackened Earth (62862).
    - Kill kithicor/"Blackened Tree Limb". Spawns "Blackened Dryad" (20301).
    - Loot "Blackened Earth" (62862) from "Blackened Dryad".
  - Produces Staff of Living Brambles (62863).
  - The combine does not fail.

### 9. reyfin malakwa — say hail

Zone: `abysmal`.

> stares silently out over the ocean towards the magical wards protecting the ship from the unyielding onslaught of the pounding waves. He jumps back terrorize...

Sets `druid_epic` to `9`.

- Needs `druid_epic` <9.
In script order:

1. Sets `druid_epic` to `9`.


### 10. reyfin malakwa — hand 62882

Zone: `abysmal`.

Sets `druid_epic` to `10`.

- Turn in x1: Wrapped Cloth Bag (62882).
In script order:

1. Sets `druid_epic` to `10`.
2. Gives Rune of Yuisaha (62868).


How the items are reached:

- Wrapped Cloth Bag (62882)
  - Prerequisite: "Wrapped Cloth Bag" (62882). See section 0.

Alternative or repeat transition to `druid_epic` = `10` (not an additional required stage).

### 10. historian finrazel — hand 62868

Zone: `nedaria`.

Sets `druid_epic` to `10`.

- Turn in x1: Rune of Yuisaha (62868).
In script order:

1. Sets `druid_epic` to `10`.


How the items are reached:

- Rune of Yuisaha (62868)
  - Prerequisite: "Rune of Yuisaha" (62868). See section 0.

### 11. historian finrazel — hand 62885

Zone: `nedaria`.

Sets `druid_epic` to `11`.

- Turn in x1: Synched Leather Bag (62885).
In script order:

1. Sets `druid_epic` to `11`.
2. Gives Synched Leather Bag (62885).


How the items are reached:

- Synched Leather Bag (62885)
  - Prerequisite: "Synched Leather Bag" (62885). See section 0.

### 12. reyfin malakwa — hand 62885

Zone: `abysmal`.

Sets `druid_epic` to `12`.

- Turn in x1: Synched Leather Bag (62885).
In script order:

1. Sets `druid_epic` to `12`.
2. Gives Synched Leather Bag (62885).


How the items are reached:

- Synched Leather Bag (62885)
  - Prerequisite: "Synched Leather Bag" (62885). See section 0.

### 13. global player — combine recipe 19909

Zone: `global`.

Sets `druid_epic` to `13`.

In script order:

1. Sets `druid_epic` to `13`.


Combine:

- `recipe:19909` is combined in Insulated Container (62876).
  - Prerequisite: "Insulated Container" (62876). See section 0.
  - Put in x1: Essence of Rainfall (62883).
    - Given by global/"Global Player", combine recipe 19908.
  - Put in x1: Staff of Living Brambles (62863).
    - Prerequisite: "Staff of Living Brambles" (62863). See section 0.
  - Produces Staff of Everliving Brambles (62880).
  - The combine does not fail.

### Steps on `druid_epic` that do not change it

- `abysmal` silanda leafdew, hand 62885 needs `druid_epic` set.
  - Turn in Synched Leather Bag (62885).
  - Gives Synched Leather Bag (62885).
  - Gives Insulated Container Sketch (62875).
- `burningwood` player, on enter needs `druid_epic` ==12.
  - Spawns a crippled wurm (87155).
  - Loots Polished Gear #1 (37029).
  - Loots Polished Gear #3 (37032).
  - Loots Uncut Combine Star (37845).
  - Loots Everburning Jagged Tree Limb (62879).
  - Loots Spotted Lava Rock (80010).
- `dranik` earthshaker trap, on enter needs `druid_epic` ==7.
  - Sets `druid_epic_dranik` to `1`.
  - Spawns a cracked earthshaker (336214).
  - Loots Chunk of Energized Clay (62859).
- `dranik` player, on loot needs `druid_epic` ==7.
  - Sets `druid_chest_dranik` to `1`.
  - Spawns a chest (Epic 1.5) (283157).
- `draniksscar` druid trap, on enter needs `druid_epic` ==10.
  - Spawns Tranlinor the Maimed (302086).
  - Loots Lucidem (35084).
  - Loots Versluierd Fungus (35087).
  - Loots Uncut Alexandrite (37847).
  - Loots Kyv Arrowhead (51921).
  - Loots Wind Shard (62873).
- `eastwastes` player, on enter needs `druid_epic` ==1.
  - Sets `druid_epic_ew` to `1`.
  - Spawns Ulthork Raider (116608).
  - Spawns an ulthork man o war (116066).
  - Loots Ulthork Tusks (24874).
  - Loots Ulthork Hide (30092).
  - Loots Ulthork Meat (30093).
  - Loots Ulthork Hide Legs (30123).
  - Loots Velium Long Sword (30200).
  - Loots Velium Dagger (30207).
  - Loots Velium Rapier (30209).
  - Loots Carved Prexus Totem (62821).
  - Loots Salil's Writ Pg. 174 (11714).
  - Loots Salil's Writ Pg. 282 (11716).
  - Loots Salil's Writ Pg. 288 (11719).
  - Loots Faded Salil's Writ Page (11721).
  - Loots Nilitim's Grimoire Pg. 35 (11722).
  - Loots Nilitim's Grimoire Pg. 36 (11723).
  - Loots Nilitim's Grimoire Pg. 115 (11724).
  - Loots Nilitim's Grimoire Pg. 116 (11725).
  - Loots Nilitim's Grimoire Pg. 300 (11726).
  - Loots Nilitim's Grimoire Pg. 301 (11727).
  - Loots Nilitim's Grimoire Pg. 351 (11728).
  - Loots Nilitim's Grimoire Pg. 352 (11729).
  - Loots Rune of Al'Kabor (11746).
  - Loots Rune of the Combine (11754).
  - Loots Rune of the Helix (11758).
  - Loots Rune of Petrification (11770).
  - Loots Rune of Paralysis (11772).
  - Loots Rune of Conception (11774).
  - Loots Rune of Infraction (11775).
  - Loots Rune of Rathe (11776).
  - Loots Rune of Attraction (11777).
  - Loots Rune of the Inverse (11778).
  - Loots Glove of Rallos Zek (11796).
  - Loots Flame of Vox (11797).
  - Loots The Scent of Marr (11802).
  - Loots Words of Collection (Azia) (11803).
  - Loots Words of Incarceration (11804).
  - Loots Essence of Rathe (11805).
  - Loots Tears of Prexus (11806).
  - Loots Words of the Suffering (11851).
  - Loots Words of Descrying (11852).
  - Loots Words of Seizure (11853).
  - Loots Words of Disillusionment (11854).
  - Loots Words of Projection (11855).
  - Loots Words of the Spectre (11856).
  - Loots Words of Bidding (11857).
  - Loots Words of Collection (Beza) (11858).
  - Loots Words of the Psyche (11861).
  - Loots Words of Burnishing (11862).
  - Loots Words of Obligation (11863).
  - Loots Words of Collection (Caza) (11864).
  - Loots Words of Convocation (11872).
  - Loots Words of Cazic-Thule (16039).
  - Loots Ulthork Tusks (24874).
  - Loots Ulthork Hide (30092).
  - Loots Ulthork Meat (30093).
  - Loots Walrus Tooth (30107).
  - Loots Ulthork Hide Legs (30123).
  - Loots Ulthork Hide Tunic (30126).
  - Loots Ulthork Hide Collar (30129).
  - Loots Velium Long Sword (30200).
  - Loots Velium Two Handed Sword (30201).
  - Loots Velium Short Sword (30202).
  - Loots Velium Scimitar (30203).
  - Loots Velium Warhammer (30204).
  - Loots Velium Morning Star (30205).
  - Loots Velium Great Staff (30206).
  - Loots Velium Dagger (30207).
  - Loots Velium Spear (30208).
  - Loots Velium Rapier (30209).
  - Loots Spell: Tumultuous Strength (30428).
  - Loots Spell: Ro's Fiery Sundering (30437).
  - Loots Spell: Turning of the Unnatural (30443).
  - Loots Sunshard Ore (33792).
  - Loots Pliant Loam (34878).
  - Loots Malleable Loam (34879).
  - Loots Supple Loam (34880).
  - Loots Bonded Loam (34882).
  - Loots Dry Marrow (34892).
  - Loots Damp Marrow (34893).
  - Loots Moist Marrow (34894).
  - Loots Hemic Marrow (34896).
  - Loots Thick Spinneret Fluid (34905).
  - Loots Crude Spinneret Fluid (34906).
  - Loots Natural Spinneret Fluid (34907).
  - Loots Simple Etched Rune (38667).
  - Loots Complex Platinum Silvered Rune (38691).
  - Loots Consigned Bite of the Shissar VI (44551).
  - Loots Raw Crimson Nihilite (58067).
- `feerrott` corrupted spirit, say show it needs `druid_epic` ==3.
  - Gives Disease Rune (62837).
- `harbingers` druid epic trap, on enter needs `druid_epic` ==5.
  - Sets `druid_epic_harb` to `1`.
  - Spawns Azibelle Spavin (335064).
  - Spawns Glenfire Telzir (335065).
  - Loots Sunshard Powder (35088).
  - Loots Bohab's Crystal Fragment (62886).
  - Loots Azibelle's Crystal Fragment (62887).
  - Loots Curzon (35085).
  - Loots Glenfire's Crystal Fragment (62888).
- `kithicor` player, on enter needs `druid_epic` ==7.
  - Spawns Blackened Treant (20299).
- `kithicor` player, on loot needs `druid_epic` ==7.
  - Sets `druid_chest_kith` to `1`.
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
- `lakeofillomen` player, on enter needs `druid_epic` ==1.
  - Sets `druid_epic_loio` to `1`.
  - Spawns a bloodgill forager (85234).
  - Spawns a bloodgill forager (85235).
  - Loots Opal (10030).
  - Loots Golden Pendant (10044).
  - Loots Crystallized Sulfur (16976).
  - Loots Bonded Loam (34882).
  - Loots Raw Crimson Nihilite (58067).
  - Loots Handful of Diseased Maiden's Hair (62825).
  - Loots Pearl Earring (10002).
  - Loots Pearl Ring (10003).
  - Loots Black Pearl (10012).
  - Loots Peridot (10028).
  - Loots Emerald (10029).
  - Loots Opal (10030).
  - Loots Jade Ring (10043).
  - Loots Golden Pendant (10044).
  - Loots Faded Salil's Writ Page (11712).
  - Loots Salil's Writ Pg. 153 (11713).
  - Loots Salil's Writ Pg. 174 (11714).
  - Loots Salil's Writ Pg. 174 (11715).
  - Loots Salil's Writ Pg. 282 (11716).
  - Loots Salil's Writ Pg. 288 (11719).
  - Loots Faded Salil's Writ Page (11720).
  - Loots Rune of Al'Kabor (11746).
  - Loots Rune of the Combine (11754).
  - Loots Rune of the Helix (11758).
  - Loots Rune of Petrification (11770).
  - Loots Rune of Tyranny (11771).
  - Loots Rune of Paralysis (11772).
  - Loots Rune of Embrace (11773).
  - Loots Rune of Conception (11774).
  - Loots Rune of Infraction (11775).
  - Loots Glove of Rallos Zek (11796).
  - Loots Flame of Vox (11797).
  - Loots Words of Collection (Azia) (11803).
  - Loots Words of the Suffering (11851).
  - Loots Words of Descrying (11852).
  - Loots Words of Seizure (11853).
  - Loots Words of Disillusionment (11854).
  - Loots Words of Projection (11855).
  - Loots Words of the Spectre (11856).
  - Loots Words of Bidding (11857).
  - Loots Words of Collection (Beza) (11858).
  - Loots Words of Convocation (11872).
  - Loots Harpoon of the Depths (11970).
  - Loots Ancient Coin (12936).
  - Loots Bloodgill Scales (14824).
  - Loots Words of Cazic-Thule (16039).
  - Loots Crystallized Sulfur (16976).
  - Loots Flawless Aquamarine (22505).
  - Loots Sunshard Dust (33790).
  - Loots Pliant Loam (34878).
  - Loots Malleable Loam (34879).
  - Loots Supple Loam (34880).
  - Loots Dry Marrow (34892).
  - Loots Damp Marrow (34893).
  - Loots Moist Marrow (34894).
  - Loots Thick Spinneret Fluid (34905).
  - Loots Crude Spinneret Fluid (34906).
  - Loots Natural Spinneret Fluid (34907).
  - Loots Simple Etched Rune (38667).
  - Loots Complex Platinum Silvered Rune (38691).
  - Loots Consigned Bite of the Shissar V (44550).
  - Loots Consigned Bite of the Shissar VI (44551).
  - Loots Petrified Bloodgill Eye (80378).
  - Loots Collector's Bloodgill Scale (84011).
- `natimbi` player, on loot needs `druid_epic` >5.
  - Sets `druid_chest_natimbi` to `1`.
  - Spawns a chest (283157).
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
- `nedaria` historian finrazel, say plan to find needs `druid_epic` ==10.
  - Gives Thick Leather Bag (62884).
- `northro` a madman, say still desire it needs `druid_epic` ==3.
  - Gives Soul Stone (62836).
- `northro` a madman, say will do needs `druid_epic` ==3.
  - Spawns a haunt (392104).
- `nro` a madman, say still desire it needs `druid_epic` ==3.
  - Gives Soul Stone (62836).
- `nro` a madman, say will do needs `druid_epic` ==3.
  - Spawns a haunt (392104).
- `pojustice` great bear, hand 62843 needs `druid_epic` ==4.
  - Turn in Niera's Research Notes (62843).
  - Gives Red Dogwood Seed (62844).
  - Gives Living Brambles Seed (62845).
- `poknowledge` pathfinder arelat, say worth it needs `druid_epic` ==2.
  - Gives Fresh Awakenings vol. 1 (62839).
  - Gives Fresh Awakenings vol. 2 (62840).
  - Gives Fresh Awakenings vol. 3 (62841).
- `qinimi` druid trap, on enter needs `druid_epic` ==10.
  - Sets `druid_qin` to `1`.
  - Spawns Mastruq Commander Gorlakt (281089).
  - Spawns Spiritlord Body (281091).
  - Spawns Spiritlord Mind (281090).
  - Loots Spirit Shard (62870).
  - Loots Spirit Summoner's Bag (67441).
  - Loots Mastruq Tongue (67587).
  - Loots Sunshard Powder (35088).
  - Loots Mastruq's Clawed Finger (67434).
  - Loots Ukun Summoning Idol (67443).
  - Loots Mastruq Tongue (67587).
- `qinimi` player, on loot needs `druid_epic` ==10.
  - Sets `druid_epic_qin` to `1`.
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
- `qrg` niera farbreeze, hand 62844+62845 needs `druid_epic` ==4.
  - Turn in Red Dogwood Seed (62844).
  - Turn in Living Brambles Seed (62845).
  - Gives Living Brambles Seed (62850).
  - Gives Mind Crystal (62846).
- `wallofslaughter` druid trap, on enter needs `druid_epic` ==10.
  - Sets `druid_wos` to `1`.
  - Spawns Retired Soldier (300096).
  - Spawns a nervous guardian (300097).
- `wallofslaughter` player, on loot needs `druid_epic` ==10.
  - Sets `druid_epic_wos` to `1`.
  - Spawns a chest (Epic 1.5) (893).

## Other flags touched along the way

- `druid_epic_dranik` set to 1 at dranik/earthshaker trap.
- `druid_epic_ew` set to 1 at eastwastes/player.
- `druid_epic_harb` set to 1 at harbingers/druid epic trap.
- `druid_epic_loio` set to 1 at lakeofillomen/player.
- `druid_epic_natimbi` set to 1 at natimbi/player.
- `druid_epic_qin` set to 1 at qinimi/player.
- `druid_epic_wos` set to 1 at wallofslaughter/player.
