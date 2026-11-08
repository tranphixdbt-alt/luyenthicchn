"""Giải lại các ví dụ trong slide 'Giao dịch bảo chứng' (SRTC). Chạy: python3 -I giai_slide.py"""
import math
def ceil_tick(x, t): return math.ceil(round(x, 6) / t) * t

# Tr.15 – Reg T 50%
eq = 5000; imr = .5
assert eq / imr - eq == 5000           # vay tối đa
assert 20000 * imr == 10000            # cần có để mua 20.000 USD
print("Tr15: vay tối đa 5.000 USD (sức mua 10.000); cần 10.000 USD")

# Tr.20 – ký quỹ 5.000, mua 1.000 x 10, giá còn 8
debt = 10000 - 5000; v = 8000; clm = v - debt
assert clm == 3000 and abs(clm / v - .375) < 1e-12
print("Tr20: CLM 3.000 USD; tỷ lệ thực tế 37,5%")

# Tr.22 – 10.000 USD, mua 500 SRT x20 + 500 SSC x10, sau đó 5 và 15
cost = 500*20 + 500*10; debt = cost - 10000; v = 500*5 + 500*15
r1 = (v - debt) / v
debt2 = cost * .5; cash2 = 10000 - cost * .5; r2 = (v + cash2 - debt2) / (v + cash2)   # cách hiểu 2: vay đúng 50% giá mua, tiền thừa để lại
assert (cost, debt, v) == (15000, 5000, 10000) and r1 == .5 and abs(r2 - .4) < 1e-12
print(f"Tr22: mua 15.000, nợ 5.000, giá trị mới 10.000 → tỷ lệ {r1:.2%} (nếu vay đúng 50% giá mua và giữ 2.500 tiền: {r2:.2%}) – đề mơ hồ")

# Tr.26/29 – duy trì 40%, ban đầu 50%, mua 1.000 x 10, ký quỹ 5.000
debt = 5000; p = debt / (1000 * .6)
v = 7000; e = v - debt; cash = .4 * v - e
sell = math.ceil(round(v - e / .4, 6) / 7)
sell3 = math.ceil(round(v - (e + 500) / .4, 6) / 7)
assert abs(p - 8.3333) < 1e-3 and abs(cash - 800) < 1e-9 and sell == 286 and sell3 == 108
print(f"Tr26/29: ngưỡng {p:.2f} USD; tại 7 USD tỷ lệ {e/v:.2%}; nộp {cash:.0f} USD hoặc bán {sell} cp; nộp 500 rồi bán {sell3} cp")

# Tr.30 / Tr.32 – 50%, mua 1.000 x 10, giá lên 15
v = 15000; debt = 5000; clm = v - debt; excess = clm - .5 * v; bp = excess / .5
assert (clm, excess, bp) == (10000, 2500, 5000) and v * .5 - debt == excess
print(f"Tr30/32: CLM {clm}; tỷ lệ thực tế {clm/v:.2%}; giá trị vượt trội {excess}; sức mua thêm {bp}")

# Tr.33 – giá trị 120.000, nợ 60.000, duy trì 25%, giá trị còn 75.000
v = 75000; debt = 60000; e = v - debt
pay = .25 * v - e; pay_alt = (.25 * v - e) / .75
assert e / v == .2 and pay == 3750 and pay_alt == 5000
print(f"Tr33: tỷ lệ {e/v:.0%} < 25% → vi phạm; nộp {pay:.0f} USD trả nợ (nếu tiền nộp chỉ cộng vào tài sản, không trả nợ: {pay_alt:.0f})")

# Tr.34–35 – CTCK cho vay 40% CP B, mua 1.000 x 30.000, duy trì 40%
q = 1000; p0 = 30000; debt = .4 * q * p0
p_call = debt / (q * .6)
assert p_call == 20000
r25 = (q*25000 - debt) / (q*25000); assert r25 == .52
def sessions(start, thr, tick=None):
    p, n = start, 0
    while p >= thr:
        n += 1; p = p * .93 if tick is None else ceil_tick(p * .93, tick)
    return n, p
n30, p30 = sessions(30000, 20000); n30t, p30t = sessions(30000, 20000, 50)
n25, p25 = sessions(25000, 20000); n25t, p25t = sessions(25000, 20000, 50)
assert (n30, n30t, n25, n25t) == (6, 6, 4, 4)
v = 18000 * q; e = v - debt; cash = .4 * v - e; sell = math.ceil(round(v - e / .4, 6) / 18000)
assert abs(cash - 1.2e6) < 1e-6 and sell == 167
v = 50000 * q; e = v - debt; excess = e - .6 * v; bp = excess / .6
assert excess == 8e6 and abs(bp - 13333333.33) < 1
print(f"Tr34a: ngưỡng {p_call:,.0f}; b: tại 25.000 tỷ lệ {r25:.0%} > 40% → chưa vi phạm")
print(f"Tr35d: từ 30.000 giảm sàn 7% liên tiếp → vi phạm ở phiên {n30} (giá {p30:,.0f}; làm tròn bước 50đ: {p30t:,.0f}); từ 25.000 → phiên {n25} ({p25:,.0f}; {p25t:,.0f})")
print(f"Tr35e: tại 18.000 tỷ lệ {(18e6-debt)/18e6:.2%}; nộp {cash:,.0f} đ hoặc bán {sell} cp")
print(f"Tr35f: tại 50.000 giá trị vượt trội {excess:,.0f}; sức mua tăng {bp:,.0f}")

# Tr.37 – bán khống 1.000 XYZ x 70, bảo chứng 50%, duy trì 30%
sv = 70000; eq = sv * .5; credit = sv + eq; pmax = credit / (1000 * 1.3)
assert credit == 105000 and abs(pmax - 80.769) < 1e-3
print(f"Tr37: giá trị bán {sv}; vốn thực có {eq:.0f}; dư có {credit:.0f}; ngưỡng giá {pmax:.2f} USD")

# Tr.38 – bán khống 100 x 50, giá lên 60
credit = 5000 * 1.5; v = 6000; e = credit - v; dep = .3 * v - e
assert e / v == .25 and abs(dep - 300) < 1e-9
print(f"Tr38: vốn thực có {e:.0f} ({e/v:.0%} < 30%) → nộp thêm {dep:.0f} USD")
