"""Build cm_3.json (95 câu chuyên môn BL/QU/PS). Run: python3 -I build.py
Mọi số liệu tính toán được tính lại ở đây; chk() đối chiếu với kết quả tính tay."""
import json, math, random

OUT = '/home/user/cchn_moi/web/data/src/cm_3.json'
GT = 'Giáo trình SRTC (khung chương trình)'
LAW = 'VBHN_24_VBHN-VPQH_2025_Luat_Chung_khoan_hop_nhat_Cong_bao.txt'
TT98 = 'VBHN_04_VBHN-BTC_2026_TT98_136_hop_nhat.txt'
ND158 = 'ND_158_2020_ND-CP_Cong_bao.txt'
LAWB = 'Luật Chứng khoán 2019 (VBHN 24/VBHN-VPQH năm 2025, hợp nhất Luật 56/2024/QH15)'


def vn(x, d=0):
    s = f"{x:,.{d}f}"
    s = s.replace(',', '#').replace('.', ',').replace('#', '.')
    return s.replace('-', '−') if s.startswith('-') else s


def pc(x, d=1):
    return vn(x * 100, d) + '%'


def chk(v, hand, tol=1e-3):
    """Đối chiếu kết quả Python với kết quả tính tay (sai số tương đối)."""
    assert abs(v - hand) <= tol * max(1, abs(hand)), (v, hand)


def npv(r, cfs):
    return sum(cf / (1 + r) ** t for t, cf in enumerate(cfs))


def irr(cfs, lo=-0.9, hi=1.0):
    for _ in range(200):
        mid = (lo + hi) / 2
        if npv(mid, cfs) > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


Q = []


def add(sub, topic, lv, q, o, e, basis, quote='', src=GT, num=None):
    """o[0] là đáp án đúng. num: giá trị số tương ứng o (để sắp xếp tăng dần)."""
    assert len(o) == 4 and len(set(o)) == 4, o
    Q.append(dict(sub=sub, topic=topic, lv=lv, q=q, o=o, e=e, basis=basis,
                  quote=quote, src=src, num=num))


def addn(sub, topic, lv, q, vals, fmt, e, basis):
    add(sub, topic, lv, q, [fmt(v) for v in vals], e, basis, num=list(vals))


# ============================== BL ==============================
T = 'Tổng quan về tư vấn tài chính doanh nghiệp'
add('BL', T, 1,
    'Theo quan điểm tài chính doanh nghiệp hiện đại, mục tiêu cơ bản mà nhà tư vấn tài chính hướng tới khi tư vấn cho một công ty cổ phần là gì?',
    ['Tối đa hóa giá trị tài sản của cổ đông, thể hiện qua giá trị thị trường của cổ phiếu',
     'Tối đa hóa lợi nhuận kế toán sau thuế của năm tài chính hiện hành',
     'Tối đa hóa doanh thu và thị phần của doanh nghiệp trong ngành',
     'Tối thiểu hóa số thuế thu nhập doanh nghiệp phải nộp hằng năm'],
    'Mục tiêu của tài chính doanh nghiệp là tối đa hóa giá trị cho chủ sở hữu (giá cổ phiếu), có tính đến quy mô, thời điểm và rủi ro của dòng tiền. Lợi nhuận kế toán, doanh thu hay tiết kiệm thuế chỉ là mục tiêu trung gian và có thể mâu thuẫn với giá trị dài hạn.',
    'Mục tiêu tối đa hóa giá trị doanh nghiệp/giá trị tài sản của cổ đông')
add('BL', T, 2,
    'Khoản chi nào sau đây là ví dụ điển hình của chi phí đại diện (agency cost) phát sinh từ mâu thuẫn lợi ích giữa cổ đông và ban điều hành?',
    ['Chi phí kiểm toán độc lập và chương trình thưởng cổ phiếu nhằm giám sát, ràng buộc ban điều hành',
     'Chi phí lãi vay doanh nghiệp trả cho ngân hàng theo hợp đồng tín dụng',
     'Chi phí khấu hao máy móc, thiết bị phục vụ hoạt động sản xuất kinh doanh',
     'Thuế thu nhập doanh nghiệp nộp ngân sách nhà nước theo quy định'],
    'Chi phí đại diện gồm chi phí giám sát, chi phí ràng buộc và tổn thất còn lại khi người quản lý (người đại diện) không hành động hoàn toàn vì lợi ích cổ đông (người chủ). Lãi vay, khấu hao, thuế là các chi phí hoạt động/tài chính thông thường.',
    'Lý thuyết đại diện (agency theory) – quan hệ giữa cổ đông và người quản lý')
add('BL', T, 2,
    'Dịch vụ nào sau đây KHÔNG thuộc phạm vi tư vấn tài chính doanh nghiệp mà công ty chứng khoán cung cấp cho khách hàng?',
    ['Kiểm toán và phát hành ý kiến kiểm toán về báo cáo tài chính năm của khách hàng',
     'Tư vấn tái cấu trúc tài chính, cơ cấu vốn và phương án huy động vốn',
     'Tư vấn lập hồ sơ chào bán, niêm yết chứng khoán của doanh nghiệp',
     'Tư vấn định giá doanh nghiệp trong giao dịch mua bán, sáp nhập'],
    'Tư vấn tài chính doanh nghiệp gồm tư vấn cơ cấu vốn, huy động vốn, chào bán/niêm yết, M&A, định giá, cổ phần hóa… Kiểm toán báo cáo tài chính là dịch vụ đảm bảo do doanh nghiệp kiểm toán độc lập thực hiện, không phải nghiệp vụ của CTCK; việc kiểm toán chính khách hàng mình tư vấn còn vi phạm tính độc lập.',
    'Phạm vi nghiệp vụ tư vấn tài chính doanh nghiệp của công ty chứng khoán')

T = 'Lập dự toán ngân sách vốn đầu tư'
cf = [-10, 3, 4, 5, 3]
n12, n10 = npv(0.12, cf), npv(0.10, cf)
nsh = -10 + sum(c / 1.12 ** (t - 1) for t, c in enumerate(cf) if t)  # lỗi chiết khấu lệch một kỳ
nund = sum(cf)
chk(n12, 1.3328)
pv = [c / 1.12 ** t for t, c in enumerate(cf) if t]
addn('BL', T, 3,
     'Dự án cần vốn đầu tư ban đầu 10 tỷ đồng (năm 0), tạo dòng tiền ròng cuối các năm 1, 2, 3, 4 lần lượt là 3; 4; 5 và 3 tỷ đồng. Chi phí vốn của dự án là 12%/năm. NPV của dự án xấp xỉ bằng bao nhiêu?',
     [n12, n10, nsh, nund], lambda v: vn(v, 2) + ' tỷ đồng',
     f'NPV = 3/1,12 + 4/1,12² + 5/1,12³ + 3/1,12⁴ − 10 = {vn(pv[0],4)} + {vn(pv[1],4)} + {vn(pv[2],4)} + {vn(pv[3],4)} − 10 ≈ {vn(n12,2)} tỷ đồng. Không chiết khấu cho {vn(nund,2)}; chiết khấu 10% cho {vn(n10,2)}; chiết khấu lệch một kỳ cho {vn(nsh,2)}.',
     'NPV = Σ CFt/(1+r)^t − I0')

cf = [-1000, 400, 500, 300]
r_ok, r_rev = irr(cf), irr([-1000, 300, 500, 400])
arr = (sum(cf) / 3) / 1000
tot = sum(cf) / 1000
chk(r_ok, 0.1013, 2e-2); chk(npv(r_ok, cf), 0, 1e-6); chk(r_rev, 0.0926, 2e-2)
addn('BL', T, 3,
     'Dự án đầu tư 1.000 triệu đồng tại năm 0, dòng tiền ròng cuối năm 1, 2, 3 lần lượt là 400; 500; 300 triệu đồng. Tỷ suất hoàn vốn nội bộ (IRR) của dự án gần nhất với giá trị nào?',
     [r_ok, r_rev, arr, tot], lambda v: pc(v, 1),
     f'IRR là r thỏa 400/(1+r) + 500/(1+r)² + 300/(1+r)³ = 1.000. Tại r = 10%: PV = {vn(npv(0.10, cf)+1000,2)} > 1.000 (NPV = {vn(npv(0.10, cf),2)}); nội suy/giải lặp được IRR ≈ {pc(r_ok,2)}. Đảo thứ tự dòng tiền (300; 500; 400) cho {pc(r_rev,1)}; lợi nhuận bình quân/vốn đầu tư cho {pc(arr,1)}; tổng lợi suất không chiết khấu là {pc(tot,1)}.',
     'IRR: tỷ suất chiết khấu làm NPV = 0')

af = (1 - 1.14 ** -4) / 0.14
pvi = 300 * af
pi = pvi / 800
chk(pi, 1.0926)
addn('BL', T, 3,
     'Dự án cần vốn đầu tư ban đầu 800 triệu đồng, tạo dòng tiền ròng 300 triệu đồng cuối mỗi năm trong 4 năm. Chi phí vốn 14%/năm. Chỉ số sinh lời (PI) của dự án là bao nhiêu?',
     [pi, (pvi - 800) / 800, 800 / pvi, 1200 / 800], lambda v: vn(v, 2),
     f'PV dòng tiền = 300 × [1 − 1,14⁻⁴]/0,14 = 300 × {vn(af,4)} = {vn(pvi,2)} triệu đồng; PI = PV/I0 = {vn(pvi,2)}/800 ≈ {vn(pi,2)} > 1 nên dự án đáng giá. NPV/I0 = {vn((pvi-800)/800,2)}; I0/PV = {vn(800/pvi,2)}; không chiết khấu cho 1.200/800 = 1,50.',
     'PI = PV dòng tiền vào / Vốn đầu tư ban đầu')

pvs = [350 / 1.1 ** t for t in range(1, 5)]
cum = [sum(pvs[:k]) for k in range(1, 5)]
dpp = 3 + (1000 - cum[2]) / pvs[3]
spp = 1000 / 350
mix = 3 + (1000 - cum[2]) / 350
chk(dpp, 3.542)
addn('BL', T, 3,
     'Dự án đầu tư 1.000 triệu đồng, dòng tiền ròng đều 350 triệu đồng cuối mỗi năm trong 4 năm, chi phí vốn 10%/năm. Thời gian hoàn vốn có chiết khấu của dự án xấp xỉ bao nhiêu năm?',
     [dpp, spp, mix, 4.0], lambda v: vn(v, 2) + ' năm',
     f'PV các năm: {vn(pvs[0],2)}; {vn(pvs[1],2)}; {vn(pvs[2],2)}; {vn(pvs[3],2)}. Lũy kế sau năm 3 = {vn(cum[2],2)}, còn thiếu {vn(1000-cum[2],2)}. DPP = 3 + {vn(1000-cum[2],2)}/{vn(pvs[3],2)} ≈ {vn(dpp,2)} năm. Hoàn vốn giản đơn = 1.000/350 = {vn(spp,2)} năm; chia phần thiếu cho dòng tiền chưa chiết khấu cho {vn(mix,2)} năm.',
     'Thời gian hoàn vốn có chiết khấu (discounted payback)')
add('BL', T, 1,
    'Khi thẩm định dòng tiền tăng thêm của một dự án mới, khoản mục nào sau đây KHÔNG được đưa vào dòng tiền của dự án?',
    ['Chi phí khảo sát thị trường đã chi trước khi ra quyết định đầu tư',
     'Chi phí cơ hội của mặt bằng doanh nghiệp đang sở hữu sẽ dùng cho dự án',
     'Nhu cầu vốn lưu động ròng tăng thêm khi dự án đi vào hoạt động',
     'Khoản tiết kiệm thuế nhờ chi phí khấu hao tài sản của dự án'],
    'Chi phí khảo sát đã chi là chi phí chìm: đã phát sinh và không thay đổi dù chấp nhận hay bác bỏ dự án, nên không đưa vào dòng tiền tăng thêm. Chi phí cơ hội, vốn lưu động tăng thêm và lá chắn thuế khấu hao đều là dòng tiền phù hợp.',
    'Nguyên tắc xác định dòng tiền tăng thêm: loại chi phí chìm, tính chi phí cơ hội')
add('BL', T, 2,
    'Khi xếp hạng hai dự án loại trừ lẫn nhau mà tiêu chuẩn NPV và IRR cho kết quả mâu thuẫn, doanh nghiệp nên lựa chọn như thế nào?',
    ['Chọn theo NPV, vì NPV đo trực tiếp phần giá trị tăng thêm và giả định tái đầu tư theo chi phí vốn hợp lý hơn',
     'Chọn theo IRR, vì tỷ lệ phần trăm dễ so sánh hơn giữa các dự án có quy mô khác nhau',
     'Chọn dự án có thời gian hoàn vốn ngắn hơn, vì rủi ro thấp hơn',
     'Chọn dự án có tổng dòng tiền chưa chiết khấu lớn hơn, vì tạo nhiều tiền hơn'],
    'Mâu thuẫn NPV–IRR thường do khác biệt quy mô hoặc thời điểm dòng tiền. NPV giả định tái đầu tư ở chi phí vốn và phản ánh trực tiếp mức tăng giá trị cổ đông; IRR giả định tái đầu tư ở chính IRR và bỏ qua quy mô, nên ưu tiên NPV.',
    'So sánh tiêu chuẩn NPV và IRR với dự án loại trừ nhau')

T = 'Tài trợ vốn cho hoạt động của doanh nghiệp'
wacc = 0.6 * 0.15 + 0.4 * 0.10 * 0.8
wbook = 300 / 700 * 0.15 + 400 / 700 * 0.08
chk(wacc, 0.122); chk(wbook, 0.11)
addn('BL', T, 3,
     'Doanh nghiệp có vốn chủ sở hữu giá trị sổ sách 300 tỷ đồng, giá trị thị trường 600 tỷ đồng; nợ vay có giá trị sổ sách và giá trị thị trường đều là 400 tỷ đồng. Chi phí vốn chủ sở hữu 15%, lãi suất vay trước thuế 10%, thuế suất thuế TNDN 20%. WACC tính theo trọng số giá trị thị trường là bao nhiêu?',
     [wacc, wbook, 0.125, 0.6 * 0.15 + 0.4 * 0.10], lambda v: pc(v, 1),
     f'Trọng số thị trường: E = 600/1.000 = 60%, D = 400/1.000 = 40%. Chi phí nợ sau thuế = 10% × (1 − 20%) = 8%. WACC = 60% × 15% + 40% × 8% = {pc(wacc,1)}. Dùng trọng số sổ sách cho {pc(wbook,1)}; bỏ qua thuế cho 13,0%; bình quân giản đơn cho 12,5%.',
     'WACC = wE·rE + wD·rD·(1 − t), trọng số theo giá trị thị trường')
add('BL', T, 2,
    'Nhận định nào sau đây đúng về chi phí sử dụng vốn của lợi nhuận giữ lại?',
    ['Là chi phí cơ hội, bằng tỷ suất sinh lời cổ đông đòi hỏi; thấp hơn chi phí cổ phiếu mới vì không có chi phí phát hành',
     'Bằng 0 vì doanh nghiệp không phải chi trả cho bất kỳ ai khi sử dụng nguồn vốn này',
     'Bằng lãi suất tiền gửi ngân hàng mà doanh nghiệp đang được hưởng',
     'Cao hơn chi phí phát hành cổ phiếu mới vì lợi nhuận giữ lại đã chịu thuế TNDN'],
    'Lợi nhuận giữ lại thuộc về cổ đông; nếu giữ lại thì cổ đông mất cơ hội tự đầu tư, nên chi phí của nó bằng tỷ suất sinh lời đòi hỏi trên vốn cổ phần (rE). Cổ phiếu mới có thêm chi phí phát hành nên chi phí cao hơn.',
    'Chi phí sử dụng vốn lợi nhuận giữ lại (chi phí cơ hội)')
d1 = 2000 * 1.06
rnew = d1 / (40000 * 0.95) + 0.06
chk(rnew, 0.11579)
addn('BL', T, 3,
     'Cổ phiếu của doanh nghiệp vừa trả cổ tức 2.000 đ/cp, cổ tức tăng trưởng đều 6%/năm, giá thị trường 40.000 đ/cp. Nếu phát hành cổ phiếu phổ thông mới theo giá thị trường, chi phí phát hành bằng 5% giá phát hành. Chi phí sử dụng vốn cổ phiếu phổ thông mới là bao nhiêu?',
     [rnew, d1 / 40000 + 0.06, 2000 / 38000 + 0.06, 2000 / 40000 + 0.06], lambda v: pc(v, 2),
     f'D1 = 2.000 × 1,06 = 2.120 đ; giá thuần = 40.000 × (1 − 5%) = 38.000 đ. rE mới = 2.120/38.000 + 6% = {pc(rnew,2)}. Bỏ chi phí phát hành cho {pc(d1/40000+0.06,2)}; dùng D0 thay D1 cho {pc(2000/38000+0.06,2)} hoặc 11,00%.',
     'Mô hình Gordon có chi phí phát hành: rE = D1/[P0(1 − f)] + g')
add('BL', T, 2,
    'Theo lý thuyết M&M trong điều kiện không có thuế, khi doanh nghiệp tăng tỷ lệ nợ trong cơ cấu vốn thì:',
    ['Chi phí vốn chủ sở hữu tăng, WACC và giá trị doanh nghiệp không đổi',
     'Chi phí vốn chủ sở hữu không đổi, WACC giảm và giá trị doanh nghiệp tăng',
     'Chi phí vốn chủ sở hữu tăng, WACC giảm và giá trị doanh nghiệp tăng',
     'Chi phí nợ và WACC cùng tăng, giá trị doanh nghiệp giảm'],
    'M&M không thuế: mệnh đề I – giá trị DN không phụ thuộc cơ cấu vốn; mệnh đề II – rE tăng tuyến tính theo D/E, bù đúng phần lợi ích của nợ rẻ hơn nên WACC không đổi. WACC giảm và giá trị tăng là kết luận của M&M có thuế.',
    'Mệnh đề I và II của Modigliani – Miller (không thuế)')
vl = 500 + 0.2 * 200
chk(vl, 540)
addn('BL', T, 3,
     'Theo lý thuyết M&M có thuế thu nhập doanh nghiệp, một doanh nghiệp không vay nợ có giá trị 500 tỷ đồng. Doanh nghiệp vay nợ vĩnh viễn 200 tỷ đồng để mua lại cổ phiếu; thuế suất thuế TNDN 20%. Giá trị doanh nghiệp sau khi vay nợ là bao nhiêu?',
     [vl, 500, 500 + 200 * 0.8, 700], lambda v: vn(v) + ' tỷ đồng',
     f'VL = VU + t × D = 500 + 20% × 200 = {vn(vl)} tỷ đồng (giá trị hiện tại của lá chắn thuế lãi vay = 40 tỷ). 500 là kết luận M&M không thuế; 660 và 700 là cộng nhầm số nợ vào giá trị.',
     'M&M có thuế: VL = VU + t·D')
add('BL', T, 1,
    'Theo lý thuyết trật tự phân hạng (pecking order), khi cần vốn cho dự án mới, doanh nghiệp sẽ ưu tiên sử dụng nguồn tài trợ nào trước tiên?',
    ['Lợi nhuận giữ lại (nguồn vốn nội bộ)',
     'Phát hành cổ phiếu phổ thông mới ra công chúng',
     'Phát hành trái phiếu chuyển đổi',
     'Vay nợ ngân hàng dài hạn'],
    'Do bất cân xứng thông tin, DN ưu tiên nguồn nội bộ (lợi nhuận giữ lại), tiếp đến là nợ, chứng khoán lai và cuối cùng mới phát hành cổ phiếu mới (dễ phát tín hiệu cổ phiếu đang bị định giá cao).',
    'Lý thuyết trật tự phân hạng (pecking order theory)')
terp = (4 * 30000 + 20000) / 5
chk(terp, 28000)
addn('BL', T, 3,
     'Công ty phát hành quyền mua cổ phần cho cổ đông hiện hữu với tỷ lệ thực hiện quyền 4:1 (sở hữu 4 cổ phiếu được mua 1 cổ phiếu mới), giá phát hành 20.000 đ/cp. Giá thị trường trước ngày giao dịch không hưởng quyền là 30.000 đ/cp. Giá lý thuyết của cổ phiếu sau khi pha loãng (giá điều chỉnh không hưởng quyền) là bao nhiêu?',
     [terp, (30000 + 4 * 20000) / 5, 30000 - 10000 / 4, (30000 + 20000) / 2], lambda v: vn(v) + ' đ',
     f'Giá lý thuyết = (4 × 30.000 + 1 × 20.000)/(4 + 1) = 140.000/5 = {vn(terp)} đ. Đảo tỷ lệ (1:4) cho 22.000 đ; lấy 30.000 − 10.000/4 cho 27.500 đ; bình quân giản đơn cho 25.000 đ.',
     'Giá lý thuyết sau phát hành quyền (TERP) = (N·P + S)/(N + 1)')
terp2 = (5 * 25000 + 2 * 18000) / 7
right = 25000 - terp2
chk(terp2, 23000); chk(right, 2000)
addn('BL', T, 3,
     'Công ty chào bán thêm cổ phiếu cho cổ đông hiện hữu theo tỷ lệ thực hiện quyền 5:2 (mỗi cổ phiếu được 1 quyền; 5 quyền được mua 2 cổ phiếu mới) với giá 18.000 đ/cp. Giá thị trường trước ngày giao dịch không hưởng quyền là 25.000 đ/cp. Giá trị lý thuyết của một quyền mua là bao nhiêu?',
     [right, 7000, 7000 * 2 / 5, 7000 / 7], lambda v: vn(v) + ' đ',
     f'Giá lý thuyết sau pha loãng = (5 × 25.000 + 2 × 18.000)/7 = 161.000/7 = {vn(terp2)} đ. Giá trị một quyền = 25.000 − {vn(terp2)} = {vn(right)} đ (tương đương (25.000 − 18.000)/(2,5 + 1)). 7.000 đ là chênh lệch giá chưa chia; 2.800 đ và 1.000 đ là chia sai số quyền.',
     'Giá trị quyền mua = P cum − TERP = (P − S)/(N + 1), N = số quyền cần cho 1 cổ phiếu mới')

T = 'Chính sách cổ tức và mua lại cổ phiếu của doanh nghiệp'
add('BL', T, 1,
    'Nhà đầu tư mua cổ phiếu vào đúng ngày giao dịch không hưởng quyền của đợt trả cổ tức bằng tiền thì:',
    ['Không được nhận cổ tức của đợt đó; quyền nhận cổ tức thuộc về người bán',
     'Được nhận cổ tức của đợt đó vì đã mua trước ngày đăng ký cuối cùng',
     'Được nhận một nửa số cổ tức của đợt đó, nửa còn lại thuộc về người bán',
     'Được nhận cổ tức nếu thanh toán đủ tiền mua ngay trong ngày giao dịch'],
    'Do chu kỳ thanh toán, người mua từ ngày giao dịch không hưởng quyền không có tên trong danh sách người sở hữu tại ngày đăng ký cuối cùng nên không được nhận cổ tức đợt đó; giá tham chiếu được điều chỉnh giảm tương ứng.',
    'Ngày giao dịch không hưởng quyền và ngày đăng ký cuối cùng')
add('BL', T, 2,
    'Lý thuyết "con chim trong tay" (bird-in-the-hand) về chính sách cổ tức cho rằng:',
    ['Nhà đầu tư ưa cổ tức tiền mặt hiện tại hơn lãi vốn kỳ vọng do ít rủi ro hơn, nên tỷ lệ chi trả cao có thể làm tăng giá trị doanh nghiệp',
     'Trong thị trường vốn hoàn hảo, chính sách cổ tức không ảnh hưởng đến giá trị doanh nghiệp',
     'Vì cổ tức chịu thuế cao hơn lãi vốn, doanh nghiệp nên duy trì tỷ lệ chi trả cổ tức thấp',
     'Doanh nghiệp chỉ trả cổ tức từ phần lợi nhuận còn lại sau khi tài trợ đủ các dự án có NPV dương'],
    'Gordon và Lintner: cổ tức hiện tại chắc chắn hơn lãi vốn tương lai nên nhà đầu tư đòi hỏi tỷ suất sinh lời thấp hơn với cổ phiếu trả cổ tức cao. Cổ tức không ảnh hưởng giá trị là quan điểm M&M; ưu tiên chi trả thấp do thuế là lý thuyết hiệu ứng thuế; trả từ phần còn lại là chính sách cổ tức thặng dư.',
    'Các lý thuyết về chính sách cổ tức')
add('BL', T, 2,
    'Lý do nào sau đây thường được đưa ra khi doanh nghiệp chọn mua lại cổ phiếu thay vì tăng cổ tức tiền mặt?',
    ['Phát tín hiệu cổ phiếu đang bị định giá thấp và linh hoạt hơn vì không tạo kỳ vọng duy trì mức chi trả hằng năm',
     'Làm tăng số lượng cổ phiếu đang lưu hành và tăng tính thanh khoản của cổ phiếu',
     'Làm giảm hệ số nợ trên vốn chủ sở hữu của doanh nghiệp',
     'Làm tăng vốn chủ sở hữu và giá trị sổ sách của doanh nghiệp'],
    'Mua lại cổ phiếu làm giảm số cổ phiếu lưu hành và giảm vốn chủ sở hữu (cổ phiếu quỹ ghi giảm VCSH) nên hệ số nợ/VCSH tăng. Ưu điểm: linh hoạt (cổ tức tiền mặt có tính "dính"), phát tín hiệu định giá thấp, có thể có lợi thế thuế cho cổ đông.',
    'Mua lại cổ phiếu (cổ phiếu quỹ) so với trả cổ tức tiền mặt')
adj = (45000 - 1500) / 1.1
chk(adj, 39545.45)
addn('BL', T, 3,
     'Cổ phiếu Y có giá đóng cửa 45.000 đ/cp trước ngày giao dịch không hưởng quyền. Công ty đồng thời trả cổ tức bằng tiền 1.500 đ/cp và cổ tức bằng cổ phiếu tỷ lệ 10:1 (sở hữu 10 cổ phiếu nhận thêm 1 cổ phiếu mới). Giá tham chiếu lý thuyết điều chỉnh vào ngày giao dịch không hưởng quyền (làm tròn đến đồng) là bao nhiêu?',
     [round(adj), round(45000 / 1.1 - 1500), 43500, round(45000 / 1.1)], lambda v: vn(v) + ' đ',
     f'Giá điều chỉnh = (45.000 − 1.500)/(1 + 10%) = 43.500/1,1 ≈ {vn(round(adj))} đ. Trừ cổ tức tiền sau khi chia cho 1,1 cho 39.409 đ; chỉ trừ cổ tức tiền cho 43.500 đ; chỉ điều chỉnh cổ tức cổ phiếu cho 40.909 đ.',
     'Giá điều chỉnh = (P − cổ tức tiền)/(1 + tỷ lệ cổ tức cổ phiếu)')
ni2 = 120 - 240 * 0.04
sh2 = 100 - 240e9 / 24000 / 1e6
eps2 = ni2 * 1e9 / (sh2 * 1e6)
chk(eps2, 1226.67)
addn('BL', T, 3,
     'Công ty Z có lợi nhuận sau thuế 120 tỷ đồng, 100 triệu cổ phiếu lưu hành, giá thị trường 24.000 đ/cp. Z dùng 240 tỷ đồng tiền nhàn rỗi (đang mang lại lợi suất sau thuế 4%/năm) để mua lại cổ phiếu quỹ theo giá thị trường. Các yếu tố khác không đổi, EPS sau khi mua lại xấp xỉ bao nhiêu?',
     [eps2, 1200, 120e9 / 90e6, ni2 * 1e9 / 100e6], lambda v: vn(v) + ' đ',
     f'Số cổ phiếu mua lại = 240 tỷ/24.000 = 10 triệu → còn {vn(sh2)} triệu cp. Lợi nhuận mất đi = 240 × 4% = 9,6 tỷ → LNST = {vn(ni2,1)} tỷ. EPS = {vn(ni2,1)} tỷ/{vn(sh2)} triệu ≈ {vn(eps2)} đ (trước đó 1.200 đ). Bỏ qua thu nhập tiền mất đi cho 1.333 đ; quên giảm số cổ phiếu cho 1.104 đ.',
     'Ảnh hưởng của mua lại cổ phiếu tới EPS')

T = 'Tái cấu trúc doanh nghiệp, sáp nhập và mua lại doanh nghiệp'
add('BL', T, 1,
    'Một nhà sản xuất thép mua lại doanh nghiệp khai thác quặng sắt đang cung cấp nguyên liệu cho mình. Đây là hình thức mua lại, sáp nhập nào?',
    ['Sáp nhập theo chiều dọc', 'Sáp nhập theo chiều ngang', 'Sáp nhập tập đoàn (hỗn hợp)', 'Sáp nhập mở rộng thị trường'],
    'Sáp nhập theo chiều dọc là kết hợp các doanh nghiệp ở các công đoạn khác nhau trong cùng chuỗi giá trị (nhà cung cấp – nhà sản xuất – nhà phân phối). Chiều ngang là cùng ngành, cùng công đoạn; tập đoàn là các ngành không liên quan.',
    'Phân loại M&A: chiều ngang, chiều dọc, tập đoàn')
add('BL', T, 2,
    'Công ty mục tiêu quy định: khi một bên thâu tóm vượt ngưỡng sở hữu 20% mà không được HĐQT chấp thuận, tất cả cổ đông còn lại được quyền mua thêm cổ phiếu mới với giá chiết khấu sâu. Biện pháp chống thâu tóm này là:',
    ['Viên thuốc độc (poison pill)', 'Hiệp sĩ trắng (white knight)', 'Chiếc dù vàng (golden parachute)', 'Mua lại cổ phiếu xanh (greenmail)'],
    'Viên thuốc độc pha loãng mạnh tỷ lệ sở hữu và làm tăng chi phí của bên thâu tóm. Hiệp sĩ trắng là tìm bên mua thân thiện; dù vàng là khoản bồi thường lớn cho ban điều hành khi mất chức; greenmail là mua lại cổ phần của bên thâu tóm với giá cao.',
    'Các biện pháp phòng thủ chống thâu tóm thù địch')
add('BL', T, 2,
    'Công ty A tách mảng kinh doanh X thành công ty B độc lập; cổ đông của A được nhận cổ phần của B theo tỷ lệ sở hữu tại A và A không thu tiền từ giao dịch này. Đây là hình thức tái cấu trúc nào?',
    ['Tách doanh nghiệp độc lập (spin-off)',
     'Bán bộ phận kinh doanh cho bên thứ ba (divestiture)',
     'Bán một phần cổ phần công ty con ra công chúng (carve-out)',
     'Thâu tóm doanh nghiệp bằng vốn vay (leveraged buyout)'],
    'Spin-off phân phối cổ phần công ty mới cho cổ đông hiện hữu, công ty mẹ không thu tiền. Divestiture là bán cho bên ngoài lấy tiền; equity carve-out là bán một phần cổ phần công ty con ra công chúng (thu tiền); LBO là thâu tóm chủ yếu bằng nợ vay.',
    'Các hình thức tái cấu trúc doanh nghiệp (thu hẹp)')
syn = 1100 - (800 + 200)
prem = 260 - 200
gain = syn - prem
chk(gain, 40)
addn('BL', T, 3,
     'Công ty A (giá trị 800 tỷ đồng) mua lại toàn bộ công ty B (giá trị độc lập 200 tỷ đồng) bằng tiền mặt với giá 260 tỷ đồng. Giá trị công ty hợp nhất dự kiến là 1.100 tỷ đồng. NPV của thương vụ đối với cổ đông công ty A là bao nhiêu?',
     [gain, -prem, prem, syn], lambda v: vn(v) + ' tỷ đồng',
     f'Giá trị cộng hưởng = 1.100 − (800 + 200) = {vn(syn)} tỷ; phần bù trả cho B = 260 − 200 = {vn(prem)} tỷ. NPV của A = cộng hưởng − phần bù = {vn(syn)} − {vn(prem)} = {vn(gain)} tỷ đồng (= 1.100 − 260 − 800).',
     'NPV thương vụ M&A = Giá trị cộng hưởng − Phần bù thâu tóm')

T = 'Bảo lãnh phát hành chứng khoán'
add('BL', T, 1,
    'Theo Luật Chứng khoán, cam kết nào sau đây của tổ chức bảo lãnh với tổ chức phát hành thuộc khái niệm bảo lãnh phát hành chứng khoán?',
    ['Cố gắng tối đa để phân phối số chứng khoán cần phát hành của tổ chức phát hành',
     'Mua lại toàn bộ chứng khoán từ nhà đầu tư sau khi chứng khoán được niêm yết',
     'Bảo đảm giá giao dịch của chứng khoán không giảm dưới giá chào bán trong 1 năm',
     'Cho tổ chức phát hành vay số tiền tương ứng với giá trị của đợt phát hành'],
    'Luật định nghĩa bảo lãnh phát hành gồm: nhận mua một phần/toàn bộ chứng khoán để bán lại, mua số chứng khoán còn lại chưa phân phối hết, hoặc cố gắng tối đa để phân phối. Không bao gồm bảo đảm giá, mua lại từ nhà đầu tư hay cho vay.',
    f'Khoản 31 Điều 4 {LAWB}',
    'Bảo lãnh phát hành chứng khoán là việc cam kết với tổ chức phát hành nhận mua một phần hoặc toàn bộ chứng khoán của tổ chức phát hành để bán lại hoặc mua số chứng khoán còn lại chưa được phân phối hết hoặc cố gắng tối đa để phân phối số chứng khoán cần phát hành của tổ chức phát hành.',
    LAW)
add('BL', T, 1,
    'Trong phương thức bảo lãnh phát hành với cam kết chắc chắn (firm commitment), rủi ro không phân phối hết chứng khoán thuộc về:',
    ['Tổ chức bảo lãnh phát hành', 'Tổ chức phát hành chứng khoán', 'Nhà đầu tư đã đăng ký mua', 'Đại lý phân phối chứng khoán'],
    'Với cam kết chắc chắn, tổ chức bảo lãnh mua toàn bộ chứng khoán của tổ chức phát hành (hoặc cam kết mua phần còn lại) theo giá thỏa thuận rồi bán lại, nên tự chịu rủi ro không bán hết và rủi ro giá; tổ chức phát hành chắc chắn nhận đủ tiền.',
    'Các phương thức bảo lãnh phát hành: cam kết chắc chắn')
add('BL', T, 2,
    'Theo phương thức bảo lãnh "tất cả hoặc không" (all-or-none), nếu không phân phối hết số chứng khoán dự kiến thì:',
    ['Đợt phát hành bị hủy bỏ và tiền đặt mua được hoàn trả cho nhà đầu tư',
     'Tổ chức bảo lãnh phải mua toàn bộ số chứng khoán còn lại theo giá bảo lãnh',
     'Tổ chức phát hành giữ số tiền đã thu và chào bán phần còn lại ở đợt sau',
     'Tổ chức bảo lãnh chỉ hưởng phí tương ứng với số chứng khoán đã phân phối'],
    'All-or-none là một dạng của bảo lãnh cố gắng tối đa: tổ chức phát hành cần huy động đủ toàn bộ số vốn; nếu không bán hết thì hủy đợt phát hành, hoàn tiền. Việc phải mua phần còn lại là đặc trưng của cam kết chắc chắn.',
    'Các phương thức bảo lãnh: cố gắng tối đa, tất cả hoặc không, tối thiểu – tối đa')
add('BL', T, 2,
    'Mục đích chính của phương pháp dựng sổ lệnh (book building) trong đợt IPO là gì?',
    ['Xác định giá chào bán và phân bổ khối lượng dựa trên nhu cầu đặt mua của nhà đầu tư, chủ yếu là nhà đầu tư tổ chức',
     'Bảo đảm tổ chức bảo lãnh không phải mua số chứng khoán chưa phân phối hết',
     'Thay thế thủ tục đăng ký chào bán chứng khoán ra công chúng với cơ quan quản lý',
     'Xác định giá trị sổ sách của doanh nghiệp trước khi phát hành'],
    'Dựng sổ: tổ chức bảo lãnh đưa ra khoảng giá dự kiến, thu thập lượng đặt mua ở từng mức giá để xác định giá cuối cùng và phân bổ. Phương pháp này không loại bỏ rủi ro bảo lãnh hay thủ tục đăng ký chào bán.',
    'Phương pháp xác định giá phát hành: dựng sổ lệnh')
add('BL', T, 2,
    'Trong quy trình bảo lãnh phát hành chứng khoán ra công chúng, công việc nào được thực hiện SAU khi Giấy chứng nhận đăng ký chào bán có hiệu lực?',
    ['Công bố bản thông báo phát hành và tổ chức phân phối chứng khoán cho nhà đầu tư',
     'Thẩm định tình hình tài chính của tổ chức phát hành và lựa chọn phương thức bảo lãnh',
     'Lập và nộp hồ sơ đăng ký chào bán chứng khoán lên Ủy ban Chứng khoán Nhà nước',
     'Ký thư dự định (thỏa thuận sơ bộ) giữa tổ chức bảo lãnh và tổ chức phát hành'],
    'Trình tự: tiếp xúc, thẩm định, ký thỏa thuận sơ bộ → thành lập tổ hợp, chuẩn bị và nộp hồ sơ đăng ký → được cấp Giấy chứng nhận đăng ký chào bán → công bố thông báo phát hành, phân phối, thu tiền, báo cáo kết quả. Việc phân phối chỉ được thực hiện sau khi giấy chứng nhận có hiệu lực.',
    'Quy trình bảo lãnh phát hành chứng khoán')
uw = 8e6 * (20000 - 19000) + 2e6 * (17500 - 19000) - 1.2e9
chk(uw / 1e9, 3.8)
addn('BL', T, 3,
     'CTCK X bảo lãnh phát hành theo phương thức cam kết chắc chắn 10 triệu cổ phiếu, mua của tổ chức phát hành với giá 19.000 đ/cp, giá chào bán ra công chúng 20.000 đ/cp. X bán được 8 triệu cổ phiếu theo giá chào bán; 2 triệu cổ phiếu còn lại X phải giữ và sau đó bán ra với giá 17.500 đ/cp. Chi phí phân phối của X là 1,2 tỷ đồng. Lãi (lỗ) của X từ đợt bảo lãnh là bao nhiêu?',
     [uw / 1e9, 5.0, 6.8, 10.0], lambda v: vn(v, 1) + ' tỷ đồng',
     f'Lãi trên 8 triệu cp đã bán = 8 triệu × 1.000 = 8,0 tỷ; lỗ trên 2 triệu cp còn lại = 2 triệu × (17.500 − 19.000) = −3,0 tỷ; trừ chi phí 1,2 tỷ → lãi = {vn(uw/1e9,1)} tỷ đồng. Bỏ chi phí cho 5,0 tỷ; bỏ khoản lỗ cho 6,8 tỷ; giả định bán hết cho 10,0 tỷ.',
     'Kết quả bảo lãnh cam kết chắc chắn: chênh lệch giá bảo lãnh và giá bán, trừ chi phí')

T = 'Tư vấn cổ phần hóa doanh nghiệp'
add('BL', T, 1,
    'Khi xác định giá trị doanh nghiệp để cổ phần hóa theo phương pháp tài sản, giá trị doanh nghiệp được xác định dựa trên:',
    ['Giá trị thực tế toàn bộ tài sản hiện có của doanh nghiệp tại thời điểm xác định giá trị, theo giá thị trường',
     'Giá trị hiện tại của dòng tiền tự do dự kiến trong tương lai chiết khấu theo chi phí vốn',
     'Tích số giữa lợi nhuận sau thuế và hệ số P/E bình quân của các doanh nghiệp cùng ngành',
     'Giá trị sổ sách của vốn chủ sở hữu trên báo cáo tài chính đã kiểm toán năm gần nhất'],
    'Phương pháp tài sản đánh giá lại tài sản theo giá thị trường tại thời điểm xác định giá trị; giá trị thực tế phần vốn chủ sở hữu = giá trị thực tế doanh nghiệp − nợ thực tế phải trả. Chiết khấu dòng tiền và P/E là các phương pháp khác; giá trị sổ sách chưa phản ánh giá thị trường.',
    'Phương pháp tài sản trong xác định giá trị doanh nghiệp cổ phần hóa')
v_dcf = 50 * 1.04 / 0.08 * 1e9 / 25e6
chk(v_dcf, 26000)
addn('BL', T, 3,
     'Khi tư vấn định giá cổ phần lần đầu, chuyên viên ước tính dòng tiền tự do vốn chủ sở hữu (FCFE) năm vừa qua của doanh nghiệp là 50 tỷ đồng, tăng trưởng đều 4%/năm vĩnh viễn; chi phí vốn chủ sở hữu 12%/năm. Doanh nghiệp có 25 triệu cổ phần. Giá trị một cổ phần theo mô hình FCFE tăng trưởng đều là bao nhiêu?',
     [v_dcf, 50 / 0.08 * 40, 52 / 0.12 * 40, 50 / 0.12 * 40], lambda v: vn(v) + ' đ',
     f'FCFE1 = 50 × 1,04 = 52 tỷ; giá trị VCSH = 52/(12% − 4%) = 650 tỷ; mỗi cổ phần = 650 tỷ/25 triệu = {vn(v_dcf)} đ. Dùng FCFE0 cho 25.000 đ; chia cho rE thay vì (rE − g) cho 17.333 đ hoặc 16.667 đ.',
     'Mô hình FCFE tăng trưởng đều: V0 = FCFE1/(rE − g)')
eq = 900 + 150 - 30 - 580
vps = eq * 1e9 / 30e6
chk(vps, 14666.67)
addn('BL', T, 3,
     'Doanh nghiệp X cổ phần hóa có tổng tài sản theo sổ sách 900 tỷ đồng, nợ phải trả thực tế 580 tỷ đồng. Khi xác định giá trị theo phương pháp tài sản: quyền sử dụng đất được đánh giá tăng thêm 150 tỷ đồng; các khoản phải thu không có khả năng thu hồi bị loại trừ 30 tỷ đồng. Vốn điều lệ dự kiến là 300 tỷ đồng, mệnh giá 10.000 đ/cp. Giá trị thực tế vốn chủ sở hữu tính bình quân cho một cổ phần là bao nhiêu?',
     [round(vps), round(290e9 / 30e6), round(320e9 / 30e6), round(470e9 / 30e6)], lambda v: vn(v) + ' đ',
     f'Giá trị thực tế VCSH = 900 + 150 − 30 − 580 = {vn(eq)} tỷ đồng; số cổ phần = 300 tỷ/10.000 = 30 triệu; bình quân = {vn(eq)} tỷ/30 triệu ≈ {vn(round(vps))} đ. Bỏ phần đánh giá tăng cho 9.667 đ; dùng số sổ sách cho 10.667 đ; không loại nợ khó đòi cho 15.667 đ.',
     'Phương pháp tài sản: VCSH thực tế = Tài sản đánh giá lại − Nợ thực tế phải trả')

# ============================== QU ==============================
T = 'Tổng quan về ngành quản lý tài sản và hoạt động quản lý danh mục đầu tư'
add('QU', T, 2,
    'Theo Luật Chứng khoán, chứng chỉ quỹ đóng đã chào bán ra công chúng không được mua lại theo yêu cầu của nhà đầu tư. Hệ quả nào sau đây đúng?',
    ['Nhà đầu tư muốn thoái vốn phải bán chứng chỉ quỹ trên thị trường; giá giao dịch có thể cao hơn hoặc thấp hơn NAV/chứng chỉ quỹ',
     'Công ty quản lý quỹ phải mua lại chứng chỉ quỹ theo NAV vào các ngày giao dịch định kỳ',
     'Quỹ được tự do phát hành thêm chứng chỉ quỹ cho nhà đầu tư mới theo NAV hằng ngày',
     'Giá giao dịch chứng chỉ quỹ trên thị trường luôn bằng NAV/chứng chỉ quỹ'],
    'Quỹ đóng không mua lại chứng chỉ quỹ nên thanh khoản cho nhà đầu tư đến từ giao dịch trên thị trường, giá do cung cầu quyết định nên thường có chiết khấu/thặng dư so với NAV. Quỹ đóng tăng vốn phải được UBCKNN chấp thuận và phát hành cho nhà đầu tư hiện hữu qua quyền mua (Điều 112).',
    f'Khoản 40 Điều 4; Điều 112 {LAWB}',
    'Quỹ đóng là quỹ đại chúng mà chứng chỉ quỹ đã chào bán ra công chúng không được mua lại theo yêu cầu của nhà đầu tư.',
    LAW)
add('QU', T, 1,
    'Theo Luật Chứng khoán, quỹ thành viên là quỹ đầu tư chứng khoán có:',
    ['Từ 02 đến 99 thành viên góp vốn và chỉ bao gồm nhà đầu tư chứng khoán chuyên nghiệp',
     'Từ 02 đến 100 thành viên góp vốn, gồm cả nhà đầu tư cá nhân không chuyên nghiệp',
     'Tối thiểu 100 nhà đầu tư, không kể nhà đầu tư chứng khoán chuyên nghiệp',
     'Từ 02 đến 50 thành viên góp vốn và chỉ bao gồm nhà đầu tư tổ chức trong nước'],
    'Quỹ thành viên: 02–99 thành viên, chỉ gồm nhà đầu tư chứng khoán chuyên nghiệp (vốn góp tối thiểu 50 tỷ đồng theo Điều 113). Ngưỡng ít nhất 100 nhà đầu tư là điều kiện thành lập quỹ đại chúng.',
    f'Khoản 41 Điều 4 {LAWB}',
    'Quỹ thành viên là quỹ đầu tư chứng khoán có số thành viên tham gia góp vốn từ 02 đến 99 thành viên và chỉ bao gồm thành viên là nhà đầu tư chứng khoán chuyên nghiệp.',
    LAW)
add('QU', T, 2,
    'Trong bản chính sách đầu tư (IPS) của khách hàng, yếu tố nào sau đây thuộc nhóm ràng buộc đầu tư chứ không phải mục tiêu đầu tư?',
    ['Nhu cầu thanh khoản và thời hạn đầu tư của khách hàng',
     'Mức lợi suất mục tiêu 10%/năm của danh mục',
     'Mức độ sẵn lòng chấp nhận rủi ro của khách hàng',
     'Khả năng chịu đựng tổn thất của khách hàng'],
    'IPS gồm mục tiêu (lợi suất; rủi ro – sẵn lòng và khả năng chấp nhận rủi ro) và các ràng buộc: thanh khoản, thời hạn đầu tư, thuế, pháp lý – quy định, yêu cầu đặc thù.',
    'Bản chính sách đầu tư (IPS): mục tiêu và ràng buộc')

T = 'Các lý thuyết về danh mục đầu tư'
var = 0.6**2 * 0.2**2 + 0.4**2 * 0.1**2 + 2 * 0.6 * 0.4 * 0.2 * 0.1 * 0.3
sp = math.sqrt(var)
s0 = math.sqrt(0.6**2 * 0.04 + 0.4**2 * 0.01)
s1 = math.sqrt(0.6**2 * 0.04 + 0.4**2 * 0.01 + 0.6 * 0.4 * 0.2 * 0.1 * 0.3)
chk(sp, 0.137405)
addn('QU', T, 3,
     'Danh mục gồm 60% cổ phiếu A (độ lệch chuẩn 20%) và 40% cổ phiếu B (độ lệch chuẩn 10%); hệ số tương quan giữa A và B là 0,3. Độ lệch chuẩn của danh mục là bao nhiêu?',
     [sp, s0, s1, 0.16], lambda v: pc(v, 2),
     f'σp² = 0,6² × 0,2² + 0,4² × 0,1² + 2 × 0,6 × 0,4 × 0,2 × 0,1 × 0,3 = 0,0144 + 0,0016 + 0,00288 = {vn(var,5)}; σp = {pc(sp,2)}. Bỏ hiệp phương sai cho {pc(s0,2)}; quên hệ số 2 cho {pc(s1,2)}; bình quân gia quyền độ lệch chuẩn cho 16,00% (chỉ đúng khi ρ = 1).',
     'Phương sai danh mục 2 tài sản: σp² = wA²σA² + wB²σB² + 2wAwBρσAσB')
req = 0.04 + 1.3 * (0.11 - 0.04)
chk(req, 0.131)
add('QU', T, 3,
    'Lãi suất phi rủi ro 4%/năm, lợi suất kỳ vọng của danh mục thị trường 11%/năm. Cổ phiếu K có beta 1,3; chuyên viên phân tích dự báo lợi suất kỳ vọng của K là 12%/năm. Theo CAPM, tỷ suất sinh lời yêu cầu của K và khuyến nghị phù hợp là:',
    [f'{pc(req)}; K bị định giá cao (nằm dưới SML), nên bán',
     f'{pc(req)}; K bị định giá thấp (nằm trên SML), nên mua',
     f'{pc(1.3*0.11)}; K bị định giá cao (nằm dưới SML), nên bán',
     f'{pc(0.11)}; K bị định giá thấp (nằm trên SML), nên mua'],
    f'Lợi suất yêu cầu = 4% + 1,3 × (11% − 4%) = {pc(req)}. Lợi suất dự báo 12% < {pc(req)} → K nằm dưới SML (alpha âm), bị định giá cao → nên bán. 14,3% là lỗi nhân beta với cả lợi suất thị trường; 11,0% là bỏ qua beta.',
    'CAPM: E(Ri) = rf + βi[E(Rm) − rf]; so sánh với SML')
apt = 0.05 + 1.2 * 0.04 + 0.5 * 0.02
chk(apt, 0.108)
addn('QU', T, 3,
     'Theo mô hình APT hai nhân tố, lãi suất phi rủi ro 5%; phần bù rủi ro của nhân tố 1 (tăng trưởng GDP) là 4% và nhân tố 2 (lạm phát) là 2%. Cổ phiếu M có độ nhạy với nhân tố 1 là 1,2 và với nhân tố 2 là 0,5. Lợi suất kỳ vọng của M là bao nhiêu?',
     [apt, apt - 0.05, 0.05 + 0.04 + 0.02, 0.05 + 1.2 * (0.04 + 0.02)], lambda v: pc(v, 1),
     f'E(R) = 5% + 1,2 × 4% + 0,5 × 2% = 5% + 4,8% + 1,0% = {pc(apt)}. Quên cộng lãi suất phi rủi ro cho 5,8%; bỏ qua độ nhạy cho 11,0%; áp một hệ số 1,2 cho cả hai nhân tố cho 12,2%.',
     'APT: E(Ri) = rf + Σ bik·λk')
add('QU', T, 1,
    'Theo lý thuyết danh mục của Markowitz, đường biên hiệu quả (efficient frontier) là tập hợp các danh mục:',
    ['Có lợi suất kỳ vọng cao nhất ứng với mỗi mức rủi ro (độ lệch chuẩn) cho trước',
     'Có độ lệch chuẩn cao nhất ứng với mỗi mức lợi suất kỳ vọng cho trước',
     'Gồm các cổ phiếu riêng lẻ có hệ số beta đúng bằng 1',
     'Có lợi suất kỳ vọng bằng lãi suất phi rủi ro ở mọi mức rủi ro'],
    'Danh mục hiệu quả là danh mục không bị "trội hơn": cùng rủi ro không có danh mục nào lợi suất cao hơn, cùng lợi suất không có danh mục nào rủi ro thấp hơn. Đường biên hiệu quả là phần phía trên của đường biên phương sai tối thiểu.',
    'Lý thuyết danh mục hiện đại (Markowitz) – đường biên hiệu quả')
add('QU', T, 2,
    'Phát biểu nào sau đây đúng về đường thị trường vốn (CML) và đường thị trường chứng khoán (SML)?',
    ['CML áp dụng cho danh mục hiệu quả và đo rủi ro bằng độ lệch chuẩn; SML áp dụng cho mọi tài sản và đo rủi ro bằng beta',
     'CML áp dụng cho mọi tài sản và đo rủi ro bằng beta; SML chỉ áp dụng cho danh mục hiệu quả và đo rủi ro bằng độ lệch chuẩn',
     'CML và SML đều đo rủi ro bằng beta, chỉ khác nhau ở lãi suất phi rủi ro sử dụng',
     'SML chỉ áp dụng cho danh mục thị trường, còn CML áp dụng cho từng cổ phiếu riêng lẻ'],
    'CML: E(Rp) = rf + [(E(Rm) − rf)/σm]·σp, chỉ cho danh mục kết hợp tài sản phi rủi ro với danh mục thị trường (danh mục hiệu quả). SML: E(Ri) = rf + βi[E(Rm) − rf], cho mọi chứng khoán/danh mục vì chỉ rủi ro hệ thống được bù đắp.',
    'CML và SML trong mô hình CAPM')

T = 'Phân bổ tài sản'
add('QU', T, 2,
    'Khi giá cổ phiếu tăng mạnh, nhà quản lý áp dụng chiến lược tỷ trọng cố định (constant-mix) sẽ:',
    ['Bán bớt cổ phiếu, mua thêm trái phiếu để đưa danh mục về tỷ trọng mục tiêu',
     'Mua thêm cổ phiếu vì tỷ lệ tài sản rủi ro được phép tăng theo giá trị danh mục',
     'Giữ nguyên danh mục, không giao dịch cho tới khi hết thời hạn đầu tư',
     'Chuyển toàn bộ danh mục sang tiền mặt để khóa lợi nhuận'],
    'Constant-mix tái cân bằng ngược chiều thị trường (bán tài sản tăng giá, mua tài sản giảm giá), hiệu quả khi thị trường đi ngang dao động. Mua thêm khi giá tăng là đặc trưng của CPPI; giữ nguyên là chiến lược mua và nắm giữ.',
    'Chiến lược tái cân bằng: mua và nắm giữ, constant-mix, CPPI')
st, bd = 600 * 1.2, 400 * 1.02
sell = st - 0.6 * (st + bd)
chk(sell, 43.2)
addn('QU', T, 3,
     'Danh mục 1.000 tỷ đồng có tỷ trọng mục tiêu (phân bổ tài sản chiến lược) 60% cổ phiếu, 40% trái phiếu. Sau một năm, phần cổ phiếu tăng 20%, phần trái phiếu tăng 2%. Để đưa danh mục về tỷ trọng mục tiêu, nhà quản lý cần bán bao nhiêu tỷ đồng cổ phiếu?',
     [sell, 0.4 * 120, 72.0, 120.0], lambda v: vn(v, 1) + ' tỷ đồng',
     f'Cổ phiếu = 600 × 1,2 = {vn(st)} tỷ; trái phiếu = 400 × 1,02 = {vn(bd)} tỷ; tổng = {vn(st+bd)} tỷ. Cổ phiếu mục tiêu = 60% × {vn(st+bd)} = {vn(0.6*(st+bd),1)} tỷ → bán {vn(sell,1)} tỷ đồng. Lấy mục tiêu theo quy mô cũ (600) cho 120 tỷ.',
     'Tái cân bằng danh mục về tỷ trọng phân bổ tài sản chiến lược')

T = 'Quản lý danh mục đầu tư cổ phiếu'
add('QU', T, 1,
    'Nhà quản lý danh mục theo phong cách đầu tư giá trị (value investing) thường ưu tiên những cổ phiếu có đặc điểm:',
    ['P/E, P/B thấp và tỷ suất cổ tức tương đối cao',
     'Tốc độ tăng trưởng EPS cao và P/E cao hơn bình quân thị trường',
     'Vốn hóa nhỏ, bất kể mức định giá hiện tại',
     'Đà tăng giá mạnh trong 3–6 tháng gần nhất'],
    'Phong cách giá trị tìm cổ phiếu bị định giá thấp so với giá trị nội tại (P/E, P/B thấp, cổ tức cao). Tăng trưởng cao kèm P/E cao là phong cách tăng trưởng; đà tăng giá là chiến lược động lượng.',
    'Phong cách đầu tư cổ phiếu: giá trị, tăng trưởng')
add('QU', T, 2,
    'Một quỹ chỉ số không mua toàn bộ cổ phiếu trong chỉ số mà chia chỉ số thành các nhóm theo ngành và quy mô vốn hóa, rồi chọn một số cổ phiếu đại diện sao cho tỷ trọng từng nhóm khớp với chỉ số. Đây là phương pháp:',
    ['Lấy mẫu phân tầng (stratified sampling)',
     'Mô phỏng toàn bộ (full replication)',
     'Quản lý chủ động dựa trên lựa chọn cổ phiếu',
     'Đầu tư theo phương pháp bình quân giá (DCA)'],
    'Lấy mẫu phân tầng giảm chi phí giao dịch so với mô phỏng toàn bộ nhưng chấp nhận sai lệch theo dõi lớn hơn. Quản lý chủ động nhằm vượt chỉ số; DCA là cách giải ngân định kỳ, không phải kỹ thuật mô phỏng chỉ số.',
    'Quản lý thụ động: các phương pháp mô phỏng chỉ số')
bp = 0.4 * 1.4 + 0.35 * 0.9 + 0.25 * 0.6
chk(bp, 1.025)
addn('QU', T, 2,
     'Danh mục cổ phiếu gồm: 40% cổ phiếu có beta 1,4; 35% cổ phiếu có beta 0,9 và 25% cổ phiếu có beta 0,6. Beta của danh mục là bao nhiêu?',
     [bp, (1.4 + 0.9 + 0.6) / 3, 0.4 * 0.6 + 0.35 * 0.9 + 0.25 * 1.4, 1.4 + 0.9 + 0.6], lambda v: vn(v, 3),
     f'βp = 0,40 × 1,4 + 0,35 × 0,9 + 0,25 × 0,6 = 0,560 + 0,315 + 0,150 = {vn(bp,3)}. Bình quân giản đơn cho 0,967; ghép nhầm tỷ trọng cho 0,905; cộng các beta cho 2,900.',
     'Beta danh mục = Σ wi·βi')
ap = [3.2, 1.5, -0.7, 2.0, 4.1]
bm = [2.0, 2.0, -1.5, 3.0, 3.6]
dif = [a - b for a, b in zip(ap, bm)]
mu = sum(dif) / 5
te = math.sqrt(sum((d - mu) ** 2 for d in dif) / 4) / 100
tep = math.sqrt(sum((d - mu) ** 2 for d in dif) / 5) / 100
mad = sum(abs(d) for d in dif) / 5 / 100
chk(te, 0.0091924)
addn('QU', T, 3,
     'Lợi suất theo quý của danh mục trong 5 quý lần lượt là 3,2%; 1,5%; −0,7%; 2,0%; 4,1%; của chỉ số tham chiếu lần lượt là 2,0%; 2,0%; −1,5%; 3,0%; 3,6%. Sai lệch theo dõi (tracking error) theo quý, tính bằng độ lệch chuẩn mẫu (chia n − 1) của lợi suất chênh lệch, là bao nhiêu?',
     [te, tep, mad, mu / 100], lambda v: pc(v, 2),
     f'Chênh lệch: 1,2; −0,5; 0,8; −1,0; 0,5 (%), bình quân {vn(mu,1)}%. Tổng bình phương độ lệch = 1,00 + 0,49 + 0,36 + 1,44 + 0,09 = 3,38; phương sai mẫu = 3,38/4 = 0,845; TE = {pc(te,2)}. Chia n cho {pc(tep,2)}; bình quân trị tuyệt đối cho {pc(mad,2)}; bình quân chênh lệch (lợi suất chủ động) là {pc(mu/100,2)}.',
     'Tracking error = độ lệch chuẩn của (Rp − Rb)')

T = 'Quản lý danh mục đầu tư trái phiếu'
cfs = [8, 8, 108]
pvb = [c / 1.1 ** (t + 1) for t, c in enumerate(cfs)]
price = sum(pvb)
mac = sum((t + 1) * v for t, v in enumerate(pvb)) / price
mod = mac / 1.1
chk(mac, 2.77738)
addn('QU', T, 3,
     'Trái phiếu kỳ hạn 3 năm, mệnh giá 100, lãi suất coupon 8%/năm trả cuối mỗi năm, lợi suất đáo hạn 10%/năm. Thời gian đáo hạn bình quân Macaulay (Macaulay duration) của trái phiếu xấp xỉ bao nhiêu?',
     [mac, mod, 3.0, 2.0], lambda v: vn(v, 2) + ' năm',
     f'PV dòng tiền: 8/1,1 = {vn(pvb[0],4)}; 8/1,1² = {vn(pvb[1],4)}; 108/1,1³ = {vn(pvb[2],4)}; giá = {vn(price,4)}. D = (1 × {vn(pvb[0],4)} + 2 × {vn(pvb[1],4)} + 3 × {vn(pvb[2],4)})/{vn(price,4)} ≈ {vn(mac,2)} năm. Duration điều chỉnh = {vn(mac,2)}/1,1 ≈ {vn(mod,2)}; 3,00 là kỳ hạn; 2,00 là bình quân giản đơn các mốc thời gian.',
     'Macaulay duration = Σ t·PV(CFt)/P')
dp = -6.5 * 0.01 + 0.5 * 55 * 0.01 ** 2
chk(dp, -0.06225)
addn('QU', T, 3,
     'Trái phiếu có duration điều chỉnh 6,5 và độ lồi (convexity) 55. Nếu lợi suất đáo hạn tăng 1 điểm phần trăm (100 điểm cơ bản), giá trái phiếu thay đổi xấp xỉ bao nhiêu phần trăm?',
     [dp, -0.065, -0.065 - 0.5 * 55 * 0.0001, -0.065 + 55 * 0.0001], lambda v: pc(round(v, 6), 3),
     f'%ΔP ≈ −Dmod × Δy + ½ × C × (Δy)² = −6,5 × 0,01 + 0,5 × 55 × 0,0001 = −6,500% + 0,275% = {pc(round(dp,6),3)}. Chỉ dùng duration cho −6,500%; trừ phần độ lồi cho −6,775%; quên hệ số ½ cho −5,950%.',
     'Ước lượng thay đổi giá trái phiếu bằng duration và convexity')
w10 = (5 - 2) / (10 - 2)
chk(w10 * 100, 37.5)
addn('QU', T, 3,
     'Quỹ cần phòng vệ (immunization) một khoản nợ phải trả có giá trị hiện tại 100 tỷ đồng và duration 5 năm, bằng cách kết hợp trái phiếu zero-coupon kỳ hạn 2 năm và trái phiếu zero-coupon kỳ hạn 10 năm. Số tiền cần đầu tư vào trái phiếu kỳ hạn 10 năm là bao nhiêu?',
     [w10 * 100, 30.0, 50.0, 62.5], lambda v: vn(v, 1) + ' tỷ đồng',
     f'Duration zero-coupon bằng kỳ hạn. Cần w × 10 + (1 − w) × 2 = 5 → w = 3/8 = {pc(w10,1)} → đầu tư {vn(w10*100,1)} tỷ vào trái phiếu 10 năm và 62,5 tỷ vào trái phiếu 2 năm (PV tài sản = PV nợ = 100 tỷ).',
     'Phòng vệ danh mục: duration tài sản = duration nợ, PV tài sản ≥ PV nợ')
add('QU', T, 2,
    'Nguyên lý cơ bản của chiến lược phòng vệ (immunization) đối với danh mục trái phiếu là gì?',
    ['Đặt duration danh mục bằng thời hạn đầu tư (nghĩa vụ) để rủi ro giá và rủi ro tái đầu tư bù trừ nhau',
     'Đặt kỳ hạn bình quân của danh mục bằng kỳ hạn nghĩa vụ để loại bỏ rủi ro tín dụng',
     'Chỉ nắm giữ trái phiếu lãi suất thả nổi để loại bỏ hoàn toàn rủi ro lãi suất',
     'Tối đa hóa duration danh mục để hưởng lợi khi lãi suất thị trường giảm'],
    'Khi lãi suất tăng, giá trái phiếu giảm nhưng thu nhập tái đầu tư coupon tăng (và ngược lại). Khi duration bằng thời hạn đầu tư, hai tác động xấp xỉ triệt tiêu, khóa được lợi suất mục tiêu; cần tái cân bằng định kỳ vì duration thay đổi theo thời gian và lãi suất.',
    'Chiến lược phòng vệ (immunization)')
add('QU', T, 1,
    'Danh mục trái phiếu theo cấu trúc "quả tạ" (barbell) là danh mục:',
    ['Tập trung vào trái phiếu kỳ hạn ngắn và kỳ hạn dài, rất ít trái phiếu trung hạn',
     'Tập trung gần như toàn bộ vào trái phiếu có kỳ hạn quanh một mốc thời gian mục tiêu',
     'Phân bổ đều giá trị cho các kỳ hạn liên tiếp nhau như các bậc thang',
     'Chỉ gồm trái phiếu chính phủ kỳ hạn dài để tối đa hóa duration'],
    'Barbell: hai đầu ngắn – dài. Bullet: tập trung quanh một kỳ hạn mục tiêu. Ladder (bậc thang): phân bổ đều các kỳ hạn.',
    'Cấu trúc danh mục trái phiếu: bullet, barbell, ladder')

T = 'Một số sản phẩm đầu tư thay thế'
add('QU', T, 1,
    'Cơ cấu phí "2 và 20" phổ biến của các quỹ phòng hộ (hedge fund) bao gồm:',
    ['Phí quản lý 2%/năm trên giá trị tài sản quản lý và phí thưởng hiệu quả 20% trên lợi nhuận',
     'Phí phát hành 2% trên số tiền góp vốn và phí mua lại 20% trên giá trị mua lại',
     'Phí quản lý 20%/năm trên tài sản và phí thưởng 2% trên lợi nhuận vượt ngưỡng',
     'Phí lưu ký 2%/năm và phí giao dịch 20% trên giá trị mỗi giao dịch'],
    'Quỹ phòng hộ thường thu phí quản lý khoảng 2% tài sản quản lý và phí thưởng hiệu quả khoảng 20% lợi nhuận (có thể kèm ngưỡng lợi suất tối thiểu và mức đỉnh – high-water mark).',
    'Quỹ phòng hộ – cơ cấu phí')
add('QU', T, 1,
    'Đặc điểm chung nào sau đây thường gắn với các tài sản đầu tư thay thế (quỹ phòng hộ, quỹ đầu tư tư nhân, bất động sản, hàng hóa)?',
    ['Thanh khoản thấp, khó định giá và tương quan tương đối thấp với cổ phiếu, trái phiếu truyền thống',
     'Thanh khoản cao, được định giá liên tục theo giá khớp lệnh trên sở giao dịch',
     'Lợi suất được bảo đảm cố định và không chịu rủi ro thị trường',
     'Chi phí quản lý thấp hơn quỹ chỉ số và công bố thông tin danh mục hằng ngày'],
    'Tài sản thay thế bổ sung lợi ích đa dạng hóa nhờ tương quan thấp, nhưng thường kém thanh khoản, khó định giá (dựa vào thẩm định), phí cao và ít minh bạch hơn tài sản truyền thống.',
    'Đặc điểm của tài sản đầu tư thay thế')
add('QU', T, 2,
    'Công ty X có doanh thu từ việc sở hữu và kinh doanh bất động sản chiếm 60% tổng doanh thu trên báo cáo tài chính năm gần nhất. Theo định nghĩa quỹ đầu tư bất động sản tại Luật Chứng khoán, nhận định nào sau đây đúng?',
    ['X chưa được coi là tổ chức kinh doanh bất động sản theo định nghĩa này vì tỷ lệ yêu cầu tối thiểu là 65%',
     'X được coi là tổ chức kinh doanh bất động sản vì tỷ lệ yêu cầu tối thiểu là 50%',
     'X được coi là tổ chức kinh doanh bất động sản vì tỷ lệ yêu cầu tối thiểu là 51%',
     'Định nghĩa không đặt ngưỡng doanh thu mà chỉ xét ngành nghề đăng ký kinh doanh'],
    'Quỹ đầu tư bất động sản đầu tư chủ yếu vào bất động sản và chứng khoán của tổ chức kinh doanh bất động sản có doanh thu từ sở hữu, kinh doanh bất động sản tối thiểu 65% tổng doanh thu năm gần nhất; 60% chưa đạt ngưỡng.',
    f'Khoản 43 Điều 4 {LAWB}',
    'Quỹ đầu tư bất động sản là quỹ đầu tư chứng khoán được đầu tư chủ yếu vào bất động sản và chứng khoán của tổ chức phát hành là tổ chức kinh doanh bất động sản có doanh thu từ việc sở hữu và kinh doanh bất động sản tối thiểu là 65% tổng doanh thu',
    LAW)
g = 18; mf = 2; inc = 0.2 * (g - mf)
net = (g - mf - inc) / 100
chk(net, 0.128)
addn('QU', T, 3,
     'Quỹ phòng hộ có tài sản đầu kỳ 100 tỷ đồng, lợi suất gộp trong năm 18%. Phí quản lý 2% tính trên tài sản đầu kỳ; phí thưởng hiệu quả 20% tính trên lợi nhuận sau khi trừ phí quản lý (không có ngưỡng lợi suất tối thiểu). Lợi suất ròng của nhà đầu tư là bao nhiêu?',
     [net, (g - mf - 0.2 * g) / 100, (g - 0.2 * g) / 100, (g - mf) / 100], lambda v: pc(v, 1),
     f'Lợi nhuận gộp 18 tỷ; phí quản lý 2 tỷ → còn 16 tỷ; phí thưởng = 20% × 16 = {vn(inc,1)} tỷ; lợi nhuận ròng = {vn(g-mf-inc,1)} tỷ → {pc(net)}. Tính phí thưởng trên lợi nhuận gộp cho 12,4%; bỏ phí quản lý cho 14,4%; bỏ phí thưởng cho 16,0%.',
     'Tính phí quản lý và phí thưởng hiệu quả của quỹ phòng hộ')

T = 'Quản lý rủi ro danh mục đầu tư'
var1 = 200 * 0.015 * 1.65
var10 = var1 * math.sqrt(10)
chk(var10, 15.653)
addn('QU', T, 3,
     'Danh mục trị giá 200 tỷ đồng có độ lệch chuẩn lợi suất ngày 1,5%, giả định lợi suất phân phối chuẩn với kỳ vọng bằng 0 và các ngày độc lập. Với z = 1,65 (độ tin cậy 95%, một phía), VaR 10 ngày của danh mục xấp xỉ bao nhiêu?',
     [var10, var1, var1 * 10, 200 * 0.015 * math.sqrt(10)], lambda v: vn(v, 2) + ' tỷ đồng',
     f'VaR 1 ngày = 200 × 1,5% × 1,65 = {vn(var1,2)} tỷ; VaR 10 ngày = {vn(var1,2)} × √10 ≈ {vn(var10,2)} tỷ đồng. Nhân 10 thay vì √10 cho {vn(var1*10,2)}; quên z cho {vn(200*0.015*math.sqrt(10),2)}.',
     'VaR tham số: VaR = z·σ·V; VaR(T ngày) = VaR(1 ngày)·√T')
add('QU', T, 2,
    'Một danh mục có VaR 1 ngày ở độ tin cậy 95% là 5 tỷ đồng. Cách hiểu nào sau đây đúng?',
    ['Trong điều kiện thị trường bình thường, có 5% khả năng tổn thất trong 1 ngày vượt quá 5 tỷ đồng',
     'Tổn thất tối đa có thể xảy ra trong 1 ngày là 5 tỷ đồng trong mọi trường hợp',
     'Có 95% khả năng danh mục bị lỗ đúng 5 tỷ đồng trong 1 ngày',
     'Tổn thất bình quân trong 5% số ngày xấu nhất là 5 tỷ đồng'],
    'VaR là ngưỡng tổn thất mà xác suất bị vượt qua bằng (1 − độ tin cậy); VaR không phải tổn thất tối đa tuyệt đối. Tổn thất bình quân trong vùng đuôi là CVaR (expected shortfall).',
    'Khái niệm giá trị chịu rủi ro (VaR)')
bt = 0.8 * 0.30 / 0.20
chk(bt, 1.2)
addn('QU', T, 3,
     'Cổ phiếu Q có độ lệch chuẩn lợi suất 30%, danh mục thị trường có độ lệch chuẩn 20%, hệ số tương quan giữa Q và thị trường là 0,8. Hệ số beta của Q là bao nhiêu?',
     [bt, 0.30 / 0.20, 0.8 * 0.20 / 0.30, 0.8 ** 2 * 1.5], lambda v: vn(v, 2),
     f'β = Cov(Q, M)/σM² = ρ × σQ/σM = 0,8 × 30%/20% = {vn(bt,2)}. Bỏ qua tương quan cho 1,50; đảo tỷ số độ lệch chuẩn cho 0,53; dùng ρ² cho 0,96.',
     'β = ρiM·σi/σM')
add('QU', T, 1,
    'Loại rủi ro nào có thể giảm đáng kể (tiến dần về 0) khi tăng số lượng chứng khoán ít tương quan với nhau trong danh mục?',
    ['Rủi ro phi hệ thống (rủi ro đặc thù của từng doanh nghiệp)',
     'Rủi ro hệ thống (rủi ro thị trường)',
     'Rủi ro lãi suất chung của toàn nền kinh tế',
     'Rủi ro lạm phát và tỷ giá ở cấp độ vĩ mô'],
    'Đa dạng hóa loại bỏ được rủi ro phi hệ thống; rủi ro hệ thống (lãi suất, lạm phát, tỷ giá, chu kỳ kinh tế) tác động tới mọi chứng khoán nên không thể loại bỏ bằng đa dạng hóa.',
    'Rủi ro hệ thống và rủi ro phi hệ thống')
ps = [0.3, 0.5, 0.2]; rs = [25, 10, -15]
er = sum(p * r for p, r in zip(ps, rs))
sd = math.sqrt(sum(p * (r - er) ** 2 for p, r in zip(ps, rs))) / 100
m3 = sum(rs) / 3
sd_eq = math.sqrt(sum((r - m3) ** 2 for r in rs) / 3) / 100
sd_raw = math.sqrt(sum(p * r * r for p, r in zip(ps, rs))) / 100
chk(sd, 0.13865)
addn('QU', T, 3,
     'Lợi suất một năm của cổ phiếu T theo các kịch bản: tăng trưởng (xác suất 30%) +25%; bình thường (xác suất 50%) +10%; suy thoái (xác suất 20%) −15%. Độ lệch chuẩn lợi suất của T là bao nhiêu?',
     [sd, er / 100, sd_eq, sd_raw], lambda v: pc(v, 2),
     f'E(R) = 0,3 × 25 + 0,5 × 10 + 0,2 × (−15) = {vn(er,1)}%. σ² = 0,3 × 15,5² + 0,5 × 0,5² + 0,2 × (−24,5)² = 72,075 + 0,125 + 120,05 = 192,25; σ = {pc(sd,2)}. {pc(er/100,2)} là lợi suất kỳ vọng; bỏ qua xác suất cho {pc(sd_eq,2)}; không trừ kỳ vọng cho {pc(sd_raw,2)}.',
     'Lợi suất kỳ vọng và độ lệch chuẩn theo kịch bản xác suất')
add('QU', T, 2,
    'Hạn chế quan trọng nhất của chỉ tiêu VaR khi dùng để quản lý rủi ro danh mục là gì?',
    ['VaR không cho biết mức độ tổn thất khi tổn thất vượt quá ngưỡng VaR (rủi ro đuôi)',
     'VaR chỉ tính được cho danh mục trái phiếu, không áp dụng cho cổ phiếu',
     'VaR không thể quy đổi giữa các khoảng thời gian nắm giữ khác nhau',
     'VaR luôn đánh giá quá cao rủi ro nên không dùng để đặt hạn mức'],
    'VaR chỉ là một ngưỡng phân vị; hai danh mục cùng VaR có thể có tổn thất đuôi rất khác nhau, nên cần bổ sung CVaR và kiểm định sức chịu đựng (stress test). VaR áp dụng cho mọi loại tài sản và có thể quy đổi kỳ hạn (quy tắc căn bậc hai thời gian).',
    'Ưu, nhược điểm của VaR; CVaR và stress test')

T = 'Đánh giá hiệu quả danh mục đầu tư'
shx, shy = (0.15 - 0.04) / 0.20, (0.12 - 0.04) / 0.12
trx, try_ = (15 - 4) / 1.2, (12 - 4) / 0.8
chk(shx, 0.55); chk(shy, 0.6667)
add('QU', T, 3,
    'Lãi suất phi rủi ro 4%. Quỹ X: lợi suất 15%, độ lệch chuẩn 20%, beta 1,2. Quỹ Y: lợi suất 12%, độ lệch chuẩn 12%, beta 0,8. Kết luận nào sau đây đúng theo chỉ số Sharpe?',
    [f'Sharpe X = {vn(shx,2)}; Sharpe Y = {vn(shy,2)}; Y hiệu quả hơn',
     f'Sharpe X = {vn(0.15/0.20,2)}; Sharpe Y = {vn(0.12/0.12,2)}; Y hiệu quả hơn',
     f'Sharpe X = {vn(trx,2)}; Sharpe Y = {vn(try_,2)}; Y hiệu quả hơn',
     f'Sharpe X = {vn(shx,2)}; Sharpe Y = {vn(shy,2)}; X hiệu quả hơn vì lợi suất cao hơn'],
    f'Sharpe = (Rp − rf)/σp. X: (15 − 4)/20 = {vn(shx,2)}; Y: (12 − 4)/12 = {vn(shy,2)} → Y có phần bù trên mỗi đơn vị tổng rủi ro cao hơn. Không trừ rf cho 0,75 và 1,00; {vn(trx,2)} và {vn(try_,2)} là chỉ số Treynor (tính theo điểm %).',
    'Chỉ số Sharpe = (Rp − rf)/σp')
alpha = 0.15 - (0.04 + 1.2 * (0.11 - 0.04))
chk(alpha, 0.026)
addn('QU', T, 3,
     'Quỹ Z đạt lợi suất 15%/năm, beta 1,2. Trong cùng kỳ, lãi suất phi rủi ro 4% và lợi suất danh mục thị trường 11%. Alpha Jensen của quỹ Z là bao nhiêu?',
     [alpha, 0.15 - 0.11, 0.15 - 1.2 * 0.11, 0.15 - 0.04], lambda v: pc(v, 1),
     f'Lợi suất yêu cầu theo CAPM = 4% + 1,2 × (11% − 4%) = 12,4%; α = 15% − 12,4% = {pc(alpha)}. Lấy Rp − Rm cho 4,0%; quên rf cho 1,8%; Rp − rf cho 11,0%.',
     'Alpha Jensen: α = Rp − [rf + βp(Rm − rf)]')
ir = (0.135 - 0.111) / 0.04
chk(ir, 0.6)
addn('QU', T, 2,
     'Danh mục quản lý chủ động có lợi suất 13,5%/năm, độ lệch chuẩn 16%; chỉ số tham chiếu có lợi suất 11,1%/năm; sai lệch theo dõi (tracking error) 4%; lãi suất phi rủi ro 4%. Tỷ số thông tin (information ratio) của danh mục là bao nhiêu?',
     [ir, 0.024 / 0.16, (0.135 - 0.04) / 0.04, 0.135 / 0.04], lambda v: vn(v, 2),
     f'IR = (Rp − Rb)/TE = (13,5% − 11,1%)/4% = {vn(ir,2)}. Chia cho độ lệch chuẩn danh mục cho 0,15; dùng rf thay chỉ số tham chiếu cho 2,38; không trừ lợi suất tham chiếu cho 3,38.',
     'Tỷ số thông tin IR = (Rp − Rb)/Tracking error')
add('QU', T, 2,
    'Khi đánh giá một quỹ chỉ chiếm phần nhỏ trong danh mục tổng thể đã được đa dạng hóa tốt của nhà đầu tư, chỉ số nào phù hợp hơn để so sánh hiệu quả giữa các quỹ?',
    ['Chỉ số Treynor, vì khi đó chỉ rủi ro hệ thống (beta) là rủi ro liên quan',
     'Chỉ số Sharpe, vì đo phần bù trên tổng rủi ro (độ lệch chuẩn)',
     'Lợi suất tuyệt đối, vì rủi ro đã được đa dạng hóa hết',
     'Độ lệch chuẩn của quỹ, vì phản ánh toàn bộ biến động'],
    'Với danh mục tổng thể đã đa dạng hóa, rủi ro phi hệ thống của từng quỹ bị triệt tiêu, nên đo phần bù trên beta (Treynor) phù hợp hơn. Sharpe phù hợp khi quỹ là toàn bộ (hoặc phần lớn) tài sản của nhà đầu tư.',
    'Lựa chọn thước đo hiệu quả: Sharpe và Treynor')

T = 'Thực tiễn công tác quản lý danh mục đầu tư'
nav = (520 - 20) * 1e9 / 40e6
recv = 10000 * nav * (1 - 0.005)
chk(recv, 124375000)
addn('QU', T, 3,
     'Tại ngày định giá, quỹ mở có tổng giá trị tài sản 520 tỷ đồng, tổng nợ phải trả 20 tỷ đồng và 40 triệu chứng chỉ quỹ đang lưu hành. Nhà đầu tư bán lại (yêu cầu quỹ mua lại) 10.000 chứng chỉ quỹ, phí mua lại 0,5% giá trị giao dịch tính theo NAV. Số tiền nhà đầu tư nhận được (chưa tính thuế) là bao nhiêu?',
     [recv, 10000 * nav, 10000 * 13000 * 0.995, 10000 * 13000.0], lambda v: vn(v) + ' đ',
     f'NAV = 520 − 20 = 500 tỷ; NAV/chứng chỉ quỹ = 500 tỷ/40 triệu = {vn(nav)} đ. Tiền nhận = 10.000 × {vn(nav)} × (1 − 0,5%) = {vn(recv)} đ. Dùng tổng tài sản (13.000 đ/ccq) là sai vì NAV phải trừ nợ phải trả.',
     'NAV = Tổng tài sản − Tổng nợ phải trả; giá mua lại = NAV/ccq × (1 − phí mua lại)')
add('QU', T, 1,
    'Theo Thông tư 98/2020/TT-BTC (hợp nhất với Thông tư 136/2025/TT-BTC), công ty quản lý quỹ phải xác định giá trị tài sản ròng của quỹ ETF với tần suất nào?',
    ['Hàng ngày', 'Định kỳ tối thiểu một lần trong một tuần', 'Theo ngày giao dịch, tối thiểu hai lần trong một tháng', 'Định kỳ tối thiểu một lần trong một tháng'],
    'Điều 20 khoản 4: quỹ đóng xác định NAV định kỳ tối thiểu 1 lần/tuần; quỹ mở theo ngày giao dịch, tối thiểu 1 lần/tuần; quỹ ETF hàng ngày (kèm NAV trên một lô chứng chỉ quỹ).',
    'Điểm c khoản 4 Điều 20 Thông tư 98/2020/TT-BTC (VBHN 04/VBHN-BTC năm 2026, hợp nhất Thông tư 136/2025/TT-BTC)',
    'Xác định giá trị tài sản ròng, giá trị tài sản ròng trên một lô chứng chỉ quỹ, giá trị tài sản ròng trên một chứng chỉ quỹ của quỹ ETF hàng ngày.',
    TT98)

# ============================== PS ==============================
M = 100000  # hệ số nhân HĐTL chỉ số VN30: 100.000 đ/điểm
T = 'Tổng quan về chứng khoán phái sinh và thị trường chứng khoán phái sinh'
add('PS', T, 1,
    'Theo Luật Chứng khoán, đặc điểm nào sau đây phân biệt hợp đồng kỳ hạn với hợp đồng tương lai?',
    ['Hợp đồng kỳ hạn là chứng khoán phái sinh giao dịch thỏa thuận, còn hợp đồng tương lai là chứng khoán phái sinh niêm yết',
     'Hợp đồng kỳ hạn xác nhận quyền của người mua, còn hợp đồng tương lai xác nhận nghĩa vụ của người bán',
     'Hợp đồng kỳ hạn không có tài sản cơ sở, còn hợp đồng tương lai có tài sản cơ sở',
     'Hợp đồng kỳ hạn chỉ thanh toán bằng tiền, còn hợp đồng tương lai luôn chuyển giao tài sản'],
    'Luật định nghĩa hợp đồng tương lai là chứng khoán phái sinh niêm yết, còn hợp đồng kỳ hạn là chứng khoán phái sinh giao dịch thỏa thuận; cả hai đều xác nhận cam kết (nghĩa vụ) của các bên đối với tài sản cơ sở. Quyền của người mua – nghĩa vụ của người bán là đặc trưng của hợp đồng quyền chọn.',
    f'Khoản 12, khoản 13 Điều 4 {LAWB}',
    'Hợp đồng kỳ hạn là loại chứng khoán phái sinh giao dịch thỏa thuận, xác nhận cam kết giữa các bên về việc mua hoặc bán số lượng tài sản cơ sở nhất định theo mức giá đã được xác định vào ngày đã xác định trong tương lai.',
    LAW)
add('PS', T, 2,
    'Chức năng nào sau đây KHÔNG phải là chức năng kinh tế chủ yếu của thị trường chứng khoán phái sinh?',
    ['Huy động vốn trực tiếp cho tổ chức phát hành tài sản cơ sở',
     'Phòng ngừa rủi ro biến động giá của tài sản cơ sở',
     'Phát hiện giá, phản ánh kỳ vọng về giá tài sản cơ sở trong tương lai',
     'Tăng thanh khoản và hiệu quả cho thị trường tài sản cơ sở'],
    'Chứng khoán phái sinh là hợp đồng giữa các nhà đầu tư; giao dịch phái sinh không đem lại vốn cho doanh nghiệp phát hành tài sản cơ sở. Các chức năng chính là phòng ngừa rủi ro, phát hiện giá, tăng thanh khoản – hiệu quả thị trường và tạo thêm công cụ đầu tư.',
    'Chức năng của thị trường chứng khoán phái sinh')

T = 'Giới thiệu khung pháp lý cho thị trường chứng khoán phái sinh'
add('PS', T, 2,
    'Theo Nghị định 158/2020/NĐ-CP, công ty quản lý quỹ được đầu tư chứng khoán phái sinh từ nguồn vốn của quỹ đầu tư chứng khoán với mục đích nào?',
    ['Chỉ nhằm mục đích phòng ngừa rủi ro theo quy định của pháp luật về quỹ đầu tư chứng khoán',
     'Đầu tư kiếm lời không hạn chế nếu Điều lệ quỹ cho phép',
     'Thực hiện hoạt động tạo lập thị trường cho hợp đồng tương lai chỉ số',
     'Đầu tư kiếm lời trong hạn mức 20% giá trị tài sản ròng của quỹ'],
    'Công ty quản lý quỹ chỉ được đầu tư chứng khoán phái sinh nhằm phòng ngừa rủi ro cho danh mục ủy thác và cho quỹ/công ty đầu tư chứng khoán; không được đầu tư phái sinh từ vốn của chính mình, vốn vay và vốn huy động khác. Nghị định 306/2025/NĐ-CP không sửa đổi điểm này.',
    'Điểm b khoản 1 Điều 16 Nghị định 158/2020/NĐ-CP (không bị sửa đổi bởi Nghị định 306/2025/NĐ-CP)',
    'công ty quản lý quỹ chỉ được đầu tư chứng khoán phái sinh nhằm mục đích phòng ngừa rủi ro theo quy định của pháp luật về quỹ đầu tư chứng khoán đối với nguồn vốn của quỹ đầu tư chứng khoán, công ty đầu tư chứng khoán.',
    ND158)
add('PS', T, 1,
    'Theo Nghị định 158/2020/NĐ-CP, "giới hạn vị thế" được hiểu là:',
    ['Vị thế tối đa của một chứng khoán phái sinh (hoặc các chứng khoán phái sinh cùng tài sản cơ sở) mà nhà đầu tư được quyền nắm giữ tại một thời điểm',
     'Số lượng chứng khoán phái sinh tối đa có thể đặt trên một lệnh giao dịch',
     'Chênh lệch giữa vị thế mua và vị thế bán đã mở của một chứng khoán phái sinh tại cùng một thời điểm',
     'Mức lỗ tối đa trên vị thế mà nhà đầu tư được chịu trước khi bị đóng vị thế bắt buộc'],
    'Khoản 5 Điều 3 định nghĩa giới hạn vị thế. Số lượng tối đa trên một lệnh là "giới hạn lệnh giao dịch" (khoản 6); chênh lệch vị thế mua – bán là "vị thế ròng" (khoản 4).',
    'Khoản 5 Điều 3 Nghị định 158/2020/NĐ-CP (không bị sửa đổi bởi Nghị định 306/2025/NĐ-CP)',
    'Giới hạn vị thế là vị thế tối đa của một chứng khoán phái sinh, hoặc của chứng khoán phái sinh đó và các chứng khoán phái sinh khác dựa trên cùng một tài sản cơ sở mà nhà đầu tư được quyền nắm giữ tại một thời điểm.',
    ND158)

T = 'Những vấn đề cơ bản về hợp đồng tương lai'
add('PS', T, 1,
    'Đặc điểm nào sau đây có ở hợp đồng tương lai nhưng KHÔNG có ở hợp đồng kỳ hạn thông thường?',
    ['Lãi/lỗ vị thế được xác định và thanh toán hằng ngày qua cơ chế ký quỹ, bù trừ tập trung',
     'Xác định trước giá và khối lượng tài sản cơ sở giao dịch trong tương lai',
     'Có ngày đáo hạn xác định trong tương lai',
     'Có thể được sử dụng để phòng ngừa rủi ro biến động giá'],
    'Hợp đồng tương lai được chuẩn hóa, niêm yết, ký quỹ và thanh toán lãi lỗ hằng ngày (mark-to-market) qua đối tác bù trừ trung tâm. Xác định trước giá, có ngày đáo hạn và dùng để phòng ngừa rủi ro là đặc điểm chung của cả hai loại hợp đồng.',
    'So sánh hợp đồng tương lai và hợp đồng kỳ hạn')
vm2 = (1295.0 - 1312.5) * M * 3
chk(vm2, -5250000)
addn('PS', T, 3,
     'Nhà đầu tư mở 3 vị thế mua HĐTL chỉ số VN30 ở mức 1.300,0 điểm (hệ số nhân 100.000 đ/điểm). Giá thanh toán cuối ngày thứ nhất là 1.312,5 điểm, ngày thứ hai là 1.295,0 điểm. Lãi/lỗ vị thế được thanh toán vào cuối ngày thứ hai là bao nhiêu?',
     [vm2, (1295.0 - 1312.5) * M, (1295.0 - 1300.0) * M * 3, (1312.5 - 1300.0) * M * 3], lambda v: vn(v) + ' đ',
     f'Lãi/lỗ ngày 2 = (1.295,0 − 1.312,5) × 100.000 × 3 = {vn(vm2)} đ (ngày 1 đã thanh toán lãi +3.750.000 đ). Lãi/lỗ lũy kế so với giá mở là −1.500.000 đ; −1.750.000 đ là tính cho 1 hợp đồng.',
     'Thanh toán lãi lỗ hằng ngày (mark-to-market) theo giá thanh toán cuối ngày')
mc = 1250.0 + (20e6 - 15e6) / M
chk(mc, 1300.0)
addn('PS', T, 3,
     'Giả định (phục vụ bài tập): ký quỹ ban đầu 20 triệu đồng/hợp đồng, ký quỹ duy trì 15 triệu đồng/hợp đồng. Nhà đầu tư mở 2 vị thế bán HĐTL chỉ số VN30 ở mức 1.250,0 điểm (hệ số nhân 100.000 đ/điểm), nộp đúng mức ký quỹ ban đầu và không rút tiền. Giá thanh toán cuối ngày vượt quá mức nào thì nhà đầu tư bắt đầu nhận yêu cầu bổ sung ký quỹ?',
     [mc, 1200.0, 1250.0 + 5e6 / (2 * M), 1250.0 + 20e6 / M], lambda v: vn(v, 1) + ' điểm',
     f'Mức lỗ chịu được trên mỗi hợp đồng = 20 − 15 = 5 triệu đồng, tương đương 5.000.000/100.000 = 50 điểm. Vị thế bán lỗ khi giá tăng → giá ngưỡng = 1.250,0 + 50 = {vn(mc,1)} điểm. 1.200,0 là nhầm chiều; 1.275,0 là chia nhầm cho 2 hợp đồng; 1.450,0 là dùng toàn bộ ký quỹ ban đầu.',
     'Ký quỹ ban đầu, ký quỹ duy trì và yêu cầu bổ sung ký quỹ')

T = 'Định giá và sử dụng hợp đồng tương lai'
F = 1250 * (1 + 0.06 * 73 / 365) - 3.2
chk(F, 1261.8)
addn('PS', T, 3,
     'Chỉ số VN30 đang ở mức 1.250,0 điểm. HĐTL chỉ số VN30 còn 73 ngày đến đáo hạn; lãi suất phi rủi ro 6%/năm (lãi đơn, cơ sở 365 ngày); cổ tức của các cổ phiếu trong rổ dự kiến nhận trước đáo hạn quy đổi tương đương 3,2 điểm chỉ số (bỏ qua lãi trên cổ tức). Giá lý thuyết của HĐTL theo mô hình chi phí lưu giữ là bao nhiêu?',
     [F, 1250 * 1.012, 1250 - 3.2, 1250 * 1.06 - 3.2], lambda v: vn(v, 1) + ' điểm',
     f'F = S × (1 + r × t/365) − D = 1.250 × (1 + 6% × 73/365) − 3,2 = 1.250 × 1,012 − 3,2 = {vn(F,1)} điểm. Bỏ cổ tức cho 1.265,0; bỏ chi phí vốn cho 1.246,8; không quy đổi lãi suất theo thời gian cho 1.321,8.',
     'Mô hình chi phí lưu giữ (cost of carry): F = S(1 + rt) − D')
Ff = 1200 * (1 + 0.06 * 90 / 365)
gainA = (1230 - Ff) * M
chk(Ff, 1217.753); chk(gainA, 1224658, 1e-4)
add('PS', T, 3,
    'Chỉ số VN30 ở mức 1.200,0 điểm; HĐTL chỉ số VN30 còn 90 ngày đến đáo hạn đang giao dịch ở 1.230,0 điểm. Lãi suất phi rủi ro 6%/năm (lãi đơn, cơ sở 365 ngày), bỏ qua cổ tức và chi phí giao dịch, giả định có thể giao dịch rổ cổ phiếu mô phỏng chính xác chỉ số (hệ số nhân 100.000 đ/điểm). Chiến lược kinh doanh chênh lệch giá và lợi nhuận tại đáo hạn cho mỗi hợp đồng là:',
    [f'Mua rổ VN30 bằng vốn vay, bán HĐTL; lợi nhuận ≈ {vn(gainA/1e6,2)} triệu đồng/hợp đồng',
     f'Bán khống rổ VN30, mua HĐTL; lợi nhuận ≈ {vn(gainA/1e6,2)} triệu đồng/hợp đồng',
     f'Mua rổ VN30 bằng vốn vay, bán HĐTL; lợi nhuận ≈ {vn(30*M/1e6,2)} triệu đồng/hợp đồng',
     'Không có cơ hội chênh lệch giá vì giá HĐTL cao hơn giá giao ngay là bình thường'],
    f'Giá lý thuyết = 1.200 × (1 + 6% × 90/365) = {vn(Ff,2)} điểm < 1.230,0 → HĐTL bị định giá cao. Kinh doanh chênh lệch thuận (cash and carry): vay tiền mua rổ, bán HĐTL; lợi nhuận = (1.230,0 − {vn(Ff,2)}) × 100.000 ≈ {vn(gainA)} đ/hợp đồng. 3,00 triệu là quên chi phí vốn.',
    'Kinh doanh chênh lệch giá (cash and carry) khi F thị trường > F lý thuyết')
nadj = (0.5 - 1.2) * 15e9 / (1250 * M)
chk(nadj, -84)
add('PS', T, 3,
    'Quỹ nắm giữ danh mục cổ phiếu trị giá 15 tỷ đồng, beta 1,2 so với chỉ số VN30, muốn giảm beta danh mục xuống 0,5. HĐTL chỉ số VN30 đang ở mức 1.250,0 điểm, hệ số nhân 100.000 đ/điểm. Quỹ cần thực hiện giao dịch nào?',
    [f'Bán {vn(-nadj)} hợp đồng', f'Bán {vn(1.2*15e9/(1250*M))} hợp đồng', f'Bán {vn(0.5*15e9/(1250*M))} hợp đồng', f'Mua {vn(-nadj)} hợp đồng'],
    f'Giá trị 1 hợp đồng = 1.250 × 100.000 = 125 triệu đồng. N = (β mục tiêu − β hiện tại) × V/(F × hệ số nhân) = (0,5 − 1,2) × 15 tỷ/125 triệu = {vn(nadj)} → bán {vn(-nadj)} hợp đồng. Bán 144 hợp đồng là phòng vệ toàn bộ (β về 0); 60 hợp đồng là dùng nhầm β mục tiêu.',
    'Điều chỉnh beta danh mục bằng HĐTL chỉ số: N = (β* − β)·V/(F·hệ số nhân)')
add('PS', T, 2,
    'Nhà đầu tư phòng vệ danh mục cổ phiếu bằng HĐTL chỉ số VN30 và dự kiến đóng vị thế trước ngày đáo hạn. Rủi ro cơ sở (basis risk) của chiến lược này phát sinh chủ yếu do:',
    ['Chênh lệch giữa giá giao ngay và giá HĐTL tại thời điểm đóng vị thế biến động không như dự kiến',
     'Chỉ số VN30 có thể giảm mạnh trong thời gian phòng vệ',
     'Lãi lỗ vị thế HĐTL phải thanh toán hằng ngày qua tài khoản ký quỹ',
     'Bên đối ứng của HĐTL có thể mất khả năng thanh toán'],
    'Cơ sở = giá giao ngay − giá tương lai, hội tụ về 0 khi đáo hạn; nếu đóng vị thế trước đáo hạn (hoặc danh mục không trùng rổ VN30) thì cơ sở tại thời điểm đóng là bất định nên phòng vệ không hoàn hảo. Rủi ro đối tác được hạn chế nhờ cơ chế đối tác bù trừ trung tâm.',
    'Cơ sở (basis) và rủi ro cơ sở khi phòng vệ bằng HĐTL')

T = 'Những vấn đề cơ bản về hợp đồng quyền chọn'
add('PS', T, 1,
    'Một quyền chọn bán (put) ở trạng thái cao giá (in-the-money) khi:',
    ['Giá tài sản cơ sở thấp hơn giá thực hiện', 'Giá tài sản cơ sở cao hơn giá thực hiện',
     'Giá tài sản cơ sở bằng giá thực hiện', 'Phí quyền chọn cao hơn giá trị nội tại'],
    'Giá trị nội tại của quyền chọn bán = max(K − S, 0) > 0 khi S < K (cao giá). S > K là kiệt giá với quyền chọn bán; S = K là ngang giá.',
    'Trạng thái quyền chọn: cao giá, ngang giá, kiệt giá')
add('PS', T, 1,
    'Theo Luật Chứng khoán, chứng quyền có bảo đảm là loại chứng khoán có tài sản bảo đảm do tổ chức nào phát hành?',
    ['Công ty chứng khoán', 'Tổ chức phát hành chứng khoán cơ sở',
     'Công ty quản lý quỹ', 'Sở giao dịch chứng khoán'],
    'Chứng quyền có bảo đảm do công ty chứng khoán phát hành, cho phép người sở hữu quyền mua (chứng quyền mua) hoặc quyền bán (chứng quyền bán) chứng khoán cơ sở, hoặc nhận khoản tiền chênh lệch tại thời điểm thực hiện.',
    f'Khoản 6 Điều 4 {LAWB}',
    'Chứng quyền có bảo đảm là loại chứng khoán có tài sản bảo đảm do công ty chứng khoán phát hành, cho phép người sở hữu được quyền mua (chứng quyền mua) hoặc được quyền bán (chứng quyền bán) chứng khoán cơ sở',
    LAW)
pay = (36500 - 30000) / 5
cwp = (pay - 900) * 10000
chk(cwp, 4000000)
addn('PS', T, 3,
     'Nhà đầu tư mua 10.000 chứng quyền mua (kiểu châu Âu, thanh toán bằng tiền) với giá 900 đ/chứng quyền; tỷ lệ chuyển đổi 5:1 (5 chứng quyền tương ứng 1 cổ phiếu cơ sở), giá thực hiện 30.000 đ. Giá thanh toán tại ngày đáo hạn là 36.500 đ. Lợi nhuận của nhà đầu tư (bỏ qua thuế, phí) là bao nhiêu?',
     [cwp, (6500 - 900) * 10000, pay * 10000, (6500 - 900) / 5 * 10000], lambda v: vn(v) + ' đ',
     f'Khoản thanh toán mỗi chứng quyền = (36.500 − 30.000)/5 = {vn(pay)} đ; lợi nhuận = ({vn(pay)} − 900) × 10.000 = {vn(cwp)} đ. Quên tỷ lệ chuyển đổi cho 56.000.000 đ; chưa trừ giá mua cho 13.000.000 đ; chia cả giá mua cho tỷ lệ chuyển đổi cho 11.200.000 đ.',
     'Khoản thanh toán chứng quyền mua = (Giá thanh toán − Giá thực hiện)/Tỷ lệ chuyển đổi')

T = 'Định giá và sử dụng hợp đồng quyền chọn'
pvk = 50000 / 1.08 ** 0.5
put = 3000 + pvk - 48000
chk(put, 3112.52)
addn('PS', T, 3,
     'Cổ phiếu XYZ giá 48.000 đ. Quyền chọn mua kiểu châu Âu trên XYZ, giá thực hiện 50.000 đ, kỳ hạn 6 tháng, có giá 3.000 đ. Lãi suất phi rủi ro 8%/năm (chiết khấu theo lãi kép năm), cổ phiếu không trả cổ tức. Theo ngang giá quyền chọn mua – bán, giá quyền chọn bán kiểu châu Âu cùng giá thực hiện và kỳ hạn xấp xỉ:',
     [round(put), round(3000 - pvk + 48000), 3000 + 50000 - 48000, 3000 - 2000], lambda v: vn(v) + ' đ',
     f'P = C + K/(1 + r)^T − S = 3.000 + 50.000/1,08^0,5 − 48.000 = 3.000 + {vn(pvk,2)} − 48.000 ≈ {vn(round(put))} đ. Không chiết khấu K cho 5.000 đ; đảo dấu cho 2.887 đ; lấy C − (K − S) cho 1.000 đ.',
     'Ngang giá quyền chọn mua – bán: C + K/(1+r)^T = P + S')
bull = (43000 - 40000) - (2500 - 1000)
chk(bull, 1500)
addn('PS', T, 3,
     'Nhà đầu tư mua quyền chọn mua giá thực hiện 40.000 đ (phí 2.500 đ) và bán quyền chọn mua giá thực hiện 45.000 đ (phí 1.000 đ), cùng tài sản cơ sở và cùng ngày đáo hạn. Khi đáo hạn, giá tài sản cơ sở là 43.000 đ. Lợi nhuận của chiến lược tính trên một đơn vị tài sản cơ sở là bao nhiêu?',
     [bull, 3000, 3000 - 3500, 3000 + 2500 - 1000], lambda v: vn(v) + ' đ',
     f'Chênh lệch giá mua (bull call spread): thu từ quyền mua 40.000 = 3.000 đ; quyền mua 45.000 không được thực hiện. Chi phí ròng = 2.500 − 1.000 = 1.500 đ. Lợi nhuận = 3.000 − 1.500 = {vn(bull)} đ. Cộng cả hai phí như chi phí cho −500 đ; quên phí cho 3.000 đ; đảo dấu phí ròng cho 4.500 đ.',
     'Chiến lược chênh lệch giá tăng (bull call spread)')
add('PS', T, 2,
    'Khi các yếu tố khác không đổi, nếu độ biến động (volatility) kỳ vọng của tài sản cơ sở tăng lên thì giá quyền chọn mua và quyền chọn bán kiểu châu Âu thay đổi như thế nào?',
    ['Quyền chọn mua và quyền chọn bán đều tăng giá', 'Quyền chọn mua tăng giá, quyền chọn bán giảm giá',
     'Quyền chọn mua giảm giá, quyền chọn bán tăng giá', 'Hai loại quyền chọn đều giảm giá do rủi ro cao hơn'],
    'Vega của vị thế mua quyền chọn (mua hoặc bán) đều dương: biến động cao làm tăng khả năng quyền chọn kết thúc ở trạng thái cao giá, trong khi khoản lỗ của người nắm giữ bị giới hạn ở phí quyền chọn.',
    'Các hệ số nhạy (Greeks): vega')
dsh = 2_000_000 / 4 * 0.55
chk(dsh, 275000)
addn('PS', T, 3,
     'CTCK phát hành 2.000.000 chứng quyền mua, tỷ lệ chuyển đổi 4:1 (4 chứng quyền tương ứng 1 cổ phiếu cơ sở). Delta của chứng quyền tính theo 1 cổ phiếu cơ sở là 0,55. Để phòng ngừa rủi ro delta cho vị thế phát hành, CTCK cần nắm giữ bao nhiêu cổ phiếu cơ sở?',
     [dsh, 2_000_000 * 0.55, 2_000_000 / 4, dsh / 4], lambda v: vn(v) + ' cổ phiếu',
     f'Số cổ phiếu cơ sở tương ứng = 2.000.000/4 = 500.000; số cổ phiếu phòng ngừa = 500.000 × 0,55 = {vn(dsh)} cổ phiếu (mua vào vì CTCK đang ở vị thế bán quyền chọn mua). Quên tỷ lệ chuyển đổi cho 1.100.000; bỏ qua delta cho 500.000.',
     'Phòng ngừa delta (delta hedging)')

T = 'Sở Giao dịch CKPS và giao dịch CKPS trên sở giao dịch'
im = 1280.5 * M * 0.17
chk(im, 21768500)
addn('PS', T, 2,
     'HĐTL chỉ số VN30 đang giao dịch ở mức 1.280,5 điểm, hệ số nhân 100.000 đ/điểm. Giả định tỷ lệ ký quỹ ban đầu là 17% giá trị hợp đồng. Giá trị ký quỹ ban đầu cho 1 hợp đồng là bao nhiêu?',
     [im, 1280.5 * M, 1280.5 * 10000 * 0.17, im * 10], lambda v: vn(v) + ' đ',
     f'Giá trị hợp đồng = 1.280,5 × 100.000 = 128.050.000 đ; ký quỹ ban đầu = 17% × 128.050.000 = {vn(im)} đ. Dùng nhầm hệ số nhân 10.000 cho 2.176.850 đ.',
     'Giá trị hợp đồng = Giá × Hệ số nhân; Ký quỹ = Giá trị hợp đồng × Tỷ lệ ký quỹ')
add('PS', T, 1,
    'HĐTL chỉ số VN30 giao dịch trên thị trường chứng khoán phái sinh Việt Nam được thanh toán khi đáo hạn theo phương thức nào?',
    ['Thanh toán bằng tiền, dựa trên chênh lệch giữa giá hợp đồng và giá thanh toán cuối cùng',
     'Chuyển giao vật chất toàn bộ rổ 30 cổ phiếu thành phần của chỉ số VN30',
     'Chuyển giao chứng chỉ quỹ ETF mô phỏng chỉ số VN30',
     'Người mua được lựa chọn giữa nhận tiền hoặc nhận rổ cổ phiếu'],
    'Tài sản cơ sở là chỉ số nên không thể chuyển giao vật chất; HĐTL chỉ số VN30 thanh toán bằng tiền theo giá thanh toán cuối cùng (giá đóng cửa của chỉ số cơ sở tại ngày giao dịch cuối cùng).',
    'Đặc tả HĐTL chỉ số VN30 – phương thức thanh toán')
pl = (1318.7 - 1305.2) * M * 5 - 20000 * 5 * 2
chk(pl, 6550000)
addn('PS', T, 3,
     'Nhà đầu tư mở 5 vị thế mua HĐTL chỉ số VN30 ở mức 1.305,2 điểm và đóng toàn bộ vị thế ở 1.318,7 điểm (hệ số nhân 100.000 đ/điểm). Giả định tổng phí là 20.000 đ/hợp đồng cho mỗi lượt mở hoặc đóng vị thế; bỏ qua thuế. Lợi nhuận ròng của nhà đầu tư là bao nhiêu?',
     [pl, (1318.7 - 1305.2) * M * 5, (1318.7 - 1305.2) * M * 5 - 20000 * 5, (1318.7 - 1305.2) * M - 40000], lambda v: vn(v) + ' đ',
     f'Lãi gộp = (1.318,7 − 1.305,2) × 100.000 × 5 = 6.750.000 đ; phí = 20.000 × 5 × 2 lượt = 200.000 đ; lãi ròng = {vn(pl)} đ. Chỉ tính phí một chiều cho 6.650.000 đ; 1.310.000 đ là lãi ròng của 1 hợp đồng.',
     'Lãi lỗ khi đóng vị thế HĐTL = (Giá đóng − Giá mở) × Hệ số nhân × Số hợp đồng − Phí')

T = 'Một số công cụ phái sinh giao dịch trên thị trường OTC'
net2 = (0.068 - 0.060) * 100 * 0.5
chk(net2, 0.4)
add('PS', T, 2,
    'Hợp đồng hoán đổi lãi suất danh nghĩa 100 tỷ đồng, kỳ hạn 1 năm, thanh toán 6 tháng/lần: bên A trả lãi cố định 6,0%/năm, bên B trả lãi thả nổi theo lãi suất tham chiếu xác định vào đầu mỗi kỳ, các khoản lãi được bù trừ ròng. Lãi suất tham chiếu đầu kỳ 1 là 5,4%/năm, đầu kỳ 2 là 6,8%/năm. Khoản thanh toán ròng vào cuối kỳ 2 là:',
    ['Bên A nhận ròng 0,4 tỷ đồng từ bên B', 'Bên A trả ròng 0,4 tỷ đồng cho bên B',
     'Bên A nhận ròng 0,8 tỷ đồng từ bên B', 'Bên A trả ròng 0,3 tỷ đồng cho bên B'],
    f'Lãi thả nổi kỳ 2 xác định đầu kỳ = 6,8%. Bên B trả 100 × 6,8% × 0,5 = 3,4 tỷ; bên A trả 100 × 6,0% × 0,5 = 3,0 tỷ → bên A nhận ròng {vn(net2,1)} tỷ đồng. Quên nhân 0,5 năm cho 0,8 tỷ; dùng lãi suất đầu kỳ 1 cho bên A trả ròng 0,3 tỷ.',
    'Hoán đổi lãi suất (cố định – thả nổi), thanh toán ròng')
add('PS', T, 2,
    'So với hợp đồng hoán đổi lãi suất thông thường (plain vanilla), điểm khác biệt cơ bản của hợp đồng hoán đổi tiền tệ là:',
    ['Thường có trao đổi số tiền gốc bằng hai đồng tiền khác nhau vào đầu và cuối kỳ hạn',
     'Chỉ trao đổi phần chênh lệch lãi tính trên cùng một số tiền gốc danh nghĩa',
     'Bắt buộc niêm yết và giao dịch tập trung trên Sở giao dịch chứng khoán',
     'Không phát sinh rủi ro tỷ giá cho các bên tham gia'],
    'Hoán đổi tiền tệ trao đổi gốc và lãi bằng hai đồng tiền (thường trao đổi gốc đầu và cuối kỳ), nên các bên chịu rủi ro tỷ giá. Hoán đổi lãi suất thông thường cùng một đồng tiền, không trao đổi gốc, chỉ thanh toán ròng chênh lệch lãi. Cả hai chủ yếu giao dịch OTC.',
    'Hoán đổi tiền tệ và hoán đổi lãi suất')

T = 'Hoạt động bù trừ và thanh toán trong giao dịch CKPS'
add('PS', T, 1,
    'Theo Nghị định 158/2020/NĐ-CP, trong cơ chế đối tác bù trừ trung tâm, tổ chức nào thông qua hoạt động thế vị trở thành một đối tác của giao dịch chứng khoán phái sinh?',
    ['Tổng công ty lưu ký và bù trừ chứng khoán Việt Nam', 'Sở giao dịch chứng khoán tổ chức thị trường phái sinh',
     'Ngân hàng thanh toán do các thành viên bù trừ lựa chọn', 'Ủy ban Chứng khoán Nhà nước'],
    'Trong cơ chế đối tác bù trừ trung tâm, VSDC thông qua thế vị trở thành một đối tác của giao dịch, thành viên bù trừ là đối tác còn lại; nhờ đó rủi ro đối tác giữa các nhà đầu tư được loại bỏ.',
    'Khoản 19 Điều 3 Nghị định 158/2020/NĐ-CP (không bị sửa đổi bởi Nghị định 306/2025/NĐ-CP)',
    'Tổng công ty lưu ký và bù trừ chứng khoán Việt Nam thông qua hoạt động thế vị trở thành một đối tác của giao dịch chứng khoán phái sinh, thành viên bù trừ là đối tác còn lại của giao dịch.',
    ND158)
add('PS', T, 2,
    'Theo Nghị định 158/2020/NĐ-CP, biện pháp nào sau đây thuộc cơ chế phòng ngừa rủi ro mà Tổng công ty lưu ký và bù trừ chứng khoán Việt Nam được áp dụng?',
    ['Yêu cầu thành viên bù trừ đóng góp vào quỹ bù trừ',
     'Bảo đảm mức lợi nhuận tối thiểu cho nhà đầu tư có vị thế mở',
     'Cho thành viên bù trừ vay vốn để thanh toán lỗ vị thế',
     'Quyết định hủy niêm yết hợp đồng tương lai khi đáo hạn'],
    'Điều 35: VSDC được xác định, điều chỉnh mức ký quỹ; yêu cầu thành viên bù trừ đóng góp quỹ bù trừ; xác định giới hạn vị thế; đóng vị thế của bên mất khả năng thanh toán; sử dụng quỹ bù trừ. Hủy niêm yết chứng khoán phái sinh thuộc thẩm quyền Sở giao dịch chứng khoán (Điều 15).',
    'Điểm b khoản 1 Điều 35 Nghị định 158/2020/NĐ-CP (không bị sửa đổi bởi Nghị định 306/2025/NĐ-CP)',
    'b) Yêu cầu thành viên bù trừ đóng góp vào quỹ bù trừ;',
    ND158)

# ====================== sắp xếp đáp án và xuất ======================
assert len(Q) == 95, len(Q)
cnt = [0, 0, 0, 0]
pos = [None] * len(Q)
for i, x in enumerate(Q):
    if x['num'] is not None:
        order = sorted(range(4), key=lambda k: x['num'][k])
        x['o'] = [x['o'][k] for k in order]
        pos[i] = order.index(0)
        cnt[pos[i]] += 1
target = [24, 24, 24, 23]
need = [t - c for t, c in zip(target, cnt)]
assert min(need) >= 0, (cnt, need)
free = [i for i in range(len(Q)) if pos[i] is None]
for seed in range(2026, 3000):  # chọn seed đầu tiên không tạo chuỗi >= 4 đáp án trùng vị trí liên tiếp
    pool = [p for p in range(4) for _ in range(need[p])]
    random.Random(seed).shuffle(pool)
    trial = pos[:]
    for i, p in zip(free, pool):
        trial[i] = p
    if all(len(set(trial[k:k + 4])) > 1 for k in range(len(trial) - 3)):
        break
for i in free:
    o = Q[i]['o'][1:]
    o.insert(trial[i], Q[i]['o'][0])
    Q[i]['o'] = o
pos = trial

out = []
for i, x in enumerate(Q):
    out.append({'id': f'C3-{i+1:03d}', 'part': 'CM', 'subject': x['sub'], 'topic': x['topic'],
                'level': x['lv'], 'q': x['q'], 'o': x['o'], 'a': pos[i], 'e': x['e'],
                'basis': x['basis'], 'quote': x['quote'], 'src': x['src'], 'as_of': '2026-11',
                **({'_num': True} if x['num'] is not None else {})})
# _num chỉ dùng cho validate rồi bị loại khỏi file xuất
json.dump([{k: v for k, v in r.items() if k != '_num'} for r in out],
          open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
for i, r in enumerate(out):
    if Q[i]['num'] is not None:
        assert sorted(Q[i]['num'])[r['a']] == Q[i]['num'][0], r['id']
json.dump({r['id']: [Q[i]['num'][0], r['o'][r['a']]] for i, r in enumerate(out) if Q[i]['num'] is not None},
          open('/home/user/cchn_moi/web/data/src/work_c3/num_answers.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('wrote', len(out), 'numeric-sorted positions', cnt, 'final', [pos.count(k) for k in range(4)])
