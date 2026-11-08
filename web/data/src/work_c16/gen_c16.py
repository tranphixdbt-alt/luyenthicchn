"""Sinh web/data/src/cm_16.json (C16-001…) từ slide 'Giao dịch bảo chứng'. Chạy: python3 -I gen_c16.py"""
import json, math, re, unicodedata
from pathlib import Path
HERE = Path(__file__).resolve().parent
DOCS = HERE.parents[3] / "tai_lieu_phap_ly" / "van_ban_txt"
OUT = HERE.parent / "cm_16.json"
TT120 = "TT_120_2020_TT-BTC_hop_nhat_VBHN_08_VBHN-BTC_2026.txt"
ND155 = "ND_155_2020_ND-CP_Cong_bao_so_45-56_2021.txt"
QD87 = "QD_87_QD-UBCK_2017_Quy_che_giao_dich_ky_quy_ban_dang_lai_MBS.txt"
B120 = "Thông tư 120/2020/TT-BTC (VBHN 08/VBHN-BTC/2026, hợp nhất TT 68/2024, TT 18/2025, TT 08/2026)"
B87 = ("Quy chế hướng dẫn giao dịch ký quỹ chứng khoán ban hành kèm Quyết định 87/QĐ-UBCK ngày 25/01/2017 "
       "(văn bản do UBCKNN ban hành theo khoản 8 Điều 9 TT 120/2020; UBCKNN tiếp tục áp dụng trong Kết luận thanh tra 109/KL-TT ngày 08/11/2024 và 47/KL-TT ngày 08/8/2025)")
TOPIC = "Giao dịch cổ phiếu trên thị trường chứng khoán"

def loose(s):
    s = unicodedata.normalize("NFC", s).lower()
    return re.sub(r"[\W_]+", "", s)
def check_quote(src, quote):
    raw = (DOCS / src).read_text(encoding="utf-8")
    raw = "\n".join(l for l in raw.splitlines() if not re.search(r"CÔNG BÁO/Số|^\s*\d{1,4}\s*$", l))
    assert len(quote) <= 300, (src, len(quote))
    assert loose(quote) in loose(raw), f"quote không khớp {src}: {quote[:60]}"
def vn(x, d=0):  # định dạng số kiểu Việt Nam
    s = f"{x:,.{d}f}"
    return s.replace(",", "§").replace(".", ",").replace("§", ".")

Q = []
def add(level, q, o, a, e, basis, quote="", src=""):
    assert len(o) == 4 and len(set(o)) == 4 and 0 <= a < 4
    if quote: check_quote(src, quote)
    Q.append(dict(id=f"C16-{len(Q)+1:03d}", part="CM", subject="MG", topic=TOPIC, level=level, q=q, o=o, a=a,
                  e=e, basis=basis, quote=quote, src=src, as_of="2026-11"))

# 001 – tài khoản giao dịch ký quỹ (k3 Đ9 TT120)
add(1, "Theo Thông tư 120/2020/TT-BTC, nhận định nào sau đây đúng về tài khoản giao dịch ký quỹ của nhà đầu tư?",
    ["Mỗi nhà đầu tư chỉ được có 01 tài khoản giao dịch ký quỹ trên toàn thị trường",
     "Có thể là tiểu khoản của tài khoản giao dịch hiện có nhưng phải hạch toán tách biệt",
     "Được hạch toán chung với tài khoản giao dịch thông thường của cùng nhà đầu tư",
     "Tại mỗi công ty chứng khoán, nhà đầu tư được mở tối đa 02 tài khoản ký quỹ"], 1,
    "Khoản 3 Điều 9: tại mỗi công ty chứng khoán nơi mở tài khoản giao dịch, nhà đầu tư chỉ được mở 01 tài khoản giao dịch ký quỹ (nên có thể có tài khoản ký quỹ ở nhiều công ty khác nhau, mỗi nơi một tài khoản). Tài khoản này là tài khoản riêng biệt, được quản lý riêng biệt hoặc hạch toán dưới hình thức tiểu khoản của tài khoản giao dịch hiện có; công ty phải hạch toán tách biệt với tài khoản giao dịch thông thường của từng nhà đầu tư và giữa các nhà đầu tư.",
    f"Khoản 3 Điều 9 {B120}",
    "Tại mỗi công ty chứng khoán nơi nhà đầu tư mở tài khoản giao dịch chứng khoán, nhà đầu tư chỉ được mở 01 tài khoản giao dịch ký quỹ. Tài khoản giao dịch ký quỹ là tài khoản riêng biệt hoặc được quản lý riêng biệt hoặc được hạch toán dưới hình thức tiểu khoản", TT120)

# 002 – danh sách chứng khoán ký quỹ (k4, k5 Đ9)
add(2, "Theo Thông tư 120/2020/TT-BTC, danh sách chứng khoán được thực hiện giao dịch ký quỹ tại một công ty chứng khoán được xác định như thế nào?",
    ["UBCKNN phê duyệt riêng danh sách chứng khoán ký quỹ cho từng công ty chứng khoán",
     "Công ty tự chọn bất kỳ mã niêm yết nào, không phụ thuộc danh sách của Sở giao dịch",
     "Công ty tự lựa chọn trên cơ sở danh sách Sở giao dịch công bố theo tiêu chí UBCKNN",
     "Công ty phải áp dụng nguyên danh sách Sở giao dịch công bố, không được bớt mã nào"], 2,
    "Khoản 4 Điều 9: chứng khoán được giao dịch ký quỹ là cổ phiếu niêm yết, đăng ký giao dịch, chứng chỉ quỹ niêm yết đáp ứng tiêu chí (thời gian niêm yết, quy mô vốn, kết quả kinh doanh, thanh khoản, minh bạch…) theo quy chế của UBCKNN; Sở giao dịch chứng khoán công bố danh sách được hoặc không được giao dịch ký quỹ. Khoản 5: trên cơ sở danh sách đó, công ty chứng khoán tự lựa chọn danh sách thực hiện tại công ty (có thể hẹp hơn) và công bố thông tin. Danh mục này là một trong các điều kiện dịch vụ công ty phải thông báo cho khách hàng (khoản 3 Điều 123 Luật Chứng khoán).",
    f"Khoản 4, 5 Điều 9 {B120}",
    "Trên cơ sở danh sách chứng khoán được giao dịch ký quỹ hoặc chứng khoán không được giao dịch ký quỹ do Sở giao dịch chứng khoán công bố, công ty chứng khoán lựa chọn danh sách chứng khoán được thực hiện giao dịch ký quỹ tại công ty", TT120)

# 003 – chứng khoán bị loại khỏi danh sách không tính vào tài sản khi xác định tỷ lệ ký quỹ
cash, pend, ok, z, debt = 40, 60, 700, 200, 450
eb = cash + pend + ok; r = (eb - debt) / eb
w_incl = (eb + z - debt) / (eb + z); w_nopend = (cash + ok - debt) / (cash + ok); w_pv = (eb - debt) / ok
assert abs(r - .4375) < 1e-12 and abs(w_incl - .55) < 1e-12 and abs(w_pv - .5) < 1e-12 and round(w_nopend*100, 2) == 39.19
add(3, "Tài khoản giao dịch ký quỹ của khách hàng có: tiền 40 triệu đồng; tiền bán chứng khoán chờ về 60 triệu đồng; chứng khoán thuộc danh sách được giao dịch ký quỹ trị giá 700 triệu đồng; cổ phiếu Z trị giá 200 triệu đồng (vừa bị Sở giao dịch đưa ra khỏi danh sách được giao dịch ký quỹ); dư nợ 450 triệu đồng. Hợp đồng quy định tỷ lệ ký quỹ = (Tổng tài sản − Dư nợ)/Tổng tài sản. Tỷ lệ ký quỹ của tài khoản theo quy định hiện hành là",
    ["55,00%", "50,00%", "39,19%", "43,75%"], 3,
    f"Khoản 6 Điều 9 TT 120/2020: chứng khoán không được phép giao dịch ký quỹ không được tính vào tài sản bảo đảm khi xác định tỷ lệ ký quỹ ban đầu và duy trì ⇒ loại cổ phiếu Z. Tổng tài sản = tiền + tiền bán chờ về + chứng khoán được ký quỹ = 40 + 60 + 700 = 800 triệu đồng; tài sản thực có = 800 − 450 = 350 ⇒ tỷ lệ = 350/800 = 43,75%. Lỗi thường gặp: vẫn tính Z ((1.000 − 450)/1.000 = 55,00%), bỏ tiền bán chờ về ((740 − 450)/740 = 39,19%), chia tài sản thực có cho riêng giá trị chứng khoán (350/700 = 50,00%). Theo Quy chế 87/QĐ-UBCK (Điều 10 khoản 2), cổ phiếu bị loại khỏi danh sách không được cho vay mới, không tính vào tài sản thực có nhưng vẫn là tài sản bảo đảm cho khoản vay hiện hữu (trừ khi có thỏa thuận khác).",
    f"Khoản 6 Điều 9 {B120}; Điều 2, khoản 2 Điều 10 {B87}",
    "Chứng khoán không được phép giao dịch ký quỹ không được tính vào tài sản bảo đảm khi xác định tỷ lệ ký quỹ ban đầu và tỷ lệ ký quỹ duy trì cho giao dịch ký quỹ.", TT120)

# 004 – điều kiện CTCK (Điều 198 NĐ155) – tổ hợp
add(2, "Theo Điều 198 Nghị định 155/2020/NĐ-CP (không bị Nghị định 245/2025/NĐ-CP sửa đổi), xét các điều kiện sau đối với công ty chứng khoán cung cấp dịch vụ cho khách hàng vay tiền mua chứng khoán để giao dịch ký quỹ:\nI. Được cấp phép nghiệp vụ môi giới và được Hội đồng quản trị (Hội đồng thành viên, chủ sở hữu) thông qua việc cung cấp dịch vụ\nII. Không đang trong tình trạng cảnh báo, kiểm soát, kiểm soát đặc biệt, đình chỉ hoặc tạm ngừng hoạt động\nIII. Không có lỗ lũy kế từ 50% vốn điều lệ trở lên\nIV. Có tối thiểu hai nhân viên có chứng chỉ hành nghề chuyên trách giao dịch ký quỹ\nNhững điều kiện nào có trong quy định hiện hành?",
    ["I và II", "I, II và III", "II, III và IV", "I, II và IV"], 0,
    "Điều 198 khoản 1 NĐ 155/2020 gồm: (a) được cấp phép môi giới và được HĐQT/HĐTV/chủ sở hữu thông qua; (b) không đang trong tình trạng cảnh báo, kiểm soát, kiểm soát đặc biệt, đình chỉ, tạm ngừng hoạt động, hợp nhất, sáp nhập, giải thể, phá sản; (c) tỷ lệ tổng nợ/vốn chủ sở hữu theo quy định của Bộ Tài chính (hiện là không quá 05 lần – khoản 1 Điều 26 TT 121/2020) và vốn chủ sở hữu không thấp hơn vốn điều lệ tối thiểu; (d) tỷ lệ vốn khả dụng tối thiểu 180% liên tục 06 tháng; (đ) hệ thống giao dịch, giám sát, quy trình nghiệp vụ và quản lý rủi ro. Các điều kiện \"lỗ lũy kế dưới 50% vốn điều lệ\", \"tối thiểu hai nhân viên có chứng chỉ hành nghề\" (cùng \"nợ/vốn chủ sở hữu không quá 6 lần\", \"vốn khả dụng trên 150% trong 3 tháng\") là quy định cũ, không còn trong văn bản hiện hành.",
    "Khoản 1 Điều 198 Nghị định 155/2020/NĐ-CP (không bị NĐ 245/2025/NĐ-CP sửa đổi); khoản 1 Điều 26 Thông tư 121/2020/TT-BTC (VBHN 09/VBHN-BTC/2026)",
    "Được cấp phép thực hiện nghiệp vụ môi giới chứng khoán và được Hội đồng quản trị hoặc Hội đồng thành viên hoặc chủ sở hữu công ty thông qua việc thực hiện cung cấp dịch vụ cho khách hàng vay tiền mua chứng khoán", ND155)

# 005 – hạn mức cho vay một khách hàng (3%) và tổng (200%)
vcsh, du_no, xin = 2400, 4700, 90
room_total = 2 * vcsh - du_no; cap_kh = .03 * vcsh; key = min(xin, room_total, cap_kh)
assert (room_total, cap_kh, key) == (100, 72, 72)
add(3, "Công ty chứng khoán K có vốn chủ sở hữu 2.400 tỷ đồng (theo báo cáo tài chính soát xét gần nhất), tổng dư nợ cho vay giao dịch ký quỹ hiện là 4.700 tỷ đồng. Khách hàng M chưa có dư nợ, đề nghị vay ký quỹ 90 tỷ đồng để mua một mã cổ phiếu mà K còn dư hạn mức theo mã. Theo hạn mức cho vay giao dịch ký quỹ của UBCKNN, K được cho M vay tối đa",
    ["100 tỷ đồng", "72 tỷ đồng", "240 tỷ đồng", "90 tỷ đồng"], 1,
    "Hạn mức: tổng dư nợ cho vay ký quỹ ≤ 200% vốn chủ sở hữu = 4.800 tỷ ⇒ còn 4.800 − 4.700 = 100 tỷ; cho vay một khách hàng ≤ 3% vốn chủ sở hữu = 72 tỷ. Mức cho vay tối đa = min(90; 100; 72) = 72 tỷ đồng. Lỗi thường gặp: chỉ xét hạn mức tổng (100), đáp ứng đủ đề nghị (90), dùng nhầm hạn mức theo một loại chứng khoán 10% (240).",
    f"Khoản 1, 2 Điều 9 {B87}",
    "Tổng mức cho vay giao dịch ký quỹ của công ty chứng khoán đối với một khách hàng không được vượt quá 3% vốn chủ sở hữu của công ty chứng khoán.", QD87)

# 006 – các hạn mức (phủ định)
add(2, "Theo hạn mức cho vay giao dịch ký quỹ trong Quy chế hướng dẫn giao dịch ký quỹ chứng khoán của UBCKNN (được áp dụng trong các kết luận thanh tra năm 2024–2025), nhận định nào sau đây KHÔNG đúng?",
    ["Tổng dư nợ cho vay ký quỹ của công ty không vượt quá 200% vốn chủ sở hữu",
     "Dư nợ cho vay ký quỹ đối với một loại chứng khoán không vượt quá 10% vốn chủ sở hữu",
     "Tổng mức cho vay ký quỹ đối với một khách hàng không vượt quá 3% vốn chủ sở hữu",
     "Số chứng khoán cho vay ký quỹ không vượt quá 10% số chứng khoán niêm yết của tổ chức"], 3,
    "Điều 9 Quy chế: tổng dư nợ ≤ 200% vốn chủ sở hữu; một khách hàng ≤ 3%; một loại chứng khoán ≤ 10% vốn chủ sở hữu; tổng số chứng khoán cho vay ký quỹ của một công ty ≤ 5% (không phải 10%) tổng số chứng khoán niêm yết của một tổ chức niêm yết. Vốn chủ sở hữu lấy theo báo cáo tài chính kiểm toán/soát xét gần nhất, không quá 06 tháng. Kết luận thanh tra 47/KL-TT (2025) của UBCKNN xử lý vi phạm hạn mức 3% và 5% này.",
    f"Điều 9 {B87}",
    "Tổng số chứng khoán cho vay giao dịch ký quỹ của một công ty chứng khoán không được vượt quá 5% tổng số chứng khoán niêm yết của một tổ chức niêm yết.", QD87)

# 007 – hạn chế giao dịch ký quỹ (tổ hợp, phủ định)
add(2, "Xét các tình huống sau tại công ty chứng khoán P (đã được cung cấp dịch vụ giao dịch ký quỹ):\nI. Khách hàng đề nghị vay ký quỹ để mua cổ phiếu do chính P phát hành\nII. Cá nhân nước ngoài đã có mã số giao dịch đề nghị mở tài khoản giao dịch ký quỹ tại P\nIII. Thành viên Hội đồng quản trị của P đề nghị mở tài khoản giao dịch ký quỹ tại P\nIV. Cổ phiếu khách hàng đã mua bằng tiền vay bị Sở giao dịch đưa ra khỏi danh sách ký quỹ; P tiếp tục giữ cổ phiếu này làm tài sản bảo đảm cho khoản vay hiện hữu (hợp đồng không có thỏa thuận khác)\nNhững tình huống nào P KHÔNG được chấp thuận hoặc thực hiện?",
    ["I và III", "II, III và IV", "I, II và III", "I, II, III và IV"], 2,
    "I: Điều 10 khoản 1 Quy chế 87 – không cho vay ký quỹ đối với cổ phiếu do chính công ty chứng khoán phát hành (cũng không cho vay đối với cổ phiếu, chứng chỉ quỹ do chính công ty bảo lãnh phát hành theo hình thức cam kết chắc chắn trong thời gian quy định, cổ phiếu của công ty sở hữu từ 50% vốn điều lệ của công ty chứng khoán hoặc do công ty chứng khoán sở hữu từ 50%). II: khoản 2 Điều 9 TT 120/2020 – nhà đầu tư nước ngoài không được giao dịch ký quỹ. III: Điều 13 khoản 4 Quy chế – không mở tài khoản ký quỹ cho chủ sở hữu, cổ đông lớn, thành viên HĐQT/HĐTV, Ban kiểm soát, Ban Giám đốc, kế toán trưởng… và người có liên quan (Kết luận thanh tra 109/KL-TT năm 2024 xử lý đúng các vi phạm I và III). IV được phép: Điều 10 khoản 2 – chứng khoán bị loại khỏi danh sách thì không cho vay mới, không tính vào tài sản thực có, nhưng vẫn là tài sản bảo đảm cho khoản vay trừ khi có thỏa thuận khác.",
    f"Khoản 2 Điều 9 {B120}; Điều 10, khoản 4 Điều 13 {B87}",
    "Nhà đầu tư nước ngoài không được thực hiện giao dịch ký quỹ.", TT120)

# 008 – nội dung tối thiểu của hợp đồng (NGOẠI TRỪ)
add(2, "Theo Thông tư 120/2020/TT-BTC, hợp đồng giao dịch ký quỹ tối thiểu phải có các nội dung sau, NGOẠI TRỪ:",
    ["Tài sản bảo đảm cho giao dịch ký quỹ và thời hạn bổ sung ký quỹ",
     "Cách xử lý tài sản bảo đảm khi nhà đầu tư không bổ sung ký quỹ",
     "Các rủi ro, thiệt hại có thể phát sinh và chi phí khách hàng phải trả",
     "Mức lợi nhuận kỳ vọng của danh mục chứng khoán mua bằng tiền vay"], 3,
    "Khoản 1 Điều 9: trước khi giao dịch ký quỹ, nhà đầu tư phải ký hợp đồng giao dịch ký quỹ với công ty chứng khoán được phép cho vay tiền mua chứng khoán; hợp đồng này đồng thời là hợp đồng cho các khoản vay trên tài khoản ký quỹ và tối thiểu gồm: tài sản bảo đảm, thời hạn bổ sung ký quỹ, xử lý tài sản bảo đảm khi không bổ sung ký quỹ, phương thức giải quyết tranh chấp, các rủi ro, thiệt hại có thể phát sinh và chi phí khách hàng phải thanh toán. Công ty không được cam kết lợi nhuận cho khách hàng.",
    f"Khoản 1 Điều 9 {B120}",
    "Hợp đồng giao dịch ký quỹ tối thiểu phải bao gồm nội dung về tài sản bảo đảm cho giao dịch ký quỹ, thời hạn bổ sung ký quỹ, xử lý tài sản bảo đảm cho giao dịch ký quỹ khi nhà đầu tư không bổ sung ký quỹ", TT120)

# 009 – bán tài sản bảo đảm: công bố thông tin, thông báo kết quả
add(2, "Khách hàng không bổ sung ký quỹ theo lệnh gọi ký quỹ, công ty chứng khoán quyết định bán chứng khoán là tài sản bảo đảm theo hợp đồng. Theo Thông tư 120/2020/TT-BTC, công ty chứng khoán phải",
    ["Xin chấp thuận của UBCKNN trước khi đặt lệnh bán chứng khoán là tài sản bảo đảm",
     "Công bố thông tin theo quy định trước khi bán, rồi thông báo kết quả bán cho khách hàng",
     "Chỉ bán khi khách hàng đồng ý bằng văn bản đối với từng lệnh bán tài sản bảo đảm",
     "Chuyển chứng khoán sang tài khoản tự doanh của công ty theo giá tham chiếu ngày đó"], 1,
    "Khoản 6 Điều 9: khi khách hàng không ký quỹ bổ sung, công ty có quyền bán chứng khoán là tài sản bảo đảm theo hợp đồng (không cần xin UBCKNN hay chờ khách hàng đồng ý từng lệnh). Trước khi bán, công ty công bố thông tin theo quy định và thông báo kết quả bán cho nhà đầu tư để họ thực hiện nghĩa vụ báo cáo sở hữu, công bố thông tin (nếu có – ví dụ cổ đông lớn, người nội bộ). Công ty không được tự chuyển chứng khoán của khách hàng sang tài khoản của mình.",
    f"Khoản 6 Điều 9 {B120}",
    "Trước khi thực hiện bán chứng khoán là tài sản bảo đảm, công ty chứng khoán thực hiện công bố thông tin theo quy định pháp luật và thông báo kết quả giao dịch bán chứng khoán là tài sản bảo đảm cho nhà đầu tư biết", TT120)

# 010 – vai trò UBCKNN (tổ hợp)
add(2, "Theo Thông tư 120/2020/TT-BTC, xét các nhận định sau về giao dịch ký quỹ:\nI. UBCKNN có quyền yêu cầu tạm ngừng giao dịch ký quỹ tại công ty chứng khoán khi cần thiết để ổn định thị trường\nII. UBCKNN ban hành quy chế hướng dẫn hoạt động giao dịch ký quỹ tại công ty chứng khoán\nIII. Sở giao dịch chứng khoán quyết định tỷ lệ ký quỹ ban đầu trong từng hợp đồng của khách hàng\nIV. Nhà đầu tư nước ngoài là tổ chức được giao dịch ký quỹ nếu công ty chứng khoán đánh giá rủi ro thanh toán đạt yêu cầu\nNhững nhận định nào đúng?",
    ["I, II và III", "II và IV", "I và II", "I, III và IV"], 2,
    "Khoản 8 Điều 9: UBCKNN ban hành quy chế hướng dẫn giao dịch ký quỹ (hiện là Quy chế kèm Quyết định 87/QĐ-UBCK); khoản 9: UBCKNN có quyền yêu cầu tạm ngừng giao dịch ký quỹ khi cần ổn định thị trường. III sai: tỷ lệ ký quỹ ban đầu, duy trì do công ty chứng khoán quy định trong hợp đồng (không thấp hơn mức tối thiểu của quy chế); nhà đầu tư có nghĩa vụ bảo đảm các tỷ lệ này (khoản 6). IV sai: nhà đầu tư nước ngoài không được giao dịch ký quỹ (khoản 2); đánh giá rủi ro thanh toán thuộc cơ chế mua cổ phiếu không yêu cầu đủ tiền của nhà đầu tư nước ngoài là tổ chức (Điều 9a), không phải cho vay ký quỹ.",
    f"Khoản 2, 6, 8, 9 Điều 9; Điều 9a {B120}",
    "Trong trường hợp cần thiết để ổn định thị trường, Ủy ban Chứng khoán Nhà nước có quyền yêu cầu tạm ngừng giao dịch ký quỹ tại công ty chứng khoán.", TT120)

# 011 – tỷ lệ ký quỹ thực tế danh mục hai mã
qx, px0, qy, py0, own = 20000, 30000, 30000, 20000, 600e6
cost = qx*px0 + qy*py0; debt = cost - own; v = qx*24000 + qy*23000; r = (v - debt)/v
assert (cost, debt, v) == (1200e6, 600e6, 1170e6) and round(r*100, 2) == 48.72
assert round((v-debt)/cost*100, 2) == 47.5 and round(debt/v*100, 2) == 51.28 and (qx*24000 - debt/2)/(qx*24000) == .375
add(3, "Khách hàng dùng 600 triệu đồng vốn tự có và vay ký quỹ phần còn lại để mua 20.000 cổ phiếu X giá 30.000 đồng và 30.000 cổ phiếu Y giá 20.000 đồng. Phiên sau, X giảm còn 24.000 đồng, Y tăng lên 23.000 đồng. Hợp đồng quy định tỷ lệ ký quỹ = (Giá trị chứng khoán − Dư nợ)/Giá trị chứng khoán; bỏ qua lãi vay và phí. Tỷ lệ ký quỹ thực tế của tài khoản là",
    ["47,50%", "48,72%", "51,28%", "37,50%"], 1,
    "Giá trị mua = 600 + 600 = 1.200 triệu ⇒ dư nợ = 1.200 − 600 = 600 triệu (không đổi). Giá trị mới = 20.000 × 24.000 + 30.000 × 23.000 = 480 + 690 = 1.170 triệu ⇒ tỷ lệ = (1.170 − 600)/1.170 = 48,72%. Tỷ lệ ký quỹ tính trên toàn tài khoản, mã tăng bù cho mã giảm. Lỗi thường gặp: chia cho giá trị mua ban đầu (570/1.200 = 47,50%), lấy dư nợ/giá trị (51,28%), chỉ xét mã X với nửa dư nợ ((480 − 300)/480 = 37,50%).",
    "Giáo trình Môi giới và tư vấn đầu tư chứng khoán (UBCKNN/SRTC) – Giá trị chứng khoán thực có và tỷ lệ ký quỹ thực tế của danh mục nhiều mã")

# 012 – số phiên giảm sàn liên tiếp đến khi vi phạm tỷ lệ duy trì
q, p0, lend, mmr = 3000, 40000, .4, .35
debt = lend*q*p0; pcall = debt/(q*(1-mmr))
n = next(k for k in range(1, 50) if p0*.93**k < pcall)
lin = math.ceil((1 - pcall/p0)/.07); wrong_mmr = next(k for k in range(1, 50) if p0*.93**k < p0*(1-mmr))
assert round(pcall) == 24615 and n == 7 and lin == 6 and wrong_mmr == 6
assert p0*.93**6 >= pcall > p0*.93**7
add(3, "Khách hàng mua 3.000 cổ phiếu giá 40.000 đồng; công ty chứng khoán cho vay 40% giá trị mua. Hợp đồng quy định tỷ lệ ký quỹ = (Giá trị chứng khoán − Dư nợ)/Giá trị chứng khoán, tỷ lệ duy trì 35%. Giả sử ngay sau đó cổ phiếu giảm sàn liên tiếp, mỗi phiên giảm đúng 7% so với giá đóng cửa phiên trước (bỏ qua làm tròn bước giá, lãi vay, phí). Tài khoản bắt đầu thấp hơn tỷ lệ duy trì vào cuối phiên giảm sàn thứ",
    ["5", "6", "7", "8"], 2,
    f"Dư nợ = 40% × 120 triệu = 48 triệu đồng. Ngưỡng giá: (3.000P − 48.000.000)/(3.000P) = 35% ⇒ P = 48.000.000/(3.000 × 0,65) ≈ 24.615 đồng (giảm 38,46%). Giá sau n phiên = 40.000 × 0,93^n: phiên 6 ≈ {vn(p0*.93**6)} đồng (vẫn ≥ ngưỡng), phiên 7 ≈ {vn(p0*.93**7)} đồng < 24.615 ⇒ phiên thứ 7. Lỗi thường gặp: chia mức giảm cần thiết cho 7% như giảm tuyến tính (38,46%/7% ≈ 5,5 ⇒ 6), coi ngưỡng là giá giảm 35% (0,93^n < 0,65 ⇒ 6). Biên độ dao động và quy tắc làm tròn giá sàn do Sở giao dịch quy định, có thể thay đổi theo hệ thống giao dịch.",
    "Giáo trình Môi giới và tư vấn đầu tư chứng khoán (UBCKNN/SRTC) – Ngưỡng giá gọi ký quỹ duy trì (biên độ giá là giả định của đề)")

# 013 – bán khống: số tiền nộp thêm
qs_, ps, imr_s, mm_s, p1 = 2000, 60000, .5, .3, 72000
credit = qs_*ps*(1+imr_s); v = qs_*p1; eq = credit - v; dep = mm_s*v - eq
dep_wrong = (mm_s*v - eq)/(1-mm_s); back50 = imr_s*v - eq
assert (credit, v, eq) == (180e6, 144e6, 36e6) and abs(dep - 7.2e6) < 1e-6 and round(dep_wrong) == 10285714 and back50 == 36e6
add(3, "Giả sử thị trường cho phép bán khống (ở Việt Nam, bán khống có bảo đảm theo Điều 11 Thông tư 120/2020/TT-BTC chỉ thực hiện khi UBCKNN triển khai). Nhà đầu tư bán khống 2.000 cổ phiếu giá 60.000 đồng, nộp ký quỹ 50% giá trị bán bằng tiền; tiền bán được giữ trong tài khoản. Tỷ lệ ký quỹ = (Tổng tiền trong tài khoản − Giá trị thị trường cổ phiếu phải trả)/Giá trị thị trường cổ phiếu phải trả; tỷ lệ duy trì 30%. Khi giá lên 72.000 đồng, bỏ qua lãi và phí, số tiền tối thiểu phải nộp thêm để về tỷ lệ duy trì là",
    ["36.000.000 đồng", "24.000.000 đồng", "7.200.000 đồng", "10.285.714 đồng"], 2,
    "Tổng tiền (dư có) = 120 + 60 = 180 triệu đồng. Giá trị cổ phiếu phải trả = 2.000 × 72.000 = 144 triệu ⇒ vốn thực có = 36 triệu, tỷ lệ 25% < 30%. Tiền nộp thêm làm tăng cả tổng tiền và vốn thực có, giá trị phải trả không đổi: (36 + X)/144 = 30% ⇒ X = 43,2 − 36 = 7,2 triệu đồng. Lỗi thường gặp: áp công thức của vị thế mua ((36 + X)/(144 + X) = 30% ⇒ 10.285.714), lấy toàn bộ khoản lỗ (12.000 × 2.000 = 24 triệu), đưa về tỷ lệ ban đầu 50% (72 − 36 = 36 triệu).",
    "Giáo trình Môi giới và tư vấn đầu tư chứng khoán (UBCKNN/SRTC) – Ký quỹ bổ sung của vị thế bán trước mua sau; Điều 11 Thông tư 120/2020/TT-BTC (VBHN 08/VBHN-BTC/2026)")

# 014 – nộp một phần tiền rồi bán bớt cổ phiếu
qn, pb, pn, mm = 10000, 50000, 34000, .35
debt = .5*qn*pb; v = qn*pn; e = v - debt; cashin = 20e6
need = v - (e + cashin)/mm; key = math.ceil(round(need/pn, 6))
w1 = math.ceil(round((mm*v - e - cashin)/pn, 6)); w2 = math.ceil(round((v + cashin - (e + cashin)/mm)/pn, 6)); w3 = math.ceil(round((v - e/mm)/pn, 6))
assert (debt, v, e) == (250e6, 340e6, 90e6) and (key, w1, w2, w3) == (757, 265, 1345, 2437)
qa = qn - key; assert (qa*pn - (debt - cashin - key*pn))/(qa*pn) >= mm
add(3, "Khách hàng mua 10.000 cổ phiếu giá 50.000 đồng bằng giao dịch ký quỹ, vay 50%. Hợp đồng quy định tỷ lệ ký quỹ = (Giá trị chứng khoán − Dư nợ)/Giá trị chứng khoán, tỷ lệ duy trì 35%. Giá giảm còn 34.000 đồng và khách hàng bị gọi ký quỹ. Khách hàng nộp 20 triệu đồng để trả bớt nợ, phần còn thiếu xử lý bằng cách bán cổ phiếu ở giá 34.000 đồng, toàn bộ tiền bán dùng trả nợ. Bỏ qua lãi, phí, thuế; số cổ phiếu tối thiểu phải bán (làm tròn lên) là",
    ["265 cổ phiếu", "757 cổ phiếu", "1.345 cổ phiếu", "2.437 cổ phiếu"], 1,
    "Dư nợ = 250 triệu; giá trị = 340 triệu; vốn tự có = 90 triệu (26,47% < 35%). Nộp 20 triệu trả nợ ⇒ vốn tự có 110 triệu, nợ 230 triệu. Bán cổ phiếu trả nợ không đổi vốn tự có: 110/(340 − S) ≥ 35% ⇒ S ≥ 340 − 314,29 = 25,71 triệu ⇒ 25.714.286/34.000 = 756,3 ⇒ 757 cổ phiếu (kiểm tra: còn 9.243 cổ phiếu, giá trị 314,26 triệu, nợ 204,26 triệu, tỷ lệ 35,0%). Lỗi thường gặp: lấy phần tiền còn thiếu (35% × 340 − 90 − 20 = 9 triệu) chia cho giá (265), coi 20 triệu là tài sản tăng thêm chứ không trả nợ (1.345), quên khoản 20 triệu đã nộp (2.437).",
    "Giáo trình Môi giới và tư vấn đầu tư chứng khoán (UBCKNN/SRTC) – Ký quỹ bổ sung kết hợp nộp tiền và thanh lý chứng khoán")

# 015 – giá trị thị trường hiện hành (tổ hợp)
add(1, "Theo giáo trình, xét các cách xác định giá trị thị trường hiện hành của chứng khoán trên tài khoản giao dịch ký quỹ:\nI. Ngày thông thường: theo giá đóng cửa của ngày giao dịch liền trước\nII. Ngày mua chứng khoán: bằng tổng số tiền trả cho chứng khoán, gồm cả hoa hồng và phí\nIII. Ngày bán chứng khoán: bằng giá khớp nhân khối lượng, chưa trừ hoa hồng, phí và thuế\nIV. Ngày bán chứng khoán: bằng tổng số tiền đã trả khi mua chứng khoán đó trước đây\nNhững cách xác định nào đúng?",
    ["I, II và III", "I và II", "II và IV", "I và III"], 1,
    "Giáo trình: giá trị thị trường hiện hành thường tính theo giá đóng cửa ngày giao dịch liền trước; ngày mua là tổng số tiền phải trả cho chứng khoán (gồm hoa hồng, phí); ngày bán là số tiền thực nhận sau khi trừ hoa hồng, phí và thuế (không phải giá trị gộp, càng không phải giá vốn). Quy chế 87/QĐ-UBCK (khoản 4 Điều 2) cũng quy định giá trị chứng khoán ký quỹ do công ty xác định trong hợp đồng nhưng không vượt quá giá đóng cửa tại ngày gần nhất; tỷ lệ ký quỹ được xác định vào cuối ngày giao dịch (Điều 6).",
    f"Giáo trình Môi giới và tư vấn đầu tư chứng khoán (UBCKNN/SRTC) – Giá trị thị trường hiện hành trên tài khoản giao dịch ký quỹ; khoản 4 Điều 2, Điều 6 {B87}")

for x in Q:
    assert len(x["q"]) > 20 and x["topic"] == TOPIC
    L = [len(o) for o in x["o"]]
    assert max(L) <= 2.2 * min(L) or max(L) < 20, (x["id"], L)
OUT.write_text(json.dumps(Q, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
from collections import Counter
print(len(Q), "câu →", OUT, "| vị trí đáp án:", dict(Counter(x["a"] for x in Q)),
      "| tổ hợp:", sum("\nI." in x["q"] for x in Q))
