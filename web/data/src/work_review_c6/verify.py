"""Tính lại độc lập mọi câu có số của cm_6 (bản sau review). Chạy: python3 -I verify.py"""
import json
from pathlib import Path
d = {q['id']: q for q in json.loads(Path('/home/user/cchn_moi/web/data/src/cm_6.json').read_text(encoding='utf-8'))}
key = lambda i: d[i]['o'][d[i]['a']]
r = lambda x, n=2: f"{x:.{n}f}".replace('.', ',')
def thou(x): return f"{round(x):,}".replace(',', '.')

# C6-014 zero-coupon YTM
P, F, n = 79383, 100000, 3
ytm = (F / P) ** (1 / n) - 1
assert r(ytm * 100) in key('C6-014'), (ytm, key('C6-014'))
dis14 = {'lãi đơn/giá': (F - P) / n / P, 'lãi đơn/mệnh giá': (F - P) / n / F,
         'gần đúng giá bq': (F - P) / n / ((F + P) / 2), '1-(P/F)^(1/n)': 1 - (P / F) ** (1 / n)}
print('C6-014', r(ytm * 100), {k: r(v * 100) for k, v in dis14.items()})

# C6-015 cumulative preferred
pref = 2_000_000 * 10_000 * 0.09
assert abs(pref - 1.8e9) < 1
common = 15e9 - 3 * pref
assert r(common / 1e9, 1) in key('C6-015')
print('C6-015', common / 1e9, 'non-cum', (15e9 - pref) / 1e9, 'quên năm 2026', (15e9 - 2 * pref) / 1e9)

# C6-016 conversion parity
par, ratio, pb, ps = 100000, 5, 115000, 21000
assert thou(pb / ratio) in key('C6-016')
print('C6-016', pb / ratio, 'nominal', par / ratio, 'inverse', round(ps * par / pb), 'x1.15', ps * pb / par)

# C6-022 pro-rata allocation
rate = 6_000_000 / 9_600_000
assert thou(80_000 * rate) in key('C6-022')
print('C6-022', 80_000 * rate, 'refund', 80_000 * (1 - rate), 'excess-ratio', 80_000 * (9.6 - 6) / 6)

# C6-023 discriminatory auction
book = [('A', 600_000, 25_500), ('B', 800_000, 25_200), ('C', 900_000, 25_000), ('D', 500_000, 24_800)]
left, cash, last = 2_000_000, 0, None
for _, q, p in sorted(book, key=lambda b: -b[2]):
    take = min(q, left); cash += take * p; left -= take
    if take: last = p
    if not left: break
assert r(cash / 1e9) in key('C6-023')
print('C6-023', cash / 1e9, 'uniform', 2e6 * last / 1e9, 'start', 2e6 * 24_500 / 1e9, 'max', 2e6 * 25_500 / 1e9)

# C6-024 ownership after combined IPO
s = (40 - 7.5) / (50 + 12.5)
assert r(s * 100) in key('C6-024')
print('C6-024', r(s * 100), r(32.5 / 50 * 100), r(40 / 62.5 * 100), r(32.5 / 70 * 100))

# C6-030 free-float cap-weighted index
st = [(200e6, .3, 50000, 54000), (80e6, .5, 40000, 36800), (40e6, .9, 25000, 29000)]
ff = 100 * sum(n * f * p1 for n, f, p0, p1 in st) / sum(n * f * p0 for n, f, p0, p1 in st)
full = 100 * sum(n * p1 for n, f, p0, p1 in st) / sum(n * p0 for n, f, p0, p1 in st)
eq = 100 * sum(p1 / p0 for n, f, p0, p1 in st) / 3
pw = 100 * sum(p1 for *_, p1 in st) / sum(p0 for n, f, p0, p1 in st)
assert r(ff) in key('C6-030')
print('C6-030', r(ff), r(full), r(eq), r(pw))

# C6-031 divisor adjustment on addition
div0 = 2_400_000 / 1200; div1 = div0 * (2_400_000 + 120_000) / 2_400_000
idx = 2_583_000 / div1
assert r(idx).replace(',', ',') in key('C6-031').replace('.', '')
print('C6-031', div1, idx, 2_583_000 / div0, (2_583_000 - 126_000) / div0, (2_583_000 - 126_000) / div1)

# C6-032 price-weighted split
div = 3; z = 75 / 3; div2 = (30 + 45 + z) / ((30 + 45 + 75) / div)
v = (33 + 47 + 23) / div2
assert r(v) in key('C6-032')
print('C6-032', div2, r(v), r(103 / 3), r((33 + 47 + 69) / 3), r(50 * (33 / 30 + 47 / 45 + 23 / 25) / 3))

# C6-038 minimum charter capital
need = 25 + 50 + 165 + 10 - 40
assert f"{need} tỷ" in key('C6-038')
print('C6-038', need, 50 + 165 - 40 + 0, 25 + 50 + 165 - 40, 165)

# C6-039 investment limits
out, held, px, eq_ = 12_000_000, 500_000, 60_000, 1000e9
lim20 = 0.20 * out - held
lim15e = (0.15 * eq_ - held * px) / px
ans = min(lim20, lim15e)
assert thou(ans) in key('C6-039')
print('C6-039', lim20, lim15e, '15%CP', 0.15 * out - held, 'quên đang nắm', 0.20 * out, 0.15 * eq_ / px)

# C6-040 capital adequacy headroom
tr = 150 + 60 + 50; cap = 540 / 1.8
assert f"{cap - tr:.0f} tỷ" in key('C6-040')
print('C6-040', r(540 / tr * 100), cap - tr, 540 / 1.5 - tr, cap - 210, (540 / tr - 1.8) * tr)
print('ALL OK')
