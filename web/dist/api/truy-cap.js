// Đếm lượt truy cập cho trang quản trị: lượt xem, người truy cập (mã ngẫu nhiên trên trình duyệt, đếm bằng HyperLogLog),
// khung giờ, trang, thiết bị, khu vực, nguồn (lượt đầu mỗi phiên), và 200 lượt gần nhất (IP đã che bớt). Không lưu IP đầy đủ của khách.
const { db, ipHash, limited, body, hasStore, vnNow, vnDay, ipOf, maskIp, isBot, device, place } = require('./_db');
const VID = /^[0-9a-f-]{36}$/, PAGE = /^[a-z-]{1,24}$/, SRC = /^[a-z0-9-]{1,16}$/, KEEP = 120 * 86400;

module.exports = async (req, res) => {
  if (req.method !== 'POST') return res.status(405).json({ error: 'method' });
  if (!hasStore || isBot(req)) return res.status(204).end();
  const b = body(req);
  if (!b || !VID.test(b.v || '')) return res.status(400).json({ error: 'bad body' });
  try {
    const r = await db();
    if (await limited(r, 'tc:' + ipHash(req), 300, 60)) return res.status(429).json({ error: 'too many' });
    const now = vnNow(), day = vnDay(now), page = PAGE.test(b.p || '') ? b.p : 'khac', dev = device(req), where = place(req);
    const m = r.multi();
    if (SRC.test(b.s || '')) m.hIncrBy('st:src:' + day, b.s, 1).expire('st:src:' + day, KEEP);
    await m
      .hIncrBy('st:pv', day, 1)
      .pfAdd('st:uv:' + day, b.v).expire('st:uv:' + day, 400 * 86400)
      .pfAdd('st:uv:all', b.v)
      .hIncrBy('st:h:' + day, String(now.getUTCHours()), 1).expire('st:h:' + day, KEEP)
      .hIncrBy('st:pg:' + day, page, 1).expire('st:pg:' + day, KEEP)
      .hIncrBy('st:dev:' + day, dev, 1).expire('st:dev:' + day, KEEP)
      .hIncrBy('st:geo:' + day, where, 1).expire('st:geo:' + day, KEEP)
      .lPush('st:log', JSON.stringify({ at: Date.now(), p: page, dev, where, ip: maskIp(ipOf(req)) })).lTrim('st:log', 0, 199)
      .exec();
    return res.status(204).end();
  } catch {
    return res.status(502).json({ error: 'store' });
  }
};
