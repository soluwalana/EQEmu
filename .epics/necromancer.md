# Necromancer — Epic Quest Walkthrough

Generated directly from quest-graph item rewards. Unresolved dependencies are marked, not inferred.

## Epic 1.0

### "Scythe of the Shadowed Soul" (20544)

<a id="epic-item-20544"></a>

1. Loot "Silver Disc" (20938) from "an azarack" (NPC 71031) in `airplane`. Drop cache: 14.2857% chance per kill.
2. Loot "Spiroc Feathers" (20782) from "an avenging gazer" (NPC 71027) in `airplane`. Drop cache: 10.626% chance per kill.
3. Kill airplane/"A Soul Carrier".
4. Spawns "Keeper of Souls" (npc:71075) via `airplane/key master#timer:87`.
5. Kill "Keeper of Souls" (NPC 71075) in `airplane` and loot "Black Silk Cape" (20783).
6. airplane/"Jzil Gsix", hand "Silver Disc" (20938) + "Spiroc Feathers" (20782) + "Black Silk Cape" (20783). Gives "Cloak of Spiroc Feathers" (1278).
    - event_trade NPC say: Very good. Now take this and leave me.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 20938, item2 = 20782, item3 = 20783}))`
7. Loot "Eye of Innoruuk" (20656) from "Innoruuk" (NPC 76007) in `hateplane`. Drop cache: 40.7296% chance per kill.
8. Loot "Slime Blood of Cazic-Thule" (20655) from "Dread" (NPC 72000) in `fearplane`. Drop cache: 10.4954% chance per kill.
9. Kill lakerathe/"A Bone Golem".
10. Spawns "a tortured soul" (npc:51144) via `lakerathe/a failed apprentice#event_death_complete`.
11. Kill "a tortured soul" (NPC 51144) in `lakerathe` and loot "Symbol of Insanity" (20648).
12. timorous/"Drendico Metalbones", hand "Symbol of Insanity" (20648). Gives "Journal of Drendico" (18086).
    - event_item NPC emote: says, 'Seek, search, turn, twist! Kazen hopes to death master truly! Read out, read in between! Talk to the pretty clouds.' Drendico turns his back to you and throws a book over his shoulder. 'Bring back book! Bring back reagents three!!' He shouts as he mumbles some more gibberish.
      - Event guard: `(plugin::check_handin(\%itemcount, 20648 => 1))`
13. timorous/"Drendico Metalbones", hand "Cloak of Spiroc Feathers" (1278) + "Eye of Innoruuk" (20656) + "Slime Blood of Cazic-Thule" (20655) + "Journal of Drendico" (18086). Gives "Prepared Reagent Box" (20653).
    - event_item NPC emote: turns to you in amazement. 'You actually did it! These are the correct components! Kazen will be most pleased. I searched the planes for almost a year and could not find all the correct components.' Drendico fiddles with the components, puts them into a box and hands it to you. 'You must have access to an army, $name. Return the components to Kazen quickly!
      - Event guard: `(plugin::check_handin(\%itemcount, 1278 => 1, 20656 => 1, 20655 => 1, 18086 => 1))`
14. lakerathe/"Kazen Fecae", hand "Prepared Reagent Box" (20653). Gives "Tome of Instruction" (18087).
    - event_item NPC emote: stares through you at the horizon, pausing as he reaches into his robes. Kazen pulls out a scythe with a shimmering black blade that seems too large to have been hidden there. As quickly and gracefully as it was displayed to you, it is returned to the void inside Kazen's robes. 'It is a creation of Miragul which was looted from his lair under the ice. Take this tome, it will be your final task for me as an apprentice.'
      - Event guard: `(plugin::check_handin(\%itemcount, 20653 => 1))`
15. airplane/"Gkzzallk", hand "Tome of Instruction" (18087). Gives "Gkzzallk in a Box" (20652).
    - event_trade NPC emote: screams as he touches the book. His body shimmers as he shrinks smaller and smaller until it's no larger than an insect. The book shimmers, shifting into the shape of a small, black box. Gkzzallk holds on to the opening of the box as he is sucked backward into it. The tiny screams are finally silenced as the box top closes.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 18087}))`
16. lakerathe/"Kazen Fecae", hand "Gkzzallk in a Box" (20652). Gives "Scythe of the Shadowed Soul" (20544).
    - event_item NPC emote: grins wildly and his eyes flare a deep red. The scythe he promised you flies through the air and into your hand. 'Enjoy your toy, I have no more need of you as a servant.'
      - Event guard: `(plugin::check_handin(\%itemcount, 20652 => 1))`

## Epic 1.5

### "Soulwhisper" (62581)

<a id="epic-item-62581"></a>

1. Spawns "Tarlang (Active)" (npc:303083) via `causeway/tarlang#hail`.
2. Kill "Tarlang (Active)" (NPC 303083) in `causeway` and loot "Tarlang's Head" (55855).
3. natimbi/"Whiahdi", hand "Tarlang's Head" (55855). Gives "Soulwhisper" (62581).
    - event_item NPC say: Take this weapon for helping me. I regret giving away a weapon of such power, but having it near me was most unsettling. Do not ask how I obtained it.
      - Event guard: `((defined($qglobals{Soulwhisper}) && ($qglobals{Soulwhisper} == 3)) && plugin::check_handin(\%itemcount, 55855 => 1))`
    - event_item NPC message: You have gained 5 ability points!

## Epic 2.0

### "Deathwhisper" (64067)

<a id="epic-item-64067"></a>

**Earlier reward routes required by this graph path:** ["Soulwhisper" (62581)](#epic-item-62581).
Revisit those instructions if another copy of a consumed item is needed.

1. Spawns "arl" (npc:336242) via `dranik/discord fluctuation#event_proximity_say`.
2. Kill "arl" (NPC 336242) in `dranik` and loot "Staff Piece Number Two" (55940).
3. Kill "gor" (NPC 336243) in `dranik` and loot "Staff Piece Number Three" (55932).
4. global/"Global Player", say "Recipe:19908". Gives "Globe of Discordant Energy" (47100).
5. natimbi/"Whiahdi", hand "Staff Piece Number Two" (55940) + "Staff Piece Number Three" (55932) + "Globe of Discordant Energy" (47100) + "Soulwhisper" (62581). Gives "Deathwhisper" (64067).
    - event_item NPC say: It is against my better judgment to rebuild this staff, but I agreed to help you, if you helped me.
      - Event guard: `(plugin::check_handin(\%itemcount, 55940 => 1, 55932 => 1, 47100 => 1, 62581 => 1))`
    - event_item NPC emote: takes the staff pieces from you and sets them down on the ground. She waves her ghostly hands over the pieces and they begin to glow. A bright, orange flame engulfs the pieces as they begin to join, forming the staff. A bone-chilling shriek fills your ears. You look down to see the staff fully formed. 'Take the staff and leave. I have done something that I should not have done this day.'
    - event_item NPC message: You have gained 10 ability points!
