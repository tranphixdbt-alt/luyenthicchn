# Soát "Câu hỏi ôn tập lớp Chứng khoán cơ bản": (1) giải lại 2 bài tập + tính lại mọi con số của tài liệu
# và của các câu tương ứng trong ngân hàng (assert); (2) sinh câu mới -> ../cm_12.json.
# Chạy: python3 -I gen_c12.py
import json, random, re, unicodedata
from collections import Counter
from fractions import Fraction as Fr

OUT = '/home/user/cchn_moi/web/data/src/cm_12.json'
VB = '/home/user/cchn_moi/tai_lieu_phap_ly/van_ban_txt/'
LCK = 'VBHN_102_VBHN-VPQH_2026_Luat_Chung_khoan_hop_nhat.txt'
TT120 = 'TT_120_2020_TT-BTC_hop_nhat_VBHN_08_VBHN-BTC_2026.txt'
GT = 'Giáo trình Những vấn đề cơ bản về chứng khoán và TTCK (UBCKNN/SRTC) – '
T_CC = "Các công cụ tài chính trên thị trường chứng khoán"
T_TC = "Thị trường chứng khoán thứ cấp"
T_SC = "Thị trường chứng khoán sơ cấp"

def vn(x, d=0):
    return f"{x:,.{d}f}".replace(',', 'X').replace('.', ',').replace('X', '.')

# ---------- động cơ khớp lệnh (quy tắc HOSE trước KRX, chỉ dùng làm giả định) ----------
def band(ref, pct, tick):
    """Giá trần làm tròn xuống, giá sàn làm tròn lên theo bước giá."""
    return ref * (100 + pct) // (100 * tick) * tick, -(-ref * (100 - pct) // (100 * tick)) * tick

def auction(buys, sells, ref, levels=None):
    """Khớp lệnh định kỳ: KL lớn nhất -> gần giá tham chiếu nhất -> giá cao hơn. Lệnh p=None là ATO/ATC."""
    lv = levels or sorted({o['p'] for o in buys + sells if o['p']})
    def vol(P):
        d = sum(o['q'] for o in buys if o['p'] is None or o['p'] >= P)
        s = sum(o['q'] for o in sells if o['p'] is None or o['p'] <= P)
        return d, s, min(d, s)
    tab = {P: vol(P) for P in lv}
    best = max(v[2] for v in tab.values())
    cands = [P for P in lv if tab[P][2] == best]
    near = min(abs(P - ref) for P in cands)
    return max(P for P in cands if abs(P - ref) == near), best, tab

def allocate(orders, buy, P, V):
    """Phân bổ V tại giá P: ATO/ATC trước, rồi ưu tiên giá, rồi thời gian."""
    elig = [o for o in orders if o['p'] is None or (o['p'] >= P if buy else o['p'] <= P)]
    key = lambda o: (o['p'] is not None, -(o['p'] or 0) if buy else (o['p'] or 0), o['t'])
    fills, left = {}, V
    for o in sorted(elig, key=key):
        fills[o['id']] = min(o['q'], left); left -= fills[o['id']]
    assert left == 0
    return fills

def continuous(seq, tick, ceil, floor, bids=None, asks=None):
    """Khớp lệnh liên tục theo thứ tự nhập; giá khớp = giá lệnh chờ; MP: quét giá tốt nhất,
    phần còn lại thành LO cách giá khớp cuối 1 bước giá (chạm trần/sàn thì lấy trần/sàn)."""
    bids, asks, trades = [dict(o) for o in bids or []], [dict(o) for o in asks or []], []
    t0 = len(bids) + len(asks)
    for i, o in enumerate(seq):
        buy, p, q = o['side'] == 'B', o['p'], o['q']
        book, last = (asks if buy else bids), None
        while q and book:
            best = min(book, key=lambda x: (x['p'], x['t'])) if buy else min(book, key=lambda x: (-x['p'], x['t']))
            if p is not None and (best['p'] > p if buy else best['p'] < p):
                break
            f = min(q, best['q']); q -= f; best['q'] -= f; last = best['p']
            trades.append((o['id'], best['id'], best['p'], f))
            if not best['q']:
                book.remove(best)
        if q:
            if p is None:
                assert last is not None, 'MP không có lệnh đối ứng'
                p = min(last + tick, ceil) if buy else max(last - tick, floor)
            (bids if buy else asks).append(dict(id=o['id'], p=p, q=q, t=t0 + i))
    return trades, bids, asks

def filled(trades, who):
    return [(p, f) for a, b, p, f in trades if who in (a, b)]

O = lambda i, p, q, t=0: dict(id=i, p=p, q=q, t=t)

# ======================= 1. Bài tập 01 (ATO, VHM – đề ghi nhầm "MSN") =======================
ref1 = 33000
ceil1, floor1 = band(ref1, 7, 50)
assert abs(ref1 * 1.07 - 35310) < 1e-6 and abs(ref1 * 0.93 - 30690) < 1e-6
assert (ceil1, floor1) == (35300, 30700)
B1 = [O('M1', None, 3500, 1), O('M2', 35000, 2000, 2), O('M3', 34900, 2500, 3), O('M4', 34000, 3000, 4),
      O('M5', 33600, 2300, 5), O('M6', 33500, 5000, 6), O('M7', 32000, 4000, 7)]
S1 = [O('B7', None, 2000, 1), O('B6', 35000, 2500, 2), O('B5', 34900, 2000, 3), O('B4', 34500, 5000, 4),
      O('A', 33900, 2000, 900), O('C', 33900, 1500, 908), O('B', 33900, 1500, 910),   # B3 = A 9h00, C 9h08, B 9h10
      O('B2', 33500, 5000, 6), O('B1', 32000, 3500, 7)]
P1, V1, tab1 = auction(B1, S1, ref1)
assert (P1, V1) == (33900, 11000)
assert tab1[34000] == (11000, 15500, 11000) and tab1[33900] == (11000, 15500, 11000) and tab1[33600][2] == 10500
# kiểm tra với mọi bước giá 50 đồng trong biên độ: kết quả không đổi (33.950 cũng đạt 11.000 nhưng xa giá TC hơn)
P1b, V1b, _ = auction(B1, S1, ref1, levels=list(range(floor1, ceil1 + 1, 50)))
assert (P1b, V1b) == (33900, 11000)
fb1, fs1 = allocate(B1, True, P1, V1), allocate(S1, False, P1, V1)
assert fb1 == {'M1': 3500, 'M2': 2000, 'M3': 2500, 'M4': 3000}
assert fs1 == {'B7': 2000, 'B1': 3500, 'B2': 5000, 'A': 500, 'C': 0, 'B': 0}
print("Bài tập 01:")
print(f"  trần/sàn: {vn(ref1 * 1.07)}/{vn(ref1 * 0.93)} (chưa làm tròn) -> {vn(ceil1)}/{vn(floor1)} (bước giá 50)")
for P in sorted(tab1, reverse=True):
    print(f"  {vn(P):>7}: mua cộng dồn {vn(tab1[P][0]):>7} | bán cộng dồn {vn(tab1[P][1]):>7} | khớp {vn(tab1[P][2])}")
print(f"  giá mở cửa {vn(P1)}, KL {vn(V1)}; bán: {fs1}")
# sổ lệnh sau phiên ATO (lệnh ATO hết hiệu lực; ở đây đều khớp đủ)
rest_b = [dict(o, q=o['q'] - fb1.get(o['id'], 0)) for o in B1 if o['p'] and o['q'] > fb1.get(o['id'], 0)]
rest_s = [dict(o, q=o['q'] - fs1.get(o['id'], 0)) for o in S1 if o['p'] and o['q'] > fs1.get(o['id'], 0)]
assert [(o['id'], o['p'], o['q']) for o in sorted(rest_b, key=lambda o: -o['p'])] == \
    [('M5', 33600, 2300), ('M6', 33500, 5000), ('M7', 32000, 4000)]
assert [(o['id'], o['p'], o['q']) for o in sorted(rest_s, key=lambda o: (o['p'], o['t']))] == \
    [('A', 33900, 1500), ('C', 33900, 1500), ('B', 33900, 1500), ('B4', 34500, 5000), ('B5', 34900, 2000), ('B6', 35000, 2500)]
print("  sổ lệnh sau phiên: mua", [(o['id'], o['p'], o['q']) for o in rest_b], "| bán", [(o['id'], o['p'], o['q']) for o in rest_s])
# M8: MP mua 20.000 trong phiên liên tục kế tiếp
tr, bb, aa = continuous([dict(id='M8', side='B', p=None, q=20000)], 50, ceil1, floor1, rest_b, rest_s)
m8 = filled(tr, 'M8')
assert m8 == [(33900, 1500), (33900, 1500), (33900, 1500), (34500, 5000), (34900, 2000), (35000, 2500)]
assert [t[1] for t in tr[:3]] == ['A', 'C', 'B']
q8, v8 = sum(f for _, f in m8), sum(p * f for p, f in m8)
assert (q8, v8) == (14000, 482350000) and not aa
assert [(o['id'], o['p'], o['q']) for o in bb if o['id'] == 'M8'] == [('M8', 35050, 6000)]
print(f"  M8: khớp {vn(q8)} cp, giá trị {vn(v8)}, giá BQ {vn(v8 / q8, 2)}; 6.000 cp còn lại thành LO mua 35.050")

# ======================= 2. Bài tập 02 (khớp liên tục, giá TC 70.000) =======================
ceil2, floor2 = band(70000, 7, 100)
assert (ceil2, floor2) == (74900, 65100)
seq2 = [dict(id='A', side='B', p=68000, q=1000), dict(id='F', side='S', p=70500, q=1000),
        dict(id='D', side='B', p=None, q=300), dict(id='B', side='B', p=68500, q=900),
        dict(id='I', side='S', p=None, q=1500), dict(id='H', side='B', p=73000, q=1200)]   # lệnh 001…006
tr2, bb2, aa2 = continuous(seq2, 100, ceil2, floor2)
res2 = {k: filled(tr2, k) for k in 'ABDFIH'}
assert res2 == {'A': [(68000, 600)], 'B': [(68500, 900)], 'D': [(70500, 300)], 'F': [(70500, 300), (70500, 700)],
                'I': [(68500, 900), (68000, 600)], 'H': [(70500, 700)]}
assert [(o['id'], o['p'], o['q']) for o in bb2] == [('A', 68000, 400), ('H', 73000, 500)] and not aa2
print("Bài tập 02:", res2, "| chờ mua:", [(o['id'], o['p'], o['q']) for o in bb2])

# ======================= 3. Các câu có tính toán =======================
# Câu 02: cổ tức/cp = 560 tr / (600.000 − 40.000)
assert 560_000_000 / (600_000 - 40_000) == 1000
# Câu 13: mua call K=48, phí 5 USD/cp × 100 cp, S_T = 45 -> không thực hiện
assert max(45 - 48, 0) * 100 - 5 * 100 == -500
# Câu 16: khớp liên tục theo giờ
seq16 = [dict(id='b910', side='B', p=20000, q=2000), dict(id='b911', side='B', p=20500, q=1000),
         dict(id='s913', side='S', p=20500, q=2000), dict(id='b914', side='B', p=21000, q=3000),
         dict(id='s915', side='S', p=20000, q=2000)]
tr16, bb16, _ = continuous(seq16, 50, 99999, 0)
agg16 = Counter()
for *_, p, f in tr16:
    agg16[p] += f
assert dict(agg16) == {20500: 2000, 21000: 2000} and [(o['id'], o['q']) for o in bb16] == [('b910', 2000)]
# Câu 23: lệnh nào chờ trước thì giá khớp là giá lệnh đó
t1, *_ = continuous([dict(id='s', side='S', p=101000, q=1000), dict(id='b', side='B', p=102000, q=1000)], 100, 10**6, 0)
t2, *_ = continuous([dict(id='b', side='B', p=102000, q=1000), dict(id='s', side='S', p=101000, q=1000)], 100, 10**6, 0)
assert t1[0][2] == 101000 and t2[0][2] == 102000          # TH1 thấp hơn TH2
# Câu 17: cổ tức tiền 7,5% × mệnh giá 10.000 = 750; thưởng 2:1 (2 cp cũ được 1 cp mới)
assert (54000 - 750) / Fr(3, 2) == 35500
assert 54000 - 750 == 53250 and 54000 / Fr(3, 2) - 750 == 35250 and 54000 / Fr(3, 2) == 36000   # các phương án nhiễu
# Câu 18: (40 − 30) × 100 + 2 × 100
assert (40 - 30) * 100 + 2 * 100 == 1200
# Câu 19, 20: MP bán khớp giá mua cao nhất, MP mua khớp giá bán thấp nhất
assert max([90000, 95000, 98000, 100000]) == 100000 and min([80000, 90000, 100000, 110000]) == 80000
# Câu 21: chỉ số giá trị vốn hóa, ngày gốc 1/2 = 100; C niêm yết 2/2 -> điều chỉnh hệ số chia
base, v_ab, v_c = 10 * 20 + 12 * 21, 10 * 21 + 12 * 25, 10 * 10
base_adj = Fr(base) * (v_ab + v_c) / v_ab                     # cổ phiếu mới không làm đổi chỉ số
idx21 = (v_ab + v_c) / base_adj * 100
assert round(float(idx21), 2) == 112.83 and idx21 == Fr(v_ab, base) * 100
assert round((v_ab + v_c) / base * 100, 2) == 134.96 and round((v_ab + v_c) / (base + v_c) * 100, 2) == 110.51  # cách sai
# Câu 24: NAV quỹ đóng
sec24 = 1000 * 35000 + 20500 * 34800 + 14000 * 44000 + 4200 * 31500
nav24 = sec24 + 3_300_000 - 500_000_000
assert sec24 == 1_496_700_000 and nav24 == 1_000_000_000 and nav24 / 2_000_000 == 500
# Câu 26: lưu hành = đã phát hành − cổ phiếu quỹ
assert 3_000_000 - 2_000_000 == 1_000_000
print(f"Câu 16: {dict(agg16)}; Câu 21: {float(idx21):.4f} (không điều chỉnh: 134,96; cộng C vào gốc: 110,51); "
      f"Câu 24: CK {vn(sec24)}, NAV {vn(nav24)}")

# ======================= 4. Câu tương ứng của ngân hàng =======================
# C1-015 (ATO, hòa KL -> gần giá TC)
P, V, _ = auction([O('a', None, 2000), O('b1', 25200, 3000), O('b2', 25100, 3000), O('b3', 25000, 3000), O('b4', 24900, 3000), O('b5', 24800, 1000)],
                  [O('s', None, 1000), O('s1', 24800, 1000), O('s2', 24900, 1000), O('s3', 25000, 1000), O('s4', 25100, 1000), O('s5', 25200, 2000)], 25000)
assert (P, V) == (25100, 5000)
# C1-016 (trần/sàn, bước 50)
assert band(25350, 7, 50) == (27100, 23600)
# C5-015 (giá mua tốt nhất sau ATO)
bv = [O('ato', None, 2000)] + [O(f'b{p}', p, q) for p, q in zip([60300, 60200, 60100, 60000, 59900], [1000, 2000, 3000, 2500, 1500])]
sv = [O('ato', None, 1500)] + [O(f's{p}', p, q) for p, q in zip([60300, 60200, 60100, 60000, 59900], [2500, 3000, 2000, 1500, 1000])]
P, V, _ = auction(bv, sv, 60000)
fb = allocate(bv, True, P, V)
assert (P, V) == (60100, 6000) and fb['b60100'] == 1000            # còn 2.000 chờ mua tại 60.100
# C5-016 (ATC, ưu tiên thời gian: K khớp 500)
bv = [O('atc', None, 1500), O('b412', 41200, 2500), O('H', 41100, 2500, 1432), O('K', 41100, 1500, 1435), O('b410', 41000, 3000)]
sv = [O('atc', None, 1000), O('s410', 41000, 4000), O('s411', 41100, 2000), O('s412', 41200, 2000)]
P, V, _ = auction(bv, sv, 41000)
assert (P, V) == (41100, 7000) and allocate(bv, True, P, V)['K'] == 500
# C5-018 (MP mua: phần còn lại thành LO 32.400)
c18 = band(32300, 7, 50)
_, bb, _ = continuous([dict(id='mp', side='B', p=None, q=4000)], 50, *c18, asks=[O('x', 32300, 1000, 0), O('y', 32350, 1500, 1)])
assert c18 == (34550, 30050) and [(o['p'], o['q']) for o in bb] == [(32400, 1500)]
# C1-014 (giá lệnh chờ, ưu tiên giá rồi thời gian)
tr, *_ = continuous([dict(id='s', side='S', p=25000, q=2500)], 50, 10**6, 0,
                    bids=[O('A', 25000, 2000, 1), O('B', 25000, 5000, 3), O('C', 25050, 1000, 5)])
assert [(t[1], t[2], t[3]) for t in tr] == [('C', 25050, 1000), ('A', 25000, 1500)]
# C5-017 (LO mua 18.500 quét 2 mức giá)
tr, *_ = continuous([dict(id='b', side='B', p=18500, q=7000)], 50, 10**6, 0,
                    asks=[O('x', 18450, 3000, 0), O('y', 18500, 2000, 1), O('z', 18550, 5000, 2)])
assert sum(p * f for *_, p, f in tr) == 92_350_000
# C1-061, C6-031, C1-023, C7-007, C2-006, C2-070, C6-013/C3-084
assert (39000 - 1500) / Fr(6, 5) == 31250
assert Fr(2_583_000) / (Fr(2_400_000, 1200) * Fr(2_520_000, 2_400_000)) == 1230
assert (8.6 + 120 + 25 + 0.4 - 3 - 1) * 1e9 / 1e7 == 15000
assert Fr(1_260 - 60, 80) * 1000 == 15000 and Fr(15000 - 12600, 15000) == Fr(16, 100)
assert Fr(46000 - 40000 + 2000, 40000) == Fr(20, 100)
assert Fr(30000) / (Fr(1_200_000, 60)) == Fr(3, 2)                # P/B, 60 triệu cp lưu hành
assert ((49800 - 45000) // 2 - 1200) * 20000 == 24_000_000
print("Câu tương ứng của ngân hàng: mọi con số khớp")

# ======================= 5. Câu mới =======================
Q = []
def add(topic, level, q, correct, wrong, e, basis, quote="", src="", part="CM", subject="CB"):
    assert len(wrong) == 3 and len({correct, *wrong}) == 4, q[:40]
    Q.append(dict(topic=topic, level=level, q=q, correct=correct, wrong=wrong, e=e, basis=basis,
                  quote=quote, src=src, part=part, subject=subject))

# C12-001 – Câu 02, 10, 26: cổ phiếu được phép phát hành / đã phát hành / quỹ / lưu hành; cổ tức mỗi cổ phiếu
iss, tre, auth, div, ni = 6_000_000, 1_500_000, 10_000_000, 9_000_000_000, 12_000_000_000
out_sh = iss - tre
dps = div / out_sh
assert (out_sh, dps, div / iss, div / auth, round(ni / out_sh)) == (4_500_000, 2000, 1500, 900, 2667)
add(T_CC, 3,
    "Điều lệ của công ty niêm yết K cho phép phát hành tối đa 10.000.000 cổ phiếu phổ thông. K đã phát hành "
    "6.000.000 cổ phiếu, trong đó có 1.500.000 cổ phiếu quỹ do K mua lại trước năm 2021 và chưa bán ra; K không "
    "có cổ phiếu ưu đãi. Năm N, K có lợi nhuận sau thuế 12 tỷ đồng và Đại hội đồng cổ đông quyết định dùng "
    "9 tỷ đồng trả cổ tức bằng tiền. Cổ tức mỗi cổ phiếu cổ đông nhận được là:",
    "2.000 đồng", ["1.500 đồng", "900 đồng", "2.667 đồng"],
    "Cổ phiếu quỹ là cổ phiếu đã phát hành được chính tổ chức phát hành mua lại; không được nhận cổ tức, không có "
    "quyền biểu quyết. Cổ phiếu đang lưu hành = 6.000.000 − 1.500.000 = 4.500.000 cổ phiếu (10.000.000 chỉ là số "
    "được phép phát hành theo điều lệ). Cổ tức mỗi cổ phiếu = 9.000.000.000 / 4.500.000 = 2.000 đồng. Chia cho số "
    "đã phát hành (gồm cả cổ phiếu quỹ) ra 1.500 đồng; chia cho số được phép phát hành ra 900 đồng; dùng lợi nhuận "
    "sau thuế thay cho tổng cổ tức ra 2.667 đồng (đó là EPS). Lưu ý: từ năm 2021, công ty đại chúng mua lại cổ "
    "phiếu theo khoản 1, điểm a khoản 2 Điều 37 Luật Chứng khoán phải giảm vốn điều lệ tương ứng (khoản 5), nên "
    "cổ phiếu quỹ chủ yếu còn ở các đợt mua lại trước năm 2021.",
    GT + "Cổ phiếu được phép phát hành, đã phát hành, đang lưu hành, cổ phiếu quỹ; cổ tức mỗi cổ phiếu; "
    "khoản 5 Điều 37 Luật Chứng khoán (VBHN 102/VBHN-VPQH năm 2026)")

# C12-002 – Câu 07: lệnh dừng để mua bảo vệ vị thế bán khống
stop = 60000 * 115 // 100
assert stop == 69000 and 60000 * 85 // 100 == 51000 and (stop - 60000) * 2000 == 18_000_000
add(T_TC, 2,
    "Giả sử thị trường cho phép bán khống và công ty chứng khoán nhận lệnh dừng (stop order). Nhà đầu tư vừa bán "
    "khống 2.000 cổ phiếu Z ở giá 60.000 đồng và muốn tự động đóng vị thế nếu mức lỗ lên tới 15% giá bán. Lệnh nên "
    "đặt ngay là:",
    "Lệnh dừng để mua 2.000 cổ phiếu, giá dừng 69.000 đồng",
    ["Lệnh dừng để bán 2.000 cổ phiếu, giá dừng 51.000 đồng",
     "Lệnh giới hạn mua 2.000 cổ phiếu, giá 69.000 đồng",
     "Lệnh dừng để mua 2.000 cổ phiếu, giá dừng 51.000 đồng"],
    "Người bán khống lỗ khi giá tăng, nên phải mua lại cổ phiếu để đóng vị thế khi giá tăng tới ngưỡng chịu lỗ: "
    "60.000 × (1 + 15%) = 69.000 đồng. Lệnh dừng để mua đặt cao hơn giá thị trường, chỉ được kích hoạt thành lệnh "
    "mua khi giá tăng chạm 69.000 đồng; lỗ dự kiến (69.000 − 60.000) × 2.000 = 18.000.000 đồng, chưa tính trượt giá. "
    "Lệnh giới hạn mua giá 69.000 sẽ khớp ngay ở giá bán hiện có quanh 60.000 nên đóng vị thế luôn; lệnh dừng để bán "
    "dùng bảo vệ vị thế mua; 51.000 là mức giá có lãi của vị thế bán khống, không phải ngưỡng lỗ. Ở Việt Nam nhà đầu "
    "tư chỉ được bán chứng khoán đã có trên tài khoản, trừ các trường hợp khoản 3 Điều 7 Thông tư 120/2020/TT-BTC; "
    "lệnh dừng không phải loại lệnh của Sở mà là lệnh điều kiện do một số công ty chứng khoán cung cấp, nên đề nêu "
    "dưới dạng giả sử.",
    GT + "Lệnh dừng (stop order) và bán khống; khoản 3 Điều 7, Điều 11 Thông tư 120/2020/TT-BTC (VBHN 08/VBHN-BTC năm 2026)")

# C12-003 – Câu 29: lệnh dừng để bán đặt thấp hơn giá thị trường
assert 45000 - 40000 == 5000
add(T_TC, 2,
    "Giả sử công ty chứng khoán nhận lệnh dừng (stop order). Nhà đầu tư đang nắm giữ cổ phiếu Y mua giá 40.000 đồng, "
    "giá thị trường hiện là 48.000 đồng. Nhà đầu tư chưa muốn bán ngay nhưng muốn tự động bán để giữ phần lớn khoản "
    "lãi nếu giá đảo chiều giảm. Cách đặt lệnh phù hợp là:",
    "Lệnh dừng để bán, giá dừng 45.000 đồng, thấp hơn giá thị trường",
    ["Lệnh dừng để bán, giá dừng 51.000 đồng, cao hơn giá thị trường",
     "Lệnh giới hạn bán, giá 45.000 đồng, thấp hơn giá thị trường",
     "Lệnh dừng để mua, giá dừng 45.000 đồng, thấp hơn giá thị trường"],
    "Lệnh dừng để bán được đặt dưới giá thị trường hiện hành; khi giá giảm chạm giá dừng 45.000 đồng, lệnh được kích "
    "hoạt thành lệnh bán, giữ lại khoảng 45.000 − 40.000 = 5.000 đồng lãi mỗi cổ phiếu (chưa tính trượt giá). Giá dừng "
    "bán cao hơn giá thị trường sẽ kích hoạt ngay (bán luôn); lệnh giới hạn bán giá 45.000 đồng khớp ngay với lệnh mua "
    "tốt nhất quanh 48.000 đồng; lệnh dừng để mua dùng để bảo vệ vị thế bán khống, được đặt cao hơn giá thị trường.",
    GT + "Lệnh dừng (stop order): lệnh dừng để bán đặt thấp hơn, lệnh dừng để mua đặt cao hơn giá thị trường")

# C12-004 – Câu 08: quyền chọn kiểu Mỹ
add(T_CC, 1,
    "Nhà đầu tư trả phí để mua một quyền chọn mua kiểu Mỹ trên 2.000 cổ phiếu Q, giá thực hiện 30.000 đồng/cổ phiếu, "
    "thời hạn 3 tháng. Quyền và nghĩa vụ của nhà đầu tư theo hợp đồng này là:",
    "Có quyền mua 2.000 cổ phiếu Q giá 30.000 đồng vào bất kỳ ngày nào đến hết ngày đáo hạn",
    ["Có quyền mua 2.000 cổ phiếu Q giá 30.000 đồng, nhưng chỉ vào đúng ngày đáo hạn",
     "Có quyền bán 2.000 cổ phiếu Q giá 30.000 đồng vào bất kỳ ngày nào đến hết ngày đáo hạn",
     "Có nghĩa vụ phải mua 2.000 cổ phiếu Q giá 30.000 đồng vào ngày đáo hạn"],
    "Quyền chọn kiểu Mỹ cho phép người mua thực hiện quyền vào bất kỳ thời điểm nào từ khi mua đến hết ngày đáo hạn; "
    "kiểu châu Âu chỉ được thực hiện vào ngày đáo hạn. Khoản 11 Điều 4 Luật Chứng khoán: hợp đồng quyền chọn xác "
    "nhận quyền của người mua và nghĩa vụ của người bán, giao dịch theo giá thực hiện \"tại thời điểm trước hoặc vào "
    "ngày đã xác định trong tương lai\". Người mua quyền không có nghĩa vụ phải mua (cam kết bắt buộc là đặc điểm của "
    "hợp đồng kỳ hạn, tương lai); quyền bán theo giá thực hiện là quyền chọn bán.",
    GT + "Hợp đồng quyền chọn kiểu Mỹ và kiểu châu Âu; khoản 11 Điều 4 Luật Chứng khoán (VBHN 102/VBHN-VPQH năm 2026)",
    quote="Hợp đồng quyền chọn là loại chứng khoán phái sinh, xác nhận quyền của người mua và nghĩa vụ của người bán",
    src=LCK)

# C12-005 – Câu 28: bản cáo bạch
add(T_SC, 1,
    "Trong hồ sơ đăng ký chào bán cổ phiếu ra công chúng, tài liệu công khai thông tin chính xác, trung thực, khách "
    "quan về tổ chức phát hành và đợt chào bán, là căn cứ chính để nhà đầu tư quyết định đăng ký mua, là:",
    "Bản cáo bạch của tổ chức phát hành",
    ["Báo cáo tài chính năm đã kiểm toán", "Giấy đăng ký chào bán ra công chúng", "Phương án phát hành, sử dụng vốn"],
    "Khoản 23 Điều 4 Luật Chứng khoán: bản cáo bạch là tài liệu hoặc dữ liệu điện tử công khai những thông tin chính "
    "xác, trung thực, khách quan liên quan đến việc chào bán hoặc niêm yết chứng khoán của tổ chức phát hành. Theo "
    "Điều 19, bản cáo bạch tổng hợp thông tin về tổ chức phát hành, đợt chào bán (rủi ro, phương án phát hành và sử "
    "dụng vốn) và báo cáo tài chính 02 năm gần nhất, nên quan trọng nhất với nhà đầu tư. Giấy đăng ký, báo cáo tài "
    "chính, nghị quyết thông qua phương án phát hành là các tài liệu khác trong hồ sơ (Điều 18).",
    "Khoản 23 Điều 4, Điều 18, Điều 19 Luật Chứng khoán (VBHN 102/VBHN-VPQH năm 2026); " + GT + "Bản cáo bạch",
    quote="Bản cáo bạch là tài liệu hoặc dữ liệu điện tử công khai những thông tin chính xác, trung thực, khách quan "
          "liên quan đến việc chào bán hoặc niêm yết chứng khoán của tổ chức phát hành.",
    src=LCK)

# C12-006 – Câu 32: khớp lệnh tập trung vs giao dịch thỏa thuận (câu Luật)
add("Giao dịch chứng khoán", 1,
    "Theo Thông tư 120/2020/TT-BTC (VBHN 08/VBHN-BTC năm 2026), phương thức giao dịch thỏa thuận trên hệ thống giao "
    "dịch chứng khoán được thực hiện theo nguyên tắc nào?",
    "Các bên tham gia giao dịch tự thỏa thuận, thống nhất các nội dung giao dịch",
    ["Hệ thống so khớp lệnh mua, bán theo nguyên tắc ưu tiên về giá và thời gian",
     "Sở giao dịch chứng khoán ấn định giá thực hiện cho từng giao dịch thỏa thuận",
     "Công ty chứng khoán xác định giá theo giá đóng cửa của ngày giao dịch liền trước"],
    "Điểm b khoản 1 Điều 3: phương thức giao dịch thỏa thuận được thực hiện theo nguyên tắc các bên tham gia giao dịch "
    "tự thỏa thuận, thống nhất các nội dung giao dịch; còn phương thức khớp lệnh tập trung phải bảo đảm nguyên tắc ưu "
    "tiên về giá và thời gian (điểm a). Vì vậy điểm khác biệt cơ bản giữa hai phương thức là cách xác định giá: khớp "
    "lệnh do hệ thống so khớp, thỏa thuận do hai bên tự thống nhất. Thời gian, biên độ, khối lượng của giao dịch thỏa "
    "thuận do quy chế giao dịch của Sở giao dịch chứng khoán Việt Nam quy định (khoản 3 Điều 3).",
    "Điểm a, b khoản 1 và khoản 3 Điều 3 Thông tư 120/2020/TT-BTC (VBHN 08/VBHN-BTC năm 2026)",
    quote="Phương thức giao dịch thỏa thuận trên hệ thống giao dịch chứng khoán được thực hiện theo nguyên tắc các bên "
          "tham gia giao dịch tự thỏa thuận, thống nhất các nội dung giao dịch.",
    src=TT120, part="LUAT", subject="LU")

# C12-007 – Bài tập 02, Câu 16, 23: xử lý lệnh theo thứ tự nhập, giá khớp = giá lệnh chờ, lệnh MP
c7 = band(45000, 7, 50)
seq7 = [dict(id='P', side='B', p=44800, q=2000), dict(id='Q', side='S', p=45300, q=1500),
        dict(id='R', side='B', p=45000, q=1000), dict(id='S', side='B', p=None, q=500),
        dict(id='T', side='S', p=None, q=2500), dict(id='U', side='B', p=45500, q=1200)]
tr7, bb7, aa7 = continuous(seq7, 50, *c7)
assert c7 == (48150, 41850)
assert filled(tr7, 'U') == [(45300, 1000)] and [(o['id'], o['p'], o['q']) for o in bb7] == [('P', 44800, 500), ('U', 45500, 200)]
assert filled(tr7, 'S') == [(45300, 500)] and filled(tr7, 'T') == [(45000, 1000), (44800, 1500)] and not aa7
add(T_TC, 3,
    "Giả sử trong phiên khớp lệnh liên tục: lệnh được so khớp ngay khi nhập theo ưu tiên giá rồi thời gian, giá thực "
    "hiện là giá của lệnh đối ứng đang chờ trên sổ lệnh; lệnh MP khớp lần lượt với các mức giá tốt nhất của phía đối "
    "ứng. Cổ phiếu G có giá tham chiếu 45.000 đồng, sổ lệnh ban đầu trống; các lệnh được nhập lần lượt: (1) P mua LO "
    "2.000 cổ phiếu giá 44.800; (2) Q bán LO 1.500 cổ phiếu giá 45.300; (3) R mua LO 1.000 cổ phiếu giá 45.000; "
    "(4) S mua MP 500 cổ phiếu; (5) T bán MP 2.500 cổ phiếu; (6) U mua LO 1.200 cổ phiếu giá 45.500. Kết quả của U là:",
    "Khớp 1.000 cổ phiếu giá 45.300 đồng; 200 cổ phiếu chờ mua giá 45.500 đồng",
    ["Khớp 1.200 cổ phiếu giá 45.300 đồng; không còn khối lượng chờ khớp",
     "Khớp 1.000 cổ phiếu giá 45.500 đồng; 200 cổ phiếu chờ mua giá 45.500 đồng",
     "Khớp 1.200 cổ phiếu giá 45.500 đồng; không còn khối lượng chờ khớp"],
    "Xử lý theo thứ tự nhập: (1) P chờ mua 44.800. (2) Q chờ bán 45.300 vì giá mua tốt nhất chỉ 44.800. (3) R chờ mua "
    "45.000. (4) S mua MP khớp 500 cổ phiếu với Q tại 45.300, Q còn 1.000. (5) T bán MP khớp 1.000 với R tại 45.000 "
    "rồi 1.500 với P tại 44.800, P còn 500 chờ mua. (6) U mua 45.500 ≥ giá bán tốt nhất 45.300 nên khớp 1.000 cổ phiếu "
    "còn lại của Q tại giá lệnh chờ 45.300; 200 cổ phiếu còn lại chờ mua tại 45.500. Bỏ qua lệnh của S cho kết quả "
    "1.200 cổ phiếu; lấy giá đặt của U (45.500) là sai vì giá khớp là giá của lệnh đối ứng đã chờ trên sổ.",
    GT + "Khớp lệnh liên tục: ưu tiên giá, thời gian; giá thực hiện là giá lệnh đối ứng đang chờ; lệnh thị trường "
    "(quy tắc giao dịch là giả định nêu trong đề)")

# kiểm tra trích dẫn khớp nguyên văn văn bản
loose = lambda s: re.sub(r"[\W_]+", "", unicodedata.normalize("NFC", s).lower())
for x in Q:
    if x['quote']:
        assert loose(x['quote']) in loose(open(VB + x['src'], encoding='utf-8').read()), x['quote'][:40]

# ======================= Gán id, vị trí đáp án =======================
pos = [0, 1, 2, 3, 0, 1, 2]
random.Random(20261108).shuffle(pos)
out = []
for i, (x, a) in enumerate(zip(Q, pos), 1):
    o = list(x['wrong']); o.insert(a, x['correct'])
    if x['level'] == 3:
        assert re.search(r"\d[\d.,]*", x['correct']).group(0) in x['e'], i
    lens = [len(s) for s in o]
    assert max(lens) <= 1.6 * min(lens), (i, lens)
    assert not re.search(r"(phương án|đáp án|chọn|câu)\s+[A-D]\b", x['e']), i
    out.append(dict(id=f"C12-{i:03d}", part=x['part'], subject=x['subject'], topic=x['topic'], level=x['level'],
                    q=x['q'], o=o, a=a, e=x['e'], basis=x['basis'], quote=x['quote'], src=x['src'], as_of="2026-11"))
with open(OUT, 'w', encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False, indent=1)
print("wrote", len(out), "| a:", dict(sorted(Counter(x['a'] for x in out).items())),
      "| môn:", dict(Counter(x['subject'] for x in out)), "| level:", dict(sorted(Counter(x['level'] for x in out).items())))
