"""Áp dụng các sửa đổi review lên cm_6.json (chạy một lần trên bản gốc cm_6.orig.json)."""
import json
from pathlib import Path
SRC = Path('/home/user/cchn_moi/web/data/src')
d = json.loads((SRC / 'work_review_c6/cm_6.orig.json').read_text(encoding='utf-8'))
Q = {q['id']: q for q in d}

q = Q['C6-006']
q['q'] = ('Giáo trình chia các chủ thể tham gia thị trường chứng khoán thành: tổ chức phát hành, nhà đầu tư, '
          'tổ chức kinh doanh chứng khoán và các tổ chức có liên quan đến thị trường chứng khoán. '
          'Chủ thể nào sau đây thuộc nhóm các tổ chức có liên quan đến thị trường chứng khoán?')
q['e'] += (' Lưu ý: đây là cách phân nhóm chủ thể của giáo trình, không phải khái niệm “người có liên quan” '
           'tại khoản 46 Điều 4 Luật Chứng khoán (quan hệ sở hữu, kiểm soát, gia đình… giữa các tổ chức, cá nhân).')

q = Q['C6-010']
q['q'] = ('Theo Luật Doanh nghiệp 2020, trừ trường hợp Đại hội đồng cổ đông biểu quyết nghị quyết làm thay đổi bất lợi '
          'quyền của cổ đông ưu đãi, cổ đông sở hữu cổ phần ưu đãi cổ tức KHÔNG có quyền nào sau đây?')
q['basis'] = 'Khoản 2, khoản 3 Điều 117 Luật Doanh nghiệp 2020; Giáo trình Cơ bản về chứng khoán (UBCKNN/SRTC) – Cổ phiếu ưu đãi'

q = Q['C6-014']
q['o'] = ['6,87%/năm', '7,41%/năm', '7,66%/năm', '8,00%/năm']; q['a'] = 3
q['e'] = ('YTM = (100.000 / 79.383)^(1/3) − 1 = 1,2597^(1/3) − 1 ≈ 1,0800 − 1 = 8,00%/năm. '
          '7,41% là lấy 1 − (79.383 / 100.000)^(1/3) (tỷ suất chiết khấu, không phải lợi suất); '
          '6,87% là lãi đơn bình quân (20.617 / 3) chia mệnh giá; 7,66% là công thức gần đúng chia cho giá bình quân 89.691,5 – '
          'các cách này đều không phải lợi suất kép hằng năm.')

q = Q['C6-015']
q['e'] = q['e'].replace('13,2 tỷ là cách tính như cổ phiếu ưu đãi không tích lũy;',
                        '13,2 tỷ là cách tính như cổ phiếu ưu đãi không tích lũy (chỉ trả 1,8 tỷ của năm 2026); '
                        '11,4 tỷ là chỉ trả phần nợ 2024, 2025 mà quên cổ tức ưu đãi năm 2026;')

q = Q['C6-016']
q['o'] = ['18.261 đồng', '20.000 đồng', '21.000 đồng', '23.000 đồng']; q['a'] = 3
q['e'] = ('Giá chuyển đổi ngang giá = giá thị trường trái phiếu / tỷ lệ chuyển đổi = 115.000 / 5 = 23.000 đồng. '
          'Giá trị chuyển đổi hiện tại = 5 × 21.000 = 105.000 đồng < 115.000 đồng, nên giá cổ phiếu phải tăng lên 23.000 đồng '
          'thì chuyển đổi mới hòa vốn. 20.000 đồng là giá chuyển đổi danh nghĩa (mệnh giá / tỷ lệ chuyển đổi); 21.000 đồng là giá '
          'cổ phiếu hiện tại; 18.261 đồng là nhân nhầm giá cổ phiếu với tỷ số mệnh giá/giá trái phiếu (21.000 × 100.000 / 115.000).')

q = Q['C6-022']
q['e'] = q['e'].replace('48.000 là dùng nhầm tỷ lệ 60%.',
                        '48.000 là dùng nhầm tỷ lệ đăng ký vượt (9,6 − 6) / 6 = 60% làm tỷ lệ phân phối; 80.000 là bỏ qua việc phân phối theo tỷ lệ.')

q = Q['C6-023']
q['e'] = q['e'].replace('49,00 tỷ là tính theo giá khởi điểm.',
                        '49,00 tỷ là tính theo giá khởi điểm; 51,00 tỷ là tính toàn bộ 2.000.000 cổ phần theo giá đặt cao nhất 25.500 đồng.')

q = Q['C6-036']
q['o'] = ['Mua cổ phiếu niêm yết của doanh nghiệp khác cho chính công ty',
          'Bán trái phiếu Chính phủ thuộc danh mục đầu tư của công ty',
          'Bán chứng chỉ quỹ ETF trong danh mục đầu tư của công ty',
          'Mua, bán chứng khoán phát sinh do sửa lỗi sau giao dịch']
q['a'] = 3

q = Q['C6-037']
q['q'] = ('Công ty chứng khoán K nắm giữ đúng 10% vốn điều lệ của công ty cổ phần D; D chuẩn bị chào bán cổ phiếu lần đầu '
          'ra công chúng và niêm yết. Theo Thông tư 121/2020/TT-BTC (văn bản hợp nhất năm 2026), K được cung cấp cho D dịch vụ nào sau đây?')
q['o'] = ['Mở tài khoản và môi giới giao dịch chứng khoán cho D',
          'Tư vấn lập hồ sơ chào bán cổ phiếu lần đầu ra công chúng của D',
          'Tư vấn lập hồ sơ đăng ký niêm yết cổ phiếu của D',
          'Tư vấn xác định giá trị doanh nghiệp D trước đợt chào bán']
q['a'] = 0
q['e'] = ('Khoản 2 Điều 25 Thông tư 121/2020/TT-BTC: CTCK không được tư vấn chào bán, tư vấn niêm yết, tư vấn cổ phần hóa, '
          'tư vấn xác định giá trị doanh nghiệp cho công ty mà mình nắm giữ từ 10% trở lên vốn điều lệ – mức đúng 10% đã thuộc diện cấm, '
          'nên ba dịch vụ tư vấn đều bị cấm. Mở tài khoản, môi giới giao dịch cho D không bị hạn chế '
          '(khoản 7 Điều 24 còn cấm tư vấn đầu tư chứng khoán cho công ty này).')
q['basis'] = 'Khoản 2 Điều 25 Thông tư 121/2020/TT-BTC (VBHN 09/VBHN-BTC năm 2026)'

q = Q['C6-039']
q['o'] = ['1.900.000 cổ phiếu', '2.000.000 cổ phiếu', '2.400.000 cổ phiếu', '2.500.000 cổ phiếu']; q['a'] = 0
q['e'] = ('Hạn mức 1 (điểm c khoản 4 Điều 28): không quá 20% số cổ phiếu đang lưu hành của tổ chức niêm yết = 2.400.000 cổ phiếu '
          '→ được mua thêm 2.400.000 − 500.000 = 1.900.000. Hạn mức 2 (điểm e): không quá 15% vốn chủ sở hữu vào một tổ chức = 150 tỷ đồng; '
          'đang đầu tư 500.000 × 60.000 = 30 tỷ → (150 − 30) tỷ / 60.000 = 2.000.000 cổ phiếu. Lấy mức nhỏ hơn: 1.900.000 cổ phiếu. '
          '2.400.000 và 2.500.000 là quên trừ 500.000 cổ phiếu đang nắm giữ ở từng hạn mức; 2.000.000 là chỉ xét hạn mức 15% vốn chủ sở hữu.')

q = Q['C6-040']
q['basis'] = ('Khoản 5, khoản 7 Điều 2 và khoản 1 Điều 11 Thông tư 91/2020/TT-BTC (không bị Thông tư 102/2025/TT-BTC sửa đổi; '
              'Phụ lục V, VI thay thế bởi Thông tư 102/2025/TT-BTC vẫn tính Tổng giá trị rủi ro = 1+2+3 và Tỷ lệ vốn khả dụng = 5/4); '
              'mốc 180% là mục tiêu giả định của đề')
q['e'] += ' (180% cũng là ngưỡng mà dưới đó CTCK phải báo cáo bất thường theo khoản 2 Điều 12 Thông tư 91/2020/TT-BTC.)'

(SRC / 'cm_6.json').write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('applied')
