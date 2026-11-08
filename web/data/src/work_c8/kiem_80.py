"""Tính lại các câu có số liệu trong 80 câu công khai của onthicchnchungkhoan (chỉ để soát đáp án của họ).
Chạy: python3 -I kiem_80.py"""

# MG-1372: repo 1 triệu TPCP giá 10.000, 14 ngày, 4,5%/năm, 365 ngày
p1 = 1_000_000 * 10_000
p2 = p1 * (1 + 0.045 * 14 / 365)
assert round(p2) == 10_017_260_274, p2

# MG-1190: khớp lệnh liên tục theo thứ tự thời gian (giá tham chiếu 70.000)
orders = [  # (thứ tự, bên, KH, KL, giá; None = MP)
    (1, 'B', 'A', 1000, 68000), (2, 'S', 'F', 1000, 70500), (3, 'B', 'D', 300, None),
    (4, 'B', 'B', 900, 68500), (5, 'S', 'I', 1500, None), (6, 'B', 'H', 1200, 73000)]
book = {'B': [], 'S': []}
fills = []
for _, side, who, qty, px in orders:
    opp = 'S' if side == 'B' else 'B'
    # sổ đối ứng: bán tăng dần, mua giảm dần, cùng giá theo thời gian
    book[opp].sort(key=lambda o: (o[2] if opp == 'S' else -o[2], o[3]))
    while qty and book[opp]:
        ow, oq, op, ot = book[opp][0]
        if px is not None and ((side == 'B' and op > px) or (side == 'S' and op < px)):
            break
        q = min(qty, oq)
        fills.append((who, ow, q, op)); qty -= q
        book[opp][0] = (ow, oq - q, op, ot)
        if book[opp][0][1] == 0: book[opp].pop(0)
    if qty and px is not None:
        book[side].append((who, qty, px, _))
assert fills == [('D', 'F', 300, 70500), ('I', 'B', 900, 68500), ('I', 'A', 600, 68000), ('H', 'F', 700, 70500)], fills

# PT-1649: CAPM
k = 0.08 + 2 * 0.09
assert abs(k - 0.26) < 1e-12 and 0.25 < k

# PT-1652: lãi trả sau 11% -> trả trước
assert round(0.11 / 1.11 * 100, 2) == 9.91

# PT-1677: lãi kép 3 năm 8,4%
assert round((1.084 ** 3 - 1) * 100, 3) == 27.376   # đề ghi 27,37% (cắt bớt), đúng ra 27,38%; vẫn là phương án gần nhất

# PT-1893: call, phí 2, X 40, chi phí 0,5, P_T 50, 100 cp
assert (50 - 40 - 2 - 0.5) * 100 == 750

# PT-1657: DPS với cổ phiếu quỹ
assert 560_000_000 / (600_000 - 40_000) == 1000

# PT-1889: dòng n của bảng FVIFA luôn > n (n >= 2, r > 0); FVIF thì không
for r in [0.01, 0.05, 0.1, 0.2]:
    for n in range(2, 31):
        fvifa = ((1 + r) ** n - 1) / r
        assert fvifa > n
assert (1.10 ** 5) < 5          # FVIF dòng 5 có thể nhỏ hơn 5
print('OK: số liệu của các câu tính toán trong 80 câu đã được tính lại')
