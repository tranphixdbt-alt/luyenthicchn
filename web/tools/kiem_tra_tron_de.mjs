// Kiểm tra trộn đề qua giao diện: câu sai ~30% và cách đều, câu đúng chỉ dùng khi thiếu, đề thi đủ câu và rải chủ đề.
import { chromium } from "playwright-core";
const url = process.argv[2], DAY = 864e5;
const b = await chromium.launch({ executablePath: "/opt/pw-browsers/chromium-1194/chrome-linux/chrome" });
const p = await b.newPage({ viewport: { width: 1280, height: 900 } }); const errs = []; p.on("pageerror", e => errs.push(e.message));
p.on("dialog", d => d.accept());
const A = (c, m) => { if (!c) throw new Error(m); };
await p.goto(url + "#tong-quan");
const Q = await p.evaluate(() => JSON.parse(document.getElementById('data-questions').textContent));
const byId = new Map(Q.map(q => [q.id, q])), lu = Q.filter(q => q.subject === 'LU').map(q => q.id), t = Date.now();
const wrongIds = new Set(lu.slice(0, 40)), okIds = new Set(lu.slice(40, 140)), q = {};
[...wrongIds].forEach((id, k) => q[id] = { n: 1, ok: 0, box: 1, due: t - k * 1000, lastOk: false });
[...okIds].forEach(id => q[id] = { n: 1, ok: 1, box: 2, due: t + 3 * DAY, lastOk: true });
const setState = async st => { await p.evaluate(s => localStorage.setItem('docchn_v1', JSON.stringify(s)), st); };
const sess = async () => (await p.evaluate(() => JSON.parse(localStorage.getItem('docchn_v1')).sess));
const base = { v: 1, q, star: {}, hist: [], sess: null, last: null, theme: '', reports: [], cards: {}, prefs: { cert: 'moi-gioi', n: 35, mode: 'both' } };
const out = {};
// 1) Ôn luyện phần Luật 20 câu
await setState(base); await p.goto(url + "#on-luyen"); await p.reload(); await p.waitForSelector('#f-part');
await p.selectOption('#f-part', 'LUAT'); await p.selectOption('#f-n', '20');
out.count = await p.textContent('#f-count');
A(/40 đang sai · 100 đã đúng/.test(out.count), 'dòng đếm sai: ' + out.count);
await p.click('#f-start'); await p.waitForSelector('#qcard');
let a = (await sess()).parts[0].ids, wPos = a.map((id, i) => wrongIds.has(id) ? i : -1).filter(i => i >= 0);
A(a.length === 20 && new Set(a).size === 20, 'lượt 20 câu phải đủ và không trùng');
A(wPos.length === 6, 'cần 6 câu sai, có ' + wPos.length);
A(!a.some(id => okIds.has(id)), 'không được có câu đã đúng');
A(wPos.every((x, i) => i === 0 || x - wPos[i - 1] >= 2), 'câu sai phải cách nhau: ' + wPos);
out.practiceWrongAt = wPos.join(',');
// 2) Nguồn câu "làm sai lần gần nhất": toàn câu sai
await setState(base); await p.goto(url + "#on-luyen"); await p.reload(); await p.waitForSelector('#f-part');
await p.selectOption('#f-part', 'LUAT'); await p.selectOption('#f-pool', 'wrong'); await p.selectOption('#f-n', '20');
await p.click('#f-start'); await p.waitForSelector('#qcard');
a = (await sess()).parts[0].ids; A(a.length === 20 && a.every(id => wrongIds.has(id)), 'lọc câu sai phải ra toàn câu sai');
// 3) Thi thử: phần Luật 35 câu có 11 câu sai, không câu đúng, rải nhiều chủ đề; phần Chuyên môn đủ 35 câu
await setState(base); await p.goto(url + "#thi-thu"); await p.reload(); await p.waitForSelector('#e-start');
await p.click('#e-start'); await p.waitForSelector('#qcard');
const s = await sess(), law = s.parts[0].ids, spec = s.parts[1].ids;
A(law.length === 35 && new Set(law).size === 35, 'phần Luật đủ 35 câu');
A(law.filter(id => wrongIds.has(id)).length === 11, 'phần Luật cần 11 câu sai, có ' + law.filter(id => wrongIds.has(id)).length);
A(!law.some(id => okIds.has(id)), 'phần Luật không có câu đã đúng');
out.lawTopics = new Set(law.map(id => byId.get(id).topic)).size; A(out.lawTopics >= 15, 'phần Luật phải rải nhiều chủ đề');
A(spec.length === 35 && new Set(spec).size === 35, 'phần Chuyên môn đủ 35 câu');
out.spec = spec.reduce((m, id) => (m[byId.get(id).subject] = (m[byId.get(id).subject] || 0) + 1, m), {});
// 4) Chủ đề nhỏ đã làm đúng gần hết: thiếu câu thì mới lấy câu đúng
const topic = Q.find(x => x.subject === 'LU' && Q.filter(y => y.topic === x.topic).length >= 12).topic;
const tIds = Q.filter(x => x.topic === topic).map(x => x.id), q4 = {};
tIds.forEach((id, k) => q4[id] = k < 2 ? { n: 1, ok: 0, box: 1, due: t, lastOk: false } : { n: 1, ok: 1, box: 3, due: t + 7 * DAY - k, lastOk: true });
await setState({ ...base, q: q4 }); await p.goto(url + "#on-luyen"); await p.reload(); await p.waitForSelector('#f-part');
await p.selectOption('#f-part', 'LUAT'); await p.selectOption('#f-topic', topic); await p.selectOption('#f-n', '10');
await p.click('#f-start'); await p.waitForSelector('#qcard');
a = (await sess()).parts[0].ids; A(a.length === 10 && a.filter(id => !q4[id].lastOk).length === 2, 'chủ đề nhỏ: 2 câu sai + 8 câu đúng bù vào');
// 5) Người mới: vẫn ra đề bình thường
await setState({ ...base, q: {} }); await p.goto(url + "#thi-thu"); await p.reload(); await p.waitForSelector('#e-start');
await p.click('#e-start'); await p.waitForSelector('#qcard');
A((await sess()).parts.every(x => x.ids.length === 35), 'người mới vẫn ra đủ đề');
A(!errs.length, 'lỗi trang: ' + errs.join(' | '));
console.log(JSON.stringify(out));
await b.close(); console.log("SMART OK");
