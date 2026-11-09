"""Kiểm tra nhanh bằng số các công thức dùng trong thẻ PT/BC. Chạy: python3 -I kiem_so.py"""
import math

def close(a, b, tol=0.005): assert abs(a - b) <= tol, (a, b)

# --- Giá trị thời gian của tiền ---
pvifa = lambda r, n: (1 - (1 + r) ** -n) / r
fvifa = lambda r, n: ((1 + r) ** n - 1) / r
close(20 * pvifa(.1, 5), 75.82)                       # PV niên kim cuối kỳ (C2-003)
close(20 * pvifa(.1, 5) * 1.1, 83.40)                 # niên kim đầu kỳ = cuối kỳ × (1 + r)
close(10 * fvifa(.08, 4), 45.06)                      # FV niên kim (C9-003)
close(500 * .01 / (1 - 1.01 ** -24), 23.54)           # trả góp (C9-004)
close(sum(20 / 1.1 ** t for t in range(1, 6)), 20 * pvifa(.1, 5), 1e-9)
close(sum(50 / 1.1 ** t for t in range(4, 3000)), 50 / .1 / 1.1 ** 3)   # vĩnh viễn trả chậm 375,66
close(50 / .1 / 1.1 ** 3, 375.66)
close(sum(5 * 1.03 ** (t - 1) / 1.1 ** t for t in range(1, 3000)), 5 / (.1 - .03))  # vĩnh viễn tăng trưởng
close((1 + .1 / 4) ** 4 - 1, .1038, 5e-5)             # EAR ghép quý
close((1 + .1 / 1e6) ** 1e6 - 1, math.exp(.1) - 1, 1e-6)  # ghép liên tục
close(.1 / .9, .1111, 5e-5); close(.075 / 1.075, .0698, 5e-5)   # trả trước ↔ trả sau
# trả trước d: nhận 1 − d, trả 1 cuối kỳ ⇒ r = d/(1 − d)
d = .1; close(1 / (1 - d) - 1, d / (1 - d), 1e-12)

# --- Lợi suất, rủi ro ---
close((46 - 40 + 2) / 40, .20, 1e-9)                  # HPR
import random
for _ in range(1000):                                 # bình quân hình học ≤ số học
    rs = [random.uniform(-.5, .8) for _ in range(5)]
    g = math.prod(1 + r for r in rs) ** (1 / 5) - 1
    assert g <= sum(rs) / 5 + 1e-12
p, R = [.3, .5, .2], [.25, .10, -.10]
E = sum(a * b for a, b in zip(p, R)); close(E, .105, 1e-9)
close(math.sqrt(sum(a * (b - E) ** 2 for a, b in zip(p, R))), .1213, 5e-5)
sp = math.sqrt(.6**2*.2**2 + .4**2*.3**2 + 2*.6*.4*.2*.2*.3); close(sp, .1859, 5e-5); assert sp < .6*.2 + .4*.3
sp1 = math.sqrt(.6**2*.2**2 + .4**2*.3**2 + 2*.6*.4*1*.2*.3); close(sp1, .6*.2 + .4*.3, 1e-12)  # ρ = 1: không đa dạng hóa
sA, sB = .3, .2; wA = sB / (sA + sB); close(wA, .4, 1e-12)
close(abs(wA * sA - (1 - wA) * sB), 0, 1e-12)          # ρ = −1 ⇒ σp = 0
close(.018 / .12**2, 1.25, 1e-9)                      # beta
close(.3 * 1.4 + .2 * .9 + .5 * 0, .60, 1e-9)         # beta danh mục
close(.05 + 1.3 * .06, .128, 1e-9)                    # CAPM
close(.04 + .8 * (.11 - .04), .096, 1e-9)
close(.10 - (.04 + .6 * (.12 - .04)), .012, 1e-9)     # Jensen
close((.14 - .04) / .18, .56, .005); close((.14 - .04) / 1.2, .0833, 5e-5)

# --- Trái phiếu ---
price = lambda c, y, n, F=100000, m=1: sum(c * F / m / (1 + y / m) ** t for t in range(1, n * m + 1)) + F / (1 + y / m) ** (n * m)
close(price(.08, .10, 3), 95026, .5)
close(price(.10, .08, 2, m=2), 103630, .5)
close(100000 / 1.07 ** 5, 71299, .5)
close(9000 / 95000, .0947, 5e-5)
close(price(.06, .08, 2), 96433, .5)
def mac(c, y, n, F=100000):
    P = price(c, y, n, F); return sum(t * (c * F + (F if t == n else 0)) / (1 + y) ** t for t in range(1, n + 1)) / P
close(mac(.10, .10, 3), 2.7355, 5e-5)
close(98000 * (1 - 5.4 / 1.08 * .005), 95550, .5)
close(-6.5 * .01 + .5 * 60 * .01**2, -.062, 1e-9)
P = price(.08, .10, 3); cy = 8000 / P; assert .08 < cy < .10   # chiết khấu: coupon < CY < YTM
P = price(.12, .10, 3); cy = 12000 / P; assert .12 > cy > .10  # phụ trội: coupon > CY > YTM
assert mac(.04, .08, 10) > mac(.10, .08, 10)          # coupon thấp ⇒ D dài
assert mac(.08, .05, 10) > mac(.08, .10, 10)          # YTM thấp ⇒ D dài
assert mac(.08, .08, 15) > mac(.08, .08, 5)           # kỳ hạn dài ⇒ D dài
y = .08; P0 = price(.08, y, 10); D = mac(.08, y, 10); MD = D / (1 + y)
dP = (price(.08, y + .0001, 10) - price(.08, y - .0001, 10)) / (.0002 * P0); close(-dP, MD, 1e-3)  # MD = D/(1+y)

# --- Cổ phiếu ---
close(2000 * 1.06 / (.14 - .06), 26500, .01)
P0 = 50000; g = (P0 * .12 - 2000) / (P0 + 2000); close(g, .0769, 5e-5); close(2000 * (1 + g) / P0 + g, .12, 1e-12)  # r = D1/P0 + g
D1, D2 = 1200, 1440; P2 = D2 * 1.05 / (.12 - .05); close(D1 / 1.12 + (D2 + P2) / 1.12**2, 19439, .5)
close(.4 / (.12 - .15 * .6), 13.33, .005); close(.6 * 1.06 / (.11 - .06), 12.72, .005)
E1 = 1000; vals = [E1 * (1 - b) / (.12 - .08 * b) for b in (0, .4, .6)]; assert vals[0] > vals[1] > vals[2]   # ROE < r
vals = [E1 * (1 - b) / (.12 - .16 * b) for b in (0, .4, .6)]; assert vals[0] < vals[1] < vals[2]           # ROE > r
close(200 + 50 - 120 - 30 + (70 - 30), 140, 1e-9); close(300 * .8 + 60 - 100 - 20, 180, 1e-9)
close(.6 * .15 + .4 * .10 * .8, .122, 1e-9)
close(100 - 100 / (1 + 1500 / 500), 75, 1e-9)         # RSI
close(1.09 / 1.04 - 1, .0481, 5e-5)                   # Fisher

# --- BC ---
close(.18 / (.06 * 1.2), 2.5, 1e-9); close(1 - 1 / 2.5, .60, 1e-9)    # DuPont 3, nợ/TTS
DA = .6; close(1 / (1 - DA), 1 + DA / (1 - DA), 1e-12); close(1 / (1 - DA), 2.5, 1e-12)   # hệ số nhân vốn chủ
close(.8 * .75 * .15 * 1.2 * 2.0, .216, 1e-9)         # DuPont 5
close(365 / (1460 / 200), 50, 1e-9)                   # số ngày tồn kho
close((55 + 90 - 45) - (40 + 70 - 50), 40, 1e-9)      # CCC
close((1200 - 1000) * .8 - (1200 - 1000) * .2 - 1200 * .1 * .6, 48, 1e-9)   # AFN
close(350 / 150, 2.33, .005); assert 60 / 80 < 80 / 100                     # trả nợ NH bằng tiền
close((2.5 - .4) / 2.5, .84, 1e-9)                    # HTK ≈ 84% TSNH
close((200 - 80) / 1000, .12, 1e-9)                   # tỷ lệ dồn tích
close(300 - (180 - 20), 140, 1e-9)                    # FCF
close((180 + 60) / 60, 4, 1e-9)                       # khả năng trả lãi
print("OK: mọi kiểm tra số đều khớp")
