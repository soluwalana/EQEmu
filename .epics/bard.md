# Bard — Epic Quest Walkthrough

Generated directly from quest-graph item rewards. Unresolved dependencies are marked, not inferred.

## Epic 1.0

### "Singing Short Sword" (20542)

1. qey2hh1/"Konia Swiftfoot", say "Hail".
    - Player: "hail"
      - NPC say: Hello there, .  I am hosting a relay running contest.  Would you like to participate?
      - Condition: `(e.message:findi("hail"))`
2. qey2hh1/"Konia Swiftfoot", say "Ready". Gives "Torch of Misty" (20532).
    - Player: "ready"
      - NPC say: Here you go.  Run with this torch as fast as you can to the Misty Thicket and hand this torch off to Fajio Knejo.  He will tell you where to go from there.  Hurry!  You do not have much time!
      - Condition: `(e.message:findi("ready"))`
      - Linked from "like to participate" (explicit prompt).
3. misty/"Fajio Knejo", hand "Torch of Misty" (20532). Gives "Torch of Ro" (20533).
    - event_item NPC say: Run onward, my friend, to the far off Desert of Ro and give this torch to Andad Filla.
      - Event guard: `(plugin::check_handin(\%itemcount, 20532 => 1))`
4. southro/"Andad Filla", hand "Torch of Ro" (20533). Gives "Torch of Rathe" (20534).
    - event_trade NPC say: You still have a ways to go! Seek out Misty Tekcihta near the arena at Lake Rathe. Run like the wind!
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 20533}))`
5. lakerathe/"Misty Tekcihta", hand "Torch of Rathe" (20534). Gives "Proof of Speed" (20379).
    - event_item NPC emote: hands you a small ring.
      - Event guard: `(plugin::check_handin(\%itemcount, 20534 => 1))`
6. qey2hh1/"Konia Swiftfoot", hand "Proof of Speed" (20379). Gives "Maestro's Symphony Page 24 Top" (20376).
    - event_trade NPC say: Excellent!  You are quite a runner.  Here is half of the sheet music.  I decided to keep the other half because it has this wonderful signature.  I think it might be quite valuable.  It is probably worth as much as an instrument the great Mahlin used.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 20379}))`
7. southkarana/"Baenar Swiftsong", say "Doll". Gives "Solusek Mining Company Invoice" (20372).
    - Player: "doll"
      - NPC say: What's that you say? You wish to have the doll I was to give her? Whatever for? Bah! Nevermind me. I rant like an old woman sometimes. I should let her memory go but I would stop my heart from beating before I forget that child. Here, take this invoice. I have no further use for it. Give it to Marfen Binkdirple.
      - Condition: `(e.message:findi("doll"))`
      - Linked from "ghouls" (sequence only; unverified).
8. soldunga/"Marfen Binkdirple", hand "Solusek Mining Company Invoice" (20372). Gives "Mechanical Doll" (20370).
    - event_item NPC say: Ah! 'Bout time ye got yer lazy bones down here! I was beginnin' ta worry bout ya. Thought ye'd never pick the doll up. Me kin worked and toiled over this thing fer days. That Baenar was sure exact in every detail. For a special child, he said. Must be some child. He spent all he had and some he didn't. Still owes us a show! Anyway, I heard she passed away some time ago. Give the lad muh regards.
      - Event guard: `(plugin::check_handin(\%itemcount, 20372 => 1))`
9. unrest/"Serra", hand "Mechanical Doll" (20370). Gives "Note for Baenar" (20371).
    - event_trade NPC say: Oh! You have the dolly! Thank you! Thank you! Thank you! I can go home now. Please give this to my father, Baenar. He will understand when he gets it.' Serra begins to fade away. 'Bye bye!
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 20370}))`
10. southkarana/"Baenar Swiftsong", hand "Note for Baenar" (20371). Gives "Note to Maligar" (20368).
    - event_trade NPC say: A note from the child? How can that be! How could she know I was her father? Unless? Cyrah told her. Forgive me. Cyrah was the name of the woman to whom I was betrothed. Unfortunately her parents forbade her from marrying a lowly bard such as myself. Her father married her off to a young merchant in Qeynos named Maligar. She married him only out of respect to her father. Her heart was truly mine, at least, so she always said. When Serra was born, I visited them both often. She was like no other, so innocent and sweet. In those few years I watched her grow up to be more and more like her mother and I saw none of the father in her appearance. I do not like Maligar, but the least we can do is inform him of his child's death. I saw his caravan pass by not more than a day ago headed to Qeynos.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 20371}))`
11. qey2hh1/"Maligar", hand "Note to Maligar" (20368).
    - event_item NPC say: Hmmm. What's this? A note from that silly bard Baenar? I wasn't aware that those of his kind could write, much less read.' Maligar lets out a deep laugh. 'I see you do not share my sense of humor. Let's read it, shall we? Oh, no! She's dead? I knew that already, you fool. It was by my hand she died! Ooops! Did I let that slip out? Silly me. I guess I will have to kill you now!
      - Event guard: `(plugin::check_handin(\%itemcount, 20368 => 1))`
12. Spawns "Maligars Enraged Doppleganger" (npc:12173) after the hand-in.
13. Kill "Maligars Enraged Doppleganger" (NPC 12173) in `qey2hh1` and loot "Maligar's Head" (20367).
14. southkarana/"Baenar Swiftsong", hand "Maligar's Head" (20367). Gives "Mahlin's Mystical Bongos" (20366).
    - event_trade NPC say: That vile dog! I knew there was something not right with him, the way he stared at everyone with contempt! Even his own wife! I curse him! I curse him to stay upon the realm and deny him what he most desires! This is too much! I cannot play or write this day. The sadness overwhelms me. In honor of Serra, the daughter that was denied to me in spirit, I vow never to play this instrument again! It was her favorite and she listened to me play for hours on end. Here take it! Take it out of my sight! Leave me be with my grief and my loss.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 20367}))`
15. qey2hh1/"Konia Swiftfoot", hand "Mahlin's Mystical Bongos" (20366). Gives "Maestro's Symphony Page 24 Bottom" (20383).
    - event_trade NPC say: Mahlin's bongos!  Here, take the other half of the sheet music.  I can't really make out what the signature was, anyway.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 20366}))`
16. Loot "Chromodrac Gut" (20527) from "Eldrig the Old" (NPC 91085) in `skyfire`. Drop cache: 100% chance per kill.
17. Loot "Red Wurm Gut" (20528) from "Nezekezena" (NPC 87034) in `burningwood`. Drop cache: 80% chance per kill.
18. Loot "Onyx Drake Gut" (20529) from "Blackwing" (NPC 50323) in `rathemtn`. Drop cache: 100% chance per kill.
19. southkarana/"Kelkim Menkia", hand "Chromodrac Gut" (20527) + "Red Wurm Gut" (20528) + "Onyx Drake Gut" (20529). Gives "Maestro's Symphony Page 25" (20377).
    - event_trade NPC emote: snatches the gut strings from your hand and immediately begins to string her lute. 'This is wonderful, I will be able to play my lute again soon! Take this old sheet of music I found - I don't think I will have much use for it. My new desire is to bash gnoll heads in with my lute. Safe travels to you, .
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 20527,item2 = 20528,item3 = 20529}))`
20. Loot "Alluring Horn" (20530) from "Quag Maelstrom" (NPC 69093) in `oot`. Drop cache: 100% chance per kill.
21. butcher/"Vedico Windwisper", hand "Alluring Horn" (20530). Gives "Note to Forpar Fizfla" (20378).
    - event_trade NPC say: Where did you find this? I thought the cyclops took it. I am in your debt, . This horn has always been special to me.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 20530}))`
    - event_trade NPC emote: reaches into her pack and pulls out a note. 'Do you think you could deliver this to my gnome friend Forpar? I have not spoken to him in a while and unfortunatly I will be unable to make the trip to visit him. If you are looking to have an instrument made he is the man to ask.'
22. steamfont/"Forpar Fizfla", hand "Note to Forpar Fizfla" (20378). Gives "Forpar's Note to Himself" (20380).
    - event_item NPC say: So you know Vedico! How is the lass? If Vedico would give you the time of day, you must be something special. What can I do for you? I hope you have not come to have me make another [mystical instrument].
      - Event guard: `(plugin::check_handin(\%itemcount, 20378 => 1))`
23. Loot "Kedge Backbone" (20524) from "Phinigel Autropos" (NPC 64001) in `kedge`. Drop cache: 20% chance per kill.
24. Loot "Petrified Werewolf Skull" (20525) from "a Drolvarg warlord" (NPC 102103) in `karnor`. Drop cache: 35% chance per kill.
25. Loot "Amygdalan Tendril" (5520) from "Amygdalan warrior" (NPC 72015) in `fearplane`. Drop cache: 8.1441% chance per kill.
26. steamfont/"Forpar Fizfla", hand "Forpar's Note to Himself" (20380) + "Kedge Backbone" (20524) + "Petrified Werewolf Skull" (20525) + "Amygdalan Tendril" (5520). Gives "Mystical Lute Head" (20535).
    - event_item NPC say: Wow! I didn't think a $race like you would be able to gather all of those things.
      - Event guard: `(plugin::check_handin(\%itemcount, 20380 => 1, 20524 => 1, 20525 => 1, 5520 => 1))`
    - event_item NPC emote: rambles around and works with small tools for a good ten minutes before handing you a very fine looking lute head.
    - event_item NPC say: Now, do you want to gather the next pieces for me?
27. Loot "White Dragon Scales" (11602) from "Lady Vox" (NPC 73057) in `permafrost`. Drop cache: 42.8346% chance per kill.
28. Loot "Red Dragon Scales" (11622) from "Lord Nagafen" (NPC 32040) in `soldungb`. Drop cache: 36.408% chance per kill.
29. kaladimb/"Jeet", say "Collect The Gnome Profit". Gives "Scrubber Key" (12164).
    - Player: "collect the gnome profit"
      - NPC say: Take this key. Don't lose it!! You will need to use it on a metal rat called a scrubber. They are all over Ak'Anon. You must find the one that responds to the number, '628'. If it responds, use the key on it. It will hand over a bag with the 'gnome take'. Return it to me. Get moving!!
        - Reply guard: `($faction <= 4)`
      - NPC say: Don't take this personally, but I can't quite trust you with such matters. Maybe a few less Butcherblock bandits would prove your worth.
        - Reply guard: `($faction <= 5)`
      - NPC say: The word around the mines is that you are not to be trusted. You'd best leave before my dagger finds a new home in your back.
        - Reply guard: ``
      - Condition: `(($text=~/collect the gnome profit/i))`
      - Linked from "run to the gnome city" (explicit prompt).
30. akanon/"Clockwork Scrubber", hand "Scrubber Key" (12164). Gives "Gnome Take" (12167).
    - event_trade NPC emote: .wizz.click.628.
      - Event guard: `(miner628 == 1 and item_lib.check_turn_in(e.trade, {item1 = 12164}))`
31. kaladimb/"Jeet", hand "Gnome Take" (12167). Gives "Small Piece of Ore" (10500).
    - event_item NPC say: What is all this junk!! That blasted tin rat is supposed to be heisting expensive goods from rich gnomes - not all this garbage!! Here. This is your cut of this junk.
      - Event guard: `(($faction <= 4) && (plugin::check_handin(\%itemcount, 12167 => 1)))`
32. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
    - Player: "battle the undead"
      - NPC say: Then you shall venture to Toxxulia Forest. There has been an increase in skeleton sightings lately. I do not know their origin, but I believe that your efforts will reduce their numbers! Take this box. Return it to me when you have filled it with the bones of these undead creatures and combined it. May Quellious' light guide you.
      - Condition: `(e.message:findi("battle the undead"))`
      - Linked from "new acolyte of peace" (explicit prompt).
33. Loot "Useless Cloth Cap" (13894) from "a kobold scout" (NPC 38035) in `tox`. Drop cache: 20% chance per kill.
34. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
35. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). Requires Remove Traps.
36. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
    - event_trade NPC say: You have done well. Let it be known to all that you fight for the Rainkeeper. Go and continue the battle.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 13882}))`
37. Combine in appropriate tradeskill container: "Small Piece of Ore" (10500), "Water Flask" (13006). Produces "Metal Bits" (16905). Requires Blacksmithing.
38. steamfont/"Forpar Fizfla", hand "White Dragon Scales" (11602) + "Red Dragon Scales" (11622) + "Metal Bits" (16905). Gives "Mystical Lute Body" (20536).
    - event_item NPC say: Wooooooo! You are doing a wonderful job, $name. I wish I could go out and gather these things myself.' Forpar sits back down at his desk and pulls several very strange looking tools out. Eventually he looks up at you and says, 'The body is done! Only one more piece to go!
      - Event guard: `(plugin::check_handin(\%itemcount, 11602 => 1, 11622 => 1, 16905 => 1))`
39. Spawns "Trakanon" (npc:89181) via `sebilis/an undead bard#event_death_complete`.
40. Kill "Trakanon" (NPC 89181) in `sebilis` and loot "Undead Dragongut Strings" (20526).
41. steamfont/"Forpar Fizfla", hand "Mystical Lute Head" (20535) + "Mystical Lute Body" (20536) + "Undead Dragongut Strings" (20526). Gives "Mystical Lute" (20538).
    - event_item NPC say: Goodness! I can hardly contain myself! This will be my greatest creation ever!
      - Event guard: `(plugin::check_handin(\%itemcount, 20535 => 1, 20536 => 1, 20526 => 1))`
    - event_item NPC emote: sits down, slides the lute head into place and screws it together. After a few minutes, he begins to string the lute with the gut strings of the poison dragon. A wonderful sound fills the air as he strums the lute once and hands it to you.
    - event_item NPC say: I hope you find a good use for that! I bet you could play it from the mountaintops and the people below would hear you. Thank you, $name, for making my lifelong dream come true!
42. dreadlands/"Baldric Slezaf", hand "Maestro's Symphony Page 24 Top" (20376) + "Maestro's Symphony Page 24 Bottom" (20383) + "Maestro's Symphony Page 25" (20377) + "Mystical Lute" (20538). Gives "Singing Short Sword" (20542).
    - event_item NPC emote: looks shocked as you hand him the pages and the mystical lute. 'I will put on a symphony the likes of which the gods have never seen. Thank you so much, $name. Please take this sword as a token of my gratitude.
      - Event guard: `(plugin::check_handin(\%itemcount, 20376 => 1, 20383 => 1, 20377 => 1, 20538 => 1))`

## Epic 1.5

### "Prismatic Dragon Blade" (77631)

1. **Unresolved acquisition:** "Note from Metala" (77627) has no graph or catalog producer.
2. southkarana/"Vhalen Nostrolo", hand "Note from Metala" (77627). Gives "Vhalen's Necklace" (77629).
    - event_trade NPC say: No this can't be true! Metala must have been kidnapped and forced to sign this letter!  You must find her and save her, ! Please!  Take this necklace; it was a gift she gave me on our anniversary long ago.  Surely it will help her remember her true self and make her come to her senses.
      - Event guard: `(qglobals["bard15"] == "5" and item_lib.check_turn_in(e.trade, {item1= 77627}))`
3. potorment/"A Bruised Woman", hand "Vhalen's Necklace" (77629).
    - event_trade NPC emote: 's eyebrows shift into the shadow of a quizzical expression as you show her the necklace.  A flash of recognition crosses her face and she jerks back across the floor in horror.  A screeching wail tears through your mind 'You are a fool Vahlen!  You send these peasants to do your dirty work, you never were much for getting your hands dirty!  The path of pain is the only way to true power.  I will never turn from it!
      - Event guard: `qglobals["bard15"] == "5" and item_lib.check_turn_in(e.trade, {item1 = 77629})`
4. Spawns "Metala Von Korach" (npc:207084) after the hand-in.
5. Kill "Metala Von Korach" (NPC 207084) in `potorment` and loot "Rusted Bile Etched Blade" (77630).
6. **Unresolved acquisition:** "Crest of Rizlona" (77626) has no graph or catalog producer.
7. Loot "Dragorn Blood" (77639) from "a dragorn serf" (NPC 300018) in `wallofslaughter`. Drop cache: 9.5158% chance per kill.
8. **Unresolved acquisition:** "Enchanted Velium Bar" (22099) has no graph or catalog producer.
9. **Unresolved acquisition:** "Cloudy Diamond of Air" (29989) has no graph or catalog producer.
10. **Unresolved acquisition:** "Wind Dragon Crystal" (12783) has no graph or catalog producer.
11. Combine in appropriate tradeskill container: "Dragorn Blood" (77639), "Enchanted Velium Bar" (22099), "Cloudy Diamond of Air" (29989), "Wind Dragon Crystal" (12783). Produces "Wind Dragon Prism" (77618). Requires Jewelry Making.
12. **Unresolved acquisition:** "Red Diamond of Fire" (29986) has no graph or catalog producer.
13. **Unresolved acquisition:** "Fire Dragon Crystal" (12487) has no graph or catalog producer.
14. Combine in appropriate tradeskill container: "Dragorn Blood" (77639), "Enchanted Velium Bar" (22099), "Red Diamond of Fire" (29986), "Fire Dragon Crystal" (12487). Produces "Fire Dragon Prism" (77619). Requires Jewelry Making.
15. **Unresolved acquisition:** "Aqua Diamond of Water" (29987) has no graph or catalog producer.
16. **Unresolved acquisition:** "Ice Dragon Crystal" (12781) has no graph or catalog producer.
17. Combine in appropriate tradeskill container: "Dragorn Blood" (77639), "Enchanted Velium Bar" (22099), "Aqua Diamond of Water" (29987), "Ice Dragon Crystal" (12781). Produces "Water Dragon Prism" (77620). Requires Jewelry Making.
18. **Unresolved acquisition:** "Brown Diamond of Earth" (29988) has no graph or catalog producer.
19. **Unresolved acquisition:** "Earth Dragon Crystal" (12782) has no graph or catalog producer.
20. Combine in appropriate tradeskill container: "Dragorn Blood" (77639), "Enchanted Velium Bar" (22099), "Brown Diamond of Earth" (29988), "Earth Dragon Crystal" (12782). Produces "Earth Dragon Prism" (77621). Requires Jewelry Making.
21. **Unresolved acquisition:** "Green Diamond of Disease" (30118) has no graph or catalog producer.
22. Spawns "a swamp dragon" (npc:83249) via `swampofnohope/a dire leech#event_hp`.
23. Kill "a swamp dragon" (NPC 83249) in `swampofnohope` and loot "Swamp Dragon Crystal" (77614).
24. Combine in appropriate tradeskill container: "Dragorn Blood" (77639), "Enchanted Velium Bar" (22099), "Green Diamond of Disease" (30118), "Swamp Dragon Crystal" (77614). Produces "Swamp Dragon Prism" (77622). Requires Jewelry Making.
25. **Unresolved acquisition:** "Gray Diamond of Storms" (29991) has no graph or catalog producer.
26. Spawns "a plains dragon" (npc:13130) via `northkarana/a dire griffon#event_hp`.
27. Kill "a plains dragon" (NPC 13130) in `northkarana` and loot "Plains Dragon Crystal" (77615).
28. Combine in appropriate tradeskill container: "Dragorn Blood" (77639), "Enchanted Velium Bar" (22099), "Gray Diamond of Storms" (29991), "Plains Dragon Crystal" (77615). Produces "Plains Dragon Prism" (77623). Requires Jewelry Making.
29. **Unresolved acquisition:** "Yellow Diamond of Valor" (30489) has no graph or catalog producer.
30. Spawns "a forest dragon" (npc:181224) via `jaggedpine/a dire kodiak#event_hp`.
31. Kill "a forest dragon" (NPC 181224) in `jaggedpine` and loot "Forest Dragon Crystal" (77616).
32. Combine in appropriate tradeskill container: "Dragorn Blood" (77639), "Enchanted Velium Bar" (22099), "Yellow Diamond of Valor" (30489), "Forest Dragon Crystal" (77616). Produces "Forest Dragon Prism" (77624). Requires Jewelry Making.
33. **Unresolved acquisition:** "White Diamond of Justice" (29494) has no graph or catalog producer.
34. Spawns "a mountain dragon" (npc:100227) via `stonebrunt/a dire panda#event_hp`.
35. Kill "a mountain dragon" (NPC 100227) in `stonebrunt` and loot "Mountain Dragon Crystal" (77617).
36. Combine in appropriate tradeskill container: "Dragorn Blood" (77639), "Enchanted Velium Bar" (22099), "White Diamond of Justice" (29494), "Mountain Dragon Crystal" (77617). Produces "Mountain Dragon Prism" (77625). Requires Jewelry Making.
37. Combine in "Crest of Rizlona" (77626): "Wind Dragon Prism" (77618), "Fire Dragon Prism" (77619), "Water Dragon Prism" (77620), "Earth Dragon Prism" (77621), "Swamp Dragon Prism" (77622), "Plains Dragon Prism" (77623), "Forest Dragon Prism" (77624), "Mountain Dragon Prism" (77625). Produces "Draconic Prism" (77628). Requires Remove Traps.
38. Combine in "Rusted Bile Etched Blade" (77630): "Draconic Prism" (77628). Produces "Prismatic Dragon Blade" (77631). Requires Remove Traps.

## Epic 2.0

### "Blade of Vesagran" (77640)

1. Loot "Black Chaos Gauntlets" (77641) from "Stone Thrower" (NPC 303087) in `causeway`. Drop cache: 2.0088% chance per kill.
2. Loot "Black Chaos Boots" (77642) from "a dragorn darkwarrior" (NPC 300010) in `wallofslaughter`. Drop cache: 1.626% chance per kill.
3. Loot "Black Chaos Breastplate" (77643) from "a gelidran flamefreeze" (NPC 334016) in `riftseekers`. Drop cache: 4.4945% chance per kill.
4. global/"Global Player", say "Recipe:19908". Gives "Globe of Discordant Energy" (47100).
5. causeway/"Alkron Wyrmsong", hand "Black Chaos Gauntlets" (77641) + "Black Chaos Boots" (77642) + "Black Chaos Breastplate" (77643) + "Globe of Discordant Energy" (47100).
    - event_trade NPC emote:  nods slowly and places the armor on the ground at his feet with the discordant orb in the center.  'Now we shall see if our efforts are for our salvation or destruction.  He begins to mark the ground with Dragorn runes and recite an ancient Dragorn rite.  The armor begins to hum as the orb dissolves into a black pool on the ground.  Alkron draws back in terror. 'No! I was a fool to think I could destroy him! I have brought about the end of us all!'  The armor spins and crackles with energy as it flies from your hands and rises into the air.  The armor begins to grow as bolts of energy begin to snap between them.  A maniacal cackle fills the air as the armor forms into a vaguely humanoid shape.
      - Event guard: `qglobals["bard15"] == "6"`
      - Event guard: `item_lib.check_turn_in(e.trade, {item1 = 77641, item2 = 77642, item3 = 77643, item4 = 47100})`
    - event_trade NPC message: The blade in your hand begins to glow as the dark orb begins to burn your flesh.  You struggle to keep the orb from flying away.
6. Spawns "Oshiruk" (npc:303125) after the hand-in.
7. Kill "Oshiruk" (NPC 303125) in `causeway` and loot "Dragorn Essence" (77644).
8. wakening/"Lantaric-Dar", hand "Dark Orb" (77613). Gives "Dark Orb" (77613).
    - event_trade NPC say: It must be an object of considerable power to be able to imbue a mere mortal such as Vesthon with the power to control a dragon kin spirit.  This orb must be destroyed, but I know not how that might be done.  For now I entrust the orb to your care, and charge you with finding a way to destroy it.  You must not fail .  An artifact of that much evil potential must not be allowed to exist.
      - Event guard: `qglobals["bard15"] == "3" and item_lib.check_turn_in(e.trade, {item1 = 77613})`
9. **Unresolved acquisition:** "Note from Metala" (77627) has no graph or catalog producer.
10. southkarana/"Vhalen Nostrolo", hand "Note from Metala" (77627). Gives "Vhalen's Necklace" (77629).
    - event_trade NPC say: No this can't be true! Metala must have been kidnapped and forced to sign this letter!  You must find her and save her, ! Please!  Take this necklace; it was a gift she gave me on our anniversary long ago.  Surely it will help her remember her true self and make her come to her senses.
      - Event guard: `(qglobals["bard15"] == "5" and item_lib.check_turn_in(e.trade, {item1= 77627}))`
11. potorment/"A Bruised Woman", hand "Vhalen's Necklace" (77629).
    - event_trade NPC emote: 's eyebrows shift into the shadow of a quizzical expression as you show her the necklace.  A flash of recognition crosses her face and she jerks back across the floor in horror.  A screeching wail tears through your mind 'You are a fool Vahlen!  You send these peasants to do your dirty work, you never were much for getting your hands dirty!  The path of pain is the only way to true power.  I will never turn from it!
      - Event guard: `qglobals["bard15"] == "5" and item_lib.check_turn_in(e.trade, {item1 = 77629})`
12. Spawns "Metala Von Korach" (npc:207084) after the hand-in.
13. Kill "Metala Von Korach" (NPC 207084) in `potorment` and loot "Rusted Bile Etched Blade" (77630).
14. **Unresolved acquisition:** "Crest of Rizlona" (77626) has no graph or catalog producer.
15. Loot "Dragorn Blood" (77639) from "a dragorn serf" (NPC 300018) in `wallofslaughter`. Drop cache: 9.5158% chance per kill.
16. **Unresolved acquisition:** "Enchanted Velium Bar" (22099) has no graph or catalog producer.
17. **Unresolved acquisition:** "Cloudy Diamond of Air" (29989) has no graph or catalog producer.
18. **Unresolved acquisition:** "Wind Dragon Crystal" (12783) has no graph or catalog producer.
19. Combine in appropriate tradeskill container: "Dragorn Blood" (77639), "Enchanted Velium Bar" (22099), "Cloudy Diamond of Air" (29989), "Wind Dragon Crystal" (12783). Produces "Wind Dragon Prism" (77618). Requires Jewelry Making.
20. **Unresolved acquisition:** "Red Diamond of Fire" (29986) has no graph or catalog producer.
21. **Unresolved acquisition:** "Fire Dragon Crystal" (12487) has no graph or catalog producer.
22. Combine in appropriate tradeskill container: "Dragorn Blood" (77639), "Enchanted Velium Bar" (22099), "Red Diamond of Fire" (29986), "Fire Dragon Crystal" (12487). Produces "Fire Dragon Prism" (77619). Requires Jewelry Making.
23. **Unresolved acquisition:** "Aqua Diamond of Water" (29987) has no graph or catalog producer.
24. **Unresolved acquisition:** "Ice Dragon Crystal" (12781) has no graph or catalog producer.
25. Combine in appropriate tradeskill container: "Dragorn Blood" (77639), "Enchanted Velium Bar" (22099), "Aqua Diamond of Water" (29987), "Ice Dragon Crystal" (12781). Produces "Water Dragon Prism" (77620). Requires Jewelry Making.
26. **Unresolved acquisition:** "Brown Diamond of Earth" (29988) has no graph or catalog producer.
27. **Unresolved acquisition:** "Earth Dragon Crystal" (12782) has no graph or catalog producer.
28. Combine in appropriate tradeskill container: "Dragorn Blood" (77639), "Enchanted Velium Bar" (22099), "Brown Diamond of Earth" (29988), "Earth Dragon Crystal" (12782). Produces "Earth Dragon Prism" (77621). Requires Jewelry Making.
29. **Unresolved acquisition:** "Green Diamond of Disease" (30118) has no graph or catalog producer.
30. Spawns "a swamp dragon" (npc:83249) via `swampofnohope/a dire leech#event_hp`.
31. Kill "a swamp dragon" (NPC 83249) in `swampofnohope` and loot "Swamp Dragon Crystal" (77614).
32. Combine in appropriate tradeskill container: "Dragorn Blood" (77639), "Enchanted Velium Bar" (22099), "Green Diamond of Disease" (30118), "Swamp Dragon Crystal" (77614). Produces "Swamp Dragon Prism" (77622). Requires Jewelry Making.
33. **Unresolved acquisition:** "Gray Diamond of Storms" (29991) has no graph or catalog producer.
34. Spawns "a plains dragon" (npc:13130) via `northkarana/a dire griffon#event_hp`.
35. Kill "a plains dragon" (NPC 13130) in `northkarana` and loot "Plains Dragon Crystal" (77615).
36. Combine in appropriate tradeskill container: "Dragorn Blood" (77639), "Enchanted Velium Bar" (22099), "Gray Diamond of Storms" (29991), "Plains Dragon Crystal" (77615). Produces "Plains Dragon Prism" (77623). Requires Jewelry Making.
37. **Unresolved acquisition:** "Yellow Diamond of Valor" (30489) has no graph or catalog producer.
38. Spawns "a forest dragon" (npc:181224) via `jaggedpine/a dire kodiak#event_hp`.
39. Kill "a forest dragon" (NPC 181224) in `jaggedpine` and loot "Forest Dragon Crystal" (77616).
40. Combine in appropriate tradeskill container: "Dragorn Blood" (77639), "Enchanted Velium Bar" (22099), "Yellow Diamond of Valor" (30489), "Forest Dragon Crystal" (77616). Produces "Forest Dragon Prism" (77624). Requires Jewelry Making.
41. **Unresolved acquisition:** "White Diamond of Justice" (29494) has no graph or catalog producer.
42. Spawns "a mountain dragon" (npc:100227) via `stonebrunt/a dire panda#event_hp`.
43. Kill "a mountain dragon" (NPC 100227) in `stonebrunt` and loot "Mountain Dragon Crystal" (77617).
44. Combine in appropriate tradeskill container: "Dragorn Blood" (77639), "Enchanted Velium Bar" (22099), "White Diamond of Justice" (29494), "Mountain Dragon Crystal" (77617). Produces "Mountain Dragon Prism" (77625). Requires Jewelry Making.
45. Combine in "Crest of Rizlona" (77626): "Wind Dragon Prism" (77618), "Fire Dragon Prism" (77619), "Water Dragon Prism" (77620), "Earth Dragon Prism" (77621), "Swamp Dragon Prism" (77622), "Plains Dragon Prism" (77623), "Forest Dragon Prism" (77624), "Mountain Dragon Prism" (77625). Produces "Draconic Prism" (77628). Requires Remove Traps.
46. Combine in "Rusted Bile Etched Blade" (77630): "Draconic Prism" (77628). Produces "Prismatic Dragon Blade" (77631). Requires Remove Traps.
47. causeway/"Alkron Wyrmsong", hand "Dragorn Essence" (77644) + "Dark Orb" (77613) + "Prismatic Dragon Blade" (77631). Gives "Blade of Vesagran" (77640).
    - event_trade NPC message: You have gained 10 ability point(s)!
      - Event guard: `qglobals["bard20"] == "1"`
      - Event guard: `item_lib.check_turn_in(e.trade, {item1 = 77644, item2 = 77613, item3 = 77631})`
    - event_trade NPC emote:  takes the blade and the two orbs from you.  He thrusts the sword into the ground at his feet and takes an orb in either hand.  He begins to recite an ancient dragorn rite as the air fills with magic around you.  Energy begins to surge between the two orbs and eventually begin to strike the blade as well.  The roar of energy rises and culminates in a flash of light.  The two orbs disappear into thin air as your sword takes on a new glow of power.

**Unresolved graph dependencies:**
- Cycle while acquiring "Dark Orb" (77613)
