"""Gộp dữ liệu + mã thành dist/ để đưa lên Vercel/GitHub Pages hoặc mở trực tiếp bằng trình duyệt (một file index.html, chạy offline)."""
import json, os, re, shutil, sys
from pathlib import Path

root = Path(__file__).resolve().parent.parent
dist = root / "dist"; dist.mkdir(exist_ok=True)
SITE = os.environ.get("SITE_URL", "https://luyenthicchn-dist.vercel.app").rstrip("/")   # dùng cho ảnh xem trước khi chia sẻ link
frag = (root / "index.html").read_text(encoding="utf-8")
app = (root / "app.js").read_text(encoding="utf-8")
head, body = frag.split("</style>", 1)
data = ""
for name in ["questions", "luat_ck", "so_lieu", "thay_doi", "van_ban"]:
    txt = json.dumps(json.loads((root / "data" / f"{name}.json").read_text(encoding="utf-8")), ensure_ascii=False, separators=(",", ":"))
    data += f'<script type="application/json" id="data-{name}">{txt.replace("</", "<\\/")}</script>\n'
confetti = (root / "vendor" / "confetti.browser.js").read_text(encoding="utf-8")
body = body.replace('<script src="vendor/confetti.browser.js" defer></script>', "<script>\n" + confetti.replace("</script", "<\\/script") + "\n</script>")
body = body.replace('<script src="app.js"></script>', data + "<script>\n" + app.replace("</script", "<\\/script") + "\n</script>")
assert body.count("<script>") == 2 and "src=" not in body.split("</nav>")[-1].split("<script")[1][:20], "không gộp được confetti/app.js vào index.html"
html = ('<!doctype html>\n<html lang="vi">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        '<meta name="theme-color" content="#0C2A63">\n<link rel="manifest" href="manifest.webmanifest">\n'
        '<link rel="icon" href="favicon-64.png" type="image/png">\n<link rel="apple-touch-icon" href="apple-touch-icon.png">\n'
        f'<meta property="og:type" content="website">\n<meta property="og:site_name" content="BT-INVEST">\n<meta property="og:title" content="BT-INVEST – Luyện thi chứng chỉ hành nghề chứng khoán 2026">\n'
        f'<meta property="og:description" content="{len(json.loads((root / "data" / "questions.json").read_text(encoding="utf-8")))} câu soát theo luật hiện hành, thi thử đúng cấu trúc từng chứng chỉ, ôn lặp lại, thư viện luật. Hotline/Zalo 0942 037 820.">\n'
        f'<link rel="canonical" href="{SITE}/">\n<meta name="google-site-verification" content="JHUVILS5gqxInnCNy_be3kgz15urfBSVhl7WADmpQ3U">\n<script type="application/ld+json">{{"@context":"https://schema.org","@type":"WebSite","name":"BT-INVEST – Luyện thi CCHN chứng khoán","url":"{SITE}/","inLanguage":"vi"}}</script>\n'
        f'<meta property="og:url" content="{SITE}/">\n<meta property="og:image" content="{SITE}/og.png">\n<meta property="og:image:width" content="1200">\n<meta property="og:image:height" content="630">\n<meta name="twitter:card" content="summary_large_image">\n'
        + head + "</style>\n</head>\n<body>\n" + body + "\n</body>\n</html>\n")
(dist / "index.html").write_text(html, encoding="utf-8")
for f in ["manifest.webmanifest", "sw.js"]:
    shutil.copy(root / "pwa" / f, dist / f)
for f in ["icon-192.png", "icon-512.png", "apple-touch-icon.png", "favicon-64.png", "og.png"]:
    shutil.copy(root / "brand" / "out" / f, dist / f)
(dist / "icon.svg").unlink(missing_ok=True)
shutil.copytree(root / "api", dist / "api", dirs_exist_ok=True)   # Vercel Function: thống kê chung ẩn danh
for f in ["package.json", "package-lock.json"]:   # thư viện redis cho hàm thống kê (Vercel tự cài)
    shutil.copy(root / f, dist / f)
print("dist/index.html", round(len(html.encode()) / 1024), "KB")

# ---- Trang tĩnh cho Google: mỗi môn một trang đề mẫu (Google không đọc được nội dung sau dấu # của ứng dụng) ----
from html import escape as E
from collections import defaultdict
from datetime import date
SUBJ = {"LU": ("mon-phap-luat", "Pháp luật về chứng khoán và thị trường chứng khoán"), "MG": ("mon-moi-gioi", "Môi giới và tư vấn đầu tư chứng khoán"),
        "CB": ("mon-co-ban", "Những vấn đề cơ bản về chứng khoán và thị trường chứng khoán"), "PT": ("mon-phan-tich-dau-tu", "Phân tích và đầu tư chứng khoán"),
        "BC": ("mon-phan-tich-bao-cao-tai-chinh", "Phân tích báo cáo tài chính doanh nghiệp"), "BL": ("mon-tu-van-tai-chinh-bao-lanh", "Tư vấn tài chính và bảo lãnh phát hành chứng khoán"),
        "QU": ("mon-quan-ly-quy", "Quản lý quỹ và tài sản"), "PS": ("mon-phai-sinh", "Chứng khoán phái sinh và thị trường chứng khoán phái sinh")}
QS = json.loads((root / "data" / "questions.json").read_text(encoding="utf-8"))
CSS = """:root{--bg:#F1F4F1;--sf:#fff;--ink:#13201A;--mu:#56645C;--ln:#D1D9D3;--ac:#17408F;--up:#0A8653}
@media (prefers-color-scheme:dark){:root{--bg:#0E1513;--sf:#151E1B;--ink:#E4EDE8;--mu:#9AABA2;--ln:#2B3833;--ac:#8FB0F5;--up:#3CCB8B}}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.6 "Be Vietnam Pro",system-ui,sans-serif}main{max-width:820px;margin:0 auto;padding:16px}
a{color:var(--ac)}.cta{display:inline-block;background:var(--ac);color:#fff;padding:10px 16px;border-radius:8px;text-decoration:none;font-weight:600;margin:4px 8px 4px 0}
.q{background:var(--sf);border:1px solid var(--ln);border-radius:10px;padding:14px 16px;margin:12px 0}.q p{white-space:pre-line;margin:0 0 8px}.q ol{margin:0;padding-left:22px}
details{margin-top:8px}summary{cursor:pointer;color:var(--ac);font-weight:600}.ok{color:var(--up);font-weight:600}.mu{color:var(--mu);font-size:14px}"""
def page(path, title, desc, body, ld):
    d = dist / path; d.mkdir(parents=True, exist_ok=True)
    (d / "index.html").write_text(f"""<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)}</title><meta name="description" content="{E(desc)}"><link rel="canonical" href="{SITE}/{path}/"><link rel="icon" href="/favicon-64.png">
<meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}"><meta property="og:image" content="{SITE}/og.png"><meta property="og:url" content="{SITE}/{path}/">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script><style>{CSS}</style></head><body><main>
<p class="mu"><a href="/">BT-INVEST</a> › <a href="/on-thi/">Đề mẫu theo môn</a></p>{body}
<p class="mu">BT-INVEST, trang luyện thi CCHN chứng khoán miễn phí. Hotline/Zalo 0942 037 820. Không phải trang chính thức của UBCKNN.</p></main></body></html>""", encoding="utf-8")
cta = '<p><a class="cta" href="/#thi-thu">Thi thử tính giờ miễn phí</a><a class="cta" href="/#on-luyen">Ôn luyện có giải thích</a></p>'
urls = ["", "on-thi"]
for k, (slug, name) in SUBJ.items():
    qs = [q for q in QS if q["subject"] == k]
    by = defaultdict(list)
    for q in sorted(qs, key=lambda q: q["id"]): by[q["topic"]].append(q)
    pick = []   # rải đều theo chủ đề: lần lượt mỗi chủ đề 1 câu cho tới 30 câu
    while len(pick) < min(30, len(qs)):
        for t in list(by):
            if by[t] and len(pick) < 30: pick.append(by[t].pop(0))
    items = "".join(f'<div class="q"><p><b>Câu {i}.</b> {E(q["q"])}</p><ol type="A">{"".join(f"<li>{E(o)}</li>" for o in q["o"])}</ol>'
                    f'<details><summary>Xem đáp án và giải thích</summary><p class="ok">Đáp án: {"ABCD"[q["a"]]}. {E(q["o"][q["a"]])}</p><p>{E(q["e"])}</p><p class="mu">Căn cứ: {E(q["basis"])}</p></details></div>'
                    for i, q in enumerate(pick, 1))
    topics = "".join(f"<li>{E(t)} ({sum(1 for q in qs if q['topic'] == t)} câu)</li>" for t in sorted({q["topic"] for q in qs}))
    title = f"Câu hỏi ôn thi CCHN môn {name} có đáp án ({date.today().year})"
    page(f"on-thi/{slug}", title, f"{len(qs)} câu hỏi ôn thi chứng chỉ môn {name}, có đáp án, giải thích và căn cứ pháp lý hiện hành. Xem 30 câu mẫu và thi thử miễn phí.",
         f"<h1>{E(title)}</h1><p>Ngân hàng có <b>{len(qs)} câu</b> môn {E(name)}, soát theo văn bản pháp luật hiện hành, mỗi câu có giải thích và căn cứ. "
         f"Dưới đây là 30 câu mẫu rải đều các chủ đề; làm đủ ngân hàng, thi thử tính giờ và ôn lại câu sai trên ứng dụng.</p>{cta}<h2>Các chủ đề</h2><ul>{topics}</ul><h2>30 câu hỏi mẫu</h2>{items}{cta}",
         {"@context": "https://schema.org", "@type": "LearningResource", "name": title, "inLanguage": "vi", "isAccessibleForFree": True, "educationalLevel": "Chứng chỉ hành nghề chứng khoán", "url": f"{SITE}/on-thi/{slug}/"})
    urls.append(f"on-thi/{slug}")
# Trang hỏi đáp về kỳ thi (dữ liệu FAQPage cho Google và các trợ lý AI trích dẫn)
FAQ = json.loads((root / "seo" / "hoi_dap.json").read_text(encoding="utf-8"))
page("hoi-dap-thi-cchn", "Hỏi đáp thi chứng chỉ hành nghề chứng khoán (CCHN) 2026: điều kiện, lệ phí, điểm đạt, lịch thi",
     "Giải đáp các câu hỏi thường gặp về thi sát hạch CCHN chứng khoán 2026: điều kiện cấp, môn phải học, cấu trúc đề, điểm đạt 60%, thi lại, lệ phí, lịch thi, theo văn bản hiện hành.",
     f"<h1>Hỏi đáp thi chứng chỉ hành nghề chứng khoán 2026</h1><p class='mu'>Cập nhật {date.today().strftime('%d/%m/%Y')} theo Luật Chứng khoán, Nghị định 155/2020 (sửa bởi Nghị định 245/2025), Thông tư 135/2025 và thông báo của Hội đồng thi sát hạch năm 2026.</p>"
     + "".join(f"<h2>{E(q)}</h2><p>{a}</p>" for q, a in FAQ) + cta,
     {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", a.replace("<br>", " "))}} for q, a in FAQ]})
urls.append("hoi-dap-thi-cchn")

def md(t):   # đủ cho ghi chú ôn tập: tiêu đề, đậm/nghiêng, gạch đầu dòng, bảng, đường kẻ, đoạn văn
    inline = lambda s: re.sub(r"\*(.+?)\*", r"<i>\1</i>", re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", E(s, quote=False)))
    out, lst, tbl = [], False, []
    def flush():
        nonlocal lst, tbl
        if lst: out.append("</ul>"); lst = False
        if tbl:
            rows = [[inline(c.strip()) for c in r.strip().strip("|").split("|")] for r in tbl if not re.fullmatch(r"[\s|:-]+", r)]
            out.append("<div style='overflow-x:auto'><table><tr>" + "".join(f"<th>{c}</th>" for c in rows[0]) + "</tr>" + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows[1:]) + "</table></div>"); tbl = []
    for l in t.splitlines():
        if l.startswith("|"): tbl.append(l); continue
        if not l.startswith("- "): flush()
        if m := re.match(r"(#{1,3}) (.*)", l): out.append(f"<h{len(m[1])}>{inline(m[2])}</h{len(m[1])}>")
        elif l.startswith("- "):
            if not lst: out.append("<ul>"); lst = True
            out.append(f"<li>{inline(l[2:])}</li>")
        elif l.strip() == "---": out.append("<hr>")
        elif l.strip(): out.append(f"<p>{inline(l)}</p>")
    flush(); return "\n".join(out)
CSS += "table{border-collapse:collapse;margin:8px 0;font-size:15px}th,td{border:1px solid var(--ln);padding:6px 8px;text-align:left;vertical-align:top}"
NOTES = [("20-cau-luat-de-sai", "20_cau_luat_de_ra_de_sai.md", "20 câu môn Pháp luật chứng khoán dễ ra và dễ sai nhất khi thi CCHN, có đáp án và giải thích"),
         ("moi-gioi-cum-cau-hoi", "moi_gioi_cum_cau_hoi.md", "Môn Môi giới chứng khoán: các cụm câu hỏi dễ nhớ khi ôn thi CCHN (nhân sự tối thiểu, ký quỹ, nhà đầu tư nước ngoài)")]
for slug, f, desc in NOTES:
    t = (root.parent / "on_nhanh" / f).read_text(encoding="utf-8")
    title = re.search(r"^# (.+)", t, re.M)[1]
    page(f"on-tap/{slug}", title + " | Ôn thi CCHN", desc, md(t).replace("Mã câu ở cuối mỗi câu để tìm lại trên trang", "Mã câu ở cuối mỗi câu để tìm lại trên <a href='/#ngan-hang'>Ngân hàng câu hỏi</a>") + cta,
         {"@context": "https://schema.org", "@type": "Article", "headline": title, "inLanguage": "vi", "dateModified": date.today().isoformat(), "author": {"@type": "Organization", "name": "BT-INVEST"}})
    urls.append(f"on-tap/{slug}")

page("on-thi", "Đề thi thử CCHN chứng khoán theo từng môn, có đáp án (2026)", f"{len(QS)} câu hỏi ôn thi chứng chỉ hành nghề chứng khoán chia theo 8 môn, có đáp án và giải thích theo luật hiện hành.",
     f"<h1>Đề mẫu ôn thi CCHN chứng khoán theo từng môn</h1><p>{len(QS)} câu hỏi có đáp án và giải thích, cập nhật theo luật hiện hành. Chọn môn để xem 30 câu mẫu:</p><ul>"
     + "".join(f'<li><a href="/on-thi/{s}/">Môn {E(n)}</a> ({sum(1 for q in QS if q["subject"] == k)} câu)</li>' for k, (s, n) in SUBJ.items()) + "</ul>"
     + "<h2>Tài liệu ôn nhanh</h2><ul><li><a href='/hoi-dap-thi-cchn/'>Hỏi đáp thi CCHN 2026: điều kiện, lệ phí, điểm đạt, lịch thi</a></li>"
     + "".join(f"<li><a href='/on-tap/{s}/'>{E(d)}</a></li>" for s, _, d in NOTES) + f"</ul>{cta}",
     {"@context": "https://schema.org", "@type": "WebSite", "name": "BT-INVEST – Luyện thi CCHN chứng khoán", "url": f"{SITE}/", "inLanguage": "vi"})
today = date.today().isoformat()
(dist / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + "".join(f"<url><loc>{SITE}/{u + '/' if u else ''}</loc><lastmod>{today}</lastmod></url>\n" for u in urls) + "</urlset>\n", encoding="utf-8")
(dist / "google08caf10d2d0d89c8.html").write_text("google-site-verification: google08caf10d2d0d89c8.html", encoding="utf-8")   # xác minh Google Search Console (tệp HTML)
AI_BOTS = ["GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-SearchBot", "PerplexityBot", "Google-Extended", "Applebot-Extended", "Bingbot"]
(dist / "robots.txt").write_text("".join(f"User-agent: {b}\n" for b in AI_BOTS) + "Allow: /\nDisallow: /api/\n\n" + f"User-agent: *\nAllow: /\nDisallow: /api/\n\nSitemap: {SITE}/sitemap.xml\n", encoding="utf-8")
(dist / "llms.txt").write_text(f"""# BT-INVEST – Luyện thi chứng chỉ hành nghề chứng khoán (CCHN) Việt Nam

> Trang luyện thi miễn phí, không cần tài khoản, cho kỳ thi sát hạch chứng chỉ hành nghề chứng khoán của Ủy ban Chứng khoán Nhà nước (môi giới, phân tích tài chính, quản lý quỹ) và các môn chứng chỉ chuyên môn của SRTC. {len(QS)} câu hỏi trắc nghiệm 8 môn, mỗi câu có đáp án, giải thích và căn cứ pháp lý theo văn bản hiện hành (cập nhật {date.today().strftime('%m/%Y')}).

Tính năng: thi thử tính giờ theo cấu trúc từng chứng chỉ (phần Pháp luật và phần Chuyên môn, đạt từ 60% mỗi phần), thi thử từng môn chuyên môn, ôn theo chủ đề, ôn lặp lại câu sai, thẻ ghi nhớ số liệu, máy tính công thức, thư viện văn bản luật. Không phải trang chính thức của UBCKNN.

## Trang chính
- [Ứng dụng luyện thi]({SITE}/): thi thử, ôn luyện, ngân hàng câu hỏi
- [Hỏi đáp thi CCHN 2026]({SITE}/hoi-dap-thi-cchn/): điều kiện cấp, môn phải học, cấu trúc đề, điểm đạt, thi lại, lệ phí, lịch thi
- [Đề mẫu theo môn]({SITE}/on-thi/): 30 câu mẫu có đáp án cho mỗi môn

## Đề mẫu từng môn
""" + "".join(f"- [Môn {n}]({SITE}/on-thi/{s}/)\n" for s, n in SUBJ.values()) + "\n## Ôn nhanh\n" + "".join(f"- [{d}]({SITE}/on-tap/{s}/)\n" for s, _, d in NOTES), encoding="utf-8")
assert all((dist / u / "index.html").exists() for u in urls if u), "thiếu trang tĩnh"
print("trang tĩnh:", len(urls) - 1, "+ sitemap.xml, robots.txt")
