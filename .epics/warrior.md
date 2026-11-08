# Warrior

Steps taken from the quest graph only. **Broken** means the graph has no edge for that value or that item.

Flags with writes: `warrior_pre`, `warrior_epic`.

## 0. Prerequisites

Shared acquisition steps appear in the first prerequisite chain that needs them. Later sections reference that chain rather than repeating it.

### "Emblazoned Champion's Hilt" (60288)

1. draniksscar/"Korbuk Brimblade", say "Work". Sets `warrior_pre` to `1`.
2. Loot "Korbuk's Weapon Plans" (60285) from "The Diaku Overseer" in `potactics`.
3. draniksscar/"Korbuk Brimblade", hand "Korbuk's Weapon Plans" (60285). Sets `warrior_pre` to `2`.
4. Loot "Elegant Shank" (60286) from "Shoqui the Forgotten" in `hatesfury`.
5. draniksscar/"Korbuk Brimblade", hand "Elegant Shank" (60286). Sets `warrior_pre` to `3`.
6. Loot "Redblade Family Sword" (60287) from "Drevlon Knacknabber" in `eastkarana`.
7. freeporteast/"Kargek Redblade", hand "Redblade Family Sword" (60287). Requires `warrior_pre` set. Requires `warrior_pre` ==3. Gives "Emblazoned Champion's Hilt" (60288).

### "Dardek's Forged Blade" (60292)

1. Acquisition of "Emblazoned Champion's Hilt" (60288) is documented under "Emblazoned Champion's Hilt" (60288); obtain another copy if needed.
2. draniksscar/"Korbuk Brimblade", hand "Emblazoned Champion's Hilt" (60288). Sets `warrior_pre` to `4`.
3. Acquisition of "Korbuk's Weapon Plans" (60285) is documented under "Emblazoned Champion's Hilt" (60288); obtain another copy if needed.
4. Acquisition of "Elegant Shank" (60286) is documented under "Emblazoned Champion's Hilt" (60288); obtain another copy if needed.
5. thurgadina/"Dardek Bladewright", hand "Korbuk's Weapon Plans" (60285) + "Elegant Shank" (60286) + "Emblazoned Champion's Hilt" (60288). Requires `warrior_pre` ==4. Gives "Dardek's Forged Blade" (60292).

### "Blackfall Blade" (60303)

1. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
2. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `steamfont`.
3. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `tox`.
4. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `toxxulia`.
5. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
6. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). The combine does not fail.
7. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
8. nedaria/"Korezna Orecleaver", hand "Water Flask" (13006) + "Water Flask" (13006) + "Water Flask" (13006) + "Water Flask" (13006). Sets `warrior_epic_korezna` to `1`.
9. nedaria/"Korezna Orecleaver", hand "Water Flask" (13006) + "Water Flask" (13006) + "Water Flask" (13006). Sets `warrior_epic_korezna` to `2`.
10. **Broken:** nothing in the graph gives, loots, spawns, or combines Blackfall Ore (60301).
11. Unresolved cyclic prerequisite: `warrior_epic` ==15.
12. Loot "Champion's Sword of Eternal Power" (60321) from "Krekk Brimblade" in `dranik`.
13. draniksscar/"Korbuk Brimblade", say "Hail". Sets `warrior_epic` to `16`.
14. Acquisition of "Korbuk's Weapon Plans" (60285) is documented under "Emblazoned Champion's Hilt" (60288); obtain another copy if needed.
15. Acquisition of "Elegant Shank" (60286) is documented under "Emblazoned Champion's Hilt" (60288); obtain another copy if needed.
16. Acquisition of "Emblazoned Champion's Hilt" (60288) is documented under "Emblazoned Champion's Hilt" (60288); obtain another copy if needed.
17. thurgadina/"Dardek Bladewright", hand "Korbuk's Weapon Plans" (60285) + "Elegant Shank" (60286) + "Emblazoned Champion's Hilt" (60288). Sets `warrior_pre` to `5`.
18. Acquisition of "Dardek's Forged Blade" (60292) is documented under "Dardek's Forged Blade" (60292); obtain another copy if needed.
19. draniksscar/"Korbuk Brimblade", hand "Dardek's Forged Blade" (60292). Sets `warrior_pre` to `6`.
20. draniksscar/"Korbuk Brimblade", say "Work". Sets `warrior_epic` to `1`.
21. Kill bloodfields/"Girplan Slasher". Spawns "Girplan Devourer" (301063).
22. Loot "Decrepit Hilt" (60307) from "Girplan Devourer".
23. firiona/"Corfia Nultethen", hand "Decrepit Hilt" (60307). Sets `warrior_epic` to `9`.
24. firiona/"Corfia Nultethen", say "Galuk Drek". Sets `warrior_epic_veksar` to `1`.
25. Spawns "Decaying Lord Galuk Drek, not be in db yet" (109906) in `veksar` on enter.
26. Loot "Skeletal Tome of Galuk Drek" (60310) from "Decaying Lord Galuk Drek, not be in db yet".
27. firiona/"Corfia Nultethen", hand "Skeletal Tome of Galuk Drek" (60310). Requires `warrior_epic` set. Requires `warrior_epic` ==9. Gives "Glistening Hilt" (60311).
28. butcher/"Gridbar Galund", hand "Glistening Hilt" (60311). Requires `warrior_epic` set. Requires `warrior_epic` >=13. Gives "Carved Keg Stamp" (60318).
29. shadowhaven/"Koren Galund", hand "Carved Keg Stamp" (60318). Requires `warrior_epic` set. Requires `warrior_epic` >=13. Gives "Tube of Setting Solution" (60319).
30. butcher/"Gridbar Galund", hand "Tube of Setting Solution" (60319). Requires `warrior_epic` set. Requires `warrior_epic` >=13. Gives "Hilt of Eternal Power" (60320).
31. draniksscar/"Korbuk Brimblade", hand "Hilt of Eternal Power" (60320). Sets `warrior_epic` to `14`.
32. everfrost/"Kimber Whitefoot", say "Hail". Requires `warrior_epic` set. Requires `warrior_epic` >=4. Gives "Potion of Blackfall Spirit" (60306).
33. dranik/"Krekk Brimblade", hand "Blackfall Blade" (60303) + "Potion of Blackfall Spirit" (60306) + "Hilt of Eternal Power" (60320). Sets `warrior_epic` to `15`.
34. draniksscar/"Korbuk Brimblade", hand "Blackfall Ore" (60301). Requires `warrior_epic` >=2. Gives "Smelting Plans" (60302).
35. nedaria/"Korezna Orecleaver", hand "Blackfall Ore" (60301) + "Smelting Plans" (60302). Requires `warrior_epic_korezna` ==2. Gives "Blackfall Blade" (60303).

### "Sealed Vial of Blackfall Blood" (60305)

1. Kill vxed/"Blackfall Borerling". Spawns "Blackfall Borer" (290069).
2. Loot "Vial of Blackfall Blood" (60304) from "Blackfall Borer".
3. draniksscar/"Korbuk Brimblade", hand "Vial of Blackfall Blood" (60304). Requires `warrior_epic` >=3. Gives "Sealed Vial of Blackfall Blood" (60305).

### "Potion of Blackfall Spirit" (60306)

1. Acquisition of "Potion of Blackfall Spirit" (60306) is documented under "Blackfall Blade" (60303); obtain another copy if needed.

### "Nocturnal Mask of Acuity" (60309)

1. Common item: Jeweler's Kit (17912). Listed in 33 zones.
2. No quest step gives Darkened Star Rose Quartz (60308). The dump lists it in firiona, qeynos2.
3. Summon "Enchanted Electrum Bar" (16505) by casting "Enchant Electrum", "Mass Enchant Electrum", "Greater Mass Enchant Electrum".
4. Combine in "Jeweler's Kit" (17912): "Darkened Star Rose Quartz" (60308), "Enchanted Electrum Bar" (16505). Produces "Nocturnal Mask of Acuity" (60309). Requires Jewelry Making, trivial 103.

### "Glistening Hilt" (60311)

1. Acquisition of "Glistening Hilt" (60311) is documented under "Blackfall Blade" (60303); obtain another copy if needed.

### "Gemming Tool" (60316)

1. **Broken:** nothing in the graph gives, loots, spawns, or combines Notice to Cease and Desist (9590).
2. Hand "Notice to Cease and Desist" (9590) to freeporteast/"Lythe Songbird". Spawns "a Freeport guard" (382255). Loot "Fine Steel Two Handed Sword" (5351) from "a Freeport guard".
3. 10 alternative loot source(s) also yield Fine Steel Two Handed Sword (5351).
4. Acquisition of "Water Flask" (13006) is documented under "Blackfall Blade" (60303); obtain another copy if needed.
5. Combine in Forge (17): "Fine Steel Two Handed Sword" (5351), "Water Flask" (13006). Produces "Small Brick of High Quality Ore" (10468) x2, "Small Piece of High Quality Ore" (22229). Requires Blacksmithing, trivial 21.
6. Combine in Royal Qeynos Forge (40): "Small Piece of High Quality Ore" (22229), "Water Flask" (13006). Produces "High Quality Metal Bits" (22230). Requires Blacksmithing, trivial 20.
7. Common item: Gemming Mold (60317). Listed in 4 zones.
8. Combine in Forge (17): "High Quality Metal Bits" (22230), "Water Flask" (13006), "Gemming Mold" (60317). Produces "Gemming Tool" (60316). Requires Blacksmithing, trivial 115.

### "Hilt of Eternal Power" (60320)

1. Acquisition of "Hilt of Eternal Power" (60320) is documented under "Blackfall Blade" (60303); obtain another copy if needed.

### "Kreljnok's Focused Rage" (60327)

1. Loot "Kreljnok's Muddled Rage" (60322) from "Possessed Brute" in `provinggrounds`.
2. draniksscar/"Korbuk Brimblade", hand "Kreljnok's Muddled Rage" (60322). Sets `warrior_epic` to `17`.
3. Ground spawn of "Frozen Pestle" (60323) in `iceclad`.
4. iceclad/"Fazzle Thumpkin", hand "Frozen Pestle" (60323). Sets `warrior_epic` to `18`.
5. iceclad/"Fazzle Thumpkin", say "Map". Requires `warrior_epic` ==18. Gives "Fazzle's Map of East Wastes" (60324).
6. Spawns "Larnik the Recluse" (116609) in `eastwastes` on enter.
7. Loot "Larnik's Locked Purification Kit" (60325) from "Larnik the Recluse".
8. draniksscar/"Korbuk Brimblade", hand "Larnik's Locked Purification Kit" (60325). Requires `warrior_epic` >=18. Gives "Larnik's Unlocked Purification Kit" (60326).
9. Combine in "Larnik's Unlocked Purification Kit" (60326): "Kreljnok's Muddled Rage" (60322). Produces "Kreljnok's Focused Rage" (60327). The combine does not fail.

### "Raging Sword of Eternal Power" (60329)

1. global/"Global Player", combine recipe 19902. Sets `warrior_epic` to `21`.
2. Acquisition of "Champion's Sword of Eternal Power" (60321) is documented under "Blackfall Blade" (60303); obtain another copy if needed.
3. Acquisition of "Kreljnok's Focused Rage" (60327) is documented under "Kreljnok's Focused Rage" (60327); obtain another copy if needed.
4. draniksscar/"Korbuk Brimblade", hand "Champion's Sword of Eternal Power" (60321) + "Kreljnok's Focused Rage" (60327). Requires `warrior_epic` >=19. Gives "Raging Sword of Eternal Power" (60329).

## `warrior_pre`

Values written: 1, 2, 3, 4, 5, 6.

### 1. korbuk brimblade — say work

Zone: `draniksscar`.

> Yeah, ok. You look like da respectable type. I wish it was an easy story to tell, but me thinks it

Sets `warrior_pre` to `1`.

- Needs `warrior_pre` unset.
In script order:

1. Sets `warrior_pre` to `1`.


### 2. korbuk brimblade — hand 60285

Zone: `draniksscar`.

Sets `warrior_pre` to `2`.

- Needs `warrior_pre` ==1.
- Turn in x1: Korbuk's Weapon Plans (60285).
In script order:

1. Sets `warrior_pre` to `2`.
2. Gives Korbuk's Weapon Plans (60285).


How the items are reached:

- Korbuk's Weapon Plans (60285)
  - Loot "Korbuk's Weapon Plans" (60285) from "The Diaku Overseer" in `potactics`.

### 3. korbuk brimblade — hand 60286

Zone: `draniksscar`.

Sets `warrior_pre` to `3`.

- Needs `warrior_pre` ==2.
- Turn in x1: Elegant Shank (60286).
In script order:

1. Sets `warrior_pre` to `3`.
2. Gives Elegant Shank (60286).


How the items are reached:

- Elegant Shank (60286)
  - Loot "Elegant Shank" (60286) from "Shoqui the Forgotten" in `hatesfury`.

### 4. korbuk brimblade — hand 60288

Zone: `draniksscar`.

Sets `warrior_pre` to `4`.

- Needs `warrior_pre` ==3.
- Turn in x1: Emblazoned Champion's Hilt (60288).
In script order:

1. Sets `warrior_pre` to `4`.
2. Gives Emblazoned Champion's Hilt (60288).


How the items are reached:

- Emblazoned Champion's Hilt (60288)
  - Prerequisite: "Emblazoned Champion's Hilt" (60288). See section 0.

### 5. dardek bladewright — hand 60285+60286+60288

Zone: `thurgadina`.

Sets `warrior_pre` to `5`.

- Needs `warrior_pre` ==4.
- Turn in x1: Korbuk's Weapon Plans (60285).
- Turn in x1: Elegant Shank (60286).
- Turn in x1: Emblazoned Champion's Hilt (60288).
In script order:

1. Sets `warrior_pre` to `5`.
2. Gives Dardek's Forged Blade (60292).


How the items are reached:

- Korbuk's Weapon Plans (60285)
  - Loot "Korbuk's Weapon Plans" (60285) from "The Diaku Overseer" in `potactics`.
- Elegant Shank (60286)
  - Loot "Elegant Shank" (60286) from "Shoqui the Forgotten" in `hatesfury`.
- Emblazoned Champion's Hilt (60288)
  - Prerequisite: "Emblazoned Champion's Hilt" (60288). See section 0.

### 6. korbuk brimblade — hand 60292

Zone: `draniksscar`.

Sets `warrior_pre` to `6`.

- Needs `warrior_pre` ==5.
- Turn in x1: Dardek's Forged Blade (60292).
In script order:

1. Sets `warrior_pre` to `6`.
2. Gives Korbuk's Blade of Mastery (60293).


How the items are reached:

- Dardek's Forged Blade (60292)
  - Prerequisite: "Dardek's Forged Blade" (60292). See section 0.

### Steps on `warrior_pre` that do not change it

- `draniksscar` korbuk brimblade, say work needs `warrior_pre` ==6.
  - Sets `warrior_epic` to `1`.
- `freeporteast` kargek redblade, hand 60287 needs `warrior_pre` set.
  - Turn in Redblade Family Sword (60287).
  - Gives Emblazoned Champion's Hilt (60288).
- `freporte` kargek redblade, hand 60287 needs `warrior_pre` set.
  - Turn in Redblade Family Sword (60287).
  - Gives Emblazoned Champion's Hilt (60288).
- `thurgadina` dardek bladewright, hand 60289 needs `warrior_pre` ==4.
  - Turn in Coldain Coffee Blend (60289).

## `warrior_epic`

Values written: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21.

### 1. korbuk brimblade — say work

Zone: `draniksscar`.

> Yeah, ok. You look like da respectable type. I wish it was an easy story to tell, but me thinks it

Sets `warrior_epic` to `1`.

- Needs `warrior_epic` unset.
- Needs `warrior_pre` ==6.
In script order:

1. Sets `warrior_epic` to `1`.


This step also depends on `warrior_pre`, shown above.

### 2. korbuk brimblade — hand 60295+60296+60297+60298

Zone: `draniksscar`.

Sets `warrior_epic` to `2`.

- Needs `warrior_epic` >=1.
- Turn in x1: Decomposing Page I (60295).
- Turn in x1: Decomposing Page II (60296).
- Turn in x1: Decomposing Page III (60297).
- Turn in x1: Decomposing Cover (60298).
In script order:

1. Sets `warrior_epic` to `2`.
2. Gives Decomposing Page I (60295).
3. Gives Decomposing Page II (60296).
4. Gives Decomposing Page III (60297).
5. Gives Decomposing Cover (60298).


How the items are reached:

- Decomposing Page I (60295)
  - Ground spawn of "Decomposing Page I" (60295) in `draniksscar`.
- Decomposing Page II (60296)
  - Ground spawn of "Decomposing Page II" (60296) in `draniksscar`.
- Decomposing Page III (60297)
  - Ground spawn of "Decomposing Page III" (60297) in `draniksscar`.
- Decomposing Cover (60298)
  - Ground spawn of "Decomposing Cover" (60298) in `draniksscar`.

### 3. korbuk brimblade — hand 60303

Zone: `draniksscar`.

Sets `warrior_epic` to `3`.

- Needs `warrior_epic` >=2.
- Turn in x1: Blackfall Blade (60303).
In script order:

1. Sets `warrior_epic` to `3`.
2. Gives Blackfall Blade (60303).


How the items are reached:

- Blackfall Blade (60303)
  - Prerequisite: "Blackfall Blade" (60303). See section 0.

### 4. kimber whitefoot — hand 60305

Zone: `everfrost`.

Sets `warrior_epic` to `4`.

- Needs `warrior_epic` set.
- Needs `warrior_epic` >=3.
- Needs `warrior_epic` <4.
- Turn in x1: Sealed Vial of Blackfall Blood (60305).
In script order:

1. Sets `warrior_epic` to `4`.


How the items are reached:

- Sealed Vial of Blackfall Blood (60305)
  - Prerequisite: "Sealed Vial of Blackfall Blood" (60305). See section 0.

### 5. korbuk brimblade — hand 60306

Zone: `draniksscar`.

Sets `warrior_epic` to `5`.

- Needs `warrior_epic` >=4.
- Turn in x1: Potion of Blackfall Spirit (60306).
In script order:

1. Sets `warrior_epic` to `5`.
2. Gives Potion of Blackfall Spirit (60306).


How the items are reached:

- Potion of Blackfall Spirit (60306)
  - Prerequisite: "Potion of Blackfall Spirit" (60306). See section 0.

### 6. korbuk brimblade — hand 60307

Zone: `draniksscar`.

Sets `warrior_epic` to `6`.

- Needs `warrior_epic` >=5.
- Turn in x1: Decrepit Hilt (60307).
In script order:

1. Sets `warrior_epic` to `6`.
2. Gives Decrepit Hilt (60307).


How the items are reached:

- Decrepit Hilt (60307)
  - Kill bloodfields/"Girplan Slasher". Spawns "Girplan Devourer" (301063).
  - Loot "Decrepit Hilt" (60307) from "Girplan Devourer".

### 7. corfia nultethen — hand 16503

Zone: `firiona`.

Sets `warrior_epic` to `7`.

- Needs `warrior_epic` set.
- Needs `warrior_epic` >=6.
- Needs `warrior_epic` <7.
- Turn in x1: Platinum Bar (16503).
In script order:

1. Sets `warrior_epic` to `7`.


How the items are reached:

- Platinum Bar (16503)
  - Common item: Platinum Bar (16503). Listed in 30 zones.

### 8. corfia nultethen — hand 60309

Zone: `firiona`.

Sets `warrior_epic` to `8`.

- Needs `warrior_epic` set.
- Needs `warrior_epic` >=7.
- Needs `warrior_epic` <8.
- Turn in x1: Nocturnal Mask of Acuity (60309).
In script order:

1. Sets `warrior_epic` to `8`.


How the items are reached:

- Nocturnal Mask of Acuity (60309)
  - Prerequisite: "Nocturnal Mask of Acuity" (60309). See section 0.

### 9. corfia nultethen — hand 60307

Zone: `firiona`.

Sets `warrior_epic` to `9`.

- Needs `warrior_epic` set.
- Needs `warrior_epic` >=8.
- Needs `warrior_epic` <9.
- Turn in x1: Decrepit Hilt (60307).
In script order:

1. Sets `warrior_epic` to `9`.


How the items are reached:

- Decrepit Hilt (60307)
  - Kill bloodfields/"Girplan Slasher". Spawns "Girplan Devourer" (301063).
  - Loot "Decrepit Hilt" (60307) from "Girplan Devourer".

### 10. korbuk brimblade — hand 60311

Zone: `draniksscar`.

Sets `warrior_epic` to `10`.

- Needs `warrior_epic` >=9.
- Turn in x1: Glistening Hilt (60311).
In script order:

1. Sets `warrior_epic` to `10`.
2. Gives Glistening Hilt (60311).


How the items are reached:

- Glistening Hilt (60311)
  - Prerequisite: "Glistening Hilt" (60311). See section 0.

### 11. korbuk brimblade — hand 60312+60313+60314+60315

Zone: `draniksscar`.

Sets `warrior_epic` to `11`.

- Needs `warrior_epic` ==10.
- Turn in x1: Stone of Eternal Power: Northeast Eye (60312).
- Turn in x1: Stone of Eternal Power: Northwest Eye (60313).
- Turn in x1: Stone of Eternal Power: Southeast Eye (60314).
- Turn in x1: Stone of Eternal Power: Southwest Eye (60315).
In script order:

1. Sets `warrior_epic` to `11`.
2. Gives Stone of Eternal Power: Northeast Eye (60312).
3. Gives Stone of Eternal Power: Northwest Eye (60313).
4. Gives Stone of Eternal Power: Southeast Eye (60314).
5. Gives Stone of Eternal Power: Southwest Eye (60315).


How the items are reached:

- Stone of Eternal Power: Northeast Eye (60312)
  - Loot "Stone of Eternal Power: Northeast Eye" (60312) from "Dragorn Champion" in `wallofslaughter`.
- Stone of Eternal Power: Northwest Eye (60313)
  - Ground spawn of "Stone of Eternal Power: Northwest Eye" (60313) in `bloodfields`.
- Stone of Eternal Power: Southeast Eye (60314)
  - Ground spawn of "Stone of Eternal Power: Southeast Eye" (60314) in `provinggrounds`.
- Stone of Eternal Power: Southwest Eye (60315)
  - Ground spawn of "Stone of Eternal Power: Southwest Eye" (60315) in `causeway`.

### 12. gridbar galund — hand 60312+60313+60314+60315

Zone: `butcher`.

Sets `warrior_epic` to `12`.

- Needs `warrior_epic` set.
- Needs `warrior_epic` >=11.
- Turn in x1: Stone of Eternal Power: Northeast Eye (60312).
- Turn in x1: Stone of Eternal Power: Northwest Eye (60313).
- Turn in x1: Stone of Eternal Power: Southeast Eye (60314).
- Turn in x1: Stone of Eternal Power: Southwest Eye (60315).
In script order:

1. Sets `warrior_epic` to `12`.


How the items are reached:

- Stone of Eternal Power: Northeast Eye (60312)
  - Loot "Stone of Eternal Power: Northeast Eye" (60312) from "Dragorn Champion" in `wallofslaughter`.
- Stone of Eternal Power: Northwest Eye (60313)
  - Ground spawn of "Stone of Eternal Power: Northwest Eye" (60313) in `bloodfields`.
- Stone of Eternal Power: Southeast Eye (60314)
  - Ground spawn of "Stone of Eternal Power: Southeast Eye" (60314) in `provinggrounds`.
- Stone of Eternal Power: Southwest Eye (60315)
  - Ground spawn of "Stone of Eternal Power: Southwest Eye" (60315) in `causeway`.

### 13. gridbar galund — hand 15433+60316

Zone: `butcher`.

Sets `warrior_epic` to `13`.

- Needs `warrior_epic` set.
- Needs `warrior_epic` >=12.
- Turn in x1: Gemming Tool (60316).
- Turn in x1: Spell: Fire (15433).
In script order:

1. Sets `warrior_epic` to `13`.


How the items are reached:

- Gemming Tool (60316)
  - Prerequisite: "Gemming Tool" (60316). See section 0.
- Spell: Fire (15433)
  - Common item: Spell: Fire (15433). Listed in 5 zones.

### 14. korbuk brimblade — hand 60320

Zone: `draniksscar`.

Sets `warrior_epic` to `14`.

- Needs `warrior_epic` >=13.
- Turn in x1: Hilt of Eternal Power (60320).
In script order:

1. Sets `warrior_epic` to `14`.
2. Gives Hilt of Eternal Power (60320).


How the items are reached:

- Hilt of Eternal Power (60320)
  - Prerequisite: "Hilt of Eternal Power" (60320). See section 0.

### 15. krekk brimblade — hand 60303+60306+60320

Zone: `dranik`.

Sets `warrior_epic` to `15`.

- Needs `warrior_epic` ==14.
- Turn in x1: Hilt of Eternal Power (60320).
- Turn in x1: Potion of Blackfall Spirit (60306).
- Turn in x1: Blackfall Blade (60303).
In script order:

1. Sets `warrior_epic` to `15`.


How the items are reached:

- Hilt of Eternal Power (60320)
  - Prerequisite: "Hilt of Eternal Power" (60320). See section 0.
- Potion of Blackfall Spirit (60306)
  - Prerequisite: "Potion of Blackfall Spirit" (60306). See section 0.
- Blackfall Blade (60303)
  - Prerequisite: "Blackfall Blade" (60303). See section 0.

### 16. korbuk brimblade — say hail

Zone: `draniksscar`.

> You were able to purify da presence, good. Just as I thought, da essence is pure and unadultered. Things are becoming ever clearer da closer we come to unrav...

Sets `warrior_epic` to `16`.

- Needs `warrior_epic` ==15.
- Needs Champion's Sword of Eternal Power (60321).
In script order:

1. Sets `warrior_epic` to `16`.


How the items are reached:

- Champion's Sword of Eternal Power (60321)
  - Loot "Champion's Sword of Eternal Power" (60321) from "Krekk Brimblade" in `dranik`.

### 17. korbuk brimblade — hand 60322

Zone: `draniksscar`.

Sets `warrior_epic` to `17`.

- Needs `warrior_epic` >=16.
- Turn in x1: Kreljnok's Muddled Rage (60322).
In script order:

1. Sets `warrior_epic` to `17`.
2. Gives Kreljnok's Muddled Rage (60322).


How the items are reached:

- Kreljnok's Muddled Rage (60322)
  - Loot "Kreljnok's Muddled Rage" (60322) from "Possessed Brute" in `provinggrounds`.

### 18. fazzle thumpkin — hand 60323

Zone: `iceclad`.

Sets `warrior_epic` to `18`.

- Needs `warrior_epic` ==17.
- Turn in x1: Frozen Pestle (60323).
In script order:

1. Sets `warrior_epic` to `18`.


How the items are reached:

- Frozen Pestle (60323)
  - Ground spawn of "Frozen Pestle" (60323) in `iceclad`.

### 19. korbuk brimblade — hand 47100

Zone: `draniksscar`.

Sets `warrior_epic` to `19`.

- Needs `warrior_epic` >=18.
- Turn in x1: Globe of Discordant Energy (47100).
In script order:

1. Sets `warrior_epic` to `19`.


How the items are reached:

- Globe of Discordant Energy (47100)
  - Say "Check Lorb" to anguish/"Zone Status".
  - Spawns "Orb of Discordant Energy" (317087).
  - Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy".
  - 4 alternative loot source(s) also yield Globe of Discordant Energy (47100).

### 20. korbuk brimblade — hand 60321+60327

Zone: `draniksscar`.

Sets `warrior_epic` to `20`.

- Needs `warrior_epic` >=19.
- Turn in x1: Champion's Sword of Eternal Power (60321).
- Turn in x1: Kreljnok's Focused Rage (60327).
In script order:

1. Sets `warrior_epic` to `20`.
2. Gives Raging Sword of Eternal Power (60329).


How the items are reached:

- Champion's Sword of Eternal Power (60321)
  - Loot "Champion's Sword of Eternal Power" (60321) from "Krekk Brimblade" in `dranik`.
- Kreljnok's Focused Rage (60327)
  - Prerequisite: "Kreljnok's Focused Rage" (60327). See section 0.

### 21. global player — combine recipe 19902

Zone: `global`.

Sets `warrior_epic` to `21`.

In script order:

1. Sets `warrior_epic` to `21`.


Combine:

- `recipe:19902` is combined in Brimblade's Scabbard (60331).
  - Kill causeway/"Korbuk Brimblade". Spawns "Essence of Kreljnok" (303129).
  - Loot "Brimblade's Scabbard" (60331) from "Essence of Kreljnok".
  - Put in x1: Kreljnok's Essence (60330).
    - Kill causeway/"Korbuk Brimblade". Spawns "Essence of Kreljnok" (303129).
    - Loot "Kreljnok's Essence" (60330) from "Essence of Kreljnok".
  - Put in x1: Raging Sword of Eternal Power (60329).
    - Prerequisite: "Raging Sword of Eternal Power" (60329). See section 0.
  - Produces Kreljnok's Sword of Eternal Power (60332).
  - The combine does not fail.

### Steps on `warrior_epic` that do not change it

- `abysmal` rewina jalmoy, hand 60295+60296+60297+60298 needs `warrior_epic` set.
  - Turn in Decomposing Page I (60295).
  - Turn in Decomposing Page II (60296).
  - Turn in Decomposing Page III (60297).
  - Turn in Decomposing Cover (60298).
  - Gives Recounted History of War (60299).
- `bloodfields` player, on loot needs `warrior_epic` set.
  - Sets `warr_epic_bloodfield` to `1`.
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
- `butcher` gridbar galund, hand 60311 needs `warrior_epic` set.
  - Turn in Glistening Hilt (60311).
  - Gives Carved Keg Stamp (60318).
- `butcher` gridbar galund, hand 60319 needs `warrior_epic` set.
  - Turn in Tube of Setting Solution (60319).
  - Gives Hilt of Eternal Power (60320).
- `causeway` player, on loot needs `warrior_epic` ==20.
  - Sets `warr_chest_causeway` to `1`.
  - Spawns a chest (epic 2.0) (893).
- `causeway` warr trap, on enter needs `warrior_epic` ==20.
  - Spawns Korbuk (303128).
- `dranik` player, on loot needs `warrior_epic` ==15.
  - Sets `warrior_epic_dranik` to `1`.
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
- `draniksscar` korbuk brimblade, hand 60299 needs `warrior_epic` >=2.
  - Turn in Recounted History of War (60299).
- `draniksscar` korbuk brimblade, hand 60301 needs `warrior_epic` >=2.
  - Turn in Blackfall Ore (60301).
  - Gives Blackfall Ore (60301).
  - Gives Smelting Plans (60302).
- `draniksscar` korbuk brimblade, hand 60304 needs `warrior_epic` >=3.
  - Turn in Vial of Blackfall Blood (60304).
  - Gives Sealed Vial of Blackfall Blood (60305).
- `draniksscar` korbuk brimblade, hand 60325 needs `warrior_epic` >=18.
  - Turn in Larnik's Locked Purification Kit (60325).
  - Gives Larnik's Unlocked Purification Kit (60326).
- `draniksscar` korbuk brimblade, say loose needs `warrior_epic` set.
  - Sets `warrior_epic_vxed` to `1`.
- `draniksscar` korbuk brimblade, say rock needs `warrior_epic` set.
  - Gives Energy Receptor (60300).
- `everfrost` kimber whitefoot, say hail needs `warrior_epic` set.
  - Gives Potion of Blackfall Spirit (60306).
- `everfrost` kimber whitefoot, say hail needs `warrior_epic` set.
  - Gives Potion of Blackfall Spirit (60306).
- `firiona` corfia nultethen, say galuk drek needs `warrior_epic` set.
  - Sets `warrior_epic_veksar` to `1`.
- `firiona` corfia nultethen, hand 60310 needs `warrior_epic` set.
  - Turn in Skeletal Tome of Galuk Drek (60310).
  - Gives Glistening Hilt (60311).
- `iceclad` fazzle thumpkin, say map needs `warrior_epic` ==18.
  - Gives Fazzle's Map of East Wastes (60324).
- `nedaria` a blacksmith, say hail needs `warrior_epic` set.
  - Spawns Korezna Orecleaver (182149).
- `shadowhaven` koren galund, hand 60318 needs `warrior_epic` set.
  - Turn in Carved Keg Stamp (60318).
  - Gives Tube of Setting Solution (60319).
- `wallofslaughter` player, on loot needs `warrior_epic` ==10.
  - Sets `warr_epic_wos` to `1`.
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

## Other flags touched along the way

- `warr_epic_bloodfield` set to 1 at bloodfields/player.
- `warr_epic_wos` set to 1 at wallofslaughter/player.
- `warrior_epic_dranik` set to 1 at dranik/player.
- `warrior_epic_gulak` set to 1 at veksar/player.
- `warrior_epic_korezna` set to 1, 2 at nedaria/korezna orecleaver.
- `warrior_epic_veksar` set to 1 at firiona/corfia nultethen.
- `warrior_epic_vxed` set to 1 at draniksscar/korbuk brimblade.
