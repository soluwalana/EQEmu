#include "zone/bot_command.h"
#include "zone/bot_raid_roster.h"

#include "common/strings.h"

#include "fmt/format.h"

void bot_command_raidform(Client* c, const Seperator* sep)
{
	if (helper_command_alias_fail(c, "bot_command_raidform", sep->arg[0], "raidform")) {
		return;
	}

	if (helper_is_help_or_usage(sep->arg[1])) {
		c->Message(Chat::White, "usage: %s [all | save | reset | camp | clear]", sep->arg[0]);
		c->Message(Chat::White, "all replaces the roster with every bot you own and forms the raid.");
		c->Message(Chat::White, "save stores the current raid groups. reset rebuilds them and requires raid leadership.");
		c->Message(Chat::White, "camp sends the bots away and keeps their seats. clear stops the roster from forming again.");
		return;
	}

	const std::string sub = Strings::ToLower(sep->arg[1] ? sep->arg[1] : "");

	if (sub.empty()) {
		BotRaidRoster::Form(c, false, false);
	}
	else if (sub == "all") {
		BotRaidRoster::ReplaceWithAll(c);
	}
	else if (sub == "save") {
		BotRaidRoster::Save(c);
	}
	else if (sub == "reset") {
		BotRaidRoster::Form(c, true, false);
	}
	else if (sub == "camp") {
		BotRaidRoster::Camp(c);
	}
	else if (sub == "clear") {
		BotRaidRoster::Clear(c);
	}
	else {
		c->Message(Chat::White, "usage: %s [all | save | reset | camp | clear]", sep->arg[0]);
	}
}

void bot_command_scatter(Client* c, const Seperator* sep)
{
	if (helper_command_alias_fail(c, "bot_command_scatter", sep->arg[0], "scatter")) {
		return;
	}

	if (helper_is_help_or_usage(sep->arg[1])) {
		c->Message(Chat::White, "usage: %s [radius]", sep->arg[0]);
		c->Message(Chat::White, "Bots guard a ring around you. Tanks stay at 15. The default radius is 60.");
		return;
	}

	float radius = 60.0f;
	if (sep->IsNumber(1)) {
		radius = Strings::ToFloat(sep->arg[1]);
	}

	BotRaidRoster::Scatter(c, radius);
}

void bot_command_stack(Client* c, const Seperator* sep)
{
	if (helper_command_alias_fail(c, "bot_command_stack", sep->arg[0], "stack")) {
		return;
	}

	if (helper_is_help_or_usage(sep->arg[1])) {
		c->Message(Chat::White, "usage: %s", sep->arg[0]);
		return;
	}

	BotRaidRoster::Stack(c);
}

void bot_command_stand(Client* c, const Seperator* sep)
{
	if (helper_command_alias_fail(c, "bot_command_stand", sep->arg[0], "stand")) {
		return;
	}

	if (helper_is_help_or_usage(sep->arg[1])) {
		c->Message(Chat::White, "usage: %s group <1-12> [clear] | %s <tanks|healers|support|dps|class> [clear]", sep->arg[0], sep->arg[0]);
		return;
	}

	const std::string first = Strings::ToLower(sep->arg[1] ? sep->arg[1] : "");
	if (first.empty()) {
		c->Message(Chat::White, "usage: %s group <1-12> [clear] | %s <tanks|healers|support|dps|class> [clear]", sep->arg[0], sep->arg[0]);
		return;
	}

	std::string who = first;
	bool clear = false;

	if (first == "group") {
		who = fmt::format("group {}", sep->arg[2] ? sep->arg[2] : "");
		clear = Strings::EqualFold(sep->arg[3] ? sep->arg[3] : "", "clear");
	}
	else {
		clear = Strings::EqualFold(sep->arg[2] ? sep->arg[2] : "", "clear");
	}

	BotRaidRoster::Stand(c, who, clear);
}

void bot_command_rez(Client* c, const Seperator* sep)
{
	if (helper_command_alias_fail(c, "bot_command_rez", sep->arg[0], "rez")) {
		return;
	}

	if (helper_is_help_or_usage(sep->arg[1])) {
		c->Message(Chat::White, "usage: %s [on | off | me | raid]", sep->arg[0]);
		return;
	}

	const std::string sub = Strings::ToLower(sep->arg[1] ? sep->arg[1] : "");

	if (sub.empty() || sub == "on") {
		BotRaidRoster::SetRezEnabled(c, true);
	}
	else if (sub == "off") {
		BotRaidRoster::SetRezEnabled(c, false);
	}
	else if (sub == "me") {
		BotRaidRoster::RezMe(c);
	}
	else if (sub == "raid") {
		BotRaidRoster::RezRaid(c);
	}
	else {
		c->Message(Chat::White, "usage: %s [on | off | me | raid]", sep->arg[0]);
	}
}
