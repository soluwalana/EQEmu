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
10. overthere/"Astral Projection", hand "Trunt's Head" (1686). Gives "Eye of Kaiaren" (1687).
    - event_item NPC emote: looks up and down.
      - Event guard: `(plugin::check_handin(\%itemcount, 1686 => 1))`
      - Event guard: `(defined($qglobals{Trunt}) && $qglobals{Trunt}==1)`
    - event_item NPC say: Hmmm, I was hoping for something more impressive. This is just a small token of the last person who tried to interfere with my plans. He failed as shall you. But tell me truly, are you the one who has so rudely removed my students?
    - event_item NPC emote: ignores you.
      - Event guard: ``
11. lakeofillomen/"Astral Projection", hand "Eye of Kaiaren" (1687).
12. Spawns "Xenevorash" (npc:85208) via `lakeofillomen/vorash#event_death_complete`.
13. Kill "Xenevorash" (NPC 85208) in `lakeofillomen` and loot "Demon Fangs" (1688).
14. Loot "Metal Pipe" (12979) from "a drolvarg pawbuster" (NPC 102122) in `karnor`. Drop cache: 100% chance per kill.
15. Loot "Metal Pipe" (12980) from "an iksar betrayer" (NPC 103193) in `chardok`. Drop cache: 100% chance per kill.
16. Buy "King's Court Token" (66616) from "Keiya Oakwood" (NPC 150311) in `shadowhaven`. Base price: 95,239 copper.
17. shadowhaven/"Gralin Silvertooth", hand "King's Court Token" (66616). Gives "Deluxe Sewing Kit" (17966).
    - event_item NPC say: Better luck next time, $name!
      - Event guard: `(plugin::check_handin(\%itemcount, 66616 => 1))`
      - Event guard: ``
18. Loot "Code of Zan Fi" (12316) from "Targin the Rock" (NPC 32067) in `soldungb`. Drop cache: 100% chance per kill.
19. Loot "Blackburrow Gnoll Pelt" (13027) from "Refugee Splitpaw" (NPC 17023) in `blackburrow`. Drop cache: 55% chance per kill.
20. Loot "Blackburrow Gnoll Skin" (13028) from "the gnoll high shaman" (NPC 17042) in `blackburrow`. Drop cache: 55% chance per kill.
21. Loot "Putrid Rib Bone" (13722) from "a putrid skeleton" (NPC 4148) in `qeytoqrg`. Drop cache: 26.6842% chance per kill.
22. Loot "Gnoll Pup Scalp" (13789) from "a gnoll pup" (NPC 4079) in `qeytoqrg`. Drop cache: 18.15% chance per kill.
23. qeynos2/"Phin Esrinap", hand "Gnoll Pup Scalp" (13789). Gives "White Headband" (10110).
    - event_trade NPC say: Good job, , keep up the good work! Here is your white training headband. Wear it with honor, and make Lu'Sun proud.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 13789,item2 = 13789, item3 = 13789,item4 = 13789}) and fac <= 5)`
24. qeynos2/"Phin Esrinap", hand "Putrid Rib Bone" (13722) + "White Headband" (10110). Gives "Yellow Headband" (10111).
    - event_trade NPC say: Good work.. and, as promised, here is your reward. It is an honor to present this yellow headband to , for recent acts of courage and heroism, on behalf of the Silent Fist Clan.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 13722,item2 = 13722, item3 = 13722,item4 = 10110}))`
25. qeynos2/"Phin Esrinap", hand "Blackburrow Gnoll Pelt" (13027) + "Blackburrow Gnoll Skin" (13028) + "Yellow Headband" (10111). Gives "Orange Headband" (10112).
    - event_trade NPC say: It is an honor to present the orange headband of the Silent Fist Clan to one of our finest members,  the mighty!
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 13027,item2 = 13027, item3 = 13028,item4 = 10111}))`
26. Loot "Head of Ghanex Drah" (13165) from "Ghanex Drah" (NPC 14116) in `southkarana`. Drop cache: 100% chance per kill.
27. Loot "Dareb's Skull" (13166) from "High Shaman Phido" (NPC 14124) in `southkarana`. Drop cache: 100% chance per kill.
28. Loot "Head of Shen" (13167) from "High Shaman Grisok" (NPC 14011) in `southkarana`. Drop cache: 100% chance per kill.
29. qeynos2/"Togahn Sorast", hand "Orange Headband" (10112) + "Head of Ghanex Drah" (13165) + "Dareb's Skull" (13166) + "Head of Shen" (13167). Gives "Red Headband" (10113).
    - event_trade NPC say: We are deeply honored to have such great warrior as part of our Clan. With a proper burial, Shen and Dareb's souls will finally be at peace, and with the death of that vile Ghanex, the plains will be much safer for travelers. It is a great honor to present you, , with the red headband of the Silent Fist Clan.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 10112, item2 =13165, item3 = 13166, item4 = 13167}))`
30. Loot "Skull of Jhen`Tra" (13168) from "a gnoll embalmer" (NPC 51131) in `lakerathe`. Drop cache: 50% chance per kill.
31. Loot "Dagger of Marnek" (13169) from "the thaumaturgist" (NPC 36097) in `befallen`. Drop cache: 28.188% chance per kill.
32. Loot "Zaharn's Coronet" (3000) from "High Priest Zaharn" (NPC 73006) in `permafrost`. Drop cache: 100% chance per kill.
33. qeynos2/"Togahn Sorast", hand "Red Headband" (10113) + "Skull of Jhen`Tra" (13168) + "Dagger of Marnek" (13169) + "Zaharn's Coronet" (3000). Gives "Purple Headband" (10114).
    - event_trade NPC say: In honor of your recent acts of courage and dedication, I reward you, , with the purple headband of the Silent Fist Clan.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 10113, item2 =13168, item3 = 13169, item4 = 3000}))`
34. southkarana/"Brother Qwinn", hand "Code of Zan Fi" (12316) + "Purple Headband" (10114). Gives "Needle of the Void" (12314).
    - event_trade NPC say: We had an agreement. The proof of a skilled monk, the purple headband, and the Code of the Whistling Fist.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 12316,item2 = 10114}))`
    - event_trade NPC say: We thank you for the return of the Code of the Whistling Fist. Take this sewing needle. You shall find it useful should you aid [Brother Zephyl] in his quest. His item, the needle, a swatch of shadow silk and a scroll containing Jonathan's Whistling Warsong. Into a sewing kit they will be going. And into the brotherhood will you. I hope you do not wish me to [return the headband]..
35. Loot "The Idol" (12317) from "Raster of Guk" (NPC 66172) in `gukbottom`. Drop cache: 100% chance per kill.
36. Loot "Blackened Wand" (13237) from "Priest Amiaz" (NPC 36095) in `befallen`. Drop cache: 100% chance per kill.
37. Loot "Blackened Sapphire" (13238) from "Ekeros" (NPC 44102) in `najena`. Drop cache: 90% chance per kill.
38. Loot "Greater Lightstone" (10400) from "a windwillow wisp" (NPC 397070) in `mesa`. Drop cache: 32.7976% chance per kill.
39. Loot "Cutthroat Insignia Ring" (1903) from "a Dervish Cutthroat" (NPC 457074) in `oldcommons`. Drop cache: 55.556% chance per kill.
40. Loot "Legionnaire's Bracer" (2299) from "orc legionnaire" (NPC 21119) in `commons`. Drop cache: 84% chance per kill.
41. Loot "Deathfist Pawn Scalp" (13794) from "orc pawn" (NPC 415088) in `mistythicket`. Drop cache: 50% chance per kill.
42. Loot "Snake Fang" (13067) from "a giant briar snake" (NPC 414061) in `toxxulia`. Drop cache: 58.209% chance per kill.
43. Loot "Useless Cloth Cap" (13894) from "a kobold scout" (NPC 38035) in `tox`. Drop cache: 20% chance per kill.
44. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
45. freeportwest/"Velan Torresk", hand "Deathfist Pawn Scalp" (13794) + "Snake Fang" (13067) + "Bone Chips" (13073). Gives "White Training Sash" (10130).
    - event_trade NPC say: Good work, , you've worked hard and proven yourself a valuable addition to the Ashen Order. Here's your white sash, wear it with pride.
      - Event guard: `(fac < 4)`
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 13794,item2 = 13794,item3 = 13067,item4 = 13073}))`
46. Loot "Giant Snake Rattle" (13058) from "a darkweed snake" (NPC 457018) in `oldcommons`. Drop cache: 43.939% chance per kill.
47. Loot "Deathfist Slashed Belt" (13916) from "High Chief Kellerus" (NPC 457125) in `oldcommons`. Drop cache: 50% chance per kill.
48. Loot "Desert Tarantula Chitin" (20901) from "a dune tarantula" (NPC 392086) in `northro`. Drop cache: 45.5636% chance per kill.
49. freeportwest/"Velan Torresk", hand "White Training Sash" (10130) + "Giant Snake Rattle" (13058) + "Deathfist Slashed Belt" (13916) + "Desert Tarantula Chitin" (20901). Gives "Yellow Sash of Order" (10131).
    - event_trade NPC say: Good work, , you've worked hard and proven yourself a valuable addition to the Ashen Order. Here's your white sash, wear it with pride.
      - Event guard: `(fac < 4)`
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 10130,item2 = 13058,item3 = 13916,item4 = 20901}))`
50. freeportwest/"Reyia Beslin", hand "Greater Lightstone" (10400) + "Cutthroat Insignia Ring" (1903) + "Legionnaire's Bracer" (2299) + "Yellow Sash of Order" (10131). Gives "Orange Sash of Order" (10132).
    - event_trade NPC say: You have proven yourself a mighty warrior. I am honored to present you, , with the orange Sash of Order.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 10400,item2 = 1903,item3 = 2299,item4 = 10131}))`
51. freeportwest/"Reyia Beslin", hand "Blackened Wand" (13237) + "Blackened Sapphire" (13238) + "Orange Sash of Order" (10132). Gives "Red Sash of Order" (10133).
    - event_trade NPC say: Great job,  ! Congratulations. With the destruction of these evil items, the wand of the Burning Dead will never bring harm to anyone on Norrath again. It is my honor to present to you, on behalf of Master Closk and the Ashen Order, the red sash. May Quellious be with you always.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 13237,item2 = 13238,item3 = 10132}))`
52. rathemtn/"Brother Zephyl", hand "The Idol" (12317) + "Red Sash of Order" (10133). Gives "Rare Robe Pattern" (12315).
    - event_item NPC say: We had an agreement. The proof of a skilled monk, the red sash, and the idol of Zan Fi.
      - Event guard: `(plugin::check_handin(\%itemcount, 12317 => 1, 10133 => 1))`
    - event_item NPC say: We thank you for the return of the idol of Zan Fi. Take this rare robe pattern. You shall find it useful should you aid [Brother Qwinn] in his quest. His item, the rare robe pattern, a swatch of shadow silk and a scroll containing Jonathan's Whistling Warsong. Into a sewing kit they will be going. And into the brotherhood will you. I hope you do not wish me to [return the sash].
53. Buy "Song: Jonthan's Whistling Warsong" (15734) from "Lysric Loresinger" (NPC 1035) in `qeynos`. Base price: 43 copper.
54. Buy "Needle Mold" (12019) from "Dyona Rossook" (NPC 5065) in `highpass`. Base price: 180 copper.
55. Buy "Thimble Mold" (12057) from "Dyona Rossook" (NPC 5065) in `highpass`. Base price: 180 copper.
56. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
    - Player: "battle the undead"
      - NPC say: Then you shall venture to Toxxulia Forest. There has been an increase in skeleton sightings lately. I do not know their origin, but I believe that your efforts will reduce their numbers! Take this box. Return it to me when you have filled it with the bones of these undead creatures and combined it. May Quellious' light guide you.
      - Condition: `(e.message:findi("battle the undead"))`
      - Linked from "new acolyte of peace" (explicit prompt).
57. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). Requires Remove Traps.
58. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
    - event_trade NPC say: You have done well. Let it be known to all that you fight for the Rainkeeper. Go and continue the battle.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 13882}))`
59. Loot "Fine Steel Wakizashi" (6932) from "a corrupted gnome explorer" (NPC 66111) in `gukbottom`. Drop cache: 100% chance per kill.
60. Combine in appropriate tradeskill container: "Fine Steel Wakizashi" (6932), "Water Flask" (13006). Produces "Small Piece of High Quality Ore" (22229). Requires Blacksmithing.
61. Combine in appropriate tradeskill container: "Small Piece of High Quality Ore" (22229), "Water Flask" (13006). Produces "High Quality Metal Bits" (22230). Requires Blacksmithing.
62. Combine in appropriate tradeskill container: "Needle Mold" (12019), "Thimble Mold" (12057), "Water Flask" (13006), "High Quality Metal Bits" (22230). Produces "Vale Sewing Kit" (92882). Requires Blacksmithing.
63. Loot "Shadow Wolf Pelt" (13779) from "a shadow wolf" (NPC 408093) in `commonlands`. Drop cache: 7.6384% chance per kill.
64. Buy "Spell: Gather Shadows" (15522) from "Tagus Wunne" (NPC 10030) in `freporte`. Base price: 43 copper.
65. Forage "Spider Silk" (13041) in `mistmoore` or `mmca` or `mmcb` or `mmcc` or `mmcd` or `mmce` or `mmcf` or `mmcg` or `mmch` or `mmci` or `mmcj`.
66. Combine in "Vale Sewing Kit" (92882): "Spider Silk" (13041). Produces "Silk Swatch" (16482). Requires Tailoring.
67. Combine in "Vale Sewing Kit" (92882): "Shadow Wolf Pelt" (13779), "Spell: Gather Shadows" (15522), "Silk Swatch" (16482). Produces "Shadow Silk" (16483). Requires Tailoring.
68. Combine in "Deluxe Sewing Kit" (17966): "Needle of the Void" (12314), "Rare Robe Pattern" (12315), "Song: Jonthan's Whistling Warsong" (15734), "Shadow Silk" (16483). Produces "Robe of the Lost Circle" (12256). Requires Tailoring.
69. dreadlands/"Brother Balatin", hand "Metal Pipe" (12979) + "Metal Pipe" (12980) + "Robe of the Lost Circle" (12256). Gives "Robe of the Whistling Fists" (12970).
    - event_item NPC emote: holds his arms out and a fine robe materializes before your eyes. You grab it just in time to see the skeleton fade from existence.
      - Event guard: `(plugin::check_handin(\%itemcount, 12979 => 1, 12980 => 1, 12256 => 1))`
70. Loot "Immortals" (18195) from "Faerie of Dismay" (NPC 91012) in `skyfire`. Drop cache: 35% chance per kill.
71. erudnext/"Tomekeeper Danl", hand "Immortals" (18195). Gives "Danl's Reference" (1682).
    - event_trade NPC emote: gasps at the sight of the rare book. 'This is a great find indeed! I can only imagine who you had to.. persuade to give you the book. Our library would be very interested in acquiring this and I am prepared to give you this referral that marks you as a friend of the library. If only [Lheao] could see this.'
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 18195}) and e.other:GetLevel() >= 46 and e.other:Class() == "Monk")`
72. timorous/"Lheao", hand "Robe of the Whistling Fists" (12970) + "Danl's Reference" (1682). Gives "Celestial Fists" (1683).
    - event_item NPC say: Astonishing! To think that you are a master of an order thought to be lost in our world. Forgive my earlier doubts. I believe you are indeed worthy to be given the responsibility of watching over this book. Take great care that it does not fall into the wrong hands as it would be truly disastrous.
      - Event guard: `(plugin::check_handin(\%itemcount, 12970 => 1, 1682 => 1))`
73. trakanon/"Kaiaren", hand "Celestial Fists" (1683). Gives "Book of Celestial Fists" (1689).
    - event_item NPC say: Now, then. Where did you find this, monk? This is not just some light reading to be borrowed from the town library. Who gave this to you?
      - Event guard: `((plugin::check_handin(\%itemcount, 1683 => 1)) && ($ulevel>=46) && ($class=="Monk"))`
    - event_item NPC emote: eyes open wide and he attacks you!
74. trakanon/"Kaiaren", hand "Demon Fangs" (1688) + "Book of Celestial Fists" (1689). Gives "Celestial Fists" (10652).
    - event_item NPC emote: bows his head and breathes a long sigh as if relived of a great weight. He then looks up at you and says, 'I honestly did not believe you could have defeated Vorash. Even though he sought nothing but war and bloodshed, it is a life nonetheless and we must mourn him. I will sew these fangs into magical fist wraps and they shall be yours. Remember Xenevorash. A purpose can be found for every situation and individual. To achieve perfection is to perceive this truth.'
      - Event guard: `((plugin::check_handin(\%itemcount, 1688 => 1, 1689 => 1)) && ($ulevel>=46) && ($class=="Monk"))`

## Epic 1.5

### "Fistwraps of Celestial Discipline" (61025)

<a id="epic-item-61025"></a>

1. Loot "Scribed Note" (20435) from "The Keeper" (NPC 301030) in `bloodfields`. Drop cache: 100% chance per kill.
2. potranquility/"Vortix", hand "Scribed Note" (20435). Gives "Fistwraps of Celestial Discipline" (61025).
    - event_item NPC say: I can see that you are truly a great member of the Celestial Order now. You have helped the Order when it was needed and have helped me regain the honor which I had lost. The Order has given me the privilege now to bestow upon you the Fistwraps of the Celestial Disciple. May you enjoy your new ranking within the Order. Kaiaren will be pleased to speak to the person responsible for his saving. You may find him wandering the lands with his newfound well-being. I believe the last place he was seen was travelling in the Ocean of Tears. Be safe $name and thank you again.
      - Event guard: `($client->GetGlobal("monk_epic") ==8 && plugin::check_handin(\%itemcount, 20435 => 1))`
    - event_item NPC message: You have gained 5 ability points!

## Epic 2.0

### "Transcended Fistwraps of Immortality" (67742)

<a id="epic-item-67742"></a>

**Earlier reward routes required by this graph path:** ["Fistwraps of Celestial Discipline" (61025)](#epic-item-61025).
Revisit those instructions if another copy of a consumed item is needed.

1. global/"Global Player", say "Recipe:19908". Gives "Globe of Discordant Energy" (47100).
2. poknowledge/"Sebast Muckle", hand "Globe of Discordant Energy" (47100) + "Fistwraps of Celestial Discipline" (61025). Gives "Transcended Fistwraps of Immortality" (67742).
    - event_trade NPC message: You have gained 10 ability point(s)!
      - Event guard: `(qglobals["mnk_epic20"] == "6" and item_lib.check_turn_in(e.trade, {item1 = 47100, item2 = 61025}))`
    - event_trade NPC say: I see you have found a way to bring order and balance back to the world. You should have also learned of the need for such evils in the world. There cannot be good without evil just as there cannot be truth without deception. I will take the discordant globe now with your fistwraps and make something wonderful for you from them. They will help guide you through the most difficult of times as a reminder of the knowledge you now possess for without the balance between good and evil we are but lost.
