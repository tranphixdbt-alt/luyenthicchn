# Independent recomputation of every numeric C9 item (final version of cm_9.json).
# Run: python3 -I verify.py  -> prints each item's computed key/distractors and asserts they match the file.
import json, math
from pathlib import Path

D = {q['id']: q for q in json.loads((Path(__file__).parent.parent / 'cm_9.json').read_text(encoding='utf-8'))}

def vn(x, d=2):  # Vietnamese number format
    s = f"{x:,.{d}f}"
    return s.replace(',', 'X').replace('.', ',').replace('X', '.')

def check(i, key, others, unit=''):
    q = D[i]
    opts = [o.strip() for o in q['o']]
    k = opts[q['a']]
    assert key + unit in k or k.startswith(key), (i, 'key', key, k)
    for o in others:
        assert any(o in x for x in opts if x != k), (i, 'distractor', o, opts)
    print(i, 'OK key', key, '| distractors', others)

pv_ann = lambda r, n: (1 - (1 + r) ** -n) / r

# C9-001 EAR quarterly
check('C9-001', vn(100 * (1.025 ** 4 - 1)) + '%', [vn(10.0) + '%', vn(100 * ((1 + .1 / 12) ** 12 - 1)) + '%', vn(2.5) + '%'])
# C9-003 FV ordinary annuity
fv = 10 * ((1.08 ** 4 - 1) / .08)
check('C9-003', vn(fv), [vn(40.0), vn(10 + 10.8 + 11.6 + 12.4), vn(fv * 1.08)])
# C9-004 PMT
check('C9-004', vn(500 * .01 / (1 - 1.01 ** -24)), [vn(500 / 24 + 5), vn(500 / pv_ann(.12, 2) / 12), vn(500 / 24)])
# C9-005 deferred perpetuity
check('C9-005', vn(500 / 1.1 ** 3), [vn(500.0), vn(500 / 1.1 ** 4), vn(500 / 1.1 ** 2)])
# C9-006 CAPM with MRP
check('C9-006', vn(5 + 1.3 * 6) + '%', [vn(1.3 * 6) + '%', vn(5 + 1.3 * 1) + '%', vn(11.0) + '%'])
# C9-008 SML from two correctly priced stocks
slope = (14.2 - 10.0) / (1.4 - 0.8); rf = 10.0 - 0.8 * slope
check('C9-008', vn(rf + slope) + '%', [vn(slope) + '%', vn((10 + 14.2) / 2) + '%', vn(10 / 0.8) + '%'])
# C9-009 rho = -1 zero-risk portfolio
wa = 20 / 50
wv = 400 / (900 + 400)
check('C9-009', vn(wa * 14 + (1 - wa) * 8) + '%', [vn(.6 * 14 + .4 * 8) + '%', vn(11.0) + '%', vn(wv * 14 + (1 - wv) * 8) + '%'])
# C9-010 N equally weighted stocks
N, var, cov = 25, .40 ** 2, .04
sp = math.sqrt(var / N + (1 - 1 / N) * cov)
check('C9-010', vn(100 * sp) + '%', [vn(100 * math.sqrt(cov)) + '%', vn(100 * math.sqrt(var / N)) + '%', vn(40.0) + '%'])
# C9-011 portfolio beta with T-bills
check('C9-011', vn(.3 * 1.4 + .2 * .9), [vn((.3 * 1.4 + .2 * .9) / .5), vn((1.4 + .9 + 0) / 3), vn((1.4 + .9) / 2)])
# C9-012 Sharpe / Treynor
assert 10 / 18 > 8 / 20 and 10 / 1.2 < 8 / .8; print('C9-012 OK Sharpe X, Treynor Y')
# C9-013 Jensen
alpha = 10 - (4 + .6 * 8)
assert abs(alpha - 1.2) < 1e-9; print('C9-013 OK alpha', alpha)
# C9-014 hedge outcome
V, beta, n, F0, F1, m = 20e9, 1.1, 169, 1300, 1235, 1e5
assert abs(F1 / F0 - 0.95) < 1e-12
port = V * beta * -0.05; fut = n * (F0 - F1) * m
net = port + fut
check('C9-014', 'Lỗ ' + vn(-net / 1e6, 1), ['Lỗ ' + vn(-port / 1e6, 0).replace(',0', ''), 'Lãi ' + vn((V * -0.05 + fut) / 1e6, 1), 'Lỗ ' + vn((-port + fut) / 1e6, 1)])
# C9-015 put-call parity arbitrage
pvk = 32000 / (1 + .08 * 3 / 12)
gap = 2000 + pvk - (2800 + 30000)
assert gap > 0 and round(gap) == 573 and 2000 + 32000 - 32800 == 1200
cash0 = 2000 + pvk - 2800 - 30000
for ST in (20000, 32000, 45000):  # riskless at expiry
    assert abs(ST + max(32000 - ST, 0) - max(ST - 32000, 0) - 32000) < 1e-9
print('C9-015 OK arbitrage', round(cash0, 2))
# C9-016 implied g
g = (50000 * .12 - 2000) / (50000 + 2000)
check('C9-016', vn(100 * g) + '%', [vn(8.0) + '%', vn(16.0) + '%', vn(4.0) + '%'])
# C9-017 two-year DDM with P/E exit
P2 = 12 * 3000
v = 1000 / 1.14 + (1200 + P2) / 1.14 ** 2
fmt0 = lambda x: f"{round(x):,}".replace(',', '.')
check('C9-017', fmt0(v), [fmt0(1000 / 1.14 + 1200 / 1.14 ** 2 + P2 / 1.14), fmt0(1000 / 1.14 + 1200 / 1.14 ** 2 + P2), fmt0(1000 + 1200 + P2)])
# C9-018 trailing P/E
check('C9-018', vn(.6 * 1.06 / .05), [vn(.6 / .05), vn(.6 * 1.06 / .11), vn(.4 * 1.06 / .05)])
# C9-019 ROE < r example
assert round(1000 / .12) == 8333 and round(600 / (.12 - .08 * .4)) == 6818 and round(400 / (.12 - .08 * .6)) == 5556
print('C9-019 OK example')
# C9-020 semiannual bond
price = lambda c, y, n, F=100000: c * pv_ann(y, n) + F / (1 + y) ** n
check('C9-020', fmt0(price(5000, .04, 4)), [fmt0(price(10000, .08, 2)), fmt0(price(4000, .05, 4)), fmt0(price(5000, .08, 4))])
# C9-021 realized compound yield with reinvestment at 6%
end = 10000 * 1.06 + 110000
check('C9-021', vn(100 * (math.sqrt(end / 100000) - 1)) + '%', [vn(10.0) + '%', vn(100 * (end - 100000) / 2 / 100000) + '%', vn(100 * (math.sqrt(1.2) - 1)) + '%'])
# C9-022 zero-coupon
check('C9-022', fmt0(100000 / 1.07 ** 5), [fmt0(100000 * (1 - 5 * .07)), fmt0(100000 / 1.35), fmt0(100000 / 1.035 ** 10)])
# C9-023 duration approximation
MD = 5.4 / 1.08
check('C9-023', fmt0(98000 * (1 - MD * .005)), [fmt0(98000 * (1 - 5.4 * .005)), fmt0(98000 * (1 + MD * .005)), fmt0(98000 * (1 - MD * .0005))])
# C9-029 short sale with dividend
check('C9-029', 'Lãi ' + fmt0(5000 * 6000 - 5000 * 1000), ['Lãi ' + fmt0(5000 * 6000), 'Lãi ' + fmt0(5000 * 7000), 'Lỗ ' + fmt0(25e6)])
# C9-030 short-sale margin call price
check('C9-030', fmt0(750e6 / (1.3 * 10000)), [fmt0(60000), fmt0(65000), fmt0(75000)])
# C9-031 actual margin ratio
check('C9-031', vn(100 * (500 - 300) / 500) + '%', [vn(60.0) + '%', vn(50 * 25 / 30) + '%', vn(50.0) + '%'])
# C9-032 leverage loss
check('C9-032', vn(100 * 500 * .15 / 300) + '%', [vn(15.0) + '%', vn(100 * 75 / 200) + '%', vn(9.0) + '%'])
# C9-033 buying power
check('C9-033', fmt0(300e6 / .4 / 25000), [fmt0(12000), fmt0(300e6 * 1.4 / 25000), fmt0(300e6 / .6 / 25000)])
# C9-034 shares to sell to restore 35%
x = 600 - 180 / .35
check('C9-034', fmt0(math.ceil(x * 1e6 / 20000)), [fmt0((.35 * 600 - 180) * 1e6 / 20000), fmt0(math.ceil((600 - 180 / .5) * 1e6 / 20000)), fmt0(math.ceil((600 - 180 / .65) * 1e6 / 20000))])
# C9-035 excess equity -> extra buying power
ex = (1000 - 450) - .5 * 1000
assert (1000 + ex / .5 - 550) / (1000 + ex / .5) == .5
check('C9-035', fmt0(ex / .5), [fmt0(ex * .5), fmt0(ex), fmt0(550 / .5)])
# C9-036 margin call price with accrued interest
loan = 250e6; intr = loan * .13 * 146 / 365; debt = loan + intr
assert abs(intr - 13e6) < 1e-6
check('C9-036', fmt0(debt / (.7 * 20000)), [fmt0(loan / (.7 * 20000)), fmt0((loan + 500e6 * .13 * 146 / 365) / (.7 * 20000)), fmt0(25000 * (1 - .2))])
# C9-039 repo with haircut
back = lambda cash, r, d, b=365: cash * (1 + r * d / b)
check('C9-039', fmt0(back(9.5e9, .05, 30)), [fmt0(back(10e9, .05, 30)), fmt0(back(9.5e9, .05, 30, 360)), fmt0(9.5e9 + 10e9 * .05 * 30 / 365)])
# C9-040 implied repo rate
hp = 20046027397 / 20e9 - 1
check('C9-040', vn(100 * hp * 365 / 14) + '%', [vn(100 * hp) + '%', vn(100 * hp * 360 / 14) + '%', vn(100 * ((1 + hp) ** (365 / 14) - 1)) + '%'])

# rank of the numeric key among its options (1 = smallest), to spot a systematic pattern
import re
def num(s):
    m = re.search(r'(−|-)?\d[\d.]*(,\d+)?', s)
    if not m: return None
    v = float(m.group(0).replace('−', '-').replace('.', '').replace(',', '.'))
    return -v if s.strip().startswith('Lỗ') else v
ranks = {}
for i, q in D.items():
    vals = [num(o) for o in q['o']]
    if all(v is not None for v in vals) and len(set(vals)) == 4 and not q['o'][0].startswith('PV'):
        ranks[i] = sorted(vals).index(vals[q['a']]) + 1
from collections import Counter
print('key rank among numeric options:', dict(sorted(Counter(ranks.values()).items())))
print(ranks)
