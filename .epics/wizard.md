# Wizard

Acquisition paths traced backwards from the 1.0, 1.5 and 2.0 epic rewards. Flags are dependencies, not the definition of an epic. **Broken** indicates missing graph provenance.

## Epic 1.0

### "Staff of the Four" (14341)

1. Loot "Blue Crystal Staff" (14337) from "Phinigel Autropos" in `kedge`.
2. Loot "Gnarled Staff" (14338) from "Venril Sathir" in `karnor`.
3. Loot "Mistletoe Powder" (14333) from "Tolapumj" in `sebilis`.
4. Loot "Cazic's Skin" (14332) from "Cazic Thule" in `fearplane`.
5. butcher/"Kandin Firepot", hand "Cazic's Skin" (14332) + "Mistletoe Powder" (14333). Gives "Staff of Gabstik" (14339).
6. halas/"Arantir Karondor", hand "Blue Crystal Staff" (14337) + "Gnarled Staff" (14338) + "Staff of Gabstik" (14339). Gives "Magically Sealed Bag" (14340).
7. soltemple/"Solomen", hand "Magically Sealed Bag" (14340). Gives "Staff of the Four" (14341).
    - Dialogue with soltemple/"Solomen":
      - Player: "Hail"
        - NPC say: Ah, I see you have found my study. This is where I study and scribe the history of magic in Norrath.
        - Condition: `($text=~/hail/i)`
      - Player: "History" (link: explicit mention)
        - NPC say: I have worked to chronicle everything from the beginnings of magic to what we consider the modern day of magic. Solusek Ro has been very generous to those who wield magic in Norrath. But throughout history there is one thing I have noticed - too much power corrupts the soul. I have seen and documented that the strongest wizards and those closest to Solusek Ro become corrupted by their power.
        - Condition: `($text=~/history/i)`
      - Player: "Wizards" (link: explicit mention)
        - NPC say: Unfortunately, I don't have time to speak of such things right now. But I could use your help since you are here. I have here an envelope that I need delivered to one Camin. You can find him near the wizard tower in the city of Erudin. He is a sage like myself whose knowledge rivals my own. Do you [agree] to undertake my task?
        - Condition: `($text=~/wizards/i)`
      - Player: "Agree" (link: explicit mention)
        - NPC say: Here you are, then. Good luck on your journey.
        - Condition: `($text=~/agree/i)`
        - Gives Note to Camin (18088).

## Epic 1.5

### "Staff of Prismatic Power" (12665)

1. Summon "Collapsible Sewing Kit" (17165) by casting "Unfold Sewing Kit".
2. Buy "Backpack Pattern" (12089) from "Iala Lenard" (NPC 1141) in `qeynos`. Base price: 500 copper.
3. Buy "Needle Mold" (12019) from "Dyona Rossook" (NPC 5065) in `highpass`. Base price: 180 copper.
4. Buy "Thimble Mold" (12057) from "Dyona Rossook" (NPC 5065) in `highpass`. Base price: 180 copper.
5. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
6. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `steamfont`.
7. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `tox`.
8. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `toxxulia`.
9. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
10. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). The combine does not fail.
11. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
12. **Broken:** nothing in the graph gives, loots, spawns, or combines Notice to Cease and Desist (9590).
13. Hand "Notice to Cease and Desist" (9590) to freeporteast/"Lythe Songbird". Spawns "a Freeport guard" (382255). Loot "Fine Steel Two Handed Sword" (5351) from "a Freeport guard".
14. Alternative: Loot "Fine Steel Two Handed Sword" (5351) from "a seasoned Freeport guard" (NPC 382256) in `freeporteast`; trigger: freeporteast/"Lythe Songbird", hand "Notice to Cease and Desist" (9590).
15. Alternative: Loot "Fine Steel Two Handed Sword" (5351) from "a Freeport guard" (NPC 382255) in `freportw`; trigger: freportw/"Lythe Songbird", hand "Notice to Cease and Desist" (9590).
16. Alternative: Loot "Fine Steel Two Handed Sword" (5351) from "a seasoned Freeport guard" (NPC 382256) in `freportw`; trigger: freportw/"Lythe Songbird", hand "Notice to Cease and Desist" (9590).
17. Alternative: Loot "Fine Steel Two Handed Sword" (5351) from "a minion of Meldrath" (NPC 56173) in `steamfont`; trigger: steamfont/"Meldraths Paige", say "We Shall Never Surrender".
18. Alternative: Loot "Fine Steel Two Handed Sword" (5351) from "Meldrath's melded minions" (NPC 56174) in `steamfont`; trigger: steamfont/"Meldraths Paige", say "Your Forces Are Deafeated".
19. Alternative: Loot "Fine Steel Two Handed Sword" (5351) from "Arnold the Gnomeinator" (NPC 56175) in `steamfont`; trigger: steamfont/"Meldraths Paige", say "You Shall Not Break Our Defense".
20. Alternative: Loot "Fine Steel Two Handed Sword" (5351) from "a Freeport guard" (NPC 382255) in `freeporteast`; trigger: freeporteast/"Lythe Songbird", on timer guard.
21. Alternative: Loot "Fine Steel Two Handed Sword" (5351) from "a seasoned Freeport guard" (NPC 382256) in `freeporteast`; trigger: freeporteast/"Lythe Songbird", on timer guard.
22. Alternative: Loot "Fine Steel Two Handed Sword" (5351) from "a Freeport guard" (NPC 382255) in `freportw`; trigger: freportw/"Lythe Songbird", on timer guard.
23. Alternative: Loot "Fine Steel Two Handed Sword" (5351) from "a seasoned Freeport guard" (NPC 382256) in `freportw`; trigger: freportw/"Lythe Songbird", on timer guard.
24. Combine in Forge (17): "Fine Steel Two Handed Sword" (5351), "Water Flask" (13006). Produces "Small Brick of High Quality Ore" (10468) x2, "Small Piece of High Quality Ore" (22229). Requires Blacksmithing, trivial 21.
25. Combine in Royal Qeynos Forge (40): "Small Piece of High Quality Ore" (22229), "Water Flask" (13006). Produces "High Quality Metal Bits" (22230). Requires Blacksmithing, trivial 20.
26. Combine in Vale Forge (49): "Needle Mold" (12019), "Thimble Mold" (12057), "Water Flask" (13006), "High Quality Metal Bits" (22230). Produces "Vale Sewing Kit" (92882). Requires Blacksmithing, trivial 162.
27. **Broken:** no event trigger found for `misty/misty#timer:Spawn`.
28. Starts timer `Hatch`.
29. Spawns "A Vicious Spider" (33167) after `misty/misty#timer:Hatch`.
30. Loot "Spiderling Silk" (13099) from "A Vicious Spider".
31. Forage "Spiderling Silk" (13099) in `mistmoore`.
32. Forage "Spiderling Silk" (13099) in `mmca`.
33. Forage "Spiderling Silk" (13099) in `mmcb`.
34. Forage "Spiderling Silk" (13099) in `mmcc`.
35. Forage "Spiderling Silk" (13099) in `mmcd`.
36. Forage "Spiderling Silk" (13099) in `mmce`.
37. Forage "Spiderling Silk" (13099) in `mmcf`.
38. Forage "Spiderling Silk" (13099) in `mmcg`.
39. Forage "Spiderling Silk" (13099) in `mmch`.
40. Forage "Spiderling Silk" (13099) in `mmci`.
41. Forage "Spiderling Silk" (13099) in `mmcj`.
42. Combine in "Vale Sewing Kit" (92882): "Spiderling Silk" (13099). Produces "Silk Thread" (16486). Requires Tailoring, trivial 15. The combine does not fail.
43. Combine in "Vale Sewing Kit" (92882): "Silk Thread" (16486). Produces "Silk Cord" (16489). Requires Tailoring, trivial 26.
44. potranquility/"Kalym Rasalan", say "Hail". Gives "Silken Tapestry" (12593).
45. Combine in "Collapsible Sewing Kit" (17165): "Backpack Pattern" (12089), "Silk Cord" (16489), "Silken Tapestry" (12593). Produces "Silken Tapestry Satchel" (12596). Requires Tailoring 128. The combine does not fail.
46. Ground spawn of "Prismatic Crystal" (12599) in `veksar`.
47. Ground spawn of "Prismatic Crystal" (12625) in `timorous`.
48. Ground spawn of "Prismatic Crystal" (12628) in `twilight`.
49. Loot "Prismatic Crystal" (12662) from "Treasure Sorter Neiben" in `dulak`.
50. Loot "Cohesion Gem" (67022) from "A Metallic Slime" (NPC 206031) in `poinnovation`. Drop cache: 34.24% chance per kill.
51. Spawns "Spawn Wiz 1.5; Pure Flame Elemental" (278108) in `soldungc` on event_signal.
52. Loot "Wisp of Pure Flame" (11619) from "Spawn Wiz 1.5; Pure Flame Elemental".
53. lavastorm/"Talwyn Flamecaller", hand "Wisp of Pure Flame" (11619). Sets `wiz_epic_wisp` to `1`.
54. Spawns "Mistress of the Darkwater Quest-only" (125075) in `sirens` on enter.
55. Loot "Shard of Pure Ice" (11599) from "Mistress of the Darkwater Quest-only".
56. Loot "Fluxing Staff" (11445) from "Girplan Guardian" in `wallofslaughter`.
57. lavastorm/"Talwyn Flamecaller", say "Hail". Sets `wiz_epic` to `1`.
58. Say "Gem" to scarlet/"The Gem Guardian".
59. Spawns "Elite Sun Revenant" (175306).
60. Loot "Fluxing Gem" (11448) from "Elite Sun Revenant".
61. Loot "Fluxing Rune" (11474) from "Hobgoblin Horrorfiend" in `ponightmare`.
62. Ground spawn of "Fluxing Chunk of Ore" (11576) in `dranik`.
63. lavastorm/"Talwyn Flamecaller", hand "Fluxing Staff" (11445) + "Fluxing Gem" (11448) + "Fluxing Rune" (11474) + "Fluxing Chunk of Ore" (11576). Gives "Staff of Fluxing Power" (11596).
64. Combine in "Silken Tapestry Satchel" (12596): "Prismatic Crystal" (12599), "Prismatic Crystal" (12625), "Prismatic Crystal" (12628), "Prismatic Crystal" (12662), "Cohesion Gem" (67022), "Shard of Pure Ice" (11599), "Wisp of Pure Flame" (11619), "Staff of Fluxing Power" (11596). Produces "Full Tapestry Satchel" (16753). The combine does not fail.
65. lavastorm/"Talwyn Flamecaller", hand "Full Tapestry Satchel" (16753). Gives "Staff of Prismatic Power" (12665).

## Epic 2.0

### "Staff of Phenomenal Power" (16576)

1. lavastorm/"Talwyn Flamecaller", say "Hail". Sets `wiz_epic20` to `1`.
2. Unresolved cyclic prerequisite: `wiz_epic20` >=1.
3. draniksscar/"Grathnok Gilforgan", say "Intricate Horn Of Galien". Sets `wiz_epic20` to `2`.
4. Loot "Intricate Horn of Galien" (15825) from "Lightningcaller Vhalek" in `provinggrounds`.
5. draniksscar/"Grathnok Gilforgan", hand "Intricate Horn of Galien" (15825). Sets `wiz_epic20` to `3`.
6. Say "Check Lorb" to anguish/"Zone Status".
7. Spawns "Orb of Discordant Energy" (317087).
8. Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy".
9. Alternative: Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy" (NPC 317087) in `anguish`; trigger: anguish/"Zone Status", say "Check Uorb".
10. Alternative: Loot "Globe of Discordant Energy" (47100) from "Ornate Chest" (NPC 317112) in `anguish`; trigger: anguish/"Zone Status", say "Check Amv Chest".
11. Alternative: Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy" (NPC 317087) in `anguish`; trigger: anguish/"Zone Status", on event_signal.
12. Alternative: Loot "Globe of Discordant Energy" (47100) from "Overlords Chest" (NPC 317124) in `anguish`; trigger: anguish/"Zone Status", on event_signal.
13. lavastorm/"Talwyn Flamecaller", hand "Globe of Discordant Energy" (47100). Sets `wiz_epic20` to `4`.
14. **Broken:** nothing in the graph gives, loots, spawns, or combines Spacial Distortion (16695).
15. lavastorm/"Talwyn Flamecaller", hand "Globe of Discordant Energy" (47100). Requires `wiz_epic20` set. Requires `wiz_epic20` >=3. Gives "Broken Orb of Discordant Energy" (16147).
16. Combine in "Spacial Distortion" (16695): "Broken Orb of Discordant Energy" (16147). Produces "Infused Orb of Discordant Energy" (16451). The combine does not fail.
17. **Broken:** nothing in the graph gives, loots, spawns, or combines Spacial Distortion (16765).
18. lavastorm/"Talwyn Flamecaller", hand "Globe of Discordant Energy" (47100). Requires `wiz_epic20` set. Requires `wiz_epic20` >=3. Gives "Broken Orb of Discordant Energy" (15836).
19. Combine in "Spacial Distortion" (16765): "Broken Orb of Discordant Energy" (15836). Produces "Infused Orb of Discordant Energy" (16334). The combine does not fail.
20. Summon "Collapsible Sewing Kit" (17165) by casting "Unfold Sewing Kit".
21. Buy "Backpack Pattern" (12089) from "Iala Lenard" (NPC 1141) in `qeynos`. Base price: 500 copper.
22. Buy "Needle Mold" (12019) from "Dyona Rossook" (NPC 5065) in `highpass`. Base price: 180 copper.
23. Buy "Thimble Mold" (12057) from "Dyona Rossook" (NPC 5065) in `highpass`. Base price: 180 copper.
24. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
25. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `steamfont`.
26. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `tox`.
27. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `toxxulia`.
28. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
29. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). The combine does not fail.
30. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
31. **Broken:** nothing in the graph gives, loots, spawns, or combines Notice to Cease and Desist (9590).
32. Hand "Notice to Cease and Desist" (9590) to freeporteast/"Lythe Songbird". Spawns "a Freeport guard" (382255). Loot "Fine Steel Two Handed Sword" (5351) from "a Freeport guard".
33. Alternative: Loot "Fine Steel Two Handed Sword" (5351) from "a seasoned Freeport guard" (NPC 382256) in `freeporteast`; trigger: freeporteast/"Lythe Songbird", hand "Notice to Cease and Desist" (9590).
34. Alternative: Loot "Fine Steel Two Handed Sword" (5351) from "a Freeport guard" (NPC 382255) in `freportw`; trigger: freportw/"Lythe Songbird", hand "Notice to Cease and Desist" (9590).
35. Alternative: Loot "Fine Steel Two Handed Sword" (5351) from "a seasoned Freeport guard" (NPC 382256) in `freportw`; trigger: freportw/"Lythe Songbird", hand "Notice to Cease and Desist" (9590).
36. Alternative: Loot "Fine Steel Two Handed Sword" (5351) from "a minion of Meldrath" (NPC 56173) in `steamfont`; trigger: steamfont/"Meldraths Paige", say "We Shall Never Surrender".
37. Alternative: Loot "Fine Steel Two Handed Sword" (5351) from "Meldrath's melded minions" (NPC 56174) in `steamfont`; trigger: steamfont/"Meldraths Paige", say "Your Forces Are Deafeated".
38. Alternative: Loot "Fine Steel Two Handed Sword" (5351) from "Arnold the Gnomeinator" (NPC 56175) in `steamfont`; trigger: steamfont/"Meldraths Paige", say "You Shall Not Break Our Defense".
39. Alternative: Loot "Fine Steel Two Handed Sword" (5351) from "a Freeport guard" (NPC 382255) in `freeporteast`; trigger: freeporteast/"Lythe Songbird", on timer guard.
40. Alternative: Loot "Fine Steel Two Handed Sword" (5351) from "a seasoned Freeport guard" (NPC 382256) in `freeporteast`; trigger: freeporteast/"Lythe Songbird", on timer guard.
41. Alternative: Loot "Fine Steel Two Handed Sword" (5351) from "a Freeport guard" (NPC 382255) in `freportw`; trigger: freportw/"Lythe Songbird", on timer guard.
42. Alternative: Loot "Fine Steel Two Handed Sword" (5351) from "a seasoned Freeport guard" (NPC 382256) in `freportw`; trigger: freportw/"Lythe Songbird", on timer guard.
43. Combine in Forge (17): "Fine Steel Two Handed Sword" (5351), "Water Flask" (13006). Produces "Small Brick of High Quality Ore" (10468) x2, "Small Piece of High Quality Ore" (22229). Requires Blacksmithing, trivial 21.
44. Combine in Royal Qeynos Forge (40): "Small Piece of High Quality Ore" (22229), "Water Flask" (13006). Produces "High Quality Metal Bits" (22230). Requires Blacksmithing, trivial 20.
45. Combine in Vale Forge (49): "Needle Mold" (12019), "Thimble Mold" (12057), "Water Flask" (13006), "High Quality Metal Bits" (22230). Produces "Vale Sewing Kit" (92882). Requires Blacksmithing, trivial 162.
46. **Broken:** no event trigger found for `misty/misty#timer:Spawn`.
47. Starts timer `Hatch`.
48. Spawns "A Vicious Spider" (33167) after `misty/misty#timer:Hatch`.
49. Loot "Spiderling Silk" (13099) from "A Vicious Spider".
50. Forage "Spiderling Silk" (13099) in `mistmoore`.
51. Forage "Spiderling Silk" (13099) in `mmca`.
52. Forage "Spiderling Silk" (13099) in `mmcb`.
53. Forage "Spiderling Silk" (13099) in `mmcc`.
54. Forage "Spiderling Silk" (13099) in `mmcd`.
55. Forage "Spiderling Silk" (13099) in `mmce`.
56. Forage "Spiderling Silk" (13099) in `mmcf`.
57. Forage "Spiderling Silk" (13099) in `mmcg`.
58. Forage "Spiderling Silk" (13099) in `mmch`.
59. Forage "Spiderling Silk" (13099) in `mmci`.
60. Forage "Spiderling Silk" (13099) in `mmcj`.
61. Combine in "Vale Sewing Kit" (92882): "Spiderling Silk" (13099). Produces "Silk Thread" (16486). Requires Tailoring, trivial 15. The combine does not fail.
62. Combine in "Vale Sewing Kit" (92882): "Silk Thread" (16486). Produces "Silk Cord" (16489). Requires Tailoring, trivial 26.
63. potranquility/"Kalym Rasalan", say "Hail". Gives "Silken Tapestry" (12593).
64. Combine in "Collapsible Sewing Kit" (17165): "Backpack Pattern" (12089), "Silk Cord" (16489), "Silken Tapestry" (12593). Produces "Silken Tapestry Satchel" (12596). Requires Tailoring 128. The combine does not fail.
65. Ground spawn of "Prismatic Crystal" (12599) in `veksar`.
66. Ground spawn of "Prismatic Crystal" (12625) in `timorous`.
67. Ground spawn of "Prismatic Crystal" (12628) in `twilight`.
68. Loot "Prismatic Crystal" (12662) from "Treasure Sorter Neiben" in `dulak`.
69. Loot "Cohesion Gem" (67022) from "A Metallic Slime" (NPC 206031) in `poinnovation`. Drop cache: 34.24% chance per kill.
70. Spawns "Spawn Wiz 1.5; Pure Flame Elemental" (278108) in `soldungc` on event_signal.
71. Loot "Wisp of Pure Flame" (11619) from "Spawn Wiz 1.5; Pure Flame Elemental".
72. lavastorm/"Talwyn Flamecaller", hand "Wisp of Pure Flame" (11619). Sets `wiz_epic_wisp` to `1`.
73. Spawns "Mistress of the Darkwater Quest-only" (125075) in `sirens` on enter.
74. Loot "Shard of Pure Ice" (11599) from "Mistress of the Darkwater Quest-only".
75. Loot "Fluxing Staff" (11445) from "Girplan Guardian" in `wallofslaughter`.
76. lavastorm/"Talwyn Flamecaller", say "Hail". Sets `wiz_epic` to `1`.
77. Say "Gem" to scarlet/"The Gem Guardian".
78. Spawns "Elite Sun Revenant" (175306).
79. Loot "Fluxing Gem" (11448) from "Elite Sun Revenant".
80. Loot "Fluxing Rune" (11474) from "Hobgoblin Horrorfiend" in `ponightmare`.
81. Ground spawn of "Fluxing Chunk of Ore" (11576) in `dranik`.
82. lavastorm/"Talwyn Flamecaller", hand "Fluxing Staff" (11445) + "Fluxing Gem" (11448) + "Fluxing Rune" (11474) + "Fluxing Chunk of Ore" (11576). Gives "Staff of Fluxing Power" (11596).
83. Combine in "Silken Tapestry Satchel" (12596): "Prismatic Crystal" (12599), "Prismatic Crystal" (12625), "Prismatic Crystal" (12628), "Prismatic Crystal" (12662), "Cohesion Gem" (67022), "Shard of Pure Ice" (11599), "Wisp of Pure Flame" (11619), "Staff of Fluxing Power" (11596). Produces "Full Tapestry Satchel" (16753). The combine does not fail.
84. lavastorm/"Talwyn Flamecaller", hand "Full Tapestry Satchel" (16753). Gives "Staff of Prismatic Power" (12665).
85. lavastorm/"Talwyn Flamecaller", hand "Staff of Prismatic Power" (12665) + "Infused Orb of Discordant Energy" (16334) + "Infused Orb of Discordant Energy" (16451). Requires `wiz_epic20` ==4. Gives "Staff of Phenomenal Power" (16576).

## Quest-state progression

## 0. Prerequisites

Shared acquisition steps appear in the first prerequisite chain that needs them. Later sections reference that chain rather than repeating it.

### "Spell: Electrical Charge" (16623)

1. bazaar/"Caerlyna", hand "Spell Research Kit" (93492). Gives "Spell Research Kit Token" (93667).
    - Dialogue with bazaar/"Caerlyna":
      - Player: "Hail"
        - NPC say: Greetings $name! Nice to meet you. I've started up a complimentary bag check service. Feel free to give me your weight reducing bag, and I'll give you a token in return. When you would like to get your bag back, simply return to me with your token.
        - Condition: `($text=~/hail/i)`
2. bazaar/"Caerlyna", hand "Spell Research Kit Token" (93667). Gives "Spell Research Kit" (93492).
3. Loot "Metal Pipe" (12979) from "A Drolvarg Pawbuster" in `karnor`.
4. Loot "Metal Pipe" (12980) from "An Iksar Betrayer" in `chardok`.
5. Buy "King's Court Token" (66616) from "Keiya Oakwood" (NPC 150311) in `shadowhaven`. Base price: 95,239 copper.
6. shadowhaven/"Gralin Silvertooth", hand "King's Court Token" (66616). Gives "Deluxe Sewing Kit" (17966).
    - Dialogue with shadowhaven/"Gralin Silvertooth":
      - Player: "Hail"
        - NPC say: Thank you for coming to Shandeling's Casino! If you would like to try your luck at a game of chance, I can offer you a game of King's Court with prizes best suited for any Shadowknight, Ranger, Beastlord, Bard, or Paladin. To play, buy a token from any of the waitresses and hand it to me when ready.
        - Condition: `($text=~/hail/i)`
7. Loot "Code of Zan Fi" (12316) from "Targin the Rock" in `soldungb`.
8. Loot "Blackburrow Gnoll Pelt" (13027) from "Refugee Splitpaw" (NPC 17023) in `blackburrow`. Drop cache: 55% chance per kill.
9. Loot "Blackburrow Gnoll Skin" (13028) from "The Gnoll High Shaman" (NPC 17042) in `blackburrow`. Drop cache: 55% chance per kill.
10. Loot "Putrid Rib Bone" (13722) from "A Putrid Skeleton" in `qeytoqrg`.
11. Loot "Gnoll Pup Scalp" (13789) from "A Gnoll Pup" in `blackburrow`.
12. Loot "Gnoll Pup Scalp" (13789) from "A Gnoll Pup" in `everfrost`.
13. Loot "Gnoll Pup Scalp" (13789) from "A Gnoll Pup" in `qeynos2`.
14. Loot "Gnoll Pup Scalp" (13789) from "A Gnoll Pup" in `qeytoqrg`.
15. qeynos2/"Phin Esrinap", hand "Gnoll Pup Scalp" (13789) + "Gnoll Pup Scalp" (13789) + "Gnoll Pup Scalp" (13789) + "Gnoll Pup Scalp" (13789). Gives "White Headband" (10110).
    - Dialogue with qeynos2/"Phin Esrinap":
      - Player: "Hail"
        - NPC say: Hello, my name is Phin. Practice, practice, practice.. That's my motto. It is my responsibility to train our members, and help them to advance their skills and abilities. I also reward our members with colored [headbands] for completing certain tasks.
        - Condition: `(e.message:findi("hail"))`
      - Player: "Headbands" (link: explicit mention)
        - NPC say: Yes, I give the [White, Yellow, and Orange Headbands] to our newer members, and Togahn gives out [Red, Purple, and Blue Headbands] to our elder members.
        - Condition: `(e.message:findi("headbands"))`
      - Player: "Tomer Instogle" (link: conversation sequence)
        - NPC say: Tomer? I think Seta needs someone to go find him... Go ask her.
        - Condition: `(e.message:findi("Tomer Instogle"))`
      - Player: "Konem Matse" (link: conversation sequence)
        - NPC say: Konem was sent to retrieve [supplies] and has not returned.
        - Condition: `(e.message:findi("Konem Matse"))`
      - Player: "Supplies" (link: explicit mention)
        - NPC say: Take this message to Konem and find out where my supplies are.
        - Condition: `(e.message:findi("supplies"))`
        - Gives Message to Konem (18921).
      - Player: "Gnoll"
        - NPC say: Those vile creatures are constantly attacking our city.. and often killing innocent citizens. It is our duty to help defend Qeynos from their vicious raids.
        - Condition: `(e.message:findi("gnoll"))`
      - Player: "White Headband" (link: conversation sequence)
        - NPC say: That is our training headband.. Beginning students can earn this by slaying four [gnoll] pups, and bringing their scalps back to me.
        - Condition: `(fac <= 5)`
        - Condition: `(e.message:findi("white headband"))`
      - Player: "Yellow Headband" (link: external event mention)
        - Prompted by `event_trade`:
          - NPC say: Good work.. and, as promised, here is your reward. It is an honor to present this yellow headband to , for recent acts of courage and heroism, on behalf of the Silent Fist Clan.
          - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 13722,item2 = 13722, item3 = 13722,item4 = 10110}))`
        - NPC say: This is awarded to our students for helping clear out the evil that inhabits the old ruins of the Qeynos Hills. Just bring me back three putrid rib bones as proof of your good deeds and turn in your [training headband], and then I will give you the yellow headband.
        - Condition: `(fac <= 5)`
        - Condition: `(e.message:findi("yellow headband"))`
      - Player: "Orange Headband" (link: explicit mention)
        - Prompted by player input: "Headbands"
        - NPC say: This is a difficult award to obtain. The city of Qeynos is, as you know, under constant attack by the gnolls of Blackburrow. The Silent Fist Clan rewards its members who venture deep into this gnoll stronghold and bring swift justice to these vile creatures. Please return two Blackburrow gnoll pelts - make sure they aren't ruined - and a Blackburrow gnoll skin as proof of your noble actions. Also, turn in your [yellow headband], and then I shall give you the orange one. Good luck.
        - Condition: `(fac <= 5)`
        - Condition: `(e.message:findi("orange headband"))`
16. qeynos2/"Phin Esrinap", hand "White Headband" (10110) + "Putrid Rib Bone" (13722) + "Putrid Rib Bone" (13722) + "Putrid Rib Bone" (13722). Gives "Yellow Headband" (10111).
17. qeynos2/"Phin Esrinap", hand "Yellow Headband" (10111) + "Blackburrow Gnoll Pelt" (13027) + "Blackburrow Gnoll Pelt" (13027) + "Blackburrow Gnoll Skin" (13028). Gives "Orange Headband" (10112).
18. Loot "Head of Ghanex Drah" (13165) from "Ghanex Drah" in `southkarana`.
19. Loot "Dareb's Skull" (13166) from "High Shaman Phido" in `southkarana`.
20. Loot "Dareb's Skull" (13166) from "An Undead Cyclops" in `southkarana`.
21. Loot "Head of Shen" (13167) from "High Shaman Grisok" in `southkarana`.
22. qeynos2/"Togahn Sorast", hand "Orange Headband" (10112) + "Head of Ghanex Drah" (13165) + "Dareb's Skull" (13166) + "Head of Shen" (13167). Gives "Red Headband" (10113).
    - Dialogue with qeynos2/"Togahn Sorast":
      - Player: "Hail"
        - NPC say: Greetings.. I am Second Master Togahn Sorast. I am here to teach the ways of our guild. For our more advanced members, I will give out [headbands] as a reward for their contribution to the clan.
        - Condition: `(e.message:findi("hail"))`
      - Player: "Headbands" (link: explicit mention)
        - NPC say: The Silent Fist Clan gives out colored Headbands for various deeds completed by our students. Phin gives out the White, Yellow, and Orange Headbands.. and I give out the [Red, Purple, and Blue Headbands].
        - Condition: `(e.message:findi("headbands"))`
      - Player: "Red Headband" (link: external event mention)
        - Prompted by `event_trade`:
          - NPC say: We are deeply honored to have such great warrior as part of our Clan. With a proper burial, Shen and Dareb's souls will finally be at peace, and with the death of that vile Ghanex, the plains will be much safer for travelers. It is a great honor to present you, , with the red headband of the Silent Fist Clan.
          - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 10112, item2 =13165, item3 = 13166, item4 = 13167}))`
        - NPC say: Ah, you think you are skilled enough to earn the red headband of the Silent Fist Clan, ? Hmmm.. Well, if you can help us find [Brother Dareb], you would certainly deserve the honor of wearing the red headband.
        - Condition: `(fac <= 3)`
        - Condition: `(e.message:findi("red headband"))`
      - Player: "Brother Dareb" (link: explicit mention)
        - NPC say: Yes, brother Dareb was last heard from over two weeks ago. He was out in the Plains of South Karana, and then just disappeared. We fear that those vile gnolls fleeing Splitpaw may have captured him or worse. We sent brother Shen to go search the Karanas and look for Dareb over three days ago, but haven't heard from him, either. I fear the worst for both of them, especially if the [Splitpaws] are involved. Please, , find and return our lost brothers to us. If they are not alive, bring back their remains so we may give them a proper burial.. and, if it is that evil [Ghanex Drah]'s doing, bring me his head as well, for the honor of the clan. You do this for us, , and turn in your orange headband, and I will reward you with the red headband of the Silent Fist. Good luck.
        - Condition: `(fac <= 3)`
        - Condition: `(e.message:findi("brother dareb"))`
      - Player: "Splitpaws" (link: explicit mention)
        - NPC say: The Splitpaws were a large clan of gnolls that lived in a burrow out in South Karana, They have recently been ousted from their home by a new clan of gnolls that are very powerful. We try to stay away from them if we can, for we do not know much about this new breed. The Splitpaws are on the move and now is the only time to strike. If we wait too long, there will be no way to find our brother. Go now my friend, we haven't much time.
        - Condition: `(fac <= 3)`
        - Condition: `(e.message:findi("splitpaws"))`
      - Player: "Ghanex Drah" (link: explicit mention)
        - Prompted by player input: "Brother Dareb"
        - NPC say: Ghanex Drah is ruler of the now fleeing gnolls of Splitpaw. I've heard rumors that he has been dabbling in the dark art of necromancy. Ghanex is looking for more test subjects, no doubt to rebuild his stronghold. The good people of Antonica must put an end to his evil reign soon, or I fear he could grow much more powerful.
        - Condition: `(fac <= 3)`
        - Condition: `(e.message:findi("Ghanex Drah"))`
      - Player: "Purple Headband" (link: external event mention)
        - Prompted by `event_trade`:
          - NPC say: In honor of your recent acts of courage and dedication, I reward you, , with the purple headband of the Silent Fist Clan.
          - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 10113, item2 =13168, item3 = 13169, item4 = 3000}))`
        - NPC say: Ah, you think you are now skilled enough to deserve the purple headband of the Silent Fist Clan? Very well, , I have a task for you that will prove whether or not you are worthy of this honor. I have heard recent rumors of ancient evils surfacing once again throughout Antonica. These evil groups have discovered some items that are giving them mystical and dangerous powers. These items must be destroyed, or else the evils of Norrath may gain control of the world's future. Bring me these [evil items], and turn in your red headband, and you will have proven yourself a mighty spirit and dedicated member of the Silent Fist.
        - Condition: `(fac <= 3)`
        - Condition: `(e.message:findi("purple headband"))`
      - Player: "Evil Items" (link: explicit mention)
        - NPC say: These evil creations have been found all over Antonica, and no one knows, or at least no one admits to knowing, where exactly they were found, but we do know that they are currently in the wrong hands and must be destroyed. Please, , seek out the [Skull of Jhen'Tra], the [Dagger of Marnek], and the [Coronet of Buried Blood], and bring them to me.
        - Condition: `(fac <= 3)`
        - Condition: `(e.message:findi("evil items"))`
      - Player: "Dagger of Marnek" (link: explicit mention)
        - NPC say: The Dagger of Marnek is a diabolical weapon created by the ancient necromancer Marnek Jaull. Marnek was the leader of a small cult of necromancers who worshipped Solusek Ro. Marnek used this dagger in his ceremonial sacrifices to the Burning Prince, to increase his own power and show his loyalty to his god. His cult grew stronger and word of the evil acts spread all over Antonica. Legend has it that a group of paladins from Erudin, followers of Prexus, spent over 10 years searching out Marnek and his followers, and finally destroyed them. Though Marnek's evil reign was put to an end, many of his books and items are still being uncovered to this day. The Dagger of Marnek is now being used by the evil inhabitants who control the depths of Befallen. Bring this dagger to me, so that we may dispose of it and banish its evil powers forever.
        - Condition: `(fac <= 3)`
        - Condition: `(e.message:findi("Dagger of Marnek"))`
      - Player: "Coronet of Buried Blood" (link: explicit mention)
        - Prompted by player input: "Evil Items"
        - NPC say: The Coronet of Buried Blood is an ancient headdress which is said to have belonged to the High Priest of the Plexant Temple. The Plexant were known to be devout followers of Innoruuk and the coronet is supposed to have been blessed by the Prince of Hate himself. Apparently, the coronet is now in the hands of a clan of goblins that dwell in the caverns of Permafrost.
        - Condition: `(fac <= 3)`
        - Condition: `(e.message:findi("Coronet of Buried Blood"))`
      - Player: "Blue Headband" (link: explicit mention)
        - Prompted by player input: "Headbands"
        - NPC say: Sorry, we are currently out of blue headbands. Please check back later.
        - Condition: `(fac <= 3)`
        - Condition: `(e.message:findi("blue headband"))`
      - Player: "Black Headband" (link: conversation sequence)
        - NPC say: The black headband is one of the highest honors of our guild.. [Lu'Sun] only gives those out for great acts of heroism and devotion to the clan.
        - Condition: `(fac <= 3)`
        - Condition: `(e.message:findi("black headband"))`
23. Loot "Skull of Jhen'Tra" (13168) from "A Gnoll Embalmer" in `lakerathe`.
24. Loot "Dagger of Marnek" (13169) from "The Fabled Thaumaturgist".
25. Loot "Dagger of Marnek" (13169) from "The Thaumaturgist" in `befallen`.
26. Loot "Zaharn's Coronet" (3000) from "High Priest Zaharn" in `permafrost`.
27. qeynos2/"Togahn Sorast", hand "Zaharn's Coronet" (3000) + "Red Headband" (10113) + "Skull of Jhen'Tra" (13168) + "Dagger of Marnek" (13169). Gives "Purple Headband" (10114).
28. southkarana/"Brother Qwinn", hand "Purple Headband" (10114) + "Code of Zan Fi" (12316). Gives "Needle of the Void" (12314).
    - Dialogue with southkarana/"Brother Qwinn":
      - Player: "Hail"
        - NPC say: In the name of the [Brotherhood of the Lost Circle], I greet you.
        - Condition: `(e.message:findi("hail"))`
      - Player: "Brotherhood Of The Lost Circle" (link: explicit mention)
        - NPC say: The [monks of the Whistling Fist] are called the Lost Circle by others. We are an ancient league of monks, long forgotten and nearly extinct. Within this realm, there are only two. [Brother Zephyl] and myself. We seek the items stolen from us. I seek the [Code of Zan Fi].
        - Condition: `(e.message:findi("brotherhood of the lost circle"))`
      - Player: "Monks Of The Whistling Fist" (link: explicit mention)
        - NPC say: The monks of the Whistling fist were forged from the vision of the great master, Zan Fi. When the Combine Empire reigned supreme, a single bard grew to learn the ways of the monk. This bard was Zan Fi. The brotherhood was all but destroyed in the times that followed. Now only a few remain to carry on Zan Fi's legacy.
        - Condition: `(e.message:findi("monks of the whistling fist"))`
      - Player: "Code Of Zan Fi" (link: explicit mention)
        - Prompted by player input: "Brotherhood Of The Lost Circle"
        - NPC say: The tome called the Code of the Whistling Fist has been stolen from me. It contains many secrets pertaining to our brotherhood. Thankfully, it is magically locked and only a Zan Fi master could unlock it. I require a monk to retrieve it. Would you be an [interested monk]?
        - Condition: `(e.message:findi("code of zan fi"))`
      - Player: "Interested Monk" (link: explicit mention)
        - NPC say: Then venture into the depths beyond the great Solusek Mining Company. There, living among the kobolds, will be Targin the Rock. Get the book from him, then return here and wait for my reappearance. When we meet again, you shall hand me the book and a purple headband earned from the Silent Fist clan. Do so and you shall be closer to joining the brotherhood.
        - Condition: `(e.message:findi("interested monk"))`
      - Player: "Brother Zephyl" (link: explicit mention)
        - Prompted by player input: "Brotherhood Of The Lost Circle"
        - NPC say: Brother Zephyl is searching for one who can return the [idol of Zan Fi]. I believe he is somewhere in the vicinity of the Rathe Mountains.
        - Condition: `(e.message:findi("brother zephyl"))`
      - Player: "Idol Of Zan Fi" (link: explicit mention)
        - NPC say: The idol of Zan Fi is a totem that is sacred to our brotherhood. I cannot share its secrets, but I can tell you that [Brother Zephyl] will offer to you a reward for its return..
        - Condition: `(e.message:findi("idol of zan fi"))`
      - Player: "Return The Headband" (link: external event mention)
        - Prompted by `event_trade`:
          - NPC say: We thank you for the return of the Code of the Whistling Fist. Take this sewing needle. You shall find it useful should you aid [Brother Zephyl] in his quest. His item, the needle, a swatch of shadow silk and a scroll containing Jonathan's Whistling Warsong. Into a sewing kit they will be going. And into the brotherhood will you. I hope you do not wish me to [return the headband]..
          - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 12316,item2 = 10114}))`
        - NPC say: Then you will return that which was earned or the robe.
        - Condition: `(e.message:findi("return the headband"))`
29. Loot "The Idol" (12317) from "Raster of Guk" in `gukbottom`.
30. Loot "Blackened Wand" (13237) from "Priest Amiaz" in `befallen`.
31. Loot "Blackened Sapphire" (13238) from "Ekeros" in `najena`.
32. Buy "Greater Lightstone" (10400) from "Gliblixl Rocktok" (NPC 151204) in `bazaar`. Base price: 4,500 copper.
33. Loot "Cutthroat Insignia Ring" (1903) from "a Dervish Cutthroat" (NPC 457074) in `oldcommons`. Drop cache: 55.56% chance per kill.
34. Loot "Legionnaire's Bracer" (2299) from "Orc Legionnaire" (NPC 21119) in `commons`. Drop cache: 84% chance per kill.
35. Loot "Deathfist Pawn Scalp" (13794) from "Orc Pawn" (NPC 415088) in `mistythicket`. Drop cache: 50% chance per kill.
36. Loot "Snake Fang" (13067) from "A Giant Briar Snake" (NPC 414061) in `toxxulia`. Drop cache: 58.21% chance per kill.
37. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `steamfont`.
38. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `tox`.
39. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `toxxulia`.
40. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
41. freeportwest/"Velan Torresk", hand "Snake Fang" (13067) + "Bone Chips" (13073) + "Deathfist Pawn Scalp" (13794) + "Deathfist Pawn Scalp" (13794). Gives "White Training Sash" (10130).
    - Dialogue with freeportwest/"Velan Torresk":
      - Player: "Hail"
        - NPC say: Greetings. ! I am Velan Torresk of the Ashen Order. I am in charge of training the newest members of our clan. and helping them advance their skills and rank. When members perform certain tasks on behalf of the Order. they advance to a higher rank in our clan. and are awarded a special [sash].
        - Condition: `(e.message:findi("hail"))`
      - Player: "Sash" (link: explicit mention)
        - NPC say: The Sashes of Order are given out by the various trainers of our clan. I give out the [white training sash] and the [yellow Sash of Order]. and [Reyia] is in charge of the [orange and red sashes].
        - Condition: `(e.message:findi("sash"))`
      - Player: "Orcs"
        - NPC say: The Deathfist Orcs are a large tribe of Orcs who live out in the desert. They are constantly sending small raiding parties and scouts to attack Freeport and its citizens.
        - Condition: `(e.message:findi("orcs"))`
      - Player: "White Training Sash" (link: explicit mention)
        - Prompted by player input: "Sash"
        - NPC say: The white training sash of the Ashen Order is awarded to our new members for completing a few simple tasks to prove their devotion to our clan. As you know, Freeport is a very hostile place, under constant attack from [orcs], wild beasts, and even the undead. To help keep this city and its citizens relatively safe, we must help the Militia protect the main gates. Bring me two Deathfist pawn scalps from those vile [Deathfist orcs], a snake fang, and some bone chips from a skeleton. Good luck, , represent us well!
        - Condition: `(fac < 4)`
        - Condition: `(e.message:findi("white training sash"))`
      - Player: "Yellow Sash Of Order" (link: explicit mention)
        - Prompted by player input: "Sash"
        - NPC say: To earn the yellow sash, you must prove yourself to be very skilled in the art of fighting. The lands to the west and south of Freeport are filled with dangerous beasts that often prey upon innocent travelers. Help protect our merchant caravans and traveling citizens, while at the same time practicing your defensive skills, and eliminating these deadly creatures from the surrounding landscape. Bring me a giant snake rattle, a Deathfist slashed belt, the chitin of a desert tarantula, and turn in your white training sash, and I shall reward your noble work with our yellow Sash of Order. Good luck, !
        - Condition: `(fac < 4)`
        - Condition: `(e.message:findi("yellow sash of order"))`
      - Player: "White Training Sash" (link: explicit mention)
        - NPC say: I have been watching you, and appreciate the help you've given to the brothers and sisters of the Ashen Order, but I feel that such a vital matter should be left to one of our more trusted members.
        - Condition: `(fac > 3)`
        - Condition: `(e.message:findi("white training sash") or e.message:findi("yellow sash of order"))`
      - Player: "Yellow Sash Of Order" (link: explicit mention)
        - Prompted by player input: "Sash"
        - NPC say: I have been watching you, and appreciate the help you've given to the brothers and sisters of the Ashen Order, but I feel that such a vital matter should be left to one of our more trusted members.
        - Condition: `(fac > 3)`
        - Condition: `(e.message:findi("white training sash") or e.message:findi("yellow sash of order"))`
42. Loot "Giant Snake Rattle" (13058) from "A Darkweed Snake" (NPC 457018) in `oldcommons`. Drop cache: 43.94% chance per kill.
43. misty/"Misty", on event signal:33161.
44. Starts timer `Adds`.
45. Spawns "A Scarecrow" (33168) after `misty/misty#timer:Adds`.
46. Loot "Deathfist Slashed Belt" (13916) from "A Scarecrow".
47. Loot "Desert Tarantula Chitin" (20901) from "A Dune Tarantula" (NPC 392086) in `northro`. Drop cache: 45.56% chance per kill.
48. freeportwest/"Velan Torresk", hand "White Training Sash" (10130) + "Giant Snake Rattle" (13058) + "Deathfist Slashed Belt" (13916) + "Desert Tarantula Chitin" (20901). Gives "Yellow Sash of Order" (10131).
49. freeportwest/"Reyia Beslin", hand "Cutthroat Insignia Ring" (1903) + "Legionnaire's Bracer" (2299) + "Yellow Sash of Order" (10131) + "Greater Lightstone" (10400). Gives "Orange Sash of Order" (10132).
    - Dialogue with freeportwest/"Reyia Beslin":
      - Player: "Hail"
        - NPC say: Greetings. . I am Reyia Beslin of the Ashen Order. I help to train our members and I am in charge of handing out the orange and red Sashes of Order. Would you like to know how you can get an [orange sash]? Or maybe you think you are ready to earn the [red sash]?
        - Condition: `(e.message:findi("hail"))`
      - Player: "Orange Sash" (link: explicit mention)
        - NPC say: To prove your skills and earn the orange Sash of Order, you must bring me the following items - a greater lightstone, a cutthroat insignia ring, a legionnaire's bracer, and, of course, your yellow sash. I will leave it to you to figure out exactly where to get these items. Good luck, .
        - Condition: `(e.message:findi("orange sash"))`
      - Player: "Red Sash" (link: explicit mention)
        - Prompted by player input: "Hail"
        - NPC say: So, you think you are skilled enough to earn the red Sash of Order, ? I have just the [task] for you then. But be warned, this will be the toughest challenge you have faced yet. There are many legends and myths of great heroes and ancient evils from all over Norrath. Here in Freeport, we get travelers from all over the world, and we get their tales as well. The point is that most of these stories are just that, stories and fairy tales. Told to amuse people and frighten children. I also thought the tales I'd heard about the [Marnek Jaull] were only legends, but now I know better.
        - Condition: `(e.message:findi("red sash"))`
      - Player: "Marnek Jaull" (link: explicit mention)
        - NPC say: Marnek Jaull led a cult of necromancers who followed the Burning Prince, Solusek Ro. He built an army, known as the Burning Dead, and spread destruction and fire throughout Antonica. Over the years, the Burning Dead fought many fierce and bloody battles with the paladins of Prexus, the Oceanlord. Though Marnek achieved many victories over the paladins, ultimately they were able to defeat him and destroy the Burning Dead. Legends say that before his defeat, Marnek created many powerful weapons and items, and wrote many books on his findings in the areas of magic. Many of these items were hidden away from the paladin forces, and remain untouched, waiting for Marnek's return, as the legends go.
        - Condition: `(e.message:findi("Marnek Jaull"))`
      - Player: "Task" (link: explicit mention)
        - Prompted by player input: "Red Sash"
        - NPC say: I've heard a few legends of a powerful wand that Marnek himself used to wield. This was known as the wand of the Burning Dead, and was rumored to instill its owner with mystical energies. The legends I have heard all differed on the wand's creation and powers, but the basic story was always the same. I will [tell you the legend] if you like. The task I have for you is to bring me the two parts that make up the wand of the Burning Dead, before they can be assembled and used for evil once again. Bring me [Marnek's wand] and the [Sapphire of Souls], along with your orange sash, and you will have proven yourself a loyal member of the Ashen Order, worthy of receiving the red sash.
        - Condition: `(e.message:findi("task"))`
      - Player: "Tell Me The Legend" (link: prompt response)
        - NPC say: The legend of the wand of the Burning Dead goes basically like this, though you may hear slighty different versions from others. Marnek did a lot of experiments and created an unknown number of diabolical artifacts and weapons. One of his creations was this wand. Marnek fashioned a charred wand from the scorched bone of a paladin of Prexus, and Solusek Ro himself created the wretched Sapphire of Souls. Then, Marnek and his priests combined these, with the Burning Prince's blessing, to create the wand of the Burning Dead. Marnek used this Wand and its powers in his evil and destructive reign over Antonica. Years later, as Marnek starting losing battles to the paladins of Prexus, one of his own followers, a necromancer named Kenox, was able to steal the wand. Sensing Marnek's defeat, Kenox made his way toward Odus, hoping to strike a deal with the paladins for the wand. Would you like me to [tell you about Kenox]?
        - Condition: `(e.message:findi("tell me the legend") or e.message:findi("tell you the legend"))`
      - Player: "Tell You The Legend" (link: explicit mention)
        - Prompted by player input: "Task"
        - NPC say: The legend of the wand of the Burning Dead goes basically like this, though you may hear slighty different versions from others. Marnek did a lot of experiments and created an unknown number of diabolical artifacts and weapons. One of his creations was this wand. Marnek fashioned a charred wand from the scorched bone of a paladin of Prexus, and Solusek Ro himself created the wretched Sapphire of Souls. Then, Marnek and his priests combined these, with the Burning Prince's blessing, to create the wand of the Burning Dead. Marnek used this Wand and its powers in his evil and destructive reign over Antonica. Years later, as Marnek starting losing battles to the paladins of Prexus, one of his own followers, a necromancer named Kenox, was able to steal the wand. Sensing Marnek's defeat, Kenox made his way toward Odus, hoping to strike a deal with the paladins for the wand. Would you like me to [tell you about Kenox]?
        - Condition: `(e.message:findi("tell me the legend") or e.message:findi("tell you the legend"))`
      - Player: "tell me about Kenox" (link: prompt response)
        - NPC say: Well, Kenox was not as sly as he liked to think he was. Marnek knew full well what he was up to, but let him continue with his plans. Kenox had arranged to meet with two paladins late one nght on a small island in Erud's Crossing, a place that would be considered neutral ground. Sir Toran Neshal, leader of the paladins, knowing the power of the wand, was certainly not going to make any deals with a servant of Solusek Ro, and definitely not foolish enough to take any chances with this mission. Imagine the look on Kenox's face when a ship carrying more than 25 paladins, including Sir Toran, arrived at the small island! The paladins immediately captured Kenox and the wand, and headed back to Erudin. Would like me to tell you [what happened to Toran]?
        - Condition: `(e.message:findi("tell me about Kenox") or e.message:findi("tell you about Kenox"))`
      - Player: "tell you about Kenox" (link: explicit mention)
        - Prompted by player input: "Tell Me The Legend"
        - NPC say: Well, Kenox was not as sly as he liked to think he was. Marnek knew full well what he was up to, but let him continue with his plans. Kenox had arranged to meet with two paladins late one nght on a small island in Erud's Crossing, a place that would be considered neutral ground. Sir Toran Neshal, leader of the paladins, knowing the power of the wand, was certainly not going to make any deals with a servant of Solusek Ro, and definitely not foolish enough to take any chances with this mission. Imagine the look on Kenox's face when a ship carrying more than 25 paladins, including Sir Toran, arrived at the small island! The paladins immediately captured Kenox and the wand, and headed back to Erudin. Would like me to tell you [what happened to Toran]?
        - Condition: `(e.message:findi("tell me about Kenox") or e.message:findi("tell you about Kenox"))`
      - Player: "What happened to Toran" (link: explicit mention)
        - NPC say: Below the deck of the ship, Toran and his men questioned Kenox and carefully inspected the wand. Toran ordered one of his men to pick up the wand and try to identify its true powers. The man picked up the wand, but was unable to decipher its magic. He handed it to Toran, just as Marnek and Solusek had hoped, and the wand exploded, instantly incinerating the ship and everyone aboard, and lighting up the night sky with a giant fireball. Marnek's plan had succeeded. With the help and blessing of the Burning Prince, they had destroyed Sir Toran and an entire squad of Prexus' finest paladins. Years later, though, the paladins were able to regroup and ultimately defeat Marnek. The wand of the Burning Dead was destroyed and gone forever. Or least, that's what we thought. This wand must never be allowed to be made whole again.
        - Condition: `(e.message:findi("What happened to Toran"))`
      - Player: "Sapphire of Souls" (link: explicit mention)
        - Prompted by player input: "Task"
        - NPC say: The Sapphire of Souls is rumored to be held by A thief IN Najena. No one knows how this guy obtained the Sapphire, but we believe he is trying to strike A bargain with those who are currently holding Befallen. Apparently and we aren't the only ones who know of the Wand's powers, and this thief thinks he can make A profit from it. Sadly and his greed will surely lead to his death.
        - Condition: `(e.message:findi("Sapphire of Souls"))`
50. freeportwest/"Reyia Beslin", hand "Orange Sash of Order" (10132) + "Blackened Wand" (13237) + "Blackened Sapphire" (13238). Gives "Red Sash of Order" (10133).
51. rathemtn/"Brother Zephyl", hand "Red Sash of Order" (10133) + "The Idol" (12317). Gives "Rare Robe Pattern" (12315).
    - Dialogue with rathemtn/"Brother Zephyl":
      - Player: "Hail"
        - NPC say: Greetings. I am one with the [Lost Circle]. You have found me. What is it you desire?
        - Condition: `($text=~/hail/i)`
      - Player: "Lost Circle" (link: explicit mention)
        - NPC say: The [monks of the Whistling Fist] are called the Lost Circle by others. We are an ancient league of monks. Long forgotten and few yet remain. Within this realm there are only two. [Brother Qwinn] and I. We seek the items stolen from us. I seek the [idol of Zan Fi].
        - Condition: `($text=~/lost circle/i)`
      - Player: "Interested Monk"
        - NPC say: Then venture to the lands of evil. The swamps of the trolls and ogres. There, seek out a monk called Raster. He has the idol. You will return here and wait for my reappearance. When we meet again, you shall hand me the idol and a red sash earned from the Ashen Order. Do so and you shall be closer to joining the brotherhood.
        - Condition: `($text=~/interested monk/i)`
      - Player: "Idol Of Zan Fi" (link: explicit mention)
        - Prompted by player input: "Lost Circle"
        - NPC say: The idol of Zan Fi is a totem that is sacred to our brotherhood. I cannot share its secrets, but I can offer to you a reward for its return. Are you an [interested monk]?
        - Condition: `($text=~/idol of zan fi/i)`
      - Player: "Brother Qwinn" (link: explicit mention)
        - Prompted by player input: "Lost Circle"
        - NPC say: Brother Qwinn is searching for one who can return the [Code of the Whistling Fist]. I believe he is in the vicinity of the Plains of Karana.
        - Condition: `($text=~/brother qwinn/i)`
      - Player: "Code Of The Whistling Fist" (link: explicit mention)
        - NPC say: The tome called the Code of the Whistling Fist has been stolen from [Brother Qwinn]. It contains many secrets pertaining to our brotherhood. Thankfully, it is magically locked and only a Zan Fi master could unlock it. Still, Qwinn must see its safe return.
        - Condition: `($text=~/code of the whistling fist/i)`
      - Player: "Return The Sash" (link: external event mention)
        - Prompted by `event_item`:
          - NPC say: We thank you for the return of the idol of Zan Fi. Take this rare robe pattern. You shall find it useful should you aid [Brother Qwinn] in his quest. His item, the rare robe pattern, a swatch of shadow silk and a scroll containing Jonathan's Whistling Warsong. Into a sewing kit they will be going. And into the brotherhood will you. I hope you do not wish me to [return the sash].
          - Event guard: `(plugin::check_handin(\%itemcount, 12317 => 1, 10133 => 1))`
        - NPC say: Very well. Give to me that which you have been rewarded or the robe, if you have a tailored one.
        - Condition: `($text=~/return the sash/i)`
52. Buy "Song: Jonthan's Whistling Warsong" (15734) from "Lysric Loresinger" (NPC 1035) in `qeynos`. Base price: 43 copper.
53. Buy "Needle Mold" (12019) from "Dyona Rossook" (NPC 5065) in `highpass`. Base price: 180 copper.
54. Buy "Thimble Mold" (12057) from "Dyona Rossook" (NPC 5065) in `highpass`. Base price: 180 copper.
55. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
    - Dialogue with erudnext/"Lumi Stergnon":
      - Player: "Hail"
        - NPC say: Peace and tranquility be with you. . Are you a [new acolyte of peace] or are you [here to pay homage] to the child of tranquility?
        - Condition: `(e.message:findi("hail"))`
      - Player: "New Acolyte Of Peace" (link: explicit mention)
        - NPC say: Then you shall learn the ways of Quellious and learn to do as you are told by higher ranking members. It is time for you to do the lesser duties of a young priest. Which will it be? [Retrieve the Peacekeeper staffs] or [battle the undead]?
        - Condition: `(e.message:findi("new acolyte of peace"))`
      - Player: "retrieve the Peacekeeper staffs" (link: explicit mention)
        - NPC say: Then take this note to the woodworker in Toxxulia Forest. His name is Emil Parsini. He shall have the staff to be returned to the temple.
        - Condition: `(e.message:findi("retrieve the Peacekeeper staffs"))`
        - Gives Sealed Letter (18833).
      - Player: "Battle The Undead" (link: explicit mention)
        - Prompted by player input: "New Acolyte Of Peace"
        - NPC say: Then you shall venture to Toxxulia Forest. There has been an increase in skeleton sightings lately. I do not know their origin, but I believe that your efforts will reduce their numbers! Take this box. Return it to me when you have filled it with the bones of these undead creatures and combined it. May Quellious' light guide you.
        - Condition: `(e.message:findi("battle the undead"))`
        - Gives Box For Bones (17941).
      - Player: "Important Missions" (link: external event mention)
        - Prompted by `event_trade`:
          - NPC say: You have done well, neophyte.Let me add the touch of harmony to finish the job.. Here, then. Take these supplies. I am sure you'll need them. Soon you may be able to assist us in [important missions].
          - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 13816}))`
        - NPC say: We have need of skilled priests. We have learned that a High Guard battle staff has been stolen. We require a priest to [track down the staff].
        - Condition: `(fac <= 4)`
        - Condition: `(e.message:findi("important missions"))`
      - Player: "Here To Pay Homage" (link: explicit mention)
        - Prompted by player input: "Hail"
        - NPC say: Then respect our temple and keep your prayers silent.
        - Condition: `(fac <= 4)`
        - Condition: `(e.message:findi("here to pay homage"))`
56. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). The combine does not fail.
57. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
    - Dialogue with qeynos/"Wolten Grafe":
      - Player: "Hail"
        - NPC say: Hail, noble . Remember to spread the words of Karana throughout the faraway lands on which you shall tread. We of the Temple of Thunder are looking for new members - good people who [wish to join our cause]. Let the call go out!
        - Condition: `(e.message:findi("hail"))`
      - Player: "Join The Cause" (link: conversation sequence)
        - NPC say: That IS good news! If you walk the righteous path of the Rainkeeper, Karana, then you are truly noble. I have need of someone like that. I must find someone to perform a [dangerous mission] or perhaps you would rather seek out the [Rat King] or [crush the undead].
        - Condition: `(e.message:findi("join the cause"))`
      - Player: "Crush The Undead" (link: explicit mention)
        - NPC say: Those who passed generations ago have had their bones exhumed and enchanted. Some evil force plagues this land with these evil skeletons. You will fight for us and crush the skeletons. Take this box and fill it with the bones of those creatures. We will not allow them to rise again and you shall earn our respect. Go forth and fight for Karana!
        - Condition: `(e.message:findi("crush the undead"))`
        - Gives Box For Bones (17941).
      - Player: "Dangerous Mission" (link: explicit mention)
        - Prompted by player input: "Join The Cause"
        - NPC say: You must go into the catacombs and find a man named Drosco Finlayer. Pass him this note. He has been deep undercover in the Shrine of Bertoxxulous and will have directions to that vile place. To do this will surely show your allegiance to this temple.
        - Condition: `(e.message:findi("dangerous mission"))`
        - Gives Tattered Note (18804).
      - Player: "Rat King" (link: explicit mention)
        - Prompted by player input: "Join The Cause"
        - NPC say: You may try, but no one has truly seen him. I would look in the sewers.
        - Condition: `(e.message:findi("rat king"))`
58. **Broken:** nothing in the graph gives, loots, spawns, or combines Notice to Cease and Desist (9590).
59. Hand "Notice to Cease and Desist" (9590) to freeporteast/"Lythe Songbird". Spawns "a Freeport guard" (382255). Loot "Fine Steel Two Handed Sword" (5351) from "a Freeport guard".
60. Alternative: Loot "Fine Steel Two Handed Sword" (5351) from "a seasoned Freeport guard" (NPC 382256) in `freeporteast`; trigger: freeporteast/"Lythe Songbird", hand "Notice to Cease and Desist" (9590).
61. Alternative: Loot "Fine Steel Two Handed Sword" (5351) from "a Freeport guard" (NPC 382255) in `freportw`; trigger: freportw/"Lythe Songbird", hand "Notice to Cease and Desist" (9590).
62. Alternative: Loot "Fine Steel Two Handed Sword" (5351) from "a seasoned Freeport guard" (NPC 382256) in `freportw`; trigger: freportw/"Lythe Songbird", hand "Notice to Cease and Desist" (9590).
63. Alternative: Loot "Fine Steel Two Handed Sword" (5351) from "a minion of Meldrath" (NPC 56173) in `steamfont`; trigger: steamfont/"Meldraths Paige", say "We Shall Never Surrender".
64. Alternative: Loot "Fine Steel Two Handed Sword" (5351) from "Meldrath's melded minions" (NPC 56174) in `steamfont`; trigger: steamfont/"Meldraths Paige", say "Your Forces Are Deafeated".
65. Alternative: Loot "Fine Steel Two Handed Sword" (5351) from "Arnold the Gnomeinator" (NPC 56175) in `steamfont`; trigger: steamfont/"Meldraths Paige", say "You Shall Not Break Our Defense".
66. Alternative: Loot "Fine Steel Two Handed Sword" (5351) from "a Freeport guard" (NPC 382255) in `freeporteast`; trigger: freeporteast/"Lythe Songbird", on timer guard.
67. Alternative: Loot "Fine Steel Two Handed Sword" (5351) from "a seasoned Freeport guard" (NPC 382256) in `freeporteast`; trigger: freeporteast/"Lythe Songbird", on timer guard.
68. Alternative: Loot "Fine Steel Two Handed Sword" (5351) from "a Freeport guard" (NPC 382255) in `freportw`; trigger: freportw/"Lythe Songbird", on timer guard.
69. Alternative: Loot "Fine Steel Two Handed Sword" (5351) from "a seasoned Freeport guard" (NPC 382256) in `freportw`; trigger: freportw/"Lythe Songbird", on timer guard.
70. Combine in Forge (17): "Fine Steel Two Handed Sword" (5351), "Water Flask" (13006). Produces "Small Brick of High Quality Ore" (10468) x2, "Small Piece of High Quality Ore" (22229). Requires Blacksmithing, trivial 21.
71. Combine in Royal Qeynos Forge (40): "Small Piece of High Quality Ore" (22229), "Water Flask" (13006). Produces "High Quality Metal Bits" (22230). Requires Blacksmithing, trivial 20.
72. Combine in Vale Forge (49): "Needle Mold" (12019), "Thimble Mold" (12057), "Water Flask" (13006), "High Quality Metal Bits" (22230). Produces "Vale Sewing Kit" (92882). Requires Blacksmithing, trivial 162.
73. Loot "Shadow Wolf Pelt" (13779) from "A Shadow Wolf" (NPC 408093) in `commonlands`. Drop cache: 7.64% chance per kill.
74. Buy "Spell: Gather Shadows" (15522) from "Tagus Wunne" (NPC 10030) in `freporte`. Base price: 43 copper.
75. Forage "Spider Silk" (13041) in `mistmoore`.
76. Forage "Spider Silk" (13041) in `mmca`.
77. Forage "Spider Silk" (13041) in `mmcb`.
78. Forage "Spider Silk" (13041) in `mmcc`.
79. Forage "Spider Silk" (13041) in `mmcd`.
80. Forage "Spider Silk" (13041) in `mmce`.
81. Forage "Spider Silk" (13041) in `mmcf`.
82. Forage "Spider Silk" (13041) in `mmcg`.
83. Forage "Spider Silk" (13041) in `mmch`.
84. Forage "Spider Silk" (13041) in `mmci`.
85. Forage "Spider Silk" (13041) in `mmcj`.
86. Combine in "Vale Sewing Kit" (92882): "Spider Silk" (13041). Produces "Silk Swatch" (16482). Requires Tailoring, trivial 15. The combine does not fail.
87. Combine in "Vale Sewing Kit" (92882): "Shadow Wolf Pelt" (13779), "Spell: Gather Shadows" (15522), "Silk Swatch" (16482). Produces "Shadow Silk" (16483). Requires Tailoring, trivial 36.
88. Combine in "Deluxe Sewing Kit" (17966): "Needle of the Void" (12314), "Rare Robe Pattern" (12315), "Song: Jonthan's Whistling Warsong" (15734), "Shadow Silk" (16483). Produces "Robe of the Lost Circle" (12256). Requires Tailoring. The combine does not fail.
89. dreadlands/"Brother Balatin", hand "Robe of the Lost Circle" (12256) + "Metal Pipe" (12979) + "Metal Pipe" (12980). Gives "Robe of the Whistling Fists" (12970).
    - Dialogue with dreadlands/"Brother Balatin":
      - Player: "Hail"
        - NPC say: What discipline do you follow?
        - Condition: `($text=~/hail/i)`
      - Player: "Lost Circle" (link: conversation sequence)
        - NPC say: Then we are one. The rebirth of our circle shall start with you. I have waited decades for your arrival. You should seek the living brothers within Tunaria. When you have earned your garb then you will be ready for the [true drape].
        - Condition: `($text=~/lost circle/i)`
      - Player: "True Drape" (link: explicit mention)
        - NPC say: Seek the broken flute of our master. Taken from us by the Iksar twins of Vistrei. To me they will come and to me your robe and you will come the dawning of the new brotherhood.
        - Condition: `($text=~/true drape/i)`
90. Loot "Immortals" (18195) from "Faerie of Dismay" (NPC 91012) in `skyfire`. Drop cache: 35% chance per kill.
91. erudnext/"Tomekeeper Danl", hand "Immortals" (18195). Gives "Danl's Reference" (1682).
    - Dialogue with erudnext/"Tomekeeper Danl":
      - Player: "Hail"
        - NPC say: Good day, citizen. Please remember to keep your voice down in our library. Feel free to browse the extensive collection of books we have on display. Learning is all about you. Our library is the greatest collection of educational literature in the world, as you can no doubt see. If you come across any [rare finds] we may be interested in purchasing them.
        - Condition: `(e.other:GetLevel() >= 46 and e.other:Class() == "Monk")`
        - Condition: `(e.message:findi("hail"))`
      - Player: "Rare Find" (link: explicit mention)
        - NPC say: Yes, any rare books, tomes, essays, or other literature you find may be of interest to me. Although the finds I am interested in are quite high profile and would most likely only be found in the possession of very powerful or influential beings. Give me what you find and I will pay you what it is worth to us.
        - Condition: `(e.other:GetLevel() >= 46 and e.other:Class() == "Monk")`
        - Condition: `(e.message:findi("rare find"))`
      - Player: "Lheao" (link: external event mention)
        - Prompted by `event_trade`:
          - NPC say: gasps at the sight of the rare book. 'This is a great find indeed! I can only imagine who you had to.. persuade to give you the book. Our library would be very interested in acquiring this and I am prepared to give you this referral that marks you as a friend of the library. If only [Lheao] could see this.'
          - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 18195}) and e.other:GetLevel() >= 46 and e.other:Class() == "Monk")`
        - NPC say: Lheao was my predecessor here at the library of Erudin. He has since retired, just a few years ago. Im sure he would be most impressed with your find and other insightful conversation on the subject. Although Im not sure one of your profession would be interested in such a scholarly endeavor, no offense. If you are interested, find him and tell him you found the book Immortals. Im not sure where he has retired to, but I hear it is near an ocean somewhere.
        - Condition: `(e.other:GetLevel() >= 46 and e.other:Class() == "Monk")`
        - Condition: `(e.message:findi("lheao"))`
      - Player: "Power Of The Immortals" (link: conversation sequence)
        - NPC say: Power of the Immortals? Hmmm. . .well of course I know about that, but at the moment I have more pressing issues at hand. I'm sorry I could not be of more help, but maybe after my assistant has returned I can help you.
        - Condition: `(e.other:GetLevel() >= 46 and e.other:Class() == "Monk")`
        - Condition: `(qglobals["monk_epic"] ~= nil and qglobals["monk_epic"] >= "2" and e.message:findi("power of the immortals"))`
      - Player: "disciple of Kaiaren" (link: external event mention)
        - Prompted by `event_trade`:
          - NPC say: Well I suppose I do owe you the information you had come here seeking. Unfortunately, I do not know much more than what is in this book already. The other references I have found do speak of another [disciple of Kaiaren].
          - Event guard: `(qglobals["monk_epic"] ~= nil and qglobals["monk_epic"] >= "2" and item_lib.check_turn_in(e.trade, {item1 = 48132}))`
        - NPC say: It is unknown to many that Kaiaren had another student before Vorash. He was a disciple that wanted to learn the true power of mind and body. Sage Kaiaren had so much respect for him that he decided that he was going to take Kaiaren's place among the Order of the Celestial Fists when it was his turn to choose a new member. This disciple's name was [Vortix].
        - Condition: `(e.other:GetLevel() >= 46 and e.other:Class() == "Monk")`
        - Condition: `(qglobals["monk_epic"] ~= nil and qglobals["monk_epic"] >= "3" and e.message:findi("disciple of Kaiaren"))`
      - Player: "Vortix" (link: explicit mention)
        - NPC say: When Vortix was training with Kaiaren, he learned many techniques that Vorash never had time to learn because of Kaiaren's suspicions of him. The only soul that may know of these lost disciplines is Vortix. Unfortunately, he went into hiding shortly after Kaiaren's battle with Vorash. He became a coward hiding from the public and began to write himself out of history to live the life of an outcast. If he cannot be found you can also find his [book].
        - Condition: `(e.other:GetLevel() >= 46 and e.other:Class() == "Monk")`
        - Condition: `(qglobals["monk_epic"] ~= nil and qglobals["monk_epic"] >= "3" and e.message:findi("vortix"))`
      - Player: "Book" (link: explicit mention)
        - NPC say: Well I shouldn't say book. It was really a diary of sorts. Kaiaren wrote a diary and it contained all of his disciplines. There may also be a way to reverse the effects of Vorash's attacks located within it. Unfortunately, Vortix would also be the only one that would know the diary's location. Go now and try to locate Vortix and ask him [where Kaiaren's diary] may be. Who referred you to me in the first place? Maybe he knows more than he appears to. I remember that Vortix will only address those that call to him by name.
        - Condition: `(e.other:GetLevel() >= 46 and e.other:Class() == "Monk")`
        - Condition: `(qglobals["monk_epic"] ~= nil and qglobals["monk_epic"] >= "3" and e.message:findi("book"))`
      - Player: "Hail" (link: conversation sequence)
        - NPC say: Good day, citizen. Please remember to keep your voice down in our library. Feel free to browse the extensive collection of books we have on display. Learning is all about you. Our library is the greatest collection of educational literature in the world, as you can no doubt see. Return to me again when you are an experienced monk.
        - Condition: ``
        - Condition: `(e.message:findi("hail"))`
92. timorous/"Lheao", hand "Danl's Reference" (1682) + "Robe of the Whistling Fists" (12970). Gives "Celestial Fists" (1683).
    - Dialogue with timorous/"Lheao":
      - Player: "Hail"
        - NPC emote: jumps at your voice and begins laughing at his skittishness.
        - NPC say: Ahh, hello there. Not many people know of this place, so visitors are quite rare. Hehehe. Its a very beautiful place indeed, so.. ummm, dont go telling everyone you know about it. Heheh. Thanks, Friend.
        - Condition: `($text=~/hail/i)`
      - Player: "I Have Found The Book Of Immortals" (link: conversation sequence)
        - NPC emote: looks up at you, eyes wide in astonishment.
        - NPC say: My god, you found Immortals?! Where did you find it? Nevermind, that is unimportant. I have in my possession a book that explains more of these individuals. Its value is unimaginable as well as the impact it is capable of. As you can see, I grow old. I need an individual to watch over this book and make sure it is protected. Would you be willing to take this [responsibility]?
        - Condition: `($text=~/i have found the book of immortals/i)`
      - Player: "Responsibility" (link: explicit mention)
        - NPC say: Im sorry, $name, but I could only give this book to a true master, such as a member of the Whistling Fists Order. And unless you can give me proof that you are one, in addition to Danls reference, which is very unlikely, there is no way I'll let you take charge of the [Celestial Fists].
        - Condition: `($text=~/responsibility/i)`
      - Player: "Celestial Fists" (link: explicit mention)
        - NPC say: The Celestial Fists is the title of a book written by an unknown author. His writing is sub par but the legend is interesting from a biographical standpoint alone. Its rarity commands top dollar in the scholarly community but the secrets revealed in the book are what truely makes it dangerous. I hope Im able to find someone to watch over it soon.
        - Condition: `($text=~/celestial fists/i)`
93. Hand "Celestial Fists" (1683) to trakanon/"Kaiaren". Spawns "Kaiaren (True)" (95183). Loot "Rune of Cascade" (65270) from "Kaiaren (True)".
94. Alternative: Loot "Rune of Cascade" (65270) from "A Black Reaver" (NPC 90004) in `citymist`; trigger: citymist/"A Black Reaver", on event_death_complete.
95. Alternative: Loot "Rune of Cascade" (65270) from "A Black Reaver" (NPC 90005) in `citymist`; trigger: citymist/"A Black Reaver", on event_death_complete.
96. Alternative: Loot "Rune of Cascade" (65270) from "A Black Reaver" (NPC 90192) in `citymist`; trigger: citymist/"A Black Reaver", on event_death_complete.
97. Alternative: Loot "Rune of Cascade" (65270) from "An Ancient Thought Horror" (NPC 164122) in `thedeep`; trigger: thedeep/"Ancient Thought Horror Trap", on enter.
98. Say "Spawnwave" to cazicthule/"Avatar Of Fear".
99. Spawns "a Tentacle Terror" (48252).
100. Loot "Rune of Coruscation" (16631) from "a Tentacle Terror".
101. sleeper/"Master Of The Guard", on event combat.
102. Starts timer `spawn`.
103. Spawns "A Newly Created Sentry" (128014) after `sleeper/master of the guard#timer:spawn`.
104. Loot "Rune of Flash" (65279) from "A Newly Created Sentry".
105. Alternative: Loot "Rune of Flash" (65279) from "An Erratic Arachnid" (NPC 215460) in `poair`; trigger: poair/"Dust Trigger", on event_signal.
106. Alternative: Loot "Rune of Flash" (65279) from "An Erratic Arachnid" (NPC 215460) in `poair`; trigger: poair/"An Erratic Arachnid", on event_death_complete.
107. Alternative: Loot "Rune of Flash" (65279) from "A Noc Havocblade" (NPC 281130) in `qinimi`; trigger: qinimi/"Trigger Qinimi 2", on event_signal.
108. Alternative: Loot "Rune of Flash" (65279) from "A Ra'Tuk Skullstriker" (NPC 281131) in `qinimi`; trigger: qinimi/"Trigger Qinimi 2", on event_signal.
109. Alternative: Loot "Rune of Flash" (65279) from "A Kyv Bloodhunter" (NPC 281139) in `qinimi`; trigger: qinimi/"Execution", say "I Wish To Enter".
110. Alternative: Loot "Rune of Flash" (65279) from "A Kyv Bloodhunter" (NPC 281140) in `qinimi`; trigger: qinimi/"Execution", say "I Wish To Enter".
111. Alternative: Loot "Rune of Flash" (65279) from "A Kyv Bloodhunter" (NPC 281141) in `qinimi`; trigger: qinimi/"Execution", say "I Wish To Enter".
112. Alternative: Loot "Rune of Flash" (65279) from "A Crystal Shard" (NPC 112046) in `velketor`; trigger: velketor/"A Chill", on event_combat.
113. Alternative: Loot "Rune of Flash" (65279) from "A Crystal Shard" (NPC 112046) in `velketor`; trigger: velketor/"A Stalagtite", on event_combat.
114. Alternative: Loot "Rune of Flash" (65279) from "A Crystal Shard" (NPC 112046) in `velketor`; trigger: velketor/"A Tentacle", on event_combat.
115. Alternative: Loot "Rune of Flash" (65279) from "A Crystal Shard" (NPC 112046) in `velketor`; trigger: velketor/"From No Where", on event_combat.
116. Alternative: Loot "Rune of Flash" (65279) from "A Crystal Shard" (NPC 112046) in `velketor`; trigger: velketor/"Ice", on event_combat.
117. Alternative: Loot "Rune of Flash" (65279) from "A Crystal Shard" (NPC 112046) in `velketor`; trigger: velketor/"Something Seems", on event_combat.
118. Alternative: Loot "Rune of Flash" (65279) from "A Crystal Shard" (NPC 112046) in `velketor`; trigger: velketor/"The Hair", on event_combat.
119. Alternative: Loot "Rune of Flash" (65279) from "A Crystal Shard" (NPC 112046) in `velketor`; trigger: velketor/"The Walls", on event_combat.
120. Alternative: Loot "Rune of Flash" (65279) from "A Crystal Shard" (NPC 112046) in `velketor`; trigger: velketor/"You Are", on event_combat.
121. Alternative: Loot "Rune of Flash" (65279) from "A Kyv Bloodhunter" (NPC 281139) in `qinimi`; trigger: qinimi/"Execution", on timer startevent.
122. Alternative: Loot "Rune of Flash" (65279) from "A Kyv Bloodhunter" (NPC 281140) in `qinimi`; trigger: qinimi/"Execution", on timer startevent.
123. Alternative: Loot "Rune of Flash" (65279) from "A Kyv Bloodhunter" (NPC 281141) in `qinimi`; trigger: qinimi/"Execution", on timer startevent.
124. lavastorm/"Talwyn Flamecaller", say "Hail". Sets `wiz_epic_pre` to `1`.
125. lavastorm/"Talwyn Flamecaller", say "Test Of Intelligence". Sets `wiz_test_intel` to `1`.
126. Ground spawn of "Empty Jug" (11425) in `katta`.
127. lavastorm/"Talwyn Flamecaller", hand "Empty Jug" (11425). Sets `wiz_test_intel` to `2`.
128. Ground spawn of "Emerald-Tipped Staff" (11419) in `beholder`.
129. lavastorm/"Talwyn Flamecaller", hand "Emerald-Tipped Staff" (11419). Sets `wiz_test_intel` to `3`.
130. Ground spawn of "Meditation Basket" (11282) in `warslikswood`.
131. lavastorm/"Talwyn Flamecaller", hand "Meditation Basket" (11282). Sets `wiz_test_intel` to `4`.
132. Ground spawn of "Platinum Token" (11433) in `pojustice`.
133. lavastorm/"Talwyn Flamecaller", hand "Platinum Token" (11433). Sets `wiz_test_intel` to `5`.
134. Ground spawn of "White Sash" (11413) in `letalis`.
135. lavastorm/"Talwyn Flamecaller", hand "White Sash" (11413). Sets `wiz_test_intel` to `6`.
136. Ground spawn of "Golden Dagger" (11424) in `skyfire`.
137. lavastorm/"Talwyn Flamecaller", hand "Golden Dagger" (11424). Sets `wiz_test_intel` to `7`.
138. Ground spawn of "Ivory Bone" (11436) in `gunthak`.
139. lavastorm/"Talwyn Flamecaller", hand "Ivory Bone" (11436). Sets `wiz_test_intel` to `8`.
140. Ground spawn of "Red Cloth" (11418) in `maiden`.
141. lavastorm/"Talwyn Flamecaller", hand "Red Cloth" (11418). Sets `wiz_test_intel` to `9`.
142. Fish "Worn Turban" (11299) in `potranquility`.
143. lavastorm/"Talwyn Flamecaller", hand "Worn Turban" (11299). Sets `wiz_test_intel` to `10`.
144. Ground spawn of "Old Pipe" (11412) in `cauldron`.
145. lavastorm/"Talwyn Flamecaller", hand "Old Pipe" (11412). Requires `wiz_test_intel` ==10. Gives "Rune of Greater Desiccation" (11439).
146. Kill citymist/"A Black Reaver". Spawns "A Black Reaver" (90004).
147. Loot "Rune of Glint" (65281) from "A Black Reaver".
148. Alternative: Loot "Rune of Glint" (65281) from "A Black Reaver" (NPC 90005) in `citymist`; trigger: citymist/"A Black Reaver", on event_death_complete.
149. Alternative: Loot "Rune of Glint" (65281) from "A Black Reaver" (NPC 90192) in `citymist`; trigger: citymist/"A Black Reaver", on event_death_complete.
150. Alternative: Loot "Rune of Glint" (65281) from "A Shadowy Figure" (NPC 163190) in `griegsend`; trigger: griegsend/"Trapman Two", on event_combat.
151. Alternative: Loot "Rune of Glint" (65281) from "An Ancient Thought Horror" (NPC 164122) in `thedeep`; trigger: thedeep/"Ancient Thought Horror Trap", on enter.
152. Alternative: Loot "Rune of Glint" (65281) from "A Ra'Tuk Decimator" (NPC 289004) in `tipt`; trigger: tipt/"Zone Status", say "Spawn Keyroom".
153. Ground spawn of "Icon of the High Scale" (1671) in `citymist`.
154. Hand "Icon of the High Scale" (1671) to hole/"High Scale Kirn". Spawns "High Scale Kirn" (39083). Loot "Engraved Ring" (1681) from "High Scale Kirn".
155. Hand "Engraved Ring" (1681) to citymist/"Neh-Ashiir". Spawns "Neh'Ashir" (90181). Loot "Rune of Impulse" (65282) from "Neh'Ashir".
156. Alternative: Loot "Rune of Impulse" (65282) from "a Tae Ew disciple" (NPC 48026) in `cazicthule`; trigger: cazicthule/"Trap Disc", on event_combat.
157. Alternative: Loot "Rune of Impulse" (65282) from "Lhranc" (NPC 90187) in `citymist`; trigger: citymist/"Lhranc", hand "Corrupted Ghoulbane" (14367) + "Heart of the Innocent" (14368) + "Head of the Valiant" (14369) + "Will of Innoruuk" (14370).
158. Alternative: Loot "Rune of Impulse" (65282) from "Neh'Ashir" (NPC 90184) in `citymist`; trigger: citymist/"90000", on event_death_complete.
159. Alternative: Loot "Rune of Impulse" (65282) from "Neh'Ashiir" (NPC 90184) in `citymist`; trigger: citymist/"A Black Reaver", on event_death_complete.
160. Alternative: Loot "Rune of Impulse" (65282) from "Pxet Elite Blademaster" (NPC 284039) in `ferubi`; trigger: ferubi/"Event Spawner", on event_signal.
161. Alternative: Loot "Rune of Impulse" (65282) from "Pxet Elite Spearmaster" (NPC 284091) in `ferubi`; trigger: ferubi/"Event Spawner", on event_signal.
162. Alternative: Loot "Rune of Impulse" (65282) from "A Soldier Of Madness" (NPC 163185) in `griegsend`; trigger: griegsend/"Trapman", on event_combat.
163. Alternative: Loot "Rune of Impulse" (65282) from "A Devastating Pooka" (NPC 289037) in `tipt`; trigger: tipt/"Rikabi The Riddler", say "Spawn Devastating Pookas".
164. Alternative: Loot "Rune of Impulse" (65282) from "A Ra'Tuk Decimator" (NPC 289004) in `tipt`; trigger: tipt/"Zone Status", say "Spawn Keyroom".
165. Alternative: Loot "Rune of Impulse" (65282) from "A Trusik Anchorite" (NPC 292029) in `uqua`; trigger: uqua/"Trap Uqua 1", on enter.
166. Alternative: Loot "Rune of Impulse" (65282) from "A Trusik Summoner" (NPC 292002) in `uqua`; trigger: uqua/"Trap Uqua 1", on enter.
167. Alternative: Loot "Rune of Impulse" (65282) from "A Trusik Anchorite" (NPC 292029) in `uqua`; trigger: uqua/"Trap Uqua 2", on enter.
168. Alternative: Loot "Rune of Impulse" (65282) from "A Trusik Summoner" (NPC 292002) in `uqua`; trigger: uqua/"Trap Uqua 2", on enter.
169. Alternative: Loot "Rune of Impulse" (65282) from "A Trusik Anchorite" (NPC 292029) in `uqua`; trigger: uqua/"Trap Uqua 3", on enter.
170. Alternative: Loot "Rune of Impulse" (65282) from "A Trusik Summoner" (NPC 292002) in `uqua`; trigger: uqua/"Trap Uqua 3", on enter.
171. Alternative: Loot "Rune of Impulse" (65282) from "A Trusik Anchorite" (NPC 292029) in `uqua`; trigger: uqua/"Trap Uqua 4", on enter.
172. Alternative: Loot "Rune of Impulse" (65282) from "A Trusik Summoner" (NPC 292002) in `uqua`; trigger: uqua/"Trap Uqua 4", on enter.
173. Alternative: Loot "Rune of Impulse" (65282) from "A Trusik Anchorite" (NPC 292029) in `uqua`; trigger: uqua/"Trap Uqua 5", on enter.
174. Alternative: Loot "Rune of Impulse" (65282) from "A Trusik Summoner" (NPC 292002) in `uqua`; trigger: uqua/"Trap Uqua 5", on enter.
175. Alternative: Loot "Rune of Impulse" (65282) from "A Trusik Anchorite" (NPC 292029) in `uqua`; trigger: uqua/"Trap Uqua 6", on enter.
176. Alternative: Loot "Rune of Impulse" (65282) from "A Trusik Summoner" (NPC 292002) in `uqua`; trigger: uqua/"Trap Uqua 6", on enter.
177. Alternative: Loot "Rune of Impulse" (65282) from "A Trusik Anchorite" (NPC 292029) in `uqua`; trigger: uqua/"Trap Uqua 7", on enter.
178. Alternative: Loot "Rune of Impulse" (65282) from "A Trusik Summoner" (NPC 292002) in `uqua`; trigger: uqua/"Trap Uqua 7", on enter.
179. Alternative: Loot "Rune of Impulse" (65282) from "A Trusik Anchorite" (NPC 292029) in `uqua`; trigger: uqua/"Trap Uqua 8", on enter.
180. Alternative: Loot "Rune of Impulse" (65282) from "A Trusik Summoner" (NPC 292002) in `uqua`; trigger: uqua/"Trap Uqua 8", on enter.
181. Alternative: Loot "Rune of Impulse" (65282) from "Pixtt Votal" (NPC 284079) in `ferubi`; trigger: ferubi/"Zun-Muram Votal", on timer popadds.
182. Alternative: Loot "Rune of Impulse" (65282) from "Pixtt Votal" (NPC 284103) in `ferubi`; trigger: ferubi/"Zun-Muram Votal", on timer popadds.
183. Alternative: Loot "Rune of Impulse" (65282) from "Tiv Prayer Chanter" (NPC 297066) in `txevu`; trigger: txevu/"Highpriest", on event spawn:297199.
184. Alternative: Loot "Rune of Impulse" (65282) from "Tiv Prayer Chanter" (NPC 297062) in `txevu`; trigger: txevu/"Highpriest", on event spawn:297061.
185. Alternative: Loot "Rune of Impulse" (65282) from "Tiv Prayer Chanter" (NPC 297063) in `txevu`; trigger: txevu/"Highpriest", on event spawn:297197.
186. Alternative: Loot "Rune of Impulse" (65282) from "Tiv Prayer Chanter" (NPC 297064) in `txevu`; trigger: txevu/"Highpriest", on event spawn:297059.
187. Alternative: Loot "Rune of Impulse" (65282) from "Tiv Prayer Chanter" (NPC 297065) in `txevu`; trigger: txevu/"Highpriest", on event spawn:297057.
188. Say "Spawn Devastating Pookas" to tipt/"Rikabi The Riddler".
189. Spawns "A Devastating Pooka" (289037).
190. Loot "Rune of Synergy" (65289) from "A Devastating Pooka".
191. Alternative: Loot "Rune of Synergy" (65289) from "A Cragbeast Hatchling" (NPC 289034) in `tipt`; trigger: tipt/"Cragbeasts", say "Spawn Hatchlings".
192. Spawns "a Tae Ew Justicar" (48029) in `cazicthule` on event_spawn.
193. Loot "Rune of Tempest" (65291) from "a Tae Ew Justicar".
194. Alternative: Loot "Rune of Tempest" (65291) from "A Swirling Ooze" (NPC 48001) in `cazicthule`; trigger: cazicthule/"An Acidic Mass", on event_hp.
195. Alternative: Loot "Rune of Tempest" (65291) from "a Tae Ew disciple" (NPC 48026) in `cazicthule`; trigger: cazicthule/"Trap Disc", on event_combat.
196. Alternative: Loot "Rune of Tempest" (65291) from "a Tae Ew proselyte" (NPC 48007) in `cazicthule`; trigger: cazicthule/"Trap Pros", on event_combat.
197. Alternative: Loot "Rune of Tempest" (65291) from "a Tae Ew warrior" (NPC 48076) in `cazicthule`; trigger: cazicthule/"Trap War", on event_combat.
198. Alternative: Loot "Rune of Tempest" (65291) from "A Revived Sarnak" (NPC 277008) in `chardokb`; trigger: chardokb/, on event_combat.
199. Alternative: Loot "Rune of Tempest" (65291) from "An Iksar Skeleton" (NPC 277032) in `chardokb`; trigger: chardokb/, on event_combat.
200. Alternative: Loot "Rune of Tempest" (65291) from "Servant Of The Magistrate" (NPC 163189) in `griegsend`; trigger: griegsend/"Trapman Two", on event_combat.
201. Alternative: Loot "Rune of Tempest" (65291) from "A Devastating Pooka" (NPC 289037) in `tipt`; trigger: tipt/"Rikabi The Riddler", say "Spawn Devastating Pookas".
202. Alternative: Loot "Rune of Tempest" (65291) from "A Ra'Tuk Decimator" (NPC 289004) in `tipt`; trigger: tipt/"Zone Status", say "Spawn Keyroom".
203. Spawns "An Ooze" (48004) in `cazicthule` on event_hp.
204. Loot "Rune of Vortex" (65293) from "An Ooze".
205. Alternative: Loot "Rune of Vortex" (65293) from "A Shadowy Figure" (NPC 163190) in `griegsend`; trigger: griegsend/"Trapman Two", on event_combat.
206. Alternative: Loot "Rune of Vortex" (65293) from "A Ra'Tuk Decimator" (NPC 289004) in `tipt`; trigger: tipt/"Zone Status", say "Spawn Keyroom".
207. Loot "Rune of Greater Conflagration" (11442) from "Shar Vinitras" in `akheva`.
208. Combine in "Spell Research Kit" (93492): "Rune of Cascade" (65270), "Rune of Coruscation" (16631), "Rune of Flash" (65279), "Rune of Greater Desiccation" (11439), "Rune of Glint" (65281), "Rune of Impulse" (65282), "Rune of Synergy" (65289), "Rune of Tempest" (65291), "Rune of Vortex" (65293), "Rune of Greater Conflagration" (11442). Produces "Spell: Electrical Charge" (16623). Requires Research, trivial 190. The combine does not fail.

### "Note to Arantir" (18168)

1. halas/"Arantir Karondor", say "Gnome". Gives "Note from Arantir" (18169).
2. butcher/"Kandin Firepot", hand "Note from Arantir" (18169). Sets `wizepicK` to `1`.
3. butcher/"Kandin Firepot", say "What Oil". Requires `wizepicK` set. Gives "Golem Sprocket" (14319).
4. Hand "Golem Sprocket" (14319) to fearplane/"A Broken Golem". Spawns "An Enraged Golem" (72106). Loot "Green Oil" (14349) from "An Enraged Golem".
5. butcher/"Kandin Firepot", hand "Green Oil" (14349). Gives "Note to Arantir" (18168).

### "Arantir's Ring" (14335)

1. halas/"Arantir Karondor", say "Hail". Gives "Arantir's Ring" (14334).
2. felwithea/"Challice", hand "Arantir's Ring" (14334). Gives "Arantir's Ring" (14335).
    - Dialogue with felwithea/"Challice":
      - Player: "Hail"
        - NPC say: You! Remove yourself from my presence! Do you not know to whom you speak? My husband is a very powerful noble and if you do not do as I say. he will have your head!
        - Condition: `(e.message:findi("hail"))`

### "Silken Tapestry Satchel" (12596)

1. Summon "Collapsible Sewing Kit" (17165) by casting "Unfold Sewing Kit".
2. Buy "Backpack Pattern" (12089) from "Iala Lenard" (NPC 1141) in `qeynos`. Base price: 500 copper.
3. Acquisition of "Vale Sewing Kit" (92882) is documented under "Spell: Electrical Charge" (16623); obtain another copy if needed.
4. **Broken:** no event trigger found for `misty/misty#timer:Spawn`.
5. Starts timer `Hatch`.
6. Spawns "A Vicious Spider" (33167) after `misty/misty#timer:Hatch`.
7. Loot "Spiderling Silk" (13099) from "A Vicious Spider".
8. Forage "Spiderling Silk" (13099) in `mistmoore`.
9. Forage "Spiderling Silk" (13099) in `mmca`.
10. Forage "Spiderling Silk" (13099) in `mmcb`.
11. Forage "Spiderling Silk" (13099) in `mmcc`.
12. Forage "Spiderling Silk" (13099) in `mmcd`.
13. Forage "Spiderling Silk" (13099) in `mmce`.
14. Forage "Spiderling Silk" (13099) in `mmcf`.
15. Forage "Spiderling Silk" (13099) in `mmcg`.
16. Forage "Spiderling Silk" (13099) in `mmch`.
17. Forage "Spiderling Silk" (13099) in `mmci`.
18. Forage "Spiderling Silk" (13099) in `mmcj`.
19. Combine in "Vale Sewing Kit" (92882): "Spiderling Silk" (13099). Produces "Silk Thread" (16486). Requires Tailoring, trivial 15. The combine does not fail.
20. Combine in "Vale Sewing Kit" (92882): "Silk Thread" (16486). Produces "Silk Cord" (16489). Requires Tailoring, trivial 26.
21. potranquility/"Kalym Rasalan", say "Hail". Gives "Silken Tapestry" (12593).
22. Combine in "Collapsible Sewing Kit" (17165): "Backpack Pattern" (12089), "Silk Cord" (16489), "Silken Tapestry" (12593). Produces "Silken Tapestry Satchel" (12596). Requires Tailoring 128. The combine does not fail.

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

### `wiz_epic_pre`

Values written: 1, 2, 3, 4.

1. lavastorm/"Talwyn Flamecaller", say "Hail". Sets `wiz_epic_pre` to `1`.
    - Requires `wiz_epic` unset.
    - Requires `wiz_epic_pre` unset.
    - Dialogue with lavastorm/"Talwyn Flamecaller":
      - Player: "Final Task" (link: external event mention)
        - Prompted by `event_trade`:
          - NPC say: To obtain this globe was no trivial task, yet you have prevailed! Your staff is nearly complete now, you have only two final tasks remaining.', he says as he begins to murmur a brief incantation. Without warning, the orb splits into two equal halves and are then given to you. They will infuse your staff with one of the most useful powers of a wizard; teleportation.'
          - Event guard: `(qglobals["wiz_epic20"] ~= nil and qglobals["wiz_epic20"] >= "3" and item_lib.check_turn_in(e.trade, {item1 = 47100}))`
        - NPC say: Your first task is to take the right half of the orb to the highest point achieved by a wizards spire on Norrath. On the western prong, you will find a small tear in space. Place the orb inside this tear; it will absorb the pure essence of teleportation. The second task will take you to the highest point achieved by a wizards spire on Luclin. Find another tear in space there and absorb that essence as well. Return to me with both halves imbued with the proper essence and hand them to me, along with your staff.
        - Condition: `(e.message:findi("final task") and qglobals["wiz_epic"] == "4")`
      - Player: "Hail" (link: conversation sequence)
        - NPC say: The power of the wizard courses through your veins thoroughly, ever in search of the opportunity to harness even more power. You have created a staff of immense power, yet even in its glory, is limited. To unleash the full potential of this weapon will be a large undertaking of its own. You must obtain a globe of pure discordant energy and return it to me. Look for assistance from the Plane of Discord from Grathnok Gilforgan. I know not where this being may be, but I do know that once you find him, he will be willing to assist you in finding the globe you seek.
        - Condition: `(e.message:findi("hail") and e.other:HasItem(12665))`
        - Sets `wiz_epic20` to `1`.
      - Player: "Hail" (link: conversation sequence)
        - NPC say: The fire of destruction burns within you, does it not? I can see that your affinity for destructive magic has served you well in your travels. It has served you so well that it has caught the eye of Solusek Ro. He has created and sent me here to discuss the matter of joining his legions. If you do, you will be granted power unheard of on mortal lands. Will you [agree]?
          - Reply guard: `(qglobals["wiz_epic"] == nil)`
        - Condition: `(e.message:findi("hail") and e.other:HasItem(14341))`
        - Sets `wiz_epic` to `1`.
      - Player: "Hail" (link: conversation sequence)
        - NPC say: The fire of destruction burns within you, does it not? I can see that your affinity for destructive magic has served you well in your travels. It has served you so well that it has caught the eye of Solusek Ro. He has created and sent me here to discuss the matter of joining his legions. If you do, you will be granted power unheard of on mortal lands. Will you [agree]?
          - Reply guard: `(qglobals["wiz_epic"] == nil and qglobals["wiz_epic_pre"] == nil)`
        - NPC say: You have completed the four tests of your abilities, but your journey to joining Solusek's legion is far from complete. You must now assemble a wand to help further focus your energies. In the lands of Discord, power surges and fades in an awesome display, the fluxing power flows through all things on the landscape. Go, investigate the lands of Discord; return to me with a [fluxing rod], [gem], [rune], and [ore]. With them you will be ready to take your first steps as a new soldier.
          - Reply guard: `(qglobals["wiz_epic_pre"] == "5")`
        - NPC say: The fire of destruction burns within you, does it not? I can see that your affinity for destructive magic has served you well in your travels. It has served you so well that it has caught the eye of Solusek Ro. He has created and sent me here to discuss the matter of joining his legions. If you do, you will be granted power unheard of on mortal lands. Will you [agree]?
          - Reply guard: ``
        - Condition: `(e.message:findi("hail") and e.other:GetClass() == Class.WIZARD and e.other:GetLevel() >= 65)`
        - Sets `wiz_epic_pre` to `1`.
        - Sets `wiz_epic` to `1`.
      - Player: "Agree" (link: explicit mention)
        - NPC say: I knew you would... What wizard could refuse an offer of such power? Since you have proven yourself only through combat and not yet through adventuring, I require you to prove yourself worthy once more. A small set of [tests], really.
          - Reply guard: `(qglobals["wiz_epic_pre"] ~= nil)`
        - NPC say: You have completed the tests of your abilities, but your journey to joining Solusek's legion is far from complete. You must now assemble a wand to help further focus your energies. In the lands of Discord power surges and fades in an awesome display, the fluxing power flows thru all things in the landscape. Go, investigate the lands of Discord; return to me with a [fluxing rod], [gem], [rune], and [ore]. With them you will be ready to take your first steps as a new soldier.
          - Reply guard: `(qglobals["wiz_epic"] == "1")`
        - Condition: `(e.message:findi("agree"))`
      - Player: "Fluxing Rod" (link: explicit mention)
        - NPC say: The rod that will be used to create the foundation for the staff can only be found in the place where magic tears and screams across the landscape. Only in the plane where discord reigns does the power exist to charge the rod properly. A race that has been recently discovered there has been seen carrying around rods of super charged discordant magic. We are unsure of their origin, but we believe the rods hold a great, yet unknown power worthy of use in this staff.
        - Condition: `(e.message:findi("fluxing rod"))`
      - Player: "Gem" (link: explicit mention)
        - Prompted by player input: "Hail"
        - NPC say: Fluxing gems have been found growing in the desert of Luclin. They form from the sand that has been blasted by magic. Sun Revenants have been known to collect them. Go to the plateau, and speak the word proclaim your desire to take their gems, this will draw out the elite revenants, one of them should be carrying the fluxing gem.
        - Condition: `(e.message:findi("gem"))`
      - Player: "Rune" (link: explicit mention)
        - Prompted by player input: "Hail"
        - NPC say: Fluxing runes are carried by the army of Terris Thule. These runes help her minions slip into their victim's dreams more easily. I believe you would be able to find one being carried by the lord of the hobgoblins.
        - Condition: `(e.message:findi("rune"))`
      - Player: "Ore" (link: explicit mention)
        - Prompted by player input: "Hail"
        - NPC say: It shouldn't be too hard to find some fluxing ore in an area we have termed the Ruined City of Dranik. Look in areas where one might expect to find ore-veins. Look on the mountain sides, beneath cliffs, even among the loose pieces of rock in the area.
        - Condition: `(e.message:findi("ore"))`
      - Player: "Powerful Item" (link: external event mention)
        - Prompted by `event_trade`:
          - NPC say: You are indeed ready to join the ranks as a soldier of Solusek Ro. Every soldier in Solusek's league must wield a staff of power, which will focus your abilities in a way that you have never felt before! Fear will consume you as you feel your essence being ripped from your body. Do not give up, use the staff with faith and hope that you will be rewarded with the most [powerful item] you could ever imagine.
          - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 11445, item2 = 11448, item3 = 11474, item4 = 11576}))`
        - NPC say: To lay hands on this staff you will have to construct it of items of this world. Power is not given out freely, you must earn it. You will be pressed to the limits of your knowledge and abilities. To begin you will need to gather the fires of Solusek himself. These fires burn in the deepest part of the dungeons named after him. The pure flame burns near the runes. Bring it to me to examine when you get it.
        - Condition: `(e.message:findi("powerful item") and qglobals.wiz_epic == "2")`
      - Player: "Tests" (link: explicit mention)
        - Prompted by player input: "Hail"
        - NPC say: The tests I require of you are merely to measure your ability as a wizard and follower of Solusek. They will draw upon the focal points of being a wizard. Through intelligence and its application to magic, you can call upon the elements more often without strain. Through subtlety, you are able to be destructive without calling the attention unto yourself. Through research, new, more powerful spells and incantations are discovered. Through channeling, the ability to concentrate on spells is enhanced, even in the most distracting of environments. Once you have completed these tests, return to me with the results, so that I may review them.
        - Condition: `(e.message:findi("tests"))`
      - Player: "Test Of Intelligence" (link: external event mention)
        - Prompted by `event_trade`:
          - NPC say: Excellent work, wizard! There was once a time when I thought these puzzles could not be solved, but through perseverance and knowledge, you have passed the Test of Intelligence.
          - Event guard: `(qglobals["wiz_test_intel"] ~= nil)`
          - Event guard: `(qglobals["wiz_test_intel"] == "10" and item_lib.check_turn_in(e.trade, {item1 = 11412}))`
        - NPC say: Through the intelligent use of magic, we are able to become more efficient at what we do. To prove to me that you have this gift, I will need you to work your way through a set of riddles. These riddles will take you full circle, beginning with me and ending with me. The path between those two points must be discovered by your own mettle. Take this note and do as it instructs. Take care when handling these notes, they are the lifeblood that will guide you on your journey and should you lose them, you will fail the test. I hope to see you back here with the correct answer soon.
          - Reply guard: `(qglobals["wiz_epic_pre"] == "1" and qglobals["wiz_test_intel"] == nil)`
        - NPC say: You have already successfully completed this test of your abilities! Waste no more time, young wizard, continue on with the other tasks that have been entrusted to you!
          - Reply guard: `(qglobals["wiz_epic_pre"] > "1")`
        - Condition: `(e.message:findi("test of intelligence"))`
        - Gives Old Parchment (11197).
        - Sets `wiz_test_intel` to `1`.
      - Player: "Test Of Channeling" (link: external event mention)
        - Prompted by `event_trade`:
          - NPC say: Your speed and concentration impress even me. The Test of Channeling is no easy feat to accomplish, especially with so many dangerous distractions nearby.
          - Event guard: `(qglobals["wiz_epic_pre"] == "2" and item_lib.check_turn_in(e.trade, {item1 = 16675}))`
        - NPC say: In the fortress of the sarnak, amidst some old bones, you will find a small, cursed trinket that I require you to obtain. I say that it is cursed because any that try to take it are surrounded in a swarm of scorpions. The scorpions are small and not dangerous by themselves, but when a hundred of them engulf your body, you can't stand but to run away. With your proficiency in channeling, you must go and retrieve this trinket for me. Prepare yourself for the curse will land on you and only by cutting through them will you find it.
          - Reply guard: `(qglobals["wiz_epic_pre"] == "2")`
        - NPC say: You have already successfully completed this test of your abilities! Waste no more time, young wizard, continue on with the other tasks that have been entrusted to you!
          - Reply guard: `(qglobals["wiz_epic_pre"] > "2")`
        - Condition: `(e.message:findi("test of channeling"))`
      - Player: "Test Of Research" (link: external event mention)
        - Prompted by `event_trade`:
          - NPC say: The Test of Research wears thin upon you, but with this parchment I hold in my hand, you have proven your worth as a contributor to the cause!
          - Event guard: `((qglobals["wiz_epic_pre"] == "3" or qglobals["wiz_epic_pre"] == "4") and item_lib.check_turn_in(e.trade, {item1 = 16623}))`
        - NPC say: Our ranks simply cannot be filled with slouches! We need to know that you will take the time and effort to be an effective wizard, not only for your own preservation, but also to be a contributor to our cause. You will be required to create a new spell. The research will be difficult, the runes many, but through cascade, coruscation, flash, desiccation, glint, impulse, synergy, tempest, vortex, and conflagration, you will find the path that burns deep within you. As with all spells, keep in mind the runes must be combined in a spell research kit. When you have crafted the spell, return it to me so that I may inspect it.
          - Reply guard: `(qglobals["wiz_epic_pre"] == "3")`
        - NPC say: You have already successfully completed this test of your abilities! Waste no more time, young wizard, continue on with the other tasks that have been entrusted to you!
          - Reply guard: `(qglobals["wiz_epic_pre"] > "3")`
        - Condition: `(e.message:findi("test of research"))`
      - Player: "Test Of Subtlety" (link: conversation sequence)
        - NPC say: In Steamfont you will find a friend of mine, Yama Twerik, with a bit of a dilemma on his hands. He was able to bring a non-functional clockwork back to Ak`Anon from the Plane of Innovation. He is by no means a wizard, so he needs help recharging the battery of the clockwork to get it working again. Go see, he will discuss with you the details of his predicament.
          - Reply guard: `(qglobals["wiz_epic_pre"] == "4")`
        - NPC say: You have already successfully completed this test of your abilities! Waste no more time, young wizard, continue on with the other tasks that have been entrusted to you!
          - Reply guard: `(qglobals["wiz_epic_pre"] > "4")`
        - Condition: `(e.message:findi("test of subtlety"))`

    - Subquest `wiz_epic`:
#### `wiz_epic`

Values written: 1, 2, 3, 4, 5.

1. lavastorm/"Talwyn Flamecaller", say "Hail". Sets `wiz_epic` to `1`.
    - Requires `wiz_epic` unset.

Alternative or repeat transition to `wiz_epic` = `1` (not an additional required stage).

1. lavastorm/"Talwyn Flamecaller", say "Hail". Sets `wiz_epic` to `1`.
    - Requires `wiz_epic_pre` ==5.

    - Subquest `wiz_epic_pre` documented earlier.
2. lavastorm/"Talwyn Flamecaller", hand "Fluxing Staff" (11445) + "Fluxing Gem" (11448) + "Fluxing Rune" (11474) + "Fluxing Chunk of Ore" (11576). Sets `wiz_epic` to `2`.
    - Hand in x1: "Fluxing Staff" (11445).
    - Hand in x1: "Fluxing Gem" (11448).
    - Hand in x1: "Fluxing Rune" (11474).
    - Hand in x1: "Fluxing Chunk of Ore" (11576).
    - Loot "Fluxing Staff" (11445) from "Girplan Guardian" in `wallofslaughter`.
    - Say "Gem" to scarlet/"The Gem Guardian".
    - Spawns "Elite Sun Revenant" (175306).
    - Loot "Fluxing Gem" (11448) from "Elite Sun Revenant".
    - Loot "Fluxing Rune" (11474) from "Hobgoblin Horrorfiend" in `ponightmare`.
    - Ground spawn of "Fluxing Chunk of Ore" (11576) in `dranik`.
    - Gives "Staff of Fluxing Power" (11596).

3. potranquility/"Kalym Rasalan", say "Hail". Sets `wiz_epic` to `3`.
    - Gives "Silken Tapestry" (12593).
    - Dialogue with potranquility/"Kalym Rasalan":
      - Player: "Hail"
        - NPC say: Hello , Talwyn told me of the coming of new recruits. I suppose he told you that you would need to use the magic in our woven tapestries to create a satchel to hold something very delicate? Well, you are lucky enough that I have this finished swatch of tapestry here that you can use. I am busy and can't tailor it for you though. You will need to tailor it yourself. If you take the tapestry, a backpack pattern, and a silk cord you should be able to tailor it with moderate effort.
        - Condition: `(e.message:findi("hail") and (qglobals.wiz_epic_wisp == "1") and (qglobals.wiz_epic_shard == "1"))`
        - Gives Silken Tapestry (12593).
        - Sets `wiz_epic` to `3`.

4. lavastorm/"Talwyn Flamecaller", hand "Silken Tapestry Satchel" (12596). Sets `wiz_epic` to `4`.
    - Hand in x1: "Silken Tapestry Satchel" (12596).
    - Prerequisite: "Silken Tapestry Satchel" (12596). See section 0.
    - Sets `wiz_epic_satchel` to `1`.
    - Gives "Silken Tapestry Satchel" (12596).

5. lavastorm/"Talwyn Flamecaller", hand "Full Tapestry Satchel" (16753). Sets `wiz_epic` to `5`.
    - Hand in x1: "Full Tapestry Satchel" (16753).
    - Prerequisite: "Full Tapestry Satchel" (16753). See section 0.
    - Gives "Staff of Prismatic Power" (12665).

###### Steps on `wiz_epic` that do not change it

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

2. lavastorm/"Talwyn Flamecaller", hand "Old Pipe" (11412). Sets `wiz_epic_pre` to `2`.
    - Requires `wiz_test_intel` ==10.
    - Hand in x1: "Old Pipe" (11412).
    - Ground spawn of "Old Pipe" (11412) in `cauldron`.
    - Gives "Rune of Greater Desiccation" (11439).

    - Subquest `wiz_test_intel`:
#### `wiz_test_intel`

Values written: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10.

1. lavastorm/"Talwyn Flamecaller", say "Test Of Intelligence". Sets `wiz_test_intel` to `1`.
    - Requires `wiz_epic_pre` ==1.
    - Requires `wiz_test_intel` unset.
    - Gives "Old Parchment" (11197).

    - Subquest `wiz_epic_pre` documented earlier.
2. lavastorm/"Talwyn Flamecaller", hand "Empty Jug" (11425). Sets `wiz_test_intel` to `2`.
    - Requires `wiz_test_intel` ==1.
    - Hand in x1: "Empty Jug" (11425).
    - Ground spawn of "Empty Jug" (11425) in `katta`.
    - Gives "Old Parchment" (11179).

3. lavastorm/"Talwyn Flamecaller", hand "Emerald-Tipped Staff" (11419). Sets `wiz_test_intel` to `3`.
    - Requires `wiz_test_intel` ==2.
    - Hand in x1: "Emerald-Tipped Staff" (11419).
    - Ground spawn of "Emerald-Tipped Staff" (11419) in `beholder`.
    - Gives "Old Parchment" (11044).

4. lavastorm/"Talwyn Flamecaller", hand "Meditation Basket" (11282). Sets `wiz_test_intel` to `4`.
    - Requires `wiz_test_intel` ==3.
    - Hand in x1: "Meditation Basket" (11282).
    - Ground spawn of "Meditation Basket" (11282) in `warslikswood`.
    - Gives "Old Parchment" (11200).

5. lavastorm/"Talwyn Flamecaller", hand "Platinum Token" (11433). Sets `wiz_test_intel` to `5`.
    - Requires `wiz_test_intel` ==4.
    - Hand in x1: "Platinum Token" (11433).
    - Ground spawn of "Platinum Token" (11433) in `pojustice`.
    - Gives "Old Parchment" (11148).

6. lavastorm/"Talwyn Flamecaller", hand "White Sash" (11413). Sets `wiz_test_intel` to `6`.
    - Requires `wiz_test_intel` ==5.
    - Hand in x1: "White Sash" (11413).
    - Ground spawn of "White Sash" (11413) in `letalis`.
    - Gives "Old Parchment" (11194).

7. lavastorm/"Talwyn Flamecaller", hand "Golden Dagger" (11424). Sets `wiz_test_intel` to `7`.
    - Requires `wiz_test_intel` ==6.
    - Hand in x1: "Golden Dagger" (11424).
    - Ground spawn of "Golden Dagger" (11424) in `skyfire`.
    - Gives "Old Parchment" (11279).

8. lavastorm/"Talwyn Flamecaller", hand "Ivory Bone" (11436). Sets `wiz_test_intel` to `8`.
    - Requires `wiz_test_intel` ==7.
    - Hand in x1: "Ivory Bone" (11436).
    - Ground spawn of "Ivory Bone" (11436) in `gunthak`.
    - Gives "Old Parchment" (11166).

9. lavastorm/"Talwyn Flamecaller", hand "Red Cloth" (11418). Sets `wiz_test_intel` to `9`.
    - Requires `wiz_test_intel` ==8.
    - Hand in x1: "Red Cloth" (11418).
    - Ground spawn of "Red Cloth" (11418) in `maiden`.
    - Gives "Old Parchment" (11095).

10. lavastorm/"Talwyn Flamecaller", hand "Worn Turban" (11299). Sets `wiz_test_intel` to `10`.
    - Requires `wiz_test_intel` ==9.
    - Hand in x1: "Worn Turban" (11299).
    - Fish "Worn Turban" (11299) in `potranquility`.
    - Gives "Old Parchment" (11102).

###### Steps on `wiz_test_intel` that do not change it

- `lavastorm` talwyn flamecaller, hand 11412 needs `wiz_test_intel` ==10.
  - Sets `wiz_epic_pre` to `2`.
  - Turn in Old Pipe (11412).
  - Gives Rune of Greater Desiccation (11439).

3. lavastorm/"Talwyn Flamecaller", hand "Cursed Talisman" (16675). Sets `wiz_epic_pre` to `3`.
    - Requires `wiz_epic_pre` ==2.
    - Hand in x1: "Cursed Talisman" (16675).
    - Kill lakeofillomen/. Spawns "A Scorpion Hatchling" (85240).
    - Loot "Cursed Talisman" (16675) from "A Scorpion Hatchling".
    - Gives "Cursed Talisman" (16675).

4. lavastorm/"Talwyn Flamecaller", hand "Spell: Electrical Charge" (16623). Sets `wiz_epic_pre` to `4`.
    - Requires `wiz_epic_pre` ==3.
    - Requires `wiz_epic_pre` ==4.
    - Hand in x1: "Spell: Electrical Charge" (16623).
    - Prerequisite: "Spell: Electrical Charge" (16623). See section 0.
    - Gives "Spell: Electrical Charge" (16623).

#### Steps on `wiz_epic_pre` that do not change it

- `lavastorm` talwyn flamecaller, say hail needs `wiz_epic_pre` ==5.
  - Sets `wiz_epic` to `1`.
- `lavastorm` talwyn flamecaller, say test of intelligence needs `wiz_epic_pre` ==1.
  - Sets `wiz_test_intel` to `1`.
  - Gives Old Parchment (11197).

### `wiz_epic`

See `wiz_epic` earlier in this file.

### `wizepic`

Values written: 1.

1. erudnext/"Camin", hand platinum:1000. Sets `wizepic` to `1`.
    - Hand in 1000 platinum.
    - Dialogue with erudnext/"Camin":
      - Player: "Hail"
        - NPC say: Go away! I have no time for you!
        - Condition: `(e.message:findi("hail"))`
      - Player: "What are you searching for" (link: conversation sequence)
        - NPC say: Ah! A smart one, I see! If you really wish to know about such a thing, you will have to help me finance my studies. The knowledge I have acquired and researched did not come cheaply.
        - Condition: `(e.message:findi("What are you searching for"))`

#### Steps on `wizepic` that do not change it

- `erudnext` camin, hand 14330 needs `wizepic` ==1.
  - Turn in Ro's Breath (14330).
  - Gives Ro's Breath (14331).

### `wizepicA`

Values written: 1.

1. halas/"Arantir Karondor", hand "Arantir's Ring" (14335). Sets `wizepicA` to `1`.
    - Hand in x1: "Arantir's Ring" (14335).
    - Prerequisite: "Arantir's Ring" (14335). See section 0.
    - Dialogue with halas/"Arantir Karondor":
      - Player: "Hail"
        - NPC say: Ah yes, you again. Do you have the items? Give me the three you possess and I'll combine them with my own.
          - Reply guard: `(qglobals["wizepicB"] == "1")`
        - NPC say: Ah, but it pains my heart to see this. How I could love a women like that is beyond me. And yet, I still do love her. It was on the day I was to ask her to marry me that I lost my powers. When I was about to cast my greatest spell to prove my love to her, my magic failed. She ran out on me that day. But enough of me, do you wish to hear my story?
          - Reply guard: `(qglobals["wizepicA"] == "1")`
        - NPC say: Before I tell you anything, I require you to help me. Seek a woman named Challice. Give her this ring and then return to me.
          - Reply guard: ``
        - Condition: `(e.message:findi("hail"))`
        - Gives Arantir's Ring (14334).
      - Player: "Story" (link: explicit mention)
        - NPC say: I once was one of four true followers of Solusek Ro. So great were the four of us that Solusek Ro himself made us each a special item. We did not know what the others' items were, but we realized that was for our own safety. Each one of us, after receiving the item, began to plot against Solusek Ro. Each of us believed we had enough power to dominate Norrath. Solusek Ro saw this and at the time we needed our powers most, he stripped us of them. Now I know two of the other wizards by name. One was called Sylen Tyrn, the other's name was Demunir Scry. The last wizard was a gnome, but I can't think of his name.
        - Condition: `(e.message:findi("story"))`
      - Player: "Sylen Tyrn" (link: explicit mention)
        - NPC say: Sylen was a high elf wizard, and like many high elves, he believed himself to be better than others. Because of his birth, he thought he was more noble and more intelligent than anyone else. I heard how met his demise - while flying over a vast area of water, his powers were stripped from him in midflight. He fell and was captured by a rival wizard who specialized in magics of the water. Search for that wizard and you could find a trace of Sylen.
        - Condition: `(e.message:findi("Sylen Tyrn"))`
      - Player: "Demunir Scry" (link: explicit mention)
        - Prompted by player input: "Story"
        - NPC say: Demunir was a human in a rush for power. He was extremely intelligent and resourceful but, unfortunately, was more interested in destructive magic. Hearing of an ancient land, he immediately traveled to it, believing there to be powerful relics left undiscovered there. While exploring, he came upon a dwelling that housed a powerful warrior. Believing himself to be more powerful, he attempted to take this dwelling for himself. While in battle with this warrior, Solusek Ro stole his powers and left him helpless. It is said that Demunir's item is the warrior's most prized trophy.
        - Condition: `(e.message:findi("Demunir Scry"))`
      - Player: "Gnome" (link: explicit mention)
        - Prompted by player input: "Story"
        - NPC say: Ah, the gnome I know very little about. I know he was small and crafty, and that he had a brother. His brother's craft was that of making fireworks, and he was the unfortunate victim of one of his own experiments. His firework exploded, leaving his mind diminished in capacity, even for a gnome. I remember others calling him 'Old Stewpot' in jest. I do not know if this is his birth name, but it may help you to locate him. I hear he also stays close to water because of the explosion. You never know when another gnomish invention will go awry. Give him this letter to help motivate him to remember.
        - Condition: `(e.message:findi("gnome") and e.other:Class() == "Wizard")`
        - Gives Note from Arantir (18169).

Alternative or repeat transition to `wizepicA` = `1` (not an additional required stage).

1. halas/"Dargon", hand "Arantir's Ring" (14335). Sets `wizepicA` to `1`.
    - Hand in x1: "Arantir's Ring" (14335).
    - Prerequisite: "Arantir's Ring" (14335). See section 0.
    - Spawns Arantir Karondor (29089).
    - Dialogue with halas/"Dargon":
      - Player: "Hail"
        - NPC say: Hello there, . Can I interest you in any components to help you in your research?
        - Condition: `(e.message:findi("Hail"))`

### `wizepicB`

Values written: 1.

1. halas/"Arantir Karondor", hand "Note to Arantir" (18168). Sets `wizepicB` to `1`.
    - Hand in x1: "Note to Arantir" (18168).
    - Prerequisite: "Note to Arantir" (18168). See section 0.

Alternative or repeat transition to `wizepicB` = `1` (not an additional required stage).

1. halas/"Dargon", hand "Note to Arantir" (18168). Sets `wizepicB` to `1`.
    - Hand in x1: "Note to Arantir" (18168).
    - Prerequisite: "Note to Arantir" (18168). See section 0.
    - Spawns Arantir Karondor (29089).

### `wizepicK`

Values written: 1.

1. butcher/"Kandin Firepot", hand "Note from Arantir" (18169). Sets `wizepicK` to `1`.
    - Hand in x1: "Note from Arantir" (18169).
    - Given by halas/"Arantir Karondor", say "Gnome".
    - Dialogue with butcher/"Kandin Firepot":
      - Player: "Hail"
        - NPC say: Hello, there! Don't have time to talk. I'm workin', workin', workin'! Careful! Don't slip in the oil!
        - Condition: `e.message:findi("hail")`
      - Player: "What Oil" (link: explicit mention)
        - NPC say: Ah the oil! I recently sent a specially crafted golem to explore through a huge portal to another plane. It's instructions were to collect special oil that I suspect existed in the plane. What I think is the golem broke down. This looks like a good task for one like you. Go see what's wrong with the golem. Here is spare gears of mine incase it's broken. Be careful though, if you put it in wrong it could explode or worse!
        - Condition: `qglobals["wizepicK"] ~= nil`
        - Condition: `e.message:findi("what oil")`
        - Gives Golem Sprocket (14319).

#### Steps on `wizepicK` that do not change it

- `butcher` kandin firepot, say what oil needs `wizepicK` set.
  - Gives Golem Sprocket (14319).

### `wiz_epic20`

Values written: 1, 2, 3, 4.

1. lavastorm/"Talwyn Flamecaller", say "Hail". Sets `wiz_epic20` to `1`.
    - Requires `wiz_epic20` unset.

2. draniksscar/"Grathnok Gilforgan", say "Intricate Horn Of Galien". Sets `wiz_epic20` to `2`.
    - Requires `wiz_epic20` ==1.
    - Requires `wiz_epic20` set.
    - Requires `wiz_epic20` >=1.
    - Dialogue with draniksscar/"Grathnok Gilforgan":
      - Player: "Globe Of Pure Discordant Energy"
        - NPC say: I know about the globes of which you speak and perhaps may even be able to aid you in obtaining one. First, though, I have to ask a favor of you. My people have suffered tireless ages here in Discord, protecting the portal. If we lose our hold on the portal the armies of discord would be able to overrun our home world, much like what has started to happen on your home world of Norrath.
        - Condition: `(qglobals["wiz_epic20"] ~= nil and qglobals["wiz_epic20"] >= "1")`
        - Condition: `(e.message:findi("globe of pure discordant energy"))`
      - Player: "Lose your hold" (link: conversation sequence)
        - NPC say: It is still too early to tell... We are well established here, but the constant attacks and dreary landscape really take their toll on young minds. Adding to that, when an attack is successful it bears heavy in the minds of my people. In a recent attack, a surprise raid upon our encampments, the precious Intricate Horn of Galien was taken. The purpose for this atrocity is as of yet unknown, however this item holds great meaning to us and the favor I ask is simply to return this sacred artifact to me.
        - Condition: `(qglobals["wiz_epic20"] ~= nil and qglobals["wiz_epic20"] >= "1")`
        - Condition: `(e.message:findi("Lose your hold"))`
      - Player: "Intricate Horn of Galien" (link: explicit mention)
        - NPC say: This precious artifact was placed on our largest tower, where its resonating voice stretched across the planes and through the mountains to rally our troops and warn us of an impending attack. The horn has tremendous sentimental value for us, as it belonged to one of the great leaders of our past. It is a horn made of the finest precious metals of our homeland, laden with runes and etchings and filled with gems and precious stones. It is a signification of our strength and perseverance over the ages and without it the morale is very low amongst our soldiers.
        - Condition: `(qglobals["wiz_epic20"] ~= nil and qglobals["wiz_epic20"] >= "1")`
        - Condition: `(e.message:findi("Intricate Horn of Galien"))`
        - Sets `wiz_epic20` to `2`.

3. draniksscar/"Grathnok Gilforgan", hand "Intricate Horn of Galien" (15825). Sets `wiz_epic20` to `3`.
    - Requires `wiz_epic20` ==2.
    - Hand in x1: "Intricate Horn of Galien" (15825).
    - Loot "Intricate Horn of Galien" (15825) from "Lightningcaller Vhalek" in `provinggrounds`.

4. lavastorm/"Talwyn Flamecaller", hand "Globe of Discordant Energy" (47100). Sets `wiz_epic20` to `4`.
    - Requires `wiz_epic20` set.
    - Requires `wiz_epic20` >=3.
    - Hand in x1: "Globe of Discordant Energy" (47100).
    - Say "Check Lorb" to anguish/"Zone Status".
    - Spawns "Orb of Discordant Energy" (317087).
    - Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy".
    - Alternative: Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy" (NPC 317087) in `anguish`; trigger: anguish/"Zone Status", say "Check Uorb".
    - Alternative: Loot "Globe of Discordant Energy" (47100) from "Ornate Chest" (NPC 317112) in `anguish`; trigger: anguish/"Zone Status", say "Check Amv Chest".
    - Alternative: Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy" (NPC 317087) in `anguish`; trigger: anguish/"Zone Status", on event_signal.
    - Alternative: Loot "Globe of Discordant Energy" (47100) from "Overlords Chest" (NPC 317124) in `anguish`; trigger: anguish/"Zone Status", on event_signal.
    - Gives "Broken Orb of Discordant Energy" (15836).
    - Gives "Broken Orb of Discordant Energy" (16147).

#### Steps on `wiz_epic20` that do not change it

- `lavastorm` talwyn flamecaller, hand 12665+16334+16451 needs `wiz_epic20` ==4.
  - Turn in Infused Orb of Discordant Energy (16451).
  - Turn in Infused Orb of Discordant Energy (16334).
  - Turn in Staff of Prismatic Power (12665).
  - Gives Staff of Phenomenal Power (16576).
- `provinggrounds` player, on loot needs `wiz_epic20` set.
  - Sets `wiz20_mpg_chest` to `1`.
  - Spawns a chest (epic 2.0) (893).

### Other flags touched along the way

- `wiz20_mpg_chest` set to 1 at provinggrounds/player.
- `wiz_epic_satchel` set to 1 at lavastorm/talwyn flamecaller.
- `wiz_epic_shard` set to 1 at lavastorm/talwyn flamecaller.
- `wiz_epic_wisp` set to 1 at lavastorm/talwyn flamecaller.
