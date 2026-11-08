// Kiểm tra api/tai-khoan.js với redis-server chạy tạm (chạy: node web/tools/kiem_tra_tai_khoan.js; cần `npm install` trong web/)
const { spawn } = require('child_process'), assert = require('assert'), path = require('path');
const API = path.join(__dirname, '../api/tai-khoan.js'), PORT = 6490 + Math.floor(Math.random() * 100);
const UA = { 'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0) Mobile', 'x-vercel-ip-city': 'Ho%20Chi%20Minh%20City', 'x-vercel-ip-country': 'VN' };
const call = (h, b, headers = {}, ip = '1.2.3.4') => new Promise(done => {
  const res = { code: 0, body: null, status(c) { this.code = c; return this; }, json(o) { this.body = o; done(this); }, end() { done(this); }, setHeader() {} };
  h({ method: 'POST', body: b, headers: { 'x-forwarded-for': ip, ...UA, ...headers } }, res);
});
(async () => {
  const srv = spawn('redis-server', ['--port', String(PORT), '--save', '', '--appendonly', 'no'], { stdio: 'ignore' });
  await new Promise(r => setTimeout(r, 400));
  for (const k of Object.keys(process.env)) if (/REDIS|^KV_/.test(k)) delete process.env[k];
  process.env.REDIS_URL = 'redis://127.0.0.1:' + PORT; process.env.ADMIN_KEY = 'khoa-quan-tri-thu-123';
  const h = require(API), { merge } = h, tc = require(path.join(__dirname, '../api/truy-cap.js'));
  try {
    // gộp tiến độ: câu làm gần đây hơn thắng, lịch sử không trùng, cài đặt theo bên được chọn
    const m = merge({ q: { A: { last: 5, lastOk: true }, B: { last: 9 } }, hist: [{ at: 1, title: 'x' }], prefs: { cert: 'phan-tich' } },
      { q: { A: { last: 7, lastOk: false }, B: { last: 3 }, C: { last: 1 } }, hist: [{ at: 1, title: 'x' }, { at: 2, title: 'y' }], prefs: { cert: 'moi-gioi' } }, true);
    assert.deepStrictEqual([m.q.A.last, m.q.B.last, m.q.C.last, m.hist.length, m.hist[0].at, m.prefs.cert], [7, 9, 1, 2, 2, 'phan-tich']);

    const local = { q: { 'L1-001': { n: 1, ok: 1, last: 100, lastOk: true } }, hist: [{ at: 50, title: 'Ôn luyện', kind: 'practice' }], prefs: { cert: 'phan-tich' } };
    const reg = { a: 'dang-ky', phone: '0912 345 678', email: 'An@Mail.com', password: 'matkhau123', name: 'An', cert: 'moi-gioi', consent: true, data: local };
    for (const [bad, msg] of [[{ phone: '123' }, 'Số điện thoại'], [{ email: 'x@' }, 'Email'], [{ password: 'ngan' }, 'Mật khẩu'], [{ cert: 'abc' }, 'chứng chỉ'], [{ consent: false }, 'đồng ý']]) {
      const r = await call(h, { ...reg, ...bad }); assert.strictEqual(r.code, 400); assert.match(r.body.error, new RegExp(msg));
    }
    const r1 = await call(h, reg);
    assert.strictEqual(r1.code, 200); assert.match(r1.body.token, /^[0-9a-f]{64}$/);
    assert.deepStrictEqual([r1.body.user.phone, r1.body.user.email, r1.body.user.cert], ['0912345678', 'an@mail.com', 'moi-gioi']);
    assert.strictEqual(r1.body.data.q['L1-001'].lastOk, true, 'tiến độ khách được gộp vào tài khoản');
    assert.strictEqual(r1.body.data.prefs.cert, 'moi-gioi', 'mục tiêu lấy theo lúc đăng ký');
    assert.ok(!('hash' in r1.body.user) && !('salt' in r1.body.user), 'không trả mật khẩu băm');
    assert.strictEqual((await call(h, { ...reg, email: 'khac@mail.com' })).code, 409, 'trùng SĐT');
    assert.strictEqual((await call(h, { ...reg, phone: '0987654321' })).code, 409, 'trùng email');
    const auth = { authorization: 'Bearer ' + r1.body.token };

    // máy thứ hai: đăng nhập bằng email hoặc SĐT, nhận tiến độ, gộp tiến độ của máy đó
    assert.strictEqual((await call(h, { a: 'dang-nhap', id: 'an@mail.com', password: 'sai-mat-khau' })).code, 401);
    const r2 = await call(h, { a: 'dang-nhap', id: '+84912345678', password: 'matkhau123', data: { q: { 'L1-002': { n: 1, ok: 0, last: 200, lastOk: false } }, prefs: { cert: 'quan-ly-quy' } } });
    assert.strictEqual(r2.code, 200);
    assert.ok(r2.body.data.q['L1-001'] && r2.body.data.q['L1-002'], 'có tiến độ của cả hai máy');
    assert.strictEqual(r2.body.data.prefs.cert, 'moi-gioi', 'mục tiêu trên tài khoản không bị máy mới ghi đè');

    // đồng bộ: câu làm lại gần đây hơn thắng
    const r3 = await call(h, { a: 'luu', data: { q: { 'L1-001': { n: 2, ok: 1, last: 300, lastOk: false } } } }, auth);
    assert.strictEqual(r3.code, 200); assert.strictEqual(r3.body.data.q['L1-001'].lastOk, false);
    assert.strictEqual((await call(h, { a: 'luu', data: {} }, { authorization: 'Bearer ' + 'f'.repeat(64) })).code, 401, 'mã phiên giả bị từ chối');
    assert.strictEqual((await call(h, { a: 'luu', data: { q: { x: 'y'.repeat(1_600_000) } } }, auth)).code, 413, 'chặn dữ liệu quá lớn');
    assert.strictEqual((await call(h, { a: 'cap-nhat', cert: 'phan-tich', name: 'An Nguyễn' }, auth)).body.user.cert, 'phan-tich');

    // truy cập: 3 lượt xem của 2 người; bot bị bỏ qua; mã người truy cập sai bị từ chối
    const v1 = '11111111-1111-4111-8111-111111111111', v2 = '22222222-2222-4222-8222-222222222222';
    for (const [v, p] of [[v1, 'tong-quan'], [v1, 'thi-thu'], [v2, 'tong-quan']]) assert.strictEqual((await call(tc, { v, p }, {}, '113.161.5.9')).code, 204);
    assert.strictEqual((await call(tc, { v: v1, p: 'tong-quan' }, { 'user-agent': 'Googlebot/2.1' })).code, 204);
    assert.strictEqual((await call(tc, { v: 'abc', p: 'x' })).code, 400);

    // quản trị: cần khóa đúng; trả danh sách không có mật khẩu
    assert.strictEqual((await call(h, { a: 'quan-tri' }, { 'x-admin-key': 'sai' })).code, 401);
    const ad = await call(h, { a: 'quan-tri' }, { 'x-admin-key': 'khoa-quan-tri-thu-123' });
    assert.strictEqual(ad.code, 200); assert.strictEqual(ad.body.users.length, 1);
    assert.deepStrictEqual([ad.body.users[0].phone, ad.body.users[0].name, ad.body.users[0].done], ['0912345678', 'An Nguyễn', 2]);
    assert.ok(!JSON.stringify(ad.body).includes('"hash"'));
    const st = ad.body.stats, today = st.days[29];
    assert.deepStrictEqual([today.pv, today.uv, st.uvAll, st.pvAll], [3, 2, 2, 3], 'đếm lượt xem và người truy cập (bỏ bot)');
    assert.strictEqual(st.pages['tong-quan'], 2); assert.strictEqual(st.devs['Điện thoại'], 3); assert.strictEqual(st.geo['Ho Chi Minh City, VN'], 3);
    assert.strictEqual(st.hours.reduce((a, n) => a + n, 0), 3);
    assert.strictEqual(st.log[0].ip, '113.161.x.x', 'khách: IP chỉ lưu dạng che bớt');
    assert.ok(!JSON.stringify(st).includes('113.161.5.9'), 'không lưu IP đầy đủ của khách');
    assert.strictEqual(ad.body.logins.length, 2, 'đăng ký + đăng nhập = 2 lần');
    assert.strictEqual(ad.body.logins[0].ip, '1.2.3.4'); assert.strictEqual(ad.body.logins[0].who, 'An Nguyễn');
    assert.strictEqual(ad.body.users[0].login.where, 'Ho Chi Minh City, VN');

    // đăng xuất làm hỏng mã phiên; xóa tài khoản cần đúng mật khẩu và xóa sạch
    assert.strictEqual((await call(h, { a: 'dang-xuat' }, auth)).code, 200);
    assert.strictEqual((await call(h, { a: 'luu', data: {} }, auth)).code, 401);
    const t2 = { authorization: 'Bearer ' + r2.body.token };
    assert.strictEqual((await call(h, { a: 'xoa', password: 'sai' }, t2)).code, 401);
    assert.strictEqual((await call(h, { a: 'xoa', password: 'matkhau123' }, t2)).code, 200);
    assert.strictEqual((await call(h, { a: 'dang-nhap', id: '0912345678', password: 'matkhau123' })).code, 401, 'đã xóa thì không đăng nhập được');
    assert.strictEqual((await call(h, { a: 'quan-tri' }, { 'x-admin-key': 'khoa-quan-tri-thu-123' })).body.logins.length, 0, 'xóa tài khoản thì xóa lịch sử đăng nhập');
    assert.strictEqual((await call(h, reg)).code, 200, 'xóa xong đăng ký lại được bằng SĐT/email cũ');

    // chặn dò mật khẩu: một tài khoản tối đa 10 lần đăng nhập/giờ
    let last; for (let i = 0; i < 11; i++) last = await call(h, { a: 'dang-nhap', id: '0912345678', password: 'sai' + i }, {}, '5.5.5.' + i);
    assert.strictEqual(last.code, 429);
    console.log('TAI KHOAN OK');
  } finally { srv.kill(); process.exit(process.exitCode || 0); }
})().catch(e => { console.error(e); process.exit(1); });
