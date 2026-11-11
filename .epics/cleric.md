# Cleric — Epic Quest Walkthrough

Generated directly from quest-graph item rewards. Unresolved dependencies are marked, not inferred.

## Epic 1.0

### "Water Sprinkler of Nem Ankh" (5532)

<a id="epic-item-5532"></a>

1. lakerathe/"Shmendrik Lavawalker", say "Hail".
    - Player: "hail"
      - NPC say: Hail, good $name!! Be wary near the waters of Lake Rathe! The Riptide goblin king, Lord Bergurgle, has been commanding his minions to murder and rob all who come near it! I am here seeking his death but I am afraid I am no match for all of his subjects. I shall reward you greatly for the death of Lord Bergurgle. I simply ask that you bring me his crown as proof.
      - Condition: `($text=~/hail/i)`
2. Loot "Lord Bergurgle's Crown" (28044) from "Lord Bergurgle" (NPC 51143) in `lakerathe`. Drop cache: 100% chance per kill.
3. lakerathe/"Shmendrik Lavawalker", hand "Lord Bergurgle's Crown" (28044).
    - event_item NPC emote: shoves the crown into a scorch marked leather satchel and cackles uncontrollably as madness twists his features and flames dance in his eyes. 'You, $name, have reduced the Riptides into chaos! Without a king to keep them in control they will ravage the settlements surrounding this lake! After the slaughter I shall return and easily burn the remainder of the villages and fishing shanties to the ground! None shall escape the fires of the Tyrant!!'
      - Event guard: `(plugin::check_handin(\%itemcount,28044=>1))`
4. Spawns "Natasha Whitewater" (npc:51138) after the hand-in.
5. Kill lakerathe/"Shmendrik Lavawalker".
6. Spawns "a spirit of flame" (npc:51145) via `lakerathe/natasha whitewater#signal:599`.
7. Kill "a spirit of flame" (NPC 51145) in `lakerathe` and loot "Damaged Goblin Crown" (28046).
8. lakerathe/"Natasha Whitewater", hand "Damaged Goblin Crown" (28046). Gives "Ornate Sea Shell" (28047).
    - event_item NPC say: I will have this crown returned to the Riptide Goblins immediately! Should you ever come across an Erudite named Omat Vastsea, give him this sea shell. The waters of Norrath shimmer with awareness of your deeds here today!
      - Event guard: `(plugin::check_handin(\%itemcount,28046=>1))`
9. timorous/"Omat Vastsea", hand "Ornate Sea Shell" (28047). Gives "Coral Statue of Tarew" (28051).
    - event_item NPC say: So, you are a friend of Natasha's? That is good to see. She is a very wise and gifted woman. The Riptide goblins have adopted a new king but are still in a vulnerable state until his subjects accept his rule. The Plasmatic Priesthood is aware of the weakened state of the Riptides and has convinced the Fire Peak goblins to strike against them. Although I do not agree with the mannerisms or actions of any goblin clan, such a war would be detrimental to all who are caught in its path. Lord Gimblox of the Fire Peak clan has been meeting with a member of the Plasmatic Priesthood in the Temple of Solusek Ro. Locate the Plasmatic Priest, hand him this statue to hinder his powers, then eliminate him and bring me his robe.
      - Event guard: `(plugin::check_handin(\%itemcount, 28047 => 1))`
10. soltemple/"Npc:80002", hand "Coral Statue of Tarew" (28051).
11. Spawns "a plasmatic priest" (npc:80042) after the hand-in.
12. Kill "a plasmatic priest" (NPC 80042) in `soltemple` and loot "Blood Soaked Plasmatic Priest Robe" (1299).
13. timorous/"Omat Vastsea", hand "Blood Soaked Plasmatic Priest Robe" (1299). Gives "Orb of Frozen Water" (28049).
    - event_item NPC say: You have proven yourself to be one who is willing to take responsibility for his own actions. Such a trait is desired by all deities to be present in their faithful. I pray that you had the wisdom to slay Lord Gimblox as well as the Plasmatic Priest in order to prevent further advancement in the incursion against the Riptides. Priestess Natasha awaits inside the inn for Lord Gimblox's ring, make haste for she is a busy women and will depart soon.
      - Event guard: `(plugin::check_handin(\%itemcount, 1299 => 1))`
14. Loot "Singed Scroll" (18170) from "Overking Bathezid" (NPC 103056) in `chardok`. Drop cache: 100% chance per kill.
15. Loot "Lord Gimblox's Signet Ring" (28018) from "Lord Gimblox" (NPC 31126) in `soldunga`. Drop cache: 100% chance per kill.
16. timorous/"Natasha Whitewater", hand "Lord Gimblox's Signet Ring" (28018). Gives "Ornate Sea Shell" (28056).
    - event_trade NPC say: Thank you, , for your services thus far. The Triumvirate missionaries are, so far, impressed. However, there is yet another threat rising from the Plasmatic Priesthood that may have dire effects on all of Norrath if it is not stopped. An Iksar member of the Triumvirate missionaries has discovered that the Plasmatic Priesthood has somehow convinced the sarnak summoners of Chardok to assist them in summoning Ixilblat Fer to Norrath. Take this shell to Naxot Deepwater in the Burning Woods so that she knows I have sent you. We ask that you return with the Sceptre of Ixiblat Fer as well as evidence to show that the Plasmatic Priesthood is dealing with sarnaks. High Priest Omat will await your return. I must depart now. I pray for your success.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 28018}))`
17. burningwood/"Naxot Deepwater", hand "Ornate Sea Shell" (28056). Gives "Message to Natasha" (28052).
    - event_trade NPC say: Praise the Triumvirate! Natasha sent you just in time! Those twisted sarnak summoners are summoning Ixiblat Fer as we speak! We must stop Ixiblat Fer while he is still weak or all of Norrath may be set aflame! Please do me one more favor, should I perish to this beast of fire. Give this note to Natasha when you next see her, and if you should perish and I survive, I will make sure the waters never forget your reflections of your deeds this day.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 28056}))`
18. Spawns "Ixiblat Fer, kill him, loot scepter of I.F." (npc:87151) after the hand-in.
19. Kill "Ixiblat Fer, kill him, loot scepter of I.F." (NPC 87151) in `burningwood` and loot "Sceptre of Ixiblat Fer" (28017).
20. timorous/"Omat Vastsea", hand "Singed Scroll" (18170) + "Sceptre of Ixiblat Fer" (28017). Gives "Orb of Clear Water" (28048).
    - event_item NPC say: I commend you on your success over the fire elemental lord, Ixiblat Fer. The fact that the Plasmatic Priesthood has mustered up the power to summon such a being means drastic actions must be taken to stop the fanatic cult of Fennin Ro. I wonder what kind of favor Zordak Ragefire performed for the sarnak summoners to convince them to assist in the ritual that brought forth Ixiblat Fer. The dragon Iksar hybrid abominations are not beings who ally with others easily. All I have seen in my divinations of the High Plasmatic Priest are riddles, and signs that the one who slays him may be awarded an Orb of the Triumvirate. If you are the one whom my visions foretell, then seek Zordak Ragefire and bring me his heart.
      - Event guard: `(plugin::check_handin(\%itemcount, 18170 => 1, 28017 => 1))`
21. timorous/"Natasha Whitewater", hand "Message to Natasha" (28052). Gives "Shimmering Pearl" (28054).
    - event_trade NPC say: lowers her head in mourning and whispers a prayer. 'It is a shame that fate has decided one so young and from such a background should perish, but we must not attempt to change what was destined to be. Priestess Naxot sacrificed herself selflessly so that others may be spared the horrors Ixiblat would have brought to Norrath. May the waters of Norrath forever remember her reflection. I thank you for delivering Naxot's message to me and give you this pearl imbued with the power of the Triumvirate. Should you find Zordak Ragefire, speak with him before all else and hand him this pearl. No mortal enemy of the Triumvirate can resist its enchantments.'
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 28052}))`
22. soldungb/"Zordak Ragefire", hand "Shimmering Pearl" (28054). Gives "Zordak's Box of Bindings" (17175) + "Swirling Pearl" (28059).
    - event_trade NPC emote: is engulfed by a shimmering blue light! An inhuman expression of rage crosses his face and flames leap in his eyes as he begins to vanish in the shimmering light! 'The Triumvirate may have succeeded in sending me back to my cursed homeland for the time being! I swear to you I shall return from Skyfire and destroy all of the Triumvirate Missionaries in flames!'
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 28054}))`
23. Loot "Pearlescent Fragment" (24995) from "a skyfire drake" (NPC 91038) in `skyfire`. Drop cache: 1.1213% chance per kill.
24. Combine in "Zordak's Box of Bindings" (17175): "Pearlescent Fragment" (24995). Produces "Assembled Pearlescent Shard" (24996). Requires Remove Traps.
25. skyfire/"Warder Cecilia", hand "Assembled Pearlescent Shard" (24996). Gives "Pearlescent Seal" (24997).
26. Spawns "Zordakalicus Ragefire" (npc:91090) via `skyfire/zordak ragefire#event_death_complete`.
27. Kill "Zordakalicus Ragefire" (NPC 91090) in `skyfire` and loot "Impure Heart of Zordak Ragefire" (17122).
28. Combine in "Impure Heart of Zordak Ragefire" (17122): "Pearlescent Seal" (24997), "Swirling Pearl" (28059). Produces "Zordak Ragefire's Heart" (28019). Requires Remove Traps.
29. timorous/"Omat Vastsea", hand "Zordak Ragefire's Heart" (28019). Gives "Orb of Vapor" (28050).
    - event_item NPC say: I see now that Zordak Ragefire and the exiled elder dragon Zordakalicus were the same being. That explains how he resisted our attempts to divine his affairs and past. Each of these orbs I have granted you represents one of the Triumvirate. Jhassad Oceanson awaits on the shore below to perform the ritual that will merge the orbs into a single Orb of the Triumvirate and summon an avatar from the Plane of Water. Present the Orb of the Triumvirate to the Avatar of Water when it arrives and allow your destiny to be unraveled.
      - Event guard: `(plugin::check_handin(\%itemcount, 28019 => 1))`
30. timorous/"Jhassad Oceanson", hand "Orb of Frozen Water" (28049) + "Orb of Clear Water" (28048) + "Orb of Vapor" (28050). Gives "Orb of the Triumvirate" (28023).
    - event_item NPC emote: kneels in the sand and places the three orbs into a large abalone shell bowl. A blue glow surrounds his hands as he waves them over the orbs resting in the bowl. The orbs crack and fall apart, releasing their contents, then reform into a single glowing orb. Jhassad Oceanson gently removes the Orb of the Triumvirate and places it in your hands.
      - Event guard: `(plugin::check_handin(\%itemcount, 28048 => 1, 28049 => 1, 28050 => 1))`
    - event_item NPC say: The Avatar of Water approaches. You must hand him the Orb of the Triumvirate and it will be decided if it is your destiny to wield the Nem Ankh Sprinkler.
31. timorous/"Avatar Of Water", hand "Orb of the Triumvirate" (28023). Gives "Water Sprinkler of Nem Ankh" (5532).
    - event_item NPC emote: takes the orb from you. The avatar has determined that you are worthy!
      - Event guard: `(plugin::check_handin(\%itemcount, 28023 => 1))`

## Epic 1.5

### "Harmony of the Soul" (9955)

<a id="epic-item-9955"></a>

1. erudnext/"Lumi Stergnon", say "Hail".
    - Player: "hail"
      - NPC say: Peace and tranquility be with you. .  Are you a [new acolyte of peace] or are you [here to pay homage] to the child of tranquility?
      - Condition: `(e.message:findi("hail"))`
2. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
    - Player: "battle the undead"
      - NPC say: Then you shall venture to Toxxulia Forest. There has been an increase in skeleton sightings lately. I do not know their origin, but I believe that your efforts will reduce their numbers! Take this box. Return it to me when you have filled it with the bones of these undead creatures and combined it. May Quellious' light guide you.
      - Condition: `(e.message:findi("battle the undead"))`
      - Linked from "new acolyte of peace" (explicit prompt).
3. Loot "Useless Cloth Cap" (13894) from "a kobold scout" (NPC 38035) in `tox`. Drop cache: 20% chance per kill.
4. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
5. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). Requires Remove Traps.
6. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
    - event_trade NPC say: You have done well. Let it be known to all that you fight for the Rainkeeper. Go and continue the battle.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 13882}))`
7. timorous/"Omat Vastsea", say "Destruction". Gives "Talisman of the Plasmatic Priests" (56010).
    - Player: "destruction"
      - NPC say: They are in hiding, the few alcoves that I managed to find were shrouded and hidden. Take this signet and find the keeper for each alcove. Show it to him and he will drop the veil. Strike fast and exterminate the camp before he is able to cloak the camp again. Return the talisman to me with proof of the deaths of the three remaining high priests. Once you have done this, I will send you to my brother with my blessings.
      - Condition: `($text=~/destruction/i)`
      - Linked from "Plasmatic Priests" (explicit prompt).
8. lavastorm/"Laura Rako", hand "Talisman of the Plasmatic Priests" (56010).
9. Spawns "High Priestess Shima" (npc:27128) after the hand-in.
10. Kill "High Priestess Shima" (NPC 27128) in `lavastorm` and loot "Head of High Priestess Shima" (5768).
11. greatdivide/"Gavon Morant", hand "Talisman of the Plasmatic Priests" (56010).
12. Spawns "High Priest Maltan" (npc:118211) after the hand-in.
13. Kill "High Priest Maltan" (NPC 118211) in `greatdivide` and loot "Head of High Priest Maltan" (6505).
14. scarlet/"Jimmic Adle", hand "Talisman of the Plasmatic Priests" (56010).
15. Spawns "High Priest Valon" (npc:175308) after the hand-in.
16. Kill "High Priest Valon" (NPC 175308) in `scarlet` and loot "Head of High Priest Valon" (6506).
17. timorous/"Omat Vastsea", hand "Head of High Priestess Shima" (5768) + "Head of High Priest Maltan" (6505) + "Head of High Priest Valon" (6506) + "Talisman of the Plasmatic Priests" (56010).
    - event_item NPC say: Excellent. I think this was the last of the organized Plasmatic Priests. You have done well. I will send you to my brother with my blessing. Thank you for your assistance.
      - Event guard: `(plugin::check_handin(\%itemcount, 5768 => 1, 6505 => 1, 6506 => 1, 56010 => 1))`
18. nedaria/"Tavon Vastsea", say "Hail". Sets `cleric_epic` to `1`.
    - Player: "hail"
      - NPC say: I hear you were able to put that shield to some use. That is good to hear. I was able to find some news on the leader, someone matching his description has been seen on the other side of the Wayfarer's portal in the Realm of Discord. Please visit my friend Cryssa, at the camp in Discord. She has been working on tracking the Disciple's movement in Discord.
        - Reply guard: `(e.other:HasItem(9955) and qglobals["cleric20"] ~= nil)`
      - NPC say: Greetings , I see you helped my brother in eradicating the Plasmatic Priests, stopping Zordak Ragefire, and saved Norrath from an eternity of flames. We need to [ call you to duty ] again
        - Reply guard: `(e.other:HasItem(5532) or qglobals["cleric15pre"] == "1")`
      - NPC say: Greetings , I am afraid that I need someone that I can [trust] with this task, these are dark times, and it is hard to tell friend from foe.
        - Reply guard: ``
      - Condition: `(e.other:Class() == "Cleric")`
      - Condition: `(e.message:findi("hail"))`
19. Loot "Encrypted Note" (7135) from "a noc bloodluster" (NPC 283111) in `barindu`. Drop cache: 1.575% chance per kill.
20. abysmal/"Shav The Cryptologist", hand "Encrypted Note" (7135).
    - event_trade NPC say: Interesting, you say someone who claims to be part of the Brotherhood wrote this? This is one of the dialects used by the Legion. I am the only one able to read or write any of their languages, and this is the first I have seen of this note. From what I can tell, the author is trying to arrange a meeting with the Muramites. It sounds like the contact spot is pre-arranged, as it is only vaguely referred to here. I doubt this is the first note of this nature, perhaps if you could find earlier correspondence we can find the location of the camp.
      - Event guard: `qglobals["cleric_epic"] ~= nil and qglobals["cleric_epic"] == "1" and item_lib.check_turn_in(e.trade, {item1 = 7135})`
21. Loot "Ripped Quarter of a Map" (9476) from "a ra`tuk bonebreaker" (NPC 284032) in `ferubi`. Drop cache: 5.6014% chance per kill.
22. Loot "Shredded Quarter of a Map" (9447) from "a kyv eyecollector" (NPC 284052) in `ferubi`. Drop cache: 5.0901% chance per kill.
23. Loot "Tattered Quarter of a Map" (9477) from "a mastruq warfiend" (NPC 284003) in `ferubi`. Drop cache: 5.3269% chance per kill.
24. Loot "Torn Quarter of a Map" (8778) from "an aneuk bone binder" (NPC 284035) in `ferubi`. Drop cache: 5.1778% chance per kill.
25. abysmal/"Shav The Cryptologist", hand "Ripped Quarter of a Map" (9476) + "Shredded Quarter of a Map" (9447) + "Tattered Quarter of a Map" (9477) + "Torn Quarter of a Map" (8778). Gives "Assembled Map" (56015).
    - event_trade NPC say: Ahh yes, this is exactly what we needed.' She scratches a few notes down on a piece of paper. 'Bring this to Tweister in Nedaria's Landing. She will tell you the location of the camp.
      - Event guard: `qglobals["cleric_epic"] ~= nil and qglobals["cleric_epic"] == "2" and item_lib.check_turn_in(e.trade, {item1 = 9476, item2 = 9447, item3 = 9477, item4 = 8778})`
26. **Unverified quest flag:** `cleric_epic` `==1` required.
27. nedaria/"Cartographer Tweister", hand "Assembled Map" (56015).
    - event_trade NPC emote: pulls out a map and a compass and begins triangulating the coordinates, 'This location is in the South Western corner of Lesser Faydark.
      - Event guard: `(qglobals["cleric_epic"] ~= nil and qglobals["cleric_epic"] >= "3" and item_lib.check_turn_in(e.trade, {item1 = 56015}))`
28. Kill lfaydark/"A Wayfarer".
29. Spawns "Taskmaster Mirot" (npc:57151) via `lfaydark/taskmaster mirot#signal:1`.
30. Kill "Taskmaster Mirot" (NPC 57151) in `lfaydark` and loot "Magically Sealed Letter" (9585).
31. nedaria/"Tavon Vastsea", hand "Magically Sealed Letter" (9585). Gives "Dark Disciples Notice of Service" (9591).
    - event_trade NPC emote: opens the envelope and pulls out a short letter, his brow furrows as his eyes dance across the pages. 'This is truly grim news. Until now I held hopes that the rumors held no truth, but this is irrefutable evidence of their existence. They call themselves the Disciples of Discord. As we speak they are gaining information for the Legion, gathering information about races that would prove to be powerful allies or enemies for the Legion. Bring this note to Plavo, I do not know where he is, but he must be found. His scouts may already have found what they are looking for, so make haste.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 9585}))`
32. wakening/"Scout Leader Plavo", hand "Dark Disciples Notice of Service" (9591).
    - event_trade NPC say: You are from the Faydwer camp are you? I'm not terribly familiar with the faces from there. Anyway, the scouts have been sent out, and are gathering the "parts" that we believe the Legion will need to prepare for the incursion into our realm. If we are to find their good graces, we must prove that we will stop at nothing to [aid] them.
      - Event guard: `qglobals["cleric_epic"] ~= nil and qglobals["cleric_epic"] >= "4" and item_lib.check_turn_in(e.trade, {item1 = 9591})`
33. Loot "Shissar Cerebral Cortex" (9945) from "an elite temple guard" (NPC 162026) in `ssratemple`. Drop cache: 43% chance per kill.
34. westwastes/"Scout Pirri", say "Hail".
    - Player: "hail"
      - NPC say: You are here to "help"? I think not. I will not share my glory with anyone. The only way you will get this is by prying it from the clasped fingers of my dead hand
      - Condition: `(qglobals["cleric_epic"] ~= nil and qglobals["cleric_epic"] >= "5" and e.message:findi("hail"))`
35. Spawns "Scout Pirri" (npc:120112) via `westwastes/scout pirri#hail`.
36. Kill "Scout Pirri" (NPC 120112) in `westwastes` and loot "Dragon Cerebrum" (9948).
37. Spawns "sheleric vis" (npc:179046) via `akheva/shei vinitras#event_spawn`.
38. Kill "sheleric vis" (NPC 179046) in `akheva` and loot "Akhevan Brain Stem" (9597).
39. wakening/"Scout Leader Plavo", hand "Shissar Cerebral Cortex" (9945) + "Dragon Cerebrum" (9948) + "Akhevan Brain Stem" (9597).
    - event_trade NPC say: Excellent work! The leader will be pleased. He should be here any moment to collect them.
      - Event guard: `qglobals["cleric_epic"] ~= nil and qglobals["cleric_epic"] >= "5" and item_lib.check_turn_in(e.trade, {item1 = 9945, item2 = 9948, item3 = 9597})`
40. Spawns "a gilded chest" (npc:119179) via `wakening/dark disciple master#event_death_complete`.
41. Open "a gilded chest" (NPC 119179) in `wakening` and loot "Aegis of Chaotic Worship" (9954).
42. Spawns "a murk hatchling" (npc:300084) via `wallofslaughter/a quivering egg#timer:hatch`.
43. Kill "a murk hatchling" (NPC 300084) in `wallofslaughter` and loot "Murkglider Plasma" (13639).
44. Loot "Bazu Plasma" (13658) from "Bazu Bonesmasher" (NPC 300000) in `wallofslaughter`. Drop cache: 43.0881% chance per kill.
45. Loot "Pyrilen Plasma" (13667) from "a dragorn assassin" (NPC 300046) in `wallofslaughter`. Drop cache: 91.935% chance per kill.
46. Combine in appropriate tradeskill container: "Murkglider Plasma" (13639), "Bazu Plasma" (13658), "Pyrilen Plasma" (13667). Produces "Soul Temper" (14047). Requires Brewing.
47. Combine in appropriate tradeskill container: "Water Flask" (13006), "Aegis of Chaotic Worship" (9954), "Soul Temper" (14047). Produces "Harmony of the Soul" (9955). Requires Blacksmithing.

**Unresolved graph dependencies:**
- Unverified quest flag `cleric_epic` ==1: no acyclic setter

## Epic 2.0

### "Aegis of Superior Divinity" (20076)

<a id="epic-item-20076"></a>

**Earlier reward routes required by this graph path:** ["Harmony of the Soul" (9955)](#epic-item-9955).
Revisit those instructions if another copy of a consumed item is needed.

1. timorous/"Omat Vastsea", say "Hail".
    - Player: "hail"
      - NPC say: Jhassad told me to notify him the minute you returned.  Hurry down to the beach so you do not miss him again!
        - Reply guard: `(plugin::check_hasitem($client,28048) && plugin::check_hasitem($client,28049) && plugin::check_hasitem($client,28050))`
      - NPC emote: bows deeply. 'I have been expecting you, $name. The waters have foretold your arrival. I am High Priest Omat Vastsea of the Triumvirate missionaries. Please feel free to enjoy the quiet solitude of this inn.'
        - Reply guard: ``
      - Condition: `($text=~/hail/i)`
2. dranik/"Natvil", say "Hail". Sets `cleric20` to `1`.
    - Player: "hail"
      - NPC emote: examines your craftsmanship. 'Impressive, but I'm afraid that the temper was not sufficient to unlock the full potential of the shield. For now you may use it in its current state. I suspect to fully realize the latent potential of the shield you will require a soulstone from the person who it was bound to originally as well as a Globe of Discordant Energy. Return to me when you have that, I will assist you in completing its enhancement.
        - Reply guard: `e.other:HasItem(9955)`
      - NPC say: Greetings, well met, salutations, and good day! I hear you are trying to change the resonance on a shield from Discord. Well I believe that is something with which I can assist you. You will need to have a temper made from some of the native creatures of Discord, you'll need the plasma from one of the giants of Discord, one of those flying squids, and the plasma from one of those fiery women. Brewing the temper should prove no trouble for you. Once you have the temper combine it with the shield in the forge with a flask of water, and it should become attuned to you. Once you are finished return to me, so I may evaluate your work.
        - Reply guard: ``
      - Condition: `qglobals["cleric_epic"] ~= nil and qglobals["cleric_epic"] >= "5" and e.message:findi("hail")`
3. Loot "Top Section of an Engraved Signet" (9956) from "an ikaav miragenist" (NPC 301015) in `bloodfields`. Drop cache: 6.083% chance per kill.
4. Loot "Bottom Section of an Engraved Signet" (10399) from "an ikaav castigator" (NPC 301003) in `bloodfields`. Drop cache: 4% chance per kill.
5. Loot "Center Section of an Engraved Signet" (10235) from "an ikaav deathbeckoner" (NPC 301008) in `bloodfields`. Drop cache: 5.126% chance per kill.
6. bloodfields/"Cryssa", hand "Top Section of an Engraved Signet" (9956) + "Bottom Section of an Engraved Signet" (10399) + "Center Section of an Engraved Signet" (10235).
    - event_trade NPC say: Interesting, this appears to be a charm of some sort. If I am correct you can use this to not only locate the camp, but to break whatever illusion they are using to hide it.
      - Event guard: `(qglobals["cleric20"] ~= nil and qglobals["cleric20"] >= "2")`
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 9956, item2 = 10399, item3 = 10235}))`
7. Loot "Dark Red Robe" (12433) from "default" in `wallofslaughter`.
8. timorous/"Omat Vastsea", hand "Dark Red Robe" (12433). Gives "Robe of Plasmatic Priesthood" (12509).
    - event_item NPC say: What? You found this on a Disciple in Discord?  This is a robe of the Plasmatic Priesthood, without question.  Bring this to Cecilia quickly, hopefully she will be able to divine their intentions.
      - Event guard: `($client->GetGlobal("cleric20") >= 2 && plugin::check_handin(\%itemcount, 12433 => 1))`
9. skyfire/"Warder Cecilia", hand "Robe of Plasmatic Priesthood" (12509).
    - event_item NPC say: Yes, Omat told me you were coming.  Let me see what I can divine from the robe.'  She holds the robe to her temple and closes her eyes.  You notice a brief glow from behind her eyelids before her eyes shoot open. 'This is truly terrible news.  The Plasmatic Priests are still fighting for the destruction of Norrath.  Fennin Ro's voice is silent to them now.  The remainder of their power faded with the Pantheon's interest in mortal affairs.  In their mad pursuit of power, they have allied themselves with Mata Muram.  They plan on trading their home-world for the promise of power.  Even now their leader is within the Muramite Trials.  Trying to earn a position of rank within the Legion.  Once he completes the trials we may lose our opportunity.  I am afraid you will have to visit the Labyrinth's trials and stop him before he is able to complete them.  Best of luck to you.'
      - Event guard: `($client->GetGlobal("cleric20") >= 2 && plugin::check_handin(\%itemcount, 12509 => 1))`
10. Kill "Shell of the Master" (NPC 304013) in `chambersa` and loot "Journal of the Prime Disciple" (56016).
11. Loot "Torn Journal Page" (56012) from "a lightning warrior staticfist" (NPC 316007) in `provinggrounds`. Drop cache: 5.9853% chance per kill.
12. Loot "Ripped Journal Page" (56011) from "Girplan Scavenger" (NPC 316031) in `provinggrounds`. Drop cache: 100% chance per kill.
13. Combine in "Journal of the Prime Disciple" (56016): "Torn Journal Page" (56012), "Ripped Journal Page" (56011). Produces "Ethereal Disciple's Journal" (56013). Requires Remove Traps.
14. timorous/"Omat Vastsea", hand "Ethereal Disciple's Journal" (56013).
    - event_item NPC emote: grows pale as he reads the journal, 'It is just as a feared. I can't believe he is on his way here.
      - Event guard: `($client->GetGlobal("cleric20") >= 2 && plugin::check_handin(\%itemcount, 56013 => 1))`
    - event_item NPC message: The walls of the cove tremble as the Prime Disciple appears before Omat. 'Well this is an unexpected surprise, I came looking for Omat, however revenge on you, $name, will be that much sweeter.
15. Spawns "Gefaari Drokaz" (npc:96368) after the hand-in.
16. Kill "Gefaari Drokaz" (NPC 96368) in `timorous` and loot "Soulshard of Zordak" (56014).
17. global/"Global Player", say "Recipe:19908". Gives "Globe of Discordant Energy" (47100).
18. dranik/"Natvil", hand "Soulshard of Zordak" (56014) + "Globe of Discordant Energy" (47100) + "Harmony of the Soul" (9955). Gives "Aegis of Superior Divinity" (20076).
    - event_trade NPC say: Amazing! You have found everything.' He then pulls deftly complete the shield. 'Quickly, take this back. It will bind itself to you. You have done well.
      - Event guard: `item_lib.check_turn_in(e.trade, {item1 = 56014, item2 = 47100, item3 = 9955})`
    - event_trade NPC message: You have gained 10 ability points!

**Unresolved graph dependencies:**
- Unverified quest flag `cleric_epic` ==1: no acyclic setter
