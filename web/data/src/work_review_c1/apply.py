import json, sys
P='/home/user/cchn_moi/web/data/src/cm_1.json'
d=json.load(open(P,encoding='utf-8'))
q={x['id']:x for x in d}
V09='VBHN_09_VBHN-BTC_2026_TT121_68_08_hop_nhat.txt'

x=q['C1-057']
x.update(level=1,
 q='Trên Sở Giao dịch Chứng khoán TP. Hồ Chí Minh (HOSE), trong ngày giao dịch bình thường (không có sự kiện điều chỉnh giá), giá tham chiếu của cổ phiếu là:',
 o=['Giá mở cửa được xác định trong chính ngày giao dịch đó',
    'Giá đóng cửa của ngày giao dịch gần nhất trước đó',
    'Giá bình quân gia quyền của 05 ngày giao dịch gần nhất',
    'Giá khớp lệnh cao nhất của ngày giao dịch gần nhất'],
 a=1,
 e='Trên HOSE, giá tham chiếu của cổ phiếu trong ngày giao dịch bình thường là giá đóng cửa của ngày giao dịch gần nhất trước đó; các trường hợp đặc biệt (ngày giao dịch không hưởng quyền, ngày giao dịch đầu tiên…) có cách xác định riêng. Giá trần, giá sàn được tính từ giá tham chiếu cộng, trừ biên độ dao động giá.',
 basis='Quy chế giao dịch chứng khoán của Sở giao dịch chứng khoán: xác định giá tham chiếu cổ phiếu niêm yết trên HOSE',
 quote='', src='Giáo trình SRTC (khung chương trình)')

x=q['C1-064']
x.update(level=2,
 q='Bà K gọi điện cho nhân viên môi giới đề nghị đặt lệnh bán cổ phiếu trên tài khoản giao dịch đứng tên chồng là ông L; ông L chưa có văn bản ủy quyền cho bà K. Theo Thông tư 121/2020/TT-BTC, nhân viên môi giới phải:',
 o=['Nhận lệnh vì vợ chồng là người có liên quan theo quy định của Luật Chứng khoán',
    'Nhận lệnh nếu bà K cung cấp đúng số tài khoản và mật khẩu giao dịch của ông L',
    'Từ chối nhận lệnh vì người đặt lệnh không có văn bản ủy quyền của chủ tài khoản',
    'Nhận lệnh trước, yêu cầu bổ sung văn bản ủy quyền trong vòng 05 ngày làm việc'],
 a=2,
 e='Điểm d khoản 4 Điều 13 TT 121/2020: công ty chứng khoán thực hiện nghiệp vụ môi giới không được nhận lệnh giao dịch với người không phải là người đứng tên tài khoản giao dịch mà không có ủy quyền bằng văn bản của người đứng tên tài khoản. Quan hệ vợ chồng, việc biết mật khẩu hay hứa bổ sung giấy tờ sau đều không thay thế được văn bản ủy quyền.',
 basis='Điểm d khoản 4 Điều 13 Thông tư 121/2020/TT-BTC (sửa đổi, bổ sung bởi khoản 2 Điều 9 Thông tư 08/2026/TT-BTC)',
 quote='', src=V09)

q['C1-016']['basis']='Giá trần/giá sàn = Giá tham chiếu × (1 ± biên độ), làm tròn theo bước giá (biên độ, bước giá và quy tắc làm tròn là dữ kiện nêu trong đề)'

q['C1-031']['o']=['Chưa phải công bố vì tỷ lệ sở hữu chỉ thay đổi 0,6%, chưa vượt qua ngưỡng thay đổi 1%',
 'Công bố thông tin tối thiểu 03 ngày làm việc trước ngày dự kiến thực hiện giao dịch mua',
 'Công bố việc trở thành cổ đông lớn trong 05 ngày làm việc kể từ ngày hoàn tất giao dịch',
 'Công bố thông tin trong thời hạn 24 giờ kể từ thời điểm lệnh mua cổ phiếu X được khớp']

q['C1-034']['o']=['Đặt lệnh mua và bán cùng loại chứng khoán trong ngày, không chuyển quyền sở hữu thực sự, để tạo cung cầu giả tạo',
 'Mua cổ phiếu sau khi tham khảo báo cáo phân tích đã được công ty chứng khoán công bố công khai',
 'Bán bớt cổ phiếu đang nắm giữ để cơ cấu lại danh mục đầu tư khi thị trường giảm điểm mạnh',
 'Đặt lệnh ATC mua cổ phiếu theo danh mục chỉ số tham chiếu để cơ cấu danh mục quỹ ETF theo kỳ']

q['C1-036']['o']=['Thao túng thị trường chứng khoán do tạo ra nguồn cung giả tạo đối với cổ phiếu X',
 'Tư vấn cho người khác giao dịch trên cơ sở thông tin nội bộ, thuộc hành vi bị nghiêm cấm',
 'Không vi phạm vì ông B không trực tiếp giao dịch cổ phiếu X trên tài khoản của mình',
 'Chỉ vi phạm nghĩa vụ công bố thông tin giao dịch của người có liên quan của người nội bộ']

q['C1-047']['o']=['Số tài khoản và số dư tiền gửi của khách hàng tại tất cả các ngân hàng thương mại',
 'Danh mục và kết quả đầu tư của khách hàng tại tất cả các công ty chứng khoán khác',
 'Tình hình tài chính, mục tiêu đầu tư, khả năng chấp nhận rủi ro, kinh nghiệm và hiểu biết đầu tư',
 'Thu nhập, tình trạng hôn nhân, quê quán và nghề nghiệp của những người thân trong gia đình']

q['C1-053']['o']=['Chỉ phục vụ 20% khách hàng có tài sản lớn nhất và từ chối phục vụ các khách hàng còn lại',
 'Ưu tiên nguồn lực cho nhóm nhỏ khách hàng tạo phần lớn doanh thu nhưng vẫn phục vụ mọi khách hàng',
 'Dành 80% thời gian tìm kiếm khách hàng mới và ngừng chăm sóc các khách hàng hiện có',
 'Phân bổ thời gian chăm sóc như nhau cho tất cả khách hàng, bất kể mức độ giao dịch của từng người']

q['C1-054']['o']=['Định kỳ rà soát danh mục, cập nhật tình hình tài chính, mục tiêu và khẩu vị rủi ro của khách hàng',
 'Liên tục khuyến nghị khách hàng mua bán để duy trì doanh số phí giao dịch hằng tháng',
 'Gửi tin nhắn dự báo cổ phiếu sắp tăng trần để khách hàng kịp mua trước phiên sau',
 'Chỉ liên hệ lại với khách hàng khi khách hàng có khiếu nại hoặc yêu cầu hỗ trợ']

q['C1-059']['o']=['Không ghi giá cụ thể, được khớp ngay tại mức giá tốt nhất đang có trên sổ lệnh đối ứng',
 'Chỉ được thực hiện tại mức giá đã đặt hoặc tốt hơn; hiệu lực đến hết ngày hoặc đến khi bị hủy',
 'Chỉ được nhập vào hệ thống giao dịch trong phiên khớp lệnh định kỳ xác định giá đóng cửa',
 'Được ưu tiên so khớp trước lệnh ATO trong phiên khớp lệnh định kỳ xác định giá mở cửa']

q['C1-074']['o']=['Ngăn thông tin từ bộ phận bảo lãnh, tư vấn tài chính sang môi giới, tự doanh để hạn chế xung đột lợi ích',
 'Bảo vệ hệ thống giao dịch trực tuyến của công ty khỏi các cuộc tấn công mạng từ bên ngoài',
 'Tách bạch tiền gửi giao dịch của khách hàng với tiền của công ty tại ngân hàng thương mại',
 'Giới hạn số lượng lệnh mà mỗi nhân viên môi giới được phép nhập vào hệ thống trong một ngày']

x=q['C1-048']
old='trái phiếu doanh nghiệp riêng lẻ chỉ dành cho nhà đầu tư chuyên nghiệp và cá nhân chuyên nghiệp cũng chỉ được mua loại có xếp hạng tín nhiệm kèm bảo đảm.'
assert old in x['e']
x['e']=x['e'].replace(old,'trái phiếu doanh nghiệp riêng lẻ chỉ dành cho nhà đầu tư chứng khoán chuyên nghiệp, và cá nhân chuyên nghiệp cũng chỉ được mua loại có xếp hạng tín nhiệm và có tài sản bảo đảm hoặc bảo lãnh thanh toán của tổ chức tín dụng.')

x=q['C1-061']
x['e']='Ptc = (39.000 − 1.500) / (1 + 1/5) = 37.500 / 1,2 = 31.250 đồng. Kiểm tra: người giữ 5 cổ phiếu có 5 × 39.000 = 195.000 đồng trước quyền; sau quyền nhận 7.500 đồng tiền và có 6 cổ phiếu, nên 6 × P = 187.500 → P = 31.250 đồng. Chia trước rồi mới trừ cổ tức tiền (39.000/1,2 − 1.500) cho kết quả sai 31.000 đồng.'

json.dump(d,open(P,'w',encoding='utf-8'),ensure_ascii=False,indent=2)
open(P,'a').write('\n')
print('ok')
