// Kiểm tra trang Trọng tâm từng môn, gửi số liệu ẩn danh và thi thử từng môn (chạy: node kiem_tra_trong_tam.mjs <url>)
import { chromium } from "playwright-core";
const url = process.argv[2];
const b = await chromium.launch({ executablePath: "/opt/pw-browsers/chromium-1194/chrome-linux/chrome" });
const p = await b.newPage({ viewport: { width: 1280, height: 900 } }); const errs = []; p.on("pageerror", e => errs.push(e.message));
const A = (c, m) => { if (!c) throw new Error(m); };
const posts = [];
await p.route("**/api/thong-ke", async r => {
  if (r.request().method() === "POST") { posts.push(JSON.parse(r.request().postData())); return r.fulfill({ status: 204 }); }
  const n = {}, w = {}; for (const id of HARD) { n[id] = 20; w[id] = 15; } for (const id of EASY) { n[id] = 20; w[id] = 1; }
  return r.fulfill({ status: 200, contentType: "application/json", body: JSON.stringify({ n, w }) });
});
await p.goto(url + "#tong-quan");
const Q = await p.evaluate(() => JSON.parse(document.getElementById('data-questions').textContent));
const byIdT = id => Q.find(x => x.id === id).topic;
const mg = Q.filter(q => q.subject === 'MG'), HARD = mg.slice(0, 12).map(q => q.id), EASY = mg.slice(12, 40).map(q => q.id);
const t = Date.now(), q = {};
mg.slice(50, 60).forEach((x, k) => q[x.id] = { n: 2, ok: k % 2, box: 1, due: t, lastOk: k % 3 === 0 });
Q.filter(x => x.subject === 'LU').slice(0, 5).forEach(x => q[x.id] = { n: 1, ok: 0, box: 1, due: t, lastOk: false });
const base = { v: 1, q, star: {}, hist: [], sess: null, last: null, theme: '', reports: [], cards: {}, prefs: { cert: 'moi-gioi', n: 25, mode: 'both', focus: 'MG' } };
const setState = st => p.evaluate(s => localStorage.setItem('docchn_v1', JSON.stringify(s)), st);
const sess = async () => (await p.evaluate(() => JSON.parse(localStorage.getItem('docchn_v1')).sess));
// 1) Trọng tâm: chỉ môn Môi giới, có phần của bạn và phần nhiều người sai
await setState(base); await p.goto(url + "#trong-tam"); await p.reload(); await p.waitForSelector('#tt-mine');
await p.waitForSelector('#tt-hard');
const mineTopics = await p.$$eval('[data-mytopic]', bs => bs.map(x => x.dataset.mytopic));
A(mineTopics.length && mineTopics.every(t => Q.some(x => x.subject === 'MG' && x.topic === t)), 'chủ đề của bạn phải thuộc môn Môi giới');
await p.click('#tt-hard'); await p.waitForSelector('#qcard');
let ids = (await sess()).parts[0].ids; A(ids.length === 12 && ids.every(id => HARD.includes(id)), 'luyện câu nhiều người sai phải đúng 12 câu khó');
// 2) Đổi sang môn Pháp luật: không lẫn câu môn khác
await setState({ ...base, prefs: { ...base.prefs, focus: 'MG' } }); await p.goto(url + "#trong-tam"); await p.reload(); await p.waitForSelector('[data-focus="LU"]');
await p.click('[data-focus="LU"]'); await p.waitForSelector('#tt-mine');
await p.click('#tt-mine'); await p.waitForSelector('#qcard');
ids = (await sess()).parts[0].ids; A(ids.length === 5 && ids.every(id => Q.find(x => x.id === id).subject === 'LU'), 'câu bạn hay sai môn Luật chỉ gồm câu Luật');
// 3) Trả lời một câu rồi kết thúc: số liệu ẩn danh được gửi (chỉ mã câu và 0/1)
await p.click('.opt'); await p.click('#q-submit'); await p.waitForTimeout(500);
A(posts.length && posts.flatMap(x => x.a).every(([id, ok]) => /^[A-Z0-9]+-\d{3}$/.test(id) && (ok === 0 || ok === 1)), 'phải gửi số liệu dạng [mã, 0/1]');
// 4) Tắt góp số liệu: không gửi nữa
const before = posts.length;
await setState({ ...base, prefs: { ...base.prefs, share: false } }); await p.goto(url + "#on-luyen"); await p.reload(); await p.waitForSelector('#f-start');
await p.click('#f-start'); await p.waitForSelector('#qcard'); await p.click('.opt'); await p.click('#q-submit'); await p.waitForTimeout(500);
A(posts.length === before, 'đã tắt góp số liệu thì không được gửi');
// 5) Thi thử riêng môn Môi giới: 1 phần, 25 câu MG, 45 phút
await setState({ ...base, prefs: { ...base.prefs, type: 'MG', min: 45 } }); await p.goto(url + "#thi-thu"); await p.reload(); await p.waitForSelector('#e-min');
await p.click('#e-start'); await p.waitForSelector('#qcard');
let s = await sess();
A(s.parts.length === 1 && s.parts[0].ids.length === 25 && s.parts[0].ids.every(id => Q.find(x => x.id === id).subject === 'MG'), 'thi môn Môi giới: 25 câu MG');
A(Math.round((s.parts[0].endAt - s.parts[0].startAt) / 60e3) === 45, 'thời gian 45 phút');
await p.click('#q-submit'); await p.click('#modal-root .btn.primary');
await p.waitForFunction(() => /Kết quả thi thử/.test(document.querySelector('.page .eyebrow')?.textContent || ''));
const h1 = (await p.textContent('h1')).trim(); A(h1 === 'Đạt' || h1 === 'Chưa đạt', 'kết quả thi một môn: ' + h1);
// 6) Quay lại thi CCHN 2 phần vẫn bình thường
await setState({ ...base, prefs: { ...base.prefs, type: '' } }); await p.goto(url + "#thi-thu"); await p.reload(); await p.waitForSelector('#e-cert');
await p.click('#e-start'); await p.waitForSelector('#qcard'); s = await sess(); A(s.parts.length === 2, 'thi CCHN vẫn 2 phần');
// 7) Người mới thi riêng môn Môi giới 35 câu: chọn bằng nút trên trang; mỗi chủ đề góp số câu theo tỷ trọng (lệch tối đa 1 câu)
await setState({ ...base, q: {}, prefs: { ...base.prefs, type: '', n: 35 } }); await p.goto(url + "#thi-thu"); await p.reload(); await p.waitForSelector('[data-etype="MG"]');
await p.click('[data-etype="MG"]'); await p.waitForSelector('#e-min'); await p.click('#e-start'); await p.waitForSelector('#qcard');
s = await sess(); const got = {}, size = {};
for (const id of s.parts[0].ids) { const t = byIdT(id); got[t] = (got[t] || 0) + 1; }
for (const x of mg) size[x.topic] = (size[x.topic] || 0) + 1;
for (const t of Object.keys(size)) { const exp = 35 * size[t] / mg.length; A(Math.abs((got[t] || 0) - exp) <= 1, `chủ đề ${t}: ${got[t] || 0} câu, kỳ vọng ${exp.toFixed(1)}`); }
// 8) Bấm môn ở Tổng quan mở đúng trang Trọng tâm của môn đó
await p.goto(url + "#tong-quan"); await p.waitForSelector('[data-subj="LU"]'); await p.click('[data-subj="LU"]');
await p.waitForSelector('#tt-all'); A((await p.textContent('#tt-comm').catch(() => '')) !== null && /Pháp luật/.test(await p.textContent('.page')), 'bấm môn ở Tổng quan phải mở Trọng tâm môn đó');
A(await p.$('#tabbar a[href="#trong-tam"]'), 'thanh dưới phải có nút Trọng tâm');
A(!errs.length, 'lỗi trang: ' + errs.join(' | '));
await b.close(); console.log("TRONG TAM OK");
