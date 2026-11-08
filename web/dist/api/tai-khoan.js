// Tài khoản học: đăng ký (SĐT + email + mật khẩu + chứng chỉ mục tiêu), đăng nhập, đồng bộ tiến độ, trang quản trị.
// POST {a: hành động, ...}; đăng nhập rồi thì gửi "Authorization: Bearer <mã phiên>". Trang quản trị gửi "X-Admin-Key".
// Mật khẩu chỉ lưu dạng băm scrypt + muối; mã phiên ngẫu nhiên 32 byte, hết hạn sau 180 ngày.
const crypto = require('crypto');
const { db, ipHash, limited, body, hasStore, env } = require('./_db');

const CERTS = ['moi-gioi', 'phan-tich', 'quan-ly-quy'];
const SESSION_SEC = 180 * 86400, MAX_DATA = 1_500_000;
const normPhone = s => { const d = String(s || '').replace(/[\s.\-()]/g, '').replace(/^\+?84/, '0'); return /^0\d{9}$/.test(d) ? d : null; };
const normEmail = s => { const e = String(s || '').trim().toLowerCase(); return e.length <= 120 && /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(e) ? e : null; };
const scrypt = (pw, salt) => new Promise((ok, no) => crypto.scrypt(pw, salt, 64, (e, k) => (e ? no(e) : ok(k))));
const pub = u => ({ id: u.id, phone: u.phone, email: u.email, name: u.name || '', cert: u.cert, created: u.created });

// Gộp tiến độ: câu/thẻ nào làm gần đây hơn thì giữ; lịch sử gộp theo thời điểm; cài đặt bên "win" thắng.
// shortcut: đánh dấu sao chỉ cộng dồn (bỏ sao ở máy này không xóa sao ở máy kia), đủ dùng khi mỗi người học một mình.
function merge(a, b, prefsFromA) {
  a = a || {}; b = b || {};
  const newer = (x, y, t) => { const o = { ...(x || {}) }; for (const [k, v] of Object.entries(y || {})) if (v && (!o[k] || (v[t] || 0) >= (o[k][t] || 0))) o[k] = v; return o; };
  const seen = new Set();
  const hist = [...(b.hist || []), ...(a.hist || [])].filter(h => h && h.at && !seen.has(h.at + '|' + h.title) && seen.add(h.at + '|' + h.title))
    .sort((x, y) => y.at - x.at).slice(0, 200);
  return { q: newer(a.q, b.q, 'last'), cards: newer(a.cards, b.cards, 'at'), hist, star: { ...(a.star || {}), ...(b.star || {}) },
    prefs: prefsFromA ? { ...(b.prefs || {}), ...(a.prefs || {}) } : { ...(a.prefs || {}), ...(b.prefs || {}) } };
}
const pick = d => (d && typeof d === 'object' ? { q: d.q, star: d.star, hist: d.hist, cards: d.cards, prefs: d.prefs } : {});

async function newSession(r, id) {
  const t = crypto.randomBytes(32).toString('hex');
  await r.multi().set('t:' + t, id, { EX: SESSION_SEC }).sAdd('ut:' + id, t).exec();
  return t;
}
async function userOf(r, req) {
  const t = String(req.headers.authorization || '').replace(/^Bearer\s+/i, '');
  if (!/^[0-9a-f]{64}$/.test(t)) return null;
  const id = await r.get('t:' + t), raw = id && await r.get('u:' + id);
  return raw ? { u: JSON.parse(raw), t } : null;
}
async function loadData(r, id) { const raw = await r.get('d:' + id); return raw ? JSON.parse(raw) : {}; }
async function saveData(r, id, d) {
  const s = JSON.stringify(d);
  if (s.length > MAX_DATA) throw Object.assign(new Error('big'), { code: 413 });
  await r.set('d:' + id, s);
}
const fail = (res, code, msg) => res.status(code).json({ error: msg });

module.exports = async (req, res) => {
  if (req.method !== 'POST') return fail(res, 405, 'Chỉ nhận POST.');
  if (!hasStore) return fail(res, 503, 'Máy chủ chưa nối kho dữ liệu.');
  const b = body(req);
  if (!b || typeof b.a !== 'string') return fail(res, 400, 'Yêu cầu không hợp lệ.');
  try {
    const r = await db(), ip = ipHash(req);

    if (b.a === 'dang-ky') {
      if (await limited(r, 'reg:' + ip, 10, 3600)) return fail(res, 429, 'Bạn tạo tài khoản quá nhiều lần, hãy thử lại sau.');
      const phone = normPhone(b.phone), email = normEmail(b.email), pw = String(b.password || ''), name = String(b.name || '').trim().slice(0, 60);
      if (!phone) return fail(res, 400, 'Số điện thoại chưa đúng (10 số, bắt đầu bằng 0).');
      if (!email) return fail(res, 400, 'Email chưa đúng.');
      if (pw.length < 8 || pw.length > 128) return fail(res, 400, 'Mật khẩu cần từ 8 ký tự.');
      if (!CERTS.includes(b.cert)) return fail(res, 400, 'Hãy chọn chứng chỉ mục tiêu.');
      if (b.consent !== true) return fail(res, 400, 'Cần đồng ý điều khoản dữ liệu cá nhân.');
      const id = crypto.randomUUID();
      // giữ chỗ SĐT và email trước (NX) để hai người không đăng ký trùng cùng lúc
      if (!(await r.set('ix:p:' + phone, id, { NX: true }))) return fail(res, 409, 'Số điện thoại đã có tài khoản. Hãy đăng nhập.');
      if (!(await r.set('ix:e:' + email, id, { NX: true }))) { await r.del('ix:p:' + phone); return fail(res, 409, 'Email đã có tài khoản. Hãy đăng nhập.'); }
      const salt = crypto.randomBytes(16).toString('hex'), hash = (await scrypt(pw, salt)).toString('hex'), now = Date.now();
      const u = { id, phone, email, name, cert: b.cert, salt, hash, created: now, last: now, consentAt: now };
      const data = merge({}, pick(b.data)); data.prefs = { ...(data.prefs || {}), cert: b.cert };
      await r.multi().set('u:' + id, JSON.stringify(u)).zAdd('users', { score: now, value: id }).exec();
      await saveData(r, id, data);
      return res.status(200).json({ token: await newSession(r, id), user: pub(u), data });
    }

    if (b.a === 'dang-nhap') {
      const key = String(b.id || '').includes('@') ? 'ix:e:' + normEmail(b.id) : 'ix:p:' + normPhone(b.id);
      if (await limited(r, 'login:' + ip, 30, 600) || await limited(r, 'login:' + key, 10, 3600)) return fail(res, 429, 'Đăng nhập sai quá nhiều lần, hãy thử lại sau.');
      const id = await r.get(key), raw = id && await r.get('u:' + id), u = raw && JSON.parse(raw);
      const ok = u && crypto.timingSafeEqual(await scrypt(String(b.password || ''), u.salt), Buffer.from(u.hash, 'hex'));
      if (!ok) return fail(res, 401, 'SĐT/email hoặc mật khẩu chưa đúng.');
      const data = merge(await loadData(r, id), pick(b.data), true);   // cài đặt (mục tiêu) trên tài khoản thắng máy mới
      u.last = Date.now();
      await r.set('u:' + id, JSON.stringify(u)); await saveData(r, id, data);
      return res.status(200).json({ token: await newSession(r, id), user: pub(u), data });
    }

    if (b.a === 'quan-tri') {
      const key = String(req.headers['x-admin-key'] || '');
      if (!env.ADMIN_KEY || env.ADMIN_KEY.length < 12) return fail(res, 503, 'Chưa đặt biến ADMIN_KEY (từ 12 ký tự) trên Vercel.');
      if (await limited(r, 'adm:' + ip, 20, 600)) return fail(res, 429, 'Thử quá nhiều lần, hãy đợi 10 phút.');
      const a = Buffer.from(crypto.createHash('sha256').update(key).digest()), e = Buffer.from(crypto.createHash('sha256').update(env.ADMIN_KEY).digest());
      if (!crypto.timingSafeEqual(a, e)) return fail(res, 401, 'Sai mã quản trị.');
      const ids = await r.zRange('users', 0, -1, { REV: true }), out = [];
      for (const id of ids.slice(0, 5000)) {
        const raw = await r.get('u:' + id); if (!raw) continue;
        const u = JSON.parse(raw), d = await loadData(r, id), q = Object.values(d.q || {});
        out.push({ ...pub(u), last: u.last, done: q.length, ok: q.filter(s => s && s.lastOk).length, exams: (d.hist || []).filter(h => h.kind === 'exam').length });
      }
      return res.status(200).json({ users: out });
    }

    const me = await userOf(r, req);
    if (!me) return fail(res, 401, 'Phiên đăng nhập đã hết hạn, hãy đăng nhập lại.');
    const { u, t } = me;

    if (b.a === 'luu') {
      if (await limited(r, 'sync:' + u.id, 120, 600)) return fail(res, 429, 'Đồng bộ quá dày, hãy thử lại sau.');
      const data = merge(await loadData(r, u.id), pick(b.data));
      await saveData(r, u.id, data);
      u.last = Date.now(); await r.set('u:' + u.id, JSON.stringify(u));
      return res.status(200).json({ user: pub(u), data, at: u.last });
    }
    if (b.a === 'cap-nhat') {
      if (b.name !== undefined) u.name = String(b.name).trim().slice(0, 60);
      if (b.cert !== undefined) { if (!CERTS.includes(b.cert)) return fail(res, 400, 'Chứng chỉ không hợp lệ.'); u.cert = b.cert; }
      await r.set('u:' + u.id, JSON.stringify(u));
      return res.status(200).json({ user: pub(u) });
    }
    if (b.a === 'dang-xuat') { await r.multi().del('t:' + t).sRem('ut:' + u.id, t).exec(); return res.status(200).json({ ok: true }); }
    if (b.a === 'xoa') {
      const ok = crypto.timingSafeEqual(await scrypt(String(b.password || ''), u.salt), Buffer.from(u.hash, 'hex'));
      if (!ok) return fail(res, 401, 'Mật khẩu chưa đúng.');
      const toks = await r.sMembers('ut:' + u.id), m = r.multi();
      for (const x of toks) m.del('t:' + x);
      await m.del(['ut:' + u.id, 'u:' + u.id, 'd:' + u.id, 'ix:p:' + u.phone, 'ix:e:' + u.email]).zRem('users', u.id).exec();
      return res.status(200).json({ ok: true });
    }
    return fail(res, 400, 'Hành động không hợp lệ.');
  } catch (e) {
    if (e.code === 413) return fail(res, 413, 'Dữ liệu tiến độ quá lớn.');
    return fail(res, 502, 'Máy chủ đang bận, hãy thử lại.');
  }
};
module.exports.merge = merge;   // để kiểm thử
