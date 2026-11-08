# Cleric

Steps taken from the quest graph only. **Broken** means the graph has no edge for that value or that item.

Flags with writes: `cleric_epic`, `cleric15pre`, `cleric20`.

## 0. Prerequisites

Each list is the order you obtain that item. Later steps point here instead of repeating the chain.

### "Harmony of the Soul" (9955)

1. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
2. qeynos/"Wolten Grafe", say "Crush The Undead". Gives "Box For Bones" (17941).
3. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `steamfont`.
4. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `tox`.
5. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `toxxulia`.
6. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
7. toxxulia/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
8. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). The combine does not fail.
9. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
10. qeynos2/"Phin Esrinap", say "Supplies". Gives "Message to Konem" (18921).
11. qeytoqrg/"Konem Matse", hand "Message to Konem" (18921). Gives "Grathin's Invoice" (18922).
12. qeynos2/"Phin Esrinap", hand "Grathin's Invoice" (18922). Gives "Water Flask" (13006).
13. Say "Tm Devrak Death" to rujd/"Rujd".
14. Spawns "spawn chest with Heavy Orcish Prison Key" (245241).
15. Loot "Pod of Water" (13044) from "spawn chest with Heavy Orcish Prison Key".
16. Say "Tm Dokorel Death" to rujd/"Rujd".
17. Say "Tm Velrek Death" to rujd/"Rujd".
18. Say "Researcher Death" to rujg/"Rujg".
19. Spawns "A Barrel" (260015).
20. Loot "Pod of Water" (13044) from "A Barrel".
21. 3 other loot steps also yield Pod of Water (13044).
22. Forage "Pod of Water" (13044) in `ruja`.
23. Forage "Pod of Water" (13044) in `uqua`.
24. Forage "Pod of Water" (13044) in `yxtta`.
25. Combine in Brew Barrel (19): "Bottle of Aged Bloodwine" (51163), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aged Bloodwine" (51164). Requires Brewing, trivial 255.
26. Combine in Brew Barrel (19): "Bottle of Aldo's Bitter Ale" (75805), "Cask" (16580). Produces "Bottle" (16598) x8, "Cork" (16851) x8, "Cask of Aldo's Bitter Ale" (75811). Requires Brewing, trivial 15.
27. 17 other recipes also produce Bottle (16598).
28. Combine in Brew Barrel (19): "Pod of Water" (13044), "Bottle" (16598). Produces "Water Flask" (13006). Requires Brewing, trivial 21.
29. Kill wakening/"Dark Disciple Master". Spawns "A Gilded Chest" (119179).
30. Loot "Aegis of Chaotic Worship" (9954) from "A Gilded Chest".
31. **Broken:** no event trigger found for `wallofslaughter/a quivering egg#timer:hatch`.
32. Spawns "A Murk Hatchling" (300084) after `wallofslaughter/a quivering egg#timer:hatch`.
33. Loot "Murkglider Plasma" (13639) from "A Murk Hatchling".
34. No quest step gives Bazu Plasma (13658). The dump lists it in causeway, wallofslaughter.
35. Loot "Pyrilen Plasma" (13667) from "A Dragorn Assassin" in `wallofslaughter`.
36. Combine in Brew Barrel (19): "Murkglider Plasma" (13639), "Bazu Plasma" (13658), "Pyrilen Plasma" (13667). Produces "Soul Temper" (14047). Requires Brewing, trivial 100.
37. Combine in Forge (17): "Water Flask" (13006), "Aegis of Chaotic Worship" (9954), "Soul Temper" (14047). Produces "Harmony of the Soul" (9955). Requires Blacksmithing. The combine does not fail.

### "Water Sprinkler of Nem Ankh" (5532)

1. Loot "Singed Scroll" (18170) from "Overking Bathezid" in `chardok`.
2. Hand "Ornate Sea Shell" (28056) to burningwood/"Naxot Deepwater". Spawns "Ixiblat Fer, kill him, loot scepter of I.F." (87151). Loot "Sceptre of Ixiblat Fer" (28017) from "Ixiblat Fer, kill him, loot scepter of I.F.".
3. Loot "Sceptre of Ixiblat Fer" (28017) from "Ixiblat Fer".
4. timorous/"Omat Vastsea", hand "Singed Scroll" (18170) + "Sceptre of Ixiblat Fer" (28017). Gives "Orb of Clear Water" (28048).
5. Hand "Coral Statue of Tarew" (28051) to soltemple/"A Seeker". Spawns "A Plasmatic Priest" (80042). Loot "Blood Soaked Plasmatic Priest Robe" (1299) from "A Plasmatic Priest".
6. Loot "Blood Soaked Plasmatic Priest Robe" (1299) from "A Plasmatic Priest".
7. timorous/"Omat Vastsea", hand "Blood Soaked Plasmatic Priest Robe" (1299). Gives "Orb of Frozen Water" (28049).
8. Kill skyfire/"Zordak Ragefire". Spawns "Zordakalicus Ragefire" (91090).
9. Loot "Impure Heart of Zordak Ragefire" (17122) from "Zordakalicus Ragefire".
10. Loot "Lord Gimblox's Signet Ring" (28018) from "Lord Gimblox" in `soldunga`.
11. timorous/"Natasha Whitewater", hand "Lord Gimblox's Signet Ring" (28018). Gives "Ornate Sea Shell" (28056).
12. burningwood/"Naxot Deepwater", hand "Ornate Sea Shell" (28056). Gives "Message to Natasha" (28052).
13. timorous/"Natasha Whitewater", hand "Message to Natasha" (28052). Gives "Shimmering Pearl" (28054).
14. soldungb/"Zordak Ragefire", hand "Shimmering Pearl" (28054). Gives "Swirling Pearl" (28059).
15. skyfire/"Warder Cecilia", say "Hail". Gives "Zordak's Box of Bindings" (17175).
16. soldungb/"Zordak Ragefire", hand "Shimmering Pearl" (28054). Gives "Zordak's Box of Bindings" (17175).
17. No quest step gives Pearlescent Fragment (24995). The dump lists it in skyfire, westwastes.
18. Combine in "Zordak's Box of Bindings" (17175): "Pearlescent Fragment" (24995). Produces "Assembled Pearlescent Shard" (24996). The combine does not fail.
19. skyfire/"Warder Cecilia", hand "Assembled Pearlescent Shard" (24996). Gives "Pearlescent Seal" (24997).
20. Combine in "Impure Heart of Zordak Ragefire" (17122): "Pearlescent Seal" (24997), "Swirling Pearl" (28059). Produces "Zordak Ragefire's Heart" (28019). The combine does not fail.
21. timorous/"Omat Vastsea", hand "Zordak Ragefire's Heart" (28019). Gives "Orb of Vapor" (28050).
22. timorous/"Jhassad Oceanson", hand "Orb of Clear Water" (28048) + "Orb of Frozen Water" (28049) + "Orb of Vapor" (28050). Gives "Orb of the Triumvirate" (28023).
23. timorous/"Avatar Of Water", hand "Orb of the Triumvirate" (28023). Gives "Water Sprinkler of Nem Ankh" (5532).

### "Ethereal Disciple's Journal" (56013)

1. Loot "Journal of the Prime Disciple" (56016) at chambersa/"Mpg Fear", say "Chest Spawn".
2. Loot "Journal of the Prime Disciple" (56016) at chambersb/"Mpg Weaponry", say "Chest Spawn".
3. Loot "Journal of the Prime Disciple" (56016) at chambersc/"Mpg Subversion", say "Chest Spawn".
4. Loot "Journal of the Prime Disciple" (56016) at chambersd/"Mpg Efficiency", say "Chest Spawn".
5. 9 other loot steps also yield Journal of the Prime Disciple (56016).
6. No quest step gives Torn Journal Page (56012). The dump lists it in provinggrounds.
7. Loot "Ripped Journal Page" (56011) from "Girplan Scavenger" in `provinggrounds`.
8. Combine in "Journal of the Prime Disciple" (56016): "Torn Journal Page" (56012), "Ripped Journal Page" (56011). Produces "Ethereal Disciple's Journal" (56013). The combine does not fail.

### "Assembled Map" (56015)

1. global/"Global Player", combine recipe 19460. Sets `cleric_epic` to `7`.
2. No quest step gives Encrypted Note (7135). The dump lists it in barindu.
3. abysmal/"Shav The Cryptologist", hand "Encrypted Note" (7135). Sets `cleric_epic` to `2`.
4. No quest step gives Ripped Quarter of a Map (9476). The dump lists it in ferubi.
5. No quest step gives Shredded Quarter of a Map (9447). The dump lists it in ferubi.
6. No quest step gives Tattered Quarter of a Map (9477). The dump lists it in ferubi.
7. No quest step gives Torn Quarter of a Map (8778). The dump lists it in ferubi.
8. abysmal/"Shav The Cryptologist", hand "Torn Quarter of a Map" (8778) + "Shredded Quarter of a Map" (9447) + "Ripped Quarter of a Map" (9476) + "Tattered Quarter of a Map" (9477). Requires `cleric_epic` set. Requires `cleric_epic` ==2. Gives "Assembled Map" (56015).

### "Dark Disciples Notice of Service" (9591)

1. Spawns "Taskmaster Mirot" (57151) in `lfaydark` on event_signal.
2. Loot "Magically Sealed Letter" (9585) from "Taskmaster Mirot".
3. nedaria/"Tavon Vastsea", hand "Magically Sealed Letter" (9585). Gives "Dark Disciples Notice of Service" (9591).

### "Water Flask" (13006)

1. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
2. qeynos/"Wolten Grafe", say "Crush The Undead". Gives "Box For Bones" (17941).
3. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `steamfont`.
4. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `tox`.
5. Loot "Useless Cloth Cap" (13894) from "A Kobold Scout" in `toxxulia`.
6. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
7. toxxulia/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
8. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). The combine does not fail.
9. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).

### "Soul Temper" (14047)

1. **Broken:** no event trigger found for `wallofslaughter/a quivering egg#timer:hatch`.
2. Spawns "A Murk Hatchling" (300084) after `wallofslaughter/a quivering egg#timer:hatch`.
3. Loot "Murkglider Plasma" (13639) from "A Murk Hatchling".
4. No quest step gives Bazu Plasma (13658). The dump lists it in causeway, wallofslaughter.
5. Loot "Pyrilen Plasma" (13667) from "A Dragorn Assassin" in `wallofslaughter`.
6. Combine in Brew Barrel (19): "Murkglider Plasma" (13639), "Bazu Plasma" (13658), "Pyrilen Plasma" (13667). Produces "Soul Temper" (14047). Requires Brewing, trivial 100.

## `cleric_epic`

Values written: 1, 2, 3, 4, 5, 7.

### 1. tavon vastsea — say hail

Zone: `nedaria`.

> I hear you were able to put that shield to some use. That is good to hear. I was able to find some news on the leader, someone matching his description has b...

Sets `cleric_epic` to `1`.

- Needs `cleric20` set.
- Needs Harmony of the Soul (9955).
- Needs `cleric20` ==1.
- Needs `cleric_epic` unset.
- One of: `cleric15pre` ==1; Water Sprinkler of Nem Ankh (5532).
In script order:

1. Sets `cleric20` to `2`.
2. Sets `cleric_epic` to `1`.


How the items are reached:

- Harmony of the Soul (9955)
  - Prerequisite: "Harmony of the Soul" (9955). See section 0.
- Water Sprinkler of Nem Ankh (5532)
  - Prerequisite: "Water Sprinkler of Nem Ankh" (5532). See section 0.

Subquest `cleric20`:

#### `cleric20`

Values written: 1, 2, 3.

##### 1. natvil — say hail

Zone: `dranik`.

> examines your craftsmanship.

Sets `cleric20` to `1`.

- Needs `cleric_epic` set.
- Needs `cleric_epic` >=5.
- Needs Harmony of the Soul (9955).
- Needs `cleric20` unset.
In script order:

1. Sets `cleric20` to `1`.


How the items are reached:

- Harmony of the Soul (9955)
  - Prerequisite: "Harmony of the Soul" (9955). See section 0.

This step also depends on `cleric_epic`, shown above.

##### 2. tavon vastsea — say hail

Zone: `nedaria`.

> I hear you were able to put that shield to some use. That is good to hear. I was able to find some news on the leader, someone matching his description has b...

Sets `cleric20` to `2`.

- Needs `cleric20` set.
- Needs Harmony of the Soul (9955).
- Needs `cleric20` ==1.
- Needs `cleric_epic` unset.
- One of: `cleric15pre` ==1; Water Sprinkler of Nem Ankh (5532).
In script order:

1. Sets `cleric20` to `2`.
2. Sets `cleric_epic` to `1`.


How the items are reached:

- Harmony of the Soul (9955)
  - Prerequisite: "Harmony of the Soul" (9955). See section 0.
- Water Sprinkler of Nem Ankh (5532)
  - Prerequisite: "Water Sprinkler of Nem Ankh" (5532). See section 0.

Subquest `cleric15pre`:

#### `cleric15pre`

Values written: 1.

###### 1. omat vastsea — hand 5768+6505+6506+56010

Zone: `timorous`.

Sets `cleric15pre` to `1`.

- Turn in x1: Head of High Priestess Shima (5768).
- Turn in x1: Head of High Priest Maltan (6505).
- Turn in x1: Head of High Priest Valon (6506).
- Turn in x1: Talisman of the Plasmatic Priests (56010).
In script order:

1. Sets `cleric15pre` to `1`.


How the items are reached:

- Head of High Priestess Shima (5768)
  - timorous/"Omat Vastsea", say "Destruction". Gives "Talisman of the Plasmatic Priests" (56010).
  - Hand "Talisman of the Plasmatic Priests" (56010) to lavastorm/"Laura Rako". Spawns "High Priestess Shima" (27128). Loot "Head of High Priestess Shima" (5768) from "High Priestess Shima".
  - Loot "Head of High Priestess Shima" (5768) from "High Priestess Shima".
- Head of High Priest Maltan (6505)
  - timorous/"Omat Vastsea", say "Destruction". Gives "Talisman of the Plasmatic Priests" (56010).
  - Hand "Talisman of the Plasmatic Priests" (56010) to greatdivide/"Gavon Morant". Spawns "High Priest Maltan" (118211). Loot "Head of High Priest Maltan" (6505) from "High Priest Maltan".
  - Loot "Head of High Priest Maltan" (6505) from "High Priest Maltan".
- Head of High Priest Valon (6506)
  - timorous/"Omat Vastsea", say "Destruction". Gives "Talisman of the Plasmatic Priests" (56010).
  - Hand "Talisman of the Plasmatic Priests" (56010) to scarlet/"Jimmic Adle". Spawns "High Priest Valon" (175308). Loot "Head of High Priest Valon" (6506) from "High Priest Valon".
  - Loot "Head of High Priest Valon" (6506) from "High Priest Valon".
- Talisman of the Plasmatic Priests (56010)
  - Given by timorous/"Omat Vastsea", say "Destruction".

###### Steps on `cleric15pre` that do not change it

- `nedaria` tavon vastsea, say hail needs `cleric15pre` ==1.
  - Sets `cleric20` to `2`.
  - Sets `cleric_epic` to `1`.

This step also depends on `cleric_epic`, shown above.

##### 3. omat vastsea — hand 56013

Zone: `timorous`.

Sets `cleric20` to `3`.

- Needs `cleric20` >=2.
- Turn in x1: Ethereal Disciple's Journal (56013).
In script order:

1. Sets `cleric20` to `3`.
2. Spawns Gefaari Drokaz (96368).
   - Loots Soulshard of Zordak (56014).
3. Gives Ethereal Disciple's Journal (56013).


How the items are reached:

- Ethereal Disciple's Journal (56013)
  - Prerequisite: "Ethereal Disciple's Journal" (56013). See section 0.

##### Steps on `cleric20` that do not change it

- `nedaria` tavon vastsea, say hail needs `cleric20` set.
  - Sets `cleric_epic` to `1`.
- `provinggrounds` player, on loot needs `cleric20` set.
  - Sets `cleric20_mpg_chest` to `1`.
  - Spawns a chest (epic 2.0) (893).
  - Sets `wiz20_mpg_chest` to `1`.
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

This step also depends on `cleric15pre`, shown above.

### 2. shav the cryptologist — hand 7135

Zone: `abysmal`.

Sets `cleric_epic` to `2`.

- Needs `cleric_epic` set.
- Needs `cleric_epic` ==1.
- Turn in x1: Encrypted Note (7135).
In script order:

1. Sets `cleric_epic` to `2`.


How the items are reached:

- Encrypted Note (7135)
  - No quest step gives Encrypted Note (7135). The dump lists it in barindu.

### 3. shav the cryptologist — hand 8778+9447+9476+9477

Zone: `abysmal`.

Sets `cleric_epic` to `3`.

- Needs `cleric_epic` set.
- Needs `cleric_epic` ==2.
- Turn in x1: Ripped Quarter of a Map (9476).
- Turn in x1: Shredded Quarter of a Map (9447).
- Turn in x1: Tattered Quarter of a Map (9477).
- Turn in x1: Torn Quarter of a Map (8778).
In script order:

1. Sets `cleric_epic` to `3`.
2. Gives Assembled Map (56015).


How the items are reached:

- Ripped Quarter of a Map (9476)
  - No quest step gives Ripped Quarter of a Map (9476). The dump lists it in ferubi.
- Shredded Quarter of a Map (9447)
  - No quest step gives Shredded Quarter of a Map (9447). The dump lists it in ferubi.
- Tattered Quarter of a Map (9477)
  - No quest step gives Tattered Quarter of a Map (9477). The dump lists it in ferubi.
- Torn Quarter of a Map (8778)
  - No quest step gives Torn Quarter of a Map (8778). The dump lists it in ferubi.

### 4. cartographer tweister — hand 56015

Zone: `nedaria`.

Sets `cleric_epic` to `4`.

- Needs `cleric_epic` set.
- Needs `cleric_epic` >=3.
- Turn in x1: Assembled Map (56015).
In script order:

1. Sets `cleric_epic` to `4`.


How the items are reached:

- Assembled Map (56015)
  - Prerequisite: "Assembled Map" (56015). See section 0.

### 5. scout leader plavo — hand 9591

Zone: `wakening`.

Sets `cleric_epic` to `5`.

- Needs `cleric_epic` set.
- Needs `cleric_epic` >=4.
- Turn in x1: Dark Disciples Notice of Service (9591).
In script order:

1. Sets `cleric_epic` to `5`.


How the items are reached:

- Dark Disciples Notice of Service (9591)
  - Prerequisite: "Dark Disciples Notice of Service" (9591). See section 0.

### 7. global player — combine recipe 19460

Zone: `global`.

Sets `cleric_epic` to `7`.

In script order:

1. Sets `cleric_epic` to `7`.


Combine:

- `recipe:19460` is combined in Forge (17). A container in the world. Placed in abysmal, akanon, bazaar, bloodmoon, brellsrest, brellstemple and 51 more.
  - Put in x1: Water Flask (13006).
    - Prerequisite: "Water Flask" (13006). See section 0.
  - Put in x1: Aegis of Chaotic Worship (9954).
    - Kill wakening/"Dark Disciple Master". Spawns "A Gilded Chest" (119179).
    - Loot "Aegis of Chaotic Worship" (9954) from "A Gilded Chest".
    - Loot "Aegis of Chaotic Worship" (9954) from "A Gilded Chest".
  - Put in x1: Soul Temper (14047).
    - Prerequisite: "Soul Temper" (14047). See section 0.
  - Produces Harmony of the Soul (9955).
  - Requires Blacksmithing. The combine does not fail.

### Steps on `cleric_epic` that do not change it

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

## `cleric15pre`

See `cleric15pre` earlier in this file.

## `cleric20`

See `cleric20` earlier in this file.

## Other flags touched along the way

- `cleric20_darkdisciples` set to 1 at bloodfields/cryssa.
- `cleric20_mpg_chest` set to 1 at provinggrounds/player.
- `cleric20_mpg_drop` set to 1 at skyfire/warder cecilia.
- `cleric20_robedropped` set to 1 at wallofslaughter/default.
- `cleric20_td_chest` set to 1 at timorous/player.
- `cleric_epic_lfay` set to 1 at lfaydark/player.
- `cleric_epic_wakeningchest` set to 1 at wakening/player.
