# Soát số liệu ví dụ trong thẻ PT/BC/BL/QU (chạy: python3 -I kiem_so.py)
import math
close = lambda a, b, t=5e-3: abs(a - b) < t
# PT-03 FV niên kim 10 triệu, 8%, 4 kỳ
assert close(10 * ((1.08**4 - 1) / 0.08), 45.06, 0.01)
# PT-05 vĩnh viễn 1.200/10%
assert close(1200 / 0.10, 12000)
# PT-06 EAR 10% ghép quý
assert close((1 + 0.10 / 4)**4 - 1, 0.1038, 1e-4)
# PT-07 lãi trả trước 10%
assert close(0.10 / 0.90, 0.1111, 1e-4)
# PT-14 rho=-1
assert close(0.20 / (0.30 + 0.20), 0.40, 1e-9)
# PT-16 beta danh mục
assert close(0.3 * 1.4 + 0.2 * 0.9 + 0.5 * 0, 0.60, 1e-9)
# PT-29 MD 5, +50bp
assert close(-5 * 0.005, -0.025, 1e-12)
# PT-37 P/B hợp lý = (ROE-g)/(r-g): kiểm bằng Gordon
B0, ROE, b, r = 100, 0.15, 0.6, 0.12
g = ROE * b; E1 = ROE * B0; D1 = E1 * (1 - b); P0 = D1 / (r - g)
assert close(P0 / B0, (ROE - g) / (r - g), 1e-9) and close(P0 / B0, 2.0, 1e-9)
# PT-39 FCFF = FCFE + lãi vay(1-t) - vay ròng
NI, D, capex, dwc, I, t, nb = 80, 30, 50, 10, 20, 0.2, 15
EBIT = NI / (1 - t) + I
FCFF = EBIT * (1 - t) + D - capex - dwc
FCFE = NI + D - capex - dwc + nb
assert close(FCFF, FCFE + I * (1 - t) - nb, 1e-9)
# PT-48 Fisher
assert close(1.09 / 1.04 - 1, 0.0481, 1e-4)
# BC-22 hệ số nhân vốn chủ khi Nợ/TTS 60%
assert close(1 / (1 - 0.6), 2.5, 1e-9)
# BC-45 hiện hành 2,5; nhanh 0,4 => HTK & TSNH khác chiếm 84% TSNH
assert close((2.5 - 0.4) / 2.5, 0.84, 1e-9)
# BC-49 trả nợ ngắn hạn bằng tiền
assert close(350 / 150, 2.33, 0.01)
# BL-34 giá trị quyền: N=2,5 (5 quyền mua 2 CP), P0=25.000, S=18.000
N, P0, S = 2.5, 25000, 18000
Px = (N * P0 + S) / (N + 1)
assert close((P0 - S) / (N + 1), 2000) and close((Px - S) / N, 2000) and close(P0 - Px, 2000)
# BL-47 phần bù kiểm soát 25% <=> chiết khấu thiểu số 20%
assert close(1 - 1 / 1.25, 0.20, 1e-9)
# BL-31 M&M có thuế: WACC giảm khi tăng nợ (ví dụ)
rU, rD, t = 0.12, 0.06, 0.2
for de in (0.0, 0.5, 1.0):
    rE = rU + (rU - rD) * (1 - t) * de
    wacc = (rE + rD * (1 - t) * de) / (1 + de)
    print("D/E", de, "rE", round(rE, 4), "WACC", round(wacc, 4))
# QU-46 phí 2 và 20: tài sản 100, lãi gộp 18
fee_m = 2; fee_p = 0.2 * (18 - fee_m)
assert close(fee_m + fee_p, 5.2) and close(18 - fee_m - fee_p, 12.8)
# QU-45 M² = rf + Sharpe_p × σm
rf, Rp, sp, sm = 0.04, 0.15, 0.20, 0.16
M2 = rf + (Rp - rf) / sp * sm
assert close(M2, 0.128, 1e-9)
# QU-22 CPPI ví dụ: V=100, sàn 80, m=3 => cổ phiếu 60
assert close(3 * (100 - 80), 60)
print("OK: mọi ví dụ số trong thẻ khớp")
