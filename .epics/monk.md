# Monk — Epic Quest Walkthrough

Generated directly from quest-graph item rewards. Unresolved dependencies are marked, not inferred.

## Epic 1.0

### "Celestial Fists" (10652)

<a id="epic-item-10652"></a>

1. erudnext/"Lumi Stergnon", say "Hail".
    - Player: "hail"
      - NPC say: Peace and tranquility be with you. .  Are you a [new acolyte of peace] or are you [here to pay homage] to the child of tranquility?
      - Condition: `(e.message:findi("hail"))`
2. Spawns "Eejag" (npc:27119) via `lavastorm/a fire sprite#challenge eejag`.
3. Kill "Eejag" (NPC 27119) in `lavastorm` and loot "Charred Scale" (1684).
4. airplane/"A Presence", hand "Charred Scale" (1684).
    - event_trade NPC say: Hahaha! That dolt Eejag fell to the likes of you? Im not surprised. So, I guess this means you are here to challenge me. Normally, I wouldnt waste my time, but since you have defeated my younger brother, I suppose Im obligated.
      - Event guard: `((item_lib.check_turn_in(e.trade, {item1 = 1684})) and (e.other:GetLevel() >= 46) and (e.other:Class() == "Monk"))`
5. Spawns "Gwan" (npc:71069) after the hand-in.
6. Kill "Gwan" (NPC 71069) in `airplane` and loot "Breath of Gwan" (1685).
7. nurga/"A Sleeping Ogre", hand "Breath of Gwan" (1685).
    - event_trade NPC say: Your path of wanton destruction ends here. Gwan and Eejag were impatient and hot-headed. You will not defeat me, for I have the patience and perseverance of stone, unlike the children you have beaten before me. Are you sure you want to challenge me?
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 1685}))`
8. Spawns "Trunt" (npc:107161) after the hand-in.
9. Kill "Trunt" (NPC 107161) in `nurga` and loot "Trunt's Head" (1686).
10. lakerathe/"Deep", hand "Trunt's Head" (1686).
    - event_item NPC emote: slowly opens her eyes and looks up at you. She stares at you a long while and then closes her eyes and lowers her head again.
      - Event guard: `((plugin::check_handin(\%itemcount, 1686 => 1)) && ($ulevel >= 46) && ($class eq "Monk"))`
    - event_item NPC say: Very well, $name, if you wish death so greatly, we will be happy to oblige. My master projects part of himself in the wilder lands known as the Overthere. He has granted you an audience. Find him and show him the head of our earth brother. At that point, we will discuss how we will end your life.
11. overthere/"Astral Projection", hand "Trunt's Head" (1686). Gives "Eye of Kaiaren" (1687).
    - event_item NPC emote: looks up and down.
      - Event guard: `(plugin::check_handin(\%itemcount, 1686 => 1))`
      - Event guard: `(defined($qglobals{Trunt}) && $qglobals{Trunt}==1)`
    - event_item NPC say: Hmmm, I was hoping for something more impressive. This is just a small token of the last person who tried to interfere with my plans. He failed as shall you. But tell me truly, are you the one who has so rudely removed my students?
    - event_item NPC emote: ignores you.
      - Event guard: ``
12. lakeofillomen/"Astral Projection", hand "Eye of Kaiaren" (1687).
13. Spawns "Xenevorash" (npc:85208) via `lakeofillomen/vorash#event_death_complete`.
14. Kill "Xenevorash" (NPC 85208) in `lakeofillomen` and loot "Demon Fangs" (1688).
15. Loot "Metal Pipe" (12979) from "a drolvarg pawbuster" (NPC 102122) in `karnor`. Drop cache: 100% chance per kill.
16. Loot "Metal Pipe" (12980) from "an iksar betrayer" (NPC 103193) in `chardok`. Drop cache: 100% chance per kill.
17. Buy "King's Court Token" (66616) from "Keiya Oakwood" (NPC 150311) in `shadowhaven`. Base price: 95,239 copper.
18. shadowhaven/"Gralin Silvertooth", hand "King's Court Token" (66616). Gives "Deluxe Sewing Kit" (17966).
    - event_item NPC say: Better luck next time, $name!
      - Event guard: `(plugin::check_handin(\%itemcount, 66616 => 1))`
      - Event guard: ``
19. Loot "Code of Zan Fi" (12316) from "Targin the Rock" (NPC 32067) in `soldungb`. Drop cache: 100% chance per kill.
20. Loot "Blackburrow Gnoll Pelt" (13027) from "Refugee Splitpaw" (NPC 17023) in `blackburrow`. Drop cache: 55% chance per kill.
21. Loot "Blackburrow Gnoll Skin" (13028) from "the gnoll high shaman" (NPC 17042) in `blackburrow`. Drop cache: 55% chance per kill.
22. Loot "Putrid Rib Bone" (13722) from "a putrid skeleton" (NPC 4148) in `qeytoqrg`. Drop cache: 26.6842% chance per kill.
23. Loot "Gnoll Pup Scalp" (13789) from "a gnoll pup" (NPC 4079) in `qeytoqrg`. Drop cache: 18.15% chance per kill.
24. qeynos2/"Phin Esrinap", hand "Gnoll Pup Scalp" (13789). Gives "White Headband" (10110).
    - event_trade NPC say: Good job, , keep up the good work! Here is your white training headband. Wear it with honor, and make Lu'Sun proud.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 13789,item2 = 13789, item3 = 13789,item4 = 13789}) and fac <= 5)`
25. qeynos2/"Phin Esrinap", hand "Putrid Rib Bone" (13722) + "White Headband" (10110). Gives "Yellow Headband" (10111).
    - event_trade NPC say: Good work.. and, as promised, here is your reward. It is an honor to present this yellow headband to , for recent acts of courage and heroism, on behalf of the Silent Fist Clan.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 13722,item2 = 13722, item3 = 13722,item4 = 10110}))`
26. qeynos2/"Phin Esrinap", hand "Blackburrow Gnoll Pelt" (13027) + "Blackburrow Gnoll Skin" (13028) + "Yellow Headband" (10111). Gives "Orange Headband" (10112).
    - event_trade NPC say: It is an honor to present the orange headband of the Silent Fist Clan to one of our finest members,  the mighty!
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 13027,item2 = 13027, item3 = 13028,item4 = 10111}))`
27. Loot "Head of Ghanex Drah" (13165) from "Ghanex Drah" (NPC 14116) in `southkarana`. Drop cache: 100% chance per kill.
28. Loot "Dareb's Skull" (13166) from "High Shaman Phido" (NPC 14124) in `southkarana`. Drop cache: 100% chance per kill.
29. Loot "Head of Shen" (13167) from "High Shaman Grisok" (NPC 14011) in `southkarana`. Drop cache: 100% chance per kill.
30. qeynos2/"Togahn Sorast", hand "Orange Headband" (10112) + "Head of Ghanex Drah" (13165) + "Dareb's Skull" (13166) + "Head of Shen" (13167). Gives "Red Headband" (10113).
    - event_trade NPC say: We are deeply honored to have such great warrior as part of our Clan. With a proper burial, Shen and Dareb's souls will finally be at peace, and with the death of that vile Ghanex, the plains will be much safer for travelers. It is a great honor to present you, , with the red headband of the Silent Fist Clan.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 10112, item2 =13165, item3 = 13166, item4 = 13167}))`
31. Loot "Skull of Jhen`Tra" (13168) from "a gnoll embalmer" (NPC 51131) in `lakerathe`. Drop cache: 50% chance per kill.
32. Loot "Dagger of Marnek" (13169) from "the thaumaturgist" (NPC 36097) in `befallen`. Drop cache: 28.188% chance per kill.
33. Loot "Zaharn's Coronet" (3000) from "High Priest Zaharn" (NPC 73006) in `permafrost`. Drop cache: 100% chance per kill.
34. qeynos2/"Togahn Sorast", hand "Red Headband" (10113) + "Skull of Jhen`Tra" (13168) + "Dagger of Marnek" (13169) + "Zaharn's Coronet" (3000). Gives "Purple Headband" (10114).
    - event_trade NPC say: In honor of your recent acts of courage and dedication, I reward you, , with the purple headband of the Silent Fist Clan.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 10113, item2 =13168, item3 = 13169, item4 = 3000}))`
35. southkarana/"Brother Qwinn", hand "Code of Zan Fi" (12316) + "Purple Headband" (10114). Gives "Needle of the Void" (12314).
    - event_trade NPC say: We had an agreement. The proof of a skilled monk, the purple headband, and the Code of the Whistling Fist.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 12316,item2 = 10114}))`
    - event_trade NPC say: We thank you for the return of the Code of the Whistling Fist. Take this sewing needle. You shall find it useful should you aid [Brother Zephyl] in his quest. His item, the needle, a swatch of shadow silk and a scroll containing Jonathan's Whistling Warsong. Into a sewing kit they will be going. And into the brotherhood will you. I hope you do not wish me to [return the headband]..
36. Loot "The Idol" (12317) from "Raster of Guk" (NPC 66172) in `gukbottom`. Drop cache: 100% chance per kill.
37. Loot "Blackened Wand" (13237) from "Priest Amiaz" (NPC 36095) in `befallen`. Drop cache: 100% chance per kill.
38. Loot "Blackened Sapphire" (13238) from "Ekeros" (NPC 44102) in `najena`. Drop cache: 90% chance per kill.
39. Loot "Greater Lightstone" (10400) from "a windwillow wisp" (NPC 397070) in `mesa`. Drop cache: 32.7976% chance per kill.
40. Loot "Cutthroat Insignia Ring" (1903) from "a Dervish Cutthroat" (NPC 457074) in `oldcommons`. Drop cache: 55.556% chance per kill.
41. Loot "Legionnaire's Bracer" (2299) from "orc legionnaire" (NPC 21119) in `commons`. Drop cache: 84% chance per kill.
42. Loot "Deathfist Pawn Scalp" (13794) from "orc pawn" (NPC 415088) in `mistythicket`. Drop cache: 50% chance per kill.
43. Loot "Snake Fang" (13067) from "a giant briar snake" (NPC 414061) in `toxxulia`. Drop cache: 58.209% chance per kill.
44. Loot "Useless Cloth Cap" (13894) from "a kobold scout" (NPC 38035) in `tox`. Drop cache: 20% chance per kill.
45. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
46. freeportwest/"Velan Torresk", hand "Deathfist Pawn Scalp" (13794) + "Snake Fang" (13067) + "Bone Chips" (13073). Gives "White Training Sash" (10130).
    - event_trade NPC say: Good work, , you've worked hard and proven yourself a valuable addition to the Ashen Order. Here's your white sash, wear it with pride.
      - Event guard: `(fac < 4)`
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 13794,item2 = 13794,item3 = 13067,item4 = 13073}))`
47. Loot "Giant Snake Rattle" (13058) from "a darkweed snake" (NPC 457018) in `oldcommons`. Drop cache: 43.939% chance per kill.
48. Loot "Deathfist Slashed Belt" (13916) from "High Chief Kellerus" (NPC 457125) in `oldcommons`. Drop cache: 50% chance per kill.
49. Loot "Desert Tarantula Chitin" (20901) from "a dune tarantula" (NPC 392086) in `northro`. Drop cache: 45.5636% chance per kill.
50. freeportwest/"Velan Torresk", hand "White Training Sash" (10130) + "Giant Snake Rattle" (13058) + "Deathfist Slashed Belt" (13916) + "Desert Tarantula Chitin" (20901). Gives "Yellow Sash of Order" (10131).
    - event_trade NPC say: Good work, , you've worked hard and proven yourself a valuable addition to the Ashen Order. Here's your white sash, wear it with pride.
      - Event guard: `(fac < 4)`
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 10130,item2 = 13058,item3 = 13916,item4 = 20901}))`
51. freeportwest/"Reyia Beslin", hand "Greater Lightstone" (10400) + "Cutthroat Insignia Ring" (1903) + "Legionnaire's Bracer" (2299) + "Yellow Sash of Order" (10131). Gives "Orange Sash of Order" (10132).
    - event_trade NPC say: You have proven yourself a mighty warrior. I am honored to present you, , with the orange Sash of Order.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 10400,item2 = 1903,item3 = 2299,item4 = 10131}))`
52. freeportwest/"Reyia Beslin", hand "Blackened Wand" (13237) + "Blackened Sapphire" (13238) + "Orange Sash of Order" (10132). Gives "Red Sash of Order" (10133).
    - event_trade NPC say: Great job,  ! Congratulations. With the destruction of these evil items, the wand of the Burning Dead will never bring harm to anyone on Norrath again. It is my honor to present to you, on behalf of Master Closk and the Ashen Order, the red sash. May Quellious be with you always.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 13237,item2 = 13238,item3 = 10132}))`
53. rathemtn/"Brother Zephyl", hand "The Idol" (12317) + "Red Sash of Order" (10133). Gives "Rare Robe Pattern" (12315).
    - event_item NPC say: We had an agreement. The proof of a skilled monk, the red sash, and the idol of Zan Fi.
      - Event guard: `(plugin::check_handin(\%itemcount, 12317 => 1, 10133 => 1))`
    - event_item NPC say: We thank you for the return of the idol of Zan Fi. Take this rare robe pattern. You shall find it useful should you aid [Brother Qwinn] in his quest. His item, the rare robe pattern, a swatch of shadow silk and a scroll containing Jonathan's Whistling Warsong. Into a sewing kit they will be going. And into the brotherhood will you. I hope you do not wish me to [return the sash].
54. Buy "Song: Jonthan's Whistling Warsong" (15734) from "Lysric Loresinger" (NPC 1035) in `qeynos`. Base price: 43 copper.
55. Buy "Needle Mold" (12019) from "Dyona Rossook" (NPC 5065) in `highpass`. Base price: 180 copper.
56. Buy "Thimble Mold" (12057) from "Dyona Rossook" (NPC 5065) in `highpass`. Base price: 180 copper.
57. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
    - Player: "battle the undead"
      - NPC say: Then you shall venture to Toxxulia Forest. There has been an increase in skeleton sightings lately. I do not know their origin, but I believe that your efforts will reduce their numbers! Take this box. Return it to me when you have filled it with the bones of these undead creatures and combined it. May Quellious' light guide you.
      - Condition: `(e.message:findi("battle the undead"))`
      - Linked from "new acolyte of peace" (explicit prompt).
58. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). Requires Remove Traps.
59. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
    - event_trade NPC say: You have done well. Let it be known to all that you fight for the Rainkeeper. Go and continue the battle.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 13882}))`
60. Loot "Fine Steel Wakizashi" (6932) from "a corrupted gnome explorer" (NPC 66111) in `gukbottom`. Drop cache: 100% chance per kill.
61. Combine in appropriate tradeskill container: "Fine Steel Wakizashi" (6932), "Water Flask" (13006). Produces "Small Piece of High Quality Ore" (22229). Requires Blacksmithing.
62. Combine in appropriate tradeskill container: "Small Piece of High Quality Ore" (22229), "Water Flask" (13006). Produces "High Quality Metal Bits" (22230). Requires Blacksmithing.
63. Combine in appropriate tradeskill container: "Needle Mold" (12019), "Thimble Mold" (12057), "Water Flask" (13006), "High Quality Metal Bits" (22230). Produces "Vale Sewing Kit" (92882). Requires Blacksmithing.
64. Loot "Shadow Wolf Pelt" (13779) from "a shadow wolf" (NPC 408093) in `commonlands`. Drop cache: 7.6384% chance per kill.
65. Buy "Spell: Gather Shadows" (15522) from "Tagus Wunne" (NPC 10030) in `freporte`. Base price: 43 copper.
66. Forage "Spider Silk" (13041) in `mistmoore` or `mmca` or `mmcb` or `mmcc` or `mmcd` or `mmce` or `mmcf` or `mmcg` or `mmch` or `mmci` or `mmcj`.
67. Combine in "Vale Sewing Kit" (92882): "Spider Silk" (13041). Produces "Silk Swatch" (16482). Requires Tailoring.
68. Combine in "Vale Sewing Kit" (92882): "Shadow Wolf Pelt" (13779), "Spell: Gather Shadows" (15522), "Silk Swatch" (16482). Produces "Shadow Silk" (16483). Requires Tailoring.
69. Combine in "Deluxe Sewing Kit" (17966): "Needle of the Void" (12314), "Rare Robe Pattern" (12315), "Song: Jonthan's Whistling Warsong" (15734), "Shadow Silk" (16483). Produces "Robe of the Lost Circle" (12256). Requires Tailoring.
70. dreadlands/"Brother Balatin", hand "Metal Pipe" (12979) + "Metal Pipe" (12980) + "Robe of the Lost Circle" (12256). Gives "Robe of the Whistling Fists" (12970).
    - event_item NPC emote: holds his arms out and a fine robe materializes before your eyes. You grab it just in time to see the skeleton fade from existence.
      - Event guard: `(plugin::check_handin(\%itemcount, 12979 => 1, 12980 => 1, 12256 => 1))`
71. Loot "Immortals" (18195) from "Faerie of Dismay" (NPC 91012) in `skyfire`. Drop cache: 35% chance per kill.
72. erudnext/"Tomekeeper Danl", hand "Immortals" (18195). Gives "Danl's Reference" (1682).
    - event_trade NPC emote: gasps at the sight of the rare book. 'This is a great find indeed! I can only imagine who you had to.. persuade to give you the book. Our library would be very interested in acquiring this and I am prepared to give you this referral that marks you as a friend of the library. If only [Lheao] could see this.'
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 18195}) and e.other:GetLevel() >= 46 and e.other:Class() == "Monk")`
73. timorous/"Lheao", hand "Robe of the Whistling Fists" (12970) + "Danl's Reference" (1682). Gives "Celestial Fists" (1683).
    - event_item NPC say: Astonishing! To think that you are a master of an order thought to be lost in our world. Forgive my earlier doubts. I believe you are indeed worthy to be given the responsibility of watching over this book. Take great care that it does not fall into the wrong hands as it would be truly disastrous.
      - Event guard: `(plugin::check_handin(\%itemcount, 12970 => 1, 1682 => 1))`
74. trakanon/"Kaiaren", hand "Celestial Fists" (1683). Gives "Book of Celestial Fists" (1689).
    - event_item NPC say: Now, then. Where did you find this, monk? This is not just some light reading to be borrowed from the town library. Who gave this to you?
      - Event guard: `((plugin::check_handin(\%itemcount, 1683 => 1)) && ($ulevel>=46) && ($class=="Monk"))`
    - event_item NPC emote: eyes open wide and he attacks you!
75. trakanon/"Kaiaren", hand "Demon Fangs" (1688) + "Book of Celestial Fists" (1689). Gives "Celestial Fists" (10652).
    - event_item NPC emote: bows his head and breathes a long sigh as if relived of a great weight. He then looks up at you and says, 'I honestly did not believe you could have defeated Vorash. Even though he sought nothing but war and bloodshed, it is a life nonetheless and we must mourn him. I will sew these fangs into magical fist wraps and they shall be yours. Remember Xenevorash. A purpose can be found for every situation and individual. To achieve perfection is to perceive this truth.'
      - Event guard: `((plugin::check_handin(\%itemcount, 1688 => 1, 1689 => 1)) && ($ulevel>=46) && ($class=="Monk"))`

## Epic 1.5

### "Fistwraps of Celestial Discipline" (61025)

<a id="epic-item-61025"></a>

1. Shared prerequisite: see ["Celestial Fists" (10652)](#epic-item-10652), step 1. Follow those instructions again if the required item was consumed or another copy is needed.
2. Loot "Scribed Note" (20435) from "The Keeper" (NPC 301030) in `bloodfields`. Drop cache: 100% chance per kill.
3. lakerathe/"Vortix", say "Diary". Sets `monk_epic` to `4`.
    - Player: "diary"
      - NPC say: Kaiaren's Diary? I haven't seen it in some time now. If I were not such a coward, I would have kept it. I have heard rumors of it being torn in half. Some students that wanted to learn the ways of the Celestial Fists were looking for it a while back. One was a pirate that wanted to only learn the Path of the Silent to gain more treasures than he had. The other, wanted to become the most powerful fighter alive. You may want to seek them out and see if they have located pieces of it. I am sorry I could not be of more help. If you do happen to locate the two pieces, bring them back to me and maybe I will be able to aid you further. Now that you know my secret, there is no reason to remain hidden from the world. You will be able to find me resting in the Plane of Tranquility. Be safe, $name .
      - Condition: `($text=~/diary/i)`
4. Loot "1/2 of Kaiaren's Diary" (48109) from "Wygrish" (NPC 125072) in `sirens`. Drop cache: 100% chance per kill.
5. Loot "1/2 of Kaiaren's Diary" (48110) from "Quigli" (NPC 225231) in `dulak`. Drop cache: 100% chance per kill.
6. potranquility/"Vortix", hand "1/2 of Kaiaren's Diary" (48109) + "1/2 of Kaiaren's Diary" (48110).
    - event_item NPC say: You have found it. Let me look at it for a minute. Ah yes, it has been a while but it is all coming back to me. Whats this though? It seems like what I was [searching] for is located elsewhere.
      - Event guard: `($client->GetGlobal("monk_epic") ==4 && plugin::check_handin(\%itemcount, 48109 => 1, 48110 => 1))`
7. Spawns "Disciple of Moon" (npc:120138) via `westwastes/disciple of moon trap#enter`.
8. Kill "Disciple of Moon" (NPC 120138) in `westwastes` and loot "Symbol of Moon" (48111).
9. Spawns "Disciple of Sun" (npc:175179) via `scarlet/a sun reaver#event_death`.
10. Kill "Disciple of Sun" (NPC 175179) in `scarlet` and loot "Symbol of Sun" (48112).
11. Spawns "The Seventh Hammer" (npc:201074) via `pojustice/player#event_click_door`.
12. Kill "The Seventh Hammer" (NPC 201074) in `pojustice` and loot "Symbol of Order" (48113).
13. Buy "Glaze Mortar" (17882) from "Winn Greenbane" (NPC 5059) in `highpass`. Base price: 1,000 copper.
14. Shared prerequisite: see ["Celestial Fists" (10652)](#epic-item-10652), step 57. Follow those instructions again if the required item was consumed or another copy is needed.
15. Shared prerequisite: see ["Celestial Fists" (10652)](#epic-item-10652), steps 44–45. Follow those instructions again if the required item was consumed or another copy is needed.
16. Shared prerequisite: see ["Celestial Fists" (10652)](#epic-item-10652), steps 58–59. Follow those instructions again if the required item was consumed or another copy is needed.
17. Buy "Firing Sheet" (16906) from "Winn Greenbane" (NPC 5059) in `highpass`. Base price: 10 copper.
18. Loot "Small Block of Clay" (16900) from "a muddite recordkeeper" (NPC 16003) in `beholder`. Drop cache: 5.2127% chance per kill.
19. Combine in appropriate tradeskill container: "Small Block of Clay" (16900), "Water Flask" (13006). Produces "Block of Clay" (16901). Requires Pottery.
20. Combine in appropriate tradeskill container: "Block of Clay" (16901), "Water Flask" (13006). Produces "Large Block of Clay" (16902). Requires Pottery.
21. Buy "Large Bowl Sketch" (16963) from "Min Greyeagle" (NPC 5057) in `highpass`. Base price: 760 copper.
22. Combine in appropriate tradeskill container: "Large Block of Clay" (16902), "Water Flask" (13006), "Large Bowl Sketch" (16963). Produces "Unfired Mixing Bowl" (16930). Requires Pottery.
23. Combine in appropriate tradeskill container: "Firing Sheet" (16906), "Unfired Mixing Bowl" (16930). Produces "Mixing Bowl" (17906). Requires Pottery.
24. Buy "Limestone" (16844) from "Myre" (NPC 67016) in `kaladimb`. Base price: 400 copper.
25. Buy "Lead Sulphide" (16845) from "Myre" (NPC 67016) in `kaladimb`. Base price: 450 copper.
26. Combine in "Mixing Bowl" (17906): "Limestone" (16844), "Lead Sulphide" (16845). Produces "White Lead" (16558). Requires Baking.
27. Collect ground spawn "Permafrost Crystals" (22121) in `permafrost`.
28. Kill citymist/"Npc:90004".
29. Spawns "a black reaver" (npc:90004) via `citymist/npc:90004#event_death_complete`.
30. Kill "a black reaver" (NPC 90004) in `citymist` and loot "Iron Oxide" (22124).
31. Combine in "Glaze Mortar" (17882): "Water Flask" (13006), "White Lead" (16558), "Permafrost Crystals" (22121), "Iron Oxide" (22124). Produces "Divine Crystalline Glaze" (16578). Requires Pottery.
32. Combine in appropriate tradeskill container: "Divine Crystalline Glaze" (16578), "Symbol of Sun" (48112). Produces "Polished Symbol of Sun" (48124). Requires Pottery.
33. Combine in appropriate tradeskill container: "Divine Crystalline Glaze" (16578), "Symbol of Moon" (48111). Produces "Polished Symbol of Moon" (48125). Requires Pottery.
34. Combine in appropriate tradeskill container: "Divine Crystalline Glaze" (16578), "Symbol of Order" (48113). Produces "Polished Symbol of Order" (48126). Requires Pottery.
35. potranquility/"Vortix", say "Hail". Gives "Letter to Stremstin" (48128).
    - Player: "hail"
      - NPC say: Ah, I see you have seen a Disciple. The tokens you now possess are used to represent status among the Order. There used to be a tradesman that would fashion them into sashes for us but I'm afraid he has since passed on. I believe there may be another that has learned his trade. His name is Eryke Stremstin, and you should be able to find him peddling his wares across the land. Take this and give it to him. He should be able to tell you of what you will need to fashion your new sash. Once you have fashioned it please bring it to me.
        - Reply guard: `($client->GetGlobal("monk_epic") >=5 && (plugin::check_hasitem($client, 48111) || plugin::check_hasitem($client, 48112) || plugin::check_hasitem($client, 48113)
	 || plugin::check_hasitem($client, 48124) || plugin::check_hasitem($client, 48125) || plugin::check_hasitem($client, 48126)))`
      - NPC say: It is good to see you $name, but I have no new information to share with you. If you have anything to show me, please do.
        - Reply guard: ``
      - Condition: `($text=~/hail/i)`
36. bazaar/"Eryke Stremstin", hand "Letter to Stremstin" (48128).
    - event_trade NPC say: What's this? A note from Vortix. . .I have not made anything in a long while. I am afraid I cannot be of much use to you except to sell you the required materials. I suppose I could also 'guide' you by telling you what you need to make the garment yourself. . .but that's if the [price] is right.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 48128}))`
37. Buy "Coldain Tanners Kit" (17863) from "Rexx Frostweaver" (NPC 115167) in `thurgadina`. Base price: 10,000 copper.
38. Buy "Belt Pattern" (13807) from "Dyona Rossook" (NPC 5065) in `highpass`. Base price: 50 copper.
39. bazaar/"Eryke Stremstin", say "Hand:Platinum:1000". Gives "Celestial Thread" (48123).
40. Combine in "Coldain Tanners Kit" (17863): "Polished Symbol of Order" (48126), "Polished Symbol of Moon" (48125), "Polished Symbol of Sun" (48124), "Belt Pattern" (13807), "Celestial Thread" (48123). Produces "Initiate's Sash of the Celestial Order" (48127). Requires Tailoring.
41. potranquility/"Vortix", hand "Initiate's Sash of the Celestial Order" (48127).
    - event_item NPC say: I see you have gained great strength during your journey as you now wear the Sash of the Celestial Order. I am glad you have made it this far. You will need that for the next steps of your [journey].
      - Event guard: `($client->GetGlobal("monk_epic") ==6 && plugin::check_handin(\%itemcount, 48127 => 1))`
42. Loot "Kaiaren's Mind" (48137) from "Kragsmash" (NPC 301035) in `bloodfields`. Drop cache: 100% chance per kill.
43. Loot "Kaiaren's Body" (48138) from "Windrush" (NPC 335022) in `harbingers`. Drop cache: 100% chance per kill.
44. potranquility/"Vortix", hand "Kaiaren's Mind" (48137) + "Kaiaren's Body" (48138).
    - event_item NPC say: You have proven time and time to be very courageous, $name. Let us hope that lasts for the final issues we must resolve. The Order has seen that Kaiaren will not be ready in time to battle the evil which is growing stronger with every passing day. you must return to the land of Discord and find Vorash. He must be stopped now before he returns to full strength.
      - Event guard: `($client->GetGlobal("monk_epic") ==7 && plugin::check_handin(\%itemcount, 48137 => 1, 48138 => 1))`
45. potranquility/"Vortix", hand "Scribed Note" (20435). Gives "Fistwraps of Celestial Discipline" (61025).
    - event_item NPC say: I can see that you are truly a great member of the Celestial Order now. You have helped the Order when it was needed and have helped me regain the honor which I had lost. The Order has given me the privilege now to bestow upon you the Fistwraps of the Celestial Disciple. May you enjoy your new ranking within the Order. Kaiaren will be pleased to speak to the person responsible for his saving. You may find him wandering the lands with his newfound well-being. I believe the last place he was seen was travelling in the Ocean of Tears. Be safe $name and thank you again.
      - Event guard: `($client->GetGlobal("monk_epic") ==8 && plugin::check_handin(\%itemcount, 20435 => 1))`
    - event_item NPC message: You have gained 5 ability points!

## Epic 2.0

### "Transcended Fistwraps of Immortality" (67742)

<a id="epic-item-67742"></a>

**Earlier reward routes required by this graph path:** ["Fistwraps of Celestial Discipline" (61025)](#epic-item-61025).
Revisit those instructions if another copy of a consumed item is needed.

1. global/"Global Player", say "Recipe:19908". Gives "Globe of Discordant Energy" (47100).
2. Spawns "a chest (epic 2.0)" (npc:893) via `oceanoftears/kaiaren#event_death_complete`.
3. potranquility/"Vortix", hand "Globe of Discordant Energy" (47100).
    - event_item NPC say: By handing me this I already know of the events that have taken place this day. You must not be upset. Everything has balanced itself again. The Order has been restored and we must continue to train in the ways of the Enlightened. Take the globe back, and with it and your Fistwraps of Celestial Discipline, please find Sebast Muckle in Plane of Knowledge and hand them to him. He is a great sage and will be able to know what to do with them to reward you properly.
      - Event guard: `($client->GetGlobal("mnk_epic20") >= 5 && plugin::check_handin(\%itemcount, 47100 => 1))`
4. poknowledge/"Sebast Muckle", hand "Globe of Discordant Energy" (47100) + "Fistwraps of Celestial Discipline" (61025). Gives "Transcended Fistwraps of Immortality" (67742).
    - event_trade NPC message: You have gained 10 ability point(s)!
      - Event guard: `(qglobals["mnk_epic20"] == "6" and item_lib.check_turn_in(e.trade, {item1 = 47100, item2 = 61025}))`
    - event_trade NPC say: I see you have found a way to bring order and balance back to the world. You should have also learned of the need for such evils in the world. There cannot be good without evil just as there cannot be truth without deception. I will take the discordant globe now with your fistwraps and make something wonderful for you from them. They will help guide you through the most difficult of times as a reminder of the knowledge you now possess for without the balance between good and evil we are but lost.
