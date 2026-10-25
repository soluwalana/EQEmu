#pragma once

#include <string>

class Bot;
class Client;
class Corpse;
class Mob;

// Owner-scoped raid layout and the in-memory orders that sit on top of it.
// Camp, rez claims, and stand positions are forgotten when the owner zones.
namespace BotRaidRoster {

void Form(Client* c, bool reset, bool quiet);
void Save(Client* c);
void Clear(Client* c);
void Camp(Client* c);
void ReplaceWithAll(Client* c);
void FormOnConnect(Client* c);

void Scatter(Client* c, float radius);
void Stack(Client* c);
void Stand(Client* c, const std::string& who, bool clear);

void SetRezEnabled(Client* c, bool enabled);
void RezMe(Client* c);
void RezRaid(Client* c);
void HealTanks(Client* c);

void Offtank(Client* c);
void SetMez(Client* c, bool enabled);
void Burn(Client* c, bool enabled);
void Hold(Client* c, bool enabled);
void ClericsOn(Client* c, const std::string& name);
void MarkCamp(Client* c);
void BackToCamp(Client* c);
void Pull(Client* c);
void Evac(Client* c);
void Sit(Client* c);
void Taunt(Client* c, bool enabled);
void Behind(Client* c);

bool HandlePhrase(Client* c, const char* message);

void RegisterBotCorpse(uint32 owner_id, uint16 corpse_id);
void Tick(Client* owner);
void ApplyOfftank(Bot* bot);
bool TryPriorityHeal(Bot* bot);
bool IsOfftank(Bot* bot);
bool AllowMezTarget(Bot* caster, Mob* npc);
void Forget(uint32 character_id);
void CompleteBotCorpseRez(Corpse* corpse, Mob* caster);

}
