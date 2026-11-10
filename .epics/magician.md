# Magician

Steps taken from the quest graph only. **Broken** means the graph has no edge for that value or that item.

Flags with writes: `mage_epic`.

## 0. Prerequisites

Shared acquisition steps appear in the first prerequisite chain that needs them. Later sections reference that chain rather than repeating it.

### "Pouch of Powdered Riftseeker Essence" (19149)

1. Loot "Gelidran Essence" (19099) from "A Gelidran Flamefreeze" (NPC 334016) in `riftseekers`. Drop cache: 8.79% chance per kill.
2. Loot "Pyrilen Essence" (19093) from "A Pyrilen Firecharmer" (NPC 334010) in `riftseekers`. Drop cache: 8.75% chance per kill.
3. draniksscar/"Iilivina", hand "Pyrilen Essence" (19093) + "Pyrilen Essence" (19093) + "Gelidran Essence" (19099) + "Gelidran Essence" (19099). Gives "Pouch of Powdered Riftseeker Essence" (19149).

### "Note from Iilivina" (19438)

1. Acquisition of "Gelidran Essence" (19099) is documented under "Pouch of Powdered Riftseeker Essence" (19149); obtain another copy if needed.
2. Acquisition of "Pyrilen Essence" (19093) is documented under "Pouch of Powdered Riftseeker Essence" (19149); obtain another copy if needed.
3. draniksscar/"Iilivina", hand "Pyrilen Essence" (19093) + "Pyrilen Essence" (19093) + "Gelidran Essence" (19099) + "Gelidran Essence" (19099). Gives "Note from Iilivina" (19438).

### "Small pouch of Riftseeker Essence" (19441)

1. Acquisition of "Note from Iilivina" (19438) is documented under "Note from Iilivina" (19438); obtain another copy if needed.
2. Acquisition of "Pouch of Powdered Riftseeker Essence" (19149) is documented under "Pouch of Powdered Riftseeker Essence" (19149); obtain another copy if needed.
3. poknowledge/"Bantil Io'Tuv", hand "Pouch of Powdered Riftseeker Essence" (19149) + "Note from Iilivina" (19438). Gives "Small pouch of Riftseeker Essence" (19441).

### "Tome of Primal Fires" (15769)

1. Loot "Journal of Magus Tvish" (15639) from "Danvi's Corpse" (NPC 179132) in `akheva`. Drop cache: 100% chance per kill.
2. poknowledge/"Bantil Io'Tuv", hand "Journal of Magus Tvish" (15639). Sets `mage_epic` to `2`.
3. westwastes/"A Lost Tomekeeper", say "Violet Roses". Requires `mage_epic` ==2. Gives "Tome of Primal Fires" (15769).
    - Dialogue with westwastes/"A Lost Tomekeeper":
      - Player: "Violet Roses"
        - NPC say: Oh? Yes. The tunips blow clockwise, or something or other. Here you go. Stay diligent. The enemy may be anyone.
        - Condition: `(e.message:findi("Violet Roses") and qglobals["mage_epic"] == "2" )`
        - Gives Tome of Primal Fires (15769).

### "Staff of Elemental Essence" (19092)

1. Acquisition of "Tome of Primal Fires" (15769) is documented under "Tome of Primal Fires" (15769); obtain another copy if needed.
2. poknowledge/"Bantil Io'Tuv", hand "Tome of Primal Fires" (15769). Sets `mage_epic` to `3`.
3. Ground spawn of "Book of Bindings and Incantations" (15772) in `charasis`.
4. poknowledge/"Bantil Io'Tuv", hand "Book of Bindings and Incantations" (15772). Sets `mage_epic` to `4`.
5. Loot "Codex of Ice and Ether" (15775) from "Grigor Rojha" in `thedeep`.
6. poknowledge/"Bantil Io'Tuv", hand "Codex of Ice and Ether" (15775). Sets `mage_epic` to `5`.
7. najena/"Akksstaff'S Minion", on event_death_complete. Sets `ask_minion_dead` to `1`.
8. najena/"Akksstaff", say "Demise". Requires `ask_minion_dead` set. Gives "Sentience of Elements" (15778).
    - Dialogue with najena/"Akksstaff":
      - Player: "Hail"
        - NPC say: How is this possible? I cannot be defeated. Spare my life and I will tell you the truth of Magi'kot's [demise].
        - Condition: `(qglobals["ask_minion_dead"] ~= nil and e.message:findi("hail"))`
      - Player: "Demise" (link: explicit mention)
        - NPC say: I am the last Council Member of the Order of the Elemental Shadows. For Centuries, we protected the true secrets behind elemental mastery, but our sect dies here with me. I chose to sit at Magi'kot's side and watch his progress, he showed more promise than anyone since Tvish. When I learned he was to receive the Orb of Mastery, I sabotaged his spell. The flaw was not his, but now people have succeeded where he failed. It doesn't matter, even with the power of the Orb and the knowledge in these tomes, Bantil will never unlock the full power of elemental mastery. You are only helping him to meet the same fate as Magi'Kot.' He then hands you the book and fades into the shadows.
        - Condition: `(qglobals["ask_minion_dead"] ~= nil and e.message:findi("demise"))`
        - Gives Sentience of Elements (15778).
      - Player: "Hail" (link: conversation sequence)
        - NPC say: What do you want?! Foolish , I am in no mood to treat with beggars. I have half a mind to turn my pet here loose on you! Well, don't keep me waiting, state your business or be off with you!
        - Condition: `(e.message:findi("hail"))`
      - Player: "Wish To Hear More" (link: conversation sequence)
        - NPC say: Then bring me the torn pages of Mastery, there are four pages that can be found upon the women In this keep, though have a care, Najena's followers guard her treasures carefully, and delight in punishing trespassers.
        - Condition: `(e.message:findi("wish to hear more"))`
      - Player: "Bantil Sent Me" (link: conversation sequence)
        - NPC say: My, you are persistent aren't you? Well you have found more trouble than you expected, now haven't you? Prepare to witness the true power of a master of the elements!
        - Condition: `(e.message:findi("bantil sent me") and qglobals["mage_epic"] ~= nil and qglobals["mage_epic"] >= "5")`
        - Spawns NPC 44108.
9. poknowledge/"Bantil Io'Tuv", hand "Sentience of Elements" (15778). Sets `mage_epic` to `6`.
10. potranquility/"Jurmak The Undertow", say "Elemental Essences". Sets `mage_epic_water1` to `1`.
    - Dialogue with potranquility/"Jurmak The Undertow":
      - Player: "Hail"
        - NPC say: The Elders say that you are now allowed to enter the Plane of Water. I shall allow you to enter, but I will not be responsible for whatever fate may befall you upon entry to this greater elemental plane.
        - Condition: `(($text=~/hail/i) && ($pop_tactics_ralloz == 1))`
      - Player: "Hail" (link: conversation sequence)
        - NPC say: Well met I am keeper of the Portal to the Plane of Water.
        - Condition: `($text=~/hail/i)`
      - Player: "Elemental Essences" (link: conversation sequence)
        - NPC say: Oh? The Elemental Essence of water? That is what you mean, yes? Consider yourself fortunate, I know the location of the Essence. It has spent quite some time living as a minor god to the othmir.
        - Condition: `(($text=~/elemental essences/i) && defined($qglobals{mage_epic}) && ($qglobals{mage_epic}==6))`
        - Sets `mage_epic_water1` to `1`.
11. Loot "Ice Burrower Meat" (19022) from "An Ice Burrower" in `westwastes`.
12. Hand "Ice Burrower Meat" (19022) + "Ice Burrower Meat" (19022) + "Ice Burrower Meat" (19022) + "Ice Burrower Meat" (19022) to cobaltscar/"High Priest Margle". Spawns "Tiknonmanin" (117094). Loot "Elemental Essence of Water" (19086) from "Tiknonmanin".
13. Spawns "Elemental Essence of Fire" (214127) in `potactics` on event_waypoint_arrive.
14. Loot "Elemental Essence of Fire" (16807) from "Elemental Essence of Fire".
15. potranquility/"Sarhya The Dawnbreeze", say "Elemental Essences". Sets `mage_epic_air1` to `1`.
    - Dialogue with potranquility/"Sarhya The Dawnbreeze":
      - Player: "Hail"
        - NPC say: It appears that you are ready to travel into the Elemental Planes. Beware many of the gods there have set up wards to protect them against assaults. Most I cannot speak about; however I do have information on the Circle of Protection that guards Xegony, in her [Plane of Air].
        - Condition: `(($text=~/hail/i) && ($pop_tactics_ralloz == 1))`
      - Player: "Hail" (link: conversation sequence)
        - NPC say: Well met I am keeper of the Portal to the [Plane of Air].
        - Condition: `($text=~/hail/i)`
      - Player: "Plane Of Air" (link: explicit mention)
        - NPC say: Xegony has created four avatars, each one embodies a different aspect of her power, and each of these avatars was created with a portion of her very essence. The story goes, the one who possesses each of these essences may create a key to break Xegony's ward and enter into her inner sanctum. I don't know the truth behind this, as I have neither the power, nor the desire to challenge the Avatars myself. I have fashioned this, which I believe will form the four essences into a key.
        - Condition: `($text=~/plane of air/i && ($pop_tactics_ralloz == 1))`
        - Gives Pouch of Swirling Winds (17888).
      - Player: "Plane Of Air" (link: explicit mention)
        - Prompted by player input: "Hail"
        - NPC say: The Elemental Planes are not for idle exploration. Return to me when you have a reason to enter and I will consider opening the portal for you.
        - Condition: `($text=~/plane of air/i)`
      - Player: "Elemental Essences" (link: conversation sequence)
        - NPC say: You seek the elemental essences? It has been a very long time since I've heard them spoke of. I am afraid I cannot be of much help, except to tell you it often enjoys to whistle through valleys and canyons. I fear it may not even reside in this realm any longer.
        - Condition: `(($text=~/elemental essences/i) && defined($qglobals{mage_epic}) && ($qglobals{mage_epic}==6))`
        - Sets `mage_epic_air1` to `1`.
16. Spawns "Elemental Essence of Air" (303100) in `causeway` on enter.
17. Loot "Elemental Essence of Air" (16773) from "Elemental Essence of Air".
18. potranquility/"Taq'Aal Emeraldshard", say "Elemental Essences". Sets `mage_epic_earth1` to `1`.
19. Spawns "Elemental Essence of Earth" (169127) in `letalis` on enter.
20. Loot "Elemental Essence of Earth" (19087) from "Elemental Essence of Earth".
21. poknowledge/"Bantil Io'Tuv", hand "Elemental Essence of Air" (16773) + "Elemental Essence of Fire" (16807) + "Elemental Essence of Water" (19086) + "Elemental Essence of Earth" (19087). Requires `mage_epic` ==6. Gives "Staff of Elemental Essence" (19092).

### "Sentience of Elements" (15778)

1. Acquisition of "Sentience of Elements" (15778) is documented under "Staff of Elemental Essence" (19092); obtain another copy if needed.

## `mage_epic` 1.5

Values written: 1, 2, 3, 4, 5, 6, 7.

1. poknowledge/"Bantil Io'Tuv", say "Hail". Sets `mage_epic` to `1`.
    - Requires `mage_epic` unset.

Alternative or repeat transition to `mage_epic` = `1` (not an additional required stage).

1. poknowledge/"Bantil Io'Tuv", hand "Captured Earthquake Elemental" (11998) + "Captured Wildfire Elemental" (14941) + "Captured Monsoon Elemental" (14960) + "Captured Tsunami Elemental" (14966). Sets `mage_epic` to `1`.
    - Hand in x1: "Captured Monsoon Elemental" (14960).
    - Hand in x1: "Captured Earthquake Elemental" (11998).
    - Hand in x1: "Captured Wildfire Elemental" (14941).
    - Hand in x1: "Captured Tsunami Elemental" (14966).
    - Loot "Captured Monsoon Elemental" (14960) from "Swirling Monsoon Elemental" in `postorms`.
    - Loot "Captured Earthquake Elemental" (11998) from "Trembling Earthquake Elemental" in `thegrey`.
    - Loot "Captured Wildfire Elemental" (14941) from "Raging Wildfire Elemental" in `shadeweaver`.
    - Loot "Captured Tsunami Elemental" (14966) from "Ravaging Tsunami Elemental" in `sirens`.

2. poknowledge/"Bantil Io'Tuv", hand "Journal of Magus Tvish" (15639). Sets `mage_epic` to `2`.
    - Hand in x1: "Journal of Magus Tvish" (15639).
    - Loot "Journal of Magus Tvish" (15639) from "Danvi's Corpse" (NPC 179132) in `akheva`. Drop cache: 100% chance per kill.

3. poknowledge/"Bantil Io'Tuv", hand "Tome of Primal Fires" (15769). Sets `mage_epic` to `3`.
    - Hand in x1: "Tome of Primal Fires" (15769).
    - Prerequisite: "Tome of Primal Fires" (15769). See section 0.

4. poknowledge/"Bantil Io'Tuv", hand "Book of Bindings and Incantations" (15772). Sets `mage_epic` to `4`.
    - Requires `mage_epic` ==3.
    - Hand in x1: "Book of Bindings and Incantations" (15772).
    - Ground spawn of "Book of Bindings and Incantations" (15772) in `charasis`.

5. poknowledge/"Bantil Io'Tuv", hand "Codex of Ice and Ether" (15775). Sets `mage_epic` to `5`.
    - Requires `mage_epic` ==4.
    - Hand in x1: "Codex of Ice and Ether" (15775).
    - Loot "Codex of Ice and Ether" (15775) from "Grigor Rojha" in `thedeep`.

6. poknowledge/"Bantil Io'Tuv", hand "Sentience of Elements" (15778). Sets `mage_epic` to `6`.
    - Requires `mage_epic` ==5.
    - Hand in x1: "Sentience of Elements" (15778).
    - Prerequisite: "Sentience of Elements" (15778). See section 0.

7. poknowledge/"Bantil Io'Tuv", hand "Elemental Essence of Air" (16773) + "Elemental Essence of Fire" (16807) + "Elemental Essence of Water" (19086) + "Elemental Essence of Earth" (19087). Sets `mage_epic` to `7`.
    - Requires `mage_epic` ==6.
    - Hand in x1: "Elemental Essence of Water" (19086).
    - Hand in x1: "Elemental Essence of Fire" (16807).
    - Hand in x1: "Elemental Essence of Air" (16773).
    - Hand in x1: "Elemental Essence of Earth" (19087).
    - Hand "Ice Burrower Meat" (19022) + "Ice Burrower Meat" (19022) + "Ice Burrower Meat" (19022) + "Ice Burrower Meat" (19022) to cobaltscar/"High Priest Margle". Spawns "Tiknonmanin" (117094). Loot "Elemental Essence of Water" (19086) from "Tiknonmanin".
    - Spawns "Elemental Essence of Fire" (214127) in `potactics` on event_waypoint_arrive.
    - Loot "Elemental Essence of Fire" (16807) from "Elemental Essence of Fire".
    - Spawns "Elemental Essence of Air" (303100) in `causeway` on enter.
    - Loot "Elemental Essence of Air" (16773) from "Elemental Essence of Air".
    - Spawns "Elemental Essence of Earth" (169127) in `letalis` on enter.
    - Loot "Elemental Essence of Earth" (19087) from "Elemental Essence of Earth".
    - Gives "Staff of Elemental Essence" (19092).

### Steps on `mage_epic` that do not change it

- `draniksscar` iilivina, hand 19092 needs `mage_epic` ==7.
  - Turn in Staff of Elemental Essence (19092).
  - Gives Staff of Elemental Essence (19092).
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
- `hohonora` player, on loot needs `mage_epic` set.
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

## `mage_epic` 2.0

Values written: 8, 9, 10, 11.

8. draniksscar/"Iilivina", hand "Staff of Elemental Essence" (19092). Sets `mage_epic` to `8`.
    - Requires `mage_epic` ==7.
    - Hand in x1: "Staff of Elemental Essence" (19092).
    - Prerequisite: "Staff of Elemental Essence" (19092). See section 0.
    - Gives "Staff of Elemental Essence" (19092).
    - Dialogue with draniksscar/"Iilivina":
      - Player: "Hail"
        - NPC say: Hello again. So, you are looking for the Primal Elemental essences? That has a nice ring to it Transon has always had a penchant for the dramatic. I do not believe that you will find these beings in Discord however, if they exist at all. I do believe that your staff will resonate when you approach the creatures, so travel the world you know. Elementals tend to gravitate to areas that reflect their element best, I don't see why the [Primals] would behave any differently.
          - Reply guard: `(qglobals["mage_epic"] ~=nil and tonumber(qglobals["mage_epic"]) >= 9)`
        - NPC say: The magic here is quite unique. I am thrilled I've had the opportunity to study it.
          - Reply guard: ``
        - Condition: `(e.message:findi("hail"))`
      - Player: "Bantil"
        - NPC say: Yes, Bantil told me you would be coming. Perhaps we can help each other. There are two tribes of elemental beings here. They have an unprecedented ability to channel elemental energy. I have yet to see one with my own eyes, but they may just contain [power] that will help you unleash the staff's true power.
        - Condition: `(qglobals["mage_epic"] >= "8" and e.message:findi("bantil"))`
      - Player: "Power" (link: explicit mention)
        - NPC say: They use the elements in a way we have yet to understand. I suspect something in their essence that allows them to tap into the elements in a different manner than we understand. If my suspicions are true, these creatures should leave behind a small portion of their essence, when their spirits leave their bodies. If you find anything like that, bring it to me. They may be rather small, so bring me two from each type for good measure.
        - Condition: `(qglobals["mage_epic"] >= "8" and e.message:findi("power"))`
      - Player: "Primals" (link: explicit mention)
        - Prompted by player input: "Hail"
        - NPC say: Were I to venture a guess, I'd say look for Chaos near the ruins of a fallen empire, as order would tend to oppose chaos, I would look for the Order elemental near the ranks of a well regimented army, probably an ancient army, it is a creature of prestige. The Spirit elemental would find someplace where death and decay have a strong foothold. The Body Elemental may be the most elusive, as there is life everywhere. I would assume that its strong ties with this realm would pull it to a place where there are Muramites. When you find them, bring their remains to me and I'll see what else needs to be done.
        - Condition: `(qglobals["mage_epic"] >= "9" and e.message:findi("Primals"))`
        - Sets `mage_epic` to `10`.

9. poknowledge/"Bantil Io'Tuv", hand "Pouch of Powdered Riftseeker Essence" (19149) + "Note from Iilivina" (19438). Sets `mage_epic` to `9`.
    - Hand in x1: "Note from Iilivina" (19438).
    - Hand in x1: "Pouch of Powdered Riftseeker Essence" (19149).
    - Prerequisite: "Note from Iilivina" (19438). See section 0.
    - Prerequisite: "Pouch of Powdered Riftseeker Essence" (19149). See section 0.
    - Gives "Small pouch of Riftseeker Essence" (19441).

Alternative or repeat transition to `mage_epic` = `9` (not an additional required stage).

9. twilight/"Vornol Transon", hand "Small pouch of Riftseeker Essence" (19441). Sets `mage_epic` to `9`.
    - Hand in x1: "Small pouch of Riftseeker Essence" (19441).
    - Prerequisite: "Small pouch of Riftseeker Essence" (19441). See section 0.
    - Dialogue with twilight/"Vornol Transon":
      - Player: "Hail"
        - NPC emote: pauses for a second staring off into the distance. 'Ah welcome friend. I am Vornol, a summoner of sorts, and master of this tower.'
        - NPC say: Most excellent what I have is some armor, if you will do few errands for me it is yours. The pieces I have are the cap, robe, sleeves, pants, shawl, and bracer. My apprentice, the lady Galdara, has the rest. Just ask her about armor and she will tell you what you need to do.
        - Condition: `($text =~ /hail/i)`
      - Player: "Cap" (link: explicit mention)
        - NPC say: For the cap you will have to bring back to me a sun jewel, a fire idol, a fire marked scroll and a runed ring of fire.
        - Condition: `($text =~ /cap/i)`
      - Player: "Robe" (link: explicit mention)
        - Prompted by player input: "Hail"
        - NPC say: For the robe you will have to bring back to me a moon jewel, a vial of purified fire, a vial of purified water, and a vial of purified air.
        - Condition: `($text =~ /robe/i)`
      - Player: "Sleeves" (link: explicit mention)
        - Prompted by player input: "Hail"
        - NPC say: For the sleeves you will have to bring back to me a star jewel, an air idol, an air marked scroll and a runed ring of air.
        - Condition: `($text =~ /sleeves/i)`
      - Player: "Pants" (link: explicit mention)
        - Prompted by player input: "Hail"
        - NPC say: For the pants you will have to bring back to me a cloud jewel, an earth idol, an earth marked scroll, and a runed ring of earth.
        - Condition: `($text =~ /pants/i)`
      - Player: "Shawl" (link: explicit mention)
        - Prompted by player input: "Hail"
        - NPC say: For the shawl you will have to bring back to me a sky jewel, a talisman of burning earth, and a vial of purified earth.
        - Condition: `($text =~ /shawl/i)`
      - Player: "Bracer" (link: explicit mention)
        - Prompted by player input: "Hail"
        - NPC say: For the bracer you will have to bring back to me a meteor jewel, talisman of moisture, and a vial of aqua waters.
        - Condition: `($text =~ /bracer/i)`

10. draniksscar/"Iilivina", say "Primals". Sets `mage_epic` to `10`.
    - Requires `mage_epic` >=9.

11. draniksscar/"Iilivina", hand "Element of Chaos" (19444) + "Element of Body" (19447) + "Element of Spirit" (19544) + "Element of Order" (19547). Sets `mage_epic` to `11`.
    - Hand in x1: "Element of Order" (19547).
    - Hand in x1: "Element of Body" (19447).
    - Hand in x1: "Element of Chaos" (19444).
    - Hand in x1: "Element of Spirit" (19544).
    - Spawns "Order Elemental" (211057) in `hohonora` on enter.
    - Loot "Element of Order" (19547) from "Order Elemental".
    - Spawns "Body Elemental" (284105) in `ferubi` on enter.
    - Loot "Element of Body" (19447) from "Body Elemental".
    - Spawns "Chaos Elemental" (86174) in `dreadlands` on enter.
    - Loot "Element of Chaos" (19444) from "Chaos Elemental".
    - Spawns "Spirit Elemental" (200060) in `codecay` on enter.
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
- `dreadlands` player, on loot needs `mage_epic` ==10.
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
- `poknowledge` bantil io`tuv, hand 19092+47100 needs `mage_epic` ==11.
  - Turn in Globe of Discordant Energy (47100).
  - Turn in Staff of Elemental Essence (19092).
  - Gives Focus of Primal Elements (19839).

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
