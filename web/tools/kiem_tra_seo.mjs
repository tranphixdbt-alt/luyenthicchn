// Trang tĩnh cho Google: đề mẫu từng môn, mục lục, link vào ứng dụng. Chạy: node kiem_tra_seo.mjs <URL>
import { chromium } from "playwright-core";
const url = process.argv[2];
const b = await chromium.launch({ executablePath: "/opt/pw-browsers/chromium-1194/chrome-linux/chrome" });
const p = await b.newPage({ viewport: { width: 390, height: 900 } }); const errs = []; p.on("pageerror", e => errs.push(e.message));
await p.goto(url + "on-thi/mon-moi-gioi/"); await p.click("details summary");
const w = await p.evaluate(() => document.documentElement.scrollWidth); if (w > 390) throw new Error("tràn ngang " + w);
await p.screenshot({ path: "seo_mg.png" });
await p.goto(url + "on-thi/"); const n = await p.$$eval("main li a", a => a.length); if (n !== 11) throw new Error("trang mục lục cần 11 link, có " + n);
await p.click("text=Thi thử tính giờ miễn phí"); await p.waitForSelector("#e-start");
if (errs.length) throw new Error(errs.join("|")); console.log("SEO OK"); await b.close();
