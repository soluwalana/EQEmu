#!/usr/bin/env bash
set -euo pipefail

SRC="${EQEMU_SRC:-$HOME/other/EQEmu}"
PEQ_DUMP="${EQEMU_PEQ_DUMP:-$HOME/other/peq-dump}"
RUN="${EQEMU_RUN:-$HOME/other/eqemu-run}"
source "${EQEMU_DB_ENV:-$HOME/other/eqemu-data/mariadb.env}"

MYSQL=(mysql --max-allowed-packet=256M -h 127.0.0.1 -P 3306 -u "$MARIADB_USER" -p"$MARIADB_PASSWORD" "$MARIADB_DATABASE")

"$RUN/eqemu.sh" stop || true

# Tables created by migrations after this dump. drop_all_tables.sql does not know them,
# so a second reload leaves them behind and the same CREATE/RENAME fails again.
"${MYSQL[@]}" -e "
SET FOREIGN_KEY_CHECKS = 0;
DROP TABLE IF EXISTS
  starting_items_backup_9243,
  starting_items_new,
  guild_permissions,
  guild_tributes,
  character_parcels,
  character_parcels_containers,
  buyer_buy_lines,
  buyer_trade_items,
  character_evolving_items,
  items_evolving_details,
  character_pet_name,
  player_event_loot_items,
  player_event_merchant_sell,
  player_event_merchant_purchase,
  player_event_npc_handin,
  player_event_npc_handin_entries,
  player_event_trade,
  player_event_trade_entries,
  player_event_speech,
  player_event_killed_npc,
  player_event_killed_named_npc,
  player_event_killed_raid_npc,
  player_event_aa_purchase,
  dynamic_zone_lockouts,
  zone_state_spawns;
SET FOREIGN_KEY_CHECKS = 1;
"

(
	cd "$PEQ_DUMP"
	"${MYSQL[@]}" -e "source drop_all_tables.sql"
	"${MYSQL[@]}" -e "source create_all_tables.sql"
)

(cd "$RUN" && ./world bots:disable)
(cd "$RUN" && ./world bots:enable)
(cd "$RUN" && ./world database:updates)

