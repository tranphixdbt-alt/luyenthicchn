# Soát file 4 (đáp án ôn tập lớp Môi giới – tư vấn): (1) tính lại mọi con số của tài liệu và của
# các câu tương ứng trong ngân hàng; (2) sinh các câu mới -> ../cm_11.json. Chạy: python3 -I gen_c11.py
import json, random, re, unicodedata
from collections import Counter

OUT = '/home/user/cchn_moi/web/data/src/cm_11.json'
LAW = '/home/user/cchn_moi/tai_lieu_phap_ly/van_ban_txt/VBHN_24_VBHN-VPQH_2025_Luat_Chung_khoan_hop_nhat_Cong_bao.txt'
SRC = 'Giáo trình SRTC (khung chương trình)'
GT_MG = 'Giáo trình Môi giới và tư vấn đầu tư chứng khoán (UBCKNN/SRTC) – '
M_CP = "Giao dịch cổ phiếu trên thị trường chứng khoán"
M_KH = "Xây dựng mạng lưới khách hàng và chăm sóc khách hàng"
close = lambda a, b, t=1e-6: abs(a - b) < t

def vn(x, d=0):
    return f"{x:,.{d}f}".replace(',', 'X').replace('.', ',').replace('X', '.')

# ======================= 1. Tính lại tài liệu =======================
# Bài tập: 1.000 cp × 10 USD, ký quỹ 50%, tỷ lệ duy trì ("dự trữ tối thiểu") 40%
n, p0, im, mm = 1000, 10, .5, .4
debt = n * p0 * (1 - im)                       # 5.000 USD
p_call = debt / (n * (1 - mm))                 # (nP − nợ)/nP = 40%
assert close(p_call, 25 / 3)                   # 8,33 USD
v7 = n * 7; eq7 = v7 - debt                    # 7.000; 2.000
assert close(eq7 / v7, 2 / 7)                  # 28,57% < 40% -> gọi ký quỹ
cash_mm = mm * v7 - eq7                        # nộp tiền trả nợ để về 40%
cash_im = im * v7 - eq7                        # nếu công ty đòi về 50%
sec_mm = (mm * v7 - eq7) / (1 - mm)            # nộp CK ký quỹ (tính đủ giá trị): (2000+Y)/(7000+Y)=40%
sell = v7 - eq7 / mm                           # bán CK trả nợ: 2000/(7000−S)=40%
assert close(cash_mm, 800) and close(cash_im, 1500) and close(sec_mm, 4000 / 3) and close(sell, 2000)
assert close((v7 - (debt - cash_mm)) / v7, mm) and close((eq7 + sec_mm) / (v7 + sec_mm), mm) and close(eq7 / (v7 - sell), mm)
sell_sh = -(-sell // 7)                        # 286 cp
assert sell_sh == 286
print(f"Bài tập: giá gọi ký quỹ {p_call:.4f} USD; tại 7 USD tỷ lệ {eq7 / v7:.2%}; nộp {cash_mm:.0f} USD tiền "
      f"(về 50%: {cash_im:.0f}); hoặc {sec_mm:.2f} USD CK; hoặc bán {sell:.0f} USD ≈ {sell_sh:.0f} cp")

# Câu 93: mua 16 tr, vay 8 tr; giá trị còn 12 tr; duy trì 25%
need93, eq93 = .25 * 12e6, 12e6 - 8e6
assert need93 == 3e6 and eq93 == 4e6 and close(eq93 / 12e6, 1 / 3)
# Câu 11: 100 cp, mua 5 tr, nộp 4 tr; đóng cửa 15/4 52.000, 16/4 48.000 (giá trị ngày t theo giá đóng cửa t−1)
mv11 = [5e6, 100 * 52000, 100 * 48000]
assert mv11 == [5e6, 5.2e6, 4.8e6]
# Câu 15: mua 20 tr, trả 15 tr; đóng cửa 10–13/3: 21, 20, 19, 18 nghìn; ngày 10/3 tính theo giá mua
eq15 = [(v - 5e6) / 1e6 for v in [20e6] + [1000 * c for c in (21000, 20000, 19000, 18000)]]
assert eq15 == [15, 16, 15, 14, 13]
# Câu 16: 1.000 cp × 50.000, ký quỹ 60%
mv16, debt16 = 1000 * 100000, 20e6
eq16 = mv16 - debt16; excess16 = eq16 - .6 * mv16; bp16 = excess16 / .6
assert (eq16, excess16) == (80e6, 20e6) and close(bp16, 33333333.333, 1e-2)
assert close((eq16 + bp16 - bp16) / (mv16 + bp16), .6) and close((mv16 - (debt16 + excess16)) / mv16, .6)  # mua thêm hết bằng vay / rút 20 tr
# Câu 26: 1.000 cp × 60.000, ký quỹ 50%, duy trì 25%
p26 = 30e6 / (1000 * .75)
assert p26 == 40000 and (1000 * 50000 - 30e6) / 50e6 >= .25 and (1000 * 35000 - 30e6) / 35e6 < .25
# Câu 27: 60,49 tr / (263 × 100)
assert close(60.49e6 / (263 * 100), 2300)

# Câu tương ứng trong ngân hàng (tính lại để xác nhận câu của ta vẫn đúng)
assert vn(200e6 / (.7 * 10000)) == "28.571"                                  # C1-063
assert .35 * 560e6 - (560e6 - 400e6) == 36e6                                 # C5-023
assert close((500 - 300) / 500, .4)                                          # C9-031
assert vn(-(-(600e6 - 180e6 / .35) // 20000)) == "4.286"                     # C9-034
assert close((1000 - 450 - 500) / .5, 100)                                   # C9-035
assert close(24 / 2, 12) and close(.0015 * 47.6e9, 71.4e6)                   # C4-030
print("Tài liệu và câu tương ứng: mọi con số khớp")

# ======================= 2. Câu mới =======================
Q = []
def add(topic, level, q, correct, wrong, e, basis, quote="", src=SRC):
    assert len(wrong) == 3 and len({correct, *wrong}) == 4, q[:40]
    Q.append(dict(topic=topic, level=level, q=q, correct=correct, wrong=wrong, e=e, basis=basis, quote=quote, src=src))

add(M_CP, 1,
    "Giao dịch ký quỹ (giao dịch bảo chứng) mua chứng khoán là nghiệp vụ trong đó công ty chứng khoán",
    "Cho nhà đầu tư vay một phần tiền mua chứng khoán, dùng chính chứng khoán đó làm tài sản bảo đảm khoản vay",
    ["Cho nhà đầu tư vay toàn bộ tiền mua chứng khoán, nhà đầu tư không phải góp vốn tự có",
     "Chỉ thực hiện lệnh mua trong phạm vi số tiền nhà đầu tư đã có sẵn trên tài khoản",
     "Cho nhà đầu tư vay tiền mua chứng khoán và để nhà đầu tư tự do rút chứng khoán khi còn dư nợ"],
    "Trong giao dịch ký quỹ, nhà đầu tư góp phần vốn tự có theo tỷ lệ ký quỹ, phần còn lại vay công ty chứng khoán; chứng khoán mua được (và chứng khoán ký quỹ khác) là tài sản bảo đảm nên không được tự do rút, chuyển khi còn dư nợ. Khoản tiền công ty cho vay (cộng lãi cộng dồn) là dư nợ; giá trị chứng khoán thực có = giá trị thị trường hiện hành − dư nợ. Giao dịch chỉ trong phạm vi tiền có sẵn là tài khoản tiền mặt (giao dịch thông thường); cho vay toàn bộ thì không còn phần ký quỹ của nhà đầu tư.",
    GT_MG + "Khái niệm giao dịch ký quỹ (bảo chứng) và dư nợ; điểm b khoản 1 Điều 86 Luật Chứng khoán 2019 (dịch vụ cho khách hàng vay tiền mua chứng khoán)")

add(M_CP, 1,
    "Lợi ích nào sau đây là ưu điểm của giao dịch ký quỹ đối với nhà đầu tư và thị trường chứng khoán?",
    "Tăng sức mua của nhà đầu tư, qua đó làm tăng cầu và tính thanh khoản của thị trường",
    ["Giảm tỷ lệ lỗ trên vốn tự có của nhà đầu tư khi giá chứng khoán giảm",
     "Chuyển rủi ro giảm giá của chứng khoán ký quỹ sang công ty chứng khoán",
     "Hạn chế biến động giá vì chứng khoán ký quỹ không được bán trước hạn vay"],
    "Vay ký quỹ cho phép nhà đầu tư mua lượng chứng khoán lớn hơn vốn tự có (sức mua = vốn tự có/tỷ lệ ký quỹ), làm tăng cầu, khối lượng giao dịch và thanh khoản, góp phần phát triển thị trường; khi giá tăng, lợi nhuận trên vốn tự có được khuếch đại. Ngược lại, đòn bẩy cũng khuếch đại thua lỗ khi giá giảm, nhà đầu tư vẫn chịu toàn bộ rủi ro giá và phải trả đủ nợ vay; chứng khoán ký quỹ bị bán giải chấp khi tài khoản thiếu ký quỹ, và bán giải chấp hàng loạt lúc thị trường giảm mạnh còn có thể làm giá biến động mạnh hơn.",
    GT_MG + "Ưu điểm và rủi ro của giao dịch ký quỹ")

add(M_CP, 2,
    "Trước khi khách hàng mở tài khoản giao dịch ký quỹ, nhân viên môi giới cần giải thích rõ rủi ro nào sau đây?",
    "Khách hàng có thể lỗ vượt số vốn ký quỹ ban đầu và vẫn phải trả đủ dư nợ, lãi vay",
    ["Khoản lỗ tối đa chỉ bằng vốn ký quỹ ban đầu, phần lỗ vượt quá do công ty chịu",
     "Khi bị gọi ký quỹ, khách hàng được chờ giá phục hồi, công ty không được bán chứng khoán",
     "Lãi vay ký quỹ chỉ phát sinh khi giá chứng khoán giảm xuống dưới giá mua"],
    "Với đòn bẩy, tỷ lệ lỗ trên vốn tự có ≈ tỷ lệ giảm giá/tỷ lệ ký quỹ (ký quỹ 50%, giá giảm 60% ⇒ lỗ 120% vốn tự có). Nếu giá giảm sâu, liên tục (giảm sàn nhiều phiên, thiếu thanh khoản) trước khi công ty kịp bán giải chấp, tiền bán chứng khoán không đủ trả nợ: khách hàng mất hết vốn ký quỹ mà vẫn còn nợ công ty. Khi bị gọi ký quỹ, khách hàng phải bổ sung tài sản trong thời hạn theo hợp đồng; quá hạn, công ty được bán chứng khoán ký quỹ để thu hồi nợ mà không chờ giá phục hồi. Lãi vay tính trên dư nợ theo thời gian vay, không phụ thuộc giá tăng hay giảm.",
    GT_MG + "Rủi ro của giao dịch ký quỹ cần giải thích cho khách hàng (lỗ vượt vốn ký quỹ, gọi ký quỹ, bán giải chấp)")

QUOTE = "Trường hợp cung cấp dịch vụ giao dịch ký quỹ, công ty chứng khoán phải thông báo các điều kiện cung cấp dịch vụ bao gồm yêu cầu về tỷ lệ ký quỹ, lãi suất vay, thời hạn vay, phương thức thực hiện lệnh gọi ký quỹ bổ sung, danh mục chứng khoán thực hiện giao dịch ký quỹ."
add(M_CP, 1,
    "Theo Luật Chứng khoán, khi cung cấp dịch vụ giao dịch ký quỹ, công ty chứng khoán phải thông báo các điều kiện cung cấp dịch vụ, bao gồm:",
    "Tỷ lệ ký quỹ, lãi suất vay, thời hạn vay, phương thức gọi ký quỹ bổ sung, danh mục chứng khoán ký quỹ",
    ["Tỷ lệ ký quỹ, lãi suất vay và mức lợi nhuận tối thiểu cam kết cho khách hàng sử dụng dịch vụ",
     "Tỷ lệ ký quỹ, lãi suất vay, danh sách khách hàng đang vay và dư nợ của từng khách hàng",
     "Lãi suất vay, thời hạn vay và cam kết mua lại chứng khoán ký quỹ của khách hàng khi giá giảm"],
    "Khoản 3 Điều 123 Luật Chứng khoán: trường hợp cung cấp dịch vụ giao dịch ký quỹ, công ty chứng khoán phải thông báo điều kiện cung cấp dịch vụ gồm yêu cầu về tỷ lệ ký quỹ, lãi suất vay, thời hạn vay, phương thức thực hiện lệnh gọi ký quỹ bổ sung, danh mục chứng khoán thực hiện giao dịch ký quỹ. Vì vậy khách hàng chỉ ký quỹ hoặc bổ sung ký quỹ bằng chứng khoán thuộc danh mục công ty chấp nhận. Công ty không được cam kết lợi nhuận, chia sẻ lỗ hay cam kết mua lại chứng khoán cho khách hàng, và phải bảo mật thông tin tài khoản của khách hàng khác.",
    "Khoản 3 Điều 123 Luật Chứng khoán 2019 (VBHN 24/VBHN-VPQH/2025); " + GT_MG + "Điều kiện cung cấp dịch vụ giao dịch ký quỹ",
    QUOTE, "VBHN_24_VBHN-VPQH_2025_Luat_Chung_khoan_hop_nhat_Cong_bao.txt")

add(M_CP, 2,
    "Trong giao dịch ký quỹ (bảo chứng), lệnh gọi ký quỹ ban đầu và lệnh gọi ký quỹ duy trì khác nhau ở điểm nào?",
    "Gọi ban đầu yêu cầu nộp đủ vốn tự có theo tỷ lệ ký quỹ ban đầu khi mua; gọi duy trì phát sinh khi tỷ lệ ký quỹ thực tế giảm dưới tỷ lệ duy trì",
    ["Gọi ban đầu phát sinh khi tỷ lệ ký quỹ thực tế giảm dưới tỷ lệ duy trì; gọi duy trì yêu cầu nộp đủ vốn tự có theo tỷ lệ ban đầu khi mua",
     "Gọi ban đầu chỉ áp dụng cho vị thế bán khống; gọi duy trì chỉ áp dụng cho vị thế mua chứng khoán bằng tiền vay công ty chứng khoán",
     "Gọi ban đầu do Sở giao dịch chứng khoán gửi cho nhà đầu tư; gọi duy trì do công ty chứng khoán gửi cho khách hàng của mình"],
    "Lệnh gọi ký quỹ ban đầu: khi khách hàng mua chứng khoán trên tài khoản ký quỹ, công ty yêu cầu nộp phần vốn tự có tối thiểu theo tỷ lệ ký quỹ ban đầu (mua 100 triệu đồng với tỷ lệ 50% phải có 50 triệu đồng). Lệnh gọi ký quỹ duy trì: sau khi mua, nếu giá giảm làm tỷ lệ ký quỹ thực tế = (giá trị chứng khoán − dư nợ)/giá trị chứng khoán thấp hơn tỷ lệ duy trì, công ty yêu cầu bổ sung tiền, chứng khoán hoặc bán bớt chứng khoán. Cả hai đều do công ty chứng khoán (bên cho vay) thực hiện với khách hàng và áp dụng cho cả vị thế mua ký quỹ lẫn bán khống (nơi được phép).",
    GT_MG + "Các loại lệnh gọi ký quỹ: gọi ký quỹ ban đầu và gọi ký quỹ duy trì")

add(M_CP, 2,
    "Mục đích chủ yếu của việc quy định tỷ lệ ký quỹ duy trì và thực hiện gọi ký quỹ duy trì trên tài khoản giao dịch ký quỹ là",
    "Bảo vệ công ty chứng khoán cho vay trước rủi ro giá trị tài sản bảo đảm không đủ thu hồi nợ",
    ["Bảo đảm nhà đầu tư không bị lỗ quá tỷ lệ ký quỹ duy trì tính trên vốn tự có ban đầu",
     "Tăng doanh thu lãi vay cho công ty chứng khoán khi giá chứng khoán ký quỹ giảm",
     "Giữ giá chứng khoán ký quỹ không giảm xuống dưới giá mua ban đầu của nhà đầu tư"],
    "Tỷ lệ duy trì tạo vùng đệm vốn tự có của nhà đầu tư so với dư nợ: khi giá giảm làm vùng đệm mỏng tới mức duy trì, công ty gọi ký quỹ để khách hàng bổ sung tài sản hoặc bán bớt chứng khoán trả nợ trước khi giá trị chứng khoán xuống thấp hơn dư nợ. Mục đích là bảo vệ khoản cho vay của công ty chứng khoán; gọi ký quỹ không bảo đảm nhà đầu tư không lỗ (đòn bẩy vẫn khuếch đại lỗ), không làm tăng lãi vay và không giữ được giá chứng khoán.",
    GT_MG + "Mục đích của ký quỹ duy trì và gọi ký quỹ duy trì")

sh, cost, paid, cl = 2000, 60e6, 42e6, (31500, 29000, 27500)
d7 = cost - paid
chain = [cost - d7] + [sh * c - d7 for c in cl[:2]]            # ngày 1 theo giá mua, ngày 2–3 theo giá đóng cửa hôm trước
assert chain == [42e6, 45e6, 40e6]
w7 = [sh * cl[2] - d7, sh * cl[0] - d7, sh * cl[1]]             # giá của chính ngày 3; giá ngày mua; quên trừ nợ
assert w7 == [37e6, 45e6, 58e6]
add(M_CP, 3,
    "Ngày giao dịch thứ nhất, khách hàng mua 2.000 cổ phiếu K trên tài khoản ký quỹ với tổng số tiền 60.000.000 đồng, cùng ngày thanh toán 42.000.000 đồng, phần còn lại vay công ty chứng khoán. Giá đóng cửa của K trong ba ngày giao dịch liên tiếp kể từ ngày mua lần lượt là 31.500; 29.000 và 27.500 đồng. Giả sử giá trị thị trường hiện hành của chứng khoán trên tài khoản trong mỗi ngày được xác định theo giá đóng cửa của ngày giao dịch liền trước (riêng ngày mua tính theo giá mua). Bỏ qua lãi vay và phí, giá trị chứng khoán thực có trên tài khoản vào ngày giao dịch thứ ba là",
    vn(chain[2]) + " đồng", [vn(x) + " đồng" for x in w7],
    f"Dư nợ = 60.000.000 − 42.000.000 = {vn(d7)} đồng. Ngày thứ ba dùng giá đóng cửa ngày thứ hai: giá trị thị trường hiện hành = 2.000 × 29.000 = 58.000.000 đồng ⇒ giá trị chứng khoán thực có = 58.000.000 − 18.000.000 = {vn(chain[2])} đồng (chuỗi ba ngày: 42, 45, 40 triệu đồng). Lỗi thường gặp: dùng giá đóng cửa của chính ngày thứ ba (2.000 × 27.500 − 18.000.000 = 37.000.000), dùng giá đóng cửa ngày mua (45.000.000), quên trừ dư nợ (58.000.000).",
    GT_MG + "Giá trị thị trường hiện hành, dư nợ và giá trị chứng khoán thực có trên tài khoản ký quỹ")

yr, calls = 6.3e6 * 12, 252 * 120
v_call = yr / calls
w8 = [yr / (365 * 120), 6.3e6 / calls, yr / 252]
assert vn(v_call) == "2.500" and [vn(x) for x in w8] == ["1.726", "208", "300.000"]
add(M_KH, 3,
    "Công ty chứng khoán trả cho nhân viên môi giới lương cố định 6,3 triệu đồng/tháng (12 tháng/năm). Một năm có 252 ngày làm việc; mỗi ngày nhân viên dự kiến thực hiện 120 cuộc điện thoại tìm kiếm khách hàng (không tính cước điện thoại). Giá trị (chi phí lương) của một cuộc gọi tìm kiếm khách hàng là",
    vn(v_call) + " đồng", [vn(x) + " đồng" for x in w8],
    f"Lương năm = 6,3 triệu × 12 = {vn(yr)} đồng; số cuộc gọi/năm = 252 × 120 = {vn(calls)} ⇒ giá trị một cuộc gọi = {vn(yr)}/{vn(calls)} = {vn(v_call)} đồng. Con số này giúp nhân viên môi giới ý thức chi phí thời gian, sàng lọc danh sách gọi và đo hiệu quả tìm kiếm khách hàng. Lỗi thường gặp: chia cho 365 ngày lịch ({vn(w8[0])}), lấy lương một tháng chia số cuộc gọi cả năm ({vn(w8[1])}), chỉ tính chi phí lương một ngày ({vn(w8[2])}).",
    GT_MG + "Giá trị một cuộc gọi trong kế hoạch tìm kiếm khách hàng")

# trích dẫn phải khớp nguyên văn (bỏ khoảng trắng/xuống dòng)
loose = lambda s: re.sub(r"[\W_]+", "", unicodedata.normalize("NFC", s).lower())
assert loose(QUOTE) in loose(open(LAW, encoding='utf-8').read())

# ======================= Gán id, vị trí đáp án =======================
pos = [0, 1, 2, 3] * 2
random.Random(20261108).shuffle(pos)
out = []
for i, (x, a) in enumerate(zip(Q, pos), 1):
    o = list(x['wrong']); o.insert(a, x['correct'])
    if x['level'] == 3:
        m = re.search(r"\d[\d.,]*", x['correct'])
        assert m.group(0) in x['e'], i
    lens = [len(s) for s in o]
    assert max(lens) <= 1.6 * min(lens), (i, lens)
    assert not re.search(r"(phương án|đáp án|chọn|câu)\s+[A-D]\b", x['e']), i
    out.append(dict(id=f"C11-{i:03d}", part="CM", subject="MG", topic=x['topic'], level=x['level'], q=x['q'], o=o, a=a,
                    e=x['e'], basis=x['basis'], quote=x['quote'], src=x['src'], as_of="2026-11"))
with open(OUT, 'w', encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False, indent=1)
print("wrote", len(out), "| a:", dict(sorted(Counter(x['a'] for x in out).items())),
      "| level:", dict(sorted(Counter(x['level'] for x in out).items())))
