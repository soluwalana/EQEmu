# Warrior — Epic Quest Walkthrough

Generated directly from quest-graph item rewards. Unresolved dependencies are marked, not inferred.

## Epic 1.0

### "Jagged Blade of War" (10908)

<a id="epic-item-10908"></a>

1. freeporteast/"Kargek Redblade", say "Hail".
    - Player: "hail"
      - NPC emote:  looks up from his forge and says, 'Hello there, can I help you?' Your eyes are drawn to an extremely large red sword scabbard strapped to his back with no sword in it. Kargek speaks again, 'I said, can I help you or do you need help from Wenden?'
      - Condition: `(e.other:Class() == "Warrior")`
      - Condition: `(e.message:findi("hail"))`
2. freeporteast/"Kargek Redblade", say "Favor". Gives "Wax Sealed Note" (20673).
    - Player: "favor"
      - NPC say: An associate of mine is wandering somewhere in the Feerrott. His name is Oknoggin Stonesmacker. If you will deliver this note to him, I would appreciate it.
      - Condition: `(e.other:Class() == "Warrior")`
      - Condition: `(e.message:findi("favor"))`
      - Linked from "scabbard" (explicit prompt).
3. feerrott/"Oknoggin Stonesmacker", hand "Wax Sealed Note" (20673). Gives "Tiny Lute" (20674).
    - event_trade NPC emote: snatches the note from your hand and rips it open with his large hands. 'You take dis to Kargek. He want!'
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 20673}))`
4. freeporteast/"Kargek Redblade", hand "Tiny Lute" (20674). Gives "Redblade's Legacy" (18083).
    - event_trade NPC say: Thank you for delivering the note to my associate. Take this book - it will tell you a little of the history of the old scabbard. If you would like to own the scabbard, seek out my younger brother Tenal and give him the book.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 20674}))`
5. eastkarana/"Tenal Redblade", hand "Redblade's Legacy" (18083). Gives "Totem of the Freezing War" (20680).
    - event_trade NPC say: So, you know my brother Kargek. He is weak and does not believe the legend that our family was chosen by Rallos Zek to bear the great scabbard. Yet he still holds it. Very well, I shall give you the first test since my 'dear' brother seems to have forgotten it. Travel to the fortress where the children of Rallos were first cursed by the Rathe and bring me the heart of one of the goblins who have made it their new home. Do not return without the heart of your foe and this war totem.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 18083}))`
6. Loot "Heart of Frost" (10549) from "a goblin wizard" (NPC 73038) in `permafrost`. Drop cache: 20% chance per kill.
7. eastkarana/"Tenal Redblade", hand "Totem of the Freezing War" (20680) + "Heart of Frost" (10549). Gives "Totem of Fiery War" (20681).
    - event_trade NPC say: Very good, you have wreaked havoc on your foes in the ancient land of the giants. Rallos Zek must have guided your blade. (Tenal's voice is suddenly silenced and you feel as if your body is frozen. From Tenal's lips issues a voice that is not his own.) 'Bring this mortal the scales of the children of Veeshan. The red and green as well as my war totem. I will guide your blade.' Your movement returns as Tenal falls to the ground, gasping for breath.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 20680,item2 = 10549}))`
8. Loot "Red Dragon Scales" (11622) from "Lord Nagafen" (NPC 32040) in `soldungb`. Drop cache: 36.408% chance per kill.
9. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
    - Player: "battle the undead"
      - NPC say: Then you shall venture to Toxxulia Forest. There has been an increase in skeleton sightings lately. I do not know their origin, but I believe that your efforts will reduce their numbers! Take this box. Return it to me when you have filled it with the bones of these undead creatures and combined it. May Quellious' light guide you.
      - Condition: `(e.message:findi("battle the undead"))`
      - Linked from "new acolyte of peace" (explicit prompt).
10. Loot "Useless Cloth Cap" (13894) from "a kobold scout" (NPC 38035) in `tox`. Drop cache: 20% chance per kill.
11. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
12. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). Requires Remove Traps.
13. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
    - event_trade NPC say: You have done well. Let it be known to all that you fight for the Rainkeeper. Go and continue the battle.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 13882}))`
14. northro/"Verrell Cogswin", hand "Water Flask" (13006).
    - event_item NPC say: Thank Brell your kindness will not go unnoticed. I am eager to get back home I have been in the cold environment of Halas for so long, I thought I was going to turn into a snowgnome. I am just glad we finally figured out the [recipe] for that concoction.
      - Event guard: `(plugin::check_handin(\%itemcount, 13006 => 1))`
15. northro/"Verrell Cogswin", hand "Red Dragon Scales" (11622).
    - event_item NPC emote: pulls a vial out of his pocket and places the red scale on the ground before pouring some of the vials contents on the scale. The scale begins to bubble and fizz as the liquid covers it entirely. Verrell looks at you and smiles before looking back at the scale. gasping and snatching the scale up from the floor.
      - Event guard: `(plugin::check_handin(\%itemcount, 11622 => 1))`
      - Event guard: `(defined($qglobals{Green_Scale_Quest}) && ($qglobals{Green_Scale_Quest} == 1))`
    - event_item NPC say: Hmmm . . well I have some [good news] and a lot of [bad news] which do you want to hear first?
16. northro/"Verrell Cogswin", say "Adhesive". Gives "Verrell's Box of Potions" (67387).
    - Player: "adhesive"
      - NPC say: In order to make this special adhesive you will need to combine some [glue powder] and some [Deep Barley Brew] in this container with this special vial. Return the result to me and I should be able to fix the scale, but please try to hurry I have to meet my brother Pellillo Cogswin at the wizard platform so he can take me home.
      - Condition: `(defined($qglobals{Green_Scale_Quest}) && ($qglobals{Green_Scale_Quest} == 2))`
      - Condition: `($text=~/adhesive/i)`
      - Linked from "catch" (explicit prompt).
17. Loot "Fractured Centaur Hoof" (67388) from "centaur sheltie" (NPC 14088) in `southkarana`. Drop cache: 35% chance per kill.
18. Loot "Fire Giant Embers" (67389) from "a fire giant warlord" (NPC 278023) in `soldungc`. Drop cache: 28.3488% chance per kill.
19. Loot "Jagged Permafrost Shards" (67390) from "The Chilling Terror" (NPC 73092) in `permafrost`. Drop cache: 25.4833% chance per kill.
20. Combine in appropriate tradeskill container: "Fractured Centaur Hoof" (67388), "Fire Giant Embers" (67389), "Jagged Permafrost Shards" (67390). Produces "Glue Powder" (67391). Requires Baking.
21. Buy "Barley" (16590) from "Heidi Grainsifter" (NPC 1065) in `qeynos`. Base price: 15 copper.
22. Buy "Deep Fungus Mold" (67393) from "Heidi Grainsifter" (NPC 1065) in `qeynos`. Base price: 50,000 copper.
23. Buy "Distilled Spirits" (67394) from "Heidi Grainsifter" (NPC 1065) in `qeynos`. Base price: 5,000 copper.
24. Combine in appropriate tradeskill container: "Barley" (16590), "Deep Fungus Mold" (67393), "Distilled Spirits" (67394). Produces "Deep Barley Brew" (67392). Requires Brewing.
25. Combine in "Verrell's Box of Potions" (67387): "Glue Powder" (67391), "Deep Barley Brew" (67392), "Potion Vial" (67395). Produces "Thick Adhesive" (67386). Requires Remove Traps.
26. northro/"Verrell Cogswin", hand "Thick Adhesive" (67386). Gives "Grey Scale Pieces" (67385) + "Thick Adhesive" (67396).
    - event_item NPC say: That should do. Here, combine these in the Box of Potions I gave you.
      - Event guard: `(plugin::check_handin(\%itemcount, 67386 => 1))`
27. Combine in "Verrell's Box of Potions" (67387): "Grey Scale Pieces" (67385), "Thick Adhesive" (67396). Produces "Grey Colored Scales" (67384). Requires Remove Traps.
28. northro/"Verrell Cogswin", hand "Grey Colored Scales" (67384). Gives "Green Dragon Scales" (11582).
    - event_item NPC emote: pulls a vial out of his pocket and places the red scale on the ground before pouring some of the vials contents on the scale. The scale begins to bubble and fizz as the liquid covers it entirely. Verrell looks at you and smiles before looking back at the scale.
      - Event guard: `(plugin::check_handin(\%itemcount, 67384 => 1))`
    - event_item NPC say: Worked that time, yer bugger!
29. eastkarana/"Tenal Redblade", hand "Totem of Fiery War" (20681) + "Red Dragon Scales" (11622) + "Green Dragon Scales" (11582). Gives "Mark of the Sword" (20683).
    - event_trade NPC emote: looks at you oddly as you hand him the scales. 'What are..? 'You have done well, mortal, and you will be rewarded if you are truly brave. Travel to the Plane of Hatred and slay the ancient bard who lives there. Do not return without his hand and this mark or you will never be a true warlord.' Tenal drops to the ground as the last words leave his lips.'
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 20681,item2 = 11622,item3 = 11582}))`
30. Loot "Hand of the Maestro" (20676) from "Hand of the Maestro" (NPC 76015) in `hateplane`. Drop cache: 100% chance per kill.
31. eastkarana/"Tenal Redblade", hand "Mark of the Sword" (20683) + "Hand of the Maestro" (20676). Gives "Tenal's note to Kargek" (20684).
    - event_trade NPC emote: looks horrified as you give him the hand of the Maestro of Rancor and show him the mark of the sword.  The godlike voice returns, 'You have done well to acquire this. One final task must be completed before you hold the red scabbard in your mortal hands.' Tenal reaches out and hands you a note. 'Take this note and a wingblade of the spirocs to Kargek. When he receives them, I will speak to you one last time.'
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 20683,item2 = 20676}))`
32. Loot "Spiroc Wingblade" (20679) from "The Spiroc Lord" (NPC 71012) in `airplane`. Drop cache: 50.413% chance per kill.
33. freeporteast/"Kargek Redblade", hand "Tenal's note to Kargek" (20684) + "Spiroc Wingblade" (20679). Gives "Red Scabbard" (17859).
    - event_trade NPC say: What is this? A note from my brother? Thank you for the gift as well.' Kargek reads the note and hands you the huge sword hilt. Your mind is filled with the sound of battle and a voice. 'Place the ancient sword blade, ancient blade, finely crafted dragon head hilt and the jeweled dragon head hilt into the scabbard to receive your rewards. If you think you are worthy, place your rewards into the scabbard and see what havoc you can unleash on the world. Kargek addresses you as you turn to leave. 'One more thing. Gartrog over there has told me of a great discovery. Seems there are all sorts of stones being found in the recently discovered lost dungeons scattered around Antonica. The Wayfarer's Brotherhood has found a way to make items even more powerful by using the stones with existing items.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 20684, item2 = 20679}))`
34. lakerathe/"Triathalon Swim Goggles", say "Hail". Gives "Rebreather" (16889).
    - Player: "hail"
      - NPC say: Welcome, $name!  Good to see that you came out for the event.  here are some swim goggles to help you cross the lake.  Don't forget to hand these to my friend Bike on the far shore so that you can complete the next leg of the race.
      - Condition: `($text=~/hail/i)`
35. Loot "Block of Permafrost" (20665) from "an ice giant" (NPC 73078) in `permafrost`. Drop cache: 35% chance per kill.
36. Buy "Keg of Vox Tail Ale" (20664) from "Captain Rohand" (NPC 1101) in `qeynos`. Base price: 1 copper.
37. oceanoftears/"Denken Strongpick", hand "Rebreather" (16889) + "Block of Permafrost" (20665) + "Keg of Vox Tail Ale" (20664). Gives "Ancient Sword Blade" (20667).
    - event_item NPC say: Excellent! Here is your sword. I feel like I'm at home already!
      - Event guard: `(plugin::check_handin(\%itemcount,16889=>2,20665=>1,20664=>1))`
38. Loot "Ancient Blade" (20670) from "Queen Velazul Di`zok" (NPC 103055) in `chardok`. Drop cache: 100% chance per kill.
39. Collect ground spawn "Unjeweled Dragon Head Hilt" (20668) in `lakerathe`.
40. potranquility/"Elder Gelok", say "Dorandomgem". Gives "Diamond" (10037).
41. Spawns "A parasitic murkglider" (npc:303121) via `causeway/withering murkglider#event_hp`.
42. Kill "A parasitic murkglider" (NPC 303121) in `causeway` and loot "Black Sapphire" (10036).
43. Loot "Soulstone of Lanys" (52337) from "a Teir`Dal guardian".
44. Loot "Bayle List I" (18808) from "Mutt Rootlit" (NPC 5026) in `highpass`. Drop cache: 35% chance per kill.
45. qrg/"Gerael Woodone", say "Deliver A Flask". Gives "Flask of Nitrates" (13945).
    - Player: "deliver a flask"
      - NPC say: That is splendid! I thought I would have to take the long journey to the western Plains of Karana myself. Here you are, my friend. Take this flask of nitrates to a woman named Linaya Sowlin. It will help her crops grow stronger. You will find her farm alongside the road to Highpass Hold. She should pay you well for the delivery. Farewell.
      - Condition: `(e.message:findi("deliver a flask"))`
      - Linked from "hail" (explicit prompt).
46. akanon/"Kimble Nogflop", hand "Flask of Nitrates" (13945). Gives "Regurgitonic" (12140).
    - event_trade NPC say: The flask of nitrates I sent for!! As was the deal, here is my [Regurgitonic]. Give it to whoever may need it and they will surely cough up whatever may be inside them with no harm to them whatsoever.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 13945}))`
      - Event guard: `(fac <= 5)`
    - event_trade NPC say: You must show a greater allegiance to the Gemchoppers before we can speak with you. Search the hills for rogue clockworks. Captain Compolten shall accept two of their blackboxes and you shall prove your loyalty to our hall.
      - Event guard: ``
47. qrg/"Mammoth", hand "Regurgitonic" (12140). Gives "Bayle List II" (18809).
48. Loot "Bayle List III" (18810) from "Dyllin Starsine" (NPC 5015) in `highpass`. Drop cache: 91% chance per kill.
49. southro/"Rathmana Allin", hand "Bayle List I" (18808) + "Bayle List II" (18809) + "Bayle List III" (18810). Gives "Translated Parchment" (18961).
    - event_trade NPC say: hmm.  I'm not sure how you knew I could translate these, but I can always use the gold.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 18808, item2 = 18809, item3 = 18810, gold = 20}))`
    - event_trade NPC say: Here is your translation.
50. highpass/"Stanos Herkanor", hand "Translated Parchment" (18961). Gives "Sealed Box" (28057).
    - event_trade NPC say: Let me see what you have here. Aha, so that's who.. yes, yes! There is one more thing I need you to do. This document tells me who the originator of the plot really was. His name is General V'ghera, which is interesting, as Anson's men have spotted him in Kithicor recently. He will not be easy to get to, but if you give this box to one of his many aides, the General will HAVE to come to investigate. You see, this box used to contain the tools crafted for the assassination. When he arrives, kill him! I need any documents you find on him - with luck it will be enough evidence to convince Hanns that what I say is true. Bring any documents or dispatch cases you find, along with those blades Vilnius made you work so hard for, and we will make a trade.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 18961}))`
51. kithicor/"Adjutant D-Kan", hand "Sealed Box" (28057).
    - event_item NPC say: The General will take care of you!
      - Event guard: `(plugin::check_handin(\%itemcount, 28057 => 1))`
52. Spawns "General V`ghera" (npc:20205) after the hand-in.
53. Kill "General V`ghera" (NPC 20205) in `kithicor` and loot "General's Pouch" (28013).
54. Loot "Fleshripper" (5411) from "Solusek kobold king" (NPC 32066) in `soldungb`. Drop cache: 50% chance per kill.
55. Loot "Painbringer" (5410) from "kobold champion" (NPC 32045) in `soldungb`. Drop cache: 25% chance per kill.
56. Loot "Mithril Two-Handed Sword" (5401) from "the froglok king" (NPC 66159) in `gukbottom`. Drop cache: 25% chance per kill.
57. Loot "Gigantic Zweihander" (5308) from "Karg IceBear" (NPC 30100) in `everfrost`. Drop cache: 25% chance per kill.
58. qey2hh1/"Vilnius The Small", hand "Fleshripper" (5411) + "Painbringer" (5410) + "Mithril Two-Handed Sword" (5401) + "Gigantic Zweihander" (5308). Gives "Jagged Diamond Dagger" (7506).
    - event_trade NPC say: Very good, though how you managed to lug around all these oversized blades amazes me. I feel we can do business now, and Malka still has not shown up. Take this dagger. I had an old client who didn't, um.. pay.. so this was extracted from him. Right after it was inserted in him. For your next job, I need a collection of robes. The Robe of the Ishva, some Shining Metallic robes, an Oracle robe, and a Robe of the Kedge. I am not even sure where all these come from, but they are on my list here, and Rokyl is one of my best clients, so I figure that is your job.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 5411,item2 = 5410,item3 = 5401,item4 = 5308}))`
59. Kill "General V`ghera" (NPC 20205) in `kithicor` and loot "Cazic Quill" (7505).
60. highpass/"Stanos Herkanor", hand "General's Pouch" (28013) + "Jagged Diamond Dagger" (7506) + "Cazic Quill" (7505). Gives "Ragebringer" (11057).
    - event_trade NPC say: Very well done. I leave now to confront Hanns with this evidence. Even so, it will not be easy to regain his trust. That is why I need those daggers, in case all else fails. Bristlebane grant me luck - I can no longer live like a hunted dog. In any case, I am grateful for your aid. Take this wretched blade, I can bear it no longer. I must warn you, I feel it carries Innoruuk's curse; all who are near it learn the meaning of hate. Ironic, isn't it? You went to all that work to redeem yourself for a rapier, yet the true reward came when you redeemed another..Good luck, , for much as I, you will need it.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 28013,item2 = 7506,item3 = 7505}))`
61. highpass/"Stanos Herkanor", say "Hail". Sets `Fatestealer` to `1`.
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
62. **Unverified quest flag:** `Fatestealer_gal` `==1` required.
63. **Unverified quest flag:** `Fatestealer_mar` `==1` required.
64. **Unverified quest flag:** `Fatestealer_lyt` `==1` required.
65. Loot "Signed Agreement" (10239) from "Seana Marsinger" (NPC 54102) in `gfaydark`. Drop cache: 100% chance per kill.
66. Loot "Signed Agreement" (52416) from "Stefan Marsinger" (NPC 54101) in `gfaydark`. Drop cache: 100% chance per kill.
67. overthere/"Inem R`Ker", hand "Signed Agreement" (10239) + "Signed Agreement" (52416).
    - event_trade NPC say: Those Marsingers won't be speaking ill about us again anytime soon.
      - Event guard: `(qglobals["Fatestealer"] == "1" and item_lib.check_turn_in(e.trade, {item1 = 10239,item2 = 52416}))`
    - event_trade NPC say: That should do the trick. I think our contact will speak with you now. His name is Lirpin, and he is a paladin that works for the Wayfarer's Brotherhood. I hear he led an expedition into Kuua recently, but his current location is anyone's guess. Good Luck.
      - Event guard: `(qglobals["Fatestealer_gal"] == "1" and qglobals["Fatestealer_mar"] == "1" and qglobals["Fatestealer_lyt"] == "1")`
68. Loot "Stack of Pages" (52335) from "a Teir`Dal guardian".
69. steamfont/"Yendar Starpyre", hand "Stack of Pages" (52335).
    - event_item NPC say: Splendid! The missing pages I had been looking for! Allow me a moment to sift through them.' He scans the texts line by line, flipping quickly from one sheet of parchment to another. Withdrawing a quill he quickly makes notes in the margins, then snatches your journal and copies the notes there. 'Yes, it is exactly as I had predicted. These texts detail the process by which an object can be imbued with a tortured soul. Unfortunately the focus is mostly on weaponry, which doesn't interest me in the slightest. Ah well. Appreciate the effort, $name. Perhaps it will come in handy for you. Farewell and good luck.
      - Event guard: `(plugin::check_handin(\%itemcount, 52335 => 1))`
    - event_item NPC message: You have learned how to imbue a blade with dark energy.
70. Spawns "a furious magma guardian" (npc:278123) via `soldungc/ #signal:100`.
71. Kill "a furious magma guardian" (NPC 278123) in `soldungc` and loot "Crystallized Shard of Doomfire" (21339).
72. Loot "Foul Doomfire Brimstone" (21342) from "a pool of living lava" (NPC 278043) in `soldungc`. Drop cache: 15.9687% chance per kill.
73. Loot "Igneous Rock of Doomfire" (21340) from "Typhoeus" (NPC 278069) in `soldungc`. Drop cache: 35% chance per kill.
74. Loot "Pile of Doomfire Ash" (21341) from "a Taklasinai marauder" (NPC 278075) in `soldungc`. Drop cache: 35% chance per kill.
75. soldungc/"The Firewatcher", hand "Crystallized Shard of Doomfire" (21339) + "Foul Doomfire Brimstone" (21342) + "Igneous Rock of Doomfire" (21340) + "Pile of Doomfire Ash" (21341).
    - event_trade NPC say: This should do the trick, I think! The gate is...Yes it's opening. Ha ha! The Gatekeeper comes!
      - Event guard: `(qglobals["Fatestealer_culth"] == "1" and not el:IsMobSpawnedByNpcTypeID(278005))`
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 21339,item2=21342,item3=21340,item4=21341}))`
76. Spawns "Culthor the Gatekeeper" (npc:278005) after the hand-in.
77. Kill "Culthor the Gatekeeper" (NPC 278005) in `soldungc` and loot "Smoldering Embers of Solusek" (52346).
78. nedaria/"Smith Dandi", hand "Smoldering Embers of Solusek" (52346).
    - event_trade NPC emote: gawks in amazement.  By the Gods, where did you come by these embers? These are positively unnatural, and they bare the mark of Solusek himself!' She sprinkles a handful of the smoldering lumps into the forge and -KABOOM- a blast of incredible heat knocks you off your feet. Immediately, the metal of the forge swells and becomes white hot. 'Yep, this will do the trick,' she gloats cheerfully. The blazing heat doesnt seem to bother her.
      - Event guard: `(qglobals["Fatestealer_bard"] == "1" and item_lib.check_turn_in(e.trade, {item1 = 52346}) )`
    - event_trade NPC message: You have fueled Smith Dandi's furnace with Solusek's Embers.
79. nedaria/"Lirprin, Head Of Affairs", hand "Soulstone of Lanys" (52337). Gives "Fatestealer" (52347).
    - event_trade NPC emote: discusses the process with his assistant. She listens, nodding, then begins work immediately. She takes measurements of your hands and fashions the grip so that it's a perfect fit, then turns to the hot coals of the forge. She selects a brick of fine metal. Her back to you, Dandi hammers away at the metal, sparks flying in all directions. When the job is completed she hands you the blade, still warm. 'Best work I've ever done. I hope it serves you well. Unfortunately the metal I have to work with isn't the recommended 'Velixite'. Based on the description I used the closest thing we have. Also, without an example to work from I had to improvise on a few details that weren't fully described in your documentation.
      - Event guard: `( qglobals["Fatestealer_bard"] == "1" and qglobals["Fatestealer_page"] == "1" and qglobals["Fatestealer_forge"] == "1" and item_lib.check_turn_in(e.trade, {item1 = 52337}) )`
    - event_trade NPC message: You have gained 5 ability points!
80. nedaria/"Lirprin, Head Of Affairs", say "Hail". Sets `Fatestealer` to `3`.
    - Player: "hail"
      - NPC say: I suppose the bad publicity surrounding your organization has subsided to the point where we can speak freely.' He clears his throat, 'Word is that you are looking for someone to forge a blade or two specifically for you for a specific purpose. I'll go on faith that you intend to use this weapon to catch a criminal and not become one yourself. We have the ability. My assistant, Dandi, is the best smith I know. And . . . As luck would have it I owe your friends a [favor]. The only thing we lack is the knowledge of how to imbue the weapon with dark energy. I thought this secret lied in the hands of the Teir`dal, but if they will not acquiesce perhaps there is another way. Did you ever stop to think that the directions may have been written down somewhere?
      - Condition: `(qglobals["Fatestealer"] == "1" and qglobals["Fatestealer_bard"] == "1" and e.message:findi("hail"))`
81. Loot "Polished Bone Horn" (52349) from "a baleful stoneworker" (NPC 301023) in `bloodfields`. Drop cache: 4% chance per kill.
82. Loot "Brass Mouthpiece" (52350) from "an ukun fleshhound" (NPC 301009) in `bloodfields`. Drop cache: 3.672% chance per kill.
83. Loot "Bucket Mute" (52351) from "an ukun fleshhound" (NPC 301009) in `bloodfields`. Drop cache: 3.672% chance per kill.
84. Loot "Thin Leather Straps" (52352) from "an ukun fleshhound" (NPC 301009) in `bloodfields`. Drop cache: 3.672% chance per kill.
85. bloodfields/"Caller Donivin", hand "Polished Bone Horn" (52349) + "Brass Mouthpiece" (52350) + "Bucket Mute" (52351) + "Thin Leather Straps" (52352).
86. Spawns "a reclusive girplan" (npc:301033) after the hand-in.
87. Kill "a reclusive girplan" (NPC 301033) in `bloodfields` and loot "Jacinth" (10053).
88. freeporteast/"Wenden Blackhammer", hand "Unjeweled Dragon Head Hilt" (20668) + "Diamond" (10037) + "Black Sapphire" (10036) + "Jacinth" (10053). Gives "Jeweled Dragon Head Hilt" (20671).
    - event_trade NPC emote: begins to fiddle with the hilt, gently pressing the gems into place. It seems to take forever as you watch in silence. Wenden slowly places the last gem in place and gently bends the settings to hold the gems before he hands it back to you. 'That's a very impressive looking hilt there. The material it is made out of seems strangely familiar,' Wenden says as he turns back to his forge and his other work.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 20668,item2 = 10037,item3 = 10036,item4 = 10053}))`
89. Collect ground spawn "Severely Damaged Dragon Head Hilt" (20669) in `timorous`.
90. Loot "Giant Sized Monocle" (20678) from "a mountain giant patriarch" (NPC 86144) in `dreadlands`. Drop cache: 30% chance per kill.
91. frontiermtns/"Mentrax Mountainbone", hand "Giant Sized Monocle" (20678). Gives "Rejesiam Ore" (20666).
    - event_item NPC say: Eh, you actually found one! Thank you, $name. Here is a block of ore for you. Just don't let the other giants know.
      - Event guard: `(plugin::check_handin(\%itemcount, 20678 => 1))`
92. Loot "Ball of Everliving Golem" (20677) from "Dread" (NPC 72000) in `fearplane`. Drop cache: 10.4954% chance per kill.
93. freeporteast/"Wenden Blackhammer", hand "Severely Damaged Dragon Head Hilt" (20669) + "Rejesiam Ore" (20666) + "Ball of Everliving Golem" (20677). Gives "Finely Crafted Dragon Head Hilt" (20672).
    - event_trade NPC emote: works his magic with his forge as you have never seen done quite like this. The bending and shaping to repair the hilt is only something a master of his art could even fathom to try. Once the hilt has been cooled in a near by bucket of ice cold water, he checks it for balance and resonance before handing it to you.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 20669,item2 = 20666,item3 = 20677}))`
94. Combine in "Red Scabbard" (17859): "Ancient Sword Blade" (20667), "Ancient Blade" (20670), "Jeweled Dragon Head Hilt" (20671), "Finely Crafted Dragon Head Hilt" (20672). Produces "Jagged Blade of War" (10908). Requires Remove Traps.

**Unresolved graph dependencies:**
- Unverified quest flag `Fatestealer_gal` ==1: no acyclic setter
- Unverified quest flag `Fatestealer_mar` ==1: no acyclic setter
- Unverified quest flag `Fatestealer_lyt` ==1: no acyclic setter

## Epic 1.5

### "Champion's Sword of Eternal Power" (60321)

<a id="epic-item-60321"></a>

1. Loot "Champion's Sword of Eternal Power" (60321) from "Krekk Brimblade" (NPC 336091) in `dranik`. Drop cache: 100% chance per kill.

## Epic 2.0

### "Kreljnok's Sword of Eternal Power" (60332)

<a id="epic-item-60332"></a>

**Earlier reward routes required by this graph path:** ["Champion's Sword of Eternal Power" (60321)](#epic-item-60321).
Revisit those instructions if another copy of a consumed item is needed.

1. iceclad/"Fazzle Thumpkin", say "Hail".
    - Player: "hail"
      - NPC say: Damnable interruptions! Can't you see I'm looking for my pestle?! I lost that blasted thing months ago and haven't been able to find it! What will I do without my pestle?! My poor, poor pestle. Where have you gone? I thought I'd lost it around here somewhere, but maybe I left it near one of those statues during my surveying of the islands. Drat and double drat! Where did I leave you? Woe...
        - Reply guard: `(qglobals["warrior_epic"] == "17")`
      - Condition: `(e.other:Class() == "Warrior")`
      - Condition: `(e.message:findi("hail"))`
2. Spawns "Korbuk" (npc:303128) via `causeway/warr trap#enter`.
3. Spawns "Essence of Kreljnok" (npc:303129) via `causeway/korbuk brimblade#event_death_complete`.
4. Kill "Essence of Kreljnok" (NPC 303129) in `causeway` and loot "Brimblade's Scabbard" (60331).
5. Kill "Essence of Kreljnok" (NPC 303129) in `causeway` and loot "Kreljnok's Essence" (60330).
6. **Unverified quest flag:** `warrior_epic` `>=18` required.
7. global/"Global Player", say "Recipe:19908". Gives "Globe of Discordant Energy" (47100).
8. draniksscar/"Korbuk Brimblade", hand "Globe of Discordant Energy" (47100).
    - event_trade NPC say: Yes, this is precisely what I felt. Its power is indescribable. We're so close now! I can see what's left and it's a glorious end to a glorious journey. There are just two [last items] you need to take care of.
      - Event guard: `(qglobals["warrior_epic"] ~= nil)`
      - Event guard: `(qglobals["warrior_epic"] >= "18" and item_lib.check_turn_in(e.trade, {item1 = 47100}))`
9. Loot "Kreljnok's Muddled Rage" (60322) from "Possessed Brute" (NPC 316057) in `provinggrounds`. Drop cache: 90.083% chance per kill.
10. draniksscar/"Korbuk Brimblade", hand "Kreljnok's Muddled Rage" (60322).
    - event_trade NPC say: All too easy. For you, I mean. You did well. I'm... I'm getting unclear visions from this essence. I can't seem to understand what it's trying to tell me. This essence is impure and needs to be purified. I happen to know of a [purification expert] dat can help us clear this mystery up.
      - Event guard: `(qglobals["warrior_epic"] ~= nil)`
      - Event guard: `(qglobals["warrior_epic"] >= "16" and item_lib.check_turn_in(e.trade, {item1 = 60322}))`
11. Collect ground spawn "Frozen Pestle" (60323) in `iceclad`.
12. iceclad/"Fazzle Thumpkin", hand "Frozen Pestle" (60323).
    - event_trade NPC say: You... you found it! My pestle! Hooray! I can get back to my work! I'm so grateful for this kind act, I've got to have something in my knapsack that you want! Here, how about some lint... wait, how did that get in there. You don't want lint! Hah! How about some cogs? No, what would you do with cogs? I know... you'll be able to make special use of this [map] I have.
      - Event guard: `(qglobals["warrior_epic"] == "17" and item_lib.check_turn_in(e.trade, {item1 = 60323}))`
13. iceclad/"Fazzle Thumpkin", say "Map". Gives "Fazzle's Map of East Wastes" (60324).
    - Player: "map"
      - NPC say: I've had this map for a long time. I can't seem to remember who gave it to me. I may have even made it myself. I do remember that something special can be found by following where the map leads. It's a magical map and will only show you the way in the dead of night, and only in the eastern wastes of this dreadful ice-covered place. You have to hold onto it tightly for it to work, keep that in mind! Good luck, you may need it!
      - Condition: `(e.other:Class() == "Warrior")`
      - Condition: `(e.message:findi("map") and qglobals["warrior_epic"] == "18")`
14. Spawns "Larnik the Recluse" (npc:116609) via `eastwastes/warr trap#enter`.
15. Kill "Larnik the Recluse" (NPC 116609) in `eastwastes` and loot "Larnik's Locked Purification Kit" (60325).
16. draniksscar/"Korbuk Brimblade", hand "Larnik's Locked Purification Kit" (60325). Gives "Larnik's Unlocked Purification Kit" (60326).
    - event_trade NPC say: Uh oh. I'm guessing dat he didn't want to part with this peacefully? Well, I can't say I'm sorry. He was a jerk to me da last time we talked. I guess I just figured someone else might be able to persuade him to change his mind. I went ahead and broke open da lock for you. You'll be able to make use of da [kit] now.
      - Event guard: `(qglobals["warrior_epic"] ~= nil)`
      - Event guard: `(qglobals["warrior_epic"] >= "18" and item_lib.check_turn_in(e.trade, {item1 = 60325}))`
17. Combine in "Larnik's Unlocked Purification Kit" (60326): "Kreljnok's Muddled Rage" (60322). Produces "Kreljnok's Focused Rage" (60327). Requires Remove Traps.
18. draniksscar/"Korbuk Brimblade", hand "Champion's Sword of Eternal Power" (60321) + "Kreljnok's Focused Rage" (60327). Gives "Raging Sword of Eternal Power" (60329).
    - event_trade NPC say: Well done. Well done, indeed. I knew da moment I saw you dat you were da right person for all of this. Here is da sword, but there's one [last item] dat you need to do.
      - Event guard: `(qglobals["warrior_epic"] ~= nil)`
      - Event guard: `(qglobals["warrior_epic"] >= "19" and item_lib.check_turn_in(e.trade, {item1 = 60321, item2 = 60327}))`
19. Combine in "Brimblade's Scabbard" (60331): "Kreljnok's Essence" (60330), "Raging Sword of Eternal Power" (60329). Produces "Kreljnok's Sword of Eternal Power" (60332). Requires Remove Traps.

**Unresolved graph dependencies:**
- Unverified quest flag `warrior_epic` >=18: no acyclic setter
