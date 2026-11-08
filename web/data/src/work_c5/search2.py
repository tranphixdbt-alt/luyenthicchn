import random
prices = [51800, 51900, 52000, 52100, 52200, 52300]
def auction(bm, buys, sm, sells):
    return [(p, bm + sum(q for pr, q in buys.items() if pr >= p), sm + sum(q for pr, q in sells.items() if pr <= p)) for p in prices]
rnd = random.Random(11)
for _ in range(2000000):
    buys = {p: rnd.choice([0, 500, 1000, 1500, 2000, 3000]) for p in prices}
    sells = {p: rnd.choice([0, 500, 1000, 1500, 2000, 3000]) for p in prices}
    bm, sm = rnd.choice([1000, 1500, 2000]), rnd.choice([500, 1000])
    r = auction(bm, buys, sm, sells)
    v = [min(b, s) for _, b, s in r]
    m = max(v); top = [p for (p, _, _), x in zip(r, v) if x == m]
    if top == [52100, 52200] and sum(1 for x in buys.values() if x) >= 5 and sum(1 for x in sells.values() if x) >= 5:
        # without market orders the answer should differ
        r0 = auction(0, buys, 0, sells); v0 = [min(b, s) for _, b, s in r0]; m0 = max(v0)
        top0 = [p for (p, _, _), x in zip(r0, v0) if x == m0]
        if top0 != top and len(top0) == 1:
            print(bm, buys, sm, sells); [print(x, min(x[1], x[2])) for x in r]; print(top0, m0); break
