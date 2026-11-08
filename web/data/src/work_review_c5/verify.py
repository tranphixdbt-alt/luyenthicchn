# Independent recomputation of every numeric item in cm_5.json (second pass).
from decimal import Decimal as D, ROUND_HALF_UP, ROUND_FLOOR, ROUND_CEILING
import math
from datetime import date

def floor_tick(x, t): return math.floor(x / t) * t
def ceil_tick(x, t): return math.ceil(x / t - 1e-12) * t
out = {}

# C5-014 ex-dividend ceiling
ref = 38500 - 2000
out['014'] = dict(key=floor_tick(ref * 1.07, 50), up=ceil_tick(ref * 1.07, 50),
                  noadj=floor_tick(38500 * 1.07, 50), late=floor_tick(38500 * 1.07 - 2000, 50))

# Periodic auction helper: returns {price: matched}, matched price under max-volume rule
def auction(buy_mkt, sell_mkt, levels):
    # levels: list of (price, buy_qty, sell_qty)
    res = {}
    for p, _, _ in levels:
        b = buy_mkt + sum(q for pp, q, _ in levels if pp >= p)
        s = sell_mkt + sum(q for pp, _, q in levels if pp <= p)
        res[p] = min(b, s)
    return res

# C5-015 opening auction
lv = [(60300, 1000, 2500), (60200, 2000, 3000), (60100, 3000, 2000), (60000, 2500, 1500), (59900, 1500, 1000)]
r = auction(2000, 1500, lv)
mx = max(r.values()); ps = [p for p, v in r.items() if v == mx]
assert len(ps) == 1
p = ps[0]
left = mx - 2000
rest = {}
for pp, b, _ in sorted(lv, reverse=True):
    if pp >= p:
        take = min(b, left); left -= take; rest[pp] = b - take
    else:
        rest[pp] = b
best = max(pp for pp, q in rest.items() if q > 0)
out['015'] = dict(match=r, price=p, vol=mx, best=(best, rest[best]))

# C5-016 closing auction with time priority at 41,100
lv = [(41200, 2500, 2000), (41100, 4000, 2000), (41000, 3000, 4000)]
r = auction(1500, 1000, lv)
mx = max(r.values()); ps = [p for p, v in r.items() if v == mx]; assert len(ps) == 1
left = mx - 1500 - 2500  # ATC then better price 41,200
H = min(2500, left); K = min(1500, left - H)
r2 = auction(0, 0, lv); mx2 = max(r2.values())
left2 = mx2 - 2500; H2 = min(2500, left2); K2 = min(1500, left2 - H2)
out['016'] = dict(match=r, price=ps[0], K=K, K_noATC=K2)

# C5-017 continuous LO buy sweep
asks = [(18450, 3000), (18500, 2000), (18550, 5000)]
q, val = 7000, 0
for pr, qq in asks:
    if pr > 18500: break
    t = min(q, qq); val += t * pr; q -= t
out['017'] = dict(key=val, all_at_limit=5000 * 18500, nolimit=3000*18450+2000*18500+2000*18550, all7000=7000*18500,
                  first_only=3000*18450)

# C5-018 MP remainder
out['018'] = dict(key=32350 + 50, ceiling=floor_tick(32300 * 1.07, 50))

# C5-019 buying power with odd lot (rewritten item)
cash, px, fee = 200_000_000, 39950, D('0.0015')
unit = D(px) * (1 + fee)
n_max = int(D(cash) / unit)
board = n_max // 100 * 100
rem = D(cash) - board * unit
odd = int(rem / unit)
assert odd <= 99 and (board + odd) * unit <= cash and (board + odd + 1) * unit > cash
nofee = cash // px
out['019'] = dict(unit=unit, board=board, odd=odd, total=board + odd, nofee_total=nofee,
                  nofee_board=nofee // 100 * 100, cost5000=5000 * unit)

# C5-020 breakeven sell price search for distinct distractors handled in search_020.py
def be(p0, f, t, tick):
    exact = p0 * (1 + f) / (1 - f - t)
    return dict(exact=exact, key=ceil_tick(exact, tick), buyfee_only=ceil_tick(p0 * (1 + f), tick),
                notax=ceil_tick(p0 * (1 + f) / (1 - f), tick), down=floor_tick(exact, tick))
out['020_orig'] = be(24000, 0.002, 0.001, 50)

# C5-021 WAC realized gain
cost = (2000 * 15200 + 3000 * 14600) * D('1.0015')
avg = cost / 5000
net = D(3000 * 15500) * (1 - D('0.0015') - D('0.001'))
gain = net - 3000 * avg
fifo = net - (2000 * 15200 + 1000 * 14600) * D('1.0015')
simple = net - 3000 * D((15200 + 14600) / 2) * D('1.0015')
nofee = 3000 * 15500 - 3000 * D(74_200_000) / 5000
out['021'] = dict(cost=cost, avg=avg, net=net, gain=gain, fifo=fifo, simple=simple, nofee=nofee)

# C5-022 adjusted reference with bonus 10:2 and rights 10:1 @15,000
out['022'] = dict(key=(45000 + 0.1 * 15000) / 1.3, norights=45000 / 1.2, den12=46500 / 1.2,
                  minus=(45000 - 1500) / 1.3, nopay=45000 / 1.3)

# C5-023 margin call deposit
V = 25000 * 22400; L = 25000 * 32000 * 0.5
X = 0.35 * V - (V - L)
Y = (0.35 * V - (V - L)) / 0.65  # wrong: deposit added as asset, debt unchanged
out['023'] = dict(ratio=(V - L) / V, key=X, wrong_asset=Y, back50=0.5 * V - (V - L), req=0.35 * V)

# C5-024 levered ROE
gainv = 400e6 * 0.08
i365 = 200e6 * 0.12 * 90 / 365; i360 = 200e6 * 0.12 * 90 / 360
out['024'] = dict(key=(gainv - i365) / 200e6, a360=(gainv - i360) / 200e6, noint=gainv / 200e6,
                  year=(gainv - 200e6 * 0.12) / 200e6, onall=(gainv - 400e6*0.12*90/365)/200e6)

# C5-034 coupon after tax
c = 2500 * 100000 * 0.092 / 2
out['034'] = dict(gross=c, key=c * 0.95, tax10=c * 0.9, annual_net=2 * c * 0.95)

# C5-035 30/360 accrued interest
def d30360(d1, d2): return (d2.year - d1.year) * 360 + (d2.month - d1.month) * 30 + (min(d2.day, 30) - min(d1.day, 30))
d1, d2 = date(2026, 3, 15), date(2026, 7, 21)
n30, nact = d30360(d1, d2), (d2 - d1).days
ai = 100000 * 0.08 * n30 / 360
out['035'] = dict(n30=n30, nact=nact, ai=ai, key=round(103450 - ai), a365=round(103450 - 8000 * nact / 365),
                  n30_365=round(103450 - 8000 * n30 / 365), a360=round(103450 - 8000 * nact / 360),
                  plus=round(103450 + ai), months4=round(103450 - 8000 * 4 / 12))

# C5-036 net bond sale proceeds
g = 5000 * (101500 + 1850)
out['036'] = dict(gross=g, key=g * 0.998, clean_only=5000 * 101500 * 0.998, fee_only=g * 0.999,
                  minus_ai=5000 * (101500 - 1850) * 0.998)

# C5-037 price from current yield
out['037'] = dict(key=7200 / 0.08, inv=100000 * 8 / 7.2, minus=100000 * (1 - 0.008), pv=107200 / 1.08)

# C5-038 approximate YTM
out['038'] = dict(key=(7000 + 6000 / 4) / 97000, cy=7000 / 94000, onP=8500 / 94000, onF=8500 / 100000,
                  full=(7000 + 6000) / 97000)

# C5-039 semiannual price
def price(c, y, n, F=100000): return sum(c / (1 + y) ** t for t in range(1, n + 1)) + F / (1 + y) ** n
out['039'] = dict(key=price(3000, 0.04, 4), annual=price(6000, 0.08, 2), nodisc=4 * 3000 + 100000 / 1.04 ** 4,
                  swap=price(4000, 0.03, 4), y8=price(3000, 0.08, 4))

# C5-040 price change 7% -> 8%
p8, p6 = price(7000, 0.08, 3), price(7000, 0.06, 3)
w = [7000 / 1.07, 7000 / 1.07 ** 2, 107000 / 1.07 ** 3]
mac = sum((i + 1) * x for i, x in enumerate(w)) / sum(w)
out['040'] = dict(p8=p8, key=(p8 / 100000 - 1) * 100, up6=(p6 / 100000 - 1) * 100, mac=mac, md=mac / 1.07)

for k, v in out.items():
    print(k, {a: (float(b) if isinstance(b, D) else b) for a, b in v.items()})

# New numbers introduced by the review
n = be(31200, 0.0015, 0.001, 50)
n['tax_both'] = ceil_tick(31200 * 1.0025 / 0.9975, 50)
assert (n['buyfee_only'], n['notax'], n['key'], n['tax_both']) == (31250, 31300, 31350, 31400)
assert 31300 * 0.9975 < 31200 * 1.0015 <= 31350 * 0.9975
print('020_new', n)
print('035_127', round(103450 - 8000 * 127 / 360))
assert round(103450 - 8000 * 127 / 360) == 100628 and round(out['040']['mac'] * 100) / 100 == 2.81
assert round(out['024']['a360'] * 100, 2) == 13.00 and round(out['024']['key'] * 100, 2) == 13.04
print('all asserts passed')
