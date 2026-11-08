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
// Thông tin truy cập lấy từ tiêu đề Vercel gắn sẵn (khu vực theo IP), giờ Việt Nam (UTC+7)
const vnNow = () => new Date(Date.now() + 7 * 3600e3);
const vnDay = (d = vnNow()) => d.toISOString().slice(0, 10);
const ipOf = req => String(req.headers['x-forwarded-for'] || req.headers['x-real-ip'] || '').split(',')[0].trim().slice(0, 45);
const maskIp = ip => !ip ? 'Không rõ' : ip.includes(':') ? ip.split(':').slice(0, 2).join(':') + ':…' : ip.split('.').slice(0, 2).concat(['x', 'x']).join('.');
const ua = req => String(req.headers['user-agent'] || '');
const isBot = req => /bot|crawl|spider|slurp|headless|lighthouse|preview|facebookexternalhit|zalo.*link/i.test(ua(req));
const device = req => /iPad|Tablet/i.test(ua(req)) ? 'Máy tính bảng' : /Mobi|Android|iPhone/i.test(ua(req)) ? 'Điện thoại' : 'Máy tính';
const place = req => {
  const dec = v => { try { return decodeURIComponent(String(v || '')); } catch { return String(v || ''); } };
  const city = dec(req.headers['x-vercel-ip-city']), cc = String(req.headers['x-vercel-ip-country'] || '');
  return [city, cc].filter(Boolean).join(', ').slice(0, 60) || 'Không rõ';
};
module.exports = { db, ipHash, limited, body, hasStore: !!URL_, env, vnNow, vnDay, ipOf, maskIp, isBot, device, place };
