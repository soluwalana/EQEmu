# Shaman

Steps taken from the quest graph only. **Broken** means the graph has no edge for that value or that item.

Flags with writes: `shaman_pre`, `shaman_epic`.

## 0. Prerequisites

Each list is the order you obtain that item. Later steps point here instead of repeating the chain.

### "Black Fur Boots" (1678)

1. Loot "Black Dire Pelt" (1672) from "Black Dire" in `mistmoore`.
2. emeraldjungle/"Spirit Sentinel", hand "Black Dire Pelt" (1672). Gives "Black Fur Boots" (1678).

### "Spear of Fate" (10651)

1. Hand "Child's Tear" (1673) to citymist/"Lord Rak-Ashiir". Spawns "Lord Rak'Ashiir" (90183). Loot "Iksar Scale" (1674) from "Lord Rak'Ashiir".
2. Loot "Iksar Scale" (1674) from "Lord Rak'Ashiir".
3. emeraldjungle/"Spirit Sentinel", hand "Iksar Scale" (1674). Gives "Spear of Fate" (10651).

### "Distilled Potion of Endurance" (52921)

1. shadeweaver/"Wunshi Kashra", hand platinum:1000. Gives "Thatched Medicine Bag" (57704).
2. Loot "Bleak Fungus" (57620) from "Shuddering Fungus" in `fungusgrove`.
3. Say "Up To It" to lakerathe/"Kimm Mcshannel".
4. Spawns "Ancient Megalodon" (51160).
5. Loot "Lustrous Seaweed" (52926) from "Ancient Megalodon".
6. lakerathe/"Kimm Mcshannel", hand "Lustrous Seaweed" (52926). Gives "Twine-Wrapped Lustrous Seaweed" (57600).
7. Combine in "Thatched Medicine Bag" (57704): "Bleak Fungus" (57620), "Twine-Wrapped Lustrous Seaweed" (57600). Produces "Shadowed Pulp" (57550). Requires Alchemy 100. Trivial at 175. The combine does not fail.
8. Ground spawn of "Twinkling Shrub" (57080) in `twilight`.
9. twilight/"Tikl Huk", hand "Twinkling Shrub" (57080). Gives "Tied Twinkling Shrubs" (52920).
10. Say "Elder Spirit Sent Me" to cobaltscar/"Yoppa Greenthumb".
11. Spawns "Gnashing Killer Shark" (117091).
12. Loot "Brittle Burned Bark" (57086) from "Gnashing Killer Shark".
13. Combine in "Thatched Medicine Bag" (57704): "Tied Twinkling Shrubs" (52920), "Brittle Burned Bark" (57086). Produces "Brittle Twigs" (57369). Requires Alchemy 100. Trivial at 175. The combine does not fail.
14. warrens/"Wilslik Gissu", hand "Brittle Twigs" (57369) + "Shadowed Pulp" (57550). Gives "Distilled Potion of Endurance" (52921).

### "Blessed Talisman of Wisdom" (57083)

1. freeportwest/"Elder Spirit Of Enlightenment", say "Rare Gift". Gives "Potion of Sustenance" (57081).
2. freportn/"Elder Spirit Of Enlightenment", say "Rare Gift". Gives "Potion of Sustenance" (57081).
3. airplane/"Eternal Spirit", hand "Potion of Sustenance" (57081). Gives "Blessed Talisman of Wisdom" (57083).

### "Runed Purse of the McShannels" (57614)

1. lakerathe/"Kimm Mcshannel", say "Break Down". Gives "Heyokah Medicine Bag" (52922).
2. Loot "Revenant Tooth" (57500) from "A Sun Revenant" in `thegrey`.
3. Loot "Perfect Marked Ukun Skin" (57701) from "Fang" in `draniksscar`.
4. Loot "Perfect Marked Ukun Skin" (57701) from "Ukun Gutfeaster" in `draniksscar`.
5. Loot "Perfect Marked Ukun Skin" (57701) from "Ukun Slavehunter" in `draniksscar`.
6. Loot "Corrosive Goo" (57100) from "A Pulsating Bile" in `charasis`.
7. Loot "Corruption Powder" (57520) from "Elite Corrupted Knight" in `codecay`.
8. Combine in "Heyokah Medicine Bag" (52922): "Revenant Tooth" (57500), "Perfect Marked Ukun Skin" (57701), "Corrosive Goo" (57100), "Corruption Powder" (57520). Produces "Shaman's Precious Diffusing Agent" (57560). Requires Alchemy 100. The combine does not fail.
9. lakerathe/"Kimm Mcshannel", hand "Shaman's Precious Diffusing Agent" (57560). Gives "Runed Purse of the McShannels" (57614).

### "Impervious Medicine Bag" (57551)

1. Spawns "Darkened Chanting Woodspirit" (210250) in `postorms` on enter.
2. Loot "Piece of Moaning Timber" (57403) from "Darkened Chanting Woodspirit".
3. fungusgrove/"Lupot Nukla", hand "Piece of Moaning Timber" (57403). Gives "Impervious Medicine Bag" (57551).

### "Glowing Spirit Charm of Might" (57987)

1. freeportwest/"Elder Spirit Of Enlightenment", say "Seek". Gives "Pouch of Spirit Dust" (57710).
2. freportn/"Elder Spirit Of Enlightenment", say "Seek". Gives "Pouch of Spirit Dust" (57710).
3. Spawns "A Phase Spider" (123190) in `necropolis` on event_combat.
4. Loot "Spirit-Touched Phased Spider Thorax" (57562) from "A Phase Spider".
5. Spawns "Lightning Warrior Spiritseeker" (316073) in `provinggrounds` on enter.
6. Loot "Glowing Trace of Might" (57250) from "Lightning Warrior Spiritseeker".
7. Say "Ready" to causeway/"Kupiop Iku".
8. Spawns "epic version of Murkglider School Leader" (303116).
9. Loot "Slight Trace of a Spirit" (57800) from "epic version of Murkglider School Leader".
10. Loot "Slight Trace of a Spirit" (57800) from "Murkglider School Leader".
11. Loot "Reviving Potion of Might" (57315) from "Bloated Girplan" in `dranik`.
12. Combine in "Pouch of Spirit Dust" (57710): "Spirit-Touched Phased Spider Thorax" (57562), "Glowing Trace of Might" (57250), "Slight Trace of a Spirit" (57800), "Reviving Potion of Might" (57315). Produces "Glowing Spirit Charm of Might" (57987). The combine does not fail.

## `shaman_pre`

Values written: 1, 2, 3.

### 1. elder spirit of enlightenment — say hail

Zone: `freeportwest`.

> It appears you are not yet ready for the great tasks that I require to be done. There are others lesser than me that can guide you and prepare you to walk a ...

Sets `shaman_pre` to `1`.

- Needs Crafted Talisman of Fates (57400).
- Needs `shaman_pre` unset.
In script order:

1. Sets `shaman_pre` to `1`.


How the items are reached:

- Crafted Talisman of Fates (57400)
  - Given by freeportwest/"Elder Spirit Of Enlightenment", say "Acknowledge".
  - Given by freportn/"Elder Spirit Of Enlightenment", say "Acknowledge".

### 1. elder spirit of enlightenment — say hail

Zone: `freportn`.

> It appears you are not yet ready for the great tasks that I require to be done. There are others lesser than me that can guide you and prepare you to walk a ...

Sets `shaman_pre` to `1`.

- Needs Crafted Talisman of Fates (57400).
- Needs `shaman_pre` unset.
In script order:

1. Sets `shaman_pre` to `1`.


How the items are reached:

- Crafted Talisman of Fates (57400)
  - Given by freeportwest/"Elder Spirit Of Enlightenment", say "Acknowledge".
  - Given by freportn/"Elder Spirit Of Enlightenment", say "Acknowledge".

### 2. spirit sentinel — hand 1678

Zone: `lakeofillomen`.

Sets `shaman_pre` to `2`.

- Needs `shaman_pre` ==1.
- Turn in x1: Black Fur Boots (1678).
In script order:

1. Sets `shaman_pre` to `2`.


How the items are reached:

- Black Fur Boots (1678)
  - Prerequisite: "Black Fur Boots" (1678). See section 0.

### 3. spirit sentinel — hand 57988+57989+57990+57991

Zone: `lakeofillomen`.

Sets `shaman_pre` to `3`.

- Turn in x1: Crystallized Blood (57988).
- Turn in x1: Clouded Glass Vial (57991).
- Turn in x1: Stonemite Antennae (57990).
- Turn in x1: Mellian Leaf (57989).
In script order:

1. Sets `shaman_pre` to `3`.


How the items are reached:

- Crystallized Blood (57988)
  - Loot "Crystallized Blood" (57988) from "A Crystalline Arachnae" in `povalor`.
- Clouded Glass Vial (57991)
  - Given by southro/"Bratoq Jiplup", hand platinum:2000.
  - Given by sro/"Bratoq Jiplup", hand platinum:2000.
- Stonemite Antennae (57990)
  - No quest step gives Stonemite Antennae (57990). The dump lists it in natimbi, qinimi, riwwi.
- Mellian Leaf (57989)
  - Loot "Mellian Leaf" (57989) from "A Malarian Crysalis" in `podisease`.

## `shaman_epic`

Values written: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15.

### 1. elder spirit of enlightenment — say shaman

Zone: `freeportwest`.

> Ah, yes. You are not only a shaman, but one who has passed the tests of the heyokah. There are many problems that face us now and I grow weaker by the day. I...

Sets `shaman_epic` to `1`.

- Needs `shaman_epic` unset.
- One of: Spear of Fate (10651); Spear of Fate (36223).
In script order:

1. Sets `shaman_epic` to `1`.


How the items are reached:

- Spear of Fate (10651)
  - Prerequisite: "Spear of Fate" (10651). See section 0.
- Spear of Fate (36223)
  - Same item as "Spear of Fate" (10651).
  - Given by emeraldjungle/"Spirit Sentinel", hand "Iksar Scale" (1674).

### 1. elder spirit of enlightenment — say shaman

Zone: `freportn`.

> Ah, yes. You are not only a shaman, but one who has passed the tests of the heyokah. There are many problems that face us now and I grow weaker by the day. I...

Sets `shaman_epic` to `1`.

- Needs `shaman_epic` unset.
- One of: Spear of Fate (10651); Spear of Fate (36223).
In script order:

1. Sets `shaman_epic` to `1`.


How the items are reached:

- Spear of Fate (10651)
  - Prerequisite: "Spear of Fate" (10651). See section 0.
- Spear of Fate (36223)
  - Same item as "Spear of Fate" (10651).
  - Given by emeraldjungle/"Spirit Sentinel", hand "Iksar Scale" (1674).

### 2. elder spirit of enlightenment — hand 52921

Zones: `freeportwest`, `freportn`.

Sets `shaman_epic` to `2`.

- Needs `shaman_epic` ==1.
- Turn in x1: Distilled Potion of Endurance (52921).
In script order:

1. Sets `shaman_epic` to `2`.


How the items are reached:

- Distilled Potion of Endurance (52921)
  - Prerequisite: "Distilled Potion of Endurance" (52921). See section 0.

### 3. elder spirit of enlightenment — hand 57083+57084

Zones: `freeportwest`, `freportn`.

Sets `shaman_epic` to `3`.

- Needs `shaman_epic` ==2.
- Turn in x1: Blessed Talisman of Wisdom (57083).
- Turn in x1: Blessed Talisman of Patience (57084).
In script order:

1. Sets `shaman_epic` to `3`.


How the items are reached:

- Blessed Talisman of Wisdom (57083)
  - Prerequisite: "Blessed Talisman of Wisdom" (57083). See section 0.
- Blessed Talisman of Patience (57084)
  - Spawns "Punisher Veshtaq" (201455) in `pojustice` on event_timer.
  - Loot "Blessed Talisman of Patience" (57084) from "Punisher Veshtaq".
  - Loot "Blessed Talisman of Patience" (57084) from "Punisher Veshtaq".

### 4. wunshi kashra — hand 57085+57087

Zone: `shadeweaver`.

Sets `shaman_epic` to `4`.

- Needs `shaman_epic` ==3.
- Turn in x1: Amulet of the Spiritist (57087).
- Turn in x1: Ring of the Undead Spiritcharmer (57085).
In script order:

1. Sets `shaman_epic` to `4`.


How the items are reached:

- Amulet of the Spiritist (57087)
  - Loot "Amulet of the Spiritist" (57087) from "Netherbian Swarmfiend" in `umbral`.
- Ring of the Undead Spiritcharmer (57085)
  - Spawns "Spiritseeker Nadox" (227319) in `nadox` on enter.
  - Loot "Ring of the Undead Spiritcharmer" (57085) from "Spiritseeker Nadox".
  - Loot "Ring of the Undead Spiritcharmer" (57085) from "Spiritseeker Nadox".
  - Loot "Ring of the Undead Spiritcharmer" (57085) from "Spiritseeker Nadox" in `nadox`.

### 5. kimm mcshannel — hand 57088

Zone: `lakerathe`.

Sets `shaman_epic` to `5`.

- Turn in x1: Gemmed Bangle of Enlightenment (57088).
In script order:

1. Sets `shaman_epic` to `5`.


How the items are reached:

- Gemmed Bangle of Enlightenment (57088)
  - Given by freeportwest/"Elder Spirit Of Enlightenment", say "Business With Wunshi Is Finished".
  - Given by freportn/"Elder Spirit Of Enlightenment", say "Business With Wunshi Is Finished".

### 6. elder spirit of enlightenment — hand 57614

Zones: `freeportwest`, `freportn`.

Sets `shaman_epic` to `6`.

- Needs `shaman_epic` ==5.
- Turn in x1: Runed Purse of the McShannels (57614).
In script order:

1. Sets `shaman_epic` to `6`.


How the items are reached:

- Runed Purse of the McShannels (57614)
  - Prerequisite: "Runed Purse of the McShannels" (57614). See section 0.

### 7. elder spirit of enlightenment — say acknowledge

Zone: `freeportwest`.

> We, the spirits, have chosen to grant you a gift for all that you

Sets `shaman_epic` to `7`.

- Needs `shaman_epic` ==6.
In script order:

1. Sets `shaman_epic` to `7`.
2. Gives Crafted Talisman of Fates (57400).


### 7. elder spirit of enlightenment — say acknowledge

Zone: `freportn`.

> We, the spirits, have chosen to grant you a gift for all that you

Sets `shaman_epic` to `7`.

- Needs `shaman_epic` ==6.
In script order:

1. Sets `shaman_epic` to `7`.
2. Gives Crafted Talisman of Fates (57400).


### 8. elder spirit of enlightenment — say prepared to carry on

Zone: `freeportwest`.

> I knew we could count on you,

Sets `shaman_epic` to `8`.

- Needs Crafted Talisman of Fates (57400).
- Needs `shaman_epic` unset.
In script order:

1. Sets `shaman_epic` to `8`.


How the items are reached:

- Crafted Talisman of Fates (57400)
  - Given by freeportwest/"Elder Spirit Of Enlightenment", say "Acknowledge".
  - Given by freportn/"Elder Spirit Of Enlightenment", say "Acknowledge".

### 8. elder spirit of enlightenment — say prepared to carry on

Zone: `freportn`.

> I knew we could count on you,

Sets `shaman_epic` to `8`.

- Needs Crafted Talisman of Fates (57400).
- Needs `shaman_epic` unset.
In script order:

1. Sets `shaman_epic` to `8`.


How the items are reached:

- Crafted Talisman of Fates (57400)
  - Given by freeportwest/"Elder Spirit Of Enlightenment", say "Acknowledge".
  - Given by freportn/"Elder Spirit Of Enlightenment", say "Acknowledge".

### 9. lupot nukla — say taken by force

Zone: `fungusgrove`.

> Over in Taelosia, the peaceful folk there found themselves overcome by the Muramites. They had stolen much of what had meaning to them. If you can track down...

Sets `shaman_epic` to `9`.

- Needs `shaman_epic` ==8.
In script order:

1. Sets `shaman_epic` to `9`.


### 10. lupot nukla — hand 57401

Zone: `fungusgrove`.

Sets `shaman_epic` to `10`.

- Needs `shaman_epic` ==9.
- Turn in x1: Necklace of Perseverance (57401).
In script order:

1. Sets `shaman_epic` to `10`.


How the items are reached:

- Necklace of Perseverance (57401)
  - Say "Hail" to kodtaz/"Undari Perunea".
  - Spawns "Ikaav Spiritstealer" (293233).
  - Loot "Necklace of Perseverance" (57401) from "Ikaav Spiritstealer".
  - Loot "Necklace of Perseverance" (57401) from "Ikaav Spiritstealer".

### 11. elder spirit of enlightenment — hand 57551

Zones: `freeportwest`, `freportn`.

Sets `shaman_epic` to `11`.

- Needs `shaman_epic` ==10.
- Turn in x1: Impervious Medicine Bag (57551).
In script order:

1. Sets `shaman_epic` to `11`.


How the items are reached:

- Impervious Medicine Bag (57551)
  - Prerequisite: "Impervious Medicine Bag" (57551). See section 0.

### 12. elder spirit of enlightenment — hand 57987

Zones: `freeportwest`, `freportn`.

Sets `shaman_epic` to `12`.

- Needs `shaman_epic` ==11.
- Turn in x1: Glowing Spirit Charm of Might (57987).
In script order:

1. Sets `shaman_epic` to `12`.


How the items are reached:

- Glowing Spirit Charm of Might (57987)
  - Prerequisite: "Glowing Spirit Charm of Might" (57987). See section 0.

### 13. elder spirit of enlightenment — hand 57404

Zones: `freeportwest`, `freportn`.

Sets `shaman_epic` to `13`.

- Needs `shaman_epic` ==12.
- Turn in x1: Spiritcaller Beads (57404).
In script order:

1. Sets `shaman_epic` to `13`.


How the items are reached:

- Spiritcaller Beads (57404)
  - Say "Fooled" to wallofslaughter/"Hudar Trittan".
  - Spawns "Discordling Spiritcaller" (300091).
  - Loot "Spiritcaller Beads" (57404) from "Discordling Spiritcaller".
  - Loot "Spiritcaller Beads" (57404) from "Discordling Spiritcaller".

### 14. elder spirit of enlightenment — hand 47100

Zones: `freeportwest`, `freportn`.

Sets `shaman_epic` to `14`.

- Needs `shaman_epic` ==13.
- Turn in x1: Globe of Discordant Energy (47100).
In script order:

1. Sets `shaman_epic` to `14`.


How the items are reached:

- Globe of Discordant Energy (47100)
  - Say "Check Lorb" to anguish/"Zone Status".
  - Spawns "Orb of Discordant Energy" (317087).
  - Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy".
  - Say "Check Lorb" to anguish/"Zone Status".
  - Spawns "Orb of Discordant Energy" (317087).
  - Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy".
  - Say "Check Uorb" to anguish/"Zone Status".
  - Spawns "Orb of Discordant Energy" (317087).
  - Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy".
  - Say "Check Amv Chest" to anguish/"Zone Status".
  - Spawns "Ornate Chest" (317112).
  - Loot "Globe of Discordant Energy" (47100) from "Ornate Chest".
  - 2 other loot steps also yield Globe of Discordant Energy (47100).
  - Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy" in `anguish`.
  - Loot "Globe of Discordant Energy" (47100) from "Ornate Chest".
  - Loot "Globe of Discordant Energy" (47100) from "Overlords Chest".

### 15. elder spirit of enlightenment — hand 57400

Zones: `freeportwest`, `freportn`.

Sets `shaman_epic` to `15`.

- Needs `shaman_epic` ==14.
- Turn in x1: Crafted Talisman of Fates (57400).
In script order:

1. Sets `shaman_epic` to `15`.
2. Gives Blessed Spiritstaff of the Heyokah (57405).


How the items are reached:

- Crafted Talisman of Fates (57400)
  - Given by freeportwest/"Elder Spirit Of Enlightenment", say "Acknowledge".
  - Given by freportn/"Elder Spirit Of Enlightenment", say "Acknowledge".

### Steps on `shaman_epic` that do not change it

- `causeway` kupiop iku, say ready needs `shaman_epic` ==11.
  - Spawns epic version of Murkglider School Leader (303116).
  - Loots Slight Trace of a Spirit (57800).
- `cobaltscar` yoppa greenthumb, say elder spirit sent me needs `shaman_epic` ==1.
  - Spawns Gnashing Killer Shark (117091).
  - Spawns Darting Shark (117089).
  - Spawns Feeder Shark (117090).
  - Loots Brittle Burned Bark (57086).
- `dranik` player, on loot needs `shaman_epic` ==11.
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
- `freeportwest` elder spirit of enlightenment, say business with wunshi is finished needs `shaman_epic` ==4.
  - Gives Gemmed Bangle of Enlightenment (57088).
- `freeportwest` elder spirit of enlightenment, say prepared for the ceremony needs `shaman_epic` ==14.
  - Spawns Elder Spirit of Perseverance (8119).
  - Spawns Elder Spirit of Understanding (8120).
  - Spawns Elder Spirit of Fortitude (8121).
  - Spawns Elder Spirit of Will (8122).
  - Spawns Elder Spirit of Sense (8123).
- `freeportwest` elder spirit of enlightenment, say rare gift needs `shaman_epic` ==2.
  - Gives Potion of Sustenance (57081).
- `freeportwest` elder spirit of enlightenment, say seek needs `shaman_epic` ==11.
  - Gives Pouch of Spirit Dust (57710).
- `freportn` elder spirit of enlightenment, say business with wunshi is finished needs `shaman_epic` ==4.
  - Gives Gemmed Bangle of Enlightenment (57088).
- `freportn` elder spirit of enlightenment, say prepared for the ceremony needs `shaman_epic` ==14.
  - Spawns Elder Spirit of Perseverance (8119).
  - Spawns Elder Spirit of Understanding (8120).
  - Spawns Elder Spirit of Fortitude (8121).
  - Spawns Elder Spirit of Will (8122).
  - Spawns Elder Spirit of Sense (8123).
- `freportn` elder spirit of enlightenment, say rare gift needs `shaman_epic` ==2.
  - Gives Potion of Sustenance (57081).
- `freportn` elder spirit of enlightenment, say seek needs `shaman_epic` ==11.
  - Gives Pouch of Spirit Dust (57710).
- `fungusgrove` lupot nukla, hand 57403 needs `shaman_epic` ==10.
  - Turn in Piece of Moaning Timber (57403).
  - Gives Impervious Medicine Bag (57551).
- `kodtaz` undari perunea, say hail needs `shaman_epic` ==9.
  - Spawns Ikaav Spiritstealer (293233).
  - Loots Lucidem (35084).
  - Loots Versluierd Fungus (35087).
  - Loots Uncut Jacinth (37850).
  - Loots Necklace of Perseverance (57401).
- `lakerathe` kimm mcshannel, say break down needs `shaman_epic` ==5.
  - Gives Heyokah Medicine Bag (52922).
- `lakerathe` kimm mcshannel, say up to it needs `shaman_epic` ==1.
  - Spawns Ancient Megalodon (51160).
  - Loots Lustrous Seaweed (52926).
- `lakerathe` player, on loot needs `shaman_epic` >=1.
  - Sets `shaman_epic_lakerathechest` to `1`.
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
- `postorms` 210252, on enter needs `shaman_epic` ==10.
  - Spawns Darkened Chanting Woodspirit (210250).
  - Loots Versluierd Fungus (35087).
  - Loots Piece of Moaning Timber (57403).
  - Loots Staurolite (97002).
- `provinggrounds` stilled lightning warrior, on enter needs `shaman_epic` ==11.
  - Spawns Lightning Warrior Spiritseeker (316073).
  - Loots Lucidem (35084).
  - Loots Versluierd Fungus (35087).
  - Loots Glowing Trace of Might (57250).
- `shadeweaver` wunshi kashra, say stolen needs `shaman_epic` ==3.
  - Sets `shaman_epic_nadox` to `1`.
- `umbral` player, on loot needs `shaman_epic` >=3.
  - Sets `shaman_epic_umbralchest` to `1`.
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
- `wallofslaughter` hudar trittan, say fooled needs `shaman_epic` ==12.
  - Spawns Discordling Spiritcaller (300091).
  - Loots Platinum Etched Gear #2 (37047).
  - Loots Platinum Etched Gear #3 (37048).
  - Loots Spiritcaller Beads (57404).
  - Loots Polished Blue Softstone (80030).
  - Loots Old Eternal Grove Leather Wrist Ornament (84538).
  - Loots Old Eternal Grove Cloth Wrist Ornament (84545).
- `wallofslaughter` player, on loot needs `shaman_epic` ==12.
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
- `warrens` wilslik gissu, hand 57369+57550 needs `shaman_epic` ==1.
  - Turn in Shadowed Pulp (57550).
  - Turn in Brittle Twigs (57369).
  - Gives Distilled Potion of Endurance (52921).

## Other flags touched along the way

- `shaman_epic_lakerathechest` set to 1 at lakerathe/player.
- `shaman_epic_nadox` set to 1 at shadeweaver/wunshi kashra.
- `shaman_epic_nadoxrespawn` set to 1 at nadox/player.
- `shaman_epic_umbralchest` set to 1 at umbral/player.
- `shaman_epic_wos` set to 1 at wallofslaughter/player.
