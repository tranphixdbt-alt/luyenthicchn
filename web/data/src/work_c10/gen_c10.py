# Sinh câu C10 (soát 90 câu lớp Môi giới – Thầy Chung, file 1–3) -> ../cm_10.json
import json, re
from collections import Counter

OUT = '/home/user/cchn_moi/web/data/src/cm_10.json'
SRC_GT = 'Giáo trình SRTC (khung chương trình)'
LCK = 'VBHN_24_VBHN-VPQH_2025_Luat_Chung_khoan_hop_nhat_Cong_bao.txt'
TT121 = 'VBHN_09_VBHN-BTC_2026_TT121_68_08_hop_nhat.txt'
GT = 'Giáo trình Môi giới và tư vấn đầu tư chứng khoán (UBCKNN/SRTC) – '
KN = 'Kiến thức và kỹ năng cần thiết của người môi giới chứng khoán và tư vấn đầu tư chứng khoán'
ML = 'Xây dựng mạng lưới khách hàng và chăm sóc khách hàng'
XD = 'Xung đột lợi ích và giải quyết xung đột lợi ích trong hoạt động môi giới và tư vấn đầu tư chứng khoán'
Q = []


def add(subj, topic, level, q, correct, wrong, e, basis, quote='', src=SRC_GT):
    assert len(wrong) == 3 and len({correct, *wrong}) == 4, q[:40]
    Q.append(dict(subject=subj, topic=topic, level=level, q=q, correct=correct, wrong=wrong,
                  e=e, basis=basis, quote=quote, src=src))


# 1 – F1 câu 3, 4
add('MG', KN, 2,
    'Dịch vụ tài chính, chứng khoán mà công ty chứng khoán cung cấp cho khách hàng có các đặc điểm sau, NGOẠI TRỪ:',
    'Có thể tạo ra trước, lưu kho rồi cung cấp dần khi khách hàng cần',
    ['Vô hình, khách hàng khó đánh giá chất lượng trước khi sử dụng',
     'Việc cung cấp và việc sử dụng dịch vụ thường diễn ra đồng thời',
     'Chất lượng không đồng nhất, phụ thuộc người cung cấp và thời điểm'],
    'Dịch vụ tài chính mang các đặc điểm chung của dịch vụ: tính vô hình (không nhìn thấy, cầm nắm được nên khách hàng '
    'khó đánh giá trước, phải dựa vào uy tín và lòng tin), tính không tách rời (cung ứng và tiêu dùng diễn ra đồng thời, '
    'có sự tham gia của khách hàng), tính không đồng nhất (chất lượng thay đổi theo người phục vụ, thời điểm) và tính '
    'không thể cất trữ (không thể sản xuất trước để lưu kho). Vì vậy uy tín, kỹ năng và sự ổn định trong chất lượng phục vụ '
    'của nhân viên môi giới đặc biệt quan trọng.',
    GT + 'Đặc điểm của dịch vụ tài chính (vô hình, không tách rời, không đồng nhất, không thể cất trữ)')

# 2 – F1 câu 1
add('LU', 'Giải thích từ ngữ', 1,
    'Theo Luật Chứng khoán, chứng khoán phái sinh là:',
    'Công cụ tài chính dạng hợp đồng xác nhận quyền, nghĩa vụ thanh toán tiền, chuyển giao tài sản cơ sở theo giá xác định cho thời điểm tương lai',
    ['Chứng khoán có tài sản bảo đảm do công ty chứng khoán phát hành, cho quyền mua hoặc bán chứng khoán cơ sở với tổ chức phát hành',
     'Chứng khoán phát hành cùng trái phiếu hoặc cổ phiếu ưu đãi, cho quyền mua một số cổ phiếu phổ thông theo giá xác định trước',
     'Chứng khoán được phát hành trên cơ sở chứng khoán của tổ chức được thành lập và hoạt động hợp pháp tại Việt Nam'],
    'Khoản 9 Điều 4 Luật Chứng khoán: chứng khoán phái sinh là công cụ tài chính dưới dạng hợp đồng (quyền chọn, tương lai, '
    'kỳ hạn), xác nhận quyền, nghĩa vụ của các bên về thanh toán tiền, chuyển giao tài sản cơ sở theo mức giá đã xác định, '
    'trong khoảng thời gian hoặc vào ngày xác định trong tương lai; tài sản cơ sở là chứng khoán, chỉ số chứng khoán hoặc '
    'tài sản khác theo quy định của Chính phủ (khoản 10). Chứng khoán có tài sản bảo đảm do CTCK phát hành là chứng quyền '
    'có bảo đảm (khoản 6); chứng khoán phát hành cùng trái phiếu hoặc cổ phiếu ưu đãi là chứng quyền (khoản 5); chứng khoán '
    'phát hành trên cơ sở chứng khoán của tổ chức tại Việt Nam là chứng chỉ lưu ký (khoản 8) – đều không phải chứng khoán phái sinh.',
    'Khoản 9 Điều 4 Luật Chứng khoán 2019 (VBHN 24/VBHN-VPQH năm 2025)',
    'Chứng khoán phái sinh là công cụ tài chính dưới dạng hợp đồng, bao gồm hợp đồng quyền chọn, hợp đồng tương lai, '
    'hợp đồng kỳ hạn, trong đó xác nhận quyền, nghĩa vụ của các bên đối với việc thanh toán tiền, chuyển giao số lượng '
    'tài sản cơ sở nhất định theo mức giá đã được xác định', LCK)

# 3 – F1 câu 21, 26–30
add('MG', KN, 1,
    'Trình tự hợp lý của quy trình bán hàng (cung cấp sản phẩm, dịch vụ chứng khoán) của nhân viên môi giới đối với một khách hàng mới là:',
    'Chuẩn bị thông tin → Tiếp cận khách hàng → Giới thiệu sản phẩm → Thống nhất, ký hợp đồng → Chăm sóc sau bán',
    ['Tiếp cận khách hàng → Giới thiệu sản phẩm → Chuẩn bị thông tin → Thống nhất, ký hợp đồng → Chăm sóc sau bán',
     'Chuẩn bị thông tin → Giới thiệu sản phẩm → Tiếp cận khách hàng → Chăm sóc sau bán → Thống nhất, ký hợp đồng',
     'Giới thiệu sản phẩm → Tiếp cận khách hàng → Thống nhất, ký hợp đồng → Chuẩn bị thông tin → Chăm sóc sau bán'],
    'Trước khi gặp khách hàng, nhân viên môi giới chuẩn bị hồ sơ, thông tin về khách hàng và sản phẩm; tiếp theo tiếp cận, '
    'tạo thiện cảm và tìm hiểu nhu cầu; sau đó giới thiệu sản phẩm phù hợp với nhu cầu và giải đáp thắc mắc; khi khách hàng '
    'đồng ý thì thống nhất điều khoản, ký hợp đồng (bước chốt); cuối cùng là chăm sóc sau bán để duy trì quan hệ lâu dài và '
    'được khách hàng giới thiệu thêm khách hàng mới. Chăm sóc sau bán không thể đặt trước bước ký hợp đồng; giới thiệu sản '
    'phẩm khi chưa tiếp cận, chưa hiểu khách hàng dễ dẫn đến tư vấn không phù hợp.',
    GT + 'Kỹ năng bán hàng: quy trình bán hàng (chuẩn bị, tiếp cận, giới thiệu sản phẩm, kết thúc bán hàng, chăm sóc sau bán)')

# 4 – F2 câu 3, 4
add('MG', ML, 2,
    'Ông H luôn yêu cầu mọi việc phải làm đúng quy định, thủ tục và nguyên tắc; bà K thường quyết định theo số đông, thấy '
    'nhiều người mua thì mua theo. Theo cách phân loại khách hàng theo phong cách hành vi (độc tài, quan liêu, xã hội…), '
    'ông H và bà K lần lượt thuộc nhóm:',
    'Quan liêu và xã hội',
    ['Xã hội và quan liêu', 'Độc tài và xã hội', 'Quan liêu và độc tài'],
    'Khách hàng quan liêu làm việc theo luật lệ, quy trình, cần thông tin chi tiết, chính xác và thời gian cân nhắc – nhân '
    'viên môi giới nên chuẩn bị tài liệu đầy đủ, làm đúng thủ tục. Khách hàng xã hội coi trọng quan hệ, dễ chịu ảnh hưởng '
    'của người khác và có xu hướng làm theo đám đông – cần xây dựng quan hệ, đồng thời giúp họ thấy rủi ro của việc chạy '
    'theo số đông. Khách hàng độc tài thích chi phối, muốn khẳng định quan điểm của mình và quyết định nhanh.',
    GT + 'Phân loại khách hàng theo phong cách hành vi (độc tài, quan liêu, xã hội)')

# 5 – F2 câu 5
add('MG', ML, 2,
    'Khi làm việc với khách hàng thuộc nhóm “độc tài” (thích chi phối cuộc trao đổi, muốn áp đặt quan điểm, quyết định nhanh), '
    'cách ứng xử phù hợp của nhân viên môi giới là:',
    'Khẳng định quan điểm một cách thân thiện, lắng nghe, trình bày ngắn gọn và đi thẳng vào vấn đề',
    ['Im lặng, nhượng bộ mọi ý kiến của khách hàng để tránh làm khách hàng phật ý',
     'Tranh luận trực diện đến cùng để khách hàng thấy rõ chuyên môn của mình',
     'Gửi thật nhiều tài liệu chi tiết và để khách hàng tự nghiên cứu trong thời gian dài'],
    'Với khách hàng độc tài, né tránh hay nhượng bộ hoàn toàn làm nhân viên môi giới mất vai trò tư vấn, còn đối đầu trực '
    'tiếp dễ làm đổ vỡ quan hệ. Cách phù hợp là khẳng định thân thiện: tôn trọng, lắng nghe nhưng tự tin nêu quan điểm có '
    'căn cứ, trình bày ngắn gọn, tập trung vào kết quả và để khách hàng cảm thấy mình là người quyết định. Cung cấp nhiều '
    'tài liệu chi tiết và cho thời gian cân nhắc phù hợp hơn với khách hàng quan liêu.',
    GT + 'Cách ứng xử với từng nhóm khách hàng theo phong cách hành vi (khách hàng độc tài: khẳng định thân thiện)')

# 6 – F2 câu 8, 9, 10
add('MG', ML, 2,
    'Về các mô hình giao tiếp giữa nhân viên môi giới và khách hàng (bổ sung, đối xứng, song song), nhận định nào sau đây đúng?',
    'Song song: hai bên linh hoạt đổi vai trò dẫn dắt, là kiểu giao tiếp tích cực, hiệu quả',
    ['Bổ sung: cả hai bên cùng muốn chi phối nên dễ phát sinh cạnh tranh, căng thẳng',
     'Đối xứng: một bên chi phối, bên còn lại chấp nhận để mình bị chi phối',
     'Đối xứng: hai bên luân phiên dẫn dắt, là kiểu giao tiếp linh hoạt nhất'],
    'Giao tiếp bổ sung: một bên chi phối, một bên bị chi phối (hai vai trò bổ sung cho nhau). Giao tiếp đối xứng: hai bên có '
    'hành vi giống nhau – cùng muốn kiểm soát hoặc cùng bị động – dễ dẫn tới cạnh tranh, căng thẳng hoặc bế tắc. Giao tiếp '
    'song song: hai bên linh hoạt chuyển đổi vai trò tùy tình huống, là kiểu giao tiếp tích cực, hiệu quả mà nhân viên môi '
    'giới nên hướng tới.',
    GT + 'Các mô hình giao tiếp với khách hàng (bổ sung, đối xứng, song song)')

# 7 – F2 câu 13
add('MG', ML, 1,
    'Theo thang nhu cầu của Maslow, thứ tự các bậc nhu cầu của con người từ thấp đến cao là:',
    'Sinh lý → An toàn → Xã hội → Được tôn trọng → Tự thể hiện',
    ['An toàn → Sinh lý → Xã hội → Được tôn trọng → Tự thể hiện',
     'Sinh lý → Xã hội → An toàn → Tự thể hiện → Được tôn trọng',
     'Sinh lý → An toàn → Được tôn trọng → Xã hội → Tự thể hiện'],
    'Maslow xếp nhu cầu thành 5 bậc: sinh lý (ăn, mặc, ở) → an toàn (ổn định, được bảo vệ) → xã hội (được yêu thương, thuộc '
    'về một nhóm) → được tôn trọng (địa vị, được công nhận) → tự thể hiện (phát huy năng lực bản thân). Khi nhu cầu bậc thấp '
    'cơ bản được đáp ứng, nhu cầu bậc cao hơn mới trở thành động lực chính. Nhân viên môi giới dùng thang này để hiểu động cơ '
    'đầu tư: khách hàng chưa có quỹ dự phòng sẽ ưu tiên an toàn, còn khách hàng đã đủ đầy có thể đầu tư vì mong muốn được '
    'công nhận, tự khẳng định.',
    GT + 'Tìm hiểu nhu cầu khách hàng theo thang nhu cầu của Maslow')

# 8 – F2 câu 12, 14, 15, 20
add('MG', ML, 2,
    'Khi lập hồ sơ khách hàng, mục tiêu đầu tư nào sau đây được xác định rõ ràng nhất, có tác dụng thúc đẩy và làm căn cứ tư vấn tốt nhất?',
    'Tích lũy đủ 1,5 tỷ đồng sau 10 năm để thanh toán tiền mua nhà',
    ['Đầu tư sao cho tài sản tăng nhanh nhất có thể trong thời gian tới',
     'Có thu nhập ổn định hơn để cuộc sống gia đình thoải mái hơn',
     'Đạt mức lợi nhuận cao hơn bình quân của thị trường chứng khoán'],
    'Mục tiêu đầu tư cụ thể gắn với nhu cầu thực (mua nhà, học phí, nghỉ hưu…), có số tiền và thời hạn xác định nên đo lường '
    'được, tạo động lực tích lũy và giúp tính được mức sinh lời yêu cầu, khung thời gian, mức rủi ro phù hợp. Khi khách hàng có '
    'nhiều mục tiêu, nhân viên môi giới cần sắp xếp thứ tự ưu tiên và xác định giới hạn (số tiền, thời gian) cho từng mục tiêu. '
    'Các mong muốn chung chung như tăng tài sản nhanh, sống thoải mái hơn hay thắng thị trường không đo lường được nên khó làm '
    'căn cứ tư vấn.',
    GT + 'Xây dựng hồ sơ khách hàng: xác định mục tiêu đầu tư cụ thể, thứ tự ưu tiên và giới hạn')

# 9 – F2 câu 23
add('MG', ML, 2,
    'Một khách hàng cá nhân ra quyết định dựa trên số liệu và báo cáo phân tích, thường tìm thêm nguồn thông tin để kiểm chứng '
    'và hầu như không gắn cảm xúc với khoản đầu tư của mình. Theo cách phân loại nhà đầu tư cá nhân theo tính cách, khách '
    'hàng này thuộc nhóm:',
    'Nhà đầu tư có phương pháp',
    ['Nhà đầu tư thận trọng', 'Nhà đầu tư cá nhân (độc lập)', 'Nhà đầu tư tự phát'],
    'Phân loại theo tính cách gồm 4 nhóm. Nhà đầu tư có phương pháp dựa vào dữ kiện, số liệu, nghiên cứu, ít để cảm xúc chi '
    'phối. Nhà đầu tư thận trọng đặt nặng an toàn tài chính, rất ngại thua lỗ, chuộng tài sản ít biến động và thường chậm ra '
    'quyết định. Nhà đầu tư cá nhân (độc lập) tự tin, thích tự nghiên cứu và tự quyết định. Nhà đầu tư tự phát hay thay đổi '
    'danh mục theo diễn biến thị trường, sợ bỏ lỡ cơ hội hơn sợ rủi ro nên vòng quay và chi phí giao dịch cao.',
    GT + 'Phân loại nhà đầu tư cá nhân theo tính cách (thận trọng, có phương pháp, cá nhân, tự phát)')

# 10 – F2 câu 24, 25
add('MG', ML, 2,
    'So với khách hàng cá nhân, khách hàng tổ chức như quỹ hưu trí, công ty bảo hiểm, ngân hàng thương mại thường có đặc điểm nào sau đây?',
    'Mục tiêu, ràng buộc đầu tư được xác định rõ theo chức năng, điều lệ và quy định áp dụng',
    ['Quyết định đầu tư chủ yếu dựa vào cảm xúc và sở thích của người đứng đầu tổ chức',
     'Mục tiêu đầu tư thay đổi liên tục theo diễn biến thị trường, khó xác định trước',
     'Không chịu ràng buộc pháp lý về danh mục nên được tự do đầu tư mọi loại tài sản'],
    'Khách hàng tổ chức đầu tư theo chức năng hoạt động: quỹ hưu trí phải bảo đảm chi trả lương hưu dài hạn, công ty bảo hiểm '
    'phải cân đối tài sản với nghĩa vụ bồi thường, ngân hàng chú trọng thanh khoản. Vì vậy mục tiêu, khẩu vị rủi ro và các ràng '
    'buộc về thanh khoản, thời hạn, pháp lý (giới hạn đầu tư theo luật chuyên ngành, điều lệ) được xác định rõ; quyết định '
    'thường qua quy trình tập thể, ít bị cảm xúc chi phối như nhiều khách hàng cá nhân.',
    GT + 'Đặc điểm khách hàng tổ chức (quỹ hưu trí, công ty bảo hiểm, ngân hàng)')

# 11 – F3 câu 15, 21, 28
add('MG', XD, 3,
    'Nhân viên tư vấn của công ty chứng khoán A được hưởng hoa hồng cao hơn khi giới thiệu chứng chỉ quỹ do công ty quản lý '
    'quỹ cùng tập đoàn với A quản lý. Cách xử lý phù hợp với nguyên tắc quản lý xung đột lợi ích là:',
    'Công khai mối quan hệ và cơ chế hoa hồng, chỉ giới thiệu khi sản phẩm phù hợp với khách hàng',
    ['Ưu tiên giới thiệu sản phẩm cùng tập đoàn vì nhân viên hiểu rõ sản phẩm này hơn',
     'Giới thiệu như sản phẩm khác, không nêu cơ chế hoa hồng vì đó là thông tin nội bộ',
     'Chỉ giới thiệu sản phẩm cùng tập đoàn cho các khách hàng có khẩu vị rủi ro cao'],
    'Bán sản phẩm của công ty liên quan khi được hưởng thù lao cao hơn là xung đột lợi ích tiềm ẩn: nhân viên dễ tư vấn thiên '
    'lệch về sản phẩm nội bộ. Biện pháp cơ bản là công bố cho khách hàng mối quan hệ và lợi ích của mình để khách hàng tự '
    'đánh giá, kết hợp kiểm soát nội bộ và chỉ khuyến nghị khi sản phẩm phù hợp với tình hình tài chính, mục tiêu, khả năng '
    'chấp nhận rủi ro của khách hàng. Luật Chứng khoán yêu cầu CTCK giám sát, ngăn ngừa xung đột lợi ích trong giao dịch với '
    'người có liên quan (khoản 1 Điều 89), cung cấp đầy đủ, trung thực thông tin (khoản 4) và bảo đảm tư vấn phù hợp với '
    'từng khách hàng (khoản 6). Khẩu vị rủi ro cao không thay thế việc công khai xung đột lợi ích.',
    'Khoản 1, 4, 6 Điều 89 Luật Chứng khoán 2019; ' + GT + 'Xung đột lợi ích khi bán sản phẩm của công ty liên quan, biện pháp công bố và kiểm soát',
    src=LCK)

# 12 – F2 câu 29
add('LU', 'Hoạt động CTCK', 1,
    'Theo Thông tư 121/2020/TT-BTC (sửa đổi bởi Thông tư 08/2026/TT-BTC), khi thực hiện nghiệp vụ môi giới, công ty chứng '
    'khoán có nghĩa vụ cập nhật các thông tin thay đổi của khách hàng trong trường hợp nào?',
    'Khi khách hàng hoặc tổ chức kinh doanh chứng khoán nước ngoài đại diện có yêu cầu',
    ['Khi Ủy ban Chứng khoán Nhà nước yêu cầu trong quá trình thanh tra, kiểm tra công ty',
     'Khi Tổng công ty Lưu ký và Bù trừ chứng khoán Việt Nam gửi thông báo thay đổi',
     'Khi khách hàng phát sinh giao dịch có giá trị từ 01 tỷ đồng trở lên trong ngày'],
    'Khoản 2 Điều 14 TT 121/2020 (sửa đổi bởi khoản 1 Điều 10 TT 08/2026/TT-BTC): công ty chứng khoán có nghĩa vụ cập nhật '
    'các thông tin thay đổi của khách hàng khi khách hàng hoặc tổ chức kinh doanh chứng khoán nước ngoài đại diện có yêu cầu. '
    'Khoản 7 Điều 89 Luật Chứng khoán cũng yêu cầu CTCK cập nhật, lưu giữ đầy đủ hồ sơ thông tin khách hàng; còn khách hàng '
    'chịu trách nhiệm cung cấp đầy đủ, chính xác thông tin nhận biết khách hàng (khoản 1 Điều 15 TT 121/2020). Thông tư không '
    'gắn nghĩa vụ này với yêu cầu của UBCKNN, thông báo của VSDC hay giá trị giao dịch.',
    'Khoản 2 Điều 14 Thông tư 121/2020/TT-BTC (sửa đổi bởi khoản 1 Điều 10 Thông tư 08/2026/TT-BTC; VBHN 09/VBHN-BTC năm 2026)',
    'Công ty chứng khoán có nghĩa vụ cập nhật các thông tin thay đổi của khách hàng khi khách hàng hoặc tổ chức kinh '
    'doanh chứng khoán nước ngoài đại diện có yêu cầu.', TT121)

# ---- ghi file: đáp án đúng xoay đều A–D ----
out = []
for i, x in enumerate(Q, 1):
    a = (i + 1) % 4
    o = x['wrong'][:]
    o.insert(a, x['correct'])
    lens = [len(s) for s in o]
    assert max(lens) <= 2.2 * min(lens) or max(lens) - min(lens) <= 12, (i, lens)
    assert len(x['quote']) <= 300, (i, len(x['quote']))
    assert (x['subject'] == 'LU') == bool(x['quote']), i
    assert not re.search(r"(phương án|đáp án|chọn|câu)\s+[A-D]\b", x['e']), i
    out.append(dict(id=f"C10-{i:03d}", part='LUAT' if x['subject'] == 'LU' else 'CM', subject=x['subject'],
                    topic=x['topic'], level=x['level'], q=x['q'], o=o, a=a, e=x['e'], basis=x['basis'],
                    quote=x['quote'], src=x['src'], as_of='2026-11'))
with open(OUT, 'w', encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False, indent=1)
print('wrote', len(out), 'a:', dict(sorted(Counter(x['a'] for x in out).items())),
      'subject:', dict(Counter(x['subject'] for x in out)))
