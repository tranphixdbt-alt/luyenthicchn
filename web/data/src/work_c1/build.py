"""Build + validate cm_1.json (CB 40, MG 40). Run: python3 -I build.py"""
import datetime as dt, json, os, random, re, sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from questions import CB, MG  # noqa: E402

OUT = os.path.join(HERE, "..", "cm_1.json")
TXT = "/home/user/cchn_moi/tai_lieu_phap_ly/van_ban_txt"


def f(n):  # 1234567 -> "1.234.567"
    return f"{round(n):,}".replace(",", ".")


# ---------- recompute every calculation; returns the expected correct option ----------
def ato():
    ref = 25000
    buy_ato, sell_ato = 2000, 1000
    buys = {25200: 3000, 25100: 3000, 25000: 3000, 24900: 3000, 24800: 1000}
    sells = {24800: 1000, 24900: 1000, 25000: 1000, 25100: 1000, 25200: 2000}
    rows = []
    for p in sorted(buys):
        cb = buy_ato + sum(q for pr, q in buys.items() if pr >= p)
        cs = sell_ato + sum(q for pr, q in sells.items() if pr <= p)
        rows.append((p, min(cb, cs)))
    mx = max(v for _, v in rows)
    cands = [p for p, v in rows if v == mx]
    best = min(abs(p - ref) for p in cands)
    p = max(c for c in cands if abs(c - ref) == best)
    return f"{f(p)} đồng; {f(mx)} cổ phiếu"


def cont():
    book = [("C", 25050, 1000, 3), ("A", 25000, 2000, 1), ("B", 25000, 5000, 2)]  # (name, price, qty, time order)
    book.sort(key=lambda x: (-x[1], x[3]))
    left, fills = 2500, []
    for n, p, q, _ in book:
        if left == 0 or p < 25000:
            break
        m = min(q, left); left -= m; fills.append((n, m, p))
    assert fills == [("C", 1000, 25050), ("A", 1500, 25000)]
    return "C khớp 1.000 cổ phiếu giá 25.050 đồng; A khớp 1.500 cổ phiếu giá 25.000 đồng"


def band():
    ref, tick = 25350, 50
    ceil_ = ref * 107 // (100 * tick) * tick          # exact integer math, round down
    floor_ = -(-(ref * 93) // (100 * tick)) * tick     # round up
    return f"{f(ceil_)} đồng và {f(floor_)} đồng"


def exdate():
    rec = dt.date(2026, 11, 12)
    assert rec.weekday() == 3  # Thursday
    ex = rec - dt.timedelta(days=1)  # previous working day (Wed, no holiday)
    assert ex.weekday() == 2
    return f"Thứ Tư, ngày {ex:%d/%m/%Y}"


def fsdeadline():
    d10 = dt.date(2026, 3, 25) + dt.timedelta(days=10)
    d90 = dt.date(2025, 12, 31) + dt.timedelta(days=90)
    assert d10 == dt.date(2026, 4, 4) and d90 == dt.date(2026, 3, 31)
    d = min(d10, d90)
    return f"{d.day}/{d.month}/{d.year}"


def major():
    before, after = 2_300_000 / 50_000_000, 2_600_000 / 50_000_000
    assert before < 0.05 <= after and abs(after - before - 0.006) < 1e-12
    return "Công bố thông tin về việc trở thành cổ đông lớn trong 05 ngày làm việc kể từ ngày hoàn tất giao dịch"


def score():
    s = sum([4, 3, 5, 2, 4, 3]); assert 15 <= s <= 22
    return f"Cân bằng ({s} điểm): kết hợp cổ phiếu và tài sản thu nhập cố định tương đối cân đối"


def pe():
    pe_ = 36000 / 2400; v = 2400 * 12; assert pe_ == 15 and v < 36000
    return f"P/E của Z là {pe_:.0f} lần; giá trị ước tính theo P/E ngành là {f(v)} đồng, thấp hơn thị giá"


def leads():
    fee = 1e9 * 0.0015; act = 60e6 / fee; return f"{act / 0.2:.0f} khách hàng"


def roundtrip():
    buy = 3000 * 24800; sell = 3000 * 27300
    net = sell - sell * 0.0015 - sell * 0.001 - buy - buy * 0.0015
    return f"{f(net)} đồng"


def margin():
    loan = 0.5 * 10000 * 40000; p = loan / (0.7 * 10000)
    return f"{f(p)} đồng"


def bondpv():
    p = 8000 / 1.1 + 108000 / 1.1 ** 2
    return f"{f(p)} đồng"


def nav():
    return f"{f((8.6 + 120 + 25 + 0.4 - 3 - 1) * 1e9 / 10_000_000)} đồng"


def fundlimit():
    cap = 0.2 * 650 - 2_000_000 * 30000 / 1e9
    by_outstanding = (0.1 * 50_000_000 - 2_000_000) * 30000 / 1e9
    return f"{min(cap, by_outstanding):.0f} tỷ đồng"


CALC = {
    "conv": lambda: f"{f(100000 / 25000 * 28500)} đồng",
    "cw": lambda: f"{f((36500 - 30000) * 10000 / 5)} đồng",
    "firm": lambda: f"{f((5_000_000 - 4_200_000) * 18000)} đồng",
    "cont": cont, "ato": ato, "band": band,
    "uwlimit": lambda: f"{f(min(800, 15 * (1250 - 1200)))} tỷ đồng",
    "nav": nav, "fundlimit": fundlimit, "exdate": exdate,
    "net": lambda: f"Phải trả {12 - 9.5:.1f}".replace(".", ",") + " tỷ đồng",
    "fsdeadline": fsdeadline, "major": major, "score": score, "pe": pe, "leads": leads,
    "roundtrip": roundtrip,
    "adjdiv": lambda: f"{f((39000 - 1500) / (1 + 1 / 5))} đồng",
    "adjrights": lambda: f"{f((28000 + 0.5 * 10000) / 1.5)} đồng",
    "margin": margin,
    "dirty": lambda: f"{f((98500 + 100000 * 0.06 * 146 / 365) * 10000)} đồng",
    "repo": lambda: f"{f(10e9 * (1 + 0.0438 * 14 / 365))} đồng",
    "bondpv": bondpv,
}

# distractor sanity: the wrong numeric options really are the "common errors" they claim to be
assert f(100000 / 28500 * 25000) == "87.719" and f(36500 - 30000) and f(6500 * 10000) == "65.000.000"
assert f(8000 / 1.06 + 108000 / 1.06 ** 2) == "103.667"
assert f(10e9 * (1 + 0.0438 * 14 / 360)) == "10.017.033.333"
assert f(3000 * 27300 - 3000 * 24800 - 3000 * 24800 * 0.0015 - 3000 * 27300 * 0.0015) == "7.265.550"
assert f(39000 / 1.2 - 1500) == "31.000" and f(28000 / 1.5) == "18.667"

BANNED = re.compile(r"tất cả|cả hai|cả ba|không phương án|các phương án|phương án trên|đáp án|"
                    r"\b[A-D] và [A-D]\b|\b[A-D], [A-D]\b|\bcâu trên\b", re.I)
LETTER_REF = re.compile(r"(phương án|đáp án)\s+[A-D]\b", re.I)


def main():
    items = CB + MG
    assert len(CB) == 40 and len(MG) == 40
    rng = random.Random(20261104)
    targets = []
    for _ in range(2):  # balance per subject: 10 of each index in CB and in MG
        t = [i % 4 for i in range(40)]
        rng.shuffle(t)
        targets += t
    out, seen = [], set()
    for k, (it, tgt) in enumerate(zip(items, targets), 1):
        o = list(it["o"])
        assert len(o) == 4 and len(set(o)) == 4 and all(x.strip() for x in o), it["q"]
        for x in o:
            assert not BANNED.search(x), ("banned option text", x)
        assert not LETTER_REF.search(it["e"]), it["e"]
        if it["calc"]:
            exp = CALC[it["calc"]]()
            assert exp == o[0], (it["calc"], exp, o[0])
        lens = [len(x) for x in o]
        if max(lens) > 2.6 * min(lens):
            print("WARN length spread", k, lens)
        key = re.sub(r"\W+", " ", it["q"].lower()).strip()
        assert key not in seen, it["q"]; seen.add(key)
        if re.search(r"\b(không|ngoại trừ)\b", it["q"]) and "KHÔNG" not in it["q"] and "NGOẠI TRỪ" not in it["q"]:
            print("CHECK negation casing", k, it["q"][:80])
        correct = o[0]
        rest = o[1:]
        rest.insert(tgt, correct)
        assert rest.index(correct) == tgt
        out.append({
            "id": f"C1-{k:03d}", "part": "CM", "subject": it["subject"], "topic": it["topic"],
            "level": it["level"], "q": it["q"], "o": rest, "a": tgt, "e": it["e"],
            "basis": it["basis"], "quote": "", "src": it["src"], "as_of": "2026-11",
        })
    # schema + src checks
    keys = ["id", "part", "subject", "topic", "level", "q", "o", "a", "e", "basis", "quote", "src", "as_of"]
    for r in out:
        assert list(r) == keys and r["a"] in range(4) and r["level"] in (1, 2, 3)
        assert r["subject"] in ("CB", "MG") and r["part"] == "CM"
        assert r["src"] == "Giáo trình SRTC (khung chương trình)" or os.path.exists(os.path.join(TXT, r["src"])), r["src"]
    json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("written", os.path.normpath(OUT), len(out))
    print("subject", Counter(r["subject"] for r in out))
    for s in ("CB", "MG"):
        print(s, "levels", sorted(Counter(r["level"] for r in out if r["subject"] == s).items()))
        for t, c in Counter(r["topic"] for r in out if r["subject"] == s).items():
            print("  ", c, t)
    print("levels all", sorted(Counter(r["level"] for r in out).items()))
    print("answers", sorted(Counter(r["a"] for r in out).items()))
    print("calc items", sum(1 for it in items if it["calc"]))


if __name__ == "__main__":
    main()
