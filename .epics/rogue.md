# Rogue — Epic Quest Walkthrough

Generated directly from quest-graph item rewards. Unresolved dependencies are marked, not inferred.

## Epic 1.0

### "Ragebringer" (11057)

<a id="epic-item-11057"></a>

1. qrg/"Gerael Woodone", say "Hail".
    - Player: "hail"
      - NPC say: It is good to meet you, . You, my friend, are an adventurer. The rugged look of you testifies to that. Let me know if you plan to adventure in the Plains of Karana. I have need of a person such as yourself to [deliver a flask].
      - Condition: `(e.message:findi("hail"))`
2. Loot "Bayle List I" (18808) from "Mutt Rootlit" (NPC 5026) in `highpass`. Drop cache: 35% chance per kill.
3. qrg/"Gerael Woodone", say "Deliver A Flask". Gives "Flask of Nitrates" (13945).
    - Player: "deliver a flask"
      - NPC say: That is splendid! I thought I would have to take the long journey to the western Plains of Karana myself. Here you are, my friend. Take this flask of nitrates to a woman named Linaya Sowlin. It will help her crops grow stronger. You will find her farm alongside the road to Highpass Hold. She should pay you well for the delivery. Farewell.
      - Condition: `(e.message:findi("deliver a flask"))`
      - Linked from "hail" (explicit prompt).
4. akanon/"Kimble Nogflop", hand "Flask of Nitrates" (13945). Gives "Regurgitonic" (12140).
    - event_trade NPC say: The flask of nitrates I sent for!! As was the deal, here is my [Regurgitonic]. Give it to whoever may need it and they will surely cough up whatever may be inside them with no harm to them whatsoever.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 13945}))`
      - Event guard: `(fac <= 5)`
    - event_trade NPC say: You must show a greater allegiance to the Gemchoppers before we can speak with you. Search the hills for rogue clockworks. Captain Compolten shall accept two of their blackboxes and you shall prove your loyalty to our hall.
      - Event guard: ``
5. qrg/"Mammoth", hand "Regurgitonic" (12140). Gives "Bayle List II" (18809).
6. Loot "Bayle List III" (18810) from "Dyllin Starsine" (NPC 5015) in `highpass`. Drop cache: 91% chance per kill.
7. southro/"Rathmana Allin", hand "Bayle List I" (18808) + "Bayle List II" (18809) + "Bayle List III" (18810). Gives "Translated Parchment" (18961).
    - event_trade NPC say: hmm.  I'm not sure how you knew I could translate these, but I can always use the gold.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 18808, item2 = 18809, item3 = 18810, gold = 20}))`
    - event_trade NPC say: Here is your translation.
8. highpass/"Stanos Herkanor", hand "Translated Parchment" (18961). Gives "Sealed Box" (28057).
    - event_trade NPC say: Let me see what you have here. Aha, so that's who.. yes, yes! There is one more thing I need you to do. This document tells me who the originator of the plot really was. His name is General V'ghera, which is interesting, as Anson's men have spotted him in Kithicor recently. He will not be easy to get to, but if you give this box to one of his many aides, the General will HAVE to come to investigate. You see, this box used to contain the tools crafted for the assassination. When he arrives, kill him! I need any documents you find on him - with luck it will be enough evidence to convince Hanns that what I say is true. Bring any documents or dispatch cases you find, along with those blades Vilnius made you work so hard for, and we will make a trade.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 18961}))`
9. kithicor/"Adjutant D-Kan", hand "Sealed Box" (28057).
    - event_item NPC say: The General will take care of you!
      - Event guard: `(plugin::check_handin(\%itemcount, 28057 => 1))`
10. Spawns "General V`ghera" (npc:20205) after the hand-in.
11. Kill "General V`ghera" (NPC 20205) in `kithicor` and loot "General's Pouch" (28013).
12. Loot "Fleshripper" (5411) from "Solusek kobold king" (NPC 32066) in `soldungb`. Drop cache: 50% chance per kill.
13. Loot "Painbringer" (5410) from "kobold champion" (NPC 32045) in `soldungb`. Drop cache: 25% chance per kill.
14. Loot "Mithril Two-Handed Sword" (5401) from "the froglok king" (NPC 66159) in `gukbottom`. Drop cache: 25% chance per kill.
15. Loot "Gigantic Zweihander" (5308) from "Karg IceBear" (NPC 30100) in `everfrost`. Drop cache: 25% chance per kill.
16. qey2hh1/"Vilnius The Small", hand "Fleshripper" (5411) + "Painbringer" (5410) + "Mithril Two-Handed Sword" (5401) + "Gigantic Zweihander" (5308). Gives "Jagged Diamond Dagger" (7506).
    - event_trade NPC say: Very good, though how you managed to lug around all these oversized blades amazes me. I feel we can do business now, and Malka still has not shown up. Take this dagger. I had an old client who didn't, um.. pay.. so this was extracted from him. Right after it was inserted in him. For your next job, I need a collection of robes. The Robe of the Ishva, some Shining Metallic robes, an Oracle robe, and a Robe of the Kedge. I am not even sure where all these come from, but they are on my list here, and Rokyl is one of my best clients, so I figure that is your job.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 5411,item2 = 5410,item3 = 5401,item4 = 5308}))`
17. Kill "General V`ghera" (NPC 20205) in `kithicor` and loot "Cazic Quill" (7505).
18. highpass/"Stanos Herkanor", hand "General's Pouch" (28013) + "Jagged Diamond Dagger" (7506) + "Cazic Quill" (7505). Gives "Ragebringer" (11057).
    - event_trade NPC say: Very well done. I leave now to confront Hanns with this evidence. Even so, it will not be easy to regain his trust. That is why I need those daggers, in case all else fails. Bristlebane grant me luck - I can no longer live like a hunted dog. In any case, I am grateful for your aid. Take this wretched blade, I can bear it no longer. I must warn you, I feel it carries Innoruuk's curse; all who are near it learn the meaning of hate. Ironic, isn't it? You went to all that work to redeem yourself for a rapier, yet the true reward came when you redeemed another..Good luck, , for much as I, you will need it.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 28013,item2 = 7506,item3 = 7505}))`

## Epic 1.5

### "Fatestealer" (52347)

<a id="epic-item-52347"></a>

**Earlier reward routes required by this graph path:** ["Ragebringer" (11057)](#epic-item-11057).
Revisit those instructions if another copy of a consumed item is needed.

1. Loot "Soulstone of Lanys" (52337) from "a Teir`Dal guardian".
2. highpass/"Stanos Herkanor", say "Hail". Sets `Fatestealer` to `1`.
    - Player: "hail"
      - NPC say: Ha, the prodigy returns. So good to see you, . I always consider it an honor to have your company, and we have much to talk about!
        - Reply guard: `e.other:HasItem(11057) and qglobals.Fatestealer == nil`
      - NPC say: But not here and not now. We are in grave danger, you and I, and should not be seen speaking to one another. Seek out my associates. They will apprise you of what needs to be done. When you have found them... Tell them that the sun is setting on the horizon.' He clasps your palm and gives you a strange handshake, 'Before you go, know that you have proved yourself as one of us, . You are a member of this circle and nothing will ever break that.
        - Reply guard: `e.other:HasItem(11057) and qglobals.Fatestealer == nil`
      - NPC say: We are in grave danger, you and I, and should not be seen speaking to one another. Seek out my associates. They will apprise you of what needs to be done. When you have found them... Tell them that the sun is setting on the horizon.' He clasps your palm and gives you a strange handshake, 'Before you go, know that you have proved yourself as one of us, . You are a member of this circle and nothing will ever break that.
        - Reply guard: `(qglobals.Fatestealer ~= nil)`
      - NPC say: Ah, the pouch. This is the first step. The Circle has to be upset having this taken right out from under them. That speaks well of the person who did the taking. Hanns must be even more furious now. I think I might be able to trust you. We could make a deal. I have a blade I won't use anymore, and you have those fine looking daggers Vilnius gave you. Of course, you would have to do something for me first. Let me tell you my story, then you decide.
        - Reply guard: ``
      - Condition: `(e.message:findi("hail"))`
3. Loot "Signed Agreement" (10243) from "Galdorin Visigothe" (NPC 279002) in `abysmal`. Drop cache: 100% chance per kill.
4. overthere/"Inem R`Ker", hand "Signed Agreement" (10243).
    - event_trade NPC say: Well done, . Galdorin had it coming, so don't feel too guilty about your part in this.
      - Event guard: `(qglobals["Fatestealer"] == "1" and item_lib.check_turn_in(e.trade, {item1 = 10243}))`
    - event_trade NPC say: That should do the trick. I think our contact will speak with you now. His name is Lirpin, and he is a paladin that works for the Wayfarer's Brotherhood. I hear he led an expedition into Kuua recently, but his current location is anyone's guess. Good Luck.
      - Event guard: `(qglobals["Fatestealer_gal"] == "1" and qglobals["Fatestealer_mar"] == "1" and qglobals["Fatestealer_lyt"] == "1")`
5. Loot "Signed Agreement" (10239) from "Seana Marsinger" (NPC 54102) in `gfaydark`. Drop cache: 100% chance per kill.
6. Loot "Signed Agreement" (52416) from "Stefan Marsinger" (NPC 54101) in `gfaydark`. Drop cache: 100% chance per kill.
7. overthere/"Inem R`Ker", hand "Signed Agreement" (10239) + "Signed Agreement" (52416).
    - event_trade NPC say: Those Marsingers won't be speaking ill about us again anytime soon.
      - Event guard: `(qglobals["Fatestealer"] == "1" and item_lib.check_turn_in(e.trade, {item1 = 10239,item2 = 52416}))`
    - event_trade NPC say: That should do the trick. I think our contact will speak with you now. His name is Lirpin, and he is a paladin that works for the Wayfarer's Brotherhood. I hear he led an expedition into Kuua recently, but his current location is anyone's guess. Good Luck.
      - Event guard: `(qglobals["Fatestealer_gal"] == "1" and qglobals["Fatestealer_mar"] == "1" and qglobals["Fatestealer_lyt"] == "1")`
8. Loot "Signed Agreement" (10246) from "Lythe Songbird" (NPC 382253) in `freportw`. Drop cache: 100% chance per kill.
9. overthere/"Inem R`Ker", hand "Signed Agreement" (10246).
    - event_trade NPC say: Excellent, Lythe has been silenced.
      - Event guard: `(qglobals["Fatestealer"] == "1" and item_lib.check_turn_in(e.trade, {item1 = 10246}))`
    - event_trade NPC say: That should do the trick. I think our contact will speak with you now. His name is Lirpin, and he is a paladin that works for the Wayfarer's Brotherhood. I hear he led an expedition into Kuua recently, but his current location is anyone's guess. Good Luck.
      - Event guard: `(qglobals["Fatestealer_gal"] == "1" and qglobals["Fatestealer_mar"] == "1" and qglobals["Fatestealer_lyt"] == "1")`
10. Loot "Stack of Pages" (52335) from "a Teir`Dal guardian".
11. steamfont/"Yendar Starpyre", hand "Stack of Pages" (52335).
    - event_item NPC say: Splendid! The missing pages I had been looking for! Allow me a moment to sift through them.' He scans the texts line by line, flipping quickly from one sheet of parchment to another. Withdrawing a quill he quickly makes notes in the margins, then snatches your journal and copies the notes there. 'Yes, it is exactly as I had predicted. These texts detail the process by which an object can be imbued with a tortured soul. Unfortunately the focus is mostly on weaponry, which doesn't interest me in the slightest. Ah well. Appreciate the effort, $name. Perhaps it will come in handy for you. Farewell and good luck.
      - Event guard: `(plugin::check_handin(\%itemcount, 52335 => 1))`
    - event_item NPC message: You have learned how to imbue a blade with dark energy.
12. Spawns "a furious magma guardian" (npc:278123) via `soldungc/ #signal:100`.
13. Kill "a furious magma guardian" (NPC 278123) in `soldungc` and loot "Crystallized Shard of Doomfire" (21339).
14. Loot "Foul Doomfire Brimstone" (21342) from "a pool of living lava" (NPC 278043) in `soldungc`. Drop cache: 15.9687% chance per kill.
15. Loot "Igneous Rock of Doomfire" (21340) from "Typhoeus" (NPC 278069) in `soldungc`. Drop cache: 35% chance per kill.
16. Loot "Pile of Doomfire Ash" (21341) from "a Taklasinai marauder" (NPC 278075) in `soldungc`. Drop cache: 35% chance per kill.
17. soldungc/"The Firewatcher", hand "Crystallized Shard of Doomfire" (21339) + "Foul Doomfire Brimstone" (21342) + "Igneous Rock of Doomfire" (21340) + "Pile of Doomfire Ash" (21341).
    - event_trade NPC say: This should do the trick, I think! The gate is...Yes it's opening. Ha ha! The Gatekeeper comes!
      - Event guard: `(qglobals["Fatestealer_culth"] == "1" and not el:IsMobSpawnedByNpcTypeID(278005))`
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 21339,item2=21342,item3=21340,item4=21341}))`
18. Spawns "Culthor the Gatekeeper" (npc:278005) after the hand-in.
19. Kill "Culthor the Gatekeeper" (NPC 278005) in `soldungc` and loot "Smoldering Embers of Solusek" (52346).
20. nedaria/"Smith Dandi", hand "Smoldering Embers of Solusek" (52346).
    - event_trade NPC emote: gawks in amazement.  By the Gods, where did you come by these embers? These are positively unnatural, and they bare the mark of Solusek himself!' She sprinkles a handful of the smoldering lumps into the forge and -KABOOM- a blast of incredible heat knocks you off your feet. Immediately, the metal of the forge swells and becomes white hot. 'Yep, this will do the trick,' she gloats cheerfully. The blazing heat doesnt seem to bother her.
      - Event guard: `(qglobals["Fatestealer_bard"] == "1" and item_lib.check_turn_in(e.trade, {item1 = 52346}) )`
    - event_trade NPC message: You have fueled Smith Dandi's furnace with Solusek's Embers.
21. nedaria/"Lirprin, Head Of Affairs", hand "Soulstone of Lanys" (52337). Gives "Fatestealer" (52347).
    - event_trade NPC emote: discusses the process with his assistant. She listens, nodding, then begins work immediately. She takes measurements of your hands and fashions the grip so that it's a perfect fit, then turns to the hot coals of the forge. She selects a brick of fine metal. Her back to you, Dandi hammers away at the metal, sparks flying in all directions. When the job is completed she hands you the blade, still warm. 'Best work I've ever done. I hope it serves you well. Unfortunately the metal I have to work with isn't the recommended 'Velixite'. Based on the description I used the closest thing we have. Also, without an example to work from I had to improvise on a few details that weren't fully described in your documentation.
      - Event guard: `( qglobals["Fatestealer_bard"] == "1" and qglobals["Fatestealer_page"] == "1" and qglobals["Fatestealer_forge"] == "1" and item_lib.check_turn_in(e.trade, {item1 = 52337}) )`
    - event_trade NPC message: You have gained 5 ability points!

## Epic 2.0

### "Nightshade, Blade of Entropy" (52348)

<a id="epic-item-52348"></a>

**Earlier reward routes required by this graph path:** ["Fatestealer" (52347)](#epic-item-52347).
Revisit those instructions if another copy of a consumed item is needed.

1. global/"Global Player", say "Recipe:19908". Gives "Globe of Discordant Energy" (47100).
2. nedaria/"Lirprin, Head Of Affairs", say "Hail". Sets `Fatestealer` to `3`.
    - Player: "hail"
      - NPC say: I suppose the bad publicity surrounding your organization has subsided to the point where we can speak freely.' He clears his throat, 'Word is that you are looking for someone to forge a blade or two specifically for you for a specific purpose. I'll go on faith that you intend to use this weapon to catch a criminal and not become one yourself. We have the ability. My assistant, Dandi, is the best smith I know. And . . . As luck would have it I owe your friends a [favor]. The only thing we lack is the knowledge of how to imbue the weapon with dark energy. I thought this secret lied in the hands of the Teir`dal, but if they will not acquiesce perhaps there is another way. Did you ever stop to think that the directions may have been written down somewhere?
      - Condition: `(qglobals["Fatestealer"] == "1" and qglobals["Fatestealer_bard"] == "1" and e.message:findi("hail"))`
3. iceclad/"Lookout Larithim", say "What Happened Then". Gives "Air-Tight Strongbox" (52339).
    - Player: "what happened then"
      - NPC say: Arrr. The boat she tipped and groaned, wood bucklin' and rope snappin'. My precious cargo of metal alloy spilled overboard. Before we knew it, she capsized like a maiden's . . . Wait, is that . . .? Well I'll be a crusty barnacle. Ye see that there, Sanam!? NO, not the tower. There it is again - the scurvy squid has returned. IT BE THE POLAR KRAKEN! Get out there and harpoon its backside, Sanam. I'll keep a sharp lookout here and we'll split the booty. The alloy will oxidize right quick if ye expose it to the air - stash it in here and bring it back te me.
        - Reply guard: `(qglobals["rogue_epic_iceclad"] ==  nil)`
      - NPC say: Hrm, looks like the tentacled monstrosity has taken its leave of us. Had its fill of hapless sailors I'd wager, but not te worry. The kraken'll be back, and we'll be waitin' for it. Arrr.
        - Reply guard: ``
      - Condition: `(e.message:findi("what happened then") and qglobals["Fatestealer"] == "3")`
      - Linked from "hear the tale" (explicit prompt).
4. Loot "Lump of Raw Alloy" (52340) from "Polar Kraken".
5. Combine in "Air-Tight Strongbox" (52339): "Lump of Raw Alloy" (52340). Produces "Strongbox Full of Alloy" (52341). Requires Remove Traps.
6. iceclad/"Lookout Larithim", hand "Strongbox Full of Alloy" (52341). Gives "Strongbox Half Full of Velixite" (52342).
    - event_trade NPC say: Yar! Heres ye half matey
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 52341}) )`
    - event_trade NPC message: You have confirmed Larithim's innocence.
7. bloodfields/"Keetra The Lost", say "Lirprin Sent Me". Sets `rogue_epic_keetra` to `1`.
    - Player: "lirprin sent me"
      - NPC message: You have confirmed Keetra's innocence.
      - NPC say: 
      - Condition: `(e.message:findi("lirprin sent me") and qglobals["Fatestealer"] == "3")`
8. Kill gunthak/"A Shadowed Assassin".
9. Spawns "Krill the Backbleeder" (npc:224436) via `gunthak/lairyn debeian#signal:1`.
10. Kill "Krill the Backbleeder" (NPC 224436) in `gunthak` and loot "Krill's Head" (52344).
11. gunthak/"Lairyn Debeian", hand "Krill's Head" (52344).
    - event_trade NPC emote: adjusts his spectacles and peers at the head, 'True enough. This is a Wayfarer . . . Errr, was at one time. I imagine he renounced his membership in the Brotherhood sometime before he took up a career of tormenting a poor scholar. They must have been trying to get to Nedaria by coming after me. I am famliar with Krill and he is a follower, not a leader. Someone else is the mastermind behind this - a person with access to magical disguises to hide their identity. Lirprin must know of this at once, .
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 52344}) )`
    - event_trade NPC message: You have confirmed Lairyn's innocence.
12. mirb/"Durgin Skell", say "Lirprin Sent Me". Sets `rogue_epic_durgin` to `1`.
    - Player: "lirprin sent me"
      - NPC say: There's no need to mince words %s. I have no quarrel with Lirprin, but unfortunately the reverse is not also true. The man is undoubtedly angry with me. He will never forgive me for courting Sharalla and does not realize that it was her choice. She loved me, and not him. His paranoia and overbearing attitude, and eventually the outright abuse of his leadership position merely pushed her away. Now that she has fallen in the valiant service of the Brotherhood there is no further need for his insecurity.
        - Reply guard: `qglobals["Fatestealer"] == "3"`
      - NPC message: You have confirmed Durgin's innocence.
        - Reply guard: `qglobals["Fatestealer"] == "3"`
      - Condition: `e.message:findi("lirprin sent me") and laskuth_complete`
      - Linked from "progress" (sequence only; unverified).
13. Spawns "Wren Simsy" (npc:336253) via `dranik/daignal the revered#kill`.
14. Kill "Wren Simsy" (NPC 336253) in `dranik` and loot "Wren's Fatestealer" (21346).
15. nedaria/"Lirprin, Head Of Affairs", hand "Globe of Discordant Energy" (47100) + "Strongbox Half Full of Velixite" (52342) + "Wren's Fatestealer" (21346) + "Fatestealer" (52347). Gives "Nightshade, Blade of Entropy" (52348).
    - event_trade NPC message: You have gained 10 ability points!
      - Event guard: `( qglobals["Fatestealer"] == "3" and item_lib.check_turn_in(e.trade, {item1 = 47100,item2 = 52342,item3 = 21346,item4 = 52347}) )`
