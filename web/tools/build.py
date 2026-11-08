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
