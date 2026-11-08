from pathlib import Path

DATA_DIR = Path(__file__).parent


def load_dbstr(path: Path) -> dict[tuple[int, int], str]:
    strings = {}
    with open(path, encoding="utf-8-sig", errors="replace") as f:
        for line in f:
            try:
                parts = line.rstrip("\r\n").split("^", 3)
                if len(parts) >= 3:
                    sid, kind, text = parts[:3]
                    strings[(int(sid), int(kind))] = text
            except ValueError:
                continue
    return strings


DB_STRS = load_dbstr(DATA_DIR / "dbstr_us.txt")

DB_STR_TYPES = {
    0: "banner_campsite_description",
    1: "aa_name",
    2: "hotkey_line_1",
    3: "hotkey_line_2",
    4: "aa_description",
    5: "spell_effect_category",
    6: "spell_description",
    7: "lore_group",
    8: "race_description",
    9: "class_description",
    10: "stat_description",
    11: "race_name",
    12: "race_name_plural",
    13: "class_name_plural",
    14: "deity_description",
    15: "starting_city_description",
    16: "augmentation_type",
    17: "currency_name",
    18: "currency_name_plural",
    19: "aa_category",
    20: "expansion_name",
    21: "mercenary_type",
    22: "mercenary_tier",
    23: "mercenary_type_description",
    24: "mercenary_stance",
    25: "mercenary_stance_description",
    26: "mercenary_stance_tooltip",
    28: "npc_quest_command_unknown",
    31: "membership_advertisement",
    32: "membership_upgrade_label",
    33: "membership_action_button",
    34: "achievement_description",
    35: "achievement_description_alternate",
    36: "mercenary_group",
    39: "resist_type",
    43: "item_click_effect_description",
    44: "damage_type",
    45: "faction_name",
    47: "currency_description",
    52: "overseer_agent_short_name",
    53: "overseer_agent_full_name",
    61: "overseer_agent_lore",
    71: "brellium_token",
}


def load_eqstr(path: Path) -> dict[int, str]:
    strings = {}
    with open(path, encoding="utf-8-sig", errors="replace") as f:
        for line in f:
            try:
                parts = line.rstrip("\r\n").split("^", 1)
                if len(parts) == 2 and parts[0].isdigit():
                    strings[int(parts[0])] = parts[1].rstrip("^")
            except ValueError:
                continue
    return strings


EQ_STRS = load_eqstr(DATA_DIR / "eqstr_us.txt")
