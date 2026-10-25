#include "bot_raid_roster.h"

#include "bot.h"
#include "client.h"
#include "corpse.h"
#include "raids.h"

#include "common/classes.h"
#include "common/emu_constants.h"
#include "common/rulesys.h"
#include "common/spdat.h"
#include "common/strings.h"
#include "zone/zonedb.h"

#include "fmt/format.h"

#include <algorithm>
#include <cmath>
#include <unordered_map>
#include <utility>
#include <vector>

namespace {

enum RaidRole : uint8 {
	RaidRoleAuto = 0,
	RaidRoleTank = 1,
	RaidRoleHeal = 2,
	RaidRoleSupport = 3,
	RaidRoleDps = 4
};

struct RezClaim {
	uint16 corpse_id = 0;
	uint16 caster_id = 0;
	uint32 started = 0;
	uint32 expire = 0;
};

struct OwnerState {
	bool rez_enabled = true;
	bool heal_tanks = false;
	bool mez_adds = false;
	bool camp_set = false;
	std::string heal_focus_name;
	uint16 offtank_entity_id = 0;
	uint32 offtank_bot_id = 0;
	glm::vec4 camp{};
	uint32 last_tick = 0;
	uint32 last_assign = 0;
	std::vector<uint16> corpse_ids;
	std::vector<RezClaim> claims;
};

std::unordered_map<uint32, OwnerState> g_state;

OwnerState& State(uint32 character_id)
{
	return g_state[character_id];
}

std::string Normalize(const char* message)
{
	std::string lower = Strings::ToLower(message ? message : "");
	std::string out;
	bool pending_space = false;

	for (unsigned char ch : lower) {
		if (std::isspace(ch)) {
			if (!out.empty()) {
				pending_space = true;
			}
			continue;
		}

		if (pending_space) {
			out.push_back(' ');
			pending_space = false;
		}

		out.push_back(static_cast<char>(ch));
	}

	return out;
}

std::string Compact(std::string value)
{
	value.erase(
		std::remove_if(value.begin(), value.end(), [](unsigned char ch) { return std::isspace(ch) != 0; }),
		value.end()
	);
	return value;
}

bool IsTankClass(uint8 class_id)
{
	return class_id == Class::Warrior || class_id == Class::ShadowKnight || class_id == Class::Paladin;
}

bool IsHealClass(uint8 class_id)
{
	return class_id == Class::Cleric || class_id == Class::Druid;
}

bool IsSupportClass(uint8 class_id)
{
	return class_id == Class::Shaman || class_id == Class::Enchanter || class_id == Class::Bard;
}

bool IsDpsClass(uint8 class_id)
{
	return class_id == Class::Ranger ||
		class_id == Class::Monk ||
		class_id == Class::Rogue ||
		class_id == Class::Necromancer ||
		class_id == Class::Wizard ||
		class_id == Class::Magician ||
		class_id == Class::Beastlord ||
		class_id == Class::Berserker;
}

uint8 ResolveRole(uint8 class_id, uint8 roster_role)
{
	if (roster_role >= RaidRoleTank && roster_role <= RaidRoleDps) {
		return roster_role;
	}

	if (IsTankClass(class_id)) {
		return RaidRoleTank;
	}

	if (IsHealClass(class_id)) {
		return RaidRoleHeal;
	}

	if (IsSupportClass(class_id)) {
		return RaidRoleSupport;
	}

	return RaidRoleDps;
}

std::vector<Bot*> SpawnedOwned(Client* owner)
{
	std::vector<Bot*> bots;

	if (!owner) {
		return bots;
	}

	for (auto* bot : entity_list.GetBotsByBotOwnerCharacterID(owner->CharacterID())) {
		if (bot) {
			bots.push_back(bot);
		}
	}

	return bots;
}

void PlaceOnRing(const std::vector<Bot*>& bots, const glm::vec4& center, float radius)
{
	if (bots.empty()) {
		return;
	}

	if (bots.size() == 1 || radius < 1.0f) {
		for (auto* bot : bots) {
			bot->GuardAt(center);
		}
		return;
	}

	const float step = 6.2831853f / static_cast<float>(bots.size());

	for (size_t i = 0; i < bots.size(); ++i) {
		glm::vec4 point = center;
		point.x += radius * std::cos(step * static_cast<float>(i));
		point.y += radius * std::sin(step * static_cast<float>(i));
		bots[i]->GuardAt(point);
	}
}

uint8 ClassFromToken(std::string token)
{
	if (!token.empty() && token.back() == 's' && token != "dps") {
		token.pop_back();
	}

	const std::string compact_token = Compact(token);

	for (const auto& [class_id, class_name] : class_names) {
		const std::string compact_name = Compact(Strings::ToLower(class_name));
		if (compact_token == compact_name) {
			return class_id;
		}
	}

	return Class::None;
}

uint8 RoleFromToken(std::string token)
{
	if (!token.empty() && token.back() == 's') {
		token.pop_back();
	}

	if (token == "tank") {
		return RaidRoleTank;
	}

	if (token == "healer" || token == "heal") {
		return RaidRoleHeal;
	}

	if (token == "support") {
		return RaidRoleSupport;
	}

	if (token == "dp") {
		return RaidRoleDps;
	}

	return RaidRoleAuto;
}

void ForgetCorpse(OwnerState& state, uint16 corpse_id)
{
	state.corpse_ids.erase(
		std::remove(state.corpse_ids.begin(), state.corpse_ids.end(), corpse_id),
		state.corpse_ids.end()
	);
	state.claims.erase(
		std::remove_if(
			state.claims.begin(),
			state.claims.end(),
			[corpse_id](const RezClaim& claim) { return claim.corpse_id == corpse_id; }
		),
		state.claims.end()
	);
}

void StopRezzes(Client* owner)
{
	if (!owner) {
		return;
	}

	auto& state = State(owner->CharacterID());

	for (const auto& claim : state.claims) {
		Mob* caster = entity_list.GetMob(claim.caster_id);
		if (caster && caster->IsBot() && caster->IsCasting()) {
			caster->InterruptSpell();
		}

		Corpse* corpse = entity_list.GetCorpseByID(claim.corpse_id);
		if (corpse && corpse->RezClaimEntity() == claim.caster_id) {
			corpse->ClearRezClaim();
		}
	}

	state.claims.clear();
}

float RezRange(uint16 spell_id)
{
	float range = spells[spell_id].range;
	if (range < 1.0f) {
		range = 100.0f;
	}

	return range;
}

uint32 RezClaimDuration(uint16 spell_id)
{
	uint32 cast_time = spells[spell_id].cast_time;
	if (cast_time > 60000) {
		cast_time = 10000;
	}

	return cast_time + 2000;
}

bool StartRez(Client* owner, Bot* healer, Corpse* corpse)
{
	if (!owner || !healer || !corpse || healer->IsCasting()) {
		return false;
	}

	BotSpell rez = healer->GetBestBotSpellForRez(healer, corpse, BotSpellTypes::Resurrect);
	if (!rez.SpellId || !IsValidSpell(rez.SpellId)) {
		return false;
	}

	if (healer->GetMana() < rez.ManaCost) {
		return false;
	}

	if (Distance(healer->GetPosition(), corpse->GetPosition()) > RezRange(rez.SpellId)) {
		return false;
	}

	if (corpse->IsRezClaimedByOther(healer->GetID())) {
		return false;
	}

	const uint32 duration = RezClaimDuration(rez.SpellId);
	if (!corpse->TryClaimRez(healer->GetID(), duration)) {
		return false;
	}

	if (!healer->CastSpell(rez.SpellId, corpse->GetID())) {
		if (corpse->RezClaimEntity() == healer->GetID()) {
			corpse->ClearRezClaim();
		}
		return false;
	}

	auto& state = State(owner->CharacterID());
	const uint32 started = Timer::GetCurrentTime();
	state.claims.push_back({corpse->GetID(), healer->GetID(), started, started + duration});
	return true;
}

Bot* NearestRezzer(Client* owner, Corpse* corpse, const std::vector<Bot*>& healers)
{
	Bot* nearest = nullptr;
	float nearest_distance = 0.0f;

	for (auto* healer : healers) {
		if (!healer || healer->IsCasting() || healer->GetHP() <= 0) {
			continue;
		}

		BotSpell rez = healer->GetBestBotSpellForRez(healer, corpse, BotSpellTypes::Resurrect);
		if (!rez.SpellId || healer->GetMana() < rez.ManaCost) {
			continue;
		}

		const float distance = Distance(healer->GetPosition(), corpse->GetPosition());
		if (distance > RezRange(rez.SpellId)) {
			continue;
		}

		if (!nearest || distance < nearest_distance) {
			nearest = healer;
			nearest_distance = distance;
		}
	}

	return nearest;
}

std::vector<Corpse*> RezzableBotCorpses(Client* owner)
{
	std::vector<Corpse*> corpses;
	auto& state = State(owner->CharacterID());

	for (auto it = state.corpse_ids.begin(); it != state.corpse_ids.end();) {
		Corpse* corpse = entity_list.GetCorpseByID(*it);
		if (!corpse || !corpse->IsBotCorpse() || corpse->IsRezzed() || corpse->GetBotCorpseOwnerID() != owner->CharacterID()) {
			it = state.corpse_ids.erase(it);
			continue;
		}

		corpses.push_back(corpse);
		++it;
	}

	return corpses;
}

void AssignRezzes(Client* owner)
{
	if (!owner) {
		return;
	}

	std::vector<Bot*> clerics;
	std::vector<Bot*> druids;

	for (auto* bot : SpawnedOwned(owner)) {
		if (!bot || bot->GetHP() <= 0 || bot->IsCasting()) {
			continue;
		}

		if (bot->GetClass() == Class::Cleric) {
			clerics.push_back(bot);
		}
		else if (bot->GetClass() == Class::Druid) {
			druids.push_back(bot);
		}
	}

	std::vector<Bot*> pool = clerics.empty() ? druids : clerics;
	std::vector<Bot*> used;

	for (auto* corpse : RezzableBotCorpses(owner)) {
		std::vector<Bot*> free_healers;
		for (auto* healer : pool) {
			if (std::find(used.begin(), used.end(), healer) == used.end()) {
				free_healers.push_back(healer);
			}
		}

		Bot* healer = NearestRezzer(owner, corpse, free_healers);
		if (!healer) {
			continue;
		}

		if (StartRez(owner, healer, corpse)) {
			used.push_back(healer);
		}
	}
}

void WatchRezClaims(Client* owner)
{
	auto& state = State(owner->CharacterID());
	const uint32 now = Timer::GetCurrentTime();

	if (owner->IsCasting() && IsValidSpell(owner->CastingSpellID()) && IsResurrectSpell(owner->CastingSpellID())) {
		Mob* target = owner->GetTarget();
		if (target && target->IsCorpse()) {
			Corpse* corpse = target->CastToCorpse();
			const uint16 claim = corpse->RezClaimEntity();
			if (claim != owner->GetID()) {
				Mob* caster = claim ? entity_list.GetMob(claim) : nullptr;
				if (caster && caster->IsBot() && caster->IsCasting()) {
					caster->InterruptSpell();
				}

				corpse->ForceClaimRez(owner->GetID(), RezClaimDuration(owner->CastingSpellID()));
			}
		}
	}

	std::vector<RezClaim> kept;
	for (const auto& claim : state.claims) {
		Corpse* corpse = entity_list.GetCorpseByID(claim.corpse_id);
		Mob* caster = entity_list.GetMob(claim.caster_id);
		const bool expired = !corpse || corpse->IsRezzed() || !caster || caster->GetHP() <= 0;
		const bool cast_should_still_be_going = claim.expire > 2000 && now + 2000 < claim.expire;
		const bool interrupted = cast_should_still_be_going && now > claim.started + 500 && (!caster || !caster->IsCasting());

		if (expired || interrupted || (corpse && corpse->RezClaimEntity() != claim.caster_id)) {
			if (corpse && caster && corpse->RezClaimEntity() == claim.caster_id) {
				corpse->ClearRezClaim();
			}
			continue;
		}

		kept.push_back(claim);
	}

	state.claims.swap(kept);
}

Mob* ResolveNamedMob(Client* owner, const std::string& name)
{
	if (!owner || name.empty()) {
		return nullptr;
	}

	if (name == "me" || Strings::EqualFold(name, owner->GetName())) {
		return owner;
	}

	for (auto* bot : SpawnedOwned(owner)) {
		if (bot && Strings::EqualFold(bot->GetCleanName(), name)) {
			return bot;
		}
	}

	return entity_list.GetMob(name.c_str());
}

Mob* LowestTank(Client* owner)
{
	Mob* lowest = nullptr;

	auto consider = [&lowest](Mob* mob) {
		if (!mob || mob->GetHP() <= 0 || !IsTankClass(mob->GetClass())) {
			return;
		}

		if (!lowest || mob->GetHPRatio() < lowest->GetHPRatio()) {
			lowest = mob;
		}
	};

	consider(owner);
	for (auto* bot : SpawnedOwned(owner)) {
		consider(bot);
	}

	return lowest;
}

struct Candidate {
	uint32 bot_id = 0;
	std::string name;
	uint8 class_id = 0;
	uint8 roster_role = RaidRoleAuto;
	uint8 role = RaidRoleDps;
	uint8 saved_group = 255;
	uint8 group = 255;
	bool in_raid = false;
	bool place = false;
	bool leader = false;
};

bool TakeSlot(Candidate& candidate, int group, int* slots, bool* has_tank, bool* has_leader)
{
	if (group < 0 || group >= MAX_RAID_GROUPS || slots[group] <= 0) {
		return false;
	}

	candidate.group = static_cast<uint8>(group);
	candidate.place = true;
	slots[group]--;

	if (candidate.role == RaidRoleTank) {
		has_tank[group] = true;
	}

	if (!has_leader[group]) {
		candidate.leader = true;
		has_leader[group] = true;
	}

	return true;
}

void PlaceUnassignedTanks(std::vector<Candidate>& candidates, int* slots, bool* has_tank, bool* has_leader)
{
	for (auto& candidate : candidates) {
		if (candidate.in_raid || candidate.place || candidate.role != RaidRoleTank) {
			continue;
		}

		bool placed = false;
		for (int group = 0; group < MAX_RAID_GROUPS; ++group) {
			if (!has_tank[group] && TakeSlot(candidate, group, slots, has_tank, has_leader)) {
				placed = true;
				break;
			}
		}

		if (!placed) {
			for (int group = 0; group < MAX_RAID_GROUPS; ++group) {
				if (TakeSlot(candidate, group, slots, has_tank, has_leader)) {
					break;
				}
			}
		}
	}
}

void PlaceRoundRobin(std::vector<Candidate>& candidates, uint8 role, int* slots, bool* has_tank, bool* has_leader)
{
	int cursor = 0;

	for (auto& candidate : candidates) {
		if (candidate.in_raid || candidate.place || candidate.role != role) {
			continue;
		}

		for (int attempt = 0; attempt < MAX_RAID_GROUPS; ++attempt) {
			const int group = (cursor + attempt) % MAX_RAID_GROUPS;
			if (TakeSlot(candidate, group, slots, has_tank, has_leader)) {
				cursor = group + 1;
				break;
			}
		}
	}
}

Bot* SpawnRosterBot(Client* owner, const Candidate& candidate, bool& limit_hit)
{
	Mob* existing = entity_list.GetMobByBotID(candidate.bot_id);
	if (existing && existing->IsBot()) {
		return existing->CastToBot();
	}

	if (limit_hit) {
		return nullptr;
	}

	if (!Bot::CheckHighEnoughLevelForBots(owner, candidate.class_id)) {
		return nullptr;
	}

	if (!Bot::CheckSpawnLimit(owner) || !Bot::CheckSpawnLimit(owner, candidate.class_id)) {
		limit_hit = true;
		return nullptr;
	}

	Bot* loaded = Bot::LoadBot(candidate.bot_id);
	if (!loaded) {
		owner->Message(Chat::White, fmt::format("Could not load '{}'.", candidate.name).c_str());
		return nullptr;
	}

	if (!loaded->Spawn(owner, true)) {
		safe_delete(loaded);
		owner->Message(Chat::White, fmt::format("Could not spawn '{}'.", candidate.name).c_str());
		return nullptr;
	}

	return loaded;
}

void RememberRaidBot(Bot* bot, Raid* raid)
{
	if (!bot || !raid) {
		return;
	}

	bot->SetRaidGrouped(true);
	bot->SetStoredRaid(raid);
	bot->p_raid_instance = raid;
	bot->SetVerifiedRaid(false);
}

} // namespace

namespace BotRaidRoster {

void RegisterBotCorpse(uint32 owner_id, uint16 corpse_id)
{
	if (!owner_id || !corpse_id) {
		return;
	}

	auto& state = State(owner_id);
	if (std::find(state.corpse_ids.begin(), state.corpse_ids.end(), corpse_id) == state.corpse_ids.end()) {
		state.corpse_ids.push_back(corpse_id);
	}
}

void Forget(uint32 character_id)
{
	g_state.erase(character_id);
}

void Form(Client* owner, bool reset, bool quiet)
{
	if (!owner) {
		return;
	}

	if (!RuleB(Bots, Enabled)) {
		if (!quiet) {
			owner->Message(Chat::White, "Bots are disabled on this server.");
		}
		return;
	}

	if (!Bot::CheckHighEnoughLevelForBots(owner) || !Bot::CheckCampSpawnConditions(owner)) {
		return;
	}

	Raid* raid = entity_list.GetRaidByClient(owner);

	if (reset) {
		if (!raid) {
			owner->Message(Chat::White, "You are not in a raid.");
			return;
		}

		if (!raid->IsLeader(owner)) {
			owner->Message(Chat::White, "Only the raid leader can reset the bot raid.");
			return;
		}
	}

	std::vector<BotRaidRosterRecord> records;
	if (!database.botdb.LoadRaidRoster(owner->CharacterID(), records)) {
		owner->Message(Chat::White, "The bot raid roster table is missing. Run the database updates and try again.");
		return;
	}

	std::list<BotsAvailableList> owned_list;
	if (!database.botdb.LoadBotsList(owner->CharacterID(), owned_list) || owned_list.empty()) {
		if (!quiet) {
			owner->Message(Chat::White, "You do not own any bots.");
		}
		return;
	}

	std::unordered_map<uint32, BotsAvailableList> owned_by_id;
	for (const auto& bot : owned_list) {
		owned_by_id[bot.bot_id] = bot;
	}

	if (reset && raid) {
		for (const auto& record : records) {
			auto owned = owned_by_id.find(record.bot_id);
			if (owned == owned_by_id.end()) {
				continue;
			}

			if (raid->IsRaidMember(owned->second.bot_name)) {
				raid->RemoveMember(owned->second.bot_name);
			}
		}

		raid = entity_list.GetRaidByClient(owner);
	}

	std::vector<Candidate> candidates;
	for (const auto& record : records) {
		if (!record.active) {
			continue;
		}

		auto owned = owned_by_id.find(record.bot_id);
		if (owned == owned_by_id.end()) {
			continue;
		}

		Candidate candidate;
		candidate.bot_id = record.bot_id;
		candidate.name = owned->second.bot_name;
		candidate.class_id = static_cast<uint8>(owned->second.class_);
		candidate.roster_role = record.role;
		candidate.role = ResolveRole(candidate.class_id, record.role);
		candidate.saved_group = reset ? 255 : record.raid_group;
		candidates.push_back(candidate);
	}

	if (candidates.empty()) {
		if (!quiet) {
			owner->Message(Chat::White, "You have no active bot raid roster. Use ^raidform all.");
		}
		return;
	}

	if (!raid) {
		Group* group = owner->GetGroup();
		if (group) {
			for (const auto& member : group->members) {
				if (member && member->IsClient() && member != owner) {
					if (!quiet) {
						owner->Message(Chat::White, "Leave your group before forming a bot raid.");
					}
					return;
				}
			}

			if (!group->IsLeader(owner)) {
				if (!quiet) {
					owner->Message(Chat::White, "Leave your group before forming a bot raid.");
				}
				return;
			}

			group->DisbandGroup(false);
		}

		raid = new Raid(owner);
		entity_list.AddRaid(raid);
		if (!raid->GetID()) {
			safe_delete(raid);
			owner->Message(Chat::White, "Could not create a raid.");
			return;
		}

		raid->SetRaidDetails();
		raid->SendRaidCreate(owner);
		raid->AddMember(owner, 0, true, true, true);
		raid->SendMakeLeaderPacketTo(owner->GetName(), owner);
		owner->SetRaidGrouped(true);
	}

	int slots[MAX_RAID_GROUPS];
	bool has_tank[MAX_RAID_GROUPS];
	bool has_leader[MAX_RAID_GROUPS];

	for (int group = 0; group < MAX_RAID_GROUPS; ++group) {
		slots[group] = MAX_GROUP_MEMBERS;
		has_tank[group] = false;
		has_leader[group] = false;
	}

	for (const auto& member : raid->GetMembers()) {
		if (member.member_name[0] == '\0' || member.group_number >= MAX_RAID_GROUPS) {
			continue;
		}

		if (slots[member.group_number] > 0) {
			slots[member.group_number]--;
		}

		if (ResolveRole(member._class, RaidRoleAuto) == RaidRoleTank) {
			has_tank[member.group_number] = true;
		}

		if (member.is_group_leader) {
			has_leader[member.group_number] = true;
		}
	}

	for (auto& candidate : candidates) {
		candidate.in_raid = raid->IsRaidMember(candidate.name.c_str());
	}

	for (auto& candidate : candidates) {
		if (candidate.in_raid || candidate.role != RaidRoleTank || candidate.saved_group >= MAX_RAID_GROUPS) {
			continue;
		}

		TakeSlot(candidate, candidate.saved_group, slots, has_tank, has_leader);
	}

	PlaceUnassignedTanks(candidates, slots, has_tank, has_leader);

	for (auto& candidate : candidates) {
		if (candidate.in_raid || candidate.place || candidate.saved_group >= MAX_RAID_GROUPS) {
			continue;
		}

		TakeSlot(candidate, candidate.saved_group, slots, has_tank, has_leader);
	}

	PlaceRoundRobin(candidates, RaidRoleHeal, slots, has_tank, has_leader);
	PlaceRoundRobin(candidates, RaidRoleSupport, slots, has_tank, has_leader);
	PlaceRoundRobin(candidates, RaidRoleDps, slots, has_tank, has_leader);

	bool limit_hit = false;
	int added = 0;
	int skipped = 0;
	int spawned = 0;

	for (const auto& candidate : candidates) {
		if (!candidate.in_raid && !candidate.place) {
			++skipped;
			continue;
		}

		Bot* bot = SpawnRosterBot(owner, candidate, limit_hit);
		if (!bot) {
			if (!candidate.in_raid) {
				++skipped;
			}
			continue;
		}

		++spawned;

		if (candidate.in_raid || raid->IsRaidMember(bot->GetName())) {
			RememberRaidBot(bot, raid);
			continue;
		}

		raid->AddBot(bot, candidate.group, false, candidate.leader, false);
		RememberRaidBot(bot, raid);
		++added;
	}

	for (const auto& candidate : candidates) {
		if (!raid->IsRaidMember(candidate.name.c_str())) {
			continue;
		}

		const uint32 group = raid->GetGroup(candidate.name.c_str());
		BotRaidRosterRecord record;
		record.bot_id = candidate.bot_id;
		record.raid_group = group < MAX_RAID_GROUPS ? static_cast<uint8>(group) : 255;
		record.role = candidate.roster_role;
		record.active = 1;
		database.botdb.SaveRaidRosterEntry(owner->CharacterID(), record);
	}

	raid->SendBulkRaid(owner);

	if (!quiet || added || spawned) {
		owner->Message(
			Chat::White,
			fmt::format(
				"Bot raid formed. {} bots spawned, {} newly joined, {} left out.",
				spawned,
				added,
				skipped
			).c_str()
		);
	}
}

void Save(Client* owner)
{
	if (!owner) {
		return;
	}

	Raid* raid = entity_list.GetRaidByClient(owner);
	if (!raid) {
		owner->Message(Chat::White, "You are not in a raid.");
		return;
	}

	std::list<BotsAvailableList> owned_list;
	if (!database.botdb.LoadBotsList(owner->CharacterID(), owned_list)) {
		owner->Message(Chat::White, "Could not load your bots.");
		return;
	}

	std::unordered_map<std::string, BotsAvailableList> owned_by_name;
	for (const auto& bot : owned_list) {
		owned_by_name[bot.bot_name] = bot;
	}

	std::vector<BotRaidRosterRecord> previous;
	database.botdb.LoadRaidRoster(owner->CharacterID(), previous);
	std::unordered_map<uint32, uint8> previous_role;
	for (const auto& record : previous) {
		previous_role[record.bot_id] = record.role;
	}

	std::vector<BotRaidRosterRecord> records;
	for (const auto& member : raid->GetMembers()) {
		if (!member.is_bot || member.member_name[0] == '\0') {
			continue;
		}

		auto owned = owned_by_name.find(member.member_name);
		if (owned == owned_by_name.end()) {
			continue;
		}

		BotRaidRosterRecord record;
		record.bot_id = owned->second.bot_id;
		record.raid_group = member.group_number < MAX_RAID_GROUPS ? static_cast<uint8>(member.group_number) : 255;
		auto role = previous_role.find(record.bot_id);
		record.role = role == previous_role.end() ? RaidRoleAuto : role->second;
		record.active = 1;
		records.push_back(record);
	}

	if (!database.botdb.ReplaceRaidRoster(owner->CharacterID(), records)) {
		owner->Message(Chat::White, "Could not save the bot raid roster.");
		return;
	}

	owner->Message(Chat::White, fmt::format("Saved {} bots to the raid roster.", records.size()).c_str());
}

void Clear(Client* owner)
{
	if (!owner) {
		return;
	}

	if (!database.botdb.SetRaidRosterActive(owner->CharacterID(), 0)) {
		owner->Message(Chat::White, "Could not update the bot raid roster.");
		return;
	}

	owner->Message(Chat::White, "Bot raid roster will not form again until you ^raidform save or ^raidform all. The raid is unchanged.");
}

void Camp(Client* owner)
{
	if (!owner) {
		return;
	}

	Bot::BotOrderCampAll(owner);
	owner->Message(Chat::White, "Bots camped. Their raid seats are kept.");
}

void ReplaceWithAll(Client* owner)
{
	if (!owner) {
		return;
	}

	std::list<BotsAvailableList> owned_list;
	if (!database.botdb.LoadBotsList(owner->CharacterID(), owned_list) || owned_list.empty()) {
		owner->Message(Chat::White, "You do not own any bots.");
		return;
	}

	std::vector<BotRaidRosterRecord> records;
	for (const auto& bot : owned_list) {
		BotRaidRosterRecord record;
		record.bot_id = bot.bot_id;
		record.raid_group = 255;
		record.role = RaidRoleAuto;
		record.active = 1;
		records.push_back(record);
	}

	if (!database.botdb.ReplaceRaidRoster(owner->CharacterID(), records)) {
		owner->Message(Chat::White, "Could not save the bot raid roster.");
		return;
	}

	Form(owner, false, false);
}

void FormOnConnect(Client* owner)
{
	if (!owner || entity_list.GetRaidByClient(owner)) {
		return;
	}

	std::vector<BotRaidRosterRecord> records;
	if (!database.botdb.LoadRaidRoster(owner->CharacterID(), records)) {
		return;
	}

	for (const auto& record : records) {
		if (record.active) {
			Form(owner, false, true);
			return;
		}
	}
}

void Scatter(Client* owner, float radius)
{
	if (!owner) {
		return;
	}

	if (radius < 5.0f) {
		radius = 5.0f;
	}
	else if (radius > 200.0f) {
		radius = 200.0f;
	}

	const float tank_radius = radius < 15.0f ? radius : 15.0f;
	std::vector<Bot*> tanks;
	std::vector<Bot*> others;

	for (auto* bot : SpawnedOwned(owner)) {
		if (IsTankClass(bot->GetClass())) {
			tanks.push_back(bot);
		}
		else {
			others.push_back(bot);
		}
	}

	PlaceOnRing(tanks, owner->GetPosition(), tank_radius);
	PlaceOnRing(others, owner->GetPosition(), radius);
	owner->Message(
		Chat::White,
		fmt::format("Bots scattering. Tanks at {:.0f}, everyone else at {:.0f}.", tank_radius, radius).c_str()
	);
}

void Stack(Client* owner)
{
	if (!owner) {
		return;
	}

	for (auto* bot : SpawnedOwned(owner)) {
		bot->SetGuardFlag(false);
	}

	owner->Message(Chat::White, "Bots are stacking on you.");
}

void Stand(Client* owner, const std::string& who, bool clear)
{
	if (!owner) {
		return;
	}

	std::string token = Normalize(who.c_str());
	if (Strings::BeginsWith(token, "all ")) {
		token = token.substr(4);
	}

	int group_number = -1;
	uint8 role = RaidRoleAuto;
	uint8 class_id = Class::None;

	if (Strings::BeginsWith(token, "group ")) {
		group_number = Strings::ToInt(token.substr(6));
		if (group_number < 1 || group_number > MAX_RAID_GROUPS) {
			owner->Message(Chat::White, "Use a raid group from 1 to 12.");
			return;
		}
	}
	else {
		role = RoleFromToken(token);
		if (role == RaidRoleAuto) {
			class_id = ClassFromToken(token);
		}

		if (role == RaidRoleAuto && !class_id) {
			owner->Message(Chat::White, "Name a raid group, role, or class. Example: ^stand group 1");
			return;
		}
	}

	Raid* raid = entity_list.GetRaidByClient(owner);
	if (group_number > 0 && !raid) {
		owner->Message(Chat::White, "Form a raid before placing a group.");
		return;
	}

	std::vector<Bot*> picked;
	for (auto* bot : SpawnedOwned(owner)) {
		if (group_number > 0 && raid->GetGroup(bot->GetName()) != static_cast<uint32>(group_number - 1)) {
			continue;
		}

		if (role != RaidRoleAuto && ResolveRole(bot->GetClass(), RaidRoleAuto) != role) {
			continue;
		}

		if (class_id && bot->GetClass() != class_id) {
			continue;
		}

		picked.push_back(bot);
	}

	if (picked.empty()) {
		owner->Message(Chat::White, "No spawned bots matched.");
		return;
	}

	if (clear) {
		for (auto* bot : picked) {
			bot->SetGuardFlag(false);
		}
		owner->Message(Chat::White, fmt::format("{} bots released.", picked.size()).c_str());
		return;
	}

	PlaceOnRing(picked, owner->GetPosition(), 8.0f);
	owner->Message(Chat::White, fmt::format("{} bots moving onto that spot.", picked.size()).c_str());
}

void SetRezEnabled(Client* owner, bool enabled)
{
	if (!owner) {
		return;
	}

	auto& state = State(owner->CharacterID());
	state.rez_enabled = enabled;

	if (enabled) {
		state.heal_tanks = false;
		owner->Message(Chat::White, "Rezzing is on. Out of combat, clerics will rez the fallen.");
		return;
	}

	state.heal_tanks = true;
	state.heal_focus_name.clear();
	StopRezzes(owner);
	owner->Message(Chat::White, "Rezzing is off. Healers will keep the tanks up.");
}

void RezMe(Client* owner)
{
	if (!owner) {
		return;
	}

	Corpse* corpse = entity_list.GetCorpseByOwner(owner);
	if (!corpse) {
		owner->Message(Chat::White, "You have no corpse here.");
		return;
	}

	if (corpse->IsRezzed()) {
		owner->Message(Chat::White, "That corpse already has a resurrection pending.");
		return;
	}

	if (corpse->IsRezClaimedByOther(0)) {
		owner->Message(Chat::White, "A resurrection is already coming for your corpse.");
		return;
	}

	std::vector<Bot*> clerics;
	std::vector<Bot*> druids;
	for (auto* bot : SpawnedOwned(owner)) {
		if (!bot || bot->GetHP() <= 0) {
			continue;
		}

		if (bot->GetClass() == Class::Cleric) {
			clerics.push_back(bot);
		}
		else if (bot->GetClass() == Class::Druid) {
			druids.push_back(bot);
		}
	}

	const std::vector<Bot*>& pool = clerics.empty() ? druids : clerics;
	Bot* healer = NearestRezzer(owner, corpse, pool);
	if (!healer || !StartRez(owner, healer, corpse)) {
		owner->Message(Chat::White, "No cleric or druid is close enough to your corpse.");
		return;
	}

	owner->Message(Chat::White, fmt::format("{} is resurrecting you.", healer->GetCleanName()).c_str());
}

void RezRaid(Client* owner)
{
	if (!owner) {
		return;
	}

	const int before = static_cast<int>(State(owner->CharacterID()).claims.size());
	AssignRezzes(owner);
	const int started = static_cast<int>(State(owner->CharacterID()).claims.size()) - before;
	owner->Message(Chat::White, fmt::format("{} resurrection{} started.", started, started == 1 ? "" : "s").c_str());
}

void HealTanks(Client* owner)
{
	SetRezEnabled(owner, false);
}

void Offtank(Client* owner)
{
	if (!owner) {
		return;
	}

	Mob* target = owner->GetTarget();
	if (!target || !target->IsNPC() || target->GetHP() <= 0) {
		owner->Message(Chat::White, "Target the add you want offtanked.");
		return;
	}

	std::vector<Bot*> tanks;
	Raid* raid = entity_list.GetRaidByClient(owner);
	for (auto* bot : SpawnedOwned(owner)) {
		if (IsTankClass(bot->GetClass())) {
			tanks.push_back(bot);
		}
	}

	if (tanks.empty()) {
		owner->Message(Chat::White, "You have no tank bots spawned.");
		return;
	}

	std::sort(tanks.begin(), tanks.end(), [raid](Bot* left, Bot* right) {
		const uint32 left_group = raid ? raid->GetGroup(left->GetName()) : 0;
		const uint32 right_group = raid ? raid->GetGroup(right->GetName()) : 0;
		return left_group < right_group;
	});

	Bot* offtank = tanks.size() > 1 ? tanks.back() : tanks.front();
	offtank->SetAttackFlag(false);
	offtank->WipeHateList();
	offtank->AddToHateList(target, 5000);
	offtank->SetTarget(target);

	auto& state = State(owner->CharacterID());
	state.offtank_bot_id = offtank->GetBotID();
	state.offtank_entity_id = target->GetID();
	owner->Message(
		Chat::White,
		fmt::format("{} is offtanking {}.", offtank->GetCleanName(), target->GetCleanName()).c_str()
	);
}

void SetMez(Client* owner, bool enabled)
{
	if (!owner) {
		return;
	}

	State(owner->CharacterID()).mez_adds = enabled;
	owner->Message(Chat::White, enabled ? "Enchanters will mez adds." : "Add mez is off.");
}

void Burn(Client* owner, bool enabled)
{
	if (!owner) {
		return;
	}

	int changed = 0;
	for (auto* bot : SpawnedOwned(owner)) {
		if (!IsDpsClass(bot->GetClass())) {
			continue;
		}

		bot->SetBotStance(enabled ? Stance::Burn : Stance::Balanced);
		++changed;
	}

	owner->Message(
		Chat::White,
		fmt::format("{} damage dealers {}.", changed, enabled ? "are burning" : "are holding their burn").c_str()
	);
}

void Hold(Client* owner, bool enabled)
{
	if (!owner) {
		return;
	}

	for (auto* bot : SpawnedOwned(owner)) {
		bot->SetHoldFlag(enabled);
		if (!enabled) {
			bot->SetGuardFlag(false);
			bot->Stand();
		}
	}

	owner->Message(Chat::White, enabled ? "Bots are holding." : "Bots are following.");
}

void ClericsOn(Client* owner, const std::string& name)
{
	if (!owner) {
		return;
	}

	const std::string token = Normalize(name.c_str());
	Mob* target = ResolveNamedMob(owner, token);
	if (!target) {
		owner->Message(Chat::White, fmt::format("Nobody named '{}' is here.", token).c_str());
		return;
	}

	State(owner->CharacterID()).heal_focus_name = token;
	owner->Message(Chat::White, fmt::format("Clerics are focusing {}.", target->GetCleanName()).c_str());
}

void MarkCamp(Client* owner)
{
	if (!owner) {
		return;
	}

	auto& state = State(owner->CharacterID());
	state.camp = owner->GetPosition();
	state.camp_set = true;
	owner->Message(Chat::White, "Camp marked. Say back to camp to return here.");
}

void BackToCamp(Client* owner)
{
	if (!owner) {
		return;
	}

	auto& state = State(owner->CharacterID());
	if (!state.camp_set) {
		owner->Message(Chat::White, "No camp is marked.");
		return;
	}

	PlaceOnRing(SpawnedOwned(owner), state.camp, 8.0f);
	owner->Message(Chat::White, "Bots are returning to camp.");
}

void Pull(Client* owner)
{
	if (!owner) {
		return;
	}

	Mob* target = owner->GetTarget();
	if (!target || !target->IsNPC()) {
		owner->Message(Chat::White, "Target the creature you want pulled.");
		return;
	}

	if (!target->GetHateList().empty()) {
		owner->Message(Chat::White, "That target is already engaged.");
		return;
	}

	const uint8 preferred[] = {Class::Monk, Class::Bard, Class::Ranger};
	Bot* puller = nullptr;

	for (uint8 class_id : preferred) {
		for (auto* bot : SpawnedOwned(owner)) {
			if (bot->GetClass() == class_id) {
				puller = bot;
				break;
			}
		}

		if (puller) {
			break;
		}
	}

	if (!puller) {
		for (auto* bot : SpawnedOwned(owner)) {
			if (IsTankClass(bot->GetClass())) {
				puller = bot;
				break;
			}
		}
	}

	if (!puller) {
		owner->Message(Chat::White, "No monk, bard, ranger, or tank is spawned to pull.");
		return;
	}

	for (auto* bot : SpawnedOwned(owner)) {
		if (bot != puller) {
			bot->SetPullFlag(false);
		}
	}

	puller->SetPullFlag(true);
	owner->Message(Chat::White, fmt::format("{} is pulling.", puller->GetCleanName()).c_str());
}

void Evac(Client* owner)
{
	if (!owner) {
		return;
	}

	Raid* raid = entity_list.GetRaidByClient(owner);
	std::unordered_map<uint32, std::pair<Bot*, uint16>> caster_for_group;
	int started = 0;

	for (auto* bot : SpawnedOwned(owner)) {
		if (!bot || bot->IsCasting() || (bot->GetClass() != Class::Druid && bot->GetClass() != Class::Wizard)) {
			continue;
		}

		auto available = Bot::GetBotSpellsForSpellEffect(bot, BotSpellTypes::Succor, SpellEffect::Succor);
		if (available.empty()) {
			continue;
		}

		uint32 group = raid ? raid->GetGroup(bot->GetName()) : 0;
		if (group >= MAX_RAID_GROUPS) {
			group = 0;
		}

		auto existing = caster_for_group.find(group);
		if (existing == caster_for_group.end() || (bot->GetClass() == Class::Druid && existing->second.first->GetClass() != Class::Druid)) {
			caster_for_group[group] = {bot, available.front().SpellId};
		}
	}

	for (const auto& [group, caster] : caster_for_group) {
		if (caster.first->CastSpell(caster.second, caster.first->GetID())) {
			++started;
		}
	}

	if (!started) {
		owner->Message(Chat::White, "No druid or wizard has evac ready.");
		return;
	}

	owner->Message(Chat::White, fmt::format("{} group{} evacuating.", started, started == 1 ? " is" : "s are").c_str());
}

void Sit(Client* owner)
{
	if (!owner) {
		return;
	}

	for (auto* bot : SpawnedOwned(owner)) {
		bot->GuardAt(bot->GetPosition());
		bot->SetHoldFlag(true);
		bot->Sit();
	}

	owner->Message(Chat::White, "Bots are sitting. Say go when you want them to follow.");
}

void Taunt(Client* owner, bool enabled)
{
	if (!owner) {
		return;
	}

	int changed = 0;
	for (auto* bot : SpawnedOwned(owner)) {
		if (!IsTankClass(bot->GetClass())) {
			continue;
		}

		bot->SetTaunting(enabled);
		++changed;
	}

	owner->Message(Chat::White, fmt::format("{} tanks {} taunting.", changed, enabled ? "are" : "stopped").c_str());
}

void Behind(Client* owner)
{
	if (!owner) {
		return;
	}

	for (auto* bot : SpawnedOwned(owner)) {
		bot->SetBehindMob(true);
	}

	owner->Message(Chat::White, "Bots will try to stay behind their target.");
}

bool HandlePhrase(Client* owner, const char* message)
{
	if (!owner || !message || !message[0] || message[0] == '^' || message[0] == '#') {
		return false;
	}

	const std::string text = Normalize(message);
	if (text.empty()) {
		return false;
	}

	const std::string stand_suffix = " stand here";
	if (text.size() > stand_suffix.size() && text.compare(text.size() - stand_suffix.size(), stand_suffix.size(), stand_suffix) == 0) {
		Stand(owner, text.substr(0, text.size() - stand_suffix.size()), false);
		return true;
	}

	if (text == "form raid") {
		Form(owner, false, false);
	}
	else if (text == "follow") {
		Hold(owner, false);
	}
	else if (text == "guard") {
		for (auto* bot : SpawnedOwned(owner)) {
			bot->SetGuardMode();
		}
		owner->Message(Chat::White, "Bots are guarding here.");
	}
	else if (text == "attack" || text == "assist me") {
		if (!owner->GetTarget()) {
			owner->Message(Chat::White, "Target something first.");
			return true;
		}

		for (auto* bot : SpawnedOwned(owner)) {
			if (IsOfftank(bot)) {
				continue;
			}

			bot->SetOwnerTarget(owner);
			bot->SetAttackFlag(true);
		}
		owner->Message(Chat::White, "Bots are assisting you.");
	}
	else if (text == "camp") {
		Camp(owner);
	}
	else if (text == "scatter") {
		Scatter(owner, 60.0f);
	}
	else if (text == "stack") {
		Stack(owner);
	}
	else if (text == "rez me") {
		RezMe(owner);
	}
	else if (text == "rez the raid") {
		RezRaid(owner);
	}
	else if (text == "heal tanks") {
		HealTanks(owner);
	}
	else if (text == "rez") {
		SetRezEnabled(owner, true);
	}
	else if (text == "offtank") {
		Offtank(owner);
	}
	else if (text == "mez") {
		SetMez(owner, true);
	}
	else if (text == "mez off") {
		SetMez(owner, false);
	}
	else if (text == "burn") {
		Burn(owner, true);
	}
	else if (text == "burn off") {
		Burn(owner, false);
	}
	else if (text == "hold") {
		Hold(owner, true);
	}
	else if (text == "go") {
		Hold(owner, false);
	}
	else if (text == "clerics on me") {
		ClericsOn(owner, "me");
	}
	else if (Strings::BeginsWith(text, "clerics on ")) {
		ClericsOn(owner, text.substr(11));
	}
	else if (text == "mark camp") {
		MarkCamp(owner);
	}
	else if (text == "back to camp") {
		BackToCamp(owner);
	}
	else if (text == "pull") {
		Pull(owner);
	}
	else if (text == "evac") {
		Evac(owner);
	}
	else if (text == "sit") {
		Sit(owner);
	}
	else if (text == "taunt") {
		Taunt(owner, true);
	}
	else if (text == "taunt off") {
		Taunt(owner, false);
	}
	else if (text == "behind") {
		Behind(owner);
	}
	else {
		return false;
	}

	return true;
}

void Tick(Client* owner)
{
	if (!owner) {
		return;
	}

	auto& state = State(owner->CharacterID());
	const uint32 now = Timer::GetCurrentTime();
	if (state.last_tick != 0 && now < state.last_tick + 500) {
		return;
	}

	state.last_tick = now;
	WatchRezClaims(owner);

	if (!state.rez_enabled || now < state.last_assign + 2000) {
		return;
	}

	bool engaged = owner->IsEngaged();
	if (!engaged) {
		for (auto* bot : SpawnedOwned(owner)) {
			if (bot->IsEngaged()) {
				engaged = true;
				break;
			}
		}
	}

	if (engaged) {
		return;
	}

	state.last_assign = now;
	AssignRezzes(owner);
}

void ApplyOfftank(Bot* bot)
{
	if (!bot) {
		return;
	}

	Client* owner = bot->GetBotOwner() && bot->GetBotOwner()->IsClient() ? bot->GetBotOwner()->CastToClient() : nullptr;
	if (!owner) {
		return;
	}

	auto& state = State(owner->CharacterID());
	if (!state.offtank_bot_id || bot->GetBotID() != state.offtank_bot_id) {
		return;
	}

	Mob* target = entity_list.GetMob(state.offtank_entity_id);
	if (!target || target->IsCorpse() || target->GetHP() <= 0) {
		state.offtank_bot_id = 0;
		state.offtank_entity_id = 0;
		return;
	}

	if (bot->GetTarget() != target) {
		bot->AddToHateList(target, 5000);
		bot->SetTarget(target);
	}
}

bool TryPriorityHeal(Bot* bot)
{
	if (!bot || bot->IsCasting() || bot->GetHP() <= 0) {
		return false;
	}

	const uint8 class_id = bot->GetClass();
	if (class_id != Class::Cleric && class_id != Class::Druid) {
		return false;
	}

	Client* owner = bot->GetBotOwner() && bot->GetBotOwner()->IsClient() ? bot->GetBotOwner()->CastToClient() : nullptr;
	if (!owner) {
		return false;
	}

	auto& state = State(owner->CharacterID());
	Mob* focus = nullptr;

	if (!state.heal_focus_name.empty() && class_id == Class::Cleric) {
		focus = ResolveNamedMob(owner, state.heal_focus_name);
	}
	else if (state.heal_tanks) {
		focus = LowestTank(owner);
	}

	if (!focus || focus->GetHP() <= 0 || focus->GetHPRatio() > 90.0f) {
		return false;
	}

	if (bot->AttemptAICastSpell(BotSpellTypes::FastHeals, focus)) {
		return true;
	}

	return bot->AttemptAICastSpell(BotSpellTypes::RegularHeal, focus);
}

bool IsOfftank(Bot* bot)
{
	if (!bot) {
		return false;
	}

	Client* owner = bot->GetBotOwner() && bot->GetBotOwner()->IsClient() ? bot->GetBotOwner()->CastToClient() : nullptr;
	if (!owner) {
		return false;
	}

	const auto& state = State(owner->CharacterID());
	return state.offtank_bot_id && bot->GetBotID() == state.offtank_bot_id;
}

bool AllowMezTarget(Bot* caster, Mob* npc)
{
	if (!caster || !npc) {
		return true;
	}

	Client* owner = caster->GetBotOwner() && caster->GetBotOwner()->IsClient() ? caster->GetBotOwner()->CastToClient() : nullptr;
	if (!owner) {
		return true;
	}

	const auto& state = State(owner->CharacterID());
	if (!state.mez_adds) {
		return true;
	}

	if (owner->GetTarget() == npc) {
		return false;
	}

	Mob* offtank_target = state.offtank_entity_id ? entity_list.GetMob(state.offtank_entity_id) : nullptr;
	return offtank_target != npc;
}

void CompleteBotCorpseRez(Corpse* corpse, Mob* caster)
{
	if (!corpse || !corpse->IsBotCorpse() || corpse->IsRezzed()) {
		return;
	}

	corpse->IsRezzed(true);

	const uint32 bot_id = corpse->GetBotCorpseID();
	const uint32 owner_id = corpse->GetBotCorpseOwnerID();
	const glm::vec4 position = corpse->GetPosition();
	const uint16 corpse_id = corpse->GetID();
	Client* owner = entity_list.GetClientByCharID(owner_id);

	auto fail = [&]() {
		corpse->IsRezzed(false);
		corpse->ClearRezClaim();
	};

	if (!owner) {
		fail();
		return;
	}

	Mob* existing = entity_list.GetMobByBotID(bot_id);
	if (existing && existing->IsBot()) {
		corpse->ClearRezClaim();
		ForgetCorpse(State(owner_id), corpse_id);
		corpse->DepopNPCCorpse();
		return;
	}

	Bot* loaded = Bot::LoadBot(bot_id);
	if (!loaded || loaded->GetBotOwnerCharacterID() != owner_id) {
		safe_delete(loaded);
		fail();
		return;
	}

	if (!loaded->Spawn(owner, true, &position)) {
		safe_delete(loaded);
		fail();
		return;
	}

	corpse->ClearRezClaim();
	ForgetCorpse(State(owner_id), corpse_id);
	if (caster && caster->IsClient()) {
		caster->Message(Chat::White, fmt::format("{} is back on their feet.", loaded->GetCleanName()).c_str());
	}
	else if (owner) {
		owner->Message(Chat::White, fmt::format("{} is back on their feet.", loaded->GetCleanName()).c_str());
	}

	corpse->DepopNPCCorpse();
}

} // namespace BotRaidRoster
