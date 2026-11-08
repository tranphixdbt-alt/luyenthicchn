// Kiểm tra api/thong-ke.js với một redis-server chạy tạm trên máy (chạy: node web/tools/kiem_tra_thong_ke.js; cần `npm install` trong web/)
const { spawn } = require('child_process'), assert = require('assert'), path = require('path');
const API = path.join(__dirname, '../api/thong-ke.js'), PORT = 6390 + Math.floor(Math.random() * 100);
const call = (h, method, body, ip = '1.2.3.4') => new Promise(done => {
  const res = { code: 0, body: null, headers: {}, status(c) { this.code = c; return this; }, json(o) { this.body = o; done(this); }, end() { done(this); }, setHeader(k, v) { this.headers[k] = v; } };
  h({ method, body, headers: { 'x-forwarded-for': ip } }, res);
});
(async () => {
  for (const k of Object.keys(process.env)) if (/REDIS|^KV_/.test(k)) delete process.env[k];
  const off = require(API);
  assert.strictEqual((await call(off, 'GET')).body.off, true, 'chưa có kho thì báo tắt');
  assert.strictEqual((await call(off, 'POST', { a: [['L1-001', 1]] })).code, 204, 'chưa có kho thì POST bỏ qua êm');
  for (const k of Object.keys(require.cache)) if (k.includes('/api/')) delete require.cache[k];   // nạp lại cả _db.js để đọc biến mới
  const srv = spawn('redis-server', ['--port', String(PORT), '--save', '', '--appendonly', 'no'], { stdio: 'ignore' });
  await new Promise(r => setTimeout(r, 400));
  process.env.STORAGE_REDIS_URL = 'redis://127.0.0.1:' + PORT;   // tiền tố tùy ý vẫn phải nhận
  const h = require(API);
  try {
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
    console.log('THONG KE OK');
  } finally { srv.kill(); process.exit(process.exitCode || 0); }
})().catch(e => { console.error(e); process.exit(1); });
