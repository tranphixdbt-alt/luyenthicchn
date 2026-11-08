// Thống kê chung, ẩn danh: đếm số lượt làm và số lượt sai của từng câu (Vercel Function + Upstash Redis).
// POST {a: [[mã câu, 1 đúng | 0 sai], ...]} để cộng dồn; GET trả {n: {mã: lượt làm}, w: {mã: lượt sai}}.
// Cần biến môi trường của Upstash Redis (tự có khi nối kho Upstash với dự án trên Vercel).
const crypto = require('crypto');
// Tên biến tùy tiền tố chọn khi nối kho (KV_…, STORAGE_…, UPSTASH_REDIS_…): nhận mọi tên kết thúc bằng REST_API_URL / REST_URL
const env = process.env, pick = re => env[Object.keys(env).sort().find(k => re.test(k))];
const URL_ = env.KV_REST_API_URL || env.UPSTASH_REDIS_REST_URL || pick(/REST_(API_)?URL$/);
const TOKEN = env.KV_REST_API_TOKEN || env.UPSTASH_REDIS_REST_TOKEN || pick(/^(?!.*READ_ONLY).*REST_(API_)?TOKEN$/);
const ID = /^[A-Z][A-Z0-9]{0,3}-\d{3}$/, MAX_BATCH = 200, MAX_PER_MIN = 1000;

async function redis(cmds) {
  const r = await fetch(URL_ + '/pipeline', { method: 'POST', headers: { Authorization: 'Bearer ' + TOKEN, 'Content-Type': 'application/json' }, body: JSON.stringify(cmds) });
  if (!r.ok) throw new Error('redis ' + r.status);
  return (await r.json()).map(x => x.result);
}
const toObj = flat => { const o = {}; for (let i = 0; i + 1 < (flat || []).length; i += 2) o[flat[i]] = +flat[i + 1]; return o; };

module.exports = async (req, res) => {
  // chưa nối kho: GET báo tắt, POST bỏ qua êm (không làm trình duyệt báo lỗi)
  // kèm tên (không kèm giá trị) các biến liên quan để biết vì sao chưa nối được
  if (!URL_ || !TOKEN) return req.method === 'POST' ? res.status(204).end()
    : res.status(200).json({ off: true, n: {}, w: {}, vars: Object.keys(env).filter(k => /REDIS|UPSTASH|^KV_|REST_API/.test(k)) });
  try {
    if (req.method === 'GET') {
      const [n, w] = await redis([['HGETALL', 'n'], ['HGETALL', 'w']]);
      res.setHeader('Cache-Control', 's-maxage=600, stale-while-revalidate=3600');
      return res.status(200).json({ n: toObj(n), w: toObj(w), at: Date.now() });
    }
    if (req.method !== 'POST') return res.status(405).json({ error: 'method' });
    let body = req.body;
    if (typeof body === 'string') { try { body = JSON.parse(body); } catch { body = null; } }
    const a = Array.isArray(body?.a) ? body.a : null;
    if (!a || !a.length || a.length > MAX_BATCH || !a.every(x => Array.isArray(x) && ID.test(x[0]) && (x[1] === 0 || x[1] === 1)))
      return res.status(400).json({ error: 'bad body' });
    // chống gửi dồn: mỗi địa chỉ (đã băm, giữ 2 phút) tối đa 1000 lượt/phút
    const ip = String(req.headers['x-forwarded-for'] || '').split(',')[0].trim() || 'na';
    const key = 'rl:' + crypto.createHash('sha256').update(ip).digest('hex').slice(0, 16) + ':' + Math.floor(Date.now() / 60e3);
    const [used] = await redis([['INCRBY', key, a.length], ['EXPIRE', key, 120]]);
    if (used > MAX_PER_MIN) return res.status(429).json({ error: 'too many' });
    await redis(a.flatMap(([id, ok]) => ok ? [['HINCRBY', 'n', id, 1]] : [['HINCRBY', 'n', id, 1], ['HINCRBY', 'w', id, 1]]));
    return res.status(204).end();
  } catch (e) {
    return res.status(502).json({ error: 'store' });
  }
};
