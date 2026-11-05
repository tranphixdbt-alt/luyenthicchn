# Sinh 90 câu CM (PT 50, BC 40) -> ../cm_2.json. Mọi phép tính được tính lại và assert.
import json, math, random

OUT = '/home/user/cchn_moi/web/data/src/cm_2.json'
SRC = 'Giáo trình SRTC (khung chương trình)'
Q = []


def vn(x, d=2):
    s = f"{abs(x):,.{d}f}".replace(',', 'X').replace('.', ',').replace('X', '.')
    return ('−' if x < 0 else '') + s


def pct(x, d=2):
    return vn(x * 100, d) + '%'


def add(subj, topic, level, q, correct, wrong, e, basis):
    assert len(wrong) == 3
    Q.append(dict(subject=subj, topic=topic, level=level, q=q, correct=correct, wrong=wrong, e=e, basis=basis))


T_TQ = "Tổng quan về phân tích và đầu tư"
T_SL = "Mức sinh lời và rủi ro"
T_HQ = "Thị trường hiệu quả và tài chính hành vi"
T_KT = "Phân tích kinh tế trong đầu tư chứng khoán"
T_CP = "Phân tích và định giá cổ phiếu"
T_TP = "Phân tích và định giá trái phiếu"
T_KTH = "Phân tích kỹ thuật"
B_TQ = "Tổng quan về phân tích báo cáo tài chính doanh nghiệp"
B_HT = "Hệ thống báo cáo tài chính doanh nghiệp"
B_CT = "Phân tích các chỉ tiêu tài chính"
B_DB = "Dự báo báo cáo tài chính doanh nghiệp"
B_CL = "Chất lượng báo cáo tài chính doanh nghiệp"
B_TH = "Nghiên cứu tình huống"

# =========================== PT: Tổng quan ===========================
r = 50 / (500 - 50)
assert pct(r) == "11,11%"
add('PT', T_TQ, 3,
    "Một khoản vay kỳ hạn 1 năm, số tiền 500 triệu đồng, lãi suất danh nghĩa 10%/năm, tiền lãi được khấu trừ trả trước ngay khi giải ngân (người vay thực nhận 450 triệu đồng và cuối năm trả 500 triệu đồng). Lãi suất thực tế người vay phải chịu là bao nhiêu?",
    pct(r), [pct(0.10), pct(50 / 550), pct(0.11)],
    f"Lãi trả trước = 500 × 10% = 50 triệu đồng; số tiền thực nhận = 500 − 50 = 450 triệu đồng. Lãi suất thực tế = 50/450 = {pct(r)}/năm (tức 10/90). Lỗi thường gặp: giữ nguyên 10% hoặc chia cho 550 (9,09%).",
    "Lãi suất thực tế khi trả lãi trước: r = i/(1 − i) = 10/90")

add('PT', T_TQ, 2,
    "Với cùng một mức lãi suất danh nghĩa năm, khi tần suất ghép lãi trong năm tăng lên (ví dụ từ ghép lãi năm sang ghép lãi tháng), lãi suất thực tế năm (EAR) thay đổi như thế nào?",
    "Tăng lên, vì tiền lãi được nhập vào gốc sớm hơn và tiếp tục sinh lãi",
    ["Giảm xuống, vì lãi suất áp dụng cho mỗi kỳ ghép lãi nhỏ hơn",
     "Không đổi, vì lãi suất danh nghĩa năm vẫn giữ nguyên",
     "Tăng hoặc giảm tùy theo số năm của khoản đầu tư"],
    "EAR = (1 + i/m)^m − 1 tăng khi số lần ghép lãi m tăng, vì lãi được nhập gốc sớm hơn (ví dụ 12%/năm: ghép năm 12,00%, ghép tháng 12,68%).",
    "Lãi suất thực tế năm: EAR = (1 + i/m)^m − 1")

pv = 20 * (1 - 1.1 ** -5) / 0.1
assert vn(pv) == "75,82"
add('PT', T_TQ, 3,
    "Nhà đầu tư sẽ nhận 20 triệu đồng vào cuối mỗi năm trong 5 năm liên tiếp. Với lãi suất chiết khấu 10%/năm (ghép lãi hằng năm), giá trị hiện tại của dòng tiền này là bao nhiêu?",
    vn(pv) + " triệu đồng", [vn(100) + " triệu đồng", vn(pv * 1.1) + " triệu đồng", vn(100 / 1.1 ** 5) + " triệu đồng"],
    f"PV = 20 × [1 − 1,1^(−5)]/0,1 = 20 × 3,7908 = {vn(pv)} triệu đồng. Lỗi thường gặp: không chiết khấu (100), coi là niên kim đầu kỳ ({vn(pv * 1.1)}), chiết khấu tổng 100 một lần ({vn(100 / 1.1 ** 5)}).",
    "Giá trị hiện tại của niên kim cuối kỳ: PV = A × [1 − (1 + r)^(−n)]/r")

add('PT', T_TQ, 1,
    "Trong quy trình đầu tư, bước nào cần được thực hiện đầu tiên?",
    "Xác định mục tiêu và các ràng buộc của nhà đầu tư (chính sách đầu tư)",
    ["Phân tích và lựa chọn các chứng khoán cụ thể đưa vào danh mục",
     "Phân bổ tài sản và xây dựng danh mục đầu tư theo kỳ vọng",
     "Đánh giá kết quả đầu tư và tái cơ cấu danh mục định kỳ"],
    "Quy trình đầu tư bắt đầu bằng xây dựng chính sách đầu tư (mục tiêu sinh lời – rủi ro và các ràng buộc), sau đó mới phân tích, xây dựng danh mục, theo dõi và đánh giá.",
    "Quy trình đầu tư: chính sách đầu tư → phân tích → xây dựng danh mục → đánh giá, điều chỉnh")

add('PT', T_TQ, 1,
    "Yếu tố nào sau đây thuộc nhóm ràng buộc trong chính sách đầu tư, thay vì nhóm mục tiêu sinh lời – rủi ro?",
    "Nhu cầu thanh khoản và thời hạn đầu tư của nhà đầu tư",
    ["Mức sinh lời yêu cầu hằng năm của nhà đầu tư",
     "Mức độ sẵn sàng chấp nhận rủi ro của nhà đầu tư",
     "Khả năng chịu đựng rủi ro về mặt tài chính"],
    "Mục tiêu gồm sinh lời và rủi ro (mức sẵn sàng, khả năng chấp nhận rủi ro); ràng buộc gồm thanh khoản, thời hạn, thuế, pháp lý và các yếu tố đặc thù.",
    "Chính sách đầu tư: mục tiêu (sinh lời, rủi ro) và ràng buộc (thanh khoản, thời hạn, thuế, pháp lý, đặc thù)")

# =========================== PT: Mức sinh lời và rủi ro ===========================
hpr = (46000 - 40000 + 2000) / 40000
assert pct(hpr) == "20,00%"
add('PT', T_SL, 3,
    "Nhà đầu tư mua cổ phiếu ABC giá 40.000 đồng/cp, trong thời gian nắm giữ nhận cổ tức tiền mặt 2.000 đồng/cp và bán ra với giá 46.000 đồng/cp. Bỏ qua thuế, phí. Mức sinh lời trong thời gian nắm giữ (HPR) là bao nhiêu?",
    pct(hpr), [pct(6000 / 40000), pct(8000 / 46000), pct(2000 / 40000)],
    "HPR = (P1 − P0 + D)/P0 = (46.000 − 40.000 + 2.000)/40.000 = 20,00%. Lỗi thường gặp: bỏ cổ tức (15%), chia cho giá bán (17,39%), chỉ tính cổ tức (5%).",
    "HPR = (P1 − P0 + D)/P0")

p = [0.3, 0.5, 0.2]; ret = [0.25, 0.10, -0.10]
er = sum(a * b for a, b in zip(p, ret))
sd = math.sqrt(sum(a * (b - er) ** 2 for a, b in zip(p, ret)))
m3 = sum(ret) / 3
sd_unw = math.sqrt(sum((b - m3) ** 2 for b in ret) / 3)
mad = sum(a * abs(b - er) for a, b in zip(p, ret))
assert pct(er) == "10,50%" and pct(sd) == "12,13%"
add('PT', T_SL, 3,
    "Dự báo mức sinh lời của cổ phiếu XYZ trong năm tới: kịch bản tăng trưởng (xác suất 30%) 25%; kịch bản bình thường (xác suất 50%) 10%; kịch bản suy thoái (xác suất 20%) −10%. Độ lệch chuẩn của mức sinh lời là bao nhiêu?",
    pct(sd), [pct(sd_unw), pct(mad), pct(er)],
    f"E(R) = 0,3×25% + 0,5×10% + 0,2×(−10%) = {pct(er)}. σ² = 0,3×(14,5%)² + 0,5×(−0,5%)² + 0,2×(−20,5%)² = 0,014725; σ = {pct(sd)}. Lỗi thường gặp: bỏ xác suất ({pct(sd_unw)}), không bình phương độ lệch ({pct(mad)}), nhầm với lợi suất kỳ vọng.",
    "σ = √Σ pᵢ[Rᵢ − E(R)]²")

w1, w2, s1, s2, rho = 0.6, 0.4, 0.20, 0.30, 0.2
var_p = w1**2 * s1**2 + w2**2 * s2**2 + 2 * w1 * w2 * rho * s1 * s2
sp = math.sqrt(var_p)
assert pct(sp) == "18,59%"
add('PT', T_SL, 3,
    "Danh mục gồm 60% cổ phiếu A (độ lệch chuẩn 20%) và 40% cổ phiếu B (độ lệch chuẩn 30%); hệ số tương quan giữa A và B là 0,2. Độ lệch chuẩn của danh mục là bao nhiêu?",
    pct(sp), [pct(w1 * s1 + w2 * s2), pct(math.sqrt(w1**2 * s1**2 + w2**2 * s2**2)), pct(var_p)],
    f"σp² = 0,6²×0,2² + 0,4²×0,3² + 2×0,6×0,4×0,2×0,2×0,3 = 0,0144 + 0,0144 + 0,00576 = {vn(var_p, 5)}; σp = {pct(sp)}. Thấp hơn bình quân gia quyền 24% vì ρ < 1. Lỗi thường gặp: bình quân gia quyền (24%), bỏ hiệp phương sai (16,97%), lấy phương sai làm độ lệch chuẩn (3,46%).",
    "σp² = w₁²σ₁² + w₂²σ₂² + 2w₁w₂ρσ₁σ₂")

add('PT', T_SL, 2,
    "Danh mục gồm hai cổ phiếu có rủi ro với tỷ trọng đều dương. Độ lệch chuẩn của danh mục nhỏ hơn bình quân gia quyền độ lệch chuẩn của hai cổ phiếu (có lợi ích đa dạng hóa) trong trường hợp nào?",
    "Hệ số tương quan giữa hai cổ phiếu nhỏ hơn +1",
    ["Chỉ khi hệ số tương quan giữa hai cổ phiếu là số âm",
     "Chỉ khi hệ số tương quan giữa hai cổ phiếu bằng −1",
     "Chỉ khi hai cổ phiếu có độ lệch chuẩn bằng nhau"],
    "σp = w₁σ₁ + w₂σ₂ chỉ khi ρ = +1; với mọi ρ < +1 thì σp nhỏ hơn bình quân gia quyền, nên đa dạng hóa có tác dụng (ρ càng thấp, tác dụng càng lớn; ρ = −1 có thể triệt tiêu rủi ro).",
    "Đa dạng hóa danh mục: mọi ρ < +1 đều làm giảm rủi ro danh mục")

add('PT', T_SL, 2,
    "Theo mô hình CAPM, lãi suất phi rủi ro dương và mức bù rủi ro thị trường không đổi. Nếu hệ số beta của một cổ phiếu tăng từ 0,8 lên 1,6 thì",
    "Mức bù rủi ro của cổ phiếu tăng gấp đôi, lợi suất yêu cầu tăng nhưng chưa tới gấp đôi",
    ["Lợi suất yêu cầu của cổ phiếu tăng đúng gấp đôi so với trước",
     "Mức bù rủi ro của danh mục thị trường tăng gấp đôi so với trước",
     "Rủi ro phi hệ thống của cổ phiếu tăng gấp đôi so với trước"],
    "E(Ri) = Rf + β[E(Rm) − Rf]. Mức bù rủi ro của cổ phiếu β[E(Rm) − Rf] tỷ lệ thuận với β nên tăng gấp đôi; do có thành phần Rf > 0 không đổi nên lợi suất yêu cầu tăng ít hơn gấp đôi.",
    "CAPM: E(Ri) = Rf + βi[E(Rm) − Rf]")

rf, rm, b, fc = 0.04, 0.11, 0.8, 0.13
req = rf + b * (rm - rf)
assert pct(req, 1) == "9,6%"
add('PT', T_SL, 3,
    "Lãi suất phi rủi ro 4%, lợi suất kỳ vọng của danh mục thị trường 11%. Cổ phiếu DEF có beta 0,8; nhà phân tích dự báo lợi suất kỳ vọng của DEF là 13%. Theo CAPM, nhận định nào đúng?",
    f"Lợi suất yêu cầu {pct(req, 1)}; DEF nằm phía trên đường SML, đang bị định giá thấp",
    [f"Lợi suất yêu cầu {pct(req, 1)}; DEF nằm phía dưới đường SML, đang bị định giá cao",
     f"Lợi suất yêu cầu {pct(rf + b * rm, 1)}; DEF được định giá xấp xỉ hợp lý theo SML",
     f"Lợi suất yêu cầu {pct(rf + b * fc, 1)}; DEF nằm phía dưới đường SML, đang bị định giá cao"],
    f"Lợi suất yêu cầu = 4% + 0,8×(11% − 4%) = {pct(req, 1)}. Lợi suất kỳ vọng 13% > {pct(req, 1)} (alpha = {pct(fc - req, 1)}) nên DEF nằm phía trên đường SML, bị định giá thấp – tín hiệu mua. Lỗi thường gặp: nhân beta với cả lợi suất thị trường (12,8%).",
    "CAPM/SML: E(Ri) = Rf + βi[E(Rm) − Rf]; alpha > 0 ⇒ nằm phía trên đường SML")

add('PT', T_SL, 1,
    "Loại rủi ro nào sau đây KHÔNG thể loại bỏ bằng cách đa dạng hóa danh mục đầu tư?",
    "Rủi ro do lãi suất và lạm phát của nền kinh tế thay đổi",
    ["Rủi ro do công ty bị mất một khách hàng lớn",
     "Rủi ro do ban điều hành công ty thay đổi đột ngột",
     "Rủi ro do một nhà máy của công ty bị hỏa hoạn"],
    "Rủi ro lãi suất, lạm phát là rủi ro hệ thống (rủi ro thị trường), tác động lên mọi chứng khoán nên không loại bỏ được bằng đa dạng hóa; các rủi ro riêng của từng công ty là rủi ro phi hệ thống.",
    "Phân loại rủi ro: rủi ro hệ thống và rủi ro phi hệ thống")

beta = 0.018 / 0.12**2
assert vn(beta) == "1,25"
add('PT', T_SL, 3,
    "Hiệp phương sai giữa lợi suất cổ phiếu GHI và lợi suất danh mục thị trường là 0,018; độ lệch chuẩn lợi suất của danh mục thị trường là 12%. Hệ số beta của cổ phiếu GHI là bao nhiêu?",
    vn(beta), [vn(0.018 / 0.12), vn(1 / beta), vn(0.018 / 0.012)],
    f"β = Cov(Ri, Rm)/σm² = 0,018/0,12² = 0,018/0,0144 = {vn(beta)}. Lỗi thường gặp: chia cho σm thay vì σm² (0,15) hoặc đảo ngược tỷ số (0,80).",
    "β = Cov(Ri, Rm)/σm²")

add('PT', T_SL, 1,
    "Chỉ số Sharpe đo lường điều gì?",
    "Mức sinh lời vượt lãi suất phi rủi ro trên mỗi đơn vị tổng rủi ro (độ lệch chuẩn)",
    ["Mức sinh lời vượt lãi suất phi rủi ro trên mỗi đơn vị rủi ro hệ thống (beta)",
     "Chênh lệch giữa lợi suất thực tế và lợi suất yêu cầu theo mô hình CAPM",
     "Mức độ chênh lệch lợi suất của danh mục so với chỉ số tham chiếu"],
    "Sharpe = (Rp − Rf)/σp. Chia cho beta là chỉ số Treynor; chênh lệch so với CAPM là alpha Jensen; chênh lệch so với chỉ số tham chiếu là tracking error.",
    "Chỉ số Sharpe = (Rp − Rf)/σp")

# =========================== PT: Thị trường hiệu quả & tài chính hành vi ===========================
add('PT', T_HQ, 1,
    "Theo giả thuyết thị trường hiệu quả dạng yếu, giá chứng khoán đã phản ánh đầy đủ",
    "Toàn bộ thông tin về giá và khối lượng giao dịch trong quá khứ",
    ["Toàn bộ thông tin đã công bố công khai, kể cả báo cáo tài chính",
     "Toàn bộ thông tin công khai và cả thông tin nội bộ chưa công bố",
     "Chỉ các thông tin kinh tế vĩ mô do cơ quan nhà nước công bố"],
    "Dạng yếu: giá phản ánh thông tin giá, khối lượng quá khứ (nên phân tích kỹ thuật không tạo lợi suất vượt trội). Dạng trung bình: thêm mọi thông tin công khai. Dạng mạnh: mọi thông tin kể cả nội bộ.",
    "Giả thuyết thị trường hiệu quả (EMH) – dạng yếu")

add('PT', T_HQ, 2,
    "Nếu thị trường hiệu quả ở dạng trung bình (bán mạnh) nhưng chưa đạt dạng mạnh, nhà đầu tư nào có khả năng đạt lợi suất vượt trội (sau điều chỉnh rủi ro) một cách nhất quán?",
    "Người giao dịch dựa trên thông tin nội bộ chưa được công bố",
    ["Người phân tích kỹ lưỡng các báo cáo tài chính đã công bố",
     "Người giao dịch theo các mô hình đồ thị giá và khối lượng",
     "Người mua ngay sau khi công ty công bố tăng mức cổ tức"],
    "Ở dạng trung bình, mọi thông tin công khai (BCTC, công bố cổ tức, dữ liệu giá) đã phản ánh vào giá; chỉ thông tin nội bộ chưa công bố mới có thể tạo lợi suất vượt trội vì thị trường chưa đạt dạng mạnh.",
    "Giả thuyết thị trường hiệu quả (EMH) – dạng trung bình và dạng mạnh")

add('PT', T_HQ, 1,
    "Dạng hiệu quả nào của thị trường cho rằng giá chứng khoán phản ánh mọi thông tin, bao gồm cả thông tin nội bộ?",
    "Dạng mạnh",
    ["Dạng trung bình (bán mạnh)", "Dạng yếu", "Dạng hiệu quả về phân bổ vốn"],
    "Dạng mạnh: giá phản ánh mọi thông tin (quá khứ, công khai và nội bộ), nên không ai đạt lợi suất vượt trội một cách nhất quán.",
    "Giả thuyết thị trường hiệu quả (EMH) – dạng mạnh")

add('PT', T_HQ, 2,
    "Nhà đầu tư thường bán sớm cổ phiếu đang có lãi để “chốt lời” nhưng lại tiếp tục nắm giữ cổ phiếu đang thua lỗ với hy vọng giá sẽ hồi phục. Theo tài chính hành vi, đây là biểu hiện của",
    "Hiệu ứng bán lời, giữ lỗ (disposition effect)",
    ["Hiệu ứng mỏ neo (anchoring)", "Tâm lý bầy đàn (herding)", "Thiên lệch quá tự tin (overconfidence)"],
    "Disposition effect xuất phát từ tâm lý né tránh thua lỗ: nhà đầu tư ngại hiện thực hóa khoản lỗ nên giữ cổ phiếu lỗ quá lâu và bán cổ phiếu lãi quá sớm.",
    "Tài chính hành vi: né tránh thua lỗ, hiệu ứng bán lời giữ lỗ")

add('PT', T_HQ, 2,
    "Một chuyên viên phân tích đưa ra dự báo EPS ban đầu là 5.000 đồng; khi có thông tin mới bất lợi, anh ta chỉ điều chỉnh dự báo rất ít so với con số ban đầu. Đây là biểu hiện của thiên lệch hành vi nào?",
    "Hiệu ứng mỏ neo (anchoring)",
    ["Tâm lý bầy đàn (herding)", "Hiệu ứng bán lời, giữ lỗ (disposition effect)", "Thiên lệch kế toán tâm lý (mental accounting)"],
    "Hiệu ứng mỏ neo: bám vào một con số ban đầu (điểm neo) và điều chỉnh không đủ khi có thông tin mới.",
    "Tài chính hành vi: hiệu ứng mỏ neo")

# =========================== PT: Phân tích kinh tế ===========================
add('PT', T_KT, 2,
    "Khi mặt bằng lãi suất thị trường tăng mạnh và các yếu tố khác không đổi, tác động nào sau đây là hợp lý nhất đối với thị trường cổ phiếu?",
    "Tỷ suất chiết khấu yêu cầu tăng làm giá trị nội tại của cổ phiếu giảm",
    ["Hệ số P/E hợp lý của thị trường có xu hướng tăng lên",
     "Chi phí vốn của doanh nghiệp giảm, lợi nhuận kỳ vọng tăng",
     "Dòng tiền có xu hướng chuyển từ tiền gửi sang cổ phiếu"],
    "Lãi suất tăng làm tăng lãi suất phi rủi ro và tỷ suất chiết khấu, tăng chi phí vốn, làm giảm giá trị hiện tại của dòng tiền tương lai và P/E hợp lý; kênh tiền gửi hấp dẫn hơn.",
    "Tác động của lãi suất đến định giá: P0 = Σ CFt/(1 + r)^t")

real = 1.09 / 1.04 - 1
assert pct(real) == "4,81%"
add('PT', T_KT, 3,
    "Lãi suất danh nghĩa của trái phiếu Chính phủ kỳ hạn 1 năm là 9%/năm, tỷ lệ lạm phát dự kiến 4%/năm. Theo phương trình Fisher dạng chính xác, lãi suất thực là bao nhiêu?",
    pct(real), [pct(0.05), pct(1.09 * 1.04 - 1), pct(0.05 / 1.09)],
    f"(1 + i) = (1 + r)(1 + π) ⇒ r = 1,09/1,04 − 1 = {pct(real)}. 5,00% là kết quả xấp xỉ i − π; 13,36% là nhân thay vì chia.",
    "Phương trình Fisher: (1 + i) = (1 + r)(1 + π)")

add('PT', T_KT, 1,
    "Chỉ báo nào sau đây thường được xếp vào nhóm chỉ báo dẫn dắt (chỉ báo sớm) của chu kỳ kinh tế?",
    "Chỉ số giá cổ phiếu trên thị trường chứng khoán",
    ["Thời gian thất nghiệp bình quân", "Chỉ số sản xuất công nghiệp", "Lãi suất cho vay bình quân của ngân hàng"],
    "Chỉ số giá cổ phiếu thường biến động trước chu kỳ kinh tế (chỉ báo dẫn dắt); sản xuất công nghiệp là chỉ báo trùng hợp; thời gian thất nghiệp bình quân, lãi suất cho vay bình quân là chỉ báo trễ.",
    "Phân tích vĩ mô: chỉ báo dẫn dắt, trùng hợp, trễ")

add('PT', T_KT, 2,
    "Khi nền kinh tế bước vào giai đoạn suy thoái, nhóm ngành nào thường có lợi nhuận ít biến động nhất (ngành phòng thủ)?",
    "Hàng tiêu dùng thiết yếu, dược phẩm, điện nước",
    ["Bất động sản và vật liệu xây dựng", "Ô tô và hàng tiêu dùng lâu bền", "Chứng khoán và dịch vụ tài chính"],
    "Nhu cầu hàng thiết yếu, thuốc, điện nước ít co giãn theo thu nhập nên lợi nhuận ổn định (ngành phòng thủ); các ngành còn lại là ngành chu kỳ.",
    "Phân tích ngành: ngành chu kỳ và ngành phòng thủ")

add('PT', T_KT, 2,
    "Một ngành có doanh thu tăng trưởng nhanh, lợi nhuận tăng mạnh, nhu cầu vốn đầu tư mở rộng lớn nên doanh nghiệp thường trả cổ tức tiền mặt thấp. Ngành này đang ở giai đoạn nào của vòng đời?",
    "Giai đoạn tăng trưởng",
    ["Giai đoạn khởi sự (hình thành)", "Giai đoạn bão hòa (chín muồi)", "Giai đoạn suy thoái"],
    "Giai đoạn tăng trưởng: doanh thu và lợi nhuận tăng nhanh, cần nhiều vốn tái đầu tư nên chi trả cổ tức thấp. Khởi sự thường chưa có lãi; bão hòa tăng trưởng chậm, cổ tức cao; suy thoái doanh thu giảm.",
    "Phân tích ngành: vòng đời ngành")

add('PT', T_KT, 1,
    "Yếu tố nào sau đây KHÔNG thuộc mô hình năm áp lực cạnh tranh của Michael Porter?",
    "Chính sách tiền tệ của ngân hàng trung ương",
    ["Mối đe dọa từ các sản phẩm thay thế", "Quyền thương lượng của nhà cung cấp", "Nguy cơ gia nhập ngành của đối thủ tiềm năng"],
    "Năm áp lực: cạnh tranh nội bộ ngành, đe dọa gia nhập, sản phẩm thay thế, quyền thương lượng của người mua và của nhà cung cấp. Chính sách tiền tệ là yếu tố vĩ mô.",
    "Mô hình năm áp lực cạnh tranh của Porter")

add('PT', T_KT, 2,
    "Khi VND mất giá so với USD và các yếu tố khác không đổi, nhóm doanh nghiệp nào hưởng lợi trực tiếp nhất?",
    "Doanh nghiệp xuất khẩu có doanh thu bằng USD, chi phí chủ yếu bằng VND",
    ["Doanh nghiệp nhập khẩu phần lớn nguyên vật liệu đầu vào",
     "Doanh nghiệp có dư nợ vay USD lớn, doanh thu bằng VND",
     "Doanh nghiệp phân phối hàng nhập khẩu tại thị trường nội địa"],
    "VND mất giá làm doanh thu USD quy đổi tăng trong khi chi phí VND không đổi; các doanh nghiệp nhập khẩu hoặc vay nợ USD bị tăng chi phí, tăng nghĩa vụ nợ quy đổi.",
    "Phân tích vĩ mô: tác động của tỷ giá")

# =========================== PT: Cổ phiếu ===========================
P0 = 2000 * 1.06 / (0.14 - 0.06)
assert round(P0) == 26500
add('PT', T_CP, 3,
    "Công ty vừa trả cổ tức D0 = 2.000 đồng/cp. Cổ tức được kỳ vọng tăng trưởng đều 6%/năm mãi mãi; tỷ suất sinh lời yêu cầu của nhà đầu tư là 14%/năm. Giá trị nội tại của cổ phiếu theo mô hình Gordon là",
    vn(P0, 0) + " đồng", [vn(2000 / 0.08, 0) + " đồng", vn(2120 / 0.14, 0) + " đồng", vn(2120 / 0.20, 0) + " đồng"],
    f"D1 = 2.000 × 1,06 = 2.120 đồng; P0 = D1/(r − g) = 2.120/(14% − 6%) = {vn(P0, 0)} đồng. Lỗi thường gặp: dùng D0 (25.000), bỏ g ở mẫu số (15.143), cộng g vào mẫu số (10.600).",
    "Mô hình Gordon: P0 = D1/(r − g)")

D0, r_, g1, g2 = 1000, 0.12, 0.20, 0.05
D1, D2 = D0 * 1.2, D0 * 1.2**2
D3 = D2 * (1 + g2)
P2 = D3 / (r_ - g2)
P0 = D1 / 1.12 + (D2 + P2) / 1.12**2
P0_a = D1 / 1.12 + (D2 + D2 / (r_ - g2)) / 1.12**2
P0_b = D1 / 1.12 + D2 / 1.12**2 + P2 / 1.12
P0_c = D0 * 1.05 / 0.07
assert round(P0) == 19439 and round(P2) == 21600
add('PT', T_CP, 3,
    "Công ty vừa trả cổ tức D0 = 1.000 đồng/cp. Cổ tức dự kiến tăng 20%/năm trong 2 năm tới, sau đó tăng đều 5%/năm mãi mãi. Tỷ suất sinh lời yêu cầu là 12%/năm. Giá trị nội tại hiện tại của cổ phiếu (làm tròn đến đồng) là",
    vn(P0, 0) + " đồng", [vn(P0_a, 0) + " đồng", vn(P0_b, 0) + " đồng", vn(P0_c, 0) + " đồng"],
    f"D1 = 1.200; D2 = 1.440; D3 = 1.440 × 1,05 = 1.512. P2 = D3/(12% − 5%) = {vn(P2, 0)}. P0 = 1.200/1,12 + (1.440 + {vn(P2, 0)})/1,12² = {vn(D1 / 1.12, 2)} + {vn((D2 + P2) / 1.12**2, 2)} = {vn(P0, 0)} đồng. Lỗi thường gặp: tính P2 bằng D2 thay vì D3 ({vn(P0_a, 0)}), chiết khấu P2 một kỳ ({vn(P0_b, 0)}), dùng Gordon một giai đoạn ({vn(P0_c, 0)}).",
    "Mô hình chiết khấu cổ tức hai giai đoạn: P0 = Σ Dt/(1 + r)^t + Pn/(1 + r)^n, Pn = Dn+1/(r − g)")

add('PT', T_CP, 2,
    "Cổ phiếu A có P/E cao hơn đáng kể so với P/E bình quân của các doanh nghiệp cùng ngành. Nếu thị trường định giá hợp lý, điều này phù hợp nhất với giả thiết nào?",
    "Nhà đầu tư kỳ vọng tăng trưởng lợi nhuận của A cao hơn hoặc rủi ro của A thấp hơn",
    ["Tỷ suất sinh lời yêu cầu đối với A cao hơn mức bình quân của ngành",
     "Tỷ lệ chi trả cổ tức và tốc độ tăng trưởng của A đều thấp hơn ngành",
     "A có EPS cao hơn ngành nên giá cổ phiếu và P/E cũng cao hơn ngành"],
    "P/E hợp lý = tỷ lệ chi trả/(r − g): P/E cao tương ứng g cao hơn và/hoặc r thấp hơn (rủi ro thấp hơn). EPS cao bản thân nó không làm P/E cao.",
    "P/E hợp lý = (D1/E1)/(r − g)")

g = 0.15 * 0.6
pe = 0.4 / (0.12 - g)
assert vn(pe) == "13,33"
add('PT', T_CP, 3,
    "Công ty có ROE ổn định 15%, tỷ lệ chi trả cổ tức 40%, tỷ suất sinh lời yêu cầu 12%. Giả định công ty tăng trưởng ổn định mãi mãi với g = ROE × tỷ lệ lợi nhuận giữ lại. Hệ số P/E kỳ vọng hợp lý (P0/E1) là",
    vn(pe) + " lần", [vn(0.4 * (1 + g) / (0.12 - g)) + " lần", vn(0.6 / (0.12 - g)) + " lần", vn(0.4 / (0.12 - 0.15 * 0.4)) + " lần"],
    f"g = 15% × (1 − 40%) = 9%; P0/E1 = tỷ lệ chi trả/(r − g) = 0,4/(12% − 9%) = {vn(pe)} lần. Lỗi thường gặp: tính P/E hiện hành P0/E0 = 0,4×1,09/0,03 (14,53), dùng tỷ lệ giữ lại ở tử số (20,00), tính g = ROE × tỷ lệ chi trả (6,67).",
    "P/E kỳ vọng hợp lý: P0/E1 = (1 − b)/(r − g), g = ROE × b")

add('PT', T_CP, 2,
    "Phương pháp định giá dựa trên hệ số P/B thường được ưu tiên áp dụng cho nhóm doanh nghiệp nào?",
    "Ngân hàng, công ty chứng khoán có tài sản chủ yếu là tài sản tài chính",
    ["Doanh nghiệp công nghệ có nhiều tài sản vô hình chưa được ghi nhận",
     "Doanh nghiệp dịch vụ có rất ít tài sản hữu hình trên sổ sách",
     "Doanh nghiệp khởi nghiệp đang có vốn chủ sở hữu âm kéo dài"],
    "Giá trị sổ sách của tổ chức tài chính phản ánh khá sát giá trị thị trường của tài sản tài chính, nên P/B phù hợp; với doanh nghiệp có nhiều tài sản vô hình không ghi nhận hoặc vốn chủ âm, P/B kém ý nghĩa.",
    "Định giá theo P/B = giá thị trường/giá trị sổ sách mỗi cổ phần")

ev = 500 * 8
eq = ev - 1200 + 200
assert eq == 3000
add('PT', T_CP, 3,
    "Công ty XYZ có EBITDA dự phóng 500 tỷ đồng; hệ số EV/EBITDA bình quân của các doanh nghiệp so sánh là 8 lần. XYZ có tổng nợ vay 1.200 tỷ đồng, tiền và tương đương tiền 200 tỷ đồng, 100 triệu cổ phiếu đang lưu hành, không có cổ phần ưu đãi và lợi ích cổ đông không kiểm soát. Giá trị hợp lý mỗi cổ phiếu là",
    vn(eq * 1e9 / 1e8, 0) + " đồng", [vn((ev - 1200) * 10, 0) + " đồng", vn((ev - 1200 - 200) * 10, 0) + " đồng", vn(ev * 10, 0) + " đồng"],
    f"EV = 8 × 500 = {vn(ev, 0)} tỷ; giá trị vốn chủ = EV − nợ vay + tiền = 4.000 − 1.200 + 200 = {vn(eq, 0)} tỷ; mỗi cổ phiếu = 3.000 tỷ/100 triệu = 30.000 đồng. Lỗi thường gặp: không cộng tiền (28.000), trừ cả tiền (26.000), coi EV là giá trị vốn chủ (40.000).",
    "EV/EBITDA: giá trị vốn chủ = EV − nợ vay + tiền và tương đương tiền")

fcfe = 200 + 50 - 120 - 30 + (70 - 30)
assert fcfe == 140
add('PT', T_CP, 3,
    "Năm tới, công ty dự kiến (tỷ đồng): lợi nhuận sau thuế 200; khấu hao 50; chi đầu tư TSCĐ 120; vốn lưu động (không kể tiền) tăng 30; vay nợ mới 70 và trả nợ gốc 30. Dòng tiền tự do vốn chủ sở hữu (FCFE) là",
    f"{fcfe} tỷ đồng", ["100 tỷ đồng", "170 tỷ đồng", "200 tỷ đồng"],
    "FCFE = LNST + khấu hao − chi đầu tư TSCĐ − tăng vốn lưu động + vay ròng = 200 + 50 − 120 − 30 + (70 − 30) = 140 tỷ đồng. Lỗi thường gặp: bỏ vay ròng (100), cộng vay mới gộp (170), cộng thay vì trừ tăng vốn lưu động (200).",
    "FCFE = LNST + khấu hao − CAPEX − ΔVLĐ + vay ròng")

fcff = 300 * (1 - 0.2) + 60 - 100 - 20
assert fcff == 180
add('PT', T_CP, 3,
    "Năm tới, công ty dự kiến (tỷ đồng): EBIT 300; thuế suất thuế TNDN 20%; khấu hao 60; chi đầu tư TSCĐ 100; vốn lưu động (không kể tiền) tăng 20. Dòng tiền tự do doanh nghiệp (FCFF) là",
    f"{fcff:.0f} tỷ đồng", ["240 tỷ đồng", "120 tỷ đồng", "220 tỷ đồng"],
    "FCFF = EBIT(1 − t) + khấu hao − CAPEX − ΔVLĐ = 300 × 0,8 + 60 − 100 − 20 = 180 tỷ đồng. Lỗi thường gặp: không trừ thuế (240), bỏ khấu hao (120), cộng ΔVLĐ (220).",
    "FCFF = EBIT(1 − t) + khấu hao − CAPEX − ΔVLĐ")

add('PT', T_CP, 2,
    "Trong trường hợp nào định giá bằng mô hình chiết khấu FCFF thường phù hợp hơn mô hình FCFE?",
    "Doanh nghiệp có đòn bẩy cao hoặc cơ cấu vốn dự kiến thay đổi đáng kể",
    ["Doanh nghiệp trả cổ tức ổn định, tương xứng với khả năng tạo tiền",
     "Doanh nghiệp có cơ cấu vốn ổn định và FCFE dự báo được tin cậy",
     "Ngân hàng thương mại có hoạt động chính là huy động và cho vay"],
    "Khi nợ vay lớn hoặc cơ cấu vốn biến động, FCFE khó dự báo (phụ thuộc vay ròng) nên dùng FCFF chiết khấu bằng WACC rồi trừ nợ. Cổ tức ổn định phù hợp DDM; ngân hàng thường dùng P/B hoặc thu nhập thặng dư.",
    "Lựa chọn mô hình FCFF (chiết khấu bằng WACC) và FCFE (chiết khấu bằng chi phí vốn chủ)")

add('PT', T_CP, 1,
    "Mô hình tăng trưởng cổ tức không đổi (Gordon) chỉ cho kết quả có ý nghĩa khi",
    "Tỷ suất sinh lời yêu cầu lớn hơn tốc độ tăng trưởng cổ tức và g không đổi mãi mãi",
    ["Tốc độ tăng trưởng cổ tức lớn hơn tỷ suất sinh lời yêu cầu của nhà đầu tư",
     "Doanh nghiệp không chi trả cổ tức trong một số năm đầu của kỳ dự báo",
     "Tốc độ tăng trưởng cổ tức thay đổi mạnh qua từng giai đoạn phát triển"],
    "P0 = D1/(r − g) chỉ xác định khi r > g và g ổn định vĩnh viễn; nếu g thay đổi qua các giai đoạn cần dùng mô hình nhiều giai đoạn.",
    "Mô hình Gordon: P0 = D1/(r − g), điều kiện r > g")

wacc = 0.6 * 0.15 + 0.4 * 0.10 * (1 - 0.2)
assert pct(wacc, 1) == "12,2%"
add('PT', T_CP, 3,
    "Cơ cấu vốn mục tiêu của công ty: 60% vốn chủ sở hữu, 40% nợ vay. Chi phí vốn chủ sở hữu 15%, lãi suất vay trước thuế 10%, thuế suất thuế TNDN 20%. Chi phí vốn bình quân gia quyền (WACC) là",
    pct(wacc, 1), [pct(0.6 * 0.15 + 0.4 * 0.10, 1), pct(0.4 * 0.15 + 0.6 * 0.08, 1), pct((0.15 + 0.08) / 2, 1)],
    f"WACC = 60% × 15% + 40% × 10% × (1 − 20%) = 9% + 3,2% = {pct(wacc, 1)}. Lỗi thường gặp: bỏ lá chắn thuế (13,0%), đảo tỷ trọng (10,8%), lấy bình quân giản đơn (11,5%).",
    "WACC = wE × rE + wD × rD × (1 − t)")


# =========================== PT: Trái phiếu ===========================
def price(c, y, n, f=1, F=100000):
    cp = F * c / f
    return sum(cp / (1 + y / f) ** t for t in range(1, n * f + 1)) + F / (1 + y / f) ** (n * f)


P = price(0.08, 0.10, 3)
assert round(P) == 95026
P_semi = price(0.08, 0.10, 3, 2)
P_sw = price(0.10, 0.08, 3)
P_pr = 24000 + 100000 / 1.1**3
add('PT', T_TP, 3,
    "Trái phiếu mệnh giá 100.000 đồng, lãi suất coupon 8%/năm, trả lãi mỗi năm một lần, còn đúng 3 năm đến hạn (vừa trả coupon). Nếu lợi suất đáo hạn yêu cầu là 10%/năm, giá trái phiếu (làm tròn đến đồng) là",
    vn(P, 0) + " đồng", [vn(P_sw, 0) + " đồng", vn(P_semi, 0) + " đồng", vn(P_pr, 0) + " đồng"],
    f"P = 8.000/1,1 + 8.000/1,1² + 108.000/1,1³ = 7.272,73 + 6.611,57 + 81.142,00 = {vn(P, 0)} đồng. Lỗi thường gặp: đảo coupon và lợi suất ({vn(P_sw, 0)}), tính như trả lãi nửa năm ({vn(P_semi, 0)}), không chiết khấu coupon ({vn(P_pr, 0)}).",
    "Giá trái phiếu: P = Σ C/(1 + y)^t + F/(1 + y)^n")

mkt = round(price(0.06, 0.08, 2))
assert mkt == 96433
lo, hi = 0.0, 0.5
for _ in range(200):
    mid = (lo + hi) / 2
    lo, hi = (mid, hi) if price(0.06, mid, 2) > mkt else (lo, mid)
ytm = (lo + hi) / 2
assert pct(ytm) == "8,00%"
add('PT', T_TP, 3,
    "Trái phiếu mệnh giá 100.000 đồng, lãi suất coupon 6%/năm trả hằng năm, còn đúng 2 năm đến hạn (vừa trả coupon), đang giao dịch ở giá 96.433 đồng. Lợi suất đáo hạn (YTM) của trái phiếu xấp xỉ bằng",
    pct(ytm), [pct(0.06), pct(6000 / mkt), pct((6000 + 100000 - mkt) / mkt)],
    f"YTM là y thỏa mãn 96.433 = 6.000/(1 + y) + 106.000/(1 + y)². Thử y = 8%: 5.555,56 + 90.877,89 = 96.433 ⇒ YTM ≈ {pct(ytm)}. 6,00% là lãi suất coupon; {pct(6000 / mkt)} là lợi suất hiện hành; {pct((6000 + 100000 - mkt) / mkt)} là gộp toàn bộ chênh lệch giá vào một năm.",
    "Lợi suất đáo hạn: P = Σ C/(1 + YTM)^t + F/(1 + YTM)^n")

cy = 9000 / 95000
assert pct(cy) == "9,47%"
add('PT', T_TP, 3,
    "Trái phiếu mệnh giá 100.000 đồng, lãi suất coupon 9%/năm (trả hằng năm), đang giao dịch ở giá 95.000 đồng. Lợi suất hiện hành của trái phiếu là",
    pct(cy), [pct(0.09), pct(9000 * 0.95 / 100000), pct(14000 / 95000)],
    f"Lợi suất hiện hành = coupon năm/giá thị trường = 9.000/95.000 = {pct(cy)}. 9,00% là lãi suất coupon; 14,74% là cộng cả chênh lệch giá 5.000 vào tử số.",
    "Lợi suất hiện hành = coupon hằng năm/giá thị trường")

cfs = [10000, 10000, 110000]
pvs = [c / 1.1 ** (t + 1) for t, c in enumerate(cfs)]
dmac = sum((t + 1) * v for t, v in enumerate(pvs)) / sum(pvs)
dmod = dmac / 1.1
assert vn(dmac) == "2,74" and vn(dmod) == "2,49"
add('PT', T_TP, 3,
    "Trái phiếu mệnh giá 100.000 đồng, kỳ hạn còn lại 3 năm, coupon 10%/năm trả hằng năm, lợi suất đáo hạn 10%/năm. Thời gian đáo hạn bình quân Macaulay (Macaulay duration) của trái phiếu là",
    vn(dmac) + " năm", ["3,00 năm", vn(dmod) + " năm", "2,00 năm"],
    f"PV dòng tiền: 9.090,91; 8.264,46; 82.644,63 (tổng 100.000). D = (1×9.090,91 + 2×8.264,46 + 3×82.644,63)/100.000 = {vn(dmac, 4)} ≈ {vn(dmac)} năm. 3,00 là kỳ hạn; {vn(dmod)} là duration điều chỉnh D/(1 + y).",
    "Duration Macaulay: D = Σ t × PV(CFt)/P")

d_ok = -6.5 * 0.01 + 0.5 * 60 * 0.01**2
assert abs(d_ok + 0.062) < 1e-12
add('PT', T_TP, 3,
    "Trái phiếu có duration điều chỉnh (modified duration) 6,5 và độ lồi (convexity) 60, theo quy ước %ΔP ≈ −MD × Δy + ½ × C × (Δy)². Nếu lợi suất đáo hạn tăng 100 điểm cơ bản, giá trái phiếu thay đổi xấp xỉ",
    pct(d_ok), [pct(-6.5 * 0.01 - 0.5 * 60 * 0.0001), pct(-0.065), pct(-6.5 * 0.01 + 60 * 0.0001)],
    f"%ΔP ≈ −6,5 × 0,01 + ½ × 60 × 0,01² = −6,50% + 0,30% = {pct(d_ok)}. Độ lồi luôn cộng thêm (với độ lồi dương) bất kể lãi suất tăng hay giảm. Lỗi thường gặp: trừ phần độ lồi (−6,80%), bỏ độ lồi (−6,50%), quên hệ số ½ (−5,90%).",
    "%ΔP ≈ −MD × Δy + ½ × Convexity × (Δy)²")

add('PT', T_TP, 2,
    "Đối với trái phiếu thông thường (không có quyền chọn), các yếu tố khác không đổi, thay đổi nào sau đây làm duration của trái phiếu tăng lên?",
    "Lãi suất coupon của trái phiếu thấp hơn",
    ["Lợi suất đáo hạn của trái phiếu cao hơn",
     "Thời gian còn lại đến khi đáo hạn ngắn hơn",
     "Gốc được trả dần hằng năm thay vì trả một lần"],
    "Coupon thấp làm tỷ trọng giá trị dòng tiền cuối kỳ lớn hơn nên duration dài hơn. Lợi suất cao hơn, kỳ hạn ngắn hơn hoặc trả gốc dần đều làm duration ngắn lại.",
    "Các nhân tố ảnh hưởng đến duration: coupon, kỳ hạn, lợi suất đáo hạn")

add('PT', T_TP, 1,
    "Một trái phiếu được giao dịch dưới mệnh giá (trái phiếu chiết khấu) khi",
    "Lãi suất coupon thấp hơn lợi suất đáo hạn yêu cầu của thị trường",
    ["Lãi suất coupon cao hơn lợi suất đáo hạn yêu cầu của thị trường",
     "Lãi suất coupon bằng lợi suất đáo hạn yêu cầu của thị trường",
     "Lợi suất hiện hành của trái phiếu thấp hơn lãi suất coupon"],
    "Coupon < YTM ⇒ P < mệnh giá; coupon > YTM ⇒ P > mệnh giá; bằng nhau ⇒ P = mệnh giá. Với trái phiếu chiết khấu, lợi suất hiện hành lớn hơn lãi suất coupon.",
    "Quan hệ giữa giá trái phiếu, lãi suất coupon và lợi suất đáo hạn")

# =========================== PT: Phân tích kỹ thuật ===========================
add('PT', T_KTH, 2,
    "Trên đồ thị giá ngày, đường trung bình động ngắn hạn MA20 cắt đường trung bình động dài hạn MA50 từ dưới lên trên. Theo phân tích kỹ thuật truyền thống, đây là",
    "Tín hiệu mua (giao cắt vàng – golden cross)",
    ["Tín hiệu bán (giao cắt tử thần – death cross)",
     "Tín hiệu cổ phiếu rơi vào vùng quá mua",
     "Tín hiệu xác nhận xu hướng giảm trung hạn"],
    "MA ngắn hạn cắt MA dài hạn từ dưới lên cho thấy giá gần đây tăng nhanh hơn mặt bằng dài hạn – tín hiệu mua (golden cross). Cắt từ trên xuống là tín hiệu bán (death cross).",
    "Đường trung bình động: giao cắt MA ngắn hạn và dài hạn")

add('PT', T_KTH, 1,
    "Theo cách diễn giải thông thường, chỉ báo RSI(14) vượt lên trên mức 70 cho thấy",
    "Cổ phiếu ở vùng quá mua, có khả năng điều chỉnh giảm",
    ["Cổ phiếu ở vùng quá bán, có khả năng hồi phục tăng",
     "Khối lượng giao dịch đang tăng đột biến bất thường",
     "Giá đã phá vỡ ngưỡng hỗ trợ dài hạn của cổ phiếu"],
    "RSI > 70: vùng quá mua; RSI < 30: vùng quá bán. RSI đo động lượng giá, không đo khối lượng.",
    "Chỉ báo RSI: ngưỡng 70 (quá mua) và 30 (quá bán)")

rs = 1500 / 500
rsi = 100 - 100 / (1 + rs)
assert rsi == 75
add('PT', T_KTH, 3,
    "Trong 14 phiên gần nhất, mức tăng giá bình quân là 1.500 đồng và mức giảm giá bình quân là 500 đồng (cả hai tính bình quân trên 14 phiên). Giá trị RSI(14) và cách diễn giải phù hợp là",
    f"RSI = {vn(rsi, 0)}; cổ phiếu ở vùng quá mua",
    [f"RSI = {vn(100 - 100 / (1 + 1 / rs), 0)}; cổ phiếu ở vùng quá bán",
     f"RSI = {vn(100 - 100 / rs)}; cổ phiếu ở vùng trung tính",
     f"RSI = {vn(rsi, 0)}; cổ phiếu ở vùng quá bán"],
    f"RS = 1.500/500 = 3; RSI = 100 − 100/(1 + RS) = 100 − 25 = {vn(rsi, 0)} > 70 ⇒ vùng quá mua. Lỗi thường gặp: đảo tỷ số RS (25), dùng 100 − 100/RS (66,67).",
    "RSI = 100 − 100/(1 + RS), RS = mức tăng bình quân/mức giảm bình quân")

macd = 25.4 - 24.6
assert abs(macd - 0.8) < 1e-9
add('PT', T_KTH, 3,
    "Phiên hôm qua, đường MACD của cổ phiếu nằm phía trên đường tín hiệu. Phiên hôm nay: EMA12 = 25,4; EMA26 = 24,6 (nghìn đồng); đường tín hiệu (EMA9 của MACD) = 0,95. Giá trị MACD hôm nay và tín hiệu tương ứng là",
    f"MACD = {vn(macd)}; cắt đường tín hiệu từ trên xuống – tín hiệu bán",
    [f"MACD = {vn(macd)}; cắt đường tín hiệu từ dưới lên – tín hiệu mua",
     f"MACD = {vn(-macd)}; nằm phía dưới đường 0 – tín hiệu bán",
     f"MACD = {vn(0.95 - macd)}; nằm phía trên đường 0 – tín hiệu mua"],
    "MACD = EMA12 − EMA26 = 25,4 − 24,6 = 0,80. Hôm qua MACD nằm phía trên đường tín hiệu, hôm nay 0,80 < 0,95 ⇒ MACD cắt đường tín hiệu từ trên xuống – tín hiệu bán.",
    "MACD = EMA12 − EMA26; đường tín hiệu = EMA9 của MACD")

add('PT', T_KTH, 2,
    "Giá cổ phiếu vượt dứt khoát ngưỡng kháng cự 30.000 đồng với khối lượng giao dịch lớn. Theo phân tích kỹ thuật truyền thống, ngưỡng 30.000 đồng sau đó thường",
    "Đóng vai trò ngưỡng hỗ trợ mới khi giá điều chỉnh",
    ["Trở thành ngưỡng kháng cự mạnh hơn so với trước",
     "Báo hiệu xu hướng tăng của cổ phiếu đã kết thúc",
     "Không còn ý nghĩa kỹ thuật nào đối với cổ phiếu"],
    "Khi kháng cự bị phá vỡ dứt khoát (có khối lượng xác nhận), vùng giá này thường đảo vai trò thành hỗ trợ (nguyên lý đổi vai hỗ trợ – kháng cự).",
    "Ngưỡng hỗ trợ và kháng cự: nguyên lý đổi vai")

add('PT', T_KTH, 1,
    "Giả định nào sau đây là nền tảng của phân tích kỹ thuật?",
    "Giá phản ánh mọi yếu tố, vận động theo xu hướng và lịch sử có xu hướng lặp lại",
    ["Giá cổ phiếu luôn hội tụ về giá trị nội tại xác định từ báo cáo tài chính",
     "Biến động giá là hoàn toàn ngẫu nhiên nên không thể dự báo được",
     "Giá cổ phiếu chỉ phụ thuộc vào lợi nhuận và cổ tức dự kiến"],
    "Ba giả định của phân tích kỹ thuật (lý thuyết Dow): thị trường phản ánh tất cả, giá vận động theo xu hướng, lịch sử lặp lại. Các phương án khác là quan điểm của phân tích cơ bản hoặc bước ngẫu nhiên.",
    "Giả định cơ bản của phân tích kỹ thuật")

# =========================== BC: Tổng quan ===========================
add('BC', B_TQ, 1,
    "Phương pháp so sánh số liệu của cùng một chỉ tiêu tài chính qua nhiều kỳ (cả số tuyệt đối và tỷ lệ thay đổi) để đánh giá xu hướng biến động được gọi là",
    "Phân tích theo chiều ngang (phân tích xu hướng)",
    ["Phân tích theo chiều dọc (quy mô chung)", "Phân tích Dupont", "Phân tích độ nhạy"],
    "Phân tích ngang so sánh một chỉ tiêu giữa các kỳ; phân tích dọc biểu diễn khoản mục theo tỷ lệ % so với một chỉ tiêu gốc trong cùng kỳ.",
    "Phương pháp so sánh theo chiều ngang trong phân tích BCTC")

lnkd = 800 - 560 + 12 - 32 - 48 - 40
assert lnkd == 132
add('BC', B_TQ, 3,
    "Báo cáo kết quả hoạt động kinh doanh năm N của công ty (tỷ đồng): doanh thu thuần 800; giá vốn hàng bán 560; doanh thu hoạt động tài chính 12; chi phí tài chính 32; chi phí bán hàng 48; chi phí quản lý doanh nghiệp 40. Trên báo cáo dạng quy mô chung (% doanh thu thuần), tỷ lệ lợi nhuận thuần từ hoạt động kinh doanh là",
    pct(lnkd / 800), [pct(152 / 800), pct(120 / 800), pct(240 / 800)],
    "LN thuần từ HĐKD = 800 − 560 + 12 − 32 − 48 − 40 = 132; tỷ lệ = 132/800 = 16,50%. Lỗi thường gặp: bỏ hoạt động tài chính (19,00%), bỏ doanh thu tài chính (15,00%), nhầm với biên lợi nhuận gộp (30,00%).",
    "Phân tích quy mô chung: khoản mục/doanh thu thuần")

add('BC', B_TQ, 2,
    "Một ngân hàng đang thẩm định khoản vay bổ sung vốn lưu động kỳ hạn 6 tháng cho doanh nghiệp. Nhóm chỉ tiêu nào ngân hàng cần quan tâm trước tiên?",
    "Khả năng thanh toán ngắn hạn và dòng tiền từ hoạt động kinh doanh",
    ["Các chỉ tiêu giá thị trường như P/E, P/B của cổ phiếu",
     "Tốc độ tăng trưởng doanh thu dài hạn trong 5–10 năm tới",
     "Cơ cấu cổ đông và tỷ lệ sở hữu của nhà đầu tư nước ngoài"],
    "Chủ nợ ngắn hạn quan tâm khả năng trả nợ trong ngắn hạn: hệ số thanh toán, chất lượng tài sản ngắn hạn và dòng tiền HĐKD.",
    "Đối tượng sử dụng BCTC và mục tiêu phân tích")

add('BC', B_TQ, 1,
    "Khi phân tích báo cáo tình hình tài chính (bảng cân đối kế toán) theo chiều dọc, mỗi khoản mục thường được biểu diễn dưới dạng tỷ lệ % so với",
    "Tổng tài sản (tổng nguồn vốn)",
    ["Doanh thu thuần trong kỳ", "Vốn chủ sở hữu cuối kỳ", "Chính khoản mục đó ở kỳ gốc"],
    "Phân tích dọc bảng cân đối lấy tổng tài sản (= tổng nguồn vốn) làm gốc 100%; với báo cáo KQKD gốc là doanh thu thuần; so với kỳ gốc là phân tích ngang.",
    "Phân tích theo chiều dọc (quy mô chung)")

# =========================== BC: Hệ thống BCTC ===========================
add('BC', B_HT, 1,
    "Theo VAS 24 – Báo cáo lưu chuyển tiền tệ, các luồng tiền trong kỳ được phân loại theo những hoạt động nào?",
    "Hoạt động kinh doanh, hoạt động đầu tư và hoạt động tài chính",
    ["Hoạt động sản xuất, hoạt động thương mại và hoạt động dịch vụ",
     "Hoạt động kinh doanh, hoạt động tài chính và hoạt động khác",
     "Hoạt động thường xuyên, hoạt động đầu tư và hoạt động bất thường"],
    "VAS 24 phân loại luồng tiền thành: hoạt động kinh doanh, hoạt động đầu tư, hoạt động tài chính.",
    "VAS 24 – Báo cáo lưu chuyển tiền tệ")

add('BC', B_HT, 2,
    "Theo VAS 24, giao dịch nào sau đây được phân loại vào luồng tiền từ hoạt động tài chính?",
    "Tiền chi trả nợ gốc vay ngân hàng",
    ["Tiền chi mua cổ phiếu của doanh nghiệp khác",
     "Tiền chi mua sắm máy móc, thiết bị sản xuất",
     "Tiền chi trả người cung cấp hàng hóa, dịch vụ"],
    "Trả nợ gốc vay thuộc hoạt động tài chính (thay đổi quy mô, kết cấu vốn chủ và vốn vay). Mua cổ phiếu doanh nghiệp khác, mua TSCĐ thuộc hoạt động đầu tư; trả người bán thuộc hoạt động kinh doanh.",
    "VAS 24 – phân loại luồng tiền hoạt động tài chính")

cfo = 150 + 40 - 30 - 25 + 20
assert cfo == 155
add('BC', B_HT, 3,
    "Năm N, công ty có (tỷ đồng): lợi nhuận sau thuế 150; khấu hao TSCĐ 40; phải thu khách hàng tăng 30; hàng tồn kho tăng 25; phải trả người bán tăng 20. Giả định không có khoản điều chỉnh nào khác (thuế TNDN phải nộp đã nộp đủ trong kỳ). Lưu chuyển tiền thuần từ hoạt động kinh doanh theo phương pháp gián tiếp là",
    f"{cfo} tỷ đồng", ["225 tỷ đồng", "115 tỷ đồng", "190 tỷ đồng"],
    "CFO = 150 + 40 − 30 (tăng phải thu) − 25 (tăng tồn kho) + 20 (tăng phải trả) = 155 tỷ đồng. Lỗi thường gặp: đảo dấu biến động vốn lưu động (225), bỏ khấu hao (115), bỏ biến động vốn lưu động (190).",
    "Phương pháp gián tiếp: CFO = LN + khấu hao − tăng TS ngắn hạn + tăng nợ phải trả ngắn hạn")

add('BC', B_HT, 2,
    "Khoản dự phòng giảm giá hàng tồn kho được trình bày trên báo cáo tình hình tài chính (bảng cân đối kế toán) như thế nào?",
    "Ghi số âm, điều chỉnh giảm hàng tồn kho trong tài sản ngắn hạn",
    ["Trình bày là một khoản nợ phải trả ngắn hạn",
     "Trình bày là một khoản mục thuộc vốn chủ sở hữu",
     "Trình bày là một khoản tài sản ngắn hạn khác"],
    "Dự phòng giảm giá hàng tồn kho là khoản điều chỉnh giảm giá trị tài sản, trình bày dưới dạng số âm ngay trong khoản mục hàng tồn kho để phản ánh giá trị thuần có thể thực hiện được.",
    "VAS 02 – Hàng tồn kho: giá trị thuần có thể thực hiện được và dự phòng")

add('BC', B_HT, 2,
    "Ngày 01/01/N, công ty nhận trước 360 triệu đồng tiền cho thuê văn phòng trong 3 năm (01/01/N – 31/12/N+2). Theo nguyên tắc cơ sở dồn tích, trên BCTC năm N công ty",
    "Ghi nhận doanh thu 120 triệu; 240 triệu còn lại là doanh thu chưa thực hiện (nợ phải trả)",
    ["Ghi nhận doanh thu 360 triệu vì đã thu đủ tiền trong năm N",
     "Ghi nhận doanh thu 120 triệu; 240 triệu còn lại ghi tăng vốn chủ sở hữu",
     "Ghi nhận doanh thu 120 triệu; 240 triệu còn lại ghi giảm phải thu khách hàng"],
    "Doanh thu được ghi nhận theo kỳ cung cấp dịch vụ: 360/3 = 120 triệu cho năm N; 240 triệu nhận trước cho 2 năm sau là doanh thu chưa thực hiện, một khoản nợ phải trả.",
    "VAS 01 – Chuẩn mực chung: nguyên tắc cơ sở dồn tích và phù hợp")

add('BC', B_HT, 1,
    "Trên báo cáo kết quả hoạt động kinh doanh, chỉ tiêu “Lợi nhuận gộp về bán hàng và cung cấp dịch vụ” được xác định bằng",
    "Doanh thu thuần trừ giá vốn hàng bán",
    ["Doanh thu thuần trừ giá vốn, chi phí bán hàng và chi phí quản lý",
     "Doanh thu chưa trừ các khoản giảm trừ, trừ giá vốn hàng bán",
     "Doanh thu thuần trừ giá vốn hàng bán và chi phí tài chính"],
    "Lợi nhuận gộp = doanh thu thuần về bán hàng và cung cấp dịch vụ − giá vốn hàng bán.",
    "Cấu trúc báo cáo kết quả hoạt động kinh doanh")

# =========================== BC: Chỉ tiêu tài chính ===========================
qr = (80 + 40 + 180) / 400
assert vn(qr) == "0,75"
add('BC', B_CT, 3,
    "Tại 31/12/N, công ty có (tỷ đồng): tiền và tương đương tiền 80; đầu tư tài chính ngắn hạn 40; phải thu ngắn hạn 180; hàng tồn kho 260; tài sản ngắn hạn khác 40; nợ ngắn hạn 400. Hệ số khả năng thanh toán nhanh (không tính hàng tồn kho và tài sản ngắn hạn khác) là",
    vn(qr) + " lần", [vn(600 / 400) + " lần", vn(340 / 400) + " lần", vn(120 / 400) + " lần"],
    "Thanh toán nhanh = (tiền 80 + đầu tư ngắn hạn 40 + phải thu 180)/nợ ngắn hạn 400 = 0,75 lần. 1,50 là thanh toán hiện hành; 0,85 là chỉ trừ hàng tồn kho; 0,30 là thanh toán tức thời.",
    "Hệ số thanh toán nhanh = (tiền + đầu tư TC ngắn hạn + phải thu ngắn hạn)/nợ ngắn hạn")

dio = 365 / (1460 / 200)
assert abs(dio - 50) < 1e-9
add('BC', B_CT, 3,
    "Năm N: giá vốn hàng bán 1.460 tỷ đồng; hàng tồn kho đầu năm 180 tỷ, cuối năm 220 tỷ; doanh thu thuần 2.000 tỷ. Tính theo hàng tồn kho bình quân, giá vốn hàng bán và năm 365 ngày, số ngày tồn kho bình quân là",
    vn(dio, 1) + " ngày", [vn(220 / 1460 * 365, 1) + " ngày", vn(200 / 2000 * 365, 1) + " ngày", vn(180 / 1460 * 365, 1) + " ngày"],
    "HTK bình quân = (180 + 220)/2 = 200; vòng quay = 1.460/200 = 7,3 vòng; số ngày tồn kho = 365/7,3 = 50,0 ngày. Lỗi thường gặp: dùng HTK cuối kỳ (55,0), dùng doanh thu (36,5), dùng HTK đầu kỳ (45,0).",
    "Số ngày tồn kho = 365/(giá vốn hàng bán/HTK bình quân)")

add('BC', B_CT, 1,
    "Chu kỳ chuyển đổi tiền mặt (cash conversion cycle) của doanh nghiệp được xác định bằng",
    "Số ngày tồn kho + kỳ thu tiền bình quân − kỳ trả tiền bình quân",
    ["Số ngày tồn kho + kỳ thu tiền bình quân + kỳ trả tiền bình quân",
     "Kỳ thu tiền bình quân − số ngày tồn kho − kỳ trả tiền bình quân",
     "Số ngày tồn kho + kỳ trả tiền bình quân − kỳ thu tiền bình quân"],
    "CCC = DIO + DSO − DPO: thời gian từ khi chi tiền mua hàng đến khi thu tiền bán hàng.",
    "Chu kỳ chuyển đổi tiền mặt = DIO + DSO − DPO")

em = 0.18 / (0.06 * 1.2)
da = 1 - 1 / em
assert abs(em - 2.5) < 1e-12 and pct(da, 1) == "60,0%"
add('BC', B_CT, 3,
    "Năm N, công ty có ROE 18%, tỷ suất lợi nhuận ròng trên doanh thu 6% và vòng quay tổng tài sản 1,2 lần (các chỉ tiêu tính trên số bình quân). Theo mô hình Dupont, tỷ lệ nợ phải trả trên tổng tài sản bình quân là",
    pct(da, 1), [pct(1 / em, 1), pct(em - 1, 1), pct(em, 1)],
    f"Hệ số nhân vốn chủ = ROE/(ROS × vòng quay TS) = 18%/(6% × 1,2) = {vn(em, 1)}; VCSH/TTS = 1/2,5 = 40% ⇒ nợ/TTS = 60,0%. Lỗi thường gặp: lấy VCSH/TTS (40%), nợ/VCSH (150%), hoặc chính hệ số nhân (250%).",
    "Dupont: ROE = ROS × vòng quay tổng tài sản × hệ số nhân vốn chủ")

roe5 = 0.8 * 0.75 * 0.15 * 1.2 * 2.0
assert pct(roe5, 1) == "21,6%"
add('BC', B_CT, 3,
    "Công ty có: LNST/LNTT = 0,80; LNTT/EBIT = 0,75; EBIT/doanh thu thuần = 15%; vòng quay tổng tài sản 1,2 lần; tổng tài sản bình quân/vốn chủ sở hữu bình quân = 2,0. ROE theo mô hình Dupont mở rộng (5 nhân tố) là",
    pct(roe5, 1), [pct(0.8 * 0.15 * 1.2 * 2, 1), pct(0.75 * 0.15 * 1.2 * 2, 1), pct(0.8 * 0.75 * 0.15 * 1.2, 1)],
    "ROE = 0,80 × 0,75 × 15% × 1,2 × 2,0 = 21,6%. Lỗi thường gặp: bỏ gánh nặng lãi vay (28,8%), bỏ gánh nặng thuế (27,0%), bỏ hệ số nhân vốn chủ (10,8% – đó là ROA).",
    "Dupont 5 nhân tố: ROE = (LNST/LNTT) × (LNTT/EBIT) × (EBIT/DT) × (DT/TTS) × (TTS/VCSH)")

icr = (180 + 60) / 60
assert icr == 4.0
add('BC', B_CT, 3,
    "Năm N, công ty có lợi nhuận trước thuế 180 tỷ đồng, chi phí lãi vay 60 tỷ đồng, khấu hao 60 tỷ đồng, thuế suất thuế TNDN 20%. Hệ số khả năng thanh toán lãi vay (EBIT/chi phí lãi vay) là",
    vn(icr, 1) + " lần", [vn(180 / 60, 1) + " lần", vn(300 / 60, 1) + " lần", vn(144 / 60, 1) + " lần"],
    "EBIT = LNTT + lãi vay = 180 + 60 = 240; hệ số = 240/60 = 4,0 lần. Lỗi thường gặp: dùng LNTT (3,0), dùng EBITDA (5,0), dùng LNST (2,4).",
    "Khả năng thanh toán lãi vay = EBIT/chi phí lãi vay")

add('BC', B_CT, 2,
    "Doanh nghiệp có tỷ suất sinh lời trên tổng tài sản (trước lãi vay) cao hơn lãi suất vay. Khi doanh nghiệp tăng tỷ trọng nợ vay trong cơ cấu vốn, các yếu tố khác không đổi, thì",
    "ROE có xu hướng tăng nhưng rủi ro tài chính của doanh nghiệp cũng tăng",
    ["ROE có xu hướng giảm vì chi phí lãi vay của doanh nghiệp tăng lên",
     "ROE có xu hướng tăng và rủi ro tài chính của doanh nghiệp giảm đi",
     "ROE không thay đổi vì tỷ suất sinh lời trên tổng tài sản không đổi"],
    "Khi khả năng sinh lời của tài sản lớn hơn chi phí nợ, đòn bẩy tài chính khuếch đại ROE (đòn bẩy dương), nhưng nghĩa vụ trả lãi cố định tăng làm rủi ro tài chính tăng.",
    "Đòn bẩy tài chính và tác động đến ROE")

add('BC', B_CT, 1,
    "Hệ số khả năng thanh toán tức thời (thanh toán bằng tiền) được tính bằng",
    "Tiền và các khoản tương đương tiền/nợ ngắn hạn",
    ["(Tài sản ngắn hạn − hàng tồn kho)/nợ ngắn hạn",
     "Tài sản ngắn hạn/nợ ngắn hạn",
     "Tiền và các khoản tương đương tiền/tổng nợ phải trả"],
    "Thanh toán tức thời = (tiền + tương đương tiền)/nợ ngắn hạn; (TSNH − HTK)/nợ ngắn hạn là thanh toán nhanh; TSNH/nợ ngắn hạn là thanh toán hiện hành.",
    "Nhóm chỉ tiêu khả năng thanh toán")

add('BC', B_CT, 2,
    "Trong 2 năm, doanh thu của doanh nghiệp đi ngang nhưng số ngày tồn kho bình quân tăng từ 45 ngày lên 90 ngày. Dấu hiệu này phù hợp nhất với nhận định nào?",
    "Hàng tồn kho có thể bị ứ đọng, làm tăng nhu cầu vốn lưu động và rủi ro giảm giá",
    ["Hiệu quả quản lý hàng tồn kho của doanh nghiệp được cải thiện rõ rệt",
     "Khả năng thanh toán nhanh của doanh nghiệp chắc chắn được cải thiện",
     "Chu kỳ chuyển đổi tiền mặt của doanh nghiệp đang được rút ngắn lại"],
    "Số ngày tồn kho tăng gấp đôi khi doanh thu không đổi nghĩa là vòng quay HTK giảm một nửa: vốn bị chôn trong HTK, chu kỳ tiền mặt dài ra, rủi ro lỗi thời, giảm giá tăng.",
    "Nhóm chỉ tiêu hiệu quả hoạt động: vòng quay hàng tồn kho")

bvps = 1200e9 / 60e6
pb = 30000 / bvps
assert bvps == 20000 and vn(pb) == "1,50"
add('BC', B_CT, 3,
    "Tại 31/12/N, vốn chủ sở hữu của công ty là 1.200 tỷ đồng; công ty đã phát hành 65 triệu cổ phiếu phổ thông, trong đó có 5 triệu cổ phiếu quỹ; không có cổ phiếu ưu đãi. Giá thị trường là 30.000 đồng/cp. Hệ số P/B là",
    vn(pb) + " lần", [vn(30000 / (1200e9 / 65e6)) + " lần", vn(1 / pb) + " lần", vn(30000 / (1200e9 / 70e6)) + " lần"],
    f"Cổ phiếu lưu hành = 65 − 5 = 60 triệu; giá trị sổ sách/cp = 1.200 tỷ/60 triệu = 20.000 đồng; P/B = 30.000/20.000 = 1,50 lần. Lỗi thường gặp: tính cả cổ phiếu quỹ ({vn(30000 / (1200e9 / 65e6))}), đảo tỷ số (0,67), cộng thêm cổ phiếu quỹ (1,75).",
    "P/B = giá thị trường/giá trị sổ sách mỗi cổ phiếu đang lưu hành")

add('BC', B_CT, 1,
    "Chỉ tiêu nào sau đây thuộc nhóm chỉ tiêu cơ cấu vốn (đòn bẩy tài chính)?",
    "Hệ số nợ phải trả trên vốn chủ sở hữu",
    ["Vòng quay khoản phải thu khách hàng", "Tỷ suất lợi nhuận gộp trên doanh thu", "Hệ số khả năng thanh toán nhanh"],
    "Nhóm cơ cấu vốn gồm nợ/VCSH, nợ/tổng tài sản, hệ số nhân vốn chủ…; các chỉ tiêu còn lại thuộc nhóm hiệu quả hoạt động, sinh lời và thanh toán.",
    "Nhóm chỉ tiêu cơ cấu vốn và đòn bẩy tài chính")

assert abs(0.10 * 1.0 * 2.0 - 0.2) < 1e-12 and abs(0.04 * 1.25 * 4.0 - 0.2) < 1e-12
add('BC', B_CT, 2,
    "Hai công ty S và T cùng có ROE 20%. Phân tích Dupont: S có tỷ suất lợi nhuận ròng 10%, vòng quay tổng tài sản 1,0 lần, hệ số nhân vốn chủ 2,0; T có tỷ suất lợi nhuận ròng 4%, vòng quay tổng tài sản 1,25 lần, hệ số nhân vốn chủ 4,0. Nhận định nào đúng?",
    "ROE của T dựa nhiều hơn vào đòn bẩy nên rủi ro tài chính của T cao hơn S",
    ["S sử dụng tài sản hiệu quả hơn T vì vòng quay tổng tài sản cao hơn",
     "Rủi ro tài chính của S và T như nhau vì hai công ty có cùng ROE",
     "T có tỷ suất sinh lời trên tổng tài sản (ROA) cao hơn công ty S"],
    "ROA S = 10% × 1,0 = 10%; ROA T = 4% × 1,25 = 5%. T đạt cùng ROE 20% nhờ hệ số nhân vốn chủ 4,0 (nợ/TTS 75%) so với 2,0 của S (50%) nên rủi ro tài chính cao hơn; vòng quay TS của T (1,25) cao hơn S.",
    "Dupont: ROE = ROS × vòng quay tổng tài sản × hệ số nhân vốn chủ")

add('BC', B_CT, 2,
    "Vòng quay tổng tài sản của doanh nghiệp giảm từ 1,5 lần xuống 1,1 lần trong khi doanh thu thuần không đổi. Điều này cho thấy",
    "Tổng tài sản bình quân tăng, hiệu quả sử dụng tài sản để tạo doanh thu giảm",
    ["Tổng tài sản bình quân giảm, hiệu quả sử dụng tài sản để tạo doanh thu tăng",
     "Tỷ suất lợi nhuận ròng trên doanh thu của doanh nghiệp chắc chắn giảm",
     "Khả năng thanh toán ngắn hạn của doanh nghiệp chắc chắn được cải thiện"],
    "Vòng quay TS = doanh thu/TTS bình quân; doanh thu không đổi mà vòng quay giảm ⇒ TTS bình quân tăng (khoảng 36%), mỗi đồng tài sản tạo ra ít doanh thu hơn.",
    "Vòng quay tổng tài sản = doanh thu thuần/tổng tài sản bình quân")

cr_new = (400 - 50) / (200 - 50)
assert vn(cr_new) == "2,33"
add('BC', B_CT, 3,
    "Công ty có tài sản ngắn hạn 400 tỷ đồng và nợ ngắn hạn 200 tỷ đồng. Công ty dùng 50 tỷ đồng tiền mặt để trả nợ người bán. Sau giao dịch, hệ số khả năng thanh toán hiện hành",
    f"Tăng lên {vn(cr_new)} lần", [f"Giảm xuống {vn(350 / 200)} lần", "Không đổi ở mức 2,00 lần", f"Tăng lên {vn(400 / 150)} lần"],
    "Trước: 400/200 = 2,00. Sau: (400 − 50)/(200 − 50) = 350/150 = 2,33 lần. Khi hệ số > 1, giảm cùng một lượng ở tử và mẫu làm hệ số tăng. Lỗi thường gặp: chỉ giảm tử (1,75) hoặc chỉ giảm mẫu (2,67).",
    "Hệ số thanh toán hiện hành = TSNH/nợ ngắn hạn")

# =========================== BC: Dự báo ===========================
re1 = 1000 * 1.2 * 0.10 * (1 - 0.4)
assert abs(re1 - 72) < 1e-9
add('BC', B_DB, 3,
    "Doanh thu năm N là 1.000 tỷ đồng, dự báo tăng 20% trong năm N+1. Tỷ suất lợi nhuận ròng trên doanh thu dự kiến 10%, tỷ lệ chi trả cổ tức 40%. Lợi nhuận giữ lại bổ sung vốn chủ sở hữu năm N+1 là",
    f"{re1:.0f} tỷ đồng", ["48 tỷ đồng", "60 tỷ đồng", "120 tỷ đồng"],
    "Doanh thu N+1 = 1.000 × 1,2 = 1.200; LNST = 1.200 × 10% = 120; LN giữ lại = 120 × (1 − 40%) = 72 tỷ đồng. Lỗi thường gặp: nhân với tỷ lệ chi trả (48), dùng doanh thu năm N (60), lấy toàn bộ LNST (120).",
    "Dự báo: LN giữ lại = DT dự báo × biên LN ròng × (1 − tỷ lệ chi trả cổ tức)")

afn = 0.8 * 200 - 0.2 * 200 - 1200 * 0.1 * 0.6
assert abs(afn - 48) < 1e-9
add('BC', B_DB, 3,
    "Doanh thu năm N là 1.000 tỷ đồng, dự báo năm N+1 là 1.200 tỷ đồng. Doanh nghiệp hoạt động hết công suất; tài sản tăng theo doanh thu với tỷ lệ tài sản/doanh thu 0,8; nợ phải trả phát sinh tự động (phải trả người bán, chi phí phải trả) bằng 20% doanh thu. Tỷ suất lợi nhuận ròng 10%, tỷ lệ chi trả cổ tức 40%. Nhu cầu vốn bổ sung từ bên ngoài (AFN) năm N+1 là",
    f"{afn:.0f} tỷ đồng", ["120 tỷ đồng", "88 tỷ đồng", "60 tỷ đồng"],
    "Tài sản tăng = 0,8 × 200 = 160; nợ tự phát tăng = 0,2 × 200 = 40; LN giữ lại = 1.200 × 10% × 60% = 72. AFN = 160 − 40 − 72 = 48 tỷ đồng. Lỗi thường gặp: bỏ LN giữ lại (120), bỏ nợ tự phát (88), tính LN giữ lại theo doanh thu năm N (60).",
    "Phương pháp tỷ lệ % trên doanh thu: AFN = ΔTS − ΔNợ tự phát − LN giữ lại")

add('BC', B_DB, 2,
    "Khi dự báo BCTC theo phương pháp tỷ lệ phần trăm trên doanh thu, khoản mục nào thường KHÔNG được giả định biến động tự động theo doanh thu mà phụ thuộc quyết định tài trợ?",
    "Vay ngân hàng và vốn góp của chủ sở hữu",
    ["Phải trả người bán", "Hàng tồn kho", "Phải thu khách hàng"],
    "Phải thu, tồn kho, phải trả người bán biến động gần tỷ lệ với doanh thu; vay ngân hàng, phát hành cổ phiếu là nguồn tài trợ chủ động, dùng để cân đối nhu cầu vốn bổ sung.",
    "Phương pháp tỷ lệ % trên doanh thu: khoản mục biến đổi và nguồn tài trợ chủ động")

add('BC', B_DB, 1,
    "Trong quy trình dự báo báo cáo tài chính doanh nghiệp, chỉ tiêu nào thường được dự báo đầu tiên và làm cơ sở cho các khoản mục khác?",
    "Doanh thu thuần",
    ["Lợi nhuận sau thuế", "Tổng tài sản", "Cổ tức chi trả"],
    "Dự báo doanh thu là bước đầu tiên; chi phí, tài sản, nợ và lợi nhuận được dự báo dựa trên doanh thu.",
    "Quy trình dự báo BCTC: bắt đầu từ dự báo doanh thu")

ni = (2400 * 0.25 - 2400 * 0.12 - 60) * 0.8
assert abs(ni - 201.6) < 1e-9
add('BC', B_DB, 3,
    "Năm N+1, công ty dự báo: doanh thu thuần 2.400 tỷ đồng; tỷ suất lợi nhuận gộp 25%; chi phí bán hàng và quản lý doanh nghiệp bằng 12% doanh thu; chi phí lãi vay 60 tỷ đồng; không có doanh thu, chi phí khác; thuế suất thuế TNDN 20%. Lợi nhuận sau thuế dự báo là",
    vn(ni, 1) + " tỷ đồng", [vn(312 * 0.8, 1) + " tỷ đồng", vn(252, 1) + " tỷ đồng", vn(312 * 0.8 - 60, 1) + " tỷ đồng"],
    "LN gộp = 2.400 × 25% = 600; chi phí BH và QLDN = 288; EBIT = 312; LNTT = 312 − 60 = 252; LNST = 252 × 0,8 = 201,6 tỷ đồng. Lỗi thường gặp: bỏ lãi vay (249,6), quên thuế (252,0), trừ lãi vay sau thuế (189,6).",
    "Dự báo báo cáo KQKD theo tỷ lệ % doanh thu")

# =========================== BC: Chất lượng BCTC ===========================
add('BC', B_CL, 2,
    "Dấu hiệu nào sau đây cho thấy chất lượng lợi nhuận của doanh nghiệp có thể thấp?",
    "Lợi nhuận tăng đều nhiều năm nhưng lưu chuyển tiền thuần HĐKD liên tục âm",
    ["Lưu chuyển tiền thuần HĐKD ổn định và xấp xỉ lợi nhuận sau thuế",
     "Doanh thu và phải thu khách hàng tăng cùng tốc độ trong nhiều năm",
     "Lợi nhuận chủ yếu đến từ hoạt động kinh doanh cốt lõi, có tính lặp lại"],
    "Lợi nhuận không chuyển hóa thành tiền (CFO âm kéo dài) cho thấy lợi nhuận dựa nhiều vào các khoản dồn tích như phải thu, tồn kho – dấu hiệu có thể ghi nhận doanh thu sớm hoặc chất lượng lợi nhuận thấp.",
    "Chất lượng lợi nhuận: so sánh lợi nhuận với lưu chuyển tiền thuần HĐKD")

acc = (200 - 80) / 1000
assert pct(acc, 1) == "12,0%"
add('BC', B_CL, 3,
    "Năm N, công ty có lợi nhuận sau thuế 200 tỷ đồng, lưu chuyển tiền thuần từ hoạt động kinh doanh 80 tỷ đồng, tổng tài sản bình quân 1.000 tỷ đồng. Tỷ lệ dồn tích tính theo công thức (LNST − lưu chuyển tiền thuần HĐKD)/tổng tài sản bình quân là",
    pct(acc, 1), [pct(80 / 1000, 1), pct(200 / 1000, 1), pct(280 / 1000, 1)],
    "Tỷ lệ dồn tích = (200 − 80)/1.000 = 12,0%. CFO/LNST chỉ 0,4 – phần lớn lợi nhuận là dồn tích, cảnh báo chất lượng lợi nhuận thấp. Lỗi thường gặp: lấy CFO/TTS (8,0%), ROA (20,0%), cộng thay vì trừ (28,0%).",
    "Tỷ lệ dồn tích = (LNST − CFO)/tổng tài sản bình quân")

add('BC', B_CL, 2,
    "Doanh nghiệp thay đổi ước tính kế toán, kéo dài thời gian khấu hao TSCĐ vượt quá thời gian sử dụng hữu ích thực tế. Trong năm thay đổi, tác động trực tiếp là",
    "Chi phí khấu hao giảm làm lợi nhuận kế toán tăng, dòng tiền thực không được cải thiện",
    ["Chi phí khấu hao tăng làm lợi nhuận kế toán giảm tương ứng trong năm",
     "Lưu chuyển tiền thuần HĐKD tăng đúng bằng mức giảm chi phí khấu hao",
     "Giá trị còn lại của TSCĐ trên báo cáo tình hình tài chính giảm nhanh hơn"],
    "Khấu hao là chi phí không bằng tiền: kéo dài thời gian khấu hao làm khấu hao mỗi năm giảm, lợi nhuận tăng nhưng không tạo thêm tiền; giá trị còn lại của TSCĐ giảm chậm hơn. Đây là dấu hiệu điều chỉnh lợi nhuận.",
    "VAS 03, VAS 29: thay đổi ước tính kế toán; chất lượng lợi nhuận")

add('BC', B_CL, 1,
    "Ý kiến kiểm toán nào thể hiện BCTC đã phản ánh trung thực và hợp lý, trên các khía cạnh trọng yếu, tình hình tài chính của doanh nghiệp mà không có ngoại trừ?",
    "Ý kiến chấp nhận toàn phần",
    ["Ý kiến kiểm toán ngoại trừ", "Ý kiến kiểm toán trái ngược", "Từ chối đưa ra ý kiến kiểm toán"],
    "Ý kiến chấp nhận toàn phần: BCTC trung thực, hợp lý trên các khía cạnh trọng yếu. Ý kiến ngoại trừ, trái ngược và từ chối đưa ra ý kiến là các dạng ý kiến không phải chấp nhận toàn phần.",
    "VSA 700, VSA 705 – Ý kiến kiểm toán trên BCTC")

add('BC', B_CL, 2,
    "Trong năm N, doanh nghiệp vốn hóa 50 tỷ đồng chi phí lẽ ra phải ghi nhận vào chi phí trong kỳ (chưa phân bổ trong năm N; bỏ qua ảnh hưởng thuế). So với cách ghi nhận đúng, BCTC năm N sẽ có",
    "Lợi nhuận cao hơn 50 tỷ; tiền thuần HĐKD cao hơn và HĐ đầu tư thấp hơn 50 tỷ",
    ["Lợi nhuận cao hơn 50 tỷ; tiền thuần theo từng hoạt động không thay đổi",
     "Lợi nhuận không đổi; tiền thuần HĐKD cao hơn 50 tỷ so với cách ghi đúng",
     "Lợi nhuận cao hơn 50 tỷ; tiền thuần HĐKD thấp hơn 50 tỷ so với cách ghi đúng"],
    "Vốn hóa sai làm chi phí kỳ giảm 50 tỷ ⇒ lợi nhuận tăng 50 tỷ; khoản chi tiền bị chuyển từ luồng HĐKD sang luồng đầu tư (mua tài sản) ⇒ CFO cao hơn 50 tỷ, CFI thấp hơn 50 tỷ; tổng lưu chuyển tiền không đổi.",
    "Chất lượng BCTC: tác động của vốn hóa chi phí đến lợi nhuận và dòng tiền")

# =========================== BC: Nghiên cứu tình huống ===========================
ebt = 2000 - 1500 - 200 - 50
nim = ebt * 0.8
avgE, avgA = (900 + 1100) / 2, (1800 + 2200) / 2
assert nim == 200 and pct(nim / avgE) == "20,00%"
case_M = "Tình huống Công ty M (tỷ đồng): năm N doanh thu thuần 2.000; giá vốn hàng bán 1.500; chi phí bán hàng và quản lý 200; chi phí lãi vay 50; không có thu nhập, chi phí khác; thuế suất thuế TNDN 20%. Tổng tài sản đầu năm 1.800, cuối năm 2.200; vốn chủ sở hữu đầu năm 900, cuối năm 1.100."
add('BC', B_TH, 3,
    case_M + " ROE tính trên vốn chủ sở hữu bình quân là",
    pct(nim / avgE), [pct(nim / 1100), pct(nim / 900), pct(ebt / avgE)],
    "LNTT = 2.000 − 1.500 − 200 − 50 = 250; LNST = 250 × 0,8 = 200; VCSH bình quân = (900 + 1.100)/2 = 1.000; ROE = 200/1.000 = 20,00%. Lỗi thường gặp: dùng VCSH cuối kỳ (18,18%), đầu kỳ (22,22%), dùng LNTT (25,00%).",
    "ROE = LNST/VCSH bình quân")

at, emm = 2000 / avgA, avgA / avgE
assert at == 1.0 and emm == 2.0
add('BC', B_TH, 3,
    case_M + " Vòng quay tổng tài sản và hệ số nhân vốn chủ sở hữu (tính trên số bình quân) lần lượt là",
    f"{vn(at)} lần và {vn(emm)} lần",
    [f"{vn(2000 / 2200)} lần và {vn(2200 / 1100)} lần", f"{vn(2000 / 1800)} lần và {vn(1800 / 900)} lần", f"{vn(at)} lần và {vn((avgA - avgE) / avgE)} lần"],
    "TTS bình quân = (1.800 + 2.200)/2 = 2.000; VCSH bình quân = 1.000. Vòng quay TS = 2.000/2.000 = 1,00; hệ số nhân vốn chủ = 2.000/1.000 = 2,00. Lỗi thường gặp: dùng số cuối kỳ (0,91) hoặc đầu kỳ (1,11), nhầm hệ số nhân với nợ/VCSH (1,00).",
    "Dupont: vòng quay TS = DT/TTS bình quân; hệ số nhân vốn chủ = TTS bình quân/VCSH bình quân")

assert abs(0.075 * 1 * 2 - 0.15) < 1e-12 and abs(0.05 * 1 * 4 - 0.20) < 1e-12
add('BC', B_TH, 2,
    "Tình huống: ROE của Công ty K tăng từ 15% (năm N−1) lên 20% (năm N). Phân tích Dupont cho thấy tỷ suất lợi nhuận ròng giảm từ 7,5% xuống 5%, vòng quay tổng tài sản không đổi ở mức 1,0 lần, hệ số nhân vốn chủ sở hữu tăng từ 2,0 lên 4,0. Nhận định nào phù hợp nhất?",
    "ROE tăng chủ yếu nhờ tăng đòn bẩy tài chính, chất lượng tăng trưởng ROE kém bền vững",
    ["ROE tăng chủ yếu nhờ cải thiện hiệu quả hoạt động và biên lợi nhuận ròng",
     "ROE tăng chủ yếu nhờ hiệu quả sử dụng tài sản được cải thiện mạnh",
     "Rủi ro tài chính của K giảm đi do ROE tăng từ 15% lên 20%"],
    "15% = 7,5% × 1,0 × 2,0; 20% = 5% × 1,0 × 4,0. Biên lợi nhuận giảm, vòng quay không đổi; ROE tăng hoàn toàn do hệ số nhân vốn chủ tăng gấp đôi (nợ/TTS từ 50% lên 75%), nên rủi ro tài chính tăng và mức ROE kém bền vững.",
    "Phân tích Dupont theo thời gian")

fcf = 300 - (180 - 20)
assert fcf == 140
add('BC', B_TH, 3,
    "Tình huống Công ty P năm N (tỷ đồng): lưu chuyển tiền thuần từ HĐKD 300; tiền chi mua sắm TSCĐ 180; tiền thu từ thanh lý TSCĐ 20; cổ tức đã trả 60; tiền vay mới nhận được 100. Dòng tiền tự do được xác định bằng lưu chuyển tiền thuần HĐKD trừ chi đầu tư TSCĐ thuần (sau khi trừ tiền thu thanh lý). Dòng tiền tự do năm N là",
    f"{fcf} tỷ đồng", ["120 tỷ đồng", "80 tỷ đồng", "240 tỷ đồng"],
    "Chi đầu tư TSCĐ thuần = 180 − 20 = 160; dòng tiền tự do = 300 − 160 = 140 tỷ đồng. Cổ tức và vay mới là luồng tài chính, không tham gia công thức. Lỗi thường gặp: bỏ tiền thu thanh lý (120), trừ cổ tức (80), cộng vay mới (240).",
    "Dòng tiền tự do = CFO − chi đầu tư TSCĐ thuần")

ccc0, ccc1 = 40 + 70 - 50, 55 + 90 - 45
assert ccc1 - ccc0 == 40
add('BC', B_TH, 3,
    "Tình huống Công ty Q: năm N−1 kỳ thu tiền bình quân 40 ngày, số ngày tồn kho bình quân 70 ngày, kỳ trả tiền bình quân 50 ngày; năm N lần lượt là 55 ngày, 90 ngày và 45 ngày. Chu kỳ chuyển đổi tiền mặt của Q thay đổi như thế nào?",
    f"Tăng {ccc1 - ccc0} ngày", ["Tăng 30 ngày", "Tăng 35 ngày", "Giảm 40 ngày"],
    "CCC N−1 = 40 + 70 − 50 = 60 ngày; CCC N = 55 + 90 − 45 = 100 ngày ⇒ tăng 40 ngày, nhu cầu vốn lưu động tăng. Lỗi thường gặp: cộng kỳ trả tiền (tăng 30), bỏ kỳ trả tiền (tăng 35), nhầm dấu (giảm 40).",
    "Chu kỳ chuyển đổi tiền mặt = DSO + DIO − DPO")

add('BC', B_TH, 2,
    "Tình huống: Công ty R có hệ số thanh toán hiện hành 2,5 lần nhưng hệ số thanh toán nhanh chỉ 0,4 lần, trong khi hệ số thanh toán nhanh bình quân ngành là 1,0 lần. Nhận định nào hợp lý nhất?",
    "Tài sản ngắn hạn của R tập trung lớn vào hàng tồn kho; thanh khoản yếu nếu tồn kho khó bán",
    ["R có lượng tiền mặt dồi dào nên khả năng thanh toán tức thời rất tốt",
     "R đang dùng quá ít nợ ngắn hạn nên cần tăng vay ngắn hạn để tối ưu vốn",
     "Phải thu khách hàng chiếm tỷ trọng lớn nhất trong tài sản ngắn hạn của R"],
    "Chênh lệch lớn giữa thanh toán hiện hành (2,5) và thanh toán nhanh (0,4) nghĩa là khoảng 84% TSNH là hàng tồn kho (và TSNH khác); tiền và phải thu chỉ bằng 0,4 lần nợ ngắn hạn, thấp hơn ngành.",
    "Phân tích khả năng thanh toán: hệ số hiện hành và hệ số nhanh")

# =========================== Gán id, vị trí đáp án ===========================
assert len(Q) == 90, len(Q)
pos = ([0, 1, 2, 3] * 23)[:90]
random.Random(20261104).shuffle(pos)
out = []
for i, (x, a) in enumerate(zip(Q, pos), 1):
    o = list(x['wrong'])
    o.insert(a, x['correct'])
    assert len(set(o)) == 4, (i, o)
    out.append(dict(id=f"C2-{i:03d}", part="CM", subject=x['subject'], topic=x['topic'], level=x['level'],
                    q=x['q'], o=o, a=a, e=x['e'], basis=x['basis'], quote="", src=SRC, as_of="2026-11"))
with open(OUT, 'w', encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False, indent=1)
print("wrote", len(out))
