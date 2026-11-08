# Warrior

Steps taken from the quest graph only. **Broken** means the graph has no edge for that value or that item.

Flags with writes: `warrior_pre`, `warrior_epic`.

## 0. Prerequisites

Each list is the order you obtain that item. Later steps point here instead of repeating the chain.

### "Emblazoned Champion's Hilt" (60288)

1. Unresolved cyclic prerequisite: `warrior_pre` ==3.
2. draniksscar/"Korbuk Brimblade", hand "Emblazoned Champion's Hilt" (60288). Sets `warrior_pre` to `4`.
3. Loot "Korbuk's Weapon Plans" (60285) from "The Diaku Overseer" in `potactics`.
4. Loot "Elegant Shank" (60286) from "Shoqui the Forgotten" in `hatesfury`.
5. thurgadina/"Dardek Bladewright", hand "Korbuk's Weapon Plans" (60285) + "Elegant Shank" (60286) + "Emblazoned Champion's Hilt" (60288). Sets `warrior_pre` to `5`.
6. thurgadina/"Dardek Bladewright", hand "Korbuk's Weapon Plans" (60285) + "Elegant Shank" (60286) + "Emblazoned Champion's Hilt" (60288). Requires `warrior_pre` ==4. Gives "Dardek's Forged Blade" (60292).
7. draniksscar/"Korbuk Brimblade", hand "Dardek's Forged Blade" (60292). Sets `warrior_pre` to `6`.
8. freeporteast/"Kargek Redblade", say "Favor". Gives "Wax Sealed Note" (20673).
9. feerrott/"Oknoggin Stonesmacker", hand "Wax Sealed Note" (20673). Gives "Tiny Lute" (20674).
10. freeporteast/"Kargek Redblade", hand "Tiny Lute" (20674). Gives "Redblade's Legacy" (18083).
11. eastkarana/"Tenal Redblade", hand "Redblade's Legacy" (18083). Gives "Totem of the Freezing War" (20680).
12. Loot "Heart of Frost" (10549) from "A Goblin Wizard" in `permafrost`.
13. eastkarana/"Tenal Redblade", hand "Heart of Frost" (10549) + "Totem of the Freezing War" (20680). Gives "Totem of Fiery War" (20681).
14. Loot "Red Dragon Scales" (11622) from "Echo of Nortlav" in `hole`.
15. Loot "Red Dragon Scales" (11622) from "Lord Nagafen" in `soldungb`.
16. Loot "Red Dragon Scales" (11622) from "Melalafen" in `westwastes`.
17. Loot "Red Dragon Scales" (11622) from "Talendor" in `skyfire`.
18. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
19. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `steamfont`.
20. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `tox`.
21. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `toxxulia`.
22. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
23. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). The combine does not fail.
24. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
25. northro/"Verrell Cogswin", hand "Water Flask" (13006). Sets `Green_Scale_Quest` to `1`.
26. northro/"Verrell Cogswin", hand "Red Dragon Scales" (11622). Sets `Green_Scale_Quest` to `2`.
27. northro/"Verrell Cogswin", say "Adhesive". Requires `Green_Scale_Quest` ==2. Requires `Green_Scale_Quest` set. Gives "Verrell's Box of Potions" (67387).
28. Loot "Fractured Centaur Hoof" (67388) from "Centaur Archer" in `southkarana`.
29. Loot "Fractured Centaur Hoof" (67388) from "Centaur Charger" in `southkarana`.
30. Loot "Fractured Centaur Hoof" (67388) from "Centaur Courser" in `southkarana`.
31. Loot "Fractured Centaur Hoof" (67388) from "Centaur Foal" in `southkarana`.
32. Loot "Fractured Centaur Hoof" (67388) from "Centaur Sheltie" in `southkarana`.
33. Loot "Fire Giant Embers" (67389) from "A Fire Giant Warlord" (NPC 278023) in `soldungc`. Drop cache: 28.35% chance per kill.
34. Loot "Jagged Permafrost Shards" (67390) from "The Chilling Terror" in `permafrost`.
35. Combine in Oven (15): "Fractured Centaur Hoof" (67388), "Fire Giant Embers" (67389), "Jagged Permafrost Shards" (67390). Produces "Glue Powder" (67391). Requires Baking. The combine does not fail.
36. Common item: Barley (16590). Listed in 28 zones.
37. Common item: Deep Fungus Mold (67393). Listed in 28 zones.
38. Common item: Distilled Spirits (67394). Listed in 28 zones.
39. Combine in Brew Barrel (19): "Barley" (16590), "Deep Fungus Mold" (67393), "Distilled Spirits" (67394). Produces "Deep Barley Brew" (67392). Requires Brewing, trivial 110.
40. northro/"Verrell Cogswin", say "Adhesive". Requires `Green_Scale_Quest` ==2. Requires `Green_Scale_Quest` set. Gives "Potion Vial" (67395).
41. Combine in "Verrell's Box of Potions" (67387): "Glue Powder" (67391), "Deep Barley Brew" (67392), "Potion Vial" (67395). Produces "Thick Adhesive" (67386). The combine does not fail.
42. northro/"Verrell Cogswin", hand "Thick Adhesive" (67386). Gives "Grey Scale Pieces" (67385).
43. northro/"Verrell Cogswin", hand "Thick Adhesive" (67386). Gives "Thick Adhesive" (67396).
44. Combine in "Verrell's Box of Potions" (67387): "Grey Scale Pieces" (67385), "Thick Adhesive" (67396). Produces "Grey Colored Scales" (67384). The combine does not fail.
45. northro/"Verrell Cogswin", hand "Grey Colored Scales" (67384). Gives "Green Dragon Scales" (11582).
46. eastkarana/"Tenal Redblade", hand "Green Dragon Scales" (11582) + "Red Dragon Scales" (11622) + "Totem of Fiery War" (20681). Gives "Mark of the Sword" (20683).
47. Loot "Hand of the Maestro" (20676) from "Hand of the Maestro" in `hateplane`.
48. Loot "Hand of the Maestro" (20676) from "Hand of the Maestro" in `hateplaneb`.
49. eastkarana/"Tenal Redblade", hand "Hand of the Maestro" (20676) + "Mark of the Sword" (20683). Gives "Tenal's note to Kargek" (20684).
50. Loot "Spiroc Wingblade" (20679) from "The Spiroc Lord" in `airplane`.
51. freeporteast/"Kargek Redblade", hand "Spiroc Wingblade" (20679) + "Tenal's note to Kargek" (20684). Gives "Red Scabbard" (17859).
52. Combine in "Red Scabbard" (17859): "Jagged Blade of War" (10908). Produces "Blade of Tactics" (10909), "Blade of Strategy" (10910). The combine does not fail.
53. Combine in "Red Scabbard" (17859): "Blade of Tactics" (10909), "Blade of Strategy" (10910). Produces "Jagged Blade of War" (10908). The combine does not fail.
54. lakerathe/"Triathalon Swim Goggles", say "Hail". Gives "Rebreather" (16889).
55. Loot "Block of Permafrost" (20665) from "Lady Vox" in `permafrost`.
56. Loot "Block of Permafrost" (20665) from "An Ice Giant" in `permafrost`.
57. Common item: Keg of Vox Tail Ale (20664). Listed in 13 zones.
58. oceanoftears/"Denken Strongpick", hand "Rebreather" (16889) + "Keg of Vox Tail Ale" (20664) + "Block of Permafrost" (20665). Gives "Ancient Sword Blade" (20667).
59. Loot "Ancient Blade" (20670) from "Queen Velazul Di'zok" in `chardok`.
60. Ground spawn of "Unjeweled Dragon Head Hilt" (20668) in `lakerathe`.
61. Loot "Apothic Crown" (1239) from "Magi P'Tasa" (NPC 186157) in `hateplaneb`. Drop cache: 19.16% chance per kill.
62. poknowledge/"Arch Mage Deidus", hand "Apothic Crown" (1239). Gives "Diamond" (10037).
63. Loot "Scroll of the Ox" (49007) from "A Sturdy Chest" in `stillmoona`.
64. Loot "Scroll of the Boar" (49008) from "A Sturdy Chest" in `stillmoona`.
65. Loot "Scroll of the Dragon" (49009) from "A Sturdy Chest" in `stillmoona`.
66. Loot "Scroll of the Tiger" (49010) from "A Sturdy Chest" in `stillmoona`.
67. Hand "Scroll of the Ox" (49007) + "Scroll of the Boar" (49008) + "Scroll of the Dragon" (49009) + "Scroll of the Tiger" (49010) to stillmoona/"The Keeper Of Strength". Spawns "A Spirit Keeper" (338169). Loot "Black Sapphire" (10036) from "A Spirit Keeper".
68. 42 alternative loot source(s) also yield Black Sapphire (10036).
69. Say "Tm Devrak Death" to rujd/"Rujd".
70. Spawns "spawn chest with Heavy Orcish Prison Key" (245241).
71. Loot "Heavy Orcish Prison Key" (59571) from "spawn chest with Heavy Orcish Prison Key".
72. 2 alternative loot source(s) also yield Heavy Orcish Prison Key (59571).
73. Hand "Heavy Orcish Prison Key" (59571) to rujd/"Rujd". Spawns "Prison Guard Talkor" (245290). Loot "Jacinth" (10053) from "Prison Guard Talkor".
74. 54 alternative loot source(s) also yield Jacinth (10053).
75. freeporteast/"Wenden Blackhammer", hand "Black Sapphire" (10036) + "Diamond" (10037) + "Jacinth" (10053) + "Unjeweled Dragon Head Hilt" (20668). Gives "Jeweled Dragon Head Hilt" (20671).
76. Ground spawn of "Severely Damaged Dragon Head Hilt" (20669) in `timorous`.
77. Loot "Giant Sized Monocle" (20678) from "A Mountain Giant Patriarch" in `dreadlands`.
78. frontiermtns/"Mentrax Mountainbone", hand "Giant Sized Monocle" (20678). Gives "Rejesiam Ore" (20666).
79. Loot "Ball of Everliving Golem" (20677) from "Dread" in `fearplane`.
80. Loot "Ball of Everliving Golem" (20677) from "Fright" in `fearplane`.
81. Loot "Ball of Everliving Golem" (20677) from "Terror" in `fearplane`.
82. freeporteast/"Wenden Blackhammer", hand "Rejesiam Ore" (20666) + "Severely Damaged Dragon Head Hilt" (20669) + "Ball of Everliving Golem" (20677). Gives "Finely Crafted Dragon Head Hilt" (20672).
83. Combine in "Red Scabbard" (17859): "Ancient Sword Blade" (20667), "Ancient Blade" (20670), "Jeweled Dragon Head Hilt" (20671), "Finely Crafted Dragon Head Hilt" (20672). Produces "Jagged Blade of War" (10908). The combine does not fail.
84. freeporteast/"Gartrog Smitehammer", hand "Jagged Blade of War" (10908) + "Red Scabbard" (17859). Gives "Red Scabbard" (17869).
85. freeporteast/"Gartrog Smitehammer", hand "Jagged Blade of War" (10908) + "Red Scabbard" (17859). Gives "Jagged Blade of War" (66175).
86. Combine in "Red Scabbard" (17869): "Jagged Blade of War" (66175). Produces "Blade of Tactics" (66176), "Blade of Strategy" (66177). Requires Pottery. The combine does not fail.
87. draniksscar/"Korbuk Brimblade", say "Work". Sets `warrior_pre` to `1`.
88. draniksscar/"Korbuk Brimblade", hand "Korbuk's Weapon Plans" (60285). Sets `warrior_pre` to `2`.
89. draniksscar/"Korbuk Brimblade", hand "Elegant Shank" (60286). Sets `warrior_pre` to `3`.
90. Loot "Redblade Family Sword" (60287) from "Drevlon Knacknabber" in `eastkarana`.
91. freeporteast/"Kargek Redblade", hand "Redblade Family Sword" (60287). Requires `warrior_pre` set. Requires `warrior_pre` ==3. Gives "Emblazoned Champion's Hilt" (60288).

### "Dardek's Forged Blade" (60292)

1. Unresolved cyclic prerequisite: `warrior_pre` ==4.
2. Loot "Korbuk's Weapon Plans" (60285) from "The Diaku Overseer" in `potactics`.
3. Loot "Elegant Shank" (60286) from "Shoqui the Forgotten" in `hatesfury`.
4. Unresolved cyclic prerequisite: `warrior_pre` ==3.
5. draniksscar/"Korbuk Brimblade", hand "Emblazoned Champion's Hilt" (60288). Sets `warrior_pre` to `4`.
6. thurgadina/"Dardek Bladewright", hand "Korbuk's Weapon Plans" (60285) + "Elegant Shank" (60286) + "Emblazoned Champion's Hilt" (60288). Sets `warrior_pre` to `5`.
7. draniksscar/"Korbuk Brimblade", hand "Dardek's Forged Blade" (60292). Sets `warrior_pre` to `6`.
8. freeporteast/"Kargek Redblade", say "Favor". Gives "Wax Sealed Note" (20673).
9. feerrott/"Oknoggin Stonesmacker", hand "Wax Sealed Note" (20673). Gives "Tiny Lute" (20674).
10. freeporteast/"Kargek Redblade", hand "Tiny Lute" (20674). Gives "Redblade's Legacy" (18083).
11. eastkarana/"Tenal Redblade", hand "Redblade's Legacy" (18083). Gives "Totem of the Freezing War" (20680).
12. Loot "Heart of Frost" (10549) from "A Goblin Wizard" in `permafrost`.
13. eastkarana/"Tenal Redblade", hand "Heart of Frost" (10549) + "Totem of the Freezing War" (20680). Gives "Totem of Fiery War" (20681).
14. Loot "Red Dragon Scales" (11622) from "Echo of Nortlav" in `hole`.
15. Loot "Red Dragon Scales" (11622) from "Lord Nagafen" in `soldungb`.
16. Loot "Red Dragon Scales" (11622) from "Melalafen" in `westwastes`.
17. Loot "Red Dragon Scales" (11622) from "Talendor" in `skyfire`.
18. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
19. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `steamfont`.
20. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `tox`.
21. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `toxxulia`.
22. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
23. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). The combine does not fail.
24. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
25. northro/"Verrell Cogswin", hand "Water Flask" (13006). Sets `Green_Scale_Quest` to `1`.
26. northro/"Verrell Cogswin", hand "Red Dragon Scales" (11622). Sets `Green_Scale_Quest` to `2`.
27. northro/"Verrell Cogswin", say "Adhesive". Requires `Green_Scale_Quest` ==2. Requires `Green_Scale_Quest` set. Gives "Verrell's Box of Potions" (67387).
28. Loot "Fractured Centaur Hoof" (67388) from "Centaur Archer" in `southkarana`.
29. Loot "Fractured Centaur Hoof" (67388) from "Centaur Charger" in `southkarana`.
30. Loot "Fractured Centaur Hoof" (67388) from "Centaur Courser" in `southkarana`.
31. Loot "Fractured Centaur Hoof" (67388) from "Centaur Foal" in `southkarana`.
32. Loot "Fractured Centaur Hoof" (67388) from "Centaur Sheltie" in `southkarana`.
33. Loot "Fire Giant Embers" (67389) from "A Fire Giant Warlord" (NPC 278023) in `soldungc`. Drop cache: 28.35% chance per kill.
34. Loot "Jagged Permafrost Shards" (67390) from "The Chilling Terror" in `permafrost`.
35. Combine in Oven (15): "Fractured Centaur Hoof" (67388), "Fire Giant Embers" (67389), "Jagged Permafrost Shards" (67390). Produces "Glue Powder" (67391). Requires Baking. The combine does not fail.
36. Common item: Barley (16590). Listed in 28 zones.
37. Common item: Deep Fungus Mold (67393). Listed in 28 zones.
38. Common item: Distilled Spirits (67394). Listed in 28 zones.
39. Combine in Brew Barrel (19): "Barley" (16590), "Deep Fungus Mold" (67393), "Distilled Spirits" (67394). Produces "Deep Barley Brew" (67392). Requires Brewing, trivial 110.
40. northro/"Verrell Cogswin", say "Adhesive". Requires `Green_Scale_Quest` ==2. Requires `Green_Scale_Quest` set. Gives "Potion Vial" (67395).
41. Combine in "Verrell's Box of Potions" (67387): "Glue Powder" (67391), "Deep Barley Brew" (67392), "Potion Vial" (67395). Produces "Thick Adhesive" (67386). The combine does not fail.
42. northro/"Verrell Cogswin", hand "Thick Adhesive" (67386). Gives "Grey Scale Pieces" (67385).
43. northro/"Verrell Cogswin", hand "Thick Adhesive" (67386). Gives "Thick Adhesive" (67396).
44. Combine in "Verrell's Box of Potions" (67387): "Grey Scale Pieces" (67385), "Thick Adhesive" (67396). Produces "Grey Colored Scales" (67384). The combine does not fail.
45. northro/"Verrell Cogswin", hand "Grey Colored Scales" (67384). Gives "Green Dragon Scales" (11582).
46. eastkarana/"Tenal Redblade", hand "Green Dragon Scales" (11582) + "Red Dragon Scales" (11622) + "Totem of Fiery War" (20681). Gives "Mark of the Sword" (20683).
47. Loot "Hand of the Maestro" (20676) from "Hand of the Maestro" in `hateplane`.
48. Loot "Hand of the Maestro" (20676) from "Hand of the Maestro" in `hateplaneb`.
49. eastkarana/"Tenal Redblade", hand "Hand of the Maestro" (20676) + "Mark of the Sword" (20683). Gives "Tenal's note to Kargek" (20684).
50. Loot "Spiroc Wingblade" (20679) from "The Spiroc Lord" in `airplane`.
51. freeporteast/"Kargek Redblade", hand "Spiroc Wingblade" (20679) + "Tenal's note to Kargek" (20684). Gives "Red Scabbard" (17859).
52. Combine in "Red Scabbard" (17859): "Jagged Blade of War" (10908). Produces "Blade of Tactics" (10909), "Blade of Strategy" (10910). The combine does not fail.
53. Combine in "Red Scabbard" (17859): "Blade of Tactics" (10909), "Blade of Strategy" (10910). Produces "Jagged Blade of War" (10908). The combine does not fail.
54. lakerathe/"Triathalon Swim Goggles", say "Hail". Gives "Rebreather" (16889).
55. Loot "Block of Permafrost" (20665) from "Lady Vox" in `permafrost`.
56. Loot "Block of Permafrost" (20665) from "An Ice Giant" in `permafrost`.
57. Common item: Keg of Vox Tail Ale (20664). Listed in 13 zones.
58. oceanoftears/"Denken Strongpick", hand "Rebreather" (16889) + "Keg of Vox Tail Ale" (20664) + "Block of Permafrost" (20665). Gives "Ancient Sword Blade" (20667).
59. Loot "Ancient Blade" (20670) from "Queen Velazul Di'zok" in `chardok`.
60. Ground spawn of "Unjeweled Dragon Head Hilt" (20668) in `lakerathe`.
61. Loot "Apothic Crown" (1239) from "Magi P'Tasa" (NPC 186157) in `hateplaneb`. Drop cache: 19.16% chance per kill.
62. poknowledge/"Arch Mage Deidus", hand "Apothic Crown" (1239). Gives "Diamond" (10037).
63. Loot "Scroll of the Ox" (49007) from "A Sturdy Chest" in `stillmoona`.
64. Loot "Scroll of the Boar" (49008) from "A Sturdy Chest" in `stillmoona`.
65. Loot "Scroll of the Dragon" (49009) from "A Sturdy Chest" in `stillmoona`.
66. Loot "Scroll of the Tiger" (49010) from "A Sturdy Chest" in `stillmoona`.
67. Hand "Scroll of the Ox" (49007) + "Scroll of the Boar" (49008) + "Scroll of the Dragon" (49009) + "Scroll of the Tiger" (49010) to stillmoona/"The Keeper Of Strength". Spawns "A Spirit Keeper" (338169). Loot "Black Sapphire" (10036) from "A Spirit Keeper".
68. 42 alternative loot source(s) also yield Black Sapphire (10036).
69. Say "Tm Devrak Death" to rujd/"Rujd".
70. Spawns "spawn chest with Heavy Orcish Prison Key" (245241).
71. Loot "Heavy Orcish Prison Key" (59571) from "spawn chest with Heavy Orcish Prison Key".
72. 2 alternative loot source(s) also yield Heavy Orcish Prison Key (59571).
73. Hand "Heavy Orcish Prison Key" (59571) to rujd/"Rujd". Spawns "Prison Guard Talkor" (245290). Loot "Jacinth" (10053) from "Prison Guard Talkor".
74. 54 alternative loot source(s) also yield Jacinth (10053).
75. freeporteast/"Wenden Blackhammer", hand "Black Sapphire" (10036) + "Diamond" (10037) + "Jacinth" (10053) + "Unjeweled Dragon Head Hilt" (20668). Gives "Jeweled Dragon Head Hilt" (20671).
76. Ground spawn of "Severely Damaged Dragon Head Hilt" (20669) in `timorous`.
77. Loot "Giant Sized Monocle" (20678) from "A Mountain Giant Patriarch" in `dreadlands`.
78. frontiermtns/"Mentrax Mountainbone", hand "Giant Sized Monocle" (20678). Gives "Rejesiam Ore" (20666).
79. Loot "Ball of Everliving Golem" (20677) from "Dread" in `fearplane`.
80. Loot "Ball of Everliving Golem" (20677) from "Fright" in `fearplane`.
81. Loot "Ball of Everliving Golem" (20677) from "Terror" in `fearplane`.
82. freeporteast/"Wenden Blackhammer", hand "Rejesiam Ore" (20666) + "Severely Damaged Dragon Head Hilt" (20669) + "Ball of Everliving Golem" (20677). Gives "Finely Crafted Dragon Head Hilt" (20672).
83. Combine in "Red Scabbard" (17859): "Ancient Sword Blade" (20667), "Ancient Blade" (20670), "Jeweled Dragon Head Hilt" (20671), "Finely Crafted Dragon Head Hilt" (20672). Produces "Jagged Blade of War" (10908). The combine does not fail.
84. freeporteast/"Gartrog Smitehammer", hand "Jagged Blade of War" (10908) + "Red Scabbard" (17859). Gives "Red Scabbard" (17869).
85. freeporteast/"Gartrog Smitehammer", hand "Jagged Blade of War" (10908) + "Red Scabbard" (17859). Gives "Jagged Blade of War" (66175).
86. Combine in "Red Scabbard" (17869): "Jagged Blade of War" (66175). Produces "Blade of Tactics" (66176), "Blade of Strategy" (66177). Requires Pottery. The combine does not fail.
87. draniksscar/"Korbuk Brimblade", say "Work". Sets `warrior_pre` to `1`.
88. draniksscar/"Korbuk Brimblade", hand "Korbuk's Weapon Plans" (60285). Sets `warrior_pre` to `2`.
89. draniksscar/"Korbuk Brimblade", hand "Elegant Shank" (60286). Sets `warrior_pre` to `3`.
90. Loot "Redblade Family Sword" (60287) from "Drevlon Knacknabber" in `eastkarana`.
91. freeporteast/"Kargek Redblade", hand "Redblade Family Sword" (60287). Requires `warrior_pre` set. Requires `warrior_pre` ==3. Gives "Emblazoned Champion's Hilt" (60288).
92. thurgadina/"Dardek Bladewright", hand "Korbuk's Weapon Plans" (60285) + "Elegant Shank" (60286) + "Emblazoned Champion's Hilt" (60288). Requires `warrior_pre` ==4. Gives "Dardek's Forged Blade" (60292).

### "Blade of Strategy" (10910)

1. freeporteast/"Kargek Redblade", say "Favor". Gives "Wax Sealed Note" (20673).
2. feerrott/"Oknoggin Stonesmacker", hand "Wax Sealed Note" (20673). Gives "Tiny Lute" (20674).
3. freeporteast/"Kargek Redblade", hand "Tiny Lute" (20674). Gives "Redblade's Legacy" (18083).
4. eastkarana/"Tenal Redblade", hand "Redblade's Legacy" (18083). Gives "Totem of the Freezing War" (20680).
5. Loot "Heart of Frost" (10549) from "A Goblin Wizard" in `permafrost`.
6. eastkarana/"Tenal Redblade", hand "Heart of Frost" (10549) + "Totem of the Freezing War" (20680). Gives "Totem of Fiery War" (20681).
7. Loot "Red Dragon Scales" (11622) from "Echo of Nortlav" in `hole`.
8. Loot "Red Dragon Scales" (11622) from "Lord Nagafen" in `soldungb`.
9. Loot "Red Dragon Scales" (11622) from "Melalafen" in `westwastes`.
10. Loot "Red Dragon Scales" (11622) from "Talendor" in `skyfire`.
11. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
12. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `steamfont`.
13. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `tox`.
14. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `toxxulia`.
15. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
16. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). The combine does not fail.
17. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
18. northro/"Verrell Cogswin", hand "Water Flask" (13006). Sets `Green_Scale_Quest` to `1`.
19. northro/"Verrell Cogswin", hand "Red Dragon Scales" (11622). Sets `Green_Scale_Quest` to `2`.
20. northro/"Verrell Cogswin", say "Adhesive". Requires `Green_Scale_Quest` ==2. Requires `Green_Scale_Quest` set. Gives "Verrell's Box of Potions" (67387).
21. Loot "Fractured Centaur Hoof" (67388) from "Centaur Archer" in `southkarana`.
22. Loot "Fractured Centaur Hoof" (67388) from "Centaur Charger" in `southkarana`.
23. Loot "Fractured Centaur Hoof" (67388) from "Centaur Courser" in `southkarana`.
24. Loot "Fractured Centaur Hoof" (67388) from "Centaur Foal" in `southkarana`.
25. Loot "Fractured Centaur Hoof" (67388) from "Centaur Sheltie" in `southkarana`.
26. Loot "Fire Giant Embers" (67389) from "A Fire Giant Warlord" (NPC 278023) in `soldungc`. Drop cache: 28.35% chance per kill.
27. Loot "Jagged Permafrost Shards" (67390) from "The Chilling Terror" in `permafrost`.
28. Combine in Oven (15): "Fractured Centaur Hoof" (67388), "Fire Giant Embers" (67389), "Jagged Permafrost Shards" (67390). Produces "Glue Powder" (67391). Requires Baking. The combine does not fail.
29. Common item: Barley (16590). Listed in 28 zones.
30. Common item: Deep Fungus Mold (67393). Listed in 28 zones.
31. Common item: Distilled Spirits (67394). Listed in 28 zones.
32. Combine in Brew Barrel (19): "Barley" (16590), "Deep Fungus Mold" (67393), "Distilled Spirits" (67394). Produces "Deep Barley Brew" (67392). Requires Brewing, trivial 110.
33. northro/"Verrell Cogswin", say "Adhesive". Requires `Green_Scale_Quest` ==2. Requires `Green_Scale_Quest` set. Gives "Potion Vial" (67395).
34. Combine in "Verrell's Box of Potions" (67387): "Glue Powder" (67391), "Deep Barley Brew" (67392), "Potion Vial" (67395). Produces "Thick Adhesive" (67386). The combine does not fail.
35. northro/"Verrell Cogswin", hand "Thick Adhesive" (67386). Gives "Grey Scale Pieces" (67385).
36. northro/"Verrell Cogswin", hand "Thick Adhesive" (67386). Gives "Thick Adhesive" (67396).
37. Combine in "Verrell's Box of Potions" (67387): "Grey Scale Pieces" (67385), "Thick Adhesive" (67396). Produces "Grey Colored Scales" (67384). The combine does not fail.
38. northro/"Verrell Cogswin", hand "Grey Colored Scales" (67384). Gives "Green Dragon Scales" (11582).
39. eastkarana/"Tenal Redblade", hand "Green Dragon Scales" (11582) + "Red Dragon Scales" (11622) + "Totem of Fiery War" (20681). Gives "Mark of the Sword" (20683).
40. Loot "Hand of the Maestro" (20676) from "Hand of the Maestro" in `hateplane`.
41. Loot "Hand of the Maestro" (20676) from "Hand of the Maestro" in `hateplaneb`.
42. eastkarana/"Tenal Redblade", hand "Hand of the Maestro" (20676) + "Mark of the Sword" (20683). Gives "Tenal's note to Kargek" (20684).
43. Loot "Spiroc Wingblade" (20679) from "The Spiroc Lord" in `airplane`.
44. freeporteast/"Kargek Redblade", hand "Spiroc Wingblade" (20679) + "Tenal's note to Kargek" (20684). Gives "Red Scabbard" (17859).
45. lakerathe/"Triathalon Swim Goggles", say "Hail". Gives "Rebreather" (16889).
46. Loot "Block of Permafrost" (20665) from "Lady Vox" in `permafrost`.
47. Loot "Block of Permafrost" (20665) from "An Ice Giant" in `permafrost`.
48. Common item: Keg of Vox Tail Ale (20664). Listed in 13 zones.
49. oceanoftears/"Denken Strongpick", hand "Rebreather" (16889) + "Keg of Vox Tail Ale" (20664) + "Block of Permafrost" (20665). Gives "Ancient Sword Blade" (20667).
50. Loot "Ancient Blade" (20670) from "Queen Velazul Di'zok" in `chardok`.
51. Ground spawn of "Unjeweled Dragon Head Hilt" (20668) in `lakerathe`.
52. Loot "Apothic Crown" (1239) from "Magi P'Tasa" (NPC 186157) in `hateplaneb`. Drop cache: 19.16% chance per kill.
53. poknowledge/"Arch Mage Deidus", hand "Apothic Crown" (1239). Gives "Diamond" (10037).
54. Loot "Scroll of the Ox" (49007) from "A Sturdy Chest" in `stillmoona`.
55. Loot "Scroll of the Boar" (49008) from "A Sturdy Chest" in `stillmoona`.
56. Loot "Scroll of the Dragon" (49009) from "A Sturdy Chest" in `stillmoona`.
57. Loot "Scroll of the Tiger" (49010) from "A Sturdy Chest" in `stillmoona`.
58. Hand "Scroll of the Ox" (49007) + "Scroll of the Boar" (49008) + "Scroll of the Dragon" (49009) + "Scroll of the Tiger" (49010) to stillmoona/"The Keeper Of Strength". Spawns "A Spirit Keeper" (338169). Loot "Black Sapphire" (10036) from "A Spirit Keeper".
59. 42 alternative loot source(s) also yield Black Sapphire (10036).
60. Say "Tm Devrak Death" to rujd/"Rujd".
61. Spawns "spawn chest with Heavy Orcish Prison Key" (245241).
62. Loot "Heavy Orcish Prison Key" (59571) from "spawn chest with Heavy Orcish Prison Key".
63. 2 alternative loot source(s) also yield Heavy Orcish Prison Key (59571).
64. Hand "Heavy Orcish Prison Key" (59571) to rujd/"Rujd". Spawns "Prison Guard Talkor" (245290). Loot "Jacinth" (10053) from "Prison Guard Talkor".
65. 54 alternative loot source(s) also yield Jacinth (10053).
66. freeporteast/"Wenden Blackhammer", hand "Black Sapphire" (10036) + "Diamond" (10037) + "Jacinth" (10053) + "Unjeweled Dragon Head Hilt" (20668). Gives "Jeweled Dragon Head Hilt" (20671).
67. Ground spawn of "Severely Damaged Dragon Head Hilt" (20669) in `timorous`.
68. Loot "Giant Sized Monocle" (20678) from "A Mountain Giant Patriarch" in `dreadlands`.
69. frontiermtns/"Mentrax Mountainbone", hand "Giant Sized Monocle" (20678). Gives "Rejesiam Ore" (20666).
70. Loot "Ball of Everliving Golem" (20677) from "Dread" in `fearplane`.
71. Loot "Ball of Everliving Golem" (20677) from "Fright" in `fearplane`.
72. Loot "Ball of Everliving Golem" (20677) from "Terror" in `fearplane`.
73. freeporteast/"Wenden Blackhammer", hand "Rejesiam Ore" (20666) + "Severely Damaged Dragon Head Hilt" (20669) + "Ball of Everliving Golem" (20677). Gives "Finely Crafted Dragon Head Hilt" (20672).
74. Combine in "Red Scabbard" (17859): "Ancient Sword Blade" (20667), "Ancient Blade" (20670), "Jeweled Dragon Head Hilt" (20671), "Finely Crafted Dragon Head Hilt" (20672). Produces "Jagged Blade of War" (10908). The combine does not fail.
75. Combine in "Red Scabbard" (17859): "Jagged Blade of War" (10908). Produces "Blade of Tactics" (10909), "Blade of Strategy" (10910). The combine does not fail.

### "Blade of Tactics" (10909)

1. freeporteast/"Kargek Redblade", say "Favor". Gives "Wax Sealed Note" (20673).
2. feerrott/"Oknoggin Stonesmacker", hand "Wax Sealed Note" (20673). Gives "Tiny Lute" (20674).
3. freeporteast/"Kargek Redblade", hand "Tiny Lute" (20674). Gives "Redblade's Legacy" (18083).
4. eastkarana/"Tenal Redblade", hand "Redblade's Legacy" (18083). Gives "Totem of the Freezing War" (20680).
5. Loot "Heart of Frost" (10549) from "A Goblin Wizard" in `permafrost`.
6. eastkarana/"Tenal Redblade", hand "Heart of Frost" (10549) + "Totem of the Freezing War" (20680). Gives "Totem of Fiery War" (20681).
7. Loot "Red Dragon Scales" (11622) from "Echo of Nortlav" in `hole`.
8. Loot "Red Dragon Scales" (11622) from "Lord Nagafen" in `soldungb`.
9. Loot "Red Dragon Scales" (11622) from "Melalafen" in `westwastes`.
10. Loot "Red Dragon Scales" (11622) from "Talendor" in `skyfire`.
11. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
12. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `steamfont`.
13. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `tox`.
14. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `toxxulia`.
15. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
16. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). The combine does not fail.
17. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
18. northro/"Verrell Cogswin", hand "Water Flask" (13006). Sets `Green_Scale_Quest` to `1`.
19. northro/"Verrell Cogswin", hand "Red Dragon Scales" (11622). Sets `Green_Scale_Quest` to `2`.
20. northro/"Verrell Cogswin", say "Adhesive". Requires `Green_Scale_Quest` ==2. Requires `Green_Scale_Quest` set. Gives "Verrell's Box of Potions" (67387).
21. Loot "Fractured Centaur Hoof" (67388) from "Centaur Archer" in `southkarana`.
22. Loot "Fractured Centaur Hoof" (67388) from "Centaur Charger" in `southkarana`.
23. Loot "Fractured Centaur Hoof" (67388) from "Centaur Courser" in `southkarana`.
24. Loot "Fractured Centaur Hoof" (67388) from "Centaur Foal" in `southkarana`.
25. Loot "Fractured Centaur Hoof" (67388) from "Centaur Sheltie" in `southkarana`.
26. Loot "Fire Giant Embers" (67389) from "A Fire Giant Warlord" (NPC 278023) in `soldungc`. Drop cache: 28.35% chance per kill.
27. Loot "Jagged Permafrost Shards" (67390) from "The Chilling Terror" in `permafrost`.
28. Combine in Oven (15): "Fractured Centaur Hoof" (67388), "Fire Giant Embers" (67389), "Jagged Permafrost Shards" (67390). Produces "Glue Powder" (67391). Requires Baking. The combine does not fail.
29. Common item: Barley (16590). Listed in 28 zones.
30. Common item: Deep Fungus Mold (67393). Listed in 28 zones.
31. Common item: Distilled Spirits (67394). Listed in 28 zones.
32. Combine in Brew Barrel (19): "Barley" (16590), "Deep Fungus Mold" (67393), "Distilled Spirits" (67394). Produces "Deep Barley Brew" (67392). Requires Brewing, trivial 110.
33. northro/"Verrell Cogswin", say "Adhesive". Requires `Green_Scale_Quest` ==2. Requires `Green_Scale_Quest` set. Gives "Potion Vial" (67395).
34. Combine in "Verrell's Box of Potions" (67387): "Glue Powder" (67391), "Deep Barley Brew" (67392), "Potion Vial" (67395). Produces "Thick Adhesive" (67386). The combine does not fail.
35. northro/"Verrell Cogswin", hand "Thick Adhesive" (67386). Gives "Grey Scale Pieces" (67385).
36. northro/"Verrell Cogswin", hand "Thick Adhesive" (67386). Gives "Thick Adhesive" (67396).
37. Combine in "Verrell's Box of Potions" (67387): "Grey Scale Pieces" (67385), "Thick Adhesive" (67396). Produces "Grey Colored Scales" (67384). The combine does not fail.
38. northro/"Verrell Cogswin", hand "Grey Colored Scales" (67384). Gives "Green Dragon Scales" (11582).
39. eastkarana/"Tenal Redblade", hand "Green Dragon Scales" (11582) + "Red Dragon Scales" (11622) + "Totem of Fiery War" (20681). Gives "Mark of the Sword" (20683).
40. Loot "Hand of the Maestro" (20676) from "Hand of the Maestro" in `hateplane`.
41. Loot "Hand of the Maestro" (20676) from "Hand of the Maestro" in `hateplaneb`.
42. eastkarana/"Tenal Redblade", hand "Hand of the Maestro" (20676) + "Mark of the Sword" (20683). Gives "Tenal's note to Kargek" (20684).
43. Loot "Spiroc Wingblade" (20679) from "The Spiroc Lord" in `airplane`.
44. freeporteast/"Kargek Redblade", hand "Spiroc Wingblade" (20679) + "Tenal's note to Kargek" (20684). Gives "Red Scabbard" (17859).
45. lakerathe/"Triathalon Swim Goggles", say "Hail". Gives "Rebreather" (16889).
46. Loot "Block of Permafrost" (20665) from "Lady Vox" in `permafrost`.
47. Loot "Block of Permafrost" (20665) from "An Ice Giant" in `permafrost`.
48. Common item: Keg of Vox Tail Ale (20664). Listed in 13 zones.
49. oceanoftears/"Denken Strongpick", hand "Rebreather" (16889) + "Keg of Vox Tail Ale" (20664) + "Block of Permafrost" (20665). Gives "Ancient Sword Blade" (20667).
50. Loot "Ancient Blade" (20670) from "Queen Velazul Di'zok" in `chardok`.
51. Ground spawn of "Unjeweled Dragon Head Hilt" (20668) in `lakerathe`.
52. Loot "Apothic Crown" (1239) from "Magi P'Tasa" (NPC 186157) in `hateplaneb`. Drop cache: 19.16% chance per kill.
53. poknowledge/"Arch Mage Deidus", hand "Apothic Crown" (1239). Gives "Diamond" (10037).
54. Loot "Scroll of the Ox" (49007) from "A Sturdy Chest" in `stillmoona`.
55. Loot "Scroll of the Boar" (49008) from "A Sturdy Chest" in `stillmoona`.
56. Loot "Scroll of the Dragon" (49009) from "A Sturdy Chest" in `stillmoona`.
57. Loot "Scroll of the Tiger" (49010) from "A Sturdy Chest" in `stillmoona`.
58. Hand "Scroll of the Ox" (49007) + "Scroll of the Boar" (49008) + "Scroll of the Dragon" (49009) + "Scroll of the Tiger" (49010) to stillmoona/"The Keeper Of Strength". Spawns "A Spirit Keeper" (338169). Loot "Black Sapphire" (10036) from "A Spirit Keeper".
59. 42 alternative loot source(s) also yield Black Sapphire (10036).
60. Say "Tm Devrak Death" to rujd/"Rujd".
61. Spawns "spawn chest with Heavy Orcish Prison Key" (245241).
62. Loot "Heavy Orcish Prison Key" (59571) from "spawn chest with Heavy Orcish Prison Key".
63. 2 alternative loot source(s) also yield Heavy Orcish Prison Key (59571).
64. Hand "Heavy Orcish Prison Key" (59571) to rujd/"Rujd". Spawns "Prison Guard Talkor" (245290). Loot "Jacinth" (10053) from "Prison Guard Talkor".
65. 54 alternative loot source(s) also yield Jacinth (10053).
66. freeporteast/"Wenden Blackhammer", hand "Black Sapphire" (10036) + "Diamond" (10037) + "Jacinth" (10053) + "Unjeweled Dragon Head Hilt" (20668). Gives "Jeweled Dragon Head Hilt" (20671).
67. Ground spawn of "Severely Damaged Dragon Head Hilt" (20669) in `timorous`.
68. Loot "Giant Sized Monocle" (20678) from "A Mountain Giant Patriarch" in `dreadlands`.
69. frontiermtns/"Mentrax Mountainbone", hand "Giant Sized Monocle" (20678). Gives "Rejesiam Ore" (20666).
70. Loot "Ball of Everliving Golem" (20677) from "Dread" in `fearplane`.
71. Loot "Ball of Everliving Golem" (20677) from "Fright" in `fearplane`.
72. Loot "Ball of Everliving Golem" (20677) from "Terror" in `fearplane`.
73. freeporteast/"Wenden Blackhammer", hand "Rejesiam Ore" (20666) + "Severely Damaged Dragon Head Hilt" (20669) + "Ball of Everliving Golem" (20677). Gives "Finely Crafted Dragon Head Hilt" (20672).
74. Combine in "Red Scabbard" (17859): "Ancient Sword Blade" (20667), "Ancient Blade" (20670), "Jeweled Dragon Head Hilt" (20671), "Finely Crafted Dragon Head Hilt" (20672). Produces "Jagged Blade of War" (10908). The combine does not fail.
75. Combine in "Red Scabbard" (17859): "Jagged Blade of War" (10908). Produces "Blade of Tactics" (10909), "Blade of Strategy" (10910). The combine does not fail.

### "Blade of Tactics" (66176)

1. freeporteast/"Kargek Redblade", say "Favor". Gives "Wax Sealed Note" (20673).
2. feerrott/"Oknoggin Stonesmacker", hand "Wax Sealed Note" (20673). Gives "Tiny Lute" (20674).
3. freeporteast/"Kargek Redblade", hand "Tiny Lute" (20674). Gives "Redblade's Legacy" (18083).
4. eastkarana/"Tenal Redblade", hand "Redblade's Legacy" (18083). Gives "Totem of the Freezing War" (20680).
5. Loot "Heart of Frost" (10549) from "A Goblin Wizard" in `permafrost`.
6. eastkarana/"Tenal Redblade", hand "Heart of Frost" (10549) + "Totem of the Freezing War" (20680). Gives "Totem of Fiery War" (20681).
7. Loot "Red Dragon Scales" (11622) from "Echo of Nortlav" in `hole`.
8. Loot "Red Dragon Scales" (11622) from "Lord Nagafen" in `soldungb`.
9. Loot "Red Dragon Scales" (11622) from "Melalafen" in `westwastes`.
10. Loot "Red Dragon Scales" (11622) from "Talendor" in `skyfire`.
11. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
12. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `steamfont`.
13. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `tox`.
14. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `toxxulia`.
15. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
16. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). The combine does not fail.
17. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
18. northro/"Verrell Cogswin", hand "Water Flask" (13006). Sets `Green_Scale_Quest` to `1`.
19. northro/"Verrell Cogswin", hand "Red Dragon Scales" (11622). Sets `Green_Scale_Quest` to `2`.
20. northro/"Verrell Cogswin", say "Adhesive". Requires `Green_Scale_Quest` ==2. Requires `Green_Scale_Quest` set. Gives "Verrell's Box of Potions" (67387).
21. Loot "Fractured Centaur Hoof" (67388) from "Centaur Archer" in `southkarana`.
22. Loot "Fractured Centaur Hoof" (67388) from "Centaur Charger" in `southkarana`.
23. Loot "Fractured Centaur Hoof" (67388) from "Centaur Courser" in `southkarana`.
24. Loot "Fractured Centaur Hoof" (67388) from "Centaur Foal" in `southkarana`.
25. Loot "Fractured Centaur Hoof" (67388) from "Centaur Sheltie" in `southkarana`.
26. Loot "Fire Giant Embers" (67389) from "A Fire Giant Warlord" (NPC 278023) in `soldungc`. Drop cache: 28.35% chance per kill.
27. Loot "Jagged Permafrost Shards" (67390) from "The Chilling Terror" in `permafrost`.
28. Combine in Oven (15): "Fractured Centaur Hoof" (67388), "Fire Giant Embers" (67389), "Jagged Permafrost Shards" (67390). Produces "Glue Powder" (67391). Requires Baking. The combine does not fail.
29. Common item: Barley (16590). Listed in 28 zones.
30. Common item: Deep Fungus Mold (67393). Listed in 28 zones.
31. Common item: Distilled Spirits (67394). Listed in 28 zones.
32. Combine in Brew Barrel (19): "Barley" (16590), "Deep Fungus Mold" (67393), "Distilled Spirits" (67394). Produces "Deep Barley Brew" (67392). Requires Brewing, trivial 110.
33. northro/"Verrell Cogswin", say "Adhesive". Requires `Green_Scale_Quest` ==2. Requires `Green_Scale_Quest` set. Gives "Potion Vial" (67395).
34. Combine in "Verrell's Box of Potions" (67387): "Glue Powder" (67391), "Deep Barley Brew" (67392), "Potion Vial" (67395). Produces "Thick Adhesive" (67386). The combine does not fail.
35. northro/"Verrell Cogswin", hand "Thick Adhesive" (67386). Gives "Grey Scale Pieces" (67385).
36. northro/"Verrell Cogswin", hand "Thick Adhesive" (67386). Gives "Thick Adhesive" (67396).
37. Combine in "Verrell's Box of Potions" (67387): "Grey Scale Pieces" (67385), "Thick Adhesive" (67396). Produces "Grey Colored Scales" (67384). The combine does not fail.
38. northro/"Verrell Cogswin", hand "Grey Colored Scales" (67384). Gives "Green Dragon Scales" (11582).
39. eastkarana/"Tenal Redblade", hand "Green Dragon Scales" (11582) + "Red Dragon Scales" (11622) + "Totem of Fiery War" (20681). Gives "Mark of the Sword" (20683).
40. Loot "Hand of the Maestro" (20676) from "Hand of the Maestro" in `hateplane`.
41. Loot "Hand of the Maestro" (20676) from "Hand of the Maestro" in `hateplaneb`.
42. eastkarana/"Tenal Redblade", hand "Hand of the Maestro" (20676) + "Mark of the Sword" (20683). Gives "Tenal's note to Kargek" (20684).
43. Loot "Spiroc Wingblade" (20679) from "The Spiroc Lord" in `airplane`.
44. freeporteast/"Kargek Redblade", hand "Spiroc Wingblade" (20679) + "Tenal's note to Kargek" (20684). Gives "Red Scabbard" (17859).
45. Combine in "Red Scabbard" (17859): "Jagged Blade of War" (10908). Produces "Blade of Tactics" (10909), "Blade of Strategy" (10910). The combine does not fail.
46. Combine in "Red Scabbard" (17859): "Blade of Tactics" (10909), "Blade of Strategy" (10910). Produces "Jagged Blade of War" (10908). The combine does not fail.
47. lakerathe/"Triathalon Swim Goggles", say "Hail". Gives "Rebreather" (16889).
48. Loot "Block of Permafrost" (20665) from "Lady Vox" in `permafrost`.
49. Loot "Block of Permafrost" (20665) from "An Ice Giant" in `permafrost`.
50. Common item: Keg of Vox Tail Ale (20664). Listed in 13 zones.
51. oceanoftears/"Denken Strongpick", hand "Rebreather" (16889) + "Keg of Vox Tail Ale" (20664) + "Block of Permafrost" (20665). Gives "Ancient Sword Blade" (20667).
52. Loot "Ancient Blade" (20670) from "Queen Velazul Di'zok" in `chardok`.
53. Ground spawn of "Unjeweled Dragon Head Hilt" (20668) in `lakerathe`.
54. Loot "Apothic Crown" (1239) from "Magi P'Tasa" (NPC 186157) in `hateplaneb`. Drop cache: 19.16% chance per kill.
55. poknowledge/"Arch Mage Deidus", hand "Apothic Crown" (1239). Gives "Diamond" (10037).
56. Loot "Scroll of the Ox" (49007) from "A Sturdy Chest" in `stillmoona`.
57. Loot "Scroll of the Boar" (49008) from "A Sturdy Chest" in `stillmoona`.
58. Loot "Scroll of the Dragon" (49009) from "A Sturdy Chest" in `stillmoona`.
59. Loot "Scroll of the Tiger" (49010) from "A Sturdy Chest" in `stillmoona`.
60. Hand "Scroll of the Ox" (49007) + "Scroll of the Boar" (49008) + "Scroll of the Dragon" (49009) + "Scroll of the Tiger" (49010) to stillmoona/"The Keeper Of Strength". Spawns "A Spirit Keeper" (338169). Loot "Black Sapphire" (10036) from "A Spirit Keeper".
61. 42 alternative loot source(s) also yield Black Sapphire (10036).
62. Say "Tm Devrak Death" to rujd/"Rujd".
63. Spawns "spawn chest with Heavy Orcish Prison Key" (245241).
64. Loot "Heavy Orcish Prison Key" (59571) from "spawn chest with Heavy Orcish Prison Key".
65. 2 alternative loot source(s) also yield Heavy Orcish Prison Key (59571).
66. Hand "Heavy Orcish Prison Key" (59571) to rujd/"Rujd". Spawns "Prison Guard Talkor" (245290). Loot "Jacinth" (10053) from "Prison Guard Talkor".
67. 54 alternative loot source(s) also yield Jacinth (10053).
68. freeporteast/"Wenden Blackhammer", hand "Black Sapphire" (10036) + "Diamond" (10037) + "Jacinth" (10053) + "Unjeweled Dragon Head Hilt" (20668). Gives "Jeweled Dragon Head Hilt" (20671).
69. Ground spawn of "Severely Damaged Dragon Head Hilt" (20669) in `timorous`.
70. Loot "Giant Sized Monocle" (20678) from "A Mountain Giant Patriarch" in `dreadlands`.
71. frontiermtns/"Mentrax Mountainbone", hand "Giant Sized Monocle" (20678). Gives "Rejesiam Ore" (20666).
72. Loot "Ball of Everliving Golem" (20677) from "Dread" in `fearplane`.
73. Loot "Ball of Everliving Golem" (20677) from "Fright" in `fearplane`.
74. Loot "Ball of Everliving Golem" (20677) from "Terror" in `fearplane`.
75. freeporteast/"Wenden Blackhammer", hand "Rejesiam Ore" (20666) + "Severely Damaged Dragon Head Hilt" (20669) + "Ball of Everliving Golem" (20677). Gives "Finely Crafted Dragon Head Hilt" (20672).
76. Combine in "Red Scabbard" (17859): "Ancient Sword Blade" (20667), "Ancient Blade" (20670), "Jeweled Dragon Head Hilt" (20671), "Finely Crafted Dragon Head Hilt" (20672). Produces "Jagged Blade of War" (10908). The combine does not fail.
77. freeporteast/"Gartrog Smitehammer", hand "Jagged Blade of War" (10908) + "Red Scabbard" (17859). Gives "Red Scabbard" (17869).
78. freeporteast/"Gartrog Smitehammer", hand "Jagged Blade of War" (10908) + "Red Scabbard" (17859). Gives "Jagged Blade of War" (66175).
79. Combine in "Red Scabbard" (17869): "Jagged Blade of War" (66175). Produces "Blade of Tactics" (66176), "Blade of Strategy" (66177). Requires Pottery. The combine does not fail.

### "Blade of Strategy" (66177)

1. freeporteast/"Kargek Redblade", say "Favor". Gives "Wax Sealed Note" (20673).
2. feerrott/"Oknoggin Stonesmacker", hand "Wax Sealed Note" (20673). Gives "Tiny Lute" (20674).
3. freeporteast/"Kargek Redblade", hand "Tiny Lute" (20674). Gives "Redblade's Legacy" (18083).
4. eastkarana/"Tenal Redblade", hand "Redblade's Legacy" (18083). Gives "Totem of the Freezing War" (20680).
5. Loot "Heart of Frost" (10549) from "A Goblin Wizard" in `permafrost`.
6. eastkarana/"Tenal Redblade", hand "Heart of Frost" (10549) + "Totem of the Freezing War" (20680). Gives "Totem of Fiery War" (20681).
7. Loot "Red Dragon Scales" (11622) from "Echo of Nortlav" in `hole`.
8. Loot "Red Dragon Scales" (11622) from "Lord Nagafen" in `soldungb`.
9. Loot "Red Dragon Scales" (11622) from "Melalafen" in `westwastes`.
10. Loot "Red Dragon Scales" (11622) from "Talendor" in `skyfire`.
11. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
12. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `steamfont`.
13. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `tox`.
14. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `toxxulia`.
15. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
16. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). The combine does not fail.
17. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
18. northro/"Verrell Cogswin", hand "Water Flask" (13006). Sets `Green_Scale_Quest` to `1`.
19. northro/"Verrell Cogswin", hand "Red Dragon Scales" (11622). Sets `Green_Scale_Quest` to `2`.
20. northro/"Verrell Cogswin", say "Adhesive". Requires `Green_Scale_Quest` ==2. Requires `Green_Scale_Quest` set. Gives "Verrell's Box of Potions" (67387).
21. Loot "Fractured Centaur Hoof" (67388) from "Centaur Archer" in `southkarana`.
22. Loot "Fractured Centaur Hoof" (67388) from "Centaur Charger" in `southkarana`.
23. Loot "Fractured Centaur Hoof" (67388) from "Centaur Courser" in `southkarana`.
24. Loot "Fractured Centaur Hoof" (67388) from "Centaur Foal" in `southkarana`.
25. Loot "Fractured Centaur Hoof" (67388) from "Centaur Sheltie" in `southkarana`.
26. Loot "Fire Giant Embers" (67389) from "A Fire Giant Warlord" (NPC 278023) in `soldungc`. Drop cache: 28.35% chance per kill.
27. Loot "Jagged Permafrost Shards" (67390) from "The Chilling Terror" in `permafrost`.
28. Combine in Oven (15): "Fractured Centaur Hoof" (67388), "Fire Giant Embers" (67389), "Jagged Permafrost Shards" (67390). Produces "Glue Powder" (67391). Requires Baking. The combine does not fail.
29. Common item: Barley (16590). Listed in 28 zones.
30. Common item: Deep Fungus Mold (67393). Listed in 28 zones.
31. Common item: Distilled Spirits (67394). Listed in 28 zones.
32. Combine in Brew Barrel (19): "Barley" (16590), "Deep Fungus Mold" (67393), "Distilled Spirits" (67394). Produces "Deep Barley Brew" (67392). Requires Brewing, trivial 110.
33. northro/"Verrell Cogswin", say "Adhesive". Requires `Green_Scale_Quest` ==2. Requires `Green_Scale_Quest` set. Gives "Potion Vial" (67395).
34. Combine in "Verrell's Box of Potions" (67387): "Glue Powder" (67391), "Deep Barley Brew" (67392), "Potion Vial" (67395). Produces "Thick Adhesive" (67386). The combine does not fail.
35. northro/"Verrell Cogswin", hand "Thick Adhesive" (67386). Gives "Grey Scale Pieces" (67385).
36. northro/"Verrell Cogswin", hand "Thick Adhesive" (67386). Gives "Thick Adhesive" (67396).
37. Combine in "Verrell's Box of Potions" (67387): "Grey Scale Pieces" (67385), "Thick Adhesive" (67396). Produces "Grey Colored Scales" (67384). The combine does not fail.
38. northro/"Verrell Cogswin", hand "Grey Colored Scales" (67384). Gives "Green Dragon Scales" (11582).
39. eastkarana/"Tenal Redblade", hand "Green Dragon Scales" (11582) + "Red Dragon Scales" (11622) + "Totem of Fiery War" (20681). Gives "Mark of the Sword" (20683).
40. Loot "Hand of the Maestro" (20676) from "Hand of the Maestro" in `hateplane`.
41. Loot "Hand of the Maestro" (20676) from "Hand of the Maestro" in `hateplaneb`.
42. eastkarana/"Tenal Redblade", hand "Hand of the Maestro" (20676) + "Mark of the Sword" (20683). Gives "Tenal's note to Kargek" (20684).
43. Loot "Spiroc Wingblade" (20679) from "The Spiroc Lord" in `airplane`.
44. freeporteast/"Kargek Redblade", hand "Spiroc Wingblade" (20679) + "Tenal's note to Kargek" (20684). Gives "Red Scabbard" (17859).
45. Combine in "Red Scabbard" (17859): "Jagged Blade of War" (10908). Produces "Blade of Tactics" (10909), "Blade of Strategy" (10910). The combine does not fail.
46. Combine in "Red Scabbard" (17859): "Blade of Tactics" (10909), "Blade of Strategy" (10910). Produces "Jagged Blade of War" (10908). The combine does not fail.
47. lakerathe/"Triathalon Swim Goggles", say "Hail". Gives "Rebreather" (16889).
48. Loot "Block of Permafrost" (20665) from "Lady Vox" in `permafrost`.
49. Loot "Block of Permafrost" (20665) from "An Ice Giant" in `permafrost`.
50. Common item: Keg of Vox Tail Ale (20664). Listed in 13 zones.
51. oceanoftears/"Denken Strongpick", hand "Rebreather" (16889) + "Keg of Vox Tail Ale" (20664) + "Block of Permafrost" (20665). Gives "Ancient Sword Blade" (20667).
52. Loot "Ancient Blade" (20670) from "Queen Velazul Di'zok" in `chardok`.
53. Ground spawn of "Unjeweled Dragon Head Hilt" (20668) in `lakerathe`.
54. Loot "Apothic Crown" (1239) from "Magi P'Tasa" (NPC 186157) in `hateplaneb`. Drop cache: 19.16% chance per kill.
55. poknowledge/"Arch Mage Deidus", hand "Apothic Crown" (1239). Gives "Diamond" (10037).
56. Loot "Scroll of the Ox" (49007) from "A Sturdy Chest" in `stillmoona`.
57. Loot "Scroll of the Boar" (49008) from "A Sturdy Chest" in `stillmoona`.
58. Loot "Scroll of the Dragon" (49009) from "A Sturdy Chest" in `stillmoona`.
59. Loot "Scroll of the Tiger" (49010) from "A Sturdy Chest" in `stillmoona`.
60. Hand "Scroll of the Ox" (49007) + "Scroll of the Boar" (49008) + "Scroll of the Dragon" (49009) + "Scroll of the Tiger" (49010) to stillmoona/"The Keeper Of Strength". Spawns "A Spirit Keeper" (338169). Loot "Black Sapphire" (10036) from "A Spirit Keeper".
61. 42 alternative loot source(s) also yield Black Sapphire (10036).
62. Say "Tm Devrak Death" to rujd/"Rujd".
63. Spawns "spawn chest with Heavy Orcish Prison Key" (245241).
64. Loot "Heavy Orcish Prison Key" (59571) from "spawn chest with Heavy Orcish Prison Key".
65. 2 alternative loot source(s) also yield Heavy Orcish Prison Key (59571).
66. Hand "Heavy Orcish Prison Key" (59571) to rujd/"Rujd". Spawns "Prison Guard Talkor" (245290). Loot "Jacinth" (10053) from "Prison Guard Talkor".
67. 54 alternative loot source(s) also yield Jacinth (10053).
68. freeporteast/"Wenden Blackhammer", hand "Black Sapphire" (10036) + "Diamond" (10037) + "Jacinth" (10053) + "Unjeweled Dragon Head Hilt" (20668). Gives "Jeweled Dragon Head Hilt" (20671).
69. Ground spawn of "Severely Damaged Dragon Head Hilt" (20669) in `timorous`.
70. Loot "Giant Sized Monocle" (20678) from "A Mountain Giant Patriarch" in `dreadlands`.
71. frontiermtns/"Mentrax Mountainbone", hand "Giant Sized Monocle" (20678). Gives "Rejesiam Ore" (20666).
72. Loot "Ball of Everliving Golem" (20677) from "Dread" in `fearplane`.
73. Loot "Ball of Everliving Golem" (20677) from "Fright" in `fearplane`.
74. Loot "Ball of Everliving Golem" (20677) from "Terror" in `fearplane`.
75. freeporteast/"Wenden Blackhammer", hand "Rejesiam Ore" (20666) + "Severely Damaged Dragon Head Hilt" (20669) + "Ball of Everliving Golem" (20677). Gives "Finely Crafted Dragon Head Hilt" (20672).
76. Combine in "Red Scabbard" (17859): "Ancient Sword Blade" (20667), "Ancient Blade" (20670), "Jeweled Dragon Head Hilt" (20671), "Finely Crafted Dragon Head Hilt" (20672). Produces "Jagged Blade of War" (10908). The combine does not fail.
77. freeporteast/"Gartrog Smitehammer", hand "Jagged Blade of War" (10908) + "Red Scabbard" (17859). Gives "Red Scabbard" (17869).
78. freeporteast/"Gartrog Smitehammer", hand "Jagged Blade of War" (10908) + "Red Scabbard" (17859). Gives "Jagged Blade of War" (66175).
79. Combine in "Red Scabbard" (17869): "Jagged Blade of War" (66175). Produces "Blade of Tactics" (66176), "Blade of Strategy" (66177). Requires Pottery. The combine does not fail.

### "Jagged Blade of War" (10908)

1. freeporteast/"Kargek Redblade", say "Favor". Gives "Wax Sealed Note" (20673).
2. feerrott/"Oknoggin Stonesmacker", hand "Wax Sealed Note" (20673). Gives "Tiny Lute" (20674).
3. freeporteast/"Kargek Redblade", hand "Tiny Lute" (20674). Gives "Redblade's Legacy" (18083).
4. eastkarana/"Tenal Redblade", hand "Redblade's Legacy" (18083). Gives "Totem of the Freezing War" (20680).
5. Loot "Heart of Frost" (10549) from "A Goblin Wizard" in `permafrost`.
6. eastkarana/"Tenal Redblade", hand "Heart of Frost" (10549) + "Totem of the Freezing War" (20680). Gives "Totem of Fiery War" (20681).
7. Loot "Red Dragon Scales" (11622) from "Echo of Nortlav" in `hole`.
8. Loot "Red Dragon Scales" (11622) from "Lord Nagafen" in `soldungb`.
9. Loot "Red Dragon Scales" (11622) from "Melalafen" in `westwastes`.
10. Loot "Red Dragon Scales" (11622) from "Talendor" in `skyfire`.
11. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
12. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `steamfont`.
13. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `tox`.
14. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `toxxulia`.
15. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
16. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). The combine does not fail.
17. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
18. northro/"Verrell Cogswin", hand "Water Flask" (13006). Sets `Green_Scale_Quest` to `1`.
19. northro/"Verrell Cogswin", hand "Red Dragon Scales" (11622). Sets `Green_Scale_Quest` to `2`.
20. northro/"Verrell Cogswin", say "Adhesive". Requires `Green_Scale_Quest` ==2. Requires `Green_Scale_Quest` set. Gives "Verrell's Box of Potions" (67387).
21. Loot "Fractured Centaur Hoof" (67388) from "Centaur Archer" in `southkarana`.
22. Loot "Fractured Centaur Hoof" (67388) from "Centaur Charger" in `southkarana`.
23. Loot "Fractured Centaur Hoof" (67388) from "Centaur Courser" in `southkarana`.
24. Loot "Fractured Centaur Hoof" (67388) from "Centaur Foal" in `southkarana`.
25. Loot "Fractured Centaur Hoof" (67388) from "Centaur Sheltie" in `southkarana`.
26. Loot "Fire Giant Embers" (67389) from "A Fire Giant Warlord" (NPC 278023) in `soldungc`. Drop cache: 28.35% chance per kill.
27. Loot "Jagged Permafrost Shards" (67390) from "The Chilling Terror" in `permafrost`.
28. Combine in Oven (15): "Fractured Centaur Hoof" (67388), "Fire Giant Embers" (67389), "Jagged Permafrost Shards" (67390). Produces "Glue Powder" (67391). Requires Baking. The combine does not fail.
29. Common item: Barley (16590). Listed in 28 zones.
30. Common item: Deep Fungus Mold (67393). Listed in 28 zones.
31. Common item: Distilled Spirits (67394). Listed in 28 zones.
32. Combine in Brew Barrel (19): "Barley" (16590), "Deep Fungus Mold" (67393), "Distilled Spirits" (67394). Produces "Deep Barley Brew" (67392). Requires Brewing, trivial 110.
33. northro/"Verrell Cogswin", say "Adhesive". Requires `Green_Scale_Quest` ==2. Requires `Green_Scale_Quest` set. Gives "Potion Vial" (67395).
34. Combine in "Verrell's Box of Potions" (67387): "Glue Powder" (67391), "Deep Barley Brew" (67392), "Potion Vial" (67395). Produces "Thick Adhesive" (67386). The combine does not fail.
35. northro/"Verrell Cogswin", hand "Thick Adhesive" (67386). Gives "Grey Scale Pieces" (67385).
36. northro/"Verrell Cogswin", hand "Thick Adhesive" (67386). Gives "Thick Adhesive" (67396).
37. Combine in "Verrell's Box of Potions" (67387): "Grey Scale Pieces" (67385), "Thick Adhesive" (67396). Produces "Grey Colored Scales" (67384). The combine does not fail.
38. northro/"Verrell Cogswin", hand "Grey Colored Scales" (67384). Gives "Green Dragon Scales" (11582).
39. eastkarana/"Tenal Redblade", hand "Green Dragon Scales" (11582) + "Red Dragon Scales" (11622) + "Totem of Fiery War" (20681). Gives "Mark of the Sword" (20683).
40. Loot "Hand of the Maestro" (20676) from "Hand of the Maestro" in `hateplane`.
41. Loot "Hand of the Maestro" (20676) from "Hand of the Maestro" in `hateplaneb`.
42. eastkarana/"Tenal Redblade", hand "Hand of the Maestro" (20676) + "Mark of the Sword" (20683). Gives "Tenal's note to Kargek" (20684).
43. Loot "Spiroc Wingblade" (20679) from "The Spiroc Lord" in `airplane`.
44. freeporteast/"Kargek Redblade", hand "Spiroc Wingblade" (20679) + "Tenal's note to Kargek" (20684). Gives "Red Scabbard" (17859).
45. Combine in "Red Scabbard" (17859): "Jagged Blade of War" (10908). Produces "Blade of Tactics" (10909), "Blade of Strategy" (10910). The combine does not fail.
46. Combine in "Red Scabbard" (17859): "Jagged Blade of War" (10908). Produces "Blade of Tactics" (10909), "Blade of Strategy" (10910). The combine does not fail.
47. Combine in "Red Scabbard" (17859): "Blade of Tactics" (10909), "Blade of Strategy" (10910). Produces "Jagged Blade of War" (10908). The combine does not fail.

### "Jagged Blade of War" (66175)

1. freeporteast/"Kargek Redblade", say "Favor". Gives "Wax Sealed Note" (20673).
2. feerrott/"Oknoggin Stonesmacker", hand "Wax Sealed Note" (20673). Gives "Tiny Lute" (20674).
3. freeporteast/"Kargek Redblade", hand "Tiny Lute" (20674). Gives "Redblade's Legacy" (18083).
4. eastkarana/"Tenal Redblade", hand "Redblade's Legacy" (18083). Gives "Totem of the Freezing War" (20680).
5. Loot "Heart of Frost" (10549) from "A Goblin Wizard" in `permafrost`.
6. eastkarana/"Tenal Redblade", hand "Heart of Frost" (10549) + "Totem of the Freezing War" (20680). Gives "Totem of Fiery War" (20681).
7. Loot "Red Dragon Scales" (11622) from "Echo of Nortlav" in `hole`.
8. Loot "Red Dragon Scales" (11622) from "Lord Nagafen" in `soldungb`.
9. Loot "Red Dragon Scales" (11622) from "Melalafen" in `westwastes`.
10. Loot "Red Dragon Scales" (11622) from "Talendor" in `skyfire`.
11. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
12. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `steamfont`.
13. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `tox`.
14. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `toxxulia`.
15. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
16. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). The combine does not fail.
17. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
18. northro/"Verrell Cogswin", hand "Water Flask" (13006). Sets `Green_Scale_Quest` to `1`.
19. northro/"Verrell Cogswin", hand "Red Dragon Scales" (11622). Sets `Green_Scale_Quest` to `2`.
20. northro/"Verrell Cogswin", say "Adhesive". Requires `Green_Scale_Quest` ==2. Requires `Green_Scale_Quest` set. Gives "Verrell's Box of Potions" (67387).
21. Loot "Fractured Centaur Hoof" (67388) from "Centaur Archer" in `southkarana`.
22. Loot "Fractured Centaur Hoof" (67388) from "Centaur Charger" in `southkarana`.
23. Loot "Fractured Centaur Hoof" (67388) from "Centaur Courser" in `southkarana`.
24. Loot "Fractured Centaur Hoof" (67388) from "Centaur Foal" in `southkarana`.
25. Loot "Fractured Centaur Hoof" (67388) from "Centaur Sheltie" in `southkarana`.
26. Loot "Fire Giant Embers" (67389) from "A Fire Giant Warlord" (NPC 278023) in `soldungc`. Drop cache: 28.35% chance per kill.
27. Loot "Jagged Permafrost Shards" (67390) from "The Chilling Terror" in `permafrost`.
28. Combine in Oven (15): "Fractured Centaur Hoof" (67388), "Fire Giant Embers" (67389), "Jagged Permafrost Shards" (67390). Produces "Glue Powder" (67391). Requires Baking. The combine does not fail.
29. Common item: Barley (16590). Listed in 28 zones.
30. Common item: Deep Fungus Mold (67393). Listed in 28 zones.
31. Common item: Distilled Spirits (67394). Listed in 28 zones.
32. Combine in Brew Barrel (19): "Barley" (16590), "Deep Fungus Mold" (67393), "Distilled Spirits" (67394). Produces "Deep Barley Brew" (67392). Requires Brewing, trivial 110.
33. northro/"Verrell Cogswin", say "Adhesive". Requires `Green_Scale_Quest` ==2. Requires `Green_Scale_Quest` set. Gives "Potion Vial" (67395).
34. Combine in "Verrell's Box of Potions" (67387): "Glue Powder" (67391), "Deep Barley Brew" (67392), "Potion Vial" (67395). Produces "Thick Adhesive" (67386). The combine does not fail.
35. northro/"Verrell Cogswin", hand "Thick Adhesive" (67386). Gives "Grey Scale Pieces" (67385).
36. northro/"Verrell Cogswin", hand "Thick Adhesive" (67386). Gives "Thick Adhesive" (67396).
37. Combine in "Verrell's Box of Potions" (67387): "Grey Scale Pieces" (67385), "Thick Adhesive" (67396). Produces "Grey Colored Scales" (67384). The combine does not fail.
38. northro/"Verrell Cogswin", hand "Grey Colored Scales" (67384). Gives "Green Dragon Scales" (11582).
39. eastkarana/"Tenal Redblade", hand "Green Dragon Scales" (11582) + "Red Dragon Scales" (11622) + "Totem of Fiery War" (20681). Gives "Mark of the Sword" (20683).
40. Loot "Hand of the Maestro" (20676) from "Hand of the Maestro" in `hateplane`.
41. Loot "Hand of the Maestro" (20676) from "Hand of the Maestro" in `hateplaneb`.
42. eastkarana/"Tenal Redblade", hand "Hand of the Maestro" (20676) + "Mark of the Sword" (20683). Gives "Tenal's note to Kargek" (20684).
43. Loot "Spiroc Wingblade" (20679) from "The Spiroc Lord" in `airplane`.
44. freeporteast/"Kargek Redblade", hand "Spiroc Wingblade" (20679) + "Tenal's note to Kargek" (20684). Gives "Red Scabbard" (17859).
45. Combine in "Red Scabbard" (17859): "Jagged Blade of War" (10908). Produces "Blade of Tactics" (10909), "Blade of Strategy" (10910). The combine does not fail.
46. Combine in "Red Scabbard" (17859): "Blade of Tactics" (10909), "Blade of Strategy" (10910). Produces "Jagged Blade of War" (10908). The combine does not fail.
47. lakerathe/"Triathalon Swim Goggles", say "Hail". Gives "Rebreather" (16889).
48. Loot "Block of Permafrost" (20665) from "Lady Vox" in `permafrost`.
49. Loot "Block of Permafrost" (20665) from "An Ice Giant" in `permafrost`.
50. Common item: Keg of Vox Tail Ale (20664). Listed in 13 zones.
51. oceanoftears/"Denken Strongpick", hand "Rebreather" (16889) + "Keg of Vox Tail Ale" (20664) + "Block of Permafrost" (20665). Gives "Ancient Sword Blade" (20667).
52. Loot "Ancient Blade" (20670) from "Queen Velazul Di'zok" in `chardok`.
53. Ground spawn of "Unjeweled Dragon Head Hilt" (20668) in `lakerathe`.
54. Loot "Apothic Crown" (1239) from "Magi P'Tasa" (NPC 186157) in `hateplaneb`. Drop cache: 19.16% chance per kill.
55. poknowledge/"Arch Mage Deidus", hand "Apothic Crown" (1239). Gives "Diamond" (10037).
56. Loot "Scroll of the Ox" (49007) from "A Sturdy Chest" in `stillmoona`.
57. Loot "Scroll of the Boar" (49008) from "A Sturdy Chest" in `stillmoona`.
58. Loot "Scroll of the Dragon" (49009) from "A Sturdy Chest" in `stillmoona`.
59. Loot "Scroll of the Tiger" (49010) from "A Sturdy Chest" in `stillmoona`.
60. Hand "Scroll of the Ox" (49007) + "Scroll of the Boar" (49008) + "Scroll of the Dragon" (49009) + "Scroll of the Tiger" (49010) to stillmoona/"The Keeper Of Strength". Spawns "A Spirit Keeper" (338169). Loot "Black Sapphire" (10036) from "A Spirit Keeper".
61. 42 alternative loot source(s) also yield Black Sapphire (10036).
62. Say "Tm Devrak Death" to rujd/"Rujd".
63. Spawns "spawn chest with Heavy Orcish Prison Key" (245241).
64. Loot "Heavy Orcish Prison Key" (59571) from "spawn chest with Heavy Orcish Prison Key".
65. 2 alternative loot source(s) also yield Heavy Orcish Prison Key (59571).
66. Hand "Heavy Orcish Prison Key" (59571) to rujd/"Rujd". Spawns "Prison Guard Talkor" (245290). Loot "Jacinth" (10053) from "Prison Guard Talkor".
67. 54 alternative loot source(s) also yield Jacinth (10053).
68. freeporteast/"Wenden Blackhammer", hand "Black Sapphire" (10036) + "Diamond" (10037) + "Jacinth" (10053) + "Unjeweled Dragon Head Hilt" (20668). Gives "Jeweled Dragon Head Hilt" (20671).
69. Ground spawn of "Severely Damaged Dragon Head Hilt" (20669) in `timorous`.
70. Loot "Giant Sized Monocle" (20678) from "A Mountain Giant Patriarch" in `dreadlands`.
71. frontiermtns/"Mentrax Mountainbone", hand "Giant Sized Monocle" (20678). Gives "Rejesiam Ore" (20666).
72. Loot "Ball of Everliving Golem" (20677) from "Dread" in `fearplane`.
73. Loot "Ball of Everliving Golem" (20677) from "Fright" in `fearplane`.
74. Loot "Ball of Everliving Golem" (20677) from "Terror" in `fearplane`.
75. freeporteast/"Wenden Blackhammer", hand "Rejesiam Ore" (20666) + "Severely Damaged Dragon Head Hilt" (20669) + "Ball of Everliving Golem" (20677). Gives "Finely Crafted Dragon Head Hilt" (20672).
76. Combine in "Red Scabbard" (17859): "Ancient Sword Blade" (20667), "Ancient Blade" (20670), "Jeweled Dragon Head Hilt" (20671), "Finely Crafted Dragon Head Hilt" (20672). Produces "Jagged Blade of War" (10908). The combine does not fail.
77. freeporteast/"Gartrog Smitehammer", hand "Jagged Blade of War" (10908) + "Red Scabbard" (17859). Gives "Jagged Blade of War" (66175).

### "Blackfall Blade" (60303)

1. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
2. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `steamfont`.
3. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `tox`.
4. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `toxxulia`.
5. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
6. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). The combine does not fail.
7. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
8. nedaria/"Korezna Orecleaver", hand "Water Flask" (13006) + "Water Flask" (13006) + "Water Flask" (13006) + "Water Flask" (13006). Sets `warrior_epic_korezna` to `1`.
9. nedaria/"Korezna Orecleaver", hand "Water Flask" (13006) + "Water Flask" (13006) + "Water Flask" (13006). Sets `warrior_epic_korezna` to `2`.
10. **Broken:** nothing in the graph gives, loots, spawns, or combines Blackfall Ore (60301).
11. Unresolved cyclic prerequisite: `warrior_epic` ==17.
12. Ground spawn of "Frozen Pestle" (60323) in `iceclad`.
13. iceclad/"Fazzle Thumpkin", hand "Frozen Pestle" (60323). Sets `warrior_epic` to `18`.
14. Loot "Kreljnok's Muddled Rage" (60322) from "Possessed Brute" in `provinggrounds`.
15. draniksscar/"Korbuk Brimblade", hand "Kreljnok's Muddled Rage" (60322). Sets `warrior_epic` to `17`.
16. draniksscar/"Korbuk Brimblade", hand "Blackfall Ore" (60301). Requires `warrior_epic` >=2. Gives "Smelting Plans" (60302).
17. nedaria/"Korezna Orecleaver", hand "Blackfall Ore" (60301) + "Smelting Plans" (60302). Requires `warrior_epic_korezna` ==2. Gives "Blackfall Blade" (60303).

### "Sealed Vial of Blackfall Blood" (60305)

1. Unresolved cyclic prerequisite: `warrior_epic` ==17.
2. Ground spawn of "Frozen Pestle" (60323) in `iceclad`.
3. iceclad/"Fazzle Thumpkin", hand "Frozen Pestle" (60323). Sets `warrior_epic` to `18`.
4. Loot "Kreljnok's Muddled Rage" (60322) from "Possessed Brute" in `provinggrounds`.
5. draniksscar/"Korbuk Brimblade", hand "Kreljnok's Muddled Rage" (60322). Sets `warrior_epic` to `17`.
6. Kill vxed/"Blackfall Borerling". Spawns "Blackfall Borer" (290069).
7. Loot "Vial of Blackfall Blood" (60304) from "Blackfall Borer".
8. draniksscar/"Korbuk Brimblade", hand "Vial of Blackfall Blood" (60304). Requires `warrior_epic` >=3. Gives "Sealed Vial of Blackfall Blood" (60305).

### "Potion of Blackfall Spirit" (60306)

1. Unresolved cyclic prerequisite: `warrior_epic` ==17.
2. Ground spawn of "Frozen Pestle" (60323) in `iceclad`.
3. iceclad/"Fazzle Thumpkin", hand "Frozen Pestle" (60323). Sets `warrior_epic` to `18`.
4. Loot "Kreljnok's Muddled Rage" (60322) from "Possessed Brute" in `provinggrounds`.
5. draniksscar/"Korbuk Brimblade", hand "Kreljnok's Muddled Rage" (60322). Sets `warrior_epic` to `17`.
6. everfrost/"Kimber Whitefoot", say "Hail". Requires `warrior_epic` set. Requires `warrior_epic` >=4. Gives "Potion of Blackfall Spirit" (60306).

### "Nocturnal Mask of Acuity" (60309)

1. Common item: Jeweler's Kit (17912). Listed in 33 zones.
2. No quest step gives Darkened Star Rose Quartz (60308). The dump lists it in firiona, qeynos2.
3. Summon "Enchanted Electrum Bar" (16505) by casting "Enchant Electrum", "Mass Enchant Electrum", "Greater Mass Enchant Electrum".
4. Combine in "Jeweler's Kit" (17912): "Darkened Star Rose Quartz" (60308), "Enchanted Electrum Bar" (16505). Produces "Nocturnal Mask of Acuity" (60309). Requires Jewelry Making, trivial 103.

### "Glistening Hilt" (60311)

1. Unresolved cyclic prerequisite: `warrior_epic` ==17.
2. Ground spawn of "Frozen Pestle" (60323) in `iceclad`.
3. iceclad/"Fazzle Thumpkin", hand "Frozen Pestle" (60323). Sets `warrior_epic` to `18`.
4. Loot "Kreljnok's Muddled Rage" (60322) from "Possessed Brute" in `provinggrounds`.
5. draniksscar/"Korbuk Brimblade", hand "Kreljnok's Muddled Rage" (60322). Sets `warrior_epic` to `17`.
6. Unresolved cyclic prerequisite: `warrior_pre` ==6.
7. freeporteast/"Kargek Redblade", say "Favor". Gives "Wax Sealed Note" (20673).
8. feerrott/"Oknoggin Stonesmacker", hand "Wax Sealed Note" (20673). Gives "Tiny Lute" (20674).
9. freeporteast/"Kargek Redblade", hand "Tiny Lute" (20674). Gives "Redblade's Legacy" (18083).
10. eastkarana/"Tenal Redblade", hand "Redblade's Legacy" (18083). Gives "Totem of the Freezing War" (20680).
11. Loot "Heart of Frost" (10549) from "A Goblin Wizard" in `permafrost`.
12. eastkarana/"Tenal Redblade", hand "Heart of Frost" (10549) + "Totem of the Freezing War" (20680). Gives "Totem of Fiery War" (20681).
13. Loot "Red Dragon Scales" (11622) from "Echo of Nortlav" in `hole`.
14. Loot "Red Dragon Scales" (11622) from "Lord Nagafen" in `soldungb`.
15. Loot "Red Dragon Scales" (11622) from "Melalafen" in `westwastes`.
16. Loot "Red Dragon Scales" (11622) from "Talendor" in `skyfire`.
17. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
18. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `steamfont`.
19. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `tox`.
20. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `toxxulia`.
21. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
22. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). The combine does not fail.
23. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
24. northro/"Verrell Cogswin", hand "Water Flask" (13006). Sets `Green_Scale_Quest` to `1`.
25. northro/"Verrell Cogswin", hand "Red Dragon Scales" (11622). Sets `Green_Scale_Quest` to `2`.
26. northro/"Verrell Cogswin", say "Adhesive". Requires `Green_Scale_Quest` ==2. Requires `Green_Scale_Quest` set. Gives "Verrell's Box of Potions" (67387).
27. Loot "Fractured Centaur Hoof" (67388) from "Centaur Archer" in `southkarana`.
28. Loot "Fractured Centaur Hoof" (67388) from "Centaur Charger" in `southkarana`.
29. Loot "Fractured Centaur Hoof" (67388) from "Centaur Courser" in `southkarana`.
30. Loot "Fractured Centaur Hoof" (67388) from "Centaur Foal" in `southkarana`.
31. Loot "Fractured Centaur Hoof" (67388) from "Centaur Sheltie" in `southkarana`.
32. Loot "Fire Giant Embers" (67389) from "A Fire Giant Warlord" (NPC 278023) in `soldungc`. Drop cache: 28.35% chance per kill.
33. Loot "Jagged Permafrost Shards" (67390) from "The Chilling Terror" in `permafrost`.
34. Combine in Oven (15): "Fractured Centaur Hoof" (67388), "Fire Giant Embers" (67389), "Jagged Permafrost Shards" (67390). Produces "Glue Powder" (67391). Requires Baking. The combine does not fail.
35. Common item: Barley (16590). Listed in 28 zones.
36. Common item: Deep Fungus Mold (67393). Listed in 28 zones.
37. Common item: Distilled Spirits (67394). Listed in 28 zones.
38. Combine in Brew Barrel (19): "Barley" (16590), "Deep Fungus Mold" (67393), "Distilled Spirits" (67394). Produces "Deep Barley Brew" (67392). Requires Brewing, trivial 110.
39. northro/"Verrell Cogswin", say "Adhesive". Requires `Green_Scale_Quest` ==2. Requires `Green_Scale_Quest` set. Gives "Potion Vial" (67395).
40. Combine in "Verrell's Box of Potions" (67387): "Glue Powder" (67391), "Deep Barley Brew" (67392), "Potion Vial" (67395). Produces "Thick Adhesive" (67386). The combine does not fail.
41. northro/"Verrell Cogswin", hand "Thick Adhesive" (67386). Gives "Grey Scale Pieces" (67385).
42. northro/"Verrell Cogswin", hand "Thick Adhesive" (67386). Gives "Thick Adhesive" (67396).
43. Combine in "Verrell's Box of Potions" (67387): "Grey Scale Pieces" (67385), "Thick Adhesive" (67396). Produces "Grey Colored Scales" (67384). The combine does not fail.
44. northro/"Verrell Cogswin", hand "Grey Colored Scales" (67384). Gives "Green Dragon Scales" (11582).
45. eastkarana/"Tenal Redblade", hand "Green Dragon Scales" (11582) + "Red Dragon Scales" (11622) + "Totem of Fiery War" (20681). Gives "Mark of the Sword" (20683).
46. Loot "Hand of the Maestro" (20676) from "Hand of the Maestro" in `hateplane`.
47. Loot "Hand of the Maestro" (20676) from "Hand of the Maestro" in `hateplaneb`.
48. eastkarana/"Tenal Redblade", hand "Hand of the Maestro" (20676) + "Mark of the Sword" (20683). Gives "Tenal's note to Kargek" (20684).
49. Loot "Spiroc Wingblade" (20679) from "The Spiroc Lord" in `airplane`.
50. freeporteast/"Kargek Redblade", hand "Spiroc Wingblade" (20679) + "Tenal's note to Kargek" (20684). Gives "Red Scabbard" (17859).
51. Combine in "Red Scabbard" (17859): "Jagged Blade of War" (10908). Produces "Blade of Tactics" (10909), "Blade of Strategy" (10910). The combine does not fail.
52. Combine in "Red Scabbard" (17859): "Blade of Tactics" (10909), "Blade of Strategy" (10910). Produces "Jagged Blade of War" (10908). The combine does not fail.
53. lakerathe/"Triathalon Swim Goggles", say "Hail". Gives "Rebreather" (16889).
54. Loot "Block of Permafrost" (20665) from "Lady Vox" in `permafrost`.
55. Loot "Block of Permafrost" (20665) from "An Ice Giant" in `permafrost`.
56. Common item: Keg of Vox Tail Ale (20664). Listed in 13 zones.
57. oceanoftears/"Denken Strongpick", hand "Rebreather" (16889) + "Keg of Vox Tail Ale" (20664) + "Block of Permafrost" (20665). Gives "Ancient Sword Blade" (20667).
58. Loot "Ancient Blade" (20670) from "Queen Velazul Di'zok" in `chardok`.
59. Ground spawn of "Unjeweled Dragon Head Hilt" (20668) in `lakerathe`.
60. Loot "Apothic Crown" (1239) from "Magi P'Tasa" (NPC 186157) in `hateplaneb`. Drop cache: 19.16% chance per kill.
61. poknowledge/"Arch Mage Deidus", hand "Apothic Crown" (1239). Gives "Diamond" (10037).
62. Loot "Scroll of the Ox" (49007) from "A Sturdy Chest" in `stillmoona`.
63. Loot "Scroll of the Boar" (49008) from "A Sturdy Chest" in `stillmoona`.
64. Loot "Scroll of the Dragon" (49009) from "A Sturdy Chest" in `stillmoona`.
65. Loot "Scroll of the Tiger" (49010) from "A Sturdy Chest" in `stillmoona`.
66. Hand "Scroll of the Ox" (49007) + "Scroll of the Boar" (49008) + "Scroll of the Dragon" (49009) + "Scroll of the Tiger" (49010) to stillmoona/"The Keeper Of Strength". Spawns "A Spirit Keeper" (338169). Loot "Black Sapphire" (10036) from "A Spirit Keeper".
67. 42 alternative loot source(s) also yield Black Sapphire (10036).
68. Say "Tm Devrak Death" to rujd/"Rujd".
69. Spawns "spawn chest with Heavy Orcish Prison Key" (245241).
70. Loot "Heavy Orcish Prison Key" (59571) from "spawn chest with Heavy Orcish Prison Key".
71. 2 alternative loot source(s) also yield Heavy Orcish Prison Key (59571).
72. Hand "Heavy Orcish Prison Key" (59571) to rujd/"Rujd". Spawns "Prison Guard Talkor" (245290). Loot "Jacinth" (10053) from "Prison Guard Talkor".
73. 54 alternative loot source(s) also yield Jacinth (10053).
74. freeporteast/"Wenden Blackhammer", hand "Black Sapphire" (10036) + "Diamond" (10037) + "Jacinth" (10053) + "Unjeweled Dragon Head Hilt" (20668). Gives "Jeweled Dragon Head Hilt" (20671).
75. Ground spawn of "Severely Damaged Dragon Head Hilt" (20669) in `timorous`.
76. Loot "Giant Sized Monocle" (20678) from "A Mountain Giant Patriarch" in `dreadlands`.
77. frontiermtns/"Mentrax Mountainbone", hand "Giant Sized Monocle" (20678). Gives "Rejesiam Ore" (20666).
78. Loot "Ball of Everliving Golem" (20677) from "Dread" in `fearplane`.
79. Loot "Ball of Everliving Golem" (20677) from "Fright" in `fearplane`.
80. Loot "Ball of Everliving Golem" (20677) from "Terror" in `fearplane`.
81. freeporteast/"Wenden Blackhammer", hand "Rejesiam Ore" (20666) + "Severely Damaged Dragon Head Hilt" (20669) + "Ball of Everliving Golem" (20677). Gives "Finely Crafted Dragon Head Hilt" (20672).
82. Combine in "Red Scabbard" (17859): "Ancient Sword Blade" (20667), "Ancient Blade" (20670), "Jeweled Dragon Head Hilt" (20671), "Finely Crafted Dragon Head Hilt" (20672). Produces "Jagged Blade of War" (10908). The combine does not fail.
83. freeporteast/"Gartrog Smitehammer", hand "Jagged Blade of War" (10908) + "Red Scabbard" (17859). Gives "Red Scabbard" (17869).
84. freeporteast/"Gartrog Smitehammer", hand "Jagged Blade of War" (10908) + "Red Scabbard" (17859). Gives "Jagged Blade of War" (66175).
85. Combine in "Red Scabbard" (17869): "Jagged Blade of War" (66175). Produces "Blade of Tactics" (66176), "Blade of Strategy" (66177). Requires Pottery. The combine does not fail.
86. draniksscar/"Korbuk Brimblade", say "Work". Sets `warrior_pre` to `1`.
87. Loot "Korbuk's Weapon Plans" (60285) from "The Diaku Overseer" in `potactics`.
88. draniksscar/"Korbuk Brimblade", hand "Korbuk's Weapon Plans" (60285). Sets `warrior_pre` to `2`.
89. Loot "Elegant Shank" (60286) from "Shoqui the Forgotten" in `hatesfury`.
90. draniksscar/"Korbuk Brimblade", hand "Elegant Shank" (60286). Sets `warrior_pre` to `3`.
91. Loot "Redblade Family Sword" (60287) from "Drevlon Knacknabber" in `eastkarana`.
92. freeporteast/"Kargek Redblade", hand "Redblade Family Sword" (60287). Requires `warrior_pre` set. Requires `warrior_pre` ==3. Gives "Emblazoned Champion's Hilt" (60288).
93. draniksscar/"Korbuk Brimblade", hand "Emblazoned Champion's Hilt" (60288). Sets `warrior_pre` to `4`.
94. thurgadina/"Dardek Bladewright", hand "Korbuk's Weapon Plans" (60285) + "Elegant Shank" (60286) + "Emblazoned Champion's Hilt" (60288). Sets `warrior_pre` to `5`.
95. thurgadina/"Dardek Bladewright", hand "Korbuk's Weapon Plans" (60285) + "Elegant Shank" (60286) + "Emblazoned Champion's Hilt" (60288). Requires `warrior_pre` ==4. Gives "Dardek's Forged Blade" (60292).
96. draniksscar/"Korbuk Brimblade", hand "Dardek's Forged Blade" (60292). Sets `warrior_pre` to `6`.
97. draniksscar/"Korbuk Brimblade", say "Work". Sets `warrior_epic` to `1`.
98. Kill bloodfields/"Girplan Slasher". Spawns "Girplan Devourer" (301063).
99. Loot "Decrepit Hilt" (60307) from "Girplan Devourer".
100. firiona/"Corfia Nultethen", hand "Decrepit Hilt" (60307). Sets `warrior_epic` to `9`.
101. Unresolved cyclic prerequisite: `warrior_epic_gulak` ==1.
102. firiona/"Corfia Nultethen", say "Galuk Drek". Sets `warrior_epic_veksar` to `1`.
103. veksar/"Player", on enter. Sets `warrior_epic_gulak` to `1`.
104. Spawns "Decaying Lord Galuk Drek, not be in db yet" (109906) in `veksar` on enter.
105. Loot "Skeletal Tome of Galuk Drek" (60310) from "Decaying Lord Galuk Drek, not be in db yet".
106. firiona/"Corfia Nultethen", hand "Skeletal Tome of Galuk Drek" (60310). Requires `warrior_epic` set. Requires `warrior_epic` ==9. Gives "Glistening Hilt" (60311).

### "Gemming Tool" (60316)

1. Combine in Forge (17): "Fine Steel Two Handed Sword" (5351), "Water Flask" (13006). Produces "Small Brick of High Quality Ore" (10468) x2, "Small Piece of High Quality Ore" (22229). Requires Blacksmithing, trivial 21.
2. Combine in Forge (17): "Smithing Chisel" (7052), "Small Brick of High Quality Ore" (10468). Hands back "Smithing Chisel" (7052). Produces "Small Piece of High Quality Ore" (22229) x2. Requires Blacksmithing, trivial 27.
3. 4 other recipes also produce Small Piece of High Quality Ore (22229).
4. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
5. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `steamfont`.
6. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `tox`.
7. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `toxxulia`.
8. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
9. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). The combine does not fail.
10. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
11. Combine in Royal Qeynos Forge (40): "Small Piece of High Quality Ore" (22229), "Water Flask" (13006). Produces "High Quality Metal Bits" (22230). Requires Blacksmithing, trivial 20.
12. Common item: Gemming Mold (60317). Listed in 4 zones.
13. Combine in Forge (17): "High Quality Metal Bits" (22230), "Water Flask" (13006), "Gemming Mold" (60317). Produces "Gemming Tool" (60316). Requires Blacksmithing, trivial 115.

### "Hilt of Eternal Power" (60320)

1. Unresolved cyclic prerequisite: `warrior_epic` ==17.
2. Ground spawn of "Frozen Pestle" (60323) in `iceclad`.
3. iceclad/"Fazzle Thumpkin", hand "Frozen Pestle" (60323). Sets `warrior_epic` to `18`.
4. Loot "Kreljnok's Muddled Rage" (60322) from "Possessed Brute" in `provinggrounds`.
5. draniksscar/"Korbuk Brimblade", hand "Kreljnok's Muddled Rage" (60322). Sets `warrior_epic` to `17`.
6. Unresolved cyclic prerequisite: `warrior_pre` ==6.
7. freeporteast/"Kargek Redblade", say "Favor". Gives "Wax Sealed Note" (20673).
8. feerrott/"Oknoggin Stonesmacker", hand "Wax Sealed Note" (20673). Gives "Tiny Lute" (20674).
9. freeporteast/"Kargek Redblade", hand "Tiny Lute" (20674). Gives "Redblade's Legacy" (18083).
10. eastkarana/"Tenal Redblade", hand "Redblade's Legacy" (18083). Gives "Totem of the Freezing War" (20680).
11. Loot "Heart of Frost" (10549) from "A Goblin Wizard" in `permafrost`.
12. eastkarana/"Tenal Redblade", hand "Heart of Frost" (10549) + "Totem of the Freezing War" (20680). Gives "Totem of Fiery War" (20681).
13. Loot "Red Dragon Scales" (11622) from "Echo of Nortlav" in `hole`.
14. Loot "Red Dragon Scales" (11622) from "Lord Nagafen" in `soldungb`.
15. Loot "Red Dragon Scales" (11622) from "Melalafen" in `westwastes`.
16. Loot "Red Dragon Scales" (11622) from "Talendor" in `skyfire`.
17. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
18. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `steamfont`.
19. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `tox`.
20. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `toxxulia`.
21. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
22. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). The combine does not fail.
23. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
24. northro/"Verrell Cogswin", hand "Water Flask" (13006). Sets `Green_Scale_Quest` to `1`.
25. northro/"Verrell Cogswin", hand "Red Dragon Scales" (11622). Sets `Green_Scale_Quest` to `2`.
26. northro/"Verrell Cogswin", say "Adhesive". Requires `Green_Scale_Quest` ==2. Requires `Green_Scale_Quest` set. Gives "Verrell's Box of Potions" (67387).
27. Loot "Fractured Centaur Hoof" (67388) from "Centaur Archer" in `southkarana`.
28. Loot "Fractured Centaur Hoof" (67388) from "Centaur Charger" in `southkarana`.
29. Loot "Fractured Centaur Hoof" (67388) from "Centaur Courser" in `southkarana`.
30. Loot "Fractured Centaur Hoof" (67388) from "Centaur Foal" in `southkarana`.
31. Loot "Fractured Centaur Hoof" (67388) from "Centaur Sheltie" in `southkarana`.
32. Loot "Fire Giant Embers" (67389) from "A Fire Giant Warlord" (NPC 278023) in `soldungc`. Drop cache: 28.35% chance per kill.
33. Loot "Jagged Permafrost Shards" (67390) from "The Chilling Terror" in `permafrost`.
34. Combine in Oven (15): "Fractured Centaur Hoof" (67388), "Fire Giant Embers" (67389), "Jagged Permafrost Shards" (67390). Produces "Glue Powder" (67391). Requires Baking. The combine does not fail.
35. Common item: Barley (16590). Listed in 28 zones.
36. Common item: Deep Fungus Mold (67393). Listed in 28 zones.
37. Common item: Distilled Spirits (67394). Listed in 28 zones.
38. Combine in Brew Barrel (19): "Barley" (16590), "Deep Fungus Mold" (67393), "Distilled Spirits" (67394). Produces "Deep Barley Brew" (67392). Requires Brewing, trivial 110.
39. northro/"Verrell Cogswin", say "Adhesive". Requires `Green_Scale_Quest` ==2. Requires `Green_Scale_Quest` set. Gives "Potion Vial" (67395).
40. Combine in "Verrell's Box of Potions" (67387): "Glue Powder" (67391), "Deep Barley Brew" (67392), "Potion Vial" (67395). Produces "Thick Adhesive" (67386). The combine does not fail.
41. northro/"Verrell Cogswin", hand "Thick Adhesive" (67386). Gives "Grey Scale Pieces" (67385).
42. northro/"Verrell Cogswin", hand "Thick Adhesive" (67386). Gives "Thick Adhesive" (67396).
43. Combine in "Verrell's Box of Potions" (67387): "Grey Scale Pieces" (67385), "Thick Adhesive" (67396). Produces "Grey Colored Scales" (67384). The combine does not fail.
44. northro/"Verrell Cogswin", hand "Grey Colored Scales" (67384). Gives "Green Dragon Scales" (11582).
45. eastkarana/"Tenal Redblade", hand "Green Dragon Scales" (11582) + "Red Dragon Scales" (11622) + "Totem of Fiery War" (20681). Gives "Mark of the Sword" (20683).
46. Loot "Hand of the Maestro" (20676) from "Hand of the Maestro" in `hateplane`.
47. Loot "Hand of the Maestro" (20676) from "Hand of the Maestro" in `hateplaneb`.
48. eastkarana/"Tenal Redblade", hand "Hand of the Maestro" (20676) + "Mark of the Sword" (20683). Gives "Tenal's note to Kargek" (20684).
49. Loot "Spiroc Wingblade" (20679) from "The Spiroc Lord" in `airplane`.
50. freeporteast/"Kargek Redblade", hand "Spiroc Wingblade" (20679) + "Tenal's note to Kargek" (20684). Gives "Red Scabbard" (17859).
51. Combine in "Red Scabbard" (17859): "Jagged Blade of War" (10908). Produces "Blade of Tactics" (10909), "Blade of Strategy" (10910). The combine does not fail.
52. Combine in "Red Scabbard" (17859): "Blade of Tactics" (10909), "Blade of Strategy" (10910). Produces "Jagged Blade of War" (10908). The combine does not fail.
53. lakerathe/"Triathalon Swim Goggles", say "Hail". Gives "Rebreather" (16889).
54. Loot "Block of Permafrost" (20665) from "Lady Vox" in `permafrost`.
55. Loot "Block of Permafrost" (20665) from "An Ice Giant" in `permafrost`.
56. Common item: Keg of Vox Tail Ale (20664). Listed in 13 zones.
57. oceanoftears/"Denken Strongpick", hand "Rebreather" (16889) + "Keg of Vox Tail Ale" (20664) + "Block of Permafrost" (20665). Gives "Ancient Sword Blade" (20667).
58. Loot "Ancient Blade" (20670) from "Queen Velazul Di'zok" in `chardok`.
59. Ground spawn of "Unjeweled Dragon Head Hilt" (20668) in `lakerathe`.
60. Loot "Apothic Crown" (1239) from "Magi P'Tasa" (NPC 186157) in `hateplaneb`. Drop cache: 19.16% chance per kill.
61. poknowledge/"Arch Mage Deidus", hand "Apothic Crown" (1239). Gives "Diamond" (10037).
62. Loot "Scroll of the Ox" (49007) from "A Sturdy Chest" in `stillmoona`.
63. Loot "Scroll of the Boar" (49008) from "A Sturdy Chest" in `stillmoona`.
64. Loot "Scroll of the Dragon" (49009) from "A Sturdy Chest" in `stillmoona`.
65. Loot "Scroll of the Tiger" (49010) from "A Sturdy Chest" in `stillmoona`.
66. Hand "Scroll of the Ox" (49007) + "Scroll of the Boar" (49008) + "Scroll of the Dragon" (49009) + "Scroll of the Tiger" (49010) to stillmoona/"The Keeper Of Strength". Spawns "A Spirit Keeper" (338169). Loot "Black Sapphire" (10036) from "A Spirit Keeper".
67. 42 alternative loot source(s) also yield Black Sapphire (10036).
68. Say "Tm Devrak Death" to rujd/"Rujd".
69. Spawns "spawn chest with Heavy Orcish Prison Key" (245241).
70. Loot "Heavy Orcish Prison Key" (59571) from "spawn chest with Heavy Orcish Prison Key".
71. 2 alternative loot source(s) also yield Heavy Orcish Prison Key (59571).
72. Hand "Heavy Orcish Prison Key" (59571) to rujd/"Rujd". Spawns "Prison Guard Talkor" (245290). Loot "Jacinth" (10053) from "Prison Guard Talkor".
73. 54 alternative loot source(s) also yield Jacinth (10053).
74. freeporteast/"Wenden Blackhammer", hand "Black Sapphire" (10036) + "Diamond" (10037) + "Jacinth" (10053) + "Unjeweled Dragon Head Hilt" (20668). Gives "Jeweled Dragon Head Hilt" (20671).
75. Ground spawn of "Severely Damaged Dragon Head Hilt" (20669) in `timorous`.
76. Loot "Giant Sized Monocle" (20678) from "A Mountain Giant Patriarch" in `dreadlands`.
77. frontiermtns/"Mentrax Mountainbone", hand "Giant Sized Monocle" (20678). Gives "Rejesiam Ore" (20666).
78. Loot "Ball of Everliving Golem" (20677) from "Dread" in `fearplane`.
79. Loot "Ball of Everliving Golem" (20677) from "Fright" in `fearplane`.
80. Loot "Ball of Everliving Golem" (20677) from "Terror" in `fearplane`.
81. freeporteast/"Wenden Blackhammer", hand "Rejesiam Ore" (20666) + "Severely Damaged Dragon Head Hilt" (20669) + "Ball of Everliving Golem" (20677). Gives "Finely Crafted Dragon Head Hilt" (20672).
82. Combine in "Red Scabbard" (17859): "Ancient Sword Blade" (20667), "Ancient Blade" (20670), "Jeweled Dragon Head Hilt" (20671), "Finely Crafted Dragon Head Hilt" (20672). Produces "Jagged Blade of War" (10908). The combine does not fail.
83. freeporteast/"Gartrog Smitehammer", hand "Jagged Blade of War" (10908) + "Red Scabbard" (17859). Gives "Red Scabbard" (17869).
84. freeporteast/"Gartrog Smitehammer", hand "Jagged Blade of War" (10908) + "Red Scabbard" (17859). Gives "Jagged Blade of War" (66175).
85. Combine in "Red Scabbard" (17869): "Jagged Blade of War" (66175). Produces "Blade of Tactics" (66176), "Blade of Strategy" (66177). Requires Pottery. The combine does not fail.
86. draniksscar/"Korbuk Brimblade", say "Work". Sets `warrior_pre` to `1`.
87. Loot "Korbuk's Weapon Plans" (60285) from "The Diaku Overseer" in `potactics`.
88. draniksscar/"Korbuk Brimblade", hand "Korbuk's Weapon Plans" (60285). Sets `warrior_pre` to `2`.
89. Loot "Elegant Shank" (60286) from "Shoqui the Forgotten" in `hatesfury`.
90. draniksscar/"Korbuk Brimblade", hand "Elegant Shank" (60286). Sets `warrior_pre` to `3`.
91. Loot "Redblade Family Sword" (60287) from "Drevlon Knacknabber" in `eastkarana`.
92. freeporteast/"Kargek Redblade", hand "Redblade Family Sword" (60287). Requires `warrior_pre` set. Requires `warrior_pre` ==3. Gives "Emblazoned Champion's Hilt" (60288).
93. draniksscar/"Korbuk Brimblade", hand "Emblazoned Champion's Hilt" (60288). Sets `warrior_pre` to `4`.
94. thurgadina/"Dardek Bladewright", hand "Korbuk's Weapon Plans" (60285) + "Elegant Shank" (60286) + "Emblazoned Champion's Hilt" (60288). Sets `warrior_pre` to `5`.
95. thurgadina/"Dardek Bladewright", hand "Korbuk's Weapon Plans" (60285) + "Elegant Shank" (60286) + "Emblazoned Champion's Hilt" (60288). Requires `warrior_pre` ==4. Gives "Dardek's Forged Blade" (60292).
96. draniksscar/"Korbuk Brimblade", hand "Dardek's Forged Blade" (60292). Sets `warrior_pre` to `6`.
97. draniksscar/"Korbuk Brimblade", say "Work". Sets `warrior_epic` to `1`.
98. Kill bloodfields/"Girplan Slasher". Spawns "Girplan Devourer" (301063).
99. Loot "Decrepit Hilt" (60307) from "Girplan Devourer".
100. firiona/"Corfia Nultethen", hand "Decrepit Hilt" (60307). Sets `warrior_epic` to `9`.
101. Unresolved cyclic prerequisite: `warrior_epic_gulak` ==1.
102. firiona/"Corfia Nultethen", say "Galuk Drek". Sets `warrior_epic_veksar` to `1`.
103. veksar/"Player", on enter. Sets `warrior_epic_gulak` to `1`.
104. Spawns "Decaying Lord Galuk Drek, not be in db yet" (109906) in `veksar` on enter.
105. Loot "Skeletal Tome of Galuk Drek" (60310) from "Decaying Lord Galuk Drek, not be in db yet".
106. firiona/"Corfia Nultethen", hand "Skeletal Tome of Galuk Drek" (60310). Requires `warrior_epic` set. Requires `warrior_epic` ==9. Gives "Glistening Hilt" (60311).
107. butcher/"Gridbar Galund", hand "Glistening Hilt" (60311). Requires `warrior_epic` set. Requires `warrior_epic` >=13. Gives "Carved Keg Stamp" (60318).
108. shadowhaven/"Koren Galund", hand "Carved Keg Stamp" (60318). Requires `warrior_epic` set. Requires `warrior_epic` >=13. Gives "Tube of Setting Solution" (60319).
109. butcher/"Gridbar Galund", hand "Tube of Setting Solution" (60319). Requires `warrior_epic` set. Requires `warrior_epic` >=13. Gives "Hilt of Eternal Power" (60320).

### "Kreljnok's Focused Rage" (60327)

1. Unresolved cyclic prerequisite: `warrior_epic` ==17.
2. Ground spawn of "Frozen Pestle" (60323) in `iceclad`.
3. iceclad/"Fazzle Thumpkin", hand "Frozen Pestle" (60323). Sets `warrior_epic` to `18`.
4. Loot "Kreljnok's Muddled Rage" (60322) from "Possessed Brute" in `provinggrounds`.
5. draniksscar/"Korbuk Brimblade", hand "Kreljnok's Muddled Rage" (60322). Sets `warrior_epic` to `17`.
6. iceclad/"Fazzle Thumpkin", say "Map". Requires `warrior_epic` ==18. Gives "Fazzle's Map of East Wastes" (60324).
7. Spawns "Larnik the Recluse" (116609) in `eastwastes` on enter.
8. Loot "Larnik's Locked Purification Kit" (60325) from "Larnik the Recluse".
9. draniksscar/"Korbuk Brimblade", hand "Larnik's Locked Purification Kit" (60325). Requires `warrior_epic` >=18. Gives "Larnik's Unlocked Purification Kit" (60326).
10. Combine in "Larnik's Unlocked Purification Kit" (60326): "Kreljnok's Muddled Rage" (60322). Produces "Kreljnok's Focused Rage" (60327). The combine does not fail.

### "Raging Sword of Eternal Power" (60329)

1. global/"Global Player", combine recipe 19902. Sets `warrior_epic` to `21`.
2. Loot "Champion's Sword of Eternal Power" (60321) from "Krekk Brimblade" in `dranik`.
3. Unresolved cyclic prerequisite: `warrior_epic` ==17.
4. Ground spawn of "Frozen Pestle" (60323) in `iceclad`.
5. iceclad/"Fazzle Thumpkin", hand "Frozen Pestle" (60323). Sets `warrior_epic` to `18`.
6. Loot "Kreljnok's Muddled Rage" (60322) from "Possessed Brute" in `provinggrounds`.
7. draniksscar/"Korbuk Brimblade", hand "Kreljnok's Muddled Rage" (60322). Sets `warrior_epic` to `17`.
8. iceclad/"Fazzle Thumpkin", say "Map". Requires `warrior_epic` ==18. Gives "Fazzle's Map of East Wastes" (60324).
9. Spawns "Larnik the Recluse" (116609) in `eastwastes` on enter.
10. Loot "Larnik's Locked Purification Kit" (60325) from "Larnik the Recluse".
11. draniksscar/"Korbuk Brimblade", hand "Larnik's Locked Purification Kit" (60325). Requires `warrior_epic` >=18. Gives "Larnik's Unlocked Purification Kit" (60326).
12. Combine in "Larnik's Unlocked Purification Kit" (60326): "Kreljnok's Muddled Rage" (60322). Produces "Kreljnok's Focused Rage" (60327). The combine does not fail.
13. draniksscar/"Korbuk Brimblade", hand "Champion's Sword of Eternal Power" (60321) + "Kreljnok's Focused Rage" (60327). Requires `warrior_epic` >=19. Gives "Raging Sword of Eternal Power" (60329).

## `warrior_pre`

Values written: 1, 2, 3, 4, 5, 6.

### 2. korbuk brimblade — hand 60285

Zone: `draniksscar`.

Sets `warrior_pre` to `2`.

- Needs `warrior_pre` ==1.
- Turn in x1: Korbuk's Weapon Plans (60285).
In script order:

1. Sets `warrior_pre` to `2`.
2. Gives Korbuk's Weapon Plans (60285).


How the items are reached:

- Korbuk's Weapon Plans (60285)
  - Loot "Korbuk's Weapon Plans" (60285) from "The Diaku Overseer" in `potactics`.

### 3. korbuk brimblade — hand 60286

Zone: `draniksscar`.

Sets `warrior_pre` to `3`.

- Needs `warrior_pre` ==2.
- Turn in x1: Elegant Shank (60286).
In script order:

1. Sets `warrior_pre` to `3`.
2. Gives Elegant Shank (60286).


How the items are reached:

- Elegant Shank (60286)
  - Loot "Elegant Shank" (60286) from "Shoqui the Forgotten" in `hatesfury`.

### 4. korbuk brimblade — hand 60288

Zone: `draniksscar`.

Sets `warrior_pre` to `4`.

- Needs `warrior_pre` ==3.
- Turn in x1: Emblazoned Champion's Hilt (60288).
In script order:

1. Sets `warrior_pre` to `4`.
2. Gives Emblazoned Champion's Hilt (60288).


How the items are reached:

- Emblazoned Champion's Hilt (60288)
  - Prerequisite: "Emblazoned Champion's Hilt" (60288). See section 0.

### 5. dardek bladewright — hand 60285+60286+60288

Zone: `thurgadina`.

Sets `warrior_pre` to `5`.

- Needs `warrior_pre` ==4.
- Turn in x1: Korbuk's Weapon Plans (60285).
- Turn in x1: Elegant Shank (60286).
- Turn in x1: Emblazoned Champion's Hilt (60288).
In script order:

1. Sets `warrior_pre` to `5`.
2. Gives Dardek's Forged Blade (60292).


How the items are reached:

- Korbuk's Weapon Plans (60285)
  - Loot "Korbuk's Weapon Plans" (60285) from "The Diaku Overseer" in `potactics`.
- Elegant Shank (60286)
  - Loot "Elegant Shank" (60286) from "Shoqui the Forgotten" in `hatesfury`.
- Emblazoned Champion's Hilt (60288)
  - Prerequisite: "Emblazoned Champion's Hilt" (60288). See section 0.

### 6. korbuk brimblade — hand 60292

Zone: `draniksscar`.

Sets `warrior_pre` to `6`.

- Needs `warrior_pre` ==5.
- Turn in x1: Dardek's Forged Blade (60292).
In script order:

1. Sets `warrior_pre` to `6`.
2. Gives Korbuk's Blade of Mastery (60293).


How the items are reached:

- Dardek's Forged Blade (60292)
  - Prerequisite: "Dardek's Forged Blade" (60292). See section 0.

### 1. korbuk brimblade — say work

Zone: `draniksscar`.

> Yeah, ok. You look like da respectable type. I wish it was an easy story to tell, but me thinks it

Sets `warrior_pre` to `1`.

- Needs `warrior_pre` ==6.
- Needs Blade of Strategy (10910).
- Needs Blade of Tactics (10909).
- Needs Blade of Tactics (66176).
- Needs Blade of Strategy (66177).
- Needs Jagged Blade of War (10908).
- Needs Jagged Blade of War (66175).
- Needs `warrior_epic` unset.
- Needs `warrior_pre` unset.
In script order:

1. Sets `warrior_epic` to `1`.
2. Sets `warrior_pre` to `1`.


How the items are reached:

- Blade of Strategy (10910)
  - Prerequisite: "Blade of Strategy" (10910). See section 0.
- Blade of Tactics (10909)
  - Prerequisite: "Blade of Tactics" (10909). See section 0.
- Blade of Tactics (66176)
  - Prerequisite: "Blade of Tactics" (66176). See section 0.
- Blade of Strategy (66177)
  - Prerequisite: "Blade of Strategy" (66177). See section 0.
- Jagged Blade of War (10908)
  - Prerequisite: "Jagged Blade of War" (10908). See section 0.
- Jagged Blade of War (66175)
  - Prerequisite: "Jagged Blade of War" (66175). See section 0.

Subquest `warrior_epic`:

#### `warrior_epic`

Values written: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21.

##### 1. korbuk brimblade — say work

Zone: `draniksscar`.

> Yeah, ok. You look like da respectable type. I wish it was an easy story to tell, but me thinks it

Sets `warrior_epic` to `1`.

- Needs `warrior_pre` ==6.
- Needs Blade of Strategy (10910).
- Needs Blade of Tactics (10909).
- Needs Blade of Tactics (66176).
- Needs Blade of Strategy (66177).
- Needs Jagged Blade of War (10908).
- Needs Jagged Blade of War (66175).
- Needs `warrior_epic` unset.
- Needs `warrior_pre` unset.
In script order:

1. Sets `warrior_epic` to `1`.
2. Sets `warrior_pre` to `1`.


How the items are reached:

- Blade of Strategy (10910)
  - Prerequisite: "Blade of Strategy" (10910). See section 0.
- Blade of Tactics (10909)
  - Prerequisite: "Blade of Tactics" (10909). See section 0.
- Blade of Tactics (66176)
  - Prerequisite: "Blade of Tactics" (66176). See section 0.
- Blade of Strategy (66177)
  - Prerequisite: "Blade of Strategy" (66177). See section 0.
- Jagged Blade of War (10908)
  - Prerequisite: "Jagged Blade of War" (10908). See section 0.
- Jagged Blade of War (66175)
  - Prerequisite: "Jagged Blade of War" (66175). See section 0.

This step also depends on `warrior_pre`, shown above.

##### 2. korbuk brimblade — hand 60295+60296+60297+60298

Zone: `draniksscar`.

Sets `warrior_epic` to `2`.

- Needs `warrior_epic` >=1.
- Turn in x1: Decomposing Page I (60295).
- Turn in x1: Decomposing Page II (60296).
- Turn in x1: Decomposing Page III (60297).
- Turn in x1: Decomposing Cover (60298).
In script order:

1. Sets `warrior_epic` to `2`.
2. Gives Decomposing Page I (60295).
3. Gives Decomposing Page II (60296).
4. Gives Decomposing Page III (60297).
5. Gives Decomposing Cover (60298).


How the items are reached:

- Decomposing Page I (60295)
  - Ground spawn of "Decomposing Page I" (60295) in `draniksscar`.
- Decomposing Page II (60296)
  - Ground spawn of "Decomposing Page II" (60296) in `draniksscar`.
- Decomposing Page III (60297)
  - Ground spawn of "Decomposing Page III" (60297) in `draniksscar`.
- Decomposing Cover (60298)
  - Ground spawn of "Decomposing Cover" (60298) in `draniksscar`.

##### 3. korbuk brimblade — hand 60303

Zone: `draniksscar`.

Sets `warrior_epic` to `3`.

- Needs `warrior_epic` >=2.
- Turn in x1: Blackfall Blade (60303).
In script order:

1. Sets `warrior_epic` to `3`.
2. Gives Blackfall Blade (60303).


How the items are reached:

- Blackfall Blade (60303)
  - Prerequisite: "Blackfall Blade" (60303). See section 0.

##### 4. kimber whitefoot — hand 60305

Zone: `everfrost`.

Sets `warrior_epic` to `4`.

- Needs `warrior_epic` set.
- Needs `warrior_epic` >=3.
- Needs `warrior_epic` <4.
- Turn in x1: Sealed Vial of Blackfall Blood (60305).
In script order:

1. Sets `warrior_epic` to `4`.


How the items are reached:

- Sealed Vial of Blackfall Blood (60305)
  - Prerequisite: "Sealed Vial of Blackfall Blood" (60305). See section 0.

##### 5. korbuk brimblade — hand 60306

Zone: `draniksscar`.

Sets `warrior_epic` to `5`.

- Needs `warrior_epic` >=4.
- Turn in x1: Potion of Blackfall Spirit (60306).
In script order:

1. Sets `warrior_epic` to `5`.
2. Gives Potion of Blackfall Spirit (60306).


How the items are reached:

- Potion of Blackfall Spirit (60306)
  - Prerequisite: "Potion of Blackfall Spirit" (60306). See section 0.

##### 6. korbuk brimblade — hand 60307

Zone: `draniksscar`.

Sets `warrior_epic` to `6`.

- Needs `warrior_epic` >=5.
- Turn in x1: Decrepit Hilt (60307).
In script order:

1. Sets `warrior_epic` to `6`.
2. Gives Decrepit Hilt (60307).


How the items are reached:

- Decrepit Hilt (60307)
  - Kill bloodfields/"Girplan Slasher". Spawns "Girplan Devourer" (301063).
  - Loot "Decrepit Hilt" (60307) from "Girplan Devourer".

##### 7. corfia nultethen — hand 16503

Zone: `firiona`.

Sets `warrior_epic` to `7`.

- Needs `warrior_epic` set.
- Needs `warrior_epic` >=6.
- Needs `warrior_epic` <7.
- Turn in x1: Platinum Bar (16503).
In script order:

1. Sets `warrior_epic` to `7`.


How the items are reached:

- Platinum Bar (16503)
  - Common item: Platinum Bar (16503). Listed in 30 zones.

##### 8. corfia nultethen — hand 60309

Zone: `firiona`.

Sets `warrior_epic` to `8`.

- Needs `warrior_epic` set.
- Needs `warrior_epic` >=7.
- Needs `warrior_epic` <8.
- Turn in x1: Nocturnal Mask of Acuity (60309).
In script order:

1. Sets `warrior_epic` to `8`.


How the items are reached:

- Nocturnal Mask of Acuity (60309)
  - Prerequisite: "Nocturnal Mask of Acuity" (60309). See section 0.

##### 9. corfia nultethen — hand 60307

Zone: `firiona`.

Sets `warrior_epic` to `9`.

- Needs `warrior_epic` set.
- Needs `warrior_epic` >=8.
- Needs `warrior_epic` <9.
- Turn in x1: Decrepit Hilt (60307).
In script order:

1. Sets `warrior_epic` to `9`.


How the items are reached:

- Decrepit Hilt (60307)
  - Kill bloodfields/"Girplan Slasher". Spawns "Girplan Devourer" (301063).
  - Loot "Decrepit Hilt" (60307) from "Girplan Devourer".

##### 10. korbuk brimblade — hand 60311

Zone: `draniksscar`.

Sets `warrior_epic` to `10`.

- Needs `warrior_epic` >=9.
- Turn in x1: Glistening Hilt (60311).
In script order:

1. Sets `warrior_epic` to `10`.
2. Gives Glistening Hilt (60311).


How the items are reached:

- Glistening Hilt (60311)
  - Prerequisite: "Glistening Hilt" (60311). See section 0.

##### 11. korbuk brimblade — hand 60312+60313+60314+60315

Zone: `draniksscar`.

Sets `warrior_epic` to `11`.

- Needs `warrior_epic` ==10.
- Turn in x1: Stone of Eternal Power: Northeast Eye (60312).
- Turn in x1: Stone of Eternal Power: Northwest Eye (60313).
- Turn in x1: Stone of Eternal Power: Southeast Eye (60314).
- Turn in x1: Stone of Eternal Power: Southwest Eye (60315).
In script order:

1. Sets `warrior_epic` to `11`.
2. Gives Stone of Eternal Power: Northeast Eye (60312).
3. Gives Stone of Eternal Power: Northwest Eye (60313).
4. Gives Stone of Eternal Power: Southeast Eye (60314).
5. Gives Stone of Eternal Power: Southwest Eye (60315).


How the items are reached:

- Stone of Eternal Power: Northeast Eye (60312)
  - Loot "Stone of Eternal Power: Northeast Eye" (60312) from "Dragorn Champion" in `wallofslaughter`.
- Stone of Eternal Power: Northwest Eye (60313)
  - Ground spawn of "Stone of Eternal Power: Northwest Eye" (60313) in `bloodfields`.
- Stone of Eternal Power: Southeast Eye (60314)
  - Ground spawn of "Stone of Eternal Power: Southeast Eye" (60314) in `provinggrounds`.
- Stone of Eternal Power: Southwest Eye (60315)
  - Ground spawn of "Stone of Eternal Power: Southwest Eye" (60315) in `causeway`.

##### 12. gridbar galund — hand 60312+60313+60314+60315

Zone: `butcher`.

Sets `warrior_epic` to `12`.

- Needs `warrior_epic` set.
- Needs `warrior_epic` >=11.
- Turn in x1: Stone of Eternal Power: Northeast Eye (60312).
- Turn in x1: Stone of Eternal Power: Northwest Eye (60313).
- Turn in x1: Stone of Eternal Power: Southeast Eye (60314).
- Turn in x1: Stone of Eternal Power: Southwest Eye (60315).
In script order:

1. Sets `warrior_epic` to `12`.


How the items are reached:

- Stone of Eternal Power: Northeast Eye (60312)
  - Loot "Stone of Eternal Power: Northeast Eye" (60312) from "Dragorn Champion" in `wallofslaughter`.
- Stone of Eternal Power: Northwest Eye (60313)
  - Ground spawn of "Stone of Eternal Power: Northwest Eye" (60313) in `bloodfields`.
- Stone of Eternal Power: Southeast Eye (60314)
  - Ground spawn of "Stone of Eternal Power: Southeast Eye" (60314) in `provinggrounds`.
- Stone of Eternal Power: Southwest Eye (60315)
  - Ground spawn of "Stone of Eternal Power: Southwest Eye" (60315) in `causeway`.

##### 13. gridbar galund — hand 15433+60316

Zone: `butcher`.

Sets `warrior_epic` to `13`.

- Needs `warrior_epic` set.
- Needs `warrior_epic` >=12.
- Turn in x1: Gemming Tool (60316).
- Turn in x1: Spell: Fire (15433).
In script order:

1. Sets `warrior_epic` to `13`.


How the items are reached:

- Gemming Tool (60316)
  - Prerequisite: "Gemming Tool" (60316). See section 0.
- Spell: Fire (15433)
  - Common item: Spell: Fire (15433). Listed in 5 zones.

##### 14. korbuk brimblade — hand 60320

Zone: `draniksscar`.

Sets `warrior_epic` to `14`.

- Needs `warrior_epic` >=13.
- Turn in x1: Hilt of Eternal Power (60320).
In script order:

1. Sets `warrior_epic` to `14`.
2. Gives Hilt of Eternal Power (60320).


How the items are reached:

- Hilt of Eternal Power (60320)
  - Prerequisite: "Hilt of Eternal Power" (60320). See section 0.

##### 15. krekk brimblade — hand 60303+60306+60320

Zone: `dranik`.

Sets `warrior_epic` to `15`.

- Needs `warrior_epic` ==14.
- Turn in x1: Hilt of Eternal Power (60320).
- Turn in x1: Potion of Blackfall Spirit (60306).
- Turn in x1: Blackfall Blade (60303).
In script order:

1. Sets `warrior_epic` to `15`.


How the items are reached:

- Hilt of Eternal Power (60320)
  - Prerequisite: "Hilt of Eternal Power" (60320). See section 0.
- Potion of Blackfall Spirit (60306)
  - Prerequisite: "Potion of Blackfall Spirit" (60306). See section 0.
- Blackfall Blade (60303)
  - Prerequisite: "Blackfall Blade" (60303). See section 0.

##### 17. korbuk brimblade — hand 60322

Zone: `draniksscar`.

Sets `warrior_epic` to `17`.

- Needs `warrior_epic` >=16.
- Turn in x1: Kreljnok's Muddled Rage (60322).
In script order:

1. Sets `warrior_epic` to `17`.
2. Gives Kreljnok's Muddled Rage (60322).


How the items are reached:

- Kreljnok's Muddled Rage (60322)
  - Loot "Kreljnok's Muddled Rage" (60322) from "Possessed Brute" in `provinggrounds`.

##### 18. fazzle thumpkin — hand 60323

Zone: `iceclad`.

Sets `warrior_epic` to `18`.

- Needs `warrior_epic` ==17.
- Turn in x1: Frozen Pestle (60323).
In script order:

1. Sets `warrior_epic` to `18`.


How the items are reached:

- Frozen Pestle (60323)
  - Ground spawn of "Frozen Pestle" (60323) in `iceclad`.

##### 16. korbuk brimblade — say hail

Zone: `draniksscar`.

> You were able to purify da presence, good. Just as I thought, da essence is pure and unadultered. Things are becoming ever clearer da closer we come to unrav...

Sets `warrior_epic` to `16`.

- Needs `warrior_epic` ==18.
- Needs Kreljnok's Focused Rage (60327).
- Needs `warrior_epic` ==15.
- Needs Champion's Sword of Eternal Power (60321).
In script order:

1. Sets `warrior_epic` to `16`.


How the items are reached:

- Kreljnok's Focused Rage (60327)
  - Prerequisite: "Kreljnok's Focused Rage" (60327). See section 0.
- Champion's Sword of Eternal Power (60321)
  - Loot "Champion's Sword of Eternal Power" (60321) from "Krekk Brimblade" in `dranik`.

##### 19. korbuk brimblade — hand 47100

Zone: `draniksscar`.

Sets `warrior_epic` to `19`.

- Needs `warrior_epic` >=18.
- Turn in x1: Globe of Discordant Energy (47100).
In script order:

1. Sets `warrior_epic` to `19`.


How the items are reached:

- Globe of Discordant Energy (47100)
  - Say "Check Lorb" to anguish/"Zone Status".
  - Spawns "Orb of Discordant Energy" (317087).
  - Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy".
  - 4 alternative loot source(s) also yield Globe of Discordant Energy (47100).

##### 20. korbuk brimblade — hand 60321+60327

Zone: `draniksscar`.

Sets `warrior_epic` to `20`.

- Needs `warrior_epic` >=19.
- Turn in x1: Champion's Sword of Eternal Power (60321).
- Turn in x1: Kreljnok's Focused Rage (60327).
In script order:

1. Sets `warrior_epic` to `20`.
2. Gives Raging Sword of Eternal Power (60329).


How the items are reached:

- Champion's Sword of Eternal Power (60321)
  - Loot "Champion's Sword of Eternal Power" (60321) from "Krekk Brimblade" in `dranik`.
- Kreljnok's Focused Rage (60327)
  - Prerequisite: "Kreljnok's Focused Rage" (60327). See section 0.

##### 21. global player — combine recipe 19902

Zone: `global`.

Sets `warrior_epic` to `21`.

In script order:

1. Sets `warrior_epic` to `21`.


Combine:

- `recipe:19902` is combined in Brimblade's Scabbard (60331).
  - Kill causeway/"Korbuk Brimblade". Spawns "Essence of Kreljnok" (303129).
  - Loot "Brimblade's Scabbard" (60331) from "Essence of Kreljnok".
  - Put in x1: Kreljnok's Essence (60330).
    - Kill causeway/"Korbuk Brimblade". Spawns "Essence of Kreljnok" (303129).
    - Loot "Kreljnok's Essence" (60330) from "Essence of Kreljnok".
  - Put in x1: Raging Sword of Eternal Power (60329).
    - Prerequisite: "Raging Sword of Eternal Power" (60329). See section 0.
  - Produces Kreljnok's Sword of Eternal Power (60332).
  - The combine does not fail.

##### Steps on `warrior_epic` that do not change it

- `abysmal` rewina jalmoy, hand 60295+60296+60297+60298 needs `warrior_epic` set.
  - Turn in Decomposing Page I (60295).
  - Turn in Decomposing Page II (60296).
  - Turn in Decomposing Page III (60297).
  - Turn in Decomposing Cover (60298).
  - Gives Recounted History of War (60299).
- `bloodfields` player, on loot needs `warrior_epic` set.
  - Sets `warr_epic_bloodfield` to `1`.
  - Spawns a chest (Epic 1.5) (283157).
  - Sets `monk_epic_bloodfield` to `1`.
  - Sets `monk_epic_keeper` to `1`.
  - Sets `bst_chest_causeway` to `1`.
  - Spawns a chest (epic 2.0) (893).
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
- `butcher` gridbar galund, hand 60311 needs `warrior_epic` set.
  - Turn in Glistening Hilt (60311).
  - Gives Carved Keg Stamp (60318).
- `butcher` gridbar galund, hand 60319 needs `warrior_epic` set.
  - Turn in Tube of Setting Solution (60319).
  - Gives Hilt of Eternal Power (60320).
- `causeway` player, on loot needs `warrior_epic` ==20.
  - Sets `mage_epic_causeway` to `1`.
  - Spawns a chest (Epic 1.5) (283157).
  - Sets `nec_epic_causeway` to `1`.
  - Sets `bard20_chest` to `1`.
  - Spawns a chest (epic 2.0) (893).
  - Sets `warr_chest_causeway` to `1`.
  - Sets `ber_chest_causeway` to `1`.
  - Sets `ench_chest_causeway` to `1`.
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
- `causeway` warr trap, on enter needs `warrior_epic` ==20.
  - Spawns Korbuk (303128).
- `dranik` player, on loot needs `warrior_epic` ==15.
  - Sets `warrior_epic_dranik` to `1`.
  - Spawns a chest (Epic 1.5) (283157).
  - Sets `beast_epic_dran` to `1`.
  - Sets `druid_chest_dranik` to `1`.
  - Sets `shaman_chest_dranik` to `1`.
  - Spawns a chest (Epic 2.0) (893).
  - Sets `nec_chest_dranik` to `1`.
  - Sets `sk_chest_dranik` to `1`.
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
- `draniksscar` korbuk brimblade, hand 60299 needs `warrior_epic` >=2.
  - Turn in Recounted History of War (60299).
- `draniksscar` korbuk brimblade, hand 60301 needs `warrior_epic` >=2.
  - Turn in Blackfall Ore (60301).
  - Gives Blackfall Ore (60301).
  - Gives Smelting Plans (60302).
- `draniksscar` korbuk brimblade, hand 60304 needs `warrior_epic` >=3.
  - Turn in Vial of Blackfall Blood (60304).
  - Gives Sealed Vial of Blackfall Blood (60305).
- `draniksscar` korbuk brimblade, hand 60325 needs `warrior_epic` >=18.
  - Turn in Larnik's Locked Purification Kit (60325).
  - Gives Larnik's Unlocked Purification Kit (60326).
- `draniksscar` korbuk brimblade, say loose needs `warrior_epic` set.
  - Sets `warrior_epic_vxed` to `1`.
- `draniksscar` korbuk brimblade, say rock needs `warrior_epic` set.
  - Gives Energy Receptor (60300).
- `everfrost` kimber whitefoot, say hail needs `warrior_epic` set.
  - Gives Potion of Blackfall Spirit (60306).
- `firiona` corfia nultethen, say galuk drek needs `warrior_epic` set.
  - Sets `warrior_epic_veksar` to `1`.
- `firiona` corfia nultethen, hand 60310 needs `warrior_epic` set.
  - Turn in Skeletal Tome of Galuk Drek (60310).
  - Gives Glistening Hilt (60311).
- `iceclad` fazzle thumpkin, say map needs `warrior_epic` ==18.
  - Gives Fazzle's Map of East Wastes (60324).
- `nedaria` a blacksmith, say hail needs `warrior_epic` set.
  - Spawns Korezna Orecleaver (182149).
- `shadowhaven` koren galund, hand 60318 needs `warrior_epic` set.
  - Turn in Carved Keg Stamp (60318).
  - Gives Tube of Setting Solution (60319).
- `wallofslaughter` player, on loot needs `warrior_epic` ==10.
  - Sets `warr_epic_wos` to `1`.
  - Spawns a chest (Epic 1.5) (283157).
  - Sets `wiz_wos_chest` to `1`.
  - Sets `paladin_epic_wos` to `1`.
  - Sets `shaman_epic_wos` to `1`.
  - Spawns a chest (Epic 1.5) (893).
  - Sets `druid_epic_wos` to `1`.
  - Sets `rng_wos_chest` to `1`.
  - Sets `ench_wos_chest` to `1`.
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

### Steps on `warrior_pre` that do not change it

- `draniksscar` korbuk brimblade, say work needs `warrior_pre` ==6.
  - Sets `warrior_epic` to `1`.
- `freeporteast` kargek redblade, hand 60287 needs `warrior_pre` set.
  - Turn in Redblade Family Sword (60287).
  - Gives Emblazoned Champion's Hilt (60288).
- `freporte` kargek redblade, hand 60287 needs `warrior_pre` set.
  - Turn in Redblade Family Sword (60287).
  - Gives Emblazoned Champion's Hilt (60288).
- `thurgadina` dardek bladewright, hand 60289 needs `warrior_pre` ==4.
  - Turn in Coldain Coffee Blend (60289).

## `warrior_epic`

See `warrior_epic` earlier in this file.

## Other flags touched along the way

- `warr_epic_bloodfield` set to 1 at bloodfields/player.
- `warr_epic_wos` set to 1 at wallofslaughter/player.
- `warrior_epic_dranik` set to 1 at dranik/player.
- `warrior_epic_gulak` set to 1 at veksar/player.
- `warrior_epic_korezna` set to 1, 2 at nedaria/korezna orecleaver.
- `warrior_epic_veksar` set to 1 at firiona/corfia nultethen.
- `warrior_epic_vxed` set to 1 at draniksscar/korbuk brimblade.
