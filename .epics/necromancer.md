# Necromancer

Steps taken from the quest graph only. **Broken** means the graph has no edge for that value or that item.

Flags with writes: `NecroPre`, `necro_epic`.

## 0. Prerequisites

Each list is the order you obtain that item. Later steps point here instead of repeating the chain.

### "Soulwhisper" (62581)

1. Say "Hail" to causeway/"Tarlang".
2. Spawns "Tarlang (Active)" (303083).
3. Loot "Tarlang's Head" (55855) from "Tarlang (Active)".
4. Loot "Tarlang's Head" (55855) from "Tarlang".
5. Loot "Tarlang's Head" (55855) from "Tarlang" in `causeway`.
6. natimbi/"Whiahdi", hand "Tarlang's Head" (55855). Gives "Soulwhisper" (62581).

## `NecroPre`

Values written: 1, 2.

### 1. egonis — hand 15523

Zone: `lakerathe`.

Sets `NecroPre` to `1`.

- Turn in x1: Contract of Sale (15523).
In script order:

1. Sets `NecroPre` to `1`.
2. Spawns Ronaiar Skullmoore (51155).
   - Loots Lucidem (35084).
   - Loots Versluierd Fungus (35087).
   - Loots Elaborate Binding Powder (36285).


How the items are reached:

- Contract of Sale (15523)
  - Kill qey2hh1/"A Snarling Werewolf". Spawns "Shady Bandit" (12185).
  - Loot "Contract of Sale" (15523) from "Shady Bandit".
  - Loot "Contract of Sale" (15523) from "Shady Bandit".

### 2. geboron — hand 20612

Zone: `poknowledge`.

Sets `NecroPre` to `2`.

- Needs `NecroPre` ==1.
- Turn in x1: Piece of the Staff (20612).
In script order:

1. Sets `NecroPre` to `2`.
2. Gives Piece of the Staff (20612).


How the items are reached:

- Piece of the Staff (20612)
  - Spawns "Man-eating Freshwater Shark" (51158) in `lakerathe` on event_signal.
  - Loot "Piece of the Staff" (20612) from "Man-eating Freshwater Shark".
  - Loot "Piece of the Staff" (20612) from "Man-eating Freshwater Shark".

### Steps on `NecroPre` that do not change it

- `lakerathe` egonis, say hail needs `NecroPre` ==1.
  - Spawns Ronaiar Skullmoore (51155).
  - Loots Lucidem (35084).
  - Loots Versluierd Fungus (35087).
  - Loots Elaborate Binding Powder (36285).
- `lakerathe` kazen fecae, hand 20612 needs `NecroPre` ==2.
  - Sets `Soulwhisper` to `1`.
  - Turn in Piece of the Staff (20612).
  - Gives Note to Biddliss (9831).
  - Gives Piece of the Staff (20612).

## `necro_epic`

Values written: 5, 6.

### 5. whiahdi — say locate the paladin

Zone: `natimbi`.

> I fear for you should you seek the staff, but I promised to help you. I can still hear the staff

Sets `necro_epic` to `5`.

- Needs Soulwhisper (62581).
In script order:

1. Sets `necro_epic` to `5`.


How the items are reached:

- Soulwhisper (62581)
  - Prerequisite: "Soulwhisper" (62581). See section 0.

### 6. whiahdi — hand 47100+55932+55940+62581

Zone: `natimbi`.

Sets `necro_epic` to `6`.

- Turn in x1: Staff Piece Number Two (55940).
- Turn in x1: Staff Piece Number Three (55932).
- Turn in x1: Globe of Discordant Energy (47100).
- Turn in x1: Soulwhisper (62581).
In script order:

1. Sets `necro_epic` to `6`.
2. Gives Deathwhisper (64067).


How the items are reached:

- Staff Piece Number Two (55940)
  - Say "Sanait Sanaiij Tsulum" to dranik/"Discord Fluctuation".
  - Spawns "Arl" (336242).
  - Loot "Staff Piece Number Two" (55940) from "Arl".
  - Loot "Staff Piece Number Two" (55940) from "Arlagai the Defiler".
- Staff Piece Number Three (55932)
  - Say "Sanait Sanaiij Tsulum" to dranik/"Discord Fluctuation".
  - Spawns "Gor" (336243).
  - Loot "Staff Piece Number Three" (55932) from "Gor".
  - Loot "Staff Piece Number Three" (55932) from "Gornogg the Awful".
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
- Soulwhisper (62581)
  - Prerequisite: "Soulwhisper" (62581). See section 0.

### Steps on `necro_epic` that do not change it

- `dranik` discord fluctuation, say sanait sanaiij tsulum needs `necro_epic` ==5.
  - Spawns rag (336244).
  - Spawns gor (336243).
  - Spawns arl (336242).
  - Loots Staff Piece Number Three (55932).
  - Loots Staff Piece Number Two (55940).
- `dranik` player, on loot needs `necro_epic` ==5.
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

## Other flags touched along the way

- `nec_epic_barindu` set to 1 at barindu/player.
- `nec_epic_causeway` set to 1 at causeway/player.
