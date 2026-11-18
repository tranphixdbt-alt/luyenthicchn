// Trang mới nhận tiến độ từ trang cũ (đúng nguồn, không ghi đè). Chạy: node kiem_tra_chuyen_ten_mien.mjs (cần máy chủ thử dist ở cổng 8790)
import { createRequire } from "module"; const { chromium } = createRequire(import.meta.url)("playwright");
const url = "http://localhost:8790/", OLD = "https://luyenthicchn-dist.vercel.app/";
const b = await chromium.launch(); const A = (c, m) => { if (!c) throw new Error(m); };
const pack = s => "#chuyen=" + encodeURIComponent(JSON.stringify(s));
const st = { S: { v: 1, q: { "L1-001": { n: 1, ok: 1, box: 1, due: 1, lastOk: true } }, star: {}, hist: [], prefs: { cert: "phan-tich", n: 50 } }, AUTH: null, vid: "vid-cu", r: "#on-luyen" };
const run = async (hash, referer, pre) => {
  const c = await b.newContext(); const p = await c.newPage(); const errs = []; p.on("pageerror", e => errs.push(e.message));
  if (pre) { await p.goto(url + "#tong-quan"); await p.evaluate(s => localStorage.setItem("docchn_v1", JSON.stringify(s)), pre); }
  await p.goto(url + hash, { referer }); await p.waitForTimeout(800);
  const r = await p.evaluate(() => ({ s: JSON.parse(localStorage.getItem("docchn_v1") || "null"), vid: localStorage.getItem("btinvest_vid"), hash: location.hash }));
  A(!errs.length, errs.join("|")); await c.close(); return r;
};
let r = await run(pack(st), OLD);
A(r.s && r.s.q["L1-001"] && r.s.prefs.cert === "phan-tich", "phải nhận tiến độ từ trang cũ"); A(r.vid === "vid-cu", "giữ mã người truy cập"); A(r.hash === "#on-luyen", "về đúng trang: " + r.hash);
r = await run(pack(st), "https://ke-gian.example/");
A(!r.s || !r.s.q || !r.s.q["L1-001"], "không nhận khi không đến từ trang cũ"); A(!r.hash.includes("chuyen"), "xóa dữ liệu khỏi địa chỉ");
r = await run(pack(st), OLD, { v: 1, q: { "L2-002": { n: 1, ok: 0, box: 1, due: 1, lastOk: false } }, star: {}, hist: [], prefs: {} });
A(r.s.q["L2-002"] && !r.s.q["L1-001"], "không ghi đè tiến độ đã có");
await b.close(); console.log("CHUYEN TEN MIEN OK");
