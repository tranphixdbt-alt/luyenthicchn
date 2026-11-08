"""Second-pass fixes for cm_4.json. Run once: python3 -I fix.py (reads cm_4.orig.json, writes cm_4.json)."""
import json, re

D = '/home/user/cchn_moi/web/data/src/'
data = json.load(open(D + 'work_review_c4/cm_4.orig.json', encoding='utf-8'))
Q = {x['id']: x for x in data}


def rep(s, old, new):
    assert old in s, old
    return s.replace(old, new)


# Textbook items: chapter numbers ("Chuyên đề N") are unverifiable (conflict-of-interest topic is 4th but labelled 6) -> drop them.
for x in data:
    x['basis'] = re.sub(r' – Chuyên đề \d+: ', ' – ', x['basis'])

Q['C4-004']['o'][0] = 'Có cơ sở hợp lý, ghi rõ nguồn trích dẫn số liệu và tên người chịu trách nhiệm nội dung'

x = Q['C4-012']
x['o'][3] = 'Tiền gửi kỳ hạn 12 tháng hoặc trái phiếu Chính phủ đáo hạn sau 1 năm'
x['e'] = ('Ràng buộc quan trọng nhất là thời gian ngắn (12 tháng), nhu cầu thanh khoản đúng hạn và không chấp nhận hụt vốn '
          '→ cần tài sản rủi ro thấp, đáo hạn khớp thời điểm cần tiền và nắm giữ đến đáo hạn. Cổ phiếu vốn hóa nhỏ và giao dịch '
          'ký quỹ có rủi ro giá cao; trái phiếu kỳ hạn 10 năm phải bán trước hạn nên chịu rủi ro lãi suất, rủi ro thanh khoản '
          'và rủi ro tín dụng.')

x = Q['C4-015']
x['q'] = ('Khi sàng lọc danh sách khách hàng tiềm năng, nhân viên môi giới nên ưu tiên tiếp cận trước những người '
          'đồng thời đáp ứng các tiêu chí nào sau đây?')
x['o'] = ['Có quan hệ quen biết, có nhiều thời gian rảnh và sẵn lòng nghe giới thiệu',
          'Sống gần chi nhánh, còn trẻ tuổi và thường xuyên sử dụng mạng xã hội',
          'Có người giới thiệu, có học vấn cao và từng tham dự hội thảo đầu tư',
          'Có nhu cầu đầu tư, có khả năng tài chính và có quyền tự quyết định đầu tư']
x['a'] = 3
x['e'] = ('Khách hàng tiềm năng đủ điều kiện (qualified prospect) là người có nhu cầu về sản phẩm, dịch vụ đầu tư, có khả năng '
          'tài chính (nguồn tiền để đầu tư) và có quyền ra quyết định đầu tư. Sàng lọc theo các tiêu chí này giúp nhân viên '
          'môi giới tập trung thời gian vào người có khả năng trở thành khách hàng thực sự; quen biết, địa bàn, độ tuổi, học vấn '
          'hay việc từng dự hội thảo chỉ là yếu tố hỗ trợ tiếp cận.')
x['basis'] = 'Giáo trình Môi giới và tư vấn đầu tư chứng khoán – sàng lọc, đánh giá khách hàng tiềm năng'

x = Q['C4-017']
x['e'] = rep(x['e'], 'nguyên tắc thực hiện lệnh nhanh chóng, chính xác theo thời gian nhận lệnh',
                        'nguyên tắc thực hiện lệnh nhanh chóng, chính xác và ghi nhận đúng thời gian nhận lệnh')

Q['C4-020']['quote'] = ('Công ty chứng khoán phải thông báo kết quả thực hiện lệnh giao dịch cho khách hàng hoặc '
                        'tổ chức kinh doanh chứng khoán nước ngoài đại diện ngay')

x = Q['C4-021']
x['e'] = ('CTCK phải có bộ phận chuyên trách giải quyết thắc mắc, khiếu nại (khoản 6 Điều 14 TT 121/2020), nên phải tiếp nhận, '
          'rà soát hồ sơ tư vấn và phản hồi có căn cứ. Khuyến nghị có cơ sở, đã cảnh báo rủi ro và khách hàng tự quyết định thì '
          'khoản lỗ do biến động giá là rủi ro của khách hàng. Bù lỗ hay cam kết gỡ lỗ là chia sẻ thua lỗ, bảo đảm khách hàng '
          'không bị thua lỗ – bị cấm (điểm b khoản 6 Điều 4 TT 121/2020; khoản 1 Điều 91 Luật Chứng khoán).')
x['basis'] = ('Khoản 6 Điều 14, điểm b khoản 6 Điều 4 Thông tư 121/2020/TT-BTC (VBHN 09/VBHN-BTC/2026); '
              'khoản 1 Điều 91 Luật Chứng khoán 2019')

x = Q['C4-022']
x['e'] = rep(x['e'], '(150/0,85 − 120 ≈ 56,5)', '(150/0,85 − 120 ≈ 56,5, làm tròn lên 57)')

x = Q['C4-025']
x['o'][1] = 'Mua thêm cổ phiếu Y trước khi gửi khuyến nghị vì tin vào nhận định của mình'
x['o'][3] = 'Báo bộ phận tuân thủ và công khai việc sở hữu cổ phiếu Y trong khuyến nghị'
x['e'] = ('Quản lý xung đột lợi ích: nhận diện – báo cáo – công khai – kiểm soát. Bộ phận kiểm soát nội bộ của CTCK giám sát '
          'các hoạt động tiềm ẩn xung đột lợi ích, đặc biệt là giao dịch cá nhân của nhân viên (điểm b khoản 2 Điều 12 TT 121/2020). '
          'Giấu lợi ích, mua thêm trước khi phát hành khuyến nghị để hưởng lợi khi giá tăng hay chuyển cổ phiếu sang tài khoản '
          'người thân đều không loại bỏ xung đột mà còn đặt lợi ích cá nhân lên trên lợi ích của khách hàng.')

Q['C4-026']['o'][1] = 'Ký hợp đồng tư vấn đầu tư chứng khoán cho công ty Q'
Q['C4-027']['o'][0] = 'Bị cấm, vì không được đưa ra lãi suất cụ thể hay chia sẻ lãi, lỗ để lôi kéo khách hàng'
Q['C4-028']['o'][3] = 'Từ chối, vì không được nhận ủy quyền chuyển tiền nội bộ giữa các khách hàng'

x = Q['C4-039']
x['o'][0] = 'Được phép, vì khách hàng M là chủ tài khoản và đã đồng ý cho sử dụng'
x['e'] = rep(x['e'], 
    ' và có thể vi phạm khoản 6 Điều 12 Luật Chứng khoán nếu dẫn tới thao túng giá.',
    '; CTCK chịu trách nhiệm về hoạt động nghiệp vụ của người hành nghề (khoản 4 Điều 98 Luật Chứng khoán), còn việc cho '
    'mượn tài khoản dẫn đến thao túng giá bị nghiêm cấm (khoản 6 Điều 12 Luật Chứng khoán).')
x['basis'] = ('Điểm e khoản 4 Điều 13, điểm b khoản 2 Điều 12 Thông tư 121/2020/TT-BTC (VBHN 09/VBHN-BTC/2026); '
              'khoản 4 Điều 98, khoản 6 Điều 12 Luật Chứng khoán 2019')

Q['C4-040']['o'][3] = 'Vi phạm, vì nêu ý kiến tăng giá không có căn cứ để lôi kéo giao dịch'

json.dump(data, open(D + 'cm_4.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('written', len(data))
