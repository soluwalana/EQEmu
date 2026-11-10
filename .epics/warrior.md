# Warrior — Epic Quest Walkthrough

Generated directly from quest-graph item rewards. Unresolved dependencies are marked, not inferred.

## Epic 1.0

### "Jagged Blade of War" (10908)

1. freeporteast/"Kargek Redblade", say "Hail".
    - Player: "hail"
      - NPC emote:  looks up from his forge and says, 'Hello there, can I help you?' Your eyes are drawn to an extremely large red sword scabbard strapped to his back with no sword in it. Kargek speaks again, 'I said, can I help you or do you need help from Wenden?'
      - Condition: `(e.other:Class() == "Warrior")`
      - Condition: `(e.message:findi("hail"))`
2. freeporteast/"Kargek Redblade", say "Favor". Gives "Wax Sealed Note" (20673).
    - Player: "favor"
      - NPC say: An associate of mine is wandering somewhere in the Feerrott. His name is Oknoggin Stonesmacker. If you will deliver this note to him, I would appreciate it.
      - Condition: `(e.other:Class() == "Warrior")`
      - Condition: `(e.message:findi("favor"))`
      - Linked from "scabbard" (explicit prompt).
3. feerrott/"Oknoggin Stonesmacker", hand "Wax Sealed Note" (20673). Gives "Tiny Lute" (20674).
    - event_trade NPC emote: snatches the note from your hand and rips it open with his large hands. 'You take dis to Kargek. He want!'
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 20673}))`
4. freeporteast/"Kargek Redblade", hand "Tiny Lute" (20674). Gives "Redblade's Legacy" (18083).
    - event_trade NPC say: Thank you for delivering the note to my associate. Take this book - it will tell you a little of the history of the old scabbard. If you would like to own the scabbard, seek out my younger brother Tenal and give him the book.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 20674}))`
5. eastkarana/"Tenal Redblade", hand "Redblade's Legacy" (18083). Gives "Totem of the Freezing War" (20680).
    - event_trade NPC say: So, you know my brother Kargek. He is weak and does not believe the legend that our family was chosen by Rallos Zek to bear the great scabbard. Yet he still holds it. Very well, I shall give you the first test since my 'dear' brother seems to have forgotten it. Travel to the fortress where the children of Rallos were first cursed by the Rathe and bring me the heart of one of the goblins who have made it their new home. Do not return without the heart of your foe and this war totem.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 18083}))`
6. Loot "Heart of Frost" (10549) from "a goblin wizard" (NPC 73038) in `permafrost`. Drop cache: 20% chance per kill.
7. eastkarana/"Tenal Redblade", hand "Totem of the Freezing War" (20680) + "Heart of Frost" (10549). Gives "Totem of Fiery War" (20681).
    - event_trade NPC say: Very good, you have wreaked havoc on your foes in the ancient land of the giants. Rallos Zek must have guided your blade. (Tenal's voice is suddenly silenced and you feel as if your body is frozen. From Tenal's lips issues a voice that is not his own.) 'Bring this mortal the scales of the children of Veeshan. The red and green as well as my war totem. I will guide your blade.' Your movement returns as Tenal falls to the ground, gasping for breath.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 20680,item2 = 10549}))`
8. Loot "Red Dragon Scales" (11622) from "Lord Nagafen" (NPC 32040) in `soldungb`. Drop cache: 36.408% chance per kill.
9. northro/"Verrell Cogswin", hand "Red Dragon Scales" (11622).
    - event_item NPC emote: pulls a vial out of his pocket and places the red scale on the ground before pouring some of the vials contents on the scale. The scale begins to bubble and fizz as the liquid covers it entirely. Verrell looks at you and smiles before looking back at the scale. gasping and snatching the scale up from the floor.
      - Event guard: `(plugin::check_handin(\%itemcount, 11622 => 1))`
      - Event guard: `(defined($qglobals{Green_Scale_Quest}) && ($qglobals{Green_Scale_Quest} == 1))`
    - event_item NPC say: Hmmm . . well I have some [good news] and a lot of [bad news] which do you want to hear first?
10. northro/"Verrell Cogswin", say "Adhesive". Gives "Verrell's Box of Potions" (67387).
    - Player: "adhesive"
      - NPC say: In order to make this special adhesive you will need to combine some [glue powder] and some [Deep Barley Brew] in this container with this special vial. Return the result to me and I should be able to fix the scale, but please try to hurry I have to meet my brother Pellillo Cogswin at the wizard platform so he can take me home.
      - Condition: `(defined($qglobals{Green_Scale_Quest}) && ($qglobals{Green_Scale_Quest} == 2))`
      - Condition: `($text=~/adhesive/i)`
      - Linked from "catch" (explicit prompt).
11. Loot "Fractured Centaur Hoof" (67388) from "centaur sheltie" (NPC 14088) in `southkarana`. Drop cache: 35% chance per kill.
12. Loot "Fire Giant Embers" (67389) from "a fire giant warlord" (NPC 278023) in `soldungc`. Drop cache: 28.3488% chance per kill.
13. Loot "Jagged Permafrost Shards" (67390) from "The Chilling Terror" (NPC 73092) in `permafrost`. Drop cache: 25.4833% chance per kill.
14. Combine in appropriate tradeskill container: "Fractured Centaur Hoof" (67388), "Fire Giant Embers" (67389), "Jagged Permafrost Shards" (67390). Produces "Glue Powder" (67391). Requires Baking.
15. Buy "Barley" (16590) from "Heidi Grainsifter" (NPC 1065) in `qeynos`. Base price: 15 copper.
16. Buy "Deep Fungus Mold" (67393) from "Heidi Grainsifter" (NPC 1065) in `qeynos`. Base price: 50,000 copper.
17. Buy "Distilled Spirits" (67394) from "Heidi Grainsifter" (NPC 1065) in `qeynos`. Base price: 5,000 copper.
18. Combine in appropriate tradeskill container: "Barley" (16590), "Deep Fungus Mold" (67393), "Distilled Spirits" (67394). Produces "Deep Barley Brew" (67392). Requires Brewing.
19. Combine in "Verrell's Box of Potions" (67387): "Glue Powder" (67391), "Deep Barley Brew" (67392), "Potion Vial" (67395). Produces "Thick Adhesive" (67386). Requires Remove Traps.
20. northro/"Verrell Cogswin", hand "Thick Adhesive" (67386). Gives "Grey Scale Pieces" (67385).
    - event_item NPC say: That should do. Here, combine these in the Box of Potions I gave you.
      - Event guard: `(plugin::check_handin(\%itemcount, 67386 => 1))`
21. Combine in "Verrell's Box of Potions" (67387): "Grey Scale Pieces" (67385), "Thick Adhesive" (67396). Produces "Grey Colored Scales" (67384). Requires Remove Traps.
22. northro/"Verrell Cogswin", hand "Grey Colored Scales" (67384). Gives "Green Dragon Scales" (11582).
    - event_item NPC emote: pulls a vial out of his pocket and places the red scale on the ground before pouring some of the vials contents on the scale. The scale begins to bubble and fizz as the liquid covers it entirely. Verrell looks at you and smiles before looking back at the scale.
      - Event guard: `(plugin::check_handin(\%itemcount, 67384 => 1))`
    - event_item NPC say: Worked that time, yer bugger!
23. eastkarana/"Tenal Redblade", hand "Totem of Fiery War" (20681) + "Red Dragon Scales" (11622) + "Green Dragon Scales" (11582). Gives "Mark of the Sword" (20683).
    - event_trade NPC emote: looks at you oddly as you hand him the scales. 'What are..? 'You have done well, mortal, and you will be rewarded if you are truly brave. Travel to the Plane of Hatred and slay the ancient bard who lives there. Do not return without his hand and this mark or you will never be a true warlord.' Tenal drops to the ground as the last words leave his lips.'
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 20681,item2 = 11622,item3 = 11582}))`
24. Loot "Hand of the Maestro" (20676) from "Hand of the Maestro" (NPC 76015) in `hateplane`. Drop cache: 100% chance per kill.
25. eastkarana/"Tenal Redblade", hand "Mark of the Sword" (20683) + "Hand of the Maestro" (20676). Gives "Tenal's note to Kargek" (20684).
    - event_trade NPC emote: looks horrified as you give him the hand of the Maestro of Rancor and show him the mark of the sword.  The godlike voice returns, 'You have done well to acquire this. One final task must be completed before you hold the red scabbard in your mortal hands.' Tenal reaches out and hands you a note. 'Take this note and a wingblade of the spirocs to Kargek. When he receives them, I will speak to you one last time.'
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 20683,item2 = 20676}))`
26. Loot "Spiroc Wingblade" (20679) from "The Spiroc Lord" (NPC 71012) in `airplane`. Drop cache: 50.413% chance per kill.
27. freeporteast/"Kargek Redblade", hand "Tenal's note to Kargek" (20684) + "Spiroc Wingblade" (20679). Gives "Red Scabbard" (17859).
    - event_trade NPC say: What is this? A note from my brother? Thank you for the gift as well.' Kargek reads the note and hands you the huge sword hilt. Your mind is filled with the sound of battle and a voice. 'Place the ancient sword blade, ancient blade, finely crafted dragon head hilt and the jeweled dragon head hilt into the scabbard to receive your rewards. If you think you are worthy, place your rewards into the scabbard and see what havoc you can unleash on the world. Kargek addresses you as you turn to leave. 'One more thing. Gartrog over there has told me of a great discovery. Seems there are all sorts of stones being found in the recently discovered lost dungeons scattered around Antonica. The Wayfarer's Brotherhood has found a way to make items even more powerful by using the stones with existing items.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 20684, item2 = 20679}))`
28. Combine in "Red Scabbard" (17859): "Jagged Blade of War" (10908). Produces "Blade of Tactics" (10909). Requires Remove Traps.
29. Combine in "Red Scabbard" (17859): "Jagged Blade of War" (10908). Produces "Blade of Strategy" (10910). Requires Remove Traps.
30. Combine in "Red Scabbard" (17859): "Blade of Tactics" (10909), "Blade of Strategy" (10910). Produces "Jagged Blade of War" (10908). Requires Remove Traps.

**Unresolved graph dependencies:**
- Cycle while acquiring "Jagged Blade of War" (10908)

## Epic 1.5

### "Champion's Sword of Eternal Power" (60321)

1. Loot "Champion's Sword of Eternal Power" (60321) from "Krekk Brimblade" (NPC 336091) in `dranik`. Drop cache: 100% chance per kill.
**Unverified final reward:** "Champion's Sword of Eternal Power" (60321)

## Epic 2.0

### "Kreljnok's Sword of Eternal Power" (60332)

1. draniksscar/"Korbuk Brimblade", say "Hail".
    - Player: "hail"
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
2. Spawns "Korbuk" (npc:303128) via `causeway/warr trap#enter`.
3. Spawns "Essence of Kreljnok" (npc:303129) via `causeway/korbuk brimblade#event_death_complete`.
4. Kill "Essence of Kreljnok" (NPC 303129) in `causeway` and loot "Brimblade's Scabbard" (60331).
5. Kill "Essence of Kreljnok" (NPC 303129) in `causeway` and loot "Kreljnok's Essence" (60330).
6. Loot "Champion's Sword of Eternal Power" (60321) from "Krekk Brimblade" (NPC 336091) in `dranik`. Drop cache: 100% chance per kill.
7. Spawns "Larnik the Recluse" (npc:116609) via `eastwastes/warr trap#enter`.
8. Kill "Larnik the Recluse" (NPC 116609) in `eastwastes` and loot "Larnik's Locked Purification Kit" (60325).
9. draniksscar/"Korbuk Brimblade", hand "Larnik's Locked Purification Kit" (60325). Gives "Larnik's Unlocked Purification Kit" (60326).
    - event_trade NPC say: Uh oh. I'm guessing dat he didn't want to part with this peacefully? Well, I can't say I'm sorry. He was a jerk to me da last time we talked. I guess I just figured someone else might be able to persuade him to change his mind. I went ahead and broke open da lock for you. You'll be able to make use of da [kit] now.
      - Event guard: `(qglobals["warrior_epic"] ~= nil)`
      - Event guard: `(qglobals["warrior_epic"] >= "18" and item_lib.check_turn_in(e.trade, {item1 = 60325}))`
10. draniksscar/"Korbuk Brimblade", hand "Kreljnok's Muddled Rage" (60322). Gives "Kreljnok's Muddled Rage" (60322).
    - event_trade NPC say: All too easy. For you, I mean. You did well. I'm... I'm getting unclear visions from this essence. I can't seem to understand what it's trying to tell me. This essence is impure and needs to be purified. I happen to know of a [purification expert] dat can help us clear this mystery up.
      - Event guard: `(qglobals["warrior_epic"] ~= nil)`
      - Event guard: `(qglobals["warrior_epic"] >= "16" and item_lib.check_turn_in(e.trade, {item1 = 60322}))`
11. Combine in "Larnik's Unlocked Purification Kit" (60326): "Kreljnok's Muddled Rage" (60322). Produces "Kreljnok's Focused Rage" (60327). Requires Remove Traps.
12. draniksscar/"Korbuk Brimblade", hand "Champion's Sword of Eternal Power" (60321) + "Kreljnok's Focused Rage" (60327). Gives "Raging Sword of Eternal Power" (60329).
    - event_trade NPC say: Well done. Well done, indeed. I knew da moment I saw you dat you were da right person for all of this. Here is da sword, but there's one [last item] dat you need to do.
      - Event guard: `(qglobals["warrior_epic"] ~= nil)`
      - Event guard: `(qglobals["warrior_epic"] >= "19" and item_lib.check_turn_in(e.trade, {item1 = 60321, item2 = 60327}))`
13. Combine in "Brimblade's Scabbard" (60331): "Kreljnok's Essence" (60330), "Raging Sword of Eternal Power" (60329). Produces "Kreljnok's Sword of Eternal Power" (60332). Requires Remove Traps.

**Unresolved graph dependencies:**
- Cycle while acquiring "Kreljnok's Muddled Rage" (60322)
