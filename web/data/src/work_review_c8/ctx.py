"""In ngữ cảnh quanh trích dẫn của các câu Luật trong cm_8: python3 -I ctx.py [id...]"""
import json, sys, re, unicodedata
from pathlib import Path
SRC = Path(__file__).resolve().parent.parent
DOCS = SRC.parent.parent.parent / "tai_lieu_phap_ly" / "van_ban_txt"
def n(s): return re.sub(r"\s+", " ", unicodedata.normalize("NFC", s))
for q in json.loads((SRC / "cm_8.json").read_text()):
    if q["part"] != "LUAT" or (sys.argv[1:] and q["id"] not in sys.argv[1:]): continue
    t = n((DOCS / q["src"]).read_text())
    k = t.find(n(q["quote"])[:60])
    print("=====", q["id"], q["src"], "pos", k)
    print(t[max(0, k - 900): k + len(q["quote"]) + 500] if k >= 0 else "NOT FOUND")
