# Kiểm trích dẫn của cm_14 (kể cả câu CM, vì kiem_tra.py chỉ kiểm câu LUAT), cùng cách chuẩn hóa của kiem_tra.py
import json, re, unicodedata
from pathlib import Path
DOCS = Path('/home/user/cchn_moi/tai_lieu_phap_ly/van_ban_txt')
def norm_ws(s): return re.sub(r"\s+", " ", unicodedata.normalize("NFC", s)).strip()
def loose(s):
    s = unicodedata.normalize("NFC", s).lower()
    s = re.sub(r"(?<=[^\W\d_])\d{1,3}(?=\W|$)", "", s)
    return re.sub(r"[\W_]+", "", s)
qs = json.load(open('/home/user/cchn_moi/web/data/src/cm_14.json'))
bad = 0
for q in qs:
    if not q.get('quote'): print(q['id'], 'không có trích dẫn'); continue
    raw = (DOCS / q['src']).read_text(encoding='utf-8')
    clean = "\n".join(l for l in raw.splitlines() if not re.search(r"CÔNG BÁO/Số|^\s*\d{1,4}\s*$", l))
    t = norm_ws(clean) + " \x00 " + norm_ws(raw)
    ok = norm_ws(q['quote']) in t or loose(q['quote']) in loose(t)
    bad += not ok
    print(q['id'], 'OK' if ok else 'KHÔNG KHỚP', q['src'])
assert bad == 0, bad
