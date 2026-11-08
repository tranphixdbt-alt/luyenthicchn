# Rebuild cm_12.json from the backup cm_12.orig.json with the second-pass fixes.
import json
P = '/home/user/cchn_moi/web/data/src/'
qs = json.load(open(P + 'work_review_c12/cm_12.orig.json', encoding='utf-8'))
Q = {q['id']: q for q in qs}

def rep(i, field, old, new):
    s = Q[i][field]
    assert s.count(old) == 1, (i, field, old)
    Q[i][field] = s.replace(old, new)

# C12-001: buyback/capital-reduction rule is Điều 36 khoản 5 (Điều 37 is reporting/disclosure); record date made explicit.
rep('C12-001', 'q', 'do K mua lại trước năm 2021 và chưa bán ra;',
    'do K mua lại trước năm 2021, đến ngày đăng ký cuối cùng vẫn chưa bán ra;')
rep('C12-001', 'e', 'ra 2.667 đồng (đó là EPS).', 'ra 2.667 đồng (12.000.000.000 / 4.500.000, tức EPS khi số cổ phiếu lưu hành không đổi trong năm).')
rep('C12-001', 'e', 'theo khoản 1, điểm a khoản 2 Điều 37 Luật Chứng khoán phải giảm vốn điều lệ tương ứng (khoản 5)',
    'theo khoản 1, điểm a khoản 2 Điều 36 Luật Chứng khoán phải làm thủ tục giảm vốn điều lệ tương ứng (khoản 5 Điều 36)')
rep('C12-001', 'basis', 'khoản 5 Điều 37 Luật Chứng khoán', 'khoản 5 Điều 36 Luật Chứng khoán')

# C12-002: order types belong to the exchange's rules (may change with KRX); explain why each distractor fails.
rep('C12-002', 'e', 'Lệnh giới hạn mua giá 69.000 sẽ khớp ngay ở giá bán hiện có quanh 60.000 nên đóng vị thế luôn; lệnh dừng để bán dùng bảo vệ vị thế mua; 51.000 là mức giá có lãi của vị thế bán khống, không phải ngưỡng lỗ.',
    'Lệnh giới hạn mua giá 69.000 có hiệu lực ngay chứ không chờ giá tăng: nếu hợp lệ sẽ khớp ngay với lệnh bán quanh 60.000 (đóng vị thế luôn), nếu vượt giá trần thì bị từ chối. Lệnh dừng để bán dùng bảo vệ vị thế mua. 51.000 = 60.000 × (1 − 15%) là mức giá có lãi của vị thế bán khống; lệnh dừng mua đặt thấp hơn giá thị trường sẽ bị kích hoạt ngay.')
rep('C12-002', 'e', 'lệnh dừng không phải loại lệnh của Sở mà là lệnh điều kiện do một số công ty chứng khoán cung cấp, nên đề nêu dưới dạng giả sử.',
    'các loại lệnh do quy chế giao dịch của Sở giao dịch chứng khoán Việt Nam quy định (khoản 3 Điều 3) và có thể thay đổi theo hệ thống giao dịch mới; trên thực tế lệnh dừng thường là lệnh điều kiện do công ty chứng khoán cung cấp, nên đề nêu dưới dạng giả sử.')
rep('C12-002', 'basis', 'khoản 3 Điều 7, Điều 11 Thông tư', 'khoản 3 Điều 3, khoản 3 Điều 7, Điều 11 Thông tư')

# C12-003: a sell stop above market is either triggered at once or rejected; band check for the limit order.
rep('C12-003', 'e', 'Giá dừng bán cao hơn giá thị trường sẽ kích hoạt ngay (bán luôn);',
    'Giá dừng bán cao hơn giá thị trường sẽ bị kích hoạt ngay (bán luôn) hoặc bị từ chối, không chờ giá giảm;')

# C12-005: financial statements are part of the prospectus (Điều 19 khoản 1 điểm c), not a separate item of Điều 18 khoản 1.
rep('C12-005', 'e', 'Giấy đăng ký, báo cáo tài chính, nghị quyết thông qua phương án phát hành là các tài liệu khác trong hồ sơ (Điều 18).',
    'Giấy đăng ký chào bán và quyết định của Đại hội đồng cổ đông thông qua phương án phát hành, phương án sử dụng vốn là các tài liệu khác trong hồ sơ (khoản 1 Điều 18); báo cáo tài chính 02 năm gần nhất là một phần nội dung của bản cáo bạch (điểm c khoản 1 Điều 19).')

# C12-006: khoản 3 Điều 3 lists trading time, price band, order types…, not "khối lượng"; add the khoản 7 Điều 2 definition.
rep('C12-006', 'e', 'Thời gian, biên độ, khối lượng của giao dịch thỏa thuận do quy chế giao dịch của Sở giao dịch chứng khoán Việt Nam quy định (khoản 3 Điều 3).',
    'Định nghĩa ở khoản 7 Điều 2 cũng vậy: các bên thông qua thành viên giao dịch tự thỏa thuận các điều kiện giao dịch trên hệ thống, hoặc thỏa thuận, thực hiện rồi ghi nhận kết quả vào hệ thống. Thời gian giao dịch, biên độ dao động giá, loại lệnh… do quy chế giao dịch của Sở giao dịch chứng khoán Việt Nam quy định (khoản 3 Điều 3).')
rep('C12-006', 'basis', 'Điểm a, b khoản 1 và khoản 3 Điều 3', 'Khoản 7 Điều 2, điểm a, b khoản 1 và khoản 3 Điều 3')

# C12-007: state band, tick and "no other orders/cancellations" so the book is fully specified.
rep('C12-007', 'q', 'Cổ phiếu G có giá tham chiếu 45.000 đồng, sổ lệnh ban đầu trống;',
    'Cổ phiếu G có giá tham chiếu 45.000 đồng, biên độ ±7%, bước giá 50 đồng; sổ lệnh ban đầu trống, ngoài các lệnh dưới đây không có lệnh nào khác và không lệnh nào bị sửa, hủy;')
rep('C12-007', 'q', '(1) P mua LO 2.000 cổ phiếu giá 44.800;', '(1) P mua LO 2.000 cổ phiếu giá 44.800 đồng;')
rep('C12-007', 'q', 'giá 45.300; (3)', 'giá 45.300 đồng; (3)')
rep('C12-007', 'q', 'giá 45.000; (4)', 'giá 45.000 đồng; (4)')
rep('C12-007', 'q', 'giá 45.500. Kết quả', 'giá 45.500 đồng. Kết quả')
rep('C12-007', 'e', 'Xử lý theo thứ tự nhập:', 'Giá trần/sàn 48.150/41.850 đồng, mọi giá đặt đều hợp lệ (bội số 50 đồng, trong biên độ). Xử lý theo thứ tự nhập:')

json.dump(qs, open(P + 'cm_12.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('written')
