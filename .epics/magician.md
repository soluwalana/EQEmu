# Magician — Epic Quest Walkthrough

Generated directly from quest-graph item rewards. Unresolved dependencies are marked, not inferred.

## Epic 1.0

### "Orb of Mastery" (28034)

<a id="epic-item-28034"></a>

1. firiona/"Tiblner Milnik", say "Hail".
    - Player: "hail"
      - NPC say: Huh? What? Oh, you speak so fast, it took me a moment. I have become used to the slow and stately conversation the Earth holds, where a thought can span aeons. I am the Master of Earth, you know. Though I'm usually too humble to say this, that makes me the most powerful mortal in Norrath, as everyone knows that Earth is the only REAL Element, all else must give way before its power. Water is absorbed by it, Air is ignored by it, and Fire is contained in it. But you know all these things, I am sure. Are you interested in obtaining the Element of Earth? I know Magi'kot was, but we know what happened to him, don't we?
      - Condition: `($text=~/hail/i)`
2. Loot "Staff of Elemental Mastery: Earth" (11567) from "Innoruuk" (NPC 76007) in `hateplane`. Drop cache: 19.5643% chance per kill.
3. Loot "Dirt of Underfoot" (28042) from "Slixin Klex" (NPC 87047) in `burningwood`. Drop cache: 35% chance per kill.
4. Spawns "Rathyl reincarnate" (npc:44104) via `najena/rathyl#event_death_complete`.
5. Kill "Rathyl reincarnate" (NPC 44104) in `najena` and loot "Broom" (16544).
6. Loot "Cyclops Toes" (16543) from "a cyclops" (NPC 12197) in `qey2hh1`. Drop cache: 100% chance per kill.
7. Loot "Griffon Feathers" (16538) from "Callowwing" (NPC 13115) in `northkarana`. Drop cache: 34% chance per kill.
8. Spawns "A parasitic murkglider" (npc:303121) via `causeway/withering murkglider#event_hp`.
9. Kill "A parasitic murkglider" (NPC 303121) in `causeway` and loot "Star Ruby" (10032).
10. soltemple/"Vira", hand "Broom" (16544) + "Cyclops Toes" (16543) + "Griffon Feathers" (16538) + "Star Ruby" (10032). Gives "Broom of Trilon" (6360).
    - event_item NPC say: All of the components to make the infamous broom of Trilon! Well done, adventurer. As you have proven yourself worthy, I grant you this broom.
      - Event guard: `(quest::handin({16544 => 1, 16543 => 1, 16538 => 1, 10032 => 1}))`
11. Spawns "The Broodqueen" (npc:337254) via `broodlands/brood drone#event_death_complete`.
12. Kill "The Broodqueen" (NPC 337254) in `broodlands` and loot "Ruby" (10035).
13. Loot "Gargoyle Eye" (10014) from "Stishovite" (NPC 93142) in `overthere`. Drop cache: 46.667% chance per kill.
14. Loot "Shovel" (16545) from "Tiplo the Gardener" (NPC 150044) in `shadowhaven`. Drop cache: 25% chance per kill.
15. Loot "Hill Giant Toes" (16539) from "tainted hill giant" (NPC 50304) in `rathemtn`. Drop cache: 55% chance per kill.
16. soltemple/"Vira", hand "Ruby" (10035) + "Gargoyle Eye" (10014) + "Shovel" (16545) + "Hill Giant Toes" (16539). Gives "Shovel of Ponz" (6361).
    - event_item NPC say: Each of the four items needed to construct the famed Shovel of Ponz! Very well. As you have displayed ingenuity, I grant you this shovel.
      - Event guard: `(quest::handin({10035 => 1, 10014 => 1, 16545 => 1, 16539 => 1}))`
17. firiona/"Tiblner Milnik", hand "Staff of Elemental Mastery: Earth" (11567) + "Dirt of Underfoot" (28042) + "Broom of Trilon" (6360) + "Shovel of Ponz" (6361). Gives "Element of Earth" (28032).
    - event_item NPC say: Take this Element and keep it with you. I wish you the best in your journey, but I must ask you to leave me now. This frantic pace you set makes me nervous.
      - Event guard: `(plugin::check_handin(\%itemcount, 11567 => 1, 28042 => 1, 6360 => 1, 6361 => 1))`
18. Loot "Torn Page of Magi`kot pg. 1" (28000) from "dread wolf" (NPC 20280) in `kithicor`. Drop cache: 50% chance per kill.
19. Loot "Torn Page of Magi`kot pg. 2" (28001) from "a tentacle terror" (NPC 63043) in `unrest`. Drop cache: 90% chance per kill.
20. Loot "Torn Page of Magi`kot pg. 3" (28002) from "a bloodthirsty ghoul" (NPC 66137) in `gukbottom`. Drop cache: 91% chance per kill.
21. commonlands/"Jahsohn Aksot", hand "Torn Page of Magi`kot pg. 1" (28000) + "Torn Page of Magi`kot pg. 2" (28001) + "Torn Page of Magi`kot pg. 3" (28002). Gives "Words of Magi`kot" (28003).
    - event_item NPC say: Rykas may have been right about you, $name. Now, go find Walnan. Walnan was apprenticed to a very powerful Mage. After her apprenticeship was complete, she wished to begin teaching other beings of Norrath. Even those who knew nothing of the art! I do not believe she was successful, though. Seek her out to further your tale. Good luck in your journeys, $name!
      - Event guard: `(plugin::check_handin(\%itemcount, 28000 => 1, 28001 => 1, 28002 => 1))`
22. Kill "Rathyl reincarnate" (NPC 44104) in `najena` and loot "Torn Page of Mastery Fire" (28027).
23. Kill "Rathyl reincarnate" (NPC 44104) in `najena` and loot "Torn Page of Mastery Wind" (28028).
24. Kill "Rathyl reincarnate" (NPC 44104) in `najena` and loot "Torn Page of Mastery Earth" (28029).
25. Kill "Rathyl reincarnate" (NPC 44104) in `najena` and loot "Torn Page of Mastery Water" (28030).
26. najena/"Akksstaff", hand "Torn Page of Mastery Fire" (28027) + "Torn Page of Mastery Wind" (28028) + "Torn Page of Mastery Earth" (28029) + "Torn Page of Mastery Water" (28030). Gives "Words of Mastery" (28004).
27. Loot "Power of Fire" (28036) from "lava elemental" (NPC 31143) in `soldunga`. Drop cache: 28% chance per kill.
28. Loot "Power of Wind" (28037) from "a gypsy dancer" (NPC 59144) in `mistmoore`. Drop cache: 100% chance per kill.
29. Loot "Power of Earth" (28038) from "a faerie guard" (NPC 54041) in `gfaydark`. Drop cache: 13.903% chance per kill.
30. Loot "Power of Water" (28039) from "gorged ravener" (NPC 88038) in `kaesora`. Drop cache: 100% chance per kill.
31. butcher/"Walnan", hand "Power of Fire" (28036) + "Power of Wind" (28037) + "Power of Earth" (28038) + "Power of Water" (28039). Gives "Power of the Elements" (28031).
    - event_trade NPC say: The arcane art of Summoning is derived from the power of the elements which surround us. Continue your journey across the Ocean of Tears. In a dark fortress, you should find Akksstaf lurking about. Be wary, but tell him that you seek Magi'kot. Hurry now , you do not wish to miss the ship!
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 28036, item2 = 28037, item3 = 28038, item4 = 28039}))`
32. lakerathe/"Rykas", hand "Words of Magi`kot" (28003) + "Words of Mastery" (28004) + "Power of the Elements" (28031). Gives "Power of the Orb" (18958).
    - event_item NPC say: I see that you have completed the quest I laid before you. That speaks well of your dedication, yet you do not realize your journey has just begun. Study this tome.
      - Event guard: `(plugin::check_handin(\%itemcount, 28003 => 1, 28004 => 1, 28031 => 1))`
33. Kill citymist/"90000".
34. Spawns "Neh'Ashir" (npc:90184) via `citymist/90000#event_death_complete`.
35. Kill "Neh'Ashir" (NPC 90184) in `citymist` and loot "Torch of the Elements" (28007).
36. Loot "Blazing Wand" (10376) from "Undertow" (NPC 64087) in `kedge`. Drop cache: 70% chance per kill.
37. Loot "Burning Embers" (28008) from "Phurzikon" (NPC 87148) in `burningwood`. Drop cache: 13% chance per kill.
38. skyfire/"Jennus Lyklobar", hand "Power of the Orb" (18958) + "Torch of the Elements" (28007) + "Blazing Wand" (10376) + "Burning Embers" (28008). Gives "Element of Fire" (28009).
    - event_item NPC say: I see that you are well versed in the ways of Fire. Indeed, if you are as adept in the other, lesser elements, you may just seize the Orb of Mastery after all, and avoid Magi'kot's fate. Take this element, and guard it well, for more trials are to come, I assure you. Succeed and you shall be remembered always! Oh, and $name? Watch out for the puddles! HAHAHAHAHAHA!
      - Event guard: `(plugin::check_handin(\%itemcount, 18958 => 1, 28007 => 1, 10376 => 1, 28008 => 1))`
39. Loot "Staff of Elemental Mastery: Water" (11569) from "Phinigel Autropos" (NPC 64001) in `kedge`. Drop cache: 27.1049% chance per kill.
40. Loot "Tears of Erollisi" (28040) from "Captain Rottgrime" (NPC 93085) in `overthere`. Drop cache: 100% chance per kill.
41. Loot "Rain of Karana" (28041) from "Tarbul Earthstrider" (NPC 15171) in `eastkarana`. Drop cache: 100% chance per kill.
42. cauldron/"Jinalis Andir", hand "Staff of Elemental Mastery: Water" (11569) + "Tears of Erollisi" (28040) + "Rain of Karana" (28041). Gives "Element of Water" (28006).
    - event_trade NPC say: You have the control needed in order to manipulate the water which surrounds us. Take this Element and guard it well, you will need it in the times to come.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 11569, item2 = 28040, item3 = 28041}))`
43. Loot "Crown of Elemental Mastery" (20764) from "a windrider drake" (NPC 71002) in `airplane`. Drop cache: 10.8633% chance per kill.
44. Loot "Elemental Binder" (28043) from "an elemental monstrosity" (NPC 39004) in `hole`. Drop cache: 4.9583% chance per kill.
45. Spawns "Quillmane" (npc:14139) via `southkarana/#a lioness#event_death_complete`.
46. Kill "Quillmane" (NPC 14139) in `southkarana` and loot "Pegasus Feather Cloak" (2463).
47. airplane/"Kihun Solstin", hand "Crown of Elemental Mastery" (20764) + "Elemental Binder" (28043) + "Pegasus Feather Cloak" (2463). Gives "Element of Wind" (28033).
    - event_trade NPC say: If you have obtained the other, lesser Elements, go speak with The Master of Elements, who is now waiting for you. I wish you luck. If you have not completed all the tasks set for you, let me know, and I shall let you see the Master.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 20764, item2 = 28043, item3 = 2463}))`
48. airplane/"Master Of Elements", hand "Element of Earth" (28032) + "Element of Fire" (28009) + "Element of Water" (28006) + "Element of Wind" (28033). Gives "Spell: Summon Orb" (19436).
    - event_trade NPC say: You... are.. balanced... and.. powerful.. for.. a.. mortal...  ..... . More.. so.. than.... Magi'kot. But.... you.. are.. not.. yet.. ready.. to.. transcend.. transcend... this.. mortal.. coil. Take.. take.. seize.. this.. Orb... for.. you.. are.. worthy.. of.. reward.. and.. with... the.. aid.. of... the... balance.. balance.. contained.. within.. the.. Orb.. you.. may.. yet.. reach.. the... ultimate... Mastery.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 28032, item2 = 28009, item3 = 28006, item4 = 28033}))`
49. Learn "Spell: Summon Orb" (19436) and cast "Summon Orb" to summon "Orb of Mastery" (28034).

## Epic 1.5

### "Staff of Elemental Essence" (19092)

<a id="epic-item-19092"></a>

1. najena/"Akksstaff", say "Hail".
    - Player: "hail"
      - NPC say: How is this possible? I cannot be defeated. Spare my life and I will tell you the truth of Magi'kot's [demise].
      - Condition: `(qglobals["ask_minion_dead"] ~= nil and e.message:findi("hail"))`
2. Loot "Journal of Magus Tvish" (15639) from "Danvi`s Corpse" (NPC 179132) in `akheva`. Drop cache: 100% chance per kill.
3. poknowledge/"Bantil Io`Tuv", hand "Journal of Magus Tvish" (15639).
    - event_trade NPC emote: focuses for a minute, his hands glow with power. He then blows softly and the shadows melt from the Tome. As he opens it a small note falls to the floor. What is this? it appears to be some sort of correspondence. Hmm, interesting, it seems the next tome was given to a gnome, he set sail somewhere, but has not been heard from in quite some time. You will have to find him, he was supposed to wait for [Danvi] so he could take the tome
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 15639}))`
4. westwastes/"A Lost Tomekeeper", say "Violet Roses". Gives "Tome of Primal Fires" (15769).
    - Player: "violet roses"
      - NPC say: Oh? Yes. The tunips blow clockwise, or something or other. Here you go. Stay diligent. The enemy may be anyone.
      - Condition: `(e.message:findi("Violet Roses") and qglobals["mage_epic"] == "2" )`
5. poknowledge/"Bantil Io`Tuv", hand "Tome of Primal Fires" (15769).
    - event_trade NPC emote: quickly thumbs through the book. You can see the excitement growing on his face. 'This is incredible. I can see why Magi'Kot was able to learn so much from these tomes. There are just three more that we need to find, and we will be able to [ascend beyond] Magi'Kot's greatest dreams.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 15769}))`
6. Collect ground spawn "Book of Bindings and Incantations" (15772) in `charasis`.
7. poknowledge/"Bantil Io`Tuv", hand "Book of Bindings and Incantations" (15772).
    - event_trade NPC say: Ahh great, thank you. There are some interesting notes in these books. I suspect soon we should be able to find who is responsible for the disappearance in the first place.
      - Event guard: `(qglobals["mage_epic"] == "3" and item_lib.check_turn_in(e.trade, {item1 = 15772}) )`
8. Loot "Codex of Ice and Ether" (15775) from "Grigor Rojha" (NPC 164121) in `thedeep`. Drop cache: 100% chance per kill.
9. poknowledge/"Bantil Io`Tuv", hand "Codex of Ice and Ether" (15775).
    - event_trade NPC say: Oh my. Oh this is most disturbing news. It appears that one of Magi'Kot's apprentices was responsible for the theft of these books. This may not be the end of the story. Magi'Kot had four apprentices. Jahson Aksot, Akksstaff, Walnan and myself. There are notes in some of these letters that no one but one of his apprentices could have known. Speak to the others please, but be discreet, I sense something much larger at work here, return to me with anything you find.
      - Event guard: `(qglobals["mage_epic"] == "4" and item_lib.check_turn_in(e.trade, {item1 = 15775}) )`
10. Spawns "Akksstaff`s Minion" (npc:44108) via `najena/akksstaff#bantil sent me`.
11. najena/"Akksstaff", say "Demise". Gives "Sentience of Elements" (15778).
    - Player: "demise"
      - NPC say: I am the last Council Member of the Order of the Elemental Shadows. For Centuries, we protected the true secrets behind elemental mastery, but our sect dies here with me. I chose to sit at Magi'kot's side and watch his progress, he showed more promise than anyone since Tvish. When I learned he was to receive the Orb of Mastery, I sabotaged his spell. The flaw was not his, but now people have succeeded where he failed. It doesn't matter, even with the power of the Orb and the knowledge in these tomes, Bantil will never unlock the full power of elemental mastery. You are only helping him to meet the same fate as Magi'Kot.' He then hands you the book and fades into the shadows.
      - Condition: `(qglobals["ask_minion_dead"] ~= nil and e.message:findi("demise"))`
      - Linked from "hail" (explicit prompt).
12. poknowledge/"Bantil Io`Tuv", hand "Sentience of Elements" (15778).
    - event_trade NPC say: Akksstaff was responsible for our teacher's death? That is truly sad news. I knew he was devious, but I never suspected this type of betrayal.' Bantil takes a deep breath as he regains his composure, and he starts to browse through the book. 'This is truly amazing. I don't think Magi'Kot ever had access to this... No, of course he didn't. He never would have believed the Orb of Mastery was the pinnacle of [power] if that was the case.
      - Event guard: `(qglobals["mage_epic"] == "5" and item_lib.check_turn_in(e.trade, {item1 = 15778}) )`
13. potranquility/"Jurmak The Undertow", say "Elemental Essences". Sets `mage_epic_water1` to `1`.
    - Player: "elemental essences"
      - NPC say: Oh? The Elemental Essence of water? That is what you mean, yes? Consider yourself fortunate, I know the location of the Essence. It has spent quite some time living as a minor god to the othmir.
      - Condition: `(($text=~/elemental essences/i) && defined($qglobals{mage_epic}) && ($qglobals{mage_epic}==6))`
      - Linked from "hail" (sequence only; unverified).
14. Loot "Ice Burrower Meat" (19022) from "an ice burrower" (NPC 120010) in `westwastes`. Drop cache: 31.0425% chance per kill.
15. cobaltscar/"High Priest Margle", hand "Ice Burrower Meat" (19022).
    - event_trade NPC say: Tiknonmanin awaits your challenge.
      - Event guard: `(qglobals["mage_epic_water1"] == "1" and item_lib.check_turn_in(e.trade, {item1 = 19022, item2 = 19022, item3 = 19022, item4 = 19022}))`
16. Spawns "Tiknonmanin" (npc:117094) after the hand-in.
17. Kill "Tiknonmanin" (NPC 117094) in `cobaltscar` and loot "Elemental Essence of Water" (19086).
18. Spawns "Elemental Essence of Fire" (npc:214127) via `potactics/gnaap guinders#event_waypoint_arrive`.
19. Kill "Elemental Essence of Fire" (NPC 214127) in `potactics` and loot "Elemental Essence of Fire" (16807).
20. potranquility/"Sarhya The Dawnbreeze", say "Elemental Essences". Sets `mage_epic_air1` to `1`.
    - Player: "elemental essences"
      - NPC say: You seek the elemental essences? It has been a very long time since I've heard them spoke of. I am afraid I cannot be of much help, except to tell you it often enjoys to whistle through valleys and canyons. I fear it may not even reside in this realm any longer.
      - Condition: `(($text=~/elemental essences/i) && defined($qglobals{mage_epic}) && ($qglobals{mage_epic}==6))`
      - Linked from "plane of air" (sequence only; unverified).
21. Spawns "Elemental Essence of Air" (npc:303100) via `causeway/player#enter`.
22. Kill "Elemental Essence of Air" (NPC 303100) in `causeway` and loot "Elemental Essence of Air" (16773).
23. potranquility/"Taq`Aal Emeraldshard", say "Elemental Essences". Sets `mage_epic_earth1` to `1`.
24. Spawns "Elemental Essence of Earth" (npc:169127) via `letalis/player#enter`.
25. Kill "Elemental Essence of Earth" (NPC 169127) in `letalis` and loot "Elemental Essence of Earth" (19087).
26. poknowledge/"Bantil Io`Tuv", hand "Elemental Essence of Water" (19086) + "Elemental Essence of Fire" (16807) + "Elemental Essence of Air" (16773) + "Elemental Essence of Earth" (19087). Gives "Staff of Elemental Essence" (19092).
    - event_trade NPC say: Very well done! You have accomplished more than Magi'Kot could have ever imagined.' He then reads a passage from one of the books. The elemental essences begin to glow and take shape. You are blinded for a moment with a flash of light, when your eyes clear he presents you with an ornate staff. 'You should be honored. You have done what few have even dreamed of. In creating this staff, it has become apparent to me that there is still [further] to go.
      - Event guard: `(qglobals["mage_epic"] == "6" and item_lib.check_turn_in(e.trade, {item1=19086,item2=16807,item3=16773,item4=19087}) )`
    - event_trade NPC message: You have gained 5 ability points!

## Epic 2.0

### "Focus of Primal Elements" (19839)

<a id="epic-item-19839"></a>

**Earlier reward routes required by this graph path:** ["Staff of Elemental Essence" (19092)](#epic-item-19092).
Revisit those instructions if another copy of a consumed item is needed.

1. global/"Global Player", say "Recipe:19908". Gives "Globe of Discordant Energy" (47100).
2. Loot "Gelidran Essence" (19099) from "a gelidran flamefreeze" (NPC 334016) in `riftseekers`. Drop cache: 8.7857% chance per kill.
3. Loot "Pyrilen Essence" (19093) from "a pyrilen firecharmer" (NPC 334010) in `riftseekers`. Drop cache: 8.7527% chance per kill.
4. draniksscar/"Iilivina", hand "Gelidran Essence" (19099) + "Pyrilen Essence" (19093). Gives "Note from Iilivina" (19438) + "Pouch of Powdered Riftseeker Essence" (19149).
    - event_trade NPC emote: grinds the small crystals into a fine powder, 'This is like nothing I have ever seen. It will take some time for me to analyze this, but thank you. I have more here than I will need. Take this pouch to Bantil, along with this note. If he doesn't know how this will help you, he may know someone who does.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1=19099,item2=19099,item3=19093,item4=19093}))`
5. poknowledge/"Bantil Io`Tuv", hand "Note from Iilivina" (19438) + "Pouch of Powdered Riftseeker Essence" (19149).
    - event_trade NPC emote:  unrolls the note and reads it to himself, 'Interesting. Well, I'm not sure I can do anything with this, but if you take this to Transon in Twilight sea, he may be able to understand it a little better.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 19438,item2=19149}))`
6. draniksscar/"Iilivina", say "Primals". Sets `mage_epic` to `10`.
    - Player: "primals"
      - NPC say: Were I to venture a guess, I'd say look for Chaos near the ruins of a fallen empire, as order would tend to oppose chaos, I would look for the Order elemental near the ranks of a well regimented army, probably an ancient army, it is a creature of prestige. The Spirit elemental would find someplace where death and decay have a strong foothold. The Body Elemental may be the most elusive, as there is life everywhere. I would assume that its strong ties with this realm would pull it to a place where there are Muramites. When you find them, bring their remains to me and I'll see what else needs to be done.
      - Condition: `(qglobals["mage_epic"] >= "9" and e.message:findi("Primals"))`
      - Linked from "hail" (explicit prompt).
7. Spawns "Order Elemental" (npc:211057) via `hohonora/mage trap#enter`.
8. Kill "Order Elemental" (NPC 211057) in `hohonora` and loot "Element of Order" (19547).
9. Spawns "Body Elemental" (npc:284105) via `ferubi/mage trap#enter`.
10. Kill "Body Elemental" (NPC 284105) in `ferubi` and loot "Element of Body" (19447).
11. Spawns "Chaos Elemental" (npc:86174) via `dreadlands/mage trap#enter`.
12. Kill "Chaos Elemental" (NPC 86174) in `dreadlands` and loot "Element of Chaos" (19444).
13. Spawns "Spirit Elemental" (npc:200060) via `codecay/mage trap#enter`.
14. Kill "Spirit Elemental" (NPC 200060) in `codecay` and loot "Element of Spirit" (19544).
15. draniksscar/"Iilivina", hand "Element of Order" (19547) + "Element of Body" (19447) + "Element of Chaos" (19444) + "Element of Spirit" (19544).
    - event_trade NPC say: You work so fast! Amazing work you have done.' She looks at the 4 essences for a moment, 'Yes, these can probably be used to bind to your staff, but we'll need some sort of binding. Something that can be used to keep large amounts of energy bound together. I have no idea where you'd find such a thing, but if you do bring it to Bantil with your staff, and he'll be able to finish your journey.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1=19547,item2=19447,item3=19444,item4=19544}))`
16. poknowledge/"Bantil Io`Tuv", hand "Globe of Discordant Energy" (47100) + "Staff of Elemental Essence" (19092). Gives "Focus of Primal Elements" (19839).
    - event_trade NPC emote: pulls the four essences from his pocket.  He then wraps them around your staff with the binding.  He opens a book and reads a few words in a language that you do not recognize, the staff then begins to radiate with power.  When he hands it back to you it looks very much the same, but appears to be transformed. 'You have done the impossible, we will both be remembered in the history books.  In fact, I have already started writing of our journey together, and all the assitance that you provided me.  I will make sure you get a copy when I am finished.  That you again friend!'
      - Event guard: `(qglobals["mage_epic"] == "11" and item_lib.check_turn_in(e.trade, {item1=47100,item2=19092}) )`
    - event_trade NPC message: You have gained 10 ability points!
