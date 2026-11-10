# Druid

Acquisition paths traced backwards from the 1.0, 1.5 and 2.0 epic rewards. Flags are dependencies, not the definition of an epic. **Broken** indicates missing graph provenance.

## Epic 1.0

### "Nature Walkers Scimitar" (20490)

1. **Unresolved introduction:** no connected introductory hail in the graph.
2. Loot "Froglok Essence" (20696) from "Ulump Pujluk" in `swampofnohope`.
3. Kill emeraldjungle/"Tainted Gorilla". Spawns "Corrupted Gorilla" (94140).
4. Loot "Green Tree Bark" (20686) from "Corrupted Gorilla".
5. Kill lakeofillomen/"Tainted Barracuda". Spawns "Corrupted Barracuda" (85224).
6. Loot "Pure Lakewater" (20685) from "Corrupted Barracuda".
7. Hand "Froglok Essence" (20696) to timorous/"Dolgin Codslayer". Spawns "Faydedar" (96073). Loot "Pod of Seawater" (20687) from "Faydedar".
8. overthere/"Nekexin Virulence", hand "Pure Lakewater" (20685) + "Green Tree Bark" (20686) + "Pod of Seawater" (20687) + "Froglok Essence" (20696). Gives "Cleansed Spirit of Kunark" (20699).
9. Kill kedge/"Tainted Seahorse". Spawns "Corrupted Seahorse" (64050).
10. Loot "Kedge Cave Crystals" (20691) from "Corrupted Seahorse".
11. Kill oceanoftears/"Tainted Seafury Cyclops". Spawns "Corrupted Seafury Cyclops" (69142).
12. Loot "Ocean of Tears Seavines" (20692) from "Corrupted Seafury Cyclops".
13. Alternative: Loot "Ocean of Tears Seavines" (20692) from "Corrupted Seafury Cyclops" (NPC 69142) in `oot`; trigger: oot/"Tainted Seafury Cyclops", on event_death_complete.
14. Kill lfaydark/"Tainted Brownie". Spawns "Corrupted Brownie" (57117).
15. Loot "Green Heartwood Branch" (20693) from "Corrupted Brownie".
16. lfaydark/"Pained Unicorn", hand "Kedge Cave Crystals" (20691) + "Ocean of Tears Seavines" (20692) + "Green Heartwood Branch" (20693). Gives "Gleaming Unicorn Horn" (20694).
17. akanon/"Silox Azrix", hand "Gleaming Unicorn Horn" (20694). Gives "Cleansed Spirit of Faydwer" (20697).
18. Loot "Ring of the Ancients" (12268) from "The Fabled Ancient Cyclops" in `sro`.
19. Loot "Ring of the Ancients" (12268) from "An Ancient Cyclops".
20. Loot "Ring of the Ancients" (12268) from "An Ancient Cyclops" in `oot`.
21. Loot "Ring of the Ancients" (12268) from "An Ancient Cyclops" in `sro`.
22. Kill rathemtn/"Ytyrs The Reborn". Spawns "Ytyrs Reborn" (50346).
23. Loot "Shadowed Rapier" (7100) from "Ytyrs Reborn".
24. rathemtn/"Hasten Bootstrutter", hand "Shadowed Rapier" (7100) + "Ring of the Ancients" (12268). Gives "Journeyman's Boots" (2300).
25. northkarana/"Triathalon Token", hand "Journeyman's Boots" (2300). Gives "Warm Pulsing Treant Heart" (20695).
26. southkarana/"Yeka Ias", hand "Warm Pulsing Treant Heart" (20695). Gives "Cleansed Spirit of Antonica" (20698).
27. burningwood/"Telin Darkforest", say "Action". Gives "Worn Note" (20472).
28. gfaydark/"Faelin Bloodbriar", hand "Worn Note" (20472). Gives "Faelin's Ring" (20446).
29. kithicor/"Giz X-Tin", hand "Faelin's Ring" (20446). Gives "Dark Metal Coin" (20447).
30. burningwood/"Telin Darkforest", hand "Dark Metal Coin" (20447). Gives "Worn Dark Metal Coin" (20448).
31. eastkarana/"Althele", hand "Worn Dark Metal Coin" (20448). Gives "Braided Grass Amulet" (20450).
    - Dialogue with eastkarana/"Althele":
      - Player: "Hail"
        - NPC say: Hello, friend. Beautiful is what I would call such a day normally, but lately? I sense that something is [out of balance].
          - Reply guard: `($class eq "Ranger" && (plugin::check_hasitem($client, 20488) || plugin::check_hasitem($client, 62600)))`
        - Condition: `($text=~/hail/i)`
        - Sets `ranger_epic` to `1`.
      - Player: "Your Eyes" (link: conversation sequence)
        - NPC say: Yes. I cannot see any longer, my sight long since lost in the march of years. By the blessings of Tunare and Karana, though, I still make myself useful.
        - Condition: `($text=~/your eyes/i)`
      - Player: "Out Of Balance" (link: explicit mention)
        - Prompted by player input: "Hail"
        - NPC say: I don't know for certain what is wrong. It feels like the start of a cold, a sort of tickling at the back of Norrath's throat, if I may make such a poor metaphor. In much the same way that I can sense that you have wielded the power of nature, probably in the form of the weapons known as Swiftwind and Earthcaller, I can sense a power of illness creeping upon the land. Please, if you come across anything suspicious bring it to me. I am worried, this does not feel like a natural sickness to me. Go with the blessing of the Mother and the speed of the Storm, my child.
          - Reply guard: `($class eq "Ranger" && $client->GetGlobal("ranger_epic") ==1)`
        - NPC say: I am certain that you would sense it too, had you been so blessed as to be without sight. My sense of the life of Norrath is greatly heightened without the hindrance of vision. As I can sense that you have at your call the power of the lands, perhaps in the form of the Nature Walkers Scimitar. I can feel an unnatural illness creeping about the edges of Norrath. Please, if you come across anything suspicious bring it to me. I am worried about this cold sickness that I can almost taste. Go with the blessing of the Mother and the speed of the Storm, my child.
          - Reply guard: `($class eq "Druid" && plugin::check_hasitem($client, 20490) or plugin::check_hasitem($client, 62809))`
        - NPC say: I sense something foreboding, young one, but you should think nothing of it. The sons and daughters of nature will be able to deal with this problem.
          - Reply guard: ``
        - Condition: `($text=~/out of balance/i)`
        - Sets `druid_epic` to `1`.
32. eastkarana/"Sionae", hand "Braided Grass Amulet" (20450). Gives "Frayed Braided Grass Amulet" (20451).
33. eastkarana/"Teloa", hand "Frayed Braided Grass Amulet" (20451). Triggers `eastkarana/althele#signal:1`.
34. Starts timer `attack`.
35. Spawns "Corruptor" (15153) after `eastkarana/althele#timer:attack`.
36. Loot "Fleshbound Tome" (20452) from "Corruptor".
37. eastkarana/"Althele", hand "Fleshbound Tome" (20452). Gives "Earth Stained Note" (18959).
38. misty/"Ella Foodcrafter", hand "Earth Stained Note" (18959). Sets `shiny_tin_bowl` to `1`.
39. misty/"Ella Foodcrafter", say "Two Tasks". Requires `shiny_tin_bowl` set. Gives "Shiny Tin Bowl" (17860).
40. Forage "Ripened Heartfruit" (20464) in `gfaydark`.
41. Forage "Sweetened Mudroot" (20465) in `misty`.
42. Forage "Sweetened Mudroot" (20465) in `mistythicket`.
43. Forage "Speckled Molded Mushroom" (20466) in `innothule`.
44. Forage "Chilled Tundra Root" (20467) in `everfrost`.
45. Combine in "Shiny Tin Bowl" (17860): "Ripened Heartfruit" (20464), "Sweetened Mudroot" (20465), "Speckled Molded Mushroom" (20466), "Chilled Tundra Root" (20467). Produces "Hardened Mixture" (20473). Requires Pottery. The combine does not fail.
46. timorous/"Alrik Farsight", say "Take The Artifact". Gives "Crushed Pot" (20457).
47. felwitheb/"Farios Elianos", hand "Crushed Pot" (20457). Gives "Grocery List" (20458).
48. felwithea/"Merchant Nora", hand "Grocery List" (20458). Gives "Bag of Provisions" (20459).
49. felwitheb/"Farios Elianos", hand "Bag of Provisions" (20459). Gives "Receipt" (20474).
50. timorous/"Alrik Farsight", hand "Receipt" (20474). Gives "Ancient Pattern" (18960).
51. Kill citymist/"A Black Reaver". Spawns "A Black Reaver" (90004).
52. Loot "Jade Reaver" (5664) from "A Black Reaver".
53. Alternative: Loot "Jade Reaver" (5664) from "A Black Reaver" (NPC 90005) in `citymist`; trigger: citymist/"A Black Reaver", on event_death_complete.
54. Alternative: Loot "Jade Reaver" (5664) from "A Black Reaver" (NPC 90192) in `citymist`; trigger: citymist/"A Black Reaver", on event_death_complete.
55. kaladimb/"Kinlo Strongarm", hand "Jade Reaver" (5664). Gives "Enchanted Clay" (20455).
56. Forage "Rose of Firiona" (12774) in `firiona`.
57. qrg/"Merdan Fleetfoot", hand "Rose of Firiona" (12774). Gives "Wood Painting" (20475).
58. frontiermtns/"A Human Skeleton", hand "Wood Painting" (20475). Gives "Silver Chained Locket" (20476).
59. qrg/"Niera Farbreeze", hand "Silver Chained Locket" (20476). Gives "Platinum Speckled Powder" (20456).
60. Combine in Pottery Wheel (21): "Ancient Pattern" (18960), "Enchanted Clay" (20455), "Platinum Speckled Powder" (20456). Produces "Runecrested Bowl" (20460). Requires Pottery. The combine does not fail.
61. misty/"Ella Foodcrafter", hand "Runecrested Bowl" (20460) + "Hardened Mixture" (20473). Gives "Softly Glowing Stone" (20462).
62. Buy "Spell: Resurrection" (15392) from "Henlom Visrek" (NPC 2054) in `qeynos2`. Base price: 18,936 copper.
63. Hand "Spell: Resurrection" (15392) to karnor/"Spirit Of Venril Sathir". Spawns "Venril Sathir" (102126). Loot "Pulsing Green Stone" (20461) from "Venril Sathir".
64. firiona/"Foloal Stormforest", hand "Pulsing Green Stone" (20461) + "Softly Glowing Stone" (20462). Gives "Warmly Glowing Stone" (20468).
65. misty/"Ella Foodcrafter", hand "Warmly Glowing Stone" (20468). Gives "Elaborate Scimitar" (20440).
66. northkarana/"Xanuusus", hand "Elaborate Scimitar" (20440) + "Cleansed Spirit of Faydwer" (20697) + "Cleansed Spirit of Antonica" (20698) + "Cleansed Spirit of Kunark" (20699). Gives "Nature Walkers Scimitar" (20490).
    - Dialogue with northkarana/"Xanuusus":
      - Player: "Hail"
        - NPC say: I see you have purified that stone. Can I look at it?
          - Reply guard: `( e.other:HasItem(62604) )`
        - NPC say: You make my limbs ache. There is something unnatural about you. What is it?
          - Reply guard: `( qglobals["ranger_epic15_pre"] == "6" )`
        - NPC say: Greetings, small one! I am Xanuusus of the Stormreapers. You are welcome to rest beneath my mighty branches.
          - Reply guard: ``
        - Condition: `(e.message:findi("hail"))`
        - Gives Polished Blasted Stone (62603).
      - Player: "Help"
        - NPC say: Well, I suppose I can help you a little, small one. There are three principles expressed in my lovely poem.
        - NPC say: First one must defeat a worthy enemy of the Storm Lord, as you obviously understood from the second stanza. Seek a weapon born by one that would shackle the world if he could. He takes his name from his home, as if to claim it as his own.
        - NPC say: Secondly one must aid a friend of the Storm Lord. There is one that considers himself small and worthless. Heal his heart so that his bare feet may roam again.
        - NPC say: Finally one must perform and act of faith in the Storm Lord. When you have accomplished the other tasks, return to me and we shall again speak of this act of faith.
        - Condition: `( qglobals["ranger_epic15_pre"] == "7" and e.message:findi("help") )`
      - Player: "Ready" (link: conversation sequence)
        - NPC say: Stay close or this won't work. It is better that you do this, for trees are not very well structured to withstand lightning.
          - Reply guard: `( e.other:HasItem(62631) and e.other:HasItem(62633) and e.other:HasItem(62603) )`
          - Reply guard: `( client:GetItemIDAt(Slot.Face) == 62603 and client:GetItemIDAt(Slot.Primary) == 62633 and client:GetItemIDAt(Slot.Secondary) == 62631 )`
        - NPC emote: The treant releases a sound from his hollows that sounds much like thunder.
          - Reply guard: `( e.other:HasItem(62631) and e.other:HasItem(62633) and e.other:HasItem(62603) )`
          - Reply guard: `( client:GetItemIDAt(Slot.Face) == 62603 and client:GetItemIDAt(Slot.Primary) == 62633 and client:GetItemIDAt(Slot.Secondary) == 62631 )`
        - Condition: `( qglobals["ranger_epic15_pre"] == "8" and e.message:findi("ready") )`

## Epic 1.5

### "Staff of Living Brambles" (62863)

1. **Unresolved introduction:** no connected introductory hail in the graph.
2. Loot "Crystal Fragment" (62852) from "Finnelzi Springworthy" in `southkarana`.
3. Loot "Crystal Fragment" (62852) from "Rendolf Deathbringer" in `southkarana`.
4. Loot "Crystal Fragment" (62852) from "Tehana Elsent" in `southkarana`.
5. freportw/"Shana Liskia", hand "Crystal Fragment" (62852) + "Crystal Fragment" (62852) + "Crystal Fragment" (62852). Gives "Small Padded Bag" (62853).
6. freportw/"Shana Liskia", hand "Crystal Fragment" (62852) + "Crystal Fragment" (62852) + "Crystal Fragment" (62852). Sets `druid_epic` to `5`.
7. Spawns "Azibelle Spavin" (335064) in `harbingers` on enter.
8. Loot "Bohab's Crystal Fragment" (62886) from "Azibelle Spavin".
9. Spawns "Azibelle Spavin" (335064) in `harbingers` on enter.
10. Loot "Azibelle's Crystal Fragment" (62887) from "Azibelle Spavin".
11. Spawns "Glenfire Telzir" (335065) in `harbingers` on enter.
12. Loot "Glenfire's Crystal Fragment" (62888) from "Glenfire Telzir".
13. Combine in "Small Padded Bag" (62853): "Bohab's Crystal Fragment" (62886), "Azibelle's Crystal Fragment" (62887), "Glenfire's Crystal Fragment" (62888), "Crystal Fragment" (62852). Produces "Full Padded Bag" (62854). The combine does not fail.
14. freportw/"Shana Liskia", hand "Full Padded Bag" (62854). Gives "Bowl of Foul-smelling Liquid" (62855).
15. Spawns "Noc Juggernaut" (280091) in `natimbi` on event spawn:280090.
16. Loot "Energized Noc Blood" (62889) from "Noc Juggernaut".
17. Alternative: Loot "Energized Noc Blood" (62889) from "Noc Juggernaut" (NPC 280091) in `natimbi`; trigger: natimbi/"Druid 1 5", on event death_complete:280069.
18. Forage "Emerald Moss" (62856) in `emeraldjungle`.
19. Forage "Sickly Maiden's Hair" (62810) in `rathemtn`.
20. eastkarana/"Althele", hand "Sickly Maiden's Hair" (62810). Gives "Tuft of Sickly Maiden's Hair" (62811).
21. qrg/"Niera Farbreeze", hand "Tuft of Sickly Maiden's Hair" (62811). Gives "Waterproof Collection Bag" (62812).
22. Say "King Timer" to frontiermtns/"Druid 1 5".
23. Spawns npc 92202 (92202).
24. Loot "Bag of Diseased Maiden's Hair" (62826) from npc 92202.
25. eastkarana/"Althele", say "Out Of Balance". Sets `druid_epic` to `1`.
26. Spawns "A Bloodgill Forager" (85234) in `lakeofillomen` on enter.
27. Loot "Handful of Diseased Maiden's Hair" (62825) from "A Bloodgill Forager".
28. Buy "Tackle Box" (17048) from "Misla McMannus" (NPC 12094) in `qey2hh1`. Base price: 1,000 copper.
29. Spawns "Ulthork Raider" (116608) in `eastwastes` on enter.
30. Loot "Carved Prexus Totem" (62821) from "Ulthork Raider".
31. cobaltscar/"Blumblum Swigwater", hand "Carved Prexus Totem" (62821). Gives "Small Trigger Fish" (62820).
32. Buy "Gutting Knife" (62823) from "Tasec Dreeng" (NPC 279113) in `abysmal`. Base price: 40 copper.
33. Combine in "Tackle Box" (17048): "Small Trigger Fish" (62820), "Gutting Knife" (62823). Hands back "Gutting Knife" (62823). Produces "Soggy Maiden's Hair" (62824). Requires Fishing, trivial 20. The combine does not fail.
34. Spawns "spawn #Swamp Terror" (47208) in `feerrott` on enter.
35. Loot "Partially Digested Maiden's Hair" (62819) from "spawn #Swamp Terror".
36. Combine in "Waterproof Collection Bag" (62812): "Bag of Diseased Maiden's Hair" (62826), "Handful of Diseased Maiden's Hair" (62825), "Soggy Maiden's Hair" (62824), "Partially Digested Maiden's Hair" (62819). Produces "Sealed Collection Bag" (62813). The combine does not fail.
37. qrg/"Niera Farbreeze", hand "Sealed Collection Bag" (62813). Gives "Wash Cloth" (62847).
38. Spawns "spawn #Swamp Terror" (47208) in `feerrott` on enter.
39. Loot "Mangled Head" (62818) from "spawn #Swamp Terror".
40. Combine in "Wash Cloth" (62847): "Mangled Head" (62818). Produces "Wrapped Mangled Head" (62848). The combine does not fail.
41. qrg/"Niera Farbreeze", hand "Wrapped Mangled Head" (62848). Gives "Mangled Head" (62827).
42. qrg/"Niera Farbreeze", hand "Wrapped Mangled Head" (62848). Sets `druid_epic` to `2`.
43. poknowledge/"Pathfinder Arelat", say "Worth It". Requires `druid_epic` ==2. Gives "Fresh Awakenings vol. 1" (62839).
44. poknowledge/"Pathfinder Arelat", say "Worth It". Requires `druid_epic` ==2. Gives "Fresh Awakenings vol. 2" (62840).
45. poknowledge/"Pathfinder Arelat", say "Worth It". Requires `druid_epic` ==2. Gives "Fresh Awakenings vol. 3" (62841).
46. poknowledge/"Gravelady Beddia", hand "Fresh Awakenings vol. 1" (62839) + "Fresh Awakenings vol. 2" (62840) + "Fresh Awakenings vol. 3" (62841). Gives "Healing Plants" (62842).
47. qrg/"Niera Farbreeze", hand "Healing Plants" (62842). Sets `druid_epic` to `3`.
48. feerrott/"Corrupted Spirit", say "Show It". Requires `druid_epic` ==3. Gives "Disease Rune" (62837).
49. tox/"A Skeleton", say "I Will Do It". Triggers `tox/a skeleton#timer:pathback`.
50. Starts timer `pathbacktwo`.
51. Starts timer `pathbackthree`.
52. Starts timer `giveitem`.
53. tox/"A Skeleton", on timer giveitem. Gives "Animating Heads" (62828).
54. Combine in "Mangled Head" (62827): "Disease Rune" (62837), "Animating Heads" (62828). Produces "Runed Skull" (62838). The combine does not fail.
55. qrg/"Niera Farbreeze", hand "Healing Plants" (62842). Gives "Niera's Healing Notes" (62849).
56. qrg/"Niera Farbreeze", hand "Runed Skull" (62838) + "Niera's Healing Notes" (62849). Sets `druid_epic` to `4`.
57. qrg/"Niera Farbreeze", hand "Runed Skull" (62838) + "Niera's Healing Notes" (62849). Gives "Niera's Research Notes" (62843).
58. pojustice/"Great Bear", hand "Niera's Research Notes" (62843). Requires `druid_epic` ==4. Gives "Living Brambles Seed" (62845).
59. pojustice/"Great Bear", hand "Niera's Research Notes" (62843). Requires `druid_epic` ==4. Gives "Red Dogwood Seed" (62844).
60. qrg/"Niera Farbreeze", hand "Red Dogwood Seed" (62844) + "Living Brambles Seed" (62845). Requires `druid_epic` ==4. Gives "Mind Crystal" (62846).
61. Combine in "Bowl of Foul-smelling Liquid" (62855): "Energized Noc Blood" (62889), "Emerald Moss" (62856), "Mind Crystal" (62846). Produces "Clear Mind Crystal" (62857). The combine does not fail.
62. abysmal/"Silanda Leafdew", hand "Clear Mind Crystal" (62857). Sets `druid_epic` to `7`.
63. Spawns "A Cracked Earthshaker" (336214) in `dranik` on enter.
64. Loot "Chunk of Energized Clay" (62859) from "A Cracked Earthshaker".
65. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
66. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `steamfont`.
67. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `tox`.
68. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `toxxulia`.
69. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
70. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). The combine does not fail.
71. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
72. Combine in Pottery Wheel (21): "Water Flask" (13006), "Block of Clay" (16901). Produces "Small Block of Clay" (16900) x3. Requires Pottery, trivial 21.
73. Combine in Pottery Wheel (21): "Small Block of Clay" (16900), "Water Flask" (13006). Produces "Block of Clay" (16901). Requires Pottery, trivial 21.
74. Buy "Aerated Pot Sketch" (62858) from "Elisha Dirtyshoes" (NPC 202134) in `poknowledge`. Base price: 300 copper.
75. Combine in Pottery Wheel (21): "Water Flask" (13006), "Block of Clay" (16901), "Aerated Pot Sketch" (62858). Produces "Aerated Pot Shell" (62860). Requires Pottery, trivial 68.
76. Combine in Kiln (22): "Chunk of Energized Clay" (62859), "Aerated Pot Shell" (62860). Produces "Reinforced Aerated Pot" (62861). Requires Pottery, trivial 100. The combine does not fail.
77. qrg/"Niera Farbreeze", hand "Red Dogwood Seed" (62844) + "Living Brambles Seed" (62845). Requires `druid_epic` ==4. Gives "Living Brambles Seed" (62850).
78. Kill kithicor/"Blackened Tree Limb". Spawns "Blackened Dryad" (20301).
79. Loot "Blackened Earth" (62862) from "Blackened Dryad".
80. Combine in "Reinforced Aerated Pot" (62861): "Living Brambles Seed" (62850), "Clear Mind Crystal" (62857), "Blackened Earth" (62862). Produces "Staff of Living Brambles" (62863). The combine does not fail.

## Epic 2.0

### "Staff of Everliving Brambles" (62880)

1. abysmal/"Reyfin Malakwa", say "Hail". Gives "Ragged Cloth Bag" (62881).
2. Loot "Crystal Fragment" (62852) from "Finnelzi Springworthy" in `southkarana`.
3. Loot "Crystal Fragment" (62852) from "Rendolf Deathbringer" in `southkarana`.
4. Loot "Crystal Fragment" (62852) from "Tehana Elsent" in `southkarana`.
5. freportw/"Shana Liskia", hand "Crystal Fragment" (62852) + "Crystal Fragment" (62852) + "Crystal Fragment" (62852). Gives "Small Padded Bag" (62853).
6. freportw/"Shana Liskia", hand "Crystal Fragment" (62852) + "Crystal Fragment" (62852) + "Crystal Fragment" (62852). Sets `druid_epic` to `5`.
7. Spawns "Azibelle Spavin" (335064) in `harbingers` on enter.
8. Loot "Bohab's Crystal Fragment" (62886) from "Azibelle Spavin".
9. Spawns "Azibelle Spavin" (335064) in `harbingers` on enter.
10. Loot "Azibelle's Crystal Fragment" (62887) from "Azibelle Spavin".
11. Spawns "Glenfire Telzir" (335065) in `harbingers` on enter.
12. Loot "Glenfire's Crystal Fragment" (62888) from "Glenfire Telzir".
13. Combine in "Small Padded Bag" (62853): "Bohab's Crystal Fragment" (62886), "Azibelle's Crystal Fragment" (62887), "Glenfire's Crystal Fragment" (62888), "Crystal Fragment" (62852). Produces "Full Padded Bag" (62854). The combine does not fail.
14. freportw/"Shana Liskia", hand "Full Padded Bag" (62854). Gives "Bowl of Foul-smelling Liquid" (62855).
15. Spawns "Noc Juggernaut" (280091) in `natimbi` on event spawn:280090.
16. Loot "Energized Noc Blood" (62889) from "Noc Juggernaut".
17. Alternative: Loot "Energized Noc Blood" (62889) from "Noc Juggernaut" (NPC 280091) in `natimbi`; trigger: natimbi/"Druid 1 5", on event death_complete:280069.
18. Forage "Emerald Moss" (62856) in `emeraldjungle`.
19. Forage "Sickly Maiden's Hair" (62810) in `rathemtn`.
20. eastkarana/"Althele", hand "Sickly Maiden's Hair" (62810). Gives "Tuft of Sickly Maiden's Hair" (62811).
21. qrg/"Niera Farbreeze", hand "Tuft of Sickly Maiden's Hair" (62811). Gives "Waterproof Collection Bag" (62812).
22. Say "King Timer" to frontiermtns/"Druid 1 5".
23. Spawns npc 92202 (92202).
24. Loot "Bag of Diseased Maiden's Hair" (62826) from npc 92202.
25. eastkarana/"Althele", say "Out Of Balance". Sets `druid_epic` to `1`.
26. Spawns "A Bloodgill Forager" (85234) in `lakeofillomen` on enter.
27. Loot "Handful of Diseased Maiden's Hair" (62825) from "A Bloodgill Forager".
28. Buy "Tackle Box" (17048) from "Misla McMannus" (NPC 12094) in `qey2hh1`. Base price: 1,000 copper.
29. Spawns "Ulthork Raider" (116608) in `eastwastes` on enter.
30. Loot "Carved Prexus Totem" (62821) from "Ulthork Raider".
31. cobaltscar/"Blumblum Swigwater", hand "Carved Prexus Totem" (62821). Gives "Small Trigger Fish" (62820).
32. Buy "Gutting Knife" (62823) from "Tasec Dreeng" (NPC 279113) in `abysmal`. Base price: 40 copper.
33. Combine in "Tackle Box" (17048): "Small Trigger Fish" (62820), "Gutting Knife" (62823). Hands back "Gutting Knife" (62823). Produces "Soggy Maiden's Hair" (62824). Requires Fishing, trivial 20. The combine does not fail.
34. Spawns "spawn #Swamp Terror" (47208) in `feerrott` on enter.
35. Loot "Partially Digested Maiden's Hair" (62819) from "spawn #Swamp Terror".
36. Combine in "Waterproof Collection Bag" (62812): "Bag of Diseased Maiden's Hair" (62826), "Handful of Diseased Maiden's Hair" (62825), "Soggy Maiden's Hair" (62824), "Partially Digested Maiden's Hair" (62819). Produces "Sealed Collection Bag" (62813). The combine does not fail.
37. qrg/"Niera Farbreeze", hand "Sealed Collection Bag" (62813). Gives "Wash Cloth" (62847).
38. Spawns "spawn #Swamp Terror" (47208) in `feerrott` on enter.
39. Loot "Mangled Head" (62818) from "spawn #Swamp Terror".
40. Combine in "Wash Cloth" (62847): "Mangled Head" (62818). Produces "Wrapped Mangled Head" (62848). The combine does not fail.
41. qrg/"Niera Farbreeze", hand "Wrapped Mangled Head" (62848). Gives "Mangled Head" (62827).
42. qrg/"Niera Farbreeze", hand "Wrapped Mangled Head" (62848). Sets `druid_epic` to `2`.
43. poknowledge/"Pathfinder Arelat", say "Worth It". Requires `druid_epic` ==2. Gives "Fresh Awakenings vol. 1" (62839).
44. poknowledge/"Pathfinder Arelat", say "Worth It". Requires `druid_epic` ==2. Gives "Fresh Awakenings vol. 2" (62840).
45. poknowledge/"Pathfinder Arelat", say "Worth It". Requires `druid_epic` ==2. Gives "Fresh Awakenings vol. 3" (62841).
46. poknowledge/"Gravelady Beddia", hand "Fresh Awakenings vol. 1" (62839) + "Fresh Awakenings vol. 2" (62840) + "Fresh Awakenings vol. 3" (62841). Gives "Healing Plants" (62842).
47. qrg/"Niera Farbreeze", hand "Healing Plants" (62842). Sets `druid_epic` to `3`.
48. feerrott/"Corrupted Spirit", say "Show It". Requires `druid_epic` ==3. Gives "Disease Rune" (62837).
49. tox/"A Skeleton", say "I Will Do It". Triggers `tox/a skeleton#timer:pathback`.
50. Starts timer `pathbacktwo`.
51. Starts timer `pathbackthree`.
52. Starts timer `giveitem`.
53. tox/"A Skeleton", on timer giveitem. Gives "Animating Heads" (62828).
54. Combine in "Mangled Head" (62827): "Disease Rune" (62837), "Animating Heads" (62828). Produces "Runed Skull" (62838). The combine does not fail.
55. qrg/"Niera Farbreeze", hand "Healing Plants" (62842). Gives "Niera's Healing Notes" (62849).
56. qrg/"Niera Farbreeze", hand "Runed Skull" (62838) + "Niera's Healing Notes" (62849). Sets `druid_epic` to `4`.
57. qrg/"Niera Farbreeze", hand "Runed Skull" (62838) + "Niera's Healing Notes" (62849). Gives "Niera's Research Notes" (62843).
58. pojustice/"Great Bear", hand "Niera's Research Notes" (62843). Requires `druid_epic` ==4. Gives "Living Brambles Seed" (62845).
59. pojustice/"Great Bear", hand "Niera's Research Notes" (62843). Requires `druid_epic` ==4. Gives "Red Dogwood Seed" (62844).
60. qrg/"Niera Farbreeze", hand "Red Dogwood Seed" (62844) + "Living Brambles Seed" (62845). Requires `druid_epic` ==4. Gives "Mind Crystal" (62846).
61. Combine in "Bowl of Foul-smelling Liquid" (62855): "Energized Noc Blood" (62889), "Emerald Moss" (62856), "Mind Crystal" (62846). Produces "Clear Mind Crystal" (62857). The combine does not fail.
62. abysmal/"Silanda Leafdew", hand "Clear Mind Crystal" (62857). Sets `druid_epic` to `7`.
63. Spawns "A Cracked Earthshaker" (336214) in `dranik` on enter.
64. Loot "Chunk of Energized Clay" (62859) from "A Cracked Earthshaker".
65. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
66. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `steamfont`.
67. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `tox`.
68. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `toxxulia`.
69. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
70. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). The combine does not fail.
71. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
72. Combine in Pottery Wheel (21): "Water Flask" (13006), "Block of Clay" (16901). Produces "Small Block of Clay" (16900) x3. Requires Pottery, trivial 21.
73. Combine in Pottery Wheel (21): "Small Block of Clay" (16900), "Water Flask" (13006). Produces "Block of Clay" (16901). Requires Pottery, trivial 21.
74. Buy "Aerated Pot Sketch" (62858) from "Elisha Dirtyshoes" (NPC 202134) in `poknowledge`. Base price: 300 copper.
75. Combine in Pottery Wheel (21): "Water Flask" (13006), "Block of Clay" (16901), "Aerated Pot Sketch" (62858). Produces "Aerated Pot Shell" (62860). Requires Pottery, trivial 68.
76. Combine in Kiln (22): "Chunk of Energized Clay" (62859), "Aerated Pot Shell" (62860). Produces "Reinforced Aerated Pot" (62861). Requires Pottery, trivial 100. The combine does not fail.
77. qrg/"Niera Farbreeze", hand "Red Dogwood Seed" (62844) + "Living Brambles Seed" (62845). Requires `druid_epic` ==4. Gives "Living Brambles Seed" (62850).
78. Kill kithicor/"Blackened Tree Limb". Spawns "Blackened Dryad" (20301).
79. Loot "Blackened Earth" (62862) from "Blackened Dryad".
80. Combine in "Reinforced Aerated Pot" (62861): "Living Brambles Seed" (62850), "Clear Mind Crystal" (62857), "Blackened Earth" (62862). Produces "Staff of Living Brambles" (62863). The combine does not fail.
81. qinimi/"A Broken Ritesdancer", say "What About The Rune Fragments?". Gives "Threadbare Cloth Bag" (62890).
82. qinimi/"A Broken Ritesdancer", say "What About The Rune Fragments?". Gives "Undamaged Noc Fang" (62864).
83. Combine in "Threadbare Cloth Bag" (62890): "Undamaged Noc Fang" (62864). Produces "Closed Cloth Bag" (62891). The combine does not fail.
84. qinimi/"A Broken Ritesdancer", hand "Closed Cloth Bag" (62891). Gives "Rune Fragment" (62867).
85. Forage "Rune Fragment" (62866) in `barindu`.
86. Forage "Rune Fragment" (62866) in `ferubi`.
87. Forage "Rune Fragment" (62866) in `riwwi`.
88. Forage "Rune Fragment" (62865) in `barindu`.
89. Forage "Rune Fragment" (62865) in `ferubi`.
90. Forage "Rune Fragment" (62865) in `riwwi`.
91. Combine in "Ragged Cloth Bag" (62881): "Rune Fragment" (62867), "Rune Fragment" (62866), "Rune Fragment" (62865). Produces "Wrapped Cloth Bag" (62882). The combine does not fail.
92. abysmal/"Reyfin Malakwa", hand "Wrapped Cloth Bag" (62882). Sets `druid_epic` to `10`.
93. nedaria/"Historian Finrazel", say "Plan To Find". Requires `druid_epic` ==10. Gives "Thick Leather Bag" (62884).
94. Kill wallofslaughter/"A Nervous Guardian". Spawns "Lightning Lord" (300098).
95. Loot "Rain Shard" (62872) from "Lightning Lord".
96. Loot "Frost Shard" (62871) from "Bazu Scavenger" in `causeway`.
97. Spawns "Mastruq Commander Gorlakt" (281089) in `qinimi` on enter.
98. Loot "Spirit Shard" (62870) from "Mastruq Commander Gorlakt".
99. Spawns "Tranlinor the Maimed" (302086) in `draniksscar` on enter.
100. Loot "Wind Shard" (62873) from "Tranlinor the Maimed".
101. Combine in "Thick Leather Bag" (62884): "Rain Shard" (62872), "Frost Shard" (62871), "Spirit Shard" (62870), "Wind Shard" (62873). Produces "Synched Leather Bag" (62885). The combine does not fail.
102. abysmal/"Reyfin Malakwa", hand "Synched Leather Bag" (62885). Sets `druid_epic` to `12`.
103. abysmal/"Silanda Leafdew", hand "Synched Leather Bag" (62885). Requires `druid_epic` set. Requires `druid_epic` ==12. Gives "Insulated Container Sketch" (62875).
104. Loot "Faded-Glyph Tablet" (60224) from "Pixtt Condemner" in `ikkinz`.
105. Loot "Runed Glyph: Aktek" (60221) from "Visionary of Glory" in `ikkinz`.
106. Loot "Runed Glyph: Fexika" (60222) from "Visionary of Glory" in `ikkinz`.
107. Loot "Runed Glyph: Niliktek" (60223) from "Visionary of Glory" in `ikkinz`.
108. Combine in "Faded-Glyph Tablet" (60224): "Runed Glyph: Aktek" (60221), "Runed Glyph: Fexika" (60222), "Runed Glyph: Niliktek" (60223). Produces "Axtekilitek" (60225). Requires Research, trivial 100. The combine does not fail.
109. Loot "Runed Glyph: Kruxek" (60226) from "Sentinel of Glorification" in `ikkinz`.
110. Combine in "Faded-Glyph Tablet" (60224): "Axtekilitek" (60225), "Runed Glyph: Kruxek" (60226). Produces "Kruxilitek" (60227). Requires Research, trivial 100. The combine does not fail.
111. Hand "Kruxilitek" (60227) to ikkinz/"Guardian Of Glorification". Spawns "Guardian of Glorification" (294582). Loot "Chunk of Broken Ancient Stone Worker" (58026) from "Guardian of Glorification".
112. Alternative: Loot "Chunk of Broken Ancient Stone Worker" (58026) from "Guardian of Glorification" (NPC 294583) in `ikkinz`; trigger: ikkinz/"Guardian Of Glorification", on event_hp.
113. Alternative: Loot "Chunk of Broken Ancient Stone Worker" (58026) from "A Clay Monolith" (NPC 296002) in `inktuta`; trigger: inktuta/"Zone Status", say "Spawn Golems".
114. Alternative: Loot "Chunk of Broken Ancient Stone Worker" (58026) from "A Clay Monolith" (NPC 296049) in `inktuta`; trigger: inktuta/"Zone Status", say "Spawn Golems".
115. Alternative: Loot "Chunk of Broken Ancient Stone Worker" (58026) from "A Clay Monolith" (NPC 296050) in `inktuta`; trigger: inktuta/"Zone Status", say "Spawn Golems".
116. Alternative: Loot "Chunk of Broken Ancient Stone Worker" (58026) from "A Clay Monolith" (NPC 296051) in `inktuta`; trigger: inktuta/"Zone Status", say "Spawn Golems".
117. Alternative: Loot "Chunk of Broken Ancient Stone Worker" (58026) from "A Freed Rockbearer" (NPC 291131) in `yxtta`; trigger: yxtta/"Player", say "Stone Attack".
118. abysmal/"Hiloan O-Yviania", hand "Chunk of Broken Ancient Stone Worker" (58026). Gives "Clump of Refined Ancient Taelosian Clay" (58031).
119. Combine in Kiln (22): "Insulated Container Sketch" (62875), "Clump of Refined Ancient Taelosian Clay" (58031). Produces "Insulated Container" (62876). Requires Pottery 100. The combine does not fail.
120. global/"Global Player", combine recipe 19908. Gives "Essence of Rainfall" (62883).
121. Combine in "Insulated Container" (62876): "Essence of Rainfall" (62883), "Staff of Living Brambles" (62863). Produces "Staff of Everliving Brambles" (62880). The combine does not fail.

## Quest-state progression

## 0. Prerequisites

Shared acquisition steps appear in the first prerequisite chain that needs them. Later sections reference that chain rather than repeating it.

### "Runed Skull" (62838)

1. Forage "Sickly Maiden's Hair" (62810) in `rathemtn`.
2. eastkarana/"Althele", hand "Sickly Maiden's Hair" (62810). Gives "Tuft of Sickly Maiden's Hair" (62811).
3. qrg/"Niera Farbreeze", hand "Tuft of Sickly Maiden's Hair" (62811). Gives "Waterproof Collection Bag" (62812).
4. Say "King Timer" to frontiermtns/"Druid 1 5".
5. Spawns npc 92202 (92202).
6. Loot "Bag of Diseased Maiden's Hair" (62826) from npc 92202.
7. eastkarana/"Althele", say "Out Of Balance". Sets `druid_epic` to `1`.
8. Spawns "A Bloodgill Forager" (85234) in `lakeofillomen` on enter.
9. Loot "Handful of Diseased Maiden's Hair" (62825) from "A Bloodgill Forager".
10. Buy "Tackle Box" (17048) from "Misla McMannus" (NPC 12094) in `qey2hh1`. Base price: 1,000 copper.
11. Spawns "Ulthork Raider" (116608) in `eastwastes` on enter.
12. Loot "Carved Prexus Totem" (62821) from "Ulthork Raider".
13. cobaltscar/"Blumblum Swigwater", hand "Carved Prexus Totem" (62821). Gives "Small Trigger Fish" (62820).
    - Dialogue with cobaltscar/"Blumblum Swigwater":
      - Player: "Hail"
        - NPC say: I am very busy. Thank you for taking the time to speak to me, stranger, but I have no time for talk right now. I'm afraid that your business can not be urgent enough.
        - Condition: `(e.message:findi("hail"))`
      - Player: "Problem" (link: conversation sequence)
        - NPC say: I appreciate your warm concern strange one, but the Othmir will handle this ourselves. I am certain that it would be below you to take on such troubles, especially when I have only a paltry few sentences of information to trade for it. That is, unless this is seems like a [fair deal] to you, for who am I to judge such a noble, if unusually depilated, creature such as yourself.
        - Condition: `(e.message:findi("problem"))`
      - Player: "Fair Deal" (link: explicit mention)
        - NPC emote: eyes light up and he smiles warmly. 'Such a kind offer! As you may know, we Othmir are exceptional carvers, though it is at brewing that we excel. Our carvings are made from many things, but most commonly of the gruesome teeth of those disgusting Ulthork. We create these beautiful carvings in tribute to our lord Prexus. Turning the ugly teeth of our enemies into items of worship provides several layers of irony and amusement that we can not resist.'
        - Condition: `(e.message:findi("fair deal"))`
      - Player: "Carvings" (link: explicit mention)
        - NPC say: The Ulthork raid our homes when they become desperate. We always push them back, of course. But lately there has been one of there kind that is unusually powerful and he has managed to breach our defenses by force or trickery. They steal food and kill our young, as they always do. This one, though, is unusual in that he has taken one of our carvings. This concerns us, for we had not thought the beasts smart enough to recognize the irony in what we have done with their tusks. Our concern is that this one may be able to recognize the carving for what it is and will use it to incite his people to be more trouble that they usually are. If you can recover that carving as evidence that this beastly Ulthork is dispensed with, I will gladly share with you what we have seen of sickness in our waters.
        - Condition: `(e.message:findi("carvings"))`
      - Player: "Rumors" (link: conversation sequence)
        - NPC say: I hate to repeat such rudeness, but as you insist. Some of my people witnessed a hairless-one swimming from the grotto just before the first sickness was seen. Of course many of your people come swimming out of the grotto, so I would give it little thought. Some of my people have decided that it must have been that hairless swimmer that cause the illness. They say, and forgive me for repeating this, that the skin of your people is poison in the water, that you expose it because it defends you in such ways. Obvious foolishness, I apologize for repeating it.
        - Condition: `(e.message:findi("rumors") and e.other:HasItem(62812))`
14. Buy "Gutting Knife" (62823) from "Tasec Dreeng" (NPC 279113) in `abysmal`. Base price: 40 copper.
15. Combine in "Tackle Box" (17048): "Small Trigger Fish" (62820), "Gutting Knife" (62823). Hands back "Gutting Knife" (62823). Produces "Soggy Maiden's Hair" (62824). Requires Fishing, trivial 20. The combine does not fail.
16. Spawns "spawn #Swamp Terror" (47208) in `feerrott` on enter.
17. Loot "Partially Digested Maiden's Hair" (62819) from "spawn #Swamp Terror".
18. Combine in "Waterproof Collection Bag" (62812): "Bag of Diseased Maiden's Hair" (62826), "Handful of Diseased Maiden's Hair" (62825), "Soggy Maiden's Hair" (62824), "Partially Digested Maiden's Hair" (62819). Produces "Sealed Collection Bag" (62813). The combine does not fail.
19. qrg/"Niera Farbreeze", hand "Sealed Collection Bag" (62813). Gives "Wash Cloth" (62847).
20. Spawns "spawn #Swamp Terror" (47208) in `feerrott` on enter.
21. Loot "Mangled Head" (62818) from "spawn #Swamp Terror".
22. Combine in "Wash Cloth" (62847): "Mangled Head" (62818). Produces "Wrapped Mangled Head" (62848). The combine does not fail.
23. qrg/"Niera Farbreeze", hand "Wrapped Mangled Head" (62848). Gives "Mangled Head" (62827).
24. qrg/"Niera Farbreeze", hand "Wrapped Mangled Head" (62848). Sets `druid_epic` to `2`.
25. poknowledge/"Pathfinder Arelat", say "Worth It". Requires `druid_epic` ==2. Gives "Fresh Awakenings vol. 1" (62839).
    - Dialogue with poknowledge/"Pathfinder Arelat":
      - Player: "Hail"
        - NPC say: Welcome to New Tanaan, friend, and know us as neither friend nor foe. We are your allies in knowledge and shall guide you wherever we are able. Each citizen of New Tanaan, be them a child of the gods or a creature of the natural wilds, has come forward in these times to offer their wisdom and guidance unto you in any way possible. I traveled Norrath once as a pathfinder of Karana, but my fate would eventually call me here where I progressed beyond my mortal limits. Though you have some time left in you before such possibilities are open to you, perhaps the spells I have penned from memory of my service to Norrath will come to be of some use.
        - Condition: `(e.message:findi("hail"))`
      - Player: "Corruption of the Night" (link: conversation sequence)
        - NPC emote: raises an eyebrow. 'Now where did you hear that name?' He looks intently at you for a moment. 'You've been talking to Beddia. She's been trying to get a copy of that text for a long time. I've been careful not to let her get one, if only for the principle of the thing. It's obvious that she sent you here, or one of her minions. Why would I want to give it to you? More importantly, why would a druid want to give it to her?' Arelat raises a hand, 'No, you don't have to tell me. If I can't trust you, , then I suppose I can't even trust myself. Just tell me that it's worth it.
        - Condition: `(qglobals["druid_epic"] == "2" and e.message:findi("Corruption of the Night"))`
      - Player: "Worth It" (link: explicit mention)
        - NPC say: Then here it is. This is a copy of an ancient text that we have preserved and copied for many long years. The author died generations ago. You should read it before you give it to that witch. Good luck to you, friend.
        - Condition: `(qglobals["druid_epic"] == "2" and e.message:findi("worth it"))`
        - Gives Fresh Awakenings vol. 1 (62839).
        - Gives Fresh Awakenings vol. 2 (62840).
        - Gives Fresh Awakenings vol. 3 (62841).
26. poknowledge/"Pathfinder Arelat", say "Worth It". Requires `druid_epic` ==2. Gives "Fresh Awakenings vol. 2" (62840).
27. poknowledge/"Pathfinder Arelat", say "Worth It". Requires `druid_epic` ==2. Gives "Fresh Awakenings vol. 3" (62841).
28. poknowledge/"Gravelady Beddia", hand "Fresh Awakenings vol. 1" (62839) + "Fresh Awakenings vol. 2" (62840) + "Fresh Awakenings vol. 3" (62841). Gives "Healing Plants" (62842).
    - Dialogue with poknowledge/"Gravelady Beddia":
      - Player: "Hail"
        - NPC say: Hail seeker of knowledge. There is much to be learned here in New Tanaan of the dark gods of Norrath. I have been searching the great library for tomes pertaining to my patron Bertoxxulous. the Plague Lord and made some interesting finds. If you wish to study the tomes I have uncovered you may borrow them and they will be returned to me by the magic of New Tanaan when you are through.
        - Condition: `(e.message:findi("hail"))`
      - Player: "What diseases of the skin" (link: conversation sequence)
        - NPC say: I know much about such things, but what would you want such knowledge for? I can only surmise that your goals would not be such that I would approve of them. You would have to be willing to [sacrifice] something, get me something precious, in order to get any such information from me.
        - Condition: `(qglobals["druid_epic"] == "2" and e.message:findi("What diseases of the skin"))`
      - Player: "Sacrifice" (link: explicit mention)
        - NPC say: Hmmm... since you seem to be a creature of the woods, perhaps you can get something for me that I've wanted to read for a long time. There is a story of a battle between the God of Dribbles and the Lord of Plagues. We call this battle The Corruption of Night. I don't know what you people call it, but I know you must have a text concerning it. Bring me that text and I shall give you something that you probably should not have.
        - Condition: `(qglobals["druid_epic"] == "2" and e.message:findi("sacrifice"))`
29. qrg/"Niera Farbreeze", hand "Healing Plants" (62842). Sets `druid_epic` to `3`.
30. feerrott/"Corrupted Spirit", say "Show It". Requires `druid_epic` ==3. Gives "Disease Rune" (62837).
    - Dialogue with feerrott/"Corrupted Spirit":
      - Player: "Who are you?"
        - NPC say: You don't even know who I am? You summon me back here and you don't even know me? There's no way I'll. . .' The voice wavers as it struggles to deny an answer to your question. The struggle is short, however, and he continues. 'Gah! Fine, my name is Sanmuel Gingerfly of Qeynos.
        - Condition: `(qglobals["druid_epic"] == "3" and e.message:findi("Who are you?"))`
      - Player: "What about the disease?" (link: conversation sequence)
        - NPC say: What do you want to know about disease? I'm kind of an expert. I know something about a great plague that you will soon die from! I helped create it!
        - Condition: `(e.message:findi("What about the disease?"))`
      - Player: "What plague?" (link: explicit mention)
        - NPC say: I know that it is a special plague, designed by. . .' again he tries to resist speaking, but the power of the gem that binds him into his own skull is too powerful, 'Azibelle and the Afflicted. Oh, she's gonna be mad at me. It will grow in the plants and be eaten by the animals. It won't show any signs for a long time. By then you'll all have eaten something with the plague! I got to deliver some of it to the first victims! I even remember one of the key runes. I. . .' again the hesitation, 'can [show it] to you if you want.
        - Condition: `(qglobals["druid_epic"] == "3" and e.message:findi("What plague?"))`
      - Player: "Show It" (link: explicit mention)
        - NPC message: The skull of the dead acolyte glows briefly and all of the remaining flesh falls from it. An ephemeral rune appears in your hand. 'Place that where that horrible stone was before, in my very own head with that nasty scroll, and you will be able to engrave it into my skull. My poor skull! Hurry up, though, that rune won't last forever.
        - Condition: `(qglobals["druid_epic"] == "3" and e.message:findi("show it"))`
        - Gives Disease Rune (62837).
      - Player: "Who are Azibelle and the Afflicted?" (link: prompt response)
        - Prompted by player input: "What plague?"
        - NPC say: I won't tell you!' The voice goes silent for a few moments and you fear that he might have broken the spell, but his voice returns. 'The Afflicted were created by Azibelle shortly after Mordavin was killed. When the Bloodsabers refused to protect Mordavin, she broke from them and took some key members with her. Glenfire is her right hand, a wicked woman with great power. The others she has brought in are Finnelzi Springworthy, Rendolf Deathbringer, Tehana Elsent and my brother, Bohab.
        - Condition: `(qglobals["druid_epic"] == "3" and e.message:findi("Who are Azibelle and the Afflicted?"))`
      - Player: "Who is Glenfire?" (link: prompt response)
        - NPC say: She's the most powerful woman I've ever met. She's a dark elven shadowknight and if I were you I'd stay away from her. Nobody has ever beat her in a fight and I don't think she tries her hardest.
        - Condition: `(qglobals["druid_epic"] == "3" and e.message:findi("Who is Glenfire?"))`
      - Player: "Who is Finnelzi Springworthy?" (link: prompt response)
        - Prompted by player input: "Who are Azibelle and the Afflicted?"
        - NPC say: Fin? He's a gnome. I suppose he's a powerful necromancer, but it's hard to fear someone that can't see over a low hedge. Besides, I always suspected that he had reservations about our work. I should have had his place in the coven!
        - Condition: `(qglobals["druid_epic"] == "3" and e.message:findi("Who is Finnelzi Springworthy?"))`
      - Player: "Who is Rendolf Deathbringer?" (link: prompt response)
        - Prompted by player input: "Who are Azibelle and the Afflicted?"
        - NPC say: Heh. He used to be called Rendolf Shelton. He changed his name so he'd sound more like a shadowknight. He's a great fighter, though, so nobody teases him about it. I think he has a crush on Glenfire, but she'd rather kill a human than sleep with one.
        - Condition: `(qglobals["druid_epic"] == "3" and e.message:findi("Who is Rendolf Deathbringer?"))`
      - Player: "Who is Tehana Elsent?" (link: prompt response)
        - Prompted by player input: "Who are Azibelle and the Afflicted?"
        - NPC say: Tehana is a true necromancer. She studies the lore and the spells. She knows everything there is to know about the undead. She has been studying diseases, but I don't think they really meant much to her except that they make people dead. She was the one to recreate some of Mordavin's work from his notes and repurposed it for Azibelle's needs. She's kind of excited about killing everyone. She is inspired by Azibelle and Glenfire and does most of the support work for the coven.
        - Condition: `(qglobals["druid_epic"] == "3" and e.message:findi("Who is Tehana Elsent?"))`
      - Player: "Who is Bohab?" (link: prompt response)
        - Prompted by player input: "Who are Azibelle and the Afflicted?"
        - NPC say: I won't tell you anything about him. He protected me as a child in the streets of Qeynos and I will not tell you anything about him.
        - Condition: `(qglobals["druid_epic"] == "3" and e.message:findi("Who is Bohab?"))`
31. tox/"A Skeleton", say "I Will Do It". Triggers `tox/a skeleton#timer:pathback`.
32. Starts timer `pathbacktwo`.
33. Starts timer `pathbackthree`.
34. Starts timer `giveitem`.
35. tox/"A Skeleton", on timer giveitem. Gives "Animating Heads" (62828).
36. Combine in "Mangled Head" (62827): "Disease Rune" (62837), "Animating Heads" (62828). Produces "Runed Skull" (62838). The combine does not fail.

### "Healing Plants" (62842)

1. Acquisition of "Healing Plants" (62842) is documented under "Runed Skull" (62838); obtain another copy if needed.

### "Mind Crystal" (62846)

1. Acquisition of "Runed Skull" (62838) is documented under "Runed Skull" (62838); obtain another copy if needed.
2. Acquisition of "Healing Plants" (62842) is documented under "Runed Skull" (62838); obtain another copy if needed.
3. qrg/"Niera Farbreeze", hand "Healing Plants" (62842). Gives "Niera's Healing Notes" (62849).
4. qrg/"Niera Farbreeze", hand "Runed Skull" (62838) + "Niera's Healing Notes" (62849). Sets `druid_epic` to `4`.
5. qrg/"Niera Farbreeze", hand "Runed Skull" (62838) + "Niera's Healing Notes" (62849). Gives "Niera's Research Notes" (62843).
6. pojustice/"Great Bear", hand "Niera's Research Notes" (62843). Requires `druid_epic` ==4. Gives "Living Brambles Seed" (62845).
    - Dialogue with pojustice/"Great Bear":
      - Player: "Hail"
        - NPC say: What do you want? Were you not, what is it you are called, druid? Were you not druid I would rip your head from your torso. What you want had better be important.
        - Condition: `(qglobals["druid_epic"] == "4" and e.other:GetFaction(e.self) < 5)`
        - Condition: `( e.message:findi("hail"))`
      - Player: "What about the Tribe of the Dawn?" (link: conversation sequence)
        - NPC say: I am the tribe of the Dawn. I have been placed here for killing some beast that entered my territory. The creatures here say that I was unjust in doing so. I don't care about their justice or rules. It was where it did not belong. What do you want of me? I have something I must do soon.
        - Condition: `(qglobals["druid_epic"] == "4" and e.other:GetFaction(e.self) < 5)`
        - Condition: `(e.message:findi("What about the Tribe of the Dawn?"))`
7. pojustice/"Great Bear", hand "Niera's Research Notes" (62843). Requires `druid_epic` ==4. Gives "Red Dogwood Seed" (62844).
8. qrg/"Niera Farbreeze", hand "Red Dogwood Seed" (62844) + "Living Brambles Seed" (62845). Requires `druid_epic` ==4. Gives "Mind Crystal" (62846).

### "Wrapped Mangled Head" (62848)

1. Acquisition of "Wrapped Mangled Head" (62848) is documented under "Runed Skull" (62838); obtain another copy if needed.

### "Niera's Healing Notes" (62849)

1. Acquisition of "Niera's Healing Notes" (62849) is documented under "Mind Crystal" (62846); obtain another copy if needed.

### "Living Brambles Seed" (62850)

1. Acquisition of "Living Brambles Seed" (62845) is documented under "Mind Crystal" (62846); obtain another copy if needed.
2. Acquisition of "Red Dogwood Seed" (62844) is documented under "Mind Crystal" (62846); obtain another copy if needed.
3. qrg/"Niera Farbreeze", hand "Red Dogwood Seed" (62844) + "Living Brambles Seed" (62845). Requires `druid_epic` ==4. Gives "Living Brambles Seed" (62850).

### "Clear Mind Crystal" (62857)

1. Loot "Crystal Fragment" (62852) from "Finnelzi Springworthy" in `southkarana`.
2. Loot "Crystal Fragment" (62852) from "Rendolf Deathbringer" in `southkarana`.
3. Loot "Crystal Fragment" (62852) from "Tehana Elsent" in `southkarana`.
4. freportw/"Shana Liskia", hand "Crystal Fragment" (62852) + "Crystal Fragment" (62852) + "Crystal Fragment" (62852). Gives "Small Padded Bag" (62853).
5. freportw/"Shana Liskia", hand "Crystal Fragment" (62852) + "Crystal Fragment" (62852) + "Crystal Fragment" (62852). Sets `druid_epic` to `5`.
6. Spawns "Azibelle Spavin" (335064) in `harbingers` on enter.
7. Loot "Bohab's Crystal Fragment" (62886) from "Azibelle Spavin".
8. Spawns "Azibelle Spavin" (335064) in `harbingers` on enter.
9. Loot "Azibelle's Crystal Fragment" (62887) from "Azibelle Spavin".
10. Spawns "Glenfire Telzir" (335065) in `harbingers` on enter.
11. Loot "Glenfire's Crystal Fragment" (62888) from "Glenfire Telzir".
12. Combine in "Small Padded Bag" (62853): "Bohab's Crystal Fragment" (62886), "Azibelle's Crystal Fragment" (62887), "Glenfire's Crystal Fragment" (62888), "Crystal Fragment" (62852). Produces "Full Padded Bag" (62854). The combine does not fail.
13. freportw/"Shana Liskia", hand "Full Padded Bag" (62854). Gives "Bowl of Foul-smelling Liquid" (62855).
14. Spawns "Noc Juggernaut" (280091) in `natimbi` on event spawn:280090.
15. Loot "Energized Noc Blood" (62889) from "Noc Juggernaut".
16. Alternative: Loot "Energized Noc Blood" (62889) from "Noc Juggernaut" (NPC 280091) in `natimbi`; trigger: natimbi/"Druid 1 5", on event death_complete:280069.
17. Forage "Emerald Moss" (62856) in `emeraldjungle`.
18. Acquisition of "Mind Crystal" (62846) is documented under "Mind Crystal" (62846); obtain another copy if needed.
19. Combine in "Bowl of Foul-smelling Liquid" (62855): "Energized Noc Blood" (62889), "Emerald Moss" (62856), "Mind Crystal" (62846). Produces "Clear Mind Crystal" (62857). The combine does not fail.

### "Reinforced Aerated Pot" (62861)

1. Acquisition of "Clear Mind Crystal" (62857) is documented under "Clear Mind Crystal" (62857); obtain another copy if needed.
2. abysmal/"Silanda Leafdew", hand "Clear Mind Crystal" (62857). Sets `druid_epic` to `7`.
3. Spawns "A Cracked Earthshaker" (336214) in `dranik` on enter.
4. Loot "Chunk of Energized Clay" (62859) from "A Cracked Earthshaker".
5. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
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
6. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `steamfont`.
7. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `tox`.
8. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `toxxulia`.
9. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
10. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). The combine does not fail.
11. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
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
12. Combine in Pottery Wheel (21): "Water Flask" (13006), "Block of Clay" (16901). Produces "Small Block of Clay" (16900) x3. Requires Pottery, trivial 21.
13. Combine in Pottery Wheel (21): "Small Block of Clay" (16900), "Water Flask" (13006). Produces "Block of Clay" (16901). Requires Pottery, trivial 21.
14. Buy "Aerated Pot Sketch" (62858) from "Elisha Dirtyshoes" (NPC 202134) in `poknowledge`. Base price: 300 copper.
15. Combine in Pottery Wheel (21): "Water Flask" (13006), "Block of Clay" (16901), "Aerated Pot Sketch" (62858). Produces "Aerated Pot Shell" (62860). Requires Pottery, trivial 68.
16. Combine in Kiln (22): "Chunk of Energized Clay" (62859), "Aerated Pot Shell" (62860). Produces "Reinforced Aerated Pot" (62861). Requires Pottery, trivial 100. The combine does not fail.

### "Staff of Living Brambles" (62863)

1. Acquisition of "Reinforced Aerated Pot" (62861) is documented under "Reinforced Aerated Pot" (62861); obtain another copy if needed.
2. Acquisition of "Living Brambles Seed" (62850) is documented under "Living Brambles Seed" (62850); obtain another copy if needed.
3. Acquisition of "Clear Mind Crystal" (62857) is documented under "Clear Mind Crystal" (62857); obtain another copy if needed.
4. Kill kithicor/"Blackened Tree Limb". Spawns "Blackened Dryad" (20301).
5. Loot "Blackened Earth" (62862) from "Blackened Dryad".
6. Combine in "Reinforced Aerated Pot" (62861): "Living Brambles Seed" (62850), "Clear Mind Crystal" (62857), "Blackened Earth" (62862). Produces "Staff of Living Brambles" (62863). The combine does not fail.

### "Rune of Yuisaha" (62868)

1. Acquisition of "Staff of Living Brambles" (62863) is documented under "Staff of Living Brambles" (62863); obtain another copy if needed.
2. abysmal/"Reyfin Malakwa", say "Hail". Gives "Ragged Cloth Bag" (62881).
3. qinimi/"A Broken Ritesdancer", say "What About The Rune Fragments?". Gives "Threadbare Cloth Bag" (62890).
    - Dialogue with qinimi/"A Broken Ritesdancer":
      - Player: "What about the rune fragments?"
        - NPC message: The worn Taelosian looks up at you defiantly. She studies you a moment and nods. Whatever judgment she was making about you, you seem to have passed. She reaches into her ragged clothing and pulls out a small hunk of rock and hands it to you. She then quickly returns to work.
          - Reply guard: `(e.other:GetFaction(e.self) <=2)`
        - NPC message: The worn Taelosian looks up at you discretely, as if looking at you directly would cause physical pain. She shyly hands you a small, worn bag and what appears to be an animal fang. She then holds up six fingers and points at the fang, then points at herself. She then turns quickly away and proceeds to act as if you are not there.
          - Reply guard: ``
        - Condition: `(e.message:findi("What about the rune fragments?"))`
        - Gives Rune Fragment (62867).
        - Gives Threadbare Cloth Bag (62890).
        - Gives Undamaged Noc Fang (62864).
4. qinimi/"A Broken Ritesdancer", say "What About The Rune Fragments?". Gives "Undamaged Noc Fang" (62864).
5. Combine in "Threadbare Cloth Bag" (62890): "Undamaged Noc Fang" (62864). Produces "Closed Cloth Bag" (62891). The combine does not fail.
6. qinimi/"A Broken Ritesdancer", hand "Closed Cloth Bag" (62891). Gives "Rune Fragment" (62867).
7. Forage "Rune Fragment" (62866) in `barindu`.
8. Forage "Rune Fragment" (62866) in `ferubi`.
9. Forage "Rune Fragment" (62866) in `riwwi`.
10. Forage "Rune Fragment" (62865) in `barindu`.
11. Forage "Rune Fragment" (62865) in `ferubi`.
12. Forage "Rune Fragment" (62865) in `riwwi`.
13. Combine in "Ragged Cloth Bag" (62881): "Rune Fragment" (62867), "Rune Fragment" (62866), "Rune Fragment" (62865). Produces "Wrapped Cloth Bag" (62882). The combine does not fail.
14. abysmal/"Reyfin Malakwa", hand "Wrapped Cloth Bag" (62882). Gives "Rune of Yuisaha" (62868).

### "Insulated Container" (62876)

1. Acquisition of "Wrapped Cloth Bag" (62882) is documented under "Rune of Yuisaha" (62868); obtain another copy if needed.
2. abysmal/"Reyfin Malakwa", hand "Wrapped Cloth Bag" (62882). Sets `druid_epic` to `10`.
3. nedaria/"Historian Finrazel", say "Plan To Find". Requires `druid_epic` ==10. Gives "Thick Leather Bag" (62884).
4. Kill wallofslaughter/"A Nervous Guardian". Spawns "Lightning Lord" (300098).
5. Loot "Rain Shard" (62872) from "Lightning Lord".
6. Loot "Frost Shard" (62871) from "Bazu Scavenger" in `causeway`.
7. Spawns "Mastruq Commander Gorlakt" (281089) in `qinimi` on enter.
8. Loot "Spirit Shard" (62870) from "Mastruq Commander Gorlakt".
9. Spawns "Tranlinor the Maimed" (302086) in `draniksscar` on enter.
10. Loot "Wind Shard" (62873) from "Tranlinor the Maimed".
11. Combine in "Thick Leather Bag" (62884): "Rain Shard" (62872), "Frost Shard" (62871), "Spirit Shard" (62870), "Wind Shard" (62873). Produces "Synched Leather Bag" (62885). The combine does not fail.
12. abysmal/"Reyfin Malakwa", hand "Synched Leather Bag" (62885). Sets `druid_epic` to `12`.
13. abysmal/"Silanda Leafdew", hand "Synched Leather Bag" (62885). Requires `druid_epic` set. Requires `druid_epic` ==12. Gives "Insulated Container Sketch" (62875).
14. Loot "Faded-Glyph Tablet" (60224) from "Pixtt Condemner" in `ikkinz`.
15. Loot "Runed Glyph: Aktek" (60221) from "Visionary of Glory" in `ikkinz`.
16. Loot "Runed Glyph: Fexika" (60222) from "Visionary of Glory" in `ikkinz`.
17. Loot "Runed Glyph: Niliktek" (60223) from "Visionary of Glory" in `ikkinz`.
18. Combine in "Faded-Glyph Tablet" (60224): "Runed Glyph: Aktek" (60221), "Runed Glyph: Fexika" (60222), "Runed Glyph: Niliktek" (60223). Produces "Axtekilitek" (60225). Requires Research, trivial 100. The combine does not fail.
19. Loot "Runed Glyph: Kruxek" (60226) from "Sentinel of Glorification" in `ikkinz`.
20. Combine in "Faded-Glyph Tablet" (60224): "Axtekilitek" (60225), "Runed Glyph: Kruxek" (60226). Produces "Kruxilitek" (60227). Requires Research, trivial 100. The combine does not fail.
21. Hand "Kruxilitek" (60227) to ikkinz/"Guardian Of Glorification". Spawns "Guardian of Glorification" (294582). Loot "Chunk of Broken Ancient Stone Worker" (58026) from "Guardian of Glorification".
22. Alternative: Loot "Chunk of Broken Ancient Stone Worker" (58026) from "Guardian of Glorification" (NPC 294583) in `ikkinz`; trigger: ikkinz/"Guardian Of Glorification", on event_hp.
23. Alternative: Loot "Chunk of Broken Ancient Stone Worker" (58026) from "A Clay Monolith" (NPC 296002) in `inktuta`; trigger: inktuta/"Zone Status", say "Spawn Golems".
24. Alternative: Loot "Chunk of Broken Ancient Stone Worker" (58026) from "A Clay Monolith" (NPC 296049) in `inktuta`; trigger: inktuta/"Zone Status", say "Spawn Golems".
25. Alternative: Loot "Chunk of Broken Ancient Stone Worker" (58026) from "A Clay Monolith" (NPC 296050) in `inktuta`; trigger: inktuta/"Zone Status", say "Spawn Golems".
26. Alternative: Loot "Chunk of Broken Ancient Stone Worker" (58026) from "A Clay Monolith" (NPC 296051) in `inktuta`; trigger: inktuta/"Zone Status", say "Spawn Golems".
27. Alternative: Loot "Chunk of Broken Ancient Stone Worker" (58026) from "A Freed Rockbearer" (NPC 291131) in `yxtta`; trigger: yxtta/"Player", say "Stone Attack".
28. abysmal/"Hiloan O-Yviania", hand "Chunk of Broken Ancient Stone Worker" (58026). Gives "Clump of Refined Ancient Taelosian Clay" (58031).
    - Dialogue with abysmal/"Hiloan O-Yviania":
      - Player: "Hail"
        - NPC emote: glances at you and holds your stare for a moment before speaking.
        - NPC say: I don't suppose you have any skill at all throwing pots or at the kiln, because if you do I could use your help with some of the more [intricate items] that the fools around here are always breaking.
        - Condition: `($text=~/hail/i)`
      - Player: "Intricate Items" (link: explicit mention)
        - NPC say: I have been given the unsatisfying task of replacing [specialty items] for the gardeners and the folks that deal in poisons and other such things. But I just don't have time for it. I have my own research into the native clay to work on. There appear to be golems made out of a type of clay that was dug up long ago, when this land was much more fertile and magical. The clay of these [ancient golems] is more powerful and useful than the rest. If you are interested in helping Malkidiv out with lesser tasks, talk to him. He can also refine chunks of broken golem for you.
        - Condition: `($text=~/intricate items/i)`
      - Player: "Specialty Items" (link: explicit mention)
        - NPC say: Let's put you to work. You don't have to be a skilled potter to handle this. Oh and, well, I'll need you to get some Clump of Refined Taelosian Golem Clay from Malkidiv. He can refine chunks of golems for you, if you can find some. I won't need the ancient stuff for these tasks. Hand me the clumps and I'll get you started. Work hard for me and I'll reward you with the secret recipe that Malkidiv and I share. And since what I need is more difficult to obtain, I'll be quicker to reward you.
        - Condition: `($text=~/specialty items/i)`
29. Combine in Kiln (22): "Insulated Container Sketch" (62875), "Clump of Refined Ancient Taelosian Clay" (58031). Produces "Insulated Container" (62876). Requires Pottery 100. The combine does not fail.

### "Wrapped Cloth Bag" (62882)

1. Acquisition of "Wrapped Cloth Bag" (62882) is documented under "Rune of Yuisaha" (62868); obtain another copy if needed.

### "Synched Leather Bag" (62885)

1. Acquisition of "Synched Leather Bag" (62885) is documented under "Insulated Container" (62876); obtain another copy if needed.

### `druid_epic`

Values written: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13.

1. eastkarana/"Althele", say "Out Of Balance". Sets `druid_epic` to `1`.
    - Requires `druid_epic` unset.

2. qrg/"Niera Farbreeze", hand "Wrapped Mangled Head" (62848). Sets `druid_epic` to `2`.
    - Hand in x1: "Wrapped Mangled Head" (62848).
    - Prerequisite: "Wrapped Mangled Head" (62848). See section 0.
    - Gives "Mangled Head" (62827).
    - Dialogue with qrg/"Niera Farbreeze":
      - Player: "Tune"
        - NPC say: Ohh. Just a little song my mother taught me when I was young. It speaks of the earth, the sky, and the sparkling stars above, always there.
        - Condition: `(e.message:findi("tune") or e.message:findi("humming"))`
      - Player: "Humming" (link: conversation sequence)
        - NPC say: Ohh. Just a little song my mother taught me when I was young. It speaks of the earth, the sky, and the sparkling stars above, always there.
        - Condition: `(e.message:findi("tune") or e.message:findi("humming"))`
      - Player: "Always There" (link: explicit mention)
        - NPC say: Aye, always there. Like this small bag I wear around my neck. The last gift of my dying mother. It holds a fine dust, a dust she collected during her short life, that she believed brought her luck. It's speckled, flecked as the night sky is with stars.
        - Condition: `(e.message:findi("always there"))`
      - Player: "Speckled Flecked Dust" (link: conversation sequence)
        - NPC say: I've had this little bit of dust, all I have of my mother, for many years now. It's the only reminder I have of her. She said it was special, magical, a warmth to help me through the nights. Even if my life were in the balance, I would have a hard time giving it up.
        - Condition: `(e.message:findi("speckled flecked dust"))`
      - Player: "Idea" (link: external event mention)
        - Prompted by `event_trade`:
          - NPC say: You say that this Bouncer told you that he'd thrown someone in the river with grass in his pants? How very strange. You should search the river, see if you can find anything, though I don't know how you could expect to find anything in that mess. Hmm... these scales give me an [idea].
          - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 62814}))`
        - NPC say: Well, you could enlist the aid of the animals. Unfortunately, you can't get a lot of useful information out of a fish or a bird in normal circumstances. There might be a way, however, to get some very specific information. There is lore that suggests that a simple charm can be made that will allow you to know the thoughts of a befriended animal, but only about a particular subject. You need four things, magical clay, a body part from the animal you wish to befriend, something on the subject that you wish to know about and some water. You also need to use a kiln, so I hope you are a talented potter. Now, this only works on the animal from which the body part is taken or one of its direct descendents. You may have to try a lot of animals to find the right one.
        - NPC say: You already have a body part from an alligator in Feerrott. There is magical clay to be found in Taelosia, from what I hear. All you need then is something to focus the animal's mind on. Food is probably the best thing. Gators eat just about anything, so there's a chance you can find one that knows where that intruder with the grass ended up if you can get an alligator to tell you where it's eaten. I'd suggest a good slab of the best piranha meat you can find. It's worth a try. At this point any help would be good. I've been looking at this disease and it is nasty in a subtle way. It barely infects the plants, causes them little harm, but it spreads quickly. So quickly, in fact, that it must be magical. We need more information to stop it.
        - Condition: `(e.message:findi("idea") and e.other:HasItem(62817))`

3. qrg/"Niera Farbreeze", hand "Healing Plants" (62842). Sets `druid_epic` to `3`.
    - Hand in x1: "Healing Plants" (62842).
    - Prerequisite: "Healing Plants" (62842). See section 0.
    - Gives "Niera's Healing Notes" (62849).

4. qrg/"Niera Farbreeze", hand "Runed Skull" (62838) + "Niera's Healing Notes" (62849). Sets `druid_epic` to `4`.
    - Hand in x1: "Runed Skull" (62838).
    - Hand in x1: "Niera's Healing Notes" (62849).
    - Prerequisite: "Runed Skull" (62838). See section 0.
    - Prerequisite: "Niera's Healing Notes" (62849). See section 0.
    - Gives "Niera's Research Notes" (62843).

5. freportw/"Shana Liskia", hand "Crystal Fragment" (62852) + "Crystal Fragment" (62852) + "Crystal Fragment" (62852). Sets `druid_epic` to `5`.
    - Hand in x1: "Crystal Fragment" (62852).
    - Loot "Crystal Fragment" (62852) from "Finnelzi Springworthy" in `southkarana`.
    - Loot "Crystal Fragment" (62852) from "Rendolf Deathbringer" in `southkarana`.
    - Loot "Crystal Fragment" (62852) from "Tehana Elsent" in `southkarana`.
    - Gives "Crystal Fragment" (62852).
    - Gives "Small Padded Bag" (62853).
    - Dialogue with freportw/"Shana Liskia":
      - Player: "Hail"
        - NPC say: Hail and well met . I am Shana Liskia. Enchantress of Freeport. I have studied my art for years here in our wonderful academy. I am also delighted to meet and teach those that come here to gain knowledge. My specialty however lies in Beguiling so I like to train young newcomers to our academy. Are you studying the ways of a [Magician] an [Enchanter] or a [Wizard]??
        - Condition: `(e.message:findi("hail"))`
      - Player: "Magician" (link: explicit mention)
        - NPC say: Wonderful! Let me be the first to tell you that your training here will be top notch and you will learn all that is to be known about being an enchanter should you put forth the willingness to learn. I will walk you through your early training and assist you in your hunting and gathering skills. I have created a [special sewing kit] that I present to all of the new initiates.
        - Condition: `(e.message:findi("magician") or e.message:findi("enchanter") or e.message:findi("wizard"))`
      - Player: "Enchanter" (link: explicit mention)
        - NPC say: Wonderful! Let me be the first to tell you that your training here will be top notch and you will learn all that is to be known about being an enchanter should you put forth the willingness to learn. I will walk you through your early training and assist you in your hunting and gathering skills. I have created a [special sewing kit] that I present to all of the new initiates.
        - Condition: `(e.message:findi("magician") or e.message:findi("enchanter") or e.message:findi("wizard"))`
      - Player: "Wizard" (link: explicit mention)
        - Prompted by player input: "Hail"
        - NPC say: Wonderful! Let me be the first to tell you that your training here will be top notch and you will learn all that is to be known about being an enchanter should you put forth the willingness to learn. I will walk you through your early training and assist you in your hunting and gathering skills. I have created a [special sewing kit] that I present to all of the new initiates.
        - Condition: `(e.message:findi("magician") or e.message:findi("enchanter") or e.message:findi("wizard"))`
      - Player: "Diseases Of The Mind" (link: conversation sequence)
        - NPC say: I study the mind. My most recent research deals with, well, I'd rather not discuss that. Unless you need something specific, I don't really have time for long random conversations right now.
        - Condition: `(e.message:findi("diseases of the mind"))`
      - Player: "Special Sewing Kit" (link: explicit mention)
        - Prompted by player input: "Magician"
        - NPC say: This kit that I speak of is one that is able to magically infuse different components into materials used for creating Arcane Scientists Armor. The components that you use will be collected from numerous different areas and shops in Freeport. You will use these materials along with patterns that I will present you with to create your armor. Once you are [ready to begin] I will present you with your Enchanted Sewing Kit.
        - Condition: `(e.other:Class() == "Enchanter" or e.other:Class() == "Magician" or e.other:Class() == "Wizard")`
        - Condition: `(e.message:findi("special sewing kit"))`
      - Player: "Ready To Begin" (link: explicit mention)
        - NPC say: Very well. Here you are . in this box you will combine specific component recipes as I mentioned before. When you are ready to attempt a specific piece you must tell me what piece you [want] to craft. For example if you had intent on crafting a cap you would say. [I want to craft a cap]. I can offer you the recipes for Arcane Scientists [Caps], [Bracers], [Sleeves], [Sandals], [Trousers], [Gloves] and [Robes]. I must also suggest that you attempt your robe last due to the difficult nature of collecting the correct components.
        - Condition: `(e.other:Class() == "Enchanter" or e.other:Class() == "Magician" or e.other:Class() == "Wizard")`
        - Condition: `(e.message:findi("ready to begin"))`
        - Gives Enchanted Sewing Kit (17260).
      - Player: "Sleeve" (link: explicit mention)
        - NPC say: Sleeves will be a great and necessary addition to your armor. To create your sleeve material you will need to combine 2 Woven Spider Silks, 2 Bone Chips, 1 Spider Legs and Cloth Sleeves in your assembly kit. Once you have created the proper material take it to a loom along with this mold to fashion your very own Arcane Scientists Sleeves.
        - Condition: `(e.other:Class() == "Enchanter" or e.other:Class() == "Magician" or e.other:Class() == "Wizard")`
        - Condition: `(e.message:findi("sleeve"))`
        - Gives Enchanted Sleeves Pattern (22586).
      - Player: "Bracer" (link: explicit mention)
        - Prompted by player input: "Ready To Begin"
        - NPC say: A wise choice indeed, having the correct wrist protection is very important in spell channeling. To create your bracer material you will need to combine 1 Woven Spider Silk, 1 Desert Tarantula Chitin, 1 Armadillo Tooth and a Cloth wristband in your assembly kit. Once you have created the proper material take it to a loom along with this mold to fashion your very own Arcane Scientists Bracer.
        - Condition: `(e.other:Class() == "Enchanter" or e.other:Class() == "Magician" or e.other:Class() == "Wizard")`
        - Condition: `(e.message:findi("bracer"))`
        - Gives Enchanted Bracer Pattern (22584).
      - Player: "Cap" (link: explicit mention)
        - Prompted by player input: "Ready To Begin"
        - NPC say: A cap will keep you safe from any attackers as well as the elements. To create your cap material you will need to combine 2 Woven Spider Silks, 1 Snake Fang, 1 Chunk of Meat and a Cloth Cap in your assembly kit. Once you have created the proper material take it to a loom along with this mold to fashion your very own Arcane Scientists Cap.
        - Condition: `(e.other:Class() == "Enchanter" or e.other:Class() == "Magician" or e.other:Class() == "Wizard")`
        - Condition: `(e.message:findi("cap"))`
        - Gives Enchanted Cap Pattern (22583).
      - Player: "Glove" (link: explicit mention)
        - Prompted by player input: "Ready To Begin"
        - NPC say: Gloves are very important for your early training especially Isola. While you are learning your first set of incantations you should not have to worry about any injuries to your hands. To create your glove material you will need to combine 3 Woven Spider Silks, 1 Giant Scarab Brain, 1 High Quality Cat Pelt 1 Zombie Skin and 1 Large Leaf Scarab Leg in your assembly kit. Once you have created the proper material take it to a loom along with this mold to fashion your very own Arcane Scientists Gloves.
        - Condition: `(e.other:Class() == "Enchanter" or e.other:Class() == "Magician" or e.other:Class() == "Wizard")`
        - Condition: `(e.message:findi("glove"))`
        - Gives Enchanted Gloves Pattern (22588).
      - Player: "Sandal" (link: explicit mention)
        - Prompted by player input: "Ready To Begin"
        - NPC say: Sandals will keep you save from any harmful things you may walk in, it is a good idea to have them. To create your sandal material you will need to combine 3 Woven Spider Silks, 1 Coyote Pelt, 2 Black Bear Paws, 1 Urticating Hairs and Cloth Sandals in your assembly kit. Once you have created the proper material take it to a loom along with this mold to fashion your very own Arcane Scientists Sandals.
        - Condition: `(e.other:Class() == "Enchanter" or e.other:Class() == "Magician" or e.other:Class() == "Wizard")`
        - Condition: `(e.message:findi("sandal"))`
        - Gives Enchanted Sandals Pattern (22585).
      - Player: "Trouser" (link: explicit mention)
        - Prompted by player input: "Ready To Begin"
        - NPC say: I would always recommend pants to all my new students since they are a very important part of your armor set. To create your trouser material you will need to combine 4 Woven Spider Silks, 1 Embalming Dust, 1 Rotting Zombie Skull and 1 Armadillo Tail in your assembly kit. Once you have created the proper material take it to a loom along with this mold to fashion your very own Arcane Scientists Trousers.
        - Condition: `(e.other:Class() == "Enchanter" or e.other:Class() == "Magician" or e.other:Class() == "Wizard")`
        - Condition: `(e.message:findi("trouser"))`
        - Gives Enchanted Trousers Pattern (22587).
      - Player: "Robe" (link: explicit mention)
        - Prompted by player input: "Ready To Begin"
        - NPC say: I am very pleased to see that you have progressed through your armor pieces so quickly. I am also proud to see that you are ready to attempt your robe! To create your robe material you will need to combine 5 Woven Spider Silks, 1 Snake Bile, 1 Cutthroat Golden Tooth, 1 Shadow Wolf Tibia, 1 Orc Prayer Beads and 1 Cloth Shirt in your assembly kit. Once you have created the proper material take it to a loom along with this mold to fashion your very own Arcane Scientists Robe. Be sure to come back to see me for a [final assignment] after you have completed your robe.
        - Condition: `(e.other:Class() == "Enchanter" or e.other:Class() == "Magician" or e.other:Class() == "Wizard")`
        - Condition: `(e.message:findi("robe"))`
        - Gives Enchanted Robe Pattern (22589).
      - Player: "Final Assignment" (link: explicit mention)
        - NPC say: I have a trinket that was given to me by my mother a long time ago. Before she died I told her I would always keep it close to me. Recently, some militia officers came in to our academy and confiscated anything that appeared to be valuable. Fearing for my life I did not fight to keep the necklace my mother gave me. The officer that took it was named Teridsan. If you should find him you have my permission to kill him if that's what it takes to get my necklace back. Return to me when you have my necklace along with 2 Lion Teeth.
        - Condition: `(e.other:Class() == "Enchanter" or e.other:Class() == "Magician" or e.other:Class() == "Wizard")`
        - Condition: `(e.message:findi("final assignment"))`

6. abysmal/"Silanda Leafdew", hand "Mind Crystal" (62846). Sets `druid_epic` to `6`.
    - Hand in x1: "Mind Crystal" (62846).
    - Prerequisite: "Mind Crystal" (62846). See section 0.
    - Gives "Mind Crystal" (62846).
    - Dialogue with abysmal/"Silanda Leafdew":
      - Player: "Hail"
        - NPC say: Hi. It's a wonderful view. I'm not sure that it makes up for what we've [done] to get here, though.
        - Condition: `e.message:findi("hail")`
      - Player: "Stabilizer" (link: conversation sequence)
        - NPC say: A stabilizer? Well, there are several in nature. What do you need it for?
        - Condition: `qglobals["druid_epic"] ~= nil and qglobals["druid_epic"] == "5" and e.message:findi("stabilizer")`
      - Player: "I need to purify a Mind Crystal" (link: conversation sequence)
        - NPC say: Really? I have been consulted about the Mind Crystal, but I have not had the chance to see it yet. Please, let me see this crystal.
        - Condition: `qglobals["druid_epic"] ~= nil and qglobals["druid_epic"] == "5" and e.message:findi("I need to purify a Mind Crystal")`

7. abysmal/"Silanda Leafdew", hand "Clear Mind Crystal" (62857). Sets `druid_epic` to `7`.
    - Hand in x1: "Clear Mind Crystal" (62857).
    - Prerequisite: "Clear Mind Crystal" (62857). See section 0.
    - Gives "Clear Mind Crystal" (62857).

8. global/"Global Player", combine recipe 19892. Sets `druid_epic` to `8`.
    - `recipe:19892` is combined in Reinforced Aerated Pot (62861).
      - Prerequisite: "Reinforced Aerated Pot" (62861). See section 0.
      - Put in x1: Living Brambles Seed (62850).
        - Prerequisite: "Living Brambles Seed" (62850). See section 0.
      - Put in x1: Clear Mind Crystal (62857).
        - Prerequisite: "Clear Mind Crystal" (62857). See section 0.
      - Put in x1: Blackened Earth (62862).
        - Kill kithicor/"Blackened Tree Limb". Spawns "Blackened Dryad" (20301).
        - Loot "Blackened Earth" (62862) from "Blackened Dryad".
      - Produces Staff of Living Brambles (62863).
      - The combine does not fail.

9. abysmal/"Reyfin Malakwa", say "Hail". Sets `druid_epic` to `9`.
    - Requires `druid_epic` <9.
    - Dialogue with abysmal/"Reyfin Malakwa":
      - Player: "Hail"
        - NPC emote: stares silently out over the ocean towards the magical wards protecting the ship from the unyielding onslaught of the pounding waves. He jumps back terrorized when he realizes your presence. His visage calms a bit when he senses you mean him no immediate harm. He ponders you timidly for a moment and then leans down and begins drawing something in the sea grime that covers one of the boxes. You study his sketch for a moment and begin to understand that it is a rune of sorts. Three arching lines join in the center to form a sort of Y-shape.
        - NPC message: The bedraggled Taelosian refugee looks up at you after drawing the symbol and looks you directly in the eyes for the first time. He seems to draw strength from your presence and you sense that he feels the power of nature that you carry. He smiles weakly at you and then bends down and erases the symbol by smearing around the surrounding grime. He then draws a new symbol. This symbol is much more complicated, it is an arch with rods protruding from either side at the base. The rod to the right splits into four branches, the one on the left ends in a swirl. He looks up at you with a pleading look in his eyes as he hands you a small bag that appears to be made from his own clothing
          - Reply guard: `(plugin::check_hasitem($client, 62863))`
        - Condition: `($text=~/hail/i)`
        - Sets `druid_epic` to `9`.
        - Gives Ragged Cloth Bag (62881).

10. abysmal/"Reyfin Malakwa", hand "Wrapped Cloth Bag" (62882). Sets `druid_epic` to `10`.
    - Hand in x1: "Wrapped Cloth Bag" (62882).
    - Prerequisite: "Wrapped Cloth Bag" (62882). See section 0.
    - Gives "Rune of Yuisaha" (62868).

Alternative or repeat transition to `druid_epic` = `10` (not an additional required stage).

10. nedaria/"Historian Finrazel", hand "Rune of Yuisaha" (62868). Sets `druid_epic` to `10`.
    - Hand in x1: "Rune of Yuisaha" (62868).
    - Prerequisite: "Rune of Yuisaha" (62868). See section 0.
    - Dialogue with nedaria/"Historian Finrazel":
      - Player: "Plan To Find" (link: external event mention)
        - Prompted by `event_trade`:
          - NPC say: Well, this is an amazing find! I didn't think any of his runes survived the invasion.' The historian cleans the rune with a special solution, then hands it back to you. 'Let me tell you what I know of Yuisaha. He was a great rain spirit, perhaps the greatest patron of the Taelosians. He was manifested when the Muramites invaded Talosia so long ago. He was captured by the army and brought back to the Plane of Discord. What happened to Yuisaha then is hard to say, but there is a separate story of a powerful rain spirit that was frozen during a battle and shattered. The story claims that the frozen shards of the spirit were divided among the leaders of the winning army. Where they have gone since then, or if they still exist, nobody can tell. Do you really [plan to find] him?
          - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 62868}))`
        - NPC say: Then you'll need this. I use it to store magical potions, but it might work for holding frozen pieces of a greater rain spirit.' He shrugs. 'I hope so, anyway. I don't exactly see a lot of frozen rain spirits.' He smiles. 'I wish you luck, friend. Rescuing such a being would be a boon for all of Norrath.
        - Condition: `(e.message:findi("plan to find") and qglobals["druid_epic"] == "10")`
        - Gives Thick Leather Bag (62884).

11. nedaria/"Historian Finrazel", hand "Synched Leather Bag" (62885). Sets `druid_epic` to `11`.
    - Hand in x1: "Synched Leather Bag" (62885).
    - Prerequisite: "Synched Leather Bag" (62885). See section 0.
    - Gives "Synched Leather Bag" (62885).

12. abysmal/"Reyfin Malakwa", hand "Synched Leather Bag" (62885). Sets `druid_epic` to `12`.
    - Hand in x1: "Synched Leather Bag" (62885).
    - Prerequisite: "Synched Leather Bag" (62885). See section 0.
    - Gives "Synched Leather Bag" (62885).

13. global/"Global Player", combine recipe 19909. Sets `druid_epic` to `13`.
    - `recipe:19909` is combined in Insulated Container (62876).
      - Prerequisite: "Insulated Container" (62876). See section 0.
      - Put in x1: Essence of Rainfall (62883).
        - Given by global/"Global Player", combine recipe 19908.
      - Put in x1: Staff of Living Brambles (62863).
        - Prerequisite: "Staff of Living Brambles" (62863). See section 0.
      - Produces Staff of Everliving Brambles (62880).
      - The combine does not fail.

#### Steps on `druid_epic` that do not change it

- `abysmal` silanda leafdew, hand 62885 needs `druid_epic` set.
  - Turn in Synched Leather Bag (62885).
  - Gives Synched Leather Bag (62885).
  - Gives Insulated Container Sketch (62875).
- `burningwood` player, on enter needs `druid_epic` ==12.
  - Spawns a crippled wurm (87155).
  - Loots Polished Gear #1 (37029).
  - Loots Polished Gear #3 (37032).
  - Loots Uncut Combine Star (37845).
  - Loots Everburning Jagged Tree Limb (62879).
  - Loots Spotted Lava Rock (80010).
- `dranik` earthshaker trap, on enter needs `druid_epic` ==7.
  - Sets `druid_epic_dranik` to `1`.
  - Spawns a cracked earthshaker (336214).
  - Loots Chunk of Energized Clay (62859).
- `dranik` player, on loot needs `druid_epic` ==7.
  - Sets `druid_chest_dranik` to `1`.
  - Spawns a chest (Epic 1.5) (283157).
- `draniksscar` druid trap, on enter needs `druid_epic` ==10.
  - Spawns Tranlinor the Maimed (302086).
  - Loots Lucidem (35084).
  - Loots Versluierd Fungus (35087).
  - Loots Uncut Alexandrite (37847).
  - Loots Kyv Arrowhead (51921).
  - Loots Wind Shard (62873).
- `eastwastes` player, on enter needs `druid_epic` ==1.
  - Sets `druid_epic_ew` to `1`.
  - Spawns Ulthork Raider (116608).
  - Spawns an ulthork man o war (116066).
  - Loots Ulthork Tusks (24874).
  - Loots Ulthork Hide (30092).
  - Loots Ulthork Meat (30093).
  - Loots Ulthork Hide Legs (30123).
  - Loots Velium Long Sword (30200).
  - Loots Velium Dagger (30207).
  - Loots Velium Rapier (30209).
  - Loots Carved Prexus Totem (62821).
  - Loots Salil's Writ Pg. 174 (11714).
  - Loots Salil's Writ Pg. 282 (11716).
  - Loots Salil's Writ Pg. 288 (11719).
  - Loots Faded Salil's Writ Page (11721).
  - Loots Nilitim's Grimoire Pg. 35 (11722).
  - Loots Nilitim's Grimoire Pg. 36 (11723).
  - Loots Nilitim's Grimoire Pg. 115 (11724).
  - Loots Nilitim's Grimoire Pg. 116 (11725).
  - Loots Nilitim's Grimoire Pg. 300 (11726).
  - Loots Nilitim's Grimoire Pg. 301 (11727).
  - Loots Nilitim's Grimoire Pg. 351 (11728).
  - Loots Nilitim's Grimoire Pg. 352 (11729).
  - Loots Rune of Al'Kabor (11746).
  - Loots Rune of the Combine (11754).
  - Loots Rune of the Helix (11758).
  - Loots Rune of Petrification (11770).
  - Loots Rune of Paralysis (11772).
  - Loots Rune of Conception (11774).
  - Loots Rune of Infraction (11775).
  - Loots Rune of Rathe (11776).
  - Loots Rune of Attraction (11777).
  - Loots Rune of the Inverse (11778).
  - Loots Glove of Rallos Zek (11796).
  - Loots Flame of Vox (11797).
  - Loots The Scent of Marr (11802).
  - Loots Words of Collection (Azia) (11803).
  - Loots Words of Incarceration (11804).
  - Loots Essence of Rathe (11805).
  - Loots Tears of Prexus (11806).
  - Loots Words of the Suffering (11851).
  - Loots Words of Descrying (11852).
  - Loots Words of Seizure (11853).
  - Loots Words of Disillusionment (11854).
  - Loots Words of Projection (11855).
  - Loots Words of the Spectre (11856).
  - Loots Words of Bidding (11857).
  - Loots Words of Collection (Beza) (11858).
  - Loots Words of the Psyche (11861).
  - Loots Words of Burnishing (11862).
  - Loots Words of Obligation (11863).
  - Loots Words of Collection (Caza) (11864).
  - Loots Words of Convocation (11872).
  - Loots Words of Cazic-Thule (16039).
  - Loots Ulthork Tusks (24874).
  - Loots Ulthork Hide (30092).
  - Loots Ulthork Meat (30093).
  - Loots Walrus Tooth (30107).
  - Loots Ulthork Hide Legs (30123).
  - Loots Ulthork Hide Tunic (30126).
  - Loots Ulthork Hide Collar (30129).
  - Loots Velium Long Sword (30200).
  - Loots Velium Two Handed Sword (30201).
  - Loots Velium Short Sword (30202).
  - Loots Velium Scimitar (30203).
  - Loots Velium Warhammer (30204).
  - Loots Velium Morning Star (30205).
  - Loots Velium Great Staff (30206).
  - Loots Velium Dagger (30207).
  - Loots Velium Spear (30208).
  - Loots Velium Rapier (30209).
  - Loots Spell: Tumultuous Strength (30428).
  - Loots Spell: Ro's Fiery Sundering (30437).
  - Loots Spell: Turning of the Unnatural (30443).
  - Loots Sunshard Ore (33792).
  - Loots Pliant Loam (34878).
  - Loots Malleable Loam (34879).
  - Loots Supple Loam (34880).
  - Loots Bonded Loam (34882).
  - Loots Dry Marrow (34892).
  - Loots Damp Marrow (34893).
  - Loots Moist Marrow (34894).
  - Loots Hemic Marrow (34896).
  - Loots Thick Spinneret Fluid (34905).
  - Loots Crude Spinneret Fluid (34906).
  - Loots Natural Spinneret Fluid (34907).
  - Loots Simple Etched Rune (38667).
  - Loots Complex Platinum Silvered Rune (38691).
  - Loots Consigned Bite of the Shissar VI (44551).
  - Loots Raw Crimson Nihilite (58067).
- `feerrott` corrupted spirit, say show it needs `druid_epic` ==3.
  - Gives Disease Rune (62837).
- `harbingers` druid epic trap, on enter needs `druid_epic` ==5.
  - Sets `druid_epic_harb` to `1`.
  - Spawns Azibelle Spavin (335064).
  - Spawns Glenfire Telzir (335065).
  - Loots Sunshard Powder (35088).
  - Loots Bohab's Crystal Fragment (62886).
  - Loots Azibelle's Crystal Fragment (62887).
  - Loots Curzon (35085).
  - Loots Glenfire's Crystal Fragment (62888).
- `kithicor` player, on enter needs `druid_epic` ==7.
  - Spawns Blackened Treant (20299).
- `kithicor` player, on loot needs `druid_epic` ==7.
  - Sets `druid_chest_kith` to `1`.
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
- `lakeofillomen` player, on enter needs `druid_epic` ==1.
  - Sets `druid_epic_loio` to `1`.
  - Spawns a bloodgill forager (85234).
  - Spawns a bloodgill forager (85235).
  - Loots Opal (10030).
  - Loots Golden Pendant (10044).
  - Loots Crystallized Sulfur (16976).
  - Loots Bonded Loam (34882).
  - Loots Raw Crimson Nihilite (58067).
  - Loots Handful of Diseased Maiden's Hair (62825).
  - Loots Pearl Earring (10002).
  - Loots Pearl Ring (10003).
  - Loots Black Pearl (10012).
  - Loots Peridot (10028).
  - Loots Emerald (10029).
  - Loots Opal (10030).
  - Loots Jade Ring (10043).
  - Loots Golden Pendant (10044).
  - Loots Faded Salil's Writ Page (11712).
  - Loots Salil's Writ Pg. 153 (11713).
  - Loots Salil's Writ Pg. 174 (11714).
  - Loots Salil's Writ Pg. 174 (11715).
  - Loots Salil's Writ Pg. 282 (11716).
  - Loots Salil's Writ Pg. 288 (11719).
  - Loots Faded Salil's Writ Page (11720).
  - Loots Rune of Al'Kabor (11746).
  - Loots Rune of the Combine (11754).
  - Loots Rune of the Helix (11758).
  - Loots Rune of Petrification (11770).
  - Loots Rune of Tyranny (11771).
  - Loots Rune of Paralysis (11772).
  - Loots Rune of Embrace (11773).
  - Loots Rune of Conception (11774).
  - Loots Rune of Infraction (11775).
  - Loots Glove of Rallos Zek (11796).
  - Loots Flame of Vox (11797).
  - Loots Words of Collection (Azia) (11803).
  - Loots Words of the Suffering (11851).
  - Loots Words of Descrying (11852).
  - Loots Words of Seizure (11853).
  - Loots Words of Disillusionment (11854).
  - Loots Words of Projection (11855).
  - Loots Words of the Spectre (11856).
  - Loots Words of Bidding (11857).
  - Loots Words of Collection (Beza) (11858).
  - Loots Words of Convocation (11872).
  - Loots Harpoon of the Depths (11970).
  - Loots Ancient Coin (12936).
  - Loots Bloodgill Scales (14824).
  - Loots Words of Cazic-Thule (16039).
  - Loots Crystallized Sulfur (16976).
  - Loots Flawless Aquamarine (22505).
  - Loots Sunshard Dust (33790).
  - Loots Pliant Loam (34878).
  - Loots Malleable Loam (34879).
  - Loots Supple Loam (34880).
  - Loots Dry Marrow (34892).
  - Loots Damp Marrow (34893).
  - Loots Moist Marrow (34894).
  - Loots Thick Spinneret Fluid (34905).
  - Loots Crude Spinneret Fluid (34906).
  - Loots Natural Spinneret Fluid (34907).
  - Loots Simple Etched Rune (38667).
  - Loots Complex Platinum Silvered Rune (38691).
  - Loots Consigned Bite of the Shissar V (44550).
  - Loots Consigned Bite of the Shissar VI (44551).
  - Loots Petrified Bloodgill Eye (80378).
  - Loots Collector's Bloodgill Scale (84011).
- `natimbi` player, on loot needs `druid_epic` >5.
  - Sets `druid_chest_natimbi` to `1`.
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
- `nedaria` historian finrazel, say plan to find needs `druid_epic` ==10.
  - Gives Thick Leather Bag (62884).
- `northro` a madman, say still desire it needs `druid_epic` ==3.
  - Gives Soul Stone (62836).
- `northro` a madman, say will do needs `druid_epic` ==3.
  - Spawns a haunt (392104).
- `nro` a madman, say still desire it needs `druid_epic` ==3.
  - Gives Soul Stone (62836).
- `nro` a madman, say will do needs `druid_epic` ==3.
  - Spawns a haunt (392104).
- `pojustice` great bear, hand 62843 needs `druid_epic` ==4.
  - Turn in Niera's Research Notes (62843).
  - Gives Red Dogwood Seed (62844).
  - Gives Living Brambles Seed (62845).
- `poknowledge` pathfinder arelat, say worth it needs `druid_epic` ==2.
  - Gives Fresh Awakenings vol. 1 (62839).
  - Gives Fresh Awakenings vol. 2 (62840).
  - Gives Fresh Awakenings vol. 3 (62841).
- `qinimi` druid trap, on enter needs `druid_epic` ==10.
  - Sets `druid_qin` to `1`.
  - Spawns Mastruq Commander Gorlakt (281089).
  - Spawns Spiritlord Body (281091).
  - Spawns Spiritlord Mind (281090).
  - Loots Spirit Shard (62870).
  - Loots Spirit Summoner's Bag (67441).
  - Loots Mastruq Tongue (67587).
  - Loots Sunshard Powder (35088).
  - Loots Mastruq's Clawed Finger (67434).
  - Loots Ukun Summoning Idol (67443).
  - Loots Mastruq Tongue (67587).
- `qinimi` player, on loot needs `druid_epic` ==10.
  - Sets `druid_epic_qin` to `1`.
  - Spawns a chest (Epic 2.0) (893).
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
- `qrg` niera farbreeze, hand 62844+62845 needs `druid_epic` ==4.
  - Turn in Red Dogwood Seed (62844).
  - Turn in Living Brambles Seed (62845).
  - Gives Living Brambles Seed (62850).
  - Gives Mind Crystal (62846).
- `wallofslaughter` druid trap, on enter needs `druid_epic` ==10.
  - Sets `druid_wos` to `1`.
  - Spawns Retired Soldier (300096).
  - Spawns a nervous guardian (300097).
- `wallofslaughter` player, on loot needs `druid_epic` ==10.
  - Sets `druid_epic_wos` to `1`.
  - Spawns a chest (Epic 1.5) (893).

### Other flags touched along the way

- `druid_epic_dranik` set to 1 at dranik/earthshaker trap.
- `druid_epic_ew` set to 1 at eastwastes/player.
- `druid_epic_harb` set to 1 at harbingers/druid epic trap.
- `druid_epic_loio` set to 1 at lakeofillomen/player.
- `druid_epic_natimbi` set to 1 at natimbi/player.
- `druid_epic_qin` set to 1 at qinimi/player.
- `druid_epic_wos` set to 1 at wallofslaughter/player.
