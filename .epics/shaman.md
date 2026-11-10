# Shaman — Epic Quest Walkthrough

Generated directly from quest-graph item rewards. Unresolved dependencies are marked, not inferred.

## Epic 1.0

### "Spear of Fate" (10651)

1. Spawns "Iksar broodling" (npc:72105) via `fearplane/dread#event_death_complete`.
2. Kill "Iksar broodling" (NPC 72105) in `fearplane` and loot "Child's Tear" (1673).
3. citymist/"Lord Rak-Ashiir", hand "Child's Tear" (1673).
    - event_trade NPC emote: looks down at the tear in his hand and says 'A minion of my god came to me one night. I knew it was of Cazic-Thule as I was frozen in terror. My mind screamed for me to flee but my body would not respond. The being took my daughter and vanished to only he knew where. When I regained control of my body and thoughts, I felt nothing but betrayal. I don't care anymore about anything. If you want repentance then slay me, .
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 1673}))`
      - Event guard: `(e.other:GetModCharacterFactionLevel(e.self:GetPrimaryFaction()) >= 1800)`
    - event_trade NPC say: You need to prove your dedication to our cause before I can discuss such matters with you.
      - Event guard: ``
4. Spawns "Lord Rak`Ashiir " (npc:90183) after the hand-in.
5. Kill "Lord Rak`Ashiir " (NPC 90183) in `citymist` and loot "Iksar Scale" (1674).
6. emeraldjungle/"Spirit Sentinel ", hand "Iksar Scale" (1674). Gives "Spear of Fate" (10651).
    - event_trade NPC emote: What is this? The scale of Rak'Ashiir's father? Then Rak has repented his mistake? But why is the mantle still in place? If Rak has repented, then the mantle should have dissolved since he was the one who initiated its construction. But is its initiation the key? How could we have been so blind? Kirn said Rak'Ashiir had the blood of his people on his hands but that is false. Rak merely pointed to a path that would lead them to destruction. It was the people who chose to follow. Now all [is lost].
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 1674}))`

## Epic 1.5

### "Crafted Talisman of Fates" (57400)

1. freeportwest/"Elder Spirit Of Enlightenment", say "Hail".
    - Player: "hail"
      - NPC emote: eyes you with an ageless wisdom.
      - NPC say: Ah, your spirit shines brightly. Should I know you?
      - Condition: `(e.other:Class() == "Shaman")`
      - Condition: `(e.other:HasItem(10651) or e.other:HasItem(36223) or qglobals["shaman_pre"] == "3")`
      - Condition: `(e.message:findi("hail"))`
2. Loot "Amulet of the Spiritist" (57087) from "Netherbian Swarmfiend" (NPC 176111) in `umbral`. Drop cache: 100% chance per kill.
3. Spawns "Spiritseeker Nadox" (npc:227319) via `nadox/player#enter`.
4. Kill "Spiritseeker Nadox" (NPC 227319) in `nadox` and loot "Ring of the Undead Spiritcharmer" (57085).
5. shadeweaver/"Wunshi Kashra", hand "Amulet of the Spiritist" (57087) + "Ring of the Undead Spiritcharmer" (57085).
    - event_trade NPC say: Marvelous! You have come a long way,  . I didn't have many doubts, but to see you return with this very rare and precious item is a joy. Now that we have this, we are yet another step closer to performing the Ruchu. I will keep this and deliver it. Thank you and stay strong, heyokah.
      - Event guard: `(qglobals["shaman_epic"] == "3" and item_lib.check_turn_in(e.trade, {item1 = 57087, item2 = 57085}))`
    - event_trade NPC say: I'll be! You have successfully put an end to that fiend. This amulet will be used by the spirits during Ruchu. Now this amulet which I had used so many times in the past will help the one who wears it during the ritual to bind itself to the consciousness of the spirits so that they can be called. Stay focused shaman.
6. freeportwest/"Elder Spirit Of Enlightenment", say "Business With Wunshi Is Finished". Gives "Gemmed Bangle of Enlightenment" (57088).
    - Player: "business with wunshi is finished"
      - NPC say: Is that so? I am both grateful and anxious. My sight into the spirit world grows darker with each hour. You have done well, but I am ever fearful that we are not moving quickly enough. You must use all of your skills for your next task. Return to Kimm McShannel and when you return to me, tell me that you have created the potion. Show her this bangle.
      - Condition: `(e.other:Class() == "Shaman")`
      - Condition: `(e.message:findi("business with Wunshi is finished") and qglobals["shaman_epic"] == "4")`
      - Linked from "stolen" (explicit prompt).
7. lakerathe/"Kimm Mcshannel", hand "Gemmed Bangle of Enlightenment" (57088).
    - event_trade NPC say: Aye, so ye have returned. We have much to do here, me friend. The first thing we must do is [break down] this bangle into its gems and metal. This here bangle was very carefully made. First, the gems were blessed by the spirits, then the metal itself as it was forged. Aye, we need to carefully separate them. The two gems were blessed by the spirits of Wisdom and Patience, and the metal was strengthened by the Spirit of Might. We will use these to call them back to us.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 57088}))`
    - event_item NPC say: Aye, so ye have returned. We have much to do here, me friend. The first thing we must do is [break down] this bangle into its gems and metal. This here bangle was very carefully made. First, the gems were blessed by the spirits, then the metal itself as it was forged. Aye, we need to carefully separate them. The two gems were blessed by the spirits of Wisdom and Patience, and the metal was strengthened by the Spirit of Might. We will use these to call them back to us.
      - Event guard: `(plugin::check_handin(\%itemcount, 57088 => 1))`
8. lakerathe/"Kimm Mcshannel", say "Break Down". Gives "Heyokah Medicine Bag" (52922).
    - Player: "break down"
      - NPC say: As most things, the process is not a simple one and we'll need some ingredients for a special potion. You must retrieve four items, which should not prove difficult for a shaman of your stature. They are very specific and I can tell you more about the [skin], the [powder], the [tooth], and the [goo]. When you have all of these things, use my medicine bag to create this potion and return it to me.
      - Condition: `(e.message:findi("break down") and qglobals["shaman_epic"] == "5")`
9. Loot "Revenant Tooth" (57500) from "a sun revenant" (NPC 171002) in `thegrey`. Drop cache: 16.7105% chance per kill.
10. Loot "Perfect Marked Ukun Skin" (57701) from "Fang" (NPC 302063) in `draniksscar`. Drop cache: 100% chance per kill.
11. Loot "Corrosive Goo" (57100) from "a pulsating bile" (NPC 105113) in `charasis`. Drop cache: 47.0748% chance per kill.
12. Loot "Corruption Powder" (57520) from "Elite Corrupted Knight" (NPC 200014) in `codecay`. Drop cache: 79.8369% chance per kill.
13. Combine in "Heyokah Medicine Bag" (52922): "Revenant Tooth" (57500), "Perfect Marked Ukun Skin" (57701), "Corrosive Goo" (57100), "Corruption Powder" (57520). Produces "Shaman's Precious Diffusing Agent" (57560). Requires Alchemy.
14. lakerathe/"Kimm Mcshannel", hand "Shaman's Precious Diffusing Agent" (57560). Gives "Runed Purse of the McShannels" (57614).
    - event_trade NPC emote: nods at you and reaches into her pocket and takes out the gemmed bangle and puts it on the ground. She takes the vial and slowly lets a few drops fall on the platinum. It seems to coil and bend and pulls itself into a small globe and the gems lazily fall onto the ground.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 57560}))`
    - event_trade NPC say: Perfect! Now, you must return the gems and platinum to the Spirit of Enlightenment. I've put it in a purse to keep them safe. You truly are beginning to surpass all of our expectations, .
    - event_item NPC emote: nods at you and reaches into her pocket and takes out the gemmed bangle and puts it on the ground. She takes the vial and slowly lets a few drops fall on the platinum. It seems to coil and bend and pulls itself into a small globe and the gems lazily fall onto the ground.
      - Event guard: `(plugin::check_handin(\%itemcount, 57560 => 1))`
    - event_item NPC say: Perfect! Now, you must return the gems and platinum to the Spirit of Enlightenment. I've put it in a purse to keep them safe. You truly are beginning to surpass all of our expectations, $name.
15. freeportwest/"Elder Spirit Of Enlightenment", hand "Runed Purse of the McShannels" (57614).
    - event_trade NPC say: I will have to pass these along as soon as my messenger gets here. I'm sure you understand that as each spirit loses strength, each of our abilities to keep a form in this tangible world becomes very difficult. We must find a way to sustain a physical presence here or the Ruchu will be in jeopardy. We will ask you to [take part] in the ceremony where our strength may fail us.
      - Event guard: `(qglobals["shaman_epic"] == "5" and item_lib.check_turn_in(e.trade, {item1 = 57614}))`
16. freeportwest/"Elder Spirit Of Enlightenment", say "Acknowledge". Gives "Crafted Talisman of Fates" (57400).
    - Player: "acknowledge"
      - NPC say: We, the spirits, have chosen to grant you a gift for all that you've done for us and what you still have left to do. It is just a sampling of the power you may obtain one day as you move forward as one of the heyokah. Guard it and use it well. Should you choose to continue your journey, tell me that you are [prepared to carry on] and save the spirits.
      - NPC message: You have gained 5 ability points!
      - Condition: `(e.other:Class() == "Shaman")`
      - Condition: `(e.message:findi("acknowledge") and qglobals["shaman_epic"] == "6")`
      - Linked from "take part" (explicit prompt).

## Epic 2.0

### "Blessed Spiritstaff of the Heyokah" (57405)

1. freeportwest/"Elder Spirit Of Enlightenment", say "Hail".
    - Player: "hail"
      - NPC emote: eyes you with an ageless wisdom.
      - NPC say: Ah, your spirit shines brightly. Should I know you?
      - Condition: `(e.other:Class() == "Shaman")`
      - Condition: `(e.other:HasItem(10651) or e.other:HasItem(36223) or qglobals["shaman_pre"] == "3")`
      - Condition: `(e.message:findi("hail"))`
2. Loot "Amulet of the Spiritist" (57087) from "Netherbian Swarmfiend" (NPC 176111) in `umbral`. Drop cache: 100% chance per kill.
3. Spawns "Spiritseeker Nadox" (npc:227319) via `nadox/player#enter`.
4. Kill "Spiritseeker Nadox" (NPC 227319) in `nadox` and loot "Ring of the Undead Spiritcharmer" (57085).
5. shadeweaver/"Wunshi Kashra", hand "Amulet of the Spiritist" (57087) + "Ring of the Undead Spiritcharmer" (57085).
    - event_trade NPC say: Marvelous! You have come a long way,  . I didn't have many doubts, but to see you return with this very rare and precious item is a joy. Now that we have this, we are yet another step closer to performing the Ruchu. I will keep this and deliver it. Thank you and stay strong, heyokah.
      - Event guard: `(qglobals["shaman_epic"] == "3" and item_lib.check_turn_in(e.trade, {item1 = 57087, item2 = 57085}))`
    - event_trade NPC say: I'll be! You have successfully put an end to that fiend. This amulet will be used by the spirits during Ruchu. Now this amulet which I had used so many times in the past will help the one who wears it during the ritual to bind itself to the consciousness of the spirits so that they can be called. Stay focused shaman.
6. freeportwest/"Elder Spirit Of Enlightenment", say "Business With Wunshi Is Finished". Gives "Gemmed Bangle of Enlightenment" (57088).
    - Player: "business with wunshi is finished"
      - NPC say: Is that so? I am both grateful and anxious. My sight into the spirit world grows darker with each hour. You have done well, but I am ever fearful that we are not moving quickly enough. You must use all of your skills for your next task. Return to Kimm McShannel and when you return to me, tell me that you have created the potion. Show her this bangle.
      - Condition: `(e.other:Class() == "Shaman")`
      - Condition: `(e.message:findi("business with Wunshi is finished") and qglobals["shaman_epic"] == "4")`
      - Linked from "stolen" (explicit prompt).
7. lakerathe/"Kimm Mcshannel", hand "Gemmed Bangle of Enlightenment" (57088).
    - event_trade NPC say: Aye, so ye have returned. We have much to do here, me friend. The first thing we must do is [break down] this bangle into its gems and metal. This here bangle was very carefully made. First, the gems were blessed by the spirits, then the metal itself as it was forged. Aye, we need to carefully separate them. The two gems were blessed by the spirits of Wisdom and Patience, and the metal was strengthened by the Spirit of Might. We will use these to call them back to us.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 57088}))`
    - event_item NPC say: Aye, so ye have returned. We have much to do here, me friend. The first thing we must do is [break down] this bangle into its gems and metal. This here bangle was very carefully made. First, the gems were blessed by the spirits, then the metal itself as it was forged. Aye, we need to carefully separate them. The two gems were blessed by the spirits of Wisdom and Patience, and the metal was strengthened by the Spirit of Might. We will use these to call them back to us.
      - Event guard: `(plugin::check_handin(\%itemcount, 57088 => 1))`
8. lakerathe/"Kimm Mcshannel", say "Break Down". Gives "Heyokah Medicine Bag" (52922).
    - Player: "break down"
      - NPC say: As most things, the process is not a simple one and we'll need some ingredients for a special potion. You must retrieve four items, which should not prove difficult for a shaman of your stature. They are very specific and I can tell you more about the [skin], the [powder], the [tooth], and the [goo]. When you have all of these things, use my medicine bag to create this potion and return it to me.
      - Condition: `(e.message:findi("break down") and qglobals["shaman_epic"] == "5")`
9. Loot "Revenant Tooth" (57500) from "a sun revenant" (NPC 171002) in `thegrey`. Drop cache: 16.7105% chance per kill.
10. Loot "Perfect Marked Ukun Skin" (57701) from "Fang" (NPC 302063) in `draniksscar`. Drop cache: 100% chance per kill.
11. Loot "Corrosive Goo" (57100) from "a pulsating bile" (NPC 105113) in `charasis`. Drop cache: 47.0748% chance per kill.
12. Loot "Corruption Powder" (57520) from "Elite Corrupted Knight" (NPC 200014) in `codecay`. Drop cache: 79.8369% chance per kill.
13. Combine in "Heyokah Medicine Bag" (52922): "Revenant Tooth" (57500), "Perfect Marked Ukun Skin" (57701), "Corrosive Goo" (57100), "Corruption Powder" (57520). Produces "Shaman's Precious Diffusing Agent" (57560). Requires Alchemy.
14. lakerathe/"Kimm Mcshannel", hand "Shaman's Precious Diffusing Agent" (57560). Gives "Runed Purse of the McShannels" (57614).
    - event_trade NPC emote: nods at you and reaches into her pocket and takes out the gemmed bangle and puts it on the ground. She takes the vial and slowly lets a few drops fall on the platinum. It seems to coil and bend and pulls itself into a small globe and the gems lazily fall onto the ground.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 57560}))`
    - event_trade NPC say: Perfect! Now, you must return the gems and platinum to the Spirit of Enlightenment. I've put it in a purse to keep them safe. You truly are beginning to surpass all of our expectations, .
    - event_item NPC emote: nods at you and reaches into her pocket and takes out the gemmed bangle and puts it on the ground. She takes the vial and slowly lets a few drops fall on the platinum. It seems to coil and bend and pulls itself into a small globe and the gems lazily fall onto the ground.
      - Event guard: `(plugin::check_handin(\%itemcount, 57560 => 1))`
    - event_item NPC say: Perfect! Now, you must return the gems and platinum to the Spirit of Enlightenment. I've put it in a purse to keep them safe. You truly are beginning to surpass all of our expectations, $name.
15. freeportwest/"Elder Spirit Of Enlightenment", hand "Runed Purse of the McShannels" (57614).
    - event_trade NPC say: I will have to pass these along as soon as my messenger gets here. I'm sure you understand that as each spirit loses strength, each of our abilities to keep a form in this tangible world becomes very difficult. We must find a way to sustain a physical presence here or the Ruchu will be in jeopardy. We will ask you to [take part] in the ceremony where our strength may fail us.
      - Event guard: `(qglobals["shaman_epic"] == "5" and item_lib.check_turn_in(e.trade, {item1 = 57614}))`
16. freeportwest/"Elder Spirit Of Enlightenment", say "Acknowledge". Gives "Crafted Talisman of Fates" (57400).
    - Player: "acknowledge"
      - NPC say: We, the spirits, have chosen to grant you a gift for all that you've done for us and what you still have left to do. It is just a sampling of the power you may obtain one day as you move forward as one of the heyokah. Guard it and use it well. Should you choose to continue your journey, tell me that you are [prepared to carry on] and save the spirits.
      - NPC message: You have gained 5 ability points!
      - Condition: `(e.other:Class() == "Shaman")`
      - Condition: `(e.message:findi("acknowledge") and qglobals["shaman_epic"] == "6")`
      - Linked from "take part" (explicit prompt).
17. freeportwest/"Elder Spirit Of Enlightenment", hand "Crafted Talisman of Fates" (57400). Gives "Blessed Spiritstaff of the Heyokah" (57405).
    - event_trade NPC say: You have heard the stories of the blessings bestowed on some of Norrath's most faithful to the ways of the heyokah. To reward you for all that you've done, the spirits have chosen to bless this talisman and offer it to you as our thanks, for without you, all shaman would have suffered without our presence in this realm. Walk proud, heyokah, and never forget what you are.' All around you, you feel the strength of the spirit world begin to strengthen as the spirit leaves to tend to his wounded companions.
      - Event guard: `(qglobals["shaman_epic"] == "14" and item_lib.check_turn_in(e.trade, {item1 = 57400}))`
    - event_trade NPC message: You have gained 10 ability points!
