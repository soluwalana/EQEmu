# Berserker

Acquisition paths traced backwards from the 1.0, 1.5 and 2.0 epic rewards. Flags are dependencies, not the definition of an epic. **Broken** indicates missing graph provenance.

## Epic 1.0

### "Kerasian Axe of Ire" (68299)

1. fieldofbone/"Mardic Crimsonsteel", say "Hail". Requires `bersolo` ==1. Gives "Image Essence" (60196).
2. Loot "Treanik's Tarnished Axe" (60200) at cauldron/"Praklion Of The Cauldron", on event_hp.
3. cauldron/"Treanik Ireblade", hand "Treanik's Tarnished Axe" (60200). Gives "Bone Trinket" (60201).
4. fieldofbone/"Berserker-S Image", on event_death_complete. Sets `bersolo` to `1`.
5. Say "Defeat" to lakeofillomen/"Lingering Axefall".
6. Spawns "An Impervious Bloodbeast" (85225).
7. Loot "Bloodbeast Tooth" (60192) from "An Impervious Bloodbeast".
8. lakeofillomen/"Keras Mcarik", say "Great Stride". Gives "Medal of Blood" (60190).
9. lakeofillomen/"Keras Mcarik", hand "Medal of Blood" (60190) + "Bloodbeast Tooth" (60192). Gives "Medal of Mirages" (60194).
10. lakeofillomen/"Keras Mcarik", hand "Medal of Mirages" (60194) + "Image Essence" (60196). Gives "Medal of Strategy" (60198).
11. lakeofillomen/"Keras Mcarik", hand "Medal of Strategy" (60198) + "Bone Trinket" (60201). Gives "Medal of Fervid Rage" (60202).
12. Kill fearplane/"Enraged Imp". Spawns "Ireblind Imp" (72069).
13. Loot "Burning Essence of Rage" (60203) from "Ireblind Imp".
14. lakeofillomen/"Keras Mcarik", hand "Medal of Fervid Rage" (60202) + "Burning Essence of Rage" (60203). Gives "Medal of Hunting" (60204).
15. lakeofillomen/"Keras Mcarik", say "Do". Gives "McArik Reagent Satchel" (60205).
16. Loot "Decaying Liver" (60206) from "Disease-Ridden Gorilla" in `emeraldjungle`.
17. Loot "Gnashing Kobold Paw" (60207) from "Gnashing Kobold" in `stonebrunt`.
18. Loot "Scent Gland" (60208) from "Reeking Skunk" in `tox`.
19. Loot "Scent Gland" (60208) from "Reeking Skunk" in `toxxulia`.
20. Buy "Medicine Bag" (17901) from "Rendallen Ironforge" (NPC 2071) in `qeynos2`. Base price: 1,000 copper.
21. Buy "Handful of Prism Grains" (95922) from "Murak" (NPC 49085) in `oggok`. Base price: 800 copper.
22. Loot "Heliotrope" (14242) from "a Di'zok Herbalist" in `chardok`.
23. Loot "Heliotrope" (14242) from "a Sarnak Herb Collector" in `chardok`.
24. Loot "Heliotrope" (14242) from "an Apprentice Herbalist" in `chardok`.
25. Buy "Yebamante" (16510) from "Guri" (NPC 30098) in `everfrost`. Base price: 25,000 copper.
26. Buy "Blade Leaf" (22143) from "Guri" (NPC 30098) in `everfrost`. Base price: 2,500 copper.
27. Buy "Simple Potion Vial" (95843) from "Guri" (NPC 30098) in `everfrost`. Base price: 750 copper.
28. Combine in "Medicine Bag" (17901): "Handful of Prism Grains" (95922), "Heliotrope" (14242), "Yebamante" (16510), "Blade Leaf" (22143), "Simple Potion Vial" (95843). Produces "Philter of Major Translocation" (96467). Requires Alchemy, trivial 131.
29. Combine in "McArik Reagent Satchel" (60205): "Decaying Liver" (60206), "Gnashing Kobold Paw" (60207), "Scent Gland" (60208), "Philter of Major Translocation" (96467). Produces "Bag of Image Essence Dust" (60209). The combine does not fail.
30. lakeofillomen/"Keras Mcarik", hand "Medal of Hunting" (60204) + "Bag of Image Essence Dust" (60209). Gives "Medal of Mastery" (60210).
31. Spawns "Raving Goblinmaster - KOS" (79126) in `warslikswood` on event_waypoint_arrive.
32. Loot "Maniac's Garbled Tome" (60211) from "Raving Goblinmaster - KOS".
33. lakeofillomen/"Keras Mcarik", hand "Medal of Mastery" (60210) + "Maniac's Garbled Tome" (60211). Gives "Kerasian Axe of Ire" (68299).

## Epic 1.5

### "Raging Taelosian Alloy Axe" (18398)

1. halas/"Shanis Macdarren", say "Hail". Requires `berserk_epic` >=1. Requires `berserk_epic` set. Gives "Raging Soul Shard" (11999).
2. sebilis/"Berserkerepic 1 5", say "Protector Timer". Gives "Taelosian Alloy Blood Axe" (18976).
3. sebilis/"Berserkerepic 1 5", say "Protector Timer". Gives "Broken Trial Taelosian Blood Axe" (17833).
4. sebilis/"Berserkerepic 1 5", say "Protector Timer". Gives "Damaged Trial Taelosian Blood Axe" (17898).
5. sebilis/"Berserkerepic 1 5", say "Protector Timer". Gives "Damaged Trial Taelosian Blood Axe" (17399).
6. lakeofillomen/"Keras Mcarik", hand "Damaged Trial Taelosian Blood Axe" (17399) + "Broken Trial Taelosian Blood Axe" (17833) + "Damaged Trial Taelosian Blood Axe" (17898) + "Taelosian Alloy Blood Axe" (18976). Sets `berserk_epic` to `5`.
7. abysmal/"Teekan Opousbabolaoi", hand "Raging Soul Shard" (11999) + "Taelosian Alloy Blood Axe" (18976). Sets `berserk_epic` to `7`.
8. Unresolved cyclic prerequisite: `berserk_epic` >=7.
9. lakeofillomen/"Keras Mcarik", say "Find Out". Sets `berserk_epic` to `8`.
10. abysmal/"Teekan Opousbabolaoi", hand "Raging Soul Shard" (11999) + "Taelosian Alloy Blood Axe" (18976). Requires `berserk_epic` ==5. Gives "Raging Taelosian Alloy Axe" (18398).

## Epic 2.0

### "Vengeful Taelosian Blood Axe" (18609)

1. halas/"Shanis Macdarren", say "Hail". Requires `berserk_epic` >=1. Requires `berserk_epic` set. Gives "Raging Soul Shard" (11999).
2. sebilis/"Berserkerepic 1 5", say "Protector Timer". Gives "Taelosian Alloy Blood Axe" (18976).
3. sebilis/"Berserkerepic 1 5", say "Protector Timer". Gives "Broken Trial Taelosian Blood Axe" (17833).
4. sebilis/"Berserkerepic 1 5", say "Protector Timer". Gives "Damaged Trial Taelosian Blood Axe" (17898).
5. sebilis/"Berserkerepic 1 5", say "Protector Timer". Gives "Damaged Trial Taelosian Blood Axe" (17399).
6. lakeofillomen/"Keras Mcarik", hand "Damaged Trial Taelosian Blood Axe" (17399) + "Broken Trial Taelosian Blood Axe" (17833) + "Damaged Trial Taelosian Blood Axe" (17898) + "Taelosian Alloy Blood Axe" (18976). Sets `berserk_epic` to `5`.
7. abysmal/"Teekan Opousbabolaoi", hand "Raging Soul Shard" (11999) + "Taelosian Alloy Blood Axe" (18976). Sets `berserk_epic` to `7`.
8. Unresolved cyclic prerequisite: `berserk_epic` >=7.
9. lakeofillomen/"Keras Mcarik", say "Find Out". Sets `berserk_epic` to `8`.
10. hole/"Julei Direaxe", say "Hail". Requires `berserk_epic` ==8. Gives "Julei's Twilight Pendant" (17200).
11. lakeofillomen/"Keras Mcarik", hand "Julei's Twilight Pendant" (17200). Sets `berserk_epic` to `9`.
12. Loot "Lightning Core" (72029) from "A Lightning Warrior Stormer" (NPC 317083) in `anguish`. Drop cache: 0.5% chance per kill.
13. abysmal/"Teekan Opousbabolaoi", hand "Raging Soul Shard" (11999) + "Taelosian Alloy Blood Axe" (18976). Requires `berserk_epic` ==5. Gives "Raging Taelosian Alloy Axe" (18398).
14. causeway/"Bazu Smasher", on event combat.
15. Starts timer `wipecheck`.
16. Spawns "Bazu Smasher" (303081) after `causeway/bazu smasher#timer:wipecheck`.
17. Loot "Faceted Moonstone" (17349) from "Bazu Smasher".
18. Loot "Shadowed Bronze Lump" (17137) from "An Ancient Necromantic Shade" in `griegsend`.
19. lakeofillomen/"Keras Mcarik", hand "Shadowed Bronze Lump" (17137) + "Faceted Moonstone" (17349) + "Raging Taelosian Alloy Axe" (18398) + "Lightning Core" (72029). Gives "Unhoned Vengeful Taelosian Blood Axe" (20072).
20. Say "Check Lorb" to anguish/"Zone Status".
21. Spawns "Orb of Discordant Energy" (317087).
22. Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy".
23. Alternative: Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy" (NPC 317087) in `anguish`; trigger: anguish/"Zone Status", say "Check Uorb".
24. Alternative: Loot "Globe of Discordant Energy" (47100) from "Ornate Chest" (NPC 317112) in `anguish`; trigger: anguish/"Zone Status", say "Check Amv Chest".
25. Alternative: Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy" (NPC 317087) in `anguish`; trigger: anguish/"Zone Status", say "Signal:999999".
26. Alternative: Loot "Globe of Discordant Energy" (47100) from "Overlords Chest" (NPC 317124) in `anguish`; trigger: anguish/"Zone Status", say "Signal:999999".
27. dranik/"Grithyank Avlonnon", hand "Unhoned Vengeful Taelosian Blood Axe" (20072) + "Globe of Discordant Energy" (47100). Requires `berserk_epic` ==9. Gives "Vengeful Taelosian Blood Axe" (18609).

## Quest-state progression

## 0. Prerequisites

Shared acquisition steps appear in the first prerequisite chain that needs them. Later sections reference that chain rather than repeating it.

### "Raging Soul Shard" (11999)

1. sebilis/"Berserkerepic 1 5", say "Protector Timer". Gives "Taelosian Alloy Blood Axe" (18976).
2. sebilis/"Berserkerepic 1 5", say "Protector Timer". Gives "Broken Trial Taelosian Blood Axe" (17833).
3. sebilis/"Berserkerepic 1 5", say "Protector Timer". Gives "Damaged Trial Taelosian Blood Axe" (17898).
4. sebilis/"Berserkerepic 1 5", say "Protector Timer". Gives "Damaged Trial Taelosian Blood Axe" (17399).
5. lakeofillomen/"Keras Mcarik", hand "Damaged Trial Taelosian Blood Axe" (17399) + "Broken Trial Taelosian Blood Axe" (17833) + "Damaged Trial Taelosian Blood Axe" (17898) + "Taelosian Alloy Blood Axe" (18976). Sets `berserk_epic` to `5`.
6. abysmal/"Teekan Opousbabolaoi", hand "Raging Soul Shard" (11999) + "Taelosian Alloy Blood Axe" (18976). Sets `berserk_epic` to `7`.
7. Unresolved cyclic prerequisite: `berserk_epic` >=7.
8. lakeofillomen/"Keras Mcarik", say "Find Out". Sets `berserk_epic` to `8`.
9. halas/"Shanis Macdarren", say "Hail". Requires `berserk_epic` >=1. Requires `berserk_epic` set. Gives "Raging Soul Shard" (11999).
    - Dialogue with halas/"Shanis Macdarren":
      - Player: "Hail"
        - NPC emote: looks around briefly, 'It's a great day out here today, it almost makes me want to be out on the tundra enjoying it!' She continues to admire the day for a moment more. 'What can I help you with today? What's that? Something about your soul gem? Hmm . . . Let's see what we can do here. Here you go, but please take care of this one, they are not easy to create. You may wish to seek out Keras. He will be interested in one so young as you who has begun the process of learning to control and focus their rage.'
          - Reply guard: `(defined $qglobals{berserk_epic} && $qglobals{berserk_epic} >= 1)`
        - NPC say: Why, as I live and breathe this frigid air, have ye come to join our fine guild of berserkers? The Bloodrage Brawlers are a fearsome collection of berserkers, indeed, me friend. If ye be interested in joinin' up with us, read the note in yer inventory and then hand it to me! Oh, and don't ye be forgetin' to ask me about that [tome] in yer inventory if ye want ta learn to use it!
          - Reply guard: `($qglobals{berserk_epic} == undef)`
        - Condition: `($text =~ /hail/i)`
        - Gives Raging Soul Shard (11999).
      - Player: "Tome" (link: explicit mention)
        - Condition: `($text =~/tome/i)`

### "Julei's Twilight Pendant" (17200)

1. hole/"Julei Direaxe", say "Hail". Requires `berserk_epic` ==8. Gives "Julei's Twilight Pendant" (17200).
    - Dialogue with hole/"Julei Direaxe":
      - Player: "Hail"
        - NPC emote: ignores you and continues to move forward
          - Reply guard: `ignoreplayer==0`
        - NPC say: Here take this back to Keras. This should be proof enough that I am fine. My thanks to you berserker. May you honor the path.
          - Reply guard: ``
        - Condition: `(qglobals["berserk_epic"] == "8" and e.message:findi("hail") and ignoresay==0)`
        - Gives Julei's Twilight Pendant (17200).

### "Unhoned Vengeful Taelosian Blood Axe" (20072)

1. Loot "Lightning Core" (72029) from "A Lightning Warrior Stormer" (NPC 317083) in `anguish`. Drop cache: 0.5% chance per kill.
2. Acquisition of "Taelosian Alloy Blood Axe" (18976) is documented under "Raging Soul Shard" (11999); obtain another copy if needed.
3. Acquisition of "Raging Soul Shard" (11999) is documented under "Raging Soul Shard" (11999); obtain another copy if needed.
4. abysmal/"Teekan Opousbabolaoi", hand "Raging Soul Shard" (11999) + "Taelosian Alloy Blood Axe" (18976). Requires `berserk_epic` ==5. Gives "Raging Taelosian Alloy Axe" (18398).
5. causeway/"Bazu Smasher", on event combat.
6. Starts timer `wipecheck`.
7. Spawns "Bazu Smasher" (303081) after `causeway/bazu smasher#timer:wipecheck`.
8. Loot "Faceted Moonstone" (17349) from "Bazu Smasher".
9. Loot "Shadowed Bronze Lump" (17137) from "An Ancient Necromantic Shade" in `griegsend`.
10. lakeofillomen/"Keras Mcarik", hand "Shadowed Bronze Lump" (17137) + "Faceted Moonstone" (17349) + "Raging Taelosian Alloy Axe" (18398) + "Lightning Core" (72029). Gives "Unhoned Vengeful Taelosian Blood Axe" (20072).

### "Medal of Mastery" (60210)

1. Loot "Treanik's Tarnished Axe" (60200) at cauldron/"Praklion Of The Cauldron", on event_hp.
2. cauldron/"Treanik Ireblade", hand "Treanik's Tarnished Axe" (60200). Gives "Bone Trinket" (60201).
    - Dialogue with cauldron/"Treanik Ireblade":
      - Player: "Beast Fights" (link: external event mention)
        - Prompted by `event_trade`:
          - NPC say: Me hopes you can hold your breath, . Me make sure to stock up before makin' dat long swim. Pesky goblins all over. Treanik must tell dat dere is much more dan pests here to taunt da likes of us. Dere be a beast down dere dat me not killed yet. Me much younger dan you, but me learn how dat [beast fights] -- it smarter dan da average creature, you know. Don't be fooled.
          - Event guard: `item_lib.check_turn_in(e.trade, {item1 = 60199})`
        - NPC say: Da only way to learn is to fight. It called Praklion of the Cauldron or sometin. Me hear it live here very long time, but rarely come out. It feed at weird times. Course, dat when it most mad. McArik found it traveling through deep craggy lands. Dat is how he decided it was good beast to test his ability to beat a baddy dat had some [sense of strategy]. It even took him long time to defeat it.
        - Condition: `e.other:GetClass() == Class.BERSERKER or e.other:GetGM()`
        - Condition: `e.other:GetLevel() >= 45`
        - Condition: `e.message:findi("beast fights")`
      - Player: "Strategy" (link: explicit mention)
        - NPC say: It do have sense of stragegy. It a creature dat has got smartz wit da magic too. Da way it mixes its abilities is good stuffs. You gots to try to catch it when it eats. It usually comes out when it dark out. And when you kill it, can you get my axe back? Me lost it to dat beast. Plus me needs proof you killed it so me can give you sumtin to give to McArik.
        - Condition: `e.other:GetClass() == Class.BERSERKER or e.other:GetGM()`
        - Condition: `e.other:GetLevel() >= 45`
        - Condition: `e.message:findi("strategy")`
3. fieldofbone/"Berserker-S Image", on event_death_complete. Sets `bersolo` to `1`.
4. fieldofbone/"Mardic Crimsonsteel", say "Hail". Requires `bersolo` ==1. Gives "Image Essence" (60196).
    - Dialogue with fieldofbone/"Mardic Crimsonsteel":
      - Player: "Hail"
        - NPC say: Hail, , Run along and give McArik the items he requested.
          - Reply guard: `(qglobals["bersolo"] == "1" and e.other:GetLevel() >= 45)`
        - NPC say: Hail to you, feared one. I see the glint of rage in them eyes of yours there. One day you'll be able to recognize the same in others. I suppose now is the time to talk to you about the mirage around here. Tell you the truth, I wasn't able to beat it myself... that's why I'm out here and not establishing myself as a berserker.
          - Reply guard: ``
        - NPC say: I wasn't meant for that path. I'm here to guide folk like yourself and help you gain control of the insane beast that lurks inside you. You must be prepared to fight one like yourself. All ye need are your wits, brawn, and skill, nought else. When you are ready give me the note McArik gave you and I'll send you to the training grounds.
          - Reply guard: ``
        - Condition: `(e.message:findi("hail"))`
        - Gives Image Essence (60196).
5. Say "Defeat" to lakeofillomen/"Lingering Axefall".
6. Spawns "An Impervious Bloodbeast" (85225).
7. Loot "Bloodbeast Tooth" (60192) from "An Impervious Bloodbeast".
8. lakeofillomen/"Keras Mcarik", say "Great Stride". Gives "Medal of Blood" (60190).
9. lakeofillomen/"Keras Mcarik", hand "Medal of Blood" (60190) + "Bloodbeast Tooth" (60192). Gives "Medal of Mirages" (60194).
10. lakeofillomen/"Keras Mcarik", hand "Medal of Mirages" (60194) + "Image Essence" (60196). Gives "Medal of Strategy" (60198).
11. lakeofillomen/"Keras Mcarik", hand "Medal of Strategy" (60198) + "Bone Trinket" (60201). Gives "Medal of Fervid Rage" (60202).
12. Kill fearplane/"Enraged Imp". Spawns "Ireblind Imp" (72069).
13. Loot "Burning Essence of Rage" (60203) from "Ireblind Imp".
14. lakeofillomen/"Keras Mcarik", hand "Medal of Fervid Rage" (60202) + "Burning Essence of Rage" (60203). Gives "Medal of Hunting" (60204).
15. lakeofillomen/"Keras Mcarik", say "Do". Gives "McArik Reagent Satchel" (60205).
16. Loot "Decaying Liver" (60206) from "Disease-Ridden Gorilla" in `emeraldjungle`.
17. Loot "Gnashing Kobold Paw" (60207) from "Gnashing Kobold" in `stonebrunt`.
18. Loot "Scent Gland" (60208) from "Reeking Skunk" in `tox`.
19. Loot "Scent Gland" (60208) from "Reeking Skunk" in `toxxulia`.
20. Buy "Medicine Bag" (17901) from "Rendallen Ironforge" (NPC 2071) in `qeynos2`. Base price: 1,000 copper.
21. Buy "Handful of Prism Grains" (95922) from "Murak" (NPC 49085) in `oggok`. Base price: 800 copper.
22. Loot "Heliotrope" (14242) from "a Di'zok Herbalist" in `chardok`.
23. Loot "Heliotrope" (14242) from "a Sarnak Herb Collector" in `chardok`.
24. Loot "Heliotrope" (14242) from "an Apprentice Herbalist" in `chardok`.
25. Buy "Yebamante" (16510) from "Guri" (NPC 30098) in `everfrost`. Base price: 25,000 copper.
26. Buy "Blade Leaf" (22143) from "Guri" (NPC 30098) in `everfrost`. Base price: 2,500 copper.
27. Buy "Simple Potion Vial" (95843) from "Guri" (NPC 30098) in `everfrost`. Base price: 750 copper.
28. Combine in "Medicine Bag" (17901): "Handful of Prism Grains" (95922), "Heliotrope" (14242), "Yebamante" (16510), "Blade Leaf" (22143), "Simple Potion Vial" (95843). Produces "Philter of Major Translocation" (96467). Requires Alchemy, trivial 131.
29. Combine in "McArik Reagent Satchel" (60205): "Decaying Liver" (60206), "Gnashing Kobold Paw" (60207), "Scent Gland" (60208), "Philter of Major Translocation" (96467). Produces "Bag of Image Essence Dust" (60209). The combine does not fail.
30. lakeofillomen/"Keras Mcarik", hand "Medal of Hunting" (60204) + "Bag of Image Essence Dust" (60209). Gives "Medal of Mastery" (60210).

### "Kerasian Axe of Ire" (68299)

1. Acquisition of "Medal of Mastery" (60210) is documented under "Medal of Mastery" (60210); obtain another copy if needed.
2. Spawns "Raving Goblinmaster - KOS" (79126) in `warslikswood` on event_waypoint_arrive.
3. Loot "Maniac's Garbled Tome" (60211) from "Raving Goblinmaster - KOS".
4. lakeofillomen/"Keras Mcarik", hand "Medal of Mastery" (60210) + "Maniac's Garbled Tome" (60211). Gives "Kerasian Axe of Ire" (68299).

### `berserk_epic`

Values written: 1, 2, 3, 4, 5, 7, 8, 9, 10.

1. lakeofillomen/"Keras Mcarik", say "Hail". Sets `berserk_epic` to `1`.
    - Requires "Kerasian Axe of Ire" (68299).
    - Prerequisite: "Kerasian Axe of Ire" (68299). See section 0.
    - Dialogue with lakeofillomen/"Keras Mcarik":
      - Player: "Enhance My Axe"
        - NPC emote: chuckles as he hears your request. 'I knew ye would be askin' fer this soon enough!' Keras slowly drags his eyes over your axe examining it from tip to tip. 'Ah, yes. Teekan's enchantments have weathered your journey fine. Yet I sense that even that even more may be done with it. Like yerself, the potential within this axe is truly astounding. As the basis of power of yer axe comes from gems and metals I would seek those out. Ye may also wish to look for other items of power that could fortify it further. After ye've managed to procure such things, come back and give them and yer axe to me and I'll see what I can dew fer ye then.
        - Condition: `($qglobals{berserk_epic} ==9)`
        - Condition: `($text=~/enhance my axe/i)`
      - Player: "Items Of Power" (link: explicit mention)
        - NPC say: I'm no tinkerer so I cannah tell ye what ye should be lookin' fer. Perhaps ye should head to Steamfont and seek out the advice of a Gnome as they are clever folk with all sorts of objects.
        - Condition: `($qglobals{berserk_epic} ==9)`
        - Condition: `($text=~/items of power/i)`
      - Player: "Gem" (link: external event mention)
        - Prompted by `event_item`:
          - NPC say: grabs each axe individually and mutters something inaudible. He takes each axe in his hands and looks them over. 'This axe seems to display almost no wear, which is highly unusual, given the amount of punishment ye must have put it through. Surely all three of these axes are of higher quality than the ones we normally make, but this one is vastly superior. Given the quality of this axe, I'd say that it could very easily benefit from some enchantments. So the next step in this axe's journey should be to imbue it with some of the owner's essence. This will create an axe that can actually become aware of its owner's wishes to help him realize his true Berserker's potential. Why if I were the owner and had a rare Soul Gem handy, I'd be headin' off to Teekan the Enchanter in the Abysmal Sea. Her abilities to weave such magic are unsurpassed.
          - Event guard: `(plugin::check_handin(\%itemcount, 18976 => 1, 17833 => 1, 17898 => 1, 17399 => 1))`
        - NPC say: I have heard of a Dwarven jewel merchant that goes by the name of Tarvash Scriller that is currently studying the gems found Discord. Seek him out fer I am sure he can help ye with information as he is an expert in all manner of gems and jewels. Ye need keep ye purse strings tightly closed though as I've heard he's a crafty devil with a sly tongue that would surely sell ya the stars if'in he could.
        - Condition: `($qglobals{berserk_epic} ==9)`
        - Condition: `($text=~/gem/i)`
      - Player: "Metal" (link: explicit mention)
        - Prompted by player input: "Enhance My Axe"
        - NPC say: Ach, there's the rub! I dinnah know much about the metals ye brought back the first time as they were all used in those axes. Maybe ye should look for a smith from that area. You must let them look at the axe but be wary though fer little do we know of them.
        - Condition: `($qglobals{berserk_epic} ==9)`
        - Condition: `($text=~/metal/i)`
      - Player: "Hail" (link: conversation sequence)
        - NPC emote: eyes your axe in a somewhat awe-stricken fashion. 'What have ye got there? Let me take a look at that! You stride up to Keras and proudly outstretch your finished Axe but notice that it takes Keras a moment before he realizes that you've even arrived. 'Ach. . .sorry lad. Let's have a look, shall we?' Keras begins to carefully examine the axe, each step of the way nodding approvingly. 'This is truly excellent work. Teekan has never let me down. This axe is possibly the highest quality that I have ever seen and should serve ye well in ye travels.' As he hands you the axe back, you once again notice a deep concern growing over his countenance. 'I am sorry that I canna' spend more time wit ye but ye've no doubt noticed that as of late, I've been troubled.
        - Condition: `(defined $qglobals{berserk_epic} && $qglobals{berserk_epic} >=7)`
        - Condition: `($text=~/hail/i)`
      - Player: "Troubled" (link: explicit mention)
        - NPC say: That student o' mine is now long overdue and I fear she may have her failed in her lesson. Would ye do an old man a favor and find out what has happened to me other student?
        - Condition: `(defined $qglobals{berserk_epic} && $qglobals{berserk_epic} >=7)`
        - Condition: `($text=~/troubled/i)`
      - Player: "Find Out" (link: explicit mention)
        - NPC say: I dinnah not exactly know where she may be, but her name is Julei Direaxe and I fear that she may be in trouble. Please, hurry, strike out and find her, rescue her from any troubles she may be in. Return her to safety and bring me proof that she is alright and ye shall forever have me gratitude.
        - Condition: `(defined $qglobals{berserk_epic} && $qglobals{berserk_epic} >=7)`
        - Condition: `($text=~/find out/i && $qglobals{berserk_epic}==7)`
        - Sets `berserk_epic` to `8`.
      - Player: "Hail" (link: conversation sequence)
        - NPC emote: appears to be lost in this own thoughts, mumbling to himself occasionally, and barely acknowledging your existence. Just as you're about to speak again, he says, 'Ach, ya have to forgive me absentmindedness, friend. I've been rather busy pondering [matters] at hand.
        - Condition: `(defined $qglobals{berserk_epic} && $qglobals{berserk_epic} >=1)`
        - Condition: `($text=~/hail/i && ($qglobals{berserk_epic} ==1 || $qglobals{berserk_epic} ==2)  && plugin::check_hasitem($client, 11999))`
        - Sets `berserk_epic` to `3`.
      - Player: "Hail" (link: conversation sequence)
        - NPC emote: Its good to see you again, friend. It seems my axe has fared well thus far, aye? Indeed it has. Have you spoke with your guildmaster yet? They will be glad to see that you are on your path towards controlling your rage.
        - Condition: `(defined $qglobals{berserk_epic} && $qglobals{berserk_epic} >=1)`
        - Condition: `($text=~/hail/i && $qglobals{berserk_epic} ==1 && !plugin::check_hasitem($client, 11999))`
      - Player: "Matters" (link: explicit mention)
        - NPC say: Since the recent discovery of the portal on Taelosia, we've been finding many different types of ores, plants, and minerals that were unlike anything we'd ever seen before. These materials have been used to craft simple weapons, potions, and sometimes even been used in various recipes for. . .uh. . .some interesting dishes. Yet I believe that they can be used for [something] much, much more.
        - Condition: `(defined $qglobals{berserk_epic} && $qglobals{berserk_epic} >=1)`
        - Condition: `($text=~/matters/i && $qglobals{berserk_epic} ==1 && plugin::check_hasitem($client, 11999))`
      - Player: "Something" (link: explicit mention)
        - NPC say: Some of these materials were of a quality that I feel can be used to craft implements of incredible power and perhaps these [materials] can even be incorporated into the processes used to craft the Axe of Ire to create an even more durable [weapon].
        - Condition: `(defined $qglobals{berserk_epic} && $qglobals{berserk_epic} >=1)`
        - Condition: `($text=~/something/i && $qglobals{berserk_epic} ==1 && plugin::check_hasitem($client, 11999))`
      - Player: "Materials" (link: explicit mention)
        - NPC say: Smiths have used many different types of tempering materials, from water to plant extracts to even blood from exotic animals on occasion. Why I've even heard about one legendary smith using the tears of a god! But given the magical properties of the ore that yew are collecting for me, I suspect that the plants and even some of the animal have been affected by the same type of magic. It is my theory that if we combined the [ore] with [blood] and [extracts] from the plants and animals of Taelosia, we would increase our efforts doubly.
        - Condition: `(defined $qglobals{berserk_epic} && $qglobals{berserk_epic} >=1)`
        - Condition: `($text=~/materials/i && $qglobals{berserk_epic} ==1 && plugin::check_hasitem($client, 11999))`
      - Player: "Ore" (link: explicit mention)
        - NPC say: I thank ye for volunteering. The ore I seek comes form the areas closest to where the portal to Discord was originally opened. Ore from this area, I've been told, seems to be the purest form available. Once yew've gathered 4 pieces of this ore, return to me so that I may continue my research.
        - Condition: `(defined $qglobals{berserk_epic} && $qglobals{berserk_epic} >=1)`
        - Condition: `($text=~/ore/i && $qglobals{berserk_epic} ==1 && plugin::check_hasitem($client, 11999))`
      - Player: "Blood" (link: explicit mention)
        - Prompted by player input: "Materials"
        - NPC say: There are many different types of creatures lurking throughout all of Taelosia though two intrigue me the most. . .the cragbeasts and the hynids. In order to craft the various tempers that I need, I will require 4 vials of blood from each of these creatures.
        - Condition: `(defined $qglobals{berserk_epic} && $qglobals{berserk_epic} >=1)`
        - Condition: `($text=~/blood/i && $qglobals{berserk_epic} ==1 && plugin::check_hasitem($client, 11999))`
      - Player: "Extracts" (link: explicit mention)
        - Prompted by player input: "Materials"
        - NPC say: Taelosia is vibrant with some of the most exotic plants known to Norrath, with nary a tree in sight. That in and of itself is a bit unusual but the plant-life that does exist in Taelosia seems to be very potent in nature. Gather 4 samples from two different plants and return to me once this has been done.
        - Condition: `(defined $qglobals{berserk_epic} && $qglobals{berserk_epic} >=1)`
        - Condition: `($text=~/extracts/i && $qglobals{berserk_epic} ==1 && plugin::check_hasitem($client, 11999))`
      - Player: "Weapon" (link: explicit mention)
        - Prompted by player input: "Matters"
        - NPC say: Ever since I've heard stories about these materials, I've been working on various designs for a new axe. . .trying to figure out how one could imbue it with the essence and spirit of a true berserker. Unfortunately I have been unable to get my hands on any raw ore of a high enough quality to experiment with.
        - Condition: `(defined $qglobals{berserk_epic} && $qglobals{berserk_epic} >=1)`
        - Condition: `($text=~/weapon/i && $qglobals{berserk_epic} ==1 && plugin::check_hasitem($client, 11999))`
      - Player: "Hail" (link: conversation sequence)
        - NPC emote: once again looks lost in deep thought, 'Apologies $name. Another student o'mine has not returned yet and shall soon be overdue. I am beginning to worry that she may be in trouble. Yet she still has more time to complete her task so mayhap I shouldnah worry. Shaking himself of his concerns Keras asks, 'Come now, how well did the axes fair?'
        - Condition: `(defined $qglobals{berserk_epic} && $qglobals{berserk_epic} >=1)`
        - Condition: `($text=~/hail/i && $qglobals{berserk_epic} ==4)`
      - Player: "Hail" (link: conversation sequence)
        - NPC say: Its good to see you again, friend. It seems my axe has fared well thus far, aye? Indeed it has. Have you spoke with your guildmaster yet? They will be glad to see that you are on your path towards controlling your rage.
        - Condition: ``
        - Condition: `($text=~/hail/i && $class eq "Berserker" && plugin::check_hasitem($client, 68299) && $qglobals{"berserk_epic"} == undef)`
        - Sets `berserk_epic` to `1`.
      - Player: "Hail" (link: conversation sequence)
        - NPC say: Aye, I see a familiar look in yer eye. Ye are much like me, friend. If ye truly wish to [master the fires] within ye and become a true berserker, ye must learn many lessons.
        - Condition: ``
        - Condition: `($text=~/hail/i && $class eq "Berserker" && $ulevel > 45 && $dragon == undef && $imp == undef  && !plugin::check_hasitem($client, 68299))`
      - Player: "Master The Fires" (link: explicit mention)
        - NPC say: Much as ye are now, I was once saddled with unbridled rage, and now with age and experience, I have learned to master the power that comes with my anger.
        - NPC say: Once ye have mastered yer abilities, ye will be rewarded with a gift that only a true berserker can control. It is a gift that will harness yer rage and use it to yer advantage. This is why ye must walk the same path I did in me youth. Do ye wish to take this [great stride]?
        - Condition: ``
        - Condition: `($text=~/master the fires/i && $class eq "Berserker" && $ulevel > 45 && $dragon == undef && $imp == undef)`
      - Player: "Great Stride" (link: explicit mention)
        - NPC say: Ye do understand there is no turning back? I hope so. This is a journey -- and sometimes a long one -- depending on what ye've leared so far. Yer skills and wisdom in battle will be tested. Go talk to an old, fallen friend of mine, Lingering Axefall. We call him that because he reguses to let his spirit rest. He failed his task and remains bound here to lead others into the trial he lost. Be wary, though. He is elusive.
        - NPC say: The foe he stood against and lost to still wishes to extinguish his spirit. Take this axe and give it to him so he will know that ye are ready for the test and that I sent ye. Also, take this medal with you. It will help me keep track of your progress. Best of luck, friend.
        - Condition: ``
        - Condition: `($text=~/great stride/i && $class eq "Berserker" && $ulevel > 45 && $dragon == undef && $imp == undef)`
        - Gives Throwing Axe of the Spirit (60189).
        - Gives Medal of Blood (60190).
      - Player: "Hail" (link: conversation sequence)
        - NPC say: Return once you have trained more, young Berserker.
        - Condition: ``
        - Condition: `($text=~/hail/i && $ulevel < 46 && $class eq "Berserker")`
      - Player: "Challenge"
        - NPC say: The challange is for ye, and ye alone. If you have anyone try to assist ye, ye will fail. Do not attempt to cheat yerself of yer own development. Ye must seek out Mardic Crimsonsteel and get his guidance. He will prepare ye to fight a mirage of a berserker that has been created through years of refined magic. I cannot tell ye the source of such magic, but ye must know that I used that mirage as me sparring partner, constantly improving me skills against it and advancing. Perhaps now it's yer turn to face it... alone. Take this sealed note to Mardic. It will give him instructions for yer test.
        - Condition: ``
        - Condition: `($text=~/challenge/i && plugin::check_hasitem($client, 60194))`
        - Gives Sealed Note for Mardic (60195).
      - Player: "Strategize In Battle" (link: external event mention)
        - Prompted by `event_item`:
          - NPC say: Well, I am indeed hopeful and pleased about yer progress, $name. Ye should be proud that you have now attained the Medal of Strategy. Well done, indeed! It seems that ye can best yer equal now. The next test of yer masters of yer abilities is much more difficult, however, and may require ye to ask yer friends for some 'elp... but it must be the right kind of 'elp. This test will determine how well ye [strategize in battle]. Ye must gather trustworthy friends and they must be willing to work under yer command.
          - Event guard: `(plugin::check_handin(\%itemcount, 60196 => 1, 60194 => 1))`
        - NPC say: One of the best strategists I've ever met is ready and willing to help any who attempt to prove their skills in battle. Seek out Treanik Ireblade. She won't give ye any advantage, however. This is yer fight to win, not hers, though she'll be itchin' to get her blade bloodied. Take this note and give it to her.
        - Condition: ``
        - Condition: `($text=~/strategize in battle/i && plugin::check_hasitem($client, 60198))`
        - Gives Note for Treanik (60199).
      - Player: "Ready" (link: explicit mention)
        - NPC say: Eager one, aren't ye? Good to see, but do not underestimate how volatile our rage is. In me youth, it snuck up on me and in a blind rage, I had slain me sparring partner. It was then that I knew I was different and shouldn't keep close friends until I'ad my rage under control. There are some, though, that will [never control the rage].
        - Condition: ``
        - Condition: `($text=~/ready/i && $ulevel > 45 && $class eq "Berserker" && $imp == 1)`
      - Player: "Never Control The Rage" (link: explicit mention)
        - NPC say: Well, you see, the fire that drives the rage through us and into our muscles and minds can burn out of control in come creatures. I have encountered several in my travels, aye. They are merciless and blind to the rage, which makes 'em poor at strategy, but deadly in combat. Ye will have to [face one] of 'em so that ye may learn how dangerous ye can truly become if ye do not complete these trials and master the rage. I do 'ope ye appreciate this lesson.
        - Condition: ``
        - Condition: `($text=~/never control the rage/i && $ulevel > 45 && $class eq "Berserker" && $imp == 1)`
      - Player: "Face One" (link: explicit mention)
        - NPC say: This creature is unlike any you have seen wandering the lands. this beast is fearsome and ethereal. It strikes out with its rage without thought or care. Ye must learn to recognize this type of beast if ye are to learn how to master it and yer own abilities. It will try to disguise itself so ye don't recognize the fury it holds within it -- it has an [enraged essence] within it and I want ye to bring it to me. Remember, $name, do not be fooled and always be aware.
        - Condition: ``
        - Condition: `($text=~/face one/i && $ulevel > 45 && $class eq "Berserker" && $imp == 1)`
      - Player: "Enraged Essence" (link: explicit mention)
        - NPC say: I will give ye no more hints. Ye must seek this creature out alone. Look far and use your mind and brawn to beat it. Yer noggin will give ye an advantage o'er this un.
        - Condition: ``
        - Condition: `($text=~/enraged essence/i && $ulevel > 45 && $class eq "Berserker" && $imp == 1)`
      - Player: "Do" (link: explicit mention)
        - Prompted by player input: "Metal"
        - NPC say: For my mirage to remain part of my trials, I need some very specific reagents. There is a sickly gorilla that carries a rotting organ which I am in need of. Also, I need a paw of a very special and dangerous kobold. Lastly, bring me the poison sac of a dangerous spider. A potion that allows us to create a gate from one place to another is also required. If ye believe ye can do this for me, tell me so, and I will give ye a bag to hold them in. When ye have all of the ingredients, combine them in the bag I've given ye, and bring it back to me. Good luck in your hunt!
        - Condition: ``
        - Condition: `($text=~/do/i && ($hunting == 1 || plugin::check_hasitem($client,60204)))`
        - Gives McArik Reagent Satchel (60205).
      - Player: "Next Challenge" (link: external event mention)
        - Prompted by `event_item`:
          - NPC say: Wonderful. Ye have earned yer Medal of Mastery, but ye are not done yet. There is one final test ye must complete before I can recognize ye as a true berserker. Ye must prove that in the face of great adversity, ye can keep yer wits about ye. This final test, naturally, is the most difficult, but I would not present this [next challenge] to ye if I thought ye could not finish yer journey.
          - Event guard: `(plugin::check_handin(\%itemcount, 60209 => 1, 60204 => 1))`
        - NPC say: For this encounter, ye must be prepared for the unexpected and, in the face of chaos, be able to focus on the task at hand. Yer stamina will also be tested. When I first encountered this wicked trap in me travels, even I had to attempt it a couple of times. However, I do have faith in ye. With my advance warning, ye shouldn't be caught off guard. This challenge will also prove how loyal and skilled yer own friends are. One thing is for certain, ye can't complete this [next test] alone.
        - Condition: ``
        - Condition: `($text=~/next challenge/i && ($mastery == 1 || plugin::check_hasitem($client,60210)))`
      - Player: "Next Test" (link: explicit mention)
        - NPC say: Make your way to the woods in Kunark. Use the hunting skills ye have gained to find a most unusual and war-hungry creature. It has a very unique magic in its battle repertoire that will definitely test yer mettle. Off with ye, then. I do hope I see ye again...I've become quite fond of ye. I recently sent another like ye to do this trial and I haven't heard from him...
        - Condition: ``
        - Condition: `($text=~/next test/i && ($mastery == 1 || plugin::check_hasitem($client,60210)))`

Alternative or repeat transition to `berserk_epic` = `1` (not an additional required stage).

1. lakeofillomen/"Keras Mcarik", hand "Medal of Mastery" (60210) + "Maniac's Garbled Tome" (60211). Sets `berserk_epic` to `1`.
    - Hand in x1: "Medal of Mastery" (60210).
    - Hand in x1: "Maniac's Garbled Tome" (60211).
    - Prerequisite: "Medal of Mastery" (60210). See section 0.
    - Spawns "Raving Goblinmaster - KOS" (79126) in `warslikswood` on event_waypoint_arrive.
    - Loot "Maniac's Garbled Tome" (60211) from "Raving Goblinmaster - KOS".
    - Gives "Kerasian Axe of Ire" (68299).

2. poknowledge/"Baeldarr Hawkeye", hand "Taelosian Tempered Ore" (15793) + "Taelosian Tempered Ore" (17319) + "Taelosian Tempered Ore" (17496) + "Taelosian Tempered Ore" (17589). Sets `berserk_epic` to `2`.
    - Requires `berserk_epic` set.
    - Requires `berserk_epic` >=1.
    - Hand in x1: "Taelosian Tempered Ore" (15793).
    - Hand in x1: "Taelosian Tempered Ore" (17589).
    - Hand in x1: "Taelosian Tempered Ore" (17319).
    - Hand in x1: "Taelosian Tempered Ore" (17496).
    - Given by lakeofillomen/"Keras Mcarik", say "Check5Globalserk".
    - Given by lakeofillomen/"Keras Mcarik", say "Check5Globalserk".
    - Given by lakeofillomen/"Keras Mcarik", say "Check5Globalserk".
    - Given by lakeofillomen/"Keras Mcarik", say "Check5Globalserk".

3. lakeofillomen/"Keras Mcarik", say "Hail". Sets `berserk_epic` to `3`.
    - Requires `berserk_epic` ==1.
    - Requires `berserk_epic` ==2.
    - Requires "Raging Soul Shard" (11999).
    - Requires `berserk_epic` >=1.
    - Requires `berserk_epic` set.
    - Prerequisite: "Raging Soul Shard" (11999). See section 0.

Alternative or repeat transition to `berserk_epic` = `3` (not an additional required stage).

3. poknowledge/"Baeldarr Hawkeye", hand "Darkwood Sapling Branch" (17286) + "Darkwood Sapling Branch" (17286) + "Darkwood Sapling Branch" (17286) + "Darkwood Sapling Branch" (17286). Sets `berserk_epic` to `3`.
    - Requires `berserk_epic` set.
    - Requires `berserk_epic` >=2.
    - Hand in x1: "Darkwood Sapling Branch" (17286).
    - Ground spawn of "Darkwood Sapling Branch" (17286) in `draniksscar`.
    - Gives "Trial Taelosian Alloy Blood Axe" (17370).
    - Gives "Trial Taelosian Alloy Blood Axe" (17700).
    - Gives "Trial Taelosian Alloy Blood Axe" (17759).
    - Gives "Trial Taelosian Alloy Blood Axe" (16779).

4. sebilis/"Berserkerepic 1 5", say "Protector Death". Sets `berserk_epic` to `4`.
    - Sets `berserk_epic_sebchest` to `1`.

5. lakeofillomen/"Keras Mcarik", hand "Damaged Trial Taelosian Blood Axe" (17399) + "Broken Trial Taelosian Blood Axe" (17833) + "Damaged Trial Taelosian Blood Axe" (17898) + "Taelosian Alloy Blood Axe" (18976). Sets `berserk_epic` to `5`.
    - Hand in x1: "Taelosian Alloy Blood Axe" (18976).
    - Hand in x1: "Broken Trial Taelosian Blood Axe" (17833).
    - Hand in x1: "Damaged Trial Taelosian Blood Axe" (17898).
    - Hand in x1: "Damaged Trial Taelosian Blood Axe" (17399).
    - Given by sebilis/"Berserkerepic 1 5", say "Protector Timer".
    - Given by sebilis/"Berserkerepic 1 5", say "Protector Timer".
    - Given by sebilis/"Berserkerepic 1 5", say "Protector Timer".
    - Given by sebilis/"Berserkerepic 1 5", say "Protector Timer".
    - Gives "Taelosian Alloy Blood Axe" (18976).

7. abysmal/"Teekan Opousbabolaoi", hand "Raging Soul Shard" (11999) + "Taelosian Alloy Blood Axe" (18976). Sets `berserk_epic` to `7`.
    - Requires `berserk_epic` ==5.
    - Hand in x1: "Taelosian Alloy Blood Axe" (18976).
    - Hand in x1: "Raging Soul Shard" (11999).
    - Given by sebilis/"Berserkerepic 1 5", say "Protector Timer".
    - Prerequisite: "Raging Soul Shard" (11999). See section 0.
    - Gives "Raging Taelosian Alloy Axe" (18398).
    - Dialogue with abysmal/"Teekan Opousbabolaoi":
      - Player: "Hail"
        - NPC say: Hail to thee friend! No doubt you sought me out for my expertise in enchanting though I admit to wondering what need a bersrker like yourself would have of me. Pray tell how may I serve thee?
        - Condition: `(e.message:findi("hail") and e.other:Class() == "Berserker")`

8. lakeofillomen/"Keras Mcarik", say "Find Out". Sets `berserk_epic` to `8`.
    - Requires `berserk_epic` ==7.
    - Requires `berserk_epic` >=7.
    - Requires `berserk_epic` set.

9. lakeofillomen/"Keras Mcarik", hand "Julei's Twilight Pendant" (17200). Sets `berserk_epic` to `9`.
    - Hand in x1: "Julei's Twilight Pendant" (17200).
    - Prerequisite: "Julei's Twilight Pendant" (17200). See section 0.

10. dranik/"Grithyank Avlonnon", hand "Unhoned Vengeful Taelosian Blood Axe" (20072) + "Globe of Discordant Energy" (47100). Sets `berserk_epic` to `10`.
    - Requires `berserk_epic` ==9.
    - Hand in x1: "Unhoned Vengeful Taelosian Blood Axe" (20072).
    - Hand in x1: "Globe of Discordant Energy" (47100).
    - Prerequisite: "Unhoned Vengeful Taelosian Blood Axe" (20072). See section 0.
    - Say "Check Lorb" to anguish/"Zone Status".
    - Spawns "Orb of Discordant Energy" (317087).
    - Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy".
    - Alternative: Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy" (NPC 317087) in `anguish`; trigger: anguish/"Zone Status", say "Check Uorb".
    - Alternative: Loot "Globe of Discordant Energy" (47100) from "Ornate Chest" (NPC 317112) in `anguish`; trigger: anguish/"Zone Status", say "Check Amv Chest".
    - Alternative: Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy" (NPC 317087) in `anguish`; trigger: anguish/"Zone Status", say "Signal:999999".
    - Alternative: Loot "Globe of Discordant Energy" (47100) from "Overlords Chest" (NPC 317124) in `anguish`; trigger: anguish/"Zone Status", say "Signal:999999".
    - Gives "Vengeful Taelosian Blood Axe" (18609).
    - Dialogue with dranik/"Grithyank Avlonnon":
      - Player: "Hail"
        - NPC say: Yes outlander? What would you have of me now?' You notice his eyes widen further upon glancing over your improved axe. 'So you managed to successfully lace the Shadowed Bronze into the haft as I spoke of. Very good. I also notice this extra moonstone that wasn't here before. As to its purpose I can not speak of.' Running his sinewy finger carefully across the edge he says, 'But the edge here could still use some sharpening. Blades such as this though can not be sharpened by a normal means. No, a blade this strong will require naught but a portion of Discordant matter itself. It has been said that this matter can sometimes be found captured within the tears of those that have been tortured. Return to me only when you have succeeded in finding one. Then we will see how else I can aid thee.
          - Reply guard: `(e.other:HasItem(20072))`
        - Condition: `(qglobals["berserk_epic"] == "9")`
        - Condition: `(e.message:findi("hail"))`
      - Player: "Enhance My Axe" (link: conversation sequence)
        - NPC emote: turns fully towards you as if now willing to pay more attention to you. 'An interesting specimen of a weapon. It blends craftsmanship from your world, components from mine, and magic from both. I would love the opportunity to study it further but I know you did not bring it to me to study. I gather you wish to learn more about it though?
        - Condition: `(qglobals["berserk_epic"] == "9")`
        - Condition: `(e.message:findi("enhance my axe"))`
      - Player: "Learn" (link: explicit mention)
        - NPC say: The ore chosen for the head of the axe your people would call Chaotic Steel. It is an extremely durable base to form a weapon from so likely there is little I can do for this piece. I notice the handle, however, appears to be made of a fairly strong yet flexible wood. Yet I believe the smith did not know that this metal can cause undue stress upon the handle eventually shattering it at the least convenient time, in the heat of battle. From my studies of your world I suggest lacing it with a small portion of what our people call Shadowed Bronze. I believe you can find the proper Shadowed Bronze on an ancient shade in Grieg's End. This should help to absorb much of the stress passed along from the axe head.
        - Condition: `(qglobals["berserk_epic"] == "9")`
        - Condition: `(e.message:findi("learn"))`

#### Steps on `berserk_epic` that do not change it

- `bloodfields` tarvash scriller, hand gold:50 needs `berserk_epic` ==9.
- `bloodfields` tarvash scriller, hand platinum:50 needs `berserk_epic` ==9.
- `causeway` player, on loot needs `berserk_epic` ==9.
  - Sets `ber_chest_causeway` to `1`.
  - Spawns a chest (epic 2.0) (893).
- `griegsend` player, on loot needs `berserk_epic` ==9.
  - Sets `ber_epic_ge` to `1`.
  - Spawns a chest (Epic 2.0) (893).
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
- `halas` shanis macdarren, say hail needs `berserk_epic` >=1.
  - Gives Raging Soul Shard (11999).
- `hole` julei direaxe, say hail needs `berserk_epic` ==8.
  - Gives Julei's Twilight Pendant (17200).
- `kaladimb` dravel axethrasher, say hail needs `berserk_epic` >=1.
  - Gives Raging Soul Shard (11999).
- `oggok` baddi waca, say hail needs `berserk_epic` >=1.
  - Gives Raging Soul Shard (11999).
- `sharvahl` vrasha piennsa, say hail needs `berserk_epic` >=1.
  - Gives Raging Soul Shard (11999).

### Other flags touched along the way

- `ber_epic_ge` set to 1 at griegsend/player.
- `berserk_epic_crag` set to 1 at lakeofillomen/keras mcarik.
- `berserk_epic_fern` set to 1 at lakeofillomen/keras mcarik.
- `berserk_epic_hyn` set to 1 at lakeofillomen/keras mcarik.
- `berserk_epic_ore` set to 1 at lakeofillomen/keras mcarik.
- `berserk_epic_sebchest` set to 1 at sebilis/berserkerepic 1 5.
- `berserk_epic_tea` set to 1 at lakeofillomen/keras mcarik.
- `berserk_epic_test16779` set to 1 at sebilis/berserkerepic 1 5.
- `berserk_epic_test17370` set to 1 at sebilis/berserkerepic 1 5.
- `berserk_epic_test17700` set to 1 at sebilis/berserkerepic 1 5.
- `berserk_epic_test17759` set to 1 at sebilis/berserkerepic 1 5.
