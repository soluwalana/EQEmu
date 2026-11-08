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
25. Say "Tm Devrak Death" to rujd/"Rujd".
26. Spawns "spawn chest with Heavy Orcish Prison Key" (245241).
27. Loot "Pod of Water" (13044) from "spawn chest with Heavy Orcish Prison Key".
28. 6 alternative loot source(s) also yield Pod of Water (13044).
29. Forage "Pod of Water" (13044) in `ruja`.
30. Forage "Pod of Water" (13044) in `uqua`.
31. Forage "Pod of Water" (13044) in `yxtta`.
32. Combine in Brew Barrel (19): "Bottle of Aged Bloodwine" (51163), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aged Bloodwine" (51164). Requires Brewing, trivial 255.
33. Combine in Brew Barrel (19): "Bottle of Aldo's Bitter Ale" (75805), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aldo's Bitter Ale" (75811). Requires Brewing, trivial 15.
34. 17 other recipes also produce Bottle (16598).
35. Combine in Brew Barrel (19): "Pod of Water" (13044), "Bottle" (16598). Produces "Water Flask" (13006). Requires Brewing, trivial 21.
36. northro/"Verrell Cogswin", hand "Water Flask" (13006). Sets `Green_Scale_Quest` to `1`.
37. northro/"Verrell Cogswin", hand "Red Dragon Scales" (11622). Sets `Green_Scale_Quest` to `2`.
38. northro/"Verrell Cogswin", say "Adhesive". Requires `Green_Scale_Quest` ==2. Requires `Green_Scale_Quest` set. Gives "Verrell's Box of Potions" (67387).
39. Loot "Fractured Centaur Hoof" (67388) from "Centaur Archer" in `southkarana`.
40. Loot "Fractured Centaur Hoof" (67388) from "Centaur Charger" in `southkarana`.
41. Loot "Fractured Centaur Hoof" (67388) from "Centaur Courser" in `southkarana`.
42. Loot "Fractured Centaur Hoof" (67388) from "Centaur Foal" in `southkarana`.
43. Loot "Fractured Centaur Hoof" (67388) from "Centaur Sheltie" in `southkarana`.
44. Loot "Fire Giant Embers" (67389) from "A Fire Giant Warlord" (NPC 278023) in `soldungc`. Drop cache: 28.35% chance per kill.
45. Loot "Jagged Permafrost Shards" (67390) from "The Chilling Terror" in `permafrost`.
46. Combine in Oven (15): "Fractured Centaur Hoof" (67388), "Fire Giant Embers" (67389), "Jagged Permafrost Shards" (67390). Produces "Glue Powder" (67391). Requires Baking. The combine does not fail.
47. Common item: Barley (16590). Listed in 28 zones.
48. Common item: Deep Fungus Mold (67393). Listed in 28 zones.
49. Common item: Distilled Spirits (67394). Listed in 28 zones.
50. Combine in Brew Barrel (19): "Barley" (16590), "Deep Fungus Mold" (67393), "Distilled Spirits" (67394). Produces "Deep Barley Brew" (67392). Requires Brewing, trivial 110.
51. northro/"Verrell Cogswin", say "Adhesive". Requires `Green_Scale_Quest` ==2. Requires `Green_Scale_Quest` set. Gives "Potion Vial" (67395).
52. Combine in "Verrell's Box of Potions" (67387): "Glue Powder" (67391), "Deep Barley Brew" (67392), "Potion Vial" (67395). Produces "Thick Adhesive" (67386). The combine does not fail.
53. northro/"Verrell Cogswin", hand "Thick Adhesive" (67386). Gives "Grey Scale Pieces" (67385).
54. northro/"Verrell Cogswin", hand "Thick Adhesive" (67386). Gives "Thick Adhesive" (67396).
55. Combine in "Verrell's Box of Potions" (67387): "Grey Scale Pieces" (67385), "Thick Adhesive" (67396). Produces "Grey Colored Scales" (67384). The combine does not fail.
56. northro/"Verrell Cogswin", hand "Grey Colored Scales" (67384). Gives "Green Dragon Scales" (11582).
57. eastkarana/"Tenal Redblade", hand "Green Dragon Scales" (11582) + "Red Dragon Scales" (11622) + "Totem of Fiery War" (20681). Gives "Mark of the Sword" (20683).
58. Loot "Hand of the Maestro" (20676) from "Hand of the Maestro" in `hateplane`.
59. Loot "Hand of the Maestro" (20676) from "Hand of the Maestro" in `hateplaneb`.
60. eastkarana/"Tenal Redblade", hand "Hand of the Maestro" (20676) + "Mark of the Sword" (20683). Gives "Tenal's note to Kargek" (20684).
61. Loot "Spiroc Wingblade" (20679) from "The Spiroc Lord" in `airplane`.
62. freeporteast/"Kargek Redblade", hand "Spiroc Wingblade" (20679) + "Tenal's note to Kargek" (20684). Gives "Red Scabbard" (17859).
63. Combine in "Red Scabbard" (17859): "Jagged Blade of War" (10908). Produces "Blade of Tactics" (10909), "Blade of Strategy" (10910). The combine does not fail.
64. Combine in "Red Scabbard" (17859): "Blade of Tactics" (10909), "Blade of Strategy" (10910). Produces "Jagged Blade of War" (10908). The combine does not fail.
65. lakerathe/"Triathalon Swim Goggles", say "Hail". Gives "Rebreather" (16889).
66. Combine in Forge (17): "Smithing Chisel" (7052), "Large Brick of Ore" (10502). Hands back "Smithing Chisel" (7052). Produces "Small Brick of Ore" (10501). Requires Blacksmithing, trivial 27.
67. Combine in Forge (17): "Small Piece of Ore" (10500), "Water Flask" (13006). Produces "Small Brick of Ore" (10501). Requires Blacksmithing, trivial 27.
68. 11 other recipes also produce Small Brick of Ore (10501).
69. Loot "Toolbox Mold" (12077) from "Shevra Kollintar" in `paineel`.
70. kaladimb/"Jeet", say "Collect The Gnome Profit". Gives "Scrubber Key" (12164).
71. akanon/"Clockwork Scrubber", hand "Scrubber Key" (12164). Gives "Gnome Take" (12167).
72. kaladimb/"Jeet", hand "Gnome Take" (12167). Gives "Small Piece of Ore" (10500).
73. Combine in Forge (17): "Small Piece of Ore" (10500), "Water Flask" (13006). Produces "Metal Bits" (16905) x2. Requires Blacksmithing, trivial 18.
74. Combine in Forge (17): "Small Brick of Ore" (10501), "Toolbox Mold" (12077), "Water Flask" (13006), "Metal Bits" (16905). Produces "Toolbox" (17902). Requires Blacksmithing, trivial 51.
75. Common item: Platemail Helm (4001). Listed in 15 zones.
76. Fish "Fresh Fish" (13019) in `zone 0`.
77. Forage "Fresh Fish" (13019) in `kedge`.
78. Common item: Metal Rod (16850). Listed in 14 zones.
79. Common item: Metal Twine (16857). Listed in 10 zones.
80. Common item: Gnomish Bolts (16861). Listed in 10 zones.
81. Common item: Silk Lined Steel Helm (16862). Listed in 9 zones.
82. Common item: Fine Coral Mesh (16890). Listed in 14 zones.
83. Combine in "Toolbox" (17902): "Fresh Fish" (13019), "Metal Rod" (16850), "Metal Twine" (16857), "Gnomish Bolts" (16861), "Silk Lined Steel Helm" (16862), "Fine Coral Mesh" (16890). Produces "Aqualung" (16873) x20. Requires Tinkering, trivial 148.
84. Summon "Black Diamond of Nightmares" (29990) by casting "Imbue Nightmare".
85. potranquility/"Elder Fuirstel", say "Hail". Sets `pop_cod_final` to `1`.
86. poknowledge/"Aid Grimel", say "Versed In The Art Of Smithing". Requires `pop_cod_final` ==1. Requires `pop_cod_final` set. Gives "Filthy Breastplate" (15984).
87. Combine in "Mixing Bowl" (17906): "Celestial Solvent" (9731), "Words of Acquisition (Beza)" (11866). Produces "Celestial Essence" (9650). Requires Baking, trivial 15. The combine does not fail.
88. Combine in "Mixing Bowl" (17906): "Celestial Solvent" (9731), "Words of Burnishing" (11862). Produces "Celestial Essence" (9650). Requires Baking, trivial 15. The combine does not fail.
89. 67 other recipes also produce Celestial Essence (9650).
90. Common item: Jar of Acid (22133). Listed in 15 zones.
91. Combine in Brew Barrel (19): "Celestial Essence" (9650), "Jar of Acid" (22133). Produces "Acid Wash" (15987). Requires Brewing, trivial 151.
92. Combine in Forge (17): "Filthy Breastplate" (15984), "Acid Wash" (15987). Produces "Cleansed Breastplate" (15998). Requires Blacksmithing, trivial 227.
93. Common item: Mortar and Pestle (17904). Listed in 12 zones.
94. Loot "Sandstorm Pearl" (29909) from "Rorek Steelthorn" (NPC 209081) in `bothunder`. Drop cache: 5.33% chance per kill.
95. Combine in "Mortar and Pestle" (17904): "Sandstorm Pearl" (29909). Produces "Powdered Sandstorm Pearl" (29520) x4. Requires Make Poison, trivial 255.
96. Common item: Firing Sheet (16906). Listed in 34 zones.
97. Combine in Pottery Wheel (21): "Water Flask" (13006), "Block of Clay" (16901). Produces "Small Block of Clay" (16900) x3. Requires Pottery, trivial 21.
98. Combine in Pottery Wheel (21): "Small Block of Clay" (16900), "Water Flask" (13006). Produces "Block of Clay" (16901). Requires Pottery, trivial 21.
99. Combine in Pottery Wheel (21): "Water Flask" (13006), "Large Block of Clay" (16902). Produces "Block of Clay" (16901) x2. Requires Pottery, trivial 21.
100. Combine in Pottery Wheel (21): "Block of Clay" (16901), "Water Flask" (13006). Produces "Large Block of Clay" (16902). Requires Pottery, trivial 21.
101. Common item: Large Bowl Sketch (16963). Listed in 29 zones.
102. Combine in Pottery Wheel (21): "Large Block of Clay" (16902), "Water Flask" (13006), "Large Bowl Sketch" (16963). Produces "Unfired Mixing Bowl" (16930). Requires Pottery, trivial 128.
103. Combine in Kiln (22): "Firing Sheet" (16906), "Unfired Mixing Bowl" (16930). Produces "Mixing Bowl" (17906). Requires Pottery, trivial 15.
104. Combine in "Mixing Bowl" (17906): "Sandstorm Pearl" (29909). Produces "Powdered Sandstorm Pearl" (29520) x4. Requires Baking. The combine does not fail.
105. Spawns "a Koka'Vor chieftain" (210236) in `postorms` on event_signal.
106. Loot "Storm Rider Blood" (29526) from "a Koka'Vor chieftain".
107. Loot "Drop of Pure Rain" (29904) from "A vann stav" (NPC 209018) in `bothunder`. Drop cache: 4% chance per kill.
108. Combine in Brew Barrel (19): "Powdered Sandstorm Pearl" (29520), "Storm Rider Blood" (29526), "Drop of Pure Rain" (29904). Produces "Hurricane Temper" (29533). Requires Brewing, trivial 135.
109. Combine in Forge (17): "Cleansed Breastplate" (15998), "Hurricane Temper" (29533). Produces "Tempered Breastplate" (15999). Requires Blacksmithing, trivial 229.
110. Combine in Forge (17): "Black Diamond of Nightmares" (29990), "Tempered Breastplate" (15999). Produces "Imbued Breastplate" (15985). Requires Blacksmithing 220. Trivial at 275.
111. poknowledge/"Aid Grimel", hand "Imbued Breastplate" (15985). Gives "Hardened Leather Signet" (16249).
112. poknowledge/"Aid Grimel", say "Skill In Brewing". Requires `pop_cod_final` ==1. Requires `pop_cod_final` set. Gives "Portable Drink Barrel" (17179).
113. Spawns "Sepsis Rat" (45113) in `qcat` on event_death.
114. Loot "Rat Ears" (13072) from "Sepsis Rat".
115. 2 alternative loot source(s) also yield Rat Ears (13072).
116. Loot "Spider Legs" (13417) from "A Large Yellow Recluse" (NPC 56052) in `steamfont`. Drop cache: 55% chance per kill.
117. Common item: Rice (16593). Listed in 30 zones.
118. Combine in "Portable Drink Barrel" (17179): "Rat Ears" (13072), "Spider Legs" (13417), "Rice" (16593), "Bottle" (16598). Produces "Gnomish Spirits" (13037) x2. Requires Brewing, trivial 102.
119. Combine in Brew Barrel (19): "Rat Ears" (13072), "Spider Legs" (13417), "Rice" (16593), "Bottle" (16598). Produces "Gnomish Spirits" (13037) x2. Requires Brewing, trivial 102.
120. Combine in "Toolbox" (17902): "Water Flask" (13006), "Gnomish Spirits" (13037). Produces "Firewater" (16881). Requires Tinkering, trivial 17.
121. Common item: Metal Fastening (16888). Listed in 14 zones.
122. Common item: Sharkskin Tubing (16891). Listed in 14 zones.
123. Common item: Lime Coated Meshing (16892). Listed in 10 zones.
124. Combine in "Toolbox" (17902): "Platemail Helm" (4001), "Aqualung" (16873), "Firewater" (16881), "Metal Fastening" (16888), "Sharkskin Tubing" (16891), "Lime Coated Meshing" (16892). Produces "Rebreather" (16889). Requires Tinkering, trivial 175.
125. Loot "Block of Permafrost" (20665) from "Lady Vox" in `permafrost`.
126. Loot "Block of Permafrost" (20665) from "An Ice Giant" in `permafrost`.
127. Common item: Keg of Vox Tail Ale (20664). Listed in 13 zones.
128. oceanoftears/"Denken Strongpick", hand "Rebreather" (16889) + "Keg of Vox Tail Ale" (20664) + "Block of Permafrost" (20665). Gives "Ancient Sword Blade" (20667).
129. Loot "Ancient Blade" (20670) from "Queen Velazul Di'zok" in `chardok`.
130. Ground spawn of "Unjeweled Dragon Head Hilt" (20668) in `lakerathe`.
131. Loot "Apothic Crown" (1239) from "Magi P'Tasa" (NPC 186157) in `hateplaneb`. Drop cache: 19.16% chance per kill.
132. poknowledge/"Arch Mage Deidus", hand "Apothic Crown" (1239). Gives "Diamond" (10037).
133. Loot "Scroll of the Ox" (49007) from "A Sturdy Chest" in `stillmoona`.
134. Loot "Scroll of the Boar" (49008) from "A Sturdy Chest" in `stillmoona`.
135. Loot "Scroll of the Dragon" (49009) from "A Sturdy Chest" in `stillmoona`.
136. Loot "Scroll of the Tiger" (49010) from "A Sturdy Chest" in `stillmoona`.
137. Hand "Scroll of the Ox" (49007) + "Scroll of the Boar" (49008) + "Scroll of the Dragon" (49009) + "Scroll of the Tiger" (49010) to stillmoona/"The Keeper Of Strength". Spawns "A Spirit Keeper" (338169). Loot "Black Sapphire" (10036) from "A Spirit Keeper".
138. 43 alternative loot source(s) also yield Black Sapphire (10036).
139. Loot "Bayle List I" (18808) from "Mutt Rootlit" in `highpass`.
140. qrg/"Gerael Woodone", say "Deliver A Flask". Gives "Flask of Nitrates" (13945).
141. akanon/"Kimble Nogflop", hand "Flask of Nitrates" (13945). Gives "Regurgitonic" (12140).
142. qrg/"Mammoth", hand "Regurgitonic" (12140). Gives "Bayle List II" (18809).
143. Loot "Bayle List III" (18810) from "Dyllin Starsine" in `highpass`.
144. Loot "Bayle List III" (18810) from "Dyllin Starsine" in `highpasshold`.
145. southro/"Rathmana Allin", hand "Bayle List I" (18808) + "Bayle List II" (18809) + "Bayle List III" (18810). Gives "Translated Parchment" (18961).
146. highpass/"Stanos Herkanor", hand "Translated Parchment" (18961). Gives "Sealed Box" (28057).
147. Kill wakening/"A Tar Goo". Spawns "A Tar Goo" (119122).
148. Loot "Oily Goo Secretion" (11637) from "A Tar Goo".
149. 1 alternative loot source(s) also yield Oily Goo Secretion (11637).
150. bazaar/"Caerlyna", hand "Vale Sewing Kit" (92882). Gives "Vale Sewing Kit Token" (56884).
151. bazaar/"Caerlyna", hand "Vale Sewing Kit Token" (56884). Gives "Vale Sewing Kit" (92882).
152. Common item: Needle Mold (12019). Listed in 32 zones.
153. Common item: Thimble Mold (12057). Listed in 32 zones.
154. Combine in Forge (17): "Fine Steel Two Handed Sword" (5351), "Water Flask" (13006). Produces "Small Brick of High Quality Ore" (10468) x2, "Small Piece of High Quality Ore" (22229). Requires Blacksmithing, trivial 21.
155. Combine in Forge (17): "Smithing Chisel" (7052), "Small Brick of High Quality Ore" (10468). Hands back "Smithing Chisel" (7052). Produces "Small Piece of High Quality Ore" (22229) x2. Requires Blacksmithing, trivial 27.
156. 4 other recipes also produce Small Piece of High Quality Ore (22229).
157. Combine in Royal Qeynos Forge (40): "Small Piece of High Quality Ore" (22229), "Water Flask" (13006). Produces "High Quality Metal Bits" (22230). Requires Blacksmithing, trivial 20.
158. Combine in Vale Forge (49): "Needle Mold" (12019), "Thimble Mold" (12057), "Water Flask" (13006), "High Quality Metal Bits" (22230). Produces "Vale Sewing Kit" (92882). Requires Blacksmithing, trivial 162.
159. Loot "Crystalline Silk" (25306) from "A Crystal Grinder" (NPC 121089) in `crystal`. Drop cache: 100% chance per kill.
160. Combine in "Vale Sewing Kit" (92882): "Crystalline Silk" (25306). Produces "Crystalline Silk Mesh" (11636). Requires Tailoring, trivial 68.
161. skyshrine/"Iago Sabuela", hand "Crystalline Silk Mesh" (11636) + "Oily Goo Secretion" (11637). Gives "Empty Artifact Container" (17167).
162. Loot "Crystal Dragon Eye" (11638) from "An Ice Paw Sorcerer" in `velketor`.
163. Loot "Golden Dragon Claw" (11639) from "A Chetari Runemage" in `necropolis`.
164. Loot "Platinum Dragon Scale" (11640) from "A Siren Sorceress" in `sirens`.
165. Loot "Rodrick's Head" (1045) from "Rodrick Tardok".
166. Loot "Rodrick's Head" (1045) from "Rodrick Tardok" in `eastwastes`.
167. Spawns "Poxbreath Yellowfang" (116566) in `eastwastes` on event_signal.
168. Loot "Note from Kromrif" (18084) from "Poxbreath Yellowfang".
169. Spawns "Scarbrow Ga'Hruk" (116568) in `eastwastes` on event_signal.
170. Loot "Head of Scarbrow" (30141) from "Scarbrow Ga'Hruk".
171. Say "Help" to eastwastes/"Tain Hammerfrost".
172. Spawns "Ghrek Squatnot" (116560).
173. Loot "Frozen Elixir" (30138) from "Ghrek Squatnot".
174. eastwastes/"Tain Hammerfrost", hand "Frozen Elixir" (30138). Gives "Coldain Smithing Hammer" (30140).
175. Spawns "Rabid Tundra Kodiak" (116545) in `eastwastes` on event_waypoint_arrive.
176. Loot "Rabid Kodiak Skin" (30266) from "Rabid Tundra Kodiak".
177. eastwastes/"Boridain Glacierbane", hand "Rabid Kodiak Skin" (30266). Gives "Broken Axe" (30267).
178. iceclad/"A Lost Pirate", say "I Will Find The Parts". Gives "Map Binding" (17053).
179. Loot "First part of an Iceclad Map" (30043) from "Dire Wolf Stalker" in `iceclad`.
180. Loot "Second part of an Iceclad Map" (30044) from "Stormfeather" in `iceclad`.
181. Loot "Second part of an Iceclad Map" (30044) from "The Fabled Stormfeather".
182. greatdivide/"Bloody Gnome Captive", say "Map". Gives "Third part of an Iceclad Map" (30045).
183. Loot "Fourth part of an Iceclad Map" (30073) from "Lodizal" in `iceclad`.
184. Loot "Fourth part of an Iceclad Map" (30073) from "The Fabled Lodizal".
185. Combine in "Map Binding" (17053): "First part of an Iceclad Map" (30043), "Second part of an Iceclad Map" (30044), "Third part of an Iceclad Map" (30045), "Fourth part of an Iceclad Map" (30073). Produces "Pieces of the Iceclad Map" (30046). The combine does not fail.
186. Hand "Pieces of the Iceclad Map" (30046) to iceclad/"A Lost Pirate". Spawns "Rabid Snow Cougar Does Not Exist Using Regular For Now" (116008). Loot "High Quality Cougarskin" (30030) from "Rabid Snow Cougar Does Not Exist Using Regular For Now".
187. Loot "High Quality Tundra Kodiak Pelt" (30077) from "A Tundra Kodiak" (NPC 116044) in `eastwastes`. Drop cache: 3.91% chance per kill.
188. Combine in "Vale Sewing Kit" (92882): "High Quality Cougarskin" (30030), "High Quality Tundra Kodiak Pelt" (30077). Produces "Coldain Hunting Blanket" (30135). Requires Tailoring, trivial 41.
189. eastwastes/"Garadain Glacierbane", hand "Coldain Hunting Blanket" (30135). Gives "Copper Coldain Insignia Ring" (30131).
190. eastwastes/"Garadain Glacierbane", hand "Copper Coldain Insignia Ring" (30131) + "Broken Axe" (30267). Gives "Silver Coldain Insignia Ring" (30133).
191. Ground spawn of "Skinning Rock" (30062) in `eastwastes`.
192. Loot "Wooly Rhino Horn" (30088) from "A Wooly Rhino" (NPC 116033) in `eastwastes`. Drop cache: 20% chance per kill.
193. Loot "High Quality Walrus Hide" (30096) from "A Walrus" (NPC 116065) in `eastwastes`. Drop cache: 14.1% chance per kill.
194. Combine in Forge (17): "Skinning Rock" (30062), "Wooly Rhino Horn" (30088), "High Quality Walrus Hide" (30096). Produces "Coldain Hunting Knife" (30137). Requires Blacksmithing, trivial 41.
195. eastwastes/"Garadain Glacierbane", hand "Silver Coldain Insignia Ring" (30133) + "Coldain Hunting Knife" (30137). Gives "Gold Coldain Insignia Ring" (30132).
196. eastwastes/"Garadain Glacierbane", hand "Gold Coldain Insignia Ring" (30132) + "Coldain Smithing Hammer" (30140). Gives "Platinum Coldain Insignia Ring" (30134).
197. eastwastes/"Garadain Glacierbane", hand "Platinum Coldain Insignia Ring" (30134) + "Head of Scarbrow" (30141). Gives "Obsidian Coldain Insignia Ring" (30268).
198. eastwastes/"Garadain Glacierbane", hand "Rodrick's Head" (1045) + "Note from Kromrif" (18084) + "Obsidian Coldain Insignia Ring" (30268). Gives "Mithril Coldain Insignia Ring" (30162).
199. eastwastes/"Dobbin Crossaxe", hand "Mithril Coldain Insignia Ring" (30162). Gives "Note from Corbin" (1047).
200. eastwastes/"Garadain Glacierbane", hand "Note from Corbin" (1047). Gives "Adamantium Coldain Insignia Ring" (30163).
201. eastwastes/"Garadain Glacierbane", hand "Adamantium Coldain Insignia Ring" (30163). Gives "Marching Orders" (1093).
202. Hand "Marching Orders" (1093) to eastwastes/"Gloradin Coldheart". Spawns "Oracle of Ry'Gorr" (116006). Loot "Dragon Scripture Tablet" (11651) from "Oracle of Ry'Gorr".
203. 1 alternative loot source(s) also yield Dragon Scripture Tablet (11651).
204. Combine in "Empty Artifact Container" (17167): "Crystal Dragon Eye" (11638), "Golden Dragon Claw" (11639), "Platinum Dragon Scale" (11640), "Dragon Scripture Tablet" (11651). Produces "Sealed Box" (28057). The combine does not fail.
205. Hand "Sealed Box" (28057) to kithicor/"Adjutant D-Kan". Spawns "General V'ghera" (20205). Loot "General's Pouch" (28013) from "General V'ghera".
206. 6 alternative loot source(s) also yield General's Pouch (28013).
207. Loot "Fleshripper" (5411) from "Solusek kobold king" in `soldungb`.
208. Loot "Painbringer" (5410) from "Kobold Champion" in `soldungb`.
209. Loot "Mithril Two-Handed Sword" (5401) from "The Froglok King" in `gukbottom`.
210. Loot "Gigantic Zweihander" (5308) from "Karg IceBear" in `everfrost`.
211. qey2hh1/"Vilnius The Small", hand "Gigantic Zweihander" (5308) + "Mithril Two-Handed Sword" (5401) + "Painbringer" (5410) + "Fleshripper" (5411). Gives "Jagged Diamond Dagger" (7506).
212. Loot "Robe of the Ishva" (1357) from "Coercer Q'ioul" in `kithicor`.
213. Loot "Robe of the Ishva" (1357) from "Jinalis Andir" in `cauldron`.
214. Loot "Robe of the Ishva" (1357) from "The Ishva Mal" in `southkarana`.
215. Loot "Robe of the Kedge" (1253) from "Kubaria" (NPC 309002) in `chambersf`. Drop cache: 100% chance per kill.
216. Loot "Robe of the Oracle" (1354) from "Oracle of K'Arnon" in `oceanoftears`.
217. Loot "Robe of the Oracle" (1354) from "Oracle of K'Arnon" in `oot`.
218. Loot "Shining Metallic Robes" (1360) from "Yendar Starpyre" (NPC 56012) in `steamfont`. Drop cache: 100% chance per kill.
219. qey2hh1/"Vilnius The Small", hand "Robe of the Kedge" (1253) + "Robe of the Oracle" (1354) + "Robe of the Ishva" (1357) + "Shining Metallic Robes" (1360). Gives "Cazic Quill" (7505).
220. highpass/"Stanos Herkanor", hand "Cazic Quill" (7505) + "Jagged Diamond Dagger" (7506) + "General's Pouch" (28013). Gives "Ragebringer" (11057).
221. highpass/"Stanos Herkanor", say "Hail". Sets `Fatestealer` to `1`.
222. Unresolved cyclic prerequisite: `Fatestealer_gal` ==1.
223. Unresolved cyclic prerequisite: `Fatestealer_gal` ==1.
224. Unresolved cyclic prerequisite: `Fatestealer_mar` ==1.
225. Unresolved cyclic prerequisite: `Fatestealer_gal` ==1.
226. Unresolved cyclic prerequisite: `Fatestealer_mar` ==1.
227. Unresolved cyclic prerequisite: `Fatestealer_lyt` ==1.
228. Loot "Signed Agreement" (10246) from "Lythe Songbird" in `freeporteast`.
229. Loot "Signed Agreement" (10246) from "Lythe Songbird" in `freportw`.
230. overthere/"Inem R'Ker", hand "Signed Agreement" (10246). Sets `Fatestealer_lyt` to `1`.
231. Loot "Signed Agreement" (10239) from "Seana Marsinger" in `gfaydark`.
232. Loot "Signed Agreement" (52416) from "Stefan Marsinger" in `gfaydark`.
233. overthere/"Inem R'Ker", hand "Signed Agreement" (10239) + "Signed Agreement" (52416). Sets `Fatestealer_mar` to `1`.
234. Loot "Signed Agreement" (10243) from "Galdorin Visigothe" in `abysmal`.
235. overthere/"Inem R'Ker", hand "Signed Agreement" (10243). Sets `Fatestealer_gal` to `1`.
236. overthere/"Inem R'Ker", hand "Signed Agreement" (10243). Sets `Fatestealer_bard` to `1`.
237. Spawns "a Teir'Dal guardian" (186190) in `hateplaneb` on event death_complete:186114.
238. Loot "Stack of Pages" (52335) from "a Teir'Dal guardian".
239. 5 alternative loot source(s) also yield Stack of Pages (52335).
240. steamfont/"Yendar Starpyre", hand "Stack of Pages" (52335). Sets `Fatestealer_page` to `1`.
241. Spawns "A Furious Magma Guardian" (278123) in `soldungc` on event_signal.
242. Loot "Crystallized Shard of Doomfire" (21339) from "A Furious Magma Guardian".
243. 1 alternative loot source(s) also yield Crystallized Shard of Doomfire (21339).
244. Loot "Foul Doomfire Brimstone" (21342) from "A Pool Of Living Lava" (NPC 278043) in `soldungc`. Drop cache: 15.97% chance per kill.
245. Loot "Igneous Rock of Doomfire" (21340) from "Typhoeus" (NPC 278069) in `soldungc`. Drop cache: 35% chance per kill.
246. Loot "Pile of Doomfire Ash" (21341) from "a Taklasinai marauder" (NPC 278075) in `soldungc`. Drop cache: 35% chance per kill.
247. Hand "Crystallized Shard of Doomfire" (21339) + "Igneous Rock of Doomfire" (21340) + "Pile of Doomfire Ash" (21341) + "Foul Doomfire Brimstone" (21342) to soldungc/"The Firewatcher". Spawns "Culthor the Gatekeeper" (278005). Loot "Smoldering Embers of Solusek" (52346) from "Culthor the Gatekeeper".
248. nedaria/"Smith Dandi", hand "Smoldering Embers of Solusek" (52346). Sets `Fatestealer_forge` to `1`.
249. Spawns "a Teir'Dal guardian" (186190) in `hateplaneb` on event death_complete:186114.
250. Loot "Soulstone of Lanys" (52337) from "a Teir'Dal guardian".
251. 5 alternative loot source(s) also yield Soulstone of Lanys (52337).
252. nedaria/"Lirprin, Head Of Affairs", hand "Soulstone of Lanys" (52337). Requires `Fatestealer_bard` ==1. Requires `Fatestealer_page` ==1. Requires `Fatestealer_forge` ==1. Gives "Fatestealer" (52347).
253. nedaria/"Lirprin, Head Of Affairs", say "Hail". Sets `Fatestealer` to `3`.
254. Loot "Polished Bone Horn" (52349) from "A Baleful Stoneworker" (NPC 301023) in `bloodfields`. Drop cache: 4% chance per kill.
255. Loot "Brass Mouthpiece" (52350) from "An Ukun Fleshhound" (NPC 301009) in `bloodfields`. Drop cache: 3.67% chance per kill.
256. Loot "Bucket Mute" (52351) from "An Ukun Fleshhound" (NPC 301009) in `bloodfields`. Drop cache: 3.67% chance per kill.
257. Loot "Thin Leather Straps" (52352) from "An Ukun Fleshhound" (NPC 301009) in `bloodfields`. Drop cache: 3.67% chance per kill.
258. Hand "Polished Bone Horn" (52349) + "Brass Mouthpiece" (52350) + "Bucket Mute" (52351) + "Thin Leather Straps" (52352) to bloodfields/"Caller Donivin". Spawns "A Reclusive Girplan" (301033). Loot "Jacinth" (10053) from "A Reclusive Girplan".
259. 55 alternative loot source(s) also yield Jacinth (10053).
260. freeporteast/"Wenden Blackhammer", hand "Black Sapphire" (10036) + "Diamond" (10037) + "Jacinth" (10053) + "Unjeweled Dragon Head Hilt" (20668). Gives "Jeweled Dragon Head Hilt" (20671).
261. Ground spawn of "Severely Damaged Dragon Head Hilt" (20669) in `timorous`.
262. Loot "Giant Sized Monocle" (20678) from "A Mountain Giant Patriarch" in `dreadlands`.
263. frontiermtns/"Mentrax Mountainbone", hand "Giant Sized Monocle" (20678). Gives "Rejesiam Ore" (20666).
264. Loot "Ball of Everliving Golem" (20677) from "Dread" in `fearplane`.
265. Loot "Ball of Everliving Golem" (20677) from "Fright" in `fearplane`.
266. Loot "Ball of Everliving Golem" (20677) from "Terror" in `fearplane`.
267. freeporteast/"Wenden Blackhammer", hand "Rejesiam Ore" (20666) + "Severely Damaged Dragon Head Hilt" (20669) + "Ball of Everliving Golem" (20677). Gives "Finely Crafted Dragon Head Hilt" (20672).
268. Combine in "Red Scabbard" (17859): "Ancient Sword Blade" (20667), "Ancient Blade" (20670), "Jeweled Dragon Head Hilt" (20671), "Finely Crafted Dragon Head Hilt" (20672). Produces "Jagged Blade of War" (10908). The combine does not fail.
269. freeporteast/"Gartrog Smitehammer", hand "Jagged Blade of War" (10908) + "Red Scabbard" (17859). Gives "Red Scabbard" (17869).
270. freeporteast/"Gartrog Smitehammer", hand "Jagged Blade of War" (10908) + "Red Scabbard" (17859). Gives "Jagged Blade of War" (66175).
271. Combine in "Red Scabbard" (17869): "Jagged Blade of War" (66175). Produces "Blade of Tactics" (66176), "Blade of Strategy" (66177). Requires Pottery. The combine does not fail.
272. Combine in "Red Scabbard" (17869): "Blade of Tactics" (66176), "Blade of Strategy" (66177). Produces "Jagged Blade of War" (66175). Requires Pottery. The combine does not fail.
273. draniksscar/"Korbuk Brimblade", say "Work". Sets `warrior_pre` to `1`.
274. draniksscar/"Korbuk Brimblade", hand "Korbuk's Weapon Plans" (60285). Sets `warrior_pre` to `2`.
275. draniksscar/"Korbuk Brimblade", hand "Elegant Shank" (60286). Sets `warrior_pre` to `3`.
276. Loot "Redblade Family Sword" (60287) from "Drevlon Knacknabber" in `eastkarana`.
277. freeporteast/"Kargek Redblade", hand "Redblade Family Sword" (60287). Requires `warrior_pre` set. Requires `warrior_pre` ==3. Gives "Emblazoned Champion's Hilt" (60288).

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
25. Say "Tm Devrak Death" to rujd/"Rujd".
26. Spawns "spawn chest with Heavy Orcish Prison Key" (245241).
27. Loot "Pod of Water" (13044) from "spawn chest with Heavy Orcish Prison Key".
28. 6 alternative loot source(s) also yield Pod of Water (13044).
29. Forage "Pod of Water" (13044) in `ruja`.
30. Forage "Pod of Water" (13044) in `uqua`.
31. Forage "Pod of Water" (13044) in `yxtta`.
32. Combine in Brew Barrel (19): "Bottle of Aged Bloodwine" (51163), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aged Bloodwine" (51164). Requires Brewing, trivial 255.
33. Combine in Brew Barrel (19): "Bottle of Aldo's Bitter Ale" (75805), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aldo's Bitter Ale" (75811). Requires Brewing, trivial 15.
34. 17 other recipes also produce Bottle (16598).
35. Combine in Brew Barrel (19): "Pod of Water" (13044), "Bottle" (16598). Produces "Water Flask" (13006). Requires Brewing, trivial 21.
36. northro/"Verrell Cogswin", hand "Water Flask" (13006). Sets `Green_Scale_Quest` to `1`.
37. northro/"Verrell Cogswin", hand "Red Dragon Scales" (11622). Sets `Green_Scale_Quest` to `2`.
38. northro/"Verrell Cogswin", say "Adhesive". Requires `Green_Scale_Quest` ==2. Requires `Green_Scale_Quest` set. Gives "Verrell's Box of Potions" (67387).
39. Loot "Fractured Centaur Hoof" (67388) from "Centaur Archer" in `southkarana`.
40. Loot "Fractured Centaur Hoof" (67388) from "Centaur Charger" in `southkarana`.
41. Loot "Fractured Centaur Hoof" (67388) from "Centaur Courser" in `southkarana`.
42. Loot "Fractured Centaur Hoof" (67388) from "Centaur Foal" in `southkarana`.
43. Loot "Fractured Centaur Hoof" (67388) from "Centaur Sheltie" in `southkarana`.
44. Loot "Fire Giant Embers" (67389) from "A Fire Giant Warlord" (NPC 278023) in `soldungc`. Drop cache: 28.35% chance per kill.
45. Loot "Jagged Permafrost Shards" (67390) from "The Chilling Terror" in `permafrost`.
46. Combine in Oven (15): "Fractured Centaur Hoof" (67388), "Fire Giant Embers" (67389), "Jagged Permafrost Shards" (67390). Produces "Glue Powder" (67391). Requires Baking. The combine does not fail.
47. Common item: Barley (16590). Listed in 28 zones.
48. Common item: Deep Fungus Mold (67393). Listed in 28 zones.
49. Common item: Distilled Spirits (67394). Listed in 28 zones.
50. Combine in Brew Barrel (19): "Barley" (16590), "Deep Fungus Mold" (67393), "Distilled Spirits" (67394). Produces "Deep Barley Brew" (67392). Requires Brewing, trivial 110.
51. northro/"Verrell Cogswin", say "Adhesive". Requires `Green_Scale_Quest` ==2. Requires `Green_Scale_Quest` set. Gives "Potion Vial" (67395).
52. Combine in "Verrell's Box of Potions" (67387): "Glue Powder" (67391), "Deep Barley Brew" (67392), "Potion Vial" (67395). Produces "Thick Adhesive" (67386). The combine does not fail.
53. northro/"Verrell Cogswin", hand "Thick Adhesive" (67386). Gives "Grey Scale Pieces" (67385).
54. northro/"Verrell Cogswin", hand "Thick Adhesive" (67386). Gives "Thick Adhesive" (67396).
55. Combine in "Verrell's Box of Potions" (67387): "Grey Scale Pieces" (67385), "Thick Adhesive" (67396). Produces "Grey Colored Scales" (67384). The combine does not fail.
56. northro/"Verrell Cogswin", hand "Grey Colored Scales" (67384). Gives "Green Dragon Scales" (11582).
57. eastkarana/"Tenal Redblade", hand "Green Dragon Scales" (11582) + "Red Dragon Scales" (11622) + "Totem of Fiery War" (20681). Gives "Mark of the Sword" (20683).
58. Loot "Hand of the Maestro" (20676) from "Hand of the Maestro" in `hateplane`.
59. Loot "Hand of the Maestro" (20676) from "Hand of the Maestro" in `hateplaneb`.
60. eastkarana/"Tenal Redblade", hand "Hand of the Maestro" (20676) + "Mark of the Sword" (20683). Gives "Tenal's note to Kargek" (20684).
61. Loot "Spiroc Wingblade" (20679) from "The Spiroc Lord" in `airplane`.
62. freeporteast/"Kargek Redblade", hand "Spiroc Wingblade" (20679) + "Tenal's note to Kargek" (20684). Gives "Red Scabbard" (17859).
63. Combine in "Red Scabbard" (17859): "Jagged Blade of War" (10908). Produces "Blade of Tactics" (10909), "Blade of Strategy" (10910). The combine does not fail.
64. Combine in "Red Scabbard" (17859): "Blade of Tactics" (10909), "Blade of Strategy" (10910). Produces "Jagged Blade of War" (10908). The combine does not fail.
65. lakerathe/"Triathalon Swim Goggles", say "Hail". Gives "Rebreather" (16889).
66. Combine in Forge (17): "Smithing Chisel" (7052), "Large Brick of Ore" (10502). Hands back "Smithing Chisel" (7052). Produces "Small Brick of Ore" (10501). Requires Blacksmithing, trivial 27.
67. Combine in Forge (17): "Small Piece of Ore" (10500), "Water Flask" (13006). Produces "Small Brick of Ore" (10501). Requires Blacksmithing, trivial 27.
68. 11 other recipes also produce Small Brick of Ore (10501).
69. Loot "Toolbox Mold" (12077) from "Shevra Kollintar" in `paineel`.
70. kaladimb/"Jeet", say "Collect The Gnome Profit". Gives "Scrubber Key" (12164).
71. akanon/"Clockwork Scrubber", hand "Scrubber Key" (12164). Gives "Gnome Take" (12167).
72. kaladimb/"Jeet", hand "Gnome Take" (12167). Gives "Small Piece of Ore" (10500).
73. Combine in Forge (17): "Small Piece of Ore" (10500), "Water Flask" (13006). Produces "Metal Bits" (16905) x2. Requires Blacksmithing, trivial 18.
74. Combine in Forge (17): "Small Brick of Ore" (10501), "Toolbox Mold" (12077), "Water Flask" (13006), "Metal Bits" (16905). Produces "Toolbox" (17902). Requires Blacksmithing, trivial 51.
75. Common item: Platemail Helm (4001). Listed in 15 zones.
76. Fish "Fresh Fish" (13019) in `zone 0`.
77. Forage "Fresh Fish" (13019) in `kedge`.
78. Common item: Metal Rod (16850). Listed in 14 zones.
79. Common item: Metal Twine (16857). Listed in 10 zones.
80. Common item: Gnomish Bolts (16861). Listed in 10 zones.
81. Common item: Silk Lined Steel Helm (16862). Listed in 9 zones.
82. Common item: Fine Coral Mesh (16890). Listed in 14 zones.
83. Combine in "Toolbox" (17902): "Fresh Fish" (13019), "Metal Rod" (16850), "Metal Twine" (16857), "Gnomish Bolts" (16861), "Silk Lined Steel Helm" (16862), "Fine Coral Mesh" (16890). Produces "Aqualung" (16873) x20. Requires Tinkering, trivial 148.
84. Summon "Black Diamond of Nightmares" (29990) by casting "Imbue Nightmare".
85. potranquility/"Elder Fuirstel", say "Hail". Sets `pop_cod_final` to `1`.
86. poknowledge/"Aid Grimel", say "Versed In The Art Of Smithing". Requires `pop_cod_final` ==1. Requires `pop_cod_final` set. Gives "Filthy Breastplate" (15984).
87. Combine in "Mixing Bowl" (17906): "Celestial Solvent" (9731), "Words of Acquisition (Beza)" (11866). Produces "Celestial Essence" (9650). Requires Baking, trivial 15. The combine does not fail.
88. Combine in "Mixing Bowl" (17906): "Celestial Solvent" (9731), "Words of Burnishing" (11862). Produces "Celestial Essence" (9650). Requires Baking, trivial 15. The combine does not fail.
89. 67 other recipes also produce Celestial Essence (9650).
90. Common item: Jar of Acid (22133). Listed in 15 zones.
91. Combine in Brew Barrel (19): "Celestial Essence" (9650), "Jar of Acid" (22133). Produces "Acid Wash" (15987). Requires Brewing, trivial 151.
92. Combine in Forge (17): "Filthy Breastplate" (15984), "Acid Wash" (15987). Produces "Cleansed Breastplate" (15998). Requires Blacksmithing, trivial 227.
93. Common item: Mortar and Pestle (17904). Listed in 12 zones.
94. Loot "Sandstorm Pearl" (29909) from "Rorek Steelthorn" (NPC 209081) in `bothunder`. Drop cache: 5.33% chance per kill.
95. Combine in "Mortar and Pestle" (17904): "Sandstorm Pearl" (29909). Produces "Powdered Sandstorm Pearl" (29520) x4. Requires Make Poison, trivial 255.
96. Common item: Firing Sheet (16906). Listed in 34 zones.
97. Combine in Pottery Wheel (21): "Water Flask" (13006), "Block of Clay" (16901). Produces "Small Block of Clay" (16900) x3. Requires Pottery, trivial 21.
98. Combine in Pottery Wheel (21): "Small Block of Clay" (16900), "Water Flask" (13006). Produces "Block of Clay" (16901). Requires Pottery, trivial 21.
99. Combine in Pottery Wheel (21): "Water Flask" (13006), "Large Block of Clay" (16902). Produces "Block of Clay" (16901) x2. Requires Pottery, trivial 21.
100. Combine in Pottery Wheel (21): "Block of Clay" (16901), "Water Flask" (13006). Produces "Large Block of Clay" (16902). Requires Pottery, trivial 21.
101. Common item: Large Bowl Sketch (16963). Listed in 29 zones.
102. Combine in Pottery Wheel (21): "Large Block of Clay" (16902), "Water Flask" (13006), "Large Bowl Sketch" (16963). Produces "Unfired Mixing Bowl" (16930). Requires Pottery, trivial 128.
103. Combine in Kiln (22): "Firing Sheet" (16906), "Unfired Mixing Bowl" (16930). Produces "Mixing Bowl" (17906). Requires Pottery, trivial 15.
104. Combine in "Mixing Bowl" (17906): "Sandstorm Pearl" (29909). Produces "Powdered Sandstorm Pearl" (29520) x4. Requires Baking. The combine does not fail.
105. Spawns "a Koka'Vor chieftain" (210236) in `postorms` on event_signal.
106. Loot "Storm Rider Blood" (29526) from "a Koka'Vor chieftain".
107. Loot "Drop of Pure Rain" (29904) from "A vann stav" (NPC 209018) in `bothunder`. Drop cache: 4% chance per kill.
108. Combine in Brew Barrel (19): "Powdered Sandstorm Pearl" (29520), "Storm Rider Blood" (29526), "Drop of Pure Rain" (29904). Produces "Hurricane Temper" (29533). Requires Brewing, trivial 135.
109. Combine in Forge (17): "Cleansed Breastplate" (15998), "Hurricane Temper" (29533). Produces "Tempered Breastplate" (15999). Requires Blacksmithing, trivial 229.
110. Combine in Forge (17): "Black Diamond of Nightmares" (29990), "Tempered Breastplate" (15999). Produces "Imbued Breastplate" (15985). Requires Blacksmithing 220. Trivial at 275.
111. poknowledge/"Aid Grimel", hand "Imbued Breastplate" (15985). Gives "Hardened Leather Signet" (16249).
112. poknowledge/"Aid Grimel", say "Skill In Brewing". Requires `pop_cod_final` ==1. Requires `pop_cod_final` set. Gives "Portable Drink Barrel" (17179).
113. Spawns "Sepsis Rat" (45113) in `qcat` on event_death.
114. Loot "Rat Ears" (13072) from "Sepsis Rat".
115. 2 alternative loot source(s) also yield Rat Ears (13072).
116. Loot "Spider Legs" (13417) from "A Large Yellow Recluse" (NPC 56052) in `steamfont`. Drop cache: 55% chance per kill.
117. Common item: Rice (16593). Listed in 30 zones.
118. Combine in "Portable Drink Barrel" (17179): "Rat Ears" (13072), "Spider Legs" (13417), "Rice" (16593), "Bottle" (16598). Produces "Gnomish Spirits" (13037) x2. Requires Brewing, trivial 102.
119. Combine in Brew Barrel (19): "Rat Ears" (13072), "Spider Legs" (13417), "Rice" (16593), "Bottle" (16598). Produces "Gnomish Spirits" (13037) x2. Requires Brewing, trivial 102.
120. Combine in "Toolbox" (17902): "Water Flask" (13006), "Gnomish Spirits" (13037). Produces "Firewater" (16881). Requires Tinkering, trivial 17.
121. Common item: Metal Fastening (16888). Listed in 14 zones.
122. Common item: Sharkskin Tubing (16891). Listed in 14 zones.
123. Common item: Lime Coated Meshing (16892). Listed in 10 zones.
124. Combine in "Toolbox" (17902): "Platemail Helm" (4001), "Aqualung" (16873), "Firewater" (16881), "Metal Fastening" (16888), "Sharkskin Tubing" (16891), "Lime Coated Meshing" (16892). Produces "Rebreather" (16889). Requires Tinkering, trivial 175.
125. Loot "Block of Permafrost" (20665) from "Lady Vox" in `permafrost`.
126. Loot "Block of Permafrost" (20665) from "An Ice Giant" in `permafrost`.
127. Common item: Keg of Vox Tail Ale (20664). Listed in 13 zones.
128. oceanoftears/"Denken Strongpick", hand "Rebreather" (16889) + "Keg of Vox Tail Ale" (20664) + "Block of Permafrost" (20665). Gives "Ancient Sword Blade" (20667).
129. Loot "Ancient Blade" (20670) from "Queen Velazul Di'zok" in `chardok`.
130. Ground spawn of "Unjeweled Dragon Head Hilt" (20668) in `lakerathe`.
131. Loot "Apothic Crown" (1239) from "Magi P'Tasa" (NPC 186157) in `hateplaneb`. Drop cache: 19.16% chance per kill.
132. poknowledge/"Arch Mage Deidus", hand "Apothic Crown" (1239). Gives "Diamond" (10037).
133. Loot "Scroll of the Ox" (49007) from "A Sturdy Chest" in `stillmoona`.
134. Loot "Scroll of the Boar" (49008) from "A Sturdy Chest" in `stillmoona`.
135. Loot "Scroll of the Dragon" (49009) from "A Sturdy Chest" in `stillmoona`.
136. Loot "Scroll of the Tiger" (49010) from "A Sturdy Chest" in `stillmoona`.
137. Hand "Scroll of the Ox" (49007) + "Scroll of the Boar" (49008) + "Scroll of the Dragon" (49009) + "Scroll of the Tiger" (49010) to stillmoona/"The Keeper Of Strength". Spawns "A Spirit Keeper" (338169). Loot "Black Sapphire" (10036) from "A Spirit Keeper".
138. 43 alternative loot source(s) also yield Black Sapphire (10036).
139. Loot "Bayle List I" (18808) from "Mutt Rootlit" in `highpass`.
140. qrg/"Gerael Woodone", say "Deliver A Flask". Gives "Flask of Nitrates" (13945).
141. akanon/"Kimble Nogflop", hand "Flask of Nitrates" (13945). Gives "Regurgitonic" (12140).
142. qrg/"Mammoth", hand "Regurgitonic" (12140). Gives "Bayle List II" (18809).
143. Loot "Bayle List III" (18810) from "Dyllin Starsine" in `highpass`.
144. Loot "Bayle List III" (18810) from "Dyllin Starsine" in `highpasshold`.
145. southro/"Rathmana Allin", hand "Bayle List I" (18808) + "Bayle List II" (18809) + "Bayle List III" (18810). Gives "Translated Parchment" (18961).
146. highpass/"Stanos Herkanor", hand "Translated Parchment" (18961). Gives "Sealed Box" (28057).
147. Kill wakening/"A Tar Goo". Spawns "A Tar Goo" (119122).
148. Loot "Oily Goo Secretion" (11637) from "A Tar Goo".
149. 1 alternative loot source(s) also yield Oily Goo Secretion (11637).
150. bazaar/"Caerlyna", hand "Vale Sewing Kit" (92882). Gives "Vale Sewing Kit Token" (56884).
151. bazaar/"Caerlyna", hand "Vale Sewing Kit Token" (56884). Gives "Vale Sewing Kit" (92882).
152. Common item: Needle Mold (12019). Listed in 32 zones.
153. Common item: Thimble Mold (12057). Listed in 32 zones.
154. Combine in Forge (17): "Fine Steel Two Handed Sword" (5351), "Water Flask" (13006). Produces "Small Brick of High Quality Ore" (10468) x2, "Small Piece of High Quality Ore" (22229). Requires Blacksmithing, trivial 21.
155. Combine in Forge (17): "Smithing Chisel" (7052), "Small Brick of High Quality Ore" (10468). Hands back "Smithing Chisel" (7052). Produces "Small Piece of High Quality Ore" (22229) x2. Requires Blacksmithing, trivial 27.
156. 4 other recipes also produce Small Piece of High Quality Ore (22229).
157. Combine in Royal Qeynos Forge (40): "Small Piece of High Quality Ore" (22229), "Water Flask" (13006). Produces "High Quality Metal Bits" (22230). Requires Blacksmithing, trivial 20.
158. Combine in Vale Forge (49): "Needle Mold" (12019), "Thimble Mold" (12057), "Water Flask" (13006), "High Quality Metal Bits" (22230). Produces "Vale Sewing Kit" (92882). Requires Blacksmithing, trivial 162.
159. Loot "Crystalline Silk" (25306) from "A Crystal Grinder" (NPC 121089) in `crystal`. Drop cache: 100% chance per kill.
160. Combine in "Vale Sewing Kit" (92882): "Crystalline Silk" (25306). Produces "Crystalline Silk Mesh" (11636). Requires Tailoring, trivial 68.
161. skyshrine/"Iago Sabuela", hand "Crystalline Silk Mesh" (11636) + "Oily Goo Secretion" (11637). Gives "Empty Artifact Container" (17167).
162. Loot "Crystal Dragon Eye" (11638) from "An Ice Paw Sorcerer" in `velketor`.
163. Loot "Golden Dragon Claw" (11639) from "A Chetari Runemage" in `necropolis`.
164. Loot "Platinum Dragon Scale" (11640) from "A Siren Sorceress" in `sirens`.
165. Loot "Rodrick's Head" (1045) from "Rodrick Tardok".
166. Loot "Rodrick's Head" (1045) from "Rodrick Tardok" in `eastwastes`.
167. Spawns "Poxbreath Yellowfang" (116566) in `eastwastes` on event_signal.
168. Loot "Note from Kromrif" (18084) from "Poxbreath Yellowfang".
169. Spawns "Scarbrow Ga'Hruk" (116568) in `eastwastes` on event_signal.
170. Loot "Head of Scarbrow" (30141) from "Scarbrow Ga'Hruk".
171. Say "Help" to eastwastes/"Tain Hammerfrost".
172. Spawns "Ghrek Squatnot" (116560).
173. Loot "Frozen Elixir" (30138) from "Ghrek Squatnot".
174. eastwastes/"Tain Hammerfrost", hand "Frozen Elixir" (30138). Gives "Coldain Smithing Hammer" (30140).
175. Spawns "Rabid Tundra Kodiak" (116545) in `eastwastes` on event_waypoint_arrive.
176. Loot "Rabid Kodiak Skin" (30266) from "Rabid Tundra Kodiak".
177. eastwastes/"Boridain Glacierbane", hand "Rabid Kodiak Skin" (30266). Gives "Broken Axe" (30267).
178. iceclad/"A Lost Pirate", say "I Will Find The Parts". Gives "Map Binding" (17053).
179. Loot "First part of an Iceclad Map" (30043) from "Dire Wolf Stalker" in `iceclad`.
180. Loot "Second part of an Iceclad Map" (30044) from "Stormfeather" in `iceclad`.
181. Loot "Second part of an Iceclad Map" (30044) from "The Fabled Stormfeather".
182. greatdivide/"Bloody Gnome Captive", say "Map". Gives "Third part of an Iceclad Map" (30045).
183. Loot "Fourth part of an Iceclad Map" (30073) from "Lodizal" in `iceclad`.
184. Loot "Fourth part of an Iceclad Map" (30073) from "The Fabled Lodizal".
185. Combine in "Map Binding" (17053): "First part of an Iceclad Map" (30043), "Second part of an Iceclad Map" (30044), "Third part of an Iceclad Map" (30045), "Fourth part of an Iceclad Map" (30073). Produces "Pieces of the Iceclad Map" (30046). The combine does not fail.
186. Hand "Pieces of the Iceclad Map" (30046) to iceclad/"A Lost Pirate". Spawns "Rabid Snow Cougar Does Not Exist Using Regular For Now" (116008). Loot "High Quality Cougarskin" (30030) from "Rabid Snow Cougar Does Not Exist Using Regular For Now".
187. Loot "High Quality Tundra Kodiak Pelt" (30077) from "A Tundra Kodiak" (NPC 116044) in `eastwastes`. Drop cache: 3.91% chance per kill.
188. Combine in "Vale Sewing Kit" (92882): "High Quality Cougarskin" (30030), "High Quality Tundra Kodiak Pelt" (30077). Produces "Coldain Hunting Blanket" (30135). Requires Tailoring, trivial 41.
189. eastwastes/"Garadain Glacierbane", hand "Coldain Hunting Blanket" (30135). Gives "Copper Coldain Insignia Ring" (30131).
190. eastwastes/"Garadain Glacierbane", hand "Copper Coldain Insignia Ring" (30131) + "Broken Axe" (30267). Gives "Silver Coldain Insignia Ring" (30133).
191. Ground spawn of "Skinning Rock" (30062) in `eastwastes`.
192. Loot "Wooly Rhino Horn" (30088) from "A Wooly Rhino" (NPC 116033) in `eastwastes`. Drop cache: 20% chance per kill.
193. Loot "High Quality Walrus Hide" (30096) from "A Walrus" (NPC 116065) in `eastwastes`. Drop cache: 14.1% chance per kill.
194. Combine in Forge (17): "Skinning Rock" (30062), "Wooly Rhino Horn" (30088), "High Quality Walrus Hide" (30096). Produces "Coldain Hunting Knife" (30137). Requires Blacksmithing, trivial 41.
195. eastwastes/"Garadain Glacierbane", hand "Silver Coldain Insignia Ring" (30133) + "Coldain Hunting Knife" (30137). Gives "Gold Coldain Insignia Ring" (30132).
196. eastwastes/"Garadain Glacierbane", hand "Gold Coldain Insignia Ring" (30132) + "Coldain Smithing Hammer" (30140). Gives "Platinum Coldain Insignia Ring" (30134).
197. eastwastes/"Garadain Glacierbane", hand "Platinum Coldain Insignia Ring" (30134) + "Head of Scarbrow" (30141). Gives "Obsidian Coldain Insignia Ring" (30268).
198. eastwastes/"Garadain Glacierbane", hand "Rodrick's Head" (1045) + "Note from Kromrif" (18084) + "Obsidian Coldain Insignia Ring" (30268). Gives "Mithril Coldain Insignia Ring" (30162).
199. eastwastes/"Dobbin Crossaxe", hand "Mithril Coldain Insignia Ring" (30162). Gives "Note from Corbin" (1047).
200. eastwastes/"Garadain Glacierbane", hand "Note from Corbin" (1047). Gives "Adamantium Coldain Insignia Ring" (30163).
201. eastwastes/"Garadain Glacierbane", hand "Adamantium Coldain Insignia Ring" (30163). Gives "Marching Orders" (1093).
202. Hand "Marching Orders" (1093) to eastwastes/"Gloradin Coldheart". Spawns "Oracle of Ry'Gorr" (116006). Loot "Dragon Scripture Tablet" (11651) from "Oracle of Ry'Gorr".
203. 1 alternative loot source(s) also yield Dragon Scripture Tablet (11651).
204. Combine in "Empty Artifact Container" (17167): "Crystal Dragon Eye" (11638), "Golden Dragon Claw" (11639), "Platinum Dragon Scale" (11640), "Dragon Scripture Tablet" (11651). Produces "Sealed Box" (28057). The combine does not fail.
205. Hand "Sealed Box" (28057) to kithicor/"Adjutant D-Kan". Spawns "General V'ghera" (20205). Loot "General's Pouch" (28013) from "General V'ghera".
206. 6 alternative loot source(s) also yield General's Pouch (28013).
207. Loot "Fleshripper" (5411) from "Solusek kobold king" in `soldungb`.
208. Loot "Painbringer" (5410) from "Kobold Champion" in `soldungb`.
209. Loot "Mithril Two-Handed Sword" (5401) from "The Froglok King" in `gukbottom`.
210. Loot "Gigantic Zweihander" (5308) from "Karg IceBear" in `everfrost`.
211. qey2hh1/"Vilnius The Small", hand "Gigantic Zweihander" (5308) + "Mithril Two-Handed Sword" (5401) + "Painbringer" (5410) + "Fleshripper" (5411). Gives "Jagged Diamond Dagger" (7506).
212. Loot "Robe of the Ishva" (1357) from "Coercer Q'ioul" in `kithicor`.
213. Loot "Robe of the Ishva" (1357) from "Jinalis Andir" in `cauldron`.
214. Loot "Robe of the Ishva" (1357) from "The Ishva Mal" in `southkarana`.
215. Loot "Robe of the Kedge" (1253) from "Kubaria" (NPC 309002) in `chambersf`. Drop cache: 100% chance per kill.
216. Loot "Robe of the Oracle" (1354) from "Oracle of K'Arnon" in `oceanoftears`.
217. Loot "Robe of the Oracle" (1354) from "Oracle of K'Arnon" in `oot`.
218. Loot "Shining Metallic Robes" (1360) from "Yendar Starpyre" (NPC 56012) in `steamfont`. Drop cache: 100% chance per kill.
219. qey2hh1/"Vilnius The Small", hand "Robe of the Kedge" (1253) + "Robe of the Oracle" (1354) + "Robe of the Ishva" (1357) + "Shining Metallic Robes" (1360). Gives "Cazic Quill" (7505).
220. highpass/"Stanos Herkanor", hand "Cazic Quill" (7505) + "Jagged Diamond Dagger" (7506) + "General's Pouch" (28013). Gives "Ragebringer" (11057).
221. highpass/"Stanos Herkanor", say "Hail". Sets `Fatestealer` to `1`.
222. Unresolved cyclic prerequisite: `Fatestealer_gal` ==1.
223. Unresolved cyclic prerequisite: `Fatestealer_gal` ==1.
224. Unresolved cyclic prerequisite: `Fatestealer_mar` ==1.
225. Unresolved cyclic prerequisite: `Fatestealer_gal` ==1.
226. Unresolved cyclic prerequisite: `Fatestealer_mar` ==1.
227. Unresolved cyclic prerequisite: `Fatestealer_lyt` ==1.
228. Loot "Signed Agreement" (10246) from "Lythe Songbird" in `freeporteast`.
229. Loot "Signed Agreement" (10246) from "Lythe Songbird" in `freportw`.
230. overthere/"Inem R'Ker", hand "Signed Agreement" (10246). Sets `Fatestealer_lyt` to `1`.
231. Loot "Signed Agreement" (10239) from "Seana Marsinger" in `gfaydark`.
232. Loot "Signed Agreement" (52416) from "Stefan Marsinger" in `gfaydark`.
233. overthere/"Inem R'Ker", hand "Signed Agreement" (10239) + "Signed Agreement" (52416). Sets `Fatestealer_mar` to `1`.
234. Loot "Signed Agreement" (10243) from "Galdorin Visigothe" in `abysmal`.
235. overthere/"Inem R'Ker", hand "Signed Agreement" (10243). Sets `Fatestealer_gal` to `1`.
236. overthere/"Inem R'Ker", hand "Signed Agreement" (10243). Sets `Fatestealer_bard` to `1`.
237. Spawns "a Teir'Dal guardian" (186190) in `hateplaneb` on event death_complete:186114.
238. Loot "Stack of Pages" (52335) from "a Teir'Dal guardian".
239. 5 alternative loot source(s) also yield Stack of Pages (52335).
240. steamfont/"Yendar Starpyre", hand "Stack of Pages" (52335). Sets `Fatestealer_page` to `1`.
241. Spawns "A Furious Magma Guardian" (278123) in `soldungc` on event_signal.
242. Loot "Crystallized Shard of Doomfire" (21339) from "A Furious Magma Guardian".
243. 1 alternative loot source(s) also yield Crystallized Shard of Doomfire (21339).
244. Loot "Foul Doomfire Brimstone" (21342) from "A Pool Of Living Lava" (NPC 278043) in `soldungc`. Drop cache: 15.97% chance per kill.
245. Loot "Igneous Rock of Doomfire" (21340) from "Typhoeus" (NPC 278069) in `soldungc`. Drop cache: 35% chance per kill.
246. Loot "Pile of Doomfire Ash" (21341) from "a Taklasinai marauder" (NPC 278075) in `soldungc`. Drop cache: 35% chance per kill.
247. Hand "Crystallized Shard of Doomfire" (21339) + "Igneous Rock of Doomfire" (21340) + "Pile of Doomfire Ash" (21341) + "Foul Doomfire Brimstone" (21342) to soldungc/"The Firewatcher". Spawns "Culthor the Gatekeeper" (278005). Loot "Smoldering Embers of Solusek" (52346) from "Culthor the Gatekeeper".
248. nedaria/"Smith Dandi", hand "Smoldering Embers of Solusek" (52346). Sets `Fatestealer_forge` to `1`.
249. Spawns "a Teir'Dal guardian" (186190) in `hateplaneb` on event death_complete:186114.
250. Loot "Soulstone of Lanys" (52337) from "a Teir'Dal guardian".
251. 5 alternative loot source(s) also yield Soulstone of Lanys (52337).
252. nedaria/"Lirprin, Head Of Affairs", hand "Soulstone of Lanys" (52337). Requires `Fatestealer_bard` ==1. Requires `Fatestealer_page` ==1. Requires `Fatestealer_forge` ==1. Gives "Fatestealer" (52347).
253. nedaria/"Lirprin, Head Of Affairs", say "Hail". Sets `Fatestealer` to `3`.
254. Loot "Polished Bone Horn" (52349) from "A Baleful Stoneworker" (NPC 301023) in `bloodfields`. Drop cache: 4% chance per kill.
255. Loot "Brass Mouthpiece" (52350) from "An Ukun Fleshhound" (NPC 301009) in `bloodfields`. Drop cache: 3.67% chance per kill.
256. Loot "Bucket Mute" (52351) from "An Ukun Fleshhound" (NPC 301009) in `bloodfields`. Drop cache: 3.67% chance per kill.
257. Loot "Thin Leather Straps" (52352) from "An Ukun Fleshhound" (NPC 301009) in `bloodfields`. Drop cache: 3.67% chance per kill.
258. Hand "Polished Bone Horn" (52349) + "Brass Mouthpiece" (52350) + "Bucket Mute" (52351) + "Thin Leather Straps" (52352) to bloodfields/"Caller Donivin". Spawns "A Reclusive Girplan" (301033). Loot "Jacinth" (10053) from "A Reclusive Girplan".
259. 55 alternative loot source(s) also yield Jacinth (10053).
260. freeporteast/"Wenden Blackhammer", hand "Black Sapphire" (10036) + "Diamond" (10037) + "Jacinth" (10053) + "Unjeweled Dragon Head Hilt" (20668). Gives "Jeweled Dragon Head Hilt" (20671).
261. Ground spawn of "Severely Damaged Dragon Head Hilt" (20669) in `timorous`.
262. Loot "Giant Sized Monocle" (20678) from "A Mountain Giant Patriarch" in `dreadlands`.
263. frontiermtns/"Mentrax Mountainbone", hand "Giant Sized Monocle" (20678). Gives "Rejesiam Ore" (20666).
264. Loot "Ball of Everliving Golem" (20677) from "Dread" in `fearplane`.
265. Loot "Ball of Everliving Golem" (20677) from "Fright" in `fearplane`.
266. Loot "Ball of Everliving Golem" (20677) from "Terror" in `fearplane`.
267. freeporteast/"Wenden Blackhammer", hand "Rejesiam Ore" (20666) + "Severely Damaged Dragon Head Hilt" (20669) + "Ball of Everliving Golem" (20677). Gives "Finely Crafted Dragon Head Hilt" (20672).
268. Combine in "Red Scabbard" (17859): "Ancient Sword Blade" (20667), "Ancient Blade" (20670), "Jeweled Dragon Head Hilt" (20671), "Finely Crafted Dragon Head Hilt" (20672). Produces "Jagged Blade of War" (10908). The combine does not fail.
269. freeporteast/"Gartrog Smitehammer", hand "Jagged Blade of War" (10908) + "Red Scabbard" (17859). Gives "Red Scabbard" (17869).
270. freeporteast/"Gartrog Smitehammer", hand "Jagged Blade of War" (10908) + "Red Scabbard" (17859). Gives "Jagged Blade of War" (66175).
271. Combine in "Red Scabbard" (17869): "Jagged Blade of War" (66175). Produces "Blade of Tactics" (66176), "Blade of Strategy" (66177). Requires Pottery. The combine does not fail.
272. Combine in "Red Scabbard" (17869): "Blade of Tactics" (66176), "Blade of Strategy" (66177). Produces "Jagged Blade of War" (66175). Requires Pottery. The combine does not fail.
273. draniksscar/"Korbuk Brimblade", say "Work". Sets `warrior_pre` to `1`.
274. draniksscar/"Korbuk Brimblade", hand "Korbuk's Weapon Plans" (60285). Sets `warrior_pre` to `2`.
275. draniksscar/"Korbuk Brimblade", hand "Elegant Shank" (60286). Sets `warrior_pre` to `3`.
276. Loot "Redblade Family Sword" (60287) from "Drevlon Knacknabber" in `eastkarana`.
277. freeporteast/"Kargek Redblade", hand "Redblade Family Sword" (60287). Requires `warrior_pre` set. Requires `warrior_pre` ==3. Gives "Emblazoned Champion's Hilt" (60288).
278. thurgadina/"Dardek Bladewright", hand "Korbuk's Weapon Plans" (60285) + "Elegant Shank" (60286) + "Emblazoned Champion's Hilt" (60288). Requires `warrior_pre` ==4. Gives "Dardek's Forged Blade" (60292).

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
18. Say "Tm Devrak Death" to rujd/"Rujd".
19. Spawns "spawn chest with Heavy Orcish Prison Key" (245241).
20. Loot "Pod of Water" (13044) from "spawn chest with Heavy Orcish Prison Key".
21. 6 alternative loot source(s) also yield Pod of Water (13044).
22. Forage "Pod of Water" (13044) in `ruja`.
23. Forage "Pod of Water" (13044) in `uqua`.
24. Forage "Pod of Water" (13044) in `yxtta`.
25. Combine in Brew Barrel (19): "Bottle of Aged Bloodwine" (51163), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aged Bloodwine" (51164). Requires Brewing, trivial 255.
26. Combine in Brew Barrel (19): "Bottle of Aldo's Bitter Ale" (75805), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aldo's Bitter Ale" (75811). Requires Brewing, trivial 15.
27. 17 other recipes also produce Bottle (16598).
28. Combine in Brew Barrel (19): "Pod of Water" (13044), "Bottle" (16598). Produces "Water Flask" (13006). Requires Brewing, trivial 21.
29. northro/"Verrell Cogswin", hand "Water Flask" (13006). Sets `Green_Scale_Quest` to `1`.
30. northro/"Verrell Cogswin", hand "Red Dragon Scales" (11622). Sets `Green_Scale_Quest` to `2`.
31. northro/"Verrell Cogswin", say "Adhesive". Requires `Green_Scale_Quest` ==2. Requires `Green_Scale_Quest` set. Gives "Verrell's Box of Potions" (67387).
32. Loot "Fractured Centaur Hoof" (67388) from "Centaur Archer" in `southkarana`.
33. Loot "Fractured Centaur Hoof" (67388) from "Centaur Charger" in `southkarana`.
34. Loot "Fractured Centaur Hoof" (67388) from "Centaur Courser" in `southkarana`.
35. Loot "Fractured Centaur Hoof" (67388) from "Centaur Foal" in `southkarana`.
36. Loot "Fractured Centaur Hoof" (67388) from "Centaur Sheltie" in `southkarana`.
37. Loot "Fire Giant Embers" (67389) from "A Fire Giant Warlord" (NPC 278023) in `soldungc`. Drop cache: 28.35% chance per kill.
38. Loot "Jagged Permafrost Shards" (67390) from "The Chilling Terror" in `permafrost`.
39. Combine in Oven (15): "Fractured Centaur Hoof" (67388), "Fire Giant Embers" (67389), "Jagged Permafrost Shards" (67390). Produces "Glue Powder" (67391). Requires Baking. The combine does not fail.
40. Common item: Barley (16590). Listed in 28 zones.
41. Common item: Deep Fungus Mold (67393). Listed in 28 zones.
42. Common item: Distilled Spirits (67394). Listed in 28 zones.
43. Combine in Brew Barrel (19): "Barley" (16590), "Deep Fungus Mold" (67393), "Distilled Spirits" (67394). Produces "Deep Barley Brew" (67392). Requires Brewing, trivial 110.
44. northro/"Verrell Cogswin", say "Adhesive". Requires `Green_Scale_Quest` ==2. Requires `Green_Scale_Quest` set. Gives "Potion Vial" (67395).
45. Combine in "Verrell's Box of Potions" (67387): "Glue Powder" (67391), "Deep Barley Brew" (67392), "Potion Vial" (67395). Produces "Thick Adhesive" (67386). The combine does not fail.
46. northro/"Verrell Cogswin", hand "Thick Adhesive" (67386). Gives "Grey Scale Pieces" (67385).
47. northro/"Verrell Cogswin", hand "Thick Adhesive" (67386). Gives "Thick Adhesive" (67396).
48. Combine in "Verrell's Box of Potions" (67387): "Grey Scale Pieces" (67385), "Thick Adhesive" (67396). Produces "Grey Colored Scales" (67384). The combine does not fail.
49. northro/"Verrell Cogswin", hand "Grey Colored Scales" (67384). Gives "Green Dragon Scales" (11582).
50. eastkarana/"Tenal Redblade", hand "Green Dragon Scales" (11582) + "Red Dragon Scales" (11622) + "Totem of Fiery War" (20681). Gives "Mark of the Sword" (20683).
51. Loot "Hand of the Maestro" (20676) from "Hand of the Maestro" in `hateplane`.
52. Loot "Hand of the Maestro" (20676) from "Hand of the Maestro" in `hateplaneb`.
53. eastkarana/"Tenal Redblade", hand "Hand of the Maestro" (20676) + "Mark of the Sword" (20683). Gives "Tenal's note to Kargek" (20684).
54. Loot "Spiroc Wingblade" (20679) from "The Spiroc Lord" in `airplane`.
55. freeporteast/"Kargek Redblade", hand "Spiroc Wingblade" (20679) + "Tenal's note to Kargek" (20684). Gives "Red Scabbard" (17859).
56. lakerathe/"Triathalon Swim Goggles", say "Hail". Gives "Rebreather" (16889).
57. Combine in Forge (17): "Smithing Chisel" (7052), "Large Brick of Ore" (10502). Hands back "Smithing Chisel" (7052). Produces "Small Brick of Ore" (10501). Requires Blacksmithing, trivial 27.
58. Combine in Forge (17): "Small Piece of Ore" (10500), "Water Flask" (13006). Produces "Small Brick of Ore" (10501). Requires Blacksmithing, trivial 27.
59. 11 other recipes also produce Small Brick of Ore (10501).
60. Loot "Toolbox Mold" (12077) from "Shevra Kollintar" in `paineel`.
61. kaladimb/"Jeet", say "Collect The Gnome Profit". Gives "Scrubber Key" (12164).
62. akanon/"Clockwork Scrubber", hand "Scrubber Key" (12164). Gives "Gnome Take" (12167).
63. kaladimb/"Jeet", hand "Gnome Take" (12167). Gives "Small Piece of Ore" (10500).
64. Combine in Forge (17): "Small Piece of Ore" (10500), "Water Flask" (13006). Produces "Metal Bits" (16905) x2. Requires Blacksmithing, trivial 18.
65. Combine in Forge (17): "Small Brick of Ore" (10501), "Toolbox Mold" (12077), "Water Flask" (13006), "Metal Bits" (16905). Produces "Toolbox" (17902). Requires Blacksmithing, trivial 51.
66. Common item: Platemail Helm (4001). Listed in 15 zones.
67. Fish "Fresh Fish" (13019) in `zone 0`.
68. Forage "Fresh Fish" (13019) in `kedge`.
69. Common item: Metal Rod (16850). Listed in 14 zones.
70. Common item: Metal Twine (16857). Listed in 10 zones.
71. Common item: Gnomish Bolts (16861). Listed in 10 zones.
72. Common item: Silk Lined Steel Helm (16862). Listed in 9 zones.
73. Common item: Fine Coral Mesh (16890). Listed in 14 zones.
74. Combine in "Toolbox" (17902): "Fresh Fish" (13019), "Metal Rod" (16850), "Metal Twine" (16857), "Gnomish Bolts" (16861), "Silk Lined Steel Helm" (16862), "Fine Coral Mesh" (16890). Produces "Aqualung" (16873) x20. Requires Tinkering, trivial 148.
75. Summon "Black Diamond of Nightmares" (29990) by casting "Imbue Nightmare".
76. potranquility/"Elder Fuirstel", say "Hail". Sets `pop_cod_final` to `1`.
77. poknowledge/"Aid Grimel", say "Versed In The Art Of Smithing". Requires `pop_cod_final` ==1. Requires `pop_cod_final` set. Gives "Filthy Breastplate" (15984).
78. Combine in "Mixing Bowl" (17906): "Celestial Solvent" (9731), "Words of Acquisition (Beza)" (11866). Produces "Celestial Essence" (9650). Requires Baking, trivial 15. The combine does not fail.
79. Combine in "Mixing Bowl" (17906): "Celestial Solvent" (9731), "Words of Burnishing" (11862). Produces "Celestial Essence" (9650). Requires Baking, trivial 15. The combine does not fail.
80. 67 other recipes also produce Celestial Essence (9650).
81. Common item: Jar of Acid (22133). Listed in 15 zones.
82. Combine in Brew Barrel (19): "Celestial Essence" (9650), "Jar of Acid" (22133). Produces "Acid Wash" (15987). Requires Brewing, trivial 151.
83. Combine in Forge (17): "Filthy Breastplate" (15984), "Acid Wash" (15987). Produces "Cleansed Breastplate" (15998). Requires Blacksmithing, trivial 227.
84. Common item: Mortar and Pestle (17904). Listed in 12 zones.
85. Loot "Sandstorm Pearl" (29909) from "Rorek Steelthorn" (NPC 209081) in `bothunder`. Drop cache: 5.33% chance per kill.
86. Combine in "Mortar and Pestle" (17904): "Sandstorm Pearl" (29909). Produces "Powdered Sandstorm Pearl" (29520) x4. Requires Make Poison, trivial 255.
87. Common item: Firing Sheet (16906). Listed in 34 zones.
88. Combine in Pottery Wheel (21): "Water Flask" (13006), "Block of Clay" (16901). Produces "Small Block of Clay" (16900) x3. Requires Pottery, trivial 21.
89. Combine in Pottery Wheel (21): "Small Block of Clay" (16900), "Water Flask" (13006). Produces "Block of Clay" (16901). Requires Pottery, trivial 21.
90. Combine in Pottery Wheel (21): "Water Flask" (13006), "Large Block of Clay" (16902). Produces "Block of Clay" (16901) x2. Requires Pottery, trivial 21.
91. Combine in Pottery Wheel (21): "Block of Clay" (16901), "Water Flask" (13006). Produces "Large Block of Clay" (16902). Requires Pottery, trivial 21.
92. Common item: Large Bowl Sketch (16963). Listed in 29 zones.
93. Combine in Pottery Wheel (21): "Large Block of Clay" (16902), "Water Flask" (13006), "Large Bowl Sketch" (16963). Produces "Unfired Mixing Bowl" (16930). Requires Pottery, trivial 128.
94. Combine in Kiln (22): "Firing Sheet" (16906), "Unfired Mixing Bowl" (16930). Produces "Mixing Bowl" (17906). Requires Pottery, trivial 15.
95. Combine in "Mixing Bowl" (17906): "Sandstorm Pearl" (29909). Produces "Powdered Sandstorm Pearl" (29520) x4. Requires Baking. The combine does not fail.
96. Spawns "a Koka'Vor chieftain" (210236) in `postorms` on event_signal.
97. Loot "Storm Rider Blood" (29526) from "a Koka'Vor chieftain".
98. Loot "Drop of Pure Rain" (29904) from "A vann stav" (NPC 209018) in `bothunder`. Drop cache: 4% chance per kill.
99. Combine in Brew Barrel (19): "Powdered Sandstorm Pearl" (29520), "Storm Rider Blood" (29526), "Drop of Pure Rain" (29904). Produces "Hurricane Temper" (29533). Requires Brewing, trivial 135.
100. Combine in Forge (17): "Cleansed Breastplate" (15998), "Hurricane Temper" (29533). Produces "Tempered Breastplate" (15999). Requires Blacksmithing, trivial 229.
101. Combine in Forge (17): "Black Diamond of Nightmares" (29990), "Tempered Breastplate" (15999). Produces "Imbued Breastplate" (15985). Requires Blacksmithing 220. Trivial at 275.
102. poknowledge/"Aid Grimel", hand "Imbued Breastplate" (15985). Gives "Hardened Leather Signet" (16249).
103. poknowledge/"Aid Grimel", say "Skill In Brewing". Requires `pop_cod_final` ==1. Requires `pop_cod_final` set. Gives "Portable Drink Barrel" (17179).
104. Spawns "Sepsis Rat" (45113) in `qcat` on event_death.
105. Loot "Rat Ears" (13072) from "Sepsis Rat".
106. 2 alternative loot source(s) also yield Rat Ears (13072).
107. Loot "Spider Legs" (13417) from "A Large Yellow Recluse" (NPC 56052) in `steamfont`. Drop cache: 55% chance per kill.
108. Common item: Rice (16593). Listed in 30 zones.
109. Combine in "Portable Drink Barrel" (17179): "Rat Ears" (13072), "Spider Legs" (13417), "Rice" (16593), "Bottle" (16598). Produces "Gnomish Spirits" (13037) x2. Requires Brewing, trivial 102.
110. Combine in Brew Barrel (19): "Rat Ears" (13072), "Spider Legs" (13417), "Rice" (16593), "Bottle" (16598). Produces "Gnomish Spirits" (13037) x2. Requires Brewing, trivial 102.
111. Combine in "Toolbox" (17902): "Water Flask" (13006), "Gnomish Spirits" (13037). Produces "Firewater" (16881). Requires Tinkering, trivial 17.
112. Common item: Metal Fastening (16888). Listed in 14 zones.
113. Common item: Sharkskin Tubing (16891). Listed in 14 zones.
114. Common item: Lime Coated Meshing (16892). Listed in 10 zones.
115. Combine in "Toolbox" (17902): "Platemail Helm" (4001), "Aqualung" (16873), "Firewater" (16881), "Metal Fastening" (16888), "Sharkskin Tubing" (16891), "Lime Coated Meshing" (16892). Produces "Rebreather" (16889). Requires Tinkering, trivial 175.
116. Loot "Block of Permafrost" (20665) from "Lady Vox" in `permafrost`.
117. Loot "Block of Permafrost" (20665) from "An Ice Giant" in `permafrost`.
118. Common item: Keg of Vox Tail Ale (20664). Listed in 13 zones.
119. oceanoftears/"Denken Strongpick", hand "Rebreather" (16889) + "Keg of Vox Tail Ale" (20664) + "Block of Permafrost" (20665). Gives "Ancient Sword Blade" (20667).
120. Loot "Ancient Blade" (20670) from "Queen Velazul Di'zok" in `chardok`.
121. Ground spawn of "Unjeweled Dragon Head Hilt" (20668) in `lakerathe`.
122. Loot "Apothic Crown" (1239) from "Magi P'Tasa" (NPC 186157) in `hateplaneb`. Drop cache: 19.16% chance per kill.
123. poknowledge/"Arch Mage Deidus", hand "Apothic Crown" (1239). Gives "Diamond" (10037).
124. Loot "Scroll of the Ox" (49007) from "A Sturdy Chest" in `stillmoona`.
125. Loot "Scroll of the Boar" (49008) from "A Sturdy Chest" in `stillmoona`.
126. Loot "Scroll of the Dragon" (49009) from "A Sturdy Chest" in `stillmoona`.
127. Loot "Scroll of the Tiger" (49010) from "A Sturdy Chest" in `stillmoona`.
128. Hand "Scroll of the Ox" (49007) + "Scroll of the Boar" (49008) + "Scroll of the Dragon" (49009) + "Scroll of the Tiger" (49010) to stillmoona/"The Keeper Of Strength". Spawns "A Spirit Keeper" (338169). Loot "Black Sapphire" (10036) from "A Spirit Keeper".
129. 43 alternative loot source(s) also yield Black Sapphire (10036).
130. Loot "Bayle List I" (18808) from "Mutt Rootlit" in `highpass`.
131. qrg/"Gerael Woodone", say "Deliver A Flask". Gives "Flask of Nitrates" (13945).
132. akanon/"Kimble Nogflop", hand "Flask of Nitrates" (13945). Gives "Regurgitonic" (12140).
133. qrg/"Mammoth", hand "Regurgitonic" (12140). Gives "Bayle List II" (18809).
134. Loot "Bayle List III" (18810) from "Dyllin Starsine" in `highpass`.
135. Loot "Bayle List III" (18810) from "Dyllin Starsine" in `highpasshold`.
136. southro/"Rathmana Allin", hand "Bayle List I" (18808) + "Bayle List II" (18809) + "Bayle List III" (18810). Gives "Translated Parchment" (18961).
137. highpass/"Stanos Herkanor", hand "Translated Parchment" (18961). Gives "Sealed Box" (28057).
138. Kill wakening/"A Tar Goo". Spawns "A Tar Goo" (119122).
139. Loot "Oily Goo Secretion" (11637) from "A Tar Goo".
140. 1 alternative loot source(s) also yield Oily Goo Secretion (11637).
141. bazaar/"Caerlyna", hand "Vale Sewing Kit" (92882). Gives "Vale Sewing Kit Token" (56884).
142. bazaar/"Caerlyna", hand "Vale Sewing Kit Token" (56884). Gives "Vale Sewing Kit" (92882).
143. Common item: Needle Mold (12019). Listed in 32 zones.
144. Common item: Thimble Mold (12057). Listed in 32 zones.
145. Combine in Forge (17): "Fine Steel Two Handed Sword" (5351), "Water Flask" (13006). Produces "Small Brick of High Quality Ore" (10468) x2, "Small Piece of High Quality Ore" (22229). Requires Blacksmithing, trivial 21.
146. Combine in Forge (17): "Smithing Chisel" (7052), "Small Brick of High Quality Ore" (10468). Hands back "Smithing Chisel" (7052). Produces "Small Piece of High Quality Ore" (22229) x2. Requires Blacksmithing, trivial 27.
147. 4 other recipes also produce Small Piece of High Quality Ore (22229).
148. Combine in Royal Qeynos Forge (40): "Small Piece of High Quality Ore" (22229), "Water Flask" (13006). Produces "High Quality Metal Bits" (22230). Requires Blacksmithing, trivial 20.
149. Combine in Vale Forge (49): "Needle Mold" (12019), "Thimble Mold" (12057), "Water Flask" (13006), "High Quality Metal Bits" (22230). Produces "Vale Sewing Kit" (92882). Requires Blacksmithing, trivial 162.
150. Loot "Crystalline Silk" (25306) from "A Crystal Grinder" (NPC 121089) in `crystal`. Drop cache: 100% chance per kill.
151. Combine in "Vale Sewing Kit" (92882): "Crystalline Silk" (25306). Produces "Crystalline Silk Mesh" (11636). Requires Tailoring, trivial 68.
152. skyshrine/"Iago Sabuela", hand "Crystalline Silk Mesh" (11636) + "Oily Goo Secretion" (11637). Gives "Empty Artifact Container" (17167).
153. Loot "Crystal Dragon Eye" (11638) from "An Ice Paw Sorcerer" in `velketor`.
154. Loot "Golden Dragon Claw" (11639) from "A Chetari Runemage" in `necropolis`.
155. Loot "Platinum Dragon Scale" (11640) from "A Siren Sorceress" in `sirens`.
156. Loot "Rodrick's Head" (1045) from "Rodrick Tardok".
157. Loot "Rodrick's Head" (1045) from "Rodrick Tardok" in `eastwastes`.
158. Spawns "Poxbreath Yellowfang" (116566) in `eastwastes` on event_signal.
159. Loot "Note from Kromrif" (18084) from "Poxbreath Yellowfang".
160. Spawns "Scarbrow Ga'Hruk" (116568) in `eastwastes` on event_signal.
161. Loot "Head of Scarbrow" (30141) from "Scarbrow Ga'Hruk".
162. Say "Help" to eastwastes/"Tain Hammerfrost".
163. Spawns "Ghrek Squatnot" (116560).
164. Loot "Frozen Elixir" (30138) from "Ghrek Squatnot".
165. eastwastes/"Tain Hammerfrost", hand "Frozen Elixir" (30138). Gives "Coldain Smithing Hammer" (30140).
166. Spawns "Rabid Tundra Kodiak" (116545) in `eastwastes` on event_waypoint_arrive.
167. Loot "Rabid Kodiak Skin" (30266) from "Rabid Tundra Kodiak".
168. eastwastes/"Boridain Glacierbane", hand "Rabid Kodiak Skin" (30266). Gives "Broken Axe" (30267).
169. iceclad/"A Lost Pirate", say "I Will Find The Parts". Gives "Map Binding" (17053).
170. Loot "First part of an Iceclad Map" (30043) from "Dire Wolf Stalker" in `iceclad`.
171. Loot "Second part of an Iceclad Map" (30044) from "Stormfeather" in `iceclad`.
172. Loot "Second part of an Iceclad Map" (30044) from "The Fabled Stormfeather".
173. greatdivide/"Bloody Gnome Captive", say "Map". Gives "Third part of an Iceclad Map" (30045).
174. Loot "Fourth part of an Iceclad Map" (30073) from "Lodizal" in `iceclad`.
175. Loot "Fourth part of an Iceclad Map" (30073) from "The Fabled Lodizal".
176. Combine in "Map Binding" (17053): "First part of an Iceclad Map" (30043), "Second part of an Iceclad Map" (30044), "Third part of an Iceclad Map" (30045), "Fourth part of an Iceclad Map" (30073). Produces "Pieces of the Iceclad Map" (30046). The combine does not fail.
177. Hand "Pieces of the Iceclad Map" (30046) to iceclad/"A Lost Pirate". Spawns "Rabid Snow Cougar Does Not Exist Using Regular For Now" (116008). Loot "High Quality Cougarskin" (30030) from "Rabid Snow Cougar Does Not Exist Using Regular For Now".
178. Loot "High Quality Tundra Kodiak Pelt" (30077) from "A Tundra Kodiak" (NPC 116044) in `eastwastes`. Drop cache: 3.91% chance per kill.
179. Combine in "Vale Sewing Kit" (92882): "High Quality Cougarskin" (30030), "High Quality Tundra Kodiak Pelt" (30077). Produces "Coldain Hunting Blanket" (30135). Requires Tailoring, trivial 41.
180. eastwastes/"Garadain Glacierbane", hand "Coldain Hunting Blanket" (30135). Gives "Copper Coldain Insignia Ring" (30131).
181. eastwastes/"Garadain Glacierbane", hand "Copper Coldain Insignia Ring" (30131) + "Broken Axe" (30267). Gives "Silver Coldain Insignia Ring" (30133).
182. Ground spawn of "Skinning Rock" (30062) in `eastwastes`.
183. Loot "Wooly Rhino Horn" (30088) from "A Wooly Rhino" (NPC 116033) in `eastwastes`. Drop cache: 20% chance per kill.
184. Loot "High Quality Walrus Hide" (30096) from "A Walrus" (NPC 116065) in `eastwastes`. Drop cache: 14.1% chance per kill.
185. Combine in Forge (17): "Skinning Rock" (30062), "Wooly Rhino Horn" (30088), "High Quality Walrus Hide" (30096). Produces "Coldain Hunting Knife" (30137). Requires Blacksmithing, trivial 41.
186. eastwastes/"Garadain Glacierbane", hand "Silver Coldain Insignia Ring" (30133) + "Coldain Hunting Knife" (30137). Gives "Gold Coldain Insignia Ring" (30132).
187. eastwastes/"Garadain Glacierbane", hand "Gold Coldain Insignia Ring" (30132) + "Coldain Smithing Hammer" (30140). Gives "Platinum Coldain Insignia Ring" (30134).
188. eastwastes/"Garadain Glacierbane", hand "Platinum Coldain Insignia Ring" (30134) + "Head of Scarbrow" (30141). Gives "Obsidian Coldain Insignia Ring" (30268).
189. eastwastes/"Garadain Glacierbane", hand "Rodrick's Head" (1045) + "Note from Kromrif" (18084) + "Obsidian Coldain Insignia Ring" (30268). Gives "Mithril Coldain Insignia Ring" (30162).
190. eastwastes/"Dobbin Crossaxe", hand "Mithril Coldain Insignia Ring" (30162). Gives "Note from Corbin" (1047).
191. eastwastes/"Garadain Glacierbane", hand "Note from Corbin" (1047). Gives "Adamantium Coldain Insignia Ring" (30163).
192. eastwastes/"Garadain Glacierbane", hand "Adamantium Coldain Insignia Ring" (30163). Gives "Marching Orders" (1093).
193. Hand "Marching Orders" (1093) to eastwastes/"Gloradin Coldheart". Spawns "Oracle of Ry'Gorr" (116006). Loot "Dragon Scripture Tablet" (11651) from "Oracle of Ry'Gorr".
194. 1 alternative loot source(s) also yield Dragon Scripture Tablet (11651).
195. Combine in "Empty Artifact Container" (17167): "Crystal Dragon Eye" (11638), "Golden Dragon Claw" (11639), "Platinum Dragon Scale" (11640), "Dragon Scripture Tablet" (11651). Produces "Sealed Box" (28057). The combine does not fail.
196. Hand "Sealed Box" (28057) to kithicor/"Adjutant D-Kan". Spawns "General V'ghera" (20205). Loot "General's Pouch" (28013) from "General V'ghera".
197. 6 alternative loot source(s) also yield General's Pouch (28013).
198. Loot "Fleshripper" (5411) from "Solusek kobold king" in `soldungb`.
199. Loot "Painbringer" (5410) from "Kobold Champion" in `soldungb`.
200. Loot "Mithril Two-Handed Sword" (5401) from "The Froglok King" in `gukbottom`.
201. Loot "Gigantic Zweihander" (5308) from "Karg IceBear" in `everfrost`.
202. qey2hh1/"Vilnius The Small", hand "Gigantic Zweihander" (5308) + "Mithril Two-Handed Sword" (5401) + "Painbringer" (5410) + "Fleshripper" (5411). Gives "Jagged Diamond Dagger" (7506).
203. Loot "Robe of the Ishva" (1357) from "Coercer Q'ioul" in `kithicor`.
204. Loot "Robe of the Ishva" (1357) from "Jinalis Andir" in `cauldron`.
205. Loot "Robe of the Ishva" (1357) from "The Ishva Mal" in `southkarana`.
206. Loot "Robe of the Kedge" (1253) from "Kubaria" (NPC 309002) in `chambersf`. Drop cache: 100% chance per kill.
207. Loot "Robe of the Oracle" (1354) from "Oracle of K'Arnon" in `oceanoftears`.
208. Loot "Robe of the Oracle" (1354) from "Oracle of K'Arnon" in `oot`.
209. Loot "Shining Metallic Robes" (1360) from "Yendar Starpyre" (NPC 56012) in `steamfont`. Drop cache: 100% chance per kill.
210. qey2hh1/"Vilnius The Small", hand "Robe of the Kedge" (1253) + "Robe of the Oracle" (1354) + "Robe of the Ishva" (1357) + "Shining Metallic Robes" (1360). Gives "Cazic Quill" (7505).
211. highpass/"Stanos Herkanor", hand "Cazic Quill" (7505) + "Jagged Diamond Dagger" (7506) + "General's Pouch" (28013). Gives "Ragebringer" (11057).
212. highpass/"Stanos Herkanor", say "Hail". Sets `Fatestealer` to `1`.
213. Unresolved cyclic prerequisite: `Fatestealer_gal` ==1.
214. Unresolved cyclic prerequisite: `Fatestealer_gal` ==1.
215. Unresolved cyclic prerequisite: `Fatestealer_mar` ==1.
216. Unresolved cyclic prerequisite: `Fatestealer_gal` ==1.
217. Unresolved cyclic prerequisite: `Fatestealer_mar` ==1.
218. Unresolved cyclic prerequisite: `Fatestealer_lyt` ==1.
219. Loot "Signed Agreement" (10246) from "Lythe Songbird" in `freeporteast`.
220. Loot "Signed Agreement" (10246) from "Lythe Songbird" in `freportw`.
221. overthere/"Inem R'Ker", hand "Signed Agreement" (10246). Sets `Fatestealer_lyt` to `1`.
222. Loot "Signed Agreement" (10239) from "Seana Marsinger" in `gfaydark`.
223. Loot "Signed Agreement" (52416) from "Stefan Marsinger" in `gfaydark`.
224. overthere/"Inem R'Ker", hand "Signed Agreement" (10239) + "Signed Agreement" (52416). Sets `Fatestealer_mar` to `1`.
225. Loot "Signed Agreement" (10243) from "Galdorin Visigothe" in `abysmal`.
226. overthere/"Inem R'Ker", hand "Signed Agreement" (10243). Sets `Fatestealer_gal` to `1`.
227. overthere/"Inem R'Ker", hand "Signed Agreement" (10243). Sets `Fatestealer_bard` to `1`.
228. Spawns "a Teir'Dal guardian" (186190) in `hateplaneb` on event death_complete:186114.
229. Loot "Stack of Pages" (52335) from "a Teir'Dal guardian".
230. 5 alternative loot source(s) also yield Stack of Pages (52335).
231. steamfont/"Yendar Starpyre", hand "Stack of Pages" (52335). Sets `Fatestealer_page` to `1`.
232. Spawns "A Furious Magma Guardian" (278123) in `soldungc` on event_signal.
233. Loot "Crystallized Shard of Doomfire" (21339) from "A Furious Magma Guardian".
234. 1 alternative loot source(s) also yield Crystallized Shard of Doomfire (21339).
235. Loot "Foul Doomfire Brimstone" (21342) from "A Pool Of Living Lava" (NPC 278043) in `soldungc`. Drop cache: 15.97% chance per kill.
236. Loot "Igneous Rock of Doomfire" (21340) from "Typhoeus" (NPC 278069) in `soldungc`. Drop cache: 35% chance per kill.
237. Loot "Pile of Doomfire Ash" (21341) from "a Taklasinai marauder" (NPC 278075) in `soldungc`. Drop cache: 35% chance per kill.
238. Hand "Crystallized Shard of Doomfire" (21339) + "Igneous Rock of Doomfire" (21340) + "Pile of Doomfire Ash" (21341) + "Foul Doomfire Brimstone" (21342) to soldungc/"The Firewatcher". Spawns "Culthor the Gatekeeper" (278005). Loot "Smoldering Embers of Solusek" (52346) from "Culthor the Gatekeeper".
239. nedaria/"Smith Dandi", hand "Smoldering Embers of Solusek" (52346). Sets `Fatestealer_forge` to `1`.
240. Spawns "a Teir'Dal guardian" (186190) in `hateplaneb` on event death_complete:186114.
241. Loot "Soulstone of Lanys" (52337) from "a Teir'Dal guardian".
242. 5 alternative loot source(s) also yield Soulstone of Lanys (52337).
243. nedaria/"Lirprin, Head Of Affairs", hand "Soulstone of Lanys" (52337). Requires `Fatestealer_bard` ==1. Requires `Fatestealer_page` ==1. Requires `Fatestealer_forge` ==1. Gives "Fatestealer" (52347).
244. nedaria/"Lirprin, Head Of Affairs", say "Hail". Sets `Fatestealer` to `3`.
245. Loot "Polished Bone Horn" (52349) from "A Baleful Stoneworker" (NPC 301023) in `bloodfields`. Drop cache: 4% chance per kill.
246. Loot "Brass Mouthpiece" (52350) from "An Ukun Fleshhound" (NPC 301009) in `bloodfields`. Drop cache: 3.67% chance per kill.
247. Loot "Bucket Mute" (52351) from "An Ukun Fleshhound" (NPC 301009) in `bloodfields`. Drop cache: 3.67% chance per kill.
248. Loot "Thin Leather Straps" (52352) from "An Ukun Fleshhound" (NPC 301009) in `bloodfields`. Drop cache: 3.67% chance per kill.
249. Hand "Polished Bone Horn" (52349) + "Brass Mouthpiece" (52350) + "Bucket Mute" (52351) + "Thin Leather Straps" (52352) to bloodfields/"Caller Donivin". Spawns "A Reclusive Girplan" (301033). Loot "Jacinth" (10053) from "A Reclusive Girplan".
250. 55 alternative loot source(s) also yield Jacinth (10053).
251. freeporteast/"Wenden Blackhammer", hand "Black Sapphire" (10036) + "Diamond" (10037) + "Jacinth" (10053) + "Unjeweled Dragon Head Hilt" (20668). Gives "Jeweled Dragon Head Hilt" (20671).
252. Ground spawn of "Severely Damaged Dragon Head Hilt" (20669) in `timorous`.
253. Loot "Giant Sized Monocle" (20678) from "A Mountain Giant Patriarch" in `dreadlands`.
254. frontiermtns/"Mentrax Mountainbone", hand "Giant Sized Monocle" (20678). Gives "Rejesiam Ore" (20666).
255. Loot "Ball of Everliving Golem" (20677) from "Dread" in `fearplane`.
256. Loot "Ball of Everliving Golem" (20677) from "Fright" in `fearplane`.
257. Loot "Ball of Everliving Golem" (20677) from "Terror" in `fearplane`.
258. freeporteast/"Wenden Blackhammer", hand "Rejesiam Ore" (20666) + "Severely Damaged Dragon Head Hilt" (20669) + "Ball of Everliving Golem" (20677). Gives "Finely Crafted Dragon Head Hilt" (20672).
259. Combine in "Red Scabbard" (17859): "Ancient Sword Blade" (20667), "Ancient Blade" (20670), "Jeweled Dragon Head Hilt" (20671), "Finely Crafted Dragon Head Hilt" (20672). Produces "Jagged Blade of War" (10908). The combine does not fail.
260. Combine in "Red Scabbard" (17859): "Jagged Blade of War" (10908). Produces "Blade of Tactics" (10909), "Blade of Strategy" (10910). The combine does not fail.

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
18. Say "Tm Devrak Death" to rujd/"Rujd".
19. Spawns "spawn chest with Heavy Orcish Prison Key" (245241).
20. Loot "Pod of Water" (13044) from "spawn chest with Heavy Orcish Prison Key".
21. 6 alternative loot source(s) also yield Pod of Water (13044).
22. Forage "Pod of Water" (13044) in `ruja`.
23. Forage "Pod of Water" (13044) in `uqua`.
24. Forage "Pod of Water" (13044) in `yxtta`.
25. Combine in Brew Barrel (19): "Bottle of Aged Bloodwine" (51163), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aged Bloodwine" (51164). Requires Brewing, trivial 255.
26. Combine in Brew Barrel (19): "Bottle of Aldo's Bitter Ale" (75805), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aldo's Bitter Ale" (75811). Requires Brewing, trivial 15.
27. 17 other recipes also produce Bottle (16598).
28. Combine in Brew Barrel (19): "Pod of Water" (13044), "Bottle" (16598). Produces "Water Flask" (13006). Requires Brewing, trivial 21.
29. northro/"Verrell Cogswin", hand "Water Flask" (13006). Sets `Green_Scale_Quest` to `1`.
30. northro/"Verrell Cogswin", hand "Red Dragon Scales" (11622). Sets `Green_Scale_Quest` to `2`.
31. northro/"Verrell Cogswin", say "Adhesive". Requires `Green_Scale_Quest` ==2. Requires `Green_Scale_Quest` set. Gives "Verrell's Box of Potions" (67387).
32. Loot "Fractured Centaur Hoof" (67388) from "Centaur Archer" in `southkarana`.
33. Loot "Fractured Centaur Hoof" (67388) from "Centaur Charger" in `southkarana`.
34. Loot "Fractured Centaur Hoof" (67388) from "Centaur Courser" in `southkarana`.
35. Loot "Fractured Centaur Hoof" (67388) from "Centaur Foal" in `southkarana`.
36. Loot "Fractured Centaur Hoof" (67388) from "Centaur Sheltie" in `southkarana`.
37. Loot "Fire Giant Embers" (67389) from "A Fire Giant Warlord" (NPC 278023) in `soldungc`. Drop cache: 28.35% chance per kill.
38. Loot "Jagged Permafrost Shards" (67390) from "The Chilling Terror" in `permafrost`.
39. Combine in Oven (15): "Fractured Centaur Hoof" (67388), "Fire Giant Embers" (67389), "Jagged Permafrost Shards" (67390). Produces "Glue Powder" (67391). Requires Baking. The combine does not fail.
40. Common item: Barley (16590). Listed in 28 zones.
41. Common item: Deep Fungus Mold (67393). Listed in 28 zones.
42. Common item: Distilled Spirits (67394). Listed in 28 zones.
43. Combine in Brew Barrel (19): "Barley" (16590), "Deep Fungus Mold" (67393), "Distilled Spirits" (67394). Produces "Deep Barley Brew" (67392). Requires Brewing, trivial 110.
44. northro/"Verrell Cogswin", say "Adhesive". Requires `Green_Scale_Quest` ==2. Requires `Green_Scale_Quest` set. Gives "Potion Vial" (67395).
45. Combine in "Verrell's Box of Potions" (67387): "Glue Powder" (67391), "Deep Barley Brew" (67392), "Potion Vial" (67395). Produces "Thick Adhesive" (67386). The combine does not fail.
46. northro/"Verrell Cogswin", hand "Thick Adhesive" (67386). Gives "Grey Scale Pieces" (67385).
47. northro/"Verrell Cogswin", hand "Thick Adhesive" (67386). Gives "Thick Adhesive" (67396).
48. Combine in "Verrell's Box of Potions" (67387): "Grey Scale Pieces" (67385), "Thick Adhesive" (67396). Produces "Grey Colored Scales" (67384). The combine does not fail.
49. northro/"Verrell Cogswin", hand "Grey Colored Scales" (67384). Gives "Green Dragon Scales" (11582).
50. eastkarana/"Tenal Redblade", hand "Green Dragon Scales" (11582) + "Red Dragon Scales" (11622) + "Totem of Fiery War" (20681). Gives "Mark of the Sword" (20683).
51. Loot "Hand of the Maestro" (20676) from "Hand of the Maestro" in `hateplane`.
52. Loot "Hand of the Maestro" (20676) from "Hand of the Maestro" in `hateplaneb`.
53. eastkarana/"Tenal Redblade", hand "Hand of the Maestro" (20676) + "Mark of the Sword" (20683). Gives "Tenal's note to Kargek" (20684).
54. Loot "Spiroc Wingblade" (20679) from "The Spiroc Lord" in `airplane`.
55. freeporteast/"Kargek Redblade", hand "Spiroc Wingblade" (20679) + "Tenal's note to Kargek" (20684). Gives "Red Scabbard" (17859).
56. lakerathe/"Triathalon Swim Goggles", say "Hail". Gives "Rebreather" (16889).
57. Combine in Forge (17): "Smithing Chisel" (7052), "Large Brick of Ore" (10502). Hands back "Smithing Chisel" (7052). Produces "Small Brick of Ore" (10501). Requires Blacksmithing, trivial 27.
58. Combine in Forge (17): "Small Piece of Ore" (10500), "Water Flask" (13006). Produces "Small Brick of Ore" (10501). Requires Blacksmithing, trivial 27.
59. 11 other recipes also produce Small Brick of Ore (10501).
60. Loot "Toolbox Mold" (12077) from "Shevra Kollintar" in `paineel`.
61. kaladimb/"Jeet", say "Collect The Gnome Profit". Gives "Scrubber Key" (12164).
62. akanon/"Clockwork Scrubber", hand "Scrubber Key" (12164). Gives "Gnome Take" (12167).
63. kaladimb/"Jeet", hand "Gnome Take" (12167). Gives "Small Piece of Ore" (10500).
64. Combine in Forge (17): "Small Piece of Ore" (10500), "Water Flask" (13006). Produces "Metal Bits" (16905) x2. Requires Blacksmithing, trivial 18.
65. Combine in Forge (17): "Small Brick of Ore" (10501), "Toolbox Mold" (12077), "Water Flask" (13006), "Metal Bits" (16905). Produces "Toolbox" (17902). Requires Blacksmithing, trivial 51.
66. Common item: Platemail Helm (4001). Listed in 15 zones.
67. Fish "Fresh Fish" (13019) in `zone 0`.
68. Forage "Fresh Fish" (13019) in `kedge`.
69. Common item: Metal Rod (16850). Listed in 14 zones.
70. Common item: Metal Twine (16857). Listed in 10 zones.
71. Common item: Gnomish Bolts (16861). Listed in 10 zones.
72. Common item: Silk Lined Steel Helm (16862). Listed in 9 zones.
73. Common item: Fine Coral Mesh (16890). Listed in 14 zones.
74. Combine in "Toolbox" (17902): "Fresh Fish" (13019), "Metal Rod" (16850), "Metal Twine" (16857), "Gnomish Bolts" (16861), "Silk Lined Steel Helm" (16862), "Fine Coral Mesh" (16890). Produces "Aqualung" (16873) x20. Requires Tinkering, trivial 148.
75. Summon "Black Diamond of Nightmares" (29990) by casting "Imbue Nightmare".
76. potranquility/"Elder Fuirstel", say "Hail". Sets `pop_cod_final` to `1`.
77. poknowledge/"Aid Grimel", say "Versed In The Art Of Smithing". Requires `pop_cod_final` ==1. Requires `pop_cod_final` set. Gives "Filthy Breastplate" (15984).
78. Combine in "Mixing Bowl" (17906): "Celestial Solvent" (9731), "Words of Acquisition (Beza)" (11866). Produces "Celestial Essence" (9650). Requires Baking, trivial 15. The combine does not fail.
79. Combine in "Mixing Bowl" (17906): "Celestial Solvent" (9731), "Words of Burnishing" (11862). Produces "Celestial Essence" (9650). Requires Baking, trivial 15. The combine does not fail.
80. 67 other recipes also produce Celestial Essence (9650).
81. Common item: Jar of Acid (22133). Listed in 15 zones.
82. Combine in Brew Barrel (19): "Celestial Essence" (9650), "Jar of Acid" (22133). Produces "Acid Wash" (15987). Requires Brewing, trivial 151.
83. Combine in Forge (17): "Filthy Breastplate" (15984), "Acid Wash" (15987). Produces "Cleansed Breastplate" (15998). Requires Blacksmithing, trivial 227.
84. Common item: Mortar and Pestle (17904). Listed in 12 zones.
85. Loot "Sandstorm Pearl" (29909) from "Rorek Steelthorn" (NPC 209081) in `bothunder`. Drop cache: 5.33% chance per kill.
86. Combine in "Mortar and Pestle" (17904): "Sandstorm Pearl" (29909). Produces "Powdered Sandstorm Pearl" (29520) x4. Requires Make Poison, trivial 255.
87. Common item: Firing Sheet (16906). Listed in 34 zones.
88. Combine in Pottery Wheel (21): "Water Flask" (13006), "Block of Clay" (16901). Produces "Small Block of Clay" (16900) x3. Requires Pottery, trivial 21.
89. Combine in Pottery Wheel (21): "Small Block of Clay" (16900), "Water Flask" (13006). Produces "Block of Clay" (16901). Requires Pottery, trivial 21.
90. Combine in Pottery Wheel (21): "Water Flask" (13006), "Large Block of Clay" (16902). Produces "Block of Clay" (16901) x2. Requires Pottery, trivial 21.
91. Combine in Pottery Wheel (21): "Block of Clay" (16901), "Water Flask" (13006). Produces "Large Block of Clay" (16902). Requires Pottery, trivial 21.
92. Common item: Large Bowl Sketch (16963). Listed in 29 zones.
93. Combine in Pottery Wheel (21): "Large Block of Clay" (16902), "Water Flask" (13006), "Large Bowl Sketch" (16963). Produces "Unfired Mixing Bowl" (16930). Requires Pottery, trivial 128.
94. Combine in Kiln (22): "Firing Sheet" (16906), "Unfired Mixing Bowl" (16930). Produces "Mixing Bowl" (17906). Requires Pottery, trivial 15.
95. Combine in "Mixing Bowl" (17906): "Sandstorm Pearl" (29909). Produces "Powdered Sandstorm Pearl" (29520) x4. Requires Baking. The combine does not fail.
96. Spawns "a Koka'Vor chieftain" (210236) in `postorms` on event_signal.
97. Loot "Storm Rider Blood" (29526) from "a Koka'Vor chieftain".
98. Loot "Drop of Pure Rain" (29904) from "A vann stav" (NPC 209018) in `bothunder`. Drop cache: 4% chance per kill.
99. Combine in Brew Barrel (19): "Powdered Sandstorm Pearl" (29520), "Storm Rider Blood" (29526), "Drop of Pure Rain" (29904). Produces "Hurricane Temper" (29533). Requires Brewing, trivial 135.
100. Combine in Forge (17): "Cleansed Breastplate" (15998), "Hurricane Temper" (29533). Produces "Tempered Breastplate" (15999). Requires Blacksmithing, trivial 229.
101. Combine in Forge (17): "Black Diamond of Nightmares" (29990), "Tempered Breastplate" (15999). Produces "Imbued Breastplate" (15985). Requires Blacksmithing 220. Trivial at 275.
102. poknowledge/"Aid Grimel", hand "Imbued Breastplate" (15985). Gives "Hardened Leather Signet" (16249).
103. poknowledge/"Aid Grimel", say "Skill In Brewing". Requires `pop_cod_final` ==1. Requires `pop_cod_final` set. Gives "Portable Drink Barrel" (17179).
104. Spawns "Sepsis Rat" (45113) in `qcat` on event_death.
105. Loot "Rat Ears" (13072) from "Sepsis Rat".
106. 2 alternative loot source(s) also yield Rat Ears (13072).
107. Loot "Spider Legs" (13417) from "A Large Yellow Recluse" (NPC 56052) in `steamfont`. Drop cache: 55% chance per kill.
108. Common item: Rice (16593). Listed in 30 zones.
109. Combine in "Portable Drink Barrel" (17179): "Rat Ears" (13072), "Spider Legs" (13417), "Rice" (16593), "Bottle" (16598). Produces "Gnomish Spirits" (13037) x2. Requires Brewing, trivial 102.
110. Combine in Brew Barrel (19): "Rat Ears" (13072), "Spider Legs" (13417), "Rice" (16593), "Bottle" (16598). Produces "Gnomish Spirits" (13037) x2. Requires Brewing, trivial 102.
111. Combine in "Toolbox" (17902): "Water Flask" (13006), "Gnomish Spirits" (13037). Produces "Firewater" (16881). Requires Tinkering, trivial 17.
112. Common item: Metal Fastening (16888). Listed in 14 zones.
113. Common item: Sharkskin Tubing (16891). Listed in 14 zones.
114. Common item: Lime Coated Meshing (16892). Listed in 10 zones.
115. Combine in "Toolbox" (17902): "Platemail Helm" (4001), "Aqualung" (16873), "Firewater" (16881), "Metal Fastening" (16888), "Sharkskin Tubing" (16891), "Lime Coated Meshing" (16892). Produces "Rebreather" (16889). Requires Tinkering, trivial 175.
116. Loot "Block of Permafrost" (20665) from "Lady Vox" in `permafrost`.
117. Loot "Block of Permafrost" (20665) from "An Ice Giant" in `permafrost`.
118. Common item: Keg of Vox Tail Ale (20664). Listed in 13 zones.
119. oceanoftears/"Denken Strongpick", hand "Rebreather" (16889) + "Keg of Vox Tail Ale" (20664) + "Block of Permafrost" (20665). Gives "Ancient Sword Blade" (20667).
120. Loot "Ancient Blade" (20670) from "Queen Velazul Di'zok" in `chardok`.
121. Ground spawn of "Unjeweled Dragon Head Hilt" (20668) in `lakerathe`.
122. Loot "Apothic Crown" (1239) from "Magi P'Tasa" (NPC 186157) in `hateplaneb`. Drop cache: 19.16% chance per kill.
123. poknowledge/"Arch Mage Deidus", hand "Apothic Crown" (1239). Gives "Diamond" (10037).
124. Loot "Scroll of the Ox" (49007) from "A Sturdy Chest" in `stillmoona`.
125. Loot "Scroll of the Boar" (49008) from "A Sturdy Chest" in `stillmoona`.
126. Loot "Scroll of the Dragon" (49009) from "A Sturdy Chest" in `stillmoona`.
127. Loot "Scroll of the Tiger" (49010) from "A Sturdy Chest" in `stillmoona`.
128. Hand "Scroll of the Ox" (49007) + "Scroll of the Boar" (49008) + "Scroll of the Dragon" (49009) + "Scroll of the Tiger" (49010) to stillmoona/"The Keeper Of Strength". Spawns "A Spirit Keeper" (338169). Loot "Black Sapphire" (10036) from "A Spirit Keeper".
129. 43 alternative loot source(s) also yield Black Sapphire (10036).
130. Loot "Bayle List I" (18808) from "Mutt Rootlit" in `highpass`.
131. qrg/"Gerael Woodone", say "Deliver A Flask". Gives "Flask of Nitrates" (13945).
132. akanon/"Kimble Nogflop", hand "Flask of Nitrates" (13945). Gives "Regurgitonic" (12140).
133. qrg/"Mammoth", hand "Regurgitonic" (12140). Gives "Bayle List II" (18809).
134. Loot "Bayle List III" (18810) from "Dyllin Starsine" in `highpass`.
135. Loot "Bayle List III" (18810) from "Dyllin Starsine" in `highpasshold`.
136. southro/"Rathmana Allin", hand "Bayle List I" (18808) + "Bayle List II" (18809) + "Bayle List III" (18810). Gives "Translated Parchment" (18961).
137. highpass/"Stanos Herkanor", hand "Translated Parchment" (18961). Gives "Sealed Box" (28057).
138. Kill wakening/"A Tar Goo". Spawns "A Tar Goo" (119122).
139. Loot "Oily Goo Secretion" (11637) from "A Tar Goo".
140. 1 alternative loot source(s) also yield Oily Goo Secretion (11637).
141. bazaar/"Caerlyna", hand "Vale Sewing Kit" (92882). Gives "Vale Sewing Kit Token" (56884).
142. bazaar/"Caerlyna", hand "Vale Sewing Kit Token" (56884). Gives "Vale Sewing Kit" (92882).
143. Common item: Needle Mold (12019). Listed in 32 zones.
144. Common item: Thimble Mold (12057). Listed in 32 zones.
145. Combine in Forge (17): "Fine Steel Two Handed Sword" (5351), "Water Flask" (13006). Produces "Small Brick of High Quality Ore" (10468) x2, "Small Piece of High Quality Ore" (22229). Requires Blacksmithing, trivial 21.
146. Combine in Forge (17): "Smithing Chisel" (7052), "Small Brick of High Quality Ore" (10468). Hands back "Smithing Chisel" (7052). Produces "Small Piece of High Quality Ore" (22229) x2. Requires Blacksmithing, trivial 27.
147. 4 other recipes also produce Small Piece of High Quality Ore (22229).
148. Combine in Royal Qeynos Forge (40): "Small Piece of High Quality Ore" (22229), "Water Flask" (13006). Produces "High Quality Metal Bits" (22230). Requires Blacksmithing, trivial 20.
149. Combine in Vale Forge (49): "Needle Mold" (12019), "Thimble Mold" (12057), "Water Flask" (13006), "High Quality Metal Bits" (22230). Produces "Vale Sewing Kit" (92882). Requires Blacksmithing, trivial 162.
150. Loot "Crystalline Silk" (25306) from "A Crystal Grinder" (NPC 121089) in `crystal`. Drop cache: 100% chance per kill.
151. Combine in "Vale Sewing Kit" (92882): "Crystalline Silk" (25306). Produces "Crystalline Silk Mesh" (11636). Requires Tailoring, trivial 68.
152. skyshrine/"Iago Sabuela", hand "Crystalline Silk Mesh" (11636) + "Oily Goo Secretion" (11637). Gives "Empty Artifact Container" (17167).
153. Loot "Crystal Dragon Eye" (11638) from "An Ice Paw Sorcerer" in `velketor`.
154. Loot "Golden Dragon Claw" (11639) from "A Chetari Runemage" in `necropolis`.
155. Loot "Platinum Dragon Scale" (11640) from "A Siren Sorceress" in `sirens`.
156. Loot "Rodrick's Head" (1045) from "Rodrick Tardok".
157. Loot "Rodrick's Head" (1045) from "Rodrick Tardok" in `eastwastes`.
158. Spawns "Poxbreath Yellowfang" (116566) in `eastwastes` on event_signal.
159. Loot "Note from Kromrif" (18084) from "Poxbreath Yellowfang".
160. Spawns "Scarbrow Ga'Hruk" (116568) in `eastwastes` on event_signal.
161. Loot "Head of Scarbrow" (30141) from "Scarbrow Ga'Hruk".
162. Say "Help" to eastwastes/"Tain Hammerfrost".
163. Spawns "Ghrek Squatnot" (116560).
164. Loot "Frozen Elixir" (30138) from "Ghrek Squatnot".
165. eastwastes/"Tain Hammerfrost", hand "Frozen Elixir" (30138). Gives "Coldain Smithing Hammer" (30140).
166. Spawns "Rabid Tundra Kodiak" (116545) in `eastwastes` on event_waypoint_arrive.
167. Loot "Rabid Kodiak Skin" (30266) from "Rabid Tundra Kodiak".
168. eastwastes/"Boridain Glacierbane", hand "Rabid Kodiak Skin" (30266). Gives "Broken Axe" (30267).
169. iceclad/"A Lost Pirate", say "I Will Find The Parts". Gives "Map Binding" (17053).
170. Loot "First part of an Iceclad Map" (30043) from "Dire Wolf Stalker" in `iceclad`.
171. Loot "Second part of an Iceclad Map" (30044) from "Stormfeather" in `iceclad`.
172. Loot "Second part of an Iceclad Map" (30044) from "The Fabled Stormfeather".
173. greatdivide/"Bloody Gnome Captive", say "Map". Gives "Third part of an Iceclad Map" (30045).
174. Loot "Fourth part of an Iceclad Map" (30073) from "Lodizal" in `iceclad`.
175. Loot "Fourth part of an Iceclad Map" (30073) from "The Fabled Lodizal".
176. Combine in "Map Binding" (17053): "First part of an Iceclad Map" (30043), "Second part of an Iceclad Map" (30044), "Third part of an Iceclad Map" (30045), "Fourth part of an Iceclad Map" (30073). Produces "Pieces of the Iceclad Map" (30046). The combine does not fail.
177. Hand "Pieces of the Iceclad Map" (30046) to iceclad/"A Lost Pirate". Spawns "Rabid Snow Cougar Does Not Exist Using Regular For Now" (116008). Loot "High Quality Cougarskin" (30030) from "Rabid Snow Cougar Does Not Exist Using Regular For Now".
178. Loot "High Quality Tundra Kodiak Pelt" (30077) from "A Tundra Kodiak" (NPC 116044) in `eastwastes`. Drop cache: 3.91% chance per kill.
179. Combine in "Vale Sewing Kit" (92882): "High Quality Cougarskin" (30030), "High Quality Tundra Kodiak Pelt" (30077). Produces "Coldain Hunting Blanket" (30135). Requires Tailoring, trivial 41.
180. eastwastes/"Garadain Glacierbane", hand "Coldain Hunting Blanket" (30135). Gives "Copper Coldain Insignia Ring" (30131).
181. eastwastes/"Garadain Glacierbane", hand "Copper Coldain Insignia Ring" (30131) + "Broken Axe" (30267). Gives "Silver Coldain Insignia Ring" (30133).
182. Ground spawn of "Skinning Rock" (30062) in `eastwastes`.
183. Loot "Wooly Rhino Horn" (30088) from "A Wooly Rhino" (NPC 116033) in `eastwastes`. Drop cache: 20% chance per kill.
184. Loot "High Quality Walrus Hide" (30096) from "A Walrus" (NPC 116065) in `eastwastes`. Drop cache: 14.1% chance per kill.
185. Combine in Forge (17): "Skinning Rock" (30062), "Wooly Rhino Horn" (30088), "High Quality Walrus Hide" (30096). Produces "Coldain Hunting Knife" (30137). Requires Blacksmithing, trivial 41.
186. eastwastes/"Garadain Glacierbane", hand "Silver Coldain Insignia Ring" (30133) + "Coldain Hunting Knife" (30137). Gives "Gold Coldain Insignia Ring" (30132).
187. eastwastes/"Garadain Glacierbane", hand "Gold Coldain Insignia Ring" (30132) + "Coldain Smithing Hammer" (30140). Gives "Platinum Coldain Insignia Ring" (30134).
188. eastwastes/"Garadain Glacierbane", hand "Platinum Coldain Insignia Ring" (30134) + "Head of Scarbrow" (30141). Gives "Obsidian Coldain Insignia Ring" (30268).
189. eastwastes/"Garadain Glacierbane", hand "Rodrick's Head" (1045) + "Note from Kromrif" (18084) + "Obsidian Coldain Insignia Ring" (30268). Gives "Mithril Coldain Insignia Ring" (30162).
190. eastwastes/"Dobbin Crossaxe", hand "Mithril Coldain Insignia Ring" (30162). Gives "Note from Corbin" (1047).
191. eastwastes/"Garadain Glacierbane", hand "Note from Corbin" (1047). Gives "Adamantium Coldain Insignia Ring" (30163).
192. eastwastes/"Garadain Glacierbane", hand "Adamantium Coldain Insignia Ring" (30163). Gives "Marching Orders" (1093).
193. Hand "Marching Orders" (1093) to eastwastes/"Gloradin Coldheart". Spawns "Oracle of Ry'Gorr" (116006). Loot "Dragon Scripture Tablet" (11651) from "Oracle of Ry'Gorr".
194. 1 alternative loot source(s) also yield Dragon Scripture Tablet (11651).
195. Combine in "Empty Artifact Container" (17167): "Crystal Dragon Eye" (11638), "Golden Dragon Claw" (11639), "Platinum Dragon Scale" (11640), "Dragon Scripture Tablet" (11651). Produces "Sealed Box" (28057). The combine does not fail.
196. Hand "Sealed Box" (28057) to kithicor/"Adjutant D-Kan". Spawns "General V'ghera" (20205). Loot "General's Pouch" (28013) from "General V'ghera".
197. 6 alternative loot source(s) also yield General's Pouch (28013).
198. Loot "Fleshripper" (5411) from "Solusek kobold king" in `soldungb`.
199. Loot "Painbringer" (5410) from "Kobold Champion" in `soldungb`.
200. Loot "Mithril Two-Handed Sword" (5401) from "The Froglok King" in `gukbottom`.
201. Loot "Gigantic Zweihander" (5308) from "Karg IceBear" in `everfrost`.
202. qey2hh1/"Vilnius The Small", hand "Gigantic Zweihander" (5308) + "Mithril Two-Handed Sword" (5401) + "Painbringer" (5410) + "Fleshripper" (5411). Gives "Jagged Diamond Dagger" (7506).
203. Loot "Robe of the Ishva" (1357) from "Coercer Q'ioul" in `kithicor`.
204. Loot "Robe of the Ishva" (1357) from "Jinalis Andir" in `cauldron`.
205. Loot "Robe of the Ishva" (1357) from "The Ishva Mal" in `southkarana`.
206. Loot "Robe of the Kedge" (1253) from "Kubaria" (NPC 309002) in `chambersf`. Drop cache: 100% chance per kill.
207. Loot "Robe of the Oracle" (1354) from "Oracle of K'Arnon" in `oceanoftears`.
208. Loot "Robe of the Oracle" (1354) from "Oracle of K'Arnon" in `oot`.
209. Loot "Shining Metallic Robes" (1360) from "Yendar Starpyre" (NPC 56012) in `steamfont`. Drop cache: 100% chance per kill.
210. qey2hh1/"Vilnius The Small", hand "Robe of the Kedge" (1253) + "Robe of the Oracle" (1354) + "Robe of the Ishva" (1357) + "Shining Metallic Robes" (1360). Gives "Cazic Quill" (7505).
211. highpass/"Stanos Herkanor", hand "Cazic Quill" (7505) + "Jagged Diamond Dagger" (7506) + "General's Pouch" (28013). Gives "Ragebringer" (11057).
212. highpass/"Stanos Herkanor", say "Hail". Sets `Fatestealer` to `1`.
213. Unresolved cyclic prerequisite: `Fatestealer_gal` ==1.
214. Unresolved cyclic prerequisite: `Fatestealer_gal` ==1.
215. Unresolved cyclic prerequisite: `Fatestealer_mar` ==1.
216. Unresolved cyclic prerequisite: `Fatestealer_gal` ==1.
217. Unresolved cyclic prerequisite: `Fatestealer_mar` ==1.
218. Unresolved cyclic prerequisite: `Fatestealer_lyt` ==1.
219. Loot "Signed Agreement" (10246) from "Lythe Songbird" in `freeporteast`.
220. Loot "Signed Agreement" (10246) from "Lythe Songbird" in `freportw`.
221. overthere/"Inem R'Ker", hand "Signed Agreement" (10246). Sets `Fatestealer_lyt` to `1`.
222. Loot "Signed Agreement" (10239) from "Seana Marsinger" in `gfaydark`.
223. Loot "Signed Agreement" (52416) from "Stefan Marsinger" in `gfaydark`.
224. overthere/"Inem R'Ker", hand "Signed Agreement" (10239) + "Signed Agreement" (52416). Sets `Fatestealer_mar` to `1`.
225. Loot "Signed Agreement" (10243) from "Galdorin Visigothe" in `abysmal`.
226. overthere/"Inem R'Ker", hand "Signed Agreement" (10243). Sets `Fatestealer_gal` to `1`.
227. overthere/"Inem R'Ker", hand "Signed Agreement" (10243). Sets `Fatestealer_bard` to `1`.
228. Spawns "a Teir'Dal guardian" (186190) in `hateplaneb` on event death_complete:186114.
229. Loot "Stack of Pages" (52335) from "a Teir'Dal guardian".
230. 5 alternative loot source(s) also yield Stack of Pages (52335).
231. steamfont/"Yendar Starpyre", hand "Stack of Pages" (52335). Sets `Fatestealer_page` to `1`.
232. Spawns "A Furious Magma Guardian" (278123) in `soldungc` on event_signal.
233. Loot "Crystallized Shard of Doomfire" (21339) from "A Furious Magma Guardian".
234. 1 alternative loot source(s) also yield Crystallized Shard of Doomfire (21339).
235. Loot "Foul Doomfire Brimstone" (21342) from "A Pool Of Living Lava" (NPC 278043) in `soldungc`. Drop cache: 15.97% chance per kill.
236. Loot "Igneous Rock of Doomfire" (21340) from "Typhoeus" (NPC 278069) in `soldungc`. Drop cache: 35% chance per kill.
237. Loot "Pile of Doomfire Ash" (21341) from "a Taklasinai marauder" (NPC 278075) in `soldungc`. Drop cache: 35% chance per kill.
238. Hand "Crystallized Shard of Doomfire" (21339) + "Igneous Rock of Doomfire" (21340) + "Pile of Doomfire Ash" (21341) + "Foul Doomfire Brimstone" (21342) to soldungc/"The Firewatcher". Spawns "Culthor the Gatekeeper" (278005). Loot "Smoldering Embers of Solusek" (52346) from "Culthor the Gatekeeper".
239. nedaria/"Smith Dandi", hand "Smoldering Embers of Solusek" (52346). Sets `Fatestealer_forge` to `1`.
240. Spawns "a Teir'Dal guardian" (186190) in `hateplaneb` on event death_complete:186114.
241. Loot "Soulstone of Lanys" (52337) from "a Teir'Dal guardian".
242. 5 alternative loot source(s) also yield Soulstone of Lanys (52337).
243. nedaria/"Lirprin, Head Of Affairs", hand "Soulstone of Lanys" (52337). Requires `Fatestealer_bard` ==1. Requires `Fatestealer_page` ==1. Requires `Fatestealer_forge` ==1. Gives "Fatestealer" (52347).
244. nedaria/"Lirprin, Head Of Affairs", say "Hail". Sets `Fatestealer` to `3`.
245. Loot "Polished Bone Horn" (52349) from "A Baleful Stoneworker" (NPC 301023) in `bloodfields`. Drop cache: 4% chance per kill.
246. Loot "Brass Mouthpiece" (52350) from "An Ukun Fleshhound" (NPC 301009) in `bloodfields`. Drop cache: 3.67% chance per kill.
247. Loot "Bucket Mute" (52351) from "An Ukun Fleshhound" (NPC 301009) in `bloodfields`. Drop cache: 3.67% chance per kill.
248. Loot "Thin Leather Straps" (52352) from "An Ukun Fleshhound" (NPC 301009) in `bloodfields`. Drop cache: 3.67% chance per kill.
249. Hand "Polished Bone Horn" (52349) + "Brass Mouthpiece" (52350) + "Bucket Mute" (52351) + "Thin Leather Straps" (52352) to bloodfields/"Caller Donivin". Spawns "A Reclusive Girplan" (301033). Loot "Jacinth" (10053) from "A Reclusive Girplan".
250. 55 alternative loot source(s) also yield Jacinth (10053).
251. freeporteast/"Wenden Blackhammer", hand "Black Sapphire" (10036) + "Diamond" (10037) + "Jacinth" (10053) + "Unjeweled Dragon Head Hilt" (20668). Gives "Jeweled Dragon Head Hilt" (20671).
252. Ground spawn of "Severely Damaged Dragon Head Hilt" (20669) in `timorous`.
253. Loot "Giant Sized Monocle" (20678) from "A Mountain Giant Patriarch" in `dreadlands`.
254. frontiermtns/"Mentrax Mountainbone", hand "Giant Sized Monocle" (20678). Gives "Rejesiam Ore" (20666).
255. Loot "Ball of Everliving Golem" (20677) from "Dread" in `fearplane`.
256. Loot "Ball of Everliving Golem" (20677) from "Fright" in `fearplane`.
257. Loot "Ball of Everliving Golem" (20677) from "Terror" in `fearplane`.
258. freeporteast/"Wenden Blackhammer", hand "Rejesiam Ore" (20666) + "Severely Damaged Dragon Head Hilt" (20669) + "Ball of Everliving Golem" (20677). Gives "Finely Crafted Dragon Head Hilt" (20672).
259. Combine in "Red Scabbard" (17859): "Ancient Sword Blade" (20667), "Ancient Blade" (20670), "Jeweled Dragon Head Hilt" (20671), "Finely Crafted Dragon Head Hilt" (20672). Produces "Jagged Blade of War" (10908). The combine does not fail.
260. Combine in "Red Scabbard" (17859): "Jagged Blade of War" (10908). Produces "Blade of Tactics" (10909), "Blade of Strategy" (10910). The combine does not fail.

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
18. Say "Tm Devrak Death" to rujd/"Rujd".
19. Spawns "spawn chest with Heavy Orcish Prison Key" (245241).
20. Loot "Pod of Water" (13044) from "spawn chest with Heavy Orcish Prison Key".
21. 6 alternative loot source(s) also yield Pod of Water (13044).
22. Forage "Pod of Water" (13044) in `ruja`.
23. Forage "Pod of Water" (13044) in `uqua`.
24. Forage "Pod of Water" (13044) in `yxtta`.
25. Combine in Brew Barrel (19): "Bottle of Aged Bloodwine" (51163), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aged Bloodwine" (51164). Requires Brewing, trivial 255.
26. Combine in Brew Barrel (19): "Bottle of Aldo's Bitter Ale" (75805), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aldo's Bitter Ale" (75811). Requires Brewing, trivial 15.
27. 17 other recipes also produce Bottle (16598).
28. Combine in Brew Barrel (19): "Pod of Water" (13044), "Bottle" (16598). Produces "Water Flask" (13006). Requires Brewing, trivial 21.
29. northro/"Verrell Cogswin", hand "Water Flask" (13006). Sets `Green_Scale_Quest` to `1`.
30. northro/"Verrell Cogswin", hand "Red Dragon Scales" (11622). Sets `Green_Scale_Quest` to `2`.
31. northro/"Verrell Cogswin", say "Adhesive". Requires `Green_Scale_Quest` ==2. Requires `Green_Scale_Quest` set. Gives "Verrell's Box of Potions" (67387).
32. Loot "Fractured Centaur Hoof" (67388) from "Centaur Archer" in `southkarana`.
33. Loot "Fractured Centaur Hoof" (67388) from "Centaur Charger" in `southkarana`.
34. Loot "Fractured Centaur Hoof" (67388) from "Centaur Courser" in `southkarana`.
35. Loot "Fractured Centaur Hoof" (67388) from "Centaur Foal" in `southkarana`.
36. Loot "Fractured Centaur Hoof" (67388) from "Centaur Sheltie" in `southkarana`.
37. Loot "Fire Giant Embers" (67389) from "A Fire Giant Warlord" (NPC 278023) in `soldungc`. Drop cache: 28.35% chance per kill.
38. Loot "Jagged Permafrost Shards" (67390) from "The Chilling Terror" in `permafrost`.
39. Combine in Oven (15): "Fractured Centaur Hoof" (67388), "Fire Giant Embers" (67389), "Jagged Permafrost Shards" (67390). Produces "Glue Powder" (67391). Requires Baking. The combine does not fail.
40. Common item: Barley (16590). Listed in 28 zones.
41. Common item: Deep Fungus Mold (67393). Listed in 28 zones.
42. Common item: Distilled Spirits (67394). Listed in 28 zones.
43. Combine in Brew Barrel (19): "Barley" (16590), "Deep Fungus Mold" (67393), "Distilled Spirits" (67394). Produces "Deep Barley Brew" (67392). Requires Brewing, trivial 110.
44. northro/"Verrell Cogswin", say "Adhesive". Requires `Green_Scale_Quest` ==2. Requires `Green_Scale_Quest` set. Gives "Potion Vial" (67395).
45. Combine in "Verrell's Box of Potions" (67387): "Glue Powder" (67391), "Deep Barley Brew" (67392), "Potion Vial" (67395). Produces "Thick Adhesive" (67386). The combine does not fail.
46. northro/"Verrell Cogswin", hand "Thick Adhesive" (67386). Gives "Grey Scale Pieces" (67385).
47. northro/"Verrell Cogswin", hand "Thick Adhesive" (67386). Gives "Thick Adhesive" (67396).
48. Combine in "Verrell's Box of Potions" (67387): "Grey Scale Pieces" (67385), "Thick Adhesive" (67396). Produces "Grey Colored Scales" (67384). The combine does not fail.
49. northro/"Verrell Cogswin", hand "Grey Colored Scales" (67384). Gives "Green Dragon Scales" (11582).
50. eastkarana/"Tenal Redblade", hand "Green Dragon Scales" (11582) + "Red Dragon Scales" (11622) + "Totem of Fiery War" (20681). Gives "Mark of the Sword" (20683).
51. Loot "Hand of the Maestro" (20676) from "Hand of the Maestro" in `hateplane`.
52. Loot "Hand of the Maestro" (20676) from "Hand of the Maestro" in `hateplaneb`.
53. eastkarana/"Tenal Redblade", hand "Hand of the Maestro" (20676) + "Mark of the Sword" (20683). Gives "Tenal's note to Kargek" (20684).
54. Loot "Spiroc Wingblade" (20679) from "The Spiroc Lord" in `airplane`.
55. freeporteast/"Kargek Redblade", hand "Spiroc Wingblade" (20679) + "Tenal's note to Kargek" (20684). Gives "Red Scabbard" (17859).
56. Combine in "Red Scabbard" (17859): "Jagged Blade of War" (10908). Produces "Blade of Tactics" (10909), "Blade of Strategy" (10910). The combine does not fail.
57. Combine in "Red Scabbard" (17859): "Blade of Tactics" (10909), "Blade of Strategy" (10910). Produces "Jagged Blade of War" (10908). The combine does not fail.
58. lakerathe/"Triathalon Swim Goggles", say "Hail". Gives "Rebreather" (16889).
59. Combine in Forge (17): "Smithing Chisel" (7052), "Large Brick of Ore" (10502). Hands back "Smithing Chisel" (7052). Produces "Small Brick of Ore" (10501). Requires Blacksmithing, trivial 27.
60. Combine in Forge (17): "Small Piece of Ore" (10500), "Water Flask" (13006). Produces "Small Brick of Ore" (10501). Requires Blacksmithing, trivial 27.
61. 11 other recipes also produce Small Brick of Ore (10501).
62. Loot "Toolbox Mold" (12077) from "Shevra Kollintar" in `paineel`.
63. kaladimb/"Jeet", say "Collect The Gnome Profit". Gives "Scrubber Key" (12164).
64. akanon/"Clockwork Scrubber", hand "Scrubber Key" (12164). Gives "Gnome Take" (12167).
65. kaladimb/"Jeet", hand "Gnome Take" (12167). Gives "Small Piece of Ore" (10500).
66. Combine in Forge (17): "Small Piece of Ore" (10500), "Water Flask" (13006). Produces "Metal Bits" (16905) x2. Requires Blacksmithing, trivial 18.
67. Combine in Forge (17): "Small Brick of Ore" (10501), "Toolbox Mold" (12077), "Water Flask" (13006), "Metal Bits" (16905). Produces "Toolbox" (17902). Requires Blacksmithing, trivial 51.
68. Common item: Platemail Helm (4001). Listed in 15 zones.
69. Fish "Fresh Fish" (13019) in `zone 0`.
70. Forage "Fresh Fish" (13019) in `kedge`.
71. Common item: Metal Rod (16850). Listed in 14 zones.
72. Common item: Metal Twine (16857). Listed in 10 zones.
73. Common item: Gnomish Bolts (16861). Listed in 10 zones.
74. Common item: Silk Lined Steel Helm (16862). Listed in 9 zones.
75. Common item: Fine Coral Mesh (16890). Listed in 14 zones.
76. Combine in "Toolbox" (17902): "Fresh Fish" (13019), "Metal Rod" (16850), "Metal Twine" (16857), "Gnomish Bolts" (16861), "Silk Lined Steel Helm" (16862), "Fine Coral Mesh" (16890). Produces "Aqualung" (16873) x20. Requires Tinkering, trivial 148.
77. Summon "Black Diamond of Nightmares" (29990) by casting "Imbue Nightmare".
78. potranquility/"Elder Fuirstel", say "Hail". Sets `pop_cod_final` to `1`.
79. poknowledge/"Aid Grimel", say "Versed In The Art Of Smithing". Requires `pop_cod_final` ==1. Requires `pop_cod_final` set. Gives "Filthy Breastplate" (15984).
80. Combine in "Mixing Bowl" (17906): "Celestial Solvent" (9731), "Words of Acquisition (Beza)" (11866). Produces "Celestial Essence" (9650). Requires Baking, trivial 15. The combine does not fail.
81. Combine in "Mixing Bowl" (17906): "Celestial Solvent" (9731), "Words of Burnishing" (11862). Produces "Celestial Essence" (9650). Requires Baking, trivial 15. The combine does not fail.
82. 67 other recipes also produce Celestial Essence (9650).
83. Common item: Jar of Acid (22133). Listed in 15 zones.
84. Combine in Brew Barrel (19): "Celestial Essence" (9650), "Jar of Acid" (22133). Produces "Acid Wash" (15987). Requires Brewing, trivial 151.
85. Combine in Forge (17): "Filthy Breastplate" (15984), "Acid Wash" (15987). Produces "Cleansed Breastplate" (15998). Requires Blacksmithing, trivial 227.
86. Common item: Mortar and Pestle (17904). Listed in 12 zones.
87. Loot "Sandstorm Pearl" (29909) from "Rorek Steelthorn" (NPC 209081) in `bothunder`. Drop cache: 5.33% chance per kill.
88. Combine in "Mortar and Pestle" (17904): "Sandstorm Pearl" (29909). Produces "Powdered Sandstorm Pearl" (29520) x4. Requires Make Poison, trivial 255.
89. Common item: Firing Sheet (16906). Listed in 34 zones.
90. Combine in Pottery Wheel (21): "Water Flask" (13006), "Block of Clay" (16901). Produces "Small Block of Clay" (16900) x3. Requires Pottery, trivial 21.
91. Combine in Pottery Wheel (21): "Small Block of Clay" (16900), "Water Flask" (13006). Produces "Block of Clay" (16901). Requires Pottery, trivial 21.
92. Combine in Pottery Wheel (21): "Water Flask" (13006), "Large Block of Clay" (16902). Produces "Block of Clay" (16901) x2. Requires Pottery, trivial 21.
93. Combine in Pottery Wheel (21): "Block of Clay" (16901), "Water Flask" (13006). Produces "Large Block of Clay" (16902). Requires Pottery, trivial 21.
94. Common item: Large Bowl Sketch (16963). Listed in 29 zones.
95. Combine in Pottery Wheel (21): "Large Block of Clay" (16902), "Water Flask" (13006), "Large Bowl Sketch" (16963). Produces "Unfired Mixing Bowl" (16930). Requires Pottery, trivial 128.
96. Combine in Kiln (22): "Firing Sheet" (16906), "Unfired Mixing Bowl" (16930). Produces "Mixing Bowl" (17906). Requires Pottery, trivial 15.
97. Combine in "Mixing Bowl" (17906): "Sandstorm Pearl" (29909). Produces "Powdered Sandstorm Pearl" (29520) x4. Requires Baking. The combine does not fail.
98. Spawns "a Koka'Vor chieftain" (210236) in `postorms` on event_signal.
99. Loot "Storm Rider Blood" (29526) from "a Koka'Vor chieftain".
100. Loot "Drop of Pure Rain" (29904) from "A vann stav" (NPC 209018) in `bothunder`. Drop cache: 4% chance per kill.
101. Combine in Brew Barrel (19): "Powdered Sandstorm Pearl" (29520), "Storm Rider Blood" (29526), "Drop of Pure Rain" (29904). Produces "Hurricane Temper" (29533). Requires Brewing, trivial 135.
102. Combine in Forge (17): "Cleansed Breastplate" (15998), "Hurricane Temper" (29533). Produces "Tempered Breastplate" (15999). Requires Blacksmithing, trivial 229.
103. Combine in Forge (17): "Black Diamond of Nightmares" (29990), "Tempered Breastplate" (15999). Produces "Imbued Breastplate" (15985). Requires Blacksmithing 220. Trivial at 275.
104. poknowledge/"Aid Grimel", hand "Imbued Breastplate" (15985). Gives "Hardened Leather Signet" (16249).
105. poknowledge/"Aid Grimel", say "Skill In Brewing". Requires `pop_cod_final` ==1. Requires `pop_cod_final` set. Gives "Portable Drink Barrel" (17179).
106. Spawns "Sepsis Rat" (45113) in `qcat` on event_death.
107. Loot "Rat Ears" (13072) from "Sepsis Rat".
108. 2 alternative loot source(s) also yield Rat Ears (13072).
109. Loot "Spider Legs" (13417) from "A Large Yellow Recluse" (NPC 56052) in `steamfont`. Drop cache: 55% chance per kill.
110. Common item: Rice (16593). Listed in 30 zones.
111. Combine in "Portable Drink Barrel" (17179): "Rat Ears" (13072), "Spider Legs" (13417), "Rice" (16593), "Bottle" (16598). Produces "Gnomish Spirits" (13037) x2. Requires Brewing, trivial 102.
112. Combine in Brew Barrel (19): "Rat Ears" (13072), "Spider Legs" (13417), "Rice" (16593), "Bottle" (16598). Produces "Gnomish Spirits" (13037) x2. Requires Brewing, trivial 102.
113. Combine in "Toolbox" (17902): "Water Flask" (13006), "Gnomish Spirits" (13037). Produces "Firewater" (16881). Requires Tinkering, trivial 17.
114. Common item: Metal Fastening (16888). Listed in 14 zones.
115. Common item: Sharkskin Tubing (16891). Listed in 14 zones.
116. Common item: Lime Coated Meshing (16892). Listed in 10 zones.
117. Combine in "Toolbox" (17902): "Platemail Helm" (4001), "Aqualung" (16873), "Firewater" (16881), "Metal Fastening" (16888), "Sharkskin Tubing" (16891), "Lime Coated Meshing" (16892). Produces "Rebreather" (16889). Requires Tinkering, trivial 175.
118. Loot "Block of Permafrost" (20665) from "Lady Vox" in `permafrost`.
119. Loot "Block of Permafrost" (20665) from "An Ice Giant" in `permafrost`.
120. Common item: Keg of Vox Tail Ale (20664). Listed in 13 zones.
121. oceanoftears/"Denken Strongpick", hand "Rebreather" (16889) + "Keg of Vox Tail Ale" (20664) + "Block of Permafrost" (20665). Gives "Ancient Sword Blade" (20667).
122. Loot "Ancient Blade" (20670) from "Queen Velazul Di'zok" in `chardok`.
123. Ground spawn of "Unjeweled Dragon Head Hilt" (20668) in `lakerathe`.
124. Loot "Apothic Crown" (1239) from "Magi P'Tasa" (NPC 186157) in `hateplaneb`. Drop cache: 19.16% chance per kill.
125. poknowledge/"Arch Mage Deidus", hand "Apothic Crown" (1239). Gives "Diamond" (10037).
126. Loot "Scroll of the Ox" (49007) from "A Sturdy Chest" in `stillmoona`.
127. Loot "Scroll of the Boar" (49008) from "A Sturdy Chest" in `stillmoona`.
128. Loot "Scroll of the Dragon" (49009) from "A Sturdy Chest" in `stillmoona`.
129. Loot "Scroll of the Tiger" (49010) from "A Sturdy Chest" in `stillmoona`.
130. Hand "Scroll of the Ox" (49007) + "Scroll of the Boar" (49008) + "Scroll of the Dragon" (49009) + "Scroll of the Tiger" (49010) to stillmoona/"The Keeper Of Strength". Spawns "A Spirit Keeper" (338169). Loot "Black Sapphire" (10036) from "A Spirit Keeper".
131. 43 alternative loot source(s) also yield Black Sapphire (10036).
132. Loot "Bayle List I" (18808) from "Mutt Rootlit" in `highpass`.
133. qrg/"Gerael Woodone", say "Deliver A Flask". Gives "Flask of Nitrates" (13945).
134. akanon/"Kimble Nogflop", hand "Flask of Nitrates" (13945). Gives "Regurgitonic" (12140).
135. qrg/"Mammoth", hand "Regurgitonic" (12140). Gives "Bayle List II" (18809).
136. Loot "Bayle List III" (18810) from "Dyllin Starsine" in `highpass`.
137. Loot "Bayle List III" (18810) from "Dyllin Starsine" in `highpasshold`.
138. southro/"Rathmana Allin", hand "Bayle List I" (18808) + "Bayle List II" (18809) + "Bayle List III" (18810). Gives "Translated Parchment" (18961).
139. highpass/"Stanos Herkanor", hand "Translated Parchment" (18961). Gives "Sealed Box" (28057).
140. Kill wakening/"A Tar Goo". Spawns "A Tar Goo" (119122).
141. Loot "Oily Goo Secretion" (11637) from "A Tar Goo".
142. 1 alternative loot source(s) also yield Oily Goo Secretion (11637).
143. bazaar/"Caerlyna", hand "Vale Sewing Kit" (92882). Gives "Vale Sewing Kit Token" (56884).
144. bazaar/"Caerlyna", hand "Vale Sewing Kit Token" (56884). Gives "Vale Sewing Kit" (92882).
145. Common item: Needle Mold (12019). Listed in 32 zones.
146. Common item: Thimble Mold (12057). Listed in 32 zones.
147. Combine in Forge (17): "Fine Steel Two Handed Sword" (5351), "Water Flask" (13006). Produces "Small Brick of High Quality Ore" (10468) x2, "Small Piece of High Quality Ore" (22229). Requires Blacksmithing, trivial 21.
148. Combine in Forge (17): "Smithing Chisel" (7052), "Small Brick of High Quality Ore" (10468). Hands back "Smithing Chisel" (7052). Produces "Small Piece of High Quality Ore" (22229) x2. Requires Blacksmithing, trivial 27.
149. 4 other recipes also produce Small Piece of High Quality Ore (22229).
150. Combine in Royal Qeynos Forge (40): "Small Piece of High Quality Ore" (22229), "Water Flask" (13006). Produces "High Quality Metal Bits" (22230). Requires Blacksmithing, trivial 20.
151. Combine in Vale Forge (49): "Needle Mold" (12019), "Thimble Mold" (12057), "Water Flask" (13006), "High Quality Metal Bits" (22230). Produces "Vale Sewing Kit" (92882). Requires Blacksmithing, trivial 162.
152. Loot "Crystalline Silk" (25306) from "A Crystal Grinder" (NPC 121089) in `crystal`. Drop cache: 100% chance per kill.
153. Combine in "Vale Sewing Kit" (92882): "Crystalline Silk" (25306). Produces "Crystalline Silk Mesh" (11636). Requires Tailoring, trivial 68.
154. skyshrine/"Iago Sabuela", hand "Crystalline Silk Mesh" (11636) + "Oily Goo Secretion" (11637). Gives "Empty Artifact Container" (17167).
155. Loot "Crystal Dragon Eye" (11638) from "An Ice Paw Sorcerer" in `velketor`.
156. Loot "Golden Dragon Claw" (11639) from "A Chetari Runemage" in `necropolis`.
157. Loot "Platinum Dragon Scale" (11640) from "A Siren Sorceress" in `sirens`.
158. Loot "Rodrick's Head" (1045) from "Rodrick Tardok".
159. Loot "Rodrick's Head" (1045) from "Rodrick Tardok" in `eastwastes`.
160. Spawns "Poxbreath Yellowfang" (116566) in `eastwastes` on event_signal.
161. Loot "Note from Kromrif" (18084) from "Poxbreath Yellowfang".
162. Spawns "Scarbrow Ga'Hruk" (116568) in `eastwastes` on event_signal.
163. Loot "Head of Scarbrow" (30141) from "Scarbrow Ga'Hruk".
164. Say "Help" to eastwastes/"Tain Hammerfrost".
165. Spawns "Ghrek Squatnot" (116560).
166. Loot "Frozen Elixir" (30138) from "Ghrek Squatnot".
167. eastwastes/"Tain Hammerfrost", hand "Frozen Elixir" (30138). Gives "Coldain Smithing Hammer" (30140).
168. Spawns "Rabid Tundra Kodiak" (116545) in `eastwastes` on event_waypoint_arrive.
169. Loot "Rabid Kodiak Skin" (30266) from "Rabid Tundra Kodiak".
170. eastwastes/"Boridain Glacierbane", hand "Rabid Kodiak Skin" (30266). Gives "Broken Axe" (30267).
171. iceclad/"A Lost Pirate", say "I Will Find The Parts". Gives "Map Binding" (17053).
172. Loot "First part of an Iceclad Map" (30043) from "Dire Wolf Stalker" in `iceclad`.
173. Loot "Second part of an Iceclad Map" (30044) from "Stormfeather" in `iceclad`.
174. Loot "Second part of an Iceclad Map" (30044) from "The Fabled Stormfeather".
175. greatdivide/"Bloody Gnome Captive", say "Map". Gives "Third part of an Iceclad Map" (30045).
176. Loot "Fourth part of an Iceclad Map" (30073) from "Lodizal" in `iceclad`.
177. Loot "Fourth part of an Iceclad Map" (30073) from "The Fabled Lodizal".
178. Combine in "Map Binding" (17053): "First part of an Iceclad Map" (30043), "Second part of an Iceclad Map" (30044), "Third part of an Iceclad Map" (30045), "Fourth part of an Iceclad Map" (30073). Produces "Pieces of the Iceclad Map" (30046). The combine does not fail.
179. Hand "Pieces of the Iceclad Map" (30046) to iceclad/"A Lost Pirate". Spawns "Rabid Snow Cougar Does Not Exist Using Regular For Now" (116008). Loot "High Quality Cougarskin" (30030) from "Rabid Snow Cougar Does Not Exist Using Regular For Now".
180. Loot "High Quality Tundra Kodiak Pelt" (30077) from "A Tundra Kodiak" (NPC 116044) in `eastwastes`. Drop cache: 3.91% chance per kill.
181. Combine in "Vale Sewing Kit" (92882): "High Quality Cougarskin" (30030), "High Quality Tundra Kodiak Pelt" (30077). Produces "Coldain Hunting Blanket" (30135). Requires Tailoring, trivial 41.
182. eastwastes/"Garadain Glacierbane", hand "Coldain Hunting Blanket" (30135). Gives "Copper Coldain Insignia Ring" (30131).
183. eastwastes/"Garadain Glacierbane", hand "Copper Coldain Insignia Ring" (30131) + "Broken Axe" (30267). Gives "Silver Coldain Insignia Ring" (30133).
184. Ground spawn of "Skinning Rock" (30062) in `eastwastes`.
185. Loot "Wooly Rhino Horn" (30088) from "A Wooly Rhino" (NPC 116033) in `eastwastes`. Drop cache: 20% chance per kill.
186. Loot "High Quality Walrus Hide" (30096) from "A Walrus" (NPC 116065) in `eastwastes`. Drop cache: 14.1% chance per kill.
187. Combine in Forge (17): "Skinning Rock" (30062), "Wooly Rhino Horn" (30088), "High Quality Walrus Hide" (30096). Produces "Coldain Hunting Knife" (30137). Requires Blacksmithing, trivial 41.
188. eastwastes/"Garadain Glacierbane", hand "Silver Coldain Insignia Ring" (30133) + "Coldain Hunting Knife" (30137). Gives "Gold Coldain Insignia Ring" (30132).
189. eastwastes/"Garadain Glacierbane", hand "Gold Coldain Insignia Ring" (30132) + "Coldain Smithing Hammer" (30140). Gives "Platinum Coldain Insignia Ring" (30134).
190. eastwastes/"Garadain Glacierbane", hand "Platinum Coldain Insignia Ring" (30134) + "Head of Scarbrow" (30141). Gives "Obsidian Coldain Insignia Ring" (30268).
191. eastwastes/"Garadain Glacierbane", hand "Rodrick's Head" (1045) + "Note from Kromrif" (18084) + "Obsidian Coldain Insignia Ring" (30268). Gives "Mithril Coldain Insignia Ring" (30162).
192. eastwastes/"Dobbin Crossaxe", hand "Mithril Coldain Insignia Ring" (30162). Gives "Note from Corbin" (1047).
193. eastwastes/"Garadain Glacierbane", hand "Note from Corbin" (1047). Gives "Adamantium Coldain Insignia Ring" (30163).
194. eastwastes/"Garadain Glacierbane", hand "Adamantium Coldain Insignia Ring" (30163). Gives "Marching Orders" (1093).
195. Hand "Marching Orders" (1093) to eastwastes/"Gloradin Coldheart". Spawns "Oracle of Ry'Gorr" (116006). Loot "Dragon Scripture Tablet" (11651) from "Oracle of Ry'Gorr".
196. 1 alternative loot source(s) also yield Dragon Scripture Tablet (11651).
197. Combine in "Empty Artifact Container" (17167): "Crystal Dragon Eye" (11638), "Golden Dragon Claw" (11639), "Platinum Dragon Scale" (11640), "Dragon Scripture Tablet" (11651). Produces "Sealed Box" (28057). The combine does not fail.
198. Hand "Sealed Box" (28057) to kithicor/"Adjutant D-Kan". Spawns "General V'ghera" (20205). Loot "General's Pouch" (28013) from "General V'ghera".
199. 6 alternative loot source(s) also yield General's Pouch (28013).
200. Loot "Fleshripper" (5411) from "Solusek kobold king" in `soldungb`.
201. Loot "Painbringer" (5410) from "Kobold Champion" in `soldungb`.
202. Loot "Mithril Two-Handed Sword" (5401) from "The Froglok King" in `gukbottom`.
203. Loot "Gigantic Zweihander" (5308) from "Karg IceBear" in `everfrost`.
204. qey2hh1/"Vilnius The Small", hand "Gigantic Zweihander" (5308) + "Mithril Two-Handed Sword" (5401) + "Painbringer" (5410) + "Fleshripper" (5411). Gives "Jagged Diamond Dagger" (7506).
205. Loot "Robe of the Ishva" (1357) from "Coercer Q'ioul" in `kithicor`.
206. Loot "Robe of the Ishva" (1357) from "Jinalis Andir" in `cauldron`.
207. Loot "Robe of the Ishva" (1357) from "The Ishva Mal" in `southkarana`.
208. Loot "Robe of the Kedge" (1253) from "Kubaria" (NPC 309002) in `chambersf`. Drop cache: 100% chance per kill.
209. Loot "Robe of the Oracle" (1354) from "Oracle of K'Arnon" in `oceanoftears`.
210. Loot "Robe of the Oracle" (1354) from "Oracle of K'Arnon" in `oot`.
211. Loot "Shining Metallic Robes" (1360) from "Yendar Starpyre" (NPC 56012) in `steamfont`. Drop cache: 100% chance per kill.
212. qey2hh1/"Vilnius The Small", hand "Robe of the Kedge" (1253) + "Robe of the Oracle" (1354) + "Robe of the Ishva" (1357) + "Shining Metallic Robes" (1360). Gives "Cazic Quill" (7505).
213. highpass/"Stanos Herkanor", hand "Cazic Quill" (7505) + "Jagged Diamond Dagger" (7506) + "General's Pouch" (28013). Gives "Ragebringer" (11057).
214. highpass/"Stanos Herkanor", say "Hail". Sets `Fatestealer` to `1`.
215. Unresolved cyclic prerequisite: `Fatestealer_gal` ==1.
216. Unresolved cyclic prerequisite: `Fatestealer_gal` ==1.
217. Unresolved cyclic prerequisite: `Fatestealer_mar` ==1.
218. Unresolved cyclic prerequisite: `Fatestealer_gal` ==1.
219. Unresolved cyclic prerequisite: `Fatestealer_mar` ==1.
220. Unresolved cyclic prerequisite: `Fatestealer_lyt` ==1.
221. Loot "Signed Agreement" (10246) from "Lythe Songbird" in `freeporteast`.
222. Loot "Signed Agreement" (10246) from "Lythe Songbird" in `freportw`.
223. overthere/"Inem R'Ker", hand "Signed Agreement" (10246). Sets `Fatestealer_lyt` to `1`.
224. Loot "Signed Agreement" (10239) from "Seana Marsinger" in `gfaydark`.
225. Loot "Signed Agreement" (52416) from "Stefan Marsinger" in `gfaydark`.
226. overthere/"Inem R'Ker", hand "Signed Agreement" (10239) + "Signed Agreement" (52416). Sets `Fatestealer_mar` to `1`.
227. Loot "Signed Agreement" (10243) from "Galdorin Visigothe" in `abysmal`.
228. overthere/"Inem R'Ker", hand "Signed Agreement" (10243). Sets `Fatestealer_gal` to `1`.
229. overthere/"Inem R'Ker", hand "Signed Agreement" (10243). Sets `Fatestealer_bard` to `1`.
230. Spawns "a Teir'Dal guardian" (186190) in `hateplaneb` on event death_complete:186114.
231. Loot "Stack of Pages" (52335) from "a Teir'Dal guardian".
232. 5 alternative loot source(s) also yield Stack of Pages (52335).
233. steamfont/"Yendar Starpyre", hand "Stack of Pages" (52335). Sets `Fatestealer_page` to `1`.
234. Spawns "A Furious Magma Guardian" (278123) in `soldungc` on event_signal.
235. Loot "Crystallized Shard of Doomfire" (21339) from "A Furious Magma Guardian".
236. 1 alternative loot source(s) also yield Crystallized Shard of Doomfire (21339).
237. Loot "Foul Doomfire Brimstone" (21342) from "A Pool Of Living Lava" (NPC 278043) in `soldungc`. Drop cache: 15.97% chance per kill.
238. Loot "Igneous Rock of Doomfire" (21340) from "Typhoeus" (NPC 278069) in `soldungc`. Drop cache: 35% chance per kill.
239. Loot "Pile of Doomfire Ash" (21341) from "a Taklasinai marauder" (NPC 278075) in `soldungc`. Drop cache: 35% chance per kill.
240. Hand "Crystallized Shard of Doomfire" (21339) + "Igneous Rock of Doomfire" (21340) + "Pile of Doomfire Ash" (21341) + "Foul Doomfire Brimstone" (21342) to soldungc/"The Firewatcher". Spawns "Culthor the Gatekeeper" (278005). Loot "Smoldering Embers of Solusek" (52346) from "Culthor the Gatekeeper".
241. nedaria/"Smith Dandi", hand "Smoldering Embers of Solusek" (52346). Sets `Fatestealer_forge` to `1`.
242. Spawns "a Teir'Dal guardian" (186190) in `hateplaneb` on event death_complete:186114.
243. Loot "Soulstone of Lanys" (52337) from "a Teir'Dal guardian".
244. 5 alternative loot source(s) also yield Soulstone of Lanys (52337).
245. nedaria/"Lirprin, Head Of Affairs", hand "Soulstone of Lanys" (52337). Requires `Fatestealer_bard` ==1. Requires `Fatestealer_page` ==1. Requires `Fatestealer_forge` ==1. Gives "Fatestealer" (52347).
246. nedaria/"Lirprin, Head Of Affairs", say "Hail". Sets `Fatestealer` to `3`.
247. Loot "Polished Bone Horn" (52349) from "A Baleful Stoneworker" (NPC 301023) in `bloodfields`. Drop cache: 4% chance per kill.
248. Loot "Brass Mouthpiece" (52350) from "An Ukun Fleshhound" (NPC 301009) in `bloodfields`. Drop cache: 3.67% chance per kill.
249. Loot "Bucket Mute" (52351) from "An Ukun Fleshhound" (NPC 301009) in `bloodfields`. Drop cache: 3.67% chance per kill.
250. Loot "Thin Leather Straps" (52352) from "An Ukun Fleshhound" (NPC 301009) in `bloodfields`. Drop cache: 3.67% chance per kill.
251. Hand "Polished Bone Horn" (52349) + "Brass Mouthpiece" (52350) + "Bucket Mute" (52351) + "Thin Leather Straps" (52352) to bloodfields/"Caller Donivin". Spawns "A Reclusive Girplan" (301033). Loot "Jacinth" (10053) from "A Reclusive Girplan".
252. 55 alternative loot source(s) also yield Jacinth (10053).
253. freeporteast/"Wenden Blackhammer", hand "Black Sapphire" (10036) + "Diamond" (10037) + "Jacinth" (10053) + "Unjeweled Dragon Head Hilt" (20668). Gives "Jeweled Dragon Head Hilt" (20671).
254. Ground spawn of "Severely Damaged Dragon Head Hilt" (20669) in `timorous`.
255. Loot "Giant Sized Monocle" (20678) from "A Mountain Giant Patriarch" in `dreadlands`.
256. frontiermtns/"Mentrax Mountainbone", hand "Giant Sized Monocle" (20678). Gives "Rejesiam Ore" (20666).
257. Loot "Ball of Everliving Golem" (20677) from "Dread" in `fearplane`.
258. Loot "Ball of Everliving Golem" (20677) from "Fright" in `fearplane`.
259. Loot "Ball of Everliving Golem" (20677) from "Terror" in `fearplane`.
260. freeporteast/"Wenden Blackhammer", hand "Rejesiam Ore" (20666) + "Severely Damaged Dragon Head Hilt" (20669) + "Ball of Everliving Golem" (20677). Gives "Finely Crafted Dragon Head Hilt" (20672).
261. Combine in "Red Scabbard" (17859): "Ancient Sword Blade" (20667), "Ancient Blade" (20670), "Jeweled Dragon Head Hilt" (20671), "Finely Crafted Dragon Head Hilt" (20672). Produces "Jagged Blade of War" (10908). The combine does not fail.
262. freeporteast/"Gartrog Smitehammer", hand "Jagged Blade of War" (10908) + "Red Scabbard" (17859). Gives "Red Scabbard" (17869).
263. freeporteast/"Gartrog Smitehammer", hand "Jagged Blade of War" (10908) + "Red Scabbard" (17859). Gives "Jagged Blade of War" (66175).
264. Combine in "Red Scabbard" (17869): "Jagged Blade of War" (66175). Produces "Blade of Tactics" (66176), "Blade of Strategy" (66177). Requires Pottery. The combine does not fail.

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
18. Say "Tm Devrak Death" to rujd/"Rujd".
19. Spawns "spawn chest with Heavy Orcish Prison Key" (245241).
20. Loot "Pod of Water" (13044) from "spawn chest with Heavy Orcish Prison Key".
21. 6 alternative loot source(s) also yield Pod of Water (13044).
22. Forage "Pod of Water" (13044) in `ruja`.
23. Forage "Pod of Water" (13044) in `uqua`.
24. Forage "Pod of Water" (13044) in `yxtta`.
25. Combine in Brew Barrel (19): "Bottle of Aged Bloodwine" (51163), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aged Bloodwine" (51164). Requires Brewing, trivial 255.
26. Combine in Brew Barrel (19): "Bottle of Aldo's Bitter Ale" (75805), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aldo's Bitter Ale" (75811). Requires Brewing, trivial 15.
27. 17 other recipes also produce Bottle (16598).
28. Combine in Brew Barrel (19): "Pod of Water" (13044), "Bottle" (16598). Produces "Water Flask" (13006). Requires Brewing, trivial 21.
29. northro/"Verrell Cogswin", hand "Water Flask" (13006). Sets `Green_Scale_Quest` to `1`.
30. northro/"Verrell Cogswin", hand "Red Dragon Scales" (11622). Sets `Green_Scale_Quest` to `2`.
31. northro/"Verrell Cogswin", say "Adhesive". Requires `Green_Scale_Quest` ==2. Requires `Green_Scale_Quest` set. Gives "Verrell's Box of Potions" (67387).
32. Loot "Fractured Centaur Hoof" (67388) from "Centaur Archer" in `southkarana`.
33. Loot "Fractured Centaur Hoof" (67388) from "Centaur Charger" in `southkarana`.
34. Loot "Fractured Centaur Hoof" (67388) from "Centaur Courser" in `southkarana`.
35. Loot "Fractured Centaur Hoof" (67388) from "Centaur Foal" in `southkarana`.
36. Loot "Fractured Centaur Hoof" (67388) from "Centaur Sheltie" in `southkarana`.
37. Loot "Fire Giant Embers" (67389) from "A Fire Giant Warlord" (NPC 278023) in `soldungc`. Drop cache: 28.35% chance per kill.
38. Loot "Jagged Permafrost Shards" (67390) from "The Chilling Terror" in `permafrost`.
39. Combine in Oven (15): "Fractured Centaur Hoof" (67388), "Fire Giant Embers" (67389), "Jagged Permafrost Shards" (67390). Produces "Glue Powder" (67391). Requires Baking. The combine does not fail.
40. Common item: Barley (16590). Listed in 28 zones.
41. Common item: Deep Fungus Mold (67393). Listed in 28 zones.
42. Common item: Distilled Spirits (67394). Listed in 28 zones.
43. Combine in Brew Barrel (19): "Barley" (16590), "Deep Fungus Mold" (67393), "Distilled Spirits" (67394). Produces "Deep Barley Brew" (67392). Requires Brewing, trivial 110.
44. northro/"Verrell Cogswin", say "Adhesive". Requires `Green_Scale_Quest` ==2. Requires `Green_Scale_Quest` set. Gives "Potion Vial" (67395).
45. Combine in "Verrell's Box of Potions" (67387): "Glue Powder" (67391), "Deep Barley Brew" (67392), "Potion Vial" (67395). Produces "Thick Adhesive" (67386). The combine does not fail.
46. northro/"Verrell Cogswin", hand "Thick Adhesive" (67386). Gives "Grey Scale Pieces" (67385).
47. northro/"Verrell Cogswin", hand "Thick Adhesive" (67386). Gives "Thick Adhesive" (67396).
48. Combine in "Verrell's Box of Potions" (67387): "Grey Scale Pieces" (67385), "Thick Adhesive" (67396). Produces "Grey Colored Scales" (67384). The combine does not fail.
49. northro/"Verrell Cogswin", hand "Grey Colored Scales" (67384). Gives "Green Dragon Scales" (11582).
50. eastkarana/"Tenal Redblade", hand "Green Dragon Scales" (11582) + "Red Dragon Scales" (11622) + "Totem of Fiery War" (20681). Gives "Mark of the Sword" (20683).
51. Loot "Hand of the Maestro" (20676) from "Hand of the Maestro" in `hateplane`.
52. Loot "Hand of the Maestro" (20676) from "Hand of the Maestro" in `hateplaneb`.
53. eastkarana/"Tenal Redblade", hand "Hand of the Maestro" (20676) + "Mark of the Sword" (20683). Gives "Tenal's note to Kargek" (20684).
54. Loot "Spiroc Wingblade" (20679) from "The Spiroc Lord" in `airplane`.
55. freeporteast/"Kargek Redblade", hand "Spiroc Wingblade" (20679) + "Tenal's note to Kargek" (20684). Gives "Red Scabbard" (17859).
56. Combine in "Red Scabbard" (17859): "Jagged Blade of War" (10908). Produces "Blade of Tactics" (10909), "Blade of Strategy" (10910). The combine does not fail.
57. Combine in "Red Scabbard" (17859): "Blade of Tactics" (10909), "Blade of Strategy" (10910). Produces "Jagged Blade of War" (10908). The combine does not fail.
58. lakerathe/"Triathalon Swim Goggles", say "Hail". Gives "Rebreather" (16889).
59. Combine in Forge (17): "Smithing Chisel" (7052), "Large Brick of Ore" (10502). Hands back "Smithing Chisel" (7052). Produces "Small Brick of Ore" (10501). Requires Blacksmithing, trivial 27.
60. Combine in Forge (17): "Small Piece of Ore" (10500), "Water Flask" (13006). Produces "Small Brick of Ore" (10501). Requires Blacksmithing, trivial 27.
61. 11 other recipes also produce Small Brick of Ore (10501).
62. Loot "Toolbox Mold" (12077) from "Shevra Kollintar" in `paineel`.
63. kaladimb/"Jeet", say "Collect The Gnome Profit". Gives "Scrubber Key" (12164).
64. akanon/"Clockwork Scrubber", hand "Scrubber Key" (12164). Gives "Gnome Take" (12167).
65. kaladimb/"Jeet", hand "Gnome Take" (12167). Gives "Small Piece of Ore" (10500).
66. Combine in Forge (17): "Small Piece of Ore" (10500), "Water Flask" (13006). Produces "Metal Bits" (16905) x2. Requires Blacksmithing, trivial 18.
67. Combine in Forge (17): "Small Brick of Ore" (10501), "Toolbox Mold" (12077), "Water Flask" (13006), "Metal Bits" (16905). Produces "Toolbox" (17902). Requires Blacksmithing, trivial 51.
68. Common item: Platemail Helm (4001). Listed in 15 zones.
69. Fish "Fresh Fish" (13019) in `zone 0`.
70. Forage "Fresh Fish" (13019) in `kedge`.
71. Common item: Metal Rod (16850). Listed in 14 zones.
72. Common item: Metal Twine (16857). Listed in 10 zones.
73. Common item: Gnomish Bolts (16861). Listed in 10 zones.
74. Common item: Silk Lined Steel Helm (16862). Listed in 9 zones.
75. Common item: Fine Coral Mesh (16890). Listed in 14 zones.
76. Combine in "Toolbox" (17902): "Fresh Fish" (13019), "Metal Rod" (16850), "Metal Twine" (16857), "Gnomish Bolts" (16861), "Silk Lined Steel Helm" (16862), "Fine Coral Mesh" (16890). Produces "Aqualung" (16873) x20. Requires Tinkering, trivial 148.
77. Summon "Black Diamond of Nightmares" (29990) by casting "Imbue Nightmare".
78. potranquility/"Elder Fuirstel", say "Hail". Sets `pop_cod_final` to `1`.
79. poknowledge/"Aid Grimel", say "Versed In The Art Of Smithing". Requires `pop_cod_final` ==1. Requires `pop_cod_final` set. Gives "Filthy Breastplate" (15984).
80. Combine in "Mixing Bowl" (17906): "Celestial Solvent" (9731), "Words of Acquisition (Beza)" (11866). Produces "Celestial Essence" (9650). Requires Baking, trivial 15. The combine does not fail.
81. Combine in "Mixing Bowl" (17906): "Celestial Solvent" (9731), "Words of Burnishing" (11862). Produces "Celestial Essence" (9650). Requires Baking, trivial 15. The combine does not fail.
82. 67 other recipes also produce Celestial Essence (9650).
83. Common item: Jar of Acid (22133). Listed in 15 zones.
84. Combine in Brew Barrel (19): "Celestial Essence" (9650), "Jar of Acid" (22133). Produces "Acid Wash" (15987). Requires Brewing, trivial 151.
85. Combine in Forge (17): "Filthy Breastplate" (15984), "Acid Wash" (15987). Produces "Cleansed Breastplate" (15998). Requires Blacksmithing, trivial 227.
86. Common item: Mortar and Pestle (17904). Listed in 12 zones.
87. Loot "Sandstorm Pearl" (29909) from "Rorek Steelthorn" (NPC 209081) in `bothunder`. Drop cache: 5.33% chance per kill.
88. Combine in "Mortar and Pestle" (17904): "Sandstorm Pearl" (29909). Produces "Powdered Sandstorm Pearl" (29520) x4. Requires Make Poison, trivial 255.
89. Common item: Firing Sheet (16906). Listed in 34 zones.
90. Combine in Pottery Wheel (21): "Water Flask" (13006), "Block of Clay" (16901). Produces "Small Block of Clay" (16900) x3. Requires Pottery, trivial 21.
91. Combine in Pottery Wheel (21): "Small Block of Clay" (16900), "Water Flask" (13006). Produces "Block of Clay" (16901). Requires Pottery, trivial 21.
92. Combine in Pottery Wheel (21): "Water Flask" (13006), "Large Block of Clay" (16902). Produces "Block of Clay" (16901) x2. Requires Pottery, trivial 21.
93. Combine in Pottery Wheel (21): "Block of Clay" (16901), "Water Flask" (13006). Produces "Large Block of Clay" (16902). Requires Pottery, trivial 21.
94. Common item: Large Bowl Sketch (16963). Listed in 29 zones.
95. Combine in Pottery Wheel (21): "Large Block of Clay" (16902), "Water Flask" (13006), "Large Bowl Sketch" (16963). Produces "Unfired Mixing Bowl" (16930). Requires Pottery, trivial 128.
96. Combine in Kiln (22): "Firing Sheet" (16906), "Unfired Mixing Bowl" (16930). Produces "Mixing Bowl" (17906). Requires Pottery, trivial 15.
97. Combine in "Mixing Bowl" (17906): "Sandstorm Pearl" (29909). Produces "Powdered Sandstorm Pearl" (29520) x4. Requires Baking. The combine does not fail.
98. Spawns "a Koka'Vor chieftain" (210236) in `postorms` on event_signal.
99. Loot "Storm Rider Blood" (29526) from "a Koka'Vor chieftain".
100. Loot "Drop of Pure Rain" (29904) from "A vann stav" (NPC 209018) in `bothunder`. Drop cache: 4% chance per kill.
101. Combine in Brew Barrel (19): "Powdered Sandstorm Pearl" (29520), "Storm Rider Blood" (29526), "Drop of Pure Rain" (29904). Produces "Hurricane Temper" (29533). Requires Brewing, trivial 135.
102. Combine in Forge (17): "Cleansed Breastplate" (15998), "Hurricane Temper" (29533). Produces "Tempered Breastplate" (15999). Requires Blacksmithing, trivial 229.
103. Combine in Forge (17): "Black Diamond of Nightmares" (29990), "Tempered Breastplate" (15999). Produces "Imbued Breastplate" (15985). Requires Blacksmithing 220. Trivial at 275.
104. poknowledge/"Aid Grimel", hand "Imbued Breastplate" (15985). Gives "Hardened Leather Signet" (16249).
105. poknowledge/"Aid Grimel", say "Skill In Brewing". Requires `pop_cod_final` ==1. Requires `pop_cod_final` set. Gives "Portable Drink Barrel" (17179).
106. Spawns "Sepsis Rat" (45113) in `qcat` on event_death.
107. Loot "Rat Ears" (13072) from "Sepsis Rat".
108. 2 alternative loot source(s) also yield Rat Ears (13072).
109. Loot "Spider Legs" (13417) from "A Large Yellow Recluse" (NPC 56052) in `steamfont`. Drop cache: 55% chance per kill.
110. Common item: Rice (16593). Listed in 30 zones.
111. Combine in "Portable Drink Barrel" (17179): "Rat Ears" (13072), "Spider Legs" (13417), "Rice" (16593), "Bottle" (16598). Produces "Gnomish Spirits" (13037) x2. Requires Brewing, trivial 102.
112. Combine in Brew Barrel (19): "Rat Ears" (13072), "Spider Legs" (13417), "Rice" (16593), "Bottle" (16598). Produces "Gnomish Spirits" (13037) x2. Requires Brewing, trivial 102.
113. Combine in "Toolbox" (17902): "Water Flask" (13006), "Gnomish Spirits" (13037). Produces "Firewater" (16881). Requires Tinkering, trivial 17.
114. Common item: Metal Fastening (16888). Listed in 14 zones.
115. Common item: Sharkskin Tubing (16891). Listed in 14 zones.
116. Common item: Lime Coated Meshing (16892). Listed in 10 zones.
117. Combine in "Toolbox" (17902): "Platemail Helm" (4001), "Aqualung" (16873), "Firewater" (16881), "Metal Fastening" (16888), "Sharkskin Tubing" (16891), "Lime Coated Meshing" (16892). Produces "Rebreather" (16889). Requires Tinkering, trivial 175.
118. Loot "Block of Permafrost" (20665) from "Lady Vox" in `permafrost`.
119. Loot "Block of Permafrost" (20665) from "An Ice Giant" in `permafrost`.
120. Common item: Keg of Vox Tail Ale (20664). Listed in 13 zones.
121. oceanoftears/"Denken Strongpick", hand "Rebreather" (16889) + "Keg of Vox Tail Ale" (20664) + "Block of Permafrost" (20665). Gives "Ancient Sword Blade" (20667).
122. Loot "Ancient Blade" (20670) from "Queen Velazul Di'zok" in `chardok`.
123. Ground spawn of "Unjeweled Dragon Head Hilt" (20668) in `lakerathe`.
124. Loot "Apothic Crown" (1239) from "Magi P'Tasa" (NPC 186157) in `hateplaneb`. Drop cache: 19.16% chance per kill.
125. poknowledge/"Arch Mage Deidus", hand "Apothic Crown" (1239). Gives "Diamond" (10037).
126. Loot "Scroll of the Ox" (49007) from "A Sturdy Chest" in `stillmoona`.
127. Loot "Scroll of the Boar" (49008) from "A Sturdy Chest" in `stillmoona`.
128. Loot "Scroll of the Dragon" (49009) from "A Sturdy Chest" in `stillmoona`.
129. Loot "Scroll of the Tiger" (49010) from "A Sturdy Chest" in `stillmoona`.
130. Hand "Scroll of the Ox" (49007) + "Scroll of the Boar" (49008) + "Scroll of the Dragon" (49009) + "Scroll of the Tiger" (49010) to stillmoona/"The Keeper Of Strength". Spawns "A Spirit Keeper" (338169). Loot "Black Sapphire" (10036) from "A Spirit Keeper".
131. 43 alternative loot source(s) also yield Black Sapphire (10036).
132. Loot "Bayle List I" (18808) from "Mutt Rootlit" in `highpass`.
133. qrg/"Gerael Woodone", say "Deliver A Flask". Gives "Flask of Nitrates" (13945).
134. akanon/"Kimble Nogflop", hand "Flask of Nitrates" (13945). Gives "Regurgitonic" (12140).
135. qrg/"Mammoth", hand "Regurgitonic" (12140). Gives "Bayle List II" (18809).
136. Loot "Bayle List III" (18810) from "Dyllin Starsine" in `highpass`.
137. Loot "Bayle List III" (18810) from "Dyllin Starsine" in `highpasshold`.
138. southro/"Rathmana Allin", hand "Bayle List I" (18808) + "Bayle List II" (18809) + "Bayle List III" (18810). Gives "Translated Parchment" (18961).
139. highpass/"Stanos Herkanor", hand "Translated Parchment" (18961). Gives "Sealed Box" (28057).
140. Kill wakening/"A Tar Goo". Spawns "A Tar Goo" (119122).
141. Loot "Oily Goo Secretion" (11637) from "A Tar Goo".
142. 1 alternative loot source(s) also yield Oily Goo Secretion (11637).
143. bazaar/"Caerlyna", hand "Vale Sewing Kit" (92882). Gives "Vale Sewing Kit Token" (56884).
144. bazaar/"Caerlyna", hand "Vale Sewing Kit Token" (56884). Gives "Vale Sewing Kit" (92882).
145. Common item: Needle Mold (12019). Listed in 32 zones.
146. Common item: Thimble Mold (12057). Listed in 32 zones.
147. Combine in Forge (17): "Fine Steel Two Handed Sword" (5351), "Water Flask" (13006). Produces "Small Brick of High Quality Ore" (10468) x2, "Small Piece of High Quality Ore" (22229). Requires Blacksmithing, trivial 21.
148. Combine in Forge (17): "Smithing Chisel" (7052), "Small Brick of High Quality Ore" (10468). Hands back "Smithing Chisel" (7052). Produces "Small Piece of High Quality Ore" (22229) x2. Requires Blacksmithing, trivial 27.
149. 4 other recipes also produce Small Piece of High Quality Ore (22229).
150. Combine in Royal Qeynos Forge (40): "Small Piece of High Quality Ore" (22229), "Water Flask" (13006). Produces "High Quality Metal Bits" (22230). Requires Blacksmithing, trivial 20.
151. Combine in Vale Forge (49): "Needle Mold" (12019), "Thimble Mold" (12057), "Water Flask" (13006), "High Quality Metal Bits" (22230). Produces "Vale Sewing Kit" (92882). Requires Blacksmithing, trivial 162.
152. Loot "Crystalline Silk" (25306) from "A Crystal Grinder" (NPC 121089) in `crystal`. Drop cache: 100% chance per kill.
153. Combine in "Vale Sewing Kit" (92882): "Crystalline Silk" (25306). Produces "Crystalline Silk Mesh" (11636). Requires Tailoring, trivial 68.
154. skyshrine/"Iago Sabuela", hand "Crystalline Silk Mesh" (11636) + "Oily Goo Secretion" (11637). Gives "Empty Artifact Container" (17167).
155. Loot "Crystal Dragon Eye" (11638) from "An Ice Paw Sorcerer" in `velketor`.
156. Loot "Golden Dragon Claw" (11639) from "A Chetari Runemage" in `necropolis`.
157. Loot "Platinum Dragon Scale" (11640) from "A Siren Sorceress" in `sirens`.
158. Loot "Rodrick's Head" (1045) from "Rodrick Tardok".
159. Loot "Rodrick's Head" (1045) from "Rodrick Tardok" in `eastwastes`.
160. Spawns "Poxbreath Yellowfang" (116566) in `eastwastes` on event_signal.
161. Loot "Note from Kromrif" (18084) from "Poxbreath Yellowfang".
162. Spawns "Scarbrow Ga'Hruk" (116568) in `eastwastes` on event_signal.
163. Loot "Head of Scarbrow" (30141) from "Scarbrow Ga'Hruk".
164. Say "Help" to eastwastes/"Tain Hammerfrost".
165. Spawns "Ghrek Squatnot" (116560).
166. Loot "Frozen Elixir" (30138) from "Ghrek Squatnot".
167. eastwastes/"Tain Hammerfrost", hand "Frozen Elixir" (30138). Gives "Coldain Smithing Hammer" (30140).
168. Spawns "Rabid Tundra Kodiak" (116545) in `eastwastes` on event_waypoint_arrive.
169. Loot "Rabid Kodiak Skin" (30266) from "Rabid Tundra Kodiak".
170. eastwastes/"Boridain Glacierbane", hand "Rabid Kodiak Skin" (30266). Gives "Broken Axe" (30267).
171. iceclad/"A Lost Pirate", say "I Will Find The Parts". Gives "Map Binding" (17053).
172. Loot "First part of an Iceclad Map" (30043) from "Dire Wolf Stalker" in `iceclad`.
173. Loot "Second part of an Iceclad Map" (30044) from "Stormfeather" in `iceclad`.
174. Loot "Second part of an Iceclad Map" (30044) from "The Fabled Stormfeather".
175. greatdivide/"Bloody Gnome Captive", say "Map". Gives "Third part of an Iceclad Map" (30045).
176. Loot "Fourth part of an Iceclad Map" (30073) from "Lodizal" in `iceclad`.
177. Loot "Fourth part of an Iceclad Map" (30073) from "The Fabled Lodizal".
178. Combine in "Map Binding" (17053): "First part of an Iceclad Map" (30043), "Second part of an Iceclad Map" (30044), "Third part of an Iceclad Map" (30045), "Fourth part of an Iceclad Map" (30073). Produces "Pieces of the Iceclad Map" (30046). The combine does not fail.
179. Hand "Pieces of the Iceclad Map" (30046) to iceclad/"A Lost Pirate". Spawns "Rabid Snow Cougar Does Not Exist Using Regular For Now" (116008). Loot "High Quality Cougarskin" (30030) from "Rabid Snow Cougar Does Not Exist Using Regular For Now".
180. Loot "High Quality Tundra Kodiak Pelt" (30077) from "A Tundra Kodiak" (NPC 116044) in `eastwastes`. Drop cache: 3.91% chance per kill.
181. Combine in "Vale Sewing Kit" (92882): "High Quality Cougarskin" (30030), "High Quality Tundra Kodiak Pelt" (30077). Produces "Coldain Hunting Blanket" (30135). Requires Tailoring, trivial 41.
182. eastwastes/"Garadain Glacierbane", hand "Coldain Hunting Blanket" (30135). Gives "Copper Coldain Insignia Ring" (30131).
183. eastwastes/"Garadain Glacierbane", hand "Copper Coldain Insignia Ring" (30131) + "Broken Axe" (30267). Gives "Silver Coldain Insignia Ring" (30133).
184. Ground spawn of "Skinning Rock" (30062) in `eastwastes`.
185. Loot "Wooly Rhino Horn" (30088) from "A Wooly Rhino" (NPC 116033) in `eastwastes`. Drop cache: 20% chance per kill.
186. Loot "High Quality Walrus Hide" (30096) from "A Walrus" (NPC 116065) in `eastwastes`. Drop cache: 14.1% chance per kill.
187. Combine in Forge (17): "Skinning Rock" (30062), "Wooly Rhino Horn" (30088), "High Quality Walrus Hide" (30096). Produces "Coldain Hunting Knife" (30137). Requires Blacksmithing, trivial 41.
188. eastwastes/"Garadain Glacierbane", hand "Silver Coldain Insignia Ring" (30133) + "Coldain Hunting Knife" (30137). Gives "Gold Coldain Insignia Ring" (30132).
189. eastwastes/"Garadain Glacierbane", hand "Gold Coldain Insignia Ring" (30132) + "Coldain Smithing Hammer" (30140). Gives "Platinum Coldain Insignia Ring" (30134).
190. eastwastes/"Garadain Glacierbane", hand "Platinum Coldain Insignia Ring" (30134) + "Head of Scarbrow" (30141). Gives "Obsidian Coldain Insignia Ring" (30268).
191. eastwastes/"Garadain Glacierbane", hand "Rodrick's Head" (1045) + "Note from Kromrif" (18084) + "Obsidian Coldain Insignia Ring" (30268). Gives "Mithril Coldain Insignia Ring" (30162).
192. eastwastes/"Dobbin Crossaxe", hand "Mithril Coldain Insignia Ring" (30162). Gives "Note from Corbin" (1047).
193. eastwastes/"Garadain Glacierbane", hand "Note from Corbin" (1047). Gives "Adamantium Coldain Insignia Ring" (30163).
194. eastwastes/"Garadain Glacierbane", hand "Adamantium Coldain Insignia Ring" (30163). Gives "Marching Orders" (1093).
195. Hand "Marching Orders" (1093) to eastwastes/"Gloradin Coldheart". Spawns "Oracle of Ry'Gorr" (116006). Loot "Dragon Scripture Tablet" (11651) from "Oracle of Ry'Gorr".
196. 1 alternative loot source(s) also yield Dragon Scripture Tablet (11651).
197. Combine in "Empty Artifact Container" (17167): "Crystal Dragon Eye" (11638), "Golden Dragon Claw" (11639), "Platinum Dragon Scale" (11640), "Dragon Scripture Tablet" (11651). Produces "Sealed Box" (28057). The combine does not fail.
198. Hand "Sealed Box" (28057) to kithicor/"Adjutant D-Kan". Spawns "General V'ghera" (20205). Loot "General's Pouch" (28013) from "General V'ghera".
199. 6 alternative loot source(s) also yield General's Pouch (28013).
200. Loot "Fleshripper" (5411) from "Solusek kobold king" in `soldungb`.
201. Loot "Painbringer" (5410) from "Kobold Champion" in `soldungb`.
202. Loot "Mithril Two-Handed Sword" (5401) from "The Froglok King" in `gukbottom`.
203. Loot "Gigantic Zweihander" (5308) from "Karg IceBear" in `everfrost`.
204. qey2hh1/"Vilnius The Small", hand "Gigantic Zweihander" (5308) + "Mithril Two-Handed Sword" (5401) + "Painbringer" (5410) + "Fleshripper" (5411). Gives "Jagged Diamond Dagger" (7506).
205. Loot "Robe of the Ishva" (1357) from "Coercer Q'ioul" in `kithicor`.
206. Loot "Robe of the Ishva" (1357) from "Jinalis Andir" in `cauldron`.
207. Loot "Robe of the Ishva" (1357) from "The Ishva Mal" in `southkarana`.
208. Loot "Robe of the Kedge" (1253) from "Kubaria" (NPC 309002) in `chambersf`. Drop cache: 100% chance per kill.
209. Loot "Robe of the Oracle" (1354) from "Oracle of K'Arnon" in `oceanoftears`.
210. Loot "Robe of the Oracle" (1354) from "Oracle of K'Arnon" in `oot`.
211. Loot "Shining Metallic Robes" (1360) from "Yendar Starpyre" (NPC 56012) in `steamfont`. Drop cache: 100% chance per kill.
212. qey2hh1/"Vilnius The Small", hand "Robe of the Kedge" (1253) + "Robe of the Oracle" (1354) + "Robe of the Ishva" (1357) + "Shining Metallic Robes" (1360). Gives "Cazic Quill" (7505).
213. highpass/"Stanos Herkanor", hand "Cazic Quill" (7505) + "Jagged Diamond Dagger" (7506) + "General's Pouch" (28013). Gives "Ragebringer" (11057).
214. highpass/"Stanos Herkanor", say "Hail". Sets `Fatestealer` to `1`.
215. Unresolved cyclic prerequisite: `Fatestealer_gal` ==1.
216. Unresolved cyclic prerequisite: `Fatestealer_gal` ==1.
217. Unresolved cyclic prerequisite: `Fatestealer_mar` ==1.
218. Unresolved cyclic prerequisite: `Fatestealer_gal` ==1.
219. Unresolved cyclic prerequisite: `Fatestealer_mar` ==1.
220. Unresolved cyclic prerequisite: `Fatestealer_lyt` ==1.
221. Loot "Signed Agreement" (10246) from "Lythe Songbird" in `freeporteast`.
222. Loot "Signed Agreement" (10246) from "Lythe Songbird" in `freportw`.
223. overthere/"Inem R'Ker", hand "Signed Agreement" (10246). Sets `Fatestealer_lyt` to `1`.
224. Loot "Signed Agreement" (10239) from "Seana Marsinger" in `gfaydark`.
225. Loot "Signed Agreement" (52416) from "Stefan Marsinger" in `gfaydark`.
226. overthere/"Inem R'Ker", hand "Signed Agreement" (10239) + "Signed Agreement" (52416). Sets `Fatestealer_mar` to `1`.
227. Loot "Signed Agreement" (10243) from "Galdorin Visigothe" in `abysmal`.
228. overthere/"Inem R'Ker", hand "Signed Agreement" (10243). Sets `Fatestealer_gal` to `1`.
229. overthere/"Inem R'Ker", hand "Signed Agreement" (10243). Sets `Fatestealer_bard` to `1`.
230. Spawns "a Teir'Dal guardian" (186190) in `hateplaneb` on event death_complete:186114.
231. Loot "Stack of Pages" (52335) from "a Teir'Dal guardian".
232. 5 alternative loot source(s) also yield Stack of Pages (52335).
233. steamfont/"Yendar Starpyre", hand "Stack of Pages" (52335). Sets `Fatestealer_page` to `1`.
234. Spawns "A Furious Magma Guardian" (278123) in `soldungc` on event_signal.
235. Loot "Crystallized Shard of Doomfire" (21339) from "A Furious Magma Guardian".
236. 1 alternative loot source(s) also yield Crystallized Shard of Doomfire (21339).
237. Loot "Foul Doomfire Brimstone" (21342) from "A Pool Of Living Lava" (NPC 278043) in `soldungc`. Drop cache: 15.97% chance per kill.
238. Loot "Igneous Rock of Doomfire" (21340) from "Typhoeus" (NPC 278069) in `soldungc`. Drop cache: 35% chance per kill.
239. Loot "Pile of Doomfire Ash" (21341) from "a Taklasinai marauder" (NPC 278075) in `soldungc`. Drop cache: 35% chance per kill.
240. Hand "Crystallized Shard of Doomfire" (21339) + "Igneous Rock of Doomfire" (21340) + "Pile of Doomfire Ash" (21341) + "Foul Doomfire Brimstone" (21342) to soldungc/"The Firewatcher". Spawns "Culthor the Gatekeeper" (278005). Loot "Smoldering Embers of Solusek" (52346) from "Culthor the Gatekeeper".
241. nedaria/"Smith Dandi", hand "Smoldering Embers of Solusek" (52346). Sets `Fatestealer_forge` to `1`.
242. Spawns "a Teir'Dal guardian" (186190) in `hateplaneb` on event death_complete:186114.
243. Loot "Soulstone of Lanys" (52337) from "a Teir'Dal guardian".
244. 5 alternative loot source(s) also yield Soulstone of Lanys (52337).
245. nedaria/"Lirprin, Head Of Affairs", hand "Soulstone of Lanys" (52337). Requires `Fatestealer_bard` ==1. Requires `Fatestealer_page` ==1. Requires `Fatestealer_forge` ==1. Gives "Fatestealer" (52347).
246. nedaria/"Lirprin, Head Of Affairs", say "Hail". Sets `Fatestealer` to `3`.
247. Loot "Polished Bone Horn" (52349) from "A Baleful Stoneworker" (NPC 301023) in `bloodfields`. Drop cache: 4% chance per kill.
248. Loot "Brass Mouthpiece" (52350) from "An Ukun Fleshhound" (NPC 301009) in `bloodfields`. Drop cache: 3.67% chance per kill.
249. Loot "Bucket Mute" (52351) from "An Ukun Fleshhound" (NPC 301009) in `bloodfields`. Drop cache: 3.67% chance per kill.
250. Loot "Thin Leather Straps" (52352) from "An Ukun Fleshhound" (NPC 301009) in `bloodfields`. Drop cache: 3.67% chance per kill.
251. Hand "Polished Bone Horn" (52349) + "Brass Mouthpiece" (52350) + "Bucket Mute" (52351) + "Thin Leather Straps" (52352) to bloodfields/"Caller Donivin". Spawns "A Reclusive Girplan" (301033). Loot "Jacinth" (10053) from "A Reclusive Girplan".
252. 55 alternative loot source(s) also yield Jacinth (10053).
253. freeporteast/"Wenden Blackhammer", hand "Black Sapphire" (10036) + "Diamond" (10037) + "Jacinth" (10053) + "Unjeweled Dragon Head Hilt" (20668). Gives "Jeweled Dragon Head Hilt" (20671).
254. Ground spawn of "Severely Damaged Dragon Head Hilt" (20669) in `timorous`.
255. Loot "Giant Sized Monocle" (20678) from "A Mountain Giant Patriarch" in `dreadlands`.
256. frontiermtns/"Mentrax Mountainbone", hand "Giant Sized Monocle" (20678). Gives "Rejesiam Ore" (20666).
257. Loot "Ball of Everliving Golem" (20677) from "Dread" in `fearplane`.
258. Loot "Ball of Everliving Golem" (20677) from "Fright" in `fearplane`.
259. Loot "Ball of Everliving Golem" (20677) from "Terror" in `fearplane`.
260. freeporteast/"Wenden Blackhammer", hand "Rejesiam Ore" (20666) + "Severely Damaged Dragon Head Hilt" (20669) + "Ball of Everliving Golem" (20677). Gives "Finely Crafted Dragon Head Hilt" (20672).
261. Combine in "Red Scabbard" (17859): "Ancient Sword Blade" (20667), "Ancient Blade" (20670), "Jeweled Dragon Head Hilt" (20671), "Finely Crafted Dragon Head Hilt" (20672). Produces "Jagged Blade of War" (10908). The combine does not fail.
262. freeporteast/"Gartrog Smitehammer", hand "Jagged Blade of War" (10908) + "Red Scabbard" (17859). Gives "Red Scabbard" (17869).
263. freeporteast/"Gartrog Smitehammer", hand "Jagged Blade of War" (10908) + "Red Scabbard" (17859). Gives "Jagged Blade of War" (66175).
264. Combine in "Red Scabbard" (17869): "Jagged Blade of War" (66175). Produces "Blade of Tactics" (66176), "Blade of Strategy" (66177). Requires Pottery. The combine does not fail.

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
18. Say "Tm Devrak Death" to rujd/"Rujd".
19. Spawns "spawn chest with Heavy Orcish Prison Key" (245241).
20. Loot "Pod of Water" (13044) from "spawn chest with Heavy Orcish Prison Key".
21. 6 alternative loot source(s) also yield Pod of Water (13044).
22. Forage "Pod of Water" (13044) in `ruja`.
23. Forage "Pod of Water" (13044) in `uqua`.
24. Forage "Pod of Water" (13044) in `yxtta`.
25. Combine in Brew Barrel (19): "Bottle of Aged Bloodwine" (51163), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aged Bloodwine" (51164). Requires Brewing, trivial 255.
26. Combine in Brew Barrel (19): "Bottle of Aldo's Bitter Ale" (75805), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aldo's Bitter Ale" (75811). Requires Brewing, trivial 15.
27. 17 other recipes also produce Bottle (16598).
28. Combine in Brew Barrel (19): "Pod of Water" (13044), "Bottle" (16598). Produces "Water Flask" (13006). Requires Brewing, trivial 21.
29. northro/"Verrell Cogswin", hand "Water Flask" (13006). Sets `Green_Scale_Quest` to `1`.
30. northro/"Verrell Cogswin", hand "Red Dragon Scales" (11622). Sets `Green_Scale_Quest` to `2`.
31. northro/"Verrell Cogswin", say "Adhesive". Requires `Green_Scale_Quest` ==2. Requires `Green_Scale_Quest` set. Gives "Verrell's Box of Potions" (67387).
32. Loot "Fractured Centaur Hoof" (67388) from "Centaur Archer" in `southkarana`.
33. Loot "Fractured Centaur Hoof" (67388) from "Centaur Charger" in `southkarana`.
34. Loot "Fractured Centaur Hoof" (67388) from "Centaur Courser" in `southkarana`.
35. Loot "Fractured Centaur Hoof" (67388) from "Centaur Foal" in `southkarana`.
36. Loot "Fractured Centaur Hoof" (67388) from "Centaur Sheltie" in `southkarana`.
37. Loot "Fire Giant Embers" (67389) from "A Fire Giant Warlord" (NPC 278023) in `soldungc`. Drop cache: 28.35% chance per kill.
38. Loot "Jagged Permafrost Shards" (67390) from "The Chilling Terror" in `permafrost`.
39. Combine in Oven (15): "Fractured Centaur Hoof" (67388), "Fire Giant Embers" (67389), "Jagged Permafrost Shards" (67390). Produces "Glue Powder" (67391). Requires Baking. The combine does not fail.
40. Common item: Barley (16590). Listed in 28 zones.
41. Common item: Deep Fungus Mold (67393). Listed in 28 zones.
42. Common item: Distilled Spirits (67394). Listed in 28 zones.
43. Combine in Brew Barrel (19): "Barley" (16590), "Deep Fungus Mold" (67393), "Distilled Spirits" (67394). Produces "Deep Barley Brew" (67392). Requires Brewing, trivial 110.
44. northro/"Verrell Cogswin", say "Adhesive". Requires `Green_Scale_Quest` ==2. Requires `Green_Scale_Quest` set. Gives "Potion Vial" (67395).
45. Combine in "Verrell's Box of Potions" (67387): "Glue Powder" (67391), "Deep Barley Brew" (67392), "Potion Vial" (67395). Produces "Thick Adhesive" (67386). The combine does not fail.
46. northro/"Verrell Cogswin", hand "Thick Adhesive" (67386). Gives "Grey Scale Pieces" (67385).
47. northro/"Verrell Cogswin", hand "Thick Adhesive" (67386). Gives "Thick Adhesive" (67396).
48. Combine in "Verrell's Box of Potions" (67387): "Grey Scale Pieces" (67385), "Thick Adhesive" (67396). Produces "Grey Colored Scales" (67384). The combine does not fail.
49. northro/"Verrell Cogswin", hand "Grey Colored Scales" (67384). Gives "Green Dragon Scales" (11582).
50. eastkarana/"Tenal Redblade", hand "Green Dragon Scales" (11582) + "Red Dragon Scales" (11622) + "Totem of Fiery War" (20681). Gives "Mark of the Sword" (20683).
51. Loot "Hand of the Maestro" (20676) from "Hand of the Maestro" in `hateplane`.
52. Loot "Hand of the Maestro" (20676) from "Hand of the Maestro" in `hateplaneb`.
53. eastkarana/"Tenal Redblade", hand "Hand of the Maestro" (20676) + "Mark of the Sword" (20683). Gives "Tenal's note to Kargek" (20684).
54. Loot "Spiroc Wingblade" (20679) from "The Spiroc Lord" in `airplane`.
55. freeporteast/"Kargek Redblade", hand "Spiroc Wingblade" (20679) + "Tenal's note to Kargek" (20684). Gives "Red Scabbard" (17859).
56. Combine in "Red Scabbard" (17859): "Jagged Blade of War" (10908). Produces "Blade of Tactics" (10909), "Blade of Strategy" (10910). The combine does not fail.
57. Combine in "Red Scabbard" (17859): "Jagged Blade of War" (10908). Produces "Blade of Tactics" (10909), "Blade of Strategy" (10910). The combine does not fail.
58. Combine in "Red Scabbard" (17859): "Blade of Tactics" (10909), "Blade of Strategy" (10910). Produces "Jagged Blade of War" (10908). The combine does not fail.

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
18. Say "Tm Devrak Death" to rujd/"Rujd".
19. Spawns "spawn chest with Heavy Orcish Prison Key" (245241).
20. Loot "Pod of Water" (13044) from "spawn chest with Heavy Orcish Prison Key".
21. 6 alternative loot source(s) also yield Pod of Water (13044).
22. Forage "Pod of Water" (13044) in `ruja`.
23. Forage "Pod of Water" (13044) in `uqua`.
24. Forage "Pod of Water" (13044) in `yxtta`.
25. Combine in Brew Barrel (19): "Bottle of Aged Bloodwine" (51163), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aged Bloodwine" (51164). Requires Brewing, trivial 255.
26. Combine in Brew Barrel (19): "Bottle of Aldo's Bitter Ale" (75805), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aldo's Bitter Ale" (75811). Requires Brewing, trivial 15.
27. 17 other recipes also produce Bottle (16598).
28. Combine in Brew Barrel (19): "Pod of Water" (13044), "Bottle" (16598). Produces "Water Flask" (13006). Requires Brewing, trivial 21.
29. northro/"Verrell Cogswin", hand "Water Flask" (13006). Sets `Green_Scale_Quest` to `1`.
30. northro/"Verrell Cogswin", hand "Red Dragon Scales" (11622). Sets `Green_Scale_Quest` to `2`.
31. northro/"Verrell Cogswin", say "Adhesive". Requires `Green_Scale_Quest` ==2. Requires `Green_Scale_Quest` set. Gives "Verrell's Box of Potions" (67387).
32. Loot "Fractured Centaur Hoof" (67388) from "Centaur Archer" in `southkarana`.
33. Loot "Fractured Centaur Hoof" (67388) from "Centaur Charger" in `southkarana`.
34. Loot "Fractured Centaur Hoof" (67388) from "Centaur Courser" in `southkarana`.
35. Loot "Fractured Centaur Hoof" (67388) from "Centaur Foal" in `southkarana`.
36. Loot "Fractured Centaur Hoof" (67388) from "Centaur Sheltie" in `southkarana`.
37. Loot "Fire Giant Embers" (67389) from "A Fire Giant Warlord" (NPC 278023) in `soldungc`. Drop cache: 28.35% chance per kill.
38. Loot "Jagged Permafrost Shards" (67390) from "The Chilling Terror" in `permafrost`.
39. Combine in Oven (15): "Fractured Centaur Hoof" (67388), "Fire Giant Embers" (67389), "Jagged Permafrost Shards" (67390). Produces "Glue Powder" (67391). Requires Baking. The combine does not fail.
40. Common item: Barley (16590). Listed in 28 zones.
41. Common item: Deep Fungus Mold (67393). Listed in 28 zones.
42. Common item: Distilled Spirits (67394). Listed in 28 zones.
43. Combine in Brew Barrel (19): "Barley" (16590), "Deep Fungus Mold" (67393), "Distilled Spirits" (67394). Produces "Deep Barley Brew" (67392). Requires Brewing, trivial 110.
44. northro/"Verrell Cogswin", say "Adhesive". Requires `Green_Scale_Quest` ==2. Requires `Green_Scale_Quest` set. Gives "Potion Vial" (67395).
45. Combine in "Verrell's Box of Potions" (67387): "Glue Powder" (67391), "Deep Barley Brew" (67392), "Potion Vial" (67395). Produces "Thick Adhesive" (67386). The combine does not fail.
46. northro/"Verrell Cogswin", hand "Thick Adhesive" (67386). Gives "Grey Scale Pieces" (67385).
47. northro/"Verrell Cogswin", hand "Thick Adhesive" (67386). Gives "Thick Adhesive" (67396).
48. Combine in "Verrell's Box of Potions" (67387): "Grey Scale Pieces" (67385), "Thick Adhesive" (67396). Produces "Grey Colored Scales" (67384). The combine does not fail.
49. northro/"Verrell Cogswin", hand "Grey Colored Scales" (67384). Gives "Green Dragon Scales" (11582).
50. eastkarana/"Tenal Redblade", hand "Green Dragon Scales" (11582) + "Red Dragon Scales" (11622) + "Totem of Fiery War" (20681). Gives "Mark of the Sword" (20683).
51. Loot "Hand of the Maestro" (20676) from "Hand of the Maestro" in `hateplane`.
52. Loot "Hand of the Maestro" (20676) from "Hand of the Maestro" in `hateplaneb`.
53. eastkarana/"Tenal Redblade", hand "Hand of the Maestro" (20676) + "Mark of the Sword" (20683). Gives "Tenal's note to Kargek" (20684).
54. Loot "Spiroc Wingblade" (20679) from "The Spiroc Lord" in `airplane`.
55. freeporteast/"Kargek Redblade", hand "Spiroc Wingblade" (20679) + "Tenal's note to Kargek" (20684). Gives "Red Scabbard" (17859).
56. Combine in "Red Scabbard" (17859): "Jagged Blade of War" (10908). Produces "Blade of Tactics" (10909), "Blade of Strategy" (10910). The combine does not fail.
57. Combine in "Red Scabbard" (17859): "Blade of Tactics" (10909), "Blade of Strategy" (10910). Produces "Jagged Blade of War" (10908). The combine does not fail.
58. lakerathe/"Triathalon Swim Goggles", say "Hail". Gives "Rebreather" (16889).
59. Combine in Forge (17): "Smithing Chisel" (7052), "Large Brick of Ore" (10502). Hands back "Smithing Chisel" (7052). Produces "Small Brick of Ore" (10501). Requires Blacksmithing, trivial 27.
60. Combine in Forge (17): "Small Piece of Ore" (10500), "Water Flask" (13006). Produces "Small Brick of Ore" (10501). Requires Blacksmithing, trivial 27.
61. 11 other recipes also produce Small Brick of Ore (10501).
62. Loot "Toolbox Mold" (12077) from "Shevra Kollintar" in `paineel`.
63. kaladimb/"Jeet", say "Collect The Gnome Profit". Gives "Scrubber Key" (12164).
64. akanon/"Clockwork Scrubber", hand "Scrubber Key" (12164). Gives "Gnome Take" (12167).
65. kaladimb/"Jeet", hand "Gnome Take" (12167). Gives "Small Piece of Ore" (10500).
66. Combine in Forge (17): "Small Piece of Ore" (10500), "Water Flask" (13006). Produces "Metal Bits" (16905) x2. Requires Blacksmithing, trivial 18.
67. Combine in Forge (17): "Small Brick of Ore" (10501), "Toolbox Mold" (12077), "Water Flask" (13006), "Metal Bits" (16905). Produces "Toolbox" (17902). Requires Blacksmithing, trivial 51.
68. Common item: Platemail Helm (4001). Listed in 15 zones.
69. Fish "Fresh Fish" (13019) in `zone 0`.
70. Forage "Fresh Fish" (13019) in `kedge`.
71. Common item: Metal Rod (16850). Listed in 14 zones.
72. Common item: Metal Twine (16857). Listed in 10 zones.
73. Common item: Gnomish Bolts (16861). Listed in 10 zones.
74. Common item: Silk Lined Steel Helm (16862). Listed in 9 zones.
75. Common item: Fine Coral Mesh (16890). Listed in 14 zones.
76. Combine in "Toolbox" (17902): "Fresh Fish" (13019), "Metal Rod" (16850), "Metal Twine" (16857), "Gnomish Bolts" (16861), "Silk Lined Steel Helm" (16862), "Fine Coral Mesh" (16890). Produces "Aqualung" (16873) x20. Requires Tinkering, trivial 148.
77. Summon "Black Diamond of Nightmares" (29990) by casting "Imbue Nightmare".
78. potranquility/"Elder Fuirstel", say "Hail". Sets `pop_cod_final` to `1`.
79. poknowledge/"Aid Grimel", say "Versed In The Art Of Smithing". Requires `pop_cod_final` ==1. Requires `pop_cod_final` set. Gives "Filthy Breastplate" (15984).
80. Combine in "Mixing Bowl" (17906): "Celestial Solvent" (9731), "Words of Acquisition (Beza)" (11866). Produces "Celestial Essence" (9650). Requires Baking, trivial 15. The combine does not fail.
81. Combine in "Mixing Bowl" (17906): "Celestial Solvent" (9731), "Words of Burnishing" (11862). Produces "Celestial Essence" (9650). Requires Baking, trivial 15. The combine does not fail.
82. 67 other recipes also produce Celestial Essence (9650).
83. Common item: Jar of Acid (22133). Listed in 15 zones.
84. Combine in Brew Barrel (19): "Celestial Essence" (9650), "Jar of Acid" (22133). Produces "Acid Wash" (15987). Requires Brewing, trivial 151.
85. Combine in Forge (17): "Filthy Breastplate" (15984), "Acid Wash" (15987). Produces "Cleansed Breastplate" (15998). Requires Blacksmithing, trivial 227.
86. Common item: Mortar and Pestle (17904). Listed in 12 zones.
87. Loot "Sandstorm Pearl" (29909) from "Rorek Steelthorn" (NPC 209081) in `bothunder`. Drop cache: 5.33% chance per kill.
88. Combine in "Mortar and Pestle" (17904): "Sandstorm Pearl" (29909). Produces "Powdered Sandstorm Pearl" (29520) x4. Requires Make Poison, trivial 255.
89. Common item: Firing Sheet (16906). Listed in 34 zones.
90. Combine in Pottery Wheel (21): "Water Flask" (13006), "Block of Clay" (16901). Produces "Small Block of Clay" (16900) x3. Requires Pottery, trivial 21.
91. Combine in Pottery Wheel (21): "Small Block of Clay" (16900), "Water Flask" (13006). Produces "Block of Clay" (16901). Requires Pottery, trivial 21.
92. Combine in Pottery Wheel (21): "Water Flask" (13006), "Large Block of Clay" (16902). Produces "Block of Clay" (16901) x2. Requires Pottery, trivial 21.
93. Combine in Pottery Wheel (21): "Block of Clay" (16901), "Water Flask" (13006). Produces "Large Block of Clay" (16902). Requires Pottery, trivial 21.
94. Common item: Large Bowl Sketch (16963). Listed in 29 zones.
95. Combine in Pottery Wheel (21): "Large Block of Clay" (16902), "Water Flask" (13006), "Large Bowl Sketch" (16963). Produces "Unfired Mixing Bowl" (16930). Requires Pottery, trivial 128.
96. Combine in Kiln (22): "Firing Sheet" (16906), "Unfired Mixing Bowl" (16930). Produces "Mixing Bowl" (17906). Requires Pottery, trivial 15.
97. Combine in "Mixing Bowl" (17906): "Sandstorm Pearl" (29909). Produces "Powdered Sandstorm Pearl" (29520) x4. Requires Baking. The combine does not fail.
98. Spawns "a Koka'Vor chieftain" (210236) in `postorms` on event_signal.
99. Loot "Storm Rider Blood" (29526) from "a Koka'Vor chieftain".
100. Loot "Drop of Pure Rain" (29904) from "A vann stav" (NPC 209018) in `bothunder`. Drop cache: 4% chance per kill.
101. Combine in Brew Barrel (19): "Powdered Sandstorm Pearl" (29520), "Storm Rider Blood" (29526), "Drop of Pure Rain" (29904). Produces "Hurricane Temper" (29533). Requires Brewing, trivial 135.
102. Combine in Forge (17): "Cleansed Breastplate" (15998), "Hurricane Temper" (29533). Produces "Tempered Breastplate" (15999). Requires Blacksmithing, trivial 229.
103. Combine in Forge (17): "Black Diamond of Nightmares" (29990), "Tempered Breastplate" (15999). Produces "Imbued Breastplate" (15985). Requires Blacksmithing 220. Trivial at 275.
104. poknowledge/"Aid Grimel", hand "Imbued Breastplate" (15985). Gives "Hardened Leather Signet" (16249).
105. poknowledge/"Aid Grimel", say "Skill In Brewing". Requires `pop_cod_final` ==1. Requires `pop_cod_final` set. Gives "Portable Drink Barrel" (17179).
106. Spawns "Sepsis Rat" (45113) in `qcat` on event_death.
107. Loot "Rat Ears" (13072) from "Sepsis Rat".
108. 2 alternative loot source(s) also yield Rat Ears (13072).
109. Loot "Spider Legs" (13417) from "A Large Yellow Recluse" (NPC 56052) in `steamfont`. Drop cache: 55% chance per kill.
110. Common item: Rice (16593). Listed in 30 zones.
111. Combine in "Portable Drink Barrel" (17179): "Rat Ears" (13072), "Spider Legs" (13417), "Rice" (16593), "Bottle" (16598). Produces "Gnomish Spirits" (13037) x2. Requires Brewing, trivial 102.
112. Combine in Brew Barrel (19): "Rat Ears" (13072), "Spider Legs" (13417), "Rice" (16593), "Bottle" (16598). Produces "Gnomish Spirits" (13037) x2. Requires Brewing, trivial 102.
113. Combine in "Toolbox" (17902): "Water Flask" (13006), "Gnomish Spirits" (13037). Produces "Firewater" (16881). Requires Tinkering, trivial 17.
114. Common item: Metal Fastening (16888). Listed in 14 zones.
115. Common item: Sharkskin Tubing (16891). Listed in 14 zones.
116. Common item: Lime Coated Meshing (16892). Listed in 10 zones.
117. Combine in "Toolbox" (17902): "Platemail Helm" (4001), "Aqualung" (16873), "Firewater" (16881), "Metal Fastening" (16888), "Sharkskin Tubing" (16891), "Lime Coated Meshing" (16892). Produces "Rebreather" (16889). Requires Tinkering, trivial 175.
118. Loot "Block of Permafrost" (20665) from "Lady Vox" in `permafrost`.
119. Loot "Block of Permafrost" (20665) from "An Ice Giant" in `permafrost`.
120. Common item: Keg of Vox Tail Ale (20664). Listed in 13 zones.
121. oceanoftears/"Denken Strongpick", hand "Rebreather" (16889) + "Keg of Vox Tail Ale" (20664) + "Block of Permafrost" (20665). Gives "Ancient Sword Blade" (20667).
122. Loot "Ancient Blade" (20670) from "Queen Velazul Di'zok" in `chardok`.
123. Ground spawn of "Unjeweled Dragon Head Hilt" (20668) in `lakerathe`.
124. Loot "Apothic Crown" (1239) from "Magi P'Tasa" (NPC 186157) in `hateplaneb`. Drop cache: 19.16% chance per kill.
125. poknowledge/"Arch Mage Deidus", hand "Apothic Crown" (1239). Gives "Diamond" (10037).
126. Loot "Scroll of the Ox" (49007) from "A Sturdy Chest" in `stillmoona`.
127. Loot "Scroll of the Boar" (49008) from "A Sturdy Chest" in `stillmoona`.
128. Loot "Scroll of the Dragon" (49009) from "A Sturdy Chest" in `stillmoona`.
129. Loot "Scroll of the Tiger" (49010) from "A Sturdy Chest" in `stillmoona`.
130. Hand "Scroll of the Ox" (49007) + "Scroll of the Boar" (49008) + "Scroll of the Dragon" (49009) + "Scroll of the Tiger" (49010) to stillmoona/"The Keeper Of Strength". Spawns "A Spirit Keeper" (338169). Loot "Black Sapphire" (10036) from "A Spirit Keeper".
131. 43 alternative loot source(s) also yield Black Sapphire (10036).
132. Loot "Bayle List I" (18808) from "Mutt Rootlit" in `highpass`.
133. qrg/"Gerael Woodone", say "Deliver A Flask". Gives "Flask of Nitrates" (13945).
134. akanon/"Kimble Nogflop", hand "Flask of Nitrates" (13945). Gives "Regurgitonic" (12140).
135. qrg/"Mammoth", hand "Regurgitonic" (12140). Gives "Bayle List II" (18809).
136. Loot "Bayle List III" (18810) from "Dyllin Starsine" in `highpass`.
137. Loot "Bayle List III" (18810) from "Dyllin Starsine" in `highpasshold`.
138. southro/"Rathmana Allin", hand "Bayle List I" (18808) + "Bayle List II" (18809) + "Bayle List III" (18810). Gives "Translated Parchment" (18961).
139. highpass/"Stanos Herkanor", hand "Translated Parchment" (18961). Gives "Sealed Box" (28057).
140. Kill wakening/"A Tar Goo". Spawns "A Tar Goo" (119122).
141. Loot "Oily Goo Secretion" (11637) from "A Tar Goo".
142. 1 alternative loot source(s) also yield Oily Goo Secretion (11637).
143. bazaar/"Caerlyna", hand "Vale Sewing Kit" (92882). Gives "Vale Sewing Kit Token" (56884).
144. bazaar/"Caerlyna", hand "Vale Sewing Kit Token" (56884). Gives "Vale Sewing Kit" (92882).
145. Common item: Needle Mold (12019). Listed in 32 zones.
146. Common item: Thimble Mold (12057). Listed in 32 zones.
147. Combine in Forge (17): "Fine Steel Two Handed Sword" (5351), "Water Flask" (13006). Produces "Small Brick of High Quality Ore" (10468) x2, "Small Piece of High Quality Ore" (22229). Requires Blacksmithing, trivial 21.
148. Combine in Forge (17): "Smithing Chisel" (7052), "Small Brick of High Quality Ore" (10468). Hands back "Smithing Chisel" (7052). Produces "Small Piece of High Quality Ore" (22229) x2. Requires Blacksmithing, trivial 27.
149. 4 other recipes also produce Small Piece of High Quality Ore (22229).
150. Combine in Royal Qeynos Forge (40): "Small Piece of High Quality Ore" (22229), "Water Flask" (13006). Produces "High Quality Metal Bits" (22230). Requires Blacksmithing, trivial 20.
151. Combine in Vale Forge (49): "Needle Mold" (12019), "Thimble Mold" (12057), "Water Flask" (13006), "High Quality Metal Bits" (22230). Produces "Vale Sewing Kit" (92882). Requires Blacksmithing, trivial 162.
152. Loot "Crystalline Silk" (25306) from "A Crystal Grinder" (NPC 121089) in `crystal`. Drop cache: 100% chance per kill.
153. Combine in "Vale Sewing Kit" (92882): "Crystalline Silk" (25306). Produces "Crystalline Silk Mesh" (11636). Requires Tailoring, trivial 68.
154. skyshrine/"Iago Sabuela", hand "Crystalline Silk Mesh" (11636) + "Oily Goo Secretion" (11637). Gives "Empty Artifact Container" (17167).
155. Loot "Crystal Dragon Eye" (11638) from "An Ice Paw Sorcerer" in `velketor`.
156. Loot "Golden Dragon Claw" (11639) from "A Chetari Runemage" in `necropolis`.
157. Loot "Platinum Dragon Scale" (11640) from "A Siren Sorceress" in `sirens`.
158. Loot "Rodrick's Head" (1045) from "Rodrick Tardok".
159. Loot "Rodrick's Head" (1045) from "Rodrick Tardok" in `eastwastes`.
160. Spawns "Poxbreath Yellowfang" (116566) in `eastwastes` on event_signal.
161. Loot "Note from Kromrif" (18084) from "Poxbreath Yellowfang".
162. Spawns "Scarbrow Ga'Hruk" (116568) in `eastwastes` on event_signal.
163. Loot "Head of Scarbrow" (30141) from "Scarbrow Ga'Hruk".
164. Say "Help" to eastwastes/"Tain Hammerfrost".
165. Spawns "Ghrek Squatnot" (116560).
166. Loot "Frozen Elixir" (30138) from "Ghrek Squatnot".
167. eastwastes/"Tain Hammerfrost", hand "Frozen Elixir" (30138). Gives "Coldain Smithing Hammer" (30140).
168. Spawns "Rabid Tundra Kodiak" (116545) in `eastwastes` on event_waypoint_arrive.
169. Loot "Rabid Kodiak Skin" (30266) from "Rabid Tundra Kodiak".
170. eastwastes/"Boridain Glacierbane", hand "Rabid Kodiak Skin" (30266). Gives "Broken Axe" (30267).
171. iceclad/"A Lost Pirate", say "I Will Find The Parts". Gives "Map Binding" (17053).
172. Loot "First part of an Iceclad Map" (30043) from "Dire Wolf Stalker" in `iceclad`.
173. Loot "Second part of an Iceclad Map" (30044) from "Stormfeather" in `iceclad`.
174. Loot "Second part of an Iceclad Map" (30044) from "The Fabled Stormfeather".
175. greatdivide/"Bloody Gnome Captive", say "Map". Gives "Third part of an Iceclad Map" (30045).
176. Loot "Fourth part of an Iceclad Map" (30073) from "Lodizal" in `iceclad`.
177. Loot "Fourth part of an Iceclad Map" (30073) from "The Fabled Lodizal".
178. Combine in "Map Binding" (17053): "First part of an Iceclad Map" (30043), "Second part of an Iceclad Map" (30044), "Third part of an Iceclad Map" (30045), "Fourth part of an Iceclad Map" (30073). Produces "Pieces of the Iceclad Map" (30046). The combine does not fail.
179. Hand "Pieces of the Iceclad Map" (30046) to iceclad/"A Lost Pirate". Spawns "Rabid Snow Cougar Does Not Exist Using Regular For Now" (116008). Loot "High Quality Cougarskin" (30030) from "Rabid Snow Cougar Does Not Exist Using Regular For Now".
180. Loot "High Quality Tundra Kodiak Pelt" (30077) from "A Tundra Kodiak" (NPC 116044) in `eastwastes`. Drop cache: 3.91% chance per kill.
181. Combine in "Vale Sewing Kit" (92882): "High Quality Cougarskin" (30030), "High Quality Tundra Kodiak Pelt" (30077). Produces "Coldain Hunting Blanket" (30135). Requires Tailoring, trivial 41.
182. eastwastes/"Garadain Glacierbane", hand "Coldain Hunting Blanket" (30135). Gives "Copper Coldain Insignia Ring" (30131).
183. eastwastes/"Garadain Glacierbane", hand "Copper Coldain Insignia Ring" (30131) + "Broken Axe" (30267). Gives "Silver Coldain Insignia Ring" (30133).
184. Ground spawn of "Skinning Rock" (30062) in `eastwastes`.
185. Loot "Wooly Rhino Horn" (30088) from "A Wooly Rhino" (NPC 116033) in `eastwastes`. Drop cache: 20% chance per kill.
186. Loot "High Quality Walrus Hide" (30096) from "A Walrus" (NPC 116065) in `eastwastes`. Drop cache: 14.1% chance per kill.
187. Combine in Forge (17): "Skinning Rock" (30062), "Wooly Rhino Horn" (30088), "High Quality Walrus Hide" (30096). Produces "Coldain Hunting Knife" (30137). Requires Blacksmithing, trivial 41.
188. eastwastes/"Garadain Glacierbane", hand "Silver Coldain Insignia Ring" (30133) + "Coldain Hunting Knife" (30137). Gives "Gold Coldain Insignia Ring" (30132).
189. eastwastes/"Garadain Glacierbane", hand "Gold Coldain Insignia Ring" (30132) + "Coldain Smithing Hammer" (30140). Gives "Platinum Coldain Insignia Ring" (30134).
190. eastwastes/"Garadain Glacierbane", hand "Platinum Coldain Insignia Ring" (30134) + "Head of Scarbrow" (30141). Gives "Obsidian Coldain Insignia Ring" (30268).
191. eastwastes/"Garadain Glacierbane", hand "Rodrick's Head" (1045) + "Note from Kromrif" (18084) + "Obsidian Coldain Insignia Ring" (30268). Gives "Mithril Coldain Insignia Ring" (30162).
192. eastwastes/"Dobbin Crossaxe", hand "Mithril Coldain Insignia Ring" (30162). Gives "Note from Corbin" (1047).
193. eastwastes/"Garadain Glacierbane", hand "Note from Corbin" (1047). Gives "Adamantium Coldain Insignia Ring" (30163).
194. eastwastes/"Garadain Glacierbane", hand "Adamantium Coldain Insignia Ring" (30163). Gives "Marching Orders" (1093).
195. Hand "Marching Orders" (1093) to eastwastes/"Gloradin Coldheart". Spawns "Oracle of Ry'Gorr" (116006). Loot "Dragon Scripture Tablet" (11651) from "Oracle of Ry'Gorr".
196. 1 alternative loot source(s) also yield Dragon Scripture Tablet (11651).
197. Combine in "Empty Artifact Container" (17167): "Crystal Dragon Eye" (11638), "Golden Dragon Claw" (11639), "Platinum Dragon Scale" (11640), "Dragon Scripture Tablet" (11651). Produces "Sealed Box" (28057). The combine does not fail.
198. Hand "Sealed Box" (28057) to kithicor/"Adjutant D-Kan". Spawns "General V'ghera" (20205). Loot "General's Pouch" (28013) from "General V'ghera".
199. 6 alternative loot source(s) also yield General's Pouch (28013).
200. Loot "Fleshripper" (5411) from "Solusek kobold king" in `soldungb`.
201. Loot "Painbringer" (5410) from "Kobold Champion" in `soldungb`.
202. Loot "Mithril Two-Handed Sword" (5401) from "The Froglok King" in `gukbottom`.
203. Loot "Gigantic Zweihander" (5308) from "Karg IceBear" in `everfrost`.
204. qey2hh1/"Vilnius The Small", hand "Gigantic Zweihander" (5308) + "Mithril Two-Handed Sword" (5401) + "Painbringer" (5410) + "Fleshripper" (5411). Gives "Jagged Diamond Dagger" (7506).
205. Loot "Robe of the Ishva" (1357) from "Coercer Q'ioul" in `kithicor`.
206. Loot "Robe of the Ishva" (1357) from "Jinalis Andir" in `cauldron`.
207. Loot "Robe of the Ishva" (1357) from "The Ishva Mal" in `southkarana`.
208. Loot "Robe of the Kedge" (1253) from "Kubaria" (NPC 309002) in `chambersf`. Drop cache: 100% chance per kill.
209. Loot "Robe of the Oracle" (1354) from "Oracle of K'Arnon" in `oceanoftears`.
210. Loot "Robe of the Oracle" (1354) from "Oracle of K'Arnon" in `oot`.
211. Loot "Shining Metallic Robes" (1360) from "Yendar Starpyre" (NPC 56012) in `steamfont`. Drop cache: 100% chance per kill.
212. qey2hh1/"Vilnius The Small", hand "Robe of the Kedge" (1253) + "Robe of the Oracle" (1354) + "Robe of the Ishva" (1357) + "Shining Metallic Robes" (1360). Gives "Cazic Quill" (7505).
213. highpass/"Stanos Herkanor", hand "Cazic Quill" (7505) + "Jagged Diamond Dagger" (7506) + "General's Pouch" (28013). Gives "Ragebringer" (11057).
214. highpass/"Stanos Herkanor", say "Hail". Sets `Fatestealer` to `1`.
215. Unresolved cyclic prerequisite: `Fatestealer_gal` ==1.
216. Unresolved cyclic prerequisite: `Fatestealer_gal` ==1.
217. Unresolved cyclic prerequisite: `Fatestealer_mar` ==1.
218. Unresolved cyclic prerequisite: `Fatestealer_gal` ==1.
219. Unresolved cyclic prerequisite: `Fatestealer_mar` ==1.
220. Unresolved cyclic prerequisite: `Fatestealer_lyt` ==1.
221. Loot "Signed Agreement" (10246) from "Lythe Songbird" in `freeporteast`.
222. Loot "Signed Agreement" (10246) from "Lythe Songbird" in `freportw`.
223. overthere/"Inem R'Ker", hand "Signed Agreement" (10246). Sets `Fatestealer_lyt` to `1`.
224. Loot "Signed Agreement" (10239) from "Seana Marsinger" in `gfaydark`.
225. Loot "Signed Agreement" (52416) from "Stefan Marsinger" in `gfaydark`.
226. overthere/"Inem R'Ker", hand "Signed Agreement" (10239) + "Signed Agreement" (52416). Sets `Fatestealer_mar` to `1`.
227. Loot "Signed Agreement" (10243) from "Galdorin Visigothe" in `abysmal`.
228. overthere/"Inem R'Ker", hand "Signed Agreement" (10243). Sets `Fatestealer_gal` to `1`.
229. overthere/"Inem R'Ker", hand "Signed Agreement" (10243). Sets `Fatestealer_bard` to `1`.
230. Spawns "a Teir'Dal guardian" (186190) in `hateplaneb` on event death_complete:186114.
231. Loot "Stack of Pages" (52335) from "a Teir'Dal guardian".
232. 5 alternative loot source(s) also yield Stack of Pages (52335).
233. steamfont/"Yendar Starpyre", hand "Stack of Pages" (52335). Sets `Fatestealer_page` to `1`.
234. Spawns "A Furious Magma Guardian" (278123) in `soldungc` on event_signal.
235. Loot "Crystallized Shard of Doomfire" (21339) from "A Furious Magma Guardian".
236. 1 alternative loot source(s) also yield Crystallized Shard of Doomfire (21339).
237. Loot "Foul Doomfire Brimstone" (21342) from "A Pool Of Living Lava" (NPC 278043) in `soldungc`. Drop cache: 15.97% chance per kill.
238. Loot "Igneous Rock of Doomfire" (21340) from "Typhoeus" (NPC 278069) in `soldungc`. Drop cache: 35% chance per kill.
239. Loot "Pile of Doomfire Ash" (21341) from "a Taklasinai marauder" (NPC 278075) in `soldungc`. Drop cache: 35% chance per kill.
240. Hand "Crystallized Shard of Doomfire" (21339) + "Igneous Rock of Doomfire" (21340) + "Pile of Doomfire Ash" (21341) + "Foul Doomfire Brimstone" (21342) to soldungc/"The Firewatcher". Spawns "Culthor the Gatekeeper" (278005). Loot "Smoldering Embers of Solusek" (52346) from "Culthor the Gatekeeper".
241. nedaria/"Smith Dandi", hand "Smoldering Embers of Solusek" (52346). Sets `Fatestealer_forge` to `1`.
242. Spawns "a Teir'Dal guardian" (186190) in `hateplaneb` on event death_complete:186114.
243. Loot "Soulstone of Lanys" (52337) from "a Teir'Dal guardian".
244. 5 alternative loot source(s) also yield Soulstone of Lanys (52337).
245. nedaria/"Lirprin, Head Of Affairs", hand "Soulstone of Lanys" (52337). Requires `Fatestealer_bard` ==1. Requires `Fatestealer_page` ==1. Requires `Fatestealer_forge` ==1. Gives "Fatestealer" (52347).
246. nedaria/"Lirprin, Head Of Affairs", say "Hail". Sets `Fatestealer` to `3`.
247. Loot "Polished Bone Horn" (52349) from "A Baleful Stoneworker" (NPC 301023) in `bloodfields`. Drop cache: 4% chance per kill.
248. Loot "Brass Mouthpiece" (52350) from "An Ukun Fleshhound" (NPC 301009) in `bloodfields`. Drop cache: 3.67% chance per kill.
249. Loot "Bucket Mute" (52351) from "An Ukun Fleshhound" (NPC 301009) in `bloodfields`. Drop cache: 3.67% chance per kill.
250. Loot "Thin Leather Straps" (52352) from "An Ukun Fleshhound" (NPC 301009) in `bloodfields`. Drop cache: 3.67% chance per kill.
251. Hand "Polished Bone Horn" (52349) + "Brass Mouthpiece" (52350) + "Bucket Mute" (52351) + "Thin Leather Straps" (52352) to bloodfields/"Caller Donivin". Spawns "A Reclusive Girplan" (301033). Loot "Jacinth" (10053) from "A Reclusive Girplan".
252. 55 alternative loot source(s) also yield Jacinth (10053).
253. freeporteast/"Wenden Blackhammer", hand "Black Sapphire" (10036) + "Diamond" (10037) + "Jacinth" (10053) + "Unjeweled Dragon Head Hilt" (20668). Gives "Jeweled Dragon Head Hilt" (20671).
254. Ground spawn of "Severely Damaged Dragon Head Hilt" (20669) in `timorous`.
255. Loot "Giant Sized Monocle" (20678) from "A Mountain Giant Patriarch" in `dreadlands`.
256. frontiermtns/"Mentrax Mountainbone", hand "Giant Sized Monocle" (20678). Gives "Rejesiam Ore" (20666).
257. Loot "Ball of Everliving Golem" (20677) from "Dread" in `fearplane`.
258. Loot "Ball of Everliving Golem" (20677) from "Fright" in `fearplane`.
259. Loot "Ball of Everliving Golem" (20677) from "Terror" in `fearplane`.
260. freeporteast/"Wenden Blackhammer", hand "Rejesiam Ore" (20666) + "Severely Damaged Dragon Head Hilt" (20669) + "Ball of Everliving Golem" (20677). Gives "Finely Crafted Dragon Head Hilt" (20672).
261. Combine in "Red Scabbard" (17859): "Ancient Sword Blade" (20667), "Ancient Blade" (20670), "Jeweled Dragon Head Hilt" (20671), "Finely Crafted Dragon Head Hilt" (20672). Produces "Jagged Blade of War" (10908). The combine does not fail.
262. freeporteast/"Gartrog Smitehammer", hand "Jagged Blade of War" (10908) + "Red Scabbard" (17859). Gives "Jagged Blade of War" (66175).

### "Blackfall Blade" (60303)

1. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
2. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `steamfont`.
3. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `tox`.
4. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `toxxulia`.
5. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
6. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). The combine does not fail.
7. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
8. Say "Tm Devrak Death" to rujd/"Rujd".
9. Spawns "spawn chest with Heavy Orcish Prison Key" (245241).
10. Loot "Pod of Water" (13044) from "spawn chest with Heavy Orcish Prison Key".
11. 6 alternative loot source(s) also yield Pod of Water (13044).
12. Forage "Pod of Water" (13044) in `ruja`.
13. Forage "Pod of Water" (13044) in `uqua`.
14. Forage "Pod of Water" (13044) in `yxtta`.
15. Combine in Brew Barrel (19): "Bottle of Aged Bloodwine" (51163), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aged Bloodwine" (51164). Requires Brewing, trivial 255.
16. Combine in Brew Barrel (19): "Bottle of Aldo's Bitter Ale" (75805), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aldo's Bitter Ale" (75811). Requires Brewing, trivial 15.
17. 17 other recipes also produce Bottle (16598).
18. Combine in Brew Barrel (19): "Pod of Water" (13044), "Bottle" (16598). Produces "Water Flask" (13006). Requires Brewing, trivial 21.
19. nedaria/"Korezna Orecleaver", hand "Water Flask" (13006) + "Water Flask" (13006) + "Water Flask" (13006) + "Water Flask" (13006). Sets `warrior_epic_korezna` to `1`.
20. nedaria/"Korezna Orecleaver", hand "Water Flask" (13006) + "Water Flask" (13006) + "Water Flask" (13006). Sets `warrior_epic_korezna` to `2`.
21. **Broken:** nothing in the graph gives, loots, spawns, or combines Blackfall Ore (60301).
22. Unresolved cyclic prerequisite: `warrior_epic` ==17.
23. Ground spawn of "Frozen Pestle" (60323) in `iceclad`.
24. iceclad/"Fazzle Thumpkin", hand "Frozen Pestle" (60323). Sets `warrior_epic` to `18`.
25. Loot "Kreljnok's Muddled Rage" (60322) from "Possessed Brute" in `provinggrounds`.
26. draniksscar/"Korbuk Brimblade", hand "Kreljnok's Muddled Rage" (60322). Sets `warrior_epic` to `17`.
27. draniksscar/"Korbuk Brimblade", hand "Blackfall Ore" (60301). Requires `warrior_epic` >=2. Gives "Smelting Plans" (60302).
28. nedaria/"Korezna Orecleaver", hand "Blackfall Ore" (60301) + "Smelting Plans" (60302). Requires `warrior_epic_korezna` ==2. Gives "Blackfall Blade" (60303).

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
24. Say "Tm Devrak Death" to rujd/"Rujd".
25. Spawns "spawn chest with Heavy Orcish Prison Key" (245241).
26. Loot "Pod of Water" (13044) from "spawn chest with Heavy Orcish Prison Key".
27. 6 alternative loot source(s) also yield Pod of Water (13044).
28. Forage "Pod of Water" (13044) in `ruja`.
29. Forage "Pod of Water" (13044) in `uqua`.
30. Forage "Pod of Water" (13044) in `yxtta`.
31. Combine in Brew Barrel (19): "Bottle of Aged Bloodwine" (51163), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aged Bloodwine" (51164). Requires Brewing, trivial 255.
32. Combine in Brew Barrel (19): "Bottle of Aldo's Bitter Ale" (75805), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aldo's Bitter Ale" (75811). Requires Brewing, trivial 15.
33. 17 other recipes also produce Bottle (16598).
34. Combine in Brew Barrel (19): "Pod of Water" (13044), "Bottle" (16598). Produces "Water Flask" (13006). Requires Brewing, trivial 21.
35. northro/"Verrell Cogswin", hand "Water Flask" (13006). Sets `Green_Scale_Quest` to `1`.
36. northro/"Verrell Cogswin", hand "Red Dragon Scales" (11622). Sets `Green_Scale_Quest` to `2`.
37. northro/"Verrell Cogswin", say "Adhesive". Requires `Green_Scale_Quest` ==2. Requires `Green_Scale_Quest` set. Gives "Verrell's Box of Potions" (67387).
38. Loot "Fractured Centaur Hoof" (67388) from "Centaur Archer" in `southkarana`.
39. Loot "Fractured Centaur Hoof" (67388) from "Centaur Charger" in `southkarana`.
40. Loot "Fractured Centaur Hoof" (67388) from "Centaur Courser" in `southkarana`.
41. Loot "Fractured Centaur Hoof" (67388) from "Centaur Foal" in `southkarana`.
42. Loot "Fractured Centaur Hoof" (67388) from "Centaur Sheltie" in `southkarana`.
43. Loot "Fire Giant Embers" (67389) from "A Fire Giant Warlord" (NPC 278023) in `soldungc`. Drop cache: 28.35% chance per kill.
44. Loot "Jagged Permafrost Shards" (67390) from "The Chilling Terror" in `permafrost`.
45. Combine in Oven (15): "Fractured Centaur Hoof" (67388), "Fire Giant Embers" (67389), "Jagged Permafrost Shards" (67390). Produces "Glue Powder" (67391). Requires Baking. The combine does not fail.
46. Common item: Barley (16590). Listed in 28 zones.
47. Common item: Deep Fungus Mold (67393). Listed in 28 zones.
48. Common item: Distilled Spirits (67394). Listed in 28 zones.
49. Combine in Brew Barrel (19): "Barley" (16590), "Deep Fungus Mold" (67393), "Distilled Spirits" (67394). Produces "Deep Barley Brew" (67392). Requires Brewing, trivial 110.
50. northro/"Verrell Cogswin", say "Adhesive". Requires `Green_Scale_Quest` ==2. Requires `Green_Scale_Quest` set. Gives "Potion Vial" (67395).
51. Combine in "Verrell's Box of Potions" (67387): "Glue Powder" (67391), "Deep Barley Brew" (67392), "Potion Vial" (67395). Produces "Thick Adhesive" (67386). The combine does not fail.
52. northro/"Verrell Cogswin", hand "Thick Adhesive" (67386). Gives "Grey Scale Pieces" (67385).
53. northro/"Verrell Cogswin", hand "Thick Adhesive" (67386). Gives "Thick Adhesive" (67396).
54. Combine in "Verrell's Box of Potions" (67387): "Grey Scale Pieces" (67385), "Thick Adhesive" (67396). Produces "Grey Colored Scales" (67384). The combine does not fail.
55. northro/"Verrell Cogswin", hand "Grey Colored Scales" (67384). Gives "Green Dragon Scales" (11582).
56. eastkarana/"Tenal Redblade", hand "Green Dragon Scales" (11582) + "Red Dragon Scales" (11622) + "Totem of Fiery War" (20681). Gives "Mark of the Sword" (20683).
57. Loot "Hand of the Maestro" (20676) from "Hand of the Maestro" in `hateplane`.
58. Loot "Hand of the Maestro" (20676) from "Hand of the Maestro" in `hateplaneb`.
59. eastkarana/"Tenal Redblade", hand "Hand of the Maestro" (20676) + "Mark of the Sword" (20683). Gives "Tenal's note to Kargek" (20684).
60. Loot "Spiroc Wingblade" (20679) from "The Spiroc Lord" in `airplane`.
61. freeporteast/"Kargek Redblade", hand "Spiroc Wingblade" (20679) + "Tenal's note to Kargek" (20684). Gives "Red Scabbard" (17859).
62. Combine in "Red Scabbard" (17859): "Jagged Blade of War" (10908). Produces "Blade of Tactics" (10909), "Blade of Strategy" (10910). The combine does not fail.
63. Combine in "Red Scabbard" (17859): "Blade of Tactics" (10909), "Blade of Strategy" (10910). Produces "Jagged Blade of War" (10908). The combine does not fail.
64. lakerathe/"Triathalon Swim Goggles", say "Hail". Gives "Rebreather" (16889).
65. Combine in Forge (17): "Smithing Chisel" (7052), "Large Brick of Ore" (10502). Hands back "Smithing Chisel" (7052). Produces "Small Brick of Ore" (10501). Requires Blacksmithing, trivial 27.
66. Combine in Forge (17): "Small Piece of Ore" (10500), "Water Flask" (13006). Produces "Small Brick of Ore" (10501). Requires Blacksmithing, trivial 27.
67. 11 other recipes also produce Small Brick of Ore (10501).
68. Loot "Toolbox Mold" (12077) from "Shevra Kollintar" in `paineel`.
69. kaladimb/"Jeet", say "Collect The Gnome Profit". Gives "Scrubber Key" (12164).
70. akanon/"Clockwork Scrubber", hand "Scrubber Key" (12164). Gives "Gnome Take" (12167).
71. kaladimb/"Jeet", hand "Gnome Take" (12167). Gives "Small Piece of Ore" (10500).
72. Combine in Forge (17): "Small Piece of Ore" (10500), "Water Flask" (13006). Produces "Metal Bits" (16905) x2. Requires Blacksmithing, trivial 18.
73. Combine in Forge (17): "Small Brick of Ore" (10501), "Toolbox Mold" (12077), "Water Flask" (13006), "Metal Bits" (16905). Produces "Toolbox" (17902). Requires Blacksmithing, trivial 51.
74. Common item: Platemail Helm (4001). Listed in 15 zones.
75. Fish "Fresh Fish" (13019) in `zone 0`.
76. Forage "Fresh Fish" (13019) in `kedge`.
77. Common item: Metal Rod (16850). Listed in 14 zones.
78. Common item: Metal Twine (16857). Listed in 10 zones.
79. Common item: Gnomish Bolts (16861). Listed in 10 zones.
80. Common item: Silk Lined Steel Helm (16862). Listed in 9 zones.
81. Common item: Fine Coral Mesh (16890). Listed in 14 zones.
82. Combine in "Toolbox" (17902): "Fresh Fish" (13019), "Metal Rod" (16850), "Metal Twine" (16857), "Gnomish Bolts" (16861), "Silk Lined Steel Helm" (16862), "Fine Coral Mesh" (16890). Produces "Aqualung" (16873) x20. Requires Tinkering, trivial 148.
83. Summon "Black Diamond of Nightmares" (29990) by casting "Imbue Nightmare".
84. potranquility/"Elder Fuirstel", say "Hail". Sets `pop_cod_final` to `1`.
85. poknowledge/"Aid Grimel", say "Versed In The Art Of Smithing". Requires `pop_cod_final` ==1. Requires `pop_cod_final` set. Gives "Filthy Breastplate" (15984).
86. Combine in "Mixing Bowl" (17906): "Celestial Solvent" (9731), "Words of Acquisition (Beza)" (11866). Produces "Celestial Essence" (9650). Requires Baking, trivial 15. The combine does not fail.
87. Combine in "Mixing Bowl" (17906): "Celestial Solvent" (9731), "Words of Burnishing" (11862). Produces "Celestial Essence" (9650). Requires Baking, trivial 15. The combine does not fail.
88. 67 other recipes also produce Celestial Essence (9650).
89. Common item: Jar of Acid (22133). Listed in 15 zones.
90. Combine in Brew Barrel (19): "Celestial Essence" (9650), "Jar of Acid" (22133). Produces "Acid Wash" (15987). Requires Brewing, trivial 151.
91. Combine in Forge (17): "Filthy Breastplate" (15984), "Acid Wash" (15987). Produces "Cleansed Breastplate" (15998). Requires Blacksmithing, trivial 227.
92. Common item: Mortar and Pestle (17904). Listed in 12 zones.
93. Loot "Sandstorm Pearl" (29909) from "Rorek Steelthorn" (NPC 209081) in `bothunder`. Drop cache: 5.33% chance per kill.
94. Combine in "Mortar and Pestle" (17904): "Sandstorm Pearl" (29909). Produces "Powdered Sandstorm Pearl" (29520) x4. Requires Make Poison, trivial 255.
95. Common item: Firing Sheet (16906). Listed in 34 zones.
96. Combine in Pottery Wheel (21): "Water Flask" (13006), "Block of Clay" (16901). Produces "Small Block of Clay" (16900) x3. Requires Pottery, trivial 21.
97. Combine in Pottery Wheel (21): "Small Block of Clay" (16900), "Water Flask" (13006). Produces "Block of Clay" (16901). Requires Pottery, trivial 21.
98. Combine in Pottery Wheel (21): "Water Flask" (13006), "Large Block of Clay" (16902). Produces "Block of Clay" (16901) x2. Requires Pottery, trivial 21.
99. Combine in Pottery Wheel (21): "Block of Clay" (16901), "Water Flask" (13006). Produces "Large Block of Clay" (16902). Requires Pottery, trivial 21.
100. Common item: Large Bowl Sketch (16963). Listed in 29 zones.
101. Combine in Pottery Wheel (21): "Large Block of Clay" (16902), "Water Flask" (13006), "Large Bowl Sketch" (16963). Produces "Unfired Mixing Bowl" (16930). Requires Pottery, trivial 128.
102. Combine in Kiln (22): "Firing Sheet" (16906), "Unfired Mixing Bowl" (16930). Produces "Mixing Bowl" (17906). Requires Pottery, trivial 15.
103. Combine in "Mixing Bowl" (17906): "Sandstorm Pearl" (29909). Produces "Powdered Sandstorm Pearl" (29520) x4. Requires Baking. The combine does not fail.
104. Spawns "a Koka'Vor chieftain" (210236) in `postorms` on event_signal.
105. Loot "Storm Rider Blood" (29526) from "a Koka'Vor chieftain".
106. Loot "Drop of Pure Rain" (29904) from "A vann stav" (NPC 209018) in `bothunder`. Drop cache: 4% chance per kill.
107. Combine in Brew Barrel (19): "Powdered Sandstorm Pearl" (29520), "Storm Rider Blood" (29526), "Drop of Pure Rain" (29904). Produces "Hurricane Temper" (29533). Requires Brewing, trivial 135.
108. Combine in Forge (17): "Cleansed Breastplate" (15998), "Hurricane Temper" (29533). Produces "Tempered Breastplate" (15999). Requires Blacksmithing, trivial 229.
109. Combine in Forge (17): "Black Diamond of Nightmares" (29990), "Tempered Breastplate" (15999). Produces "Imbued Breastplate" (15985). Requires Blacksmithing 220. Trivial at 275.
110. poknowledge/"Aid Grimel", hand "Imbued Breastplate" (15985). Gives "Hardened Leather Signet" (16249).
111. poknowledge/"Aid Grimel", say "Skill In Brewing". Requires `pop_cod_final` ==1. Requires `pop_cod_final` set. Gives "Portable Drink Barrel" (17179).
112. Spawns "Sepsis Rat" (45113) in `qcat` on event_death.
113. Loot "Rat Ears" (13072) from "Sepsis Rat".
114. 2 alternative loot source(s) also yield Rat Ears (13072).
115. Loot "Spider Legs" (13417) from "A Large Yellow Recluse" (NPC 56052) in `steamfont`. Drop cache: 55% chance per kill.
116. Common item: Rice (16593). Listed in 30 zones.
117. Combine in "Portable Drink Barrel" (17179): "Rat Ears" (13072), "Spider Legs" (13417), "Rice" (16593), "Bottle" (16598). Produces "Gnomish Spirits" (13037) x2. Requires Brewing, trivial 102.
118. Combine in Brew Barrel (19): "Rat Ears" (13072), "Spider Legs" (13417), "Rice" (16593), "Bottle" (16598). Produces "Gnomish Spirits" (13037) x2. Requires Brewing, trivial 102.
119. Combine in "Toolbox" (17902): "Water Flask" (13006), "Gnomish Spirits" (13037). Produces "Firewater" (16881). Requires Tinkering, trivial 17.
120. Common item: Metal Fastening (16888). Listed in 14 zones.
121. Common item: Sharkskin Tubing (16891). Listed in 14 zones.
122. Common item: Lime Coated Meshing (16892). Listed in 10 zones.
123. Combine in "Toolbox" (17902): "Platemail Helm" (4001), "Aqualung" (16873), "Firewater" (16881), "Metal Fastening" (16888), "Sharkskin Tubing" (16891), "Lime Coated Meshing" (16892). Produces "Rebreather" (16889). Requires Tinkering, trivial 175.
124. Loot "Block of Permafrost" (20665) from "Lady Vox" in `permafrost`.
125. Loot "Block of Permafrost" (20665) from "An Ice Giant" in `permafrost`.
126. Common item: Keg of Vox Tail Ale (20664). Listed in 13 zones.
127. oceanoftears/"Denken Strongpick", hand "Rebreather" (16889) + "Keg of Vox Tail Ale" (20664) + "Block of Permafrost" (20665). Gives "Ancient Sword Blade" (20667).
128. Loot "Ancient Blade" (20670) from "Queen Velazul Di'zok" in `chardok`.
129. Ground spawn of "Unjeweled Dragon Head Hilt" (20668) in `lakerathe`.
130. Loot "Apothic Crown" (1239) from "Magi P'Tasa" (NPC 186157) in `hateplaneb`. Drop cache: 19.16% chance per kill.
131. poknowledge/"Arch Mage Deidus", hand "Apothic Crown" (1239). Gives "Diamond" (10037).
132. Loot "Scroll of the Ox" (49007) from "A Sturdy Chest" in `stillmoona`.
133. Loot "Scroll of the Boar" (49008) from "A Sturdy Chest" in `stillmoona`.
134. Loot "Scroll of the Dragon" (49009) from "A Sturdy Chest" in `stillmoona`.
135. Loot "Scroll of the Tiger" (49010) from "A Sturdy Chest" in `stillmoona`.
136. Hand "Scroll of the Ox" (49007) + "Scroll of the Boar" (49008) + "Scroll of the Dragon" (49009) + "Scroll of the Tiger" (49010) to stillmoona/"The Keeper Of Strength". Spawns "A Spirit Keeper" (338169). Loot "Black Sapphire" (10036) from "A Spirit Keeper".
137. 43 alternative loot source(s) also yield Black Sapphire (10036).
138. Loot "Bayle List I" (18808) from "Mutt Rootlit" in `highpass`.
139. qrg/"Gerael Woodone", say "Deliver A Flask". Gives "Flask of Nitrates" (13945).
140. akanon/"Kimble Nogflop", hand "Flask of Nitrates" (13945). Gives "Regurgitonic" (12140).
141. qrg/"Mammoth", hand "Regurgitonic" (12140). Gives "Bayle List II" (18809).
142. Loot "Bayle List III" (18810) from "Dyllin Starsine" in `highpass`.
143. Loot "Bayle List III" (18810) from "Dyllin Starsine" in `highpasshold`.
144. southro/"Rathmana Allin", hand "Bayle List I" (18808) + "Bayle List II" (18809) + "Bayle List III" (18810). Gives "Translated Parchment" (18961).
145. highpass/"Stanos Herkanor", hand "Translated Parchment" (18961). Gives "Sealed Box" (28057).
146. Kill wakening/"A Tar Goo". Spawns "A Tar Goo" (119122).
147. Loot "Oily Goo Secretion" (11637) from "A Tar Goo".
148. 1 alternative loot source(s) also yield Oily Goo Secretion (11637).
149. bazaar/"Caerlyna", hand "Vale Sewing Kit" (92882). Gives "Vale Sewing Kit Token" (56884).
150. bazaar/"Caerlyna", hand "Vale Sewing Kit Token" (56884). Gives "Vale Sewing Kit" (92882).
151. Common item: Needle Mold (12019). Listed in 32 zones.
152. Common item: Thimble Mold (12057). Listed in 32 zones.
153. Combine in Forge (17): "Fine Steel Two Handed Sword" (5351), "Water Flask" (13006). Produces "Small Brick of High Quality Ore" (10468) x2, "Small Piece of High Quality Ore" (22229). Requires Blacksmithing, trivial 21.
154. Combine in Forge (17): "Smithing Chisel" (7052), "Small Brick of High Quality Ore" (10468). Hands back "Smithing Chisel" (7052). Produces "Small Piece of High Quality Ore" (22229) x2. Requires Blacksmithing, trivial 27.
155. 4 other recipes also produce Small Piece of High Quality Ore (22229).
156. Combine in Royal Qeynos Forge (40): "Small Piece of High Quality Ore" (22229), "Water Flask" (13006). Produces "High Quality Metal Bits" (22230). Requires Blacksmithing, trivial 20.
157. Combine in Vale Forge (49): "Needle Mold" (12019), "Thimble Mold" (12057), "Water Flask" (13006), "High Quality Metal Bits" (22230). Produces "Vale Sewing Kit" (92882). Requires Blacksmithing, trivial 162.
158. Loot "Crystalline Silk" (25306) from "A Crystal Grinder" (NPC 121089) in `crystal`. Drop cache: 100% chance per kill.
159. Combine in "Vale Sewing Kit" (92882): "Crystalline Silk" (25306). Produces "Crystalline Silk Mesh" (11636). Requires Tailoring, trivial 68.
160. skyshrine/"Iago Sabuela", hand "Crystalline Silk Mesh" (11636) + "Oily Goo Secretion" (11637). Gives "Empty Artifact Container" (17167).
161. Loot "Crystal Dragon Eye" (11638) from "An Ice Paw Sorcerer" in `velketor`.
162. Loot "Golden Dragon Claw" (11639) from "A Chetari Runemage" in `necropolis`.
163. Loot "Platinum Dragon Scale" (11640) from "A Siren Sorceress" in `sirens`.
164. Loot "Rodrick's Head" (1045) from "Rodrick Tardok".
165. Loot "Rodrick's Head" (1045) from "Rodrick Tardok" in `eastwastes`.
166. Spawns "Poxbreath Yellowfang" (116566) in `eastwastes` on event_signal.
167. Loot "Note from Kromrif" (18084) from "Poxbreath Yellowfang".
168. Spawns "Scarbrow Ga'Hruk" (116568) in `eastwastes` on event_signal.
169. Loot "Head of Scarbrow" (30141) from "Scarbrow Ga'Hruk".
170. Say "Help" to eastwastes/"Tain Hammerfrost".
171. Spawns "Ghrek Squatnot" (116560).
172. Loot "Frozen Elixir" (30138) from "Ghrek Squatnot".
173. eastwastes/"Tain Hammerfrost", hand "Frozen Elixir" (30138). Gives "Coldain Smithing Hammer" (30140).
174. Spawns "Rabid Tundra Kodiak" (116545) in `eastwastes` on event_waypoint_arrive.
175. Loot "Rabid Kodiak Skin" (30266) from "Rabid Tundra Kodiak".
176. eastwastes/"Boridain Glacierbane", hand "Rabid Kodiak Skin" (30266). Gives "Broken Axe" (30267).
177. iceclad/"A Lost Pirate", say "I Will Find The Parts". Gives "Map Binding" (17053).
178. Loot "First part of an Iceclad Map" (30043) from "Dire Wolf Stalker" in `iceclad`.
179. Loot "Second part of an Iceclad Map" (30044) from "Stormfeather" in `iceclad`.
180. Loot "Second part of an Iceclad Map" (30044) from "The Fabled Stormfeather".
181. greatdivide/"Bloody Gnome Captive", say "Map". Gives "Third part of an Iceclad Map" (30045).
182. Loot "Fourth part of an Iceclad Map" (30073) from "Lodizal" in `iceclad`.
183. Loot "Fourth part of an Iceclad Map" (30073) from "The Fabled Lodizal".
184. Combine in "Map Binding" (17053): "First part of an Iceclad Map" (30043), "Second part of an Iceclad Map" (30044), "Third part of an Iceclad Map" (30045), "Fourth part of an Iceclad Map" (30073). Produces "Pieces of the Iceclad Map" (30046). The combine does not fail.
185. Hand "Pieces of the Iceclad Map" (30046) to iceclad/"A Lost Pirate". Spawns "Rabid Snow Cougar Does Not Exist Using Regular For Now" (116008). Loot "High Quality Cougarskin" (30030) from "Rabid Snow Cougar Does Not Exist Using Regular For Now".
186. Loot "High Quality Tundra Kodiak Pelt" (30077) from "A Tundra Kodiak" (NPC 116044) in `eastwastes`. Drop cache: 3.91% chance per kill.
187. Combine in "Vale Sewing Kit" (92882): "High Quality Cougarskin" (30030), "High Quality Tundra Kodiak Pelt" (30077). Produces "Coldain Hunting Blanket" (30135). Requires Tailoring, trivial 41.
188. eastwastes/"Garadain Glacierbane", hand "Coldain Hunting Blanket" (30135). Gives "Copper Coldain Insignia Ring" (30131).
189. eastwastes/"Garadain Glacierbane", hand "Copper Coldain Insignia Ring" (30131) + "Broken Axe" (30267). Gives "Silver Coldain Insignia Ring" (30133).
190. Ground spawn of "Skinning Rock" (30062) in `eastwastes`.
191. Loot "Wooly Rhino Horn" (30088) from "A Wooly Rhino" (NPC 116033) in `eastwastes`. Drop cache: 20% chance per kill.
192. Loot "High Quality Walrus Hide" (30096) from "A Walrus" (NPC 116065) in `eastwastes`. Drop cache: 14.1% chance per kill.
193. Combine in Forge (17): "Skinning Rock" (30062), "Wooly Rhino Horn" (30088), "High Quality Walrus Hide" (30096). Produces "Coldain Hunting Knife" (30137). Requires Blacksmithing, trivial 41.
194. eastwastes/"Garadain Glacierbane", hand "Silver Coldain Insignia Ring" (30133) + "Coldain Hunting Knife" (30137). Gives "Gold Coldain Insignia Ring" (30132).
195. eastwastes/"Garadain Glacierbane", hand "Gold Coldain Insignia Ring" (30132) + "Coldain Smithing Hammer" (30140). Gives "Platinum Coldain Insignia Ring" (30134).
196. eastwastes/"Garadain Glacierbane", hand "Platinum Coldain Insignia Ring" (30134) + "Head of Scarbrow" (30141). Gives "Obsidian Coldain Insignia Ring" (30268).
197. eastwastes/"Garadain Glacierbane", hand "Rodrick's Head" (1045) + "Note from Kromrif" (18084) + "Obsidian Coldain Insignia Ring" (30268). Gives "Mithril Coldain Insignia Ring" (30162).
198. eastwastes/"Dobbin Crossaxe", hand "Mithril Coldain Insignia Ring" (30162). Gives "Note from Corbin" (1047).
199. eastwastes/"Garadain Glacierbane", hand "Note from Corbin" (1047). Gives "Adamantium Coldain Insignia Ring" (30163).
200. eastwastes/"Garadain Glacierbane", hand "Adamantium Coldain Insignia Ring" (30163). Gives "Marching Orders" (1093).
201. Hand "Marching Orders" (1093) to eastwastes/"Gloradin Coldheart". Spawns "Oracle of Ry'Gorr" (116006). Loot "Dragon Scripture Tablet" (11651) from "Oracle of Ry'Gorr".
202. 1 alternative loot source(s) also yield Dragon Scripture Tablet (11651).
203. Combine in "Empty Artifact Container" (17167): "Crystal Dragon Eye" (11638), "Golden Dragon Claw" (11639), "Platinum Dragon Scale" (11640), "Dragon Scripture Tablet" (11651). Produces "Sealed Box" (28057). The combine does not fail.
204. Hand "Sealed Box" (28057) to kithicor/"Adjutant D-Kan". Spawns "General V'ghera" (20205). Loot "General's Pouch" (28013) from "General V'ghera".
205. 6 alternative loot source(s) also yield General's Pouch (28013).
206. Loot "Fleshripper" (5411) from "Solusek kobold king" in `soldungb`.
207. Loot "Painbringer" (5410) from "Kobold Champion" in `soldungb`.
208. Loot "Mithril Two-Handed Sword" (5401) from "The Froglok King" in `gukbottom`.
209. Loot "Gigantic Zweihander" (5308) from "Karg IceBear" in `everfrost`.
210. qey2hh1/"Vilnius The Small", hand "Gigantic Zweihander" (5308) + "Mithril Two-Handed Sword" (5401) + "Painbringer" (5410) + "Fleshripper" (5411). Gives "Jagged Diamond Dagger" (7506).
211. Loot "Robe of the Ishva" (1357) from "Coercer Q'ioul" in `kithicor`.
212. Loot "Robe of the Ishva" (1357) from "Jinalis Andir" in `cauldron`.
213. Loot "Robe of the Ishva" (1357) from "The Ishva Mal" in `southkarana`.
214. Loot "Robe of the Kedge" (1253) from "Kubaria" (NPC 309002) in `chambersf`. Drop cache: 100% chance per kill.
215. Loot "Robe of the Oracle" (1354) from "Oracle of K'Arnon" in `oceanoftears`.
216. Loot "Robe of the Oracle" (1354) from "Oracle of K'Arnon" in `oot`.
217. Loot "Shining Metallic Robes" (1360) from "Yendar Starpyre" (NPC 56012) in `steamfont`. Drop cache: 100% chance per kill.
218. qey2hh1/"Vilnius The Small", hand "Robe of the Kedge" (1253) + "Robe of the Oracle" (1354) + "Robe of the Ishva" (1357) + "Shining Metallic Robes" (1360). Gives "Cazic Quill" (7505).
219. highpass/"Stanos Herkanor", hand "Cazic Quill" (7505) + "Jagged Diamond Dagger" (7506) + "General's Pouch" (28013). Gives "Ragebringer" (11057).
220. highpass/"Stanos Herkanor", say "Hail". Sets `Fatestealer` to `1`.
221. Unresolved cyclic prerequisite: `Fatestealer_gal` ==1.
222. Unresolved cyclic prerequisite: `Fatestealer_gal` ==1.
223. Unresolved cyclic prerequisite: `Fatestealer_mar` ==1.
224. Unresolved cyclic prerequisite: `Fatestealer_gal` ==1.
225. Unresolved cyclic prerequisite: `Fatestealer_mar` ==1.
226. Unresolved cyclic prerequisite: `Fatestealer_lyt` ==1.
227. Loot "Signed Agreement" (10246) from "Lythe Songbird" in `freeporteast`.
228. Loot "Signed Agreement" (10246) from "Lythe Songbird" in `freportw`.
229. overthere/"Inem R'Ker", hand "Signed Agreement" (10246). Sets `Fatestealer_lyt` to `1`.
230. Loot "Signed Agreement" (10239) from "Seana Marsinger" in `gfaydark`.
231. Loot "Signed Agreement" (52416) from "Stefan Marsinger" in `gfaydark`.
232. overthere/"Inem R'Ker", hand "Signed Agreement" (10239) + "Signed Agreement" (52416). Sets `Fatestealer_mar` to `1`.
233. Loot "Signed Agreement" (10243) from "Galdorin Visigothe" in `abysmal`.
234. overthere/"Inem R'Ker", hand "Signed Agreement" (10243). Sets `Fatestealer_gal` to `1`.
235. overthere/"Inem R'Ker", hand "Signed Agreement" (10243). Sets `Fatestealer_bard` to `1`.
236. Spawns "a Teir'Dal guardian" (186190) in `hateplaneb` on event death_complete:186114.
237. Loot "Stack of Pages" (52335) from "a Teir'Dal guardian".
238. 5 alternative loot source(s) also yield Stack of Pages (52335).
239. steamfont/"Yendar Starpyre", hand "Stack of Pages" (52335). Sets `Fatestealer_page` to `1`.
240. Spawns "A Furious Magma Guardian" (278123) in `soldungc` on event_signal.
241. Loot "Crystallized Shard of Doomfire" (21339) from "A Furious Magma Guardian".
242. 1 alternative loot source(s) also yield Crystallized Shard of Doomfire (21339).
243. Loot "Foul Doomfire Brimstone" (21342) from "A Pool Of Living Lava" (NPC 278043) in `soldungc`. Drop cache: 15.97% chance per kill.
244. Loot "Igneous Rock of Doomfire" (21340) from "Typhoeus" (NPC 278069) in `soldungc`. Drop cache: 35% chance per kill.
245. Loot "Pile of Doomfire Ash" (21341) from "a Taklasinai marauder" (NPC 278075) in `soldungc`. Drop cache: 35% chance per kill.
246. Hand "Crystallized Shard of Doomfire" (21339) + "Igneous Rock of Doomfire" (21340) + "Pile of Doomfire Ash" (21341) + "Foul Doomfire Brimstone" (21342) to soldungc/"The Firewatcher". Spawns "Culthor the Gatekeeper" (278005). Loot "Smoldering Embers of Solusek" (52346) from "Culthor the Gatekeeper".
247. nedaria/"Smith Dandi", hand "Smoldering Embers of Solusek" (52346). Sets `Fatestealer_forge` to `1`.
248. Spawns "a Teir'Dal guardian" (186190) in `hateplaneb` on event death_complete:186114.
249. Loot "Soulstone of Lanys" (52337) from "a Teir'Dal guardian".
250. 5 alternative loot source(s) also yield Soulstone of Lanys (52337).
251. nedaria/"Lirprin, Head Of Affairs", hand "Soulstone of Lanys" (52337). Requires `Fatestealer_bard` ==1. Requires `Fatestealer_page` ==1. Requires `Fatestealer_forge` ==1. Gives "Fatestealer" (52347).
252. nedaria/"Lirprin, Head Of Affairs", say "Hail". Sets `Fatestealer` to `3`.
253. Loot "Polished Bone Horn" (52349) from "A Baleful Stoneworker" (NPC 301023) in `bloodfields`. Drop cache: 4% chance per kill.
254. Loot "Brass Mouthpiece" (52350) from "An Ukun Fleshhound" (NPC 301009) in `bloodfields`. Drop cache: 3.67% chance per kill.
255. Loot "Bucket Mute" (52351) from "An Ukun Fleshhound" (NPC 301009) in `bloodfields`. Drop cache: 3.67% chance per kill.
256. Loot "Thin Leather Straps" (52352) from "An Ukun Fleshhound" (NPC 301009) in `bloodfields`. Drop cache: 3.67% chance per kill.
257. Hand "Polished Bone Horn" (52349) + "Brass Mouthpiece" (52350) + "Bucket Mute" (52351) + "Thin Leather Straps" (52352) to bloodfields/"Caller Donivin". Spawns "A Reclusive Girplan" (301033). Loot "Jacinth" (10053) from "A Reclusive Girplan".
258. 55 alternative loot source(s) also yield Jacinth (10053).
259. freeporteast/"Wenden Blackhammer", hand "Black Sapphire" (10036) + "Diamond" (10037) + "Jacinth" (10053) + "Unjeweled Dragon Head Hilt" (20668). Gives "Jeweled Dragon Head Hilt" (20671).
260. Ground spawn of "Severely Damaged Dragon Head Hilt" (20669) in `timorous`.
261. Loot "Giant Sized Monocle" (20678) from "A Mountain Giant Patriarch" in `dreadlands`.
262. frontiermtns/"Mentrax Mountainbone", hand "Giant Sized Monocle" (20678). Gives "Rejesiam Ore" (20666).
263. Loot "Ball of Everliving Golem" (20677) from "Dread" in `fearplane`.
264. Loot "Ball of Everliving Golem" (20677) from "Fright" in `fearplane`.
265. Loot "Ball of Everliving Golem" (20677) from "Terror" in `fearplane`.
266. freeporteast/"Wenden Blackhammer", hand "Rejesiam Ore" (20666) + "Severely Damaged Dragon Head Hilt" (20669) + "Ball of Everliving Golem" (20677). Gives "Finely Crafted Dragon Head Hilt" (20672).
267. Combine in "Red Scabbard" (17859): "Ancient Sword Blade" (20667), "Ancient Blade" (20670), "Jeweled Dragon Head Hilt" (20671), "Finely Crafted Dragon Head Hilt" (20672). Produces "Jagged Blade of War" (10908). The combine does not fail.
268. freeporteast/"Gartrog Smitehammer", hand "Jagged Blade of War" (10908) + "Red Scabbard" (17859). Gives "Red Scabbard" (17869).
269. freeporteast/"Gartrog Smitehammer", hand "Jagged Blade of War" (10908) + "Red Scabbard" (17859). Gives "Jagged Blade of War" (66175).
270. Combine in "Red Scabbard" (17869): "Jagged Blade of War" (66175). Produces "Blade of Tactics" (66176), "Blade of Strategy" (66177). Requires Pottery. The combine does not fail.
271. Combine in "Red Scabbard" (17869): "Blade of Tactics" (66176), "Blade of Strategy" (66177). Produces "Jagged Blade of War" (66175). Requires Pottery. The combine does not fail.
272. draniksscar/"Korbuk Brimblade", say "Work". Sets `warrior_pre` to `1`.
273. Loot "Korbuk's Weapon Plans" (60285) from "The Diaku Overseer" in `potactics`.
274. draniksscar/"Korbuk Brimblade", hand "Korbuk's Weapon Plans" (60285). Sets `warrior_pre` to `2`.
275. Loot "Elegant Shank" (60286) from "Shoqui the Forgotten" in `hatesfury`.
276. draniksscar/"Korbuk Brimblade", hand "Elegant Shank" (60286). Sets `warrior_pre` to `3`.
277. Loot "Redblade Family Sword" (60287) from "Drevlon Knacknabber" in `eastkarana`.
278. freeporteast/"Kargek Redblade", hand "Redblade Family Sword" (60287). Requires `warrior_pre` set. Requires `warrior_pre` ==3. Gives "Emblazoned Champion's Hilt" (60288).
279. draniksscar/"Korbuk Brimblade", hand "Emblazoned Champion's Hilt" (60288). Sets `warrior_pre` to `4`.
280. thurgadina/"Dardek Bladewright", hand "Korbuk's Weapon Plans" (60285) + "Elegant Shank" (60286) + "Emblazoned Champion's Hilt" (60288). Sets `warrior_pre` to `5`.
281. thurgadina/"Dardek Bladewright", hand "Korbuk's Weapon Plans" (60285) + "Elegant Shank" (60286) + "Emblazoned Champion's Hilt" (60288). Requires `warrior_pre` ==4. Gives "Dardek's Forged Blade" (60292).
282. draniksscar/"Korbuk Brimblade", hand "Dardek's Forged Blade" (60292). Sets `warrior_pre` to `6`.
283. draniksscar/"Korbuk Brimblade", say "Work". Sets `warrior_epic` to `1`.
284. Kill bloodfields/"Girplan Slasher". Spawns "Girplan Devourer" (301063).
285. Loot "Decrepit Hilt" (60307) from "Girplan Devourer".
286. firiona/"Corfia Nultethen", hand "Decrepit Hilt" (60307). Sets `warrior_epic` to `9`.
287. Unresolved cyclic prerequisite: `warrior_epic_gulak` ==1.
288. firiona/"Corfia Nultethen", say "Galuk Drek". Sets `warrior_epic_veksar` to `1`.
289. burningwood/"Telin Darkforest", say "Action". Gives "Worn Note" (20472).
290. gfaydark/"Faelin Bloodbriar", hand "Worn Note" (20472). Gives "Faelin's Ring" (20446).
291. kithicor/"Giz X-Tin", hand "Faelin's Ring" (20446). Gives "Dark Metal Coin" (20447).
292. burningwood/"Telin Darkforest", hand "Dark Metal Coin" (20447). Gives "Worn Dark Metal Coin" (20448).
293. eastkarana/"Althele", hand "Worn Dark Metal Coin" (20448). Gives "Braided Grass Amulet" (20450).
294. eastkarana/"Sionae", hand "Braided Grass Amulet" (20450). Gives "Frayed Braided Grass Amulet" (20451).
295. eastkarana/"Teloa", hand "Frayed Braided Grass Amulet" (20451). Triggers `eastkarana/althele#signal:1`.
296. Starts timer `attack`.
297. Spawns "Corruptor" (15153) after `eastkarana/althele#timer:attack`.
298. Loot "Fleshbound Tome" (20452) from "Corruptor".
299. eastkarana/"Althele", hand "Fleshbound Tome" (20452). Gives "Earth Stained Note" (18959).
300. misty/"Ella Foodcrafter", hand "Earth Stained Note" (18959). Sets `shiny_tin_bowl` to `1`.
301. misty/"Ella Foodcrafter", say "Two Tasks". Requires `shiny_tin_bowl` set. Gives "Shiny Tin Bowl" (17860).
302. Hand "Shiny Tin Bowl" (17860) to hole/"Jaeil The Wretched". Spawns "Jaeil the Insane" (39154). Loot "Soulbound Hammer" (20478) from "Jaeil the Insane".
303. erudnint/"Mairee Silentone", hand "Soulbound Hammer" (20478). Gives "Dwarven Smiths Hammer" (20479).
304. Kill airplane/"An Essence Carrier". Spawns "An Essence Tamer" (71071).
305. Loot "Swirling Sphere of Color" (20494) from "An Essence Tamer".
306. erudnint/"Mairee Silentone", hand "Dwarven Smiths Hammer" (20479) + "Swirling Sphere of Color" (20494). Gives "Hammer of the Ancients" (20485).
307. kaladimb/"Kinlo Strongarm", hand "Hammer of the Ancients" (20485). Gives "Small bit of Mithril Ore" (20482).
308. kaladimb/"Kinlo Strongarm", hand "Small bit of Mithril Ore" (20482). Gives "Refined Mithril Blade" (20483).
309. Encounter starts when NPC 186201 spawns in `hateplaneb`.
310. Starts timer `popinny`.
311. Kill NPC 186158.
312. Starts timer `text`.
313. Starts timer `text2`.
314. Starts timer `spawninny`.
315. Spawns "Innoruuk" (186107) after `hateplaneb/inny#timer:spawninny`.
316. Loot "Shattered Emerald of Corruption" (20484) from "Innoruuk".
317. 1 alternative loot source(s) also yield Shattered Emerald of Corruption (20484).
318. northkarana/"Xanuusus", hand "Refined Mithril Blade" (20483) + "Shattered Emerald of Corruption" (20484). Gives "Earthcaller" (20488).
319. eastkarana/"Althele", say "Hail". Sets `ranger_epic` to `1`.
320. veksar/"Player", on enter. Sets `warrior_epic_gulak` to `1`.
321. Spawns "Decaying Lord Galuk Drek, not be in db yet" (109906) in `veksar` on enter.
322. Loot "Skeletal Tome of Galuk Drek" (60310) from "Decaying Lord Galuk Drek, not be in db yet".
323. firiona/"Corfia Nultethen", hand "Skeletal Tome of Galuk Drek" (60310). Requires `warrior_epic` set. Requires `warrior_epic` ==9. Gives "Glistening Hilt" (60311).

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
11. Say "Tm Devrak Death" to rujd/"Rujd".
12. Spawns "spawn chest with Heavy Orcish Prison Key" (245241).
13. Loot "Pod of Water" (13044) from "spawn chest with Heavy Orcish Prison Key".
14. 6 alternative loot source(s) also yield Pod of Water (13044).
15. Forage "Pod of Water" (13044) in `ruja`.
16. Forage "Pod of Water" (13044) in `uqua`.
17. Forage "Pod of Water" (13044) in `yxtta`.
18. Combine in Brew Barrel (19): "Bottle of Aged Bloodwine" (51163), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aged Bloodwine" (51164). Requires Brewing, trivial 255.
19. Combine in Brew Barrel (19): "Bottle of Aldo's Bitter Ale" (75805), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aldo's Bitter Ale" (75811). Requires Brewing, trivial 15.
20. 17 other recipes also produce Bottle (16598).
21. Combine in Brew Barrel (19): "Pod of Water" (13044), "Bottle" (16598). Produces "Water Flask" (13006). Requires Brewing, trivial 21.
22. Combine in Royal Qeynos Forge (40): "Small Piece of High Quality Ore" (22229), "Water Flask" (13006). Produces "High Quality Metal Bits" (22230). Requires Blacksmithing, trivial 20.
23. Common item: Gemming Mold (60317). Listed in 4 zones.
24. Combine in Forge (17): "High Quality Metal Bits" (22230), "Water Flask" (13006), "Gemming Mold" (60317). Produces "Gemming Tool" (60316). Requires Blacksmithing, trivial 115.

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
24. Say "Tm Devrak Death" to rujd/"Rujd".
25. Spawns "spawn chest with Heavy Orcish Prison Key" (245241).
26. Loot "Pod of Water" (13044) from "spawn chest with Heavy Orcish Prison Key".
27. 6 alternative loot source(s) also yield Pod of Water (13044).
28. Forage "Pod of Water" (13044) in `ruja`.
29. Forage "Pod of Water" (13044) in `uqua`.
30. Forage "Pod of Water" (13044) in `yxtta`.
31. Combine in Brew Barrel (19): "Bottle of Aged Bloodwine" (51163), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aged Bloodwine" (51164). Requires Brewing, trivial 255.
32. Combine in Brew Barrel (19): "Bottle of Aldo's Bitter Ale" (75805), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aldo's Bitter Ale" (75811). Requires Brewing, trivial 15.
33. 17 other recipes also produce Bottle (16598).
34. Combine in Brew Barrel (19): "Pod of Water" (13044), "Bottle" (16598). Produces "Water Flask" (13006). Requires Brewing, trivial 21.
35. northro/"Verrell Cogswin", hand "Water Flask" (13006). Sets `Green_Scale_Quest` to `1`.
36. northro/"Verrell Cogswin", hand "Red Dragon Scales" (11622). Sets `Green_Scale_Quest` to `2`.
37. northro/"Verrell Cogswin", say "Adhesive". Requires `Green_Scale_Quest` ==2. Requires `Green_Scale_Quest` set. Gives "Verrell's Box of Potions" (67387).
38. Loot "Fractured Centaur Hoof" (67388) from "Centaur Archer" in `southkarana`.
39. Loot "Fractured Centaur Hoof" (67388) from "Centaur Charger" in `southkarana`.
40. Loot "Fractured Centaur Hoof" (67388) from "Centaur Courser" in `southkarana`.
41. Loot "Fractured Centaur Hoof" (67388) from "Centaur Foal" in `southkarana`.
42. Loot "Fractured Centaur Hoof" (67388) from "Centaur Sheltie" in `southkarana`.
43. Loot "Fire Giant Embers" (67389) from "A Fire Giant Warlord" (NPC 278023) in `soldungc`. Drop cache: 28.35% chance per kill.
44. Loot "Jagged Permafrost Shards" (67390) from "The Chilling Terror" in `permafrost`.
45. Combine in Oven (15): "Fractured Centaur Hoof" (67388), "Fire Giant Embers" (67389), "Jagged Permafrost Shards" (67390). Produces "Glue Powder" (67391). Requires Baking. The combine does not fail.
46. Common item: Barley (16590). Listed in 28 zones.
47. Common item: Deep Fungus Mold (67393). Listed in 28 zones.
48. Common item: Distilled Spirits (67394). Listed in 28 zones.
49. Combine in Brew Barrel (19): "Barley" (16590), "Deep Fungus Mold" (67393), "Distilled Spirits" (67394). Produces "Deep Barley Brew" (67392). Requires Brewing, trivial 110.
50. northro/"Verrell Cogswin", say "Adhesive". Requires `Green_Scale_Quest` ==2. Requires `Green_Scale_Quest` set. Gives "Potion Vial" (67395).
51. Combine in "Verrell's Box of Potions" (67387): "Glue Powder" (67391), "Deep Barley Brew" (67392), "Potion Vial" (67395). Produces "Thick Adhesive" (67386). The combine does not fail.
52. northro/"Verrell Cogswin", hand "Thick Adhesive" (67386). Gives "Grey Scale Pieces" (67385).
53. northro/"Verrell Cogswin", hand "Thick Adhesive" (67386). Gives "Thick Adhesive" (67396).
54. Combine in "Verrell's Box of Potions" (67387): "Grey Scale Pieces" (67385), "Thick Adhesive" (67396). Produces "Grey Colored Scales" (67384). The combine does not fail.
55. northro/"Verrell Cogswin", hand "Grey Colored Scales" (67384). Gives "Green Dragon Scales" (11582).
56. eastkarana/"Tenal Redblade", hand "Green Dragon Scales" (11582) + "Red Dragon Scales" (11622) + "Totem of Fiery War" (20681). Gives "Mark of the Sword" (20683).
57. Loot "Hand of the Maestro" (20676) from "Hand of the Maestro" in `hateplane`.
58. Loot "Hand of the Maestro" (20676) from "Hand of the Maestro" in `hateplaneb`.
59. eastkarana/"Tenal Redblade", hand "Hand of the Maestro" (20676) + "Mark of the Sword" (20683). Gives "Tenal's note to Kargek" (20684).
60. Loot "Spiroc Wingblade" (20679) from "The Spiroc Lord" in `airplane`.
61. freeporteast/"Kargek Redblade", hand "Spiroc Wingblade" (20679) + "Tenal's note to Kargek" (20684). Gives "Red Scabbard" (17859).
62. Combine in "Red Scabbard" (17859): "Jagged Blade of War" (10908). Produces "Blade of Tactics" (10909), "Blade of Strategy" (10910). The combine does not fail.
63. Combine in "Red Scabbard" (17859): "Blade of Tactics" (10909), "Blade of Strategy" (10910). Produces "Jagged Blade of War" (10908). The combine does not fail.
64. lakerathe/"Triathalon Swim Goggles", say "Hail". Gives "Rebreather" (16889).
65. Combine in Forge (17): "Smithing Chisel" (7052), "Large Brick of Ore" (10502). Hands back "Smithing Chisel" (7052). Produces "Small Brick of Ore" (10501). Requires Blacksmithing, trivial 27.
66. Combine in Forge (17): "Small Piece of Ore" (10500), "Water Flask" (13006). Produces "Small Brick of Ore" (10501). Requires Blacksmithing, trivial 27.
67. 11 other recipes also produce Small Brick of Ore (10501).
68. Loot "Toolbox Mold" (12077) from "Shevra Kollintar" in `paineel`.
69. kaladimb/"Jeet", say "Collect The Gnome Profit". Gives "Scrubber Key" (12164).
70. akanon/"Clockwork Scrubber", hand "Scrubber Key" (12164). Gives "Gnome Take" (12167).
71. kaladimb/"Jeet", hand "Gnome Take" (12167). Gives "Small Piece of Ore" (10500).
72. Combine in Forge (17): "Small Piece of Ore" (10500), "Water Flask" (13006). Produces "Metal Bits" (16905) x2. Requires Blacksmithing, trivial 18.
73. Combine in Forge (17): "Small Brick of Ore" (10501), "Toolbox Mold" (12077), "Water Flask" (13006), "Metal Bits" (16905). Produces "Toolbox" (17902). Requires Blacksmithing, trivial 51.
74. Common item: Platemail Helm (4001). Listed in 15 zones.
75. Fish "Fresh Fish" (13019) in `zone 0`.
76. Forage "Fresh Fish" (13019) in `kedge`.
77. Common item: Metal Rod (16850). Listed in 14 zones.
78. Common item: Metal Twine (16857). Listed in 10 zones.
79. Common item: Gnomish Bolts (16861). Listed in 10 zones.
80. Common item: Silk Lined Steel Helm (16862). Listed in 9 zones.
81. Common item: Fine Coral Mesh (16890). Listed in 14 zones.
82. Combine in "Toolbox" (17902): "Fresh Fish" (13019), "Metal Rod" (16850), "Metal Twine" (16857), "Gnomish Bolts" (16861), "Silk Lined Steel Helm" (16862), "Fine Coral Mesh" (16890). Produces "Aqualung" (16873) x20. Requires Tinkering, trivial 148.
83. Summon "Black Diamond of Nightmares" (29990) by casting "Imbue Nightmare".
84. potranquility/"Elder Fuirstel", say "Hail". Sets `pop_cod_final` to `1`.
85. poknowledge/"Aid Grimel", say "Versed In The Art Of Smithing". Requires `pop_cod_final` ==1. Requires `pop_cod_final` set. Gives "Filthy Breastplate" (15984).
86. Combine in "Mixing Bowl" (17906): "Celestial Solvent" (9731), "Words of Acquisition (Beza)" (11866). Produces "Celestial Essence" (9650). Requires Baking, trivial 15. The combine does not fail.
87. Combine in "Mixing Bowl" (17906): "Celestial Solvent" (9731), "Words of Burnishing" (11862). Produces "Celestial Essence" (9650). Requires Baking, trivial 15. The combine does not fail.
88. 67 other recipes also produce Celestial Essence (9650).
89. Common item: Jar of Acid (22133). Listed in 15 zones.
90. Combine in Brew Barrel (19): "Celestial Essence" (9650), "Jar of Acid" (22133). Produces "Acid Wash" (15987). Requires Brewing, trivial 151.
91. Combine in Forge (17): "Filthy Breastplate" (15984), "Acid Wash" (15987). Produces "Cleansed Breastplate" (15998). Requires Blacksmithing, trivial 227.
92. Common item: Mortar and Pestle (17904). Listed in 12 zones.
93. Loot "Sandstorm Pearl" (29909) from "Rorek Steelthorn" (NPC 209081) in `bothunder`. Drop cache: 5.33% chance per kill.
94. Combine in "Mortar and Pestle" (17904): "Sandstorm Pearl" (29909). Produces "Powdered Sandstorm Pearl" (29520) x4. Requires Make Poison, trivial 255.
95. Common item: Firing Sheet (16906). Listed in 34 zones.
96. Combine in Pottery Wheel (21): "Water Flask" (13006), "Block of Clay" (16901). Produces "Small Block of Clay" (16900) x3. Requires Pottery, trivial 21.
97. Combine in Pottery Wheel (21): "Small Block of Clay" (16900), "Water Flask" (13006). Produces "Block of Clay" (16901). Requires Pottery, trivial 21.
98. Combine in Pottery Wheel (21): "Water Flask" (13006), "Large Block of Clay" (16902). Produces "Block of Clay" (16901) x2. Requires Pottery, trivial 21.
99. Combine in Pottery Wheel (21): "Block of Clay" (16901), "Water Flask" (13006). Produces "Large Block of Clay" (16902). Requires Pottery, trivial 21.
100. Common item: Large Bowl Sketch (16963). Listed in 29 zones.
101. Combine in Pottery Wheel (21): "Large Block of Clay" (16902), "Water Flask" (13006), "Large Bowl Sketch" (16963). Produces "Unfired Mixing Bowl" (16930). Requires Pottery, trivial 128.
102. Combine in Kiln (22): "Firing Sheet" (16906), "Unfired Mixing Bowl" (16930). Produces "Mixing Bowl" (17906). Requires Pottery, trivial 15.
103. Combine in "Mixing Bowl" (17906): "Sandstorm Pearl" (29909). Produces "Powdered Sandstorm Pearl" (29520) x4. Requires Baking. The combine does not fail.
104. Spawns "a Koka'Vor chieftain" (210236) in `postorms` on event_signal.
105. Loot "Storm Rider Blood" (29526) from "a Koka'Vor chieftain".
106. Loot "Drop of Pure Rain" (29904) from "A vann stav" (NPC 209018) in `bothunder`. Drop cache: 4% chance per kill.
107. Combine in Brew Barrel (19): "Powdered Sandstorm Pearl" (29520), "Storm Rider Blood" (29526), "Drop of Pure Rain" (29904). Produces "Hurricane Temper" (29533). Requires Brewing, trivial 135.
108. Combine in Forge (17): "Cleansed Breastplate" (15998), "Hurricane Temper" (29533). Produces "Tempered Breastplate" (15999). Requires Blacksmithing, trivial 229.
109. Combine in Forge (17): "Black Diamond of Nightmares" (29990), "Tempered Breastplate" (15999). Produces "Imbued Breastplate" (15985). Requires Blacksmithing 220. Trivial at 275.
110. poknowledge/"Aid Grimel", hand "Imbued Breastplate" (15985). Gives "Hardened Leather Signet" (16249).
111. poknowledge/"Aid Grimel", say "Skill In Brewing". Requires `pop_cod_final` ==1. Requires `pop_cod_final` set. Gives "Portable Drink Barrel" (17179).
112. Spawns "Sepsis Rat" (45113) in `qcat` on event_death.
113. Loot "Rat Ears" (13072) from "Sepsis Rat".
114. 2 alternative loot source(s) also yield Rat Ears (13072).
115. Loot "Spider Legs" (13417) from "A Large Yellow Recluse" (NPC 56052) in `steamfont`. Drop cache: 55% chance per kill.
116. Common item: Rice (16593). Listed in 30 zones.
117. Combine in "Portable Drink Barrel" (17179): "Rat Ears" (13072), "Spider Legs" (13417), "Rice" (16593), "Bottle" (16598). Produces "Gnomish Spirits" (13037) x2. Requires Brewing, trivial 102.
118. Combine in Brew Barrel (19): "Rat Ears" (13072), "Spider Legs" (13417), "Rice" (16593), "Bottle" (16598). Produces "Gnomish Spirits" (13037) x2. Requires Brewing, trivial 102.
119. Combine in "Toolbox" (17902): "Water Flask" (13006), "Gnomish Spirits" (13037). Produces "Firewater" (16881). Requires Tinkering, trivial 17.
120. Common item: Metal Fastening (16888). Listed in 14 zones.
121. Common item: Sharkskin Tubing (16891). Listed in 14 zones.
122. Common item: Lime Coated Meshing (16892). Listed in 10 zones.
123. Combine in "Toolbox" (17902): "Platemail Helm" (4001), "Aqualung" (16873), "Firewater" (16881), "Metal Fastening" (16888), "Sharkskin Tubing" (16891), "Lime Coated Meshing" (16892). Produces "Rebreather" (16889). Requires Tinkering, trivial 175.
124. Loot "Block of Permafrost" (20665) from "Lady Vox" in `permafrost`.
125. Loot "Block of Permafrost" (20665) from "An Ice Giant" in `permafrost`.
126. Common item: Keg of Vox Tail Ale (20664). Listed in 13 zones.
127. oceanoftears/"Denken Strongpick", hand "Rebreather" (16889) + "Keg of Vox Tail Ale" (20664) + "Block of Permafrost" (20665). Gives "Ancient Sword Blade" (20667).
128. Loot "Ancient Blade" (20670) from "Queen Velazul Di'zok" in `chardok`.
129. Ground spawn of "Unjeweled Dragon Head Hilt" (20668) in `lakerathe`.
130. Loot "Apothic Crown" (1239) from "Magi P'Tasa" (NPC 186157) in `hateplaneb`. Drop cache: 19.16% chance per kill.
131. poknowledge/"Arch Mage Deidus", hand "Apothic Crown" (1239). Gives "Diamond" (10037).
132. Loot "Scroll of the Ox" (49007) from "A Sturdy Chest" in `stillmoona`.
133. Loot "Scroll of the Boar" (49008) from "A Sturdy Chest" in `stillmoona`.
134. Loot "Scroll of the Dragon" (49009) from "A Sturdy Chest" in `stillmoona`.
135. Loot "Scroll of the Tiger" (49010) from "A Sturdy Chest" in `stillmoona`.
136. Hand "Scroll of the Ox" (49007) + "Scroll of the Boar" (49008) + "Scroll of the Dragon" (49009) + "Scroll of the Tiger" (49010) to stillmoona/"The Keeper Of Strength". Spawns "A Spirit Keeper" (338169). Loot "Black Sapphire" (10036) from "A Spirit Keeper".
137. 43 alternative loot source(s) also yield Black Sapphire (10036).
138. Loot "Bayle List I" (18808) from "Mutt Rootlit" in `highpass`.
139. qrg/"Gerael Woodone", say "Deliver A Flask". Gives "Flask of Nitrates" (13945).
140. akanon/"Kimble Nogflop", hand "Flask of Nitrates" (13945). Gives "Regurgitonic" (12140).
141. qrg/"Mammoth", hand "Regurgitonic" (12140). Gives "Bayle List II" (18809).
142. Loot "Bayle List III" (18810) from "Dyllin Starsine" in `highpass`.
143. Loot "Bayle List III" (18810) from "Dyllin Starsine" in `highpasshold`.
144. southro/"Rathmana Allin", hand "Bayle List I" (18808) + "Bayle List II" (18809) + "Bayle List III" (18810). Gives "Translated Parchment" (18961).
145. highpass/"Stanos Herkanor", hand "Translated Parchment" (18961). Gives "Sealed Box" (28057).
146. Kill wakening/"A Tar Goo". Spawns "A Tar Goo" (119122).
147. Loot "Oily Goo Secretion" (11637) from "A Tar Goo".
148. 1 alternative loot source(s) also yield Oily Goo Secretion (11637).
149. bazaar/"Caerlyna", hand "Vale Sewing Kit" (92882). Gives "Vale Sewing Kit Token" (56884).
150. bazaar/"Caerlyna", hand "Vale Sewing Kit Token" (56884). Gives "Vale Sewing Kit" (92882).
151. Common item: Needle Mold (12019). Listed in 32 zones.
152. Common item: Thimble Mold (12057). Listed in 32 zones.
153. Combine in Forge (17): "Fine Steel Two Handed Sword" (5351), "Water Flask" (13006). Produces "Small Brick of High Quality Ore" (10468) x2, "Small Piece of High Quality Ore" (22229). Requires Blacksmithing, trivial 21.
154. Combine in Forge (17): "Smithing Chisel" (7052), "Small Brick of High Quality Ore" (10468). Hands back "Smithing Chisel" (7052). Produces "Small Piece of High Quality Ore" (22229) x2. Requires Blacksmithing, trivial 27.
155. 4 other recipes also produce Small Piece of High Quality Ore (22229).
156. Combine in Royal Qeynos Forge (40): "Small Piece of High Quality Ore" (22229), "Water Flask" (13006). Produces "High Quality Metal Bits" (22230). Requires Blacksmithing, trivial 20.
157. Combine in Vale Forge (49): "Needle Mold" (12019), "Thimble Mold" (12057), "Water Flask" (13006), "High Quality Metal Bits" (22230). Produces "Vale Sewing Kit" (92882). Requires Blacksmithing, trivial 162.
158. Loot "Crystalline Silk" (25306) from "A Crystal Grinder" (NPC 121089) in `crystal`. Drop cache: 100% chance per kill.
159. Combine in "Vale Sewing Kit" (92882): "Crystalline Silk" (25306). Produces "Crystalline Silk Mesh" (11636). Requires Tailoring, trivial 68.
160. skyshrine/"Iago Sabuela", hand "Crystalline Silk Mesh" (11636) + "Oily Goo Secretion" (11637). Gives "Empty Artifact Container" (17167).
161. Loot "Crystal Dragon Eye" (11638) from "An Ice Paw Sorcerer" in `velketor`.
162. Loot "Golden Dragon Claw" (11639) from "A Chetari Runemage" in `necropolis`.
163. Loot "Platinum Dragon Scale" (11640) from "A Siren Sorceress" in `sirens`.
164. Loot "Rodrick's Head" (1045) from "Rodrick Tardok".
165. Loot "Rodrick's Head" (1045) from "Rodrick Tardok" in `eastwastes`.
166. Spawns "Poxbreath Yellowfang" (116566) in `eastwastes` on event_signal.
167. Loot "Note from Kromrif" (18084) from "Poxbreath Yellowfang".
168. Spawns "Scarbrow Ga'Hruk" (116568) in `eastwastes` on event_signal.
169. Loot "Head of Scarbrow" (30141) from "Scarbrow Ga'Hruk".
170. Say "Help" to eastwastes/"Tain Hammerfrost".
171. Spawns "Ghrek Squatnot" (116560).
172. Loot "Frozen Elixir" (30138) from "Ghrek Squatnot".
173. eastwastes/"Tain Hammerfrost", hand "Frozen Elixir" (30138). Gives "Coldain Smithing Hammer" (30140).
174. Spawns "Rabid Tundra Kodiak" (116545) in `eastwastes` on event_waypoint_arrive.
175. Loot "Rabid Kodiak Skin" (30266) from "Rabid Tundra Kodiak".
176. eastwastes/"Boridain Glacierbane", hand "Rabid Kodiak Skin" (30266). Gives "Broken Axe" (30267).
177. iceclad/"A Lost Pirate", say "I Will Find The Parts". Gives "Map Binding" (17053).
178. Loot "First part of an Iceclad Map" (30043) from "Dire Wolf Stalker" in `iceclad`.
179. Loot "Second part of an Iceclad Map" (30044) from "Stormfeather" in `iceclad`.
180. Loot "Second part of an Iceclad Map" (30044) from "The Fabled Stormfeather".
181. greatdivide/"Bloody Gnome Captive", say "Map". Gives "Third part of an Iceclad Map" (30045).
182. Loot "Fourth part of an Iceclad Map" (30073) from "Lodizal" in `iceclad`.
183. Loot "Fourth part of an Iceclad Map" (30073) from "The Fabled Lodizal".
184. Combine in "Map Binding" (17053): "First part of an Iceclad Map" (30043), "Second part of an Iceclad Map" (30044), "Third part of an Iceclad Map" (30045), "Fourth part of an Iceclad Map" (30073). Produces "Pieces of the Iceclad Map" (30046). The combine does not fail.
185. Hand "Pieces of the Iceclad Map" (30046) to iceclad/"A Lost Pirate". Spawns "Rabid Snow Cougar Does Not Exist Using Regular For Now" (116008). Loot "High Quality Cougarskin" (30030) from "Rabid Snow Cougar Does Not Exist Using Regular For Now".
186. Loot "High Quality Tundra Kodiak Pelt" (30077) from "A Tundra Kodiak" (NPC 116044) in `eastwastes`. Drop cache: 3.91% chance per kill.
187. Combine in "Vale Sewing Kit" (92882): "High Quality Cougarskin" (30030), "High Quality Tundra Kodiak Pelt" (30077). Produces "Coldain Hunting Blanket" (30135). Requires Tailoring, trivial 41.
188. eastwastes/"Garadain Glacierbane", hand "Coldain Hunting Blanket" (30135). Gives "Copper Coldain Insignia Ring" (30131).
189. eastwastes/"Garadain Glacierbane", hand "Copper Coldain Insignia Ring" (30131) + "Broken Axe" (30267). Gives "Silver Coldain Insignia Ring" (30133).
190. Ground spawn of "Skinning Rock" (30062) in `eastwastes`.
191. Loot "Wooly Rhino Horn" (30088) from "A Wooly Rhino" (NPC 116033) in `eastwastes`. Drop cache: 20% chance per kill.
192. Loot "High Quality Walrus Hide" (30096) from "A Walrus" (NPC 116065) in `eastwastes`. Drop cache: 14.1% chance per kill.
193. Combine in Forge (17): "Skinning Rock" (30062), "Wooly Rhino Horn" (30088), "High Quality Walrus Hide" (30096). Produces "Coldain Hunting Knife" (30137). Requires Blacksmithing, trivial 41.
194. eastwastes/"Garadain Glacierbane", hand "Silver Coldain Insignia Ring" (30133) + "Coldain Hunting Knife" (30137). Gives "Gold Coldain Insignia Ring" (30132).
195. eastwastes/"Garadain Glacierbane", hand "Gold Coldain Insignia Ring" (30132) + "Coldain Smithing Hammer" (30140). Gives "Platinum Coldain Insignia Ring" (30134).
196. eastwastes/"Garadain Glacierbane", hand "Platinum Coldain Insignia Ring" (30134) + "Head of Scarbrow" (30141). Gives "Obsidian Coldain Insignia Ring" (30268).
197. eastwastes/"Garadain Glacierbane", hand "Rodrick's Head" (1045) + "Note from Kromrif" (18084) + "Obsidian Coldain Insignia Ring" (30268). Gives "Mithril Coldain Insignia Ring" (30162).
198. eastwastes/"Dobbin Crossaxe", hand "Mithril Coldain Insignia Ring" (30162). Gives "Note from Corbin" (1047).
199. eastwastes/"Garadain Glacierbane", hand "Note from Corbin" (1047). Gives "Adamantium Coldain Insignia Ring" (30163).
200. eastwastes/"Garadain Glacierbane", hand "Adamantium Coldain Insignia Ring" (30163). Gives "Marching Orders" (1093).
201. Hand "Marching Orders" (1093) to eastwastes/"Gloradin Coldheart". Spawns "Oracle of Ry'Gorr" (116006). Loot "Dragon Scripture Tablet" (11651) from "Oracle of Ry'Gorr".
202. 1 alternative loot source(s) also yield Dragon Scripture Tablet (11651).
203. Combine in "Empty Artifact Container" (17167): "Crystal Dragon Eye" (11638), "Golden Dragon Claw" (11639), "Platinum Dragon Scale" (11640), "Dragon Scripture Tablet" (11651). Produces "Sealed Box" (28057). The combine does not fail.
204. Hand "Sealed Box" (28057) to kithicor/"Adjutant D-Kan". Spawns "General V'ghera" (20205). Loot "General's Pouch" (28013) from "General V'ghera".
205. 6 alternative loot source(s) also yield General's Pouch (28013).
206. Loot "Fleshripper" (5411) from "Solusek kobold king" in `soldungb`.
207. Loot "Painbringer" (5410) from "Kobold Champion" in `soldungb`.
208. Loot "Mithril Two-Handed Sword" (5401) from "The Froglok King" in `gukbottom`.
209. Loot "Gigantic Zweihander" (5308) from "Karg IceBear" in `everfrost`.
210. qey2hh1/"Vilnius The Small", hand "Gigantic Zweihander" (5308) + "Mithril Two-Handed Sword" (5401) + "Painbringer" (5410) + "Fleshripper" (5411). Gives "Jagged Diamond Dagger" (7506).
211. Loot "Robe of the Ishva" (1357) from "Coercer Q'ioul" in `kithicor`.
212. Loot "Robe of the Ishva" (1357) from "Jinalis Andir" in `cauldron`.
213. Loot "Robe of the Ishva" (1357) from "The Ishva Mal" in `southkarana`.
214. Loot "Robe of the Kedge" (1253) from "Kubaria" (NPC 309002) in `chambersf`. Drop cache: 100% chance per kill.
215. Loot "Robe of the Oracle" (1354) from "Oracle of K'Arnon" in `oceanoftears`.
216. Loot "Robe of the Oracle" (1354) from "Oracle of K'Arnon" in `oot`.
217. Loot "Shining Metallic Robes" (1360) from "Yendar Starpyre" (NPC 56012) in `steamfont`. Drop cache: 100% chance per kill.
218. qey2hh1/"Vilnius The Small", hand "Robe of the Kedge" (1253) + "Robe of the Oracle" (1354) + "Robe of the Ishva" (1357) + "Shining Metallic Robes" (1360). Gives "Cazic Quill" (7505).
219. highpass/"Stanos Herkanor", hand "Cazic Quill" (7505) + "Jagged Diamond Dagger" (7506) + "General's Pouch" (28013). Gives "Ragebringer" (11057).
220. highpass/"Stanos Herkanor", say "Hail". Sets `Fatestealer` to `1`.
221. Unresolved cyclic prerequisite: `Fatestealer_gal` ==1.
222. Unresolved cyclic prerequisite: `Fatestealer_gal` ==1.
223. Unresolved cyclic prerequisite: `Fatestealer_mar` ==1.
224. Unresolved cyclic prerequisite: `Fatestealer_gal` ==1.
225. Unresolved cyclic prerequisite: `Fatestealer_mar` ==1.
226. Unresolved cyclic prerequisite: `Fatestealer_lyt` ==1.
227. Loot "Signed Agreement" (10246) from "Lythe Songbird" in `freeporteast`.
228. Loot "Signed Agreement" (10246) from "Lythe Songbird" in `freportw`.
229. overthere/"Inem R'Ker", hand "Signed Agreement" (10246). Sets `Fatestealer_lyt` to `1`.
230. Loot "Signed Agreement" (10239) from "Seana Marsinger" in `gfaydark`.
231. Loot "Signed Agreement" (52416) from "Stefan Marsinger" in `gfaydark`.
232. overthere/"Inem R'Ker", hand "Signed Agreement" (10239) + "Signed Agreement" (52416). Sets `Fatestealer_mar` to `1`.
233. Loot "Signed Agreement" (10243) from "Galdorin Visigothe" in `abysmal`.
234. overthere/"Inem R'Ker", hand "Signed Agreement" (10243). Sets `Fatestealer_gal` to `1`.
235. overthere/"Inem R'Ker", hand "Signed Agreement" (10243). Sets `Fatestealer_bard` to `1`.
236. Spawns "a Teir'Dal guardian" (186190) in `hateplaneb` on event death_complete:186114.
237. Loot "Stack of Pages" (52335) from "a Teir'Dal guardian".
238. 5 alternative loot source(s) also yield Stack of Pages (52335).
239. steamfont/"Yendar Starpyre", hand "Stack of Pages" (52335). Sets `Fatestealer_page` to `1`.
240. Spawns "A Furious Magma Guardian" (278123) in `soldungc` on event_signal.
241. Loot "Crystallized Shard of Doomfire" (21339) from "A Furious Magma Guardian".
242. 1 alternative loot source(s) also yield Crystallized Shard of Doomfire (21339).
243. Loot "Foul Doomfire Brimstone" (21342) from "A Pool Of Living Lava" (NPC 278043) in `soldungc`. Drop cache: 15.97% chance per kill.
244. Loot "Igneous Rock of Doomfire" (21340) from "Typhoeus" (NPC 278069) in `soldungc`. Drop cache: 35% chance per kill.
245. Loot "Pile of Doomfire Ash" (21341) from "a Taklasinai marauder" (NPC 278075) in `soldungc`. Drop cache: 35% chance per kill.
246. Hand "Crystallized Shard of Doomfire" (21339) + "Igneous Rock of Doomfire" (21340) + "Pile of Doomfire Ash" (21341) + "Foul Doomfire Brimstone" (21342) to soldungc/"The Firewatcher". Spawns "Culthor the Gatekeeper" (278005). Loot "Smoldering Embers of Solusek" (52346) from "Culthor the Gatekeeper".
247. nedaria/"Smith Dandi", hand "Smoldering Embers of Solusek" (52346). Sets `Fatestealer_forge` to `1`.
248. Spawns "a Teir'Dal guardian" (186190) in `hateplaneb` on event death_complete:186114.
249. Loot "Soulstone of Lanys" (52337) from "a Teir'Dal guardian".
250. 5 alternative loot source(s) also yield Soulstone of Lanys (52337).
251. nedaria/"Lirprin, Head Of Affairs", hand "Soulstone of Lanys" (52337). Requires `Fatestealer_bard` ==1. Requires `Fatestealer_page` ==1. Requires `Fatestealer_forge` ==1. Gives "Fatestealer" (52347).
252. nedaria/"Lirprin, Head Of Affairs", say "Hail". Sets `Fatestealer` to `3`.
253. Loot "Polished Bone Horn" (52349) from "A Baleful Stoneworker" (NPC 301023) in `bloodfields`. Drop cache: 4% chance per kill.
254. Loot "Brass Mouthpiece" (52350) from "An Ukun Fleshhound" (NPC 301009) in `bloodfields`. Drop cache: 3.67% chance per kill.
255. Loot "Bucket Mute" (52351) from "An Ukun Fleshhound" (NPC 301009) in `bloodfields`. Drop cache: 3.67% chance per kill.
256. Loot "Thin Leather Straps" (52352) from "An Ukun Fleshhound" (NPC 301009) in `bloodfields`. Drop cache: 3.67% chance per kill.
257. Hand "Polished Bone Horn" (52349) + "Brass Mouthpiece" (52350) + "Bucket Mute" (52351) + "Thin Leather Straps" (52352) to bloodfields/"Caller Donivin". Spawns "A Reclusive Girplan" (301033). Loot "Jacinth" (10053) from "A Reclusive Girplan".
258. 55 alternative loot source(s) also yield Jacinth (10053).
259. freeporteast/"Wenden Blackhammer", hand "Black Sapphire" (10036) + "Diamond" (10037) + "Jacinth" (10053) + "Unjeweled Dragon Head Hilt" (20668). Gives "Jeweled Dragon Head Hilt" (20671).
260. Ground spawn of "Severely Damaged Dragon Head Hilt" (20669) in `timorous`.
261. Loot "Giant Sized Monocle" (20678) from "A Mountain Giant Patriarch" in `dreadlands`.
262. frontiermtns/"Mentrax Mountainbone", hand "Giant Sized Monocle" (20678). Gives "Rejesiam Ore" (20666).
263. Loot "Ball of Everliving Golem" (20677) from "Dread" in `fearplane`.
264. Loot "Ball of Everliving Golem" (20677) from "Fright" in `fearplane`.
265. Loot "Ball of Everliving Golem" (20677) from "Terror" in `fearplane`.
266. freeporteast/"Wenden Blackhammer", hand "Rejesiam Ore" (20666) + "Severely Damaged Dragon Head Hilt" (20669) + "Ball of Everliving Golem" (20677). Gives "Finely Crafted Dragon Head Hilt" (20672).
267. Combine in "Red Scabbard" (17859): "Ancient Sword Blade" (20667), "Ancient Blade" (20670), "Jeweled Dragon Head Hilt" (20671), "Finely Crafted Dragon Head Hilt" (20672). Produces "Jagged Blade of War" (10908). The combine does not fail.
268. freeporteast/"Gartrog Smitehammer", hand "Jagged Blade of War" (10908) + "Red Scabbard" (17859). Gives "Red Scabbard" (17869).
269. freeporteast/"Gartrog Smitehammer", hand "Jagged Blade of War" (10908) + "Red Scabbard" (17859). Gives "Jagged Blade of War" (66175).
270. Combine in "Red Scabbard" (17869): "Jagged Blade of War" (66175). Produces "Blade of Tactics" (66176), "Blade of Strategy" (66177). Requires Pottery. The combine does not fail.
271. Combine in "Red Scabbard" (17869): "Blade of Tactics" (66176), "Blade of Strategy" (66177). Produces "Jagged Blade of War" (66175). Requires Pottery. The combine does not fail.
272. draniksscar/"Korbuk Brimblade", say "Work". Sets `warrior_pre` to `1`.
273. Loot "Korbuk's Weapon Plans" (60285) from "The Diaku Overseer" in `potactics`.
274. draniksscar/"Korbuk Brimblade", hand "Korbuk's Weapon Plans" (60285). Sets `warrior_pre` to `2`.
275. Loot "Elegant Shank" (60286) from "Shoqui the Forgotten" in `hatesfury`.
276. draniksscar/"Korbuk Brimblade", hand "Elegant Shank" (60286). Sets `warrior_pre` to `3`.
277. Loot "Redblade Family Sword" (60287) from "Drevlon Knacknabber" in `eastkarana`.
278. freeporteast/"Kargek Redblade", hand "Redblade Family Sword" (60287). Requires `warrior_pre` set. Requires `warrior_pre` ==3. Gives "Emblazoned Champion's Hilt" (60288).
279. draniksscar/"Korbuk Brimblade", hand "Emblazoned Champion's Hilt" (60288). Sets `warrior_pre` to `4`.
280. thurgadina/"Dardek Bladewright", hand "Korbuk's Weapon Plans" (60285) + "Elegant Shank" (60286) + "Emblazoned Champion's Hilt" (60288). Sets `warrior_pre` to `5`.
281. thurgadina/"Dardek Bladewright", hand "Korbuk's Weapon Plans" (60285) + "Elegant Shank" (60286) + "Emblazoned Champion's Hilt" (60288). Requires `warrior_pre` ==4. Gives "Dardek's Forged Blade" (60292).
282. draniksscar/"Korbuk Brimblade", hand "Dardek's Forged Blade" (60292). Sets `warrior_pre` to `6`.
283. draniksscar/"Korbuk Brimblade", say "Work". Sets `warrior_epic` to `1`.
284. Kill bloodfields/"Girplan Slasher". Spawns "Girplan Devourer" (301063).
285. Loot "Decrepit Hilt" (60307) from "Girplan Devourer".
286. firiona/"Corfia Nultethen", hand "Decrepit Hilt" (60307). Sets `warrior_epic` to `9`.
287. Unresolved cyclic prerequisite: `warrior_epic_gulak` ==1.
288. firiona/"Corfia Nultethen", say "Galuk Drek". Sets `warrior_epic_veksar` to `1`.
289. burningwood/"Telin Darkforest", say "Action". Gives "Worn Note" (20472).
290. gfaydark/"Faelin Bloodbriar", hand "Worn Note" (20472). Gives "Faelin's Ring" (20446).
291. kithicor/"Giz X-Tin", hand "Faelin's Ring" (20446). Gives "Dark Metal Coin" (20447).
292. burningwood/"Telin Darkforest", hand "Dark Metal Coin" (20447). Gives "Worn Dark Metal Coin" (20448).
293. eastkarana/"Althele", hand "Worn Dark Metal Coin" (20448). Gives "Braided Grass Amulet" (20450).
294. eastkarana/"Sionae", hand "Braided Grass Amulet" (20450). Gives "Frayed Braided Grass Amulet" (20451).
295. eastkarana/"Teloa", hand "Frayed Braided Grass Amulet" (20451). Triggers `eastkarana/althele#signal:1`.
296. Starts timer `attack`.
297. Spawns "Corruptor" (15153) after `eastkarana/althele#timer:attack`.
298. Loot "Fleshbound Tome" (20452) from "Corruptor".
299. eastkarana/"Althele", hand "Fleshbound Tome" (20452). Gives "Earth Stained Note" (18959).
300. misty/"Ella Foodcrafter", hand "Earth Stained Note" (18959). Sets `shiny_tin_bowl` to `1`.
301. misty/"Ella Foodcrafter", say "Two Tasks". Requires `shiny_tin_bowl` set. Gives "Shiny Tin Bowl" (17860).
302. Hand "Shiny Tin Bowl" (17860) to hole/"Jaeil The Wretched". Spawns "Jaeil the Insane" (39154). Loot "Soulbound Hammer" (20478) from "Jaeil the Insane".
303. erudnint/"Mairee Silentone", hand "Soulbound Hammer" (20478). Gives "Dwarven Smiths Hammer" (20479).
304. Kill airplane/"An Essence Carrier". Spawns "An Essence Tamer" (71071).
305. Loot "Swirling Sphere of Color" (20494) from "An Essence Tamer".
306. erudnint/"Mairee Silentone", hand "Dwarven Smiths Hammer" (20479) + "Swirling Sphere of Color" (20494). Gives "Hammer of the Ancients" (20485).
307. kaladimb/"Kinlo Strongarm", hand "Hammer of the Ancients" (20485). Gives "Small bit of Mithril Ore" (20482).
308. kaladimb/"Kinlo Strongarm", hand "Small bit of Mithril Ore" (20482). Gives "Refined Mithril Blade" (20483).
309. Encounter starts when NPC 186201 spawns in `hateplaneb`.
310. Starts timer `popinny`.
311. Kill NPC 186158.
312. Starts timer `text`.
313. Starts timer `text2`.
314. Starts timer `spawninny`.
315. Spawns "Innoruuk" (186107) after `hateplaneb/inny#timer:spawninny`.
316. Loot "Shattered Emerald of Corruption" (20484) from "Innoruuk".
317. 1 alternative loot source(s) also yield Shattered Emerald of Corruption (20484).
318. northkarana/"Xanuusus", hand "Refined Mithril Blade" (20483) + "Shattered Emerald of Corruption" (20484). Gives "Earthcaller" (20488).
319. eastkarana/"Althele", say "Hail". Sets `ranger_epic` to `1`.
320. veksar/"Player", on enter. Sets `warrior_epic_gulak` to `1`.
321. Spawns "Decaying Lord Galuk Drek, not be in db yet" (109906) in `veksar` on enter.
322. Loot "Skeletal Tome of Galuk Drek" (60310) from "Decaying Lord Galuk Drek, not be in db yet".
323. firiona/"Corfia Nultethen", hand "Skeletal Tome of Galuk Drek" (60310). Requires `warrior_epic` set. Requires `warrior_epic` ==9. Gives "Glistening Hilt" (60311).
324. butcher/"Gridbar Galund", hand "Glistening Hilt" (60311). Requires `warrior_epic` set. Requires `warrior_epic` >=13. Gives "Carved Keg Stamp" (60318).
325. shadowhaven/"Koren Galund", hand "Carved Keg Stamp" (60318). Requires `warrior_epic` set. Requires `warrior_epic` >=13. Gives "Tube of Setting Solution" (60319).
326. butcher/"Gridbar Galund", hand "Tube of Setting Solution" (60319). Requires `warrior_epic` set. Requires `warrior_epic` >=13. Gives "Hilt of Eternal Power" (60320).

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
