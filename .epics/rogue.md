# Rogue

Acquisition paths traced backwards from the 1.0, 1.5 and 2.0 epic rewards. Flags are dependencies, not the definition of an epic. **Broken** indicates missing graph provenance.

## Epic 1.0

### "Ragebringer" (11057)

1. **Unresolved introduction:** no connected introductory hail in the graph.
2. Loot "Bayle List I" (18808) from "Mutt Rootlit" in `highpass`.
3. qrg/"Gerael Woodone", say "Deliver A Flask". Gives "Flask of Nitrates" (13945).
4. akanon/"Kimble Nogflop", hand "Flask of Nitrates" (13945). Gives "Regurgitonic" (12140).
5. qrg/"Mammoth", hand "Regurgitonic" (12140). Gives "Bayle List II" (18809).
6. Loot "Bayle List III" (18810) from "Dyllin Starsine" in `highpass`.
7. Loot "Bayle List III" (18810) from "Dyllin Starsine" in `highpasshold`.
8. southro/"Rathmana Allin", hand "Bayle List I" (18808) + "Bayle List II" (18809) + "Bayle List III" (18810). Gives "Translated Parchment" (18961).
9. highpass/"Stanos Herkanor", hand "Translated Parchment" (18961). Gives "Sealed Box" (28057).
10. Hand "Sealed Box" (28057) to kithicor/"Adjutant D-Kan". Spawns "General V'ghera" (20205). Loot "General's Pouch" (28013) from "General V'ghera".
11. Alternative: Loot "General's Pouch" (28013) from "General V'ghera" (NPC 20205) in `kithicor`; trigger: kithicor/"Advisor C-Zatl", hand "Sealed Box" (28057).
12. Alternative: Loot "General's Pouch" (28013) from "General V'ghera" (NPC 20205) in `kithicor`; trigger: kithicor/"Brigadier G-Tav", hand "Sealed Box" (28057).
13. Alternative: Loot "General's Pouch" (28013) from "General V'ghera" (NPC 20205) in `kithicor`; trigger: kithicor/"Coercer Q-Ioul", hand "Sealed Box" (28057).
14. Alternative: Loot "General's Pouch" (28013) from "General V'ghera" (NPC 20205) in `kithicor`; trigger: kithicor/"Ioltos V-Ghera", hand "Sealed Box" (28057).
15. Alternative: Loot "General's Pouch" (28013) from "General V'ghera" (NPC 20205) in `kithicor`; trigger: kithicor/"Tasi V-Ghera", hand "Sealed Box" (28057).
16. Alternative: Loot "General's Pouch" (28013) from "General V'ghera" (NPC 20205) in `kithicor`; trigger: kithicor/"War Priestess T-Zan", hand "Sealed Box" (28057).
17. Loot "Fleshripper" (5411) from "Solusek kobold king" in `soldungb`.
18. Loot "Painbringer" (5410) from "Kobold Champion" in `soldungb`.
19. Loot "Mithril Two-Handed Sword" (5401) from "The Froglok King" in `gukbottom`.
20. Loot "Gigantic Zweihander" (5308) from "Karg IceBear" in `everfrost`.
21. qey2hh1/"Vilnius The Small", hand "Gigantic Zweihander" (5308) + "Mithril Two-Handed Sword" (5401) + "Painbringer" (5410) + "Fleshripper" (5411). Gives "Jagged Diamond Dagger" (7506).
22. Loot "Robe of the Ishva" (1357) from "Coercer Q'ioul" in `kithicor`.
23. Loot "Robe of the Ishva" (1357) from "Jinalis Andir" in `cauldron`.
24. Loot "Robe of the Ishva" (1357) from "The Ishva Mal" in `southkarana`.
25. Loot "Robe of the Kedge" (1253) from "Kubaria" (NPC 309002) in `chambersf`. Drop cache: 100% chance per kill.
26. Loot "Robe of the Oracle" (1354) from "Oracle of K'Arnon" in `oceanoftears`.
27. Loot "Robe of the Oracle" (1354) from "Oracle of K'Arnon" in `oot`.
28. Loot "Shining Metallic Robes" (1360) from "Yendar Starpyre" (NPC 56012) in `steamfont`. Drop cache: 100% chance per kill.
29. qey2hh1/"Vilnius The Small", hand "Robe of the Kedge" (1253) + "Robe of the Oracle" (1354) + "Robe of the Ishva" (1357) + "Shining Metallic Robes" (1360). Gives "Cazic Quill" (7505).
30. highpass/"Stanos Herkanor", hand "Cazic Quill" (7505) + "Jagged Diamond Dagger" (7506) + "General's Pouch" (28013). Gives "Ragebringer" (11057).

## Epic 1.5

### "Fatestealer" (52347)

1. **Unresolved introduction:** no connected introductory hail in the graph.
2. **Broken:** nothing in the graph gives, loots, spawns, or combines Fatestealer (52347).

## Epic 2.0

### "Nightshade, Blade of Entropy" (52348)

1. nedaria/"Lirprin, Head Of Affairs", say "Hail". Sets `Fatestealer` to `3`.
2. **Broken:** nothing in the graph gives, loots, spawns, or combines Fatestealer (52347).
3. Say "Check Lorb" to anguish/"Zone Status".
4. Spawns "Orb of Discordant Energy" (317087).
5. Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy".
6. Alternative: Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy" (NPC 317087) in `anguish`; trigger: anguish/"Zone Status", say "Check Uorb".
7. Alternative: Loot "Globe of Discordant Energy" (47100) from "Ornate Chest" (NPC 317112) in `anguish`; trigger: anguish/"Zone Status", say "Check Amv Chest".
8. Alternative: Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy" (NPC 317087) in `anguish`; trigger: anguish/"Zone Status", say "Signal:999999".
9. Alternative: Loot "Globe of Discordant Energy" (47100) from "Overlords Chest" (NPC 317124) in `anguish`; trigger: anguish/"Zone Status", say "Signal:999999".
10. iceclad/"Lookout Larithim", say "What Happened Then". Requires `rogue_epic_iceclad` unset. Requires `Fatestealer` ==3. Gives "Air-Tight Strongbox" (52339).
11. Say "What Happened Then" to iceclad/"Lookout Larithim".
12. Spawns "Polar Kraken" (110131).
13. Loot "Lump of Raw Alloy" (52340) from "Polar Kraken".
14. Combine in "Air-Tight Strongbox" (52339): "Lump of Raw Alloy" (52340). Produces "Strongbox Full of Alloy" (52341). The combine does not fail.
15. iceclad/"Lookout Larithim", hand "Strongbox Full of Alloy" (52341). Gives "Strongbox Half Full of Velixite" (52342).
16. bloodfields/"Keetra The Lost", say "Lirprin Sent Me". Sets `rogue_epic_keetra` to `1`.
17. **Broken:** no event trigger found for `gunthak/a shadowed assassin#event_death_complete`.
18. Loot "Krill's Head" (52344) from "Krill the Backbleeder".
19. gunthak/"Lairyn Debeian", hand "Krill's Head" (52344). Sets `rogue_epic_lairyn` to `1`.
20. iceclad/"Lookout Larithim", hand "Strongbox Full of Alloy" (52341). Sets `rogue_epic_larithim` to `1`.
21. mirb/"Durgin Skell", say "Lirprin Sent Me". Sets `rogue_epic_durgin` to `1`.
22. Spawns "Wren Simsy" (336253) in `dranik` on kill.
23. Loot "Wren's Fatestealer" (21346) from "Wren Simsy".
24. nedaria/"Lirprin, Head Of Affairs", hand "Wren's Fatestealer" (21346) + "Globe of Discordant Energy" (47100) + "Strongbox Half Full of Velixite" (52342) + "Fatestealer" (52347). Requires `Fatestealer` ==3. Gives "Nightshade, Blade of Entropy" (52348).

## Quest-state progression

## 0. Prerequisites

Shared acquisition steps appear in the first prerequisite chain that needs them. Later sections reference that chain rather than repeating it.

### "Strongbox Half Full of Velixite" (52342)

1. **Broken:** nothing in the graph gives, loots, spawns, or combines Fatestealer (52347).
2. nedaria/"Lirprin, Head Of Affairs", say "Hail". Sets `Fatestealer` to `3`.
3. iceclad/"Lookout Larithim", say "What Happened Then". Requires `rogue_epic_iceclad` unset. Requires `Fatestealer` ==3. Gives "Air-Tight Strongbox" (52339).
    - Dialogue with iceclad/"Lookout Larithim":
      - Player: "Lirprin Sent Me"
        - NPC say: Lirprin sent ye, did he mate? I was beginnin' ta wonder when the perils of me dastardly mutiny would catch up with me. Tis my shame, and I'll shoulder the burden 'til the day I rest at the bottom of the ocean. To tell ye the truth Cap'n Lirprin treated us alright, but te be away from ship n' sail was murder. I'd rather be scrapin' barnacles for all eternity than spend another moment in yon Discord Plane. Only, well, it seems that me ship and sail are gone again.' Larithim sighs dramatically, and waits for the effect to sink in before continuing. 'Would ye like ta [hear the tale], landlubber? Tis guaranteed to bring a tear ta the eye o' even the saltiest sea dog. Arrrr.
        - Condition: `(e.message:findi("lirprin sent me") and qglobals["Fatestealer"] == "3")`
      - Player: "Hear The Tale" (link: explicit mention)
        - NPC say: Allow me te paint ye the picture, Sanam, of a story so strange and frightenin'! Twasn't more than a fortnight followin' my glorious return to plunderin'. I was bringin' me ship, Glaciersmash, into the coast ye see before ya now. The weather was cruel and unrelentin'. Waves they were crashin' up against the port bow.' He motions with his arms to indicate large waves, and makes a shrill blowing sound to imitate the wind. 'Hoist the main sail, tug the riggin's and man the longboats men, says I. That's when a twisting tentacle as thick as yer leg stretched out from the waters and latched ahold of the main mast! Guess ye [what happened then]?
        - Condition: `(e.message:findi("hear the tale") and qglobals["Fatestealer"] == "3")`
      - Player: "What Happened Then" (link: explicit mention)
        - NPC say: Arrr. The boat she tipped and groaned, wood bucklin' and rope snappin'. My precious cargo of metal alloy spilled overboard. Before we knew it, she capsized like a maiden's . . . Wait, is that . . .? Well I'll be a crusty barnacle. Ye see that there, Sanam!? NO, not the tower. There it is again - the scurvy squid has returned. IT BE THE POLAR KRAKEN! Get out there and harpoon its backside, Sanam. I'll keep a sharp lookout here and we'll split the booty. The alloy will oxidize right quick if ye expose it to the air - stash it in here and bring it back te me.
          - Reply guard: `(qglobals["rogue_epic_iceclad"] ==  nil)`
        - NPC say: Hrm, looks like the tentacled monstrosity has taken its leave of us. Had its fill of hapless sailors I'd wager, but not te worry. The kraken'll be back, and we'll be waitin' for it. Arrr.
          - Reply guard: ``
        - Condition: `(e.message:findi("what happened then") and qglobals["Fatestealer"] == "3")`
        - Sets `rogue_epic_iceclad` to `1`.
        - Gives Air-Tight Strongbox (52339).
        - Spawns NPC 110131.
4. Say "What Happened Then" to iceclad/"Lookout Larithim".
5. Spawns "Polar Kraken" (110131).
6. Loot "Lump of Raw Alloy" (52340) from "Polar Kraken".
7. Combine in "Air-Tight Strongbox" (52339): "Lump of Raw Alloy" (52340). Produces "Strongbox Full of Alloy" (52341). The combine does not fail.
8. iceclad/"Lookout Larithim", hand "Strongbox Full of Alloy" (52341). Gives "Strongbox Half Full of Velixite" (52342).

### "Ragebringer" (11057)

1. Loot "Bayle List I" (18808) from "Mutt Rootlit" in `highpass`.
2. qrg/"Gerael Woodone", say "Deliver A Flask". Gives "Flask of Nitrates" (13945).
    - Dialogue with qrg/"Gerael Woodone":
      - Player: "Hail"
        - NPC say: It is good to meet you, . You, my friend, are an adventurer. The rugged look of you testifies to that. Let me know if you plan to adventure in the Plains of Karana. I have need of a person such as yourself to [deliver a flask].
        - Condition: `(e.message:findi("hail"))`
      - Player: "Deliver A Flask" (link: explicit mention)
        - NPC say: That is splendid! I thought I would have to take the long journey to the western Plains of Karana myself. Here you are, my friend. Take this flask of nitrates to a woman named Linaya Sowlin. It will help her crops grow stronger. You will find her farm alongside the road to Highpass Hold. She should pay you well for the delivery. Farewell.
        - Condition: `(e.message:findi("deliver a flask"))`
        - Gives Flask of Nitrates (13945).
      - Player: "Jale Phlintoes"
        - NPC say: Jale Phlintoes was trained in the ways of the Jaggedpine Treefolk since his birth. He was only eight when his parents were killed by poachers. Young Jale would have had his throat slit also if he were not off fishing at the lake. Unfortunate. The now orphaned Jale was brought up by us druids. After many conflicts with our council, he ran off to start his own sect somewhere in the nearby lands. For his terrorist activities his head now brings a high price.
        - Condition: `(e.message:findi("Jale Phlintoes"))`
      - Player: "Unkempt Druid" (link: external event mention)
        - Prompted by `event_trade`:
          - NPC say: So the Unkempt Druids are alive and well. We shall keep a watchful eye out as should you. Take this for your bravery and defense of the Jaggedpine.
          - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 12141}))`
        - NPC say: The Unkempt Druids are a radical splinter group of druids. Their beliefs have been contorted by the mad druid [Jale Phlintoes]. It is he who engineers and coordinates the druids' transgressions. From setting lumbermills aflame to murdering any man who dares to wear a bearhide. They must be stopped!! Citizens must learn to understand Tunare's will, not fear it.
        - Condition: `(e.message:findi("Unkempt Druid"))`
3. akanon/"Kimble Nogflop", hand "Flask of Nitrates" (13945). Gives "Regurgitonic" (12140).
    - Dialogue with akanon/"Kimble Nogflop":
      - Player: "Hail"
        - NPC say: Greetings! I am the keeper of this zoo. I advise you to stay on the upper tiers to observe the animals.
        - Condition: `(e.message:findi("hail"))`
      - Player: "Regurgitonic" (link: external event mention)
        - Prompted by `event_trade`:
          - NPC say: The flask of nitrates I sent for!! As was the deal, here is my [Regurgitonic]. Give it to whoever may need it and they will surely cough up whatever may be inside them with no harm to them whatsoever.
          - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 13945}))`
          - Event guard: `(fac <= 5)`
        - NPC say: I formulate the Regurgitonic myself. My animals kept eating the occasional spectator here and there. Femurs and ribs kept getting stuck inside, not to mention a few platinum pieces. Sometimes my batch would come out wrong and the animals would go berserk!! I hope I got the formula right this time.
          - Reply guard: `(fac <= 5)`
        - NPC say: You must show a greater allegiance to the Gemchoppers before we can speak with you. Search the hills for rogue clockworks. Captain Compolten shall accept two of their blackboxes and you shall prove your loyalty to our hall.
          - Reply guard: ``
        - Condition: `(e.message:findi("regurgitonic"))`
4. qrg/"Mammoth", hand "Regurgitonic" (12140). Gives "Bayle List II" (18809).
5. Loot "Bayle List III" (18810) from "Dyllin Starsine" in `highpass`.
6. Loot "Bayle List III" (18810) from "Dyllin Starsine" in `highpasshold`.
7. southro/"Rathmana Allin", hand "Bayle List I" (18808) + "Bayle List II" (18809) + "Bayle List III" (18810). Gives "Translated Parchment" (18961).
    - Dialogue with southro/"Rathmana Allin":
      - Player: "Hail"
        - NPC say: Company?! Way out here in the desert of Ro? This is a pleasant surprise! Won't you stay for a while? I am sure the desert has dried your throat. I have supplies if necessary. At a price, of course. Are you [traveling] or are you here on [business]?
        - Condition: `(e.message:findi("hail"))`
      - Player: "Business" (link: explicit mention)
        - NPC say: Of course. You do not look like a traveling merchant or a lost adventurer. Someone has sent you to Rathmana. Well then, let's not waste time. Give me the item, or items, and my fee of twenty gold coins. It must be gold. I have no use for any other metals.
        - Condition: `(e.message:findi("business"))`
      - Player: "Traveling" (link: explicit mention)
        - NPC say: Oh, wonderful! Then you must need water and rations for your long journey. Be sure to approach any camp you may find in Ro with caution. There are many bandits in the desert. If it were not for Ortallius, they would have gutted me and thieved all my merchandise by now. If you have any use of magic then I believe I may have an [offer] for you.
        - Condition: `(e.message:findi("traveling"))`
      - Player: "Offer" (link: explicit mention)
        - NPC say: My offer to you is this, you give me thirty gold and I allow you to reach into my scroll bag and retrieve one scroll and only one. It may be the spell of a wizard or maybe not. The school of magic will not be known beforehand. The only knowledge you will have is that Rathmana will not exchange the spell for another. You get what you take. Do you wish to reach into my bag? Then give Rathmana his thirty gold coins.
        - Condition: `(e.message:findi("offer"))`
8. highpass/"Stanos Herkanor", hand "Translated Parchment" (18961). Gives "Sealed Box" (28057).
9. Hand "Sealed Box" (28057) to kithicor/"Adjutant D-Kan". Spawns "General V'ghera" (20205). Loot "General's Pouch" (28013) from "General V'ghera".
10. Alternative: Loot "General's Pouch" (28013) from "General V'ghera" (NPC 20205) in `kithicor`; trigger: kithicor/"Advisor C-Zatl", hand "Sealed Box" (28057).
11. Alternative: Loot "General's Pouch" (28013) from "General V'ghera" (NPC 20205) in `kithicor`; trigger: kithicor/"Brigadier G-Tav", hand "Sealed Box" (28057).
12. Alternative: Loot "General's Pouch" (28013) from "General V'ghera" (NPC 20205) in `kithicor`; trigger: kithicor/"Coercer Q-Ioul", hand "Sealed Box" (28057).
13. Alternative: Loot "General's Pouch" (28013) from "General V'ghera" (NPC 20205) in `kithicor`; trigger: kithicor/"Ioltos V-Ghera", hand "Sealed Box" (28057).
14. Alternative: Loot "General's Pouch" (28013) from "General V'ghera" (NPC 20205) in `kithicor`; trigger: kithicor/"Tasi V-Ghera", hand "Sealed Box" (28057).
15. Alternative: Loot "General's Pouch" (28013) from "General V'ghera" (NPC 20205) in `kithicor`; trigger: kithicor/"War Priestess T-Zan", hand "Sealed Box" (28057).
16. Loot "Fleshripper" (5411) from "Solusek kobold king" in `soldungb`.
17. Loot "Painbringer" (5410) from "Kobold Champion" in `soldungb`.
18. Loot "Mithril Two-Handed Sword" (5401) from "The Froglok King" in `gukbottom`.
19. Loot "Gigantic Zweihander" (5308) from "Karg IceBear" in `everfrost`.
20. qey2hh1/"Vilnius The Small", hand "Gigantic Zweihander" (5308) + "Mithril Two-Handed Sword" (5401) + "Painbringer" (5410) + "Fleshripper" (5411). Gives "Jagged Diamond Dagger" (7506).
    - Dialogue with qey2hh1/"Vilnius The Small":
      - Player: "Hail"
        - NPC say: , just because I am short don't mean I can't bounce your rump all over these hills. Now, do you have something for me, or are you just in search of a rump bouncing?
        - Condition: `(e.message:findi("hail"))`
      - Player: "Rump" (link: explicit mention)
        - NPC say: My pleasure to oblige you then. Shall I start on the left side or the right side?
        - Condition: `(e.message:findi("rump"))`
      - Player: "You" (link: explicit mention)
        - NPC say: Vilnius, as I have told you. And yes, I am not as large as most of my kin. But that is a blessing, because my brain is bigger than that of an $race. <grin> I am a Facilitator. I.. facilitate.. jobs. You want something somebody else has, I can arrange for you to have it.. even if that something is their life. That is why I am here now, waiting on something to turn up in my hands before I pass it on to my client. Though I am a bit tired of waiting. My hired help seem to be delayed.
        - Condition: `(e.message:findi("you"))`
      - Player: "Malka"
        - NPC say: Malka Rale works for me from time to time. One of the best thieves I have ever met, and damn handy with a blade. She is long overdue to meet me here. I'm afraid she may have run into trouble in Qeynos.
        - Condition: `(e.message:findi("malka"))`
      - Player: "Delayed" (link: explicit mention)
        - Prompted by player input: "You"
        - NPC say: Yes, delayed. She has always been prompt in the past, but she is several days overdue, and I know for a fact she completed the job. I am beginning to wonder if something happened to her. I would go check, but I run the risk of missing her if she shows up here.
        - Condition: `(e.message:findi("delayed"))`
      - Player: "Job" (link: explicit mention)
        - NPC say: I need a few more items for a collector. They are rare and valuable, but I will pay you well for your trouble. I need the sword owned by the king of the Frogloks, the sword my distant cousin Karg is so proud of, and the matched set of Painbringer and Fleshripper, held by the kobolds. Return those to me quickly, and we will take it from there, eh?
        - Condition: `(e.message:findi("job"))`
21. Loot "Robe of the Ishva" (1357) from "Coercer Q'ioul" in `kithicor`.
22. Loot "Robe of the Ishva" (1357) from "Jinalis Andir" in `cauldron`.
23. Loot "Robe of the Ishva" (1357) from "The Ishva Mal" in `southkarana`.
24. Loot "Robe of the Kedge" (1253) from "Kubaria" (NPC 309002) in `chambersf`. Drop cache: 100% chance per kill.
25. Loot "Robe of the Oracle" (1354) from "Oracle of K'Arnon" in `oceanoftears`.
26. Loot "Robe of the Oracle" (1354) from "Oracle of K'Arnon" in `oot`.
27. Loot "Shining Metallic Robes" (1360) from "Yendar Starpyre" (NPC 56012) in `steamfont`. Drop cache: 100% chance per kill.
28. qey2hh1/"Vilnius The Small", hand "Robe of the Kedge" (1253) + "Robe of the Oracle" (1354) + "Robe of the Ishva" (1357) + "Shining Metallic Robes" (1360). Gives "Cazic Quill" (7505).
29. highpass/"Stanos Herkanor", hand "Cazic Quill" (7505) + "Jagged Diamond Dagger" (7506) + "General's Pouch" (28013). Gives "Ragebringer" (11057).

### `roguepre`

Values written: 1.

1. highkeep/"Dealer Maeline", say "Cash Out". Sets `roguepre` to `1`.
    - Requires `roguepre` unset.
    - Dialogue with highkeep/"Dealer Maeline":
      - Player: "Hail"
        - NPC say: Greetings, .
        - Condition: `(e.other:Class() == "Rogue" or e.other:GetGM())`
        - Condition: `(e.message:findi("hail"))`
      - Player: "Deal"
        - NPC emote: sweeps the cards from the table. 'Great! You won several hands that round!
        - NPC message: You now have chips to gamble with. Let me know at any time if you want me to [deal you a hand], or if you'd rather [cash out].
        - NPC emote: sweeps the cards from the table. 'Great! You ...
          - Reply guard: `prize_money == 1900`
          - Reply guard: `(rand >= 50)`
        - NPC emote: sweeps the cards from the table. 'Great! You ...
          - Reply guard: `prize_money == 2000`
          - Reply guard: `(rand >= 50)`
        - NPC emote: sweeps the cards from the table. 'Great! You ...
          - Reply guard: `prize_money >= 2100`
          - Reply guard: `(rand >= 50)`
        - Condition: `(e.other:Class() == "Rogue" or e.other:GetGM())`
        - Condition: `(e.message:findi("deal") and urn == 1 and busy == 0)`
      - Player: "Deal" (link: explicit mention)
        - NPC emote: deftly shuffles the cards together. 'Just a moment, hon, I'm still shuffling.
        - Condition: `(e.other:Class() == "Rogue" or e.other:GetGM())`
        - Condition: `(e.message:findi("deal") and urn == 1 and busy == 1)`
      - Player: "Cash Out" (link: explicit mention)
        - NPC message: You have unloaded the stolen urn, completing the first task for the Smuggler's Camp.
          - Reply guard: `prize_money >= 1800`
        - NPC say: Thanks for playing, . Here are your winnings. Come back to our establishment again anytime.
          - Reply guard: `prize_money >= 1800`
        - NPC say: Thanks for playing, . Here are your ...
          - Reply guard: `prize_money < 1800`
        - Condition: `(e.other:Class() == "Rogue" or e.other:GetGM())`
        - Condition: `(e.message:findi("cash out") and urn == 1 and qglobals["roguepre"] == nil)`
        - Sets `roguepre` to `1`.
      - Player: "Cash Out" (link: explicit mention)
        - Prompted by player input: "Deal"
        - NPC say: You have no winnings to cash in.
        - Condition: `(e.other:Class() == "Rogue" or e.other:GetGM())`
        - Condition: `(e.message:findi("cash out") and urn == 0)`

#### Steps on `roguepre` that do not change it

- `highkeep` dealer maeline, hand 9446 needs `roguepre` unset.
  - Turn in Gold-Leafed Urn (9446).

### `Fatestealer` 1.5

Values written: 1, 2, 3, 4.

1. highpass/"Stanos Herkanor", say "Hail". Sets `Fatestealer` to `1`.
    - Requires "Ragebringer" (11057).
    - Prerequisite: "Ragebringer" (11057). See section 0.
    - Dialogue with highpass/"Stanos Herkanor":
      - Player: "Hail"
        - NPC say: Ha, the prodigy returns. So good to see you, . I always consider it an honor to have your company, and we have much to talk about!
          - Reply guard: `e.other:HasItem(11057) and qglobals.Fatestealer == nil`
        - NPC say: But not here and not now. We are in grave danger, you and I, and should not be seen speaking to one another. Seek out my associates. They will apprise you of what needs to be done. When you have found them... Tell them that the sun is setting on the horizon.' He clasps your palm and gives you a strange handshake, 'Before you go, know that you have proved yourself as one of us, . You are a member of this circle and nothing will ever break that.
          - Reply guard: `e.other:HasItem(11057) and qglobals.Fatestealer == nil`
        - NPC say: We are in grave danger, you and I, and should not be seen speaking to one another. Seek out my associates. They will apprise you of what needs to be done. When you have found them... Tell them that the sun is setting on the horizon.' He clasps your palm and gives you a strange handshake, 'Before you go, know that you have proved yourself as one of us, . You are a member of this circle and nothing will ever break that.
          - Reply guard: `(qglobals.Fatestealer ~= nil)`
        - NPC say: Ah, the pouch. This is the first step. The Circle has to be upset having this taken right out from under them. That speaks well of the person who did the taking. Hanns must be even more furious now. I think I might be able to trust you. We could make a deal. I have a blade I won't use anymore, and you have those fine looking daggers Vilnius gave you. Of course, you would have to do something for me first. Let me tell you my story, then you decide.
          - Reply guard: ``
        - Condition: `(e.message:findi("hail"))`
        - Sets `Fatestealer` to `1`.
      - Player: "Who Are You" (link: conversation sequence)
        - NPC say: (chuckle) You are young, aren't you? I ran [the Circle] out of Qeynos for well over 30 years, and did a right fine job of it. It's a long story, and isn't over yet. I have much to answer for.
        - Condition: `(e.message:findi("who are you"))`
      - Player: "The Circle" (link: explicit mention)
        - NPC say: The Circle of Unseen Hands, you oaf! The largest collection of thieves, murderers, con artists, and rogues in the world. No finer men can be found anywhere.
        - Condition: `(e.message:findi("the circle"))`
      - Player: "Deal" (link: explicit mention)
        - Prompted by player input: "Hail"
        - NPC say: Aye, we could make a deal. I have a blade I won't use anymore, and you have those fine looking daggers Vilnius gave you. Of course, you would have to do something for me first. Let me tell you my [story], then you decide
        - Condition: `(e.message:findi("deal"))`
      - Player: "Story" (link: explicit mention)
        - NPC say: Johann Krieghor was the leader of the Circle and I was his second-in-command. He made a dark bargain with a Teir'Dal [General]. The Circle was to assassinate [Joren], the high elf ambassador to Qeynos. Had the plot worked, it would have weakened the alliance between high elves and humans, and possibly caused a war between the two powers. In either case, the Teir'Dal would have profited greatly by this event, and all others would have suffered. I could not stand by and let this happen, but Johann would not be deterred, for the Teir'Dal had promised him much. I had no choice but to kill Johann and the Teir'Dal agent. I made it look like they offed each other, and then I hid the [tools].
        - Condition: `(e.message:findi("story"))`
      - Player: "Joren" (link: explicit mention)
        - NPC say: Joren was the boon companion to the King of Felwithe, a mighty paladin of great reknown, much loved by all the high elves. To slay him, certain. . .items. . .were crafted to make the job possible. With the death of the Teir'dal agent, and my theft of the [tools], the General was forced to abandon the plot.
        - Condition: `(e.message:findi("joren"))`
      - Player: "General" (link: explicit mention)
        - NPC say: The General? I know not his true name, only that he is ranked high among the dark elves. He kept his identity secret, and it was only upon the death of his agent that I even learned the smallest amount about him, that of his Generalship. Knowing who he is would aid me greatly.
        - Condition: `(e.message:findi("general"))`
      - Player: "Hanns" (link: explicit mention)
        - Prompted by player input: "Hail"
        - NPC say: Hanns Krieghor was a talented young man, in many ways much more of a man than his father. After the death of [Johann], I raised Hanns as my own son, and grew to love him as such. A few years back, to take revenge upon me for his [father's murder] Hanns seized control of the Circle. At the same time, he sent four of his best killers to finish me. The killers failed, I still live. Hanns still leads the Circle in Qeynos, and still seeks [my head]
        - Condition: `(e.message:findi("hanns"))`
      - Player: "Your Head" (link: explicit mention)
        - NPC say: Aye, , Hanns has wanted me dead for years. He's tried many times, though not personally. He's smart, that one, for not facing me, but foolish for wasting so many good men for naught.
        - Condition: `(e.message:findi("your head"))`
      - Player: "Tools" (link: explicit mention)
        - Prompted by player input: "Story"
        - NPC say: To allow the assassin to slay a prince, and fight his way back out, a fell blade was crafted. It was small enough to conceal under a garment and yet large enough to strike a mortal blow through armor. Aided by vile Teir'Dal enchantments, it is much more fearsome than it appears. I would gladly rid myself of it, but I fear I can not until I [clear my name] with Hanns.
        - Condition: `(e.message:findi("tools"))`
      - Player: "Clear Your Name" (link: explicit mention)
        - NPC say: I need proof that what I say about Johann is truth, so that Hanns may forgive me. YOU can gather that proof for me. First, travel to Kaladim and Neriak, and there, upon the persons of the rogue guildmasters, you should find that which I seek, two parts of a document I recovered from the dead agent. I entrusted one to Founy, but that trust is gone, and Founy would betray me to Hanns were I to attempt to reclaim it. Tani N'mar has the other, which he should not possess, and keeps it only to spite me, not knowing its real importance. Steal them both, and bring them back to me. And don't let anyone follow you! If I am not around, tell Anson you want to see me.
        - Condition: `(e.message:findi("clear your name"))`

2. nedaria/"Lirprin, Head Of Affairs", hand "Soulstone of Lanys" (52337). Sets `Fatestealer` to `2`.
    - Requires `Fatestealer_bard` ==1.
    - Requires `Fatestealer_page` ==1.
    - Requires `Fatestealer_forge` ==1.
    - Hand in x1: "Soulstone of Lanys" (52337).
    - Spawns "a Teir'Dal guardian" (186190) in `hateplaneb` on event death_complete:186114.
    - Loot "Soulstone of Lanys" (52337) from "a Teir'Dal guardian".
    - Alternative: Loot "Soulstone of Lanys" (52337) from "a Teir'Dal guardian" (NPC 186190) in `hateplaneb`; trigger: hateplaneb/"Rogue 1 5", on event death_complete:186100.
    - Alternative: Loot "Soulstone of Lanys" (52337) from "a Teir'Dal guardian" (NPC 186190) in `hateplaneb`; trigger: hateplaneb/"Rogue 1 5", on event death_complete:186112.
    - Alternative: Loot "Soulstone of Lanys" (52337) from "a Teir'Dal guardian" (NPC 186190) in `hateplaneb`; trigger: hateplaneb/"Rogue 1 5", on event death_complete:186116.
    - Alternative: Loot "Soulstone of Lanys" (52337) from "a Teir'Dal guardian" (NPC 186190) in `hateplaneb`; trigger: hateplaneb/"Rogue 1 5", on event death_complete:186098.
    - Alternative: Loot "Soulstone of Lanys" (52337) from "a Teir'Dal guardian" (NPC 186190) in `hateplaneb`; trigger: hateplaneb/"Rogue 1 5", on event death_complete:186115.
    - Gives "Fatestealer" (52347).
    - Dialogue with nedaria/"Lirprin, Head Of Affairs":
      - Player: "Hail"
        - NPC say: I suppose the bad publicity surrounding your organization has subsided to the point where we can speak freely.' He clears his throat, 'Word is that you are looking for someone to forge a blade or two specifically for you for a specific purpose. I'll go on faith that you intend to use this weapon to catch a criminal and not become one yourself. We have the ability. My assistant, Dandi, is the best smith I know. And . . . As luck would have it I owe your friends a [favor]. The only thing we lack is the knowledge of how to imbue the weapon with dark energy. I thought this secret lied in the hands of the Teir`dal, but if they will not acquiesce perhaps there is another way. Did you ever stop to think that the directions may have been written down somewhere?
        - Condition: `(qglobals["Fatestealer"] == "1" and qglobals["Fatestealer_bard"] == "1" and e.message:findi("hail"))`
      - Player: "Favor" (link: explicit mention)
        - NPC say: Let's get one thing straight, right now, . I do NOT work for Stanos, and I do NOT work for you. It's a simple matter of repaying a favor, and I'd suggest you not press the issue lest I change my mind.
        - Condition: `(e.message:findi("favor"))`
      - Player: "Hail" (link: conversation sequence)
        - NPC say: I'm sure Stanos has already briefed you on his concern: An assassin is planning to start a war between the Dragorn and the Wayfarer's by offing a well-respected member of their society and making it look like it was us. This is true. I've verified the information myself. What Stanos doesn't know, and I'm embarrassed to admit . . . It's one of my people that's behind it all.' He fumes, and smashes his left fist into his opposite palm. 'Bah. If I ever get my hands on the scoundrel! If I even knew WHICH one it was! We've had a disturbing number of our rank go 'deserter' since my group's last visit to the Realms of Discord. Haven't heard from some of my members in days, weeks, or months. It's one of those scumbags.
        - NPC say: I'd bet my [bronze breastplate] that it's either [Lairyn Debeian], [Wren Simsy], [Longarm Larithim], [Durgin Skell] or [Keetra the Lost]. If you can prove without a shadow of a doubt, please tell me you [know who is guilty].
        - Condition: `(e.other:HasItem(52347))`
        - Condition: `(e.message:findi("hail"))`
        - Sets `Fatestealer` to `3`.
      - Player: "Lairyn" (link: explicit mention)
        - NPC say: Yes, Lairyn Debeian. Does his name sound familiar to you? It should - that's Nedaria's brother. He left my side long ago to research new magics, and for the better part of the years he kept in touch. We had been corresponding by mail. The last letter I received from him was written in a desperate scrawl. His tone was fearful and angry, which isn't like him at all. He spoke of shadows and hearing voices in his head. I'm afraid he may have done something rash. Something horrible. Don't let his frail appearance fool you, Fyredragn. He's from the same blood as Nedaria and very powerful. If you find him, drop my name. Let him know Lirprin sent you and see if he can explain his odd behavior.
        - Condition: `(e.other:HasItem(52347))`
        - Condition: `(e.message:findi("Lairyn"))`
      - Player: "Wren" (link: explicit mention)
        - Prompted by player input: "Hail"
        - NPC say: Ah, Wren. Mistress of disguise and as deadly as they come. She always obeyed orders and was ruthlessly efficient in her tasks, but I've got this feeling that what she did for the Brotherhood was done begrudgingly. That is to say, I think she was biding her time waiting for an opportunity to leave. And leave she did. She and some of the impressionable members of my group disappeared a few weeks ago. In typical rogue-like fashion, they made off with most of our supplies, too. The more unsavory Wayfarer pledges were quite taken with her striking beauty and her skill with a blade. I imagine they'd follow her anywhere. If you find her, drop my name. Let her know Lirprin sent you and see if she can explain her disappearance and theft.
        - Condition: `(e.other:HasItem(52347))`
        - Condition: `(e.message:findi("Wren"))`
      - Player: "Longarm" (link: explicit mention)
        - Prompted by player input: "Hail"
        - NPC say: Bah, just hearing his name is like hearing the screech of a harpy. The little twerp didn't care for the dangerous environment of Kuaa and deserted us without so much as a goodbye. This is the kind of behavior I have to deal with on a daily basis, and what's going to be the death of me. I swear I'll throw shackles on the next walking panic attack that whimpers about wanting to go back to their home. It goes without saying that Larithim was a roguish type and I wouldn't put it past him to do something rash and stupid. Someone overheard him saying he'd do anything to send us packing back to Norrath, for good. Starting a war with the Dragorn would fit that bill. Who knows what hole Larithim's cowering in now. There are a lot of hiding spots for a fainthearted three-foot tall gnome. If you find him, drop my name. Let him know Lirprin sent you and see if he can explain his desertion.
        - Condition: `(e.other:HasItem(52347))`
        - Condition: `(e.message:findi("Longarm"))`
      - Player: "Durgin" (link: explicit mention)
        - Prompted by player input: "Hail"
        - NPC say: I've had the pleasure of serving with a beastlord named Sharalla for quite awhile. For years, she was a reliable friend and companion. At one point I nearly asked her to become my betrothed - we were that close. However, things changed the moment she met that scoundrel Durgin Skell. Her dedication to the Wayfarer's cause wavered noticably whenever he was about. Last time I saw them, Durgin and Sharalla were preparing for [some foolish expedition]. They took a cadre of my best people, ventured off in search a 'great threat' to Norrath and haven't been seen since. I trust Durgin about as far as I can pitch an orc. There's a good chance he's used his silver tongue and charismatic appearance to misguide his group into doing something foolish. If you find him, drop my name. Let him know Lirprin sent you and see if he can explain what he's been up to.
        - Condition: `(e.other:HasItem(52347))`
        - Condition: `(e.message:findi("Durgin"))`
      - Player: "Foolish" (link: explicit mention)
        - NPC say: Yes, foolish indeed. He kept mentioning something about a frozen underground cavern below Everfrost and the nightmarish creatures that resided within. We had heard rumors of such a place, but I wouldn't give them much credibility. They're only rumors, after all.
        - Condition: `(e.other:HasItem(52347))`
        - Condition: `(e.message:findi("foolish"))`
      - Player: "Keetra" (link: explicit mention)
        - Prompted by player input: "Hail"
        - NPC say: 'Keetra the Lost' is right. She was simply 'Keetra' until we discovered her uncanny knack for straying off the beaten path. We couldn't travel half a mile without having to double back to find Keetra. You don't want to know how many times we sent a search team to locate her sorry hide. What I need to know is, was this simply absent-minded disorientation or was she feigning ignorance, trying to escape? I'm inclined to say it was the former, but with this war on the horizon we can't be too careful. Having another thief slip out of sight is not something we can afford to ignore. If you find her, drop my name. Let her know Lirprin sent you and see if she can explain where she's been.
        - Condition: `(e.other:HasItem(52347))`
        - Condition: `(e.message:findi("Keetra"))`
      - Player: "Bronze Breastplate" (link: explicit mention)
        - Prompted by player input: "Hail"
        - NPC emote: sighs, I'm not really wearing a bronze breastplate, . That's what we like to call a 'figure of speech'.
        - Condition: `(e.other:HasItem(52347))`
        - Condition: `(e.message:findi("bronze breastplate"))`
      - Player: "Know" (link: explicit mention)
        - Prompted by player input: "Hail"
        - NPC say: placeholder
          - Reply guard: `(qglobals["Fatestealer_lairyn"])`
        - NPC emote: taps his foot impatiently. There's no time to tarry, . So far, your research has turned up nothing at all. Keep looking for [Lairyn Debeian], [Wren Simsy], [Longarm Larithim], [Durgin Skell] and [Keetra the Lost].. Come back and speak with me when you know more.
          - Reply guard: ``
        - Condition: `(e.other:HasItem(52347))`
        - Condition: `(e.message:findi("know"))`

    - Subquest `Fatestealer_bard`:
#### `Fatestealer_bard`

Values written: 1.

1. overthere/"Inem R'Ker", hand "Signed Agreement" (10239) + "Signed Agreement" (52416). Sets `Fatestealer_bard` to `1`.
    - Requires `Fatestealer` ==1.
    - Requires `Fatestealer_gal` ==1.
    - Requires `Fatestealer_mar` ==1.
    - Requires `Fatestealer_lyt` ==1.
    - Hand in x1: "Signed Agreement" (10239).
    - Hand in x1: "Signed Agreement" (52416).
    - Loot "Signed Agreement" (10239) from "Seana Marsinger" in `gfaydark`.
    - Loot "Signed Agreement" (52416) from "Stefan Marsinger" in `gfaydark`.
    - Sets `Fatestealer_mar` to `1`.
    - Gives "Notice to Cease and Desist" (9590).

    - Subquest `Fatestealer` documented earlier.
    - Subquest `Fatestealer_gal`:
#### `Fatestealer_gal`

Values written: 1.

1. overthere/"Inem R'Ker", hand "Signed Agreement" (10243). Sets `Fatestealer_gal` to `1`.
    - Requires `Fatestealer` ==1.
    - Requires `Fatestealer_gal` ==1.
    - Requires `Fatestealer_mar` ==1.
    - Requires `Fatestealer_lyt` ==1.
    - Hand in x1: "Signed Agreement" (10243).
    - Loot "Signed Agreement" (10243) from "Galdorin Visigothe" in `abysmal`.
    - Sets `Fatestealer_bard` to `1`.
    - Gives "Notice to Cease and Desist" (9590).

    - Subquest `Fatestealer` documented earlier.
    - Subquest `Fatestealer_mar`:
#### `Fatestealer_mar`

Values written: 1.

1. overthere/"Inem R'Ker", hand "Signed Agreement" (10239) + "Signed Agreement" (52416). Sets `Fatestealer_mar` to `1`.
    - Requires `Fatestealer` ==1.
    - Requires `Fatestealer_gal` ==1.
    - Requires `Fatestealer_mar` ==1.
    - Requires `Fatestealer_lyt` ==1.
    - Hand in x1: "Signed Agreement" (10239).
    - Hand in x1: "Signed Agreement" (52416).
    - Loot "Signed Agreement" (10239) from "Seana Marsinger" in `gfaydark`.
    - Loot "Signed Agreement" (52416) from "Stefan Marsinger" in `gfaydark`.
    - Sets `Fatestealer_bard` to `1`.
    - Gives "Notice to Cease and Desist" (9590).

    - Subquest `Fatestealer` documented earlier.
    - Subquest `Fatestealer_gal` documented earlier.
    - Subquest `Fatestealer_lyt`:
#### `Fatestealer_lyt`

Values written: 1.

1. overthere/"Inem R'Ker", hand "Signed Agreement" (10246). Sets `Fatestealer_lyt` to `1`.
    - Requires `Fatestealer` ==1.
    - Requires `Fatestealer_gal` ==1.
    - Requires `Fatestealer_mar` ==1.
    - Requires `Fatestealer_lyt` ==1.
    - Hand in x1: "Signed Agreement" (10246).
    - Loot "Signed Agreement" (10246) from "Lythe Songbird" in `freeporteast`.
    - Loot "Signed Agreement" (10246) from "Lythe Songbird" in `freportw`.
    - Sets `Fatestealer_bard` to `1`.
    - Gives "Notice to Cease and Desist" (9590).

    - Subquest `Fatestealer` documented earlier.
    - Subquest `Fatestealer_gal` documented earlier.
    - Subquest `Fatestealer_mar` documented earlier.
###### Steps on `Fatestealer_lyt` that do not change it

- `overthere` inem r`ker, hand 10239+52416 needs `Fatestealer_lyt` ==1.
  - Sets `Fatestealer_mar` to `1`.
  - Sets `Fatestealer_bard` to `1`.
  - Turn in Signed Agreement (10239).
  - Turn in Signed Agreement (52416).
  - Gives Notice to Cease and Desist (9590).
- `overthere` inem r`ker, hand 10243 needs `Fatestealer_lyt` ==1.
  - Sets `Fatestealer_gal` to `1`.
  - Sets `Fatestealer_bard` to `1`.
  - Turn in Signed Agreement (10243).
  - Gives Notice to Cease and Desist (9590).

###### Steps on `Fatestealer_mar` that do not change it

- `overthere` inem r`ker, hand 10243 needs `Fatestealer_mar` ==1.
  - Sets `Fatestealer_gal` to `1`.
  - Sets `Fatestealer_bard` to `1`.
  - Turn in Signed Agreement (10243).
  - Gives Notice to Cease and Desist (9590).
- `overthere` inem r`ker, hand 10246 needs `Fatestealer_mar` ==1.
  - Sets `Fatestealer_lyt` to `1`.
  - Sets `Fatestealer_bard` to `1`.
  - Turn in Signed Agreement (10246).
  - Gives Notice to Cease and Desist (9590).

    - Subquest `Fatestealer_lyt` documented earlier.
###### Steps on `Fatestealer_gal` that do not change it

- `overthere` inem r`ker, hand 10239+52416 needs `Fatestealer_gal` ==1.
  - Sets `Fatestealer_mar` to `1`.
  - Sets `Fatestealer_bard` to `1`.
  - Turn in Signed Agreement (10239).
  - Turn in Signed Agreement (52416).
  - Gives Notice to Cease and Desist (9590).
- `overthere` inem r`ker, hand 10246 needs `Fatestealer_gal` ==1.
  - Sets `Fatestealer_lyt` to `1`.
  - Sets `Fatestealer_bard` to `1`.
  - Turn in Signed Agreement (10246).
  - Gives Notice to Cease and Desist (9590).

    - Subquest `Fatestealer_mar` documented earlier.
    - Subquest `Fatestealer_lyt` documented earlier.
Alternative or repeat transition to `Fatestealer_bard` = `1` (not an additional required stage).

1. overthere/"Inem R'Ker", hand "Signed Agreement" (10243). Sets `Fatestealer_bard` to `1`.
    - Requires `Fatestealer` ==1.
    - Requires `Fatestealer_gal` ==1.
    - Requires `Fatestealer_mar` ==1.
    - Requires `Fatestealer_lyt` ==1.
    - Hand in x1: "Signed Agreement" (10243).
    - Loot "Signed Agreement" (10243) from "Galdorin Visigothe" in `abysmal`.
    - Sets `Fatestealer_gal` to `1`.
    - Gives "Notice to Cease and Desist" (9590).

    - Subquest `Fatestealer` documented earlier.
    - Subquest `Fatestealer_gal` documented earlier.
    - Subquest `Fatestealer_mar` documented earlier.
    - Subquest `Fatestealer_lyt` documented earlier.
Alternative or repeat transition to `Fatestealer_bard` = `1` (not an additional required stage).

1. overthere/"Inem R'Ker", hand "Signed Agreement" (10246). Sets `Fatestealer_bard` to `1`.
    - Requires `Fatestealer` ==1.
    - Requires `Fatestealer_gal` ==1.
    - Requires `Fatestealer_mar` ==1.
    - Requires `Fatestealer_lyt` ==1.
    - Hand in x1: "Signed Agreement" (10246).
    - Loot "Signed Agreement" (10246) from "Lythe Songbird" in `freeporteast`.
    - Loot "Signed Agreement" (10246) from "Lythe Songbird" in `freportw`.
    - Sets `Fatestealer_lyt` to `1`.
    - Gives "Notice to Cease and Desist" (9590).

    - Subquest `Fatestealer` documented earlier.
    - Subquest `Fatestealer_gal` documented earlier.
    - Subquest `Fatestealer_mar` documented earlier.
    - Subquest `Fatestealer_lyt` documented earlier.
###### Steps on `Fatestealer_bard` that do not change it

- `nedaria` lirprin, head of affairs, hand 52337 needs `Fatestealer_bard` ==1.
  - Sets `Fatestealer` to `2`.
  - Turn in Soulstone of Lanys (52337).
  - Gives Fatestealer (52347).
- `nedaria` smith dandi, say hail needs `Fatestealer_bard` ==1.
  - Sets `Fatestealer_culth` to `1`.
- `nedaria` smith dandi, hand 52346 needs `Fatestealer_bard` ==1.
  - Sets `Fatestealer_forge` to `1`.
  - Turn in Smoldering Embers of Solusek (52346).

    - Subquest `Fatestealer_page`:
#### `Fatestealer_page`

Values written: 1.

1. steamfont/"Yendar Starpyre", hand "Stack of Pages" (52335). Sets `Fatestealer_page` to `1`.
    - Hand in x1: "Stack of Pages" (52335).
    - Spawns "a Teir'Dal guardian" (186190) in `hateplaneb` on event death_complete:186114.
    - Loot "Stack of Pages" (52335) from "a Teir'Dal guardian".
    - Alternative: Loot "Stack of Pages" (52335) from "a Teir'Dal guardian" (NPC 186190) in `hateplaneb`; trigger: hateplaneb/"Rogue 1 5", on event death_complete:186100.
    - Alternative: Loot "Stack of Pages" (52335) from "a Teir'Dal guardian" (NPC 186190) in `hateplaneb`; trigger: hateplaneb/"Rogue 1 5", on event death_complete:186112.
    - Alternative: Loot "Stack of Pages" (52335) from "a Teir'Dal guardian" (NPC 186190) in `hateplaneb`; trigger: hateplaneb/"Rogue 1 5", on event death_complete:186116.
    - Alternative: Loot "Stack of Pages" (52335) from "a Teir'Dal guardian" (NPC 186190) in `hateplaneb`; trigger: hateplaneb/"Rogue 1 5", on event death_complete:186098.
    - Alternative: Loot "Stack of Pages" (52335) from "a Teir'Dal guardian" (NPC 186190) in `hateplaneb`; trigger: hateplaneb/"Rogue 1 5", on event death_complete:186115.
    - Dialogue with steamfont/"Yendar Starpyre":
      - Player: "Hail"
        - NPC say: Well, if it isn't $name. I trust you don't have any unsavory women tailing you again. There's nothing more unnerving than a humie lass armed with poisoned blades. He shivers involuntarily. Still gives me nightmares to this day. But enough about that. I'm certain you didn't seek me out again for small talk. What can I help you with? Recovered any unusual artifacts lately?
          - Reply guard: `($client->GetGlobal("Fatestealer_forge") == 1)`
        - NPC say: Actually, I've been meaning to speak with you about that. When I had time alone to study the Book of Souls, I discovered that there was a section with details on how to utilize the tainted souls. In particular, how to merge them with inanimate objects. Quite interesting light reading. Unfortunately, some of the most important pages had been torn out. I can't imagine who would do such a thing. If you ever come upon these pages, which wouldn't be unusual considering your talent for acquiring unusual artifacts, please allow me to translate them for you. I'd be most interested to find out how this story ends. Oh, and this time, watch your back and don't let any strangers follow you. My heart can't take another surprise from your admirers.
          - Reply guard: `($client->GetGlobal("Fatestealer_forge") == 1)`
        - NPC say: Hail, traveler! I sense you did not simply chance upon my isolation here, but are instead seeking me for something.
          - Reply guard: ``
        - Condition: `($text=~/hail/i)`
      - Player: "Blue Orb" (link: conversation sequence)
        - NPC say: Ah yes, a blue orb composed of strange metal. My studies referred to an artifact such as that. I believe it was once in the hands of a gentleman called Laarthik K'Shin. And Laarthik, he was in the employ of someone or other, hmm. Forgive my poor memory.' His eyes widen suddenly, 'Oh! I do recall that the metal orb could be reforged over extreme heat if you were able to recover every missing piece. That by itself wouldn't be enough though, you'd need a binding element with the same aura. Furthermore, if you don't have all the pieces, melding a piece with several diamonds of bluish hue inside a forge may indicate where the remaining fragments are hidden. The orb wants to be whole again.
        - Condition: `($text=~/blue orb/i)`
      - Player: "Translate" (link: explicit mention)
        - Prompted by player input: "Hail"
        - NPC say: Oh, if it is written in Eder Teir'Dal, most likely I can translate it. I will be happy to try, in any case. Let me see it, please.
        - Condition: `($text=~/translate/i)`
      - Player: "Key" (link: external event mention)
        - Prompted by `event_item`:
          - NPC say: I say, this is indeed a challenge. This is written in what I'm sure is the language of the High Priesthood of Innoruuk. I've often wished I could read this, but I have never had the key to unlock the language. Take this for now.
          - Event guard: `(plugin::check_handin(\%itemcount, 28053 => 1))`
        - NPC say: In the Plane of Hate, where dwell Innoruuk and his minions, there is a tome. This tome is called the Book of Souls.
        - Condition: `($text=~/key/i)`
      - Player: "Book Of Souls" (link: explicit mention)
        - NPC say: The Book of Souls chronicles all the lives Innoruuk has tainted over the years. It is in the care of the Maestro of Rancor. I can use this tome as a basis for my translation, if you return it and the note to me. An experienced practitioner in the art of non-detection should be able to snatch it from its resting place, don't you think, $race?'
        - Condition: `($text=~/book of souls/i)`

###### Steps on `Fatestealer_page` that do not change it

- `nedaria` lirprin, head of affairs, hand 52337 needs `Fatestealer_page` ==1.
  - Sets `Fatestealer` to `2`.
  - Turn in Soulstone of Lanys (52337).
  - Gives Fatestealer (52347).

    - Subquest `Fatestealer_forge`:
#### `Fatestealer_forge`

Values written: 1.

1. nedaria/"Smith Dandi", hand "Smoldering Embers of Solusek" (52346). Sets `Fatestealer_forge` to `1`.
    - Requires `Fatestealer_bard` ==1.
    - Hand in x1: "Smoldering Embers of Solusek" (52346).
    - Hand "Crystallized Shard of Doomfire" (21339) + "Igneous Rock of Doomfire" (21340) + "Pile of Doomfire Ash" (21341) + "Foul Doomfire Brimstone" (21342) to soldungc/"The Firewatcher". Spawns "Culthor the Gatekeeper" (278005). Loot "Smoldering Embers of Solusek" (52346) from "Culthor the Gatekeeper".
    - Dialogue with nedaria/"Smith Dandi":
      - Player: "Hail"
        - NPC emote: Smith Dandi looks to Lirprin for approval and he nods. She turns to you again, smiling broadly, and clasps your fingers in a warm handshake.
        - NPC say: Smith Dandi is my name. I trained under Rondo before we lost him in that horrible incident, bless his poor soul. Lirprin says it's okay to talk, and I understand you have a job for me? Let's see if you have what we need...
        - NPC message: In the rocky lair of Kaladim, you have coerced the Dwarven rogues into sharing their secret of blade construction: Metallurgy.
          - Reply guard: `(qglobals["Fatestealer_nk"] == "1")`
        - NPC message: You have not coerced the Dwarven rogues into revealing their secret.
          - Reply guard: ``
        - NPC message: In the majestic palace of Shar Vahl, you have coerced the Vah Shir rogues into sharing their secret of blade construction: Blade Form.
          - Reply guard: `(qglobals["Fatestealer_sv"] == "1")`
        - NPC message: You have not coerced the Vah Shir rogues into revealing their secret.
          - Reply guard: ``
        - NPC message: In the frigid northern lands of Halas, you have coerced the Barbarian rogues into sharing their secret of blade construction: Grip.
          - Reply guard: `(qglobals["Fatestealer_hl"] == "1")`
        - NPC message: You have not coerced the Barbarian rogues into revealing their secret.
          - Reply guard: ``
        - NPC message: In the dank caverns of Paludal, you have coerced the Human rogues into sharing their secret of blade construction: Endless Poison.
          - Reply guard: `(qglobals["Fatestealer_pl"] == "1")`
        - NPC message: You have not coerced the Human rogues into revealing their secret.
          - Reply guard: ``
        - NPC message: In the cozy hovel of Rivervale, you have coerced the Halfling rogues into sharing their secret of blade construction: Perfect Balance.
          - Reply guard: `(qglobals["Fatestealer_rv"] == "1")`
        - NPC message: You have not coerced the Halfling rogues into revealing their secret.
          - Reply guard: ``
        - NPC message: You have fueled Smith Dandi's furnace with Solusek's Embers.
          - Reply guard: `(qglobals["Fatestealer_forge"] == "1")`
        - NPC message: Smith Dandi's forge is not hot enough to craft the blade.
          - Reply guard: ``
        - NPC message: Wresting the information from the icy grip of Lanys T`Vyl, you have obtained the Teir`dal secret of blade construction: Dark Enchantments.
          - Reply guard: `(qglobals["Fatestealer_page"] == "1")`
        - NPC message: You lack the Teir`dal secret of blade construction.
          - Reply guard: ``
        - NPC say: Seems you're all ready to craft the blade. The instructions you've provided call for a soulstone. If you have one of those, show it to Lirprin and then I'll get started.
          - Reply guard: `(qglobals["Fatestealer_nk"] == "1" and qglobals["Fatestealer_sv"] == "1" and qglobals["Fatestealer_hl"] == "1" and qglobals["Fatestealer_pl"] == "1" and qglobals["Fatestealer_rv"] == "1" 
			and qglobals["Fatestealer_forge"] == "1" and qglobals["Fatestealer_page"] == "1")`
        - NPC say: Hmm, you're still missing a few things. Keep at it, .
          - Reply guard: ``
        - Condition: `( qglobals["Fatestealer_bard"] == "1" and e.message:findi("hail"))`
        - Sets `Fatestealer_culth` to `1`.
      - Player: "Hail" (link: conversation sequence)
        - NPC emote: wipes her sooty hands on her apron and smiles at you. 'So, it looks as if you'll need the services of Smith Dandi once again. I was hoping you'd stop by soon so we could talk. Fantastic work clearing the names of those innocent Wayfarers. I knew them all personally and they weren't bad folk. It's a shame Lirprin can be so quick to judge. Now, something tells me you're looking to get that blade of yours improved. Let's see if you have what we need. . .
        - NPC message: From the deadly realm of Mata Muram himself, you have recovered a source of discordant energy.
          - Reply guard: `(e.other:HasItem(47100))`
        - NPC message: Smith Dandi is unable to duplicate the enchantments on Wren's weapon without a source of discordant energy.
          - Reply guard: ``
        - NPC message: From the freezing depths of Iceclad, you have recovered a lump of Velixite alloy.
          - Reply guard: `(e.other:HasItem(52342))`
        - NPC message: Smith Dandi is unable to craft the blade without a special alloy.
          - Reply guard: ``
        - NPC message: You have slain Wren Simsy and recovered her blade, which courses with discordant energy.
          - Reply guard: `(e.other:HasItem(21346))`
        - NPC message: Smith Dandi requires a blade touched by discordant energy.
          - Reply guard: ``
        - NPC say: Seems you're all ready to craft the blade. We'll need the Velixite alloy, the weapon I crafted for you last time, an example of someone else's weapon that I can use for a reference, and a source of pure discordant energy. Show those items to Lirprin and we'll get started!
          - Reply guard: `(e.other:HasItem(47100) and e.other:HasItem(52342) and e.other:HasItem(21346))`
        - Condition: `( qglobals["Fatestealer"] == "3" and e.message:findi("hail"))`

    - Subquest `Fatestealer_bard` documented earlier.
###### Steps on `Fatestealer_forge` that do not change it

- `nedaria` lirprin, head of affairs, hand 52337 needs `Fatestealer_forge` ==1.
  - Sets `Fatestealer` to `2`.
  - Turn in Soulstone of Lanys (52337).
  - Gives Fatestealer (52347).
- `steamfont` findleznax grimblewimbus, say help needs `Fatestealer_forge` ==1.
  - Spawns a decomposing body (448203).
- `steamfont` player, on loot needs `Fatestealer_forge` ==1.
  - Sets `rogue_steam_chest` to `1`.
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
- `steamfontmts` findleznax grimblewimbus, say help needs `Fatestealer_forge` ==1.
  - Spawns a decomposing body (448203).
- `steamfontmts` player, on loot needs `Fatestealer_forge` ==1.
  - Sets `rogue_steam_chest` to `1`.
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

3. nedaria/"Lirprin, Head Of Affairs", say "Hail". Sets `Fatestealer` to `3`.
    - Requires "Fatestealer" (52347).
    - **Broken:** nothing in the graph gives, loots, spawns, or combines Fatestealer (52347).

4. nedaria/"Lirprin, Head Of Affairs", hand "Wren's Fatestealer" (21346) + "Globe of Discordant Energy" (47100) + "Strongbox Half Full of Velixite" (52342) + "Fatestealer" (52347). Sets `Fatestealer` to `4`.
    - Requires `Fatestealer` ==3.
    - Hand in x1: "Globe of Discordant Energy" (47100).
    - Hand in x1: "Strongbox Half Full of Velixite" (52342).
    - Hand in x1: "Wren's Fatestealer" (21346).
    - Hand in x1: "Fatestealer" (52347).
    - Say "Check Lorb" to anguish/"Zone Status".
    - Spawns "Orb of Discordant Energy" (317087).
    - Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy".
    - Alternative: Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy" (NPC 317087) in `anguish`; trigger: anguish/"Zone Status", say "Check Uorb".
    - Alternative: Loot "Globe of Discordant Energy" (47100) from "Ornate Chest" (NPC 317112) in `anguish`; trigger: anguish/"Zone Status", say "Check Amv Chest".
    - Alternative: Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy" (NPC 317087) in `anguish`; trigger: anguish/"Zone Status", say "Signal:999999".
    - Alternative: Loot "Globe of Discordant Energy" (47100) from "Overlords Chest" (NPC 317124) in `anguish`; trigger: anguish/"Zone Status", say "Signal:999999".
    - Prerequisite: "Strongbox Half Full of Velixite" (52342). See section 0.
    - Spawns "Wren Simsy" (336253) in `dranik` on kill.
    - Loot "Wren's Fatestealer" (21346) from "Wren Simsy".
    - **Broken:** nothing in the graph gives, loots, spawns, or combines Fatestealer (52347).
    - Gives "Nightshade, Blade of Entropy" (52348).

#### Steps on `Fatestealer` that do not change it

- `bloodfields` caller donivin, hand 52349+52350+52351+52352 needs `Fatestealer` ==3.
  - Sets `rog_bf_trigger` to `1`.
  - Spawns a reclusive girplan (301033).
  - Loots Cloth Cap (1001).
  - Loots Peridot (10028).
  - Loots Diamond (10037).
  - Loots Jacinth (10053).
  - Loots Sunshard Ore (33792).
  - Loots Lucidem (35084).
  - Loots Versluierd Fungus (35087).
  - Loots Raw Shimmering Nihilite (58068).
  - Turn in Polished Bone Horn (52349).
  - Turn in Brass Mouthpiece (52350).
  - Turn in Bucket Mute (52351).
  - Turn in Thin Leather Straps (52352).
- `bloodfields` keetra the lost, say lirprin sent me needs `Fatestealer` ==3.
  - Sets `rogue_epic_keetra` to `1`.
- `dranik` daignal the revered, on kill needs `Fatestealer` ==3.
  - Spawns Wren Simsy (336253).
  - Loots Fine Steel Dagger (7350).
  - Loots Wren's Fatestealer (21346).
  - Loots Versluierd Fungus (35087).
- `firiona` vorla diensk, say come in needs `Fatestealer` ==1.
  - Gives Occluded Sun Pendant (52009).
- `halas` elyn connoy, hand 52353 needs `Fatestealer` ==1.
  - Sets `Fatestealer_hl` to `1`.
  - Sets `Fatestealer_gem` to `1`.
  - Turn in Pouch of Gems (52353).
- `halas` elyn connoy, hand 9807 needs `Fatestealer` ==1.
  - Sets `Fatestealer_hl` to `1`.
  - Turn in Satchel of Deceiver's Garb (9807).
- `hateplaneb` player, on enter needs `Fatestealer` ==1.
  - Sets `hpb_zone_emote` to `1`.
- `hateplaneb` player, on loot needs `Fatestealer` ==1.
  - Sets `rogue_hate_chest` to `1`.
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
- `iceclad` lookout larithim, say what happened then needs `Fatestealer` ==3.
  - Sets `rogue_epic_iceclad` to `1`.
  - Spawns Polar Kraken (110131).
  - Loots Lump of Raw Alloy (52340).
  - Gives Air-Tight Strongbox (52339).
- `iceclad` player, on loot needs `Fatestealer` ==3.
  - Sets `rogue_chest_ice` to `1`.
  - Spawns a chest (epic 2.0) (893).
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
- `kaladimb` diggins, hand 52353 needs `Fatestealer` ==1.
  - Sets `Fatestealer_nk` to `1`.
  - Sets `Fatestealer_gem` to `1`.
  - Turn in Pouch of Gems (52353).
- `kaladimb` diggins, hand 9813 needs `Fatestealer` ==1.
  - Sets `Fatestealer_nk` to `1`.
  - Turn in Satchel of Smithed Relics (9813).
- `kaladimb` diggins, say small job needs `Fatestealer` ==1.
  - Gives Collection Satchel (8775).
  - Gives Test of Smithing (52331).
- `mirb` durgin skell, say lirprin sent me needs `Fatestealer` ==3.
  - Sets `rogue_epic_durgin` to `1`.
- `mirb` durgin skell, say lirprin sent me needs `Fatestealer` ==3.
  - Sets `rogue_chest_mira` to `1`.
  - Spawns a chest (893).
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
- `oasis` a wayward kiraikuei, hand 9599 needs `Fatestealer` ==1.
  - Turn in Pulsating Blue Metal Sphere (9599).
  - Gives Pulsating Blue Metal Sphere (9599).
- `overthere` inem r`ker, say change their tune needs `Fatestealer` ==1.
  - Gives Notice to Cease and Desist (9590).
- `overthere` inem r`ker, hand 10239+52416 needs `Fatestealer` ==1.
  - Sets `Fatestealer_mar` to `1`.
  - Sets `Fatestealer_bard` to `1`.
  - Turn in Signed Agreement (10239).
  - Turn in Signed Agreement (52416).
  - Gives Notice to Cease and Desist (9590).
- `overthere` inem r`ker, hand 10243 needs `Fatestealer` ==1.
  - Sets `Fatestealer_gal` to `1`.
  - Sets `Fatestealer_bard` to `1`.
  - Turn in Signed Agreement (10243).
  - Gives Notice to Cease and Desist (9590).
- `overthere` inem r`ker, hand 10246 needs `Fatestealer` ==1.
  - Sets `Fatestealer_lyt` to `1`.
  - Sets `Fatestealer_bard` to `1`.
  - Turn in Signed Agreement (10246).
  - Gives Notice to Cease and Desist (9590).
- `paludal` arly golyeck, hand 52353 needs `Fatestealer` ==1.
  - Sets `Fatestealer_pl` to `1`.
  - Sets `Fatestealer_gem` to `1`.
  - Turn in Pouch of Gems (52353).
- `paludal` arly golyeck, hand 9810 needs `Fatestealer` ==1.
  - Sets `Fatestealer_pl` to `1`.
  - Turn in Satchel of Poisons (9810).
- `rivervale` lendel deeppockets, hand 13588 needs `Fatestealer` ==1.
  - Sets `Fatestealer_rv` to `1`.
  - Turn in Gubbin's Approval Letter (13588).
- `rivervale` lendel deeppockets, hand 52353 needs `Fatestealer` ==1.
  - Sets `Fatestealer_rv` to `1`.
  - Sets `Fatestealer_gem` to `1`.
  - Turn in Pouch of Gems (52353).
- `rivervale` lendel deeppockets, say small job needs `Fatestealer` ==1.
  - Gives Jumjum Twist Recipe (52333).
- `sharvahl` master taruun rakutah, hand 52353 needs `Fatestealer` ==1.
  - Sets `Fatestealer_sv` to `1`.
  - Sets `Fatestealer_gem` to `1`.
  - Turn in Pouch of Gems (52353).
- `sharvahl` master taruun rakutah, hand 9491 needs `Fatestealer` ==1.
  - Sets `Fatestealer_sv` to `1`.
  - Turn in King's Feast (9491).
- `sharvahl` master taruun rakutah, say small task needs `Fatestealer` ==1.
  - Gives King's Feast Request (52334).

### Other flags touched along the way

- `rogue_chest_ice` set to 1 at iceclad/player.
- `rogue_chest_mira` set to 1 at mirb/durgin skell.
- `rogue_epic_durgin` set to 1 at mirb/durgin skell.
- `rogue_epic_iceclad` set to 1 at iceclad/lookout larithim.
- `rogue_epic_keetra` set to 1 at bloodfields/keetra the lost.
- `rogue_epic_lairyn` set to 1 at gunthak/lairyn debeian.
- `rogue_epic_larithim` set to 1 at iceclad/lookout larithim.
- `rogue_hate_chest` set to 1 at hateplaneb/player.
- `rogue_solc_chest` set to 1 at soldungc/player.
- `rogue_steam_chest` set to 1 at steamfont/player, steamfontmts/player.
