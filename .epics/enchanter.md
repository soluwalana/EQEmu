# Enchanter — Epic Quest Walkthrough

Generated directly from quest-graph item rewards. Unresolved dependencies are marked, not inferred.

## Epic 1.0

### "Staff of the Serpent" (10650)

<a id="epic-item-10650"></a>

1. qcat/"Reania Jukle", say "Hail".
    - Player: "hail"
      - NPC say: Greetings, $name. What can I help you with?
      - Condition: `($text=~/hail/i)`
2. Buy "Piece of Parchment" (13063) from "Hanlore Escaval" (NPC 1052) in `qeynos`. Base price: 100 copper.
3. Loot "Greater Lightstone" (10400) from "a windwillow wisp" (NPC 397070) in `mesa`. Drop cache: 32.7976% chance per kill.
4. northkarana/"Mrysila", hand "Greater Lightstone" (10400). Gives "Concordance of Research" (17504).
    - event_trade NPC say: A greater lightstone? Thank you very much. Here is a 'Concordance of Research' for you.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 10400}))`
5. Talk to acrylia/"Npc:154052" to trigger the encounter.
6. Spawns "needs heading validation" (npc:154147) via `acrylia/wdtrpmn#signal:1`.
7. Spawns "Ward of death" (npc:154155) via `acrylia/wdtrpmn#signal:1`.
8. Spawns "Ward of Life -- needs heading validation" (npc:154154) via `acrylia/wdtrpmn#signal:1`.
9. Spawns "EvInvis" (npc:154095) via `acrylia/wdtrpmn#signal:1`.
10. Spawns "RaidMan" (npc:154122) via `acrylia/wdtrpmn#signal:1`.
11. Spawns "grimling" (npc:154129) via `acrylia/evinvis#event_spawn`.
12. Kill "grimling" (NPC 154129) in `acrylia` and loot "Pearl" (10024).
13. Loot "Undead Froglok Tongue" (16532) from "BoneCracker" (NPC 44095) in `najena`. Drop cache: 25% chance per kill.
14. Loot "Griffon Feathers" (16538) from "Callowwing" (NPC 13115) in `northkarana`. Drop cache: 34% chance per kill.
15. Combine in "Concordance of Research" (17504): "Pearl" (10024), "Piece of Parchment" (13063), "Undead Froglok Tongue" (16532), "Griffon Feathers" (16538). Produces "Quill" (13051). Requires Research.
16. qey2hh1/"Chrislin Baker", hand "Piece of Parchment" (13063) + "Quill" (13051).
    - event_trade NPC emote: gives you a hug. 'Thank you so much. I did some cleaning after you left and found this behind a barrel. It may have been left behind by the person who took my materials. You can have it.'
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 13063,item2 = 13051}))`
17. Spawns "Thrackin Griften" (npc:12172) after the hand-in.
18. Kill "Thrackin Griften" (NPC 12172) in `qey2hh1` and loot "White Paper" (10602).
19. Loot "Shining Metallic Robes" (1360) from "Yendar Starpyre" (NPC 56012) in `steamfont`. Drop cache: 100% chance per kill.
20. akanon/"Rilgor Plegnog", hand "Shining Metallic Robes" (1360). Gives "Mechanical Pen" (10600).
    - event_trade NPC say: Very nice!! It is perfect! Here take this pen. Have fun with it.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 1360}))`
21. qcat/"Reania Jukle", say "Supply". Gives "Empty Ink Vial" (10626).
    - Player: "supply"
      - NPC say: The ink is the blood of a dark scribe. Tempt him and give him this vial. He should cooperate.
        - Reply guard: `($ulevel >= 50)`
      - NPC say: Sorry, but your skills just aren't advanced enough for this.
        - Reply guard: ``
      - Condition: `($text=~/supply/i)`
      - Linked from "ink of the dark" (explicit prompt).
22. gukbottom/"A Ghoul Scribe", hand "Empty Ink Vial" (10626). Gives "Ink of the Dark" (10601).
    - event_trade NPC say: Crroooaak! Crrroooooaaakk!
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 10626}))`
23. erudnext/"Stofo Olan", hand "White Paper" (10602) + "Mechanical Pen" (10600) + "Ink of the Dark" (10601). Gives "Copy of Notes" (10603).
    - event_trade NPC say: Yes, that is what I wanted. Here, take these notes. My teacher will be very interested if he is shown what I have found.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 10600,item2 = 10601,item3 = 10602}))`
24. burningwood/"A Sarnak Imitator", hand "Copy of Notes" (10603). Gives "Jeb's Seal" (10604).
    - event_trade NPC say: I see that you have what I was waiting for. Stofo does do excellent work. It seems that you are to start on a long journey. Take this seal and it will guide you on your next step. Seek out the masters of enchantment. In time we will craft the Serpent for you. When you have collected the four parts of the staff, you must combine them in a bundle and return them to me.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 10603}))`
    - event_trade NPC say: Take this seal. You will need to show my seal to the other masters so that they may grant you the tools to complete your next tasks. When you have collected the four parts of the staff, you must combine them in a bundle for me. The other masters can provide the means to bundle them. Good luck and safe travels.
25. firiona/"Nadia Starfeast", say "I Need A Sack". Gives "Enchanters Sack" (17861).
    - Player: "i need a sack"
      - NPC say: Take this sack and combine the items I requested in it. Then return it to me.
      - Condition: `($text=~/i need a sack/i && plugin::check_hasitem($client,10604))`
      - Linked from "hail" (sequence only; unverified).
26. Loot "Xolion Rod" (10606) from "Vessel Drozlin" (NPC 106008) in `cabeast`. Drop cache: 100% chance per kill.
27. Loot "Innoruuk's Word" (10607) from "Verina Tomb" (NPC 42112) in `neriakc`. Drop cache: 100% chance per kill.
28. Loot "Head of a Prince" (10627) from "Prince Selrach Di`zok" (NPC 103080) in `chardok`. Drop cache: 100% chance per kill.
29. felwitheb/"Joren Nobleheart", hand "Head of a Prince" (10627). Gives "Chalice of Kings" (10608).
    - event_trade NPC say: Vengeance has been fufilled! However, the King still has a heavy heart. Not until Firiona has been returned can this sadness be lifted. But in appreciation of your efforts, I am honored to present to you the King's Chalice.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 10627}))`
30. Collect ground spawn "Large Muddy Sandals" (10628) in `oggok`.
31. oggok/"Bozlum Blossom", hand "Large Muddy Sandals" (10628). Gives "Scribbled Parchment" (10629).
    - event_item NPC emote: writes something down on a piece of parchment.
      - Event guard: `(plugin::check_handin(\%itemcount, 10628 => 1))`
    - event_item NPC say: You go tell dat Brokk dat he owe me big for smushing garden. Make him read dis.
32. oggok/"Brokk Boxtripper", hand "Scribbled Parchment" (10629). Gives "Gift to Bozlum" (10630).
    - event_item NPC say: Brokk sorry, me no smush Bozlum's perty garden on purpose. Me felt bad and me too shy to go tell Boz Brokk sorry. Umm....go give her these perty flowers. Dem smell good and maybe make Bozlum feel better.
      - Event guard: `(plugin::check_handin(\%itemcount, 10629 => 1))`
33. oggok/"Bozlum Blossom", hand "Gift to Bozlum" (10630). Gives "Snow Blossoms" (10609).
    - event_item NPC say: 'Oh, dat silly Brokk. He sent me too many of these perty flowers. Me not know where put them all. Here, you take some cause you help Bozlum. Me like you. Flowers make you smell perty, too.
      - Event guard: `(plugin::check_handin(\%itemcount, 10630 => 1))`
34. Combine in "Enchanters Sack" (17861): "Xolion Rod" (10606), "Innoruuk's Word" (10607), "Chalice of Kings" (10608), "Snow Blossoms" (10609). Produces "Sack For Modani" (10635). Requires Remove Traps.
35. overthere/"Modani Qu-Loni", hand "Sack For Modani" (10635). Gives "1st Piece of Staff" (10610).
    - event_item NPC say: Excellent, you have done well. Here is the first piece of the staff. Now you must go seek out the second master; he will clear the path for you.
      - Event guard: `(plugin::check_handin(\%itemcount, 10635 => 1))`
36. Loot "Spoon" (10614) from "Cazel" (NPC 393012) in `southro`. Drop cache: 81.25% chance per kill.
37. Collect ground spawn "The One Key" (10615) in `overthere`.
38. Collect ground spawn "Lost Scroll" (10616) in `dalnir`.
39. Collect ground spawn "Charm and Sacrifice" (10617) in `airplane`.
40. Combine in "Enchanters Sack" (17861): "Spoon" (10614), "The One Key" (10615), "Lost Scroll" (10616), "Charm and Sacrifice" (10617). Produces "Sack For Mizzle" (10636). Requires Remove Traps.
41. akanon/"Clockwork Viix", hand "Sack For Mizzle" (10636). Gives "2nd Piece of Staff" (10611).
    - event_trade NPC say: Oh excellent, you have done what is required. Here take this part, and seek the third master, you are well on your way.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 10636}))`
42. firiona/"Nadia Starfeast", say "Diamond". Gives "Dull Diamond" (10631).
    - Player: "diamond"
      - NPC say: Here is the diamond that I have prepared for you. Its only purpose is to trap the essence of a particular book worm. If you should fail in your first attempt, do not worry. I will provide you with another.
      - Condition: `($text=~/diamond/i)`
      - Linked from "gems" (explicit prompt).
43. kaesora/"Spectral Librarian", hand "Dull Diamond" (10631). Gives "Enchanted Diamond" (10618).
    - event_item NPC say: You have no idea what it is like to be trapped in this place. Take your precious little stone and leave this place.
      - Event guard: `(plugin::check_handin(\%itemcount, 10631 => 1))`
44. firiona/"Nadia Starfeast", say "Sapphire". Gives "Dull Sapphire" (10632).
    - Player: "sapphire"
      - NPC say: Here is the sapphire that I have prepared for you. Take it and give it to the one referred to as the Golden Faerie.
      - Condition: `($text=~/sapphire/i)`
      - Linked from "gems" (explicit prompt).
45. skyfire/"Felia Goldenwing", hand "Dull Sapphire" (10632). Gives "Enchanted Sapphire" (10619).
46. firiona/"Nadia Starfeast", say "Ruby". Gives "Dull Ruby" (10633).
    - Player: "ruby"
      - NPC say: Blood red is the ruby that I have given you. The city that you must travel to has no sun, but still a day and night. And at night, the mist could suffocate one. Tis the fate of poor Jaxion.
      - Condition: `($text=~/ruby/i)`
      - Linked from "gems" (explicit prompt).
47. citymist/"Wraith Of Jaxion", hand "Dull Ruby" (10633). Gives "Enchanted Ruby" (10620).
    - event_trade NPC say: Hisss...my spirit is forever trapped here. Leave before your fate is as mine.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 10633}))`
48. firiona/"Nadia Starfeast", say "Emerald". Gives "Dull Emerald" (10634).
    - Player: "emerald"
      - NPC emote: jumps.
      - NPC say: Eeekk... a scorpion. I thought they rid this area of these critters. Those things give me the creepers. Take this emerald and be on your way.
      - Condition: `($text=~/emerald/i)`
      - Linked from "gems" (explicit prompt).
49. overthere/"Impaler Tzilug", hand "Dull Emerald" (10634). Gives "Enchanted Emerald" (10621).
    - event_item NPC say: Your bidding has been done, now leave this land and never return.
      - Event guard: `(plugin::check_handin(\%itemcount, 10634 => 1))`
50. Combine in "Enchanters Sack" (17861): "Enchanted Diamond" (10618), "Enchanted Sapphire" (10619), "Enchanted Ruby" (10620), "Enchanted Emerald" (10621). Produces "Sack For Nadia" (10637). Requires Remove Traps.
51. firiona/"Nadia Starfeast", hand "Sack For Nadia" (10637). Gives "3rd Piece of Staff" (10612).
    - event_item NPC say: Lovely! You are indeed quite the charmer. Here, take the third part, and seek out the last master. The time draws near.
      - Event guard: `(plugin::check_handin(\%itemcount, 10637 => 1))`
52. Loot "Head of the Serpent" (10622) from "Wraith of a Shissar" (NPC 72001) in `fearplane`. Drop cache: 100% chance per kill.
53. Loot "Essence of a Ghost" (10623) from "the Ghost of Kindle" (NPC 39080) in `hole`. Drop cache: 100% chance per kill.
54. Loot "Essence of a Vampire" (10624) from "a forsaken revenant" (NPC 76005) in `hateplane`. Drop cache: 10.5658% chance per kill.
55. Loot "Sands of the Mystics" (10625) from "The Tangrin" (NPC 78070) in `fieldofbone`. Drop cache: 100% chance per kill.
56. Combine in "Enchanters Sack" (17861): "Head of the Serpent" (10622), "Essence of a Ghost" (10623), "Essence of a Vampire" (10624), "Sands of the Mystics" (10625). Produces "Sack For Polzin" (10638). Requires Remove Traps.
57. hole/"Polzin Mrid", hand "Sack For Polzin" (10638). Gives "4th Piece of Staff" (10613).
    - event_item NPC say: You have done well, take this last piece and return them to Jeb. He will be able to complete the final crafting.
      - Event guard: `(plugin::check_handin(\%itemcount, 10638 => 1))`
58. Combine in "Enchanters Sack" (17861): "1st Piece of Staff" (10610), "2nd Piece of Staff" (10611), "3rd Piece of Staff" (10612), "4th Piece of Staff" (10613). Produces "Bundle of Staves" (10639). Requires Remove Traps.
59. burningwood/"A Sarnak Imitator", hand "Bundle of Staves" (10639). Gives "Staff of the Serpent" (10650).
    - event_trade NPC say: The path you trod was long and hard. Now you are worthy to bear the Serpent. Use it well.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 10639}))`

## Epic 1.5

### "Oculus of Persuasion" (52952)

<a id="epic-item-52952"></a>

1. akanon/"Rilgor Plegnog", say "Hail".
    - Player: "hail"
      - NPC say: Oh, what is it now. Can't you see that I am a very busy gnome?
      - Condition: `(e.message:findi("hail"))`
2. Loot "Crumbling Tome" (54313) from "A Shissar Lorekeeper" (NPC 162184) in `ssratemple`. Drop cache: 100% chance per kill.
3. Loot "Dragon Boneshard" (65574) from "a curate" (NPC 109068) in `veksar`. Drop cache: 10% chance per kill.
4. veksar/"Spirit Of Garudon", hand "Dragon Boneshard" (65574).
5. Spawns "Garudon" (npc:109107) after the hand-in.
6. Kill "Garudon" (NPC 109107) in `veksar` and loot "Garudon's Statue" (52941).
7. lakeofillomen/"A Bloodgill Mimic", hand "Garudon's Statue" (52941).
    - event_trade NPC say: I thank you. How terrible it must be to still remain after such time. You must possess some measure of power to return this to me. I believe Aida could benefit from the help of one such as yourself.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 52941}))`
8. ssratemple/"A Soriz Imitator", hand "Crumbling Tome" (54313). Gives "Illegible Tome" (52947).
    - event_trade NPC say:  'It is remarkable that you have found it! Unfortunately, it appears to be written in some language so archaic I cannot even begin to decipher it. Please, you must see Rilgor about a translating device. I will stay here and see if I can find anything further that would be of use.' 
      - Event guard: `(qglobals["EnchPre"] == "1" and item_lib.check_turn_in(e.trade, {item1 = 54313}))`
9. akanon/"Rilgor Plegnog", say "Insidious". Gives "Compacting Satchel" (54303).
    - Player: "insidious"
      - NPC say: 'Yes indeed, it is lovely. Fetch me a set and I just might consider undertaking that translating device of yours. Take this sack. I am quite interested in the halo, sleeves, manacle, gloves, pantaloons, and slippers. As I said, my robe is still serving me quite nicely, so no need to worry about that.' 
      - Condition: `(e.message:findi("insidious") and e.other:HasItem(52947))`
      - Linked from "compensation" (explicit prompt).
10. Loot "Fine Insidious Halo" (54384) from "a forsaken revenant" (NPC 186146) in `hateplaneb`. Drop cache: 2% chance per kill.
11. Loot "Fine Insidious Sleeves" (54385) from "a forsaken revenant" (NPC 186146) in `hateplaneb`. Drop cache: 2.08% chance per kill.
12. Loot "Fine Insidious Manacle" (54386) from "a forsaken revenant" (NPC 186146) in `hateplaneb`. Drop cache: 2.0914% chance per kill.
13. Loot "Fine Insidious Gloves" (54387) from "a forsaken revenant" (NPC 186146) in `hateplaneb`. Drop cache: 2.2398% chance per kill.
14. Loot "Fine Insidious Pantaloons" (54388) from "a forsaken revenant" (NPC 186146) in `hateplaneb`. Drop cache: 2.2284% chance per kill.
15. Loot "Fine Insidious Slippers" (54389) from "a forsaken revenant" (NPC 186146) in `hateplaneb`. Drop cache: 2.0685% chance per kill.
16. Combine in "Compacting Satchel" (54303): "Fine Insidious Halo" (54384), "Fine Insidious Sleeves" (54385), "Fine Insidious Manacle" (54386), "Fine Insidious Gloves" (54387), "Fine Insidious Pantaloons" (54388), "Fine Insidious Slippers" (54389). Produces "Insidious Bundle" (54317). Requires Remove Traps.
17. akanon/"Rilgor Plegnog", hand "Insidious Bundle" (54317). Gives "Gnomish Translating Device" (52945).
    - event_trade NPC say: 'Very fine it is. So kind of you to fulfill a dream of mine. I believe this device should be able to handle just about anything you'd need. In fact, if I were you I would take it along to your master right away.' 
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 54317}))`
18. burningwood/"A Sarnak Imitator", hand "Illegible Tome" (52947) + "Gnomish Translating Device" (52945). Gives "Tattered Illegible Tome" (57918).
    - event_trade NPC say: How very interesting. This could prove to be invaluable to my work. I have long been researching a new and most powerful tool to help our kind. It is necessary in these most dangerous of times. Unfortunately, it appears as though time has taken its toll on this tome. It is incomplete. Seek the missing pages so that I may study it in depth. There should be ten, unless they have been destroyed by time and decay.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 52947, item2 = 52945}))`
19. Collect ground spawn "Cryptic Page" (52933) in `charasis`.
20. Collect ground spawn "Cryptic Page" (52934) in `sebilis`.
21. Collect ground spawn "Cryptic Page" (52935) in `cazicthule`.
22. Collect ground spawn "Cryptic Page" (52936) in `crystal`.
23. Collect ground spawn "Cryptic Page" (52937) in `skyshrine`.
24. Collect ground spawn "Cryptic Page" (52938) in `velketor`.
25. Collect ground spawn "Cryptic Page" (52939) in `nadox`.
26. Collect ground spawn "Cryptic Page" (54308) in `najena`.
27. Collect ground spawn "Cryptic Page" (57916) in `fungusgrove`.
28. Collect ground spawn "Cryptic Page" (57923) in `oot`.
29. Combine in "Tattered Illegible Tome" (57918): "Cryptic Page" (52933), "Cryptic Page" (52934), "Cryptic Page" (52935), "Cryptic Page" (52936), "Cryptic Page" (52937), "Cryptic Page" (52938), "Cryptic Page" (52939), "Cryptic Page" (54308), "Cryptic Page" (57916), "Cryptic Page" (57923). Produces "Complete Illegible Tome" (54267). Requires Remove Traps.
30. burningwood/"A Sarnak Imitator", hand "Complete Illegible Tome" (54267).
    - event_trade NPC say: As I suspected, this is something extraordinary. You must go speak to Maelin at once. It has been many moons since I have entered the Plane of Knowledge. He may well have some new information for me. Go at once and tell him I sent you.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 54267}))`
31. poknowledge/"Grand Librarian Maelin", say "Jeb Lumsed Sent Me". Gives "Note to Lobaen" (52950).
    - Player: "jeb lumsed sent me"
      - NPC say: This is from Jeb, you say? I will set my best researchers on it at once. We have recently made some discoveries that he should be aware of. Here, take this note down to Lobaen, she will retrieve them for you.
      - Condition: `(qglobals["ench_epic"] == "2" and e.message:findi("Jeb Lumsed sent me"))`
      - Linked from "find an egg" (sequence only; unverified).
32. poknowledge/"Illusionist Lobaen", hand "Note to Lobaen" (52950). Gives "Sealed Documents" (52959).
    - event_trade NPC say: It is not often that I receive a request from Maelin himself. Please, take these and be most careful.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 52950}))`
33. burningwood/"A Sarnak Imitator", hand "Sealed Documents" (52959). Gives "Assembling the Staff" (54286).
    - event_trade NPC say: Interesting indeed. I see that I was not wrong in my instinct to begin this as quickly as possible. I have created a list of the items that you will need to begin the construction of this tool. Mind you, it will not be a simple thing. When you have gathered them all return to me. Would you like a [chest] to carry them in?
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 52959}))`
34. burningwood/"A Sarnak Imitator", say "Chest". Gives "Ornate Staff Chest" (52960).
    - Player: "chest"
      - Condition: `(e.message:findi("chest") and qglobals["ench_epic"] ~= nil and qglobals["ench_epic"] >= "3")`
35. Collect ground spawn "Taste of Enticement" (52964) in `mistmoore`.
36. frozenshadow/"Advisor Svartmane", hand "Taste of Enticement" (52964). Gives "1st Piece of the Staff" (54289).
    - event_trade NPC say: I can't . . I . . .of course, I do not think that Tserrina has any need for this. I can't imagine that she would miss it at all. Please, take it.
      - Event guard: `(qglobals["ench_epic"] ~= nil and qglobals["ench_epic"] >= "2" and e.other:GetFaction(e.self) < 5)`
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 52964}))`
37. Loot "2nd Piece of the Staff" (54310) from "the yrendan scarab" (NPC 201422) in `pojustice`. Drop cache: 100% chance per kill.
38. Loot "3rd Piece of the Staff" (54299) from "Chavoor the Trickster" (NPC 290057) in `vxed`. Drop cache: 100% chance per kill.
39. Loot "4th Piece of the Staff" (54284) from "War Caller Kaavi" (NPC 301042) in `bloodfields`. Drop cache: 100% chance per kill.
40. Loot "Ornate Staff Topper" (52961) from "Faleniel of Darkwater" (NPC 125070) in `sirens`. Drop cache: 100% chance per kill.
41. Loot "All-Seeing Eye" (54293) from "All-Seeing Eye" (NPC 126374) in `mischiefplane`. Drop cache: 100% chance per kill.
42. potranquility/"Elder Fuirstel", say "Hail". Sets `pop_cod_final` to `1`.
    - Player: "hail"
      - NPC message: Elder Fuirstel slowly turns towards you. You can feel the heat radiating from his face. The warding that envelopes your body reaches out and begins to surround him. You immediately see improvement in his condition. The pus filled sores covering his face and his burning fever start to vanish.
      - NPC say: Thank you friend. I no longer feel the touch of death on my soul. However I do feel the grasp on Bertoxxulous, his plague is still upon me but not spreading throughout my body. I fear the only way to remove this pox would be to weaken Bertoxxulous enough that his curse would be lifted. I now renounce my faith in Bertoxxulous, please fell this god so that I may continue and learn from my mistakes.
      - NPC message: You receive a character flag!
      - Condition: `($text=~/hail/i && $pop_pod_alder_fuirstel == 1 && $pop_pod_grimmus_planar_projection == 1 && $pop_pod_elder_fuirstel == undef)`
43. poknowledge/"Aid Grimel", say "Skill In Brewing". Gives "Portable Drink Barrel" (17179).
    - Player: "skill in brewing"
      - NPC say: I bet you could make a wicked brew! However I am forced to drink a refreshing drink while out adventuring. I do have this powder that will give the best drinks quite a bite though. Mix the powder in with two Kaladim Constitutionals and a flask of pure water. If you need more dust just ask for it! Put three twice brewed constitutionals and the signet in this drink barrel. As hard as drink barrels are to get these days, you need to return it to me along with the drink you create with it.
        - Reply guard: `($client->GetRawSkill(65) >= 220)`
      - NPC say: You do not seem to be skilled enough.
        - Reply guard: ``
      - Condition: ``
      - Condition: `(defined($qglobals{pop_cod_final}) && ($qglobals{pop_cod_final} == 1))`
      - Condition: `(($text=~/skill in brewing/i) && plugin::check_hasitem($client, 16249))`
      - Linked from "versed in the art of smithing" (sequence only; unverified).
44. erudnext/"Lumi Stergnon", say "Battle The Undead". Gives "Box For Bones" (17941).
    - Player: "battle the undead"
      - NPC say: Then you shall venture to Toxxulia Forest. There has been an increase in skeleton sightings lately. I do not know their origin, but I believe that your efforts will reduce their numbers! Take this box. Return it to me when you have filled it with the bones of these undead creatures and combined it. May Quellious' light guide you.
      - Condition: `(e.message:findi("battle the undead"))`
      - Linked from "new acolyte of peace" (explicit prompt).
45. Loot "Useless Cloth Cap" (13894) from "a kobold scout" (NPC 38035) in `tox`. Drop cache: 20% chance per kill.
46. tox/"A Skeleton", hand "Useless Cloth Cap" (13894). Gives "Bone Chips" (13073).
47. Combine in "Box For Bones" (17941): "Bone Chips" (13073). Produces "Box of Bones" (13882). Requires Remove Traps.
48. qeynos/"Wolten Grafe", hand "Box of Bones" (13882). Gives "Water Flask" (13006).
    - event_trade NPC say: You have done well. Let it be known to all that you fight for the Rainkeeper. Go and continue the battle.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 13882}))`
49. Forage "Dragon Egg" (19139) in `templeveeshan` or `westwastes`.
50. Combine in "Portable Drink Barrel" (17179): "Water Flask" (13006), "Dragon Egg" (19139). Produces "Dragon Egg Oil" (9664). Requires Brewing.
51. Loot "Glimmering Oil" (52942) from "a greasy clockwork" (NPC 206048) in `poinnovation`. Drop cache: 100% chance per kill.
52. Buy "Spell Research Kit" (93492) from "Eric Rasumus" (NPC 202375) in `poknowledge`. Base price: 10,000 copper.
53. Buy "Firing Sheet" (16906) from "Winn Greenbane" (NPC 5059) in `highpass`. Base price: 10 copper.
54. Loot "Small Block of Clay" (16900) from "a muddite recordkeeper" (NPC 16003) in `beholder`. Drop cache: 5.2127% chance per kill.
55. Combine in appropriate tradeskill container: "Small Block of Clay" (16900), "Water Flask" (13006). Produces "Block of Clay" (16901). Requires Pottery.
56. Combine in appropriate tradeskill container: "Block of Clay" (16901), "Water Flask" (13006). Produces "Large Block of Clay" (16902). Requires Pottery.
57. Buy "Large Bowl Sketch" (16963) from "Min Greyeagle" (NPC 5057) in `highpass`. Base price: 760 copper.
58. Combine in appropriate tradeskill container: "Large Block of Clay" (16902), "Water Flask" (13006), "Large Bowl Sketch" (16963). Produces "Unfired Mixing Bowl" (16930). Requires Pottery.
59. Combine in appropriate tradeskill container: "Firing Sheet" (16906), "Unfired Mixing Bowl" (16930). Produces "Mixing Bowl" (17906). Requires Pottery.
60. Buy "Concentrated Celestial Solvent" (96952) from "Gilliad Coldheart" (NPC 121050) in `crystal`. Base price: 372 copper.
61. Spawns "a wraith" (npc:90064) via `citymist/npc:90006#event_death_complete`.
62. Kill "a wraith" (NPC 90064) in `citymist` and loot "The Scent of Marr" (11802).
63. Combine in "Mixing Bowl" (17906): "Concentrated Celestial Solvent" (96952), "The Scent of Marr" (11802). Produces "Celestial Essence" (9650). Requires Baking.
64. Loot "Coalesced Mana" (97042) from "Assistant Gareth" (NPC 371049) in `skylance`. Drop cache: 66.667% chance per kill.
65. Loot "White Wolf Skin" (13768) from "a snow wolf" (NPC 30014) in `everfrost`. Drop cache: 23.7188% chance per kill.
66. Buy "Vial Sketch" (16968) from "Winn Greenbane" (NPC 5059) in `highpass`. Base price: 300 copper.
67. Combine in appropriate tradeskill container: "Water Flask" (13006), "White Wolf Skin" (13768), "Small Block of Clay" (16900), "Vial Sketch" (16968). Produces "Unfired Poison Vial" (16885). Requires Pottery.
68. Buy "High Quality Firing Sheet" (16908) from "Winn Greenbane" (NPC 5059) in `highpass`. Base price: 40 copper.
69. Combine in appropriate tradeskill container: "Unfired Poison Vial" (16885), "High Quality Firing Sheet" (16908). Produces "Poison Vial" (16965). Requires Pottery.
70. Spawns "The Broodqueen" (npc:337254) via `broodlands/brood drone#event_death_complete`.
71. Kill "The Broodqueen" (NPC 337254) in `broodlands` and loot "Ruby" (10035).
72. Combine in "Spell Research Kit" (93492): "Celestial Essence" (9650), "Coalesced Mana" (97042), "Poison Vial" (16965), "Ruby" (10035). Produces "Vial of Purified Mana" (10254). Requires Research.
73. Forage "Glow Lichen" (14925) in `nektulos`.
74. Loot "Essence of Sunlight" (22527) from "a faerie dragon" (NPC 119073) in `wakening`. Drop cache: 55% chance per kill.
75. Collect ground spawn "Abysmal Moonwater" (54298) in `abysmal`.
76. Combine in appropriate tradeskill container: "Vial of Purified Mana" (10254), "Glow Lichen" (14925), "Essence of Sunlight" (22527), "Abysmal Moonwater" (54298). Produces "Glowing Concoction" (52943). Requires Brewing.
77. Buy "Medicine Bag" (17901) from "Rendallen Ironforge" (NPC 2071) in `qeynos2`. Base price: 1,000 copper.
78. Buy "Glaze Lacquer" (29355) from "Elisha Dirtyshoes" (NPC 202134) in `poknowledge`. Base price: 8,000 copper.
79. Buy "Prism Shard" (65469) from "Elisha Dirtyshoes" (NPC 202134) in `poknowledge`. Base price: 5,000 copper.
80. Combine in "Medicine Bag" (17901): "Glaze Lacquer" (29355), "Prism Shard" (65469). Produces "Prismatic Dye" (65472). Requires Alchemy.
81. Combine in appropriate tradeskill container: "Dragon Egg Oil" (9664), "Glimmering Oil" (52942), "Glowing Concoction" (52943), "Prismatic Dye" (65472). Produces "Incandescent Oil" (57924). Requires Brewing.
82. Loot "Sullied Gold Filigree" (52963) from "an enticing potameid" (NPC 280070) in `natimbi`. Drop cache: 85.106% chance per kill.
83. hohonora/"Anthone Chapin", hand "Sullied Gold Filigree" (52963). Gives "Purified Gold Filigree" (52953).
84. Combine in "Ornate Staff Chest" (52960): "1st Piece of the Staff" (54289), "2nd Piece of the Staff" (54310), "3rd Piece of the Staff" (54299), "4th Piece of the Staff" (54284), "Ornate Staff Topper" (52961), "All-Seeing Eye" (54293), "Incandescent Oil" (57924), "Purified Gold Filigree" (52953). Produces "Latched Ornate Chest" (52966). Requires Remove Traps.
85. burningwood/"A Sarnak Imitator", hand "Latched Ornate Chest" (52966). Gives "Oculus of Persuasion" (52952).
    - event_trade NPC say: You have done well, my student. The staff is now complete. In order to stand up to the true fury of discord, it will need purifying, but even in this state it shall protect you well.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 52966}))`
    - event_trade NPC message: You have gained 5 ability points!

## Epic 2.0

### "Staff of Eternal Eloquence" (52962)

<a id="epic-item-52962"></a>

**Earlier reward routes required by this graph path:** ["Oculus of Persuasion" (52952)](#epic-item-52952).
Revisit those instructions if another copy of a consumed item is needed.

1. Loot "Tattered Incantation" (57919) from "Cipheron" (NPC 300031) in `wallofslaughter`. Drop cache: 100% chance per kill.
2. Loot "Noxious Secretion" (52951) from "Withering Murkglider" (NPC 303078) in `causeway`. Drop cache: 100% chance per kill.
3. Buy "Planar Jeweler's Kit" (17764) from "Noirin Khalen" (NPC 202084) in `poknowledge`. Base price: 1,000 copper.
4. Loot "Heart of a Twisted Stoneservant" (54239) from "a twisted stoneservant" (NPC 282016) in `riwwi`. Drop cache: 90.129% chance per kill.
5. wakening/"Alaurin", hand "Heart of a Twisted Stoneservant" (54239).
    - event_trade NPC say: How very interesting. There is a geonid of great beauty that I have seen nearby in the caves. I have coveted its shining gem for some time. Destroy it and bring me the stone and I shall let you have your fragment.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 54239}) and e.other:HasItem(52952) and not eq.get_entity_list():IsMobSpawnedByNpcTypeID(119184))`
6. Spawns "a luminescent geonid" (npc:119184) after the hand-in.
7. Kill "a luminescent geonid" (NPC 119184) in `wakening` and loot "Luminescent Crystal" (52949).
8. wakening/"Alaurin", hand "Luminescent Crystal" (52949). Gives "Purifying Crystal Fragment" (52955).
    - event_trade NPC say: It is even more beautiful from up close. Look at the way it sparkles! Take your fragment then, and leave me in peace.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 52949}) and e.other:HasItem(52952))`
9. Loot "Volatile Vampyre Blood" (52965) from "a Coterie insatiate" (NPC 172189) in `tenebrous`. Drop cache: 100% chance per kill.
10. westwastes/"Vohnkare", hand "Volatile Vampyre Blood" (52965). Gives "Purifying Crystal Fragment" (52956).
    - event_trade NPC say: This will do quite nicely. Are you aware of the properties of vampyre blood? It can make such lovely protective concoctions. Why, I once fended off . . . There I go again. Here is your crystal, make haste!
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 52965}) and e.other:HasItem(52952) and not eq.get_entity_list():IsMobSpawnedByNpcTypeID(119184))`
11. Loot "Harnessing Stone" (52946) from "Miriku the Chaotic" (NPC 113561) in `kael`. Drop cache: 100% chance per kill.
12. Buy "Gnomish Candy" (52944) from "Clockwork Merchant" (NPC 55308) in `akanon`. Base price: 125,000 copper.
13. Buy "Koada`Dal Silk" (52948) from "Merchant Tyslin" (NPC 61044) in `felwithea`. Base price: 125,000 copper.
14. Buy "Feir`Dal Champagne" (52940) from "Innkeep" (NPC 19084) in `rivervale`. Base price: 125,000 copper.
15. Buy "Dwarven Steel" (57921) from "Gretta Mottle" (NPC 60000) in `kaladima`. Base price: 125,000 copper.
16. lfaydark/"A Brownie Noble", hand "Gnomish Candy" (52944) + "Koada`Dal Silk" (52948) + "Feir`Dal Champagne" (52940) + "Dwarven Steel" (57921).
    - event_trade NPC say: Perhaps your intentions are true, after all. I have one shard of a purifying crystal that you will need for the task ahead of you. It is quite powerful, and I hate to part with it. I will give it to you, but only in trade. There is a harnessing stone possessed by a seeker in Kael. It is less powerful than the crystal, but should prove sufficient for my needs. Bring me this crystal and it shall be yours.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 52944,item2 = 52948,item3 = 52940,item4 = 57921}) and e.other:HasItem(52952) and not eq.get_entity_list():IsMobSpawnedByNpcTypeID(119184))`
17. lfaydark/"A Brownie Noble", hand "Harnessing Stone" (52946). Gives "Purifying Crystal Fragment" (52957).
    - event_trade NPC say: Very well, here is the fragment. I can only imagine at the power of the unified crystal.
      - Event guard: `(qglobals["ench_epic"] == "8" and item_lib.check_turn_in(e.trade, {item1 = 52946}) and e.other:HasItem(52952) and not eq.get_entity_list():IsMobSpawnedByNpcTypeID(119184))`
18. Spawns "a devastating pooka" (npc:289037) via `tipt/rikabi the riddler#spawn_devastating_pookas`.
19. Kill "a devastating pooka" (NPC 289037) in `tipt` and loot "Mountain Pooka Meat" (54240).
20. jaggedpine/"Chef Brargus", hand "Mountain Pooka Meat" (54240).
    - event_item NPC say: That should do nicely. Now, about Firwyn. You should be able to find her in the forest nearby but I would be careful if I were you. She can be a bit feisty, and you don't exactly look like a warrior if you know what I mean.
      - Event guard: `(plugin::check_handin(\%itemcount, 54240 => 1))`
21. Spawns "Firwyn" (npc:181226) after the hand-in.
22. Kill "Firwyn" (NPC 181226) in `jaggedpine` and loot "Dryad Necklace" (57917).
23. gfaydark/"Feyana Lightwing", hand "Dryad Necklace" (57917). Gives "Purifying Crystal Fragment" (52958).
    - event_trade NPC say: Even lovelier than I remembered. Thank you ever so much.
      - Event guard: `(item_lib.check_turn_in(e.trade, {item1 = 57917}) and e.other:HasItem(52952) and not eq.get_entity_list():IsMobSpawnedByNpcTypeID(119184))`
24. Combine in "Planar Jeweler's Kit" (17764): "Purifying Crystal Fragment" (52955), "Purifying Crystal Fragment" (52956), "Purifying Crystal Fragment" (52957), "Purifying Crystal Fragment" (52958). Produces "Purifying Crystal" (52954). Requires Jewelry Making.
25. Combine recipe recipe:19919 to set `ench_epic` to `9`.
26. nedaria/"Priestess Rakhu", hand "Tattered Incantation" (57919) + "Noxious Secretion" (52951). Gives "Channeling Crystal" (57920).
    - event_trade NPC emote: murmurs in a strange tongue as she scans the incantation. She draws an intricate design along different portions of the staff, using the strange secretion, from which rises a pale green smoke. At last she stops and opens her eyes. 'Perfect. This tool has been consecrated and protected in the best way I know. There is but one thing left to do, for the staff is ready but not yet tested. Take this channeling crystal and venture into the land riddled with discord. When you encounter great evil there, you will recognize the energy of discord. Channel this energy into your staff, and it will become something more powerful than this world has seen. I wish you luck.
      - Event guard: `(qglobals["ench_epic"] == "9" and item_lib.check_turn_in(e.trade, {item1 = 57919,item2 = 52951}))`
27. global/"Global Player", say "Recipe:19908". Gives "Globe of Discordant Energy" (47100).
28. Combine in "Channeling Crystal" (57920): "Globe of Discordant Energy" (47100), "Oculus of Persuasion" (52952). Produces "Staff of Eternal Eloquence" (52962). Requires Remove Traps.
