# Wizard — Epic Quest Walkthrough

Generated directly from quest-graph item rewards. Unresolved dependencies are marked, not inferred.

## Epic 1.0

### "Staff of the Four" (14341)

<a id="epic-item-14341"></a>

1. halas/"Arantir Karondor", say "Hail".
    - Player: "hail"
      - NPC say: Ah yes, you again. Do you have the items? Give me the three you possess and I'll combine them with my own.
        - Reply guard: `(qglobals["wizepicB"] == "1")`
      - NPC say: Ah, but it pains my heart to see this. How I could love a women like that is beyond me. And yet, I still do love her. It was on the day I was to ask her to marry me that I lost my powers. When I was about to cast my greatest spell to prove my love to her, my magic failed. She ran out on me that day. But enough of me, do you wish to hear my story?
        - Reply guard: `(qglobals["wizepicA"] == "1")`
      - NPC say: Before I tell you anything, I require you to help me. Seek a woman named Challice. Give her this ring and then return to me.
        - Reply guard: ``
      - Condition: `(e.message:findi("hail"))`
2. Loot "Blue Crystal Staff" (14337) from "Phinigel Autropos" (NPC 64001) in `kedge`. Drop cache: 27.1049% chance per kill.
3. Loot "Gnarled Staff" (14338) from "Venril Sathir" (NPC 102112) in `karnor`. Drop cache: 50% chance per kill.
4. halas/"Arantir Karondor", say "Gnome". Gives "Note from Arantir" (18169).
    - Player: "gnome"
      - NPC say: Ah, the gnome I know very little about. I know he was small and crafty, and that he had a brother. His brother's craft was that of making fireworks, and he was the unfortunate victim of one of his own experiments. His firework exploded, leaving his mind diminished in capacity, even for a gnome. I remember others calling him 'Old Stewpot' in jest. I do not know if this is his birth name, but it may help you to locate him. I hear he also stays close to water because of the explosion. You never know when another gnomish invention will go awry. Give him this letter to help motivate him to remember.
      - Condition: `(e.message:findi("gnome") and e.other:Class() == "Wizard")`
      - Linked from "story" (explicit prompt).
5. butcher/"Kandin Firepot", hand "Note from Arantir" (18169).
    - event_trade NPC say: Brother! I have one of those. He's great, but he's dead. His name was Gabstik and he was a really powerful wizard. I still have one of his greatest possesions! You look like you could use it. I've added another thing to my shopping list. I require a dry brittle skin that I can mold or a rare oil found in the planes that I can soak the fuse in. Get me one of these things and I'll trade it for my bother's stick.
      - Event guard: `item_lib.check_turn_in(e.trade, {item1 = 18169})`
6. butcher/"Kandin Firepot", say "What Oil". Gives "Golem Sprocket" (14319).
    - Player: "what oil"
      - NPC say: Ah the oil! I recently sent a specially crafted golem to explore through a huge portal to another plane. It's instructions were to collect special oil that I suspect existed in the plane. What I think is the golem broke down. This looks like a good task for one like you. Go see what's wrong with the golem. Here is spare gears of mine incase it's broken. Be careful though, if you put it in wrong it could explode or worse!
      - Condition: `qglobals["wizepicK"] ~= nil`
      - Condition: `e.message:findi("what oil")`
      - Linked from "hail" (explicit prompt).
7. fearplane/"A Broken Golem", hand "Golem Sprocket" (14319).
    - event_trade NPC say: Error! Malfunction! Destroy!
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 14319}))`
    - event_trade NPC say: A  like you always bring out the worst in me.
8. Spawns "an enraged golem" (npc:72106) after the hand-in.
9. Kill "an enraged golem" (NPC 72106) in `fearplane` and loot "Green Oil" (14349).
10. butcher/"Kandin Firepot", hand "Green Oil" (14349). Gives "Staff of Gabstik" (14339).
    - event_trade NPC say: Oh wow! You found the oil! Where is the golem? You didn't hurt him did you? I am very fond of him. Anyways, here is your reward a note and staff to give to that guy you were asking me about.
      - Event guard: `qglobals["wizepicK"] ~= nil`
      - Event guard: `item_lib.check_turn_in(e.trade, {item1 = 14349})`
11. halas/"Arantir Karondor", hand "Blue Crystal Staff" (14337) + "Gnarled Staff" (14338) + "Staff of Gabstik" (14339). Gives "Magically Sealed Bag" (14340).
12. soltemple/"Solomen", hand "Magically Sealed Bag" (14340). Gives "Staff of the Four" (14341).
    - event_item NPC say: You actually did it! I never would have thought that anyone could have truly followed this path. This is a tribute to your intelligence and patience. Here, take this staff and know that you have made Solusek Ro and all the wizards of the world proud this day.
      - Event guard: `(quest::handin({14340 => 1}))`

## Epic 1.5

### "Staff of Prismatic Power" (12665)

<a id="epic-item-12665"></a>

1. erudnext/"Lumi Stergnon", say "Hail".
    - Player: "hail"
      - NPC say: Peace and tranquility be with you. .  Are you a [new acolyte of peace] or are you [here to pay homage] to the child of tranquility?
      - Condition: `(e.message:findi("hail"))`
2. Summon "Collapsible Sewing Kit" (17165) by casting "Unfold Sewing Kit".
3. Buy "Backpack Pattern" (12089) from "Iala Lenard" (NPC 1141) in `qeynos`. Base price: 500 copper.
4. Buy "Needle Mold" (12019) from "Dyona Rossook" (NPC 5065) in `highpass`. Base price: 180 copper.
5. Buy "Thimble Mold" (12057) from "Dyona Rossook" (NPC 5065) in `highpass`. Base price: 180 copper.
6. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
    - Player: "battle the undead"
      - NPC say: Then you shall venture to Toxxulia Forest. There has been an increase in skeleton sightings lately. I do not know their origin, but I believe that your efforts will reduce their numbers! Take this box. Return it to me when you have filled it with the bones of these undead creatures and combined it. May Quellious' light guide you.
      - Condition: `(e.message:findi("battle the undead"))`
      - Linked from "new acolyte of peace" (explicit prompt).
7. Loot "Useless Cloth Cap" (13894) from "a kobold scout" (NPC 38035) in `tox`. Drop cache: 20% chance per kill.
8. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
9. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). Requires Remove Traps.
10. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
    - event_trade NPC say: You have done well. Let it be known to all that you fight for the Rainkeeper. Go and continue the battle.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 13882}))`
11. Loot "Fine Steel Wakizashi" (6932) from "a corrupted gnome explorer" (NPC 66111) in `gukbottom`. Drop cache: 100% chance per kill.
12. Combine in appropriate tradeskill container: "Fine Steel Wakizashi" (6932), "Water Flask" (13006). Produces "Small Piece of High Quality Ore" (22229). Requires Blacksmithing.
13. Combine in appropriate tradeskill container: "Small Piece of High Quality Ore" (22229), "Water Flask" (13006). Produces "High Quality Metal Bits" (22230). Requires Blacksmithing.
14. Combine in appropriate tradeskill container: "Needle Mold" (12019), "Thimble Mold" (12057), "Water Flask" (13006), "High Quality Metal Bits" (22230). Produces "Vale Sewing Kit" (92882). Requires Blacksmithing.
15. Forage "Spiderling Silk" (13099) in `mistmoore` or `mmca` or `mmcb` or `mmcc` or `mmcd` or `mmce` or `mmcf` or `mmcg` or `mmch` or `mmci` or `mmcj`.
16. Combine in "Vale Sewing Kit" (92882): "Spiderling Silk" (13099). Produces "Silk Thread" (16486). Requires Tailoring.
17. Combine in "Vale Sewing Kit" (92882): "Silk Thread" (16486). Produces "Silk Cord" (16489). Requires Tailoring.
18. potranquility/"Kalym Rasalan", say "Hail". Gives "Silken Tapestry" (12593).
    - Player: "hail"
      - NPC say: Hello , Talwyn told me of the coming of new recruits. I suppose he told you that you would need to use the magic in our woven tapestries to create a satchel to hold something very delicate? Well, you are lucky enough that I have this finished swatch of tapestry here that you can use. I am busy and can't tailor it for you though. You will need to tailor it yourself. If you take the tapestry, a backpack pattern, and a silk cord you should be able to tailor it with moderate effort.
      - Condition: `(e.message:findi("hail") and (qglobals.wiz_epic_wisp == "1") and (qglobals.wiz_epic_shard == "1"))`
19. Combine in "Collapsible Sewing Kit" (17165): "Backpack Pattern" (12089), "Silk Cord" (16489), "Silken Tapestry" (12593). Produces "Silken Tapestry Satchel" (12596). Requires Tailoring.
20. Collect ground spawn "Prismatic Crystal" (12599) in `veksar`.
21. Collect ground spawn "Prismatic Crystal" (12625) in `timorous`.
22. Collect ground spawn "Prismatic Crystal" (12628) in `twilight`.
23. Loot "Prismatic Crystal" (12662) from "Treasure Sorter Neiben" (NPC 225031) in `dulak`. Drop cache: 100% chance per kill.
24. Loot "Cohesion Gem" (67022) from "a metallic slime" (NPC 206031) in `poinnovation`. Drop cache: 34.241% chance per kill.
25. Spawns "Spawn Wiz 1.5; Pure Flame Elemental" (npc:278108) via `soldungc/ #signal:100`.
26. Kill "Spawn Wiz 1.5; Pure Flame Elemental" (NPC 278108) in `soldungc` and loot "Wisp of Pure Flame" (11619).
27. lavastorm/"Talwyn Flamecaller", hand "Wisp of Pure Flame" (11619).
    - event_trade NPC say: You have obtained the pure flame? That was impressive how quickly you did it, the other wizards I am recruiting have not returned yet. Back to the recruitment, you will need pure ice. The ice is coldest in the wastes of Velious. Retrieve this pure ice and bring it back to me.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 11619}))`
28. Spawns "Mistress of the Darkwater Quest-only" (npc:125075) via `sirens/player#enter`.
29. Kill "Mistress of the Darkwater Quest-only" (NPC 125075) in `sirens` and loot "Shard of Pure Ice" (11599).
30. Loot "Fluxing Staff" (11445) from "Girplan Guardian" (NPC 300037) in `wallofslaughter`. Drop cache: 100% chance per kill.
31. Spawns "Elite Sun Revenant" (npc:175306) via `scarlet/the gem guardian#event_proximity_say`.
32. Kill "Elite Sun Revenant" (NPC 175306) in `scarlet` and loot "Fluxing Gem" (11448).
33. Loot "Fluxing Rune" (11474) from "Hobgoblin Horrorfiend" (NPC 204053) in `ponightmare`. Drop cache: 100% chance per kill.
34. Collect ground spawn "Fluxing Chunk of Ore" (11576) in `dranik`.
35. lavastorm/"Talwyn Flamecaller", hand "Fluxing Staff" (11445) + "Fluxing Gem" (11448) + "Fluxing Rune" (11474) + "Fluxing Chunk of Ore" (11576). Gives "Staff of Fluxing Power" (11596).
    - event_trade NPC say: You are indeed ready to join the ranks as a soldier of Solusek Ro. Every soldier in Solusek's league must wield a staff of power, which will focus your abilities in a way that you have never felt before! Fear will consume you as you feel your essence being ripped from your body. Do not give up, use the staff with faith and hope that you will be rewarded with the most [powerful item] you could ever imagine.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 11445, item2 = 11448, item3 = 11474, item4 = 11576}))`
36. Combine in "Silken Tapestry Satchel" (12596): "Prismatic Crystal" (12599), "Prismatic Crystal" (12625), "Prismatic Crystal" (12628), "Prismatic Crystal" (12662), "Cohesion Gem" (67022), "Shard of Pure Ice" (11599), "Wisp of Pure Flame" (11619), "Staff of Fluxing Power" (11596). Produces "Full Tapestry Satchel" (16753). Requires Remove Traps.
37. lavastorm/"Talwyn Flamecaller", hand "Full Tapestry Satchel" (16753). Gives "Staff of Prismatic Power" (12665).
    - event_trade NPC emote: removes the components from the tapestry satchel they begin to vibrate with power. They pulse quickly as they move towards each other, static flies in each direction as the pieces fuse into each other. In a final burst of magic the staff is complete. Talwyn looks it over with wise eyes before giving it to you.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 16753}))`
    - event_trade NPC say: The staff of power is yours to wield. If you are up to the task I can set you on the final portions of what is needed to become a true avatar of Solusek.
    - event_trade NPC message: You have gained 5 ability points!

## Epic 2.0

### "Staff of Phenomenal Power" (16576)

<a id="epic-item-16576"></a>

**Earlier reward routes required by this graph path:** ["Staff of Prismatic Power" (12665)](#epic-item-12665).
Revisit those instructions if another copy of a consumed item is needed.

1. global/"Global Player", say "Recipe:19908". Gives "Globe of Discordant Energy" (47100).
2. lavastorm/"Talwyn Flamecaller", say "Hail". Sets `wiz_epic20` to `1`.
    - Player: "hail"
      - NPC say: The power of the wizard courses through your veins thoroughly, ever in search of the opportunity to harness even more power. You have created a staff of immense power, yet even in its glory, is limited. To unleash the full potential of this weapon will be a large undertaking of its own. You must obtain a globe of pure discordant energy and return it to me. Look for assistance from the Plane of Discord from Grathnok Gilforgan. I know not where this being may be, but I do know that once you find him, he will be willing to assist you in finding the globe you seek.
      - Condition: `(e.message:findi("hail") and e.other:HasItem(12665))`
3. draniksscar/"Grathnok Gilforgan", say "Intricate Horn Of Galien". Sets `wiz_epic20` to `2`.
    - Player: "intricate horn of galien"
      - NPC say: This precious artifact was placed on our largest tower, where its resonating voice stretched across the planes and through the mountains to rally our troops and warn us of an impending attack. The horn has tremendous sentimental value for us, as it belonged to one of the great leaders of our past. It is a horn made of the finest precious metals of our homeland, laden with runes and etchings and filled with gems and precious stones. It is a signification of our strength and perseverance over the ages and without it the morale is very low amongst our soldiers.
      - Condition: `(qglobals["wiz_epic20"] ~= nil and qglobals["wiz_epic20"] >= "1")`
      - Condition: `(e.message:findi("Intricate Horn of Galien"))`
      - Linked from "Lose your hold" (explicit prompt).
4. Loot "Intricate Horn of Galien" (15825) from "Lightningcaller Vhalek" (NPC 316034) in `provinggrounds`. Drop cache: 100% chance per kill.
5. draniksscar/"Grathnok Gilforgan", hand "Intricate Horn of Galien" (15825).
    - event_trade NPC say: Your resolve and strength of will astounds me. You have returned to my people, the most sacred artifact we have on this world, and for that, you have earned my gratitude. As promised, I will give you the information that I have on the discordant globes. These globes can only be collected in one area, where the magic of discord constantly fluxes and an eerie sense of pain and anguish resides. Beware, it is an extremely dangerous area, protected by many of the Muramite Army's best and highest ranking members. Good luck to you, I hope you achieve all that you aspire.
      - Event guard: `(qglobals["wiz_epic20"] ~= nil and qglobals["wiz_epic20"] >= "2")`
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 15825}))`
6. lavastorm/"Talwyn Flamecaller", hand "Globe of Discordant Energy" (47100). Gives "Broken Orb of Discordant Energy" (16147) + "Broken Orb of Discordant Energy" (15836).
    - event_trade NPC say: To obtain this globe was no trivial task, yet you have prevailed! Your staff is nearly complete now, you have only two final tasks remaining.', he says as he begins to murmur a brief incantation. Without warning, the orb splits into two equal halves and are then given to you. They will infuse your staff with one of the most useful powers of a wizard; teleportation.'
      - Event guard: `(qglobals["wiz_epic20"] ~= nil and qglobals["wiz_epic20"] >= "3" and item_lib.check_turn_in(e.trade, {item1 = 47100}))`
7. Combine recipe 19894 (container 16695): "Broken Orb of Discordant Energy" (16147). Produces "Infused Orb of Discordant Energy" (16451). Requires Remove Traps.
8. Combine recipe 19895 (container 16765): "Broken Orb of Discordant Energy" (15836). Produces "Infused Orb of Discordant Energy" (16334). Requires Remove Traps.
9. lavastorm/"Talwyn Flamecaller", hand "Infused Orb of Discordant Energy" (16451) + "Infused Orb of Discordant Energy" (16334) + "Staff of Prismatic Power" (12665). Gives "Staff of Phenomenal Power" (16576).
    - event_trade NPC say: With these Infused Orbs, your path to becoming a soldier of Solusek's legions has been completed. You have surpassed even my expectations!' he says. You hear Talwyn chant in low, almost inaudible tones. His hands glow bright with power as he assembles a weapon worthy of Solusek himself. 'Take this staff as a symbol of your loyalty to Solusek and wield it proudly, wizard!
      - Event guard: `(qglobals["wiz_epic20"] == "4" and item_lib.check_turn_in(e.trade, {item1 = 16451, item2 = 16334, item3 = 12665}))`
    - event_trade NPC message: You have gained 10 ability points!
