# Explore designs for periodic auction examples
def auction(buy_mkt, buys, sell_mkt, sells, prices):
    out = []
    for p in prices:
        cb = buy_mkt + sum(q for pr, q in buys.items() if pr >= p)
        cs = sell_mkt + sum(q for pr, q in sells.items() if pr <= p)
        out.append((p, cb, cs, min(cb, cs)))
    return out
prices = [24900, 25000, 25100, 25200, 25300]
buys = {25300: 1000, 25200: 1500, 25100: 2000, 25000: 3000, 24900: 2500}
sells = {24900: 2000, 25000: 1500, 25100: 2500, 25200: 3000, 25300: 2000}
for ba, sa in [(2000, 1000), (0, 0)]:
    print('mkt', ba, sa)
    for r in auction(ba, buys, sa, sells, prices): print(r)
# ATC example
print('ATC')
for r in auction(1500, {41200: 2500, 41100: 4000, 41000: 3000}, 1000, {41000: 4000, 41100: 2000, 41200: 2000}, [41000, 41100, 41200]): print(r)
import datetime
print((datetime.date(2026,7,21)-datetime.date(2026,3,15)).days)
