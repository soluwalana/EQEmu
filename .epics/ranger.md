# Ranger

Steps taken from the quest graph only. **Broken** means the graph has no edge for that value or that item.

Flags with writes: `ranger_epic`, `ranger_epic15_pre`.

## 0. Prerequisites

Shared acquisition steps appear in the first prerequisite chain that needs them. Later sections reference that chain rather than repeating it.

### "Swiftwind" (20487)

1. burningwood/"Telin Darkforest", say "Action". Gives "Worn Note" (20472).
    - Dialogue with burningwood/"Telin Darkforest":
      - Player: "Hail"
        - NPC emote: looks at you serenely. 'Hello, wanderer.'
        - Condition: `(fac < 4)`
        - Condition: `(e.message:findi("hail"))`
      - Player: "What Are You Doing" (link: conversation sequence)
        - NPC say: Mighty this place must have been, once. Now scarred by hatred and suffering. I have been sent here seeking answers to problems not yet understood.
        - Condition: `(fac < 4)`
        - Condition: `(e.message:findi("what are you doing"))`
      - Player: "Answers" (link: explicit mention)
        - NPC emote: considers you for a few moments before speaking. 'A great evil walks across the land. The hand of some demon we don't yet know is twisting and polluting forests.'
        - Condition: `(fac < 4)`
        - Condition: `(e.message:findi("answers"))`
      - Player: "Evil" (link: explicit mention)
        - NPC say: If I knew that, I wouldn't be here looking for answers. I would be elsewhere, looking for solutions. For now, I suspect much but know little.
        - Condition: `(fac < 4)`
        - Condition: `(e.message:findi("evil"))`
      - Player: "Suspect" (link: explicit mention)
        - NPC emote: looks at you and sighs. 'The lands are changing. Beasts, large and small, have turned upon those who watched over them. Druids and rangers, worshippers of both Karana and Tunare, have reported a feeling of hatred throughout their once peaceful lands.'
        - Condition: `(fac < 4)`
        - Condition: `(e.message:findi("suspect"))`
      - Player: "Innoruuk" (link: lore association)
        - NPC emote: raises his eyebrow slightly and a subtle look of surprise creeps across his face. 'Innoruuk? Perhaps. Aye. It must be. Perhaps I knew and didn't want to consider the possibility. It must be this though, and some action will have to be taken.'
        - Condition: `(fac < 4)`
        - Condition: `(e.message:findi("innoruuk"))`
      - Player: "Action" (link: explicit mention)
        - NPC emote: looks at you consideringly and then scribbles something quickly on a small, worn paper. 'You seem powerful enough. Perhaps you can help those who seek to protect nature's peace. Take this note. Deliver it only into the hands of Faelin Bloodbriar. Where you will find her, I cannot say. She is a friend of mine and a wanderer. She has been seen from one end of the lands to the other. Seek her out, and quickly.'
          - Reply guard: `(e.other:GetLevel() >= 46)`
        - NPC say: You are not yet powerful enough to complete this task. Return when you have gained more experience.
          - Reply guard: ``
        - Condition: `(fac < 4)`
        - Condition: `(e.message:findi("action"))`
        - Gives Worn Note (20472).
2. gfaydark/"Faelin Bloodbriar", hand "Worn Note" (20472). Gives "Faelin's Ring" (20446).
3. kithicor/"Giz X-Tin", hand "Faelin's Ring" (20446). Gives "Dark Metal Coin" (20447).
4. burningwood/"Telin Darkforest", hand "Dark Metal Coin" (20447). Gives "Worn Dark Metal Coin" (20448).
5. eastkarana/"Althele", hand "Worn Dark Metal Coin" (20448). Gives "Braided Grass Amulet" (20450).
6. eastkarana/"Sionae", hand "Braided Grass Amulet" (20450). Gives "Frayed Braided Grass Amulet" (20451).
7. eastkarana/"Teloa", hand "Frayed Braided Grass Amulet" (20451). Triggers `eastkarana/althele#signal:1`.
8. Starts timer `attack`.
9. Spawns "Corruptor" (15153) after `eastkarana/althele#timer:attack`.
10. Loot "Fleshbound Tome" (20452) from "Corruptor".
11. eastkarana/"Althele", hand "Fleshbound Tome" (20452). Gives "Earth Stained Note" (18959).
12. misty/"Ella Foodcrafter", hand "Earth Stained Note" (18959). Sets `shiny_tin_bowl` to `1`.
    - Dialogue with misty/"Ella Foodcrafter":
      - Player: "Hail"
        - NPC say: Hi, hi. I've got a lot to do, many mouths to feed, some filthy goblins to smack. If you don't need me for something, please let me go back to my work. Karana watch over you.
        - Condition: `($text=~/hail/i)`
      - Player: "Two Tasks" (link: conversation sequence)
        - NPC say: Well, ya ask before ya act. That's a good sign. What I need isn't easy to find. First, I need a mixture. Plain sounding enough but it's a special one. Cleanses the mind and focuses the earth's energies into a forest walker's mind. I don't know how to make it. I don't even know what it's called. I merely know it exists and we'll be needing it for our task. When ya do find how to make it ya can mix it in that bowl. Keep it when you're done, it's a good bowl.
        - Condition: `(($text=~/two tasks/i) && (defined $qglobals{shiny_tin_bowl}))`
        - Gives Shiny Tin Bowl (17860).
      - Player: "Second Task" (link: conversation sequence)
        - NPC say: Good, ya didn't run off without finding out what else ya need to do. Second, I need a special type of bowl. An ancient type of bowl, which strengthened the food placed inside it, once made by the elves of old. Again, I cannot tell ya how it is made for the making was lost to the ages. Seek this knowledge and these items out in the lands. Come to me when ya have found both.
        - Condition: `($text=~/second task/i)`
13. misty/"Ella Foodcrafter", say "Two Tasks". Requires `shiny_tin_bowl` set. Gives "Shiny Tin Bowl" (17860).
14. Forage "Ripened Heartfruit" (20464) in `gfaydark`.
15. Forage "Sweetened Mudroot" (20465) in `misty`.
16. Forage "Sweetened Mudroot" (20465) in `mistythicket`.
17. Forage "Speckled Molded Mushroom" (20466) in `innothule`.
18. Forage "Chilled Tundra Root" (20467) in `everfrost`.
19. Combine in "Shiny Tin Bowl" (17860): "Ripened Heartfruit" (20464), "Sweetened Mudroot" (20465), "Speckled Molded Mushroom" (20466), "Chilled Tundra Root" (20467). Produces "Hardened Mixture" (20473). Requires Pottery. The combine does not fail.
20. timorous/"Alrik Farsight", say "Take The Artifact". Gives "Crushed Pot" (20457).
    - Dialogue with timorous/"Alrik Farsight":
      - Player: "Hail"
        - NPC say: Ah. Hello there, adventurer. Come to search for ancient artifacts with Fizzlebik and myself?
        - Condition: `($faction < 5)`
        - Condition: `($text=~/hail/i)`
      - Player: "Ancient Artifact" (link: conversation sequence)
        - NPC say: Oh. All types of things. This area is great. So many artifacts and remains of things all over. It's starting to fall into the pattern of things.
        - Condition: `($faction < 5)`
        - Condition: `($text=~/ancient artifact/i)`
      - Player: "Ancient Bowl" (link: conversation sequence)
        - NPC emote: rummages through his tattered bag and throws aside a towel. 'Too many towels. Oh well, someone told me they were good to have once. Here it is, a bowl pattern. Interesting bowl. Looks almost like a magical bowl but I'm no potter. You need it, you say? Well, it is interesting. Part of my research here is for the wizard guild in Felwithe. I'm sure they'd put a high price on this one, the enchanters guild being so interested in trading for magical paraphernalia and all. Of course if you helped me out on a chore I have, I'd be happy to give it to you. I need to deliver an artifact to the guild and I'd much rather stay here exploring. If you wish, you can take the artifact and return with the receipt and I'll give you the pattern.'
        - Condition: `($faction < 5)`
        - Condition: `($text=~/ancient bowl/i)`
      - Player: "Take The Artifact" (link: explicit mention)
        - NPC say: Hah! Okay, then. Here take this to Farios Elianos in Felwithe. He will give you the receipt.
        - Condition: `($faction < 5)`
        - Condition: `($text=~/take the artifact/i)`
        - Gives Crushed Pot (20457).
21. felwitheb/"Farios Elianos", hand "Crushed Pot" (20457). Gives "Grocery List" (20458).
22. felwithea/"Merchant Nora", hand "Grocery List" (20458). Gives "Bag of Provisions" (20459).
23. felwitheb/"Farios Elianos", hand "Bag of Provisions" (20459). Gives "Receipt" (20474).
24. timorous/"Alrik Farsight", hand "Receipt" (20474). Gives "Ancient Pattern" (18960).
25. Kill citymist/"A Black Reaver". Spawns "A Black Reaver" (90004).
26. Loot "Jade Reaver" (5664) from "A Black Reaver".
27. Alternative: Loot "Jade Reaver" (5664) from "A Black Reaver" (NPC 90005) in `citymist`; trigger: citymist/"A Black Reaver", on event_death_complete.
28. Alternative: Loot "Jade Reaver" (5664) from "A Black Reaver" (NPC 90192) in `citymist`; trigger: citymist/"A Black Reaver", on event_death_complete.
29. kaladimb/"Kinlo Strongarm", hand "Jade Reaver" (5664). Gives "Enchanted Clay" (20455).
    - Dialogue with kaladimb/"Kinlo Strongarm":
      - Player: "Mud"
        - NPC say: Eh? Oh, the clay. Arrr. Lots o' that mud round 'ere. Mostly, a good dwarf not be needin' somethin' so soft 'n squishy but the womenfolk, you know, the elves come lookin' fer it. If ye be one o' those pansy elves wantin' some mud fer workin' into fairy statues, flashy trinkets, 'n pig sticker arrers then I can get it for ye. Course I'd be lowerin' meself, a good dwarf, ta be diggin' that kinda mush outta the ground, but I can do it fer ya.
        - Condition: `($faction <= 5)`
        - Condition: `($text=~/mud/i)`
      - Player: "Do It For Me" (link: conversation sequence)
        - NPC say: Arrr. Shaddap. I ain't doin' it til ya bring me somethin'. A fee, I guess ye'd call it, fer lowerin' meself ta elf woman work. Go get me a good strong axe and I'll do it fer ye. Mebbe somethin' with a good tinted polish on it. I got plenty o' axes but no tinted ones. Har har! Colored axe. Somethin' to go with the color left on the blade after I be crackin open a gobbo head.
        - Condition: `($faction <= 5)`
        - Condition: `($text=~/do it for me/i)`
      - Player: "Ancient Longsword" (link: conversation sequence)
        - NPC say: The ancient smiths, for what I think yer askin' about, ain't been around fer a long time, laddy. Last anyone heard o' the ancients was 'fore my time even. There be more than a few tales about 'em.
        - Condition: `($faction <= 5)`
        - Condition: `($text=~/ancient longsword/i)`
      - Player: "Tales" (link: explicit mention)
        - NPC say: There be some who talk about how the ancient smiths went down to work fer the Duke o' Below, sayin' he be needin' some fine dwarven smiths fer makin' some castle or some such. There be tales that the ancients were so good at smithin' that the Duke took 'em down and made 'em head smiths over his minions. There's even tales that some o' the smiths' souls were trapped in their hammers, stuck there by some necromancer or somethin', as punishment or retribution.
        - Condition: `($faction <= 5)`
        - Condition: `($text=~/tales/i)`
      - Player: "Trapped In Their Hammers" (link: explicit mention)
        - NPC say: Aye. Some says their souls were bound into their hammers by an Erudite necromancer and enchanter. They say they used the power of the hammers ta profit by makin' ships, boats, and houses better than any other merchants. Sad tale, if'n it be true.
        - Condition: `($faction <= 5)`
        - Condition: `($text=~/trapped in their hammers/i)`
      - Player: "Necromancer And Enchanter" (link: explicit mention)
        - NPC say: I'm not knowin' more about the story, lad. Everythin' I know is already in what I said. Aye, Erudites. I suppose if yer wantin' ta run after shortbeard tales ya can look over on that plague island they call Odus.
        - Condition: `($faction <= 5)`
        - Condition: `($text=~/necromancer and enchanter/i)`
      - Player: "Rock" (link: conversation sequence)
        - NPC say: Aye, good stuff ta be workin' with.
        - Condition: `($faction <= 5)`
        - Condition: `(($text=~/rock/i) || ($text=~/gem/i) || ($text=~/metal/i))`
      - Player: "Gem" (link: conversation sequence)
        - NPC say: Aye, good stuff ta be workin' with.
        - Condition: `($faction <= 5)`
        - Condition: `(($text=~/rock/i) || ($text=~/gem/i) || ($text=~/metal/i))`
      - Player: "Metal" (link: conversation sequence)
        - NPC say: Aye, good stuff ta be workin' with.
        - Condition: `($faction <= 5)`
        - Condition: `(($text=~/rock/i) || ($text=~/gem/i) || ($text=~/metal/i))`
      - Player: "Arrrr" (link: conversation sequence)
        - NPC say: Har, har! Ooooo! Arrrrrr!
        - Condition: `($faction <= 5)`
        - Condition: `($text=~/arrrr/i)`
30. Forage "Rose of Firiona" (12774) in `firiona`.
31. qrg/"Merdan Fleetfoot", hand "Rose of Firiona" (12774). Gives "Wood Painting" (20475).
    - Dialogue with qrg/"Merdan Fleetfoot":
      - Player: "Hail"
        - NPC say: Yes Niera! Oh. Erm. Hi. I mean, uh. How are you?
        - Condition: `(e.message:findi("hail"))`
      - Player: "Niera" (link: explicit mention)
        - NPC emote: blushes. 'She is, uh.. I don't know. I haven't been able to speak with her. She has many suitors, and I'm just another poor ranger. I spend my days here pretending to fish, to carve bows, but really I'm just waiting to catch a glimpse of her. I thought about adventuring into the world to find some kind of token to give her, to show her how I feel, but I can't tear myself away from here.'
        - Condition: `(e.message:findi("niera"))`
32. frontiermtns/"A Human Skeleton", hand "Wood Painting" (20475). Gives "Silver Chained Locket" (20476).
33. qrg/"Niera Farbreeze", hand "Silver Chained Locket" (20476). Gives "Platinum Speckled Powder" (20456).
    - Dialogue with qrg/"Niera Farbreeze":
      - Player: "Tune"
        - NPC say: Ohh. Just a little song my mother taught me when I was young. It speaks of the earth, the sky, and the sparkling stars above, always there.
        - Condition: `(e.message:findi("tune") or e.message:findi("humming"))`
      - Player: "Humming" (link: conversation sequence)
        - NPC say: Ohh. Just a little song my mother taught me when I was young. It speaks of the earth, the sky, and the sparkling stars above, always there.
        - Condition: `(e.message:findi("tune") or e.message:findi("humming"))`
      - Player: "Always There" (link: explicit mention)
        - NPC say: Aye, always there. Like this small bag I wear around my neck. The last gift of my dying mother. It holds a fine dust, a dust she collected during her short life, that she believed brought her luck. It's speckled, flecked as the night sky is with stars.
        - Condition: `(e.message:findi("always there"))`
      - Player: "Speckled Flecked Dust" (link: conversation sequence)
        - NPC say: I've had this little bit of dust, all I have of my mother, for many years now. It's the only reminder I have of her. She said it was special, magical, a warmth to help me through the nights. Even if my life were in the balance, I would have a hard time giving it up.
        - Condition: `(e.message:findi("speckled flecked dust"))`
      - Player: "Idea" (link: conversation sequence)
        - NPC say: Well, you could enlist the aid of the animals. Unfortunately, you can't get a lot of useful information out of a fish or a bird in normal circumstances. There might be a way, however, to get some very specific information. There is lore that suggests that a simple charm can be made that will allow you to know the thoughts of a befriended animal, but only about a particular subject. You need four things, magical clay, a body part from the animal you wish to befriend, something on the subject that you wish to know about and some water. You also need to use a kiln, so I hope you are a talented potter. Now, this only works on the animal from which the body part is taken or one of its direct descendents. You may have to try a lot of animals to find the right one.
        - NPC say: You already have a body part from an alligator in Feerrott. There is magical clay to be found in Taelosia, from what I hear. All you need then is something to focus the animal's mind on. Food is probably the best thing. Gators eat just about anything, so there's a chance you can find one that knows where that intruder with the grass ended up if you can get an alligator to tell you where it's eaten. I'd suggest a good slab of the best piranha meat you can find. It's worth a try. At this point any help would be good. I've been looking at this disease and it is nasty in a subtle way. It barely infects the plants, causes them little harm, but it spreads quickly. So quickly, in fact, that it must be magical. We need more information to stop it.
        - Condition: `(e.message:findi("idea") and e.other:HasItem(62817))`
34. Combine in Pottery Wheel (21): "Ancient Pattern" (18960), "Enchanted Clay" (20455), "Platinum Speckled Powder" (20456). Produces "Runecrested Bowl" (20460). Requires Pottery. The combine does not fail.
35. misty/"Ella Foodcrafter", hand "Runecrested Bowl" (20460) + "Hardened Mixture" (20473). Gives "Softly Glowing Stone" (20462).
36. Buy "Spell: Resurrection" (15392) from "Henlom Visrek" (NPC 2054) in `qeynos2`. Base price: 18,936 copper.
37. Hand "Spell: Resurrection" (15392) to karnor/"Spirit Of Venril Sathir". Spawns "Venril Sathir" (102126). Loot "Pulsing Green Stone" (20461) from "Venril Sathir".
38. firiona/"Foloal Stormforest", hand "Pulsing Green Stone" (20461) + "Softly Glowing Stone" (20462). Gives "Warmly Glowing Stone" (20468).
    - Dialogue with firiona/"Foloal Stormforest":
      - Player: "Are You One Such As Myself"
        - NPC emote: stares at you and whispers. 'You must be the one that has been spoken of. Yes, yes I am one of the circle. There are many of us in the lands right now, all seeking answers to the ills that have befallen our homes.'
        - Condition: `($text=~/are you one such as myself/i)`
      - Player: "Answers" (link: explicit mention)
        - NPC say: I have heard whispers of new Iksar movements in the land. The name of Venril Sathir is on the scaled lips and sharp tongues of every cold blooded lizard in this place.
        - Condition: `($text=~/answers/i)`
      - Player: "Venril Sathir" (link: explicit mention)
        - NPC say: All I've heard are whispers of connections between the undead lizards and the dark god of hate. There's some kind of history behind the two. It might be that Venril is the main focus of Innoruuk's will in the land. Then again, maybe not, but this is the best we've gotten so far. If you think you can do it, then find him and remove him from the face of this earth. Bring me the half of the stone I know you have and whatever conduit of power you find on his rotting corpse.
        - Condition: `($text=~/venril sathir/i)`
39. burningwood/"Telin Darkforest", hand "Warmly Glowing Stone" (20468). Gives "Ancient Longsword" (20477).
40. kaladimb/"Usbak The Old", hand "Ancient Longsword" (20477). Gives "Refined Ancient Sword" (20481).
    - Dialogue with kaladimb/"Usbak The Old":
      - Player: "Hail"
        - NPC say: Took ya long enough! Ye'd think ya had an Orc head on them shoulders there. I'm owin' ya for yer help though. Else I'd have been on that darn hammer for ages. Ye said ya had an ancient blade or somethin ta be smithin. If so lemme see it.
        - Condition: `($text=~/hail/i)`
41. burningwood/"Faelin Bloodbriar", hand "Refined Ancient Sword" (20481). Gives "Swiftwind" (20487).
    - Dialogue with burningwood/"Faelin Bloodbriar":
      - Player: "Hail"
        - NPC say: Didn't think I was gone for good, did you? We're that much closer to finishing this trial of our strength, thanks to you.
        - Condition: `(e.message:findi("hail"))`

### "Earthcaller" (20488)

1. Acquisition of "Shiny Tin Bowl" (17860) is documented under "Swiftwind" (20487); obtain another copy if needed.
2. Hand "Shiny Tin Bowl" (17860) to hole/"Jaeil The Wretched". Spawns "Jaeil the Insane" (39154). Loot "Soulbound Hammer" (20478) from "Jaeil the Insane".
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
17. Alternative: Loot "Shattered Emerald of Corruption" (20484) from "Maestro of Rancor" (NPC 186111) in `hateplaneb`; trigger: hateplaneb/"Maestro", on timer popmaestro.
18. northkarana/"Xanuusus", hand "Refined Mithril Blade" (20483) + "Shattered Emerald of Corruption" (20484). Gives "Earthcaller" (20488).

### "Polished Blasted Stone" (62603)

1. nedaria/"Targen Stonefall", say "Native Stones". Sets `ranger_epic15_pre` to `1`.
2. Forage "Blasted Stone" (62601) in `bloodfields`.
3. nedaria/"Targen Stonefall", hand "Blasted Stone" (62601). Sets `ranger_epic15_pre` to `2`.
4. nedaria/"Targen Stonefall", say "Odus". Sets `ranger_epic15_pre` to `3`.
5. Spawns "Stone Collector" (39168) in `hole` on enter.
6. Loot "Dusty Stone" (62653) from "Stone Collector".
7. hole/"Player", on loot. Sets `ranger_epic15_pre` to `4`.
8. nedaria/"Targen Stonefall", say "Bloodfields". Requires `ranger_epic15_pre` ==2. Gives "Sample Cloth" (62640).
9. nedaria/"Targen Stonefall", say "Bloodfields". Requires `ranger_epic15_pre` ==2. Gives "Targen's Emulsion" (62639).
10. Combine in "Sample Cloth" (62640): "Targen's Emulsion" (62639), "Dusty Stone" (62653). Produces "Rock of Odus" (62606). The combine does not fail.
11. nedaria/"Targen Stonefall", hand "Blasted Stone" (62601). Requires `ranger_epic15_pre` ==1. Gives "Washed Blasted Stone" (62602).
12. Combine in "Sample Cloth" (62640): "Rock of Odus" (62606), "Washed Blasted Stone" (62602). Produces "Closed Sample Cloth" (62641). The combine does not fail.
13. nedaria/"Targen Stonefall", hand "Closed Sample Cloth" (62641). Sets `ranger_epic15_pre` to `5`.
14. nedaria/"Targen Stonefall", say "Impurities". Requires `ranger_epic15_pre` ==5. Gives "Polished Blasted Stone" (62603).

### "Sound Capture Jar" (62637)

1. nedaria/"Targen Stonefall", say "Impurities". Sets `ranger_epic15_pre` to `6`.
2. Acquisition of "Polished Blasted Stone" (62603) is documented under "Polished Blasted Stone" (62603); obtain another copy if needed.
3. northkarana/"Xanuusus", hand "Polished Blasted Stone" (62603). Sets `ranger_epic15_pre` to `7`.
4. Loot "Taskmaster's Cutlass" (62631) from "Taskmaster Waggad Brokenskull" in `torgiran`.
5. torgiran/"Player", on loot. Sets `ranger_epic15_pre` to `8`.
6. Say "Ready" to northkarana/"Xanuusus".
7. Spawns "A Tainted Beast" (13131).
8. Loot "Stone of Winde" (62604) from "A Tainted Beast".
9. northkarana/"Xanuusus", hand "Stone of Winde" (62604). Sets `ranger_epic15_pre` to `9`.
10. steamfont/"Godbin Strumharp", hand platinum:30. Requires `ranger_epic15_pre` ==9. Gives "Sound Capture Jar" (62637).
    - Dialogue with steamfont/"Godbin Strumharp":
      - Player: "Mera"
        - NPC say: Mera? Sure, I know her. Bright girl. She left here a while ago with one of my new [
        - Condition: `(e.other:Class() == "Ranger")`
        - Condition: `( qglobals["ranger_epic15_pre"] == "9" )`
        - Condition: `(e.message:findi("mera"))`
      - Player: "Sound Capture Jars" (link: conversation sequence)
        - NPC say: The sound capture jar does exactly what it sounds like it does. If you use it properly, you can capture a sound in the jar for use later. I haven't worked out the details about how exactly you might use a sound, but I'm sure I'll figure something out. I have a few with me. They aren't part of my regular inventory, but I can sell you one if you need it for something. Seeing as you're a friend of Mera, I'll let you have it for cost, thirty platinum.
        - Condition: `(e.other:Class() == "Ranger")`
        - Condition: `( qglobals["ranger_epic15_pre"] == "9" )`
        - Condition: `(e.message:findi("sound capture jars"))`

### "Closed Sample Cloth" (62641)

1. Acquisition of "Closed Sample Cloth" (62641) is documented under "Polished Blasted Stone" (62603); obtain another copy if needed.

### "Stone of Winde" (62604)

1. Acquisition of "Stone of Winde" (62604) is documented under "Sound Capture Jar" (62637); obtain another copy if needed.

### "Heartwood Blade" (62627)

1. Buy "Planar Fletching Kit" (17762) from "Ellis Cloudchaser" (NPC 202076) in `poknowledge`. Base price: 1,000 copper.
2. global/"Global Player", combine recipe 13412. Sets `ranger_epic` to `3`.
3. jaggedpine/"Red Dogwood Treant", say "Hail". Requires `ranger_epic` ==3. Gives "Red Dogwood Heartwood" (62623).
    - Dialogue with jaggedpine/"Red Dogwood Treant":
      - Player: "Hail"
        - NPC emote: looks about for a moment. It peers at the sky and the earth for a while. It then looks down and says, We finally meet. Thank you for helping me to grow. I understand that I have been blessed by spirits of rain and earth and that is why I can speak to you and move. You have given me much, my friend. Now I would give something to you. The great treant gently pulls a small piece of wood from its bole. The wood is hard and dark. It then reaches down with one of its high branches and plucks a singular flower, smaller and of blue color that differs from the white of the others. The petals fall from the flower as he reaches out and hands you these two items. I have been with you and your people for a while. I know what you seek. That seed will grow the plant you need. The heartwood is for you. May it serve you well.
        - Condition: `(e.message:findi("hail") and treesize>=8 and qglobals["ranger_epic"] == "3")`
        - Gives Red Dogwood Heartwood (62623).
        - Gives Spring Dogwood Seed (62624).
4. dranik/"Ranger 1 5", hand "Red Dogwood Heartwood" (62623). Requires `ranger_dranik_chest` unset. Gives "Wind-blessed Heartwood" (62626).
5. jaggedpine/"Red Dogwood Treant", say "Hail". Requires `ranger_epic` ==3. Gives "Spring Dogwood Seed" (62624).
6. qrg/"Corun Finisc", hand "Spring Dogwood Seed" (62624). Gives "Block of Purest Silver" (62625).
    - Dialogue with qrg/"Corun Finisc":
      - Player: "Hail"
        - NPC say: Hello. My name is Corun Finisc and I am one of the Jaggedpine Treefolk. It is our divine responsibility to watch over and protect Surefall Glade and its [
        - Condition: `(e.message:findi("hail"))`
      - Player: "Inhabitants" (link: conversation sequence)
        - NPC say: The bears of Surefall Glade are our brothers. We are all children of [
        - Condition: `(e.message:findi("inhabitants"))`
      - Player: "Tunare" (link: conversation sequence)
        - NPC say: Tunare is the Mother of All. It is though Her will that we protect this land and its many creatures.
        - Condition: `(e.message:findi("tunare"))`
      - Player: "Destroy" (link: conversation sequence)
        - NPC say: Poachers in seach of bear skins and [gnolls] who attack us unprovoked. We are doing all we can to stop them. May [
        - Condition: `(e.message:findi("destroy"))`
      - Player: "Crook" (link: conversation sequence)
        - NPC say: My crook? The Jaggedpine crook is an enchanted weapon of the Jaggedpine Treefolk. The [
        - Condition: `(e.message:findi("crook"))`
      - Player: "Sabertooths" (link: conversation sequence)
        - NPC say: The Sabertooths are a vicious band of gnolls who live in Blackburrow, to the east of Surefall Glade. They constantly attack us when we only seek to share this land with them. They also send many patrols out into the Qeynos Hills to the south. We have even seen a Sabertooth skulking about in the caves behind Grizzly Falls. There is a [
        - Condition: `(e.message:findi("Sabertooths"))`
      - Player: "Reward" (link: conversation sequence)
        - NPC say: Yes. We are offering a small reward for slaying the skulking gnoll in the bear caves. Bring me his paw to claim your bounty. The Jaggedpine Treefolk remember well those who aid their cause.
        - Condition: `(e.message:findi("reward"))`
      - Player: "Sabertooths" (link: conversation sequence)
        - NPC say: The gnolls of Blackburrow are called Sabertooths. They have been seen in force on a regular basis. They are surely up to something.
        - Condition: `(e.message:findi("sabertooths"))`
7. Combine in "Planar Fletching Kit" (17762): "Wind-blessed Heartwood" (62626), "Block of Purest Silver" (62625). Produces "Heartwood Blade" (62627). Requires Fletching. The combine does not fail.

### "Corun's Notes" (62617)

1. Forage "Sickly Maiden's Hair" (62810) in `rathemtn`.
2. eastkarana/"Althele", hand "Sickly Maiden's Hair" (62810). Gives "Tuft of Sickly Maiden's Hair" (62811).
3. qrg/"Corun Finisc", hand "Tuft of Sickly Maiden's Hair" (62811). Gives "Borrowed Medicine Bag" (62605).
4. eastkarana/"Althele", say "Hail". Sets `ranger_epic` to `1`.
5. Spawns "An Asteatotic Highborn" (109907) in `veksar` on enter.
6. Loot "Asteatotic Veksar Blood" (35100) from "An Asteatotic Highborn".
7. Spawns "A Neuralgic Huntress" (120136) in `westwastes` on enter.
8. Loot "Neuralgic Wyvern Blood" (72605) from "A Neuralgic Huntress".
9. Summon "Collapsible Fletching Kit" (17189) by casting "Unfold Fletching Kit".
10. qrg/"Corun Finisc", hand "Tuft of Sickly Maiden's Hair" (62811). Gives "Magical Sample Vial" (62657).
11. cazicthule/"A Sickly Mosquito", on event hp.
12. Starts timer `check`.
13. Acquisition of "Planar Fletching Kit" (17762) is documented under "Heartwood Blade" (62627); obtain another copy if needed.
14. Buy "Whittling Knife" (62608) from "Yoen Ormard" (NPC 279110) in `abysmal`. Base price: 50 copper.
15. Forage "Fallen Tree Branch" (62652) in `dranik`.
16. Forage "Fallen Tree Branch" (62652) in `draniksscar`.
17. Combine in "Planar Fletching Kit" (17762): "Whittling Knife" (62608), "Fallen Tree Branch" (62652). Produces "Long Net Pole" (62607). Requires Fletching 100. Trivial at 15. The combine does not fail.
18. Spawns "A Phase Spider" (123190) in `necropolis` on event_combat.
19. Loot "Phase Spider Silk" (55303) from "A Phase Spider".
20. Forage "Pine Sap" (62650) in `jaggedpine`.
21. Forage "Pine Sap" (62650) in `nedaria`.
22. Forage "Pine Sap" (62650) in `qrg`.
23. Combine in "Planar Fletching Kit" (17762): "Phase Spider Silk" (55303), "Pine Sap" (62650). Produces "Phase Netting" (62651). Requires Fletching 100. Trivial at 15. The combine does not fail.
24. Combine in "Planar Fletching Kit" (17762): "Long Net Pole" (62607), "Phase Netting" (62651). Produces "Large Butterfly Net" (62646). Requires Fletching 100. Trivial at 15. The combine does not fail.
25. Equip "Large Butterfly Net" (62646) in primary slot.
26. cazicthule/"A Sickly Mosquito", on timer check. Gives "Captured Mosquito" (62642).
27. Combine in "Collapsible Fletching Kit" (17189): "Magical Sample Vial" (62657), "Captured Mosquito" (62642). Produces "Sickly Mosquito Blood Sample" (62611). Requires Fletching. The combine does not fail.
28. sirens/"A Twitching Swordfish", on event hp.
29. Starts timer `check`.
30. Equip "Large Butterfly Net" (62646) in primary slot.
31. sirens/"A Twitching Swordfish", on timer check. Gives "Captured Swordfish" (62643).
32. Combine in "Collapsible Fletching Kit" (17189): "Magical Sample Vial" (62657), "Captured Swordfish" (62643). Produces "Twitching Swordfish Blood Sample" (62612). Requires Fletching. The combine does not fail.
33. chardokb/"A Leprous Chokidai", on event hp.
34. Starts timer `check`.
35. Buy "Hinge Mold" (12027) from "Frannie" (NPC 3020) in `qrg`. Base price: 10 copper.
36. Buy "Container Base Mold" (12062) from "Tislan" (NPC 10077) in `freporte`. Base price: 110 copper.
37. Buy "Container Lid Mold" (12069) from "Tislan" (NPC 10077) in `freporte`. Base price: 110 copper.
38. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
    - Dialogue with erudnext/"Lumi Stergnon":
      - Player: "Hail"
        - Condition: `(e.message:findi("hail"))`
      - Player: "New Acolyte Of Peace" (link: conversation sequence)
        - Condition: `(e.message:findi("new acolyte of peace"))`
      - Player: "retrieve the Peacekeeper staffs" (link: conversation sequence)
        - Condition: `(e.message:findi("retrieve the Peacekeeper staffs"))`
        - Gives Sealed Letter (18833).
      - Player: "Battle The Undead" (link: conversation sequence)
        - Condition: `(e.message:findi("battle the undead"))`
        - Gives Box For Bones (17941).
      - Player: "Important Missions" (link: conversation sequence)
        - Condition: `(fac <= 4)`
        - Condition: `(e.message:findi("important missions"))`
      - Player: "Here To Pay Homage" (link: conversation sequence)
        - Condition: `(fac <= 4)`
        - Condition: `(e.message:findi("here to pay homage"))`
39. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `steamfont`.
40. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `tox`.
41. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `toxxulia`.
42. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
43. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). The combine does not fail.
44. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
    - Dialogue with qeynos/"Wolten Grafe":
      - Player: "Hail"
        - NPC say: Hail, noble
        - Condition: `(e.message:findi("hail"))`
      - Player: "Join The Cause" (link: conversation sequence)
        - NPC say: That IS good news! If you walk the righteous path of the Rainkeeper, Karana, then you are truly noble. I have need of someone like that. I must find someone to perform a [dangerous mission] or perhaps you would rather seek out the [Rat King] or [crush the undead].
        - Condition: `(e.message:findi("join the cause"))`
      - Player: "Crush The Undead" (link: explicit mention)
        - NPC say: Those who passed generations ago have had their bones exhumed and enchanted. Some evil force plagues this land with these evil skeletons. You will fight for us and crush the skeletons. Take this box and fill it with the bones of those creatures. We will not allow them to rise again and you shall earn our respect. Go forth and fight for Karana!
        - Condition: `(e.message:findi("crush the undead"))`
        - Gives Box For Bones (17941).
      - Player: "Dangerous Mission" (link: conversation sequence)
        - NPC say: You must go into the catacombs and find a man named Drosco Finlayer. Pass him this note. He has been deep undercover in the Shrine of Bertoxxulous and will have directions to that vile place. To do this will surely show your allegiance to this temple.
        - Condition: `(e.message:findi("dangerous mission"))`
        - Gives Tattered Note (18804).
      - Player: "Rat King" (link: conversation sequence)
        - NPC say: You may try, but no one has truly seen him. I would look in the sewers.
        - Condition: `(e.message:findi("rat king"))`
45. Buy "Small Brick of Steel" (66168) from "Qaelin Hailstorm" (NPC 3042) in `qrg`. Base price: 5,890 copper.
46. qrg/"Qaelin Hailstorm", say "Need A Mark". Gives "Mark of Karana" (66172).
    - Dialogue with qrg/"Qaelin Hailstorm":
      - Player: "Hail"
        - NPC say: Welcome to Surefall Glade. I have the great honor of bestowing these small but powerful Marks of Karana to those who follow him. With it they can use fletching to create bows and arrorws. If you [need a mark] and are a true follower of Karana, I will give you all that you need. There is no fear running out.
        - Condition: `(e.message:findi("hail"))`
      - Player: "Need A Mark" (link: explicit mention)
        - NPC say: Here you go, if you need another please let me know.
          - Reply guard: `(deity == 207)`
        - NPC say: How dare you state that you are something that you aren't! You are no follower of the Rainbringer!
          - Reply guard: ``
        - Condition: `(e.message:findi("need a mark"))`
        - Gives Mark of Karana (66172).
47. Combine in Forge (17): "Hinge Mold" (12027), "Container Base Mold" (12062), "Container Lid Mold" (12069), "Water Flask" (13006), "Small Brick of Steel" (66168), "Mark of Karana" (66172). Hands back "Mark of Karana" (66172). Produces "Surefall Fletching Kit" (66163). Requires Blacksmithing, trivial 163.
48. Loot "Smithy Hammer" (10489) from "Gliblixl Rocktok" in `bazaar`.
49. Forage "Golanda Nut" (62610) in `causeway`.
50. Forage "Golanda Nut" (62610) in `dranik`.
51. Forage "Golanda Nut" (62610) in `draniksscar`.
52. Forage "Golanda Nut" (62610) in `provinggrounds`.
53. Forage "Golanda Nut" (62610) in `riftseekers`.
54. Forage "Golanda Nut" (62610) in `wallofslaughter`.
55. Combine in "Surefall Fletching Kit" (66163): "Smithy Hammer" (10489), "Golanda Nut" (62610). Hands back "Smithy Hammer" (10489). Produces "Fibrous Rope" (62609). Requires Fletching 100. Trivial at 15. The combine does not fail.
56. Combine in "Surefall Fletching Kit" (66163): "Fibrous Rope" (62609). Produces "Eight-loop Lasso" (62648). Requires Fletching 100. Trivial at 15. The combine does not fail.
57. Equip "Eight-loop Lasso" (62648) in primary slot.
58. chardokb/"A Leprous Chokidai", on timer check. Gives "Captured Chokidai" (62645).
59. Combine in "Collapsible Fletching Kit" (17189): "Magical Sample Vial" (62657), "Captured Chokidai" (62645). Produces "Leprous Chokidai Blood Sample" (62614). Requires Fletching. The combine does not fail.
60. droga/"A Bloated Drogan Spider", on event hp.
61. Starts timer `check`.
62. Equip "Eight-loop Lasso" (62648) in primary slot.
63. droga/"A Bloated Drogan Spider", on timer check. Gives "Captured Spider" (62644).
64. Combine in "Collapsible Fletching Kit" (17189): "Magical Sample Vial" (62657), "Captured Spider" (62644). Produces "Bloated Drogan Spider Blood Sample" (62613). Requires Fletching. The combine does not fail.
65. Combine in "Borrowed Medicine Bag" (62605): "Asteatotic Veksar Blood" (35100), "Neuralgic Wyvern Blood" (72605), "Sickly Mosquito Blood Sample" (62611), "Twitching Swordfish Blood Sample" (62612), "Leprous Chokidai Blood Sample" (62614), "Bloated Drogan Spider Blood Sample" (62613). Produces "Full Medicine Bag" (62616). The combine does not fail.
66. qrg/"Corun Finisc", hand "Full Medicine Bag" (62616). Gives "Corun's Notes" (62617).

### "Block of Purest Silver" (62625)

1. Acquisition of "Block of Purest Silver" (62625) is documented under "Heartwood Blade" (62627); obtain another copy if needed.

### "Wind-blessed Heartwood" (62626)

1. Acquisition of "Wind-blessed Heartwood" (62626) is documented under "Heartwood Blade" (62627); obtain another copy if needed.

### "Heated Loadstone" (62628)

1. global/"Global Player", combine recipe 13413. Sets `ranger_epic` to `5`.
2. nedaria/"A Wayfarers Brotherhood Officer", say "Hail". Sets `ranger_epic` to `6`.
3. causeway/"Siflu", say "Adventurers". Requires `ranger_epic` ==6. Gives "Heated Loadstone" (62628).
    - Dialogue with causeway/"Siflu":
      - Player: "Adventurers"
        - NPC say: There have been plenty of those, that's for sure. If you mean recently, then, I suppose I know the group you're talking about. They were hunting us, just as I suspect you are. I was sent to kill anyone that might be on our trail. They gave me a loadstone that I could use to find them again. Here, you take it; I'm getting out of here while I still can.
        - Condition: `(e.message:findi("adventurers") and qglobals["ranger_epic"] == "6")`
        - Gives Heated Loadstone (62628).

### "Elemental Ice Spirit Cage" (62647)

1. Loot "Crooked Cage" (32042) from "a Broken Skull bruiser" in `torgiran`.
2. Acquisition of "Earthcaller" (20488) is documented under "Earthcaller" (20488); obtain another copy if needed.
3. Acquisition of "Swiftwind" (20487) is documented under "Swiftwind" (20487); obtain another copy if needed.
4. Loot "Living Fragment of Fire" (28294) from "A Jopal Mystic" (NPC 217026) in `pofire`. Drop cache: 5.04% chance per kill.
5. Loot "Living Fragment of Water" (28293) from "A Triloun Diviner" in `powater`.
6. Loot "Living Fragment of Water" (28293) from "A Triloun Keeper" in `powater`.
7. Loot "Living Fragment of Water" (28293) from "A Triloun Water Guardian" in `powater`.
8. Acquisition of "Heated Loadstone" (62628) is documented under "Heated Loadstone" (62628); obtain another copy if needed.
9. Spawns "A Mangled Muramite Captain" (300069) in `wallofslaughter` on enter.
10. Loot "Spirit Manacles" (72340) from "A Mangled Muramite Captain".
11. Combine in "Crooked Cage" (32042): "Earthcaller" (20488), "Swiftwind" (20487), "Living Fragment of Fire" (28294), "Living Fragment of Water" (28293), "Heated Loadstone" (62628), "Spirit Manacles" (72340). Hands back "Earthcaller" (20488), "Swiftwind" (20487). Produces "Spirit Cage" (62656). The combine does not fail.
12. global/"Global Player", combine recipe 19914. Sets `ranger_epic` to `8`.
13. Spawns "Craftmaster Tieranu" (334087) in `riftseekers` on enter.
14. Loot "Ring of Warmth" (11427) from "Craftmaster Tieranu".
15. Spawns "Herrian Warfrost" (300057) in `wallofslaughter` on enter.
16. Loot "Hoarfrost Wand" (76999) from "Herrian Warfrost".
17. Combine in "Spirit Cage" (62656): "Ring of Warmth" (11427), "Hoarfrost Wand" (76999). Produces "Elemental Ice Spirit Cage" (62647). The combine does not fail.

### "Senvial's Blessing" (62621)

1. Spawns "An Ancient Thought Horror" (164122) in `thedeep` on enter.
2. Loot "Thick Spinal Fluid" (40420) from "An Ancient Thought Horror".
3. Acquisition of "Corun's Notes" (62617) is documented under "Corun's Notes" (62617); obtain another copy if needed.
4. freeportwest/"Shana Liskia", hand "Corun's Notes" (62617). Gives "Corun's Notes - annotated" (62654).
5. freeportwest/"Shana Liskia", hand "Thick Spinal Fluid" (40420) + "Corun's Notes - annotated" (62654). Gives "Mind Crystal" (62846).
6. eastkarana/"Tholris", say "You Are Diseased". Gives "Red Crystal" (62618).
    - Dialogue with eastkarana/"Tholris":
      - Player: "You Are Diseased"
        - NPC emote: looks at you indignantly
          - Reply guard: `($saydisease==1)`
        - NPC emote: kicks dirt at your feet
          - Reply guard: `($saydisease==2)`
        - NPC emote: shakes his head. Then he catches a glimpse of the Mind Crystal and looks thoughtful for a moment. Then he reaches into his pocket and produces two unusual crystals and hands them to you.
          - Reply guard: `($saydisease==3)`
        - Condition: `(($text=~/you are diseased/i) && plugin::check_hasitem($client, 62846))`
        - Gives Red Crystal (62618).
        - Gives Violet Crystal (62619).
7. eastkarana/"Tholris", say "You Are Diseased". Gives "Violet Crystal" (62619).
8. freeportwest/"Shana Liskia", hand "Red Crystal" (62618) + "Violet Crystal" (62619). Gives "Letter to Corun" (62655).
9. qrg/"Corun Finisc", hand "Letter to Corun" (62655) + "Mind Crystal" (62846). Gives "Red Dogwood Seed" (62844).
10. freeportwest/"Shana Liskia", hand "Corun's Notes" (62617). Sets `ranger_epic` to `2`.
11. natimbi/"Ranger 1 5", say "Hail". Requires `ranger_epic` set. Requires `ranger_epic` ==2. Gives "Senvial's Blessing" (62621).

### "Grinbik's Blessing" (62622)

1. Acquisition of "Red Dogwood Seed" (62844) is documented under "Senvial's Blessing" (62621); obtain another copy if needed.
2. bloodfields/"Ranger 1 5", say "Hail". Requires `ranger_epic` ==2. Gives "Grinbik's Blessing" (62622).

### "Red Dogwood Seed" (62844)

1. Acquisition of "Red Dogwood Seed" (62844) is documented under "Senvial's Blessing" (62621); obtain another copy if needed.

## `ranger_epic`

Values written: 1, 2, 3, 5, 6, 7.

1. eastkarana/"Althele", say "Hail". Sets `ranger_epic` to `1`.
    - Requires `ranger_epic` unset.
    - Dialogue with eastkarana/"Althele":
      - Player: "Hail"
        - NPC say: Hello, friend. Beautiful is what I would call such a day normally, but lately? I sense that something is [
          - Reply guard: `($class eq "Ranger" && (plugin::check_hasitem($client, 20488) || plugin::check_hasitem($client, 62600)))`
        - Condition: `($text=~/hail/i)`
        - Sets `ranger_epic` to `1`.
      - Player: "Your Eyes" (link: conversation sequence)
        - NPC say: Yes. I cannot see any longer, my sight long since lost in the march of years. By the blessings of Tunare and Karana, though, I still make myself useful.
        - Condition: `($text=~/your eyes/i)`
      - Player: "Out Of Balance" (link: conversation sequence)
        - NPC say: I don't know for certain what is wrong. It feels like the start of a cold, a sort of tickling at the back of Norrath's throat, if I may make such a poor metaphor. In much the same way that I can sense that you have wielded the power of nature, probably in the form of the weapons known as Swiftwind and Earthcaller, I can sense a power of illness creeping upon the land. Please, if you come across anything suspicious bring it to me. I am worried, this does not feel like a natural sickness to me. Go with the blessing of the Mother and the speed of the Storm, my child.
          - Reply guard: `($class eq "Ranger" && $client->GetGlobal("ranger_epic") ==1)`
        - NPC say: I am certain that you would sense it too, had you been so blessed as to be without sight. My sense of the life of Norrath is greatly heightened without the hindrance of vision. As I can sense that you have at your call the power of the lands, perhaps in the form of the Nature Walkers Scimitar. I can feel an unnatural illness creeping about the edges of Norrath. Please, if you come across anything suspicious bring it to me. I am worried about this cold sickness that I can almost taste. Go with the blessing of the Mother and the speed of the Storm, my child.
          - Reply guard: `($class eq "Druid" && plugin::check_hasitem($client, 20490) or plugin::check_hasitem($client, 62809))`
        - NPC say: I sense something foreboding, young one, but you should think nothing of it. The sons and daughters of nature will be able to deal with this problem.
          - Reply guard: ``
        - Condition: `($text=~/out of balance/i)`
        - Sets `druid_epic` to `1`.

2. freeportwest/"Shana Liskia", hand "Corun's Notes" (62617). Sets `ranger_epic` to `2`.
    - Hand in x1: "Corun's Notes" (62617).
    - Prerequisite: "Corun's Notes" (62617). See section 0.
    - Gives "Corun's Notes - annotated" (62654).
    - Dialogue with freeportwest/"Shana Liskia":
      - Player: "Hail"
        - NPC say: Hail and well met
        - Condition: `(e.message:findi("hail"))`
      - Player: "Magician" (link: conversation sequence)
        - NPC say: Wonderful! Let me be the first to tell you that your training here will be top notch and you will learn all that is to be known about being an enchanter should you put forth the willingness to learn. I will walk you through your early training and assist you in your hunting and gathering skills. I have created a [
        - Condition: `(e.message:findi("magician") or e.message:findi("enchanter") or e.message:findi("wizard"))`
      - Player: "Enchanter" (link: explicit mention)
        - NPC say: Wonderful! Let me be the first to tell you that your training here will be top notch and you will learn all that is to be known about being an enchanter should you put forth the willingness to learn. I will walk you through your early training and assist you in your hunting and gathering skills. I have created a [
        - Condition: `(e.message:findi("magician") or e.message:findi("enchanter") or e.message:findi("wizard"))`
      - Player: "Wizard" (link: conversation sequence)
        - NPC say: Wonderful! Let me be the first to tell you that your training here will be top notch and you will learn all that is to be known about being an enchanter should you put forth the willingness to learn. I will walk you through your early training and assist you in your hunting and gathering skills. I have created a [
        - Condition: `(e.message:findi("magician") or e.message:findi("enchanter") or e.message:findi("wizard"))`
      - Player: "Diseases Of The Mind" (link: conversation sequence)
        - NPC say: I study the mind. My most recent research deals with, well, I'd rather not discuss that. Unless you need something specific, I don't really have time for long random conversations right now.
        - Condition: `(e.message:findi("diseases of the mind"))`
      - Player: "Special Sewing Kit" (link: conversation sequence)
        - NPC say: This kit that I speak of is one that is able to magically infuse different components into materials used for creating Arcane Scientists Armor. The components that you use will be collected from numerous different areas and shops in Freeport. You will use these materials along with patterns that I will present you with to create your armor. Once you are [ready to begin] I will present you with your Enchanted Sewing Kit.
        - Condition: `(e.other:Class() == "Enchanter" or e.other:Class() == "Magician" or e.other:Class() == "Wizard")`
        - Condition: `(e.message:findi("special sewing kit"))`
      - Player: "Ready To Begin" (link: explicit mention)
        - NPC say: Very well. Here you are
        - Condition: `(e.other:Class() == "Enchanter" or e.other:Class() == "Magician" or e.other:Class() == "Wizard")`
        - Condition: `(e.message:findi("ready to begin"))`
        - Gives Enchanted Sewing Kit (17260).
      - Player: "Sleeve" (link: conversation sequence)
        - NPC say: Sleeves will be a great and necessary addition to your armor. To create your sleeve material you will need to combine 2 Woven Spider Silks, 2 Bone Chips, 1 Spider Legs and Cloth Sleeves in your assembly kit. Once you have created the proper material take it to a loom along with this mold to fashion your very own Arcane Scientists Sleeves.
        - Condition: `(e.other:Class() == "Enchanter" or e.other:Class() == "Magician" or e.other:Class() == "Wizard")`
        - Condition: `(e.message:findi("sleeve"))`
        - Gives Enchanted Sleeves Pattern (22586).
      - Player: "Bracer" (link: conversation sequence)
        - NPC say: A wise choice indeed, having the correct wrist protection is very important in spell channeling. To create your bracer material you will need to combine 1 Woven Spider Silk, 1 Desert Tarantula Chitin, 1 Armadillo Tooth and a Cloth wristband in your assembly kit. Once you have created the proper material take it to a loom along with this mold to fashion your very own Arcane Scientists Bracer.
        - Condition: `(e.other:Class() == "Enchanter" or e.other:Class() == "Magician" or e.other:Class() == "Wizard")`
        - Condition: `(e.message:findi("bracer"))`
        - Gives Enchanted Bracer Pattern (22584).
      - Player: "Cap" (link: conversation sequence)
        - NPC say: A cap will keep you safe from any attackers as well as the elements. To create your cap material you will need to combine 2 Woven Spider Silks, 1 Snake Fang, 1 Chunk of Meat and a Cloth Cap in your assembly kit. Once you have created the proper material take it to a loom along with this mold to fashion your very own Arcane Scientists Cap.
        - Condition: `(e.other:Class() == "Enchanter" or e.other:Class() == "Magician" or e.other:Class() == "Wizard")`
        - Condition: `(e.message:findi("cap"))`
        - Gives Enchanted Cap Pattern (22583).
      - Player: "Glove" (link: conversation sequence)
        - NPC say: Gloves are very important for your early training especially Isola. While you are learning your first set of incantations you should not have to worry about any injuries to your hands. To create your glove material you will need to combine 3 Woven Spider Silks, 1 Giant Scarab Brain, 1 High Quality Cat Pelt 1 Zombie Skin and 1 Large Leaf Scarab Leg in your assembly kit. Once you have created the proper material take it to a loom along with this mold to fashion your very own Arcane Scientists Gloves.
        - Condition: `(e.other:Class() == "Enchanter" or e.other:Class() == "Magician" or e.other:Class() == "Wizard")`
        - Condition: `(e.message:findi("glove"))`
        - Gives Enchanted Gloves Pattern (22588).
      - Player: "Sandal" (link: conversation sequence)
        - NPC say: Sandals will keep you save from any harmful things you may walk in, it is a good idea to have them. To create your sandal material you will need to combine 3 Woven Spider Silks, 1 Coyote Pelt, 2 Black Bear Paws, 1 Urticating Hairs and Cloth Sandals in your assembly kit. Once you have created the proper material take it to a loom along with this mold to fashion your very own Arcane Scientists Sandals.
        - Condition: `(e.other:Class() == "Enchanter" or e.other:Class() == "Magician" or e.other:Class() == "Wizard")`
        - Condition: `(e.message:findi("sandal"))`
        - Gives Enchanted Sandals Pattern (22585).
      - Player: "Trouser" (link: conversation sequence)
        - NPC say: I would always recommend pants to all my new students since they are a very important part of your armor set. To create your trouser material you will need to combine 4 Woven Spider Silks, 1 Embalming Dust, 1 Rotting Zombie Skull and 1 Armadillo Tail in your assembly kit. Once you have created the proper material take it to a loom along with this mold to fashion your very own Arcane Scientists Trousers.
        - Condition: `(e.other:Class() == "Enchanter" or e.other:Class() == "Magician" or e.other:Class() == "Wizard")`
        - Condition: `(e.message:findi("trouser"))`
        - Gives Enchanted Trousers Pattern (22587).
      - Player: "Robe" (link: conversation sequence)
        - NPC say: I am very pleased to see that you have progressed through your armor pieces so quickly. I am also proud to see that you are ready to attempt your robe! To create your robe material you will need to combine 5 Woven Spider Silks, 1 Snake Bile, 1 Cutthroat Golden Tooth, 1 Shadow Wolf Tibia, 1 Orc Prayer Beads and 1 Cloth Shirt in your assembly kit. Once you have created the proper material take it to a loom along with this mold to fashion your very own Arcane Scientists Robe. Be sure to come back to see me for a [final assignment] after you have completed your robe.
        - Condition: `(e.other:Class() == "Enchanter" or e.other:Class() == "Magician" or e.other:Class() == "Wizard")`
        - Condition: `(e.message:findi("robe"))`
        - Gives Enchanted Robe Pattern (22589).
      - Player: "Final Assignment" (link: explicit mention)
        - NPC say: I have a trinket that was given to me by my mother a long time ago. Before she died I told her I would always keep it close to me. Recently, some militia officers came in to our academy and confiscated anything that appeared to be valuable. Fearing for my life I did not fight to keep the necklace my mother gave me. The officer that took it was named Teridsan. If you should find him you have my permission to kill him if that's what it takes to get my necklace back. Return to me when you have my necklace along with 2 Lion Teeth.
        - Condition: `(e.other:Class() == "Enchanter" or e.other:Class() == "Magician" or e.other:Class() == "Wizard")`
        - Condition: `(e.message:findi("final assignment"))`

3. global/"Global Player", combine recipe 13412. Sets `ranger_epic` to `3`.
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

5. global/"Global Player", combine recipe 13413. Sets `ranger_epic` to `5`.
    - `recipe:13413` is combined in Planar Fletching Kit (17762).
      - Buy "Planar Fletching Kit" (17762) from "Ellis Cloudchaser" (NPC 202076) in `poknowledge`. Base price: 1,000 copper.
      - Put in x1: Wind-blessed Heartwood (62626).
        - Prerequisite: "Wind-blessed Heartwood" (62626). See section 0.
      - Put in x1: Block of Purest Silver (62625).
        - Prerequisite: "Block of Purest Silver" (62625). See section 0.
      - Produces Heartwood Blade (62627).
      - Requires Fletching. The combine does not fail.

6. nedaria/"A Wayfarers Brotherhood Officer", say "Hail". Sets `ranger_epic` to `6`.
    - Requires `ranger_epic` ==5.
    - Dialogue with nedaria/"A Wayfarers Brotherhood Officer":
      - Player: "Hail"
        - NPC say: Hello. I can tell that you are a great hunter and tracker. I wanted to pass on to you some information, act on it as you will. A group of adventurers stopped in here a while ago. They said that they had information about a particular member of the Muramite army, some general or something, that had enslaved some elemental spirits. They went looking for him but haven't returned. I would appreciate any information you can find out about them. For now I am going to have to assume that they have all been killed.
        - Condition: `(e.message:findi("hail") and qglobals["ranger_epic"] == "5")`
        - Sets `ranger_epic` to `6`.

7. nedaria/"A Wayfarers Brotherhood Officer", hand "Traveler's Journal" (62629). Sets `ranger_epic` to `7`.
    - Requires `ranger_epic` ==6.
    - Hand in x1: "Traveler's Journal" (62629).
    - Spawns "A Mangled Muramite Captain" (300069) in `wallofslaughter` on enter.
    - Loot "Traveler's Journal" (62629) from "A Mangled Muramite Captain".

### Steps on `ranger_epic` that do not change it

- `bloodfields` marshall trap, on enter needs `ranger_epic` ==2.
  - Sets `ranger_epic_bloodfield` to `1`.
  - Spawns Marshal Histent (301065).
  - Spawns Grinbik the Fertile (301066).
  - Spawns an enslaved earthmover (301067).
  - Spawns an eager student (301068).
- `bloodfields` ranger 1 5, say hail needs `ranger_epic` ==2.
  - Sets `ranger_bloodfield_chest` to `1`.
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
- `bloodfields` ranger 1 5, say hail needs `ranger_epic` ==2.
  - Gives Grinbik's Blessing (62622).
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
- `jaggedpine` red dogwood treant, say hail needs `ranger_epic` ==3.
  - Gives Red Dogwood Heartwood (62623).
  - Gives Spring Dogwood Seed (62624).
- `natimbi` ranger 1 5, say hail needs `ranger_epic` set.
  - Gives Senvial's Blessing (62621).
- `natimbi` ranger 1 5, say hail needs `ranger_epic` set.
  - Sets `ranger_natimbi_chest` to `1`.
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
- `natimbi` trenzar trap, on enter needs `ranger_epic` ==2.
  - Sets `ranger_epic_natimbi` to `1`.
  - Spawns Spiritbinder Trenzar (280084).
  - Spawns a bound earth spirit (280085).
  - Spawns a bound fire spirit (280086).
- `thedeep` player, on enter needs `ranger_epic` ==2.
  - Sets `ranger_epic_deep` to `1`.
  - Spawns ancient thought horror trap (164123).
- `veksar` player, on enter needs `ranger_epic` ==1.
  - Sets `ranger_epic_veks` to `1`.
  - Spawns an asteatotic highborn (109907).
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

1. nedaria/"Targen Stonefall", say "Native Stones". Sets `ranger_epic15_pre` to `1`.
    - Requires `ranger_epic15_pre` unset.
    - Dialogue with nedaria/"Targen Stonefall":
      - Player: "Hail"
        - NPC say: Hello there,
        - Condition: ``
        - Condition: `( qglobals["ranger_epic15_pre"] == nil )`
        - Condition: `(e.message:findi('hail'))`
      - Player: "Interesting Stones" (link: conversation sequence)
        - NPC say: Well, I've been hearing about stones that have inherent power, much like those that we've been calling augmentation stones. These are cruder and you'd have to talk to someone else about exactly how to work with those. I'm more of a geologist myself. I study the way earth and stone are formed. I think there's a lot we can learn about this place from the formation of the [
        - Condition: ``
        - Condition: `( qglobals["ranger_epic15_pre"] == nil )`
        - Condition: `(e.message:findi('interesting stones'))`
      - Player: "Native Stones" (link: conversation sequence)
        - NPC say: Just about any of them, really. I've seen most of what can be found, but if you see anything interesting, please let me look at it. You never know what gems you might find! Best of luck to you, my friend.
        - Condition: ``
        - Condition: `( qglobals["ranger_epic15_pre"] == nil )`
        - Condition: `(e.message:findi('native stones'))`
        - Sets `ranger_epic15_pre` to `1`.
      - Player: "Bloodfields" (link: conversation sequence)
        - NPC say: What? You found this there? Now that is unusual.' Targen pauses a moment to scratch his chin. 'This might bear further investigation. I'll need a sample to compare to this new stone of yours. Maybe you can do me a favor. Gather up a stone from someplace like [
        - Condition: ``
        - Condition: `( qglobals["ranger_epic15_pre"] == "2" and e.message:findi('bloodfields') )`
        - Gives Targen's Emulsion (62639).
        - Gives Sample Cloth (62640).
      - Player: "Odus" (link: conversation sequence)
        - NPC say: It's pretty obvious where all the good stone on that little rock is.
        - Condition: ``
        - Condition: `( qglobals["ranger_epic15_pre"] == "2" and e.message:findi('odus') )`
        - Sets `ranger_epic15_pre` to `3`.
      - Player: "Impurities" (link: conversation sequence)
        - NPC say: A large portion of this stone is infused with material native to this place. I call those impurities because to me the real stone here is the stuff that seems to be from ancient Taelosia. I hope you can find someone with enough earth magic to purify it for you.
        - Condition: ``
        - Condition: `( qglobals["ranger_epic15_pre"] == "5" and e.message:findi('impurities') )`
        - Gives Polished Blasted Stone (62603).
        - Sets `ranger_epic15_pre` to `6`.

2. nedaria/"Targen Stonefall", hand "Blasted Stone" (62601). Sets `ranger_epic15_pre` to `2`.
    - Requires `ranger_epic15_pre` ==1.
    - Hand in x1: "Blasted Stone" (62601).
    - Forage "Blasted Stone" (62601) in `bloodfields`.
    - Gives "Washed Blasted Stone" (62602).

3. nedaria/"Targen Stonefall", say "Odus". Sets `ranger_epic15_pre` to `3`.
    - Requires `ranger_epic15_pre` ==2.

4. hole/"Player", on loot. Sets `ranger_epic15_pre` to `4`.
    - Requires `ranger_epic15_pre` ==3.
    - Requires "Dusty Stone" (62653).
    - Spawns "Stone Collector" (39168) in `hole` on enter.
    - Loot "Dusty Stone" (62653) from "Stone Collector".

5. nedaria/"Targen Stonefall", hand "Closed Sample Cloth" (62641). Sets `ranger_epic15_pre` to `5`.
    - Requires `ranger_epic15_pre` ==4.
    - Hand in x1: "Closed Sample Cloth" (62641).
    - Prerequisite: "Closed Sample Cloth" (62641). See section 0.

6. nedaria/"Targen Stonefall", say "Impurities". Sets `ranger_epic15_pre` to `6`.
    - Requires `ranger_epic15_pre` ==5.
    - Gives "Polished Blasted Stone" (62603).

7. northkarana/"Xanuusus", hand "Polished Blasted Stone" (62603). Sets `ranger_epic15_pre` to `7`.
    - Requires `ranger_epic15_pre` ==6.
    - Hand in x1: "Polished Blasted Stone" (62603).
    - Prerequisite: "Polished Blasted Stone" (62603). See section 0.
    - Gives "Polished Blasted Stone" (62603).
    - Gives "Poem of the Storms" (62632).
    - Dialogue with northkarana/"Xanuusus":
      - Player: "Hail"
        - NPC say: I see you have purified that stone. Can I look at it?
          - Reply guard: `( e.other:HasItem(62604) )`
        - NPC say: You make my limbs ache. There is something unnatural about you. What is it?
          - Reply guard: `( qglobals["ranger_epic15_pre"] == "6" )`
        - NPC say: Greetings, small one! I am Xanuusus of the Stormreapers. You are welcome to rest beneath my mighty branches.
          - Reply guard: ``
        - Condition: `(e.message:findi("hail"))`
        - Gives Polished Blasted Stone (62603).
      - Player: "Help" (link: conversation sequence)
        - NPC say: Well, I suppose I can help you a little, small one. There are three principles expressed in my lovely poem.
        - NPC say: First one must defeat a worthy enemy of the Storm Lord, as you obviously understood from the second stanza. Seek a weapon born by one that would shackle the world if he could. He takes his name from his home, as if to claim it as his own.
        - NPC say: Secondly one must aid a friend of the Storm Lord. There is one that considers himself small and worthless. Heal his heart so that his bare feet may roam again.
        - NPC say: Finally one must perform and act of faith in the Storm Lord. When you have accomplished the other tasks, return to me and we shall again speak of this act of faith.
        - Condition: `( qglobals["ranger_epic15_pre"] == "7" and e.message:findi("help") )`
      - Player: "Ready" (link: conversation sequence)
        - NPC say: Stay close or this won't work. It is better that you do this, for trees are not very well structured to withstand lightning.
          - Reply guard: `( e.other:HasItem(62631) and e.other:HasItem(62633) and e.other:HasItem(62603) )`
          - Reply guard: `( client:GetItemIDAt(Slot.Face) == 62603 and client:GetItemIDAt(Slot.Primary) == 62633 and client:GetItemIDAt(Slot.Secondary) == 62631 )`
        - NPC emote: The treant releases a sound from his hollows that sounds much like thunder.
          - Reply guard: `( e.other:HasItem(62631) and e.other:HasItem(62633) and e.other:HasItem(62603) )`
          - Reply guard: `( client:GetItemIDAt(Slot.Face) == 62603 and client:GetItemIDAt(Slot.Primary) == 62633 and client:GetItemIDAt(Slot.Secondary) == 62631 )`
        - Condition: `( qglobals["ranger_epic15_pre"] == "8" and e.message:findi("ready") )`

8. torgiran/"Player", on loot. Sets `ranger_epic15_pre` to `8`.
    - Requires `ranger_epic15_pre` ==7.
    - Requires "Taskmaster's Cutlass" (62631).
    - Loot "Taskmaster's Cutlass" (62631) from "Taskmaster Waggad Brokenskull" in `torgiran`.

9. northkarana/"Xanuusus", hand "Stone of Winde" (62604). Sets `ranger_epic15_pre` to `9`.
    - Requires `ranger_epic15_pre` ==8.
    - Hand in x1: "Stone of Winde" (62604).
    - Prerequisite: "Stone of Winde" (62604). See section 0.
    - Gives "Stone of Winde" (62604).

10. charasis/"Ghost Of Mera", hand "Sound Capture Jar" (62637). Sets `ranger_epic15_pre` to `10`.
    - Requires `ranger_epic15_pre` ==9.
    - Requires `ranger_epic15_pre` ==10.
    - Hand in x1: "Sound Capture Jar" (62637).
    - Prerequisite: "Sound Capture Jar" (62637). See section 0.
    - Dialogue with charasis/"Ghost Of Mera":
      - Player: "Hail"
        - NPC say: What? Oh, hello. You're . . . you're alive, aren't you. I'm dead, I think. Why can't I leave here? I need to be free so I can continue my [
        - Condition: `(e.other:Class() == "Ranger")`
        - Condition: `( qglobals["ranger_epic15_pre"] == "9" )`
        - Condition: `(e.message:findi("hail"))`
      - Player: "Work" (link: conversation sequence)
        - NPC say: My work . . . I was working with sound, I remember that. I remember hearing all of the wonderful noise that the stones make in the wind. I think I found the perfect sound, but then they killed me. A sacrifice, I think. That makes me sad. I do have one happiness, though. I know the perfect sound. I just wish I could have saved it so that others could hear it. If only they hadn't broken my jars.
        - Condition: `(e.other:Class() == "Ranger")`
        - Condition: `( qglobals["ranger_epic15_pre"] == "9" )`
        - Condition: `(e.message:findi("work"))`

11. erudnint/"Mairee Silentone", hand "Stone of Winde" (62604) + "Echoing Jar" (62638). Sets `ranger_epic15_pre` to `11`.
    - Requires `ranger_epic15_pre` ==10.
    - Hand in x1: "Echoing Jar" (62638).
    - Hand in x1: "Stone of Winde" (62604).
    - Spawns "Ghost of Mera" (105290) in `charasis` on event_enterzone.
    - Hand "Sound Capture Jar" (62637) to charasis/"Ghost Of Mera". Sets `ranger_epic15_pre` to `10`.
    - Loot "Echoing Jar" (62638) from "Ghost of Mera".
    - Prerequisite: "Stone of Winde" (62604). See section 0.
    - Gives "Essence of Earth and Wind" (62600).
    - Dialogue with erudnint/"Mairee Silentone":
      - Player: "Ancient Hammer"
        - NPC say: Yes, the ancient hammer. I heard something about that. Do you mind if I take a look at it?
        - Condition: `(e.message:findi("ancient hammer"))`

### Steps on `ranger_epic15_pre` that do not change it

- `hole` player, on enter needs `ranger_epic15_pre` ==3.
  - Spawns Stone Collector (39168).
  - Loots Dusty Stone (62653).
- `nedaria` targen stonefall, say bloodfields needs `ranger_epic15_pre` ==2.
  - Gives Targen's Emulsion (62639).
  - Gives Sample Cloth (62640).
- `northkarana` xanuusus, say hail needs `ranger_epic15_pre` ==7.
  - Gives Polished Blasted Stone (62603).
- `steamfont` godbin strumharp, hand platinum:30 needs `ranger_epic15_pre` ==9.
  - Gives Sound Capture Jar (62637).
- `steamfontmts` godbin strumharp, hand platinum:30 needs `ranger_epic15_pre` ==9.
  - Gives Sound Capture Jar (62637).

## `ranger_epic` 2.0

Values written: 8, 9.

8. global/"Global Player", combine recipe 19914. Sets `ranger_epic` to `8`.
    - `recipe:19914` is combined in Crooked Cage (32042).
      - Loot "Crooked Cage" (32042) from "a Broken Skull bruiser" in `torgiran`.
      - Put in x1: Earthcaller (20488).
        - Prerequisite: "Earthcaller" (20488). See section 0.
      - Put in x1: Swiftwind (20487).
        - Prerequisite: "Swiftwind" (20487). See section 0.
      - Put in x1: Living Fragment of Fire (28294).
        - Loot "Living Fragment of Fire" (28294) from "A Jopal Mystic" (NPC 217026) in `pofire`. Drop cache: 5.04% chance per kill.
      - Put in x1: Living Fragment of Water (28293).
        - Loot "Living Fragment of Water" (28293) from "A Triloun Diviner" in `powater`.
        - Loot "Living Fragment of Water" (28293) from "A Triloun Keeper" in `powater`.
        - Loot "Living Fragment of Water" (28293) from "A Triloun Water Guardian" in `powater`.
      - Put in x1: Heated Loadstone (62628).
        - Prerequisite: "Heated Loadstone" (62628). See section 0.
      - Put in x1: Spirit Manacles (72340).
        - Spawns "A Mangled Muramite Captain" (300069) in `wallofslaughter` on enter.
        - Loot "Spirit Manacles" (72340) from "A Mangled Muramite Captain".
      - Hands back Earthcaller (20488), Swiftwind (20487).
      - Produces Spirit Cage (62656).
      - The combine does not fail.

Alternative or repeat transition to `ranger_epic` = `8` (not an additional required stage).

8. global/"Global Player", combine recipe 19915. Sets `ranger_epic` to `8`.
    - `recipe:19915` is combined in Crooked Cage (32042).
      - Loot "Crooked Cage" (32042) from "a Broken Skull bruiser" in `torgiran`.
      - Put in x1: Living Fragment of Fire (28294).
        - Loot "Living Fragment of Fire" (28294) from "A Jopal Mystic" (NPC 217026) in `pofire`. Drop cache: 5.04% chance per kill.
      - Put in x1: Living Fragment of Water (28293).
        - Loot "Living Fragment of Water" (28293) from "A Triloun Diviner" in `powater`.
        - Loot "Living Fragment of Water" (28293) from "A Triloun Keeper" in `powater`.
        - Loot "Living Fragment of Water" (28293) from "A Triloun Water Guardian" in `powater`.
      - Put in x1: Heated Loadstone (62628).
        - Prerequisite: "Heated Loadstone" (62628). See section 0.
      - Put in x1: Spirit Manacles (72340).
        - Spawns "A Mangled Muramite Captain" (300069) in `wallofslaughter` on enter.
        - Loot "Spirit Manacles" (72340) from "A Mangled Muramite Captain".
      - Put in x1: Living Fragment of Earth (28295).
        - Spawns "A Vekerchiki Drone" (218047) in `poeartha` on event_combat.
        - Loot "Living Fragment of Earth" (28295) from "A Vekerchiki Drone".
        - Alternative: Loot "Living Fragment of Earth" (28295) from "A Vekerchiki Warrior" (NPC 218025) in `poeartha`; trigger: poeartha/"Vekerchiki Trap", on event_combat.
      - Put in x1: Living Fragment of Air (28292).
        - Loot "Living Fragment of Air" (28292) from "A Temple Guardian".
        - Loot "Living Fragment of Air" (28292) from "A Temple Guardian" in `poair`.
      - Produces Spirit Cage (62656).
      - The combine does not fail.

9. anguish/"Oshimai Spirit Of The High Air", hand "Globe of Discordant Energy" (47100) + "Heartwood Blade" (62627) + "Elemental Ice Spirit Cage" (62647). Sets `ranger_epic` to `9`.
    - Requires `ranger_epic` ==8.
    - Hand in x1: "Elemental Ice Spirit Cage" (62647).
    - Hand in x1: "Globe of Discordant Energy" (47100).
    - Hand in x1: "Heartwood Blade" (62627).
    - Prerequisite: "Elemental Ice Spirit Cage" (62647). See section 0.
    - Say "Check Lorb" to anguish/"Zone Status".
    - Spawns "Orb of Discordant Energy" (317087).
    - Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy".
    - Alternative: Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy" (NPC 317087) in `anguish`; trigger: anguish/"Zone Status", say "Check Uorb".
    - Alternative: Loot "Globe of Discordant Energy" (47100) from "Ornate Chest" (NPC 317112) in `anguish`; trigger: anguish/"Zone Status", say "Check Amv Chest".
    - Alternative: Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy" (NPC 317087) in `anguish`; trigger: anguish/"Zone Status", on event_signal.
    - Alternative: Loot "Globe of Discordant Energy" (47100) from "Overlords Chest" (NPC 317124) in `anguish`; trigger: anguish/"Zone Status", on event_signal.
    - Prerequisite: "Heartwood Blade" (62627). See section 0.
    - Gives "Aurora, the Heartwood Blade" (62649).

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
  - Sets `rng_spawn_wos` to `1`.
  - Spawns Herrian Warfrost (300057).
  - Spawns an excited builder (300058).
  - Loots Gelidran Blood (72073).
  - Loots Hoarfrost Wand (76999).
  - Loots Polished Blue Softstone (80030).
  - Loots Sunshard Powder (35088).
  - Loots Platinum Etched Reinforced Rod (37046).
  - Loots Raw Crimson Nihilite (58067).
- `wallofslaughter` player, on loot needs `ranger_epic` ==8.
  - Sets `rng_wos_chest` to `1`.
  - Spawns a chest (Epic 1.5) (893).

## Other flags touched along the way

- `ranger_epic_bloodfield` set to 1 at bloodfields/marshall trap.
- `ranger_epic_deep` set to 1 at thedeep/player.
- `ranger_epic_dranik` set to 1 at dranik/sverins trap.
- `ranger_epic_natimbi` set to 1 at natimbi/trenzar trap.
- `ranger_epic_veks` set to 1 at veksar/player.
- `ranger_epic_wyv` set to 1 at westwastes/player.
