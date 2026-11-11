# Ranger — Epic Quest Walkthrough

Generated directly from quest-graph item rewards. Unresolved dependencies are marked, not inferred.

## Epic 1.0

### "Swiftwind" (20487)

<a id="epic-item-20487"></a>

1. burningwood/"Telin Darkforest", say "Hail".
    - Player: "hail"
      - NPC emote: looks at you serenely. 'Hello, wanderer.'
      - Condition: `(fac < 4)`
      - Condition: `(e.message:findi("hail"))`
2. burningwood/"Telin Darkforest", say "Action". Gives "Worn Note" (20472).
    - Player: "action"
      - NPC emote: looks at you consideringly and then scribbles something quickly on a small, worn paper. 'You seem powerful enough. Perhaps you can help those who seek to protect nature's peace. Take this note. Deliver it only into the hands of Faelin Bloodbriar. Where you will find her, I cannot say. She is a friend of mine and a wanderer. She has been seen from one end of the lands to the other. Seek her out, and quickly.'
        - Reply guard: `(e.other:GetLevel() >= 46)`
      - NPC say: You are not yet powerful enough to complete this task. Return when you have gained more experience.
        - Reply guard: ``
      - Condition: `(fac < 4)`
      - Condition: `(e.message:findi("action"))`
      - Linked from "innoruuk" (explicit prompt).
3. gfaydark/"Faelin Bloodbriar", hand "Worn Note" (20472). Gives "Faelin`s Ring" (20446).
    - event_item NPC emote: reads the note carefully and growls to herself. 'Bad news, eh? Take this ring. There is one elf, dark elf even, whom we must go to in order to gather insight into Innoruuk's plans. Giz X'Tin, he goes by most commonly. Kithicor seems to be his favorite haunt and most likely you will find him there. Don't ask how I know him. Just take the ring as my sign to him and he will speak to you. We don't need to speak again, so don't seek me out. Just go to Telin. I must leave to investigate these events.'
      - Event guard: `(plugin::check_handin(\%itemcount, 20472 => 1))`
4. kithicor/"Giz X-Tin", hand "Faelin`s Ring" (20446). Gives "Dark Metal Coin" (20447).
    - event_item NPC emote: flips you a coin after he recognizes the ring. 'It seems we have a mutual 'acquaintance.' The coin repays an old debt. You don't have to worry about what that is. Luckily, Lord Innoruuk has informed me of your coming and your desires. Fortunately, I have all the answers you require right here at the end of my friend's blade. I think I'll be paying my old 'friend' a visit.'
      - Event guard: `(plugin::check_handin(\%itemcount, 20446 => 1))`
5. burningwood/"Telin Darkforest", hand "Dark Metal Coin" (20447). Gives "Worn Dark Metal Coin" (20448).
    - event_trade NPC emote: scratches the coin as he looks at it. 'Faelin sent you to Giz? Surprising. This coin speaks to the outcome of your talk. He would hardly give this bit of metal to a stranger, but that's a story for a different time. So, you say Giz did confirm Innoruuk's involvement, and something about undead minions? Here, take this coin back. Find Arch Druid Althele in the Karanas and show her that. Tell her what we have discussed. She will look kindly on an ally in this matter.'
      - Event guard: `(fac < 4)`
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 20447}))`
6. eastkarana/"Althele", hand "Worn Dark Metal Coin" (20448). Gives "Braided Grass Amulet" (20450).
    - event_item NPC emote: looks at the coin and nods gravely at you as she slips it into a fold of her clothing. 'I see. The story of this coin speaks much to me as do the words you have given me. Telin sent word that you would arrive. The tidings you bring are ill indeed. Here, take this amulet and find Sionae. She is nearby. We will speak more on this matter when all are present.'
      - Event guard: `(plugin::check_handin(\%itemcount, 20448 => 1))`
7. eastkarana/"Sionae", hand "Braided Grass Amulet" (20450). Gives "Frayed Braided Grass Amulet" (20451).
    - event_item NPC say: I see that the time has come. Take the amulet and give it to the third of our kin, Nuien. I will meet you at the gathering.
      - Event guard: `(plugin::check_handin(\%itemcount, 20450 => 1))`
8. eastkarana/"Teloa", hand "Frayed Braided Grass Amulet" (20451).
    - event_item NPC emote: begins walking toward the gathering spot. 'Follow, friend.'
      - Event guard: `(plugin::check_handin(\%itemcount, 20451 => 1))`
9. Spawns "corruptor" (npc:15153) via `eastkarana/althele#timer:attack`.
10. Kill "corruptor" (NPC 15153) in `eastkarana` and loot "Fleshbound Tome" (20452).
11. eastkarana/"Althele", hand "Fleshbound Tome" (20452). Gives "Earth Stained Note" (18959).
    - event_item NPC emote: hands the book to Tholris who reads through it with lines of concern etched on his face, then whispers into her ear. 'Dire news, indeed. This cannot be allowed. I must keep this book but you, $name, must not allow Innoruuk to seed the land with his hatred and filth. You have only just begun your quest. The path you are guided upon will be difficult, if not impossible, but someone must finish it. Please, take this, read of it, follow its instructions. Tunare bless your path and Karana watch over you.
      - Event guard: `(plugin::check_handin(\%itemcount, 20452 => 1))`
12. misty/"Ella Foodcrafter", hand "Earth Stained Note" (18959).
    - event_item NPC say: Hmmm. I've been waiting for someone to bring me this. I'm sorry such a young one as you has taken up this task. Maybe the sky god blesses ya though. Aye, ya have that look in your eye. Our task is to focus the blessings of the gods and cleanse the filth from the land. I have two tasks for ya.
      - Event guard: `(plugin::check_handin(\%itemcount, 18959 => 1))`
13. misty/"Ella Foodcrafter", say "Two Tasks". Gives "Shiny Tin Bowl" (17860).
    - Player: "two tasks"
      - NPC say: Well, ya ask before ya act. That's a good sign. What I need isn't easy to find. First, I need a mixture. Plain sounding enough but it's a special one. Cleanses the mind and focuses the earth's energies into a forest walker's mind. I don't know how to make it. I don't even know what it's called. I merely know it exists and we'll be needing it for our task. When ya do find how to make it ya can mix it in that bowl. Keep it when you're done, it's a good bowl.
      - Condition: `(($text=~/two tasks/i) && (defined $qglobals{shiny_tin_bowl}))`
14. Forage "Ripened Heartfruit" (20464) in `gfaydark`.
15. Forage "Sweetened Mudroot" (20465) in `misty` or `mistythicket`.
16. Forage "Speckled Molded Mushroom" (20466) in `innothule`.
17. Forage "Chilled Tundra Root" (20467) in `everfrost`.
18. Combine in "Shiny Tin Bowl" (17860): "Ripened Heartfruit" (20464), "Sweetened Mudroot" (20465), "Speckled Molded Mushroom" (20466), "Chilled Tundra Root" (20467). Produces "Hardened Mixture" (20473). Requires Pottery.
19. timorous/"Alrik Farsight", say "Take The Artifact". Gives "Crushed Pot" (20457).
    - Player: "take the artifact"
      - NPC say: Hah! Okay, then. Here take this to Farios Elianos in Felwithe. He will give you the receipt.
      - Condition: `($faction < 5)`
      - Condition: `($text=~/take the artifact/i)`
      - Linked from "ancient bowl" (explicit prompt).
20. felwitheb/"Farios Elianos", hand "Crushed Pot" (20457). Gives "Grocery List" (20458).
    - event_trade NPC say: Eh? What is this? A cracked earthen pot? Why in the nine hells would I need a crushed pot? Perhaps I could use it to not hold water! Why did you even bother me with this? Are you mentally deficient? Apparently. Oh, well, you're just a servant boy. Well, then, we'll make you useful, if just a little. Take this shopping list and go get my groceries. Take it to Nora in the tavern. She'll know what I need.
      - Event guard: `(e.other:GetFaction(e.self) < 5)`
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 20457}))`
21. felwithea/"Merchant Nora", hand "Grocery List" (20458). Gives "Bag of Provisions" (20459).
    - event_trade NPC say: You hardly look like the type of errand runner Farios usually sends out to fetch his groceries but here they are. I hope he chokes on them. Oh, and tell him he still owes me five gold for his last order!
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 20458}))`
22. felwitheb/"Farios Elianos", hand "Bag of Provisions" (20459). Gives "Receipt" (20474).
    - event_trade NPC say: Ah, good. Here's a few copper and a receipt for services rendered. Now be off, I'm sure citizens across the land are in dire need of broken pots at right this moment.
      - Event guard: `(e.other:GetFaction(e.self) < 5)`
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 20459}))`
23. timorous/"Alrik Farsight", hand "Receipt" (20474). Gives "Ancient Pattern" (18960).
    - event_item NPC emote: grins happily. 'Excellent! Was he pleased with the artifact? Oh, that's not even worth answering. I'm sure he was. He's always happy with the things I send him. That's why he honored me with this position of esteem, searching for useful and powerful items in this newly discovered land.'
      - Event guard: `($faction < 5)`
      - Event guard: `(plugin::check_handin(\%itemcount, 20474 => 1))`
24. Kill citymist/"Npc:90004".
25. Spawns "a black reaver" (npc:90004) via `citymist/npc:90004#event_death_complete`.
26. Kill "a black reaver" (NPC 90004) in `citymist` and loot "Jade Reaver" (5664).
27. kaladimb/"Kinlo Strongarm", hand "Jade Reaver" (5664). Gives "Enchanted Clay" (20455).
    - event_item NPC say: Arrrrr. Ooooo. Arrrrrr... Yah, now that's what I be callin' a good lookin' axe. I be crackin' a few skulls with this one. Oh, here's yer block o' mud. Our priests o' Brell use the mud pit fer relievin' themselves after really hard ale blessin' ceremonies, so ya ain't got ta be enchantin' it in holy water or anythin' cause they already have. Har har!
      - Event guard: `($faction <= 5)`
      - Event guard: `(plugin::check_handin(\%itemcount, 5664 => 1))`
28. Forage "Rose of Firiona" (12774) in `firiona`.
29. qrg/"Merdan Fleetfoot", hand "Rose of Firiona" (12774). Gives "Wood Painting" (20475).
    - event_trade NPC emote: blinks and looks at the flower. 'This is perfect. Thank you! I'm going to go over to her now. Erm, well, maybe I'll wait a week to let the uh.. beauty of the flower.. uhm.. blossom. Yes, that sounds good. Here, you take this painting. I don't need it now. I made it myself, she wouldn't like it anyways.'
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 12774}))`
30. frontiermtns/"A Human Skeleton", hand "Wood Painting" (20475). Gives "Silver Chained Locket" (20476).
    - event_item NPC emote: begins to crack and disintegrate, its body collapsing into a pile of dust that scatters into the winds. On the ground you notice a locket on a fine, thin chain which you pick up.
      - Event guard: `(plugin::check_handin(\%itemcount, 20475 => 1))`
31. qrg/"Niera Farbreeze", hand "Silver Chained Locket" (20476). Gives "Platinum Speckled Powder" (20456).
    - event_trade NPC say: This, this is my mother's amulet. I cannot believe it. Please, take this powder you say you need. Perhaps it does have powers, I don't know, I don't care. Thank you, my eternal thanks for this.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 20476}))`
32. Combine in appropriate tradeskill container: "Ancient Pattern" (18960), "Enchanted Clay" (20455), "Platinum Speckled Powder" (20456). Produces "Runecrested Bowl" (20460). Requires Pottery.
33. misty/"Ella Foodcrafter", hand "Hardened Mixture" (20473) + "Runecrested Bowl" (20460). Gives "Softly Glowing Stone" (20462).
    - event_item NPC emote: smiles slowly as she works the mixture in the bowl and it starts to shine with power. 'This is... a piece of a lost magic item known as Nature's Gem. When restored to completeness I've heard its healing powers will be extraordinary. Take it now. I will take the bowl and hopefully do some good from my end. From here, you can go many ways but I can't guide your path step by step. The only advice I can give you is to look for ones such as yourself.'
      - Event guard: `(plugin::check_handin(\%itemcount, 20473 => 1, 20460 => 1))`
34. Buy "Spell: Resurrection" (15392) from "Henlom Visrek" (NPC 2054) in `qeynos2`. Base price: 18,936 copper.
35. karnor/"Spirit Of Venril Sathir", hand "Spell: Resurrection" (15392).
    - event_item NPC say: I am alive! My thanks to you, $name. And now I will aid you in your quest for preserving the forests of norrath. Your carcass will help nurture the soils of the wilderness.
      - Event guard: `(plugin::check_handin(\%itemcount, 15392 => 1))`
36. Spawns "Venril Sathir" (npc:102126) after the hand-in.
37. Kill "Venril Sathir" (NPC 102126) in `karnor` and loot "Pulsing Green Stone" (20461).
38. firiona/"Foloal Stormforest", hand "Softly Glowing Stone" (20462) + "Pulsing Green Stone" (20461). Gives "Warmly Glowing Stone" (20468).
    - event_item NPC emote: blinks and carefully takes the stones from you, cautiously scratching the jagged green stone against the other. Its skin seems to shiver and flake at the contact and eventually begins to shine brightly. 'With the gem nature's balance is complete. Take the stone and walk your path. Blade or lightning caller, burning sword or the mother's walk.'
      - Event guard: `(plugin::check_handin(\%itemcount, 20462 => 1, 20461 => 1))`
39. burningwood/"Telin Darkforest", hand "Warmly Glowing Stone" (20468). Gives "Ancient Longsword" (20477).
    - event_trade NPC emote: nods as he unbuckles his sword and hands it to you. 'The storm callers are working on containing and fighting against the corruption but they can not hold back the inevitable for long. It is up to us to strike against Innoruuk directly. If we were warriors or paladins we would have a fancy ceremony and plenty of feasting but we're just rangers, without time for pleasantries. The sword you hold in your hands is one of the oldest blades known, even to the eldest. To strike at the darkest heart of evil requires a weapon beyond this, or even ones you may carry at your side. The first task, the first preparation you must make, is the smithing of that blade. Its edge sharpened, its balance made perfect. When you have finished, bring me this sword again.'
      - Event guard: `(fac < 4)`
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 20468}))`
40. kaladimb/"Usbak The Old", hand "Ancient Longsword" (20477). Gives "Refined Ancient Sword" (20481).
    - event_item NPC emote: admires the blade and then starts to bang the edge with a hammer. 'Hah, that was a good blade, no doubt. Ain't seen one I couldn't make better though. I'm knowin' yer cause and all I know is ye should take that ancient blade ta yer friend in the woods, he'll know what to do now. With that I'm gonna be takin muh leave. Debt paid and all. If'n yer wantin' another blade, which ye do, ye got enough ore left that Kinlo can do it for ye'
      - Event guard: `(plugin::check_handin(\%itemcount, 20477 => 1))`
41. burningwood/"Faelin Bloodbriar", hand "Refined Ancient Sword" (20481). Gives "Swiftwind" (20487).
    - event_trade NPC emote: smiles at you, then closes her eyes as she sets the gem 'Nature's Balance' into the crossguard and begins to channel her spirit into the sword. The ground rumbles loudly as she casts. She collapses in exhaustion after a short time. 'Take the blade, and perhaps you can finish this. You must strike at the heart of Innoruuk's lair. Bring a shattered gem and the mithril blade to Xanuusus. Only by weakening Innoruuk's grip over his realm can the balance of the land once again be restored. If we do not meet again, , remember you always have my eternal thanks.'
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 20481}))`

### "Earthcaller" (20488)

<a id="epic-item-20488"></a>

1. Shared prerequisite: see ["Swiftwind" (20487)](#epic-item-20487), steps 1–13. Follow those instructions again if the required item was consumed or another copy is needed.
2. hole/"Jaeil The Wretched", hand "Shiny Tin Bowl" (17860).
    - event_item NPC emote: howls in anger, his body seeming to suck energy from the walls around him as he sees his reflection. He pulls a hammer from the bundle in his arms and swings fiercely at your head.
      - Event guard: `(plugin::check_handin(\%itemcount, 17860 => 1))`
3. Spawns "Jaeil the Insane" (npc:39154) after the hand-in.
4. Kill "Jaeil the Insane" (NPC 39154) in `hole` and loot "Soulbound Hammer" (20478).
5. erudnint/"Mairee Silentone", hand "Soulbound Hammer" (20478). Gives "Dwarven Smiths Hammer" (20479).
    - event_trade NPC emote: makes a few marks on the hammer, and all the while you can hear a muffled cursing coming from the hammer head. 'Yes, it is an ancient dwarf's hammer. Interesting artifact. I've marked it to keep it stable while you retrieve something for me. You need to travel to the Plane of Sky and find a swirling sphere of color. Bring it and the hammer back to me.'
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 20478}))`
6. Kill airplane/"A Soul Carrier".
7. Spawns "an essence tamer" (npc:71071) via `airplane/an essence carrier#event_death_complete`.
8. Kill "an essence tamer" (NPC 71071) in `airplane` and loot "Swirling Sphere of Color" (20494).
9. erudnint/"Mairee Silentone", hand "Dwarven Smiths Hammer" (20479) + "Swirling Sphere of Color" (20494). Gives "Hammer of the Ancients" (20485).
    - event_trade NPC emote: holds the sphere and makes intricate marks and patterns on it, eventually turning the entire crystal clear. She rolls it across the hammer, raising a ringing sound in the room. 'There. Now take the hammer back to Kinlo. He'll know what to do from here. Good luck to you.'
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 20479,item2 = 20494}))`
10. kaladimb/"Kinlo Strongarm", hand "Hammer of the Ancients" (20485). Gives "Small bit of Mithril Ore" (20482).
    - event_item NPC emote: looks at the hammer and nods once before slamming the head against his anvil, and shattering the head. In a cloud of dust, another dwarf appears from the cloud and tosses you a hunk of metal. Kinlo stares in awe.
      - Event guard: `($faction <= 5)`
      - Event guard: `(plugin::check_handin(\%itemcount, 20485 => 1))`
11. kaladimb/"Kinlo Strongarm", hand "Small bit of Mithril Ore" (20482). Gives "Refined Mithril Blade" (20483).
    - event_item NPC say: Erm. Well, I ain't never worked with this stuff but here's what I got for ya. It ain't bad, pretty much like the one ye got there. I suppose ye should take the one the ancient made and show it ta yer friend.
      - Event guard: `($faction <= 5)`
      - Event guard: `(plugin::check_handin(\%itemcount, 20482 => 1))`
12. Loot "Shattered Emerald of Corruption" (20484) from "a hideous rat" (NPC 186166) in `hateplaneb`. Drop cache: 17.19% chance per kill.
13. northkarana/"Xanuusus", hand "Refined Mithril Blade" (20483) + "Shattered Emerald of Corruption" (20484). Gives "Earthcaller" (20488).
    - event_trade NPC emote: waves his hands over the gem of corruption and a wave of warm energy passes through the area. With care for such a huge creature, he melds the gem into the sword and seems to glow all over as he channels energy into the weapon. 'Thus is the link of hate broken between Innoruuk and the spirit of earth. Through your will has balance returned. Your deeds, your work for the good of all, will be remembered by anyone who walks beneath the canopy of a forest or roams the plains. Continue your vigil over nature's balance.'
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 20483,item2 = 20484}))`

## Epic 1.5

### "Heartwood Blade" (62627)

<a id="epic-item-62627"></a>

1. erudnext/"Lumi Stergnon", say "Hail".
    - Player: "hail"
      - NPC say: Peace and tranquility be with you. .  Are you a [new acolyte of peace] or are you [here to pay homage] to the child of tranquility?
      - Condition: `(e.message:findi("hail"))`
2. Buy "Planar Fletching Kit" (17762) from "Ellis Cloudchaser" (NPC 202076) in `poknowledge`. Base price: 1,000 copper.
3. Spawns "an ancient thought horror" (npc:164122) via `thedeep/ancient thought horror trap#enter`.
4. Kill "an ancient thought horror" (NPC 164122) in `thedeep` and loot "Thick Spinal Fluid" (40420).
5. Forage "Sickly Maiden's Hair" (62810) in `rathemtn`.
6. eastkarana/"Althele", hand "Sickly Maiden's Hair" (62810). Gives "Tuft of Sickly Maiden's Hair" (62811).
    - event_item NPC say: This plant has an illness that I have never sensed before.' Althele pauses in thought for a moment. 'You are a hunter, so I shall put your skills to work. First, take this to Corun in Surefall. He is an expert on animal illnesses. Then put your hunting skills to work and see if you can capture any animals that may have eaten this plant. Corun will want to see them to help him discover what the sickness is.
      - Event guard: `(plugin::check_handin(\%itemcount, 62810 => 1))`
7. qrg/"Corun Finisc", hand "Tuft of Sickly Maiden's Hair" (62811). Gives "Borrowed Medicine Bag" (62605) + "Magical Sample Vial" (62657).
    - event_trade NPC say: Well, this is certainly an unpleasant sight. If Althele sent you to me it must be because I've had a lot of experience with sick animals. If you can find me some animals that have become ill by eating this plant perhaps I can discover something about this disease. You must not kill these animals. It is never good to harm an animal if you do not need to. It is also important that the animal be alive when you take samples of their blood. If any animals have eaten this plant and become ill, you need to find a way to capture them and use your fletching kit and these vials to gather blood samples. Althele is rarely wrong about what she senses from Antonica. Be careful with that medicine bag, I borrowed it from a friend in Halas a while back. I'll need you to use it to store some samples as you capture the animals. Don't lose it, you don't want Lars angry with you!
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 62811}))`
8. eastkarana/"Althele", say "Hail". Sets `ranger_epic` to `1`.
    - Player: "hail"
      - NPC say: Hello, friend. Beautiful is what I would call such a day normally, but lately? I sense that something is [out of balance].
        - Reply guard: `($class eq "Ranger" && (plugin::check_hasitem($client, 20488) || plugin::check_hasitem($client, 62600)))`
      - Condition: `($text=~/hail/i)`
9. Spawns "an asteatotic highborn" (npc:109907) via `veksar/player#enter`.
10. Kill "an asteatotic highborn" (NPC 109907) in `veksar` and loot "Asteatotic Veksar Blood" (35100).
11. Spawns "a neuralgic huntress" (npc:120136) via `westwastes/player#enter`.
12. Kill "a neuralgic huntress" (NPC 120136) in `westwastes` and loot "Neuralgic Wyvern Blood" (72605).
13. Summon "Collapsible Fletching Kit" (17189) by casting "Unfold Fletching Kit".
14. Buy "Whittling Knife" (62608) from "Yoen Ormard" (NPC 279110) in `abysmal`. Base price: 50 copper.
15. Forage "Fallen Tree Branch" (62652) in `dranik` or `draniksscar`.
16. Combine in "Planar Fletching Kit" (17762): "Whittling Knife" (62608), "Fallen Tree Branch" (62652). Produces "Long Net Pole" (62607). Requires Fletching.
17. Spawns "a phase spider" (npc:123190) via `necropolis/an out of phase spider#event_combat`.
18. Kill "a phase spider" (NPC 123190) in `necropolis` and loot "Phase Spider Silk" (55303).
19. Forage "Pine Sap" (62650) in `jaggedpine` or `nedaria` or `qrg`.
20. Combine in "Planar Fletching Kit" (17762): "Phase Spider Silk" (55303), "Pine Sap" (62650). Produces "Phase Netting" (62651). Requires Fletching.
21. Combine in "Planar Fletching Kit" (17762): "Long Net Pole" (62607), "Phase Netting" (62651). Produces "Large Butterfly Net" (62646). Requires Fletching.
22. cazicthule/"A Sickly Mosquito", say "". Gives "Captured Mosquito" (62642).
23. Combine in "Collapsible Fletching Kit" (17189): "Magical Sample Vial" (62657), "Captured Mosquito" (62642). Produces "Sickly Mosquito Blood Sample" (62611). Requires Fletching.
24. sirens/"A Twitching Swordfish", say "". Gives "Captured Swordfish" (62643).
25. Combine in "Collapsible Fletching Kit" (17189): "Magical Sample Vial" (62657), "Captured Swordfish" (62643). Produces "Twitching Swordfish Blood Sample" (62612). Requires Fletching.
26. Buy "Hinge Mold" (12027) from "Frannie" (NPC 3020) in `qrg`. Base price: 10 copper.
27. Buy "Container Base Mold" (12062) from "Tislan" (NPC 10077) in `freporte`. Base price: 110 copper.
28. Buy "Container Lid Mold" (12069) from "Tislan" (NPC 10077) in `freporte`. Base price: 110 copper.
29. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
    - Player: "battle the undead"
      - NPC say: Then you shall venture to Toxxulia Forest. There has been an increase in skeleton sightings lately. I do not know their origin, but I believe that your efforts will reduce their numbers! Take this box. Return it to me when you have filled it with the bones of these undead creatures and combined it. May Quellious' light guide you.
      - Condition: `(e.message:findi("battle the undead"))`
      - Linked from "new acolyte of peace" (explicit prompt).
30. Loot "Useless Cloth Cap" (13894) from "a kobold scout" (NPC 38035) in `tox`. Drop cache: 20% chance per kill.
31. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
32. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). Requires Remove Traps.
33. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
    - event_trade NPC say: You have done well. Let it be known to all that you fight for the Rainkeeper. Go and continue the battle.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 13882}))`
34. Buy "Small Brick of Steel" (66168) from "Qaelin Hailstorm" (NPC 3042) in `qrg`. Base price: 5,890 copper.
35. qrg/"Qaelin Hailstorm", say "Need A Mark". Gives "Mark of Karana" (66172).
    - Player: "need a mark"
      - NPC say: Here you go, if you need another please let me know.
        - Reply guard: `(deity == 207)`
      - NPC say: How dare you state that you are something that you aren't! You are no follower of the Rainbringer!
        - Reply guard: ``
      - Condition: `(e.message:findi("need a mark"))`
      - Linked from "hail" (explicit prompt).
36. Combine in appropriate tradeskill container: "Hinge Mold" (12027), "Container Base Mold" (12062), "Container Lid Mold" (12069), "Water Flask" (13006), "Small Brick of Steel" (66168), "Mark of Karana" (66172). Produces "Surefall Fletching Kit" (66163). Requires Blacksmithing.
37. Spawns "A Dragorn flunky" (npc:301080) via `bloodfields/elite dragorn jekisia#event_hp`.
38. Kill "A Dragorn flunky" (NPC 301080) in `bloodfields` and loot "Broken Magnetized Collar" (72062).
39. Combine in appropriate tradeskill container: "Broken Magnetized Collar" (72062). Produces "Smithy Hammer" (10489). Requires Blacksmithing.
40. Forage "Golanda Nut" (62610) in `causeway` or `dranik` or `draniksscar` or `provinggrounds` or `riftseekers` or `wallofslaughter`.
41. Combine in "Surefall Fletching Kit" (66163): "Smithy Hammer" (10489), "Golanda Nut" (62610). Produces "Fibrous Rope" (62609). Requires Fletching.
42. Combine in "Surefall Fletching Kit" (66163): "Fibrous Rope" (62609). Produces "Eight-loop Lasso" (62648). Requires Fletching.
43. chardokb/"A Leprous Chokidai", say "". Gives "Captured Chokidai" (62645).
44. Combine in "Collapsible Fletching Kit" (17189): "Magical Sample Vial" (62657), "Captured Chokidai" (62645). Produces "Leprous Chokidai Blood Sample" (62614). Requires Fletching.
45. droga/"A Bloated Drogan Spider", say "". Gives "Captured Spider" (62644).
46. Combine in "Collapsible Fletching Kit" (17189): "Magical Sample Vial" (62657), "Captured Spider" (62644). Produces "Bloated Drogan Spider Blood Sample" (62613). Requires Fletching.
47. Combine in "Borrowed Medicine Bag" (62605): "Asteatotic Veksar Blood" (35100), "Neuralgic Wyvern Blood" (72605), "Sickly Mosquito Blood Sample" (62611), "Twitching Swordfish Blood Sample" (62612), "Leprous Chokidai Blood Sample" (62614), "Bloated Drogan Spider Blood Sample" (62613). Produces "Full Medicine Bag" (62616). Requires Remove Traps.
48. qrg/"Corun Finisc", hand "Full Medicine Bag" (62616). Gives "Corun's Notes" (62617).
    - event_trade NPC say: This is frightening. A disease that can affect mosquito and wyvern must be a truly horrible thing. I will examine these samples carefully and pass knowledge to others who are working to repair this. From what you've shown me I can tell that the disease affects both the mind and the skin. Others seek information about illnesses of the skin. I need you to uncover information about diseases of the mind. I know not where to find such information, but you are a seeker and a worthy ranger. Find someone, somewhere, that knows enough about disease that affects 'more advanced' creatures such as men. Learn about the diseases of the mind. I will seek among the folk of the glade and pine for assistance with a cure for the Maiden's Hair. Please do not give up the search, no matter how difficult. This is a terrible illness and we must stop it from spreading. Take a copy of my notes with you, they may be of use to someone with the right knowledge.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 62616}))`
49. freeportwest/"Shana Liskia", hand "Corun's Notes" (62617). Gives "Corun's Notes - annotated" (62654).
    - event_trade NPC say: Well, this certainly is an interesting puzzle. I see here that these creatures were infected in their spinal columns. I'll tell you that a part of my research involves the use of the fluids of the brain and spine. I suspect that further details might be unpleasant. I might be able to help you, but I'll need materials to work with. Gather fluids from the brain of the creature with the greatest mental power that you can find. I'll test it and see if it's strong enough and has the right properties. If I can duplicate what you saw in these infected creatures, perhaps I can help. Aslo, bring back those notes that Corun made, I'll need them as well.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 62617}))`
    - event_trade NPC emote: makes a few hasty scribbles in the margins of Corun's Notes and hands them back to you.
50. freeportwest/"Shana Liskia", hand "Thick Spinal Fluid" (40420) + "Corun's Notes - annotated" (62654). Gives "Mind Crystal" (62846).
    - event_trade NPC say: Perfect! Yes, this will work nicely. Shana looks through Corun's notes while gathering items from her stores. This should work. What I'm going to do is grow a crystal around this fluid and some of the key ingredients of the disease. The crystal will focus the power of the fluid and the elements of the disease will guide it. If this goes well, I should be able to create a crystal that will guide you to the disease. Shana places the gathered items into a violet-tinted container and casts a spell over them. A moment later she retrieves a crystal from the container. The crystal is clear except for a dark, murky coloration at the center. Take that crystal and see if you can locate any creatures with the disease. If you have any success, please return and let me know.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 40420,item2 = 62654}))`
51. eastkarana/"Tholris", say "You Are Diseased". Gives "Red Crystal" (62618).
    - Player: "you are diseased"
      - NPC emote: looks at you indignantly
        - Reply guard: `($saydisease==1)`
      - NPC emote: kicks dirt at your feet
        - Reply guard: `($saydisease==2)`
      - NPC emote: shakes his head. Then he catches a glimpse of the Mind Crystal and looks thoughtful for a moment. Then he reaches into his pocket and produces two unusual crystals and hands them to you.
        - Reply guard: `($saydisease==3)`
      - Condition: `(($text=~/you are diseased/i) && plugin::check_hasitem($client, 62846))`
52. freeportwest/"Shana Liskia", hand "Red Crystal" (62618) + "Violet Crystal" (62619). Gives "Letter to Corun" (62655).
    - event_trade NPC say: Ah, well, it seems as though the crystal was attuned to these other crystals. They must have come in contact with a rather large element of the disease, otherwise I just can't see how the Mind Crystal would have noticed them. These crystals were created by someone with more experience than I have in this area. I will examine them further and attempt to learn something from them. I can tell now, though, that they were probably created in a fashion similar to the one I used to create the Mind Crystal. Shana pulls out a piece of parchment and writes a note. She gives you the note and says, Take this note to Corun along with the Mind Crystal. He can use the crystal and my notes to seek out the plague in whatever fashion he thinks is best. I need to get to work investigating these new crystals.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 62618,item2 = 62619}))`
53. qrg/"Corun Finisc", hand "Mind Crystal" (62846) + "Letter to Corun" (62655). Gives "Red Dogwood Seed" (62844).
    - event_trade NPC emote: looks at the crystal for a moment; confusion, disgust and curiosity chasing each other across his tired face. After reading the letter, he looks up at you.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 62846,item2 = 62655}))`
    - event_trade NPC say: This crystal seems strange, but if you and this Shana believe that it will help, then I know just the person to put it to work.' Corun puts the note and the crystal into a pouch. He reaches into another pouch to retrieve something small and hands it to you. 'This seed was brought to us by a druid of great skill. It should provide the cure we seek, but we do not know the place or circumstances under which to plant it. We have agreed to leave it to you to find that place and that time. I urge you to hasten, we do not know how long it will be until the plague is released upon us in earnest. The only thing that I know is that there may be a link between those that created the disease and the Plane of Discord. A very tenuous link, but keep the seed with you at all times, you never know when you will need it. May the Mother smile on your effort.
54. natimbi/"Ranger 1 5", say "Hail". Gives "Senvial's Blessing" (62621).
    - NPC say: Thank you for freeing me, . I am not sure how it is that you broke the power that commanded me, but for that I am very grateful. The water spirit looks at you carefully before speaking again. I sense that you will need my aid in the future. To repay my debt to you I give you my blessing. This is no mean thing, it carries with it a portion of my own power. Mine is the cool rain and soft mist. I am the essence of morning dew and the lazy fog. I have no doubt that you will use it wisely. There are more of my kin enslaved by these beasts and others like them. You appear to have the power to rescue them as you have me. I am not a being of foresight or far-seeing, mine is the realm of small, gentle things, but even I can see that you are a being of portent. I am honored to have met you. I must return to my realm. I shall never forget this place and what it has made me do, nor shall I forget the one thing that freed me.
55. bloodfields/"Ranger 1 5", say "Hail". Gives "Grinbik's Blessing" (62622).
    - NPC say: shouts Aaaah! A deep rumbling voice flows along the ground. I thank you, . You have freed me from such torture! Imagine me, Grinbik the Fertile, forced to kill and destroy! I was created to nurture and protect! I must go back to my own home and begin again to be what I was ment to be. I am honored and grateful to you for saving me. I see that you carry a powerful seed, nearly a seedling with its desire to grow! As my first act upon regaining myself I must aid you. If you wish that seed to flourish, you must find the land here that remains fertile. It is a rare thing but I have seen it. Take with you my blessing. This is a portion of my own power and it will aid you and that seed. I also know that my cousin Senvial is a slave here somewhere. You will need his aid as well to achieve your goal. Deliver that seedling and our blessings into the fertile ground and it will grow very quickly indeed! Thank you again ! All present should praise you for your kind heart and warrior soul.
56. Combine recipe recipe:13412 to set `ranger_epic` to `3`.
57. jaggedpine/"Red Dogwood Treant", say "Hail". Gives "Red Dogwood Heartwood" (62623).
    - Player: "hail"
      - NPC emote: looks about for a moment. It peers at the sky and the earth for a while. It then looks down and says, We finally meet. Thank you for helping me to grow. I understand that I have been blessed by spirits of rain and earth and that is why I can speak to you and move. You have given me much, my friend. Now I would give something to you. The great treant gently pulls a small piece of wood from its bole. The wood is hard and dark. It then reaches down with one of its high branches and plucks a singular flower, smaller and of blue color that differs from the white of the others. The petals fall from the flower as he reaches out and hands you these two items. I have been with you and your people for a while. I know what you seek. That seed will grow the plant you need. The heartwood is for you. May it serve you well.
      - Condition: `(e.message:findi("hail") and treesize>=8 and qglobals["ranger_epic"] == "3")`
58. dranik/"Ranger 1 5", hand "Red Dogwood Heartwood" (62623). Gives "Wind-blessed Heartwood" (62626).
59. qrg/"Corun Finisc", hand "Spring Dogwood Seed" (62624). Gives "Block of Purest Silver" (62625).
    - event_trade NPC emote: look at the seed, perplexed for a moment. Then he suddenly goes into motion. He pulls a sheaf of papers from a backpack and riffles through them. He mutters to himself as he compares the seed to sketches in the notes. This is it! If we plant this seed and its seeds widely enough, it should protect and even cure the Maiden's Hair with its pollen! You've done it! Thank you! The Glade thanks you. You've saved many good and fair things from death. Corun looks crestfallen for a moment. I only wish I had something to give you to express our appreciation. From what you have told me I think this may help you. It is a rare metal, I hope you can find a worthy use for it.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 62624}))`
60. Combine in "Planar Fletching Kit" (17762): "Wind-blessed Heartwood" (62626), "Block of Purest Silver" (62625). Produces "Heartwood Blade" (62627). Requires Fletching.

## Epic 2.0

### "Aurora, the Heartwood Blade" (62649)

<a id="epic-item-62649"></a>

**Earlier reward routes required by this graph path:** ["Swiftwind" (20487)](#epic-item-20487), ["Earthcaller" (20488)](#epic-item-20488), ["Heartwood Blade" (62627)](#epic-item-62627).
Revisit those instructions if another copy of a consumed item is needed.

1. Loot "Crooked Cage" (32042) from "a Broken Skull bruiser" (NPC 226002) in `torgiran`. Drop cache: 9.9701% chance per kill.
2. Loot "Living Fragment of Fire" (28294) from "a jopal mystic" (NPC 217026) in `pofire`. Drop cache: 5.0414% chance per kill.
3. Loot "Living Fragment of Water" (28293) from "a triloun diviner" (NPC 216017) in `powater`. Drop cache: 8.3814% chance per kill.
4. Combine recipe recipe:13413 to set `ranger_epic` to `5`.
5. nedaria/"A Wayfarers Brotherhood Officer", say "Hail". Sets `ranger_epic` to `6`.
    - Player: "hail"
      - NPC say: Hello. I can tell that you are a great hunter and tracker. I wanted to pass on to you some information, act on it as you will. A group of adventurers stopped in here a while ago. They said that they had information about a particular member of the Muramite army, some general or something, that had enslaved some elemental spirits. They went looking for him but haven't returned. I would appreciate any information you can find out about them. For now I am going to have to assume that they have all been killed.
      - Condition: `(e.message:findi("hail") and qglobals["ranger_epic"] == "5")`
6. causeway/"Siflu", say "Adventurers". Gives "Heated Loadstone" (62628).
    - Player: "adventurers"
      - NPC say: There have been plenty of those, that's for sure. If you mean recently, then, I suppose I know the group you're talking about. They were hunting us, just as I suspect you are. I was sent to kill anyone that might be on our trail. They gave me a loadstone that I could use to find them again. Here, you take it; I'm getting out of here while I still can.
      - Condition: `(e.message:findi("adventurers") and qglobals["ranger_epic"] == "6")`
7. Spawns "a mangled muramite captain" (npc:300069) via `wallofslaughter/rng trap#enter`.
8. Kill "a mangled muramite captain" (NPC 300069) in `wallofslaughter` and loot "Spirit Manacles" (72340).
9. Combine in "Crooked Cage" (32042): "Earthcaller" (20488), "Swiftwind" (20487), "Living Fragment of Fire" (28294), "Living Fragment of Water" (28293), "Heated Loadstone" (62628), "Spirit Manacles" (72340). Produces "Spirit Cage" (62656). Requires Remove Traps.
10. Combine recipe recipe:19914 to set `ranger_epic` to `8`.
11. Spawns "Craftmaster Tieranu" (npc:334087) via `riftseekers/player#enter`.
12. Kill "Craftmaster Tieranu" (NPC 334087) in `riftseekers` and loot "Ring of Warmth" (11427).
13. Spawns "Herrian Warfrost" (npc:300057) via `wallofslaughter/player#enter`.
14. Kill "Herrian Warfrost" (NPC 300057) in `wallofslaughter` and loot "Hoarfrost Wand" (76999).
15. Combine in "Spirit Cage" (62656): "Ring of Warmth" (11427), "Hoarfrost Wand" (76999). Produces "Elemental Ice Spirit Cage" (62647). Requires Remove Traps.
16. global/"Global Player", say "Recipe:19908". Gives "Globe of Discordant Energy" (47100).
17. anguish/"Oshimai Spirit Of The High Air", hand "Elemental Ice Spirit Cage" (62647) + "Globe of Discordant Energy" (47100) + "Heartwood Blade" (62627). Gives "Aurora, the Heartwood Blade" (62649).
    - event_trade NPC message: You have gained 10 ability points!
      - Event guard: `(qglobals["ranger_epic"] == "8" and item_lib.check_turn_in(e.trade, {item1 = 62647,item2 = 47100,item3 = 62627}))`
