// Dùng chung cho các hàm trong api/: kết nối kho Redis của dự án (Vercel không biến file bắt đầu bằng "_" thành hàm).
const crypto = require('crypto');
const { createClient } = require('redis');
const env = process.env;
const URL_ = env.REDIS_URL || env.KV_URL || env[Object.keys(env).sort().find(k => /(REDIS|KV)_URL$/.test(k))];

let client;   // giữ kết nối giữa các lần gọi của cùng một phiên bản hàm
async function db() {
  if (!client) { client = createClient({ url: URL_, socket: { connectTimeout: 5000 } }); client.on('error', () => {}); }
  if (!client.isOpen) await client.connect();
  return client;
}
const ipHash = req => crypto.createHash('sha256').update(String(req.headers['x-forwarded-for'] || '').split(',')[0].trim() || 'na').digest('hex').slice(0, 16);
// đếm số lần trong một cửa sổ thời gian; true nếu đã vượt giới hạn
async function limited(r, key, max, sec, by = 1) {
  const k = 'rl:' + key + ':' + Math.floor(Date.now() / 1000 / sec);
  const [n] = await r.multi().incrBy(k, by).expire(k, sec * 2).exec();
  return n > max;
}
function body(req) {
  let b = req.body;
  if (typeof b === 'string') { try { b = JSON.parse(b); } catch { b = null; } }
  return b && typeof b === 'object' ? b : null;
}
module.exports = { db, ipHash, limited, body, hasStore: !!URL_, env };
