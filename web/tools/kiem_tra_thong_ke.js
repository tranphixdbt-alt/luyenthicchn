// Kiểm tra api/thong-ke.js với một Upstash Redis giả (chạy: node web/tools/kiem_tra_thong_ke.js)
const http = require('http'), assert = require('assert');
const db = {};
const srv = http.createServer((req, res) => {
  let b = ''; req.on('data', c => (b += c)); req.on('end', () => {
    assert.strictEqual(req.headers.authorization, 'Bearer t0k');
    const out = JSON.parse(b).map(([cmd, k, f, v]) => {
      if (cmd === 'HINCRBY') { db[k] = db[k] || {}; db[k][f] = (db[k][f] || 0) + v; return { result: db[k][f] }; }
      if (cmd === 'HGETALL') return { result: Object.entries(db[k] || {}).flat().map(String) };
      if (cmd === 'INCRBY') { db[k] = (db[k] || 0) + f; return { result: db[k] }; }
      if (cmd === 'EXPIRE') return { result: 1 };
      throw new Error(cmd);
    });
    res.setHeader('content-type', 'application/json'); res.end(JSON.stringify(out));
  });
});
const call = (h, method, body, ip = '1.2.3.4') => new Promise(done => {
  const res = { code: 0, body: null, headers: {}, status(c) { this.code = c; return this; }, json(o) { this.body = o; done(this); }, end() { done(this); }, setHeader(k, v) { this.headers[k] = v; } };
  h({ method, body, headers: { 'x-forwarded-for': ip } }, res);
});
srv.listen(0, async () => {
  const off = require('../api/thong-ke.js');
  assert.strictEqual((await call(off, 'GET')).body.off, true, 'chưa có kho thì báo tắt');
  assert.strictEqual((await call(off, 'POST', { a: [['L1-001', 1]] })).code, 204, 'chưa có kho thì POST bỏ qua êm');
  delete require.cache[require.resolve('../api/thong-ke.js')];
  process.env.KV_REST_API_URL = 'http://127.0.0.1:' + srv.address().port; process.env.KV_REST_API_TOKEN = 't0k';
  const h = require('../api/thong-ke.js');
  assert.strictEqual((await call(h, 'POST', { a: [['L1-001', 0], ['L1-001', 1], ['C4-010', 0]] })).code, 204);
  assert.strictEqual((await call(h, 'POST', JSON.stringify({ a: [['L1-001', 0]] }))).code, 204, 'nhận cả thân dạng chuỗi (sendBeacon)');
  for (const bad of [null, {}, { a: [] }, { a: [['x', 1]] }, { a: [['L1-001', 2]] }, { a: Array(201).fill(['L1-001', 1]) }])
    assert.strictEqual((await call(h, 'POST', bad)).code, 400, 'từ chối dữ liệu sai: ' + JSON.stringify(bad)?.slice(0, 40));
  const g = await call(h, 'GET');
  assert.deepStrictEqual(g.body.n, { 'L1-001': 3, 'C4-010': 1 }); assert.deepStrictEqual(g.body.w, { 'L1-001': 2, 'C4-010': 1 });
  assert.match(g.headers['Cache-Control'], /s-maxage/);
  for (let i = 0; i < 5; i++) await call(h, 'POST', { a: Array(200).fill(['L2-001', 1]) }, '9.9.9.9');
  assert.strictEqual((await call(h, 'POST', { a: [['L2-001', 1]] }, '9.9.9.9')).code, 429, 'chặn gửi dồn quá 1000 lượt/phút');
  assert.strictEqual((await call(h, 'PUT', {})).code, 405);
  console.log('THONG KE OK'); srv.close();
});
