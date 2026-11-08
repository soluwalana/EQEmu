# Beastlord

Steps taken from the quest graph only. **Broken** means the graph has no edge for that value or that item.

Flags with writes: `beast_epic`, `bstepic`.

## 0. Prerequisites

Each list is the order you obtain that item. Later steps point here instead of repeating the chain.

### "Decorated Statuette of the Feral" (57059)

1. Common item: Large Sewing Kit (17880). Listed in 39 zones.
2. Spawns "An Ukun Battlehound" (281128) in `qinimi` on event_signal.
3. Loot "Ukun Hide" (67424) from "An Ukun Battlehound".
4. Combine in "Mixing Bowl" (17906): "Celestial Solvent" (9731), "Words of Acquisition (Beza)" (11866). Produces "Celestial Essence" (9650). Requires Baking, trivial 15. The combine does not fail.
5. Combine in "Mixing Bowl" (17906): "Celestial Solvent" (9731), "Words of Burnishing" (11862). Produces "Celestial Essence" (9650). Requires Baking, trivial 15. The combine does not fail.
6. 67 other recipes also produce Celestial Essence (9650).
7. Common item: Jar of Acid (22133). Listed in 15 zones.
8. Combine in Brew Barrel (19): "Celestial Essence" (9650), "Jar of Acid" (22133). Produces "Acid Wash" (15987). Requires Brewing, trivial 151.
9. Combine in Brew Barrel (19): "Ukun Hide" (67424), "Acid Wash" (15987). Produces "Tanned Ukun Leather" (52932). Requires Brewing, trivial 100.
10. Loot "Gem of the Void" (9053) from "Xi Xaui" (NPC 173047) in `maiden`. Drop cache: 6.52% chance per kill.
11. Loot "Chunk of Dense Fungal Padding" (9054) from "A Deepspore Mushroom" (NPC 164041) in `thedeep`. Drop cache: 15.97% chance per kill.
12. Spawns "A Boulder Fiend" (171063) in `thegrey` on enter.
13. Loot "Perfect Acrylia Ore" (9052) from "A Boulder Fiend".
14. 3 alternative loot source(s) also yield Perfect Acrylia Ore (9052).
15. sharvahl/"Weapons Master Rahoul", hand "Perfect Acrylia Ore" (9052) + "Gem of the Void" (9053) + "Chunk of Dense Fungal Padding" (9054). Sets `beast_turnin` to `1`.
16. sharvahl/"Weapons Master Rahoul", say "Adornments". Requires `beast_turnin` ==1. Gives "Adornments Pattern" (57056).
17. Combine in "Large Sewing Kit" (17880): "Tanned Ukun Leather" (52932), "Adornments Pattern" (57056). Produces "Crafted Tassels" (52929). Requires Tailoring, trivial 100.
18. sharvahl/"Weapons Master Rahoul", hand platinum:2000. Gives "Plain Beastlord Statuette" (52931).
19. Combine in "Large Sewing Kit" (17880): "Crafted Tassels" (52929), "Plain Beastlord Statuette" (52931). Produces "Decorated Statuette of the Feral" (57059). Requires Tailoring, trivial 100.

### "Letter from Muada" (57008)

1. cazicthule/"Ikpug Giblod", hand "Letter from Muada" (57008). Sets `beast_epic` to `5`.
2. cazicthule/"Ikpug Giblod", say "Learning". Requires `beast_epic` ==5. Gives "Letter from Muada" (57008).

### "Note to Irionu" (57996)

1. Loot "Darkened Spirit Essence" (57009) from "Frantic Ravenous Beast" in `maiden`.
2. Loot "Disturbed Beast Essence" (57995) from "A Ravenous Nightstalker" in `ponightmare`.
3. sharvahl/"Elder Animist Muada", hand "Darkened Spirit Essence" (57009) + "Disturbed Beast Essence" (57995). Sets `beast_epic` to `7`.
4. sharvahl/"Elder Animist Muada", say "Greater Calling". Requires `beast_epic` ==7. Gives "Note to Irionu" (57996).

### "Sealed Note for Muada" (52900)

1. Loot "Swirling Feral Essence" (57010) from "Delirious Drogmor" in `gunthak`.
2. overthere/"Irionu Bastun", hand "Swirling Feral Essence" (57010). Gives "Sealed Note for Muada" (52900).

### "Ale" (13039)

1. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
2. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `steamfont`.
3. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `tox`.
4. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `toxxulia`.
5. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
6. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). The combine does not fail.
7. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
8. global/"Familiarbrewworks", hand "Water Flask" (13006). Gives "Ale" (13039).

### "Gift of the Sphinx" (52905)

1. Say "Happening" to rathemtn/"Zazamoukh".
2. Spawns "Needs Heading Validation" (50326).
3. Loot "Tarnished Ankh Piece" (52902) from "Needs Heading Validation".
4. rathemtn/"Zazamoukh", hand "Tarnished Ankh Piece" (52902). Gives "Sparkling Silk Scarf" (52904).
5. Hand "Sparkling Silk Scarf" (52904) to rathemtn/"Ankhefenmut". Spawns "Needs Heading Validation" (50327). Loot "Sullied Ankh Piece" (52903) from "Needs Heading Validation".
6. rathemtn/"Ankhefenmut", hand "Sullied Ankh Piece" (52903). Gives "Gift of the Sphinx" (52905).

### "Sealed Response to the Elders" (52908)

1. Say "Happening" to rathemtn/"Zazamoukh".
2. Spawns "Needs Heading Validation" (50326).
3. Loot "Tarnished Ankh Piece" (52902) from "Needs Heading Validation".
4. rathemtn/"Zazamoukh", hand "Tarnished Ankh Piece" (52902). Gives "Sparkling Silk Scarf" (52904).
5. Hand "Sparkling Silk Scarf" (52904) to rathemtn/"Ankhefenmut". Spawns "Needs Heading Validation" (50327). Loot "Sullied Ankh Piece" (52903) from "Needs Heading Validation".
6. rathemtn/"Ankhefenmut", hand "Sullied Ankh Piece" (52903). Gives "Gift of the Sphinx" (52905).
7. sharvahl/"Elder Animist Muada", hand "Gift of the Sphinx" (52905). Sets `beast_epic` to `15`.
8. jaggedpine/"Rashara Wrualla", say "Not Possible". Requires `beast_epic` ==15. Gives "Request of the Elders" (52906).
9. Hand "Request of the Elders" (52906) to draniksscar/"Yerika Sisslak". Spawns "Girplan Spiritleech" (302085). Loot "Rashara's Warder's Essence" (52907) from "Girplan Spiritleech".
10. draniksscar/"Yerika Sisslak", hand "Rashara's Warder's Essence" (52907). Gives "Sealed Response to the Elders" (52908).

### "Wrapped Discordant Totem of the Feral" (52914)

1. Say "Happening" to rathemtn/"Zazamoukh".
2. Spawns "Needs Heading Validation" (50326).
3. Loot "Tarnished Ankh Piece" (52902) from "Needs Heading Validation".
4. rathemtn/"Zazamoukh", hand "Tarnished Ankh Piece" (52902). Gives "Sparkling Silk Scarf" (52904).
5. Hand "Sparkling Silk Scarf" (52904) to rathemtn/"Ankhefenmut". Spawns "Needs Heading Validation" (50327). Loot "Sullied Ankh Piece" (52903) from "Needs Heading Validation".
6. rathemtn/"Ankhefenmut", hand "Sullied Ankh Piece" (52903). Gives "Gift of the Sphinx" (52905).
7. sharvahl/"Elder Animist Muada", hand "Gift of the Sphinx" (52905). Sets `beast_epic` to `15`.
8. jaggedpine/"Rashara Wrualla", say "Not Possible". Requires `beast_epic` ==15. Gives "Request of the Elders" (52906).
9. Hand "Request of the Elders" (52906) to draniksscar/"Yerika Sisslak". Spawns "Girplan Spiritleech" (302085). Loot "Rashara's Warder's Essence" (52907) from "Girplan Spiritleech".
10. draniksscar/"Yerika Sisslak", hand "Rashara's Warder's Essence" (52907). Gives "Sealed Response to the Elders" (52908).
11. jaggedpine/"Rashara Wrualla", hand "Rashara's Warder's Essence" (52907) + "Sealed Response to the Elders" (52908). Sets `beast_epic` to `16`.
12. sharvahl/"Elder Animist Muada", say "Stopped". Requires `beast_epic` ==16. Gives "Elder Cloak of Resilience" (52909).
13. Hand "Elder Cloak of Resilience" (52909) to dranik/"Erana Farrel". Spawns "Discordling Dark Animist" (336126). Loot "Discordant Totem of the Feral" (52910) from "Discordling Dark Animist".
14. dranik/"Erana Farrel", hand "Discordant Totem of the Feral" (52910). Gives "Wrapped Discordant Totem of the Feral" (52914).

### "Claw of the Savage Spirit" (8495)

1. Spawns "Arcanist Ukigit" (167661) in `grimling` on event_signal.
2. Loot "Copper Medal of War" (4393) from "Arcanist Ukigit".
3. sharvahl/"Elder Animist Dumul", hand "Copper Medal of War" (4393). Gives "Carved Wooden Chest" (17361).
4. Hand "Official Seal of the Khati Sha" (9031) to emeraldjungle/"Scout Vyrak". Spawns "The Spirit of Rage" (94126). Loot "Totem of the Gorilla" (9038) from "The Spirit of Rage".
5. emeraldjungle/"Scout Vyrak", hand "Totem of the Gorilla" (9038). Gives "Official Seal of the Khati Sha" (9031).
6. Hand "Official Seal of the Khati Sha" (9031) to feerrott/"Scout Ahlikal". Spawns "The Spirit of Decay" (47205). Loot "Totem of the Spider" (9032) from "The Spirit of Decay".
7. feerrott/"Scout Ahlikal", hand "Totem of the Spider" (9032). Gives "Wrapped Spider Totem" (9033).
8. Hand "Official Seal of the Khati Sha" (9031) to lfaydark/"Scout Rahjiq". Spawns "The Spirit of Malevolence" (57119). Loot "Totem of the Wolf" (9034) from "The Spirit of Malevolence".
9. lfaydark/"Scout Rahjiq", hand "Totem of the Wolf" (9034). Gives "Wrapped Wolf Totem" (9035).
10. Hand "Official Seal of the Khati Sha" (9031) to permafrost/"Scout Janomin". Spawns "The Icebound Spirit" (73107). Loot "Totem of the Ice Bear" (9036) from "The Icebound Spirit".
11. permafrost/"Scout Janomin", hand "Totem of the Ice Bear" (9036). Gives "Wrapped Ice Bear Totem" (9037).
12. emeraldjungle/"Scout Vyrak", hand "Totem of the Gorilla" (9038). Gives "Wrapped Gorilla Totem" (9039).
13. Hand "Official Seal of the Khati Sha" (9031) to stonebrunt/"Scout Malom". Spawns "The Spirit of Torment" (100220). Loot "Totem of the Watcher" (9040) from "The Spirit of Torment".
14. stonebrunt/"Scout Malom", hand "Totem of the Watcher" (9040). Gives "Wrapped Watcher Totem" (9041).
15. Hand "Official Seal of the Khati Sha" (9031) to swampofnohope/"Scout Eyru". Spawns "The Spirit of Sorrow" (83244). Loot "Totem of the Alligator" (9042) from "The Spirit of Sorrow".
16. swampofnohope/"Scout Eyru", hand "Totem of the Alligator" (9042). Gives "Wrapped Alligator Totem" (9043).
17. Combine in "Carved Wooden Chest" (17361): "Wrapped Spider Totem" (9033), "Wrapped Wolf Totem" (9035), "Wrapped Ice Bear Totem" (9037), "Wrapped Gorilla Totem" (9039), "Wrapped Watcher Totem" (9041), "Wrapped Alligator Totem" (9043). Produces "Sealed Box of Totems" (9044). The combine does not fail.
18. sharvahl/"Elder Animist Dumul", hand "Sealed Box of Totems" (9044). Gives "Seal of Elder Dumul" (9045).
19. timorous/"Scout Sihmoj", hand "Seal of Elder Dumul" (9045). Gives "Black Silk Sack" (17360).
20. Kill timorous/"Draz Nurakk". Spawns "Draz Nurakks Image" (96322).
21. Loot "Shards of Broken Glass" (9046) from "Draz Nurakks Image".
22. Combine in "Black Silk Sack" (17360): "Shards of Broken Glass" (9046). Produces "Sack of Broken Glass" (9047). The combine does not fail.
23. timorous/"Scout Sihmoj", hand "Sack of Broken Glass" (9047). Gives "Sack of Broken Glass" (9048).
24. sharvahl/"Elder Animist Dumul", hand "Sack of Broken Glass" (9048). Gives "Note for Historian Qua" (9049).
25. sharvahl/"Arms Historian Qua", hand "Note for Historian Qua" (9049). Gives "Qua's Receipt" (9050).
26. sharvahl/"Weapons Master Rahoul", hand "Qua's Receipt" (9050). Gives "Rahoul's Collection Box" (17363).
27. Loot "Gem of the Void" (9053) from "Xi Xaui" (NPC 173047) in `maiden`. Drop cache: 6.52% chance per kill.
28. Spawns "A Boulder Fiend" (171063) in `thegrey` on enter.
29. Loot "Perfect Acrylia Ore" (9052) from "A Boulder Fiend".
30. 3 alternative loot source(s) also yield Perfect Acrylia Ore (9052).
31. Loot "Chunk of Dense Fungal Padding" (9054) from "A Deepspore Mushroom" (NPC 164041) in `thedeep`. Drop cache: 15.97% chance per kill.
32. Combine in "Rahoul's Collection Box" (17363): "Gem of the Void" (9053), "Perfect Acrylia Ore" (9052), "Chunk of Dense Fungal Padding" (9054). Produces "Sealed Collection Box" (9051). The combine does not fail.
33. sharvahl/"Weapons Master Rahoul", hand "Sealed Collection Box" (9051). Gives "Jagged Claw of Rending" (9055).
34. sharvahl/"Weapons Master Rahoul", hand "Sealed Collection Box" (9051). Gives "Jagged Claw of Rending" (9056).
35. sharvahl/"Elder Animist Dumul", hand "Jagged Claw of Rending" (9055) + "Jagged Claw of Rending" (9056). Gives "Acrylia Gilded Box" (17362).
36. sharvahl/"Elder Animist Dumul", hand "Jagged Claw of Rending" (9055) + "Jagged Claw of Rending" (9056). Gives "Khati Sha Seal of War" (9057).
37. Hand "Khati Sha Seal of War" (9057) to fungusgrove/"Scout Halmia". Spawns "Draz Nurakk" (157116). Loot "Draz Nurakk's Head" (9059) from "Draz Nurakk".
38. fungusgrove/"Scout Halmia", hand "Khati Sha Seal of War" (9057). Gives "Khati Sha Seal of War" (9062).
39. Combine in "Acrylia Gilded Box" (17362): "Jagged Claw of Rending" (9055), "Jagged Claw of Rending" (9056), "Draz Nurakk's Head" (9059), "Khati Sha Seal of War" (9062). Produces "Sealed Gilded Wooden Chest" (9060). The combine does not fail.
40. sharvahl/"Elder Animist Dumul", hand "Sealed Gilded Wooden Chest" (9060). Gives "Claw of the Savage Spirit" (8495).

### "Claw of the Savage Spirit" (8496)

1. Spawns "Arcanist Ukigit" (167661) in `grimling` on event_signal.
2. Loot "Copper Medal of War" (4393) from "Arcanist Ukigit".
3. sharvahl/"Elder Animist Dumul", hand "Copper Medal of War" (4393). Gives "Carved Wooden Chest" (17361).
4. Hand "Official Seal of the Khati Sha" (9031) to emeraldjungle/"Scout Vyrak". Spawns "The Spirit of Rage" (94126). Loot "Totem of the Gorilla" (9038) from "The Spirit of Rage".
5. emeraldjungle/"Scout Vyrak", hand "Totem of the Gorilla" (9038). Gives "Official Seal of the Khati Sha" (9031).
6. Hand "Official Seal of the Khati Sha" (9031) to feerrott/"Scout Ahlikal". Spawns "The Spirit of Decay" (47205). Loot "Totem of the Spider" (9032) from "The Spirit of Decay".
7. feerrott/"Scout Ahlikal", hand "Totem of the Spider" (9032). Gives "Wrapped Spider Totem" (9033).
8. Hand "Official Seal of the Khati Sha" (9031) to lfaydark/"Scout Rahjiq". Spawns "The Spirit of Malevolence" (57119). Loot "Totem of the Wolf" (9034) from "The Spirit of Malevolence".
9. lfaydark/"Scout Rahjiq", hand "Totem of the Wolf" (9034). Gives "Wrapped Wolf Totem" (9035).
10. Hand "Official Seal of the Khati Sha" (9031) to permafrost/"Scout Janomin". Spawns "The Icebound Spirit" (73107). Loot "Totem of the Ice Bear" (9036) from "The Icebound Spirit".
11. permafrost/"Scout Janomin", hand "Totem of the Ice Bear" (9036). Gives "Wrapped Ice Bear Totem" (9037).
12. emeraldjungle/"Scout Vyrak", hand "Totem of the Gorilla" (9038). Gives "Wrapped Gorilla Totem" (9039).
13. Hand "Official Seal of the Khati Sha" (9031) to stonebrunt/"Scout Malom". Spawns "The Spirit of Torment" (100220). Loot "Totem of the Watcher" (9040) from "The Spirit of Torment".
14. stonebrunt/"Scout Malom", hand "Totem of the Watcher" (9040). Gives "Wrapped Watcher Totem" (9041).
15. Hand "Official Seal of the Khati Sha" (9031) to swampofnohope/"Scout Eyru". Spawns "The Spirit of Sorrow" (83244). Loot "Totem of the Alligator" (9042) from "The Spirit of Sorrow".
16. swampofnohope/"Scout Eyru", hand "Totem of the Alligator" (9042). Gives "Wrapped Alligator Totem" (9043).
17. Combine in "Carved Wooden Chest" (17361): "Wrapped Spider Totem" (9033), "Wrapped Wolf Totem" (9035), "Wrapped Ice Bear Totem" (9037), "Wrapped Gorilla Totem" (9039), "Wrapped Watcher Totem" (9041), "Wrapped Alligator Totem" (9043). Produces "Sealed Box of Totems" (9044). The combine does not fail.
18. sharvahl/"Elder Animist Dumul", hand "Sealed Box of Totems" (9044). Gives "Seal of Elder Dumul" (9045).
19. timorous/"Scout Sihmoj", hand "Seal of Elder Dumul" (9045). Gives "Black Silk Sack" (17360).
20. Kill timorous/"Draz Nurakk". Spawns "Draz Nurakks Image" (96322).
21. Loot "Shards of Broken Glass" (9046) from "Draz Nurakks Image".
22. Combine in "Black Silk Sack" (17360): "Shards of Broken Glass" (9046). Produces "Sack of Broken Glass" (9047). The combine does not fail.
23. timorous/"Scout Sihmoj", hand "Sack of Broken Glass" (9047). Gives "Sack of Broken Glass" (9048).
24. sharvahl/"Elder Animist Dumul", hand "Sack of Broken Glass" (9048). Gives "Note for Historian Qua" (9049).
25. sharvahl/"Arms Historian Qua", hand "Note for Historian Qua" (9049). Gives "Qua's Receipt" (9050).
26. sharvahl/"Weapons Master Rahoul", hand "Qua's Receipt" (9050). Gives "Rahoul's Collection Box" (17363).
27. Loot "Gem of the Void" (9053) from "Xi Xaui" (NPC 173047) in `maiden`. Drop cache: 6.52% chance per kill.
28. Spawns "A Boulder Fiend" (171063) in `thegrey` on enter.
29. Loot "Perfect Acrylia Ore" (9052) from "A Boulder Fiend".
30. 3 alternative loot source(s) also yield Perfect Acrylia Ore (9052).
31. Loot "Chunk of Dense Fungal Padding" (9054) from "A Deepspore Mushroom" (NPC 164041) in `thedeep`. Drop cache: 15.97% chance per kill.
32. Combine in "Rahoul's Collection Box" (17363): "Gem of the Void" (9053), "Perfect Acrylia Ore" (9052), "Chunk of Dense Fungal Padding" (9054). Produces "Sealed Collection Box" (9051). The combine does not fail.
33. sharvahl/"Weapons Master Rahoul", hand "Sealed Collection Box" (9051). Gives "Jagged Claw of Rending" (9055).
34. sharvahl/"Weapons Master Rahoul", hand "Sealed Collection Box" (9051). Gives "Jagged Claw of Rending" (9056).
35. sharvahl/"Elder Animist Dumul", hand "Jagged Claw of Rending" (9055) + "Jagged Claw of Rending" (9056). Gives "Acrylia Gilded Box" (17362).
36. sharvahl/"Elder Animist Dumul", hand "Jagged Claw of Rending" (9055) + "Jagged Claw of Rending" (9056). Gives "Khati Sha Seal of War" (9057).
37. Hand "Khati Sha Seal of War" (9057) to fungusgrove/"Scout Halmia". Spawns "Draz Nurakk" (157116). Loot "Draz Nurakk's Head" (9059) from "Draz Nurakk".
38. fungusgrove/"Scout Halmia", hand "Khati Sha Seal of War" (9057). Gives "Khati Sha Seal of War" (9062).
39. Combine in "Acrylia Gilded Box" (17362): "Jagged Claw of Rending" (9055), "Jagged Claw of Rending" (9056), "Draz Nurakk's Head" (9059), "Khati Sha Seal of War" (9062). Produces "Sealed Gilded Wooden Chest" (9060). The combine does not fail.
40. sharvahl/"Elder Animist Dumul", hand "Sealed Gilded Wooden Chest" (9060). Gives "Claw of the Savage Spirit" (8496).

### "Spiritbound Totem" (57027)

1. Say "Happening" to rathemtn/"Zazamoukh".
2. Spawns "Needs Heading Validation" (50326).
3. Loot "Tarnished Ankh Piece" (52902) from "Needs Heading Validation".
4. rathemtn/"Zazamoukh", hand "Tarnished Ankh Piece" (52902). Gives "Sparkling Silk Scarf" (52904).
5. Hand "Sparkling Silk Scarf" (52904) to rathemtn/"Ankhefenmut". Spawns "Needs Heading Validation" (50327). Loot "Sullied Ankh Piece" (52903) from "Needs Heading Validation".
6. rathemtn/"Ankhefenmut", hand "Sullied Ankh Piece" (52903). Gives "Gift of the Sphinx" (52905).
7. sharvahl/"Elder Animist Muada", hand "Gift of the Sphinx" (52905). Sets `beast_epic` to `15`.
8. jaggedpine/"Rashara Wrualla", say "Not Possible". Requires `beast_epic` ==15. Gives "Request of the Elders" (52906).
9. Hand "Request of the Elders" (52906) to draniksscar/"Yerika Sisslak". Spawns "Girplan Spiritleech" (302085). Loot "Rashara's Warder's Essence" (52907) from "Girplan Spiritleech".
10. draniksscar/"Yerika Sisslak", hand "Rashara's Warder's Essence" (52907). Gives "Sealed Response to the Elders" (52908).
11. jaggedpine/"Rashara Wrualla", hand "Rashara's Warder's Essence" (52907) + "Sealed Response to the Elders" (52908). Sets `beast_epic` to `16`.
12. sharvahl/"Elder Animist Muada", say "Stopped". Requires `beast_epic` ==16. Gives "Elder Cloak of Resilience" (52909).
13. Hand "Elder Cloak of Resilience" (52909) to dranik/"Erana Farrel". Spawns "Discordling Dark Animist" (336126). Loot "Discordant Totem of the Feral" (52910) from "Discordling Dark Animist".
14. dranik/"Erana Farrel", hand "Discordant Totem of the Feral" (52910). Gives "Wrapped Discordant Totem of the Feral" (52914).
15. sharvahl/"Elder Animist Muada", hand "Wrapped Discordant Totem of the Feral" (52914). Sets `beast_epic` to `17`.
16. Say "End The Threat In The Grimling Forest" to grimling/"Scout Husman".
17. Spawns "Grimling Colonel" (167426).
18. Loot "Eerie Medallion" (57025) from "Grimling Colonel".
19. 1 alternative loot source(s) also yield Eerie Medallion (57025).
20. Say "Hail" to jaggedpine/"Rashara Wrualla".
21. Spawns "Dismal Darkpaw Mystic" (181225).
22. Loot "Scalding Blood" (57058) from "Dismal Darkpaw Mystic".
23. Loot "Fierce Spirit Clay" (57020) from "Spiritfrenzied Phoenix" in `poair`.
24. sharvahl/"Elder Animist Muada", say "Make The Totem". Requires `beast_epic` ==17. Gives "Elders' Totem Mold" (52930).
25. sharvahl/"Elder Animist Muada", say "Task". Requires `beast_epic` ==17. Gives "Peculiar Unshapen Piece of Wood" (57011).
26. Combine in Kiln (22): "Fierce Spirit Clay" (57020), "Eerie Medallion" (57025), "Scalding Blood" (57058). Produces "Gilded Resonating Clay" (57029). Requires Pottery 100. The combine does not fail.
27. sharvahl/"Elder Animist Muada", say "Make The Totem". Requires `beast_epic` ==17. Gives "Combined Essence" (52913).
28. Combine in Oven (15): "Peculiar Unshapen Piece of Wood" (57011), "Gilded Resonating Clay" (57029), "Combined Essence" (52913). Produces "Malleable Glowing Totem" (57050). Requires Baking 100. The combine does not fail.
29. Combine in Forge (17): "Elders' Totem Mold" (52930), "Malleable Glowing Totem" (57050). Produces "Spiritbound Totem" (57027). Requires Blacksmithing 100. The combine does not fail.

### "Blended Elixir of Fortitude" (57051)

1. Say "Happening" to rathemtn/"Zazamoukh".
2. Spawns "Needs Heading Validation" (50326).
3. Loot "Tarnished Ankh Piece" (52902) from "Needs Heading Validation".
4. rathemtn/"Zazamoukh", hand "Tarnished Ankh Piece" (52902). Gives "Sparkling Silk Scarf" (52904).
5. Hand "Sparkling Silk Scarf" (52904) to rathemtn/"Ankhefenmut". Spawns "Needs Heading Validation" (50327). Loot "Sullied Ankh Piece" (52903) from "Needs Heading Validation".
6. rathemtn/"Ankhefenmut", hand "Sullied Ankh Piece" (52903). Gives "Gift of the Sphinx" (52905).
7. sharvahl/"Elder Animist Muada", hand "Gift of the Sphinx" (52905). Sets `beast_epic` to `15`.
8. jaggedpine/"Rashara Wrualla", say "Not Possible". Requires `beast_epic` ==15. Gives "Request of the Elders" (52906).
9. Hand "Request of the Elders" (52906) to draniksscar/"Yerika Sisslak". Spawns "Girplan Spiritleech" (302085). Loot "Rashara's Warder's Essence" (52907) from "Girplan Spiritleech".
10. draniksscar/"Yerika Sisslak", hand "Rashara's Warder's Essence" (52907). Gives "Sealed Response to the Elders" (52908).
11. jaggedpine/"Rashara Wrualla", hand "Rashara's Warder's Essence" (52907) + "Sealed Response to the Elders" (52908). Sets `beast_epic` to `16`.
12. sharvahl/"Elder Animist Muada", say "Stopped". Requires `beast_epic` ==16. Gives "Elder Cloak of Resilience" (52909).
13. Hand "Elder Cloak of Resilience" (52909) to dranik/"Erana Farrel". Spawns "Discordling Dark Animist" (336126). Loot "Discordant Totem of the Feral" (52910) from "Discordling Dark Animist".
14. dranik/"Erana Farrel", hand "Discordant Totem of the Feral" (52910). Gives "Wrapped Discordant Totem of the Feral" (52914).
15. sharvahl/"Elder Animist Muada", hand "Wrapped Discordant Totem of the Feral" (52914). Sets `beast_epic` to `17`.
16. Say "End The Threat In The Grimling Forest" to grimling/"Scout Husman".
17. Spawns "Grimling Colonel" (167426).
18. Loot "Eerie Medallion" (57025) from "Grimling Colonel".
19. 1 alternative loot source(s) also yield Eerie Medallion (57025).
20. Say "Hail" to jaggedpine/"Rashara Wrualla".
21. Spawns "Dismal Darkpaw Mystic" (181225).
22. Loot "Scalding Blood" (57058) from "Dismal Darkpaw Mystic".
23. Loot "Fierce Spirit Clay" (57020) from "Spiritfrenzied Phoenix" in `poair`.
24. sharvahl/"Elder Animist Muada", say "Make The Totem". Requires `beast_epic` ==17. Gives "Elders' Totem Mold" (52930).
25. sharvahl/"Elder Animist Muada", say "Task". Requires `beast_epic` ==17. Gives "Peculiar Unshapen Piece of Wood" (57011).
26. Combine in Kiln (22): "Fierce Spirit Clay" (57020), "Eerie Medallion" (57025), "Scalding Blood" (57058). Produces "Gilded Resonating Clay" (57029). Requires Pottery 100. The combine does not fail.
27. sharvahl/"Elder Animist Muada", say "Make The Totem". Requires `beast_epic` ==17. Gives "Combined Essence" (52913).
28. Combine in Oven (15): "Peculiar Unshapen Piece of Wood" (57011), "Gilded Resonating Clay" (57029), "Combined Essence" (52913). Produces "Malleable Glowing Totem" (57050). Requires Baking 100. The combine does not fail.
29. Combine in Forge (17): "Elders' Totem Mold" (52930), "Malleable Glowing Totem" (57050). Produces "Spiritbound Totem" (57027). Requires Blacksmithing 100. The combine does not fail.
30. sharvahl/"Elder Animist Muada", say "Trapped Spirits". Sets `beast_epic` to `18`.
31. Kill causeway/"Bazu Terror". Spawns "Discordling Dark Animist" (303094).
32. Loot "Dark Animist Wand" (57012) from "Discordling Dark Animist".
33. causeway/"Jillaa Oogblat", hand "Dark Animist Wand" (57012). Sets `beast_epic` to `19`.
34. sharvahl/"Elder Animist Muada", say "Agree To Take On This Charge". Requires `beast_epic` ==19. Gives "Blended Elixir of Fortitude" (57051).

### "Wrapped Gemmed Wand" (57052)

1. Say "Happening" to rathemtn/"Zazamoukh".
2. Spawns "Needs Heading Validation" (50326).
3. Loot "Tarnished Ankh Piece" (52902) from "Needs Heading Validation".
4. rathemtn/"Zazamoukh", hand "Tarnished Ankh Piece" (52902). Gives "Sparkling Silk Scarf" (52904).
5. Hand "Sparkling Silk Scarf" (52904) to rathemtn/"Ankhefenmut". Spawns "Needs Heading Validation" (50327). Loot "Sullied Ankh Piece" (52903) from "Needs Heading Validation".
6. rathemtn/"Ankhefenmut", hand "Sullied Ankh Piece" (52903). Gives "Gift of the Sphinx" (52905).
7. sharvahl/"Elder Animist Muada", hand "Gift of the Sphinx" (52905). Sets `beast_epic` to `15`.
8. jaggedpine/"Rashara Wrualla", say "Not Possible". Requires `beast_epic` ==15. Gives "Request of the Elders" (52906).
9. Hand "Request of the Elders" (52906) to draniksscar/"Yerika Sisslak". Spawns "Girplan Spiritleech" (302085). Loot "Rashara's Warder's Essence" (52907) from "Girplan Spiritleech".
10. draniksscar/"Yerika Sisslak", hand "Rashara's Warder's Essence" (52907). Gives "Sealed Response to the Elders" (52908).
11. jaggedpine/"Rashara Wrualla", hand "Rashara's Warder's Essence" (52907) + "Sealed Response to the Elders" (52908). Sets `beast_epic` to `16`.
12. sharvahl/"Elder Animist Muada", say "Stopped". Requires `beast_epic` ==16. Gives "Elder Cloak of Resilience" (52909).
13. Hand "Elder Cloak of Resilience" (52909) to dranik/"Erana Farrel". Spawns "Discordling Dark Animist" (336126). Loot "Discordant Totem of the Feral" (52910) from "Discordling Dark Animist".
14. dranik/"Erana Farrel", hand "Discordant Totem of the Feral" (52910). Gives "Wrapped Discordant Totem of the Feral" (52914).
15. sharvahl/"Elder Animist Muada", hand "Wrapped Discordant Totem of the Feral" (52914). Sets `beast_epic` to `17`.
16. Say "End The Threat In The Grimling Forest" to grimling/"Scout Husman".
17. Spawns "Grimling Colonel" (167426).
18. Loot "Eerie Medallion" (57025) from "Grimling Colonel".
19. 1 alternative loot source(s) also yield Eerie Medallion (57025).
20. Say "Hail" to jaggedpine/"Rashara Wrualla".
21. Spawns "Dismal Darkpaw Mystic" (181225).
22. Loot "Scalding Blood" (57058) from "Dismal Darkpaw Mystic".
23. Loot "Fierce Spirit Clay" (57020) from "Spiritfrenzied Phoenix" in `poair`.
24. sharvahl/"Elder Animist Muada", say "Make The Totem". Requires `beast_epic` ==17. Gives "Elders' Totem Mold" (52930).
25. sharvahl/"Elder Animist Muada", say "Task". Requires `beast_epic` ==17. Gives "Peculiar Unshapen Piece of Wood" (57011).
26. Combine in Kiln (22): "Fierce Spirit Clay" (57020), "Eerie Medallion" (57025), "Scalding Blood" (57058). Produces "Gilded Resonating Clay" (57029). Requires Pottery 100. The combine does not fail.
27. sharvahl/"Elder Animist Muada", say "Make The Totem". Requires `beast_epic` ==17. Gives "Combined Essence" (52913).
28. Combine in Oven (15): "Peculiar Unshapen Piece of Wood" (57011), "Gilded Resonating Clay" (57029), "Combined Essence" (52913). Produces "Malleable Glowing Totem" (57050). Requires Baking 100. The combine does not fail.
29. Combine in Forge (17): "Elders' Totem Mold" (52930), "Malleable Glowing Totem" (57050). Produces "Spiritbound Totem" (57027). Requires Blacksmithing 100. The combine does not fail.
30. sharvahl/"Elder Animist Muada", say "Trapped Spirits". Sets `beast_epic` to `18`.
31. Kill causeway/"Bazu Terror". Spawns "Discordling Dark Animist" (303094).
32. Loot "Dark Animist Wand" (57012) from "Discordling Dark Animist".
33. causeway/"Jillaa Oogblat", hand "Dark Animist Wand" (57012). Sets `beast_epic` to `19`.
34. sharvahl/"Elder Animist Muada", say "Agree To Take On This Charge". Requires `beast_epic` ==19. Gives "Blended Elixir of Fortitude" (57051).
35. causeway/"Jillaa Oogblat", hand "Blended Elixir of Fortitude" (57051). Sets `beast_epic` to `20`.
36. Say "Strong" to bloodfields/"Tormented Scout".
37. Spawns "DDA" (301069).
38. Loot "Gemmed Dark Animist Wand" (57014) from "DDA".
39. bloodfields/"Tormented Scout", hand "Gemmed Dark Animist Wand" (57014). Gives "Wrapped Gemmed Wand" (57052).

### "Savage Lord's Totem" (52911)

1. Say "Happening" to rathemtn/"Zazamoukh".
2. Spawns "Needs Heading Validation" (50326).
3. Loot "Tarnished Ankh Piece" (52902) from "Needs Heading Validation".
4. rathemtn/"Zazamoukh", hand "Tarnished Ankh Piece" (52902). Gives "Sparkling Silk Scarf" (52904).
5. Hand "Sparkling Silk Scarf" (52904) to rathemtn/"Ankhefenmut". Spawns "Needs Heading Validation" (50327). Loot "Sullied Ankh Piece" (52903) from "Needs Heading Validation".
6. rathemtn/"Ankhefenmut", hand "Sullied Ankh Piece" (52903). Gives "Gift of the Sphinx" (52905).
7. sharvahl/"Elder Animist Muada", hand "Gift of the Sphinx" (52905). Sets `beast_epic` to `15`.
8. jaggedpine/"Rashara Wrualla", say "Not Possible". Requires `beast_epic` ==15. Gives "Request of the Elders" (52906).
9. Hand "Request of the Elders" (52906) to draniksscar/"Yerika Sisslak". Spawns "Girplan Spiritleech" (302085). Loot "Rashara's Warder's Essence" (52907) from "Girplan Spiritleech".
10. draniksscar/"Yerika Sisslak", hand "Rashara's Warder's Essence" (52907). Gives "Sealed Response to the Elders" (52908).
11. jaggedpine/"Rashara Wrualla", hand "Rashara's Warder's Essence" (52907) + "Sealed Response to the Elders" (52908). Sets `beast_epic` to `16`.
12. sharvahl/"Elder Animist Muada", say "Stopped". Requires `beast_epic` ==16. Gives "Elder Cloak of Resilience" (52909).
13. Hand "Elder Cloak of Resilience" (52909) to dranik/"Erana Farrel". Spawns "Discordling Dark Animist" (336126). Loot "Discordant Totem of the Feral" (52910) from "Discordling Dark Animist".
14. dranik/"Erana Farrel", hand "Discordant Totem of the Feral" (52910). Gives "Wrapped Discordant Totem of the Feral" (52914).
15. sharvahl/"Elder Animist Muada", hand "Wrapped Discordant Totem of the Feral" (52914). Gives "Savage Lord's Totem" (52911).

### "Sealed Letter from Muada" (57053)

1. Say "Happening" to rathemtn/"Zazamoukh".
2. Spawns "Needs Heading Validation" (50326).
3. Loot "Tarnished Ankh Piece" (52902) from "Needs Heading Validation".
4. rathemtn/"Zazamoukh", hand "Tarnished Ankh Piece" (52902). Gives "Sparkling Silk Scarf" (52904).
5. Hand "Sparkling Silk Scarf" (52904) to rathemtn/"Ankhefenmut". Spawns "Needs Heading Validation" (50327). Loot "Sullied Ankh Piece" (52903) from "Needs Heading Validation".
6. rathemtn/"Ankhefenmut", hand "Sullied Ankh Piece" (52903). Gives "Gift of the Sphinx" (52905).
7. sharvahl/"Elder Animist Muada", hand "Gift of the Sphinx" (52905). Sets `beast_epic` to `15`.
8. jaggedpine/"Rashara Wrualla", say "Not Possible". Requires `beast_epic` ==15. Gives "Request of the Elders" (52906).
9. Hand "Request of the Elders" (52906) to draniksscar/"Yerika Sisslak". Spawns "Girplan Spiritleech" (302085). Loot "Rashara's Warder's Essence" (52907) from "Girplan Spiritleech".
10. draniksscar/"Yerika Sisslak", hand "Rashara's Warder's Essence" (52907). Gives "Sealed Response to the Elders" (52908).
11. jaggedpine/"Rashara Wrualla", hand "Rashara's Warder's Essence" (52907) + "Sealed Response to the Elders" (52908). Sets `beast_epic` to `16`.
12. sharvahl/"Elder Animist Muada", say "Stopped". Requires `beast_epic` ==16. Gives "Elder Cloak of Resilience" (52909).
13. Hand "Elder Cloak of Resilience" (52909) to dranik/"Erana Farrel". Spawns "Discordling Dark Animist" (336126). Loot "Discordant Totem of the Feral" (52910) from "Discordling Dark Animist".
14. dranik/"Erana Farrel", hand "Discordant Totem of the Feral" (52910). Gives "Wrapped Discordant Totem of the Feral" (52914).
15. sharvahl/"Elder Animist Muada", hand "Wrapped Discordant Totem of the Feral" (52914). Sets `beast_epic` to `17`.
16. Say "End The Threat In The Grimling Forest" to grimling/"Scout Husman".
17. Spawns "Grimling Colonel" (167426).
18. Loot "Eerie Medallion" (57025) from "Grimling Colonel".
19. 1 alternative loot source(s) also yield Eerie Medallion (57025).
20. Say "Hail" to jaggedpine/"Rashara Wrualla".
21. Spawns "Dismal Darkpaw Mystic" (181225).
22. Loot "Scalding Blood" (57058) from "Dismal Darkpaw Mystic".
23. Loot "Fierce Spirit Clay" (57020) from "Spiritfrenzied Phoenix" in `poair`.
24. sharvahl/"Elder Animist Muada", say "Make The Totem". Requires `beast_epic` ==17. Gives "Elders' Totem Mold" (52930).
25. sharvahl/"Elder Animist Muada", say "Task". Requires `beast_epic` ==17. Gives "Peculiar Unshapen Piece of Wood" (57011).
26. Combine in Kiln (22): "Fierce Spirit Clay" (57020), "Eerie Medallion" (57025), "Scalding Blood" (57058). Produces "Gilded Resonating Clay" (57029). Requires Pottery 100. The combine does not fail.
27. sharvahl/"Elder Animist Muada", say "Make The Totem". Requires `beast_epic` ==17. Gives "Combined Essence" (52913).
28. Combine in Oven (15): "Peculiar Unshapen Piece of Wood" (57011), "Gilded Resonating Clay" (57029), "Combined Essence" (52913). Produces "Malleable Glowing Totem" (57050). Requires Baking 100. The combine does not fail.
29. Combine in Forge (17): "Elders' Totem Mold" (52930), "Malleable Glowing Totem" (57050). Produces "Spiritbound Totem" (57027). Requires Blacksmithing 100. The combine does not fail.
30. sharvahl/"Elder Animist Muada", say "Trapped Spirits". Sets `beast_epic` to `18`.
31. Kill causeway/"Bazu Terror". Spawns "Discordling Dark Animist" (303094).
32. Loot "Dark Animist Wand" (57012) from "Discordling Dark Animist".
33. causeway/"Jillaa Oogblat", hand "Dark Animist Wand" (57012). Sets `beast_epic` to `19`.
34. sharvahl/"Elder Animist Muada", say "Agree To Take On This Charge". Requires `beast_epic` ==19. Gives "Blended Elixir of Fortitude" (57051).
35. causeway/"Jillaa Oogblat", hand "Blended Elixir of Fortitude" (57051). Sets `beast_epic` to `20`.
36. Say "Strong" to bloodfields/"Tormented Scout".
37. Spawns "DDA" (301069).
38. Loot "Gemmed Dark Animist Wand" (57014) from "DDA".
39. bloodfields/"Tormented Scout", hand "Gemmed Dark Animist Wand" (57014). Gives "Wrapped Gemmed Wand" (57052).
40. sharvahl/"Elder Animist Muada", hand "Wrapped Gemmed Wand" (57052). Sets `beast_epic` to `21`.
41. Say "Check Lorb" to anguish/"Zone Status".
42. Spawns "Orb of Discordant Energy" (317087).
43. Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy".
44. 4 alternative loot source(s) also yield Globe of Discordant Energy (47100).
45. sharvahl/"Elder Animist Muada", hand "Globe of Discordant Energy" (47100) + "Spiritbound Totem" (57027). Requires `beast_epic` ==21. Gives "Sealed Letter from Muada" (57053).

## `beast_epic`

Values written: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23.

### 1. elder animist muada — hand 57059

Zone: `sharvahl`.

Sets `beast_epic` to `1`.

- Needs `beast_epic` unset.
- Turn in x1: Decorated Statuette of the Feral (57059).
In script order:

1. Sets `beast_epic` to `1`.


How the items are reached:

- Decorated Statuette of the Feral (57059)
  - Prerequisite: "Decorated Statuette of the Feral" (57059). See section 0.

### 2. marrey mcgrannel — hand 57008

Zone: `oot`.

Sets `beast_epic` to `2`.

- Needs `beast_epic` ==1.
- Turn in x1: Letter from Muada (57008).
In script order:

1. Sets `beast_epic` to `2`.


How the items are reached:

- Letter from Muada (57008)
  - Prerequisite: "Letter from Muada" (57008). See section 0.

### 3. irionu bastun — hand 57008

Zone: `overthere`.

Sets `beast_epic` to `3`.

- Turn in x1: Letter from Muada (57008).
In script order:

1. Sets `beast_epic` to `3`.


How the items are reached:

- Letter from Muada (57008)
  - Prerequisite: "Letter from Muada" (57008). See section 0.

### 4. rashara wrualla — hand 57008

Zone: `jaggedpine`.

Sets `beast_epic` to `4`.

- Turn in x1: Letter from Muada (57008).
In script order:

1. Sets `beast_epic` to `4`.


How the items are reached:

- Letter from Muada (57008)
  - Prerequisite: "Letter from Muada" (57008). See section 0.

### 5. ikpug giblod — hand 57008

Zone: `cazicthule`.

Sets `beast_epic` to `5`.

- Turn in x1: Letter from Muada (57008).
In script order:

1. Sets `beast_epic` to `5`.


How the items are reached:

- Letter from Muada (57008)
  - Prerequisite: "Letter from Muada" (57008). See section 0.

### 6. diddugu — hand 57008

Zone: `westwastes`.

Sets `beast_epic` to `6`.

- Turn in x1: Letter from Muada (57008).
In script order:

1. Sets `beast_epic` to `6`.


How the items are reached:

- Letter from Muada (57008)
  - Prerequisite: "Letter from Muada" (57008). See section 0.

### 7. elder animist muada — hand 57009+57995

Zone: `sharvahl`.

Sets `beast_epic` to `7`.

- Turn in x1: Darkened Spirit Essence (57009).
- Turn in x1: Disturbed Beast Essence (57995).
In script order:

1. Sets `beast_epic` to `7`.


How the items are reached:

- Darkened Spirit Essence (57009)
  - Loot "Darkened Spirit Essence" (57009) from "Frantic Ravenous Beast" in `maiden`.
- Disturbed Beast Essence (57995)
  - Loot "Disturbed Beast Essence" (57995) from "A Ravenous Nightstalker" in `ponightmare`.

### 8. irionu bastun — hand 57996

Zone: `overthere`.

Sets `beast_epic` to `8`.

- Turn in x1: Note to Irionu (57996).
In script order:

1. Sets `beast_epic` to `8`.


How the items are reached:

- Note to Irionu (57996)
  - Prerequisite: "Note to Irionu" (57996). See section 0.

### 9. elder animist muada — hand 52900

Zone: `sharvahl`.

Sets `beast_epic` to `9`.

- Turn in x1: Sealed Note for Muada (52900).
In script order:

1. Sets `beast_epic` to `9`.


How the items are reached:

- Sealed Note for Muada (52900)
  - Prerequisite: "Sealed Note for Muada" (52900). See section 0.

### 10. marrey mcgrannel — hand 13039

Zone: `oot`.

Sets `beast_epic` to `10`.

- Needs `beast_epic` ==9.
- Turn in x3: Ale (13039).
In script order:

1. Sets `beast_epic` to `10`.


How the items are reached:

- Ale (13039)
  - Prerequisite: "Ale" (13039). See section 0.

### 11. marrey mcgrannel — say speak

Zone: `oot`.

> We must accommodate their requests to build trust. This means we must weave through their riddles. Once we do, we will be able to talk to them and help them. We

Sets `beast_epic` to `11`.

- Needs `beast_epic` ==10.
In script order:

1. Sets `beast_epic` to `11`.
2. Gives Feral Lord's Brooch (52901).


### 12. ankhefenmut — say endangered

Zone: `rathemtn`.

> Zazamoukh calls to me. You must go see the sphinx quickly.

Sets `beast_epic` to `12`.

- Needs `beast_epic` ==11.
In script order:

1. Sets `beast_epic` to `12`.


### 13. zazamoukh — hand 52902

Zone: `rathemtn`.

Sets `beast_epic` to `13`.

- Turn in x1: Tarnished Ankh Piece (52902).
In script order:

1. Sets `beast_epic` to `13`.
2. Gives Sparkling Silk Scarf (52904).


How the items are reached:

- Tarnished Ankh Piece (52902)
  - Say "Happening" to rathemtn/"Zazamoukh".
  - Spawns "Needs Heading Validation" (50326).
  - Loot "Tarnished Ankh Piece" (52902) from "Needs Heading Validation".

### 14. ankhefenmut — hand 52903

Zone: `rathemtn`.

Sets `beast_epic` to `14`.

- Turn in x1: Sullied Ankh Piece (52903).
In script order:

1. Sets `beast_epic` to `14`.
2. Gives Gift of the Sphinx (52905).


How the items are reached:

- Sullied Ankh Piece (52903)
  - Hand "Sparkling Silk Scarf" (52904) to rathemtn/"Ankhefenmut". Spawns "Needs Heading Validation" (50327). Loot "Sullied Ankh Piece" (52903) from "Needs Heading Validation".

### 15. elder animist muada — hand 52905

Zone: `sharvahl`.

Sets `beast_epic` to `15`.

- Turn in x1: Gift of the Sphinx (52905).
In script order:

1. Sets `beast_epic` to `15`.


How the items are reached:

- Gift of the Sphinx (52905)
  - Prerequisite: "Gift of the Sphinx" (52905). See section 0.

### 16. rashara wrualla — hand 52907+52908

Zone: `jaggedpine`.

Sets `beast_epic` to `16`.

- Turn in x1: Rashara's Warder's Essence (52907).
- Turn in x1: Sealed Response to the Elders (52908).
In script order:

1. Sets `beast_epic` to `16`.


How the items are reached:

- Rashara's Warder's Essence (52907)
  - Hand "Request of the Elders" (52906) to draniksscar/"Yerika Sisslak". Spawns "Girplan Spiritleech" (302085). Loot "Rashara's Warder's Essence" (52907) from "Girplan Spiritleech".
- Sealed Response to the Elders (52908)
  - Prerequisite: "Sealed Response to the Elders" (52908). See section 0.

### 17. elder animist muada — hand 52914

Zone: `sharvahl`.

Sets `beast_epic` to `17`.

- Turn in x1: Wrapped Discordant Totem of the Feral (52914).
In script order:

1. Sets `beast_epic` to `17`.
2. Gives Savage Lord's Totem (52911).


How the items are reached:

- Wrapped Discordant Totem of the Feral (52914)
  - Prerequisite: "Wrapped Discordant Totem of the Feral" (52914). See section 0.

Alternative or repeat transition to `beast_epic` = `1` (not an additional required stage).

### 1. elder animist muada — say hail

Zone: `sharvahl`.

> I am honored to have had the opportunity to observe you -- a feral champion for the ills that have befallen our kind. You have certainly made your name known...

Sets `beast_epic` to `1`.

- Needs `beast_epic` ==17.
- Needs Claw of the Savage Spirit (8495).
- Needs Claw of the Savage Spirit (8496).
- Needs `beast_epic` unset.
In script order:

1. Sets `beast_epic` to `1`.


How the items are reached:

- Claw of the Savage Spirit (8495)
  - Prerequisite: "Claw of the Savage Spirit" (8495). See section 0.
- Claw of the Savage Spirit (8496)
  - Prerequisite: "Claw of the Savage Spirit" (8496). See section 0.

### 18. elder animist muada — say trapped spirits

Zone: `sharvahl`.

> There are discordant beasts that have become twisted through no fault of their own. You may think of it as a spiritual plage, which has us mystified, but we ...

Sets `beast_epic` to `18`.

- Needs Spiritbound Totem (57027).
- Needs `beast_epic` ==17.
In script order:

1. Sets `beast_epic` to `18`.


How the items are reached:

- Spiritbound Totem (57027)
  - Prerequisite: "Spiritbound Totem" (57027). See section 0.

### 19. jillaa oogblat — hand 57012

Zone: `causeway`.

Sets `beast_epic` to `19`.

- Needs `beast_epic` ==18.
- Turn in x1: Dark Animist Wand (57012).
In script order:

1. Sets `beast_epic` to `19`.


How the items are reached:

- Dark Animist Wand (57012)
  - Kill causeway/"Bazu Terror". Spawns "Discordling Dark Animist" (303094).
  - Loot "Dark Animist Wand" (57012) from "Discordling Dark Animist".

### 20. jillaa oogblat — hand 57051

Zone: `causeway`.

Sets `beast_epic` to `20`.

- Turn in x1: Blended Elixir of Fortitude (57051).
In script order:

1. Sets `beast_epic` to `20`.


How the items are reached:

- Blended Elixir of Fortitude (57051)
  - Prerequisite: "Blended Elixir of Fortitude" (57051). See section 0.

### 21. elder animist muada — hand 57052

Zone: `sharvahl`.

Sets `beast_epic` to `21`.

- Turn in x1: Wrapped Gemmed Wand (57052).
In script order:

1. Sets `beast_epic` to `21`.


How the items are reached:

- Wrapped Gemmed Wand (57052)
  - Prerequisite: "Wrapped Gemmed Wand" (57052). See section 0.

### 22. alladnu araihse — hand 52911+57053

Zone: `hollowshade`.

Sets `beast_epic` to `22`.

- Turn in x1: Savage Lord's Totem (52911).
- Turn in x1: Sealed Letter from Muada (57053).
In script order:

1. Sets `beast_epic` to `22`.


How the items are reached:

- Savage Lord's Totem (52911)
  - Prerequisite: "Savage Lord's Totem" (52911). See section 0.
- Sealed Letter from Muada (57053)
  - Prerequisite: "Sealed Letter from Muada" (57053). See section 0.

### 23. alladnu araihse — say ready

Zone: `hollowshade`.

> Then you have finished your journey. Here ends my service and those of the spirits. You are one with the spirits now. Travel your life

Sets `beast_epic` to `23`.

- Needs `beast_epic` ==22.
In script order:

1. Sets `beast_epic` to `23`.
2. Gives Spiritcaller Totem of the Feral (57054).


### Steps on `beast_epic` that do not change it

- `bloodfields` player, on loot needs `beast_epic` ==20.
  - Sets `warr_epic_bloodfield` to `1`.
  - Spawns a chest (Epic 1.5) (283157).
  - Sets `monk_epic_bloodfield` to `1`.
  - Sets `monk_epic_keeper` to `1`.
  - Sets `bst_chest_causeway` to `1`.
  - Spawns a chest (epic 2.0) (893).
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
- `bloodfields` tormented scout, say strong needs `beast_epic` ==20.
  - Spawns DDA (301069).
  - Loots Gemmed Dark Animist Wand (57014).
- `causeway` jillaa oogblat, say hail needs `beast_epic` ==18.
  - Spawns Bazu Terror (303092).
  - Spawns a bazu crusher (303093).
  - Loots Feral Dust (57013).
- `causeway` player, on loot needs `beast_epic` ==18.
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
- `cazicthule` ikpug giblod, say learning needs `beast_epic` ==5.
  - Gives Letter from Muada (57008).
- `dranik` player, on loot needs `beast_epic` ==16.
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
- `draniksscar` player, on loot needs `beast_epic` ==15.
  - Sets `beast_epic_ds` to `1`.
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
- `grimling` scout husman, say end the threat in the grimling forest needs `beast_epic` ==17.
  - Spawns Grimling Colonel (167426).
  - Spawns Grimling General (167726).
  - Loots Sunshard Ore (33792).
  - Loots Bonded Loam (34882).
  - Loots Eerie Medallion (57025).
  - Loots Harmonagate (97003).
  - Loots Sunshard Ore (33792).
  - Loots Bonded Loam (34882).
  - Loots Eerie Medallion (57025).
  - Loots Harmonagate (97003).
- `jaggedpine` rashara wrualla, say not possible needs `beast_epic` ==15.
  - Gives Request of the Elders (52906).
- `jaggedpine` rashara wrualla, say wait needs `beast_epic` ==4.
  - Gives Letter from Muada (57008).
- `oot` marrey mcgrannel, say way needs `beast_epic` ==2.
  - Gives Letter from Muada (57008).
- `overthere` irionu bastun, say read needs `beast_epic` ==3.
  - Gives Letter from Muada (57008).
- `sharvahl` elder animist muada, say agree to take on this charge needs `beast_epic` ==19.
  - Gives Blended Elixir of Fortitude (57051).
- `sharvahl` elder animist muada, say greater calling needs `beast_epic` ==7.
  - Gives Note to Irionu (57996).
- `sharvahl` elder animist muada, hand 47100+57027 needs `beast_epic` ==21.
  - Turn in Globe of Discordant Energy (47100).
  - Turn in Spiritbound Totem (57027).
  - Gives Sealed Letter from Muada (57053).
- `sharvahl` elder animist muada, say make the totem needs `beast_epic` ==17.
  - Gives Elders' Totem Mold (52930).
  - Gives Combined Essence (52913).
- `sharvahl` elder animist muada, say stopped needs `beast_epic` ==16.
  - Gives Elder Cloak of Resilience (52909).
- `sharvahl` elder animist muada, say task needs `beast_epic` ==17.
  - Gives Peculiar Unshapen Piece of Wood (57011).
- `westwastes` diddugu, say mastodon needs `beast_epic` ==6.
  - Gives Letter from Muada (57008).

## `bstepic`

Values written: 1.

### 1. elder animist dumul — hand 4393

Zone: `sharvahl`.

Sets `bstepic` to `1`.

- Turn in x1: Copper Medal of War (4393).
In script order:

1. Sets `bstepic` to `1`.
2. Gives Carved Wooden Chest (17361).
3. Gives Official Seal of the Khati Sha (9031).


How the items are reached:

- Copper Medal of War (4393)
  - Spawns "Arcanist Ukigit" (167661) in `grimling` on event_signal.
  - Loot "Copper Medal of War" (4393) from "Arcanist Ukigit".

## Other flags touched along the way

- `beast_epic_dran` set to 1 at dranik/player.
- `beast_epic_ds` set to 1 at draniksscar/player.
- `bst_chest_causeway` set to 1 at bloodfields/player.
