# Soát 3 chuyên đề slide SRTC môn Môi giới (Tổng quan; Xây dựng mạng lưới KH; Kiến thức và kỹ năng):
# sinh câu mới cho các ý ngân hàng chưa có -> ../cm_13.json, kèm tự kiểm tra (trích dẫn khớp nguyên văn,
# độ dài phương án, giải thích không nhắc tên phương án, chủ đề đúng chuyên đề MG).
# Chạy: python3 -I gen_c13.py
import json, re, unicodedata

OUT = '/home/user/cchn_moi/web/data/src/cm_13.json'
VB = '/home/user/cchn_moi/tai_lieu_phap_ly/van_ban_txt/'
LCK = 'VBHN_102_VBHN-VPQH_2026_Luat_Chung_khoan_hop_nhat.txt'
TT121 = 'VBHN_09_VBHN-BTC_2026_TT121_68_08_hop_nhat.txt'
B_LCK = ' Luật Chứng khoán 2019 (VBHN 102/VBHN-VPQH/2026)'
B_121 = ' Thông tư 121/2020/TT-BTC (VBHN 09/VBHN-BTC/2026, hợp nhất TT 68/2024 và TT 08/2026)'
GT = 'Giáo trình Môi giới và tư vấn đầu tư chứng khoán (UBCKNN/SRTC) – '
T1 = 'Tổng quan về môi giới và tư vấn đầu tư chứng khoán'
T2 = 'Kiến thức và kỹ năng cần thiết của người môi giới chứng khoán và tư vấn đầu tư chứng khoán'
T3 = 'Xây dựng mạng lưới khách hàng và chăm sóc khách hàng'

Q = []
def add(topic, level, q, o, a, e, basis, quote='', src=''):
    Q.append(dict(id=f'C13-{len(Q) + 1:03d}', part='CM', subject='MG', topic=topic, level=level,
                  q=q, o=o, a=a, e=e, basis=basis, quote=quote, src=src, as_of='2026-11'))

# ---------------- Chuyên đề 1: Tổng quan (CTCK, nguyên tắc hoạt động, triết lý hành nghề) ----------------
add(T1, 2,
    'Theo Luật Chứng khoán, những tổ chức nào sau đây được thực hiện nghiệp vụ tư vấn đầu tư chứng khoán?\n'
    'I. Công ty chứng khoán được cấp phép nghiệp vụ tư vấn đầu tư chứng khoán\n'
    'II. Công ty quản lý quỹ đầu tư chứng khoán\n'
    'III. Chi nhánh công ty chứng khoán nước ngoài tại Việt Nam\n'
    'IV. Ngân hàng thương mại làm ngân hàng giám sát cho quỹ đầu tư chứng khoán',
    ['Chỉ I', 'I và II', 'I, II và III', 'II, III và IV'], 2,
    'Khoản 1 Điều 72: tư vấn đầu tư chứng khoán là một nghiệp vụ của công ty chứng khoán. Khoản 1 Điều 73: '
    'công ty quản lý quỹ được thực hiện quản lý quỹ, quản lý danh mục và tư vấn đầu tư chứng khoán (cấp chung '
    'trong Giấy phép). Khoản 7 Điều 86: chi nhánh công ty chứng khoán nước ngoài tại Việt Nam chỉ được thực hiện '
    'nghiệp vụ tư vấn đầu tư chứng khoán. Ngân hàng giám sát không có nghiệp vụ này. Vì vậy, cách nói “tư vấn đầu tư '
    'chứng khoán là hoạt động chỉ công ty chứng khoán mới được thực hiện” là không chính xác.',
    'Khoản 1 Điều 72, khoản 1 Điều 73, khoản 7 Điều 86' + B_LCK,
    'Công ty quản lý quỹ đầu tư chứng khoán được thực hiện các nghiệp vụ kinh doanh sau đây: a) Quản lý quỹ đầu tư '
    'chứng khoán; b) Quản lý danh mục đầu tư chứng khoán; c) Tư vấn đầu tư chứng khoán.', LCK)

add(T1, 2,
    'Theo quy định về hạn chế cho vay tại Thông tư 121/2020/TT-BTC, công ty chứng khoán ĐƯỢC thực hiện hoạt động nào sau đây?',
    ['Cho khách hàng vay tiền mua chứng khoán dưới hình thức giao dịch ký quỹ khi đã được phép',
     'Cho cổ đông lớn của công ty vay vốn ngắn hạn, có tài sản bảo đảm đầy đủ và hợp pháp',
     'Cho thành viên Ban Giám đốc vay tiền với lãi suất bằng lãi suất cho vay trên thị trường',
     'Dùng tiền gửi của khách hàng để bảo đảm nghĩa vụ thanh toán cho một đối tác của công ty'], 0,
    'Khoản 1 Điều 27: trừ các dịch vụ tại khoản 1 Điều 86 Luật Chứng khoán, công ty chứng khoán không được cho vay '
    'tiền, chứng khoán dưới mọi hình thức; khoản 4 cho phép công ty đã được thực hiện giao dịch ký quỹ cho khách hàng '
    'vay tiền mua chứng khoán dưới hình thức giao dịch ký quỹ. Khoản 3 cấm cho vay dưới bất kỳ hình thức nào đối với '
    'cổ đông lớn, thành viên Ban Giám đốc, Hội đồng quản trị, Ban kiểm soát… và người có liên quan của họ, dù có tài sản '
    'bảo đảm hay lãi suất thị trường. Khoản 2 cấm dùng tiền, tài sản của công ty hoặc của khách hàng để bảo đảm nghĩa '
    'vụ thanh toán cho bên thứ ba.',
    'Khoản 1, 2, 3, 4 Điều 27' + B_121,
    'Công ty chứng khoán đã được thực hiện giao dịch ký quỹ theo quy định pháp luật được cho khách hàng vay tiền mua '
    'chứng khoán dưới hình thức giao dịch ký quỹ theo hướng dẫn của Bộ Tài chính.', TT121)

add(T1, 2,
    'Theo Thông tư 121/2020/TT-BTC, xét các nhận định sau về giới hạn tài chính của công ty chứng khoán:\n'
    'I. Tỷ lệ tổng nợ trên vốn chủ sở hữu không vượt quá 05 lần; tổng nợ không tính tiền gửi giao dịch chứng khoán của khách hàng\n'
    'II. Nợ ngắn hạn tối đa bằng tài sản ngắn hạn\n'
    'III. Giá trị còn lại của tài sản cố định và bất động sản làm trụ sở, chi nhánh không vượt quá 70% tổng tài sản\n'
    'IV. Tổng giá trị đầu tư vào trái phiếu doanh nghiệp không vượt quá 70% vốn chủ sở hữu\n'
    'Các nhận định đúng là:',
    ['I và II', 'I, II và IV', 'II, III và IV', 'I, III và IV'], 1,
    'Khoản 1 Điều 26: tổng nợ/vốn chủ sở hữu tối đa 05 lần; tổng nợ không gồm tiền gửi giao dịch chứng khoán của '
    'khách hàng, quỹ khen thưởng phúc lợi, dự phòng trợ cấp mất việc làm, dự phòng bồi thường thiệt hại cho nhà đầu tư. '
    'Khoản 2 Điều 26: nợ ngắn hạn tối đa bằng tài sản ngắn hạn. Khoản 3 Điều 28: đầu tư trái phiếu doanh nghiệp tối đa '
    '70% vốn chủ sở hữu. Nhận định III sai: theo khoản 2 Điều 28, giá trị còn lại của tài sản cố định và bất động sản '
    'không được vượt quá 50% tổng tài sản.',
    'Khoản 1, 2 Điều 26; khoản 2, 3 Điều 28' + B_121,
    'Nợ ngắn hạn của công ty chứng khoán tối đa bằng tài sản ngắn hạn.', TT121)

add(T1, 2,
    'Theo Thông tư 121/2020/TT-BTC, cách bố trí nào sau đây tại công ty chứng khoán vi phạm nguyên tắc tổ chức hệ thống quản trị rủi ro?',
    ['Giám đốc khối môi giới được giao kiêm nhiệm phụ trách bộ phận quản trị rủi ro của công ty',
     'Trưởng phòng tự doanh chịu trách nhiệm quản trị rủi ro trong phạm vi hoạt động của phòng mình',
     'Hạn mức rủi ro của từng nghiệp vụ được ban hành bằng văn bản và được rà soát, cập nhật thường xuyên',
     'Bộ phận quản trị rủi ro hoạt động độc lập với các bộ phận tác nghiệp như môi giới, tự doanh'], 0,
    'Điểm d khoản 1 Điều 11: bộ phận tác nghiệp và bộ phận quản trị rủi ro phải được tổ chức tách biệt, độc lập; người '
    'phụ trách bộ phận tác nghiệp (như khối môi giới) không đồng thời phụ trách bộ phận quản trị rủi ro và ngược lại. '
    'Trưởng các bộ phận nghiệp vụ vẫn có trách nhiệm quản trị rủi ro trong bộ phận mình (điểm a khoản 1); quy trình, '
    'hạn mức rủi ro phải bằng văn bản và được rà soát, cập nhật thường xuyên (điểm a khoản 1, khoản 2).',
    'Điểm a, d khoản 1, khoản 2 Điều 11' + B_121,
    'Hệ thống quản trị rủi ro được thiết lập phải đảm bảo các bộ phận tác nghiệp và bộ phận quản trị rủi ro được tổ chức '
    'tách biệt và độc lập với nhau và người phụ trách bộ phận tác nghiệp không đồng thời phụ trách bộ phận quản trị rủi ro '
    'và ngược lại.', TT121)

add(T1, 1,
    'Theo Thông tư 121/2020/TT-BTC, kế hoạch dự phòng cho các tình huống khẩn cấp nhằm bảo đảm tính liên tục trong hoạt '
    'động kinh doanh của công ty chứng khoán do ai xây dựng và ai thông qua?',
    ['Tổng giám đốc (Giám đốc) xây dựng, rà soát; Hội đồng quản trị (Hội đồng thành viên, Chủ sở hữu) thông qua',
     'Bộ phận công nghệ thông tin xây dựng, rà soát; Tổng giám đốc (Giám đốc) phê duyệt và ban hành áp dụng',
     'Bộ phận quản trị rủi ro xây dựng, rà soát; Ủy ban Chứng khoán Nhà nước chấp thuận trước khi áp dụng',
     'Ban kiểm soát xây dựng, rà soát; Đại hội đồng cổ đông (Hội đồng thành viên) thông qua hằng năm'], 0,
    'Khoản 4 Điều 11: công ty chứng khoán phải xây dựng kế hoạch dự phòng cho các tình huống khẩn cấp; Tổng giám đốc '
    '(Giám đốc) chịu trách nhiệm xây dựng, rà soát thường xuyên; kế hoạch phải được Hội đồng quản trị hoặc Hội đồng thành '
    'viên hoặc Chủ sở hữu công ty thông qua. Kế hoạch này đi cùng nghĩa vụ xây dựng hệ thống công nghệ thông tin, cơ sở dữ '
    'liệu dự phòng (khoản 10 Điều 89 Luật Chứng khoán); không có thủ tục UBCKNN chấp thuận trước kế hoạch dự phòng.',
    'Khoản 4 Điều 11' + B_121 + '; khoản 10 Điều 89' + B_LCK,
    'Tổng Giám đốc (Giám đốc) chịu trách nhiệm xây dựng, rà soát thường xuyên kế hoạch dự phòng. Kế hoạch dự phòng phải '
    'được Hội đồng quản trị hoặc Hội đồng thành viên hoặc Chủ sở hữu công ty thông qua.', TT121)

add(T1, 2,
    'Theo Thông tư 121/2020/TT-BTC, khi thực hiện hoạt động nghiệp vụ, công ty chứng khoán phải bảo đảm những nguyên tắc nào sau đây?\n'
    'I. Ban hành quy trình hoạt động cho các nghiệp vụ và quy tắc đạo đức hành nghề\n'
    'II. Được quyết định mua, bán thay khách hàng trên tài khoản giao dịch thông thường nếu khách hàng đồng ý qua điện thoại\n'
    'III. Thiết lập bộ phận chuyên trách thông tin liên lạc với khách hàng, giải quyết thắc mắc, khiếu nại của khách hàng\n'
    'IV. Xây dựng hệ thống công nghệ thông tin, cơ sở dữ liệu dự phòng để bảo đảm hoạt động an toàn, liên tục',
    ['I và III', 'I, III và IV', 'II, III và IV', 'I, II và IV'], 1,
    'Điều 4: công ty chứng khoán phải ban hành quy trình hoạt động cho các nghiệp vụ (khoản 1) và quy tắc đạo đức hành '
    'nghề (khoản 2); xây dựng hệ thống công nghệ thông tin, cơ sở dữ liệu dự phòng (khoản 9); thiết lập bộ phận chuyên trách '
    'liên lạc với khách hàng và giải quyết thắc mắc, khiếu nại (khoản 11). Ý II sai: công ty, nhân viên không được đầu tư '
    'thay khách hàng, trừ trường hợp ủy thác quản lý tài khoản của nhà đầu tư cá nhân theo Điều 19 (khoản 3, điểm a khoản 6 '
    'Điều 4); lời đồng ý qua điện thoại không biến tài khoản thông thường thành tài khoản ủy thác.',
    'Khoản 1, 2, 3, 9, 11 và điểm a khoản 6 Điều 4' + B_121,
    'Công ty chứng khoán phải thiết lập một bộ phận chuyên trách chịu trách nhiệm thông tin liên lạc với khách hàng và '
    'giải quyết các thắc mắc, khiếu nại của khách hàng.', TT121)

add(T1, 2,
    'Tổ chức Y đề nghị cấp Giấy phép thành lập và hoạt động công ty chứng khoán với hai nghiệp vụ môi giới và tư vấn đầu tư '
    'chứng khoán. Theo Luật Chứng khoán, yêu cầu về nhân sự mà Y phải đáp ứng là:',
    ['Có Tổng giám đốc; tối thiểu 03 người có CCHN phù hợp cho mỗi nghiệp vụ; tối thiểu 01 nhân viên kiểm soát tuân thủ',
     'Có Tổng giám đốc; tối thiểu 05 người có CCHN cho toàn công ty; tối thiểu 01 nhân viên kiểm toán nội bộ',
     'Có Tổng giám đốc; tối thiểu 02 người có CCHN phù hợp cho mỗi nghiệp vụ; tối thiểu 01 nhân viên kiểm soát tuân thủ',
     'Có Tổng giám đốc; tối thiểu 03 người có CCHN cho toàn công ty; không bắt buộc có nhân viên kiểm soát tuân thủ'], 0,
    'Khoản 5 Điều 74: có Tổng giám đốc (Giám đốc), tối thiểu 03 nhân viên có chứng chỉ hành nghề chứng khoán phù hợp cho '
    'mỗi nghiệp vụ đề nghị cấp phép và tối thiểu 01 nhân viên kiểm soát tuân thủ; Tổng giám đốc phải có CCHN phân tích tài '
    'chính hoặc quản lý quỹ. Con số 05 người có CCHN là điều kiện của công ty quản lý quỹ (khoản 5 Điều 75); 02 người cho '
    'mỗi nghiệp vụ là điều kiện khi công ty chứng khoán lập chi nhánh trong nước (Nghị định 155/2020/NĐ-CP).',
    'Khoản 5 Điều 74' + B_LCK,
    'Có Tổng giám đốc (Giám đốc), tối thiểu 03 nhân viên có chứng chỉ hành nghề chứng khoán phù hợp cho mỗi nghiệp vụ '
    'kinh doanh chứng khoán đề nghị cấp phép và tối thiểu 01 nhân viên kiểm soát tuân thủ.', LCK)

add(T1, 1,
    'Vai trò của công ty chứng khoán đối với thị trường chứng khoán và nền kinh tế bao gồm các nội dung sau, NGOẠI TRỪ:',
    ['Bảo đảm giá trị khoản đầu tư của khách hàng không bị sụt giảm',
     'Tạo cơ chế huy động vốn cho doanh nghiệp và nền kinh tế',
     'Góp phần giảm chi phí giao dịch, nâng cao hiệu quả đầu tư',
     'Hỗ trợ cơ quan quản lý giám sát thị trường hiệu quả hơn'], 0,
    'Công ty chứng khoán tạo cơ chế huy động vốn, giảm chi phí giao dịch và rủi ro, nâng cao hiệu quả đầu tư, góp phần '
    'tạo sản phẩm, dịch vụ mới và hỗ trợ cơ quan quản lý giám sát thị trường. Công ty không bảo đảm khách hàng không bị '
    'lỗ: nhà đầu tư tự chịu trách nhiệm về rủi ro (khoản 4 Điều 5 Luật Chứng khoán); công ty không được bảo đảm khách '
    'hàng không bị thua lỗ, trừ trường hợp đầu tư vào chứng khoán có thu nhập cố định (khoản 1 Điều 91 Luật Chứng khoán).',
    GT + 'vai trò của công ty chứng khoán; khoản 4 Điều 5, khoản 1 Điều 91 Luật Chứng khoán 2019 (VBHN 102/VBHN-VPQH/2026)')

add(T1, 1,
    'Trong cơ cấu tổ chức thường gặp của công ty chứng khoán, bộ phận nào sau đây KHÔNG thuộc khối nghiệp vụ (front office)?',
    ['Phòng kế toán – ngân quỹ', 'Phòng môi giới chứng khoán', 'Phòng tự doanh chứng khoán', 'Phòng bảo lãnh phát hành'], 0,
    'Khối nghiệp vụ (front office) trực tiếp thực hiện các giao dịch kinh doanh và dịch vụ chứng khoán: môi giới, tự doanh, '
    'bảo lãnh phát hành, tư vấn tài chính và đầu tư… Khối hỗ trợ (back office) phục vụ khối nghiệp vụ, gồm kế toán, ngân '
    'quỹ, nhân sự, công nghệ thông tin, thanh toán – lưu ký… nên phòng kế toán – ngân quỹ thuộc khối hỗ trợ.',
    GT + 'cơ cấu tổ chức của công ty chứng khoán (khối nghiệp vụ và khối hỗ trợ)')

add(T1, 2,
    'Nhân viên môi giới hành nghề theo triết lý “bán hàng tư vấn” sẽ làm việc với khách hàng theo cách nào sau đây?',
    ['Tìm hiểu kỹ nhu cầu, hoàn cảnh của từng khách hàng rồi đề xuất sản phẩm đáp ứng tốt nhất',
     'Chào bán càng nhiều càng tốt những sản phẩm công ty đang có sẵn, không cần phân biệt khách hàng',
     'Nghiên cứu nhu cầu chung của thị trường để thiết kế sản phẩm mới rồi chào bán đại trà',
     'Ưu tiên giới thiệu sản phẩm mang lại phí, hoa hồng cao nhất cho công ty và cho bản thân'], 0,
    'Có ba triết lý: truyền thống (bán càng nhiều càng tốt những gì có sẵn), bán hàng – tiếp thị (tìm hiểu nhu cầu thị '
    'trường để tạo ra sản phẩm rồi bán) và bán hàng tư vấn (tìm hiểu từng khách hàng cần gì rồi đáp ứng bằng sản phẩm phù '
    'hợp nhất). Bán hàng tư vấn phù hợp với nguyên tắc tính phù hợp: khuyến nghị phải hợp với tình hình tài chính, mục tiêu '
    'và khả năng chấp nhận rủi ro của khách hàng (khoản 6 Điều 89 Luật Chứng khoán). Ưu tiên sản phẩm hoa hồng cao là '
    'biểu hiện xung đột lợi ích.',
    GT + 'triết lý hành nghề môi giới (bán hàng tư vấn); khoản 6 Điều 89 Luật Chứng khoán 2019')

# ---------------- Chuyên đề 2: Xây dựng mạng lưới khách hàng ----------------
add(T3, 2,
    'Xét các nhận định sau về phạm vi chăm sóc khách hàng của nhân viên môi giới:\n'
    'I. Việc chăm sóc bắt đầu ngay từ khi người đó còn là khách hàng tiềm năng\n'
    'II. Với khách hàng đang giao dịch thường xuyên, cần duy trì liên hệ và định kỳ rà soát nhu cầu\n'
    'III. Khi khách hàng đã ngừng giao dịch, vẫn nên giữ liên hệ thiện chí và tìm hiểu lý do rời đi\n'
    'Các nhận định đúng là:',
    ['Chỉ II', 'I và II', 'II và III', 'I, II và III'], 3,
    'Chăm sóc khách hàng được thực hiện ở cả ba giai đoạn: khi là khách hàng tiềm năng (tạo thiện cảm, cung cấp thông tin '
    'hữu ích), khi là khách hàng thân thiết (duy trì liên hệ, rà soát danh mục và nhu cầu) và khi không còn là khách hàng '
    '(giữ quan hệ, tìm hiểu nguyên nhân để cải thiện dịch vụ, tạo cơ hội để khách hàng quay lại hoặc giới thiệu người khác).',
    GT + 'chăm sóc khách hàng ở ba giai đoạn (tiềm năng, thân thiết, không còn là khách hàng)')

add(T3, 2,
    'Chị K gửi tiết kiệm lâu năm tại ngân hàng mẹ của công ty chứng khoán A và đã đồng ý nhận thông tin về sản phẩm của các '
    'công ty trong tập đoàn. Nhân viên môi giới của A liên hệ, giới thiệu dịch vụ chứng khoán phù hợp với chị K. Đây là cách '
    'tìm kiếm khách hàng thông qua:',
    ['Bán chéo sản phẩm, dịch vụ giữa các đơn vị trong cùng hệ thống',
     'Khách hàng hiện tại của chính nhân viên môi giới giới thiệu',
     'Trung tâm ảnh hưởng như luật sư, kế toán, hiệp hội doanh nghiệp',
     'Gọi điện chào hàng ngẫu nhiên theo danh bạ không chọn lọc'], 0,
    'Nguồn khách hàng của nhân viên môi giới gồm: bạn bè, người thân; khách hàng do công ty phân bổ; khách hàng hiện tại '
    'giới thiệu; bán chéo sản phẩm (khách hàng của đơn vị khác trong cùng hệ thống, tập đoàn được giới thiệu thêm sản phẩm '
    'chứng khoán); internet, mạng xã hội; hội thảo chuyên ngành, đại hội cổ đông… Chị K đến từ hệ thống ngân hàng mẹ nên '
    'đây là bán chéo. Việc dùng thông tin khách hàng của ngân hàng phải có sự đồng ý của khách hàng, như trong tình huống.',
    GT + 'nguồn khách hàng tiềm năng (bán chéo sản phẩm)')

add(T3, 2,
    'Khi phân loại nhu cầu và mục tiêu đầu tư của một khách hàng tiềm năng, trình tự hợp lý mà nhân viên môi giới nên thực hiện là:',
    ['Thiết lập quan hệ → Phát hiện nhu cầu, mục tiêu → Sắp xếp ưu tiên → Xác định giới hạn → Thảo luận giải pháp',
     'Phát hiện nhu cầu, mục tiêu → Thảo luận giải pháp → Thiết lập quan hệ → Sắp xếp ưu tiên → Xác định giới hạn',
     'Thiết lập quan hệ → Thảo luận giải pháp → Phát hiện nhu cầu, mục tiêu → Xác định giới hạn → Sắp xếp ưu tiên',
     'Thiết lập quan hệ → Phát hiện nhu cầu, mục tiêu → Thảo luận giải pháp → Sắp xếp ưu tiên → Xác định giới hạn'], 0,
    'Các bước: (1) thiết lập quan hệ tốt với khách hàng tiềm năng; (2) phát hiện nhu cầu, mục tiêu, vấn đề riêng; (3) sắp '
    'xếp thứ tự ưu tiên; (4) xác định giới hạn của từng nhu cầu (rủi ro, thời hạn, số tiền…); (5) thống nhất kỳ vọng; (6) '
    'xem xét từng mục tiêu và khả năng thực hiện trước khi gợi ý bất kỳ giải pháp nào; (7) gặp gỡ, thảo luận các giải pháp '
    'khả thi. Giải pháp chỉ được đưa ra sau khi đã rõ ưu tiên và giới hạn của từng mục tiêu.',
    GT + 'phân loại nhu cầu và mục tiêu đầu tư của khách hàng (các bước xây dựng hồ sơ khách hàng)')

add(T3, 2,
    'Khi khai thác thông tin để lập hồ sơ khách hàng, câu hỏi nào sau đây chủ yếu nhằm đánh giá mức độ chấp nhận rủi ro của khách hàng?',
    ['“Nếu danh mục giảm 20% trong một tháng, anh/chị sẽ cảm thấy thế nào và xử lý ra sao?”',
     '“Khoản đầu tư thành công nhất anh/chị từng thực hiện là khoản nào, vì sao?”',
     '“Anh/chị đang mở tài khoản ở công ty nào và hài lòng điều gì ở người môi giới?”',
     '“Anh/chị cần khoản thu nhập bao nhiêu mỗi năm từ danh mục và dùng vào việc gì?”'], 0,
    'Nhóm câu hỏi về rủi ro có thể chấp nhận hỏi khách hàng sẵn sàng chịu mức lỗ bao nhiêu, phản ứng thế nào khi thua lỗ. '
    'Câu hỏi về khoản đầu tư thành công nhất thuộc nhóm lịch sử đầu tư; câu hỏi về công ty, người môi giới hiện tại thuộc '
    'nhóm thông tin liên quan đến nhà môi giới; câu hỏi về khoản thu nhập cần có thuộc nhóm mục tiêu thu nhập.',
    GT + 'các nhóm câu hỏi khai thác nhu cầu, mục tiêu và khả năng chấp nhận rủi ro của khách hàng')

add(T3, 2,
    'Ông A và bà B có tài sản ròng, thu nhập và thời gian đầu tư tương đương nhau. Ông A tự gây dựng tài sản qua nhiều năm '
    'khởi nghiệp, điều hành doanh nghiệp; tài sản của bà B chủ yếu do thừa kế. Khi xét nguồn gốc tài sản trong hồ sơ khách '
    'hàng cá nhân, nhận định nào sau đây thường đúng?',
    ['Ông A thường sẵn sàng chấp nhận rủi ro cao hơn vì quen chủ động chấp nhận rủi ro để tạo tài sản',
     'Bà B thường sẵn sàng chấp nhận rủi ro cao hơn vì tài sản có được không do công sức tích lũy',
     'Nguồn gốc tài sản không ảnh hưởng thái độ với rủi ro; chỉ quy mô tài sản mới cần được xem xét',
     'Hai người phải được xếp cùng một mức rủi ro vì tài sản ròng và thu nhập của họ như nhau'], 0,
    'Nguồn gốc của sự giàu có là một yếu tố trong hồ sơ khách hàng cá nhân (cùng với giai đoạn cuộc đời, hồ sơ tâm lý…). '
    'Người tự tạo ra tài sản bằng kinh doanh thường tự tin, quen chấp nhận rủi ro và cảm thấy kiểm soát được kết quả nên '
    'mức sẵn sàng chấp nhận rủi ro thường cao hơn. Người có tài sản do thừa kế thường thận trọng hơn vì lo mất phần tài sản '
    'khó tạo lại. Đây là xu hướng chung; nhân viên môi giới vẫn phải kiểm chứng qua trao đổi với từng khách hàng.',
    GT + 'hồ sơ khách hàng cá nhân: nguồn gốc của sự giàu có')

add(T3, 3,
    'Anh Q, 35 tuổi, có ba mục tiêu: (1) quỹ dự phòng bằng 6 tháng chi tiêu, có thể cần bất cứ lúc nào; (2) học phí đại học '
    'cho con sau 4 năm; (3) nghỉ hưu sau 25 năm. Theo nguyên tắc mỗi mục tiêu gắn với một phần danh mục và một mức rủi ro '
    'thích hợp, cách phân bổ nào sau đây hợp lý nhất?',
    ['(1) tiền gửi, công cụ thanh khoản cao; (2) chủ yếu trái phiếu, tiền gửi kỳ hạn khớp 4 năm; (3) tỷ trọng cổ phiếu cao',
     '(1) cổ phiếu tăng trưởng; (2) trái phiếu kỳ hạn 10 năm lợi suất cao; (3) tiền gửi tiết kiệm để bảo toàn vốn',
     'Gộp cả ba mục tiêu vào một danh mục rủi ro trung bình, cùng một tỷ trọng cổ phiếu và trái phiếu như nhau',
     'Dồn toàn bộ vào cổ phiếu tăng trưởng vì anh Q còn trẻ, thời gian đầu tư dài cho cả ba mục tiêu của mình'], 0,
    'Mỗi mục tiêu ứng với một tỷ lệ trong danh mục và một mức rủi ro phù hợp với thời hạn, tính thanh khoản của mục tiêu đó. '
    'Quỹ dự phòng cần rút được ngay nên dùng tiền gửi, công cụ thanh khoản cao. Học phí sau 4 năm cần ổn định nên dùng trái '
    'phiếu, tiền gửi có kỳ hạn tương ứng. Mục tiêu nghỉ hưu sau 25 năm chịu được biến động ngắn hạn nên có thể dùng tỷ trọng '
    'cổ phiếu cao. Gộp chung một mức rủi ro hoặc dồn hết vào cổ phiếu bỏ qua ràng buộc thanh khoản và thời hạn của mục tiêu '
    'ngắn hạn; trái phiếu 10 năm không khớp thời hạn 4 năm.',
    GT + 'đánh giá hồ sơ đầu tư: mỗi mục tiêu gắn với một tỷ lệ danh mục và mức rủi ro thích hợp')

add(T3, 2,
    'Nhân viên môi giới cần thường xuyên theo dõi, quản lý tài khoản và điều chỉnh danh mục của khách hàng vì những lý do nào sau đây?\n'
    'I. Nhân viên môi giới cần đạt chỉ tiêu số lệnh giao dịch hằng tháng\n'
    'II. Hoàn cảnh, nhu cầu và mục tiêu của khách hàng thay đổi\n'
    'III. Điều kiện thị trường vốn thay đổi, làm thay đổi kỳ vọng lợi nhuận và rủi ro\n'
    'IV. Biến động giá làm tỷ trọng tài sản thực tế lệch khỏi phân bổ tài sản chiến lược',
    ['II và IV', 'II, III và IV', 'I, II và III', 'I, III và IV'], 1,
    'Quản lý tài khoản khách hàng là cần thiết vì: nhu cầu và hoàn cảnh của khách hàng thay đổi; điều kiện thị trường vốn '
    'thay đổi nên kỳ vọng phải được điều chỉnh; biến động giá làm phân bổ tài sản hiện tại lệch khỏi phân bổ chiến lược, '
    'cần tái cân bằng. Giao dịch để đạt chỉ tiêu số lệnh là giao dịch quá mức (churning), đi ngược lợi ích khách hàng.',
    GT + 'quản lý tài khoản khách hàng (lý do điều chỉnh, tái cân bằng danh mục)')

# ---------------- Chuyên đề 3: Kiến thức và kỹ năng ----------------
add(T2, 2,
    'Nhận định nào sau đây mô tả đúng một phương thức đầu tư trái phiếu?',
    ['Kinh doanh chênh lệch giá: mua trái phiếu ở thị trường giá thấp, đồng thời bán ở thị trường giá cao',
     'Đầu tư ngân quỹ: ưu tiên trái phiếu dài hạn lợi suất cao, chấp nhận tính thanh khoản thấp',
     'Mua và nắm giữ: liên tục mua bán trái phiếu để hưởng chênh lệch giá trong ngắn hạn',
     'Đầu tư phòng vệ: vay thêm vốn mua trái phiếu để khuếch đại lợi nhuận kỳ vọng của danh mục'], 0,
    'Đầu tư ngân quỹ dùng công cụ nợ có thanh khoản cao như chứng chỉ tiền gửi chuyển nhượng được, kỳ phiếu ngân hàng, tín '
    'phiếu kho bạc, trái phiếu Chính phủ. Mua và nắm giữ là giữ trái phiếu lâu dài, thường đến đáo hạn. Kinh doanh chênh lệch '
    'giá tận dụng việc cùng một trái phiếu có giá khác nhau trên hai thị trường: mua nơi giá thấp, bán ngay nơi giá cao. Đầu '
    'tư phòng vệ nhằm hạn chế rủi ro, không phải dùng đòn bẩy để tăng lợi nhuận.',
    GT + 'các phương thức đầu tư trái phiếu (ngân quỹ, mua và nắm giữ, chênh lệch giá, phòng vệ)')

add(T2, 2,
    'Theo Luật Chứng khoán, loại chứng khoán nào sau đây được niêm yết trên hệ thống giao dịch chứng khoán theo đề nghị của tổ '
    'chức phát hành hoặc tổ chức được ủy quyền phát hành, thay vì thuộc nhóm bắt buộc phải niêm yết, đăng ký giao dịch?',
    ['Trái phiếu chính quyền địa phương và trái phiếu được Chính phủ bảo lãnh',
     'Cổ phiếu của công ty đại chúng chưa niêm yết trên Sở giao dịch chứng khoán',
     'Chứng chỉ quỹ hoán đổi danh mục được Ủy ban Chứng khoán Nhà nước chấp thuận',
     'Chứng quyền có bảo đảm do công ty chứng khoán phát hành, được UBCKNN chấp thuận'], 0,
    'Khoản 1 Điều 48: chứng khoán đã chào bán ra công chúng, cổ phiếu của công ty đại chúng, chứng chỉ quỹ đóng, chứng chỉ quỹ '
    'hoán đổi danh mục, chứng quyền có bảo đảm, hợp đồng tương lai, hợp đồng quyền chọn do UBCKNN chấp thuận phải được niêm '
    'yết, đăng ký giao dịch. Khoản 2 Điều 48: công cụ nợ của Chính phủ, trái phiếu được Chính phủ bảo lãnh và trái phiếu chính '
    'quyền địa phương được niêm yết theo đề nghị của tổ chức phát hành hoặc tổ chức được ủy quyền phát hành.',
    'Khoản 1, 2 Điều 48' + B_LCK,
    'Công cụ nợ của Chính phủ, trái phiếu được Chính phủ bảo lãnh và trái phiếu chính quyền địa phương được niêm yết trên hệ '
    'thống giao dịch chứng khoán theo đề nghị của tổ chức phát hành hoặc tổ chức được ủy quyền phát hành theo quy định của '
    'pháp luật.', LCK)

add(T2, 2,
    'Khi giải thích cho một khách hàng quen giao dịch cổ phiếu muốn chuyển sang giao dịch hợp đồng tương lai chỉ số, nhân viên '
    'môi giới nêu các nhận định sau:\n'
    'I. Có thể mở vị thế bán mà không cần sở hữu tài sản cơ sở\n'
    'II. Khi mở vị thế chỉ cần nộp ký quỹ, không phải thanh toán đủ giá trị hợp đồng\n'
    'III. Lãi, lỗ chỉ được thanh toán một lần khi đóng vị thế hoặc khi hợp đồng đáo hạn\n'
    'IV. Hợp đồng có tháng đáo hạn, cần chọn hợp đồng có thời hạn phù hợp với kế hoạch giao dịch\n'
    'Các nhận định đúng là:',
    ['I và II', 'I, II và IV', 'II, III và IV', 'I, III và IV'], 1,
    'Khác với cổ phiếu (mua phải đủ tiền, bán phải có cổ phiếu), với hợp đồng tương lai nhà đầu tư không cần đủ toàn bộ tiền '
    'để mở vị thế mua, không cần nắm giữ tài sản cơ sở để mở vị thế bán; ký quỹ đóng vai trò khoản đặt cọc bảo đảm nghĩa vụ. '
    'Hợp đồng có ngày đáo hạn nên phải chọn tháng đáo hạn phù hợp. Ý III sai: lãi, lỗ vị thế được xác định và thanh toán hằng '
    'ngày theo giá thanh toán cuối ngày (thời hạn nộp, nhận tiền cụ thể theo quy chế của VSDC).',
    GT + 'kiến thức về sản phẩm phái sinh: ký quỹ, thanh toán lãi lỗ hằng ngày, tháng đáo hạn')

add(T2, 2,
    'Để tạo lập sự tín nhiệm và lòng tin với khách hàng, nhân viên môi giới nên tuân thủ những nguyên tắc nào sau đây?\n'
    'I. Đưa ra các phương án phù hợp để khách hàng tự quyết định, không quyết định thay khách hàng\n'
    'II. Nhận vay tiền của khách hàng thân thiết khi khách hàng chủ động đề nghị và có giấy vay rõ ràng\n'
    'III. Áp dụng phương pháp làm việc nhất quán, tuân thủ các nguyên tắc đã cam kết với khách hàng',
    ['Chỉ I', 'I và III', 'II và III', 'I, II và III'], 1,
    'Nguyên tắc tạo lập tín nhiệm: cung cấp giải pháp, lựa chọn phù hợp để khách hàng quyết định, không quyết định thay; đặt '
    'lợi ích khách hàng lên đầu; có phương pháp nhất quán và tuyệt đối tuân thủ; không tư lợi về tiền bạc với khách hàng. Vay '
    'tiền của khách hàng, dù có giấy tờ, tạo quan hệ lợi ích cá nhân và xung đột lợi ích nên vi phạm nguyên tắc này.',
    GT + 'tạo lập sự tín nhiệm và lòng tin với khách hàng')

add(T2, 1,
    'So với dịch vụ thông thường, dịch vụ tài chính – chứng khoán còn mang thêm những nét riêng. Nét nào sau đây KHÔNG đúng?',
    ['Được bảo hộ độc quyền nên đối thủ khó sao chép',
     'Thường tích hợp trên nền tảng công nghệ hiện đại',
     'Cần phối hợp nhiều bộ phận, nhiều trung gian tài chính',
     'Luôn hàm chứa yếu tố rủi ro trong quá trình cung ứng'], 0,
    'Ngoài đặc điểm chung của dịch vụ, dịch vụ tài chính liên tục thay đổi, dễ bắt chước và không có bản quyền; được tích '
    'hợp trên nền tảng công nghệ cao; được cung cấp trên cơ sở liên kết nhiều bộ phận chức năng và nhiều trung gian tài '
    'chính; hàm chứa yếu tố rủi ro trong cung ứng. Vì dễ bị sao chép, lợi thế cạnh tranh bền vững của công ty chứng khoán '
    'chủ yếu đến từ chất lượng đội ngũ, uy tín và quan hệ với khách hàng.',
    GT + 'đặc tính của dịch vụ tài chính')

# đưa đáp án của câu không kết hợp về các vị trí khác nhau (câu kết hợp giữ thứ tự đã viết)
for k, q in enumerate([q for q in Q if '\nI. ' not in q['q']]):
    o = q['o'][:]; key = o.pop(q['a']); o.insert(k % 4, key); q['o'], q['a'] = o, k % 4

# ---------------- tự kiểm tra ----------------
TOPICS = {T1, T2, T3}
LETTER_IN_E = re.compile(r"(phương án|đáp án|chọn|câu)\s+[A-D]\b")
REF = re.compile(r"(\b[A-Da-d]\s*(và|,|&)\s*[A-Da-d]\b)|tất cả (các )?(phương án|đáp án|ý|câu) (trên|đều)|cả (hai|ba|bốn) (phương án|ý|đáp án)|không (có )?(phương án|đáp án|ý|câu) nào", re.I)
norm = lambda s: re.sub(r'\s+', ' ', unicodedata.normalize('NFC', s)).strip()
docs = {}
for q in Q:
    assert q['topic'] in TOPICS, q['id']
    assert len(q['o']) == 4 and len(set(q['o'])) == 4 and 0 <= q['a'] < 4, q['id']
    assert not LETTER_IN_E.search(q['e']), q['id']
    assert not any(REF.search(x) for x in q['o']), q['id']
    assert not re.search(r'\b(không|ngoại trừ)\b', q['q'].split('\n')[0]), ('phủ định phải viết HOA', q['id'])
    L =[len(x) for x in q['o']]
    if '\n' not in q['q']:  # câu kết hợp có phương án ngắn kiểu “I và II”
        assert max(L) / min(L) <= 1.35, (q['id'], L)
    if q['quote']:
        assert len(q['quote']) <= 300, (q['id'], len(q['quote']))
        if q['src'] not in docs:
            docs[q['src']] = norm(open(VB + q['src'], encoding='utf-8').read())
        assert norm(q['quote']) in docs[q['src']], ('trích dẫn không khớp', q['id'])
combo = [q['id'] for q in Q if '\nI. ' in q['q']]
json.dump(Q, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(Q), 'câu; kết hợp:', len(combo), combo)
print('vị trí đáp án:', [q['a'] for q in Q])
