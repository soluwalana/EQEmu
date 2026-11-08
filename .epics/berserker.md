# Berserker

Steps taken from the quest graph only. **Broken** means the graph has no edge for that value or that item.

Flags with writes: `berserk_epic`.

## 0. Prerequisites

Shared acquisition steps appear in the first prerequisite chain that needs them. Later sections reference that chain rather than repeating it.

### "Raging Soul Shard" (11999)

1. sebilis/"Berserkerepic 1 5", say "Protector Timer". Gives "Taelosian Alloy Blood Axe" (18976).
2. sebilis/"Berserkerepic 1 5", say "Protector Timer". Gives "Broken Trial Taelosian Blood Axe" (17833).
3. sebilis/"Berserkerepic 1 5", say "Protector Timer". Gives "Damaged Trial Taelosian Blood Axe" (17898).
4. sebilis/"Berserkerepic 1 5", say "Protector Timer". Gives "Damaged Trial Taelosian Blood Axe" (17399).
5. lakeofillomen/"Keras Mcarik", hand "Damaged Trial Taelosian Blood Axe" (17399) + "Broken Trial Taelosian Blood Axe" (17833) + "Damaged Trial Taelosian Blood Axe" (17898) + "Taelosian Alloy Blood Axe" (18976). Sets `berserk_epic` to `5`.
6. abysmal/"Teekan Opousbabolaoi", hand "Raging Soul Shard" (11999) + "Taelosian Alloy Blood Axe" (18976). Sets `berserk_epic` to `7`.
7. Unresolved cyclic prerequisite: `berserk_epic` >=7.
8. lakeofillomen/"Keras Mcarik", say "Find Out". Sets `berserk_epic` to `8`.
9. halas/"Shanis Macdarren", say "Hail". Requires `berserk_epic` >=1. Requires `berserk_epic` set. Gives "Raging Soul Shard" (11999).

### "Julei's Twilight Pendant" (17200)

1. hole/"Julei Direaxe", say "Hail". Requires `berserk_epic` ==8. Gives "Julei's Twilight Pendant" (17200).

### "Unhoned Vengeful Taelosian Blood Axe" (20072)

1. Loot "Lightning Core" (72029) from "A Lightning Warrior Stormer" (NPC 317083) in `anguish`. Drop cache: 0.5% chance per kill.
2. Acquisition of "Taelosian Alloy Blood Axe" (18976) is documented under "Raging Soul Shard" (11999); obtain another copy if needed.
3. Acquisition of "Raging Soul Shard" (11999) is documented under "Raging Soul Shard" (11999); obtain another copy if needed.
4. abysmal/"Teekan Opousbabolaoi", hand "Raging Soul Shard" (11999) + "Taelosian Alloy Blood Axe" (18976). Requires `berserk_epic` ==5. Gives "Raging Taelosian Alloy Axe" (18398).
5. causeway/"Bazu Smasher", on event combat.
6. Starts timer `wipecheck`.
7. Spawns "Bazu Smasher" (303081) after `causeway/bazu smasher#timer:wipecheck`.
8. Loot "Faceted Moonstone" (17349) from "Bazu Smasher".
9. Loot "Shadowed Bronze Lump" (17137) from "An Ancient Necromantic Shade" in `griegsend`.
10. lakeofillomen/"Keras Mcarik", hand "Shadowed Bronze Lump" (17137) + "Faceted Moonstone" (17349) + "Raging Taelosian Alloy Axe" (18398) + "Lightning Core" (72029). Gives "Unhoned Vengeful Taelosian Blood Axe" (20072).

### "Medal of Mastery" (60210)

1. Loot "Treanik's Tarnished Axe" (60200) at cauldron/"Praklion Of The Cauldron", on event_hp.
2. cauldron/"Treanik Ireblade", hand "Treanik's Tarnished Axe" (60200). Gives "Bone Trinket" (60201).
3. fieldofbone/"Berserker-S Image", on event_death_complete. Sets `bersolo` to `1`.
4. fieldofbone/"Mardic Crimsonsteel", say "Hail". Requires `bersolo` ==1. Gives "Image Essence" (60196).
5. Say "Defeat" to lakeofillomen/"Lingering Axefall".
6. Spawns "An Impervious Bloodbeast" (85225).
7. Loot "Bloodbeast Tooth" (60192) from "An Impervious Bloodbeast".
8. lakeofillomen/"Keras Mcarik", say "Great Stride". Gives "Medal of Blood" (60190).
9. lakeofillomen/"Keras Mcarik", hand "Medal of Blood" (60190) + "Bloodbeast Tooth" (60192). Gives "Medal of Mirages" (60194).
10. lakeofillomen/"Keras Mcarik", hand "Medal of Mirages" (60194) + "Image Essence" (60196). Gives "Medal of Strategy" (60198).
11. lakeofillomen/"Keras Mcarik", hand "Medal of Strategy" (60198) + "Bone Trinket" (60201). Gives "Medal of Fervid Rage" (60202).
12. Kill fearplane/"Enraged Imp". Spawns "Ireblind Imp" (72069).
13. Loot "Burning Essence of Rage" (60203) from "Ireblind Imp".
14. lakeofillomen/"Keras Mcarik", hand "Medal of Fervid Rage" (60202) + "Burning Essence of Rage" (60203). Gives "Medal of Hunting" (60204).
15. lakeofillomen/"Keras Mcarik", say "Do". Gives "McArik Reagent Satchel" (60205).
16. Loot "Decaying Liver" (60206) from "Disease-Ridden Gorilla" in `emeraldjungle`.
17. Loot "Gnashing Kobold Paw" (60207) from "Gnashing Kobold" in `stonebrunt`.
18. Loot "Scent Gland" (60208) from "Reeking Skunk" in `tox`.
19. Loot "Scent Gland" (60208) from "Reeking Skunk" in `toxxulia`.
20. Buy "Medicine Bag" (17901) from "Rendallen Ironforge" (NPC 2071) in `qeynos2`. Base price: 1,000 copper.
21. Buy "Handful of Prism Grains" (95922) from "Murak" (NPC 49085) in `oggok`. Base price: 800 copper.
22. Loot "Heliotrope" (14242) from "a Di'zok Herbalist" in `chardok`.
23. Loot "Heliotrope" (14242) from "a Sarnak Herb Collector" in `chardok`.
24. Loot "Heliotrope" (14242) from "an Apprentice Herbalist" in `chardok`.
25. Buy "Yebamante" (16510) from "Guri" (NPC 30098) in `everfrost`. Base price: 25,000 copper.
26. Buy "Blade Leaf" (22143) from "Guri" (NPC 30098) in `everfrost`. Base price: 2,500 copper.
27. Buy "Simple Potion Vial" (95843) from "Guri" (NPC 30098) in `everfrost`. Base price: 750 copper.
28. Combine in "Medicine Bag" (17901): "Handful of Prism Grains" (95922), "Heliotrope" (14242), "Yebamante" (16510), "Blade Leaf" (22143), "Simple Potion Vial" (95843). Produces "Philter of Major Translocation" (96467). Requires Alchemy, trivial 131.
29. Combine in "McArik Reagent Satchel" (60205): "Decaying Liver" (60206), "Gnashing Kobold Paw" (60207), "Scent Gland" (60208), "Philter of Major Translocation" (96467). Produces "Bag of Image Essence Dust" (60209). The combine does not fail.
30. lakeofillomen/"Keras Mcarik", hand "Medal of Hunting" (60204) + "Bag of Image Essence Dust" (60209). Gives "Medal of Mastery" (60210).

### "Kerasian Axe of Ire" (68299)

1. Acquisition of "Medal of Mastery" (60210) is documented under "Medal of Mastery" (60210); obtain another copy if needed.
2. Spawns "Raving Goblinmaster - KOS" (79126) in `warslikswood` on event_waypoint_arrive.
3. Loot "Maniac's Garbled Tome" (60211) from "Raving Goblinmaster - KOS".
4. lakeofillomen/"Keras Mcarik", hand "Medal of Mastery" (60210) + "Maniac's Garbled Tome" (60211). Gives "Kerasian Axe of Ire" (68299).

## `berserk_epic`

Values written: 1, 2, 3, 4, 5, 7, 8, 9, 10.

### 1. keras mcarik — say hail

Zone: `lakeofillomen`.

> Return once you have trained more, young Berserker.

Sets `berserk_epic` to `1`.

- Needs Kerasian Axe of Ire (68299).
In script order:

1. Sets `berserk_epic` to `1`.


How the items are reached:

- Kerasian Axe of Ire (68299)
  - Prerequisite: "Kerasian Axe of Ire" (68299). See section 0.

Alternative or repeat transition to `berserk_epic` = `1` (not an additional required stage).

### 1. keras mcarik — hand 60210+60211

Zone: `lakeofillomen`.

Sets `berserk_epic` to `1`.

- Turn in x1: Medal of Mastery (60210).
- Turn in x1: Maniac's Garbled Tome (60211).
In script order:

1. Sets `berserk_epic` to `1`.
2. Gives Kerasian Axe of Ire (68299).


How the items are reached:

- Medal of Mastery (60210)
  - Prerequisite: "Medal of Mastery" (60210). See section 0.
- Maniac's Garbled Tome (60211)
  - Spawns "Raving Goblinmaster - KOS" (79126) in `warslikswood` on event_waypoint_arrive.
  - Loot "Maniac's Garbled Tome" (60211) from "Raving Goblinmaster - KOS".

### 2. baeldarr hawkeye — hand 15793+17319+17496+17589

Zone: `poknowledge`.

Sets `berserk_epic` to `2`.

- Needs `berserk_epic` set.
- Needs `berserk_epic` >=1.
- Turn in x1: Taelosian Tempered Ore (15793).
- Turn in x1: Taelosian Tempered Ore (17589).
- Turn in x1: Taelosian Tempered Ore (17319).
- Turn in x1: Taelosian Tempered Ore (17496).
In script order:

1. Sets `berserk_epic` to `2`.


How the items are reached:

- Taelosian Tempered Ore (15793)
  - Given by lakeofillomen/"Keras Mcarik", say "Check5Globalserk".
- Taelosian Tempered Ore (17589)
  - Given by lakeofillomen/"Keras Mcarik", say "Check5Globalserk".
- Taelosian Tempered Ore (17319)
  - Given by lakeofillomen/"Keras Mcarik", say "Check5Globalserk".
- Taelosian Tempered Ore (17496)
  - Given by lakeofillomen/"Keras Mcarik", say "Check5Globalserk".

### 3. keras mcarik — say hail

Zone: `lakeofillomen`.

> Return once you have trained more, young Berserker.

Sets `berserk_epic` to `3`.

- Needs `berserk_epic` ==1.
- Needs `berserk_epic` ==2.
- Needs Raging Soul Shard (11999).
- Needs `berserk_epic` >=1.
- Needs `berserk_epic` set.
In script order:

1. Sets `berserk_epic` to `3`.


How the items are reached:

- Raging Soul Shard (11999)
  - Prerequisite: "Raging Soul Shard" (11999). See section 0.

Alternative or repeat transition to `berserk_epic` = `3` (not an additional required stage).

### 3. baeldarr hawkeye — hand 17286+17286+17286+17286

Zone: `poknowledge`.

Sets `berserk_epic` to `3`.

- Needs `berserk_epic` set.
- Needs `berserk_epic` >=2.
- Turn in x1: Darkwood Sapling Branch (17286).
In script order:

1. Sets `berserk_epic` to `3`.
2. Gives Trial Taelosian Alloy Blood Axe (17370).
3. Gives Trial Taelosian Alloy Blood Axe (17700).
4. Gives Trial Taelosian Alloy Blood Axe (17759).
5. Gives Trial Taelosian Alloy Blood Axe (16779).


How the items are reached:

- Darkwood Sapling Branch (17286)
  - Ground spawn of "Darkwood Sapling Branch" (17286) in `draniksscar`.

### 4. berserkerepic 1 5 — say protector_death

Zone: `sebilis`.

Sets `berserk_epic` to `4`.

In script order:

1. Sets `berserk_epic_sebchest` to `1`.
2. Sets `berserk_epic` to `4`.


### 5. keras mcarik — hand 17399+17833+17898+18976

Zone: `lakeofillomen`.

Sets `berserk_epic` to `5`.

- Turn in x1: Taelosian Alloy Blood Axe (18976).
- Turn in x1: Broken Trial Taelosian Blood Axe (17833).
- Turn in x1: Damaged Trial Taelosian Blood Axe (17898).
- Turn in x1: Damaged Trial Taelosian Blood Axe (17399).
In script order:

1. Sets `berserk_epic` to `5`.
2. Gives Taelosian Alloy Blood Axe (18976).


How the items are reached:

- Taelosian Alloy Blood Axe (18976)
  - Given by sebilis/"Berserkerepic 1 5", say "Protector Timer".
- Broken Trial Taelosian Blood Axe (17833)
  - Given by sebilis/"Berserkerepic 1 5", say "Protector Timer".
- Damaged Trial Taelosian Blood Axe (17898)
  - Given by sebilis/"Berserkerepic 1 5", say "Protector Timer".
- Damaged Trial Taelosian Blood Axe (17399)
  - Given by sebilis/"Berserkerepic 1 5", say "Protector Timer".

### 7. teekan opousbabolaoi — hand 11999+18976

Zone: `abysmal`.

Sets `berserk_epic` to `7`.

- Needs `berserk_epic` ==5.
- Turn in x1: Taelosian Alloy Blood Axe (18976).
- Turn in x1: Raging Soul Shard (11999).
In script order:

1. Sets `berserk_epic` to `7`.
2. Gives Raging Taelosian Alloy Axe (18398).


How the items are reached:

- Taelosian Alloy Blood Axe (18976)
  - Given by sebilis/"Berserkerepic 1 5", say "Protector Timer".
- Raging Soul Shard (11999)
  - Prerequisite: "Raging Soul Shard" (11999). See section 0.

### 8. keras mcarik — say find out

Zone: `lakeofillomen`.

> I dinnah not exactly know where she may be, but her name is Julei Direaxe and I fear that she may be in trouble. Please, hurry, strike out and find her, resc...

Sets `berserk_epic` to `8`.

- Needs `berserk_epic` ==7.
- Needs `berserk_epic` >=7.
- Needs `berserk_epic` set.
In script order:

1. Sets `berserk_epic` to `8`.


### 9. keras mcarik — hand 17200

Zone: `lakeofillomen`.

Sets `berserk_epic` to `9`.

- Turn in x1: Julei's Twilight Pendant (17200).
In script order:

1. Sets `berserk_epic` to `9`.


How the items are reached:

- Julei's Twilight Pendant (17200)
  - Prerequisite: "Julei's Twilight Pendant" (17200). See section 0.

### 10. grithyank avlonnon — hand 20072+47100

Zone: `dranik`.

Sets `berserk_epic` to `10`.

- Needs `berserk_epic` ==9.
- Turn in x1: Unhoned Vengeful Taelosian Blood Axe (20072).
- Turn in x1: Globe of Discordant Energy (47100).
In script order:

1. Sets `berserk_epic` to `10`.
2. Gives Vengeful Taelosian Blood Axe (18609).


How the items are reached:

- Unhoned Vengeful Taelosian Blood Axe (20072)
  - Prerequisite: "Unhoned Vengeful Taelosian Blood Axe" (20072). See section 0.
- Globe of Discordant Energy (47100)
  - Say "Check Lorb" to anguish/"Zone Status".
  - Spawns "Orb of Discordant Energy" (317087).
  - Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy".
  - Alternative: Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy" (NPC 317087) in `anguish`; trigger: anguish/"Zone Status", say "Check Uorb".
  - Alternative: Loot "Globe of Discordant Energy" (47100) from "Ornate Chest" (NPC 317112) in `anguish`; trigger: anguish/"Zone Status", say "Check Amv Chest".
  - Alternative: Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy" (NPC 317087) in `anguish`; trigger: anguish/"Zone Status", on event_signal.
  - Alternative: Loot "Globe of Discordant Energy" (47100) from "Overlords Chest" (NPC 317124) in `anguish`; trigger: anguish/"Zone Status", on event_signal.

### Steps on `berserk_epic` that do not change it

- `bloodfields` tarvash scriller, hand gold:50 needs `berserk_epic` ==9.
- `bloodfields` tarvash scriller, hand platinum:50 needs `berserk_epic` ==9.
- `causeway` player, on loot needs `berserk_epic` ==9.
  - Sets `ber_chest_causeway` to `1`.
  - Spawns a chest (epic 2.0) (893).
- `griegsend` player, on loot needs `berserk_epic` ==9.
  - Sets `ber_epic_ge` to `1`.
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
- `halas` shanis macdarren, say hail needs `berserk_epic` >=1.
  - Gives Raging Soul Shard (11999).
- `hole` julei direaxe, say hail needs `berserk_epic` ==8.
  - Gives Julei's Twilight Pendant (17200).
- `kaladimb` dravel axethrasher, say hail needs `berserk_epic` >=1.
  - Gives Raging Soul Shard (11999).
- `oggok` baddi waca, say hail needs `berserk_epic` >=1.
  - Gives Raging Soul Shard (11999).
- `sharvahl` vrasha piennsa, say hail needs `berserk_epic` >=1.
  - Gives Raging Soul Shard (11999).

## Other flags touched along the way

- `ber_epic_ge` set to 1 at griegsend/player.
- `berserk_epic_crag` set to 1 at lakeofillomen/keras mcarik.
- `berserk_epic_fern` set to 1 at lakeofillomen/keras mcarik.
- `berserk_epic_hyn` set to 1 at lakeofillomen/keras mcarik.
- `berserk_epic_ore` set to 1 at lakeofillomen/keras mcarik.
- `berserk_epic_sebchest` set to 1 at sebilis/berserkerepic 1 5.
- `berserk_epic_tea` set to 1 at lakeofillomen/keras mcarik.
- `berserk_epic_test16779` set to 1 at sebilis/berserkerepic 1 5.
- `berserk_epic_test17370` set to 1 at sebilis/berserkerepic 1 5.
- `berserk_epic_test17700` set to 1 at sebilis/berserkerepic 1 5.
- `berserk_epic_test17759` set to 1 at sebilis/berserkerepic 1 5.
