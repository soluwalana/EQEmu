# Paladin

Steps taken from the quest graph only. **Broken** means the graph has no edge for that value or that item.

Flags with writes: `paladin_epic`.

## 0. Prerequisites

Shared acquisition steps appear in the first prerequisite chain that needs them. Later sections reference that chain rather than repeating it.

### "Drema's Fingerbone" (69946)

1. Spawns "A Corrupted Koalindl" (69141) in `oot` on event_fish_success.
2. Loot "Corrupted Koalindl's Heart" (69929) from "A Corrupted Koalindl".
3. Spawns "A Corrupted Koalindl" (224432) in `gunthak` on event_fish_success.
4. Loot "Corrupted Koalindl's Heart" (69930) from "A Corrupted Koalindl".
5. Spawns "A Corrupted Koalindl" (93306) in `overthere` on event_fish_success.
6. Loot "Corrupted Koalindl's Heart" (69931) from "A Corrupted Koalindl".
7. Spawns "A Corrupted Koalindl" (182150) in `nedaria` on event_fish_success.
8. Loot "Corrupted Koalindl's Heart" (69932) from "A Corrupted Koalindl".
9. qeynos2/"Enic Ruklin", hand "Corrupted Koalindl's Heart" (69929) + "Corrupted Koalindl's Heart" (69930) + "Corrupted Koalindl's Heart" (69931) + "Corrupted Koalindl's Heart" (69932). Sets `paladin_epic` to `4`.
10. dawnshroud/"Mikhal Young", hand "Drema's Fingerbone" (69946). Sets `paladin_epic` to `5`.
11. dawnshroud/"Mikhal Young", say "Find Anything". Requires `paladin_epic` ==4. Gives "Drema's Locket" (69945).
12. letalis/"Drema Young", hand "Drema's Locket" (69945). Requires `paladin_epic` set. Requires `paladin_epic` >=4. Gives "Drema's Fingerbone" (69946).

### "Rithnok's Soulstone" (69941)

1. Acquisition of "Corrupted Koalindl's Heart" (69929) is documented under "Drema's Fingerbone" (69946); obtain another copy if needed.
2. Acquisition of "Corrupted Koalindl's Heart" (69930) is documented under "Drema's Fingerbone" (69946); obtain another copy if needed.
3. Acquisition of "Corrupted Koalindl's Heart" (69931) is documented under "Drema's Fingerbone" (69946); obtain another copy if needed.
4. Acquisition of "Corrupted Koalindl's Heart" (69932) is documented under "Drema's Fingerbone" (69946); obtain another copy if needed.
5. qeynos2/"Enic Ruklin", hand "Corrupted Koalindl's Heart" (69929) + "Corrupted Koalindl's Heart" (69930) + "Corrupted Koalindl's Heart" (69931) + "Corrupted Koalindl's Heart" (69932). Gives "Seal of Enic" (69933).
6. Say "Hail" to skyfire/"Dry Sapara".
7. Spawns "Rithnok the Tormented" (91193).
8. Loot "Rithnok's Soulstone" (69935) from "Rithnok the Tormented".
9. skyfire/"Dry Sapara", hand "Rithnok's Soulstone" (69935). Gives "Rithnok's Soulstone" (69936).
10. Ground spawn of "Soulstone Shard" (69937) in `draniksscar`.
11. Ground spawn of "Soulstone Shard" (69938) in `bloodfields`.
12. Ground spawn of "Soulstone Shard" (69939) in `causeway`.
13. Ground spawn of "Soulstone Shard" (69940) in `dranik`.
14. Combine in "Rithnok's Soulstone" (69936): "Soulstone Shard" (69937), "Soulstone Shard" (69938), "Soulstone Shard" (69939), "Soulstone Shard" (69940). Produces "Rithnok's Soulstone" (69941). The combine does not fail.

### "Drema's Soulstone" (69952)

1. Acquisition of "Drema's Fingerbone" (69946) is documented under "Drema's Fingerbone" (69946); obtain another copy if needed.
2. dawnshroud/"Denns Rootenpaw", hand "Drema's Fingerbone" (69946). Requires `paladin_epic` ==5. Gives "Bone Collector's Bag" (69947).
3. Loot "Dark Skeleton Remains" (69927) from "A Sun Revenant" in `thegrey`.
4. Loot "Dark Skeleton Remains" (69926) from "Disturbed Elysian Remains" (NPC 176016) in `umbral`. Drop cache: 2.58% chance per kill.
5. Loot "Dark Skeleton Remains" (69925) from "A Soriz Slave" (NPC 162029) in `ssratemple`. Drop cache: 35% chance per kill.
6. Combine in "Bone Collector's Bag" (69947): "Dark Skeleton Remains" (69927), "Dark Skeleton Remains" (69926), "Dark Skeleton Remains" (69925). Produces "Bone Collector's Bag" (69948). The combine does not fail.
7. dawnshroud/"Denns Rootenpaw", hand "Bone Collector's Bag" (69948). Requires `paladin_epic` ==5. Gives "Enchanted Bone Powder" (69949).
8. Hand "Enchanted Bone Powder" (69949) to letalis/"Drema Young". Spawns "Drema Young" (169128). Loot "Drema's Soulstone" (69928) from "Drema Young".
9. Loot "Soulstone Shard" (69950) from "Coterie Corruptor" in `tenebrous`.
10. Spawns "Shade of Mujaki the Devourer" (204081) in `ponightmare` on event death_complete:204080.
11. Loot "Soulstone Shard" (69951) from "Shade of Mujaki the Devourer".
12. Combine in "Drema's Soulstone" (69928): "Soulstone Shard" (69950), "Soulstone Shard" (69951). Produces "Drema's Soulstone" (69952). The combine does not fail.

### "Reiya's Soulstone" (69942)

1. abysmal/"Lovine Lemise", say "Ingredients". Requires `paladin_epic` ==5. Gives "Lovine's Potion Bag" (69922).
2. Loot "Ra'Tuk Screambringer's Jaw" (69921) from "A Ra'Tuk Screambringer" (NPC 283104) in `barindu`. Drop cache: 4.06% chance per kill.
3. Loot "Noc Fleshfeasters Tail" (69920) from "A Noc Fleshfeaster" in `riwwi`.
4. Loot "Mastruq Havocblade Blood" (69919) from "A Mastruq Havocblade" in `qinimi`.
5. Loot "Mastruq Havocblade Blood" (69919) from "A Mastruq Warfiend" in `qinimi`.
6. Loot "Potameid Seaweed Strands" (69918) from "An Entrapped Potameid" in `natimbi`.
7. Combine in "Lovine's Potion Bag" (69922): "Ra'Tuk Screambringer's Jaw" (69921), "Noc Fleshfeasters Tail" (69920), "Mastruq Havocblade Blood" (69919), "Potameid Seaweed Strands" (69918). Produces "Lovine's Potion Bag" (69923). The combine does not fail.
8. abysmal/"Lovine Lemise", hand "Lovine's Potion Bag" (69923). Sets `paladin_epic_reiya` to `1`.
9. Summon "Foldable Medicine Bag" (17770) by casting "Unfold Medicine Bag".
10. Common item: Fine Potion Vial (95846). Listed in 15 zones.
11. Loot "Robust Shadow Essence" (96911) from "Qua Senshali Xakra" (NPC 158020) in `vexthal`. Drop cache: 28.72% chance per kill.
12. Loot "Sage Leaf" (14215) from "a Di'zok Herbalist" in `chardok`.
13. Loot "Sage Leaf" (14215) from "a Sarnak Herb Collector" in `chardok`.
14. Loot "Sage Leaf" (14215) from "an Apprentice Herbalist" in `chardok`.
15. Loot "Valerian Root" (14230) from "a Di'zok Herbalist" in `chardok`.
16. Loot "Valerian Root" (14230) from "a Sarnak Herb Collector" in `chardok`.
17. Loot "Valerian Root" (14230) from "an Apprentice Herbalist" in `chardok`.
18. Common item: Woundwart (16526). Listed in 9 zones.
19. Combine in "Foldable Medicine Bag" (17770): "Fine Potion Vial" (95846), "Robust Shadow Essence" (96911), "Sage Leaf" (14215), "Valerian Root" (14230), "Woundwart" (16526). Produces "Mist of the Breathless" (96937). Requires Alchemy, trivial 224.
20. abysmal/"Reiya The Pained", hand "Mist of the Breathless" (96937). Requires `paladin_epic_reiya` ==1. Gives "Reiya's Soulstone" (69924).
21. Spawns "Shade of Reiya the Pained" (284104) in `ferubi` on enter.
22. Loot "Soulstone Shard" (69943) from "Shade of Reiya the Pained".
23. Loot "Soulstone Shard" (69944) from "Vuranish Xxuro" in `vxed`.
24. Combine in "Reiya's Soulstone" (69924): "Soulstone Shard" (69943), "Soulstone Shard" (69944). Produces "Reiya's Soulstone" (69942). The combine does not fail.

### "Dark and Twisted Sword" (69972)

1. Acquisition of "Rithnok's Soulstone" (69941) is documented under "Rithnok's Soulstone" (69941); obtain another copy if needed.
2. Acquisition of "Drema's Soulstone" (69952) is documented under "Drema's Soulstone" (69952); obtain another copy if needed.
3. Acquisition of "Reiya's Soulstone" (69942) is documented under "Reiya's Soulstone" (69942); obtain another copy if needed.
4. hohonora/"Irak Altil", say "Hail". Sets `paladin_epic` to `6`.
5. Loot "Redis' Soulstone" (69983) from "Shade of Redis Linrok" in `dranikcatacombsa`.
6. Spawns "Durunal the Cursebearer" (300087) in `wallofslaughter` on enter.
7. Loot "Dark and Twisted Sword" (69971) from "Durunal the Cursebearer".
8. hohonora/"Irak Altil", hand "Dark and Twisted Sword" (69971). Requires `paladin_epic` ==6. Gives "Dark and Twisted Sword" (69972).

### "Redemption" (64031)

1. Acquisition of "Dark and Twisted Sword" (69972) is documented under "Dark and Twisted Sword" (69972); obtain another copy if needed.
2. Acquisition of "Rithnok's Soulstone" (69941) is documented under "Rithnok's Soulstone" (69941); obtain another copy if needed.
3. Acquisition of "Drema's Soulstone" (69952) is documented under "Drema's Soulstone" (69952); obtain another copy if needed.
4. Acquisition of "Reiya's Soulstone" (69942) is documented under "Reiya's Soulstone" (69942); obtain another copy if needed.
5. Acquisition of "Redis' Soulstone" (69983) is documented under "Dark and Twisted Sword" (69972); obtain another copy if needed.
6. Combine in "Dark and Twisted Sword" (69972): "Rithnok's Soulstone" (69941), "Drema's Soulstone" (69952), "Reiya's Soulstone" (69942), "Redis' Soulstone" (69983). Produces "Redemption" (64031). The combine does not fail.

### "Token of Compassion" (69953)

1. Acquisition of "Redemption" (64031) is documented under "Redemption" (64031); obtain another copy if needed.
2. hohonora/"Irak Altil", say "Tell Me About Your Master". Sets `paladin_epic` to `9`.
3. qeynos2/"Camlend Serbold", say "Gem". Requires `paladin_epic` ==9. Gives "Unfilled Set of Prayer Beads" (69968).
4. rivervale/"Kaya Cloudfoot", say "Different About It". Requires `paladin_epic` ==9. Gives "Note from Kaya" (69970).
5. rivervale/"Deputy Cheel", hand "Note from Kaya" (69970). Gives "Rivervale Prayer Bead" (69967).
6. akanon/"Lewis Reldnok", say "Blessed Gem". Triggers `akanon/lewis reldnok#timer:check_sit`.
7. Sit before the NPC while its timer checks your posture.
8. akanon/"Lewis Reldnok", on timer check_sit. Gives "Ak'anon Prayer Bead" (69966).
9. erudnint/"Josper Kenshed", say "Collect Component". Gives "Empty Bag" (17944).
10. Loot "Goblin Ice Necklace" (13897) from "Redwind" in `everfrost`.
11. Loot "Goblin Ice Necklace" (13897) from "An Ice Goblin Scout" in `everfrost`.
12. Loot "Goblin Ice Necklace" (13897) from "An Ice Goblin Whelp" in `everfrost`.
13. Loot "Goblin Ice Necklace" (13897) from "An Icy Orc" in `everfrost`.
14. Loot "Goblin Ice Necklace" (13897) from "Ice Goblin Diver" in `everfrost`.
15. Combine in "Empty Bag" (17944): "Goblin Ice Necklace" (13897). Produces "Bag of Ice Necklaces" (13898). The combine does not fail.
16. halas/"Lysbith Mcnaff", hand "Bag of Ice Necklaces" (13898). Gives "Iron Ration" (13005).
17. potranquility/"Elder Fuirstel", say "Hail". Sets `pop_cod_final` to `1`.
18. poknowledge/"Aid Grimel", say "Skill In Brewing". Requires `pop_cod_final` ==1. Requires `pop_cod_final` set. Gives "Portable Drink Barrel" (17179).
19. Loot "Cask" (16580) from "Tugog Grigol" in `rathemtn`.
20. Common item: Hops (16591). Listed in 31 zones.
21. Common item: Malt (16595). Listed in 30 zones.
22. Common item: Yeast (16596). Listed in 30 zones.
23. Combine in "Portable Drink Barrel" (17179): "Cask" (16580), "Hops" (16591), "Malt" (16595), "Yeast" (16596). Produces "Mead" (13008). Requires Brewing, trivial 41.
24. erudnext/"Reklon Gnallen", hand "Iron Ration" (13005) + "Mead" (13008). Requires `paladin_epic` ==9. Gives "Erudin Prayer Bead" (69965).
25. Summon "Quiver of Marr" (17307) by casting "Quiver of Marr".
26. rathemtn/"Shin Master Grubbus", hand "Quiver of Marr" (17307). Requires `paladin_epic` ==9. Gives "Gukta Prayer Bead" (69964).
27. Common item: Barley (16590). Listed in 28 zones.
28. Common item: Bottle (16598). Listed in 70 zones.
29. Common item: Cork (16851). Listed in 12 zones.
30. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
31. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `steamfont`.
32. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `tox`.
33. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `toxxulia`.
34. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
35. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). The combine does not fail.
36. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
37. Common item: Firing Sheet (16906). Listed in 34 zones.
38. Combine in Pottery Wheel (21): "Water Flask" (13006), "Block of Clay" (16901). Produces "Small Block of Clay" (16900) x3. Requires Pottery, trivial 21.
39. Combine in Pottery Wheel (21): "Small Block of Clay" (16900), "Water Flask" (13006). Produces "Block of Clay" (16901). Requires Pottery, trivial 21.
40. Combine in Pottery Wheel (21): "Block of Clay" (16901), "Water Flask" (13006). Produces "Large Block of Clay" (16902). Requires Pottery, trivial 21.
41. Common item: Large Bowl Sketch (16963). Listed in 29 zones.
42. Combine in Pottery Wheel (21): "Large Block of Clay" (16902), "Water Flask" (13006), "Large Bowl Sketch" (16963). Produces "Unfired Mixing Bowl" (16930). Requires Pottery, trivial 128.
43. Combine in Kiln (22): "Firing Sheet" (16906), "Unfired Mixing Bowl" (16930). Produces "Mixing Bowl" (17906). Requires Pottery, trivial 15.
44. Common item: Celestial Solvent (9731). Listed in 13 zones.
45. Loot "Fetid Skin" (13150) from "A Fetid Fiend" (NPC 72059) in `fearplane`. Drop cache: 35% chance per kill.
46. Loot "Scare Straw" (13152) from "A Samhain" in `fearplane`.
47. Loot "Turmoil Warts" (8331) from "A Turmoil Toad" in `fearplane`.
48. Spawns "Grimling" (154129) in `acrylia` on event_spawn.
49. Loot "Pearl" (10024) from "Grimling".
50. 14 alternative loot source(s) also yield Pearl (10024).
51. neriaka/"X-Ta Tompi", hand "Turmoil Warts" (8331) + "Pearl" (10024) + "Fetid Skin" (13150) + "Scare Straw" (13152). Gives "Words of Acquisition (Beza)" (11866).
52. Combine in "Mixing Bowl" (17906): "Celestial Solvent" (9731), "Words of Acquisition (Beza)" (11866). Produces "Celestial Essence" (9650). Requires Baking, trivial 15. The combine does not fail.
53. Combine in "Portable Drink Barrel" (17179): "Water Flask" (13006), "Celestial Essence" (9650). Produces "Purified Water" (12607). Requires Brewing, trivial 58.
54. Forage "Sand Verbena" (65582) in `taka`.
55. Forage "Sand Verbena" (65582) in `takb`.
56. Forage "Sand Verbena" (65582) in `takc`.
57. Forage "Sand Verbena" (65582) in `takd`.
58. Forage "Sand Verbena" (65582) in `take`.
59. Forage "Sand Verbena" (65582) in `takf`.
60. Forage "Sand Verbena" (65582) in `takg`.
61. Forage "Sand Verbena" (65582) in `takh`.
62. Forage "Sand Verbena" (65582) in `taki`.
63. Forage "Sand Verbena" (65582) in `takj`.
64. Combine in Brew Barrel (19): "Barley" (16590), "Bottle" (16598), "Cork" (16851), "Hops" (16591), "Purified Water" (12607), "Sand Verbena" (65582), "Yeast" (16596). Produces "Bottle of Double Brewed Double Dry Stout" (51157). Requires Brewing, trivial 226.
65. kaladimb/"Datur Nightseer", hand "Bottle of Double Brewed Double Dry Stout" (51157). Requires `paladin_epic` ==9. Gives "Kaladim Prayer Bead" (69963).
66. felwithea/"General Jyleel", hand platinum:1000. Requires `paladin_epic` ==9. Gives "Felwithe Prayer Bead" (69962).
67. Ground spawn of "Freeport Prayer Bead" (69961) in `freeportwest`.
68. Ground spawn of "Freeport Prayer Bead" (69961) in `freportn`.
69. qeynos2/"Ziska Ironforge", hand platinum:500. Requires `paladin_epic` ==9. Gives "Qeynos Prayer Bead" (69960).
70. Combine in "Unfilled Set of Prayer Beads" (69968): "Rivervale Prayer Bead" (69967), "Ak'anon Prayer Bead" (69966), "Erudin Prayer Bead" (69965), "Gukta Prayer Bead" (69964), "Kaladim Prayer Bead" (69963), "Felwithe Prayer Bead" (69962), "Freeport Prayer Bead" (69961), "Qeynos Prayer Bead" (69960). Produces "Set of Prayer Beads" (69969). The combine does not fail.
71. dranikhollowsc/"Anetal", hand "Set of Prayer Beads" (69969). Sets `paladin_epic_hollowc` to `2`.
72. natimbi/"Kemik Arulon", say "Hail". Requires `paladin_epic_hollowc` ==2. Requires `paladin_epic` ==9. Gives "Token of Compassion" (69953).

### "Token of Chivalry" (69954)

1. Acquisition of "Token of Compassion" (69953) is documented under "Token of Compassion" (69953); obtain another copy if needed.
2. oasis/"Paladin Epic", say "Hail". Gives "Keelee's Brooch" (69982).
3. sro/"Instructor Maerceci", hand "Keelee's Brooch" (69982). Gives "Token of Chivalry" (69954).

### "Token of Heroism" (69955)

1. Loot "Valdoon Kel'Novar's Heart" (69981) from "Valdoon Kel'Novar" in `mmcc`.
2. felwithea/"Galrun Starforge", hand "Valdoon Kel'Novar's Heart" (69981). Gives "Token of Cleansing" (69956).
3. provinggrounds/"Pashia Clouddancer", say "Note". Gives "Note from Pashia" (69973).
4. nedaria/"Duram Firechaser", hand "Note from Pashia" (69973). Gives "Token of Heroism" (69955).

### "Token of Cleansing" (69956)

1. Acquisition of "Token of Cleansing" (69956) is documented under "Token of Heroism" (69955); obtain another copy if needed.

### "Scabbard of the Righteous" (69959)

1. Acquisition of "Token of Compassion" (69953) is documented under "Token of Compassion" (69953); obtain another copy if needed.
2. Acquisition of "Token of Chivalry" (69954) is documented under "Token of Chivalry" (69954); obtain another copy if needed.
3. Acquisition of "Token of Heroism" (69955) is documented under "Token of Heroism" (69955); obtain another copy if needed.
4. Acquisition of "Token of Cleansing" (69956) is documented under "Token of Heroism" (69955); obtain another copy if needed.
5. Say "Check Lorb" to anguish/"Zone Status".
6. Spawns "Orb of Discordant Energy" (317087).
7. Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy".
8. 4 alternative loot source(s) also yield Globe of Discordant Energy (47100).
9. airplane/"Inte Akera", hand "Globe of Discordant Energy" (47100). Gives "Scabbard of the Righteous" (69959).

### "Token of Loyalty" (69958)

1. Acquisition of "Token of Compassion" (69953) is documented under "Token of Compassion" (69953); obtain another copy if needed.
2. Acquisition of "Token of Chivalry" (69954) is documented under "Token of Chivalry" (69954); obtain another copy if needed.
3. Acquisition of "Token of Heroism" (69955) is documented under "Token of Heroism" (69955); obtain another copy if needed.
4. Acquisition of "Token of Cleansing" (69956) is documented under "Token of Heroism" (69955); obtain another copy if needed.
5. Acquisition of "Globe of Discordant Energy" (47100) is documented under "Scabbard of the Righteous" (69959); obtain another copy if needed.
6. airplane/"Inte Akera", hand "Globe of Discordant Energy" (47100). Gives "Token of Loyalty" (69958).

### "Token of Conviction" (69957)

1. Acquisition of "Token of Compassion" (69953) is documented under "Token of Compassion" (69953); obtain another copy if needed.
2. Acquisition of "Token of Chivalry" (69954) is documented under "Token of Chivalry" (69954); obtain another copy if needed.
3. Acquisition of "Token of Heroism" (69955) is documented under "Token of Heroism" (69955); obtain another copy if needed.
4. Acquisition of "Token of Cleansing" (69956) is documented under "Token of Heroism" (69955); obtain another copy if needed.
5. Acquisition of "Globe of Discordant Energy" (47100) is documented under "Scabbard of the Righteous" (69959); obtain another copy if needed.
6. airplane/"Inte Akera", hand "Globe of Discordant Energy" (47100). Gives "Token of Conviction" (69957).

## `paladin_epic`

Values written: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11.

### 1. irak altil — say hail

Zone: `hohonora`.

> Ah

Sets `paladin_epic` to `1`.

- Needs `paladin_epic` unset.
In script order:

1. Sets `paladin_epic` to `1`.


### 2. enic ruklin — say track down

Zone: `qeynos2`.

> Very well,

Sets `paladin_epic` to `2`.

- Needs `paladin_epic` ==1.
In script order:

1. Sets `paladin_epic` to `2`.


### 3. brunar rankin — say hail

Zone: `freporte`.

> How are you? Please excuse my stench. I fish all day and night just to feed my large family. You look like an adventurer. That must be exciting. I am but a h...

Sets `paladin_epic` to `3`.

- Needs `paladin_epic` >=2.
In script order:

1. Sets `paladin_epic` to `3`.
2. Gives Iksar's Note (69934).


### 4. enic ruklin — hand 69929+69930+69931+69932

Zone: `qeynos2`.

Sets `paladin_epic` to `4`.

- Turn in x1: Corrupted Koalindl's Heart (69929).
- Turn in x1: Corrupted Koalindl's Heart (69930).
- Turn in x1: Corrupted Koalindl's Heart (69931).
- Turn in x1: Corrupted Koalindl's Heart (69932).
In script order:

1. Sets `paladin_epic` to `4`.
2. Gives Seal of Enic (69933).


How the items are reached:

- Corrupted Koalindl's Heart (69929)
  - Spawns "A Corrupted Koalindl" (69141) in `oot` on event_fish_success.
  - Loot "Corrupted Koalindl's Heart" (69929) from "A Corrupted Koalindl".
- Corrupted Koalindl's Heart (69930)
  - Spawns "A Corrupted Koalindl" (224432) in `gunthak` on event_fish_success.
  - Loot "Corrupted Koalindl's Heart" (69930) from "A Corrupted Koalindl".
- Corrupted Koalindl's Heart (69931)
  - Spawns "A Corrupted Koalindl" (93306) in `overthere` on event_fish_success.
  - Loot "Corrupted Koalindl's Heart" (69931) from "A Corrupted Koalindl".
- Corrupted Koalindl's Heart (69932)
  - Spawns "A Corrupted Koalindl" (182150) in `nedaria` on event_fish_success.
  - Loot "Corrupted Koalindl's Heart" (69932) from "A Corrupted Koalindl".

### 5. mikhal young — hand 69946

Zone: `dawnshroud`.

Sets `paladin_epic` to `5`.

- Needs `paladin_epic` ==4.
- Turn in x1: Drema's Fingerbone (69946).
In script order:

1. Sets `paladin_epic` to `5`.
2. Gives Drema's Fingerbone (69946).


How the items are reached:

- Drema's Fingerbone (69946)
  - Prerequisite: "Drema's Fingerbone" (69946). See section 0.

### 6. irak altil — say hail

Zone: `hohonora`.

> Ah

Sets `paladin_epic` to `6`.

- Needs Rithnok's Soulstone (69941).
- Needs Drema's Soulstone (69952).
- Needs Reiya's Soulstone (69942).
In script order:

1. Sets `paladin_epic` to `6`.


How the items are reached:

- Rithnok's Soulstone (69941)
  - Prerequisite: "Rithnok's Soulstone" (69941). See section 0.
- Drema's Soulstone (69952)
  - Prerequisite: "Drema's Soulstone" (69952). See section 0.
- Reiya's Soulstone (69942)
  - Prerequisite: "Reiya's Soulstone" (69942). See section 0.

### 7. irak altil — hand 69971

Zone: `hohonora`.

Sets `paladin_epic` to `7`.

- Needs `paladin_epic` ==6.
- Turn in x1: Dark and Twisted Sword (69971).
In script order:

1. Sets `paladin_epic` to `7`.
2. Gives Dark and Twisted Sword (69972).


How the items are reached:

- Dark and Twisted Sword (69971)
  - Spawns "Durunal the Cursebearer" (300087) in `wallofslaughter` on enter.
  - Loot "Dark and Twisted Sword" (69971) from "Durunal the Cursebearer".

### 8. global player — combine recipe 19880

Zone: `global`.

Sets `paladin_epic` to `8`.

In script order:

1. Sets `paladin_epic` to `8`.


Combine:

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

### 9. irak altil — say tell me about your master

Zone: `hohonora`.

> Yes, this was my final master, the one who rarely taught knights. You have proven yourself to be a powerful and honorable paladin, and you have surpassed any...

Sets `paladin_epic` to `9`.

- Needs Redemption (64031).
In script order:

1. Sets `paladin_epic` to `9`.


How the items are reached:

- Redemption (64031)
  - Prerequisite: "Redemption" (64031). See section 0.

### 10. inte akera — hand 47100

Zone: `airplane`.

Sets `paladin_epic` to `10`.

- Needs Token of Compassion (69953).
- Needs Token of Chivalry (69954).
- Needs Token of Heroism (69955).
- Needs Token of Cleansing (69956).
- Turn in x1: Globe of Discordant Energy (47100).
In script order:

1. Sets `paladin_epic` to `10`.
2. Gives Token of Conviction (69957).
3. Gives Token of Loyalty (69958).
4. Gives Scabbard of the Righteous (69959).


How the items are reached:

- Token of Compassion (69953)
  - Prerequisite: "Token of Compassion" (69953). See section 0.
- Token of Chivalry (69954)
  - Prerequisite: "Token of Chivalry" (69954). See section 0.
- Token of Heroism (69955)
  - Prerequisite: "Token of Heroism" (69955). See section 0.
- Token of Cleansing (69956)
  - Prerequisite: "Token of Cleansing" (69956). See section 0.
- Globe of Discordant Energy (47100)
  - Say "Check Lorb" to anguish/"Zone Status".
  - Spawns "Orb of Discordant Energy" (317087).
  - Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy".
  - 4 alternative loot source(s) also yield Globe of Discordant Energy (47100).

### 11. global player — combine recipe 19925

Zone: `global`.

Sets `paladin_epic` to `11`.

In script order:

1. Sets `paladin_epic` to `11`.


Combine:

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
