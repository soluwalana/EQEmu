# Berserker — Epic Quest Walkthrough

Generated directly from quest-graph item rewards. Unresolved dependencies are marked, not inferred.

## Epic 1.0

### "Kerasian Axe of Ire" (68299)

<a id="epic-item-68299"></a>

1. lakeofillomen/"Keras Mcarik", say "Hail".
    - Player: "hail"
      - NPC emote: eyes your axe in a somewhat awe-stricken fashion. 'What have ye got there? Let me take a look at that! You stride up to Keras and proudly outstretch your finished Axe but notice that it takes Keras a moment before he realizes that you've even arrived. 'Ach. . .sorry lad. Let's have a look, shall we?' Keras begins to carefully examine the axe, each step of the way nodding approvingly. 'This is truly excellent work. Teekan has never let me down. This axe is possibly the highest quality that I have ever seen and should serve ye well in ye travels.' As he hands you the axe back, you once again notice a deep concern growing over his countenance. 'I am sorry that I canna' spend more time wit ye but ye've no doubt noticed that as of late, I've been troubled.
      - Condition: `(defined $qglobals{berserk_epic} && $qglobals{berserk_epic} >=7)`
      - Condition: `($text=~/hail/i)`
2. Loot "Treanik's Tarnished Axe" (60200) from "praklion of the cauldron" in `cauldron`.
3. cauldron/"Treanik Ireblade", hand "Treanik's Tarnished Axe" (60200). Gives "Bone Trinket" (60201).
    - event_trade NPC say: My axe! Me so happy! You are big force to be rekoned with, . Me wasn't sure... but now, look at you, like spiroc fluffing feathers. McArik be so pleased! Take dis amulet me made. I know not much, but me swore to McArik that anyone who passes dis test would get a trinket from me.
      - Event guard: `item_lib.check_turn_in(e.trade, {item1 = 60200})`
4. fieldofbone/"Mardic Crimsonsteel", say "Hail". Gives "Image Essence" (60196).
    - Player: "hail"
      - NPC say: Hail, , Run along and give McArik the items he requested.
        - Reply guard: `(qglobals["bersolo"] == "1" and e.other:GetLevel() >= 45)`
      - NPC say: Hail to you, feared one. I see the glint of rage in them eyes of yours there. One day you'll be able to recognize the same in others. I suppose now is the time to talk to you about the mirage around here. Tell you the truth, I wasn't able to beat it myself... that's why I'm out here and not establishing myself as a berserker.
        - Reply guard: ``
      - NPC say: I wasn't meant for that path. I'm here to guide folk like yourself and help you gain control of the insane beast that lurks inside you. You must be prepared to fight one like yourself. All ye need are your wits, brawn, and skill, nought else. When you are ready give me the note McArik gave you and I'll send you to the training grounds.
        - Reply guard: ``
      - Condition: `(e.message:findi("hail"))`
5. Spawns "An Impervious Bloodbeast" (npc:85225) via `lakeofillomen/lingering axefall#defeat`.
6. Kill "An Impervious Bloodbeast" (NPC 85225) in `lakeofillomen` and loot "Bloodbeast Tooth" (60192).
7. lakeofillomen/"Keras Mcarik", say "Great Stride". Gives "Medal of Blood" (60190).
    - Player: "great stride"
      - NPC say: Ye do understand there is no turning back? I hope so. This is a journey -- and sometimes a long one -- depending on what ye've leared so far. Yer skills and wisdom in battle will be tested. Go talk to an old, fallen friend of mine, Lingering Axefall. We call him that because he reguses to let his spirit rest. He failed his task and remains bound here to lead others into the trial he lost. Be wary, though. He is elusive.
      - NPC say: The foe he stood against and lost to still wishes to extinguish his spirit. Take this axe and give it to him so he will know that ye are ready for the test and that I sent ye. Also, take this medal with you. It will help me keep track of your progress. Best of luck, friend.
      - Condition: ``
      - Condition: `($text=~/great stride/i && $class eq "Berserker" && $ulevel > 45 && $dragon == undef && $imp == undef)`
      - Linked from "master the fires" (explicit prompt).
8. lakeofillomen/"Keras Mcarik", hand "Bloodbeast Tooth" (60192) + "Medal of Blood" (60190). Gives "Medal of Mirages" (60194).
    - event_item NPC say: Aye, ye have done well, $name. However, that was a simple task and I'm sure ye had much help with it. Now ye must go alone. Ye may want to take some bandages with ye and be sure yer skill with them is top-notch. Ye'll likely need 'em. Here, take some o'mine. Ye may find 'em to be most useful. Do ye believe ye're [ready for this challenge]
      - Event guard: `(plugin::check_handin(\%itemcount, 60192 => 1, 60190 => 1))`
9. lakeofillomen/"Keras Mcarik", hand "Image Essence" (60196) + "Medal of Mirages" (60194). Gives "Medal of Strategy" (60198).
    - event_item NPC say: Well, I am indeed hopeful and pleased about yer progress, $name. Ye should be proud that you have now attained the Medal of Strategy. Well done, indeed! It seems that ye can best yer equal now. The next test of yer masters of yer abilities is much more difficult, however, and may require ye to ask yer friends for some 'elp... but it must be the right kind of 'elp. This test will determine how well ye [strategize in battle]. Ye must gather trustworthy friends and they must be willing to work under yer command.
      - Event guard: `(plugin::check_handin(\%itemcount, 60196 => 1, 60194 => 1))`
10. lakeofillomen/"Keras Mcarik", hand "Bone Trinket" (60201) + "Medal of Strategy" (60198). Gives "Medal of Fervid Rage" (60202).
    - event_item NPC say: Ye are well on the way, me friend. I knew the moment I saw ye that ye were going to get through this. I'm just not convinced that yer as powerful as even ye may think. So, are ye [ready] for the next trial ye must face?
      - Event guard: `(plugin::check_handin(\%itemcount, 60201 => 1, 60198 => 1))`
11. Kill fearplane/"A Scareling".
12. Spawns "Ireblind Imp" (npc:72069) via `fearplane/enraged imp#event_death_complete`.
13. Kill "Ireblind Imp" (NPC 72069) in `fearplane` and loot "Burning Essence of Rage" (60203).
14. lakeofillomen/"Keras Mcarik", hand "Medal of Fervid Rage" (60202) + "Burning Essence of Rage" (60203). Gives "Medal of Hunting" (60204).
    - event_item NPC say: I am indeed impressed by yer control and ability to best such a horrific beast, my friend. Ye are certainly well on yer way to mastering yer rage and taking advantage of the abilities ye were born with. Here is your Medal of Hunting. Ye are nearly there -- nearly complete with yer trials, but there are a few more things ye [must do] for me. 
      - Event guard: `(plugin::check_handin(\%itemcount, 60202 => 1, 60203 => 1))`
15. lakeofillomen/"Keras Mcarik", say "Do". Gives "McArik Reagent Satchel" (60205).
    - Player: "do"
      - NPC say: For my mirage to remain part of my trials, I need some very specific reagents. There is a sickly gorilla that carries a rotting organ which I am in need of. Also, I need a paw of a very special and dangerous kobold. Lastly, bring me the poison sac of a dangerous spider. A potion that allows us to create a gate from one place to another is also required. If ye believe ye can do this for me, tell me so, and I will give ye a bag to hold them in. When ye have all of the ingredients, combine them in the bag I've given ye, and bring it back to me. Good luck in your hunt!
      - Condition: ``
      - Condition: `($text=~/do/i && ($hunting == 1 || plugin::check_hasitem($client,60204)))`
      - Linked from "metal" (explicit prompt).
      - Linked from "troubled" (explicit prompt).
      - Linked from "master the fires" (explicit prompt).
      - Linked from "great stride" (explicit prompt).
      - Linked from "challenge" (explicit prompt).
      - Linked from "ready" (explicit prompt).
      - Linked from "never control the rage" (explicit prompt).
      - Linked from "face one" (explicit prompt).
      - Linked from "next challenge" (explicit prompt).
      - Linked from "next test" (explicit prompt).
16. Loot "Decaying Liver" (60206) from "Disease-Ridden Gorilla" (NPC 94130) in `emeraldjungle`. Drop cache: 100% chance per kill.
17. Loot "Gnashing Kobold Paw" (60207) from "Gnashing Kobold" (NPC 100166) in `stonebrunt`. Drop cache: 80% chance per kill.
18. Loot "Scent Gland" (60208) from "Reeking Skunk" (NPC 38047) in `tox`. Drop cache: 100% chance per kill.
19. Buy "Medicine Bag" (17901) from "Rendallen Ironforge" (NPC 2071) in `qeynos2`. Base price: 1,000 copper.
20. Buy "Handful of Prism Grains" (95922) from "Murak" (NPC 49085) in `oggok`. Base price: 800 copper.
21. Loot "Heliotrope" (14242) from "a Sarnak Herb Collector" (NPC 103012) in `chardok`. Drop cache: 4.3204% chance per kill.
22. Buy "Yebamante" (16510) from "Guri" (NPC 30098) in `everfrost`. Base price: 25,000 copper.
23. Buy "Blade Leaf" (22143) from "Guri" (NPC 30098) in `everfrost`. Base price: 2,500 copper.
24. Buy "Simple Potion Vial" (95843) from "Guri" (NPC 30098) in `everfrost`. Base price: 750 copper.
25. Combine in "Medicine Bag" (17901): "Handful of Prism Grains" (95922), "Heliotrope" (14242), "Yebamante" (16510), "Blade Leaf" (22143), "Simple Potion Vial" (95843). Produces "Philter of Major Translocation" (96467). Requires Alchemy.
26. Combine in "McArik Reagent Satchel" (60205): "Decaying Liver" (60206), "Gnashing Kobold Paw" (60207), "Scent Gland" (60208), "Philter of Major Translocation" (96467). Produces "Bag of Image Essence Dust" (60209). Requires Remove Traps.
27. lakeofillomen/"Keras Mcarik", hand "Bag of Image Essence Dust" (60209) + "Medal of Hunting" (60204). Gives "Medal of Mastery" (60210).
    - event_item NPC say: Wonderful. Ye have earned yer Medal of Mastery, but ye are not done yet. There is one final test ye must complete before I can recognize ye as a true berserker. Ye must prove that in the face of great adversity, ye can keep yer wits about ye. This final test, naturally, is the most difficult, but I would not present this [next challenge] to ye if I thought ye could not finish yer journey.
      - Event guard: `(plugin::check_handin(\%itemcount, 60209 => 1, 60204 => 1))`
28. Spawns "Raving Goblinmaster - KOS" (npc:79126) via `warslikswood/npc:79127#event_waypoint_arrive`.
29. Kill "Raving Goblinmaster - KOS" (NPC 79126) in `warslikswood` and loot "Maniac's Garbled Tome" (60211).
30. lakeofillomen/"Keras Mcarik", hand "Medal of Mastery" (60210) + "Maniac's Garbled Tome" (60211). Gives "Kerasian Axe of Ire" (68299).
    - event_item NPC say: I am so impressed and proud of ye, $name. This had been a long journey, hasn't it? That said, this will be the most important adventure of yer life, for now you are a true berserker and a master of all of yer skills. As I promised, the completion of these trials would not only bring ye the honor of being recognized as a true berserker, but also a weapon only a true berserker can wield -- one that I fashioned myself. Use this weapon in yer travels and may it serve ye well in battle. Be well,$name, the Berserker.
      - Event guard: `(plugin::check_handin(\%itemcount, 60210 => 1, 60211 => 1))`

## Epic 1.5

### "Raging Taelosian Alloy Axe" (18398)

<a id="epic-item-18398"></a>

**Earlier reward routes required by this graph path:** ["Kerasian Axe of Ire" (68299)](#epic-item-68299).
Revisit those instructions if another copy of a consumed item is needed.

1. sebilis/"Berserkerepic 1 5", say "Protector_Timer". Gives "Taelosian Alloy Blood Axe" (18976).
2. halas/"Shanis Macdarren", say "Hail". Gives "Raging Soul Shard" (11999).
    - Player: "hail"
      - NPC emote: looks around briefly, 'It's a great day out here today, it almost makes me want to be out on the tundra enjoying it!' She continues to admire the day for a moment more. 'What can I help you with today? What's that? Something about your soul gem? Hmm . . . Let's see what we can do here. Here you go, but please take care of this one, they are not easy to create. You may wish to seek out Keras. He will be interested in one so young as you who has begun the process of learning to control and focus their rage.'
        - Reply guard: `(defined $qglobals{berserk_epic} && $qglobals{berserk_epic} >= 1)`
      - NPC say: Why, as I live and breathe this frigid air, have ye come to join our fine guild of berserkers?  The Bloodrage Brawlers are a fearsome collection of berserkers, indeed, me friend.  If ye be interested in joinin' up with us, read the note in yer inventory and then hand it to me!  Oh, and don't ye be forgetin' to ask me about that [tome] in yer inventory if ye want ta learn to use it!
        - Reply guard: `($qglobals{berserk_epic} == undef)`
      - Condition: `($text =~ /hail/i)`
3. lakeofillomen/"Keras Mcarik", hand "Taelosian Alloy Blood Axe" (18976) + "Broken Trial Taelosian Blood Axe" (17833) + "Damaged Trial Taelosian Blood Axe" (17898) + "Damaged Trial Taelosian Blood Axe" (17399).
    - event_item NPC emote: grabs each axe individually and mutters something inaudible. He takes each axe in his hands and looks them over. 'This axe seems to display almost no wear, which is highly unusual, given the amount of punishment ye must have put it through. Surely all three of these axes are of higher quality than the ones we normally make, but this one is vastly superior. Given the quality of this axe, I'd say that it could very easily benefit from some enchantments. So the next step in this axe's journey should be to imbue it with some of the owner's essence. This will create an axe that can actually become aware of its owner's wishes to help him realize his true Berserker's potential. Why if I were the owner and had a rare Soul Gem handy, I'd be headin' off to Teekan the Enchanter in the Abysmal Sea. Her abilities to weave such magic are unsurpassed.
      - Event guard: `(plugin::check_handin(\%itemcount, 18976 => 1, 17833 => 1, 17898 => 1, 17399 => 1))`
4. abysmal/"Teekan Opousbabolaoi", hand "Taelosian Alloy Blood Axe" (18976) + "Raging Soul Shard" (11999). Gives "Raging Taelosian Alloy Axe" (18398).
    - event_trade NPC emote: takes the axe and the Soul Gem and begins the chant in low, near inaudible tones. Smoke begins to swirl around the axe as the orb twists and writhes like a serpent around the haft of the axe, melding itself to the dark wooden handle. When the smoke clears, she hands the axe back to you and says, 'This should be what you're looking for! Be sure to show this to Keras and give him my regards. Tell him he should stop by and visit sometime!
      - Event guard: `qglobals["berserk_epic"] == "5" and item_lib.check_turn_in(e.trade, {item1 = 18976, item2 = 11999})`
    - event_trade NPC message: You have gained 5 ability points!

## Epic 2.0

### "Vengeful Taelosian Blood Axe" (18609)

<a id="epic-item-18609"></a>

**Earlier reward routes required by this graph path:** ["Raging Taelosian Alloy Axe" (18398)](#epic-item-18398).
Revisit those instructions if another copy of a consumed item is needed.

1. Loot "Lightning Core" (72029) from "a lightning warrior stormer" (NPC 317083) in `anguish`. Drop cache: 0.4998% chance per kill.
2. Spawns "Bazu Smasher" (npc:303081) via `causeway/bazu smasher#timer:wipecheck`.
3. Kill "Bazu Smasher" (NPC 303081) in `causeway` and loot "Faceted Moonstone" (17349).
4. Loot "Shadowed Bronze Lump" (17137) from "an ancient necromantic shade" (NPC 163052) in `griegsend`. Drop cache: 100% chance per kill.
5. lakeofillomen/"Keras Mcarik", hand "Lightning Core" (72029) + "Raging Taelosian Alloy Axe" (18398) + "Faceted Moonstone" (17349) + "Shadowed Bronze Lump" (17137). Gives "Unhoned Vengeful Taelosian Blood Axe" (20072).
    - event_item NPC say: Ah ye've returned with the necessary components, me friend? Give me but a moment to look over what you've managed to get yer hands on. Yes, these should do the job quite nicely. We'll see just what potential can be unleashed in this axe of yours! So the Dragorn smith said to reinforce the haft with this ore, eh? I can accomplish that surely. Work with the Moonstone should be easy enough tew as it don't seem to require much enchantment from me. The Lightning Core will require a bit o' work though as I'm not very experienced with it. Still though, I can surely do something with it. I would na ever thought of using one of these on an axe though! Crafty Gnomes indeed.' After some time and a bit of effort, Keras hands you back your axe. 'Here ya go, lad. I tried honing the edge further but I dinnah have a whetstone strong enough. Maybe that smith o' yours can help ye futher?
      - Event guard: `(plugin::check_handin(\%itemcount, 72029 => 1, 18398 => 1, 17349 => 1, 17137 => 1))`
6. global/"Global Player", say "Recipe:19908". Gives "Globe of Discordant Energy" (47100).
7. lakeofillomen/"Keras Mcarik", say "Find Out". Sets `berserk_epic` to `8`.
    - Player: "find out"
      - NPC say: I dinnah not exactly know where she may be, but her name is Julei Direaxe and I fear that she may be in trouble. Please, hurry, strike out and find her, rescue her from any troubles she may be in. Return her to safety and bring me proof that she is alright and ye shall forever have me gratitude.
      - Condition: `(defined $qglobals{berserk_epic} && $qglobals{berserk_epic} >=7)`
      - Condition: `($text=~/find out/i && $qglobals{berserk_epic}==7)`
      - Linked from "troubled" (explicit prompt).
8. hole/"Julei Direaxe", say "Hail". Gives "Julei's Twilight Pendant" (17200).
    - Player: "hail"
      - NPC emote: ignores you and continues to move forward
        - Reply guard: `ignoreplayer==0`
      - NPC say: Here take this back to Keras. This should be proof enough that I am fine. My thanks to you berserker. May you honor the path.
        - Reply guard: ``
      - Condition: `(qglobals["berserk_epic"] == "8" and e.message:findi("hail") and ignoresay==0)`
9. lakeofillomen/"Keras Mcarik", hand "Julei's Twilight Pendant" (17200).
    - event_item NPC emote: 's demeanor quickly changes from one fraught with worry and guilt to one of relief. 'Ach! Julei is in good health. Tis good news indeed! My thanks to ye. If'in there be anything I can do for ye, ask and ye shall have it.
      - Event guard: `(plugin::check_handin(\%itemcount, 17200 => 1))`
10. dranik/"Grithyank Avlonnon", hand "Unhoned Vengeful Taelosian Blood Axe" (20072) + "Globe of Discordant Energy" (47100). Gives "Vengeful Taelosian Blood Axe" (18609).
    - event_trade NPC say: Ah, very good outlander, you managed to find some Discordant Matter. Very well, I will see what I can accomplish. Though the ore in this axe is originally from my world, the smithing technique and some of the magic are from yours. Therefore I can make no promises.' After some time and much effort the Dragorn hands the axe back. You immediately notice that edge has a brilliance to it that is nearly blinding. There outlander. I think you will be pleased with the results. The smithing technique used to forge that axe is quite unique. . .I doubt another of its kind exists. Be wary though for as I was applying the Discordant matter to the edge, I felt a disturbing presence emanating from the axe. There is someone or something that endures within it. . .something that seeks to control those who wield it. You must be ever cautious lest the axe is able to compel its influence onto you. I fear that though the axe will bring you many victories, those victories may come at a cost. Travel safe and fair, my friend!
      - Event guard: `(qglobals["berserk_epic"] == "9" and item_lib.check_turn_in(e.trade, {item1 = 20072, item2 = 47100}))`
    - event_trade NPC message: You have gained 10 ability points!
