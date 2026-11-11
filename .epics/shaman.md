# Shaman — Epic Quest Walkthrough

Generated directly from quest-graph item rewards. Unresolved dependencies are marked, not inferred.

## Epic 1.0

### "Spear of Fate" (10651)

<a id="epic-item-10651"></a>

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

<a id="epic-item-57400"></a>

**Earlier reward routes required by this graph path:** ["Spear of Fate" (10651)](#epic-item-10651).
Revisit those instructions if another copy of a consumed item is needed.

1. freeportwest/"Elder Spirit Of Enlightenment", say "Hail".
    - Player: "hail"
      - NPC emote: eyes you with an ageless wisdom.
      - NPC say: Ah, your spirit shines brightly. Should I know you?
      - Condition: `(e.other:Class() == "Shaman")`
      - Condition: `(e.other:HasItem(10651) or e.other:HasItem(36223) or qglobals["shaman_pre"] == "3")`
      - Condition: `(e.message:findi("hail"))`
2. freeportwest/"Elder Spirit Of Enlightenment", say "Shaman". Sets `shaman_epic` to `1`.
    - Player: "shaman"
      - NPC say: Ah, yes. You are not only a shaman, but one who has passed the tests of the heyokah. There are many problems that face us now and I grow weaker by the day. If you feel you are ready to bear a great burden and help all of those like us, including the immortals that charge our essence and consciousness, say [it is so].
      - Condition: `(e.other:Class() == "Shaman")`
      - Condition: `(e.other:HasItem(10651) or e.other:HasItem(36223) or qglobals["shaman_pre"] == "3")`
      - Condition: `(e.message:findi("shaman"))`
      - Linked from "wasichu" (explicit prompt).
      - Linked from "great heyokah" (explicit prompt).
      - Linked from "wise" (explicit prompt).
      - Linked from "trials of justice" (explicit prompt).
      - Linked from "troubled" (explicit prompt).
      - Linked from "meaningful way" (explicit prompt).
      - Linked from "take part" (explicit prompt).
3. shadeweaver/"Wunshi Kashra", say "Hand:Platinum:1000". Gives "Thatched Medicine Bag" (57704).
4. Loot "Bleak Fungus" (57620) from "Shuddering Fungus" (NPC 157118) in `fungusgrove`. Drop cache: 71.4286% chance per kill.
5. Spawns "Ancient Megalodon" (npc:51160) via `lakerathe/#kimm mcshannel#up to it`.
6. Kill "Ancient Megalodon" (NPC 51160) in `lakerathe` and loot "Lustrous Seaweed" (52926).
7. lakerathe/, hand "Lustrous Seaweed" (52926). Gives "Twine-Wrapped Lustrous Seaweed" (57600).
8. Combine in "Thatched Medicine Bag" (57704): "Bleak Fungus" (57620), "Twine-Wrapped Lustrous Seaweed" (57600). Produces "Shadowed Pulp" (57550). Requires Alchemy.
9. Collect ground spawn "Twinkling Shrub" (57080) in `twilight`.
10. twilight/"Tikl Huk", hand "Twinkling Shrub" (57080). Gives "Tied Twinkling Shrubs" (52920).
    - event_item NPC say: Me proud! Now you must protect dat for da spirit. It need it badly. You be careful. Dere might be some baddies out dere dat may want to take dat from you. Spirit said dere are evils working against us. I hab tied da shrub for you so dat it don't get ruined.
      - Event guard: `(plugin::check_handin(\%itemcount, 57080 =>3 ))`
11. Spawns "Gnashing Killer Shark" (npc:117091) via `cobaltscar/yoppa greenthumb#elder spirit sent me`.
12. Kill "Gnashing Killer Shark" (NPC 117091) in `cobaltscar` and loot "Brittle Burned Bark" (57086).
13. Combine in "Thatched Medicine Bag" (57704): "Tied Twinkling Shrubs" (52920), "Brittle Burned Bark" (57086). Produces "Brittle Twigs" (57369). Requires Alchemy.
14. warrens/"Wilslik Gissu", hand "Shadowed Pulp" (57550) + "Brittle Twigs" (57369). Gives "Distilled Potion of Endurance" (52921).
    - event_trade NPC say: Take these and return to the spirit!
      - Event guard: `(qglobals["shaman_epic"] == "1" and item_lib.check_turn_in(e.trade, {item1 = 57550, item2 = 57369}))`
15. freeportwest/"Elder Spirit Of Enlightenment", hand "Distilled Potion of Endurance" (52921).
    - event_trade NPC emote: drinks the potion hastily and shudders. Its essence grows brighter and it's dull eyes begin to sparkle with renewed strength.
      - Event guard: `(qglobals["shaman_epic"] == "1" and item_lib.check_turn_in(e.trade, {item1 = 52921}))`
    - event_trade NPC say: You have bought me time -- time to explain how you may aid us all. The darkness of Discord seeps ever deeper into Norrath and the spirit world. Some of the most revered and oldest spirits known have turned to grim pursuits, becoming the [wasichu] -- those creatures you may remember from you time conversing with another great spirit.
16. freeportwest/"Elder Spirit Of Enlightenment", say "Rare Gift". Gives "Potion of Sustenance" (57081).
    - Player: "rare gift"
      - NPC say: The Spirit of Wisdom itself blessed a talisman and gave it to Juktopp, telling him of our offer. Needless to say, he was overwhelmed and overjoyed. To this day, he remains light as air and just as free in a planar realm of great beauty. You must find him and retrieve the talisman. Give him this potion which will sustain him while we prepare for Ruchu. There is [still more] you must do.
      - Condition: `(e.other:Class() == "Shaman")`
      - Condition: `(e.message:findi("rare gift") and qglobals["shaman_epic"] == "2")`
      - Linked from "watched" (explicit prompt).
17. airplane/"Eternal Spirit", hand "Potion of Sustenance" (57081). Gives "Blessed Talisman of Wisdom" (57083).
    - event_trade NPC emote: beams and looks at you with pride, 'Greetings, . I am both glad to see you and somewhat sad. I know you are here to retrieve my talisman -- which is the reason for my weeping heart. I do understand the importance of taking it for the Ruchu. My heart does warm, though, at the sight of a class in pursuit of great things. I am envious. Here, take the talisman and protect it with your life. I should like to see it again after all has been set right.'
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 57081}))`
18. Loot "Blessed Talisman of Patience" (57084) from "Punisher Veshtaq".
19. freeportwest/"Elder Spirit Of Enlightenment", hand "Blessed Talisman of Wisdom" (57083) + "Blessed Talisman of Patience" (57084).
    - event_trade NPC say: This is a start. There is still much to do. While we have gotten the talismans from our allies, there are those that are not our friends -- the wasichu and worse -- who carry or have [stolen] items we need. They will not part with them willingly. This is where your strength and might will be put to the test . . . and your presence of mind. Are you certain you wish to go on?
      - Event guard: `(qglobals["shaman_epic"] == "2" and item_lib.check_turn_in(e.trade, {item1 = 57083, item2 = 57084}))`
20. Loot "Amulet of the Spiritist" (57087) from "Netherbian Swarmfiend" (NPC 176111) in `umbral`. Drop cache: 100% chance per kill.
21. shadeweaver/"Wunshi Kashra", say "Stolen". Sets `shaman_epic_nadox` to `1`.
    - Player: "stolen"
      - NPC say: The vermin that stole it now abuses it to gain control over spirits it wants to command. It is a peculiar beast that lives way up in the heavens on the moon. It is not often seen, so your timing must be right. Return its amulet to me when you obtain it. We will all be better off without this creature lurking about.
      - Condition: `(e.message:findi("stolen") and qglobals["shaman_epic"] == "3")`
      - Linked from "second beast" (explicit prompt).
22. Spawns "Spiritseeker Nadox" (npc:227319) via `nadox/player#enter`.
23. Kill "Spiritseeker Nadox" (NPC 227319) in `nadox` and loot "Ring of the Undead Spiritcharmer" (57085).
24. shadeweaver/"Wunshi Kashra", hand "Amulet of the Spiritist" (57087) + "Ring of the Undead Spiritcharmer" (57085).
    - event_trade NPC say: Marvelous! You have come a long way,  . I didn't have many doubts, but to see you return with this very rare and precious item is a joy. Now that we have this, we are yet another step closer to performing the Ruchu. I will keep this and deliver it. Thank you and stay strong, heyokah.
      - Event guard: `(qglobals["shaman_epic"] == "3" and item_lib.check_turn_in(e.trade, {item1 = 57087, item2 = 57085}))`
    - event_trade NPC say: I'll be! You have successfully put an end to that fiend. This amulet will be used by the spirits during Ruchu. Now this amulet which I had used so many times in the past will help the one who wears it during the ritual to bind itself to the consciousness of the spirits so that they can be called. Stay focused shaman.
25. freeportwest/"Elder Spirit Of Enlightenment", say "Business With Wunshi Is Finished". Gives "Gemmed Bangle of Enlightenment" (57088).
    - Player: "business with wunshi is finished"
      - NPC say: Is that so? I am both grateful and anxious. My sight into the spirit world grows darker with each hour. You have done well, but I am ever fearful that we are not moving quickly enough. You must use all of your skills for your next task. Return to Kimm McShannel and when you return to me, tell me that you have created the potion. Show her this bangle.
      - Condition: `(e.other:Class() == "Shaman")`
      - Condition: `(e.message:findi("business with Wunshi is finished") and qglobals["shaman_epic"] == "4")`
      - Linked from "stolen" (explicit prompt).
26. lakerathe/, hand "Gemmed Bangle of Enlightenment" (57088).
27. lakerathe/, say "Kimm Mcshannel". Gives "Heyokah Medicine Bag" (52922).
28. Loot "Revenant Tooth" (57500) from "a sun revenant" (NPC 171002) in `thegrey`. Drop cache: 16.7105% chance per kill.
29. Loot "Perfect Marked Ukun Skin" (57701) from "Fang" (NPC 302063) in `draniksscar`. Drop cache: 100% chance per kill.
30. Loot "Corrosive Goo" (57100) from "a pulsating bile" (NPC 105113) in `charasis`. Drop cache: 47.0748% chance per kill.
31. Loot "Corruption Powder" (57520) from "Elite Corrupted Knight" (NPC 200014) in `codecay`. Drop cache: 79.8369% chance per kill.
32. Combine in "Heyokah Medicine Bag" (52922): "Revenant Tooth" (57500), "Perfect Marked Ukun Skin" (57701), "Corrosive Goo" (57100), "Corruption Powder" (57520). Produces "Shaman's Precious Diffusing Agent" (57560). Requires Alchemy.
33. lakerathe/, hand "Shaman's Precious Diffusing Agent" (57560). Gives "Runed Purse of the McShannels" (57614).
34. freeportwest/"Elder Spirit Of Enlightenment", hand "Runed Purse of the McShannels" (57614).
    - event_trade NPC say: I will have to pass these along as soon as my messenger gets here. I'm sure you understand that as each spirit loses strength, each of our abilities to keep a form in this tangible world becomes very difficult. We must find a way to sustain a physical presence here or the Ruchu will be in jeopardy. We will ask you to [take part] in the ceremony where our strength may fail us.
      - Event guard: `(qglobals["shaman_epic"] == "5" and item_lib.check_turn_in(e.trade, {item1 = 57614}))`
35. freeportwest/"Elder Spirit Of Enlightenment", say "Acknowledge". Gives "Crafted Talisman of Fates" (57400).
    - Player: "acknowledge"
      - NPC say: We, the spirits, have chosen to grant you a gift for all that you've done for us and what you still have left to do. It is just a sampling of the power you may obtain one day as you move forward as one of the heyokah. Guard it and use it well. Should you choose to continue your journey, tell me that you are [prepared to carry on] and save the spirits.
      - NPC message: You have gained 5 ability points!
      - Condition: `(e.other:Class() == "Shaman")`
      - Condition: `(e.message:findi("acknowledge") and qglobals["shaman_epic"] == "6")`
      - Linked from "take part" (explicit prompt).

## Epic 2.0

### "Blessed Spiritstaff of the Heyokah" (57405)

<a id="epic-item-57405"></a>

**Earlier reward routes required by this graph path:** ["Crafted Talisman of Fates" (57400)](#epic-item-57400).
Revisit those instructions if another copy of a consumed item is needed.

1. freeportwest/"Elder Spirit Of Enlightenment", say "Prepared To Carry On". Sets `shaman_epic` to `8`.
    - Player: "prepared to carry on"
      - NPC say: I knew we could count on you, .  The time for Ruchu is drawing ever nearer, but we still must gather some essential elements. Soon, you will have to cross the barrier into that realm of Discord. Lupot Nukla can help you.
      - Condition: `(e.other:Class() == "Shaman")`
      - Condition: `(e.message:findi("prepared to carry on") and e.other:HasItem(57400))`
      - Linked from "hail" (explicit prompt).
      - Linked from "acknowledge" (explicit prompt).
2. fungusgrove/"Lupot Nukla", say "Taken By Force". Sets `shaman_epic` to `9`.
    - Player: "taken by force"
      - NPC say: Over in Taelosia, the peaceful folk there found themselves overcome by the Muramites. They had stolen much of what had meaning to them. If you can track down Undari Perunea she can tell you how to find a sacred necklace of perseverance that was created by her own people, though Norrath's spirits did charm it. You will find Undari near the temples, hiding, and waiting for you. Return the talisman to me.
      - Condition: `(e.message:findi("taken by force") and qglobals["shaman_epic"] == "8")`
      - Linked from "hail" (explicit prompt).
3. kodtaz/"Undari Perunea", say "Hail".
    - Player: "hail"
      - NPC say: Are you here to help me? Yes, I feel the intent of your spirit. You must be careful, the evil beast that stole my necklace is ever near.
      - Condition: `(e.message:findi("hail") and qglobals["shaman_epic"] == "9")`
4. Spawns "Ikaav Spiritstealer" (npc:293233) via `kodtaz/undari perunea#hail`.
5. Kill "Ikaav Spiritstealer" (NPC 293233) in `kodtaz` and loot "Necklace of Perseverance" (57401).
6. fungusgrove/"Lupot Nukla", hand "Necklace of Perseverance" (57401).
    - event_trade NPC say: You have traveled far, my friend. This necklace is more powerful than those foolish Muramites knew. Undari has been holding a key to the spirit world around her neck for many years. How do you think she remained [protected] near those temples and beasts?
      - Event guard: `(qglobals["shaman_epic"] == "9" and item_lib.check_turn_in(e.trade, {item1 = 57401}))`
7. Spawns "Darkened Chanting Woodspirit" (npc:210250) via `postorms/210252#enter`.
8. Kill "Darkened Chanting Woodspirit" (NPC 210250) in `postorms` and loot "Piece of Moaning Timber" (57403).
9. fungusgrove/"Lupot Nukla", hand "Piece of Moaning Timber" (57403). Gives "Impervious Medicine Bag" (57551).
    - event_trade NPC say: You have done well,. We are drawing nearer to being fully prepared for the Ruchu. I've put the bark and the necklace into this satchel that is protected by a spell. The only one who may open it is the Spirit of Enlightenment. Go and give that to it.
      - Event guard: `(qglobals["shaman_epic"] == "10" and item_lib.check_turn_in(e.trade, {item1 = 57403}))`
10. freeportwest/"Elder Spirit Of Enlightenment", hand "Impervious Medicine Bag" (57551).
    - event_trade NPC say: You never cease to surprise me. I felt in my heart that you would get this far, but I did not expect you to be so bold and steady with your advance. Can you feel the spirits smiling on you?' The spirit lifts its weary head and closes its eyes . . . Yes, yes, they are pleased, but they are weak just as I am. And now the path grows dark and dreary. We must ask you to once again to risk your life, but not in this world, but the world of [Discord].
      - Event guard: `(qglobals["shaman_epic"] == "10" and item_lib.check_turn_in(e.trade, {item1 = 57551}))`
11. freeportwest/"Elder Spirit Of Enlightenment", say "Seek". Gives "Pouch of Spirit Dust" (57710).
    - Player: "seek"
      - NPC say: The other creature you must find is a soldier of evil. Another is an scurrying creature that is not bound to our realm. You have much ahead of you. Take this pouch and carefully piece together everything you find and return it to me. You will know how to do it. The spirits will guide you.
      - Condition: `(e.other:Class() == "Shaman")`
      - Condition: `(e.message:findi("seek") and qglobals["shaman_epic"] == "11")`
      - Linked from "hail" (explicit prompt).
      - Linked from "discord" (explicit prompt).
12. Spawns "a phase spider" (npc:123190) via `necropolis/an out of phase spider#event_combat`.
13. Kill "a phase spider" (NPC 123190) in `necropolis` and loot "Spirit-Touched Phased Spider Thorax" (57562).
14. Spawns "Lightning Warrior Spiritseeker" (npc:316073) via `provinggrounds/stilled lightning warrior#enter`.
15. Kill "Lightning Warrior Spiritseeker" (NPC 316073) in `provinggrounds` and loot "Glowing Trace of Might" (57250).
16. Spawns "epic version of Murkglider School Leader" (npc:303116) via `causeway/kupiop iku#ready`.
17. Kill "epic version of Murkglider School Leader" (NPC 303116) in `causeway` and loot "Slight Trace of a Spirit" (57800).
18. Loot "Reviving Potion of Might" (57315) from "Bloated Girplan" (NPC 336143) in `dranik`. Drop cache: 100% chance per kill.
19. Combine in "Pouch of Spirit Dust" (57710): "Spirit-Touched Phased Spider Thorax" (57562), "Glowing Trace of Might" (57250), "Slight Trace of a Spirit" (57800), "Reviving Potion of Might" (57315). Produces "Glowing Spirit Charm of Might" (57987). Requires Remove Traps.
20. freeportwest/"Elder Spirit Of Enlightenment", hand "Glowing Spirit Charm of Might" (57987).
    - event_trade NPC say: The time is nearly here! We have only a few remaining pieces that we must collect in order to restore our spirits. We did miss something, however, and it must be stopped. You must gather your allies and return to Discord. A wasichu has learned to summon the fiercest beasts and has grown out of control. It is now a [spiritcaller] who is drawing the strength of our most precious elders to do it.
      - Event guard: `(qglobals["shaman_epic"] == "11" and item_lib.check_turn_in(e.trade, {item1 = 57987}))`
21. Spawns "Discordling Spiritcaller" (npc:300091) via `wallofslaughter/hudar trittan#fooled`.
22. Kill "Discordling Spiritcaller" (NPC 300091) in `wallofslaughter` and loot "Spiritcaller Beads" (57404).
23. freeportwest/"Elder Spirit Of Enlightenment", hand "Spiritcaller Beads" (57404).
    - event_trade NPC say: There is one last thing you must do. Your defeat of the spiritcaller has proven your strength and I believe you are ready. Do not fail us now. You must go into the lair of Mata Muram himself. There is a strange orb that only exists there. We believe some of our spirits, beyond those we shall restore with Ruchu, are becoming absorbed or attracted to these orbs. You must find one and bring it to me and then we shall have all we need.
      - Event guard: `(qglobals["shaman_epic"] == "12" and item_lib.check_turn_in(e.trade, {item1 = 57404}))`
24. global/"Global Player", say "Recipe:19908". Gives "Globe of Discordant Energy" (47100).
25. freeportwest/"Elder Spirit Of Enlightenment", hand "Globe of Discordant Energy" (47100).
    - event_trade NPC emote: lowers its head and you believe you see a shade of a tear drop from its eyes and disappear into nothingness. 'You have done it. You cannot imagine our gratitude. The time for Ruchu is at hand and we offer you the privilege of taking part. If you are able to do the ceremony now, tell me you are [prepared for the ceremony].'
      - Event guard: `(qglobals["shaman_epic"] == "13" and item_lib.check_turn_in(e.trade, {item1 = 47100}))`
26. freeportwest/"Elder Spirit Of Enlightenment", hand "Crafted Talisman of Fates" (57400). Gives "Blessed Spiritstaff of the Heyokah" (57405).
    - event_trade NPC say: You have heard the stories of the blessings bestowed on some of Norrath's most faithful to the ways of the heyokah. To reward you for all that you've done, the spirits have chosen to bless this talisman and offer it to you as our thanks, for without you, all shaman would have suffered without our presence in this realm. Walk proud, heyokah, and never forget what you are.' All around you, you feel the strength of the spirit world begin to strengthen as the spirit leaves to tend to his wounded companions.
      - Event guard: `(qglobals["shaman_epic"] == "14" and item_lib.check_turn_in(e.trade, {item1 = 57400}))`
    - event_trade NPC message: You have gained 10 ability points!
