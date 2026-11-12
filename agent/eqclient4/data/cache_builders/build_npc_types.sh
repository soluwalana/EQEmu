mysql -h 10.0.0.51 -P 3306 -u eqemu -D peq --password=$MARIADB_PASSWORD -N -B --raw <<'SQL' > ~/.eqclient/npc_types.jsonl
SET SESSION group_concat_max_len = 1048576;

SELECT JSON_OBJECT(
    'id', nt.id,
    'name', nt.name,
    'lastname', nt.lastname,
    'race', nt.race,
    'class', nt.class,
    'level', nt.level,
    'bodytype', nt.bodytype,
    'npc_faction_id', nt.npc_faction_id,
    'spawngroups', COALESCE(
        JSON_QUERY(sp.spawngroups, '$'), JSON_ARRAY()
    ),
    'zones', COALESCE(
        JSON_QUERY(sp.zones, '$'), JSON_ARRAY()
    )
)
FROM npc_types nt
LEFT JOIN (
    SELECT
        se.npcID,
        JSON_ARRAYAGG(
            DISTINCT se.spawngroupID ORDER BY se.spawngroupID
        ) AS spawngroups,
        JSON_ARRAYAGG(
            DISTINCT s2.zone ORDER BY s2.zone
        ) AS zones
    FROM spawnentry se
    INNER JOIN spawn2 s2
        ON s2.spawngroupID = se.spawngroupID
    GROUP BY se.npcID
) sp ON sp.npcID = nt.id
ORDER BY nt.id;
SQL
