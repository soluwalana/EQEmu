# Beastlord — Epic Quest Walkthrough

Generated directly from quest-graph item rewards. Unresolved dependencies are marked, not inferred.

## Epic 1.0

### "Claw of the Savage Spirit" (8495)

<a id="epic-item-8495"></a>

1. feerrott/"Scout Ahlikal", say "Hail".
    - Player: "hail"
      - NPC say: It is a pleasure to meet you, but I do not have time to speak. I am waiting on official word from Shar Vahl. If you have been sent to assist me, please show me the Official Seal of the Khati Sha at this time. If you are not such a person, please carry on with your business and leave me to tend to mine.
      - Condition: `(e.message:findi("hail"))`
2. Spawns "counter spawn" (npc:167663) via `grimling/scout husman#ready to begin`.
3. Spawns "untargetable Ukigit" (npc:167662) via `grimling/scout husman#ready to begin`.
4. Kill grimling/"A Grimling Gruntling".
5. Spawns "Arcanist Ukigit" (npc:167661) via `grimling/grimling counter#signal:1`.
6. Kill "Arcanist Ukigit" (NPC 167661) in `grimling` and loot "Copper Medal of War" (4393).
7. sharvahl/"Elder Animist Dumul", hand "Copper Medal of War" (4393). Gives "Carved Wooden Chest" (17361).
    - event_item NPC say: You have returned at a most opportune time, $name. If this medal is indicative of your abilities in combat, I may be able to find a slight amount of hope soon. We have learned answers for many of the questions that we had prior to your last visit. Please take this seal and this container. Place them somewhere safe, while I gather the information that we've accumulated so far. Let me know when you have the seal packed and are ready to be briefed. Should you ever lose it, just ask for another.
      - Event guard: `(plugin::check_handin(\%itemcount, 4393 =>1 ))`
8. sharvahl/"Elder Animist Dumul", say "Lost The Seal". Gives "Official Seal of the Khati Sha" (9031).
    - Player: "lost the seal"
      - NPC say: Here you go.  Keep this one safe.
      - Condition: `($text=~/lost the seal/i && $bstepic >=1)`
      - Linked from "ready to be briefed" (sequence only; unverified).
9. feerrott/"Scout Ahlikal", hand "Official Seal of the Khati Sha" (9031).
    - event_trade NPC say: Well met, I'm glad that you made it! This jungle is oppressive, with its dank earth and dark canopy. The sooner you dispatch that spirit, the sooner we can both make our way out of this vile place. Move towards the ruins that lie about two hundred feet from here. The spirit will be there. Release it from its current form and return the totem to me. I will wrap it for you, so that you may place it in the container that you should have been given. Take care and be swift!
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 9031}))`
    - event_trade NPC emote: A large yellow spider drifts down from the jungle canopy. Perhaps it senses the proximity of its next meal.
10. Spawns "The Spirit of Decay" (npc:47205) after the hand-in.
11. Kill "The Spirit of Decay" (NPC 47205) in `feerrott` and loot "Totem of the Spider" (9032).
12. feerrott/"Scout Ahlikal", hand "Totem of the Spider" (9032). Gives "Wrapped Spider Totem" (9033).
    - event_trade NPC say: Amazing work, ! We are all in your debt. I have wrapped the totem to prevent its harmful magic from affecting you. Please keep it in the box until you can return it to Elder Dumul. If you have not found the other spirits, please seek them out. If you have filled the container, please seal it and return to Shar Vahl. Here is your seal. May the spirits watch over you.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 9032}))`
13. lfaydark/"Scout Rahjiq", hand "Official Seal of the Khati Sha" (9031).
    - event_item NPC say: Keep your head down, mate! The spirit that you have come for is very close. I have spotted it several times today. It keeps appearing near that odd structure just over the hill. Be careful not to attract the attention of those invisible creatures that roam near the structure. Just release the spirit and return the totem to me. I'll prepare the totem for placement in the container that you were given.
      - Event guard: `(plugin::check_handin(\%itemcount, 9031 =>1 ))`
    - event_item NPC emote: The air before the large monolith grows solid, as misty tendrils wrap together in the shape of a large wolf.
14. Spawns "The Spirit of Malevolence" (npc:57119) after the hand-in.
15. Kill "The Spirit of Malevolence" (NPC 57119) in `lfaydark` and loot "Totem of the Wolf" (9034).
16. lfaydark/"Scout Rahjiq", hand "Totem of the Wolf" (9034). Gives "Wrapped Wolf Totem" (9035).
    - event_item NPC emote: wraps the totem and returns it with the seal you gave him and says
      - Event guard: `(plugin::check_handin(\%itemcount, 9034 =>1 ))`
    - event_item NPC say: That spirit was very powerful. I'm glad that you were able to release it. Please keep this totem safe until you can return to Shar Vahl. Once you collect all of the totems, seal the box and return it to your master. May the spirits watch over you!
17. permafrost/"Scout Janomin", hand "Official Seal of the Khati Sha" (9031).
    - event_item NPC say: The spirit that you seek is deep within these halls. I tracked it into this lair more than a week ago. The spirit has taken up residence with the other bears in the lower chambers during that time. It should be relatively easy for your and your people to reach. Once you release the spirit, please return the totem to me. I will prepare it for the journey to Shar Vahl. May stealth and good fortune move with you.
      - Event guard: `(plugin::check_handin(\%itemcount, 9031 => 1))`
18. Spawns "The Icebound Spirit" (npc:73107) after the hand-in.
19. Kill "The Icebound Spirit" (NPC 73107) in `permafrost` and loot "Totem of the Ice Bear" (9036).
20. permafrost/"Scout Janomin", hand "Totem of the Ice Bear" (9036). Gives "Wrapped Ice Bear Totem" (9037).
    - event_item NPC say: Perfect work, $name! I am glad the Elders made such a wise choice in sending you. I must admit, I was rather scared during the exploration of these halls. This lair is quite foul, quite foul indeed! Take this wrapped totem and place it in the case that you were given. Once you have all of the totems, seal the case and make your way back to Shar Vahl. I work my way back as well. Thank you again.
      - Event guard: `(plugin::check_handin(\%itemcount, 9036 => 1))`
21. emeraldjungle/"Scout Vyrak", hand "Official Seal of the Khati Sha" (9031).
    - event_item NPC say: Well met, $name, well met indeed I find comfort in the fact that the jungle permitted your passage to me! Maybe there is still hope we can stop this disturbance before any more damage can be done to the balance of the spirit realm I have spent several weeks tracking the corrupted spirit. It seems to have made a home of the ruins just south of here. The spirit no longer resembles he entity that it once was. It is quickly becoming something foul and savage. Let us hope that you are not too late.'
Scout Vyrak says 'Destroy the spirit's current form and you will be able to retrieve the implement which has befouled it. Once you gather that totem please return it to me and I will wrap it so that you may carry it in the case that you were given in Shar Vahl.
      - Event guard: `(plugin::check_handin(\%itemcount, 9031 =>1 ))`
    - event_item NPC emote: You here a massive creature roar as if awakened from a deep sleep.
22. Spawns "The Spirit of Rage" (npc:94126) after the hand-in.
23. Kill "The Spirit of Rage" (NPC 94126) in `emeraldjungle` and loot "Totem of the Gorilla" (9038).
24. emeraldjungle/"Scout Vyrak", hand "Totem of the Gorilla" (9038). Gives "Wrapped Gorilla Totem" (9039).
    - event_item NPC say: Excellent work, $name! Judging by the speed with which it altered that spirit, this totem must be extremely powerful. I've wrapped it, so you should be safe from its magic. Just be sure to keep it in the case. Once you have all of the totems, seal the case and make your way back to Shar Vahl. They will be waiting for you there. I'll continue to look for the person that perpetrated this vile act.
      - Event guard: `(plugin::check_handin(\%itemcount, 9038 =>1 ))`
25. stonebrunt/"Scout Malom", hand "Official Seal of the Khati Sha" (9031).
    - event_item NPC say: Thank you for coming. I am surprised that you were able to find me. I barely know where I am at this point. I followed the vile beast that has been corrupting the spirits, but he eluded me after I followed him to that ridge up there. Fortunately, the spirit that you seek has remained at the site of its transformation. Use levitation to work your way up the falls and return to me with the totem that you will acquire from releasing the spirit.
      - Event guard: `(plugin::check_handin(\%itemcount, 9031 =>1 ))`
    - event_item NPC emote: Something glows brightly from high above the falls.
26. Spawns "The Spirit of Torment" (npc:100220) after the hand-in.
27. Kill "The Spirit of Torment" (NPC 100220) in `stonebrunt` and loot "Totem of the Watcher" (9040).
28. stonebrunt/"Scout Malom", hand "Totem of the Watcher" (9040). Gives "Wrapped Watcher Totem" (9041).
    - event_item NPC say: Great work, friend. Take this totem and place it in the case that you were given in Shar Vahl. Do not unwrap the totem and be quick in your pursuit of the others. Once you have all of the totems, please seal the case and return it to Shar Vahl. I can only hope that you will get to all of the spirits in time. Take care, friend.
      - Event guard: `(plugin::check_handin(\%itemcount, 9040 =>1 ))`
29. swampofnohope/"Scout Eyru", hand "Official Seal of the Khati Sha" (9031).
    - event_item NPC say: It is a relief to see you. I was beginning to fear that no one would be able to find me in this miserable swamp. I wanted to get word back to Shar Vahl about my location, but I was afraid that I would lose the trail off this spirit if I were to break off my pursuit. This location is as strange of a destination for our spirit as it is dangerous. I have seen the spirit several times and it is very out of place here. I can't help but think that the transformation has left the spirit confused beyond all repair.
      - Event guard: `(plugin::check_handin(\%itemcount, 9031 =>1 ))`
    - event_item NPC say: If you move towards the large body of water just north of here, you should be able to find a vantage point that will allow you to see it. The spirit has been resting under the surface of the water there for several days now. Once you release the spirit, please return to me with the totem that binds it. I will prepare the totem, so that you may return it to Shar Vahl.
    - event_item NPC emote: A giant reptile roars, as it sinks below the surface of the pond. It appears that is senses your approach.
30. Spawns "The Spirit of Sorrow" (npc:83244) after the hand-in.
31. Kill "The Spirit of Sorrow" (NPC 83244) in `swampofnohope` and loot "Totem of the Alligator" (9042).
32. swampofnohope/"Scout Eyru", hand "Totem of the Alligator" (9042). Gives "Wrapped Alligator Totem" (9043).
    - event_item NPC say: Splendid job, $name. This wrapping should help to shield you from any of the negative properties that may be manifested in the totem. You should be fine if you keep it in the box that you were given. Once you collect all of the totems, please seal the box and return it to Shar Vahl. Be careful to protect the totems during the course of your travels. The balance of power in several realms is reliant on your ability to fulfill this mission. Please do not fail us.
      - Event guard: `(plugin::check_handin(\%itemcount, 9042 =>1 ))`
33. Combine in "Carved Wooden Chest" (17361): "Wrapped Spider Totem" (9033), "Wrapped Wolf Totem" (9035), "Wrapped Ice Bear Totem" (9037), "Wrapped Gorilla Totem" (9039), "Wrapped Watcher Totem" (9041), "Wrapped Alligator Totem" (9043). Produces "Sealed Box of Totems" (9044). Requires Remove Traps.
34. sharvahl/"Elder Animist Dumul", hand "Sealed Box of Totems" (9044). Gives "Seal of Elder Dumul" (9045).
    - event_item NPC say: I have received word from several of our scouts indicating your impending arrival. We are all very pleased that you were able to release all of the spirits before any true harm could manifest itself. Your efforts have not only restored balance to the spirit realm, they seem to have also acted to hinder any other plans our antagonist may have had... for the time being.
      - Event guard: `(plugin::check_handin(\%itemcount, 9044 =>1 ))`
    - event_item NPC say: Our Taruun scouts have discovered Draz Nurakk's location. A scout has returned from a set of islands on the Old World. The islands are in a place called Timorous. The Taruun returned while leaving a scout behind to insure that the foul Animist does not evade us any further. You will need to find the island on which our scout has set up camp. The island has a great statue on it. Hopefully, he will still be in that location. Show him this seal and he will know that I sent you to assist.
35. timorous/"Scout Sihmoj", hand "Seal of Elder Dumul" (9045). Gives "Black Silk Sack" (17360).
    - event_item NPC say: Good to see you, now keep your head down friend. He may look out here at any moment, though he's been asleep most of the day. He's been staying in a ruined building on that island over there. I'm sure you can see it from here. You should be able to surprise him with little trouble. Just take care to avoid any traps he may have set. He's proven to be a very capable magic-user.
      - Event guard: `(plugin::check_handin(\%itemcount, 9045 =>1 ))`
    - event_item NPC say: When you finish with him, please bring any evidence of his being dispatched back to me in this bag. I'll direct you from there. Good luck... I'll watch from here.
36. Spawns "Draz Nurakks Image" (npc:96322) via `timorous/draz nurakk#event_death_complete`.
37. Kill "Draz Nurakks Image" (NPC 96322) in `timorous` and loot "Shards of Broken Glass" (9046).
38. Combine in "Black Silk Sack" (17360): "Shards of Broken Glass" (9046). Produces "Sack of Broken Glass" (9047). Requires Remove Traps.
39. timorous/"Scout Sihmoj", hand "Sack of Broken Glass" (9047). Gives "Sack of Broken Glass" (9048).
    - event_item NPC say: I knew that this creature had power, but how do you explain this? That fight was well beyond my comprehension. I'm not sure what to do other than have you return the bag to Elder Dumul. I'm sure that he will know what to do next. Take care and be swift.
      - Event guard: `(plugin::check_handin(\%itemcount, 9047 =>1 ))`
40. sharvahl/"Elder Animist Dumul", hand "Sack of Broken Glass" (9048). Gives "Note for Historian Qua" (9049).
    - event_item NPC say: My fears were well founded, and I am glad that I have had people that are able to understand those fears. Please do not think that I have intentionally placed you in the path of harm, but I did have my suspicions about our adversary's strength. I am not surprised that he was able to deceive us in this manner. I thank the spirits that you were able to evade harm in your completion of this task.
      - Event guard: `(plugin::check_handin(\%itemcount, 9048 =>1 ))`
    - event_item NPC say: Take this note to Arms Historian Qua. He has been researching a means of circumventing any protective magic that Draz Nurakk may have in place. When you meet him next, you will be well equipped to complete the restoration of balance to the spirit realm. Make your way to Qua and do as he says.
41. sharvahl/"Arms Historian Qua", hand "Note for Historian Qua" (9049). Gives "Qua's Receipt" (9050).
    - event_item NPC say: It is a pleasure to meet you, $name. The Animists mentioned that someone would be by, but for me not to wait, so I sent the information that they requested to Weapons Master Rahoul. He is having a master smith finish the blades.
      - Event guard: `(plugin::check_handin(\%itemcount, 9049 => 1))`
    - event_item NPC say: Take him this receipt and I'm sure that he'll get you the weapons as soon as possible. Take care. It appears that a lot of people are relying on you in this matter. You may be the only person that can do this.
42. sharvahl/"Weapons Master Rahoul", hand "Qua's Receipt" (9050). Gives "Rahoul's Collection Box" (17363).
    - event_item NPC say: You are just the time. The weapon that Elder Dumul requested has almost been completed. We need you to gather a few items in order to complete the weapon. These items will not require much effort to acquire, but I will need to tell you where to look. Place all of the items that I request in this box and return it to me as quickly as possible.
      - Event guard: `(plugin::check_handin(\%itemcount, 9050 => 1))`
    - event_item NPC say: Now, seek out a large chunk of perfect acrylia [ore], two Gems of the [void], and chunk of dense fungal [padding]. Once I have those items, I can finish the weapon that you will need to use to kill the dark animist.
43. Loot "Gem of the Void" (9053) from "Xi Xaui" (NPC 173047) in `maiden`. Drop cache: 6.5214% chance per kill.
44. Spawns "a boulder fiend" (npc:171063) via `thegrey/a creature#enter`.
45. Kill "a boulder fiend" (NPC 171063) in `thegrey` and loot "Perfect Acrylia Ore" (9052).
46. Loot "Chunk of Dense Fungal Padding" (9054) from "a deepspore mushroom" (NPC 164041) in `thedeep`. Drop cache: 15.9687% chance per kill.
47. Combine in "Rahoul's Collection Box" (17363): "Gem of the Void" (9053), "Perfect Acrylia Ore" (9052), "Chunk of Dense Fungal Padding" (9054). Produces "Sealed Collection Box" (9051). Requires Remove Traps.
48. sharvahl/"Weapons Master Rahoul", hand "Sealed Collection Box" (9051). Gives "Jagged Claw of Rending" (9055) + "Jagged Claw of Rending" (9056).
    - event_item NPC say: These claws should work well for you. The design was research by Historian Qua. They should work to neutralize the magical field that protects the dark animist and allow you to tear his scaly flesh from his frame. Remember that all of this is theoretical. Those claws are an original creation. You will be the first to prove their effectiveness in combat.
      - Event guard: `(plugin::check_handin(\%itemcount, 9051 => 1))`
    - event_item NPC say: Take the claws back to Animist Dumul and show him their design. Use them well, $name. May the spirits guide you in your attack.
49. sharvahl/"Elder Animist Dumul", hand "Jagged Claw of Rending" (9055) + "Jagged Claw of Rending" (9056). Gives "Acrylia Gilded Box" (17362) + "Khati Sha Seal of War" (9057).
    - event_item NPC say: These claws are exquisite. I can see that a great deal of thought went into their design. Now it is your turn to demonstrate your proficiency in your chosen role. You have a great challenge ahead of you, for we have determined that only these claws will work to harm this dark animist, this corrupter of spirits. You will need the support of your people; but in the end, only the strength of your will can save us.
      - Event guard: `(plugin::check_handin(\%itemcount, 9055 =>1, 9056 =>1 ))`
    - event_item NPC say: Our scouts have tracked Draz Nurakk to an abandoned village in the Fungus Grove. We learned of his intent to track you down. I take it that he did not appreciate your willingness to assist us. He knows who you are, so it will be best for us to get him before he can conjure up any more surprises. Find Scout Halmia in the Grove and give her this seal. Then bring the evidence of his destruction to me when you are done. Place his head, the seal, and those claws in this box and return it to me.
50. fungusgrove/"Scout Halmia", hand "Khati Sha Seal of War" (9057). Gives "Khati Sha Seal of War" (9062).
    - event_item NPC say: I thank the spirits that you have arrived. I would not have been able to stop the dark animist if he were to attempt to leave. He has made camp in an empty set of huts. He has moved from hut to hut, but made no attempt to leave the area. I would be wary of traps if I were you. I must admit that I was afraid. That is why I moved to this location. He should still be there though.
      - Event guard: `(plugin::check_handin(\%itemcount, 9057 =>1 ))`
51. Spawns "Draz Nurakk" (npc:157116) after the hand-in.
52. Kill "Draz Nurakk" (NPC 157116) in `fungusgrove` and loot "Draz Nurakk's Head" (9059).
53. Combine in "Acrylia Gilded Box" (17362): "Jagged Claw of Rending" (9055), "Jagged Claw of Rending" (9056), "Draz Nurakk's Head" (9059), "Khati Sha Seal of War" (9062). Produces "Sealed Gilded Wooden Chest" (9060). Requires Remove Traps.
54. sharvahl/"Elder Animist Dumul", hand "Sealed Gilded Wooden Chest" (9060). Gives "Claw of the Savage Spirit" (8495).
    - event_item NPC emote: opens the container and looks at its contents
      - Event guard: `(plugin::check_handin(\%itemcount, 9060 =>1 ))`
    - event_item NPC say: $name, you have saved the balance of the spirit realm. Your selflessness has made an impression that will last well beyond the effects of your recent deeds. The inhabitants of this realm are all in your debt. Your efforts to restore balance in the material realm have been worth more than we can reward you for.

## Epic 1.5

### "Savage Lord's Totem" (52911)

<a id="epic-item-52911"></a>

1. jaggedpine/"Rashara Wrualla", say "Hail".
    - Player: "hail"
      - NPC say: Aye, I do remember that face, Beastlord. I am still recovering from my short trip to Kuua that suffers from the touch of the Realm of Discord. What a dark and foul place it is. Some of the creatures have hearts so dark it is nearly inconceivable. One of those creatures has robbed me of what I hold [most dear].
      - Condition: `($client->GetGlobal("beast_epic") ==15)`
      - Condition: `($text=~/hail/i)`
2. Loot "Sullied Ankh Piece" (52903) from "Raving Sphinx Spiritservant".
3. rathemtn/"Ankhefenmut", hand "Sullied Ankh Piece" (52903). Gives "Gift of the Sphinx" (52905).
    - event_item NPC say: Beastlord, I am indeed impressed. We did not know that there was a dark magic on the ankh pieces. It seems the life that flows from the ankh will need to be restored, but I think we are safe now. Take this gift to return to the beastlord elders who aided us.
      - Event guard: `($client->GetGlobal("beast_epic") ==13)`
      - Event guard: `(plugin::check_handin(\%itemcount, 52903 =>1 ))`
4. sharvahl/"Elder Animist Muada", hand "Gift of the Sphinx" (52905).
    - event_item NPC say: Gracious, that is indeed a precious gift. I will present it to the elders when we next gather as a council. They will be overjoyed at the rescue. You may keep that Feral Lord's Brooch to yourself as a reminder of what you learned. All [does not end] here though.
      - Event guard: `($client->GetGlobal("beast_epic") ==14)`
      - Event guard: `(plugin::check_handin(\%itemcount, 52905 =>1 ))`
5. jaggedpine/"Rashara Wrualla", say "Not Possible". Gives "Request of the Elders" (52906).
    - Player: "not possible"
      - NPC say: It would mean a great deal to me and the elders if you could seek out this girplan in that eerie scarred land and, perhaps, discover what it did to my warder. I am unable to go myself as I could never dream of traveling without my warder. You will find a beastlord in Discord who also seeks the same creature. Give him this note.
      - Condition: `($client->GetGlobal("beast_epic") ==15)`
      - Condition: `($text=~/not possible/i)`
      - Linked from "luck" (explicit prompt).
6. draniksscar/"Yerika Sisslak", hand "Request of the Elders" (52906).
    - event_item NPC say: I have seen the creature nearby, but I have not been able to defeat it.  I am not strong enough.  Perhaps you may have better luck.  You must hurry.  It has used the warder spirit to create twisted and dark companions of its own. If you should overcome this creature, return to me.
      - Event guard: `(plugin::check_handin(\%itemcount, 52906 =>1 ))`
7. Spawns "Girplan Spiritleech" (npc:302085) after the hand-in.
8. Kill "Girplan Spiritleech" (NPC 302085) in `draniksscar` and loot "Rashara's Warder's Essence" (52907).
9. draniksscar/"Yerika Sisslak", hand "Rashara's Warder's Essence" (52907). Gives "Sealed Response to the Elders" (52908).
    - event_item NPC say: You have certainly accomplished what I was not able to. I must go now, but be sure to take this letter and the essence back to Rashara.
      - Event guard: `(plugin::check_handin(\%itemcount, 52907 =>1 ))`
10. jaggedpine/"Rashara Wrualla", hand "Rashara's Warder's Essence" (52907) + "Sealed Response to the Elders" (52908).
    - event_item NPC say: I am speechless. You have done what I thought was impossible. You've restored my place as a beastlord and an elder. I am forever in your debt. Return to Muada and tell him I sent you so you may hear the most-troubling news . . . it seems we know more about a true enemy of beastlords in Discord. I can say no more.
      - Event guard: `($client->GetGlobal("beast_epic") ==15)`
      - Event guard: `(plugin::check_handin(\%itemcount, 52907 =>1, 52908 =>1 ))`
11. sharvahl/"Elder Animist Muada", say "Stopped". Gives "Elder Cloak of Resilience" (52909).
    - Player: "stopped"
      - NPC say: Go speak to Erana Farrel. She is in the city of the dragorn and will most likely be in hiding while she investigates. She was the first to discover this evil plot and has the most information to help you. Give her this cloak. She had asked for some protection while she was out in that volatile realm.
      - Condition: `($client->GetGlobal("beast_epic") ==16)`
      - Condition: `($text=~/stopped/i)`
      - Linked from "beast" (explicit prompt).
      - Linked from "trapped spirits" (explicit prompt).
12. dranik/"Erana Farrel", hand "Elder Cloak of Resilience" (52909).
    - event_item NPC say: Egads, me friend. It has been summoned from the ground. Take as many friends as ye can muster. Ye are going to need them. This creature will be surrounded by summoned spirits of our very own warders. Ye must release as many of those abused spirits as ye can and dispatch the animist. That beast must have something he uses to control the warders. Return it to me!
      - Event guard: `(plugin::check_handin(\%itemcount, 52909 =>1 ))`
13. Spawns "Discordling Dark Animist" (npc:336126) after the hand-in.
14. Kill "Discordling Dark Animist" (NPC 336126) in `dranik` and loot "Discordant Totem of the Feral" (52910).
15. dranik/"Erana Farrel", hand "Discordant Totem of the Feral" (52910). Gives "Wrapped Discordant Totem of the Feral" (52914).
    - event_item NPC say: You are owed a great debt from beastlords everywhere. You have restored the revered spirits of the wild and they have returned to Norrath. And, what's this? Interesting. I would not have expected you to find this totem. Its markings are unfamiliar. I have wrapped it for you. You must go to see Muada at once and show him this.
      - Event guard: `($client->GetGlobal("beast_epic") ==16)`
      - Event guard: `(plugin::check_handin(\%itemcount, 52910 =>1 ))`
16. sharvahl/"Elder Animist Muada", hand "Wrapped Discordant Totem of the Feral" (52914). Gives "Savage Lord's Totem" (52911).
    - event_item NPC say: I am honored to have had the opportunity to observe you -- a feral champion for the ills that have befallen our kind. You have certainly made your name known among us. While the spirit world is not freed from danger, it is much more promising with all that you've done. Take this token of our appreciation. It may not appear to be too much right now, but it will be very important should you [wish to continue to walk among the elders] of the lords of beasts.
      - Event guard: `($client->GetGlobal("beast_epic") ==16)`
      - Event guard: `(plugin::check_handin(\%itemcount, 52914 =>1 ))`
    - event_item NPC message: You have gained 5 ability points!

## Epic 2.0

### "Spiritcaller Totem of the Feral" (57054)

<a id="epic-item-57054"></a>

**Earlier reward routes required by this graph path:** ["Savage Lord's Totem" (52911)](#epic-item-52911).
Revisit those instructions if another copy of a consumed item is needed.

1. global/"Global Player", say "Recipe:19908". Gives "Globe of Discordant Energy" (47100).
2. Spawns "Grimling Colonel" (npc:167426) via `grimling/scout husman#end the threat in the grimling forest`.
3. Kill "Grimling Colonel" (NPC 167426) in `grimling` and loot "Eerie Medallion" (57025).
4. jaggedpine/"Rashara Wrualla", say "Hail".
    - Player: "hail"
      - NPC say: Aye, I do remember that face, Beastlord. I am still recovering from my short trip to Kuua that suffers from the touch of the Realm of Discord. What a dark and foul place it is. Some of the creatures have hearts so dark it is nearly inconceivable. One of those creatures has robbed me of what I hold [most dear].
      - Condition: `($client->GetGlobal("beast_epic") ==15)`
      - Condition: `($text=~/hail/i)`
5. Spawns "Dismal Darkpaw Mystic" (npc:181225) via `jaggedpine/rashara wrualla#hail`.
6. Kill "Dismal Darkpaw Mystic" (NPC 181225) in `jaggedpine` and loot "Scalding Blood" (57058).
7. Loot "Fierce Spirit Clay" (57020) from "Spiritfrenzied Phoenix" (NPC 215062) in `poair`. Drop cache: 100% chance per kill.
8. sharvahl/"Elder Animist Muada", say "Make The Totem". Gives "Elders' Totem Mold" (52930).
    - Player: "make the totem"
      - NPC say: Very well. You must now fashion the shape of the totem and imbue it with what you have collected, but not without this bit of beastlord magic. The elders fashion this essence rarely, so treat it with care. You must find a way to blend the magic items taken from the earth and blood together to make the magical base for this totem. Then, use the result to surround a solid frame you find and bathe it with our essence with heat to form the magical basis for this treasured item. Then, you must use fires to mold it. I trush your knowledge and willingness to learn will guid you through this phase of your trials as a beastlord. Return to me and tell me that you are finished with this important duty. Be careful.
        - Reply guard: `(plugin::check_hasitem($client, 57025) && plugin::check_hasitem($client, 57058) && plugin::check_hasitem($client, 57020))`
      - Condition: `($client->GetGlobal("beast_epic") ==17)`
      - Condition: `($text=~/make the totem/i)`
      - Linked from "learning" (explicit prompt).
      - Linked from "task" (explicit prompt).
      - Linked from "prepared" (explicit prompt).
      - Linked from "there is more" (explicit prompt).
      - Linked from "problem" (explicit prompt).
9. sharvahl/"Elder Animist Muada", say "Task". Gives "Peculiar Unshapen Piece of Wood" (57011).
    - Player: "task"
      - NPC say: You must create a totem that is bound to the wild spirits as well as your own. At one time in their lives, each elder has had one. We used it to focus the power of our warders to make them stronger and to bond them to our own spirits. It is time for you to take on this labor of life, now that you are well on the path to becoming one with the elders. Are you [prepared] to do this?
      - Condition: `($client->GetGlobal("beast_epic") ==17)`
      - Condition: `($text=~/task/i)`
      - Linked from "hail" (explicit prompt).
      - Linked from "dedication" (explicit prompt).
      - Linked from "infected" (explicit prompt).
      - Linked from "requirements" (explicit prompt).
      - Linked from "learning" (explicit prompt).
      - Linked from "agree to take on this charge" (explicit prompt).
10. Combine in appropriate tradeskill container: "Fierce Spirit Clay" (57020), "Eerie Medallion" (57025), "Scalding Blood" (57058). Produces "Gilded Resonating Clay" (57029). Requires Pottery.
11. Combine in appropriate tradeskill container: "Peculiar Unshapen Piece of Wood" (57011), "Gilded Resonating Clay" (57029), "Combined Essence" (52913). Produces "Malleable Glowing Totem" (57050). Requires Baking.
12. Combine in appropriate tradeskill container: "Elders' Totem Mold" (52930), "Malleable Glowing Totem" (57050). Produces "Spiritbound Totem" (57027). Requires Blacksmithing.
13. sharvahl/"Elder Animist Muada", say "Trapped Spirits". Sets `beast_epic` to `18`.
    - Player: "trapped spirits"
      - NPC say: There are discordant beasts that have become twisted through no fault of their own. You may think of it as a spiritual plage, which has us mystified, but we need these creatures stopped. As they grow more infected with spirits, their strength is growing out of contol. We need you to go to that realm and find the source of the problem. They are incredibly large beasts, so beware and do not go alone. Go seek the scout.
      - Condition: `($client->GetGlobal("beast_epic") ==17)`
      - Condition: `(plugin::check_hasitem($client, 57027))`
      - Condition: `($text=~/trapped spirits/i)`
      - Linked from "finished" (explicit prompt).
14. causeway/"Jillaa Oogblat", say "Hail".
    - Player: "hail"
      - NPC say: Ah, you have the totem. Me call you friend. So friend, we gots big trouble here. Dem bazu are out of control. It not as dough dey weren't tough enough already! Dey gots da wrong spirits running in deir bodies. Dere is no way to calm dem eider. So we are going to have to kill them to get da spirits back. You must do dis. I tink dey know I'm here. Dey close by!
      - Condition: `(e.message:findi("hail") and qglobals["beast_epic"] == "18" and not eq.get_entity_list():IsMobSpawnedByNpcTypeID(303092))`
15. Spawns "Bazu Terror" (npc:303092) via `causeway/jillaa oogblat#hail`.
16. Spawns "a bazu crusher" (npc:303093) via `causeway/jillaa oogblat#hail`.
17. Spawns "Discordling Dark Animist" (npc:303094) via `causeway/bazu terror#event_death_complete`.
18. Kill "Discordling Dark Animist" (NPC 303094) in `causeway` and loot "Dark Animist Wand" (57012).
19. causeway/"Jillaa Oogblat", hand "Dark Animist Wand" (57012).
    - event_trade NPC say: Dat must be it! Da creature had da wand dat infected creatures. It must have tried to make an army. We done solved it! Me will wrap it and [keep] it until me see Muada soon. Me stay a bit to be sure dat dis not happen again.
      - Event guard: `(qglobals["beast_epic"] == "18" and item_lib.check_turn_in(e.trade, {item1 = 57012}))`
20. sharvahl/"Elder Animist Muada", say "Agree To Take On This Charge". Gives "Blended Elixir of Fortitude" (57051).
    - Player: "agree to take on this charge"
      - NPC say: I had no doubts, $name... Messenger, you may return to our scouts and tell them that our friend here will take on the hunt for the lost scout. Give Jillaa this elixir. I'm sure she is in need of it and it will alert her to your acceptance of the task.
      - Condition: `($client->GetGlobal("beast_epic") ==19 && $text=~/agree to take on this charge/i)`
      - Linked from "trapped spirits" (sequence only; unverified).
21. causeway/"Jillaa Oogblat", hand "Blended Elixir of Fortitude" (57051).
    - event_trade NPC say: Yes, yes, welcome back. Me so worried. Me gave dat wand to scout, an ogre friend, and now it gone! And so is da scout. Someone told me dey found a tattered tunic dat looked liked da scout may have worn it quite far from here! It covered in strange black hairs and a sharp claw was stuck in it. Me don't want to tink about dat too much. It make me sad. Please go find da scout. And hurry!
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 57051}))`
22. Spawns "DDA" (npc:301069) via `bloodfields/tormented scout#strong`.
23. Kill "DDA" (NPC 301069) in `bloodfields` and loot "Gemmed Dark Animist Wand" (57014).
24. bloodfields/"Tormented Scout", hand "Gemmed Dark Animist Wand" (57014). Gives "Wrapped Gemmed Wand" (57052).
    - event_trade NPC emote: looks at you with sad eyes. 'Me so sorry, but me could not stop it. Wand is terrible power. Me wrap it again like Jillaa. You take it to Muada, quickly. Me tinks we did it! It has no power without dis wand!
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 57014}))`
25. sharvahl/"Elder Animist Muada", hand "Wrapped Gemmed Wand" (57052).
    - event_item NPC say: Well, this indeed explains why we were never rid of the dark animist. I do believe you have overcome that despicable fiend. I feel the wild spirits are safe now. But that doesn't mean we're done with you. What I must ask you will be the most difficult task yet. The dark animist has been using a magical item of great power. It holds within it the very essence of Discord that drives much of the dark animist's energy. You must bring one to me so we may study it and prevent any further abuse of our most beloved creatures. If you complete this task, you must also give me your Spiritbound Totem when you return, for it will indeed be time for you to transcend. If you have [lost] it, please tell. We may be able to help you.
      - Event guard: `(plugin::check_handin(\%itemcount, 57052 =>1 ))`
26. sharvahl/"Elder Animist Muada", hand "Globe of Discordant Energy" (47100) + "Spiritbound Totem" (57027). Gives "Sealed Letter from Muada" (57053).
    - event_item NPC emote: appears overwhelmed. 'There is no limit to your greatness, is there? You have done more than any other to save us -- the masters of the wild. Your time has come, savage lord. You are about to meet one of the very first beastlords of Luclin. Her name is Alladnu Eshiara. She is often found in the wild, studying nature and the ways of feral creatures. Find her, give her this letter and your Savage Lord Totem and she will complete your journey. I will be there in spirit friend.
      - Event guard: `($client->GetGlobal("beast_epic") ==21 && plugin::check_handin(\%itemcount, 47100 =>1, 57027 =>1 ))`
27. hollowshade/"Alladnu Araihse", hand "Savage Lord's Totem" (52911) + "Sealed Letter from Muada" (57053).
    - event_trade NPC say: Follow me, . We will embark upon the final steps of your journey.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 52911,item2 = 57053}))`
28. hollowshade/"Alladnu Araihse", say "Ready". Gives "Spiritcaller Totem of the Feral" (57054).
    - Player: "ready"
      - NPC say: Then you have finished your journey. Here ends my service and those of the spirits. You are one with the spirits now. Travel your life's journey with pride.
      - NPC message: You have gained 10 ability points!
      - Condition: `(e.message:findi("ready") and qglobals["beast_epic"] == "22" and finished_event==1)`
      - Linked from "hail" (sequence only; unverified).
