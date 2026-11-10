# Shadowknight — Epic Quest Walkthrough

Generated directly from quest-graph item rewards. Unresolved dependencies are marked, not inferred.

## Epic 1.0

### "Innoruuk's Curse" (14383)

1. neriakc/"Selzar L-Crit", say "Hail".
    - Player: "hail"
      - NPC say: What have we here? Another hopeful member of the House of the Ebon Mask? You've got much to learn before you will be of much use to our House or the secret operations that support both the thrones of our King and Queen. First you need to outfit yourself in a suit of [armor], $name.
      - Condition: `($text=~/hail/i)`
2. neriakc/"Selzar L-Crit", say "Armor". Gives "Note to Kanthuk" (2416).
    - Player: "armor"
      - NPC say: Seek Kanthu M'Rekkor and give him this request parchment. When you have outfitted yourself in a suit of armor return to the House of the Ebon Mask and I will grant you [another task].
      - Condition: `($text=~/armor/i)`
      - Linked from "hail" (explicit prompt).
3. butcher/"Kanthuk Ogrebane", hand "Note to Kanthuk" (2416).
    - event_trade NPC say: Ahh, I see you have spoken to Ryshon. You seem tired from your long journey. Sit with me as I tell you a tale. A tale about a true friend of mine, a great man known as [Amstaf Trunolis].
      - Event guard: `item_lib.check_turn_in(e.trade, {item1 = 2416})`
4. butcher/"Kanthuk Ogrebane", say "Strange Image". Gives "Pendant" (2414).
    - Player: "strange image"
      - NPC say: I saw Amstaf lower his head and walked away in silence. He was surronded by two beings carrying a torch. I don't know what it meant, but I swear it was so real. When I awoke both Amstaf and Ambreen were gone. Please find Llara and give this pendant to her. This pendant belonged to Amstaf. She too had a vision that night that may clear things up. If she asks where you got it from, mention my name.
      - Condition: `qglobals["Kanthuk"] ~= nil`
      - Condition: `e.message:findi("strange image")`
      - Linked from "slumber" (explicit prompt).
5. cauldron/"Llara", hand "Pendant" (2414).
    - event_trade NPC say: Oh my, this belongs to Amstaf! Where did you get it?
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 2414}))`
6. cauldron/"Llara", say "Ruathey". Gives "Note to Ruathey" (2417).
    - Player: "ruathey"
      - NPC say: Ruathey is known for her ability to look into people's souls and find truth. Though I wasn't able to find Amstaf, I was able to recover his sword. I believe that by having his sword I am closer to finding him. Take this note to Ruathey and tell her that I sent you.
      - Condition: `(qglobals["Llara"] ~= nil)`
      - Condition: `(e.message:findi("ruathey"))`
      - Linked from "see" (explicit prompt).
7. lavastorm/"Ruathey", hand "Note to Ruathey" (2417).
    - event_trade NPC say: I see that you've spoken to Llara. She too came to me looking for Amstaf. Though she wasn't able to find her friend, she was able to recover his [sword].
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 2417}))`
    - event_item NPC say: I see that you've spoken to Llara. She too came to me looking for Amstaf. Though she wasn't able to find her friend, she was able to recover his [sword].
      - Event guard: `(plugin::check_handin(\%itemcount, 2417 => 1))`
8. lavastorm/"Ruathey", say "Bag". Gives "Nobleman's Bag" (17878).
    - Player: "bag"
      - NPC say: Take this bag and gather the items I've mentioned. I've been told that the Ghoul's Heart can be found in the estate of the undead, while the scroll can be found in the Keep not far from the Karanas. One of the others are rumored to be found near the dwarven city among the goblins. While the last should be found in the caverns of Najena.
      - Condition: `(qglobals["Ruathey"] ~= nil)`
      - Condition: `(e.message:findi("bag"))`
      - Linked from "sword" (explicit prompt).
9. Loot "Ghoul's Heart" (2410) from "a ghoul" (NPC 63011) in `unrest`. Drop cache: 25% chance per kill.
10. Loot "Amstaf's Scroll" (2411) from "a goblin thief" (NPC 6150) in `highkeep`. Drop cache: 35% chance per kill.
11. Loot "Blade of Nobility" (2412) from "a crazed goblin" (NPC 68162) in `butcher`. Drop cache: 10.5658% chance per kill.
12. Loot "Hilt of the Nobleman" (2413) from "a skeleton" (NPC 44025) in `najena`. Drop cache: 11.946% chance per kill.
13. Combine in "Nobleman's Bag" (17878): "Ghoul's Heart" (2410), "Amstaf's Scroll" (2411), "Blade of Nobility" (2412), "Hilt of the Nobleman" (2413). Produces "Ghoulbane" (5403). Requires Remove Traps.
14. Loot "Soul Leech, Dark Sword of Blood" (11609) from "Dread" (NPC 72000) in `fearplane`. Drop cache: 10.4954% chance per kill.
15. Spawns "an essence carrier" (npc:71070) via `airplane/a soul carrier#event_death_complete`.
16. Kill "an essence carrier" (NPC 71070) in `airplane` and loot "Blade of Abrogation" (5430).
17. Loot "Drake Spine" (14372) from "Rharzar" (NPC 50324) in `rathemtn`. Drop cache: 100% chance per kill.
18. Loot "Decrepit Hide" (14371) from "an ashenbone drake" (NPC 186049) in `hateplaneb`. Drop cache: 11.2025% chance per kill.
19. **Unresolved acquisition:** "Enchanted Platinum Bar" (16507) has no graph or catalog producer.
20. qcat/"Teydar", hand "Drake Spine" (14372) + "Decrepit Hide" (14371) + "Enchanted Platinum Bar" (16507). Gives "Decrepit Sheath" (14366).
    - event_item NPC say: I did it! The pieces you got me were perfect! It took a huge effort on my part to craft this, of course. It saddens me that I'm unable to keep one of my best works, but a deal is a deal. There is honor among shadowknights.
      - Event guard: `($faction >= 28 && plugin::check_handin(\%itemcount, 14372 => 1, 14371 => 1, 16507 => 1))`
21. paineel/"Duriek Bloodpool", hand "Ghoulbane" (5403) + "Soul Leech, Dark Sword of Blood" (11609) + "Blade of Abrogation" (5430) + "Decrepit Sheath" (14366). Gives "Corrupted Ghoulbane" (14367).
    - event_item NPC emote: takes the Ghoulbane and places the other swords on either side of it. The sheath begins to gleam so intensely, you can see the bones inside Duriek's hands. After several minutes, there is a final, blinding flash. Duriek collapses to the ground. After a few moments, Duriek motions you closer and whispers, 'You have done well. I wish fate had been kinder to me and allowed me your aid years ago--I might have lived long enough to enjoy the fame of our combined efforts. I studied much of the tome you retrieved and have stumbled upon something that may be the key to unleashing darkness upon the face of Norrath forever. You must seek out a powerful lich by the name of Lhranc. Farewell, $name.' With his last bit of energy, Duriek places the corrupted Ghoulbane in your hands.
      - Event guard: `(($faction >= 35) && plugin::check_handin(\%itemcount, 5403 => 1, 11609 => 1, 5430 => 1, 14366 => 1))`
22. tox/"Knarthenne Skurl", say "Heart Of An Innocent". Gives "Soulcase" (17051).
    - Player: "heart of an innocent"
      - NPC say: What's that? Heart of the Innocent, you say?! Ages, it has been, since I was last asked that. The Heart of the Innocent is an item of great power. Few are they who have ever commanded the dark magic of such an object. It is the bound soul of a pure mortal, rare indeed. Take this hollow gem, and combine with it the heart of one who is pure. If your hand is steady and your mind is clear, you shall have what you seek.
      - Condition: `($text=~/heart of an innocent/i)`
      - Linked from "Hail" (explicit prompt).
23. Loot "Cell Key" (14373) from "a chest" (NPC 39056) in `hole`. Drop cache: 25% chance per kill.
24. hole/"Caradon", hand "Cell Key" (14373).
    - event_item NPC say: Kyrenna! We are free!
      - Event guard: `($faction >= 44 && plugin::check_handin(\%itemcount, 14373 => 1))`
25. Spawns "Kyrenna" (npc:39155) after the hand-in.
26. Kill "Kyrenna" (NPC 39155) in `hole` and loot "Heart of Kyrenna" (14380).
27. Combine in "Soulcase" (17051): "Heart of Kyrenna" (14380). Produces "Heart of the Innocent" (14368). Requires Remove Traps.
28. Kill "Kyrenna" (NPC 39155) in `hole` and loot "Blood of Kyrenna" (14381).
29. kerraridge/"Marl Kastane", hand "Blood of Kyrenna" (14381). Gives "Dark Shroud" (14377).
    - event_item NPC say: Here, you take this shroud. You must now find the spirit of glohnor and place this item on him. This should force him back into his mummified body and then you must destroy this newly raised form and return to me its wrappings.
      - Event guard: `(($faction >= 51) && plugin::check_handin(\%itemcount, 14381 => 1))`
30. hole/"Ghost Of Glohnor", hand "Dark Shroud" (14377).
31. Spawns "Mummy of Glohnor" (npc:39165) after the hand-in.
32. Kill "Mummy of Glohnor" (NPC 39165) in `hole` and loot "Head of Glohnor" (14378).
33. paineel/"Gerot Kastane", hand "Head of Glohnor" (14378). Gives "Head of the Valiant" (14369).
    - event_item NPC say: Good travels, dark one! May Innoruuk curse your enemies!
      - Event guard: `(($faction >= 58) && plugin::check_handin(\%itemcount, 14378 => 1))`
34. Kill "Mummy of Glohnor" (NPC 39165) in `hole` and loot "Glohnor wrappings" (14379).
35. kerraridge/"Marl Kastane", hand "Glohnor wrappings" (14379). Gives "Will of Innoruuk" (14370).
    - event_item NPC say: You've done it! Your efforts will stand as a tribute to our kind for time eternal, my friend. Although nothing could possibly serve as a just reward for your accomplishments, please accept this as well as my eternal gratitude. It has been fashioned from the wraps of the mummy and shall protect you well.
      - Event guard: `(($faction >= 58) && plugin::check_handin(\%itemcount, 14379 => 1))`
36. citymist/"Lhranc", hand "Corrupted Ghoulbane" (14367) + "Heart of the Innocent" (14368) + "Head of the Valiant" (14369) + "Will of Innoruuk" (14370). Gives "Lhranc's Token" (14384).
    - event_trade NPC say: Ahh, at last I can free myself of this prison! Centuries have passed since I enjoyed the fruits of mortality.' He hurls the components above his head where they remain suspended in midair. They hover in place while he chants the words of an ancient spell. As he speaks, the items begin to rotate around his head, slowly at first, then faster as the chanting grows louder, until it spins in a blur. Soon, the room is filled with a deafening shriek that pierces you to the core.
      - Event guard: `(e.other:GetModCharacterFactionLevel(e.self:GetPrimaryFaction()) >= 72)`
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 14367, item2 = 14368, item3 = 14369, item4 = 14370}))`
37. citymist/"Marl Kastane", hand "Lhranc's Token" (14384). Gives "Innoruuk's Curse" (14383).
    - event_trade NPC say: Very good, I will go deliver this right away.
      - Event guard: `(e.other:GetModCharacterFactionLevel(e.self:GetPrimaryFaction()) > 82 and item_lib.check_turn_in(e.trade, {item1 = 14384}))`

## Epic 1.5

### "Innoruuk's Voice" (50003)

1. Loot "Sir Elmonious's Holy Symbol" (55901) from "Sir Elmonious Falmont" (NPC 120133) in `westwastes`. Drop cache: 100% chance per kill.
2. poknowledge/"Gilina Yilzior", hand "Sir Elmonious's Holy Symbol" (55901). Gives "Innoruuk's Voice" (50003).
    - event_trade NPC say: You have performed well. The blade is yours to wield now, champion. You may be on your way, or stay to hear about a [vision] I recently had.
      - Event guard: `(qglobals["shadowknight_epic"] == "8" and item_lib.check_turn_in(e.trade, {item1 = 55901}))`
    - event_trade NPC message: You have gained 5 ability points!

## Epic 2.0

### "Innoruuk's Dark Blessing" (48136)

1. Kill dranik/"A Minion Of Lhranc".
2. Spawns "Lhranc" (npc:336250) via `dranik/filligno the slayer#signal:1`.
3. Kill "Lhranc" (NPC 336250) in `dranik` and loot "Essence of the Shadowknight" (55903).
4. Loot "Sir Elmonious's Holy Symbol" (55901) from "Sir Elmonious Falmont" (NPC 120133) in `westwastes`. Drop cache: 100% chance per kill.
5. poknowledge/"Gilina Yilzior", hand "Sir Elmonious's Holy Symbol" (55901). Gives "Innoruuk's Voice" (50003).
    - event_trade NPC say: You have performed well. The blade is yours to wield now, champion. You may be on your way, or stay to hear about a [vision] I recently had.
      - Event guard: `(qglobals["shadowknight_epic"] == "8" and item_lib.check_turn_in(e.trade, {item1 = 55901}))`
    - event_trade NPC message: You have gained 5 ability points!
6. dranik/"Filligno The Slayer", hand "Essence of the Shadowknight" (55903) + "Innoruuk's Voice" (50003). Gives "Innoruuk's Dark Blessing" (48136).
    - event_trade NPC emote: takes the essence and begins to study it most carefully. After what seems like an eternity, Filligno throws the globe onto the floor. It cracks open, letting loose a stream of ghastly spirits. Filligno dives for cover. As the cackling spirits dissipate, a powerful looking sword floats in mid-air before you.
      - Event guard: `(qglobals["shadowknight_epic"] == "11" and item_lib.check_turn_in(e.trade, {item1 = 55903, item2 = 50003}))`
    - event_trade NPC say: Take it! The blade is yours! A gift from Innoruuk, for the most powerful of shadowknights!
    - event_trade NPC message: You have gained 10 ability points!
