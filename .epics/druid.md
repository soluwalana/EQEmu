# Druid — Epic Quest Walkthrough

Generated directly from quest-graph item rewards. Unresolved dependencies are marked, not inferred.

## Epic 1.0

### "Nature Walkers Scimitar" (20490)

<a id="epic-item-20490"></a>

1. burningwood/"Telin Darkforest", say "Hail".
    - Player: "hail"
      - NPC emote: looks at you serenely. 'Hello, wanderer.'
      - Condition: `(fac < 4)`
      - Condition: `(e.message:findi("hail"))`
2. Loot "Froglok Essence" (20696) from "Ulump Pujluk" (NPC 83030) in `swampofnohope`. Drop cache: 100% chance per kill.
3. Spawns "corrupted gorilla" (npc:94140) via `emeraldjungle/tainted gorilla#event_death_complete`.
4. Kill "corrupted gorilla" (NPC 94140) in `emeraldjungle` and loot "Green Tree Bark" (20686).
5. Spawns "corrupted barracuda" (npc:85224) via `lakeofillomen/tainted barracuda#event_death_complete`.
6. Kill "corrupted barracuda" (NPC 85224) in `lakeofillomen` and loot "Pure Lakewater" (20685).
7. timorous/"Dolgin Codslayer", hand "Froglok Essence" (20696).
    - event_item NPC say: What's this? Egads! It's perfect.  Now all we gotta do is hope he bites.' Dolgin takes a little of the essence and smears it on a piece of bread. He places the bait into the water and watches intently.
      - Event guard: `(plugin::check_handin(\%itemcount,20696=>1))`
8. Spawns "Faydedar" (npc:96073) after the hand-in.
9. Kill "Faydedar" (NPC 96073) in `timorous` and loot "Pod of Seawater" (20687).
10. overthere/"Nekexin Virulence", hand "Froglok Essence" (20696) + "Green Tree Bark" (20686) + "Pure Lakewater" (20685) + "Pod of Seawater" (20687). Gives "Cleansed Spirit of Kunark" (20699).
    - event_item NPC emote: stares at the swirling bottle of essence. His eyes open wide as he realizes what it is. As its warm bright waves wash over him his skin dissolves into a green goo that coats the ground. From his remains a floating white ball is retrieved.
      - Event guard: `(plugin::check_handin(\%itemcount, 20696 => 1, 20686 => 1, 20685 => 1, 20687 => 1))`
11. Spawns "corrupted seahorse" (npc:64050) via `kedge/tainted seahorse#event_death_complete`.
12. Kill "corrupted seahorse" (NPC 64050) in `kedge` and loot "Kedge Cave Crystals" (20691).
13. Spawns "corrupted seafury cyclops" (npc:69142) via `oceanoftears/tainted seafury cyclops#event_death_complete`.
14. Kill "corrupted seafury cyclops" (NPC 69142) in `oceanoftears` and loot "Ocean of Tears Seavines" (20692).
15. Spawns "corrupted brownie" (npc:57117) via `lfaydark/tainted brownie#event_death_complete`.
16. Kill "corrupted brownie" (NPC 57117) in `lfaydark` and loot "Green Heartwood Branch" (20693).
17. lfaydark/"Pained Unicorn", hand "Kedge Cave Crystals" (20691) + "Ocean of Tears Seavines" (20692) + "Green Heartwood Branch" (20693). Gives "Gleaming Unicorn Horn" (20694).
    - event_trade NPC say: Take my horn, symbol of Faydwer, now cleansed, to the gnome priest. It is anathema to him, to the corrupt forces in his soul, channeled into him by his dark god and will release the grip of corruption on the land. He is close, I can feel it.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 20691,item2 = 20692,item3 = 20693}))`
18. akanon/"Silox Azrix", hand "Gleaming Unicorn Horn" (20694). Gives "Cleansed Spirit of Faydwer" (20697).
    - event_trade NPC emote: looks up at you with a twisted gleam in his eyes. 'Something for me then, eh?' As he looks closer his skin begins to peel and stretch, a bright hot light emanating from his hands gripped around the unicorn horn. 'NOOOO!' The pure cleansing light burns away the gnome without a trace of his existence except for a tiny ball of light which you pick up.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 20694}))`
19. lakerathe/"Triathalon Swim Goggles", say "Hail". Gives "Rebreather" (16889).
    - Player: "hail"
      - NPC say: Welcome, $name!  Good to see that you came out for the event.  here are some swim goggles to help you cross the lake.  Don't forget to hand these to my friend Bike on the far shore so that you can complete the next leg of the race.
      - Condition: `($text=~/hail/i)`
20. lakerathe/"Triathalon Bike", hand "Rebreather" (16889). Gives "Tan Rope Bridle" (21800).
    - event_item NPC say: Excellent, congratulations  on completing the swim.  Here is something that will help you cross South Karana.  Don't forget to give this to my friend on the bridge before crossing into North Karana.
      - Event guard: `(plugin::check_handin(\%itemcount, 16889 => 1))`
21. southkarana/"Triathalon Running Shoes", hand "Tan Rope Bridle" (21800). Gives "Journeyman's Boots" (2300).
    - event_trade NPC say: Perfect!  Here take these and finish the race! Remember to give this to my friend at the end to receive your proof of completing the race!
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 21800}))`
22. northkarana/"Triathalon Token", hand "Journeyman's Boots" (2300). Gives "Warm Pulsing Treant Heart" (20695).
    - event_trade NPC say: Here, take this to Eldarian over there as fast as you can!
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 2300}))`
23. southkarana/"Yeka Ias", hand "Warm Pulsing Treant Heart" (20695). Gives "Cleansed Spirit of Antonica" (20698).
    - event_trade NPC emote: grabs the heart as you toss it to him before realizing what it is. As soon as it touches his hands, his body convulses, a sickly light emanating from his eyes and oozing cracks appear in his skin. As he melts into the ground, a small glowing ball floats where he once stood.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 20695}))`
24. burningwood/"Telin Darkforest", say "Action". Gives "Worn Note" (20472).
    - Player: "action"
      - NPC emote: looks at you consideringly and then scribbles something quickly on a small, worn paper. 'You seem powerful enough. Perhaps you can help those who seek to protect nature's peace. Take this note. Deliver it only into the hands of Faelin Bloodbriar. Where you will find her, I cannot say. She is a friend of mine and a wanderer. She has been seen from one end of the lands to the other. Seek her out, and quickly.'
        - Reply guard: `(e.other:GetLevel() >= 46)`
      - NPC say: You are not yet powerful enough to complete this task. Return when you have gained more experience.
        - Reply guard: ``
      - Condition: `(fac < 4)`
      - Condition: `(e.message:findi("action"))`
      - Linked from "innoruuk" (explicit prompt).
25. gfaydark/"Faelin Bloodbriar", hand "Worn Note" (20472). Gives "Faelin`s Ring" (20446).
    - event_item NPC emote: reads the note carefully and growls to herself. 'Bad news, eh? Take this ring. There is one elf, dark elf even, whom we must go to in order to gather insight into Innoruuk's plans. Giz X'Tin, he goes by most commonly. Kithicor seems to be his favorite haunt and most likely you will find him there. Don't ask how I know him. Just take the ring as my sign to him and he will speak to you. We don't need to speak again, so don't seek me out. Just go to Telin. I must leave to investigate these events.'
      - Event guard: `(plugin::check_handin(\%itemcount, 20472 => 1))`
26. kithicor/"Giz X-Tin", hand "Faelin`s Ring" (20446). Gives "Dark Metal Coin" (20447).
    - event_item NPC emote: flips you a coin after he recognizes the ring. 'It seems we have a mutual 'acquaintance.' The coin repays an old debt. You don't have to worry about what that is. Luckily, Lord Innoruuk has informed me of your coming and your desires. Fortunately, I have all the answers you require right here at the end of my friend's blade. I think I'll be paying my old 'friend' a visit.'
      - Event guard: `(plugin::check_handin(\%itemcount, 20446 => 1))`
27. burningwood/"Telin Darkforest", hand "Dark Metal Coin" (20447). Gives "Worn Dark Metal Coin" (20448).
    - event_trade NPC emote: scratches the coin as he looks at it. 'Faelin sent you to Giz? Surprising. This coin speaks to the outcome of your talk. He would hardly give this bit of metal to a stranger, but that's a story for a different time. So, you say Giz did confirm Innoruuk's involvement, and something about undead minions? Here, take this coin back. Find Arch Druid Althele in the Karanas and show her that. Tell her what we have discussed. She will look kindly on an ally in this matter.'
      - Event guard: `(fac < 4)`
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 20447}))`
28. eastkarana/"Althele", hand "Worn Dark Metal Coin" (20448). Gives "Braided Grass Amulet" (20450).
    - event_item NPC emote: looks at the coin and nods gravely at you as she slips it into a fold of her clothing. 'I see. The story of this coin speaks much to me as do the words you have given me. Telin sent word that you would arrive. The tidings you bring are ill indeed. Here, take this amulet and find Sionae. She is nearby. We will speak more on this matter when all are present.'
      - Event guard: `(plugin::check_handin(\%itemcount, 20448 => 1))`
29. eastkarana/"Sionae", hand "Braided Grass Amulet" (20450). Gives "Frayed Braided Grass Amulet" (20451).
    - event_item NPC say: I see that the time has come. Take the amulet and give it to the third of our kin, Nuien. I will meet you at the gathering.
      - Event guard: `(plugin::check_handin(\%itemcount, 20450 => 1))`
30. eastkarana/"Teloa", hand "Frayed Braided Grass Amulet" (20451).
    - event_item NPC emote: begins walking toward the gathering spot. 'Follow, friend.'
      - Event guard: `(plugin::check_handin(\%itemcount, 20451 => 1))`
31. Spawns "corruptor" (npc:15153) via `eastkarana/althele#timer:attack`.
32. Kill "corruptor" (NPC 15153) in `eastkarana` and loot "Fleshbound Tome" (20452).
33. eastkarana/"Althele", hand "Fleshbound Tome" (20452). Gives "Earth Stained Note" (18959).
    - event_item NPC emote: hands the book to Tholris who reads through it with lines of concern etched on his face, then whispers into her ear. 'Dire news, indeed. This cannot be allowed. I must keep this book but you, $name, must not allow Innoruuk to seed the land with his hatred and filth. You have only just begun your quest. The path you are guided upon will be difficult, if not impossible, but someone must finish it. Please, take this, read of it, follow its instructions. Tunare bless your path and Karana watch over you.
      - Event guard: `(plugin::check_handin(\%itemcount, 20452 => 1))`
34. misty/"Ella Foodcrafter", hand "Earth Stained Note" (18959).
    - event_item NPC say: Hmmm. I've been waiting for someone to bring me this. I'm sorry such a young one as you has taken up this task. Maybe the sky god blesses ya though. Aye, ya have that look in your eye. Our task is to focus the blessings of the gods and cleanse the filth from the land. I have two tasks for ya.
      - Event guard: `(plugin::check_handin(\%itemcount, 18959 => 1))`
35. misty/"Ella Foodcrafter", say "Two Tasks". Gives "Shiny Tin Bowl" (17860).
    - Player: "two tasks"
      - NPC say: Well, ya ask before ya act. That's a good sign. What I need isn't easy to find. First, I need a mixture. Plain sounding enough but it's a special one. Cleanses the mind and focuses the earth's energies into a forest walker's mind. I don't know how to make it. I don't even know what it's called. I merely know it exists and we'll be needing it for our task. When ya do find how to make it ya can mix it in that bowl. Keep it when you're done, it's a good bowl.
      - Condition: `(($text=~/two tasks/i) && (defined $qglobals{shiny_tin_bowl}))`
36. Forage "Ripened Heartfruit" (20464) in `gfaydark`.
37. Forage "Sweetened Mudroot" (20465) in `misty` or `mistythicket`.
38. Forage "Speckled Molded Mushroom" (20466) in `innothule`.
39. Forage "Chilled Tundra Root" (20467) in `everfrost`.
40. Combine in "Shiny Tin Bowl" (17860): "Ripened Heartfruit" (20464), "Sweetened Mudroot" (20465), "Speckled Molded Mushroom" (20466), "Chilled Tundra Root" (20467). Produces "Hardened Mixture" (20473). Requires Pottery.
41. timorous/"Alrik Farsight", say "Take The Artifact". Gives "Crushed Pot" (20457).
    - Player: "take the artifact"
      - NPC say: Hah! Okay, then. Here take this to Farios Elianos in Felwithe. He will give you the receipt.
      - Condition: `($faction < 5)`
      - Condition: `($text=~/take the artifact/i)`
      - Linked from "ancient bowl" (explicit prompt).
42. felwitheb/"Farios Elianos", hand "Crushed Pot" (20457). Gives "Grocery List" (20458).
    - event_trade NPC say: Eh? What is this? A cracked earthen pot? Why in the nine hells would I need a crushed pot? Perhaps I could use it to not hold water! Why did you even bother me with this? Are you mentally deficient? Apparently. Oh, well, you're just a servant boy. Well, then, we'll make you useful, if just a little. Take this shopping list and go get my groceries. Take it to Nora in the tavern. She'll know what I need.
      - Event guard: `(e.other:GetFaction(e.self) < 5)`
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 20457}))`
43. felwithea/"Merchant Nora", hand "Grocery List" (20458). Gives "Bag of Provisions" (20459).
    - event_trade NPC say: You hardly look like the type of errand runner Farios usually sends out to fetch his groceries but here they are. I hope he chokes on them. Oh, and tell him he still owes me five gold for his last order!
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 20458}))`
44. felwitheb/"Farios Elianos", hand "Bag of Provisions" (20459). Gives "Receipt" (20474).
    - event_trade NPC say: Ah, good. Here's a few copper and a receipt for services rendered. Now be off, I'm sure citizens across the land are in dire need of broken pots at right this moment.
      - Event guard: `(e.other:GetFaction(e.self) < 5)`
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 20459}))`
45. timorous/"Alrik Farsight", hand "Receipt" (20474). Gives "Ancient Pattern" (18960).
    - event_item NPC emote: grins happily. 'Excellent! Was he pleased with the artifact? Oh, that's not even worth answering. I'm sure he was. He's always happy with the things I send him. That's why he honored me with this position of esteem, searching for useful and powerful items in this newly discovered land.'
      - Event guard: `($faction < 5)`
      - Event guard: `(plugin::check_handin(\%itemcount, 20474 => 1))`
46. Kill citymist/"A Black Reaver".
47. Spawns "a black reaver" (npc:90004) via `citymist/a black reaver#event_death_complete`.
48. Kill "a black reaver" (NPC 90004) in `citymist` and loot "Jade Reaver" (5664).
49. kaladimb/"Kinlo Strongarm", hand "Jade Reaver" (5664). Gives "Enchanted Clay" (20455).
    - event_item NPC say: Arrrrr. Ooooo. Arrrrrr... Yah, now that's what I be callin' a good lookin' axe. I be crackin' a few skulls with this one. Oh, here's yer block o' mud. Our priests o' Brell use the mud pit fer relievin' themselves after really hard ale blessin' ceremonies, so ya ain't got ta be enchantin' it in holy water or anythin' cause they already have. Har har!
      - Event guard: `($faction <= 5)`
      - Event guard: `(plugin::check_handin(\%itemcount, 5664 => 1))`
50. Forage "Rose of Firiona" (12774) in `firiona`.
51. qrg/"Merdan Fleetfoot", hand "Rose of Firiona" (12774). Gives "Wood Painting" (20475).
    - event_trade NPC emote: blinks and looks at the flower. 'This is perfect. Thank you! I'm going to go over to her now. Erm, well, maybe I'll wait a week to let the uh.. beauty of the flower.. uhm.. blossom. Yes, that sounds good. Here, you take this painting. I don't need it now. I made it myself, she wouldn't like it anyways.'
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 12774}))`
52. frontiermtns/"A Human Skeleton", hand "Wood Painting" (20475). Gives "Silver Chained Locket" (20476).
    - event_item NPC emote: begins to crack and disintegrate, its body collapsing into a pile of dust that scatters into the winds. On the ground you notice a locket on a fine, thin chain which you pick up.
      - Event guard: `(plugin::check_handin(\%itemcount, 20475 => 1))`
53. qrg/"Niera Farbreeze", hand "Silver Chained Locket" (20476). Gives "Platinum Speckled Powder" (20456).
    - event_trade NPC say: This, this is my mother's amulet. I cannot believe it. Please, take this powder you say you need. Perhaps it does have powers, I don't know, I don't care. Thank you, my eternal thanks for this.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 20476}))`
54. Combine in appropriate tradeskill container: "Ancient Pattern" (18960), "Enchanted Clay" (20455), "Platinum Speckled Powder" (20456). Produces "Runecrested Bowl" (20460). Requires Pottery.
55. misty/"Ella Foodcrafter", hand "Hardened Mixture" (20473) + "Runecrested Bowl" (20460). Gives "Softly Glowing Stone" (20462).
    - event_item NPC emote: smiles slowly as she works the mixture in the bowl and it starts to shine with power. 'This is... a piece of a lost magic item known as Nature's Gem. When restored to completeness I've heard its healing powers will be extraordinary. Take it now. I will take the bowl and hopefully do some good from my end. From here, you can go many ways but I can't guide your path step by step. The only advice I can give you is to look for ones such as yourself.'
      - Event guard: `(plugin::check_handin(\%itemcount, 20473 => 1, 20460 => 1))`
56. Buy "Spell: Resurrection" (15392) from "Henlom Visrek" (NPC 2054) in `qeynos2`. Base price: 18,936 copper.
57. karnor/"Spirit Of Venril Sathir", hand "Spell: Resurrection" (15392).
    - event_item NPC say: I am alive! My thanks to you, $name. And now I will aid you in your quest for preserving the forests of norrath. Your carcass will help nurture the soils of the wilderness.
      - Event guard: `(plugin::check_handin(\%itemcount, 15392 => 1))`
58. Spawns "Venril Sathir" (npc:102126) after the hand-in.
59. Kill "Venril Sathir" (NPC 102126) in `karnor` and loot "Pulsing Green Stone" (20461).
60. firiona/"Foloal Stormforest", hand "Softly Glowing Stone" (20462) + "Pulsing Green Stone" (20461). Gives "Warmly Glowing Stone" (20468).
    - event_item NPC emote: blinks and carefully takes the stones from you, cautiously scratching the jagged green stone against the other. Its skin seems to shiver and flake at the contact and eventually begins to shine brightly. 'With the gem nature's balance is complete. Take the stone and walk your path. Blade or lightning caller, burning sword or the mother's walk.'
      - Event guard: `(plugin::check_handin(\%itemcount, 20462 => 1, 20461 => 1))`
61. misty/"Ella Foodcrafter", hand "Warmly Glowing Stone" (20468). Gives "Elaborate Scimitar" (20440).
    - event_item NPC emote: hands you a scimitar she usually wears at her side. 'Thank you, $name. With this we can hold back the corruption. We have learned something new though. Not only is this work the responsibility of the lord of hatred alone. For some reason we cannot know the lord of disease has decided it worthy of his time to work in conjunction with Innoruuk. The spirits of the three main continents, Faydwer Antonica and Kunark, have been corrupted. Look for the corrupted forces of the land and heal them. When you have found them all then take my scimitar and the spirits to Xanuusus.'
      - Event guard: `(plugin::check_handin(\%itemcount, 20468 => 1))`
62. northkarana/"Xanuusus", hand "Cleansed Spirit of Kunark" (20699) + "Cleansed Spirit of Faydwer" (20697) + "Cleansed Spirit of Antonica" (20698) + "Elaborate Scimitar" (20440). Gives "Nature Walkers Scimitar" (20490).
    - event_trade NPC emote: pushes the spirits into the air, making them dance around the scimitar. With a wave of his hand they melt into the blade and hilt of the weapon. 'With this the spirits of the lands are now free from the corruption of the dark gods.  Through your strength and dedication was this possible, .  May the foul poison that once poured into the earth itself never do so again. Take this weapon that you may continue to watch over the balance of nature. Go now, with the gods' blessings.'
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 20699,item2 = 20697,item3 = 20698,item4 = 20440}))`

## Epic 1.5

### "Staff of Living Brambles" (62863)

<a id="epic-item-62863"></a>

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
9. Loot "Small Block of Clay" (16900) from "a muddite recordkeeper" (NPC 16003) in `beholder`. Drop cache: 5.2127% chance per kill.
10. Combine in appropriate tradeskill container: "Small Block of Clay" (16900), "Water Flask" (13006). Produces "Block of Clay" (16901). Requires Pottery.
11. Buy "Aerated Pot Sketch" (62858) from "Elisha Dirtyshoes" (NPC 202134) in `poknowledge`. Base price: 300 copper.
12. Combine in appropriate tradeskill container: "Water Flask" (13006), "Block of Clay" (16901), "Aerated Pot Sketch" (62858). Produces "Aerated Pot Shell" (62860). Requires Pottery.
13. Combine in appropriate tradeskill container: "Chunk of Energized Clay" (62859), "Aerated Pot Shell" (62860). Produces "Reinforced Aerated Pot" (62861). Requires Pottery.
14. Spawns "an ancient thought horror" (npc:164122) via `thedeep/ancient thought horror trap#enter`.
15. Kill "an ancient thought horror" (NPC 164122) in `thedeep` and loot "Thick Spinal Fluid" (40420).
16. Forage "Sickly Maiden's Hair" (62810) in `rathemtn`.
17. eastkarana/"Althele", hand "Sickly Maiden's Hair" (62810). Gives "Tuft of Sickly Maiden's Hair" (62811).
    - event_item NPC say: This plant has an illness that I have never sensed before.' Althele pauses in thought for a moment. 'You are a hunter, so I shall put your skills to work. First, take this to Corun in Surefall. He is an expert on animal illnesses. Then put your hunting skills to work and see if you can capture any animals that may have eaten this plant. Corun will want to see them to help him discover what the sickness is.
      - Event guard: `(plugin::check_handin(\%itemcount, 62810 => 1))`
18. qrg/"Corun Finisc", hand "Tuft of Sickly Maiden's Hair" (62811). Gives "Borrowed Medicine Bag" (62605) + "Magical Sample Vial" (62657).
    - event_trade NPC say: Well, this is certainly an unpleasant sight. If Althele sent you to me it must be because I've had a lot of experience with sick animals. If you can find me some animals that have become ill by eating this plant perhaps I can discover something about this disease. You must not kill these animals. It is never good to harm an animal if you do not need to. It is also important that the animal be alive when you take samples of their blood. If any animals have eaten this plant and become ill, you need to find a way to capture them and use your fletching kit and these vials to gather blood samples. Althele is rarely wrong about what she senses from Antonica. Be careful with that medicine bag, I borrowed it from a friend in Halas a while back. I'll need you to use it to store some samples as you capture the animals. Don't lose it, you don't want Lars angry with you!
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 62811}))`
19. Spawns "an asteatotic highborn" (npc:109907) via `veksar/player#enter`.
20. Kill "an asteatotic highborn" (NPC 109907) in `veksar` and loot "Asteatotic Veksar Blood" (35100).
21. Spawns "a neuralgic huntress" (npc:120136) via `westwastes/player#enter`.
22. Kill "a neuralgic huntress" (NPC 120136) in `westwastes` and loot "Neuralgic Wyvern Blood" (72605).
23. Summon "Collapsible Fletching Kit" (17189) by casting "Unfold Fletching Kit".
24. cazicthule/"A Sickly Mosquito", say "". Gives "Captured Mosquito" (62642).
25. Combine in "Collapsible Fletching Kit" (17189): "Magical Sample Vial" (62657), "Captured Mosquito" (62642). Produces "Sickly Mosquito Blood Sample" (62611). Requires Fletching.
26. sirens/"A Twitching Swordfish", say "". Gives "Captured Swordfish" (62643).
27. Combine in "Collapsible Fletching Kit" (17189): "Magical Sample Vial" (62657), "Captured Swordfish" (62643). Produces "Twitching Swordfish Blood Sample" (62612). Requires Fletching.
28. chardokb/"A Leprous Chokidai", say "". Gives "Captured Chokidai" (62645).
29. Combine in "Collapsible Fletching Kit" (17189): "Magical Sample Vial" (62657), "Captured Chokidai" (62645). Produces "Leprous Chokidai Blood Sample" (62614). Requires Fletching.
30. droga/"A Bloated Drogan Spider", say "". Gives "Captured Spider" (62644).
31. Combine in "Collapsible Fletching Kit" (17189): "Magical Sample Vial" (62657), "Captured Spider" (62644). Produces "Bloated Drogan Spider Blood Sample" (62613). Requires Fletching.
32. Combine in "Borrowed Medicine Bag" (62605): "Asteatotic Veksar Blood" (35100), "Neuralgic Wyvern Blood" (72605), "Sickly Mosquito Blood Sample" (62611), "Twitching Swordfish Blood Sample" (62612), "Leprous Chokidai Blood Sample" (62614), "Bloated Drogan Spider Blood Sample" (62613). Produces "Full Medicine Bag" (62616). Requires Remove Traps.
33. qrg/"Corun Finisc", hand "Full Medicine Bag" (62616). Gives "Corun's Notes" (62617).
    - event_trade NPC say: This is frightening. A disease that can affect mosquito and wyvern must be a truly horrible thing. I will examine these samples carefully and pass knowledge to others who are working to repair this. From what you've shown me I can tell that the disease affects both the mind and the skin. Others seek information about illnesses of the skin. I need you to uncover information about diseases of the mind. I know not where to find such information, but you are a seeker and a worthy ranger. Find someone, somewhere, that knows enough about disease that affects 'more advanced' creatures such as men. Learn about the diseases of the mind. I will seek among the folk of the glade and pine for assistance with a cure for the Maiden's Hair. Please do not give up the search, no matter how difficult. This is a terrible illness and we must stop it from spreading. Take a copy of my notes with you, they may be of use to someone with the right knowledge.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 62616}))`
34. freeportwest/"Shana Liskia", hand "Corun's Notes" (62617). Gives "Corun's Notes - annotated" (62654).
    - event_trade NPC say: Well, this certainly is an interesting puzzle. I see here that these creatures were infected in their spinal columns. I'll tell you that a part of my research involves the use of the fluids of the brain and spine. I suspect that further details might be unpleasant. I might be able to help you, but I'll need materials to work with. Gather fluids from the brain of the creature with the greatest mental power that you can find. I'll test it and see if it's strong enough and has the right properties. If I can duplicate what you saw in these infected creatures, perhaps I can help. Aslo, bring back those notes that Corun made, I'll need them as well.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 62617}))`
    - event_trade NPC emote: makes a few hasty scribbles in the margins of Corun's Notes and hands them back to you.
35. freeportwest/"Shana Liskia", hand "Thick Spinal Fluid" (40420) + "Corun's Notes - annotated" (62654). Gives "Mind Crystal" (62846).
    - event_trade NPC say: Perfect! Yes, this will work nicely. Shana looks through Corun's notes while gathering items from her stores. This should work. What I'm going to do is grow a crystal around this fluid and some of the key ingredients of the disease. The crystal will focus the power of the fluid and the elements of the disease will guide it. If this goes well, I should be able to create a crystal that will guide you to the disease. Shana places the gathered items into a violet-tinted container and casts a spell over them. A moment later she retrieves a crystal from the container. The crystal is clear except for a dark, murky coloration at the center. Take that crystal and see if you can locate any creatures with the disease. If you have any success, please return and let me know.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 40420,item2 = 62654}))`
36. eastkarana/"Tholris", say "You Are Diseased". Gives "Red Crystal" (62618).
    - Player: "you are diseased"
      - NPC emote: looks at you indignantly
        - Reply guard: `($saydisease==1)`
      - NPC emote: kicks dirt at your feet
        - Reply guard: `($saydisease==2)`
      - NPC emote: shakes his head. Then he catches a glimpse of the Mind Crystal and looks thoughtful for a moment. Then he reaches into his pocket and produces two unusual crystals and hands them to you.
        - Reply guard: `($saydisease==3)`
      - Condition: `(($text=~/you are diseased/i) && plugin::check_hasitem($client, 62846))`
37. freeportwest/"Shana Liskia", hand "Red Crystal" (62618) + "Violet Crystal" (62619). Gives "Letter to Corun" (62655).
    - event_trade NPC say: Ah, well, it seems as though the crystal was attuned to these other crystals. They must have come in contact with a rather large element of the disease, otherwise I just can't see how the Mind Crystal would have noticed them. These crystals were created by someone with more experience than I have in this area. I will examine them further and attempt to learn something from them. I can tell now, though, that they were probably created in a fashion similar to the one I used to create the Mind Crystal. Shana pulls out a piece of parchment and writes a note. She gives you the note and says, Take this note to Corun along with the Mind Crystal. He can use the crystal and my notes to seek out the plague in whatever fashion he thinks is best. I need to get to work investigating these new crystals.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 62618,item2 = 62619}))`
38. qrg/"Corun Finisc", hand "Mind Crystal" (62846) + "Letter to Corun" (62655). Gives "Red Dogwood Seed" (62844).
    - event_trade NPC emote: looks at the crystal for a moment; confusion, disgust and curiosity chasing each other across his tired face. After reading the letter, he looks up at you.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 62846,item2 = 62655}))`
    - event_trade NPC say: This crystal seems strange, but if you and this Shana believe that it will help, then I know just the person to put it to work.' Corun puts the note and the crystal into a pouch. He reaches into another pouch to retrieve something small and hands it to you. 'This seed was brought to us by a druid of great skill. It should provide the cure we seek, but we do not know the place or circumstances under which to plant it. We have agreed to leave it to you to find that place and that time. I urge you to hasten, we do not know how long it will be until the plague is released upon us in earnest. The only thing that I know is that there may be a link between those that created the disease and the Plane of Discord. A very tenuous link, but keep the seed with you at all times, you never know when you will need it. May the Mother smile on your effort.
39. Spawns "spawn #Swamp Terror" (npc:47208) via `feerrott/druid epic trap#enter`.
40. Kill "spawn #Swamp Terror" (NPC 47208) in `feerrott` and loot "Mangled Head" (62818).
41. Combine recipe 19887 (container 62847): "Mangled Head" (62818). Produces "Wrapped Mangled Head" (62848). Requires Remove Traps.
42. qrg/"Niera Farbreeze", hand "Wrapped Mangled Head" (62848). Gives "Mangled Head" (62827).
    - event_trade NPC emote: examines the head. You say that this might belong to one of those that is involved in all of this? Even if we had seen this person before we'd never be able to recognize it. I don't know how you'll be able to get any information from that, but it's our only clue. See if you can find a way to learn the identity of that head, but first I need you to learn as much as you can about diseases of the skin. Others have come up with some useful information about diseases of the mind and we need your research to put this puzzle together.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 62848}))`
43. poknowledge/"Pathfinder Arelat", say "Worth It". Gives "Fresh Awakenings vol. 1" (62839).
    - Player: "worth it"
      - NPC say: Then here it is. This is a copy of an ancient text that we have preserved and copied for many long years. The author died generations ago. You should read it before you give it to that witch. Good luck to you, friend.
      - Condition: `(qglobals["druid_epic"] == "2" and e.message:findi("worth it"))`
      - Linked from "Corruption of the Night" (explicit prompt).
44. poknowledge/"Gravelady Beddia", hand "Fresh Awakenings vol. 1" (62839) + "Fresh Awakenings vol. 2" (62840) + "Fresh Awakenings vol. 3" (62841). Gives "Healing Plants" (62842).
45. qrg/"Niera Farbreeze", hand "Healing Plants" (62842). Gives "Niera's Healing Notes" (62849).
    - event_trade NPC say: That's great! Niera scribbles some notes as she flips through the text. She then hands the notes to you, keeping the book herself. There is some useful information in there. Hold onto these notes until later, you may need them. Give them back to me when you've discovered the identity of that skull.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 62842}))`
46. feerrott/"Corrupted Spirit", say "Show It". Gives "Disease Rune" (62837).
    - Player: "show it"
      - NPC message: The skull of the dead acolyte glows briefly and all of the remaining flesh falls from it. An ephemeral rune appears in your hand. 'Place that where that horrible stone was before, in my very own head with that nasty scroll, and you will be able to engrave it into my skull. My poor skull! Hurry up, though, that rune won't last forever.
      - Condition: `(qglobals["druid_epic"] == "3" and e.message:findi("show it"))`
      - Linked from "What plague?" (explicit prompt).
47. tox/"A Skeleton", say "". Gives "Animating Heads" (62828).
48. Combine in "Mangled Head" (62827): "Disease Rune" (62837), "Animating Heads" (62828). Produces "Runed Skull" (62838). Requires Remove Traps.
49. qrg/"Niera Farbreeze", hand "Runed Skull" (62838) + "Niera's Healing Notes" (62849). Gives "Niera's Research Notes" (62843).
    - event_trade NPC say: That's an amazing story. So there is a coven of Mordavin's followers out there. This is indeed bad news.' She gathers all of the information she has gained so far. She examines the rune on the skull and the text on healing plants. She then pulls out a worn bag and shows you several blood and skin samples from various creatures. All look sickly to you. Niera looks at you and sighs. 'We have a lot of information now, thanks to you and one of our Rangers. We know the nature of the disease and we know the identity of those that created it. Now we need to find the cure. A council of the learned has reviewed all of the information brought to us so far, and this text confirms our suspicions. We need the help of the Unkempt to find a cure. That is your task now. Find the Unkempt and ask them for help. Take these notes, they will explain the details, if you can find someone to give them to.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 62838, item2 = 62849}))`
50. pojustice/"Great Bear", hand "Niera's Research Notes" (62843). Gives "Living Brambles Seed" (62845).
    - event_trade NPC emote: looks at the paper you hand him. 'I can almost understand this writing. This is not a natural disease. I see that you understand the seed rituals, this is good.' The ursine waves his arms in a way that might indicate that he is casting a spell, though it looks little like the sort of spell casting you know. Two seeds appear in his hands. 'Good. I was not sure that I could grow these here. Take them. One is for your cause, one is for you.
      - Event guard: `(qglobals["druid_epic"] == "4" and e.other:GetFaction(e.self) < 5 and item_lib.check_turn_in(e.trade, {item1 = 62843}) )`
51. qrg/"Niera Farbreeze", hand "Red Dogwood Seed" (62844) + "Living Brambles Seed" (62845). Gives "Living Brambles Seed" (62850).
    - event_trade NPC say: Wonderful! These are amazing seeds! I've never seen any just like them before. And you got them from one of the Unkempt. Amazing.' Niera examines the seeds closely while referring to a book called Unkempt Seed Rituals. She wraps both seeds in a soft, moist cloth and hands one of them to you. 'I think I know what the Unkempt meant. This one is for you. Keep it safe. I believe that I know where the other is needed. I have learned much while you were gone and I need to tell you about it.
      - Event guard: `(qglobals["druid_epic"] == "4" and item_lib.check_turn_in(e.trade, {item1 = 62844, item2 = 62845}))`
    - event_trade NPC say: Others have discovered a method for locating the virus. Our brothers and sisters, along with the help of Shana Liskia in Freeport, have grown a crystal from traces of the disease and that crystal can find the disease. They have called it a Mind Crystal, though I'm not sure why. Take it. I need you to put it to work for us. Go out and use it to find the members of that coven and destroy them. I know that we have few clues as to where to look, but you have been wonderfully clever so far and we're relying on you to hunt them down.
52. Loot "Crystal Fragment" (62852) from "Finnelzi Springworthy" (NPC 14190) in `southkarana`. Drop cache: 100% chance per kill.
53. freportw/"Shana Liskia", hand "Crystal Fragment" (62852). Gives "Small Padded Bag" (62853).
    - event_trade NPC say: Well these certainly are interesting. You say there might be more of them on those necromancers that escaped? Well here, take this. Find all of them and place them into this bag to keep them safe. Then bring them all to me and I'll examine them more closely. I can tell you that they are similiar to the Mind Crystal, but it appears to have different magical properties. I have never seen anything like them and I suspect that they are not from Norrath.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 62852,item2 = 62852,item3 = 62852}))`
54. Spawns "Azibelle Spavin" (npc:335064) via `harbingers/druid epic trap#enter`.
55. Kill "Azibelle Spavin" (NPC 335064) in `harbingers` and loot "Bohab's Crystal Fragment" (62886).
56. Kill "Azibelle Spavin" (NPC 335064) in `harbingers` and loot "Azibelle's Crystal Fragment" (62887).
57. Kill "Glenfire Telzir" (NPC 335065) in `harbingers` and loot "Glenfire's Crystal Fragment" (62888).
58. Combine in "Small Padded Bag" (62853): "Bohab's Crystal Fragment" (62886), "Azibelle's Crystal Fragment" (62887), "Glenfire's Crystal Fragment" (62888), "Crystal Fragment" (62852). Produces "Full Padded Bag" (62854). Requires Remove Traps.
59. freportw/"Shana Liskia", hand "Full Padded Bag" (62854). Gives "Bowl of Foul-smelling Liquid" (62855).
    - event_trade NPC emote: takes the crystal fragments from the pouch. She applies a drop of liquid to it. The liquid turns the crystal white where it spreads.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 62854}))`
    - event_trade NPC say: These small crystals are easier to work with than the Mind Crystal. They also differ from the Mind Crystal in that they are from the Plane of Discord. Take this mixture and find something to enhance its magical power and you just might be able to purify the Mind Crystal. I have no idea what that might be, but I know what it should be. You'll need two components. One will increase the power of the mixture, something with a lot of magical power. It needs to be a liquid or powder to integrate properly. And you'll need a stabilizer, something to help the mixture and the new material to remain stable. This influences the kind of attunement that the crystal takes on during the process. It should be something from nature if you want the result to suit your tastes. You'll have to find someone that knows of something about it among the druids for help on what to use.
60. Loot "Energized Noc Blood" (62889) from "Noc Juggernaut".
61. Forage "Emerald Moss" (62856) in `emeraldjungle`.
62. Combine in "Bowl of Foul-smelling Liquid" (62855): "Energized Noc Blood" (62889), "Emerald Moss" (62856), "Mind Crystal" (62846). Produces "Clear Mind Crystal" (62857). Requires Remove Traps.
63. Kill kithicor/"Blackened Treant".
64. Spawns "Blackened Dryad" (npc:20301) via `kithicor/blackened tree limb#event_death_complete`.
65. Kill "Blackened Dryad" (NPC 20301) in `kithicor` and loot "Blackened Earth" (62862).
66. Combine in "Reinforced Aerated Pot" (62861): "Living Brambles Seed" (62850), "Clear Mind Crystal" (62857), "Blackened Earth" (62862). Produces "Staff of Living Brambles" (62863). Requires Remove Traps.

## Epic 2.0

### "Staff of Everliving Brambles" (62880)

<a id="epic-item-62880"></a>

**Earlier reward routes required by this graph path:** ["Staff of Living Brambles" (62863)](#epic-item-62863).
Revisit those instructions if another copy of a consumed item is needed.

1. global/"Global Player", say "Recipe:19908". Gives "Insulated Container" (62876).
2. Combine in "Insulated Container" (62876): "Essence of Rainfall" (62883), "Staff of Living Brambles" (62863). Produces "Staff of Everliving Brambles" (62880). Requires Remove Traps.
