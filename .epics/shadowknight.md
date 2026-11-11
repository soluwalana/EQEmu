# Shadowknight — Epic Quest Walkthrough

Generated directly from quest-graph item rewards. Unresolved dependencies are marked, not inferred.

## Epic 1.0

### "Innoruuk's Curse" (14383)

<a id="epic-item-14383"></a>

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
7. lavastorm/, hand "Note to Ruathey" (2417).
8. lavastorm/, say "Ruathey". Gives "Nobleman's Bag" (17878).
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
19. Summon "Enchanted Platinum Bar" (16507) by casting "Enchant Platinum" or "Greater Mass Enchant Platinum" or "Mass Enchant Platinum".
20. **Faction:** `404` `>=28` required. Progress unverified.
21. qcat/"Teydar", hand "Drake Spine" (14372) + "Decrepit Hide" (14371) + "Enchanted Platinum Bar" (16507). Gives "Decrepit Sheath" (14366).
    - event_item NPC say: I did it! The pieces you got me were perfect! It took a huge effort on my part to craft this, of course. It saddens me that I'm unable to keep one of my best works, but a deal is a deal. There is honor among shadowknights.
      - Event guard: `($faction >= 28 && plugin::check_handin(\%itemcount, 14372 => 1, 14371 => 1, 16507 => 1))`
22. **Faction:** `404` `>=35` required. Progress unverified.
23. paineel/"Duriek Bloodpool", hand "Ghoulbane" (5403) + "Soul Leech, Dark Sword of Blood" (11609) + "Blade of Abrogation" (5430) + "Decrepit Sheath" (14366). Gives "Corrupted Ghoulbane" (14367).
    - event_item NPC emote: takes the Ghoulbane and places the other swords on either side of it. The sheath begins to gleam so intensely, you can see the bones inside Duriek's hands. After several minutes, there is a final, blinding flash. Duriek collapses to the ground. After a few moments, Duriek motions you closer and whispers, 'You have done well. I wish fate had been kinder to me and allowed me your aid years ago--I might have lived long enough to enjoy the fame of our combined efforts. I studied much of the tome you retrieved and have stumbled upon something that may be the key to unleashing darkness upon the face of Norrath forever. You must seek out a powerful lich by the name of Lhranc. Farewell, $name.' With his last bit of energy, Duriek places the corrupted Ghoulbane in your hands.
      - Event guard: `(($faction >= 35) && plugin::check_handin(\%itemcount, 5403 => 1, 11609 => 1, 5430 => 1, 14366 => 1))`
24. tox/"Knarthenne Skurl", say "Heart Of An Innocent". Gives "Soulcase" (17051).
    - Player: "heart of an innocent"
      - NPC say: What's that? Heart of the Innocent, you say?! Ages, it has been, since I was last asked that. The Heart of the Innocent is an item of great power. Few are they who have ever commanded the dark magic of such an object. It is the bound soul of a pure mortal, rare indeed. Take this hollow gem, and combine with it the heart of one who is pure. If your hand is steady and your mind is clear, you shall have what you seek.
      - Condition: `($text=~/heart of an innocent/i)`
      - Linked from "Hail" (explicit prompt).
25. **Faction:** `404` `>=44` required. Progress unverified.
26. Loot "Cell Key" (14373) from "a chest" (NPC 39056) in `hole`. Drop cache: 25% chance per kill.
27. hole/"Caradon", hand "Cell Key" (14373).
    - event_item NPC say: Kyrenna! We are free!
      - Event guard: `($faction >= 44 && plugin::check_handin(\%itemcount, 14373 => 1))`
28. Spawns "Kyrenna" (npc:39155) after the hand-in.
29. Kill "Kyrenna" (NPC 39155) in `hole` and loot "Heart of Kyrenna" (14380).
30. Combine in "Soulcase" (17051): "Heart of Kyrenna" (14380). Produces "Heart of the Innocent" (14368). Requires Remove Traps.
31. Kill "Kyrenna" (NPC 39155) in `hole` and loot "Blood of Kyrenna" (14381).
32. **Faction:** `404` `>=51` required. Progress unverified.
33. kerraridge/"Marl Kastane", hand "Blood of Kyrenna" (14381). Gives "Dark Shroud" (14377).
    - event_item NPC say: Here, you take this shroud. You must now find the spirit of glohnor and place this item on him. This should force him back into his mummified body and then you must destroy this newly raised form and return to me its wrappings.
      - Event guard: `(($faction >= 51) && plugin::check_handin(\%itemcount, 14381 => 1))`
34. hole/"Ghost Of Glohnor", hand "Dark Shroud" (14377).
35. Spawns "Mummy of Glohnor" (npc:39165) after the hand-in.
36. Kill "Mummy of Glohnor" (NPC 39165) in `hole` and loot "Head of Glohnor" (14378).
37. **Faction:** `404` `>=58` required. Progress unverified.
38. paineel/"Gerot Kastane", hand "Head of Glohnor" (14378). Gives "Head of the Valiant" (14369).
    - event_item NPC say: Good travels, dark one! May Innoruuk curse your enemies!
      - Event guard: `(($faction >= 58) && plugin::check_handin(\%itemcount, 14378 => 1))`
39. Kill "Mummy of Glohnor" (NPC 39165) in `hole` and loot "Glohnor wrappings" (14379).
40. kerraridge/"Marl Kastane", hand "Glohnor wrappings" (14379). Gives "Will of Innoruuk" (14370).
    - event_item NPC say: You've done it! Your efforts will stand as a tribute to our kind for time eternal, my friend. Although nothing could possibly serve as a just reward for your accomplishments, please accept this as well as my eternal gratitude. It has been fashioned from the wraps of the mummy and shall protect you well.
      - Event guard: `(($faction >= 58) && plugin::check_handin(\%itemcount, 14379 => 1))`
41. citymist/"Lhranc", hand "Corrupted Ghoulbane" (14367) + "Heart of the Innocent" (14368) + "Head of the Valiant" (14369) + "Will of Innoruuk" (14370). Gives "Lhranc's Token" (14384).
    - event_trade NPC say: Ahh, at last I can free myself of this prison! Centuries have passed since I enjoyed the fruits of mortality.' He hurls the components above his head where they remain suspended in midair. They hover in place while he chants the words of an ancient spell. As he speaks, the items begin to rotate around his head, slowly at first, then faster as the chanting grows louder, until it spins in a blur. Soon, the room is filled with a deafening shriek that pierces you to the core.
      - Event guard: `(e.other:GetModCharacterFactionLevel(e.self:GetPrimaryFaction()) >= 72)`
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 14367, item2 = 14368, item3 = 14369, item4 = 14370}))`
42. citymist/"Marl Kastane", hand "Lhranc's Token" (14384). Gives "Innoruuk's Curse" (14383).
    - event_trade NPC say: Very good, I will go deliver this right away.
      - Event guard: `(e.other:GetModCharacterFactionLevel(e.self:GetPrimaryFaction()) > 82 and item_lib.check_turn_in(e.trade, {item1 = 14384}))`

## Epic 1.5

### "Innoruuk's Voice" (50003)

<a id="epic-item-50003"></a>

1. Loot "Sir Elmonious's Holy Symbol" (55901) from "Sir Elmonious Falmont" (NPC 120133) in `westwastes`. Drop cache: 100% chance per kill.
2. Loot "Ancient Flamberge of Hatred" (55902) from "Captain Varns" (NPC 225232) in `dulak`. Drop cache: 100% chance per kill.
3. Loot "Essence of Hate" (21870) from "Mistress of Malevolence" (NPC 186181) in `hateplaneb`. Drop cache: 70% chance per kill.
4. Loot "Stormborn Phylactery" (21782) from "Olidan" (NPC 210189) in `postorms`. Drop cache: 100% chance per kill.
5. dulak/"Ritald", say "Hail". Sets `shadowknight_pre` to `1`.
    - Player: "hail"
      - NPC say: Greetings, dark one. Do you feel it? I am sure you do. Innoruuk's voice is so distant now. His voice is merely a whisper. This disturbs me greatly. How will the evil ones do their master's bidding without his dark guidance? I fear the end is almost near for true champions of darkness such as yourself. We cannot let that happen! I believe I know of a way to slow down the diminishing of our master's voice. There is a sword of great evil. It is however not of this world. I believe I can summon it to this plane of existence, but I will need several items first. Will you [take on this task]? Your future and the future of all our dark brethren depends on obtaining this sword!
      - Condition: `(e.other:Class() == "Shadow Knight")`
      - Condition: `(e.message:findi("hail") and qglobals["shadowknight_pre"] == nil)`
6. dulak/"Ritald", hand "Ancient Flamberge of Hatred" (55902) + "Essence of Hate" (21870) + "Stormborn Phylactery" (21782). Gives "Innoruuk's Voice" (22944).
    - event_trade NPC say: You have done well. The flamberge you have brought to me will act as a vessel for the summoning of the sword. The essence of hate will help generate hatred needed to fuel the summoning, and the phylactery should hopefully help contain that hate to be used in the summoning.
      - Event guard: `qglobals["shadowknight_pre"] == "1" and item_lib.check_turn_in(e.trade, {item1 = 55902, item2 = 21870, item3 = 21782})`
    - event_trade NPC emote: Ritald holds the flamberge above his head with both hands and begins to chant. Dark storm clouds gather overhead as a flash of lightning momentarily blinds you. When you regain your sight, Ritald holds the summoned sword of Innoruuk's Voice.
    - event_trade NPC say: I [have done it]!
7. poknowledge/"Sienn Kastane", hand "Innoruuk's Voice" (22944).
8. Loot "Gelatinous Murkglider Egg" (55900) from "Murkglider Breeder" (NPC 336201) in `dranik`. Drop cache: 100% chance per kill.
9. poknowledge/"Grand Librarian Maelin", hand "Gelatinous Murkglider Egg" (55900). Gives "The Silent Gods" (20520).
    - event_trade NPC say: I knew they were egg-layers! Ha, this is one gnome who hates losing a bet and thanks to you I wont! This is the tome you seek. Please bring it back to me when you are done.
      - Event guard: `(qglobals["shadowknight_epic"] == "1" and item_lib.check_turn_in(e.trade, {item1 = 55900}))`
10. poknowledge/"Sienn Kastane", hand "The Silent Gods" (20520).
    - event_trade NPC say: You have done well in acquiring this tome.' Sienn opens the tome and begins to read. 'It says that a sheath must be created to protect the sword. Unfortunately the instructions for making this sheath are a bit unclear. The only clues given to the items needed are, to gather a dark hide of a creature unmatched in its bleakness, a holy lock of hair from a fair creature unmatched in happiness, and a gem possessing the very essence of fear itself, held by a creature more fearsome. If you find these three items, combine them in a sewing kit and then hand the sheath to me. I await your return.
      - Event guard: `(qglobals["shadowknight_epic"] == "1" and item_lib.check_turn_in(e.trade, {item1 = 20520}))`
11. Summon "Collapsible Sewing Kit" (17165) by casting "Unfold Sewing Kit".
12. Loot "Eye of the Dark God" (21675) from "Amygdalan warrior" (NPC 72015) in `fearplane`. Drop cache: 18.3167% chance per kill.
13. Loot "Gloom Nightmare Hide" (20622) from "a gloom nightmare" (NPC 204018) in `ponightmare`. Drop cache: 22.1895% chance per kill.
14. Loot "Lock of Blessed Unicorn Hair" (21496) from "a rolling plains steed" (NPC 127084) in `growthplane`. Drop cache: 11% chance per kill.
15. Combine in "Collapsible Sewing Kit" (17165): "Eye of the Dark God" (21675), "Gloom Nightmare Hide" (20622), "Lock of Blessed Unicorn Hair" (21496). Produces "Sheath of Darktidings" (20426). Requires Tailoring.
16. poknowledge/"Sienn Kastane", hand "Sheath of Darktidings" (20426).
    - event_trade NPC say: I admit that I did not think you could accomplish this task. Perhaps you really are meant to be the sword's champion. Our work here is not done however. There are those that wish the sword to be destroyed. One of these beings is a froglok paladin named Fraga. He was last seen in the Plane of Valor. Kill him and bring me any clues as to what his plans may be.
      - Event guard: `(qglobals["shadowknight_epic"] == "2" and item_lib.check_turn_in(e.trade, {item1 = 20426}))`
17. Loot "Fraga's Parchment" (23492) from "Fraga" (NPC 208080) in `povalor`. Drop cache: 83.333% chance per kill.
18. poknowledge/"Sienn Kastane", hand "Fraga's Parchment" (23492).
    - event_trade NPC emote: begins to read the parchment. A worried look plays across her face.
      - Event guard: `(qglobals["shadowknight_epic"] == "3" and item_lib.check_turn_in(e.trade, {item1 = 23492}))`
    - event_trade NPC say: The weapon is not safe. The forces of good strongly wish to have it destroyed. To make matters worse, the sword is emanating hate that can be felt by powerful beings, both good and evil, across all planes of existence. As it stands right now, I wouldn't be surprised if the forces of good are converging to have the sword destroyed and the forces of evil are conniving to take the sword for themselves. It is only a matter of time before they locate the sword and come for it themselves. I have been studying the tome while you were gone. The tome describes a way to [mask the sword's presence].
19. Loot "Wailing Sister Blood" (20497) from "The Wailing Sister" (NPC 204052) in `ponightmare`. Drop cache: 100% chance per kill.
20. Loot "Wailing Rune" (19025) from "The Wailing Sister" (NPC 204052) in `ponightmare`. Drop cache: 100% chance per kill.
21. poknowledge/"Sienn Kastane", hand "Wailing Sister Blood" (20497) + "Wailing Rune" (19025). Gives "Sheathed Innoruuk's Voice" (11407).
    - event_trade NPC emote: pours the blood on the rune. The rune begins to glow a bright red color and a horrifying wail fills your ears.
      - Event guard: `(qglobals["shadowknight_epic"] == "4" and item_lib.check_turn_in(e.trade, {item1 = 20497, item2 = 19025}))`
    - event_trade NPC say: The rune has been activated.
    - event_trade NPC emote: holds the rune against the sheath you created earlier. The rune instantaneously melts into the sheath.
    - event_trade NPC say: The sword is safe for now, but I think it should be moved just in case. Do not lose the sheathed sword. If you do lose it somehow, come back to me and tell me you lost it and I will attempt to make you another one. I only have enough left of the items you brought me to make you one more though. Now, take the sword to a servant of mine, named Gilina Yilzior, here in the Plane of Knowledge. She is very knowledgeable and should be able to help you further.
22. **Unverified quest flag:** `shadowknight_epic` `==1` required.
23. poknowledge/"Gilina Yilzior", hand "Sheathed Innoruuk's Voice" (11407).
    - event_trade NPC emote: looks at you with a cold stare.
      - Event guard: `(qglobals["shadowknight_epic"] == "5" and item_lib.check_turn_in(e.trade, {item1 = 11407}))`
    - event_trade NPC say: The time has come. I have heard the dark blade's whispers. It wants to find a master, but before that can become a reality, a test must be passed. There are four other shadowknights who wish to become the sword's wielder. If you are up for the challenge, then seek out Silithis Sisnta in the Timorous Deep, Gubblegrot Smashfist in the Ocean of Tears, Skurza Slicekutt in the Swamp of No Hope, and Giligatabbus Igglebix in Iceclad Ocean. Return their heads to me and we shall see if the sword is satisfied with your progress.
24. Loot "Skurza's Head" (20899) from "Skurza Slicekutt" (NPC 83250) in `swampofnohope`. Drop cache: 100% chance per kill.
25. Loot "Silithis's Head" (16813) from "Silithis Sisnta" (NPC 96362) in `timorous`. Drop cache: 100% chance per kill.
26. Loot "Gubblegrot's Head" (16793) from "Gubblegrot Smashfist" (NPC 409150) in `oceanoftears`. Drop cache: 100% chance per kill.
27. Loot "Giligatabbus's Head" (20079) from "Giligatabbus Igglebix" (NPC 110104) in `iceclad`. Drop cache: 100% chance per kill.
28. poknowledge/"Gilina Yilzior", hand "Skurza's Head" (20899) + "Silithis's Head" (16813) + "Gubblegrot's Head" (16793) + "Giligatabbus's Head" (20079). Gives "Sheathed Innoruuk's Voice" (22199).
    - event_trade NPC say: I can sense that the sword is pleased with your progress. However there is another task it wishes you to perform. I have learned through a contact of mine, that there is to be a ceremony in Kithicor Woods. Several paladins will be converging there to try to cleanse the undead from the forest, once and for all. The blade thirsts for the blood of these paladins. Before the blade will allow you to become its champion, you must kill as many of these paladins as you can, and bring me three samples of their blood. Take the Sheathed Innoruuk's Voice back and when you have three samples of paladin's blood, hand them to me along with the Sheathed Innoruuk's Voice so that I may perform the ceremony to sate the blade's thirst. Go now and find my contact in Kithicor. His name is Tarnamil. Take the sword back for safe keeping.
      - Event guard: `(qglobals["shadowknight_epic"] == "6" and item_lib.check_turn_in(e.trade, {item1 = 20899, item2 = 16813, item3  = 16793, item4 = 20079}))`
29. kithicor/"Tarnamil", say "Hail".
    - Player: "hail"
      - NPC say: The paladins are coming from the west, my lord. The come to destroy the dead that walk at night. Already, the undead generals plot their demise, but they are powerful. They approach soon. I am getting out of here.
      - Condition: `(e.message:findi("hail") and qglobals["shadowknight_epic"] == "7")`
30. Spawns "Uglib Gaibido" (npc:20293) via `kithicor/tarnamil#hail`.
31. Kill "Uglib Gaibido" (NPC 20293) in `kithicor` and loot "Paladin Blood Sample" (20904).
32. poknowledge/"Gilina Yilzior", hand "Paladin Blood Sample" (20904) + "Sheathed Innoruuk's Voice" (22199).
    - event_trade NPC say: Well done.' Gilina takes the blood samples starts to pour them onto the blade of Innoruuk's Voice. The blade appears to become super-heated as the blood drops trickle down its surface. A thick black smoke begins to waft from the blade. 'The blade is now complete. Before I give the blade to you there is something else you must do. A mighty templar named Sir Elmonious Falmont has heard of your crimes against the paladins and seeks revenge. It is important that we let none get in the way of our goals. As we speak, he is making his way from the Western Wastes in the continent of Velious to kill us. Destroy him and return his holy symbol to me.
      - Event guard: `(qglobals["shadowknight_epic"] == "7" and item_lib.check_turn_in(e.trade, {item1 = 20904, item2 = 20904, item3  = 20904, item4 = 22199}))`
33. poknowledge/"Gilina Yilzior", hand "Sir Elmonious's Holy Symbol" (55901). Gives "Innoruuk's Voice" (50003).
    - event_trade NPC say: You have performed well. The blade is yours to wield now, champion. You may be on your way, or stay to hear about a [vision] I recently had.
      - Event guard: `(qglobals["shadowknight_epic"] == "8" and item_lib.check_turn_in(e.trade, {item1 = 55901}))`
    - event_trade NPC message: You have gained 5 ability points!

**Unresolved graph dependencies:**
- Unverified quest flag `shadowknight_epic` ==1: no acyclic setter

## Epic 2.0

### "Innoruuk's Dark Blessing" (48136)

<a id="epic-item-48136"></a>

**Earlier reward routes required by this graph path:** ["Innoruuk's Voice" (50003)](#epic-item-50003).
Revisit those instructions if another copy of a consumed item is needed.

1. Kill dranik/"A Minion Of Lhranc".
2. Spawns "Lhranc" (npc:336250) via `dranik/filligno the slayer#signal:1`.
3. Kill "Lhranc" (NPC 336250) in `dranik` and loot "Essence of the Shadowknight" (55903).
4. poknowledge/"Gilina Yilzior", say "Vision". Sets `shadowknight_epic` to `9`.
    - Player: "vision"
      - NPC say: My recent vision was of Lhranc. Perhaps you remember him, perhaps not. In any case, his spirit has returned from the dead. He now seeks revenge on those who killed him. There is something sinister behind his return. What exactly is going on, I do not know at this time, but I fear the worst. You must find Lhranc and [destroy] him.
      - Condition: `(e.other:Class() == "Shadow Knight")`
      - Condition: `(e.message:findi("vision") and e.other:HasItem(50003))`
5. Loot "Kilidna's Head" (19098) from "Kilidna" (NPC 90186) in `citymist`. Drop cache: 100% chance per kill.
6. poknowledge/"Gilina Yilzior", hand "Kilidna's Head" (19098).
    - event_trade NPC emote: takes the head from you and holds it by the hair. Gilina casts a small spell and the head springs to life.  'Talk, Kilidna. What has happened to you?' Kilidna's head begins to sob. 'I am sorry, master. I was corrupted by evil magic! Now look at me! I dare say I will not be able to finish my studies any time soon.' Gilina scowls, 'What did you find out while in the city of mist? Tell me now!' 'Well master, it seems that when Innoruuk's Voice was summoned to this plane, it drew the attention of many [powerful beings].'
      - Event guard: `(qglobals["shadowknight_epic"] == "9" and item_lib.check_turn_in(e.trade, {item1 = 19098}))`
7. Loot "Lhranc's Corroded Bracer" (24612) from "a mortiferous golem" (NPC 105021) in `charasis`. Drop cache: 1.1599% chance per kill.
8. Kill citymist/"Npc:90004".
9. Spawns "a black reaver" (npc:90004) via `citymist/npc:90004#event_death_complete`.
10. Kill "a black reaver" (NPC 90004) in `citymist` and loot "Lhranc's Pendant" (23489).
11. Loot "Lhranc's Ring" (24632) from "risen corporal" (NPC 20107) in `kithicor`. Drop cache: 19.5635% chance per kill.
12. poknowledge/"Gilina Yilzior", hand "Lhranc's Corroded Bracer" (24612) + "Lhranc's Pendant" (23489) + "Lhranc's Ring" (24632). Gives "Lhranc's Earthly Anchor" (24584).
    - event_trade NPC emote: takes the items from you and holds them before you in her hands. She mutters an incantation and the items meld into one.
      - Event guard: `(qglobals["shadowknight_epic"] == "10" and item_lib.check_turn_in(e.trade, {item1 = 24612, item2 = 23489, item3 = 24632}))`
    - event_trade NPC say: This item will be used to help anchor Lhranc to this plane of existence. The anchor will not be enough however. In an area in the Realm of Discord known as Anguish, you will need to find a globe of discordant energy. This will be used to infuse the earthly anchor with the power of discord. When you have these two items, hand them to my contact, Filligno the Slayer. He has tracked down Lhranc in Dranik, the Ruined City in the Realm of Discord. He will need your help to get Lhranc's attention however.
13. global/"Global Player", say "Recipe:19908". Gives "Globe of Discordant Energy" (47100).
14. dranik/"Filligno The Slayer", hand "Lhranc's Earthly Anchor" (24584) + "Globe of Discordant Energy" (47100).
    - event_trade NPC say: Yes, yes, Gilina said you would be coming. I can help you in your battle against Lhranc! I have a personal vendetta against Lhranc. He killed my twin brother, Gilligno. This is going to be a tough battle. Lhranc has been reincarnated as a powerful general of the Mata Muram army. Are you [ready] for me to attempt the summoning of Lhranc?
      - Event guard: `(qglobals["shadowknight_epic"] == "10" and item_lib.check_turn_in(e.trade, {item1 = 24584, item2 = 47100}))`
15. dranik/"Filligno The Slayer", hand "Essence of the Shadowknight" (55903) + "Innoruuk's Voice" (50003). Gives "Innoruuk's Dark Blessing" (48136).
    - event_trade NPC emote: takes the essence and begins to study it most carefully. After what seems like an eternity, Filligno throws the globe onto the floor. It cracks open, letting loose a stream of ghastly spirits. Filligno dives for cover. As the cackling spirits dissipate, a powerful looking sword floats in mid-air before you.
      - Event guard: `(qglobals["shadowknight_epic"] == "11" and item_lib.check_turn_in(e.trade, {item1 = 55903, item2 = 50003}))`
    - event_trade NPC say: Take it! The blade is yours! A gift from Innoruuk, for the most powerful of shadowknights!
    - event_trade NPC message: You have gained 10 ability points!

**Unresolved graph dependencies:**
- Unverified quest flag `shadowknight_epic` ==1: no acyclic setter
