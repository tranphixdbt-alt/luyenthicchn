import itertools, random
ref = 25000
prices = [24800, 24900, 25000, 25100, 25200]
def solve(buy_ato, buys, sell_ato, sells):
    res = []
    for p in prices:
        cb = buy_ato + sum(q for pr, q in buys.items() if pr >= p)
        cs = sell_ato + sum(q for pr, q in sells.items() if pr <= p)
        res.append((p, min(cb, cs), cb, cs))
    return res
random.seed(7)
for _ in range(200000):
    buys = {p: random.choice([1000, 2000, 3000]) for p in prices}
    sells = {p: random.choice([1000, 2000, 3000]) for p in prices}
    ba, sa = random.choice([1000, 2000]), random.choice([1000, 2000])
    r = solve(ba, buys, sa, sells)
    mx = max(x[1] for x in r)
    top = [x[0] for x in r if x[1] == mx]
    if top == [25100, 25200]:
        print(ba, buys, sa, sells); [print(x) for x in r]; break
