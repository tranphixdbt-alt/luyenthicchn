"""Tính lại độc lập các câu số/ngày của cm_7 (second pass). Chạy: python3 -I verify.py"""
import datetime as D
from decimal import Decimal as M, ROUND_DOWN

# C7-006: giá bán = NAV*(1+1,5%); số đơn vị làm tròn xuống 2 chữ số
nav, amt = M(15625), M(200_000_000)
price = nav * M('1.015')
key6 = (amt / price).quantize(M('0.01'), ROUND_DOWN)
d6 = [(amt / nav).quantize(M('0.01'), ROUND_DOWN),               # bỏ giá dịch vụ
      (amt * M('0.985') / nav).quantize(M('0.01'), ROUND_DOWN),  # trừ phí khỏi tiền rồi chia NAV
      (amt * M('0.985') / price).quantize(M('0.01'), ROUND_DOWN)]  # trừ phí hai lần
assert key6 == M('12610.83') and d6 == [M('12800.00'), M('12608.00'), M('12421.67')], (key6, d6)

# C7-007: chiết khấu so với NAV/ccq
n = 80_000_000
navu = (1260e9 - 60e9) / n
assert navu == 15000
k7 = round((navu - 12600) / navu * 100, 2)
d7 = [round((1150e9 / n - 12600) / (1150e9 / n) * 100, 2), round((navu - 12600) / 12600 * 100, 2),
      round((1260e9 / n - 12600) / (1260e9 / n) * 100, 2)]
assert k7 == 16.0 and d7 == [12.35, 19.05, 20.0], (k7, d7)

# C7-008: ETF, 5 lô x 100.000 ccq theo NAV
need = 18350 * 100_000 * 5
assert need - 9_120_000_000 == 55_000_000
assert 18420 * 500_000 - 9_120_000_000 == 90_000_000 and 55_000_000 // 5 == 11_000_000

# C7-031: bù trừ đa phương ròng tiền (tỷ đồng); (người mua, người bán, giá trị)
trades = [('P', 'Q', 10), ('Q', 'R', 8), ('R', 'P', 6), ('P', 'R', 3)]
net = {m: 0 for m in 'PQR'}
for b, s, v in trades:
    net[b] -= v; net[s] += v
gross = sum(v for _, _, v in trades)
pay_after = -sum(x for x in net.values() if x < 0)
assert net == {'P': -7, 'Q': 2, 'R': 5} and gross == 27 and pay_after == 7
key31 = gross - pay_after
d31 = [pay_after, sum(abs(x) for x in net.values()), 2 * gross - sum(abs(x) for x in net.values())]
assert key31 == 20 and d31 == [7, 14, 40], d31

# C7-032: bù trừ theo từng mã, tiền gộp
aaa, bbb = 120_000 - 85_000, 15_000 - 40_000
cash = (85_000 * 25_000 + 40_000 * 40_000) - (120_000 * 25_000 + 15_000 * 40_000)
assert (aaa, bbb, cash) == (35_000, -25_000, 125_000_000) and 35_000 * 25_000 == 875_000_000

# C7-033: 12 tháng kể từ 15/01/2026
assert D.date(2027, 1, 15).weekday() == 4  # Thứ Sáu

# C7-041: tối thiểu 10 ngày (dương lịch) trước ngày ĐKCC 26/11/2026 (Thứ Năm)
rec = D.date(2026, 11, 26); assert rec.weekday() == 3
assert rec - D.timedelta(10) == D.date(2026, 11, 16) and D.date(2026, 11, 16).weekday() == 0
assert rec - D.timedelta(20) == D.date(2026, 11, 6)
def back_wd(d, k):
    while k:
        d -= D.timedelta(1)
        if d.weekday() < 5: k -= 1
    return d
assert back_wd(rec, 10) == D.date(2026, 11, 12) and back_wd(rec, 5) == D.date(2026, 11, 19)

# C7-042: 15/11/2026 là Chủ nhật, ngày làm việc liền sau là Thứ Hai 16/11
assert D.date(2026, 11, 15).weekday() == 6 and D.date(2026, 11, 16).weekday() == 0
print('verify OK')
