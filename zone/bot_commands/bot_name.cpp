/*	EQEmu: EQEmulator

	Copyright (C) 2001-2026 EQEmu Development Team

	This program is free software; you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation; either version 3 of the License, or
	(at your option) any later version.

	This program is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
	GNU General Public License for more details.

	You should have received a copy of the GNU General Public License
	along with this program. If not, see <http://www.gnu.org/licenses/>.
*/
#include "zone/bot_command.h"

#include "common/eq_packet.h"
#include "common/eq_packet_structs.h"
#include "zone/entity.h"

void bot_command_rename(Client *c, const Seperator *sep)
{
	if (helper_command_alias_fail(c, "bot_command_rename", sep->arg[0], "botrename")) {
		return;
	}

	if (helper_is_help_or_usage(sep->arg[1]) || !sep->arg[1][0] || !sep->arg[2][0]) {
		c->Message(Chat::White, "Usage: %s [old_name] [new_name] (bot must be camped)", sep->arg[0]);
		return;
	}

	const std::string requested_name = sep->arg[1];
	std::string new_name = sep->arg[2];
	uint32 bot_id = 0;
	uint8 bot_class = Class::None;

	if (!database.botdb.LoadBotID(requested_name, bot_id, bot_class) || !bot_id ||
		database.botdb.GetOwnerID(bot_id) != c->CharacterID()) {
		c->Message(Chat::White, "You do not own a bot named '%s'.", requested_name.c_str());
		return;
	}

	// Camped bots may still have group/raid membership, but must have no live entity.
	if (entity_list.GetMobByBotID(bot_id)) {
		c->Message(Chat::White, "You must camp '%s' before renaming it.", requested_name.c_str());
		return;
	}

	if (new_name.find_first_not_of("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz") != std::string::npos ||
		!Bot::IsValidName(new_name)) {
		c->Message(Chat::White, "'%s' is not a valid bot name.", new_name.c_str());
		return;
	}

	if (!database.botdb.QueryNameAvailability(new_name)) {
		c->Message(Chat::White, "The name '%s' is unavailable.", new_name.c_str());
		return;
	}

	std::string old_name;
	if (!database.botdb.RenameBot(bot_id, c->CharacterID(), new_name, old_name)) {
		c->Message(Chat::White, "Failed to rename '%s'. Check the zone server log.", requested_name.c_str());
		return;
	}

	// The database is committed before changing any cached names or notifying clients.
	entity_list.RenameBotReferences(c->CharacterID(), old_name, new_name);

	// Notify the owner even though the bot has no spawned entity.
	EQApplicationPacket outapp(OP_MobRename, sizeof(MobRename_Struct));
	auto *data = reinterpret_cast<MobRename_Struct *>(outapp.pBuffer);
	outapp.priority = 6;
	strn0cpy(data->old_name, old_name.c_str(), sizeof(data->old_name));
	strn0cpy(data->old_name_again, old_name.c_str(), sizeof(data->old_name_again));
	strn0cpy(data->new_name, new_name.c_str(), sizeof(data->new_name));
	data->unknown192 = 0;
	data->unknown196 = 1;
	c->QueuePacket(&outapp);

	c->Message(Chat::White, "Bot '%s' renamed to '%s' (ID %u).", old_name.c_str(), new_name.c_str(), bot_id);
}

void bot_command_surname(Client *c, const Seperator *sep)
{
	if (sep->arg[1][0] == '\0' || sep->IsNumber(1)) {
		c->Message(Chat::White, "You must specify a [surname] to use this command (use _ to define spaces or -remove to clear.)");
		return;
	}
	auto my_bot = ActionableBots::AsTarget_ByBot(c);
	if (!my_bot) {
		c->Message(Chat::White, "You must <target> a bot that you own to use this command");
		return;
	}
	if (strlen(sep->arg[1]) > 31) {
		c->Message(Chat::White, "Surname must be 31 characters or less.");
		return;
	}
	std::string bot_surname = sep->arg[1];
	bot_surname = (bot_surname == "-remove") ? "" : bot_surname;
	std::replace(bot_surname.begin(), bot_surname.end(), '_', ' ');

	my_bot->SetSurname(bot_surname);
	if (database.botdb.SaveBot(my_bot)) {
		c->Message(Chat::White, "Bot Surname Saved.");
	}
}

void bot_command_title(Client *c, const Seperator *sep)
{
	if (sep->arg[1][0] == '\0' || sep->IsNumber(1)) {
		c->Message(Chat::White, "You must specify a [title] to use this command. (use _ to define spaces or -remove to clear.)");
		return;
	}
	auto my_bot = ActionableBots::AsTarget_ByBot(c);
	if (!my_bot) {
		c->Message(Chat::White, "You must <target> a bot that you own to use this command");
		return;
	}
	if (strlen(sep->arg[1]) > 31) {
		c->Message(Chat::White, "Title must be 31 characters or less.");
		return;
	}
	std::string bot_title = sep->arg[1];
	bot_title = (bot_title == "-remove") ? "" : bot_title;
	std::replace(bot_title.begin(), bot_title.end(), '_', ' ');

	my_bot->SetTitle(bot_title);
	if (database.botdb.SaveBot(my_bot)) {
		c->Message(Chat::White, "Bot Title Saved.");
	}
}

void bot_command_suffix(Client *c, const Seperator *sep)
{
	if (sep->arg[1][0] == '\0' || sep->IsNumber(1)) {
		c->Message(Chat::White, "You must specify a [suffix] to use this command. (use _ to define spaces or -remove to clear.)");
		return;
	}
	auto my_bot = ActionableBots::AsTarget_ByBot(c);
	if (!my_bot) {
		c->Message(Chat::White, "You must <target> a bot that you own to use this command");
		return;
	}
	if (strlen(sep->arg[1]) > 31) {
		c->Message(Chat::White, "Suffix must be 31 characters or less.");
		return;
	}
	std::string bot_suffix = sep->arg[1];
	bot_suffix = (bot_suffix == "-remove") ? "" : bot_suffix;
	std::replace(bot_suffix.begin(), bot_suffix.end(), '_', ' ');

	my_bot->SetSuffix(bot_suffix);
	if (database.botdb.SaveBot(my_bot)) {
		c->Message(Chat::White, "Bot Suffix Saved.");
	}
}
