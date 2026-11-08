# Bard

Steps taken from the quest graph only. **Broken** means the graph has no edge for that value or that item.

Flags with writes: `bardPQ`, `Fatestealer_bard`, `bard15`, `bard20`.

## 0. Prerequisites

Each list is the order you obtain that item. Later steps point here instead of repeating the chain.

### "Ragebringer" (11057)

1. Loot "Bayle List I" (18808) from "Mutt Rootlit" in `highpass`.
2. qrg/"Gerael Woodone", say "Deliver A Flask". Gives "Flask of Nitrates" (13945).
3. akanon/"Kimble Nogflop", hand "Flask of Nitrates" (13945). Gives "Regurgitonic" (12140).
4. qrg/"Mammoth", hand "Regurgitonic" (12140). Gives "Bayle List II" (18809).
5. Loot "Bayle List III" (18810) from "Dyllin Starsine" in `highpass`.
6. Loot "Bayle List III" (18810) from "Dyllin Starsine" in `highpasshold`.
7. southro/"Rathmana Allin", hand "Bayle List I" (18808) + "Bayle List II" (18809) + "Bayle List III" (18810). Gives "Translated Parchment" (18961).
8. highpass/"Stanos Herkanor", hand "Translated Parchment" (18961). Gives "Sealed Box" (28057).
9. Hand "Sealed Box" (28057) to kithicor/"Adjutant D-Kan". Spawns "General V'ghera" (20205). Loot "General's Pouch" (28013) from "General V'ghera".
10. 6 alternative loot source(s) also yield General's Pouch (28013).
11. Loot "Fleshripper" (5411) from "Solusek kobold king" in `soldungb`.
12. Loot "Painbringer" (5410) from "Kobold Champion" in `soldungb`.
13. Loot "Mithril Two-Handed Sword" (5401) from "The Froglok King" in `gukbottom`.
14. Loot "Gigantic Zweihander" (5308) from "Karg IceBear" in `everfrost`.
15. qey2hh1/"Vilnius The Small", hand "Gigantic Zweihander" (5308) + "Mithril Two-Handed Sword" (5401) + "Painbringer" (5410) + "Fleshripper" (5411). Gives "Jagged Diamond Dagger" (7506).
16. Loot "Robe of the Ishva" (1357) from "Coercer Q'ioul" in `kithicor`.
17. Loot "Robe of the Ishva" (1357) from "Jinalis Andir" in `cauldron`.
18. Loot "Robe of the Ishva" (1357) from "The Ishva Mal" in `southkarana`.
19. Loot "Robe of the Kedge" (1253) from "Kubaria" (NPC 309002) in `chambersf`. Drop cache: 100% chance per kill.
20. Loot "Robe of the Oracle" (1354) from "Oracle of K'Arnon" in `oceanoftears`.
21. Loot "Robe of the Oracle" (1354) from "Oracle of K'Arnon" in `oot`.
22. Loot "Shining Metallic Robes" (1360) from "Yendar Starpyre" (NPC 56012) in `steamfont`. Drop cache: 100% chance per kill.
23. qey2hh1/"Vilnius The Small", hand "Robe of the Kedge" (1253) + "Robe of the Oracle" (1354) + "Robe of the Ishva" (1357) + "Shining Metallic Robes" (1360). Gives "Cazic Quill" (7505).
24. highpass/"Stanos Herkanor", hand "Cazic Quill" (7505) + "Jagged Diamond Dagger" (7506) + "General's Pouch" (28013). Gives "Ragebringer" (11057).

### "Fatestealer" (52347)

1. Unresolved cyclic prerequisite: `Fatestealer_gal` ==1.
2. Unresolved cyclic prerequisite: `Fatestealer_gal` ==1.
3. Unresolved cyclic prerequisite: `Fatestealer_mar` ==1.
4. Unresolved cyclic prerequisite: `Fatestealer_gal` ==1.
5. Unresolved cyclic prerequisite: `Fatestealer_mar` ==1.
6. Unresolved cyclic prerequisite: `Fatestealer_lyt` ==1.
7. Loot "Signed Agreement" (10246) from "Lythe Songbird" in `freeporteast`.
8. Loot "Signed Agreement" (10246) from "Lythe Songbird" in `freportw`.
9. overthere/"Inem R'Ker", hand "Signed Agreement" (10246). Sets `Fatestealer_lyt` to `1`.
10. Loot "Signed Agreement" (10239) from "Seana Marsinger" in `gfaydark`.
11. Loot "Signed Agreement" (52416) from "Stefan Marsinger" in `gfaydark`.
12. overthere/"Inem R'Ker", hand "Signed Agreement" (10239) + "Signed Agreement" (52416). Sets `Fatestealer_mar` to `1`.
13. Loot "Signed Agreement" (10243) from "Galdorin Visigothe" in `abysmal`.
14. overthere/"Inem R'Ker", hand "Signed Agreement" (10243). Sets `Fatestealer_gal` to `1`.
15. overthere/"Inem R'Ker", hand "Signed Agreement" (10243). Sets `Fatestealer_bard` to `1`.
16. Spawns "a Teir'Dal guardian" (186190) in `hateplaneb` on event death_complete:186114.
17. Loot "Stack of Pages" (52335) from "a Teir'Dal guardian".
18. 5 alternative loot source(s) also yield Stack of Pages (52335).
19. steamfont/"Yendar Starpyre", hand "Stack of Pages" (52335). Sets `Fatestealer_page` to `1`.
20. Spawns "A Furious Magma Guardian" (278123) in `soldungc` on event_signal.
21. Loot "Crystallized Shard of Doomfire" (21339) from "A Furious Magma Guardian".
22. 1 alternative loot source(s) also yield Crystallized Shard of Doomfire (21339).
23. Loot "Foul Doomfire Brimstone" (21342) from "A Pool Of Living Lava" (NPC 278043) in `soldungc`. Drop cache: 15.97% chance per kill.
24. Loot "Igneous Rock of Doomfire" (21340) from "Typhoeus" (NPC 278069) in `soldungc`. Drop cache: 35% chance per kill.
25. Loot "Pile of Doomfire Ash" (21341) from "a Taklasinai marauder" (NPC 278075) in `soldungc`. Drop cache: 35% chance per kill.
26. Hand "Crystallized Shard of Doomfire" (21339) + "Igneous Rock of Doomfire" (21340) + "Pile of Doomfire Ash" (21341) + "Foul Doomfire Brimstone" (21342) to soldungc/"The Firewatcher". Spawns "Culthor the Gatekeeper" (278005). Loot "Smoldering Embers of Solusek" (52346) from "Culthor the Gatekeeper".
27. nedaria/"Smith Dandi", hand "Smoldering Embers of Solusek" (52346). Sets `Fatestealer_forge` to `1`.
28. Spawns "a Teir'Dal guardian" (186190) in `hateplaneb` on event death_complete:186114.
29. Loot "Soulstone of Lanys" (52337) from "a Teir'Dal guardian".
30. 5 alternative loot source(s) also yield Soulstone of Lanys (52337).
31. nedaria/"Lirprin, Head Of Affairs", hand "Soulstone of Lanys" (52337). Requires `Fatestealer_bard` ==1. Requires `Fatestealer_page` ==1. Requires `Fatestealer_forge` ==1. Gives "Fatestealer" (52347).

### "Strongbox Half Full of Velixite" (52342)

1. **Broken:** nothing in the graph gives, loots, spawns, or combines Air-Tight Strongbox (52339).
2. No quest step gives Lump of Raw Alloy (52340). The dump lists it in iceclad.
3. Combine in "Air-Tight Strongbox" (52339): "Lump of Raw Alloy" (52340). Produces "Strongbox Full of Alloy" (52341). The combine does not fail.
4. iceclad/"Lookout Larithim", hand "Strongbox Full of Alloy" (52341). Gives "Strongbox Half Full of Velixite" (52342).

### "Singing Short Sword" (20542)

1. qey2hh1/"Konia Swiftfoot", say "Ready". Gives "Torch of Misty" (20532).
2. misty/"Fajio Knejo", hand "Torch of Misty" (20532). Gives "Torch of Ro" (20533).
3. southro/"Andad Filla", hand "Torch of Ro" (20533). Gives "Torch of Rathe" (20534).
4. lakerathe/"Misty Tekcihta", hand "Torch of Rathe" (20534). Gives "Proof of Speed" (20379).
5. qey2hh1/"Konia Swiftfoot", hand "Proof of Speed" (20379). Gives "Maestro's Symphony Page 24 Top" (20376).
6. southkarana/"Baenar Swiftsong", say "Doll". Gives "Solusek Mining Company Invoice" (20372).
7. soldunga/"Marfen Binkdirple", hand "Solusek Mining Company Invoice" (20372). Gives "Mechanical Doll" (20370).
8. unrest/"Serra", hand "Mechanical Doll" (20370). Gives "Note for Baenar" (20371).
9. southkarana/"Baenar Swiftsong", hand "Note for Baenar" (20371). Gives "Note to Maligar" (20368).
10. Hand "Note to Maligar" (20368) to qey2hh1/"Maligar". Spawns "Maligars Enraged Doppleganger" (12173). Loot "Maligar's Head" (20367) from "Maligars Enraged Doppleganger".
11. southkarana/"Baenar Swiftsong", hand "Maligar's Head" (20367). Gives "Mahlin's Mystical Bongos" (20366).
12. qey2hh1/"Konia Swiftfoot", hand "Mahlin's Mystical Bongos" (20366). Gives "Maestro's Symphony Page 24 Bottom" (20383).
13. Loot "Chromodrac Gut" (20527) from "Eldrig the Old" in `skyfire`.
14. Loot "Red Wurm Gut" (20528) from "Nezekezena" in `burningwood`.
15. Loot "Onyx Drake Gut" (20529) from "Blackwing".
16. Loot "Onyx Drake Gut" (20529) from "Blackwing" in `rathemtn`.
17. southkarana/"Kelkim Menkia", hand "Chromodrac Gut" (20527) + "Red Wurm Gut" (20528) + "Onyx Drake Gut" (20529). Gives "Maestro's Symphony Page 25" (20377).
18. Loot "Alluring Horn" (20530) from "Quag Maelstrom" in `oceanoftears`.
19. Loot "Alluring Horn" (20530) from "Quag Maelstrom" in `oot`.
20. butcher/"Vedico Windwisper", hand "Alluring Horn" (20530). Gives "Note to Forpar Fizfla" (20378).
21. steamfont/"Forpar Fizfla", hand "Note to Forpar Fizfla" (20378). Gives "Forpar's Note to Himself" (20380).
22. Loot "Kedge Backbone" (20524) from "Phinigel Autropos" in `kedge`.
23. Loot "Petrified Werewolf Skull" (20525) from "The Fabled Drolvarg Warlord".
24. Loot "Petrified Werewolf Skull" (20525) from "a Drolvarg warlord" in `karnor`.
25. Loot "Amygdalan Tendril" (5520) from "Amygdalan warrior" (NPC 72015) in `fearplane`. Drop cache: 8.14% chance per kill.
26. steamfont/"Forpar Fizfla", hand "Amygdalan Tendril" (5520) + "Forpar's Note to Himself" (20380) + "Kedge Backbone" (20524) + "Petrified Werewolf Skull" (20525). Gives "Mystical Lute Head" (20535).
27. Loot "White Dragon Scales" (11602) from "Gorenaire" in `dreadlands`.
28. Loot "White Dragon Scales" (11602) from "Lady Vox" in `permafrost`.
29. Loot "White Dragon Scales" (11602) from "The Fabled Gorenaire".
30. Loot "Red Dragon Scales" (11622) from "Echo of Nortlav" in `hole`.
31. Loot "Red Dragon Scales" (11622) from "Lord Nagafen" in `soldungb`.
32. Loot "Red Dragon Scales" (11622) from "Melalafen" in `westwastes`.
33. Loot "Red Dragon Scales" (11622) from "Talendor" in `skyfire`.
34. kaladimb/"Jeet", say "Collect The Gnome Profit". Gives "Scrubber Key" (12164).
35. akanon/"Clockwork Scrubber", hand "Scrubber Key" (12164). Gives "Gnome Take" (12167).
36. kaladimb/"Jeet", hand "Gnome Take" (12167). Gives "Small Piece of Ore" (10500).
37. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
38. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `steamfont`.
39. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `tox`.
40. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `toxxulia`.
41. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
42. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). The combine does not fail.
43. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
44. Combine in Forge (17): "Small Piece of Ore" (10500), "Water Flask" (13006). Produces "Metal Bits" (16905) x2. Requires Blacksmithing, trivial 18.
45. steamfont/"Forpar Fizfla", hand "White Dragon Scales" (11602) + "Red Dragon Scales" (11622) + "Metal Bits" (16905). Gives "Mystical Lute Body" (20536).
46. Kill sebilis/"An Undead Bard". Spawns "Trakanon" (89181).
47. Loot "Undead Dragongut Strings" (20526) from "Trakanon".
48. steamfont/"Forpar Fizfla", hand "Undead Dragongut Strings" (20526) + "Mystical Lute Head" (20535) + "Mystical Lute Body" (20536). Gives "Mystical Lute" (20538).
49. dreadlands/"Baldric Slezaf", hand "Maestro's Symphony Page 24 Top" (20376) + "Maestro's Symphony Page 25" (20377) + "Maestro's Symphony Page 24 Bottom" (20383) + "Mystical Lute" (20538). Gives "Singing Short Sword" (20542).

### "Wind Dragon Prism" (77618)

1. Loot "Dragorn Blood" (77639) from "A Dragorn Serf" (NPC 300018) in `wallofslaughter`. Drop cache: 9.52% chance per kill.
2. Summon "Enchanted Velium Bar" (22099) by casting "Enchant Velium", "Mass Enchant Velium", "Greater Mass Enchant Velium".
3. Summon "Cloudy Diamond of Air" (29989) by casting "Imbue Air".
4. Forage "Wind Dragon Crystal" (12783) in `skyfire`.
5. Combine in Jeweler's Kit (20): "Dragorn Blood" (77639), "Enchanted Velium Bar" (22099), "Cloudy Diamond of Air" (29989), "Wind Dragon Crystal" (12783). Produces "Wind Dragon Prism" (77618). Requires Jewelry Making. The combine does not fail.

### "Fire Dragon Prism" (77619)

1. Loot "Dragorn Blood" (77639) from "A Dragorn Serf" (NPC 300018) in `wallofslaughter`. Drop cache: 9.52% chance per kill.
2. Summon "Enchanted Velium Bar" (22099) by casting "Enchant Velium", "Mass Enchant Velium", "Greater Mass Enchant Velium".
3. Summon "Red Diamond of Fire" (29986) by casting "Imbue Fire".
4. Forage "Fire Dragon Crystal" (12487) in `skyfire`.
5. Combine in Jeweler's Kit (20): "Dragorn Blood" (77639), "Enchanted Velium Bar" (22099), "Red Diamond of Fire" (29986), "Fire Dragon Crystal" (12487). Produces "Fire Dragon Prism" (77619). Requires Jewelry Making. The combine does not fail.

### "Water Dragon Prism" (77620)

1. Loot "Dragorn Blood" (77639) from "A Dragorn Serf" (NPC 300018) in `wallofslaughter`. Drop cache: 9.52% chance per kill.
2. Summon "Enchanted Velium Bar" (22099) by casting "Enchant Velium", "Mass Enchant Velium", "Greater Mass Enchant Velium".
3. Summon "Aqua Diamond of Water" (29987) by casting "Imbue Water".
4. Forage "Ice Dragon Crystal" (12781) in `skyfire`.
5. Combine in Jeweler's Kit (20): "Dragorn Blood" (77639), "Enchanted Velium Bar" (22099), "Aqua Diamond of Water" (29987), "Ice Dragon Crystal" (12781). Produces "Water Dragon Prism" (77620). Requires Jewelry Making. The combine does not fail.

### "Earth Dragon Prism" (77621)

1. Loot "Dragorn Blood" (77639) from "A Dragorn Serf" (NPC 300018) in `wallofslaughter`. Drop cache: 9.52% chance per kill.
2. Summon "Enchanted Velium Bar" (22099) by casting "Enchant Velium", "Mass Enchant Velium", "Greater Mass Enchant Velium".
3. Summon "Brown Diamond of Earth" (29988) by casting "Imbue Earth".
4. Forage "Earth Dragon Crystal" (12782) in `skyfire`.
5. Combine in Jeweler's Kit (20): "Dragorn Blood" (77639), "Enchanted Velium Bar" (22099), "Brown Diamond of Earth" (29988), "Earth Dragon Crystal" (12782). Produces "Earth Dragon Prism" (77621). Requires Jewelry Making. The combine does not fail.

### "Swamp Dragon Prism" (77622)

1. Loot "Dragorn Blood" (77639) from "A Dragorn Serf" (NPC 300018) in `wallofslaughter`. Drop cache: 9.52% chance per kill.
2. Summon "Enchanted Velium Bar" (22099) by casting "Enchant Velium", "Mass Enchant Velium", "Greater Mass Enchant Velium".
3. Summon "Green Diamond of Disease" (30118) by casting "Imbue Disease".
4. Spawns "A Swamp Dragon" (83249) in `swampofnohope` on event_hp.
5. Loot "Swamp Dragon Crystal" (77614) from "A Swamp Dragon".
6. Combine in Jeweler's Kit (20): "Dragorn Blood" (77639), "Enchanted Velium Bar" (22099), "Green Diamond of Disease" (30118), "Swamp Dragon Crystal" (77614). Produces "Swamp Dragon Prism" (77622). Requires Jewelry Making. The combine does not fail.

### "Plains Dragon Prism" (77623)

1. Loot "Dragorn Blood" (77639) from "A Dragorn Serf" (NPC 300018) in `wallofslaughter`. Drop cache: 9.52% chance per kill.
2. Summon "Enchanted Velium Bar" (22099) by casting "Enchant Velium", "Mass Enchant Velium", "Greater Mass Enchant Velium".
3. Summon "Gray Diamond of Storms" (29991) by casting "Imbue Storm".
4. Spawns "A Plains Dragon" (13130) in `northkarana` on event_hp.
5. Loot "Plains Dragon Crystal" (77615) from "A Plains Dragon".
6. Combine in Jeweler's Kit (20): "Dragorn Blood" (77639), "Enchanted Velium Bar" (22099), "Gray Diamond of Storms" (29991), "Plains Dragon Crystal" (77615). Produces "Plains Dragon Prism" (77623). Requires Jewelry Making. The combine does not fail.

### "Forest Dragon Prism" (77624)

1. Loot "Dragorn Blood" (77639) from "A Dragorn Serf" (NPC 300018) in `wallofslaughter`. Drop cache: 9.52% chance per kill.
2. Summon "Enchanted Velium Bar" (22099) by casting "Enchant Velium", "Mass Enchant Velium", "Greater Mass Enchant Velium".
3. Summon "Yellow Diamond of Valor" (30489) by casting "Imbue Valor".
4. Spawns "A Forest Dragon" (181224) in `jaggedpine` on event_hp.
5. Loot "Forest Dragon Crystal" (77616) from "A Forest Dragon".
6. Combine in Jeweler's Kit (20): "Dragorn Blood" (77639), "Enchanted Velium Bar" (22099), "Yellow Diamond of Valor" (30489), "Forest Dragon Crystal" (77616). Produces "Forest Dragon Prism" (77624). Requires Jewelry Making. The combine does not fail.

### "Mountain Dragon Prism" (77625)

1. Loot "Dragorn Blood" (77639) from "A Dragorn Serf" (NPC 300018) in `wallofslaughter`. Drop cache: 9.52% chance per kill.
2. Summon "Enchanted Velium Bar" (22099) by casting "Enchant Velium", "Mass Enchant Velium", "Greater Mass Enchant Velium".
3. Summon "White Diamond of Justice" (29494) by casting "Imbue Justice".
4. Spawns "A Mountain Dragon" (100227) in `stonebrunt` on event_hp.
5. Loot "Mountain Dragon Crystal" (77617) from "A Mountain Dragon".
6. Combine in Jeweler's Kit (20): "Dragorn Blood" (77639), "Enchanted Velium Bar" (22099), "White Diamond of Justice" (29494), "Mountain Dragon Crystal" (77617). Produces "Mountain Dragon Prism" (77625). Requires Jewelry Making. The combine does not fail.

### "Draconic Prism" (77628)

1. Spawns "A Shadow Thief" (20292) in `kithicor` on event death_complete:20291.
2. Loot "Crest of Rizlona" (77626) from "A Shadow Thief".
3. Loot "Dragorn Blood" (77639) from "A Dragorn Serf" (NPC 300018) in `wallofslaughter`. Drop cache: 9.52% chance per kill.
4. Summon "Enchanted Velium Bar" (22099) by casting "Enchant Velium", "Mass Enchant Velium", "Greater Mass Enchant Velium".
5. Summon "Cloudy Diamond of Air" (29989) by casting "Imbue Air".
6. Forage "Wind Dragon Crystal" (12783) in `skyfire`.
7. Combine in Jeweler's Kit (20): "Dragorn Blood" (77639), "Enchanted Velium Bar" (22099), "Cloudy Diamond of Air" (29989), "Wind Dragon Crystal" (12783). Produces "Wind Dragon Prism" (77618). Requires Jewelry Making. The combine does not fail.
8. Summon "Red Diamond of Fire" (29986) by casting "Imbue Fire".
9. Forage "Fire Dragon Crystal" (12487) in `skyfire`.
10. Combine in Jeweler's Kit (20): "Dragorn Blood" (77639), "Enchanted Velium Bar" (22099), "Red Diamond of Fire" (29986), "Fire Dragon Crystal" (12487). Produces "Fire Dragon Prism" (77619). Requires Jewelry Making. The combine does not fail.
11. Summon "Aqua Diamond of Water" (29987) by casting "Imbue Water".
12. Forage "Ice Dragon Crystal" (12781) in `skyfire`.
13. Combine in Jeweler's Kit (20): "Dragorn Blood" (77639), "Enchanted Velium Bar" (22099), "Aqua Diamond of Water" (29987), "Ice Dragon Crystal" (12781). Produces "Water Dragon Prism" (77620). Requires Jewelry Making. The combine does not fail.
14. Summon "Brown Diamond of Earth" (29988) by casting "Imbue Earth".
15. Forage "Earth Dragon Crystal" (12782) in `skyfire`.
16. Combine in Jeweler's Kit (20): "Dragorn Blood" (77639), "Enchanted Velium Bar" (22099), "Brown Diamond of Earth" (29988), "Earth Dragon Crystal" (12782). Produces "Earth Dragon Prism" (77621). Requires Jewelry Making. The combine does not fail.
17. Summon "Green Diamond of Disease" (30118) by casting "Imbue Disease".
18. Spawns "A Swamp Dragon" (83249) in `swampofnohope` on event_hp.
19. Loot "Swamp Dragon Crystal" (77614) from "A Swamp Dragon".
20. Combine in Jeweler's Kit (20): "Dragorn Blood" (77639), "Enchanted Velium Bar" (22099), "Green Diamond of Disease" (30118), "Swamp Dragon Crystal" (77614). Produces "Swamp Dragon Prism" (77622). Requires Jewelry Making. The combine does not fail.
21. Summon "Gray Diamond of Storms" (29991) by casting "Imbue Storm".
22. Spawns "A Plains Dragon" (13130) in `northkarana` on event_hp.
23. Loot "Plains Dragon Crystal" (77615) from "A Plains Dragon".
24. Combine in Jeweler's Kit (20): "Dragorn Blood" (77639), "Enchanted Velium Bar" (22099), "Gray Diamond of Storms" (29991), "Plains Dragon Crystal" (77615). Produces "Plains Dragon Prism" (77623). Requires Jewelry Making. The combine does not fail.
25. Summon "Yellow Diamond of Valor" (30489) by casting "Imbue Valor".
26. Spawns "A Forest Dragon" (181224) in `jaggedpine` on event_hp.
27. Loot "Forest Dragon Crystal" (77616) from "A Forest Dragon".
28. Combine in Jeweler's Kit (20): "Dragorn Blood" (77639), "Enchanted Velium Bar" (22099), "Yellow Diamond of Valor" (30489), "Forest Dragon Crystal" (77616). Produces "Forest Dragon Prism" (77624). Requires Jewelry Making. The combine does not fail.
29. Summon "White Diamond of Justice" (29494) by casting "Imbue Justice".
30. Spawns "A Mountain Dragon" (100227) in `stonebrunt` on event_hp.
31. Loot "Mountain Dragon Crystal" (77617) from "A Mountain Dragon".
32. Combine in Jeweler's Kit (20): "Dragorn Blood" (77639), "Enchanted Velium Bar" (22099), "White Diamond of Justice" (29494), "Mountain Dragon Crystal" (77617). Produces "Mountain Dragon Prism" (77625). Requires Jewelry Making. The combine does not fail.
33. Combine in "Crest of Rizlona" (77626): "Wind Dragon Prism" (77618), "Fire Dragon Prism" (77619), "Water Dragon Prism" (77620), "Earth Dragon Prism" (77621), "Swamp Dragon Prism" (77622), "Plains Dragon Prism" (77623), "Forest Dragon Prism" (77624), "Mountain Dragon Prism" (77625). Produces "Draconic Prism" (77628). The combine does not fail.

## `bardPQ`

Values written: 1, 2, 3, 4.

### 1. lantaric-dar — hand 77600+77600+77600

Zone: `wakening`.

Sets `bardPQ` to `1`.

- Turn in x1: Storm Giant Herald Head (77600).
In script order:

1. Sets `bardPQ` to `1`.


How the items are reached:

- Storm Giant Herald Head (77600)
  - Loot "Storm Giant Herald Head" (77600) from "A Giant Herald" in `wakening`.

### 2. lantaric-dar — hand 77601

Zone: `wakening`.

Sets `bardPQ` to `2`.

- Needs `bardPQ` ==1.
- Turn in x1: Kromzek Supply Orders (77601).
In script order:

1. Sets `bardPQ` to `2`.
2. Spawns Cristoc Bonethug (119182).
   - Loots Sealed Letter (77602).
3. Spawns a Bonethug mercenary (119183).


How the items are reached:

- Kromzek Supply Orders (77601)
  - Loot "Kromzek Supply Orders" (77601) from "A Giant Messenger" in `wakening`.

### 3. lantaric-dar — hand 77602

Zone: `wakening`.

Sets `bardPQ` to `3`.

- Needs `bardPQ` ==2.
- Turn in x1: Sealed Letter (77602).
In script order:

1. Sets `bardPQ` to `3`.


How the items are reached:

- Sealed Letter (77602)
  - Hand "Kromzek Supply Orders" (77601) to wakening/"Lantaric-Dar". Spawns "Cristoc Bonethug" (119182). Loot "Sealed Letter" (77602) from "Cristoc Bonethug".

### 4. vas thorel — hand 77603

Zone: `iceclad`.

Sets `bardPQ` to `4`.

- Needs `bardPQ` ==3.
- Turn in x1: Sealed Kromzek Scroll (77603).
In script order:

1. Sets `bardPQ` to `4`.


How the items are reached:

- Sealed Kromzek Scroll (77603)
  - Say "Lantaric" to iceclad/"Vas Thorel".
  - Spawns "Noble Oldencamp" (110123).
  - Loot "Sealed Kromzek Scroll" (77603) from "Noble Oldencamp".

### Steps on `bardPQ` that do not change it

- `iceclad` vas thorel, say lantaric needs `bardPQ` ==3.
  - Spawns Noble Oldencamp (110123).
  - Spawns Amilia Verisue (110128).
  - Spawns Nihilist Xeegarn (110127).
  - Spawns Puella Opalis (110126).
  - Spawns Locis V`Sek (110125).
  - Spawns a frost giant escort (110129).
  - Spawns a frost giant warrior (110130).
  - Loots Sealed Kromzek Scroll (77603).
  - Loots Amilia's Head (77605).
  - Loots Xeegarn's Head (77604).
  - Loots Puella's Head (77606).
  - Loots Locis' Head (77607).
- `wakening` lantaric-dar, hand 77604+77605+77606+77607 needs `bardPQ` ==4.
  - Sets `bard15` to `1`.
  - Turn in Xeegarn's Head (77604).
  - Turn in Amilia's Head (77605).
  - Turn in Puella's Head (77606).
  - Turn in Locis' Head (77607).

## `Fatestealer_bard`

Values written: 1.

### 1. inem r`ker — hand 10239+52416

Zone: `overthere`.

Sets `Fatestealer_bard` to `1`.

- Needs `Fatestealer` ==1.
- Needs `Fatestealer_gal` ==1.
- Needs `Fatestealer_mar` ==1.
- Needs `Fatestealer_lyt` ==1.
- Turn in x1: Signed Agreement (10239).
- Turn in x1: Signed Agreement (52416).
In script order:

1. Sets `Fatestealer_mar` to `1`.
2. Sets `Fatestealer_bard` to `1`.
3. Gives Notice to Cease and Desist (9590).


How the items are reached:

- Signed Agreement (10239)
  - Loot "Signed Agreement" (10239) from "Seana Marsinger" in `gfaydark`.
- Signed Agreement (52416)
  - Loot "Signed Agreement" (52416) from "Stefan Marsinger" in `gfaydark`.

Subquest `Fatestealer`:

#### `Fatestealer`

Values written: 1, 2, 3, 4.

##### 1. stanos herkanor — say hail

Zone: `highpass`.

> Ah, the pouch. This is the first step. The Circle has to be upset having this taken right out from under them. That speaks well of the person who did the tak...

Sets `Fatestealer` to `1`.

- Needs Ragebringer (11057).
In script order:

1. Sets `Fatestealer` to `1`.


How the items are reached:

- Ragebringer (11057)
  - Prerequisite: "Ragebringer" (11057). See section 0.

Alternative or repeat transition to `Fatestealer` = `1` (not an additional required stage).

##### 1. stanos herkanor — say hail

Zone: `highpasshold`.

> Ah, the pouch. This is the first step. The Circle has to be upset having this taken right out from under them. That speaks well of the person who did the tak...

Sets `Fatestealer` to `1`.

- Needs Ragebringer (11057).
In script order:

1. Sets `Fatestealer` to `1`.


How the items are reached:

- Ragebringer (11057)
  - Prerequisite: "Ragebringer" (11057). See section 0.

##### 2. lirprin, head of affairs — hand 52337

Zone: `nedaria`.

Sets `Fatestealer` to `2`.

- Needs `Fatestealer_bard` ==1.
- Needs `Fatestealer_page` ==1.
- Needs `Fatestealer_forge` ==1.
- Turn in x1: Soulstone of Lanys (52337).
In script order:

1. Sets `Fatestealer` to `2`.
2. Gives Fatestealer (52347).


How the items are reached:

- Soulstone of Lanys (52337)
  - Spawns "a Teir'Dal guardian" (186190) in `hateplaneb` on event death_complete:186114.
  - Loot "Soulstone of Lanys" (52337) from "a Teir'Dal guardian".
  - 5 alternative loot source(s) also yield Soulstone of Lanys (52337).

This step also depends on `Fatestealer_bard`, shown above.

Subquest `Fatestealer_page`:

#### `Fatestealer_page`

Values written: 1.

###### 1. yendar starpyre — hand 52335

Zones: `steamfont`, `steamfontmts`.

Sets `Fatestealer_page` to `1`.

- Turn in x1: Stack of Pages (52335).
In script order:

1. Sets `Fatestealer_page` to `1`.


How the items are reached:

- Stack of Pages (52335)
  - Spawns "a Teir'Dal guardian" (186190) in `hateplaneb` on event death_complete:186114.
  - Loot "Stack of Pages" (52335) from "a Teir'Dal guardian".
  - 5 alternative loot source(s) also yield Stack of Pages (52335).

###### Steps on `Fatestealer_page` that do not change it

- `nedaria` lirprin, head of affairs, hand 52337 needs `Fatestealer_page` ==1.
  - Sets `Fatestealer` to `2`.
  - Turn in Soulstone of Lanys (52337).
  - Gives Fatestealer (52347).
- `nedaria` smith dandi, say hail needs `Fatestealer_page` ==1.
  - Sets `Fatestealer_culth` to `1`.

Subquest `Fatestealer_forge`:

#### `Fatestealer_forge`

Values written: 1.

###### 1. smith dandi — hand 52346

Zone: `nedaria`.

Sets `Fatestealer_forge` to `1`.

- Needs `Fatestealer_bard` ==1.
- Turn in x1: Smoldering Embers of Solusek (52346).
In script order:

1. Sets `Fatestealer_forge` to `1`.


How the items are reached:

- Smoldering Embers of Solusek (52346)
  - Hand "Crystallized Shard of Doomfire" (21339) + "Igneous Rock of Doomfire" (21340) + "Pile of Doomfire Ash" (21341) + "Foul Doomfire Brimstone" (21342) to soldungc/"The Firewatcher". Spawns "Culthor the Gatekeeper" (278005). Loot "Smoldering Embers of Solusek" (52346) from "Culthor the Gatekeeper".

This step also depends on `Fatestealer_bard`, shown above.

###### Steps on `Fatestealer_forge` that do not change it

- `nedaria` lirprin, head of affairs, hand 52337 needs `Fatestealer_forge` ==1.
  - Sets `Fatestealer` to `2`.
  - Turn in Soulstone of Lanys (52337).
  - Gives Fatestealer (52347).
- `nedaria` smith dandi, say hail needs `Fatestealer_forge` ==1.
  - Sets `Fatestealer_culth` to `1`.
- `steamfont` findleznax grimblewimbus, say help needs `Fatestealer_forge` ==1.
  - Spawns a decomposing body (448203).
- `steamfont` player, on loot needs `Fatestealer_forge` ==1.
  - Sets `rogue_steam_chest` to `1`.
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
- `steamfontmts` findleznax grimblewimbus, say help needs `Fatestealer_forge` ==1.
  - Spawns a decomposing body (448203).
- `steamfontmts` player, on loot needs `Fatestealer_forge` ==1.
  - Sets `rogue_steam_chest` to `1`.
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

##### 3. lirprin, head of affairs — say hail

Zone: `nedaria`.

> I

Sets `Fatestealer` to `3`.

- Needs `Fatestealer` ==1.
- Needs `Fatestealer_bard` ==1.
- Needs Fatestealer (52347).
In script order:

1. Sets `Fatestealer` to `3`.


How the items are reached:

- Fatestealer (52347)
  - Prerequisite: "Fatestealer" (52347). See section 0.

This step also depends on `Fatestealer_bard`, shown above.

##### 4. lirprin, head of affairs — hand 21346+47100+52342+52347

Zone: `nedaria`.

Sets `Fatestealer` to `4`.

- Needs `Fatestealer` ==3.
- Turn in x1: Globe of Discordant Energy (47100).
- Turn in x1: Strongbox Half Full of Velixite (52342).
- Turn in x1: Wren's Fatestealer (21346).
- Turn in x1: Fatestealer (52347).
In script order:

1. Sets `Fatestealer` to `4`.
2. Gives Nightshade, Blade of Entropy (52348).


How the items are reached:

- Globe of Discordant Energy (47100)
  - Say "Check Lorb" to anguish/"Zone Status".
  - Spawns "Orb of Discordant Energy" (317087).
  - Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy".
  - 4 alternative loot source(s) also yield Globe of Discordant Energy (47100).
- Strongbox Half Full of Velixite (52342)
  - Prerequisite: "Strongbox Half Full of Velixite" (52342). See section 0.
- Wren's Fatestealer (21346)
  - No quest step gives Wren's Fatestealer (21346). The dump lists it in dranik.
- Fatestealer (52347)
  - Prerequisite: "Fatestealer" (52347). See section 0.

##### Steps on `Fatestealer` that do not change it

- `bloodfields` caller donivin, hand 52349+52350+52351+52352 needs `Fatestealer` ==3.
  - Sets `rog_bf_trigger` to `1`.
  - Spawns a reclusive girplan (301033).
  - Loots Cloth Cap (1001).
  - Loots Peridot (10028).
  - Loots Diamond (10037).
  - Loots Jacinth (10053).
  - Loots Sunshard Ore (33792).
  - Loots Lucidem (35084).
  - Loots Versluierd Fungus (35087).
  - Loots Raw Shimmering Nihilite (58068).
  - Turn in Polished Bone Horn (52349).
  - Turn in Brass Mouthpiece (52350).
  - Turn in Bucket Mute (52351).
  - Turn in Thin Leather Straps (52352).
- `bloodfields` keetra the lost, say lirprin sent me needs `Fatestealer` ==3.
  - Sets `rogue_epic_keetra` to `1`.
- `dranik` daignal the revered, on kill needs `Fatestealer` ==3.
  - Spawns Wren Simsy (336253).
  - Loots Fine Steel Dagger (7350).
  - Loots Wren's Fatestealer (21346).
  - Loots Versluierd Fungus (35087).
- `firiona` vorla diensk, say come in needs `Fatestealer` ==1.
  - Gives Occluded Sun Pendant (52009).
- `halas` elyn connoy, hand 52353 needs `Fatestealer` ==1.
  - Sets `Fatestealer_hl` to `1`.
  - Sets `Fatestealer_gem` to `1`.
  - Turn in Pouch of Gems (52353).
- `halas` elyn connoy, hand 9807 needs `Fatestealer` ==1.
  - Sets `Fatestealer_hl` to `1`.
  - Turn in Satchel of Deceiver's Garb (9807).
- `hateplaneb` player, on enter needs `Fatestealer` ==1.
  - Sets `hpb_zone_emote` to `1`.
- `hateplaneb` player, on loot needs `Fatestealer` ==1.
  - Sets `rogue_hate_chest` to `1`.
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
- `iceclad` lookout larithim, say what happened then needs `Fatestealer` ==3.
  - Sets `rogue_epic_iceclad` to `1`.
  - Spawns Polar Kraken (110131).
  - Loots Lump of Raw Alloy (52340).
  - Gives Air-Tight Strongbox (52339).
- `iceclad` player, on loot needs `Fatestealer` ==3.
  - Sets `rogue_chest_ice` to `1`.
  - Spawns a chest (epic 2.0) (893).
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
- `kaladimb` diggins, hand 52353 needs `Fatestealer` ==1.
  - Sets `Fatestealer_nk` to `1`.
  - Sets `Fatestealer_gem` to `1`.
  - Turn in Pouch of Gems (52353).
- `kaladimb` diggins, hand 9813 needs `Fatestealer` ==1.
  - Sets `Fatestealer_nk` to `1`.
  - Turn in Satchel of Smithed Relics (9813).
- `kaladimb` diggins, say small job needs `Fatestealer` ==1.
  - Gives Collection Satchel (8775).
  - Gives Test of Smithing (52331).
- `mirb` durgin skell, say lirprin sent me needs `Fatestealer` ==3.
  - Sets `rogue_epic_durgin` to `1`.
  - Sets `rogue_chest_mira` to `1`.
  - Spawns a chest (893).
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
- `nedaria` smith dandi, say hail needs `Fatestealer` ==3.
  - Sets `Fatestealer_culth` to `1`.
- `oasis` a wayward kiraikuei, hand 9599 needs `Fatestealer` ==1.
  - Turn in Pulsating Blue Metal Sphere (9599).
  - Gives Pulsating Blue Metal Sphere (9599).
- `overthere` inem r`ker, say change their tune needs `Fatestealer` ==1.
  - Gives Notice to Cease and Desist (9590).
- `overthere` inem r`ker, hand 10239+52416 needs `Fatestealer` ==1.
  - Sets `Fatestealer_mar` to `1`.
  - Sets `Fatestealer_bard` to `1`.
  - Turn in Signed Agreement (10239).
  - Turn in Signed Agreement (52416).
  - Gives Notice to Cease and Desist (9590).
- `overthere` inem r`ker, hand 10243 needs `Fatestealer` ==1.
  - Sets `Fatestealer_gal` to `1`.
  - Sets `Fatestealer_bard` to `1`.
  - Turn in Signed Agreement (10243).
  - Gives Notice to Cease and Desist (9590).
- `overthere` inem r`ker, hand 10246 needs `Fatestealer` ==1.
  - Sets `Fatestealer_lyt` to `1`.
  - Sets `Fatestealer_bard` to `1`.
  - Turn in Signed Agreement (10246).
  - Gives Notice to Cease and Desist (9590).
- `paludal` arly golyeck, hand 52353 needs `Fatestealer` ==1.
  - Sets `Fatestealer_pl` to `1`.
  - Sets `Fatestealer_gem` to `1`.
  - Turn in Pouch of Gems (52353).
- `paludal` arly golyeck, hand 9810 needs `Fatestealer` ==1.
  - Sets `Fatestealer_pl` to `1`.
  - Turn in Satchel of Poisons (9810).
- `rivervale` lendel deeppockets, hand 13588 needs `Fatestealer` ==1.
  - Sets `Fatestealer_rv` to `1`.
  - Turn in Gubbin's Approval Letter (13588).
- `rivervale` lendel deeppockets, hand 52353 needs `Fatestealer` ==1.
  - Sets `Fatestealer_rv` to `1`.
  - Sets `Fatestealer_gem` to `1`.
  - Turn in Pouch of Gems (52353).
- `rivervale` lendel deeppockets, say small job needs `Fatestealer` ==1.
  - Gives Jumjum Twist Recipe (52333).
- `sharvahl` master taruun rakutah, hand 52353 needs `Fatestealer` ==1.
  - Sets `Fatestealer_sv` to `1`.
  - Sets `Fatestealer_gem` to `1`.
  - Turn in Pouch of Gems (52353).
- `sharvahl` master taruun rakutah, hand 9491 needs `Fatestealer` ==1.
  - Sets `Fatestealer_sv` to `1`.
  - Turn in King's Feast (9491).
- `sharvahl` master taruun rakutah, say small task needs `Fatestealer` ==1.
  - Gives King's Feast Request (52334).

Subquest `Fatestealer_gal`:

#### `Fatestealer_gal`

Values written: 1.

##### 1. inem r`ker — hand 10243

Zone: `overthere`.

Sets `Fatestealer_gal` to `1`.

- Needs `Fatestealer` ==1.
- Needs `Fatestealer_gal` ==1.
- Needs `Fatestealer_mar` ==1.
- Needs `Fatestealer_lyt` ==1.
- Turn in x1: Signed Agreement (10243).
In script order:

1. Sets `Fatestealer_gal` to `1`.
2. Sets `Fatestealer_bard` to `1`.
3. Gives Notice to Cease and Desist (9590).


How the items are reached:

- Signed Agreement (10243)
  - Loot "Signed Agreement" (10243) from "Galdorin Visigothe" in `abysmal`.

This step also depends on `Fatestealer`, shown above.

Subquest `Fatestealer_mar`:

#### `Fatestealer_mar`

Values written: 1.

###### 1. inem r`ker — hand 10239+52416

Zone: `overthere`.

Sets `Fatestealer_mar` to `1`.

- Needs `Fatestealer` ==1.
- Needs `Fatestealer_gal` ==1.
- Needs `Fatestealer_mar` ==1.
- Needs `Fatestealer_lyt` ==1.
- Turn in x1: Signed Agreement (10239).
- Turn in x1: Signed Agreement (52416).
In script order:

1. Sets `Fatestealer_mar` to `1`.
2. Sets `Fatestealer_bard` to `1`.
3. Gives Notice to Cease and Desist (9590).


How the items are reached:

- Signed Agreement (10239)
  - Loot "Signed Agreement" (10239) from "Seana Marsinger" in `gfaydark`.
- Signed Agreement (52416)
  - Loot "Signed Agreement" (52416) from "Stefan Marsinger" in `gfaydark`.

This step also depends on `Fatestealer`, shown above.

This step also depends on `Fatestealer_gal`, shown above.

Subquest `Fatestealer_lyt`:

#### `Fatestealer_lyt`

Values written: 1.

###### 1. inem r`ker — hand 10246

Zone: `overthere`.

Sets `Fatestealer_lyt` to `1`.

- Needs `Fatestealer` ==1.
- Needs `Fatestealer_gal` ==1.
- Needs `Fatestealer_mar` ==1.
- Needs `Fatestealer_lyt` ==1.
- Turn in x1: Signed Agreement (10246).
In script order:

1. Sets `Fatestealer_lyt` to `1`.
2. Sets `Fatestealer_bard` to `1`.
3. Gives Notice to Cease and Desist (9590).


How the items are reached:

- Signed Agreement (10246)
  - Loot "Signed Agreement" (10246) from "Lythe Songbird" in `freeporteast`.
  - Loot "Signed Agreement" (10246) from "Lythe Songbird" in `freportw`.

This step also depends on `Fatestealer`, shown above.

This step also depends on `Fatestealer_gal`, shown above.

This step also depends on `Fatestealer_mar`, shown above.

###### Steps on `Fatestealer_lyt` that do not change it

- `overthere` inem r`ker, hand 10239+52416 needs `Fatestealer_lyt` ==1.
  - Sets `Fatestealer_mar` to `1`.
  - Sets `Fatestealer_bard` to `1`.
  - Turn in Signed Agreement (10239).
  - Turn in Signed Agreement (52416).
  - Gives Notice to Cease and Desist (9590).
- `overthere` inem r`ker, hand 10243 needs `Fatestealer_lyt` ==1.
  - Sets `Fatestealer_gal` to `1`.
  - Sets `Fatestealer_bard` to `1`.
  - Turn in Signed Agreement (10243).
  - Gives Notice to Cease and Desist (9590).

###### Steps on `Fatestealer_mar` that do not change it

- `overthere` inem r`ker, hand 10243 needs `Fatestealer_mar` ==1.
  - Sets `Fatestealer_gal` to `1`.
  - Sets `Fatestealer_bard` to `1`.
  - Turn in Signed Agreement (10243).
  - Gives Notice to Cease and Desist (9590).
- `overthere` inem r`ker, hand 10246 needs `Fatestealer_mar` ==1.
  - Sets `Fatestealer_lyt` to `1`.
  - Sets `Fatestealer_bard` to `1`.
  - Turn in Signed Agreement (10246).
  - Gives Notice to Cease and Desist (9590).

This step also depends on `Fatestealer_lyt`, shown above.

##### Steps on `Fatestealer_gal` that do not change it

- `overthere` inem r`ker, hand 10239+52416 needs `Fatestealer_gal` ==1.
  - Sets `Fatestealer_mar` to `1`.
  - Sets `Fatestealer_bard` to `1`.
  - Turn in Signed Agreement (10239).
  - Turn in Signed Agreement (52416).
  - Gives Notice to Cease and Desist (9590).
- `overthere` inem r`ker, hand 10246 needs `Fatestealer_gal` ==1.
  - Sets `Fatestealer_lyt` to `1`.
  - Sets `Fatestealer_bard` to `1`.
  - Turn in Signed Agreement (10246).
  - Gives Notice to Cease and Desist (9590).

This step also depends on `Fatestealer_mar`, shown above.

This step also depends on `Fatestealer_lyt`, shown above.

Alternative or repeat transition to `Fatestealer_bard` = `1` (not an additional required stage).

### 1. inem r`ker — hand 10243

Zone: `overthere`.

Sets `Fatestealer_bard` to `1`.

- Needs `Fatestealer` ==1.
- Needs `Fatestealer_gal` ==1.
- Needs `Fatestealer_mar` ==1.
- Needs `Fatestealer_lyt` ==1.
- Turn in x1: Signed Agreement (10243).
In script order:

1. Sets `Fatestealer_gal` to `1`.
2. Sets `Fatestealer_bard` to `1`.
3. Gives Notice to Cease and Desist (9590).


How the items are reached:

- Signed Agreement (10243)
  - Loot "Signed Agreement" (10243) from "Galdorin Visigothe" in `abysmal`.

This step also depends on `Fatestealer`, shown above.

This step also depends on `Fatestealer_gal`, shown above.

This step also depends on `Fatestealer_mar`, shown above.

This step also depends on `Fatestealer_lyt`, shown above.

Alternative or repeat transition to `Fatestealer_bard` = `1` (not an additional required stage).

### 1. inem r`ker — hand 10246

Zone: `overthere`.

Sets `Fatestealer_bard` to `1`.

- Needs `Fatestealer` ==1.
- Needs `Fatestealer_gal` ==1.
- Needs `Fatestealer_mar` ==1.
- Needs `Fatestealer_lyt` ==1.
- Turn in x1: Signed Agreement (10246).
In script order:

1. Sets `Fatestealer_lyt` to `1`.
2. Sets `Fatestealer_bard` to `1`.
3. Gives Notice to Cease and Desist (9590).


How the items are reached:

- Signed Agreement (10246)
  - Loot "Signed Agreement" (10246) from "Lythe Songbird" in `freeporteast`.
  - Loot "Signed Agreement" (10246) from "Lythe Songbird" in `freportw`.

This step also depends on `Fatestealer`, shown above.

This step also depends on `Fatestealer_gal`, shown above.

This step also depends on `Fatestealer_mar`, shown above.

This step also depends on `Fatestealer_lyt`, shown above.

### Steps on `Fatestealer_bard` that do not change it

- `nedaria` lirprin, head of affairs, say hail needs `Fatestealer_bard` ==1.
  - Sets `Fatestealer` to `3`.
- `nedaria` lirprin, head of affairs, hand 52337 needs `Fatestealer_bard` ==1.
  - Sets `Fatestealer` to `2`.
  - Turn in Soulstone of Lanys (52337).
  - Gives Fatestealer (52347).
- `nedaria` smith dandi, say hail needs `Fatestealer_bard` ==1.
  - Sets `Fatestealer_culth` to `1`.
- `nedaria` smith dandi, hand 52346 needs `Fatestealer_bard` ==1.
  - Sets `Fatestealer_forge` to `1`.
  - Turn in Smoldering Embers of Solusek (52346).

## `bard15`

Values written: 1, 2, 3, 4, 5, 6.

### 1. lantaric-dar — say baldric slezaf

Zone: `wakening`.

Sets `bard15` to `1`.

- Needs Singing Short Sword (20542).
- Needs `bard15` unset.
In script order:

1. Sets `bard15` to `1`.


How the items are reached:

- Singing Short Sword (20542)
  - Prerequisite: "Singing Short Sword" (20542). See section 0.

Alternative or repeat transition to `bard15` = `1` (not an additional required stage).

### 1. lantaric-dar — hand 77604+77605+77606+77607

Zone: `wakening`.

Sets `bard15` to `1`.

- Needs `bardPQ` ==4.
- Turn in x1: Xeegarn's Head (77604).
- Turn in x1: Amilia's Head (77605).
- Turn in x1: Puella's Head (77606).
- Turn in x1: Locis' Head (77607).
In script order:

1. Sets `bard15` to `1`.


How the items are reached:

- Xeegarn's Head (77604)
  - Say "Lantaric" to iceclad/"Vas Thorel".
  - Spawns "Nihilist Xeegarn" (110127).
  - Loot "Xeegarn's Head" (77604) from "Nihilist Xeegarn".
- Amilia's Head (77605)
  - Say "Lantaric" to iceclad/"Vas Thorel".
  - Spawns "Amilia Verisue" (110128).
  - Loot "Amilia's Head" (77605) from "Amilia Verisue".
- Puella's Head (77606)
  - Say "Lantaric" to iceclad/"Vas Thorel".
  - Spawns "Puella Opalis" (110126).
  - Loot "Puella's Head" (77606) from "Puella Opalis".
- Locis' Head (77607)
  - Say "Lantaric" to iceclad/"Vas Thorel".
  - Spawns "Locis V'Sek" (110125).
  - Loot "Locis' Head" (77607) from "Locis V'Sek".

This step also depends on `bardPQ`, shown above.

### 2. lantaric-dar — hand 77608

Zone: `wakening`.

Sets `bard15` to `2`.

- Needs `bard15` ==1.
- Turn in x1: Cracked Dragon Bone (77608).
In script order:

1. Sets `bard15` to `2`.
2. Gives Cracked Dragon Bone (77608).


How the items are reached:

- Cracked Dragon Bone (77608)
  - Kill necropolis/"Excavator Quellin". Spawns "Tarn Macklin" (123164).
  - Loot "Cracked Dragon Bone" (77608) from "Tarn Macklin".

### 3. lantaric-dar — hand 77612

Zone: `wakening`.

Sets `bard15` to `3`.

- Needs `bard15` ==2.
- Turn in x1: Blackened Dragon Bone (77612).
In script order:

1. Sets `bard15` to `3`.


How the items are reached:

- Blackened Dragon Bone (77612)
  - Spawns "Vesthon's Draconic Abomination" (123171) in `necropolis` on event_hp.
  - Loot "Blackened Dragon Bone" (77612) from "Vesthon's Draconic Abomination".

### 4. lantaric-dar — hand 77613

Zone: `wakening`.

Sets `bard15` to `4`.

- Needs `bard15` ==3.
- Turn in x1: Dark Orb (77613).
In script order:

1. Sets `bard15` to `4`.
2. Gives Dark Orb (77613).


How the items are reached:

- Dark Orb (77613)
  - Spawns "Needs Heading Validation" (123189) in `necropolis` on event death_complete:123173.
  - Loot "Dark Orb" (77613) from "Needs Heading Validation".

### 5. walthin fireweaver — say hail

Zone: `soltemple`.

> Good day to you! I am Walthin Fireweaver of the League of Antonican Bards. My friend Cryssia and I are here while we deal in [

Sets `bard15` to `5`.

- Needs Wind Dragon Prism (77618).
- Needs Fire Dragon Prism (77619).
- Needs Water Dragon Prism (77620).
- Needs Earth Dragon Prism (77621).
- Needs Swamp Dragon Prism (77622).
- Needs Plains Dragon Prism (77623).
- Needs Forest Dragon Prism (77624).
- Needs Mountain Dragon Prism (77625).
- Needs `bard15` ==4.
In script order:

1. Sets `bard15` to `5`.


How the items are reached:

- Wind Dragon Prism (77618)
  - Prerequisite: "Wind Dragon Prism" (77618). See section 0.
- Fire Dragon Prism (77619)
  - Prerequisite: "Fire Dragon Prism" (77619). See section 0.
- Water Dragon Prism (77620)
  - Prerequisite: "Water Dragon Prism" (77620). See section 0.
- Earth Dragon Prism (77621)
  - Prerequisite: "Earth Dragon Prism" (77621). See section 0.
- Swamp Dragon Prism (77622)
  - Prerequisite: "Swamp Dragon Prism" (77622). See section 0.
- Plains Dragon Prism (77623)
  - Prerequisite: "Plains Dragon Prism" (77623). See section 0.
- Forest Dragon Prism (77624)
  - Prerequisite: "Forest Dragon Prism" (77624). See section 0.
- Mountain Dragon Prism (77625)
  - Prerequisite: "Mountain Dragon Prism" (77625). See section 0.

### 6. global player — combine recipe 19882

Zone: `global`.

Sets `bard15` to `6`.

In script order:

1. Sets `bard15` to `6`.


Combine:

- `recipe:19882` is combined in Rusted Bile Etched Blade (77630).
  - Hand "Vhalen's Necklace" (77629) to potorment/"A Bruised Woman". Spawns "Metala Von Korach" (207084). Loot "Rusted Bile Etched Blade" (77630) from "Metala Von Korach".
  - Put in x1: Draconic Prism (77628).
    - Prerequisite: "Draconic Prism" (77628). See section 0.
  - Produces Prismatic Dragon Blade (77631).
  - The combine does not fail.

### Steps on `bard15` that do not change it

- `kithicor` player, on enter needs `bard15` ==5.
  - Spawns a cloaked figure (20290).
  - Spawns Blackened Treant (20299).
- `necropolis` player, on enter needs `bard15` ==2.
  - Spawns Hsagra`s Shade (123172).
  - Spawns he will spawn the rest (123173).
- `necropolis` player, on enter needs `bard15` set.
  - Spawns Hsagra`s Shade (123172).
  - Spawns he will spawn the rest (123173).
- `necropolis` player, on loot needs `bard15` set.
  - Sets `bard15_dracchest` to `1`.
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
- `potorment` a bruised woman, hand 77629 needs `bard15` ==5.
  - Spawns Metala Von Korach (207084).
  - Loots Rusted Bile Etched Blade (77630).
  - Turn in Vhalen's Necklace (77629).
  - Gives Vhalen's Necklace (77629).
- `southkarana` vhalen nostrolo, hand 77627 needs `bard15` ==5.
  - Turn in Note from Metala (77627).
  - Gives Vhalen's Necklace (77629).

## `bard20`

Values written: 1.

### 1. alkron wyrmsong — hand 47100+77641+77642+77643

Zone: `causeway`.

Sets `bard20` to `1`.

- Turn in x1: Black Chaos Gauntlets (77641).
- Turn in x1: Black Chaos Boots (77642).
- Turn in x1: Black Chaos Breastplate (77643).
- Turn in x1: Globe of Discordant Energy (47100).
In script order:

1. Sets `bard20` to `1`.
2. Spawns Oshiruk (303125).
   - Loots Dragorn Essence (77644).


How the items are reached:

- Black Chaos Gauntlets (77641)
  - Loot "Black Chaos Gauntlets" (77641) from "Stone Thrower" in `causeway`.
  - Loot "Black Chaos Gauntlets" (77641) from "A Battle-Scarred Bazu" in `causeway`.
  - Loot "Black Chaos Gauntlets" (77641) from "A Mountain Bazu" in `causeway`.
  - Loot "Black Chaos Gauntlets" (77641) from "A Murkglider Stalker" in `causeway`.
- Black Chaos Boots (77642)
  - Loot "Black Chaos Boots" (77642) from "A Discordling Enchainer" in `wallofslaughter`.
  - Loot "Black Chaos Boots" (77642) from "A Discordling Taskfiend" in `wallofslaughter`.
  - Loot "Black Chaos Boots" (77642) from "A Dragorn Darkwarrior" in `wallofslaughter`.
  - Loot "Black Chaos Boots" (77642) from "A Dragorn Ireknight" in `wallofslaughter`.
- Black Chaos Breastplate (77643)
  - Loot "Black Chaos Breastplate" (77643) from "A Gelidran Flamefreeze" (NPC 334016) in `riftseekers`. Drop cache: 4.49% chance per kill.
- Globe of Discordant Energy (47100)
  - Say "Check Lorb" to anguish/"Zone Status".
  - Spawns "Orb of Discordant Energy" (317087).
  - Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy".
  - 4 alternative loot source(s) also yield Globe of Discordant Energy (47100).

### Steps on `bard20` that do not change it

- `causeway` alkron wyrmsong, say summon needs `bard20` ==1.
  - Spawns Oshiruk (303125).
  - Loots Dragorn Essence (77644).
- `causeway` player, on loot needs `bard20` ==1.
  - Sets `mage_epic_causeway` to `1`.
  - Spawns a chest (Epic 1.5) (283157).
  - Sets `nec_epic_causeway` to `1`.
  - Sets `bard20_chest` to `1`.
  - Spawns a chest (epic 2.0) (893).
  - Sets `warr_chest_causeway` to `1`.
  - Sets `ber_chest_causeway` to `1`.
  - Sets `ench_chest_causeway` to `1`.
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

- `bard15_dracchest` set to 1 at necropolis/player.
- `bard15_metalachest` set to 1 at potorment/player.
- `bard20_chest` set to 1 at causeway/player.
