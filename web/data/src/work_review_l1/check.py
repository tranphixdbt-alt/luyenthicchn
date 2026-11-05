# Validate luat_1.json + thay_doi.json after review. Usage: python3 -I check.py
import json, re, pathlib, datetime
from collections import Counter

SRC = pathlib.Path(__file__).resolve().parent.parent
DOCS = SRC.parents[2] / "tai_lieu_phap_ly"
KEYS = ["id", "part", "subject", "topic", "level", "q", "o", "a", "e", "basis", "quote", "src", "as_of"]
BAD_OPT = re.compile(r"tất cả (các )?(phương án|đáp án)|các phương án trên|không phương án nào|"
                     r"(phương án|đáp án) [A-D]\b|\b[A-D] và [A-D]\b|cả [A-D] và", re.I)
norm = lambda s: " ".join(s.split())
_txt = {}


def src_text(name):
    if name not in _txt:
        p = next(d / name for d in (DOCS / "van_ban_txt", DOCS) if (d / name).is_file())
        _txt[name] = norm(p.read_text(encoding="utf-8"))
    return _txt[name]


errs, warns = [], []
data = json.loads((SRC / "luat_1.json").read_text(encoding="utf-8"))
ids = Counter(x.get("id") for x in data)
errs += [f"duplicate id {i}" for i, n in ids.items() if n > 1]
for it in data:
    t = it.get("id")
    if list(it) != KEYS:
        errs.append(f"{t}: keys {list(it)}"); continue
    if (it["part"], it["subject"], it["as_of"]) != ("LUAT", "LU", "2026-11") or it["level"] not in (1, 2, 3):
        errs.append(f"{t}: part/subject/as_of/level")
    o = it["o"]
    if not (len(o) == 4 and all(isinstance(x, str) and x.strip() for x in o)) or len({norm(x).lower() for x in o}) != 4:
        errs.append(f"{t}: need 4 distinct non-empty options")
    if type(it["a"]) is not int or not 0 <= it["a"] <= 3:
        errs.append(f"{t}: a out of range")
    errs += [f"{t}: option refers to other options: {x}" for x in o if BAD_OPT.search(x)]
    qt = norm(it["quote"])
    if not qt or len(qt) > 300:
        errs.append(f"{t}: quote length {len(qt)}")
    elif qt not in src_text(it["src"]):
        errs.append(f"{t}: quote not verbatim in {it['src']}")
    L = [len(x) for x in o]
    others = [l for i, l in enumerate(L) if i != it["a"]]
    if L[it["a"]] > 1.3 * max(others) or L[it["a"]] < 0.7 * min(others):
        warns.append(f"{t}: key length {L[it['a']]} vs others {others}")

td = json.loads((SRC / "thay_doi.json").read_text(encoding="utf-8"))
if not 12 <= len(td) <= 17:
    errs.append(f"thay_doi: {len(td)} items")
for i, x in enumerate(td):
    if list(x) != ["title", "what", "doc", "effective"] or not all(isinstance(v, str) and v.strip() for v in x.values()):
        errs.append(f"thay_doi[{i}]: keys/empty")
    try:
        assert re.fullmatch(r"\d\d/\d\d/\d{4}", x["effective"])
        datetime.datetime.strptime(x["effective"], "%d/%m/%Y")
    except (AssertionError, ValueError, KeyError):
        errs.append(f"thay_doi[{i}]: effective not dd/mm/yyyy: {x.get('effective')}")

print(f"luat_1: {len(data)} questions, keys {dict(sorted(Counter('ABCD'[x['a']] for x in data).items()))}; thay_doi: {len(td)} items")
print("\n".join("WARN " + w for w in warns))
print("\n".join("ERR " + e for e in errs) or "ALL CHECKS PASSED")
raise SystemExit(1 if errs else 0)
