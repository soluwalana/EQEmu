# Shadow Knight

Steps taken from the quest graph only. **Broken** means the graph has no edge for that value or that item.

Flags with writes: `shadowknight_pre`, `shadowknight_epic`.

## 0. Prerequisites

Shared acquisition steps appear in the first prerequisite chain that needs them. Later sections reference that chain rather than repeating it.

### "Sheathed Innoruuk's Voice" (11407)

1. dulak/"Ritald", say "Hail". Sets `shadowknight_pre` to `1`.
2. Loot "Ancient Flamberge of Hatred" (55902) from "Captain Varns" in `dulak`.
3. Loot "Essence of Hate" (21870) from "Mistress of Malevolence" in `hateplaneb`.
4. Loot "Essence of Hate" (21870) from "Overlord R'Gahbsa" in `hateplaneb`.
5. Loot "Stormborn Phylactery" (21782) from "Olidan" in `postorms`.
6. dulak/"Ritald", hand "Stormborn Phylactery" (21782) + "Essence of Hate" (21870) + "Ancient Flamberge of Hatred" (55902). Sets `shadowknight_pre` to `2`.
7. poknowledge/"Sienn Kastane", say "Hail". Sets `shadowknight_epic` to `1`.
8. Loot "Gelatinous Murkglider Egg" (55900) from "Murkglider Breeder" in `dranik`.
9. poknowledge/"Grand Librarian Maelin", hand "Gelatinous Murkglider Egg" (55900). Requires `shadowknight_epic` ==1. Gives "The Silent Gods" (20520).
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
10. poknowledge/"Sienn Kastane", hand "The Silent Gods" (20520). Sets `shadowknight_epic` to `2`.
11. Summon "Collapsible Sewing Kit" (17165) by casting "Unfold Sewing Kit".
12. Loot "Eye of the Dark God" (21675) from "Amygdalan warrior" (NPC 72015) in `fearplane`. Drop cache: 18.32% chance per kill.
13. Loot "Gloom Nightmare Hide" (20622) from "A Gloom Nightmare" in `ponightmare`.
14. Loot "Lock of Blessed Unicorn Hair" (21496) from "A Rolling Plains Steed" (NPC 127084) in `growthplane`. Drop cache: 11% chance per kill.
15. Combine in "Collapsible Sewing Kit" (17165): "Eye of the Dark God" (21675), "Gloom Nightmare Hide" (20622), "Lock of Blessed Unicorn Hair" (21496). Produces "Sheath of Darktidings" (20426). Requires Tailoring 100. Trivial at 15. The combine does not fail.
16. poknowledge/"Sienn Kastane", hand "Sheath of Darktidings" (20426). Sets `shadowknight_epic` to `3`.
17. Loot "Fraga's Parchment" (23492) from "Fraga" in `povalor`.
18. poknowledge/"Sienn Kastane", hand "Fraga's Parchment" (23492). Sets `shadowknight_epic` to `4`.
19. Loot "Wailing Sister Blood" (20497) from "The Wailing Sister" in `ponightmare`.
20. Loot "Wailing Rune" (19025) from "The Wailing Sister" in `ponightmare`.
21. poknowledge/"Sienn Kastane", hand "Wailing Rune" (19025) + "Wailing Sister Blood" (20497). Requires `shadowknight_epic` ==4. Gives "Sheathed Innoruuk's Voice" (11407).

### "The Silent Gods" (20520)

1. Acquisition of "The Silent Gods" (20520) is documented under "Sheathed Innoruuk's Voice" (11407); obtain another copy if needed.

### "Sheathed Innoruuk's Voice" (22199)

1. Acquisition of "Wailing Sister Blood" (20497) is documented under "Sheathed Innoruuk's Voice" (11407); obtain another copy if needed.
2. Acquisition of "Wailing Rune" (19025) is documented under "Sheathed Innoruuk's Voice" (11407); obtain another copy if needed.
3. poknowledge/"Sienn Kastane", hand "Wailing Rune" (19025) + "Wailing Sister Blood" (20497). Sets `shadowknight_epic` to `5`.
4. Acquisition of "Sheathed Innoruuk's Voice" (11407) is documented under "Sheathed Innoruuk's Voice" (11407); obtain another copy if needed.
5. poknowledge/"Gilina Yilzior", hand "Sheathed Innoruuk's Voice" (11407). Sets `shadowknight_epic` to `6`.
6. Loot "Skurza's Head" (20899) from "Skurza Slicekutt" in `swampofnohope`.
7. Loot "Silithis's Head" (16813) from "Silithis Sisnta" in `timorous`.
8. Loot "Gubblegrot's Head" (16793) from "Gubblegrot Smashfist" in `oceanoftears`.
9. Loot "Gubblegrot's Head" (16793) from "Gubblegrot Smashfist" in `oot`.
10. Loot "Giligatabbus's Head" (20079) from "Giligatabbus Igglebix" in `iceclad`.
11. poknowledge/"Gilina Yilzior", hand "Gubblegrot's Head" (16793) + "Silithis's Head" (16813) + "Giligatabbus's Head" (20079) + "Skurza's Head" (20899). Requires `shadowknight_epic` ==6. Gives "Sheathed Innoruuk's Voice" (22199).

### "Innoruuk's Voice" (22944)

1. Acquisition of "Ancient Flamberge of Hatred" (55902) is documented under "Sheathed Innoruuk's Voice" (11407); obtain another copy if needed.
2. Acquisition of "Essence of Hate" (21870) is documented under "Sheathed Innoruuk's Voice" (11407); obtain another copy if needed.
3. Acquisition of "Stormborn Phylactery" (21782) is documented under "Sheathed Innoruuk's Voice" (11407); obtain another copy if needed.
4. dulak/"Ritald", hand "Stormborn Phylactery" (21782) + "Essence of Hate" (21870) + "Ancient Flamberge of Hatred" (55902). Requires `shadowknight_pre` ==1. Gives "Innoruuk's Voice" (22944).

### "Innoruuk's Voice" (50003)

1. Acquisition of "Skurza's Head" (20899) is documented under "Sheathed Innoruuk's Voice" (22199); obtain another copy if needed.
2. Acquisition of "Silithis's Head" (16813) is documented under "Sheathed Innoruuk's Voice" (22199); obtain another copy if needed.
3. Acquisition of "Gubblegrot's Head" (16793) is documented under "Sheathed Innoruuk's Voice" (22199); obtain another copy if needed.
4. Acquisition of "Giligatabbus's Head" (20079) is documented under "Sheathed Innoruuk's Voice" (22199); obtain another copy if needed.
5. poknowledge/"Gilina Yilzior", hand "Gubblegrot's Head" (16793) + "Silithis's Head" (16813) + "Giligatabbus's Head" (20079) + "Skurza's Head" (20899). Sets `shadowknight_epic` to `7`.
6. Say "Hail" to kithicor/"Tarnamil".
7. Spawns "Uglib Gaibido" (20293).
8. Loot "Paladin Blood Sample" (20904) from "Uglib Gaibido".
9. Alternative: Loot "Paladin Blood Sample" (20904) from "Tilminos Farondi" (NPC 20298) in `kithicor`; trigger: kithicor/"Tarnamil", say "Hail".
10. Alternative: Loot "Paladin Blood Sample" (20904) from "Valinda Ergington" (NPC 20296) in `kithicor`; trigger: kithicor/"Tarnamil", say "Hail".
11. Acquisition of "Sheathed Innoruuk's Voice" (22199) is documented under "Sheathed Innoruuk's Voice" (22199); obtain another copy if needed.
12. poknowledge/"Gilina Yilzior", hand "Paladin Blood Sample" (20904) + "Paladin Blood Sample" (20904) + "Paladin Blood Sample" (20904) + "Sheathed Innoruuk's Voice" (22199). Sets `shadowknight_epic` to `8`.
13. Loot "Sir Elmonious's Holy Symbol" (55901) from "Sir Elmonious Falmont" in `westwastes`.
14. poknowledge/"Gilina Yilzior", hand "Sir Elmonious's Holy Symbol" (55901). Requires `shadowknight_epic` ==8. Gives "Innoruuk's Voice" (50003).

### "Lhranc's Earthly Anchor" (24584)

1. poknowledge/"Gilina Yilzior", say "Vision". Sets `shadowknight_epic` to `9`.
2. Loot "Kilidna's Head" (19098) from "Kilidna" in `citymist`.
3. poknowledge/"Gilina Yilzior", hand "Kilidna's Head" (19098). Sets `shadowknight_epic` to `10`.
4. Loot "Lhranc's Corroded Bracer" (24612) from "A Mortiferous Golem" in `charasis`.
5. Kill citymist/"A Black Reaver". Spawns "A Black Reaver" (90004).
6. Loot "Lhranc's Pendant" (23489) from "A Black Reaver".
7. Alternative: Loot "Lhranc's Pendant" (23489) from "A Black Reaver" (NPC 90005) in `citymist`; trigger: citymist/"A Black Reaver", on event_death_complete.
8. Alternative: Loot "Lhranc's Pendant" (23489) from "A Black Reaver" (NPC 90192) in `citymist`; trigger: citymist/"A Black Reaver", on event_death_complete.
9. Loot "Lhranc's Ring" (24632) from "Risen Corporal" (NPC 20107) in `kithicor`. Drop cache: 19.56% chance per kill.
10. poknowledge/"Gilina Yilzior", hand "Lhranc's Pendant" (23489) + "Lhranc's Corroded Bracer" (24612) + "Lhranc's Ring" (24632). Requires `shadowknight_epic` ==10. Gives "Lhranc's Earthly Anchor" (24584).

### "Sheath of Darktidings" (20426)

1. Acquisition of "Sheath of Darktidings" (20426) is documented under "Sheathed Innoruuk's Voice" (11407); obtain another copy if needed.

## `shadowknight_pre`

Values written: 1, 2.

1. dulak/"Ritald", say "Hail". Sets `shadowknight_pre` to `1`.
    - Requires `shadowknight_pre` unset.
    - Dialogue with dulak/"Ritald":
      - Player: "Hail"
        - NPC say: Greetings, dark one. Do you feel it? I am sure you do. Innoruuk's voice is so distant now. His voice is merely a whisper. This disturbs me greatly. How will the evil ones do their master's bidding without his dark guidance? I fear the end is almost near for true champions of darkness such as yourself. We cannot let that happen! I believe I know of a way to slow down the diminishing of our master's voice. There is a sword of great evil. It is however not of this world. I believe I can summon it to this plane of existence, but I will need several items first. Will you [take on this task]? Your future and the future of all our dark brethren depends on obtaining this sword!
        - Condition: `(e.other:Class() == "Shadow Knight")`
        - Condition: `(e.message:findi("hail") and qglobals["shadowknight_pre"] == nil)`
        - Sets `shadowknight_pre` to `1`.
      - Player: "Take On This Task" (link: explicit mention)
        - NPC say: Excellent. There is no time to waste. The first item I need is an ancient flamberge of hatred. I believe a trollish pirate named, Captain Varns, here in Dulak's Harbor is in possession of one. Destroy him and return this item to me. The second item is an essence of hate. You should be able to find such an essence in the Plane of Hate. The last item I need is a stormborn phylactery. You should be able to find one in the Plane of Storms. When you have all these items, hand them to me so that I may begin the summoning of the sword.
        - Condition: `(e.other:Class() == "Shadow Knight")`
        - Condition: `(e.message:findi("take on this task") and qglobals["shadowknight_pre"] == "1")`
      - Player: "Have Done It" (link: external event mention)
        - Prompted by `event_trade`:
          - NPC say: I [have done it]!
          - Event guard: `qglobals["shadowknight_pre"] == "1" and item_lib.check_turn_in(e.trade, {item1 = 55902, item2 = 21870, item3 = 21782})`
        - NPC say: This sword known as Innoruuk's Voice emanates great evil. It should help to generate enough evil to sustain the mysterious powers that make one a shadowknight. It is not at full power yet however. I am now trusting you to take this sword and help to recover its full power. You will be its new champion. Take it to Sienn Kastane in the Plane of Knowledge. I believe she should be able to help you with returning the sword to its full power.
        - Condition: `(e.other:Class() == "Shadow Knight")`
        - Condition: `(e.message:findi("have done it") and e.other:HasItem(22944))`

2. dulak/"Ritald", hand "Stormborn Phylactery" (21782) + "Essence of Hate" (21870) + "Ancient Flamberge of Hatred" (55902). Sets `shadowknight_pre` to `2`.
    - Requires `shadowknight_pre` ==1.
    - Hand in x1: "Ancient Flamberge of Hatred" (55902).
    - Hand in x1: "Essence of Hate" (21870).
    - Hand in x1: "Stormborn Phylactery" (21782).
    - Loot "Ancient Flamberge of Hatred" (55902) from "Captain Varns" in `dulak`.
    - Loot "Essence of Hate" (21870) from "Mistress of Malevolence" in `hateplaneb`.
    - Loot "Essence of Hate" (21870) from "Overlord R'Gahbsa" in `hateplaneb`.
    - Loot "Stormborn Phylactery" (21782) from "Olidan" in `postorms`.
    - Gives "Innoruuk's Voice" (22944).

### Steps on `shadowknight_pre` that do not change it

- `poknowledge` sienn kastane, say hail needs `shadowknight_pre` ==2.
  - Sets `shadowknight_epic` to `1`.

## `shadowknight_epic`

Values written: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12.

1. poknowledge/"Sienn Kastane", say "Hail". Sets `shadowknight_epic` to `1`.
    - Requires `shadowknight_epic` unset.
    - Requires `shadowknight_pre` ==2.
    - Dialogue with poknowledge/"Sienn Kastane":
      - Player: "Hail"
        - NPC say: You. You are the one I have seen in my visions.' Sienn removes a dark blade from a scabbard. I have just obtained this sword from one of my apprentices. This blade may be the key to the very existence of the shadowknight. Are you familiar with what has [been transpiring]?
          - Reply guard: `(qglobals["shadowknight_epic"] == "1")`
        - Condition: `(e.other:Class() == "Shadow Knight")`
        - Condition: `(e.message:findi("hail"))`
        - Sets `shadowknight_epic` to `1`.
      - Player: "Transpiring" (link: explicit mention)
        - NPC emote: places her hands upon your forehead. A gravelly voice that is clearly not Sienn's fills your mind.
        - NPC message: Do you feel it? I am sure you do. Innoruuk's voice is so distant now. His voice is merely a whisper. This disturbs me greatly. How will the evil ones do their master's bidding without his dark guidance? I fear the end is almost near for true champions of darkness such as yourself. We cannot let that happen! I believe I know of a way to slow down the diminishing of our master's voice. There is a sword of great evil. It is however not of this world. I believe I can summon it to this plane of existence, but I will need several [items] first. . .' The voice ends. 'That was the voice of Ritald, a luggald in the service of the dark lord, Innoruuk.
        - Condition: `(e.other:Class() == "Shadow Knight")`
        - Condition: `(e.message:findi("transpiring") and qglobals["shadowknight_epic"] == "1")`
      - Player: "Items" (link: explicit mention)
        - NPC say: Your first task is to find me a tome. The sword has told me of a tome that details its history. I do not know where this tome might be, but I suggest you talk to Grand Librarian Maelin here in the Plane of Knowledge. He may have more information of this tome. When you find it, return it to me.
        - Condition: `(e.other:Class() == "Shadow Knight")`
        - Condition: `(e.message:findi("items") and qglobals["shadowknight_epic"] == "1")`

    - Subquest `shadowknight_pre` documented earlier.
Alternative or repeat transition to `shadowknight_epic` = `1` (not an additional required stage).

1. poknowledge/"Sienn Kastane", hand "Innoruuk's Voice" (22944). Sets `shadowknight_epic` to `1`.
    - Requires `shadowknight_epic` unset.
    - Hand in x1: "Innoruuk's Voice" (22944).
    - Prerequisite: "Innoruuk's Voice" (22944). See section 0.

2. poknowledge/"Sienn Kastane", hand "The Silent Gods" (20520). Sets `shadowknight_epic` to `2`.
    - Requires `shadowknight_epic` ==1.
    - Hand in x1: "The Silent Gods" (20520).
    - Prerequisite: "The Silent Gods" (20520). See section 0.

3. poknowledge/"Sienn Kastane", hand "Sheath of Darktidings" (20426). Sets `shadowknight_epic` to `3`.
    - Requires `shadowknight_epic` ==2.
    - Hand in x1: "Sheath of Darktidings" (20426).
    - Prerequisite: "Sheath of Darktidings" (20426). See section 0.

4. poknowledge/"Sienn Kastane", hand "Fraga's Parchment" (23492). Sets `shadowknight_epic` to `4`.
    - Requires `shadowknight_epic` ==3.
    - Hand in x1: "Fraga's Parchment" (23492).
    - Loot "Fraga's Parchment" (23492) from "Fraga" in `povalor`.

5. poknowledge/"Sienn Kastane", hand "Wailing Rune" (19025) + "Wailing Sister Blood" (20497). Sets `shadowknight_epic` to `5`.
    - Requires `shadowknight_epic` ==4.
    - Hand in x1: "Wailing Sister Blood" (20497).
    - Hand in x1: "Wailing Rune" (19025).
    - Loot "Wailing Sister Blood" (20497) from "The Wailing Sister" in `ponightmare`.
    - Loot "Wailing Rune" (19025) from "The Wailing Sister" in `ponightmare`.
    - Gives "Sheathed Innoruuk's Voice" (11407).

6. poknowledge/"Gilina Yilzior", hand "Sheathed Innoruuk's Voice" (11407). Sets `shadowknight_epic` to `6`.
    - Requires `shadowknight_epic` ==5.
    - Hand in x1: "Sheathed Innoruuk's Voice" (11407).
    - Prerequisite: "Sheathed Innoruuk's Voice" (11407). See section 0.
    - Dialogue with poknowledge/"Gilina Yilzior":
      - Player: "Vision" (link: external event mention)
        - Prompted by `event_trade`:
          - NPC say: You have performed well. The blade is yours to wield now, champion. You may be on your way, or stay to hear about a [vision] I recently had.
          - Event guard: `(qglobals["shadowknight_epic"] == "8" and item_lib.check_turn_in(e.trade, {item1 = 55901}))`
        - NPC say: My recent vision was of Lhranc. Perhaps you remember him, perhaps not. In any case, his spirit has returned from the dead. He now seeks revenge on those who killed him. There is something sinister behind his return. What exactly is going on, I do not know at this time, but I fear the worst. You must find Lhranc and [destroy] him.
        - Condition: `(e.other:Class() == "Shadow Knight")`
        - Condition: `(e.message:findi("vision") and e.other:HasItem(50003))`
        - Sets `shadowknight_epic` to `9`.
      - Player: "Destroy" (link: explicit mention)
        - NPC say: 'I sent a servant of mine named, Kilidna to the City of Mist to investigate Lhranc's reappearance but he has not returned. Go to the City of Mist and see if you can find him. Return to me if you find anything.
        - Condition: `(e.other:Class() == "Shadow Knight")`
        - Condition: `(e.message:findi("destroy") and qglobals["shadowknight_epic"] == "9")`
      - Player: "Powerful Beings" (link: external event mention)
        - Prompted by `event_trade`:
          - NPC say: takes the head from you and holds it by the hair. Gilina casts a small spell and the head springs to life. 'Talk, Kilidna. What has happened to you?' Kilidna's head begins to sob. 'I am sorry, master. I was corrupted by evil magic! Now look at me! I dare say I will not be able to finish my studies any time soon.' Gilina scowls, 'What did you find out while in the city of mist? Tell me now!' 'Well master, it seems that when Innoruuk's Voice was summoned to this plane, it drew the attention of many [powerful beings].'
          - Event guard: `(qglobals["shadowknight_epic"] == "9" and item_lib.check_turn_in(e.trade, {item1 = 19098}))`
        - NPC say: Yes, what powerful beings? Out with it, head!' 'Well, master, one of these powerful beings has resurrected Lhranc from the dead! When I confronted him, he turned me into a mindless zombie! I overheard Lhranc talking about recovering the sword for himself. You are both in great danger! Lhranc cannot be defeated in his current form and he will surely be coming for the sword!' Gilina tosses Kilidna's head aside. 'Thank you, Kilidna. Your services are no longer required. Well it seems we have quite the [dilemma] on our hands, wouldn't you say?
        - Condition: `(e.other:Class() == "Shadow Knight")`
        - Condition: `(e.message:findi("powerful beings") and qglobals["shadowknight_epic"] == "10")`
      - Player: "Dilemma" (link: explicit mention)
        - NPC say: Luckily, I have much knowledge of Lhranc, the first of the shadowknights. We must find a way to anchor him to this plane so that he will be vulnerable to our attacks. I believe if we recover some items of his from his former life, we may be able to accomplish this. First, you will need to find his pendant. Look for it in the City of Mist. Next, you will need to recover Lhranc's corroded bracer from Charasis. Lastly, you will need to find Lhranc's ring from the undead in the Kithicor Woods. Once you have all these items, return them to me.
        - Condition: `(e.other:Class() == "Shadow Knight")`
        - Condition: `(e.message:findi("dilemma") and qglobals["shadowknight_epic"] == "10")`

7. poknowledge/"Gilina Yilzior", hand "Gubblegrot's Head" (16793) + "Silithis's Head" (16813) + "Giligatabbus's Head" (20079) + "Skurza's Head" (20899). Sets `shadowknight_epic` to `7`.
    - Requires `shadowknight_epic` ==6.
    - Hand in x1: "Skurza's Head" (20899).
    - Hand in x1: "Silithis's Head" (16813).
    - Hand in x1: "Gubblegrot's Head" (16793).
    - Hand in x1: "Giligatabbus's Head" (20079).
    - Loot "Skurza's Head" (20899) from "Skurza Slicekutt" in `swampofnohope`.
    - Loot "Silithis's Head" (16813) from "Silithis Sisnta" in `timorous`.
    - Loot "Gubblegrot's Head" (16793) from "Gubblegrot Smashfist" in `oceanoftears`.
    - Loot "Gubblegrot's Head" (16793) from "Gubblegrot Smashfist" in `oot`.
    - Loot "Giligatabbus's Head" (20079) from "Giligatabbus Igglebix" in `iceclad`.
    - Gives "Sheathed Innoruuk's Voice" (22199).

8. poknowledge/"Gilina Yilzior", hand "Paladin Blood Sample" (20904) + "Paladin Blood Sample" (20904) + "Paladin Blood Sample" (20904) + "Sheathed Innoruuk's Voice" (22199). Sets `shadowknight_epic` to `8`.
    - Requires `shadowknight_epic` ==7.
    - Hand in x1: "Paladin Blood Sample" (20904).
    - Hand in x1: "Sheathed Innoruuk's Voice" (22199).
    - Say "Hail" to kithicor/"Tarnamil".
    - Spawns "Uglib Gaibido" (20293).
    - Loot "Paladin Blood Sample" (20904) from "Uglib Gaibido".
    - Alternative: Loot "Paladin Blood Sample" (20904) from "Tilminos Farondi" (NPC 20298) in `kithicor`; trigger: kithicor/"Tarnamil", say "Hail".
    - Alternative: Loot "Paladin Blood Sample" (20904) from "Valinda Ergington" (NPC 20296) in `kithicor`; trigger: kithicor/"Tarnamil", say "Hail".
    - Prerequisite: "Sheathed Innoruuk's Voice" (22199). See section 0.

9. poknowledge/"Gilina Yilzior", say "Vision". Sets `shadowknight_epic` to `9`.
    - Requires `shadowknight_epic` unset.

10. poknowledge/"Gilina Yilzior", hand "Kilidna's Head" (19098). Sets `shadowknight_epic` to `10`.
    - Requires `shadowknight_epic` ==9.
    - Hand in x1: "Kilidna's Head" (19098).
    - Loot "Kilidna's Head" (19098) from "Kilidna" in `citymist`.

11. dranik/"Filligno The Slayer", hand "Lhranc's Earthly Anchor" (24584) + "Globe of Discordant Energy" (47100). Sets `shadowknight_epic` to `11`.
    - Requires `shadowknight_epic` ==10.
    - Hand in x1: "Lhranc's Earthly Anchor" (24584).
    - Hand in x1: "Globe of Discordant Energy" (47100).
    - Prerequisite: "Lhranc's Earthly Anchor" (24584). See section 0.
    - Say "Check Lorb" to anguish/"Zone Status".
    - Spawns "Orb of Discordant Energy" (317087).
    - Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy".
    - Alternative: Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy" (NPC 317087) in `anguish`; trigger: anguish/"Zone Status", say "Check Uorb".
    - Alternative: Loot "Globe of Discordant Energy" (47100) from "Ornate Chest" (NPC 317112) in `anguish`; trigger: anguish/"Zone Status", say "Check Amv Chest".
    - Alternative: Loot "Globe of Discordant Energy" (47100) from "Orb of Discordant Energy" (NPC 317087) in `anguish`; trigger: anguish/"Zone Status", on event_signal.
    - Alternative: Loot "Globe of Discordant Energy" (47100) from "Overlords Chest" (NPC 317124) in `anguish`; trigger: anguish/"Zone Status", on event_signal.
    - Dialogue with dranik/"Filligno The Slayer":
      - Player: "Ready" (link: external event mention)
        - Prompted by `event_trade`:
          - NPC say: Yes, yes, Gilina said you would be coming. I can help you in your battle against Lhranc! I have a personal vendetta against Lhranc. He killed my twin brother, Gilligno. This is going to be a tough battle. Lhranc has been reincarnated as a powerful general of the Mata Muram army. Are you [ready] for me to attempt the summoning of Lhranc?
          - Event guard: `(qglobals["shadowknight_epic"] == "10" and item_lib.check_turn_in(e.trade, {item1 = 24584, item2 = 47100}))`
        - NPC emote: throws Lhranc's earthly anchor and the globe of discordant energy above his head. To your amazement, they begin to hover.
        - NPC say: Oh mighty, Lhranc! We have slain your minions and have the blade that you seek! If you want it, come get it!' Filligno looks your way. 'What? You wanted a more elaborate incantion? It really doesn't take much to anger him. Trust me.' A moment later the ground begins to shake and a mighty voice booms out, 'Fools, I have followed the steps of this pathetic weakling who believes themselves to be a shadowknight. Now your lives will end and I will retrieve the blade destined to be mine! All of Norrath will fall before the might of the Mata Muram! Attack! Leave none standing!
        - NPC emote: begins to cower in fear.
        - NPC say: The blade isn't mine! Don't kill me! Please!
        - Condition: `(e.message:findi("ready") and qglobals["shadowknight_epic"] == "11")`
        - Spawns NPC 336251.

12. dranik/"Filligno The Slayer", hand "Innoruuk's Voice" (50003) + "Essence of the Shadowknight" (55903). Sets `shadowknight_epic` to `12`.
    - Requires `shadowknight_epic` ==11.
    - Hand in x1: "Essence of the Shadowknight" (55903).
    - Hand in x1: "Innoruuk's Voice" (50003).
    - Spawns "Lhranc" (336250) in `dranik` on event_signal.
    - Loot "Essence of the Shadowknight" (55903) from "Lhranc".
    - Prerequisite: "Innoruuk's Voice" (50003). See section 0.
    - Gives "Innoruuk's Dark Blessing" (48136).

### Steps on `shadowknight_epic` that do not change it

- `dranik` filligno the slayer, say ready needs `shadowknight_epic` ==11.
  - Spawns a Minion of Lhranc (336251).
- `dranik` player, on loot needs `shadowknight_epic` ==11.
  - Sets `sk_chest_dranik` to `1`.
  - Spawns a chest (Epic 2.0) (893).
- `kithicor` tarnamil, say hail needs `shadowknight_epic` ==7.
  - Spawns Uglib Gaibido (20293).
  - Spawns Xotmidd Ferlop (20294).
  - Spawns Jarnig Kilanid (20295).
  - Spawns Tilminos Farondi (20298).
  - Spawns Shressa Farondi (20297).
  - Spawns Valinda Ergington (20296).
  - Loots Two Handed Sword (5005).
  - Loots Paladin Blood Sample (20904).
  - Loots Two Handed Sword (5005).
  - Loots Uncut Alexandrite (37847).
  - Loots Uncut Jacinth (37850).
  - Loots Two Handed Sword (5005).
  - Loots Round Shield (9002).
  - Loots Sunshard Ore (33792).
  - Loots Two Handed Sword (5005).
  - Loots Paladin Blood Sample (20904).
  - Loots Two Handed Sword (5005).
  - Loots Sunshard Ore (33792).
  - Loots Two Handed Sword (5005).
  - Loots Round Shield (9002).
  - Loots Paladin Blood Sample (20904).
  - Loots Sunshard Ore (33792).
- `poknowledge` gilina yilzior, hand 23489+24612+24632 needs `shadowknight_epic` ==10.
  - Turn in Lhranc's Corroded Bracer (24612).
  - Turn in Lhranc's Pendant (23489).
  - Turn in Lhranc's Ring (24632).
  - Gives Lhranc's Earthly Anchor (24584).
- `poknowledge` gilina yilzior, hand 55901 needs `shadowknight_epic` ==8.
  - Turn in Sir Elmonious's Holy Symbol (55901).
  - Gives Innoruuk's Voice (50003).
- `poknowledge` grand librarian maelin, hand 55900 needs `shadowknight_epic` ==1.
  - Turn in Gelatinous Murkglider Egg (55900).
  - Gives The Silent Gods (20520).
- `westwastes` player, on loot needs `shadowknight_epic` ==8.
  - Sets `sk_westwastes` to `1`.
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

## Other flags touched along the way

- `sk_chest_dranik` set to 1 at dranik/player.
- `sk_westwastes` set to 1 at westwastes/player.
