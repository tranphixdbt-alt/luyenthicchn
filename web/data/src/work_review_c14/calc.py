# Tính lại độc lập các câu tính toán C14 (soát chéo). Chạy: python3 -I calc.py
from datetime import date, timedelta
from decimal import Decimal as D

# C14-002: đấu thầu kết hợp, đơn giá; phần không cạnh tranh tối đa 30% khối lượng gọi thầu
goi, nc, cap_rate = 2000, 800, D('3.30')
bids = [(D('3.05'),300),(D('3.10'),500),(D('3.15'),400),(D('3.20'),600),(D('3.35'),500)]
nc_ok = min(nc, goi*30//100); rem = goi - nc_ok
alloc = []
for r, v in sorted(bids):
    if r > cap_rate or rem == 0: continue
    take = min(v, rem); alloc.append((r, take)); rem -= take
assert nc_ok == 600 and alloc[-1] == (D('3.20'), 200) and rem == 0
wavg = sum(r*v for r, v in alloc)/sum(v for _, v in alloc)
print('C14-002', alloc[-1], 'bình quân (đa giá, sai):', round(wavg, 4))
# không cắt 30%: 1200 cạnh tranh -> dừng ở 3,15% với 400
rem = goi - nc; last = None
for r, v in sorted(bids):
    if r > cap_rate or rem == 0: continue
    take = min(v, rem); last = (r, take); rem -= take
assert last == (D('3.15'), 400)

# C14-006 (sửa): 1.500.000 TP, giá thị trường 102.400, tỷ lệ phòng ngừa rủi ro 4%
q, p, face, h = 1_500_000, 102_400, 100_000, D('0.04')
mv = q*p
key = mv*(1+h); opts = {'key': key, 'bo_ty_le': mv, 'menh_gia': q*face*(1+h), 'chia_1_tru_h': mv/(1-h)}
assert key == 159_744_000_000 and opts['chia_1_tru_h'] == 160_000_000_000 and opts['menh_gia'] == 156_000_000_000
print('C14-006', {k: f'{int(v):,}'.replace(',', '.') for k, v in opts.items()}, 'hạng của đáp án (tăng dần):', sorted(opts.values()).index(key)+1)

# C14-014: lãi coupon năm nhận trong thời hạn repo
coupon = 200_000*100_000*D('0.042'); assert coupon == 840_000_000
print('C14-014 coupon', coupon, '30 ngày/365 (sai):', round(coupon*30/365))
d1 = date(2027, 3, 10); d2 = d1 + timedelta(days=30)
assert d1.weekday() == 2 and d2 == date(2027, 4, 9) and d2.weekday() == 4
cp = date(2027, 3, 25); assert cp.weekday() == 3
def add_wd(start, n, hol=()):
    d = start
    while n:
        d += timedelta(days=1)
        if d.weekday() < 5 and d not in hol: n -= 1
    return d
dl = add_wd(cp, 5); print('C14-014 hạn hoàn trả ngoài hệ thống (không ngày lễ):', dl)
assert dl < d2

# C14-018: 15 ngày làm việc kể từ ngày CBTT 17/12/2026, nghỉ T7, CN, 01/01/2027
cb = date(2026, 12, 17); hol = {date(2027, 1, 1)}
assert cb.weekday() == 3 and date(2027, 1, 1).weekday() == 4
k15 = add_wd(cb, 15, hol); assert k15 == date(2027, 1, 8)
k15_lam = add_wd(cb, 15); k15_tinh_ca = add_wd(cb - timedelta(days=1), 15, hol)
k10 = add_wd(cb, 10, hol); k20 = add_wd(cb, 20, hol); k5 = add_wd(cb, 5, hol)
print('C14-018 key', k15, '| coi 01/01 làm việc', k15_lam, '| tính cả ngày CBTT', k15_tinh_ca, '| 10 ngày', k10, '| 20 ngày (15+05)', k20, '| 05 ngày', k5)
assert k15_lam == k15_tinh_ca == date(2027, 1, 7) and k10 == date(2026, 12, 31) and k20 == date(2027, 1, 15)
