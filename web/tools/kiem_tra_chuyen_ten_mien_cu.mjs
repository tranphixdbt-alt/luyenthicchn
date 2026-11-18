// Giả lập tên miền cũ có tiến độ: phải tự chuyển sang tên miền mới, giữ tiến độ, ?src= và trang đang mở
import { createRequire } from "module"; import fs from "fs"; const { chromium } = createRequire(import.meta.url)("playwright");
const html = fs.readFileSync("/home/user/luyenthicchn/web/dist/index.html", "utf8");
const b = await chromium.launch(); const c = await b.newContext(); const errs = [];
for (const o of ["https://luyenthicchn-dist.vercel.app", "https://luyenthicchn.btinvest.vn"])
  await c.route(o + "/**", r => new URL(r.request().url()).pathname === "/" ? r.fulfill({ body: html, contentType: "text/html" }) : r.fulfill({ status: 204 }));
await c.addInitScript(() => { if (location.hostname.endsWith("vercel.app") && !localStorage.getItem("docchn_v1"))
  localStorage.setItem("docchn_v1", JSON.stringify({ v: 1, q: { "C1-014": { n: 2, ok: 1, box: 2, due: 1, lastOk: true } }, star: { "C1-014": 1 }, hist: [], prefs: { cert: "moi-gioi", n: 25 } })); });
const p = await c.newPage(); p.on("pageerror", e => errs.push(e.message));
await p.goto("https://luyenthicchn-dist.vercel.app/?src=facebook#thi-thu"); await p.waitForURL(/btinvest\.vn/); await p.waitForTimeout(800);
const r = await p.evaluate(() => ({ u: location.href, s: JSON.parse(localStorage.getItem("docchn_v1")) }));
if (!r.s.q["C1-014"] || !r.s.star["C1-014"]) throw new Error("mất tiến độ"); if (r.u !== "https://luyenthicchn.btinvest.vn/?src=facebook#thi-thu") throw new Error("sai địa chỉ: " + r.u);
if (errs.length) throw new Error(errs.join("|")); console.log("CHUYEN TU TRANG CU OK", r.u); await b.close();
