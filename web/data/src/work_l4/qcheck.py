"""Kiểm tra trích dẫn giống tools/kiem_tra.py (bản bỏ đầu trang + bản gốc, so khớp khoảng trắng hoặc chỉ chữ-số)."""
import re, sys, unicodedata
from pathlib import Path
DOCS = Path("/home/user/cchn_moi/tai_lieu_phap_ly")
def norm_ws(s): return re.sub(r"\s+", " ", unicodedata.normalize("NFC", s)).strip()
def loose(s):
    s = unicodedata.normalize("NFC", s).lower()
    s = re.sub(r"(?<=[^\W\d_])\d{1,3}(?=\W|$)", "", s)
    return re.sub(r"[\W_]+", "", s)
_c = {}
def text(name):
    if name not in _c:
        p = next((d / name for d in [DOCS / "van_ban_txt", DOCS] if (d / name).exists()), None)
        raw = p.read_text(encoding="utf-8")
        clean = "\n".join(l for l in raw.splitlines() if not re.search(r"CÔNG BÁO/Số|^\s*\d{1,4}\s*$", l))
        t = norm_ws(clean) + " \x00 " + norm_ws(raw)
        _c[name] = (t, loose(t))
    return _c[name]
def ok(quote, src):
    t, lt = text(src)
    return norm_ws(quote) in t or loose(quote) in lt
if __name__ == "__main__":
    print(ok(sys.argv[1], sys.argv[2]))
