# Áp dụng các sửa đổi soát chéo vào cm_14.json (giữ id, giữ định dạng indent=1)
import json
P = '/home/user/cchn_moi/web/data/src/cm_14.json'
d = json.load(open(P, encoding='utf-8')); by = {x['id']: x for x in d}
def upd(i, **kw): by[i].update(kw)

upd('C14-001',
    e=by['C14-001']['e'].replace('Họ vẫn được mua', 'Điểm a khoản 1 Điều 27 cũng ghi nhà tạo lập thị trường là đối tượng duy nhất được tham gia các phiên phát hành theo phương thức đấu thầu. Các đối tượng khác vẫn được mua'),
    basis='Khoản 3 Điều 15, điểm a khoản 1 Điều 26, điểm a khoản 1 Điều 27 Nghị định 95/2018/NĐ-CP (các điều này không bị NĐ 83/2023/NĐ-CP, NĐ 84/2026/NĐ-CP sửa đổi)')

upd('C14-003',
    e='Khoản 2 Điều 3 NĐ 95/2018: đấu thầu đơn giá là phương thức mà lãi suất phát hành là mức lãi suất trúng thầu cao nhất, áp dụng chung cho các thành viên trúng thầu. Trước đây khoản 5 Điều 15 cho Bộ Tài chính chọn đơn giá hoặc đa giá (đa giá: mỗi thành viên hưởng đúng lãi suất dự thầu của mình) trong từng thời kỳ; NĐ 83/2023 (hiệu lực 15/01/2024) sửa khoản 5 Điều 15 chỉ còn đấu thầu đơn giá và bãi bỏ định nghĩa đấu thầu đa giá tại khoản 3 Điều 3. Lãi suất bình quân gia quyền không phải là phương thức xác định kết quả đấu thầu theo Nghị định.',
    basis='Khoản 2 Điều 3 Nghị định 95/2018/NĐ-CP; khoản 5 Điều 15 (sửa đổi bởi khoản 1 Điều 1 Nghị định 83/2023/NĐ-CP); khoản 3 Điều 3 (bãi bỏ bởi khoản 1 Điều 2 Nghị định 83/2023/NĐ-CP)')

upd('C14-006',
    q='Nhà tạo lập thị trường M đề nghị Kho bạc Nhà nước phát hành 1.500.000 trái phiếu Chính phủ mã X (mệnh giá 100.000 đồng) để đảm bảo thanh khoản. Giả định giá thị trường dùng để tính ký quỹ là 102.400 đồng/trái phiếu và tỷ lệ phòng ngừa rủi ro là 4% tính trên giá trị trái phiếu phát hành theo giá thị trường. Theo Nghị định 95/2018/NĐ-CP, số tiền M phải ký quỹ tại Kho bạc Nhà nước là:',
    o=['153.600.000.000 đồng', '156.000.000.000 đồng', '159.744.000.000 đồng', '160.000.000.000 đồng'], a=2,
    e='Điểm b khoản 2 Điều 20: số tiền ký quỹ tương ứng khối lượng trái phiếu dự kiến phát hành tính theo giá thị trường cộng thêm tỷ lệ phòng ngừa rủi ro tính trên giá trị trái phiếu phát hành. Giá trị theo giá thị trường = 1.500.000 × 102.400 = 153.600.000.000 đồng; ký quỹ = 153.600.000.000 × (1 + 4%) = 159.744.000.000 đồng. Lỗi thường gặp: bỏ tỷ lệ phòng ngừa rủi ro (153.600.000.000), tính theo mệnh giá (1.500.000 × 100.000 × 1,04 = 156.000.000.000), chia cho (1 − 4%) như cách tính chiết khấu (160.000.000.000).')

upd('C14-008',
    o=['Ủy ban Thường vụ Quốc hội, trên cơ sở báo cáo của Chính phủ', 'Thủ tướng Chính phủ, trên cơ sở đề nghị của Bộ Tài chính', 'Bộ trưởng Bộ Tài chính, sau khi lấy ý kiến Ngân hàng Nhà nước', 'Kho bạc Nhà nước, căn cứ hạn mức phát hành trái phiếu hằng năm'], a=0,
    basis='Khoản 2, 3 Điều 23 Nghị định 95/2018/NĐ-CP (Điều 23 không bị NĐ 83/2023/NĐ-CP, NĐ 84/2026/NĐ-CP sửa đổi)')

upd('C14-009',
    e='Khoản 2 Điều 21 NĐ 95/2018 (sửa đổi bởi khoản 1 Điều 4 NĐ 84/2026, hiệu lực 25/3/2026): Bộ Tài chính phối hợp với Bộ Nông nghiệp và Môi trường xây dựng đề án phát hành trái phiếu Chính phủ xanh, báo cáo Thủ tướng Chính phủ phê duyệt trước khi triển khai. Đề án gồm mục đích, khối lượng, điều kiện điều khoản, đối tượng mua, phương thức phát hành, việc đăng ký, lưu ký, niêm yết, giao dịch và danh mục dự án sử dụng vốn. Bản năm 2018 ghi Bộ Tài chính phối hợp với Bộ Kế hoạch và Đầu tư, Bộ Tài nguyên và Môi trường (hai bộ này đã được tổ chức lại năm 2025), nên tài liệu cũ nêu hai bộ này là lỗi thời; cấp phê duyệt là Thủ tướng ngay từ bản gốc, ghi “báo cáo Chính phủ” là chưa chính xác.')

upd('C14-010',
    q='Theo Thông tư 30/2019/TT-BTC, xét các nhận định về thành viên giao dịch trên thị trường giao dịch công cụ nợ tại Sở giao dịch chứng khoán:\nI. Thành viên giao dịch thông thường là công ty chứng khoán, được thực hiện nghiệp vụ môi giới và tự doanh công cụ nợ.\nII. Công ty chứng khoán muốn làm thành viên giao dịch thông thường phải là thành viên lưu ký và được phép thực hiện đủ các nghiệp vụ môi giới, tự doanh, tư vấn đầu tư, bảo lãnh phát hành chứng khoán.\nIII. Nhà đầu tư cá nhân có thể đặt lệnh mua trái phiếu Chính phủ qua thành viên giao dịch đặc biệt là ngân hàng thương mại.\nCác nhận định đúng là:',
    e='Điểm a khoản 1 Điều 5 TT 30/2019: thành viên giao dịch thông thường là công ty chứng khoán được Sở chấp thuận, được môi giới và tự doanh công cụ nợ (I đúng). Điểm a, b khoản 1 Điều 6: công ty chứng khoán phải được phép thực hiện tất cả các nghiệp vụ môi giới, tự doanh, tư vấn đầu tư, bảo lãnh phát hành chứng khoán và là thành viên lưu ký (II đúng; khoản 1 Điều 97 NĐ 155/2020 yêu cầu tương tự với thành viên giao dịch công cụ nợ). Điểm b khoản 1 Điều 5: thành viên giao dịch đặc biệt (ngân hàng thương mại, chi nhánh ngân hàng) chỉ được mua, bán công cụ nợ cho chính mình nên không nhận lệnh của nhà đầu tư (III sai; khoản 3 Điều 99 NĐ 155/2020).',
    basis='Điểm a, b khoản 1 Điều 5, điểm a, b khoản 1 Điều 6 Thông tư 30/2019/TT-BTC; khoản 1 Điều 97, khoản 3 Điều 99 Nghị định 155/2020/NĐ-CP (hai điều này không bị NĐ 245/2025/NĐ-CP sửa đổi)',
    quote='Là công ty chứng khoán được Ủy ban Chứng khoán Nhà nước cấp Giấy phép thành lập và hoạt động công ty chứng khoán; được phép thực hiện tất cả các nghiệp vụ kinh doanh bao gồm: môi giới chứng khoán, tự doanh chứng khoán, tư vấn đầu tư chứng khoán, bảo lãnh phát hành chứng khoán;')

o = by['C14-012']['o']; o[3] = 'Chỉ nhà tạo lập thị trường do Bộ Tài chính lựa chọn theo quy định'

upd('C14-013', e=by['C14-013']['e'].replace(
    'So khớp theo giá, thời gian là phương thức khớp lệnh, không áp dụng cho công cụ nợ của Chính phủ.',
    'So khớp lệnh theo thứ tự ưu tiên giá, thời gian là phương thức khớp lệnh; khoản 1 Điều 16 quy định Sở áp dụng phương thức thỏa thuận cho giao dịch công cụ nợ (Sở chỉ đổi phương thức khi được UBCKNN chấp thuận).'))

upd('C14-014', e=by['C14-014']['e'].replace(
    'ngày 09/04/2027 đã quá hạn này.',
    'nếu không có ngày nghỉ lễ xen giữa, hạn chót là thứ Năm 01/04/2027 (25/3/2027 là thứ Năm), nên ngày 09/04/2027 đã quá hạn.'))

upd('C14-018',
    o=['31/12/2026', '07/01/2027', '08/01/2027', '15/01/2027'], a=2,
    e='Thời hạn là 15 ngày làm việc kể từ ngày công bố thông tin về kết quả đợt chào bán (điểm b khoản 2 Điều 21), không tính ngày bắt đầu (khoản 3 Điều 147 Bộ luật Dân sự). Đếm: 18/12 (1); 21–25/12 (2–6); 28–31/12 (7–10); 01/01/2027 nghỉ; 04–08/01/2027 (11–15) → hạn cuối thứ Sáu 08/01/2027. 07/01/2027 là do coi 01/01 là ngày làm việc hoặc tính cả ngày công bố; 31/12/2026 là mốc 10 ngày làm việc (nhầm với thời hạn đưa trái phiếu vào giao dịch sau thông báo của Sở, điểm d khoản 4); 15/01/2027 là cộng thêm 05 ngày làm việc (nhầm với thời hạn Sở ra thông báo, điểm c khoản 4).',
    basis='Điểm b khoản 2, điểm c, d khoản 4 Điều 21 Nghị định 200/2026/NĐ-CP; khoản 3 Điều 147 Bộ luật Dân sự 2015; ngày nghỉ là giả định nêu trong đề')

o = by['C14-021']['o']; by['C14-021']['o'] = [o[1], o[0], o[2], o[3]]; by['C14-021']['a'] = 0
upd('C14-021', e=by['C14-021']['e'].replace(
    'Riêng việc làm cho công ty chứng khoán khác còn vi phạm',
    'Nếu nhân viên là người hành nghề chứng khoán thì việc làm cho công ty chứng khoán khác còn vi phạm'))

upd('C14-023',
    e='Khoản 4 Điều 4 TT 121: công ty chứng khoán không được xâm phạm tài sản, quyền và lợi ích hợp pháp của khách hàng; phải quản lý tách biệt tài sản của từng khách hàng và tách biệt với tài sản của công ty (cũng là nghĩa vụ tại khoản 3 Điều 89 Luật Chứng khoán). Điểm a khoản 1 Điều 18 yêu cầu quản lý tách biệt chứng khoán của khách hàng; điểm g khoản 4 Điều 13 cấm xâm phạm tài sản của khách hàng khi môi giới. Dùng chứng khoán của khách hàng bảo đảm khoản vay của chính công ty là “mượn” tài sản của khách hàng, một dạng xung đột lợi ích giữa công ty và khách hàng; thông báo sau cho khách hàng hay giữ tổng nợ trong giới hạn 05 lần vốn chủ sở hữu (khoản 1 Điều 26) không làm việc này hợp pháp.',
    basis='Khoản 4 Điều 4, điểm g khoản 4 Điều 13, điểm a khoản 1 Điều 18, khoản 1 Điều 26 Thông tư 121/2020/TT-BTC (VBHN 09/VBHN-BTC năm 2026); khoản 3 Điều 89 Luật Chứng khoán 2019 (VBHN 102/VBHN-VPQH năm 2026)')

upd('C14-024',
    q='Công ty chứng khoán Q cần bổ nhiệm trưởng bộ phận kiểm soát nội bộ, bộ phận giám sát các hoạt động tiềm ẩn xung đột lợi ích như tự doanh của công ty và giao dịch cá nhân của nhân viên. Chỉ xét thông tin nêu trong từng phương án, theo Thông tư 121/2020/TT-BTC, ứng viên nào sau đây đáp ứng yêu cầu nhân sự của vị trí này?',
    o=['Ông C, kế toán viên lâu năm, có chứng chỉ hành nghề và chứng chỉ Pháp luật về chứng khoán, chuyên trách vị trí này',
       'Bà A, kiểm toán viên lâu năm, có đủ các chứng chỉ chuyên môn theo quy định, là em ruột của một Phó Tổng Giám đốc của Q',
       'Anh B, có chuyên môn về luật, có đủ các chứng chỉ chuyên môn theo quy định, đồng thời kiêm trưởng phòng tự doanh của Q',
       'Chị D, kiểm toán viên lâu năm, có chứng chỉ hành nghề chứng khoán nhưng chưa có chứng chỉ Pháp luật về chứng khoán'],
    a=0, level=2,
    e='Khoản 4 Điều 12 TT 121: trưởng bộ phận kiểm soát nội bộ phải có chuyên môn về luật, kế toán, kiểm toán, đủ kinh nghiệm, uy tín (điểm b); không phải là người có liên quan đến các trưởng bộ phận chuyên môn, người thực hiện nghiệp vụ, Tổng Giám đốc, Phó Tổng Giám đốc, Giám đốc chi nhánh (điểm c); có chứng chỉ Những vấn đề cơ bản về chứng khoán và thị trường chứng khoán hoặc chứng chỉ hành nghề, và chứng chỉ Pháp luật về chứng khoán và thị trường chứng khoán (điểm d); không kiêm nhiệm công việc khác trong công ty (điểm đ). Bà A là người có liên quan của Phó Tổng Giám đốc (em ruột, điểm d khoản 46 Điều 4 Luật Chứng khoán); anh B kiêm nhiệm, lại chính là người bị giám sát; chị D thiếu chứng chỉ Pháp luật. Các yêu cầu này bảo đảm bộ phận kiểm soát nội bộ độc lập khi giám sát xung đột lợi ích (khoản 1 Điều 89 Luật Chứng khoán).',
    basis='Khoản 1, điểm b khoản 2, khoản 4 Điều 12 Thông tư 121/2020/TT-BTC (VBHN 09/VBHN-BTC năm 2026); điểm d khoản 46 Điều 4, khoản 1 Điều 89 Luật Chứng khoán 2019 (VBHN 102/VBHN-VPQH năm 2026)',
    quote='Không phải là người có liên quan đến các trưởng bộ phận chuyên môn, người thực hiện nghiệp vụ, Tổng Giám đốc (Giám đốc), Phó Tổng Giám đốc (Phó Giám đốc), Giám đốc chi nhánh trong công ty chứng khoán;',
    src='VBHN_09_VBHN-BTC_2026_TT121_68_08_hop_nhat.txt')

upd('C14-026',
    q='Công ty chứng khoán K là thành viên giao dịch thông thường trên thị trường trái phiếu Chính phủ. Khách hàng đặt lệnh mua 50.000 trái phiếu mã Z với giá tối đa 101.500 đồng/trái phiếu. Bộ phận tự doanh của K cũng muốn mua Z và đã gửi yêu cầu cho đại diện giao dịch sớm hơn lệnh của khách hàng vài phút. Trên hệ thống đang có lệnh chào bán 50.000 trái phiếu Z giá 101.300 đồng. Theo Thông tư 30/2019/TT-BTC, K phải:',
    o=['Mua 50.000 trái phiếu giá 101.300 đồng cho tự doanh, rồi bán lại cho khách hàng giá 101.500 đồng',
       'Chia đều khối lượng chào bán giá 101.300 đồng cho khách hàng và bộ phận tự doanh của K',
       'Mua cho tự doanh trước vì yêu cầu của tự doanh được đưa ra sớm hơn lệnh của khách hàng',
       'Ưu tiên thực hiện lệnh của khách hàng, mua cho khách hàng ở mức 101.300 đồng đang được chào'],
    a=3,
    e='Điểm d khoản 3 Điều 10 TT 30: thành viên giao dịch phải ưu tiên thực hiện lệnh môi giới cho khách hàng trước lệnh tự doanh, với mức giá thực hiện tốt nhất có thể trên hệ thống; mức giá tốt nhất có thể là mức giá theo yêu cầu của khách hàng hoặc tốt hơn. Nguyên tắc ưu tiên khách hàng không phụ thuộc yêu cầu tự doanh có trước hay sau (khoản 5 Điều 89 Luật Chứng khoán, khoản 4 Điều 22 TT 121). Có lệnh chào bán 101.300 đồng (tốt hơn giá tối đa 101.500 đồng) thì phải mua cho khách hàng ở giá này. Tự doanh mua trước rồi bán lại cho khách hàng giá cao hơn, hay chia bớt khối lượng cho tự doanh, là đặt lợi ích công ty lên trên khách hàng (xung đột lợi ích).',
    basis='Điểm d khoản 3 Điều 10 Thông tư 30/2019/TT-BTC; khoản 5 Điều 89 Luật Chứng khoán 2019 (VBHN 102/VBHN-VPQH năm 2026); khoản 4 Điều 22 Thông tư 121/2020/TT-BTC')

# tự kiểm
for x in d:
    assert len(x['o']) == 4 and len(set(x['o'])) == 4 and 0 <= x['a'] < 4, x['id']
assert by['C14-006']['o'][by['C14-006']['a']] == '159.744.000.000 đồng'
assert by['C14-018']['o'][by['C14-018']['a']] == '08/01/2027'
assert by['C14-021']['o'][0].startswith('Xung đột giữa nhân viên và công ty')
assert by['C14-008']['o'][0].startswith('Ủy ban Thường vụ Quốc hội')
open(P, 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, indent=1) + '\n')
print('đã ghi', len(d), 'câu')

# --- đợt 2: cân độ dài phương án C14-007, C14-020
d = json.load(open(P, encoding='utf-8')); by = {x['id']: x for x in d}
by['C14-007']['o'] = ['Trái phiếu Chính phủ xanh phát hành cho dự án xanh', 'Trái phiếu Chính phủ bằng ngoại tệ tự do chuyển đổi',
                      'Trái phiếu Chính phủ phát hành theo phương thức riêng lẻ', 'Trái phiếu Chính phủ phát hành để đảm bảo thanh khoản']
by['C14-007']['a'] = 1
by['C14-020']['o'][1] = 'Chuyển giao theo quyết định của Trọng tài khi giải quyết tranh chấp hợp đồng'
by['C14-020']['o'][2] = 'Nhận thừa kế trái phiếu của cha mẹ theo quy định của pháp luật về thừa kế'
for x in d: assert len(set(x['o'])) == 4
open(P, 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, indent=1) + '\n')
print('đợt 2 xong')

# --- đợt 3: nói rõ loại chứng chỉ ở đáp án C14-024
d = json.load(open(P, encoding='utf-8')); by = {x['id']: x for x in d}
by['C14-024']['o'][0] = 'Ông C, kế toán viên lâu năm, có chứng chỉ hành nghề chứng khoán và chứng chỉ Pháp luật về chứng khoán, chỉ làm việc này'
open(P, 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, indent=1) + '\n')
print('đợt 3 xong')
