/* BT-INVEST — ứng dụng luyện thi chứng chỉ hành nghề chứng khoán. JavaScript thuần, không cần build. */
(() => {
'use strict';

// ---------- cấu hình nội dung ----------
const SUBJ = {
  LU: { name: 'Pháp luật về CK & TTCK', short: 'Pháp luật' },
  CB: { name: 'Những vấn đề cơ bản về CK & TTCK', short: 'Cơ bản' },
  PT: { name: 'Phân tích & đầu tư chứng khoán', short: 'Phân tích & đầu tư' },
  MG: { name: 'Môi giới & tư vấn đầu tư CK', short: 'Môi giới & tư vấn' },
  BC: { name: 'Phân tích báo cáo tài chính DN', short: 'Phân tích BCTC' },
  BL: { name: 'Tư vấn tài chính & bảo lãnh phát hành', short: 'Tư vấn TC & BLPH' },
  QU: { name: 'Quản lý quỹ & tài sản', short: 'Quản lý quỹ' },
  PS: { name: 'CK phái sinh & TTCK phái sinh', short: 'Phái sinh' },
};
// Môn chuyên môn theo điều kiện cấp CCHN (Điều 213 NĐ 155/2020, sửa bởi NĐ 245/2025). Tỷ trọng là cấu hình mô phỏng của ứng dụng.
const CERTS = {
  'moi-gioi': { name: 'Môi giới chứng khoán', minutes: 60, blueprint: { CB: .30, PT: .35, MG: .35 } },
  'phan-tich': { name: 'Phân tích tài chính', minutes: 75, blueprint: { CB: .10, PT: .25, MG: .15, BL: .25, BC: .25 } },
  'quan-ly-quy': { name: 'Quản lý quỹ', minutes: 90, blueprint: { CB: .05, PT: .20, MG: .05, BL: .15, BC: .20, QU: .35 } },
};
const PARTS = { LUAT: 'Pháp luật CK & TTCK', CM: 'Chuyên môn' };
const LEVEL = { 1: 'Nhớ', 2: 'Hiểu', 3: 'Vận dụng' };
const PASS = 0.6;          // sát hạch CCHN: đúng từ 60% mỗi phần (thông báo Hội đồng thi 2026)
const SUBJ_PASS = 0.5;     // thi cuối khóa chứng chỉ chuyên môn: đạt từ 50/100 điểm (nguồn tổng hợp, chưa thấy quy chế gốc công khai)
const DAY = 864e5, SRS_DAYS = [0, 1, 3, 7, 16, 35];
const KEY = 'docchn_v1';   // giữ khóa cũ để người dùng không mất tiến độ khi đổi thương hiệu
const BRAND = { name: 'BT-INVEST', phone: '0942037820', phoneShow: '0942 037 820', zalo: 'https://zalo.me/0942037820' };
const SOCIAL = [   // [mã, tên, link, tên hiển thị trên kênh]
  ['facebook', 'Facebook', 'https://www.facebook.com/profile.php?id=61590345622201', 'BT Tài Chính'],
  ['youtube', 'YouTube', 'https://www.youtube.com/@bt.invest', '@bt.invest'],
  ['tiktok', 'TikTok', 'https://www.tiktok.com/@bt.invest', '@bt.invest'],
  ['x', 'X', 'https://x.com/btinvest24', '@btinvest24'],
];
const SOCIAL_IC = {
  facebook: '<path d="M13.5 21v-7.5h2.6l.4-3h-3V8.6c0-.9.3-1.5 1.5-1.5h1.6V4.4c-.3 0-1.2-.1-2.3-.1-2.3 0-3.8 1.4-3.8 3.9v2.3H7.9v3h2.6V21z"/>',
  youtube: '<path fill-rule="evenodd" d="M21.6 7.2a2.5 2.5 0 0 0-1.8-1.8C18.2 5 12 5 12 5s-6.2 0-7.8.4a2.5 2.5 0 0 0-1.8 1.8C2 8.8 2 12 2 12s0 3.2.4 4.8a2.5 2.5 0 0 0 1.8 1.8C5.8 19 12 19 12 19s6.2 0 7.8-.4a2.5 2.5 0 0 0 1.8-1.8c.4-1.6.4-4.8.4-4.8s0-3.2-.4-4.8zM10 15V9l5.2 3z"/>',
  tiktok: '<path d="M16.6 5.8A4.3 4.3 0 0 1 15.5 3h-3.1v12.4a2.6 2.6 0 1 1-2.6-2.6c.3 0 .5 0 .8.1V9.7a5.8 5.8 0 1 0 5 5.7V9.1a7.4 7.4 0 0 0 4.3 1.4V7.4a4.3 4.3 0 0 1-3.3-1.6z"/>',
  x: '<path d="M17.8 3h3.1l-6.8 7.8L22 21h-6.2l-4.9-6.4L5.3 21H2.2l7.3-8.3L2 3h6.4l4.4 5.8zm-1.1 16.2h1.7L7.4 4.7H5.6z"/>',
};
const socialIcons = () => `<div class="social">${SOCIAL.map(([k, n, u]) => `<a href="${u}" target="_blank" rel="noopener" aria-label="BT-INVEST trên ${n}" title="${n}"><svg viewBox="0 0 24 24" aria-hidden="true">${SOCIAL_IC[k]}</svg></a>`).join('')}</div>`;
const reduceMotion = () => matchMedia('(prefers-reduced-motion: reduce)').matches;

// ---------- tiện ích ----------
const $ = s => document.querySelector(s), $$ = s => [...document.querySelectorAll(s)];
const esc = s => String(s ?? '').replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
const pct = (a, b) => (b ? Math.round(a / b * 100) : 0);
const fmt = n => Number(n).toLocaleString('vi-VN');
const shuffle = a => { a = [...a]; for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; };
const now = () => Date.now();
const L = 'ABCDEF';
const dt = t => new Date(t).toLocaleString('vi-VN', { day: '2-digit', month: '2-digit', year: 'numeric', hour: '2-digit', minute: '2-digit' });

// ---------- trạng thái người học (chỉ lưu trên máy) ----------
const blank = () => ({ v: 1, q: {}, star: {}, hist: [], sess: null, last: null, theme: '', reports: [], cards: {}, prefs: { cert: 'moi-gioi', n: 35 } });
let S = blank();
try { const raw = JSON.parse(localStorage.getItem(KEY)); if (raw && raw.v === 1) S = { ...blank(), ...raw, prefs: { ...blank().prefs, ...(raw.prefs || {}) } }; } catch { /* không có bộ nhớ: chạy với trạng thái trống */ }
let saveWarned = false;
function save() {
  try { localStorage.setItem(KEY, JSON.stringify(S)); }
  catch { if (!saveWarned) { saveWarned = true; toast('Trình duyệt không cho lưu tiến độ. Hãy dùng Cài đặt → Sao lưu để giữ kết quả.'); } }
  if (AUTH) { clearTimeout(save.t); save.t = setTimeout(syncNow, 4000); }   // có tài khoản: đẩy lên máy chủ sau 4 giây yên lặng
}

// ---------- tài khoản (không bắt buộc): đồng bộ tiến độ qua /api/tai-khoan ----------
const AUTH_KEY = 'btinvest_auth';
let AUTH = null, lastSync = 0;
try { AUTH = JSON.parse(localStorage.getItem(AUTH_KEY)); } catch { /* không có bộ nhớ */ }
const setAuth = a => { AUTH = a; try { a ? localStorage.setItem(AUTH_KEY, JSON.stringify(a)) : localStorage.removeItem(AUTH_KEY); } catch { /* bỏ qua */ } };
const syncData = () => ({ q: S.q, star: S.star, hist: S.hist, cards: S.cards, prefs: S.prefs });
function adopt(d) {   // nhận bản đã gộp từ máy chủ; ghi thẳng localStorage để không kích hoạt đồng bộ lần nữa
  if (!d) return;
  Object.assign(S, { q: d.q || {}, star: d.star || {}, hist: d.hist || [], cards: d.cards || {}, prefs: { ...S.prefs, ...(d.prefs || {}) } });
  try { localStorage.setItem(KEY, JSON.stringify(S)); } catch { /* bỏ qua */ }
}
async function api(a, body = {}, extra = {}) {
  let r;
  try {
    r = await fetch('/api/tai-khoan', { method: 'POST', headers: { 'content-type': 'application/json', ...(AUTH ? { authorization: 'Bearer ' + AUTH.token } : {}), ...extra }, body: JSON.stringify({ a, ...body }) });
  } catch { throw new Error('Không kết nối được máy chủ. Kiểm tra mạng rồi thử lại.'); }
  const j = await r.json().catch(() => ({}));
  if (r.status === 401 && AUTH && a !== 'xoa' && !extra['x-admin-key']) { setAuth(null); renderAcct(); }
  if (!r.ok) throw new Error(j.error || 'Có lỗi, hãy thử lại.');
  return j;
}
async function syncNow() {
  if (!AUTH) return;
  try { const j = await api('luu', { data: syncData() }); adopt(j.data); AUTH.user = j.user; setAuth(AUTH); lastSync = j.at; renderAcct(); }
  catch { /* mất mạng: lần lưu sau sẽ đồng bộ lại */ }
}
addEventListener('visibilitychange', () => { if (document.visibilityState === 'hidden' && AUTH && save.t) { clearTimeout(save.t); save.t = 0; syncNow(); } });
const acctBtn = compact => AUTH
  ? `<a class="btn sm acct-me" href="#tai-khoan" title="Tài khoản của bạn"><span class="av">${esc((AUTH.user.name || AUTH.user.email)[0].toUpperCase())}</span>${compact ? '' : `<span class="nm">${esc(AUTH.user.name || 'Tài khoản')}</span>`}</a>`
  : compact ? `<a class="btn sm primary" href="#tai-khoan">Đăng nhập</a>`
  : `<span class="hint">Lưu tiến độ, học trên mọi thiết bị</span><a class="btn sm primary" href="#tai-khoan">Đăng nhập / Tạo tài khoản</a>`;
function renderAcct() { const t = $('#acct-top'), d = $('#acct-desk'); if (t) t.innerHTML = acctBtn(true); if (d) d.innerHTML = acctBtn(false); }
const acctNudge = () => AUTH || (S.prefs.hideAcc && now() - S.prefs.hideAcc < 7 * DAY) ? '' :
  `<div class="note info row between acct-nudge"><span><b>Tạo tài khoản miễn phí</b> để lưu tiến độ, học tiếp trên điện thoại và máy tính, nhận gợi ý theo chứng chỉ bạn thi.</span>
    <span class="row"><a class="btn sm primary" href="#tai-khoan">Tạo tài khoản</a><button class="btn sm ghost" data-hide-acc aria-label="Ẩn gợi ý tạo tài khoản">Để sau</button></span></div>`;
document.addEventListener('click', e => { if (e.target.closest('[data-hide-acc]')) { S.prefs.hideAcc = now(); save(); e.target.closest('.acct-nudge')?.remove(); } });

// ---------- dữ liệu ----------
const D = { q: [], byId: new Map(), law: null, cards: [], changes: [], docs: [] };
async function loadJSON(name, fallback) {
  const inline = document.getElementById('data-' + name);
  if (inline) return JSON.parse(inline.textContent);
  try { const r = await fetch('data/' + name + '.json'); if (!r.ok) throw new Error(r.status); return await r.json(); }
  catch (e) { console.warn('Không tải được', name, e); return fallback; }
}

// ---------- thống kê ----------
function rec(id, ok) {
  const st = S.q[id] || { n: 0, ok: 0, box: 0, due: 0 };
  st.n++; if (ok) st.ok++; st.last = now(); st.lastOk = ok;
  if (ok) { st.box = Math.min(st.box + 1, 5); st.due = now() + SRS_DAYS[st.box] * DAY; }
  else { st.box = 1; st.due = now(); }
  S.q[id] = st;
  share(id, ok);
}
// ---------- thống kê chung, ẩn danh: chỉ gửi mã câu và đúng/sai (tắt được trong Cài đặt) ----------
const STATS_API = '/api/thong-ke';
const outbox = [];
function share(id, ok) {
  if (S.prefs.share === false || !location.protocol.startsWith('http')) return;
  outbox.push([id, ok ? 1 : 0]); if (outbox.length >= 20) flushStats();
}
function flushStats() {
  if (!outbox.length) return;
  const body = JSON.stringify({ a: outbox.splice(0, 200) });
  try { if (!navigator.sendBeacon?.(STATS_API, new Blob([body], { type: 'application/json' }))) fetch(STATS_API, { method: 'POST', body, headers: { 'content-type': 'application/json' }, keepalive: true }).catch(() => {}); }
  catch { /* mất mạng: bỏ qua, không ảnh hưởng việc học */ }
}
addEventListener('visibilitychange', () => { if (document.visibilityState === 'hidden') flushStats(); });
let COMM;   // { n: {mã: lượt làm}, w: {mã: lượt sai} } từ máy chủ; null nếu chưa bật
async function loadComm() {
  if (COMM === undefined) { COMM = null; try { const r = await fetch(STATS_API); if (r.ok) COMM = await r.json(); } catch { /* chưa có máy chủ thống kê */ } }
  return COMM;
}
const dueIds = () => D.q.filter(q => S.q[q.id] && S.q[q.id].due <= now()).map(q => q.id);
function subjStats(code) {
  const qs = D.q.filter(q => q.subject === code);
  let seen = 0, n = 0, ok = 0;
  for (const q of qs) { const st = S.q[q.id]; if (st) { seen++; n++; ok += st.lastOk ? 1 : 0; } }
  return { total: qs.length, seen, acc: n ? ok / n : 0, n };
}
function level(acc, n) {
  if (n < 5) return ['none', 'Chưa đủ dữ liệu'];
  if (acc < .4) return ['floor', 'Sàn'];
  if (acc < .6) return ['down', 'Giảm'];
  if (acc < .7) return ['ref', 'Tham chiếu'];
  if (acc < .85) return ['up', 'Tăng'];
  return ['ceil', 'Trần'];
}
function readiness(certKey) {
  const out = {};
  for (const part of ['LUAT', 'CM']) {
    const subs = part === 'LUAT' ? { LU: 1 } : CERTS[certKey].blueprint;
    let w = 0, s = 0, seen = 0;
    for (const [code, wt] of Object.entries(subs)) { const st = subjStats(code); seen += st.seen; if (st.n) { s += wt * st.acc; w += wt; } }
    out[part] = { est: w ? s / w : null, seen };
  }
  return out;
}

// ---------- giao diện chung ----------
const IC = {
  home: '<path d="M3 11l9-7 9 7"/><path d="M5 10v10h14V10"/>',
  practice: '<circle cx="12" cy="12" r="8"/><circle cx="12" cy="12" r="3"/>',
  review: '<path d="M20 12a8 8 0 1 1-2.3-5.6"/><path d="M20 4v5h-5"/>',
  exam: '<rect x="5" y="3" width="14" height="18" rx="2"/><path d="M9 8h6M9 12h6M9 16h3"/>',
  bank: '<path d="M4 6h16M4 12h16M4 18h10"/>',
  cards: '<rect x="3" y="6" width="14" height="12" rx="2"/><path d="M7 3h12a2 2 0 0 1 2 2v10"/>',
  calc: '<rect x="5" y="3" width="14" height="18" rx="2"/><path d="M8 7h8M8 12h2M12 12h2M16 12v5M8 16h2M12 16h2"/>',
  law: '<path d="M12 3v18M5 7h14M7 7l-3 7h6zM17 7l-3 7h6z"/>',
  change: '<path d="M12 8v5l3 2"/><circle cx="12" cy="12" r="9"/>',
  rules: '<path d="M6 3h9l4 4v14H6z"/><path d="M14 3v5h5M9 13h7M9 17h5"/>',
  history: '<path d="M4 19h16M7 16V9M12 16V5M17 16v-4"/>',
  gear: '<circle cx="12" cy="12" r="3"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M4.9 4.9l2.1 2.1M17 17l2.1 2.1M4.9 19.1L7 17M17 7l2.1-2.1"/>',
  menu: '<path d="M4 7h16M4 12h16M4 17h16"/>',
  target: '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><path d="M12 12l6-6M15 6h3v3"/>',
  phone: '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/>',
};
const icon = k => `<svg viewBox="0 0 24 24" aria-hidden="true">${IC[k]}</svg>`;
const NAV = [
  ['Học', [['tong-quan', 'Tổng quan', 'home'], ['on-luyen', 'Ôn luyện', 'practice'], ['trong-tam', 'Trọng tâm từng môn', 'target'], ['on-tap', 'Ôn lặp lại', 'review'], ['thi-thu', 'Thi thử', 'exam']]],
  ['Tra cứu', [['ngan-hang', 'Ngân hàng câu hỏi', 'bank'], ['the-nho', 'Thẻ ghi nhớ số liệu', 'cards'], ['cong-thuc', 'Công thức & máy tính', 'calc'],
    ['thu-vien', 'Thư viện luật', 'law'], ['thay-doi', 'Luật mới 2025–2026', 'change'], ['quy-che', 'Quy chế thi 2026', 'rules']]],
  ['Cá nhân', [['lich-su', 'Lịch sử & tiến độ', 'history'], ['cai-dat', 'Cài đặt & sao lưu', 'gear'], ['lien-he', 'Giới thiệu & liên hệ', 'phone']]],
];
const TITLES = Object.fromEntries(NAV.flatMap(g => g[1].map(x => [x[0], x[1]])));
Object.assign(TITLES, { 'lam-bai': 'Đang làm bài', 'ket-qua': 'Kết quả', 'tai-khoan': 'Tài khoản', 'quan-tri': 'Quản trị' });
const brandMark = () => `<span class="brand-mark" aria-hidden="true"><span>B<i>T</i></span><em><b style="height:3px;background:#E0505A"></b><b style="height:5px;background:#19B47A"></b><b style="height:7px;background:#E0B04A"></b></em></span>`;

function renderNav(cur) {
  const due = dueIds().length;
  $('#nav').innerHTML = `<a class="brand" href="#tong-quan" style="text-decoration:none;color:inherit">${brandMark()}<div><b>BT-<i>INVEST</i></b><small>Luyện thi CCHN</small></div></a>` +
    NAV.map(([g, items]) => `<div class="nav-group">${g}</div>` + items.map(([h, t, i]) =>
      `<a href="#${h}" class="${cur === h ? 'on' : ''}">${icon(i)}<span>${t}</span>${h === 'on-tap' && due ? `<span class="badge-due">${due}</span>` : ''}</a>`).join('')).join('') +
    `<div class="nav-foot"><a class="hotline" href="#lien-he"><span>Hotline / Zalo</span><b>${BRAND.phoneShow}</b></a>${socialIcons()}
      <span>${fmt(D.q.length)} câu hỏi, luật cập nhật đến 11/2026. Không phải trang chính thức của UBCKNN.</span></div>`;
  const tabs = [['tong-quan', 'Tổng quan', 'home'], ['on-luyen', 'Ôn luyện', 'practice'], ['trong-tam', 'Trọng tâm', 'target'], ['thi-thu', 'Thi thử', 'exam']];
  $('#tabbar').innerHTML = tabs.map(([h, t, i]) => `<a href="#${h}" class="${cur === h ? 'on' : ''}">${icon(i)}${t}</a>`).join('') +
    `<a href="#menu" id="tab-more">${icon('menu')}Thêm</a>`;
  $('#tab-more').onclick = e => { e.preventDefault(); openNav(true); };
  $('#topbar-title').textContent = TITLES[cur] || '';
  renderAcct();
}
function openNav(open) {
  $('#nav').classList.toggle('open', open);
  $('#menu-btn').setAttribute('aria-expanded', open);
  const sc = $('#scrim');
  if (open && !sc) { const d = document.createElement('div'); d.id = 'scrim'; d.className = 'scrim'; d.onclick = () => openNav(false); document.body.appendChild(d); }
  if (!open && sc) sc.remove();
}
function toast(t) { const el = $('#toast'); el.textContent = t; el.hidden = false; clearTimeout(toast.t); toast.t = setTimeout(() => (el.hidden = true), 3200); }
function modal(html, actions) {   // actions: [[label, cls, value]] → Promise(value)
  return new Promise(res => {
    const root = $('#modal-root');
    root.innerHTML = `<div class="modal-wrap"><div class="modal" role="dialog" aria-modal="true">${html}<div class="row" style="justify-content:flex-end">${
      actions.map((a, i) => `<button class="btn ${a[1] || ''}" data-i="${i}">${a[0]}</button>`).join('')}</div></div></div>`;
    const close = v => { modal.text = root.querySelector('textarea, input')?.value ?? ''; root.innerHTML = ''; document.removeEventListener('keydown', onKey); res(v); };
    const onKey = e => { if (e.key === 'Escape') close(null); };
    document.addEventListener('keydown', onKey);
    root.querySelectorAll('[data-i]').forEach(b => (b.onclick = () => close(actions[+b.dataset.i][2])));
    root.querySelector('.modal-wrap').onclick = e => { if (e.target.classList.contains('modal-wrap')) close(null); };
    (root.querySelector('textarea, input') || root.querySelector('.btn.primary') || root.querySelector('.btn'))?.focus();
  });
}
const confirmBox = (title, text, ok = 'Đồng ý', cls = 'primary') => modal(`<h2>${title}</h2><p class="muted">${text}</p>`, [['Hủy', '', false], [ok, cls, true]]);
function page(eyebrow, title, lead, body, right = '') {
  return `<div class="page"><div class="head"><div><div class="eyebrow">${eyebrow}</div><h1>${title}</h1>${lead ? `<p class="lead">${lead}</p>` : ''}</div>${right}</div>${body}</div>`;
}
const opts = (list, val) => list.map(([v, t]) => `<option value="${esc(v)}"${String(v) === String(val) ? ' selected' : ''}>${esc(t)}</option>`).join('');

// ---------- router ----------
const VIEWS = {};
let current = '';
function route() {
  let h = decodeURIComponent(location.hash.slice(1)) || 'tong-quan';
  if (h.startsWith('dieu-')) { current = 'thu-vien'; renderNav(current); VIEWS['thu-vien'](h.slice(5)); track('thu-vien'); return; }
  if (!VIEWS[h]) h = 'tong-quan';
  track(h);
  const render = () => { current = h; renderNav(h); openNav(false); VIEWS[h](); $('#main').scrollTo?.(0, 0); window.scrollTo(0, 0); };
  if (document.startViewTransition && current && current !== h && !reduceMotion()) document.startViewTransition(render); else render();
}
const go = h => { if (location.hash === '#' + h) route(); else location.hash = h; };
// Lượt truy cập cho trang quản trị: mã ngẫu nhiên của trình duyệt + tên trang (máy chủ tự thêm giờ, thiết bị, khu vực). Tắt được trong Cài đặt.
let VID = ''; try { VID = localStorage.getItem('btinvest_vid') || ''; if (!VID && crypto.randomUUID) localStorage.setItem('btinvest_vid', (VID = crypto.randomUUID())); } catch { /* không có bộ nhớ */ }
function track(p) {
  if (!VID || p === 'quan-tri' || S.prefs.share === false || !location.protocol.startsWith('http')) return;
  try { navigator.sendBeacon?.('/api/truy-cap', new Blob([JSON.stringify({ v: VID, p })], { type: 'application/json' })); } catch { /* bỏ qua */ }
}
const main = html => { $('#main').innerHTML = html; };

// Gợi ý hôm nay: trong các môn của chứng chỉ mục tiêu, chọn môn đúng ít nhất (môn chưa làm đủ 10 câu được ưu tiên trước)
function todayTip(cert) {
  const subs = ['LU', ...Object.keys(CERTS[cert].blueprint)].map(k => ({ k, ...subjStats(k) }));
  const pickS = subs.find(x => x.seen < 10) || [...subs].sort((a, b) => a.acc - b.acc)[0];
  if (!pickS) return '';
  const why = pickS.seen < 10 ? `bạn mới làm ${pickS.seen}/${pickS.total} câu môn này` : `bạn đang đúng ${Math.round(pickS.acc * 100)}%, thấp nhất trong các môn của chứng chỉ`;
  return `<div class="card row between tip-today"><div class="stack" style="gap:4px"><span class="eyebrow">Gợi ý hôm nay${AUTH?.user?.name ? ' cho ' + esc(AUTH.user.name) : ''}</span>
    <b>Ôn môn ${esc(SUBJ[pickS.k].name)}</b><span class="small muted">Vì ${why}. Mục tiêu: chứng chỉ ${esc(CERTS[cert].name)}.</span></div>
    <span class="row"><a class="btn sm primary" href="#trong-tam" data-tip="${pickS.k}">Xem trọng tâm</a><a class="btn sm" href="#thi-thu" data-tipx="${pickS.k}">Thi thử môn này</a></span></div>`;
}
document.addEventListener('click', e => {
  const a = e.target.closest('[data-tip],[data-tipx]'); if (!a) return;
  if (a.dataset.tip) S.prefs.focus = a.dataset.tip; else S.prefs.type = a.dataset.tipx;
  save();
});

// ---------- TỔNG QUAN ----------
VIEWS['tong-quan'] = () => {
  const cert = S.prefs.cert, rd = readiness(cert), due = dueIds().length;
  const seen = Object.keys(S.q).length, exams = S.hist.filter(h => h.kind === 'exam');
  const lastExam = exams[0];
  const ready = part => {
    const r = rd[part];
    if (r.seen < 15) return `<p class="small muted">Làm thêm ${15 - r.seen} câu để có ước tính.</p><div class="bar"><span class="mark" style="left:60%"></span></div>`;
    const p = Math.round(r.est * 100), [cls] = level(r.est, 99);
    return `<div class="row between"><span class="num" style="font-size:1.5rem;font-weight:700;color:var(--${cls === 'ceil' ? 'ceil' : cls === 'none' ? 'none' : cls})">${p}%</span><span class="chip ${p >= 60 ? 'up' : 'down'}">${p >= 60 ? 'Đang trên mốc 60%' : 'Dưới mốc 60%'}</span></div>
      <div class="bar"><i style="width:${p}%;background:var(--${p >= 60 ? 'up' : 'down'})"></i><span class="mark" style="left:60%"></span></div><p class="tiny muted">Dựa trên lần trả lời gần nhất của ${r.seen} câu đã làm, trọng số theo môn của chứng chỉ.</p>`;
  };
  const tiles = Object.entries(SUBJ).map(([code, s]) => {
    const st = subjStats(code), [cls, lab] = level(st.acc, st.n);
    return `<button class="tile ${cls}" data-subj="${code}" title="${esc(s.name)}"><span class="code">${code}</span><span class="name">${esc(s.short)}</span>
      <span class="pct">${st.n ? Math.round(st.acc * 100) + '%' : '—'}</span><span class="tiny muted">${lab} · đã làm ${st.seen}/${st.total}</span></button>`;
  }).join('');
  const resume = S.sess ? `<div class="note info row between"><span>Bạn có bài <b>${esc(S.sess.title)}</b> chưa hoàn tất.</span><a class="btn sm primary" href="#lam-bai">Tiếp tục</a></div>` : '';
  const last8 = exams.slice(0, 8).reverse();
  const candles = last8.length ? last8.map((h, i) => { const p = pct(h.ok, h.n); return `<span class="candle ${p >= 60 ? 'up' : 'down'}" style="height:${Math.max(p, 6)}%;animation-delay:${i * 60}ms" title="${dt(h.at)}: ${p}%"></span>`; }).join('')
    : [38, 52, 46, 64, 58, 72].map((p, i) => `<span class="candle ghost" style="height:${p}%;animation-delay:${i * 60}ms"></span>`).join('');
  main(`<div class="page"><section class="hero">
      <div><div class="who">${brandMark()}<span>BT-INVEST<span class="who-sub"> · Luyện thi CCHN 2026</span></span></div>
        <h1>Chào bạn, hôm nay ôn gì?</h1>
        <p>Mục tiêu: đúng từ 60% số câu ở <b>mỗi</b> phần thi. Chứng chỉ đang chọn: <b>${CERTS[cert].name}</b>.</p>
        <div class="cta"><a class="btn primary" href="${due ? '#on-tap' : '#on-luyen'}">${due ? `Ôn ${due} câu đến hạn` : 'Bắt đầu ôn luyện'}</a><a class="btn line" href="#thi-thu">Vào thi thử</a></div></div>
      <div class="follow"><span>Video tài chính đơn giản</span>${socialIcons()}</div>
      <div class="chart" aria-label="Phong độ thi thử"><div class="candles"><span class="line60"></span>${candles}</div>
        <span class="cap">${last8.length ? `Phong độ ${last8.length} lần thi thử gần nhất · nét đứt là mốc 60%` : 'Kết quả thi thử sẽ hiện ở đây'}</span></div>
    </section>
    ${acctNudge()}
    ${resume}
    ${todayTip(cert)}
    <div class="grid g4">
      <a class="card stat" href="#on-tap" style="text-decoration:none;color:inherit"><div class="k">Cần ôn hôm nay</div><div class="v">${due}</div><div class="d">${due ? 'Câu đến hạn theo lịch lặp lại' : 'Không có câu đến hạn'}</div></a>
      <div class="card stat"><div class="k">Đã luyện</div><div class="v">${fmt(seen)}</div><div class="d">${pct(seen, D.q.length)}% ngân hàng ${fmt(D.q.length)} câu</div></div>
      <div class="card stat"><div class="k">Bài thi thử</div><div class="v">${exams.length}</div><div class="d">${lastExam ? (lastExam.pass ? 'Lần gần nhất: Đạt' : 'Lần gần nhất: Chưa đạt') : 'Chưa thi lần nào'}</div></div>
      <div class="card stat"><div class="k">Đã đánh dấu</div><div class="v">${Object.keys(S.star).length}</div><div class="d">Câu lưu để xem lại</div></div>
    </div>
    <div class="grid g2">
      <div class="card stack"><div class="row between"><h2>Phần Pháp luật</h2><span class="chip">cần ≥ 60%</span></div>${ready('LUAT')}</div>
      <div class="card stack"><div class="row between"><h2>Phần Chuyên môn</h2><span class="chip">cần ≥ 60%</span></div>${ready('CM')}</div>
    </div>
    <div class="card stack">
      <div class="row between"><h2>Từng chứng chỉ chuyên môn</h2><span class="tiny muted">Bấm vào môn để xem phần hay sai, luyện và thi thử riêng môn đó</span></div>
      <div class="board">${tiles}</div>
      <div class="legend"><span><i style="background:var(--floor)"></i>Sàn &lt;40%</span><span><i style="background:var(--down)"></i>Giảm 40–59%</span>
        <span><i style="background:var(--ref)"></i>Tham chiếu 60–69%</span><span><i style="background:var(--up)"></i>Tăng 70–84%</span><span><i style="background:var(--ceil)"></i>Trần ≥85%</span></div>
    </div>
    <div class="grid g3">
      <a class="card stack" href="#trong-tam" style="text-decoration:none;color:inherit"><h3>Trọng tâm từng môn</h3><p class="small muted">Chủ đề và câu bạn hay sai, câu nhiều người sai của đúng môn bạn sắp thi.</p></a>
      <a class="card stack" href="#thi-thu" data-type="LU" style="text-decoration:none;color:inherit"><h3>Thi thử từng chứng chỉ chuyên môn</h3><p class="small muted">Thi riêng một môn (Pháp luật, Môi giới…): tính giờ, chỉ có câu của môn đó.</p></a>
      <a class="card stack" href="#on-luyen" style="text-decoration:none;color:inherit"><h3>Ôn luyện theo chủ đề</h3><p class="small muted">Chọn môn, chủ đề, mức độ; xem đáp án, giải thích và điều luật ngay sau mỗi câu.</p></a>
      <a class="card stack" href="#thi-thu" data-type="" style="text-decoration:none;color:inherit"><h3>Thi thử sát hạch CCHN</h3><p class="small muted">Hai phần tính giờ riêng, chỉ lấy câu thuộc chương trình của chứng chỉ bạn thi.</p></a>
      <a class="card stack" href="#thay-doi" style="text-decoration:none;color:inherit"><h3>Luật mới 2025–2026</h3><p class="small muted">Những quy định đã đổi theo Luật 56/2024, NĐ 245/2025, TT 135/2025… hay bị hỏi.</p></a>
    </div></div>`);
  $$('[data-subj]').forEach(b => (b.onclick = () => { S.prefs.focus = b.dataset.subj; save(); go('trong-tam'); }));
  $$('a[data-type]').forEach(a => (a.onclick = () => { S.prefs.type = a.dataset.type === 'LU' ? (S.prefs.type || 'LU') : ''; save(); }));
};

// ---------- ÔN LUYỆN ----------
let practiceFilter = { cert: '', part: '', subject: '', topic: '', level: '', pool: 'all', n: 20, mix: true };
function pool(f) {
  const allow = f.cert ? new Set(['LU', ...Object.keys(CERTS[f.cert].blueprint)]) : null;
  return D.q.filter(q => (!allow || allow.has(q.subject)) && (!f.part || q.part === f.part) && (!f.subject || q.subject === f.subject) &&
    (!f.topic || q.topic === f.topic) && (!f.level || String(q.level) === String(f.level)) &&
    (f.pool === 'all' || (f.pool === 'new' && !S.q[q.id]) || (f.pool === 'wrong' && S.q[q.id] && !S.q[q.id].lastOk) || (f.pool === 'star' && S.star[q.id])));
}
// Trộn đề thông minh: câu sai (khoảng 30%, sai lâu nhất trước) > câu chưa làm > câu đúng đã đến lịch ôn;
// câu đã làm đúng chỉ được lấy khi không còn câu nào khác. Rải theo tỷ trọng từng chủ đề và xen câu sai cách đều trong đề.
const WRONG_SHARE = 0.3;
const isWrong = id => !!S.q[id] && !S.q[id].lastOk;
function smartPick(ids, n, group = () => '') {
  const t = now(), tier = id => { const s = S.q[id]; return !s ? 1 : !s.lastOk ? 0 : s.due <= t ? 2 : 3; };
  const order = shuffle(ids).sort((a, b) => tier(a) - tier(b) || (S.q[a]?.due || 0) - (S.q[b]?.due || 0));
  const wrong = order.filter(id => tier(id) === 0), fresh = order.filter(id => tier(id) === 1 || tier(id) === 2);
  const w = Math.min(wrong.length, Math.max(Math.ceil(n * WRONG_SHARE), n - fresh.length));
  const out = [], cov = seenShare(group);
  for (const phase of [wrong.slice(0, w), fresh, order.filter(id => tier(id) === 3)]) {
    // lấy mẫu phân tầng: trước hết mỗi chủ đề 1 câu (chủ đề bạn làm ít nhất đi trước), phần còn lại theo tỷ trọng
    // (câu thứ i ≥ 1 của nhóm cỡ s có khóa (i + ngẫu nhiên)/s)
    const by = new Map(); for (const id of phase) by.set(group(id), [...(by.get(group(id)) || []), id]);
    const keyed = [...by.entries()].flatMap(([g, l]) => l.map((id, i) => [i ? (i + Math.random()) / l.length : cov(g) - 2 + Math.random() * 0.01, id]));
    out.push(...keyed.sort((a, b) => a[0] - b[0]).slice(0, n - out.length).map(x => x[1]));
  }
  return out;
}
// Tỷ lệ câu đã làm của từng nhóm (chủ đề): để các lượt trộn đề lần lượt phủ hết mọi chủ đề
function seenShare(group) {
  const c = new Map();
  for (const q of D.q) { const g = group(q.id), x = c.get(g) || [0, 0]; x[0] += S.q[q.id] ? 1 : 0; x[1]++; c.set(g, x); }
  return g => { const x = c.get(g); return x ? x[0] / x[1] : 0; };
}
function spread(ids) {     // thứ tự làm bài: câu sai đặt cách đều nhau, xen giữa các câu khác
  const ws = shuffle(ids.filter(isWrong)), rest = shuffle(ids.filter(id => !isWrong(id))), res = Array(ids.length).fill(null);
  ws.forEach((id, k) => (res[Math.floor((k + 0.5) * ids.length / ws.length)] = id));
  let j = 0; return res.map(x => x ?? rest[j++]);
}
VIEWS['on-luyen'] = () => {
  const f = practiceFilter;
  const subjects = Object.entries(SUBJ).filter(([c]) => (!f.part || (f.part === 'LUAT') === (c === 'LU')) && (!f.cert || c === 'LU' || CERTS[f.cert].blueprint[c]));
  if (f.subject && !subjects.some(([c]) => c === f.subject)) f.subject = '';
  const topics = [...new Set(D.q.filter(q => (!f.subject || q.subject === f.subject) && (!f.part || q.part === f.part)).map(q => q.topic))].sort((a, b) => a.localeCompare(b, 'vi'));
  if (f.topic && !topics.includes(f.topic)) f.topic = '';
  const ids = pool(f).map(q => q.id), n = ids.length;
  const nWrong = ids.filter(isWrong).length, nNew = ids.filter(id => !S.q[id]).length, nOk = n - nWrong - nNew;
  main(page('Ôn luyện', 'Ôn theo chủ đề', 'Trả lời xong là thấy ngay đáp án, giải thích và căn cứ pháp lý. Mỗi lượt trộn ưu tiên câu chưa làm, xen khoảng 30% câu bạn từng làm sai; câu đã làm đúng chỉ quay lại khi không còn câu nào khác.',
    `<div class="card stack">
      <div class="grid g3">
        <label class="f">Chứng chỉ<select id="f-cert">${opts([['', 'Tất cả môn'], ...Object.entries(CERTS).map(([k, c]) => [k, 'Chương trình ' + c.name])], f.cert)}</select></label>
        <label class="f">Phần thi<select id="f-part">${opts([['', 'Cả hai phần'], ['LUAT', PARTS.LUAT], ['CM', PARTS.CM]], f.part)}</select></label>
        <label class="f">Môn<select id="f-subject">${opts([['', 'Tất cả môn'], ...subjects.map(([c, s]) => [c, s.name])], f.subject)}</select></label>
        <label class="f">Chủ đề<select id="f-topic">${opts([['', 'Tất cả chủ đề'], ...topics.map(t => [t, t])], f.topic)}</select></label>
        <label class="f">Mức độ<select id="f-level">${opts([['', 'Mọi mức'], ...Object.entries(LEVEL)], f.level)}</select></label>
        <label class="f">Nguồn câu<select id="f-pool">${opts([['all', 'Tất cả câu phù hợp'], ['new', 'Câu chưa làm'], ['wrong', 'Câu làm sai lần gần nhất'], ['star', 'Câu đã đánh dấu']], f.pool)}</select></label>
        <label class="f">Số câu<select id="f-n">${opts([[10, '10 câu'], [20, '20 câu'], [30, '30 câu'], [50, '50 câu'], [999, 'Tất cả']], f.n)}</select></label>
      </div>
      <label class="check"><input type="checkbox" id="f-mix" ${f.mix ? 'checked' : ''}> Đảo thứ tự phương án mỗi lần làm</label>
      <div class="row between"><span class="muted small" id="f-count">Có <b>${n}</b> câu phù hợp: ${nNew} chưa làm · ${nWrong} đang sai · ${nOk} đã đúng.</span>
        <div class="row"><a class="btn" href="#ngan-hang">Xem ngân hàng</a><button class="btn primary" id="f-start" ${n ? '' : 'disabled'}>Bắt đầu ${Math.min(n, f.n)} câu</button></div></div>
    </div>`));
  const bind = (id, key, num) => ($('#' + id).onchange = e => { f[key] = num ? +e.target.value : e.target.value; if (key === 'part') f.subject = ''; VIEWS['on-luyen'](); });
  bind('f-cert', 'cert'); bind('f-part', 'part'); bind('f-subject', 'subject'); bind('f-topic', 'topic'); bind('f-level', 'level'); bind('f-pool', 'pool'); bind('f-n', 'n', true);
  $('#f-mix').onchange = e => (f.mix = e.target.checked);
  $('#f-start').onclick = () => startPractice(spread(smartPick(pool(f).map(q => q.id), f.n, topicOf)), 'Ôn luyện', f.mix);
};
async function startPractice(ids, title, mix = true, kind = 'practice') {
  if (!ids.length) return toast('Không có câu nào để luyện.');
  if (S.sess && !(await confirmBox('Bỏ bài đang làm?', `Bài "${esc(S.sess.title)}" chưa hoàn tất sẽ bị bỏ.`, 'Bỏ và bắt đầu'))) return;
  S.sess = { kind, title, mix, p: 0, i: 0, createdAt: now(), parts: [mkPart('', title, ids, mix, 0)] };
  save(); go('lam-bai');
}
function mkPart(key, label, ids, mix, minutes) {
  const perm = {};
  for (const id of ids) { const n = D.byId.get(id).o.length; const base = [...Array(n).keys()]; perm[id] = mix ? shuffle(base) : base; }
  return { key, label, ids, perm, ans: {}, flag: {}, checked: {}, minutes, startAt: null, endAt: null, done: false };
}

// ---------- ÔN LẶP LẠI ----------
VIEWS['on-tap'] = () => {
  const due = dueIds(), boxes = [0, 0, 0, 0, 0, 0];
  for (const st of Object.values(S.q)) boxes[st.box || 0]++;
  const soon = Object.values(S.q).filter(st => st.due > now() && st.due < now() + 3 * DAY).length;
  main(page('Ôn lặp lại', 'Ôn đúng lúc sắp quên', 'Câu trả lời đúng được giãn lịch ôn: 1, 3, 7, 16 rồi 35 ngày. Trả lời sai thì quay lại hộp 1 và ôn ngay.',
    `<div class="grid g3">
      <div class="card stat"><div class="k">Đến hạn hôm nay</div><div class="v">${due.length}</div><div class="d">${due.length ? 'Nên ôn trước khi học câu mới' : 'Bạn đã ôn hết câu đến hạn'}</div></div>
      <div class="card stat"><div class="k">Đến hạn trong 3 ngày tới</div><div class="v">${soon}</div></div>
      <div class="card stat"><div class="k">Đã thuộc lâu (hộp 5)</div><div class="v">${boxes[5]}</div></div>
    </div>
    <div class="card stack"><h2>Các hộp ôn tập</h2>
      <div class="grid g4">${[1, 2, 3, 4, 5].map(b => `<div class="stat"><div class="k">Hộp ${b} · ôn sau ${SRS_DAYS[b]} ngày</div><div class="v" style="font-size:1.3rem">${boxes[b]}</div></div>`).join('')}</div>
      <div class="row"><button class="btn primary" id="rv-start" ${due.length ? '' : 'disabled'}>Ôn ${Math.min(due.length, 40)} câu đến hạn</button>
      ${due.length > 40 ? `<span class="small muted">Mỗi lượt tối đa 40 câu.</span>` : ''}</div></div>`));
  $('#rv-start').onclick = () => startPractice(shuffle(due).slice(0, 40), 'Ôn lặp lại', true, 'review');
};

// ---------- TRỌNG TÂM TỪNG MÔN: chủ đề và câu bạn / mọi người hay sai ----------
const MIN_TRIES = 5;   // câu có từ 5 lượt làm (của mọi người) mới tính tỷ lệ sai chung
const errOf = id => { const s = S.q[id]; return s ? (s.n - s.ok) / s.n : 0; };
function topicBars(rows, pr) {   // rows: [chủ đề, số sai, số lượt]
  return rows.map(([t, w, n]) => `<div class="stack" style="gap:4px"><div class="row between small"><span>${esc(t)}</span>
    <span class="row"><span class="num muted">sai ${pct(w, n)}% · ${fmt(n)} lượt</span><button class="btn sm" data-${pr}="${esc(t)}">Luyện</button></span></div>
    <div class="bar"><i style="width:${pct(w, n)}%;background:var(--down)"></i></div></div>`).join('');
}
VIEWS['trong-tam'] = () => {
  const k = SUBJ[S.prefs.focus] ? S.prefs.focus : 'LU', name = SUBJ[k].name;
  const qs = D.q.filter(q => q.subject === k), ids = qs.map(q => q.id);
  const mine = {};
  for (const q of qs) { const s = S.q[q.id]; if (s) { const t = (mine[q.topic] ||= [q.topic, 0, 0]); t[1] += s.n - s.ok; t[2] += s.n; } }
  const myTopics = Object.values(mine).filter(t => t[1]).sort((a, b) => b[1] / b[2] - a[1] / a[2]);
  const myFocus = ids.filter(id => errOf(id) > 0).sort((a, b) => (S.q[a].lastOk - S.q[b].lastOk) || errOf(b) - errOf(a));
  main(page('Trọng tâm từng môn', 'Ôn đúng phần hay sai của môn sắp thi', 'Chọn chứng chỉ chuyên môn (môn) bạn sắp thi. Trang chỉ hiện chủ đề và câu của môn đó mà bạn hoặc nhiều người ôn hay làm sai, để tập trung đúng phần cần nhớ.',
    `<div class="card stack"><div class="row">${Object.entries(SUBJ).map(([c, s]) => `<button class="btn sm ${c === k ? 'primary' : ''}" data-focus="${c}" aria-pressed="${c === k}">${esc(s.short)}</button>`).join('')}</div>
      <div class="row between"><span class="small muted">Môn <b>${esc(name)}</b>: ${fmt(ids.length)} câu, bạn đã làm ${ids.filter(id => S.q[id]).length}.</span><span class="row"><button class="btn sm" id="tt-all">Luyện 20 câu môn này</button><button class="btn sm primary" id="tt-exam">Thi thử riêng môn này</button></span></div></div>
    <div class="grid g2">
      <div class="card stack"><h2>Bạn hay sai</h2>
        ${myTopics.length ? `<p class="small muted">Chủ đề sai nhiều nhất trước (tính trên mọi lượt bạn đã làm).</p>${topicBars(myTopics.slice(0, 8), 'mytopic')}
          <div class="row"><button class="btn primary" id="tt-mine">Luyện ${Math.min(myFocus.length, 20)} câu bạn hay sai nhất</button></div>`
        : '<p class="muted small">Bạn chưa làm sai câu nào của môn này. Hãy ôn luyện hoặc thi thử môn này trước, phần trọng tâm sẽ tự hiện ra.</p>'}</div>
      <div class="card stack"><h2>Nhiều người sai</h2><div id="tt-comm" data-k="${k}" class="stack"><p class="small muted">Đang tải số liệu chung…</p></div></div>
    </div>
    <p class="tiny muted">Số liệu chung là tổng hợp ẩn danh từ người ôn trên trang (chỉ gồm mã câu và đúng/sai), không có thông tin cá nhân. Có thể tắt góp dữ liệu trong Cài đặt.</p>`));
  const practiceTopic = t => startPractice(spread(smartPick(qs.filter(q => q.topic === t).map(q => q.id), 20)), `${SUBJ[k].short} · ${t}`, true);
  $$('[data-focus]').forEach(b => (b.onclick = () => { S.prefs.focus = b.dataset.focus; save(); VIEWS['trong-tam'](); }));
  $$('[data-mytopic]').forEach(b => (b.onclick = () => practiceTopic(b.dataset.mytopic)));
  $('#tt-mine') && ($('#tt-mine').onclick = () => startPractice(spread(myFocus.slice(0, 20)), 'Câu bạn hay sai · ' + SUBJ[k].short, true));
  $('#tt-exam').onclick = () => { S.prefs.type = k; save(); go('thi-thu'); };
  $('#tt-all').onclick = () => startPractice(spread(smartPick(ids, 20, topicOf)), 'Ôn luyện · ' + SUBJ[k].short, true);
  loadComm().then(C => {
    const el = $('#tt-comm'); if (!el || el.dataset.k !== k) return;   // đã chuyển sang môn/trang khác
    const cn = id => C?.n?.[id] || 0, cw = id => C?.w?.[id] || 0;
    const top = {};
    for (const q of qs) if (cn(q.id)) { const t = (top[q.topic] ||= [q.topic, 0, 0]); t[1] += cw(q.id); t[2] += cn(q.id); }
    const cTopics = Object.values(top).filter(t => t[2] >= MIN_TRIES * 2 && t[1]).sort((a, b) => b[1] / b[2] - a[1] / a[2]);
    const hard = ids.filter(id => cn(id) >= MIN_TRIES && cw(id) / cn(id) >= 0.3).sort((a, b) => cw(b) / cn(b) - cw(a) / cn(a));
    if (!cTopics.length) { el.innerHTML = `<p class="muted small">${C && !C.off ? 'Chưa đủ lượt làm bài của mọi người cho môn này. Số liệu sẽ tự hiện khi có thêm người ôn.' : 'Số liệu chung chưa được bật trên máy chủ.'}</p>`; return; }
    el.innerHTML = `<p class="small muted">Chủ đề có tỷ lệ sai cao nhất trong ${fmt(Object.values(top).reduce((s, t) => s + t[2], 0))} lượt làm của mọi người.</p>${topicBars(cTopics.slice(0, 8), 'ctopic')}
      ${hard.length ? `<div class="row"><button class="btn primary" id="tt-hard">Luyện ${Math.min(hard.length, 20)} câu nhiều người sai nhất</button></div>` : ''}`;
    $$('[data-ctopic]').forEach(b => (b.onclick = () => practiceTopic(b.dataset.ctopic)));
    $('#tt-hard') && ($('#tt-hard').onclick = () => startPractice(spread(hard.slice(0, 20)), 'Câu nhiều người sai · ' + SUBJ[k].short, true));
  });
};

// Học phí khóa chứng chỉ chuyên môn theo trang giới thiệu 08 chương trình của SRTC (truy cập 11/2026)
const SRTC_FEE = { CB: 3200000, LU: 3200000, PT: 4000000, MG: 2700000, BC: 2400000, BL: 2900000, QU: 4300000, PS: 4000000 };
// Mẹo riêng từng môn (hiện ở trang Thi thử từng chứng chỉ chuyên môn)
const TIPS = {
  LU: ['Môn Luật hỏi nhiều con số: tỷ lệ sở hữu, vốn, số nhà đầu tư, thời hạn (24 giờ, 10 ngày, 15 ngày…). Học bằng trang <a href="#the-nho">Thẻ ghi nhớ số liệu</a>.',
    'Đề dùng luật hiện hành: các điểm đã sửa theo Luật 56/2024, NĐ 245/2025, TT 135/2025, NĐ 306/2025 rất hay bị hỏi. Xem <a href="#thay-doi">Luật mới 2025–2026</a>.',
    'Chuyên đề Công ty đại chúng có 2 buổi học nên thường nhiều câu nhất: nắm chắc điều kiện công ty đại chúng, chào mua công khai, sở hữu nước ngoài.',
    'Phân biệt rõ ai làm gì: Bộ Tài chính, UBCKNN, Sở giao dịch, VSDC, ngân hàng giám sát. Nhiều phương án nhiễu chỉ đổi tên cơ quan.'],
  MG: ['Các chuyên đề lý thuyết (tổng quan, kỹ năng, mạng lưới khách hàng, xung đột lợi ích, quản lý nhà nước) là điểm dễ lấy: chiếm khoảng 5/7 đề, học kỹ để bù cho câu tính.',
    'Câu tính hay gặp: giá trần/sàn và bước giá, giá khớp lệnh định kỳ và liên tục, phí và thuế bán, lãi trái phiếu cộng dồn, giá trái phiếu, ký quỹ và lệnh gọi ký quỹ. Xem <a href="#cong-thuc">Công thức & máy tính</a>.',
    'Câu xung đột lợi ích: phương án đúng luôn ưu tiên lệnh và quyền lợi khách hàng, công bố xung đột cho khách hàng và không hứa hẹn lợi nhuận.',
    'Quy định giao dịch có thể đổi theo hệ thống KRX: đọc kỹ giả định trong đề (biên độ, bước giá, loại lệnh) thay vì dùng trí nhớ.'],
  CB: ['Nắm chắc khớp lệnh định kỳ và liên tục, giá trần/sàn, quyền lợi cổ phiếu phổ thông và ưu đãi, đặc điểm các loại quỹ.'],
  PT: ['Học thuộc công thức: lợi suất, CAPM, giá trái phiếu, Gordon, P/E, Sharpe. Luyện bấm máy cho nhanh. Xem <a href="#cong-thuc">Công thức & máy tính</a>.'],
};
// ---------- THI THỬ ----------
VIEWS['thi-thu'] = () => {
  const p = S.prefs, c = CERTS[p.cert], k = SUBJ[p.type] ? p.type : '';
  const typeSel = `<div class="stack" style="gap:8px"><div class="small"><b>Loại đề</b></div>
    <div class="row"><button class="btn sm ${k ? '' : 'primary'}" data-etype="" aria-pressed="${!k}">Sát hạch CCHN (Pháp luật + Chuyên môn)</button></div>
    <div class="small muted">Hoặc thi riêng từng chứng chỉ chuyên môn (chứng chỉ nhỏ):</div>
    <div class="row">${Object.entries(SUBJ).map(([x, s]) => `<button class="btn sm ${x === k ? 'primary' : ''}" data-etype="${x}" aria-pressed="${x === k}">${esc(s.short)}</button>`).join('')}</div></div>`;
  const nSel = label => `<label class="f">${label}<select id="e-n">${opts([[25, '25 câu'], [35, '35 câu'], [50, '50 câu'], [60, '60 câu']], p.n)}</select></label>`;
  const bindCommon = () => { $$('[data-etype]').forEach(b => (b.onclick = () => { p.type = b.dataset.etype; save(); VIEWS['thi-thu'](); })); $('#e-n').onchange = e => { p.n = +e.target.value; save(); }; $('#e-start').onclick = startExam; };
  if (k) {
    const ch = chapters(k), n = Math.min(p.n, D.q.filter(q => q.subject === k).length), qn = quotas(ch, n);
    const rows = ch.map((c, i) => {
      const ids = D.q.filter(q => q.subject === k && c[2].includes(q.topic)).map(q => q.id), seen = ids.filter(id => S.q[id]);
      const acc = seen.length ? seen.filter(id => S.q[id].lastOk).length / seen.length : null;
      return { name: c[0], w: c[1], q: qn[i], ids, seen: seen.length, acc, gain: qn[i] * (1 - (acc ?? 0.4)) };   // điểm có thể lấy thêm
    });
    const tot = ch.reduce((a, c) => a + c[1], 0), top = new Set([...rows].sort((a, b) => b.gain - a.gain).slice(0, 3).map(r => r.name));
    const need = Math.ceil(n * SUBJ_PASS), tips = TIPS[k] || [];
    main(page('Thi thử từng chứng chỉ chuyên môn', esc(SUBJ[k].name), 'Mô phỏng bài thi cuối khóa chứng chỉ chuyên môn: một bài, tính giờ, chỉ có câu của môn này. Không xem đáp án cho tới khi nộp.',
      `<div class="card stack">
        ${typeSel}<div class="grid g3">${nSel('Số câu')}
          <label class="f">Thời gian<select id="e-min">${opts([[30, '30 phút'], [45, '45 phút'], [60, '60 phút (như thi thật)'], [90, '90 phút']], p.min || 60)}</select></label></div>
        <div class="row"><button class="btn primary" id="e-start">Vào phòng thi ${n} câu · ${p.min || 60} phút</button><a class="btn" href="#trong-tam">Xem trọng tâm môn này</a></div>
      </div>
      <div class="card stack"><h2>Quy định thi cuối khóa (cập nhật 11/2026)</h2>
        <ul class="small stack" style="gap:6px;margin:0;padding-left:18px">
          <li><b>Hình thức:</b> trắc nghiệm trên máy tính tại SRTC, mỗi môn một ca thi <b>60 phút</b> (theo các thông báo lịch thi cuối khóa của SRTC).</li>
          <li><b>Mang theo:</b> giấy tờ tùy thân, máy tính cầm tay, có mặt trước giờ thi 15 phút.</li>
          <li><b>Chi phí:</b> học phí khóa ${esc(SUBJ[k].name)} tại SRTC ${SRTC_FEE[k] ? fmt(SRTC_FEE[k]) + ' đồng/khóa' : 'theo thông báo từng khóa'}; <b>thi lại 500.000 đồng/lượt/môn</b>. Người được miễn học hoặc đã bỏ thi trước đó nộp 1.000.000 đồng/lượt/môn. Mức theo thông báo của SRTC, có thể đổi theo từng đợt. Không nhầm với tiền thi sát hạch CCHN của UBCKNN (1.000.000 đồng/loại chứng chỉ).</li>
          <li><b>Điểm đạt:</b> thang 100, đạt từ <b>50 điểm</b> mỗi môn, tức khoảng <b>50% số câu</b>. Mức này lấy từ các nguồn tổng hợp; chưa thấy quy chế gốc công khai, hãy hỏi lại cán bộ lớp.</li>
          <li><b>Số câu:</b> SRTC chưa công bố công khai số câu từng môn. Nên luyện <b>50 câu trong 60 phút</b> (khoảng 1 phút 10 giây mỗi câu) để quen nhịp; với ${n} câu bạn cần đúng ít nhất <b>${need} câu</b>.</li>
          <li><b>Mục tiêu an toàn:</b> thi thử đạt từ <b>65%</b> trở lên 3 lần liên tiếp thì đi thi, vì đề thật có thể khó hơn đề luyện.</li>
        </ul></div>
      <div class="card stack"><h2>Tỷ trọng câu theo chuyên đề</h2>
        <p class="small muted">${SYL[k] ? `Ước tính theo số buổi học của từng chuyên đề trong chương trình SRTC (${tot} buổi học), vì SRTC không công bố cơ cấu đề. Đề thi thử ở đây chia câu đúng theo tỷ trọng này.` : 'Theo số câu của từng chủ đề trong ngân hàng.'} Dòng có nhãn <b>Ưu tiên</b> là chỗ ôn sẽ thêm được nhiều điểm nhất (tỷ trọng lớn, bạn còn sai nhiều).</p>
        <div class="stack" style="gap:10px">${rows.map(r => `<div class="stack" style="gap:4px">
          <div class="row between small"><span>${top.has(r.name) ? '<span class="chip down">Ưu tiên</span> ' : ''}${esc(r.name)}</span>
            <span class="row"><span class="num muted">${Math.round(r.w / tot * 100)}% · ≈${r.q} câu · ${r.acc === null ? 'chưa làm' : `bạn đúng ${Math.round(r.acc * 100)}%`}</span><button class="btn sm" data-ch="${esc(r.name)}">Luyện</button></span></div>
          <div class="bar"><i style="width:${Math.round(r.w / tot * 100)}%;background:var(--accent)"></i></div></div>`).join('')}</div></div>
      <div class="card stack"><h2>Mẹo làm bài để qua môn</h2>
        <ol class="small stack" style="gap:6px;margin:0;padding-left:18px">
          <li><b>Lượt 1</b> (khoảng 35 phút): làm hết câu chắc chắn, câu nào nghĩ quá 1 phút thì đánh dấu và bỏ qua. <b>Lượt 2</b>: quay lại câu đã đánh dấu. Còn 3 phút thì chọn hết các câu trống, vì bỏ trống chắc chắn mất điểm.</li>
          <li>Gạch chân từ khóa trong đề: <b>KHÔNG, NGOẠI TRỪ</b>, tối thiểu/tối đa, trước/sau, ngày/ngày làm việc, tổ chức/cá nhân.</li>
          <li>Loại phương án dùng quy định cũ hoặc sai cơ quan có thẩm quyền; hai phương án gần giống nhau thường có một cái đúng.</li>
          <li>Câu tính toán: viết công thức ra giấy nháp trước khi bấm máy, rồi so đơn vị (đồng/nghìn đồng, %/năm hay %/kỳ).</li>
          <li>Đề ôn của lớp và đề sát hạch cũ hay có câu <b>tổ hợp I, II, III, IV</b> và phương án <b>"a và b", "tất cả các phương án trên"</b>: xét đúng/sai từng mệnh đề trước rồi mới chọn tổ hợp; chỉ chọn "tất cả" khi chắc mọi mệnh đề đều đúng.</li>
          <li>Bộ đề trôi nổi trên mạng có nhiều câu theo luật cũ (ví dụ công bố thông tin bất thường trong 72 giờ, nay là <b>24 giờ</b>). Gặp đáp án khác trang này, xem phần Căn cứ của câu để biết quy định đang áp dụng.</li>
          ${tips.map(t => `<li>${t}</li>`).join('')}
        </ol></div>
      <div class="card stack"><h2>Kế hoạch 7 ngày để qua môn</h2>
        <ol class="small stack" style="gap:6px;margin:0;padding-left:18px">
          <li><b>Ngày 1:</b> thi thử 1 đề đủ giờ để biết mình đang ở đâu, rồi xem trang Trọng tâm của môn.</li>
          <li><b>Ngày 2–5:</b> mỗi ngày ôn 2 chuyên đề, bắt đầu từ các dòng <b>Ưu tiên</b> ở trên: bấm "Luyện" 20 câu cho mỗi chuyên đề, đọc kỹ giải thích các câu sai. Tối làm phần Ôn lặp lại.</li>
          <li><b>Ngày 6:</b> thi thử 2 đề, sau mỗi đề bấm "Ôn lại câu sai".</li>
          <li><b>Ngày 7:</b> không học mới: ôn câu sai, câu đã đánh dấu${k === 'LU' ? ', Thẻ ghi nhớ số liệu và Luật mới 2025–2026' : ''}.</li>
        </ol></div>`));
    bindCommon();
    $('#e-min').onchange = e => { p.min = +e.target.value; save(); VIEWS['thi-thu'](); };
    $('#e-n').onchange = e => { p.n = +e.target.value; save(); VIEWS['thi-thu'](); };
    $$('[data-ch]').forEach(b => (b.onclick = () => { const r = rows.find(x => x.name === b.dataset.ch); startPractice(spread(smartPick(r.ids, 20, topicOf)), `${SUBJ[k].short} · ${r.name}`, true); }));
    return;
  }
  const bp = Object.entries(c.blueprint).map(([k, w]) => `<span class="chip">${SUBJ[k].short} ${Math.round(w * 100)}%</span>`).join(' ');
  main(page('Thi thử', 'Thi sát hạch mô phỏng', 'Phần Pháp luật trước, phần Chuyên môn sau. Mỗi phần tính giờ riêng và phải đúng từ 60% số câu. Không xem đáp án cho tới khi nộp.',
    `<div class="card stack">
      ${typeSel}<div class="grid g3">
        <label class="f">Chứng chỉ<select id="e-cert">${opts(Object.entries(CERTS).map(([k, x]) => [k, `${x.name} · ${x.minutes}′ + ${x.minutes}′`]), p.cert)}</select></label>
        <label class="f">Phần thi<select id="e-mode">${opts([['both', 'Thi đủ 2 phần'], ['LUAT', 'Thi lại riêng phần Pháp luật'], ['CM', 'Thi lại riêng phần Chuyên môn']], p.mode || 'both')}</select></label>
        ${nSel('Số câu mỗi phần')}
      </div>
      <div class="grid g2">
        <div class="card flat stack"><div class="row between"><h3>Phần 1 · Pháp luật CK & TTCK</h3><span class="chip acc num">${c.minutes} phút</span></div>
          <p class="small muted">Chia câu theo 10 chuyên đề của chương trình Pháp luật SRTC, lấy từ ${D.q.filter(q => q.subject === 'LU').length} câu Luật đã soát theo văn bản hiện hành.</p></div>
        <div class="card flat stack"><div class="row between"><h3>Phần 2 · Chuyên môn</h3><span class="chip acc num">${c.minutes} phút</span></div>
          <p class="small muted">Chỉ gồm các môn trong điều kiện cấp CCHN ${c.name}:</p><div class="row">${bp}</div></div>
      </div>
      <p class="small muted">Đề được trộn theo tiến độ của bạn: ưu tiên câu chưa làm, xen khoảng 30% câu từng làm sai, câu đã làm đúng chỉ dùng khi thiếu câu.</p>
      <div class="note">Thời gian và mốc 60% mỗi phần theo thông báo của Hội đồng thi năm 2026. <b>Số câu mỗi phần chưa được công bố chính thức</b>, nên bạn tự chọn; tỷ trọng các môn chuyên môn là cấu hình mô phỏng.</div>
      <div class="row"><button class="btn primary" id="e-start">Vào phòng thi</button><span class="small muted">Phím tắt: <span class="kbd">1</span>–<span class="kbd">4</span> chọn đáp án, <span class="kbd">←</span> <span class="kbd">→</span> đổi câu, <span class="kbd">F</span> đánh dấu.</span></div>
    </div>`));
  $('#e-cert').onchange = e => { p.cert = e.target.value; save(); VIEWS['thi-thu'](); };
  $('#e-mode').onchange = e => { p.mode = e.target.value; save(); };
  bindCommon();
};
const topicOf = id => D.byId.get(id).topic;
// Chuyên đề của chương trình đào tạo SRTC: [tên, số buổi học, chủ đề tương ứng trong ngân hàng].
// SRTC không công bố cơ cấu đề, nên đề mô phỏng chia số câu theo số buổi học của từng chuyên đề.
const SYL = {
  LU: [['Khái quát pháp luật về CK & TTCK', 1, ['Giải thích từ ngữ', 'Nhà đầu tư chuyên nghiệp']],
    ['Pháp luật về công ty đại chúng', 2, ['Công ty đại chúng', 'Quản trị công ty đại chúng', 'Chào mua công khai', 'Sở hữu nước ngoài']],
    ['Chào bán chứng khoán ra công chúng', 1, ['Chào bán ra công chúng', 'Chào bán chứng khoán ra công chúng', 'Chào bán riêng lẻ', 'Chào bán trái phiếu', 'Chào bán riêng lẻ & phát hành khác']],
    ['Thị trường giao dịch chứng khoán', 1, ['Giao dịch chứng khoán', 'SGDCK & VSDC', 'Niêm yết & hủy niêm yết', 'CK phái sinh', 'Chứng quyền có bảo đảm']],
    ['Công ty chứng khoán & người hành nghề', 1, ['CTCK & CTQLQ', 'An toàn tài chính CTCK', 'Hạn chế tài chính CTCK', 'Tổ chức & hoạt động CTCK', 'Hoạt động CTCK', 'Vốn điều lệ CTCK', 'Chứng chỉ hành nghề & quy chế thi 2026', 'Chứng chỉ hành nghề chứng khoán']],
    ['Công ty quản lý quỹ, quỹ đầu tư, công ty đầu tư CK', 1, ['Quỹ đầu tư']],
    ['Đăng ký, lưu ký, bù trừ và thanh toán', 1, ['Đăng ký, lưu ký, bù trừ & thanh toán']],
    ['Công bố thông tin', 1, ['Công bố thông tin']],
    ['Quản lý nhà nước, giám sát, thanh tra, xử lý vi phạm', 1, ['Xử phạt vi phạm', 'Thanh tra & xử lý vi phạm', 'Giám sát & an ninh thị trường', 'Hành vi bị cấm']],
    ['Giải quyết tranh chấp, khiếu nại, tố cáo, bồi thường', 1, ['Giải quyết tranh chấp, khiếu nại & bồi thường']]],
  MG: ['Tổng quan về môi giới và tư vấn đầu tư chứng khoán', 'Kiến thức và kỹ năng cần thiết của người môi giới chứng khoán và tư vấn đầu tư chứng khoán',
    'Xây dựng mạng lưới khách hàng và chăm sóc khách hàng', 'Giao dịch cổ phiếu trên thị trường chứng khoán', 'Giao dịch trái phiếu trên thị trường chứng khoán',
    'Xung đột lợi ích và giải quyết xung đột lợi ích trong hoạt động môi giới và tư vấn đầu tư chứng khoán',
    'Quản lý Nhà nước đối với hoạt động môi giới và tư vấn đầu tư chứng khoán'].map(t => [t, 1, [t]]),
};
// Môn không có trong SYL: mỗi chủ đề của ngân hàng là một chuyên đề, tỷ trọng theo số câu.
const chapters = k => SYL[k] || [...new Set(D.q.filter(q => q.subject === k).map(q => q.topic))].map(t => [t, D.q.filter(q => q.subject === k && q.topic === t).length, [t]]);
function quotas(ch, n) {   // chia n câu theo trọng số, phần dư cho chuyên đề có số lẻ lớn nhất
  const tot = ch.reduce((s, c) => s + c[1], 0), want = ch.map(c => n * c[1] / tot), q = want.map(Math.floor);
  want.map((w, i) => [w - q[i], i]).sort((a, b) => b[0] - a[0]).slice(0, n - q.reduce((a, b) => a + b, 0)).forEach(([, i]) => q[i]++);
  return q;
}
function pickSubj(k, n) {
  const all = D.q.filter(q => q.subject === k).map(q => q.id), out = [];
  // chủ đề bạn chưa gặp lần nào được 1 câu trước, để vài đề đầu đã đi qua đủ mọi chủ đề của môn; phần còn lại chia theo tỷ trọng
  const met = new Set(all.filter(id => S.q[id]).map(topicOf));
  for (const t of shuffle([...new Set(all.map(topicOf))].filter(t => !met.has(t))).slice(0, n)) out.push(...smartPick(all.filter(id => topicOf(id) === t), 1));
  const used = new Set(out), ids = all.filter(id => !used.has(id)), m = n - out.length;
  if (!m) return out;
  const ch = chapters(k).map(c => [...c, ids.filter(id => c[2].includes(topicOf(id)))]).filter(c => c[3].length), q = quotas(ch, m);
  // đủ mặt mọi chuyên đề: đề dài hơn số chuyên đề thì mỗi chuyên đề ít nhất 1 câu; đề ngắn hơn thì nhường chỗ cho chuyên đề bạn làm ít nhất
  const seen = c => c[3].filter(id => S.q[id]).length / c[3].length + Math.random() * 0.01;
  if (m < ch.length) { q.fill(0); ch.map((c, i) => [seen(c), i]).sort((a, b) => a[0] - b[0]).slice(0, m).forEach(([, i]) => q[i] = 1); }
  else q.forEach((x, i) => { if (!x) { q[q.indexOf(Math.max(...q))]--; q[i] = 1; } });
  ch.forEach((c, i) => out.push(...smartPick(c[3], q[i], topicOf)));
  if (out.length < n) { const used = new Set(out); out.push(...smartPick(ids.filter(id => !used.has(id)), n - out.length, topicOf)); }
  return out;
}
function pickLaw(n) { return spread(pickSubj('LU', n)); }
function pickSpec(cert, n) {
  const bp = Object.entries(CERTS[cert].blueprint), want = bp.map(([k, w]) => [k, Math.floor(w * n)]);
  let left = n - want.reduce((s, x) => s + x[1], 0);
  for (let i = 0; left > 0; i = (i + 1) % want.length, left--) want[i][1]++;
  const out = [];
  for (const [k, m] of want) out.push(...pickSubj(k, m));
  if (out.length < n) {      // môn nào thiếu câu thì bù bằng môn khác trong cùng chương trình
    const used = new Set(out);
    out.push(...smartPick(D.q.filter(q => CERTS[cert].blueprint[q.subject] && !used.has(q.id)).map(q => q.id), n - out.length, topicOf));
  }
  return spread(out);
}
async function startExam() {
  const p = S.prefs, c = CERTS[p.cert], k = SUBJ[p.type] ? p.type : '', mode = k || p.mode || 'both';
  if (S.sess && !(await confirmBox('Bỏ bài đang làm?', `Bài "${esc(S.sess.title)}" chưa hoàn tất sẽ bị bỏ.`, 'Bỏ và vào thi'))) return;
  const parts = [];
  if (k) parts.push(mkPart(k === 'LU' ? 'LUAT' : 'CM', 'Môn ' + SUBJ[k].short, spread(pickSubj(k, p.n)), true, p.min || 60));
  else {
    if (mode !== 'CM') parts.push(mkPart('LUAT', 'Phần 1 · Pháp luật', pickLaw(p.n), true, c.minutes));
    if (mode !== 'LUAT') parts.push(mkPart('CM', mode === 'both' ? 'Phần 2 · Chuyên môn' : 'Phần Chuyên môn', pickSpec(p.cert, p.n), true, c.minutes));
  }
  if (parts.some(x => x.ids.length < p.n)) toast('Ngân hàng chưa đủ câu cho cấu hình này; đề sẽ ngắn hơn.');
  parts[0].startAt = now(); parts[0].endAt = now() + parts[0].minutes * 60e3;
  S.sess = { kind: 'exam', title: k ? 'Thi thử môn ' + SUBJ[k].name : 'Thi thử ' + c.name, cert: k ? null : p.cert, mode, p: 0, i: 0, createdAt: now(), parts, waiting: false, passAt: k ? SUBJ_PASS : PASS };
  save(); go('lam-bai');
}

// ---------- LÀM BÀI ----------
const part = () => S.sess.parts[S.sess.p];
const isRight = (q, chosen) => chosen === q.a;
VIEWS['lam-bai'] = () => {
  const s = S.sess;
  if (!s) return go('tong-quan');
  if (s.kind === 'exam' && s.waiting) return renderBreak();
  const pt = part();
  if (s.kind === 'exam' && now() >= pt.endAt) return finishPart(true);
  const id = pt.ids[s.i], q = D.byId.get(id);
  if (!q) { pt.ids.splice(s.i, 1); s.i = Math.min(s.i, pt.ids.length - 1); save(); if (!pt.ids.length) { S.sess = null; save(); return go('tong-quan'); } return VIEWS['lam-bai'](); }
  const practice = s.kind !== 'exam', chosen = pt.ans[id], shown = practice && pt.checked[id];
  const answered = pt.ids.filter(x => pt.ans[x] !== undefined).length;
  const optHtml = pt.perm[id].map((oi, pos) => {
    let cls = '';
    if (shown) cls = (oi === q.a ? 'ok' : (oi === chosen ? 'bad' : '')) + (justAnswered === id && (oi === q.a || oi === chosen) ? ' just' : '');
    else if (oi === chosen) cls = 'sel';
    return `<button class="opt ${cls}" data-oi="${oi}" ${shown ? 'disabled' : ''} aria-pressed="${oi === chosen}"><span class="l">${L[pos]}</span><span>${esc(q.o[oi])}</span></button>`;
  }).join('');
  const navg = pt.ids.map((x, k) => {
    let c = pt.ans[x] !== undefined ? 'done' : '';
    if (practice && pt.checked[x]) c = isRight(D.byId.get(x), pt.ans[x]) ? 'ok' : 'bad';
    return `<button data-k="${k}" class="${c} ${k === s.i ? 'cur' : ''} ${pt.flag[x] ? 'flag' : ''}" aria-label="Câu ${k + 1}">${k + 1}</button>`;
  }).join('');
  const last = s.i === pt.ids.length - 1;
  main(`<div class="page">
    <div class="head"><div><div class="eyebrow">${esc(s.title)}${s.parts.length > 1 || s.kind === 'exam' ? ' · ' + esc(pt.label) : ''}</div><h1 class="num" style="font-family:var(--font-num);font-size:1.3rem">Câu ${s.i + 1}/${pt.ids.length}</h1></div>
      <button class="btn sm" id="q-quit">${s.kind === 'exam' ? 'Rời phòng thi' : 'Kết thúc'}</button></div>
    <div class="quiz">
      <div class="card qcard" id="qcard">
        <div class="row between"><div class="row"><span class="chip acc">${esc(SUBJ[q.subject]?.short || q.subject)}</span><span class="chip">${esc(q.topic)}</span><span class="chip">${LEVEL[q.level] || ''}</span></div>
          <button class="btn sm ghost" id="q-flag" aria-pressed="${!!pt.flag[id]}">${pt.flag[id] ? '★ Đã đánh dấu' : '☆ Đánh dấu'}</button></div>
        <p class="qtext">${esc(q.q)}</p>
        <div class="opts" role="group" aria-label="Phương án">${optHtml}</div>
        <div id="explain" aria-live="polite">${shown ? explainHtml(q, chosen) : ''}</div>
        <div class="row between"><button class="btn" id="q-prev" ${s.i === 0 ? 'disabled' : ''}>← Câu trước</button>
          <button class="btn primary" id="q-next">${last ? (s.kind === 'exam' ? 'Nộp phần thi' : 'Xem kết quả') : 'Câu tiếp →'}</button></div>
      </div>
      <aside class="side">
        <div class="card stack">
          ${s.kind === 'exam' ? `<div class="small muted">Thời gian còn lại</div><div class="timer" id="timer">--:--</div>` : `<div class="small muted">Chế độ ôn: không giới hạn thời gian</div>`}
          <div class="small">Đã trả lời <b class="num">${answered}/${pt.ids.length}</b></div>
          <div class="bar"><i style="width:${pct(answered, pt.ids.length)}%"></i></div>
          <div class="navgrid">${navg}</div>
          <button class="btn ${s.kind === 'exam' ? 'primary' : ''}" id="q-submit">${s.kind === 'exam' ? 'Nộp ' + esc(pt.label.replace(/^Phần \d · /, 'phần ')) : 'Kết thúc và xem kết quả'}</button>
          <p class="tiny muted"><span class="kbd">1</span>–<span class="kbd">4</span> chọn · <span class="kbd">←</span><span class="kbd">→</span> đổi câu · <span class="kbd">F</span> đánh dấu</p>
        </div>
      </aside>
    </div></div>`);
  tick();
  $$('.opt').forEach(b => (b.onclick = () => choose(+b.dataset.oi)));
  $$('.navgrid button').forEach(b => (b.onclick = () => { s.i = +b.dataset.k; save(); VIEWS['lam-bai'](); }));
  $('#q-prev').onclick = () => move(-1);
  $('#q-next').onclick = next;
  $('#q-flag').onclick = () => { pt.flag[id] = !pt.flag[id]; if (pt.flag[id]) S.star[id] = true; save(); VIEWS['lam-bai'](); };
  $('#q-submit').onclick = submitPart;
  $('#q-quit').onclick = async () => {
    if (s.kind === 'exam') { toast('Bài thi vẫn giữ nguyên và đồng hồ vẫn chạy. Quay lại từ Tổng quan.'); go('tong-quan'); }
    else if (await confirmBox('Kết thúc phiên ôn?', 'Các câu đã trả lời vẫn được tính vào tiến độ.', 'Kết thúc')) finishPart(false);
  };
  $$('.explain [data-report]').forEach(b => (b.onclick = () => report(b.dataset.report)));
};
function explainHtml(q, chosen) {
  const ok = isRight(q, chosen);
  const m = /Luật Chứng khoán|Luật CK/.test(q.basis || '') && (q.basis || '').match(/Điều (\d+[a-z]?)/);
  return `<div class="explain"><div class="verdict ${ok ? 'ok' : 'bad'}">${ok ? 'Chính xác.' : 'Chưa đúng. Đáp án đúng: ' + esc(q.o[q.a])}</div>
    <p>${esc(q.e)}</p>
    ${q.basis ? `<p class="small"><b>Căn cứ:</b> ${esc(q.basis)}${m ? ` · <a href="#dieu-${m[1]}">Xem Điều ${m[1]}</a>` : ''}</p>` : ''}
    ${q.quote ? `<blockquote class="quote">“${esc(q.quote)}”</blockquote>` : ''}
    <div><button class="btn sm ghost" data-report="${esc(q.id)}">Báo lỗi câu này</button></div></div>`;
}
let justAnswered = null;
function choose(oi) {
  const s = S.sess, pt = part(), id = pt.ids[s.i];
  if (s.kind !== 'exam' && pt.checked[id]) return;
  pt.ans[id] = oi;
  if (s.kind !== 'exam') { pt.checked[id] = true; const ok = isRight(D.byId.get(id), oi); rec(id, ok); justAnswered = id; if (!ok) navigator.vibrate?.(12); }
  save(); VIEWS['lam-bai'](); justAnswered = null;
  if (s.kind !== 'exam') $('#explain')?.scrollIntoView({ block: 'nearest', behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth' });
}
function move(d) { const s = S.sess; s.i = Math.max(0, Math.min(part().ids.length - 1, s.i + d)); save(); VIEWS['lam-bai'](); }
function next() {
  const s = S.sess, pt = part();
  if (s.i < pt.ids.length - 1) return move(1);
  submitPart();
}
async function submitPart() {
  const s = S.sess, pt = part(), left = pt.ids.filter(x => pt.ans[x] === undefined).length;
  if (s.kind === 'exam') {
    const ok = await confirmBox('Nộp ' + pt.label + '?', left ? `Còn <b>${left}</b> câu chưa trả lời; câu bỏ trống tính là sai.` : 'Bạn đã trả lời hết các câu.', 'Nộp bài');
    if (ok) finishPart(false);
  } else finishPart(false);
}
function finishPart(auto) {
  const s = S.sess; if (!s) return;
  const pt = part(); if (pt.done) return;
  pt.done = true; pt.doneAt = now(); pt.auto = auto;
  setTimeout(flushStats, 0);
  if (s.kind === 'exam' && s.p < s.parts.length - 1) { s.p++; s.i = 0; s.waiting = true; save(); if (auto) toast('Hết giờ ' + pt.label + '. Bài đã được nộp.'); return go('lam-bai'); }
  // chấm
  const parts = s.parts.map(x => {
    const items = x.ids.map(id => ({ id, c: x.ans[id] ?? null, perm: x.perm[id] }));
    const ok = items.filter(it => it.c !== null && isRight(D.byId.get(it.id), it.c)).length;
    const n = s.kind === 'exam' ? items.length : items.filter(it => it.c !== null).length;
    return { key: x.key, label: x.label, n, ok, pass: n ? ok / n >= (s.passAt || PASS) : false, items };
  });
  if (s.kind === 'exam') for (const x of parts) for (const it of x.items) rec(it.id, it.c !== null && isRight(D.byId.get(it.id), it.c));
  const n = parts.reduce((a, x) => a + x.n, 0), ok = parts.reduce((a, x) => a + x.ok, 0);
  const res = { at: now(), kind: s.kind, title: s.title, cert: s.cert || null, passAt: s.passAt || PASS, n, ok, pass: s.kind === 'exam' ? parts.every(x => x.pass) : (n ? ok / n >= PASS : false),
    parts: parts.map(({ items, ...r }) => r) };
  S.hist.unshift(res); S.hist = S.hist.slice(0, 200);
  S.last = { ...res, parts };
  S.sess = null; save();
  if (auto) toast('Hết giờ. Bài thi đã được nộp tự động.');
  go('ket-qua');
}
function renderBreak() {
  const s = S.sess, pt = part();
  main(page('Chuyển phần thi', `Đã nộp ${esc(s.parts[s.p - 1].label)}`, 'Đồng hồ phần tiếp theo chỉ bắt đầu khi bạn bấm.',
    `<div class="card stack"><h2>${esc(pt.label)}</h2><p class="muted">${pt.ids.length} câu · ${pt.minutes} phút · cần đúng từ ${Math.ceil(pt.ids.length * PASS)} câu.</p>
      <div class="row"><button class="btn primary" id="b-go">Bắt đầu ${esc(pt.label.replace(/^Phần \d · /, 'phần '))}</button></div></div>`));
  $('#b-go').onclick = () => { s.waiting = false; pt.startAt = now(); pt.endAt = now() + pt.minutes * 60e3; save(); VIEWS['lam-bai'](); };
}
function tick() {
  const s = S.sess;
  if (!s || s.kind !== 'exam' || s.waiting) return;
  const pt = part(), left = Math.max(0, Math.ceil((pt.endAt - now()) / 1000));
  const el = $('#timer');
  if (el) { el.textContent = String(Math.floor(left / 60)).padStart(2, '0') + ':' + String(left % 60).padStart(2, '0'); el.classList.toggle('warn', left <= 300); }
  if (left === 0) finishPart(true);
}
setInterval(tick, 500);

// ---------- KẾT QUẢ ----------
let onlyWrong = false;
VIEWS['ket-qua'] = () => {
  const r = S.last;
  if (!r) return go('lich-su');
  const exam = r.kind === 'exam';
  const topics = {};
  for (const x of r.parts) for (const it of x.items) {
    const q = D.byId.get(it.id); if (!q) continue;
    const t = (topics[q.topic] ||= { ok: 0, n: 0, subj: q.subject });
    if (exam || it.c !== null) { t.n++; if (it.c !== null && isRight(q, it.c)) t.ok++; }
  }
  const tp = Object.entries(topics).filter(([, t]) => t.n).sort((a, b) => a[1].ok / a[1].n - b[1].ok / b[1].n);
  const wrongIds = r.parts.flatMap(x => x.items.filter(it => it.c !== null || exam).filter(it => !(it.c !== null && isRight(D.byId.get(it.id), it.c))).map(it => it.id)).filter(id => D.byId.has(id));
  const items = r.parts.flatMap(x => x.items.map(it => ({ ...it, part: x.label }))).filter(it => D.byId.has(it.id) && (exam || it.c !== null))
    .filter(it => !onlyWrong || !(it.c !== null && isRight(D.byId.get(it.id), it.c)));
  const p = pct(r.ok, r.n);
  const multi = r.parts.length > 1, pa = r.passAt || PASS;
  main(page(exam ? 'Kết quả thi thử' : 'Kết quả ôn luyện', exam ? (r.pass ? (multi ? 'Đạt cả hai phần' : 'Đạt') : 'Chưa đạt') : `Đúng ${r.ok}/${r.n} câu`,
    exam ? (multi ? 'Đạt khi đúng từ 60% số câu ở mỗi phần; không cộng bù điểm giữa hai phần.' : `Đạt khi đúng từ ${Math.round(pa * 100)}% số câu.`) : '',
    `${acctNudge()}<div class="card row" style="gap:22px">
      <div class="ring" style="--p:${p};--c:var(--${r.pass ? 'up' : 'down'})"><div><span><b>${p}%</b><span class="tiny muted">đúng</span></span></div></div>
      <div class="stack" style="flex:1">${r.parts.map(x => `<div class="stack" style="gap:6px"><div class="row between"><b>${esc(x.label || 'Ôn luyện')}</b>
        <span class="row"><span class="num">${x.ok}/${x.n}</span>${exam ? `<span class="chip ${x.pass ? 'up' : 'down'}">${x.pass ? 'Đạt' : 'Chưa đạt'}</span>` : ''}</span></div>
        <div class="bar"><i style="width:${pct(x.ok, x.n)}%;background:var(--${x.ok / Math.max(x.n, 1) >= pa ? 'up' : 'down'})"></i><span class="mark" style="left:${pa * 100}%"></span></div></div>`).join('')}
      </div></div>
    <div class="grid g2">
      <div class="card stack"><h2>Theo chủ đề (yếu nhất trước)</h2>${tp.slice(0, 12).map(([t, x]) => `<div class="stack" style="gap:4px"><div class="row between small"><span>${esc(t)}</span><span class="num">${x.ok}/${x.n}</span></div>
        <div class="bar"><i style="width:${pct(x.ok, x.n)}%;background:var(--${x.ok / x.n >= PASS ? 'up' : 'down'})"></i><span class="mark" style="left:60%"></span></div></div>`).join('') || '<p class="muted">Chưa có dữ liệu.</p>'}</div>
      <div class="card stack"><h2>Việc nên làm tiếp</h2>
        <p class="small muted">${wrongIds.length ? `Có ${wrongIds.length} câu sai hoặc bỏ trống. Ôn lại ngay giúp nhớ lâu hơn; các câu này cũng đã vào lịch ôn lặp lại.` : 'Không có câu sai. Hãy thử một đề mới hoặc tăng số câu.'}</p>
        <div class="row"><button class="btn primary" id="r-wrong" ${wrongIds.length ? '' : 'disabled'}>Ôn lại ${wrongIds.length} câu sai</button>
          ${exam ? '<a class="btn" href="#thi-thu">Thi đề khác</a>' : '<a class="btn" href="#on-luyen">Luyện tiếp</a>'}<a class="btn" href="#trong-tam">Trọng tâm từng môn</a></div></div>
    </div>
    <div class="card stack"><div class="row between"><h2>Xem lại từng câu</h2><button class="btn sm" id="r-filter">${onlyWrong ? 'Hiện tất cả' : 'Chỉ câu sai'}</button></div>
      ${items.map((it, k) => {
        const q = D.byId.get(it.id), right = it.c !== null && isRight(q, it.c);
        return `<details class="card flat"><summary class="row between" style="cursor:pointer;list-style:none"><span style="flex:1;min-width:0"><b class="num">${k + 1}.</b> ${esc(q.q.length > 140 ? q.q.slice(0, 140) + '…' : q.q)}</span>
          <span class="chip ${right ? 'up' : 'down'}">${right ? 'Đúng' : it.c === null ? 'Bỏ trống' : 'Sai'}</span></summary>
          <div class="stack" style="margin-top:10px">${it.perm.map((oi, pos) => `<div class="small" style="color:var(--${oi === q.a ? 'up' : oi === it.c ? 'down' : 'ink'})">${L[pos]}. ${esc(q.o[oi])}${oi === q.a ? ' ✓' : oi === it.c ? ' ✗' : ''}</div>`).join('')}
          ${explainHtml(q, it.c)}</div></details>`;
      }).join('') || '<p class="muted">Không có câu nào.</p>'}</div>`));
  $('#r-filter').onclick = () => { onlyWrong = !onlyWrong; VIEWS['ket-qua'](); };
  if (exam && r.pass && !r.celebrated && window.confetti) { r.celebrated = true; save(); window.confetti({ particleCount: 140, spread: 80, origin: { y: .3 }, colors: ['#0C2A63', '#E0B04A', '#19B47A', '#FFFFFF'], disableForReducedMotion: true }); }
  $('#r-wrong').onclick = () => startPractice(shuffle(wrongIds), 'Ôn câu sai', true);
  $$('.explain [data-report]').forEach(b => (b.onclick = () => report(b.dataset.report)));
};

// ---------- NGÂN HÀNG ----------
let bankF = { s: '', subject: '', pool: 'all', limit: 30 };
VIEWS['ngan-hang'] = () => {
  const f = bankF, term = f.s.trim().toLowerCase();
  const list = D.q.filter(q => (!f.subject || q.subject === f.subject) && (f.pool === 'all' || (f.pool === 'wrong' && S.q[q.id] && !S.q[q.id].lastOk) || (f.pool === 'star' && S.star[q.id]) || (f.pool === 'new' && !S.q[q.id])) &&
    (!term || (q.q + ' ' + q.topic + ' ' + q.basis + ' ' + q.o.join(' ')).toLowerCase().includes(term)));
  const counts = Object.keys(SUBJ).map(k => [k, D.q.filter(q => q.subject === k).length]);
  main(page('Ngân hàng câu hỏi', `${fmt(D.q.length)} câu đã soát`, 'Mỗi câu có giải thích và căn cứ. Câu Luật kèm trích nguyên văn điều khoản hiện hành (đến 11/2026).',
    `<div class="card stack">
      <div class="grid g3">
        <label class="f">Tìm theo từ khóa<input type="search" id="b-s" value="${esc(f.s)}" placeholder="vd: vốn điều lệ, công ty đại chúng, WACC"></label>
        <label class="f">Môn<select id="b-subject">${opts([['', 'Tất cả môn'], ...counts.map(([k, n]) => [k, `${SUBJ[k].name} (${n})`])], f.subject)}</select></label>
        <label class="f">Lọc<select id="b-pool">${opts([['all', 'Tất cả'], ['new', 'Chưa làm'], ['wrong', 'Làm sai lần gần nhất'], ['star', 'Đã đánh dấu']], f.pool)}</select></label>
      </div>
      <div class="row between"><span class="small muted">Tìm thấy <b>${list.length}</b> câu.</span><button class="btn sm primary" id="b-practice" ${list.length ? '' : 'disabled'}>Luyện ${Math.min(list.length, 50)} câu này</button></div>
    </div>
    <div class="stack">${list.slice(0, f.limit).map(q => `<details class="card">
      <summary style="cursor:pointer;list-style:none" class="stack"><div class="row"><span class="chip acc">${esc(SUBJ[q.subject]?.short)}</span><span class="chip">${esc(q.topic)}</span><span class="chip">${LEVEL[q.level] || ''}</span>
        ${S.q[q.id] ? `<span class="chip ${S.q[q.id].lastOk ? 'up' : 'down'}">${S.q[q.id].lastOk ? 'Đã làm đúng' : 'Đã làm sai'}</span>` : ''}</div><span>${esc(q.q)}</span></summary>
      <div class="stack" style="margin-top:12px">${q.o.map((o, i) => `<div class="small" style="${i === q.a ? 'color:var(--up);font-weight:600' : ''}">${L[i]}. ${esc(o)}${i === q.a ? ' ✓' : ''}</div>`).join('')}
        <p class="small">${esc(q.e)}</p>${q.basis ? `<p class="small muted"><b>Căn cứ:</b> ${esc(q.basis)}</p>` : ''}${q.quote ? `<blockquote class="quote small">“${esc(q.quote)}”</blockquote>` : ''}
        <div class="row"><button class="btn sm" data-star="${esc(q.id)}">${S.star[q.id] ? '★ Bỏ đánh dấu' : '☆ Đánh dấu'}</button><button class="btn sm ghost" data-report="${esc(q.id)}">Báo lỗi</button><span class="tiny muted num">${esc(q.id)}</span></div></div>
    </details>`).join('') || '<div class="card empty">Không có câu phù hợp.</div>'}</div>
    ${list.length > f.limit ? `<div class="row" style="justify-content:center"><button class="btn" id="b-more">Xem thêm 30 câu</button></div>` : ''}`));
  let timer;
  $('#b-s').oninput = e => { clearTimeout(timer); timer = setTimeout(() => { f.s = e.target.value; f.limit = 30; VIEWS['ngan-hang'](); const el = $('#b-s'); el.focus(); el.setSelectionRange(el.value.length, el.value.length); }, 250); };
  $('#b-subject').onchange = e => { f.subject = e.target.value; f.limit = 30; VIEWS['ngan-hang'](); };
  $('#b-pool').onchange = e => { f.pool = e.target.value; f.limit = 30; VIEWS['ngan-hang'](); };
  $('#b-more') && ($('#b-more').onclick = () => { f.limit += 30; VIEWS['ngan-hang'](); });
  $('#b-practice').onclick = () => startPractice(spread(smartPick(list.map(q => q.id), 50)), 'Luyện từ ngân hàng', true);
  $$('[data-star]').forEach(b => (b.onclick = () => { const id = b.dataset.star; if (S.star[id]) delete S.star[id]; else S.star[id] = true; save(); b.textContent = S.star[id] ? '★ Bỏ đánh dấu' : '☆ Đánh dấu'; }));
  $$('[data-report]').forEach(b => (b.onclick = () => report(b.dataset.report)));
};
async function report(id) {
  const v = await modal(`<h2>Báo lỗi câu ${esc(id)}</h2><p class="small muted">Ghi chú được lưu trên máy bạn. Vào Cài đặt để sao chép toàn bộ ghi chú gửi cho người biên soạn.</p>
    <label class="f">Lỗi bạn thấy<textarea id="rp-text" placeholder="vd: đáp án đúng phải là B theo khoản 2 Điều 15"></textarea></label>`, [['Hủy', '', null], ['Lưu ghi chú', 'primary', 'ok']]);
  if (v !== 'ok') return;
  S.reports.push({ id, note: modal.text.trim(), at: now() }); save(); toast('Đã lưu ghi chú báo lỗi.');
}

// ---------- THẺ GHI NHỚ ----------
let cardF = { subject: '', topic: '', onlyNew: false, i: 0, flip: false, order: null };
VIEWS['the-nho'] = () => {
  const f = cardF;
  if (!f.subject) f.subject = SUBJ[S.prefs.focus] ? S.prefs.focus : 'LU';
  const byId = new Map(D.cards.map(c => [c.id, c])), cards = D.cards.filter(c => c.subject === f.subject);
  const topics = [...new Set(cards.map(c => c.topic))].sort((a, b) => a.localeCompare(b, 'vi'));
  if (f.topic && !topics.includes(f.topic)) f.topic = '';
  let list = cards.filter(c => (!f.topic || c.topic === f.topic) && (!f.onlyNew || !S.cards[c.id]?.ok));
  if (!f.order || f.order.length !== list.length || f.order.some(id => byId.get(id)?.subject !== f.subject)) f.order = shuffle(list.map(c => c.id));
  list = f.order.map(id => byId.get(id)).filter(Boolean);
  const known = cards.filter(c => S.cards[c.id]?.ok).length;
  f.i = Math.min(f.i, Math.max(list.length - 1, 0));
  const c = list[f.i];
  const count = k => D.cards.filter(x => x.subject === k).length;
  main(page('Thẻ ghi nhớ', 'Thẻ ghi nhớ từng môn', `Con số, khái niệm, công thức hay bị hỏi của môn ${esc(SUBJ[f.subject].name)}. Đã nhớ ${known}/${cards.length} thẻ.`,
    `<div class="card stack"><div class="grid g3">
        <label class="f">Môn<select id="c-subj">${opts(Object.entries(SUBJ).filter(([k]) => count(k)).map(([k, x]) => [k, `${x.name} (${count(k)} thẻ)`]), f.subject)}</select></label>
        <label class="f">Chủ đề<select id="c-topic">${opts([['', 'Tất cả chủ đề'], ...topics.map(t => [t, t])], f.topic)}</select></label>
        <label class="check" style="align-self:end"><input type="checkbox" id="c-new" ${f.onlyNew ? 'checked' : ''}> Chỉ thẻ chưa nhớ</label>
      </div></div>
    ${c ? `<button class="card flash" id="c-card" aria-live="polite"><span class="tiny muted">${esc(c.topic)} · thẻ ${f.i + 1}/${list.length}</span>
        <span class="front">${esc(c.front)}</span>${f.flip ? `<span class="back${c.back.length > 40 ? ' long' : ''}">${esc(c.back)}</span><span class="tiny muted">${esc(c.basis)}</span>` : '<span class="small muted">Bấm để lật thẻ (phím cách)</span>'}</button>
      <div class="row" style="justify-content:center"><button class="btn" id="c-prev" ${f.i ? '' : 'disabled'}>← Trước</button>
        <button class="btn danger" id="c-no">Chưa nhớ</button><button class="btn primary" id="c-yes">Đã nhớ</button><button class="btn" id="c-next">Sau →</button></div>`
      : '<div class="card empty">Không còn thẻ nào trong bộ lọc này.</div>'}`));
  $('#c-subj').onchange = e => { f.subject = e.target.value; f.topic = ''; f.i = 0; f.order = null; f.flip = false; VIEWS['the-nho'](); };
  $('#c-topic').onchange = e => { f.topic = e.target.value; f.i = 0; f.order = null; f.flip = false; VIEWS['the-nho'](); };
  $('#c-new').onchange = e => { f.onlyNew = e.target.checked; f.i = 0; f.order = null; f.flip = false; VIEWS['the-nho'](); };
  if (!c) return;
  const step = d => { f.i = Math.max(0, Math.min(list.length - 1, f.i + d)); f.flip = false; VIEWS['the-nho'](); };
  $('#c-card').onclick = () => { f.flip = !f.flip; VIEWS['the-nho'](); };
  $('#c-prev').onclick = () => step(-1); $('#c-next').onclick = () => step(1);
  const mark = ok => { S.cards[c.id] = { ok, at: now() }; save(); if (f.onlyNew && ok) { f.order = null; f.flip = false; VIEWS['the-nho'](); } else step(1); };
  $('#c-yes').onclick = () => mark(true); $('#c-no').onclick = () => mark(false);
};

// ---------- CÔNG THỨC & MÁY TÍNH ----------
// Mỗi máy tính: dùng khi nào, đề ví dụ (= số điền sẵn), gợi ý từng ô, kết quả, và các bước giải thay đúng số người dùng nhập.
const nf = (x, d = 2) => (isFinite(x) ? x.toLocaleString('vi-VN', { maximumFractionDigits: d }) : '—');
const fmtM = x => nf(Math.round(x), 0);
const fmtP = x => nf(x * 100, 3) + '%';          // x là số thập phân (0,08 → 8%)
const pc = x => nf(x, 3) + '%';                  // x đã ở dạng % (8 → 8%)
function bond(v) {
  const k = v.k, N = Math.round(v.T * k), y = v.y / 100 / k, C = v.F * v.c / 100 / k;
  let p = 0, w = 0; const flows = [];
  for (let t = 1; t <= N; t++) { const cf = C + (t === N ? v.F : 0), pv = cf / (1 + y) ** t; p += pv; w += t * pv; flows.push([t, cf, pv]); }
  const mac = w / p / k; return { p, mac, mod: mac / (1 + y), N, C, y, flows };
}
const ytmOf = v => { let lo = -0.99, hi = 5; for (let i = 0; i < 200; i++) { const mid = (lo + hi) / 2; bond({ ...v, y: mid * 100 }).p > v.P ? (lo = mid) : (hi = mid); } return (lo + hi) / 2; };
const CALCS = [
  { id: 'tvm', t: 'Giá trị thời gian của tiền (lãi kép)', when: 'Biết số tiền hôm nay, muốn biết sau vài năm thành bao nhiêu khi lãi được nhập vào gốc nhiều lần trong năm.',
    ex: 'Gửi 100 triệu, lãi 8%/năm, nhập lãi mỗi quý. Sau 3 năm nhận về bao nhiêu?', f: 'FV = PV × (1 + r/m)^(m·n) · EAR = (1 + r/m)^m − 1',
    in: [['pv', 'Số tiền ban đầu PV (đ)', 100e6, 'Gõ 100000000 cho 100 triệu'], ['r', 'Lãi suất năm r (%)', 8, '8 nghĩa là 8%/năm'], ['n', 'Số năm n', 3], ['m', 'Số lần nhập lãi mỗi năm m', 4, 'Hằng năm = 1 · hằng quý = 4 · hằng tháng = 12']],
    run: v => [['Số tiền sau cùng FV', fmtM(v.pv * (1 + v.r / 100 / v.m) ** (v.m * v.n)) + ' đ'], ['Lãi suất hiệu dụng EAR', fmtP((1 + v.r / 100 / v.m) ** v.m - 1)]],
    steps: v => { const i = v.r / v.m, k = v.m * v.n, fv = v.pv * (1 + i / 100) ** k; return [
      `Lãi mỗi kỳ = r ÷ m = ${pc(v.r)} ÷ ${nf(v.m)} = <b>${pc(i)}</b>.`,
      `Số kỳ nhập lãi = m × n = ${nf(v.m)} × ${nf(v.n)} = <b>${nf(k)} kỳ</b>.`,
      `FV = PV × (1 + lãi mỗi kỳ)^số kỳ = ${fmtM(v.pv)} × (1 + ${pc(i)})^${nf(k)} = <b>${fmtM(fv)} đ</b>.`,
      `EAR = (1 + ${pc(i)})^${nf(v.m)} − 1 = <b>${fmtP((1 + i / 100) ** v.m - 1)}</b>: nhập lãi ${nf(v.m)} lần/năm ở mức ${pc(v.r)} tương đương lãi ${fmtP((1 + i / 100) ** v.m - 1)} nếu chỉ nhập 1 lần/năm.`]; } },
  { id: 'pre', t: 'Lãi suất trả trước → trả sau', when: 'Ngân hàng trả lãi ngay lúc gửi (trả trước). Muốn so sánh với lãi trả cuối kỳ thì phải quy đổi.',
    ex: 'Lãi suất trả trước 10%/năm tương đương lãi suất trả sau bao nhiêu?', f: 'r_sau = r_trước ÷ (1 − r_trước)',
    in: [['r', 'Lãi suất trả trước (%/kỳ)', 10]],
    run: v => [['Lãi suất trả sau tương đương', fmtP(v.r / 100 / (1 - v.r / 100))]],
    steps: v => [
      `Giả sử gửi 100 đồng: nhận ngay ${nf(v.r)} đồng lãi, nên thực chất chỉ bỏ ra 100 − ${nf(v.r)} = <b>${nf(100 - v.r)} đồng</b>.`,
      `Cuối kỳ nhận lại 100 đồng, tức lãi ${nf(v.r)} đồng trên ${nf(100 - v.r)} đồng bỏ ra.`,
      `r_sau = ${nf(v.r)} ÷ ${nf(100 - v.r)} = <b>${fmtP(v.r / (100 - v.r))}</b>. Lãi trả trước luôn tương đương mức trả sau cao hơn.`] },
  { id: 'bond', t: 'Định giá trái phiếu', when: 'Tính giá hợp lý của trái phiếu khi biết lãi coupon và lợi suất nhà đầu tư đòi hỏi.',
    ex: 'Trái phiếu mệnh giá 100.000 đ, coupon 8%/năm trả hằng năm, còn 5 năm. Nhà đầu tư đòi lợi suất 10%/năm. Giá hợp lý là bao nhiêu?',
    f: 'P = Σ C/(1+y)^t + F/(1+y)^N · Dmod = Dmac ÷ (1 + y)',
    in: [['F', 'Mệnh giá F (đ)', 100000], ['c', 'Lãi coupon (%/năm)', 8], ['k', 'Số lần trả lãi mỗi năm', 1, '1 = trả hằng năm · 2 = 6 tháng/lần'], ['T', 'Số năm còn lại', 5], ['y', 'Lợi suất yêu cầu (%/năm)', 10, 'Mức lợi suất nhà đầu tư muốn nhận']],
    run: v => { const b = bond(v); return [['Giá trái phiếu', fmtM(b.p) + ' đ'], ['Lợi suất hiện hành', fmtP(v.c / 100 * v.F / b.p)], ['Duration Macaulay (năm)', nf(b.mac, 3)], ['Duration điều chỉnh', nf(b.mod, 3)]]; },
    steps: v => { const b = bond(v), fl = b.flows.length > 6 ? [...b.flows.slice(0, 2), null, b.flows.at(-1)] : b.flows; return [
      `Tiền lãi mỗi kỳ C = F × coupon ÷ số lần trả = ${fmtM(v.F)} × ${pc(v.c)} ÷ ${nf(v.k)} = <b>${fmtM(b.C)} đ</b>, nhận trong <b>${b.N} kỳ</b>.`,
      `Lợi suất mỗi kỳ y = ${pc(v.y)} ÷ ${nf(v.k)} = <b>${pc(b.y * 100)}</b>.`,
      `Quy từng khoản tiền về hiện tại: ` + fl.map(f => f ? `kỳ ${f[0]}: ${fmtM(f[1])} ÷ (1 + ${pc(b.y * 100)})^${f[0]} ≈ ${fmtM(f[2])}` : '…').join('; ') + ` (kỳ cuối nhận cả lãi lẫn mệnh giá).`,
      `Cộng lại (lấy số chưa làm tròn): <b>P = ${fmtM(b.p)} đ</b>. ${v.c < v.y ? 'Coupon thấp hơn lợi suất yêu cầu nên giá thấp hơn mệnh giá (trái phiếu chiết khấu).' : v.c > v.y ? 'Coupon cao hơn lợi suất yêu cầu nên giá cao hơn mệnh giá (trái phiếu có phụ trội).' : 'Coupon bằng lợi suất yêu cầu nên giá bằng mệnh giá.'}`,
      `Duration điều chỉnh ${nf(b.mod, 2)}: nếu lợi suất tăng 1% thì giá giảm khoảng ${nf(b.mod, 2)}%.`]; } },
  { id: 'ytm', t: 'Lợi suất đáo hạn (YTM)', when: 'Biết giá đang mua trái phiếu, muốn biết nếu giữ đến đáo hạn thì mỗi năm lời bao nhiêu phần trăm.',
    ex: 'Trái phiếu mệnh giá 100.000 đ, coupon 8%/năm trả hằng năm, còn 5 năm, đang bán 95.000 đ. YTM là bao nhiêu?',
    f: 'Giá mua = Σ C/(1+YTM)^t + F/(1+YTM)^N · Gần đúng: YTM ≈ [C + (F − P)/N] ÷ [(F + P)/2]',
    in: [['F', 'Mệnh giá F (đ)', 100000], ['c', 'Lãi coupon (%/năm)', 8], ['k', 'Số lần trả lãi mỗi năm', 1, '1 = trả hằng năm · 2 = 6 tháng/lần'], ['T', 'Số năm còn lại', 5], ['P', 'Giá đang mua P (đ)', 95000]],
    run: v => [['YTM', fmtP(ytmOf(v))]],
    steps: v => { const y = ytmOf(v), C = v.F * v.c / 100, ap = (C + (v.F - v.P) / v.T) / ((v.F + v.P) / 2); return [
      `Dòng tiền: mỗi năm nhận lãi ${fmtM(C)} đ; năm thứ ${nf(v.T)} nhận thêm mệnh giá ${fmtM(v.F)} đ.`,
      `Tìm lợi suất sao cho tổng giá trị hiện tại của dòng tiền đúng bằng giá mua ${fmtM(v.P)} đ (máy thử dần). Với YTM = ${fmtP(y)}, giá lý thuyết = <b>${fmtM(bond({ ...v, y: y * 100 }).p)} đ</b> ✓.`,
      `Đi thi không có máy, dùng công thức gần đúng: [${fmtM(C)} + (${fmtM(v.F)} − ${fmtM(v.P)}) ÷ ${nf(v.T)}] ÷ [(${fmtM(v.F)} + ${fmtM(v.P)}) ÷ 2] ≈ <b>${fmtP(ap)}</b>, rồi chọn đáp án gần nhất.`,
      v.P < v.F ? `Mua dưới mệnh giá nên YTM (${fmtP(y)}) cao hơn coupon (${pc(v.c)}).` : v.P > v.F ? `Mua trên mệnh giá nên YTM (${fmtP(y)}) thấp hơn coupon (${pc(v.c)}).` : 'Mua đúng mệnh giá nên YTM bằng coupon.']; } },
  { id: 'capm', t: 'CAPM: cổ phiếu đắt hay rẻ?', when: 'Tính lợi suất tối thiểu nên đòi hỏi ở một cổ phiếu theo mức rủi ro (beta), rồi so với lợi suất bạn dự kiến.',
    ex: 'Lãi suất phi rủi ro 4%, lợi suất thị trường 12%, cổ phiếu có beta 1,2 và bạn dự kiến lời 15%. Có nên mua?', f: 'E(r) = rf + β × (rm − rf)',
    in: [['rf', 'Lãi suất phi rủi ro rf (%)', 4, 'Thường lấy lợi suất trái phiếu Chính phủ'], ['b', 'Hệ số beta β', 1.2, 'β > 1: biến động mạnh hơn thị trường'], ['rm', 'Lợi suất thị trường rm (%)', 12], ['er', 'Lợi suất bạn dự kiến (%)', 15]],
    run: v => { const req = v.rf + v.b * (v.rm - v.rf); return [['Lợi suất yêu cầu', pc(req)], ['Kết luận', v.er > req ? 'Định giá thấp, nên mua' : v.er < req ? 'Định giá cao, không nên mua' : 'Định giá hợp lý']]; },
    steps: v => { const prem = v.rm - v.rf, req = v.rf + v.b * prem; return [
      `Phần bù rủi ro thị trường = rm − rf = ${pc(v.rm)} − ${pc(v.rf)} = <b>${pc(prem)}</b>.`,
      `Nhân với beta: ${nf(v.b)} × ${pc(prem)} = <b>${pc(v.b * prem)}</b> (phần bù cho rủi ro riêng của cổ phiếu này).`,
      `Lợi suất yêu cầu E(r) = ${pc(v.rf)} + ${pc(v.b * prem)} = <b>${pc(req)}</b>.`,
      v.er > req ? `Bạn dự kiến ${pc(v.er)} > ${pc(req)}: cổ phiếu nằm <b>phía trên đường SML</b>, đang bị định giá thấp, nên mua.`
        : v.er < req ? `Bạn dự kiến ${pc(v.er)} < ${pc(req)}: cổ phiếu nằm <b>phía dưới đường SML</b>, đang bị định giá cao, không nên mua.` : 'Bằng nhau: nằm đúng trên SML, định giá hợp lý.']; } },
  { id: 'ddm', t: 'Mô hình Gordon (cổ tức tăng đều)', when: 'Định giá cổ phiếu của công ty trả cổ tức và cổ tức tăng đều mãi mãi.',
    ex: 'Công ty vừa trả cổ tức 2.000 đ/cp, cổ tức tăng đều 5%/năm, nhà đầu tư đòi lợi suất 12%. Giá hợp lý?', f: 'P0 = D1 ÷ (r − g) · D1 = D0 × (1 + g)',
    in: [['d0', 'Cổ tức vừa trả D0 (đ)', 2000], ['g', 'Tốc độ tăng cổ tức g (%)', 5], ['r', 'Lợi suất yêu cầu r (%)', 12, 'Phải lớn hơn g']],
    run: v => v.r <= v.g ? [['Lỗi', 'Cần r lớn hơn g']] : [['Cổ tức năm sau D1', fmtM(v.d0 * (1 + v.g / 100)) + ' đ'], ['Giá hợp lý P0', fmtM(v.d0 * (1 + v.g / 100) / ((v.r - v.g) / 100)) + ' đ']],
    steps: v => v.r <= v.g ? ['Mô hình chỉ dùng được khi lợi suất yêu cầu r lớn hơn tốc độ tăng g.'] : [
      `Cổ tức năm sau D1 = D0 × (1 + g) = ${fmtM(v.d0)} × (1 + ${pc(v.g)}) = <b>${fmtM(v.d0 * (1 + v.g / 100))} đ</b>.`,
      `P0 = D1 ÷ (r − g) = ${fmtM(v.d0 * (1 + v.g / 100))} ÷ (${pc(v.r)} − ${pc(v.g)}) = <b>${fmtM(v.d0 * (1 + v.g / 100) / ((v.r - v.g) / 100))} đ</b>.`,
      `Lỗi hay gặp: chia D0 thay vì D1 sẽ ra ${fmtM(v.d0 / ((v.r - v.g) / 100))} đ, thường là một phương án nhiễu.`] },
  { id: 'wacc', t: 'Chi phí vốn bình quân (WACC)', when: 'Tính chi phí trung bình của toàn bộ vốn công ty dùng (vốn chủ và vốn vay), làm lãi suất chiết khấu khi thẩm định dự án.',
    ex: 'Công ty có vốn chủ 600 tỷ (chi phí 15%), nợ vay 400 tỷ (lãi 9%), thuế TNDN 20%. WACC bằng bao nhiêu?', f: 'WACC = E/V × re + D/V × rd × (1 − t)',
    in: [['E', 'Vốn chủ sở hữu E', 600, 'Cùng đơn vị với D (tỷ, triệu…)'], ['Dv', 'Nợ vay D', 400], ['re', 'Chi phí vốn chủ re (%)', 15], ['rd', 'Lãi vay rd (%)', 9], ['t', 'Thuế suất TNDN t (%)', 20]],
    run: v => { const V = v.E + v.Dv; return [['WACC', fmtP((v.E / V) * v.re / 100 + (v.Dv / V) * v.rd / 100 * (1 - v.t / 100))]]; },
    steps: v => { const V = v.E + v.Dv, we = v.E / V, wd = v.Dv / V, rdt = v.rd * (1 - v.t / 100); return [
      `Tổng vốn V = E + D = ${nf(v.E)} + ${nf(v.Dv)} = ${nf(V)} → tỷ trọng vốn chủ <b>${fmtP(we)}</b>, nợ <b>${fmtP(wd)}</b>.`,
      `Lãi vay được trừ khi tính thuế, nên chi phí nợ sau thuế = ${pc(v.rd)} × (1 − ${pc(v.t)}) = <b>${pc(rdt)}</b>.`,
      `WACC = ${fmtP(we)} × ${pc(v.re)} + ${fmtP(wd)} × ${pc(rdt)} = ${pc(we * v.re)} + ${pc(wd * rdt)} = <b>${pc(we * v.re + wd * rdt)}</b>.`]; } },
  { id: 'adj', t: 'Giá tham chiếu điều chỉnh (ngày GDKHQ)', when: 'Ngày giao dịch không hưởng quyền, sàn hạ giá tham chiếu vì người mua từ hôm đó không còn nhận cổ tức hoặc quyền mua.',
    ex: 'Giá đóng cửa 30.000 đ. Công ty trả cổ tức tiền 2.000 đ/cp và phát hành thêm theo tỷ lệ 2:1 (2 cổ phiếu cũ mua 1 cổ phiếu mới) giá 10.000 đ. Giá tham chiếu ngày GDKHQ?',
    f: "P' = (P − Cổ tức tiền + PR × I1) ÷ (1 + I1 + I2)",
    in: [['P', 'Giá đóng cửa trước ngày GDKHQ P (đ)', 30000], ['C', 'Cổ tức tiền mặt mỗi cổ phiếu (đ)', 2000, 'Cổ tức 20% mệnh giá 10.000 đ = 2.000 đ'], ['PR', 'Giá mua cổ phiếu phát hành thêm PR (đ)', 10000],
      ['I1', 'Tỷ lệ quyền mua I1', 0.5, 'Tỷ lệ 2:1 → gõ 0.5 · 10:2 → gõ 0.2 · không có thì gõ 0'], ['I2', 'Tỷ lệ cổ tức bằng cổ phiếu I2', 0, 'Thưởng 10% (10:1) → gõ 0.1 · không có thì gõ 0']],
    run: v => [['Giá tham chiếu điều chỉnh', fmtM((v.P - v.C + v.PR * v.I1) / (1 + v.I1 + v.I2)) + ' đ']],
    steps: v => { const top = v.P - v.C + v.PR * v.I1, bot = 1 + v.I1 + v.I2; return [
      `Tử số = P − cổ tức tiền + PR × I1 = ${fmtM(v.P)} − ${fmtM(v.C)} + ${fmtM(v.PR)} × ${nf(v.I1)} = <b>${fmtM(top)}</b>.`,
      `Mẫu số = 1 + I1 + I2 = 1 + ${nf(v.I1)} + ${nf(v.I2)} = <b>${nf(bot, 4)}</b>.`,
      `P' = ${fmtM(top)} ÷ ${nf(bot, 4)} = <b>${fmtM(top / bot)} đ</b>.`,
      'Đổi tỷ lệ "a:b" thành số: lấy b ÷ a (số cổ phiếu mới được mua hoặc được thưởng trên 1 cổ phiếu cũ).']; } },
  { id: 'perf', t: 'Đo lường hiệu quả danh mục', when: 'So sánh hiệu quả các quỹ hoặc danh mục khi đã tính đến rủi ro. Cả ba chỉ số đều càng cao càng tốt.',
    ex: 'Danh mục lời 14%, độ lệch chuẩn 20%, beta 1,1. Lãi suất phi rủi ro 4%, thị trường lời 11%. Tính Sharpe, Treynor, Jensen alpha.',
    f: 'Sharpe = (rp − rf) ÷ σp · Treynor = (rp − rf) ÷ βp · Jensen α = rp − [rf + βp × (rm − rf)]',
    in: [['rp', 'Lợi suất danh mục rp (%)', 14], ['rf', 'Lãi suất phi rủi ro rf (%)', 4], ['sd', 'Độ lệch chuẩn σp (%)', 20, 'Đo rủi ro tổng'], ['b', 'Beta βp', 1.1, 'Đo rủi ro theo thị trường'], ['rm', 'Lợi suất thị trường rm (%)', 11]],
    run: v => [['Sharpe', nf((v.rp - v.rf) / v.sd, 3)], ['Treynor', pc((v.rp - v.rf) / v.b)], ['Jensen alpha', pc(v.rp - (v.rf + v.b * (v.rm - v.rf)))]],
    steps: v => { const ex = v.rp - v.rf, capm = v.rf + v.b * (v.rm - v.rf); return [
      `Lợi suất vượt phi rủi ro = rp − rf = ${pc(v.rp)} − ${pc(v.rf)} = <b>${pc(ex)}</b>.`,
      `Sharpe = ${pc(ex)} ÷ ${pc(v.sd)} = <b>${nf(ex / v.sd, 3)}</b>: mỗi 1% rủi ro tổng mang lại ${nf(ex / v.sd, 3)}% lợi suất vượt trội.`,
      `Treynor = ${pc(ex)} ÷ ${nf(v.b)} = <b>${pc(ex / v.b)}</b>: lợi suất vượt trội trên mỗi đơn vị beta.`,
      `Theo CAPM, danh mục chỉ cần lời ${pc(v.rf)} + ${nf(v.b)} × (${pc(v.rm)} − ${pc(v.rf)}) = ${pc(capm)}. Jensen α = ${pc(v.rp)} − ${pc(capm)} = <b>${pc(v.rp - capm)}</b>${v.rp - capm > 0 ? ': danh mục làm tốt hơn mức đáng lẽ đạt được.' : v.rp - capm < 0 ? ': danh mục kém hơn mức đáng lẽ đạt được.' : '.'}`]; } },
];
VIEWS['cong-thuc'] = () => {
  main(page('Công thức & máy tính', 'Bấm số nhanh cho bài tính', 'Mỗi máy tính đã điền sẵn một đề ví dụ. Thay số theo đề của bạn, kết quả và lời giải từng bước tự cập nhật.',
    `<div class="card stack"><h2>Cách dùng</h2>
      <ol class="howto"><li>Chọn đúng dạng bài bên dưới (bấm tên để nhảy tới).</li><li>Thay các ô bằng số trong đề. Phần trăm gõ số thường: 8% gõ <b>8</b>; số thập phân dùng dấu chấm: 0,5 gõ <b>0.5</b>.</li><li>Đọc kết quả, rồi xem "Cách làm từng bước" để tự làm lại trên giấy khi đi thi.</li></ol>
      <div class="row">${CALCS.map(c => `<button class="chip acc jump" data-jump="${c.id}">${esc(c.t.replace(/ \(.*\)$/, ''))}</button>`).join('')}</div></div>
    <div class="grid g2">${CALCS.map(c => `<section class="card stack calc" id="calc-${c.id}"><h2>${c.t}</h2>
      <p class="small"><b>Dùng khi:</b> ${c.when}</p>
      <div class="formula">${c.f.split(' · ').map(x => `<div>${esc(x)}</div>`).join('')}</div>
      <div class="note info small"><b>Ví dụ:</b> ${esc(c.ex)} <span class="muted">Số đã điền sẵn bên dưới.</span></div>
      <div class="grid g2" style="gap:10px">${c.in.map(([k, lab, def, hint]) => `<label class="f">${lab}<input type="number" step="any" id="${c.id}-${k}" value="${def}" inputmode="decimal">
        <span class="hint">${hint ? esc(hint) : ''}<span class="echo" id="${c.id}-${k}-echo"></span></span></label>`).join('')}</div>
      <div class="stack out-wrap" id="${c.id}-out" aria-live="polite"></div>
      <details class="steps" open><summary>Cách làm từng bước</summary><ol id="${c.id}-steps"></ol></details>
      <div><button class="btn sm" data-reset="${c.id}">Điền lại số ví dụ</button></div></section>`).join('')}</div>`));
  for (const c of CALCS) {
    const run = () => {
      const v = Object.fromEntries(c.in.map(([k]) => [k, parseFloat($(`#${c.id}-${k}`).value)]));
      for (const [k] of c.in) { const x = v[k]; $(`#${c.id}-${k}-echo`).textContent = isFinite(x) && Math.abs(x) >= 10000 ? ` = ${fmtM(x)}` : ''; }
      const bad = Object.values(v).some(x => !isFinite(x));
      $(`#${c.id}-out`).innerHTML = bad ? '<p class="small muted">Nhập đủ các ô bằng số.</p>' :
        c.run(v).map(([k, val]) => `<div class="row between"><span class="small muted">${k}</span><span class="out">${esc(val)}</span></div>`).join('');
      $(`#${c.id}-steps`).innerHTML = bad ? '<li class="muted">Điền đủ các ô để xem lời giải.</li>' : c.steps(v).map(x => `<li>${x}</li>`).join('');
    };
    c.in.forEach(([k]) => ($(`#${c.id}-${k}`).oninput = run)); run();
    $(`[data-reset="${c.id}"]`).onclick = () => { c.in.forEach(([k, , def]) => ($(`#${c.id}-${k}`).value = def)); run(); };
  }
  $$('[data-jump]').forEach(b => (b.onclick = () => $('#calc-' + b.dataset.jump).scrollIntoView({ block: 'start', behavior: reduceMotion() ? 'auto' : 'smooth' })));
};

// ---------- THƯ VIỆN LUẬT ----------
let libQ = '';
VIEWS['thu-vien'] = (target) => {
  const law = D.law;
  if (!law) return main(page('Thư viện luật', 'Chưa tải được văn bản', '', '<div class="card empty">Không đọc được dữ liệu thư viện.</div>'));
  const term = libQ.trim().toLowerCase();
  const arts = law.dieu.filter(a => !term || (a.ten + ' ' + a.doan.join(' ')).toLowerCase().includes(term));
  const hl = s => { const t = esc(s); if (!term) return t; const i = t.toLowerCase().indexOf(esc(term)); return i < 0 ? t : t.slice(0, i) + '<mark class="hit">' + t.slice(i, i + esc(term).length) + '</mark>' + t.slice(i + esc(term).length); };
  const chapters = [...new Set(law.dieu.map(a => a.chuong))];
  main(page('Thư viện luật', 'Luật Chứng khoán (hợp nhất)', esc(law.van_ban) + '. Điều có dấu ✎ đã được Luật 56/2024/QH15 sửa đổi, bổ sung.',
    `<div class="card stack"><h2>Văn bản dùng để biên soạn và soát câu hỏi</h2>
      <div class="tablewrap"><table><thead><tr><th>Văn bản</th><th>Nội dung</th><th>Tình trạng (11/2026)</th></tr></thead><tbody>
      ${D.docs.map(d => `<tr><td><b>${esc(d.so)}</b></td><td>${esc(d.ten)}</td><td class="small">${esc(d.trang_thai)}</td></tr>`).join('')}</tbody></table></div></div>
    <div class="lib">
      <div class="toc-wrap card stack"><label class="f">Tìm trong luật<input type="search" id="l-q" value="${esc(libQ)}" placeholder="vd: công ty đại chúng"></label>
        <div class="tiny muted">${arts.length} điều phù hợp</div>
        <div class="toc">${arts.map(a => `<a href="#dieu-${a.so}">Điều ${a.so}. ${esc(a.ten)}${a.sua_doi ? ' ✎' : ''}</a>`).join('')}</div></div>
      <div class="card law">${chapters.map(ch => {
        const list = arts.filter(a => a.chuong === ch); if (!list.length) return '';
        return `<h2 style="margin-top:8px">${esc(ch)}</h2>` + list.map(a => `<section class="art" id="art-${a.so}"><h3>Điều ${a.so}. ${hl(a.ten)}${a.sua_doi ? ' <span class="chip ref">✎ đã sửa đổi</span>' : ''}</h3>
          ${a.doan.map(p => `<p class="${/^[a-zđ]\)/.test(p) ? 'lvl2' : ''}">${hl(p)}</p>`).join('')}
          ${a.ghi_chu?.length ? `<p class="tiny muted" style="margin-top:8px">${a.ghi_chu.map(esc).join('<br>')}</p>` : ''}</section>`).join('');
      }).join('') || '<p class="muted">Không có điều nào chứa từ khóa này.</p>'}</div>
    </div>`));
  let t; $('#l-q').oninput = e => { clearTimeout(t); t = setTimeout(() => { libQ = e.target.value; VIEWS['thu-vien'](); const el = $('#l-q'); el.focus(); el.setSelectionRange(el.value.length, el.value.length); }, 300); };
  if (target) { if (libQ) { libQ = ''; return VIEWS['thu-vien'](target); } const el = document.getElementById('art-' + target); if (el) setTimeout(() => el.scrollIntoView({ block: 'start' }), 30); }
};

// ---------- LUẬT MỚI ----------
const dkey = d => String(d || '').split('/').reverse().join('');   // dd/mm/yyyy -> yyyymmdd để sắp xếp
VIEWS['thay-doi'] = () => {
  main(page('Luật mới 2025–2026', 'Những quy định đã thay đổi', 'Tổng hợp các thay đổi hay xuất hiện trong đề, đã đối chiếu nguyên văn văn bản. Câu hỏi theo quy định cũ trên các trang khác có thể đã sai.',
    `<div class="card"><div class="timeline">${[...D.changes].sort((x, y) => dkey(x.effective).localeCompare(dkey(y.effective))).map(c => `<div class="it"><div class="num small muted">${esc(c.effective)}</div>
      <div class="stack" style="gap:4px"><h3>${esc(c.title)}</h3><p class="small">${esc(c.what)}</p><p class="tiny muted">${esc(c.doc)}</p></div></div>`).join('') || '<p class="muted">Chưa có dữ liệu.</p>'}</div></div>`));
};

// ---------- QUY CHẾ ----------
VIEWS['quy-che'] = () => {
  const src = [
    ['Thông báo số 01/TB-HĐTSH năm 2026 (nhận hồ sơ đợt I, mức điểm đạt, không phúc khảo)', 'https://ssc.gov.vn/cs/idcplg?IdcService=GET_FILE&dDocName=APPSSCGOVVN1620165156'],
    ['Thông báo số 11 năm 2026 (lịch, thời gian làm bài đợt III)', 'https://ssc.gov.vn/cs/idcplg?IdcService=GET_FILE&dDocName=APPSSCGOVVN1620174264'],
    ['Nghị định 245/2025/NĐ-CP (sửa Điều 213–215 NĐ 155/2020)', 'https://congbao.chinhphu.vn'],
    ['SRTC: 08 chương trình đào tạo chuyên môn', 'https://www.srtc.org.vn/p/gioi-thieu-8-chuong-trinh-dao-tao-cap-chung-chi-chuyen-mon'],
  ];
  main(page('Quy chế thi 2026', 'Thi sát hạch CCHN chứng khoán', 'Tóm tắt từ Nghị định 245/2025, Thông tư 135/2025 và thông báo của Hội đồng thi sát hạch năm 2026.',
    `<div class="card stack"><h2>Cấu trúc và thời gian</h2>
      <div class="tablewrap"><table><thead><tr><th>Chứng chỉ</th><th class="r">Phần Pháp luật</th><th class="r">Phần Chuyên môn</th><th class="r">Tổng</th></tr></thead><tbody>
        ${Object.values(CERTS).map(c => `<tr><td>${c.name}</td><td class="r num">${c.minutes}′</td><td class="r num">${c.minutes}′</td><td class="r num">${c.minutes * 2}′</td></tr>`).join('')}</tbody></table></div>
      <p class="small muted">Thi trắc nghiệm trên máy tính. Hai phần làm liên tiếp, có nghỉ ngắn giữa hai phần theo lịch của từng đợt.</p></div>
    <div class="grid g2">
      <div class="card stack"><h2>Điều kiện đạt</h2><p>Trả lời đúng <b>từ 60% số câu của mỗi phần</b>, ở cả hai phần. Không cộng bù điểm giữa hai phần.</p>
        <p class="small muted">Thi lại một phần: cũng cần đúng từ 60% số câu của phần thi lại.</p></div>
      <div class="card stack"><h2>Thi lại phần chưa đạt</h2><p>Được thi lại riêng phần chưa đạt <b>trong 01 năm</b> kể từ ngày công bố kết quả lần đầu <b>hoặc ở đợt thi liền kề</b>; quá thời hạn phải thi lại cả hai phần.</p>
        <p class="small muted">Điều 213 NĐ 155/2020, sửa bởi khoản 73 Điều 1 NĐ 245/2025.</p></div>
      <div class="card stack"><h2>Phúc khảo</h2><p>Hội đồng thi <b>không tổ chức phúc khảo</b> bài thi trắc nghiệm trên máy tính.</p></div>
      <div class="card stack"><h2>Sau khi đạt</h2><p>UBCKNN ra quyết định cấp CCHN trong <b>30 ngày</b> kể từ ngày kết quả thi được thông báo. Nộp Phiếu lý lịch tư pháp trong 20 ngày sau khi có kết quả nếu chưa nộp.</p>
        <p class="small muted">Tiền dự thi sát hạch: 1.000.000 đồng/thí sinh/loại chứng chỉ, áp dụng cho cả thi mới và thi lại (mục 5.1 Thông báo 01/TB-HĐTSH năm 2026). Đây là kỳ thi của UBCKNN, khác với thi cuối khóa chứng chỉ chuyên môn tại SRTC (thi lại 500.000 đồng/lượt/môn).</p></div>
    </div>
    <div class="card stack"><h2>Môn chuyên môn bắt buộc theo chứng chỉ</h2>
      <div class="tablewrap"><table><thead><tr><th>Chứng chỉ</th><th>Chứng chỉ chuyên môn cần có</th></tr></thead><tbody>
        <tr><td>Môi giới chứng khoán</td><td>Cơ bản về CK & TTCK; Pháp luật về CK & TTCK; Phân tích & đầu tư CK; Môi giới & tư vấn đầu tư CK</td></tr>
        <tr><td>Phân tích tài chính</td><td>Các môn của Môi giới + Tư vấn tài chính & bảo lãnh phát hành + Phân tích báo cáo tài chính doanh nghiệp</td></tr>
        <tr><td>Quản lý quỹ</td><td>Các môn của Phân tích tài chính + Quản lý quỹ & tài sản; thêm tối thiểu 3 năm kinh nghiệm phù hợp hoặc giấy phép hành nghề quản lý quỹ ở nước ngoài</td></tr>
      </tbody></table></div>
      <p class="small muted">Môn Phái sinh không thuộc điều kiện của ba chứng chỉ trên; ứng dụng chỉ dùng cho ôn luyện.</p>
      <div class="note info">Từ 09/02/2026 (Thông tư 135/2025/TT-BTC): người tốt nghiệp khối Kinh tế, Kinh doanh, Tài chính – Ngân hàng – Bảo hiểm, Kế toán – Kiểm toán được miễn học môn Cơ bản; tốt nghiệp Luật kinh tế được miễn học môn Pháp luật (vẫn phải thi đạt bài kiểm tra của SRTC). CFA từ cấp II, CIIA được công nhận tương đương một số môn. CCHN có thể cấp bản điện tử; từ 01/01/2027 người hành nghề phải cập nhật kiến thức tối thiểu 8 giờ mỗi năm.</div>
    </div>
    <div class="card stack"><h2>Lịch thi năm 2026</h2>
      <div class="tablewrap"><table><tbody><tr><td>Đợt I</td><td>TP. Hồ Chí Minh, tháng 4</td></tr><tr><td>Đợt II</td><td>Hà Nội, 23–24/7</td></tr><tr><td>Đợt III</td><td>TP. Hồ Chí Minh, 31/10–01/11</td></tr><tr><td>Đợt IV</td><td>Hà Nội, dự kiến tháng 11</td></tr></tbody></table></div>
      <p class="small muted">Lịch chính thức từng đợt đăng trên trang của UBCKNN và SRTC.</p></div>
    <div class="card stack"><h2>Nguồn</h2>${src.map(([t, u]) => `<p class="small"><a href="${u}" target="_blank" rel="noopener">${esc(t)}</a></p>`).join('')}
      <p class="small muted">Số câu hỏi mỗi phần chưa được công bố trong văn bản chính thức nào.</p></div>`));
};

// ---------- LỊCH SỬ ----------
VIEWS['lich-su'] = () => {
  const ex = S.hist.filter(h => h.kind === 'exam').slice(0, 30).reverse();
  const W = 600, H = 120, pad = 20;
  const pts = key => ex.map((h, i) => { const p = h.parts.find(x => x.key === key); return p ? [pad + (ex.length > 1 ? i * (W - 2 * pad) / (ex.length - 1) : (W - 2 * pad) / 2), H - pad - (p.ok / Math.max(p.n, 1)) * (H - 2 * pad)] : null; }).filter(Boolean);
  const line = (key, color) => { const p = pts(key); return p.length ? `<polyline fill="none" stroke="var(--${color})" stroke-width="2.5" points="${p.map(x => x.join(',')).join(' ')}"/>` + p.map(([x, y]) => `<circle cx="${x}" cy="${y}" r="3.5" fill="var(--${color})"/>`).join('') : ''; };
  const y60 = H - pad - .6 * (H - 2 * pad);
  main(page('Lịch sử & tiến độ', 'Kết quả các lần làm bài', `${S.hist.length} lượt đã lưu trên máy này.`,
    `${ex.length ? `<div class="card stack"><div class="row between"><h2>Điểm thi thử theo thời gian</h2><div class="legend"><span><i style="background:var(--accent)"></i>Pháp luật</span><span><i style="background:var(--ceil)"></i>Chuyên môn</span><span><i style="background:var(--ink);height:2px"></i>Mốc 60%</span></div></div>
      <svg class="spark" viewBox="0 0 ${W} ${H}" preserveAspectRatio="none" role="img" aria-label="Biểu đồ tỷ lệ đúng các lần thi thử">
        <line x1="${pad}" x2="${W - pad}" y1="${y60}" y2="${y60}" stroke="var(--ink)" stroke-dasharray="4 4" opacity=".5"/>${line('LUAT', 'accent')}${line('CM', 'ceil')}</svg></div>` : ''}
    <div class="card"><div class="tablewrap"><table><thead><tr><th>Thời gian</th><th>Bài</th><th>Chi tiết</th><th class="r">Đúng</th><th>Kết quả</th></tr></thead><tbody>
      ${S.hist.map(h => `<tr><td class="num small">${dt(h.at)}</td><td>${esc(h.title)}</td><td class="small muted">${h.parts.map(p => `${esc(p.label || 'Ôn')}: ${p.ok}/${p.n}`).join(' · ')}</td>
        <td class="r num">${pct(h.ok, h.n)}%</td><td><span class="chip ${h.pass ? 'up' : 'down'}">${h.pass ? 'Đạt' : 'Chưa đạt'}</span></td></tr>`).join('') || '<tr><td colspan="5" class="empty">Chưa có lượt làm bài nào.</td></tr>'}
    </tbody></table></div></div>`));
};

// ---------- CÀI ĐẶT ----------
VIEWS['cai-dat'] = () => {
  const dump = JSON.stringify({ app: 'docchn', v: 1, at: now(), q: S.q, star: S.star, hist: S.hist, cards: S.cards, reports: S.reports });
  const reports = S.reports.map(r => `${r.id}: ${r.note}`).join('\n');
  main(page('Cài đặt & sao lưu', 'Tiến độ của bạn', 'Tiến độ học tập lưu trong trình duyệt này. Sao lưu để chuyển sang máy khác.',
    `<div class="grid g2">
      <div class="card stack"><h2>Giao diện</h2><label class="f">Chế độ màu<select id="s-theme">${opts([['', 'Theo hệ thống'], ['light', 'Sáng'], ['dark', 'Tối']], S.theme)}</select></label>
        <label class="f">Chứng chỉ mục tiêu<select id="s-cert">${opts(Object.entries(CERTS).map(([k, c]) => [k, c.name]), S.prefs.cert)}</select></label></div>
      <div class="card stack"><h2>Góp số liệu ẩn danh</h2><p class="small muted">Khi bật, trang gửi mã câu và đúng/sai của mỗi lượt làm (để tổng hợp phần "Nhiều người sai") và lượt xem trang kèm loại thiết bị, khu vực ước tính, địa chỉ IP đã che bớt (để thống kê truy cập). Không gửi tên, email hay số điện thoại.</p>
        <label class="check"><input type="checkbox" id="s-share" ${S.prefs.share !== false ? 'checked' : ''}> Góp số liệu ẩn danh</label></div>
      <div class="card stack"><h2>Sao lưu</h2><p class="small muted">Sao chép đoạn mã dưới đây và lưu lại; khi cần khôi phục, dán vào ô Khôi phục.</p>
        <textarea id="s-dump" readonly>${esc(dump)}</textarea><div class="row"><button class="btn" id="s-copy">Sao chép</button><button class="btn" id="s-file">Tải file .json</button></div></div>
      <div class="card stack"><h2>Khôi phục</h2><textarea id="s-in" placeholder="Dán mã sao lưu vào đây"></textarea>
        <div class="row"><button class="btn primary" id="s-restore">Khôi phục</button><label class="btn">Chọn file<input type="file" id="s-upload" accept="application/json,.json" hidden></label></div></div>
      <div class="card stack"><h2>Ghi chú báo lỗi (${S.reports.length})</h2><p class="small muted">Sao chép rồi gửi cho BT-INVEST qua Zalo <a href="${BRAND.zalo}" target="_blank" rel="noopener">${BRAND.phoneShow}</a>.</p><textarea id="s-rep" readonly>${esc(reports)}</textarea>
        <div class="row"><button class="btn" id="s-rep-copy" ${S.reports.length ? '' : 'disabled'}>Sao chép ghi chú</button></div></div>
      <div class="card stack"><h2>Xóa dữ liệu</h2><p class="small muted">Xóa lịch sử, câu đã làm, đánh dấu và thẻ đã nhớ trên máy này.</p><div><button class="btn danger" id="s-reset">Xóa toàn bộ tiến độ</button></div></div>
      <div class="card stack"><h2>Về dữ liệu</h2><p class="small">${fmt(D.q.length)} câu hỏi · ${D.law?.dieu.length || 0} điều luật · ${D.cards.length} thẻ số liệu.</p>
        <p class="small muted">Câu hỏi được biên soạn mới và soát theo văn bản hiện hành đến tháng 11/2026; câu Luật có trích nguyên văn đã được máy đối chiếu với văn bản gốc. Đây không phải trang chính thức của UBCKNN và không bảo đảm kết quả thi.</p></div>
    </div>`));
  const copy = async (id) => { const el = $('#' + id); try { await navigator.clipboard.writeText(el.value); toast('Đã sao chép.'); } catch { el.select(); toast('Hãy nhấn Ctrl+C / giữ để sao chép.'); } };
  $('#s-theme').onchange = e => { S.theme = e.target.value; applyTheme(); save(); };
  $('#s-cert').onchange = e => { S.prefs.cert = e.target.value; save(); };
  $('#s-share').onchange = e => { S.prefs.share = e.target.checked; if (!e.target.checked) outbox.length = 0; save(); };
  $('#s-copy').onclick = () => copy('s-dump');
  $('#s-rep-copy').onclick = () => copy('s-rep');
  $('#s-file').onclick = () => { try { const a = document.createElement('a'); a.href = URL.createObjectURL(new Blob([dump], { type: 'application/json' })); a.download = 'do-cchn-sao-luu.json'; a.click(); setTimeout(() => URL.revokeObjectURL(a.href), 2000); } catch { toast('Trình duyệt chặn tải file. Hãy dùng nút Sao chép.'); } };
  const restore = async text => {
    let d; try { d = JSON.parse(text); } catch { return toast('Mã sao lưu không hợp lệ: không đọc được JSON.'); }
    if (!d || d.app !== 'docchn' || typeof d.q !== 'object' || !Array.isArray(d.hist)) return toast('Mã sao lưu không đúng định dạng của Đỗ CCHN.');
    if (!(await confirmBox('Khôi phục tiến độ?', 'Tiến độ hiện tại trên máy này sẽ được thay bằng bản sao lưu.', 'Khôi phục'))) return;
    Object.assign(S, { q: d.q, star: d.star || {}, hist: d.hist, cards: d.cards || {}, reports: d.reports || [], sess: null, last: null }); save(); toast('Đã khôi phục tiến độ.'); go('tong-quan');
  };
  $('#s-restore').onclick = () => restore($('#s-in').value);
  $('#s-upload').onchange = e => { const f = e.target.files[0]; if (!f) return; const r = new FileReader(); r.onload = () => restore(r.result); r.readAsText(f, 'utf-8'); };
  $('#s-reset').onclick = async () => { if (await confirmBox('Xóa toàn bộ tiến độ?', 'Thao tác này không hoàn tác được.', 'Xóa', 'danger')) { const keep = { theme: S.theme, prefs: S.prefs }; S = { ...blank(), ...keep }; save(); toast('Đã xóa tiến độ.'); go('tong-quan'); } };
};


// ---------- TÀI KHOẢN ----------
const certOpts = v => opts(Object.entries(CERTS).map(([k, c]) => [k, 'Chứng chỉ ' + c.name]), v);
VIEWS['tai-khoan'] = () => {
  if (AUTH) {
    const u = AUTH.user;
    main(page('Tài khoản', 'Chào ' + esc(u.name || 'bạn'), 'Tiến độ học được lưu vào tài khoản và tự đồng bộ giữa các thiết bị bạn đăng nhập.',
      `<div class="grid g2">
        <div class="card stack"><h2>Thông tin</h2>
          <label class="f">Tên gọi<input id="a-name" maxlength="60" value="${esc(u.name)}"></label>
          <div class="small">Số điện thoại: <b>${esc(u.phone)}</b></div><div class="small">Email: <b>${esc(u.email)}</b></div>
          <label class="f">Mục tiêu<select id="a-cert">${certOpts(u.cert)}</select></label>
          <div class="row"><button class="btn primary" id="a-save">Lưu thông tin</button></div></div>
        <div class="card stack"><h2>Đồng bộ</h2>
          <p class="small">${lastSync ? 'Đã đồng bộ lúc ' + dt(lastSync) + '.' : 'Tiến độ sẽ được đồng bộ sau mỗi lần bạn trả lời.'} Đã lưu ${fmt(Object.keys(S.q).length)} câu đã làm, ${S.hist.filter(h => h.kind === 'exam').length} bài thi thử.</p>
          <div class="row"><button class="btn" id="a-sync">Đồng bộ ngay</button><button class="btn" id="a-out">Đăng xuất</button></div>
          <p class="tiny muted">Đăng xuất vẫn giữ tiến độ trên máy này. Muốn xóa hẳn tài khoản và dữ liệu trên máy chủ, bấm nút dưới.</p>
          <div><button class="btn danger sm" id="a-del">Xóa tài khoản</button></div></div>
      </div>`));
    $('#a-save').onclick = async () => {
      try { const j = await api('cap-nhat', { name: $('#a-name').value, cert: $('#a-cert').value }); AUTH.user = j.user; setAuth(AUTH); S.prefs.cert = j.user.cert; save(); toast('Đã lưu thông tin.'); VIEWS['tai-khoan'](); renderAcct(); }
      catch (e) { toast(e.message); }
    };
    $('#a-sync').onclick = async () => { await syncNow(); toast(lastSync ? 'Đã đồng bộ.' : 'Chưa đồng bộ được, hãy kiểm tra mạng.'); VIEWS['tai-khoan'](); };
    $('#a-out').onclick = async () => { await syncNow(); try { await api('dang-xuat'); } catch { /* vẫn đăng xuất trên máy này */ } setAuth(null); renderAcct(); toast('Đã đăng xuất.'); go('tong-quan'); };
    $('#a-del').onclick = async () => {
      const ok = await modal(`<h2>Xóa tài khoản?</h2><p class="muted">Thông tin và tiến độ trên máy chủ sẽ bị xóa vĩnh viễn. Nhập mật khẩu để xác nhận.</p><input type="password" autocomplete="current-password" aria-label="Mật khẩu">`, [['Hủy', '', false], ['Xóa tài khoản', 'danger', true]]);
      if (!ok) return;
      try { await api('xoa', { password: modal.text }); setAuth(null); renderAcct(); toast('Đã xóa tài khoản. Tiến độ trên máy này vẫn còn.'); go('tong-quan'); } catch (e) { toast(e.message); }
    };
    return;
  }
  main(page('Tài khoản', 'Tạo tài khoản hoặc đăng nhập', 'Không bắt buộc: bạn vẫn học bình thường khi không có tài khoản. Có tài khoản thì tiến độ được lưu trên máy chủ để học tiếp trên điện thoại, máy tính và nhận gợi ý theo chứng chỉ bạn thi.',
    `<p class="small">Đã có tài khoản? <a href="#tai-khoan" id="to-login">Đăng nhập ở đây</a></p>
    <div class="grid g2">
      <form class="card stack" id="f-reg" novalidate><h2>Tạo tài khoản</h2>
        <label class="f">Tên gọi (không bắt buộc)<input name="name" maxlength="60" autocomplete="name"></label>
        <label class="f">Số điện thoại *<input name="phone" type="tel" inputmode="tel" autocomplete="tel" required placeholder="09xx xxx xxx"></label>
        <label class="f">Email *<input name="email" type="email" autocomplete="email" required></label>
        <label class="f">Mật khẩu * (từ 8 ký tự)<input name="password" type="password" autocomplete="new-password" minlength="8" required></label>
        <label class="f">Mục tiêu *<select name="cert">${certOpts(S.prefs.cert)}</select></label>
        <label class="check"><input type="checkbox" name="consent"> Tôi đồng ý để BT-INVEST lưu số điện thoại, email, mục tiêu, tiến độ học và lịch sử đăng nhập (thời gian, địa chỉ IP, thiết bị, khu vực) để đồng bộ, bảo mật tài khoản, gợi ý bài học và liên hệ tư vấn. Tôi có thể xóa tài khoản bất cứ lúc nào.</label>
        <p class="tiny muted">Tiến độ bạn đã học trên máy này sẽ được chuyển vào tài khoản. Hiện chưa có chức năng lấy lại mật khẩu, hãy ghi nhớ mật khẩu.</p>
        <div><button class="btn primary">Tạo tài khoản</button></div></form>
      <form class="card stack" id="f-login" novalidate><h2>Đăng nhập</h2>
        <label class="f">Số điện thoại hoặc email<input name="id" autocomplete="username" required></label>
        <label class="f">Mật khẩu<input name="password" type="password" autocomplete="current-password" required></label>
        <div><button class="btn primary">Đăng nhập</button></div>
        <p class="tiny muted">Tiến độ trên máy này sẽ được gộp với tiến độ đã lưu trong tài khoản.</p></form>
    </div>`));
  $('#to-login').onclick = e => { e.preventDefault(); $('#f-login').scrollIntoView({ behavior: reduceMotion() ? 'auto' : 'smooth' }); $('#f-login [name=id]').focus({ preventScroll: true }); };
  const done = (j, msg) => { setAuth({ token: j.token, user: j.user }); adopt(j.data); lastSync = now(); renderAcct(); toast(msg); go('tong-quan'); };
  $('#f-reg').onsubmit = async e => {
    e.preventDefault(); const f = e.target, v = Object.fromEntries(new FormData(f));
    if (!f.consent.checked) return toast('Hãy đánh dấu ô đồng ý để tạo tài khoản.');
    f.querySelector('button').disabled = true;
    try { done(await api('dang-ky', { ...v, consent: true, data: syncData() }), 'Đã tạo tài khoản. Tiến độ sẽ tự đồng bộ.'); }
    catch (err) { toast(err.message); f.querySelector('button').disabled = false; }
  };
  $('#f-login').onsubmit = async e => {
    e.preventDefault(); const f = e.target, v = Object.fromEntries(new FormData(f));
    f.querySelector('button').disabled = true;
    try { done(await api('dang-nhap', { ...v, data: syncData() }), 'Đã đăng nhập.'); }
    catch (err) { toast(err.message); f.querySelector('button').disabled = false; }
  };
};

// ---------- QUẢN TRỊ (ẩn, vào bằng #quan-tri): danh sách người đăng ký ----------
VIEWS['quan-tri'] = async () => {
  let key = ''; try { key = sessionStorage.getItem('btinvest_admin') || ''; } catch { /* bỏ qua */ }
  const form = msg => { main(page('Quản trị', 'Danh sách tài khoản', msg || 'Nhập mã quản trị (biến ADMIN_KEY đặt trên Vercel).',
    `<form class="card stack" id="q-f"><label class="f">Mã quản trị<input type="password" name="k" autocomplete="off" required></label><div><button class="btn primary">Xem danh sách</button></div></form>`));
    $('#q-f').onsubmit = e => { e.preventDefault(); try { sessionStorage.setItem('btinvest_admin', e.target.k.value); } catch { /* bỏ qua */ } VIEWS['quan-tri'](); }; };
  if (!key) return form();
  let users, logins, st;
  try { ({ users, logins, stats: st } = await api('quan-tri', {}, { 'x-admin-key': key })); }
  catch (e) { try { sessionStorage.removeItem('btinvest_admin'); } catch { /* bỏ qua */ } return form(e.message); }
  if (current !== 'quan-tri') return;
  const cert = c => CERTS[c]?.name || c;
  const cell = v => { const t = String(v ?? ''); return '"' + (/^[=+\-@]/.test(t) ? "'" + t : t).replace(/"/g, '""') + '"'; };   // chặn công thức khi mở bằng Excel
  const csv = '﻿' + [['Tên', 'SĐT', 'Email', 'Mục tiêu', 'Ngày tạo', 'Hoạt động gần nhất', 'Số câu đã làm', 'Đúng lần gần nhất', 'Bài thi thử', 'IP đăng nhập gần nhất', 'Khu vực'],
    ...users.map(u => [u.name, u.phone, u.email, cert(u.cert), dt(u.created), dt(u.last), u.done, u.ok, u.exams, u.login?.ip, u.login?.where])].map(r => r.map(cell).join(',')).join('\r\n');
  const today = st.days[29], pv7 = st.days.slice(-7).reduce((a, d) => a + d.pv, 0), pv30 = st.days.reduce((a, d) => a + d.pv, 0);
  const new7 = users.filter(u => u.created > now() - 7 * DAY).length;
  const tile = (k, v, d) => `<div class="card stat"><div class="k">${k}</div><div class="v">${fmt(v)}</div><div class="d">${d}</div></div>`;
  const ddmm = d => d.slice(8) + '/' + d.slice(5, 7);
  // biểu đồ cột một chuỗi: một màu, không chú giải; rê chuột xem số, có bảng số bên dưới
  const vbars = (rows, label, tip) => { const mx = Math.max(1, ...rows.map(r => r.n)); return `<div class="vbars" role="img" aria-label="${esc(label)}">${rows.map(r => `<i style="height:${Math.max(2, r.n / mx * 100)}%" title="${esc(tip(r))}"></i>`).join('')}</div>`; };
  const hbars = obj => { const e = Object.entries(obj || {}).sort((a, b) => b[1] - a[1]).slice(0, 8), mx = Math.max(1, ...e.map(x => x[1]));
    return e.map(([k, n]) => `<div class="stack" style="gap:3px"><div class="row between small"><span>${esc(k)}</span><span class="num muted">${fmt(n)}</span></div><div class="bar"><i style="width:${n / mx * 100}%;background:var(--accent)"></i></div></div>`).join('') || '<p class="muted small">Chưa có dữ liệu.</p>'; };
  const pages = Object.fromEntries(Object.entries(st.pages || {}).map(([k, n]) => [TITLES[k] || k, n]));
  main(page('Quản trị', 'Thống kê & tài khoản', 'Số liệu truy cập tính theo giờ Việt Nam. Chỉ dùng để quản lý trang và chăm sóc người học đã đồng ý; không chia sẻ ra ngoài.',
    `<div class="grid g4">
      ${tile('Hôm nay', today.uv, `người truy cập · ${fmt(today.pv)} lượt xem`)}
      ${tile('7 ngày', st.uv7, `người truy cập · ${fmt(pv7)} lượt xem`)}
      ${tile('30 ngày', st.uv30, `người truy cập · ${fmt(pv30)} lượt xem`)}
      ${tile('Tài khoản', users.length, `mới trong 7 ngày: ${new7} · tổng người truy cập: ${fmt(st.uvAll)}`)}
    </div>
    <div class="card stack"><h2>Người truy cập mỗi ngày (30 ngày)</h2>
      ${vbars(st.days.map(d => ({ n: d.uv, d })), 'Người truy cập mỗi ngày trong 30 ngày', r => `${ddmm(r.d.d)}: ${r.d.uv} người, ${r.d.pv} lượt xem`)}
      <div class="row between tiny muted"><span>${ddmm(st.days[0].d)}</span><span>${ddmm(st.days[15].d)}</span><span>${ddmm(today.d)}</span></div>
      <details><summary class="small">Xem bảng số</summary><div class="tablewrap"><table><thead><tr><th>Ngày</th><th>Người truy cập</th><th>Lượt xem</th></tr></thead><tbody>
        ${[...st.days].reverse().map(d => `<tr><td class="num">${ddmm(d.d)}</td><td class="num">${d.uv}</td><td class="num">${d.pv}</td></tr>`).join('')}</tbody></table></div></details></div>
    <div class="card stack"><h2>Khung giờ truy cập (30 ngày)</h2>
      ${vbars(st.hours.map((n, h) => ({ n, h })), 'Lượt xem theo giờ trong ngày', r => `${r.h}h–${r.h + 1}h: ${r.n} lượt xem`)}
      <div class="row between tiny muted"><span>0h</span><span>6h</span><span>12h</span><span>18h</span><span>23h</span></div></div>
    <div class="grid g3">
      <div class="card stack"><h2>Trang xem nhiều</h2>${hbars(pages)}</div>
      <div class="card stack"><h2>Thiết bị</h2>${hbars(st.devs)}</div>
      <div class="card stack"><h2>Khu vực</h2>${hbars(st.geo)}<p class="tiny muted">Ước tính theo địa chỉ IP, có thể lệch tỉnh/thành.</p></div>
    </div>
    <div class="card stack"><h2>Đăng nhập gần đây</h2><div class="tablewrap"><table><thead><tr><th>Thời gian</th><th>Tài khoản</th><th>Địa chỉ IP</th><th>Khu vực</th><th>Thiết bị</th></tr></thead><tbody>
      ${logins.map(e => `<tr><td class="num small">${dt(e.at)}</td><td>${esc(e.who)}</td><td class="num">${esc(e.ip)}</td><td>${esc(e.where)}</td><td>${esc(e.dev)}</td></tr>`).join('') || '<tr><td colspan="5" class="muted">Chưa có lượt đăng nhập.</td></tr>'}</tbody></table></div></div>
    <div class="card stack"><h2>Lượt truy cập gần đây</h2><p class="tiny muted">Khách không đăng nhập: IP chỉ lưu dạng che bớt để bảo vệ dữ liệu cá nhân.</p><div class="tablewrap"><table><thead><tr><th>Thời gian</th><th>Trang</th><th>Khu vực</th><th>Thiết bị</th><th>IP</th></tr></thead><tbody>
      ${st.log.slice(0, 50).map(e => `<tr><td class="num small">${dt(e.at)}</td><td>${esc(TITLES[e.p] || e.p)}</td><td>${esc(e.where)}</td><td>${esc(e.dev)}</td><td class="num">${esc(e.ip)}</td></tr>`).join('') || '<tr><td colspan="5" class="muted">Chưa có lượt truy cập.</td></tr>'}</tbody></table></div></div>
    <div class="card stack"><div class="row between"><h2>Tài khoản (${fmt(users.length)})</h2><span class="row"><button class="btn primary sm" id="q-csv">Tải file CSV</button><button class="btn sm" id="q-out">Thoát quản trị</button></span></div>
      <div class="tablewrap"><table><thead><tr><th>Tên</th><th>SĐT</th><th>Email</th><th>Mục tiêu</th><th>Ngày tạo</th><th>Gần nhất</th><th>Đã làm</th><th>Thi thử</th><th>Đăng nhập gần nhất</th></tr></thead>
      <tbody>${users.map(u => `<tr><td>${esc(u.name)}</td><td class="num">${esc(u.phone)}</td><td>${esc(u.email)}</td><td>${esc(cert(u.cert))}</td><td class="num small">${dt(u.created)}</td><td class="num small">${dt(u.last)}</td><td class="num">${u.done}</td><td class="num">${u.exams}</td><td class="small">${u.login ? esc(u.login.ip) + '<br><span class="muted">' + esc(u.login.where) + ' · ' + esc(u.login.dev) + '</span>' : ''}</td></tr>`).join('') || '<tr><td colspan="9" class="muted">Chưa có tài khoản nào.</td></tr>'}</tbody></table></div></div>`));
  $('#q-csv').onclick = () => { const a = document.createElement('a'); a.href = URL.createObjectURL(new Blob([csv], { type: 'text/csv' })); a.download = 'tai-khoan-bt-invest.csv'; a.click(); setTimeout(() => URL.revokeObjectURL(a.href), 2000); };
  $('#q-out').onclick = () => { try { sessionStorage.removeItem('btinvest_admin'); } catch { /* bỏ qua */ } go('tong-quan'); };
};

// ---------- GIỚI THIỆU & LIÊN HỆ ----------
VIEWS['lien-he'] = () => {
  main(page('Giới thiệu & liên hệ', 'BT-INVEST', 'Đồng hành cùng người học và làm nghề chứng khoán: luyện thi chứng chỉ hành nghề bám sát luật hiện hành, kiến thức đầu tư dễ hiểu, áp dụng được.',
    `<div class="card stack"><h2>Kênh của BT-INVEST</h2><p class="small muted">Theo dõi chuỗi video kiến thức tài chính nói đơn giản và các mẹo ôn thi.</p>
      <div class="channels">${SOCIAL.map(([k, n, u, h]) => `<a href="${u}" target="_blank" rel="noopener"><svg viewBox="0 0 24 24" aria-hidden="true">${SOCIAL_IC[k]}</svg><span><b>${n}</b><small>${esc(h)}</small></span></a>`).join('')}</div></div>
    <div class="grid g2">
      <div class="card stack"><h2>Liên hệ BT-INVEST</h2><p class="small muted">Hỏi đáp khi ôn thi, góp ý hoặc báo lỗi câu hỏi.</p>
        <div class="contact-num" id="ct-num">${BRAND.phoneShow}</div>
        <div class="row"><a class="btn primary" href="tel:${BRAND.phone}">Gọi điện</a><a class="btn" href="${BRAND.zalo}" target="_blank" rel="noopener">Nhắn Zalo</a><button class="btn" id="ct-copy">Sao chép số</button></div>
        <p class="tiny muted">Trên một số thiết bị, nút Gọi và Zalo có thể không mở được ứng dụng; hãy sao chép số để gọi hoặc tìm trên Zalo.</p></div>
      <div class="card stack"><h2>Ứng dụng này có gì</h2>
        <p class="small">${fmt(D.q.length)} câu hỏi biên soạn mới; câu Luật kèm trích nguyên văn điều khoản hiện hành (cập nhật đến 11/2026) và đã đối chiếu tự động với văn bản gốc.</p>
        <p class="small">Thi thử đúng cấu trúc từng chứng chỉ: hai phần tính giờ riêng, đạt khi đúng từ 60% mỗi phần.</p>
        <p class="small">Ôn lặp lại câu sai theo lịch, thư viện Luật Chứng khoán hợp nhất, máy tính tài chính và thẻ ghi nhớ số liệu.</p></div>
      <div class="card stack"><h2>Dữ liệu của bạn</h2><p class="small">Ứng dụng không yêu cầu tài khoản và không gửi dữ liệu đi đâu. Tiến độ học lưu ngay trong trình duyệt của bạn; dùng mục Cài đặt để sao lưu khi đổi máy.</p></div>
      <div class="card stack"><h2>Lưu ý</h2><p class="small">BT-INVEST không phải cơ quan quản lý hay đơn vị tổ chức thi. Đây không phải trang chính thức của UBCKNN và không bảo đảm kết quả thi. Quy định chính thức xem tại trang của UBCKNN và SRTC.</p></div>
    </div>`));
  $('#ct-copy').onclick = async () => { try { await navigator.clipboard.writeText(BRAND.phone); toast('Đã sao chép số ' + BRAND.phoneShow); } catch { const r = document.createRange(); r.selectNodeContents($('#ct-num')); getSelection().removeAllRanges(); getSelection().addRange(r); toast('Đã chọn số, hãy nhấn sao chép.'); } };
};

// ---------- khởi động ----------
function applyTheme() { if (S.theme) document.documentElement.dataset.theme = S.theme; else delete document.documentElement.dataset.theme; }
document.addEventListener('keydown', e => {
  if (current !== 'lam-bai' || !S.sess || S.sess.waiting || $('#modal-root').children.length) return;
  if (['INPUT', 'TEXTAREA', 'SELECT'].includes(document.activeElement?.tagName)) return;
  const pt = part(), id = pt.ids[S.sess.i];
  if (/^[1-6]$/.test(e.key)) { const oi = pt.perm[id]?.[+e.key - 1]; if (oi !== undefined) choose(oi); }
  else if (e.key === 'ArrowRight') move(1);
  else if (e.key === 'ArrowLeft') move(-1);
  else if (e.key.toLowerCase() === 'f') { pt.flag[id] = !pt.flag[id]; save(); VIEWS['lam-bai'](); }
});
document.addEventListener('keydown', e => { if (current === 'the-nho' && e.key === ' ' && document.activeElement?.tagName !== 'SELECT') { e.preventDefault(); $('#c-card')?.click(); } });
$('#menu-btn').onclick = () => openNav(!$('#nav').classList.contains('open'));
window.addEventListener('hashchange', route);

(async function init() {
  applyTheme();
  const [q, law, cards, changes, docs] = await Promise.all([loadJSON('questions', []), loadJSON('luat_ck', null), loadJSON('so_lieu', []), loadJSON('thay_doi', []), loadJSON('van_ban', [])]);
  Object.assign(D, { q, law, cards, changes, docs }); D.byId = new Map(q.map(x => [x.id, x]));
  // tiến độ thẻ trước 11/2026 lưu theo số thứ tự (thẻ Luật đứng đầu, giữ nguyên thứ tự) → đổi sang mã thẻ
  if (Object.keys(S.cards).some(k => /^\d+$/.test(k))) { for (const k of Object.keys(S.cards)) if (/^\d+$/.test(k)) { if (cards[+k]) S.cards[cards[+k].id] = S.cards[k]; delete S.cards[k]; } save(); }
  if (!q.length) { main(`<div class="page"><div class="card empty">Không tải được ngân hàng câu hỏi. Nếu bạn mở file trực tiếp trên máy, hãy dùng bản <b>dist/index.html</b> hoặc chạy qua máy chủ web.</div></div>`); renderNav(''); return; }
  if (S.sess && S.sess.parts?.some(p => p.ids.some(id => !D.byId.has(id)))) S.sess.parts.forEach(p => (p.ids = p.ids.filter(id => D.byId.has(id))));
  route();
  if (AUTH) syncNow().then(() => { if (current === 'tong-quan') route(); });
  if ('serviceWorker' in navigator && location.protocol === 'https:' && document.querySelector('link[rel="manifest"]')) navigator.serviceWorker.register('sw.js').catch(() => {});
})();
})();
