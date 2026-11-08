// Kiểm tra giao diện tài khoản trên máy chủ thử (may_chu_thu.js + redis-server): khách vẫn dùng bình thường,
// đăng ký mang theo tiến độ, máy thứ hai đăng nhập nhận lại tiến độ, đồng bộ, quản trị, đăng xuất, xóa tài khoản.
// Chạy: node kiem_tra_tai_khoan.mjs http://localhost:8777/ <ADMIN_KEY>
import { chromium } from "playwright-core";
const [url, adminKey] = process.argv.slice(2);
const b = await chromium.launch({ executablePath: "/opt/pw-browsers/chromium-1194/chrome-linux/chrome" });
const A = (c, m) => { if (!c) throw new Error(m); };
const errs = [];
const newPage = async (w = 1280, h = 900) => { const ctx = await b.newContext({ viewport: { width: w, height: h } }); const p = await ctx.newPage(); p.on("pageerror", e => errs.push(e.message)); return p; };
const state = p => p.evaluate(() => JSON.parse(localStorage.getItem('docchn_v1') || 'null'));
const start = async p => { await p.click('#f-start'); await p.waitForTimeout(250); if (await p.$('#modal-root .btn.primary')) await p.click('#modal-root .btn.primary'); await p.waitForSelector('#qcard'); };
const phone = '09' + String(Date.now()).slice(-8), email = `t${Date.now()}@vi.du`;

// 1) Khách trên máy tính: thấy nút góc phải và dòng gợi ý; làm 1 câu vẫn lưu trên máy
const p1 = await newPage();
await p1.goto(url + "#tong-quan"); await p1.waitForSelector('#acct-desk .btn.primary');
A(await p1.isVisible('#acct-desk .hint'), 'máy tính: cần dòng gợi ý ở góc phải');
A(await p1.$('.acct-nudge'), 'Tổng quan: cần thẻ gợi ý tạo tài khoản');
A(await p1.$('.tip-today'), 'Tổng quan: cần gợi ý hôm nay theo mục tiêu');
await p1.goto(url + "#on-luyen"); await p1.waitForSelector('#f-start'); await start(p1);
await p1.click('.opt'); await p1.waitForTimeout(200);
const done1 = Object.keys((await state(p1)).q).length; A(done1 === 1, 'khách: câu đã làm phải lưu trên máy');
// 2) Đăng ký: kiểm tra ô đồng ý, rồi tạo tài khoản mang theo tiến độ
await p1.goto(url + "#tai-khoan"); await p1.waitForSelector('#f-reg');
await p1.fill('#f-reg [name=name]', 'Bình'); await p1.fill('#f-reg [name=phone]', phone); await p1.fill('#f-reg [name=email]', email);
await p1.fill('#f-reg [name=password]', 'matkhau123'); await p1.selectOption('#f-reg [name=cert]', 'moi-gioi');
await p1.click('#f-reg button'); await p1.waitForTimeout(300);
A(!(await p1.evaluate(() => localStorage.getItem('btinvest_auth'))), 'chưa đồng ý thì không được tạo tài khoản');
await p1.check('#f-reg [name=consent]'); await p1.click('#f-reg button');
await p1.waitForFunction(() => location.hash === '#tong-quan' && !!localStorage.getItem('btinvest_auth'));
await p1.waitForSelector('#acct-desk .acct-me');
A(!(await p1.$('.acct-nudge')), 'đã có tài khoản thì không hiện gợi ý tạo tài khoản');
A(/Bình/.test(await p1.textContent('#acct-desk')), 'nút góc phải hiện tên');
// 3) Làm thêm 1 câu: tự đồng bộ lên máy chủ (đợi quá 4 giây)
await p1.goto(url + "#on-luyen"); await p1.waitForSelector('#f-start'); await start(p1);
await p1.click('.opt'); await p1.waitForTimeout(5500);
// 4) Máy thứ hai (điện thoại): đăng nhập bằng SĐT, nhận đủ 2 câu đã làm và mục tiêu
const p2 = await newPage(390, 844);
await p2.goto(url + "#tong-quan"); await p2.waitForSelector('#acct-top .btn');
A(!(await p2.isVisible('#acct-desk')), 'điện thoại: không hiện nút cố định của máy tính');
A(await p2.isVisible('#acct-top .btn'), 'điện thoại: nút Đăng nhập trên thanh trên cùng');
A((await p2.evaluate(() => document.documentElement.scrollWidth - innerWidth)) <= 0, 'điện thoại: không tràn ngang');
await p2.click('#acct-top .btn'); await p2.waitForSelector('#f-login');
await p2.fill('#f-login [name=id]', phone); await p2.fill('#f-login [name=password]', 'sai-mat-khau'); await p2.click('#f-login button');
await p2.waitForTimeout(600); A(!(await p2.evaluate(() => localStorage.getItem('btinvest_auth'))), 'sai mật khẩu không được đăng nhập');
await p2.fill('#f-login [name=password]', 'matkhau123'); await p2.click('#f-login button');
await p2.waitForFunction(() => !!localStorage.getItem('btinvest_auth'));
const s2 = await state(p2);
A(Object.keys(s2.q).length === 2, 'máy thứ hai phải nhận 2 câu đã làm, có ' + Object.keys(s2.q).length);
A(s2.prefs.cert === 'moi-gioi', 'máy thứ hai nhận mục tiêu của tài khoản');
// 5) Quản trị: sai mã bị từ chối, đúng mã thấy tài khoản vừa tạo
const p3 = await newPage();
await p3.goto(url + "#quan-tri"); await p3.waitForSelector('#q-f');
await p3.fill('#q-f [name=k]', 'sai-ma'); await p3.click('#q-f button'); await p3.waitForSelector('#q-f'); await p3.waitForTimeout(400);
A(/Sai mã/.test(await p3.textContent('.page')), 'sai mã quản trị phải báo lỗi');
await p3.fill('#q-f [name=k]', adminKey); await p3.click('#q-f button'); await p3.waitForSelector('#q-csv');
A((await p3.textContent('table')).includes(phone), 'quản trị thấy SĐT vừa đăng ký');
// 6) Đăng xuất trên máy 1 giữ tiến độ; xóa tài khoản trên máy 2
await p1.goto(url + "#tai-khoan"); await p1.waitForSelector('#a-out'); await p1.click('#a-out');
await p1.waitForFunction(() => !localStorage.getItem('btinvest_auth'));
A(Object.keys((await state(p1)).q).length === 2, 'đăng xuất vẫn giữ tiến độ trên máy');
await p2.goto(url + "#tai-khoan"); await p2.waitForSelector('#a-del'); await p2.click('#a-del');
await p2.fill('#modal-root input', 'matkhau123'); await p2.click('#modal-root .btn.danger');
await p2.waitForFunction(() => !localStorage.getItem('btinvest_auth'));
await p3.goto(url + "#tong-quan"); await p3.goto(url + "#quan-tri"); await p3.waitForSelector('#q-csv');
A(!(await p3.textContent('table')).includes(phone), 'xóa tài khoản thì quản trị không còn thấy');
A(!errs.length, 'lỗi trang: ' + errs.join(' | '));
await b.close(); console.log("TAI KHOAN UI OK");
