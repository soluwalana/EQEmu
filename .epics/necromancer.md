# Necromancer — Epic Quest Walkthrough

Generated directly from quest-graph item rewards. Unresolved dependencies are marked, not inferred.

## Epic 1.0

### "Scythe of the Shadowed Soul" (20544)

<a id="epic-item-20544"></a>

1. Loot "Silver Disc" (20938) from "an azarack" (NPC 71031) in `airplane`. Drop cache: 14.2857% chance per kill.
2. Loot "Spiroc Feathers" (20782) from "an avenging gazer" (NPC 71027) in `airplane`. Drop cache: 10.626% chance per kill.
3. Kill airplane/"A Soul Carrier".
4. Spawns "Keeper of Souls" (npc:71075) via `airplane/key master#timer:87`.
5. Kill "Keeper of Souls" (NPC 71075) in `airplane` and loot "Black Silk Cape" (20783).
6. airplane/"Jzil Gsix", hand "Silver Disc" (20938) + "Spiroc Feathers" (20782) + "Black Silk Cape" (20783). Gives "Cloak of Spiroc Feathers" (1278).
    - event_trade NPC say: Very good. Now take this and leave me.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 20938, item2 = 20782, item3 = 20783}))`
7. Loot "Eye of Innoruuk" (20656) from "Innoruuk" (NPC 76007) in `hateplane`. Drop cache: 40.7296% chance per kill.
8. Loot "Slime Blood of Cazic-Thule" (20655) from "Dread" (NPC 72000) in `fearplane`. Drop cache: 10.4954% chance per kill.
9. Kill lakerathe/"A Bone Golem".
10. Spawns "a tortured soul" (npc:51144) via `lakerathe/a failed apprentice#event_death_complete`.
11. Kill "a tortured soul" (NPC 51144) in `lakerathe` and loot "Symbol of Insanity" (20648).
12. timorous/"Drendico Metalbones", hand "Symbol of Insanity" (20648). Gives "Journal of Drendico" (18086).
    - event_item NPC emote: says, 'Seek, search, turn, twist! Kazen hopes to death master truly! Read out, read in between! Talk to the pretty clouds.' Drendico turns his back to you and throws a book over his shoulder. 'Bring back book! Bring back reagents three!!' He shouts as he mumbles some more gibberish.
      - Event guard: `(plugin::check_handin(\%itemcount, 20648 => 1))`
13. timorous/"Drendico Metalbones", hand "Cloak of Spiroc Feathers" (1278) + "Eye of Innoruuk" (20656) + "Slime Blood of Cazic-Thule" (20655) + "Journal of Drendico" (18086). Gives "Prepared Reagent Box" (20653).
    - event_item NPC emote: turns to you in amazement. 'You actually did it! These are the correct components! Kazen will be most pleased. I searched the planes for almost a year and could not find all the correct components.' Drendico fiddles with the components, puts them into a box and hands it to you. 'You must have access to an army, $name. Return the components to Kazen quickly!
      - Event guard: `(plugin::check_handin(\%itemcount, 1278 => 1, 20656 => 1, 20655 => 1, 18086 => 1))`
14. lakerathe/"Kazen Fecae", hand "Prepared Reagent Box" (20653). Gives "Tome of Instruction" (18087).
    - event_item NPC emote: stares through you at the horizon, pausing as he reaches into his robes. Kazen pulls out a scythe with a shimmering black blade that seems too large to have been hidden there. As quickly and gracefully as it was displayed to you, it is returned to the void inside Kazen's robes. 'It is a creation of Miragul which was looted from his lair under the ice. Take this tome, it will be your final task for me as an apprentice.'
      - Event guard: `(plugin::check_handin(\%itemcount, 20653 => 1))`
15. airplane/"Gkzzallk", hand "Tome of Instruction" (18087). Gives "Gkzzallk in a Box" (20652).
    - event_trade NPC emote: screams as he touches the book. His body shimmers as he shrinks smaller and smaller until it's no larger than an insect. The book shimmers, shifting into the shape of a small, black box. Gkzzallk holds on to the opening of the box as he is sucked backward into it. The tiny screams are finally silenced as the box top closes.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 18087}))`
16. lakerathe/"Kazen Fecae", hand "Gkzzallk in a Box" (20652). Gives "Scythe of the Shadowed Soul" (20544).
    - event_item NPC emote: grins wildly and his eyes flare a deep red. The scythe he promised you flies through the air and into your hand. 'Enjoy your toy, I have no more need of you as a servant.'
      - Event guard: `(plugin::check_handin(\%itemcount, 20652 => 1))`

## Epic 1.5

### "Soulwhisper" (62581)

<a id="epic-item-62581"></a>

1. natimbi/"Whiahdi", say "Hail".
    - Player: "hail"
      - NPC say: You speak to the dead? Not many have that talent. What is it you want from me, mortal?
      - Condition: `(plugin::check_hasitem($client,15784))`
      - Condition: `($text=~/hail/i)`
2. poknowledge/"Geboron", say "Hail". Gives "Note to Yuanda" (15809).
    - Player: "hail"
      - NPC say: 'Yes. . . $name is it? I have heard of you. I am Geboron, assistant to Kazen. It is most fortunate for you that you happened upon me. I have a task that is of the utmost importance and I believe I can trust you with it. There has been talk recently among my brethren of a most powerful staff that was recently discovered in the realm of discord and is now in the hands of a group of paladins. However my undead servants have informed me that the paladins were transporting the staff through the Karanas and suddenly disappeared without a trace. I want you to find my contact, Yuanda in West Karana and give her this note. It says you are working for me now. Find out what happened to those paladins and the staff! If you find out anything, talk to my assistant, Egonis in Lake Rathe.
      - Condition: `(($text=~/hail/i) && $class eq "Necromancer" && !defined($qglobals{NecroPre}) && !defined($qglobals{SoulWhisper}))`
3. qey2hh1/"Yuanda", hand "Note to Yuanda" (15809).
    - event_trade NPC say: So you are working for Geboron? Yes I have seen the paladins and the staff they were guarding. They passed through here just one day ago. From what I have been told, they were attacked by a pack of werewolves. All of the paladins were killed and one of the werewolves took the staff. If you want the staff you will need to find these werewolves. Oh, no! Here they come now! I am getting out of here!
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 15809}))`
4. Spawns "Shady Bandit" (npc:12185) via `qey2hh1/npc:12183#event_death_complete`.
5. Kill "Shady Bandit" (NPC 12185) in `qey2hh1` and loot "Contract of Sale" (15523).
6. lakerathe/"Egonis", hand "Contract of Sale" (15523).
    - event_item NPC say: So the foolish brigand sold the staff to Ronaiar, eh? Who is Ronaiar? He is an insane necromancer that makes his home somewhere near the lake. I had a feeling he would try to get his hands on the staff. That is why I came out here. I must inform Kazen of this turn of events and you must destroy that decrepit fool, Ronaiar. If you find the staff, give it to Geboron.
      - Event guard: `(($class eq "Necromancer") && plugin::check_handin(\%itemcount, 15523 => 1))`
7. Spawns "Man-eating Freshwater Shark" (npc:51158) via `lakerathe/worboli#event_signal`.
8. Kill "Man-eating Freshwater Shark" (NPC 51158) in `lakerathe` and loot "Piece of the Staff" (20612).
9. poknowledge/"Geboron", hand "Piece of the Staff" (20612).
    - event_item NPC say: I ask you to find a staff of great power and you bring me this??! A piece of the staff? You are an incompetent fool! Take this trash back and give it to Kazen so that he may punish you as he sees fit! Begone!
      - Event guard: `(plugin::check_handin(\%itemcount, 20612 => 1))`
      - Event guard: `(defined($qglobals{NecroPre}) && ($qglobals{NecroPre} == 1))`
    - event_item NPC say: What is this trash you give me?
      - Event guard: ``
10. lakerathe/"Kazen Fecae", hand "Piece of the Staff" (20612). Gives "Note to Biddliss" (9831).
    - event_item NPC say: Geboron has told me that you would be giving this piece of the staff to me. Do not fear. While I am not angry with you for failing to bring me the staff, I am not thoroughly pleased either. However, this piece could hold the key to discovering the staff's whereabouts. I wish to research this staff piece but first I need some special research tools. Take this note and travel to Steamfont. Find a gnome named Biddliss Sperandu and give him the note. When you obtain the research tools hand them to me.
      - Event guard: `(plugin::check_handin(\%itemcount, 20612 => 1))`
      - Event guard: `(defined($qglobals{NecroPre}) && ($qglobals{NecroPre} == 2))`
    - event_item NPC say: What is this? Why do you waste my time giving me junk? Take it back and begone!
      - Event guard: ``
11. steamfont/"Biddliss Sperandu", hand "Note to Biddliss" (9831). Gives "Gleaming Ore Satchel" (9579).
    - event_item NPC say: Kazen wants some research tools? That is fine. I want something from you first, however. Bring me four gleaming zraxthil ores and combine them in this satchel. Why do I want them? Why do you care? Bring them to me or you don't get your tools. Now scram!
      - Event guard: `(plugin::check_handin(\%itemcount, 9831 => 1))`
12. Loot "Old Waterlogged Lute" (59025) from "a shady treasure sorter" (NPC 225055) in `dulak`. Drop cache: 15.9687% chance per kill.
13. torgiran/"A Crazed Miner", hand "Old Waterlogged Lute" (59025).
    - event_item NPC emote: looks over the lute for a moment. He sets his fingers carefully over the strings, closes his eyes, and begins to play. A soft aria fills the stale air of the cavern with a strange warmth. Something inside you awakens that you had long forgotten. So long forgotten that you are unable to conjure a name for it from your memory. As the song ends the strange feeling leaves you as the darkness of the cavern closes in once more around you.
      - Event guard: `(plugin::check_handin(\%itemcount, 59025 => 1))`
    - event_item NPC say: Thank you my friends, for returning my senses to me. The dark dust of the mines had torn my sanity from me. Luckily my hands remembered the songs my mind had forgotten. Here, take this note to my son Jusean in Qeynos. He'll be able to transcribe a proper song for you from it. I must stay here and attempt to save the other miners from the dark insanity of the mines.
    - event_item NPC say: 'Tell Jusean. . .' Suddenly you hear a bowstring snap as an arrow sails through the air and strikes Heltin in the chest. He lies twitching before you for a moment before he stops and lies completely still.
14. Spawns "a crazed miner (KOS)" (npc:226021) after the hand-in.
15. Kill "a crazed miner (KOS)" (NPC 226021) in `torgiran` and loot "Gleaming Zraxthril Ore" (54006).
16. Combine in "Gleaming Ore Satchel" (9579): "Gleaming Zraxthril Ore" (54006). Produces "Sealed Ore Satchel" (27982). Requires Remove Traps.
17. steamfont/"Biddliss Sperandu", hand "Sealed Ore Satchel" (27982). Gives "Biddliss's Research Tools" (21799).
    - event_item NPC say: So you're not totally useless after all. Maybe there is a reason Kazen hasn't destroyed you yet. Take these tools and give my warmest regards to Master Kazen.
      - Event guard: `(plugin::check_handin(\%itemcount, 27982 => 1))`
18. lakerathe/"Kazen Fecae", hand "Biddliss's Research Tools" (21799). Gives "Drawing of Rune" (22691).
    - event_item NPC emote:  takes the tools from you. He opens the case and pulls out a small magnifying glass. It seems to faintly glow as he passes it over the surface of the staff piece.
      - Event guard: `(plugin::check_handin(\%itemcount, 21799 => 1))`
    - event_item NPC say: There appears to be a small rune etched in the wood.
    - event_item NPC emote:  takes out a piece of parchment and draws a picture of the rune.
    - event_item NPC say: I am not familiar with this rune. Take this drawing of the rune to Ruandia in the Plane of Knowledge. She is an expert on runes and should know what it means. From here on out I will want you to handle the research of this staff through my assistant Tebarin in the Plane of Knowledge. I am busy and do not wish to be disturbed further. Tebarin will communicate to me any progress you have made with helping to recover the staff.'
19. poknowledge/"Ruandia", hand "Drawing of Rune" (22691). Gives "Ruandia's Instructions" (10138).
    - event_item NPC emote: takes the drawing from you and studies it for a moment. Her face turns pale as a look of fear overcomes her. 'You must stop your quest for whatever this rune deals with. It will only lead to your demise. This rune has many meanings; the main meaning essentially being 'discord'. I am hesitant to tell you more about it, but I am sure Kazen would not be pleased.' Ruandia writes some directions onto the drawing. 'I am not responsible for the outcome of your quest. Keep that in mind.'
      - Event guard: `(plugin::check_handin(\%itemcount, 22691 => 1))`
20. poknowledge/"Tebarin", hand "Ruandia's Instructions" (10138). Gives "Intricately Carved Box" (16689).
    - event_item NPC say: Kazen informed me that you would be coming. Ruandia deciphered the rune for you? Good. That witch better be accurate or Kazen will have her head. I need you to find two balls of elemental clay and combine them in this box. Return them to me when you have them.
      - Event guard: `(plugin::check_handin(\%itemcount, 10138 => 1))`
21. Spawns "An Earthern Crusader" (npc:218027) via `poeartha/earth trap#event_combat`.
22. Kill "An Earthern Crusader" (NPC 218027) in `poeartha` and loot "Ball of Elemental Clay" (21720).
23. Combine in "Intricately Carved Box" (16689): "Ball of Elemental Clay" (21720). Produces "Sealed Intricately Carved Box" (27282). Requires Remove Traps.
24. poknowledge/"Tebarin", hand "Sealed Intricately Carved Box" (27282). Gives "Strange Smelling Oil" (16799).
    - event_item NPC emote: takes the clay from you and combines them into a large ball. He then flattens it out into a thin sheet and carefully carves a likeness of the rune into the clay sheet with a sharp stick. 'The directions say we will require an ancient tome of lost lore. I believe you can find one somewhere in The Hole. When you find the tome, combine it in the intricately carved box with the oil and then hand it to me. The oil will protect the tome for the ritual ahead.'
      - Event guard: `(plugin::check_handin(\%itemcount, 27282 => 1))`
25. Loot "Ancient Tome of Lost Lore" (62285) from "an old gargoyle" (NPC 39118) in `hole`. Drop cache: 77.381% chance per kill.
26. Combine in "Intricately Carved Box" (16689): "Strange Smelling Oil" (16799), "Ancient Tome of Lost Lore" (62285). Produces "Protected Tome" (16759). Requires Remove Traps.
27. poknowledge/"Tebarin", hand "Protected Tome" (16759). Gives "Brightly Glowing Tome" (9834).
    - event_item NPC emote: presses the sheet of clay into the tome and closes it. A red glow begins to engulf the tome. Tebarin opens the tome and you can see words slowly start to appear on the pages as if a ghost were writing on the pages. Tebarin studies the words within for several minutes. 'There is an explanation of the history of the staff. I have decided that our best bet of obtaining the staff is for me to attempt to summon it from its home plane of existence. I would advise you to prepare for the worst. This could end up being very dangerous. Hold the tome for a moment and try to attune yourself to its magics. Hand it to me when you are ready for me to begin the summoning.'
      - Event guard: `(plugin::check_handin(\%itemcount, 16759 => 1))`
28. poknowledge/"Tebarin", hand "Brightly Glowing Tome" (9834). Gives "Rune Covered Insert" (11406).
    - event_item NPC emote: holds up the book with both hands and begins to chant. After several minutes, a sudden flash blinds you. When you regain your vision a few seconds later, you are amazed to see the staff floating in the air before you. Before you or Tebarin are able to take the staff as your own, a booming voice echoes throughout the room, 'All who seek my staff will be destroyed!' An explosion of bright magic stuns you as a magical portal opens. Four heavily armored paladins step through the portal and grab the staff. 'Not if we destroy the staff first!' one of the paladins shouts. The paladins rush back into the portal with the staff.
      - Event guard: `(plugin::check_handin(\%itemcount, 9834 => 1))`
    - event_item NPC emote: tries to follow them into the portal but it disappears. 'This cannot be!' cries Tebarin. 'We must ensure this tome does not also fall into the hands of the paladins. The tome is our only hope of recovering the staff before the paladins destroy it. We must build a [special box] that will protect the tome. Take this rune-covered insert. You will use it to construct the box.'
29. Loot "Gnarled Wood" (12081) from "a gnarled treant" (NPC 204008) in `ponightmare`. Drop cache: 6% chance per kill.
30. Loot "Elaborate Hinge" (15835) from "a scrap collector" (NPC 206005) in `poinnovation`. Drop cache: 6% chance per kill.
31. Combine in appropriate tradeskill container: "Rune Covered Insert" (11406), "Gnarled Wood" (12081), "Elaborate Hinge" (15835). Produces "Glowing Box of Protection" (13620). Requires Blacksmithing.
32. poknowledge/"Tebarin", hand "Glowing Box of Protection" (13620). Gives "Paladin Headhunting Satchel" (11517).
    - event_item NPC say: This should do nicely. At least I hope so, for your sake. Now that the box is secure, I want revenge on the paladins who took the staff! Find all four of the paladins and take their heads! Once you have their heads, combine them in this sack and hand it to me. I will make sure they are reanimated and suffer for many, many years for what they have done. Now leave me. I must ponder the turn of events that have taken place here.
      - Event guard: `(plugin::check_handin(\%itemcount, 13620 => 1))`
33. Loot "Sir Gregon's Head" (11430) from "Sir Gregon Sulltor" (NPC 15192) in `eastkarana`. Drop cache: 100% chance per kill.
34. Loot "Sir Gerwin's Head" (14344) from "Sir Gerwin Thunderblade" (NPC 13125) in `northkarana`. Drop cache: 100% chance per kill.
35. Loot "Sir Telian's Head" (22892) from "Sir Telian Mottsworth" (NPC 14170) in `southkarana`. Drop cache: 100% chance per kill.
36. Loot "Sir Arlindo's Head" (26896) from "Sir Arlindo Goldheart" (NPC 12189) in `qey2hh1`. Drop cache: 100% chance per kill.
37. Combine in "Paladin Headhunting Satchel" (11517): "Sir Gregon's Head" (11430), "Sir Gerwin's Head" (14344), "Sir Telian's Head" (22892), "Sir Arlindo's Head" (26896). Produces "Full Paladin Headhunting Satchel" (24630). Requires Remove Traps.
38. poknowledge/"Tebarin", hand "Full Paladin Headhunting Satchel" (24630). Gives "Orb of Deathspeaking" (15784).
    - event_item NPC say: Your donation will please my masters greatly. I have a special reanimation spell reserved just for these do-gooders. Now you are to travel to Natimbi and find the paladin who has the staff. You might want to talk to the dead you come across as they often have valuable information. Take this orb to help enhance your natural abilities to communicate with the dead.
      - Event guard: `(plugin::check_handin(\%itemcount, 24630 => 1))`
39. natimbi/"Whiahdi", say "I Want The Staff". Sets `Soulwhisper` to `2`.
    - Player: "i want the staff"
      - NPC say: Yes. I did see a paladin with a staff. Before I give you any more information however. I wish for you to perform a task for me. I need you to travel to Barindu and find my most precious possessions from when I was once alive. A muramite in Barindu killed me and took all I owned. If you can get my earthly possessions back, I will help you in regards to the location of the paladin. Find my brother, Taiandao in Barindu. He is still among the living, but is a slave of the vile muramites. Ask him if he knows of the muramite that killed me.
      - Condition: `(plugin::check_hasitem($client,15784))`
      - Condition: `(($text=~/i want the staff/i) && (defined($qglobals{Soulwhisper}) && ($qglobals{Soulwhisper} == 1)))`
      - Linked from "hail" (sequence only; unverified).
40. barindu/"Viarglug", say "Hail".
    - Player: "hail"
      - NPC say: I wonder how much I could get for the tongue of a blithering fool..leave before I decide to find out for myself.
      - Condition: `(($text=~/hail/i) && (defined($qglobals{Soulwhisper}) && ($qglobals{Soulwhisper} == 2)))`
41. Spawns "Viarglug (Active)" (npc:283156) via `barindu/viarglug#hail`.
42. Kill "Viarglug (Active)" (NPC 283156) in `barindu` and loot "Whiahdi's Earthly Possessions" (11174).
43. natimbi/"Whiahdi", hand "Whiahdi's Earthly Possessions" (11174).
    - event_item NPC say: You found my possessions! I am most greatful. The paladin you seek did walk by here some time ago. I believe he was on his way to Qinimi. He had a curious staff with him that seemed to whisper dark tidings. That staff seemed to have a very evil presence about it. I would advise you to let the paladin destroy it. I have in my possession another staff of great [power]. I can tell you about if you give up your quest for the paladin and the dark staff. However if you wish to [locate the paladin] I will help you since you did help me.
      - Event guard: `((defined($qglobals{Soulwhisper}) && ($qglobals{Soulwhisper} == 2)) && plugin::check_handin(\%itemcount, 11174 => 1))`
44. natimbi/"Whiahdi", say "Power". Sets `Soulwhisper` to `4`.
    - Player: "power"
      - NPC say: I have come to know many spirits from other realms. They speak of a being known as Tarlang who resides in the Realm of Discord in a area known as the Nobles Causeway. He has wronged many of my kin and I wish to see him pay for what he has done. If you bring me his head. I will reward you with a weapon of great power. He believes himself to be indestructible, but he is not. In fact I think you have what it takes to destroy him.
      - Condition: `(plugin::check_hasitem($client,15784))`
      - Condition: `(($text=~/power/i) && (defined($qglobals{Soulwhisper}) && ($qglobals{Soulwhisper} == 3)))`
      - Linked from "locate the paladin" (explicit prompt).
45. causeway/"Tarlang", say "Hail".
    - Player: "hail"
      - NPC say: You dare speak to me? I do not talk to lesser creatures. Prepare for death!
      - Condition: `(($text=~/hail/i) && (defined($qglobals{Soulwhisper}) && ($qglobals{Soulwhisper} == 4)))`
46. Spawns "Tarlang (Active)" (npc:303083) via `causeway/tarlang#hail`.
47. Kill "Tarlang (Active)" (NPC 303083) in `causeway` and loot "Tarlang's Head" (55855).
48. natimbi/"Whiahdi", hand "Tarlang's Head" (55855). Gives "Soulwhisper" (62581).
    - event_item NPC say: Take this weapon for helping me. I regret giving away a weapon of such power, but having it near me was most unsettling. Do not ask how I obtained it.
      - Event guard: `((defined($qglobals{Soulwhisper}) && ($qglobals{Soulwhisper} == 3)) && plugin::check_handin(\%itemcount, 55855 => 1))`
    - event_item NPC message: You have gained 5 ability points!

## Epic 2.0

### "Deathwhisper" (64067)

<a id="epic-item-64067"></a>

**Earlier reward routes required by this graph path:** ["Soulwhisper" (62581)](#epic-item-62581).
Revisit those instructions if another copy of a consumed item is needed.

1. Spawns "arl" (npc:336242) via `dranik/discord fluctuation#event_proximity_say`.
2. Kill "arl" (NPC 336242) in `dranik` and loot "Staff Piece Number Two" (55940).
3. Kill "gor" (NPC 336243) in `dranik` and loot "Staff Piece Number Three" (55932).
4. global/"Global Player", say "Recipe:19908". Gives "Globe of Discordant Energy" (47100).
5. natimbi/"Whiahdi", hand "Staff Piece Number Two" (55940) + "Staff Piece Number Three" (55932) + "Globe of Discordant Energy" (47100) + "Soulwhisper" (62581). Gives "Deathwhisper" (64067).
    - event_item NPC say: It is against my better judgment to rebuild this staff, but I agreed to help you, if you helped me.
      - Event guard: `(plugin::check_handin(\%itemcount, 55940 => 1, 55932 => 1, 47100 => 1, 62581 => 1))`
    - event_item NPC emote: takes the staff pieces from you and sets them down on the ground. She waves her ghostly hands over the pieces and they begin to glow. A bright, orange flame engulfs the pieces as they begin to join, forming the staff. A bone-chilling shriek fills your ears. You look down to see the staff fully formed. 'Take the staff and leave. I have done something that I should not have done this day.'
    - event_item NPC message: You have gained 10 ability points!
