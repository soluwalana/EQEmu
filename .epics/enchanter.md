# Enchanter

Steps taken from the quest graph only. **Broken** means the graph has no edge for that value or that item.

Flags with writes: `EnchPre`, `ench_epic`.

## 0. Prerequisites

Shared acquisition steps appear in the first prerequisite chain that needs them. Later sections reference that chain rather than repeating it.

### "Purifying Crystal" (52954)

1. Buy "Planar Jeweler's Kit" (17764) from "Noirin Khalen" (NPC 202084) in `poknowledge`. Base price: 1,000 copper.
2. global/"Global Player", combine recipe 19919. Sets `ench_epic` to `9`.
3. burningwood/"A Sarnak Imitator", say "Chest". Requires `ench_epic` set. Requires `ench_epic` >=3. Gives "Ornate Staff Chest" (52960).
4. Ground spawn of "Taste of Enticement" (52964) in `mistmoore`.
5. frozenshadow/"Advisor Svartmane", hand "Taste of Enticement" (52964). Gives "1st Piece of the Staff" (54289).
6. Loot "2nd Piece of the Staff" (54310) from "The Yrendan Scarab" in `pojustice`.
7. Loot "3rd Piece of the Staff" (54299) from "Chavoor the Trickster" in `vxed`.
8. Loot "3rd Piece of the Staff" (54299) from "Ikaav Firecaller" in `vxed`.
9. Loot "3rd Piece of the Staff" (54299) from "Kyv Hunter" in `vxed`.
10. Loot "3rd Piece of the Staff" (54299) from "Ukun Bloodbeast" in `vxed`.
11. Loot "3rd Piece of the Staff" (54299) from "Umbiki" in `vxed`.
12. Loot "3rd Piece of the Staff" (54299) from "misguided beludu Creque" in `vxed`.
13. **Broken:** no event trigger found for `bloodfields/war#timer:reset`.
14. Spawns "War Caller Kaavi" (301042) after `bloodfields/war#timer:reset`.
15. Loot "4th Piece of the Staff" (54284) from "War Caller Kaavi".
16. Loot "Ornate Staff Topper" (52961) from "Faleniel of Darkwater" in `sirens`.
17. Loot "All-Seeing Eye" (54293) from "All-Seeing Eye" in `mischiefplane`.
18. potranquility/"Elder Fuirstel", say "Hail". Sets `pop_cod_final` to `1`.
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
19. poknowledge/"Aid Grimel", say "Skill In Brewing". Requires `pop_cod_final` ==1. Requires `pop_cod_final` set. Gives "Portable Drink Barrel" (17179).
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
20. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
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
21. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `steamfont`.
22. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `tox`.
23. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `toxxulia`.
24. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
25. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). The combine does not fail.
26. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
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
27. Forage "Dragon Egg" (19139) in `templeveeshan`.
28. Forage "Dragon Egg" (19139) in `westwastes`.
29. Combine in "Portable Drink Barrel" (17179): "Water Flask" (13006), "Dragon Egg" (19139). Produces "Dragon Egg Oil" (9664). Requires Brewing, trivial 150.
30. Loot "Glimmering Oil" (52942) from "A Greasy Clockwork" in `poinnovation`.
31. bazaar/"Caerlyna", hand "Spell Research Kit" (93492). Gives "Spell Research Kit Token" (93667).
    - Dialogue with bazaar/"Caerlyna":
      - Player: "Hail"
        - NPC say: Greetings $name! Nice to meet you. I've started up a complimentary bag check service. Feel free to give me your weight reducing bag, and I'll give you a token in return. When you would like to get your bag back, simply return to me with your token.
        - Condition: `($text=~/hail/i)`
32. bazaar/"Caerlyna", hand "Spell Research Kit Token" (93667). Gives "Spell Research Kit" (93492).
33. Buy "Firing Sheet" (16906) from "Winn Greenbane" (NPC 5059) in `highpass`. Base price: 10 copper.
34. Combine in Pottery Wheel (21): "Water Flask" (13006), "Block of Clay" (16901). Produces "Small Block of Clay" (16900) x3. Requires Pottery, trivial 21.
35. Combine in Pottery Wheel (21): "Small Block of Clay" (16900), "Water Flask" (13006). Produces "Block of Clay" (16901). Requires Pottery, trivial 21.
36. Combine in Pottery Wheel (21): "Block of Clay" (16901), "Water Flask" (13006). Produces "Large Block of Clay" (16902). Requires Pottery, trivial 21.
37. Buy "Large Bowl Sketch" (16963) from "Min Greyeagle" (NPC 5057) in `highpass`. Base price: 760 copper.
38. Combine in Pottery Wheel (21): "Large Block of Clay" (16902), "Water Flask" (13006), "Large Bowl Sketch" (16963). Produces "Unfired Mixing Bowl" (16930). Requires Pottery, trivial 128.
39. Combine in Kiln (22): "Firing Sheet" (16906), "Unfired Mixing Bowl" (16930). Produces "Mixing Bowl" (17906). Requires Pottery, trivial 15.
40. Buy "Celestial Solvent" (9731) from "A Goblin Bartender" (NPC 11117) in `runnyeye`. Base price: 120 copper.
41. Loot "Fetid Skin" (13150) from "A Fetid Fiend" (NPC 72059) in `fearplane`. Drop cache: 35% chance per kill.
42. Loot "Scare Straw" (13152) from "A Samhain" in `fearplane`.
43. Loot "Turmoil Warts" (8331) from "A Turmoil Toad" in `fearplane`.
44. Spawns "Grimling" (154129) in `acrylia` on event_spawn.
45. Loot "Pearl" (10024) from "Grimling".
46. Alternative: Loot "Pearl" (10024) from "Grimling" (NPC 154129) in `acrylia`; trigger: acrylia/"Raidman", on event_spawn.
47. Alternative: Loot "Pearl" (10024) from "Needs Heading Validation" (NPC 154129) in `acrylia`; trigger: acrylia/"Khati Sha The Twisted", on event_signal.
48. Alternative: Loot "Pearl" (10024) from "a Grelian firelunger" (NPC 337063) in `broodlands`; trigger: broodlands/"Grel Strongboom", on event_spawn.
49. Alternative: Loot "Pearl" (10024) from "a Grelian woundmender" (NPC 337112) in `broodlands`; trigger: broodlands/"Grel Strongboom", on event_spawn.
50. Alternative: Loot "Pearl" (10024) from "a Delve spellbinder" (NPC 341091) in `delvea`; trigger: delvea/"A Drake Egg", on event_death_complete.
51. Alternative: Loot "Pearl" (10024) from "a Delve diviner" (NPC 341085) in `delvea`; trigger: delvea/"A Drake Egg", on event_death_complete.
52. Alternative: Loot "Pearl" (10024) from "a Delve evoker" (NPC 341092) in `delvea`; trigger: delvea/"A Drake Egg", on event_death_complete.
53. Alternative: Loot "Pearl" (10024) from "a Delve drake" (NPC 341087) in `delvea`; trigger: delvea/"A Drake Egg", on event_death_complete.
54. Alternative: Loot "Pearl" (10024) from "Drake Matriarch" (NPC 341149) in `delvea`; trigger: delvea/"The Drake Menace", say "Zone Death".
55. Alternative: Loot "Pearl" (10024) from "a Delve spellbinder" (NPC 341091) in `delvea`; trigger: delvea/"Lava Rock", on event_death.
56. Alternative: Loot "Pearl" (10024) from "a Delve diviner" (NPC 341085) in `delvea`; trigger: delvea/"Lava Rock", on event_death.
57. Alternative: Loot "Pearl" (10024) from "a Delve evoker" (NPC 341092) in `delvea`; trigger: delvea/"Lava Rock", on event_death.
58. Alternative: Loot "Pearl" (10024) from "a Delve drake" (NPC 341087) in `delvea`; trigger: delvea/"Lava Rock", on event_death.
59. Alternative: Loot "Pearl" (10024) from "A Tar Goo" (NPC 119122) in `wakening`; trigger: wakening/"A Tar Goo", on event_death_complete.
60. neriaka/"X-Ta Tompi", hand "Turmoil Warts" (8331) + "Pearl" (10024) + "Fetid Skin" (13150) + "Scare Straw" (13152). Gives "Words of Acquisition (Beza)" (11866).
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
61. Combine in "Mixing Bowl" (17906): "Celestial Solvent" (9731), "Words of Acquisition (Beza)" (11866). Produces "Celestial Essence" (9650). Requires Baking, trivial 15. The combine does not fail.
62. Loot "Coalesced Mana" (97042) from "Assistant Gareth" (NPC 371049) in `skylance`. Drop cache: 66.67% chance per kill.
63. Loot "White Wolf Skin" (13768) from "A Snow Wolf" in `everfrost`.
64. Loot "White Wolf Skin" (13768) from "A White Wolf" in `everfrost`.
65. Buy "Vial Sketch" (16968) from "Winn Greenbane" (NPC 5059) in `highpass`. Base price: 300 copper.
66. Combine in Pottery Wheel (21): "Water Flask" (13006), "White Wolf Skin" (13768), "Small Block of Clay" (16900), "Vial Sketch" (16968). Produces "Unfired Poison Vial" (16885). Requires Pottery, trivial 148.
67. Buy "High Quality Firing Sheet" (16908) from "Winn Greenbane" (NPC 5059) in `highpass`. Base price: 40 copper.
68. Combine in Kiln (22): "Unfired Poison Vial" (16885), "High Quality Firing Sheet" (16908). Produces "Poison Vial" (16965). Requires Pottery, trivial 17.
69. Spawns "Pxet Elite Blademaster" (284039) in `ferubi` on event_signal.
70. Loot "Broken Sword Blade" (67521) from "Pxet Elite Blademaster".
71. Spawns "Pxet Elite Spearmaster" (284091) in `ferubi` on event_signal.
72. Loot "Jagged Spear Tip" (67522) from "Pxet Elite Spearmaster".
73. Spawns "Pxet Elite Brawler" (284088) in `ferubi` on event_signal.
74. Loot "Tarnished Knuckles" (67523) from "Pxet Elite Brawler".
75. Spawns "Pxet Elite Hammermaster" (284090) in `ferubi` on event_signal.
76. Loot "Chipped Hammer Head" (67524) from "Pxet Elite Hammermaster".
77. Hand "Broken Sword Blade" (67521) + "Jagged Spear Tip" (67522) + "Tarnished Knuckles" (67523) + "Chipped Hammer Head" (67524) to ferubi/"Smith Rondo". Spawns "Master's Apprentice" (284093). Loot "Ruby" (10035) from "Master's Apprentice".
78. Alternative: Loot "Ruby" (10035) from "The Broodqueen" (NPC 337254) in `broodlands`; trigger: broodlands/"Brood Drone", on event_death_complete.
79. Alternative: Loot "Ruby" (10035) from "A parasitic murkglider" (NPC 303121) in `causeway`; trigger: causeway/"Withering Murkglider", on event_hp.
80. Alternative: Loot "Ruby" (10035) from "a Reanimated Berserker" (NPC 103093) in `chardok`; trigger: chardok/"The Earth", on enter.
81. Alternative: Loot "Ruby" (10035) from "a Delve spellbinder" (NPC 341091) in `delvea`; trigger: delvea/"A Drake Egg", on event_death_complete.
82. Alternative: Loot "Ruby" (10035) from "a Delve diviner" (NPC 341085) in `delvea`; trigger: delvea/"A Drake Egg", on event_death_complete.
83. Alternative: Loot "Ruby" (10035) from "a Delve evoker" (NPC 341092) in `delvea`; trigger: delvea/"A Drake Egg", on event_death_complete.
84. Alternative: Loot "Ruby" (10035) from "a Delve drake" (NPC 341087) in `delvea`; trigger: delvea/"A Drake Egg", on event_death_complete.
85. Alternative: Loot "Ruby" (10035) from "Drake Matriarch" (NPC 341149) in `delvea`; trigger: delvea/"The Drake Menace", say "Zone Death".
86. Alternative: Loot "Ruby" (10035) from "a Delve spellbinder" (NPC 341091) in `delvea`; trigger: delvea/"Lava Rock", on event_death.
87. Alternative: Loot "Ruby" (10035) from "a Delve diviner" (NPC 341085) in `delvea`; trigger: delvea/"Lava Rock", on event_death.
88. Alternative: Loot "Ruby" (10035) from "a Delve evoker" (NPC 341092) in `delvea`; trigger: delvea/"Lava Rock", on event_death.
89. Alternative: Loot "Ruby" (10035) from "a Delve drake" (NPC 341087) in `delvea`; trigger: delvea/"Lava Rock", on event_death.
90. Alternative: Loot "Ruby" (10035) from "Master's Apprentice" (NPC 284094) in `ferubi`; trigger: ferubi/"Smith Rondo", hand "Broken Sword Blade" (67521) + "Jagged Spear Tip" (67522) + "Tarnished Knuckles" (67523) + "Chipped Hammer Head" (67524).
91. Alternative: Loot "Ruby" (10035) from "Master's Apprentice" (NPC 284095) in `ferubi`; trigger: ferubi/"Smith Rondo", hand "Broken Sword Blade" (67521) + "Jagged Spear Tip" (67522) + "Tarnished Knuckles" (67523) + "Chipped Hammer Head" (67524).
92. Alternative: Loot "Ruby" (10035) from "Master's Apprentice" (NPC 284096) in `ferubi`; trigger: ferubi/"Smith Rondo", hand "Broken Sword Blade" (67521) + "Jagged Spear Tip" (67522) + "Tarnished Knuckles" (67523) + "Chipped Hammer Head" (67524).
93. Alternative: Loot "Ruby" (10035) from "Pxet Elite Spearmaster" (NPC 284091) in `ferubi`; trigger: ferubi/"Event Spawner", on event_signal.
94. Alternative: Loot "Ruby" (10035) from "A Soldier Of Madness" (NPC 163185) in `griegsend`; trigger: griegsend/"Trapman", on event_combat.
95. Alternative: Loot "Ruby" (10035) from "A Shadowy Figure" (NPC 163190) in `griegsend`; trigger: griegsend/"Trapman Two", on event_combat.
96. Alternative: Loot "Ruby" (10035) from "Servant Of The Magistrate" (NPC 163189) in `griegsend`; trigger: griegsend/"Trapman Two", on event_combat.
97. Alternative: Loot "Ruby" (10035) from "A Dragorn Sycophant" (NPC 335023) in `harbingers`; trigger: harbingers/"Attendant Spawner", on event_spawn.
98. Alternative: Loot "Ruby" (10035) from "Prison Guard Talkor" (NPC 245290) in `rujd`; trigger: rujd/"Rujd", hand "Heavy Orcish Prison Key" (59571).
99. Alternative: Loot "Ruby" (10035) from "Warden" (NPC 245296) in `rujd`; trigger: rujd/"Rujd", say "Zs Timer".
100. Alternative: Loot "Ruby" (10035) from "Shaman" (NPC 245284) in `rujd`; trigger: rujd/"Rujd", say "Zs Timer".
101. Alternative: Loot "Ruby" (10035) from "A Spirit Keeper" (NPC 338169) in `stillmoona`; trigger: stillmoona/"The Keeper Of Strength", hand "Scroll of the Ox" (49007) + "Scroll of the Boar" (49008) + "Scroll of the Dragon" (49009) + "Scroll of the Tiger" (49010).
102. Alternative: Loot "Ruby" (10035) from "Dark Reign Contact" (NPC 338422) in `stillmoona`; trigger: stillmoona/"Best Laid Plans", hand "Temple Plans" (36214).
103. Alternative: Loot "Ruby" (10035) from "Dark Reign assistant" (NPC 338421) in `stillmoona`; trigger: stillmoona/"Best Laid Plans", hand "Temple Plans" (36214).
104. Alternative: Loot "Ruby" (10035) from "Dark Reign Contact" (NPC 338422) in `stillmoona`; trigger: stillmoona/"Best Laid Plans", say "Player Loot".
105. Alternative: Loot "Ruby" (10035) from "A Drake Conspirator" (NPC 338424) in `stillmoona`; trigger: stillmoona/"Scales Of Justice", hand "Small sack of Koi Food" (36215).
106. Alternative: Loot "Ruby" (10035) from "Nethran" (NPC 338404) in `stillmoona`; trigger: stillmoona/"Sickness Of The Spirit", say "Wave Proximity".
107. Alternative: Loot "Ruby" (10035) from "A Goblin Poison Master" (NPC 338425) in `stillmoona`; trigger: stillmoona/"Tea For Thy Master", say "Hail".
108. Alternative: Loot "Ruby" (10035) from "A Poison Assistant" (NPC 338384) in `stillmoona`; trigger: stillmoona/"Tea For Thy Master", say "Hail".
109. Alternative: Loot "Ruby" (10035) from "A Goblin Poison Master" (NPC 338425) in `stillmoona`; trigger: stillmoona/"Tea For Thy Master", say "Tea Master Say".
110. Alternative: Loot "Ruby" (10035) from "A Poison Assistant" (NPC 338384) in `stillmoona`; trigger: stillmoona/"Tea For Thy Master", say "Tea Master Say".
111. Alternative: Loot "Ruby" (10035) from "Lair Mistress" (NPC 339296) in `stillmoonb`; trigger: stillmoonb/"Death Comes Swiftly", say "Zone Death".
112. Alternative: Loot "Ruby" (10035) from "a Goblin Guard" (NPC 339114) in `stillmoonb`; trigger: stillmoonb/"Drake Eggs", say "Drake Death".
113. Alternative: Loot "Ruby" (10035) from "Pixtt Riel Tavas" (NPC 298032) in `tacvi`; trigger: tacvi/"Zone Status", say "Spawn Prt".
114. Alternative: Loot "Ruby" (10035) from "Zun'Muram Mordl Delt" (NPC 298020) in `tacvi`; trigger: tacvi/"Zone Status", say "Spawn Zmmd".
115. Alternative: Loot "Ruby" (10035) from "A Blizzard Seeker" (NPC 340029) in `thundercrest`; trigger: thundercrest/"An End To The Storms", say "Yar Timer".
116. Alternative: Loot "Ruby" (10035) from "Furious Sentry" (NPC 340006) in `thundercrest`; trigger: thundercrest/"The Creator", say "Zone Death".
117. Alternative: Loot "Ruby" (10035) from "Creator Kro'val" (NPC 340007) in `thundercrest`; trigger: thundercrest/"The Creator", say "Player Cast On".
118. Alternative: Loot "Ruby" (10035) from "A Stone Sentinel" (NPC 340521) in `thundercrest`; trigger: thundercrest/"The Creator", say "Player Cast On".
119. Alternative: Loot "Ruby" (10035) from "A Ra'Tuk Decimator" (NPC 289004) in `tipt`; trigger: tipt/"Zone Status", say "Spawn Keyroom".
120. Alternative: Loot "Ruby" (10035) from "a Broken Skull treasurer" (NPC 226208) in `torgiran`; trigger: torgiran/"The Room", on event_signal.
121. Alternative: Loot "Ruby" (10035) from "A Frenzied Luggald Abomination" (NPC 226214) in `torgiran`; trigger: torgiran/"A Water Spirit", say "Frenzy".
122. Alternative: Loot "Ruby" (10035) from "A Berserk Luggald Abomination" (NPC 226215) in `torgiran`; trigger: torgiran/"A Water Spirit", say "Berserk".
123. Alternative: Loot "Ruby" (10035) from "A Furious Luggald Abomination" (NPC 226216) in `torgiran`; trigger: torgiran/"A Water Spirit", say "Fury".
124. Alternative: Loot "Ruby" (10035) from "An Enraged Luggald Abomination" (NPC 226217) in `torgiran`; trigger: torgiran/"A Water Spirit", say "Rage".
125. Alternative: Loot "Ruby" (10035) from "A Trusik Ritualist" (NPC 292010) in `uqua`; trigger: uqua/"Gas Chamber 1", on event_signal.
126. Alternative: Loot "Ruby" (10035) from "A Trusik Stalker" (NPC 292007) in `uqua`; trigger: uqua/"Gas Chamber 1", on event_signal.
127. Alternative: Loot "Ruby" (10035) from "A Trusik Anchorite" (NPC 292029) in `uqua`; trigger: uqua/"Trap Uqua 1", on enter.
128. Alternative: Loot "Ruby" (10035) from "A Trusik Ritualist" (NPC 292005) in `uqua`; trigger: uqua/"Trap Uqua 1", on enter.
129. Alternative: Loot "Ruby" (10035) from "A Trusik Stalker" (NPC 292006) in `uqua`; trigger: uqua/"Trap Uqua 1", on enter.
130. Alternative: Loot "Ruby" (10035) from "A Trusik Summoner" (NPC 292002) in `uqua`; trigger: uqua/"Trap Uqua 1", on enter.
131. Alternative: Loot "Ruby" (10035) from "A Trusik Anchorite" (NPC 292029) in `uqua`; trigger: uqua/"Trap Uqua 2", on enter.
132. Alternative: Loot "Ruby" (10035) from "A Trusik Ritualist" (NPC 292005) in `uqua`; trigger: uqua/"Trap Uqua 2", on enter.
133. Alternative: Loot "Ruby" (10035) from "A Trusik Stalker" (NPC 292006) in `uqua`; trigger: uqua/"Trap Uqua 2", on enter.
134. Alternative: Loot "Ruby" (10035) from "A Trusik Summoner" (NPC 292002) in `uqua`; trigger: uqua/"Trap Uqua 2", on enter.
135. Alternative: Loot "Ruby" (10035) from "A Trusik Anchorite" (NPC 292029) in `uqua`; trigger: uqua/"Trap Uqua 3", on enter.
136. Alternative: Loot "Ruby" (10035) from "A Trusik Ritualist" (NPC 292005) in `uqua`; trigger: uqua/"Trap Uqua 3", on enter.
137. Alternative: Loot "Ruby" (10035) from "A Trusik Stalker" (NPC 292006) in `uqua`; trigger: uqua/"Trap Uqua 3", on enter.
138. Alternative: Loot "Ruby" (10035) from "A Trusik Summoner" (NPC 292002) in `uqua`; trigger: uqua/"Trap Uqua 3", on enter.
139. Alternative: Loot "Ruby" (10035) from "A Trusik Anchorite" (NPC 292029) in `uqua`; trigger: uqua/"Trap Uqua 4", on enter.
140. Alternative: Loot "Ruby" (10035) from "A Trusik Ritualist" (NPC 292005) in `uqua`; trigger: uqua/"Trap Uqua 4", on enter.
141. Alternative: Loot "Ruby" (10035) from "A Trusik Stalker" (NPC 292006) in `uqua`; trigger: uqua/"Trap Uqua 4", on enter.
142. Alternative: Loot "Ruby" (10035) from "A Trusik Summoner" (NPC 292002) in `uqua`; trigger: uqua/"Trap Uqua 4", on enter.
143. Alternative: Loot "Ruby" (10035) from "A Trusik Anchorite" (NPC 292029) in `uqua`; trigger: uqua/"Trap Uqua 5", on enter.
144. Alternative: Loot "Ruby" (10035) from "A Trusik Ritualist" (NPC 292005) in `uqua`; trigger: uqua/"Trap Uqua 5", on enter.
145. Alternative: Loot "Ruby" (10035) from "A Trusik Stalker" (NPC 292006) in `uqua`; trigger: uqua/"Trap Uqua 5", on enter.
146. Alternative: Loot "Ruby" (10035) from "A Trusik Summoner" (NPC 292002) in `uqua`; trigger: uqua/"Trap Uqua 5", on enter.
147. Alternative: Loot "Ruby" (10035) from "A Trusik Anchorite" (NPC 292029) in `uqua`; trigger: uqua/"Trap Uqua 6", on enter.
148. Alternative: Loot "Ruby" (10035) from "A Trusik Ritualist" (NPC 292005) in `uqua`; trigger: uqua/"Trap Uqua 6", on enter.
149. Alternative: Loot "Ruby" (10035) from "A Trusik Stalker" (NPC 292006) in `uqua`; trigger: uqua/"Trap Uqua 6", on enter.
150. Alternative: Loot "Ruby" (10035) from "A Trusik Summoner" (NPC 292002) in `uqua`; trigger: uqua/"Trap Uqua 6", on enter.
151. Alternative: Loot "Ruby" (10035) from "A Trusik Anchorite" (NPC 292029) in `uqua`; trigger: uqua/"Trap Uqua 7", on enter.
152. Alternative: Loot "Ruby" (10035) from "A Trusik Ritualist" (NPC 292005) in `uqua`; trigger: uqua/"Trap Uqua 7", on enter.
153. Alternative: Loot "Ruby" (10035) from "A Trusik Stalker" (NPC 292006) in `uqua`; trigger: uqua/"Trap Uqua 7", on enter.
154. Alternative: Loot "Ruby" (10035) from "A Trusik Summoner" (NPC 292002) in `uqua`; trigger: uqua/"Trap Uqua 7", on enter.
155. Alternative: Loot "Ruby" (10035) from "A Trusik Anchorite" (NPC 292029) in `uqua`; trigger: uqua/"Trap Uqua 8", on enter.
156. Alternative: Loot "Ruby" (10035) from "A Trusik Ritualist" (NPC 292005) in `uqua`; trigger: uqua/"Trap Uqua 8", on enter.
157. Alternative: Loot "Ruby" (10035) from "A Trusik Stalker" (NPC 292006) in `uqua`; trigger: uqua/"Trap Uqua 8", on enter.
158. Alternative: Loot "Ruby" (10035) from "A Trusik Summoner" (NPC 292002) in `uqua`; trigger: uqua/"Trap Uqua 8", on enter.
159. Alternative: Loot "Ruby" (10035) from "Master's Apprentice" (NPC 284093) in `ferubi`; trigger: ferubi/"Weapon Master Vtiink Vzaan", on timer repop1.
160. Alternative: Loot "Ruby" (10035) from "Master's Apprentice" (NPC 284094) in `ferubi`; trigger: ferubi/"Weapon Master Vtiink Vzaan", on timer repop2.
161. Alternative: Loot "Ruby" (10035) from "Master's Apprentice" (NPC 284095) in `ferubi`; trigger: ferubi/"Weapon Master Vtiink Vzaan", on timer repop3.
162. Alternative: Loot "Ruby" (10035) from "Master's Apprentice" (NPC 284096) in `ferubi`; trigger: ferubi/"Weapon Master Vtiink Vzaan", on timer repop4.
163. Alternative: Loot "Ruby" (10035) from "a blade of the First" (NPC 249090) in `guke`; trigger: guke/"Guke", on timer adds_on_granos.
164. Alternative: Loot "Ruby" (10035) from "A Risen Acolyte" (NPC 249152) in `guke`; trigger: guke/"Guke", on timer spawn_adds.
165. Alternative: Loot "Ruby" (10035) from "A Risen Champion" (NPC 249154) in `guke`; trigger: guke/"Guke", on timer spawn_adds.
166. Alternative: Loot "Ruby" (10035) from "A Risen Death Knight" (NPC 249157) in `guke`; trigger: guke/"Guke", on timer spawn_adds.
167. Alternative: Loot "Ruby" (10035) from "A Risen Deceiver" (NPC 249161) in `guke`; trigger: guke/"Guke", on timer spawn_adds.
168. Alternative: Loot "Ruby" (10035) from "A Risen Fire Caller" (NPC 249164) in `guke`; trigger: guke/"Guke", on timer spawn_adds.
169. Alternative: Loot "Ruby" (10035) from "A Risen Partisan" (NPC 249169) in `guke`; trigger: guke/"Guke", on timer spawn_adds.
170. Alternative: Loot "Ruby" (10035) from "A Risen Stalker" (NPC 249178) in `guke`; trigger: guke/"Guke", on timer spawn_adds.
171. Alternative: Loot "Ruby" (10035) from "A Risen Witch Doctor" (NPC 249183) in `guke`; trigger: guke/"Guke", on timer spawn_adds.
172. Alternative: Loot "Ruby" (10035) from "A Malicious Force" (NPC 249128) in `guke`; trigger: guke/"Guke", on timer depop.
173. Alternative: Loot "Ruby" (10035) from "A Moaning Banshee" (NPC 186193) in `hateplaneb`; trigger: hateplaneb/"Maestro", on event signal:186111.
174. Alternative: Loot "Ruby" (10035) from "A Screeching Banshee" (NPC 186192) in `hateplaneb`; trigger: hateplaneb/"Maestro", on event signal:186111.
175. Alternative: Loot "Ruby" (10035) from "A Wailing Banshee" (NPC 186194) in `hateplaneb`; trigger: hateplaneb/"Maestro", on event signal:186111.
176. Alternative: Loot "Ruby" (10035) from "NPC: ##Pixtt Priest Summoner" (NPC 293220) in `kodtaz`; trigger: kodtaz/"Totd", on event death_complete:293210.
177. Alternative: Loot "Ruby" (10035) from "Zun'Muram Mordl Delt" (NPC 298020) in `tacvi`; trigger: tacvi/"Zmmd", on timer wipecheck.
178. Alternative: Loot "Ruby" (10035) from "A Blizzard Seeker" (NPC 340029) in `thundercrest`; trigger: thundercrest/"An End To The Storms", on timer Seekers.
179. Alternative: Loot "Ruby" (10035) from "Tiv Prayer Chanter" (NPC 297066) in `txevu`; trigger: txevu/"Highpriest", on event spawn:297199.
180. Alternative: Loot "Ruby" (10035) from "Tiv Prayer Chanter" (NPC 297062) in `txevu`; trigger: txevu/"Highpriest", on event spawn:297061.
181. Alternative: Loot "Ruby" (10035) from "Tiv Prayer Chanter" (NPC 297063) in `txevu`; trigger: txevu/"Highpriest", on event spawn:297197.
182. Alternative: Loot "Ruby" (10035) from "Tiv Prayer Chanter" (NPC 297064) in `txevu`; trigger: txevu/"Highpriest", on event spawn:297059.
183. Alternative: Loot "Ruby" (10035) from "Tiv Prayer Chanter" (NPC 297065) in `txevu`; trigger: txevu/"Highpriest", on event spawn:297057.
184. Alternative: Loot "Ruby" (10035) from "A Murk Hatchling" (NPC 300084) in `wallofslaughter`; trigger: wallofslaughter/"A Quivering Egg", on timer hatch.
185. Combine in "Spell Research Kit" (93492): "Celestial Essence" (9650), "Coalesced Mana" (97042), "Poison Vial" (16965), "Ruby" (10035). Produces "Vial of Purified Mana" (10254). Requires Research, trivial 200.
186. Forage "Glow Lichen" (14925) in `nektulos`.
187. Loot "Essence of Sunlight" (22527) from "A Faerie Dragon" (NPC 119073) in `wakening`. Drop cache: 55% chance per kill.
188. Ground spawn of "Abysmal Moonwater" (54298) in `abysmal`.
189. Combine in Brew Barrel (19): "Vial of Purified Mana" (10254), "Glow Lichen" (14925), "Essence of Sunlight" (22527), "Abysmal Moonwater" (54298). Produces "Glowing Concoction" (52943). Requires Brewing, trivial 116.
190. Buy "Medicine Bag" (17901) from "Rendallen Ironforge" (NPC 2071) in `qeynos2`. Base price: 1,000 copper.
191. Buy "Glaze Lacquer" (29355) from "Elisha Dirtyshoes" (NPC 202134) in `poknowledge`. Base price: 8,000 copper.
192. Buy "Prism Shard" (65469) from "Elisha Dirtyshoes" (NPC 202134) in `poknowledge`. Base price: 5,000 copper.
193. Combine in "Medicine Bag" (17901): "Glaze Lacquer" (29355), "Prism Shard" (65469). Produces "Prismatic Dye" (65472). Requires Alchemy, trivial 54.
194. Combine in Brew Barrel (19): "Dragon Egg Oil" (9664), "Glimmering Oil" (52942), "Glowing Concoction" (52943), "Prismatic Dye" (65472). Produces "Incandescent Oil" (57924). Requires Brewing, trivial 116. The combine does not fail.
195. Loot "Dragon Boneshard" (65574) from "A Curate" (NPC 109068) in `veksar`. Drop cache: 10% chance per kill.
196. Hand "Dragon Boneshard" (65574) to veksar/"Spirit Of Garudon". Spawns "Garudon" (109107). Loot "Garudon's Statue" (52941) from "Garudon".
197. lakeofillomen/"A Bloodgill Mimic", hand "Garudon's Statue" (52941). Sets `EnchPre` to `1`.
198. Loot "Crumbling Tome" (54313) from "A Shissar Lorekeeper" in `ssratemple`.
199. ssratemple/"A Soriz Imitator", hand "Crumbling Tome" (54313). Requires `EnchPre` ==1. Gives "Illegible Tome" (52947).
    - Dialogue with ssratemple/"A Soriz Imitator":
      - Player: "Are You Aida"
        - NPC say: 'How do you know my name?
        - Condition: `(e.other:Class() == "Enchanter")`
        - Condition: `(e.message:findi("are you aida") and qglobals["EnchPre"] == "1")`
      - Player: "Bloodgill Mimic" (link: conversation sequence)
        - NPC say: 'Then he has sent you has he... I wish that I had fared better in these years of study. It is true that I have learned many things, but there is one tome most closely guarded that I have yet to see.'
        - Condition: `(e.other:Class() == "Enchanter")`
        - Condition: `(e.message:findi("bloodgill mimic") and qglobals["EnchPre"] == "1")`
      - Player: "What Tome" (link: explicit mention)
        - NPC say: 'I believe it contains the very knowledge our master seeks. In fact, I am sure of it. You must obtain it, I have tried and tried and failed at every juncture.'
        - Condition: `(e.other:Class() == "Enchanter")`
        - Condition: `(e.message:findi("what tome") and qglobals["EnchPre"] == "1")`
      - Player: "Where" (link: conversation sequence)
        - NPC say: 'It is held by a Shissar here in the temple. I believe he wanders in order to think, that would be the best time to retrieve it'
        - Condition: `(e.other:Class() == "Enchanter")`
        - Condition: `(e.message:findi("where") and qglobals["EnchPre"] == "1")`
200. akanon/"Rilgor Plegnog", say "Insidious". Gives "Compacting Satchel" (54303).
    - Dialogue with akanon/"Rilgor Plegnog":
      - Player: "Mechanical Pen"
        - NPC say: Why do you want one of those contraptions. You will spend more time repairing it then you will writing with it. But if you insist on getting one, you are going to have to do a small favor.
        - NPC emote: tugs at your robe and grins evilly. 'Mighty nice outfit you have there. Sure beats these drab robes us three are wearing. Hmm...my favorite color is purple, in fact a shiny metallic purple would do nicely. How bad did you want that pen?'
        - Condition: `(e.message:findi("mechanical pen"))`
      - Player: "Trades" (link: external event mention)
        - Prompted by `event_trade`:
          - NPC say: It's always good to see new blood eager to learn teh dark art of mind control. Please take this robe as a symbolization of loyalty to this house. Once you are ready to begin your training please make sure that you see Tilkzog Mournunder, he can assist you in developing your hunting and gathering skills. Return to me when you have become more experienced in our art, I will be able to further instruct you on how to progress through your early ranks, as well as in some of the various [trades] you will have available to you.
          - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 18703}))`
        - NPC say: I thought you might be one who was interested in the various different trades, but which one would suit you? Ahh, alas, it would be better to let you decide for yourself, perhaps you would even like to master them all! That would be quite a feat. Well, lets not get ahead of ourselves, here, take this book. When you have finished reading it, ask me for the [second book], and I shall give it to you. Inside them you will find the most basic recipes for each trade. These recipes are typically used as a base for more advanced crafting, for instance, if you wished to be a smith, one would need to find some ore and smelt it into something usable. Good luck!
        - Condition: `(e.message:findi("trades"))`
        - Gives Tradeskill Basics : Volume I (51121).
      - Player: "Second Book" (link: explicit mention)
        - NPC say: Here is the second volume of the book you requested, may it serve you well!
        - Condition: `(e.message:findi("second book"))`
        - Gives Tradeskill Basics : Volume II (51122).
      - Player: "Hail" (link: conversation sequence)
        - NPC say: Oh, what is it now. Can't you see that I am a very busy gnome?
        - Condition: `(e.message:findi("hail"))`
      - Player: "Translating Device"
        - NPC say: Rilgor Plegnog rubs his chin thoughtfully. 'A translating device? Now that is something rather complicated. It would take all of my skill as both a tinkerer and an enchanter. This is not the sort of thing I would do for nothing, no no no. I would need some sort of [compensation] for a project like that!'
        - Condition: `(e.message:findi("translating device") and e.other:HasItem(52947))`
      - Player: "Compensation" (link: explicit mention)
        - NPC say: 'Hmm, well now that you mention it, some fine silks might do rather nicely. Oh yes, indeed. I do love my robe ever so much, but well, the rest of me could use some sprucing up. I always did feel a bit left out that I never picked up some of that nice Insidious
        - Condition: `(e.message:findi("compensation") and e.other:HasItem(52947))`
      - Player: "Insidious" (link: explicit mention)
        - NPC say: 'Yes indeed, it is lovely. Fetch me a set and I just might consider undertaking that translating device of yours. Take this sack. I am quite interested in the halo, sleeves, manacle, gloves, pantaloons, and slippers. As I said, my robe is still serving me quite nicely, so no need to worry about that.'
        - Condition: `(e.message:findi("insidious") and e.other:HasItem(52947))`
        - Gives Compacting Satchel (54303).
201. Loot "Fine Insidious Halo" (54384) from "A Forsaken Revenant" (NPC 186146) in `hateplaneb`. Drop cache: 2% chance per kill.
202. Loot "Fine Insidious Sleeves" (54385) from "A Forsaken Revenant" (NPC 186146) in `hateplaneb`. Drop cache: 2.08% chance per kill.
203. Loot "Fine Insidious Manacle" (54386) from "A Forsaken Revenant" (NPC 186146) in `hateplaneb`. Drop cache: 2.09% chance per kill.
204. Loot "Fine Insidious Gloves" (54387) from "A Forsaken Revenant" (NPC 186146) in `hateplaneb`. Drop cache: 2.24% chance per kill.
205. Loot "Fine Insidious Pantaloons" (54388) from "A Forsaken Revenant" (NPC 186146) in `hateplaneb`. Drop cache: 2.23% chance per kill.
206. Loot "Fine Insidious Slippers" (54389) from "A Forsaken Revenant" (NPC 186146) in `hateplaneb`. Drop cache: 2.07% chance per kill.
207. Combine in "Compacting Satchel" (54303): "Fine Insidious Halo" (54384), "Fine Insidious Sleeves" (54385), "Fine Insidious Manacle" (54386), "Fine Insidious Gloves" (54387), "Fine Insidious Pantaloons" (54388), "Fine Insidious Slippers" (54389). Produces "Insidious Bundle" (54317). The combine does not fail.
208. akanon/"Rilgor Plegnog", hand "Insidious Bundle" (54317). Gives "Gnomish Translating Device" (52945).
209. burningwood/"A Sarnak Imitator", hand "Gnomish Translating Device" (52945) + "Illegible Tome" (52947). Sets `EnchPre` to `2`.
210. burningwood/"A Sarnak Imitator", say "Hail". Sets `ench_epic` to `1`.
211. burningwood/"A Sarnak Imitator", say "Prepared". Requires `ench_epic` set. Requires `ench_epic` >=1. Gives "Tattered Illegible Tome" (57918).
212. Ground spawn of "Cryptic Page" (52933) in `charasis`.
213. Ground spawn of "Cryptic Page" (52934) in `sebilis`.
214. Ground spawn of "Cryptic Page" (52935) in `cazicthule`.
215. Ground spawn of "Cryptic Page" (52936) in `crystal`.
216. Ground spawn of "Cryptic Page" (52937) in `skyshrine`.
217. Ground spawn of "Cryptic Page" (52938) in `velketor`.
218. Ground spawn of "Cryptic Page" (52939) in `nadox`.
219. Ground spawn of "Cryptic Page" (54308) in `najena`.
220. Ground spawn of "Cryptic Page" (57916) in `fungusgrove`.
221. Ground spawn of "Cryptic Page" (57923) in `oot`.
222. Combine in "Tattered Illegible Tome" (57918): "Cryptic Page" (52933), "Cryptic Page" (52934), "Cryptic Page" (52935), "Cryptic Page" (52936), "Cryptic Page" (52937), "Cryptic Page" (52938), "Cryptic Page" (52939), "Cryptic Page" (54308), "Cryptic Page" (57916), "Cryptic Page" (57923). Produces "Complete Illegible Tome" (54267). The combine does not fail.
223. burningwood/"A Sarnak Imitator", hand "Complete Illegible Tome" (54267). Sets `ench_epic` to `2`.
224. poknowledge/"Grand Librarian Maelin", say "Jeb Lumsed Sent Me". Requires `ench_epic` ==2. Gives "Note to Lobaen" (52950).
    - Dialogue with poknowledge/"Grand Librarian Maelin":
      - Player: "Trick Or Treat"
        - NPC say: Ah, here you go. Fresh from the Sugar Assembalage 2000.
        - Condition: `(eq.is_task_active(500220))`
        - Condition: `(e.message:findi("trick or treat"))`
        - Gives Sand (84091).
        - Gives Chunk of Coal (84092).
        - Gives Pocket Lint (84093).
        - Gives Jawbreaker (84087).
      - Player: "Hail" (link: conversation sequence)
        - NPC say: The Quintessence! Oh my this is amazing! I have come into contact with Chronographer Muon in the realm of innovation. Go to him, show him you have the power to activate machine. I shall meet you there, this I must see!
        - Condition: `(e.other:HasItem(29165))`
        - Condition: `(e.message:findi("hail"))`
      - Player: "Hail" (link: conversation sequence)
        - NPC say: 'Welcome back my friends. I assure you that I have been studying the Cipher of Druzzil very diligently. Did you happen to find any [lore] or [information] that I could look at?'
        - Condition: `(qglobals["pop_hohb_marr"] == "1" and qglobals["pop_bot_agnarr"] == "1" and qglobals["pop_pon_hedge_jezith"] == "1" and qglobals["pop_pon_construct"] == "1" and qglobals["pop_ponb_terris"] == "1"	and qglobals["pop_ponb_poxbourne"] == "1" and qglobals["pop_pod_alder_fuirstel"] == "1" and qglobals["pop_pod_grimmus_planar_projection"] == "1" and qglobals["pop_pod_elder_fuirstel"] == "1" and qglobals["pop_poj_mavuin"] == "1" and qglobals["pop_poj_tribunal"] == "1" and qglobals["pop_poj_valor_storms"] == "1" and qglobals["pop_pov_aerin_dar"] == "1" and qglobals["pop_pos_askr_the_lost"] == "3" and qglobals["pop_pos_askr_the_lost_final"] == "1" and qglobals["pop_cod_preflag"] == "1" and qglobals["pop_cod_bertox"] == "1" and qglobals["pop_cod_final"] == "1" and qglobals["pop_pot_shadyglade"] == "1" and qglobals["pop_pot_saryrn"] == "1" and qglobals["pop_pot_saryrn_final"] == "1" and qglobals["pop_hoh_faye"] == "1" and qglobals["pop_hoh_trell"] == "1" and qglobals["pop_hoh_garn"] == "1" and qglobals["pop_tactics_ralloz"] == "1")`
        - Condition: `(e.message:findi("hail"))`
      - Player: "Lore" (link: explicit mention)
        - NPC say: 'A parchment of Rallos'? Let me read it, it says that Rallos was not alone in his feelings about mortals. Solusek Ro also holds stake in the war to be led on Norrath. Not only this but he is channeling power from his father's plane into his own. He is taking that power and intensifying it through an artifact of great power, and then focusing it onto one point. It is a detailed as a crystal that burns with all the powers of the plane of fire. It is said to have the ability to turn the face of Norrath into a charred wasteland. They plan for a manaetic behemoth to carry and deposit it upon Norrath. You must stop these plans, you must stop Solusek!'
        - Condition: `(qglobals["pop_hohb_marr"] == "1" and qglobals["pop_bot_agnarr"] == "1" and qglobals["pop_pon_hedge_jezith"] == "1" and qglobals["pop_pon_construct"] == "1" and qglobals["pop_ponb_terris"] == "1"	and qglobals["pop_ponb_poxbourne"] == "1" and qglobals["pop_pod_alder_fuirstel"] == "1" and qglobals["pop_pod_grimmus_planar_projection"] == "1" and qglobals["pop_pod_elder_fuirstel"] == "1" and qglobals["pop_poj_mavuin"] == "1" and qglobals["pop_poj_tribunal"] == "1" and qglobals["pop_poj_valor_storms"] == "1" and qglobals["pop_pov_aerin_dar"] == "1" and qglobals["pop_pos_askr_the_lost"] == "3" and qglobals["pop_pos_askr_the_lost_final"] == "1" and qglobals["pop_cod_preflag"] == "1" and qglobals["pop_cod_bertox"] == "1" and qglobals["pop_cod_final"] == "1" and qglobals["pop_pot_shadyglade"] == "1" and qglobals["pop_pot_saryrn"] == "1" and qglobals["pop_pot_saryrn_final"] == "1" and qglobals["pop_hoh_faye"] == "1" and qglobals["pop_hoh_trell"] == "1" and qglobals["pop_hoh_garn"] == "1" and qglobals["pop_tactics_ralloz"] == "1")`
        - Condition: `(e.message:findi("lore"))`
      - Player: "Information" (link: explicit mention)
        - Prompted by player input: "Hail"
        - NPC say: 'There is no way to escape from the prison that is The Plane of Time. I am sorry but your quest for information ends here. Time is something that none of us can escape. That is however.. back when my explorations of the Planes were more common, I would travel searching for knowledge and lore to bring back to Tanaan. I stumbled into the Plane of Innovation. It was a great marvel to see indeed. I found the creator of all things mechanical. Meldrath the Marvelous was a kind and just gnome. We spent many weeks together discussing all of his devices. This included a machine that would allow you to open a tear into a period of time and enter into that time. The machine was more of a flight of whimsy though as the power necessary to power such a machine was enormous. He jokingly equated needing the very essence of the elements to power it.'
        - NPC emote: Maelin takes a deep breath and continues
        - NPC say: I can see now that he was not joking at all. Let us suppose that you travelers could venture into the Elemental Planes and retrieve this essence; and form it into one powerful conglomeration. You could open a tear into the period of time before Zebuxoruk was imprisoned. There is no way you can free him from his stasis now, but if you were to halt the Pantheon at the time of imprisonment. Hah! It could work I do believe. Forgive me, but my old gnomish heart is alive with the excitement of possibilities. Gather up your strength friends, travel into the deep elements. You will need all of your wits about you. Find the very essence of the elementals, and fuse them into one. How to combine them I do not know, and can only wish you luck on finding that information. If you can accomplish this please come get me. I would like to record the events as they take place!'
        - NPC message: You receive a character flag!
        - Condition: `(qglobals["pop_hohb_marr"] == "1" and qglobals["pop_bot_agnarr"] == "1" and qglobals["pop_pon_hedge_jezith"] == "1" and qglobals["pop_pon_construct"] == "1" and qglobals["pop_ponb_terris"] == "1"	and qglobals["pop_ponb_poxbourne"] == "1" and qglobals["pop_pod_alder_fuirstel"] == "1" and qglobals["pop_pod_grimmus_planar_projection"] == "1" and qglobals["pop_pod_elder_fuirstel"] == "1" and qglobals["pop_poj_mavuin"] == "1" and qglobals["pop_poj_tribunal"] == "1" and qglobals["pop_poj_valor_storms"] == "1" and qglobals["pop_pov_aerin_dar"] == "1" and qglobals["pop_pos_askr_the_lost"] == "3" and qglobals["pop_pos_askr_the_lost_final"] == "1" and qglobals["pop_cod_preflag"] == "1" and qglobals["pop_cod_bertox"] == "1" and qglobals["pop_cod_final"] == "1" and qglobals["pop_pot_shadyglade"] == "1" and qglobals["pop_pot_saryrn"] == "1" and qglobals["pop_pot_saryrn_final"] == "1" and qglobals["pop_hoh_faye"] == "1" and qglobals["pop_hoh_trell"] == "1" and qglobals["pop_hoh_garn"] == "1" and qglobals["pop_tactics_ralloz"] == "1")`
        - Condition: `(e.message:findi("information"))`
        - Sets `pop_elemental_grand_librarian` to `1`.
      - Player: "Tome" (link: external event mention)
        - Prompted by `event_trade`:
          - NPC say: I knew they were egg-layers! Ha, this is one gnome who hates losing a bet and thanks to you I wont! This is the tome you seek. Please bring it back to me when you are done.
          - Event guard: `(qglobals["shadowknight_epic"] == "1" and item_lib.check_turn_in(e.trade, {item1 = 55900}))`
        - NPC say: Yes, I seem to recall having such a tome. But evil it is. I don't hand out such dangerous knowledge to just anyone. However. . . I am curious about something and perhaps you can help me. A prominent professor of biology and I have a bet as to how a certain creature from the Realm of Discord, known as a murkglider breeds. He believes they give live birth, and I believe they are egg layers. Unfortunately, I have been so busy here, that I have not been able to make arrangements to travel there and observe the creatures more. If you could travel to the Realm of Discord and [find an egg] for me, I will give you the book you seek.
        - Condition: `(qglobals["shadowknight_epic"] == "1")`
        - Condition: `(e.message:findi("tome"))`
      - Player: "Find An Egg" (link: explicit mention)
        - NPC say: I appreciate your help with this! The creature I was supposed to study are most commonly known as murkgliders. The easiest way to describe them is that they look like large, floating octopuses. See if you can hunt down any breeding murkgliders and return an egg to me that I can study. You might want to bring some companions along, as this might be a dangerous task.
        - Condition: `(qglobals["shadowknight_epic"] == "1")`
        - Condition: `(e.message:findi("find an egg"))`
      - Player: "Jeb Lumsed sent me" (link: conversation sequence)
        - NPC say: This is from Jeb, you say? I will set my best researchers on it at once. We have recently made some discoveries that he should be aware of. Here, take this note down to Lobaen, she will retrieve them for you.
        - Condition: `(qglobals["ench_epic"] == "2" and e.message:findi("Jeb Lumsed sent me"))`
        - Gives Note to Lobaen (52950).
225. poknowledge/"Illusionist Lobaen", hand "Note to Lobaen" (52950). Gives "Sealed Documents" (52959).
    - Dialogue with poknowledge/"Illusionist Lobaen":
      - Player: "Hail"
        - NPC say: Good day to you. $name. Despite your purpose among us in New Tanaan. know that we bear no ill will toward any for mere distinctions of race or religious preference. We are all equals -- children of the gods and children of the earth alike. It has been a very long time since I have been among adventurers. and I admit that this is truly an experience I have not craved. The nymphs were persecuted in our day. though not through intended force. but in the expansion of your cultures and the erection of great elven and human cities. Aaah. but I do dwell on matters of the past. What is done is done. Now. I exist to aid you should you wish it. friend. I have adopted the mortal art of enchantment and what knowledge I have of it is yours should it be of use.
        - Condition: `(e.message:findi("hail"))`
226. burningwood/"A Sarnak Imitator", hand "Sealed Documents" (52959). Gives "Assembling the Staff" (54286).
227. Loot "Sullied Gold Filigree" (52963) from "An Enticing Potameid" in `natimbi`.
228. hohonora/"Anthone Chapin", hand "Sullied Gold Filigree" (52963). Gives "Purified Gold Filigree" (52953).
    - Dialogue with hohonora/"Anthone Chapin":
      - Player: "Hail"
        - NPC say: Mithaniel Marr himself has entrusted me with the power to purge taint from the most desecrated of objects.
        - Condition: `(plugin::check_hasitem($client, 54286) && ($text=~/hail/i))`
229. Combine in "Ornate Staff Chest" (52960): "1st Piece of the Staff" (54289), "2nd Piece of the Staff" (54310), "3rd Piece of the Staff" (54299), "4th Piece of the Staff" (54284), "Ornate Staff Topper" (52961), "All-Seeing Eye" (54293), "Incandescent Oil" (57924), "Purified Gold Filigree" (52953). Produces "Latched Ornate Chest" (52966). The combine does not fail.
230. burningwood/"A Sarnak Imitator", hand "Latched Ornate Chest" (52966). Gives "Oculus of Persuasion" (52952).
231. Loot "Heart of a Twisted Stoneservant" (54239) from "A Twisted Stoneservant" in `riwwi`.
232. Hand "Heart of a Twisted Stoneservant" (54239) to wakening/"Alaurin". Spawns "A Luminescent Geonid" (119184). Loot "Luminescent Crystal" (52949) from "A Luminescent Geonid".
233. wakening/"Alaurin", hand "Luminescent Crystal" (52949). Gives "Purifying Crystal Fragment" (52955).
    - Dialogue with wakening/"Alaurin":
      - Player: "Hail"
        - NPC say: Hello, coercer. Why have you disturbed me?
        - Condition: `(e.message:findi("hail") and e.other:Class()=="Enchanter")`
      - Player: "Crystal"
        - NPC say: My crystal, you say? Now that is something I hold very dear. It is my most beautiful trinket. I must say, I've never had occasion to use it however . . . Actually, I believe I can make you a deal.
        - Condition: `(e.message:findi("crystal"))`
      - Player: "Deal" (link: explicit mention)
        - NPC say: I know of a stone that I could use in its stead, but before we go into that I must ask something of you. If you truly desire this piece of crystal, you must bring me the heart of a twisted stoneservant. I have heard stories of invaders that have infested this newly found continent of Taelosia, where they have managed to turn their very servants against them. This sort of utter control is very interesting to me, and I would like to study it. Once I have the heart, I know where you can find a gem to replace my crystal.
        - Condition: `(e.message:findi("deal"))`
234. Loot "Volatile Vampyre Blood" (52965) from "a Coterie insatiate" in `tenebrous`.
235. westwastes/"Vohnkare", hand "Volatile Vampyre Blood" (52965). Gives "Purifying Crystal Fragment" (52956).
    - Dialogue with westwastes/"Vohnkare":
      - Player: "Hail"
        - NPC say: What do you seek mortal?
        - Condition: `(e.message:findi("hail") and e.other:Class()=="Enchanter")`
      - Player: "Crystal" (link: external event mention)
        - Prompted by `event_trade`:
          - NPC say: This will do quite nicely. Are you aware of the properties of vampyre blood? It can make such lovely protective concoctions. Why, I once fended off . . . There I go again. Here is your crystal, make haste!
          - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 52965}) and e.other:HasItem(52952) and not eq.get_entity_list():IsMobSpawnedByNpcTypeID(119184))`
        - NPC say: Such great power for such a small being. I see that you are strong despite your size, however I fear for our world as I see such potent tools coming together. I fear a great battle is upon us. Enough of my rambling, I do have such a crystal. Bring me some volatile vampyre blood from the Tenebrous Mountains and I will part with it. It has been too long since I have had servants to fetch me such things.
        - Condition: `(e.message:findi("crystal"))`
236. Buy "Gnomish Candy" (52944) from "Clockwork Merchant" (NPC 55308) in `akanon`. Base price: 125,000 copper.
237. Buy "Koada'Dal Silk" (52948) from "Merchant Tyslin" (NPC 61044) in `felwithea`. Base price: 125,000 copper.
238. Buy "Feir'Dal Champagne" (52940) from "Innkeep" (NPC 19084) in `rivervale`. Base price: 125,000 copper.
239. Buy "Dwarven Steel" (57921) from "Gretta Mottle" (NPC 60000) in `kaladima`. Base price: 125,000 copper.
240. lfaydark/"A Brownie Noble", hand "Feir'Dal Champagne" (52940) + "Gnomish Candy" (52944) + "Koada'Dal Silk" (52948) + "Dwarven Steel" (57921). Sets `ench_epic` to `8`.
241. Loot "Harnessing Stone" (52946) from "Miriku the Chaotic" in `kael`.
242. lfaydark/"A Brownie Noble", hand "Harnessing Stone" (52946). Requires `ench_epic` ==8. Gives "Purifying Crystal Fragment" (52957).
243. Say "Spawn Devastating Pookas" to tipt/"Rikabi The Riddler".
244. Spawns "A Devastating Pooka" (289037).
245. Loot "Mountain Pooka Meat" (54240) from "A Devastating Pooka".
246. Hand "Mountain Pooka Meat" (54240) to jaggedpine/"Chef Brargus". Spawns "Firwyn" (181226). Loot "Dryad Necklace" (57917) from "Firwyn".
247. gfaydark/"Feyana Lightwing", hand "Dryad Necklace" (57917). Gives "Purifying Crystal Fragment" (52958).
    - Dialogue with gfaydark/"Feyana Lightwing":
      - Player: "Hail"
        - NPC say: Greetings. It is not often that your kind has reason to speak to us. You must be seeking something.
        - Condition: `(e.message:findi("hail") and e.other:Class()=="Enchanter")`
      - Player: "Crystal" (link: conversation sequence)
        - NPC say: To even be aware of the crystal's existence you must be of some power. I can only assume that if you are repairing it that you have good reason. It is yours if you can do me one small favor.
        - Condition: `(e.message:findi("crystal"))`
      - Player: "Favor" (link: explicit mention)
        - NPC say: There is a Dryad that has something that belongs to me. There is no rift between our kind, however you could say this is more of a personal conflict. You see, I was once given a necklace from their people in return for a service provided long ago. It was the most beautiful Dryad necklace I have ever seen, and it was stolen. I believe the culprit's name is Firwyn. Travel to the Jaggedpine Forest and seek out Chef Brargus, he should know where to find her. If you can bring me back the necklace the fragment is yours.
        - Condition: `(e.message:findi("favor"))`
248. Combine in "Planar Jeweler's Kit" (17764): "Purifying Crystal Fragment" (52955), "Purifying Crystal Fragment" (52956), "Purifying Crystal Fragment" (52957), "Purifying Crystal Fragment" (52958). Produces "Purifying Crystal" (52954). Requires Jewelry Making. The combine does not fail.

### "Oculus of Persuasion" (52952)

1. Acquisition of "Oculus of Persuasion" (52952) is documented under "Purifying Crystal" (52954); obtain another copy if needed.

### "Latched Ornate Chest" (52966)

1. Acquisition of "Latched Ornate Chest" (52966) is documented under "Purifying Crystal" (52954); obtain another copy if needed.

### "Channeling Crystal" (57920)

1. Loot "Tattered Incantation" (57919) from "Cipheron" in `wallofslaughter`.
2. Loot "Noxious Secretion" (52951) from "Withering Murkglider" in `causeway`.
3. nedaria/"Priestess Rakhu", hand "Noxious Secretion" (52951) + "Tattered Incantation" (57919). Requires `ench_epic` ==9. Gives "Channeling Crystal" (57920).
    - Dialogue with nedaria/"Priestess Rakhu":
      - Player: "Hail"
        - NPC say: I have been expecting you. There are still a few things more for you to do before the staff is properly prepared. For the next step you will need to travel into Discord and gather two items that I need to perform the next step in the purification process. A great beast by the name of Cipheron has hoarded an incantation for many years. I believe he killed one of our students who was unfortunate enough to get in his way... Reguardless, I will need it. You will also need to gather a noxious secretion from a withering murkglider. It is a strange fluid they begin to secrete as they are dying, and it is very powerful. Bring me this incantation and the secretion and we shall get started.
        - Condition: `(e.message:findi("hail") and qglobals["ench_epic"] == "9")`

### "Gnomish Translating Device" (52945)

1. Acquisition of "Gnomish Translating Device" (52945) is documented under "Purifying Crystal" (52954); obtain another copy if needed.

### "Illegible Tome" (52947)

1. Acquisition of "Illegible Tome" (52947) is documented under "Purifying Crystal" (52954); obtain another copy if needed.

### "Sealed Documents" (52959)

1. Acquisition of "Sealed Documents" (52959) is documented under "Purifying Crystal" (52954); obtain another copy if needed.

### "Complete Illegible Tome" (54267)

1. Acquisition of "Complete Illegible Tome" (54267) is documented under "Purifying Crystal" (52954); obtain another copy if needed.

## `EnchPre`

Values written: 1, 2.

1. lakeofillomen/"A Bloodgill Mimic", hand "Garudon's Statue" (52941). Sets `EnchPre` to `1`.
    - Hand in x1: "Garudon's Statue" (52941).
    - Hand "Dragon Boneshard" (65574) to veksar/"Spirit Of Garudon". Spawns "Garudon" (109107). Loot "Garudon's Statue" (52941) from "Garudon".
    - Dialogue with lakeofillomen/"A Bloodgill Mimic":
      - Player: "Hail"
        - NPC say: Can't you feel him? I hear the wind blow across the lake and I think he must still be . . .
        - Condition: `(e.message:findi("hail"))`
      - Player: "Who Is He" (link: conversation sequence)
        - NPC say: He who fell from the sky. I have sought [evidence] of him for my [master].
        - Condition: `(e.message:findi("who is he"))`
      - Player: "Master" (link: explicit mention)
        - NPC say: You know my master. Are we not the same?
        - Condition: `(e.message:findi("master"))`
      - Player: "Aida" (link: external event mention)
        - Prompted by `event_trade`:
          - NPC say: I thank you. How terrible it must be to still remain after such time. You must possess some measure of power to return this to me. I believe Aida could benefit from the help of one such as yourself.
          - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 52941}))`
        - NPC say: Aida was once my partner, but it has been years since I have seen her. It does worry me so.
        - Condition: `(e.message:findi("Aida"))`
      - Player: "Where Is She" (link: conversation sequence)
        - NPC say: I last saw her heading into an airless place. So confident, she was
        - Condition: `(e.message:findi("where is she"))`

2. burningwood/"A Sarnak Imitator", hand "Gnomish Translating Device" (52945) + "Illegible Tome" (52947). Sets `EnchPre` to `2`.
    - Hand in x1: "Illegible Tome" (52947).
    - Hand in x1: "Gnomish Translating Device" (52945).
    - Prerequisite: "Illegible Tome" (52947). See section 0.
    - Prerequisite: "Gnomish Translating Device" (52945). See section 0.
    - Gives "Tattered Illegible Tome" (57918).
    - Dialogue with burningwood/"A Sarnak Imitator":
      - Player: "Hail"
        - NPC say: Much time has passed since the creation of the Staff of the Serpent. The power of discord is seeping into our fair world, and only the most powerful of us shall stand to force it back. The time has come for a new tool, and a new breed of enchanter. [Are you prepared] to meet this challenge?
        - Condition: `(e.message:findi("hail") and (e.other:HasItem(10650) or qglobals["EnchPre"] == "2"))`
        - Sets `ench_epic` to `1`.
      - Player: "Prepared" (link: explicit mention)
        - NPC say: I have recently received this ancient tome; it contains knowledge that may prove invaluable to the construction of a new staff. Unfortunately, time has had its way with it. I need you to find the missing pages so we can get to work. There should be ten, unless they have been destroyed by time and decay.
        - Condition: `(e.message:findi("prepared") and qglobals["ench_epic"] ~= nil and qglobals["ench_epic"] >= "1")`
        - Gives Tattered Illegible Tome (57918).
      - Player: "Chest" (link: external event mention)
        - Prompted by `event_trade`:
          - NPC say: Interesting indeed. I see that I was not wrong in my instinct to begin this as quickly as possible. I have created a list of the items that you will need to begin the construction of this tool. Mind you, it will not be a simple thing. When you have gathered them all return to me. Would you like a [chest] to carry them in?
          - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 52959}))`
        - Condition: `(e.message:findi("chest") and qglobals["ench_epic"] ~= nil and qglobals["ench_epic"] >= "3")`
        - Gives Ornate Staff Chest (52960).
      - Player: "Are You Jeb Lumsed" (link: conversation sequence)
        - NPC say: Yes, I am. Use your most enlightened magic to seek the truth of what is around you. When that is done, you will know what you seek.
        - Condition: `(e.message:findi("are you jeb lumsed"))`
      - Player: "Serpent" (link: explicit mention)
        - Prompted by player input: "Hail"
        - NPC say: The first truly powerful enchanter, Krilan Pedin, crafted the Serpent years ago. He trained his students to carry on the trade in a five-step process. Each student then became a master and chose one of their own students to pass the legacy on to. Four others and I, myself, are current practitioners of the crafting.
        - Condition: `(e.message:findi("serpent"))`
      - Player: "Masters" (link: explicit mention)
        - NPC say: The masters are enchanters who have reached the plateau of understanding. Their names are Modani Qu'Loni, Mizzle Gepple, Nadia Starfeast, and Polzin Mrid. All are master crafters in their own right.
        - Condition: `(e.message:findi("masters"))`
      - Player: "Modani" (link: explicit mention)
        - NPC say: Modani is a master of illusions. You should seek him out first. Keep a careful eye out for him - he is never in his true form. The last time I spoke to him, he seemed very excited about his voyage to the elven outpost. You may or may not find more clues about his location there.
        - Condition: `(e.message:findi("modani"))`
      - Player: "Mizzle" (link: explicit mention)
        - Prompted by player input: "Masters"
        - NPC say: Mizzle is a gnome who has mastered the use of enlightened magic. Go to him once you have spoken to Modani. Mizzle is not one to travel, so you should not have to look far from his home to find him.
        - Condition: `(e.message:findi("mizzle"))`
      - Player: "Nadia" (link: explicit mention)
        - Prompted by player input: "Masters"
        - NPC say: The mistress of charm, Nadia is very beautiful. She, too, traveled with her relatives to the new land. I just recently received a letter from her. She says more and more pilgrims and explorers are arriving every day, and that the outpost is well defended now.
        - Condition: `(e.message:findi("nadia"))`
      - Player: "Polzin" (link: explicit mention)
        - Prompted by player input: "Masters"
        - NPC say: Master of the Phantasms - he is the last one you will seek out. Hmm...Polzin is native to Erudin, however, after the incident near Paineel, no one has heard from him. I hope that he is well.
        - NPC say: Take this sack and combine the items I requested in it. Then return it to me.
        - Condition: `(e.message:findi("polzin"))`
      - Player: "I Need A Sack" (link: conversation sequence)
        - NPC say: Master of the Phantasms - he is the last one you will seek out. Hmm...Polzin is native to Erudin, however, after the incident near Paineel, no one has heard from him. I hope that he is well.
        - NPC say: Take this sack and combine the items I requested in it. Then return it to me.
        - Condition: `(e.message:findi("polzin"))`
      - Player: "Purify" (link: conversation sequence)
        - NPC say: The purification is not something that I alone have the power to complete. There was once a crystal that held the power to purify something of this magnitude, however it was shattered long ago. You will need to speak to the masters that remain of dwindling races.
        - Condition: `(e.message:findi("purify") and e.other:HasItem(52952))`
      - Player: "Races" (link: explicit mention)
        - NPC say: The masters are of races that walked Norrath before you or I. I do not know their current whereabouts. Alaurin and Vohnkare were the eldest of the four. There was a noble . . Ah, yes and Feyana. I do hope you find them.
        - Condition: `(e.message:findi("races") and e.other:HasItem(52952))`

### Steps on `EnchPre` that do not change it

- `burningwood` a sarnak imitator, say hail needs `EnchPre` ==2.
  - Sets `ench_epic` to `1`.
- `ssratemple` a soriz imitator, hand 54313 needs `EnchPre` ==1.
  - Turn in Crumbling Tome (54313).
  - Gives Illegible Tome (52947).

## `ench_epic`

Values written: 1, 2, 3, 7, 8, 9, 10.

1. burningwood/"A Sarnak Imitator", say "Hail". Sets `ench_epic` to `1`.
    - Requires `ench_epic` unset.
    - Requires `EnchPre` ==2.

    - Subquest `EnchPre` documented earlier.
2. burningwood/"A Sarnak Imitator", hand "Complete Illegible Tome" (54267). Sets `ench_epic` to `2`.
    - Hand in x1: "Complete Illegible Tome" (54267).
    - Prerequisite: "Complete Illegible Tome" (54267). See section 0.

3. burningwood/"A Sarnak Imitator", hand "Sealed Documents" (52959). Sets `ench_epic` to `3`.
    - Hand in x1: "Sealed Documents" (52959).
    - Prerequisite: "Sealed Documents" (52959). See section 0.
    - Gives "Assembling the Staff" (54286).

7. burningwood/"A Sarnak Imitator", hand "Latched Ornate Chest" (52966). Sets `ench_epic` to `7`.
    - Hand in x1: "Latched Ornate Chest" (52966).
    - Prerequisite: "Latched Ornate Chest" (52966). See section 0.
    - Gives "Oculus of Persuasion" (52952).

8. lfaydark/"A Brownie Noble", hand "Feir'Dal Champagne" (52940) + "Gnomish Candy" (52944) + "Koada'Dal Silk" (52948) + "Dwarven Steel" (57921). Sets `ench_epic` to `8`.
    - Requires "Oculus of Persuasion" (52952).
    - Hand in x1: "Gnomish Candy" (52944).
    - Hand in x1: "Koada'Dal Silk" (52948).
    - Hand in x1: "Feir'Dal Champagne" (52940).
    - Hand in x1: "Dwarven Steel" (57921).
    - Prerequisite: "Oculus of Persuasion" (52952). See section 0.
    - Buy "Gnomish Candy" (52944) from "Clockwork Merchant" (NPC 55308) in `akanon`. Base price: 125,000 copper.
    - Buy "Koada'Dal Silk" (52948) from "Merchant Tyslin" (NPC 61044) in `felwithea`. Base price: 125,000 copper.
    - Buy "Feir'Dal Champagne" (52940) from "Innkeep" (NPC 19084) in `rivervale`. Base price: 125,000 copper.
    - Buy "Dwarven Steel" (57921) from "Gretta Mottle" (NPC 60000) in `kaladima`. Base price: 125,000 copper.
    - Dialogue with lfaydark/"A Brownie Noble":
      - Player: "Hail"
        - NPC say: Long time have your kind needed us, but never have we been close. Wouldn't you agree? I'm afraid I cannot help you without some token of faith
        - Condition: `(e.message:findi("hail") and e.other:Class()=="Enchanter")`
      - Player: "Faith" (link: explicit mention)
        - NPC say: So long have we retained our distance, we have nearly been forgotten. Despite the fact that this allows us our peace, there are times I wish I could provide my people with the niceties of society. If you could obtain a few items for me I could help you with the knowledge you seek.
        - Condition: `(e.message:findi("faith"))`
      - Player: "Items" (link: explicit mention)
        - NPC say: I would very much like some Gnomish Candy, Koada'Dal Silk, Feir'Dal Champagne, and Dwarven Steel.
        - Condition: `(e.message:findi("items"))`

9. global/"Global Player", combine recipe 19919. Sets `ench_epic` to `9`.
    - `recipe:19919` is combined in Planar Jeweler's Kit (17764).
      - Buy "Planar Jeweler's Kit" (17764) from "Noirin Khalen" (NPC 202084) in `poknowledge`. Base price: 1,000 copper.
      - Put in x1: Oculus of Persuasion (52952).
        - Prerequisite: "Oculus of Persuasion" (52952). See section 0.
      - Put in x1: Purifying Crystal (52954).
        - Prerequisite: "Purifying Crystal" (52954). See section 0.
      - Hands back Oculus of Persuasion (52952).
      - Produces no new item.
      - Requires Jewelry Making. The combine does not fail.

10. global/"Global Player", combine recipe 19920. Sets `ench_epic` to `10`.
    - `recipe:19920` is combined in Channeling Crystal (57920).
      - Prerequisite: "Channeling Crystal" (57920). See section 0.
      - Put in x1: Globe of Discordant Energy (47100).
        - Say "Check Lorb" to anguish/"Zone Status".
        - Spawns "Orb of Discordant Energy" (317087).
        - Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy".
        - Alternative: Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy" (NPC 317087) in `anguish`; trigger: anguish/"Zone Status", say "Check Uorb".
        - Alternative: Loot "Globe of Discordant Energy" (47100) from "Ornate Chest" (NPC 317112) in `anguish`; trigger: anguish/"Zone Status", say "Check Amv Chest".
        - Alternative: Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy" (NPC 317087) in `anguish`; trigger: anguish/"Zone Status", on event_signal.
        - Alternative: Loot "Globe of Discordant Energy" (47100) from "Overlords Chest" (NPC 317124) in `anguish`; trigger: anguish/"Zone Status", on event_signal.
      - Put in x1: Oculus of Persuasion (52952).
        - Prerequisite: "Oculus of Persuasion" (52952). See section 0.
      - Produces Staff of Eternal Eloquence (52962).
      - The combine does not fail.

### Steps on `ench_epic` that do not change it

- `burningwood` a sarnak imitator, say chest needs `ench_epic` set.
  - Gives Ornate Staff Chest (52960).
- `burningwood` a sarnak imitator, say prepared needs `ench_epic` set.
  - Gives Tattered Illegible Tome (57918).
- `causeway` player, on loot needs `ench_epic` ==9.
  - Sets `ench_chest_causeway` to `1`.
  - Spawns a chest (epic 2.0) (893).
- `lfaydark` a brownie noble, hand 52946 needs `ench_epic` ==8.
  - Turn in Harnessing Stone (52946).
  - Gives Purifying Crystal Fragment (52957).
- `mischiefplane` player, on loot needs `ench_epic` >=3.
  - Sets `ench_epic_pom` to `1`.
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
- `nedaria` priestess rakhu, hand 52951+57919 needs `ench_epic` ==9.
  - Turn in Tattered Incantation (57919).
  - Turn in Noxious Secretion (52951).
  - Gives Channeling Crystal (57920).
- `poknowledge` grand librarian maelin, say jeb lumsed sent me needs `ench_epic` ==2.
  - Gives Note to Lobaen (52950).
- `sirens` player, on loot needs `ench_epic` set.
  - Sets `ench_epic_sirens` to `1`.
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
- `wallofslaughter` player, on loot needs `ench_epic` ==9.
  - Sets `ench_wos_chest` to `1`.
  - Spawns a chest (Epic 1.5) (893).

## Other flags touched along the way

- `ench_epic_pom` set to 1 at mischiefplane/player.
- `ench_epic_sirens` set to 1 at sirens/player.
