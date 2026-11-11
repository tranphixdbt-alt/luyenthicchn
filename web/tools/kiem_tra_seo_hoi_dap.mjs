// Trang hỏi đáp, trang ôn nhanh, llms.txt, robots.txt. Chạy: node kiem_tra_seo_hoi_dap.mjs <URL>
import { chromium } from "playwright-core";
const url = process.argv[2];
const b = await chromium.launch({ executablePath: "/opt/pw-browsers/chromium-1194/chrome-linux/chrome" });
const p = await b.newPage({ viewport: { width: 390, height: 900 } }); const errs = []; p.on("pageerror", e => errs.push(e.message));
for (const u of ["hoi-dap-thi-cchn/", "on-tap/20-cau-luat-de-sai/", "on-tap/moi-gioi-cum-cau-hoi/"]) {
  const r = await p.goto(url + u); if (r.status() !== 200) throw new Error(u + " " + r.status());
  const w = await p.evaluate(() => document.documentElement.scrollWidth); if (w > 390) throw new Error(u + " tràn ngang " + w);
  await p.screenshot({ path: u.replace(/\W+/g, "_") + ".png" });
}
for (const f of ["llms.txt", "robots.txt"]) { const r = await p.goto(url + f); if (r.status() !== 200) throw new Error(f); }
if (errs.length) throw new Error(errs.join("|")); console.log("SEO2 OK"); await b.close();
