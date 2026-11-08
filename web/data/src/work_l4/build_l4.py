"""Tạo luat_4.json (câu Luật mới từ soát xét slide 7 – quỹ, 9 – QLNN/thanh tra/giám sát/xử phạt, 10 – tranh chấp/khiếu nại/tố cáo/bồi thường).
Chạy: python3 -I build_l4.py  → ghi work_l4/luat_4.json sau khi tự kiểm tra trích dẫn, độ dài, cấu trúc."""
import json, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from qcheck import ok

LCK = "VBHN_24_VBHN-VPQH_2025_Luat_Chung_khoan_hop_nhat_Cong_bao.txt"
TT98 = "VBHN_04_VBHN-BTC_2026_TT98_136_hop_nhat.txt"
ND155 = "ND_155_2020_ND-CP_Cong_bao_so_45-56_2021.txt"
ND306 = "ND_306_2025_ND-CP_Cong_bao_so_1651-1652_2025.txt"
ND128 = "ND_128_2021_ND-CP_Cong_bao_so_55-56_2022.txt"
TT95 = "VBHN_13_VBHN-BTC_2026_TT95_138_giam_sat_giao_dich_hop_nhat.txt"
XLVPHC = "VBHN_90_VBHN-VPQH_2026_Luat_XLVPHC_hop_nhat.txt"
LTT = "Luat_Thanh_tra_84_2025_QH15_Cong_bao_so_953-954_2025.txt"
LKN = "VBHN_120_VBHN-VPQH_2025_Luat_Khieu_nai_hop_nhat_Cong_bao.txt"
L136 = "Luat_136_2025_QH15_sua_Luat_Tiep_cong_dan_Khieu_nai_To_cao.txt"
LTC = "VBHN_112_VBHN-VPQH_2025_Luat_To_cao_hop_nhat_Cong_bao.txt"
BLDS = "Bo_luat_Dan_su_91_2015_QH13_Cong_bao.txt"
TTTM = "Luat_Trong_tai_thuong_mai_54_2010_QH12_Cong_bao.txt"
TT99E = "TT_99_2020_TT-BTC_English_SSC.txt"
VB24 = "Luật Chứng khoán 2019 (VBHN 24/VBHN-VPQH năm 2025, hợp nhất Luật 56/2024/QH15)"
VB04 = "Thông tư 98/2020/TT-BTC (VBHN 04/VBHN-BTC năm 2026, hợp nhất TT 136/2025/TT-BTC)"
VB13 = "Thông tư 95/2020/TT-BTC (VBHN 13/VBHN-BTC năm 2026, hợp nhất TT 138/2025/TT-BTC, hiệu lực 01/3/2026)"
TP_TC = "Giải quyết tranh chấp, khiếu nại & bồi thường"   # chủ đề mới duy nhất

Q = []
def add(topic, level, q, o, a, e, basis, quote, src):
    Q.append(dict(topic=topic, level=level, q=q, o=o, a=a, e=e, basis=basis, quote=quote, src=src))

# ---------- Chuyên đề 7: công ty quản lý quỹ, quỹ đầu tư ----------
add("CTCK & CTQLQ", 3,
    "Nhóm sáng lập dự kiến thành lập công ty quản lý quỹ đầu tư chứng khoán Q (công ty cổ phần) với cơ cấu vốn điều lệ: Công ty chứng khoán A góp 30%, Công ty thương mại B góp 35%, 06 cá nhân góp 35%; A và B là cổ đông sáng lập. Theo Luật Chứng khoán, cơ cấu cổ đông này:",
    ["Đáp ứng, vì tổ chức góp 65%, trong đó công ty chứng khoán góp 30%",
     "Chưa đáp ứng, vì chỉ ngân hàng, bảo hiểm được tính vào mức 30%",
     "Chưa đáp ứng, vì tổng vốn góp của tổ chức phải từ 75% trở lên",
     "Chưa đáp ứng, vì công ty chứng khoán không được góp vốn lập công ty quản lý quỹ"], 0,
    "Điểm a, b khoản 3 Điều 75: công ty quản lý quỹ phải có tối thiểu 02 cổ đông sáng lập là tổ chức; tổng vốn góp của các tổ chức tối thiểu 65% vốn điều lệ, trong đó ngân hàng thương mại, doanh nghiệp bảo hiểm, công ty chứng khoán sở hữu tối thiểu 30%. Q có 02 tổ chức sáng lập, tổ chức nắm 30% + 35% = 65%, công ty chứng khoán A nắm 30% nên đáp ứng. Với công ty chứng khoán (điểm b khoản 3 Điều 74) chỉ doanh nghiệp bảo hiểm, ngân hàng thương mại mới được tính vào mức 30%. Slide 2025 chỉ nêu mức 30%, bỏ sót điều kiện 65%.",
    "Điểm a, b khoản 3 Điều 75 " + VB24 + "; so sánh điểm b khoản 3 Điều 74",
    "b) Tổng tỷ lệ vốn góp của các tổ chức tối thiểu là 65% vốn điều lệ, trong đó các tổ chức là ngân hàng thương mại, doanh nghiệp bảo hiểm, công ty chứng khoán sở hữu tối thiểu là 30% vốn điều lệ.", LCK)

add("CTCK & CTQLQ", 2,
    "Bà H được đề cử làm Tổng giám đốc công ty quản lý quỹ đầu tư chứng khoán đang làm hồ sơ xin cấp Giấy phép. Bà có chứng chỉ hành nghề quản lý quỹ, 05 năm làm việc tại bộ phận đầu tư của một doanh nghiệp bảo hiểm, không bị truy cứu trách nhiệm hình sự, nhưng bị xử phạt vi phạm hành chính về chứng khoán 04 tháng trước ngày nộp hồ sơ. Theo Luật Chứng khoán, bà H:",
    ["Chưa đủ tiêu chuẩn, vì bị xử phạt hành chính về chứng khoán trong 06 tháng gần nhất",
     "Đủ tiêu chuẩn, vì chỉ người đang bị truy cứu trách nhiệm hình sự mới bị loại trừ",
     "Chưa đủ tiêu chuẩn, vì cần tối thiểu 06 năm kinh nghiệm tại công ty quản lý quỹ",
     "Chưa đủ tiêu chuẩn, vì Tổng giám đốc phải có chứng chỉ hành nghề phân tích tài chính"], 0,
    "Khoản 5 Điều 75: Tổng giám đốc công ty quản lý quỹ phải không đang bị truy cứu trách nhiệm hình sự, chấp hành án phạt tù hoặc bị cấm hành nghề; có tối thiểu 04 năm kinh nghiệm tại bộ phận nghiệp vụ của tổ chức tài chính, chứng khoán, ngân hàng, bảo hiểm (hoặc bộ phận tài chính, kế toán, đầu tư của doanh nghiệp khác); có chứng chỉ hành nghề quản lý quỹ hoặc tương đương; và không bị xử phạt vi phạm hành chính về chứng khoán trong 06 tháng gần nhất tính đến thời điểm nộp hồ sơ. Bà H đủ kinh nghiệm và chứng chỉ nhưng mới bị xử phạt 04 tháng. Chứng chỉ phân tích tài chính là một lựa chọn cho Tổng giám đốc công ty chứng khoán (Điều 74).",
    "Khoản 5 Điều 75 " + VB24,
    "d) Không bị xử phạt vi phạm hành chính trong lĩnh vực chứng khoán và thị trường chứng khoán trong thời hạn 06 tháng gần nhất tính đến thời điểm nộp hồ sơ.", LCK)

add("CTCK & CTQLQ", 2,
    "Theo Luật Chứng khoán, công ty quản lý quỹ đầu tư chứng khoán phải được Ủy ban Chứng khoán Nhà nước chấp thuận bằng văn bản trước khi thực hiện việc nào sau đây?",
    ["Thực hiện đầu tư gián tiếp ra nước ngoài",
     "Tạm ngừng hoạt động do sự kiện bất khả kháng",
     "Ký hợp đồng quản lý danh mục với khách hàng mới",
     "Thay đổi nhân viên bộ phận kiểm soát nội bộ"], 0,
    "Khoản 1 Điều 87: công ty chứng khoán, công ty quản lý quỹ phải được UBCKNN chấp thuận trước khi tạm ngừng hoạt động (trừ do bất khả kháng); chào bán, niêm yết chứng khoán của công ty ở nước ngoài; đầu tư gián tiếp ra nước ngoài; thành lập, đóng cửa chi nhánh, văn phòng đại diện, công ty con ở nước ngoài, phòng giao dịch; thay đổi tên, địa điểm chi nhánh, văn phòng đại diện, phòng giao dịch. Ký hợp đồng ủy thác là hoạt động nghiệp vụ thông thường; thay đổi nhân sự kiểm soát nội bộ chỉ phải thông báo UBCKNN trong 07 ngày làm việc (khoản 5 Điều 6 Thông tư 99/2020/TT-BTC). Danh sách trên slide 2025 gộp cả các thủ tục điều chỉnh Giấy phép (đổi tên, trụ sở chính, vốn điều lệ) và tổ chức lại (Điều 93), không phải đều thuộc Điều 87.",
    "Khoản 1 Điều 87 " + VB24 + "; khoản 5 Điều 6 Thông tư 99/2020/TT-BTC",
    "a) Tạm ngừng hoạt động, trừ trường hợp tạm ngừng do nguyên nhân bất khả kháng; b) Chào bán và niêm yết chứng khoán của công ty chứng khoán, công ty quản lý quỹ đầu tư chứng khoán tại nước ngoài; c) Đầu tư gián tiếp ra nước ngoài;", LCK)

add("Quỹ đầu tư", 2,
    "Nhận định nào sau đây đúng về việc đầu tư vào bất động sản của quỹ đầu tư chứng khoán?",
    ["Quỹ mở được đầu tư tối đa 10% tổng giá trị tài sản vào bất động sản",
     "Quỹ đóng (không phải quỹ bất động sản) đầu tư tối đa 10% tổng tài sản vào bất động sản",
     "Quỹ thành viên không được đầu tư vào bất động sản trong mọi trường hợp",
     "Quỹ đại chúng được đầu tư không hạn chế vào bất động sản đã hoàn thành"], 1,
    "Điểm d khoản 1 Điều 110: công ty quản lý quỹ không được đầu tư quá 10% tổng giá trị tài sản của quỹ đóng vào bất động sản (trừ quỹ đầu tư bất động sản) và không được đầu tư vốn của quỹ mở vào bất động sản; điểm c khoản 4 Điều 24 TT 98 (sửa bởi TT 136/2025) giữ mức 10% cho quỹ đóng. Quỹ thành viên được đầu tư bất động sản đủ điều kiện kinh doanh nếu Điều lệ quỹ quy định và Đại hội nhà đầu tư chấp thuận bằng văn bản (khoản 4 Điều 5 TT 98). Slide 2025 (trang 31) cho rằng tài sản đầu tư của quỹ đại chúng và quỹ thành viên không khác nhau, kể cả bất động sản – chưa chính xác với quỹ mở.",
    "Điểm d khoản 1 Điều 110 " + VB24 + "; điểm c khoản 4 Điều 24, khoản 4 Điều 5 " + VB04,
    "d) Đầu tư quá 10% tổng giá trị tài sản của quỹ đóng vào bất động sản, trừ trường hợp là quỹ đầu tư bất động sản; đầu tư vốn của quỹ mở vào bất động sản;", LCK)

add("Quỹ đầu tư", 3,
    "Quỹ đóng V có tổng giá trị tài sản 800 tỷ đồng, đang nắm cổ phiếu của công ty mẹ P trị giá 110 tỷ đồng và trái phiếu niêm yết của công ty S (công ty con của P) trị giá 90 tỷ đồng. Giả định giới hạn 10% chứng khoán đang lưu hành của từng tổ chức phát hành không bị vượt. Theo Luật Chứng khoán, giá trị tối đa V còn được đầu tư thêm vào cổ phiếu niêm yết của công ty T (một công ty con khác của P) là:",
    ["40 tỷ đồng", "160 tỷ đồng", "240 tỷ đồng", "70 tỷ đồng"], 0,
    "Điểm đ khoản 1 Điều 110: không đầu tư quá 30% tổng giá trị tài sản quỹ đại chúng vào các công ty trong cùng nhóm có quan hệ sở hữu (công ty mẹ, công ty con; các công ty sở hữu trên 35% của nhau; nhóm công ty con có cùng công ty mẹ). Hạn mức nhóm = 30% × 800 = 240 tỷ; đã dùng 110 + 90 = 200 tỷ nên còn 240 − 200 = 40 tỷ. Giới hạn riêng một tổ chức phát hành (điểm c, 20% × 800 = 160 tỷ) không phải ràng buộc chặt nhất. 240 tỷ là quên trừ phần đã đầu tư; 70 tỷ là lấy 160 − 90 (áp nhầm mức 20% cho cả nhóm).",
    "Điểm c, đ khoản 1 Điều 110 " + VB24 + "; điểm d khoản 4 Điều 24 " + VB04,
    "đ) Đầu tư quá 30% tổng giá trị tài sản của quỹ đại chúng vào các công ty trong cùng một nhóm công ty có quan hệ sở hữu với nhau thuộc các trường hợp sau đây: công ty mẹ, công ty con; các công ty sở hữu trên 35% cổ phần, phần vốn góp của nhau; nhóm công ty con có cùng một công ty mẹ;", LCK)

add("Quỹ đầu tư", 2,
    "Ngày 10/9/2026, công ty quản lý quỹ M phát hiện quỹ đóng do M quản lý nắm chứng khoán của một tổ chức phát hành vượt 20% tổng giá trị tài sản quỹ vì bộ phận đầu tư đặt mua vượt hạn mức, không phải do biến động giá hay nguyên nhân khách quan khác được pháp luật cho phép. Theo Thông tư 98/2020/TT-BTC (sửa đổi bởi TT 136/2025/TT-BTC), M phải:",
    ["Điều chỉnh danh mục trong 15 ngày từ ngày phát hiện, bồi thường thiệt hại cho quỹ (nếu có)",
     "Điều chỉnh danh mục trong 03 tháng từ ngày phát sinh sai lệch và thông báo cho UBCKNN",
     "Giữ nguyên danh mục nếu Ban đại diện quỹ chấp thuận bằng văn bản cho khoản vượt mức",
     "Điều chỉnh danh mục trong 06 tháng, lợi nhuận phát sinh được hạch toán cho công ty"], 0,
    "Khoản 5, 6 Điều 24 TT 98: cơ cấu quỹ đóng chỉ được vượt hạn mức do biến động giá, thanh toán theo quy định, chia, tách, hợp nhất tổ chức phát hành, quỹ mới lập chưa quá 06 tháng hoặc đang giải thể; khi đó công ty quản lý quỹ có 03 tháng để điều chỉnh và thông báo UBCKNN. Khoản 7: sai lệch do công ty không tuân thủ hạn chế đầu tư thì phải điều chỉnh trong 15 ngày kể từ ngày phát hiện, bồi thường thiệt hại cho quỹ (nếu có), chịu mọi chi phí và hạch toán ngay mọi khoản lợi nhuận phát sinh cho quỹ. Ban đại diện quỹ không có quyền cho phép vượt hạn mức luật định.",
    "Khoản 5, 6, 7 Điều 24 " + VB04 + "; khoản 3, 4 Điều 110 Luật Chứng khoán 2019",
    "7. Trường hợp sai lệch do công ty quản lý quỹ không tuân thủ các hạn chế đầu tư theo quy định của pháp luật hoặc Điều lệ quỹ, công ty quản lý quỹ phải điều chỉnh lại danh mục đầu tư trong thời hạn 15 ngày kể từ ngày phát hiện ra sai lệch.", TT98)

add("Quỹ đầu tư", 2,
    "Theo Thông tư 98/2020/TT-BTC (sửa đổi bởi TT 136/2025/TT-BTC), trường hợp Điều lệ quỹ có quy định, quỹ thành viên được vay thế chấp, thấu chi từ ngân hàng lưu ký hoặc vay mua chứng khoán (giao dịch ký quỹ) với giới hạn nào?",
    ["Hạn mức do Đại hội nhà đầu tư quyết định; tổng nợ, phải trả không quá 30% tổng tài sản",
     "Chỉ vay ngắn hạn tối đa 5% giá trị tài sản ròng, thời hạn vay không quá 30 ngày",
     "Hạn mức do công ty quản lý quỹ quyết định, không quá 50% giá trị tài sản ròng của quỹ",
     "Không được vay dưới mọi hình thức, giống quy định áp dụng cho quỹ đại chúng"], 0,
    "Điểm d khoản 5 Điều 5 TT 98: nếu Điều lệ quy định, quỹ thành viên được vay thế chấp, thấu chi hoặc hình thức khác từ ngân hàng lưu ký, vay mua chứng khoán; hạn mức vay do Đại hội nhà đầu tư quyết định nhưng tổng nợ và các khoản phải trả không vượt 30% tổng tài sản của quỹ tại mọi thời điểm; bộ phận tín dụng của ngân hàng lưu ký phải tách biệt với bộ phận lưu ký. Mức 5% giá trị tài sản ròng, tối đa 30 ngày là khoản vay ngắn hạn cho chi phí, thanh toán của quỹ đại chúng (khoản 2 Điều 110 Luật Chứng khoán). Slide 2025 ghi 'quỹ thành viên được vay 30% nếu Điều lệ cho phép' – đúng, cần hiểu 30% là trên tổng tài sản.",
    "Điểm d khoản 5 Điều 5 " + VB04 + "; khoản 2 Điều 110 Luật Chứng khoán 2019",
    "- Hạn mức vay do Đại hội nhà đầu tư quyết định, nhưng phải bảo đảm tổng nợ và các khoản phải trả của quỹ không vượt quá 30% tổng tài sản của quỹ tại mọi thời điểm;", TT98)

add("Quỹ đầu tư", 1,
    "Theo Nghị định 155/2020/NĐ-CP, kể từ ngày nhận được hồ sơ đầy đủ, hợp lệ đăng ký lập quỹ thành viên, Ủy ban Chứng khoán Nhà nước cấp Giấy chứng nhận đăng ký lập quỹ trong thời hạn nào, và vốn của quỹ được giải ngân khi nào?",
    ["15 ngày; vốn chỉ được giải ngân sau khi được cấp Giấy chứng nhận đăng ký lập quỹ",
     "07 ngày làm việc; vốn được giải ngân ngay sau khi nộp đủ hồ sơ cho UBCKNN",
     "30 ngày; vốn được giải ngân khi ngân hàng lưu ký xác nhận quy mô vốn góp",
     "15 ngày; vốn được giải ngân khi Đại hội nhà đầu tư thông qua Điều lệ quỹ"], 0,
    "Khoản 1 Điều 230 NĐ 155/2020 (không bị NĐ 245/2025 sửa): trong 15 ngày kể từ ngày nhận hồ sơ đầy đủ, hợp lệ, UBCKNN cấp Giấy chứng nhận đăng ký lập quỹ; vốn của quỹ chỉ được giải ngân sau khi có Giấy chứng nhận – khớp mốc T+15 trên slide 2025. 07 ngày làm việc là thời hạn cấp Giấy chứng nhận đăng ký lập quỹ đóng sau đợt chào bán ra công chúng (khoản 2 Điều 239); giấy xác nhận quy mô vốn của ngân hàng lưu ký chỉ là một tài liệu trong hồ sơ (Điều 223).",
    "Khoản 1 Điều 230, Điều 222, Điều 223 Nghị định 155/2020/NĐ-CP (không bị Nghị định 245/2025/NĐ-CP sửa đổi)",
    "Trong thời hạn 15 ngày kể từ ngày nhận được hồ sơ đầy đủ và hợp lệ về việc đăng ký lập quỹ, Ủy ban Chứng khoán Nhà nước cấp Giấy chứng nhận đăng ký lập quỹ; trường hợp từ chối, phải trả lời bằng văn bản và nêu rõ lý do. Vốn của quỹ chỉ được giải ngân sau khi Ủy ban Chứng khoán Nhà nước cấp Giấy", ND155)

add("Quỹ đầu tư", 2,
    "Công ty quản lý quỹ N đã hoàn thành đợt chào bán chứng chỉ quỹ đóng lần đầu ra công chúng và đạt điều kiện thành lập quỹ. Theo Nghị định 155/2020/NĐ-CP, N phải gửi hồ sơ đăng ký lập quỹ trong thời hạn nào, và UBCKNN cấp Giấy chứng nhận đăng ký lập quỹ trong thời hạn nào?",
    ["10 ngày sau khi hoàn thành chào bán; 07 ngày làm việc từ khi nhận đủ hồ sơ hợp lệ",
     "15 ngày sau khi hoàn thành chào bán; 30 ngày từ khi nhận đủ hồ sơ hợp lệ",
     "10 ngày sau khi hoàn thành chào bán; 15 ngày từ khi nhận đủ hồ sơ hợp lệ",
     "05 ngày làm việc sau khi hoàn thành chào bán; 10 ngày từ khi nhận đủ hồ sơ"], 0,
    "Điều 239 NĐ 155/2020: UBCKNN cấp Giấy chứng nhận đăng ký chào bán chứng chỉ quỹ đóng trong 30 ngày kể từ ngày nhận hồ sơ đầy đủ; trong 10 ngày sau khi hoàn thành đợt chào bán, công ty quản lý quỹ gửi hồ sơ đăng ký lập quỹ; trong 07 ngày làm việc kể từ ngày nhận hồ sơ đầy đủ, hợp lệ, UBCKNN cấp Giấy chứng nhận đăng ký lập quỹ. Đây là các mốc 'T+30 … T+60 … T+67' trên slide 2025. 15 ngày là thời hạn cấp Giấy chứng nhận cho quỹ thành viên (Điều 230).",
    "Khoản 1, 2 Điều 239 Nghị định 155/2020/NĐ-CP (không bị Nghị định 245/2025/NĐ-CP sửa đổi); khoản 2 Điều 108 Luật Chứng khoán 2019",
    "2. Trong thời hạn 10 ngày sau khi hoàn thành đợt chào bán, công ty quản lý quỹ đầu tư chứng khoán gửi hồ sơ đăng ký lập quỹ đến Ủy ban Chứng khoán Nhà nước. Trong thời hạn 07 ngày làm việc kể từ ngày nhận được hồ sơ đầy đủ và hợp lệ, Ủy ban Chứng khoán Nhà nước cấp Giấy chứng nhận đăng ký lập quỹ;", ND155)

add("Quỹ đầu tư", 2,
    "Đợt huy động vốn thành lập quỹ đại chúng P (không phải quỹ ETF) kết thúc đúng hạn, không gia hạn, với 230 nhà đầu tư nhưng tổng giá trị chứng chỉ quỹ bán được chỉ 42 tỷ đồng. Theo Luật Chứng khoán, công ty quản lý quỹ phải:",
    ["Hoàn trả mọi khoản tiền đã góp trong 15 ngày và chịu mọi chi phí phát sinh",
     "Thành lập quỹ với quy mô 42 tỷ đồng vì đã có trên 100 nhà đầu tư",
     "Hoàn trả trong 30 ngày, chi phí huy động được trừ vào tiền góp của nhà đầu tư",
     "Chuyển các nhà đầu tư đã góp vốn sang một quỹ thành viên do công ty quản lý"], 0,
    "Khoản 1 Điều 108: quỹ đại chúng chỉ được thành lập khi có ít nhất 100 nhà đầu tư (không kể nhà đầu tư chuyên nghiệp, trừ quỹ ETF) và tổng giá trị chứng chỉ quỹ bán được đạt ít nhất 50 tỷ đồng; P chỉ đạt 42 tỷ. Khoản 3: công ty quản lý quỹ phải hoàn trả cho nhà đầu tư mọi khoản tiền đã góp trong 15 ngày kể từ ngày kết thúc huy động và chịu mọi chi phí, nghĩa vụ tài chính phát sinh; khoản 3 Điều 14 TT 98 bổ sung: công bố thông tin, báo cáo UBCKNN trong 03 ngày làm việc và hoàn trả cả lãi (nếu có). Quỹ thành viên chỉ gồm nhà đầu tư chứng khoán chuyên nghiệp nên không thể chuyển nhà đầu tư đại chúng sang.",
    "Khoản 1, 3 Điều 108 " + VB24 + "; khoản 3, 4 Điều 14 " + VB04,
    "3. Trường hợp việc huy động vốn của quỹ đại chúng không đáp ứng quy định tại khoản 1 Điều này thì công ty quản lý quỹ đầu tư chứng khoán phải hoàn trả cho nhà đầu tư mọi khoản tiền đã đóng góp trong thời hạn 15 ngày kể từ ngày kết thúc việc huy động vốn.", LCK)

add("Quỹ đầu tư", 2,
    "Theo Thông tư 98/2020/TT-BTC, hoạt động nào sau đây quỹ đầu tư bất động sản KHÔNG được thực hiện?",
    ["Tham gia đấu giá quyền sử dụng đất để triển khai dự án bất động sản",
     "Mua tòa nhà văn phòng đã hoàn thành xây dựng để cho thuê lấy lợi tức",
     "Đầu tư vào cổ phiếu niêm yết của tổ chức kinh doanh bất động sản",
     "Gửi tiền tại ngân hàng thương mại theo quy định của pháp luật"], 0,
    "Điều 50 TT 98: quỹ đầu tư bất động sản không được xây dựng, triển khai và phát triển dự án bất động sản, gồm tham gia đấu giá quyền sử dụng đất, đấu thầu dự án; đề xuất dự án; triển khai dự án đầu tư xây dựng. Điều 51: quỹ đầu tư tối thiểu 65% giá trị tài sản ròng vào bất động sản ở Việt Nam để cho thuê, khai thác thu lợi tức ổn định và chứng khoán của tổ chức kinh doanh bất động sản; phần còn lại được gửi tiền, mua công cụ thị trường tiền tệ, chứng khoán theo hạn mức. Slide 2025 mô tả quỹ bất động sản 'tập trung vào bất động sản tạo dòng tiền cho thuê' là phù hợp.",
    "Điều 50, điểm a khoản 3 Điều 51 " + VB04,
    "Quỹ đầu tư bất động sản không được thực hiện các hoạt động xây dựng, triển khai và phát triển dự án bất động sản. Phát triển dự án bất động sản bao gồm một hoặc một số các hoạt động sau: 1. Tham gia đấu giá quyền sử dụng đất, đấu thầu thực hiện các dự án bất động sản;", TT98)

add("Quỹ đầu tư", 2,
    "Ngân hàng thương mại G có Giấy chứng nhận đăng ký hoạt động lưu ký chứng khoán và đang sở hữu 15% vốn điều lệ công ty quản lý quỹ R. R dự kiến chọn G làm ngân hàng giám sát cho một quỹ mở mới do R quản lý. Theo Luật Chứng khoán, nhận định nào đúng?",
    ["Không được, vì ngân hàng giám sát không được có quan hệ sở hữu với công ty quản lý quỹ",
     "Được, vì G đã có Giấy chứng nhận đăng ký hoạt động lưu ký chứng khoán",
     "Được, nếu tỷ lệ sở hữu của G tại R không vượt quá 20% vốn điều lệ",
     "Được, nếu Ban đại diện quỹ biểu quyết chấp thuận việc lựa chọn G"], 0,
    "Khoản 1 Điều 117: ngân hàng giám sát, thành viên HĐQT, người điều hành và nhân viên làm nhiệm vụ giám sát, bảo quản tài sản quỹ đại chúng không được là người có liên quan hoặc có quan hệ sở hữu, vay hoặc cho vay với công ty quản lý quỹ và ngược lại. G sở hữu 15% vốn của R nên không được làm ngân hàng giám sát cho quỹ do R quản lý, dù đủ điều kiện lưu ký (khoản 1 Điều 116). Khoản 2 Điều 117 (không được là đối tác mua, bán tài sản của quỹ) là hạn chế riêng. Khớp slide 2025 trang 13.",
    "Khoản 1 Điều 117 " + VB24,
    "Ngân hàng giám sát, thành viên Hội đồng quản trị, người điều hành và nhân viên của ngân hàng giám sát làm nhiệm vụ giám sát hoạt động và bảo quản tài sản của quỹ đại chúng, công ty đầu tư chứng khoán không được là người có liên quan hoặc có quan hệ sở hữu, vay hoặc cho vay với công ty quản lý quỹ", LCK)

add("CTCK & CTQLQ", 2,
    "Theo Thông tư 99/2020/TT-BTC, công ty quản lý quỹ nào sau đây bắt buộc phải thành lập bộ phận kiểm toán nội bộ, và bộ phận này trực thuộc cấp nào?",
    ["Công ty đang quản lý quỹ đại chúng; trực thuộc Hội đồng quản trị (Hội đồng thành viên, chủ sở hữu)",
     "Mọi công ty quản lý quỹ không phân biệt quy mô; trực thuộc Tổng giám đốc (Giám đốc) công ty",
     "Công ty chỉ quản lý quỹ thành viên và danh mục ủy thác; trực thuộc Ban kiểm soát công ty",
     "Công ty có vốn điều lệ từ 300 tỷ đồng trở lên; trực thuộc Tổng giám đốc (Giám đốc) công ty"], 0,
    "Khoản 1 Điều 5 TT 99: công ty quản lý quỹ là công ty đại chúng hoặc quản lý quỹ đại chúng, công ty đầu tư chứng khoán đại chúng phải thành lập bộ phận kiểm toán nội bộ, trực thuộc Hội đồng quản trị, Hội đồng thành viên hoặc chủ sở hữu công ty; kế hoạch kiểm toán nội bộ hằng năm do cấp này phê duyệt. Bộ phận kiểm soát nội bộ (Điều 6) thì khác: tối thiểu 01 người có bằng đại học luật và 01 người có chuyên môn kế toán, kiểm toán; thay đổi nhân sự kiểm soát nội bộ phải thông báo UBCKNN trong 07 ngày làm việc. Nội dung slide 2025 trang 11–12 phù hợp.",
    "Khoản 1 Điều 5, khoản 4, 5 Điều 6 Thông tư 99/2020/TT-BTC. Trích bản tiếng Anh của UBCKNN vì bản tiếng Việt TT 99 trong thư mục là ảnh chụp, không có lớp chữ",
    "Fund management companies that are public companies or the companies managing public funds, public securities investment companies must establish an internal audit department. The internal audit department is under the Board of Directors or the Members’ Council or the company owner.", TT99E)

add("CTCK & CTQLQ", 1,
    "Khi quản lý danh mục đầu tư cho khách hàng ủy thác, theo Luật Chứng khoán công ty quản lý quỹ đầu tư chứng khoán phải:",
    ["Lưu ký toàn bộ tài sản ủy thác, tách biệt tới từng khách hàng và với tài sản của công ty",
     "Lưu ký tài sản ủy thác tại chính công ty, gộp chung một tài khoản để giảm chi phí",
     "Chỉ lưu ký chứng khoán niêm yết; tiền của khách hàng giữ tại tài khoản của công ty",
     "Ghi nhận tài sản ủy thác là tài sản của công ty cho đến khi tất toán hợp đồng"], 0,
    "Khoản 4 Điều 90: khi quản lý tài sản ủy thác, công ty quản lý quỹ phải lưu ký toàn bộ tài sản ủy thác, bảo đảm nguyên tắc độc lập và tách biệt tới từng khách hàng ủy thác, tách biệt tài sản ủy thác với tài sản của công ty. Khoản 2, 3 Điều 88: tài sản của khách hàng ủy thác trên tài khoản lưu ký của công ty quản lý quỹ thuộc sở hữu của khách hàng, không phải tài sản của công ty; khi công ty giải thể, phá sản, tài sản này được hoàn trả cho khách hàng sau khi trừ nghĩa vụ nợ của khách hàng với công ty. Khớp nội dung 'tách biệt tài sản' trên slide 2025 trang 18.",
    "Khoản 4 Điều 90, khoản 2, 3 Điều 88 " + VB24,
    "4. Khi quản lý tài sản ủy thác, công ty quản lý quỹ đầu tư chứng khoán phải lưu ký toàn bộ tài sản ủy thác, bảo đảm nguyên tắc độc lập và tách biệt tới từng khách hàng ủy thác, tách biệt tài sản ủy thác và tài sản của công ty quản lý quỹ đầu tư chứng khoán.", LCK)

add("Sở hữu nước ngoài", 1,
    "Theo Nghị định 155/2020/NĐ-CP (sửa đổi bởi Nghị định 245/2025/NĐ-CP), nhà đầu tư nước ngoài đầu tư vào chứng chỉ quỹ và cổ phiếu của công ty đầu tư chứng khoán với tỷ lệ sở hữu:",
    ["Không hạn chế, trừ trường hợp pháp luật có liên quan quy định khác",
     "Tối đa 49% số chứng chỉ quỹ, cổ phiếu đang lưu hành",
     "Tối đa 50% số chứng chỉ quỹ, cổ phiếu có quyền biểu quyết",
     "Theo tỷ lệ sở hữu nước ngoài thấp nhất của cổ phiếu trong danh mục"], 0,
    "Khoản 3 Điều 139 NĐ 155/2020 (NĐ 245/2025 chỉ sửa khoản 2, khoản 5 Điều 139): nhà đầu tư nước ngoài được đầu tư không hạn chế vào công cụ nợ của Chính phủ, trái phiếu được Chính phủ bảo lãnh, trái phiếu chính quyền địa phương, trái phiếu doanh nghiệp, chứng chỉ quỹ, cổ phiếu của công ty đầu tư chứng khoán, chứng khoán phái sinh, chứng chỉ lưu ký, chứng quyền có bảo đảm, trừ trường hợp pháp luật liên quan quy định khác. Các mức 49%, 50% là giới hạn đối với cổ phiếu công ty đại chúng theo ngành nghề (khoản 1, 2). Slide 2025 trang 24 ghi các quỹ 'không chịu giới hạn tỷ lệ sở hữu nước ngoài' là đúng.",
    "Khoản 3 Điều 139 Nghị định 155/2020/NĐ-CP (Nghị định 245/2025/NĐ-CP chỉ sửa khoản 2, khoản 5 Điều 139)",
    "3. Nhà đầu tư nước ngoài được đầu tư không hạn chế vào công cụ nợ của Chính phủ, trái phiếu được Chính phủ bảo lãnh và trái phiếu chính quyền địa phương, trái phiếu doanh nghiệp, chứng chỉ quỹ, cổ phiếu của công ty đầu tư chứng khoán", ND155)

# ---------- Chuyên đề 9: QLNN, thanh tra, giám sát, xử phạt ----------
add("Giám sát & an ninh thị trường", 1,
    "Theo Luật Chứng khoán, cơ quan nào thống nhất quản lý nhà nước về chứng khoán và thị trường chứng khoán?",
    ["Chính phủ", "Quốc hội", "Bộ Tài chính", "Ủy ban Chứng khoán Nhà nước"], 0,
    "Khoản 1 Điều 8: Chính phủ thống nhất quản lý nhà nước về chứng khoán và thị trường chứng khoán. Bộ Tài chính chịu trách nhiệm trước Chính phủ thực hiện quản lý nhà nước (khoản 2 Điều 8); UBCKNN là cơ quan thuộc Bộ Tài chính, tham mưu, giúp Bộ trưởng quản lý nhà nước và tổ chức thực thi pháp luật về chứng khoán (Điều 9). Quốc hội ban hành luật và giám sát tối cao, không phải cơ quan quản lý nhà nước chuyên ngành.",
    "Khoản 1, 2 Điều 8, Điều 9 " + VB24,
    "1. Chính phủ thống nhất quản lý nhà nước về chứng khoán và thị trường chứng khoán.", LCK)

add("Thanh tra & xử lý vi phạm", 2,
    "Theo Luật Chứng khoán, trường hợp vụ việc vi phạm hành chính vượt thẩm quyền xử phạt của mình, Thanh tra chứng khoán thực hiện việc nào sau đây?",
    ["Kiến nghị Chủ tịch Ủy ban Chứng khoán Nhà nước quyết định việc xử phạt",
     "Chuyển hồ sơ cho Sở giao dịch chứng khoán Việt Nam ra quyết định xử phạt",
     "Đề nghị Tòa án nhân dân có thẩm quyền ra quyết định xử phạt hành chính",
     "Báo cáo Thanh tra Chính phủ để Tổng Thanh tra Chính phủ ra quyết định"], 0,
    "Điểm b khoản 4 Điều 129: Thanh tra chứng khoán xử phạt vi phạm hành chính theo thẩm quyền hoặc kiến nghị Chủ tịch UBCKNN quyết định việc xử phạt theo pháp luật về xử lý vi phạm hành chính. Chủ tịch UBCKNN có thẩm quyền xử phạt cao nhất trong lĩnh vực (khoản 6 Điều 132; khoản 2 Điều 47 NĐ 156/2020). Sở giao dịch chứng khoán không có thẩm quyền xử phạt; Tòa án không ra quyết định xử phạt hành chính. Lưu ý: Luật Thanh tra 2025 đã tổ chức lại hệ thống cơ quan thanh tra; Điều 129 Luật Chứng khoán chưa được sửa (khoản 2 Điều 62 Luật Thanh tra 2025 yêu cầu sửa trước 01/3/2027), còn NĐ 306/2025 vẫn quy định thẩm quyền của Chánh Thanh tra, Trưởng đoàn thanh tra Thanh tra Chứng khoán Nhà nước.",
    "Điểm b khoản 4 Điều 129, khoản 6 Điều 132 " + VB24,
    "b) Xử phạt vi phạm hành chính theo thẩm quyền hoặc kiến nghị Chủ tịch Ủy ban Chứng khoán Nhà nước quyết định việc xử phạt vi phạm hành chính theo quy định của pháp luật về xử lý vi phạm hành chính;", LCK)

add("Thanh tra & xử lý vi phạm", 2,
    "Theo Luật Thanh tra số 84/2025/QH15 (hiệu lực 01/7/2025), cơ quan nào sau đây KHÔNG thuộc danh sách cơ quan thanh tra?",
    ["Thanh tra Chính phủ", "Thanh tra tỉnh, thành phố", "Thanh tra Ngân hàng Nhà nước", "Thanh tra Bộ Tài chính"], 3,
    "Điều 7 Luật Thanh tra 2025: cơ quan thanh tra gồm Thanh tra Chính phủ; Thanh tra tỉnh, thành phố; cơ quan thanh tra trong Quân đội nhân dân, Công an nhân dân, Ngân hàng Nhà nước (Thanh tra Bộ Quốc phòng, Thanh tra Bộ Công an, Thanh tra Ngân hàng Nhà nước…); Thanh tra Cơ yếu và thanh tra thành lập theo điều ước quốc tế. Luật này thay Luật Thanh tra 2022 mà slide 2025 còn trích: bỏ thanh tra bộ ở các bộ khác, thanh tra sở, thanh tra huyện, thanh tra Tổng cục, Cục và mô hình cơ quan được giao thực hiện chức năng thanh tra chuyên ngành; thủ trưởng cơ quan quản lý nhà nước tổ chức kiểm tra chuyên ngành (Điều 61).",
    "Điều 7, Điều 61, Điều 63 Luật Thanh tra số 84/2025/QH15 (hiệu lực 01/7/2025, thay thế Luật Thanh tra số 11/2022/QH15)",
    "Điều 7. Cơ quan thanh tra 1. Thanh tra Chính phủ. 2. Thanh tra tỉnh, thành phố (sau đây gọi chung là Thanh tra tỉnh). 3. Cơ quan thanh tra trong Quân đội nhân dân, Công an nhân dân, Ngân hàng Nhà nước Việt Nam, bao gồm Thanh tra Bộ Quốc phòng, Thanh tra Bộ Công an, Thanh tra Ngân hàng Nhà nước", LTT)

add("Thanh tra & xử lý vi phạm", 1,
    "Theo Luật Thanh tra số 84/2025/QH15, thời hạn thực hiện một cuộc thanh tra do Thanh tra tỉnh tiến hành là:",
    ["Không quá 45 ngày; phức tạp có thể gia hạn một lần không quá 25 ngày",
     "Không quá 45 ngày; phức tạp có thể gia hạn một lần không quá 30 ngày",
     "Không quá 60 ngày; phức tạp có thể gia hạn một lần không quá 30 ngày",
     "Không quá 30 ngày; phức tạp có thể gia hạn một lần không quá 10 ngày"], 0,
    "Điểm b khoản 1 Điều 20: cuộc thanh tra do Thanh tra Bộ Quốc phòng, Thanh tra Bộ Công an, Thanh tra Ngân hàng Nhà nước, Thanh tra tỉnh tiến hành không quá 45 ngày; phức tạp hoặc ở miền núi, biên giới, hải đảo, vùng sâu, vùng xa có thể gia hạn một lần không quá 25 ngày. Thanh tra Chính phủ: không quá 60 ngày, gia hạn lần một không quá 30 ngày, đặc biệt phức tạp gia hạn lần hai không quá 20 ngày; Thanh tra Cơ yếu và các cơ quan thanh tra khác: 30 ngày, gia hạn không quá 10 ngày. Mức '45 ngày, gia hạn không quá 30 ngày' trên slide 2025 là của Luật Thanh tra 2022, đã hết hiệu lực. Thời gian tạm dừng thanh tra không tính vào thời hạn.",
    "Điểm b khoản 1, khoản 2 Điều 20 Luật Thanh tra số 84/2025/QH15",
    "b) Cuộc thanh tra do Thanh tra Bộ Quốc phòng, Thanh tra Bộ Công an, Thanh tra Ngân hàng Nhà nước, Thanh tra tỉnh tiến hành không quá 45 ngày; trường hợp phức tạp hoặc ở miền núi, biên giới, hải đảo, vùng sâu, vùng xa đi lại khó khăn thì có thể gia hạn một lần không quá 25 ngày;", LTT)

add("Giám sát & an ninh thị trường", 2,
    "Theo Thông tư 95/2020/TT-BTC (sửa đổi bởi Thông tư 138/2025/TT-BTC), tiêu chí giám sát giao dịch chứng khoán và chỉ tiêu báo cáo giám sát giao dịch áp dụng cho thành viên giao dịch được xây dựng và chấp thuận như thế nào?",
    ["Sở giao dịch chứng khoán Việt Nam xây dựng, Ủy ban Chứng khoán Nhà nước chấp thuận",
     "Ủy ban Chứng khoán Nhà nước xây dựng, Bộ trưởng Bộ Tài chính phê duyệt ban hành",
     "Từng công ty chứng khoán thành viên tự xây dựng, Hội đồng quản trị công ty phê duyệt",
     "Tổng công ty lưu ký và bù trừ chứng khoán xây dựng, Sở giao dịch chứng khoán chấp thuận"], 0,
    "Khoản 4 Điều 4 TT 95 (sửa bởi TT 138/2025): UBCKNN chấp thuận tiêu chí giám sát giao dịch, chỉ tiêu báo cáo giám sát giao dịch áp dụng cho thành viên giao dịch do Sở giao dịch chứng khoán Việt Nam xây dựng; Điều 9: Sở giao dịch chứng khoán Việt Nam xây dựng, ban hành hệ thống tiêu chí giám sát cho các công ty con (Sở giao dịch Hà Nội, TP. Hồ Chí Minh) và chỉ tiêu báo cáo cho thành viên. VSDC xây dựng phương pháp xác định mức ký quỹ, tần suất giám sát ký quỹ (cũng do UBCKNN chấp thuận). Đây là 'tuyến 2' trên slide 2025.",
    "Khoản 4 Điều 4, Điều 9 " + VB13,
    "Chấp thuận tiêu chí giám sát giao dịch chứng khoán, chỉ tiêu báo cáo giám sát giao dịch áp dụng cho thành viên giao dịch do Sở giao dịch chứng khoán Việt Nam xây dựng;", TT95)

add("Giám sát & an ninh thị trường", 2,
    "Theo Thông tư 95/2020/TT-BTC (sửa đổi bởi Thông tư 138/2025/TT-BTC), trong công tác giám sát giao dịch chứng khoán, thành viên giao dịch (công ty chứng khoán) có trách nhiệm:",
    ["Giám sát giao dịch của nhà đầu tư, kịp thời cảnh báo nhà đầu tư và báo cáo Sở giao dịch",
     "Ban hành tiêu chí giám sát và xác định giao dịch nghi vấn trên toàn thị trường",
     "Ra quyết định xử phạt hành chính đối với nhà đầu tư có giao dịch bất thường",
     "Giám sát giới hạn vị thế, ký quỹ, bù trừ và thanh toán cho toàn thị trường"], 0,
    "Khoản 6 Điều 3a TT 95 (bổ sung bởi Điều 2 TT 138/2025): thành viên giao dịch giám sát hoạt động giao dịch của nhà đầu tư, kịp thời phát hiện, cảnh báo nhà đầu tư và báo cáo Sở giao dịch chứng khoán Việt Nam và công ty con – 'tuyến 1' trên slide 2025. Sở giao dịch chứng khoán xác định giao dịch nghi vấn (khoản 3, 4); VSDC giám sát bù trừ, thanh toán, giới hạn vị thế, ký quỹ (khoản 5); UBCKNN làm rõ và xử lý vi phạm (khoản 2). Từ 09/01/2026, công ty chứng khoán không thực hiện giám sát giao dịch có thể bị phạt 300–400 triệu đồng (khoản 5b Điều 26 NĐ 156, bổ sung bởi NĐ 306/2025).",
    "Khoản 6 Điều 3a " + VB13,
    "6. Thành viên giao dịch có trách nhiệm giám sát hoạt động giao dịch của nhà đầu tư; kịp thời phát hiện, cảnh báo nhà đầu tư và báo cáo Sở giao dịch chứng khoán Việt Nam và công ty con theo quy định.", TT95)

add("Giám sát & an ninh thị trường", 2,
    "Theo Thông tư 95/2020/TT-BTC (sửa đổi bởi Thông tư 138/2025/TT-BTC), “giao dịch nghi vấn” được hiểu là:",
    ["Giao dịch bất thường được Sở giao dịch phân tích, xác định có dấu hiệu vi phạm pháp luật",
     "Mọi giao dịch chạm tiêu chí cảnh báo của hệ thống giám sát do Sở giao dịch ban hành",
     "Giao dịch đã bị UBCKNN kết luận vi phạm và ra quyết định xử phạt vi phạm hành chính",
     "Giao dịch có khối lượng vượt bình quân 20 phiên gần nhất của chứng khoán niêm yết"], 0,
    "Khoản 2, 3 Điều 3 TT 95: giao dịch bất thường là giao dịch chạm tiêu chí cảnh báo của hệ thống tiêu chí giám sát do Sở giao dịch chứng khoán Việt Nam ban hành; giao dịch nghi vấn là giao dịch bất thường được Sở giao dịch chứng khoán Việt Nam và công ty con phân tích, xác định có dấu hiệu vi phạm quy định về giao dịch chứng khoán. Sở giao dịch báo cáo giao dịch nghi vấn cho UBCKNN để phân tích, làm rõ và xử lý (Điều 3a, Điều 5). Giao dịch đã có quyết định xử phạt là vi phạm đã được xác định, không còn là 'nghi vấn'.",
    "Khoản 2, 3 Điều 3 " + VB13,
    "3. Giao dịch nghi vấn là các giao dịch bất thường được Sở giao dịch chứng khoán Việt Nam và công ty con phân tích, xác định là giao dịch có dấu hiệu vi phạm quy định của pháp luật về giao dịch chứng khoán.", TT95)

add("SGDCK & VSDC", 1,
    "Công ty chứng khoán K là thành viên lưu ký. Theo Luật Chứng khoán, chủ thể có nghĩa vụ giám sát việc tuân thủ nghĩa vụ thành viên của K, đồng thời giám sát tỷ lệ sở hữu của nhà đầu tư nước ngoài, là:",
    ["Tổng công ty lưu ký và bù trừ chứng khoán Việt Nam", "Sở giao dịch chứng khoán Việt Nam và công ty con",
     "Ngân hàng Nhà nước, qua Cục Quản lý ngoại hối", "Hiệp hội Kinh doanh chứng khoán Việt Nam"], 0,
    "Điểm c khoản 2 Điều 55: VSDC giám sát hoạt động đăng ký, lưu ký, bù trừ, thanh toán; giám sát tỷ lệ sở hữu của nhà đầu tư nước ngoài; giám sát việc tuân thủ nghĩa vụ của thành viên VSDC (thành viên lưu ký, thành viên bù trừ). Sở giao dịch chứng khoán giám sát hoạt động giao dịch, việc tuân thủ nghĩa vụ của thành viên giao dịch và công bố thông tin của tổ chức niêm yết, đăng ký giao dịch (điểm c khoản 2 Điều 46). Phân chia trên slide 2025 trang 20 là đúng.",
    "Điểm c khoản 2 Điều 55 " + VB24,
    "c) Giám sát hoạt động đăng ký, lưu ký, bù trừ và thanh toán giao dịch chứng khoán; giám sát tỷ lệ sở hữu của nhà đầu tư nước ngoài theo quy định của pháp luật về chứng khoán và thị trường chứng khoán; giám sát việc tuân thủ nghĩa vụ của thành viên", LCK)

add("Xử phạt vi phạm", 2,
    "Theo Nghị định 156/2020/NĐ-CP (sửa đổi, bổ sung bởi Nghị định 306/2025/NĐ-CP, hiệu lực 09/01/2026), công ty chứng khoán không thực hiện giám sát giao dịch chứng khoán theo quy định, không báo cáo khi phát hiện giao dịch có dấu hiệu vi phạm pháp luật thì bị phạt tiền:",
    ["Từ 300 triệu đồng đến 400 triệu đồng", "Từ 70 triệu đồng đến 100 triệu đồng",
     "Từ 100 triệu đồng đến 150 triệu đồng", "Từ 400 triệu đồng đến 500 triệu đồng"], 0,
    "Khoản 5b Điều 26 NĐ 156 (bổ sung bởi điểm g khoản 10 Điều 1 NĐ 306/2025): phạt 300–400 triệu đồng đối với công ty chứng khoán không thực hiện giám sát giao dịch theo quy định; không báo cáo khi phát hiện giao dịch có dấu hiệu vi phạm; không lập, gửi báo cáo bất thường, báo cáo theo yêu cầu của UBCKNN, Sở giao dịch. Trước 09/01/2026 hành vi này nằm ở điểm g khoản 2 Điều 26 với khung 70–100 triệu đồng; NĐ 306 đã thay điểm g khoản 2 bằng hành vi khác. Mức phạt này áp dụng cho tổ chức.",
    "Khoản 5b Điều 26 Nghị định 156/2020/NĐ-CP (bổ sung bởi điểm g khoản 10 Điều 1 Nghị định 306/2025/NĐ-CP); điểm g khoản 2 Điều 26 (sửa đổi bởi điểm b khoản 10 Điều 1 Nghị định 306/2025/NĐ-CP)",
    "5b. Phạt tiền từ 300.000.000 đồng đến 400.000.000 đồng đối với công ty chứng khoán không thực hiện giám sát giao dịch chứng khoán theo quy định; không thực hiện báo cáo khi phát hiện giao dịch chứng khoán có dấu hiệu vi phạm các quy định pháp luật về chứng khoán;", ND306)

add("Xử phạt vi phạm", 1,
    "Theo Luật Xử lý vi phạm hành chính (văn bản hợp nhất năm 2026) và Nghị định 156/2020/NĐ-CP, thời hiệu xử phạt vi phạm hành chính trong lĩnh vực chứng khoán là:",
    ["01 năm", "02 năm", "03 năm", "05 năm"], 1,
    "Điểm a khoản 1 Điều 6 Luật Xử lý vi phạm hành chính (VBHN 90/VBHN-VPQH năm 2026): thời hiệu xử phạt là 01 năm, trừ một số lĩnh vực (kế toán, hóa đơn, kinh doanh bảo hiểm, quản lý giá, chứng khoán, sở hữu trí tuệ, xây dựng…) có thời hiệu 02 năm; khoản 1 Điều 6 NĐ 156/2020 (sửa bởi NĐ 128/2021) dẫn chiếu quy định này. Hành vi đã kết thúc: thời hiệu tính từ thời điểm chấm dứt; hành vi đang thực hiện: tính từ thời điểm phát hiện. 03 năm là thời hiệu khởi kiện yêu cầu bồi thường thiệt hại theo Bộ luật Dân sự.",
    "Điểm a, b khoản 1 Điều 6 Luật Xử lý vi phạm hành chính 2012 (VBHN 90/VBHN-VPQH năm 2026, hợp nhất đến Luật 88/2025/QH15); khoản 1 Điều 6 Nghị định 156/2020/NĐ-CP (sửa đổi bởi Nghị định 128/2021/NĐ-CP)",
    "Thời hiệu xử phạt vi phạm hành chính là 01 năm, trừ các trường hợp sau đây: Vi phạm hành chính về kế toán; hóa đơn; phí, lệ phí; kinh doanh bảo hiểm; quản lý giá; chứng khoán;", XLVPHC)

add("Xử phạt vi phạm", 2,
    "Ba nhà đầu tư A, B, C cùng thực hiện một hành vi vi phạm hành chính trong lĩnh vực chứng khoán (chưa đến mức truy cứu trách nhiệm hình sự). Theo nguyên tắc xử phạt của Luật Xử lý vi phạm hành chính:",
    ["Mỗi người A, B, C đều bị xử phạt về hành vi vi phạm đó",
     "Chỉ người khởi xướng bị phạt tiền, hai người còn lại bị cảnh cáo",
     "Cả ba bị xử phạt chung một lần, tiền phạt chia đều cho ba người",
     "Chỉ xử phạt người thu được khoản lợi bất hợp pháp lớn nhất"], 0,
    "Điểm d khoản 1 Điều 3 Luật Xử lý vi phạm hành chính: một hành vi vi phạm hành chính chỉ bị xử phạt một lần; nhiều người cùng thực hiện một hành vi thì mỗi người vi phạm đều bị xử phạt về hành vi đó; một người thực hiện nhiều hành vi hoặc vi phạm nhiều lần thì bị xử phạt về từng hành vi, trừ khi Chính phủ quy định vi phạm nhiều lần là tình tiết tăng nặng. Các nguyên tắc này trên slide 2025 vẫn đúng.",
    "Điểm d khoản 1 Điều 3 Luật Xử lý vi phạm hành chính 2012 (VBHN 90/VBHN-VPQH năm 2026)",
    "Một hành vi vi phạm hành chính chỉ bị xử phạt một lần. Nhiều người cùng thực hiện một hành vi vi phạm hành chính thì mỗi người vi phạm đều bị xử phạt về hành vi vi phạm hành chính đó.", XLVPHC)

add("Xử phạt vi phạm", 1,
    "Theo Nghị định 156/2020/NĐ-CP (sửa đổi bởi Nghị định 306/2025/NĐ-CP, hiệu lực 09/01/2026), hình thức xử phạt chính “đình chỉ hoạt động giao dịch chứng khoán” được áp dụng với thời hạn:",
    ["Từ 01 tháng đến 24 tháng", "Từ 01 tháng đến 12 tháng", "Từ 03 tháng đến 06 tháng", "Từ 06 tháng đến 36 tháng"], 0,
    "Điểm c khoản 1 Điều 4 NĐ 156 (sửa bởi điểm a khoản 2 Điều 1 NĐ 306/2025): đình chỉ hoạt động giao dịch chứng khoán có thời hạn từ 01 tháng đến 24 tháng; điểm a khoản 2 Điều 4 cũng nâng thời hạn đình chỉ (hình thức bổ sung) các hoạt động chào mua công khai, kinh doanh, dịch vụ chứng khoán, bảo lãnh, lưu ký, bù trừ… lên 01–24 tháng. Mức 01–12 tháng trên slide 2025 là quy định trước ngày 09/01/2026 (NĐ 156, NĐ 128). Tước quyền sử dụng chứng chỉ hành nghề vẫn là 01–24 tháng.",
    "Điểm c khoản 1, điểm a khoản 2 Điều 4 Nghị định 156/2020/NĐ-CP (sửa đổi bởi khoản 3 Điều 1 Nghị định 128/2021/NĐ-CP và khoản 2 Điều 1 Nghị định 306/2025/NĐ-CP)",
    "c) Đình chỉ hoạt động giao dịch chứng khoán có thời hạn từ 01 tháng đến 24 tháng;", ND306)

add("Xử phạt vi phạm", 2,
    "Theo Điều 47 Nghị định 156/2020/NĐ-CP (sửa đổi bởi Nghị định 128/2021/NĐ-CP và Nghị định 306/2025/NĐ-CP), chức danh nào sau đây KHÔNG có thẩm quyền xử phạt vi phạm hành chính trong lĩnh vực chứng khoán?",
    ["Giám đốc Sở Tài chính tỉnh, thành phố", "Chủ tịch Ủy ban nhân dân cấp tỉnh",
     "Trưởng đoàn kiểm tra do Chủ tịch UBCKNN lập", "Bộ trưởng Bộ Tài chính, cơ quan chủ quản UBCKNN"], 3,
    "Điều 47 NĐ 156 hiện hành: khoản 1 (sửa bởi NĐ 306/2025) – Giám đốc Sở Tài chính, Chánh Thanh tra Chứng khoán Nhà nước, Trưởng đoàn kiểm tra do Chủ tịch UBCKNN thành lập (phạt đến 2,4 tỷ đồng với tổ chức, 1,2 tỷ đồng với cá nhân); khoản 1a – Trưởng đoàn thanh tra Thanh tra Chứng khoán Nhà nước (1,5 tỷ/750 triệu đồng); khoản 2 – Chủ tịch UBCKNN; khoản 3 – Chủ tịch UBND cấp tỉnh (đến 3 tỷ/1,5 tỷ đồng, hoặc 10 lần/05 lần khoản thu trái pháp luật với nội gián, thao túng). Bộ trưởng Bộ Tài chính không có tên trong danh sách. Slide 2025 chưa có Giám đốc Sở Tài chính, Trưởng đoàn kiểm tra và còn ghi mức 100/50 triệu đồng cho Chánh Thanh tra.",
    "Khoản 1, 1a Điều 47 Nghị định 156/2020/NĐ-CP (sửa đổi, bổ sung bởi khoản 19 Điều 1 Nghị định 306/2025/NĐ-CP); khoản 2, 3 Điều 47 (điểm d sửa đổi bởi khoản 37 Điều 1 Nghị định 128/2021/NĐ-CP)",
    "1. Giám đốc Sở Tài chính, Chánh Thanh tra Chứng khoán Nhà nước, Trưởng đoàn kiểm tra do Chủ tịch Ủy ban Chứng khoán Nhà nước thành lập có quyền: a) Cảnh cáo; b) Phạt tiền tối đa đến 2.400.000.000 đồng đối với tổ chức và phạt tiền tối đa đến 1.200.000.000 đồng đối với cá nhân;", ND306)

add("Xử phạt vi phạm", 2,
    "Theo khoản 1a Điều 47 Nghị định 156/2020/NĐ-CP (bổ sung bởi Nghị định 306/2025/NĐ-CP), Trưởng đoàn thanh tra Thanh tra Chứng khoán Nhà nước có quyền nào sau đây?",
    ["Phạt tiền đến 750 triệu đồng đối với cá nhân, 1,5 tỷ đồng đối với tổ chức",
     "Phạt tiền đến 1,2 tỷ đồng đối với cá nhân, 2,4 tỷ đồng đối với tổ chức",
     "Tước quyền sử dụng chứng chỉ hành nghề chứng khoán có thời hạn",
     "Đình chỉ hoạt động giao dịch chứng khoán có thời hạn của nhà đầu tư"], 0,
    "Khoản 1a Điều 47 (bổ sung bởi khoản 19 Điều 1 NĐ 306/2025): Trưởng đoàn thanh tra Thanh tra Chứng khoán Nhà nước được cảnh cáo; phạt tiền đến 1,5 tỷ đồng với tổ chức và 750 triệu đồng với cá nhân; tịch thu tang vật, phương tiện vi phạm; áp dụng biện pháp khắc phục hậu quả. Khoản này không trao quyền tước chứng chỉ hành nghề hay đình chỉ giao dịch – các quyền đó thuộc các chức danh ở khoản 1 (mức 2,4 tỷ/1,2 tỷ đồng), Chủ tịch UBCKNN, Chủ tịch UBND cấp tỉnh. Slide 2025 còn ghi Trưởng đoàn thanh tra chuyên ngành chỉ phạt đến 100/50 triệu đồng.",
    "Khoản 1a Điều 47 Nghị định 156/2020/NĐ-CP (bổ sung bởi khoản 19 Điều 1 Nghị định 306/2025/NĐ-CP)",
    "1a. Trưởng đoàn thanh tra Thanh tra Chứng khoán Nhà nước có quyền: a) Cảnh cáo; b) Phạt tiền tối đa đến 1.500.000.000 đồng đối với tổ chức và phạt tiền tối đa đến 750.000.000 đồng đối với cá nhân;", ND306)

add("Xử phạt vi phạm", 2,
    "Theo Nghị định 156/2020/NĐ-CP (sửa đổi bởi Nghị định 306/2025/NĐ-CP), trừ các trường hợp được quy định riêng, thời hạn thực hiện biện pháp khắc phục hậu quả trong lĩnh vực chứng khoán là:",
    ["Tối đa 30 ngày kể từ ngày quyết định áp dụng biện pháp có hiệu lực thi hành",
     "Tối đa 60 ngày kể từ ngày lập biên bản vi phạm hành chính",
     "Tối đa 15 ngày kể từ ngày nhận được quyết định xử phạt",
     "Tối đa 06 tháng kể từ ngày ban hành quyết định xử phạt"], 0,
    "Khoản 3 Điều 51 NĐ 156 (sửa bởi điểm a khoản 23 Điều 1 NĐ 306/2025): thời hạn thực hiện biện pháp khắc phục hậu quả là tối đa 30 ngày kể từ ngày quyết định áp dụng có hiệu lực thi hành, trừ một số trường hợp được liệt kê (ví dụ phải thông qua Đại hội đồng cổ đông gần nhất, hoặc khắc phục trong 06 tháng liên tiếp); tổ chức, cá nhân phải báo cáo kết quả cho người ra quyết định trong tối đa 03 ngày làm việc sau khi hết thời hạn. Riêng buộc hoàn trả tiền, chứng khoán của khách hàng có thời hạn tối đa 60 ngày (Điều 26, Điều 32).",
    "Khoản 3 Điều 51 Nghị định 156/2020/NĐ-CP (sửa đổi bởi điểm a khoản 23 Điều 1 Nghị định 306/2025/NĐ-CP)",
    "3. Thời hạn thực hiện các biện pháp khắc phục hậu quả quy định tại khoản 3 Điều 4 Nghị định này là tối đa 30 ngày, kể từ ngày quyết định áp dụng biện pháp khắc phục hậu quả có hiệu lực thi hành,", ND306)

add("Xử phạt vi phạm", 3,
    "Ông D là người hành nghề chứng khoán, cho người khác thuê chứng chỉ hành nghề chứng khoán của mình (chưa đến mức truy cứu trách nhiệm hình sự). Theo Nghị định 156/2020/NĐ-CP (sửa đổi bởi Nghị định 128/2021/NĐ-CP và Nghị định 306/2025/NĐ-CP), ông D có thể bị xử phạt:",
    ["Phạt 100–150 triệu đồng, tước CCHN 01–03 tháng, buộc nộp lại số lợi bất hợp pháp",
     "Phạt 200–300 triệu đồng, tước CCHN 01–03 tháng, buộc nộp lại số lợi bất hợp pháp",
     "Phạt 50–75 triệu đồng, tước CCHN 01–03 tháng, buộc nộp lại số lợi bất hợp pháp",
     "Phạt 100–150 triệu đồng, tước CCHN 18–24 tháng, tịch thu chứng chỉ hành nghề"], 0,
    "Điểm a khoản 4 Điều 32 NĐ 156: mượn, thuê hoặc cho mượn, cho thuê chứng chỉ hành nghề; NĐ 306/2025 nâng khung của khoản 4 lên 200–300 triệu đồng. Điểm c khoản 3 Điều 5 (sửa bởi NĐ 128/2021): mức phạt tại Chương II áp dụng cho tổ chức, cá nhân vi phạm như tổ chức bị phạt bằng 1/2 (Điều 32 không thuộc ngoại lệ), nên với cá nhân ông D là 100–150 triệu đồng. Hình thức bổ sung: tước chứng chỉ hành nghề 01–03 tháng (điểm a khoản 7); biện pháp khắc phục: buộc nộp lại số lợi bất hợp pháp từ việc cho thuê (điểm a khoản 8). 200–300 triệu là quên chia đôi; 50–75 triệu là chia đôi khung cũ 100–150 triệu (trước 09/01/2026); 18–24 tháng là mức tước với thao túng, nội gián.",
    "Điểm a khoản 4 Điều 32 (tiêu đề khoản 4 sửa đổi bởi điểm d khoản 12 Điều 1 Nghị định 306/2025/NĐ-CP), điểm a khoản 7, điểm a khoản 8 Điều 32 (sửa đổi bởi khoản 26 Điều 1 Nghị định 128/2021/NĐ-CP), điểm c khoản 3 Điều 5 Nghị định 156/2020/NĐ-CP (sửa đổi bởi khoản 4 Điều 1 Nghị định 128/2021/NĐ-CP)",
    "Trường hợp cá nhân có hành vi vi phạm như của tổ chức thì mức phạt tiền bằng 1/2 mức phạt tiền đối với tổ chức.", ND128)

# ---------- Chuyên đề 10: tranh chấp, khiếu nại, tố cáo, bồi thường ----------
add(TP_TC, 3,
    "Do lỗi hệ thống của công ty chứng khoán X, lệnh bán của nhà đầu tư N không được thực hiện, gây thiệt hại 500 triệu đồng. Trong đó 100 triệu đồng là thiệt hại tăng thêm vì N đã biết sự cố nhưng không áp dụng biện pháp cần thiết, hợp lý để hạn chế thiệt hại. Theo Bộ luật Dân sự 2015, nhận định nào đúng?",
    ["X bồi thường 400 triệu đồng; N không được bồi thường phần thiệt hại do không tự hạn chế",
     "X bồi thường toàn bộ 500 triệu đồng vì lỗi ban đầu thuộc về X",
     "X không phải bồi thường vì N cũng có lỗi trong việc để thiệt hại xảy ra",
     "X bồi thường 250 triệu đồng vì hai bên cùng có lỗi ngang nhau"], 0,
    "Khoản 2 Điều 133 Luật Chứng khoán: chủ thể xâm phạm quyền, lợi ích hợp pháp trong hoạt động chứng khoán mà gây thiệt hại phải bồi thường theo thỏa thuận, Bộ luật Dân sự và pháp luật liên quan. Bộ luật Dân sự: bên có quyền phải áp dụng biện pháp cần thiết, hợp lý để hạn chế thiệt hại (Điều 362); thiệt hại do một phần lỗi của bên bị vi phạm thì bên vi phạm chỉ bồi thường tương ứng mức độ lỗi của mình (Điều 363); với bồi thường ngoài hợp đồng, bên bị thiệt hại không được bồi thường phần thiệt hại xảy ra do không áp dụng biện pháp cần thiết, hợp lý để hạn chế (khoản 5 Điều 585). Vì vậy X bồi thường 500 − 100 = 400 triệu đồng; không chia đôi khi đã xác định được phần thiệt hại do mỗi bên gây ra.",
    "Điều 362, 363, khoản 1 và khoản 5 Điều 585 Bộ luật Dân sự 2015 (91/2015/QH13); khoản 2 Điều 133 Luật Chứng khoán 2019 (VBHN 24/VBHN-VPQH năm 2025)",
    "5. Bên có quyền, lợi ích bị xâm phạm không được bồi thường nếu thiệt hại xảy ra do không áp dụng các biện pháp cần thiết, hợp lý để ngăn chặn, hạn chế thiệt hại cho chính mình.", BLDS)

add(TP_TC, 1,
    "Nhà đầu tư cho rằng một công ty chứng khoán đã xâm phạm quyền, lợi ích hợp pháp của mình và gây thiệt hại ngoài hợp đồng. Theo Bộ luật Dân sự 2015, thời hiệu khởi kiện yêu cầu bồi thường thiệt hại là:",
    ["03 năm kể từ ngày người có quyền yêu cầu biết hoặc phải biết quyền lợi bị xâm phạm",
     "02 năm kể từ ngày xảy ra hành vi vi phạm gây thiệt hại",
     "01 năm kể từ ngày phát hiện ra thiệt hại thực tế",
     "05 năm kể từ ngày chấm dứt hành vi vi phạm gây thiệt hại"], 0,
    "Điều 588 Bộ luật Dân sự 2015: thời hiệu khởi kiện yêu cầu bồi thường thiệt hại là 03 năm, kể từ ngày người có quyền yêu cầu biết hoặc phải biết quyền, lợi ích hợp pháp của mình bị xâm phạm; tranh chấp hợp đồng cũng có thời hiệu khởi kiện 03 năm (Điều 429). Không nhầm với thời hiệu xử phạt vi phạm hành chính về chứng khoán (02 năm) hay thời hiệu khiếu nại quyết định hành chính (90 ngày, Điều 9 Luật Khiếu nại).",
    "Điều 588, Điều 429 Bộ luật Dân sự 2015 (91/2015/QH13); khoản 2 Điều 133 Luật Chứng khoán 2019",
    "Thời hiệu khởi kiện yêu cầu bồi thường thiệt hại là 03 năm, kể từ ngày người có quyền yêu cầu biết hoặc phải biết quyền, lợi ích hợp pháp của mình bị xâm phạm.", BLDS)

add(TP_TC, 2,
    "Hợp đồng quản lý danh mục đầu tư do Công ty bảo hiểm Q và công ty quản lý quỹ P trực tiếp đàm phán, ký kết có điều khoản: mọi tranh chấp được giải quyết tại Trung tâm Trọng tài Quốc tế Việt Nam (VIAC). Khi tranh chấp phát sinh, Q nộp đơn khởi kiện P tại Tòa án. Theo Luật Trọng tài thương mại, Tòa án:",
    ["Phải từ chối thụ lý, trừ khi thỏa thuận trọng tài vô hiệu hoặc không thể thực hiện được",
     "Được thụ lý vì Luật Chứng khoán cho các bên tự chọn Tòa án vào bất cứ lúc nào",
     "Phải thụ lý rồi tự quyết định có chuyển vụ việc sang VIAC giải quyết hay không",
     "Chỉ thụ lý khi UBCKNN xác nhận các bên đã hòa giải không thành"], 0,
    "Khoản 1 Điều 133 Luật Chứng khoán: tranh chấp trong hoạt động chứng khoán được giải quyết bằng thương lượng, hòa giải, Trọng tài hoặc Tòa án theo quy định của pháp luật. Điều 5 Luật Trọng tài thương mại 2010: tranh chấp được giải quyết bằng Trọng tài nếu các bên có thỏa thuận trọng tài (lập trước hoặc sau khi tranh chấp); Điều 6: đã có thỏa thuận trọng tài mà một bên khởi kiện tại Tòa án thì Tòa án phải từ chối thụ lý, trừ khi thỏa thuận vô hiệu hoặc không thể thực hiện được. Riêng người tiêu dùng ký theo điều kiện chung soạn sẵn vẫn được chọn Trọng tài hoặc Tòa án (Điều 17) – không áp dụng cho hợp đồng giữa hai tổ chức tự đàm phán. Luật không bắt buộc hòa giải tại UBCKNN.",
    "Điều 5, 6, 17 Luật Trọng tài thương mại 2010 (54/2010/QH12); khoản 1 Điều 133 Luật Chứng khoán 2019 (VBHN 24/VBHN-VPQH năm 2025)",
    "Trong trường hợp các bên tranh chấp đã có thỏa thuận trọng tài mà một bên khởi kiện tại Tòa án thì Tòa án phải từ chối thụ lý, trừ trường hợp thỏa thuận trọng tài vô hiệu hoặc thỏa thuận trọng tài không thể thực hiện được.", TTTM)

add(TP_TC, 1,
    "Theo Luật Trọng tài thương mại 2010, phán quyết trọng tài giải quyết tranh chấp giữa công ty quản lý quỹ và một khách hàng ủy thác là tổ chức:",
    ["Là chung thẩm và có hiệu lực kể từ ngày ban hành",
     "Có thể bị kháng cáo lên Tòa án nhân dân cấp tỉnh trong 15 ngày",
     "Chỉ có hiệu lực sau khi được UBCKNN xác nhận và công bố",
     "Có hiệu lực sau 30 ngày nếu các bên không có ý kiến phản đối"], 0,
    "Khoản 5 Điều 61 Luật Trọng tài thương mại: phán quyết trọng tài là chung thẩm và có hiệu lực kể từ ngày ban hành (nguyên tắc tại khoản 5 Điều 4). Phán quyết không bị kháng cáo; bên không đồng ý chỉ có thể làm đơn yêu cầu Tòa án hủy phán quyết trong 30 ngày kể từ ngày nhận phán quyết, khi có căn cứ luật định (Điều 68, 69) – Tòa án không xét xử lại nội dung tranh chấp. Slide 2025 nêu 'tính chất chung thẩm' của trọng tài là đúng.",
    "Khoản 5 Điều 4, khoản 5 Điều 61, Điều 68, 69 Luật Trọng tài thương mại 2010 (54/2010/QH12)",
    "5. Phán quyết trọng tài là chung thẩm và có hiệu lực kể từ ngày ban hành.", TTTM)

add(TP_TC, 2,
    "Công ty đại chúng Z nhận quyết định xử phạt vi phạm hành chính về công bố thông tin do Chủ tịch Ủy ban Chứng khoán Nhà nước ký và cho rằng quyết định này trái pháp luật. Theo Luật Khiếu nại, Z có thể:",
    ["Khiếu nại lần đầu đến Chủ tịch UBCKNN hoặc khởi kiện vụ án hành chính tại Tòa án",
     "Chỉ được khởi kiện vụ án dân sự yêu cầu UBCKNN bồi thường thiệt hại",
     "Khiếu nại lần đầu đến Thanh tra Chính phủ rồi mới được khởi kiện ra Tòa án",
     "Yêu cầu Trọng tài thương mại giải quyết theo Điều 133 Luật Chứng khoán"], 0,
    "Khoản 1 Điều 7 Luật Khiếu nại: khi cho rằng quyết định hành chính trái pháp luật, xâm phạm trực tiếp quyền, lợi ích hợp pháp của mình, người khiếu nại khiếu nại lần đầu đến người đã ra quyết định hoặc khởi kiện vụ án hành chính tại Tòa án; không đồng ý với kết quả lần đầu (hoặc quá hạn chưa giải quyết) thì khiếu nại lần hai đến thủ trưởng cấp trên trực tiếp hoặc khởi kiện. Quyết định xử phạt là quyết định hành chính (khoản 1 Điều 15 Luật Xử lý vi phạm hành chính cho phép khiếu nại, khởi kiện), không phải tranh chấp dân sự, thương mại nên không đưa ra Trọng tài. Thời hiệu khiếu nại: 90 ngày kể từ ngày nhận được quyết định (Điều 9).",
    "Khoản 1 Điều 7, Điều 9 Luật Khiếu nại 2011 (VBHN 120/VBHN-VPQH năm 2025; Luật 136/2025/QH15 không sửa Điều 7, Điều 9); khoản 1 Điều 15 Luật Xử lý vi phạm hành chính (VBHN 90/VBHN-VPQH năm 2026)",
    "xâm phạm trực tiếp đến quyền, lợi ích hợp pháp của mình thì người khiếu nại khiếu nại lần đầu đến người đã ra quyết định hành chính hoặc cơ quan có người có hành vi hành chính hoặc khởi kiện vụ án hành chính tại Tòa án", LKN)

add(TP_TC, 1,
    "Theo Luật Khiếu nại (sửa đổi bởi Luật 136/2025/QH15, hiệu lực 01/7/2026), kể từ ngày nhận được khiếu nại thuộc thẩm quyền và không thuộc trường hợp không thụ lý, người có thẩm quyền giải quyết khiếu nại lần đầu phải thụ lý trong thời hạn:",
    ["07 ngày làm việc", "10 ngày", "05 ngày làm việc", "15 ngày"], 0,
    "Điều 27 Luật Khiếu nại quy định thời hạn thụ lý khiếu nại lần đầu; điểm b khoản 15 Điều 2 Luật 136/2025/QH15 thay cụm từ '10 ngày' bằng '07 ngày làm việc' tại Điều 27, khoản 1 Điều 36 (thụ lý lần hai) và Điều 50, áp dụng từ 01/7/2026. Mức 10 ngày là quy định cũ. Sau khi thụ lý, thời hạn giải quyết lần đầu không quá 30 ngày (phức tạp không quá 45 ngày).",
    "Điều 27 Luật Khiếu nại 2011 (thay cụm từ bởi điểm b khoản 15 Điều 2 Luật 136/2025/QH15, hiệu lực 01/7/2026)",
    "b) Thay thế cụm từ “10 ngày” bằng cụm từ “07 ngày làm việc” tại Điều 27, khoản 1 Điều 36 và Điều 50;", L136)

add(TP_TC, 1,
    "Theo Luật Khiếu nại, thời hạn giải quyết khiếu nại lần đầu (không thuộc vùng sâu, vùng xa) là:",
    ["Không quá 30 ngày kể từ ngày thụ lý; vụ việc phức tạp không quá 45 ngày",
     "Không quá 45 ngày kể từ ngày thụ lý; vụ việc phức tạp không quá 60 ngày",
     "Không quá 15 ngày kể từ ngày thụ lý; vụ việc phức tạp không quá 30 ngày",
     "Không quá 90 ngày kể từ ngày nhận đơn; vụ việc phức tạp không quá 120 ngày"], 0,
    "Điều 28 Luật Khiếu nại (không bị Luật 136/2025 sửa): giải quyết lần đầu không quá 30 ngày kể từ ngày thụ lý, phức tạp không quá 45 ngày; vùng sâu, vùng xa: 45 ngày, phức tạp 60 ngày. 45/60 ngày là thời hạn giải quyết lần hai (Điều 37); 90 ngày là thời hiệu khiếu nại (Điều 9). Thời gian tạm đình chỉ giải quyết khiếu nại (Điều 11a bổ sung bởi Luật 136/2025) không tính vào thời hạn.",
    "Điều 28, Điều 37 Luật Khiếu nại 2011 (VBHN 120/VBHN-VPQH năm 2025; Luật 136/2025/QH15 không sửa Điều 28, 37)",
    "Thời hạn giải quyết khiếu nại lần đầu không quá 30 ngày, kể từ ngày thụ lý; đối với vụ việc phức tạp thì thời hạn giải quyết có thể kéo dài hơn nhưng không quá 45 ngày, kể từ ngày thụ lý.", LKN)

add(TP_TC, 1,
    "Theo Luật Tố cáo, “người tố cáo” là:",
    ["Cá nhân thực hiện việc tố cáo",
     "Cơ quan, tổ chức, cá nhân thực hiện việc tố cáo",
     "Cán bộ, công chức, viên chức trong cơ quan nhà nước",
     "Người có quyền, lợi ích bị xâm phạm trực tiếp"], 0,
    "Khoản 1, 4 Điều 2 Luật Tố cáo 2018: tố cáo là việc cá nhân báo cho cơ quan, tổ chức, cá nhân có thẩm quyền biết về hành vi vi phạm pháp luật của bất kỳ cơ quan, tổ chức, cá nhân nào gây thiệt hại hoặc đe dọa gây thiệt hại; người tố cáo là cá nhân. Khác với khiếu nại: người khiếu nại là cơ quan, tổ chức, cá nhân (Điều 2 Luật Khiếu nại, sửa bởi Luật 136/2025) và chỉ đề nghị xem xét lại quyết định, hành vi hành chính xâm phạm quyền lợi của chính mình. Định nghĩa trên slide 2025 ('công dân') là cách diễn đạt của Luật Tố cáo 2011, đã hết hiệu lực.",
    "Khoản 1, 4 Điều 2 Luật Tố cáo 2018 (VBHN 112/VBHN-VPQH năm 2025; Luật 136/2025/QH15 không sửa Điều 2); khoản 1, 2 Điều 2 Luật Khiếu nại (sửa đổi bởi khoản 1 Điều 2 Luật 136/2025/QH15)",
    "4. Người tố cáo là cá nhân thực hiện việc tố cáo.", LTC)

add(TP_TC, 3,
    "Theo Luật Tố cáo, đối với vụ việc đặc biệt phức tạp, thời hạn giải quyết tố cáo tối đa (tính cả các lần gia hạn) kể từ ngày thụ lý là:",
    ["90 ngày", "60 ngày", "45 ngày", "120 ngày"], 0,
    "Điều 30 Luật Tố cáo: thời hạn giải quyết không quá 30 ngày kể từ ngày thụ lý; vụ việc phức tạp được gia hạn một lần không quá 30 ngày (tối đa 60 ngày); vụ việc đặc biệt phức tạp được gia hạn hai lần, mỗi lần không quá 30 ngày, nên tối đa 30 + 30 + 30 = 90 ngày. Việc gia hạn phải quyết định bằng văn bản và thông báo cho người tố cáo, người bị tố cáo. 60 ngày là mức của vụ việc phức tạp.",
    "Điều 30 Luật Tố cáo 2018 (VBHN 112/VBHN-VPQH năm 2025; Luật 136/2025/QH15 không sửa Điều 30)",
    "1. Thời hạn giải quyết tố cáo là không quá 30 ngày kể từ ngày thụ lý tố cáo. 2. Đối với vụ việc phức tạp thì có thể gia hạn giải quyết tố cáo một lần nhưng không quá 30 ngày. 3. Đối với vụ việc đặc biệt phức tạp thì có thể gia hạn giải quyết tố cáo hai lần, mỗi lần không quá 30 ngày.", LTC)

# ---------- đánh số, xoay đáp án, tự kiểm tra ----------
out, errs = [], []
for n, x in enumerate(Q, 1):
    i = f"L4-{n:03d}"
    o = x["o"][:]; correct = o.pop(x["a"]); t = (n - 1) % 4; o.insert(t, correct)   # rải đáp án đều A–D
    q = dict(id=i, part="LUAT", subject="LU", topic=x["topic"], level=x["level"], q=x["q"], o=o, a=t,
             e=x["e"], basis=x["basis"], quote=x["quote"], src=x["src"], as_of="2026-11")
    if len(o) != 4 or len(set(o)) != 4: errs.append(f"{i}: phương án")
    if len(x["quote"]) > 300: errs.append(f"{i}: trích dẫn dài {len(x['quote'])}")
    if not ok(x["quote"], x["src"]): errs.append(f"{i}: trích dẫn không khớp {x['src']}")
    lens = [len(s) for s in o]
    if max(lens) > 1.8 * min(lens) and min(lens) > 12: errs.append(f"{i}: độ dài phương án lệch {lens}")
    out.append(q)
print(len(out), "câu;", "LỖI:" if errs else "OK", *errs, sep="\n")
if not errs:
    (HERE / "luat_4.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    from collections import Counter
    print(Counter(q["topic"] for q in out)); print(Counter(q["level"] for q in out)); print(Counter(q["a"] for q in out))
