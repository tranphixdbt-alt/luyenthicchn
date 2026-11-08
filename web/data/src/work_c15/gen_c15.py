# Chuyên đề 7 SRTC "Yêu cầu quản lý đối với hoạt động môi giới và tư vấn đầu tư chứng khoán" (2024):
# sinh câu mới cho các ý ngân hàng chưa có -> ../cm_15.json. Kiểm trích dẫn bằng đúng hàm của tools/kiem_tra.py.
# Chạy: python3 -I gen_c15.py
import json, re, sys
from collections import Counter
sys.path.insert(0, '/home/user/cchn_moi/web/tools')
from kiem_tra import doc_text, norm_ws, loose

OUT = '/home/user/cchn_moi/web/data/src/cm_15.json'
LCK = 'VBHN_102_VBHN-VPQH_2026_Luat_Chung_khoan_hop_nhat.txt'
TT121 = 'VBHN_09_VBHN-BTC_2026_TT121_68_08_hop_nhat.txt'
PCRT = 'Luat_Phong_chong_rua_tien_14_2022_QH15_Cong_bao_so_909-910_2022.txt'
T = "Quản lý Nhà nước đối với hoạt động môi giới và tư vấn đầu tư chứng khoán"
GT = "Giáo trình Môi giới và tư vấn đầu tư chứng khoán (UBCKNN/SRTC), chuyên đề Yêu cầu quản lý đối với hoạt động môi giới và tư vấn đầu tư chứng khoán – "
LCK_B = "Luật Chứng khoán 2019 (VBHN 102/VBHN-VPQH năm 2026, hợp nhất Luật 56/2024/QH15 và Luật 142/2025/QH15)"
TT121_B = "Thông tư 121/2020/TT-BTC (VBHN 09/VBHN-BTC năm 2026, hợp nhất Thông tư 68/2024/TT-BTC và Thông tư 08/2026/TT-BTC)"
PCRT_B = "Luật Phòng, chống rửa tiền số 14/2022/QH15 (hiệu lực 01/3/2023, chưa bị sửa đổi)"

Q = []
def add(level, q, correct, wrong, a, e, basis, quote="", src=""):
    assert len(wrong) == 3 and len({correct, *wrong}) == 4, q[:40]
    Q.append(dict(level=level, q=q, correct=correct, wrong=wrong, a=a, e=e, basis=basis, quote=quote, src=src))

# 001 – tr.4, 11: nội dung quản lý nhà nước
add(1, "Theo giáo trình, về cơ bản hoạt động quản lý nhà nước đối với lĩnh vực chứng khoán và thị trường chứng khoán được thực hiện qua các nội dung nào?",
    "Lập quy; giám sát thực hiện và cưỡng chế thực thi",
    ["Lập quy; trực tiếp kinh doanh và bình ổn giá chứng khoán",
     "Cấp phép; bảo lãnh giá và phân phối chứng khoán niêm yết",
     "Tuyên truyền; tư vấn đầu tư và quản lý danh mục cho nhà đầu tư"], 2,
    "Giáo trình nêu quản lý nhà nước về thị trường chứng khoán tập trung vào (1) xây dựng, hoàn thiện khuôn khổ pháp luật và (2) tổ chức, điều hành, giám sát thị trường; cụ thể hóa qua ba nội dung: lập quy, giám sát thực hiện và cưỡng chế thực thi. Nhà nước không trực tiếp kinh doanh, bảo lãnh giá hay tư vấn đầu tư; Điều 6 Luật Chứng khoán chỉ đặt chính sách quản lý, giám sát để thị trường hoạt động công bằng, công khai, minh bạch, an toàn và hiệu quả.",
    GT + "Quản lý đối với hoạt động môi giới và tư vấn đầu tư chứng khoán; Điều 6, Điều 8 " + LCK_B)

# 002 – tr.7: mục tiêu quản lý hệ thống tài chính
add(1, "Theo giáo trình, nội dung nào sau đây KHÔNG thuộc mục tiêu cơ bản của quản lý hệ thống tài chính?",
    "Bảo đảm mức lợi nhuận tối thiểu cho các công ty chứng khoán",
    ["Duy trì sự ổn định, phát triển lành mạnh của hệ thống tài chính",
     "Bảo vệ quyền lợi người gửi tiền, nhà đầu tư và khách hàng khác",
     "Bảo đảm hội nhập hiệu quả của thị trường tài chính trong nước"], 3,
    "Ba mục tiêu cơ bản: duy trì sự ổn định và phát triển lành mạnh của hệ thống tài chính; bảo đảm môi trường phát triển ổn định, lành mạnh cho mỗi thành viên, đặc biệt bảo vệ quyền lợi người gửi tiền, nhà đầu tư và khách hàng của các trung gian tài chính; bảo đảm hội nhập hiệu quả của thị trường tài chính trong nước vào thị trường quốc tế. Quản lý nhà nước không bảo đảm lợi nhuận cho bất kỳ doanh nghiệp nào; công ty chứng khoán tự chịu rủi ro kinh doanh.",
    GT + "Mục tiêu cơ bản của quản lý hệ thống tài chính")

# 003 – tr.11: nhiệm vụ của Bộ Tài chính (tổ hợp)
add(2, "Theo khoản 2 Điều 8 Luật Chứng khoán, xét các nhiệm vụ sau:\nI. Cấp, thu hồi chứng chỉ hành nghề chứng khoán;\nII. Trình Chính phủ, Thủ tướng Chính phủ ban hành chiến lược, kế hoạch, đề án, chính sách phát triển thị trường chứng khoán;\nIII. Trình cấp có thẩm quyền ban hành hoặc ban hành theo thẩm quyền văn bản quy phạm pháp luật về chứng khoán;\nIV. Chỉ đạo Ủy ban Chứng khoán Nhà nước thực hiện chiến lược, chính sách và văn bản quy phạm pháp luật về chứng khoán.\nNhững nhiệm vụ của Bộ Tài chính là:",
    "II, III và IV", ["I, II và III", "I và IV", "II và III"], 0,
    "Khoản 2 Điều 8: Bộ Tài chính chịu trách nhiệm trước Chính phủ thực hiện quản lý nhà nước về chứng khoán, có ba nhiệm vụ: (a) trình Chính phủ, Thủ tướng ban hành chiến lược, kế hoạch, đề án, chính sách – II; (b) trình cấp có thẩm quyền ban hành hoặc ban hành theo thẩm quyền văn bản quy phạm pháp luật – III; (c) chỉ đạo UBCKNN thực hiện – IV. Cấp, thu hồi chứng chỉ hành nghề chứng khoán là nhiệm vụ của Ủy ban Chứng khoán Nhà nước (điểm c khoản 1 Điều 9).",
    "Khoản 2 Điều 8, điểm c khoản 1 Điều 9 " + LCK_B,
    "b) Trình cấp có thẩm quyền ban hành hoặc ban hành theo thẩm quyền các văn bản quy phạm pháp luật về chứng khoán và thị trường chứng khoán; c) Chỉ đạo Ủy ban Chứng khoán Nhà nước thực hiện chiến lược, kế hoạch, đề án, chính sách phát triển thị trường chứng khoán",
    LCK)

# 004 – tr.5: nguyên tắc của tổ chức tự quản
add(2, "Theo giáo trình, ngoài yêu cầu các quyết định điều hành phải đúng đắn, phù hợp thực tế và giám sát có hiệu quả, tổ chức tự quản trên thị trường chứng khoán còn hoạt động theo nguyên tắc nào?",
    "Chi phí điều hành, giám sát được bù đắp từ hoạt động trên thị trường, không do ngân sách cấp",
    ["Chi phí điều hành, giám sát do ngân sách nhà nước cấp đủ hằng năm để bảo đảm độc lập",
     "Quyết định của tổ chức tự quản không chịu sự giám sát của cơ quan quản lý nhà nước",
     "Chỉ giám sát giao dịch của nhà đầu tư, không giám sát công ty chứng khoán thành viên"], 0,
    "Tổ chức tự quản (như Sở giao dịch chứng khoán, hiệp hội nghề nghiệp) dựa trên hai nguyên tắc: quyết định điều hành đúng đắn, phù hợp thực tế, giám sát hiệu quả; và chi phí điều hành, giám sát thu được từ chính hoạt động trên thị trường chứ không do ngân sách cấp. Hoạt động của các tổ chức này gồm quản lý, giám sát giao dịch, giám sát công ty chứng khoán thành viên, giải quyết tranh chấp và xử lý vi phạm. Ở Việt Nam, Sở giao dịch chứng khoán và tổ chức xã hội – nghề nghiệp về chứng khoán vẫn chịu sự quản lý, giám sát của UBCKNN (khoản 3 Điều 43, khoản 1 Điều 10 Luật Chứng khoán).",
    GT + "Quản lý của các tổ chức tự quản; khoản 3 Điều 43, khoản 1 Điều 10 " + LCK_B)

# 005 – tr.6: quyền của Sở giao dịch chứng khoán (tổ hợp)
add(2, "Theo khoản 1 Điều 46 Luật Chứng khoán, xét các quyền sau:\nI. Làm trung gian hòa giải theo yêu cầu của thành viên khi phát sinh tranh chấp liên quan đến hoạt động giao dịch chứng khoán;\nII. Kiểm tra, xử lý vi phạm đối với thành viên theo quy chế của Sở;\nIII. Thu hồi Giấy phép thành lập và hoạt động của công ty chứng khoán thành viên vi phạm nghiêm trọng;\nIV. Tạm ngừng, đình chỉ giao dịch một hoặc một số chứng khoán khi giá, khối lượng giao dịch biến động bất thường.\nNhững quyền của Sở giao dịch chứng khoán Việt Nam là:",
    "I, II và IV", ["I, II và III", "II, III và IV", "I và IV"], 1,
    "Điểm h, i, d khoản 1 Điều 46: Sở giao dịch chứng khoán Việt Nam làm trung gian hòa giải theo yêu cầu của thành viên khi có tranh chấp liên quan đến giao dịch chứng khoán – I; kiểm tra, xử lý vi phạm đối với thành viên, tổ chức niêm yết, tổ chức đăng ký giao dịch theo quy chế của Sở – II; tạm ngừng, đình chỉ giao dịch chứng khoán khi giá, khối lượng biến động bất thường – IV. Đây là các chức năng 'tự quản' tuyến đầu nêu trong giáo trình. Thu hồi Giấy phép thành lập và hoạt động kinh doanh chứng khoán của công ty chứng khoán thuộc thẩm quyền UBCKNN (Điều 95), nên III sai; Sở chỉ được chấp thuận, hủy bỏ tư cách thành viên của Sở (điểm e khoản 1 Điều 46).",
    "Điểm d, e, h, i khoản 1 Điều 46, Điều 95 " + LCK_B,
    "h) Làm trung gian hòa giải theo yêu cầu của thành viên của Sở giao dịch chứng khoán Việt Nam khi phát sinh tranh chấp liên quan đến hoạt động giao dịch chứng khoán; i) Kiểm tra, xử lý vi phạm đối với thành viên của Sở giao dịch chứng khoán Việt Nam",
    LCK)

# 006 – tr.3, 6: tổ chức xã hội – nghề nghiệp, bộ quy tắc đạo đức (tổ hợp)
add(2, "Theo Luật Chứng khoán, xét các nhận định sau về tổ chức xã hội – nghề nghiệp về chứng khoán (như Hiệp hội Kinh doanh chứng khoán Việt Nam):\nI. Được thành lập theo quyết định của Ủy ban Chứng khoán Nhà nước;\nII. Chịu sự giám sát của Ủy ban Chứng khoán Nhà nước;\nIII. Ban hành bộ quy tắc đạo đức nghề nghiệp sau khi được Ủy ban Chứng khoán Nhà nước chấp thuận;\nIV. Được cấp chứng chỉ hành nghề chứng khoán cho hội viên đạt kỳ thi do hiệp hội tổ chức.\nNhững nhận định đúng là:",
    "II và III", ["I và II", "II, III và IV", "I, III và IV"], 2,
    "Điều 10: tổ chức xã hội – nghề nghiệp về chứng khoán được thành lập, hoạt động theo pháp luật về hội (không do UBCKNN quyết định thành lập – I sai), tuân thủ pháp luật chứng khoán và chịu sự giám sát của UBCKNN – II; ban hành bộ quy tắc đạo đức nghề nghiệp sau khi được UBCKNN chấp thuận và phối hợp tuyên truyền, phổ biến pháp luật đến hội viên – III. UBCKNN cũng có nhiệm vụ giám sát tổ chức này thực hiện mục đích, tôn chỉ, Điều lệ (điểm n khoản 1 Điều 9). Chứng chỉ hành nghề chứng khoán do UBCKNN cấp (điểm c khoản 1 Điều 9) – IV sai. Riêng mỗi công ty chứng khoán cũng phải tự ban hành quy tắc đạo đức hành nghề (khoản 2 Điều 4 Thông tư 121/2020/TT-BTC).",
    "Khoản 1, 2 Điều 10, điểm c, n khoản 1 Điều 9 " + LCK_B + "; khoản 2 Điều 4 " + TT121_B,
    "Tổ chức xã hội - nghề nghiệp về chứng khoán ban hành bộ quy tắc đạo đức nghề nghiệp sau khi được Ủy ban Chứng khoán Nhà nước chấp thuận",
    LCK)

# 007 – tr.12: nhóm quy định quản lý nghề môi giới
add(1, "Theo giáo trình, nội dung nào sau đây KHÔNG thuộc nhóm quy định quản lý nhà nước đối với nghề môi giới chứng khoán?",
    "Quy định bảo đảm mức lợi nhuận tối thiểu cho khách hàng",
    ["Quy định về sự thích hợp của khuyến nghị với khách hàng",
     "Quy định cấm giao dịch quá mức trên tài khoản khách hàng",
     "Quy định về thi hành tốt nhất đối với lệnh của khách hàng"], 3,
    "Nhóm quy định quản lý nghề môi giới trong giáo trình gồm: đăng ký kinh doanh; sự thích hợp; cơ sở hợp lý; cấm tăng giá quá mức; cấm giao dịch quá mức; giám sát người hành nghề (đại diện đã đăng ký); thi hành tốt nhất; lưu trữ hồ sơ; quy định về công ty chứng khoán và người được ủy thác. Pháp luật Việt Nam tương ứng: khoản 6, 7 Điều 89 Luật Chứng khoán (phù hợp với khách hàng, lưu giữ hồ sơ), khoản 3 Điều 24 Thông tư 121/2020/TT-BTC (cơ sở hợp lý). Bảo đảm mức lợi nhuận hay bảo đảm khách hàng không thua lỗ thì bị cấm (khoản 1 Điều 91 Luật Chứng khoán).",
    GT + "Quản lý đối với nghề môi giới; khoản 6, 7 Điều 89, khoản 1 Điều 91 " + LCK_B)

# 008 – tr.12: thi hành tốt nhất
add(1, "Theo giáo trình, yêu cầu “thi hành tốt nhất” (best execution) đối với người môi giới chứng khoán có nghĩa là:",
    "Thực hiện lệnh với điều kiện có lợi nhất cho khách hàng có thể đạt được tại thời điểm đó",
    ["Thực hiện trước lệnh có giá trị lớn nhất để tối đa hóa phí môi giới cho công ty",
     "Thực hiện trước lệnh của khách hàng VIP rồi mới đến lệnh của khách hàng thông thường",
     "Gom lệnh của mọi khách hàng để thực hiện một lần tại giá đóng cửa cuối phiên"], 1,
    "Thi hành tốt nhất là nghĩa vụ thực hiện lệnh của khách hàng nhanh chóng, với giá và điều kiện có lợi nhất cho khách hàng trong hoàn cảnh thị trường lúc đó. Pháp luật Việt Nam thể hiện tinh thần này qua yêu cầu ưu tiên lệnh của khách hàng trước lệnh tự doanh (khoản 5 Điều 89 Luật Chứng khoán) và không được mua, bán cùng chiều cho mình ở mức giá bằng hoặc tốt hơn lệnh giới hạn của khách hàng trước khi lệnh đó được thực hiện (khoản 7 Điều 22 Thông tư 121/2020/TT-BTC). Ưu tiên khách hàng VIP hay lệnh lớn để hưởng phí là trái nguyên tắc đối xử công bằng.",
    GT + "Thi hành tốt nhất; khoản 5 Điều 89 " + LCK_B + "; khoản 7 Điều 22 " + TT121_B)

# 009 – tr.12, 14: giám sát người hành nghề, kiểm soát nội bộ vs kiểm toán nội bộ
add(2, "Theo Thông tư 121/2020/TT-BTC, nội dung nào sau đây KHÔNG thuộc nhiệm vụ của bộ phận kiểm soát nội bộ trực thuộc Ban Tổng giám đốc (Ban Giám đốc) công ty chứng khoán?",
    "Đánh giá độc lập sự đầy đủ, hiệu quả và hiệu lực của chính hệ thống kiểm soát nội bộ",
    ["Kiểm soát việc tuân thủ quy định pháp luật về phòng, chống rửa tiền trong công ty",
     "Kiểm tra nội dung và giám sát việc thực hiện các quy tắc về đạo đức nghề nghiệp",
     "Giám sát các hoạt động tiềm ẩn xung đột lợi ích và giao dịch cá nhân của nhân viên"], 0,
    "Khoản 2 Điều 12: bộ phận kiểm soát nội bộ kiểm soát việc tuân thủ, gồm giám sát hoạt động tiềm ẩn xung đột lợi ích và giao dịch cá nhân của nhân viên (điểm b), kiểm tra, giám sát thực hiện quy tắc đạo đức nghề nghiệp (điểm c), kiểm soát tuân thủ pháp luật về phòng, chống rửa tiền (điểm g)… Việc kiểm tra, đánh giá sự đầy đủ, hiệu quả, hiệu lực của hệ thống kiểm soát nội bộ trực thuộc Ban Tổng giám đốc là nhiệm vụ của kiểm toán nội bộ (điểm b khoản 2 Điều 9), bộ phận phải độc lập với ban điều hành. Đây là cách công ty thực hiện 'giám sát người hành nghề' mà giáo trình nêu; công ty chịu trách nhiệm về hoạt động nghiệp vụ của người hành nghề (khoản 4 Điều 98 Luật Chứng khoán).",
    "Điểm b, c, g khoản 2 Điều 12, điểm b khoản 2 Điều 9 " + TT121_B + "; khoản 4 Điều 98 Luật Chứng khoán 2019",
    "b) Kiểm tra, xem xét và đánh giá sự đầy đủ, hiệu quả và hiệu lực của hệ thống kiểm soát nội bộ trực thuộc Ban Tổng Giám đốc (Ban Giám đốc) nhằm hoàn thiện hệ thống này;",
    TT121)

# 010 – tr.12, 13: lưu trữ hồ sơ
add(2, "Theo Luật Chứng khoán và Thông tư 121/2020/TT-BTC (sửa đổi bởi Thông tư 08/2026/TT-BTC), yêu cầu nào sau đây đúng về lưu giữ hồ sơ, dữ liệu khi công ty chứng khoán thực hiện nghiệp vụ môi giới?",
    "Cập nhật, lưu giữ đủ hồ sơ khách hàng, chứng từ; dữ liệu tài khoản môi giới quản lý tập trung, có dự phòng ở địa điểm khác",
    ["Chỉ lưu hồ sơ của khách hàng còn số dư; dữ liệu tài khoản môi giới do từng chi nhánh tự quản lý độc lập",
     "Chỉ lưu hợp đồng mở tài khoản; dữ liệu giao dịch của khách hàng do Sở giao dịch chứng khoán lưu giữ thay",
     "Lưu dữ liệu tài khoản môi giới duy nhất tại trụ sở chính, không sao lưu ra nơi khác để bảo mật thông tin"], 2,
    "Khoản 7 Điều 89 Luật Chứng khoán: công ty chứng khoán phải cập nhật, lưu giữ đầy đủ hồ sơ thông tin khách hàng, chứng từ và phản ánh chi tiết, chính xác giao dịch của khách hàng và của công ty; khoản 10: xây dựng cơ sở dữ liệu dự phòng để hoạt động an toàn, liên tục. Khoản 3 Điều 13 Thông tư 121/2020 (sửa đổi bởi khoản 1 Điều 9 Thông tư 08/2026/TT-BTC, hiệu lực 03/02/2026): dữ liệu tài khoản môi giới của khách hàng, kể cả dữ liệu giao dịch của nhà đầu tư nước ngoài dùng số hiệu tài khoản lưu ký, phải được quản lý tập trung và lưu dự phòng tại địa điểm khác.",
    "Khoản 7, 10 Điều 89 " + LCK_B + "; khoản 3 Điều 13 Thông tư 121/2020/TT-BTC (sửa đổi bởi khoản 1 Điều 9 Thông tư 08/2026/TT-BTC)",
    "7. Cập nhật, lưu giữ đầy đủ hồ sơ thông tin khách hàng, chứng từ và phản ánh chi tiết, chính xác các giao dịch của khách hàng và của công ty chứng khoán.",
    LCK)

# (tr.13: chi nhánh công ty chứng khoán nước ngoài chỉ được tư vấn đầu tư – đã có ở C13-001, bỏ)

# 012 – tr.13: hợp đồng tư vấn đầu tư
add(2, "Theo Thông tư 121/2020/TT-BTC, nội dung nào sau đây KHÔNG thuộc các nội dung tối thiểu của hợp đồng cung cấp dịch vụ tư vấn đầu tư chứng khoán giữa công ty chứng khoán và khách hàng?",
    "Mức lợi nhuận tối thiểu công ty cam kết cho khách hàng",
    ["Phạm vi tư vấn đầu tư chứng khoán của công ty",
     "Phương thức công ty cung cấp dịch vụ tư vấn",
     "Phí dịch vụ tư vấn mà khách hàng phải trả"], 1,
    "Khoản 1 Điều 24: hợp đồng tư vấn đầu tư chứng khoán có tối thiểu: (a) quyền, nghĩa vụ, trách nhiệm của các bên; (b) phạm vi tư vấn đầu tư chứng khoán; (c) phương thức cung cấp dịch vụ; (d) phí dịch vụ. Công ty không được đưa ra nhận định hoặc bảo đảm về mức thu nhập, lợi nhuận hay bảo đảm khách hàng không thua lỗ, trừ chứng khoán có thu nhập cố định (khoản 1 Điều 91 Luật Chứng khoán), và không được thỏa thuận chia sẻ lợi nhuận hoặc lỗ với khách hàng (điểm b khoản 6 Điều 4 Thông tư 121).",
    "Khoản 1 Điều 24, điểm b khoản 6 Điều 4 " + TT121_B + "; khoản 1 Điều 91 Luật Chứng khoán 2019",
    "phải ký kết hợp đồng với khách hàng với các nội dung tối thiểu như sau: a) Quyền, nghĩa vụ, trách nhiệm của các bên tham gia hợp đồng; b) Phạm vi tư vấn đầu tư chứng khoán; c) Phương thức cung cấp dịch vụ; d) Phí dịch vụ.",
    TT121)

# 013 – tr.14: khái niệm rửa tiền
add(1, "Theo Luật Phòng, chống rửa tiền 2022, rửa tiền là:",
    "Hành vi của tổ chức, cá nhân nhằm hợp pháp hóa nguồn gốc của tài sản do phạm tội mà có",
    ["Hành vi mang tiền mặt ra nước ngoài vượt mức quy định mà không khai báo với hải quan",
     "Hành vi trốn thuế thu nhập cá nhân phát sinh từ chuyển nhượng chứng khoán niêm yết",
     "Hành vi giao dịch tiền mặt có giá trị lớn mà không báo cáo Ngân hàng Nhà nước Việt Nam"], 0,
    "Khoản 1 Điều 3 Luật Phòng, chống rửa tiền 2022: rửa tiền là hành vi của tổ chức, cá nhân nhằm hợp pháp hóa nguồn gốc của tài sản do phạm tội mà có; tài sản do phạm tội mà có gồm cả thu nhập, hoa lợi, lợi tức, lợi nhuận sinh ra từ tài sản đó (khoản 2). Giáo trình diễn đạt: biến lợi nhuận, tài sản có từ phạm tội hoặc tham nhũng thành tài sản được coi là 'hợp pháp'. Không khai báo tiền mặt khi xuất cảnh, trốn thuế hay không báo cáo giao dịch lớn là các vi phạm khác, tự chúng không phải là định nghĩa rửa tiền. Tội rửa tiền được quy định tại Điều 324 Bộ luật Hình sự.",
    "Khoản 1, 2 Điều 3 " + PCRT_B + "; Điều 324 Bộ luật Hình sự 2015 (sửa đổi bởi Luật 12/2017/QH14)",
    "Rửa tiền là hành vi của tổ chức, cá nhân nhằm hợp pháp hóa nguồn gốc của tài sản do phạm tội mà có.",
    PCRT)

# 014 – tr.15: thứ tự ba giai đoạn
add(1, "Theo giáo trình, hoạt động rửa tiền thường được thực hiện qua ba giai đoạn theo thứ tự nào?",
    "Sắp xếp (placement) → Phân tán (layering) → Quy tụ (integration)",
    ["Phân tán (layering) → Sắp xếp (placement) → Quy tụ (integration)",
     "Sắp xếp (placement) → Quy tụ (integration) → Phân tán (layering)",
     "Quy tụ (integration) → Phân tán (layering) → Sắp xếp (placement)"], 2,
    "Sắp xếp (placement): đưa tiền bẩn vào hệ thống tài chính (gửi ngân hàng, mua công cụ tài chính); phân tán (layering): thực hiện nhiều giao dịch phức tạp, chuyển qua nhiều tài khoản, nhiều quốc gia để xóa dấu vết nguồn gốc; quy tụ (integration): đưa tiền đã 'rửa' trở lại nền kinh tế dưới dạng tài sản, thu nhập có vẻ hợp pháp (mua bất động sản, hàng xa xỉ, đầu tư, kinh doanh).",
    GT + "Ba giai đoạn rửa tiền")

# 015 – tr.15, 17: nhận diện giai đoạn phân tán
add(2, "Sau khi đã gửi được tiền thu từ buôn lậu vào tài khoản ngân hàng của công ty X, ông T cho chuyển tiền qua lại giữa X và nhiều công ty ở nước ngoài bằng các hợp đồng mua bán, khoản vay khống để xóa dấu vết nguồn gốc của tiền. Theo mô hình ba giai đoạn trong giáo trình, các giao dịch chuyển qua lại này thuộc giai đoạn:",
    "Phân tán (layering)",
    ["Sắp xếp (placement)", "Quy tụ (integration)", "Thực hiện tội phạm nguồn"], 1,
    "Việc gửi tiền buôn lậu vào ngân hàng là giai đoạn sắp xếp (đã xong). Chuỗi chuyển tiền qua lại giữa các công ty, qua ngân hàng nước ngoài bằng hợp đồng, khoản vay giả nhằm che giấu nguồn gốc là giai đoạn phân tán – đúng sơ đồ 'quy trình rửa tiền điển hình' trong giáo trình. Khi tiền được đưa về dùng mua bất động sản, hàng hiệu, đầu tư tài chính, kinh doanh mới là giai đoạn quy tụ. Buôn lậu là hành vi phạm tội tạo ra tài sản (tội phạm nguồn), không phải một giai đoạn của rửa tiền.",
    GT + "Ba giai đoạn rửa tiền; sơ đồ quy trình rửa tiền điển hình")

# 016 – tr.16: các biện pháp rửa tiền (tổ hợp)
add(2, "Theo giáo trình, xét các cách thức sau:\nI. Dùng các công ty “ma” (không hoạt động thực tế) làm vỏ bọc để nhận và chuyển tiền;\nII. Chia một khoản tiền lớn thành nhiều giao dịch nhỏ để tránh ngưỡng phải báo cáo;\nIII. Trộn tiền bất hợp pháp vào doanh thu của một cơ sở kinh doanh hợp pháp;\nIV. Bán toàn bộ danh mục cổ phiếu để cắt lỗ rồi chuyển tiền về tài khoản ngân hàng đứng tên chính mình.\nNhững cách thức là biện pháp rửa tiền là:",
    "I, II và III", ["I và II", "II, III và IV", "I, III và IV"], 3,
    "Giáo trình nêu 6 biện pháp rửa tiền cơ bản: núp dưới vỏ bọc các công ty ma – I; khai thác kẽ hở pháp lý; thông qua giao dịch thương mại quốc tế; nhân đôi các giao dịch; trộn tiền sạch và tiền bẩn – III; chia nhỏ khoản tiền lớn – II. Bán cổ phiếu cắt lỗ và rút tiền về tài khoản chính chủ là giao dịch bình thường, không nhằm che giấu nguồn gốc tài sản (IV).",
    GT + "Sáu biện pháp rửa tiền cơ bản")

# 017 – tr.18: tác động của rửa tiền
add(1, "Theo giáo trình, nội dung nào sau đây KHÔNG phải là tác động của rửa tiền đến nền kinh tế và hệ thống tài chính?",
    "Tăng tính minh bạch và hiệu quả phân bổ vốn trên thị trường",
    ["Gây bất ổn cho thị trường tài chính – tiền tệ",
     "Đẩy dòng vốn vào hoạt động rủi ro cao, giảm tăng trưởng",
     "Tổ chức tài chính có thể bị băng nhóm tội phạm thao túng"], 2,
    "Giáo trình nêu bốn tác động: phá vỡ sự ổn định, tiềm ẩn hậu quả nghiêm trọng cho nền kinh tế; gây bất ổn thị trường tài chính – tiền tệ; tác động tiêu cực tới xu hướng đầu tư với rủi ro cao, làm giảm tốc độ tăng trưởng kinh tế; hệ thống tổ chức tài chính có thể bị các băng nhóm tội phạm thao túng. Rửa tiền làm méo mó dòng vốn và giảm minh bạch, không làm tăng hiệu quả phân bổ vốn.",
    GT + "Tác động của rửa tiền")

# 018 – Luật PCRT: đối tượng báo cáo (tổ hợp)
add(2, "Theo khoản 1 Điều 4 Luật Phòng, chống rửa tiền 2022, xét các hoạt động được cấp phép sau:\nI. Môi giới chứng khoán;\nII. Kinh doanh bảo hiểm phi nhân thọ;\nIII. Tư vấn đầu tư chứng khoán;\nIV. Quản lý danh mục đầu tư chứng khoán.\nTổ chức tài chính được cấp phép thực hiện những hoạt động nào thì thuộc đối tượng báo cáo theo luật này?",
    "I, III và IV", ["I và III", "I, II và III", "I, II, III và IV"], 0,
    "Điểm i, k, l khoản 1 Điều 4: đối tượng báo cáo gồm tổ chức tài chính được cấp phép môi giới chứng khoán; tư vấn đầu tư chứng khoán, bảo lãnh phát hành chứng khoán; quản lý quỹ đầu tư chứng khoán; quản lý danh mục đầu tư chứng khoán; kinh doanh bảo hiểm nhân thọ (không gồm bảo hiểm phi nhân thọ). Vì vậy công ty chứng khoán, công ty quản lý quỹ phải thực hiện nhận biết khách hàng, báo cáo giao dịch, lưu trữ hồ sơ theo luật này; Thông tư 121/2020/TT-BTC cũng yêu cầu công ty chứng khoán tuân thủ quy định về phòng, chống rửa tiền khi môi giới (khoản 2 Điều 13).",
    "Điểm i, k, l khoản 1 Điều 4 " + PCRT_B + "; khoản 2 Điều 13 " + TT121_B,
    "i) Môi giới chứng khoán; tư vấn đầu tư chứng khoán, bảo lãnh phát hành chứng khoán; k) Quản lý quỹ đầu tư chứng khoán; quản lý danh mục đầu tư chứng khoán; l) Kinh doanh bảo hiểm nhân thọ;",
    PCRT)

# 019 – Luật PCRT Điều 31: dấu hiệu đáng ngờ trong lĩnh vực chứng khoán (tổ hợp)
add(2, "Theo Điều 31 Luật Phòng, chống rửa tiền 2022, xét các tình huống tại công ty chứng khoán:\nI. Tài khoản của khách hàng đột nhiên nhận một khoản tiền lớn không phù hợp với khả năng tài chính của khách hàng;\nII. Khách hàng thường xuyên bán tất cả cổ phiếu và đề nghị công ty ký ủy nhiệm chi để rút tiền mặt từ ngân hàng thương mại;\nIII. Khách hàng hằng tháng chuyển một khoản cố định từ tài khoản nhận lương để mua chứng chỉ quỹ theo hợp đồng định kỳ;\nIV. Người không cư trú chuyển số tiền lớn từ tài khoản giao dịch chứng khoán để chuyển ra khỏi Việt Nam.\nNhững tình huống là dấu hiệu đáng ngờ là:",
    "I, II và IV", ["I, II và III", "II và IV", "I, III và IV"], 3,
    "Điều 31 liệt kê dấu hiệu đáng ngờ trong lĩnh vực chứng khoán, gồm: tài khoản đột nhiên nhận khoản tiền lớn không phù hợp khả năng tài chính (khoản 6) – I; khách hàng thường xuyên bán tất cả cổ phiếu và đề nghị công ty ký ủy nhiệm chi để rút tiền mặt (khoản 4) – II; người không cư trú chuyển số tiền lớn từ tài khoản giao dịch chứng khoán hoặc thanh lý hợp đồng ủy thác để chuyển tiền ra khỏi Việt Nam (khoản 3) – IV. Đầu tư định kỳ từ thu nhập hợp pháp, ổn định (III) không có dấu hiệu bất thường. Khi có dấu hiệu đáng ngờ, công ty phải xem xét, phân tích và báo cáo giao dịch đáng ngờ cho Ngân hàng Nhà nước Việt Nam (Điều 26).",
    "Khoản 3, 4, 6 Điều 31, Điều 26 " + PCRT_B,
    "6. Tài khoản chứng khoán của khách hàng đột nhiên nhận được một khoản tiền lớn không phù hợp với khả năng tài chính của khách hàng.",
    PCRT)

# 020 – Luật PCRT Điều 26, 37: báo cáo giao dịch đáng ngờ
add(2, "Theo Luật Phòng, chống rửa tiền 2022, công ty chứng khoán phải báo cáo giao dịch đáng ngờ cho cơ quan nào và trong thời hạn nào (trường hợp thông thường)?",
    "Ngân hàng Nhà nước Việt Nam; 03 ngày làm việc từ ngày phát sinh giao dịch hoặc 01 ngày làm việc từ ngày phát hiện",
    ["Ủy ban Chứng khoán Nhà nước; 05 ngày làm việc kể từ ngày phát sinh giao dịch đáng ngờ của khách hàng",
     "Bộ Công an; trong vòng 24 giờ kể từ khi phát sinh mọi giao dịch đáng ngờ, không phân biệt trường hợp",
     "Ngân hàng Nhà nước Việt Nam; 10 ngày kể từ ngày kết thúc tháng có phát sinh giao dịch đáng ngờ"], 1,
    "Điều 26: đối tượng báo cáo báo cáo giao dịch đáng ngờ cho Ngân hàng Nhà nước Việt Nam. Khoản 2 Điều 37: thời hạn 03 ngày làm việc kể từ ngày phát sinh giao dịch hoặc 01 ngày làm việc kể từ ngày phát hiện giao dịch đáng ngờ. Thời hạn 24 giờ (khoản 3 Điều 37) chỉ áp dụng khi giao dịch đáng ngờ do khách hàng yêu cầu có dấu hiệu liên quan đến tội phạm, và phải báo cáo cả cơ quan nhà nước có thẩm quyền lẫn Ngân hàng Nhà nước. Bộ Tài chính (UBCKNN) thanh tra, giám sát hoạt động phòng, chống rửa tiền của công ty chứng khoán (khoản 2 Điều 51) nhưng không phải nơi nhận báo cáo giao dịch đáng ngờ.",
    "Khoản 1 Điều 26, khoản 2, 3 Điều 37, khoản 2 Điều 51 " + PCRT_B,
    "Đối tượng báo cáo phải báo cáo giao dịch đáng ngờ quy định tại Điều 26 của Luật này trong thời hạn 03 ngày làm việc kể từ ngày phát sinh giao dịch hoặc trong thời hạn 01 ngày làm việc kể từ ngày đối tượng báo cáo phát hiện được giao dịch đáng ngờ.",
    PCRT)

# 021 – Luật PCRT Điều 44: trì hoãn giao dịch
add(3, "Khách hàng M yêu cầu công ty chứng khoán K chuyển toàn bộ tiền bán chứng khoán sang tài khoản của tổ chức N. K có căn cứ nghi ngờ N thuộc Danh sách đen. Theo Luật Phòng, chống rửa tiền 2022, K phải xử lý thế nào?",
    "Áp dụng ngay trì hoãn giao dịch, báo cáo ngay cơ quan có thẩm quyền và Ngân hàng Nhà nước; trì hoãn không quá 03 ngày làm việc",
    ["Vẫn chuyển tiền theo yêu cầu của M, sau đó báo cáo giao dịch đáng ngờ cho Ngân hàng Nhà nước trong 03 ngày làm việc",
     "Trì hoãn giao dịch tối đa 15 ngày làm việc để chờ Ủy ban Chứng khoán Nhà nước có ý kiến chấp thuận bằng văn bản",
     "Tự phong tỏa toàn bộ tài khoản của M và N cho đến khi tòa án có bản án hoặc quyết định đã có hiệu lực pháp luật"], 2,
    "Điểm a khoản 1 Điều 44: đối tượng báo cáo phải áp dụng ngay biện pháp trì hoãn giao dịch khi có căn cứ nghi ngờ hoặc phát hiện các bên liên quan đến giao dịch thuộc Danh sách đen; khoản 2: phải báo cáo ngay cho cơ quan nhà nước có thẩm quyền và Ngân hàng Nhà nước Việt Nam; khoản 3: thời hạn trì hoãn không quá 03 ngày làm việc; khoản 4: đối tượng báo cáo không chịu trách nhiệm pháp lý về hậu quả khi trì hoãn đúng quy định. Vẫn thực hiện giao dịch là sai; công ty không tự phong tỏa tài khoản tới khi có bản án.",
    "Điểm a khoản 1, khoản 2, 3, 4 Điều 44 " + PCRT_B,
    "Thời hạn áp dụng biện pháp trì hoãn giao dịch không quá 03 ngày làm việc kể từ ngày bắt đầu áp dụng.",
    PCRT)

# 022 – Luật PCRT Điều 38: thời hạn lưu trữ
add(1, "Theo Luật Phòng, chống rửa tiền 2022, công ty chứng khoán phải lưu trữ thông tin, hồ sơ, tài liệu nhận biết khách hàng trong thời hạn:",
    "05 năm kể từ ngày kết thúc giao dịch hoặc ngày đóng tài khoản hoặc ngày báo cáo",
    ["10 năm kể từ ngày kết thúc giao dịch hoặc ngày đóng tài khoản hoặc ngày báo cáo",
     "03 năm kể từ ngày kết thúc giao dịch hoặc ngày đóng tài khoản hoặc ngày báo cáo",
     "05 năm kể từ ngày khách hàng ký hợp đồng mở tài khoản giao dịch chứng khoán"], 3,
    "Khoản 2 Điều 38: thông tin, hồ sơ, tài liệu nhận biết khách hàng, kết quả phân tích, đánh giá và tài liệu khác liên quan đến khách hàng, giao dịch phải báo cáo được lưu trữ 05 năm kể từ ngày kết thúc giao dịch hoặc ngày đóng tài khoản hoặc ngày báo cáo; các báo cáo giao dịch (giao dịch giá trị lớn, đáng ngờ, chuyển tiền điện tử) lưu 05 năm kể từ ngày phát sinh giao dịch. Mốc tính không phải ngày mở tài khoản.",
    "Khoản 1, 2 Điều 38 " + PCRT_B,
    "a) 05 năm kể từ ngày kết thúc giao dịch hoặc ngày đóng tài khoản hoặc ngày báo cáo đối với các thông tin, hồ sơ, tài liệu quy định tại các điểm a, b và c khoản 1 Điều này;",
    PCRT)

# 023 – TT 121 Điều 15a (bổ sung bởi TT 08/2026): nhận biết nhà đầu tư nước ngoài qua tổ chức đại diện
add(2, "Tổ chức kinh doanh chứng khoán nước ngoài F dùng số hiệu tài khoản lưu ký của nhà đầu tư nước ngoài không cư trú G để đặt lệnh giao dịch tại công ty chứng khoán K. Theo Thông tư 121/2020/TT-BTC (bổ sung bởi Thông tư 08/2026/TT-BTC), phát biểu nào đúng về nghĩa vụ của K?",
    "K phải nhận biết cả G và F theo quy định pháp luật về phòng, chống rửa tiền",
    ["K chỉ nhận biết F, vì K không ký hợp đồng mở tài khoản giao dịch với G",
     "K không phải nhận biết G hay F, vì thông tin của G đã được VSDC quản lý",
     "K chỉ nhận biết G khi tổng giá trị giao dịch trong ngày đạt mức phải báo cáo"], 0,
    "Điều 15a Thông tư 121/2020 (bổ sung bởi Điều 12 Thông tư 08/2026/TT-BTC, hiệu lực 03/02/2026): tổ chức kinh doanh chứng khoán nước ngoài đại diện được dùng số hiệu tài khoản lưu ký của nhà đầu tư nước ngoài để đặt lệnh cho nhà đầu tư không cư trú tại công ty chứng khoán trên cơ sở hợp đồng với công ty (khoản 1, 3); công ty chứng khoán phải nhận biết cả nhà đầu tư nước ngoài và tổ chức đại diện theo pháp luật về phòng, chống rửa tiền (khoản 2); tổ chức đại diện phải cung cấp thông tin nhà đầu tư, thông tin giao dịch khi công ty hoặc cơ quan nhà nước yêu cầu (khoản 4).",
    "Khoản 1, 2, 3, 4 Điều 15a Thông tư 121/2020/TT-BTC (bổ sung bởi Điều 12 Thông tư 08/2026/TT-BTC; VBHN 09/VBHN-BTC năm 2026)",
    "Công ty chứng khoán phải thực hiện nhận biết nhà đầu tư nước ngoài, tổ chức kinh doanh chứng khoán nước ngoài đại diện theo quy định pháp luật về phòng, chống rửa tiền.",
    TT121)

# ======================= kiểm tra và ghi =======================
out = []
for i, x in enumerate(Q, 1):
    if x['quote']:
        assert len(x['quote']) <= 300, (i, len(x['quote']))
        text = doc_text(x['src'])
        assert text and (norm_ws(x['quote']) in text or loose(x['quote']) in loose(text)), (i, x['quote'][:50])
    o = list(x['wrong']); o.insert(x['a'], x['correct'])
    lens = [len(s) for s in o]
    assert '\nI.' in x['q'] or max(lens) <= 1.7 * min(lens), (i, lens)
    assert not re.search(r"(phương án|đáp án|chọn|câu)\s+[A-D]\b", x['e']), i
    neg = re.search(r"\b(không(?! cư trú)|ngoại trừ)\b", x['q'].split('\n')[0], re.I)
    assert not neg or re.search(r"\b(KHÔNG|NGOẠI TRỪ)\b", x['q']), i
    out.append(dict(id=f"C15-{i:03d}", part="CM", subject="MG", topic=T, level=x['level'], q=x['q'], o=o, a=x['a'],
                    e=x['e'], basis=x['basis'], quote=x['quote'], src=x['src'], as_of="2026-11"))
with open(OUT, 'w', encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False, indent=1)
print("wrote", len(out), "| a:", dict(sorted(Counter(x['a'] for x in out).items())),
      "| level:", dict(sorted(Counter(x['level'] for x in out).items())),
      "| tổ hợp:", sum('\nI.' in x['q'] for x in out))
