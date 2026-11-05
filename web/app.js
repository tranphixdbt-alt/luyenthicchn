/* Đỗ CCHN — ứng dụng luyện thi chứng chỉ hành nghề chứng khoán. JavaScript thuần, không cần build. */
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
const PASS = 0.6;
const DAY = 864e5, SRS_DAYS = [0, 1, 3, 7, 16, 35];
const KEY = 'docchn_v1';

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
}

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
};
const icon = k => `<svg viewBox="0 0 24 24" aria-hidden="true">${IC[k]}</svg>`;
const NAV = [
  ['Học', [['tong-quan', 'Tổng quan', 'home'], ['on-luyen', 'Ôn luyện', 'practice'], ['on-tap', 'Ôn lặp lại', 'review'], ['thi-thu', 'Thi thử', 'exam']]],
  ['Tra cứu', [['ngan-hang', 'Ngân hàng câu hỏi', 'bank'], ['the-nho', 'Thẻ ghi nhớ số liệu', 'cards'], ['cong-thuc', 'Công thức & máy tính', 'calc'],
    ['thu-vien', 'Thư viện luật', 'law'], ['thay-doi', 'Luật mới 2025–2026', 'change'], ['quy-che', 'Quy chế thi 2026', 'rules']]],
  ['Cá nhân', [['lich-su', 'Lịch sử & tiến độ', 'history'], ['cai-dat', 'Cài đặt & sao lưu', 'gear']]],
];
const TITLES = Object.fromEntries(NAV.flatMap(g => g[1].map(x => [x[0], x[1]])));
Object.assign(TITLES, { 'lam-bai': 'Đang làm bài', 'ket-qua': 'Kết quả' });

function renderNav(cur) {
  const due = dueIds().length;
  $('#nav').innerHTML = `<div class="brand"><div class="brand-mark">Đỗ</div><div><b>Đỗ CCHN</b><small>Thi sát hạch 2026</small></div></div>` +
    NAV.map(([g, items]) => `<div class="nav-group">${g}</div>` + items.map(([h, t, i]) =>
      `<a href="#${h}" class="${cur === h ? 'on' : ''}">${icon(i)}<span>${t}</span>${h === 'on-tap' && due ? `<span class="badge-due">${due}</span>` : ''}</a>`).join('')).join('') +
    `<div class="nav-foot">${fmt(D.q.length)} câu hỏi · cập nhật luật đến 11/2026<br>Không phải trang chính thức của UBCKNN.</div>`;
  const tabs = [['tong-quan', 'Tổng quan', 'home'], ['on-luyen', 'Ôn luyện', 'practice'], ['thi-thu', 'Thi thử', 'exam'], ['thu-vien', 'Thư viện', 'law']];
  $('#tabbar').innerHTML = tabs.map(([h, t, i]) => `<a href="#${h}" class="${cur === h ? 'on' : ''}">${icon(i)}${t}</a>`).join('') +
    `<a href="#menu" id="tab-more">${icon('menu')}Thêm</a>`;
  $('#tab-more').onclick = e => { e.preventDefault(); openNav(true); };
  $('#topbar-title').textContent = TITLES[cur] || '';
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
  if (h.startsWith('dieu-')) { current = 'thu-vien'; renderNav(current); VIEWS['thu-vien'](h.slice(5)); return; }
  if (!VIEWS[h]) h = 'tong-quan';
  current = h; renderNav(h); openNav(false);
  VIEWS[h]();
  $('#main').scrollTo?.(0, 0); window.scrollTo(0, 0);
}
const go = h => { if (location.hash === '#' + h) route(); else location.hash = h; };
const main = html => { $('#main').innerHTML = html; };

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
  main(page('Tổng quan', 'Chào bạn, hôm nay ôn gì?', `Mục tiêu: đúng từ 60% số câu ở <b>mỗi</b> phần thi. Chứng chỉ đang chọn: <b>${CERTS[cert].name}</b>.`,
    `${resume}
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
      <div class="row between"><h2>Mức nắm vững theo môn</h2><span class="tiny muted">Bấm vào ô để luyện môn đó</span></div>
      <div class="board">${tiles}</div>
      <div class="legend"><span><i style="background:var(--floor)"></i>Sàn &lt;40%</span><span><i style="background:var(--down)"></i>Giảm 40–59%</span>
        <span><i style="background:var(--ref)"></i>Tham chiếu 60–69%</span><span><i style="background:var(--up)"></i>Tăng 70–84%</span><span><i style="background:var(--ceil)"></i>Trần ≥85%</span></div>
    </div>
    <div class="grid g3">
      <a class="card stack" href="#on-luyen" style="text-decoration:none;color:inherit"><h3>Ôn luyện theo chủ đề</h3><p class="small muted">Chọn môn, chủ đề, mức độ; xem đáp án, giải thích và điều luật ngay sau mỗi câu.</p></a>
      <a class="card stack" href="#thi-thu" style="text-decoration:none;color:inherit"><h3>Thi thử đúng cấu trúc</h3><p class="small muted">Hai phần tính giờ riêng, chỉ lấy câu thuộc chương trình của chứng chỉ bạn thi.</p></a>
      <a class="card stack" href="#thay-doi" style="text-decoration:none;color:inherit"><h3>Luật mới 2025–2026</h3><p class="small muted">Những quy định đã đổi theo Luật 56/2024, NĐ 245/2025, TT 135/2025… hay bị hỏi.</p></a>
    </div>`));
  $$('[data-subj]').forEach(b => (b.onclick = () => { practiceFilter = { ...practiceFilter, subject: b.dataset.subj, part: b.dataset.subj === 'LU' ? 'LUAT' : 'CM', topic: '' }; go('on-luyen'); }));
};

// ---------- ÔN LUYỆN ----------
let practiceFilter = { cert: '', part: '', subject: '', topic: '', level: '', pool: 'all', n: 20, mix: true };
function pool(f) {
  const allow = f.cert ? new Set(['LU', ...Object.keys(CERTS[f.cert].blueprint)]) : null;
  return D.q.filter(q => (!allow || allow.has(q.subject)) && (!f.part || q.part === f.part) && (!f.subject || q.subject === f.subject) &&
    (!f.topic || q.topic === f.topic) && (!f.level || String(q.level) === String(f.level)) &&
    (f.pool === 'all' || (f.pool === 'new' && !S.q[q.id]) || (f.pool === 'wrong' && S.q[q.id] && !S.q[q.id].lastOk) || (f.pool === 'star' && S.star[q.id])));
}
VIEWS['on-luyen'] = () => {
  const f = practiceFilter;
  const subjects = Object.entries(SUBJ).filter(([c]) => (!f.part || (f.part === 'LUAT') === (c === 'LU')) && (!f.cert || c === 'LU' || CERTS[f.cert].blueprint[c]));
  if (f.subject && !subjects.some(([c]) => c === f.subject)) f.subject = '';
  const topics = [...new Set(D.q.filter(q => (!f.subject || q.subject === f.subject) && (!f.part || q.part === f.part)).map(q => q.topic))].sort((a, b) => a.localeCompare(b, 'vi'));
  if (f.topic && !topics.includes(f.topic)) f.topic = '';
  const n = pool(f).length;
  main(page('Ôn luyện', 'Ôn theo chủ đề', 'Trả lời xong là thấy ngay đáp án, giải thích và căn cứ pháp lý. Câu sai tự vào lịch ôn lặp lại.',
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
      <div class="row between"><span class="muted small" id="f-count">Có <b>${n}</b> câu phù hợp.</span>
        <div class="row"><a class="btn" href="#ngan-hang">Xem ngân hàng</a><button class="btn primary" id="f-start" ${n ? '' : 'disabled'}>Bắt đầu ${Math.min(n, f.n)} câu</button></div></div>
    </div>`));
  const bind = (id, key, num) => ($('#' + id).onchange = e => { f[key] = num ? +e.target.value : e.target.value; if (key === 'part') f.subject = ''; VIEWS['on-luyen'](); });
  bind('f-cert', 'cert'); bind('f-part', 'part'); bind('f-subject', 'subject'); bind('f-topic', 'topic'); bind('f-level', 'level'); bind('f-pool', 'pool'); bind('f-n', 'n', true);
  $('#f-mix').onchange = e => (f.mix = e.target.checked);
  $('#f-start').onclick = () => startPractice(shuffle(pool(f).map(q => q.id)).slice(0, f.n), 'Ôn luyện', f.mix);
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

// ---------- THI THỬ ----------
VIEWS['thi-thu'] = () => {
  const p = S.prefs, c = CERTS[p.cert];
  const bp = Object.entries(c.blueprint).map(([k, w]) => `<span class="chip">${SUBJ[k].short} ${Math.round(w * 100)}%</span>`).join(' ');
  main(page('Thi thử', 'Thi sát hạch mô phỏng', 'Phần Pháp luật trước, phần Chuyên môn sau. Mỗi phần tính giờ riêng và phải đúng từ 60% số câu. Không xem đáp án cho tới khi nộp.',
    `<div class="card stack">
      <div class="grid g3">
        <label class="f">Chứng chỉ<select id="e-cert">${opts(Object.entries(CERTS).map(([k, x]) => [k, `${x.name} · ${x.minutes}′ + ${x.minutes}′`]), p.cert)}</select></label>
        <label class="f">Phần thi<select id="e-mode">${opts([['both', 'Thi đủ 2 phần'], ['LUAT', 'Thi lại riêng phần Pháp luật'], ['CM', 'Thi lại riêng phần Chuyên môn']], p.mode || 'both')}</select></label>
        <label class="f">Số câu mỗi phần<select id="e-n">${opts([[25, '25 câu'], [35, '35 câu'], [50, '50 câu'], [60, '60 câu']], p.n)}</select></label>
      </div>
      <div class="grid g2">
        <div class="card flat stack"><div class="row between"><h3>Phần 1 · Pháp luật CK & TTCK</h3><span class="chip acc num">${c.minutes} phút</span></div>
          <p class="small muted">Lấy đều các chủ đề từ ${D.q.filter(q => q.subject === 'LU').length} câu Luật đã soát theo văn bản hiện hành.</p></div>
        <div class="card flat stack"><div class="row between"><h3>Phần 2 · Chuyên môn</h3><span class="chip acc num">${c.minutes} phút</span></div>
          <p class="small muted">Chỉ gồm các môn trong điều kiện cấp CCHN ${c.name}:</p><div class="row">${bp}</div></div>
      </div>
      <div class="note">Thời gian và mốc 60% mỗi phần theo thông báo của Hội đồng thi năm 2026. <b>Số câu mỗi phần chưa được công bố chính thức</b>, nên bạn tự chọn; tỷ trọng các môn chuyên môn là cấu hình mô phỏng.</div>
      <div class="row"><button class="btn primary" id="e-start">Vào phòng thi</button><span class="small muted">Phím tắt: <span class="kbd">1</span>–<span class="kbd">4</span> chọn đáp án, <span class="kbd">←</span> <span class="kbd">→</span> đổi câu, <span class="kbd">F</span> đánh dấu.</span></div>
    </div>`));
  $('#e-cert').onchange = e => { p.cert = e.target.value; save(); VIEWS['thi-thu'](); };
  $('#e-mode').onchange = e => { p.mode = e.target.value; save(); };
  $('#e-n').onchange = e => { p.n = +e.target.value; save(); };
  $('#e-start').onclick = startExam;
};
function pickLaw(n) {     // rải đều theo chủ đề
  const byTopic = {}; for (const q of shuffle(D.q.filter(q => q.subject === 'LU'))) (byTopic[q.topic] ||= []).push(q.id);
  const lists = shuffle(Object.values(byTopic)), out = [];
  while (out.length < n && lists.some(l => l.length)) for (const l of lists) { if (l.length && out.length < n) out.push(l.pop()); }
  return shuffle(out);
}
function pickSpec(cert, n) {
  const bp = Object.entries(CERTS[cert].blueprint), want = bp.map(([k, w]) => [k, Math.floor(w * n)]);
  let left = n - want.reduce((s, x) => s + x[1], 0);
  for (let i = 0; left > 0; i = (i + 1) % want.length, left--) want[i][1]++;
  const out = [], used = new Set();
  for (const [k, m] of want) for (const q of shuffle(D.q.filter(q => q.subject === k)).slice(0, m)) { out.push(q.id); used.add(q.id); }
  if (out.length < n) {      // môn nào thiếu câu thì bù bằng môn khác trong cùng chương trình
    const rest = shuffle(D.q.filter(q => CERTS[cert].blueprint[q.subject] && !used.has(q.id)));
    out.push(...rest.slice(0, n - out.length).map(q => q.id));
  }
  return shuffle(out);
}
async function startExam() {
  const p = S.prefs, c = CERTS[p.cert], mode = p.mode || 'both';
  if (S.sess && !(await confirmBox('Bỏ bài đang làm?', `Bài "${esc(S.sess.title)}" chưa hoàn tất sẽ bị bỏ.`, 'Bỏ và vào thi'))) return;
  const parts = [];
  if (mode !== 'CM') parts.push(mkPart('LUAT', 'Phần 1 · Pháp luật', pickLaw(p.n), true, c.minutes));
  if (mode !== 'LUAT') parts.push(mkPart('CM', mode === 'both' ? 'Phần 2 · Chuyên môn' : 'Phần Chuyên môn', pickSpec(p.cert, p.n), true, c.minutes));
  if (parts.some(x => x.ids.length < p.n)) toast('Ngân hàng chưa đủ câu cho cấu hình này; đề sẽ ngắn hơn.');
  parts[0].startAt = now(); parts[0].endAt = now() + c.minutes * 60e3;
  S.sess = { kind: 'exam', title: 'Thi thử ' + c.name, cert: p.cert, mode, p: 0, i: 0, createdAt: now(), parts, waiting: false };
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
    if (shown) cls = oi === q.a ? 'ok' : (oi === chosen ? 'bad' : '');
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
function choose(oi) {
  const s = S.sess, pt = part(), id = pt.ids[s.i];
  if (s.kind !== 'exam' && pt.checked[id]) return;
  pt.ans[id] = oi;
  if (s.kind !== 'exam') { pt.checked[id] = true; rec(id, isRight(D.byId.get(id), oi)); }
  save(); VIEWS['lam-bai']();
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
  if (s.kind === 'exam' && s.p < s.parts.length - 1) { s.p++; s.i = 0; s.waiting = true; save(); if (auto) toast('Hết giờ ' + pt.label + '. Bài đã được nộp.'); return go('lam-bai'); }
  // chấm
  const parts = s.parts.map(x => {
    const items = x.ids.map(id => ({ id, c: x.ans[id] ?? null, perm: x.perm[id] }));
    const ok = items.filter(it => it.c !== null && isRight(D.byId.get(it.id), it.c)).length;
    const n = s.kind === 'exam' ? items.length : items.filter(it => it.c !== null).length;
    return { key: x.key, label: x.label, n, ok, pass: n ? ok / n >= PASS : false, items };
  });
  if (s.kind === 'exam') for (const x of parts) for (const it of x.items) rec(it.id, it.c !== null && isRight(D.byId.get(it.id), it.c));
  const n = parts.reduce((a, x) => a + x.n, 0), ok = parts.reduce((a, x) => a + x.ok, 0);
  const res = { at: now(), kind: s.kind, title: s.title, cert: s.cert || null, n, ok, pass: s.kind === 'exam' ? parts.every(x => x.pass) : (n ? ok / n >= PASS : false),
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
  main(page(exam ? 'Kết quả thi thử' : 'Kết quả ôn luyện', exam ? (r.pass ? 'Đạt cả hai phần' : 'Chưa đạt') : `Đúng ${r.ok}/${r.n} câu`,
    exam ? 'Đạt khi đúng từ 60% số câu ở mỗi phần; không cộng bù điểm giữa hai phần.' : '',
    `<div class="card row" style="gap:22px">
      <div class="ring" style="--p:${p};--c:var(--${r.pass ? 'up' : 'down'})"><div><span><b>${p}%</b><span class="tiny muted">đúng</span></span></div></div>
      <div class="stack" style="flex:1">${r.parts.map(x => `<div class="stack" style="gap:6px"><div class="row between"><b>${esc(x.label || 'Ôn luyện')}</b>
        <span class="row"><span class="num">${x.ok}/${x.n}</span>${exam ? `<span class="chip ${x.pass ? 'up' : 'down'}">${x.pass ? 'Đạt' : 'Chưa đạt'}</span>` : ''}</span></div>
        <div class="bar"><i style="width:${pct(x.ok, x.n)}%;background:var(--${x.ok / Math.max(x.n, 1) >= PASS ? 'up' : 'down'})"></i><span class="mark" style="left:60%"></span></div></div>`).join('')}
      </div></div>
    <div class="grid g2">
      <div class="card stack"><h2>Theo chủ đề (yếu nhất trước)</h2>${tp.slice(0, 12).map(([t, x]) => `<div class="stack" style="gap:4px"><div class="row between small"><span>${esc(t)}</span><span class="num">${x.ok}/${x.n}</span></div>
        <div class="bar"><i style="width:${pct(x.ok, x.n)}%;background:var(--${x.ok / x.n >= PASS ? 'up' : 'down'})"></i><span class="mark" style="left:60%"></span></div></div>`).join('') || '<p class="muted">Chưa có dữ liệu.</p>'}</div>
      <div class="card stack"><h2>Việc nên làm tiếp</h2>
        <p class="small muted">${wrongIds.length ? `Có ${wrongIds.length} câu sai hoặc bỏ trống. Ôn lại ngay giúp nhớ lâu hơn; các câu này cũng đã vào lịch ôn lặp lại.` : 'Không có câu sai. Hãy thử một đề mới hoặc tăng số câu.'}</p>
        <div class="row"><button class="btn primary" id="r-wrong" ${wrongIds.length ? '' : 'disabled'}>Ôn lại ${wrongIds.length} câu sai</button>
          ${exam ? '<a class="btn" href="#thi-thu">Thi đề khác</a>' : '<a class="btn" href="#on-luyen">Luyện tiếp</a>'}</div></div>
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
  $('#b-practice').onclick = () => startPractice(shuffle(list.map(q => q.id)).slice(0, 50), 'Luyện từ ngân hàng', true);
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
let cardF = { topic: '', onlyNew: false, i: 0, flip: false, order: null };
VIEWS['the-nho'] = () => {
  const f = cardF, cards = D.cards.map((c, i) => ({ ...c, i }));
  const topics = [...new Set(cards.map(c => c.topic))].sort((a, b) => a.localeCompare(b, 'vi'));
  let list = cards.filter(c => (!f.topic || c.topic === f.topic) && (!f.onlyNew || !S.cards[c.i]?.ok));
  if (!f.order || f.order.length !== list.length) f.order = shuffle(list.map(c => c.i));
  list = f.order.map(i => cards[i]).filter(Boolean);
  const known = cards.filter(c => S.cards[c.i]?.ok).length;
  f.i = Math.min(f.i, Math.max(list.length - 1, 0));
  const c = list[f.i];
  main(page('Thẻ ghi nhớ', 'Những con số hay bị hỏi', `Mức vốn, tỷ lệ, thời hạn… lấy từ văn bản hiện hành. Đã nhớ ${known}/${cards.length} thẻ.`,
    `<div class="card stack"><div class="grid g3">
        <label class="f">Chủ đề<select id="c-topic">${opts([['', 'Tất cả chủ đề'], ...topics.map(t => [t, t])], f.topic)}</select></label>
        <label class="check" style="align-self:end"><input type="checkbox" id="c-new" ${f.onlyNew ? 'checked' : ''}> Chỉ thẻ chưa nhớ</label>
      </div></div>
    ${c ? `<button class="card flash" id="c-card" aria-live="polite"><span class="tiny muted">${esc(c.topic)} · thẻ ${f.i + 1}/${list.length}</span>
        <span class="front">${esc(c.front)}</span>${f.flip ? `<span class="back">${esc(c.back)}</span><span class="tiny muted">${esc(c.basis)}</span>` : '<span class="small muted">Bấm để lật thẻ (phím cách)</span>'}</button>
      <div class="row" style="justify-content:center"><button class="btn" id="c-prev" ${f.i ? '' : 'disabled'}>← Trước</button>
        <button class="btn danger" id="c-no">Chưa nhớ</button><button class="btn primary" id="c-yes">Đã nhớ</button><button class="btn" id="c-next">Sau →</button></div>`
      : '<div class="card empty">Không còn thẻ nào trong bộ lọc này.</div>'}`));
  $('#c-topic').onchange = e => { f.topic = e.target.value; f.i = 0; f.order = null; f.flip = false; VIEWS['the-nho'](); };
  $('#c-new').onchange = e => { f.onlyNew = e.target.checked; f.i = 0; f.order = null; f.flip = false; VIEWS['the-nho'](); };
  if (!c) return;
  const step = d => { f.i = Math.max(0, Math.min(list.length - 1, f.i + d)); f.flip = false; VIEWS['the-nho'](); };
  $('#c-card').onclick = () => { f.flip = !f.flip; VIEWS['the-nho'](); };
  $('#c-prev').onclick = () => step(-1); $('#c-next').onclick = () => step(1);
  const mark = ok => { S.cards[c.i] = { ok, at: now() }; save(); if (f.onlyNew && ok) { f.order = null; f.flip = false; VIEWS['the-nho'](); } else step(1); };
  $('#c-yes').onclick = () => mark(true); $('#c-no').onclick = () => mark(false);
};

// ---------- CÔNG THỨC & MÁY TÍNH ----------
const CALCS = [
  { id: 'tvm', t: 'Giá trị thời gian của tiền', f: 'FV = PV × (1 + r/m)^(m·n) · EAR = (1 + r/m)^m − 1',
    in: [['pv', 'Số tiền hiện tại PV', 100e6], ['r', 'Lãi suất năm (%)', 8], ['n', 'Số năm', 3], ['m', 'Số kỳ ghép lãi/năm', 4]],
    run: v => { const fv = v.pv * (1 + v.r / 100 / v.m) ** (v.m * v.n); return [['FV', fmtM(fv)], ['Lãi suất hiệu dụng EAR', fmtP((1 + v.r / 100 / v.m) ** v.m - 1)]]; } },
  { id: 'pre', t: 'Lãi suất trả trước → trả sau', f: 'r_sau = r_trước ÷ (1 − r_trước)',
    in: [['r', 'Lãi suất trả trước (%/kỳ)', 10]], run: v => [['Lãi suất trả sau tương đương', fmtP(v.r / 100 / (1 - v.r / 100))]] },
  { id: 'bond', t: 'Định giá trái phiếu', f: 'P = Σ C/(1+y)^t + F/(1+y)^N · Dmod = Dmac ÷ (1 + y)',
    in: [['F', 'Mệnh giá', 100000], ['c', 'Lãi suất coupon (%/năm)', 8], ['k', 'Số lần trả lãi/năm', 1], ['T', 'Số năm còn lại', 5], ['y', 'Lợi suất yêu cầu (%/năm)', 10]],
    run: v => { const b = bond(v); return [['Giá trái phiếu', fmtM(b.p)], ['Lợi suất hiện hành', fmtP(v.c / 100 * v.F / b.p)], ['Duration Macaulay (năm)', b.mac.toFixed(3)], ['Duration điều chỉnh', b.mod.toFixed(3)]]; } },
  { id: 'ytm', t: 'Lợi suất đáo hạn (YTM)', f: 'Tìm y sao cho giá lý thuyết = giá thị trường',
    in: [['F', 'Mệnh giá', 100000], ['c', 'Lãi suất coupon (%/năm)', 8], ['k', 'Số lần trả lãi/năm', 1], ['T', 'Số năm còn lại', 5], ['P', 'Giá thị trường', 95000]],
    run: v => { let lo = -0.99, hi = 5; for (let i = 0; i < 200; i++) { const mid = (lo + hi) / 2; bond({ ...v, y: mid * 100 }).p > v.P ? (lo = mid) : (hi = mid); } return [['YTM', fmtP((lo + hi) / 2)]]; } },
  { id: 'capm', t: 'CAPM và định giá cao/thấp', f: 'E(r) = rf + β × (rm − rf)',
    in: [['rf', 'Lãi suất phi rủi ro (%)', 4], ['b', 'Hệ số beta', 1.2], ['rm', 'Lợi suất thị trường (%)', 12], ['er', 'Lợi suất kỳ vọng của bạn (%)', 15]],
    run: v => { const req = v.rf + v.b * (v.rm - v.rf); return [['Lợi suất yêu cầu', req.toFixed(2) + '%'], ['Kết luận', v.er > req ? 'Nằm phía trên SML: đang bị định giá thấp, nên mua' : v.er < req ? 'Nằm phía dưới SML: đang bị định giá cao, không nên mua' : 'Nằm trên SML: định giá hợp lý']]; } },
  { id: 'ddm', t: 'Mô hình Gordon (cổ tức tăng đều)', f: 'P0 = D1 ÷ (r − g), D1 = D0 × (1 + g)',
    in: [['d0', 'Cổ tức vừa trả D0 (đ)', 2000], ['g', 'Tốc độ tăng g (%)', 5], ['r', 'Tỷ suất yêu cầu r (%)', 12]],
    run: v => v.r <= v.g ? [['Lỗi', 'Cần r lớn hơn g']] : [['D1', fmtM(v.d0 * (1 + v.g / 100))], ['Giá hợp lý P0', fmtM(v.d0 * (1 + v.g / 100) / ((v.r - v.g) / 100))]] },
  { id: 'wacc', t: 'Chi phí vốn bình quân (WACC)', f: 'WACC = E/V·re + D/V·rd·(1 − t)',
    in: [['E', 'Giá trị vốn chủ E', 600], ['Dv', 'Giá trị nợ D', 400], ['re', 'Chi phí vốn chủ re (%)', 15], ['rd', 'Chi phí nợ rd (%)', 9], ['t', 'Thuế suất TNDN (%)', 20]],
    run: v => { const V = v.E + v.Dv; return [['WACC', fmtP((v.E / V) * v.re / 100 + (v.Dv / V) * v.rd / 100 * (1 - v.t / 100))]]; } },
  { id: 'adj', t: 'Giá tham chiếu điều chỉnh (GDKHQ)', f: "P' = (P − Cổ tức tiền + PR × I1) ÷ (1 + I1 + I2)",
    in: [['P', 'Giá đóng cửa trước ngày GDKHQ', 30000], ['C', 'Cổ tức tiền mặt/cp (đ)', 0], ['PR', 'Giá mua cổ phiếu phát hành thêm (đ)', 10000], ['I1', 'Tỷ lệ quyền mua (cp mới/cp cũ)', 0.2], ['I2', 'Tỷ lệ cổ tức bằng cổ phiếu', 0]],
    run: v => [['Giá tham chiếu điều chỉnh', fmtM((v.P - v.C + v.PR * v.I1) / (1 + v.I1 + v.I2))]] },
  { id: 'perf', t: 'Đo lường hiệu quả danh mục', f: 'Sharpe = (rp − rf)/σp · Treynor = (rp − rf)/βp · Jensen α = rp − [rf + βp(rm − rf)]',
    in: [['rp', 'Lợi suất danh mục (%)', 14], ['rf', 'Lãi suất phi rủi ro (%)', 4], ['sd', 'Độ lệch chuẩn σp (%)', 20], ['b', 'Beta βp', 1.1], ['rm', 'Lợi suất thị trường (%)', 11]],
    run: v => [['Sharpe', ((v.rp - v.rf) / v.sd).toFixed(3)], ['Treynor (%)', ((v.rp - v.rf) / v.b).toFixed(3)], ['Jensen alpha (%)', (v.rp - (v.rf + v.b * (v.rm - v.rf))).toFixed(3)]] },
];
function bond(v) {
  const k = v.k, N = Math.round(v.T * k), y = v.y / 100 / k, C = v.F * v.c / 100 / k;
  let p = 0, w = 0;
  for (let t = 1; t <= N; t++) { const cf = C + (t === N ? v.F : 0), pv = cf / (1 + y) ** t; p += pv; w += t * pv; }
  const mac = w / p / k; return { p, mac, mod: mac / (1 + y) };
}
const fmtM = x => (isFinite(x) ? Math.round(x).toLocaleString('vi-VN') : '—');
const fmtP = x => (isFinite(x) ? (x * 100).toLocaleString('vi-VN', { maximumFractionDigits: 3 }) + '%' : '—');
VIEWS['cong-thuc'] = () => {
  main(page('Công thức & máy tính', 'Bấm số nhanh cho bài tính', 'Nhập số liệu đề bài để kiểm tra kết quả. Mỗi máy tính kèm công thức gốc theo giáo trình.',
    `<div class="grid g2">${CALCS.map(c => `<div class="card stack calc" data-calc="${c.id}"><h2>${c.t}</h2><div class="formula">${esc(c.f)}</div>
      <div class="grid g2" style="gap:10px">${c.in.map(([k, lab, def]) => `<label class="f">${lab}<input type="number" step="any" id="${c.id}-${k}" value="${def}" inputmode="decimal"></label>`).join('')}</div>
      <div class="stack out-wrap" id="${c.id}-out"></div></div>`).join('')}</div>`));
  for (const c of CALCS) {
    const run = () => {
      const v = Object.fromEntries(c.in.map(([k]) => [k, parseFloat($(`#${c.id}-${k}`).value)]));
      const bad = Object.values(v).some(x => !isFinite(x));
      $(`#${c.id}-out`).innerHTML = bad ? '<p class="small muted">Nhập đủ các ô bằng số.</p>' :
        c.run(v).map(([k, val]) => `<div class="row between"><span class="small muted">${k}</span><span class="out">${esc(val)}</span></div>`).join('');
    };
    c.in.forEach(([k]) => ($(`#${c.id}-${k}`).oninput = run)); run();
  }
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
        <p class="small muted">Lệ phí dự thi 1.000.000 đồng cho mỗi loại chứng chỉ.</p></div>
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
  main(page('Cài đặt & sao lưu', 'Tiến độ của bạn', 'Mọi dữ liệu học tập chỉ lưu trong trình duyệt này. Sao lưu để chuyển sang máy khác.',
    `<div class="grid g2">
      <div class="card stack"><h2>Giao diện</h2><label class="f">Chế độ màu<select id="s-theme">${opts([['', 'Theo hệ thống'], ['light', 'Sáng'], ['dark', 'Tối']], S.theme)}</select></label>
        <label class="f">Chứng chỉ mục tiêu<select id="s-cert">${opts(Object.entries(CERTS).map(([k, c]) => [k, c.name]), S.prefs.cert)}</select></label></div>
      <div class="card stack"><h2>Sao lưu</h2><p class="small muted">Sao chép đoạn mã dưới đây và lưu lại; khi cần khôi phục, dán vào ô Khôi phục.</p>
        <textarea id="s-dump" readonly>${esc(dump)}</textarea><div class="row"><button class="btn" id="s-copy">Sao chép</button><button class="btn" id="s-file">Tải file .json</button></div></div>
      <div class="card stack"><h2>Khôi phục</h2><textarea id="s-in" placeholder="Dán mã sao lưu vào đây"></textarea>
        <div class="row"><button class="btn primary" id="s-restore">Khôi phục</button><label class="btn">Chọn file<input type="file" id="s-upload" accept="application/json,.json" hidden></label></div></div>
      <div class="card stack"><h2>Ghi chú báo lỗi (${S.reports.length})</h2><textarea id="s-rep" readonly>${esc(reports)}</textarea>
        <div class="row"><button class="btn" id="s-rep-copy" ${S.reports.length ? '' : 'disabled'}>Sao chép ghi chú</button></div></div>
      <div class="card stack"><h2>Xóa dữ liệu</h2><p class="small muted">Xóa lịch sử, câu đã làm, đánh dấu và thẻ đã nhớ trên máy này.</p><div><button class="btn danger" id="s-reset">Xóa toàn bộ tiến độ</button></div></div>
      <div class="card stack"><h2>Về dữ liệu</h2><p class="small">${fmt(D.q.length)} câu hỏi · ${D.law?.dieu.length || 0} điều luật · ${D.cards.length} thẻ số liệu.</p>
        <p class="small muted">Câu hỏi được biên soạn mới và soát theo văn bản hiện hành đến tháng 11/2026; câu Luật có trích nguyên văn đã được máy đối chiếu với văn bản gốc. Đây không phải trang chính thức của UBCKNN và không bảo đảm kết quả thi.</p></div>
    </div>`));
  const copy = async (id) => { const el = $('#' + id); try { await navigator.clipboard.writeText(el.value); toast('Đã sao chép.'); } catch { el.select(); toast('Hãy nhấn Ctrl+C / giữ để sao chép.'); } };
  $('#s-theme').onchange = e => { S.theme = e.target.value; applyTheme(); save(); };
  $('#s-cert').onchange = e => { S.prefs.cert = e.target.value; save(); };
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
  if (!q.length) { main(`<div class="page"><div class="card empty">Không tải được ngân hàng câu hỏi. Nếu bạn mở file trực tiếp trên máy, hãy dùng bản <b>dist/index.html</b> hoặc chạy qua máy chủ web.</div></div>`); renderNav(''); return; }
  if (S.sess && S.sess.parts?.some(p => p.ids.some(id => !D.byId.has(id)))) S.sess.parts.forEach(p => (p.ids = p.ids.filter(id => D.byId.has(id))));
  route();
  if ('serviceWorker' in navigator && location.protocol === 'https:' && document.querySelector('link[rel="manifest"]')) navigator.serviceWorker.register('sw.js').catch(() => {});
})();
})();
