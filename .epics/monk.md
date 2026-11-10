# Monk — Epic Quest Walkthrough

Generated directly from quest-graph item rewards. Unresolved dependencies are marked, not inferred.

## Epic 1.0

### "Celestial Fists" (10652)

1. bazaar/"Caerlyna", say "Hail".
    - Player: "hail"
      - NPC say: Greetings $name! Nice to meet you. I've started up a complimentary bag check service. Feel free to give me your weight reducing bag, and I'll give you a token in return. When you would like to get your bag back, simply return to me with your token.
      - Condition: `($text=~/hail/i)`
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
16. bazaar/"Caerlyna", hand "Deluxe Sewing Kit" (17966). Gives "Deluxe Sewing Kit Token" (51537).
    - event_item NPC say: Here you go. Bring this token back to me when you would like your bag back.
      - Event guard: `(plugin::check_handin(\%itemcount, 17966 => 1))`
17. bazaar/"Caerlyna", hand "Deluxe Sewing Kit Token" (51537). Gives "Deluxe Sewing Kit" (17966).
    - event_item NPC say: Here you go. Here is your bag back.
      - Event guard: `(plugin::check_handin(\%itemcount, 51537 => 1))`
18. Loot "Code of Zan Fi" (12316) from "Targin the Rock" (NPC 32067) in `soldungb`. Drop cache: 100% chance per kill.
19. southkarana/"Brother Qwinn", hand "Needle of the Void" (12314). Gives "Purple Headband" (10114).
20. southkarana/"Brother Qwinn", hand "Code of Zan Fi" (12316) + "Purple Headband" (10114). Gives "Needle of the Void" (12314).
    - event_trade NPC say: We had an agreement. The proof of a skilled monk, the purple headband, and the Code of the Whistling Fist.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 12316,item2 = 10114}))`
    - event_trade NPC say: We thank you for the return of the Code of the Whistling Fist. Take this sewing needle. You shall find it useful should you aid [Brother Zephyl] in his quest. His item, the needle, a swatch of shadow silk and a scroll containing Jonathan's Whistling Warsong. Into a sewing kit they will be going. And into the brotherhood will you. I hope you do not wish me to [return the headband]..
21. Loot "The Idol" (12317) from "Raster of Guk" (NPC 66172) in `gukbottom`. Drop cache: 100% chance per kill.
22. rathemtn/"Brother Zephyl", hand "Rare Robe Pattern" (12315). Gives "Red Sash of Order" (10133).
23. rathemtn/"Brother Zephyl", hand "The Idol" (12317) + "Red Sash of Order" (10133). Gives "Rare Robe Pattern" (12315).
    - event_item NPC say: We had an agreement. The proof of a skilled monk, the red sash, and the idol of Zan Fi.
      - Event guard: `(plugin::check_handin(\%itemcount, 12317 => 1, 10133 => 1))`
    - event_item NPC say: We thank you for the return of the idol of Zan Fi. Take this rare robe pattern. You shall find it useful should you aid [Brother Qwinn] in his quest. His item, the rare robe pattern, a swatch of shadow silk and a scroll containing Jonathan's Whistling Warsong. Into a sewing kit they will be going. And into the brotherhood will you. I hope you do not wish me to [return the sash].
24. Buy "Song: Jonthan's Whistling Warsong" (15734) from "Lysric Loresinger" (NPC 1035) in `qeynos`. Base price: 43 copper.
25. bazaar/"Caerlyna", hand "Vale Sewing Kit" (92882). Gives "Vale Sewing Kit Token" (56884).
    - event_item NPC say: Here you go. Bring this token back to me when you would like your bag back.
      - Event guard: `(plugin::check_handin(\%itemcount, 92882 => 1))`
26. bazaar/"Caerlyna", hand "Vale Sewing Kit Token" (56884). Gives "Vale Sewing Kit" (92882).
    - event_item NPC say: Here you go. Here is your bag back.
      - Event guard: `(plugin::check_handin(\%itemcount, 56884 => 1))`
27. Loot "Shadow Wolf Pelt" (13779) from "a shadow wolf" (NPC 408093) in `commonlands`. Drop cache: 7.6384% chance per kill.
28. Buy "Spell: Gather Shadows" (15522) from "Tagus Wunne" (NPC 10030) in `freporte`. Base price: 43 copper.
29. Loot "Spider Silk" (13041) from "a large widow" (NPC 481029) in `fungalforest`. Drop cache: 99.167% chance per kill.
30. Combine in "Vale Sewing Kit" (92882): "Spider Silk" (13041). Produces "Silk Swatch" (16482). Requires Tailoring.
31. Combine in "Vale Sewing Kit" (92882): "Shadow Wolf Pelt" (13779), "Spell: Gather Shadows" (15522), "Silk Swatch" (16482). Produces "Shadow Silk" (16483). Requires Tailoring.
32. Combine in "Deluxe Sewing Kit" (17966): "Needle of the Void" (12314), "Rare Robe Pattern" (12315), "Song: Jonthan's Whistling Warsong" (15734), "Shadow Silk" (16483). Produces "Robe of the Lost Circle" (12256). Requires Tailoring.
33. dreadlands/"Brother Balatin", hand "Metal Pipe" (12979) + "Metal Pipe" (12980) + "Robe of the Lost Circle" (12256). Gives "Robe of the Whistling Fists" (12970).
    - event_item NPC emote: holds his arms out and a fine robe materializes before your eyes. You grab it just in time to see the skeleton fade from existence.
      - Event guard: `(plugin::check_handin(\%itemcount, 12979 => 1, 12980 => 1, 12256 => 1))`
34. Loot "Immortals" (18195) from "Faerie of Dismay" (NPC 91012) in `skyfire`. Drop cache: 35% chance per kill.
35. erudnext/"Tomekeeper Danl", hand "Immortals" (18195). Gives "Danl's Reference" (1682).
    - event_trade NPC emote: gasps at the sight of the rare book. 'This is a great find indeed! I can only imagine who you had to.. persuade to give you the book. Our library would be very interested in acquiring this and I am prepared to give you this referral that marks you as a friend of the library. If only [Lheao] could see this.'
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 18195}) and e.other:GetLevel() >= 46 and e.other:Class() == "Monk")`
36. timorous/"Lheao", hand "Robe of the Whistling Fists" (12970) + "Danl's Reference" (1682). Gives "Celestial Fists" (1683).
    - event_item NPC say: Astonishing! To think that you are a master of an order thought to be lost in our world. Forgive my earlier doubts. I believe you are indeed worthy to be given the responsibility of watching over this book. Take great care that it does not fall into the wrong hands as it would be truly disastrous.
      - Event guard: `(plugin::check_handin(\%itemcount, 12970 => 1, 1682 => 1))`
37. trakanon/"Kaiaren", hand "Celestial Fists" (1683). Gives "Book of Celestial Fists" (1689).
    - event_item NPC say: Now, then. Where did you find this, monk? This is not just some light reading to be borrowed from the town library. Who gave this to you?
      - Event guard: `((plugin::check_handin(\%itemcount, 1683 => 1)) && ($ulevel>=46) && ($class=="Monk"))`
    - event_item NPC emote: eyes open wide and he attacks you!
38. trakanon/"Kaiaren", hand "Demon Fangs" (1688) + "Book of Celestial Fists" (1689). Gives "Celestial Fists" (10652).
    - event_item NPC emote: bows his head and breathes a long sigh as if relived of a great weight. He then looks up at you and says, 'I honestly did not believe you could have defeated Vorash. Even though he sought nothing but war and bloodshed, it is a life nonetheless and we must mourn him. I will sew these fangs into magical fist wraps and they shall be yours. Remember Xenevorash. A purpose can be found for every situation and individual. To achieve perfection is to perceive this truth.'
      - Event guard: `((plugin::check_handin(\%itemcount, 1688 => 1, 1689 => 1)) && ($ulevel>=46) && ($class=="Monk"))`

**Unresolved graph dependencies:**
- Cycle while acquiring "Deluxe Sewing Kit" (17966)
- Cycle while acquiring "Needle of the Void" (12314)
- Cycle while acquiring "Rare Robe Pattern" (12315)
- Cycle while acquiring "Vale Sewing Kit" (92882)

## Epic 1.5

### "Fistwraps of Celestial Discipline" (61025)

1. Loot "Scribed Note" (20435) from "The Keeper" (NPC 301030) in `bloodfields`. Drop cache: 100% chance per kill.
2. potranquility/"Vortix", hand "Scribed Note" (20435). Gives "Fistwraps of Celestial Discipline" (61025).
    - event_item NPC say: I can see that you are truly a great member of the Celestial Order now. You have helped the Order when it was needed and have helped me regain the honor which I had lost. The Order has given me the privilege now to bestow upon you the Fistwraps of the Celestial Disciple. May you enjoy your new ranking within the Order. Kaiaren will be pleased to speak to the person responsible for his saving. You may find him wandering the lands with his newfound well-being. I believe the last place he was seen was travelling in the Ocean of Tears. Be safe $name and thank you again.
      - Event guard: `($client->GetGlobal("monk_epic") ==8 && plugin::check_handin(\%itemcount, 20435 => 1))`
    - event_item NPC message: You have gained 5 ability points!

## Epic 2.0

### "Transcended Fistwraps of Immortality" (67742)

1. global/"Global Player", say "Recipe:19908". Gives "Globe of Discordant Energy" (47100).
2. Loot "Scribed Note" (20435) from "The Keeper" (NPC 301030) in `bloodfields`. Drop cache: 100% chance per kill.
3. potranquility/"Vortix", hand "Scribed Note" (20435). Gives "Fistwraps of Celestial Discipline" (61025).
    - event_item NPC say: I can see that you are truly a great member of the Celestial Order now. You have helped the Order when it was needed and have helped me regain the honor which I had lost. The Order has given me the privilege now to bestow upon you the Fistwraps of the Celestial Disciple. May you enjoy your new ranking within the Order. Kaiaren will be pleased to speak to the person responsible for his saving. You may find him wandering the lands with his newfound well-being. I believe the last place he was seen was travelling in the Ocean of Tears. Be safe $name and thank you again.
      - Event guard: `($client->GetGlobal("monk_epic") ==8 && plugin::check_handin(\%itemcount, 20435 => 1))`
    - event_item NPC message: You have gained 5 ability points!
4. poknowledge/"Sebast Muckle", hand "Globe of Discordant Energy" (47100) + "Fistwraps of Celestial Discipline" (61025). Gives "Transcended Fistwraps of Immortality" (67742).
    - event_trade NPC message: You have gained 10 ability point(s)!
      - Event guard: `(qglobals["mnk_epic20"] == "6" and item_lib.check_turn_in(e.trade, {item1 = 47100, item2 = 61025}))`
    - event_trade NPC say: I see you have found a way to bring order and balance back to the world. You should have also learned of the need for such evils in the world. There cannot be good without evil just as there cannot be truth without deception. I will take the discordant globe now with your fistwraps and make something wonderful for you from them. They will help guide you through the most difficult of times as a reminder of the knowledge you now possess for without the balance between good and evil we are but lost.
