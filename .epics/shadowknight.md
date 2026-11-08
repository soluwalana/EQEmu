# Shadow Knight

Steps taken from the quest graph only. **Broken** means the graph has no edge for that value or that item.

Flags with writes: `shadowknight_pre`, `shadowknight_epic`.

## 0. Prerequisites

Each list is the order you obtain that item. Later steps point here instead of repeating the chain.

### "Innoruuk's Curse" (14383)

1. neriakc/"Selzar L-Crit", say "Armor". Gives "Note to Kanthuk" (2416).
2. butcher/"Kanthuk Ogrebane", hand "Note to Kanthuk" (2416). Sets `Kanthuk` to `ghoul`.
3. butcher/"Kanthuk Ogrebane", say "Strange Image". Requires `Kanthuk` set. Gives "Pendant" (2414).
4. cauldron/"Llara", hand "Pendant" (2414). Sets `Llara` to `ghoul`.
5. cauldron/"Llara", say "Ruathey". Requires `Llara` set. Gives "Note to Ruathey" (2417).
6. lavastorm/"Ruathey", hand "Note to Ruathey" (2417). Sets `Ruathey` to `ghoul`.
7. lavastorm/"Ruathey", hand "Note to Ruathey" (2417). Sets `ruathey_note` to `1`.
8. lavastorm/"Ruathey", say "Bag". Requires `Ruathey` set. Requires `ruathey_note` ==1. Requires `ruathey_note` set. Gives "Nobleman's Bag" (17878).
9. Loot "Ghoul's Heart" (2410) from "A Ghoul" (NPC 63011) in `unrest`. Drop cache: 25% chance per kill.
10. Loot "Amstaf's Scroll" (2411) from "A Goblin Thief" (NPC 6150) in `highkeep`. Drop cache: 35% chance per kill.
11. Loot "Blade of Nobility" (2412) from "A Crazed Goblin" (NPC 68162) in `butcher`. Drop cache: 10.57% chance per kill.
12. Loot "Hilt of the Nobleman" (2413) from "Ekeros" in `najena`.
13. Loot "Hilt of the Nobleman" (2413) from "A Skeleton" in `najena`.
14. Combine in "Nobleman's Bag" (17878): "Ghoul's Heart" (2410), "Amstaf's Scroll" (2411), "Blade of Nobility" (2412), "Hilt of the Nobleman" (2413). Produces "Ghoulbane" (5403). The combine does not fail.
15. Loot "Soul Leech, Dark Sword of Blood" (11609) from "Dread" in `fearplane`.
16. Loot "Soul Leech, Dark Sword of Blood" (11609) from "Fright" in `fearplane`.
17. Loot "Soul Leech, Dark Sword of Blood" (11609) from "Terror" in `fearplane`.
18. airplane/"A Soul Carrier", on event_death_complete. Triggers `airplane/key master#signal:2`.
19. Starts timer `87`.
20. Spawns "Keeper of Souls" (71075) after `airplane/key master#timer:87`.
21. Loot "Blade of Abrogation" (5430) from "Keeper of Souls".
22. 12 alternative loot source(s) also yield Blade of Abrogation (5430).
23. Loot "Drake Spine" (14372) from "Rharzar" in `rathemtn`.
24. Loot "Decrepit Hide" (14371) from "An Ashenbone Drake" (NPC 186049) in `hateplaneb`. Drop cache: 11.2% chance per kill.
25. Summon "Enchanted Platinum Bar" (16507) by casting "Enchant Platinum", "Mass Enchant Platinum", "Greater Mass Enchant Platinum".
26. qcat/"Teydar", hand "Decrepit Hide" (14371) + "Drake Spine" (14372) + "Enchanted Platinum Bar" (16507). Gives "Decrepit Sheath" (14366).
27. paineel/"Duriek Bloodpool", hand "Ghoulbane" (5403) + "Blade of Abrogation" (5430) + "Soul Leech, Dark Sword of Blood" (11609) + "Decrepit Sheath" (14366). Gives "Corrupted Ghoulbane" (14367).
28. tox/"Knarthenne Skurl", say "Heart Of An Innocent". Gives "Soulcase" (17051).
29. Loot "Cell Key" (14373) from "A Chest" in `hole`.
30. Hand "Cell Key" (14373) to hole/"Caradon". Spawns "Kyrenna" (39155). Loot "Heart of Kyrenna" (14380) from "Kyrenna".
31. Combine in "Soulcase" (17051): "Heart of Kyrenna" (14380). Produces "Heart of the Innocent" (14368). The combine does not fail.
32. Hand "Cell Key" (14373) to hole/"Caradon". Spawns "Kyrenna" (39155). Loot "Blood of Kyrenna" (14381) from "Kyrenna".
33. kerraridge/"Marl Kastane", hand "Blood of Kyrenna" (14381). Gives "Dark Shroud" (14377).
34. Hand "Dark Shroud" (14377) to hole/"Ghost Of Glohnor". Spawns "Mummy of Glohnor" (39165). Loot "Head of Glohnor" (14378) from "Mummy of Glohnor".
35. paineel/"Gerot Kastane", hand "Head of Glohnor" (14378). Gives "Head of the Valiant" (14369).
36. Hand "Dark Shroud" (14377) to hole/"Ghost Of Glohnor". Spawns "Mummy of Glohnor" (39165). Loot "Glohnor wrappings" (14379) from "Mummy of Glohnor".
37. kerraridge/"Marl Kastane", hand "Glohnor wrappings" (14379). Gives "Will of Innoruuk" (14370).
38. citymist/"Lhranc", hand "Corrupted Ghoulbane" (14367) + "Heart of the Innocent" (14368) + "Head of the Valiant" (14369) + "Will of Innoruuk" (14370). Gives "Lhranc's Token" (14384).
39. citymist/"Marl Kastane", hand "Lhranc's Token" (14384). Gives "Innoruuk's Curse" (14383).

### "Innoruuk's Voice" (22944)

1. dulak/"Ritald", say "Hail". Sets `shadowknight_pre` to `1`.
2. Loot "Ancient Flamberge of Hatred" (55902) from "Captain Varns" in `dulak`.
3. Loot "Essence of Hate" (21870) from "Mistress of Malevolence" in `hateplaneb`.
4. Loot "Essence of Hate" (21870) from "Overlord R'Gahbsa" in `hateplaneb`.
5. Loot "Stormborn Phylactery" (21782) from "Olidan" in `postorms`.
6. dulak/"Ritald", hand "Stormborn Phylactery" (21782) + "Essence of Hate" (21870) + "Ancient Flamberge of Hatred" (55902). Requires `shadowknight_pre` ==1. Gives "Innoruuk's Voice" (22944).

### "The Silent Gods" (20520)

1. dulak/"Ritald", say "Hail". Sets `shadowknight_pre` to `1`.
2. Loot "Ancient Flamberge of Hatred" (55902) from "Captain Varns" in `dulak`.
3. Loot "Essence of Hate" (21870) from "Mistress of Malevolence" in `hateplaneb`.
4. Loot "Essence of Hate" (21870) from "Overlord R'Gahbsa" in `hateplaneb`.
5. Loot "Stormborn Phylactery" (21782) from "Olidan" in `postorms`.
6. dulak/"Ritald", hand "Stormborn Phylactery" (21782) + "Essence of Hate" (21870) + "Ancient Flamberge of Hatred" (55902). Sets `shadowknight_pre` to `2`.
7. Unresolved cyclic prerequisite: `shadowknight_epic` ==1.
8. poknowledge/"Sienn Kastane", say "Hail". Sets `shadowknight_epic` to `1`.
9. Loot "Gelatinous Murkglider Egg" (55900) from "Murkglider Breeder" in `dranik`.
10. poknowledge/"Grand Librarian Maelin", hand "Gelatinous Murkglider Egg" (55900). Requires `shadowknight_epic` ==1. Gives "The Silent Gods" (20520).

### "Sheath of Darktidings" (20426)

1. Summon "Collapsible Sewing Kit" (17165) by casting "Unfold Sewing Kit".
2. Loot "Eye of the Dark God" (21675) from "Amygdalan warrior" (NPC 72015) in `fearplane`. Drop cache: 18.32% chance per kill.
3. Loot "Gloom Nightmare Hide" (20622) from "A Gloom Nightmare" in `ponightmare`.
4. Loot "Lock of Blessed Unicorn Hair" (21496) from "A Rolling Plains Steed" (NPC 127084) in `growthplane`. Drop cache: 11% chance per kill.
5. Combine in "Collapsible Sewing Kit" (17165): "Eye of the Dark God" (21675), "Gloom Nightmare Hide" (20622), "Lock of Blessed Unicorn Hair" (21496). Produces "Sheath of Darktidings" (20426). Requires Tailoring 100. Trivial at 15. The combine does not fail.

### "Sheathed Innoruuk's Voice" (11407)

1. dulak/"Ritald", say "Hail". Sets `shadowknight_pre` to `1`.
2. Loot "Ancient Flamberge of Hatred" (55902) from "Captain Varns" in `dulak`.
3. Loot "Essence of Hate" (21870) from "Mistress of Malevolence" in `hateplaneb`.
4. Loot "Essence of Hate" (21870) from "Overlord R'Gahbsa" in `hateplaneb`.
5. Loot "Stormborn Phylactery" (21782) from "Olidan" in `postorms`.
6. dulak/"Ritald", hand "Stormborn Phylactery" (21782) + "Essence of Hate" (21870) + "Ancient Flamberge of Hatred" (55902). Sets `shadowknight_pre` to `2`.
7. Unresolved cyclic prerequisite: `shadowknight_epic` ==1.
8. poknowledge/"Sienn Kastane", say "Hail". Sets `shadowknight_epic` to `1`.
9. Loot "Gelatinous Murkglider Egg" (55900) from "Murkglider Breeder" in `dranik`.
10. poknowledge/"Grand Librarian Maelin", hand "Gelatinous Murkglider Egg" (55900). Requires `shadowknight_epic` ==1. Gives "The Silent Gods" (20520).
11. poknowledge/"Sienn Kastane", hand "The Silent Gods" (20520). Sets `shadowknight_epic` to `2`.
12. Summon "Collapsible Sewing Kit" (17165) by casting "Unfold Sewing Kit".
13. Loot "Eye of the Dark God" (21675) from "Amygdalan warrior" (NPC 72015) in `fearplane`. Drop cache: 18.32% chance per kill.
14. Loot "Gloom Nightmare Hide" (20622) from "A Gloom Nightmare" in `ponightmare`.
15. Loot "Lock of Blessed Unicorn Hair" (21496) from "A Rolling Plains Steed" (NPC 127084) in `growthplane`. Drop cache: 11% chance per kill.
16. Combine in "Collapsible Sewing Kit" (17165): "Eye of the Dark God" (21675), "Gloom Nightmare Hide" (20622), "Lock of Blessed Unicorn Hair" (21496). Produces "Sheath of Darktidings" (20426). Requires Tailoring 100. Trivial at 15. The combine does not fail.
17. poknowledge/"Sienn Kastane", hand "Sheath of Darktidings" (20426). Sets `shadowknight_epic` to `3`.
18. Loot "Fraga's Parchment" (23492) from "Fraga" in `povalor`.
19. poknowledge/"Sienn Kastane", hand "Fraga's Parchment" (23492). Sets `shadowknight_epic` to `4`.
20. Loot "Wailing Sister Blood" (20497) from "The Wailing Sister" in `ponightmare`.
21. Loot "Wailing Rune" (19025) from "The Wailing Sister" in `ponightmare`.
22. poknowledge/"Sienn Kastane", hand "Wailing Rune" (19025) + "Wailing Sister Blood" (20497). Requires `shadowknight_epic` ==4. Gives "Sheathed Innoruuk's Voice" (11407).

### "Sheathed Innoruuk's Voice" (22199)

1. dulak/"Ritald", say "Hail". Sets `shadowknight_pre` to `1`.
2. Loot "Ancient Flamberge of Hatred" (55902) from "Captain Varns" in `dulak`.
3. Loot "Essence of Hate" (21870) from "Mistress of Malevolence" in `hateplaneb`.
4. Loot "Essence of Hate" (21870) from "Overlord R'Gahbsa" in `hateplaneb`.
5. Loot "Stormborn Phylactery" (21782) from "Olidan" in `postorms`.
6. dulak/"Ritald", hand "Stormborn Phylactery" (21782) + "Essence of Hate" (21870) + "Ancient Flamberge of Hatred" (55902). Sets `shadowknight_pre` to `2`.
7. Unresolved cyclic prerequisite: `shadowknight_epic` ==1.
8. poknowledge/"Sienn Kastane", say "Hail". Sets `shadowknight_epic` to `1`.
9. Loot "Gelatinous Murkglider Egg" (55900) from "Murkglider Breeder" in `dranik`.
10. poknowledge/"Grand Librarian Maelin", hand "Gelatinous Murkglider Egg" (55900). Requires `shadowknight_epic` ==1. Gives "The Silent Gods" (20520).
11. poknowledge/"Sienn Kastane", hand "The Silent Gods" (20520). Sets `shadowknight_epic` to `2`.
12. Summon "Collapsible Sewing Kit" (17165) by casting "Unfold Sewing Kit".
13. Loot "Eye of the Dark God" (21675) from "Amygdalan warrior" (NPC 72015) in `fearplane`. Drop cache: 18.32% chance per kill.
14. Loot "Gloom Nightmare Hide" (20622) from "A Gloom Nightmare" in `ponightmare`.
15. Loot "Lock of Blessed Unicorn Hair" (21496) from "A Rolling Plains Steed" (NPC 127084) in `growthplane`. Drop cache: 11% chance per kill.
16. Combine in "Collapsible Sewing Kit" (17165): "Eye of the Dark God" (21675), "Gloom Nightmare Hide" (20622), "Lock of Blessed Unicorn Hair" (21496). Produces "Sheath of Darktidings" (20426). Requires Tailoring 100. Trivial at 15. The combine does not fail.
17. poknowledge/"Sienn Kastane", hand "Sheath of Darktidings" (20426). Sets `shadowknight_epic` to `3`.
18. Loot "Fraga's Parchment" (23492) from "Fraga" in `povalor`.
19. poknowledge/"Sienn Kastane", hand "Fraga's Parchment" (23492). Sets `shadowknight_epic` to `4`.
20. Loot "Wailing Sister Blood" (20497) from "The Wailing Sister" in `ponightmare`.
21. Loot "Wailing Rune" (19025) from "The Wailing Sister" in `ponightmare`.
22. poknowledge/"Sienn Kastane", hand "Wailing Rune" (19025) + "Wailing Sister Blood" (20497). Sets `shadowknight_epic` to `5`.
23. poknowledge/"Sienn Kastane", hand "Wailing Rune" (19025) + "Wailing Sister Blood" (20497). Requires `shadowknight_epic` ==4. Gives "Sheathed Innoruuk's Voice" (11407).
24. poknowledge/"Gilina Yilzior", hand "Sheathed Innoruuk's Voice" (11407). Sets `shadowknight_epic` to `6`.
25. Loot "Skurza's Head" (20899) from "Skurza Slicekutt" in `swampofnohope`.
26. Loot "Silithis's Head" (16813) from "Silithis Sisnta" in `timorous`.
27. Loot "Gubblegrot's Head" (16793) from "Gubblegrot Smashfist" in `oceanoftears`.
28. Loot "Gubblegrot's Head" (16793) from "Gubblegrot Smashfist" in `oot`.
29. Loot "Giligatabbus's Head" (20079) from "Giligatabbus Igglebix" in `iceclad`.
30. poknowledge/"Gilina Yilzior", hand "Gubblegrot's Head" (16793) + "Silithis's Head" (16813) + "Giligatabbus's Head" (20079) + "Skurza's Head" (20899). Requires `shadowknight_epic` ==6. Gives "Sheathed Innoruuk's Voice" (22199).

### "Innoruuk's Voice" (50003)

1. dulak/"Ritald", say "Hail". Sets `shadowknight_pre` to `1`.
2. Loot "Ancient Flamberge of Hatred" (55902) from "Captain Varns" in `dulak`.
3. Loot "Essence of Hate" (21870) from "Mistress of Malevolence" in `hateplaneb`.
4. Loot "Essence of Hate" (21870) from "Overlord R'Gahbsa" in `hateplaneb`.
5. Loot "Stormborn Phylactery" (21782) from "Olidan" in `postorms`.
6. dulak/"Ritald", hand "Stormborn Phylactery" (21782) + "Essence of Hate" (21870) + "Ancient Flamberge of Hatred" (55902). Sets `shadowknight_pre` to `2`.
7. Unresolved cyclic prerequisite: `shadowknight_epic` ==1.
8. poknowledge/"Sienn Kastane", say "Hail". Sets `shadowknight_epic` to `1`.
9. Loot "Gelatinous Murkglider Egg" (55900) from "Murkglider Breeder" in `dranik`.
10. poknowledge/"Grand Librarian Maelin", hand "Gelatinous Murkglider Egg" (55900). Requires `shadowknight_epic` ==1. Gives "The Silent Gods" (20520).
11. poknowledge/"Sienn Kastane", hand "The Silent Gods" (20520). Sets `shadowknight_epic` to `2`.
12. Summon "Collapsible Sewing Kit" (17165) by casting "Unfold Sewing Kit".
13. Loot "Eye of the Dark God" (21675) from "Amygdalan warrior" (NPC 72015) in `fearplane`. Drop cache: 18.32% chance per kill.
14. Loot "Gloom Nightmare Hide" (20622) from "A Gloom Nightmare" in `ponightmare`.
15. Loot "Lock of Blessed Unicorn Hair" (21496) from "A Rolling Plains Steed" (NPC 127084) in `growthplane`. Drop cache: 11% chance per kill.
16. Combine in "Collapsible Sewing Kit" (17165): "Eye of the Dark God" (21675), "Gloom Nightmare Hide" (20622), "Lock of Blessed Unicorn Hair" (21496). Produces "Sheath of Darktidings" (20426). Requires Tailoring 100. Trivial at 15. The combine does not fail.
17. poknowledge/"Sienn Kastane", hand "Sheath of Darktidings" (20426). Sets `shadowknight_epic` to `3`.
18. Loot "Fraga's Parchment" (23492) from "Fraga" in `povalor`.
19. poknowledge/"Sienn Kastane", hand "Fraga's Parchment" (23492). Sets `shadowknight_epic` to `4`.
20. Loot "Wailing Sister Blood" (20497) from "The Wailing Sister" in `ponightmare`.
21. Loot "Wailing Rune" (19025) from "The Wailing Sister" in `ponightmare`.
22. poknowledge/"Sienn Kastane", hand "Wailing Rune" (19025) + "Wailing Sister Blood" (20497). Sets `shadowknight_epic` to `5`.
23. poknowledge/"Sienn Kastane", hand "Wailing Rune" (19025) + "Wailing Sister Blood" (20497). Requires `shadowknight_epic` ==4. Gives "Sheathed Innoruuk's Voice" (11407).
24. poknowledge/"Gilina Yilzior", hand "Sheathed Innoruuk's Voice" (11407). Sets `shadowknight_epic` to `6`.
25. Loot "Skurza's Head" (20899) from "Skurza Slicekutt" in `swampofnohope`.
26. Loot "Silithis's Head" (16813) from "Silithis Sisnta" in `timorous`.
27. Loot "Gubblegrot's Head" (16793) from "Gubblegrot Smashfist" in `oceanoftears`.
28. Loot "Gubblegrot's Head" (16793) from "Gubblegrot Smashfist" in `oot`.
29. Loot "Giligatabbus's Head" (20079) from "Giligatabbus Igglebix" in `iceclad`.
30. poknowledge/"Gilina Yilzior", hand "Gubblegrot's Head" (16793) + "Silithis's Head" (16813) + "Giligatabbus's Head" (20079) + "Skurza's Head" (20899). Sets `shadowknight_epic` to `7`.
31. Say "Hail" to kithicor/"Tarnamil".
32. Spawns "Uglib Gaibido" (20293).
33. Loot "Paladin Blood Sample" (20904) from "Uglib Gaibido".
34. 2 alternative loot source(s) also yield Paladin Blood Sample (20904).
35. poknowledge/"Gilina Yilzior", hand "Gubblegrot's Head" (16793) + "Silithis's Head" (16813) + "Giligatabbus's Head" (20079) + "Skurza's Head" (20899). Requires `shadowknight_epic` ==6. Gives "Sheathed Innoruuk's Voice" (22199).
36. poknowledge/"Gilina Yilzior", hand "Paladin Blood Sample" (20904) + "Paladin Blood Sample" (20904) + "Paladin Blood Sample" (20904) + "Sheathed Innoruuk's Voice" (22199). Sets `shadowknight_epic` to `8`.
37. Loot "Sir Elmonious's Holy Symbol" (55901) from "Sir Elmonious Falmont" in `westwastes`.
38. poknowledge/"Gilina Yilzior", hand "Sir Elmonious's Holy Symbol" (55901). Requires `shadowknight_epic` ==8. Gives "Innoruuk's Voice" (50003).

### "Lhranc's Earthly Anchor" (24584)

1. dulak/"Ritald", say "Hail". Sets `shadowknight_pre` to `1`.
2. Loot "Ancient Flamberge of Hatred" (55902) from "Captain Varns" in `dulak`.
3. Loot "Essence of Hate" (21870) from "Mistress of Malevolence" in `hateplaneb`.
4. Loot "Essence of Hate" (21870) from "Overlord R'Gahbsa" in `hateplaneb`.
5. Loot "Stormborn Phylactery" (21782) from "Olidan" in `postorms`.
6. dulak/"Ritald", hand "Stormborn Phylactery" (21782) + "Essence of Hate" (21870) + "Ancient Flamberge of Hatred" (55902). Sets `shadowknight_pre` to `2`.
7. Unresolved cyclic prerequisite: `shadowknight_epic` ==1.
8. poknowledge/"Sienn Kastane", say "Hail". Sets `shadowknight_epic` to `1`.
9. Loot "Gelatinous Murkglider Egg" (55900) from "Murkglider Breeder" in `dranik`.
10. poknowledge/"Grand Librarian Maelin", hand "Gelatinous Murkglider Egg" (55900). Requires `shadowknight_epic` ==1. Gives "The Silent Gods" (20520).
11. poknowledge/"Sienn Kastane", hand "The Silent Gods" (20520). Sets `shadowknight_epic` to `2`.
12. Summon "Collapsible Sewing Kit" (17165) by casting "Unfold Sewing Kit".
13. Loot "Eye of the Dark God" (21675) from "Amygdalan warrior" (NPC 72015) in `fearplane`. Drop cache: 18.32% chance per kill.
14. Loot "Gloom Nightmare Hide" (20622) from "A Gloom Nightmare" in `ponightmare`.
15. Loot "Lock of Blessed Unicorn Hair" (21496) from "A Rolling Plains Steed" (NPC 127084) in `growthplane`. Drop cache: 11% chance per kill.
16. Combine in "Collapsible Sewing Kit" (17165): "Eye of the Dark God" (21675), "Gloom Nightmare Hide" (20622), "Lock of Blessed Unicorn Hair" (21496). Produces "Sheath of Darktidings" (20426). Requires Tailoring 100. Trivial at 15. The combine does not fail.
17. poknowledge/"Sienn Kastane", hand "Sheath of Darktidings" (20426). Sets `shadowknight_epic` to `3`.
18. Loot "Fraga's Parchment" (23492) from "Fraga" in `povalor`.
19. poknowledge/"Sienn Kastane", hand "Fraga's Parchment" (23492). Sets `shadowknight_epic` to `4`.
20. Loot "Wailing Sister Blood" (20497) from "The Wailing Sister" in `ponightmare`.
21. Loot "Wailing Rune" (19025) from "The Wailing Sister" in `ponightmare`.
22. poknowledge/"Sienn Kastane", hand "Wailing Rune" (19025) + "Wailing Sister Blood" (20497). Sets `shadowknight_epic` to `5`.
23. poknowledge/"Sienn Kastane", hand "Wailing Rune" (19025) + "Wailing Sister Blood" (20497). Requires `shadowknight_epic` ==4. Gives "Sheathed Innoruuk's Voice" (11407).
24. poknowledge/"Gilina Yilzior", hand "Sheathed Innoruuk's Voice" (11407). Sets `shadowknight_epic` to `6`.
25. Loot "Skurza's Head" (20899) from "Skurza Slicekutt" in `swampofnohope`.
26. Loot "Silithis's Head" (16813) from "Silithis Sisnta" in `timorous`.
27. Loot "Gubblegrot's Head" (16793) from "Gubblegrot Smashfist" in `oceanoftears`.
28. Loot "Gubblegrot's Head" (16793) from "Gubblegrot Smashfist" in `oot`.
29. Loot "Giligatabbus's Head" (20079) from "Giligatabbus Igglebix" in `iceclad`.
30. poknowledge/"Gilina Yilzior", hand "Gubblegrot's Head" (16793) + "Silithis's Head" (16813) + "Giligatabbus's Head" (20079) + "Skurza's Head" (20899). Sets `shadowknight_epic` to `7`.
31. Say "Hail" to kithicor/"Tarnamil".
32. Spawns "Uglib Gaibido" (20293).
33. Loot "Paladin Blood Sample" (20904) from "Uglib Gaibido".
34. 2 alternative loot source(s) also yield Paladin Blood Sample (20904).
35. poknowledge/"Gilina Yilzior", hand "Gubblegrot's Head" (16793) + "Silithis's Head" (16813) + "Giligatabbus's Head" (20079) + "Skurza's Head" (20899). Requires `shadowknight_epic` ==6. Gives "Sheathed Innoruuk's Voice" (22199).
36. poknowledge/"Gilina Yilzior", hand "Paladin Blood Sample" (20904) + "Paladin Blood Sample" (20904) + "Paladin Blood Sample" (20904) + "Sheathed Innoruuk's Voice" (22199). Sets `shadowknight_epic` to `8`.
37. Loot "Sir Elmonious's Holy Symbol" (55901) from "Sir Elmonious Falmont" in `westwastes`.
38. poknowledge/"Gilina Yilzior", hand "Sir Elmonious's Holy Symbol" (55901). Requires `shadowknight_epic` ==8. Gives "Innoruuk's Voice" (50003).
39. poknowledge/"Gilina Yilzior", say "Vision". Sets `shadowknight_epic` to `9`.
40. Loot "Kilidna's Head" (19098) from "Kilidna" in `citymist`.
41. poknowledge/"Gilina Yilzior", hand "Kilidna's Head" (19098). Sets `shadowknight_epic` to `10`.
42. Loot "Lhranc's Corroded Bracer" (24612) from "A Mortiferous Golem" in `charasis`.
43. Kill citymist/"A Black Reaver". Spawns "A Black Reaver" (90004).
44. Loot "Lhranc's Pendant" (23489) from "A Black Reaver".
45. 2 alternative loot source(s) also yield Lhranc's Pendant (23489).
46. Loot "Lhranc's Ring" (24632) from "Risen Corporal" (NPC 20107) in `kithicor`. Drop cache: 19.56% chance per kill.
47. poknowledge/"Gilina Yilzior", hand "Lhranc's Pendant" (23489) + "Lhranc's Corroded Bracer" (24612) + "Lhranc's Ring" (24632). Requires `shadowknight_epic` ==10. Gives "Lhranc's Earthly Anchor" (24584).

## `shadowknight_pre`

Values written: 1, 2.

### 1. ritald — say hail

Zone: `dulak`.

> Greetings, dark one. Do you feel it? I am sure you do. Innoruuk

Sets `shadowknight_pre` to `1`.

- Needs `shadowknight_pre` unset.
In script order:

1. Sets `shadowknight_pre` to `1`.


### 2. ritald — hand 21782+21870+55902

Zone: `dulak`.

Sets `shadowknight_pre` to `2`.

- Needs `shadowknight_pre` ==1.
- Turn in x1: Ancient Flamberge of Hatred (55902).
- Turn in x1: Essence of Hate (21870).
- Turn in x1: Stormborn Phylactery (21782).
In script order:

1. Sets `shadowknight_pre` to `2`.
2. Gives Innoruuk's Voice (22944).


How the items are reached:

- Ancient Flamberge of Hatred (55902)
  - Loot "Ancient Flamberge of Hatred" (55902) from "Captain Varns" in `dulak`.
- Essence of Hate (21870)
  - Loot "Essence of Hate" (21870) from "Mistress of Malevolence" in `hateplaneb`.
  - Loot "Essence of Hate" (21870) from "Overlord R'Gahbsa" in `hateplaneb`.
- Stormborn Phylactery (21782)
  - Loot "Stormborn Phylactery" (21782) from "Olidan" in `postorms`.

### Steps on `shadowknight_pre` that do not change it

- `poknowledge` sienn kastane, say hail needs `shadowknight_pre` ==2.
  - Sets `shadowknight_epic` to `1`.
- `poknowledge` sienn kastane, say hail needs `shadowknight_pre` ==2.
  - Sets `shadowknight_epic` to `1`.

## `shadowknight_epic`

Values written: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12.

### 1. sienn kastane — say hail

Zone: `poknowledge`.

> You. You are the one I have seen in my visions.

Sets `shadowknight_epic` to `1`.

- Needs `shadowknight_epic` unset.
- Needs `shadowknight_pre` ==2.
- Needs `shadowknight_epic` ==1.
- One of: `shadowknight_pre` ==2; Innoruuk's Curse (14383).
In script order:

1. Sets `shadowknight_epic` to `1`.


How the items are reached:

- Innoruuk's Curse (14383)
  - Prerequisite: "Innoruuk's Curse" (14383). See section 0.

This step also depends on `shadowknight_pre`, shown above.

Alternative or repeat transition to `shadowknight_epic` = `1` (not an additional required stage).

### 1. sienn kastane — hand 22944

Zone: `poknowledge`.

Sets `shadowknight_epic` to `1`.

- Needs `shadowknight_epic` unset.
- Turn in x1: Innoruuk's Voice (22944).
In script order:

1. Sets `shadowknight_epic` to `1`.


How the items are reached:

- Innoruuk's Voice (22944)
  - Prerequisite: "Innoruuk's Voice" (22944). See section 0.

### 2. sienn kastane — hand 20520

Zone: `poknowledge`.

Sets `shadowknight_epic` to `2`.

- Needs `shadowknight_epic` ==1.
- Turn in x1: The Silent Gods (20520).
In script order:

1. Sets `shadowknight_epic` to `2`.


How the items are reached:

- The Silent Gods (20520)
  - Prerequisite: "The Silent Gods" (20520). See section 0.

### 3. sienn kastane — hand 20426

Zone: `poknowledge`.

Sets `shadowknight_epic` to `3`.

- Needs `shadowknight_epic` ==2.
- Turn in x1: Sheath of Darktidings (20426).
In script order:

1. Sets `shadowknight_epic` to `3`.


How the items are reached:

- Sheath of Darktidings (20426)
  - Prerequisite: "Sheath of Darktidings" (20426). See section 0.

### 4. sienn kastane — hand 23492

Zone: `poknowledge`.

Sets `shadowknight_epic` to `4`.

- Needs `shadowknight_epic` ==3.
- Turn in x1: Fraga's Parchment (23492).
In script order:

1. Sets `shadowknight_epic` to `4`.


How the items are reached:

- Fraga's Parchment (23492)
  - Loot "Fraga's Parchment" (23492) from "Fraga" in `povalor`.

### 5. sienn kastane — hand 19025+20497

Zone: `poknowledge`.

Sets `shadowknight_epic` to `5`.

- Needs `shadowknight_epic` ==4.
- Turn in x1: Wailing Sister Blood (20497).
- Turn in x1: Wailing Rune (19025).
In script order:

1. Sets `shadowknight_epic` to `5`.
2. Gives Sheathed Innoruuk's Voice (11407).


How the items are reached:

- Wailing Sister Blood (20497)
  - Loot "Wailing Sister Blood" (20497) from "The Wailing Sister" in `ponightmare`.
- Wailing Rune (19025)
  - Loot "Wailing Rune" (19025) from "The Wailing Sister" in `ponightmare`.

### 6. gilina yilzior — hand 11407

Zone: `poknowledge`.

Sets `shadowknight_epic` to `6`.

- Needs `shadowknight_epic` ==5.
- Turn in x1: Sheathed Innoruuk's Voice (11407).
In script order:

1. Sets `shadowknight_epic` to `6`.


How the items are reached:

- Sheathed Innoruuk's Voice (11407)
  - Prerequisite: "Sheathed Innoruuk's Voice" (11407). See section 0.

### 7. gilina yilzior — hand 16793+16813+20079+20899

Zone: `poknowledge`.

Sets `shadowknight_epic` to `7`.

- Needs `shadowknight_epic` ==6.
- Turn in x1: Skurza's Head (20899).
- Turn in x1: Silithis's Head (16813).
- Turn in x1: Gubblegrot's Head (16793).
- Turn in x1: Giligatabbus's Head (20079).
In script order:

1. Sets `shadowknight_epic` to `7`.
2. Gives Sheathed Innoruuk's Voice (22199).


How the items are reached:

- Skurza's Head (20899)
  - Loot "Skurza's Head" (20899) from "Skurza Slicekutt" in `swampofnohope`.
- Silithis's Head (16813)
  - Loot "Silithis's Head" (16813) from "Silithis Sisnta" in `timorous`.
- Gubblegrot's Head (16793)
  - Loot "Gubblegrot's Head" (16793) from "Gubblegrot Smashfist" in `oceanoftears`.
  - Loot "Gubblegrot's Head" (16793) from "Gubblegrot Smashfist" in `oot`.
- Giligatabbus's Head (20079)
  - Loot "Giligatabbus's Head" (20079) from "Giligatabbus Igglebix" in `iceclad`.

### 8. gilina yilzior — hand 20904+20904+20904+22199

Zone: `poknowledge`.

Sets `shadowknight_epic` to `8`.

- Needs `shadowknight_epic` ==7.
- Turn in x1: Paladin Blood Sample (20904).
- Turn in x1: Sheathed Innoruuk's Voice (22199).
In script order:

1. Sets `shadowknight_epic` to `8`.


How the items are reached:

- Paladin Blood Sample (20904)
  - Say "Hail" to kithicor/"Tarnamil".
  - Spawns "Uglib Gaibido" (20293).
  - Loot "Paladin Blood Sample" (20904) from "Uglib Gaibido".
  - 2 alternative loot source(s) also yield Paladin Blood Sample (20904).
- Sheathed Innoruuk's Voice (22199)
  - Prerequisite: "Sheathed Innoruuk's Voice" (22199). See section 0.

### 9. gilina yilzior — say vision

Zone: `poknowledge`.

> My recent vision was of Lhranc. Perhaps you remember him, perhaps not. In any case, his spirit has returned from the dead. He now seeks revenge on those who ...

Sets `shadowknight_epic` to `9`.

- Needs Innoruuk's Voice (50003).
- Needs `shadowknight_epic` unset.
In script order:

1. Sets `shadowknight_epic` to `9`.


How the items are reached:

- Innoruuk's Voice (50003)
  - Prerequisite: "Innoruuk's Voice" (50003). See section 0.

### 10. gilina yilzior — hand 19098

Zone: `poknowledge`.

Sets `shadowknight_epic` to `10`.

- Needs `shadowknight_epic` ==9.
- Turn in x1: Kilidna's Head (19098).
In script order:

1. Sets `shadowknight_epic` to `10`.


How the items are reached:

- Kilidna's Head (19098)
  - Loot "Kilidna's Head" (19098) from "Kilidna" in `citymist`.

### 11. filligno the slayer — hand 24584+47100

Zone: `dranik`.

Sets `shadowknight_epic` to `11`.

- Needs `shadowknight_epic` ==10.
- Turn in x1: Lhranc's Earthly Anchor (24584).
- Turn in x1: Globe of Discordant Energy (47100).
In script order:

1. Sets `shadowknight_epic` to `11`.


How the items are reached:

- Lhranc's Earthly Anchor (24584)
  - Prerequisite: "Lhranc's Earthly Anchor" (24584). See section 0.
- Globe of Discordant Energy (47100)
  - Say "Check Lorb" to anguish/"Zone Status".
  - Spawns "Orb of Discordant Energy" (317087).
  - Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy".
  - 4 alternative loot source(s) also yield Globe of Discordant Energy (47100).

### 12. filligno the slayer — hand 50003+55903

Zone: `dranik`.

Sets `shadowknight_epic` to `12`.

- Needs `shadowknight_epic` ==11.
- Turn in x1: Essence of the Shadowknight (55903).
- Turn in x1: Innoruuk's Voice (50003).
In script order:

1. Sets `shadowknight_epic` to `12`.
2. Gives Innoruuk's Dark Blessing (48136).


How the items are reached:

- Essence of the Shadowknight (55903)
  - Spawns "Lhranc" (336250) in `dranik` on event_signal.
  - Loot "Essence of the Shadowknight" (55903) from "Lhranc".
- Innoruuk's Voice (50003)
  - Prerequisite: "Innoruuk's Voice" (50003). See section 0.

### Steps on `shadowknight_epic` that do not change it

- `dranik` filligno the slayer, say ready needs `shadowknight_epic` ==11.
  - Spawns a Minion of Lhranc (336251).
- `dranik` player, on loot needs `shadowknight_epic` ==11.
  - Sets `warrior_epic_dranik` to `1`.
  - Spawns a chest (Epic 1.5) (283157).
  - Sets `beast_epic_dran` to `1`.
  - Sets `druid_chest_dranik` to `1`.
  - Sets `shaman_chest_dranik` to `1`.
  - Spawns a chest (Epic 2.0) (893).
  - Sets `nec_chest_dranik` to `1`.
  - Sets `sk_chest_dranik` to `1`.
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
- `kithicor` tarnamil, say hail needs `shadowknight_epic` ==7.
  - Spawns Uglib Gaibido (20293).
  - Spawns Xotmidd Ferlop (20294).
  - Spawns Jarnig Kilanid (20295).
  - Spawns Tilminos Farondi (20298).
  - Spawns Shressa Farondi (20297).
  - Spawns Valinda Ergington (20296).
  - Loots Two Handed Sword (5005).
  - Loots Paladin Blood Sample (20904).
  - Loots Two Handed Sword (5005).
  - Loots Uncut Alexandrite (37847).
  - Loots Uncut Jacinth (37850).
  - Loots Two Handed Sword (5005).
  - Loots Round Shield (9002).
  - Loots Sunshard Ore (33792).
  - Loots Two Handed Sword (5005).
  - Loots Paladin Blood Sample (20904).
  - Loots Two Handed Sword (5005).
  - Loots Sunshard Ore (33792).
  - Loots Two Handed Sword (5005).
  - Loots Round Shield (9002).
  - Loots Paladin Blood Sample (20904).
  - Loots Sunshard Ore (33792).
- `poknowledge` gilina yilzior, hand 23489+24612+24632 needs `shadowknight_epic` ==10.
  - Turn in Lhranc's Corroded Bracer (24612).
  - Turn in Lhranc's Pendant (23489).
  - Turn in Lhranc's Ring (24632).
  - Gives Lhranc's Earthly Anchor (24584).
- `poknowledge` gilina yilzior, hand 55901 needs `shadowknight_epic` ==8.
  - Turn in Sir Elmonious's Holy Symbol (55901).
  - Gives Innoruuk's Voice (50003).
- `poknowledge` grand librarian maelin, hand 55900 needs `shadowknight_epic` ==1.
  - Turn in Gelatinous Murkglider Egg (55900).
  - Gives The Silent Gods (20520).
- `westwastes` player, on loot needs `shadowknight_epic` ==8.
  - Sets `sk_westwastes` to `1`.
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

- `sk_chest_dranik` set to 1 at dranik/player.
- `sk_westwastes` set to 1 at westwastes/player.
