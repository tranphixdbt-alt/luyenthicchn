import random
prices = [24900, 25000, 25100, 25200, 25300]
def auction(bm, buys, sm, sells):
    return [(p, min(bm + sum(q for pr, q in buys.items() if pr >= p), sm + sum(q for pr, q in sells.items() if pr <= p))) for p in prices]
def uniq(r):
    m = max(v for _, v in r); t = [p for p, v in r if v == m]
    return t[0] if len(t) == 1 else None, m
rnd = random.Random(5)
for _ in range(500000):
    buys = {p: rnd.choice([1000, 1500, 2000, 2500, 3000]) for p in prices}
    sells = {p: rnd.choice([1000, 1500, 2000, 2500, 3000]) for p in prices}
    bm, sm = rnd.choice([2000, 2500, 3000]), rnd.choice([500, 1000])
    p1, m1 = uniq(auction(bm, buys, sm, sells)); p2, m2 = uniq(auction(0, buys, 0, sells))
    if p1 == 25200 and p2 == 25100:
        vols = [v for _, v in auction(bm, buys, sm, sells)]
        if len(set(vols)) == 5:
            print(bm, buys, sm, sells, auction(bm, buys, sm, sells), auction(0, buys, 0, sells)); break
