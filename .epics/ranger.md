# Ranger

Steps taken from the quest graph only. **Broken** means the graph has no edge for that value or that item.

Flags with writes: `ranger_epic`, `ranger_epic15_pre`.

## 0. Prerequisites

Each list is the order you obtain that item. Later steps point here instead of repeating the chain.

### "Earthcaller" (20488)

1. Hand "Shiny Tin Bowl" (17860) to hole/"Jaeil The Wretched". Spawns "Jaeil the Insane" (39154). Loot "Soulbound Hammer" (20478) from "Jaeil the Insane".
2. Loot "Soulbound Hammer" (20478) from "Jaeil the Insane".
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
17. Encounter starts when NPC 186196 spawns in `hateplaneb`.
18. Starts timer `popmaestro`.
19. Spawns "Maestro of Rancor" (186111) after `hateplaneb/maestro#timer:popmaestro`.
20. Loot "Shattered Emerald of Corruption" (20484) from "Maestro of Rancor".
21. northkarana/"Xanuusus", hand "Refined Mithril Blade" (20483) + "Shattered Emerald of Corruption" (20484). Gives "Earthcaller" (20488).

### "Essence of Earth and Wind" (62600)

1. Say "Ready" to northkarana/"Xanuusus".
2. Spawns "A Tainted Beast" (13131).
3. Loot "Stone of Winde" (62604) from "A Tainted Beast".
4. northkarana/"Xanuusus", hand "Stone of Winde" (62604). Sets `ranger_epic15_pre` to `9`.
5. steamfont/"Godbin Strumharp", hand platinum:30. Requires `ranger_epic15_pre` ==9. Gives "Sound Capture Jar" (62637).
6. steamfontmts/"Godbin Strumharp", hand platinum:30. Requires `ranger_epic15_pre` ==9. Gives "Sound Capture Jar" (62637).
7. charasis/"Ghost Of Mera", hand "Sound Capture Jar" (62637). Sets `ranger_epic15_pre` to `10`.
8. Spawns "Ghost of Mera" (105290) in `charasis` on event_enterzone.
9. Hand "Sound Capture Jar" (62637) to charasis/"Ghost Of Mera". Sets `ranger_epic15_pre` to `10`.
10. Loot "Echoing Jar" (62638) from "Ghost of Mera".
11. erudnint/"Mairee Silentone", hand "Stone of Winde" (62604) + "Echoing Jar" (62638). Requires `ranger_epic15_pre` ==10. Gives "Essence of Earth and Wind" (62600).

### "Corun's Notes" (62617)

1. Forage "Sickly Maiden's Hair" (62810) in `rathemtn`.
2. eastkarana/"Althele", hand "Sickly Maiden's Hair" (62810). Gives "Tuft of Sickly Maiden's Hair" (62811).
3. qrg/"Corun Finisc", hand "Tuft of Sickly Maiden's Hair" (62811). Gives "Borrowed Medicine Bag" (62605).
4. qrg/"Corun Finisc", hand "Closed Medicine Bag" (62615). Gives "Sickly Mosquito Blood Sample" (62611).
5. Summon "Collapsible Fletching Kit" (17189) by casting "Unfold Fletching Kit".
6. qrg/"Corun Finisc", hand "Tuft of Sickly Maiden's Hair" (62811). Gives "Magical Sample Vial" (62657).
7. **Broken:** nothing in the graph gives, loots, spawns, or combines Captured Mosquito (62642).
8. Combine in "Collapsible Fletching Kit" (17189): "Magical Sample Vial" (62657), "Captured Mosquito" (62642). Produces "Sickly Mosquito Blood Sample" (62611). Requires Fletching. The combine does not fail.
9. qrg/"Corun Finisc", hand "Closed Medicine Bag" (62615). Gives "Twitching Swordfish Blood Sample" (62612).
10. **Broken:** nothing in the graph gives, loots, spawns, or combines Captured Swordfish (62643).
11. Combine in "Collapsible Fletching Kit" (17189): "Magical Sample Vial" (62657), "Captured Swordfish" (62643). Produces "Twitching Swordfish Blood Sample" (62612). Requires Fletching. The combine does not fail.
12. qrg/"Corun Finisc", hand "Closed Medicine Bag" (62615). Gives "Bloated Drogan Spider Blood Sample" (62613).
13. **Broken:** nothing in the graph gives, loots, spawns, or combines Captured Spider (62644).
14. Combine in "Collapsible Fletching Kit" (17189): "Magical Sample Vial" (62657), "Captured Spider" (62644). Produces "Bloated Drogan Spider Blood Sample" (62613). Requires Fletching. The combine does not fail.
15. qrg/"Corun Finisc", hand "Closed Medicine Bag" (62615). Gives "Leprous Chokidai Blood Sample" (62614).
16. **Broken:** nothing in the graph gives, loots, spawns, or combines Captured Chokidai (62645).
17. Combine in "Collapsible Fletching Kit" (17189): "Magical Sample Vial" (62657), "Captured Chokidai" (62645). Produces "Leprous Chokidai Blood Sample" (62614). Requires Fletching. The combine does not fail.
18. Combine in "Borrowed Medicine Bag" (62605): "Sickly Mosquito Blood Sample" (62611), "Twitching Swordfish Blood Sample" (62612), "Bloated Drogan Spider Blood Sample" (62613), "Leprous Chokidai Blood Sample" (62614). Produces "Closed Medicine Bag" (62615). The combine does not fail.
19. qrg/"Corun Finisc", hand "Closed Medicine Bag" (62615). Gives "Borrowed Medicine Bag" (62605).
20. Spawns "An Asteatotic Highborn" (109907) in `veksar` on enter.
21. Loot "Asteatotic Veksar Blood" (35100) from "An Asteatotic Highborn".
22. Spawns "A Neuralgic Huntress" (120136) in `westwastes` on enter.
23. Loot "Neuralgic Wyvern Blood" (72605) from "A Neuralgic Huntress".
24. Combine in "Borrowed Medicine Bag" (62605): "Asteatotic Veksar Blood" (35100), "Neuralgic Wyvern Blood" (72605), "Sickly Mosquito Blood Sample" (62611), "Twitching Swordfish Blood Sample" (62612), "Leprous Chokidai Blood Sample" (62614), "Bloated Drogan Spider Blood Sample" (62613). Produces "Full Medicine Bag" (62616). The combine does not fail.
25. qrg/"Corun Finisc", hand "Full Medicine Bag" (62616). Gives "Corun's Notes" (62617).

### "Senvial's Blessing" (62621)

1. Forage "Sickly Maiden's Hair" (62810) in `rathemtn`.
2. eastkarana/"Althele", hand "Sickly Maiden's Hair" (62810). Gives "Tuft of Sickly Maiden's Hair" (62811).
3. qrg/"Niera Farbreeze", hand "Tuft of Sickly Maiden's Hair" (62811). Gives "Waterproof Collection Bag" (62812).
4. Say "King Timer" to frontiermtns/"Druid 1 5".
5. Spawns npc 92202 (92202).
6. Loot "Bag of Diseased Maiden's Hair" (62826) from npc 92202.
7. Spawns "A Bloodgill Forager" (85234) in `lakeofillomen` on enter.
8. Loot "Handful of Diseased Maiden's Hair" (62825) from "A Bloodgill Forager".
9. Common item: Tackle Box (17048). Listed in 11 zones.
10. Spawns "Ulthork Raider" (116608) in `eastwastes` on enter.
11. Loot "Carved Prexus Totem" (62821) from "Ulthork Raider".
12. cobaltscar/"Blumblum Swigwater", hand "Carved Prexus Totem" (62821). Gives "Small Trigger Fish" (62820).
13. Common item: Gutting Knife (62823). Listed in 4 zones.
14. Combine in "Tackle Box" (17048): "Small Trigger Fish" (62820), "Gutting Knife" (62823). Hands back "Gutting Knife" (62823). Produces "Soggy Maiden's Hair" (62824). Requires Fishing, trivial 20. The combine does not fail.
15. Spawns "spawn #Swamp Terror" (47208) in `feerrott` on enter.
16. Loot "Partially Digested Maiden's Hair" (62819) from "spawn #Swamp Terror".
17. Loot "Partially Digested Maiden's Hair" (62819) from "Swamp Terror".
18. Combine in "Waterproof Collection Bag" (62812): "Bag of Diseased Maiden's Hair" (62826), "Handful of Diseased Maiden's Hair" (62825), "Soggy Maiden's Hair" (62824), "Partially Digested Maiden's Hair" (62819). Produces "Sealed Collection Bag" (62813). The combine does not fail.
19. qrg/"Niera Farbreeze", hand "Sealed Collection Bag" (62813). Gives "Wash Cloth" (62847).
20. Spawns "spawn #Swamp Terror" (47208) in `feerrott` on enter.
21. Loot "Mangled Head" (62818) from "spawn #Swamp Terror".
22. Loot "Mangled Head" (62818) from "Swamp Terror".
23. Combine in "Wash Cloth" (62847): "Mangled Head" (62818). Produces "Wrapped Mangled Head" (62848). The combine does not fail.
24. qrg/"Niera Farbreeze", hand "Wrapped Mangled Head" (62848). Gives "Mangled Head" (62827).
25. qrg/"Niera Farbreeze", hand "Wrapped Mangled Head" (62848). Sets `druid_epic` to `2`.
26. poknowledge/"Pathfinder Arelat", say "Worth It". Requires `druid_epic` ==2. Gives "Fresh Awakenings vol. 1" (62839).
27. poknowledge/"Pathfinder Arelat", say "Worth It". Requires `druid_epic` ==2. Gives "Fresh Awakenings vol. 2" (62840).
28. poknowledge/"Pathfinder Arelat", say "Worth It". Requires `druid_epic` ==2. Gives "Fresh Awakenings vol. 3" (62841).
29. poknowledge/"Gravelady Beddia", hand "Fresh Awakenings vol. 1" (62839) + "Fresh Awakenings vol. 2" (62840) + "Fresh Awakenings vol. 3" (62841). Gives "Healing Plants" (62842).
30. qrg/"Niera Farbreeze", hand "Healing Plants" (62842). Sets `druid_epic` to `3`.
31. feerrott/"Corrupted Spirit", say "Show It". Requires `druid_epic` ==3. Gives "Disease Rune" (62837).
32. **Broken:** nothing in the graph gives, loots, spawns, or combines Animating Heads (62828).
33. Combine in "Mangled Head" (62827): "Disease Rune" (62837), "Animating Heads" (62828). Produces "Runed Skull" (62838). The combine does not fail.
34. qrg/"Niera Farbreeze", hand "Healing Plants" (62842). Gives "Niera's Healing Notes" (62849).
35. qrg/"Niera Farbreeze", hand "Runed Skull" (62838) + "Niera's Healing Notes" (62849). Sets `druid_epic` to `4`.
36. qrg/"Niera Farbreeze", hand "Runed Skull" (62838) + "Niera's Healing Notes" (62849). Gives "Niera's Research Notes" (62843).
37. pojustice/"Great Bear", hand "Niera's Research Notes" (62843). Requires `druid_epic` ==4. Gives "Red Dogwood Seed" (62844).
38. Spawns "An Ancient Thought Horror" (164122) in `thedeep` on enter.
39. Loot "Thick Spinal Fluid" (40420) from "An Ancient Thought Horror".
40. qrg/"Corun Finisc", hand "Tuft of Sickly Maiden's Hair" (62811). Gives "Borrowed Medicine Bag" (62605).
41. qrg/"Corun Finisc", hand "Closed Medicine Bag" (62615). Gives "Sickly Mosquito Blood Sample" (62611).
42. Summon "Collapsible Fletching Kit" (17189) by casting "Unfold Fletching Kit".
43. qrg/"Corun Finisc", hand "Tuft of Sickly Maiden's Hair" (62811). Gives "Magical Sample Vial" (62657).
44. **Broken:** nothing in the graph gives, loots, spawns, or combines Captured Mosquito (62642).
45. Combine in "Collapsible Fletching Kit" (17189): "Magical Sample Vial" (62657), "Captured Mosquito" (62642). Produces "Sickly Mosquito Blood Sample" (62611). Requires Fletching. The combine does not fail.
46. qrg/"Corun Finisc", hand "Closed Medicine Bag" (62615). Gives "Twitching Swordfish Blood Sample" (62612).
47. **Broken:** nothing in the graph gives, loots, spawns, or combines Captured Swordfish (62643).
48. Combine in "Collapsible Fletching Kit" (17189): "Magical Sample Vial" (62657), "Captured Swordfish" (62643). Produces "Twitching Swordfish Blood Sample" (62612). Requires Fletching. The combine does not fail.
49. qrg/"Corun Finisc", hand "Closed Medicine Bag" (62615). Gives "Bloated Drogan Spider Blood Sample" (62613).
50. **Broken:** nothing in the graph gives, loots, spawns, or combines Captured Spider (62644).
51. Combine in "Collapsible Fletching Kit" (17189): "Magical Sample Vial" (62657), "Captured Spider" (62644). Produces "Bloated Drogan Spider Blood Sample" (62613). Requires Fletching. The combine does not fail.
52. qrg/"Corun Finisc", hand "Closed Medicine Bag" (62615). Gives "Leprous Chokidai Blood Sample" (62614).
53. **Broken:** nothing in the graph gives, loots, spawns, or combines Captured Chokidai (62645).
54. Combine in "Collapsible Fletching Kit" (17189): "Magical Sample Vial" (62657), "Captured Chokidai" (62645). Produces "Leprous Chokidai Blood Sample" (62614). Requires Fletching. The combine does not fail.
55. Combine in "Borrowed Medicine Bag" (62605): "Sickly Mosquito Blood Sample" (62611), "Twitching Swordfish Blood Sample" (62612), "Bloated Drogan Spider Blood Sample" (62613), "Leprous Chokidai Blood Sample" (62614). Produces "Closed Medicine Bag" (62615). The combine does not fail.
56. qrg/"Corun Finisc", hand "Closed Medicine Bag" (62615). Gives "Borrowed Medicine Bag" (62605).
57. Spawns "An Asteatotic Highborn" (109907) in `veksar` on enter.
58. Loot "Asteatotic Veksar Blood" (35100) from "An Asteatotic Highborn".
59. Spawns "A Neuralgic Huntress" (120136) in `westwastes` on enter.
60. Loot "Neuralgic Wyvern Blood" (72605) from "A Neuralgic Huntress".
61. Combine in "Borrowed Medicine Bag" (62605): "Asteatotic Veksar Blood" (35100), "Neuralgic Wyvern Blood" (72605), "Sickly Mosquito Blood Sample" (62611), "Twitching Swordfish Blood Sample" (62612), "Leprous Chokidai Blood Sample" (62614), "Bloated Drogan Spider Blood Sample" (62613). Produces "Full Medicine Bag" (62616). The combine does not fail.
62. qrg/"Corun Finisc", hand "Full Medicine Bag" (62616). Gives "Corun's Notes" (62617).
63. freeportwest/"Shana Liskia", hand "Corun's Notes" (62617). Gives "Corun's Notes - annotated" (62654).
64. freportw/"Shana Liskia", hand "Corun's Notes" (62617). Gives "Corun's Notes - annotated" (62654).
65. freeportwest/"Shana Liskia", hand "Thick Spinal Fluid" (40420) + "Corun's Notes - annotated" (62654). Gives "Mind Crystal" (62846).
66. freportw/"Shana Liskia", hand "Thick Spinal Fluid" (40420) + "Corun's Notes - annotated" (62654). Gives "Mind Crystal" (62846).
67. pojustice/"Great Bear", hand "Niera's Research Notes" (62843). Requires `druid_epic` ==4. Gives "Living Brambles Seed" (62845).
68. qrg/"Niera Farbreeze", hand "Red Dogwood Seed" (62844) + "Living Brambles Seed" (62845). Requires `druid_epic` ==4. Gives "Mind Crystal" (62846).
69. eastkarana/"Tholris", say "You Are Diseased". Gives "Red Crystal" (62618).
70. eastkarana/"Tholris", say "You Are Diseased". Gives "Violet Crystal" (62619).
71. freeportwest/"Shana Liskia", hand "Red Crystal" (62618) + "Violet Crystal" (62619). Gives "Letter to Corun" (62655).
72. freportw/"Shana Liskia", hand "Red Crystal" (62618) + "Violet Crystal" (62619). Gives "Letter to Corun" (62655).
73. qrg/"Corun Finisc", hand "Letter to Corun" (62655) + "Mind Crystal" (62846). Gives "Red Dogwood Seed" (62844).
74. Requires `ranger_natimbi_chest` unset; no setter establishes this state.
75. natimbi/"Ranger 1 5", say "Hail". Requires `ranger_natimbi_chest` unset. Gives "Senvial's Blessing" (62621).

### "Grinbik's Blessing" (62622)

1. Forage "Sickly Maiden's Hair" (62810) in `rathemtn`.
2. eastkarana/"Althele", hand "Sickly Maiden's Hair" (62810). Gives "Tuft of Sickly Maiden's Hair" (62811).
3. qrg/"Niera Farbreeze", hand "Tuft of Sickly Maiden's Hair" (62811). Gives "Waterproof Collection Bag" (62812).
4. Say "King Timer" to frontiermtns/"Druid 1 5".
5. Spawns npc 92202 (92202).
6. Loot "Bag of Diseased Maiden's Hair" (62826) from npc 92202.
7. Spawns "A Bloodgill Forager" (85234) in `lakeofillomen` on enter.
8. Loot "Handful of Diseased Maiden's Hair" (62825) from "A Bloodgill Forager".
9. Common item: Tackle Box (17048). Listed in 11 zones.
10. Spawns "Ulthork Raider" (116608) in `eastwastes` on enter.
11. Loot "Carved Prexus Totem" (62821) from "Ulthork Raider".
12. cobaltscar/"Blumblum Swigwater", hand "Carved Prexus Totem" (62821). Gives "Small Trigger Fish" (62820).
13. Common item: Gutting Knife (62823). Listed in 4 zones.
14. Combine in "Tackle Box" (17048): "Small Trigger Fish" (62820), "Gutting Knife" (62823). Hands back "Gutting Knife" (62823). Produces "Soggy Maiden's Hair" (62824). Requires Fishing, trivial 20. The combine does not fail.
15. Spawns "spawn #Swamp Terror" (47208) in `feerrott` on enter.
16. Loot "Partially Digested Maiden's Hair" (62819) from "spawn #Swamp Terror".
17. Loot "Partially Digested Maiden's Hair" (62819) from "Swamp Terror".
18. Combine in "Waterproof Collection Bag" (62812): "Bag of Diseased Maiden's Hair" (62826), "Handful of Diseased Maiden's Hair" (62825), "Soggy Maiden's Hair" (62824), "Partially Digested Maiden's Hair" (62819). Produces "Sealed Collection Bag" (62813). The combine does not fail.
19. qrg/"Niera Farbreeze", hand "Sealed Collection Bag" (62813). Gives "Wash Cloth" (62847).
20. Spawns "spawn #Swamp Terror" (47208) in `feerrott` on enter.
21. Loot "Mangled Head" (62818) from "spawn #Swamp Terror".
22. Loot "Mangled Head" (62818) from "Swamp Terror".
23. Combine in "Wash Cloth" (62847): "Mangled Head" (62818). Produces "Wrapped Mangled Head" (62848). The combine does not fail.
24. qrg/"Niera Farbreeze", hand "Wrapped Mangled Head" (62848). Gives "Mangled Head" (62827).
25. qrg/"Niera Farbreeze", hand "Wrapped Mangled Head" (62848). Sets `druid_epic` to `2`.
26. poknowledge/"Pathfinder Arelat", say "Worth It". Requires `druid_epic` ==2. Gives "Fresh Awakenings vol. 1" (62839).
27. poknowledge/"Pathfinder Arelat", say "Worth It". Requires `druid_epic` ==2. Gives "Fresh Awakenings vol. 2" (62840).
28. poknowledge/"Pathfinder Arelat", say "Worth It". Requires `druid_epic` ==2. Gives "Fresh Awakenings vol. 3" (62841).
29. poknowledge/"Gravelady Beddia", hand "Fresh Awakenings vol. 1" (62839) + "Fresh Awakenings vol. 2" (62840) + "Fresh Awakenings vol. 3" (62841). Gives "Healing Plants" (62842).
30. qrg/"Niera Farbreeze", hand "Healing Plants" (62842). Sets `druid_epic` to `3`.
31. feerrott/"Corrupted Spirit", say "Show It". Requires `druid_epic` ==3. Gives "Disease Rune" (62837).
32. **Broken:** nothing in the graph gives, loots, spawns, or combines Animating Heads (62828).
33. Combine in "Mangled Head" (62827): "Disease Rune" (62837), "Animating Heads" (62828). Produces "Runed Skull" (62838). The combine does not fail.
34. qrg/"Niera Farbreeze", hand "Healing Plants" (62842). Gives "Niera's Healing Notes" (62849).
35. qrg/"Niera Farbreeze", hand "Runed Skull" (62838) + "Niera's Healing Notes" (62849). Sets `druid_epic` to `4`.
36. qrg/"Niera Farbreeze", hand "Runed Skull" (62838) + "Niera's Healing Notes" (62849). Gives "Niera's Research Notes" (62843).
37. pojustice/"Great Bear", hand "Niera's Research Notes" (62843). Requires `druid_epic` ==4. Gives "Red Dogwood Seed" (62844).
38. Spawns "An Ancient Thought Horror" (164122) in `thedeep` on enter.
39. Loot "Thick Spinal Fluid" (40420) from "An Ancient Thought Horror".
40. qrg/"Corun Finisc", hand "Tuft of Sickly Maiden's Hair" (62811). Gives "Borrowed Medicine Bag" (62605).
41. qrg/"Corun Finisc", hand "Closed Medicine Bag" (62615). Gives "Sickly Mosquito Blood Sample" (62611).
42. Summon "Collapsible Fletching Kit" (17189) by casting "Unfold Fletching Kit".
43. qrg/"Corun Finisc", hand "Tuft of Sickly Maiden's Hair" (62811). Gives "Magical Sample Vial" (62657).
44. **Broken:** nothing in the graph gives, loots, spawns, or combines Captured Mosquito (62642).
45. Combine in "Collapsible Fletching Kit" (17189): "Magical Sample Vial" (62657), "Captured Mosquito" (62642). Produces "Sickly Mosquito Blood Sample" (62611). Requires Fletching. The combine does not fail.
46. qrg/"Corun Finisc", hand "Closed Medicine Bag" (62615). Gives "Twitching Swordfish Blood Sample" (62612).
47. **Broken:** nothing in the graph gives, loots, spawns, or combines Captured Swordfish (62643).
48. Combine in "Collapsible Fletching Kit" (17189): "Magical Sample Vial" (62657), "Captured Swordfish" (62643). Produces "Twitching Swordfish Blood Sample" (62612). Requires Fletching. The combine does not fail.
49. qrg/"Corun Finisc", hand "Closed Medicine Bag" (62615). Gives "Bloated Drogan Spider Blood Sample" (62613).
50. **Broken:** nothing in the graph gives, loots, spawns, or combines Captured Spider (62644).
51. Combine in "Collapsible Fletching Kit" (17189): "Magical Sample Vial" (62657), "Captured Spider" (62644). Produces "Bloated Drogan Spider Blood Sample" (62613). Requires Fletching. The combine does not fail.
52. qrg/"Corun Finisc", hand "Closed Medicine Bag" (62615). Gives "Leprous Chokidai Blood Sample" (62614).
53. **Broken:** nothing in the graph gives, loots, spawns, or combines Captured Chokidai (62645).
54. Combine in "Collapsible Fletching Kit" (17189): "Magical Sample Vial" (62657), "Captured Chokidai" (62645). Produces "Leprous Chokidai Blood Sample" (62614). Requires Fletching. The combine does not fail.
55. Combine in "Borrowed Medicine Bag" (62605): "Sickly Mosquito Blood Sample" (62611), "Twitching Swordfish Blood Sample" (62612), "Bloated Drogan Spider Blood Sample" (62613), "Leprous Chokidai Blood Sample" (62614). Produces "Closed Medicine Bag" (62615). The combine does not fail.
56. qrg/"Corun Finisc", hand "Closed Medicine Bag" (62615). Gives "Borrowed Medicine Bag" (62605).
57. Spawns "An Asteatotic Highborn" (109907) in `veksar` on enter.
58. Loot "Asteatotic Veksar Blood" (35100) from "An Asteatotic Highborn".
59. Spawns "A Neuralgic Huntress" (120136) in `westwastes` on enter.
60. Loot "Neuralgic Wyvern Blood" (72605) from "A Neuralgic Huntress".
61. Combine in "Borrowed Medicine Bag" (62605): "Asteatotic Veksar Blood" (35100), "Neuralgic Wyvern Blood" (72605), "Sickly Mosquito Blood Sample" (62611), "Twitching Swordfish Blood Sample" (62612), "Leprous Chokidai Blood Sample" (62614), "Bloated Drogan Spider Blood Sample" (62613). Produces "Full Medicine Bag" (62616). The combine does not fail.
62. qrg/"Corun Finisc", hand "Full Medicine Bag" (62616). Gives "Corun's Notes" (62617).
63. freeportwest/"Shana Liskia", hand "Corun's Notes" (62617). Gives "Corun's Notes - annotated" (62654).
64. freportw/"Shana Liskia", hand "Corun's Notes" (62617). Gives "Corun's Notes - annotated" (62654).
65. freeportwest/"Shana Liskia", hand "Thick Spinal Fluid" (40420) + "Corun's Notes - annotated" (62654). Gives "Mind Crystal" (62846).
66. freportw/"Shana Liskia", hand "Thick Spinal Fluid" (40420) + "Corun's Notes - annotated" (62654). Gives "Mind Crystal" (62846).
67. pojustice/"Great Bear", hand "Niera's Research Notes" (62843). Requires `druid_epic` ==4. Gives "Living Brambles Seed" (62845).
68. qrg/"Niera Farbreeze", hand "Red Dogwood Seed" (62844) + "Living Brambles Seed" (62845). Requires `druid_epic` ==4. Gives "Mind Crystal" (62846).
69. eastkarana/"Tholris", say "You Are Diseased". Gives "Red Crystal" (62618).
70. eastkarana/"Tholris", say "You Are Diseased". Gives "Violet Crystal" (62619).
71. freeportwest/"Shana Liskia", hand "Red Crystal" (62618) + "Violet Crystal" (62619). Gives "Letter to Corun" (62655).
72. freportw/"Shana Liskia", hand "Red Crystal" (62618) + "Violet Crystal" (62619). Gives "Letter to Corun" (62655).
73. qrg/"Corun Finisc", hand "Letter to Corun" (62655) + "Mind Crystal" (62846). Gives "Red Dogwood Seed" (62844).
74. Requires `ranger_bloodfield_chest` unset; no setter establishes this state.
75. bloodfields/"Ranger 1 5", say "Hail". Requires `ranger_bloodfield_chest` unset. Gives "Grinbik's Blessing" (62622).

### "Red Dogwood Seed" (62844)

1. Forage "Sickly Maiden's Hair" (62810) in `rathemtn`.
2. eastkarana/"Althele", hand "Sickly Maiden's Hair" (62810). Gives "Tuft of Sickly Maiden's Hair" (62811).
3. qrg/"Niera Farbreeze", hand "Tuft of Sickly Maiden's Hair" (62811). Gives "Waterproof Collection Bag" (62812).
4. Say "King Timer" to frontiermtns/"Druid 1 5".
5. Spawns npc 92202 (92202).
6. Loot "Bag of Diseased Maiden's Hair" (62826) from npc 92202.
7. Spawns "A Bloodgill Forager" (85234) in `lakeofillomen` on enter.
8. Loot "Handful of Diseased Maiden's Hair" (62825) from "A Bloodgill Forager".
9. Common item: Tackle Box (17048). Listed in 11 zones.
10. Spawns "Ulthork Raider" (116608) in `eastwastes` on enter.
11. Loot "Carved Prexus Totem" (62821) from "Ulthork Raider".
12. cobaltscar/"Blumblum Swigwater", hand "Carved Prexus Totem" (62821). Gives "Small Trigger Fish" (62820).
13. Common item: Gutting Knife (62823). Listed in 4 zones.
14. Combine in "Tackle Box" (17048): "Small Trigger Fish" (62820), "Gutting Knife" (62823). Hands back "Gutting Knife" (62823). Produces "Soggy Maiden's Hair" (62824). Requires Fishing, trivial 20. The combine does not fail.
15. Spawns "spawn #Swamp Terror" (47208) in `feerrott` on enter.
16. Loot "Partially Digested Maiden's Hair" (62819) from "spawn #Swamp Terror".
17. Loot "Partially Digested Maiden's Hair" (62819) from "Swamp Terror".
18. Combine in "Waterproof Collection Bag" (62812): "Bag of Diseased Maiden's Hair" (62826), "Handful of Diseased Maiden's Hair" (62825), "Soggy Maiden's Hair" (62824), "Partially Digested Maiden's Hair" (62819). Produces "Sealed Collection Bag" (62813). The combine does not fail.
19. qrg/"Niera Farbreeze", hand "Sealed Collection Bag" (62813). Gives "Wash Cloth" (62847).
20. Spawns "spawn #Swamp Terror" (47208) in `feerrott` on enter.
21. Loot "Mangled Head" (62818) from "spawn #Swamp Terror".
22. Loot "Mangled Head" (62818) from "Swamp Terror".
23. Combine in "Wash Cloth" (62847): "Mangled Head" (62818). Produces "Wrapped Mangled Head" (62848). The combine does not fail.
24. qrg/"Niera Farbreeze", hand "Wrapped Mangled Head" (62848). Gives "Mangled Head" (62827).
25. qrg/"Niera Farbreeze", hand "Wrapped Mangled Head" (62848). Sets `druid_epic` to `2`.
26. poknowledge/"Pathfinder Arelat", say "Worth It". Requires `druid_epic` ==2. Gives "Fresh Awakenings vol. 1" (62839).
27. poknowledge/"Pathfinder Arelat", say "Worth It". Requires `druid_epic` ==2. Gives "Fresh Awakenings vol. 2" (62840).
28. poknowledge/"Pathfinder Arelat", say "Worth It". Requires `druid_epic` ==2. Gives "Fresh Awakenings vol. 3" (62841).
29. poknowledge/"Gravelady Beddia", hand "Fresh Awakenings vol. 1" (62839) + "Fresh Awakenings vol. 2" (62840) + "Fresh Awakenings vol. 3" (62841). Gives "Healing Plants" (62842).
30. qrg/"Niera Farbreeze", hand "Healing Plants" (62842). Sets `druid_epic` to `3`.
31. feerrott/"Corrupted Spirit", say "Show It". Requires `druid_epic` ==3. Gives "Disease Rune" (62837).
32. **Broken:** nothing in the graph gives, loots, spawns, or combines Animating Heads (62828).
33. Combine in "Mangled Head" (62827): "Disease Rune" (62837), "Animating Heads" (62828). Produces "Runed Skull" (62838). The combine does not fail.
34. qrg/"Niera Farbreeze", hand "Healing Plants" (62842). Gives "Niera's Healing Notes" (62849).
35. qrg/"Niera Farbreeze", hand "Runed Skull" (62838) + "Niera's Healing Notes" (62849). Sets `druid_epic` to `4`.
36. qrg/"Niera Farbreeze", hand "Runed Skull" (62838) + "Niera's Healing Notes" (62849). Gives "Niera's Research Notes" (62843).
37. pojustice/"Great Bear", hand "Niera's Research Notes" (62843). Requires `druid_epic` ==4. Gives "Red Dogwood Seed" (62844).

### "Wind-blessed Heartwood" (62626)

1. Requires `ranger_dranik_chest` unset; no setter establishes this state.
2. global/"Global Player", combine recipe 13412. Sets `ranger_epic` to `3`.
3. jaggedpine/"Red Dogwood Treant", say "Hail". Requires `ranger_epic` ==3. Gives "Red Dogwood Heartwood" (62623).
4. dranik/"Ranger 1 5", hand "Red Dogwood Heartwood" (62623). Requires `ranger_dranik_chest` unset. Gives "Wind-blessed Heartwood" (62626).

### "Block of Purest Silver" (62625)

1. global/"Global Player", combine recipe 13412. Sets `ranger_epic` to `3`.
2. jaggedpine/"Red Dogwood Treant", say "Hail". Requires `ranger_epic` ==3. Gives "Spring Dogwood Seed" (62624).
3. qrg/"Corun Finisc", hand "Spring Dogwood Seed" (62624). Gives "Block of Purest Silver" (62625).

### "Closed Sample Cloth" (62641)

1. Forage "Blasted Stone" (62601) in `bloodfields`.
2. nedaria/"Targen Stonefall", hand "Blasted Stone" (62601). Sets `ranger_epic15_pre` to `2`.
3. nedaria/"Targen Stonefall", say "Bloodfields". Requires `ranger_epic15_pre` ==2. Gives "Sample Cloth" (62640).
4. nedaria/"Targen Stonefall", say "Bloodfields". Requires `ranger_epic15_pre` ==2. Gives "Targen's Emulsion" (62639).
5. Spawns "Stone Collector" (39168) in `hole` on enter.
6. Loot "Dusty Stone" (62653) from "Stone Collector".
7. Combine in "Sample Cloth" (62640): "Targen's Emulsion" (62639), "Dusty Stone" (62653). Produces "Rock of Odus" (62606). The combine does not fail.
8. nedaria/"Targen Stonefall", say "Native Stones". Sets `ranger_epic15_pre` to `1`.
9. nedaria/"Targen Stonefall", hand "Blasted Stone" (62601). Requires `ranger_epic15_pre` ==1. Gives "Washed Blasted Stone" (62602).
10. Combine in "Sample Cloth" (62640): "Rock of Odus" (62606), "Washed Blasted Stone" (62602). Produces "Closed Sample Cloth" (62641). The combine does not fail.

### "Polished Blasted Stone" (62603)

1. Forage "Blasted Stone" (62601) in `bloodfields`.
2. nedaria/"Targen Stonefall", hand "Blasted Stone" (62601). Sets `ranger_epic15_pre` to `2`.
3. nedaria/"Targen Stonefall", say "Bloodfields". Requires `ranger_epic15_pre` ==2. Gives "Sample Cloth" (62640).
4. nedaria/"Targen Stonefall", say "Bloodfields". Requires `ranger_epic15_pre` ==2. Gives "Targen's Emulsion" (62639).
5. Spawns "Stone Collector" (39168) in `hole` on enter.
6. Loot "Dusty Stone" (62653) from "Stone Collector".
7. Combine in "Sample Cloth" (62640): "Targen's Emulsion" (62639), "Dusty Stone" (62653). Produces "Rock of Odus" (62606). The combine does not fail.
8. nedaria/"Targen Stonefall", say "Native Stones". Sets `ranger_epic15_pre` to `1`.
9. nedaria/"Targen Stonefall", hand "Blasted Stone" (62601). Requires `ranger_epic15_pre` ==1. Gives "Washed Blasted Stone" (62602).
10. Combine in "Sample Cloth" (62640): "Rock of Odus" (62606), "Washed Blasted Stone" (62602). Produces "Closed Sample Cloth" (62641). The combine does not fail.
11. nedaria/"Targen Stonefall", hand "Closed Sample Cloth" (62641). Sets `ranger_epic15_pre` to `5`.
12. nedaria/"Targen Stonefall", say "Impurities". Requires `ranger_epic15_pre` ==5. Gives "Polished Blasted Stone" (62603).

### "Stone of Winde" (62604)

1. Say "Ready" to northkarana/"Xanuusus".
2. Spawns "A Tainted Beast" (13131).
3. Loot "Stone of Winde" (62604) from "A Tainted Beast".

### "Sound Capture Jar" (62637)

1. Say "Ready" to northkarana/"Xanuusus".
2. Spawns "A Tainted Beast" (13131).
3. Loot "Stone of Winde" (62604) from "A Tainted Beast".
4. northkarana/"Xanuusus", hand "Stone of Winde" (62604). Sets `ranger_epic15_pre` to `9`.
5. steamfont/"Godbin Strumharp", hand platinum:30. Requires `ranger_epic15_pre` ==9. Gives "Sound Capture Jar" (62637).

### "Swiftwind" (20487)

1. kithicor/"Giz X-Tin", hand "Faelin's Ring" (20446). Gives "Dark Metal Coin" (20447).
2. burningwood/"Telin Darkforest", hand "Dark Metal Coin" (20447). Gives "Worn Dark Metal Coin" (20448).
3. eastkarana/"Althele", hand "Worn Dark Metal Coin" (20448). Gives "Braided Grass Amulet" (20450).
4. eastkarana/"Sionae", hand "Braided Grass Amulet" (20450). Gives "Frayed Braided Grass Amulet" (20451).
5. eastkarana/"Teloa", hand "Frayed Braided Grass Amulet" (20451). Triggers `eastkarana/althele#signal:1`.
6. Starts timer `attack`.
7. Spawns "Corruptor" (15153) after `eastkarana/althele#timer:attack`.
8. Loot "Fleshbound Tome" (20452) from "Corruptor".
9. Loot "Fleshbound Tome" (20452) from "Dark Elf Corruptor".
10. eastkarana/"Althele", hand "Fleshbound Tome" (20452). Gives "Earth Stained Note" (18959).
11. misty/"Ella Foodcrafter", hand "Earth Stained Note" (18959). Sets `shiny_tin_bowl` to `1`.
12. misty/"Ella Foodcrafter", say "Two Tasks". Requires `shiny_tin_bowl` set. Gives "Shiny Tin Bowl" (17860).
13. mistythicket/"Ella Foodcrafter", say "Two Tasks". Requires `shiny_tin_bowl` set. Gives "Shiny Tin Bowl" (17860).
14. Forage "Ripened Heartfruit" (20464) in `gfaydark`.
15. Forage "Sweetened Mudroot" (20465) in `misty`.
16. Forage "Sweetened Mudroot" (20465) in `mistythicket`.
17. Forage "Speckled Molded Mushroom" (20466) in `innothule`.
18. Forage "Chilled Tundra Root" (20467) in `everfrost`.
19. Combine in "Shiny Tin Bowl" (17860): "Ripened Heartfruit" (20464), "Sweetened Mudroot" (20465), "Speckled Molded Mushroom" (20466), "Chilled Tundra Root" (20467). Produces "Hardened Mixture" (20473). Requires Pottery. The combine does not fail.
20. timorous/"Alrik Farsight", say "Take The Artifact". Gives "Crushed Pot" (20457).
21. felwitheb/"Farios Elianos", hand "Crushed Pot" (20457). Gives "Grocery List" (20458).
22. felwithea/"Merchant Nora", hand "Grocery List" (20458). Gives "Bag of Provisions" (20459).
23. qeynos2/"Tomer Instogle", say "Backpack". Gives "Bag of Provisions" (20459).
24. felwitheb/"Farios Elianos", hand "Bag of Provisions" (20459). Gives "Receipt" (20474).
25. kael/"Wenglawks Kkeak", say "Package". Gives "Voucher for Toolset" (25279).
26. kael/"Kellek Felhammer", hand "Voucher for Toolset" (25279). Gives "Coldain Toolset" (25104).
27. iceclad/"Sojan The Sleepless", hand "Coldain Toolset" (25104). Gives "Receipt" (20474).
28. timorous/"Alrik Farsight", hand "Receipt" (20474). Gives "Ancient Pattern" (18960).
29. Kill citymist/"A Black Reaver". Spawns "A Black Reaver" (90004).
30. Loot "Jade Reaver" (5664) from "A Black Reaver".
31. Kill citymist/"A Black Reaver". Spawns "A Black Reaver" (90005).
32. Kill citymist/"A Black Reaver". Spawns "A Black Reaver" (90192).
33. Loot "Jade Reaver" (5664) from "Tzirathk" in `citymist`.
34. Loot "Jade Reaver" (5664) from "A Black Reaver" in `citymist`.
35. kaladimb/"Kinlo Strongarm", hand "Jade Reaver" (5664). Gives "Enchanted Clay" (20455).
36. Forage "Rose of Firiona" (12774) in `firiona`.
37. qrg/"Merdan Fleetfoot", hand "Rose of Firiona" (12774). Gives "Wood Painting" (20475).
38. frontiermtns/"A Human Skeleton", hand "Wood Painting" (20475). Gives "Silver Chained Locket" (20476).
39. qrg/"Niera Farbreeze", hand "Silver Chained Locket" (20476). Gives "Platinum Speckled Powder" (20456).
40. Combine in Pottery Wheel (21): "Ancient Pattern" (18960), "Enchanted Clay" (20455), "Platinum Speckled Powder" (20456). Produces "Runecrested Bowl" (20460). Requires Pottery. The combine does not fail.
41. misty/"Ella Foodcrafter", hand "Runecrested Bowl" (20460) + "Hardened Mixture" (20473). Gives "Softly Glowing Stone" (20462).
42. mistythicket/"Ella Foodcrafter", hand "Runecrested Bowl" (20460) + "Hardened Mixture" (20473). Gives "Softly Glowing Stone" (20462).
43. Hand "Spell: Resurrection" (15392) to karnor/"Spirit Of Venril Sathir". Spawns "Venril Sathir" (102126). Loot "Pulsing Green Stone" (20461) from "Venril Sathir".
44. Loot "Pulsing Green Stone" (20461) from "Venril Sathir".
45. firiona/"Foloal Stormforest", hand "Pulsing Green Stone" (20461) + "Softly Glowing Stone" (20462). Gives "Warmly Glowing Stone" (20468).
46. burningwood/"Telin Darkforest", hand "Warmly Glowing Stone" (20468). Gives "Ancient Longsword" (20477).
47. kaladimb/"Usbak The Old", hand "Ancient Longsword" (20477). Gives "Refined Ancient Sword" (20481).
48. burningwood/"Faelin Bloodbriar", hand "Refined Ancient Sword" (20481). Gives "Swiftwind" (20487).

### "Heated Loadstone" (62628)

1. nedaria/"A Wayfarers Brotherhood Officer", say "Hail". Sets `ranger_epic` to `6`.
2. causeway/"Siflu", say "Adventurers". Requires `ranger_epic` ==6. Gives "Heated Loadstone" (62628).

### "Elemental Ice Spirit Cage" (62647)

1. Loot "Crooked Cage" (32042) from "a Broken Skull bruiser" in `torgiran`.
2. Hand "Shiny Tin Bowl" (17860) to hole/"Jaeil The Wretched". Spawns "Jaeil the Insane" (39154). Loot "Soulbound Hammer" (20478) from "Jaeil the Insane".
3. Loot "Soulbound Hammer" (20478) from "Jaeil the Insane".
4. erudnint/"Mairee Silentone", hand "Soulbound Hammer" (20478). Gives "Dwarven Smiths Hammer" (20479).
5. Kill airplane/"An Essence Carrier". Spawns "An Essence Tamer" (71071).
6. Loot "Swirling Sphere of Color" (20494) from "An Essence Tamer".
7. erudnint/"Mairee Silentone", hand "Dwarven Smiths Hammer" (20479) + "Swirling Sphere of Color" (20494). Gives "Hammer of the Ancients" (20485).
8. kaladimb/"Kinlo Strongarm", hand "Hammer of the Ancients" (20485). Gives "Small bit of Mithril Ore" (20482).
9. kaladimb/"Kinlo Strongarm", hand "Small bit of Mithril Ore" (20482). Gives "Refined Mithril Blade" (20483).
10. Encounter starts when NPC 186201 spawns in `hateplaneb`.
11. Starts timer `popinny`.
12. Kill NPC 186158.
13. Starts timer `text`.
14. Starts timer `text2`.
15. Starts timer `spawninny`.
16. Spawns "Innoruuk" (186107) after `hateplaneb/inny#timer:spawninny`.
17. Loot "Shattered Emerald of Corruption" (20484) from "Innoruuk".
18. Encounter starts when NPC 186196 spawns in `hateplaneb`.
19. Starts timer `popmaestro`.
20. Spawns "Maestro of Rancor" (186111) after `hateplaneb/maestro#timer:popmaestro`.
21. Loot "Shattered Emerald of Corruption" (20484) from "Maestro of Rancor".
22. northkarana/"Xanuusus", hand "Refined Mithril Blade" (20483) + "Shattered Emerald of Corruption" (20484). Gives "Earthcaller" (20488).
23. eastkarana/"Althele", hand "Worn Dark Metal Coin" (20448). Gives "Braided Grass Amulet" (20450).
24. eastkarana/"Sionae", hand "Braided Grass Amulet" (20450). Gives "Frayed Braided Grass Amulet" (20451).
25. eastkarana/"Teloa", hand "Frayed Braided Grass Amulet" (20451). Triggers `eastkarana/althele#signal:1`.
26. Starts timer `attack`.
27. Spawns "Corruptor" (15153) after `eastkarana/althele#timer:attack`.
28. Loot "Fleshbound Tome" (20452) from "Corruptor".
29. Loot "Fleshbound Tome" (20452) from "Dark Elf Corruptor".
30. eastkarana/"Althele", hand "Fleshbound Tome" (20452). Gives "Earth Stained Note" (18959).
31. misty/"Ella Foodcrafter", hand "Earth Stained Note" (18959). Sets `shiny_tin_bowl` to `1`.
32. misty/"Ella Foodcrafter", say "Two Tasks". Requires `shiny_tin_bowl` set. Gives "Shiny Tin Bowl" (17860).
33. mistythicket/"Ella Foodcrafter", say "Two Tasks". Requires `shiny_tin_bowl` set. Gives "Shiny Tin Bowl" (17860).
34. Forage "Ripened Heartfruit" (20464) in `gfaydark`.
35. Forage "Sweetened Mudroot" (20465) in `misty`.
36. Forage "Sweetened Mudroot" (20465) in `mistythicket`.
37. Forage "Speckled Molded Mushroom" (20466) in `innothule`.
38. Forage "Chilled Tundra Root" (20467) in `everfrost`.
39. Combine in "Shiny Tin Bowl" (17860): "Ripened Heartfruit" (20464), "Sweetened Mudroot" (20465), "Speckled Molded Mushroom" (20466), "Chilled Tundra Root" (20467). Produces "Hardened Mixture" (20473). Requires Pottery. The combine does not fail.
40. timorous/"Alrik Farsight", say "Take The Artifact". Gives "Crushed Pot" (20457).
41. felwitheb/"Farios Elianos", hand "Crushed Pot" (20457). Gives "Grocery List" (20458).
42. felwithea/"Merchant Nora", hand "Grocery List" (20458). Gives "Bag of Provisions" (20459).
43. qeynos2/"Tomer Instogle", say "Backpack". Gives "Bag of Provisions" (20459).
44. felwitheb/"Farios Elianos", hand "Bag of Provisions" (20459). Gives "Receipt" (20474).
45. kael/"Wenglawks Kkeak", say "Package". Gives "Voucher for Toolset" (25279).
46. kael/"Kellek Felhammer", hand "Voucher for Toolset" (25279). Gives "Coldain Toolset" (25104).
47. iceclad/"Sojan The Sleepless", hand "Coldain Toolset" (25104). Gives "Receipt" (20474).
48. timorous/"Alrik Farsight", hand "Receipt" (20474). Gives "Ancient Pattern" (18960).
49. Kill citymist/"A Black Reaver". Spawns "A Black Reaver" (90004).
50. Loot "Jade Reaver" (5664) from "A Black Reaver".
51. Kill citymist/"A Black Reaver". Spawns "A Black Reaver" (90005).
52. Kill citymist/"A Black Reaver". Spawns "A Black Reaver" (90192).
53. Loot "Jade Reaver" (5664) from "Tzirathk" in `citymist`.
54. Loot "Jade Reaver" (5664) from "A Black Reaver" in `citymist`.
55. kaladimb/"Kinlo Strongarm", hand "Jade Reaver" (5664). Gives "Enchanted Clay" (20455).
56. Forage "Rose of Firiona" (12774) in `firiona`.
57. qrg/"Merdan Fleetfoot", hand "Rose of Firiona" (12774). Gives "Wood Painting" (20475).
58. frontiermtns/"A Human Skeleton", hand "Wood Painting" (20475). Gives "Silver Chained Locket" (20476).
59. qrg/"Niera Farbreeze", hand "Silver Chained Locket" (20476). Gives "Platinum Speckled Powder" (20456).
60. Combine in Pottery Wheel (21): "Ancient Pattern" (18960), "Enchanted Clay" (20455), "Platinum Speckled Powder" (20456). Produces "Runecrested Bowl" (20460). Requires Pottery. The combine does not fail.
61. misty/"Ella Foodcrafter", hand "Runecrested Bowl" (20460) + "Hardened Mixture" (20473). Gives "Softly Glowing Stone" (20462).
62. mistythicket/"Ella Foodcrafter", hand "Runecrested Bowl" (20460) + "Hardened Mixture" (20473). Gives "Softly Glowing Stone" (20462).
63. Hand "Spell: Resurrection" (15392) to karnor/"Spirit Of Venril Sathir". Spawns "Venril Sathir" (102126). Loot "Pulsing Green Stone" (20461) from "Venril Sathir".
64. Loot "Pulsing Green Stone" (20461) from "Venril Sathir".
65. firiona/"Foloal Stormforest", hand "Pulsing Green Stone" (20461) + "Softly Glowing Stone" (20462). Gives "Warmly Glowing Stone" (20468).
66. burningwood/"Telin Darkforest", hand "Warmly Glowing Stone" (20468). Gives "Ancient Longsword" (20477).
67. kaladimb/"Usbak The Old", hand "Ancient Longsword" (20477). Gives "Refined Ancient Sword" (20481).
68. burningwood/"Faelin Bloodbriar", hand "Refined Ancient Sword" (20481). Gives "Swiftwind" (20487).
69. No quest step gives Living Fragment of Fire (28294). The dump lists it in pofire.
70. Loot "Living Fragment of Water" (28293) from "A Triloun Diviner" in `powater`.
71. Loot "Living Fragment of Water" (28293) from "A Triloun Keeper" in `powater`.
72. Loot "Living Fragment of Water" (28293) from "A Triloun Water Guardian" in `powater`.
73. nedaria/"A Wayfarers Brotherhood Officer", say "Hail". Sets `ranger_epic` to `6`.
74. causeway/"Siflu", say "Adventurers". Requires `ranger_epic` ==6. Gives "Heated Loadstone" (62628).
75. Spawns "A Mangled Muramite Captain" (300069) in `wallofslaughter` on enter.
76. Loot "Spirit Manacles" (72340) from "A Mangled Muramite Captain".
77. Loot "Spirit Manacles" (72340) from "A Mangled Muramite Captain" in `wallofslaughter`.
78. Combine in "Crooked Cage" (32042): "Earthcaller" (20488), "Swiftwind" (20487), "Living Fragment of Fire" (28294), "Living Fragment of Water" (28293), "Heated Loadstone" (62628), "Spirit Manacles" (72340). Hands back "Earthcaller" (20488), "Swiftwind" (20487). Produces "Spirit Cage" (62656). The combine does not fail.
79. Spawns "A Vekerchiki Drone" (218047) in `poeartha` on event_combat.
80. Loot "Living Fragment of Earth" (28295) from "A Vekerchiki Drone".
81. Spawns "A Vekerchiki Warrior" (218025) in `poeartha` on event_combat.
82. Loot "Living Fragment of Earth" (28295) from "A Vekerchiki Warrior".
83. Loot "Living Fragment of Earth" (28295) from "A Vekerchiki Soldier" in `poearthb`.
84. Loot "Living Fragment of Earth" (28295) from "An Earthcrafted Assassin" in `poeartha`.
85. Loot "Living Fragment of Air" (28292) from "A Temple Guardian".
86. Loot "Living Fragment of Air" (28292) from "A Temple Guardian" in `poair`.
87. Combine in "Crooked Cage" (32042): "Living Fragment of Fire" (28294), "Living Fragment of Water" (28293), "Heated Loadstone" (62628), "Spirit Manacles" (72340), "Living Fragment of Earth" (28295), "Living Fragment of Air" (28292). Produces "Spirit Cage" (62656). The combine does not fail.
88. Spawns "Craftmaster Tieranu" (334087) in `riftseekers` on enter.
89. Loot "Ring of Warmth" (11427) from "Craftmaster Tieranu".
90. Loot "Ring of Warmth" (11427) from "Craftmaster Tieranu" in `riftseekers`.
91. Spawns "Herrian Warfrost" (300057) in `wallofslaughter` on enter.
92. Loot "Hoarfrost Wand" (76999) from "Herrian Warfrost".
93. Loot "Hoarfrost Wand" (76999) from "Herrian Warfrost" in `wallofslaughter`.
94. Combine in "Spirit Cage" (62656): "Ring of Warmth" (11427), "Hoarfrost Wand" (76999). Produces "Elemental Ice Spirit Cage" (62647). The combine does not fail.

### "Heartwood Blade" (62627)

1. No quest step gives Planar Fletching Kit (17762). The dump lists it in poknowledge.
2. Requires `ranger_dranik_chest` unset; no setter establishes this state.
3. global/"Global Player", combine recipe 13412. Sets `ranger_epic` to `3`.
4. jaggedpine/"Red Dogwood Treant", say "Hail". Requires `ranger_epic` ==3. Gives "Red Dogwood Heartwood" (62623).
5. dranik/"Ranger 1 5", hand "Red Dogwood Heartwood" (62623). Requires `ranger_dranik_chest` unset. Gives "Wind-blessed Heartwood" (62626).
6. jaggedpine/"Red Dogwood Treant", say "Hail". Requires `ranger_epic` ==3. Gives "Spring Dogwood Seed" (62624).
7. qrg/"Corun Finisc", hand "Spring Dogwood Seed" (62624). Gives "Block of Purest Silver" (62625).
8. Combine in "Planar Fletching Kit" (17762): "Wind-blessed Heartwood" (62626), "Block of Purest Silver" (62625). Produces "Heartwood Blade" (62627). Requires Fletching. The combine does not fail.

## `ranger_epic`

Values written: 1, 2, 3, 5, 6, 7.

### 1. althele — say hail

Zone: `eastkarana`.

> Hello, friend. Beautiful is what I would call such a day normally, but lately? I sense that something is [

Sets `ranger_epic` to `1`.

- Needs `ranger_epic` unset.
- One of: Earthcaller (20488); Essence of Earth and Wind (62600).
In script order:

1. Sets `ranger_epic` to `1`.


How the items are reached:

- Earthcaller (20488)
  - Prerequisite: "Earthcaller" (20488). See section 0.
- Essence of Earth and Wind (62600)
  - Prerequisite: "Essence of Earth and Wind" (62600). See section 0.

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
  - Loot "Traveler's Journal" (62629) from "A Mangled Muramite Captain" in `wallofslaughter`.

### Steps on `ranger_epic` that do not change it

- `bloodfields` marshall trap, on enter needs `ranger_epic` ==2.
  - Sets `ranger_epic_bloodfield` to `1`.
  - Spawns Marshal Histent (301065).
  - Spawns Grinbik the Fertile (301066).
  - Spawns an enslaved earthmover (301067).
  - Spawns an eager student (301068).
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
- `eastkarana` althele, say out of balance needs `ranger_epic` ==1.
  - Sets `druid_epic` to `1`.
- `jaggedpine` red dogwood treant, say hail needs `ranger_epic` ==3.
  - Gives Red Dogwood Heartwood (62623).
  - Gives Spring Dogwood Seed (62624).
- `natimbi` trenzar trap, on enter needs `ranger_epic` ==2.
  - Sets `ranger_epic_natimbi` to `1`.
  - Spawns Spiritbinder Trenzar (280084).
  - Spawns a bound earth spirit (280085).
  - Spawns a bound fire spirit (280086).
- `thedeep` player, on enter needs `ranger_epic` ==2.
  - Sets `ranger_epic_deep` to `1`.
  - Spawns ancient thought horror trap (164123).
- `veksar` player, on enter needs `ranger_epic` ==1.
  - Sets `warrior_epic_gulak` to `1`.
  - Spawns Decaying Lord Galuk Drek, not be in db yet (109906).
  - Sets `ranger_epic_veks` to `1`.
  - Spawns an asteatotic highborn (109907).
  - Loots Skeletal Tome of Galuk Drek (60310).
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
- `northkarana` xanuusus, say ready needs `ranger_epic15_pre` ==8.
  - Spawns A Tainted Beast (13131).
  - Loots Stone of Winde (62604).
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
    - No quest step gives Living Fragment of Fire (28294). The dump lists it in pofire.
  - Put in x1: Living Fragment of Water (28293).
    - Loot "Living Fragment of Water" (28293) from "A Triloun Diviner" in `powater`.
    - Loot "Living Fragment of Water" (28293) from "A Triloun Keeper" in `powater`.
    - Loot "Living Fragment of Water" (28293) from "A Triloun Water Guardian" in `powater`.
  - Put in x1: Heated Loadstone (62628).
    - Prerequisite: "Heated Loadstone" (62628). See section 0.
  - Put in x1: Spirit Manacles (72340).
    - Spawns "A Mangled Muramite Captain" (300069) in `wallofslaughter` on enter.
    - Loot "Spirit Manacles" (72340) from "A Mangled Muramite Captain".
    - Loot "Spirit Manacles" (72340) from "A Mangled Muramite Captain" in `wallofslaughter`.
  - Hands back Earthcaller (20488), Swiftwind (20487).
  - Produces Spirit Cage (62656).
  - The combine does not fail.

### 8. global player — combine recipe 19915

Zone: `global`.

Sets `ranger_epic` to `8`.

In script order:

1. Sets `ranger_epic` to `8`.


Combine:

- `recipe:19915` is combined in Crooked Cage (32042).
  - Loot "Crooked Cage" (32042) from "a Broken Skull bruiser" in `torgiran`.
  - Put in x1: Living Fragment of Fire (28294).
    - No quest step gives Living Fragment of Fire (28294). The dump lists it in pofire.
  - Put in x1: Living Fragment of Water (28293).
    - Loot "Living Fragment of Water" (28293) from "A Triloun Diviner" in `powater`.
    - Loot "Living Fragment of Water" (28293) from "A Triloun Keeper" in `powater`.
    - Loot "Living Fragment of Water" (28293) from "A Triloun Water Guardian" in `powater`.
  - Put in x1: Heated Loadstone (62628).
    - Prerequisite: "Heated Loadstone" (62628). See section 0.
  - Put in x1: Spirit Manacles (72340).
    - Spawns "A Mangled Muramite Captain" (300069) in `wallofslaughter` on enter.
    - Loot "Spirit Manacles" (72340) from "A Mangled Muramite Captain".
    - Loot "Spirit Manacles" (72340) from "A Mangled Muramite Captain" in `wallofslaughter`.
  - Put in x1: Living Fragment of Earth (28295).
    - Spawns "A Vekerchiki Drone" (218047) in `poeartha` on event_combat.
    - Loot "Living Fragment of Earth" (28295) from "A Vekerchiki Drone".
    - Spawns "A Vekerchiki Warrior" (218025) in `poeartha` on event_combat.
    - Loot "Living Fragment of Earth" (28295) from "A Vekerchiki Warrior".
    - Loot "Living Fragment of Earth" (28295) from "A Vekerchiki Drone".
    - Loot "Living Fragment of Earth" (28295) from "A Vekerchiki Soldier" in `poearthb`.
    - Loot "Living Fragment of Earth" (28295) from "A Vekerchiki Warrior".
    - Loot "Living Fragment of Earth" (28295) from "An Earthcrafted Assassin" in `poeartha`.
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
  - Say "Check Lorb" to anguish/"Zone Status".
  - Spawns "Orb of Discordant Energy" (317087).
  - Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy".
  - Say "Check Uorb" to anguish/"Zone Status".
  - Spawns "Orb of Discordant Energy" (317087).
  - Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy".
  - Say "Check Amv Chest" to anguish/"Zone Status".
  - Spawns "Ornate Chest" (317112).
  - Loot "Globe of Discordant Energy" (47100) from "Ornate Chest".
  - 2 other loot steps also yield Globe of Discordant Energy (47100).
  - Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy" in `anguish`.
  - Loot "Globe of Discordant Energy" (47100) from "Ornate Chest".
  - Loot "Globe of Discordant Energy" (47100) from "Overlords Chest".
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
  - Sets `paladin_wos` to `1`.
  - Spawns Durunal the Cursebearer (300087).
  - Sets `rng_spawn_wos` to `1`.
  - Spawns Herrian Warfrost (300057).
  - Spawns an excited builder (300058).
  - Loots Dark and Twisted Sword (69971).
  - Loots Gelidran Blood (72073).
  - Loots Hoarfrost Wand (76999).
  - Loots Polished Blue Softstone (80030).
  - Loots Sunshard Powder (35088).
  - Loots Platinum Etched Reinforced Rod (37046).
  - Loots Raw Crimson Nihilite (58067).
- `wallofslaughter` player, on loot needs `ranger_epic` ==8.
  - Sets `warr_epic_wos` to `1`.
  - Spawns a chest (Epic 1.5) (283157).
  - Sets `wiz_wos_chest` to `1`.
  - Sets `paladin_epic_wos` to `1`.
  - Sets `shaman_epic_wos` to `1`.
  - Spawns a chest (Epic 1.5) (893).
  - Sets `druid_epic_wos` to `1`.
  - Sets `rng_wos_chest` to `1`.
  - Sets `ench_wos_chest` to `1`.
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

- `ranger_epic_bloodfield` set to 1 at bloodfields/marshall trap.
- `ranger_epic_deep` set to 1 at thedeep/player.
- `ranger_epic_dranik` set to 1 at dranik/sverins trap.
- `ranger_epic_natimbi` set to 1 at natimbi/trenzar trap.
- `ranger_epic_veks` set to 1 at veksar/player.
- `ranger_epic_wyv` set to 1 at westwastes/player.
