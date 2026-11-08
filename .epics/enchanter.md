# Enchanter

Steps taken from the quest graph only. **Broken** means the graph has no edge for that value or that item.

Flags with writes: `EnchPre`, `ench_epic`.

## 0. Prerequisites

Each list is the order you obtain that item. Later steps point here instead of repeating the chain.

### "Illegible Tome" (52947)

1. Hand "Dragon Boneshard" (65574) to veksar/"Spirit Of Garudon". Spawns "Garudon" (109107). Loot "Garudon's Statue" (52941) from "Garudon".
2. Loot "Garudon's Statue" (52941) from "Garudon".
3. lakeofillomen/"A Bloodgill Mimic", hand "Garudon's Statue" (52941). Sets `EnchPre` to `1`.
4. Loot "Crumbling Tome" (54313) from "A Shissar Lorekeeper" in `ssratemple`.
5. ssratemple/"A Soriz Imitator", hand "Crumbling Tome" (54313). Requires `EnchPre` ==1. Gives "Illegible Tome" (52947).

### "Gnomish Translating Device" (52945)

1. Hand "Dragon Boneshard" (65574) to veksar/"Spirit Of Garudon". Spawns "Garudon" (109107). Loot "Garudon's Statue" (52941) from "Garudon".
2. Loot "Garudon's Statue" (52941) from "Garudon".
3. lakeofillomen/"A Bloodgill Mimic", hand "Garudon's Statue" (52941). Sets `EnchPre` to `1`.
4. Loot "Crumbling Tome" (54313) from "A Shissar Lorekeeper" in `ssratemple`.
5. ssratemple/"A Soriz Imitator", hand "Crumbling Tome" (54313). Requires `EnchPre` ==1. Gives "Illegible Tome" (52947).
6. akanon/"Rilgor Plegnog", say "Insidious". Gives "Compacting Satchel" (54303).
7. No quest step gives Fine Insidious Halo (54384). The dump lists it in hateplaneb.
8. No quest step gives Fine Insidious Sleeves (54385). The dump lists it in hateplaneb.
9. No quest step gives Fine Insidious Manacle (54386). The dump lists it in hateplaneb.
10. No quest step gives Fine Insidious Gloves (54387). The dump lists it in hateplaneb.
11. No quest step gives Fine Insidious Pantaloons (54388). The dump lists it in hateplaneb.
12. No quest step gives Fine Insidious Slippers (54389). The dump lists it in hateplaneb.
13. Combine in "Compacting Satchel" (54303): "Fine Insidious Halo" (54384), "Fine Insidious Sleeves" (54385), "Fine Insidious Manacle" (54386), "Fine Insidious Gloves" (54387), "Fine Insidious Pantaloons" (54388), "Fine Insidious Slippers" (54389). Produces "Insidious Bundle" (54317). The combine does not fail.
14. akanon/"Rilgor Plegnog", hand "Insidious Bundle" (54317). Gives "Gnomish Translating Device" (52945).

### "Staff of the Serpent" (10650)

1. Common item: Shining Metallic Robes (1360). Listed in 4 zones.
2. akanon/"Rilgor Plegnog", hand "Shining Metallic Robes" (1360). Gives "Mechanical Pen" (10600).
3. qcat/"Reania Jukle", say "Supply". Gives "Empty Ink Vial" (10626).
4. gukbottom/"A Ghoul Scribe", hand "Empty Ink Vial" (10626). Gives "Ink of the Dark" (10601).
5. Hand "Quill" (13051) + "Piece of Parchment" (13063) to qey2hh1/"Chrislin Baker". Spawns "Thrackin Griften" (12172). Loot "White Paper" (10602) from "Thrackin Griften".
6. Loot "White Paper" (10602) from "Thrackin Griften".
7. erudnext/"Stofo Olan", hand "Mechanical Pen" (10600) + "Ink of the Dark" (10601) + "White Paper" (10602). Gives "Copy of Notes" (10603).
8. burningwood/"A Sarnak Imitator", hand "Copy of Notes" (10603). Gives "Jeb's Seal" (10604).
9. akanon/"Clockwork Viix", hand "Jeb's Seal" (10604). Gives "Enchanters Sack" (17861).
10. firiona/"Nadia Starfeast", say "I Need A Sack". Gives "Enchanters Sack" (17861).
11. hole/"Polzin Mrid", hand "Jeb's Seal" (10604). Gives "Enchanters Sack" (17861).
12. overthere/"Modani Qu-Loni", hand "Jeb's Seal" (10604). Gives "Enchanters Sack" (17861).
13. Loot "Xolion Rod" (10606) from "Vessel Drozlin" in `cabeast`.
14. Loot "Innoruuk's Word" (10607) from "Verina Tomb" in `neriakc`.
15. Loot "Head of a Prince" (10627) from "Prince Selrach Di'zok" in `chardok`.
16. felwitheb/"Joren Nobleheart", hand "Head of a Prince" (10627). Gives "Chalice of Kings" (10608).
17. Ground spawn of "Large Muddy Sandals" (10628) in `oggok`.
18. oggok/"Bozlum Blossom", hand "Large Muddy Sandals" (10628). Gives "Scribbled Parchment" (10629).
19. oggok/"Brokk Boxtripper", hand "Scribbled Parchment" (10629). Gives "Gift to Bozlum" (10630).
20. oggok/"Bozlum Blossom", hand "Gift to Bozlum" (10630). Gives "Snow Blossoms" (10609).
21. Combine in "Enchanters Sack" (17861): "Xolion Rod" (10606), "Innoruuk's Word" (10607), "Chalice of Kings" (10608), "Snow Blossoms" (10609). Produces "Sack For Modani" (10635). The combine does not fail.
22. overthere/"Modani Qu-Loni", hand "Sack For Modani" (10635). Gives "1st Piece of Staff" (10610).
23. Loot "Spoon" (10614) from "Cazel" in `oasis`.
24. Loot "Spoon" (10614) from "Cazel" in `southro`.
25. Ground spawn of "The One Key" (10615) in `overthere`.
26. Ground spawn of "Lost Scroll" (10616) in `dalnir`.
27. Ground spawn of "Charm and Sacrifice" (10617) in `airplane`.
28. Combine in "Enchanters Sack" (17861): "Spoon" (10614), "The One Key" (10615), "Lost Scroll" (10616), "Charm and Sacrifice" (10617). Produces "Sack For Mizzle" (10636). The combine does not fail.
29. akanon/"Clockwork Viix", hand "Sack For Mizzle" (10636). Gives "2nd Piece of Staff" (10611).
30. firiona/"Nadia Starfeast", say "Diamond". Gives "Dull Diamond" (10631).
31. kaesora/"Spectral Librarian", hand "Dull Diamond" (10631). Gives "Enchanted Diamond" (10618).
32. firiona/"Nadia Starfeast", say "Sapphire". Gives "Dull Sapphire" (10632).
33. skyfire/"Felia Goldenwing", hand "Dull Sapphire" (10632). Gives "Enchanted Sapphire" (10619).
34. firiona/"Nadia Starfeast", say "Ruby". Gives "Dull Ruby" (10633).
35. citymist/"Wraith Of Jaxion", hand "Dull Ruby" (10633). Gives "Enchanted Ruby" (10620).
36. firiona/"Nadia Starfeast", say "Emerald". Gives "Dull Emerald" (10634).
37. overthere/"Impaler Tzilug", hand "Dull Emerald" (10634). Gives "Enchanted Emerald" (10621).
38. Combine in "Enchanters Sack" (17861): "Enchanted Diamond" (10618), "Enchanted Sapphire" (10619), "Enchanted Ruby" (10620), "Enchanted Emerald" (10621). Produces "Sack For Nadia" (10637). The combine does not fail.
39. firiona/"Nadia Starfeast", hand "Sack For Nadia" (10637). Gives "3rd Piece of Staff" (10612).
40. Loot "Head of the Serpent" (10622) from "Wraith of a Shissar" in `fearplane`.
41. Loot "Essence of a Ghost" (10623) from "the Ghost of Kindle" in `hole`.
42. No quest step gives Essence of a Vampire (10624). The dump lists it in hateplane, hateplaneb.
43. Loot "Sands of the Mystics" (10625) from "The Tangrin" in `fieldofbone`.
44. Combine in "Enchanters Sack" (17861): "Head of the Serpent" (10622), "Essence of a Ghost" (10623), "Essence of a Vampire" (10624), "Sands of the Mystics" (10625). Produces "Sack For Polzin" (10638). The combine does not fail.
45. hole/"Polzin Mrid", hand "Sack For Polzin" (10638). Gives "4th Piece of Staff" (10613).
46. Combine in "Enchanters Sack" (17861): "1st Piece of Staff" (10610), "2nd Piece of Staff" (10611), "3rd Piece of Staff" (10612), "4th Piece of Staff" (10613). Produces "Bundle of Staves" (10639). The combine does not fail.
47. burningwood/"A Sarnak Imitator", hand "Bundle of Staves" (10639). Gives "Staff of the Serpent" (10650).

### "Complete Illegible Tome" (54267)

1. Hand "Dragon Boneshard" (65574) to veksar/"Spirit Of Garudon". Spawns "Garudon" (109107). Loot "Garudon's Statue" (52941) from "Garudon".
2. Loot "Garudon's Statue" (52941) from "Garudon".
3. lakeofillomen/"A Bloodgill Mimic", hand "Garudon's Statue" (52941). Sets `EnchPre` to `1`.
4. Loot "Crumbling Tome" (54313) from "A Shissar Lorekeeper" in `ssratemple`.
5. ssratemple/"A Soriz Imitator", hand "Crumbling Tome" (54313). Requires `EnchPre` ==1. Gives "Illegible Tome" (52947).
6. akanon/"Rilgor Plegnog", say "Insidious". Gives "Compacting Satchel" (54303).
7. No quest step gives Fine Insidious Halo (54384). The dump lists it in hateplaneb.
8. No quest step gives Fine Insidious Sleeves (54385). The dump lists it in hateplaneb.
9. No quest step gives Fine Insidious Manacle (54386). The dump lists it in hateplaneb.
10. No quest step gives Fine Insidious Gloves (54387). The dump lists it in hateplaneb.
11. No quest step gives Fine Insidious Pantaloons (54388). The dump lists it in hateplaneb.
12. No quest step gives Fine Insidious Slippers (54389). The dump lists it in hateplaneb.
13. Combine in "Compacting Satchel" (54303): "Fine Insidious Halo" (54384), "Fine Insidious Sleeves" (54385), "Fine Insidious Manacle" (54386), "Fine Insidious Gloves" (54387), "Fine Insidious Pantaloons" (54388), "Fine Insidious Slippers" (54389). Produces "Insidious Bundle" (54317). The combine does not fail.
14. akanon/"Rilgor Plegnog", hand "Insidious Bundle" (54317). Gives "Gnomish Translating Device" (52945).
15. burningwood/"A Sarnak Imitator", hand "Gnomish Translating Device" (52945) + "Illegible Tome" (52947). Sets `EnchPre` to `2`.
16. Common item: Shining Metallic Robes (1360). Listed in 4 zones.
17. akanon/"Rilgor Plegnog", hand "Shining Metallic Robes" (1360). Gives "Mechanical Pen" (10600).
18. qcat/"Reania Jukle", say "Supply". Gives "Empty Ink Vial" (10626).
19. gukbottom/"A Ghoul Scribe", hand "Empty Ink Vial" (10626). Gives "Ink of the Dark" (10601).
20. Hand "Quill" (13051) + "Piece of Parchment" (13063) to qey2hh1/"Chrislin Baker". Spawns "Thrackin Griften" (12172). Loot "White Paper" (10602) from "Thrackin Griften".
21. Loot "White Paper" (10602) from "Thrackin Griften".
22. erudnext/"Stofo Olan", hand "Mechanical Pen" (10600) + "Ink of the Dark" (10601) + "White Paper" (10602). Gives "Copy of Notes" (10603).
23. burningwood/"A Sarnak Imitator", hand "Copy of Notes" (10603). Gives "Jeb's Seal" (10604).
24. akanon/"Clockwork Viix", hand "Jeb's Seal" (10604). Gives "Enchanters Sack" (17861).
25. firiona/"Nadia Starfeast", say "I Need A Sack". Gives "Enchanters Sack" (17861).
26. hole/"Polzin Mrid", hand "Jeb's Seal" (10604). Gives "Enchanters Sack" (17861).
27. overthere/"Modani Qu-Loni", hand "Jeb's Seal" (10604). Gives "Enchanters Sack" (17861).
28. Loot "Xolion Rod" (10606) from "Vessel Drozlin" in `cabeast`.
29. Loot "Innoruuk's Word" (10607) from "Verina Tomb" in `neriakc`.
30. Loot "Head of a Prince" (10627) from "Prince Selrach Di'zok" in `chardok`.
31. felwitheb/"Joren Nobleheart", hand "Head of a Prince" (10627). Gives "Chalice of Kings" (10608).
32. Ground spawn of "Large Muddy Sandals" (10628) in `oggok`.
33. oggok/"Bozlum Blossom", hand "Large Muddy Sandals" (10628). Gives "Scribbled Parchment" (10629).
34. oggok/"Brokk Boxtripper", hand "Scribbled Parchment" (10629). Gives "Gift to Bozlum" (10630).
35. oggok/"Bozlum Blossom", hand "Gift to Bozlum" (10630). Gives "Snow Blossoms" (10609).
36. Combine in "Enchanters Sack" (17861): "Xolion Rod" (10606), "Innoruuk's Word" (10607), "Chalice of Kings" (10608), "Snow Blossoms" (10609). Produces "Sack For Modani" (10635). The combine does not fail.
37. overthere/"Modani Qu-Loni", hand "Sack For Modani" (10635). Gives "1st Piece of Staff" (10610).
38. Loot "Spoon" (10614) from "Cazel" in `oasis`.
39. Loot "Spoon" (10614) from "Cazel" in `southro`.
40. Ground spawn of "The One Key" (10615) in `overthere`.
41. Ground spawn of "Lost Scroll" (10616) in `dalnir`.
42. Ground spawn of "Charm and Sacrifice" (10617) in `airplane`.
43. Combine in "Enchanters Sack" (17861): "Spoon" (10614), "The One Key" (10615), "Lost Scroll" (10616), "Charm and Sacrifice" (10617). Produces "Sack For Mizzle" (10636). The combine does not fail.
44. akanon/"Clockwork Viix", hand "Sack For Mizzle" (10636). Gives "2nd Piece of Staff" (10611).
45. firiona/"Nadia Starfeast", say "Diamond". Gives "Dull Diamond" (10631).
46. kaesora/"Spectral Librarian", hand "Dull Diamond" (10631). Gives "Enchanted Diamond" (10618).
47. firiona/"Nadia Starfeast", say "Sapphire". Gives "Dull Sapphire" (10632).
48. skyfire/"Felia Goldenwing", hand "Dull Sapphire" (10632). Gives "Enchanted Sapphire" (10619).
49. firiona/"Nadia Starfeast", say "Ruby". Gives "Dull Ruby" (10633).
50. citymist/"Wraith Of Jaxion", hand "Dull Ruby" (10633). Gives "Enchanted Ruby" (10620).
51. firiona/"Nadia Starfeast", say "Emerald". Gives "Dull Emerald" (10634).
52. overthere/"Impaler Tzilug", hand "Dull Emerald" (10634). Gives "Enchanted Emerald" (10621).
53. Combine in "Enchanters Sack" (17861): "Enchanted Diamond" (10618), "Enchanted Sapphire" (10619), "Enchanted Ruby" (10620), "Enchanted Emerald" (10621). Produces "Sack For Nadia" (10637). The combine does not fail.
54. firiona/"Nadia Starfeast", hand "Sack For Nadia" (10637). Gives "3rd Piece of Staff" (10612).
55. Loot "Head of the Serpent" (10622) from "Wraith of a Shissar" in `fearplane`.
56. Loot "Essence of a Ghost" (10623) from "the Ghost of Kindle" in `hole`.
57. No quest step gives Essence of a Vampire (10624). The dump lists it in hateplane, hateplaneb.
58. Loot "Sands of the Mystics" (10625) from "The Tangrin" in `fieldofbone`.
59. Combine in "Enchanters Sack" (17861): "Head of the Serpent" (10622), "Essence of a Ghost" (10623), "Essence of a Vampire" (10624), "Sands of the Mystics" (10625). Produces "Sack For Polzin" (10638). The combine does not fail.
60. hole/"Polzin Mrid", hand "Sack For Polzin" (10638). Gives "4th Piece of Staff" (10613).
61. Combine in "Enchanters Sack" (17861): "1st Piece of Staff" (10610), "2nd Piece of Staff" (10611), "3rd Piece of Staff" (10612), "4th Piece of Staff" (10613). Produces "Bundle of Staves" (10639). The combine does not fail.
62. burningwood/"A Sarnak Imitator", hand "Bundle of Staves" (10639). Gives "Staff of the Serpent" (10650).
63. burningwood/"A Sarnak Imitator", say "Hail". Sets `ench_epic` to `1`.
64. burningwood/"A Sarnak Imitator", say "Hail". Sets `ench_epic` to `1`.
65. burningwood/"A Sarnak Imitator", say "Prepared". Requires `ench_epic` set. Requires `ench_epic` >=1. Gives "Tattered Illegible Tome" (57918).
66. Ground spawn of "Cryptic Page" (52933) in `charasis`.
67. Ground spawn of "Cryptic Page" (52934) in `sebilis`.
68. Ground spawn of "Cryptic Page" (52935) in `cazicthule`.
69. Ground spawn of "Cryptic Page" (52936) in `crystal`.
70. Ground spawn of "Cryptic Page" (52937) in `skyshrine`.
71. Ground spawn of "Cryptic Page" (52938) in `velketor`.
72. Ground spawn of "Cryptic Page" (52939) in `nadox`.
73. Ground spawn of "Cryptic Page" (54308) in `najena`.
74. Ground spawn of "Cryptic Page" (57916) in `fungusgrove`.
75. Ground spawn of "Cryptic Page" (57923) in `oot`.
76. Combine in "Tattered Illegible Tome" (57918): "Cryptic Page" (52933), "Cryptic Page" (52934), "Cryptic Page" (52935), "Cryptic Page" (52936), "Cryptic Page" (52937), "Cryptic Page" (52938), "Cryptic Page" (52939), "Cryptic Page" (54308), "Cryptic Page" (57916), "Cryptic Page" (57923). Produces "Complete Illegible Tome" (54267). The combine does not fail.

### "Sealed Documents" (52959)

1. Hand "Dragon Boneshard" (65574) to veksar/"Spirit Of Garudon". Spawns "Garudon" (109107). Loot "Garudon's Statue" (52941) from "Garudon".
2. Loot "Garudon's Statue" (52941) from "Garudon".
3. lakeofillomen/"A Bloodgill Mimic", hand "Garudon's Statue" (52941). Sets `EnchPre` to `1`.
4. Loot "Crumbling Tome" (54313) from "A Shissar Lorekeeper" in `ssratemple`.
5. ssratemple/"A Soriz Imitator", hand "Crumbling Tome" (54313). Requires `EnchPre` ==1. Gives "Illegible Tome" (52947).
6. akanon/"Rilgor Plegnog", say "Insidious". Gives "Compacting Satchel" (54303).
7. No quest step gives Fine Insidious Halo (54384). The dump lists it in hateplaneb.
8. No quest step gives Fine Insidious Sleeves (54385). The dump lists it in hateplaneb.
9. No quest step gives Fine Insidious Manacle (54386). The dump lists it in hateplaneb.
10. No quest step gives Fine Insidious Gloves (54387). The dump lists it in hateplaneb.
11. No quest step gives Fine Insidious Pantaloons (54388). The dump lists it in hateplaneb.
12. No quest step gives Fine Insidious Slippers (54389). The dump lists it in hateplaneb.
13. Combine in "Compacting Satchel" (54303): "Fine Insidious Halo" (54384), "Fine Insidious Sleeves" (54385), "Fine Insidious Manacle" (54386), "Fine Insidious Gloves" (54387), "Fine Insidious Pantaloons" (54388), "Fine Insidious Slippers" (54389). Produces "Insidious Bundle" (54317). The combine does not fail.
14. akanon/"Rilgor Plegnog", hand "Insidious Bundle" (54317). Gives "Gnomish Translating Device" (52945).
15. burningwood/"A Sarnak Imitator", hand "Gnomish Translating Device" (52945) + "Illegible Tome" (52947). Sets `EnchPre` to `2`.
16. Common item: Shining Metallic Robes (1360). Listed in 4 zones.
17. akanon/"Rilgor Plegnog", hand "Shining Metallic Robes" (1360). Gives "Mechanical Pen" (10600).
18. qcat/"Reania Jukle", say "Supply". Gives "Empty Ink Vial" (10626).
19. gukbottom/"A Ghoul Scribe", hand "Empty Ink Vial" (10626). Gives "Ink of the Dark" (10601).
20. Hand "Quill" (13051) + "Piece of Parchment" (13063) to qey2hh1/"Chrislin Baker". Spawns "Thrackin Griften" (12172). Loot "White Paper" (10602) from "Thrackin Griften".
21. Loot "White Paper" (10602) from "Thrackin Griften".
22. erudnext/"Stofo Olan", hand "Mechanical Pen" (10600) + "Ink of the Dark" (10601) + "White Paper" (10602). Gives "Copy of Notes" (10603).
23. burningwood/"A Sarnak Imitator", hand "Copy of Notes" (10603). Gives "Jeb's Seal" (10604).
24. akanon/"Clockwork Viix", hand "Jeb's Seal" (10604). Gives "Enchanters Sack" (17861).
25. firiona/"Nadia Starfeast", say "I Need A Sack". Gives "Enchanters Sack" (17861).
26. hole/"Polzin Mrid", hand "Jeb's Seal" (10604). Gives "Enchanters Sack" (17861).
27. overthere/"Modani Qu-Loni", hand "Jeb's Seal" (10604). Gives "Enchanters Sack" (17861).
28. Loot "Xolion Rod" (10606) from "Vessel Drozlin" in `cabeast`.
29. Loot "Innoruuk's Word" (10607) from "Verina Tomb" in `neriakc`.
30. Loot "Head of a Prince" (10627) from "Prince Selrach Di'zok" in `chardok`.
31. felwitheb/"Joren Nobleheart", hand "Head of a Prince" (10627). Gives "Chalice of Kings" (10608).
32. Ground spawn of "Large Muddy Sandals" (10628) in `oggok`.
33. oggok/"Bozlum Blossom", hand "Large Muddy Sandals" (10628). Gives "Scribbled Parchment" (10629).
34. oggok/"Brokk Boxtripper", hand "Scribbled Parchment" (10629). Gives "Gift to Bozlum" (10630).
35. oggok/"Bozlum Blossom", hand "Gift to Bozlum" (10630). Gives "Snow Blossoms" (10609).
36. Combine in "Enchanters Sack" (17861): "Xolion Rod" (10606), "Innoruuk's Word" (10607), "Chalice of Kings" (10608), "Snow Blossoms" (10609). Produces "Sack For Modani" (10635). The combine does not fail.
37. overthere/"Modani Qu-Loni", hand "Sack For Modani" (10635). Gives "1st Piece of Staff" (10610).
38. Loot "Spoon" (10614) from "Cazel" in `oasis`.
39. Loot "Spoon" (10614) from "Cazel" in `southro`.
40. Ground spawn of "The One Key" (10615) in `overthere`.
41. Ground spawn of "Lost Scroll" (10616) in `dalnir`.
42. Ground spawn of "Charm and Sacrifice" (10617) in `airplane`.
43. Combine in "Enchanters Sack" (17861): "Spoon" (10614), "The One Key" (10615), "Lost Scroll" (10616), "Charm and Sacrifice" (10617). Produces "Sack For Mizzle" (10636). The combine does not fail.
44. akanon/"Clockwork Viix", hand "Sack For Mizzle" (10636). Gives "2nd Piece of Staff" (10611).
45. firiona/"Nadia Starfeast", say "Diamond". Gives "Dull Diamond" (10631).
46. kaesora/"Spectral Librarian", hand "Dull Diamond" (10631). Gives "Enchanted Diamond" (10618).
47. firiona/"Nadia Starfeast", say "Sapphire". Gives "Dull Sapphire" (10632).
48. skyfire/"Felia Goldenwing", hand "Dull Sapphire" (10632). Gives "Enchanted Sapphire" (10619).
49. firiona/"Nadia Starfeast", say "Ruby". Gives "Dull Ruby" (10633).
50. citymist/"Wraith Of Jaxion", hand "Dull Ruby" (10633). Gives "Enchanted Ruby" (10620).
51. firiona/"Nadia Starfeast", say "Emerald". Gives "Dull Emerald" (10634).
52. overthere/"Impaler Tzilug", hand "Dull Emerald" (10634). Gives "Enchanted Emerald" (10621).
53. Combine in "Enchanters Sack" (17861): "Enchanted Diamond" (10618), "Enchanted Sapphire" (10619), "Enchanted Ruby" (10620), "Enchanted Emerald" (10621). Produces "Sack For Nadia" (10637). The combine does not fail.
54. firiona/"Nadia Starfeast", hand "Sack For Nadia" (10637). Gives "3rd Piece of Staff" (10612).
55. Loot "Head of the Serpent" (10622) from "Wraith of a Shissar" in `fearplane`.
56. Loot "Essence of a Ghost" (10623) from "the Ghost of Kindle" in `hole`.
57. No quest step gives Essence of a Vampire (10624). The dump lists it in hateplane, hateplaneb.
58. Loot "Sands of the Mystics" (10625) from "The Tangrin" in `fieldofbone`.
59. Combine in "Enchanters Sack" (17861): "Head of the Serpent" (10622), "Essence of a Ghost" (10623), "Essence of a Vampire" (10624), "Sands of the Mystics" (10625). Produces "Sack For Polzin" (10638). The combine does not fail.
60. hole/"Polzin Mrid", hand "Sack For Polzin" (10638). Gives "4th Piece of Staff" (10613).
61. Combine in "Enchanters Sack" (17861): "1st Piece of Staff" (10610), "2nd Piece of Staff" (10611), "3rd Piece of Staff" (10612), "4th Piece of Staff" (10613). Produces "Bundle of Staves" (10639). The combine does not fail.
62. burningwood/"A Sarnak Imitator", hand "Bundle of Staves" (10639). Gives "Staff of the Serpent" (10650).
63. burningwood/"A Sarnak Imitator", say "Hail". Sets `ench_epic` to `1`.
64. burningwood/"A Sarnak Imitator", say "Hail". Sets `ench_epic` to `1`.
65. burningwood/"A Sarnak Imitator", say "Prepared". Requires `ench_epic` set. Requires `ench_epic` >=1. Gives "Tattered Illegible Tome" (57918).
66. Ground spawn of "Cryptic Page" (52933) in `charasis`.
67. Ground spawn of "Cryptic Page" (52934) in `sebilis`.
68. Ground spawn of "Cryptic Page" (52935) in `cazicthule`.
69. Ground spawn of "Cryptic Page" (52936) in `crystal`.
70. Ground spawn of "Cryptic Page" (52937) in `skyshrine`.
71. Ground spawn of "Cryptic Page" (52938) in `velketor`.
72. Ground spawn of "Cryptic Page" (52939) in `nadox`.
73. Ground spawn of "Cryptic Page" (54308) in `najena`.
74. Ground spawn of "Cryptic Page" (57916) in `fungusgrove`.
75. Ground spawn of "Cryptic Page" (57923) in `oot`.
76. Combine in "Tattered Illegible Tome" (57918): "Cryptic Page" (52933), "Cryptic Page" (52934), "Cryptic Page" (52935), "Cryptic Page" (52936), "Cryptic Page" (52937), "Cryptic Page" (52938), "Cryptic Page" (52939), "Cryptic Page" (54308), "Cryptic Page" (57916), "Cryptic Page" (57923). Produces "Complete Illegible Tome" (54267). The combine does not fail.
77. burningwood/"A Sarnak Imitator", hand "Complete Illegible Tome" (54267). Sets `ench_epic` to `2`.
78. poknowledge/"Grand Librarian Maelin", say "Jeb Lumsed Sent Me". Requires `ench_epic` ==2. Gives "Note to Lobaen" (52950).
79. poknowledge/"Illusionist Lobaen", hand "Note to Lobaen" (52950). Gives "Sealed Documents" (52959).

### "Latched Ornate Chest" (52966)

1. Hand "Dragon Boneshard" (65574) to veksar/"Spirit Of Garudon". Spawns "Garudon" (109107). Loot "Garudon's Statue" (52941) from "Garudon".
2. Loot "Garudon's Statue" (52941) from "Garudon".
3. lakeofillomen/"A Bloodgill Mimic", hand "Garudon's Statue" (52941). Sets `EnchPre` to `1`.
4. Loot "Crumbling Tome" (54313) from "A Shissar Lorekeeper" in `ssratemple`.
5. ssratemple/"A Soriz Imitator", hand "Crumbling Tome" (54313). Requires `EnchPre` ==1. Gives "Illegible Tome" (52947).
6. akanon/"Rilgor Plegnog", say "Insidious". Gives "Compacting Satchel" (54303).
7. No quest step gives Fine Insidious Halo (54384). The dump lists it in hateplaneb.
8. No quest step gives Fine Insidious Sleeves (54385). The dump lists it in hateplaneb.
9. No quest step gives Fine Insidious Manacle (54386). The dump lists it in hateplaneb.
10. No quest step gives Fine Insidious Gloves (54387). The dump lists it in hateplaneb.
11. No quest step gives Fine Insidious Pantaloons (54388). The dump lists it in hateplaneb.
12. No quest step gives Fine Insidious Slippers (54389). The dump lists it in hateplaneb.
13. Combine in "Compacting Satchel" (54303): "Fine Insidious Halo" (54384), "Fine Insidious Sleeves" (54385), "Fine Insidious Manacle" (54386), "Fine Insidious Gloves" (54387), "Fine Insidious Pantaloons" (54388), "Fine Insidious Slippers" (54389). Produces "Insidious Bundle" (54317). The combine does not fail.
14. akanon/"Rilgor Plegnog", hand "Insidious Bundle" (54317). Gives "Gnomish Translating Device" (52945).
15. burningwood/"A Sarnak Imitator", hand "Gnomish Translating Device" (52945) + "Illegible Tome" (52947). Sets `EnchPre` to `2`.
16. Common item: Shining Metallic Robes (1360). Listed in 4 zones.
17. akanon/"Rilgor Plegnog", hand "Shining Metallic Robes" (1360). Gives "Mechanical Pen" (10600).
18. qcat/"Reania Jukle", say "Supply". Gives "Empty Ink Vial" (10626).
19. gukbottom/"A Ghoul Scribe", hand "Empty Ink Vial" (10626). Gives "Ink of the Dark" (10601).
20. Hand "Quill" (13051) + "Piece of Parchment" (13063) to qey2hh1/"Chrislin Baker". Spawns "Thrackin Griften" (12172). Loot "White Paper" (10602) from "Thrackin Griften".
21. Loot "White Paper" (10602) from "Thrackin Griften".
22. erudnext/"Stofo Olan", hand "Mechanical Pen" (10600) + "Ink of the Dark" (10601) + "White Paper" (10602). Gives "Copy of Notes" (10603).
23. burningwood/"A Sarnak Imitator", hand "Copy of Notes" (10603). Gives "Jeb's Seal" (10604).
24. akanon/"Clockwork Viix", hand "Jeb's Seal" (10604). Gives "Enchanters Sack" (17861).
25. firiona/"Nadia Starfeast", say "I Need A Sack". Gives "Enchanters Sack" (17861).
26. hole/"Polzin Mrid", hand "Jeb's Seal" (10604). Gives "Enchanters Sack" (17861).
27. overthere/"Modani Qu-Loni", hand "Jeb's Seal" (10604). Gives "Enchanters Sack" (17861).
28. Loot "Xolion Rod" (10606) from "Vessel Drozlin" in `cabeast`.
29. Loot "Innoruuk's Word" (10607) from "Verina Tomb" in `neriakc`.
30. Loot "Head of a Prince" (10627) from "Prince Selrach Di'zok" in `chardok`.
31. felwitheb/"Joren Nobleheart", hand "Head of a Prince" (10627). Gives "Chalice of Kings" (10608).
32. Ground spawn of "Large Muddy Sandals" (10628) in `oggok`.
33. oggok/"Bozlum Blossom", hand "Large Muddy Sandals" (10628). Gives "Scribbled Parchment" (10629).
34. oggok/"Brokk Boxtripper", hand "Scribbled Parchment" (10629). Gives "Gift to Bozlum" (10630).
35. oggok/"Bozlum Blossom", hand "Gift to Bozlum" (10630). Gives "Snow Blossoms" (10609).
36. Combine in "Enchanters Sack" (17861): "Xolion Rod" (10606), "Innoruuk's Word" (10607), "Chalice of Kings" (10608), "Snow Blossoms" (10609). Produces "Sack For Modani" (10635). The combine does not fail.
37. overthere/"Modani Qu-Loni", hand "Sack For Modani" (10635). Gives "1st Piece of Staff" (10610).
38. Loot "Spoon" (10614) from "Cazel" in `oasis`.
39. Loot "Spoon" (10614) from "Cazel" in `southro`.
40. Ground spawn of "The One Key" (10615) in `overthere`.
41. Ground spawn of "Lost Scroll" (10616) in `dalnir`.
42. Ground spawn of "Charm and Sacrifice" (10617) in `airplane`.
43. Combine in "Enchanters Sack" (17861): "Spoon" (10614), "The One Key" (10615), "Lost Scroll" (10616), "Charm and Sacrifice" (10617). Produces "Sack For Mizzle" (10636). The combine does not fail.
44. akanon/"Clockwork Viix", hand "Sack For Mizzle" (10636). Gives "2nd Piece of Staff" (10611).
45. firiona/"Nadia Starfeast", say "Diamond". Gives "Dull Diamond" (10631).
46. kaesora/"Spectral Librarian", hand "Dull Diamond" (10631). Gives "Enchanted Diamond" (10618).
47. firiona/"Nadia Starfeast", say "Sapphire". Gives "Dull Sapphire" (10632).
48. skyfire/"Felia Goldenwing", hand "Dull Sapphire" (10632). Gives "Enchanted Sapphire" (10619).
49. firiona/"Nadia Starfeast", say "Ruby". Gives "Dull Ruby" (10633).
50. citymist/"Wraith Of Jaxion", hand "Dull Ruby" (10633). Gives "Enchanted Ruby" (10620).
51. firiona/"Nadia Starfeast", say "Emerald". Gives "Dull Emerald" (10634).
52. overthere/"Impaler Tzilug", hand "Dull Emerald" (10634). Gives "Enchanted Emerald" (10621).
53. Combine in "Enchanters Sack" (17861): "Enchanted Diamond" (10618), "Enchanted Sapphire" (10619), "Enchanted Ruby" (10620), "Enchanted Emerald" (10621). Produces "Sack For Nadia" (10637). The combine does not fail.
54. firiona/"Nadia Starfeast", hand "Sack For Nadia" (10637). Gives "3rd Piece of Staff" (10612).
55. Loot "Head of the Serpent" (10622) from "Wraith of a Shissar" in `fearplane`.
56. Loot "Essence of a Ghost" (10623) from "the Ghost of Kindle" in `hole`.
57. No quest step gives Essence of a Vampire (10624). The dump lists it in hateplane, hateplaneb.
58. Loot "Sands of the Mystics" (10625) from "The Tangrin" in `fieldofbone`.
59. Combine in "Enchanters Sack" (17861): "Head of the Serpent" (10622), "Essence of a Ghost" (10623), "Essence of a Vampire" (10624), "Sands of the Mystics" (10625). Produces "Sack For Polzin" (10638). The combine does not fail.
60. hole/"Polzin Mrid", hand "Sack For Polzin" (10638). Gives "4th Piece of Staff" (10613).
61. Combine in "Enchanters Sack" (17861): "1st Piece of Staff" (10610), "2nd Piece of Staff" (10611), "3rd Piece of Staff" (10612), "4th Piece of Staff" (10613). Produces "Bundle of Staves" (10639). The combine does not fail.
62. burningwood/"A Sarnak Imitator", hand "Bundle of Staves" (10639). Gives "Staff of the Serpent" (10650).
63. burningwood/"A Sarnak Imitator", say "Hail". Sets `ench_epic` to `1`.
64. global/"Global Player", combine recipe 19919. Sets `ench_epic` to `9`.
65. burningwood/"A Sarnak Imitator", say "Chest". Requires `ench_epic` set. Requires `ench_epic` >=3. Gives "Ornate Staff Chest" (52960).
66. Ground spawn of "Taste of Enticement" (52964) in `mistmoore`.
67. frozenshadow/"Advisor Svartmane", hand "Taste of Enticement" (52964). Gives "1st Piece of the Staff" (54289).
68. Loot "2nd Piece of the Staff" (54310) from "The Yrendan Scarab" in `pojustice`.
69. Loot "3rd Piece of the Staff" (54299) from "Chavoor the Trickster" in `vxed`.
70. Loot "3rd Piece of the Staff" (54299) from "Ikaav Firecaller" in `vxed`.
71. Loot "3rd Piece of the Staff" (54299) from "Kyv Hunter" in `vxed`.
72. Loot "3rd Piece of the Staff" (54299) from "Ukun Bloodbeast" in `vxed`.
73. Loot "3rd Piece of the Staff" (54299) from "Umbiki" in `vxed`.
74. Loot "3rd Piece of the Staff" (54299) from "misguided beludu Creque" in `vxed`.
75. Say "War Timer" to bloodfields/"War".
76. Spawns "War Caller Kaavi" (301042).
77. Loot "4th Piece of the Staff" (54284) from "War Caller Kaavi".
78. **Broken:** no event trigger found for `bloodfields/war#timer:reset`.
79. Spawns "War Caller Kaavi" (301042) after `bloodfields/war#timer:reset`.
80. Loot "4th Piece of the Staff" (54284) from "War Caller Kaavi" in `bloodfields`.
81. Loot "Ornate Staff Topper" (52961) from "Faleniel of Darkwater" in `sirens`.
82. Loot "All-Seeing Eye" (54293) from "All-Seeing Eye" in `mischiefplane`.
83. Summon "Black Diamond of Nightmares" (29990) by casting "Imbue Nightmare".
84. poknowledge/"Aid Grimel", say "Versed In The Art Of Smithing". Gives "Filthy Breastplate" (15984).
85. Combine in "Mixing Bowl" (17906): "Celestial Solvent" (9731), "Words of Acquisition (Beza)" (11866). Produces "Celestial Essence" (9650). Requires Baking, trivial 15. The combine does not fail.
86. Combine in "Mixing Bowl" (17906): "Celestial Solvent" (9731), "Words of Burnishing" (11862). Produces "Celestial Essence" (9650). Requires Baking, trivial 15. The combine does not fail.
87. 67 other recipes also produce Celestial Essence (9650).
88. Common item: Jar of Acid (22133). Listed in 15 zones.
89. Combine in Brew Barrel (19): "Celestial Essence" (9650), "Jar of Acid" (22133). Produces "Acid Wash" (15987). Requires Brewing, trivial 151.
90. Combine in Forge (17): "Filthy Breastplate" (15984), "Acid Wash" (15987). Produces "Cleansed Breastplate" (15998). Requires Blacksmithing, trivial 227.
91. Common item: Mortar and Pestle (17904). Listed in 12 zones.
92. No quest step gives Sandstorm Pearl (29909). The dump lists it in bothunder.
93. Combine in "Mortar and Pestle" (17904): "Sandstorm Pearl" (29909). Produces "Powdered Sandstorm Pearl" (29520) x4. Requires Make Poison, trivial 255.
94. Common item: Firing Sheet (16906). Listed in 34 zones.
95. Combine in Pottery Wheel (21): "Small Block of Clay" (16900), "Water Flask" (13006). Produces "Block of Clay" (16901). Requires Pottery, trivial 21.
96. Combine in Pottery Wheel (21): "Water Flask" (13006), "Large Block of Clay" (16902). Produces "Block of Clay" (16901) x2. Requires Pottery, trivial 21.
97. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
98. qeynos2/"Phin Esrinap", hand "Grathin's Invoice" (18922). Gives "Water Flask" (13006).
99. Combine in Brew Barrel (19): "Pod of Water" (13044), "Bottle" (16598). Produces "Water Flask" (13006). Requires Brewing, trivial 21.
100. Combine in Pottery Wheel (21): "Block of Clay" (16901), "Water Flask" (13006). Produces "Large Block of Clay" (16902). Requires Pottery, trivial 21.
101. Common item: Large Bowl Sketch (16963). Listed in 29 zones.
102. Combine in Pottery Wheel (21): "Large Block of Clay" (16902), "Water Flask" (13006), "Large Bowl Sketch" (16963). Produces "Unfired Mixing Bowl" (16930). Requires Pottery, trivial 128.
103. Combine in Kiln (22): "Firing Sheet" (16906), "Unfired Mixing Bowl" (16930). Produces "Mixing Bowl" (17906). Requires Pottery, trivial 15.
104. Combine in "Mixing Bowl" (17906): "Sandstorm Pearl" (29909). Produces "Powdered Sandstorm Pearl" (29520) x4. Requires Baking. The combine does not fail.
105. Spawns "a Koka'Vor chieftain" (210236) in `postorms` on event_signal.
106. Loot "Storm Rider Blood" (29526) from "a Koka'Vor chieftain".
107. Loot "Storm Rider Blood" (29526) from "A stormrider" in `bothunder`.
108. Loot "Storm Rider Blood" (29526) from "Dolsoj Warrebs" in `bazaar`.
109. Loot "Storm Rider Blood" (29526) from "a Koka'Vor krovian" in `postorms`.
110. Loot "Storm Rider Blood" (29526) from "a Koka'Vor senvar" in `postorms`.
111. No quest step gives Drop of Pure Rain (29904). The dump lists it in bothunder.
112. Combine in Brew Barrel (19): "Powdered Sandstorm Pearl" (29520), "Storm Rider Blood" (29526), "Drop of Pure Rain" (29904). Produces "Hurricane Temper" (29533). Requires Brewing, trivial 135.
113. Combine in Forge (17): "Cleansed Breastplate" (15998), "Hurricane Temper" (29533). Produces "Tempered Breastplate" (15999). Requires Blacksmithing, trivial 229.
114. Combine in Forge (17): "Black Diamond of Nightmares" (29990), "Tempered Breastplate" (15999). Produces "Imbued Breastplate" (15985). Requires Blacksmithing 220. Trivial at 275.
115. poknowledge/"Aid Grimel", hand "Imbued Breastplate" (15985). Gives "Hardened Leather Signet" (16249).
116. poknowledge/"Aid Grimel", say "Skill In Brewing". Gives "Portable Drink Barrel" (17179).
117. Forage "Dragon Egg" (19139) in `templeveeshan`.
118. Forage "Dragon Egg" (19139) in `westwastes`.
119. Combine in "Portable Drink Barrel" (17179): "Water Flask" (13006), "Dragon Egg" (19139). Produces "Dragon Egg Oil" (9664). Requires Brewing, trivial 150.
120. Loot "Glimmering Oil" (52942) from "A Greasy Clockwork" in `poinnovation`.
121. bazaar/"Caerlyna", hand "Spell Research Kit" (93492). Gives "Spell Research Kit Token" (93667).
122. crescent/"Realnyna", hand "Spell Research Kit" (93492). Gives "Spell Research Kit Token" (93667).
123. bazaar/"Caerlyna", hand "Spell Research Kit Token" (93667). Gives "Spell Research Kit" (93492).
124. crescent/"Realnyna", hand "Spell Research Kit Token" (93667). Gives "Spell Research Kit" (93492).
125. No quest step gives Coalesced Mana (97042). The dump lists it in arcstone, relic, skylance.
126. Combine in Pottery Wheel (21): "Water Flask" (13006), "White Wolf Skin" (13768), "Small Block of Clay" (16900), "Vial Sketch" (16968). Produces "Unfired Poison Vial" (16885). Requires Pottery, trivial 148.
127. Combine in Pottery Wheel (21): "Water Flask" (13006), "Crow's Special Brew" (13799), "Small Block of Clay" (16900), "Vial Sketch" (16968). Produces "Unfired Poison Vial" (16885). Requires Pottery, trivial 148.
128. 19 other recipes also produce Unfired Poison Vial (16885).
129. Common item: High Quality Firing Sheet (16908). Listed in 34 zones.
130. Combine in Kiln (22): "Unfired Poison Vial" (16885), "High Quality Firing Sheet" (16908). Produces "Poison Vial" (16965). Requires Pottery, trivial 17.
131. Kill broodlands/"Brood Drone". Spawns "The Broodqueen" (337254).
132. Loot "Ruby" (10035) from "The Broodqueen".
133. Spawns "A parasitic murkglider" (303121) in `causeway` on event_hp.
134. Loot "Ruby" (10035) from "A parasitic murkglider".
135. Spawns "a Reanimated Berserker" (103093) in `chardok` on enter.
136. Loot "Ruby" (10035) from "a Reanimated Berserker".
137. Kill delvea/"A Drake Egg". Spawns "a Delve spellbinder" (341091).
138. Loot "Ruby" (10035) from "a Delve spellbinder".
139. 116 other loot steps also yield Ruby (10035).
140. Combine in "Spell Research Kit" (93492): "Celestial Essence" (9650), "Coalesced Mana" (97042), "Poison Vial" (16965), "Ruby" (10035). Produces "Vial of Purified Mana" (10254). Requires Research, trivial 200.
141. Forage "Glow Lichen" (14925) in `nektulos`.
142. Common item: Essence of Sunlight (22527). Listed in 8 zones.
143. Ground spawn of "Abysmal Moonwater" (54298) in `abysmal`.
144. Combine in Brew Barrel (19): "Vial of Purified Mana" (10254), "Glow Lichen" (14925), "Essence of Sunlight" (22527), "Abysmal Moonwater" (54298). Produces "Glowing Concoction" (52943). Requires Brewing, trivial 116.
145. Common item: Medicine Bag (17901). Listed in 33 zones.
146. Common item: Glaze Lacquer (29355). Listed in 5 zones.
147. No quest step gives Prism Shard (65469). The dump lists it in crescent, gunthak, poknowledge.
148. Combine in "Medicine Bag" (17901): "Glaze Lacquer" (29355), "Prism Shard" (65469). Produces "Prismatic Dye" (65472). Requires Alchemy, trivial 54.
149. Combine in "Portable Drink Barrel" (17179): "Glaze Lacquer" (29355), "Prism Shard" (65469). Produces "Prismatic Dye" (65472). Requires Brewing, trivial 54.
150. Combine in Brew Barrel (19): "Dragon Egg Oil" (9664), "Glimmering Oil" (52942), "Glowing Concoction" (52943), "Prismatic Dye" (65472). Produces "Incandescent Oil" (57924). Requires Brewing, trivial 116. The combine does not fail.
151. burningwood/"A Sarnak Imitator", say "Hail". Sets `ench_epic` to `1`.
152. burningwood/"A Sarnak Imitator", say "Prepared". Requires `ench_epic` set. Requires `ench_epic` >=1. Gives "Tattered Illegible Tome" (57918).
153. Ground spawn of "Cryptic Page" (52933) in `charasis`.
154. Ground spawn of "Cryptic Page" (52934) in `sebilis`.
155. Ground spawn of "Cryptic Page" (52935) in `cazicthule`.
156. Ground spawn of "Cryptic Page" (52936) in `crystal`.
157. Ground spawn of "Cryptic Page" (52937) in `skyshrine`.
158. Ground spawn of "Cryptic Page" (52938) in `velketor`.
159. Ground spawn of "Cryptic Page" (52939) in `nadox`.
160. Ground spawn of "Cryptic Page" (54308) in `najena`.
161. Ground spawn of "Cryptic Page" (57916) in `fungusgrove`.
162. Ground spawn of "Cryptic Page" (57923) in `oot`.
163. Combine in "Tattered Illegible Tome" (57918): "Cryptic Page" (52933), "Cryptic Page" (52934), "Cryptic Page" (52935), "Cryptic Page" (52936), "Cryptic Page" (52937), "Cryptic Page" (52938), "Cryptic Page" (52939), "Cryptic Page" (54308), "Cryptic Page" (57916), "Cryptic Page" (57923). Produces "Complete Illegible Tome" (54267). The combine does not fail.
164. burningwood/"A Sarnak Imitator", hand "Complete Illegible Tome" (54267). Sets `ench_epic` to `2`.
165. poknowledge/"Grand Librarian Maelin", say "Jeb Lumsed Sent Me". Requires `ench_epic` ==2. Gives "Note to Lobaen" (52950).
166. poknowledge/"Illusionist Lobaen", hand "Note to Lobaen" (52950). Gives "Sealed Documents" (52959).
167. burningwood/"A Sarnak Imitator", hand "Sealed Documents" (52959). Gives "Assembling the Staff" (54286).
168. Loot "Sullied Gold Filigree" (52963) from "An Enticing Potameid" in `natimbi`.
169. hohonora/"Anthone Chapin", hand "Sullied Gold Filigree" (52963). Gives "Purified Gold Filigree" (52953).
170. Combine in "Ornate Staff Chest" (52960): "1st Piece of the Staff" (54289), "2nd Piece of the Staff" (54310), "3rd Piece of the Staff" (54299), "4th Piece of the Staff" (54284), "Ornate Staff Topper" (52961), "All-Seeing Eye" (54293), "Incandescent Oil" (57924), "Purified Gold Filigree" (52953). Produces "Latched Ornate Chest" (52966). The combine does not fail.

### "Oculus of Persuasion" (52952)

1. Hand "Dragon Boneshard" (65574) to veksar/"Spirit Of Garudon". Spawns "Garudon" (109107). Loot "Garudon's Statue" (52941) from "Garudon".
2. Loot "Garudon's Statue" (52941) from "Garudon".
3. lakeofillomen/"A Bloodgill Mimic", hand "Garudon's Statue" (52941). Sets `EnchPre` to `1`.
4. Loot "Crumbling Tome" (54313) from "A Shissar Lorekeeper" in `ssratemple`.
5. ssratemple/"A Soriz Imitator", hand "Crumbling Tome" (54313). Requires `EnchPre` ==1. Gives "Illegible Tome" (52947).
6. akanon/"Rilgor Plegnog", say "Insidious". Gives "Compacting Satchel" (54303).
7. No quest step gives Fine Insidious Halo (54384). The dump lists it in hateplaneb.
8. No quest step gives Fine Insidious Sleeves (54385). The dump lists it in hateplaneb.
9. No quest step gives Fine Insidious Manacle (54386). The dump lists it in hateplaneb.
10. No quest step gives Fine Insidious Gloves (54387). The dump lists it in hateplaneb.
11. No quest step gives Fine Insidious Pantaloons (54388). The dump lists it in hateplaneb.
12. No quest step gives Fine Insidious Slippers (54389). The dump lists it in hateplaneb.
13. Combine in "Compacting Satchel" (54303): "Fine Insidious Halo" (54384), "Fine Insidious Sleeves" (54385), "Fine Insidious Manacle" (54386), "Fine Insidious Gloves" (54387), "Fine Insidious Pantaloons" (54388), "Fine Insidious Slippers" (54389). Produces "Insidious Bundle" (54317). The combine does not fail.
14. akanon/"Rilgor Plegnog", hand "Insidious Bundle" (54317). Gives "Gnomish Translating Device" (52945).
15. burningwood/"A Sarnak Imitator", hand "Gnomish Translating Device" (52945) + "Illegible Tome" (52947). Sets `EnchPre` to `2`.
16. Common item: Shining Metallic Robes (1360). Listed in 4 zones.
17. akanon/"Rilgor Plegnog", hand "Shining Metallic Robes" (1360). Gives "Mechanical Pen" (10600).
18. qcat/"Reania Jukle", say "Supply". Gives "Empty Ink Vial" (10626).
19. gukbottom/"A Ghoul Scribe", hand "Empty Ink Vial" (10626). Gives "Ink of the Dark" (10601).
20. Hand "Quill" (13051) + "Piece of Parchment" (13063) to qey2hh1/"Chrislin Baker". Spawns "Thrackin Griften" (12172). Loot "White Paper" (10602) from "Thrackin Griften".
21. Loot "White Paper" (10602) from "Thrackin Griften".
22. erudnext/"Stofo Olan", hand "Mechanical Pen" (10600) + "Ink of the Dark" (10601) + "White Paper" (10602). Gives "Copy of Notes" (10603).
23. burningwood/"A Sarnak Imitator", hand "Copy of Notes" (10603). Gives "Jeb's Seal" (10604).
24. akanon/"Clockwork Viix", hand "Jeb's Seal" (10604). Gives "Enchanters Sack" (17861).
25. firiona/"Nadia Starfeast", say "I Need A Sack". Gives "Enchanters Sack" (17861).
26. hole/"Polzin Mrid", hand "Jeb's Seal" (10604). Gives "Enchanters Sack" (17861).
27. overthere/"Modani Qu-Loni", hand "Jeb's Seal" (10604). Gives "Enchanters Sack" (17861).
28. Loot "Xolion Rod" (10606) from "Vessel Drozlin" in `cabeast`.
29. Loot "Innoruuk's Word" (10607) from "Verina Tomb" in `neriakc`.
30. Loot "Head of a Prince" (10627) from "Prince Selrach Di'zok" in `chardok`.
31. felwitheb/"Joren Nobleheart", hand "Head of a Prince" (10627). Gives "Chalice of Kings" (10608).
32. Ground spawn of "Large Muddy Sandals" (10628) in `oggok`.
33. oggok/"Bozlum Blossom", hand "Large Muddy Sandals" (10628). Gives "Scribbled Parchment" (10629).
34. oggok/"Brokk Boxtripper", hand "Scribbled Parchment" (10629). Gives "Gift to Bozlum" (10630).
35. oggok/"Bozlum Blossom", hand "Gift to Bozlum" (10630). Gives "Snow Blossoms" (10609).
36. Combine in "Enchanters Sack" (17861): "Xolion Rod" (10606), "Innoruuk's Word" (10607), "Chalice of Kings" (10608), "Snow Blossoms" (10609). Produces "Sack For Modani" (10635). The combine does not fail.
37. overthere/"Modani Qu-Loni", hand "Sack For Modani" (10635). Gives "1st Piece of Staff" (10610).
38. Loot "Spoon" (10614) from "Cazel" in `oasis`.
39. Loot "Spoon" (10614) from "Cazel" in `southro`.
40. Ground spawn of "The One Key" (10615) in `overthere`.
41. Ground spawn of "Lost Scroll" (10616) in `dalnir`.
42. Ground spawn of "Charm and Sacrifice" (10617) in `airplane`.
43. Combine in "Enchanters Sack" (17861): "Spoon" (10614), "The One Key" (10615), "Lost Scroll" (10616), "Charm and Sacrifice" (10617). Produces "Sack For Mizzle" (10636). The combine does not fail.
44. akanon/"Clockwork Viix", hand "Sack For Mizzle" (10636). Gives "2nd Piece of Staff" (10611).
45. firiona/"Nadia Starfeast", say "Diamond". Gives "Dull Diamond" (10631).
46. kaesora/"Spectral Librarian", hand "Dull Diamond" (10631). Gives "Enchanted Diamond" (10618).
47. firiona/"Nadia Starfeast", say "Sapphire". Gives "Dull Sapphire" (10632).
48. skyfire/"Felia Goldenwing", hand "Dull Sapphire" (10632). Gives "Enchanted Sapphire" (10619).
49. firiona/"Nadia Starfeast", say "Ruby". Gives "Dull Ruby" (10633).
50. citymist/"Wraith Of Jaxion", hand "Dull Ruby" (10633). Gives "Enchanted Ruby" (10620).
51. firiona/"Nadia Starfeast", say "Emerald". Gives "Dull Emerald" (10634).
52. overthere/"Impaler Tzilug", hand "Dull Emerald" (10634). Gives "Enchanted Emerald" (10621).
53. Combine in "Enchanters Sack" (17861): "Enchanted Diamond" (10618), "Enchanted Sapphire" (10619), "Enchanted Ruby" (10620), "Enchanted Emerald" (10621). Produces "Sack For Nadia" (10637). The combine does not fail.
54. firiona/"Nadia Starfeast", hand "Sack For Nadia" (10637). Gives "3rd Piece of Staff" (10612).
55. Loot "Head of the Serpent" (10622) from "Wraith of a Shissar" in `fearplane`.
56. Loot "Essence of a Ghost" (10623) from "the Ghost of Kindle" in `hole`.
57. No quest step gives Essence of a Vampire (10624). The dump lists it in hateplane, hateplaneb.
58. Loot "Sands of the Mystics" (10625) from "The Tangrin" in `fieldofbone`.
59. Combine in "Enchanters Sack" (17861): "Head of the Serpent" (10622), "Essence of a Ghost" (10623), "Essence of a Vampire" (10624), "Sands of the Mystics" (10625). Produces "Sack For Polzin" (10638). The combine does not fail.
60. hole/"Polzin Mrid", hand "Sack For Polzin" (10638). Gives "4th Piece of Staff" (10613).
61. Combine in "Enchanters Sack" (17861): "1st Piece of Staff" (10610), "2nd Piece of Staff" (10611), "3rd Piece of Staff" (10612), "4th Piece of Staff" (10613). Produces "Bundle of Staves" (10639). The combine does not fail.
62. burningwood/"A Sarnak Imitator", hand "Bundle of Staves" (10639). Gives "Staff of the Serpent" (10650).
63. burningwood/"A Sarnak Imitator", say "Hail". Sets `ench_epic` to `1`.
64. global/"Global Player", combine recipe 19919. Sets `ench_epic` to `9`.
65. burningwood/"A Sarnak Imitator", say "Chest". Requires `ench_epic` set. Requires `ench_epic` >=3. Gives "Ornate Staff Chest" (52960).
66. Ground spawn of "Taste of Enticement" (52964) in `mistmoore`.
67. frozenshadow/"Advisor Svartmane", hand "Taste of Enticement" (52964). Gives "1st Piece of the Staff" (54289).
68. Loot "2nd Piece of the Staff" (54310) from "The Yrendan Scarab" in `pojustice`.
69. Loot "3rd Piece of the Staff" (54299) from "Chavoor the Trickster" in `vxed`.
70. Loot "3rd Piece of the Staff" (54299) from "Ikaav Firecaller" in `vxed`.
71. Loot "3rd Piece of the Staff" (54299) from "Kyv Hunter" in `vxed`.
72. Loot "3rd Piece of the Staff" (54299) from "Ukun Bloodbeast" in `vxed`.
73. Loot "3rd Piece of the Staff" (54299) from "Umbiki" in `vxed`.
74. Loot "3rd Piece of the Staff" (54299) from "misguided beludu Creque" in `vxed`.
75. Say "War Timer" to bloodfields/"War".
76. Spawns "War Caller Kaavi" (301042).
77. Loot "4th Piece of the Staff" (54284) from "War Caller Kaavi".
78. **Broken:** no event trigger found for `bloodfields/war#timer:reset`.
79. Spawns "War Caller Kaavi" (301042) after `bloodfields/war#timer:reset`.
80. Loot "4th Piece of the Staff" (54284) from "War Caller Kaavi" in `bloodfields`.
81. Loot "Ornate Staff Topper" (52961) from "Faleniel of Darkwater" in `sirens`.
82. Loot "All-Seeing Eye" (54293) from "All-Seeing Eye" in `mischiefplane`.
83. Summon "Black Diamond of Nightmares" (29990) by casting "Imbue Nightmare".
84. poknowledge/"Aid Grimel", say "Versed In The Art Of Smithing". Gives "Filthy Breastplate" (15984).
85. Combine in "Mixing Bowl" (17906): "Celestial Solvent" (9731), "Words of Acquisition (Beza)" (11866). Produces "Celestial Essence" (9650). Requires Baking, trivial 15. The combine does not fail.
86. Combine in "Mixing Bowl" (17906): "Celestial Solvent" (9731), "Words of Burnishing" (11862). Produces "Celestial Essence" (9650). Requires Baking, trivial 15. The combine does not fail.
87. 67 other recipes also produce Celestial Essence (9650).
88. Common item: Jar of Acid (22133). Listed in 15 zones.
89. Combine in Brew Barrel (19): "Celestial Essence" (9650), "Jar of Acid" (22133). Produces "Acid Wash" (15987). Requires Brewing, trivial 151.
90. Combine in Forge (17): "Filthy Breastplate" (15984), "Acid Wash" (15987). Produces "Cleansed Breastplate" (15998). Requires Blacksmithing, trivial 227.
91. Common item: Mortar and Pestle (17904). Listed in 12 zones.
92. No quest step gives Sandstorm Pearl (29909). The dump lists it in bothunder.
93. Combine in "Mortar and Pestle" (17904): "Sandstorm Pearl" (29909). Produces "Powdered Sandstorm Pearl" (29520) x4. Requires Make Poison, trivial 255.
94. Common item: Firing Sheet (16906). Listed in 34 zones.
95. Combine in Pottery Wheel (21): "Block of Clay" (16901), "Water Flask" (13006). Produces "Large Block of Clay" (16902). Requires Pottery, trivial 21.
96. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
97. qeynos2/"Phin Esrinap", hand "Grathin's Invoice" (18922). Gives "Water Flask" (13006).
98. Combine in Brew Barrel (19): "Pod of Water" (13044), "Bottle" (16598). Produces "Water Flask" (13006). Requires Brewing, trivial 21.
99. Common item: Large Bowl Sketch (16963). Listed in 29 zones.
100. Combine in Pottery Wheel (21): "Large Block of Clay" (16902), "Water Flask" (13006), "Large Bowl Sketch" (16963). Produces "Unfired Mixing Bowl" (16930). Requires Pottery, trivial 128.
101. Combine in Kiln (22): "Firing Sheet" (16906), "Unfired Mixing Bowl" (16930). Produces "Mixing Bowl" (17906). Requires Pottery, trivial 15.
102. Combine in "Mixing Bowl" (17906): "Sandstorm Pearl" (29909). Produces "Powdered Sandstorm Pearl" (29520) x4. Requires Baking. The combine does not fail.
103. Spawns "a Koka'Vor chieftain" (210236) in `postorms` on event_signal.
104. Loot "Storm Rider Blood" (29526) from "a Koka'Vor chieftain".
105. Loot "Storm Rider Blood" (29526) from "A stormrider" in `bothunder`.
106. Loot "Storm Rider Blood" (29526) from "Dolsoj Warrebs" in `bazaar`.
107. Loot "Storm Rider Blood" (29526) from "a Koka'Vor krovian" in `postorms`.
108. Loot "Storm Rider Blood" (29526) from "a Koka'Vor senvar" in `postorms`.
109. No quest step gives Drop of Pure Rain (29904). The dump lists it in bothunder.
110. Combine in Brew Barrel (19): "Powdered Sandstorm Pearl" (29520), "Storm Rider Blood" (29526), "Drop of Pure Rain" (29904). Produces "Hurricane Temper" (29533). Requires Brewing, trivial 135.
111. Combine in Forge (17): "Cleansed Breastplate" (15998), "Hurricane Temper" (29533). Produces "Tempered Breastplate" (15999). Requires Blacksmithing, trivial 229.
112. Combine in Forge (17): "Black Diamond of Nightmares" (29990), "Tempered Breastplate" (15999). Produces "Imbued Breastplate" (15985). Requires Blacksmithing 220. Trivial at 275.
113. poknowledge/"Aid Grimel", hand "Imbued Breastplate" (15985). Gives "Hardened Leather Signet" (16249).
114. poknowledge/"Aid Grimel", say "Skill In Brewing". Gives "Portable Drink Barrel" (17179).
115. Forage "Dragon Egg" (19139) in `templeveeshan`.
116. Forage "Dragon Egg" (19139) in `westwastes`.
117. Combine in "Portable Drink Barrel" (17179): "Water Flask" (13006), "Dragon Egg" (19139). Produces "Dragon Egg Oil" (9664). Requires Brewing, trivial 150.
118. Loot "Glimmering Oil" (52942) from "A Greasy Clockwork" in `poinnovation`.
119. bazaar/"Caerlyna", hand "Spell Research Kit" (93492). Gives "Spell Research Kit Token" (93667).
120. crescent/"Realnyna", hand "Spell Research Kit" (93492). Gives "Spell Research Kit Token" (93667).
121. bazaar/"Caerlyna", hand "Spell Research Kit Token" (93667). Gives "Spell Research Kit" (93492).
122. crescent/"Realnyna", hand "Spell Research Kit Token" (93667). Gives "Spell Research Kit" (93492).
123. No quest step gives Coalesced Mana (97042). The dump lists it in arcstone, relic, skylance.
124. Combine in Pottery Wheel (21): "Water Flask" (13006), "White Wolf Skin" (13768), "Small Block of Clay" (16900), "Vial Sketch" (16968). Produces "Unfired Poison Vial" (16885). Requires Pottery, trivial 148.
125. Combine in Pottery Wheel (21): "Water Flask" (13006), "Crow's Special Brew" (13799), "Small Block of Clay" (16900), "Vial Sketch" (16968). Produces "Unfired Poison Vial" (16885). Requires Pottery, trivial 148.
126. 19 other recipes also produce Unfired Poison Vial (16885).
127. Common item: High Quality Firing Sheet (16908). Listed in 34 zones.
128. Combine in Kiln (22): "Unfired Poison Vial" (16885), "High Quality Firing Sheet" (16908). Produces "Poison Vial" (16965). Requires Pottery, trivial 17.
129. Kill broodlands/"Brood Drone". Spawns "The Broodqueen" (337254).
130. Loot "Ruby" (10035) from "The Broodqueen".
131. Spawns "A parasitic murkglider" (303121) in `causeway` on event_hp.
132. Loot "Ruby" (10035) from "A parasitic murkglider".
133. Spawns "a Reanimated Berserker" (103093) in `chardok` on enter.
134. Loot "Ruby" (10035) from "a Reanimated Berserker".
135. Kill delvea/"A Drake Egg". Spawns "a Delve spellbinder" (341091).
136. Loot "Ruby" (10035) from "a Delve spellbinder".
137. 116 other loot steps also yield Ruby (10035).
138. Combine in "Spell Research Kit" (93492): "Celestial Essence" (9650), "Coalesced Mana" (97042), "Poison Vial" (16965), "Ruby" (10035). Produces "Vial of Purified Mana" (10254). Requires Research, trivial 200.
139. Forage "Glow Lichen" (14925) in `nektulos`.
140. Common item: Essence of Sunlight (22527). Listed in 8 zones.
141. Ground spawn of "Abysmal Moonwater" (54298) in `abysmal`.
142. Combine in Brew Barrel (19): "Vial of Purified Mana" (10254), "Glow Lichen" (14925), "Essence of Sunlight" (22527), "Abysmal Moonwater" (54298). Produces "Glowing Concoction" (52943). Requires Brewing, trivial 116.
143. Common item: Medicine Bag (17901). Listed in 33 zones.
144. Common item: Glaze Lacquer (29355). Listed in 5 zones.
145. No quest step gives Prism Shard (65469). The dump lists it in crescent, gunthak, poknowledge.
146. Combine in "Medicine Bag" (17901): "Glaze Lacquer" (29355), "Prism Shard" (65469). Produces "Prismatic Dye" (65472). Requires Alchemy, trivial 54.
147. Combine in "Portable Drink Barrel" (17179): "Glaze Lacquer" (29355), "Prism Shard" (65469). Produces "Prismatic Dye" (65472). Requires Brewing, trivial 54.
148. Combine in Brew Barrel (19): "Dragon Egg Oil" (9664), "Glimmering Oil" (52942), "Glowing Concoction" (52943), "Prismatic Dye" (65472). Produces "Incandescent Oil" (57924). Requires Brewing, trivial 116. The combine does not fail.
149. burningwood/"A Sarnak Imitator", say "Hail". Sets `ench_epic` to `1`.
150. burningwood/"A Sarnak Imitator", say "Prepared". Requires `ench_epic` set. Requires `ench_epic` >=1. Gives "Tattered Illegible Tome" (57918).
151. Ground spawn of "Cryptic Page" (52933) in `charasis`.
152. Ground spawn of "Cryptic Page" (52934) in `sebilis`.
153. Ground spawn of "Cryptic Page" (52935) in `cazicthule`.
154. Ground spawn of "Cryptic Page" (52936) in `crystal`.
155. Ground spawn of "Cryptic Page" (52937) in `skyshrine`.
156. Ground spawn of "Cryptic Page" (52938) in `velketor`.
157. Ground spawn of "Cryptic Page" (52939) in `nadox`.
158. Ground spawn of "Cryptic Page" (54308) in `najena`.
159. Ground spawn of "Cryptic Page" (57916) in `fungusgrove`.
160. Ground spawn of "Cryptic Page" (57923) in `oot`.
161. Combine in "Tattered Illegible Tome" (57918): "Cryptic Page" (52933), "Cryptic Page" (52934), "Cryptic Page" (52935), "Cryptic Page" (52936), "Cryptic Page" (52937), "Cryptic Page" (52938), "Cryptic Page" (52939), "Cryptic Page" (54308), "Cryptic Page" (57916), "Cryptic Page" (57923). Produces "Complete Illegible Tome" (54267). The combine does not fail.
162. burningwood/"A Sarnak Imitator", hand "Complete Illegible Tome" (54267). Sets `ench_epic` to `2`.
163. poknowledge/"Grand Librarian Maelin", say "Jeb Lumsed Sent Me". Requires `ench_epic` ==2. Gives "Note to Lobaen" (52950).
164. poknowledge/"Illusionist Lobaen", hand "Note to Lobaen" (52950). Gives "Sealed Documents" (52959).
165. burningwood/"A Sarnak Imitator", hand "Sealed Documents" (52959). Gives "Assembling the Staff" (54286).
166. Loot "Sullied Gold Filigree" (52963) from "An Enticing Potameid" in `natimbi`.
167. hohonora/"Anthone Chapin", hand "Sullied Gold Filigree" (52963). Gives "Purified Gold Filigree" (52953).
168. Combine in "Ornate Staff Chest" (52960): "1st Piece of the Staff" (54289), "2nd Piece of the Staff" (54310), "3rd Piece of the Staff" (54299), "4th Piece of the Staff" (54284), "Ornate Staff Topper" (52961), "All-Seeing Eye" (54293), "Incandescent Oil" (57924), "Purified Gold Filigree" (52953). Produces "Latched Ornate Chest" (52966). The combine does not fail.
169. burningwood/"A Sarnak Imitator", hand "Latched Ornate Chest" (52966). Gives "Oculus of Persuasion" (52952).

### "Purifying Crystal" (52954)

1. No quest step gives Planar Jeweler's Kit (17764). The dump lists it in abysmal, poknowledge.
2. Hand "Dragon Boneshard" (65574) to veksar/"Spirit Of Garudon". Spawns "Garudon" (109107). Loot "Garudon's Statue" (52941) from "Garudon".
3. Loot "Garudon's Statue" (52941) from "Garudon".
4. lakeofillomen/"A Bloodgill Mimic", hand "Garudon's Statue" (52941). Sets `EnchPre` to `1`.
5. Loot "Crumbling Tome" (54313) from "A Shissar Lorekeeper" in `ssratemple`.
6. ssratemple/"A Soriz Imitator", hand "Crumbling Tome" (54313). Requires `EnchPre` ==1. Gives "Illegible Tome" (52947).
7. akanon/"Rilgor Plegnog", say "Insidious". Gives "Compacting Satchel" (54303).
8. No quest step gives Fine Insidious Halo (54384). The dump lists it in hateplaneb.
9. No quest step gives Fine Insidious Sleeves (54385). The dump lists it in hateplaneb.
10. No quest step gives Fine Insidious Manacle (54386). The dump lists it in hateplaneb.
11. No quest step gives Fine Insidious Gloves (54387). The dump lists it in hateplaneb.
12. No quest step gives Fine Insidious Pantaloons (54388). The dump lists it in hateplaneb.
13. No quest step gives Fine Insidious Slippers (54389). The dump lists it in hateplaneb.
14. Combine in "Compacting Satchel" (54303): "Fine Insidious Halo" (54384), "Fine Insidious Sleeves" (54385), "Fine Insidious Manacle" (54386), "Fine Insidious Gloves" (54387), "Fine Insidious Pantaloons" (54388), "Fine Insidious Slippers" (54389). Produces "Insidious Bundle" (54317). The combine does not fail.
15. akanon/"Rilgor Plegnog", hand "Insidious Bundle" (54317). Gives "Gnomish Translating Device" (52945).
16. burningwood/"A Sarnak Imitator", hand "Gnomish Translating Device" (52945) + "Illegible Tome" (52947). Sets `EnchPre` to `2`.
17. Common item: Shining Metallic Robes (1360). Listed in 4 zones.
18. akanon/"Rilgor Plegnog", hand "Shining Metallic Robes" (1360). Gives "Mechanical Pen" (10600).
19. qcat/"Reania Jukle", say "Supply". Gives "Empty Ink Vial" (10626).
20. gukbottom/"A Ghoul Scribe", hand "Empty Ink Vial" (10626). Gives "Ink of the Dark" (10601).
21. Hand "Quill" (13051) + "Piece of Parchment" (13063) to qey2hh1/"Chrislin Baker". Spawns "Thrackin Griften" (12172). Loot "White Paper" (10602) from "Thrackin Griften".
22. Loot "White Paper" (10602) from "Thrackin Griften".
23. erudnext/"Stofo Olan", hand "Mechanical Pen" (10600) + "Ink of the Dark" (10601) + "White Paper" (10602). Gives "Copy of Notes" (10603).
24. burningwood/"A Sarnak Imitator", hand "Copy of Notes" (10603). Gives "Jeb's Seal" (10604).
25. akanon/"Clockwork Viix", hand "Jeb's Seal" (10604). Gives "Enchanters Sack" (17861).
26. firiona/"Nadia Starfeast", say "I Need A Sack". Gives "Enchanters Sack" (17861).
27. hole/"Polzin Mrid", hand "Jeb's Seal" (10604). Gives "Enchanters Sack" (17861).
28. overthere/"Modani Qu-Loni", hand "Jeb's Seal" (10604). Gives "Enchanters Sack" (17861).
29. Loot "Xolion Rod" (10606) from "Vessel Drozlin" in `cabeast`.
30. Loot "Innoruuk's Word" (10607) from "Verina Tomb" in `neriakc`.
31. Loot "Head of a Prince" (10627) from "Prince Selrach Di'zok" in `chardok`.
32. felwitheb/"Joren Nobleheart", hand "Head of a Prince" (10627). Gives "Chalice of Kings" (10608).
33. Ground spawn of "Large Muddy Sandals" (10628) in `oggok`.
34. oggok/"Bozlum Blossom", hand "Large Muddy Sandals" (10628). Gives "Scribbled Parchment" (10629).
35. oggok/"Brokk Boxtripper", hand "Scribbled Parchment" (10629). Gives "Gift to Bozlum" (10630).
36. oggok/"Bozlum Blossom", hand "Gift to Bozlum" (10630). Gives "Snow Blossoms" (10609).
37. Combine in "Enchanters Sack" (17861): "Xolion Rod" (10606), "Innoruuk's Word" (10607), "Chalice of Kings" (10608), "Snow Blossoms" (10609). Produces "Sack For Modani" (10635). The combine does not fail.
38. overthere/"Modani Qu-Loni", hand "Sack For Modani" (10635). Gives "1st Piece of Staff" (10610).
39. Loot "Spoon" (10614) from "Cazel" in `oasis`.
40. Loot "Spoon" (10614) from "Cazel" in `southro`.
41. Ground spawn of "The One Key" (10615) in `overthere`.
42. Ground spawn of "Lost Scroll" (10616) in `dalnir`.
43. Ground spawn of "Charm and Sacrifice" (10617) in `airplane`.
44. Combine in "Enchanters Sack" (17861): "Spoon" (10614), "The One Key" (10615), "Lost Scroll" (10616), "Charm and Sacrifice" (10617). Produces "Sack For Mizzle" (10636). The combine does not fail.
45. akanon/"Clockwork Viix", hand "Sack For Mizzle" (10636). Gives "2nd Piece of Staff" (10611).
46. firiona/"Nadia Starfeast", say "Diamond". Gives "Dull Diamond" (10631).
47. kaesora/"Spectral Librarian", hand "Dull Diamond" (10631). Gives "Enchanted Diamond" (10618).
48. firiona/"Nadia Starfeast", say "Sapphire". Gives "Dull Sapphire" (10632).
49. skyfire/"Felia Goldenwing", hand "Dull Sapphire" (10632). Gives "Enchanted Sapphire" (10619).
50. firiona/"Nadia Starfeast", say "Ruby". Gives "Dull Ruby" (10633).
51. citymist/"Wraith Of Jaxion", hand "Dull Ruby" (10633). Gives "Enchanted Ruby" (10620).
52. firiona/"Nadia Starfeast", say "Emerald". Gives "Dull Emerald" (10634).
53. overthere/"Impaler Tzilug", hand "Dull Emerald" (10634). Gives "Enchanted Emerald" (10621).
54. Combine in "Enchanters Sack" (17861): "Enchanted Diamond" (10618), "Enchanted Sapphire" (10619), "Enchanted Ruby" (10620), "Enchanted Emerald" (10621). Produces "Sack For Nadia" (10637). The combine does not fail.
55. firiona/"Nadia Starfeast", hand "Sack For Nadia" (10637). Gives "3rd Piece of Staff" (10612).
56. Loot "Head of the Serpent" (10622) from "Wraith of a Shissar" in `fearplane`.
57. Loot "Essence of a Ghost" (10623) from "the Ghost of Kindle" in `hole`.
58. No quest step gives Essence of a Vampire (10624). The dump lists it in hateplane, hateplaneb.
59. Loot "Sands of the Mystics" (10625) from "The Tangrin" in `fieldofbone`.
60. Combine in "Enchanters Sack" (17861): "Head of the Serpent" (10622), "Essence of a Ghost" (10623), "Essence of a Vampire" (10624), "Sands of the Mystics" (10625). Produces "Sack For Polzin" (10638). The combine does not fail.
61. hole/"Polzin Mrid", hand "Sack For Polzin" (10638). Gives "4th Piece of Staff" (10613).
62. Combine in "Enchanters Sack" (17861): "1st Piece of Staff" (10610), "2nd Piece of Staff" (10611), "3rd Piece of Staff" (10612), "4th Piece of Staff" (10613). Produces "Bundle of Staves" (10639). The combine does not fail.
63. burningwood/"A Sarnak Imitator", hand "Bundle of Staves" (10639). Gives "Staff of the Serpent" (10650).
64. burningwood/"A Sarnak Imitator", say "Hail". Sets `ench_epic` to `1`.
65. global/"Global Player", combine recipe 19919. Sets `ench_epic` to `9`.
66. burningwood/"A Sarnak Imitator", say "Chest". Requires `ench_epic` set. Requires `ench_epic` >=3. Gives "Ornate Staff Chest" (52960).
67. Ground spawn of "Taste of Enticement" (52964) in `mistmoore`.
68. frozenshadow/"Advisor Svartmane", hand "Taste of Enticement" (52964). Gives "1st Piece of the Staff" (54289).
69. Loot "2nd Piece of the Staff" (54310) from "The Yrendan Scarab" in `pojustice`.
70. Loot "3rd Piece of the Staff" (54299) from "Chavoor the Trickster" in `vxed`.
71. Loot "3rd Piece of the Staff" (54299) from "Ikaav Firecaller" in `vxed`.
72. Loot "3rd Piece of the Staff" (54299) from "Kyv Hunter" in `vxed`.
73. Loot "3rd Piece of the Staff" (54299) from "Ukun Bloodbeast" in `vxed`.
74. Loot "3rd Piece of the Staff" (54299) from "Umbiki" in `vxed`.
75. Loot "3rd Piece of the Staff" (54299) from "misguided beludu Creque" in `vxed`.
76. Say "War Timer" to bloodfields/"War".
77. Spawns "War Caller Kaavi" (301042).
78. Loot "4th Piece of the Staff" (54284) from "War Caller Kaavi".
79. **Broken:** no event trigger found for `bloodfields/war#timer:reset`.
80. Spawns "War Caller Kaavi" (301042) after `bloodfields/war#timer:reset`.
81. Loot "4th Piece of the Staff" (54284) from "War Caller Kaavi" in `bloodfields`.
82. Loot "Ornate Staff Topper" (52961) from "Faleniel of Darkwater" in `sirens`.
83. Loot "All-Seeing Eye" (54293) from "All-Seeing Eye" in `mischiefplane`.
84. Summon "Black Diamond of Nightmares" (29990) by casting "Imbue Nightmare".
85. poknowledge/"Aid Grimel", say "Versed In The Art Of Smithing". Gives "Filthy Breastplate" (15984).
86. Combine in "Mixing Bowl" (17906): "Celestial Solvent" (9731), "Words of Acquisition (Beza)" (11866). Produces "Celestial Essence" (9650). Requires Baking, trivial 15. The combine does not fail.
87. Combine in "Mixing Bowl" (17906): "Celestial Solvent" (9731), "Words of Burnishing" (11862). Produces "Celestial Essence" (9650). Requires Baking, trivial 15. The combine does not fail.
88. 67 other recipes also produce Celestial Essence (9650).
89. Common item: Jar of Acid (22133). Listed in 15 zones.
90. Combine in Brew Barrel (19): "Celestial Essence" (9650), "Jar of Acid" (22133). Produces "Acid Wash" (15987). Requires Brewing, trivial 151.
91. Combine in Forge (17): "Filthy Breastplate" (15984), "Acid Wash" (15987). Produces "Cleansed Breastplate" (15998). Requires Blacksmithing, trivial 227.
92. Common item: Mortar and Pestle (17904). Listed in 12 zones.
93. No quest step gives Sandstorm Pearl (29909). The dump lists it in bothunder.
94. Combine in "Mortar and Pestle" (17904): "Sandstorm Pearl" (29909). Produces "Powdered Sandstorm Pearl" (29520) x4. Requires Make Poison, trivial 255.
95. Combine in Kiln (22): "Firing Sheet" (16906), "Unfired Mixing Bowl" (16930). Produces "Mixing Bowl" (17906). Requires Pottery, trivial 15.
96. Combine in "Mixing Bowl" (17906): "Sandstorm Pearl" (29909). Produces "Powdered Sandstorm Pearl" (29520) x4. Requires Baking. The combine does not fail.
97. Spawns "a Koka'Vor chieftain" (210236) in `postorms` on event_signal.
98. Loot "Storm Rider Blood" (29526) from "a Koka'Vor chieftain".
99. Loot "Storm Rider Blood" (29526) from "A stormrider" in `bothunder`.
100. Loot "Storm Rider Blood" (29526) from "Dolsoj Warrebs" in `bazaar`.
101. Loot "Storm Rider Blood" (29526) from "a Koka'Vor krovian" in `postorms`.
102. Loot "Storm Rider Blood" (29526) from "a Koka'Vor senvar" in `postorms`.
103. No quest step gives Drop of Pure Rain (29904). The dump lists it in bothunder.
104. Combine in Brew Barrel (19): "Powdered Sandstorm Pearl" (29520), "Storm Rider Blood" (29526), "Drop of Pure Rain" (29904). Produces "Hurricane Temper" (29533). Requires Brewing, trivial 135.
105. Combine in Forge (17): "Cleansed Breastplate" (15998), "Hurricane Temper" (29533). Produces "Tempered Breastplate" (15999). Requires Blacksmithing, trivial 229.
106. Combine in Forge (17): "Black Diamond of Nightmares" (29990), "Tempered Breastplate" (15999). Produces "Imbued Breastplate" (15985). Requires Blacksmithing 220. Trivial at 275.
107. poknowledge/"Aid Grimel", hand "Imbued Breastplate" (15985). Gives "Hardened Leather Signet" (16249).
108. poknowledge/"Aid Grimel", say "Skill In Brewing". Gives "Portable Drink Barrel" (17179).
109. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
110. qeynos/"Wolten Grafe", say "Crush The Undead". Gives "Box For Bones" (17941).
111. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `steamfont`.
112. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `tox`.
113. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `toxxulia`.
114. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
115. toxxulia/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
116. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). The combine does not fail.
117. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
118. qeynos2/"Phin Esrinap", say "Supplies". Gives "Message to Konem" (18921).
119. qeytoqrg/"Konem Matse", hand "Message to Konem" (18921). Gives "Grathin's Invoice" (18922).
120. qeynos2/"Phin Esrinap", hand "Grathin's Invoice" (18922). Gives "Water Flask" (13006).
121. Say "Tm Devrak Death" to rujd/"Rujd".
122. Spawns "spawn chest with Heavy Orcish Prison Key" (245241).
123. Loot "Pod of Water" (13044) from "spawn chest with Heavy Orcish Prison Key".
124. Say "Tm Dokorel Death" to rujd/"Rujd".
125. Say "Tm Velrek Death" to rujd/"Rujd".
126. Say "Researcher Death" to rujg/"Rujg".
127. Spawns "A Barrel" (260015).
128. Loot "Pod of Water" (13044) from "A Barrel".
129. 3 other loot steps also yield Pod of Water (13044).
130. Forage "Pod of Water" (13044) in `ruja`.
131. Forage "Pod of Water" (13044) in `uqua`.
132. Forage "Pod of Water" (13044) in `yxtta`.
133. Combine in Brew Barrel (19): "Bottle of Aged Bloodwine" (51163), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aged Bloodwine" (51164). Requires Brewing, trivial 255.
134. Combine in Brew Barrel (19): "Bottle of Aldo's Bitter Ale" (75805), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aldo's Bitter Ale" (75811). Requires Brewing, trivial 15.
135. 17 other recipes also produce Bottle (16598).
136. Combine in Brew Barrel (19): "Pod of Water" (13044), "Bottle" (16598). Produces "Water Flask" (13006). Requires Brewing, trivial 21.
137. Forage "Dragon Egg" (19139) in `templeveeshan`.
138. Forage "Dragon Egg" (19139) in `westwastes`.
139. Combine in "Portable Drink Barrel" (17179): "Water Flask" (13006), "Dragon Egg" (19139). Produces "Dragon Egg Oil" (9664). Requires Brewing, trivial 150.
140. Loot "Glimmering Oil" (52942) from "A Greasy Clockwork" in `poinnovation`.
141. bazaar/"Caerlyna", hand "Spell Research Kit" (93492). Gives "Spell Research Kit Token" (93667).
142. crescent/"Realnyna", hand "Spell Research Kit" (93492). Gives "Spell Research Kit Token" (93667).
143. bazaar/"Caerlyna", hand "Spell Research Kit Token" (93667). Gives "Spell Research Kit" (93492).
144. crescent/"Realnyna", hand "Spell Research Kit Token" (93667). Gives "Spell Research Kit" (93492).
145. No quest step gives Coalesced Mana (97042). The dump lists it in arcstone, relic, skylance.
146. Combine in Pottery Wheel (21): "Water Flask" (13006), "White Wolf Skin" (13768), "Small Block of Clay" (16900), "Vial Sketch" (16968). Produces "Unfired Poison Vial" (16885). Requires Pottery, trivial 148.
147. Combine in Pottery Wheel (21): "Water Flask" (13006), "Crow's Special Brew" (13799), "Small Block of Clay" (16900), "Vial Sketch" (16968). Produces "Unfired Poison Vial" (16885). Requires Pottery, trivial 148.
148. 19 other recipes also produce Unfired Poison Vial (16885).
149. Common item: High Quality Firing Sheet (16908). Listed in 34 zones.
150. Combine in Kiln (22): "Unfired Poison Vial" (16885), "High Quality Firing Sheet" (16908). Produces "Poison Vial" (16965). Requires Pottery, trivial 17.
151. Kill broodlands/"Brood Drone". Spawns "The Broodqueen" (337254).
152. Loot "Ruby" (10035) from "The Broodqueen".
153. Spawns "A parasitic murkglider" (303121) in `causeway` on event_hp.
154. Loot "Ruby" (10035) from "A parasitic murkglider".
155. Spawns "a Reanimated Berserker" (103093) in `chardok` on enter.
156. Loot "Ruby" (10035) from "a Reanimated Berserker".
157. Kill delvea/"A Drake Egg". Spawns "a Delve spellbinder" (341091).
158. Loot "Ruby" (10035) from "a Delve spellbinder".
159. 116 other loot steps also yield Ruby (10035).
160. Combine in "Spell Research Kit" (93492): "Celestial Essence" (9650), "Coalesced Mana" (97042), "Poison Vial" (16965), "Ruby" (10035). Produces "Vial of Purified Mana" (10254). Requires Research, trivial 200.
161. Forage "Glow Lichen" (14925) in `nektulos`.
162. Common item: Essence of Sunlight (22527). Listed in 8 zones.
163. Ground spawn of "Abysmal Moonwater" (54298) in `abysmal`.
164. Combine in Brew Barrel (19): "Vial of Purified Mana" (10254), "Glow Lichen" (14925), "Essence of Sunlight" (22527), "Abysmal Moonwater" (54298). Produces "Glowing Concoction" (52943). Requires Brewing, trivial 116.
165. Common item: Medicine Bag (17901). Listed in 33 zones.
166. Common item: Glaze Lacquer (29355). Listed in 5 zones.
167. No quest step gives Prism Shard (65469). The dump lists it in crescent, gunthak, poknowledge.
168. Combine in "Medicine Bag" (17901): "Glaze Lacquer" (29355), "Prism Shard" (65469). Produces "Prismatic Dye" (65472). Requires Alchemy, trivial 54.
169. Combine in "Portable Drink Barrel" (17179): "Glaze Lacquer" (29355), "Prism Shard" (65469). Produces "Prismatic Dye" (65472). Requires Brewing, trivial 54.
170. Combine in Brew Barrel (19): "Dragon Egg Oil" (9664), "Glimmering Oil" (52942), "Glowing Concoction" (52943), "Prismatic Dye" (65472). Produces "Incandescent Oil" (57924). Requires Brewing, trivial 116. The combine does not fail.
171. burningwood/"A Sarnak Imitator", say "Hail". Sets `ench_epic` to `1`.
172. burningwood/"A Sarnak Imitator", say "Prepared". Requires `ench_epic` set. Requires `ench_epic` >=1. Gives "Tattered Illegible Tome" (57918).
173. Ground spawn of "Cryptic Page" (52933) in `charasis`.
174. Ground spawn of "Cryptic Page" (52934) in `sebilis`.
175. Ground spawn of "Cryptic Page" (52935) in `cazicthule`.
176. Ground spawn of "Cryptic Page" (52936) in `crystal`.
177. Ground spawn of "Cryptic Page" (52937) in `skyshrine`.
178. Ground spawn of "Cryptic Page" (52938) in `velketor`.
179. Ground spawn of "Cryptic Page" (52939) in `nadox`.
180. Ground spawn of "Cryptic Page" (54308) in `najena`.
181. Ground spawn of "Cryptic Page" (57916) in `fungusgrove`.
182. Ground spawn of "Cryptic Page" (57923) in `oot`.
183. Combine in "Tattered Illegible Tome" (57918): "Cryptic Page" (52933), "Cryptic Page" (52934), "Cryptic Page" (52935), "Cryptic Page" (52936), "Cryptic Page" (52937), "Cryptic Page" (52938), "Cryptic Page" (52939), "Cryptic Page" (54308), "Cryptic Page" (57916), "Cryptic Page" (57923). Produces "Complete Illegible Tome" (54267). The combine does not fail.
184. burningwood/"A Sarnak Imitator", hand "Complete Illegible Tome" (54267). Sets `ench_epic` to `2`.
185. poknowledge/"Grand Librarian Maelin", say "Jeb Lumsed Sent Me". Requires `ench_epic` ==2. Gives "Note to Lobaen" (52950).
186. poknowledge/"Illusionist Lobaen", hand "Note to Lobaen" (52950). Gives "Sealed Documents" (52959).
187. burningwood/"A Sarnak Imitator", hand "Sealed Documents" (52959). Gives "Assembling the Staff" (54286).
188. Loot "Sullied Gold Filigree" (52963) from "An Enticing Potameid" in `natimbi`.
189. hohonora/"Anthone Chapin", hand "Sullied Gold Filigree" (52963). Gives "Purified Gold Filigree" (52953).
190. Combine in "Ornate Staff Chest" (52960): "1st Piece of the Staff" (54289), "2nd Piece of the Staff" (54310), "3rd Piece of the Staff" (54299), "4th Piece of the Staff" (54284), "Ornate Staff Topper" (52961), "All-Seeing Eye" (54293), "Incandescent Oil" (57924), "Purified Gold Filigree" (52953). Produces "Latched Ornate Chest" (52966). The combine does not fail.
191. burningwood/"A Sarnak Imitator", hand "Latched Ornate Chest" (52966). Gives "Oculus of Persuasion" (52952).
192. Hand "Heart of a Twisted Stoneservant" (54239) to wakening/"Alaurin". Spawns "A Luminescent Geonid" (119184). Loot "Luminescent Crystal" (52949) from "A Luminescent Geonid".
193. Loot "Luminescent Crystal" (52949) from "A Luminescent Geonid".
194. wakening/"Alaurin", hand "Luminescent Crystal" (52949). Gives "Purifying Crystal Fragment" (52955).
195. Loot "Volatile Vampyre Blood" (52965) from "a Coterie insatiate" in `tenebrous`.
196. westwastes/"Vohnkare", hand "Volatile Vampyre Blood" (52965). Gives "Purifying Crystal Fragment" (52956).
197. No quest step gives Gnomish Candy (52944). The dump lists it in akanon.
198. No quest step gives Koada`Dal Silk (52948). The dump lists it in felwithea, felwitheb.
199. No quest step gives Feir`Dal Champagne (52940). The dump lists it in gfaydark, katta, rivervale.
200. No quest step gives Dwarven Steel (57921). The dump lists it in kaladima.
201. lfaydark/"A Brownie Noble", hand "Feir'Dal Champagne" (52940) + "Gnomish Candy" (52944) + "Koada'Dal Silk" (52948) + "Dwarven Steel" (57921). Sets `ench_epic` to `8`.
202. Loot "Harnessing Stone" (52946) from "Miriku the Chaotic" in `kael`.
203. lfaydark/"A Brownie Noble", hand "Harnessing Stone" (52946). Requires `ench_epic` ==8. Gives "Purifying Crystal Fragment" (52957).
204. Hand "Mountain Pooka Meat" (54240) to jaggedpine/"Chef Brargus". Spawns "Firwyn" (181226). Loot "Dryad Necklace" (57917) from "Firwyn".
205. Loot "Dryad Necklace" (57917) from "Firwyn".
206. gfaydark/"Feyana Lightwing", hand "Dryad Necklace" (57917). Gives "Purifying Crystal Fragment" (52958).
207. Combine in "Planar Jeweler's Kit" (17764): "Purifying Crystal Fragment" (52955), "Purifying Crystal Fragment" (52956), "Purifying Crystal Fragment" (52957), "Purifying Crystal Fragment" (52958). Produces "Purifying Crystal" (52954). Requires Jewelry Making. The combine does not fail.

### "Channeling Crystal" (57920)

1. global/"Global Player", combine recipe 19919. Sets `ench_epic` to `9`.
2. Loot "Tattered Incantation" (57919) from "Cipheron" in `wallofslaughter`.
3. Loot "Noxious Secretion" (52951) from "Withering Murkglider" in `causeway`.
4. nedaria/"Priestess Rakhu", hand "Noxious Secretion" (52951) + "Tattered Incantation" (57919). Requires `ench_epic` ==9. Gives "Channeling Crystal" (57920).

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
  - Loot "Garudon's Statue" (52941) from "Garudon".

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

- Needs `EnchPre` ==2.
- Needs Staff of the Serpent (10650).
- Needs `ench_epic` unset.
In script order:

1. Sets `ench_epic` to `1`.


How the items are reached:

- Staff of the Serpent (10650)
  - Prerequisite: "Staff of the Serpent" (10650). See section 0.

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

- `ench_epic_pom` set to 1 at mischiefplane/player.
- `ench_epic_sirens` set to 1 at sirens/player.
