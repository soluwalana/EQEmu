# Paladin

Steps taken from the quest graph only. **Broken** means the graph has no edge for that value or that item.

Flags with writes: `paladin_epic`.

## 0. Prerequisites

Shared acquisition steps appear in the first prerequisite chain that needs them. Later sections reference that chain rather than repeating it.

### "Token of Heroism" (69955)

1. Loot "Valdoon Kel'Novar's Heart" (69981) from "Valdoon Kel'Novar" in `mmcc`.
2. felwithea/"Galrun Starforge", hand "Valdoon Kel'Novar's Heart" (69981). Gives "Token of Cleansing" (69956).
    - Dialogue with felwithea/"Galrun Starforge":
      - Player: "Hail"
        - NPC say: Hail to you, . I'm very glad to see a paladin such as yourself here in Felwithe. There have been some [odd occurrences] as of late.
        - Condition: `(qglobals["paladin_epic"] == "9")`
        - Condition: `(e.message:findi("hail"))`
      - Player: "Occurrences" (link: explicit mention)
        - NPC say: Yes, about a week ago, I was helping Nora close up for the night at the Shop of All Holos. I left the shop and decided to take a quick stroll around Felwithe before going home to sleep, and I found something odd outside of the cleric's guild. I saw a Vampire! He was walking around and for a second our eyes met. . .I ran to get the guards. By the time I returned he was gone and the guards didn't believe that a Vampire was able to get this far into Felwithe. The next day I went and spoke to Lord Tynkale and [explained] to him what I saw.
        - Condition: `(qglobals["paladin_epic"] == "9")`
        - Condition: `(e.message:findi("occurrences"))`
      - Player: "Explained" (link: explicit mention)
        - NPC say: I told him how I saw a Vampire near the cleric's guild and how he wasn't there when the guards returned. Lord Tynkale didn't believe me, however, he did promise to give me a chance to prove what I saw. You will need to assist me in proving what I saw, , for I think that Vampire may have been scouting for an invasion of Felwithe. Go to all the cities in Faydwer and investigate any odd occurrences there, for I think there might be other Vampire sightings throughout the continent. Take this bag and fill it with any proof you find. Good luck crusader.
        - Condition: `(qglobals["paladin_epic"] == "9")`
        - Condition: `(e.message:findi("explained"))`
        - Gives Galrun's bag (69975).
      - Player: "Valdoon"
        - NPC say: I'm sorry, , but you need more people before we can begin this.
          - Reply guard: `not is_gm and e.other:GetRaidMemberCountInZone() < paladin_minimum_players`
        - NPC say: Very well, . The fate of all of the residents of this continent are now in your hands. Cleanse the Mistmoore Catacombs of the Vampire infestation and put an end to Valdoon Kel`Novar. Bring me his heart when you are finished, for I need proof to show Lord Tynkale that Vampire invasion has been stopped.
          - Reply guard: ``
        - Condition: `(qglobals["paladin_epic"] == "9")`
        - Condition: `(qglobals["paladin_epic_mmcc"] == "1" and e.message:findi("valdoon"))`
3. provinggrounds/"Pashia Clouddancer", say "Note". Gives "Note from Pashia" (69973).
    - Dialogue with provinggrounds/"Pashia Clouddancer":
      - Player: "Hail"
        - NPC say: At last I am free again! Thank you so much for saving me from the horrors of this vile place. You have my gratitude. I can find my way out from here friend. Here take this [note] back to my brother. It should explain what good deed you have done for me today.
          - Reply guard: `arrived`
        - NPC say: Uuugh. . .
          - Reply guard: ``
        - Condition: `(e.other:HasItem(69956))`
        - Condition: `(e.message:findi("hail"))`
      - Player: "Note" (link: explicit mention)
        - NPC say: Ok, here's the note for you. Thank you again!
        - Condition: `(e.other:HasItem(69956))`
        - Condition: `(e.message:findi("note") and arrived)`
        - Gives Note from Pashia (69973).
      - Player: "Duram Wants You To Come Home" (link: conversation sequence)
        - NPC say: Duram sent you? Unbelievable. Before I go anywhere, I need my sword back, it was taken from me earlier. That beast in there took it and knocked me down. . .he thought I was dead because I didn't move. Defeat him and bring me back my sword and I will leave with you.
        - Condition: `(e.other:HasItem(69956))`
        - Condition: `(e.message:findi("duram wants you to come home") and not following)`
        - Spawns NPC 316075.
      - Player: "Follow" (link: external event mention)
        - Prompted by `event_trade`:
          - NPC say: My sword, you have brought it back to me. Thank you , you truly are heroic. Now, let us get out of here. I will [follow] you when you are ready.
          - Event guard: `(e.other:HasItem(69956))`
          - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 69974}))`
        - NPC say: Ok, let's get out of here!
        - Condition: `(e.other:HasItem(69956))`
        - Condition: `(e.message:findi("follow") and e.other:GetID()==event_starter:GetID())`
4. nedaria/"Duram Firechaser", hand "Note from Pashia" (69973). Gives "Token of Heroism" (69955).
    - Dialogue with nedaria/"Duram Firechaser":
      - Player: "Hail"
        - NPC say: Hail to you, . I see you are a knight. Do you happen to be on a [quest of truth]?
        - Condition: `(e.other:HasItem(69956))`
        - Condition: `(e.message:findi("hail"))`
      - Player: "Quest Of Truth" (link: explicit mention)
        - NPC say: Perhaps you can assist me, then. My sister, Pashia, is a Wayfarer just as I am. She is very bold, however, and ends up getting herself in a lot of trouble quite a bit. This time, she has gotten herself into [deep trouble] and I'm not sure if anyone can help her.
        - Condition: `(e.other:HasItem(69956))`
        - Condition: `(e.message:findi("quest of truth"))`
      - Player: "Deep Trouble" (link: explicit mention)
        - NPC say: Reports are coming in from the Wayfarer scouts that she has wandered off deep into Discord by herself. She is always reckless and it's frustrating; I care for her a lot, but she doesn't take anyone else's feelings into account when she does something like this. Well, I won't dwell on this much more. Here is what I wish for you to do. . .I would like you to find Pashia in Discord and escort her back to safety. Please be careful, the reports show that Discord is a very dangerous place. One last thing. . .if you find Pashia, tell her that [Duram wants you to come home]. Thank you, heroic knight!
        - Condition: `(e.other:HasItem(69956))`
        - Condition: `(e.message:findi("deep trouble"))`

### "Token of Cleansing" (69956)

1. Acquisition of "Token of Cleansing" (69956) is documented under "Token of Heroism" (69955); obtain another copy if needed.

### "Redemption" (64031)

1. Spawns "A Corrupted Koalindl" (69141) in `oot` on event_fish_success.
2. Loot "Corrupted Koalindl's Heart" (69929) from "A Corrupted Koalindl".
3. Spawns "A Corrupted Koalindl" (224432) in `gunthak` on event_fish_success.
4. Loot "Corrupted Koalindl's Heart" (69930) from "A Corrupted Koalindl".
5. Spawns "A Corrupted Koalindl" (93306) in `overthere` on event_fish_success.
6. Loot "Corrupted Koalindl's Heart" (69931) from "A Corrupted Koalindl".
7. Spawns "A Corrupted Koalindl" (182150) in `nedaria` on event_fish_success.
8. Loot "Corrupted Koalindl's Heart" (69932) from "A Corrupted Koalindl".
9. qeynos2/"Enic Ruklin", hand "Corrupted Koalindl's Heart" (69929) + "Corrupted Koalindl's Heart" (69930) + "Corrupted Koalindl's Heart" (69931) + "Corrupted Koalindl's Heart" (69932). Sets `paladin_epic` to `4`.
10. qeynos2/"Enic Ruklin", hand "Corrupted Koalindl's Heart" (69929) + "Corrupted Koalindl's Heart" (69930) + "Corrupted Koalindl's Heart" (69931) + "Corrupted Koalindl's Heart" (69932). Gives "Seal of Enic" (69933).
11. Say "Hail" to skyfire/"Dry Sapara".
12. Spawns "Rithnok the Tormented" (91193).
13. Loot "Rithnok's Soulstone" (69935) from "Rithnok the Tormented".
14. skyfire/"Dry Sapara", hand "Rithnok's Soulstone" (69935). Gives "Rithnok's Soulstone" (69936).
    - Dialogue with skyfire/"Dry Sapara":
      - Player: "Hail"
        - NPC say: Welcome $name. I see you have the Seal of Enic, I imagine you have done a very good deed for Enic to acquire that. If Enic gave you that, he must trust you. And if he trusts you, then so shall I. I ask a favor of you, paladin. I wish for you to help me with a servant of mine. Rithnok, a very loyal servant of the Peak, disappeared a few days ago. He has returned, but he is not the same. . .he appears beaten and torn. I feel he has been tormented by some unknown being. For what reason? I do not know. However, he must be relieved of his suffering. I ask you to release him from the confines of this world and bring me back anything you find. Go now.
          - Reply guard: `($client->GetGlobal("paladin_epic") ==4 && plugin::check_hasitem($client, 69933))`
        - NPC say: What brings you here mortal? I am the new guardian of Veeshan's Peak and I will not allow you to pass. And even if I did, the ward on the door will not allow you to pass. Though, you do seem like the resourceful type and I do have something that I need researched. Would you be [willing to do a task] for me?
          - Reply guard: ``
        - Condition: `($text=~/hail/i)`
        - Spawns NPC 91193.
      - Player: "Willing To Do A Task" (link: explicit mention)
        - NPC say: Very well. Veeshan's Peak is a very old sanctuary of the Ring of Scale. This monument has been here longer than you and I have lived and will remain here past you and your lifetime. There is very little known about the monument itself though. I've been told that Veeshan's Peak was created by a powerful dragon, one who followed Jaled Dar. His name was Suled Dar and he created this place by forging the magma and stone with his will. It was said that Suled Dar fought alongside Jaled Dar against the iksars and fell to their ruler. It was also said that through his strength of mind and skill with magic, he destroyed one of the greatest iksar outposts by shaking the ground and creating a pit that swallowed the outpost whole. That type of magic is unimaginable these days, yet I yearn for that knowledge -- the power to shape a structure with my own mind out of the earth. [continue]
        - Condition: `($text=~/willing to do a task/i)`
      - Player: "Continue" (link: explicit mention)
        - NPC say: It was said that when Suled Dar was slain, he wasn't laid to rest in the Necropolis like other dragons. He chose to be buried here, in the Skyfire Mountains where he built his masterpiece. He created four globes here in the mountains, which I do not know the function for, though I have studied them intensely. They have a mystical power that I'm not certain of, but I have my own beliefs about them. Here is what I would like you to do . . . I would like you to gather a small force and activate the four globes. I will try to cast a spell that fills the globes with energy and we will try to figure out this mystery. Come back to me when you are [ready] and we will begin this experiment.
        - Condition: `($text=~/continue/i)`
      - Player: "Ready" (link: explicit mention)
        - NPC say: Very well. You and your companions need to activate the globes while I attempt to channel energy into them. Go and do this now.
        - Condition: `(($text=~/ready/i) && !defined($qglobals{dragon_not_ready}))`
15. Ground spawn of "Soulstone Shard" (69937) in `draniksscar`.
16. Ground spawn of "Soulstone Shard" (69938) in `bloodfields`.
17. Ground spawn of "Soulstone Shard" (69939) in `causeway`.
18. Ground spawn of "Soulstone Shard" (69940) in `dranik`.
19. Combine in "Rithnok's Soulstone" (69936): "Soulstone Shard" (69937), "Soulstone Shard" (69938), "Soulstone Shard" (69939), "Soulstone Shard" (69940). Produces "Rithnok's Soulstone" (69941). The combine does not fail.
20. dawnshroud/"Mikhal Young", hand "Drema's Fingerbone" (69946). Sets `paladin_epic` to `5`.
21. dawnshroud/"Mikhal Young", say "Find Anything". Requires `paladin_epic` ==4. Gives "Drema's Locket" (69945).
22. letalis/"Drema Young", hand "Drema's Locket" (69945). Requires `paladin_epic` set. Requires `paladin_epic` >=4. Gives "Drema's Fingerbone" (69946).
23. dawnshroud/"Denns Rootenpaw", hand "Drema's Fingerbone" (69946). Requires `paladin_epic` ==5. Gives "Bone Collector's Bag" (69947).
    - Dialogue with dawnshroud/"Denns Rootenpaw":
      - Player: "Hail"
        - NPC say: Can I help you? Can't you see that I'm busy right now.
        - Condition: `($text=~/Hail/i)`
24. Loot "Dark Skeleton Remains" (69927) from "A Sun Revenant" in `thegrey`.
25. Loot "Dark Skeleton Remains" (69926) from "Disturbed Elysian Remains" (NPC 176016) in `umbral`. Drop cache: 2.58% chance per kill.
26. Loot "Dark Skeleton Remains" (69925) from "A Soriz Slave" (NPC 162029) in `ssratemple`. Drop cache: 35% chance per kill.
27. Combine in "Bone Collector's Bag" (69947): "Dark Skeleton Remains" (69927), "Dark Skeleton Remains" (69926), "Dark Skeleton Remains" (69925). Produces "Bone Collector's Bag" (69948). The combine does not fail.
28. dawnshroud/"Denns Rootenpaw", hand "Bone Collector's Bag" (69948). Requires `paladin_epic` ==5. Gives "Enchanted Bone Powder" (69949).
29. Hand "Enchanted Bone Powder" (69949) to letalis/"Drema Young". Spawns "Drema Young" (169128). Loot "Drema's Soulstone" (69928) from "Drema Young".
30. Loot "Soulstone Shard" (69950) from "Coterie Corruptor" in `tenebrous`.
31. Spawns "Shade of Mujaki the Devourer" (204081) in `ponightmare` on event death_complete:204080.
32. Loot "Soulstone Shard" (69951) from "Shade of Mujaki the Devourer".
33. Combine in "Drema's Soulstone" (69928): "Soulstone Shard" (69950), "Soulstone Shard" (69951). Produces "Drema's Soulstone" (69952). The combine does not fail.
34. abysmal/"Lovine Lemise", say "Ingredients". Requires `paladin_epic` ==5. Gives "Lovine's Potion Bag" (69922).
    - Dialogue with abysmal/"Lovine Lemise":
      - Player: "Hail"
        - NPC say: $name, I am glad you are here. My name is Lovine and the poor soul lying on the bed over here is my good friend Reiya. My friend could use some [assistance].
        - Condition: `($client->GetGlobal("paladin_epic") ==5 && $text=~/hail/i)`
      - Player: "Assistance" (link: explicit mention)
        - NPC say: I should probably begin by telling you what happened. Reiya was found a couple of days ago on the shore in Natimbi, face down in the water. The Wayfarers that found him were not sure if he was dead or not, until they brought him here to Abysmal. It appears he was unconcious at the time, since he later awoke on this bed. Something is terribly [wrong] with him though.
        - Condition: `($client->GetGlobal("paladin_epic") ==5 && $text=~/assistance/i)`
      - Player: "Wrong" (link: explicit mention)
        - NPC say: I'm not sure what is wrong with him, though he constantly fades in and out of consciousness. His speech is erratic when he is awake, and his thoughts do not appear to be in this world. I have a feeling that he is being tormented in some way, but I do not know how or why. I would like you to gather a few things for me, to make a concoction that may awaken Reiya. I will tell you what the [ingredients] are.
        - Condition: `($client->GetGlobal("paladin_epic") ==5 && $text=~/wrong/i)`
      - Player: "Ingredients" (link: explicit mention)
        - NPC say: I am looking for the following things: a Potameid seaweed strand, blood from a Mastruq Havocblade, the tail of a Noc Fleshfeaster, and the jawbone of Ra'Tuk Screambringer. Place the items in this enchanted potion bag, and return it to me so that we can attempt to awaken Reiya. Please be dilligent in your search, $name.
        - Condition: `($client->GetGlobal("paladin_epic") ==5 && $text=~/ingredients/i)`
        - Gives Lovine's Potion Bag (69922).
35. Loot "Ra'Tuk Screambringer's Jaw" (69921) from "A Ra'Tuk Screambringer" (NPC 283104) in `barindu`. Drop cache: 4.06% chance per kill.
36. Loot "Noc Fleshfeasters Tail" (69920) from "A Noc Fleshfeaster" in `riwwi`.
37. Loot "Mastruq Havocblade Blood" (69919) from "A Mastruq Havocblade" in `qinimi`.
38. Loot "Mastruq Havocblade Blood" (69919) from "A Mastruq Warfiend" in `qinimi`.
39. Loot "Potameid Seaweed Strands" (69918) from "An Entrapped Potameid" in `natimbi`.
40. Combine in "Lovine's Potion Bag" (69922): "Ra'Tuk Screambringer's Jaw" (69921), "Noc Fleshfeasters Tail" (69920), "Mastruq Havocblade Blood" (69919), "Potameid Seaweed Strands" (69918). Produces "Lovine's Potion Bag" (69923). The combine does not fail.
41. abysmal/"Lovine Lemise", hand "Lovine's Potion Bag" (69923). Sets `paladin_epic_reiya` to `1`.
42. Summon "Foldable Medicine Bag" (17770) by casting "Unfold Medicine Bag".
43. Buy "Fine Potion Vial" (95846) from "Dargon" (NPC 29000) in `halas`. Base price: 1,750 copper.
44. Loot "Robust Shadow Essence" (96911) from "Qua Senshali Xakra" (NPC 158020) in `vexthal`. Drop cache: 28.72% chance per kill.
45. Loot "Sage Leaf" (14215) from "a Di'zok Herbalist" in `chardok`.
46. Loot "Sage Leaf" (14215) from "a Sarnak Herb Collector" in `chardok`.
47. Loot "Sage Leaf" (14215) from "an Apprentice Herbalist" in `chardok`.
48. Loot "Valerian Root" (14230) from "a Di'zok Herbalist" in `chardok`.
49. Loot "Valerian Root" (14230) from "a Sarnak Herb Collector" in `chardok`.
50. Loot "Valerian Root" (14230) from "an Apprentice Herbalist" in `chardok`.
51. Buy "Woundwart" (16526) from "Zok Kuluree" (NPC 50164) in `rathemtn`. Base price: 400 copper.
52. Combine in "Foldable Medicine Bag" (17770): "Fine Potion Vial" (95846), "Robust Shadow Essence" (96911), "Sage Leaf" (14215), "Valerian Root" (14230), "Woundwart" (16526). Produces "Mist of the Breathless" (96937). Requires Alchemy, trivial 224.
53. abysmal/"Reiya The Pained", hand "Mist of the Breathless" (96937). Requires `paladin_epic_reiya` ==1. Gives "Reiya's Soulstone" (69924).
54. Spawns "Shade of Reiya the Pained" (284104) in `ferubi` on enter.
55. Loot "Soulstone Shard" (69943) from "Shade of Reiya the Pained".
56. Loot "Soulstone Shard" (69944) from "Vuranish Xxuro" in `vxed`.
57. Combine in "Reiya's Soulstone" (69924): "Soulstone Shard" (69943), "Soulstone Shard" (69944). Produces "Reiya's Soulstone" (69942). The combine does not fail.
58. hohonora/"Irak Altil", say "Hail". Sets `paladin_epic` to `6`.
59. Loot "Redis' Soulstone" (69983) from "Shade of Redis Linrok" in `dranikcatacombsa`.
60. Spawns "Durunal the Cursebearer" (300087) in `wallofslaughter` on enter.
61. Loot "Dark and Twisted Sword" (69971) from "Durunal the Cursebearer".
62. hohonora/"Irak Altil", hand "Dark and Twisted Sword" (69971). Requires `paladin_epic` ==6. Gives "Dark and Twisted Sword" (69972).
63. Combine in "Dark and Twisted Sword" (69972): "Rithnok's Soulstone" (69941), "Drema's Soulstone" (69952), "Reiya's Soulstone" (69942), "Redis' Soulstone" (69983). Produces "Redemption" (64031). The combine does not fail.

### "Rithnok's Soulstone" (69941)

1. Acquisition of "Rithnok's Soulstone" (69941) is documented under "Redemption" (64031); obtain another copy if needed.

### "Reiya's Soulstone" (69942)

1. Acquisition of "Reiya's Soulstone" (69942) is documented under "Redemption" (64031); obtain another copy if needed.

### "Drema's Fingerbone" (69946)

1. Acquisition of "Drema's Fingerbone" (69946) is documented under "Redemption" (64031); obtain another copy if needed.

### "Drema's Soulstone" (69952)

1. Acquisition of "Drema's Soulstone" (69952) is documented under "Redemption" (64031); obtain another copy if needed.

### "Token of Compassion" (69953)

1. Acquisition of "Redemption" (64031) is documented under "Redemption" (64031); obtain another copy if needed.
2. hohonora/"Irak Altil", say "Tell Me About Your Master". Sets `paladin_epic` to `9`.
3. qeynos2/"Camlend Serbold", say "Gem". Requires `paladin_epic` ==9. Gives "Unfilled Set of Prayer Beads" (69968).
    - Dialogue with qeynos2/"Camlend Serbold":
      - Player: "Hail"
        - NPC say: It has been a while, . You look troubled, is there anything I can help you with? Do you know anyone that needs the [curing] touch of Rodcet Nife?
        - Condition: `(qglobals["paladin_epic"] == "9")`
        - Condition: `(e.message:findi("hail"))`
      - Player: "Curing" (link: explicit mention)
        - NPC say: I might have something that will aid you in curing Kemik. Make a small donation of say 500 platinum to Ziska and she will craft powerful prayer beads that will help Kemik. With the beads Ziska crafts you will need to combine them with [special gems].
        - Condition: `(qglobals["paladin_epic"] == "9")`
        - Condition: `(e.message:findi("curing"))`
      - Player: "Gem" (link: conversation sequence)
        - NPC say: The gems that will be needed I can't help you with, . Travel to the city of North Freeport and seek out a holy knight like yourself. Hopefully he will be able to help you for Kernik's sake.
        - Condition: `(qglobals["paladin_epic"] == "9")`
        - Condition: `(e.message:findi("gem"))`
        - Gives Unfilled Set of Prayer Beads (69968).
      - Player: "Hail" (link: conversation sequence)
        - NPC say: I say, good to meet you, ! I am Camlend Serbold. Some call me Serbold the Great. I am the leader of the righteous order of paladins which serves the Temple of Life. Together with the clerics of this temple, we defend the will of the great [Rodcet Nife] and smite all who dare to oppose us.
        - Condition: ``
        - Condition: `(e.message:findi("hail"))`
      - Player: "Rodcet Nife" (link: explicit mention)
        - NPC say: Do you feel your heart beating within your chest? It is Rodcet Nife, the Prime Healer, whose breath keeps it in perfect rhythm. If you do not pray to His glory then I assure you, someday when your heart begins to slow, you shall be crying out loud to Rodcet Nife.
        - Condition: ``
        - Condition: `(e.message:findi("rodcet nife"))`
      - Player: "Lord Grimrot" (link: external event mention)
        - Prompted by `event_trade`:
          - NPC say: We thank you for your service. With Lord Grimrot's evil soul trapped in this scythe, all but the truly evil shadowknights would be able to wield it. I would like to present you with this as a token of our appreciation. Your devotion to life is supreme. Go now, and serve life.
          - Event guard: `(fac <= 3)`
          - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 13324,item2 = 13325}))`
        - NPC say: You have heard of Lord Grimrot? He is a shadowknight working with the Bloodsabers. We have word he is trying to build an army of undead. Only a powerful knight can rid the lands of Grimrot. So, did you come here to [defend life]?
        - Condition: ``
        - Condition: `(fac <= 3)`
        - Condition: `(e.message:findi("lord grimrot"))`
      - Player: "Defend Life" (link: explicit mention)
        - NPC say: Do you feel your heart beating within your chest? It is Rodcet Nife, the Prime Healer, whose breath keeps it in perfect rhythm. If you do not pray to His glory then I assure you, someday when your heart begins to slow, you shall be crying out loud to Rodcet Nife.
        - Condition: ``
        - Condition: `(fac <= 3)`
        - Condition: `(e.message:findi("defend life"))`
      - Player: "Trades" (link: external event mention)
        - Prompted by `event_trade`:
          - NPC say: Welcome to the Temple of Life. You have much to learn and we have much work to do. Pain, hurt, disease and death lurk everywhere, our job is seemingly endless, but none is more gratifying. Here is our guild tunic, represent us well. Davloran Girionlis will help you to get started. Return to me when you have become more experienced in our art, I will be able to further instruct you on how to progress through your early ranks, as well as in some of the various [trades] you will have available for you.
          - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 18711}))`
        - NPC say: I thought you might be one who was interested in the various different trades, but which one would suit you? Ahh, alas, it would be better to let you decide for yourself, perhaps you would even like to master them all! That would be quite a feat. Well, lets not get ahead of ourselves, here, take this book. When you have finished reading it, ask me for the [second book], and I shall give it to you. Inside them you will find the most basic recipes for each trade. These recipes are typically used as a base for more advanced crafting, for instance, if you wished to be a smith, one would need to find some ore and smelt it into something usable. Good luck!
        - Condition: ``
        - Condition: `(e.message:findi("trades"))`
        - Gives Tradeskill Basics : Volume I (51121).
      - Player: "Second Book" (link: explicit mention)
        - NPC say: Here is the second volume of the book you requested, may it serve you well!
        - Condition: ``
        - Condition: `(e.message:findi("second book"))`
        - Gives Tradeskill Basics : Volume II (51122).
4. rivervale/"Kaya Cloudfoot", say "Different About It". Requires `paladin_epic` ==9. Gives "Note from Kaya" (69970).
    - Dialogue with rivervale/"Kaya Cloudfoot":
      - Player: "Hail"
        - NPC say: Hello there noble Paladin. We have been expecting you. Word has been traveling fast about the great deed you are doing to help Kemik out. You seek the final gem to that set of prayer beads you're making?
        - Condition: `(qglobals["paladin_epic"] == "9")`
        - Condition: `(e.message:findi("hail"))`
      - Player: "Yes"
        - NPC say: We halflings don't come across special gems every day ya know. A few seasons ago we happened to be preparing this huge feast for the mayor when a strange [visitor] happened to pass through the vale.
        - Condition: `(qglobals["paladin_epic"] == "9")`
        - Condition: `(e.message:findi("yes"))`
      - Player: "Visitor" (link: explicit mention)
        - NPC say: He didn't stay long. Just long enough to have a bite and some drink and he continued his journey. Before he left he left a gem for the vale. None of us were expecting anything in return. We held onto it because we knew there was something [different about it].
        - Condition: `(qglobals["paladin_epic"] == "9")`
        - Condition: `(e.message:findi("visitor"))`
      - Player: "Different About It" (link: explicit mention)
        - NPC say: I think your eyes should see for themselves. Take this note over to Cheel. He will give you the precious gem of ours. Good luck with your journey .
        - Condition: `(qglobals["paladin_epic"] == "9")`
        - Condition: `(e.message:findi("different about it"))`
        - Gives Note from Kaya (69970).
      - Player: "Hail" (link: conversation sequence)
        - NPC say: A pleasure to make your acquaintance . I am Kaya Cloudfoot. first Paladin of the Storm Reapers. I traveled long ago when I was just a wee sprout to the city of Qeynos far to the west. It was there I grew under the tutelage of the Knights of Thunder. a noble order of paladins loyal to Karana. the Storm Lord. I have returned now to Rivervale to teach interested young halflings the ways of a Knight of the Storm Reapers so that we may defend Karanas people and lands from the [evil forces] that would see it destroyed.
        - Condition: ``
        - Condition: `(e.message:findi("hail"))`
      - Player: "Evil Forces" (link: explicit mention)
        - NPC say: There are many problems and creatures that trouble Karanas people through out Norrath and threaten our otherwise peaceful ways of life. Our common folk here in Rivervale are troubled by the wicked Teir`Dal. the Death Fist Orcs. and the Goblins of Clan Runnyeye and Pickclaw. It is the calling and duty of a Knight of the Storm Reapers to defend the common folk from these enemies of Rivervale. Are you willing to [defend the commoners]?
        - Condition: ``
        - Condition: `(e.message:findi("evil forces"))`
      - Player: "Commoners" (link: explicit mention)
        - NPC say: You have made an honorable decision. . First you will need to be outfitted in a suit of armor to protect you from the weapons of our foes. Seek Jimji Bottletoe here in Rivervale and give him this letter. Jimji will instruct you further on acquiring a suit of armor worthy of a new Knight of the Storm Reapers. When you have been outfitted in your Bravefoot Armor return to me and I shall prepare you for your [next task].
        - Condition: ``
        - Condition: `(e.message:findi("commoners"))`
        - Gives Letter to Jimji Bottletoe (19628).
      - Player: "Next Task" (link: explicit mention)
        - NPC say: The Teir'Dal. or Dark Elves that reside in the underground city of Neriak to the east beyond the Commonlands have long been a bane to us Storm Reapers. Many of our Druids have fallen attempting to hold back the tide of hate and destruction that has taken hold on the Nektulos Forest and threatens the surrounding lands. It was also the Teir`Dals patron God. Innorruuk. who caused the [Curse of Bloody Kithicor]. Are you ready to [face the Teir'Dal] and bloody your hands for the protection of your Shire and our commoners humble way of life?
        - Condition: ``
        - Condition: `(e.message:findi("next task"))`
      - Player: "Curse of Bloody Kithicor" (link: explicit mention)
        - NPC say: There was a great war that was fought not long ago between the Teir'Dal. and their evil minions. and the armies of Felwithe. Qeynos. Freeport. and Kaladim. In the Kithicor Woods the Daughter of Innoruuk. Lanys T'Vyl. and her minions fought against the chosen of Tunare. Firiona Vie. and her most loyal allies. The evil God of Hate. Innoruuk. intervened every living creature in the Kithicor Woods instantly fell dead as a great rift to the Plane of Hate appeared in the sky. Since that time. when night falls on the Kithicor Woods blood seeps from the trees and ground and the hateful dead hunt any living being who dares to trespass in the woods that ended their lives.
        - Condition: ``
        - Condition: `(e.message:findi("Curse of Bloody Kithicor"))`
      - Player: "face the Teir" (link: explicit mention)
        - Prompted by player input: "Next Task"
        - NPC say: Some days ago one of our Storm Reapers. a ranger by the name of Botim Bonker. ventured into the Kithicor Forest at daybreak on a routine patrol and never returned. That night his bloodied tunic was found hanging on a fence post of Tagglefoots Farm. The blood was dried and many hours old. We believe that he was slain during the day and that deduction coupled with the fact the undead of Kithicor do not leave the woods nor possess the intelligence or means to sneak into Rivervale and leave the tunic where it would surely be found by fellow Storm Reapers led us to believe they were not responsible. We believe it was the work of the Teir'Dal. Search the Kithicor Woods by daylight and punish the Teir'Dal responsible. Return with the villains severed hands as proof of his death.
        - Condition: ``
        - Condition: `(e.message:findi("face the Teir"))`
      - Player: "Trades" (link: external event mention)
        - Prompted by `event_trade`:
          - NPC say: Karana smiles upon you young ! Take this tunic to keep you warm through the storms you must face. There is evil encroaching upon the lands of Karana's faithful. The wicked minions of Bertoxxulous and the Teir'Dal children of Hate corrupt the lands to the west and east, and the Deathfist Clan of Orcs are waging war on this region while destoying the wilderness for lumber and stone. It is Karana's will that we defend our lands and way of life from these evil threats. When you are ready to begin adventuring, I will be happy to advise you on how to help us deal with the [evil forces]. I also posses knowledge of various [trades], seek me out when you wish to learn about them.
          - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 18431}))`
        - NPC say: I thought you might be one who was interested in the various different trades, but which one would suit you? Ahh, alas, it would be better to let you decide for yourself, perhaps you would even like to master them all! That would be quite a feat. Well, lets not get ahead of ourselves, here, take this book. When you have finished reading it, ask me for the [second book], and I shall give it to you. Inside them you will find the most basic recipes for each trade. These recipes are typically used as a base for more advanced crafting, for instance, if you wished to be a smith, one would need to find some ore and smelt it into something usable. Good luck!
        - Condition: ``
        - Condition: `(e.message:findi("trades"))`
        - Gives Tradeskill Basics : Volume I (51121).
      - Player: "Second Book" (link: explicit mention)
        - NPC say: Here is the second volume of the book you requested, may it serve you well!
        - Condition: ``
        - Condition: `(e.message:findi("second book"))`
        - Gives Tradeskill Basics : Volume II (51122).
5. rivervale/"Deputy Cheel", hand "Note from Kaya" (69970). Gives "Rivervale Prayer Bead" (69967).
    - Dialogue with rivervale/"Deputy Cheel":
      - Player: "Nice Hat"
        - NPC say: Thank you, It is worn with pride and is the symbol of the Rivervale Militia
        - Condition: `(e.message:findi("nice hat"))`
6. akanon/"Lewis Reldnok", say "Blessed Gem". Triggers `akanon/lewis reldnok#timer:check_sit`.
    - Dialogue with akanon/"Lewis Reldnok":
      - Player: "Hail"
        - NPC say: Greetings What can a brave and noble Paladin like I help you with? Are you possibly looking for a [blessed gem]?
        - Condition: `qglobals["paladin_epic"] ~= nil and qglobals["paladin_epic"] == "9"`
        - Condition: `e.message:findi("hail")`
      - Player: "Blessed Gem" (link: explicit mention)
        - NPC say: So you're the one that we been hearing about. Excellent work so far . Helping Kemik out like you are brings pride to every Paladin on Norrath. Sit before me sir and you shall receive the holy gem of Ak`Anon.
        - Condition: `qglobals["paladin_epic"] ~= nil and qglobals["paladin_epic"] == "9"`
        - Condition: `e.message:findi("blessed gem")`
      - Player: "Trades" (link: external event mention)
        - Prompted by `event_trade`:
          - NPC say: Welcome to the Abbey of Deep Musing, ! Here is a tunic that you may wear to announce the beginning of your training as a Paladin of Brell Serilis! Be warned that the only dangers do not lie without Ak'Anon. There is an evil society that lurks in the deepest recesses and shadows of our magnificent city. When you are ready to begin your training, let me know. I will be able to further instruct you on how to progress through your early ranks, as well as in some of the various [trades] you will have available to you.
          - Event guard: `item_lib.check_turn_in(e.trade, {item1 = 18433})`
        - NPC say: I thought you might be one who was interested in the various different trades, but which one would suit you? Ahh, alas, it would be better to let you decide for yourself, perhaps you would even like to master them all! That would be quite a feat. Well, lets not get ahead of ourselves, here, take this book. When you have finished reading it, ask me for the [second book], and I shall give it to you. Inside them you will find the most basic recipes for each trade. These recipes are typically used as a base for more advanced crafting, for instance, if you wished to be a smith, one would need to find some ore and smelt it into something usable. Good luck!
        - Condition: ``
        - Condition: `e.message:findi("trades")`
        - Gives Tradeskill Basics : Volume I (51121).
      - Player: "Second Book" (link: explicit mention)
        - NPC say: Here is the second volume of the book you requested, may it serve you well!
        - Condition: ``
        - Condition: `e.message:findi("second book")`
        - Gives Tradeskill Basics : Volume II (51122).
7. Sit before the NPC while its timer checks your posture.
8. akanon/"Lewis Reldnok", on timer check_sit. Gives "Ak'anon Prayer Bead" (69966).
9. erudnint/"Josper Kenshed", say "Collect Component". Gives "Empty Bag" (17944).
    - Dialogue with erudnint/"Josper Kenshed":
      - Player: "Hail"
        - NPC say: Come forward and speak. What is it you seek within these walls? Let it be the knowledge of wizardry. for that is what we are. Only a [servant of wizardry] should be within these walls.
        - Condition: `(e.message:findi("hail"))`
      - Player: "Servant Of Wizardry" (link: explicit mention)
        - NPC say: A servant. you say? If you be a young apprentice. perhaps you might assist me? I could use you to [collect components]. If you believe yourself to be beyond such things. you may wish to assist me with a [special matter].
        - Condition: `(e.message:findi("servant of wizardry"))`
      - Player: "Collect Component" (link: explicit mention)
        - NPC say: Of course you may assist me!! We have much need of a certain item which can only be found in the frigid peaks of Everfrost. There you shall find creatures called ice goblins. Take this bag and fill it with ice goblin beads and be sure to combine them before you return them. Well, then... Off with you!! And be quick about it and I shall give you a fine wizard's weapon. None of this rust-covered garbage offered by our associates!
        - Condition: `(e.message:findi("collect component"))`
        - Gives Empty Bag (17944).
      - Player: "Special Matter" (link: explicit mention)
        - Prompted by player input: "Servant Of Wizardry"
        - NPC say: It seems my last apprentice was sent into Toxxulia to test a spell I call Ice Capade, well, everyone else calls it Column of Frost, how droll! Anyway... he never returned. I fear he is nothing more than BONES, though I hope I'm wrong. Could you find good old Ilanic and ask him, [where is the scroll]?! I do not wish it to fall into enemy hands. Return it and I shall let you keep the scroll. Oh yes, It is only half of a spell. I forgot to send him the full scroll. I imagine that is why he was not victorious.
        - Condition: `(e.message:findi("special matter"))`
10. Loot "Goblin Ice Necklace" (13897) from "Redwind" in `everfrost`.
11. Loot "Goblin Ice Necklace" (13897) from "An Ice Goblin Scout" in `everfrost`.
12. Loot "Goblin Ice Necklace" (13897) from "An Ice Goblin Whelp" in `everfrost`.
13. Loot "Goblin Ice Necklace" (13897) from "An Icy Orc" in `everfrost`.
14. Loot "Goblin Ice Necklace" (13897) from "Ice Goblin Diver" in `everfrost`.
15. Combine in "Empty Bag" (17944): "Goblin Ice Necklace" (13897). Produces "Bag of Ice Necklaces" (13898). The combine does not fail.
16. halas/"Lysbith Mcnaff", hand "Bag of Ice Necklaces" (13898). Gives "Iron Ration" (13005).
    - Dialogue with halas/"Lysbith Mcnaff":
      - Player: "Hail"
        - NPC say: Hail! Ye've come to [serve Halas]. have ye not? We're the Wolves o' the North and it is our task to defend our city from harm.
        - Condition: `(e.message:findi("Hail"))`
      - Player: "Serve Halas" (link: explicit mention)
        - NPC say: Halas is surrounded by barren arctic tundra. We've many foes. Among them are the [orc troopers]. [ice goblins] and the ever-present polar bears.
        - Condition: `(e.message:findi("serve halas"))`
      - Player: "What Orc Troopers" (link: explicit mention)
        - NPC say: So. Ye think yerself strong enough to battle the snow orc troopers? I pray to the Tribunal that ye are. If ye can return to me four wrath orc wristbands from the troopers' bodies. I'll reward ye with the [Seax].
        - Condition: `(e.message:findi("what orc troopers"))`
      - Player: "What Ice Goblins" (link: explicit mention)
        - Prompted by player input: "Serve Halas"
        - NPC say: The ice goblins have plagued our community fer some time now. At times. they even manage to get inside our walls. Fer the most part. they prey on travelers who pass through Everfrost Peaks. Since they're a weak race. we employ our youngest warriors to [protect the pass].
        - Condition: `(e.message:findi("what ice goblins"))`
      - Player: "What Seax" (link: explicit mention)
        - Prompted by player input: "What Orc Troopers"
        - NPC say: The Seax is a Northman warrior's piercing weapon. Dinnae confuse this with another [weapon] related to the Seax called the Langseax. The local rogues have also learned to master the Seax. I'll only offer it to those who battle the [orc troopers].
        - Condition: `(e.message:findi("what seax"))`
      - Player: "Gnoll Bounty" (link: external event mention)
        - Prompted by `event_trade`:
          - NPC say: Ye've done well, me young . We've gathered these to add to yer provisions. While in the Everfrost Peaks, be on the watch fer any gnolls ye may find. I declare there to be a [gnoll bounty].
          - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 13898}))`
        - NPC say: I've placed a bounty on the gnolls o'Blackburrow. Their whelps have invaded our land and we must carry the fight into their dens. Join the fight and return three gnoll fangs as proof of yer victory in Blackburrow. Do so, and earn the respect o' the Wolves o' the North.
        - Condition: `(e.message:findi("gnoll bounty"))`
      - Player: "Protect The Pass" (link: explicit mention)
        - Prompted by player input: "What Ice Goblins"
        - NPC say: Then travel to the Everfrost Peaks and take this pack with you. I want you to return this pack to me when it is filled with the beaded ice necklaces of the Ice Goblins. When it is filled, combine the items and return it to me and I shall decide if you deserve a reward for your deed.
        - Condition: `(e.message:findi("protect the pass"))`
        - Gives Empty Bag (17944).
17. potranquility/"Elder Fuirstel", say "Hail". Sets `pop_cod_final` to `1`.
    - Dialogue with potranquility/"Elder Fuirstel":
      - Player: "Hail"
        - NPC message: Elder Fuirstel slowly turns towards you. You can feel the heat radiating from his face. The warding that envelopes your body reaches out and begins to surround him. You immediately see improvement in his condition. The pus filled sores covering his face and his burning fever start to vanish.
        - NPC say: Thank you friend. I no longer feel the touch of death on my soul. However I do feel the grasp on Bertoxxulous, his plague is still upon me but not spreading throughout my body. I fear the only way to remove this pox would be to weaken Bertoxxulous enough that his curse would be lifted. I now renounce my faith in Bertoxxulous, please fell this god so that I may continue and learn from my mistakes.
        - NPC message: You receive a character flag!
        - Condition: `($text=~/hail/i && $pop_pod_alder_fuirstel == 1 && $pop_pod_grimmus_planar_projection == 1 && $pop_pod_elder_fuirstel == undef)`
        - Sets `pop_pod_elder_fuirstel` to `1`.
      - Player: "Hail" (link: conversation sequence)
        - NPC emote: Elder Fuirstel looks surprisingly better than when you last saw him. Elder Fuirstel says 'You actually did it! You defeated Bertoxxulous! I could feel it the moment he fell. Thank you very much, $name. You have done this world a great service.'
        - NPC message: You receive a character flag!
        - Condition: `($text=~/hail/i && $pop_cod_bertox == 1)`
        - Sets `pop_cod_final` to `1`.
18. poknowledge/"Aid Grimel", say "Skill In Brewing". Requires `pop_cod_final` ==1. Requires `pop_cod_final` set. Gives "Portable Drink Barrel" (17179).
    - Dialogue with poknowledge/"Aid Grimel":
      - Player: "Hail"
        - NPC say: Greetings and Salutations $name! I am Grimel, aid to the mighty paladin Councilman Taldarius. In between his duties to the city, Taldarius and I spend most of our time in the Planes cleansing evil. Even now I am preparing for battle. Taldarius intends to go further into the Planes than ever before on our next trip and I am working on gathering the special supplies we need. If you are willing to help I may have some use for your skills if you are a master of trades and have traveled in the Planes.
        - Condition: `($text=~/hail/i)`
      - Player: "Willing To Help And Am A Master Of Trades" (link: conversation sequence)
        - NPC say: Excellent! I am looking for a smith to add a special imbue to Councilman Taldarius's armor. Are you well versed in the art of smithing?
        - Condition: ``
        - Condition: `(defined($qglobals{pop_cod_final}) && ($qglobals{pop_cod_final} == 1))`
        - Condition: `($text=~/willing to help and am a master of trades/i)`
      - Player: "Versed In The Art Of Smithing" (link: explicit mention)
        - NPC say: Thank you for offering to help $name. Take this breastplate and clean it with a diluted acid wash to get all of the debris out of it. Brew the wash by combining acid and three celestial essences. Once the armor is cleaned, coat it with hurricane temper. Finally add two black diamonds of nightmare to the breastplate. This should provide adequate protection for our next journey.
          - Reply guard: `($client->GetRawSkill(63) >= 220)`
        - NPC say: You do not seem to be skilled enough.
          - Reply guard: ``
        - Condition: ``
        - Condition: `(defined($qglobals{pop_cod_final}) && ($qglobals{pop_cod_final} == 1))`
        - Condition: `($text=~/versed in the art of smithing/i)`
        - Gives Filthy Breastplate (15984).
      - Player: "Skill In Brewing" (link: conversation sequence)
        - NPC say: I bet you could make a wicked brew! However I am forced to drink a refreshing drink while out adventuring. I do have this powder that will give the best drinks quite a bite though. Mix the powder in with two Kaladim Constitutionals and a flask of pure water. If you need more dust just ask for it! Put three twice brewed constitutionals and the signet in this drink barrel. As hard as drink barrels are to get these days, you need to return it to me along with the drink you create with it.
          - Reply guard: `($client->GetRawSkill(65) >= 220)`
        - NPC say: You do not seem to be skilled enough.
          - Reply guard: ``
        - Condition: ``
        - Condition: `(defined($qglobals{pop_cod_final}) && ($qglobals{pop_cod_final} == 1))`
        - Condition: `(($text=~/skill in brewing/i) && plugin::check_hasitem($client, 16249))`
        - Gives Portable Drink Barrel (17179).
        - Gives Fermenting Dust (15992).
        - Gives Fermenting Dust (15992).
        - Gives Fermenting Dust (15992).
      - Player: "Put My Jewel Craft Skills To The Test" (link: external event mention)
        - Prompted by `event_item`:
          - NPC say: gulps down a Twice Brewed Constitutional and burps loudly! 'Ahhhh that was refreshing! That should hold me over for quite some time. I see you are quite deft of hand, perhaps you would care to put your jewel craft skills to the test?'
          - Event guard: `(plugin::check_handin(\%itemcount, 15993 => 1, 17179 => 1))`
        - NPC say: My hand was crushed when I used it to deflect a blow from a War Boar that was headed towards Taldarius's back. For some time afterwards my hand was crippled but Brell saw to it I regained full use of it. The ring I used to wear was damaged beyond repair and my hand was never steady enough to etch a new one. If you would make me a new one by combining a mounted blue diamond, the etching dust and etching tools in a jewelry kit. Then take the faceted gem and combine it with a bar of pure enchanted velium and my signet. I have no idea how the pure bars are made. You may want to seek the help of the ice dwarves.
          - Reply guard: `($client->GetRawSkill(68) >= 220)`
        - NPC say: You do not seem to be skilled enough.
          - Reply guard: ``
        - Condition: ``
        - Condition: `(defined($qglobals{pop_cod_final}) && ($qglobals{pop_cod_final} == 1))`
        - Condition: `(($text=~/put my jewel craft skills to the test/i) && plugin::check_hasitem($client, 16250))`
        - Gives Etching Dust (15988).
      - Player: "Ready To Use Some Clay" (link: external event mention)
        - Prompted by `event_item`:
          - NPC say: grins. 'Quite a nice ring you have made for me $name. May it serve me as well as my old ring. Here take this signet. We seem to be finishing the tasks on my list at a nice pace. Tell me when you are ready to use some clay.
          - Event guard: `(plugin::check_handin(\%itemcount, 15991 => 1))`
        - NPC say: On our last tome gathering expedition a stray arrow in the Plane of War struck our urn filled with sacred water. It was quite a waste of sacred water! Three large enchanted blocks of clay, three lacquered opals, a vial of purified mana, a ceramic lining, sculpting tools and the urn pattern should make an unfired urn. The urn is so large you will need to fire it with three divine crystalline glazes. Once you have the urn it needs to be filled with three sacred waters and the signet as a cap.
          - Reply guard: `($client->GetRawSkill(69) >= 220)`
        - NPC say: You do not seem to be skilled enough.
          - Reply guard: ``
        - Condition: ``
        - Condition: `(defined($qglobals{pop_cod_final}) && ($qglobals{pop_cod_final} == 1))`
        - Condition: `(($text=~/ready to use some clay/i) && plugin::check_hasitem($client, 16251))`
        - Gives Urn Pattern (16243).
      - Player: "Am Skilled With The Needle" (link: conversation sequence)
        - NPC say: I appreciate the help $name. I need a new tunic made for Councilman Taldarius. Last trip through the Plane of Disease, one of those flies spit mucus on him and it dripped through his armor seams! The result was a gooey mess that ate away all the leather underneath. It was a blessing he was wearing something under all that metal! Combine three firesilk swatches, a vial of purified mana, an emblem of fire, a firestrand curing agent, a tunic pattern and the signet. Bring it to me when you have completed it.
          - Reply guard: `($client->GetRawSkill(61) >= 220)`
        - NPC say: You do not seem to be skilled enough.
          - Reply guard: ``
        - Condition: ``
        - Condition: `(defined($qglobals{pop_cod_final}) && ($qglobals{pop_cod_final} == 1))`
        - Condition: `(($text=~/am skilled with the needle/i) && plugin::check_hasitem($client, 16252))`
      - Player: "Skills With A Fletching Knife" (link: external event mention)
        - Prompted by `event_item`:
          - NPC say: Good work $name. This will definitely serve Councilman Taldarius well. Here take this! If you have skills with a fletching knife I may have a job for you to do.
          - Event guard: `(plugin::check_handin(\%itemcount, 15986 => 1))`
        - NPC say: Aye I can see you are skilled with the fletching knife $name. It is good too, I need to replace Councilman Taldarius's bow from Plane of Air. Combine a planing tool, two wind metal bow cams, an air arachnid silk string, a featherwood staff and the signet. I hope the bow will be up to his standards, he sure loved his old bow.
          - Reply guard: `($client->GetRawSkill(64) >= 220)`
        - NPC say: You do not seem to be skilled enough.
          - Reply guard: ``
        - Condition: ``
        - Condition: `(defined($qglobals{pop_cod_final}) && ($qglobals{pop_cod_final} == 1))`
        - Condition: `(($text=~/skills with a fletching knife/i) && plugin::check_hasitem($client, 32800))`
      - Player: "Master Chef" (link: external event mention)
        - Prompted by `event_item`:
          - NPC say: Masterful work $name! I can see your skill in the curves of the bow. Take this as a sign of my respect for your skill. The last item I need before we can be off is some food. I warn you this will truly test your skills. Do you fancy yourself a master chef?
          - Event guard: `(plugin::check_handin(\%itemcount, 16247 => 1))`
        - NPC say: When we adventure in the Planes there is only one meal that keeps us in top fighting shape. It is called a Bristlebane's Party Platter. Unfortunately the platter is awkward and not easy to adventure with so you need to place them in this satchel. I know not how to make the Platter, a rather nice female Halfling cleric always used to deliver them to us but I heard she was crushed by a Regrua while hunting for a rare component in the Plane of Water. Brell bless her soul! Combine three of the platters and the signet inside the satchel.
          - Reply guard: `($client->GetRawSkill(60) >= 220)`
        - NPC say: You do not seem to be skilled enough.
          - Reply guard: ``
        - Condition: ``
        - Condition: `(defined($qglobals{pop_cod_final}) && ($qglobals{pop_cod_final} == 1))`
        - Condition: `(($text=~/master chef/i) && plugin::check_hasitem($client, 16254))`
        - Gives Field Satchel (17180).
19. Loot "Cask" (16580) from "Tugog Grigol" in `rathemtn`.
20. Buy "Hops" (16591) from "Heidi Grainsifter" (NPC 1065) in `qeynos`. Base price: 15 copper.
21. Buy "Malt" (16595) from "Heidi Grainsifter" (NPC 1065) in `qeynos`. Base price: 15 copper.
22. Buy "Yeast" (16596) from "Heidi Grainsifter" (NPC 1065) in `qeynos`. Base price: 15 copper.
23. Combine in "Portable Drink Barrel" (17179): "Cask" (16580), "Hops" (16591), "Malt" (16595), "Yeast" (16596). Produces "Mead" (13008). Requires Brewing, trivial 41.
24. erudnext/"Reklon Gnallen", hand "Iron Ration" (13005) + "Mead" (13008). Requires `paladin_epic` ==9. Gives "Erudin Prayer Bead" (69965).
    - Dialogue with erudnext/"Reklon Gnallen":
      - Player: "Hail"
        - NPC say: Good to see you friend. You appear to have had a long journey so far. We have been expecting you after Camlend sent word that you might be headed this way. Do you still [seek a rare gem] to help cure your friend Kemik?
        - Condition: `(e.other:HasItem(69960))`
        - Condition: `(e.message:findi("hail"))`
      - Player: "Rare Gem" (link: explicit mention)
        - NPC say: n preparation for your arrival we discussed such a rare gem that we might have for you. After the long discussion we decided it was for a good cause and we would be glad to help you. But first we must have a peaceful meal together. Go over to the Erudin Surplus store and buy us both an iron ration and a bottle of mead.
        - Condition: `(e.other:HasItem(69960))`
        - Condition: `(e.message:findi("rare gem"))`
      - Player: "Hail" (link: explicit mention)
        - Prompted by player input: "Hail"
        - NPC say: Hail to you, friend. Seek you knowledge or atonement in this temple of peace?
        - Condition: ``
        - Condition: `(e.message:findi("hail"))`
      - Player: "Seek Knowledge" (link: conversation sequence)
        - NPC say: Many are the things I could speak to you of. Have you any specific interest?
        - Condition: ``
        - Condition: `(e.message:findi("seek knowledge"))`
      - Player: "Seek Atonement" (link: conversation sequence)
        - NPC say: Yes. Many are those who enter these halls seeking the forgiveness, the atonement of a god. By turning their spirit against whatever wrong they have committed they may be able to receive redemption in the eyes of their diety. Many seek such a thing, but few truly have the strength of spirit to attain it.
        - Condition: ``
        - Condition: `(e.message:findi("seek atonement"))`
      - Player: "Temple Of Peace" (link: explicit mention)
        - Prompted by player input: "Hail"
        - NPC say: Dedicated to the god of peace, Quellious, is this temple. It is here that her clerics and paladins pray and receive inspiration.
        - Condition: ``
        - Condition: `(e.message:findi("temple of peace"))`
      - Player: "Paladins" (link: explicit mention)
        - NPC say: As the clerics are the warm hand of healing, the paladins are the stalwart shield of protection, and in times of grave need the sharp sword of justice. To our post must we always remain vigilant, else dishonor might befall us.
        - Condition: ``
        - Condition: `(e.message:findi("paladins"))`
      - Player: "Remain Vigilant" (link: explicit mention)
        - NPC say: To a paladin the upholding of his duty, or honor to his temple is foremost. To fail in his duty to stand at his assigned post in time of need is a great disgrace. Few are the paladins who have done so, and their spirits have been outcast from the god of peace.
        - Condition: ``
        - Condition: `(e.message:findi("remain vigilant"))`
      - Player: "Outcast" (link: explicit mention)
        - NPC say: Harsh though it seems, a true paladin must always remain vigilant and dedicated to his cause. If he does not then he might find himself fallen from grace.
        - Condition: ``
        - Condition: `(e.message:findi("outcast"))`
      - Player: "Fallen From Grace" (link: explicit mention)
        - NPC say: here are a few who have done so. Only a few that come to mind. Such stories are useful to remember as reminders of our beliefs.
        - Condition: ``
        - Condition: `(e.message:findi("fallen from grace"))`
      - Player: "Stories" (link: explicit mention)
        - NPC say: One is the story of the paladin who fell due to his weakness in the duty of his guard post. He let himself be seduced by a peasant woman
        - Condition: ``
        - Condition: `(e.message:findi("stories"))`
      - Player: "Peasant Woman" (link: explicit mention)
        - NPC say: Many hundreds of years ago did this story begin. There was a paladin, whose name is lost to all but our oldest leaders, who was among the greatest examples of honor. It was his post to guard the chambers to our most important halls. His fall was a creature in the guise of a poor peasant woman.
        - Condition: ``
        - Condition: `(e.message:findi("peasant woman"))`
      - Player: "Sacrifice"
        - NPC say: Only this crest and the sacrifice of something that symbolizes your strength and purity will release his spirit into the cleansing flames of our lady Quellious. Go now.
        - Condition: ``
        - Condition: `(e.message:findi("sacrifice"))`
25. Summon "Quiver of Marr" (17307) by casting "Quiver of Marr".
26. rathemtn/"Shin Master Grubbus", hand "Quiver of Marr" (17307). Requires `paladin_epic` ==9. Gives "Gukta Prayer Bead" (69964).
    - Dialogue with rathemtn/"Shin Master Grubbus":
      - Player: "Hail"
        - NPC say: Welcome back, young Shin. I hope your training is going well. I have made note of your progress as best I can, and you are truly following in the footsteps of Marr with every day that passes. As a paladin of Marr we must uphold His name and destroy those that wish to bring evil upon our people. Under Marr, I am able to offer you an additional path for training, should you truly desire to follow the path of a [Paladin].
        - Condition: `($text=~/hail/i)`
      - Player: "Paladin" (link: explicit mention)
        - NPC say: Very good. Initiates of the Knighthood of Marr must pass a series of tests. If you are devout and loyal to our cause you will be rewarded with our [ceremonial armor].
        - Condition: `($text=~/paladin/i)`
      - Player: "Ceremonial Armor" (link: explicit mention)
        - NPC say: We, the Shin Initiates, play an important role as mentors, healers, and warriors against evil in the Guktan Army. As a Shin Initiate all your battles should be fought in Marr's name. To show your homage to both Mithaniel Marr and our fellow brethren in the Guktan Army, young initiates are encouraged to complete a series of tasks that, when completed, will grant a set of Shin Initiate Armor. This armor shows your dedication and commitment to our cause. If you truly wish to walk in the path of The Truthbringer, I strongly suggest you complete your set of armor before venturing too far outside of the swamp. Are you [ready to begin]?
        - Condition: `($text=~/ceremonial armor/i)`
      - Player: "Ready To Begin" (link: explicit mention)
        - NPC say: Take this assembly kit. When you combine various items together in the assembly kit, you can create the different pieces of armor that you will need, such as [helm], [armguards], [breastplate], [bracers], [gauntlets], [legplates], and [boots]. If you would like to start crafting your armor, just tell me what piece you would like to craft and I will give you further instructions.
        - Condition: `($text=~/ready to begin/i)`
        - Gives Shin Initiate's Assembly Kit (17834).
      - Player: "Helm" (link: explicit mention)
        - NPC say: The Helm of the Shin Initiate is one of the more difficult parts of your armor that you will craft. Make sure you are prepared before you venture out to locate the needed items. To make your helm you will need to gather a Giant Snake Rattle, one Fungus Clump, one Spider Legs, and two Small Bricks of Ore from Innothule. If you cannot find any ore in the swamp, you might be able to find some ore for sale by visiting the local merchants. Once you have found these items, combine them in your assembly kit and take the newly created material to a forge, such as the one in the Gukta Exchange, along with this mold.
        - Condition: `($text=~/helm/i)`
        - Gives Mold for Froglok Helms (38932).
      - Player: "Armguards" (link: explicit mention)
        - Prompted by player input: "Ready To Begin"
        - NPC say: To create armguards, go to Innothule and find a Giant Snake Rattle, two Snake Fangs, one Spiderling Legs, and one Small Brick of Ore. If you cannot find any ore in the swamp, you might be able to find some ore for sale by visiting the local merchants. Once you have found these items, combine them in your assembly kit and take the newly created material to a forge, such as the one in the Gukta Exchange, along with this mold.
        - Condition: `($text=~/armguards/i)`
        - Gives Mold for Froglok Sleeves (38929).
      - Player: "Breastplate" (link: explicit mention)
        - Prompted by player input: "Ready To Begin"
        - NPC say: This is the most difficult item that you will make. Please meditate on this and make sure you are ready before you begin. Through great perseverance and piety we are able to overcome almost any obstacle. To make a Breastplate of the Shin Initiate you will need to travel to the Common Lands, the Deserts of Ro, and Innothule Swamp and gather a Lightstone, one Pristine Giant Scarab Carapace, a Desert Tarantula Chitin, a Deathfist Slashed Belt, and two Small Bricks of Ore. If you cannot locate any ore in your travels, you might be able to find some ore for sale by visiting the local merchants. Once you have found these items, combine them in your assembly kit and take the newly created material to a forge, such as the one in the Gukta Exchange, along with this mold. After you have completed your Breastplate, come back to talk to me if you wish to perform your [final test].
        - Condition: `($text=~/breastplate/i)`
        - Gives Mold for Froglok Chestplates (38933).
      - Player: "Bracers" (link: explicit mention)
        - Prompted by player input: "Ready To Begin"
        - NPC say: Creating bracers is a fairly easy task. However even the most basic of tasks are important when done in Marr's name. Gather one Snake Fang, one Zombie Skin, one Turquoise, and one Small Brick of Ore from the swamp. If you cannot locate any ore in the swamp, you might be able to find some ore for sale by visiting the local merchants. Once you have found these items, combine them in your assembly kit and take the newly created material to a forge, such as the one in the Gukta Exchange, along with this mold.
        - Condition: `($text=~/bracers/i)`
        - Gives Mold for Froglok Wristguards (38928).
      - Player: "Gauntlets" (link: explicit mention)
        - Prompted by player input: "Ready To Begin"
        - NPC say: Gauntlets are a good choice. Gauntlets of the Shin Initiate are fairly simple to craft. You will need to gather one Small Mosquito Wing, one Large Snake Skin, two Zombie Skins, and one Small Brick of Ore from Innothule. If you cannot find any ore in the swamp, you might be able to find some ore for sale by visiting the local merchants. Once you have found these items, combine them in your assembly kit and take the newly created material to a forge, such as the one in the Gukta Exchange, along with this mold.
        - Condition: `($text=~/gauntlets/i)`
        - Gives Mold for Froglok Gloves (38930).
      - Player: "Legplates" (link: explicit mention)
        - Prompted by player input: "Ready To Begin"
        - NPC say: In the battle for Grobb, many of our brethren fell. Their lives lost so that we may carry on Marr's Blessing. To aid in your forthcoming battles you may want to begin constructing Legplates of the Shin Initiate. Be forewarned however that they are somewhat difficult to construct. You will need to venture to the Deserts of Ro and gather a Desert Tarantula Chitin, a Giant Snake Fang, a Pristine Giant Scarab Carapace, and three Small Bricks of Ore. If you cannot locate any ore in the swamp or desert, you might be able to find some ore for sale by visiting the local merchants. Once you have found these items, combine them in your assembly kit and take the newly created material to a forge, such as the one in the Gukta Exchange, along with this mold.
        - Condition: `($text=~/legplates/i)`
        - Gives Mold for Froglok Leggings (38934).
      - Player: "Boots" (link: explicit mention)
        - Prompted by player input: "Ready To Begin"
        - NPC say: Very good. We, as paladins of Marr, have a duty to uphold Marr's teachings and be his voice to all who will listen. Though the crafting of Boots of the Shin Initiate are relatively easy to create, do not be idle in either thought or action. To craft your boots you will need to venture into the swamp and gather a few items. You will need to gather one Snake Fang, one Small Mosquito Wing, one Zombie Skin, and two Small Bricks of Ore. If you cannot locate any ore in the swamp, you might be able to find some ore for sale by visiting the local merchants. Once you have found these items, combine them in your assembly kit and take the newly created material to a forge, such as the one in the Gukta Exchange, along with this mold.
        - Condition: `($text=~/boots/i)`
        - Gives Mold for Froglok Boots (38931).
      - Player: "Final Task" (link: conversation sequence)
        - NPC say: Not all of our brethren follow the ways of The Truthbringer. In fact, a once noble paladin of our cause has decided to betray us and side with the trolls. For what reason, I do not know. His name is Fipok Glubble. There have been numerous sightings of him in the swamp. He must be stopped before he can cause any harm to our people. If you can find him, bring me his head and I will reward you.
        - Condition: `($text=~/final task/i)`
      - Player: "Prayer Bead" (link: external event mention)
        - Prompted by `event_item`:
          - NPC say: You are quite the noble Paladin $name. Take this gem and see if it fits into that set of prayer beads. If my memory is correct I believe you will find a similar gem on Odus. You should head that way to continue your journey. Be well $name.
          - Event guard: `($client->GetGlobal("paladin_epic")==9 && plugin::check_handin(\%itemcount, 17307 => 1))`
        - NPC say: This gem that you're in search for, it [will help] cure this Kemik?
        - Condition: `($client->GetGlobal("paladin_epic") ==9)`
        - Condition: `($text=~/prayer bead/i)`
      - Player: "Will Help" (link: explicit mention)
        - NPC say: Bring me a quiver of Marr and I will help your cause.
        - Condition: `($client->GetGlobal("paladin_epic") ==9)`
        - Condition: `($text=~/will help/i)`
27. Buy "Barley" (16590) from "Heidi Grainsifter" (NPC 1065) in `qeynos`. Base price: 15 copper.
28. Buy "Bottle" (16598) from "Sunsa Jocub" (NPC 1074) in `qeynos`. Base price: 4 copper.
29. Buy "Cork" (16851) from "Rylin Coil" (NPC 55027) in `akanon`. Base price: 1 copper.
30. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
    - Dialogue with erudnext/"Lumi Stergnon":
      - Player: "Hail"
        - NPC say: Peace and tranquility be with you. . Are you a [new acolyte of peace] or are you [here to pay homage] to the child of tranquility?
        - Condition: `(e.message:findi("hail"))`
      - Player: "New Acolyte Of Peace" (link: explicit mention)
        - NPC say: Then you shall learn the ways of Quellious and learn to do as you are told by higher ranking members. It is time for you to do the lesser duties of a young priest. Which will it be? [Retrieve the Peacekeeper staffs] or [battle the undead]?
        - Condition: `(e.message:findi("new acolyte of peace"))`
      - Player: "retrieve the Peacekeeper staffs" (link: explicit mention)
        - NPC say: Then take this note to the woodworker in Toxxulia Forest. His name is Emil Parsini. He shall have the staff to be returned to the temple.
        - Condition: `(e.message:findi("retrieve the Peacekeeper staffs"))`
        - Gives Sealed Letter (18833).
      - Player: "Battle The Undead" (link: explicit mention)
        - Prompted by player input: "New Acolyte Of Peace"
        - NPC say: Then you shall venture to Toxxulia Forest. There has been an increase in skeleton sightings lately. I do not know their origin, but I believe that your efforts will reduce their numbers! Take this box. Return it to me when you have filled it with the bones of these undead creatures and combined it. May Quellious' light guide you.
        - Condition: `(e.message:findi("battle the undead"))`
        - Gives Box For Bones (17941).
      - Player: "Important Missions" (link: external event mention)
        - Prompted by `event_trade`:
          - NPC say: You have done well, neophyte.Let me add the touch of harmony to finish the job.. Here, then. Take these supplies. I am sure you'll need them. Soon you may be able to assist us in [important missions].
          - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 13816}))`
        - NPC say: We have need of skilled priests. We have learned that a High Guard battle staff has been stolen. We require a priest to [track down the staff].
        - Condition: `(fac <= 4)`
        - Condition: `(e.message:findi("important missions"))`
      - Player: "Here To Pay Homage" (link: explicit mention)
        - Prompted by player input: "Hail"
        - NPC say: Then respect our temple and keep your prayers silent.
        - Condition: `(fac <= 4)`
        - Condition: `(e.message:findi("here to pay homage"))`
31. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `steamfont`.
32. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `tox`.
33. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `toxxulia`.
34. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
35. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). The combine does not fail.
36. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
    - Dialogue with qeynos/"Wolten Grafe":
      - Player: "Hail"
        - NPC say: Hail, noble . Remember to spread the words of Karana throughout the faraway lands on which you shall tread. We of the Temple of Thunder are looking for new members - good people who [wish to join our cause]. Let the call go out!
        - Condition: `(e.message:findi("hail"))`
      - Player: "Join The Cause" (link: conversation sequence)
        - NPC say: That IS good news! If you walk the righteous path of the Rainkeeper, Karana, then you are truly noble. I have need of someone like that. I must find someone to perform a [dangerous mission] or perhaps you would rather seek out the [Rat King] or [crush the undead].
        - Condition: `(e.message:findi("join the cause"))`
      - Player: "Crush The Undead" (link: explicit mention)
        - NPC say: Those who passed generations ago have had their bones exhumed and enchanted. Some evil force plagues this land with these evil skeletons. You will fight for us and crush the skeletons. Take this box and fill it with the bones of those creatures. We will not allow them to rise again and you shall earn our respect. Go forth and fight for Karana!
        - Condition: `(e.message:findi("crush the undead"))`
        - Gives Box For Bones (17941).
      - Player: "Dangerous Mission" (link: explicit mention)
        - Prompted by player input: "Join The Cause"
        - NPC say: You must go into the catacombs and find a man named Drosco Finlayer. Pass him this note. He has been deep undercover in the Shrine of Bertoxxulous and will have directions to that vile place. To do this will surely show your allegiance to this temple.
        - Condition: `(e.message:findi("dangerous mission"))`
        - Gives Tattered Note (18804).
      - Player: "Rat King" (link: explicit mention)
        - Prompted by player input: "Join The Cause"
        - NPC say: You may try, but no one has truly seen him. I would look in the sewers.
        - Condition: `(e.message:findi("rat king"))`
37. Buy "Firing Sheet" (16906) from "Winn Greenbane" (NPC 5059) in `highpass`. Base price: 10 copper.
38. Combine in Pottery Wheel (21): "Water Flask" (13006), "Block of Clay" (16901). Produces "Small Block of Clay" (16900) x3. Requires Pottery, trivial 21.
39. Combine in Pottery Wheel (21): "Small Block of Clay" (16900), "Water Flask" (13006). Produces "Block of Clay" (16901). Requires Pottery, trivial 21.
40. Combine in Pottery Wheel (21): "Block of Clay" (16901), "Water Flask" (13006). Produces "Large Block of Clay" (16902). Requires Pottery, trivial 21.
41. Buy "Large Bowl Sketch" (16963) from "Min Greyeagle" (NPC 5057) in `highpass`. Base price: 760 copper.
42. Combine in Pottery Wheel (21): "Large Block of Clay" (16902), "Water Flask" (13006), "Large Bowl Sketch" (16963). Produces "Unfired Mixing Bowl" (16930). Requires Pottery, trivial 128.
43. Combine in Kiln (22): "Firing Sheet" (16906), "Unfired Mixing Bowl" (16930). Produces "Mixing Bowl" (17906). Requires Pottery, trivial 15.
44. Buy "Celestial Solvent" (9731) from "A Goblin Bartender" (NPC 11117) in `runnyeye`. Base price: 120 copper.
45. Loot "Fetid Skin" (13150) from "A Fetid Fiend" (NPC 72059) in `fearplane`. Drop cache: 35% chance per kill.
46. Loot "Scare Straw" (13152) from "A Samhain" in `fearplane`.
47. Loot "Turmoil Warts" (8331) from "A Turmoil Toad" in `fearplane`.
48. Spawns "Grimling" (154129) in `acrylia` on event_spawn.
49. Loot "Pearl" (10024) from "Grimling".
50. Alternative: Loot "Pearl" (10024) from "Grimling" (NPC 154129) in `acrylia`; trigger: acrylia/"Raidman", on event_spawn.
51. Alternative: Loot "Pearl" (10024) from "Needs Heading Validation" (NPC 154129) in `acrylia`; trigger: acrylia/"Khati Sha The Twisted", on event_signal.
52. Alternative: Loot "Pearl" (10024) from "a Grelian firelunger" (NPC 337063) in `broodlands`; trigger: broodlands/"Grel Strongboom", on event_spawn.
53. Alternative: Loot "Pearl" (10024) from "a Grelian woundmender" (NPC 337112) in `broodlands`; trigger: broodlands/"Grel Strongboom", on event_spawn.
54. Alternative: Loot "Pearl" (10024) from "a Delve spellbinder" (NPC 341091) in `delvea`; trigger: delvea/"A Drake Egg", on event_death_complete.
55. Alternative: Loot "Pearl" (10024) from "a Delve diviner" (NPC 341085) in `delvea`; trigger: delvea/"A Drake Egg", on event_death_complete.
56. Alternative: Loot "Pearl" (10024) from "a Delve evoker" (NPC 341092) in `delvea`; trigger: delvea/"A Drake Egg", on event_death_complete.
57. Alternative: Loot "Pearl" (10024) from "a Delve drake" (NPC 341087) in `delvea`; trigger: delvea/"A Drake Egg", on event_death_complete.
58. Alternative: Loot "Pearl" (10024) from "Drake Matriarch" (NPC 341149) in `delvea`; trigger: delvea/"The Drake Menace", say "Zone Death".
59. Alternative: Loot "Pearl" (10024) from "a Delve spellbinder" (NPC 341091) in `delvea`; trigger: delvea/"Lava Rock", on event_death.
60. Alternative: Loot "Pearl" (10024) from "a Delve diviner" (NPC 341085) in `delvea`; trigger: delvea/"Lava Rock", on event_death.
61. Alternative: Loot "Pearl" (10024) from "a Delve evoker" (NPC 341092) in `delvea`; trigger: delvea/"Lava Rock", on event_death.
62. Alternative: Loot "Pearl" (10024) from "a Delve drake" (NPC 341087) in `delvea`; trigger: delvea/"Lava Rock", on event_death.
63. Alternative: Loot "Pearl" (10024) from "A Tar Goo" (NPC 119122) in `wakening`; trigger: wakening/"A Tar Goo", on event_death_complete.
64. neriaka/"X-Ta Tompi", hand "Turmoil Warts" (8331) + "Pearl" (10024) + "Fetid Skin" (13150) + "Scare Straw" (13152). Gives "Words of Acquisition (Beza)" (11866).
    - Dialogue with neriaka/"X-Ta Tompi":
      - Player: "Hail"
        - NPC say: We three are the [Sisters Dark] - [Necromancy] is our Art - Bonded dead, they serve our will - No beat of heart, yet faithful still.
        - Condition: `($text=~/hail/i)`
      - Player: "Sisters Dark" (link: explicit mention)
        - NPC say: We three are the Sisters Dark - Keepers of the shadowed Dread - [Lore of Death]. we research now - Join with us and serve [the Dead].
        - Condition: `($text=~/sisters dark/i)`
      - Player: "Lore Of Death" (link: explicit mention)
        - NPC say: The Lore of Death is shadow bound - Its [words] are [hid]. yet shall be found - Through our research into the dark - Old hexes found and parchment marked.
        - Condition: `($text=~/lore of death/i)`
      - Player: "The Dead" (link: explicit mention)
        - Prompted by player input: "Hail"
        - NPC say: The Dead are the shadowknights and necromancers of Neriak. They were formed by Queen Cristanos herself. Even among the Teir'Dal they are feared and they keep to themselves within the Lodge of the Dead in the Third Gate. I have heard they take orders only from the queen.
        - Condition: `($text=~/the dead/i)`
      - Player: "Necromancy" (link: explicit mention)
        - Prompted by player input: "Hail"
        - NPC say: Necromancy - Art of the Dead - Binding bones to serve your will - We research now the [Lore of Death] - Ancient spells with power still.
        - Condition: `($text=~/necromancy/i)`
      - Player: "Hid" (link: explicit mention)
        - Prompted by player input: "Lore Of Death"
        - NPC say: The Words are hid in tomes of old - Their yielded lore worth more than gold - Though we search both 'fore and 'hind - [Components] we can not yet find.
        - Condition: `($text=~/hid/i)`
      - Player: "Components" (link: explicit mention)
        - NPC say: We need components for research - These are things that you could find - In return for [tasks] that you perform - Words of [reward] we have in mind.
        - Condition: `($text=~/components/i)`
      - Player: "Tasks" (link: explicit mention)
        - NPC say: Bring us components for our research - We give [Word]s by tasks performed - [Possession], [Detachment], [Allure], [Haunting], [Rupturing], [Dark Paths], [Suffering], [Collection], [Obligation], [Requisition] and [Acquisition].
        - Condition: `($text=~/tasks/i)`
      - Player: "Reward" (link: explicit mention)
        - Prompted by player input: "Components"
        - NPC say: Bring us components for our research - We give [Word]s by tasks performed - [Possession], [Detachment], [Allure], [Haunting], [Rupturing], [Dark Paths], [Suffering], [Collection], [Obligation], [Requisition] and [Acquisition].
        - Condition: `($text=~/reward/i)`
      - Player: "Words Of Allure" (link: conversation sequence)
        - NPC say: From the Estate of Unrest, bring a Charred Pearl - From Castle Mistmoore, a wand charred - From a merchant bring a stone of blood and a ruby - Words of Allure will be your reward.
        - Condition: `($text=~/words of allure/i)`
      - Player: "Words Of Dark Paths" (link: conversation sequence)
        - NPC say: From the Estate of Unrest, bring an globe of darkness - From Guk, an Eye of Urd - From a merchant bring a Star Rose Quartz - Then Words of Dark Paths will to you be given.
        - Condition: `($text=~/words of dark paths/i)`
      - Player: "Words Of Acquisition" (link: conversation sequence)
        - NPC say: From the Plane of Fear, bring Fetid Skin, Scare Straw and a Turmoil Wart - From a merchant bring a pearl - Then Words of Acquisition will to you be given.
        - Condition: `($text=~/words of acquisition/i)`
      - Player: "Words Of Obligation" (link: conversation sequence)
        - NPC say: From Guk, bring an Eye of Jin - From spectres, bring a Globe of Fear - From a merchant bring a jade stone - Then Words of Obligation will to you be given.
        - Condition: `($text=~/words of obligation/i)`
      - Player: "Words Of Possession" (link: conversation sequence)
        - NPC say: The answer to that question is held by another - Ask again of my sister...
        - Condition: `($text=~/words of possession/i)`
      - Player: "Words Of Detachment" (link: conversation sequence)
        - NPC say: The answer to that question is held by another - Ask again of my sister...
        - Condition: `($text=~/words of detachment/i)`
      - Player: "Words Of Rupturing" (link: conversation sequence)
        - NPC say: The answer to that question is held by another - Ask again of my sister...
        - Condition: `($text=~/words of rupturing/i)`
      - Player: "Words Of Haunting" (link: conversation sequence)
        - NPC say: The answer to that question is held by another - Ask again of my sister...
        - Condition: `($text=~/words of haunting/i)`
      - Player: "Words Of Suffering" (link: conversation sequence)
        - NPC say: The answer to that question is held by another - Ask again of my sister...
        - Condition: `($text=~/words of suffering/i)`
      - Player: "Words Of Collection" (link: conversation sequence)
        - NPC say: The answer to that question is held by another - Ask again of my sister...
        - Condition: `($text=~/words of collection/i)`
      - Player: "Words Of Requisition" (link: conversation sequence)
        - NPC say: The answer to that question is held by another - Ask again of my sister...
        - Condition: `($text=~/words of requisition/i)`
65. Combine in "Mixing Bowl" (17906): "Celestial Solvent" (9731), "Words of Acquisition (Beza)" (11866). Produces "Celestial Essence" (9650). Requires Baking, trivial 15. The combine does not fail.
66. Combine in "Portable Drink Barrel" (17179): "Water Flask" (13006), "Celestial Essence" (9650). Produces "Purified Water" (12607). Requires Brewing, trivial 58.
67. Forage "Sand Verbena" (65582) in `taka`.
68. Forage "Sand Verbena" (65582) in `takb`.
69. Forage "Sand Verbena" (65582) in `takc`.
70. Forage "Sand Verbena" (65582) in `takd`.
71. Forage "Sand Verbena" (65582) in `take`.
72. Forage "Sand Verbena" (65582) in `takf`.
73. Forage "Sand Verbena" (65582) in `takg`.
74. Forage "Sand Verbena" (65582) in `takh`.
75. Forage "Sand Verbena" (65582) in `taki`.
76. Forage "Sand Verbena" (65582) in `takj`.
77. Combine in Brew Barrel (19): "Barley" (16590), "Bottle" (16598), "Cork" (16851), "Hops" (16591), "Purified Water" (12607), "Sand Verbena" (65582), "Yeast" (16596). Produces "Bottle of Double Brewed Double Dry Stout" (51157). Requires Brewing, trivial 226.
78. kaladimb/"Datur Nightseer", hand "Bottle of Double Brewed Double Dry Stout" (51157). Requires `paladin_epic` ==9. Gives "Kaladim Prayer Bead" (69963).
    - Dialogue with kaladimb/"Datur Nightseer":
      - Player: "Prayer Bead"
        - NPC say: You're trying to tell me that those beads in your hand are supposed to help cure someone?
        - Condition: `($client->GetGlobal("paladin_epic") ==9)`
        - Condition: `($text=~/prayer bead/i)`
      - Player: "Yes" (link: conversation sequence)
        - NPC say: Well who am I to argue with you. I'm just a holy knight of Brell! Lad, I'm feeling a little parched. Help an old knight out and run along down to a pub and get me a bottle of that double brewed double dry stout.
        - Condition: `($client->GetGlobal("paladin_epic") ==9)`
        - Condition: `($text=~/yes/i)`
79. felwithea/"General Jyleel", hand platinum:1000. Requires `paladin_epic` ==9. Gives "Felwithe Prayer Bead" (69962).
    - Dialogue with felwithea/"General Jyleel":
      - Player: "Hail" (link: external event mention)
        - Prompted by `event_trade`:
          - NPC say: 'A noble deed has been done and the alliance of evil has been stalled. I present you with the falchion of the Koada`Vie. You are now an honorable member of our order. Hail Felwithe, and may you defender her with honor.
          - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 12330,item2 = 12329,item3 = 13227}))`
        - NPC say: Stand at attention!! I am General Jyleel. of the Koada'Vie. defenders of Felwithe. Do you [follow Tunare]. the Mother of All. or do you still [seek your enlightenment]?
        - Condition: `(e.message:findi("hail"))`
      - Player: "follow Tunar" (link: conversation sequence)
        - NPC say: Then you are wise indeed. Would you like to [assist the defenders] in our conflicts or have you other business to attend to?
        - Condition: `(e.message:findi("follow Tunar"))`
      - Player: "Seek My Enlightenment" (link: explicit mention)
        - Prompted by player input: "Hail"
        - NPC say: Then seek it within these walls. We welcome all fine upstanding Koada'Dal.
        - Condition: `(e.message:findi("seek my enlightenment"))`
      - Player: "Assist The Defenders" (link: explicit mention)
        - Prompted by player input: "follow Tunar"
        - NPC say: Seek out the Crushbone orcs of the Faydarks. We must have their oracle scrolls. They are illegible to you, but we will study them here in Felwithe. Only the orc oracles will carry them, so be very careful. There is also the problem with the [Crushbone runners].
        - Condition: `(e.message:findi("assist the defenders"))`
      - Player: "Crushbone Runners" (link: explicit mention)
        - NPC say: The Crushbone orcs are sending messages across the Ocean of Tears to Antonica. Why. we do not know. The runner is usually spotted on the open pathways of Butcherblock. running toward the docks. Find him. kill him. and return his note pouch.
        - Condition: `(e.message:findi("crushbone runners"))`
      - Player: "Faithful Paladin Of This Court" (link: external event mention)
        - Prompted by `event_trade`:
          - NPC say: So, the Teir'Dal are behind the recent advances of the orcs?!! Your news has shed light on their union. It is time to step forth and prove yourself a [faithful paladin of this court].
          - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 18840}))`
        - NPC say: I command you to seek out this Ambassor DVinn and rip his heart from his lifeless body. Next, find the supreme caster of the orcs and, finally, find the spot where supplies are dropped by the Teir`Dal for the orcs. There you should find the supply crate. Return all 3 items and you shall wield the falchion.
        - Condition: `(e.message:findi("faithful paladin of this court"))`
      - Player: "Special Gem" (link: conversation sequence)
        - NPC say: I might have just the gem that you are looking for. Tunare blessed it herself! If you would make a 1000 platinum donation in the name of Tunare I will let you have it.
        - Condition: `(qglobals["paladin_epic"] == "9" and e.message:findi("special gem"))`
80. Ground spawn of "Freeport Prayer Bead" (69961) in `freeportwest`.
81. Ground spawn of "Freeport Prayer Bead" (69961) in `freportn`.
82. qeynos2/"Ziska Ironforge", hand platinum:500. Requires `paladin_epic` ==9. Gives "Qeynos Prayer Bead" (69960).
    - Dialogue with qeynos2/"Ziska Ironforge":
      - Player: "Hail"
        - NPC say: Welcome to our home of the finest jewelers in all of Norrath.
        - Condition: `(e.message:findi("hail"))`
      - Player: "Tayla" (link: conversation sequence)
        - NPC say: I know nothing.
        - Condition: `(e.message:findi("Tayla"))`
83. Combine in "Unfilled Set of Prayer Beads" (69968): "Rivervale Prayer Bead" (69967), "Ak'anon Prayer Bead" (69966), "Erudin Prayer Bead" (69965), "Gukta Prayer Bead" (69964), "Kaladim Prayer Bead" (69963), "Felwithe Prayer Bead" (69962), "Freeport Prayer Bead" (69961), "Qeynos Prayer Bead" (69960). Produces "Set of Prayer Beads" (69969). The combine does not fail.
84. dranikhollowsc/"Anetal", hand "Set of Prayer Beads" (69969). Sets `paladin_epic_hollowc` to `2`.
85. natimbi/"Kemik Arulon", say "Hail". Requires `paladin_epic_hollowc` ==2. Requires `paladin_epic` ==9. Gives "Token of Compassion" (69953).
    - Dialogue with natimbi/"Kemik Arulon":
      - Player: "Hail"
        - NPC say: ! I hear you have saved my sister Anetal! This is very good news indeed. You are truly a daring and compassionate knight. I do not have much to give you for a reward, but this might be valuable to you in your endeavors. Thank you again , and good luck to you, compassionate knight!
          - Reply guard: `(qglobals["paladin_epic_hollowc"] == "2")`
        - NPC say: Now, all that is left to be done is for you to find my sister Anetal in Discord. I have received reports that she is being held in an area called Dranik Hollows. When you are ready, bring these prayer beads with you, gather up a few of your friends, and return to me. I will see about opening up a passageway for you to find her.
          - Reply guard: `(qglobals["paladin_epic_hollowc"] == "1")`
        - NPC say: Cough, cough, hello . I apologize for my cough, my sister and I were injured badly by Muramites in Discord when some of the initial Wayfarers ventured there to explore. I luckily escaped before being mortally injured, but I lost my sister in the exodus. I have been stricken with some odd disease that appears to be eating away at me everyday, and I fear there might not be anything that can cure me. However, maybe you can try to find a cure for me. I have heard a set of prayer beads might cleanse my body of this illness, which can be found in various holy temples throughout Norrath. Curing me might be hard to do, but someone in one of those temples might be willing to help.
          - Reply guard: ``
        - Condition: `(qglobals["paladin_epic"] == "9")`
        - Condition: `(e.message:findi("hail"))`
        - Gives Token of Compassion (69953).
      - Player: "Ready" (link: explicit mention)
        - Condition: `(qglobals["paladin_epic"] == "9")`
        - Condition: `(e.message:findi("ready"))`

### "Token of Chivalry" (69954)

1. Acquisition of "Token of Compassion" (69953) is documented under "Token of Compassion" (69953); obtain another copy if needed.
2. oasis/"Paladin Epic", say "Hail". Gives "Keelee's Brooch" (69982).
3. sro/"Instructor Maerceci", hand "Keelee's Brooch" (69982). Gives "Token of Chivalry" (69954).
    - Dialogue with sro/"Instructor Maerceci":
      - Player: "Hail"
        - NPC say: ! How I am glad to see you! Something grave has [happened] to a stundent of mine, Keelee Rayin
        - Condition: `(e.other:HasItem(69953))`
        - Condition: `(e.message:findi("hail"))`
      - Player: "Happened" (link: explicit mention)
        - NPC say: Keelee was gathering a few research components for different spells that I was going to create. She had visited a few locations in Deeper Guk and then was heading to Rujarkian to gather some items there. On her way through Oasis, she was attacked by a band of Orcs. , you must save her! I am not sure where she is currently, but I would begin by searching Oasis for her. Good luck, friend.
        - Condition: `(e.other:HasItem(69953))`
        - Condition: `(e.message:findi("happened"))`

### "Token of Conviction" (69957)

1. Acquisition of "Token of Compassion" (69953) is documented under "Token of Compassion" (69953); obtain another copy if needed.
2. Acquisition of "Token of Chivalry" (69954) is documented under "Token of Chivalry" (69954); obtain another copy if needed.
3. Acquisition of "Token of Heroism" (69955) is documented under "Token of Heroism" (69955); obtain another copy if needed.
4. Acquisition of "Token of Cleansing" (69956) is documented under "Token of Heroism" (69955); obtain another copy if needed.
5. Say "Check Lorb" to anguish/"Zone Status".
6. Spawns "Orb of Discordant Energy" (317087).
7. Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy".
8. Alternative: Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy" (NPC 317087) in `anguish`; trigger: anguish/"Zone Status", say "Check Uorb".
9. Alternative: Loot "Globe of Discordant Energy" (47100) from "Ornate Chest" (NPC 317112) in `anguish`; trigger: anguish/"Zone Status", say "Check Amv Chest".
10. Alternative: Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy" (NPC 317087) in `anguish`; trigger: anguish/"Zone Status", on event_signal.
11. Alternative: Loot "Globe of Discordant Energy" (47100) from "Overlords Chest" (NPC 317124) in `anguish`; trigger: anguish/"Zone Status", on event_signal.
12. airplane/"Inte Akera", hand "Globe of Discordant Energy" (47100). Gives "Token of Conviction" (69957).

### "Token of Loyalty" (69958)

1. Acquisition of "Token of Compassion" (69953) is documented under "Token of Compassion" (69953); obtain another copy if needed.
2. Acquisition of "Token of Chivalry" (69954) is documented under "Token of Chivalry" (69954); obtain another copy if needed.
3. Acquisition of "Token of Heroism" (69955) is documented under "Token of Heroism" (69955); obtain another copy if needed.
4. Acquisition of "Token of Cleansing" (69956) is documented under "Token of Heroism" (69955); obtain another copy if needed.
5. Acquisition of "Globe of Discordant Energy" (47100) is documented under "Token of Conviction" (69957); obtain another copy if needed.
6. airplane/"Inte Akera", hand "Globe of Discordant Energy" (47100). Gives "Token of Loyalty" (69958).

### "Scabbard of the Righteous" (69959)

1. Acquisition of "Token of Compassion" (69953) is documented under "Token of Compassion" (69953); obtain another copy if needed.
2. Acquisition of "Token of Chivalry" (69954) is documented under "Token of Chivalry" (69954); obtain another copy if needed.
3. Acquisition of "Token of Heroism" (69955) is documented under "Token of Heroism" (69955); obtain another copy if needed.
4. Acquisition of "Token of Cleansing" (69956) is documented under "Token of Heroism" (69955); obtain another copy if needed.
5. Acquisition of "Globe of Discordant Energy" (47100) is documented under "Token of Conviction" (69957); obtain another copy if needed.
6. airplane/"Inte Akera", hand "Globe of Discordant Energy" (47100). Gives "Scabbard of the Righteous" (69959).

### "Dark and Twisted Sword" (69972)

1. Acquisition of "Dark and Twisted Sword" (69972) is documented under "Redemption" (64031); obtain another copy if needed.

## `paladin_epic`

Values written: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11.

1. hohonora/"Irak Altil", say "Hail". Sets `paladin_epic` to `1`.
    - Requires `paladin_epic` unset.
    - Dialogue with hohonora/"Irak Altil":
      - Player: "Hail"
        - NPC say: see you have returned with three Soulstones. These crystals are very delicate and hold the souls of those tormented beings. The keepers of these Soulstones were being controlled by some superior being, someone dark and evil in nature. I will need you to find one more Soulstone, so that we can find out who is behind all of this. This final tormented soul I feel is a Erudite...a Wayfarer Erudite, though I cannot discern where this person is. Please hurry and find this tormented being.
          - Reply guard: `(e.other:HasItem(69941) and e.other:HasItem(69952) and e.other:HasItem(69942))`
        - NPC say: Ah , it is so good to see you again. I hope my sword has been treating you well. What [brings you here], friend?
          - Reply guard: `(e.other:HasItem(10099) or e.other:HasItem(69913))`
        - Condition: `(e.message:findi("hail"))`
        - Sets `paladin_epic` to `6`.
        - Sets `paladin_epic` to `1`.
      - Player: "Brings Me Here" (link: prompt response)
        - NPC say: Yes, what is your purpose here? Perhaps you are curious as to how I've gotten here? Would you [like me to tell you]?
        - Condition: `(qglobals["paladin_epic"] == "1" and e.message:findi("brings me here"))`
      - Player: "Like You To Tell Me" (link: explicit mention)
        - NPC say: Let us start at the beginning. I, in my mortal form, was a follower of Quellious. As a young paladin, my tutors early on noticed my talents at spell-casting and my skills as a swordsman. I surpassed all of my mentor's expectations but I still had a [lot to learn].
        - Condition: `(qglobals["paladin_epic"] == "1" and e.message:findi("like you to tell me"))`
      - Player: "Lot To Learn" (link: explicit mention)
        - NPC say: My knowledge grew quickly, to the point where I could not learn anymore from my mentors. One day, I was given the choice of learning from a new master, one that rarely teaches knights. To be taught by him, I was given a series of rites that I had to pass. The path was long and difficult, but I was able to [impress my new master] and convince him to teach me.
        - Condition: `(qglobals["paladin_epic"] == "1" and e.message:findi("lot to learn"))`
      - Player: "New Master" (link: explicit mention)
        - NPC say: Oh yes, I apologize if this sounds like boasting, but my master was both impressed and surprised with my progress. He took me as his student. Years later I had gained all the knowledge I could acquire from my master and I was able to craft a great sword, the Fiery Defender. At this point in my life I decided to go on a mission to help people in need, to promote the paladin ideals to those that wished to listen, and spread the word of my Lady Quellious. However, this is not [where the story ends].
        - Condition: `(qglobals["paladin_epic"] == "1" and e.message:findi("new master"))`
      - Player: "Story Ends" (link: explicit mention)
        - NPC say: A few years after I set out on my own, I met a man named Kirak Vil. Despite being a dark elf, I welcomed him as an equal. Though I was cautious, I decided to teach him the ideals of paladins; courage, honor, truth, as well as all of the other ideals that encompass our lives. One day something [bad happened].
        - Condition: `(qglobals["paladin_epic"] == "1" and e.message:findi("story ends"))`
      - Player: "Bad Happened" (link: explicit mention)
        - NPC say: Kirak one day turned on me. We set on an expedition deep inside Old Paineel to save a kidnapped child, when a creature named a Thought Tormentor attacked us. Kirak did not help defend me and our small expedition. Last thing I remember before blacking out was a being named the Keeper of the Tombs drawing the life out of me. I [remember little after that].
        - Condition: `(qglobals["paladin_epic"] == "1" and e.message:findi("bad happened"))`
      - Player: "Remember" (link: explicit mention)
        - NPC say: I have intermittent memories of being tormented and imprisoned in the Fear plane. I was stripped of my dignity and honor, and all that was left was a shade of my former self. Most of my vivid memories of that time consisted of unbearable flashes of pain. With whatever cognitive thought that remained, I prayed to Quellious to give me strength. That is when you came to my side and [saved me].
        - Condition: `(qglobals["paladin_epic"] == "1" and e.message:findi("remember"))`
      - Player: "Saved" (link: explicit mention)
        - NPC say: Yes, by giving me the honor of wielding my sword, shield, and armor, I was set free from my torment in that wretched place. I was still not whole, however. I journeyed to many places in Norrath, looking for a place to sacrifice myself upon the spear of pain. I eventually found my way to some of the [outer Planes].
        - Condition: `(qglobals["paladin_epic"] == "1" and e.message:findi("saved"))`
      - Player: "Outer Planes" (link: explicit mention)
        - NPC say: As I stepped foot into the Plane of Tranquility, my soul began to yearn to be complete. This must have been a gift given to me by my Lady Quellious. I ventured into the Plane of Valor and this is when the Lord Mithaniel Marr found me and felt my suffering. I was summoned to the Temple of Marr and upon arrival, I was greeted and welcomed by every knight there. While I commanded respect in my former self, nothing I had ever experience was as intense as this. For the first time after the betrayal, I had felt complete. Lord Mithaniel and his priests gathered around me and chanted for three straight days. What happened next was [unbelievable].
        - Condition: `(qglobals["paladin_epic"] == "1" and e.message:findi("outer planes"))`
      - Player: "Unbelievable" (link: explicit mention)
        - NPC say: My soul and the lifeless bones that were my body began to burn like fire. It felt both painful and soothing at the same time. Energy poured out of my body and then a flash of light occurred, I passed out shortly thereafter. During my slumber, the Goddess of Love nurtured my mind and kept me company. I awoke a week later to find myself still in the Temple of Marr. The priests of Marr took care of me during my [transformation].
        - Condition: `(qglobals["paladin_epic"] == "1" and e.message:findi("unbelievable"))`
      - Player: "Transformation" (link: explicit mention)
        - NPC say: Indeed, Lord Mithaniel endowed me with this body and spoke to me, he said "My brother, while you are not a follower of Marr, I offer you a place of brotherhood here in the Halls of Honor. Your courage and perseverance are extremely commendable and I would like you to serve in my army." Honored by the ascension Lord Mithaniel had given me, I still had to take time to [consider] the offer.
        - Condition: `(qglobals["paladin_epic"] == "1" and e.message:findi("transformation"))`
      - Player: "Consider" (link: explicit mention)
        - NPC say: Yes, I was afraid my Lady Quellious would be saddened if I stayed in Mithaniel's realm. So I prayed to her and asked for guidance. My Lady appeared to me in my dreams and praised me for my loyalty. She then gave me approval to serve as a Soldier of Marr and offered me a place in her realm once my services to Lord Mithaniel were over. I was most [honored] and grateful at the same time.
        - Condition: `(qglobals["paladin_epic"] == "1" and e.message:findi("consider"))`
      - Player: "Honored" (link: explicit mention)
        - NPC say: Honored is an understatement. I was overwhelmed by the fact that the god of Valor and Honor chose me to serve in his army. I was also overwhelmed by my own god's offer to serve her after my tour was done in this plane. I try to be very humble about this honor, for that is a virtue held dear to all paladins. Now that my story is over, I [require something of you].
        - Condition: `(qglobals["paladin_epic"] == "1" and e.message:findi("honored"))`
      - Player: "Require Something" (link: explicit mention)
        - NPC say: When I ascended to this plane and was transformed, Mithaniel gave me a specific purpose. I was graced with the ability to sense others who were like me, others who were tortured and tormented. I have a sensitivity to other poor beings that have been tormented the same way as me. I would like you to find these beings who were being tortured, and perhaps that may shed some light on my past. I have had a few [visions] on what may help you find these other tormented beings.
        - Condition: `(qglobals["paladin_epic"] == "1" and e.message:findi("require something"))`
      - Player: "Visions" (link: explicit mention)
        - NPC say: I have had visions recently of various beings who have been captured by some foreign minion and tortured. The visions all were similar in nature. Very horrible things were done to these beings, very gruesome things. As the being kept fighting the pain and anguish, more torture was applied to break them...it was a horrible vision. A spell was casted mid-way though this ritual and the tormented being was held in a stasis. I felt a tugging at my soul, and I saw that the being's soul was being pulled from their body. The soul was removed from the being and imprisoned in a crystal of foreign origin. My only guess is that whoever is behind this ploy has been stealing the souls of various races of Norrath for some dark purpose. Help those that are tormented, find the crystals, and this will help you find the minions behind this plot. Go now noble Crusader!
        - Condition: `(qglobals["paladin_epic"] == "1" and e.message:findi("visions"))`
      - Player: "Tell Me About Your Master" (link: explicit mention)
        - Prompted by player input: "New Master"
        - NPC say: Yes, this was my final master, the one who rarely taught knights. You have proven yourself to be a powerful and honorable paladin, and you have surpassed anything I could teach you. You have already met my master once, a very long time ago. His name is Inte Ikera, the noblest servant of Prexus. Go to him now with Redemption in hand so that you can begin your training. Good bye and good luck, friend.
        - Condition: `(e.other:HasItem(64031) and e.message:findi("tell me about your master"))`
        - Sets `paladin_epic` to `9`.

2. qeynos2/"Enic Ruklin", say "Track Down". Sets `paladin_epic` to `2`.
    - Requires `paladin_epic` ==1.
    - Dialogue with qeynos2/"Enic Ruklin":
      - Player: "Hail"
        - NPC say: ! I'm glad you are here. Something terrible has occurred recently. Would you like to know [what happened]?
          - Reply guard: `(qglobals["paladin_epic"] == "1")`
        - NPC say: Hail! These are the sacred grounds of the Temple of Life. Please do not cause any disturbances while on our grounds. I would hate to have to hurt you. In the name of Rodcet Nife, of course. Now excuse me, I have a [problem] to attend to.
          - Reply guard: ``
        - Condition: `(e.message:findi("hail"))`
      - Player: "Problem" (link: explicit mention)
        - NPC say: I have been charged with the duty of protecting the [Pool of Jahnda] and its fish. Now it seems as though a beast by the name of [Frostbite] has slurped up another one of the sacred fish, the [Koalindl]. If I do not get the little corpse of this fish back, I could be in trouble. Any respected member of this temple who aids me will be rewarded greatly.
        - Condition: `(e.message:findi("problem"))`
      - Player: "Pool Of Jahnda" (link: explicit mention)
        - NPC say: The Pool of Jahnda is not meant for public use. It is a sacred pool created for the [Koalindl]. They say that, every so often, the Prime Healer visits our plane in the guise of a Koalindl. He swims in our pool.
        - Condition: `(e.message:findi("pool of jahnda"))`
      - Player: "Koalindl" (link: explicit mention)
        - NPC say: The fish called Koalindl were a gift to Priestess Jahnda from the Prime Healer. They come from the plane of health. To kill one Koalindl is to bring the wrath of Rodcet Nife and the Priests of Life down upon you.
        - Condition: `(e.message:findi("koalindl"))`
      - Player: "Frostbite" (link: explicit mention)
        - Prompted by player input: "Problem"
        - NPC say: Frostbite is a dog. He belongs to some barbarian who visits the city every so often. I know not where they are from. I cannot see them coming from Halas. Their visits are too frequent.
        - Condition: `(e.message:findi("frostbite"))`
      - Player: "Donate" (link: conversation sequence)
        - NPC say: I would be glad to help you out. The Knights of Thunder are a respected order.
        - Condition: `(e.message:findi("donate"))`
        - Gives Donation (13292).
      - Player: "What Happened" (link: explicit mention)
        - Prompted by player input: "Hail"
        - NPC say: A few nights ago, I was standing guard at the Pool of Jahnda like any other night, but something was different. The night air was cooler than usual and the sky was barely visible because of all of the dark clouds. Sometime around midnight, a flash occurred near the pool and I saw an Iksar run off with a Koalindl. As I chased him, he casted a portal spell and disappeared. This is grave indeed! I will need your help, . Will you help [track down] this Iksar and return the Koalindl?
        - Condition: `(qglobals["paladin_epic"] == "1" and e.message:findi("what happened"))`
      - Player: "Track Down" (link: explicit mention)
        - NPC say: Very well, . Unfortunately, I cannot offer you any hints. My only guess is that this Iksar might be near a large body of water, for the Koalindl needs to be kept near water at all times. I fear that the Koalindl may have been destroyed. Go now and find the Koalindl or the remnants of that great servant of the Prime Healer!
        - Condition: `(qglobals["paladin_epic"] == "1" and e.message:findi("track down"))`
        - Sets `paladin_epic` to `2`.

3. freporte/"Brunar Rankin", say "Hail". Sets `paladin_epic` to `3`.
    - Requires `paladin_epic` >=2.
    - Gives "Iksar's Note" (69934).
    - Dialogue with freporte/"Brunar Rankin":
      - Player: "Hail"
        - NPC say: ! Are you looking for a Koalindl? I have heard some knights such as yourself were searching for that sacred fish of Qeynos. I saw one come through here recently. An evil looking Iksar had one in some sort of stasis spell and the fish didn't look too good. Now, I'm not sure what exactly the Iksar was going to do with it, but I did see a chunk of the fish fall into the water. A few minutes later I ended up fishing up an odd looking fish scale. Immediately after I was attacked by a large and evil fish! Luckily I was carrying with me a flaying dagger and I was able to slay the evil fish before it could hurt me. Here is a note I found on the dock before the Iksar left. You must put a stop to whatever it is this Iksar is planning on doing!
          - Reply guard: `(qglobals["paladin_epic"] >= "2")`
        - NPC say: How are you? Please excuse my stench. I fish all day and night just to feed my large family. You look like an adventurer. That must be exciting. I am but a humble fisherman. Maybe someday we shall both be rich. You by your treasure and me by my catch.
          - Reply guard: ``
        - Condition: `(e.message:findi("hail"))`
        - Gives Iksar's Note (69934).
        - Sets `paladin_epic` to `3`.
      - Player: "Steal From Lenka" (link: conversation sequence)
        - NPC say: How dare you accuse me of being a thief!? I labor hour after hour trying to catch one fish which will bring me one copper piece to buy one slice of bread which I will split into five pieces to feed me, my sick wife and three little children, one of whom has the plague!! Poor little Repi. Now please, leave this humble little fisherman alone!
        - Condition: `(e.message:findi("steal from lenka"))`

4. qeynos2/"Enic Ruklin", hand "Corrupted Koalindl's Heart" (69929) + "Corrupted Koalindl's Heart" (69930) + "Corrupted Koalindl's Heart" (69931) + "Corrupted Koalindl's Heart" (69932). Sets `paladin_epic` to `4`.
    - Hand in x1: "Corrupted Koalindl's Heart" (69929).
    - Hand in x1: "Corrupted Koalindl's Heart" (69930).
    - Hand in x1: "Corrupted Koalindl's Heart" (69931).
    - Hand in x1: "Corrupted Koalindl's Heart" (69932).
    - Spawns "A Corrupted Koalindl" (69141) in `oot` on event_fish_success.
    - Loot "Corrupted Koalindl's Heart" (69929) from "A Corrupted Koalindl".
    - Spawns "A Corrupted Koalindl" (224432) in `gunthak` on event_fish_success.
    - Loot "Corrupted Koalindl's Heart" (69930) from "A Corrupted Koalindl".
    - Spawns "A Corrupted Koalindl" (93306) in `overthere` on event_fish_success.
    - Loot "Corrupted Koalindl's Heart" (69931) from "A Corrupted Koalindl".
    - Spawns "A Corrupted Koalindl" (182150) in `nedaria` on event_fish_success.
    - Loot "Corrupted Koalindl's Heart" (69932) from "A Corrupted Koalindl".
    - Gives "Seal of Enic" (69933).

5. dawnshroud/"Mikhal Young", hand "Drema's Fingerbone" (69946). Sets `paladin_epic` to `5`.
    - Requires `paladin_epic` ==4.
    - Hand in x1: "Drema's Fingerbone" (69946).
    - Prerequisite: "Drema's Fingerbone" (69946). See section 0.
    - Gives "Drema's Fingerbone" (69946).
    - Dialogue with dawnshroud/"Mikhal Young":
      - Player: "Hail"
        - NPC say: I'm so glad to find a fellow knight. Hail to you $name. I was curious, are you traveling through or could you possibly help me [try to find my sister]?
          - Reply guard: `($client->GetGlobal("paladin_epic") ==4)`
        - NPC say: Hello $name.
          - Reply guard: ``
        - Condition: `($text=~/Hail/i)`
      - Player: "Sister" (link: explicit mention)
        - NPC say: My sister Drema and I were traveling through Tenebrous Mountains after trading some supplies in Katta Castellum. We ended up setting camp in Mons Letalis for the night, so that we could have an early start on our journey back to Dawnshroud the next day. The next morning I woke up and my sister was gone! Nothing remained on her cot from the night before. . .I'm not sure where she disappeared off to. I spent the course of several days searching all of Mons Letalis for her, but I couldn't find any clues that would lead me to her where-abouts. I journeyed back to Dawnshroud Peaks and had my friends here make a rescue party so that we could find her. We set out to look for her and spent several days in Marus Seru, Mons Letalis, and the Grey looking for any sign of her. We did not [find anything].
        - Condition: `($client->GetGlobal("paladin_epic") ==4 && $text=~/sister/i)`
      - Player: "Find Anything" (link: explicit mention)
        - NPC say: As we were turning back to Dawnshroud Peaks, my good friend Ryann Desgrey found her locket in the dirt in the Grey. Here, take the locket. Perhaps you will have a better chance of finding her, and perhaps she will come with you once you present her with the locket. Please, let her know that I miss her and that we all want her to come home safely. Go now, noble paladin.
        - Condition: `($client->GetGlobal("paladin_epic") ==4 && $text=~/find anything/i)`
        - Gives Drema's Locket (69945).

6. hohonora/"Irak Altil", say "Hail". Sets `paladin_epic` to `6`.
    - Requires "Rithnok's Soulstone" (69941).
    - Requires "Drema's Soulstone" (69952).
    - Requires "Reiya's Soulstone" (69942).
    - Prerequisite: "Rithnok's Soulstone" (69941). See section 0.
    - Prerequisite: "Drema's Soulstone" (69952). See section 0.
    - Prerequisite: "Reiya's Soulstone" (69942). See section 0.

7. hohonora/"Irak Altil", hand "Dark and Twisted Sword" (69971). Sets `paladin_epic` to `7`.
    - Requires `paladin_epic` ==6.
    - Hand in x1: "Dark and Twisted Sword" (69971).
    - Spawns "Durunal the Cursebearer" (300087) in `wallofslaughter` on enter.
    - Loot "Dark and Twisted Sword" (69971) from "Durunal the Cursebearer".
    - Gives "Dark and Twisted Sword" (69972).

8. global/"Global Player", combine recipe 19880. Sets `paladin_epic` to `8`.
    - `recipe:19880` is combined in Dark and Twisted Sword (69972).
      - Prerequisite: "Dark and Twisted Sword" (69972). See section 0.
      - Put in x1: Rithnok's Soulstone (69941).
        - Prerequisite: "Rithnok's Soulstone" (69941). See section 0.
      - Put in x1: Drema's Soulstone (69952).
        - Prerequisite: "Drema's Soulstone" (69952). See section 0.
      - Put in x1: Reiya's Soulstone (69942).
        - Prerequisite: "Reiya's Soulstone" (69942). See section 0.
      - Put in x1: Redis' Soulstone (69983).
        - Loot "Redis' Soulstone" (69983) from "Shade of Redis Linrok" in `dranikcatacombsa`.
      - Produces Redemption (64031).
      - The combine does not fail.

9. hohonora/"Irak Altil", say "Tell Me About Your Master". Sets `paladin_epic` to `9`.
    - Requires "Redemption" (64031).
    - Prerequisite: "Redemption" (64031). See section 0.

10. airplane/"Inte Akera", hand "Globe of Discordant Energy" (47100). Sets `paladin_epic` to `10`.
    - Requires "Token of Compassion" (69953).
    - Requires "Token of Chivalry" (69954).
    - Requires "Token of Heroism" (69955).
    - Requires "Token of Cleansing" (69956).
    - Hand in x1: "Globe of Discordant Energy" (47100).
    - Prerequisite: "Token of Compassion" (69953). See section 0.
    - Prerequisite: "Token of Chivalry" (69954). See section 0.
    - Prerequisite: "Token of Heroism" (69955). See section 0.
    - Prerequisite: "Token of Cleansing" (69956). See section 0.
    - Say "Check Lorb" to anguish/"Zone Status".
    - Spawns "Orb of Discordant Energy" (317087).
    - Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy".
    - Alternative: Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy" (NPC 317087) in `anguish`; trigger: anguish/"Zone Status", say "Check Uorb".
    - Alternative: Loot "Globe of Discordant Energy" (47100) from "Ornate Chest" (NPC 317112) in `anguish`; trigger: anguish/"Zone Status", say "Check Amv Chest".
    - Alternative: Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy" (NPC 317087) in `anguish`; trigger: anguish/"Zone Status", on event_signal.
    - Alternative: Loot "Globe of Discordant Energy" (47100) from "Overlords Chest" (NPC 317124) in `anguish`; trigger: anguish/"Zone Status", on event_signal.
    - Gives "Token of Conviction" (69957).
    - Gives "Token of Loyalty" (69958).
    - Gives "Scabbard of the Righteous" (69959).
    - Dialogue with airplane/"Inte Akera":
      - Player: "Hail"
        - NPC say: Excellent job , I see you have acquired all four tokens. You are now ready for the final two rites: The rite of loyalty and the rite of conviction. For these final two rites, your task is simple, yet very difficult to accomplish. The main commanders in the Muramite army, found in Anguish, are set on destroying Norrath. They have already attempted once to abduct me from this plane and use me for some dark purpose, and I feel that they are doing the same to other prominent residents of Norrath. You will need to head to Anguish and defeat them and bring back proof that this has been done. Once you have completed this task, I will give you the token of loyalty and the token of conviction, for your help in defending all of Norrath. May Prexus be with you, crusader.
          - Reply guard: `(e.other:HasItem(69953) and e.other:HasItem(69954) and e.other:HasItem(69955) and e.other:HasItem(69956))`
        - NPC say: Welcome , I have been waiting for you. I see you have brought Redemption with you, which symbolizes the completion of your training with Irak. You must know that I do not train many knights, so for you to be here and receiving training is a special event. You should feel honored and proud, for not many knights will get to this point of Valor and Courage. Though, you still have a [long journey] ahead of you.
          - Reply guard: `(e.other:HasItem(64031))`
        - NPC say: Greetings, . I am Inte Akera. I have retired to the Plane of Sky after a long life toiling on Norrath's soil. Have you retreated here as well, or are you merely visiting?
          - Reply guard: ``
        - Condition: `(e.message:findi("hail"))`
      - Player: "Toil" (link: conversation sequence)
        - NPC say: Long ago, before I came to this plane, I fought in the name of Prexus against all the evils that plagued Norrath. In that time, I have done everything one can do. I have fought for the causes of good. I gained the esteem of kings and lords. The sword I hold is but one example of the treasures I have sought and won. I have accomplished all that I can, have all that I desire. My toil is done and now I sit among the clouds in peace, occasionally blessing those who seek it and are found worthy.
        - Condition: `(e.message:findi("toil"))`
      - Player: "Blessing" (link: explicit mention)
        - NPC say: Many come seeking my blessings. No matter how minor the blessing they ask, all must prove that they embody the qualities of a paladin before I bless them.
        - Condition: `(e.message:findi("blessing"))`
      - Player: "Prove Myself" (link: conversation sequence)
        - NPC say: I believe the two most important qualities of a paladin are nobility and sacrifice. Hand me an item of yours that proves you understand what nobility and sacrifice are. Be warned however, if I do not think as you do, I will simply accept the item as a gift, and give you no blessing.
        - Condition: `(e.message:findi("prove myself"))`
      - Player: "Nobility" (link: explicit mention)
        - NPC say: Ah nobility. A true measure of a paladin. If you are wondering what to bring me, then perhaps you should look within yourself. Look into your soul for a great, burning fire of nobility and you will know.
        - Condition: `(e.message:findi("nobility"))`
      - Player: "Sacrifice" (link: explicit mention)
        - Prompted by player input: "Prove Myself"
        - NPC say: Sacrifice is a virtue all paladins should strive for. The sacrifice of something dear to you will show your devotion. Perhaps something you use to smite the unholy undead.
        - Condition: `(e.message:findi("sacrifice"))`
      - Player: "Accomplish" (link: explicit mention)
        - Prompted by player input: "Hail"
        - NPC say: I accomplished many great deeds; far too many to name. I saved kings and kingdoms; I helped the weak and destitue; I accomplished all I sought to do, save one at which I failed.
        - Condition: `(e.message:findi("accomplish"))`
      - Player: "Failed" (link: explicit mention)
        - NPC say: No.. I was unable to kill my most hated foe, Miragul. The head of this wretched, foul necromancer is forever out of the reach of justice. It would be worth restoring him to his former state for the chance to take his head as a trophy.
        - Condition: `(e.message:findi("failed"))`
      - Player: "Miragul" (link: explicit mention)
        - NPC say: You think you can succeed where I cannot? Perhaps you can noble one.. Bring me the head of Miragul, his robe and hand me back the two blessings I gave you, and in return I shall bequeath to you this sword I carry. Good luck my friend.
        - Condition: `(e.message:findi("miragul"))`
      - Player: "Long Journey" (link: explicit mention)
        - Prompted by player input: "Hail"
        - NPC say: Yes, this training will be long and hard, and the risk for failure is very high. Though I have granted you the chance to train with me, that does not mean you can falter; you must be strong and dilligent. Your training will consist of four rites: The rite of compassion, the rite of chivalry, the rite of heroism, and the rite of cleansing. To complete each rite you will need to acquire a token of that rite. These tokens are very important, for they symbolize your virtues as a paladin. Once you have all four tokens, speak to me with them in hand and I will instruct you on further tasks. Good luck on your journey, knight.
        - Condition: `(e.other:HasItem(64031) and e.message:findi("long journey"))`

11. global/"Global Player", combine recipe 19925. Sets `paladin_epic` to `11`.
    - `recipe:19925` is combined in Scabbard of the Righteous (69959).
      - Prerequisite: "Scabbard of the Righteous" (69959). See section 0.
      - Put in x1: Token of Loyalty (69958).
        - Prerequisite: "Token of Loyalty" (69958). See section 0.
      - Put in x1: Token of Conviction (69957).
        - Prerequisite: "Token of Conviction" (69957). See section 0.
      - Put in x1: Token of Cleansing (69956).
        - Prerequisite: "Token of Cleansing" (69956). See section 0.
      - Put in x1: Token of Heroism (69955).
        - Prerequisite: "Token of Heroism" (69955). See section 0.
      - Put in x1: Token of Chivalry (69954).
        - Prerequisite: "Token of Chivalry" (69954). See section 0.
      - Put in x1: Token of Compassion (69953).
        - Prerequisite: "Token of Compassion" (69953). See section 0.
      - Put in x1: Redemption (64031).
        - Prerequisite: "Redemption" (64031). See section 0.
      - Produces Nightbane, Sword of the Valiant (48147).
      - The combine does not fail.

### Steps on `paladin_epic` that do not change it

- `abysmal` lovine lemise, hand 69923 needs `paladin_epic` ==5.
  - Sets `paladin_epic_reiya` to `1`.
  - Turn in Lovine's Potion Bag (69923).
- `abysmal` lovine lemise, say ingredients needs `paladin_epic` ==5.
  - Gives Lovine's Potion Bag (69922).
- `crushbone` player, on enter needs `paladin_epic` ==9.
  - Sets `paladin_epic_crushbone` to `1`.
  - Spawns Orc Messenger (58060).
  - Loots Sunshard Ore (33792).
  - Loots Orcish Battle Plans (69977).
  - Loots Steamfont Geysers (87563).
  - Loots Staurolite (97002).
- `dawnshroud` denns rootenpaw, hand 69946 needs `paladin_epic` ==5.
  - Turn in Drema's Fingerbone (69946).
  - Gives Bone Collector's Bag (69947).
- `dawnshroud` denns rootenpaw, hand 69948 needs `paladin_epic` ==5.
  - Turn in Bone Collector's Bag (69948).
  - Gives Enchanted Bone Powder (69949).
- `dawnshroud` mikhal young, say find anything needs `paladin_epic` ==4.
  - Gives Drema's Locket (69945).
- `erudnext` reklon gnallen, hand 13005+13008 needs `paladin_epic` ==9.
  - Turn in Iron Ration (13005).
  - Turn in Mead (13008).
  - Gives Erudin Prayer Bead (69965).
- `felwithea` galrun starforge, say explained needs `paladin_epic` ==9.
  - Gives Galrun's bag (69975).
- `felwithea` galrun starforge, hand 69976 needs `paladin_epic` ==9.
  - Sets `paladin_epic_mmcc` to `1`.
  - Turn in Galrun's bag (69976).
- `felwithea` general jyleel, hand platinum:1000 needs `paladin_epic` ==9.
  - Gives Felwithe Prayer Bead (69962).
- `felwithea` general jyleel, hand platinum:500 needs `paladin_epic` ==9.
- `kaladimb` datur nightseer, hand 51157 needs `paladin_epic` ==9.
  - Turn in Bottle of Double Brewed Double Dry Stout (51157).
  - Gives Kaladim Prayer Bead (69963).
- `letalis` drema young, hand 69945 needs `paladin_epic` set.
  - Turn in Drema's Locket (69945).
  - Gives Drema's Fingerbone (69946).
- `letalis` drema young, hand 69949 needs `paladin_epic` set.
  - Spawns Drema Young (169128).
  - Loots Drema's Soulstone (69928).
  - Turn in Enchanted Bone Powder (69949).
- `natimbi` kemik arulon, say hail needs `paladin_epic` ==9.
  - Gives Token of Compassion (69953).
- `ponightmare` player, on loot needs `paladin_epic` >=5.
  - Sets `paladin_epic_pon` to `1`.
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
- `qeynos2` camlend serbold, say gem needs `paladin_epic` ==9.
  - Gives Unfilled Set of Prayer Beads (69968).
- `qeynos2` ziska ironforge, hand platinum:500 needs `paladin_epic` ==9.
  - Gives Qeynos Prayer Bead (69960).
- `rathemtn` shin master grubbus, hand 17307 needs `paladin_epic` ==9.
  - Turn in Quiver of Marr (17307).
  - Gives Gukta Prayer Bead (69964).
- `rivervale` kaya cloudfoot, say different about it needs `paladin_epic` ==9.
  - Gives Note from Kaya (69970).
- `skyfire` dry sapara, say hail needs `paladin_epic` ==4.
  - Spawns Rithnok the Tormented (91193).
  - Loots Rithnok's Soulstone (69935).
- `steamfont` bigilam wantilans, hand 9181 needs `paladin_epic` ==9.
  - Turn in Mana Battery - Class Six (9181).
  - Gives Slain Vampire's Heart (69979).
- `steamfontmts` bigilam wantilans, hand 9181 needs `paladin_epic` ==9.
  - Turn in Mana Battery - Class Six (9181).
  - Gives Slain Vampire's Heart (69979).
- `vxed` player, on loot needs `paladin_epic` >=5.
  - Sets `paladin_epic_vxed` to `1`.
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
- `wallofslaughter` player, on loot needs `paladin_epic` ==6.
  - Sets `paladin_epic_wos` to `1`.
  - Spawns a chest (Epic 1.5) (283157).

## Other flags touched along the way

- `paladin_epic_crushbone` set to 1 at crushbone/player.
- `paladin_epic_ferubi` set to 1 at ferubi/player.
- `paladin_epic_hollowc` set to 1, 2 at dranikhollowsc/anetal, natimbi/kemik arulon.
- `paladin_epic_mmcc` set to 1 at felwithea/galrun starforge.
- `paladin_epic_mmcc_chest` set to 1 at mmcc/player.
- `paladin_epic_pon` set to 1 at ponightmare/player.
- `paladin_epic_reiya` set to 1 at abysmal/lovine lemise.
- `paladin_epic_vxed` set to 1 at vxed/player.
- `paladin_epic_wos` set to 1 at wallofslaughter/player.
