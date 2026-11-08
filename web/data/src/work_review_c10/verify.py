"""Independent recomputation of every number in cm_10/cm_11 and checks of keys, distractors and quotes."""
import json, re, unicodedata
from pathlib import Path

SRC = Path(__file__).resolve().parent.parent
DOCS = SRC.parent.parent.parent / "tai_lieu_phap_ly" / "van_ban_txt"
qs = {q["id"]: q for f in ("cm_10.json", "cm_11.json") for q in json.loads((SRC / f).read_text(encoding="utf-8"))}
assert len(qs) == 20, len(qs)

def vn(x):  # Vietnamese integer format
    return f"{round(x):,}".replace(",", ".")

def opts(i):
    return qs[i]["o"], qs[i]["o"][qs[i]["a"]]

# C11-007: margin account equity on day 3, valuation at previous day's close
n, price, own = 2000, 30_000, 42_000_000
debt = n * price - own
assert debt == 18_000_000
close = {1: 31_500, 2: 29_000, 3: 27_500}
key = n * close[2] - debt                       # day 3 uses day-2 close
d_same_day = n * close[3] - debt                # used day-3 close
d_day1 = n * close[1] - debt                    # used day-1 close (= day-2 value)
d_buy = n * price - debt                        # used purchase price
assert (key, d_same_day, d_day1, d_buy) == (40_000_000, 37_000_000, 45_000_000, 42_000_000)
o, k = opts("C11-007")
assert k == vn(key) + " đồng", k
assert sorted(o) == sorted(vn(x) + " đồng" for x in (key, d_same_day, d_day1, d_buy)), o

# C11-008: salary cost of one prospecting call
salary_m, days, calls = 6_300_000, 252, 120
key = salary_m * 12 / (days * calls)
assert key == 2500
d365 = salary_m * 12 / (365 * calls)
d_month = salary_m / (days * calls)
d_day = salary_m * 12 / days
o, k = opts("C11-008")
assert k == vn(key) + " đồng"
assert sorted(o) == sorted(vn(x) + " đồng" for x in (key, d365, d_month, d_day)), (o, d365, d_month, d_day)

# C11-003 e: 50% margin, price -60% -> loss 120% of equity
buy, eq = 100, 50
loss = eq - (buy * 0.4 - (buy - eq))
assert abs(loss / eq - 1.2) < 1e-12
assert "120% vốn tự có" in qs["C11-003"]["e"]

# C10-009 e: 20 round trips x 0.4% = 8%
assert abs(20 * 0.004 - 0.08) < 1e-12 and "= 8% vốn" in qs["C10-009"]["e"]

# Key rank among numeric options (want variety)
for i in ("C11-007", "C11-008"):
    o, k = opts(i)
    vals = sorted(int(re.sub(r"\D", "", x)) for x in o)
    print(i, "key rank (1 = smallest):", vals.index(int(re.sub(r"\D", "", k))) + 1)

# Quotes must be verbatim in src (whitespace-normalised)
norm = lambda s: re.sub(r"\s+", " ", unicodedata.normalize("NFC", s)).strip()
def strip_footnotes(t):  # drop page headers / bare page numbers and footnote markers like "2. 7 Công ty"
    t = "\n".join(l for l in t.splitlines() if not re.search(r"CÔNG BÁO/Số|^\s*\d{1,4}\s*$", l))
    return norm(t)
for i, q in qs.items():
    if q["quote"]:
        text = strip_footnotes((DOCS / q["src"]).read_text(encoding="utf-8"))
        assert norm(q["quote"]) in text, i
    if q["part"] == "LUAT":
        assert q["quote"] and q["subject"] == "LU", i

# Legal keys: key option wording must match the quoted rule
assert "tổ chức kinh doanh chứng khoán nước ngoài đại diện có yêu cầu" in opts("C10-012")[1]
assert "08/2026" in qs["C10-012"]["basis"]
k = opts("C11-004")[1]
for part in ("Tỷ lệ ký quỹ", "lãi suất vay", "thời hạn vay", "gọi ký quỹ bổ sung", "danh mục chứng khoán ký quỹ"):
    assert part in k, part
for j, x in enumerate(qs["C11-004"]["o"]):
    if j != qs["C11-004"]["a"]:
        assert re.search(r"cam kết|danh sách khách hàng", x), x   # each distractor carries an item not in khoản 3 Điều 123
k = opts("C10-002")[1]
assert k.startswith("Công cụ tài chính dạng hợp đồng") and "tài sản cơ sở" in k

# Style: negative stems in caps, no option referring to others, no letter names in e
for i, q in qs.items():
    assert not re.search(r"\b(không|ngoại trừ)\b", q["q"]), (i, "negative word not in caps")
    for x in q["o"]:
        assert not re.search(r"tất cả (các )?(phương án|đáp án)|cả (hai|ba) (phương án|đáp án|ý)|không có phương án|\b[A-D] và [A-D]\b", x, re.I), (i, x)
    assert not re.search(r"(phương án|đáp án|chọn|câu)\s+[A-D]\b", q["e"]), i
    L = [len(x) for x in q["o"]]
    assert max(L) / min(L) <= 1.25 or q["id"] == "C11-008", (i, L)
print("verify OK")
