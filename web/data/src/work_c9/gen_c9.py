# Sinh 40 câu CM (PT 26, MG 14) -> ../cm_9.json. Mọi phép tính được tính lại và assert.
import json, random, re
from collections import Counter

OUT = '/home/user/cchn_moi/web/data/src/cm_9.json'
SRC = 'Giáo trình SRTC (khung chương trình)'
GT_PT = 'Giáo trình Phân tích và đầu tư chứng khoán (UBCKNN/SRTC) – '
GT_MG = 'Giáo trình Môi giới và tư vấn đầu tư chứng khoán (UBCKNN/SRTC) – '
Q = []


def vn(x, d=2):
    s = f"{abs(x):,.{d}f}".replace(',', 'X').replace('.', ',').replace('X', '.')
    return ('−' if x < 0 else '') + s


def pct(x, d=2):
    return vn(x * 100, d) + '%'


def add(subj, topic, level, q, correct, wrong, e, basis, nums=None):
    """nums = giá trị số [đáp án, nhiễu...] để kiểm tra thứ hạng đáp án trong các phương án."""
    assert len(wrong) == 3 and len({correct, *wrong}) == 4, q[:40]
    if nums:
        assert len(set(nums)) == 4
    Q.append(dict(subject=subj, topic=topic, level=level, q=q, correct=correct, wrong=wrong, e=e,
                  basis=(GT_PT if subj == 'PT' else GT_MG) + basis, nums=nums))


T_TQ = "Tổng quan về phân tích và đầu tư"
T_SL = "Mức sinh lời và rủi ro"
T_HQ = "Thị trường hiệu quả và tài chính hành vi"
T_CP = "Phân tích và định giá cổ phiếu"
T_TP = "Phân tích và định giá trái phiếu"
M_CP = "Giao dịch cổ phiếu trên thị trường chứng khoán"
M_TP = "Giao dịch trái phiếu trên thị trường chứng khoán"

# ======================= PT: Giá trị thời gian của tiền =======================
ear = (1 + 0.10 / 4) ** 4 - 1
ear_m = (1 + 0.10 / 12) ** 12 - 1
assert pct(ear) == "10,38%" and pct(ear_m) == "10,47%"
add('PT', T_TQ, 3,
    "Một khoản tiền gửi có lãi suất danh nghĩa 10%/năm, tiền lãi được ghép vào gốc theo quý. Lãi suất thực tế năm (EAR) của khoản tiền gửi này là bao nhiêu?",
    pct(ear), ["10,00%", pct(ear_m), "2,50%"],
    f"Lãi suất mỗi quý = 10%/4 = 2,5%. EAR = (1 + 0,025)^4 − 1 = {pct(ear)}. Lỗi thường gặp: coi lãi suất danh nghĩa là lãi suất thực tế (10,00%), ghép lãi theo tháng thay vì theo quý ({pct(ear_m)}), lấy lãi suất một quý mà quên quy ra năm (2,50%).",
    "Lãi suất danh nghĩa (APR) và lãi suất thực tế năm: EAR = (1 + APR/m)^m − 1", [ear, .10, ear_m, .025])

add('PT', T_TQ, 1,
    "Giá trị hiện tại của một dòng tiền đều C nhận vào cuối mỗi năm, kéo dài vĩnh viễn (niên kim vĩnh viễn), với lãi suất chiết khấu r > 0, được tính bằng công thức nào?",
    "PV = C/r", ["PV = C × r", "PV = C/(1 + r)", "PV = C × (1 + r)/r"],
    "Niên kim vĩnh viễn cuối kỳ: PV = C/(1 + r) + C/(1 + r)² + … = C/r. C/(1 + r) chỉ là giá trị hiện tại của khoản tiền đầu tiên; C × (1 + r)/r là niên kim vĩnh viễn đầu kỳ (khoản đầu tiên nhận ngay).",
    "Giá trị hiện tại của niên kim vĩnh viễn")

fv = 10 * ((1.08 ** 4 - 1) / 0.08)
fv_simple = sum(10 * (1 + 0.08 * k) for k in range(4))
assert vn(fv) == "45,06" and vn(fv * 1.08) == "48,67" and vn(fv_simple) == "44,80"
add('PT', T_TQ, 2,
    "Nhà đầu tư gửi 10 triệu đồng vào cuối mỗi năm, liên tục trong 4 năm, lãi suất 8%/năm, ghép lãi hằng năm. Số tiền nhà đầu tư có ngay sau lần gửi cuối cùng là bao nhiêu?",
    vn(fv) + " triệu đồng", ["40,00 triệu đồng", vn(fv_simple) + " triệu đồng", vn(fv * 1.08) + " triệu đồng"],
    f"FV niên kim cuối kỳ = 10 × [(1,08^4 − 1)/0,08] = 10 × 4,5061 = {vn(fv)} triệu đồng. Lỗi thường gặp: không tính lãi (40,00), tính lãi đơn ({vn(fv_simple)}), coi là niên kim đầu kỳ ({vn(fv * 1.08)}).",
    "Giá trị tương lai của niên kim cuối kỳ: FV = A × [(1 + r)^n − 1]/r", [fv, 40, fv_simple, fv * 1.08])

pmt = 500 * 0.01 / (1 - 1.01 ** -24)
flat = 500 / 24 + 500 * 0.01
annual12 = 500 * 0.12 / (1 - 1.12 ** -2) / 12
assert vn(pmt) == "23,54" and vn(flat) == "25,83" and vn(annual12) == "24,65"
add('PT', T_TQ, 3,
    "Khách hàng vay 500 triệu đồng, lãi suất 12%/năm (tương đương 1%/tháng), trả góp đều vào cuối mỗi tháng trong 24 tháng, mỗi kỳ gồm cả gốc và lãi trên dư nợ còn lại. Số tiền phải trả mỗi tháng xấp xỉ bao nhiêu?",
    vn(pmt) + " triệu đồng", [vn(flat) + " triệu đồng", vn(annual12) + " triệu đồng", "20,83 triệu đồng"],
    f"PMT = PV × r/[1 − (1 + r)^(−n)] = 500 × 0,01/(1 − 1,01^(−24)) = {vn(pmt)} triệu đồng. Lỗi thường gặp: tính lãi trên gốc ban đầu cho cả 24 tháng (500/24 + 5 = {vn(flat)}), tính niên kim năm rồi chia 12 ({vn(annual12)}), bỏ qua lãi (500/24 = 20,83).",
    "Khoản trả góp đều (niên kim): PMT = PV × r/[1 − (1 + r)^(−n)]", [pmt, flat, annual12, 500 / 24])

pv3 = 50 / 0.1 / 1.1 ** 3
assert vn(pv3) == "375,66" and vn(500 / 1.1 ** 4) == "341,51" and vn(500 / 1.1 ** 2) == "413,22"
add('PT', T_TQ, 3,
    "Một khoản đầu tư mang lại 50 triệu đồng mỗi năm mãi mãi, khoản tiền đầu tiên nhận vào cuối năm thứ 4. Với lãi suất chiết khấu 10%/năm, giá trị hiện tại của khoản đầu tư là bao nhiêu?",
    vn(pv3) + " triệu đồng", ["500,00 triệu đồng", vn(500 / 1.1 ** 4) + " triệu đồng", vn(500 / 1.1 ** 2) + " triệu đồng"],
    f"Giá trị niên kim vĩnh viễn tại cuối năm 3 (một năm trước khoản đầu tiên) = 50/0,1 = 500 triệu đồng; chiết khấu về hiện tại: 500/1,1³ = {vn(pv3)} triệu đồng. Lỗi thường gặp: không chiết khấu (500,00), chiết khấu 4 năm ({vn(500 / 1.1 ** 4)}), chiết khấu 2 năm ({vn(500 / 1.1 ** 2)}).",
    "Giá trị hiện tại của niên kim vĩnh viễn trả chậm", [pv3, 500, 500 / 1.1 ** 4, 500 / 1.1 ** 2])

# ======================= PT: Mức sinh lời và rủi ro =======================
r6 = 0.05 + 1.3 * 0.06
assert pct(r6) == "12,80%"
add('PT', T_SL, 2,
    "Lãi suất phi rủi ro là 5%/năm, mức bù rủi ro thị trường [E(Rm) − Rf] là 6%/năm. Theo CAPM, lợi suất yêu cầu của cổ phiếu có hệ số beta 1,3 là bao nhiêu?",
    pct(r6), ["7,80%", "6,30%", "11,00%"],
    f"E(Ri) = Rf + β × [E(Rm) − Rf] = 5% + 1,3 × 6% = {pct(r6)}. Lỗi thường gặp: quên cộng Rf (1,3 × 6% = 7,80%), coi 6% là lợi suất thị trường rồi trừ Rf (5% + 1,3 × 1% = 6,30%), bỏ qua beta (5% + 6% = 11,00%).",
    "Mô hình CAPM: E(Ri) = Rf + βi × [E(Rm) − Rf]", [r6, .078, .063, .11])

add('PT', T_SL, 1,
    "Theo mô hình CAPM, một chứng khoán có hệ số beta bằng 1 sẽ có lợi suất yêu cầu bằng",
    "Lợi suất kỳ vọng của danh mục thị trường",
    ["Lãi suất phi rủi ro của thị trường", "Mức bù rủi ro của danh mục thị trường",
     "Tổng lãi suất phi rủi ro và lợi suất thị trường"],
    "Với β = 1: E(Ri) = Rf + 1 × [E(Rm) − Rf] = E(Rm). Chứng khoán có beta bằng 0 mới có lợi suất yêu cầu bằng lãi suất phi rủi ro.",
    "Mô hình CAPM và ý nghĩa hệ số beta")

rx, ry = 0.04 + 1.5 * 0.06, 0.04 + 0.7 * 0.06
assert pct(rx) == "13,00%" and pct(ry) == "8,20%" and 0.12 < rx and 0.09 > ry
add('PT', T_SL, 3,
    "Lãi suất phi rủi ro 4%, lợi suất kỳ vọng của danh mục thị trường 10%. Cổ phiếu X có beta 1,5, lợi suất kỳ vọng theo dự báo 12%; cổ phiếu Y có beta 0,7, lợi suất kỳ vọng theo dự báo 9%. Theo đường SML, nhận định nào đúng?",
    "X nằm dưới SML (bị định giá cao), Y nằm trên SML (bị định giá thấp)",
    ["X nằm trên SML (bị định giá thấp), Y nằm dưới SML (bị định giá cao)",
     "X và Y đều nằm trên SML vì lợi suất kỳ vọng đều cao hơn Rf",
     "X và Y đều bị định giá cao vì lợi suất kỳ vọng thấp hơn mức yêu cầu"],
    f"Lợi suất yêu cầu: X = 4% + 1,5 × 6% = {pct(rx)} > 12% (alpha = −1,00%) nên X nằm dưới SML, bị định giá cao; Y = 4% + 0,7 × 6% = {pct(ry)} < 9% (alpha = +0,80%) nên Y nằm trên SML, bị định giá thấp. Lỗi thường gặp: so trực tiếp với lợi suất thị trường 10% mà không điều chỉnh theo beta.",
    "Đường thị trường chứng khoán (SML): định giá cao/thấp theo alpha")

w_a = 0.20 / (0.30 + 0.20)
e9 = w_a * 0.14 + (1 - w_a) * 0.08
sd9 = abs(w_a * 0.30 - (1 - w_a) * 0.20)
w_inv = 0.2 ** 2 / (0.3 ** 2 + 0.2 ** 2)
e_inv = w_inv * 0.14 + (1 - w_inv) * 0.08
assert abs(w_a - 0.4) < 1e-12 and sd9 < 1e-12 and pct(e9) == "10,40%" and pct(e_inv) == "9,85%"
add('PT', T_SL, 3,
    "Cổ phiếu A có lợi suất kỳ vọng 14%, độ lệch chuẩn 30%; cổ phiếu B có lợi suất kỳ vọng 8%, độ lệch chuẩn 20%; hệ số tương quan giữa A và B là −1. Lợi suất kỳ vọng của danh mục gồm A và B có độ lệch chuẩn bằng 0 là bao nhiêu?",
    pct(e9), ["11,60%", "11,00%", pct(e_inv)],
    f"Với ρ = −1: σp = |wA × 30% − wB × 20%| = 0 ⇒ wA = 20/(30 + 20) = 40%, wB = 60%. E(Rp) = 0,4 × 14% + 0,6 × 8% = {pct(e9)}. Lỗi thường gặp: đảo tỷ trọng (60% A cho 11,60%), chia đều 50/50 (11,00%), dùng tỷ trọng theo phương sai như khi ρ = 0 ({pct(e_inv)}).",
    "Lợi suất và rủi ro danh mục hai tài sản; trường hợp tương quan hoàn hảo âm", [e9, .116, .11, e_inv])

var10 = 0.25 * 0.25 ** 2 + 0.25 * 0.15 ** 2 + 2 * 0.25 * (-0.009)
sd10 = var10 ** 0.5
sd_nocov = (0.25 * 0.25 ** 2 + 0.25 * 0.15 ** 2) ** 0.5
sd_sign = (0.25 * 0.25 ** 2 + 0.25 * 0.15 ** 2 + 2 * 0.25 * 0.009) ** 0.5
assert pct(sd10) == "12,94%" and pct(sd_nocov) == "14,58%" and pct(sd_sign) == "16,05%" and sd10 < 0.15
add('PT', T_SL, 3,
    "Danh mục đầu tư 50% vào cổ phiếu M (độ lệch chuẩn 25%) và 50% vào cổ phiếu N (độ lệch chuẩn 15%); hiệp phương sai giữa lợi suất M và N là −0,009. Độ lệch chuẩn của danh mục là bao nhiêu?",
    pct(sd10), [pct(sd_nocov), pct(sd_sign), "20,00%"],
    f"σp² = 0,5² × 0,25² + 0,5² × 0,15² + 2 × 0,5 × 0,5 × (−0,009) = 0,015625 + 0,005625 − 0,0045 = 0,01675 ⇒ σp = {pct(sd10)}, thấp hơn cả độ lệch chuẩn của N do hiệp phương sai âm. Lỗi thường gặp: bỏ qua hiệp phương sai ({pct(sd_nocov)}), cộng hiệp phương sai sai dấu ({pct(sd_sign)}), lấy bình quân gia quyền độ lệch chuẩn (20,00%).",
    "Phương sai danh mục: σp² = w₁²σ₁² + w₂²σ₂² + 2w₁w₂Cov(1,2)", [sd10, sd_nocov, sd_sign, .20])

b11 = (300 * 1.4 + 200 * 0.9 + 500 * 0) / 1000
assert vn(b11) == "0,60" and vn((300 * 1.4 + 200 * 0.9) / 500) == "1,20" and vn((1.4 + 0.9) / 3) == "0,77" and vn((1.4 + 0.9) / 2) == "1,15"
add('PT', T_SL, 2,
    "Danh mục 1.000 triệu đồng gồm: 300 triệu đồng cổ phiếu P (beta 1,4), 200 triệu đồng cổ phiếu Q (beta 0,9) và 500 triệu đồng tín phiếu Kho bạc (coi là tài sản phi rủi ro). Hệ số beta của danh mục là bao nhiêu?",
    vn(b11), ["1,20", "0,77", "1,15"],
    f"Beta tài sản phi rủi ro bằng 0. βp = 0,3 × 1,4 + 0,2 × 0,9 + 0,5 × 0 = 0,42 + 0,18 = {vn(b11)}. Lỗi thường gặp: bỏ tín phiếu khỏi mẫu số (600/500 = 1,20), bình quân giản đơn ba tài sản (0,77) hoặc hai cổ phiếu (1,15).",
    "Hệ số beta của danh mục: βp = Σ wi × βi", [b11, 1.2, (1.4 + 0.9) / 3, 1.15])

shx, shy = (0.14 - 0.04) / 0.18, (0.12 - 0.04) / 0.20
trx, try_ = (0.14 - 0.04) / 1.2, (0.12 - 0.04) / 0.8
assert shx > shy and try_ > trx and vn(shx) == "0,56" and vn(shy) == "0,40" and pct(trx) == "8,33%" and pct(try_) == "10,00%"
add('PT', T_SL, 3,
    "Lãi suất phi rủi ro 4%. Quỹ X: lợi suất 14%, độ lệch chuẩn 18%, beta 1,2. Quỹ Y: lợi suất 12%, độ lệch chuẩn 20%, beta 0,8. Kết luận nào đúng khi so sánh hai quỹ theo chỉ số Sharpe và chỉ số Treynor?",
    "Theo Sharpe quỹ X tốt hơn, theo Treynor quỹ Y tốt hơn",
    ["Theo Sharpe quỹ Y tốt hơn, theo Treynor quỹ X tốt hơn",
     "Quỹ X tốt hơn quỹ Y theo cả chỉ số Sharpe và Treynor",
     "Quỹ Y tốt hơn quỹ X theo cả chỉ số Sharpe và Treynor"],
    f"Sharpe = (R − Rf)/σ: X = 10%/18% = {vn(shx)}; Y = 8%/20% = {vn(shy)} ⇒ X tốt hơn. Treynor = (R − Rf)/β: X = 10%/1,2 = {pct(trx)}; Y = 8%/0,8 = {pct(try_)} ⇒ Y tốt hơn. Hai chỉ số cho kết quả khác nhau vì Sharpe dùng tổng rủi ro, Treynor chỉ dùng rủi ro hệ thống.",
    "Đánh giá hiệu quả danh mục: chỉ số Sharpe và chỉ số Treynor")

alpha = 0.10 - (0.04 + 0.6 * (0.12 - 0.04))
assert pct(alpha) == "1,20%"
add('PT', T_SL, 3,
    "Trong năm, quỹ Z đạt lợi suất 10% với beta 0,6, trong khi danh mục thị trường đạt 12% và lãi suất phi rủi ro là 4%. Theo chỉ số alpha của Jensen, nhận định nào đúng?",
    "Alpha = +1,20%; quỹ vượt mức lợi suất yêu cầu tương ứng rủi ro hệ thống",
    ["Alpha = −2,00%; quỹ kém hiệu quả vì lợi suất thấp hơn thị trường",
     "Alpha = +6,00%; quỹ hiệu quả vì lợi suất vượt lãi suất phi rủi ro",
     "Alpha = −1,20%; quỹ có lợi suất thấp hơn mức yêu cầu theo CAPM"],
    f"Lợi suất yêu cầu theo CAPM = 4% + 0,6 × (12% − 4%) = 8,8%. Alpha Jensen = 10% − 8,8% = +{pct(alpha)} > 0: quỹ hoạt động tốt so với rủi ro hệ thống dù lợi suất thấp hơn thị trường. Lỗi thường gặp: so trực tiếp với thị trường (−2,00%), chỉ trừ Rf (+6,00%), nhầm dấu (−1,20%).",
    "Đánh giá hiệu quả danh mục: alpha Jensen = Rp − [Rf + βp(Rm − Rf)]")

n_hedge = 1.1 * 20e9 / (1300 * 100_000)
assert round(n_hedge) == 169 and round(20e9 / 1.3e8) == 154 and round(1.1 * 20e9 / 1.28e8) == 172
add('PT', T_SL, 3,
    "Quỹ nắm giữ danh mục cổ phiếu trị giá 20 tỷ đồng, beta 1,1 so với chỉ số VN30, muốn phòng ngừa toàn bộ rủi ro giảm giá của thị trường (đưa beta danh mục về 0) bằng hợp đồng tương lai chỉ số VN30. Chỉ số VN30 đang ở mức 1.280 điểm; hợp đồng tương lai đang giao dịch ở 1.300 điểm, hệ số nhân 100.000 đồng/điểm. Quỹ cần thực hiện giao dịch nào?",
    "Bán 169 hợp đồng", ["Bán 154 hợp đồng", "Bán 172 hợp đồng", "Mua 169 hợp đồng"],
    f"Giá trị 1 hợp đồng = 1.300 × 100.000 = 130 triệu đồng. N = β × V/(F × hệ số nhân) = 1,1 × 20 tỷ/130 triệu = {vn(n_hedge)} ≈ 169 hợp đồng; vị thế mua cổ phiếu được phòng ngừa bằng vị thế bán hợp đồng tương lai. Lỗi thường gặp: bỏ qua beta (154), dùng mức chỉ số giao ngay 1.280 thay cho giá hợp đồng tương lai (172), mua thay vì bán.",
    "Phòng ngừa rủi ro hệ thống bằng hợp đồng tương lai chỉ số: N = β × V/(F × hệ số nhân)")

# ======================= PT: Định giá cổ phiếu (và quan hệ ngang giá quyền chọn) =======================
pvk = 32000 / (1 + 0.08 * 3 / 12)
gap = (2000 + pvk) - (2800 + 30000)
assert round(gap) == 573 and 2000 + 32000 - 32800 == 1200
add('PT', T_CP, 3,
    "Cổ phiếu không trả cổ tức, giá hiện tại 30.000 đồng. Quyền chọn mua và quyền chọn bán kiểu châu Âu trên cổ phiếu này cùng giá thực hiện 32.000 đồng, cùng kỳ hạn 3 tháng, có giá lần lượt 2.000 đồng và 2.800 đồng. Lãi suất phi rủi ro 8%/năm (lãi đơn). Theo quan hệ ngang giá quyền chọn mua – bán, nhà đầu tư có thể kinh doanh chênh lệch giá như thế nào?",
    "Bán quyền chọn mua, vay PV(K), mua quyền chọn bán và mua cổ phiếu; lãi ≈ 573 đồng/cp",
    ["Mua quyền chọn mua, gửi PV(K), bán quyền chọn bán và bán khống cổ phiếu; lãi ≈ 573 đồng/cp",
     "Bán quyền chọn mua, vay 32.000 đồng, mua quyền chọn bán và mua cổ phiếu; lãi ≈ 1.200 đồng/cp",
     "Ngang giá quyền chọn đang được thỏa mãn nên không có cơ hội kinh doanh chênh lệch giá"],
    f"PV(K) = 32.000/(1 + 8% × 3/12) = {vn(pvk)} đồng. C + PV(K) = {vn(2000 + pvk)} > P + S = 32.800 nên vế quyền chọn mua bị định giá cao: bán vế đắt (bán quyền chọn mua, vay PV(K)), mua vế rẻ (mua quyền chọn bán và cổ phiếu), thu ngay {vn(gap)} ≈ 573 đồng/cp; khi đáo hạn các vị thế triệt tiêu. Lỗi thường gặp: làm ngược chiều, hoặc không chiết khấu giá thực hiện (1.200 đồng).",
    "Ngang giá quyền chọn mua – bán: C + K/(1 + r × T) = P + S")

g16 = (0.12 * 50000 - 2000) / (50000 + 2000)
assert pct(g16) == "7,69%" and abs(2000 * (1 + g16) / (0.12 - g16) - 50000) < 1e-6
add('PT', T_CP, 3,
    "Cổ phiếu đang giao dịch ở giá 50.000 đồng, công ty vừa trả cổ tức D0 = 2.000 đồng/cp. Nhà đầu tư yêu cầu tỷ suất sinh lời 12%/năm. Giả định giá thị trường bằng giá trị theo mô hình Gordon, tốc độ tăng trưởng cổ tức đều mà thị trường đang kỳ vọng là bao nhiêu?",
    pct(g16), ["8,00%", "16,00%", "4,00%"],
    f"P0 = D0(1 + g)/(r − g) ⇒ 50.000 × (0,12 − g) = 2.000 × (1 + g) ⇒ 6.000 − 2.000 = 52.000g ⇒ g = {pct(g16)}. Lỗi thường gặp: coi D0 là D1 (g = 12% − 4% = 8,00%), cộng thay vì trừ tỷ suất cổ tức (16,00%), lấy tỷ suất cổ tức làm tốc độ tăng trưởng (4,00%).",
    "Mô hình Gordon: suy ra tốc độ tăng trưởng hàm ý từ giá thị trường", [g16, .08, .16, .04])

p2 = 12 * 3000
p0 = 1000 / 1.14 + (1200 + p2) / 1.14 ** 2
p_1y = 1000 / 1.14 + 1200 / 1.14 ** 2 + p2 / 1.14
p_nod = 1000 / 1.14 + 1200 / 1.14 ** 2 + p2
assert vn(p0, 0) == "29.501" and vn(p_1y, 0) == "33.380" and vn(p_nod, 0) == "37.801"
add('PT', T_CP, 3,
    "Cổ tức dự kiến năm 1 là 1.000 đồng/cp, năm 2 là 1.200 đồng/cp. Cuối năm 2, cổ phiếu dự kiến được bán với P/E bằng 12 lần EPS năm 2 (EPS năm 2 dự kiến 3.000 đồng). Tỷ suất sinh lời yêu cầu 14%/năm. Giá trị nội tại hiện tại của cổ phiếu xấp xỉ bao nhiêu?",
    vn(p0, 0) + " đồng", [vn(p_1y, 0) + " đồng", vn(p_nod, 0) + " đồng", "38.200 đồng"],
    f"Giá dự kiến cuối năm 2: P2 = 12 × 3.000 = 36.000 đồng. P0 = 1.000/1,14 + (1.200 + 36.000)/1,14² = 877,19 + 28.624,19 = {vn(p0, 0)} đồng. Lỗi thường gặp: chiết khấu P2 chỉ 1 năm ({vn(p_1y, 0)}), không chiết khấu P2 ({vn(p_nod, 0)}), cộng thẳng các khoản không chiết khấu (38.200).",
    "Chiết khấu cổ tức với giá bán cuối kỳ ước tính theo P/E", [p0, p_1y, p_nod, 38200])

pe_tr = 0.6 * 1.06 / (0.11 - 0.06)
assert vn(pe_tr) == "12,72" and vn(0.6 / 0.05) == "12,00" and vn(0.6 / 0.11) == "5,45" and vn(0.4 * 1.06 / 0.05) == "8,48"
add('PT', T_CP, 2,
    "Công ty có tỷ lệ chi trả cổ tức ổn định 60%, tốc độ tăng trưởng đều 6%/năm, tỷ suất sinh lời yêu cầu 11%/năm. Theo mô hình Gordon, hệ số P/E hợp lý tính trên EPS năm vừa qua (P0/E0) là bao nhiêu?",
    vn(pe_tr) + " lần", ["12,00 lần", "5,45 lần", "8,48 lần"],
    f"P0 = D0(1 + g)/(r − g) ⇒ P0/E0 = tỷ lệ chi trả × (1 + g)/(r − g) = 0,6 × 1,06/0,05 = {vn(pe_tr)} lần. 12,00 lần là P/E tính trên EPS năm tới (P0/E1 = 0,6/0,05); 5,45 lần là quên trừ g ở mẫu số; 8,48 lần là dùng nhầm tỷ lệ giữ lại 40%.",
    "Hệ số P/E theo mô hình tăng trưởng cổ tức đều", [pe_tr, 12, 0.6 / 0.11, 0.4 * 1.06 / 0.05])


def gordon(b, roe=0.08, r=0.12, e1=1000):
    g = roe * b
    return e1 * (1 - b) / (r - g)


assert gordon(0.6) < gordon(0.4) < gordon(0)
add('PT', T_CP, 2,
    "Công ty có ROE ổn định 8%, thấp hơn tỷ suất sinh lời yêu cầu của cổ đông là 12%. Theo mô hình tăng trưởng cổ tức với g = ROE × tỷ lệ lợi nhuận giữ lại, nếu công ty tăng tỷ lệ giữ lại để tái đầu tư (các yếu tố khác không đổi), giá trị nội tại của cổ phiếu sẽ",
    "Giảm, vì lợi nhuận tái đầu tư sinh lời thấp hơn mức cổ đông yêu cầu",
    ["Tăng, vì tốc độ tăng trưởng cổ tức g tăng theo tỷ lệ giữ lại",
     "Không đổi, vì tổng lợi nhuận của công ty không phụ thuộc chính sách",
     "Tăng, vì cổ tức năm tới giảm làm tỷ suất cổ tức của cổ phiếu tăng"],
    f"Khi ROE < r, mỗi đồng giữ lại tái đầu tư tạo giá trị hiện tại nhỏ hơn một đồng (giá trị cơ hội tăng trưởng âm). Ví dụ EPS năm tới 1.000 đồng: giữ lại 0% ⇒ P = {vn(gordon(0), 0)}; giữ lại 40% (g = 3,2%) ⇒ P = {vn(gordon(0.4), 0)}; giữ lại 60% (g = 4,8%) ⇒ P = {vn(gordon(0.6), 0)} đồng. Tăng trưởng chỉ tạo giá trị khi ROE > r.",
    "Tăng trưởng, chính sách cổ tức và giá trị cổ phiếu (ROE so với r)")

# ======================= PT: Định giá trái phiếu =======================
p20 = sum(5000 / 1.04 ** t for t in range(1, 5)) + 100000 / 1.04 ** 4
p20_ann = 10000 / 1.08 + 110000 / 1.08 ** 2
p20_swap = sum(4000 / 1.05 ** t for t in range(1, 5)) + 100000 / 1.05 ** 4
p20_nohalf = sum(5000 / 1.08 ** t for t in range(1, 5)) + 100000 / 1.08 ** 4
assert [vn(x, 0) for x in (p20, p20_ann, p20_swap, p20_nohalf)] == ["103.630", "103.567", "96.454", "90.064"]
add('PT', T_TP, 3,
    "Trái phiếu mệnh giá 100.000 đồng, lãi suất coupon 10%/năm, trả lãi 6 tháng một lần, còn đúng 2 năm đến hạn (vừa trả lãi). Lợi suất đáo hạn yêu cầu là 8%/năm (danh nghĩa, ghép lãi 6 tháng). Giá trái phiếu (làm tròn đến đồng) là",
    vn(p20, 0) + " đồng", [vn(p20_ann, 0) + " đồng", vn(p20_swap, 0) + " đồng", vn(p20_nohalf, 0) + " đồng"],
    f"Mỗi kỳ 6 tháng: coupon = 5.000 đồng, lợi suất = 4%, số kỳ = 4. P = 5.000 × [1 − 1,04^(−4)]/0,04 + 100.000/1,04^4 = 18.149 + 85.480 = {vn(p20, 0)} đồng (> mệnh giá vì coupon > YTM). Lỗi thường gặp: tính như trả lãi năm ({vn(p20_ann, 0)}), đảo coupon và lợi suất ({vn(p20_swap, 0)}), quên chia đôi lợi suất ({vn(p20_nohalf, 0)} – thấp hơn mệnh giá là vô lý).",
    "Định giá trái phiếu trả lãi nửa năm", [p20, p20_ann, p20_swap, p20_nohalf])


def bond_px(c, y, n, f=100.0):
    return sum(c * f / (1 + y) ** t for t in range(1, n + 1)) + f / (1 + y) ** n


lo, hi = 0.0, 0.08  # YTM của trái phiếu coupon 8%, giá 105, 5 năm
for _ in range(100):
    mid = (lo + hi) / 2
    lo, hi = (mid, hi) if bond_px(0.08, mid, 5) > 105 else (lo, mid)
ytm21, cy21 = lo, 8 / 105
assert 0.08 > cy21 > ytm21
add('PT', T_TP, 2,
    "Một trái phiếu trả lãi cố định hằng năm đang giao dịch ở giá cao hơn mệnh giá. Quan hệ nào sau đây giữa lãi suất coupon, lợi suất hiện hành và lợi suất đáo hạn (YTM) là đúng?",
    "Lãi suất coupon > lợi suất hiện hành > lợi suất đáo hạn",
    ["Lợi suất đáo hạn > lợi suất hiện hành > lãi suất coupon",
     "Lợi suất hiện hành > lãi suất coupon > lợi suất đáo hạn",
     "Lãi suất coupon = lợi suất hiện hành = lợi suất đáo hạn"],
    f"Giá > mệnh giá ⇒ lợi suất hiện hành = coupon/giá < lãi suất coupon; YTM còn tính khoản lỗ vốn khi giá kéo về mệnh giá lúc đáo hạn nên thấp hơn nữa. Ví dụ coupon 8%, giá 105.000 đồng, còn 5 năm: lợi suất hiện hành {pct(cy21)}, YTM ≈ {pct(ytm21)}. Thứ tự ngược lại đúng với trái phiếu chiết khấu.",
    "Quan hệ giữa lãi suất coupon, lợi suất hiện hành và YTM")

z = 100000 / 1.07 ** 5
assert vn(z, 0) == "71.299" and vn(100000 / 1.35, 0) == "74.074" and vn(100000 / 1.035 ** 10, 0) == "70.892"
add('PT', T_TP, 2,
    "Trái phiếu không trả lãi định kỳ (zero-coupon), mệnh giá 100.000 đồng, còn đúng 5 năm đến hạn. Với lợi suất đáo hạn yêu cầu 7%/năm (ghép lãi hằng năm), giá trái phiếu (làm tròn đến đồng) là",
    vn(z, 0) + " đồng", ["65.000 đồng", "74.074 đồng", "70.892 đồng"],
    f"P = 100.000/1,07^5 = 100.000/1,40255 = {vn(z, 0)} đồng. Lỗi thường gặp: trừ lãi đơn trên mệnh giá (100.000 × (1 − 5 × 7%) = 65.000), chiết khấu lãi đơn (100.000/1,35 = 74.074), ghép lãi nửa năm (100.000/1,035^10 = 70.892).",
    "Định giá trái phiếu không trả lãi định kỳ", [z, 65000, 100000 / 1.35, 100000 / 1.035 ** 10])

md = 5.4 / 1.08
p23 = 98000 * (1 - md * 0.005)
assert vn(md) == "5,00" and vn(p23, 0) == "95.550" and vn(98000 * (1 - 5.4 * 0.005), 0) == "95.354" \
    and vn(98000 * (1 + md * 0.005), 0) == "100.450" and vn(98000 * (1 - md * 0.0005), 0) == "97.755"
add('PT', T_TP, 3,
    "Trái phiếu trả lãi hằng năm đang có giá 98.000 đồng, lợi suất đáo hạn 8%/năm, thời gian đáo hạn bình quân Macaulay 5,4 năm. Nếu lợi suất đáo hạn tăng thêm 50 điểm cơ bản, theo xấp xỉ duration (bỏ qua độ lồi), giá trái phiếu ước tính là",
    vn(p23, 0) + " đồng", ["95.354 đồng", "100.450 đồng", "97.755 đồng"],
    f"Duration điều chỉnh MD = 5,4/1,08 = {vn(md)}. %ΔP ≈ −MD × Δy = −5 × 0,5% = −2,50% ⇒ P ≈ 98.000 × (1 − 0,025) = {vn(p23, 0)} đồng. Lỗi thường gặp: dùng thẳng duration Macaulay (95.354), sai dấu (100.450), đổi 50 điểm cơ bản thành 0,05% (97.755).",
    "Duration Macaulay, duration điều chỉnh và độ nhạy giá trái phiếu", [p23, 98000 * (1 - .027), 100450, 97755])

add('PT', T_TP, 1,
    "Thời gian đáo hạn bình quân Macaulay (Macaulay duration) của trái phiếu không trả lãi định kỳ (zero-coupon) bằng",
    "Đúng thời gian còn lại đến ngày đáo hạn của trái phiếu",
    ["Một nửa thời gian còn lại đến ngày đáo hạn của trái phiếu",
     "Thời gian còn lại đến đáo hạn chia cho (1 + lợi suất đáo hạn)",
     "Bằng 0, vì trái phiếu không có bất kỳ dòng tiền lãi định kỳ nào"],
    "Duration Macaulay là bình quân gia quyền các thời điểm nhận tiền theo tỷ trọng giá trị hiện tại; zero-coupon chỉ có một dòng tiền khi đáo hạn nên duration bằng đúng thời gian đáo hạn còn lại. Chia cho (1 + YTM) là duration điều chỉnh.",
    "Duration Macaulay của trái phiếu zero-coupon")

# ======================= PT: Thị trường hiệu quả =======================
add('PT', T_HQ, 2,
    "Nhiều nghiên cứu cho thấy sau khi doanh nghiệp công bố lợi nhuận cao hơn kỳ vọng, giá cổ phiếu tiếp tục tăng dần trong nhiều tuần. Hiện tượng này mâu thuẫn trực tiếp nhất với dạng nào của giả thuyết thị trường hiệu quả?",
    "Dạng trung bình, vì giá không phản ánh ngay và đầy đủ thông tin công khai",
    ["Dạng mạnh, vì chỉ người có thông tin nội bộ mới biết trước lợi nhuận",
     "Dạng yếu, vì nhà đầu tư dùng giá quá khứ để dự báo lợi nhuận kỳ tới",
     "Không mâu thuẫn, vì báo cáo lợi nhuận là thông tin đã công bố công khai"],
    "Theo dạng trung bình (bán mạnh), giá phải điều chỉnh ngay và đầy đủ khi thông tin công khai được công bố; giá còn trôi dần nhiều tuần sau công bố (post-earnings announcement drift) cho phép kiếm lợi suất vượt trội từ thông tin công khai nên mâu thuẫn với dạng này.",
    "Giả thuyết thị trường hiệu quả dạng trung bình và các bất thường thị trường")

add('PT', T_HQ, 1,
    "Nếu thị trường hiệu quả ở dạng yếu, phương pháp nào sau đây KHÔNG thể giúp nhà đầu tư đạt lợi suất vượt trội một cách ổn định (sau điều chỉnh rủi ro)?",
    "Phân tích kỹ thuật dựa trên diễn biến giá và khối lượng giao dịch quá khứ",
    ["Phân tích cơ bản dựa trên báo cáo tài chính và triển vọng doanh nghiệp",
     "Giao dịch dựa trên thông tin nội bộ chưa được công bố ra công chúng",
     "Phân tích nhanh thông tin vĩ mô, ngành vừa được công bố trên thị trường"],
    "Dạng yếu: giá đã phản ánh toàn bộ thông tin giá và khối lượng quá khứ nên phân tích kỹ thuật không tạo lợi suất vượt trội ổn định. Dạng yếu chưa loại trừ khả năng phân tích cơ bản, khai thác thông tin công khai hay thông tin nội bộ mang lại lợi suất vượt trội.",
    "Giả thuyết thị trường hiệu quả dạng yếu và phân tích kỹ thuật")

# ======================= MG: Giao dịch ký quỹ, bán khống =======================
add('MG', M_CP, 1,
    "Bán khống chứng khoán là giao dịch trong đó nhà đầu tư",
    "Bán chứng khoán đi vay, kỳ vọng sau đó mua lại với giá thấp hơn để hoàn trả",
    ["Bán chứng khoán đang sở hữu với giá thấp hơn giá tham chiếu để cắt lỗ",
     "Mua chứng khoán bằng tiền vay của công ty chứng khoán, kỳ vọng giá tăng",
     "Bán chứng khoán đang sở hữu, đồng thời cam kết mua lại sau một thời gian"],
    "Người bán khống vay chứng khoán để bán, sau đó mua lại trên thị trường để trả bên cho vay; có lãi nếu giá giảm. Mua bằng tiền vay là giao dịch ký quỹ (mua ký quỹ); bán kèm cam kết mua lại là giao dịch repo.",
    "Bán khống chứng khoán")

add('MG', M_CP, 2,
    "So với vị thế mua cổ phiếu bằng vốn tự có, vị thế bán khống cổ phiếu có đặc điểm rủi ro nào sau đây?",
    "Lỗ tối đa về lý thuyết không giới hạn vì giá cổ phiếu có thể tăng không giới hạn",
    ["Lỗ tối đa bằng số tiền thu được khi bán khống vì giá không thể xuống dưới 0",
     "Lỗ tối đa bằng đúng khoản ký quỹ ban đầu đã nộp cho công ty chứng khoán",
     "Không chịu rủi ro thị trường vì chứng khoán đem bán là chứng khoán đi vay"],
    "Người bán khống phải mua lại cổ phiếu ở giá tương lai, giá càng tăng càng lỗ và về lý thuyết không có giới hạn; trong khi lãi tối đa chỉ bằng số tiền bán khống (khi giá về 0). Người mua bằng vốn tự có lỗ tối đa bằng số vốn bỏ ra. Vì vậy bán khống luôn phải ký quỹ và bị gọi ký quỹ khi giá tăng.",
    "Rủi ro của giao dịch bán khống")

prof = 5000 * (40000 - 34000 - 1000)
assert prof == 25_000_000
add('MG', M_CP, 2,
    "Nhà đầu tư vay và bán khống 5.000 cổ phiếu ở giá 40.000 đồng. Trong thời gian vay, công ty trả cổ tức tiền mặt 1.000 đồng/cp và nhà đầu tư phải hoàn trả khoản cổ tức này cho bên cho vay chứng khoán. Sau đó nhà đầu tư mua lại 5.000 cổ phiếu ở giá 34.000 đồng để trả. Bỏ qua phí vay, phí giao dịch và thuế, kết quả của nhà đầu tư là",
    "Lãi 25.000.000 đồng", ["Lãi 30.000.000 đồng", "Lãi 35.000.000 đồng", "Lỗ 25.000.000 đồng"],
    f"Lãi do giá giảm = 5.000 × (40.000 − 34.000) = 30.000.000 đồng; trừ cổ tức phải hoàn trả 5.000 × 1.000 = 5.000.000 đồng ⇒ lãi {vn(prof, 0)} đồng. Lỗi thường gặp: quên cổ tức phải trả (30 triệu), cộng cổ tức như người sở hữu (35 triệu), tính như vị thế mua (lỗ 25 triệu).",
    "Kết quả giao dịch bán khống", [prof, 30e6, 35e6, -25e6])

v12 = 10000 * 50000
p_call_short = (v12 * 1.5) / (10000 * 1.3)
assert vn(p_call_short, 0) == "57.692" and abs((v12 * 1.5 - 10000 * p_call_short) / (10000 * p_call_short) - 0.3) < 1e-12
add('MG', M_CP, 3,
    "Giả sử trên một thị trường cho phép bán khống: nhà đầu tư bán khống 10.000 cổ phiếu giá 50.000 đồng, nộp ký quỹ ban đầu 50% giá trị bán (250 triệu đồng); tiền bán 500 triệu đồng được giữ lại trong tài khoản. Tỷ lệ ký quỹ = (Tổng tiền trong tài khoản − Giá trị thị trường cổ phiếu phải trả)/Giá trị thị trường cổ phiếu phải trả; tỷ lệ duy trì 30%. Bỏ qua lãi và phí, nhà đầu tư bị gọi ký quỹ khi giá cổ phiếu tăng vượt mức xấp xỉ",
    "57.692 đồng", ["60.000 đồng", "65.000 đồng", "75.000 đồng"],
    f"Tổng tiền trong tài khoản = 500 + 250 = 750 triệu đồng. Gọi ký quỹ khi (750.000.000 − 10.000P)/(10.000P) = 30% ⇒ P = 750.000.000/(1,3 × 10.000) = {vn(p_call_short, 0)} đồng. Lỗi thường gặp: cộng chênh lệch tỷ lệ 20% vào giá (60.000), nhân giá bán với 1,3 (65.000), lấy mức giá làm vốn ký quỹ về 0 (75.000).",
    "Giá gọi ký quỹ của vị thế bán khống", [p_call_short, 60000, 65000, 75000])

ratio3 = (20000 * 25000 - 300e6) / (20000 * 25000)
assert pct(ratio3) == "40,00%" and pct(0.5 * 25 / 30) == "41,67%"
add('MG', M_CP, 2,
    "Khách hàng mua 20.000 cổ phiếu giá 30.000 đồng bằng giao dịch ký quỹ: tự có 50%, vay công ty chứng khoán 50%. Hợp đồng quy định tỷ lệ ký quỹ = (Giá trị chứng khoán − Dư nợ)/Giá trị chứng khoán. Bỏ qua lãi vay và phí. Khi giá cổ phiếu giảm còn 25.000 đồng, tỷ lệ ký quỹ thực tế của tài khoản là",
    pct(ratio3), ["60,00%", "41,67%", "50,00%"],
    f"Dư nợ = 50% × 600 triệu = 300 triệu đồng (không đổi khi giá giảm). Giá trị chứng khoán mới = 20.000 × 25.000 = 500 triệu đồng ⇒ tỷ lệ ký quỹ = (500 − 300)/500 = {pct(ratio3)}. Lỗi thường gặp: lấy dư nợ/giá trị chứng khoán (60,00%), giảm tỷ lệ theo đúng tỷ lệ giảm giá (41,67%), cho rằng tỷ lệ không đổi (50,00%).",
    "Tỷ lệ ký quỹ thực tế trong giao dịch ký quỹ", [ratio3, .6, 0.5 * 25 / 30, .5])

loss = 500 * 0.15 / 300
assert pct(loss) == "25,00%" and pct(75 / 200) == "37,50%"
add('MG', M_CP, 2,
    "Nhà đầu tư dùng 300 triệu đồng vốn tự có và vay ký quỹ thêm 200 triệu đồng để mua cổ phiếu (tỷ lệ ký quỹ ban đầu 60%). Sau đó giá cổ phiếu giảm 15%. Bỏ qua lãi vay, phí và thuế, tỷ lệ lỗ trên vốn tự có của nhà đầu tư là",
    pct(loss), ["15,00%", "37,50%", "9,00%"],
    f"Giá trị cổ phiếu = 500 triệu đồng; lỗ = 500 × 15% = 75 triệu đồng; tỷ lệ lỗ trên vốn tự có = 75/300 = {pct(loss)} = 15%/60% (đòn bẩy khuếch đại thua lỗ). Lỗi thường gặp: bỏ qua đòn bẩy (15,00%), chia cho khoản vay (37,50%), nhân thay vì chia cho tỷ lệ ký quỹ (9,00%).",
    "Tác động của đòn bẩy trong giao dịch ký quỹ", [loss, .15, .375, .09])

shares9 = 300e6 / 0.4 / 25000
assert shares9 == 30000 and 300e6 * 1.4 / 25000 == 16800 and round(300e6 / 0.6 / 25000) == 20000
add('MG', M_CP, 3,
    "Giả sử quy chế của công ty chứng khoán quy định tỷ lệ ký quỹ ban đầu 40% (vốn tự có/giá trị chứng khoán mua). Khách hàng có 300 triệu đồng tiền mặt, muốn dùng tối đa sức mua ký quỹ để mua cổ phiếu giá 25.000 đồng. Bỏ qua phí giao dịch, khối lượng tối đa khách hàng có thể mua là",
    "30.000 cổ phiếu", ["12.000 cổ phiếu", "16.800 cổ phiếu", "20.000 cổ phiếu"],
    f"Sức mua = vốn tự có/tỷ lệ ký quỹ ban đầu = 300/0,4 = 750 triệu đồng (vay tối đa 450 triệu) ⇒ 750.000.000/25.000 = {vn(shares9, 0)} cổ phiếu. Lỗi thường gặp: chỉ dùng tiền mặt (12.000), lấy 300 × (1 + 40%) (16.800), chia cho 60% (20.000).",
    "Sức mua trong giao dịch ký quỹ", [shares9, 12000, 16800, 20000])

E10, V10, D10, m10 = 180e6, 600e6, 420e6, 0.35
x10 = V10 - E10 / m10
n10 = -(-x10 // 20000)
assert n10 == 4286 and (V10 - n10 * 20000 - (D10 - n10 * 20000)) / (V10 - n10 * 20000) >= m10
assert round((m10 * V10 - E10) / 20000) == 1500 and round((V10 - E10 / 0.5) / 20000) == 12000 and round((V10 - E10 / (1 - m10)) / 20000) == 16154
add('MG', M_CP, 3,
    "Tài khoản ký quỹ có 30.000 cổ phiếu, giá hiện tại 20.000 đồng, dư nợ 420 triệu đồng. Tỷ lệ ký quỹ = (Giá trị chứng khoán − Dư nợ)/Giá trị chứng khoán; tỷ lệ ban đầu 50%, tỷ lệ duy trì 35%. Khách hàng không nộp tiền mà bán bớt cổ phiếu ở giá 20.000 đồng, dùng toàn bộ tiền bán để trả nợ, đưa tỷ lệ ký quỹ về tối thiểu 35%. Bỏ qua phí, thuế; số cổ phiếu tối thiểu phải bán (làm tròn lên) là",
    "4.286 cổ phiếu", ["1.500 cổ phiếu", "12.000 cổ phiếu", "16.154 cổ phiếu"],
    f"Vốn tự có = 600 − 420 = 180 triệu đồng (tỷ lệ 30% < 35%); bán cổ phiếu trả nợ không làm đổi vốn tự có. Cần 180/(600 − X) ≥ 35% ⇒ X ≥ 600 − 514,29 = 85,71 triệu đồng ⇒ 85.714.286/20.000 = 4.285,7, làm tròn lên {vn(n10, 0)} cổ phiếu. Lỗi thường gặp: chia số tiền cần nộp thêm (35% × 600 − 180 = 30 triệu) cho giá (1.500), đưa về tỷ lệ ban đầu 50% (12.000), dùng nhầm 65% thay cho 35% (16.154).",
    "Xử lý gọi ký quỹ bằng bán bớt chứng khoán", [n10, 1500, 12000, 16154])

excess = (1000 - 450) - 0.5 * 1000
bp11 = excess / 0.5
assert bp11 == 100 and ((1000 + bp11) - (450 + bp11)) / (1000 + bp11) == 0.5
add('MG', M_CP, 3,
    "Tài khoản ký quỹ có giá trị chứng khoán 1.000 triệu đồng, dư nợ 450 triệu đồng. Tỷ lệ ký quỹ = (Giá trị chứng khoán − Dư nợ)/Giá trị chứng khoán; giả sử quy chế quy định tỷ lệ ký quỹ ban đầu 50%. Bỏ qua phí, giá trị cổ phiếu tối đa khách hàng có thể mua thêm bằng ký quỹ mà không nộp thêm tiền là",
    "100 triệu đồng", ["25 triệu đồng", "50 triệu đồng", "1.100 triệu đồng"],
    f"Vốn tự có = 1.000 − 450 = 550 triệu đồng; vốn yêu cầu theo tỷ lệ ban đầu = 50% × 1.000 = 500 triệu ⇒ vốn dư = 50 triệu đồng. Sức mua thêm = 50/50% = {vn(bp11, 0)} triệu đồng (sau khi mua: (1.100 − 550)/1.100 = 50%). Lỗi thường gặp: nhân thay vì chia cho tỷ lệ ký quỹ (25), chỉ tính vốn dư (50), lấy toàn bộ vốn tự có chia 50% mà quên danh mục hiện có (1.100).",
    "Vốn dư và sức mua bổ sung trong tài khoản ký quỹ", [bp11, 25, 50, 1100])

drop = 1 - 0.5 / 0.65
assert pct(drop) == "23,08%" and abs(((1 - drop) - 0.5) / (1 - drop) - 0.35) < 1e-12
add('MG', M_CP, 3,
    "Giả sử quy chế quy định tỷ lệ ký quỹ ban đầu 50% và tỷ lệ ký quỹ duy trì 35%, với tỷ lệ ký quỹ = (Giá trị chứng khoán − Dư nợ)/Giá trị chứng khoán. Khách hàng mua cổ phiếu với đúng tỷ lệ ký quỹ ban đầu. Bỏ qua lãi vay và phí, giá cổ phiếu giảm bao nhiêu phần trăm so với giá mua thì tài khoản chạm tỷ lệ duy trì?",
    pct(drop), ["15,00%", "30,00%", "35,00%"],
    f"Giá mua = 1 đơn vị, dư nợ = 0,5. Chạm duy trì khi (P − 0,5)/P = 35% ⇒ P = 0,5/0,65 = 0,7692 ⇒ giá giảm {pct(drop)}. Lỗi thường gặp: lấy hiệu hai tỷ lệ (15,00%), chia hiệu cho tỷ lệ ban đầu (30,00%), lấy chính tỷ lệ duy trì (35,00%).",
    "Tỷ lệ ký quỹ ban đầu, tỷ lệ duy trì và mức giảm giá gây gọi ký quỹ", [drop, .15, .30, .35])

# ======================= MG: Repo trái phiếu =======================
add('MG', M_TP, 1,
    "Về bản chất kinh tế, giao dịch mua bán lại trái phiếu (repo) đối với bên bán ở lượt đi tương đương với",
    "Khoản vay tiền ngắn hạn có bảo đảm bằng chính trái phiếu đã bán",
    ["Việc chuyển nhượng hẳn trái phiếu, không kèm nghĩa vụ mua lại",
     "Khoản cho vay tiền ngắn hạn, nhận trái phiếu làm tài sản bảo đảm",
     "Hợp đồng quyền chọn bán trái phiếu với giá thực hiện bằng mệnh giá"],
    "Trong repo, bên bán lượt đi nhận tiền ngay và cam kết mua lại trái phiếu ở giá cao hơn vào ngày xác định; chênh lệch giá chính là tiền lãi vay. Với bên mua lượt đi, giao dịch tương đương cho vay có bảo đảm (reverse repo).",
    "Bản chất giao dịch mua bán lại (repo) trái phiếu")

add('MG', M_TP, 2,
    "Trong giao dịch repo trái phiếu, giá trị thanh toán lượt đi thường thấp hơn giá trị thị trường của trái phiếu theo một tỷ lệ chiết khấu (haircut). Mục đích chủ yếu của haircut là",
    "Bảo vệ bên cho vay tiền trước rủi ro giá trái phiếu giảm và đối tác vỡ nợ",
    ["Bảo vệ bên vay tiền trước rủi ro lãi suất repo tăng trong kỳ hạn giao dịch",
     "Bù đắp tiền lãi coupon mà bên bán lượt đi được nhận trong kỳ hạn repo",
     "Giảm số thuế phải nộp trên chênh lệch giữa giá lượt về và giá lượt đi"],
    "Haircut tạo phần tài sản bảo đảm dư so với số tiền cho vay. Nếu bên bán lượt đi không mua lại đúng hạn, bên cho vay tiền bán trái phiếu để thu hồi; phần dư giúp bù khoản giảm giá trái phiếu trong thời gian xử lý.",
    "Tỷ lệ chiết khấu (haircut) trong giao dịch repo")

leg1 = 10e9 * 0.95
leg2 = leg1 * (1 + 0.05 * 30 / 365)
assert vn(leg2, 0) == "9.539.041.096" and vn(10e9 * (1 + 0.05 * 30 / 365), 0) == "10.041.095.890" \
    and vn(leg1 * (1 + 0.05 * 30 / 360), 0) == "9.539.583.333" and vn(leg1 + 10e9 * 0.05 * 30 / 365, 0) == "9.541.095.890"
add('MG', M_TP, 3,
    "Công ty X cần vốn ngắn hạn nên thực hiện repo: bán trái phiếu Chính phủ có giá trị thị trường 10 tỷ đồng với tỷ lệ chiết khấu (haircut) 5%, lãi suất repo 5%/năm, kỳ hạn 30 ngày, quy ước 365 ngày/năm. Giá trị thanh toán lượt về mà công ty X phải trả là",
    vn(leg2, 0) + " đồng", ["10.041.095.890 đồng", "9.539.583.333 đồng", "9.541.095.890 đồng"],
    f"Lượt đi = 10 tỷ × (1 − 5%) = 9,5 tỷ đồng. Lượt về = 9.500.000.000 × (1 + 5% × 30/365) = {vn(leg2, 0)} đồng. Lỗi thường gặp: bỏ qua haircut (10.041.095.890), dùng quy ước 360 ngày (9.539.583.333), tính lãi trên giá trị thị trường thay vì số tiền thực vay (9.541.095.890).",
    "Giá trị thanh toán lượt về của repo có haircut", [leg2, 10041095890, 9539583333, 9541095890])

l2_7 = 20e9 * (1 + 0.06 * 14 / 365)
assert vn(l2_7, 0) == "20.046.027.397"
r7 = (20046027397 - 20e9) / 20e9 * 365 / 14
hp = (20046027397 - 20e9) / 20e9
assert pct(r7) == "6,00%" and pct(hp) == "0,23%" and pct(hp * 360 / 14) == "5,92%" and pct((1 + hp) ** (365 / 14) - 1) == "6,18%"
add('MG', M_TP, 2,
    "Giao dịch repo trái phiếu kỳ hạn 14 ngày có giá trị thanh toán lượt đi 20.000.000.000 đồng và lượt về 20.046.027.397 đồng. Theo quy ước lãi đơn, 365 ngày/năm, lãi suất repo năm là",
    pct(r7), ["0,23%", "5,92%", "6,18%"],
    f"Lãi = 20.046.027.397 − 20.000.000.000 = 46.027.397 đồng ⇒ lãi suất 14 ngày = 0,23014%; lãi suất năm = 0,23014% × 365/14 = {pct(r7)}. Lỗi thường gặp: không quy ra năm (0,23%), dùng 360 ngày (5,92%), ghép lãi kép thay vì lãi đơn (6,18%).",
    "Lãi suất repo hàm ý từ giá lượt đi và lượt về", [r7, hp, hp * 360 / 14, (1 + hp) ** (365 / 14) - 1])

# ======================= Gán id, vị trí đáp án, kiểm tra =======================
assert len(Q) == 40, len(Q)
pos = [0, 1, 2, 3] * 10
random.Random(20261108).shuffle(pos)
out, ranks = [], Counter()
for i, (x, a) in enumerate(zip(Q, pos), 1):
    o = list(x['wrong'])
    o.insert(a, x['correct'])
    if x['nums']:
        ranks[sorted(x['nums']).index(x['nums'][0]) + 1] += 1
    if x['level'] == 3:  # bài tính: con số chính của đáp án phải có trong lời giải
        m = re.search(r"[−+]?\d[\d.,]*", x['correct'])
        assert m is None or m.group(0).lstrip('+−').rstrip('.,') in x['e'], (i, m.group(0))
    lens = [len(s) for s in o]
    assert max(lens) <= 2.2 * min(lens) or max(lens) - min(lens) <= 12, (i, o)
    assert not re.search(r"(phương án|đáp án|chọn|câu)\s+[A-D]\b", x['e']), i
    out.append(dict(id=f"C9-{i:03d}", part="CM", subject=x['subject'], topic=x['topic'], level=x['level'],
                    q=x['q'], o=o, a=a, e=x['e'], basis=x['basis'], quote="", src=SRC, as_of="2026-11"))
with open(OUT, 'w', encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False, indent=1)
C = Counter
print("wrote", len(out))
print("subject:", dict(C(x['subject'] for x in out)), "level:", dict(sorted(C(x['level'] for x in out).items())))
print("a:", dict(sorted(C(x['a'] for x in out).items())), "rank đáp án trong số:", dict(sorted(ranks.items())))
for s in ('PT', 'MG'):
    print(s, dict(sorted(C(x['level'] for x in out if x['subject'] == s).items())), dict(C(x['topic'] for x in out if x['subject'] == s)))
