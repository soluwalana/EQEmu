# Shaman

Acquisition paths traced backwards from the 1.0, 1.5 and 2.0 epic rewards. Flags are dependencies, not the definition of an epic. **Broken** indicates missing graph provenance.

## Epic 1.0

### "Spear of Fate" (10651)

1. **Unresolved introduction:** no connected introductory hail in the graph.
2. Kill fearplane/"Dread". Spawns "Iksar broodling" (72105).
3. Loot "Child's Tear" (1673) from "Iksar broodling".
4. Alternative: Loot "Child's Tear" (1673) from "Iksar broodling" (NPC 72105) in `fearplane`; trigger: fearplane/"Fright", on event_death_complete.
5. Alternative: Loot "Child's Tear" (1673) from "Iksar broodling" (NPC 72105) in `fearplane`; trigger: fearplane/"Terror", on event_death_complete.
6. Hand "Child's Tear" (1673) to citymist/"Lord Rak-Ashiir". Spawns "Lord Rak'Ashiir" (90183). Loot "Iksar Scale" (1674) from "Lord Rak'Ashiir".
7. emeraldjungle/"Spirit Sentinel", hand "Iksar Scale" (1674). Gives "Spear of Fate" (10651).

## Epic 1.5

### "Crafted Talisman of Fates" (57400)

1. freeportwest/"Elder Spirit Of Enlightenment", say "Hail". eyes you with an ageless wisdom. Ah, your spirit shines brightly. Should I know you? Should you choose to continue your journey, tell me that you are [prepared to carry on] and save the spirits. It appears you are not yet ready for the great tasks that I require to be done. There are others lesser than me that can guide you and prepare you to walk a greater path should you choose. You should seek them out. You can perhaps seek knowledge from your elders and peers.
2. Loot "Crystallized Blood" (57988) from "A Crystalline Arachnae" in `povalor`.
3. southro/"Bratoq Jiplup", hand platinum:2000. Gives "Clouded Glass Vial" (57991).
4. Loot "Stonemite Antennae" (57990) from "A Shore Stonemite" (NPC 280005) in `natimbi`. Drop cache: 93.14% chance per kill.
5. Loot "Mellian Leaf" (57989) from "A Malarian Crysalis" in `podisease`.
6. lakeofillomen/"Spirit Sentinel", hand "Crystallized Blood" (57988) + "Mellian Leaf" (57989) + "Stonemite Antennae" (57990) + "Clouded Glass Vial" (57991). Sets `shaman_pre` to `3`.
7. Kill fearplane/"Dread". Spawns "Iksar broodling" (72105).
8. Loot "Child's Tear" (1673) from "Iksar broodling".
9. Alternative: Loot "Child's Tear" (1673) from "Iksar broodling" (NPC 72105) in `fearplane`; trigger: fearplane/"Fright", on event_death_complete.
10. Alternative: Loot "Child's Tear" (1673) from "Iksar broodling" (NPC 72105) in `fearplane`; trigger: fearplane/"Terror", on event_death_complete.
11. Hand "Child's Tear" (1673) to citymist/"Lord Rak-Ashiir". Spawns "Lord Rak'Ashiir" (90183). Loot "Iksar Scale" (1674) from "Lord Rak'Ashiir".
12. emeraldjungle/"Spirit Sentinel", hand "Iksar Scale" (1674). Gives "Spear of Fate" (10651).
13. freeportwest/"Elder Spirit Of Enlightenment", say "Shaman". Sets `shaman_epic` to `1`.
14. shadeweaver/"Wunshi Kashra", hand platinum:1000. Gives "Thatched Medicine Bag" (57704).
15. Loot "Bleak Fungus" (57620) from "Shuddering Fungus" in `fungusgrove`.
16. Say "Up To It" to lakerathe/"Kimm Mcshannel".
17. Spawns "Ancient Megalodon" (51160).
18. Loot "Lustrous Seaweed" (52926) from "Ancient Megalodon".
19. lakerathe/"Kimm Mcshannel", hand "Lustrous Seaweed" (52926). Gives "Twine-Wrapped Lustrous Seaweed" (57600).
20. Combine in "Thatched Medicine Bag" (57704): "Bleak Fungus" (57620), "Twine-Wrapped Lustrous Seaweed" (57600). Produces "Shadowed Pulp" (57550). Requires Alchemy 100. Trivial at 175. The combine does not fail.
21. Ground spawn of "Twinkling Shrub" (57080) in `twilight`.
22. twilight/"Tikl Huk", hand "Twinkling Shrub" (57080). Gives "Tied Twinkling Shrubs" (52920).
23. Say "Elder Spirit Sent Me" to cobaltscar/"Yoppa Greenthumb".
24. Spawns "Gnashing Killer Shark" (117091).
25. Loot "Brittle Burned Bark" (57086) from "Gnashing Killer Shark".
26. Combine in "Thatched Medicine Bag" (57704): "Tied Twinkling Shrubs" (52920), "Brittle Burned Bark" (57086). Produces "Brittle Twigs" (57369). Requires Alchemy 100. Trivial at 175. The combine does not fail.
27. warrens/"Wilslik Gissu", hand "Brittle Twigs" (57369) + "Shadowed Pulp" (57550). Requires `shaman_epic` ==1. Gives "Distilled Potion of Endurance" (52921).
28. freeportwest/"Elder Spirit Of Enlightenment", hand "Distilled Potion of Endurance" (52921). Sets `shaman_epic` to `2`.
29. freeportwest/"Elder Spirit Of Enlightenment", say "Rare Gift". Requires `shaman_epic` ==2. Gives "Potion of Sustenance" (57081).
30. airplane/"Eternal Spirit", hand "Potion of Sustenance" (57081). Gives "Blessed Talisman of Wisdom" (57083).
31. Loot "Blessed Talisman of Patience" (57084) from "Punisher Veshtaq".
32. freeportwest/"Elder Spirit Of Enlightenment", hand "Blessed Talisman of Wisdom" (57083) + "Blessed Talisman of Patience" (57084). Sets `shaman_epic` to `3`.
33. Loot "Amulet of the Spiritist" (57087) from "Netherbian Swarmfiend" in `umbral`.
34. shadeweaver/"Wunshi Kashra", say "Stolen". Sets `shaman_epic_nadox` to `1`.
35. Spawns "Spiritseeker Nadox" (227319) in `nadox` on enter.
36. Loot "Ring of the Undead Spiritcharmer" (57085) from "Spiritseeker Nadox".
37. shadeweaver/"Wunshi Kashra", hand "Ring of the Undead Spiritcharmer" (57085) + "Amulet of the Spiritist" (57087). Sets `shaman_epic` to `4`.
38. freeportwest/"Elder Spirit Of Enlightenment", say "Business With Wunshi Is Finished". Requires `shaman_epic` ==4. Gives "Gemmed Bangle of Enlightenment" (57088).
39. lakerathe/"Kimm Mcshannel", hand "Gemmed Bangle of Enlightenment" (57088). Sets `shaman_epic` to `5`.
40. lakerathe/"Kimm Mcshannel", say "Break Down". Requires `shaman_epic` ==3. Requires `shaman_epic` set. Gives "Heyokah Medicine Bag" (52922).
41. Loot "Revenant Tooth" (57500) from "A Sun Revenant" in `thegrey`.
42. Loot "Perfect Marked Ukun Skin" (57701) from "Fang" in `draniksscar`.
43. Loot "Perfect Marked Ukun Skin" (57701) from "Ukun Gutfeaster" in `draniksscar`.
44. Loot "Perfect Marked Ukun Skin" (57701) from "Ukun Slavehunter" in `draniksscar`.
45. Loot "Corrosive Goo" (57100) from "A Pulsating Bile" in `charasis`.
46. Loot "Corruption Powder" (57520) from "Elite Corrupted Knight" in `codecay`.
47. Combine in "Heyokah Medicine Bag" (52922): "Revenant Tooth" (57500), "Perfect Marked Ukun Skin" (57701), "Corrosive Goo" (57100), "Corruption Powder" (57520). Produces "Shaman's Precious Diffusing Agent" (57560). Requires Alchemy 100. The combine does not fail.
48. lakerathe/"Kimm Mcshannel", hand "Shaman's Precious Diffusing Agent" (57560). Gives "Runed Purse of the McShannels" (57614).
49. freeportwest/"Elder Spirit Of Enlightenment", hand "Runed Purse of the McShannels" (57614). Sets `shaman_epic` to `6`.
50. freeportwest/"Elder Spirit Of Enlightenment", say "Acknowledge". Requires `shaman_epic` ==6. Gives "Crafted Talisman of Fates" (57400).

## Epic 2.0

### "Blessed Spiritstaff of the Heyokah" (57405)

1. freeportwest/"Elder Spirit Of Enlightenment", say "Hail". eyes you with an ageless wisdom. Ah, your spirit shines brightly. Should I know you? Should you choose to continue your journey, tell me that you are [prepared to carry on] and save the spirits. It appears you are not yet ready for the great tasks that I require to be done. There are others lesser than me that can guide you and prepare you to walk a greater path should you choose. You should seek them out. You can perhaps seek knowledge from your elders and peers.
2. freeportwest/"Elder Spirit Of Enlightenment", say "Prepared To Carry On". Sets `shaman_epic` to `8`.
3. fungusgrove/"Lupot Nukla", say "Taken By Force". Sets `shaman_epic` to `9`.
4. Say "Hail" to kodtaz/"Undari Perunea".
5. Spawns "Ikaav Spiritstealer" (293233).
6. Loot "Necklace of Perseverance" (57401) from "Ikaav Spiritstealer".
7. fungusgrove/"Lupot Nukla", hand "Necklace of Perseverance" (57401). Sets `shaman_epic` to `10`.
8. Spawns "Darkened Chanting Woodspirit" (210250) in `postorms` on enter.
9. Loot "Piece of Moaning Timber" (57403) from "Darkened Chanting Woodspirit".
10. fungusgrove/"Lupot Nukla", hand "Piece of Moaning Timber" (57403). Requires `shaman_epic` ==10. Gives "Impervious Medicine Bag" (57551).
11. freeportwest/"Elder Spirit Of Enlightenment", hand "Impervious Medicine Bag" (57551). Sets `shaman_epic` to `11`.
12. freeportwest/"Elder Spirit Of Enlightenment", say "Seek". Requires `shaman_epic` ==11. Gives "Pouch of Spirit Dust" (57710).
13. Spawns "A Phase Spider" (123190) in `necropolis` on event_combat.
14. Loot "Spirit-Touched Phased Spider Thorax" (57562) from "A Phase Spider".
15. Spawns "Lightning Warrior Spiritseeker" (316073) in `provinggrounds` on enter.
16. Loot "Glowing Trace of Might" (57250) from "Lightning Warrior Spiritseeker".
17. Say "Ready" to causeway/"Kupiop Iku".
18. Spawns "epic version of Murkglider School Leader" (303116).
19. Loot "Slight Trace of a Spirit" (57800) from "epic version of Murkglider School Leader".
20. Loot "Reviving Potion of Might" (57315) from "Bloated Girplan" in `dranik`.
21. Combine in "Pouch of Spirit Dust" (57710): "Spirit-Touched Phased Spider Thorax" (57562), "Glowing Trace of Might" (57250), "Slight Trace of a Spirit" (57800), "Reviving Potion of Might" (57315). Produces "Glowing Spirit Charm of Might" (57987). The combine does not fail.
22. freeportwest/"Elder Spirit Of Enlightenment", hand "Glowing Spirit Charm of Might" (57987). Sets `shaman_epic` to `12`.
23. Say "Fooled" to wallofslaughter/"Hudar Trittan".
24. Spawns "Discordling Spiritcaller" (300091).
25. Loot "Spiritcaller Beads" (57404) from "Discordling Spiritcaller".
26. freeportwest/"Elder Spirit Of Enlightenment", hand "Spiritcaller Beads" (57404). Sets `shaman_epic` to `13`.
27. Say "Check Lorb" to anguish/"Zone Status".
28. Spawns "Orb of Discordant Energy" (317087).
29. Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy".
30. Alternative: Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy" (NPC 317087) in `anguish`; trigger: anguish/"Zone Status", say "Check Uorb".
31. Alternative: Loot "Globe of Discordant Energy" (47100) from "Ornate Chest" (NPC 317112) in `anguish`; trigger: anguish/"Zone Status", say "Check Amv Chest".
32. Alternative: Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy" (NPC 317087) in `anguish`; trigger: anguish/"Zone Status", say "Signal:999999".
33. Alternative: Loot "Globe of Discordant Energy" (47100) from "Overlords Chest" (NPC 317124) in `anguish`; trigger: anguish/"Zone Status", say "Signal:999999".
34. freeportwest/"Elder Spirit Of Enlightenment", hand "Globe of Discordant Energy" (47100). Sets `shaman_epic` to `14`.
35. Loot "Crystallized Blood" (57988) from "A Crystalline Arachnae" in `povalor`.
36. southro/"Bratoq Jiplup", hand platinum:2000. Gives "Clouded Glass Vial" (57991).
37. Loot "Stonemite Antennae" (57990) from "A Shore Stonemite" (NPC 280005) in `natimbi`. Drop cache: 93.14% chance per kill.
38. Loot "Mellian Leaf" (57989) from "A Malarian Crysalis" in `podisease`.
39. lakeofillomen/"Spirit Sentinel", hand "Crystallized Blood" (57988) + "Mellian Leaf" (57989) + "Stonemite Antennae" (57990) + "Clouded Glass Vial" (57991). Sets `shaman_pre` to `3`.
40. Kill fearplane/"Dread". Spawns "Iksar broodling" (72105).
41. Loot "Child's Tear" (1673) from "Iksar broodling".
42. Alternative: Loot "Child's Tear" (1673) from "Iksar broodling" (NPC 72105) in `fearplane`; trigger: fearplane/"Fright", on event_death_complete.
43. Alternative: Loot "Child's Tear" (1673) from "Iksar broodling" (NPC 72105) in `fearplane`; trigger: fearplane/"Terror", on event_death_complete.
44. Hand "Child's Tear" (1673) to citymist/"Lord Rak-Ashiir". Spawns "Lord Rak'Ashiir" (90183). Loot "Iksar Scale" (1674) from "Lord Rak'Ashiir".
45. emeraldjungle/"Spirit Sentinel", hand "Iksar Scale" (1674). Gives "Spear of Fate" (10651).
46. freeportwest/"Elder Spirit Of Enlightenment", say "Shaman". Sets `shaman_epic` to `1`.
47. shadeweaver/"Wunshi Kashra", hand platinum:1000. Gives "Thatched Medicine Bag" (57704).
48. Loot "Bleak Fungus" (57620) from "Shuddering Fungus" in `fungusgrove`.
49. Say "Up To It" to lakerathe/"Kimm Mcshannel".
50. Spawns "Ancient Megalodon" (51160).
51. Loot "Lustrous Seaweed" (52926) from "Ancient Megalodon".
52. lakerathe/"Kimm Mcshannel", hand "Lustrous Seaweed" (52926). Gives "Twine-Wrapped Lustrous Seaweed" (57600).
53. Combine in "Thatched Medicine Bag" (57704): "Bleak Fungus" (57620), "Twine-Wrapped Lustrous Seaweed" (57600). Produces "Shadowed Pulp" (57550). Requires Alchemy 100. Trivial at 175. The combine does not fail.
54. Ground spawn of "Twinkling Shrub" (57080) in `twilight`.
55. twilight/"Tikl Huk", hand "Twinkling Shrub" (57080). Gives "Tied Twinkling Shrubs" (52920).
56. Say "Elder Spirit Sent Me" to cobaltscar/"Yoppa Greenthumb".
57. Spawns "Gnashing Killer Shark" (117091).
58. Loot "Brittle Burned Bark" (57086) from "Gnashing Killer Shark".
59. Combine in "Thatched Medicine Bag" (57704): "Tied Twinkling Shrubs" (52920), "Brittle Burned Bark" (57086). Produces "Brittle Twigs" (57369). Requires Alchemy 100. Trivial at 175. The combine does not fail.
60. warrens/"Wilslik Gissu", hand "Brittle Twigs" (57369) + "Shadowed Pulp" (57550). Requires `shaman_epic` ==1. Gives "Distilled Potion of Endurance" (52921).
61. freeportwest/"Elder Spirit Of Enlightenment", hand "Distilled Potion of Endurance" (52921). Sets `shaman_epic` to `2`.
62. freeportwest/"Elder Spirit Of Enlightenment", say "Rare Gift". Requires `shaman_epic` ==2. Gives "Potion of Sustenance" (57081).
63. airplane/"Eternal Spirit", hand "Potion of Sustenance" (57081). Gives "Blessed Talisman of Wisdom" (57083).
64. Loot "Blessed Talisman of Patience" (57084) from "Punisher Veshtaq".
65. freeportwest/"Elder Spirit Of Enlightenment", hand "Blessed Talisman of Wisdom" (57083) + "Blessed Talisman of Patience" (57084). Sets `shaman_epic` to `3`.
66. Loot "Amulet of the Spiritist" (57087) from "Netherbian Swarmfiend" in `umbral`.
67. shadeweaver/"Wunshi Kashra", say "Stolen". Sets `shaman_epic_nadox` to `1`.
68. Spawns "Spiritseeker Nadox" (227319) in `nadox` on enter.
69. Loot "Ring of the Undead Spiritcharmer" (57085) from "Spiritseeker Nadox".
70. shadeweaver/"Wunshi Kashra", hand "Ring of the Undead Spiritcharmer" (57085) + "Amulet of the Spiritist" (57087). Sets `shaman_epic` to `4`.
71. freeportwest/"Elder Spirit Of Enlightenment", say "Business With Wunshi Is Finished". Requires `shaman_epic` ==4. Gives "Gemmed Bangle of Enlightenment" (57088).
72. lakerathe/"Kimm Mcshannel", hand "Gemmed Bangle of Enlightenment" (57088). Sets `shaman_epic` to `5`.
73. lakerathe/"Kimm Mcshannel", say "Break Down". Requires `shaman_epic` ==3. Requires `shaman_epic` set. Gives "Heyokah Medicine Bag" (52922).
74. Loot "Revenant Tooth" (57500) from "A Sun Revenant" in `thegrey`.
75. Loot "Perfect Marked Ukun Skin" (57701) from "Fang" in `draniksscar`.
76. Loot "Perfect Marked Ukun Skin" (57701) from "Ukun Gutfeaster" in `draniksscar`.
77. Loot "Perfect Marked Ukun Skin" (57701) from "Ukun Slavehunter" in `draniksscar`.
78. Loot "Corrosive Goo" (57100) from "A Pulsating Bile" in `charasis`.
79. Loot "Corruption Powder" (57520) from "Elite Corrupted Knight" in `codecay`.
80. Combine in "Heyokah Medicine Bag" (52922): "Revenant Tooth" (57500), "Perfect Marked Ukun Skin" (57701), "Corrosive Goo" (57100), "Corruption Powder" (57520). Produces "Shaman's Precious Diffusing Agent" (57560). Requires Alchemy 100. The combine does not fail.
81. lakerathe/"Kimm Mcshannel", hand "Shaman's Precious Diffusing Agent" (57560). Gives "Runed Purse of the McShannels" (57614).
82. freeportwest/"Elder Spirit Of Enlightenment", hand "Runed Purse of the McShannels" (57614). Sets `shaman_epic` to `6`.
83. freeportwest/"Elder Spirit Of Enlightenment", say "Acknowledge". Requires `shaman_epic` ==6. Gives "Crafted Talisman of Fates" (57400).
84. freeportwest/"Elder Spirit Of Enlightenment", hand "Crafted Talisman of Fates" (57400). Requires `shaman_epic` ==14. Gives "Blessed Spiritstaff of the Heyokah" (57405).

## Quest-state progression

## 0. Prerequisites

Shared acquisition steps appear in the first prerequisite chain that needs them. Later sections reference that chain rather than repeating it.

### "Impervious Medicine Bag" (57551)

1. freeportwest/"Elder Spirit Of Enlightenment", say "Prepared To Carry On". Sets `shaman_epic` to `8`.
2. fungusgrove/"Lupot Nukla", say "Taken By Force". Sets `shaman_epic` to `9`.
3. Say "Hail" to kodtaz/"Undari Perunea".
4. Spawns "Ikaav Spiritstealer" (293233).
5. Loot "Necklace of Perseverance" (57401) from "Ikaav Spiritstealer".
6. fungusgrove/"Lupot Nukla", hand "Necklace of Perseverance" (57401). Sets `shaman_epic` to `10`.
7. Spawns "Darkened Chanting Woodspirit" (210250) in `postorms` on enter.
8. Loot "Piece of Moaning Timber" (57403) from "Darkened Chanting Woodspirit".
9. fungusgrove/"Lupot Nukla", hand "Piece of Moaning Timber" (57403). Requires `shaman_epic` ==10. Gives "Impervious Medicine Bag" (57551).

### "Glowing Spirit Charm of Might" (57987)

1. Acquisition of "Impervious Medicine Bag" (57551) is documented under "Impervious Medicine Bag" (57551); obtain another copy if needed.
2. freeportwest/"Elder Spirit Of Enlightenment", hand "Impervious Medicine Bag" (57551). Sets `shaman_epic` to `11`.
3. freeportwest/"Elder Spirit Of Enlightenment", say "Seek". Requires `shaman_epic` ==11. Gives "Pouch of Spirit Dust" (57710).
4. Spawns "A Phase Spider" (123190) in `necropolis` on event_combat.
5. Loot "Spirit-Touched Phased Spider Thorax" (57562) from "A Phase Spider".
6. Spawns "Lightning Warrior Spiritseeker" (316073) in `provinggrounds` on enter.
7. Loot "Glowing Trace of Might" (57250) from "Lightning Warrior Spiritseeker".
8. Say "Ready" to causeway/"Kupiop Iku".
9. Spawns "epic version of Murkglider School Leader" (303116).
10. Loot "Slight Trace of a Spirit" (57800) from "epic version of Murkglider School Leader".
11. Loot "Reviving Potion of Might" (57315) from "Bloated Girplan" in `dranik`.
12. Combine in "Pouch of Spirit Dust" (57710): "Spirit-Touched Phased Spider Thorax" (57562), "Glowing Trace of Might" (57250), "Slight Trace of a Spirit" (57800), "Reviving Potion of Might" (57315). Produces "Glowing Spirit Charm of Might" (57987). The combine does not fail.

### "Spear of Fate" (10651)

1. Kill fearplane/"Dread". Spawns "Iksar broodling" (72105).
2. Loot "Child's Tear" (1673) from "Iksar broodling".
3. Alternative: Loot "Child's Tear" (1673) from "Iksar broodling" (NPC 72105) in `fearplane`; trigger: fearplane/"Fright", on event_death_complete.
4. Alternative: Loot "Child's Tear" (1673) from "Iksar broodling" (NPC 72105) in `fearplane`; trigger: fearplane/"Terror", on event_death_complete.
5. Hand "Child's Tear" (1673) to citymist/"Lord Rak-Ashiir". Spawns "Lord Rak'Ashiir" (90183). Loot "Iksar Scale" (1674) from "Lord Rak'Ashiir".
6. emeraldjungle/"Spirit Sentinel", hand "Iksar Scale" (1674). Gives "Spear of Fate" (10651).
    - Dialogue with emeraldjungle/"Spirit Sentinel":
      - Player: "continue what I have started"
        - NPC say: This brings happiness to our hearts and we are grateful. However, we must ask you to walk one more path before you can become a true Heyokah. With trust, one can focus on what is important. With patience, one can perceive what is harmful. With wisdom, one can know what must be done. These, you have learned, yet without the might to carry out what must be done, all is for naught. Are you [prepared to walk the path of might]?
        - Condition: `(e.other:GetFaction(e.self) <= 3)`
        - Condition: `(e.other:GetCharacterFactionLevel(404) >= 500)`
        - Condition: `(e.message:findi("continue what I have started"))`
      - Player: "Walk The Path Of Might" (link: explicit mention)
        - NPC say: Good, good, Do you know this place, , this forest? The wasichu call it the Emerald Jungle, but we know it only as the terrible place. Where there is no spirituality, we are weak. The lost city in the middle of this jungle is a great void of belief not only absent of spirituality, but actually draining it from others. We are here to neutralize that void. The void is like the sky, and nothing escapes its gaze. If it senses us, it will drain us away and sometimes it turns our minds, making us [like the wasichu], crazy for things with no meaning.
        - Condition: `(e.other:GetFaction(e.self) <= 3)`
        - Condition: `(e.other:GetCharacterFactionLevel(404) >= 500)`
        - Condition: `(e.message:findi("walk the path of might"))`
      - Player: "Like The Wasichu" (link: explicit mention)
        - NPC say: Yes, there are some of us who have turned their backs on our world and struggle for possesions and power over others. These lost ones are our brothers and we cry for them. Our hearts are in pain like bleeding wounds when we think of them. The path of might will lead you to one of our lost brothers. We are afraid there is nothing we can do for him now, so you must eliminate him when you [find him].
        - Condition: `(e.other:GetFaction(e.self) <= 3)`
        - Condition: `(e.other:GetCharacterFactionLevel(404) >= 500)`
        - Condition: `(e.message:findi("like the wasichu"))`
      - Player: "Find Him" (link: explicit mention)
        - NPC say: He left us long ago and walked the land for ages. He soon met a man, one of the pointy-ears that live underground. This man was like a void just like the one over that terrible place now. Our Brother-Friend was attracted to this man's desire and ambition. He no doubt thought that he could get what he wanted in service of this [dark point ear] who denied his own creator.
        - Condition: `(e.other:GetFaction(e.self) <= 3)`
        - Condition: `(e.other:GetCharacterFactionLevel(404) >= 500)`
        - Condition: `(e.message:findi("find him"))`
      - Player: "Dark Point Ear" (link: explicit mention)
        - NPC say: After our brother began traveling with this point-ear, they became shrouded in a darkness we could not peer through. The point-ear was a powerful being and we soon lost their trail. We have no idea where he could be now. Although, after all these centuries, he has no doubt been gathering and cultivating his wealth and power. He must be an incredibly influential being at this point. Find this point-ear and draw our brother out, then destroy him and bring us proof. We await your return in somber mourning.
        - Condition: `(e.other:GetFaction(e.self) <= 3)`
        - Condition: `(e.other:GetCharacterFactionLevel(404) >= 500)`
        - Condition: `(e.message:findi("dark point ear"))`
      - Player: "continue what I have started"
        - NPC say: You need to prove your dedication to our cause before I can discuss such matters with you.
        - Condition: `(e.other:GetFaction(e.self) <= 3)`
        - Condition: `(e.message:findi("continue what I have started") or e.message:findi("walk the path of might") or e.message:findi("like the wasichu") or e.message:findi("find him") or e.message:findi("dark point ear"))`
      - Player: "Walk The Path Of Might" (link: explicit mention)
        - NPC say: You need to prove your dedication to our cause before I can discuss such matters with you.
        - Condition: `(e.other:GetFaction(e.self) <= 3)`
        - Condition: `(e.message:findi("continue what I have started") or e.message:findi("walk the path of might") or e.message:findi("like the wasichu") or e.message:findi("find him") or e.message:findi("dark point ear"))`
      - Player: "Like The Wasichu" (link: explicit mention)
        - NPC say: You need to prove your dedication to our cause before I can discuss such matters with you.
        - Condition: `(e.other:GetFaction(e.self) <= 3)`
        - Condition: `(e.message:findi("continue what I have started") or e.message:findi("walk the path of might") or e.message:findi("like the wasichu") or e.message:findi("find him") or e.message:findi("dark point ear"))`
      - Player: "Find Him" (link: explicit mention)
        - NPC say: You need to prove your dedication to our cause before I can discuss such matters with you.
        - Condition: `(e.other:GetFaction(e.self) <= 3)`
        - Condition: `(e.message:findi("continue what I have started") or e.message:findi("walk the path of might") or e.message:findi("like the wasichu") or e.message:findi("find him") or e.message:findi("dark point ear"))`
      - Player: "Dark Point Ear" (link: explicit mention)
        - NPC say: You need to prove your dedication to our cause before I can discuss such matters with you.
        - Condition: `(e.other:GetFaction(e.self) <= 3)`
        - Condition: `(e.message:findi("continue what I have started") or e.message:findi("walk the path of might") or e.message:findi("like the wasichu") or e.message:findi("find him") or e.message:findi("dark point ear"))`
      - Player: "Heyokah" (link: explicit mention)
        - Prompted by player input: "continue what I have started"
        - NPC say: Yes, you have walked the Path of the Heyokah to its end. You have become what few have and we will now call to you as Heyokah . From now on, you are a direct link between the spirits and man. Whether your goals are to help us or master us, you are welcomed. Though there is little time for celebration. Do you feel the darkness of this place, the forest? To eyes not trained to see beyond physical appearances, it seems like any other forest. But you know, as do we, of the mantle over the city threatening all of us. We must [rub it out].
        - Condition: `(e.other:GetFaction(e.self) <= 3)`
        - Condition: `(e.other:GetCharacterFactionLevel(404) >= 600)`
        - Condition: `(e.message:findi("Heyokah"))`
      - Player: "Rub It Out" (link: explicit mention)
        - NPC say: There are many such mantles scarring the universe and each is very different from the last. Removing them requires that we learn how they were created and go about reversing the damage done. We cannot enter under the mantle for long which is why we search out Heyokah such as yourself. We need you to enter the city and find out what you can about the [city's demise]. We hope you will do this for the cause of balance but if you desire none but your own power, we shall grant that as well.
        - Condition: `(e.other:GetFaction(e.self) <= 3)`
        - Condition: `(e.other:GetCharacterFactionLevel(404) >= 600)`
        - Condition: `(e.message:findi("rub it out"))`
      - Player: "How It All Began" (link: conversation sequence)
        - NPC say: Excellent! Go into the city and gather what evidence you can. The ghosts who still walk the streets may hoard precious memories that will aid us. Take this booklet and combine what you find in it. Then bring me the completed report. From there, we will know where to look next.
        - Condition: `(e.other:GetFaction(e.self) <= 3)`
        - Condition: `(e.other:GetCharacterFactionLevel(404) >= 600)`
        - Condition: `(e.message:findi("how it all began"))`
        - Gives Ancient Journal (17805).
      - Player: "Heyokah" (link: explicit mention)
        - Prompted by player input: "continue what I have started"
        - NPC say: You need to prove your dedication to our cause before I can discuss such matters with you.
        - Condition: `(e.other:GetFaction(e.self) <= 3)`
        - Condition: `(e.message:findi("Heyokah") or e.message:findi("rub it out") or e.message:findi("city's demise") or e.message:findi("how it all began"))`
      - Player: "Rub It Out" (link: explicit mention)
        - NPC say: You need to prove your dedication to our cause before I can discuss such matters with you.
        - Condition: `(e.other:GetFaction(e.self) <= 3)`
        - Condition: `(e.message:findi("Heyokah") or e.message:findi("rub it out") or e.message:findi("city's demise") or e.message:findi("how it all began"))`
      - Player: "How It All Began" (link: conversation sequence)
        - NPC say: You need to prove your dedication to our cause before I can discuss such matters with you.
        - Condition: `(e.other:GetFaction(e.self) <= 3)`
        - Condition: `(e.message:findi("Heyokah") or e.message:findi("rub it out") or e.message:findi("city's demise") or e.message:findi("how it all began"))`

### "Black Fur Boots" (1678)

1. Loot "Black Dire Pelt" (1672) from "Black Dire" in `mistmoore`.
2. emeraldjungle/"Spirit Sentinel", hand "Black Dire Pelt" (1672). Gives "Black Fur Boots" (1678).

### "Distilled Potion of Endurance" (52921)

1. Loot "Crystallized Blood" (57988) from "A Crystalline Arachnae" in `povalor`.
2. southro/"Bratoq Jiplup", hand platinum:2000. Gives "Clouded Glass Vial" (57991).
    - Dialogue with southro/"Bratoq Jiplup":
      - Player: "Hail"
        - NPC say: I'm going to hedge my bets and guess that you are here for my special vial? Takes me forever to make and is going to cost you 2000 platinum. Yes indeed.
        - Condition: `($text=~/hail/i)`
3. Loot "Stonemite Antennae" (57990) from "A Shore Stonemite" (NPC 280005) in `natimbi`. Drop cache: 93.14% chance per kill.
4. Loot "Mellian Leaf" (57989) from "A Malarian Crysalis" in `podisease`.
5. lakeofillomen/"Spirit Sentinel", hand "Crystallized Blood" (57988) + "Mellian Leaf" (57989) + "Stonemite Antennae" (57990) + "Clouded Glass Vial" (57991). Sets `shaman_pre` to `3`.
6. Acquisition of "Spear of Fate" (10651) is documented under "Spear of Fate" (10651); obtain another copy if needed.
7. freeportwest/"Elder Spirit Of Enlightenment", say "Shaman". Sets `shaman_epic` to `1`.
8. shadeweaver/"Wunshi Kashra", hand platinum:1000. Gives "Thatched Medicine Bag" (57704).
9. Loot "Bleak Fungus" (57620) from "Shuddering Fungus" in `fungusgrove`.
10. Say "Up To It" to lakerathe/"Kimm Mcshannel".
11. Spawns "Ancient Megalodon" (51160).
12. Loot "Lustrous Seaweed" (52926) from "Ancient Megalodon".
13. lakerathe/"Kimm Mcshannel", hand "Lustrous Seaweed" (52926). Gives "Twine-Wrapped Lustrous Seaweed" (57600).
14. Combine in "Thatched Medicine Bag" (57704): "Bleak Fungus" (57620), "Twine-Wrapped Lustrous Seaweed" (57600). Produces "Shadowed Pulp" (57550). Requires Alchemy 100. Trivial at 175. The combine does not fail.
15. Ground spawn of "Twinkling Shrub" (57080) in `twilight`.
16. twilight/"Tikl Huk", hand "Twinkling Shrub" (57080). Gives "Tied Twinkling Shrubs" (52920).
    - Dialogue with twilight/"Tikl Huk":
      - Player: "Elder Spirit Sent Me"
        - NPC say: Yous sent by spirit? Me surprised it send so quick. Me no time to get da shrub yets. Yous will needs to get three of dem. Da shrub only grow nearby in only few spots. Gib dem to me when yous nab dem.
        - Condition: `(defined $qglobals{shaman_epic} && $qglobals{shaman_epic} == 1)`
        - Condition: `($text=~/elder spirit sent me/i)`
17. Say "Elder Spirit Sent Me" to cobaltscar/"Yoppa Greenthumb".
18. Spawns "Gnashing Killer Shark" (117091).
19. Loot "Brittle Burned Bark" (57086) from "Gnashing Killer Shark".
20. Combine in "Thatched Medicine Bag" (57704): "Tied Twinkling Shrubs" (52920), "Brittle Burned Bark" (57086). Produces "Brittle Twigs" (57369). Requires Alchemy 100. Trivial at 175. The combine does not fail.
21. warrens/"Wilslik Gissu", hand "Brittle Twigs" (57369) + "Shadowed Pulp" (57550). Requires `shaman_epic` ==1. Gives "Distilled Potion of Endurance" (52921).
    - Dialogue with warrens/"Wilslik Gissu":
      - Player: "Elder Spirit Sent Me"
        - NPC say: Greetingsss fair sage. It would seem that you have come to aid the spirit who fades like each breath we let pass through our lips. There is not [much time] to dawdle. We must get to work right away. As an alchemist yourself, I will tell you what you must do. You must first make some separate combinations. Do not attempt to do this if you are not a master. You will most certainly fail. Ready for instruction?
        - Condition: `(e.message:findi("elder spirit sent me") and qglobals["shaman_epic"] == "1")`
      - Player: "Much Time" (link: explicit mention)
        - NPC say: How shall I put this in termsss you will understand? Two of the rare items of nature's bounty will join because they live in darkness. The others will join because they share love of light. You must use the medicine bag given to you by my old friend -- and entrepreneur -- Wunshi. When you've successfully worked with those, tell me you have completed the first step.
        - Condition: `(e.message:findi("much time") and qglobals["shaman_epic"] == "1")`
      - Player: "First Step" (link: explicit mention)
        - NPC say: Nicely done, friend. You have done good work. Now, give me both of those pieces and I will fashion what you need to return to the spirit.
        - Condition: `(e.message:findi("first step") and qglobals["shaman_epic"] == "1" and e.other:HasItem(57369) and e.other:HasItem(57550))`

### "Blessed Talisman of Wisdom" (57083)

1. Acquisition of "Distilled Potion of Endurance" (52921) is documented under "Distilled Potion of Endurance" (52921); obtain another copy if needed.
2. freeportwest/"Elder Spirit Of Enlightenment", hand "Distilled Potion of Endurance" (52921). Sets `shaman_epic` to `2`.
3. freeportwest/"Elder Spirit Of Enlightenment", say "Rare Gift". Requires `shaman_epic` ==2. Gives "Potion of Sustenance" (57081).
4. airplane/"Eternal Spirit", hand "Potion of Sustenance" (57081). Gives "Blessed Talisman of Wisdom" (57083).

### "Gemmed Bangle of Enlightenment" (57088)

1. Acquisition of "Blessed Talisman of Wisdom" (57083) is documented under "Blessed Talisman of Wisdom" (57083); obtain another copy if needed.
2. Loot "Blessed Talisman of Patience" (57084) from "Punisher Veshtaq".
3. freeportwest/"Elder Spirit Of Enlightenment", hand "Blessed Talisman of Wisdom" (57083) + "Blessed Talisman of Patience" (57084). Sets `shaman_epic` to `3`.
4. Loot "Amulet of the Spiritist" (57087) from "Netherbian Swarmfiend" in `umbral`.
5. shadeweaver/"Wunshi Kashra", say "Stolen". Sets `shaman_epic_nadox` to `1`.
6. Spawns "Spiritseeker Nadox" (227319) in `nadox` on enter.
7. Loot "Ring of the Undead Spiritcharmer" (57085) from "Spiritseeker Nadox".
8. shadeweaver/"Wunshi Kashra", hand "Ring of the Undead Spiritcharmer" (57085) + "Amulet of the Spiritist" (57087). Sets `shaman_epic` to `4`.
9. freeportwest/"Elder Spirit Of Enlightenment", say "Business With Wunshi Is Finished". Requires `shaman_epic` ==4. Gives "Gemmed Bangle of Enlightenment" (57088).

### "Crafted Talisman of Fates" (57400)

1. Acquisition of "Gemmed Bangle of Enlightenment" (57088) is documented under "Gemmed Bangle of Enlightenment" (57088); obtain another copy if needed.
2. lakerathe/"Kimm Mcshannel", hand "Gemmed Bangle of Enlightenment" (57088). Sets `shaman_epic` to `5`.
3. lakerathe/"Kimm Mcshannel", say "Break Down". Requires `shaman_epic` ==3. Requires `shaman_epic` set. Gives "Heyokah Medicine Bag" (52922).
4. Loot "Revenant Tooth" (57500) from "A Sun Revenant" in `thegrey`.
5. Loot "Perfect Marked Ukun Skin" (57701) from "Fang" in `draniksscar`.
6. Loot "Perfect Marked Ukun Skin" (57701) from "Ukun Gutfeaster" in `draniksscar`.
7. Loot "Perfect Marked Ukun Skin" (57701) from "Ukun Slavehunter" in `draniksscar`.
8. Loot "Corrosive Goo" (57100) from "A Pulsating Bile" in `charasis`.
9. Loot "Corruption Powder" (57520) from "Elite Corrupted Knight" in `codecay`.
10. Combine in "Heyokah Medicine Bag" (52922): "Revenant Tooth" (57500), "Perfect Marked Ukun Skin" (57701), "Corrosive Goo" (57100), "Corruption Powder" (57520). Produces "Shaman's Precious Diffusing Agent" (57560). Requires Alchemy 100. The combine does not fail.
11. lakerathe/"Kimm Mcshannel", hand "Shaman's Precious Diffusing Agent" (57560). Gives "Runed Purse of the McShannels" (57614).
12. freeportwest/"Elder Spirit Of Enlightenment", hand "Runed Purse of the McShannels" (57614). Sets `shaman_epic` to `6`.
13. freeportwest/"Elder Spirit Of Enlightenment", say "Acknowledge". Requires `shaman_epic` ==6. Gives "Crafted Talisman of Fates" (57400).

### "Runed Purse of the McShannels" (57614)

1. Acquisition of "Runed Purse of the McShannels" (57614) is documented under "Crafted Talisman of Fates" (57400); obtain another copy if needed.

### `shaman_pre`

Values written: 1, 2, 3.

1. freeportwest/"Elder Spirit Of Enlightenment", say "Hail". Sets `shaman_pre` to `1`.
    - Requires `shaman_pre` unset.
    - Dialogue with freeportwest/"Elder Spirit Of Enlightenment":
      - Player: "Hail"
        - NPC emote: eyes you with an ageless wisdom.
        - NPC say: Ah, your spirit shines brightly. Should I know you?
        - Condition: `(e.other:Class() == "Shaman")`
        - Condition: `(e.other:HasItem(10651) or e.other:HasItem(36223) or qglobals["shaman_pre"] == "3")`
        - Condition: `(e.message:findi("hail"))`
      - Player: "Shaman" (link: external event mention)
        - Prompted by `event_trade`:
          - NPC say: You have heard the stories of the blessings bestowed on some of Norrath's most faithful to the ways of the heyokah. To reward you for all that you've done, the spirits have chosen to bless this talisman and offer it to you as our thanks, for without you, all shaman would have suffered without our presence in this realm. Walk proud, heyokah, and never forget what you are.' All around you, you feel the strength of the spirit world begin to strengthen as the spirit leaves to tend to his wounded companions.
          - Event guard: `(qglobals["shaman_epic"] == "14" and item_lib.check_turn_in(e.trade, {item1 = 57400}))`
        - NPC say: Ah, yes. You are not only a shaman, but one who has passed the tests of the heyokah. There are many problems that face us now and I grow weaker by the day. If you feel you are ready to bear a great burden and help all of those like us, including the immortals that charge our essence and consciousness, say [it is so].
        - Condition: `(e.other:Class() == "Shaman")`
        - Condition: `(e.other:HasItem(10651) or e.other:HasItem(36223) or qglobals["shaman_pre"] == "3")`
        - Condition: `(e.message:findi("shaman"))`
        - Sets `shaman_epic` to `1`.
      - Player: "Hail" (link: conversation sequence)
        - NPC say: Should you choose to continue your journey, tell me that you are [prepared to carry on] and save the spirits.
        - Condition: `(e.other:Class() == "Shaman")`
        - Condition: `(e.message:findi("hail") and e.other:HasItem(57400))`
      - Player: "Hail" (link: conversation sequence)
        - NPC say: It appears you are not yet ready for the great tasks that I require to be done. There are others lesser than me that can guide you and prepare you to walk a greater path should you choose. You should seek them out. You can perhaps seek knowledge from your elders and peers.
        - Condition: `(e.other:Class() == "Shaman")`
        - Condition: ``
        - Condition: `(e.message:findi("hail"))`
        - Sets `shaman_pre` to `1`.
      - Player: "It Is So" (link: explicit mention)
        - Prompted by player input: "Shaman"
        - NPC say: To have you here, believing in us and our existence does give me warmth, but my length of time here and others like me may be at an end. The spirits are troubled and a darkness washes through our existence that we seem helpless to prevent. That is why I talk to you now -- to help us. Without the help of mortals, we may [blow away] with the winds.
        - Condition: `(e.other:Class() == "Shaman")`
        - Condition: `(e.message:findi("it is so") and qglobals["shaman_epic"] == "1")`
      - Player: "Blow Away" (link: explicit mention)
        - NPC say: You have heard of the darkness in Taelosia that came from another place. You may have even seen the world that is overshadowed by the dark influence of Discord. That seeping ill that is not touchable by claw or paw has wormed its way into the [streams of the spirit world] and the more it does, the more we, and I weaken.
        - Condition: `(e.other:Class() == "Shaman")`
        - Condition: `(e.message:findi("blow away") and qglobals["shaman_epic"] == "1")`
      - Player: "Streams Of The Spirit World" (link: explicit mention)
        - NPC say: Yes, it is true. I feel myself fading more with each turn of time. You are familiar with the ways of herbs and potions and you can aid me, should you [find the will]. With strength to keep me before you in the mortal realm, I can guide you so that you may aid us all. There is much to tell you that I will not reveal yet, lest you be tempted to take advantage -- which has happened before.
        - Condition: `(e.other:Class() == "Shaman")`
        - Condition: `(e.message:findi("streams of the spirit world") and qglobals["shaman_epic"] == "1")`
      - Player: "Find The Will" (link: explicit mention)
        - NPC say: Very well. You will not find this an easy task. There are several things you must do and other heyokah you must find that have helped us in the past. Where there is glitter upon the setting of Ro, you will find an agent of the spirits. In the deep waters where the megalodon is said to hunt, there is another. And where the wonders of nature rise in the dark, another ally awaits. Look for light in the denseness of entwined shadows. One will greet you with all you have learned. She is doing research in a bustling labyrinth of creatures and can educate you where I cannot. Tell them all of me and they will give you audience
        - Condition: `(e.other:Class() == "Shaman")`
        - Condition: `(e.message:findi("find the will") and qglobals["shaman_epic"] == "1")`
      - Player: "Wasichu"
        - NPC say: The wasichu are those that turn their backs on serving the spirit world for its own sake. They hunger for their own power. At greater risk now are the spirits of Wisdom and Patience. They have become weakened and their fading is eroding what you as shaman often rely upon. The Spirit of Might has lost its way altogether and has crossed over into the darkness of Discord in that other realm. It has been moving amongst the [dark creatures] there, using its influence to guide and move some beasts in strange ways.
        - Condition: `(e.other:Class() == "Shaman")`
        - Condition: `(e.message:findi("wasichu") and qglobals["shaman_epic"] == "2")`
      - Player: "Dark Creatures" (link: explicit mention)
        - NPC say: We must prepare a [ritual] that has not been performed in many, many years. We hope this one ritual will return the strength of the failing spirits and restore the honor and humility of the Spirit of Might, but there is much preparation to be done. If you are prepared to take on this task, I will tell you what I know. This is no small endeavor, friend. Your mind and body and your strength of spirit will be put to the test.
        - Condition: `(e.other:Class() == "Shaman")`
        - Condition: `(e.message:findi("dark creatures") and qglobals["shaman_epic"] == "2")`
      - Player: "Ritual" (link: explicit mention)
        - NPC say: The ritual we need to perform is an ancient one, called Ruchu, and it will require a lot of preparation and planning on our parts. To begin with, we need to call upon our allies for help. One thing we need is spirit talismans. In times past, the spirits bestowed very powerful talismans upon a few, but [great heyokah]. We are going to need some of them to perform this ritual as they contain some of the essence of the very beings we are tying to save.
        - Condition: `(e.other:Class() == "Shaman")`
        - Condition: `(e.message:findi("ritual") and qglobals["shaman_epic"] == "2")`
      - Player: "Great Heyokah" (link: explicit mention)
        - NPC say: One of them was a [wise] shaman who once walked the lands and gathered every morsel of wisdom his mind could consume in the ways of alchemy and magic. Even though he was a froglok, he was incredibly gifted. His name was Juktopp Gantroc. Though he was small in stature, his knowledge seemed an endless expanse.
        - Condition: `(e.other:Class() == "Shaman")`
        - Condition: `(e.message:findi("great heyokah") and qglobals["shaman_epic"] == "2")`
      - Player: "Wise" (link: explicit mention)
        - NPC say: We had [watched] him and were amazed by the depth and breadth of his knowledge and how he applied it to his arts. Over time, he began to learn things that we did not know or piece together ourselves, adding great value to the spirits and shaman everywhere.
        - Condition: `(e.other:Class() == "Shaman")`
        - Condition: `(e.message:findi("wise") and qglobals["shaman_epic"] == "2")`
      - Player: "Watched" (link: explicit mention)
        - NPC say: Upon his death, which he made no attempts to prevent and he likely could have, he accepted the passage from the confines of flesh into the spirit world with great grace and dignity. Several of us spirits gathered that night and chose to appear to him and offer him a [rare gift]... a place among the everlasting spirits where he could share his knowledge and continue to learn.
        - Condition: `(e.other:Class() == "Shaman")`
        - Condition: `(e.message:findi("watched") and qglobals["shaman_epic"] == "2")`
      - Player: "Rare Gift" (link: explicit mention)
        - NPC say: The Spirit of Wisdom itself blessed a talisman and gave it to Juktopp, telling him of our offer. Needless to say, he was overwhelmed and overjoyed. To this day, he remains light as air and just as free in a planar realm of great beauty. You must find him and retrieve the talisman. Give him this potion which will sustain him while we prepare for Ruchu. There is [still more] you must do.
        - Condition: `(e.other:Class() == "Shaman")`
        - Condition: `(e.message:findi("rare gift") and qglobals["shaman_epic"] == "2")`
        - Gives Potion of Sustenance (57081).
      - Player: "Still More" (link: explicit mention)
        - NPC say: When the gods were still young and the ethereal planes were not much more than imagination, the Tribunal wished to create an infallible system of justice. They also wanted those who approached them to hear or plead their case to have their resolve tested so the Tribunal's time would not be wasted. Thus, the Tribunal chose to create [trials of justice] so that Norrathians would be required to prove their worth to have their case heard.
        - Condition: `(e.other:Class() == "Shaman")`
        - Condition: `(e.message:findi("still more") and qglobals["shaman_epic"] == "2")`
      - Player: "Trials Of Justice" (link: explicit mention)
        - NPC say: But it was not that simple. It did take some time to decide how the trials would be created so that they were fair and just and would provide a good test of strength and might. There was a high shaman of Halas who followed the path lain by the Tribunal and lived his life according to law and justice. His name was [Veshtaq] MacDunahon.
        - Condition: `(e.other:Class() == "Shaman")`
        - Condition: `(e.message:findi("trials of justice") and qglobals["shaman_epic"] == "2")`
      - Player: "Veshtaq" (link: explicit mention)
        - NPC say: Veshtaq's strict adherence to justice eventually earned the attention of the Tribunal and he was asked to ascend from the mortal realm to aid them in creating trials that would be suitable to place before Norrathians wishing to approach the greatness of the Tribunal. Of course, Veshtaq obliged and [succeeded] in creating a series of trials that allowed Norrathians to prove their worth.
        - Condition: `(e.other:Class() == "Shaman")`
        - Condition: `(e.message:findi("veshtaq") and qglobals["shaman_epic"] == "2")`
      - Player: "Succeeded" (link: explicit mention)
        - NPC say: When his work was done, Veshtaq suddenly realized that he had grown much older and his time in the land had weakened his ties with the natural spirits of the world. This [troubled] him greatly. He felt his life perhaps had come to no real meaning.
        - Condition: `(e.other:Class() == "Shaman")`
        - Condition: `(e.message:findi("succeeded") and qglobals["shaman_epic"] == "2")`
      - Player: "Troubled" (link: explicit mention)
        - NPC say: Somehow, the Tribunal then became aware of Veshtaq's concerns and passed a judgment -- that Ceshtaq be granted a place among the trials he created, becoming immortal. With that judgment, the Tribunal had contacted one of the great spirits, that of Patience, and asked for a [meaningful way] for a shaman to become immortal.
        - Condition: `(e.other:Class() == "Shaman")`
        - Condition: `(e.message:findi("troubled") and qglobals["shaman_epic"] == "2")`
      - Player: "Meaningful Way" (link: explicit mention)
        - NPC say: For a shaman, a blessing of eternal life from any spirit is an honor, so a talisman was created by the Spirit of Patience to sustain Veshtaq for all time and he would be once again be rejoined with the spirit world. Now, , it is up to you to retrieve the talisman. You may not simply ask for it. You will have to complete the very trial he commands and defeat his essence. Do not fret. The Tribunal will sustain him in that plane so he may continue his work.
        - Condition: `(e.other:Class() == "Shaman")`
        - Condition: `(e.message:findi("meaningful way") and qglobals["shaman_epic"] == "2")`
      - Player: "Stolen" (link: external event mention)
        - Prompted by `event_trade`:
          - NPC say: This is a start. There is still much to do. While we have gotten the talismans from our allies, there are those that are not our friends -- the wasichu and worse -- who carry or have [stolen] items we need. They will not part with them willingly. This is where your strength and might will be put to the test . . . and your presence of mind. Are you certain you wish to go on?
          - Event guard: `(qglobals["shaman_epic"] == "2" and item_lib.check_turn_in(e.trade, {item1 = 57083, item2 = 57084}))`
        - NPC say: Very well. You will need to return to Wunshi for more information. He will be able to lead you to some of what we need if you ask him. Return to me and tell me when your business with Wunshi is finished. I am too tired to continue.
        - Condition: `(e.other:Class() == "Shaman")`
        - Condition: `(e.message:findi("stolen") and qglobals["shaman_epic"] == "3")`
      - Player: "business with Wunshi is finished" (link: explicit mention)
        - NPC say: Is that so? I am both grateful and anxious. My sight into the spirit world grows darker with each hour. You have done well, but I am ever fearful that we are not moving quickly enough. You must use all of your skills for your next task. Return to Kimm McShannel and when you return to me, tell me that you have created the potion. Show her this bangle.
        - Condition: `(e.other:Class() == "Shaman")`
        - Condition: `(e.message:findi("business with Wunshi is finished") and qglobals["shaman_epic"] == "4")`
        - Gives Gemmed Bangle of Enlightenment (57088).
      - Player: "Take Part" (link: external event mention)
        - Prompted by `event_trade`:
          - NPC say: I will have to pass these along as soon as my messenger gets here. I'm sure you understand that as each spirit loses strength, each of our abilities to keep a form in this tangible world becomes very difficult. We must find a way to sustain a physical presence here or the Ruchu will be in jeopardy. We will ask you to [take part] in the ceremony where our strength may fail us.
          - Event guard: `(qglobals["shaman_epic"] == "5" and item_lib.check_turn_in(e.trade, {item1 = 57614}))`
        - NPC say: We are still a long way from that, but I feel it is time to [acknowledge] you as a true shaman spirit that has earned the respect of many spirits of the world.
        - Condition: `(e.other:Class() == "Shaman")`
        - Condition: `(e.message:findi("take part") and qglobals["shaman_epic"] == "6")`
      - Player: "Acknowledge" (link: explicit mention)
        - NPC say: We, the spirits, have chosen to grant you a gift for all that you've done for us and what you still have left to do. It is just a sampling of the power you may obtain one day as you move forward as one of the heyokah. Guard it and use it well. Should you choose to continue your journey, tell me that you are [prepared to carry on] and save the spirits.
        - NPC message: You have gained 5 ability points!
        - Condition: `(e.other:Class() == "Shaman")`
        - Condition: `(e.message:findi("acknowledge") and qglobals["shaman_epic"] == "6")`
        - Gives Crafted Talisman of Fates (57400).
        - Sets `shaman_epic` to `7`.
      - Player: "Prepared To Carry On" (link: explicit mention)
        - NPC say: I knew we could count on you, . The time for Ruchu is drawing ever nearer, but we still must gather some essential elements. Soon, you will have to cross the barrier into that realm of Discord. Lupot Nukla can help you.
        - Condition: `(e.other:Class() == "Shaman")`
        - Condition: `(e.message:findi("prepared to carry on") and e.other:HasItem(57400))`
        - Sets `shaman_epic` to `8`.
      - Player: "Discord" (link: explicit mention)
        - NPC say: We know the Spirit of Might is beginning to disperse not just in Norrath, but that place shadowed by Discord as well. The spirit has passed through many beasts and is corrupting them, each one commanded by a trace of the spirit. You must find several beasts and find those traces of the wasichu. One is an airy, fluid creature. Yet another is a fierce beast that has grown beyond all normal proportions because of the spirit of Might. You must find them. And there are still others you must [seek].
        - Condition: `(e.other:Class() == "Shaman")`
        - Condition: `(e.message:findi("discord") and qglobals["shaman_epic"] == "11")`
      - Player: "Seek" (link: explicit mention)
        - NPC say: The other creature you must find is a soldier of evil. Another is an scurrying creature that is not bound to our realm. You have much ahead of you. Take this pouch and carefully piece together everything you find and return it to me. You will know how to do it. The spirits will guide you.
        - Condition: `(e.other:Class() == "Shaman")`
        - Condition: `(e.message:findi("seek") and qglobals["shaman_epic"] == "11")`
        - Gives Pouch of Spirit Dust (57710).
      - Player: "Spiritcaller"
        - NPC say: The fiend that is consuming our spirits is in Discord and is siphoning what little energy and strength we have remaining. We are losing ourselves in the passage of Discord. Without the spirits of Might, Patience, and Wisdom, we may not [survive]. We are not whole without them.
        - Condition: `(e.other:Class() == "Shaman")`
        - Condition: `(e.message:findi("spiritcaller") and qglobals["shaman_epic"] == "12")`
      - Player: "Survive" (link: explicit mention)
        - NPC say: Make your way to a place of great suffering and death in Kuua. You will need to investigate to help us learn more about our waning spirits. We have no influence there and it is a wholly unpredictable place.
        - Condition: `(e.other:Class() == "Shaman")`
        - Condition: `(e.message:findi("survive") and qglobals["shaman_epic"] == "12")`
      - Player: "Prepared For The Ceremony" (link: external event mention)
        - Prompted by `event_trade`:
          - NPC say: lowers its head and you believe you see a shade of a tear drop from its eyes and disappear into nothingness. 'You have done it. You cannot imagine our gratitude. The time for Ruchu is at hand and we offer you the privilege of taking part. If you are able to do the ceremony now, tell me you are [prepared for the ceremony].'
          - Event guard: `(qglobals["shaman_epic"] == "13" and item_lib.check_turn_in(e.trade, {item1 = 47100}))`
        - NPC say: Follow me closely. We must gather the spirits and try to call our ethereal kin of Might, Patience, and Wisdom. The other spirits will join us for Ruchu, namely the Spirit of Perseverance, Spirit of Understanding, Spirit of Fortitude, Spirit of Will, and the Spirit of Sense.
        - Condition: `(e.other:Class() == "Shaman")`
        - Condition: `(e.message:findi("prepared for the ceremony") and qglobals["shaman_epic"] == "14" and char_id == 0)`
      - Player: "Faithful Heyokah" (link: conversation sequence)
        - NPC say: Well, then, the time has come. Give me your Crafted Talisman of Fates, heyokah. Should you not have it now, give it to me when you do. If you have lost it, tell me so. I may be able to help you.
        - Condition: `(e.other:Class() == "Shaman")`
        - Condition: `(e.message:findi("faithful heyokah") and qglobals["shaman_epic"] == "14")`

2. lakeofillomen/"Spirit Sentinel", hand "Black Fur Boots" (1678). Sets `shaman_pre` to `2`.
    - Requires `shaman_pre` ==1.
    - Requires `shaman_pre` set.
    - Hand in x1: "Black Fur Boots" (1678).
    - Prerequisite: "Black Fur Boots" (1678). See section 0.
    - Dialogue with lakeofillomen/"Spirit Sentinel":
      - Player: "Hail"
        - NPC say: Ah so the Elder Spirit of Enlightenment has sent you to me. I do have a task for you if you wish to help the cause of the spirits across the lands. I have been charged with making an elixer that will aid the spirits for a time. Are you [interested] in aiding us?
        - Condition: `(defined $qglobals{shaman_pre} && $qglobals{shaman_pre} == 1)`
        - Condition: `($text=~/hail/i)`
      - Player: "Interested" (link: explicit mention)
        - NPC say: Very well then. First you must do what you can to prove yourself to our kind. There are some tests you must perform in order to gain our trust. At the end of this path, we may consider you one of the Heyokah -- the most trusted of those align themselves with shaman everywhere. You will be required to take on the tests of Patience, Wisdom, and Might. Bring me the Black fur Boots you receive to me.
        - Condition: `(defined $qglobals{shaman_pre} && $qglobals{shaman_pre} == 1)`
        - Condition: `($text=~/interested/i)`
      - Player: "Ingredients" (link: external event mention)
        - Prompted by `event_item`:
          - NPC say: You can now be called a heyokah, but there is much you may still do. I do require several [ingredients] for the potion I am required to make and should you assist me, there is a spirit with even greater tasks that will give you audience.
          - Event guard: `(defined $qglobals{shaman_pre} && $qglobals{shaman_pre} == 1 && plugin::check_handin(\%itemcount, 1678 =>1 ))`
        - NPC say: I will need some unique blood from a crystal-like spider from a valorous plane, a special leaf that an insect of the diseased hordes eats whole and antennae from a skittering bug in Taelosia. I will also need you to make your way into the deserts of Ro and find a lonely merchant who sells a unique vial I require. Return all of these to me and you will find yourself able to walk a greater path.
        - Condition: `(defined $qglobals{shaman_pre} && $qglobals{shaman_pre} == 2)`
        - Condition: `($text=~/ingredients/i)`

3. lakeofillomen/"Spirit Sentinel", hand "Crystallized Blood" (57988) + "Mellian Leaf" (57989) + "Stonemite Antennae" (57990) + "Clouded Glass Vial" (57991). Sets `shaman_pre` to `3`.
    - Requires `shaman_pre` set.
    - Hand in x1: "Crystallized Blood" (57988).
    - Hand in x1: "Clouded Glass Vial" (57991).
    - Hand in x1: "Stonemite Antennae" (57990).
    - Hand in x1: "Mellian Leaf" (57989).
    - Loot "Crystallized Blood" (57988) from "A Crystalline Arachnae" in `povalor`.
    - Given by southro/"Bratoq Jiplup", hand platinum:2000.
    - Loot "Stonemite Antennae" (57990) from "A Shore Stonemite" (NPC 280005) in `natimbi`. Drop cache: 93.14% chance per kill.
    - Loot "Mellian Leaf" (57989) from "A Malarian Crysalis" in `podisease`.

#### Steps on `shaman_pre` that do not change it

- `freeportwest` elder spirit of enlightenment, say shaman needs `shaman_pre` ==3.
  - Sets `shaman_epic` to `1`.
- `freportn` elder spirit of enlightenment, say shaman needs `shaman_pre` ==3.
  - Sets `shaman_epic` to `1`.

### `shaman_epic`

Values written: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15.

1. freeportwest/"Elder Spirit Of Enlightenment", say "Shaman". Sets `shaman_epic` to `1`.
    - Requires `shaman_epic` unset.
    - Requires `shaman_pre` ==3.
    - Requires one of: "Spear of Fate" (10651); "Spear of Fate" (36223).
    - Prerequisite: "Spear of Fate" (10651). See section 0.
    - Same item as "Spear of Fate" (10651).
    - Given by emeraldjungle/"Spirit Sentinel", hand "Iksar Scale" (1674).

    - Subquest `shaman_pre` documented earlier.
2. freeportwest/"Elder Spirit Of Enlightenment", hand "Distilled Potion of Endurance" (52921). Sets `shaman_epic` to `2`.
    - Requires `shaman_epic` ==1.
    - Hand in x1: "Distilled Potion of Endurance" (52921).
    - Prerequisite: "Distilled Potion of Endurance" (52921). See section 0.

3. freeportwest/"Elder Spirit Of Enlightenment", hand "Blessed Talisman of Wisdom" (57083) + "Blessed Talisman of Patience" (57084). Sets `shaman_epic` to `3`.
    - Requires `shaman_epic` ==2.
    - Hand in x1: "Blessed Talisman of Wisdom" (57083).
    - Hand in x1: "Blessed Talisman of Patience" (57084).
    - Prerequisite: "Blessed Talisman of Wisdom" (57083). See section 0.
    - Loot "Blessed Talisman of Patience" (57084) from "Punisher Veshtaq".

4. shadeweaver/"Wunshi Kashra", hand "Ring of the Undead Spiritcharmer" (57085) + "Amulet of the Spiritist" (57087). Sets `shaman_epic` to `4`.
    - Requires `shaman_epic` ==3.
    - Hand in x1: "Amulet of the Spiritist" (57087).
    - Hand in x1: "Ring of the Undead Spiritcharmer" (57085).
    - Loot "Amulet of the Spiritist" (57087) from "Netherbian Swarmfiend" in `umbral`.
    - Spawns "Spiritseeker Nadox" (227319) in `nadox` on enter.
    - Loot "Ring of the Undead Spiritcharmer" (57085) from "Spiritseeker Nadox".
    - Dialogue with shadeweaver/"Wunshi Kashra":
      - Player: "Elder Spirit Sent Me"
        - NPC say: Ah, another courageous alchemist after my own heart. I've been so worried and consumed by aiding the spirits that I'd forgotten how much time I'd spent here. Anyway, no matter. If you give me 1000 platinum pieces, I will give you the medicine bag you will need to work the potion for the spirit. I hate to ask for money, but this bag has cost me four times that to make. It's a long process that requires the magic of some very rare and expensive materials. We are dealing with wisps of consciousness, after all.
        - Condition: `(e.message:findi("elder spirit sent me") and qglobals["shaman_epic"] == "1")`
      - Player: "Hail" (link: conversation sequence)
        - NPC say: I am glad to see you do all you can to aid the spirits. Their grasp on existence grows weaker every day and it breaks my heart. With you, though, we may stand a chance. Now, it is up to you to find two dark creatures that carry some treasures that we need and they will not be willing to part with them. First you must find a [gruesome being] whose goal is to steal spirits to make it stronger. It wears a ring that it obtained from an evil enchanter who used it to charm the very spirits of its prey. The [second beast] is just as foul.
        - Condition: `(e.message:findi("hail") and qglobals["shaman_epic"] == "3")`
      - Player: "Gruesome Being" (link: explicit mention)
        - NPC say: This creature is found far across the seas and exists between life and death. It is quite frightful to behold amongst its followers. Good luck to you, my friend. Return the ring to me and I will guide you further.
        - Condition: `(e.message:findi("gruesome being") and qglobals["shaman_epic"] == "3")`
      - Player: "Second Beast" (link: explicit mention)
        - Prompted by player input: "Hail"
        - NPC say: The second creature is a strange and powerful beast that seeks to increase the number of its followers by overcoming them with intimidation. I am embarrassed to say that he had [stolen] a special gift from me -- a gift given to me by the elder spirits when I had proven my dedication and worth.
        - Condition: `(e.message:findi("second beast") and qglobals["shaman_epic"] == "3")`
      - Player: "Stolen" (link: explicit mention)
        - NPC say: The vermin that stole it now abuses it to gain control over spirits it wants to command. It is a peculiar beast that lives way up in the heavens on the moon. It is not often seen, so your timing must be right. Return its amulet to me when you obtain it. We will all be better off without this creature lurking about.
        - Condition: `(e.message:findi("stolen") and qglobals["shaman_epic"] == "3")`
        - Sets `shaman_epic_nadox` to `1`.

5. lakerathe/"Kimm Mcshannel", hand "Gemmed Bangle of Enlightenment" (57088). Sets `shaman_epic` to `5`.
    - Hand in x1: "Gemmed Bangle of Enlightenment" (57088).
    - Prerequisite: "Gemmed Bangle of Enlightenment" (57088). See section 0.
    - Dialogue with lakerathe/"Kimm Mcshannel":
      - Player: "Elder Spirit Sent Me"
        - NPC say: Aye, well then. Watch yerself. Thar be a crazy fella over there. Been trying for days, I 'ave, to get 'im to make some sense about this megalodon creature 'e keeps prattling on about. I been a bit shy o' stepping in the lake to get some seaweed for the spirit's potion. Maybe you could go take a look. Somethin' usually comes by to snap 'em up when they grow, so ye may need to route around a tad out there. You think you are [up to it]?
        - Condition: `(e.message:findi("elder spirit sent me") and qglobals["shaman_epic"] == "1")`
      - Player: "Up To It" (link: explicit mention)
        - NPC say: Very well, then, off you go in search of the seaweed.
        - Condition: `(e.message:findi("up to it") and qglobals["shaman_epic"] == "1")`
        - Spawns NPC 51160.
      - Player: "Break Down" (link: external event mention)
        - Prompted by `event_trade`:
          - NPC say: Aye, so ye have returned. We have much to do here, me friend. The first thing we must do is [break down] this bangle into its gems and metal. This here bangle was very carefully made. First, the gems were blessed by the spirits, then the metal itself as it was forged. Aye, we need to carefully separate them. The two gems were blessed by the spirits of Wisdom and Patience, and the metal was strengthened by the Spirit of Might. We will use these to call them back to us.
          - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 57088}))`
        - NPC say: As most things, the process is not a simple one and we'll need some ingredients for a special potion. You must retrieve four items, which should not prove difficult for a shaman of your stature. They are very specific and I can tell you more about the [skin], the [powder], the [tooth], and the [goo]. When you have all of these things, use my medicine bag to create this potion and return it to me.
        - Condition: `(e.message:findi("break down") and qglobals["shaman_epic"] == "5")`
        - Gives Heyokah Medicine Bag (52922).
      - Player: "Skin" (link: explicit mention)
        - NPC say: First, you must find your way to Kuua for part of the potion. There you will find a foul hound of flesh with no fur and fangs. We need a perfect specimen of some of its skin for our potion. Three should do nicely.
        - Condition: `(e.message:findi("skin") and qglobals["shaman_epic"] == "5")`
      - Player: "Powder" (link: explicit mention)
        - Prompted by player input: "Break Down"
        - NPC say: The powder is very unique and can be difficult to obtain -- many have died trying as it's a coveted magic. There is an undead fiend that uses this powder to turn many creatures and darken them. It is a beast in a sickly plane which makes it that much more challenging, of course. This powder is needed so that we can use a pinch of it to attract the Spirit of Might close enough to us to have it turn its back on the path of the wasichu.
        - Condition: `(e.message:findi("powder") and qglobals["shaman_epic"] == "5")`
      - Player: "Tooth" (link: explicit mention)
        - Prompted by player input: "Break Down"
        - NPC say: In suffocating lands, there are a few revenants with a marrow that we need. It's a rather unpleasant task and I'm sure they won't cooperate. You must find four of their teeth.
        - Condition: `(e.message:findi("tooth") and qglobals["shaman_epic"] == "5")`
      - Player: "Goo" (link: explicit mention)
        - Prompted by player input: "Break Down"
        - NPC say: The goo is very special and will provide a strong acidic base for the agent we are creating. You will find it deep where the spirits groan and drift, where it seems even the walls howl in agony. There is only one creature that produces this goo that we use to separate gem from metal. It is very deep within that place. You should try to obtain two samples of goo.
        - Condition: `(e.message:findi("goo") and qglobals["shaman_epic"] == "5")`
      - Player: "Elder Spirit Sent Me"
        - NPC say: Aye, well then. Watch yerself. Thar be a crazy fella over there. Been trying for days, I 'ave, to get 'im to make some sense about this megalodon creature 'e keeps prattling on about. I been a bit shy o' stepping in the lake to get some seaweed for the spirit's potion. Maybe you could go take a look. Somethin' usually comes by to snap 'em up when they grow, so ye may need to route around a tad out there. You think you are [up to it]?
        - Condition: `(defined($qglobals{shaman_epic}) && ($qglobals{shaman_epic} == 1))`
        - Condition: `($text=~/elder spirit sent me/i)`
      - Player: "Up To It" (link: explicit mention)
        - NPC say: Very well, then, off you go in search of the seaweed.
        - Condition: `(defined($qglobals{shaman_epic}) && ($qglobals{shaman_epic} == 1))`
        - Condition: `($text=~/up to it/i)`
        - Spawns NPC 51160.
      - Player: "Break Down" (link: external event mention)
        - Prompted by `event_item`:
          - NPC say: Aye, so ye have returned. We have much to do here, me friend. The first thing we must do is [break down] this bangle into its gems and metal. This here bangle was very carefully made. First, the gems were blessed by the spirits, then the metal itself as it was forged. Aye, we need to carefully separate them. The two gems were blessed by the spirits of Wisdom and Patience, and the metal was strengthened by the Spirit of Might. We will use these to call them back to us.
          - Event guard: `(plugin::check_handin(\%itemcount, 57088 => 1))`
        - NPC say: As most things, the process is not a simple one and we'll need some ingredients for a special potion. You must retrieve four items, which should not prove difficult for a shaman of your stature. They are very specific and I can tell you more about the [skin], the [powder], the [tooth], and the [goo]. When you have all of these things, use my medicine bag to create this potion and return it to me.
        - Condition: `(defined($qglobals{shaman_epic}) && ($qglobals{shaman_epic} == 3))`
        - Condition: `($text=~/break down/i)`
        - Gives Heyokah Medicine Bag (52922).
      - Player: "Skin" (link: explicit mention)
        - NPC say: First, you must find your way to Kuua for part of the potion. There you will find a foul hound of flesh with no fur and fangs. We need a perfect specimen of some of its skin for our potion. Three should do nicely.
        - Condition: `(defined($qglobals{shaman_epic}) && ($qglobals{shaman_epic} == 3))`
        - Condition: `($text=~/skin/i)`
      - Player: "Powder" (link: explicit mention)
        - Prompted by player input: "Break Down"
        - NPC say: The powder is very unique and can be difficult to obtain -- many have died trying as it's a coveted magic. There is an undead fiend that uses this powder to turn many creatures and darken them. It is a beast in a sickly plane which makes it that much more challenging, of course. This powder is needed so that we can use a pinch of it to attract the Spirit of Might close enough to us to have it turn its back on the path of the wasichu.
        - Condition: `(defined($qglobals{shaman_epic}) && ($qglobals{shaman_epic} == 3))`
        - Condition: `($text=~/powder/i)`
      - Player: "Tooth" (link: explicit mention)
        - Prompted by player input: "Break Down"
        - NPC say: In suffocating lands, there are a few revenants with a marrow that we need. It's a rather unpleasant task and I'm sure they won't cooperate. You must find four of their teeth.
        - Condition: `(defined($qglobals{shaman_epic}) && ($qglobals{shaman_epic} == 3))`
        - Condition: `($text=~/tooth/i)`
      - Player: "Goo" (link: explicit mention)
        - Prompted by player input: "Break Down"
        - NPC say: The goo is very special and will provide a strong acidic base for the agent we are creating. You will find it deep where the spirits groan and drift, where it seems even the walls howl in agony. There is only one creature that produces this goo that we use to separate gem from metal. It is very deep within that place. You should try to obtain two samples of goo.
        - Condition: `(defined($qglobals{shaman_epic}) && ($qglobals{shaman_epic} == 3))`
        - Condition: `($text=~/goo/i)`

6. freeportwest/"Elder Spirit Of Enlightenment", hand "Runed Purse of the McShannels" (57614). Sets `shaman_epic` to `6`.
    - Requires `shaman_epic` ==5.
    - Hand in x1: "Runed Purse of the McShannels" (57614).
    - Prerequisite: "Runed Purse of the McShannels" (57614). See section 0.

7. freeportwest/"Elder Spirit Of Enlightenment", say "Acknowledge". Sets `shaman_epic` to `7`.
    - Requires `shaman_epic` ==6.
    - Gives "Crafted Talisman of Fates" (57400).

Alternative or repeat transition to `shaman_epic` = `7` (not an additional required stage).

7. freportn/"Elder Spirit Of Enlightenment", say "Acknowledge". Sets `shaman_epic` to `7`.
    - Requires `shaman_epic` ==6.
    - Gives "Crafted Talisman of Fates" (57400).
    - Dialogue with freportn/"Elder Spirit Of Enlightenment":
      - Player: "Hail"
        - NPC emote: eyes you with an ageless wisdom.
        - NPC say: Ah, your spirit shines brightly. Should I know you?
        - Condition: `(e.other:Class() == "Shaman")`
        - Condition: `(e.other:HasItem(10651) or e.other:HasItem(36223) or qglobals["shaman_pre"] == "3")`
        - Condition: `(e.message:findi("hail"))`
      - Player: "Shaman" (link: external event mention)
        - Prompted by `event_trade`:
          - NPC say: You have heard the stories of the blessings bestowed on some of Norrath's most faithful to the ways of the heyokah. To reward you for all that you've done, the spirits have chosen to bless this talisman and offer it to you as our thanks, for without you, all shaman would have suffered without our presence in this realm. Walk proud, heyokah, and never forget what you are.' All around you, you feel the strength of the spirit world begin to strengthen as the spirit leaves to tend to his wounded companions.
          - Event guard: `(qglobals["shaman_epic"] == "14" and item_lib.check_turn_in(e.trade, {item1 = 57400}))`
        - NPC say: Ah, yes. You are not only a shaman, but one who has passed the tests of the heyokah. There are many problems that face us now and I grow weaker by the day. If you feel you are ready to bear a great burden and help all of those like us, including the immortals that charge our essence and consciousness, say [it is so].
        - Condition: `(e.other:Class() == "Shaman")`
        - Condition: `(e.other:HasItem(10651) or e.other:HasItem(36223) or qglobals["shaman_pre"] == "3")`
        - Condition: `(e.message:findi("shaman"))`
        - Sets `shaman_epic` to `1`.
      - Player: "Hail" (link: conversation sequence)
        - NPC say: Should you choose to continue your journey, tell me that you are [prepared to carry on] and save the spirits.
        - Condition: `(e.other:Class() == "Shaman")`
        - Condition: `(e.message:findi("hail") and e.other:HasItem(57400))`
      - Player: "Hail" (link: conversation sequence)
        - NPC say: It appears you are not yet ready for the great tasks that I require to be done. There are others lesser than me that can guide you and prepare you to walk a greater path should you choose. You should seek them out. You can perhaps seek knowledge from your elders and peers.
        - Condition: `(e.other:Class() == "Shaman")`
        - Condition: ``
        - Condition: `(e.message:findi("hail"))`
        - Sets `shaman_pre` to `1`.
      - Player: "It Is So" (link: explicit mention)
        - Prompted by player input: "Shaman"
        - NPC say: To have you here, believing in us and our existence does give me warmth, but my length of time here and others like me may be at an end. The spirits are troubled and a darkness washes through our existence that we seem helpless to prevent. That is why I talk to you now -- to help us. Without the help of mortals, we may [blow away] with the winds.
        - Condition: `(e.other:Class() == "Shaman")`
        - Condition: `(e.message:findi("it is so") and qglobals["shaman_epic"] == "1")`
      - Player: "Blow Away" (link: explicit mention)
        - NPC say: You have heard of the darkness in Taelosia that came from another place. You may have even seen the world that is overshadowed by the dark influence of Discord. That seeping ill that is not touchable by claw or paw has wormed its way into the [streams of the spirit world] and the more it does, the more we, and I weaken.
        - Condition: `(e.other:Class() == "Shaman")`
        - Condition: `(e.message:findi("blow away") and qglobals["shaman_epic"] == "1")`
      - Player: "Streams Of The Spirit World" (link: explicit mention)
        - NPC say: Yes, it is true. I feel myself fading more with each turn of time. You are familiar with the ways of herbs and potions and you can aid me, should you [find the will]. With strength to keep me before you in the mortal realm, I can guide you so that you may aid us all. There is much to tell you that I will not reveal yet, lest you be tempted to take advantage -- which has happened before.
        - Condition: `(e.other:Class() == "Shaman")`
        - Condition: `(e.message:findi("streams of the spirit world") and qglobals["shaman_epic"] == "1")`
      - Player: "Find The Will" (link: explicit mention)
        - NPC say: Very well. You will not find this an easy task. There are several things you must do and other heyokah you must find that have helped us in the past. Where there is glitter upon the setting of Ro, you will find an agent of the spirits. In the deep waters where the megalodon is said to hunt, there is another. And where the wonders of nature rise in the dark, another ally awaits. Look for light in the denseness of entwined shadows. One will greet you with all you have learned. She is doing research in a bustling labyrinth of creatures and can educate you where I cannot. Tell them all of me and they will give you audience
        - Condition: `(e.other:Class() == "Shaman")`
        - Condition: `(e.message:findi("find the will") and qglobals["shaman_epic"] == "1")`
      - Player: "Wasichu"
        - NPC say: The wasichu are those that turn their backs on serving the spirit world for its own sake. They hunger for their wn power. At greater risk now are the spirits of Wisdom and Patience. They have become weakened and their fading is eroding what you as shaman often rely upon. The Spirit of Might has lost its way altogether and has crossed over into the darkness of Discord in that other realm. It has veen mobing amongst the [dark creatures] there, using its influence to guide and move some beasts in strange ways.
        - Condition: `(e.other:Class() == "Shaman")`
        - Condition: `(e.message:findi("wasichu") and qglobals["shaman_epic"] == "2")`
      - Player: "Dark Creatures" (link: explicit mention)
        - NPC say: We must prepare a [ritual] that has not been performed in many, many years. We hope this one ritual will return the strength of the failing spirits and restore the honor and humility of the Spirit of Might, but there is much preparation to be done. If you are prepared to take on this task, I will tell you what I know. This is no small endeavor, friend. Your mind and body and your strngth of spirit will be put to the test.
        - Condition: `(e.other:Class() == "Shaman")`
        - Condition: `(e.message:findi("dark creatures") and qglobals["shaman_epic"] == "2")`
      - Player: "Ritual" (link: explicit mention)
        - NPC say: The ritual we need to perform is an ancient one, called Ruchu, and it will require a lot of preparation and planning on our parts. To begin with, we need to call upon our allies for help. One thing we need is spirit talismans. In times past, the spirits bestowed very powerful talismans upon a few, but [great heyokah] heyokah. We are going to need some of them to perform this ritual as they contain some of the essence of the very beings we are tying to save.
        - Condition: `(e.other:Class() == "Shaman")`
        - Condition: `(e.message:findi("ritual") and qglobals["shaman_epic"] == "2")`
      - Player: "Great Heyokah" (link: explicit mention)
        - NPC say: One of them was a [wise] shaman who once walked the lands and gahered every morsel of wisfom his mind could consume in the ways of alchemy and magic. Even though he was a froglok, he was incrediby gifted. His name was Juktopp Gantroc. Though he was small in stature, his knoledge seemed and endless expanse.
        - Condition: `(e.other:Class() == "Shaman")`
        - Condition: `(e.message:findi("great heyokah") and qglobals["shaman_epic"] == "2")`
      - Player: "Wise" (link: explicit mention)
        - NPC say: We had [watched] him and were amazed by the depth and breadth of his knowledge and how he applied it to his arts. Over time, he began to learn things that we did not know or piece together ourselves, adding great value to the spirits and shaman everywhere.
        - Condition: `(e.other:Class() == "Shaman")`
        - Condition: `(e.message:findi("wise") and qglobals["shaman_epic"] == "2")`
      - Player: "Watched" (link: explicit mention)
        - NPC say: Upon his death, which he made no attempts to prevent and he likely could have, he accepted the passage from the confines of flesh into the spirit world with great grace and dignity. Several of us spirits gathered that night and chose to appear to him and offer him a [rare gift]... a place among the everlasting spirits where he could share his knowledge and continue to learn.
        - Condition: `(e.other:Class() == "Shaman")`
        - Condition: `(e.message:findi("watched") and qglobals["shaman_epic"] == "2")`
      - Player: "Rare Gift" (link: explicit mention)
        - NPC say: The Spirit of Wisdom itself blessed a talisman and gave it to Juktopp, telling him of our offer. Needless to say, he was overwhelmed and overjoyed. To this day, he remains light as air and just as free in a planar realm of great beauty. You must find him and retrieve the talisman. Give him this potion whihc will sustain him while we prepare for Ruchu. There is [still more] you must do.
        - Condition: `(e.other:Class() == "Shaman")`
        - Condition: `(e.message:findi("rare gift") and qglobals["shaman_epic"] == "2")`
        - Gives Potion of Sustenance (57081).
      - Player: "Still More" (link: explicit mention)
        - NPC say: When the gods were still young and the ethereal planes were not much more than imagination, the Tribunal wished to create an infallible system of justice. They also wanted those who approached them to hear or plead their casr to have their resolve tested so the Tribunal's time would not be wasted. Thus, the Tribunal chose to create [trials of justice] so that Norrathians would be required to prove thier worth to have thier case heard.
        - Condition: `(e.other:Class() == "Shaman")`
        - Condition: `(e.message:findi("still more") and qglobals["shaman_epic"] == "2")`
      - Player: "Trials Of Justice" (link: explicit mention)
        - NPC say: But it was not that simple. It did take some time to decide how the trials would be created so that they were fair and just and would provide a good test of strength and might. There was a high shaman of halas who followed th path lain by the Tribunal and lived his life according to law and justice. His name was [Veshtaq] MacDunahon.
        - Condition: `(e.other:Class() == "Shaman")`
        - Condition: `(e.message:findi("trials of justice") and qglobals["shaman_epic"] == "2")`
      - Player: "Veshtaq" (link: explicit mention)
        - NPC say: Veshtaq's strict asherence to justice eventually earned the attention of the Tribunal and he was asked to ascend from the mortal realm to aid them in creating trials that would be suitable to place before Norathians wishing to approach the greatness of the Tribunal. Of course, Veshtaq obliged and [succeeded] in creating a series of trials that allowed Norrathians to prove thier worth.
        - Condition: `(e.other:Class() == "Shaman")`
        - Condition: `(e.message:findi("veshtaq") and qglobals["shaman_epic"] == "2")`
      - Player: "Succeeded" (link: explicit mention)
        - NPC say: When his work was done, Veshtaq suddenly realized that he had grown much olde and his time in the lane had weakened his ties with the natual spirits of the world. This [troubled] him greatly. He felt his life perhaps had come to no real meaning.
        - Condition: `(e.other:Class() == "Shaman")`
        - Condition: `(e.message:findi("succeeded") and qglobals["shaman_epic"] == "2")`
      - Player: "Troubled" (link: explicit mention)
        - NPC say: Somehow, the Tribunal then became aware of Veshtaq's concerns and passed a judgment -- that Ceshtaq be granted a place among the trials he created, becoming immortal. With that judgment, the Tribunal had contacted one of the great spirits, that of Patience, and asked for a [meaningful way] for a shaman to become immortal.
        - Condition: `(e.other:Class() == "Shaman")`
        - Condition: `(e.message:findi("troubled") and qglobals["shaman_epic"] == "2")`
      - Player: "Meaningful Way" (link: explicit mention)
        - NPC say: For a shaman, a blessing of eternal life from any spirit is an honor, so a talisman was created by the Spirit of Patience to sustain Veshtaq for all time and he would be once again be rejoined with the spirit world. Now, Mwinda, it is up to you to retrieve the talisman. You may not simply ask for it. You will have to complete the ery tial he commands and defeat his essence. Do not fret. The Tribunal will sustain him in that plane so he may continue his work.
        - Condition: `(e.other:Class() == "Shaman")`
        - Condition: `(e.message:findi("meaningful way") and qglobals["shaman_epic"] == "2")`
      - Player: "Stolen" (link: external event mention)
        - Prompted by `event_trade`:
          - NPC say: This is a start. There is still much to do. While we have gotten the talismans from our allies, there are those that are not our friends -- the wasichu and worse -- who carry or have [stolen] items we need. They will not part with them willingly. This is where your strength and might will be put to the test . . . and your presence of mind. Are you certain you wish to go on?
          - Event guard: `(qglobals["shaman_epic"] == "2" and item_lib.check_turn_in(e.trade, {item1 = 57083, item2 = 57084}))`
        - NPC say: Very well. You will need to return to Wunshi for more information. He will be able to lead you to some of what we need if you ask him. Return to me and tell me when your business with Wunshi is finished. I am too tired to continue.
        - Condition: `(e.other:Class() == "Shaman")`
        - Condition: `(e.message:findi("stolen") and qglobals["shaman_epic"] == "3")`
      - Player: "business with Wunshi is finished" (link: explicit mention)
        - NPC say: Is that so? I am both grateful and anxious. My sight into the spirit world grows darker with each hour. You have done well, but I am ever fearful that we are not moving quickly enough. You must use all of your skills for your next task. Return to Kimm McShannel and when you return to me, tell me that you have created the potion. Show her this bangle.
        - Condition: `(e.other:Class() == "Shaman")`
        - Condition: `(e.message:findi("business with Wunshi is finished") and qglobals["shaman_epic"] == "4")`
        - Gives Gemmed Bangle of Enlightenment (57088).
      - Player: "Take Part" (link: external event mention)
        - Prompted by `event_trade`:
          - NPC say: I will have to pass these along as soon as my messenger gets here. I'm sure you understand that as each spirit loses strength, each of our abilities to keep a form in this tangible world becomes very difficult. We must find a way to sustain a physical presence here or the Ruchu will be in jeopardy. We will ask you to [take part] in the ceremony where our strength may fail us.
          - Event guard: `(qglobals["shaman_epic"] == "5" and item_lib.check_turn_in(e.trade, {item1 = 57614}))`
        - NPC say: We are still a long way from that, but I feel it is time to [acknowledge] you as a true shaman spirit that has earned the respect of many spirits of the world.
        - Condition: `(e.other:Class() == "Shaman")`
        - Condition: `(e.message:findi("take part") and qglobals["shaman_epic"] == "6")`
      - Player: "Acknowledge" (link: explicit mention)
        - NPC say: We, the spirits, have chosen to grant you a gift for all that you've done for us and what you still have left to do. It is just a sampling of the power you may obtain one day as you move forward as one of the heyokah. Guard it and use it well. Should you choose to continue your journey, tell me that you are [prepared to carry on] and save the spirits.
        - NPC message: You have gained 5 ability points!
        - Condition: `(e.other:Class() == "Shaman")`
        - Condition: `(e.message:findi("acknowledge") and qglobals["shaman_epic"] == "6")`
        - Gives Crafted Talisman of Fates (57400).
        - Sets `shaman_epic` to `7`.
      - Player: "Prepared To Carry On" (link: explicit mention)
        - NPC say: I knew we could count on you, . The time for Ruchu is drawing ever nearer, but we still must gather some essential elements. Soon, you will have to cross the barrier into that realm of Discord. Lupot Nukla can help you.
        - Condition: `(e.other:Class() == "Shaman")`
        - Condition: `(e.message:findi("prepared to carry on") and e.other:HasItem(57400))`
        - Sets `shaman_epic` to `8`.
      - Player: "Discord" (link: explicit mention)
        - NPC say: We know the Spirit of Might is beginning to disperse not just in Norrath, but that place shadowed by Discord as well. The spirit has passed through many beasts and is corrupting them, each one commanded by a trace of the spirit. You must find several beasts and find those traces of the wasichu. One is an airy, fluid creature. Yet another is a fierce beast that has grown beyond all normal proportions because of the spirit of Might. You must find them. And there are still others you must [seek].
        - Condition: `(e.other:Class() == "Shaman")`
        - Condition: `(e.message:findi("discord") and qglobals["shaman_epic"] == "11")`
      - Player: "Seek" (link: explicit mention)
        - NPC say: The other creature you must find is a soldier of evil. Another is an scurrying creature that is not bound to our realm. You have much ahead of you. Take this pouch and carefully piece together everything you find and return it to me. You will know how to do it. The spirits will guide you.
        - Condition: `(e.other:Class() == "Shaman")`
        - Condition: `(e.message:findi("seek") and qglobals["shaman_epic"] == "11")`
        - Gives Pouch of Spirit Dust (57710).
      - Player: "Spiritcaller"
        - NPC say: The fiend that is consuming our spirits is in Discord and is siphoning what little energy and strength we have remaining. We are losing ourselves in the passage of Discord. Without the spirits of Might, Patience, and Wisdom, we may not [survive]. We are not whole without them.
        - Condition: `(e.other:Class() == "Shaman")`
        - Condition: `(e.message:findi("spiritcaller") and qglobals["shaman_epic"] == "12")`
      - Player: "Survive" (link: explicit mention)
        - NPC say: Make your way to a place of great suffering and death in Kuua. You will need to investigate to help us learn more about our waning spirits. We have no influence there and it is a wholly unpredictable place.
        - Condition: `(e.other:Class() == "Shaman")`
        - Condition: `(e.message:findi("survive") and qglobals["shaman_epic"] == "12")`
      - Player: "Prepared For The Ceremony" (link: external event mention)
        - Prompted by `event_trade`:
          - NPC say: lowers its head and you believe you see a shade of a tear drop from its eyes and disappear into nothingness. 'You have done it. You cannot imagine our gratitude. The time for Ruchu is at hand and we offer you the privilege of taking part. If you are able to do the ceremony now, tell me you are [prepared for the ceremony].'
          - Event guard: `(qglobals["shaman_epic"] == "13" and item_lib.check_turn_in(e.trade, {item1 = 47100}))`
        - NPC say: Follow me closely. We must gather the spirits and try to call our ethereal kin of Might, Patience, and Wisdom. The other spirits will join us for Ruchu, namely the Spirit of Perseverance, Spirit of Understanding, Spirit of Fortitude, Spirit of Will, and the Spirit of Sense.
        - Condition: `(e.other:Class() == "Shaman")`
        - Condition: `(e.message:findi("prepared for the ceremony") and qglobals["shaman_epic"] == "14" and char_id == 0)`
      - Player: "Faithful Heyokah" (link: conversation sequence)
        - NPC say: Well, then, the time has come. Give me your Crafted Talisman of Fates, heyokah. Should you not have it now, give it to me when you do. If you have lost it, tell me so. I may be able to help you.
        - Condition: `(e.other:Class() == "Shaman")`
        - Condition: `(e.message:findi("faithful heyokah") and qglobals["shaman_epic"] == "14")`

8. freeportwest/"Elder Spirit Of Enlightenment", say "Prepared To Carry On". Sets `shaman_epic` to `8`.
    - Requires `shaman_epic` unset.

9. fungusgrove/"Lupot Nukla", say "Taken By Force". Sets `shaman_epic` to `9`.
    - Requires `shaman_epic` ==8.
    - Dialogue with fungusgrove/"Lupot Nukla":
      - Player: "Elder Spirit Sent Me"
        - NPC say: Shhh! You'll scare them away, fool! Darnit! Do you have any idea at all how rare this fungus is? Any idea at all?
        - Condition: `(e.message:findi("elder spirit sent me") and qglobals["shaman_epic"] == "1")`
      - Player: "Idea" (link: explicit mention)
        - NPC say: No kidding. The way you ran up here like a herd of elephants was a dead giveaway. You make enough noise and this fungus disappears into thin air and then I have to wait for it to show itself again. Odd plant really, but very reactive, so keep it down. The spirit must have two pieces of this fungus for its potion and it only grows here. I'd like to see you prove your ability. If by a miracle you should collect two, come and speak to me.
        - Condition: `(e.message:findi("idea") and qglobals["shaman_epic"] == "1")`
      - Player: "Hail" (link: conversation sequence)
        - NPC say: Surprising. Didn't think you'd be up to the task and be able to muster the knowledge to figure it out. If you have both with you, hurry along. The spirit is in great need of the potion.
        - Condition: `(e.message:findi("hail") and qglobals["shaman_epic"] == "1" and e.other:HasItem(57620))`
      - Player: "Hail" (link: conversation sequence)
        - NPC say: Welcome back. I received word that you were ready to continue the journey. Word travels fast when we have brave spirits like you on our side. As we proceed, our tasks become more difficult. We feel you are ready to take on the charge of aiding the spirits we've lost. We must recover some items that were [taken by force].
        - Condition: `(e.message:findi("hail") and qglobals["shaman_epic"] == "8")`
      - Player: "Taken By Force" (link: explicit mention)
        - NPC say: Over in Taelosia, the peaceful folk there found themselves overcome by the Muramites. They had stolen much of what had meaning to them. If you can track down Undari Perunea she can tell you how to find a sacred necklace of perseverance that was created by her own people, though Norrath's spirits did charm it. You will find Undari near the temples, hiding, and waiting for you. Return the talisman to me.
        - Condition: `(e.message:findi("taken by force") and qglobals["shaman_epic"] == "8")`
        - Sets `shaman_epic` to `9`.
      - Player: "Protected"
        - NPC say: When Undari was a young, peaceful Taelosian, she chose to defy the trusik -- the religious fanatics -- who called for the hurt and torture of her people. You see, once, all Taelosians lived in Nihilia, but something changed. One sly and corrupt Taelosian found a path to power and preached about a false god. He convinced many to follow him and they became the [trusik] who worshipped Trushar, an ocean god. They would torture those who didn't believe as they did.
        - Condition: `(e.message:findi("protected") and qglobals["shaman_epic"] == "10")`
      - Player: "Trusik" (link: explicit mention)
        - NPC say: The trusik were eventually forced into exile in the temples of the highest mountains. The Taelosians who resisted the beliefs and rhetoric of the trusik became known as the nihil -- and Undari was one of them. She believed in nature, the ebb and flow of a greater consciousness, and that if she kept her hopes high, she would overcome the horror of the zealots. And she [prevailed].
        - Condition: `(e.message:findi("trusik") and qglobals["shaman_epic"] == "10")`
      - Player: "Prevailed" (link: explicit mention)
        - NPC say: Undari's unwavering regard and respect for nature gained the attention of the spirit world, particularly that of the Spirit of Perseverance. The spirit would watch over her and time after time would [see] her bring more of her kind into spiritual awareness.
        - Condition: `(e.message:findi("prevailed") and qglobals["shaman_epic"] == "10")`
      - Player: "See" (link: explicit mention)
        - NPC say: The spirit saw that Undari always wore a beautiful necklace made of polished stone that her mother gave her. Her mother was taken by the trusik long ago because she refused to accept Trushar into her heart. She was taken down to the shores of Natimbi and shackled, sentenced to hang over the sea until she died. It was then that the spirit chose to bestow a [great gift] on Undari, as thanks and reward for her steadfast faith in the spirit world.
        - Condition: `(e.message:findi("see") and qglobals["shaman_epic"] == "10")`
      - Player: "Great Gift" (link: explicit mention)
        - NPC say: 'The spirit appeared before Undari, who was overcome with humility. The spirit cast a mighty spell and it rained upon Undari and was imbued into her necklace. The necklace would henceforth protect the young Undari from those who held dark beliefs and would try to corrupt her mind. Now you see why we had need of this necklace. But we are not done yet. We still need to make a [talisman].
        - Condition: `(e.message:findi("great gift") and qglobals["shaman_epic"] == "10")`
      - Player: "Talisman" (link: explicit mention)
        - NPC say: Yes, we need to complete a talisman to perform the Ruchu and it is up to us to finish this part of the task. We need a particular type of wood and it is rather unusual. You shall only find this material in an ethereal plane where the woods are imbued with spirits. I am counting on you to hunt down a sample of this wood and show it to me when you've acquired it.
        - Condition: `(e.message:findi("talisman") and qglobals["shaman_epic"] == "10")`

10. fungusgrove/"Lupot Nukla", hand "Necklace of Perseverance" (57401). Sets `shaman_epic` to `10`.
    - Requires `shaman_epic` ==9.
    - Hand in x1: "Necklace of Perseverance" (57401).
    - Say "Hail" to kodtaz/"Undari Perunea".
    - Spawns "Ikaav Spiritstealer" (293233).
    - Loot "Necklace of Perseverance" (57401) from "Ikaav Spiritstealer".

11. freeportwest/"Elder Spirit Of Enlightenment", hand "Impervious Medicine Bag" (57551). Sets `shaman_epic` to `11`.
    - Requires `shaman_epic` ==10.
    - Hand in x1: "Impervious Medicine Bag" (57551).
    - Prerequisite: "Impervious Medicine Bag" (57551). See section 0.

12. freeportwest/"Elder Spirit Of Enlightenment", hand "Glowing Spirit Charm of Might" (57987). Sets `shaman_epic` to `12`.
    - Requires `shaman_epic` ==11.
    - Hand in x1: "Glowing Spirit Charm of Might" (57987).
    - Prerequisite: "Glowing Spirit Charm of Might" (57987). See section 0.

13. freeportwest/"Elder Spirit Of Enlightenment", hand "Spiritcaller Beads" (57404). Sets `shaman_epic` to `13`.
    - Requires `shaman_epic` ==12.
    - Hand in x1: "Spiritcaller Beads" (57404).
    - Say "Fooled" to wallofslaughter/"Hudar Trittan".
    - Spawns "Discordling Spiritcaller" (300091).
    - Loot "Spiritcaller Beads" (57404) from "Discordling Spiritcaller".

14. freeportwest/"Elder Spirit Of Enlightenment", hand "Globe of Discordant Energy" (47100). Sets `shaman_epic` to `14`.
    - Requires `shaman_epic` ==13.
    - Hand in x1: "Globe of Discordant Energy" (47100).
    - Say "Check Lorb" to anguish/"Zone Status".
    - Spawns "Orb of Discordant Energy" (317087).
    - Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy".
    - Alternative: Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy" (NPC 317087) in `anguish`; trigger: anguish/"Zone Status", say "Check Uorb".
    - Alternative: Loot "Globe of Discordant Energy" (47100) from "Ornate Chest" (NPC 317112) in `anguish`; trigger: anguish/"Zone Status", say "Check Amv Chest".
    - Alternative: Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy" (NPC 317087) in `anguish`; trigger: anguish/"Zone Status", say "Signal:999999".
    - Alternative: Loot "Globe of Discordant Energy" (47100) from "Overlords Chest" (NPC 317124) in `anguish`; trigger: anguish/"Zone Status", say "Signal:999999".

15. freeportwest/"Elder Spirit Of Enlightenment", hand "Crafted Talisman of Fates" (57400). Sets `shaman_epic` to `15`.
    - Requires `shaman_epic` ==14.
    - Hand in x1: "Crafted Talisman of Fates" (57400).
    - Prerequisite: "Crafted Talisman of Fates" (57400). See section 0.
    - Gives "Blessed Spiritstaff of the Heyokah" (57405).

#### Steps on `shaman_epic` that do not change it

- `causeway` kupiop iku, say ready needs `shaman_epic` ==11.
  - Spawns epic version of Murkglider School Leader (303116).
  - Loots Slight Trace of a Spirit (57800).
- `cobaltscar` yoppa greenthumb, say elder spirit sent me needs `shaman_epic` ==1.
  - Spawns Gnashing Killer Shark (117091).
  - Spawns Darting Shark (117089).
  - Spawns Feeder Shark (117090).
  - Loots Brittle Burned Bark (57086).
- `dranik` player, on loot needs `shaman_epic` ==11.
  - Sets `shaman_chest_dranik` to `1`.
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
- `freeportwest` elder spirit of enlightenment, say business with wunshi is finished needs `shaman_epic` ==4.
  - Gives Gemmed Bangle of Enlightenment (57088).
- `freeportwest` elder spirit of enlightenment, say prepared for the ceremony needs `shaman_epic` ==14.
  - Spawns Elder Spirit of Perseverance (8119).
  - Spawns Elder Spirit of Understanding (8120).
  - Spawns Elder Spirit of Fortitude (8121).
  - Spawns Elder Spirit of Will (8122).
  - Spawns Elder Spirit of Sense (8123).
- `freeportwest` elder spirit of enlightenment, say rare gift needs `shaman_epic` ==2.
  - Gives Potion of Sustenance (57081).
- `freeportwest` elder spirit of enlightenment, say seek needs `shaman_epic` ==11.
  - Gives Pouch of Spirit Dust (57710).
- `freportn` elder spirit of enlightenment, say business with wunshi is finished needs `shaman_epic` ==4.
  - Gives Gemmed Bangle of Enlightenment (57088).
- `freportn` elder spirit of enlightenment, say prepared for the ceremony needs `shaman_epic` ==14.
  - Spawns Elder Spirit of Perseverance (8119).
  - Spawns Elder Spirit of Understanding (8120).
  - Spawns Elder Spirit of Fortitude (8121).
  - Spawns Elder Spirit of Will (8122).
  - Spawns Elder Spirit of Sense (8123).
- `freportn` elder spirit of enlightenment, say rare gift needs `shaman_epic` ==2.
  - Gives Potion of Sustenance (57081).
- `freportn` elder spirit of enlightenment, say seek needs `shaman_epic` ==11.
  - Gives Pouch of Spirit Dust (57710).
- `fungusgrove` lupot nukla, hand 57403 needs `shaman_epic` ==10.
  - Turn in Piece of Moaning Timber (57403).
  - Gives Impervious Medicine Bag (57551).
- `kodtaz` undari perunea, say hail needs `shaman_epic` ==9.
  - Spawns Ikaav Spiritstealer (293233).
  - Loots Lucidem (35084).
  - Loots Versluierd Fungus (35087).
  - Loots Uncut Jacinth (37850).
  - Loots Necklace of Perseverance (57401).
- `lakerathe` kimm mcshannel, say break down needs `shaman_epic` ==3.
  - Gives Heyokah Medicine Bag (52922).
- `lakerathe` kimm mcshannel, say break down needs `shaman_epic` ==5.
  - Gives Heyokah Medicine Bag (52922).
- `lakerathe` kimm mcshannel, say up to it needs `shaman_epic` ==1.
  - Spawns Ancient Megalodon (51160).
  - Loots Lustrous Seaweed (52926).
- `lakerathe` player, on loot needs `shaman_epic` >=1.
  - Sets `shaman_epic_lakerathechest` to `1`.
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
- `postorms` 210252, on enter needs `shaman_epic` ==10.
  - Spawns Darkened Chanting Woodspirit (210250).
  - Loots Versluierd Fungus (35087).
  - Loots Piece of Moaning Timber (57403).
  - Loots Staurolite (97002).
- `provinggrounds` stilled lightning warrior, on enter needs `shaman_epic` ==11.
  - Spawns Lightning Warrior Spiritseeker (316073).
  - Loots Lucidem (35084).
  - Loots Versluierd Fungus (35087).
  - Loots Glowing Trace of Might (57250).
- `shadeweaver` wunshi kashra, say stolen needs `shaman_epic` ==3.
  - Sets `shaman_epic_nadox` to `1`.
- `umbral` player, on loot needs `shaman_epic` set.
  - Sets `shaman_epic_umbralchest` to `1`.
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
- `wallofslaughter` hudar trittan, say fooled needs `shaman_epic` ==12.
  - Spawns Discordling Spiritcaller (300091).
  - Loots Platinum Etched Gear #2 (37047).
  - Loots Platinum Etched Gear #3 (37048).
  - Loots Spiritcaller Beads (57404).
  - Loots Polished Blue Softstone (80030).
  - Loots Old Eternal Grove Leather Wrist Ornament (84538).
  - Loots Old Eternal Grove Cloth Wrist Ornament (84545).
- `wallofslaughter` player, on loot needs `shaman_epic` ==12.
  - Sets `shaman_epic_wos` to `1`.
  - Spawns a chest (Epic 1.5) (893).
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
- `warrens` wilslik gissu, hand 57369+57550 needs `shaman_epic` ==1.
  - Turn in Shadowed Pulp (57550).
  - Turn in Brittle Twigs (57369).
  - Gives Distilled Potion of Endurance (52921).

### Other flags touched along the way

- `shaman_epic_lakerathechest` set to 1 at lakerathe/player.
- `shaman_epic_nadox` set to 1 at shadeweaver/wunshi kashra.
- `shaman_epic_nadoxrespawn` set to 1 at nadox/player.
- `shaman_epic_umbralchest` set to 1 at umbral/player.
- `shaman_epic_wos` set to 1 at wallofslaughter/player.
