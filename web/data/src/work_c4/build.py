"""Build cm_4.json (MG, 40 câu). Run: python3 -I build.py"""
import json

OUT = '/home/user/cchn_moi/web/data/src/cm_4.json'
LUAT = 'VBHN_24_VBHN-VPQH_2025_Luat_Chung_khoan_hop_nhat_Cong_bao.txt'
TT121 = 'VBHN_09_VBHN-BTC_2026_TT121_68_08_hop_nhat.txt'
ND155 = 'ND_155_2020_ND-CP_Cong_bao_so_45-56_2021.txt'
GT = 'Giáo trình SRTC (khung chương trình)'

T1 = 'Tổng quan về môi giới và tư vấn đầu tư chứng khoán'
T2 = 'Kiến thức và kỹ năng cần thiết của người môi giới chứng khoán và tư vấn đầu tư chứng khoán'
T3 = 'Xây dựng mạng lưới khách hàng và chăm sóc khách hàng'
T4 = 'Xung đột lợi ích và giải quyết xung đột lợi ích trong hoạt động môi giới và tư vấn đầu tư chứng khoán'
T5 = 'Quản lý Nhà nước đối với hoạt động môi giới và tư vấn đầu tư chứng khoán'

Q = []


def add(topic, level, q, o, a, e, basis, quote='', src=GT):
    Q.append(dict(id=f'C4-{len(Q) + 1:03d}', part='CM', subject='MG', topic=topic, level=level, q=q, o=o, a=a,
                  e=e, basis=basis, quote=quote, src=src, as_of='2026-11'))


# ---------------- T1: Tổng quan (6) ----------------
add(T1, 1,
    'Theo Luật Chứng khoán, công ty chứng khoán được cấp phép nghiệp vụ môi giới chứng khoán được cung cấp dịch vụ nào sau đây?',
    ['Tư vấn tái cơ cấu, hợp nhất, sáp nhập và mua bán doanh nghiệp',
     'Đầu tư, góp vốn, phát hành và chào bán các sản phẩm tài chính',
     'Nhận ủy thác quản lý tài khoản giao dịch của nhà đầu tư cá nhân',
     'Tư vấn hồ sơ chào bán và thực hiện thủ tục trước khi chào bán'], 2,
    'Điểm a khoản 1 Điều 86: CTCK có nghiệp vụ môi giới được nhận ủy thác quản lý tài khoản giao dịch chứng khoán của nhà đầu tư cá nhân, phân phối/làm đại lý phân phối chứng khoán, quản lý tài khoản giao dịch… Tư vấn tái cơ cấu, M&A và tư vấn hồ sơ chào bán gắn với nghiệp vụ bảo lãnh phát hành (khoản 3); đầu tư, góp vốn, phát hành sản phẩm tài chính gắn với nghiệp vụ tự doanh (khoản 2).',
    'Điểm a khoản 1, khoản 2, khoản 3 Điều 86 Luật Chứng khoán 2019 (VBHN 24/VBHN-VPQH/2025)',
    'Nhận ủy thác quản lý tài khoản giao dịch chứng khoán của nhà đầu tư cá nhân; thực hiện phân phối hoặc làm đại lý phân phối chứng khoán; quản lý tài khoản giao dịch chứng khoán',
    LUAT)

add(T1, 1,
    'Trên các thị trường có sàn giao dịch truyền thống, người môi giới hoạt động cho chính mình, nhận thực hiện lệnh hộ các công ty môi giới thành viên khi họ quá tải để hưởng một phần hoa hồng, thường được gọi là:',
    ['Môi giới ủy nhiệm (môi giới thừa hành)',
     'Môi giới độc lập (môi giới hai đô la)',
     'Nhà môi giới chuyên môn (chuyên gia)',
     'Môi giới chiết khấu (môi giới giảm giá)'], 1,
    'Môi giới độc lập (two-dollar broker) làm việc cho chính mình, nhận lệnh hộ các công ty môi giới khi họ quá tải và hưởng phí. Môi giới ủy nhiệm là nhân viên của công ty thành viên, thực hiện lệnh cho khách hàng của công ty; nhà môi giới chuyên môn (specialist) duy trì thị trường cho một số chứng khoán nhất định; môi giới chiết khấu chỉ thực hiện lệnh với mức phí thấp.',
    'Giáo trình Môi giới và tư vấn đầu tư chứng khoán – Chuyên đề 1: các loại hình môi giới chứng khoán')

add(T1, 1,
    'Căn cứ vào mức độ ủy quyền của khách hàng cho người tư vấn, hoạt động tư vấn đầu tư chứng khoán được phân thành:',
    ['Tư vấn trực tiếp và tư vấn gián tiếp',
     'Tư vấn cho tổ chức phát hành và cho nhà đầu tư',
     'Tư vấn có thu phí và tư vấn không thu phí',
     'Tư vấn gợi ý và tư vấn ủy quyền'], 3,
    'Theo mức độ ủy quyền: tư vấn gợi ý (người tư vấn chỉ khuyến nghị, khách hàng tự quyết định) và tư vấn ủy quyền (khách hàng ủy quyền cho người tư vấn quyết định trong phạm vi nhất định; với CTCK, việc này chỉ được thực hiện qua dịch vụ ủy thác quản lý tài khoản theo Điều 19 TT 121/2020). Trực tiếp/gián tiếp là phân loại theo hình thức; tổ chức phát hành/nhà đầu tư là phân loại theo đối tượng.',
    'Giáo trình Môi giới và tư vấn đầu tư chứng khoán – Chuyên đề 1: phân loại tư vấn đầu tư chứng khoán')

add(T1, 2,
    'Theo Thông tư 121/2020/TT-BTC, yêu cầu nào sau đây đúng đối với nội dung tư vấn và khuyến nghị đầu tư chứng khoán của công ty chứng khoán?',
    ['Có cơ sở hợp lý, dựa trên thông tin đáng tin cậy, ghi rõ nguồn số liệu và người chịu trách nhiệm',
     'Phải được Ủy ban Chứng khoán Nhà nước thẩm định trước khi công ty gửi tới khách hàng',
     'Phải nêu mức lợi nhuận tối thiểu khách hàng chắc chắn đạt được nếu làm theo khuyến nghị',
     'Chỉ cần ghi tên công ty chứng khoán, không cần nêu tên người chịu trách nhiệm nội dung'], 0,
    'Khoản 3 Điều 24 TT 121/2020: nội dung tư vấn phải có cơ sở hợp lý, phù hợp, dựa trên thông tin đáng tin cậy, phân tích lôgic; báo cáo phân tích, khuyến nghị phải ghi rõ nguồn trích dẫn số liệu và tên người chịu trách nhiệm. Không có yêu cầu UBCKNN thẩm định khuyến nghị; đưa ra bảo đảm về mức lợi nhuận bị cấm (khoản 1 Điều 91 Luật Chứng khoán).',
    'Khoản 3 Điều 24 Thông tư 121/2020/TT-BTC (VBHN 09/VBHN-BTC/2026); khoản 1 Điều 91 Luật Chứng khoán',
    'Các báo cáo phân tích chứng khoán và thị trường, khuyến nghị đầu tư phải ghi rõ nguồn trích dẫn số liệu và tên người chịu trách nhiệm về nội dung báo cáo, khuyến nghị đầu tư chứng khoán.',
    TT121)

add(T1, 2,
    'Điểm khác biệt cơ bản giữa dịch vụ tư vấn đầu tư chứng khoán và dịch vụ ủy thác quản lý tài khoản của nhà đầu tư cá nhân tại công ty chứng khoán là:',
    ['Khi tư vấn, công ty được quyết định giao dịch thay khách hàng nếu khách đồng ý bằng lời',
     'Khi nhận ủy thác, công ty không cần thu thập thông tin về khả năng tài chính của khách',
     'Khi tư vấn, khách hàng tự quyết định; khi ủy thác, công ty giao dịch trong phạm vi ủy thác',
     'Khi nhận ủy thác, lợi nhuận phát sinh trên tài khoản được chia đôi giữa công ty và khách'], 2,
    'Khoản 3 Điều 4 TT 121/2020: CTCK, nhân viên CTCK không được đầu tư thay cho khách hàng, trừ trường hợp ủy thác quản lý tài khoản theo Điều 19. Theo Điều 19, công ty chỉ giao dịch trong phạm vi ủy thác ghi cụ thể (loại chứng khoán, khối lượng, giá trị tối đa…), phải tổng hợp thông tin về khả năng tài chính, mục tiêu, mức rủi ro chấp nhận được của khách hàng trước khi ký hợp đồng (khoản 3), và lợi nhuận phát sinh thuộc về khách hàng ủy thác; công ty thu phí quản lý, phí thưởng theo hợp đồng.',
    'Khoản 3 Điều 4; điểm c khoản 1, khoản 2, khoản 3, khoản 5 Điều 19 Thông tư 121/2020/TT-BTC (VBHN 09/VBHN-BTC/2026)',
    'Công ty chứng khoán, nhân viên công ty chứng khoán không được thực hiện đầu tư thay cho khách hàng trừ trường hợp ủy thác quản lý tài khoản giao dịch chứng khoán của nhà đầu tư cá nhân',
    TT121)

add(T1, 2,
    'Trình tự hợp lý của quy trình tư vấn đầu tư cho một khách hàng cá nhân là:',
    ['Đề xuất danh mục → Tìm hiểu khách hàng → Thực hiện giao dịch → Theo dõi, điều chỉnh',
     'Tìm hiểu khách hàng → Xác định mục tiêu, ràng buộc → Đề xuất danh mục → Theo dõi, điều chỉnh',
     'Xác định mục tiêu, ràng buộc → Thực hiện giao dịch → Tìm hiểu khách hàng → Đề xuất danh mục',
     'Tìm hiểu khách hàng → Thực hiện giao dịch → Đề xuất danh mục → Xác định mục tiêu, ràng buộc'], 1,
    'Tư vấn bắt đầu bằng thu thập thông tin về khách hàng (tình hình tài chính, kinh nghiệm, khẩu vị rủi ro), tiếp đến xác định mục tiêu và các ràng buộc (thời gian, thanh khoản, thuế, pháp lý), sau đó mới đề xuất phân bổ tài sản/danh mục để khách hàng quyết định, cuối cùng là theo dõi, đánh giá và điều chỉnh định kỳ.',
    'Giáo trình Môi giới và tư vấn đầu tư chứng khoán – Chuyên đề 1: quy trình tư vấn đầu tư')

# ---------------- T2: Kiến thức và kỹ năng (8) ----------------
add(T2, 1,
    'Nhân viên môi giới hỏi lại khách hàng: “Như vậy anh muốn đầu tư trong khoảng 3 năm, đúng không ạ?”. Đây là loại câu hỏi:',
    ['Câu hỏi đóng, dùng để xác nhận thông tin',
     'Câu hỏi mở, dùng để khai thác nhu cầu',
     'Câu hỏi giả định, dùng để thăm dò phản ứng',
     'Câu hỏi dẫn dắt, dùng để thúc đẩy quyết định'], 0,
    'Câu hỏi đóng có câu trả lời ngắn (có/không, một con số), thích hợp để xác nhận hoặc làm rõ thông tin khách hàng đã cung cấp. Câu hỏi mở (“Anh kỳ vọng gì từ khoản đầu tư này?”) dùng để khai thác nhu cầu, quan điểm của khách hàng.',
    'Giáo trình Môi giới và tư vấn đầu tư chứng khoán – Chuyên đề 2: kỹ năng đặt câu hỏi')

add(T2, 2,
    'Theo Luật Chứng khoán, công ty chứng khoán phải bảo đảm khuyến nghị, tư vấn đầu tư phù hợp với tình hình tài chính, mục tiêu đầu tư và khả năng chấp nhận rủi ro của từng khách hàng, trừ trường hợp nào sau đây?',
    ['Khách hàng là nhà đầu tư chứng khoán chuyên nghiệp theo luật',
     'Khách hàng chỉ đặt lệnh qua hệ thống giao dịch trực tuyến',
     'Khoản đầu tư của khách hàng có giá trị dưới 100 triệu đồng',
     'Khách hàng không cung cấp hoặc cung cấp thông tin thiếu chính xác'], 3,
    'Khoản 6 Điều 89 Luật Chứng khoán: CTCK phải thu thập, tìm hiểu thông tin về tình hình tài chính, mục tiêu đầu tư, khả năng chấp nhận rủi ro và bảo đảm khuyến nghị phù hợp với từng khách hàng, trừ trường hợp khách hàng không cung cấp thông tin hoặc cung cấp không đầy đủ, chính xác. Luật không loại trừ nghĩa vụ này với nhà đầu tư chuyên nghiệp, giao dịch trực tuyến hay khoản đầu tư nhỏ.',
    'Khoản 6 Điều 89 Luật Chứng khoán 2019 (VBHN 24/VBHN-VPQH/2025)',
    'bảo đảm các khuyến nghị, tư vấn đầu tư của công ty cho khách hàng phải phù hợp với tình hình tài chính, mục tiêu đầu tư và khả năng chấp nhận rủi ro của từng khách hàng, trừ trường hợp khách hàng không cung cấp thông tin hoặc cung cấp thông tin nhưng không đầy đủ, chính xác.',
    LUAT)

add(T2, 1,
    'Theo Thông tư 121/2020/TT-BTC (sửa đổi bởi Thông tư 08/2026/TT-BTC), khi mở tài khoản giao dịch chứng khoán, chủ thể chịu trách nhiệm cung cấp đầy đủ, chính xác các thông tin nhận biết khách hàng là:',
    ['Nhân viên môi giới tiếp nhận hồ sơ mở tài khoản',
     'Tổng công ty Lưu ký và Bù trừ chứng khoán Việt Nam',
     'Khách hàng mở tài khoản giao dịch chứng khoán',
     'Ngân hàng thương mại nơi khách hàng mở tài khoản'], 2,
    'Khoản 1 Điều 15 TT 121/2020 (sửa đổi bởi Điều 11 TT 08/2026): khách hàng chịu trách nhiệm cung cấp đầy đủ, chính xác thông tin nhận biết khách hàng khi mở tài khoản. Về phía CTCK: giải thích hợp đồng, tìm hiểu khả năng tài chính, khả năng chịu đựng rủi ro, kỳ vọng lợi nhuận của khách hàng (khoản 2 Điều 15) và tuân thủ quy định phòng, chống rửa tiền (khoản 2 Điều 13).',
    'Khoản 1 Điều 15 Thông tư 121/2020/TT-BTC (sửa đổi bởi Điều 11 Thông tư 08/2026/TT-BTC)',
    'Khách hàng chịu trách nhiệm cung cấp đầy đủ, chính xác các thông tin nhận biết khách hàng khi mở tài khoản giao dịch chứng khoán.',
    TT121)

add(T2, 2,
    'Theo cách tiếp cận vòng đời đầu tư, khách hàng ở giai đoạn tích lũy (khoảng 25–35 tuổi, thu nhập tăng dần, thời gian đầu tư dài, chưa có nghĩa vụ tài chính lớn) thường phù hợp với định hướng nào?',
    ['Ưu tiên tiền gửi và trái phiếu ngắn hạn để bảo toàn tuyệt đối vốn gốc',
     'Tỷ trọng cổ phiếu tăng trưởng cao hơn, chấp nhận biến động ngắn hạn',
     'Tập trung cổ phiếu cổ tức cao để lấy dòng tiền chi tiêu hằng tháng',
     'Giữ phần lớn tài sản bằng tiền mặt để chuẩn bị cho giai đoạn nghỉ hưu'], 1,
    'Giai đoạn tích lũy có thời gian đầu tư dài và thu nhập tăng nên khả năng chấp nhận rủi ro tương đối cao; định hướng thường là tăng trưởng vốn với tỷ trọng cổ phiếu lớn hơn. Bảo toàn vốn và ưu tiên thu nhập hiện tại phù hợp hơn với giai đoạn gần hoặc sau nghỉ hưu. Khuyến nghị cụ thể vẫn phải dựa trên thông tin thực tế của từng khách hàng.',
    'Giáo trình Môi giới và tư vấn đầu tư chứng khoán – Chuyên đề 2: vòng đời đầu tư và nhu cầu khách hàng')

add(T2, 3,
    'Anh T, 40 tuổi, thu nhập cao và ổn định, tài sản ròng lớn, dự kiến nắm giữ khoản đầu tư 1 tỷ đồng trên 10 năm. Tuy nhiên, anh cho biết sẽ mất ngủ và muốn bán hết nếu danh mục giảm 5%. Nhận định và cách xử lý phù hợp của chuyên viên tư vấn là:',
    ['Khả năng chịu rủi ro cao nhưng mức sẵn sàng thấp; chọn mức rủi ro thận trọng hơn và giải thích thêm',
     'Khả năng và mức sẵn sàng chịu rủi ro đều cao; tư vấn danh mục cổ phiếu tăng trưởng tỷ trọng lớn',
     'Khả năng chịu rủi ro thấp nhưng mức sẵn sàng cao; khuyến nghị dùng giao dịch ký quỹ để tăng lãi',
     'Chỉ căn cứ khả năng tài chính khách quan; tâm lý lo lắng của khách hàng không ảnh hưởng tư vấn'], 0,
    'Khả năng chấp nhận rủi ro (ability) dựa trên yếu tố khách quan – thu nhập, tài sản, thời gian đầu tư – của anh T là cao. Mức độ sẵn sàng chấp nhận rủi ro (willingness) thể hiện tâm lý – của anh T thấp (không chịu được mức giảm 5%). Khi hai yếu tố mâu thuẫn, thông thường chọn mức rủi ro theo yếu tố thấp hơn, đồng thời trao đổi, giúp khách hàng hiểu về biến động thị trường.',
    'Giáo trình Môi giới và tư vấn đầu tư chứng khoán – Chuyên đề 2: đánh giá khẩu vị rủi ro khách hàng')

add(T2, 3,
    'Chị M, 34 tuổi, có 800 triệu đồng dành để thanh toán tiền mua nhà sau đúng 12 tháng và nhấn mạnh không thể để hụt số tiền này. Khuyến nghị nào sau đây phù hợp nhất với mục tiêu và ràng buộc của chị M?',
    ['Cổ phiếu vốn hóa nhỏ có tiềm năng tăng trưởng mạnh trong năm tới',
     'Giao dịch ký quỹ cổ phiếu vốn hóa lớn để tăng quy mô vốn đầu tư',
     'Trái phiếu doanh nghiệp kỳ hạn 10 năm có lãi suất coupon cao',
     'Tiền gửi có kỳ hạn hoặc quỹ thị trường tiền tệ khớp kỳ hạn 12 tháng'], 3,
    'Ràng buộc quan trọng nhất là thời gian ngắn (12 tháng), nhu cầu thanh khoản đúng hạn và không chấp nhận hụt vốn → cần tài sản rủi ro thấp, kỳ hạn khớp với thời điểm cần tiền. Cổ phiếu vốn hóa nhỏ và giao dịch ký quỹ có rủi ro giá cao; trái phiếu kỳ hạn 10 năm phải bán trước hạn nên chịu rủi ro lãi suất, rủi ro thanh khoản và rủi ro tín dụng.',
    'Giáo trình Môi giới và tư vấn đầu tư chứng khoán – Chuyên đề 2: xác định mục tiêu và ràng buộc đầu tư')

add(T2, 2,
    'Khách hàng nói với nhân viên môi giới: “Tôi rất lo thị trường lại giảm sâu như đợt trước, tài khoản của tôi khó chịu nổi”. Phản hồi nào thể hiện kỹ năng lắng nghe chủ động?',
    ['“Anh cứ yên tâm, đợt này thị trường chắc chắn sẽ không giảm nữa đâu ạ.”',
     '“Đợt trước anh lỗ là do anh mua sai thời điểm thôi, lần này sẽ khác ạ.”',
     '“Anh đang lo một đợt giảm mạnh sẽ ảnh hưởng lớn tới danh mục, phải không ạ?”',
     '“Chuyện đó khó xảy ra lắm, mình chuyển sang bàn về mã cổ phiếu mới nhé.”'], 2,
    'Lắng nghe chủ động gồm tập trung, ghi nhận cảm xúc và diễn đạt lại (paraphrase) để xác nhận đã hiểu đúng mối quan tâm của khách hàng, làm cơ sở tìm hiểu tiếp mức chịu đựng rủi ro. Trấn an bằng khẳng định chắc chắn về giá là sai chuẩn mực; phán xét hoặc lảng tránh làm mất lòng tin của khách hàng.',
    'Giáo trình Môi giới và tư vấn đầu tư chứng khoán – Chuyên đề 2: kỹ năng lắng nghe')

add(T2, 3,
    'Bà P, 45 tuổi, có danh mục 1,5 tỷ đồng gồm 1,1 tỷ đồng cổ phiếu và 0,4 tỷ đồng trái phiếu. Công ty áp dụng quy tắc kinh nghiệm: tỷ trọng cổ phiếu mục tiêu = (100 − tuổi)%. Để tái cân bằng về tỷ trọng mục tiêu (bỏ qua chi phí giao dịch), nhân viên tư vấn nên đề xuất:',
    ['Bán 425 triệu đồng cổ phiếu, mua thêm trái phiếu tương ứng',
     'Bán 275 triệu đồng cổ phiếu, mua thêm trái phiếu tương ứng',
     'Bán 495 triệu đồng cổ phiếu, mua thêm trái phiếu tương ứng',
     'Mua thêm 275 triệu đồng cổ phiếu, bán trái phiếu tương ứng'], 1,
    'Tỷ trọng cổ phiếu mục tiêu = 100 − 45 = 55% → 55% × 1.500 = 825 triệu đồng. Hiện có 1.100 triệu đồng cổ phiếu (≈73,3%) → bán 1.100 − 825 = 275 triệu đồng, chuyển sang trái phiếu (trái phiếu tăng lên 675 triệu đồng = 45%). 425 triệu đồng là lỗi lấy tuổi làm tỷ trọng cổ phiếu (45% × 1.500 = 675); 495 triệu đồng là lỗi tính 45% × 1.100.',
    'Giáo trình Môi giới và tư vấn đầu tư chứng khoán – Chuyên đề 2: phân bổ tài sản theo đặc điểm khách hàng')

# ---------------- T3: Mạng lưới & chăm sóc khách hàng (8) ----------------
add(T3, 1,
    'Nhân viên môi giới lập danh sách số điện thoại doanh nghiệp từ niên giám và chủ động gọi giới thiệu dịch vụ dù chưa từng quen biết người nghe. Kỹ thuật tìm kiếm khách hàng này được gọi là:',
    ['Khai thác trung tâm ảnh hưởng',
     'Khai thác khách hàng giới thiệu',
     'Tổ chức hội thảo đầu tư',
     'Gọi điện lạnh (cold calling)'], 3,
    'Gọi điện lạnh là liên hệ với người chưa có quan hệ và chưa được ai giới thiệu trước; chi phí thấp, tiếp cận được nhiều người nhưng tỷ lệ thành công thấp, đòi hỏi kịch bản tốt và tôn trọng quyền riêng tư của người nghe.',
    'Giáo trình Môi giới và tư vấn đầu tư chứng khoán – Chuyên đề 3: các phương pháp tìm kiếm khách hàng')

add(T3, 1,
    'Việc nhân viên môi giới chủ động xây dựng quan hệ với luật sư, kế toán, lãnh đạo hiệp hội doanh nghiệp – những người có uy tín và có thể giới thiệu khách hàng tiềm năng – được gọi là khai thác:',
    ['Trung tâm ảnh hưởng',
     'Danh sách khách hàng cũ',
     'Kênh quảng cáo trực tuyến',
     'Thư chào hàng trực tiếp'], 0,
    'Trung tâm ảnh hưởng (centers of influence) là những cá nhân có uy tín, mạng lưới quan hệ rộng trong cộng đồng; quan hệ tốt với họ giúp nhân viên môi giới được giới thiệu tới nhiều khách hàng tiềm năng có chất lượng.',
    'Giáo trình Môi giới và tư vấn đầu tư chứng khoán – Chuyên đề 3: các phương pháp tìm kiếm khách hàng')

add(T3, 2,
    'Mục đích chính của việc phân nhóm (phân đoạn) khách hàng trong hoạt động môi giới chứng khoán là:',
    ['Xác định nhóm khách hàng được ưu tiên nhập lệnh trước khi khớp',
     'Áp mức phí riêng cho từng nhóm mà không cần công bố công khai',
     'Thiết kế sản phẩm, kênh và tần suất chăm sóc phù hợp từng nhóm',
     'Loại bỏ nhóm khách hàng giao dịch ít để giảm chi phí phục vụ'], 2,
    'Phân đoạn khách hàng (theo giá trị tài sản, mức độ giao dịch, nhu cầu, khẩu vị rủi ro…) giúp phân bổ nguồn lực và thiết kế dịch vụ phù hợp. Phân nhóm không được làm sai lệch nguyên tắc thực hiện lệnh nhanh chóng, chính xác theo thời gian nhận lệnh (khoản 4, 5 Điều 16 TT 121/2020), và CTCK vẫn phải công bố mức phí giao dịch (khoản 5 Điều 14).',
    'Giáo trình Môi giới và tư vấn đầu tư chứng khoán – Chuyên đề 3: phân loại, quản lý khách hàng; khoản 5 Điều 14, khoản 4, 5 Điều 16 Thông tư 121/2020/TT-BTC')

add(T3, 2,
    'Một khách hàng gọi điện phàn nàn gay gắt về chất lượng dịch vụ. Phản ứng đầu tiên phù hợp nhất của nhân viên môi giới là:',
    ['Giải thích ngay lỗi không thuộc về mình để khách hàng bình tĩnh lại',
     'Lắng nghe hết ý kiến, thể hiện sự thấu hiểu, không ngắt lời, tranh cãi',
     'Đề nghị khách hàng gửi đơn lên Ủy ban Chứng khoán Nhà nước giải quyết',
     'Hứa bồi thường ngay để khách hàng không phản ánh lên cấp quản lý'], 1,
    'Quy trình xử lý phàn nàn, khiếu nại: lắng nghe – ghi nhận, thấu hiểu – thu thập thông tin, xác minh – đề xuất giải pháp theo quy định và hợp đồng – theo dõi kết quả. Bước đầu tiên là lắng nghe, tránh tranh cãi hay đổ lỗi; không hứa bồi thường vượt thẩm quyền; khiếu nại được chuyển cho bộ phận chuyên trách của công ty (khoản 6 Điều 14 TT 121/2020).',
    'Giáo trình Môi giới và tư vấn đầu tư chứng khoán – Chuyên đề 3: xử lý phàn nàn, khiếu nại của khách hàng')

add(T3, 2,
    'Theo Thông tư 121/2020/TT-BTC, công ty chứng khoán phải công bố mức phí giao dịch chứng khoán như thế nào?',
    ['Trước khi khách hàng giao dịch và trên trang thông tin điện tử của công ty',
     'Chỉ khi khách hàng có yêu cầu bằng văn bản gửi tới công ty chứng khoán',
     'Sau khi lệnh khớp, trên phiếu xác nhận kết quả giao dịch gửi khách hàng',
     'Định kỳ hằng quý trong báo cáo gửi Ủy ban Chứng khoán Nhà nước'], 0,
    'Khoản 5 Điều 14 TT 121/2020: CTCK phải công bố mức phí giao dịch chứng khoán trước khi khách hàng thực hiện giao dịch và trên trang thông tin điện tử của công ty – bảo đảm khách hàng biết chi phí trước khi quyết định.',
    'Khoản 5 Điều 14 Thông tư 121/2020/TT-BTC (VBHN 09/VBHN-BTC/2026)',
    'Công ty chứng khoán phải công bố về mức phí giao dịch chứng khoán trước khi khách hàng thực hiện giao dịch, phải công bố về mức phí giao dịch chứng khoán trên trang thông tin điện tử của công ty.',
    TT121)

add(T3, 2,
    'Theo Thông tư 121/2020/TT-BTC (sửa đổi bởi Thông tư 08/2026/TT-BTC), công ty chứng khoán phải thông báo kết quả thực hiện lệnh giao dịch cho khách hàng:',
    ['Vào cuối ngày giao dịch, bằng văn bản gửi tới địa chỉ của khách hàng',
     'Trong thời hạn 03 ngày làm việc kể từ ngày lệnh giao dịch được khớp',
     'Khi khách hàng đến quầy giao dịch yêu cầu cung cấp sao kê tài khoản',
     'Ngay sau khi lệnh được khớp, theo phương thức thỏa thuận trong hợp đồng'], 3,
    'Khoản 7 Điều 16 TT 121/2020 (sửa đổi bởi khoản 3 Điều 13 TT 08/2026): CTCK phải thông báo kết quả thực hiện lệnh cho khách hàng (hoặc tổ chức kinh doanh chứng khoán nước ngoài đại diện) ngay sau khi lệnh được khớp, theo phương thức do hai bên thỏa thuận trong hợp đồng.',
    'Khoản 7 Điều 16 Thông tư 121/2020/TT-BTC (sửa đổi bởi khoản 3 Điều 13 Thông tư 08/2026/TT-BTC)',
    'sau khi lệnh được khớp theo phương thức do khách hàng hoặc tổ chức kinh doanh chứng khoán nước ngoài đại diện và công ty chứng khoán thỏa thuận trong hợp đồng.',
    TT121)

add(T3, 3,
    'Khách hàng A khiếu nại, đòi công ty chứng khoán bồi thường khoản lỗ 20% khi mua cổ phiếu X theo khuyến nghị của nhân viên môi giới B. Hồ sơ cho thấy khuyến nghị có cơ sở phân tích, đã nêu rõ rủi ro và A tự đặt lệnh qua hệ thống trực tuyến. Cách xử lý phù hợp là:',
    ['Nhân viên B tự bù một phần khoản lỗ cho A để giữ quan hệ khách hàng',
     'B cam kết với A sẽ giúp gỡ lại toàn bộ khoản lỗ trong các giao dịch tới',
     'Bộ phận chuyên trách tiếp nhận, rà soát hồ sơ tư vấn, giải thích căn cứ cho A',
     'Từ chối tiếp nhận khiếu nại vì A đã tự đặt lệnh qua hệ thống trực tuyến'], 2,
    'CTCK phải có bộ phận chuyên trách giải quyết thắc mắc, khiếu nại (khoản 6 Điều 14 TT 121/2020), nên phải tiếp nhận, xác minh và phản hồi bằng căn cứ. Khuyến nghị có cơ sở, đã cảnh báo rủi ro và khách hàng tự quyết định thì khoản lỗ do biến động giá là rủi ro của khách hàng. Bù lỗ hay cam kết gỡ lỗ là chia sẻ thua lỗ/bảo đảm lợi nhuận bị cấm (điểm b khoản 4 Điều 13 TT 121/2020; khoản 1 Điều 91 Luật Chứng khoán).',
    'Khoản 6 Điều 14, điểm b khoản 4 Điều 13 Thông tư 121/2020/TT-BTC; khoản 1 Điều 91 Luật Chứng khoán',
    'Công ty chứng khoán phải thiết lập một bộ phận chuyên trách chịu trách nhiệm thông tin liên lạc với khách hàng và giải quyết các thắc mắc, khiếu nại của khách hàng.',
    TT121)

add(T3, 3,
    'Đầu năm, nhân viên môi giới có 120 khách hàng hoạt động. Theo kinh nghiệm, mỗi năm 15% số khách hàng hiện có ngừng giao dịch. Giả định khách hàng mới phát triển trong năm đều duy trì hoạt động đến cuối năm, số khách hàng mới tối thiểu cần phát triển để có 150 khách hàng hoạt động vào cuối năm là:',
    ['18 khách hàng', '48 khách hàng', '30 khách hàng', '57 khách hàng'], 1,
    'Số khách hàng cũ còn lại = 120 × (1 − 15%) = 102. Số khách hàng mới cần có = 150 − 102 = 48. 30 là lỗi bỏ qua tỷ lệ rời bỏ; 18 chỉ là số khách hàng rời bỏ; 57 là lỗi áp tỷ lệ rời bỏ cho cả khách hàng mới (150/0,85 − 120 ≈ 56,5).',
    'Giáo trình Môi giới và tư vấn đầu tư chứng khoán – Chuyên đề 3: lập kế hoạch phát triển mạng lưới khách hàng')

# ---------------- T4: Xung đột lợi ích (8) ----------------
add(T4, 1,
    'Hành vi nhân viên môi giới khuyến khích hoặc thực hiện mua, bán quá thường xuyên trên tài khoản khách hàng, chủ yếu nhằm tăng phí giao dịch thay vì vì lợi ích của khách hàng, được gọi là:',
    ['Giao dịch quá mức (churning)',
     'Giao dịch đón đầu (front running)',
     'Giao dịch nội gián (insider trading)',
     'Tạo lập thị trường (market making)'], 0,
    'Churning là giao dịch với tần suất, khối lượng không phù hợp mục tiêu và khẩu vị rủi ro của khách hàng, chủ yếu tạo phí cho người môi giới – xung đột lợi ích điển hình giữa thu nhập của môi giới và lợi ích của khách hàng. Dấu hiệu: vòng quay tài khoản cao, chi phí giao dịch lớn so với giá trị tài khoản.',
    'Giáo trình Môi giới và tư vấn đầu tư chứng khoán – Chuyên đề 6: các dạng xung đột lợi ích')

add(T4, 2,
    'Công ty chứng khoán X dùng tài khoản tự doanh làm đối tác bán cổ phiếu niêm yết cho chính khách hàng môi giới của mình bằng phương thức giao dịch thỏa thuận. Theo Thông tư 121/2020/TT-BTC, X phải:',
    ['Xin chấp thuận trước của Ủy ban Chứng khoán Nhà nước cho từng giao dịch',
     'Chuyển giao dịch sang phương thức khớp lệnh để bảo đảm tính khách quan',
     'Công bố cho khách hàng biết công ty là đối tác trong giao dịch thỏa thuận',
     'Chỉ giao dịch nếu khách hàng là nhà đầu tư chứng khoán chuyên nghiệp'], 2,
    'Khoản 5 Điều 22 TT 121/2020: CTCK phải công bố cho khách hàng biết khi mình là đối tác trong giao dịch thỏa thuận với khách hàng – minh bạch xung đột lợi ích khi công ty vừa là người môi giới vừa là bên đối ứng. Quy định không yêu cầu UBCKNN chấp thuận từng giao dịch, không giới hạn đối tượng khách hàng.',
    'Khoản 5 Điều 22 Thông tư 121/2020/TT-BTC (VBHN 09/VBHN-BTC/2026)',
    'Công ty chứng khoán phải công bố cho khách hàng biết khi mình là đối tác trong giao dịch thỏa thuận với khách hàng.',
    TT121)

add(T4, 2,
    'Chuyên viên tư vấn chuẩn bị gửi khuyến nghị mua cổ phiếu Y cho khách hàng, trong khi bản thân anh đang nắm giữ một lượng lớn cổ phiếu Y. Cách xử lý phù hợp với nguyên tắc quản lý xung đột lợi ích là:',
    ['Vẫn khuyến nghị nhưng giữ kín việc sở hữu để khách hàng không nghi ngờ',
     'Bán ngay cổ phiếu Y trước khi gửi khuyến nghị để tránh xung đột lợi ích',
     'Chuyển cổ phiếu Y sang tài khoản người thân rồi mới đưa ra khuyến nghị',
     'Báo bộ phận tuân thủ, công khai lợi ích liên quan, theo quy định giao dịch cá nhân'], 3,
    'Quản lý xung đột lợi ích: nhận diện – báo cáo – công khai – kiểm soát. Bộ phận kiểm soát nội bộ của CTCK giám sát các hoạt động tiềm ẩn xung đột lợi ích, đặc biệt là giao dịch cá nhân của nhân viên (điểm b khoản 2 Điều 12 TT 121/2020). Giấu lợi ích, giao dịch ngược chiều trước khuyến nghị hay chuyển sang người thân đều không loại bỏ xung đột mà còn có thể gây thiệt hại cho khách hàng.',
    'Điểm b khoản 2 Điều 12 Thông tư 121/2020/TT-BTC; khoản 1 Điều 89 Luật Chứng khoán',
    'Giám sát thực thi các quy định nội bộ, các hoạt động tiềm ẩn xung đột lợi ích trong nội bộ công ty, đặc biệt đối với các hoạt động kinh doanh của bản thân công ty và các giao dịch cá nhân của nhân viên công ty',
    TT121)

add(T4, 2,
    'Công ty chứng khoán P đang nắm giữ 15% vốn điều lệ của Công ty cổ phần Q (đã niêm yết). Theo Thông tư 121/2020/TT-BTC, P KHÔNG được thực hiện hoạt động nào sau đây?',
    ['Nhận lệnh mua, bán cổ phiếu Q của khách hàng môi giới',
     'Ký hợp đồng cung cấp dịch vụ tư vấn đầu tư chứng khoán cho Q',
     'Lưu ký cổ phiếu Q cho khách hàng có tài khoản tại P',
     'Thanh toán giao dịch cổ phiếu Q cho khách hàng của P'], 1,
    'Khoản 7 Điều 24 TT 121/2020: CTCK không được cung cấp dịch vụ tư vấn đầu tư chứng khoán cho công ty mà mình nắm giữ từ 10% trở lên vốn điều lệ (tương tự, khoản 2 Điều 25 cấm tư vấn chào bán, niêm yết, cổ phần hóa, xác định giá trị doanh nghiệp cho công ty đó). Các dịch vụ môi giới, lưu ký, thanh toán cho khách hàng giao dịch cổ phiếu Q không bị cấm bởi quy định này.',
    'Khoản 7 Điều 24, khoản 2 Điều 25 Thông tư 121/2020/TT-BTC (VBHN 09/VBHN-BTC/2026)',
    'Công ty chứng khoán không được cung cấp dịch vụ tư vấn đầu tư chứng khoán cho công ty mà mình nắm giữ từ 10% trở lên vốn điều lệ.',
    TT121)

add(T4, 3,
    'Để lôi kéo một khách hàng lớn mở tài khoản, chị D (nhân viên môi giới của công ty chứng khoán K) đề xuất thỏa thuận bằng văn bản: khách hàng được bảo đảm lãi 1,5%/tháng trên vốn, nếu thua lỗ thì phía công ty chia sẻ 50% khoản lỗ. Nhận định nào sau đây đúng?',
    ['Bị cấm: công ty môi giới không được đưa ra lãi suất cụ thể hay chia sẻ lãi, lỗ để lôi kéo khách hàng',
     'Hợp lệ: thỏa thuận được lập thành văn bản có chữ ký của khách hàng nên có giá trị thực hiện',
     'Hợp lệ một phần: được chia sẻ lỗ với khách hàng nhưng không được cam kết mức lãi suất cụ thể',
     'Chỉ vi phạm khi khách hàng thực tế bị thua lỗ mà công ty không thực hiện phần chia sẻ đã hứa'], 0,
    'Điểm b khoản 4 Điều 13 TT 121/2020 cấm CTCK môi giới thỏa thuận hoặc đưa ra lãi suất cụ thể, chia sẻ lợi nhuận hoặc thua lỗ với khách hàng để lôi kéo giao dịch; điểm b khoản 6 Điều 4 cấm thỏa thuận chia sẻ lợi nhuận hoặc lỗ; khoản 1 Điều 91 Luật Chứng khoán cấm bảo đảm mức lợi nhuận hoặc bảo đảm khách hàng không bị thua lỗ. Hình thức văn bản không làm thỏa thuận hợp pháp; vi phạm phát sinh ngay khi đưa ra thỏa thuận, không phụ thuộc kết quả đầu tư.',
    'Điểm b khoản 4 Điều 13, điểm b khoản 6 Điều 4 Thông tư 121/2020/TT-BTC; khoản 1 Điều 91 Luật Chứng khoán',
    'Thỏa thuận hoặc đưa ra lãi suất cụ thể hoặc chia sẻ lợi nhuận hoặc thua lỗ với khách hàng để lôi kéo khách hàng tham gia giao dịch;',
    TT121)

add(T4, 3,
    'Tiền gửi giao dịch của khách hàng tại công ty chứng khoán M được quản lý trên tài khoản chuyên dụng của công ty tại ngân hàng. Khách hàng A gửi giấy ủy quyền đề nghị M chuyển 200 triệu đồng từ tài khoản giao dịch của A sang tài khoản giao dịch của bạn mình là B (cũng mở tại M) để B mua cổ phiếu. Nhân viên môi giới nên xử lý thế nào?',
    ['Thực hiện chuyển ngay vì đã có giấy ủy quyền hợp lệ của chủ tài khoản A',
     'Thực hiện nếu B ký cam kết hoàn trả số tiền cho A trong thời hạn 30 ngày',
     'Thực hiện, đồng thời báo cáo Ủy ban Chứng khoán Nhà nước trong 24 giờ',
     'Từ chối, vì công ty không được nhận ủy quyền chuyển tiền nội bộ giữa khách hàng'], 3,
    'Điểm b khoản 4 Điều 17 TT 121/2020: CTCK không được nhận ủy quyền của khách hàng thực hiện chuyển tiền nội bộ giữa các tài khoản của các khách hàng; tài khoản chuyên dụng chỉ phục vụ các giao dịch của chính khách hàng (nộp, rút, thanh toán…). A có thể rút tiền về tài khoản ngân hàng của mình rồi tự chuyển cho B qua ngân hàng. Quy định nhằm bảo đảm tách bạch tiền của từng khách hàng, tránh lạm dụng tiền của khách hàng.',
    'Điểm b khoản 4 Điều 17 Thông tư 121/2020/TT-BTC (VBHN 09/VBHN-BTC/2026)',
    'Công ty chứng khoán không được nhận ủy quyền của khách hàng thực hiện chuyển tiền nội bộ giữa các tài khoản của các khách hàng.',
    TT121)

add(T4, 3,
    'Anh G, nhân viên môi giới, tình cờ nghe đồng nghiệp bộ phận tư vấn tài chính doanh nghiệp trao đổi về thương vụ sáp nhập chưa công bố của công ty niêm yết Y. Một khách hàng thân thiết hỏi anh G tuần này nên mua cổ phiếu nào. Cách xử lý đúng là:',
    ['Khuyến nghị mua Y cho khách hàng nhưng bản thân anh G không giao dịch Y',
     'Khuyến nghị mua Y vì anh G không phải là người nội bộ của công ty Y',
     'Không sử dụng, không tiết lộ thông tin; báo bộ phận kiểm soát tuân thủ',
     'Chỉ gợi ý khách hàng “nên để ý cổ phiếu Y” mà không nêu lý do cụ thể'], 2,
    'Thông tin về thương vụ sáp nhập chưa công bố là thông tin nội bộ. Khoản 2 Điều 12 Luật Chứng khoán cấm không chỉ sử dụng mà cả tiết lộ, cung cấp hoặc tư vấn cho người khác mua, bán trên cơ sở thông tin nội bộ – áp dụng với bất kỳ ai nắm được thông tin, không chỉ người nội bộ của tổ chức phát hành. Gợi ý mập mờ vẫn là tư vấn trên cơ sở thông tin nội bộ. Việc thông tin rò rỉ qua “bức tường lửa” cần được báo bộ phận kiểm soát nội bộ để xử lý.',
    'Khoản 2 Điều 12 Luật Chứng khoán 2019 (VBHN 24/VBHN-VPQH/2025); điểm b khoản 2 Điều 12 Thông tư 121/2020/TT-BTC',
    'tiết lộ, cung cấp thông tin nội bộ hoặc tư vấn cho người khác mua, bán chứng khoán trên cơ sở thông tin nội bộ.',
    LUAT)

add(T4, 3,
    'Tài khoản của bà N (khẩu vị rủi ro thận trọng) có giá trị bình quân 2 tỷ đồng. Trong 12 tháng, theo khuyến nghị của nhân viên môi giới, tổng giá trị mua là 24 tỷ đồng, tổng giá trị bán là 23,6 tỷ đồng; phí môi giới 0,15% giá trị giao dịch mỗi chiều. Vòng quay tài khoản (tổng giá trị mua/giá trị bình quân tài khoản) và tổng phí môi giới trong năm lần lượt là:',
    ['11,8 lần và 71,4 triệu đồng',
     '12 lần và 71,4 triệu đồng',
     '12 lần và 36 triệu đồng',
     '23,8 lần và 71,4 triệu đồng'], 1,
    'Vòng quay = 24 / 2 = 12 lần/năm. Tổng phí = 0,15% × (24 + 23,6) tỷ = 0,15% × 47,6 tỷ = 71,4 triệu đồng (≈3,57% giá trị tài khoản). 36 triệu đồng là chỉ tính chiều mua; 11,8 lần dùng giá trị bán; 23,8 lần cộng cả mua và bán. Vòng quay rất cao và chi phí lớn trên tài khoản của khách hàng thận trọng là dấu hiệu điển hình của giao dịch quá mức (churning).',
    'Giáo trình Môi giới và tư vấn đầu tư chứng khoán – Chuyên đề 6: nhận diện giao dịch quá mức (churning)')

# ---------------- T5: Quản lý Nhà nước (10) ----------------
add(T5, 1,
    'Theo Nghị định 155/2020/NĐ-CP, người có chứng chỉ hành nghề môi giới chứng khoán được thực hiện nghiệp vụ nào?',
    ['Môi giới chứng khoán và tư vấn đầu tư chứng khoán',
     'Môi giới, tư vấn đầu tư và tự doanh chứng khoán',
     'Môi giới, tư vấn đầu tư và bảo lãnh phát hành chứng khoán',
     'Chỉ nghiệp vụ môi giới chứng khoán, không được tư vấn'], 0,
    'Điểm a khoản 2 Điều 216 NĐ 155/2020: người có CCHN môi giới chứng khoán được thực hiện nghiệp vụ môi giới chứng khoán, tư vấn đầu tư chứng khoán. Tự doanh và bảo lãnh phát hành đòi hỏi CCHN phân tích tài chính hoặc quản lý quỹ (điểm b, c khoản 2 Điều 216).',
    'Điểm a khoản 2 Điều 216 Nghị định 155/2020/NĐ-CP (khoản này không bị sửa đổi bởi Nghị định 245/2025/NĐ-CP)',
    'Người có chứng chỉ hành nghề môi giới chứng khoán được thực hiện nghiệp vụ môi giới chứng khoán, tư vấn đầu tư chứng khoán;',
    ND155)

add(T5, 1,
    'Theo Nghị định 155/2020/NĐ-CP, tại một thời điểm, người có chứng chỉ hành nghề chứng khoán được làm việc tại:',
    ['Tối đa 02 bộ phận nghiệp vụ kinh doanh chứng khoán',
     '01 bộ phận nghiệp vụ kinh doanh chứng khoán',
     'Tối đa 03 bộ phận nếu thuộc cùng một công ty',
     'Mọi bộ phận phù hợp với loại chứng chỉ được cấp'], 1,
    'Điểm e khoản 2 Điều 216 NĐ 155/2020: người có CCHN chứng khoán chỉ được làm việc tại 01 bộ phận nghiệp vụ kinh doanh chứng khoán trong một thời điểm – nhằm tách biệt nghiệp vụ, hạn chế xung đột lợi ích (ví dụ giữa môi giới và tự doanh).',
    'Điểm e khoản 2 Điều 216 Nghị định 155/2020/NĐ-CP (khoản này không bị sửa đổi bởi Nghị định 245/2025/NĐ-CP)',
    'Người có chứng chỉ hành nghề chứng khoán chỉ được làm việc tại 01 bộ phận nghiệp vụ kinh doanh chứng khoán trong một thời điểm.',
    ND155)

add(T5, 2,
    'Công ty chứng khoán X chưa được Ủy ban Chứng khoán Nhà nước chấp thuận lập phòng giao dịch tại quận Y nhưng đã thuê một văn phòng cố định ở đó để nhân viên ký hợp đồng mở tài khoản và nhận lệnh giao dịch của khách hàng. Theo Thông tư 121/2020/TT-BTC, hoạt động này:',
    ['Được phép nếu nhân viên làm việc tại văn phòng đều có CCHN môi giới',
     'Được phép nếu chỉ ký hợp đồng mở tài khoản, không thanh toán giao dịch',
     'Bị cấm, vì là địa điểm cố định ngoài địa điểm giao dịch đã được chấp thuận',
     'Được phép nếu văn phòng có kết nối trực tuyến tới hệ thống của công ty'], 2,
    'Điểm c khoản 4 Điều 13 TT 121/2020: CTCK không được trực tiếp hoặc gián tiếp thiết lập địa điểm cố định bên ngoài các địa điểm giao dịch đã được UBCKNN chấp thuận để ký hợp đồng mở tài khoản, nhận lệnh, thực hiện lệnh hoặc thanh toán giao dịch với khách hàng; ngoại lệ duy nhất là giao dịch chứng khoán trực tuyến, không phải việc lập văn phòng có kết nối mạng. Thành lập phòng giao dịch phải được UBCKNN chấp thuận (điểm d khoản 1 Điều 87 Luật Chứng khoán).',
    'Điểm c khoản 4 Điều 13 Thông tư 121/2020/TT-BTC; điểm d khoản 1 Điều 87 Luật Chứng khoán',
    'Trực tiếp hoặc gián tiếp thiết lập các địa điểm cố định bên ngoài các địa điểm giao dịch đã được Ủy ban Chứng khoán Nhà nước chấp thuận để ký hợp đồng mở tài khoản giao dịch với khách hàng, nhận lệnh, thực hiện lệnh giao dịch chứng khoán',
    TT121)

add(T5, 2,
    'Anh B là người hành nghề môi giới tại công ty chứng khoán A. Anh muốn ký thêm hợp đồng lao động bán thời gian để làm chuyên viên phân tích cho công ty quản lý quỹ C vào cuối tuần. Theo Luật Chứng khoán:',
    ['Được phép, vì làm ngoài giờ và không trùng nghiệp vụ với công ty A',
     'Được phép, nếu Tổng giám đốc công ty A chấp thuận bằng văn bản',
     'Được phép, vì công ty quản lý quỹ không phải công ty chứng khoán',
     'Không được, vì không được đồng thời làm việc cho từ 02 công ty trở lên'], 3,
    'Điểm a khoản 2 Điều 98 Luật Chứng khoán: người hành nghề chứng khoán không được đồng thời làm việc cho từ 02 tổ chức trở lên trong số CTCK, công ty quản lý quỹ, chi nhánh CTCK và công ty quản lý quỹ nước ngoài tại Việt Nam, công ty đầu tư chứng khoán. Việc làm ngoài giờ hay được công ty A đồng ý không làm thay đổi quy định này.',
    'Điểm a khoản 2 Điều 98 Luật Chứng khoán 2019 (VBHN 24/VBHN-VPQH/2025)',
    'Đồng thời làm việc cho từ 02 công ty chứng khoán, công ty quản lý quỹ đầu tư chứng khoán, chi nhánh công ty chứng khoán và công ty quản lý quỹ nước ngoài tại Việt Nam, công ty đầu tư chứng khoán trở lên;',
    LUAT)

add(T5, 2,
    'Một khách hàng lớn tuổi mang 300 triệu đồng tiền mặt đến phòng giao dịch của công ty chứng khoán, nhờ nhân viên môi giới nhận và nộp giúp vào tài khoản để mua cổ phiếu. Theo Thông tư 121/2020/TT-BTC, cách xử lý đúng là:',
    ['Nhận tiền, lập biên nhận có chữ ký hai bên rồi nộp vào tài khoản trong ngày',
     'Nhận tiền nếu số tiền không vượt hạn mức nhận tiền mặt do công ty quy định',
     'Hướng dẫn khách hàng nộp tiền qua ngân hàng thương mại theo quy định',
     'Nhận tiền và cho khách hàng đặt lệnh mua ngay, nộp tiền vào ngân hàng sau'], 2,
    'Khoản 2 Điều 17 TT 121/2020: CTCK không được trực tiếp nhận và chi trả tiền mặt để giao dịch chứng khoán của khách hàng mà phải thực hiện qua ngân hàng thương mại. Nhân viên chỉ được hướng dẫn khách hàng nộp tiền vào tài khoản qua ngân hàng; không có ngoại lệ theo hạn mức nội bộ.',
    'Khoản 2 Điều 17 Thông tư 121/2020/TT-BTC (VBHN 09/VBHN-BTC/2026)',
    'Công ty chứng khoán không được trực tiếp nhận và chi trả tiền mặt để giao dịch chứng khoán của khách hàng mà phải thực hiện qua ngân hàng thương mại.',
    TT121)

add(T5, 2,
    'Theo Thông tư 121/2020/TT-BTC, khi nhận lệnh giao dịch của khách hàng qua điện thoại, công ty chứng khoán phải tuân thủ yêu cầu nào sau đây?',
    ['Xác thực khách hàng, ghi nhận và lưu giữ bằng chứng đặt lệnh, xác nhận trước khi nhập lệnh',
     'Chỉ nhận lệnh khi khách hàng đã nộp phiếu lệnh giấy tại quầy trước ngày giao dịch',
     'Nhập lệnh ngay vào hệ thống, chỉ xác nhận lại với khách hàng sau khi lệnh đã khớp',
     'Chỉ nhận lệnh của nhà đầu tư chuyên nghiệp có giá trị từ 01 tỷ đồng trở lên mỗi lệnh'], 0,
    'Khoản 3 Điều 16 TT 121/2020: với lệnh trực tuyến, qua điện thoại, fax và đường truyền khác, CTCK phải tuân thủ Luật Giao dịch điện tử; xác thực khách hàng, ghi nhận đầy đủ thông tin tại thời điểm nhận lệnh, lưu giữ bằng chứng đặt lệnh để tra cứu; xác nhận với khách hàng trước khi nhập lệnh vào hệ thống; có biện pháp an toàn đường truyền và khắc phục khi không nhập được lệnh do lỗi của công ty.',
    'Khoản 3 Điều 16 Thông tư 121/2020/TT-BTC (VBHN 09/VBHN-BTC/2026)',
    'Xác thực khách hàng và đảm bảo có ghi nhận lại đầy đủ thông tin tại thời điểm nhận lệnh, lưu giữ bằng chứng chứng minh về việc đặt lệnh của khách hàng để có thể tra cứu được khi cần thiết;',
    TT121)

add(T5, 2,
    'Theo Thông tư 121/2020/TT-BTC, hợp đồng mở tài khoản giao dịch chứng khoán KHÔNG được chứa thỏa thuận nào sau đây?',
    ['Khách hàng tự chịu mọi thiệt hại, kể cả do lỗi hệ thống của công ty',
     'Phương thức công ty thông báo kết quả khớp lệnh cho khách hàng',
     'Mức phí giao dịch và phương thức thanh toán phí của khách hàng',
     'Trách nhiệm bảo mật thông tin giao dịch trực tuyến của các bên'], 0,
    'Khoản 3 Điều 15 TT 121/2020: hợp đồng mở tài khoản không được chứa thỏa thuận trốn tránh nghĩa vụ pháp lý của CTCK, hạn chế phạm vi bồi thường của CTCK không có lý do chính đáng hoặc chuyển rủi ro từ CTCK sang khách hàng, buộc khách hàng bồi thường không công bằng, gây bất lợi không công bằng cho khách hàng. Phương thức thông báo kết quả, phí giao dịch, trách nhiệm bảo mật giao dịch trực tuyến là nội dung hợp đồng bình thường (khoản 7 Điều 16, khoản 2 Điều 20).',
    'Điểm b khoản 3 Điều 15 Thông tư 121/2020/TT-BTC (VBHN 09/VBHN-BTC/2026)',
    'Thoả thuận hạn chế phạm vi bồi thường của công ty chứng khoán mà không có lý do chính đáng hoặc chuyển rủi ro từ công ty chứng khoán sang khách hàng;',
    TT121)

add(T5, 3,
    'Chị L đã có chứng chỉ hành nghề môi giới chứng khoán. Ngày 02/11/2026, chị ký hợp đồng lao động với công ty chứng khoán A và cùng ngày mở tài khoản giao dịch chứng khoán tại A. Theo Nghị định 155/2020/NĐ-CP (sửa đổi bởi Nghị định 245/2025/NĐ-CP), phát biểu nào đúng về nghĩa vụ báo cáo, thông báo với Ủy ban Chứng khoán Nhà nước?',
    ['Chị L báo cáo trong 02 ngày làm việc; công ty A thông báo trong 05 ngày làm việc',
     'Chị L báo cáo trong 05 ngày làm việc; công ty A thông báo trong 02 ngày làm việc',
     'Chỉ công ty A thông báo trong 05 ngày làm việc; chị L không phải báo cáo',
     'Chị L chỉ báo cáo việc mở tài khoản; việc ký hợp đồng do A báo cáo cuối năm'], 1,
    'Khoản 3 Điều 216 NĐ 155/2020: người được cấp CCHN báo cáo UBCKNN (Mẫu số 86) trong 05 ngày làm việc kể từ ngày ký kết, chấm dứt hợp đồng lao động với tổ chức sử dụng người hành nghề hoặc mở tài khoản giao dịch chứng khoán. Điểm c khoản 5 Điều 216: tổ chức sử dụng người hành nghề thông báo UBCKNN (Mẫu số 87) trong 02 ngày làm việc kể từ ngày ký kết, chấm dứt hợp đồng lao động hoặc phát hiện vi phạm. Báo cáo năm trước ngày 20/01 (điểm d khoản 5, sửa đổi bởi NĐ 245/2025) là nghĩa vụ riêng, không thay thế thông báo này.',
    'Khoản 3, điểm c và điểm d khoản 5 Điều 216 Nghị định 155/2020/NĐ-CP (điểm d khoản 5 sửa đổi bởi khoản 76 Điều 1 Nghị định 245/2025/NĐ-CP)',
    'Người được cấp chứng chỉ hành nghề chứng khoán phải báo cáo Ủy ban Chứng khoán Nhà nước theo Mẫu số 86 Phụ lục ban hành kèm theo Nghị định này trong thời hạn 05 ngày làm việc kể từ ngày ký kết hợp đồng lao động, chấm dứt hợp đồng lao động',
    ND155)

add(T5, 3,
    'Chị H, nhân viên môi giới của công ty chứng khoán A, được khách hàng M (bạn thân) đồng ý cho dùng tài khoản của M tại A để chị tự giao dịch bằng tiền của mình, nhằm tránh việc công ty giám sát giao dịch cá nhân của nhân viên. Nhận định nào sau đây đúng?',
    ['Được phép, vì khách hàng M là chủ tài khoản đã đồng ý bằng văn bản',
     'Được phép, vì tài khoản được mở tại chính công ty nơi chị H làm việc',
     'Được phép, nếu các giao dịch không gây ảnh hưởng tới giá chứng khoán',
     'Không được, vì dùng tên, tài khoản của khách hàng để giao dịch là bị cấm'], 3,
    'Điểm e khoản 4 Điều 13 TT 121/2020: trong nghiệp vụ môi giới, CTCK (qua nhân viên của mình) không được sử dụng tên hoặc tài khoản của khách hàng để đăng ký, giao dịch chứng khoán. Hành vi còn nhằm né tránh giám sát giao dịch cá nhân của bộ phận kiểm soát nội bộ (điểm b khoản 2 Điều 12) và có thể vi phạm khoản 6 Điều 12 Luật Chứng khoán nếu dẫn tới thao túng giá. Sự đồng ý của khách hàng không làm hành vi trở nên hợp pháp.',
    'Điểm e khoản 4 Điều 13, điểm b khoản 2 Điều 12 Thông tư 121/2020/TT-BTC; khoản 4 Điều 98 Luật Chứng khoán',
    'Sử dụng tên hoặc tài khoản của khách hàng để đăng ký, giao dịch chứng khoán;',
    TT121)

add(T5, 3,
    'Anh Q, nhân viên môi giới, liên tục đăng trong nhóm chat gồm các khách hàng của mình: “Mã Z chắc chắn tăng gấp đôi trong 2 tuần, ai chưa có thì vào ngay” mà không có báo cáo phân tích hay căn cứ nào. Nhận định nào sau đây đúng?',
    ['Không vi phạm, vì đây chỉ là nhận định cá nhân trong nhóm chat riêng',
     'Chỉ vi phạm nếu sau 2 tuần giá cổ phiếu Z thực tế không tăng như dự báo',
     'Không vi phạm, nếu anh Q không trực tiếp giao dịch cổ phiếu Z cho mình',
     'Vi phạm: không được nêu ý kiến tăng, giảm giá không căn cứ để lôi kéo giao dịch'], 3,
    'Điểm a khoản 4 Điều 13 TT 121/2020: CTCK môi giới (qua nhân viên) không được đưa ra ý kiến về việc tăng hay giảm giá chứng khoán mà không có căn cứ để lôi kéo khách hàng giao dịch; khoản 3 Điều 91 Luật Chứng khoán cấm làm khách hàng hiểu nhầm về giá chứng khoán. Vi phạm phát sinh từ hành vi, không phụ thuộc diễn biến giá sau đó hay việc anh Q có giao dịch hay không. Nếu kèm tung tin sai sự thật để tác động giá, hành vi còn có thể bị xem xét theo Điều 12 Luật Chứng khoán.',
    'Điểm a khoản 4 Điều 13 Thông tư 121/2020/TT-BTC; khoản 3 Điều 91 Luật Chứng khoán',
    'Đưa ra ý kiến về việc tăng hay giảm giá chứng khoán mà không có căn cứ để lôi kéo khách hàng tham gia giao dịch;',
    TT121)

assert len(Q) == 40
json.dump(Q, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(Q))
