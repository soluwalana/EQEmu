# Cleric

Acquisition paths traced backwards from the 1.0, 1.5 and 2.0 epic rewards. Flags are dependencies, not the definition of an epic. **Broken** indicates missing graph provenance.

## Epic 1.0

### "Water Sprinkler of Nem Ankh" (5532)

1. lakerathe/"Shmendrik Lavawalker", say "Hail". Hail, good $name!! Be wary near the waters of Lake Rathe! The Riptide goblin king, Lord Bergurgle, has been commanding his minions to murder and rob all who come near it! I am here seeking his death but I am afraid I am no match for all of his subjects. I shall reward you greatly for the death of Lord Bergurgle. I simply ask that you bring me his crown as proof.
2. Loot "Singed Scroll" (18170) from "Overking Bathezid" in `chardok`.
3. Loot "Lord Gimblox's Signet Ring" (28018) from "Lord Gimblox" in `soldunga`.
4. timorous/"Natasha Whitewater", hand "Lord Gimblox's Signet Ring" (28018). Gives "Ornate Sea Shell" (28056).
5. Hand "Ornate Sea Shell" (28056) to burningwood/"Naxot Deepwater". Spawns "Ixiblat Fer, kill him, loot scepter of I.F." (87151). Loot "Sceptre of Ixiblat Fer" (28017) from "Ixiblat Fer, kill him, loot scepter of I.F.".
6. timorous/"Omat Vastsea", hand "Singed Scroll" (18170) + "Sceptre of Ixiblat Fer" (28017). Gives "Orb of Clear Water" (28048).
7. Loot "Lord Bergurgle's Crown" (28044) from "Lord Bergurgle".
8. Loot "Lord Bergurgle's Crown" (28044) from "Lord Bergurgle" in `lakerathe`.
9. lakerathe/"Shmendrik Lavawalker", hand "Lord Bergurgle's Crown" (28044). Triggers `lakerathe/natasha whitewater#event_spawn`.
10. Kill lakerathe/"Shmendrik Lavawalker".
11. Loot "Damaged Goblin Crown" (28046) from "A Spirit Of Flame".
12. lakerathe/"Natasha Whitewater", hand "Damaged Goblin Crown" (28046). Gives "Ornate Sea Shell" (28047).
13. timorous/"Omat Vastsea", hand "Ornate Sea Shell" (28047). Gives "Coral Statue of Tarew" (28051).
14. Hand "Coral Statue of Tarew" (28051) to soltemple/"A Seeker". Spawns "A Plasmatic Priest" (80042). Loot "Blood Soaked Plasmatic Priest Robe" (1299) from "A Plasmatic Priest".
15. timorous/"Omat Vastsea", hand "Blood Soaked Plasmatic Priest Robe" (1299). Gives "Orb of Frozen Water" (28049).
16. Kill skyfire/"Zordak Ragefire". Spawns "Zordakalicus Ragefire" (91090).
17. Loot "Impure Heart of Zordak Ragefire" (17122) from "Zordakalicus Ragefire".
18. burningwood/"Naxot Deepwater", hand "Ornate Sea Shell" (28056). Gives "Message to Natasha" (28052).
19. timorous/"Natasha Whitewater", hand "Message to Natasha" (28052). Gives "Shimmering Pearl" (28054).
20. soldungb/"Zordak Ragefire", hand "Shimmering Pearl" (28054). Gives "Swirling Pearl" (28059).
21. skyfire/"Warder Cecilia", say "Hail". Gives "Zordak's Box of Bindings" (17175).
22. Loot "Pearlescent Fragment" (24995) from "A Skyfire Drake" (NPC 91038) in `skyfire`. Drop cache: 1.12% chance per kill.
23. Combine in "Zordak's Box of Bindings" (17175): "Pearlescent Fragment" (24995). Produces "Assembled Pearlescent Shard" (24996). The combine does not fail.
24. skyfire/"Warder Cecilia", hand "Assembled Pearlescent Shard" (24996). Gives "Pearlescent Seal" (24997).
25. Combine in "Impure Heart of Zordak Ragefire" (17122): "Pearlescent Seal" (24997), "Swirling Pearl" (28059). Produces "Zordak Ragefire's Heart" (28019). The combine does not fail.
26. timorous/"Omat Vastsea", hand "Zordak Ragefire's Heart" (28019). Gives "Orb of Vapor" (28050).
27. timorous/"Jhassad Oceanson", hand "Orb of Clear Water" (28048) + "Orb of Frozen Water" (28049) + "Orb of Vapor" (28050). Gives "Orb of the Triumvirate" (28023).
28. timorous/"Avatar Of Water", hand "Orb of the Triumvirate" (28023). Gives "Water Sprinkler of Nem Ankh" (5532).

## Epic 1.5

### "Harmony of the Soul" (9955)

1. **Unresolved introduction:** no connected introductory hail in the graph.
2. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
3. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `steamfont`.
4. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `tox`.
5. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `toxxulia`.
6. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
7. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). The combine does not fail.
8. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
9. Kill wakening/"Dark Disciple Master". Spawns "A Gilded Chest" (119179).
10. Loot "Aegis of Chaotic Worship" (9954) from "A Gilded Chest".
11. wallofslaughter/"A Quivering Egg", on event spawn.
12. Starts timer `hatch`.
13. Spawns "A Murk Hatchling" (300084) after `wallofslaughter/a quivering egg#timer:hatch`.
14. Loot "Murkglider Plasma" (13639) from "A Murk Hatchling".
15. Loot "Bazu Plasma" (13658) from "Bazu Bonesmasher" (NPC 300000) in `wallofslaughter`. Drop cache: 43.09% chance per kill.
16. Loot "Pyrilen Plasma" (13667) from "A Dragorn Assassin" in `wallofslaughter`.
17. Combine in Brew Barrel (19): "Murkglider Plasma" (13639), "Bazu Plasma" (13658), "Pyrilen Plasma" (13667). Produces "Soul Temper" (14047). Requires Brewing, trivial 100.
18. Combine in Forge (17): "Water Flask" (13006), "Aegis of Chaotic Worship" (9954), "Soul Temper" (14047). Produces "Harmony of the Soul" (9955). Requires Blacksmithing. The combine does not fail.

## Epic 2.0

### "Aegis of Superior Divinity" (20076)

1. dranik/"Natvil", say "Hail". Sets `cleric20` to `1`.
    - Dialogue with dranik/"Natvil":
      - Player: "Hail"
        - NPC emote: examines your craftsmanship. 'Impressive, but I'm afraid that the temper was not sufficient to unlock the full potential of the shield. For now you may use it in its current state. I suspect to fully realize the latent potential of the shield you will require a soulstone from the person who it was bound to originally as well as a Globe of Discordant Energy. Return to me when you have that, I will assist you in completing its enhancement.
          - Reply guard: `e.other:HasItem(9955)`
        - NPC say: Greetings, well met, salutations, and good day! I hear you are trying to change the resonance on a shield from Discord. Well I believe that is something with which I can assist you. You will need to have a temper made from some of the native creatures of Discord, you'll need the plasma from one of the giants of Discord, one of those flying squids, and the plasma from one of those fiery women. Brewing the temper should prove no trouble for you. Once you have the temper combine it with the shield in the forge with a flask of water, and it should become attuned to you. Once you are finished return to me, so I may evaluate your work.
          - Reply guard: ``
        - Condition: `qglobals["cleric_epic"] ~= nil and qglobals["cleric_epic"] >= "5" and e.message:findi("hail")`
        - Sets `cleric20` to `1`.
2. global/"Global Player", combine recipe 19460. Sets `cleric_epic` to `7`.
3. nedaria/"Tavon Vastsea", say "Hail". Sets `cleric20` to `2`.
4. Loot "Journal of the Prime Disciple" (56016) at chambersa/"Mpg Fear", say "Chest Spawn".
5. Alternative: Loot "Journal of the Prime Disciple" (56016) from chambersb/"Mpg Weaponry" in `chambersb`; trigger: chambersb/"Mpg Weaponry", say "Chest Spawn".
6. Alternative: Loot "Journal of the Prime Disciple" (56016) from chambersc/"Mpg Subversion" in `chambersc`; trigger: chambersc/"Mpg Subversion", say "Chest Spawn".
7. Alternative: Loot "Journal of the Prime Disciple" (56016) from chambersd/"Mpg Efficiency" in `chambersd`; trigger: chambersd/"Mpg Efficiency", say "Chest Spawn".
8. Alternative: Loot "Journal of the Prime Disciple" (56016) from chamberse/"Mpg Ingenuity" in `chamberse`; trigger: chamberse/"Mpg Ingenuity", say "Chest Spawn".
9. Alternative: Loot "Journal of the Prime Disciple" (56016) from chambersf/"Mpg Destruction" in `chambersf`; trigger: chambersf/"Mpg Destruction", say "Chest Spawn".
10. Alternative: Loot "Journal of the Prime Disciple" (56016) from "Shell of the Master" (NPC 304013) in `chambersa`; trigger: chambersa/"Mpg Fear", on timer minutes.
11. Alternative: Loot "Journal of the Prime Disciple" (56016) from "Shell of the Master" (NPC 304020) in `chambersa`; trigger: chambersa/"Mpg Hate", on event death_complete:304017.
12. Alternative: Loot "Journal of the Prime Disciple" (56016) from "Shell of the Master" (NPC 305005) in `chambersb`; trigger: chambersb/"Mpg Weaponry", on event signal:305004.
13. Alternative: Loot "Journal of the Prime Disciple" (56016) from "Shell of the Master" (NPC 306009) in `chambersc`; trigger: chambersc/"Mpg Subversion", on event death_complete:306001.
14. Alternative: Loot "Journal of the Prime Disciple" (56016) from "Shell of the Master" (NPC 307005) in `chambersd`; trigger: chambersd/"Mpg Efficiency", on event signal:307000.
15. Alternative: Loot "Journal of the Prime Disciple" (56016) from "Shell of the Master" (NPC 308004) in `chamberse`; trigger: chamberse/"Mpg Ingenuity", on event death_complete:308007.
16. Alternative: Loot "Journal of the Prime Disciple" (56016) from "Shell of the Master" (NPC 309068) in `chambersf`; trigger: chambersf/"Mpg Destruction", on event death_complete:309061.
17. Loot "Torn Journal Page" (56012) from "A Lightning Warrior Staticfist" (NPC 316007) in `provinggrounds`. Drop cache: 5.99% chance per kill.
18. Loot "Ripped Journal Page" (56011) from "Girplan Scavenger" in `provinggrounds`.
19. Combine in "Journal of the Prime Disciple" (56016): "Torn Journal Page" (56012), "Ripped Journal Page" (56011). Produces "Ethereal Disciple's Journal" (56013). The combine does not fail.
20. Hand "Ethereal Disciple's Journal" (56013) to timorous/"Omat Vastsea". Spawns "Gefaari Drokaz" (96368). Loot "Soulshard of Zordak" (56014) from "Gefaari Drokaz".
21. Say "Check Lorb" to anguish/"Zone Status".
22. Spawns "Orb of Discordant Energy" (317087).
23. Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy".
24. Alternative: Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy" (NPC 317087) in `anguish`; trigger: anguish/"Zone Status", say "Check Uorb".
25. Alternative: Loot "Globe of Discordant Energy" (47100) from "Ornate Chest" (NPC 317112) in `anguish`; trigger: anguish/"Zone Status", say "Check Amv Chest".
26. Alternative: Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy" (NPC 317087) in `anguish`; trigger: anguish/"Zone Status", say "Signal:999999".
27. Alternative: Loot "Globe of Discordant Energy" (47100) from "Overlords Chest" (NPC 317124) in `anguish`; trigger: anguish/"Zone Status", say "Signal:999999".
28. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
29. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `steamfont`.
30. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `tox`.
31. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `toxxulia`.
32. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
33. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). The combine does not fail.
34. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
35. Kill wakening/"Dark Disciple Master". Spawns "A Gilded Chest" (119179).
36. Loot "Aegis of Chaotic Worship" (9954) from "A Gilded Chest".
37. wallofslaughter/"A Quivering Egg", on event spawn.
38. Starts timer `hatch`.
39. Spawns "A Murk Hatchling" (300084) after `wallofslaughter/a quivering egg#timer:hatch`.
40. Loot "Murkglider Plasma" (13639) from "A Murk Hatchling".
41. Loot "Bazu Plasma" (13658) from "Bazu Bonesmasher" (NPC 300000) in `wallofslaughter`. Drop cache: 43.09% chance per kill.
42. Loot "Pyrilen Plasma" (13667) from "A Dragorn Assassin" in `wallofslaughter`.
43. Combine in Brew Barrel (19): "Murkglider Plasma" (13639), "Bazu Plasma" (13658), "Pyrilen Plasma" (13667). Produces "Soul Temper" (14047). Requires Brewing, trivial 100.
44. Combine in Forge (17): "Water Flask" (13006), "Aegis of Chaotic Worship" (9954), "Soul Temper" (14047). Produces "Harmony of the Soul" (9955). Requires Blacksmithing. The combine does not fail.
45. dranik/"Natvil", hand "Harmony of the Soul" (9955) + "Globe of Discordant Energy" (47100) + "Soulshard of Zordak" (56014). Gives "Aegis of Superior Divinity" (20076).

## Quest-state progression

## 0. Prerequisites

Shared acquisition steps appear in the first prerequisite chain that needs them. Later sections reference that chain rather than repeating it.

### "Water Flask" (13006)

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

### "Ethereal Disciple's Journal" (56013)

1. Loot "Journal of the Prime Disciple" (56016) at chambersa/"Mpg Fear", say "Chest Spawn".
2. Alternative: Loot "Journal of the Prime Disciple" (56016) from chambersb/"Mpg Weaponry" in `chambersb`; trigger: chambersb/"Mpg Weaponry", say "Chest Spawn".
3. Alternative: Loot "Journal of the Prime Disciple" (56016) from chambersc/"Mpg Subversion" in `chambersc`; trigger: chambersc/"Mpg Subversion", say "Chest Spawn".
4. Alternative: Loot "Journal of the Prime Disciple" (56016) from chambersd/"Mpg Efficiency" in `chambersd`; trigger: chambersd/"Mpg Efficiency", say "Chest Spawn".
5. Alternative: Loot "Journal of the Prime Disciple" (56016) from chamberse/"Mpg Ingenuity" in `chamberse`; trigger: chamberse/"Mpg Ingenuity", say "Chest Spawn".
6. Alternative: Loot "Journal of the Prime Disciple" (56016) from chambersf/"Mpg Destruction" in `chambersf`; trigger: chambersf/"Mpg Destruction", say "Chest Spawn".
7. Alternative: Loot "Journal of the Prime Disciple" (56016) from "Shell of the Master" (NPC 304013) in `chambersa`; trigger: chambersa/"Mpg Fear", on timer minutes.
8. Alternative: Loot "Journal of the Prime Disciple" (56016) from "Shell of the Master" (NPC 304020) in `chambersa`; trigger: chambersa/"Mpg Hate", on event death_complete:304017.
9. Alternative: Loot "Journal of the Prime Disciple" (56016) from "Shell of the Master" (NPC 305005) in `chambersb`; trigger: chambersb/"Mpg Weaponry", on event signal:305004.
10. Alternative: Loot "Journal of the Prime Disciple" (56016) from "Shell of the Master" (NPC 306009) in `chambersc`; trigger: chambersc/"Mpg Subversion", on event death_complete:306001.
11. Alternative: Loot "Journal of the Prime Disciple" (56016) from "Shell of the Master" (NPC 307005) in `chambersd`; trigger: chambersd/"Mpg Efficiency", on event signal:307000.
12. Alternative: Loot "Journal of the Prime Disciple" (56016) from "Shell of the Master" (NPC 308004) in `chamberse`; trigger: chamberse/"Mpg Ingenuity", on event death_complete:308007.
13. Alternative: Loot "Journal of the Prime Disciple" (56016) from "Shell of the Master" (NPC 309068) in `chambersf`; trigger: chambersf/"Mpg Destruction", on event death_complete:309061.
14. Loot "Torn Journal Page" (56012) from "A Lightning Warrior Staticfist" (NPC 316007) in `provinggrounds`. Drop cache: 5.99% chance per kill.
15. Loot "Ripped Journal Page" (56011) from "Girplan Scavenger" in `provinggrounds`.
16. Combine in "Journal of the Prime Disciple" (56016): "Torn Journal Page" (56012), "Ripped Journal Page" (56011). Produces "Ethereal Disciple's Journal" (56013). The combine does not fail.

### "Assembled Map" (56015)

1. timorous/"Omat Vastsea", say "Destruction". Gives "Talisman of the Plasmatic Priests" (56010).
2. timorous/"Omat Vastsea", say "Destruction". Gives "Talisman of the Plasmatic Priests" (56010).
3. Hand "Talisman of the Plasmatic Priests" (56010) to lavastorm/"Laura Rako". Spawns "High Priestess Shima" (27128). Loot "Head of High Priestess Shima" (5768) from "High Priestess Shima".
4. timorous/"Omat Vastsea", say "Destruction". Gives "Talisman of the Plasmatic Priests" (56010).
5. Hand "Talisman of the Plasmatic Priests" (56010) to greatdivide/"Gavon Morant". Spawns "High Priest Maltan" (118211). Loot "Head of High Priest Maltan" (6505) from "High Priest Maltan".
6. timorous/"Omat Vastsea", say "Destruction". Gives "Talisman of the Plasmatic Priests" (56010).
7. Hand "Talisman of the Plasmatic Priests" (56010) to scarlet/"Jimmic Adle". Spawns "High Priest Valon" (175308). Loot "Head of High Priest Valon" (6506) from "High Priest Valon".
8. timorous/"Omat Vastsea", hand "Head of High Priestess Shima" (5768) + "Head of High Priest Maltan" (6505) + "Head of High Priest Valon" (6506) + "Talisman of the Plasmatic Priests" (56010). Sets `cleric15pre` to `1`.
9. nedaria/"Tavon Vastsea", say "Hail". Sets `cleric_epic` to `1`.
10. Loot "Encrypted Note" (7135) from "A Noc Bloodluster" (NPC 283111) in `barindu`. Drop cache: 1.58% chance per kill.
11. abysmal/"Shav The Cryptologist", hand "Encrypted Note" (7135). Sets `cleric_epic` to `2`.
12. Loot "Ripped Quarter of a Map" (9476) from "A Ra'Tuk Bonebreaker" (NPC 284032) in `ferubi`. Drop cache: 5.6% chance per kill.
13. Loot "Shredded Quarter of a Map" (9447) from "A Kyv Eyecollector" (NPC 284052) in `ferubi`. Drop cache: 5.09% chance per kill.
14. Loot "Tattered Quarter of a Map" (9477) from "A Mastruq Warfiend" (NPC 284003) in `ferubi`. Drop cache: 5.33% chance per kill.
15. Loot "Torn Quarter of a Map" (8778) from "An Aneuk Bone Binder" (NPC 284035) in `ferubi`. Drop cache: 5.18% chance per kill.
16. abysmal/"Shav The Cryptologist", hand "Torn Quarter of a Map" (8778) + "Shredded Quarter of a Map" (9447) + "Ripped Quarter of a Map" (9476) + "Tattered Quarter of a Map" (9477). Requires `cleric_epic` set. Requires `cleric_epic` ==2. Gives "Assembled Map" (56015).

### "Dark Disciples Notice of Service" (9591)

1. **Broken:** cyclic event trigger at `lfaydark/taskmaster mirot#signal:1`.
2. Kill lfaydark/"A Wayfarer".
3. Loot "Magically Sealed Letter" (9585) from "Taskmaster Mirot".
4. nedaria/"Tavon Vastsea", hand "Magically Sealed Letter" (9585). Gives "Dark Disciples Notice of Service" (9591).

### "Soul Temper" (14047)

1. wallofslaughter/"A Quivering Egg", on event spawn.
2. Starts timer `hatch`.
3. Spawns "A Murk Hatchling" (300084) after `wallofslaughter/a quivering egg#timer:hatch`.
4. Loot "Murkglider Plasma" (13639) from "A Murk Hatchling".
5. Loot "Bazu Plasma" (13658) from "Bazu Bonesmasher" (NPC 300000) in `wallofslaughter`. Drop cache: 43.09% chance per kill.
6. Loot "Pyrilen Plasma" (13667) from "A Dragorn Assassin" in `wallofslaughter`.
7. Combine in Brew Barrel (19): "Murkglider Plasma" (13639), "Bazu Plasma" (13658), "Pyrilen Plasma" (13667). Produces "Soul Temper" (14047). Requires Brewing, trivial 100.

### `cleric_epic`

Values written: 1, 2, 3, 4, 5, 7.

1. nedaria/"Tavon Vastsea", say "Hail". Sets `cleric_epic` to `1`.
    - Requires `cleric_epic` unset.
    - Requires `cleric15pre` ==1.
    - Dialogue with nedaria/"Tavon Vastsea":
      - Player: "Hail"
        - NPC say: I hear you were able to put that shield to some use. That is good to hear. I was able to find some news on the leader, someone matching his description has been seen on the other side of the Wayfarer's portal in the Realm of Discord. Please visit my friend Cryssa, at the camp in Discord. She has been working on tracking the Disciple's movement in Discord.
          - Reply guard: `(e.other:HasItem(9955) and qglobals["cleric20"] ~= nil)`
        - NPC say: Greetings , I see you helped my brother in eradicating the Plasmatic Priests, stopping Zordak Ragefire, and saved Norrath from an eternity of flames. We need to [ call you to duty ] again
          - Reply guard: `(e.other:HasItem(5532) or qglobals["cleric15pre"] == "1")`
        - NPC say: Greetings , I am afraid that I need someone that I can [trust] with this task, these are dark times, and it is hard to tell friend from foe.
          - Reply guard: ``
        - Condition: `(e.other:Class() == "Cleric")`
        - Condition: `(e.message:findi("hail"))`
        - Sets `cleric20` to `2`.
        - Sets `cleric_epic` to `1`.
      - Player: "Call You To Duty" (link: explicit mention)
        - NPC say: This time the crisis threatens not only Norrath, but all of existence as we know it. Invaders from the Realm of Discord have transversed time and space to conquer this realm. The invaders, these Muramites, are not where the true threat lies. All of Norrath has banded together to stop these invaders, we have managed to halt their incursion for the time being. There are, however, whispers of a [ dark faction ] within our own, Norrathians who see our fight as futile, and are looking to swear fealty to the forces of the Legion.
        - Condition: `(e.other:Class() == "Cleric")`
        - Condition: `(e.message:findi("call you to duty"))`
      - Player: "Dark Faction" (link: explicit mention)
        - NPC say: We don't know much more about them. As I said, they are just whispers, but whispers in unison are loud enough for deaf ears. We cannot afford to present anything short of a unified front, should the Legion push toward Norrath with its full force. We need your assistance to find and exterminate these traitors. I can give you what little [ information ] I have, hopefully you will be able to track these betrayers to their leader.
        - Condition: `(e.other:Class() == "Cleric")`
        - Condition: `(e.message:findi("dark faction"))`
      - Player: "Information" (link: explicit mention)
        - NPC say: Travel to Taelosia. There you will find a young native, named Jomaj who had some suspicious dealings with someone claiming they were with the wayfarer's brotherhood. This is the closest I have to direction, gather information from this Taelosian, and bring it to my friend Shav on the Thorn. Find proof as to whether or not these traitors actually exist and return it to me.
        - Condition: `(e.other:Class() == "Cleric")`
        - Condition: `(e.message:findi("information"))`
      - Player: "Trust" (link: explicit mention)
        - Prompted by player input: "Hail"
        - NPC say: Hmmm, well I think I have a task I can entrust you with. Speak to my brother, tell him that I sent you to him. Earn his trust, and you shall have mine
        - Condition: `(e.other:Class() == "Cleric")`
        - Condition: `(e.message:findi("trust"))`

    - Subquest `cleric15pre`:
#### `cleric15pre`

Values written: 1.

1. timorous/"Omat Vastsea", hand "Head of High Priestess Shima" (5768) + "Head of High Priest Maltan" (6505) + "Head of High Priest Valon" (6506) + "Talisman of the Plasmatic Priests" (56010). Sets `cleric15pre` to `1`.
    - Hand in x1: "Head of High Priestess Shima" (5768).
    - Hand in x1: "Head of High Priest Maltan" (6505).
    - Hand in x1: "Head of High Priest Valon" (6506).
    - Hand in x1: "Talisman of the Plasmatic Priests" (56010).
    - timorous/"Omat Vastsea", say "Destruction". Gives "Talisman of the Plasmatic Priests" (56010).
    - Hand "Talisman of the Plasmatic Priests" (56010) to lavastorm/"Laura Rako". Spawns "High Priestess Shima" (27128). Loot "Head of High Priestess Shima" (5768) from "High Priestess Shima".
    - timorous/"Omat Vastsea", say "Destruction". Gives "Talisman of the Plasmatic Priests" (56010).
    - Hand "Talisman of the Plasmatic Priests" (56010) to greatdivide/"Gavon Morant". Spawns "High Priest Maltan" (118211). Loot "Head of High Priest Maltan" (6505) from "High Priest Maltan".
    - timorous/"Omat Vastsea", say "Destruction". Gives "Talisman of the Plasmatic Priests" (56010).
    - Hand "Talisman of the Plasmatic Priests" (56010) to scarlet/"Jimmic Adle". Spawns "High Priest Valon" (175308). Loot "Head of High Priest Valon" (6506) from "High Priest Valon".
    - Given by timorous/"Omat Vastsea", say "Destruction".
    - Dialogue with timorous/"Omat Vastsea":
      - Player: "Hail"
        - NPC say: Jhassad told me to notify him the minute you returned. Hurry down to the beach so you do not miss him again!
          - Reply guard: `(plugin::check_hasitem($client,28048) && plugin::check_hasitem($client,28049) && plugin::check_hasitem($client,28050))`
        - NPC emote: bows deeply. 'I have been expecting you, $name. The waters have foretold your arrival. I am High Priest Omat Vastsea of the Triumvirate missionaries. Please feel free to enjoy the quiet solitude of this inn.'
          - Reply guard: ``
        - Condition: `($text=~/hail/i)`
        - Spawns NPC 96074.
      - Player: "Triumvirate" (link: explicit mention)
        - NPC say: The Triumvirate of Water are: E'ci, the mistress of ice; Tarew Marr, the lord of water; and Povar, the formless master of vapor and mist. We Triumvirate missionaries are granted great divinatory powers and wisdom through our devotion to the Triumvirate and must defend the waters of Norrath from the ravages of the Tyrant of Fire, Fennin Ro.
        - Condition: `($text=~/Triumvirate/i)`
      - Player: "Fennin Ro" (link: explicit mention)
        - NPC say: The Tyrant of Fire, Fennin Ro, is the merciless lord of fire in all its forms. The rivalry between the tyrant and the Triumvirate is as old as the gods themselves and is an eternal battle. We witness the struggle every moment of our lives as the Oasis of Marr succumbs to the heat of the surrounding desert and is replenished by the swelling of the Lifire River. That fragile balance between the elements must be maintained but the Plasmatic Priesthood threatens that balance.
        - Condition: `($text=~/Fennin Ro/i)`
      - Player: "Plasmatic Priesthood" (link: explicit mention)
        - NPC say: The Plasmatic Priesthood are worshipers of the Tyrant of Fire, but they have been driven mad by their fanaticism and have forgotten the importance of the balance. In their madness they would set the whole world aflame, leaving nothing but lifeless ash.
        - Condition: `($text=~/plasmatic priesthood/i)`
      - Player: "Tavon sent me" (link: conversation sequence)
        - NPC say: I received word from my brother that you would be coming. I have just the task for you. I am sure you heard of the [Plasmatic Priests]
        - Condition: `($text=~/Tavon sent me/i)`
      - Player: "Plasmatic Priests" (link: explicit mention)
        - NPC say: The Plasmatic Priests were worshippers of Fennin Ro. Their numbers were all but destroyed by adventurers, and with the silence of the Pantheon they no longer draw power from the Tyrant of Fire. However they are still a danger, please find the last remnants of their order and bring me proof of their[destruction]
        - Condition: `($text=~/Plasmatic Priests/i)`
      - Player: "Destruction" (link: explicit mention)
        - NPC say: They are in hiding, the few alcoves that I managed to find were shrouded and hidden. Take this signet and find the keeper for each alcove. Show it to him and he will drop the veil. Strike fast and exterminate the camp before he is able to cloak the camp again. Return the talisman to me with proof of the deaths of the three remaining high priests. Once you have done this, I will send you to my brother with my blessings.
        - Condition: `($text=~/destruction/i)`
        - Gives Talisman of the Plasmatic Priests (56010).

###### Steps on `cleric15pre` that do not change it

- `nedaria` tavon vastsea, say hail needs `cleric15pre` ==1.
  - Sets `cleric_epic` to `1`.

2. abysmal/"Shav The Cryptologist", hand "Encrypted Note" (7135). Sets `cleric_epic` to `2`.
    - Requires `cleric_epic` set.
    - Requires `cleric_epic` ==1.
    - Hand in x1: "Encrypted Note" (7135).
    - Loot "Encrypted Note" (7135) from "A Noc Bloodluster" (NPC 283111) in `barindu`. Drop cache: 1.58% chance per kill.
    - Dialogue with abysmal/"Shav The Cryptologist":
      - Player: "Hail"
        - NPC say: Greetings. I'm a little busy, you have something you need translated?
        - Condition: `e.message:findi("hail")`

3. abysmal/"Shav The Cryptologist", hand "Torn Quarter of a Map" (8778) + "Shredded Quarter of a Map" (9447) + "Ripped Quarter of a Map" (9476) + "Tattered Quarter of a Map" (9477). Sets `cleric_epic` to `3`.
    - Requires `cleric_epic` set.
    - Requires `cleric_epic` ==2.
    - Hand in x1: "Ripped Quarter of a Map" (9476).
    - Hand in x1: "Shredded Quarter of a Map" (9447).
    - Hand in x1: "Tattered Quarter of a Map" (9477).
    - Hand in x1: "Torn Quarter of a Map" (8778).
    - Loot "Ripped Quarter of a Map" (9476) from "A Ra'Tuk Bonebreaker" (NPC 284032) in `ferubi`. Drop cache: 5.6% chance per kill.
    - Loot "Shredded Quarter of a Map" (9447) from "A Kyv Eyecollector" (NPC 284052) in `ferubi`. Drop cache: 5.09% chance per kill.
    - Loot "Tattered Quarter of a Map" (9477) from "A Mastruq Warfiend" (NPC 284003) in `ferubi`. Drop cache: 5.33% chance per kill.
    - Loot "Torn Quarter of a Map" (8778) from "An Aneuk Bone Binder" (NPC 284035) in `ferubi`. Drop cache: 5.18% chance per kill.
    - Gives "Assembled Map" (56015).

4. nedaria/"Cartographer Tweister", hand "Assembled Map" (56015). Sets `cleric_epic` to `4`.
    - Requires `cleric_epic` set.
    - Requires `cleric_epic` >=3.
    - Hand in x1: "Assembled Map" (56015).
    - Prerequisite: "Assembled Map" (56015). See section 0.
    - Dialogue with nedaria/"Cartographer Tweister":
      - Player: "Hail"
        - NPC say: Hello there, need something navigated, or mapped, or something of that sort? Hand it over already!
        - Condition: `(e.message:findi("hail"))`

5. wakening/"Scout Leader Plavo", hand "Dark Disciples Notice of Service" (9591). Sets `cleric_epic` to `5`.
    - Requires `cleric_epic` set.
    - Requires `cleric_epic` >=4.
    - Hand in x1: "Dark Disciples Notice of Service" (9591).
    - Prerequisite: "Dark Disciples Notice of Service" (9591). See section 0.
    - Dialogue with wakening/"Scout Leader Plavo":
      - Player: "Aid" (link: external event mention)
        - Prompted by `event_trade`:
          - NPC say: You are from the Faydwer camp are you? I'm not terribly familiar with the faces from there. Anyway, the scouts have been sent out, and are gathering the "parts" that we believe the Legion will need to prepare for the incursion into our realm. If we are to find their good graces, we must prove that we will stop at nothing to [aid] them.
          - Event guard: `qglobals["cleric_epic"] ~= nil and qglobals["cleric_epic"] >= "4" and item_lib.check_turn_in(e.trade, {item1 = 9591})`
        - NPC say: They will research and learn about the greatest mortal beings in this realm. Learning about the creatures that may prove to be friend or foe, so they prepare for either. Our scouts have gathered most of the information that they need, but there are a few creatures that we still need to harvest brains from. Currently scouts are attempting to find the brain of the Shissar, a dragon, and an Akhevan. I am sure any of the scouts would welcome your assistance. I will send runners ahead to notify them you may be arriving.
        - Condition: `qglobals["cleric_epic"] ~= nil and qglobals["cleric_epic"] >= "5" and e.message:findi("aid")`

7. global/"Global Player", combine recipe 19460. Sets `cleric_epic` to `7`.
    - `recipe:19460` is combined in Forge (17). A container in the world. Placed in abysmal, akanon, bazaar, bloodmoon, brellsrest, brellstemple and 51 more.
      - Put in x1: Water Flask (13006).
        - Prerequisite: "Water Flask" (13006). See section 0.
      - Put in x1: Aegis of Chaotic Worship (9954).
        - Kill wakening/"Dark Disciple Master". Spawns "A Gilded Chest" (119179).
        - Loot "Aegis of Chaotic Worship" (9954) from "A Gilded Chest".
      - Put in x1: Soul Temper (14047).
        - Prerequisite: "Soul Temper" (14047). See section 0.
      - Produces Harmony of the Soul (9955).
      - Requires Blacksmithing. The combine does not fail.

#### Steps on `cleric_epic` that do not change it

- `barindu` jomaj kaiijin, say note needs `cleric_epic` ==1.
  - Spawns Spawns "A Kyv Runner" to the immediate right of Jomaj Kaiijin. (283102).
  - Loots Soluble Loam (34884).
  - Loots Lucidem (35084).
  - Loots Versluierd Fungus (35087).
  - Loots Uncut Rubellite (37852).
  - Loots Raw Indigo Nihilite (37858).
  - Loots Raw Amber Nihilite (37859).
  - Loots Kyv Tongue (67584).
- `dranik` natvil, say hail needs `cleric_epic` set.
  - Sets `cleric20` to `1`.
- `lfaydark` player, on loot needs `cleric_epic` >=4.
  - Sets `cleric_epic_lfay` to `1`.
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
- `lfaydark` taskmaster mirot, say hail needs `cleric_epic` set.
  - Spawns a Wayfarer (57153).
- `wakening` player, on loot needs `cleric_epic` set.
  - Sets `cleric_epic_wakeningchest` to `1`.
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
- `wakening` scout leader plavo, hand 9597+9945+9948 needs `cleric_epic` set.
  - Spawns Dark Disciple Master (119176).
  - Turn in Shissar Cerebral Cortex (9945).
  - Turn in Dragon Cerebrum (9948).
  - Turn in Akhevan Brain Stem (9597).
- `westwastes` scout pirri, say hail needs `cleric_epic` set.
  - Spawns Scout Pirri (120112).
  - Loots Dragon Cerebrum (9948).
  - Loots Curzon (35085).
  - Loots Sunshard Powder (35088).
  - Loots Uncut Morganite (37849).

### `cleric15pre`

See `cleric15pre` earlier in this file.

### `cleric20`

Values written: 1, 2, 3.

1. dranik/"Natvil", say "Hail". Sets `cleric20` to `1`.
    - Requires `cleric20` unset.
    - Requires `cleric_epic` set.
    - Requires `cleric_epic` >=5.

    - Subquest `cleric_epic` documented earlier.
2. nedaria/"Tavon Vastsea", say "Hail". Sets `cleric20` to `2`.
    - Requires `cleric20` ==1.
    - Requires `cleric20` set.

3. timorous/"Omat Vastsea", hand "Ethereal Disciple's Journal" (56013). Sets `cleric20` to `3`.
    - Requires `cleric20` >=2.
    - Hand in x1: "Ethereal Disciple's Journal" (56013).
    - Prerequisite: "Ethereal Disciple's Journal" (56013). See section 0.
    - Spawns Gefaari Drokaz (96368).
    - Gives "Ethereal Disciple's Journal" (56013).

#### Steps on `cleric20` that do not change it

- `provinggrounds` player, on loot needs `cleric20` set.
  - Sets `cleric20_mpg_chest` to `1`.
  - Spawns a chest (epic 2.0) (893).
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
- `skyfire` warder cecilia, hand 12509 needs `cleric20` >=2.
  - Sets `cleric20_mpg_drop` to `1`.
  - Turn in Robe of Plasmatic Priesthood (12509).
- `timorous` omat vastsea, hand 12433 needs `cleric20` >=2.
  - Turn in Dark Red Robe (12433).
  - Gives Robe of Plasmatic Priesthood (12509).
- `timorous` player, on loot needs `cleric20` set.
  - Sets `cleric20_td_chest` to `1`.
  - Spawns a chest (epic 2.0) (893).
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

### Other flags touched along the way

- `cleric20_darkdisciples` set to 1 at bloodfields/cryssa.
- `cleric20_mpg_chest` set to 1 at provinggrounds/player.
- `cleric20_mpg_drop` set to 1 at skyfire/warder cecilia.
- `cleric20_robedropped` set to 1 at wallofslaughter/default.
- `cleric20_td_chest` set to 1 at timorous/player.
- `cleric_epic_lfay` set to 1 at lfaydark/player.
- `cleric_epic_wakeningchest` set to 1 at wakening/player.
