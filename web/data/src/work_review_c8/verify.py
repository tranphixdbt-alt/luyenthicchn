"""Tính lại độc lập mọi số liệu của cm_8 và assert khớp đáp án/phương án nhiễu trong file.
Chạy: python3 -I verify.py"""
import json
from datetime import date, timedelta
from pathlib import Path
Q = {q["id"]: q for q in json.loads((Path(__file__).resolve().parent.parent / "cm_8.json").read_text())}
key = lambda i: Q[i]["o"][Q[i]["a"]]
opts = lambda i: Q[i]["o"]
d = lambda x: x.strftime("%d/%m/%Y")
vn = lambda x, n=2: f"{x:,.{n}f}".replace(",", "X").replace(".", ",").replace("X", ".")

# C8-003: ngày ĐKCC dự kiến 30/12/2026, CBTT tối thiểu 20 ngày trước
r = date(2026, 12, 30)
assert key("C8-003") == d(r - timedelta(20)) == "10/12/2026"
assert {d(r - timedelta(n)) for n in (10, 21, 15)} == set(opts("C8-003")) - {key("C8-003")}

# C8-005: VSDC 15 ngày kể từ 02/11/2026; nhiễu 30 ngày, 7 ngày, 1 năm
x = date(2026, 11, 2)
assert key("C8-005") == d(x + timedelta(15)) == "17/11/2026"
assert {d(x + timedelta(30)), d(x + timedelta(7)), d(x.replace(year=2027))} == set(opts("C8-005")) - {key("C8-005")}

# C8-013: thời hiệu khiếu nại 90 ngày kể từ ngày nhận quyết định
x = date(2026, 10, 14)
end = x + timedelta(90)
assert key("C8-013") == d(end) == "12/01/2027" and end.weekday() < 5, end.weekday()   # ngày cuối không rơi vào cuối tuần
assert {d(x.replace(year=2027, month=1)), d(x + timedelta(60)), d(x + timedelta(30))} == set(opts("C8-013")) - {key("C8-013")}

# C8-014: giá tham chiếu UPCoM = bình quân gia quyền giá khớp lệnh liên tục
kl = [(4000, 24600), (1000, 25100), (5000, 24300)]; tt = (20000, 26000)
w = sum(a * p for a, p in kl) / sum(a for a, _ in kl)
assert w == 24500 and key("C8-014") == "24.500 đồng"
alla = (sum(a * p for a, p in kl) + tt[0] * tt[1]) / (sum(a for a, _ in kl) + tt[0])
simple = sum(p for _, p in kl) / 3
assert alla == 25500 and round(simple, -2) == 24700 and kl[-1][1] == 24300
assert {"24.300 đồng", "25.500 đồng", "24.700 đồng"} == set(opts("C8-014")) - {key("C8-014")}

# C8-016: VĐL 1.000 tỷ, LNST 120 tỷ; mức cũ TT 146: 5% LNST mỗi quỹ đến 10% VĐL
assert 0.05 * 120 == 6 and 0.10 * 120 == 12 and 0.10 * 1000 == 100
assert "6 tỷ" in opts("C8-016")[0] + "".join(opts("C8-016")) and "12 tỷ" in "".join(opts("C8-016")) and "100 tỷ" in "".join(opts("C8-016"))

# C8-022: U = E(r) − 0,5·A·σ²
U = lambda A, h=0.5: 0.14 - h * A * 0.25 ** 2
assert abs(U(2) - 0.0775) < 1e-12 and abs(U(4) - 0.015) < 1e-12 and U(2) > 0.05 > U(4)
assert abs(U(2, 1) - 0.015) < 1e-12 and abs(U(4, 1) + 0.11) < 1e-12           # quên hệ số 0,5
assert key("C8-022").startswith("U = 7,75% với A = 2 và 1,50% với A = 4; chỉ người có A = 2")

# C8-023: 400 tr; (1) 7,5% trả sau; (2) 7,0% trả trước, tiền lãi gửi tiếp 7,5%
fv1 = 400 * 0.075; fv2 = 400 * 0.07 * 1.075
assert abs(fv1 - 30) < 1e-9 and abs(fv2 - 30.1) < 1e-9 and fv2 > fv1
eq = 0.075 / 1.075; wrong = 0.075 / 0.925
assert vn(eq * 100) == "6,98" and vn(wrong * 100) == "8,11" and eq < 0.07
assert "6,98%" in key("C8-023") and "(2)" in key("C8-023")
assert any("8,11%" in o for o in opts("C8-023"))

# C8-025: mức bù tín dụng (điểm cơ bản)
X, Y = round((4.1 - 3.2) * 100), round((6.0 - 3.2) * 100)
assert (X, Y, Y - X) == (90, 280, 190)
assert key("C8-025") == f"Mức bù của Y là {Y} điểm cơ bản, cao hơn của X {Y - X} điểm cơ bản"

# C8-026: hệ số với r = 8%, n = 5
r, n = 0.08, 5
fvifa = ((1 + r) ** n - 1) / r; pvifa = (1 - (1 + r) ** -n) / r; fvif = (1 + r) ** n; pvif = (1 + r) ** -n
assert vn(fvifa, 4) == "5,8666" and fvifa > n > pvifa and pvif < 1 < fvif < n
assert "5,8666" in Q["C8-026"]["q"] and "FVIFA" in key("C8-026")
for nn in range(2, 41):                       # FVIFA > n với mọi r > 0, n ≥ 2
    for rr in (0.001, 0.05, 0.3, 2.0):
        assert ((1 + rr) ** nn - 1) / rr > nn
assert 1.08 ** 4 < 4

# C8-027: Y = 7% hoặc 11%, xác suất bằng nhau
ey = (0.07 + 0.11) / 2; sy = ((0.5 * (0.07 - ey) ** 2 + 0.5 * (0.11 - ey) ** 2)) ** 0.5
assert abs(ey - 0.09) < 1e-12 and abs(sy - 0.02) < 1e-12

# C8-028: thị trường giảm 10%, beta 1,4 và 0,7
m = -0.10
assert (round(1.4 * m * 100), round(0.7 * m * 100)) == (-14, -7)
assert key("C8-028") == "Danh mục beta 1,4 giảm khoảng 14%, danh mục beta 0,7 giảm khoảng 7%"
assert (vn(10 / 1.4, 1), vn(10 / 0.7, 1)) == ("7,1", "14,3")
assert (round((1.4 - 1) * m * 100), round((0.7 - 1) * m * 100)) == (-4, 3)

# một đáp án, 4 phương án khác nhau
for i, q in Q.items():
    assert len(q["o"]) == 4 and len(set(q["o"])) == 4 and 0 <= q["a"] < 4, i
print("OK: số liệu cm_8 đã tính lại khớp")
