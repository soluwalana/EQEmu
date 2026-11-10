# Warrior

Acquisition paths traced backwards from the 1.0, 1.5 and 2.0 epic rewards. Flags are dependencies, not the definition of an epic. **Broken** indicates missing graph provenance.

## Epic 1.0

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
29. Buy "Barley" (16590) from "Heidi Grainsifter" (NPC 1065) in `qeynos`. Base price: 15 copper.
30. Buy "Deep Fungus Mold" (67393) from "Heidi Grainsifter" (NPC 1065) in `qeynos`. Base price: 50,000 copper.
31. Buy "Distilled Spirits" (67394) from "Heidi Grainsifter" (NPC 1065) in `qeynos`. Base price: 5,000 copper.
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
45. Loot "Blade of Tactics" (10909) from "Reattim Heftsteel" (NPC 309005) in `chambersf`. Drop cache: 100% chance per kill.
46. Loot "Blade of Strategy" (10910) from "Reattim Heftsteel" (NPC 309005) in `chambersf`. Drop cache: 100% chance per kill.
47. Combine in "Red Scabbard" (17859): "Blade of Tactics" (10909), "Blade of Strategy" (10910). Produces "Jagged Blade of War" (10908). The combine does not fail.

## Epic 1.5

### "Champion's Sword of Eternal Power" (60321)

**Broken:** no quest hand-in, encounter or recipe produces "Champion's Sword of Eternal Power" (60321) in the graph. Catalog drops/spells below are not proof of the epic quest.

1. Loot "Champion's Sword of Eternal Power" (60321) from "Krekk Brimblade" in `dranik`.

## Epic 2.0

### "Kreljnok's Sword of Eternal Power" (60332)

1. Kill causeway/"Korbuk Brimblade". Spawns "Essence of Kreljnok" (303129).
2. Loot "Brimblade's Scabbard" (60331) from "Essence of Kreljnok".
3. Kill causeway/"Korbuk Brimblade". Spawns "Essence of Kreljnok" (303129).
4. Loot "Kreljnok's Essence" (60330) from "Essence of Kreljnok".
5. global/"Global Player", combine recipe 19902. Sets `warrior_epic` to `21`.
6. Loot "Champion's Sword of Eternal Power" (60321) from "Krekk Brimblade" in `dranik`.
7. Unresolved cyclic prerequisite: `warrior_epic` ==15.
8. draniksscar/"Korbuk Brimblade", say "Hail". Sets `warrior_epic` to `16`.
9. draniksscar/"Korbuk Brimblade", say "Work". Sets `warrior_pre` to `1`.
10. Loot "Korbuk's Weapon Plans" (60285) from "The Diaku Overseer" in `potactics`.
11. draniksscar/"Korbuk Brimblade", hand "Korbuk's Weapon Plans" (60285). Sets `warrior_pre` to `2`.
12. Loot "Elegant Shank" (60286) from "Shoqui the Forgotten" in `hatesfury`.
13. draniksscar/"Korbuk Brimblade", hand "Elegant Shank" (60286). Sets `warrior_pre` to `3`.
14. Loot "Redblade Family Sword" (60287) from "Drevlon Knacknabber" in `eastkarana`.
15. freeporteast/"Kargek Redblade", hand "Redblade Family Sword" (60287). Requires `warrior_pre` set. Requires `warrior_pre` ==3. Gives "Emblazoned Champion's Hilt" (60288).
16. draniksscar/"Korbuk Brimblade", hand "Emblazoned Champion's Hilt" (60288). Sets `warrior_pre` to `4`.
17. thurgadina/"Dardek Bladewright", hand "Korbuk's Weapon Plans" (60285) + "Elegant Shank" (60286) + "Emblazoned Champion's Hilt" (60288). Sets `warrior_pre` to `5`.
18. thurgadina/"Dardek Bladewright", hand "Korbuk's Weapon Plans" (60285) + "Elegant Shank" (60286) + "Emblazoned Champion's Hilt" (60288). Requires `warrior_pre` ==4. Gives "Dardek's Forged Blade" (60292).
19. draniksscar/"Korbuk Brimblade", hand "Dardek's Forged Blade" (60292). Sets `warrior_pre` to `6`.
20. draniksscar/"Korbuk Brimblade", say "Work". Sets `warrior_epic` to `1`.
21. Kill bloodfields/"Girplan Slasher". Spawns "Girplan Devourer" (301063).
22. Loot "Decrepit Hilt" (60307) from "Girplan Devourer".
23. firiona/"Corfia Nultethen", hand "Decrepit Hilt" (60307). Sets `warrior_epic` to `9`.
24. firiona/"Corfia Nultethen", say "Galuk Drek". Sets `warrior_epic_veksar` to `1`.
25. Spawns "Decaying Lord Galuk Drek, not be in db yet" (109906) in `veksar` on enter.
26. Loot "Skeletal Tome of Galuk Drek" (60310) from "Decaying Lord Galuk Drek, not be in db yet".
27. firiona/"Corfia Nultethen", hand "Skeletal Tome of Galuk Drek" (60310). Requires `warrior_epic` set. Requires `warrior_epic` ==9. Gives "Glistening Hilt" (60311).
28. butcher/"Gridbar Galund", hand "Glistening Hilt" (60311). Requires `warrior_epic` set. Requires `warrior_epic` >=13. Gives "Carved Keg Stamp" (60318).
29. shadowhaven/"Koren Galund", hand "Carved Keg Stamp" (60318). Requires `warrior_epic` set. Requires `warrior_epic` >=13. Gives "Tube of Setting Solution" (60319).
30. butcher/"Gridbar Galund", hand "Tube of Setting Solution" (60319). Requires `warrior_epic` set. Requires `warrior_epic` >=13. Gives "Hilt of Eternal Power" (60320).
31. draniksscar/"Korbuk Brimblade", hand "Hilt of Eternal Power" (60320). Sets `warrior_epic` to `14`.
32. everfrost/"Kimber Whitefoot", say "Hail". Requires `warrior_epic` set. Requires `warrior_epic` >=4. Gives "Potion of Blackfall Spirit" (60306).
33. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
34. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `steamfont`.
35. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `tox`.
36. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `toxxulia`.
37. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
38. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). The combine does not fail.
39. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
40. nedaria/"Korezna Orecleaver", hand "Water Flask" (13006) + "Water Flask" (13006) + "Water Flask" (13006) + "Water Flask" (13006). Sets `warrior_epic_korezna` to `1`.
41. nedaria/"Korezna Orecleaver", hand "Water Flask" (13006) + "Water Flask" (13006) + "Water Flask" (13006). Sets `warrior_epic_korezna` to `2`.
42. **Broken:** nothing in the graph gives, loots, spawns, or combines Blackfall Ore (60301).
43. draniksscar/"Korbuk Brimblade", hand "Blackfall Ore" (60301). Requires `warrior_epic` >=2. Gives "Smelting Plans" (60302).
44. nedaria/"Korezna Orecleaver", hand "Blackfall Ore" (60301) + "Smelting Plans" (60302). Requires `warrior_epic_korezna` ==2. Gives "Blackfall Blade" (60303).
45. dranik/"Krekk Brimblade", hand "Blackfall Blade" (60303) + "Potion of Blackfall Spirit" (60306) + "Hilt of Eternal Power" (60320). Sets `warrior_epic` to `15`.
46. Loot "Kreljnok's Muddled Rage" (60322) from "Possessed Brute" in `provinggrounds`.
47. draniksscar/"Korbuk Brimblade", hand "Kreljnok's Muddled Rage" (60322). Sets `warrior_epic` to `17`.
48. Ground spawn of "Frozen Pestle" (60323) in `iceclad`.
49. iceclad/"Fazzle Thumpkin", hand "Frozen Pestle" (60323). Sets `warrior_epic` to `18`.
50. iceclad/"Fazzle Thumpkin", say "Map". Requires `warrior_epic` ==18. Gives "Fazzle's Map of East Wastes" (60324).
51. Spawns "Larnik the Recluse" (116609) in `eastwastes` on enter.
52. Loot "Larnik's Locked Purification Kit" (60325) from "Larnik the Recluse".
53. draniksscar/"Korbuk Brimblade", hand "Larnik's Locked Purification Kit" (60325). Requires `warrior_epic` >=18. Gives "Larnik's Unlocked Purification Kit" (60326).
54. Combine in "Larnik's Unlocked Purification Kit" (60326): "Kreljnok's Muddled Rage" (60322). Produces "Kreljnok's Focused Rage" (60327). The combine does not fail.
55. draniksscar/"Korbuk Brimblade", hand "Champion's Sword of Eternal Power" (60321) + "Kreljnok's Focused Rage" (60327). Requires `warrior_epic` >=19. Gives "Raging Sword of Eternal Power" (60329).
56. Combine in "Brimblade's Scabbard" (60331): "Kreljnok's Essence" (60330), "Raging Sword of Eternal Power" (60329). Produces "Kreljnok's Sword of Eternal Power" (60332). The combine does not fail.

## Quest-state progression

## 0. Prerequisites

Shared acquisition steps appear in the first prerequisite chain that needs them. Later sections reference that chain rather than repeating it.

### "Emblazoned Champion's Hilt" (60288)

1. draniksscar/"Korbuk Brimblade", say "Work". Sets `warrior_pre` to `1`.
2. Loot "Korbuk's Weapon Plans" (60285) from "The Diaku Overseer" in `potactics`.
3. draniksscar/"Korbuk Brimblade", hand "Korbuk's Weapon Plans" (60285). Sets `warrior_pre` to `2`.
4. Loot "Elegant Shank" (60286) from "Shoqui the Forgotten" in `hatesfury`.
5. draniksscar/"Korbuk Brimblade", hand "Elegant Shank" (60286). Sets `warrior_pre` to `3`.
6. Loot "Redblade Family Sword" (60287) from "Drevlon Knacknabber" in `eastkarana`.
7. freeporteast/"Kargek Redblade", hand "Redblade Family Sword" (60287). Requires `warrior_pre` set. Requires `warrior_pre` ==3. Gives "Emblazoned Champion's Hilt" (60288).
    - Dialogue with freeporteast/"Kargek Redblade":
      - Player: "Hail"
        - NPC emote: looks up from his forge and says, 'Hello there, can I help you?' Your eyes are drawn to an extremely large red sword scabbard strapped to his back with no sword in it. Kargek speaks again, 'I said, can I help you or do you need help from Wenden?'
        - Condition: `(e.other:Class() == "Warrior")`
        - Condition: `(e.message:findi("hail"))`
      - Player: "Wenden" (link: explicit mention)
        - NPC emote: points to the other side of the forge and says, 'Wenden is my partner. He is standing right over there. If it is a question about a weapon, he will probably have the answers.'
        - Condition: `(e.other:Class() == "Warrior")`
        - Condition: `(e.message:findi("wenden"))`
      - Player: "Scabbard" (link: explicit mention)
        - Prompted by player input: "Hail"
        - NPC emote: turns to look at you and says, 'It is a family heirloom. I might tell you the story behind it if you do me a little [favor].'
        - Condition: `(e.other:Class() == "Warrior")`
        - Condition: `(e.message:findi("scabbard"))`
      - Player: "Favor" (link: explicit mention)
        - NPC say: An associate of mine is wandering somewhere in the Feerrott. His name is Oknoggin Stonesmacker. If you will deliver this note to him, I would appreciate it.
        - Condition: `(e.other:Class() == "Warrior")`
        - Condition: `(e.message:findi("favor"))`
        - Gives Wax Sealed Note (20673).
      - Player: "Sent Me To Help" (link: conversation sequence)
        - NPC say: Really? I thought we'd have to deal with this problem on our own, and that has proven most distressful. If you really are here on word from Korbuk, you'll have no problem helping my family recover a [sword] we made and put on our father's grave.
        - Condition: `(e.other:Class() == "Warrior")`
        - Condition: `(e.message:findi("sent me to help"))`
      - Player: "Sword" (link: explicit mention)
        - NPC say: The sword is a sign of our heritage and our continued patronage and service to the cause of the red scabbard. It combines the duty of our family with our proud and strong family name and was placed on our father's grave as it was on his father's grave. It's a tradition you see, and now it's gone! I know [who did it] too!
        - Condition: `(e.other:Class() == "Warrior")`
        - Condition: `(e.message:findi("sword"))`
      - Player: "Who Did It" (link: explicit mention)
        - NPC say: It's that wily gnome, that's who! Drevlon and his gang of miscreants have been plotting to get their hands on anything valuable around here and they chose that sword as their prize. I had a lookout watching the area for a while, but there weren't any problems. Wouldn't you know it, as soon as I let the lookout off for an evening, Drevlon and his thugs snuck up to the grave and stole the sword! I need you to [find Drevlon] and recover the sword from him.
        - Condition: `(e.other:Class() == "Warrior")`
        - Condition: `(e.message:findi("who did it"))`
      - Player: "Find Drevlon" (link: explicit mention)
        - NPC say: If you can catch him and return the sword he stole, we can once again place it on the grave of my father where it belongs. He'll be expecting me or someone in lieu of me to try to find him, so you'll have to wait for him during the evening, when he's most likely to come out of hiding. He hasn't had a lot of time to get out of the area, so you can probably find him near my father's grave, in the eastern plains of Karana.
        - Condition: `(e.other:Class() == "Warrior")`
        - Condition: `(e.message:findi("find drevlon"))`

### "Dardek's Forged Blade" (60292)

1. Acquisition of "Emblazoned Champion's Hilt" (60288) is documented under "Emblazoned Champion's Hilt" (60288); obtain another copy if needed.
2. draniksscar/"Korbuk Brimblade", hand "Emblazoned Champion's Hilt" (60288). Sets `warrior_pre` to `4`.
3. Acquisition of "Korbuk's Weapon Plans" (60285) is documented under "Emblazoned Champion's Hilt" (60288); obtain another copy if needed.
4. Acquisition of "Elegant Shank" (60286) is documented under "Emblazoned Champion's Hilt" (60288); obtain another copy if needed.
5. thurgadina/"Dardek Bladewright", hand "Korbuk's Weapon Plans" (60285) + "Elegant Shank" (60286) + "Emblazoned Champion's Hilt" (60288). Requires `warrior_pre` ==4. Gives "Dardek's Forged Blade" (60292).

### "Blackfall Blade" (60303)

1. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
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
2. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `steamfont`.
3. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `tox`.
4. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `toxxulia`.
5. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
6. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). The combine does not fail.
7. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
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
8. nedaria/"Korezna Orecleaver", hand "Water Flask" (13006) + "Water Flask" (13006) + "Water Flask" (13006) + "Water Flask" (13006). Sets `warrior_epic_korezna` to `1`.
9. nedaria/"Korezna Orecleaver", hand "Water Flask" (13006) + "Water Flask" (13006) + "Water Flask" (13006). Sets `warrior_epic_korezna` to `2`.
10. **Broken:** nothing in the graph gives, loots, spawns, or combines Blackfall Ore (60301).
11. Unresolved cyclic prerequisite: `warrior_epic` ==15.
12. Loot "Champion's Sword of Eternal Power" (60321) from "Krekk Brimblade" in `dranik`.
13. draniksscar/"Korbuk Brimblade", say "Hail". Sets `warrior_epic` to `16`.
14. Acquisition of "Korbuk's Weapon Plans" (60285) is documented under "Emblazoned Champion's Hilt" (60288); obtain another copy if needed.
15. Acquisition of "Elegant Shank" (60286) is documented under "Emblazoned Champion's Hilt" (60288); obtain another copy if needed.
16. Acquisition of "Emblazoned Champion's Hilt" (60288) is documented under "Emblazoned Champion's Hilt" (60288); obtain another copy if needed.
17. thurgadina/"Dardek Bladewright", hand "Korbuk's Weapon Plans" (60285) + "Elegant Shank" (60286) + "Emblazoned Champion's Hilt" (60288). Sets `warrior_pre` to `5`.
18. Acquisition of "Dardek's Forged Blade" (60292) is documented under "Dardek's Forged Blade" (60292); obtain another copy if needed.
19. draniksscar/"Korbuk Brimblade", hand "Dardek's Forged Blade" (60292). Sets `warrior_pre` to `6`.
20. draniksscar/"Korbuk Brimblade", say "Work". Sets `warrior_epic` to `1`.
21. Kill bloodfields/"Girplan Slasher". Spawns "Girplan Devourer" (301063).
22. Loot "Decrepit Hilt" (60307) from "Girplan Devourer".
23. firiona/"Corfia Nultethen", hand "Decrepit Hilt" (60307). Sets `warrior_epic` to `9`.
24. firiona/"Corfia Nultethen", say "Galuk Drek". Sets `warrior_epic_veksar` to `1`.
25. Spawns "Decaying Lord Galuk Drek, not be in db yet" (109906) in `veksar` on enter.
26. Loot "Skeletal Tome of Galuk Drek" (60310) from "Decaying Lord Galuk Drek, not be in db yet".
27. firiona/"Corfia Nultethen", hand "Skeletal Tome of Galuk Drek" (60310). Requires `warrior_epic` set. Requires `warrior_epic` ==9. Gives "Glistening Hilt" (60311).
28. butcher/"Gridbar Galund", hand "Glistening Hilt" (60311). Requires `warrior_epic` set. Requires `warrior_epic` >=13. Gives "Carved Keg Stamp" (60318).
29. shadowhaven/"Koren Galund", hand "Carved Keg Stamp" (60318). Requires `warrior_epic` set. Requires `warrior_epic` >=13. Gives "Tube of Setting Solution" (60319).
30. butcher/"Gridbar Galund", hand "Tube of Setting Solution" (60319). Requires `warrior_epic` set. Requires `warrior_epic` >=13. Gives "Hilt of Eternal Power" (60320).
31. draniksscar/"Korbuk Brimblade", hand "Hilt of Eternal Power" (60320). Sets `warrior_epic` to `14`.
32. everfrost/"Kimber Whitefoot", say "Hail". Requires `warrior_epic` set. Requires `warrior_epic` >=4. Gives "Potion of Blackfall Spirit" (60306).
33. dranik/"Krekk Brimblade", hand "Blackfall Blade" (60303) + "Potion of Blackfall Spirit" (60306) + "Hilt of Eternal Power" (60320). Sets `warrior_epic` to `15`.
34. draniksscar/"Korbuk Brimblade", hand "Blackfall Ore" (60301). Requires `warrior_epic` >=2. Gives "Smelting Plans" (60302).
35. nedaria/"Korezna Orecleaver", hand "Blackfall Ore" (60301) + "Smelting Plans" (60302). Requires `warrior_epic_korezna` ==2. Gives "Blackfall Blade" (60303).

### "Gemming Tool" (60316)

1. **Broken:** nothing in the graph gives, loots, spawns, or combines Notice to Cease and Desist (9590).
2. Hand "Notice to Cease and Desist" (9590) to freeporteast/"Lythe Songbird". Spawns "a Freeport guard" (382255). Loot "Fine Steel Two Handed Sword" (5351) from "a Freeport guard".
3. Alternative: Loot "Fine Steel Two Handed Sword" (5351) from "a seasoned Freeport guard" (NPC 382256) in `freeporteast`; trigger: freeporteast/"Lythe Songbird", hand "Notice to Cease and Desist" (9590).
4. Alternative: Loot "Fine Steel Two Handed Sword" (5351) from "a Freeport guard" (NPC 382255) in `freportw`; trigger: freportw/"Lythe Songbird", hand "Notice to Cease and Desist" (9590).
5. Alternative: Loot "Fine Steel Two Handed Sword" (5351) from "a seasoned Freeport guard" (NPC 382256) in `freportw`; trigger: freportw/"Lythe Songbird", hand "Notice to Cease and Desist" (9590).
6. Alternative: Loot "Fine Steel Two Handed Sword" (5351) from "a minion of Meldrath" (NPC 56173) in `steamfont`; trigger: steamfont/"Meldraths Paige", say "We Shall Never Surrender".
7. Alternative: Loot "Fine Steel Two Handed Sword" (5351) from "Meldrath's melded minions" (NPC 56174) in `steamfont`; trigger: steamfont/"Meldraths Paige", say "Your Forces Are Deafeated".
8. Alternative: Loot "Fine Steel Two Handed Sword" (5351) from "Arnold the Gnomeinator" (NPC 56175) in `steamfont`; trigger: steamfont/"Meldraths Paige", say "You Shall Not Break Our Defense".
9. Alternative: Loot "Fine Steel Two Handed Sword" (5351) from "a Freeport guard" (NPC 382255) in `freeporteast`; trigger: freeporteast/"Lythe Songbird", on timer guard.
10. Alternative: Loot "Fine Steel Two Handed Sword" (5351) from "a seasoned Freeport guard" (NPC 382256) in `freeporteast`; trigger: freeporteast/"Lythe Songbird", on timer guard.
11. Alternative: Loot "Fine Steel Two Handed Sword" (5351) from "a Freeport guard" (NPC 382255) in `freportw`; trigger: freportw/"Lythe Songbird", on timer guard.
12. Alternative: Loot "Fine Steel Two Handed Sword" (5351) from "a seasoned Freeport guard" (NPC 382256) in `freportw`; trigger: freportw/"Lythe Songbird", on timer guard.
13. Acquisition of "Water Flask" (13006) is documented under "Blackfall Blade" (60303); obtain another copy if needed.
14. Combine in Forge (17): "Fine Steel Two Handed Sword" (5351), "Water Flask" (13006). Produces "Small Brick of High Quality Ore" (10468) x2, "Small Piece of High Quality Ore" (22229). Requires Blacksmithing, trivial 21.
15. Combine in Royal Qeynos Forge (40): "Small Piece of High Quality Ore" (22229), "Water Flask" (13006). Produces "High Quality Metal Bits" (22230). Requires Blacksmithing, trivial 20.
16. Buy "Gemming Mold" (60317) from "Daria Smith" (NPC 10131) in `freporte`. Base price: 2,700 copper.
17. Combine in Forge (17): "High Quality Metal Bits" (22230), "Water Flask" (13006), "Gemming Mold" (60317). Produces "Gemming Tool" (60316). Requires Blacksmithing, trivial 115.

### "Nocturnal Mask of Acuity" (60309)

1. Buy "Jeweler's Kit" (17912) from "Svena Ironforge" (NPC 2068) in `qeynos2`. Base price: 1,000 copper.
2. Buy "Darkened Star Rose Quartz" (60308) from "Pelshia Thuxpire" (NPC 2073) in `qeynos2`. Base price: 3,000 copper.
3. Summon "Enchanted Electrum Bar" (16505) by casting "Enchant Electrum", "Mass Enchant Electrum", "Greater Mass Enchant Electrum".
4. Combine in "Jeweler's Kit" (17912): "Darkened Star Rose Quartz" (60308), "Enchanted Electrum Bar" (16505). Produces "Nocturnal Mask of Acuity" (60309). Requires Jewelry Making, trivial 103.

### "Raging Sword of Eternal Power" (60329)

1. global/"Global Player", combine recipe 19902. Sets `warrior_epic` to `21`.
2. Acquisition of "Champion's Sword of Eternal Power" (60321) is documented under "Blackfall Blade" (60303); obtain another copy if needed.
3. Loot "Kreljnok's Muddled Rage" (60322) from "Possessed Brute" in `provinggrounds`.
4. draniksscar/"Korbuk Brimblade", hand "Kreljnok's Muddled Rage" (60322). Sets `warrior_epic` to `17`.
5. Ground spawn of "Frozen Pestle" (60323) in `iceclad`.
6. iceclad/"Fazzle Thumpkin", hand "Frozen Pestle" (60323). Sets `warrior_epic` to `18`.
7. iceclad/"Fazzle Thumpkin", say "Map". Requires `warrior_epic` ==18. Gives "Fazzle's Map of East Wastes" (60324).
8. Spawns "Larnik the Recluse" (116609) in `eastwastes` on enter.
9. Loot "Larnik's Locked Purification Kit" (60325) from "Larnik the Recluse".
10. draniksscar/"Korbuk Brimblade", hand "Larnik's Locked Purification Kit" (60325). Requires `warrior_epic` >=18. Gives "Larnik's Unlocked Purification Kit" (60326).
11. Combine in "Larnik's Unlocked Purification Kit" (60326): "Kreljnok's Muddled Rage" (60322). Produces "Kreljnok's Focused Rage" (60327). The combine does not fail.
12. draniksscar/"Korbuk Brimblade", hand "Champion's Sword of Eternal Power" (60321) + "Kreljnok's Focused Rage" (60327). Requires `warrior_epic` >=19. Gives "Raging Sword of Eternal Power" (60329).

### "Sealed Vial of Blackfall Blood" (60305)

1. Kill vxed/"Blackfall Borerling". Spawns "Blackfall Borer" (290069).
2. Loot "Vial of Blackfall Blood" (60304) from "Blackfall Borer".
3. draniksscar/"Korbuk Brimblade", hand "Vial of Blackfall Blood" (60304). Requires `warrior_epic` >=3. Gives "Sealed Vial of Blackfall Blood" (60305).

### "Potion of Blackfall Spirit" (60306)

1. Acquisition of "Potion of Blackfall Spirit" (60306) is documented under "Blackfall Blade" (60303); obtain another copy if needed.

### "Glistening Hilt" (60311)

1. Acquisition of "Glistening Hilt" (60311) is documented under "Blackfall Blade" (60303); obtain another copy if needed.

### "Kreljnok's Focused Rage" (60327)

1. Acquisition of "Kreljnok's Focused Rage" (60327) is documented under "Raging Sword of Eternal Power" (60329); obtain another copy if needed.

### "Hilt of Eternal Power" (60320)

1. Acquisition of "Hilt of Eternal Power" (60320) is documented under "Blackfall Blade" (60303); obtain another copy if needed.

### `warrior_pre`

Values written: 1, 2, 3, 4, 5, 6.

1. draniksscar/"Korbuk Brimblade", say "Work". Sets `warrior_pre` to `1`.
    - Requires `warrior_pre` unset.
    - Dialogue with draniksscar/"Korbuk Brimblade":
      - Player: "Hail"
        - NPC say: You were able to purify da presence, good. Just as I thought, da essence is pure and unadultered. Things are becoming ever clearer da closer we come to unraveling this mystery. Even without touching da essence, I can see pure rage surrounding a sword. I cannot even begin to express what it looks like. It's a very powerful image, to be sure. We're not quite done yet, however. There's a bit [more] da needs to be done.
          - Reply guard: `(e.other:HasItem(60327) and qglobals["warrior_epic"] == "18")`
        - NPC say: Dat sword, there's something wrong with it. Was it my brother? This is terrible news. I had no idea he had been so corrupted by this place. I had no idea he'd turn into a monster and try to steal away dat which we have been charged to protect! Luckily you were able to stop him and recover da sword. You should keep it in your possession. I have a feeling you're da [one] I've been waiting for.
          - Reply guard: `(e.other:HasItem(60321) and qglobals["warrior_epic"] == "15")`
        - NPC message: You have gained 5 ability points!
          - Reply guard: `(e.other:HasItem(60321) and qglobals["warrior_epic"] == "15")`
        - NPC say: Well now, aren't you a meager one? Da name is Korbuk Brimblade. Have you felt anything strange lately?
          - Reply guard: ``
        - Condition: `(e.other:Class() == "Warrior")`
        - Condition: `(e.message:findi("hail"))`
        - Sets `warrior_epic` to `16`.
      - Player: "Strange" (link: explicit mention)
        - NPC say: Aha, you have sensed it as well. For a while, I believed it was just me dat noticed it. Now dat you've confirmed my suspicions, I'm sure I can move forward with my [work].
        - Condition: `(e.other:Class() == "Warrior")`
        - Condition: `(e.message:findi("strange"))`
      - Player: "Work" (link: explicit mention)
        - NPC say: Yeah, ok. You look like da respectable type. I wish it was an easy story to tell, but me thinks it's not so easy. I'm uncertain if you know da story of da red scabbard. I was named after my ancestor by da same name. In a great war, Rallos Zek bestowed to my ancestor da fabled red scabbard after Suteng was slain. It had been his charge and dat of my family to hold da scabbard until a [true warrior] would step forward to claim it as theirs once more.
          - Reply guard: `((e.other:HasItem(10910) and e.other:HasItem(10909)) or (e.other:HasItem(66176) and e.other:HasItem(66177)) or e.other:HasItem(10908) or e.other:HasItem(66175) or qglobals["warrior_pre"] == "6")`
        - NPC say: Hmm, I'm not sure if I should go into any more detail. After all, we've just met and I don't know how trustworthy you really are. Listen, if you really want to know what work I'm involved with, I'll need you to run a couple [errands] for me first, just so I know you're da real deal.
          - Reply guard: ``
          - Reply guard: `(qglobals["warrior_pre"] == nil)`
        - Condition: `(e.other:Class() == "Warrior")`
        - Condition: `(e.message:findi("work"))`
        - Sets `warrior_epic` to `1`.
        - Sets `warrior_pre` to `1`.
      - Player: "Errands" (link: explicit mention)
        - NPC say: You see, I had some things taken from me. I want to get dem back. I'm very partial to my weapons, and had some great [plans] to make a sword dat would be unmatched by any other. I thought it would be nice to start da plans with my brethren by talking to some of dem about da tactics involved in creating a sword.
        - Condition: `(e.other:Class() == "Warrior")`
        - Condition: `(e.message:findi("errands") and qglobals["warrior_pre"] == "1")`
      - Player: "Plans" (link: explicit mention)
        - NPC say: Da sword was going to be made of da finest metal with a hilt dat's handcrafted by someone I'm very close to. It was going to have my family seal engraved into da base of da blade and was to be my finest sword ever. But da plans were stolen by someone -- no doubt someone who oversees everything where I was working -- and I have yet to get them back. You look more than capable of recovering da plans for me. Hurry back when you've found dem.
        - Condition: `(e.other:Class() == "Warrior")`
        - Condition: `(e.message:findi("plans") and qglobals["warrior_pre"] == "1")`
      - Player: "Shank" (link: external event mention)
        - Prompted by `event_trade`:
          - NPC say: Ahh, da plans! You really gave it to dat overseer, huh? Not too bad, I must say. You're not done yet though. There are still a couple errands left dat I need finished. You know da most important part of any sword is da blade it's forged from, right? Well, it is. I had da perfect [shank] ready and waiting for me.
          - Event guard: `(qglobals["warrior_pre"] == "1" and item_lib.check_turn_in(e.trade, {item1 = 60285}))`
        - NPC say: I found dis shank during a battle dat raged on for many weeks. It was solid and strong, perfectly balanced and had an aura of cunning like I'd never seen before. I took it and stored it away in my vault at home. One night while I was away, a gang of pirates aboard da Hate's Fury plundered my home city and took da shank. I've heard dat it is in da hold of an undead pirate, long forgotten to da ages, so I need you to go recover it for me.
        - Condition: `(e.other:Class() == "Warrior")`
        - Condition: `(e.message:findi("shank") and qglobals["warrior_pre"] == "2")`
      - Player: "Job"
        - NPC say: I need the hilt, the blade and the plans taken to an ornery dwarf in the frozen tundra to the south. He hides among the coldain, mostly to keep himself drunk as much as possible. Unfortunately, he's the best person to combine the blade and the hilt into something I can use, so you need to find him and give him the three pieces. His name is Dardek.
        - Condition: `(e.other:Class() == "Warrior")`
        - Condition: `(e.message:findi("job") and qglobals["warrior_pre"] == "4")`
      - Player: "True Warrior" (link: explicit mention)
        - Prompted by player input: "Work"
        - NPC say: Time passed and no warrior came forth. Then da terrible scourge took hold of da ogres and we began to lose ourselves. It was then dat another ancestor of mine, Grivnok Brimblade, asked a human to take charge of da scabbard until da scourge had waned. He would know dat time when a descendant of Korbuk with da same name would come forth. It was then dat da Redblade family, led by Thegrek, took over da charge of da scabbard until I would return to [reclaim da charge] in da name of da Brimblade family.
        - Condition: `(e.other:Class() == "Warrior")`
        - Condition: `(e.message:findi("true warrior") and qglobals["warrior_epic"] ~= nil and qglobals["warrior_epic"] >= "1")`
      - Player: "Reclaim Da Charge" (link: explicit mention)
        - NPC say: It was I who returned to da Redblades, who spoke with da descendant of Thegrek. But I could not reclaim da charge. I felt a greater power, something more amazing and powerful than even da red scabbard contained. What draw I felt from da scabbard I felt ten fold from this [new source], and I was unable to explain where it was coming from. I just know dat it has drawn me here, to this place, so that I might find da answers I seek here.
        - Condition: `(e.other:Class() == "Warrior")`
        - Condition: `(e.message:findi("reclaim da charge") and qglobals["warrior_epic"] ~= nil and qglobals["warrior_epic"] >= "1")`
      - Player: "New Source" (link: explicit mention)
        - NPC say: I can't express who or what it is dat is drawing me here. I only know dat this is where I must be. I feel as though this is something like da scabbard, but more powerful. Perhaps it is a new weapon? If so, I must be da one to lead da charge to protect its power until da right warrior comes along to claim it. Just as my family led da charge so long ago to protect da red scabbard, so shall I continue it with this new journey. Are you [willing to help] knowing all dat?
        - Condition: `(e.other:Class() == "Warrior")`
        - Condition: `(e.message:findi("new source") and qglobals["warrior_epic"] ~= nil and qglobals["warrior_epic"] >= "1")`
      - Player: "Willing To Help" (link: explicit mention)
        - NPC say: I had hoped so. Let's get started then. It seems the powerful lure is greatest when I am at this point, so I must remain here to ensure dat I can keep a grasp on where it resides. I'm hoping dat after you return with whatever you can find, I'll be able to uncover more information. From time to time, I get flashes of da things dat we need to find, like da picture of a place or a [thing]...
        - Condition: `(e.other:Class() == "Warrior")`
        - Condition: `(e.message:findi("willing to help") and qglobals["warrior_epic"] ~= nil and qglobals["warrior_epic"] >= "1")`
      - Player: "Thing" (link: explicit mention)
        - NPC say: Just now I had a flash of a book, or pages of a book. Just as quickly as the book was there, it split into da cover and three pages and then fell to da ground. I wonder if dat's going to happen often... In any case, maybe you should have a look around to see if you can find any pages from a book that are on da ground. Return to me if you find them.
        - Condition: `(e.other:Class() == "Warrior")`
        - Condition: `(e.message:findi("thing") and qglobals["warrior_epic"] ~= nil and qglobals["warrior_epic"] >= "1")`
      - Player: "Rock" (link: external event mention)
        - Prompted by `event_trade`:
          - NPC say: Things are getting stranger by da moment. I just had a vision of a creature dat wanders about da area below, then it went dark. I'm not sure if this creature is part of everything else, but it certainly is something we should check out. I know it seems silly, but you should have this [rock].
          - Event guard: `(qglobals["warrior_epic"] ~= nil)`
          - Event guard: `(qglobals["warrior_epic"] >= "2" and item_lib.check_turn_in(e.trade, {item1 = 60299}))`
        - NPC say: I was holding da rock when I had dat vision. Whatever happened to me was passed into da rock as well and I can sense some power within da rock now. Maybe holding da rock will lead you to da creature or maybe it will lead you to something near da creature, I don't really know. You have to keep a tight grip on it though, else I don't think you'll feel da power drawing you as I did. If you do find da beast, be careful. There's no telling what dangers lay in this place.
        - Condition: `(e.other:Class() == "Warrior")`
        - Condition: `(e.message:findi("rock") and qglobals["warrior_epic"] ~= nil and qglobals["warrior_epic"] >= "2")`
        - Gives Energy Receptor (60300).
      - Player: "Smith"
        - NPC say: Blacksmith, yes. She's dealt with some of da more interesting things I've needed worked on lately and I know she'll be able to help with dat ore as well. She's in Nedaria's Landing, so you shouldn't have a lot of trouble finding her. Give her da ore and these smelting plans, she should know what to do wit them from there.
        - Condition: `(e.other:Class() == "Warrior")`
        - Condition: `(e.message:findi("smith") and qglobals["warrior_epic"] ~= nil and qglobals["warrior_epic"] >= "2")`
      - Player: "Loose" (link: external event mention)
        - Prompted by `event_trade`:
          - NPC say: What a fine looking blade, I must say dat smith did good work in such a short time. Hopefully it wasn't too much touble for you. I... oh my, this can't be good. Da creature... it's [loose]!
          - Event guard: `(qglobals["warrior_epic"] ~= nil)`
          - Event guard: `(qglobals["warrior_epic"] >= "2" and item_lib.check_turn_in(e.trade, {item1 = 60303}))`
        - NPC say: Somehow da creature dat left da ore has made its way back to Norrath and is tearing through da mountainsides! You have to head it off in da crumbling caverns of Vxed before it can get any further! Be careful, though. I had a vision of some of its spawn with it so you may have to take care of more than just da one creature when you get there. Now Hurry!
        - Condition: `(e.other:Class() == "Warrior")`
        - Condition: `(e.message:findi("loose") and qglobals["warrior_epic"] ~= nil and qglobals["warrior_epic"] >= "3")`
        - Sets `warrior_epic_vxed` to `1`.
      - Player: "Journey" (link: explicit mention)
        - Prompted by player input: "New Source"
        - NPC say: I noticed dat da blood gave me some kind of feeling. I'm not sure whether it was da same magic dat's been giving me visions or something new, but I'd like you to take it to a shaman I knew briefly growing up. He's a friend of da Redblade family and I'm sure he'd be willing to help. Just tell him I sent you. His name is Kimber Whitefoot and you shouldn't have trouble finding him, he's a very large barbarian.
        - Condition: `(e.other:Class() == "Warrior")`
        - Condition: `(e.message:findi("journey") and qglobals["warrior_epic"] ~= nil and qglobals["warrior_epic"] >= "3")`
      - Player: "Vision" (link: explicit mention)
        - NPC say: Da vision I had showed me an impish creature. It was dark and twisted and seemed to devour energy from da chaos surrounding us. I don't know what part it plays in this, but like everything else, I'm sure it's important. Perhaps there is another portal around dat was destroyed, like it was in Taelosia. See if you can find it and look for da creature there, then return to me whatever it may have in its possession dat we can use.
        - Condition: `(e.other:Class() == "Warrior")`
        - Condition: `(e.message:findi("vision") and qglobals["warrior_epic"] ~= nil and qglobals["warrior_epic"] >= "3")`
      - Player: "Cleaning up da hilt?" (link: external event mention)
        - Prompted by `event_trade`:
          - NPC say: What a worthless specimen this is. I don't understand why my vision would show me dat creature if all it had was this mediocre quality hilt. I also don't understand why there's energy emanating from da hilt when it cannot be used to wield a blade in its current state. I think we're going to have to look into [cleaning up da hilt].
          - Event guard: `(qglobals["warrior_epic"] ~= nil)`
          - Event guard: `(qglobals["warrior_epic"] >= "5" and item_lib.check_turn_in(e.trade, {item1 = 60307}))`
        - NPC say: Right now it would fall apart if you tried to attach a blade to it. We're going to put some luster back into da hilt and I think I may know someone who can do it. I don't remember her name or even where I found her, but I do remember running into a [shady jeweler] on da outskirts of one of the larger cities of Kunark.
        - Condition: `(e.other:Class() == "Warrior")`
        - Condition: `(e.message:findi("Cleaning up da hilt?") and qglobals["warrior_epic"] ~= nil and qglobals["warrior_epic"] >= "6")`
      - Player: "Shady Jeweler" (link: explicit mention)
        - NPC say: She worked on da outskirts to sell to less reputable individuals, like myself. She didn't live on the outskirts though, only worked there. I want to say she was part of da port authority, but I can't quite remember. I also don't remember her name, or if I even ever knew it, but I do remember dat she was one of da best I ever dealt with. Take da hilt to her, if you can find her, and see what she can do with it. One more thing, she's a fan of her own tongues, so be prepared for dat when you speak with her.
        - Condition: `(e.other:Class() == "Warrior")`
        - Condition: `(e.message:findi("shady jeweler") and qglobals["warrior_epic"] ~= nil and qglobals["warrior_epic"] >= "6")`
      - Player: "Glimpse"
        - NPC say: It was a series of images, really. One was of a [young combatant] within da Muramite ranks. One was of a [gorge] somewhere. Da third was a [maze] of some sort, and da final one was in a [field of blood] . At da end, I saw four eyes dat appeared in da center of da hilt. I'm guessing da eyes go in those four holes on each side of da hilt and dat one each can be found in those four places.
        - Condition: `(e.other:Class() == "Warrior")`
        - Condition: `(e.message:findi("glimpse") and qglobals["warrior_epic"] ~= nil and qglobals["warrior_epic"] >= "10")`
      - Player: "Young Combatant" (link: explicit mention)
        - NPC say: I noticed a creature dat walked like a man but looked like a dragon and was near a fortress. I can't say where exactly it was, but I can say it was a powerful looking creature unchanged by da onslaught of war. I'm guessing he is a relatively new champion of their people.
        - Condition: `(e.other:Class() == "Warrior")`
        - Condition: `(e.message:findi("young combatant") and qglobals["warrior_epic"] ~= nil and qglobals["warrior_epic"] >= "10")`
      - Player: "Gorge" (link: explicit mention)
        - Prompted by player input: "Glimpse"
        - NPC say: Giant creatures lumbered over da eye. I can't really say much else because dat's all I saw. They were massive and didn't look terribly friendly.
        - Condition: `(e.other:Class() == "Warrior")`
        - Condition: `(e.message:findi("gorge") and qglobals["warrior_epic"] ~= nil and qglobals["warrior_epic"] >= "10")`
      - Player: "Maze" (link: explicit mention)
        - Prompted by player input: "Glimpse"
        - NPC say: Near a great crystal tower within da maze, I saw da eye gleaming up at da sky. You should take caution because da tower is unlike any I've ever seen before.
        - Condition: `(e.other:Class() == "Warrior")`
        - Condition: `(e.message:findi("maze") and qglobals["warrior_epic"] ~= nil and qglobals["warrior_epic"] >= "10")`
      - Player: "Field Of Blood" (link: explicit mention)
        - Prompted by player input: "Glimpse"
        - NPC say: In a field of blood, near a large fortress, you'll find da fourth eye, though it may be out of da sight of prying eyes.
        - Condition: `(e.other:Class() == "Warrior")`
        - Condition: `(e.message:findi("field of blood") and qglobals["warrior_epic"] ~= nil and qglobals["warrior_epic"] >= "10")`
      - Player: "Another Image" (link: external event mention)
        - Prompted by `event_trade`:
          - NPC say: Met up with Gridbar did you? He's an oddball, for certain, but he's da best at what he does. I don't think I've ever seen stones set so finely into anything before, wouldn't you say? Alrighty, I think... wow [another image]...
          - Event guard: `(qglobals["warrior_epic"] ~= nil)`
          - Event guard: `(qglobals["warrior_epic"] >= "13" and item_lib.check_turn_in(e.trade, {item1 = 60320}))`
        - NPC say: This one is of da completed sword. It's not too shabby, but it's not great either. It looks like there will be more dat needs to be done than just what we have so far. In any case, I know how to get da sword put back together. It'll involve a trip to see my brother, [Krekk].
        - Condition: `(e.other:Class() == "Warrior")`
        - Condition: `(e.message:findi("another image") and qglobals["warrior_epic"] ~= nil and qglobals["warrior_epic"] >= "14")`
      - Player: "Krekk" (link: explicit mention)
        - NPC say: He's become one of da finest sword makers I've ever known. He'll know just how to put da hilt and da sword together to make a finely balanced weapon. He had come with me to this place, but went ahead to find new and precious metals he could use to make new blades. I think he mentioned visiting a ruined city somewhere, but I'm not certain.
        - Condition: `(e.other:Class() == "Warrior")`
        - Condition: `(e.message:findi("krekk") and qglobals["warrior_epic"] ~= nil and qglobals["warrior_epic"] >= "14")`
      - Player: "One" (link: explicit mention)
        - NPC say: Only da one who had da power to combine da sword could have come so far. You have it in you to make dat sword great! Right now, its power is minor. With some time and effort, you might be able to bring it into da light and make it da most powerful sword ever known! When I touched da sword, I sensed a [presence] within it.
        - Condition: `(e.other:Class() == "Warrior")`
        - Condition: `(e.message:findi("one") and qglobals["warrior_epic"] == "16")`
      - Player: "Presence" (link: explicit mention)
        - NPC say: I can't explain it really. It's as if da sword was part of a being at one time. Perhaps da sword was a being but was changed into a sword by some terrible means. All I know is dat it keeps calling to me, leading me... and you... to da next step of da puzzle. Right now it's telling me dat da next step of da puzzle resides in da labryinth. We've already been there, I wonder what more we could find from [going back].
        - Condition: `(e.other:Class() == "Warrior")`
        - Condition: `(e.message:findi("presence") and qglobals["warrior_epic"] == "16")`
      - Player: "Going Back" (link: explicit mention)
        - NPC say: Well, if you want to continue, you'll go back. Da vision I had showed a beast possessed by an evil spirit. It almost seemed like dat spirit was part of da presence dat I've felt from da sword. You should find da beast and destroy it, then see if you can recapture whatever spirit is trapped in its body.
        - Condition: `(e.other:Class() == "Warrior")`
        - Condition: `(e.message:findi("going back") and qglobals["warrior_epic"] == "16")`
      - Player: "Purification Expert" (link: external event mention)
        - Prompted by `event_trade`:
          - NPC say: All too easy. For you, I mean. You did well. I'm... I'm getting unclear visions from this essence. I can't seem to understand what it's trying to tell me. This essence is impure and needs to be purified. I happen to know of a [purification expert] dat can help us clear this mystery up.
          - Event guard: `(qglobals["warrior_epic"] ~= nil)`
          - Event guard: `(qglobals["warrior_epic"] >= "16" and item_lib.check_turn_in(e.trade, {item1 = 60322}))`
        - NPC say: You're going to need to travel to da frozen underbelly of Norrath to find a gnome I've not seen in a long time. I couldn't begin to tell you where to find him, but you might try da frozen ocean as a starting point. If you can't find him, you may be able to find someone else who knows where he is.
        - Condition: `(e.other:Class() == "Warrior")`
        - Condition: `(e.message:findi("purification expert") and qglobals["warrior_epic"] == "17")`
      - Player: "Kit" (link: external event mention)
        - Prompted by `event_trade`:
          - NPC say: Uh oh. I'm guessing dat he didn't want to part with this peacefully? Well, I can't say I'm sorry. He was a jerk to me da last time we talked. I guess I just figured someone else might be able to persuade him to change his mind. I went ahead and broke open da lock for you. You'll be able to make use of da [kit] now.
          - Event guard: `(qglobals["warrior_epic"] ~= nil)`
          - Event guard: `(qglobals["warrior_epic"] >= "18" and item_lib.check_turn_in(e.trade, {item1 = 60325}))`
        - NPC say: Da kit you got from Larnik was his very special and highly prized purification kit, used to remove impurities from magical things, such as da essence you gathered from dat possessed beast. I'm guessing it will work with dat too, so just place da essence inside and let it go to work.
        - Condition: `(e.other:Class() == "Warrior")`
        - Condition: `(e.message:findi("kit") and qglobals["warrior_epic"] == "18")`
      - Player: "More" (link: explicit mention)
        - Prompted by player input: "Hail"
        - NPC say: I have sensed a strong and powerful draw from da fallen palace to da north. I've heard whispers dat it is called Anguish and is a terrible place to go. I don't know any more than dat, except dat there is... something there. My visions about this are chaotic and I don't know what to make of them. Be careful, there's no telling what may lie in wait for you there.
        - Condition: `(e.other:Class() == "Warrior")`
        - Condition: `(e.message:findi("more") and qglobals["warrior_epic"] == "18")`
      - Player: "Last Items"
        - NPC say: First, it's time for me to put my strengths to use. Hand me da sword, and da essence and I'll let da magic of these visions flow through me and into the sword. After dat, you must let da sword guide you to da end of your journey. I know now dat you are da one who will fulfill this journey, who will see it through to da end. Hurry forth into da causeway, do not stray. Then, and only then will da power of da sword be fully realized. Hurry now, you don't have much time!
        - Condition: `(e.other:Class() == "Warrior")`
        - Condition: `(e.message:findi("last items") and qglobals["warrior_epic"] == "19")`
      - Player: "Last Item"
        - NPC say: You must let da sword guide you to da end of your journey. I know now that you are da one who will fulfill this journey, who will see it through to da end. Hurry forth into da causeway and seek out dat which will end your journey. Then, and only then will da power of da sword be fully realized. Hurry now, you don't have much time!
        - Condition: `(e.other:Class() == "Warrior")`
        - Condition: `(e.message:findi("last item") and qglobals["warrior_epic"] == "20")`

2. draniksscar/"Korbuk Brimblade", hand "Korbuk's Weapon Plans" (60285). Sets `warrior_pre` to `2`.
    - Requires `warrior_pre` ==1.
    - Hand in x1: "Korbuk's Weapon Plans" (60285).
    - Loot "Korbuk's Weapon Plans" (60285) from "The Diaku Overseer" in `potactics`.
    - Gives "Korbuk's Weapon Plans" (60285).

3. draniksscar/"Korbuk Brimblade", hand "Elegant Shank" (60286). Sets `warrior_pre` to `3`.
    - Requires `warrior_pre` ==2.
    - Hand in x1: "Elegant Shank" (60286).
    - Loot "Elegant Shank" (60286) from "Shoqui the Forgotten" in `hatesfury`.
    - Gives "Elegant Shank" (60286).

4. draniksscar/"Korbuk Brimblade", hand "Emblazoned Champion's Hilt" (60288). Sets `warrior_pre` to `4`.
    - Requires `warrior_pre` ==3.
    - Hand in x1: "Emblazoned Champion's Hilt" (60288).
    - Prerequisite: "Emblazoned Champion's Hilt" (60288). See section 0.
    - Gives "Emblazoned Champion's Hilt" (60288).

5. thurgadina/"Dardek Bladewright", hand "Korbuk's Weapon Plans" (60285) + "Elegant Shank" (60286) + "Emblazoned Champion's Hilt" (60288). Sets `warrior_pre` to `5`.
    - Requires `warrior_pre` ==4.
    - Hand in x1: "Korbuk's Weapon Plans" (60285).
    - Hand in x1: "Elegant Shank" (60286).
    - Hand in x1: "Emblazoned Champion's Hilt" (60288).
    - Loot "Korbuk's Weapon Plans" (60285) from "The Diaku Overseer" in `potactics`.
    - Loot "Elegant Shank" (60286) from "Shoqui the Forgotten" in `hatesfury`.
    - Prerequisite: "Emblazoned Champion's Hilt" (60288). See section 0.
    - Gives "Dardek's Forged Blade" (60292).
    - Dialogue with thurgadina/"Dardek Bladewright":
      - Player: "Hail"
        - NPC say: Yeah, I'm Dardek. What d' ye want?! Can't ye see I'm not in t' mood fer talkin'? Bah, t' heck with ye. If'n ye get me a nice hot cup of m' favorite coffee, I might be willin' to talk with ye for a few minutes. Hurry up now, Coldain Coffee! It's t' only thing I'll drink!
        - Condition: `(e.message:findi("hail"))`

6. draniksscar/"Korbuk Brimblade", hand "Dardek's Forged Blade" (60292). Sets `warrior_pre` to `6`.
    - Requires `warrior_pre` ==5.
    - Hand in x1: "Dardek's Forged Blade" (60292).
    - Prerequisite: "Dardek's Forged Blade" (60292). See section 0.
    - Gives "Korbuk's Blade of Mastery" (60293).

#### Steps on `warrior_pre` that do not change it

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

### `warrior_epic`

Values written: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21.

1. draniksscar/"Korbuk Brimblade", say "Work". Sets `warrior_epic` to `1`.
    - Requires `warrior_epic` unset.
    - Requires `warrior_pre` ==6.

    - Subquest `warrior_pre` documented earlier.
2. draniksscar/"Korbuk Brimblade", hand "Decomposing Page I" (60295) + "Decomposing Page II" (60296) + "Decomposing Page III" (60297) + "Decomposing Cover" (60298). Sets `warrior_epic` to `2`.
    - Requires `warrior_epic` >=1.
    - Hand in x1: "Decomposing Page I" (60295).
    - Hand in x1: "Decomposing Page II" (60296).
    - Hand in x1: "Decomposing Page III" (60297).
    - Hand in x1: "Decomposing Cover" (60298).
    - Ground spawn of "Decomposing Page I" (60295) in `draniksscar`.
    - Ground spawn of "Decomposing Page II" (60296) in `draniksscar`.
    - Ground spawn of "Decomposing Page III" (60297) in `draniksscar`.
    - Ground spawn of "Decomposing Cover" (60298) in `draniksscar`.
    - Gives "Decomposing Page I" (60295).
    - Gives "Decomposing Page II" (60296).
    - Gives "Decomposing Page III" (60297).
    - Gives "Decomposing Cover" (60298).

3. draniksscar/"Korbuk Brimblade", hand "Blackfall Blade" (60303). Sets `warrior_epic` to `3`.
    - Requires `warrior_epic` >=2.
    - Hand in x1: "Blackfall Blade" (60303).
    - Prerequisite: "Blackfall Blade" (60303). See section 0.
    - Gives "Blackfall Blade" (60303).

4. everfrost/"Kimber Whitefoot", hand "Sealed Vial of Blackfall Blood" (60305). Sets `warrior_epic` to `4`.
    - Requires `warrior_epic` set.
    - Requires `warrior_epic` >=3.
    - Requires `warrior_epic` <4.
    - Hand in x1: "Sealed Vial of Blackfall Blood" (60305).
    - Prerequisite: "Sealed Vial of Blackfall Blood" (60305). See section 0.
    - Dialogue with everfrost/"Kimber Whitefoot":
      - Player: "Hail"
        - NPC say: Yes, yes, you again. I had a chance to examine the vial you gave me. Quite an interesting substance, I must say. Scary though. Where did you say you found it? Never mind, it's not important. I made a potion out of the vial, but I can feel an evil presence within. I want to be rid of it, so you can have it back. Please don't come to me with anything like that again. I'm really not into dealing with spirits of such heinous design. Good luck.
        - Condition: `e.message:findi("hail") and qglobals["warrior_epic"] ~= nil and qglobals["warrior_epic"] >= "4"`
        - Gives Potion of Blackfall Spirit (60306).
      - Player: "Hail"
        - NPC say: Yes, yes, you again. I had a chance to examine the vial you gave me. Quite an interesting substance, I must say. Scary though. Where did you say you found it? Never mind, it's not important. I made a potion out of the vial, but I can feel an evil presence within. I want to be rid of it, so you can have it back. Please don't come to me with anything like that again. I'm really not into dealing with spirits of such heinous design. Good luck.
        - Condition: `(e.message:findi("hail") and qglobals["warrior_epic"] ~= nil and qglobals["warrior_epic"] >= "4")`
        - Gives Potion of Blackfall Spirit (60306).

5. draniksscar/"Korbuk Brimblade", hand "Potion of Blackfall Spirit" (60306). Sets `warrior_epic` to `5`.
    - Requires `warrior_epic` >=4.
    - Hand in x1: "Potion of Blackfall Spirit" (60306).
    - Prerequisite: "Potion of Blackfall Spirit" (60306). See section 0.
    - Gives "Potion of Blackfall Spirit" (60306).

6. draniksscar/"Korbuk Brimblade", hand "Decrepit Hilt" (60307). Sets `warrior_epic` to `6`.
    - Requires `warrior_epic` >=5.
    - Hand in x1: "Decrepit Hilt" (60307).
    - Kill bloodfields/"Girplan Slasher". Spawns "Girplan Devourer" (301063).
    - Loot "Decrepit Hilt" (60307) from "Girplan Devourer".
    - Gives "Decrepit Hilt" (60307).

7. firiona/"Corfia Nultethen", hand "Platinum Bar" (16503). Sets `warrior_epic` to `7`.
    - Requires `warrior_epic` set.
    - Requires `warrior_epic` >=6.
    - Requires `warrior_epic` <7.
    - Hand in x1: "Platinum Bar" (16503).
    - Buy "Platinum Bar" (16503) from "Ziska Ironforge" (NPC 2069) in `qeynos2`. Base price: 100,000 copper.
    - Dialogue with firiona/"Corfia Nultethen":
      - Player: "Hail"
        - NPC say: Yes, what can I do for you?
        - Condition: `e.language == 12 and e.other:GetLanguageSkill(12) >= 100`
        - Condition: `e.message:findi("hail")`
      - Player: "Korbuk sent me" (link: conversation sequence)
        - NPC say: That's really quite fascinating, but doesn't mean a whole lot to me. I really don't care who sent you. You don't have any [items of value] to me, so be gone.
        - Condition: `e.language == 12 and e.other:GetLanguageSkill(12) >= 100`
        - Condition: `e.message:findi("Korbuk sent me") and qglobals["warrior_epic"] ~= nil and qglobals["warrior_epic"] >= "6"`
      - Player: "Items Of Value" (link: explicit mention)
        - NPC say: Well... if you must know, I'm in need of a platinum bar so I can continue my work.
        - Condition: `e.language == 12 and e.other:GetLanguageSkill(12) >= 100`
        - Condition: `e.message:findi("items of value") and qglobals["warrior_epic"] ~= nil and qglobals["warrior_epic"] >= "6"`
      - Player: "Nocturnal Mask of Acuity" (link: external event mention)
        - Prompted by `event_trade`:
          - NPC say: Aha, something worth my time. But I've changed my mind. I'd prefer if you made me something that really showed me how interested you are in my craft. We jewelers are hard to please, but if you can present me with a [Nocturnal Mask of Acuity], I'd be more than willing to at least speak with you.
          - Event guard: `qglobals["warrior_epic"] ~= nil and qglobals["warrior_epic"] >= "6" and item_lib.check_turn_in(e.trade, {item1 = 16503})`
        - NPC say: The mask is an interesting blend that will allow me to see much better in the darkness, where we elves can sometimes have trouble. To make it, you'll need an enchanted electrum bar and two darkened star rose quartz. Show it to me when you've made it.
        - Condition: `e.language == 12 and e.other:GetLanguageSkill(12) >= 100`
        - Condition: `e.message:findi("Nocturnal Mask of Acuity") and qglobals["warrior_epic"] ~= nil and qglobals["warrior_epic"] >= "7"`
      - Player: "Favor" (link: external event mention)
        - Prompted by `event_trade`:
          - NPC say: What a filthy piece of rubbish! This will need a good deal of work, I can guarantee you that. I have a small repository of supplies that I only rarely use, and one of the things I have is a cleaning solution. I don't often use it for most mundane things, but I'd be willing to part with some if you're willing to do me a [favor].
          - Event guard: `qglobals["warrior_epic"] ~= nil and qglobals["warrior_epic"] >= "8" and item_lib.check_turn_in(e.trade, {item1 = 60307})`
        - NPC say: Yes indeed. I've been spending such a long time in the city lately that I just haven't had time to go on the expeditions I used to. Such a strong and capable person as you would be able to fill in nicely. You see, I've always wanted to explore the depths of [Veksar] to find out what treasures are hidden down there.
        - Condition: `e.language == 12 and e.other:GetLanguageSkill(12) >= 100`
        - Condition: `e.message:findi("favor") and qglobals["warrior_epic"] ~= nil and qglobals["warrior_epic"] >= "9"`
      - Player: "Veksar" (link: explicit mention)
        - NPC say: I've heard plenty of stories and read a number of tales about artifacts of great wealth down there. In fact, I was able to get a sneak peek into the ruins some time ago, but not enough to find what I needed. One of the most interesting things I've read about is a tome of bones made for a necromancer named [Galuk Drek].
        - Condition: `e.language == 12 and e.other:GetLanguageSkill(12) >= 100`
        - Condition: `e.message:findi("veksar") and qglobals["warrior_epic"] ~= nil and qglobals["warrior_epic"] >= "9"`
      - Player: "Galuk Drek" (link: explicit mention)
        - NPC say: Oh, he was a beast, to be sure. One of the nastier creatures down there, but also one of the most brilliant, from what I've read. Drek kept the tome full of information on various crafts, and one of them just happens to be jewelcraft. I'd love to set my hands on that tome, and if you can find it, I'd be more than willing to finish up this hilt for you in no time!
        - Condition: `e.language == 12 and e.other:GetLanguageSkill(12) >= 100`
        - Condition: `e.message:findi("Galuk Drek") and qglobals["warrior_epic"] ~= nil and qglobals["warrior_epic"] >= "9"`
        - Sets `warrior_epic_veksar` to `1`.

8. firiona/"Corfia Nultethen", hand "Nocturnal Mask of Acuity" (60309). Sets `warrior_epic` to `8`.
    - Requires `warrior_epic` set.
    - Requires `warrior_epic` >=7.
    - Requires `warrior_epic` <8.
    - Hand in x1: "Nocturnal Mask of Acuity" (60309).
    - Prerequisite: "Nocturnal Mask of Acuity" (60309). See section 0.

9. firiona/"Corfia Nultethen", hand "Decrepit Hilt" (60307). Sets `warrior_epic` to `9`.
    - Requires `warrior_epic` set.
    - Requires `warrior_epic` >=8.
    - Requires `warrior_epic` <9.
    - Hand in x1: "Decrepit Hilt" (60307).
    - Kill bloodfields/"Girplan Slasher". Spawns "Girplan Devourer" (301063).
    - Loot "Decrepit Hilt" (60307) from "Girplan Devourer".

10. draniksscar/"Korbuk Brimblade", hand "Glistening Hilt" (60311). Sets `warrior_epic` to `10`.
    - Requires `warrior_epic` >=9.
    - Hand in x1: "Glistening Hilt" (60311).
    - Prerequisite: "Glistening Hilt" (60311). See section 0.
    - Gives "Glistening Hilt" (60311).

11. draniksscar/"Korbuk Brimblade", hand "Stone of Eternal Power: Northeast Eye" (60312) + "Stone of Eternal Power: Northwest Eye" (60313) + "Stone of Eternal Power: Southeast Eye" (60314) + "Stone of Eternal Power: Southwest Eye" (60315). Sets `warrior_epic` to `11`.
    - Requires `warrior_epic` ==10.
    - Hand in x1: "Stone of Eternal Power: Northeast Eye" (60312).
    - Hand in x1: "Stone of Eternal Power: Northwest Eye" (60313).
    - Hand in x1: "Stone of Eternal Power: Southeast Eye" (60314).
    - Hand in x1: "Stone of Eternal Power: Southwest Eye" (60315).
    - Loot "Stone of Eternal Power: Northeast Eye" (60312) from "Dragorn Champion" in `wallofslaughter`.
    - Ground spawn of "Stone of Eternal Power: Northwest Eye" (60313) in `bloodfields`.
    - Ground spawn of "Stone of Eternal Power: Southeast Eye" (60314) in `provinggrounds`.
    - Ground spawn of "Stone of Eternal Power: Southwest Eye" (60315) in `causeway`.
    - Gives "Stone of Eternal Power: Northeast Eye" (60312).
    - Gives "Stone of Eternal Power: Northwest Eye" (60313).
    - Gives "Stone of Eternal Power: Southeast Eye" (60314).
    - Gives "Stone of Eternal Power: Southwest Eye" (60315).

12. butcher/"Gridbar Galund", hand "Stone of Eternal Power: Northeast Eye" (60312) + "Stone of Eternal Power: Northwest Eye" (60313) + "Stone of Eternal Power: Southeast Eye" (60314) + "Stone of Eternal Power: Southwest Eye" (60315). Sets `warrior_epic` to `12`.
    - Requires `warrior_epic` set.
    - Requires `warrior_epic` >=11.
    - Hand in x1: "Stone of Eternal Power: Northeast Eye" (60312).
    - Hand in x1: "Stone of Eternal Power: Northwest Eye" (60313).
    - Hand in x1: "Stone of Eternal Power: Southeast Eye" (60314).
    - Hand in x1: "Stone of Eternal Power: Southwest Eye" (60315).
    - Loot "Stone of Eternal Power: Northeast Eye" (60312) from "Dragorn Champion" in `wallofslaughter`.
    - Ground spawn of "Stone of Eternal Power: Northwest Eye" (60313) in `bloodfields`.
    - Ground spawn of "Stone of Eternal Power: Southeast Eye" (60314) in `provinggrounds`.
    - Ground spawn of "Stone of Eternal Power: Southwest Eye" (60315) in `causeway`.
    - Dialogue with butcher/"Gridbar Galund":
      - Player: "Hail"
        - NPC say: Hiya there. Oh me oh my, never mind. Huh? What can I do for ya? Er... wow, look at that bright... huh? I'm here! Hi! Are you looking for Gridbar? I think he's around here somewhere...
        - Condition: `e.message:findi("hail") and qglobals["warrior_epic"] ~= nil and qglobals["warrior_epic"] >= "11"`
      - Player: "Korbuk sent me" (link: conversation sequence)
        - NPC say: Ooh, Korbuk. Big and important, yes. Gridbar should know what Korbuk wants. You say your name is Korbuk? Or did you say you were Gridbar? Huh? Who are you? Right, Korbuk. Did you bring the stones?
        - Condition: `e.message:findi("Korbuk sent me") and qglobals["warrior_epic"] ~= nil and qglobals["warrior_epic"] >= "11"`
      - Player: "Gemming Tool" (link: external event mention)
        - Prompted by `event_trade`:
          - NPC say: Ah... huh? Oh, Gridbar says he needs a [gemming tool]. Who? What do you want? Something about Korbuk? Where's Gridbar? He says you need a [spell called Fire]. Huh? Gridbar who? No cookies for me now, thanks. Huh?
          - Event guard: `qglobals["warrior_epic"] ~= nil and qglobals["warrior_epic"] >= "11" and item_lib.check_turn_in(e.trade, {item1 = 60312, item2 = 60313, item3 = 60314, item4 = 60315})`
        - NPC say: Yes, yes. Gemming tool. Very strong... huh? Korbuk wants a cookie? Where's Gridbar? Gridbar who? I know I'm a horse, so what? Huh? Right, tool. Need a flask of water... huh? Two high quality metal bits. Where's the beef? One gemming mold. Cook them in a forge, you got yourself a... what? Tool, gemming tool.
        - Condition: `e.message:findi("gemming tool") and qglobals["warrior_epic"] ~= nil and qglobals["warrior_epic"] >= "13"`
      - Player: "Spell Called Fire" (link: external event mention)
        - Prompted by `event_trade`:
          - NPC say: Ah... huh? Oh, Gridbar says he needs a [gemming tool]. Who? What do you want? Something about Korbuk? Where's Gridbar? He says you need a [spell called Fire]. Huh? Gridbar who? No cookies for me now, thanks. Huh?
          - Event guard: `qglobals["warrior_epic"] ~= nil and qglobals["warrior_epic"] >= "11" and item_lib.check_turn_in(e.trade, {item1 = 60312, item2 = 60313, item3 = 60314, item4 = 60315})`
        - NPC say: Can buy it from a... what? Wow! Look at the stars! What stars? Where's Korbuk? Who are you?! Buy from a shop. Someone has it. Not me. Maybe Gridbar.
        - Condition: `e.message:findi("spell called fire") and qglobals["warrior_epic"] ~= nil and qglobals["warrior_epic"] >= "13"`

13. butcher/"Gridbar Galund", hand "Spell: Fire" (15433) + "Gemming Tool" (60316). Sets `warrior_epic` to `13`.
    - Requires `warrior_epic` set.
    - Requires `warrior_epic` >=12.
    - Hand in x1: "Gemming Tool" (60316).
    - Hand in x1: "Spell: Fire" (15433).
    - Prerequisite: "Gemming Tool" (60316). See section 0.
    - Buy "Spell: Fire" (15433) from "Tisiana" (NPC 27062) in `lavastorm`. Base price: 20,637 copper.

14. draniksscar/"Korbuk Brimblade", hand "Hilt of Eternal Power" (60320). Sets `warrior_epic` to `14`.
    - Requires `warrior_epic` >=13.
    - Hand in x1: "Hilt of Eternal Power" (60320).
    - Prerequisite: "Hilt of Eternal Power" (60320). See section 0.
    - Gives "Hilt of Eternal Power" (60320).

15. dranik/"Krekk Brimblade", hand "Blackfall Blade" (60303) + "Potion of Blackfall Spirit" (60306) + "Hilt of Eternal Power" (60320). Sets `warrior_epic` to `15`.
    - Requires `warrior_epic` ==14.
    - Hand in x1: "Hilt of Eternal Power" (60320).
    - Hand in x1: "Potion of Blackfall Spirit" (60306).
    - Hand in x1: "Blackfall Blade" (60303).
    - Prerequisite: "Hilt of Eternal Power" (60320). See section 0.
    - Prerequisite: "Potion of Blackfall Spirit" (60306). See section 0.
    - Prerequisite: "Blackfall Blade" (60303). See section 0.
    - Dialogue with dranik/"Krekk Brimblade":
      - Player: "Hail"
        - Condition: `(e.message:findi("hail") and qglobals["warrior_epic"] == "15")`

16. draniksscar/"Korbuk Brimblade", say "Hail". Sets `warrior_epic` to `16`.
    - Requires `warrior_epic` ==15.
    - Requires "Champion's Sword of Eternal Power" (60321).
    - Loot "Champion's Sword of Eternal Power" (60321) from "Krekk Brimblade" in `dranik`.

17. draniksscar/"Korbuk Brimblade", hand "Kreljnok's Muddled Rage" (60322). Sets `warrior_epic` to `17`.
    - Requires `warrior_epic` >=16.
    - Hand in x1: "Kreljnok's Muddled Rage" (60322).
    - Loot "Kreljnok's Muddled Rage" (60322) from "Possessed Brute" in `provinggrounds`.
    - Gives "Kreljnok's Muddled Rage" (60322).

18. iceclad/"Fazzle Thumpkin", hand "Frozen Pestle" (60323). Sets `warrior_epic` to `18`.
    - Requires `warrior_epic` ==17.
    - Hand in x1: "Frozen Pestle" (60323).
    - Ground spawn of "Frozen Pestle" (60323) in `iceclad`.
    - Dialogue with iceclad/"Fazzle Thumpkin":
      - Player: "Hail"
        - NPC say: Damnable interruptions! Can't you see I'm looking for my pestle?! I lost that blasted thing months ago and haven't been able to find it! What will I do without my pestle?! My poor, poor pestle. Where have you gone? I thought I'd lost it around here somewhere, but maybe I left it near one of those statues during my surveying of the islands. Drat and double drat! Where did I leave you? Woe...
          - Reply guard: `(qglobals["warrior_epic"] == "17")`
        - Condition: `(e.other:Class() == "Warrior")`
        - Condition: `(e.message:findi("hail"))`
      - Player: "Map" (link: external event mention)
        - Prompted by `event_trade`:
          - NPC say: You... you found it! My pestle! Hooray! I can get back to my work! I'm so grateful for this kind act, I've got to have something in my knapsack that you want! Here, how about some lint... wait, how did that get in there. You don't want lint! Hah! How about some cogs? No, what would you do with cogs? I know... you'll be able to make special use of this [map] I have.
          - Event guard: `(qglobals["warrior_epic"] == "17" and item_lib.check_turn_in(e.trade, {item1 = 60323}))`
        - NPC say: I've had this map for a long time. I can't seem to remember who gave it to me. I may have even made it myself. I do remember that something special can be found by following where the map leads. It's a magical map and will only show you the way in the dead of night, and only in the eastern wastes of this dreadful ice-covered place. You have to hold onto it tightly for it to work, keep that in mind! Good luck, you may need it!
        - Condition: `(e.other:Class() == "Warrior")`
        - Condition: `(e.message:findi("map") and qglobals["warrior_epic"] == "18")`
        - Gives Fazzle's Map of East Wastes (60324).

19. draniksscar/"Korbuk Brimblade", hand "Globe of Discordant Energy" (47100). Sets `warrior_epic` to `19`.
    - Requires `warrior_epic` >=18.
    - Hand in x1: "Globe of Discordant Energy" (47100).
    - Say "Check Lorb" to anguish/"Zone Status".
    - Spawns "Orb of Discordant Energy" (317087).
    - Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy".
    - Alternative: Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy" (NPC 317087) in `anguish`; trigger: anguish/"Zone Status", say "Check Uorb".
    - Alternative: Loot "Globe of Discordant Energy" (47100) from "Ornate Chest" (NPC 317112) in `anguish`; trigger: anguish/"Zone Status", say "Check Amv Chest".
    - Alternative: Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy" (NPC 317087) in `anguish`; trigger: anguish/"Zone Status", on event_signal.
    - Alternative: Loot "Globe of Discordant Energy" (47100) from "Overlords Chest" (NPC 317124) in `anguish`; trigger: anguish/"Zone Status", on event_signal.

20. draniksscar/"Korbuk Brimblade", hand "Champion's Sword of Eternal Power" (60321) + "Kreljnok's Focused Rage" (60327). Sets `warrior_epic` to `20`.
    - Requires `warrior_epic` >=19.
    - Hand in x1: "Champion's Sword of Eternal Power" (60321).
    - Hand in x1: "Kreljnok's Focused Rage" (60327).
    - Loot "Champion's Sword of Eternal Power" (60321) from "Krekk Brimblade" in `dranik`.
    - Prerequisite: "Kreljnok's Focused Rage" (60327). See section 0.
    - Gives "Raging Sword of Eternal Power" (60329).

21. global/"Global Player", combine recipe 19902. Sets `warrior_epic` to `21`.
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

#### Steps on `warrior_epic` that do not change it

- `abysmal` rewina jalmoy, hand 60295+60296+60297+60298 needs `warrior_epic` set.
  - Turn in Decomposing Page I (60295).
  - Turn in Decomposing Page II (60296).
  - Turn in Decomposing Page III (60297).
  - Turn in Decomposing Cover (60298).
  - Gives Recounted History of War (60299).
- `bloodfields` player, on loot needs `warrior_epic` set.
  - Sets `warr_epic_bloodfield` to `1`.
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
- `butcher` gridbar galund, hand 60311 needs `warrior_epic` set.
  - Turn in Glistening Hilt (60311).
  - Gives Carved Keg Stamp (60318).
- `butcher` gridbar galund, hand 60319 needs `warrior_epic` set.
  - Turn in Tube of Setting Solution (60319).
  - Gives Hilt of Eternal Power (60320).
- `causeway` player, on loot needs `warrior_epic` ==20.
  - Sets `warr_chest_causeway` to `1`.
  - Spawns a chest (epic 2.0) (893).
- `causeway` warr trap, on enter needs `warrior_epic` ==20.
  - Spawns Korbuk (303128).
- `dranik` player, on loot needs `warrior_epic` ==15.
  - Sets `warrior_epic_dranik` to `1`.
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

### Other flags touched along the way

- `warr_epic_bloodfield` set to 1 at bloodfields/player.
- `warr_epic_wos` set to 1 at wallofslaughter/player.
- `warrior_epic_dranik` set to 1 at dranik/player.
- `warrior_epic_gulak` set to 1 at veksar/player.
- `warrior_epic_korezna` set to 1, 2 at nedaria/korezna orecleaver.
- `warrior_epic_veksar` set to 1 at firiona/corfia nultethen.
- `warrior_epic_vxed` set to 1 at draniksscar/korbuk brimblade.
