# Magician

Steps taken from the quest graph only. **Broken** means the graph has no edge for that value or that item.

Flags with writes: `mage_epic`.

## 0. Prerequisites

Each list is the order you obtain that item. Later steps point here instead of repeating the chain.

### "Staff of Elemental Essence" (19092)

1. najena/"Akksstaff'S Minion", on event_death_complete. Sets `ask_minion_dead` to `1`.
2. najena/"Akksstaff", say "Demise". Requires `ask_minion_dead` set. Gives "Sentience of Elements" (15778).
3. poknowledge/"Bantil Io'Tuv", hand "Sentience of Elements" (15778). Sets `mage_epic` to `6`.
4. Hand "Ice Burrower Meat" (19022) + "Ice Burrower Meat" (19022) + "Ice Burrower Meat" (19022) + "Ice Burrower Meat" (19022) to cobaltscar/"High Priest Margle". Spawns "Tiknonmanin" (117094). Loot "Elemental Essence of Water" (19086) from "Tiknonmanin".
5. Loot "Elemental Essence of Water" (19086) from "Tiknonmanin".
6. Spawns "Elemental Essence of Fire" (214127) in `potactics` on event_waypoint_arrive.
7. Loot "Elemental Essence of Fire" (16807) from "Elemental Essence of Fire".
8. Spawns "Elemental Essence of Air" (303100) in `causeway` on enter.
9. Loot "Elemental Essence of Air" (16773) from "Elemental Essence of Air".
10. Spawns "Elemental Essence of Earth" (169127) in `letalis` on enter.
11. Loot "Elemental Essence of Earth" (19087) from "Elemental Essence of Earth".
12. poknowledge/"Bantil Io'Tuv", hand "Elemental Essence of Air" (16773) + "Elemental Essence of Fire" (16807) + "Elemental Essence of Water" (19086) + "Elemental Essence of Earth" (19087). Requires `mage_epic` ==6. Gives "Staff of Elemental Essence" (19092).

### "Note from Iilivina" (19438)

1. No quest step gives Gelidran Essence (19099). The dump lists it in riftseekers.
2. No quest step gives Pyrilen Essence (19093). The dump lists it in riftseekers.
3. draniksscar/"Iilivina", hand "Pyrilen Essence" (19093) + "Pyrilen Essence" (19093) + "Gelidran Essence" (19099) + "Gelidran Essence" (19099). Gives "Note from Iilivina" (19438).

### "Pouch of Powdered Riftseeker Essence" (19149)

1. No quest step gives Gelidran Essence (19099). The dump lists it in riftseekers.
2. No quest step gives Pyrilen Essence (19093). The dump lists it in riftseekers.
3. draniksscar/"Iilivina", hand "Pyrilen Essence" (19093) + "Pyrilen Essence" (19093) + "Gelidran Essence" (19099) + "Gelidran Essence" (19099). Gives "Pouch of Powdered Riftseeker Essence" (19149).

### "Small pouch of Riftseeker Essence" (19441)

1. No quest step gives Gelidran Essence (19099). The dump lists it in riftseekers.
2. No quest step gives Pyrilen Essence (19093). The dump lists it in riftseekers.
3. draniksscar/"Iilivina", hand "Pyrilen Essence" (19093) + "Pyrilen Essence" (19093) + "Gelidran Essence" (19099) + "Gelidran Essence" (19099). Gives "Note from Iilivina" (19438).
4. draniksscar/"Iilivina", hand "Pyrilen Essence" (19093) + "Pyrilen Essence" (19093) + "Gelidran Essence" (19099) + "Gelidran Essence" (19099). Gives "Pouch of Powdered Riftseeker Essence" (19149).
5. poknowledge/"Bantil Io'Tuv", hand "Pouch of Powdered Riftseeker Essence" (19149) + "Note from Iilivina" (19438). Gives "Small pouch of Riftseeker Essence" (19441).

## `mage_epic`

Values written: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11.

### 1. bantil io`tuv — say hail

Zone: `poknowledge`.

Sets `mage_epic` to `1`.

- Needs Orb of Mastery (28034).
- Needs `mage_epic` unset.
In script order:

1. Sets `mage_epic` to `1`.


How the items are reached:

- Orb of Mastery (28034)
  - Summon "Orb of Mastery" (28034) by casting "Summon Orb".
  - Loot "Orb of Mastery" (28034) from "Carreenu Opulaae" in `chambersf`.
  - Loot "Orb of Mastery" (28034) from "Gaelin" in `chambersf`.
  - Loot "Orb of Mastery" (28034) from "Ipputs Dagglebrap" in `chambersf`.
  - Loot "Orb of Mastery" (28034) from "Melodite Arinal" in `chambersf`.
  - Loot "Orb of Mastery" (28034) from "Nakert Grimmagus" in `chambersf`.

### 1. bantil io`tuv — hand 11998+14941+14960+14966

Zone: `poknowledge`.

Sets `mage_epic` to `1`.

- Turn in x1: Captured Monsoon Elemental (14960).
- Turn in x1: Captured Earthquake Elemental (11998).
- Turn in x1: Captured Wildfire Elemental (14941).
- Turn in x1: Captured Tsunami Elemental (14966).
In script order:

1. Sets `mage_epic` to `1`.


How the items are reached:

- Captured Monsoon Elemental (14960)
  - Loot "Captured Monsoon Elemental" (14960) from "Swirling Monsoon Elemental" in `postorms`.
- Captured Earthquake Elemental (11998)
  - Loot "Captured Earthquake Elemental" (11998) from "Trembling Earthquake Elemental" in `thegrey`.
- Captured Wildfire Elemental (14941)
  - Loot "Captured Wildfire Elemental" (14941) from "Raging Wildfire Elemental" in `shadeweaver`.
- Captured Tsunami Elemental (14966)
  - Loot "Captured Tsunami Elemental" (14966) from "Ravaging Tsunami Elemental" in `sirens`.

### 2. bantil io`tuv — hand 15639

Zone: `poknowledge`.

Sets `mage_epic` to `2`.

- Turn in x1: Journal of Magus Tvish (15639).
In script order:

1. Sets `mage_epic` to `2`.


How the items are reached:

- Journal of Magus Tvish (15639)
  - No quest step gives Journal of Magus Tvish (15639). The dump lists it in akheva, eastkorlacha.

### 3. bantil io`tuv — hand 15769

Zone: `poknowledge`.

Sets `mage_epic` to `3`.

- Turn in x1: Tome of Primal Fires (15769).
In script order:

1. Sets `mage_epic` to `3`.


How the items are reached:

- Tome of Primal Fires (15769)
  - Requires `mage_epic` ==2
  - Given by westwastes/"A Lost Tomekeeper", say "Violet Roses".

### 4. bantil io`tuv — hand 15772

Zone: `poknowledge`.

Sets `mage_epic` to `4`.

- Needs `mage_epic` ==3.
- Turn in x1: Book of Bindings and Incantations (15772).
In script order:

1. Sets `mage_epic` to `4`.


How the items are reached:

- Book of Bindings and Incantations (15772)
  - Ground spawn of "Book of Bindings and Incantations" (15772) in `charasis`.

### 5. bantil io`tuv — hand 15775

Zone: `poknowledge`.

Sets `mage_epic` to `5`.

- Needs `mage_epic` ==4.
- Turn in x1: Codex of Ice and Ether (15775).
In script order:

1. Sets `mage_epic` to `5`.


How the items are reached:

- Codex of Ice and Ether (15775)
  - Loot "Codex of Ice and Ether" (15775) from "Grigor Rojha" in `thedeep`.

### 6. bantil io`tuv — hand 15778

Zone: `poknowledge`.

Sets `mage_epic` to `6`.

- Needs `mage_epic` ==5.
- Turn in x1: Sentience of Elements (15778).
In script order:

1. Sets `mage_epic` to `6`.


How the items are reached:

- Sentience of Elements (15778)
  - Requires `ask_minion_dead` set
  - Given by najena/"Akksstaff", say "Demise".

### 7. bantil io`tuv — hand 16773+16807+19086+19087

Zone: `poknowledge`.

Sets `mage_epic` to `7`.

- Needs `mage_epic` ==6.
- Turn in x1: Elemental Essence of Water (19086).
- Turn in x1: Elemental Essence of Fire (16807).
- Turn in x1: Elemental Essence of Air (16773).
- Turn in x1: Elemental Essence of Earth (19087).
In script order:

1. Sets `mage_epic` to `7`.
2. Gives Staff of Elemental Essence (19092).


How the items are reached:

- Elemental Essence of Water (19086)
  - Hand "Ice Burrower Meat" (19022) + "Ice Burrower Meat" (19022) + "Ice Burrower Meat" (19022) + "Ice Burrower Meat" (19022) to cobaltscar/"High Priest Margle". Spawns "Tiknonmanin" (117094). Loot "Elemental Essence of Water" (19086) from "Tiknonmanin".
  - Loot "Elemental Essence of Water" (19086) from "Tiknonmanin".
- Elemental Essence of Fire (16807)
  - Spawns "Elemental Essence of Fire" (214127) in `potactics` on event_waypoint_arrive.
  - Loot "Elemental Essence of Fire" (16807) from "Elemental Essence of Fire".
  - Loot "Elemental Essence of Fire" (16807) from "Elemental Essence of Fire".
- Elemental Essence of Air (16773)
  - Spawns "Elemental Essence of Air" (303100) in `causeway` on enter.
  - Loot "Elemental Essence of Air" (16773) from "Elemental Essence of Air".
  - Loot "Elemental Essence of Air" (16773) from "Elemental Essence of Air".
- Elemental Essence of Earth (19087)
  - Spawns "Elemental Essence of Earth" (169127) in `letalis` on enter.
  - Loot "Elemental Essence of Earth" (19087) from "Elemental Essence of Earth".
  - Loot "Elemental Essence of Earth" (19087) from "Elemental Essence of Earth".

### 8. iilivina — hand 19092

Zone: `draniksscar`.

Sets `mage_epic` to `8`.

- Needs `mage_epic` ==7.
- Turn in x1: Staff of Elemental Essence (19092).
In script order:

1. Sets `mage_epic` to `8`.
2. Gives Staff of Elemental Essence (19092).


How the items are reached:

- Staff of Elemental Essence (19092)
  - Prerequisite: "Staff of Elemental Essence" (19092). See section 0.

### 9. bantil io`tuv — hand 19149+19438

Zone: `poknowledge`.

Sets `mage_epic` to `9`.

- Turn in x1: Note from Iilivina (19438).
- Turn in x1: Pouch of Powdered Riftseeker Essence (19149).
In script order:

1. Sets `mage_epic` to `9`.
2. Gives Small pouch of Riftseeker Essence (19441).


How the items are reached:

- Note from Iilivina (19438)
  - Prerequisite: "Note from Iilivina" (19438). See section 0.
- Pouch of Powdered Riftseeker Essence (19149)
  - Prerequisite: "Pouch of Powdered Riftseeker Essence" (19149). See section 0.

### 9. vornol transon — hand 19441

Zone: `twilight`.

Sets `mage_epic` to `9`.

- Turn in x1: Small pouch of Riftseeker Essence (19441).
In script order:

1. Sets `mage_epic` to `9`.


How the items are reached:

- Small pouch of Riftseeker Essence (19441)
  - Prerequisite: "Small pouch of Riftseeker Essence" (19441). See section 0.

### 10. iilivina — say primals

Zone: `draniksscar`.

> Were I to venture a guess, I

Sets `mage_epic` to `10`.

- Needs `mage_epic` >=9.
In script order:

1. Sets `mage_epic` to `10`.


### 11. iilivina — hand 19444+19447+19544+19547

Zone: `draniksscar`.

Sets `mage_epic` to `11`.

- Turn in x1: Element of Order (19547).
- Turn in x1: Element of Body (19447).
- Turn in x1: Element of Chaos (19444).
- Turn in x1: Element of Spirit (19544).
In script order:

1. Sets `mage_epic` to `11`.


How the items are reached:

- Element of Order (19547)
  - Spawns "Order Elemental" (211057) in `hohonora` on enter.
  - Loot "Element of Order" (19547) from "Order Elemental".
  - Loot "Element of Order" (19547) from "Order Elemental".
- Element of Body (19447)
  - Spawns "Body Elemental" (284105) in `ferubi` on enter.
  - Loot "Element of Body" (19447) from "Body Elemental".
  - Loot "Element of Body" (19447) from "Body Elemental".
- Element of Chaos (19444)
  - Spawns "Chaos Elemental" (86174) in `dreadlands` on enter.
  - Loot "Element of Chaos" (19444) from "Chaos Elemental".
  - Loot "Element of Chaos" (19444) from "Chaos Elemental".
- Element of Spirit (19544)
  - Spawns "Spirit Elemental" (200060) in `codecay` on enter.
  - Loot "Element of Spirit" (19544) from "Spirit Elemental".
  - Loot "Element of Spirit" (19544) from "Spirit Elemental".

### Steps on `mage_epic` that do not change it

- `codecay` mage trap, on enter needs `mage_epic` ==10.
  - Sets `mage_epic_cod` to `1`.
  - Spawns Spirit Elemental (200060).
  - Loots Element of Spirit (19544).
- `dreadlands` mage trap, on enter needs `mage_epic` ==10.
  - Sets `mage_epic_dl` to `1`.
  - Spawns Chaos Elemental (86174).
  - Loots Element of Chaos (19444).
- `dreadlands` player, on enter needs `mage_epic` set.
  - Spawns Time Terror (86172).
  - Loots Time Terror Essence (63130).
- `dreadlands` player, on loot needs `mage_epic` set.
  - Sets `mage_chest_dl` to `1`.
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
- `ferubi` mage trap, on enter needs `mage_epic` ==10.
  - Sets `mage_epic_ferubi` to `1`.
  - Spawns Body Elemental (284105).
  - Loots Element of Body (19447).
  - Loots Lucidem (35084).
- `ferubi` player, on enter needs `mage_epic` ==10.
  - Sets `paladin_epic_ferubi` to `1`.
  - Spawns Shade of Reiya the Pained (284104).
  - Loots Soulstone Shard (69943).
- `hohonora` mage trap, on enter needs `mage_epic` ==10.
  - Sets `mage_epic_hoh` to `1`.
  - Spawns Order Elemental (211057).
  - Loots Element of Order (19547).
- `hohonora` player, on loot needs `mage_epic` ==10.
  - Sets `mage_chest_hoh` to `1`.
  - Spawns a chest (893).
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
- `najena` akksstaff, say bantil sent me needs `mage_epic` set.
  - Spawns Akksstaff`s Minion (44108).
- `poknowledge` bantil io`tuv, hand 19092+47100 needs `mage_epic` ==11.
  - Turn in Globe of Discordant Energy (47100).
  - Turn in Staff of Elemental Essence (19092).
  - Gives Focus of Primal Elements (19839).
- `poknowledge` bantil io`tuv, say pieces needs `mage_epic` ==1.
  - Gives Tattered Note (15005).
- `potranquility` jurmak the undertow, say elemental essences needs `mage_epic` ==6.
  - Sets `mage_epic_water1` to `1`.
- `potranquility` miak the searedsoul, say elemental essences needs `mage_epic` ==6.
  - Sets `mage_epic_fire1` to `1`.
- `potranquility` sarhya the dawnbreeze, say elemental essences needs `mage_epic` ==6.
  - Sets `mage_epic_air1` to `1`.
- `potranquility` taq`aal emeraldshard, say elemental essences needs `mage_epic` ==6.
  - Sets `mage_epic_earth1` to `1`.
- `westwastes` a lost tomekeeper, say violet roses needs `mage_epic` ==2.
  - Gives Tome of Primal Fires (15769).

## Other flags touched along the way

- `mage_epic_air1` set to 1 at potranquility/sarhya the dawnbreeze.
- `mage_epic_causeway` set to 1 at causeway/player.
- `mage_epic_cod` set to 1 at codecay/mage trap.
- `mage_epic_dl` set to 1 at dreadlands/mage trap.
- `mage_epic_earth1` set to 1 at potranquility/taq`aal emeraldshard.
- `mage_epic_ferubi` set to 1 at ferubi/mage trap.
- `mage_epic_fire1` set to 1 at potranquility/miak the searedsoul.
- `mage_epic_hoh` set to 1 at hohonora/mage trap.
- `mage_epic_jah` set to 1 at commonlands/jahsohn aksot, commons/jahsohn aksot.
- `mage_epic_letalis` set to 1 at letalis/player.
- `mage_epic_potchest` set to 1 at potactics/player.
- `mage_epic_wal` set to 1 at butcher/walnan.
- `mage_epic_water1` set to 1 at potranquility/jurmak the undertow.
