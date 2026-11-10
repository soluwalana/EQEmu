# Paladin — Epic Quest Walkthrough

Generated directly from quest-graph item rewards. Unresolved dependencies are marked, not inferred.

## Epic 1.0

### "Fiery Defender" (10099)

<a id="epic-item-10099"></a>

1. freeporteast/"Peasant Woman", say "Hail".
    - Player: "hail"
      - NPC emote: grunts as she tries to fill two buckets of [water]. Her frail arms strain at her work and pain fills her eyes with tears.
      - Condition: `(e.message:findi("hail"))`
2. Loot "Tainted Darksteel Sword" (29000) from "Keeper of the Tombs" (NPC 39116) in `hole`. Drop cache: 100% chance per kill.
3. freeporteast/"Peasant Woman", say "I Will Take It". Gives "Bucket of Water" (29008).
    - Player: "i will take it"
      - NPC say: Surely you are a pure soul. If you would take this bucket of water to my brother, I would be forever grateful. I am just so tired, I need to rest... She slumps to the floor and begins to breathe shallowly, in short, harsh gasps.
      - Condition: `(e.other:Class() == "Paladin")`
      - Condition: `(e.message:findi("i will take it"))`
      - Linked from "water" (sequence only; unverified).
4. freeporteast/"Joshua", hand "Bucket of Water" (29008). Gives "Bucket of Pure Water" (29009).
    - event_trade NPC emote: dips his emaciated hand into the bucket and brings the water to his mouth. As he does, you hear a soft thump from outside and notice that through the window his sister has collapsed. A glimmer enfolds her body, and you notice the water in Joshua's hand gleam a pure, bright light for a moment. 'Thank you, sir. I hope my sister returns soon. I feel better for some reason.'
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 29008}))`
5. erudnext/"Reklon Gnallen", hand "Tainted Darksteel Sword" (29000) + "Bucket of Pure Water" (29009). Gives "Gleaming Crested Sword" (29003).
    - event_trade NPC emote: washes the sword's blade in the water of purity. Its dark surface begins to shine, as true as the day it was forged. 'Such a sacrifice is rare among the poor. Truly, the woman must have loved her brother. Remember the lesson you have learned from her. Keep the sword until your work is done.'
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 29000,item2 = 29009}))`
6. Loot "Tainted Darksteel Breastplate" (29001) from "thought destroyer" (NPC 186150) in `hateplaneb`. Drop cache: 100% chance per kill.
7. kaladimb/"Nella Stonebraids", say "Jark". Gives "Cold Plate of Beef and Bread" (29007).
    - Player: "jark"
      - NPC say: Ach! I forgot me husband's dinner. I'm so sorry. I was sendin' my wishes ta Brell for health and long life. I was just floatin' coins into the wishin' pool. Usually it's for children but things haven't been so good lately. Here, please take this to him and tell him where I was.
      - Condition: `($text=~/jark/i || $text=~/dinner/i)`
      - Linked from "hail" (sequence only; unverified).
8. kaladimb/"Jark", hand "Cold Plate of Beef and Bread" (29007). Gives "Pure Crystal" (29006).
    - event_item NPC say: Har, har! No time fer eatin' now! While you were gone I struck me a rich vein. Lookie here! Ya ever seen a gem so pure? It's tiny but clear as glass. Ya take it, $name. Ya showed me some kindness, least I can do. Besides, still a share here for me.
      - Event guard: `(plugin::check_handin(\%itemcount, 29007 => 1))`
9. erudnext/"Reklon Gnallen", hand "Tainted Darksteel Breastplate" (29001) + "Pure Crystal" (29006). Gives "Gleaming Crested Breastplate" (29004).
    - event_trade NPC emote: presses the gem of purity against the breastplate. Its dark gleam softens and then glows bright once again. 'Compassion is strong in you. Few so called heroes would sacrifice their time for such a menial task as you performed. Continue your work. Hold this ancient breastplate until you have completed your task.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 29001,item2 = 29006}))`
10. Loot "Tainted Darksteel Shield" (29002) from "Kirak Vil" (NPC 25301) in `nektulos`. Drop cache: 100% chance per kill.
11. felwithea/"Elia The Pure", hand "Tainted Darksteel Shield" (29002). Gives "Gleaming Crested Shield" (29005).
    - event_trade NPC emote: squints and turns her head. 'By the gods, such a twisted aura this has! To see it hurts my eyes. I will help you if for no other reason than to remove such a twisted thing from existence.' She unrolls a scroll from her pack and softly chants over the dark metal shield. She hands it back to you with an exhausted smile on her face. 'Your heart seems pure. If I was able to help at all, I am honored. May the light shine warmly upon you.'
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 29002}))`
12. erudnext/"Reklon Gnallen", hand "Gleaming Crested Sword" (29003) + "Gleaming Crested Breastplate" (29004) + "Gleaming Crested Shield" (29005). Gives "Mark of Atonement" (29010).
    - event_trade NPC say: I never thought our order would see these artifacts again. With the return of these relics we can now put at ease a scar upon the history of our order. This cleansing will atone for his failure. Your soul must be pure to have given so freely of yourself. Go now, take this crested token of our order. If you wish to free his soul you must undertake another sacrifice.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 29003,item2 = 29004,item3 = 29005}))`
13. Buy "Drom's Champagne" (13829) from "Henna Treghost" (NPC 10063) in `freporte`. Base price: 100 copper.
14. freeporteast/"Tykar Renlin", hand "Drom's Champagne" (13829). Gives "Bunker Cell #1" (12196).
15. potranquility/"Elder Fuirstel", say "Hail". Sets `pop_cod_final` to `1`.
    - Player: "hail"
      - NPC message: Elder Fuirstel slowly turns towards you. You can feel the heat radiating from his face. The warding that envelopes your body reaches out and begins to surround him. You immediately see improvement in his condition. The pus filled sores covering his face and his burning fever start to vanish.
      - NPC say: Thank you friend. I no longer feel the touch of death on my soul. However I do feel the grasp on Bertoxxulous, his plague is still upon me but not spreading throughout my body. I fear the only way to remove this pox would be to weaken Bertoxxulous enough that his curse would be lifted. I now renounce my faith in Bertoxxulous, please fell this god so that I may continue and learn from my mistakes.
      - NPC message: You receive a character flag!
      - Condition: `($text=~/hail/i && $pop_pod_alder_fuirstel == 1 && $pop_pod_grimmus_planar_projection == 1 && $pop_pod_elder_fuirstel == undef)`
16. poknowledge/"Aid Grimel", say "Skill In Brewing". Gives "Portable Drink Barrel" (17179).
    - Player: "skill in brewing"
      - NPC say: I bet you could make a wicked brew! However I am forced to drink a refreshing drink while out adventuring. I do have this powder that will give the best drinks quite a bite though. Mix the powder in with two Kaladim Constitutionals and a flask of pure water. If you need more dust just ask for it! Put three twice brewed constitutionals and the signet in this drink barrel. As hard as drink barrels are to get these days, you need to return it to me along with the drink you create with it.
        - Reply guard: `($client->GetRawSkill(65) >= 220)`
      - NPC say: You do not seem to be skilled enough.
        - Reply guard: ``
      - Condition: ``
      - Condition: `(defined($qglobals{pop_cod_final}) && ($qglobals{pop_cod_final} == 1))`
      - Condition: `(($text=~/skill in brewing/i) && plugin::check_hasitem($client, 16249))`
      - Linked from "versed in the art of smithing" (sequence only; unverified).
17. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
    - Player: "battle the undead"
      - NPC say: Then you shall venture to Toxxulia Forest. There has been an increase in skeleton sightings lately. I do not know their origin, but I believe that your efforts will reduce their numbers! Take this box. Return it to me when you have filled it with the bones of these undead creatures and combined it. May Quellious' light guide you.
      - Condition: `(e.message:findi("battle the undead"))`
      - Linked from "new acolyte of peace" (explicit prompt).
18. Loot "Useless Cloth Cap" (13894) from "a kobold scout" (NPC 38035) in `tox`. Drop cache: 20% chance per kill.
19. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
20. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). Requires Remove Traps.
21. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
    - event_trade NPC say: You have done well. Let it be known to all that you fight for the Rainkeeper. Go and continue the battle.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 13882}))`
22. Loot "Snake Scales" (13070) from "a kerra snake" (NPC 98017) in `erudsxing`. Drop cache: 59.227% chance per kill.
23. Loot "Red Wine" (13030) from "a lesser shaman" (NPC 101059) in `warrens`. Drop cache: 8.9243% chance per kill.
24. Loot "Cask" (16580) from "Tugog Grigol" (NPC 50115) in `rathemtn`. Drop cache: 3.4442% chance per kill.
25. Combine in appropriate tradeskill container: "Red Wine" (13030), "Cask" (16580). Produces "Bottle" (16598). Requires Brewing.
26. Combine in "Portable Drink Barrel" (17179): "Water Flask" (13006), "Snake Scales" (13070), "Bottle" (16598). Produces "Bog Juice" (16581). Requires Brewing.
27. Buy "Spit" (17947) from "Frannie" (NPC 3020) in `qrg`. Base price: 200 copper.
28. Loot "Fire Beetle Eye" (10307) from "a klicnik drone" (NPC 2021) in `qeynos2`. Drop cache: 100% chance per kill.
29. Spawns "sepsis rat" (npc:45113) via `qcat/corrupt guard helminth#event_death`.
30. Kill "sepsis rat" (NPC 45113) in `qcat` and loot "Rat Ears" (13072).
31. Combine in "Spit" (17947): "Fire Beetle Eye" (10307), "Rat Ears" (13072). Produces "Edible Goo" (13498). Requires Baking.
32. freeporteast/"A Prisoner", hand "Bunker Cell #1" (12196) + "Bog Juice" (16581) + "Edible Goo" (13498). Gives "H. K. 102" (12143).
    - event_trade NPC say: Bog n Goo.. Blanket too!!
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 12196,item2 = 16581,item3 = 13498}))`
    - event_trade NPC say: Hide, hide, safe, cee.. lerk has the clue.. Must travel.. Travel.. Travel.. Tunaria's corridor..
33. highkeep/"Assistant Kiolna", hand "H. K. 102" (12143). Gives "Sealed Note" (18936).
    - event_trade NPC say: I am sorry to see you check out. Here is all you had in your box. We hope to serve you again. Have a nice day!! Next!
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 12143}))`
34. paw/"Brother Hayle", hand "Sealed Note" (18936). Gives "Note" (18937).
    - event_trade NPC say: Finally!! I see that Ariska has found a noble knight to retrieve Soulfire. Per Ariska's orders I am not to give Soulfire to you until you can show me [proof of nobility]. You must honor both the Temple of Life as well as the Hall of Truth and to a high degree. Only then shall you hold Soulfire.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 18936}))`
35. Spawns "Sir Lucan D`Lere" (npc:9147) via `freportw/sir lucan d-lere#event_death_complete`.
36. Kill "Sir Lucan D`Lere" (NPC 9147) in `freportw` and loot "Testimony of Truth" (18827).
37. freeportwest/"Valeron Dushire", hand "Testimony of Truth" (18827). Gives "Brilliant Sword of Faith" (13947).
    - event_trade NPC say: Praise be to Marr!! You have done the impossible!! Sir Lucan is finally sent to the higher courts of the Tribunal. The city now has a chance to prosper. The Hall of Truth has been redeemed and gives you thanks. Take this, it is the Sword of Faith. May you wield it with righteousness. Beware of the remainder of the militia. They will be hunting for your head.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 18827}))`
38. Loot "Spider Venom Sac" (14018) from "stone spider" (NPC 32057) in `soldungb`. Drop cache: 51% chance per kill.
39. freeportwest/"Merko Quetalis", hand "Spider Venom Sac" (14018). Gives "Token of Bravery" (12144).
    - event_trade NPC say: You have earned the token of bravery. Now you must ask yourself if you are ready to face true fear. You will have but one chance. If you feel you are powerful enough to easily slay that desert tarantula, then hand me both tokens earned and you shall face the Test of Truth.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 14018}))`
40. **Unresolved acquisition:** "Blackbox XIVD" (13344) has no graph or catalog producer.
41. akanon/"Baxok Curhunter", hand "Blackbox XIVD" (13344). Gives "Cloth Shirt" (1004).
42. commonlands/"Altunic Jartin", hand "Cloth Shirt" (1004). Gives "Token of Generosity" (13865).
    - event_item NPC say: Thank you. You are very noble for a squire. I can see you becoming a very valuable asset to the Hall of Truth. Take this token. Tell Merko that you have [earned the Token of Generosity].
      - Event guard: `(plugin::check_handin(\%itemcount, 1004 => 1))`
43. freeportwest/"Merko Quetalis", hand "Token of Bravery" (12144) + "Token of Generosity" (13865).
    - event_trade NPC say: Go to the open sewer across the way. Inside you shall find your opponent. Victory shall bring your final token. Return it to me. Remember our ways and remember our foes. Send them to their judgement in the afterlife. Be swift with your thoughts. May Marr be with you.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 12144, item2 = 13865}))`
44. Spawns "spawns Guard Willia" (npc:383270) after the hand-in.
45. Kill "spawns Guard Willia" (NPC 383270) in `freeportwest` and loot "Token of Truth" (13866).
46. freeportwest/"Merko Quetalis", hand "Token of Truth" (13866). Gives "Testimony" (18828).
    - event_trade NPC say: You have performed well. You have shown your allegiance to truth and cast aside the Freeport Militia. The militia will surely despise you from now on. This is how they treat the Knights of Truth. Beware. The followers of Marr stand alone in this city.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 13866}))`
47. Loot "Glowing Sword Hilt" (12197) from "Xicotl" (NPC 59152) in `mistmoore`. Drop cache: 100% chance per kill.
48. paw/"Brother Hayle", hand "Note" (18937) + "Brilliant Sword of Faith" (13947) + "Testimony" (18828) + "Glowing Sword Hilt" (12197). Gives "SoulFire" (5504).
    - event_trade NPC say: You have proven yourself worthy to hold Soulfire. Do not let her slip into the hands of evil. There are many who wish to free the many trapped souls of shadowknights and necromancers trapped inside the blade. The power of the blade can be called upon to heal you if need be. May Rodcet Nife and the twins of Marr hold you in their glory.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 18937,item2 = 13947,item3 = 18828,item4 = 12197}))`
      - Event guard: `(e.other:GetModCharacterFactionLevel(e.self:GetPrimaryFaction()) >= 750)`
    - event_trade NPC say: Your mere presence disgusts me.  Please remove yourself from my sight.  Until you change yourself and your ways, you are unwelcome in the Temple of Life.
      - Event guard: ``
49. airplane/"Inte Akera", hand "SoulFire" (5504). Gives "Inte's First Blessing" (18033).
    - event_trade NPC say: You have chosen wisely, my friend. Take this note as a token of my blessing upon you.
      - Event guard: `(e.other:GetFaction(e.self) == 1)`
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 5504}))`
50. neriakc/"Selzar L-Crit", say "Armor". Gives "Note to Kanthuk" (2416).
    - Player: "armor"
      - NPC say: Seek Kanthu M'Rekkor and give him this request parchment. When you have outfitted yourself in a suit of armor return to the House of the Ebon Mask and I will grant you [another task].
      - Condition: `($text=~/armor/i)`
      - Linked from "hail" (explicit prompt).
51. butcher/"Kanthuk Ogrebane", hand "Note to Kanthuk" (2416).
    - event_trade NPC say: Ahh, I see you have spoken to Ryshon. You seem tired from your long journey. Sit with me as I tell you a tale. A tale about a true friend of mine, a great man known as [Amstaf Trunolis].
      - Event guard: `item_lib.check_turn_in(e.trade, {item1 = 2416})`
52. butcher/"Kanthuk Ogrebane", say "Strange Image". Gives "Pendant" (2414).
    - Player: "strange image"
      - NPC say: I saw Amstaf lower his head and walked away in silence. He was surronded by two beings carrying a torch. I don't know what it meant, but I swear it was so real. When I awoke both Amstaf and Ambreen were gone. Please find Llara and give this pendant to her. This pendant belonged to Amstaf. She too had a vision that night that may clear things up. If she asks where you got it from, mention my name.
      - Condition: `qglobals["Kanthuk"] ~= nil`
      - Condition: `e.message:findi("strange image")`
      - Linked from "slumber" (explicit prompt).
53. cauldron/"Llara", hand "Pendant" (2414).
    - event_trade NPC say: Oh my, this belongs to Amstaf! Where did you get it?
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 2414}))`
54. cauldron/"Llara", say "Ruathey". Gives "Note to Ruathey" (2417).
    - Player: "ruathey"
      - NPC say: Ruathey is known for her ability to look into people's souls and find truth. Though I wasn't able to find Amstaf, I was able to recover his sword. I believe that by having his sword I am closer to finding him. Take this note to Ruathey and tell her that I sent you.
      - Condition: `(qglobals["Llara"] ~= nil)`
      - Condition: `(e.message:findi("ruathey"))`
      - Linked from "see" (explicit prompt).
55. lavastorm/"Ruathey", hand "Note to Ruathey" (2417).
    - event_trade NPC say: I see that you've spoken to Llara. She too came to me looking for Amstaf. Though she wasn't able to find her friend, she was able to recover his [sword].
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 2417}))`
    - event_item NPC say: I see that you've spoken to Llara. She too came to me looking for Amstaf. Though she wasn't able to find her friend, she was able to recover his [sword].
      - Event guard: `(plugin::check_handin(\%itemcount, 2417 => 1))`
56. lavastorm/"Ruathey", say "Bag". Gives "Nobleman's Bag" (17878).
    - Player: "bag"
      - NPC say: Take this bag and gather the items I've mentioned. I've been told that the Ghoul's Heart can be found in the estate of the undead, while the scroll can be found in the Keep not far from the Karanas. One of the others are rumored to be found near the dwarven city among the goblins. While the last should be found in the caverns of Najena.
      - Condition: `(qglobals["Ruathey"] ~= nil)`
      - Condition: `(e.message:findi("bag"))`
      - Linked from "sword" (explicit prompt).
57. Loot "Ghoul's Heart" (2410) from "a ghoul" (NPC 63011) in `unrest`. Drop cache: 25% chance per kill.
58. Loot "Amstaf's Scroll" (2411) from "a goblin thief" (NPC 6150) in `highkeep`. Drop cache: 35% chance per kill.
59. Loot "Blade of Nobility" (2412) from "a crazed goblin" (NPC 68162) in `butcher`. Drop cache: 10.5658% chance per kill.
60. Loot "Hilt of the Nobleman" (2413) from "a skeleton" (NPC 44025) in `najena`. Drop cache: 11.946% chance per kill.
61. Combine in "Nobleman's Bag" (17878): "Ghoul's Heart" (2410), "Amstaf's Scroll" (2411), "Blade of Nobility" (2412), "Hilt of the Nobleman" (2413). Produces "Ghoulbane" (5403). Requires Remove Traps.
62. airplane/"Inte Akera", hand "Ghoulbane" (5403). Gives "Inte's Second Blessing" (18034).
    - event_trade NPC say: You have chosen wisely, my friend. Take this note as a token of my blessing upon you.
      - Event guard: `(e.other:GetFaction(e.self) == 1)`
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 5403}))`
63. Loot "Torn, Burnt Book" (19071) from "Lord Nagafen" (NPC 32040) in `soldungb`. Drop cache: 38.525% chance per kill.
64. Loot "Torn, Frost-covered Book" (19070) from "Gorenaire" (NPC 86014) in `dreadlands`. Drop cache: 26.3971% chance per kill.
65. neriakb/"Rysva To-Biath", hand "Torn, Burnt Book" (19071) + "Torn, Frost-covered Book" (19070). Gives "Book of Scale" (18302).
66. oceanoftears/"Oracle Of K-Arnon", hand "Book of Scale" (18302). Gives "Miragul's Phylactery" (19072).
67. everfrost/"Lich Of Miragul", hand "Miragul's Phylactery" (19072).
68. Spawns "Spawn Miragul" (npc:30094) after the hand-in.
69. Kill "Spawn Miragul" (NPC 30094) in `everfrost` and loot "Miragul's Head" (19073).
70. Kill "Spawn Miragul" (NPC 30094) in `everfrost` and loot "Miragul's Robe" (1254).
71. airplane/"Inte Akera", hand "Inte's First Blessing" (18033) + "Inte's Second Blessing" (18034) + "Miragul's Head" (19073) + "Miragul's Robe" (1254). Gives "Fiery Avenger" (11050).
    - event_trade NPC say: Long have I awaited this moment. You have done what even I thought impossible. Take this sword, the Fiery Avenger. You have earned both it and my deepest respect.
      - Event guard: `(e.other:GetFaction(e.self) == 1)`
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 18033, item2 = 18034, item3 = 19073, item4 = 1254}))`
72. fearplane/"Irak Altil", hand "Mark of Atonement" (29010) + "Fiery Avenger" (11050). Gives "Fiery Defender" (10099).
    - event_trade NPC emote: screams so loudly it echoes across the valley as the mark and flames of your holy sword touch his rotted bones. As his body twists he quiets and then speaks. 'Your selflessness has made it possible to redeem my honor. With the cleansing of my corruption your own soul has been strengthened. Your power comes from your devotion to your god and with this you have been rewarded. Remember always your purity, devotion, and why you have sacrificed. I must go now to sacrifice myself upon the spear of pain.'
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 29010, item2 = 11050}))`

## Epic 1.5

### "Redemption" (64031)

<a id="epic-item-64031"></a>

1. dawnshroud/"Mikhal Young", say "Hail".
    - Player: "hail"
      - NPC say: I'm so glad to find a fellow knight. Hail to you $name. I was curious, are you traveling through or could you possibly help me [try to find my sister]?
        - Reply guard: `($client->GetGlobal("paladin_epic") ==4)`
      - NPC say: Hello $name.
        - Reply guard: ``
      - Condition: `($text=~/Hail/i)`
2. Spawns "Durunal the Cursebearer" (npc:300087) via `wallofslaughter/player#enter`.
3. Kill "Durunal the Cursebearer" (NPC 300087) in `wallofslaughter` and loot "Dark and Twisted Sword" (69971).
4. hohonora/"Irak Altil", hand "Dark and Twisted Sword" (69971). Gives "Dark and Twisted Sword" (69972).
    - event_trade NPC emote: I see you have destroyed the monster responsible for this plot. This sword, this twisted piece of steel and blood that lies in your hands, must be the instrument used by Durunal to twist and corrupt those he tortured. I can feel that this sword has a dark magical power that he used to forcibly and violently siphon the soul of those he tormented. There is only one way to correct Durunal's wrong-doings, as well as lay to rest the souls of those he tortured. You must take the crystals you have gathered and meld them with the sword. . .give those tormented souls a new purpose and a new meaning. After you have joined the souls with this weapon, I will [tell you about my master].
      - Event guard: `(qglobals["paladin_epic"] == "6" and item_lib.check_turn_in(e.trade, {item1 = 69971}))`
5. Spawns "Rithnok the Tormented" (npc:91193) via `skyfire/dry sapara#hail`.
6. Kill "Rithnok the Tormented" (NPC 91193) in `skyfire` and loot "Rithnok's Soulstone" (69935).
7. skyfire/"Dry Sapara", hand "Rithnok's Soulstone" (69935). Gives "Rithnok's Soulstone" (69936).
    - event_item NPC say: This appears to be a vessel that housed Rithnok's soul. However, it appears to be missing a few shards. Take this soulstone and piece it back together. I have a feeling once this item becomes whole it will lead you to whoever did this to our poor Rithnok. Thank you for releasing him, $name.
      - Event guard: `(plugin::check_handin(\%itemcount, 69935 => 1))`
8. Collect ground spawn "Soulstone Shard" (69937) in `draniksscar`.
9. Collect ground spawn "Soulstone Shard" (69938) in `bloodfields`.
10. Collect ground spawn "Soulstone Shard" (69939) in `causeway`.
11. Collect ground spawn "Soulstone Shard" (69940) in `dranik`.
12. Combine in "Rithnok's Soulstone" (69936): "Soulstone Shard" (69937), "Soulstone Shard" (69938), "Soulstone Shard" (69939), "Soulstone Shard" (69940). Produces "Rithnok's Soulstone" (69941). Requires Remove Traps.
13. Spawns "A Corrupted Koalindl" (npc:69141) via `oot/player#event_fish_success`.
14. Kill "A Corrupted Koalindl" (NPC 69141) in `oot` and loot "Corrupted Koalindl's Heart" (69929).
15. Spawns "A Corrupted Koalindl" (npc:224432) via `gunthak/player#event_fish_success`.
16. Kill "A Corrupted Koalindl" (NPC 224432) in `gunthak` and loot "Corrupted Koalindl's Heart" (69930).
17. Spawns "A Corrupted Koalindl" (npc:93306) via `overthere/player#event_fish_success`.
18. Kill "A Corrupted Koalindl" (NPC 93306) in `overthere` and loot "Corrupted Koalindl's Heart" (69931).
19. Spawns "A Corrupted Koalindl" (npc:182150) via `nedaria/player#event_fish_success`.
20. Kill "A Corrupted Koalindl" (NPC 182150) in `nedaria` and loot "Corrupted Koalindl's Heart" (69932).
21. qeynos2/"Enic Ruklin", hand "Corrupted Koalindl's Heart" (69929) + "Corrupted Koalindl's Heart" (69930) + "Corrupted Koalindl's Heart" (69931) + "Corrupted Koalindl's Heart" (69932).
    - event_trade NPC say: So this is what happened to the Koalindl? This is sad indeed. I have heard that you have stopped a greater tragedy from occuring by treating the pestilence that was being brought to the seas. You have done a very good job, . I present you with a seal of nobility that was given to me long ago. This seal has granted me audiences with many of the different races of Norrath, including the Ring of Scale. Perhaps it will aide you in your journeys. Thank you again, sir.
      - Event guard: `(qglobals["paladin_epic"] >= "3")`
      - Event guard: `item_lib.check_turn_in(e.trade, {item1 = 69929, item2 = 69930, item3 = 69931, item4 = 69932})`
22. dawnshroud/"Mikhal Young", say "Find Anything". Gives "Drema's Locket" (69945).
    - Player: "find anything"
      - NPC say: As we were turning back to Dawnshroud Peaks, my good friend Ryann Desgrey found her locket in the dirt in the Grey. Here, take the locket. Perhaps you will have a better chance of finding her, and perhaps she will come with you once you present her with the locket. Please, let her know that I miss her and that we all want her to come home safely. Go now, noble paladin.
      - Condition: `($client->GetGlobal("paladin_epic") ==4 && $text=~/find anything/i)`
      - Linked from "sister" (explicit prompt).
23. letalis/"Drema Young", hand "Drema's Locket" (69945). Gives "Drema's Fingerbone" (69946).
    - event_trade NPC emote: groans, 'Uuuurgh. . . Crystal. . .' As Drema reaches out to receive the locket, her fingerbone breaks off in your hand.
      - Event guard: `(qglobals["paladin_epic"] ~= nil and qglobals["paladin_epic"] >= "4" and item_lib.check_turn_in(e.trade, {item1 = 69945}))`
24. dawnshroud/"Denns Rootenpaw", hand "Drema's Fingerbone" (69946). Gives "Bone Collector's Bag" (69947).
    - event_item NPC say: What is this? Drema's fingerbone? While I don't usually help paladins, in this situation I will help you and Mikhal investigate this tragedy. Here is what will need to be done: Take this bag and collect three dark skeleton remains, found somewhere here in Luclin. Bring them back to me so that I can cast a dark spell on it. The spell will turn bones into powder, a powder that should revive Drema long enough to have her explain what occurred. Go now and find these bones.
      - Event guard: `($client->GetGlobal("paladin_epic") ==5 && plugin::check_handin(\%itemcount, 69946 => 1))`
25. Loot "Dark Skeleton Remains" (69927) from "a sun revenant" (NPC 171002) in `thegrey`. Drop cache: 11.0475% chance per kill.
26. Loot "Dark Skeleton Remains" (69926) from "disturbed elysian remains" (NPC 176016) in `umbral`. Drop cache: 2.582% chance per kill.
27. Loot "Dark Skeleton Remains" (69925) from "A Soriz Slave" (NPC 162029) in `ssratemple`. Drop cache: 35% chance per kill.
28. Combine in "Bone Collector's Bag" (69947): "Dark Skeleton Remains" (69927), "Dark Skeleton Remains" (69926), "Dark Skeleton Remains" (69925). Produces "Bone Collector's Bag" (69948). Requires Remove Traps.
29. dawnshroud/"Denns Rootenpaw", hand "Bone Collector's Bag" (69948). Gives "Enchanted Bone Powder" (69949).
    - event_item NPC say: Very well, I have turned this collection of bones into powder. Take this powder to Drema and see if it awakens her. Good luck, knight.
      - Event guard: `($client->GetGlobal("paladin_epic") ==5 && plugin::check_handin(\%itemcount, 69948 => 1))`
30. letalis/"Drema Young", hand "Enchanted Bone Powder" (69949).
    - event_trade NPC emote: Please end my torment . I beg of you!
      - Event guard: `(qglobals["paladin_epic"] ~= nil and qglobals["paladin_epic"] >= "5" and item_lib.check_turn_in(e.trade, {item1 = 69949}))`
31. Spawns "Drema Young" (npc:169128) after the hand-in.
32. Kill "Drema Young" (NPC 169128) in `letalis` and loot "Drema's Soulstone" (69928).
33. Loot "Soulstone Shard" (69950) from "Coterie Corruptor" (NPC 172188) in `tenebrous`. Drop cache: 100% chance per kill.
34. Loot "Soulstone Shard" (69951) from "Shade of Mujaki the Devourer".
35. Combine in "Drema's Soulstone" (69928): "Soulstone Shard" (69950), "Soulstone Shard" (69951). Produces "Drema's Soulstone" (69952). Requires Remove Traps.
36. Summon "Foldable Medicine Bag" (17770) by casting "Unfold Medicine Bag".
37. Buy "Fine Potion Vial" (95846) from "Dargon" (NPC 29000) in `halas`. Base price: 1,750 copper.
38. Loot "Robust Shadow Essence" (96911) from "Qua Senshali Xakra" (NPC 158020) in `vexthal`. Drop cache: 28.7245% chance per kill.
39. Loot "Sage Leaf" (14215) from "a Di`zok Herbalist" (NPC 103166) in `chardok`. Drop cache: 6.0319% chance per kill.
40. Loot "Valerian Root" (14230) from "a Sarnak Herb Collector" (NPC 103012) in `chardok`. Drop cache: 3.7457% chance per kill.
41. Buy "Woundwart" (16526) from "Zok Kuluree" (NPC 50164) in `rathemtn`. Base price: 400 copper.
42. Combine in "Foldable Medicine Bag" (17770): "Fine Potion Vial" (95846), "Robust Shadow Essence" (96911), "Sage Leaf" (14215), "Valerian Root" (14230), "Woundwart" (16526). Produces "Mist of the Breathless" (96937). Requires Alchemy.
43. abysmal/"Reiya The Pained", hand "Mist of the Breathless" (96937). Gives "Reiya's Soulstone" (69924).
    - event_item NPC say: Aauuuugh. Ferubi. . .Ferubi is where I was taken. . .' In a bright flash, Reiya has withered away
      - Event guard: `($client->GetGlobal("paladin_epic_reiya") ==1 && plugin::check_handin(\%itemcount, 96937 => 1))`
44. Spawns "Shade of Reiya the Pained" (npc:284104) via `ferubi/player#enter`.
45. Kill "Shade of Reiya the Pained" (NPC 284104) in `ferubi` and loot "Soulstone Shard" (69943).
46. Loot "Soulstone Shard" (69944) from "Vuranish Xxuro" (NPC 290072) in `vxed`. Drop cache: 100% chance per kill.
47. Combine in "Reiya's Soulstone" (69924): "Soulstone Shard" (69943), "Soulstone Shard" (69944). Produces "Reiya's Soulstone" (69942). Requires Remove Traps.
48. Loot "Redis' Soulstone" (69983) from "Shade of Redis Linrok" (NPC 328037) in `dranikcatacombsa`. Drop cache: 100% chance per kill.
49. Combine in "Dark and Twisted Sword" (69972): "Rithnok's Soulstone" (69941), "Drema's Soulstone" (69952), "Reiya's Soulstone" (69942), "Redis' Soulstone" (69983). Produces "Redemption" (64031). Requires Remove Traps.

## Epic 2.0

### "Nightbane, Sword of the Valiant" (48147)

<a id="epic-item-48147"></a>

**Earlier reward routes required by this graph path:** ["Redemption" (64031)](#epic-item-64031).
Revisit those instructions if another copy of a consumed item is needed.

1. provinggrounds/"Pashia Clouddancer", say "Hail".
    - Player: "hail"
      - NPC say: At last I am free again! Thank you so much for saving me from the horrors of this vile place. You have my gratitude. I can find my way out from here friend. Here take this [note] back to my brother. It should explain what good deed you have done for me today.
        - Reply guard: `arrived`
      - NPC say: Uuugh. . .
        - Reply guard: ``
      - Condition: `(e.other:HasItem(69956))`
      - Condition: `(e.message:findi("hail"))`
2. global/"Global Player", say "Recipe:19908". Gives "Globe of Discordant Energy" (47100).
3. airplane/"Inte Akera", hand "Globe of Discordant Energy" (47100). Gives "Scabbard of the Righteous" (69959) + "Token of Loyalty" (69958) + "Token of Conviction" (69957).
    - event_trade NPC say: You have defeated the minions of Anguish and have exceeded my expectations, . You have proven yourself to be a powerful paladin and a savior of all of Norrath. These tokens are the embodiment of your virtues, . Take them and this scabbard and create your final sword. Place all of your tokens into this scabbard along with Redemption and forge the sword out of your own virtues. Today is a joyous day among paladins everywhere, for we have a new mentor lord protector among us.
      - Event guard: `(e.other:HasItem(69953) and e.other:HasItem(69954) and e.other:HasItem(69955) and e.other:HasItem(69956) and item_lib.check_turn_in(e.trade, {item1 = 47100}))`
4. Loot "Valdoon Kel`Novar's Heart" (69981) from "Valdoon Kel`Novar" (NPC 243672) in `mmcc`. Drop cache: 100% chance per kill.
5. felwithea/"Galrun Starforge", hand "Valdoon Kel`Novar's Heart" (69981). Gives "Token of Cleansing" (69956).
    - event_trade NPC say: Amazing, . You have cleansed all of the Mistmoore Catacombs of the impeding Vampire attack, as well as defeated their leader, Valdoon Kel`Novar. I shall take this to Lord Tynkale now and explain everything to him. You have saved us from a potential travesty. Take this, it may aide you in your journeys.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 69981}))`
6. provinggrounds/"Pashia Clouddancer", say "Note". Gives "Note from Pashia" (69973).
    - Player: "note"
      - NPC say: Ok, here's the note for you. Thank you again!
      - Condition: `(e.other:HasItem(69956))`
      - Condition: `(e.message:findi("note") and arrived)`
      - Linked from "hail" (explicit prompt).
7. nedaria/"Duram Firechaser", hand "Note from Pashia" (69973). Gives "Token of Heroism" (69955).
    - event_trade NPC say: Oh my, this brooch is from Keelee? You have saved her? That is great news! Thank you so much for your help, chivalrous knight, for without it Keelee would have not been safe. Take this as a token of my appreciation.
      - Event guard: `(e.other:HasItem(69956))`
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 69973}))`
8. hohonora/"Irak Altil", say "Tell Me About Your Master". Sets `paladin_epic` to `9`.
    - Player: "tell me about your master"
      - NPC say: Yes, this was my final master, the one who rarely taught knights. You have proven yourself to be a powerful and honorable paladin, and you have surpassed anything I could teach you. You have already met my master once, a very long time ago. His name is Inte Ikera, the noblest servant of Prexus. Go to him now with Redemption in hand so that you can begin your training. Good bye and good luck, friend.
      - Condition: `(e.other:HasItem(64031) and e.message:findi("tell me about your master"))`
      - Linked from "new master" (explicit prompt).
9. qeynos2/"Camlend Serbold", say "Gem". Gives "Unfilled Set of Prayer Beads" (69968).
    - Player: "gem"
      - NPC say: The gems that will be needed I can't help you with, . Travel to the city of North Freeport and seek out a holy knight like yourself. Hopefully he will be able to help you for Kernik's sake.
      - Condition: `(qglobals["paladin_epic"] == "9")`
      - Condition: `(e.message:findi("gem"))`
      - Linked from "curing" (sequence only; unverified).
10. rivervale/"Kaya Cloudfoot", say "Different About It". Gives "Note from Kaya" (69970).
    - Player: "different about it"
      - NPC say: I think your eyes should see for themselves. Take this note over to Cheel. He will give you the precious gem of ours. Good luck with your journey .
      - Condition: `(qglobals["paladin_epic"] == "9")`
      - Condition: `(e.message:findi("different about it"))`
      - Linked from "visitor" (explicit prompt).
11. rivervale/"Deputy Cheel", hand "Note from Kaya" (69970). Gives "Rivervale Prayer Bead" (69967).
    - event_trade NPC say: The note looks in order. Here you go . I would be careful holding that out in sight around here though. You need to watch your back around the fool's gold.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 69970}))`
12. akanon/"Lewis Reldnok", say "". Gives "Ak`anon Prayer Bead" (69966).
13. erudnint/"Josper Kenshed", say "Collect Component". Gives "Empty Bag" (17944).
    - Player: "collect component"
      - NPC say: Of course you may assist me!! We have much need of a certain item which can only be found in the frigid peaks of Everfrost. There you shall find creatures called ice goblins. Take this bag and fill it with ice goblin beads and be sure to combine them before you return them. Well, then... Off with you!! And be quick about it and I shall give you a fine wizard's weapon. None of this rust-covered garbage offered by our associates!
      - Condition: `(e.message:findi("collect component"))`
      - Linked from "servant of wizardry" (explicit prompt).
14. Loot "Goblin Ice Necklace" (13897) from "an ice goblin whelp" (NPC 30003) in `everfrost`. Drop cache: 25% chance per kill.
15. Combine in "Empty Bag" (17944): "Goblin Ice Necklace" (13897). Produces "Bag of Ice Necklaces" (13898). Requires Remove Traps.
16. halas/"Lysbith Mcnaff", hand "Bag of Ice Necklaces" (13898). Gives "Iron Ration" (13005).
    - event_trade NPC say: Ye've done well, me young  .  We've gathered these to add to yer provisions.  While in the Everfrost Peaks, be on the watch fer any gnolls ye may find.  I declare there to be a [gnoll bounty].
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 13898}))`
17. Shared prerequisite: see ["Fiery Defender" (10099)](#epic-item-10099), steps 15–16. Follow those instructions again if the required item was consumed or another copy is needed.
18. Shared prerequisite: see ["Fiery Defender" (10099)](#epic-item-10099), step 24. Follow those instructions again if the required item was consumed or another copy is needed.
19. Buy "Hops" (16591) from "Heidi Grainsifter" (NPC 1065) in `qeynos`. Base price: 15 copper.
20. Buy "Malt" (16595) from "Heidi Grainsifter" (NPC 1065) in `qeynos`. Base price: 15 copper.
21. Buy "Yeast" (16596) from "Heidi Grainsifter" (NPC 1065) in `qeynos`. Base price: 15 copper.
22. Combine in "Portable Drink Barrel" (17179): "Cask" (16580), "Hops" (16591), "Malt" (16595), "Yeast" (16596). Produces "Mead" (13008). Requires Brewing.
23. erudnext/"Reklon Gnallen", hand "Iron Ration" (13005) + "Mead" (13008). Gives "Erudin Prayer Bead" (69965).
    - event_trade NPC say: That was excellent . Take this gem and bring peace to Kemik. I don't want to hold you up any longer as you have further to travel on your journey. You should head to the city that sits before giant windmills.
      - Event guard: `(qglobals["paladin_epic"] == "9" and item_lib.check_turn_in(e.trade, {item1 = 13005,item2 = 13008}))`
24. gunthak/"Researcher Alvarik", say "Magician". Gives "Arch Magus Grimoire" (17653).
    - Player: "magician"
      - NPC say: So you too study summoning! Isn't it the most fascinating of the four realms of magic? Well I won't keep you, here is the Arch Magus Grimoire. Good luck to you in your studies.
        - Reply guard: `(($class eq "Magician") && ($client->GetSkill(58) > 100))`
      - Condition: `($text=~/magician/i)`
      - Linked from "wizard" (sequence only; unverified).
25. Loot "Greater Lightstone" (10400) from "a windwillow wisp" (NPC 397070) in `mesa`. Drop cache: 32.7976% chance per kill.
26. northkarana/"Mrysila", hand "Greater Lightstone" (10400). Gives "Concordance of Research" (17504).
    - event_trade NPC say: A greater lightstone? Thank you very much. Here is a 'Concordance of Research' for you.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 10400}))`
27. Kill acrylia/"A Spell Jammer".
28. Kill acrylia/"Ward Of Death".
29. Kill acrylia/"Ward Of Life".
30. Spawns "needs heading validation" (npc:154147) via `acrylia/wdtrpmn#signal:1`.
31. Spawns "Ward of death" (npc:154155) via `acrylia/wdtrpmn#signal:1`.
32. Spawns "Ward of Life -- needs heading validation" (npc:154154) via `acrylia/wdtrpmn#signal:1`.
33. Spawns "EvInvis" (npc:154095) via `acrylia/wdtrpmn#signal:1`.
34. Spawns "RaidMan" (npc:154122) via `acrylia/wdtrpmn#signal:1`.
35. Spawns "grimling" (npc:154129) via `acrylia/evinvis#event_spawn`.
36. Kill "grimling" (NPC 154129) in `acrylia` and loot "Pearl" (10024).
37. Buy "Piece of Parchment" (13063) from "Hanlore Escaval" (NPC 1052) in `qeynos`. Base price: 100 copper.
38. Loot "Undead Froglok Tongue" (16532) from "BoneCracker" (NPC 44095) in `najena`. Drop cache: 25% chance per kill.
39. Loot "Griffon Feathers" (16538) from "Callowwing" (NPC 13115) in `northkarana`. Drop cache: 34% chance per kill.
40. Combine in "Concordance of Research" (17504): "Pearl" (10024), "Piece of Parchment" (13063), "Undead Froglok Tongue" (16532), "Griffon Feathers" (16538). Produces "Quill" (13051). Requires Research.
41. Kill citymist/"90000".
42. Spawns "Neh'Ashir" (npc:90184) via `citymist/90000#event_death_complete`.
43. Kill "Neh'Ashir" (NPC 90184) in `citymist` and loot "Coin of Xev" (65335).
44. Kill citymist/"A Black Reaver".
45. Spawns "a black reaver" (npc:90004) via `citymist/a black reaver#event_death_complete`.
46. Kill "a black reaver" (NPC 90004) in `citymist` and loot "Words of Domination" (65348).
47. Combine in "Arch Magus Grimoire" (17653): "Quill" (13051), "Piece of Parchment" (13063), "Coin of Xev" (65335), "Words of Domination" (65348). Produces "Spell: Quiver of Marr" (19354). Requires Research.
48. Learn "Spell: Quiver of Marr" (19354) and cast "Quiver of Marr" to summon "Quiver of Marr" (17307).
49. rathemtn/"Shin Master Grubbus", hand "Quiver of Marr" (17307). Gives "Gukta Prayer Bead" (69964).
    - event_item NPC say: You are quite the noble Paladin $name. Take this gem and see if it fits into that set of prayer beads. If my memory is correct I believe you will find a similar gem on Odus. You should head that way to continue your journey. Be well $name.
      - Event guard: `($client->GetGlobal("paladin_epic")==9 && plugin::check_handin(\%itemcount, 17307 => 1))`
50. Buy "Barley" (16590) from "Heidi Grainsifter" (NPC 1065) in `qeynos`. Base price: 15 copper.
51. Shared prerequisite: see ["Fiery Defender" (10099)](#epic-item-10099), step 23. Follow those instructions again if the required item was consumed or another copy is needed.
52. Shared prerequisite: see ["Fiery Defender" (10099)](#epic-item-10099), step 25. Follow those instructions again if the required item was consumed or another copy is needed.
53. Buy "Cork" (16851) from "Rylin Coil" (NPC 55027) in `akanon`. Base price: 1 copper.
54. Shared prerequisite: see ["Fiery Defender" (10099)](#epic-item-10099), steps 17–21. Follow those instructions again if the required item was consumed or another copy is needed.
55. Buy "Firing Sheet" (16906) from "Winn Greenbane" (NPC 5059) in `highpass`. Base price: 10 copper.
56. Loot "Small Block of Clay" (16900) from "a muddite recordkeeper" (NPC 16003) in `beholder`. Drop cache: 5.2127% chance per kill.
57. Combine in appropriate tradeskill container: "Small Block of Clay" (16900), "Water Flask" (13006). Produces "Block of Clay" (16901). Requires Pottery.
58. Combine in appropriate tradeskill container: "Block of Clay" (16901), "Water Flask" (13006). Produces "Large Block of Clay" (16902). Requires Pottery.
59. Buy "Large Bowl Sketch" (16963) from "Min Greyeagle" (NPC 5057) in `highpass`. Base price: 760 copper.
60. Combine in appropriate tradeskill container: "Large Block of Clay" (16902), "Water Flask" (13006), "Large Bowl Sketch" (16963). Produces "Unfired Mixing Bowl" (16930). Requires Pottery.
61. Combine in appropriate tradeskill container: "Firing Sheet" (16906), "Unfired Mixing Bowl" (16930). Produces "Mixing Bowl" (17906). Requires Pottery.
62. Buy "Concentrated Celestial Solvent" (96952) from "Gilliad Coldheart" (NPC 121050) in `crystal`. Base price: 372 copper.
63. Kill "a wraith" (NPC 90064) in `citymist` and loot "The Scent of Marr" (11802).
64. Combine in "Mixing Bowl" (17906): "Concentrated Celestial Solvent" (96952), "The Scent of Marr" (11802). Produces "Celestial Essence" (9650). Requires Baking.
65. Combine in "Portable Drink Barrel" (17179): "Water Flask" (13006), "Celestial Essence" (9650). Produces "Purified Water" (12607). Requires Brewing.
66. Forage "Sand Verbena" (65582) in `taka` or `takb` or `takc` or `takd` or `take` or `takf` or `takg` or `takh` or `taki` or `takj`.
67. Combine in appropriate tradeskill container: "Barley" (16590), "Bottle" (16598), "Cork" (16851), "Hops" (16591), "Purified Water" (12607), "Sand Verbena" (65582), "Yeast" (16596). Produces "Bottle of Double Brewed Double Dry Stout" (51157). Requires Brewing.
68. kaladimb/"Datur Nightseer", hand "Bottle of Double Brewed Double Dry Stout" (51157). Gives "Kaladim Prayer Bead" (69963).
    - event_item NPC say: Now that is a tasty beverage!! It sure is strong too for this tiny dwarf! I guess I should give you some kind of thanks. Take this jewel that I found and see if it will help your friend Kemik. I wish I had the second jewel that was with it. You will find that one with a young but brave froglok.
      - Event guard: `($client->GetGlobal("paladin_epic")==9 && plugin::check_handin(\%itemcount, 51157 => 1))`
69. felwithea/"General Jyleel", say "Hand:Platinum:1000". Gives "Felwithe Prayer Bead" (69962).
70. Collect "Freeport Prayer Bead" (69961) at `freeportwest/arem ulosia#gem`.
71. qeynos2/"Ziska Ironforge", say "Hand:Platinum:500". Gives "Qeynos Prayer Bead" (69960).
72. Combine in "Unfilled Set of Prayer Beads" (69968): "Rivervale Prayer Bead" (69967), "Ak`anon Prayer Bead" (69966), "Erudin Prayer Bead" (69965), "Gukta Prayer Bead" (69964), "Kaladim Prayer Bead" (69963), "Felwithe Prayer Bead" (69962), "Freeport Prayer Bead" (69961), "Qeynos Prayer Bead" (69960). Produces "Set of Prayer Beads" (69969). Requires Remove Traps.
73. dranikhollowsc/"Anetal", hand "Set of Prayer Beads" (69969).
    - event_trade NPC say: Thank you  you are very compassionate. My brother must have sent you! Return to him, and he shall reward you. Goodbye, fair knight.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 69969}))`
74. natimbi/"Kemik Arulon", say "Hail". Gives "Token of Compassion" (69953).
    - Player: "hail"
      - NPC say: ! I hear you have saved my sister Anetal! This is very good news indeed. You are truly a daring and compassionate knight. I do not have much to give you for a reward, but this might be valuable to you in your endeavors. Thank you again , and good luck to you, compassionate knight!
        - Reply guard: `(qglobals["paladin_epic_hollowc"] == "2")`
      - NPC say: Now, all that is left to be done is for you to find my sister Anetal in Discord. I have received reports that she is being held in an area called Dranik Hollows. When you are ready, bring these prayer beads with you, gather up a few of your friends, and return to me. I will see about opening up a passageway for you to find her.
        - Reply guard: `(qglobals["paladin_epic_hollowc"] == "1")`
      - NPC say: Cough, cough, hello . I apologize for my cough, my sister and I were injured badly by Muramites in Discord when some of the initial Wayfarers ventured there to explore. I luckily escaped before being mortally injured, but I lost my sister in the exodus. I have been stricken with some odd disease that appears to be eating away at me everyday, and I fear there might not be anything that can cure me. However, maybe you can try to find a cure for me. I have heard a set of prayer beads might cleanse my body of this illness, which can be found in various holy temples throughout Norrath. Curing me might be hard to do, but someone in one of those temples might be willing to help.
        - Reply guard: ``
      - Condition: `(qglobals["paladin_epic"] == "9")`
      - Condition: `(e.message:findi("hail"))`
75. oasis/"Paladin Epic", say "Hail". Gives "Keelee's Brooch" (69982).
    - NPC say: ! You are my savior. Thank you very much for saving me. Here is my Brooch, take it as a symbol of friendship from me to you. I need to depart. I still have some collecting to do.
76. sro/"Instructor Maerceci", hand "Keelee's Brooch" (69982). Gives "Token of Chivalry" (69954).
    - event_trade NPC say: Oh my, this brooch is from Keelee? You have saved her? That is great news! Thank you so much for your help, chivalrous knight, for without it Keelee would have not been safe. Take this as a token of my appreciation.
      - Event guard: `(e.other:HasItem(69953))`
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 69982}))`
77. Combine in "Scabbard of the Righteous" (69959): "Token of Loyalty" (69958), "Token of Conviction" (69957), "Token of Cleansing" (69956), "Token of Heroism" (69955), "Token of Chivalry" (69954), "Token of Compassion" (69953), "Redemption" (64031). Produces "Nightbane, Sword of the Valiant" (48147). Requires Remove Traps.

**Unresolved graph dependencies:**
- Event cycle at `acrylia/wdtrpmn#signal:1`
