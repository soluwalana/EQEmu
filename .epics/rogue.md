# Rogue

Steps taken from the quest graph only. **Broken** means the graph has no edge for that value or that item.

Flags with writes: `roguepre`.

## `roguepre`

Values written: 1.

### 1. dealer maeline — say cash out

Zone: `highkeep`.

> You have no winnings to cash in.

Sets `roguepre` to `1`.

- Needs `roguepre` unset.
In script order:

1. Sets `roguepre` to `1`.


### Steps on `roguepre` that do not change it

- `highkeep` dealer maeline, hand 9446 needs `roguepre` unset.
  - Turn in Gold-Leafed Urn (9446).

## Other flags touched along the way

- `rogue_chest_ice` set to 1 at iceclad/player.
- `rogue_chest_mira` set to 1 at mirb/durgin skell.
- `rogue_epic_durgin` set to 1 at mirb/durgin skell.
- `rogue_epic_iceclad` set to 1 at iceclad/lookout larithim.
- `rogue_epic_keetra` set to 1 at bloodfields/keetra the lost.
- `rogue_epic_lairyn` set to 1 at gunthak/lairyn debeian.
- `rogue_epic_larithim` set to 1 at iceclad/lookout larithim.
- `rogue_hate_chest` set to 1 at hateplaneb/player.
- `rogue_solc_chest` set to 1 at soldungc/player.
- `rogue_steam_chest` set to 1 at steamfont/player, steamfontmts/player.
