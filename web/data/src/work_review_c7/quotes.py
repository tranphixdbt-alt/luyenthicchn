"""Kiểm tra quote cm_7 nguyên văn trong src và in ngữ cảnh (Điều gần nhất) để đối chiếu basis.
Chạy: python3 -I quotes.py [id ...]"""
import json, re, sys, unicodedata
from pathlib import Path
DOCS = Path('/home/user/cchn_moi/tai_lieu_phap_ly')
def nws(s): return re.sub(r"\s+", " ", unicodedata.normalize("NFC", s)).strip()
d = json.loads(Path('/home/user/cchn_moi/web/data/src/cm_7.json').read_text(encoding='utf-8'))
want = set(sys.argv[1:])
for q in d:
    if want and q['id'] not in want: continue
    if not q.get('quote'):
        print(q['id'], 'NO QUOTE'); continue
    p = next((x / q['src'] for x in [DOCS / 'van_ban_txt', DOCS] if (x / q['src']).exists()), None)
    raw = p.read_text(encoding='utf-8') if p else ''
    clean = "\n".join(l for l in raw.splitlines() if not re.search(r"CÔNG BÁO/Số|^\s*\d{1,4}\s*$", l))
    t = nws(clean); k = t.find(nws(q['quote']))
    if k < 0:
        print(q['id'], 'MISMATCH'); continue
    heads = [m for m in re.finditer(r"Điều \d+[a-z]?\. [^.]{0,80}", t[:k])]
    print(q['id'], 'OK |', heads[-1].group(0)[:90] if heads else '?', '| count', t.count(nws(q['quote'])))
    if want: print('   ...', t[max(0, k - 700):k + len(q['quote']) + 300], '\n')
