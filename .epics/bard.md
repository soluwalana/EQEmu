# Bard

Acquisition paths traced backwards from the 1.0, 1.5 and 2.0 epic rewards. Flags are dependencies, not the definition of an epic. **Broken** indicates missing graph provenance.

## Epic 1.0

### "Singing Short Sword" (20542)

1. qey2hh1/"Konia Swiftfoot", say "Hail". Hello there, .  I am hosting a relay running contest.  Would you like to participate?
2. qey2hh1/"Konia Swiftfoot", say "Ready". Gives "Torch of Misty" (20532).
3. misty/"Fajio Knejo", hand "Torch of Misty" (20532). Gives "Torch of Ro" (20533).
4. southro/"Andad Filla", hand "Torch of Ro" (20533). Gives "Torch of Rathe" (20534).
5. lakerathe/"Misty Tekcihta", hand "Torch of Rathe" (20534). Gives "Proof of Speed" (20379).
6. qey2hh1/"Konia Swiftfoot", hand "Proof of Speed" (20379). Gives "Maestro's Symphony Page 24 Top" (20376).
7. southkarana/"Baenar Swiftsong", say "Doll". Gives "Solusek Mining Company Invoice" (20372).
8. soldunga/"Marfen Binkdirple", hand "Solusek Mining Company Invoice" (20372). Gives "Mechanical Doll" (20370).
9. unrest/"Serra", hand "Mechanical Doll" (20370). Gives "Note for Baenar" (20371).
    - Dialogue with unrest/"Serra":
      - Player: "Hail"
        - NPC say: H..h..hello? Can you help me? I lost [something] and I need it so I can go back home.
        - Condition: `(e.message:findi("hail"))`
      - Player: "Something" (link: explicit mention)
        - NPC say: I never got my doll for my birthday. Before he could bring it to me I was h..hurt by the bad man. I cannot leave without my doll. Will you please help me?
        - Condition: `(e.message:findi("something"))`
      - Player: "Doll" (link: explicit mention)
        - NPC emote: claps her hands. 'Oh goody! But... I cannot seem to remember his name. He gave me this note before I...
        - Condition: `(e.message:findi("doll"))`
      - Player: "Note" (link: explicit mention)
        - NPC say: I hope it will help you out. Please find him so I can leave this place?
        - Condition: `(e.message:findi("note"))`
        - Gives Ripped Qeynos Bards Guild Flyer (20374).
10. southkarana/"Baenar Swiftsong", hand "Note for Baenar" (20371). Gives "Note to Maligar" (20368).
11. Hand "Note to Maligar" (20368) to qey2hh1/"Maligar". Spawns "Maligars Enraged Doppleganger" (12173). Loot "Maligar's Head" (20367) from "Maligars Enraged Doppleganger".
12. southkarana/"Baenar Swiftsong", hand "Maligar's Head" (20367). Gives "Mahlin's Mystical Bongos" (20366).
13. qey2hh1/"Konia Swiftfoot", hand "Mahlin's Mystical Bongos" (20366). Gives "Maestro's Symphony Page 24 Bottom" (20383).
14. Loot "Chromodrac Gut" (20527) from "Eldrig the Old" in `skyfire`.
15. Loot "Red Wurm Gut" (20528) from "Nezekezena" in `burningwood`.
16. Loot "Onyx Drake Gut" (20529) from "Blackwing".
17. Loot "Onyx Drake Gut" (20529) from "Blackwing" in `rathemtn`.
18. southkarana/"Kelkim Menkia", hand "Chromodrac Gut" (20527) + "Red Wurm Gut" (20528) + "Onyx Drake Gut" (20529). Gives "Maestro's Symphony Page 25" (20377).
19. Loot "Alluring Horn" (20530) from "Quag Maelstrom" in `oceanoftears`.
20. Loot "Alluring Horn" (20530) from "Quag Maelstrom" in `oot`.
21. butcher/"Vedico Windwisper", hand "Alluring Horn" (20530). Gives "Note to Forpar Fizfla" (20378).
22. steamfont/"Forpar Fizfla", hand "Note to Forpar Fizfla" (20378). Gives "Forpar's Note to Himself" (20380).
23. Loot "Kedge Backbone" (20524) from "Phinigel Autropos" in `kedge`.
24. Loot "Petrified Werewolf Skull" (20525) from "The Fabled Drolvarg Warlord".
25. Loot "Petrified Werewolf Skull" (20525) from "a Drolvarg warlord" in `karnor`.
26. Loot "Amygdalan Tendril" (5520) from "Amygdalan warrior" (NPC 72015) in `fearplane`. Drop cache: 8.14% chance per kill.
27. steamfont/"Forpar Fizfla", hand "Amygdalan Tendril" (5520) + "Forpar's Note to Himself" (20380) + "Kedge Backbone" (20524) + "Petrified Werewolf Skull" (20525). Gives "Mystical Lute Head" (20535).
28. Loot "White Dragon Scales" (11602) from "Gorenaire" in `dreadlands`.
29. Loot "White Dragon Scales" (11602) from "Lady Vox" in `permafrost`.
30. Loot "White Dragon Scales" (11602) from "The Fabled Gorenaire".
31. Loot "Red Dragon Scales" (11622) from "Echo of Nortlav" in `hole`.
32. Loot "Red Dragon Scales" (11622) from "Lord Nagafen" in `soldungb`.
33. Loot "Red Dragon Scales" (11622) from "Melalafen" in `westwastes`.
34. Loot "Red Dragon Scales" (11622) from "Talendor" in `skyfire`.
35. kaladimb/"Jeet", say "Collect The Gnome Profit". Gives "Scrubber Key" (12164).
    - Dialogue with kaladimb/"Jeet":
      - Player: "Hail"
        - NPC say: What business do you have here?!! This here is the mine and that means if you ain't a [member of Miner's Guild 628], you'd best be moving on!!
          - Reply guard: `($faction <= 7)`
        - NPC say: The word around the mines is that you are not to be trusted. You'd best leave before my dagger finds a new home in your back.
          - Reply guard: ``
        - Condition: `($text=~/hail/i)`
      - Player: "Member Of Miner'S Guild 628" (link: explicit mention)
        - NPC say: Well, then, get off yer rump and give us a hand! If you don't have a mining pick, then get down there and use your fingernails!! If you're new and you want to earn a pick, you can [volunteer to exterminate the rats] that have been infesting the mines!!
          - Reply guard: `($faction <= 4)`
        - NPC say: Don't take this personally, but I can't quite trust you with such matters. Maybe a few less Butcherblock bandits would prove your worth.
          - Reply guard: `($faction <= 5)`
        - NPC say: The word around the mines is that you are not to be trusted. You'd best leave before my dagger finds a new home in your back.
          - Reply guard: ``
        - Condition: `(($text=~/member of miner's guild 628/i))`
      - Player: "Volunteer To Exterminate The Rats" (link: explicit mention)
        - NPC say: Well, someone has to do the dirty work around here. Let it be you new miners. Go patrol the mines and if you see any rats, bash them good!! Return to me with four rat pelts and I will give you some armor as payment. If you want a 628 mining cap, yer gonna have to smash that infernal [cleaner]!!
          - Reply guard: `($faction <= 4)`
        - NPC say: Don't take this personally, but I can't quite trust you with such matters. Maybe a few less Butcherblock bandits would prove your worth.
          - Reply guard: `($faction <= 5)`
        - NPC say: The word around the mines is that you are not to be trusted. You'd best leave before my dagger finds a new home in your back.
          - Reply guard: ``
        - Condition: `(($text=~/volunteer to exterminate the rats/i))`
      - Player: "Run To The Gnome City" (link: external event mention)
        - Prompted by `event_item`:
          - NPC say: It's about time you managed to smash these four!! Here. You do good work. We could use someone like you to [run to the gnome city].
          - Event guard: `(plugin::check_handin(\%itemcount, 13054 => 4))`
        - NPC say: Well, as you most likely know, we are a non-profit organization, at least here in Kaladim. We need to make our profit elsewhere and that means a little bit of thieving. Presently we need loyal members to [collect the gnome profit].
          - Reply guard: `($faction <= 4)`
        - NPC say: Don't take this personally, but I can't quite trust you with such matters. Maybe a few less Butcherblock bandits would prove your worth.
          - Reply guard: `($faction <= 5)`
        - NPC say: The word around the mines is that you are not to be trusted. You'd best leave before my dagger finds a new home in your back.
          - Reply guard: ``
        - Condition: `(($text=~/run to the gnome city/i))`
      - Player: "Collect The Gnome Profit" (link: explicit mention)
        - NPC say: Take this key. Don't lose it!! You will need to use it on a metal rat called a scrubber. They are all over Ak'Anon. You must find the one that responds to the number, '628'. If it responds, use the key on it. It will hand over a bag with the 'gnome take'. Return it to me. Get moving!!
          - Reply guard: `($faction <= 4)`
        - NPC say: Don't take this personally, but I can't quite trust you with such matters. Maybe a few less Butcherblock bandits would prove your worth.
          - Reply guard: `($faction <= 5)`
        - NPC say: The word around the mines is that you are not to be trusted. You'd best leave before my dagger finds a new home in your back.
          - Reply guard: ``
        - Condition: `(($text=~/collect the gnome profit/i))`
        - Gives Scrubber Key (12164).
      - Player: "Cleaner" (link: explicit mention)
        - Prompted by player input: "Volunteer To Exterminate The Rats"
        - NPC say: Darn that blasted clockwork cleaner!! No one in Kaladim even knows what it is! They all think it's some kinda rat in armor!! Rat paladins?!! The name fits. We miners have seen many like it in the gnome city during heists, err.. visits. We have to get rid of this one in Kaladim!! If you smash it and get its scrap metal, I am authorized to give you a mining cap, if you are a member of Miner's Guild 628.
          - Reply guard: `($faction <= 4)`
        - NPC say: Don't take this personally, but I can't quite trust you with such matters. Maybe a few less Butcherblock bandits would prove your worth.
          - Reply guard: `($faction <= 5)`
        - NPC say: The word around the mines is that you are not to be trusted. You'd best leave before my dagger finds a new home in your back.
          - Reply guard: ``
        - Condition: `(($text=~/cleaner/i))`
36. akanon/"Clockwork Scrubber", hand "Scrubber Key" (12164). Gives "Gnome Take" (12167).
37. kaladimb/"Jeet", hand "Gnome Take" (12167). Gives "Small Piece of Ore" (10500).
38. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
39. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `steamfont`.
40. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `tox`.
41. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `toxxulia`.
42. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
43. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). The combine does not fail.
44. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
45. Combine in Forge (17): "Small Piece of Ore" (10500), "Water Flask" (13006). Produces "Metal Bits" (16905) x2. Requires Blacksmithing, trivial 18.
46. steamfont/"Forpar Fizfla", hand "White Dragon Scales" (11602) + "Red Dragon Scales" (11622) + "Metal Bits" (16905). Gives "Mystical Lute Body" (20536).
47. Kill sebilis/"An Undead Bard". Spawns "Trakanon" (89181).
48. Loot "Undead Dragongut Strings" (20526) from "Trakanon".
49. steamfont/"Forpar Fizfla", hand "Undead Dragongut Strings" (20526) + "Mystical Lute Head" (20535) + "Mystical Lute Body" (20536). Gives "Mystical Lute" (20538).
50. dreadlands/"Baldric Slezaf", hand "Maestro's Symphony Page 24 Top" (20376) + "Maestro's Symphony Page 25" (20377) + "Maestro's Symphony Page 24 Bottom" (20383) + "Mystical Lute" (20538). Gives "Singing Short Sword" (20542).

## Epic 1.5

### "Prismatic Dragon Blade" (77631)

1. soltemple/"Walthin Fireweaver", say "Hail". Sets `bard15` to `5`.
2. wakening/"Lantaric-Dar", say "Baldric Slezaf". Sets `bard15` to `1`.
    - Dialogue with wakening/"Lantaric-Dar":
      - Player: "Hail"
        - NPC say: Journey to the necropolis and stop the mercenaries . May Veeshan protect you.
          - Reply guard: `qglobals["bard15"] == "1"`
        - NPC say: Journey to the necropolis and lay Hsagra's spirit to rest! You must hurry!
          - Reply guard: `qglobals["bard15"] == "2"`
        - NPC say: Return to the necropolis and stop Vesthon before it is too late !
          - Reply guard: `qglobals["bard15"] == "3"`
        - NPC say: The kin thank you for your efforts in saving the spirit of Hsagra. May Veeshan guide your path in the destruction of the orb.
          - Reply guard: `qglobals["bard15"] ~= nil and qglobals["bard15"] >= "4"`
        - NPC emote: seems surprised as you approach him. He peers down at you with an inquisitive glint in his eyes. 'I sense a familiar aura around you One I have not felt in a long time. Tell me , do you have news of a man named Baldric?
          - Reply guard: `e.other:HasItem(20542)`
        - NPC emote: glances down at you with an almost palatable indifference. Small wonder, considering his significant stature. 'I have better things to do then deal with you mortal. The [children of Zek] hunt this land, and they hunt for me and my kin. I advise you to stay away from both them, and their quarry.'
          - Reply guard: ``
        - Condition: `e.other:Class() == "Bard"`
        - Condition: `e.message:findi("hail")`
      - Player: "Baldric Slezaf" (link: conversation sequence)
        - NPC emote: 's eyes glitter with energy as you mention Baldric's Name. 'So I was not mistaken, you do know Baldric. He was a friend, and as a great a mortal as I have ever known. You must be an exceptional mortal yourself if Baldric saw fit to bequeath the blade to you. Yes I know of it. I could feel it's energy around your body. Perhaps fate has brought you to me this day. I am in great need of help .
          - Reply guard: `e.other:HasItem(20542)`
        - NPC say: One of our scouts recently came upon a band of mercenaries in possession of a letter from King Tormax. The letter described a mission to recover relics from the necropolis. This cannot be allowed to happen. The holy resting place of my kin shall not be defiled! Journey to the necropolis and stop the mercenaries. Bring me anything you might find that would provide a clue as to what Tormax has planned.
          - Reply guard: `e.other:HasItem(20542)`
        - Condition: `e.other:Class() == "Bard"`
        - Condition: `e.message:findi("Baldric Slezaf")`
        - Sets `bard15` to `1`.
      - Player: "children of Zek" (link: explicit mention)
        - Prompted by player input: "Hail"
        - NPC emote: lets out a deep growl. You can tell that your question has angered him. 'I find it impossible to believe you have come to this land know nothing of the children of Zek. Do not toy with me, I can see deep into your very soul if I so choose. Perhaps you are a [spy] sent by Tormax to find a weakness in the kin. If you are then both he and you are fools. No mortal will ever expose any weakness in the ranks of the claws.
        - Condition: `e.other:Class() == "Bard"`
        - Condition: `e.message:findi("children of Zek")`
      - Player: "Spy" (link: explicit mention)
        - NPC emote: lowers his massive head slightly and peers down at you. You notice a small spark of light emanating from his eyes and you find yourself completely unable to look away. You feel a benign presence gliding through your thoughts.
        - NPC say: Perhaps you speak the truth mortal. But the trust of the kin is not given lightly. You will have to provide some [proof] for yourself if you wish to gain my trust.
        - Condition: `e.other:Class() == "Bard"`
        - Condition: `e.message:findi("spy")`
      - Player: "Proof" (link: explicit mention)
        - NPC message: The smallest flicker of a grin crosses over Lantaric`Dar's draconic features. 'I was hoping you'd say that. There are three giants that act as heralds for Tormax in this region. Find them, kill them, and bring me their heads to prove your loyalty.'
        - Condition: `e.other:Class() == "Bard"`
        - Condition: `e.message:findi("proof")`
      - Player: "Continue To Aid" (link: external event mention)
        - Prompted by `event_trade`:
          - NPC say: raises his claw to your forehead. The sweat dripping into your eyes does not blur your vision enough to sedate the terror of having a dragon claw mere inches from your face. Lantaric`Dar makes a series of quick, precise motions and then lowers his claw. You feel a mystical energy shiver over your body. 'You have been blessed with my mark. If you [continue to aid] me I may see fit to further increase its power.
          - Event guard: `item_lib.check_turn_in(e.trade, {item1 = 77600,item2 =77600, item3 = 77600})`
        - NPC say: Excellent . I have a matter that I believe you would be suited for. The children of Zek have been strangely silent over the last few days. While your attacks on the couriers certainly slowed them down, I suspect there is something else going on. If you can uncover what they're up to, I will be most pleased. The area around Kael Drakkel is most likely to yield information.
        - Condition: `e.other:Class() == "Bard"`
        - Condition: `e.message:findi("continue to aid")  and qglobals["bardPQ"] == "1"`
3. Kill necropolis/"Excavator Quellin". Spawns "Tarn Macklin" (123164).
4. Loot "Cracked Dragon Bone" (77608) from "Tarn Macklin".
5. wakening/"Lantaric-Dar", hand "Cracked Dragon Bone" (77608). Sets `bard15` to `2`.
6. Spawns "Vesthon's Draconic Abomination" (123171) in `necropolis` on event_hp.
7. Loot "Blackened Dragon Bone" (77612) from "Vesthon's Draconic Abomination".
8. wakening/"Lantaric-Dar", hand "Blackened Dragon Bone" (77612). Sets `bard15` to `3`.
9. Spawns "Needs Heading Validation" (123189) in `necropolis` on event death_complete:123173.
10. Loot "Dark Orb" (77613) from "Needs Heading Validation".
11. wakening/"Lantaric-Dar", hand "Dark Orb" (77613). Sets `bard15` to `4`.
12. Spawns "A Shadow Thief" (20292) in `kithicor` on event death_complete:20291.
13. Loot "Note from Metala" (77627) from "A Shadow Thief".
14. southkarana/"Vhalen Nostrolo", hand "Note from Metala" (77627). Requires `bard15` ==5. Gives "Vhalen's Necklace" (77629).
15. Hand "Vhalen's Necklace" (77629) to potorment/"A Bruised Woman". Spawns "Metala Von Korach" (207084). Loot "Rusted Bile Etched Blade" (77630) from "Metala Von Korach".
16. Spawns "A Shadow Thief" (20292) in `kithicor` on event death_complete:20291.
17. Loot "Crest of Rizlona" (77626) from "A Shadow Thief".
18. Loot "Dragorn Blood" (77639) from "A Dragorn Serf" (NPC 300018) in `wallofslaughter`. Drop cache: 9.52% chance per kill.
19. Summon "Enchanted Velium Bar" (22099) by casting "Enchant Velium", "Mass Enchant Velium", "Greater Mass Enchant Velium".
20. Summon "Cloudy Diamond of Air" (29989) by casting "Imbue Air".
21. Forage "Wind Dragon Crystal" (12783) in `skyfire`.
22. Combine in Jeweler's Kit (20): "Dragorn Blood" (77639), "Enchanted Velium Bar" (22099), "Cloudy Diamond of Air" (29989), "Wind Dragon Crystal" (12783). Produces "Wind Dragon Prism" (77618). Requires Jewelry Making. The combine does not fail.
23. Summon "Red Diamond of Fire" (29986) by casting "Imbue Fire".
24. Forage "Fire Dragon Crystal" (12487) in `skyfire`.
25. Combine in Jeweler's Kit (20): "Dragorn Blood" (77639), "Enchanted Velium Bar" (22099), "Red Diamond of Fire" (29986), "Fire Dragon Crystal" (12487). Produces "Fire Dragon Prism" (77619). Requires Jewelry Making. The combine does not fail.
26. Summon "Aqua Diamond of Water" (29987) by casting "Imbue Water".
27. Forage "Ice Dragon Crystal" (12781) in `skyfire`.
28. Combine in Jeweler's Kit (20): "Dragorn Blood" (77639), "Enchanted Velium Bar" (22099), "Aqua Diamond of Water" (29987), "Ice Dragon Crystal" (12781). Produces "Water Dragon Prism" (77620). Requires Jewelry Making. The combine does not fail.
29. Summon "Brown Diamond of Earth" (29988) by casting "Imbue Earth".
30. Forage "Earth Dragon Crystal" (12782) in `skyfire`.
31. Combine in Jeweler's Kit (20): "Dragorn Blood" (77639), "Enchanted Velium Bar" (22099), "Brown Diamond of Earth" (29988), "Earth Dragon Crystal" (12782). Produces "Earth Dragon Prism" (77621). Requires Jewelry Making. The combine does not fail.
32. Summon "Green Diamond of Disease" (30118) by casting "Imbue Disease".
33. Spawns "A Swamp Dragon" (83249) in `swampofnohope` on event_hp.
34. Loot "Swamp Dragon Crystal" (77614) from "A Swamp Dragon".
35. Combine in Jeweler's Kit (20): "Dragorn Blood" (77639), "Enchanted Velium Bar" (22099), "Green Diamond of Disease" (30118), "Swamp Dragon Crystal" (77614). Produces "Swamp Dragon Prism" (77622). Requires Jewelry Making. The combine does not fail.
36. Summon "Gray Diamond of Storms" (29991) by casting "Imbue Storm".
37. Spawns "A Plains Dragon" (13130) in `northkarana` on event_hp.
38. Loot "Plains Dragon Crystal" (77615) from "A Plains Dragon".
39. Combine in Jeweler's Kit (20): "Dragorn Blood" (77639), "Enchanted Velium Bar" (22099), "Gray Diamond of Storms" (29991), "Plains Dragon Crystal" (77615). Produces "Plains Dragon Prism" (77623). Requires Jewelry Making. The combine does not fail.
40. Summon "Yellow Diamond of Valor" (30489) by casting "Imbue Valor".
41. Spawns "A Forest Dragon" (181224) in `jaggedpine` on event_hp.
42. Loot "Forest Dragon Crystal" (77616) from "A Forest Dragon".
43. Combine in Jeweler's Kit (20): "Dragorn Blood" (77639), "Enchanted Velium Bar" (22099), "Yellow Diamond of Valor" (30489), "Forest Dragon Crystal" (77616). Produces "Forest Dragon Prism" (77624). Requires Jewelry Making. The combine does not fail.
44. Summon "White Diamond of Justice" (29494) by casting "Imbue Justice".
45. Spawns "A Mountain Dragon" (100227) in `stonebrunt` on event_hp.
46. Loot "Mountain Dragon Crystal" (77617) from "A Mountain Dragon".
47. Combine in Jeweler's Kit (20): "Dragorn Blood" (77639), "Enchanted Velium Bar" (22099), "White Diamond of Justice" (29494), "Mountain Dragon Crystal" (77617). Produces "Mountain Dragon Prism" (77625). Requires Jewelry Making. The combine does not fail.
48. Combine in "Crest of Rizlona" (77626): "Wind Dragon Prism" (77618), "Fire Dragon Prism" (77619), "Water Dragon Prism" (77620), "Earth Dragon Prism" (77621), "Swamp Dragon Prism" (77622), "Plains Dragon Prism" (77623), "Forest Dragon Prism" (77624), "Mountain Dragon Prism" (77625). Produces "Draconic Prism" (77628). The combine does not fail.
49. Combine in "Rusted Bile Etched Blade" (77630): "Draconic Prism" (77628). Produces "Prismatic Dragon Blade" (77631). The combine does not fail.

## Epic 2.0

### "Blade of Vesagran" (77640)

1. soltemple/"Walthin Fireweaver", say "Hail". Sets `bard15` to `5`.
2. Loot "Black Chaos Gauntlets" (77641) from "Stone Thrower" in `causeway`.
3. Loot "Black Chaos Gauntlets" (77641) from "A Battle-Scarred Bazu" in `causeway`.
4. Loot "Black Chaos Gauntlets" (77641) from "A Mountain Bazu" in `causeway`.
5. Loot "Black Chaos Gauntlets" (77641) from "A Murkglider Stalker" in `causeway`.
6. Loot "Black Chaos Boots" (77642) from "A Discordling Enchainer" in `wallofslaughter`.
7. Loot "Black Chaos Boots" (77642) from "A Discordling Taskfiend" in `wallofslaughter`.
8. Loot "Black Chaos Boots" (77642) from "A Dragorn Darkwarrior" in `wallofslaughter`.
9. Loot "Black Chaos Boots" (77642) from "A Dragorn Ireknight" in `wallofslaughter`.
10. Loot "Black Chaos Breastplate" (77643) from "A Gelidran Flamefreeze" (NPC 334016) in `riftseekers`. Drop cache: 4.49% chance per kill.
11. Say "Check Lorb" to anguish/"Zone Status".
12. Spawns "Orb of Discordant Energy" (317087).
13. Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy".
14. Alternative: Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy" (NPC 317087) in `anguish`; trigger: anguish/"Zone Status", say "Check Uorb".
15. Alternative: Loot "Globe of Discordant Energy" (47100) from "Ornate Chest" (NPC 317112) in `anguish`; trigger: anguish/"Zone Status", say "Check Amv Chest".
16. Alternative: Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy" (NPC 317087) in `anguish`; trigger: anguish/"Zone Status", say "Signal:999999".
17. Alternative: Loot "Globe of Discordant Energy" (47100) from "Overlords Chest" (NPC 317124) in `anguish`; trigger: anguish/"Zone Status", say "Signal:999999".
18. causeway/"Alkron Wyrmsong", hand "Globe of Discordant Energy" (47100) + "Black Chaos Gauntlets" (77641) + "Black Chaos Boots" (77642) + "Black Chaos Breastplate" (77643). Sets `bard20` to `1`.
19. Say "Summon" to causeway/"Alkron Wyrmsong".
20. Spawns "Oshiruk" (303125).
21. Loot "Dragorn Essence" (77644) from "Oshiruk".
22. Spawns "Needs Heading Validation" (123189) in `necropolis` on event death_complete:123173.
23. Loot "Dark Orb" (77613) from "Needs Heading Validation".
24. wakening/"Lantaric-Dar", say "Baldric Slezaf". Sets `bard15` to `1`.
25. Kill necropolis/"Excavator Quellin". Spawns "Tarn Macklin" (123164).
26. Loot "Cracked Dragon Bone" (77608) from "Tarn Macklin".
27. wakening/"Lantaric-Dar", hand "Cracked Dragon Bone" (77608). Sets `bard15` to `2`.
28. Spawns "Vesthon's Draconic Abomination" (123171) in `necropolis` on event_hp.
29. Loot "Blackened Dragon Bone" (77612) from "Vesthon's Draconic Abomination".
30. wakening/"Lantaric-Dar", hand "Blackened Dragon Bone" (77612). Sets `bard15` to `3`.
31. wakening/"Lantaric-Dar", hand "Dark Orb" (77613). Sets `bard15` to `4`.
32. Spawns "A Shadow Thief" (20292) in `kithicor` on event death_complete:20291.
33. Loot "Note from Metala" (77627) from "A Shadow Thief".
34. southkarana/"Vhalen Nostrolo", hand "Note from Metala" (77627). Requires `bard15` ==5. Gives "Vhalen's Necklace" (77629).
35. Hand "Vhalen's Necklace" (77629) to potorment/"A Bruised Woman". Spawns "Metala Von Korach" (207084). Loot "Rusted Bile Etched Blade" (77630) from "Metala Von Korach".
36. Spawns "A Shadow Thief" (20292) in `kithicor` on event death_complete:20291.
37. Loot "Crest of Rizlona" (77626) from "A Shadow Thief".
38. Loot "Dragorn Blood" (77639) from "A Dragorn Serf" (NPC 300018) in `wallofslaughter`. Drop cache: 9.52% chance per kill.
39. Summon "Enchanted Velium Bar" (22099) by casting "Enchant Velium", "Mass Enchant Velium", "Greater Mass Enchant Velium".
40. Summon "Cloudy Diamond of Air" (29989) by casting "Imbue Air".
41. Forage "Wind Dragon Crystal" (12783) in `skyfire`.
42. Combine in Jeweler's Kit (20): "Dragorn Blood" (77639), "Enchanted Velium Bar" (22099), "Cloudy Diamond of Air" (29989), "Wind Dragon Crystal" (12783). Produces "Wind Dragon Prism" (77618). Requires Jewelry Making. The combine does not fail.
43. Summon "Red Diamond of Fire" (29986) by casting "Imbue Fire".
44. Forage "Fire Dragon Crystal" (12487) in `skyfire`.
45. Combine in Jeweler's Kit (20): "Dragorn Blood" (77639), "Enchanted Velium Bar" (22099), "Red Diamond of Fire" (29986), "Fire Dragon Crystal" (12487). Produces "Fire Dragon Prism" (77619). Requires Jewelry Making. The combine does not fail.
46. Summon "Aqua Diamond of Water" (29987) by casting "Imbue Water".
47. Forage "Ice Dragon Crystal" (12781) in `skyfire`.
48. Combine in Jeweler's Kit (20): "Dragorn Blood" (77639), "Enchanted Velium Bar" (22099), "Aqua Diamond of Water" (29987), "Ice Dragon Crystal" (12781). Produces "Water Dragon Prism" (77620). Requires Jewelry Making. The combine does not fail.
49. Summon "Brown Diamond of Earth" (29988) by casting "Imbue Earth".
50. Forage "Earth Dragon Crystal" (12782) in `skyfire`.
51. Combine in Jeweler's Kit (20): "Dragorn Blood" (77639), "Enchanted Velium Bar" (22099), "Brown Diamond of Earth" (29988), "Earth Dragon Crystal" (12782). Produces "Earth Dragon Prism" (77621). Requires Jewelry Making. The combine does not fail.
52. Summon "Green Diamond of Disease" (30118) by casting "Imbue Disease".
53. Spawns "A Swamp Dragon" (83249) in `swampofnohope` on event_hp.
54. Loot "Swamp Dragon Crystal" (77614) from "A Swamp Dragon".
55. Combine in Jeweler's Kit (20): "Dragorn Blood" (77639), "Enchanted Velium Bar" (22099), "Green Diamond of Disease" (30118), "Swamp Dragon Crystal" (77614). Produces "Swamp Dragon Prism" (77622). Requires Jewelry Making. The combine does not fail.
56. Summon "Gray Diamond of Storms" (29991) by casting "Imbue Storm".
57. Spawns "A Plains Dragon" (13130) in `northkarana` on event_hp.
58. Loot "Plains Dragon Crystal" (77615) from "A Plains Dragon".
59. Combine in Jeweler's Kit (20): "Dragorn Blood" (77639), "Enchanted Velium Bar" (22099), "Gray Diamond of Storms" (29991), "Plains Dragon Crystal" (77615). Produces "Plains Dragon Prism" (77623). Requires Jewelry Making. The combine does not fail.
60. Summon "Yellow Diamond of Valor" (30489) by casting "Imbue Valor".
61. Spawns "A Forest Dragon" (181224) in `jaggedpine` on event_hp.
62. Loot "Forest Dragon Crystal" (77616) from "A Forest Dragon".
63. Combine in Jeweler's Kit (20): "Dragorn Blood" (77639), "Enchanted Velium Bar" (22099), "Yellow Diamond of Valor" (30489), "Forest Dragon Crystal" (77616). Produces "Forest Dragon Prism" (77624). Requires Jewelry Making. The combine does not fail.
64. Summon "White Diamond of Justice" (29494) by casting "Imbue Justice".
65. Spawns "A Mountain Dragon" (100227) in `stonebrunt` on event_hp.
66. Loot "Mountain Dragon Crystal" (77617) from "A Mountain Dragon".
67. Combine in Jeweler's Kit (20): "Dragorn Blood" (77639), "Enchanted Velium Bar" (22099), "White Diamond of Justice" (29494), "Mountain Dragon Crystal" (77617). Produces "Mountain Dragon Prism" (77625). Requires Jewelry Making. The combine does not fail.
68. Combine in "Crest of Rizlona" (77626): "Wind Dragon Prism" (77618), "Fire Dragon Prism" (77619), "Water Dragon Prism" (77620), "Earth Dragon Prism" (77621), "Swamp Dragon Prism" (77622), "Plains Dragon Prism" (77623), "Forest Dragon Prism" (77624), "Mountain Dragon Prism" (77625). Produces "Draconic Prism" (77628). The combine does not fail.
69. Combine in "Rusted Bile Etched Blade" (77630): "Draconic Prism" (77628). Produces "Prismatic Dragon Blade" (77631). The combine does not fail.
70. causeway/"Alkron Wyrmsong", hand "Dark Orb" (77613) + "Prismatic Dragon Blade" (77631) + "Dragorn Essence" (77644). Gives "Blade of Vesagran" (77640).

## Quest-state progression

## 0. Prerequisites

Shared acquisition steps appear in the first prerequisite chain that needs them. Later sections reference that chain rather than repeating it.

### "Strongbox Half Full of Velixite" (52342)

1. **Broken:** nothing in the graph gives, loots, spawns, or combines Air-Tight Strongbox (52339).
2. No quest step gives Lump of Raw Alloy (52340). The dump lists it in iceclad.
3. Combine in "Air-Tight Strongbox" (52339): "Lump of Raw Alloy" (52340). Produces "Strongbox Full of Alloy" (52341). The combine does not fail.
4. iceclad/"Lookout Larithim", hand "Strongbox Full of Alloy" (52341). Gives "Strongbox Half Full of Velixite" (52342).
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

### "Draconic Prism" (77628)

1. Spawns "A Shadow Thief" (20292) in `kithicor` on event death_complete:20291.
2. Loot "Crest of Rizlona" (77626) from "A Shadow Thief".
3. Loot "Dragorn Blood" (77639) from "A Dragorn Serf" (NPC 300018) in `wallofslaughter`. Drop cache: 9.52% chance per kill.
4. Summon "Enchanted Velium Bar" (22099) by casting "Enchant Velium", "Mass Enchant Velium", "Greater Mass Enchant Velium".
5. Summon "Cloudy Diamond of Air" (29989) by casting "Imbue Air".
6. Forage "Wind Dragon Crystal" (12783) in `skyfire`.
7. Combine in Jeweler's Kit (20): "Dragorn Blood" (77639), "Enchanted Velium Bar" (22099), "Cloudy Diamond of Air" (29989), "Wind Dragon Crystal" (12783). Produces "Wind Dragon Prism" (77618). Requires Jewelry Making. The combine does not fail.
8. Summon "Red Diamond of Fire" (29986) by casting "Imbue Fire".
9. Forage "Fire Dragon Crystal" (12487) in `skyfire`.
10. Combine in Jeweler's Kit (20): "Dragorn Blood" (77639), "Enchanted Velium Bar" (22099), "Red Diamond of Fire" (29986), "Fire Dragon Crystal" (12487). Produces "Fire Dragon Prism" (77619). Requires Jewelry Making. The combine does not fail.
11. Summon "Aqua Diamond of Water" (29987) by casting "Imbue Water".
12. Forage "Ice Dragon Crystal" (12781) in `skyfire`.
13. Combine in Jeweler's Kit (20): "Dragorn Blood" (77639), "Enchanted Velium Bar" (22099), "Aqua Diamond of Water" (29987), "Ice Dragon Crystal" (12781). Produces "Water Dragon Prism" (77620). Requires Jewelry Making. The combine does not fail.
14. Summon "Brown Diamond of Earth" (29988) by casting "Imbue Earth".
15. Forage "Earth Dragon Crystal" (12782) in `skyfire`.
16. Combine in Jeweler's Kit (20): "Dragorn Blood" (77639), "Enchanted Velium Bar" (22099), "Brown Diamond of Earth" (29988), "Earth Dragon Crystal" (12782). Produces "Earth Dragon Prism" (77621). Requires Jewelry Making. The combine does not fail.
17. Summon "Green Diamond of Disease" (30118) by casting "Imbue Disease".
18. Spawns "A Swamp Dragon" (83249) in `swampofnohope` on event_hp.
19. Loot "Swamp Dragon Crystal" (77614) from "A Swamp Dragon".
20. Combine in Jeweler's Kit (20): "Dragorn Blood" (77639), "Enchanted Velium Bar" (22099), "Green Diamond of Disease" (30118), "Swamp Dragon Crystal" (77614). Produces "Swamp Dragon Prism" (77622). Requires Jewelry Making. The combine does not fail.
21. Summon "Gray Diamond of Storms" (29991) by casting "Imbue Storm".
22. Spawns "A Plains Dragon" (13130) in `northkarana` on event_hp.
23. Loot "Plains Dragon Crystal" (77615) from "A Plains Dragon".
24. Combine in Jeweler's Kit (20): "Dragorn Blood" (77639), "Enchanted Velium Bar" (22099), "Gray Diamond of Storms" (29991), "Plains Dragon Crystal" (77615). Produces "Plains Dragon Prism" (77623). Requires Jewelry Making. The combine does not fail.
25. Summon "Yellow Diamond of Valor" (30489) by casting "Imbue Valor".
26. Spawns "A Forest Dragon" (181224) in `jaggedpine` on event_hp.
27. Loot "Forest Dragon Crystal" (77616) from "A Forest Dragon".
28. Combine in Jeweler's Kit (20): "Dragorn Blood" (77639), "Enchanted Velium Bar" (22099), "Yellow Diamond of Valor" (30489), "Forest Dragon Crystal" (77616). Produces "Forest Dragon Prism" (77624). Requires Jewelry Making. The combine does not fail.
29. Summon "White Diamond of Justice" (29494) by casting "Imbue Justice".
30. Spawns "A Mountain Dragon" (100227) in `stonebrunt` on event_hp.
31. Loot "Mountain Dragon Crystal" (77617) from "A Mountain Dragon".
32. Combine in Jeweler's Kit (20): "Dragorn Blood" (77639), "Enchanted Velium Bar" (22099), "White Diamond of Justice" (29494), "Mountain Dragon Crystal" (77617). Produces "Mountain Dragon Prism" (77625). Requires Jewelry Making. The combine does not fail.
33. Combine in "Crest of Rizlona" (77626): "Wind Dragon Prism" (77618), "Fire Dragon Prism" (77619), "Water Dragon Prism" (77620), "Earth Dragon Prism" (77621), "Swamp Dragon Prism" (77622), "Plains Dragon Prism" (77623), "Forest Dragon Prism" (77624), "Mountain Dragon Prism" (77625). Produces "Draconic Prism" (77628). The combine does not fail.

### "Fatestealer" (52347)

1. Unresolved cyclic prerequisite: `Fatestealer_gal` ==1.
2. Unresolved cyclic prerequisite: `Fatestealer_gal` ==1.
3. Unresolved cyclic prerequisite: `Fatestealer_mar` ==1.
4. Unresolved cyclic prerequisite: `Fatestealer_gal` ==1.
5. Unresolved cyclic prerequisite: `Fatestealer_mar` ==1.
6. Unresolved cyclic prerequisite: `Fatestealer_lyt` ==1.
7. Loot "Signed Agreement" (10246) from "Lythe Songbird" in `freeporteast`.
8. Loot "Signed Agreement" (10246) from "Lythe Songbird" in `freportw`.
9. overthere/"Inem R'Ker", hand "Signed Agreement" (10246). Sets `Fatestealer_lyt` to `1`.
10. Loot "Signed Agreement" (10239) from "Seana Marsinger" in `gfaydark`.
11. Loot "Signed Agreement" (52416) from "Stefan Marsinger" in `gfaydark`.
12. overthere/"Inem R'Ker", hand "Signed Agreement" (10239) + "Signed Agreement" (52416). Sets `Fatestealer_mar` to `1`.
13. Loot "Signed Agreement" (10243) from "Galdorin Visigothe" in `abysmal`.
14. overthere/"Inem R'Ker", hand "Signed Agreement" (10243). Sets `Fatestealer_gal` to `1`.
15. overthere/"Inem R'Ker", hand "Signed Agreement" (10243). Sets `Fatestealer_bard` to `1`.
16. Spawns "a Teir'Dal guardian" (186190) in `hateplaneb` on event death_complete:186114.
17. Loot "Stack of Pages" (52335) from "a Teir'Dal guardian".
18. Alternative: Loot "Stack of Pages" (52335) from "a Teir'Dal guardian" (NPC 186190) in `hateplaneb`; trigger: hateplaneb/"Rogue 1 5", on event death_complete:186100.
19. Alternative: Loot "Stack of Pages" (52335) from "a Teir'Dal guardian" (NPC 186190) in `hateplaneb`; trigger: hateplaneb/"Rogue 1 5", on event death_complete:186112.
20. Alternative: Loot "Stack of Pages" (52335) from "a Teir'Dal guardian" (NPC 186190) in `hateplaneb`; trigger: hateplaneb/"Rogue 1 5", on event death_complete:186116.
21. Alternative: Loot "Stack of Pages" (52335) from "a Teir'Dal guardian" (NPC 186190) in `hateplaneb`; trigger: hateplaneb/"Rogue 1 5", on event death_complete:186098.
22. Alternative: Loot "Stack of Pages" (52335) from "a Teir'Dal guardian" (NPC 186190) in `hateplaneb`; trigger: hateplaneb/"Rogue 1 5", on event death_complete:186115.
23. steamfont/"Yendar Starpyre", hand "Stack of Pages" (52335). Sets `Fatestealer_page` to `1`.
24. **Broken:** no event trigger found for `soldungc/ #event_signal`.
25. Loot "Crystallized Shard of Doomfire" (21339) from "A Furious Magma Guardian".
26. Alternative: Loot "Crystallized Shard of Doomfire" (21339) from "Spawn Wiz 1.5; Pure Flame Elemental" (NPC 278108) in `soldungc`; trigger: soldungc/, on event_signal.
27. Loot "Foul Doomfire Brimstone" (21342) from "A Pool Of Living Lava" (NPC 278043) in `soldungc`. Drop cache: 15.97% chance per kill.
28. Loot "Igneous Rock of Doomfire" (21340) from "Typhoeus" (NPC 278069) in `soldungc`. Drop cache: 35% chance per kill.
29. Loot "Pile of Doomfire Ash" (21341) from "a Taklasinai marauder" (NPC 278075) in `soldungc`. Drop cache: 35% chance per kill.
30. Hand "Crystallized Shard of Doomfire" (21339) + "Igneous Rock of Doomfire" (21340) + "Pile of Doomfire Ash" (21341) + "Foul Doomfire Brimstone" (21342) to soldungc/"The Firewatcher". Spawns "Culthor the Gatekeeper" (278005). Loot "Smoldering Embers of Solusek" (52346) from "Culthor the Gatekeeper".
31. nedaria/"Smith Dandi", hand "Smoldering Embers of Solusek" (52346). Sets `Fatestealer_forge` to `1`.
32. Spawns "a Teir'Dal guardian" (186190) in `hateplaneb` on event death_complete:186114.
33. Loot "Soulstone of Lanys" (52337) from "a Teir'Dal guardian".
34. Alternative: Loot "Soulstone of Lanys" (52337) from "a Teir'Dal guardian" (NPC 186190) in `hateplaneb`; trigger: hateplaneb/"Rogue 1 5", on event death_complete:186100.
35. Alternative: Loot "Soulstone of Lanys" (52337) from "a Teir'Dal guardian" (NPC 186190) in `hateplaneb`; trigger: hateplaneb/"Rogue 1 5", on event death_complete:186112.
36. Alternative: Loot "Soulstone of Lanys" (52337) from "a Teir'Dal guardian" (NPC 186190) in `hateplaneb`; trigger: hateplaneb/"Rogue 1 5", on event death_complete:186116.
37. Alternative: Loot "Soulstone of Lanys" (52337) from "a Teir'Dal guardian" (NPC 186190) in `hateplaneb`; trigger: hateplaneb/"Rogue 1 5", on event death_complete:186098.
38. Alternative: Loot "Soulstone of Lanys" (52337) from "a Teir'Dal guardian" (NPC 186190) in `hateplaneb`; trigger: hateplaneb/"Rogue 1 5", on event death_complete:186115.
39. nedaria/"Lirprin, Head Of Affairs", hand "Soulstone of Lanys" (52337). Requires `Fatestealer_bard` ==1. Requires `Fatestealer_page` ==1. Requires `Fatestealer_forge` ==1. Gives "Fatestealer" (52347).

### `bardPQ`

Values written: 1, 2, 3, 4.

1. wakening/"Lantaric-Dar", hand "Storm Giant Herald Head" (77600) + "Storm Giant Herald Head" (77600) + "Storm Giant Herald Head" (77600). Sets `bardPQ` to `1`.
    - Hand in x1: "Storm Giant Herald Head" (77600).
    - Loot "Storm Giant Herald Head" (77600) from "A Giant Herald" in `wakening`.

2. wakening/"Lantaric-Dar", hand "Kromzek Supply Orders" (77601). Sets `bardPQ` to `2`.
    - Requires `bardPQ` ==1.
    - Hand in x1: "Kromzek Supply Orders" (77601).
    - Loot "Kromzek Supply Orders" (77601) from "A Giant Messenger" in `wakening`.
    - Spawns Cristoc Bonethug (119182).
    - Spawns a Bonethug mercenary (119183).

3. wakening/"Lantaric-Dar", hand "Sealed Letter" (77602). Sets `bardPQ` to `3`.
    - Requires `bardPQ` ==2.
    - Hand in x1: "Sealed Letter" (77602).
    - Hand "Kromzek Supply Orders" (77601) to wakening/"Lantaric-Dar". Spawns "Cristoc Bonethug" (119182). Loot "Sealed Letter" (77602) from "Cristoc Bonethug".

4. iceclad/"Vas Thorel", hand "Sealed Kromzek Scroll" (77603). Sets `bardPQ` to `4`.
    - Requires `bardPQ` ==3.
    - Hand in x1: "Sealed Kromzek Scroll" (77603).
    - Say "Lantaric" to iceclad/"Vas Thorel".
    - Spawns "Noble Oldencamp" (110123).
    - Loot "Sealed Kromzek Scroll" (77603) from "Noble Oldencamp".
    - Dialogue with iceclad/"Vas Thorel":
      - Player: "Hail"
        - NPC emote: eyes you curiously. 'Greetings . What brings you to this frigid place?
        - Condition: `e.message:findi("hail")`
      - Player: "Lantaric" (link: external event mention)
        - Prompted by `event_trade`:
          - NPC say: Well done , but I'm afraid this scroll bears ill tidings indeed. Lantaric must be informed with haste. Take the heads of the necromancers and give them to Lantaric. I have a feeling your work is far from done .
          - Event guard: `qglobals["bardPQ"] == "3" and item_lib.check_turn_in(e.trade, {item1 = 77603})`
        - NPC emote: flashes a sly grin at you. 'So you're the one that's impressed Lantaric`Dar. We'll soon see whether his faith is ill conceived. The emissaries have just arrived at the portal to the south. Several of the mortal races are represented in their ranks. I suspect the Kromzek are attempted to recruit aid for a rather large mystical undertaking. Although for exactly what I don't know. They were lingering at the portal last I saw, no doubt waiting for the escort that isn't coming.' Vas Thorel grins at you again.
          - Reply guard: `qglobals["bardPQ"] == "3"`
        - NPC say: No doubt Tormax has by now learned that his mercenaries are dead and has dispatched another escort. Perhaps the new escort will have further information on what he's planning. Follow the emissaries towards Kael and keep your eyes open for a Kromzek Escort. We can't go leaving those necromancers alive if they're going to be helping the Kromzek. Bring me any information you find. Oh yes, I'm sure Lantaric will want their heads as proof of their involvement.
          - Reply guard: `qglobals["bardPQ"] == "3"`
        - Condition: `e.message:findi("Lantaric")`
        - Spawns NPC 110123.
        - Spawns NPC 110128.
        - Spawns NPC 110127.
        - Spawns NPC 110126.
        - Spawns NPC 110125.
        - Spawns NPC 110129.
        - Spawns NPC 110130.

#### Steps on `bardPQ` that do not change it

- `iceclad` vas thorel, say lantaric needs `bardPQ` ==3.
  - Spawns Noble Oldencamp (110123).
  - Spawns Amilia Verisue (110128).
  - Spawns Nihilist Xeegarn (110127).
  - Spawns Puella Opalis (110126).
  - Spawns Locis V`Sek (110125).
  - Spawns a frost giant escort (110129).
  - Spawns a frost giant warrior (110130).
  - Loots Sealed Kromzek Scroll (77603).
  - Loots Amilia's Head (77605).
  - Loots Xeegarn's Head (77604).
  - Loots Puella's Head (77606).
  - Loots Locis' Head (77607).
- `wakening` lantaric-dar, hand 77604+77605+77606+77607 needs `bardPQ` ==4.
  - Sets `bard15` to `1`.
  - Turn in Xeegarn's Head (77604).
  - Turn in Amilia's Head (77605).
  - Turn in Puella's Head (77606).
  - Turn in Locis' Head (77607).

### `Fatestealer_bard`

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

    - Subquest `Fatestealer`:
#### `Fatestealer`

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

    - Subquest `Fatestealer_bard` documented earlier.
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
    - Prerequisite: "Fatestealer" (52347). See section 0.

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
    - No quest step gives Wren's Fatestealer (21346). The dump lists it in dranik.
    - Prerequisite: "Fatestealer" (52347). See section 0.
    - Gives "Nightshade, Blade of Entropy" (52348).

###### Steps on `Fatestealer` that do not change it

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
#### Steps on `Fatestealer_bard` that do not change it

- `nedaria` lirprin, head of affairs, hand 52337 needs `Fatestealer_bard` ==1.
  - Sets `Fatestealer` to `2`.
  - Turn in Soulstone of Lanys (52337).
  - Gives Fatestealer (52347).
- `nedaria` smith dandi, say hail needs `Fatestealer_bard` ==1.
  - Sets `Fatestealer_culth` to `1`.
- `nedaria` smith dandi, hand 52346 needs `Fatestealer_bard` ==1.
  - Sets `Fatestealer_forge` to `1`.
  - Turn in Smoldering Embers of Solusek (52346).

### `bard15`

Values written: 1, 2, 3, 4, 5, 6.

1. wakening/"Lantaric-Dar", say "Baldric Slezaf". Sets `bard15` to `1`.
    - Requires `bard15` unset.

Alternative or repeat transition to `bard15` = `1` (not an additional required stage).

1. wakening/"Lantaric-Dar", hand "Xeegarn's Head" (77604) + "Amilia's Head" (77605) + "Puella's Head" (77606) + "Locis' Head" (77607). Sets `bard15` to `1`.
    - Requires `bardPQ` ==4.
    - Hand in x1: "Xeegarn's Head" (77604).
    - Hand in x1: "Amilia's Head" (77605).
    - Hand in x1: "Puella's Head" (77606).
    - Hand in x1: "Locis' Head" (77607).
    - Say "Lantaric" to iceclad/"Vas Thorel".
    - Spawns "Nihilist Xeegarn" (110127).
    - Loot "Xeegarn's Head" (77604) from "Nihilist Xeegarn".
    - Say "Lantaric" to iceclad/"Vas Thorel".
    - Spawns "Amilia Verisue" (110128).
    - Loot "Amilia's Head" (77605) from "Amilia Verisue".
    - Say "Lantaric" to iceclad/"Vas Thorel".
    - Spawns "Puella Opalis" (110126).
    - Loot "Puella's Head" (77606) from "Puella Opalis".
    - Say "Lantaric" to iceclad/"Vas Thorel".
    - Spawns "Locis V'Sek" (110125).
    - Loot "Locis' Head" (77607) from "Locis V'Sek".

    - Subquest `bardPQ` documented earlier.
2. wakening/"Lantaric-Dar", hand "Cracked Dragon Bone" (77608). Sets `bard15` to `2`.
    - Requires `bard15` ==1.
    - Hand in x1: "Cracked Dragon Bone" (77608).
    - Kill necropolis/"Excavator Quellin". Spawns "Tarn Macklin" (123164).
    - Loot "Cracked Dragon Bone" (77608) from "Tarn Macklin".
    - Gives "Cracked Dragon Bone" (77608).

3. wakening/"Lantaric-Dar", hand "Blackened Dragon Bone" (77612). Sets `bard15` to `3`.
    - Requires `bard15` ==2.
    - Hand in x1: "Blackened Dragon Bone" (77612).
    - Spawns "Vesthon's Draconic Abomination" (123171) in `necropolis` on event_hp.
    - Loot "Blackened Dragon Bone" (77612) from "Vesthon's Draconic Abomination".

4. wakening/"Lantaric-Dar", hand "Dark Orb" (77613). Sets `bard15` to `4`.
    - Requires `bard15` ==3.
    - Hand in x1: "Dark Orb" (77613).
    - Spawns "Needs Heading Validation" (123189) in `necropolis` on event death_complete:123173.
    - Loot "Dark Orb" (77613) from "Needs Heading Validation".
    - Gives "Dark Orb" (77613).

5. soltemple/"Walthin Fireweaver", say "Hail". Sets `bard15` to `5`.
    - Requires `bard15` ==4.
    - Dialogue with soltemple/"Walthin Fireweaver":
      - Player: "Hail"
        - NPC say: ! Thank Veeshan you're here! I discovered how to create the draconic prism! The secret has been here all along. One of the ancient crests of the temple was the key! It seems we are not the first bards to undertake the quest for the draconic prism. I'll explain later, but you must hurry, the crest has been stolen! Not a day ago it was here, so the thief can't have gotten far. You must find the thief and recover the crest !
          - Reply guard: `e.other:HasItem(77618) and e.other:HasItem(77619) and e.other:HasItem(77620) and e.other:HasItem(77621) and e.other:HasItem(77622) and e.other:HasItem(77623) and e.other:HasItem(77624) and e.other:HasItem(77625)`
        - NPC say: Good day to you! I am Walthin Fireweaver of the League of Antonican Bards. My friend Cryssia and I are here while we deal in [lambent stones] with the followers of Solusek Ro. If you are interested, Cryssia and I also deal in [lambent armor], the perfect armor for a bard of standing. I also dabble in some research from time to time. I'm a bit of a historian. I study the history of [dragons].
          - Reply guard: ``
        - Condition: `e.message:findi("hail")`
        - Sets `bard15` to `5`.
      - Player: "Dragons" (link: explicit mention)
        - NPC say: Dragons are a fascinating species. I'm currently researching some rare breeds of dragons. I've only found vague references to something the dragons refer to as 'the outsiders'. Unfortunately the texts aren't any more specific then that, and I haven't been able to translate much of the text I've found. One particular [note] has me very puzzled.
          - Reply guard: `qglobals["bard15"] ~= nil and qglobals["bard15"] >= "4"`
        - NPC say: I'm utterly fascinated by all things draconic. There are many tomes in the temple's libraries that catalog much of their species' history. Some day I'll have to travel to the frozen land of Velious and see what other secrets I can learn there.
          - Reply guard: ``
        - Condition: `e.message:findi("dragons")`
      - Player: "Lambent Stones" (link: explicit mention)
        - Prompted by player input: "Hail"
        - NPC say: Lambent stones are gemstones of great power. They are midnight blue in color - if you want more information on them you should ask Genni.
        - Condition: `e.message:findi("lambent stones")`
      - Player: "Lambent Armor" (link: explicit mention)
        - Prompted by player input: "Hail"
        - NPC say: Lambent armor is custom-crafted armor, made especially for bards. It is forged by the MeadowGreen brothers and then enchanted by the followers of Solusek Ro. If you are interested, I can tell you about [lambent gauntlets], [lambent greaves] and [lambent boots]. Cryssia can tell you about other lambent armor.
        - Condition: `e.message:findi("lambent armor")`
      - Player: "Lambent Gauntlets" (link: explicit mention)
        - NPC say: Lambent gauntlets are exceptionally well made gauntlets. If you are interested, I will give you a pair, but you will have to bring me the following items that I need for a trade with the followers of Solusek Ro. I need shin gauntlets from a froglok knight and black silk gloves from Castle Mistmoore. You will also need to talk to Genni about getting me a lambent star ruby. Bring me these items and you will earn lambent gauntlets.
        - Condition: `e.message:findi("lambent gauntlets")`
      - Player: "Lambent Greaves" (link: explicit mention)
        - Prompted by player input: "Lambent Armor"
        - NPC say: There are no finer leggings for a bard than lambent greaves. Collect for me two pairs of lesser greaves and I will give you some. Bring me icy greaves from the caverns of Permafrost and shin greaves from a ghoul knight, as well as a lambent fire opal and I will bestow a pair of lambent greaves upon you .
        - Condition: `e.message:findi("lambent greaves")`
      - Player: "Lambent Boots" (link: explicit mention)
        - Prompted by player input: "Lambent Armor"
        - NPC say: Lambent boots are the boots of choice for most bards. If you can bring me firewalker boots from a Solusek Mage and the middle portion of the rune of the One Eye from Froon then I ill give you a pair of lambent boots. Oh, I almost forgot! I will need a lambent sapphire as well.
        - Condition: `e.message:findi("lambent boots")`
      - Player: "Note" (link: explicit mention)
        - Prompted by player input: "Dragons"
        - NPC say: TODO: This part is not implemented, please report if you know how it should work.
        - Condition: `qglobals["bard15"] ~= nil and qglobals["bard15"] >= "4" and e.message:findi("note")`

6. global/"Global Player", combine recipe 19882. Sets `bard15` to `6`.
    - `recipe:19882` is combined in Rusted Bile Etched Blade (77630).
      - Hand "Vhalen's Necklace" (77629) to potorment/"A Bruised Woman". Spawns "Metala Von Korach" (207084). Loot "Rusted Bile Etched Blade" (77630) from "Metala Von Korach".
      - Put in x1: Draconic Prism (77628).
        - Prerequisite: "Draconic Prism" (77628). See section 0.
      - Produces Prismatic Dragon Blade (77631).
      - The combine does not fail.

#### Steps on `bard15` that do not change it

- `kithicor` player, on enter needs `bard15` ==5.
  - Spawns a cloaked figure (20290).
- `necropolis` player, on enter needs `bard15` set.
  - Spawns he will spawn the rest (123173).
- `necropolis` player, on enter needs `bard15` ==2.
  - Spawns Hsagra`s Shade (123172).
- `necropolis` player, on loot needs `bard15` set.
  - Sets `bard15_dracchest` to `1`.
  - Spawns a chest (283157).
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
- `potorment` a bruised woman, hand 77629 needs `bard15` ==5.
  - Spawns Metala Von Korach (207084).
  - Loots Rusted Bile Etched Blade (77630).
  - Turn in Vhalen's Necklace (77629).
  - Gives Vhalen's Necklace (77629).
- `southkarana` vhalen nostrolo, hand 77627 needs `bard15` ==5.
  - Turn in Note from Metala (77627).
  - Gives Vhalen's Necklace (77629).

### `bard20`

Values written: 1.

1. causeway/"Alkron Wyrmsong", hand "Globe of Discordant Energy" (47100) + "Black Chaos Gauntlets" (77641) + "Black Chaos Boots" (77642) + "Black Chaos Breastplate" (77643). Sets `bard20` to `1`.
    - Hand in x1: "Black Chaos Gauntlets" (77641).
    - Hand in x1: "Black Chaos Boots" (77642).
    - Hand in x1: "Black Chaos Breastplate" (77643).
    - Hand in x1: "Globe of Discordant Energy" (47100).
    - Loot "Black Chaos Gauntlets" (77641) from "Stone Thrower" in `causeway`.
    - Loot "Black Chaos Gauntlets" (77641) from "A Battle-Scarred Bazu" in `causeway`.
    - Loot "Black Chaos Gauntlets" (77641) from "A Mountain Bazu" in `causeway`.
    - Loot "Black Chaos Gauntlets" (77641) from "A Murkglider Stalker" in `causeway`.
    - Loot "Black Chaos Boots" (77642) from "A Discordling Enchainer" in `wallofslaughter`.
    - Loot "Black Chaos Boots" (77642) from "A Discordling Taskfiend" in `wallofslaughter`.
    - Loot "Black Chaos Boots" (77642) from "A Dragorn Darkwarrior" in `wallofslaughter`.
    - Loot "Black Chaos Boots" (77642) from "A Dragorn Ireknight" in `wallofslaughter`.
    - Loot "Black Chaos Breastplate" (77643) from "A Gelidran Flamefreeze" (NPC 334016) in `riftseekers`. Drop cache: 4.49% chance per kill.
    - Say "Check Lorb" to anguish/"Zone Status".
    - Spawns "Orb of Discordant Energy" (317087).
    - Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy".
    - Alternative: Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy" (NPC 317087) in `anguish`; trigger: anguish/"Zone Status", say "Check Uorb".
    - Alternative: Loot "Globe of Discordant Energy" (47100) from "Ornate Chest" (NPC 317112) in `anguish`; trigger: anguish/"Zone Status", say "Check Amv Chest".
    - Alternative: Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy" (NPC 317087) in `anguish`; trigger: anguish/"Zone Status", say "Signal:999999".
    - Alternative: Loot "Globe of Discordant Energy" (47100) from "Overlords Chest" (NPC 317124) in `anguish`; trigger: anguish/"Zone Status", say "Signal:999999".
    - Spawns Oshiruk (303125).
    - Dialogue with causeway/"Alkron Wyrmsong":
      - Player: "Hail"
        - NPC emote: eye's grow wide when he sees you. 'You've come back! Oshiruk now walks this world once more. We must try to save our world from his devouring maw. I may be able to lure him back here, but I do not have the power to destroy him. If you think you are ready to face him tell me and I will [summon] him.
          - Reply guard: `qglobals["bard20"] == "1"`
        - NPC emote: looks at you with barely contained terror. 'You! You have brought the orb back to this land! You will destroy us all! The terror of Oshiruk cannot be destroyed! Give up your foolish quest while you still can!' He grabs for the orb as you back away slightly. His claw trails across your sword as it draws fresh blood.
          - Reply guard: `qglobals["bard15"] == "6"`
        - NPC say: The blade in your hand begins to glow slightly. Alkron gazes down at the blade with eyes wide. His eyes snap frantically back and forth between your face and the blade, finally coming to rest eye to eye with you. His other claw subconsciously moves to cover the wound from your blade as he continues to stare directly into your eyes. 'You walk a foolish path . No mortal has the power to destroy the chaos that is the spirit of [Oshiruk]. The devourer has power beyond our comprehension. You are a fool if you think that blade will save you. The spirit of the crystalline wyrm has long since left this existence. You are alone in your quest for death.
          - Reply guard: `qglobals["bard15"] == "6"`
        - NPC emote: hisses as he looks down at you. 'Speak , if you dare. I have better things to do then sit here and listen to you and your pathetic kind. You think yourselves powerful for opposing Mata`Muram, but you are like all the rest, you will fall before him and your homes will be destroyed just as ours were.
          - Reply guard: ``
        - Condition: `e.message:findi("hail")`
      - Player: "Oshiruk" (link: explicit mention)
        - NPC emote: cackles darkly. 'You carry his spirit with you and know not who he is? Our worlds are ill fated indeed. But fate is not mine to control, and for my part I will [tell] you of Oshiruk. No warrior should fall before an unknown enemy. It is the legacy of my people, but I fear it will end here with all our deaths.
        - Condition: `qglobals["bard15"] == "6"`
        - Condition: `e.message:findi("Oshiruk")`
      - Player: "Tell" (link: explicit mention)
        - NPC say: Very well, . Millennia ago at the height of the Dragorn empire, a dark portal opened to the north. Not far from the halls of Anguish. We soon found ourselves under siege from a dark army. While we were surprised by their initial appearance, we Dragorn are not weak and were able to fight them back to the portal itself after years of war. Ten years to the day after the opening of the portal, mere days before we would have been able to destroy the portal, Oshiruk first set foot on our world. Oshiruk was rumored to be a dark deity from a reality overcome with discord long ago and that he had come to power by consuming the other deities of his pantheon. He brought a wave of destruction across our world, killing any and all dragorn kin that were sent against his [armies].
        - Condition: `qglobals["bard15"] == "6"`
        - Condition: `e.message:findi("tell")`
      - Player: "Armies" (link: explicit mention)
        - NPC say: Eventually the armies of Oshiruk stood at the gates of Dranik. The hordes of demonic creatures clawed at the gates as we prepared our final defenses, fully expecting to meet our final demise. But the Dragorn were not destined to fall that day. The priests of Vesagran stood stalwart at the gates of our city and that day our god answered us. A great cry was heard and great crystalline wings flapped across the city blowing up an enormous cloud of dust. The titans clashed and ultimately Oshiruk fell that day before the fury of the crystalline dragon. As he struck the ground, Oshiruk's body was consumed in [darkness].
        - Condition: `qglobals["bard15"] == "6"`
        - Condition: `e.message:findi("armies")`
      - Player: "Darkness" (link: explicit mention)
        - NPC say: Dark tentacles lashed out around the corpse and struck the dragon, sending ripples of dark energy across her crystal scales. When the tentacles finally died away, all that was left of the mighty Oshiruk was his infamous dark armor. The chestplate held a black orb that crackled with dark lightning. The dragon reached forward and tore the orb from the chestplate, causing a cataclysmic backlash of evil energy. She collapsed to the ground, overcome by the dark energy. The priests of Vesagran were able to protect her from the remnants of Oshiruk's army, but were not able to keep them from taking the black armor back through the portal to discord. But Vesagran held the orb, and with it the spirit of Oshiruk. The orb and Vesagran have never been seen again until today. How it might be destroyed I don't know, but should the armor ever be reunited with the [orb] Oshiruk would surely return and destroy us all.
        - Condition: `qglobals["bard15"] == "6"`
        - Condition: `e.message:findi("darkness")`
      - Player: "Orb" (link: explicit mention)
        - NPC say: The orb that sits in your very pack holds the soul of Oshiruk you fool! The orb is the source of all his power. But he requires a body in order to resurrect himself into this existence. He certainly wants to reform his former self and to that end will try to find the breastplate, gauntlets and boots of his previous armor. There may be a way to destroy his former body at least. The power of Mata`Muram is vast, perhaps we can use these two evils to destroy each other. Bring me the armor and a globe of discordant energy from the lair of Mata`Muram and I will attempt to destroy the armor and prevent Oshiruk's return.
        - Condition: `qglobals["bard15"] == "6"`
        - Condition: `e.message:findi("orb")`
      - Player: "Summon" (link: explicit mention)
        - Prompted by player input: "Hail"
        - NPC emote: nods at you and begins to scrawl runes on the ground. His voice starts quietly and grows to a dull roar as he recites an incantation of some sort. You feel the ground begin to rumble around you as dark energy pervades your soul. Alkron screams out, 'The devourer is here! Fight for your world Norrathian!
        - Condition: `e.message:findi("summon") and qglobals["bard20"] == "1"`
        - Spawns NPC 303125.

#### Steps on `bard20` that do not change it

- `causeway` alkron wyrmsong, say summon needs `bard20` ==1.
  - Spawns Oshiruk (303125).
  - Loots Dragorn Essence (77644).
- `causeway` player, on loot needs `bard20` ==1.
  - Sets `bard20_chest` to `1`.
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

### Other flags touched along the way

- `bard15_dracchest` set to 1 at necropolis/player.
- `bard15_metalachest` set to 1 at potorment/player.
- `bard20_chest` set to 1 at causeway/player.
