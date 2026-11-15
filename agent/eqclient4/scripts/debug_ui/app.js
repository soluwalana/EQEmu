'use strict';
const $ = id => document.getElementById(id), esc = v => String(v ?? '—').replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
const cls = ['—', 'Warrior', 'Cleric', 'Paladin', 'Ranger', 'Shadowknight', 'Druid', 'Monk', 'Bard', 'Rogue', 'Shaman', 'Necromancer', 'Wizard', 'Magician', 'Enchanter', 'Beastlord', 'Berserker'];
const pretty = v => JSON.stringify(v, null, 2), num = v => Number.isFinite(Number(v)) && v !== null ? Number(v).toFixed(1) : '—';
// Preserve entity category hues, desaturate only confirmed blocked entities.
// Unknown is deliberately neutral, not a claim that a ray was obstructed.
function entityTint(entity, bot = false) {
    const bright = bot ? [108,204,145] : entity.aggro ? [236,119,132] : [223,187,119];
    if (entity.los === true) return bright;
    if (entity.los === false) {
        const gray = 125;
        return bright.map(v => Math.round(gray + (v - gray) * .32));
    }
    return [122,130,143];
}
function entityColor(entity, bot = false) { return `rgb(${entityTint(entity, bot).join(',')})`; }
function losLabel(entity) { return entity.los === true ? (state?.los_map === false ? 'LoS assumed clear (no collision map)' : 'In LoS') : entity.los === false ? 'Out of LoS' : 'LoS unknown'; }
let state = null, tab = 'overview', selectedMob = null, selectedSlot = null, openBag = null, actionCatalog = new Map(), activeAction = null, lastInventory = '', mapHits = new Map(), selectedItem = null, paramReaders = [], actionGeneration = 0;
const logs = { wire: { after: -1, rows: [], paused: false, busy: false }, combat: { after: -1, rows: [], paused: false, busy: false } };
async function api(path, options = {}) { const r = await fetch(path, { cache: 'no-store', ...options }); if (!r.ok) {
    let x;
    try {
        x = await r.json();
    }
    catch {
        x = await r.text();
    }
    throw Error(typeof x.detail === 'string' ? x.detail : JSON.stringify(x.detail ?? x));
} return r.json(); }
const post = (path, body, method = 'POST') => api(path, { method, headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(body) });
const htmlCache = new WeakMap();
function text(id, v) { const el = $(id); const value = String(v ?? '—'); if (el.textContent !== value)
    el.textContent = value; htmlCache.delete(el); }
function html(id, v) { const el = $(id); if (htmlCache.get(el) !== v) {
    el.innerHTML = v;
    htmlCache.set(el, v);
} }
function status(msg, ok) { text('status', msg); $('status').className = 'pill ' + (ok ? 'good' : 'bad'); }
function setTab(name) { tab = name; document.querySelectorAll('.tab').forEach(e => e.classList.toggle('active', e.id === name)); document.querySelectorAll('nav button').forEach(e => e.classList.toggle('active', e.dataset.tab === name)); if (state)
    render(); if (name === 'actions' && !actionCatalog.size)
    loadActions(); if (name === 'logs') {
    renderLog('wire');
    renderLog('combat');
} }
document.querySelectorAll('nav button').forEach(e => e.onclick = () => setTab(e.dataset.tab));
function bar(label, val, max, kind, pct) { const p = pct ?? (max > 0 ? 100 * val / max : null); return `<div class="resource"><div class="line"><span>${esc(label)}</span><b>${esc(val)}${max > 0 ? ' / ' + esc(max) : ''}${p !== null ? ' · ' + Math.round(p) + '%' : ''}</b></div><div class="track"><div class="fill ${kind}" style="width:${Math.max(0, Math.min(100, p ?? 0))}%"></div></div></div>`; }
function mini(v, kind) { return v == null ? '—' : `${esc(v)}%<div class="track"><div class="fill ${kind}" style="width:${Math.max(0, Math.min(100, Number(v) || 0))}%"></div></div>`; }
function render() {
    if (!state)
        return;
    const s = state, c = s.character;
    text('zonehead', `${s.zone ?? '—'} · ${s.zone_id}`);
    text('metrics', `Tick ${s.tick.toLocaleString()}  ·  ↑ ${s.sent.toLocaleString()}  ↓ ${s.received.toLocaleString()}  ·  ${s.mobs.length} entities`);
    status(s.ready ? 'Connected' : 'Zone not ready', s.ready);
    if (tab === 'overview') {
        text('charname', c.name);
        text('charlevel', `Lv ${c.level} · ${c.race_name} ${c.class_name}`);
        html('resources', bar('Health', c.hp, c.max_hp, '', c.hp_percent ?? undefined) + bar('Mana', c.mana, c.max_mana, 'mana') + bar('Endurance', c.endurance, c.max_endurance, 'endurance'));
        html('attributes', [['STR', c.strength], ['STA', c.stamina], ['AGI', c.agility], ['DEX', c.dexterity], ['WIS', c.wisdom], ['INT', c.intelligence], ['CHA', c.charisma], ['AA', c.aa_points], ['XP', c.exp], ['AA spent', c.aa_points_spent], ['Food', c.food], ['Water', c.water]].map(([k, v]) => `<div class="stat"><span>${k}</span><b>${esc(v)}</b></div>`).join(''));
        text('coins', (c.coin ?? []).map((v, i) => `${v} ${['pp', 'gp', 'sp', 'cp'][i]}`).join(' · '));
        text('party', s.party_mode ?? 'Solo');
        text('position', `X ${num(s.position[0])}  Y ${num(s.position[1])}  Z ${num(s.position[2])}  H ${num(s.heading)} / 512`);
        draw('minimap', fitBotRadius(200));
        renderBots();
        renderNearby();
        renderQueue();
    }
    if (tab === 'overview') {
        renderInventory();
        renderBuffs();
    }
    if (tab === 'inventory')
        renderInventory();
    if (tab === 'world') {
        text('worldzone', `${s.zone} · instance ${s.instance}`);
        draw('worldmap', Number($('radius').value));
        renderMobs();
        text('pathdetail', s.path ? pretty(s.path) : 'No active path.');
        if (selectedMob !== null) {
            let m = s.mobs.find(x => x.id === selectedMob) || s.bots.find(x => x.id === selectedMob && x.spawned);
            text('mobdetail', m ? pretty(m) : 'Entity is no longer present.');
            $('mobaction').disabled = !m;
        }
    }
    if (tab === 'actions')
        renderRuns();
}
function renderBuffs() { const c = state.character, buffs = Object.values(c.buffs ?? {}); html('buffs', buffs.slice(0, 18).map(b => `<div class="row"><span>Spell #${esc(b.spell_id ?? b.spellid ?? '—')}</span><span class="muted">${esc(b.duration ?? b.tics_remaining ?? '')} ticks</span></div>`).join('') || '<p class="muted">No tracked buffs.</p>'); }
function botSpawnLabel(b) {
    if (!b.spawned)
        return 'Not spawned';
    return b.id > 0 ? `Spawn #${b.id}` : 'Spawn ID unknown';
}
function renderBots() {
    const bots = state.bots;
    text('botcount', `${bots.filter(b => b.spawned).length} / ${bots.length} spawned`);
    html('bots', bots.map(b => {
        const name = b.spawned && b.id > 0
            ? `<button class="bot-link" data-mob="${b.id}" title="Locate ${esc(b.name)} on the world map">${esc(b.name)}</button>`
            : `<b>${esc(b.name)}</b>`;
        return `<tr><td>${name}<div class="dim">${esc(botSpawnLabel(b))} · Lv ${b.level}</div></td><td>${esc(cls[b.class_id])}</td><td class="${b.spawned ? (b.alive ? 'goodtext' : 'danger') : 'dim'}">${b.spawned ? (b.alive ? (b.grouped ? 'Grouped' : 'Spawned') : 'Dead') : 'Offline'}</td><td>${b.spawned ? mini(b.hp, '') : '—'}</td><td>${b.spawned ? mini(b.mana, 'mana') : '—'}</td><td>${b.spawned ? mini(b.endurance, 'endurance') : '—'}</td><td>${b.spawned ? num(b.distance) + ' yd' : '—'}</td></tr>`;
    }).join(''));
}
function mobButton(m) { return `<button data-mob="${m.id}"><span>${esc(m.name)} <small>${m.bot ? 'Bot · ' : ''}Lv ${m.level}</small></span><span class="${m.aggro ? 'danger' : 'dim'}">${m.dead ? 'Dead' : num(m.distance) + ' yd'} · ${esc(m.hp)}%</span></button>`; }
function renderNearby() { const m = state.mobs.filter(x => x.distance <= 200 && !x.dead); text('mobcount', `${m.length} within 200 yd`); html('nearby', m.slice(0, 30).map(mobButton).join('') || '<p class="muted">No nearby entities.</p>'); }
function renderQueue() { const a = state.actions, cur = a.queue.find(x => x.insert === a.active); html('current', cur ? `<div class="activecard"><strong>${esc(cur.class_name)}</strong><p>Priority ${cur.priority} · #${cur.insert}</p><p>Waiting: ${esc((cur.waiting ?? []).join(', ') || '—')}</p><p>${esc(cur.source || 'Manual action')} · ${esc(cur.zone)}</p></div>` : '<div class="activecard"><strong>Idle</strong><p>No active action</p></div>'); html('queue', a.queue.map(x => `<div class="row"><b>${esc(x.class_name)}</b><span class="muted">${x.priority} · ${esc((x.waiting ?? []).join(', ') || 'ready')}</span></div>`).join('') || '<p class="muted">Queue empty.</p>'); $('queue').className = 'list'; }
function renderMobs() {
    const q = $('mobquery').value.toLowerCase(), near = $('onlynear').checked;
    const entities = [...state.mobs, ...state.bots.filter(b => b.spawned && b.id > 0).map(b => ({ ...b, bot: true, dead: !b.alive }))];
    const rows = entities.filter(m => (!q || m.name.toLowerCase().includes(q) || (m.raw_name ?? m.name).toLowerCase().includes(q) || String(m.id) === q) && (!near || m.distance <= 200)).sort((a, b) => a.distance - b.distance);
    html('moblist', rows.slice(0, 500).map(mobButton).join('') + `<p class="muted">${Math.min(rows.length, 500)} of ${rows.length} matches</p>`);
}
function validPosition(point) {
    return Array.isArray(point) && point.length >= 2 && Number.isFinite(point[0]) && Number.isFinite(point[1]);
}
function fitBotRadius(minimum) {
    const p = state.position;
    const farthest = Math.max(0, ...state.bots.filter(b => b.spawned && validPosition(b.position)).map(b => Math.hypot(b.position[0] - p[0], b.position[1] - p[1], (b.position[2] ?? p[2]) - p[2])));
    return Math.max(minimum, Math.ceil(farthest * 1.15 / 25) * 25);
}
function inspectMob(id, openWorld = true) {
    // Selection is not a camera command. A marker click stays on its map;
    // list clicks may open the World inspector, but never resize either map.
    selectedMob = id;
    if (openWorld && tab !== 'world')
        setTab('world');
    else if (state)
        render();
}
$('nearby').onclick = $('moblist').onclick = $('bots').onclick = e => {
    const b = e.target.closest('[data-mob]');
    if (b)
        inspectMob(Number(b.dataset.mob));
};
$('mobquery').oninput = $('onlynear').onchange = () => state && renderMobs();

// Separate display markers in screen space. Their anchor coordinates never
// change: a thin leader connects each displaced marker to its real position.
// Reserving the player footprint keeps following bots from disappearing
// underneath the heading arrow, including when every bot is on the same point.
function layoutBotMarkers(bots, project, width, height, radius, player = [width / 2, height / 2]) {
    const markers = [], gap = 2 * radius + 5;
    const inside = (x, y) => x >= radius + 2 && x <= width - radius - 2 && y >= radius + 2 && y <= height - radius - 2;
    const free = (x, y) => inside(x, y)
        && Math.hypot(x - player[0], y - player[1]) >= 14 + radius + 3
        && markers.every(m => Math.hypot(x - m.x, y - m.y) >= gap);
    for (const bot of bots.filter(b => b.spawned && validPosition(b.position)).sort((a, b) => a.id - b.id || a.name.localeCompare(b.name))) {
        const [ax, ay] = project(bot.position);
        if (ax < 0 || ax > width || ay < 0 || ay > height)
            continue;
        let x = ax, y = ay;
        if (!free(x, y)) {
            // Try progressively larger rings, keeping the marker close to
            // the anchor. Stable ordering avoids arbitrary per-frame jitter.
            let found = false;
            for (let ring = 1; ring <= Math.ceil(Math.hypot(width, height) / gap) && !found; ring++) {
                const distance = ring * gap, n = Math.max(8, Math.ceil(2 * Math.PI * distance / gap));
                for (let i = 0; i < n; i++) {
                    const angle = -Math.PI / 2 + 2 * Math.PI * i / n;
                    const nx = ax + Math.cos(angle) * distance, ny = ay + Math.sin(angle) * distance;
                    if (free(nx, ny)) {
                        x = nx;
                        y = ny;
                        found = true;
                        break;
                    }
                }
            }
            if (!found) {
                x = Math.max(radius + 2, Math.min(width - radius - 2, ax));
                y = Math.max(radius + 2, Math.min(height - radius - 2, ay));
            }
        }
        markers.push({ bot, ax, ay, x, y });
    }
    return markers;
}
function draw(id, radius) {
    if (window.EQMap3D?.draw(id, radius, state, selectedMob, mapHits, layoutBotMarkers))
        return;
    draw2d(id, radius);
}
if (window.EQMap3D) window.EQMap3D.fallback = (id, radius) => draw2d(id, radius);
function draw2d(id, radius) {
    const canvas = $(id), ctx = canvas.getContext('2d'), w = canvas.width, h = canvas.height, s = state, p = s.position, scale = Math.min(w, h) / (2 * radius);
    const xy = pos => [w / 2 + (pos[0] - p[0]) * scale, h / 2 - (pos[1] - p[1]) * scale];
    ctx.clearRect(0, 0, w, h);
    ctx.fillStyle = '#0a111c';
    ctx.fillRect(0, 0, w, h);
    ctx.strokeStyle = '#1d2d40';
    ctx.lineWidth = 1;
    const step = radius > 500 ? Math.max(100, Math.ceil(radius / 500) * 100) : radius > 150 ? 50 : 25;
    for (let x = Math.ceil((p[0] - w / 2 / scale) / step) * step; x < p[0] + w / 2 / scale; x += step) {
        let [sx] = xy([x, p[1]]);
        ctx.beginPath();
        ctx.moveTo(sx, 0);
        ctx.lineTo(sx, h);
        ctx.stroke();
    }
    for (let y = Math.ceil((p[1] - h / 2 / scale) / step) * step; y < p[1] + h / 2 / scale; y += step) {
        let [, sy] = xy([p[0], y]);
        ctx.beginPath();
        ctx.moveTo(0, sy);
        ctx.lineTo(w, sy);
        ctx.stroke();
    }
    ctx.fillStyle = '#8c9caf';
    ctx.font = '12px monospace';
    ctx.fillText('+Y ↑', 12, 20);
    ctx.fillText('+X →', w - 65, h - 12);
    ctx.fillText(`${radius} yd radius`, 12, h - 12);
    if (s.path?.points?.length) {
        ctx.strokeStyle = '#a19bff';
        ctx.lineWidth = 2.5;
        ctx.beginPath();
        s.path.points.forEach((v, i) => { const [x, y] = xy(v); i ? ctx.lineTo(x, y) : ctx.moveTo(x, y); });
        ctx.stroke();
        const [x, y] = xy(s.path.destination);
        ctx.strokeRect(x - 6, y - 6, 12, 12);
        if (s.path.next_point) {
            const [nx, ny] = xy(s.path.next_point);
            ctx.fillStyle = '#a19bff';
            ctx.beginPath();
            ctx.arc(nx, ny, 5, 0, Math.PI * 2);
            ctx.fill();
        }
    }
    const hits = [];
    function marker(m, color, size) { if (!m.position)
        return; const [x, y] = xy(m.position); if (x < 0 || x > w || y < 0 || y > h)
        return; ctx.beginPath(); ctx.arc(x, y, size, 0, Math.PI * 2); ctx.fillStyle = color; ctx.fill(); if (m.id === selectedMob) {
        ctx.strokeStyle = '#fff';
        ctx.lineWidth = 2;
        ctx.stroke();
    } hits.push({ x, y, id: m.id, name: m.name, radius: size, bot: false, los: m.los }); if (id === 'worldmap' && (m.id === selectedMob || m.aggro)) {
        ctx.fillStyle = '#e2e9f3';
        ctx.fillText(m.name, x + 8, y - 7);
    } }
    s.mobs.filter(m => !m.dead).forEach(m => marker(m, entityColor(m), m.aggro ? 5 : 3));
    const botRadius = Math.max(7, 5 * Math.min(2, w / Math.max(1, canvas.clientWidth)));
    const bots = layoutBotMarkers(s.bots, xy, w, h, botRadius);
    // Draw true-position anchors and leaders before the player arrow.
    ctx.lineWidth = 1.2;
    for (const b of bots) {
        ctx.strokeStyle = entityColor(b.bot, true);
        ctx.fillStyle = entityColor(b.bot, true);
        if (Math.hypot(b.x - b.ax, b.y - b.ay) > 1) {
            ctx.beginPath();
            ctx.moveTo(b.ax, b.ay);
            ctx.lineTo(b.x, b.y);
            ctx.stroke();
            ctx.beginPath();
            ctx.arc(b.ax, b.ay, 2, 0, 2 * Math.PI);
            ctx.fill();
        }
    }
    ctx.fillStyle = '#5bc9d5';
    ctx.save();
    ctx.translate(w / 2, h / 2); // EQ heading: 0=+Y, 128=+X. Canvas y is inverted.
    ctx.rotate(s.heading * Math.PI * 2 / 512);
    ctx.beginPath();
    ctx.moveTo(0, -12);
    ctx.lineTo(7, 7);
    ctx.lineTo(0, 4);
    ctx.lineTo(-7, 7);
    ctx.closePath();
    ctx.fill();
    ctx.restore();
    // Bots sit on top of the NPC layer and outside the player footprint.
    for (const b of bots) {
        ctx.beginPath();
        ctx.arc(b.x, b.y, botRadius, 0, 2 * Math.PI);
        ctx.fillStyle = entityColor(b.bot, true);
        ctx.fill();
        ctx.strokeStyle = b.bot.id === selectedMob ? '#fff' : '#102a20';
        ctx.lineWidth = b.bot.id === selectedMob ? 2.5 : 2;
        ctx.stroke();
        ctx.fillStyle = '#103524';
        ctx.font = `bold ${Math.round(botRadius + 2)}px system-ui`;
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillText('B', b.x, b.y);
        ctx.textAlign = 'start';
        ctx.textBaseline = 'alphabetic';
        if (b.bot.id > 0)
            hits.push({ x: b.x, y: b.y, id: b.bot.id, name: b.bot.name, radius: botRadius, bot: true, los: b.bot.los });
        if (b.bot.id === selectedMob) {
            ctx.font = '12px monospace';
            ctx.fillStyle = '#e2e9f3';
            ctx.fillText(b.bot.name, b.x + botRadius + 4, b.y - botRadius - 3);
        }
    }
    const spawned = s.bots.filter(b => b.spawned).length;
    const unknown = s.bots.filter(b => b.spawned && !validPosition(b.position)).length;
    text(id + 'bots', `${bots.length} / ${spawned} spawned bots in view${spawned - bots.length - unknown > 0 ? ` · ${spawned - bots.length - unknown} outside view` : ''}${unknown ? ` · ${unknown} without position` : ''}`);
    mapHits.set(id, hits);
}
function mapHit(id, event) {
    const canvas = $(id), rect = canvas.getBoundingClientRect();
    const x = (event.clientX - rect.left) * canvas.width / rect.width, y = (event.clientY - rect.top) * canvas.height / rect.height;
    const hits = (mapHits.get(id) || []).map(m => ({ ...m, d: Math.hypot(x - m.x, y - m.y) })).sort((a, b) => a.d - b.d);
    // Prefer a visible bot marker over a mob hidden behind it.
    return hits.find(m => m.bot && m.d <= m.radius + 3) ?? hits.find(m => m.d < 15);
}
for (const id of ['minimap', 'worldmap']) {
    const legend = $(id + 'bots').parentElement.querySelector('.legend');
    if (legend) {
        const hint = document.createElement('span');
        hint.textContent = 'Bright: in LoS · muted hue: blocked · slate: unknown';
        legend.append(hint);
    }
    $(id).onclick = e => {
        const hit = mapHit(id, e);
        if (hit)
            inspectMob(hit.id, false);
    };
    $(id).onmousemove = e => {
        const hit = mapHit(id, e);
        $(id).style.cursor = hit ? 'pointer' : 'default';
        $(id).title = hit ? `${hit.name} · Spawn #${hit.id} · ${losLabel(hit)}` : '';
    };
    $(id).onmouseleave = () => { $(id).title = ''; $(id).style.cursor = 'default'; };
}
$('radius').oninput = () => { window.EQMap3D?.resetZoom('worldmap'); text('radiuslabel', $('radius').value + ' yd'); if (state)
    draw('worldmap', Number($('radius').value)); };
function setWorldRadius(radius) {
    $('radius').max = String(Math.max(3000, Math.ceil(radius)));
    $('radius').value = String(Math.ceil(radius));
    $('radius').oninput();
}
$('fitpath').onclick = () => { if (!state?.path)
    return; window.EQMap3D?.resetCamera('worldmap'); const p = state.position; const r = Math.max(50, ...state.path.points.map(v => Math.hypot(v[0] - p[0], v[1] - p[1], (v[2] ?? p[2]) - p[2]))) * 1.15; setWorldRadius(r); };
$('fitbots').onclick = () => { if (state) {
    window.EQMap3D?.resetCamera('worldmap'); setWorldRadius(fitBotRadius(50)); } };
// Original EQ character-sheet arrangement, not numerical inventory order.
// A blank at upper left preserves the staggered first row in the reference.
// Each number is a native RoF2 worn slot (constants._WORN).
const EQUIPMENT_LAYOUT = [
    null, 1, 5, 3, 2, 4,
    15, 6, 9, 12, 10, 16,
    7, 17, 8, 20, 18, 19,
    13, 14, 11, 22, 0, 21,
];
const addressKey = a => `${a.type}:${a.main_slot}:${a.sub_index}:${a.aug_index}`;
function slotButton(a, label, entry) { const i = entry?.item, key = addressKey(a); return `<button class="slot ${i ? '' : 'empty'} ${selectedSlot === key ? 'selected' : ''}" data-slot="${key}" title="${esc(i?.name ?? label)}"><span class="slotname">${esc(label)}</span><span class="itemname">${esc(i?.name ?? 'Empty')}</span>${i?.stack > 1 ? `<span class="stack">×${i.stack}</span>` : ''}</button>`; }
function renderInventory() { const inv = state.inventory, lookup = new Map(inv.slots.map(e => [addressKey(e.address), e])); const mk = (t, m, s = -1, a = -1) => ({ type: t, main_slot: m, sub_index: s, aug_index: a }); const at = (t, m, label) => { const a = mk(t, m); return slotButton(a, label, lookup.get(addressKey(a))); }; const signature = JSON.stringify([inv, selectedSlot, openBag]); if (signature === lastInventory)
    return; lastInventory = signature; const equipment = EQUIPMENT_LAYOUT.map(i => i === null ? '<span class="equipment-gap" aria-hidden="true"></span>' : at(0, i, inv.worn[i])).join(''); html('equipment', equipment); html('equipmentpreview', equipment); html('gearstats', Object.entries(inv.gear ?? {}).map(([k, v]) => `<div class="stat"><span>${esc(k.replaceAll('_', ' '))}</span><b>${esc(v)}</b></div>`).join('')); html('general', Array.from({ length: 10 }, (_, i) => at(0, 23 + i, `Pack ${i + 1}`)).join('') + at(0, 33, 'Cursor')); html('bank', inv.slots.filter(e => e.address.type === 1 || e.address.type === 2).filter(e => e.address.sub_index === -1 && e.address.aug_index === -1).map(e => slotButton(e.address, `${e.address.type === 1 ? 'Bank' : 'Shared'} ${e.address.main_slot + 1}`, e)).join('') || '<p class="muted">Not loaded or empty.</p>'); let e = lookup.get(openBag ?? selectedSlot); if (e) {
    const a = e.address;
    let cells = [];
    if (e.item.bag_slots > 0) {
        for (let i = 0; i < e.item.bag_slots; i++) {
            const x = mk(a.type, a.main_slot, i);
            cells.push(slotButton(x, `Cell ${i + 1}`, lookup.get(addressKey(x))));
        }
    }
    let aug = inv.slots.filter(x => x.address.type === a.type && x.address.main_slot === a.main_slot && x.address.sub_index === a.sub_index && x.address.aug_index >= 0);
    html('bagdetail', cells.length || aug.length ? `<h3>${esc(e.item.name)} contents / augments</h3><div class="slots">${cells.join('')}${aug.map(x => slotButton(x.address, `Aug ${x.address.aug_index + 1}`, x)).join('')}</div>` : '');
}
else
    html('bagdetail', ''); }
function selectSlot(key) { if (!state)
    return; selectedSlot = key; const [t, m, s, a] = key.split(':').map(Number); if (s === -1 && a === -1)
    openBag = key; lastInventory = ''; renderInventory(); const x = state.inventory.slots.find(x => addressKey(x.address) === key); if (x)
    inspectItem(x.item.item_id, x);
else {
    text('itemcard', 'Empty slot: ' + key);
    text('itemdetail', '');
} }
$('inventory').onclick = e => { let b = e.target.closest('[data-slot]'); if (b)
    selectSlot(b.dataset.slot); };
$('equipmentpreview').onclick = e => { const b = e.target.closest('[data-slot]'); if (b) {
    setTab('inventory');
    selectSlot(b.dataset.slot);
} };
$('openinventory').onclick = () => setTab('inventory');
async function inspectItem(id, instance = null) { selectedItem = id; text('itemcard', 'Loading item #' + id + '…'); text('itemdetail', ''); try {
    let x = await api('/item/' + id);
    if (selectedItem !== id)
        return;
    const statNames = [['AC', 'ac'], ['Damage', 'damage'], ['Delay', 'delay'], ['HP', 'hp'], ['Mana', 'mana'], ['Endurance', 'endurance'], ['STR', 'strength'], ['STA', 'stamina'], ['AGI', 'agility'], ['DEX', 'dexterity'], ['WIS', 'wisdom'], ['INT', 'intelligence'], ['CHA', 'charisma'], ['Attack', 'attack'], ['Haste', 'haste'], ['Magic resist', 'resist_magic'], ['Fire resist', 'resist_fire'], ['Cold resist', 'resist_cold'], ['Poison resist', 'resist_poison'], ['Disease resist', 'resist_disease']];
    html('itemcard', `<div class="itemtitle">${esc(x.name)}</div><div class="muted">#${id} · ${esc(x.required_level ? 'Required level ' + x.required_level : 'No required level')} ${x.no_drop ? ' · NO DROP' : ''}${x.lore_group ? ' · LORE' : ''}</div>${instance ? `<p>Slot ${esc(instance.client_slot)} · Stack ${esc(instance.item.stack)} · Charges ${esc(instance.item.charges)}${instance.item.attuned ? ' · Attuned' : ''}</p>` : ''}<div class="stats">${statNames.filter(([_, k]) => x[k]).map(([label, k]) => `<div class="stat"><span>${label}</span><b>${esc(x[k])}</b></div>`).join('')}</div>${x.bag_slots ? `<p>${x.bag_slots} bag slots · Size ${esc(x.bag_size)}</p>` : ''}<p class="muted">${x.classes?.map(k => cls[k]).filter(Boolean).join(' · ') ?? ''}</p>`);
    text('itemdetail', pretty({ definition: x, instance }));
}
catch (e) {
    if (selectedItem === id) {
        text('itemcard', e.message);
        if (instance)
            text('itemdetail', pretty(instance));
    }
} }
$('itemform').onsubmit = async (e) => { e.preventDefault(); text('itemresults', 'Searching…'); try {
    let rows = await api('/dashboard/items?q=' + encodeURIComponent($('itemquery').value.trim()));
    html('itemresults', rows.map(x => `<button data-item="${x.item_id}"><span>${esc(x.name)}</span><span class="muted">#${x.item_id}</span></button>`).join('') || '<p>No matches.</p>');
}
catch (e) {
    text('itemresults', e.message);
} };
$('itemresults').onclick = e => { let b = e.target.closest('[data-item]'); if (b)
    inspectItem(Number(b.dataset.item)); };
async function loadActions() { text('actionhint', 'Loading action modules…'); try {
    const names = await api('/actions/modules');
    let results = await Promise.allSettled(names.map(async (n) => [n, await api('/actions/modules/' + n)]));
    actionCatalog.clear();
    const errors = [];
    results.forEach((r, i) => { if (r.status === 'rejected') {
        errors.push(names[i]);
        return;
    } const [n, m] = r.value; Object.entries(m.classes).forEach(([k, v]) => actionCatalog.set(n + '/' + k, { module: n, name: k, ...v })); });
    html('actionselect', [...actionCatalog].map(([k, v]) => `<option value="${esc(k)}">${esc(v.name)} (${esc(v.module)})</option>`).join(''));
    if (actionCatalog.has('form/FormParty'))
        $('actionselect').value = 'form/FormParty';
    showAction();
    if (errors.length)
        $('actionhint').textContent += ' · unavailable: ' + errors.join(', ');
    let ops = await api('/schemas');
    html('opcode', ops.map(x => `<option>${esc(x)}</option>`).join(''));
}
catch (e) {
    text('actionhint', e.message);
} }
function element(tag, props = {}, children = []) { const el = document.createElement(tag); Object.assign(el, props); children.forEach(c => el.append(c)); return el; }
function fieldControl(schema, defs, required, label, defaultValue, spawn = false) {
    const outer = element('div', { className: 'field' }), title = element('label', { textContent: label + (required ? ' *' : '') });
    outer.append(title);
    const ref = schema.$ref?.split('/').pop();
    if (ref && defs[ref])
        schema = defs[ref];
    const alternatives = schema.anyOf ?? schema.oneOf;
    if (alternatives) {
        const select = element('select');
        const variants = alternatives.map(v => v.$ref ? defs[v.$ref.split('/').pop()] ?? v : v);
        if (!required)
            select.add(element('option', { value: '', textContent: 'Use default' }));
        variants.forEach((v, i) => select.add(element('option', { value: String(i), textContent: v.title ?? (v.type === 'null' ? 'None' : v.type ?? 'Value ' + (i + 1)) })));
        const holder = element('div');
        outer.append(select, holder);
        let reader = () => undefined;
        function change() { holder.replaceChildren(); const i = select.value; if (i === '') {
            reader = () => undefined;
            return;
        } const v = variants[Number(i)]; if (v.type === 'null') {
            reader = () => null;
            return;
        } const child = fieldControl(v, defs, true, 'Value', undefined, spawn); holder.append(child.node); reader = child.read; }
        select.onchange = change;
        change();
        return { node: outer, read: () => reader() };
    }
    if (schema.type === 'object' && schema.properties) {
        const children = [];
        for (const [name, v] of Object.entries(schema.properties)) {
            const child = fieldControl(v, defs, (schema.required ?? []).includes(name), name, v.default);
            outer.append(child.node);
            children.push([name, child.read]);
        }
        return { node: outer, read: () => Object.fromEntries(children.map(([k, f]) => [k, f()]).filter(([_, v]) => v !== undefined)) };
    }
    if (schema.type === 'array' && schema.prefixItems) {
        const children = schema.prefixItems.map((v, i) => fieldControl(v, defs, true, `Component ${i + 1}`));
        children.forEach(c => outer.append(c.node));
        return { node: outer, read: () => children.map(c => c.read()) };
    }
    let input, read;
    const t = schema.type;
    if (t === 'boolean' || schema.enum) {
        input = element('select');
        if (!required)
            input.add(element('option', { value: '', textContent: 'Use default' }));
        else
            input.add(element('option', { value: '', textContent: 'Choose…' }));
        const vals = schema.enum ?? [true, false];
        vals.forEach((v, i) => input.add(element('option', { value: String(i), textContent: String(v) })));
        input.required = required;
        read = () => input.value === '' ? undefined : vals[Number(input.value)];
    }
    else if (t === 'integer' || t === 'number' || t === 'string') {
        input = element('input', { type: t === 'string' ? 'text' : 'number', required, placeholder: defaultValue === undefined ? (spawn ? 'Choose or enter spawn ID' : '') : String(defaultValue) });
        if (t !== 'string')
            input.step = t === 'integer' ? '1' : 'any';
        if (spawn) {
            input.setAttribute('list', 'entityids');
            input.dataset.spawn = 'true';
            if (selectedMob !== null)
                input.value = String(selectedMob);
        }
        if (schema.minimum !== undefined)
            input.min = schema.minimum;
        if (schema.maximum !== undefined)
            input.max = schema.maximum;
        read = () => input.value === '' ? undefined : t === 'string' ? input.value : Number(input.value);
    }
    else {
        input = element('textarea', { rows: 3, required, placeholder: 'JSON value' });
        read = () => input.value.trim() === '' ? undefined : JSON.parse(input.value);
    }
    outer.append(input);
    const note = element('small', { textContent: defaultValue === undefined ? (required ? 'Required' : 'Optional') : 'Default: ' + JSON.stringify(defaultValue) });
    outer.append(note);
    return { node: outer, read };
}
async function showAction() { const generation = ++actionGeneration; activeAction = actionCatalog.get($('actionselect').value); if (!activeAction)
    return; const a = activeAction; text('actionhint', a.signature); $('params').replaceChildren(); $('launch').disabled = true; paramReaders = []; try {
    const d = await api('/dashboard/action/' + a.module + '/' + a.name);
    if (generation !== actionGeneration)
        return;
    for (const p of d.parameters) {
        const schema = p.schema ?? {};
        const spawn = schema['x-eq-spawn'] || /^(target_id|spawn_id|npc_id)$/.test(p.name);
        const control = fieldControl(schema, schema.$defs ?? {}, p.required, p.name, p.default, spawn);
        $('params').append(control.node);
        paramReaders.push([p.name, control.read]);
    }
    const datalist = element('datalist', { id: 'entityids' });
    $('params').append(datalist);
    refreshEntityOptions();
    $('launch').disabled = !d.compatible;
    if (!d.compatible)
        text('actionhint', a.signature + ' · Legacy constructor is not compatible with the current DebugLoop API.');
}
catch (e) {
    if (generation === actionGeneration)
        text('actionhint', e.message);
} }
function refreshEntityOptions() { if (!state || !$('entityids'))
    return; html('entityids', [...state.mobs, ...state.bots.filter(b => b.spawned)].map(m => `<option value="${m.id}" label="${esc(m.name)}"></option>`).join('')); }
$('mobaction').onclick = () => { setTab('actions'); if (activeAction)
    showAction(); };
$('actionselect').onchange = showAction;
$('reload').onclick = async () => { if (!activeAction)
    return; let a = activeAction; try {
    let m = await post('/actions/reload/' + a.module, {});
    for (const k of actionCatalog.keys())
        if (k.startsWith(a.module + '/'))
            actionCatalog.delete(k);
    Object.entries(m.classes).forEach(([k, v]) => actionCatalog.set(a.module + '/' + k, { module: a.module, name: k, ...v }));
    html('actionselect', [...actionCatalog].map(([k, v]) => `<option value="${esc(k)}">${esc(v.name)} (${esc(v.module)})</option>`).join(''));
    $('actionselect').value = a.module + '/' + a.name;
    showAction();
    text('actionresult', 'Module reloaded: ' + m.version);
}
catch (e) {
    text('actionresult', e.message);
} };
$('actionform').onsubmit = async (e) => { e.preventDefault(); if (!activeAction)
    return; try {
    let p = Object.fromEntries(paramReaders.map(([k, read]) => [k, read()]).filter(([_, v]) => v !== undefined));
    let a = await post('/actions/' + activeAction.module + '/' + activeAction.name, p);
    text('actionresult', 'Queued ' + a.class_name + ' · ' + a.id);
}
catch (e) {
    text('actionresult', e.message);
} };
function renderRuns() { refreshEntityOptions(); html('runs', state.actions.runs.slice().reverse().map(r => `<div class="row"><div><b>${esc(r.class_name)}</b><div class="muted">${esc(r.state)} · ${esc(r.id.slice(0, 8))}</div>${r.error ? `<span class="danger">${esc(r.error)}</span>` : ''}</div>${['queued', 'scheduled', 'suspended', 'running'].includes(r.state) ? `<button data-cancel="${esc(r.id)}">Cancel</button>` : ''}</div>`).join('') || '<p class="muted">No submitted actions.</p>'); }
$('runs').onclick = async (e) => { let b = e.target.closest('[data-cancel]'); if (b)
    try {
        await api('/actions/' + b.dataset.cancel, { method: 'DELETE' });
    }
    catch (e) {
        text('actionresult', e.message);
    } };
$('packetform').onsubmit = async (e) => { e.preventDefault(); try {
    text('packetresult', pretty(await post('/send/' + $('opcode').value, JSON.parse($('packetbody').value))));
}
catch (e) {
    text('packetresult', e.message);
} };
function entityName(id) { if (id == null)
    return '—'; if (state?.self_id === id)
    return state.character.name; return state?.bots.find(b => b.id === id && b.spawned)?.name ?? state?.mobs.find(m => m.id === id)?.name ?? '#' + id; }
function packetSummary(p) { const v = p.payload; if (!v)
    return ''; if (p.opcode === 'OP_Damage')
    return `${entityName(v.source)} → ${entityName(v.target)}: ${v.amount} damage${v.spell_id && v.spell_id !== 65535 ? ' (spell #' + v.spell_id + ')' : ''}`; if (p.opcode === 'OP_MobHealth')
    return `${entityName(v.spawn_id)} · HP ${v.percent}%`; if (p.opcode === 'OP_MobManaUpdate' || p.opcode === 'OP_MobEnduranceUpdate')
    return `${entityName(v.spawn_id)} · ${v.percent}%`; if (p.opcode === 'OP_Buff')
    return `${entityName(v.entity_id)} · ${v.fade ? 'Faded' : 'Buff'} spell #${v.buff?.spell_id} · ${v.buff?.duration} ticks`; if (p.opcode === 'OP_BuffCreate' || p.opcode === 'OP_TargetBuffs')
    return `${entityName(v.entity_id)} · ${v.entries?.length ?? 0} buff icons`; if (p.opcode === 'OP_BeginCast')
    return `${entityName(v.caster_id ?? v.caster)} · casting spell #${v.spell_id}`; return v.message ?? v.text ?? JSON.stringify(v); }
function packetLine(p) { let summary = packetSummary(p); return `<button class="packet" data-packet="${p.id}" title="${esc(summary)}"><span class="stamp">${esc(p.timestamp.slice(11, 23))}</span> <span class="${p.direction}">${p.direction === 'recv' ? '↓' : '↑'}</span> ${esc(p.opcode)} <span class="stamp">${p.size} B</span> ${esc(summary)}</button>`; }
function renderLog(kind) { const l = logs[kind], box = $(kind + 'log'), q = $(kind + 'filter').value.toLowerCase(), dir = kind === 'wire' ? $('direction').value : 'all'; let rows = l.rows.filter(p => (dir === 'all' || p.direction === dir) && (!q || (p.opcode + ' ' + packetSummary(p) + ' ' + JSON.stringify(p.payload ?? '')).toLowerCase().includes(q))); const tail = box.scrollHeight - box.scrollTop - box.clientHeight < 40; html(kind + 'log', rows.slice(-500).map(packetLine).join('')); if (tail)
    box.scrollTop = box.scrollHeight; text(kind + 'count', `${rows.length} buffered${l.paused ? ' · paused' : ''}${l.more ? ' · catching up' : ''}`); }
async function pollLog(kind) { const l = logs[kind]; if (l.busy || l.paused)
    return; l.busy = true; try {
    let r = await api(`/dashboard/packets?stream=${kind}&after=${l.after}&limit=250`);
    l.after = r.next;
    l.more = r.has_more;
    if (r.packets.length) {
        l.rows.push(...r.packets);
        if (l.rows.length > 1500)
            l.rows.splice(0, l.rows.length - 1500);
    }
    if (tab === 'logs')
        renderLog(kind);
}
catch (e) {
    if (tab === 'logs')
        text(kind + 'count', e.message);
}
finally {
    l.busy = false;
} }
for (const k of ['wire', 'combat']) {
    $('pause' + k).onclick = () => { logs[k].paused = !logs[k].paused; text('pause' + k, logs[k].paused ? 'Resume' : 'Pause'); renderLog(k); };
    $(k + 'filter').oninput = () => renderLog(k);
    $(k + 'log').onclick = async (e) => { let b = e.target.closest('[data-packet]'); if (b)
        try {
            text('packetdetail', pretty(await api('/dashboard/packet/' + b.dataset.packet)));
        }
        catch (e) {
            text('packetdetail', e.message);
        } };
}
$('direction').onchange = () => renderLog('wire');
// No overlapping state requests: an expensive EQ tick must not accumulate HTTP work.
async function tick() { const start = performance.now(); try {
    state = await api('/dashboard/state');
    render();
}
catch (e) {
    status('Disconnected / busy', false);
    text('metrics', e.message);
} pollLog('wire'); pollLog('combat'); setTimeout(tick, Math.max(0, 200 - (performance.now() - start))); }
tick();
