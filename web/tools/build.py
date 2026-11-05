"""Gộp dữ liệu + mã thành dist/ để đưa lên Vercel/GitHub Pages hoặc mở trực tiếp bằng trình duyệt (một file index.html, chạy offline)."""
import json, re, shutil, sys
from pathlib import Path

root = Path(__file__).resolve().parent.parent
dist = root / "dist"; dist.mkdir(exist_ok=True)
frag = (root / "index.html").read_text(encoding="utf-8")
app = (root / "app.js").read_text(encoding="utf-8")
head, body = frag.split("</style>", 1)
data = ""
for name in ["questions", "luat_ck", "so_lieu", "thay_doi", "van_ban"]:
    txt = json.dumps(json.loads((root / "data" / f"{name}.json").read_text(encoding="utf-8")), ensure_ascii=False, separators=(",", ":"))
    data += f'<script type="application/json" id="data-{name}">{txt.replace("</", "<\\/")}</script>\n'
body = body.replace('<script src="app.js"></script>', data + "<script>\n" + app.replace("</script", "<\\/script") + "\n</script>")
assert "<script>" in body, "không tìm thấy thẻ script app.js trong index.html"
html = ('<!doctype html>\n<html lang="vi">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        '<meta name="theme-color" content="#1D4E92">\n<link rel="manifest" href="manifest.webmanifest">\n<link rel="icon" href="icon.svg" type="image/svg+xml">\n'
        + head + "</style>\n</head>\n<body>\n" + body + "\n</body>\n</html>\n")
(dist / "index.html").write_text(html, encoding="utf-8")
for f in ["manifest.webmanifest", "sw.js", "icon.svg"]:
    shutil.copy(root / "pwa" / f, dist / f)
print("dist/index.html", round(len(html.encode()) / 1024), "KB")
