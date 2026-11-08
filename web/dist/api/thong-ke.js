// Thống kê chung, ẩn danh: đếm số lượt làm và số lượt sai của từng câu (Vercel Function + kho Redis của dự án).
// POST {a: [[mã câu, 1 đúng | 0 sai], ...]} để cộng dồn; GET trả {n: {mã: lượt làm}, w: {mã: lượt sai}}.
// Cần biến REDIS_URL (tự có khi nối kho Redis / Upstash với dự án trên Vercel; tiền tố nào cũng nhận).
const { db, ipHash, limited, body, hasStore, env } = require('./_db');
const ID = /^[A-Z][A-Z0-9]{0,3}-\d{3}$/, MAX_BATCH = 200, MAX_PER_MIN = 1000;
const nums = o => Object.fromEntries(Object.entries(o || {}).map(([k, v]) => [k, +v]));

module.exports = async (req, res) => {
  // chưa nối kho: GET báo tắt (kèm tên biến, không kèm giá trị), POST bỏ qua êm để trình duyệt không báo lỗi
  if (!hasStore) return req.method === 'POST' ? res.status(204).end()
    : res.status(200).json({ off: true, n: {}, w: {}, vars: Object.keys(env).filter(k => /REDIS|UPSTASH|^KV_/.test(k)) });
  try {
    if (req.method === 'GET') {
      const r = await db(), [n, w] = await Promise.all([r.hGetAll('n'), r.hGetAll('w')]);
      res.setHeader('Cache-Control', 's-maxage=600, stale-while-revalidate=3600');
      return res.status(200).json({ n: nums(n), w: nums(w), at: Date.now() });
    }
    if (req.method !== 'POST') return res.status(405).json({ error: 'method' });
    const a = Array.isArray(body(req)?.a) ? body(req).a : null;
    if (!a || !a.length || a.length > MAX_BATCH || !a.every(x => Array.isArray(x) && ID.test(x[0]) && (x[1] === 0 || x[1] === 1)))
      return res.status(400).json({ error: 'bad body' });
    // chống gửi dồn: mỗi địa chỉ (đã băm) tối đa 1000 lượt/phút
    const r = await db();
    if (await limited(r, 'tk:' + ipHash(req), MAX_PER_MIN, 60, a.length)) return res.status(429).json({ error: 'too many' });
    const m = r.multi();
    for (const [id, ok] of a) { m.hIncrBy('n', id, 1); if (!ok) m.hIncrBy('w', id, 1); }
    await m.exec();
    return res.status(204).end();
  } catch (e) {
    return res.status(502).json({ error: 'store' });
  }
};
