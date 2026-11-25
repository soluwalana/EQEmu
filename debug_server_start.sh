EQEMU_QUESTS=${HOME}/work/projecteqquests\
  EQEMU_HOST=10.0.0.51 \
  EQEMU_USER=whatever \
  EQEMU_PASS=whatever \
  EQEMU_CHAR=Whatever \
  EQEMU_PEQ=~/Downloads/peq-dump/create_tables_content.sql \
  EQ_TRACE=VERBOSE \
  EQ_TRACE_EXCLUDE="OP_FloatListThing,OP_ClientUpdate,OP_PlayerStateAdd,OP_PlayerStateRemove,OP_MobHealth,OP_MobEnduranceUpdate,OP_MobManaUpdate" \
  python -m eqclient4.scripts.debug_server --port 8765
