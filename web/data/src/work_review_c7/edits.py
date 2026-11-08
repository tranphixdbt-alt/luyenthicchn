"""Áp các sửa đổi second-pass vào cm_7.json (giữ id/topic). Chạy một lần: python3 -I edits.py"""
import json
from pathlib import Path
P = Path('/home/user/cchn_moi/web/data/src/cm_7.json')
d = json.loads(P.read_text(encoding='utf-8'))
Q = {q['id']: q for q in d}
TT121 = 'VBHN_09_VBHN-BTC_2026_TT121_68_08_hop_nhat.txt'

# C7-016: bổ sung lý do P không thuộc ngoại lệ ủy thác của CTCK
Q['C7-016']['e'] += ' Công ty chứng khoán cũng chỉ được nhận ủy thác quản lý tài khoản của nhà đầu tư cá nhân theo Điều 19 TT 121/2020; P không phải công ty chứng khoán hay công ty quản lý quỹ.'

# C7-017: trùng nội dung C1-047 (4 nhóm thông tin khách hàng) -> chuyển sang nghĩa vụ bảo mật (khoản 5 Điều 24)
Q['C7-017'].update(
    level=1,
    q='Theo Thông tư 121/2020/TT-BTC, thông tin mà công ty chứng khoán nhận được từ khách hàng trong quá trình cung ứng dịch vụ tư vấn đầu tư được cung cấp cho bên thứ ba trong trường hợp nào?',
    o=['Khi bên thứ ba là đối tác đã ký thỏa thuận bảo mật thông tin với công ty',
       'Khi được khách hàng đồng ý hoặc pháp luật có quy định khác',
       'Khi thông tin được dùng làm số liệu cho báo cáo phân tích của công ty',
       'Khi hợp đồng tư vấn với khách hàng đã chấm dứt từ 12 tháng trở lên'],
    a=1,
    e='Khoản 5 Điều 24 TT 121/2020: công ty chứng khoán phải bảo mật các thông tin nhận được từ người sử dụng dịch vụ tư vấn trong quá trình cung ứng dịch vụ, trừ trường hợp được khách hàng đồng ý hoặc pháp luật có quy định khác (chẳng hạn yêu cầu của cơ quan có thẩm quyền). Thỏa thuận bảo mật với đối tác, mục đích làm báo cáo phân tích hay việc hợp đồng đã chấm dứt đều không phải ngoại lệ; bảo mật thông tin khách hàng cũng là chuẩn mực đạo đức nghề nghiệp cơ bản.',
    basis='Khoản 5 Điều 24 Thông tư 121/2020/TT-BTC (VBHN 09/VBHN-BTC năm 2026)',
    quote='Công ty chứng khoán phải bảo mật các thông tin nhận được từ người sử dụng dịch vụ tư vấn trong quá trình cung ứng dịch vụ tư vấn trừ trường hợp được khách hàng đồng ý hoặc pháp luật có quy định khác.',
    src=TT121)

# C7-021: kịch bản trùng C1-048 (bà H nghỉ hưu, chứng quyền) -> chuyển sang nghĩa vụ cung cấp rủi ro (khoản 4 Điều 24)
Q['C7-021'].update(
    q='Khách hàng Q đã nhiều năm đầu tư cổ phiếu, khẩu vị rủi ro cao, lần đầu muốn mua chứng quyền có bảo đảm. Nhân viên tư vấn chỉ giới thiệu mức lãi có thể đạt được nhờ đòn bẩy, không đề cập việc chứng quyền có thể mất toàn bộ giá trị khi đáo hạn; Q tự đặt lệnh mua. Theo Thông tư 121/2020/TT-BTC, nhận định nào đúng?',
    o=['Không vi phạm, vì sản phẩm phù hợp với kinh nghiệm và khẩu vị rủi ro cao của Q',
       'Không vi phạm, vì Q tự đặt lệnh và tự chịu trách nhiệm về quyết định đầu tư',
       'Chỉ vi phạm nếu chứng quyền Q đã mua đáo hạn ở trạng thái lỗ và Q bị thiệt hại',
       'Vi phạm, vì khách hàng phải được cung cấp đầy đủ cả nội dung và rủi ro của sản phẩm'],
    a=3,
    e='Khoản 4 Điều 24 TT 121/2020: công ty chứng khoán tư vấn đầu tư phải bảo đảm khách hàng đưa ra quyết định đầu tư trên cơ sở được cung cấp thông tin đầy đủ, bao gồm cả nội dung và rủi ro của sản phẩm, dịch vụ. Sản phẩm phù hợp với khẩu vị rủi ro (khoản 6) không miễn nghĩa vụ nêu rủi ro (chứng quyền có thể đáo hạn với giá trị bằng 0); việc khách hàng tự đặt lệnh hay kết quả lãi, lỗ sau đó không làm thay đổi việc tư vấn đã thiếu thông tin rủi ro.',
    basis='Khoản 4 Điều 24 Thông tư 121/2020/TT-BTC (VBHN 09/VBHN-BTC năm 2026)',
    quote='Công ty chứng khoán tư vấn đầu tư cho khách hàng phải đảm bảo rằng khách hàng đưa ra quyết định đầu tư trên cơ sở được cung cấp thông tin đầy đủ bao gồm cả nội dung và rủi ro của sản phẩm, dịch vụ cung cấp.',
    src=TT121)

# C7-023: dẫn đúng nguồn của câu "chứng chỉ môi giới được tư vấn đầu tư"
q = Q['C7-023']
q['e'] = q['e'].replace('Chứng chỉ môi giới cho phép tư vấn đầu tư nhưng phải thực hiện nhân danh công ty; việc nộp thuế không thay đổi bản chất vi phạm.',
                        'Theo điểm a, d khoản 2 Điều 216 NĐ 155/2020, chứng chỉ môi giới cho phép môi giới và tư vấn đầu tư nhưng chỉ có giá trị khi người được cấp làm việc tại công ty và hành nghề nhân danh công ty; việc nộp thuế không thay đổi bản chất vi phạm.')
q['basis'] += '; điểm a, d khoản 2 Điều 216 Nghị định 155/2020/NĐ-CP'

# C7-024: nói rõ D không có thông tin chưa công bố từ Q để đáp án ghép mảnh không còn tranh cãi
Q['C7-024']['q'] = 'Chuyên viên phân tích D tổng hợp báo cáo tài chính đã công bố của công ty niêm yết Q, số liệu xuất khẩu ngành do cơ quan thống kê công bố và quan sát trực tiếp lượng xe tải ra vào nhà máy của Q từ đường công cộng; D không tiếp xúc người nội bộ và không nhận thông tin chưa công bố nào của Q. Từ đó D kết luận doanh thu quý tới của Q sẽ giảm mạnh và đưa ra khuyến nghị bán. Theo Luật Chứng khoán và chuẩn mực đạo đức nghề nghiệp, nhận định nào sau đây đúng?'

# C7-029: loại trừ ngoại lệ điểm e (tổ chức phát hành được yêu cầu VSDC cung cấp thông tin sở hữu)
q = Q['C7-029']
q['q'] = 'Một doanh nghiệp (không phải tổ chức phát hành chứng khoán mà H sở hữu) đề nghị Tổng công ty lưu ký và bù trừ chứng khoán Việt Nam (VSDC) cung cấp bản sao thông tin sở hữu chứng khoán của nhà đầu tư H để phục vụ việc đòi nợ, trong khi H không đồng ý. Theo Luật Chứng khoán, VSDC phải:'
q['e'] = 'Điểm g khoản 2 Điều 55: VSDC có trách nhiệm bảo mật thông tin sở hữu của khách hàng, từ chối phong tỏa, cầm giữ, trích chuyển tài sản, trích lục, sao chép thông tin sở hữu chứng khoán của khách hàng mà không có sự đồng ý của khách hàng, trừ trường hợp theo yêu cầu của cơ quan có thẩm quyền hoặc của kiểm toán viên kiểm toán báo cáo tài chính của VSDC, của thành viên lưu ký. VSDC chỉ cung cấp thông tin sở hữu theo yêu cầu của chính công ty đại chúng, tổ chức phát hành và cơ quan có thẩm quyền (điểm e), không phải của chủ nợ. Thông tin này không phải thông tin công khai, nộp phí không thay thế sự đồng ý của khách hàng; thành viên lưu ký cũng có nghĩa vụ bảo mật tương tự (điểm a khoản 3 Điều 56).'

# C7-030: phương án "ngân hàng thanh toán" có thể gây tranh cãi với nguồn hỗ trợ khác theo thông tư -> thay bằng nhiễu sai rõ
q = Q['C7-030']
assert q['o'][2] == 'Vốn tự có của ngân hàng thanh toán theo hợp đồng ký với VSDC'
q['o'][2] = 'Khoản tạm ứng từ ngân sách nhà nước do Bộ Tài chính cấp cho VSDC'
q['e'] = q['e'].replace('; ngân hàng thanh toán chỉ cung cấp dịch vụ thanh toán tiền.', '; Luật không quy định dùng ngân sách nhà nước để thanh toán thay cho thành viên lưu ký.')

# C7-031: "tổng tiền phải chuyển" có thể hiểu tính cả chiều nhận -> định nghĩa rõ; nhiễu 13 (lỗi trộn) -> 40 (tính cả hai chiều), đáp án không còn là số lớn nhất
q = Q['C7-031']
q['q'] = q['q'].replace('So với thanh toán riêng từng giao dịch, tổng giá trị tiền phải chuyển giảm được nhờ bù trừ là:',
                        'Chỉ tính số tiền do bên phải trả chuyển đi (không tính lại chiều nhận). So với thanh toán riêng từng giao dịch, tổng số tiền phải chuyển giảm được nhờ bù trừ là:')
assert q['o'][2] == '13 tỷ đồng'
q['o'][2] = '40 tỷ đồng'
q['e'] = 'Thanh toán riêng từng giao dịch: bên mua chuyển 10 + 8 + 6 + 3 = 27 tỷ đồng. Vị thế ròng: P phải trả 13 − 6 = 7 tỷ; Q nhận 10 − 8 = 2 tỷ; R nhận 11 − 6 = 5 tỷ. Sau bù trừ chỉ P chuyển 7 tỷ (bằng tổng số Q và R nhận). Giảm được 27 − 7 = 20 tỷ đồng. Lỗi thường gặp: nhầm với số tiền còn phải chuyển (7 tỷ); cộng giá trị tuyệt đối các vị thế ròng (14 tỷ); tính cả chiều nhận tiền dù đề chỉ tính chiều chuyển (54 − 14 = 40 tỷ).'

# C7-034: cá nhân 3% có thể là người có liên quan của người nội bộ (điểm h) -> loại trừ rõ
q = Q['C7-034']
assert q['o'][0] == 'Cá nhân sở hữu 3% cổ phiếu có quyền biểu quyết, không phải người nội bộ'
q['o'][0] = 'Cá nhân sở hữu 3% cổ phiếu có quyền biểu quyết, không là người nội bộ hay người có liên quan'

# C7-036: e diễn giải sai điểm a khoản 1 Điều 6 (thứ tự người thay thế)
Q['C7-036']['e'] = 'Khoản 1 Điều 8 TT 96/2020: chỉ được tạm hoãn vì lý do bất khả kháng như thiên tai, hỏa hoạn, chiến tranh, dịch bệnh; phải báo cáo UBCKNN, Sở giao dịch ngay khi xảy ra sự kiện, đồng thời công bố việc tạm hoãn, và công bố đầy đủ ngay sau khi khắc phục (khoản 2). Lo ngại giá giảm hay hợp đồng chưa ký không phải lý do tạm hoãn. Người đại diện theo pháp luật vắng mặt thì người được ủy quyền công bố thông tin thực hiện; nếu cả hai đều vắng mặt, thành viên giữ chức vụ cao nhất của Ban Điều hành thay thế (điểm a khoản 1 Điều 6).'

# C7-042: basis dẫn hai điều
Q['C7-042']['basis'] = 'Khoản 7 Điều 7, điểm n khoản 1 Điều 11 Thông tư 96/2020/TT-BTC (hai quy định này không bị sửa đổi bởi TT 68/2024, TT 18/2025, TT 08/2026)'

P.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('edited', len(d))
