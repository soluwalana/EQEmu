# Druid — Epic Quest Walkthrough

Generated directly from quest-graph item rewards. Unresolved dependencies are marked, not inferred.

## Epic 1.0

### "Nature Walkers Scimitar" (20490)

1. burningwood/"Telin Darkforest", say "Hail".
    - Player: "hail"
      - NPC emote: looks at you serenely. 'Hello, wanderer.'
      - Condition: `(fac < 4)`
      - Condition: `(e.message:findi("hail"))`
2. timorous/"Dolgin Codslayer", hand "Froglok Essence" (20696). Gives "Froglok Essence" (20696).
    - event_item NPC say: What's this? Egads! It's perfect.  Now all we gotta do is hope he bites.' Dolgin takes a little of the essence and smears it on a piece of bread. He places the bait into the water and watches intently.
      - Event guard: `(plugin::check_handin(\%itemcount,20696=>1))`
3. Spawns "corrupted gorilla" (npc:94140) via `emeraldjungle/tainted gorilla#event_death_complete`.
4. Kill "corrupted gorilla" (NPC 94140) in `emeraldjungle` and loot "Green Tree Bark" (20686).
5. Spawns "corrupted barracuda" (npc:85224) via `lakeofillomen/tainted barracuda#event_death_complete`.
6. Kill "corrupted barracuda" (NPC 85224) in `lakeofillomen` and loot "Pure Lakewater" (20685).
7. Spawns "Faydedar" (npc:96073) after the hand-in.
8. Kill "Faydedar" (NPC 96073) in `timorous` and loot "Pod of Seawater" (20687).
9. overthere/"Nekexin Virulence", hand "Froglok Essence" (20696) + "Green Tree Bark" (20686) + "Pure Lakewater" (20685) + "Pod of Seawater" (20687). Gives "Cleansed Spirit of Kunark" (20699).
    - event_item NPC emote: stares at the swirling bottle of essence. His eyes open wide as he realizes what it is. As its warm bright waves wash over him his skin dissolves into a green goo that coats the ground. From his remains a floating white ball is retrieved.
      - Event guard: `(plugin::check_handin(\%itemcount, 20696 => 1, 20686 => 1, 20685 => 1, 20687 => 1))`
10. Spawns "corrupted seahorse" (npc:64050) via `kedge/tainted seahorse#event_death_complete`.
11. Kill "corrupted seahorse" (NPC 64050) in `kedge` and loot "Kedge Cave Crystals" (20691).
12. Spawns "corrupted seafury cyclops" (npc:69142) via `oceanoftears/tainted seafury cyclops#event_death_complete`.
13. Kill "corrupted seafury cyclops" (NPC 69142) in `oceanoftears` and loot "Ocean of Tears Seavines" (20692).
14. Spawns "corrupted brownie" (npc:57117) via `lfaydark/tainted brownie#event_death_complete`.
15. Kill "corrupted brownie" (NPC 57117) in `lfaydark` and loot "Green Heartwood Branch" (20693).
16. lfaydark/"Pained Unicorn", hand "Kedge Cave Crystals" (20691) + "Ocean of Tears Seavines" (20692) + "Green Heartwood Branch" (20693). Gives "Gleaming Unicorn Horn" (20694).
    - event_trade NPC say: Take my horn, symbol of Faydwer, now cleansed, to the gnome priest. It is anathema to him, to the corrupt forces in his soul, channeled into him by his dark god and will release the grip of corruption on the land. He is close, I can feel it.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 20691,item2 = 20692,item3 = 20693}))`
17. akanon/"Silox Azrix", hand "Gleaming Unicorn Horn" (20694). Gives "Cleansed Spirit of Faydwer" (20697).
    - event_trade NPC emote: looks up at you with a twisted gleam in his eyes. 'Something for me then, eh?' As he looks closer his skin begins to peel and stretch, a bright hot light emanating from his hands gripped around the unicorn horn. 'NOOOO!' The pure cleansing light burns away the gnome without a trace of his existence except for a tiny ball of light which you pick up.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 20694}))`
18. lakerathe/"Triathalon Swim Goggles", say "Hail". Gives "Rebreather" (16889).
    - Player: "hail"
      - NPC say: Welcome, $name!  Good to see that you came out for the event.  here are some swim goggles to help you cross the lake.  Don't forget to hand these to my friend Bike on the far shore so that you can complete the next leg of the race.
      - Condition: `($text=~/hail/i)`
19. lakerathe/"Triathalon Bike", hand "Rebreather" (16889). Gives "Tan Rope Bridle" (21800).
    - event_item NPC say: Excellent, congratulations  on completing the swim.  Here is something that will help you cross South Karana.  Don't forget to give this to my friend on the bridge before crossing into North Karana.
      - Event guard: `(plugin::check_handin(\%itemcount, 16889 => 1))`
20. southkarana/"Triathalon Running Shoes", hand "Tan Rope Bridle" (21800). Gives "Journeyman's Boots" (2300).
    - event_trade NPC say: Perfect!  Here take these and finish the race! Remember to give this to my friend at the end to receive your proof of completing the race!
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 21800}))`
21. northkarana/"Triathalon Token", hand "Journeyman's Boots" (2300). Gives "Warm Pulsing Treant Heart" (20695).
    - event_trade NPC say: Here, take this to Eldarian over there as fast as you can!
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 2300}))`
22. southkarana/"Yeka Ias", hand "Warm Pulsing Treant Heart" (20695). Gives "Cleansed Spirit of Antonica" (20698).
    - event_trade NPC emote: grabs the heart as you toss it to him before realizing what it is. As soon as it touches his hands, his body convulses, a sickly light emanating from his eyes and oozing cracks appear in his skin. As he melts into the ground, a small glowing ball floats where he once stood.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 20695}))`
23. burningwood/"Telin Darkforest", say "Action". Gives "Worn Note" (20472).
    - Player: "action"
      - NPC emote: looks at you consideringly and then scribbles something quickly on a small, worn paper. 'You seem powerful enough. Perhaps you can help those who seek to protect nature's peace. Take this note. Deliver it only into the hands of Faelin Bloodbriar. Where you will find her, I cannot say. She is a friend of mine and a wanderer. She has been seen from one end of the lands to the other. Seek her out, and quickly.'
        - Reply guard: `(e.other:GetLevel() >= 46)`
      - NPC say: You are not yet powerful enough to complete this task. Return when you have gained more experience.
        - Reply guard: ``
      - Condition: `(fac < 4)`
      - Condition: `(e.message:findi("action"))`
      - Linked from "innoruuk" (explicit prompt).
24. gfaydark/"Faelin Bloodbriar", hand "Worn Note" (20472). Gives "Faelin`s Ring" (20446).
    - event_item NPC emote: reads the note carefully and growls to herself. 'Bad news, eh? Take this ring. There is one elf, dark elf even, whom we must go to in order to gather insight into Innoruuk's plans. Giz X'Tin, he goes by most commonly. Kithicor seems to be his favorite haunt and most likely you will find him there. Don't ask how I know him. Just take the ring as my sign to him and he will speak to you. We don't need to speak again, so don't seek me out. Just go to Telin. I must leave to investigate these events.'
      - Event guard: `(plugin::check_handin(\%itemcount, 20472 => 1))`
25. kithicor/"Giz X-Tin", hand "Faelin`s Ring" (20446). Gives "Dark Metal Coin" (20447).
    - event_item NPC emote: flips you a coin after he recognizes the ring. 'It seems we have a mutual 'acquaintance.' The coin repays an old debt. You don't have to worry about what that is. Luckily, Lord Innoruuk has informed me of your coming and your desires. Fortunately, I have all the answers you require right here at the end of my friend's blade. I think I'll be paying my old 'friend' a visit.'
      - Event guard: `(plugin::check_handin(\%itemcount, 20446 => 1))`
26. burningwood/"Telin Darkforest", hand "Dark Metal Coin" (20447). Gives "Worn Dark Metal Coin" (20448).
    - event_trade NPC emote: scratches the coin as he looks at it. 'Faelin sent you to Giz? Surprising. This coin speaks to the outcome of your talk. He would hardly give this bit of metal to a stranger, but that's a story for a different time. So, you say Giz did confirm Innoruuk's involvement, and something about undead minions? Here, take this coin back. Find Arch Druid Althele in the Karanas and show her that. Tell her what we have discussed. She will look kindly on an ally in this matter.'
      - Event guard: `(fac < 4)`
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 20447}))`
27. eastkarana/"Althele", hand "Worn Dark Metal Coin" (20448). Gives "Braided Grass Amulet" (20450).
    - event_item NPC emote: looks at the coin and nods gravely at you as she slips it into a fold of her clothing. 'I see. The story of this coin speaks much to me as do the words you have given me. Telin sent word that you would arrive. The tidings you bring are ill indeed. Here, take this amulet and find Sionae. She is nearby. We will speak more on this matter when all are present.'
      - Event guard: `(plugin::check_handin(\%itemcount, 20448 => 1))`
28. eastkarana/"Sionae", hand "Braided Grass Amulet" (20450). Gives "Frayed Braided Grass Amulet" (20451).
    - event_item NPC say: I see that the time has come. Take the amulet and give it to the third of our kin, Nuien. I will meet you at the gathering.
      - Event guard: `(plugin::check_handin(\%itemcount, 20450 => 1))`
29. eastkarana/"Teloa", hand "Frayed Braided Grass Amulet" (20451).
    - event_item NPC emote: begins walking toward the gathering spot. 'Follow, friend.'
      - Event guard: `(plugin::check_handin(\%itemcount, 20451 => 1))`
30. Spawns "corruptor" (npc:15153) via `eastkarana/althele#timer:attack`.
31. Kill "corruptor" (NPC 15153) in `eastkarana` and loot "Fleshbound Tome" (20452).
32. eastkarana/"Althele", hand "Fleshbound Tome" (20452). Gives "Earth Stained Note" (18959).
    - event_item NPC emote: hands the book to Tholris who reads through it with lines of concern etched on his face, then whispers into her ear. 'Dire news, indeed. This cannot be allowed. I must keep this book but you, $name, must not allow Innoruuk to seed the land with his hatred and filth. You have only just begun your quest. The path you are guided upon will be difficult, if not impossible, but someone must finish it. Please, take this, read of it, follow its instructions. Tunare bless your path and Karana watch over you.
      - Event guard: `(plugin::check_handin(\%itemcount, 20452 => 1))`
33. misty/"Ella Foodcrafter", hand "Earth Stained Note" (18959).
    - event_item NPC say: Hmmm. I've been waiting for someone to bring me this. I'm sorry such a young one as you has taken up this task. Maybe the sky god blesses ya though. Aye, ya have that look in your eye. Our task is to focus the blessings of the gods and cleanse the filth from the land. I have two tasks for ya.
      - Event guard: `(plugin::check_handin(\%itemcount, 18959 => 1))`
34. misty/"Ella Foodcrafter", say "Two Tasks". Gives "Shiny Tin Bowl" (17860).
    - Player: "two tasks"
      - NPC say: Well, ya ask before ya act. That's a good sign. What I need isn't easy to find. First, I need a mixture. Plain sounding enough but it's a special one. Cleanses the mind and focuses the earth's energies into a forest walker's mind. I don't know how to make it. I don't even know what it's called. I merely know it exists and we'll be needing it for our task. When ya do find how to make it ya can mix it in that bowl. Keep it when you're done, it's a good bowl.
      - Condition: `(($text=~/two tasks/i) && (defined $qglobals{shiny_tin_bowl}))`
35. **Unresolved acquisition:** "Ripened Heartfruit" (20464) has no graph or catalog producer.
36. **Unresolved acquisition:** "Sweetened Mudroot" (20465) has no graph or catalog producer.
37. **Unresolved acquisition:** "Speckled Molded Mushroom" (20466) has no graph or catalog producer.
38. **Unresolved acquisition:** "Chilled Tundra Root" (20467) has no graph or catalog producer.
39. Combine in "Shiny Tin Bowl" (17860): "Ripened Heartfruit" (20464), "Sweetened Mudroot" (20465), "Speckled Molded Mushroom" (20466), "Chilled Tundra Root" (20467). Produces "Hardened Mixture" (20473). Requires Pottery.
40. timorous/"Alrik Farsight", say "Take The Artifact". Gives "Crushed Pot" (20457).
    - Player: "take the artifact"
      - NPC say: Hah! Okay, then. Here take this to Farios Elianos in Felwithe. He will give you the receipt.
      - Condition: `($faction < 5)`
      - Condition: `($text=~/take the artifact/i)`
      - Linked from "ancient bowl" (explicit prompt).
41. felwitheb/"Farios Elianos", hand "Crushed Pot" (20457). Gives "Grocery List" (20458).
    - event_trade NPC say: Eh? What is this? A cracked earthen pot? Why in the nine hells would I need a crushed pot? Perhaps I could use it to not hold water! Why did you even bother me with this? Are you mentally deficient? Apparently. Oh, well, you're just a servant boy. Well, then, we'll make you useful, if just a little. Take this shopping list and go get my groceries. Take it to Nora in the tavern. She'll know what I need.
      - Event guard: `(e.other:GetFaction(e.self) < 5)`
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 20457}))`
42. felwithea/"Merchant Nora", hand "Grocery List" (20458). Gives "Bag of Provisions" (20459).
    - event_trade NPC say: You hardly look like the type of errand runner Farios usually sends out to fetch his groceries but here they are. I hope he chokes on them. Oh, and tell him he still owes me five gold for his last order!
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 20458}))`
43. felwitheb/"Farios Elianos", hand "Bag of Provisions" (20459). Gives "Receipt" (20474).
    - event_trade NPC say: Ah, good. Here's a few copper and a receipt for services rendered. Now be off, I'm sure citizens across the land are in dire need of broken pots at right this moment.
      - Event guard: `(e.other:GetFaction(e.self) < 5)`
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 20459}))`
44. timorous/"Alrik Farsight", hand "Receipt" (20474). Gives "Ancient Pattern" (18960).
    - event_item NPC emote: grins happily. 'Excellent! Was he pleased with the artifact? Oh, that's not even worth answering. I'm sure he was. He's always happy with the things I send him. That's why he honored me with this position of esteem, searching for useful and powerful items in this newly discovered land.'
      - Event guard: `($faction < 5)`
      - Event guard: `(plugin::check_handin(\%itemcount, 20474 => 1))`
45. Kill citymist/"A Black Reaver".
46. Spawns "a black reaver" (npc:90004) via `citymist/a black reaver#event_death_complete`.
47. Kill "a black reaver" (NPC 90004) in `citymist` and loot "Jade Reaver" (5664).
48. kaladimb/"Kinlo Strongarm", hand "Jade Reaver" (5664). Gives "Enchanted Clay" (20455).
    - event_item NPC say: Arrrrr. Ooooo. Arrrrrr... Yah, now that's what I be callin' a good lookin' axe. I be crackin' a few skulls with this one. Oh, here's yer block o' mud. Our priests o' Brell use the mud pit fer relievin' themselves after really hard ale blessin' ceremonies, so ya ain't got ta be enchantin' it in holy water or anythin' cause they already have. Har har!
      - Event guard: `($faction <= 5)`
      - Event guard: `(plugin::check_handin(\%itemcount, 5664 => 1))`
49. **Unresolved acquisition:** "Rose of Firiona" (12774) has no graph or catalog producer.
50. qrg/"Merdan Fleetfoot", hand "Rose of Firiona" (12774). Gives "Wood Painting" (20475).
    - event_trade NPC emote: blinks and looks at the flower. 'This is perfect. Thank you! I'm going to go over to her now. Erm, well, maybe I'll wait a week to let the uh.. beauty of the flower.. uhm.. blossom. Yes, that sounds good. Here, you take this painting. I don't need it now. I made it myself, she wouldn't like it anyways.'
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 12774}))`
51. frontiermtns/"A Human Skeleton", hand "Wood Painting" (20475). Gives "Silver Chained Locket" (20476).
    - event_item NPC emote: begins to crack and disintegrate, its body collapsing into a pile of dust that scatters into the winds. On the ground you notice a locket on a fine, thin chain which you pick up.
      - Event guard: `(plugin::check_handin(\%itemcount, 20475 => 1))`
52. qrg/"Niera Farbreeze", hand "Silver Chained Locket" (20476). Gives "Platinum Speckled Powder" (20456).
    - event_trade NPC say: This, this is my mother's amulet. I cannot believe it. Please, take this powder you say you need. Perhaps it does have powers, I don't know, I don't care. Thank you, my eternal thanks for this.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 20476}))`
53. Combine in appropriate tradeskill container: "Ancient Pattern" (18960), "Enchanted Clay" (20455), "Platinum Speckled Powder" (20456). Produces "Runecrested Bowl" (20460). Requires Pottery.
54. misty/"Ella Foodcrafter", hand "Hardened Mixture" (20473) + "Runecrested Bowl" (20460). Gives "Softly Glowing Stone" (20462).
    - event_item NPC emote: smiles slowly as she works the mixture in the bowl and it starts to shine with power. 'This is... a piece of a lost magic item known as Nature's Gem. When restored to completeness I've heard its healing powers will be extraordinary. Take it now. I will take the bowl and hopefully do some good from my end. From here, you can go many ways but I can't guide your path step by step. The only advice I can give you is to look for ones such as yourself.'
      - Event guard: `(plugin::check_handin(\%itemcount, 20473 => 1, 20460 => 1))`
55. Buy "Spell: Resurrection" (15392) from "Henlom Visrek" (NPC 2054) in `qeynos2`. Base price: 18,936 copper.
56. karnor/"Spirit Of Venril Sathir", hand "Spell: Resurrection" (15392).
    - event_item NPC say: I am alive! My thanks to you, $name. And now I will aid you in your quest for preserving the forests of norrath. Your carcass will help nurture the soils of the wilderness.
      - Event guard: `(plugin::check_handin(\%itemcount, 15392 => 1))`
57. Spawns "Venril Sathir" (npc:102126) after the hand-in.
58. Kill "Venril Sathir" (NPC 102126) in `karnor` and loot "Pulsing Green Stone" (20461).
59. firiona/"Foloal Stormforest", hand "Softly Glowing Stone" (20462) + "Pulsing Green Stone" (20461). Gives "Warmly Glowing Stone" (20468).
    - event_item NPC emote: blinks and carefully takes the stones from you, cautiously scratching the jagged green stone against the other. Its skin seems to shiver and flake at the contact and eventually begins to shine brightly. 'With the gem nature's balance is complete. Take the stone and walk your path. Blade or lightning caller, burning sword or the mother's walk.'
      - Event guard: `(plugin::check_handin(\%itemcount, 20462 => 1, 20461 => 1))`
60. misty/"Ella Foodcrafter", hand "Warmly Glowing Stone" (20468). Gives "Elaborate Scimitar" (20440).
    - event_item NPC emote: hands you a scimitar she usually wears at her side. 'Thank you, $name. With this we can hold back the corruption. We have learned something new though. Not only is this work the responsibility of the lord of hatred alone. For some reason we cannot know the lord of disease has decided it worthy of his time to work in conjunction with Innoruuk. The spirits of the three main continents, Faydwer Antonica and Kunark, have been corrupted. Look for the corrupted forces of the land and heal them. When you have found them all then take my scimitar and the spirits to Xanuusus.'
      - Event guard: `(plugin::check_handin(\%itemcount, 20468 => 1))`
61. northkarana/"Xanuusus", hand "Cleansed Spirit of Kunark" (20699) + "Cleansed Spirit of Faydwer" (20697) + "Cleansed Spirit of Antonica" (20698) + "Elaborate Scimitar" (20440). Gives "Nature Walkers Scimitar" (20490).
    - event_trade NPC emote: pushes the spirits into the air, making them dance around the scimitar. With a wave of his hand they melt into the blade and hilt of the weapon. 'With this the spirits of the lands are now free from the corruption of the dark gods.  Through your strength and dedication was this possible, .  May the foul poison that once poured into the earth itself never do so again. Take this weapon that you may continue to watch over the balance of nature. Go now, with the gods' blessings.'
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 20699,item2 = 20697,item3 = 20698,item4 = 20440}))`

**Unresolved graph dependencies:**
- Cycle while acquiring "Froglok Essence" (20696)

## Epic 1.5

### "Staff of Living Brambles" (62863)

1. erudnext/"Lumi Stergnon", say "Hail".
    - Player: "hail"
      - NPC say: Peace and tranquility be with you. .  Are you a [new acolyte of peace] or are you [here to pay homage] to the child of tranquility?
      - Condition: `(e.message:findi("hail"))`
2. Spawns "a cracked earthshaker" (npc:336214) via `dranik/earthshaker trap#enter`.
3. Kill "a cracked earthshaker" (NPC 336214) in `dranik` and loot "Chunk of Energized Clay" (62859).
4. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
    - Player: "battle the undead"
      - NPC say: Then you shall venture to Toxxulia Forest. There has been an increase in skeleton sightings lately. I do not know their origin, but I believe that your efforts will reduce their numbers! Take this box. Return it to me when you have filled it with the bones of these undead creatures and combined it. May Quellious' light guide you.
      - Condition: `(e.message:findi("battle the undead"))`
      - Linked from "new acolyte of peace" (explicit prompt).
5. Loot "Useless Cloth Cap" (13894) from "a kobold scout" (NPC 38035) in `tox`. Drop cache: 20% chance per kill.
6. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
7. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). Requires Remove Traps.
8. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
    - event_trade NPC say: You have done well. Let it be known to all that you fight for the Rainkeeper. Go and continue the battle.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 13882}))`
9. Combine in appropriate tradeskill container: "Water Flask" (13006), "Block of Clay" (16901). Produces "Small Block of Clay" (16900). Requires Pottery.
10. Combine in appropriate tradeskill container: "Small Block of Clay" (16900), "Water Flask" (13006). Produces "Block of Clay" (16901). Requires Pottery.
11. Buy "Aerated Pot Sketch" (62858) from "Elisha Dirtyshoes" (NPC 202134) in `poknowledge`. Base price: 300 copper.
12. Combine in appropriate tradeskill container: "Water Flask" (13006), "Block of Clay" (16901), "Aerated Pot Sketch" (62858). Produces "Aerated Pot Shell" (62860). Requires Pottery.
13. Combine in appropriate tradeskill container: "Chunk of Energized Clay" (62859), "Aerated Pot Shell" (62860). Produces "Reinforced Aerated Pot" (62861). Requires Pottery.
14. Spawns "an ancient thought horror" (npc:164122) via `thedeep/ancient thought horror trap#enter`.
15. Kill "an ancient thought horror" (NPC 164122) in `thedeep` and loot "Thick Spinal Fluid" (40420).
16. **Unresolved acquisition:** "Sickly Maiden's Hair" (62810) has no graph or catalog producer.
17. eastkarana/"Althele", hand "Sickly Maiden's Hair" (62810). Gives "Tuft of Sickly Maiden's Hair" (62811).
    - event_item NPC say: This plant has an illness that I have never sensed before.' Althele pauses in thought for a moment. 'You are a hunter, so I shall put your skills to work. First, take this to Corun in Surefall. He is an expert on animal illnesses. Then put your hunting skills to work and see if you can capture any animals that may have eaten this plant. Corun will want to see them to help him discover what the sickness is.
      - Event guard: `(plugin::check_handin(\%itemcount, 62810 => 1))`
18. qrg/"Corun Finisc", hand "Tuft of Sickly Maiden's Hair" (62811). Gives "Borrowed Medicine Bag" (62605).
    - event_trade NPC say: Well, this is certainly an unpleasant sight. If Althele sent you to me it must be because I've had a lot of experience with sick animals. If you can find me some animals that have become ill by eating this plant perhaps I can discover something about this disease. You must not kill these animals. It is never good to harm an animal if you do not need to. It is also important that the animal be alive when you take samples of their blood. If any animals have eaten this plant and become ill, you need to find a way to capture them and use your fletching kit and these vials to gather blood samples. Althele is rarely wrong about what she senses from Antonica. Be careful with that medicine bag, I borrowed it from a friend in Halas a while back. I'll need you to use it to store some samples as you capture the animals. Don't lose it, you don't want Lars angry with you!
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 62811}))`
19. Spawns "an asteatotic highborn" (npc:109907) via `veksar/player#enter`.
20. Kill "an asteatotic highborn" (NPC 109907) in `veksar` and loot "Asteatotic Veksar Blood" (35100).
21. Spawns "a neuralgic huntress" (npc:120136) via `westwastes/player#enter`.
22. Kill "a neuralgic huntress" (NPC 120136) in `westwastes` and loot "Neuralgic Wyvern Blood" (72605).
23. qrg/"Corun Finisc", hand "Closed Medicine Bag" (62615). Gives "Twitching Swordfish Blood Sample" (62612).
    - event_trade NPC emote: looks over the contents of the medicine bag with a thoughtful expression. 'I wonder if this illness can affect so-called sentient beings. Take this back for now. Go and seek intelligent creatures that may have been affected by this illness. I don't care if you have to kill them, that's fine. Such beings are not of my concern. A couple of samples of their blood should be enough for me to discover something about this disease. I have been hearing from others that the course of this disease is not natural. As your own work corroborates, this illness has spread across species and locations that indicate an unnatural force. Please hurry, even I am beginning to believe that the term plague is appropriate in this situation. I shudder to think how this might affect this sacred glade.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 62615}))`
24. Combine in "Borrowed Medicine Bag" (62605): "Sickly Mosquito Blood Sample" (62611), "Twitching Swordfish Blood Sample" (62612), "Bloated Drogan Spider Blood Sample" (62613), "Leprous Chokidai Blood Sample" (62614). Produces "Closed Medicine Bag" (62615). Requires Remove Traps.
25. Combine in "Borrowed Medicine Bag" (62605): "Asteatotic Veksar Blood" (35100), "Neuralgic Wyvern Blood" (72605), "Sickly Mosquito Blood Sample" (62611), "Twitching Swordfish Blood Sample" (62612), "Leprous Chokidai Blood Sample" (62614), "Bloated Drogan Spider Blood Sample" (62613). Produces "Full Medicine Bag" (62616). Requires Remove Traps.
26. qrg/"Corun Finisc", hand "Full Medicine Bag" (62616). Gives "Corun's Notes" (62617).
    - event_trade NPC say: This is frightening. A disease that can affect mosquito and wyvern must be a truly horrible thing. I will examine these samples carefully and pass knowledge to others who are working to repair this. From what you've shown me I can tell that the disease affects both the mind and the skin. Others seek information about illnesses of the skin. I need you to uncover information about diseases of the mind. I know not where to find such information, but you are a seeker and a worthy ranger. Find someone, somewhere, that knows enough about disease that affects 'more advanced' creatures such as men. Learn about the diseases of the mind. I will seek among the folk of the glade and pine for assistance with a cure for the Maiden's Hair. Please do not give up the search, no matter how difficult. This is a terrible illness and we must stop it from spreading. Take a copy of my notes with you, they may be of use to someone with the right knowledge.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 62616}))`
27. freeportwest/"Shana Liskia", hand "Corun's Notes" (62617). Gives "Corun's Notes - annotated" (62654).
    - event_trade NPC say: Well, this certainly is an interesting puzzle. I see here that these creatures were infected in their spinal columns. I'll tell you that a part of my research involves the use of the fluids of the brain and spine. I suspect that further details might be unpleasant. I might be able to help you, but I'll need materials to work with. Gather fluids from the brain of the creature with the greatest mental power that you can find. I'll test it and see if it's strong enough and has the right properties. If I can duplicate what you saw in these infected creatures, perhaps I can help. Aslo, bring back those notes that Corun made, I'll need them as well.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 62617}))`
    - event_trade NPC emote: makes a few hasty scribbles in the margins of Corun's Notes and hands them back to you.
28. freeportwest/"Shana Liskia", hand "Thick Spinal Fluid" (40420) + "Corun's Notes - annotated" (62654). Gives "Mind Crystal" (62846).
    - event_trade NPC say: Perfect! Yes, this will work nicely. Shana looks through Corun's notes while gathering items from her stores. This should work. What I'm going to do is grow a crystal around this fluid and some of the key ingredients of the disease. The crystal will focus the power of the fluid and the elements of the disease will guide it. If this goes well, I should be able to create a crystal that will guide you to the disease. Shana places the gathered items into a violet-tinted container and casts a spell over them. A moment later she retrieves a crystal from the container. The crystal is clear except for a dark, murky coloration at the center. Take that crystal and see if you can locate any creatures with the disease. If you have any success, please return and let me know.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 40420,item2 = 62654}))`
29. eastkarana/"Tholris", say "You Are Diseased". Gives "Red Crystal" (62618).
    - Player: "you are diseased"
      - NPC emote: looks at you indignantly
        - Reply guard: `($saydisease==1)`
      - NPC emote: kicks dirt at your feet
        - Reply guard: `($saydisease==2)`
      - NPC emote: shakes his head. Then he catches a glimpse of the Mind Crystal and looks thoughtful for a moment. Then he reaches into his pocket and produces two unusual crystals and hands them to you.
        - Reply guard: `($saydisease==3)`
      - Condition: `(($text=~/you are diseased/i) && plugin::check_hasitem($client, 62846))`
30. freeportwest/"Shana Liskia", hand "Red Crystal" (62618) + "Violet Crystal" (62619). Gives "Letter to Corun" (62655).
    - event_trade NPC say: Ah, well, it seems as though the crystal was attuned to these other crystals. They must have come in contact with a rather large element of the disease, otherwise I just can't see how the Mind Crystal would have noticed them. These crystals were created by someone with more experience than I have in this area. I will examine them further and attempt to learn something from them. I can tell now, though, that they were probably created in a fashion similar to the one I used to create the Mind Crystal. Shana pulls out a piece of parchment and writes a note. She gives you the note and says, Take this note to Corun along with the Mind Crystal. He can use the crystal and my notes to seek out the plague in whatever fashion he thinks is best. I need to get to work investigating these new crystals.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 62618,item2 = 62619}))`
31. qrg/"Corun Finisc", hand "Mind Crystal" (62846) + "Letter to Corun" (62655). Gives "Red Dogwood Seed" (62844).
    - event_trade NPC emote: looks at the crystal for a moment; confusion, disgust and curiosity chasing each other across his tired face. After reading the letter, he looks up at you.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 62846,item2 = 62655}))`
    - event_trade NPC say: This crystal seems strange, but if you and this Shana believe that it will help, then I know just the person to put it to work.' Corun puts the note and the crystal into a pouch. He reaches into another pouch to retrieve something small and hands it to you. 'This seed was brought to us by a druid of great skill. It should provide the cure we seek, but we do not know the place or circumstances under which to plant it. We have agreed to leave it to you to find that place and that time. I urge you to hasten, we do not know how long it will be until the plague is released upon us in earnest. The only thing that I know is that there may be a link between those that created the disease and the Plane of Discord. A very tenuous link, but keep the seed with you at all times, you never know when you will need it. May the Mother smile on your effort.
32. qrg/"Niera Farbreeze", hand "Tuft of Sickly Maiden's Hair" (62811). Gives "Waterproof Collection Bag" (62812).
    - event_trade NPC say: Well, this is certainly new to me. It's hard to tell if this is a real concern though. Diseases of all sorts exist in the world and we can't make every one of them a priority. But then perhaps I spend too much time thinking about it. Some great druids and scholars have told me that diseases can start out as helpful things, like parasite fish that clean other fish. But sometimes they change and become harmful because they are trying to clean the wrong kind of things off the fish. They've told me that this is just the way that life tries out new things to see if they work. That might be true, but I don't believe it. Tunare isn't that cruel. And I know at least one god that is.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 62811}))`
    - event_trade NPC say: See if you can find other infected plants or any other evidence of this infection. If you can find enough of them, you may be able to see a pattern. It should spread out from one point. Knowing the first location might help me a lot in trying to discover what this gunk started out as, which parasite fish it is, so-to-speak. Here, take this bag. Put the diseased plants and other evidence you find in here. Make sure to remember where you found them. Keep the bag with you at all times on your search, you never know when you will come across evidence of value. When you think you have enough to see a pattern, seal up the bag and bring it back to me and let me know what you've found.
33. **Unresolved acquisition:** "Bag of Diseased Maiden's Hair" (62826) has no graph or catalog producer.
34. Spawns "a bloodgill forager" (npc:85234) via `lakeofillomen/player#enter`.
35. Kill "a bloodgill forager" (NPC 85234) in `lakeofillomen` and loot "Handful of Diseased Maiden's Hair" (62825).
36. Buy "Tackle Box" (17048) from "Misla McMannus" (NPC 12094) in `qey2hh1`. Base price: 1,000 copper.
37. Spawns "Ulthork Raider" (npc:116608) via `eastwastes/player#enter`.
38. Kill "Ulthork Raider" (NPC 116608) in `eastwastes` and loot "Carved Prexus Totem" (62821).
39. cobaltscar/"Blumblum Swigwater", hand "Carved Prexus Totem" (62821). Gives "Small Trigger Fish" (62820).
    - event_trade NPC say: Wonderful! You are indeed a creature of your word. Not only have you defeated an enemy of the Othmir, but you have returned to us this most precious statue. I thank you. It is unfortunate that the only thing I have to give you in return is some information and a small fish.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 62821}))`
40. Combine in "Tackle Box" (17048): "Small Trigger Fish" (62820). Produces "Gutting Knife" (62823). Requires Fishing.
41. Combine in "Tackle Box" (17048): "Small Trigger Fish" (62820), "Gutting Knife" (62823). Produces "Soggy Maiden's Hair" (62824). Requires Fishing.
42. Spawns "spawn #Swamp Terror" (npc:47208) via `feerrott/druid epic trap#enter`.
43. Kill "spawn #Swamp Terror" (NPC 47208) in `feerrott` and loot "Partially Digested Maiden's Hair" (62819).
44. Combine in "Waterproof Collection Bag" (62812): "Bag of Diseased Maiden's Hair" (62826), "Handful of Diseased Maiden's Hair" (62825), "Soggy Maiden's Hair" (62824), "Partially Digested Maiden's Hair" (62819). Produces "Sealed Collection Bag" (62813). Requires Remove Traps.
45. qrg/"Niera Farbreeze", hand "Sealed Collection Bag" (62813). Gives "Wash Cloth" (62847).
    - event_trade NPC emote: examines the contents of the bag. She also asks you about where you found each item. Your answers bring a puzzled look to her face. 'There does not appear to be any rhyme or reason to the locations where you found these. The stories you tell me indicate that these plants were introduced artificially to the environment. I will pass the samples on to others, they will be very useful, thank you for your help. I am, however, more interested in finding out who did this. Take this and wrap up that disgusting head that you said you found with one of the specimens then give it to me. I want to look at it.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 62813}))`
46. Kill "spawn #Swamp Terror" (NPC 47208) in `feerrott` and loot "Mangled Head" (62818).
47. Combine in "Wash Cloth" (62847): "Mangled Head" (62818). Produces "Wrapped Mangled Head" (62848). Requires Remove Traps.
48. qrg/"Niera Farbreeze", hand "Wrapped Mangled Head" (62848). Gives "Mangled Head" (62827).
    - event_trade NPC emote: examines the head. You say that this might belong to one of those that is involved in all of this? Even if we had seen this person before we'd never be able to recognize it. I don't know how you'll be able to get any information from that, but it's our only clue. See if you can find a way to learn the identity of that head, but first I need you to learn as much as you can about diseases of the skin. Others have come up with some useful information about diseases of the mind and we need your research to put this puzzle together.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 62848}))`
49. poknowledge/"Pathfinder Arelat", say "Worth It". Gives "Fresh Awakenings vol. 1" (62839).
    - Player: "worth it"
      - NPC say: Then here it is. This is a copy of an ancient text that we have preserved and copied for many long years. The author died generations ago. You should read it before you give it to that witch. Good luck to you, friend.
      - Condition: `(qglobals["druid_epic"] == "2" and e.message:findi("worth it"))`
      - Linked from "Corruption of the Night" (explicit prompt).
50. poknowledge/"Gravelady Beddia", hand "Fresh Awakenings vol. 1" (62839) + "Fresh Awakenings vol. 2" (62840) + "Fresh Awakenings vol. 3" (62841). Gives "Healing Plants" (62842).
51. qrg/"Niera Farbreeze", hand "Healing Plants" (62842).
    - event_trade NPC say: That's great! Niera scribbles some notes as she flips through the text. She then hands the notes to you, keeping the book herself. There is some useful information in there. Hold onto these notes until later, you may need them. Give them back to me when you've discovered the identity of that skull.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 62842}))`
52. feerrott/"Corrupted Spirit", say "Show It". Gives "Disease Rune" (62837).
    - Player: "show it"
      - NPC message: The skull of the dead acolyte glows briefly and all of the remaining flesh falls from it. An ephemeral rune appears in your hand. 'Place that where that horrible stone was before, in my very own head with that nasty scroll, and you will be able to engrave it into my skull. My poor skull! Hurry up, though, that rune won't last forever.
      - Condition: `(qglobals["druid_epic"] == "3" and e.message:findi("show it"))`
      - Linked from "What plague?" (explicit prompt).
53. tox/"A Skeleton", say "". Gives "Animating Heads" (62828).
54. Combine in "Mangled Head" (62827): "Disease Rune" (62837), "Animating Heads" (62828). Produces "Runed Skull" (62838). Requires Remove Traps.
55. qrg/"Niera Farbreeze", hand "Runed Skull" (62838) + "Niera's Healing Notes" (62849). Gives "Niera's Research Notes" (62843).
    - event_trade NPC say: That's an amazing story. So there is a coven of Mordavin's followers out there. This is indeed bad news.' She gathers all of the information she has gained so far. She examines the rune on the skull and the text on healing plants. She then pulls out a worn bag and shows you several blood and skin samples from various creatures. All look sickly to you. Niera looks at you and sighs. 'We have a lot of information now, thanks to you and one of our Rangers. We know the nature of the disease and we know the identity of those that created it. Now we need to find the cure. A council of the learned has reviewed all of the information brought to us so far, and this text confirms our suspicions. We need the help of the Unkempt to find a cure. That is your task now. Find the Unkempt and ask them for help. Take these notes, they will explain the details, if you can find someone to give them to.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 62838, item2 = 62849}))`
56. pojustice/"Great Bear", hand "Niera's Research Notes" (62843). Gives "Living Brambles Seed" (62845).
    - event_trade NPC emote: looks at the paper you hand him. 'I can almost understand this writing. This is not a natural disease. I see that you understand the seed rituals, this is good.' The ursine waves his arms in a way that might indicate that he is casting a spell, though it looks little like the sort of spell casting you know. Two seeds appear in his hands. 'Good. I was not sure that I could grow these here. Take them. One is for your cause, one is for you.
      - Event guard: `(qglobals["druid_epic"] == "4" and e.other:GetFaction(e.self) < 5 and item_lib.check_turn_in(e.trade, {item1 = 62843}) )`
57. qrg/"Niera Farbreeze", hand "Red Dogwood Seed" (62844) + "Living Brambles Seed" (62845). Gives "Living Brambles Seed" (62850).
    - event_trade NPC say: Wonderful! These are amazing seeds! I've never seen any just like them before. And you got them from one of the Unkempt. Amazing.' Niera examines the seeds closely while referring to a book called Unkempt Seed Rituals. She wraps both seeds in a soft, moist cloth and hands one of them to you. 'I think I know what the Unkempt meant. This one is for you. Keep it safe. I believe that I know where the other is needed. I have learned much while you were gone and I need to tell you about it.
      - Event guard: `(qglobals["druid_epic"] == "4" and item_lib.check_turn_in(e.trade, {item1 = 62844, item2 = 62845}))`
    - event_trade NPC say: Others have discovered a method for locating the virus. Our brothers and sisters, along with the help of Shana Liskia in Freeport, have grown a crystal from traces of the disease and that crystal can find the disease. They have called it a Mind Crystal, though I'm not sure why. Take it. I need you to put it to work for us. Go out and use it to find the members of that coven and destroy them. I know that we have few clues as to where to look, but you have been wonderfully clever so far and we're relying on you to hunt them down.
58. freportw/"Shana Liskia", hand "Crystal Fragment" (62852). Gives "Crystal Fragment" (62852).
    - event_trade NPC say: Well these certainly are interesting. You say there might be more of them on those necromancers that escaped? Well here, take this. Find all of them and place them into this bag to keep them safe. Then bring them all to me and I'll examine them more closely. I can tell you that they are similiar to the Mind Crystal, but it appears to have different magical properties. I have never seen anything like them and I suspect that they are not from Norrath.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 62852,item2 = 62852,item3 = 62852}))`
59. Spawns "Azibelle Spavin" (npc:335064) via `harbingers/druid epic trap#enter`.
60. Kill "Azibelle Spavin" (NPC 335064) in `harbingers` and loot "Bohab's Crystal Fragment" (62886).
61. Kill "Azibelle Spavin" (NPC 335064) in `harbingers` and loot "Azibelle's Crystal Fragment" (62887).
62. Kill "Glenfire Telzir" (NPC 335065) in `harbingers` and loot "Glenfire's Crystal Fragment" (62888).
63. Combine in "Small Padded Bag" (62853): "Bohab's Crystal Fragment" (62886), "Azibelle's Crystal Fragment" (62887), "Glenfire's Crystal Fragment" (62888), "Crystal Fragment" (62852). Produces "Full Padded Bag" (62854). Requires Remove Traps.
64. freportw/"Shana Liskia", hand "Full Padded Bag" (62854). Gives "Bowl of Foul-smelling Liquid" (62855).
    - event_trade NPC emote: takes the crystal fragments from the pouch. She applies a drop of liquid to it. The liquid turns the crystal white where it spreads.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 62854}))`
    - event_trade NPC say: These small crystals are easier to work with than the Mind Crystal. They also differ from the Mind Crystal in that they are from the Plane of Discord. Take this mixture and find something to enhance its magical power and you just might be able to purify the Mind Crystal. I have no idea what that might be, but I know what it should be. You'll need two components. One will increase the power of the mixture, something with a lot of magical power. It needs to be a liquid or powder to integrate properly. And you'll need a stabilizer, something to help the mixture and the new material to remain stable. This influences the kind of attunement that the crystal takes on during the process. It should be something from nature if you want the result to suit your tastes. You'll have to find someone that knows of something about it among the druids for help on what to use.
65. **Unresolved acquisition:** "Energized Noc Blood" (62889) has no graph or catalog producer.
66. **Unresolved acquisition:** "Emerald Moss" (62856) has no graph or catalog producer.
67. Combine in "Bowl of Foul-smelling Liquid" (62855): "Energized Noc Blood" (62889), "Emerald Moss" (62856), "Mind Crystal" (62846). Produces "Clear Mind Crystal" (62857). Requires Remove Traps.
68. Kill kithicor/"Blackened Treant".
69. Spawns "Blackened Dryad" (npc:20301) via `kithicor/blackened tree limb#event_death_complete`.
70. Kill "Blackened Dryad" (NPC 20301) in `kithicor` and loot "Blackened Earth" (62862).
71. Combine in "Reinforced Aerated Pot" (62861): "Living Brambles Seed" (62850), "Clear Mind Crystal" (62857), "Blackened Earth" (62862). Produces "Staff of Living Brambles" (62863). Requires Remove Traps.

**Unresolved graph dependencies:**
- Cycle while acquiring "Block of Clay" (16901)
- Cycle while acquiring "Sickly Mosquito Blood Sample" (62611)
- Cycle while acquiring "Closed Medicine Bag" (62615)
- Cycle while acquiring "Crystal Fragment" (62852)

## Epic 2.0

### "Staff of Everliving Brambles" (62880)

1. erudnext/"Lumi Stergnon", say "Hail".
    - Player: "hail"
      - NPC say: Peace and tranquility be with you. .  Are you a [new acolyte of peace] or are you [here to pay homage] to the child of tranquility?
      - Condition: `(e.message:findi("hail"))`
2. global/"Global Player", say "Recipe:19908". Gives "Insulated Container" (62876).
3. Spawns "a cracked earthshaker" (npc:336214) via `dranik/earthshaker trap#enter`.
4. Kill "a cracked earthshaker" (NPC 336214) in `dranik` and loot "Chunk of Energized Clay" (62859).
5. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
    - Player: "battle the undead"
      - NPC say: Then you shall venture to Toxxulia Forest. There has been an increase in skeleton sightings lately. I do not know their origin, but I believe that your efforts will reduce their numbers! Take this box. Return it to me when you have filled it with the bones of these undead creatures and combined it. May Quellious' light guide you.
      - Condition: `(e.message:findi("battle the undead"))`
      - Linked from "new acolyte of peace" (explicit prompt).
6. Loot "Useless Cloth Cap" (13894) from "a kobold scout" (NPC 38035) in `tox`. Drop cache: 20% chance per kill.
7. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
8. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). Requires Remove Traps.
9. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
    - event_trade NPC say: You have done well. Let it be known to all that you fight for the Rainkeeper. Go and continue the battle.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 13882}))`
10. Combine in appropriate tradeskill container: "Water Flask" (13006), "Block of Clay" (16901). Produces "Small Block of Clay" (16900). Requires Pottery.
11. Combine in appropriate tradeskill container: "Small Block of Clay" (16900), "Water Flask" (13006). Produces "Block of Clay" (16901). Requires Pottery.
12. Buy "Aerated Pot Sketch" (62858) from "Elisha Dirtyshoes" (NPC 202134) in `poknowledge`. Base price: 300 copper.
13. Combine in appropriate tradeskill container: "Water Flask" (13006), "Block of Clay" (16901), "Aerated Pot Sketch" (62858). Produces "Aerated Pot Shell" (62860). Requires Pottery.
14. Combine in appropriate tradeskill container: "Chunk of Energized Clay" (62859), "Aerated Pot Shell" (62860). Produces "Reinforced Aerated Pot" (62861). Requires Pottery.
15. Spawns "an ancient thought horror" (npc:164122) via `thedeep/ancient thought horror trap#enter`.
16. Kill "an ancient thought horror" (NPC 164122) in `thedeep` and loot "Thick Spinal Fluid" (40420).
17. **Unresolved acquisition:** "Sickly Maiden's Hair" (62810) has no graph or catalog producer.
18. eastkarana/"Althele", hand "Sickly Maiden's Hair" (62810). Gives "Tuft of Sickly Maiden's Hair" (62811).
    - event_item NPC say: This plant has an illness that I have never sensed before.' Althele pauses in thought for a moment. 'You are a hunter, so I shall put your skills to work. First, take this to Corun in Surefall. He is an expert on animal illnesses. Then put your hunting skills to work and see if you can capture any animals that may have eaten this plant. Corun will want to see them to help him discover what the sickness is.
      - Event guard: `(plugin::check_handin(\%itemcount, 62810 => 1))`
19. qrg/"Corun Finisc", hand "Tuft of Sickly Maiden's Hair" (62811). Gives "Borrowed Medicine Bag" (62605).
    - event_trade NPC say: Well, this is certainly an unpleasant sight. If Althele sent you to me it must be because I've had a lot of experience with sick animals. If you can find me some animals that have become ill by eating this plant perhaps I can discover something about this disease. You must not kill these animals. It is never good to harm an animal if you do not need to. It is also important that the animal be alive when you take samples of their blood. If any animals have eaten this plant and become ill, you need to find a way to capture them and use your fletching kit and these vials to gather blood samples. Althele is rarely wrong about what she senses from Antonica. Be careful with that medicine bag, I borrowed it from a friend in Halas a while back. I'll need you to use it to store some samples as you capture the animals. Don't lose it, you don't want Lars angry with you!
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 62811}))`
20. Spawns "an asteatotic highborn" (npc:109907) via `veksar/player#enter`.
21. Kill "an asteatotic highborn" (NPC 109907) in `veksar` and loot "Asteatotic Veksar Blood" (35100).
22. Spawns "a neuralgic huntress" (npc:120136) via `westwastes/player#enter`.
23. Kill "a neuralgic huntress" (NPC 120136) in `westwastes` and loot "Neuralgic Wyvern Blood" (72605).
24. qrg/"Corun Finisc", hand "Closed Medicine Bag" (62615). Gives "Twitching Swordfish Blood Sample" (62612).
    - event_trade NPC emote: looks over the contents of the medicine bag with a thoughtful expression. 'I wonder if this illness can affect so-called sentient beings. Take this back for now. Go and seek intelligent creatures that may have been affected by this illness. I don't care if you have to kill them, that's fine. Such beings are not of my concern. A couple of samples of their blood should be enough for me to discover something about this disease. I have been hearing from others that the course of this disease is not natural. As your own work corroborates, this illness has spread across species and locations that indicate an unnatural force. Please hurry, even I am beginning to believe that the term plague is appropriate in this situation. I shudder to think how this might affect this sacred glade.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 62615}))`
25. Combine in "Borrowed Medicine Bag" (62605): "Sickly Mosquito Blood Sample" (62611), "Twitching Swordfish Blood Sample" (62612), "Bloated Drogan Spider Blood Sample" (62613), "Leprous Chokidai Blood Sample" (62614). Produces "Closed Medicine Bag" (62615). Requires Remove Traps.
26. Combine in "Borrowed Medicine Bag" (62605): "Asteatotic Veksar Blood" (35100), "Neuralgic Wyvern Blood" (72605), "Sickly Mosquito Blood Sample" (62611), "Twitching Swordfish Blood Sample" (62612), "Leprous Chokidai Blood Sample" (62614), "Bloated Drogan Spider Blood Sample" (62613). Produces "Full Medicine Bag" (62616). Requires Remove Traps.
27. qrg/"Corun Finisc", hand "Full Medicine Bag" (62616). Gives "Corun's Notes" (62617).
    - event_trade NPC say: This is frightening. A disease that can affect mosquito and wyvern must be a truly horrible thing. I will examine these samples carefully and pass knowledge to others who are working to repair this. From what you've shown me I can tell that the disease affects both the mind and the skin. Others seek information about illnesses of the skin. I need you to uncover information about diseases of the mind. I know not where to find such information, but you are a seeker and a worthy ranger. Find someone, somewhere, that knows enough about disease that affects 'more advanced' creatures such as men. Learn about the diseases of the mind. I will seek among the folk of the glade and pine for assistance with a cure for the Maiden's Hair. Please do not give up the search, no matter how difficult. This is a terrible illness and we must stop it from spreading. Take a copy of my notes with you, they may be of use to someone with the right knowledge.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 62616}))`
28. freeportwest/"Shana Liskia", hand "Corun's Notes" (62617). Gives "Corun's Notes - annotated" (62654).
    - event_trade NPC say: Well, this certainly is an interesting puzzle. I see here that these creatures were infected in their spinal columns. I'll tell you that a part of my research involves the use of the fluids of the brain and spine. I suspect that further details might be unpleasant. I might be able to help you, but I'll need materials to work with. Gather fluids from the brain of the creature with the greatest mental power that you can find. I'll test it and see if it's strong enough and has the right properties. If I can duplicate what you saw in these infected creatures, perhaps I can help. Aslo, bring back those notes that Corun made, I'll need them as well.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 62617}))`
    - event_trade NPC emote: makes a few hasty scribbles in the margins of Corun's Notes and hands them back to you.
29. freeportwest/"Shana Liskia", hand "Thick Spinal Fluid" (40420) + "Corun's Notes - annotated" (62654). Gives "Mind Crystal" (62846).
    - event_trade NPC say: Perfect! Yes, this will work nicely. Shana looks through Corun's notes while gathering items from her stores. This should work. What I'm going to do is grow a crystal around this fluid and some of the key ingredients of the disease. The crystal will focus the power of the fluid and the elements of the disease will guide it. If this goes well, I should be able to create a crystal that will guide you to the disease. Shana places the gathered items into a violet-tinted container and casts a spell over them. A moment later she retrieves a crystal from the container. The crystal is clear except for a dark, murky coloration at the center. Take that crystal and see if you can locate any creatures with the disease. If you have any success, please return and let me know.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 40420,item2 = 62654}))`
30. eastkarana/"Tholris", say "You Are Diseased". Gives "Red Crystal" (62618).
    - Player: "you are diseased"
      - NPC emote: looks at you indignantly
        - Reply guard: `($saydisease==1)`
      - NPC emote: kicks dirt at your feet
        - Reply guard: `($saydisease==2)`
      - NPC emote: shakes his head. Then he catches a glimpse of the Mind Crystal and looks thoughtful for a moment. Then he reaches into his pocket and produces two unusual crystals and hands them to you.
        - Reply guard: `($saydisease==3)`
      - Condition: `(($text=~/you are diseased/i) && plugin::check_hasitem($client, 62846))`
31. freeportwest/"Shana Liskia", hand "Red Crystal" (62618) + "Violet Crystal" (62619). Gives "Letter to Corun" (62655).
    - event_trade NPC say: Ah, well, it seems as though the crystal was attuned to these other crystals. They must have come in contact with a rather large element of the disease, otherwise I just can't see how the Mind Crystal would have noticed them. These crystals were created by someone with more experience than I have in this area. I will examine them further and attempt to learn something from them. I can tell now, though, that they were probably created in a fashion similar to the one I used to create the Mind Crystal. Shana pulls out a piece of parchment and writes a note. She gives you the note and says, Take this note to Corun along with the Mind Crystal. He can use the crystal and my notes to seek out the plague in whatever fashion he thinks is best. I need to get to work investigating these new crystals.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 62618,item2 = 62619}))`
32. qrg/"Corun Finisc", hand "Mind Crystal" (62846) + "Letter to Corun" (62655). Gives "Red Dogwood Seed" (62844).
    - event_trade NPC emote: looks at the crystal for a moment; confusion, disgust and curiosity chasing each other across his tired face. After reading the letter, he looks up at you.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 62846,item2 = 62655}))`
    - event_trade NPC say: This crystal seems strange, but if you and this Shana believe that it will help, then I know just the person to put it to work.' Corun puts the note and the crystal into a pouch. He reaches into another pouch to retrieve something small and hands it to you. 'This seed was brought to us by a druid of great skill. It should provide the cure we seek, but we do not know the place or circumstances under which to plant it. We have agreed to leave it to you to find that place and that time. I urge you to hasten, we do not know how long it will be until the plague is released upon us in earnest. The only thing that I know is that there may be a link between those that created the disease and the Plane of Discord. A very tenuous link, but keep the seed with you at all times, you never know when you will need it. May the Mother smile on your effort.
33. qrg/"Niera Farbreeze", hand "Tuft of Sickly Maiden's Hair" (62811). Gives "Waterproof Collection Bag" (62812).
    - event_trade NPC say: Well, this is certainly new to me. It's hard to tell if this is a real concern though. Diseases of all sorts exist in the world and we can't make every one of them a priority. But then perhaps I spend too much time thinking about it. Some great druids and scholars have told me that diseases can start out as helpful things, like parasite fish that clean other fish. But sometimes they change and become harmful because they are trying to clean the wrong kind of things off the fish. They've told me that this is just the way that life tries out new things to see if they work. That might be true, but I don't believe it. Tunare isn't that cruel. And I know at least one god that is.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 62811}))`
    - event_trade NPC say: See if you can find other infected plants or any other evidence of this infection. If you can find enough of them, you may be able to see a pattern. It should spread out from one point. Knowing the first location might help me a lot in trying to discover what this gunk started out as, which parasite fish it is, so-to-speak. Here, take this bag. Put the diseased plants and other evidence you find in here. Make sure to remember where you found them. Keep the bag with you at all times on your search, you never know when you will come across evidence of value. When you think you have enough to see a pattern, seal up the bag and bring it back to me and let me know what you've found.
34. **Unresolved acquisition:** "Bag of Diseased Maiden's Hair" (62826) has no graph or catalog producer.
35. Spawns "a bloodgill forager" (npc:85234) via `lakeofillomen/player#enter`.
36. Kill "a bloodgill forager" (NPC 85234) in `lakeofillomen` and loot "Handful of Diseased Maiden's Hair" (62825).
37. Buy "Tackle Box" (17048) from "Misla McMannus" (NPC 12094) in `qey2hh1`. Base price: 1,000 copper.
38. Spawns "Ulthork Raider" (npc:116608) via `eastwastes/player#enter`.
39. Kill "Ulthork Raider" (NPC 116608) in `eastwastes` and loot "Carved Prexus Totem" (62821).
40. cobaltscar/"Blumblum Swigwater", hand "Carved Prexus Totem" (62821). Gives "Small Trigger Fish" (62820).
    - event_trade NPC say: Wonderful! You are indeed a creature of your word. Not only have you defeated an enemy of the Othmir, but you have returned to us this most precious statue. I thank you. It is unfortunate that the only thing I have to give you in return is some information and a small fish.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 62821}))`
41. Combine in "Tackle Box" (17048): "Small Trigger Fish" (62820). Produces "Gutting Knife" (62823). Requires Fishing.
42. Combine in "Tackle Box" (17048): "Small Trigger Fish" (62820), "Gutting Knife" (62823). Produces "Soggy Maiden's Hair" (62824). Requires Fishing.
43. Spawns "spawn #Swamp Terror" (npc:47208) via `feerrott/druid epic trap#enter`.
44. Kill "spawn #Swamp Terror" (NPC 47208) in `feerrott` and loot "Partially Digested Maiden's Hair" (62819).
45. Combine in "Waterproof Collection Bag" (62812): "Bag of Diseased Maiden's Hair" (62826), "Handful of Diseased Maiden's Hair" (62825), "Soggy Maiden's Hair" (62824), "Partially Digested Maiden's Hair" (62819). Produces "Sealed Collection Bag" (62813). Requires Remove Traps.
46. qrg/"Niera Farbreeze", hand "Sealed Collection Bag" (62813). Gives "Wash Cloth" (62847).
    - event_trade NPC emote: examines the contents of the bag. She also asks you about where you found each item. Your answers bring a puzzled look to her face. 'There does not appear to be any rhyme or reason to the locations where you found these. The stories you tell me indicate that these plants were introduced artificially to the environment. I will pass the samples on to others, they will be very useful, thank you for your help. I am, however, more interested in finding out who did this. Take this and wrap up that disgusting head that you said you found with one of the specimens then give it to me. I want to look at it.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 62813}))`
47. Kill "spawn #Swamp Terror" (NPC 47208) in `feerrott` and loot "Mangled Head" (62818).
48. Combine in "Wash Cloth" (62847): "Mangled Head" (62818). Produces "Wrapped Mangled Head" (62848). Requires Remove Traps.
49. qrg/"Niera Farbreeze", hand "Wrapped Mangled Head" (62848). Gives "Mangled Head" (62827).
    - event_trade NPC emote: examines the head. You say that this might belong to one of those that is involved in all of this? Even if we had seen this person before we'd never be able to recognize it. I don't know how you'll be able to get any information from that, but it's our only clue. See if you can find a way to learn the identity of that head, but first I need you to learn as much as you can about diseases of the skin. Others have come up with some useful information about diseases of the mind and we need your research to put this puzzle together.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 62848}))`
50. poknowledge/"Pathfinder Arelat", say "Worth It". Gives "Fresh Awakenings vol. 1" (62839).
    - Player: "worth it"
      - NPC say: Then here it is. This is a copy of an ancient text that we have preserved and copied for many long years. The author died generations ago. You should read it before you give it to that witch. Good luck to you, friend.
      - Condition: `(qglobals["druid_epic"] == "2" and e.message:findi("worth it"))`
      - Linked from "Corruption of the Night" (explicit prompt).
51. poknowledge/"Gravelady Beddia", hand "Fresh Awakenings vol. 1" (62839) + "Fresh Awakenings vol. 2" (62840) + "Fresh Awakenings vol. 3" (62841). Gives "Healing Plants" (62842).
52. qrg/"Niera Farbreeze", hand "Healing Plants" (62842).
    - event_trade NPC say: That's great! Niera scribbles some notes as she flips through the text. She then hands the notes to you, keeping the book herself. There is some useful information in there. Hold onto these notes until later, you may need them. Give them back to me when you've discovered the identity of that skull.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 62842}))`
53. feerrott/"Corrupted Spirit", say "Show It". Gives "Disease Rune" (62837).
    - Player: "show it"
      - NPC message: The skull of the dead acolyte glows briefly and all of the remaining flesh falls from it. An ephemeral rune appears in your hand. 'Place that where that horrible stone was before, in my very own head with that nasty scroll, and you will be able to engrave it into my skull. My poor skull! Hurry up, though, that rune won't last forever.
      - Condition: `(qglobals["druid_epic"] == "3" and e.message:findi("show it"))`
      - Linked from "What plague?" (explicit prompt).
54. tox/"A Skeleton", say "". Gives "Animating Heads" (62828).
55. Combine in "Mangled Head" (62827): "Disease Rune" (62837), "Animating Heads" (62828). Produces "Runed Skull" (62838). Requires Remove Traps.
56. qrg/"Niera Farbreeze", hand "Runed Skull" (62838) + "Niera's Healing Notes" (62849). Gives "Niera's Research Notes" (62843).
    - event_trade NPC say: That's an amazing story. So there is a coven of Mordavin's followers out there. This is indeed bad news.' She gathers all of the information she has gained so far. She examines the rune on the skull and the text on healing plants. She then pulls out a worn bag and shows you several blood and skin samples from various creatures. All look sickly to you. Niera looks at you and sighs. 'We have a lot of information now, thanks to you and one of our Rangers. We know the nature of the disease and we know the identity of those that created it. Now we need to find the cure. A council of the learned has reviewed all of the information brought to us so far, and this text confirms our suspicions. We need the help of the Unkempt to find a cure. That is your task now. Find the Unkempt and ask them for help. Take these notes, they will explain the details, if you can find someone to give them to.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 62838, item2 = 62849}))`
57. pojustice/"Great Bear", hand "Niera's Research Notes" (62843). Gives "Living Brambles Seed" (62845).
    - event_trade NPC emote: looks at the paper you hand him. 'I can almost understand this writing. This is not a natural disease. I see that you understand the seed rituals, this is good.' The ursine waves his arms in a way that might indicate that he is casting a spell, though it looks little like the sort of spell casting you know. Two seeds appear in his hands. 'Good. I was not sure that I could grow these here. Take them. One is for your cause, one is for you.
      - Event guard: `(qglobals["druid_epic"] == "4" and e.other:GetFaction(e.self) < 5 and item_lib.check_turn_in(e.trade, {item1 = 62843}) )`
58. qrg/"Niera Farbreeze", hand "Red Dogwood Seed" (62844) + "Living Brambles Seed" (62845). Gives "Living Brambles Seed" (62850).
    - event_trade NPC say: Wonderful! These are amazing seeds! I've never seen any just like them before. And you got them from one of the Unkempt. Amazing.' Niera examines the seeds closely while referring to a book called Unkempt Seed Rituals. She wraps both seeds in a soft, moist cloth and hands one of them to you. 'I think I know what the Unkempt meant. This one is for you. Keep it safe. I believe that I know where the other is needed. I have learned much while you were gone and I need to tell you about it.
      - Event guard: `(qglobals["druid_epic"] == "4" and item_lib.check_turn_in(e.trade, {item1 = 62844, item2 = 62845}))`
    - event_trade NPC say: Others have discovered a method for locating the virus. Our brothers and sisters, along with the help of Shana Liskia in Freeport, have grown a crystal from traces of the disease and that crystal can find the disease. They have called it a Mind Crystal, though I'm not sure why. Take it. I need you to put it to work for us. Go out and use it to find the members of that coven and destroy them. I know that we have few clues as to where to look, but you have been wonderfully clever so far and we're relying on you to hunt them down.
59. freportw/"Shana Liskia", hand "Crystal Fragment" (62852). Gives "Crystal Fragment" (62852).
    - event_trade NPC say: Well these certainly are interesting. You say there might be more of them on those necromancers that escaped? Well here, take this. Find all of them and place them into this bag to keep them safe. Then bring them all to me and I'll examine them more closely. I can tell you that they are similiar to the Mind Crystal, but it appears to have different magical properties. I have never seen anything like them and I suspect that they are not from Norrath.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 62852,item2 = 62852,item3 = 62852}))`
60. Spawns "Azibelle Spavin" (npc:335064) via `harbingers/druid epic trap#enter`.
61. Kill "Azibelle Spavin" (NPC 335064) in `harbingers` and loot "Bohab's Crystal Fragment" (62886).
62. Kill "Azibelle Spavin" (NPC 335064) in `harbingers` and loot "Azibelle's Crystal Fragment" (62887).
63. Kill "Glenfire Telzir" (NPC 335065) in `harbingers` and loot "Glenfire's Crystal Fragment" (62888).
64. Combine in "Small Padded Bag" (62853): "Bohab's Crystal Fragment" (62886), "Azibelle's Crystal Fragment" (62887), "Glenfire's Crystal Fragment" (62888), "Crystal Fragment" (62852). Produces "Full Padded Bag" (62854). Requires Remove Traps.
65. freportw/"Shana Liskia", hand "Full Padded Bag" (62854). Gives "Bowl of Foul-smelling Liquid" (62855).
    - event_trade NPC emote: takes the crystal fragments from the pouch. She applies a drop of liquid to it. The liquid turns the crystal white where it spreads.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 62854}))`
    - event_trade NPC say: These small crystals are easier to work with than the Mind Crystal. They also differ from the Mind Crystal in that they are from the Plane of Discord. Take this mixture and find something to enhance its magical power and you just might be able to purify the Mind Crystal. I have no idea what that might be, but I know what it should be. You'll need two components. One will increase the power of the mixture, something with a lot of magical power. It needs to be a liquid or powder to integrate properly. And you'll need a stabilizer, something to help the mixture and the new material to remain stable. This influences the kind of attunement that the crystal takes on during the process. It should be something from nature if you want the result to suit your tastes. You'll have to find someone that knows of something about it among the druids for help on what to use.
66. **Unresolved acquisition:** "Energized Noc Blood" (62889) has no graph or catalog producer.
67. **Unresolved acquisition:** "Emerald Moss" (62856) has no graph or catalog producer.
68. Combine in "Bowl of Foul-smelling Liquid" (62855): "Energized Noc Blood" (62889), "Emerald Moss" (62856), "Mind Crystal" (62846). Produces "Clear Mind Crystal" (62857). Requires Remove Traps.
69. Kill kithicor/"Blackened Treant".
70. Spawns "Blackened Dryad" (npc:20301) via `kithicor/blackened tree limb#event_death_complete`.
71. Kill "Blackened Dryad" (NPC 20301) in `kithicor` and loot "Blackened Earth" (62862).
72. Combine in "Reinforced Aerated Pot" (62861): "Living Brambles Seed" (62850), "Clear Mind Crystal" (62857), "Blackened Earth" (62862). Produces "Staff of Living Brambles" (62863). Requires Remove Traps.
73. Combine in "Insulated Container" (62876): "Essence of Rainfall" (62883), "Staff of Living Brambles" (62863). Produces "Staff of Everliving Brambles" (62880). Requires Remove Traps.

**Unresolved graph dependencies:**
- Cycle while acquiring "Block of Clay" (16901)
- Cycle while acquiring "Sickly Mosquito Blood Sample" (62611)
- Cycle while acquiring "Closed Medicine Bag" (62615)
- Cycle while acquiring "Crystal Fragment" (62852)
