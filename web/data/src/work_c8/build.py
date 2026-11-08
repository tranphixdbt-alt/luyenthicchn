"""Build cm_8.json: câu tự soạn cho các kiến thức có trong 80 câu công khai của onthicchnchungkhoan.pages.dev
mà ngân hàng chưa có. Không chép đề/phương án/lời giải của họ; chỉ kiểm tra lại cùng sự kiện pháp lý/kỹ năng.
Câu tính toán được tính lại và assert ở đây; trích dẫn được đối chiếu nguyên văn bằng hàm của tools/kiem_tra.py.
Chạy: python3 -I build.py"""
import json, re, random, sys, datetime as dt
from collections import Counter
from pathlib import Path

ROOT = Path('/home/user/cchn_moi')
SRC = ROOT / 'web/data/src'
OUT = SRC / 'cm_8.json'
sys.path.insert(0, str(ROOT / 'web/tools'))
import kiem_tra as K  # noqa: E402  (dùng lại doc_text/norm_ws/loose để kiểm trích dẫn đúng như trình kiểm tra)

LAW = 'VBHN_24_VBHN-VPQH_2025_Luat_Chung_khoan_hop_nhat_Cong_bao.txt'
N155 = 'ND_155_2020_ND-CP_Cong_bao_so_45-56_2021.txt'
N245 = 'ND_245_2025_ND-CP_Cong_bao_so_1403-1408_2025.txt'
N156 = 'ND_156_2020_ND-CP_Cong_bao.txt'
N306 = 'ND_306_2025_ND-CP_English_SSC.txt'
T96 = 'TT_96_2020_TT-BTC_Cong_bao.txt'
T98 = 'VBHN_04_VBHN-BTC_2026_TT98_136_hop_nhat.txt'
GT = 'Giáo trình SRTC (khung chương trình)'
LCK = 'Luật Chứng khoán 2019 (VBHN 24/VBHN-VPQH năm 2025, hợp nhất Luật 56/2024/QH15)'


def vn(x, d=0):
    return f"{x:,.{d}f}".replace(',', '#').replace('.', ',').replace('#', '.')


Q = []


def add(part, subj, topic, lv, q, o, e, basis, quote='', src=''):
    """o[0] là đáp án đúng."""
    assert len(o) == 4 and len(set(o)) == 4, o
    if part == 'LUAT':
        assert quote and src, q[:50]
    Q.append(dict(part=part, subject=subj, topic=topic, level=lv, q=q, o=o, e=e, basis=basis, quote=quote, src=src))


def L(*a, **k):
    add('LUAT', 'LU', *a, **k)


# ============================ LUẬT (LU) ============================
L('Thanh tra & xử lý vi phạm', 1,
  'Nhà đầu tư N và công ty chứng khoán K phát sinh tranh chấp tại Việt Nam liên quan đến việc thực hiện hợp đồng giao dịch ký quỹ. Theo Luật Chứng khoán, tranh chấp này được giải quyết thông qua:',
  ['Thương lượng, hòa giải hoặc yêu cầu Trọng tài, Tòa án Việt Nam giải quyết',
   'Hòa giải bắt buộc tại Ủy ban Chứng khoán Nhà nước trước khi khởi kiện',
   'Chỉ Tòa án nhân dân nơi công ty chứng khoán K đặt trụ sở chính',
   'Quyết định giải quyết cuối cùng của Sở giao dịch chứng khoán Việt Nam'],
  'Khoản 1 Điều 133 Luật Chứng khoán: khi có tranh chấp phát sinh trong hoạt động chứng khoán tại Việt Nam, việc giải quyết được thực hiện thông qua thương lượng, hòa giải hoặc yêu cầu Trọng tài hoặc Tòa án Việt Nam theo quy định của pháp luật. Luật không bắt buộc hòa giải tại UBCKNN, không giới hạn ở Tòa án và Sở giao dịch chứng khoán không có thẩm quyền phân xử tranh chấp dân sự giữa nhà đầu tư và công ty chứng khoán.',
  'Khoản 1 Điều 133 ' + LCK,
  'bảo vệ quyền, lợi ích hợp pháp hoặc giải quyết tranh chấp được thực hiện thông qua thương lượng, hòa giải hoặc yêu cầu Trọng tài hoặc Toà án Việt Nam giải quyết theo quy định của pháp luật.', LAW)

L('Chào bán riêng lẻ', 2,
  'Công ty cổ phần Q chưa phải là công ty đại chúng, không phải công ty chứng khoán hay công ty quản lý quỹ, dự kiến chào bán cổ phiếu riêng lẻ cho 20 nhà đầu tư. Theo Luật Chứng khoán, đợt chào bán này thực hiện theo:',
  ['Luật Doanh nghiệp và quy định khác của pháp luật có liên quan',
   'Điều kiện chào bán riêng lẻ của công ty đại chúng trong Luật Chứng khoán',
   'Thủ tục đăng ký chào bán riêng lẻ với Ủy ban Chứng khoán Nhà nước',
   'Quy định về chào bán chứng khoán ra công chúng của Luật Chứng khoán'],
  'Điều 30 Luật Chứng khoán: chào bán chứng khoán riêng lẻ của tổ chức phát hành không phải là công ty đại chúng thực hiện theo Luật Doanh nghiệp và pháp luật liên quan. Điều kiện tại Điều 31 chỉ áp dụng cho công ty đại chúng và công ty chứng khoán, công ty quản lý quỹ (kể cả khi không phải công ty đại chúng). Chào bán cho 20 nhà đầu tư (dưới 100 nhà đầu tư không chuyên nghiệp) không phải chào bán ra công chúng.',
  'Điều 30, Điều 31 ' + LCK,
  'Chào bán chứng khoán riêng lẻ của tổ chức phát hành không phải là công ty đại chúng thực hiện theo quy định của Luật Doanh nghiệp và quy định khác của pháp luật có liên quan.', LAW)

# ngày muộn nhất công bố ngày ĐKCC họp ĐHĐCĐ: 20 ngày trước
dkcc = dt.date(2026, 12, 30)
f = lambda n: (dkcc - dt.timedelta(n)).strftime('%d/%m/%Y')
assert f(20) == '10/12/2026'
L('Công bố thông tin', 3,
  'Công ty đại chúng K dự kiến họp Đại hội đồng cổ đông bất thường; ngày đăng ký cuối cùng để lập danh sách cổ đông có quyền dự họp dự kiến là 30/12/2026. Theo Thông tư 96/2020/TT-BTC, K phải công bố thông tin về ngày đăng ký cuối cùng dự kiến này chậm nhất vào ngày nào? (Tính lùi đủ số ngày dương lịch, không xét ngày nghỉ.)',
  [f(20), f(10), f(21), f(15)],
  f'Điểm b khoản 4 Điều 11 TT 96/2020: công ty đại chúng công bố thông tin về ngày đăng ký cuối cùng dự kiến để cổ đông hiện hữu tham dự họp ĐHĐCĐ tối thiểu 20 ngày trước ngày đăng ký cuối cùng dự kiến: 30/12/2026 − 20 ngày = {f(20)}. Mốc 10 ngày ({f(10)}) áp dụng cho các trường hợp thực hiện quyền khác như trả cổ tức (điểm a); 21 ngày là thời hạn đăng tài liệu họp ĐHĐCĐ thường niên trước ngày khai mạc, không phải mốc tính theo ngày đăng ký cuối cùng.',
  'Điểm b khoản 4 Điều 11 Thông tư 96/2020/TT-BTC (điều này không bị sửa đổi bởi TT 68/2024, TT 18/2025, TT 08/2026)',
  'Công ty đại chúng công bố thông tin về ngày đăng ký cuối cùng dự kiến thực hiện quyền cho cổ đông hiện hữu để tham dự họp Đại hội đồng cổ đông tối thiểu 20 ngày trước ngày đăng ký cuối cùng dự kiến.', T96)

L('Quỹ đầu tư', 2,
  'Quỹ ETF E niêm yết từ tháng 12/2026. Dự thảo Điều lệ quỹ quy định giao dịch hoán đổi chứng chỉ quỹ với thành viên lập quỹ chỉ tổ chức 01 lần mỗi tháng, vào thứ Sáu cuối tháng. Theo Thông tư 98/2020/TT-BTC (sửa đổi bởi Thông tư 136/2025/TT-BTC), nhận định nào đúng?',
  ['Không phù hợp, vì tần suất giao dịch hoán đổi tối thiểu là 02 lần trong 01 tháng',
   'Phù hợp, vì tần suất hoán đổi hoàn toàn do Điều lệ quỹ quyết định',
   'Phù hợp, vì quỹ ETF chỉ cần tổ chức hoán đổi tối thiểu 01 lần mỗi tháng',
   'Không phù hợp, vì quỹ ETF phải tổ chức giao dịch hoán đổi hằng ngày'],
  'Khoản 1 Điều 43 TT 98/2020 (VBHN 04/2026): trong 30 ngày kể từ ngày quỹ niêm yết, công ty quản lý quỹ phải tổ chức giao dịch hoán đổi; giao dịch hoán đổi được tổ chức định kỳ theo Điều lệ quỹ nhưng tần suất tối thiểu 02 lần trong 01 tháng. Điều lệ chỉ được quy định tần suất bằng hoặc dày hơn mức tối thiểu; không có yêu cầu hoán đổi hằng ngày. (Quỹ mở cũng có tần suất giao dịch tối thiểu 02 lần/tháng theo Điều 30.)',
  'Khoản 1 Điều 43 Thông tư 98/2020/TT-BTC (VBHN 04/VBHN-BTC năm 2026, hợp nhất TT 136/2025/TT-BTC)',
  'Hoạt động giao dịch hoán đổi phải được tổ chức định kỳ theo quy định tại Điều lệ quỹ và đã được công bố tại Bản cáo bạch, Bản cáo bạch tóm tắt. Tần suất giao dịch hoán đổi tối thiểu 02 lần trong 01 tháng.', T98)

xn = dt.date(2026, 11, 2)
g = lambda n: (xn + dt.timedelta(n)).strftime('%d/%m/%Y')
assert g(15) == '17/11/2026' and g(30) == '02/12/2026'
L('Công ty đại chúng', 3,
  'Ngày 02/11/2026, UBCKNN xác nhận hoàn tất việc đăng ký công ty đại chúng cho công ty cổ phần V (trở thành công ty đại chúng do đáp ứng điều kiện vốn và cơ cấu cổ đông, chưa qua chào bán lần đầu ra công chúng). Theo Nghị định 155/2020/NĐ-CP, V phải hoàn thành việc đăng ký cổ phiếu tại Tổng công ty lưu ký và bù trừ chứng khoán Việt Nam chậm nhất vào ngày nào? (Thời hạn n ngày kể từ ngày X tính đến hết ngày X + n.)',
  [g(15), g(30), g(7), '02/11/2027'],
  f'Khoản 4 Điều 149 NĐ 155/2020 (NĐ 245/2025 chỉ bổ sung khoản 3a, 3b, 4a, không sửa khoản 4): công ty đại chúng phải đăng ký cổ phiếu tại VSDC trong 15 ngày kể từ ngày UBCKNN xác nhận hoàn tất đăng ký công ty đại chúng → {g(15)}. Mốc 30 ngày ({g(30)}) là thời hạn đăng ký giao dịch cổ phiếu trên hệ thống giao dịch chứng khoán chưa niêm yết (điểm d khoản 1 Điều 34 Luật Chứng khoán); 01 năm là căn cứ hủy tư cách công ty đại chúng nếu không đăng ký tại VSDC (Điều 38 Luật, sửa đổi bởi Luật 56/2024). Khoản 3a (bổ sung bởi NĐ 245): phải hoàn tất đăng ký tại VSDC trước khi đưa chứng khoán vào giao dịch.',
  'Khoản 4 Điều 149 Nghị định 155/2020/NĐ-CP (không bị sửa đổi bởi Nghị định 245/2025/NĐ-CP); điểm d khoản 1 Điều 34 Luật Chứng khoán',
  'Công ty đại chúng phải thực hiện đăng ký cổ phiếu tại Tổng công ty lưu ký và bù trừ chứng khoán Việt Nam trong thời hạn 15 ngày kể từ ngày Ủy ban Chứng khoán Nhà nước xác nhận hoàn tất việc đăng ký công ty đại chúng.', N155)

L('Xử phạt vi phạm', 2,
  'Theo Điều 4 Nghị định 156/2020/NĐ-CP (sửa đổi bởi Nghị định 128/2021/NĐ-CP và Nghị định 306/2025/NĐ-CP), hình thức nào sau đây CHỈ được áp dụng là hình thức xử phạt bổ sung, KHÔNG thuộc các hình thức xử phạt chính trong lĩnh vực chứng khoán?',
  ['Tịch thu tang vật, phương tiện được sử dụng để vi phạm hành chính',
   'Phạt cảnh cáo đối với tổ chức, cá nhân vi phạm hành chính',
   'Đình chỉ giao dịch chứng khoán của nhà đầu tư có thời hạn',
   'Tước quyền sử dụng chứng chỉ hành nghề chứng khoán có thời hạn'],
  'Khoản 1 Điều 4 NĐ 156/2020: hình thức xử phạt chính gồm cảnh cáo; phạt tiền; đình chỉ giao dịch chứng khoán có thời hạn (NĐ 306/2025, hiệu lực 09/01/2026, sửa thành từ 01 đến 24 tháng); tước quyền sử dụng giấy chứng nhận đăng ký hoạt động văn phòng đại diện, chứng chỉ hành nghề chứng khoán có thời hạn. Tịch thu tang vật, phương tiện vi phạm chỉ nằm ở khoản 2 (hình thức bổ sung). Tước quyền sử dụng chứng chỉ hành nghề có thể là hình thức chính hoặc bổ sung.',
  'Điều 4 Nghị định 156/2020/NĐ-CP (điểm c khoản 1, điểm a khoản 2 sửa đổi bởi khoản 2 Điều 1 Nghị định 306/2025/NĐ-CP)',
  'Tịch thu tang vật vi phạm hành chính, phương tiện được sử dụng để vi phạm hành chính trong lĩnh vực chứng khoán.', N156)

L('Chứng chỉ hành nghề chứng khoán', 1,
  'Theo khoản 2 Điều 97 Luật Chứng khoán, nội dung nào sau đây KHÔNG thuộc các điều kiện để cá nhân được cấp chứng chỉ hành nghề chứng khoán?',
  ['Có tối thiểu 02 năm kinh nghiệm làm việc tại công ty chứng khoán',
   'Có trình độ từ đại học trở lên (không giới hạn chuyên ngành)',
   'Có trình độ chuyên môn về chứng khoán theo quy định',
   'Đạt kỳ thi sát hạch phù hợp với loại chứng chỉ đề nghị cấp'],
  'Khoản 2 Điều 97 Luật Chứng khoán: có năng lực hành vi dân sự đầy đủ, không đang bị truy cứu trách nhiệm hình sự hoặc bị cấm hành nghề chứng khoán; có trình độ từ đại học trở lên; có trình độ chuyên môn về chứng khoán; đạt yêu cầu kỳ thi sát hạch phù hợp loại chứng chỉ. Luật không đặt điều kiện số năm kinh nghiệm làm việc.',
  'Khoản 2 Điều 97 ' + LCK,
  'b) Có trình độ từ đại học trở lên; c) Có trình độ chuyên môn về chứng khoán; d) Đạt yêu cầu trong kỳ thi sát hạch cấp chứng chỉ hành nghề chứng khoán phù hợp với loại chứng chỉ hành nghề chứng khoán đề nghị cấp.', LAW)

L('Xử phạt vi phạm', 1,
  'Theo Nghị định 156/2020/NĐ-CP (sửa đổi bởi Nghị định 306/2025/NĐ-CP, hiệu lực 09/01/2026), Chánh Thanh tra Ủy ban Chứng khoán Nhà nước có quyền phạt tiền tối đa đến mức nào?',
  ['2,4 tỷ đồng đối với tổ chức và 1,2 tỷ đồng đối với cá nhân',
   '100 triệu đồng đối với tổ chức và 50 triệu đồng đối với cá nhân',
   '3 tỷ đồng đối với tổ chức và 1,5 tỷ đồng đối với cá nhân',
   '1,5 tỷ đồng đối với tổ chức và 750 triệu đồng đối với cá nhân'],
  'Khoản 1 Điều 47 NĐ 156 (sửa đổi bởi khoản 19 Điều 1 NĐ 306/2025): Giám đốc Sở Tài chính cấp tỉnh, Chánh Thanh tra UBCKNN, trưởng đoàn kiểm tra do Chủ tịch UBCKNN thành lập được phạt tiền tối đa 2,4 tỷ đồng với tổ chức và 1,2 tỷ đồng với cá nhân. Trưởng đoàn thanh tra do Thanh tra UBCKNN thành lập: tối đa 1,5 tỷ / 750 triệu đồng (khoản 1a mới). 3 tỷ / 1,5 tỷ đồng là mức của Chủ tịch UBCKNN đối với các hành vi vi phạm khác; 100 triệu / 50 triệu đồng là mức tại văn bản gốc NĐ 156/2020.',
  'Khoản 1, 1a Điều 47 Nghị định 156/2020/NĐ-CP (sửa đổi, bổ sung bởi khoản 19 Điều 1 Nghị định 306/2025/NĐ-CP; trích bản tiếng Anh của UBCKNN)',
  'Impose a fine up to VND 2.400.000.000 upon a violating organization and up to VND 1.200.000.000 upon a violating individual', N306)

L('Tổ chức & hoạt động CTCK', 2,
  'Công ty cổ phần T sở hữu 15% vốn điều lệ của công ty chứng khoán A. Theo điều kiện về cổ đông của công ty chứng khoán tại Luật Chứng khoán (Thông tư 121/2020/TT-BTC yêu cầu cổ đông tiếp tục tuân thủ), T cùng người có liên quan được sở hữu tối đa bao nhiêu vốn điều lệ của một công ty chứng khoán B khác?',
  ['Không quá 5% vốn điều lệ của B', 'Dưới 10% vốn điều lệ của B',
   'Không quá 15% vốn điều lệ của B', 'Không giới hạn nếu B đã niêm yết'],
  'Điểm c khoản 2 Điều 74 Luật Chứng khoán: cổ đông, thành viên góp vốn sở hữu từ 10% trở lên vốn điều lệ của 01 công ty chứng khoán và người có liên quan không sở hữu trên 5% vốn điều lệ của 01 công ty chứng khoán khác; khoản 1 Điều 6 TT 121/2020 yêu cầu cổ đông công ty chứng khoán phải bảo đảm tuân thủ quy định này. Ngưỡng 5% đối với cổ phiếu niêm yết tại khoản 6 Điều 91 là hạn chế khi chính công ty chứng khoán mua cổ phần của công ty chứng khoán khác.',
  'Điểm c khoản 2 Điều 74 ' + LCK + '; khoản 1 Điều 6 Thông tư 121/2020/TT-BTC (VBHN 09/VBHN-BTC năm 2026)',
  'Cổ đông, thành viên góp vốn sở hữu từ 10% trở lên vốn điều lệ của 01 công ty chứng khoán và người có liên quan của cổ đông, thành viên góp vốn đó (nếu có) không sở hữu trên 5% vốn điều lệ của 01 công ty chứng khoán khác', LAW)

L('Quản trị công ty đại chúng', 2,
  'Bà M không sở hữu cổ phần và chưa từng làm việc tại công ty niêm yết P; em gái ruột của bà M sở hữu 6% cổ phiếu có quyền biểu quyết của P. Bà M được đề cử làm thành viên Hội đồng quản trị độc lập của P. Theo Nghị định 155/2020/NĐ-CP (dẫn chiếu Luật Doanh nghiệp), nhận định nào đúng?',
  ['Không đủ tiêu chuẩn, vì em ruột của bà M là cổ đông lớn của P',
   'Đủ tiêu chuẩn, vì bản thân bà M không sở hữu cổ phần nào của P',
   'Đủ tiêu chuẩn, vì chỉ vợ, chồng, cha, mẹ, con mới bị hạn chế',
   'Đủ tiêu chuẩn nếu được Hội đồng quản trị đương nhiệm giới thiệu'],
  'Khoản 1 Điều 275 NĐ 155/2020: thành viên HĐQT công ty đại chúng phải đáp ứng tiêu chuẩn tại khoản 1, 2 Điều 155 Luật Doanh nghiệp. Điểm c khoản 2 Điều 155 Luật Doanh nghiệp 2020: thành viên độc lập không được là người có vợ, chồng, cha, mẹ (đẻ, nuôi), con (đẻ, nuôi), anh, chị, em ruột là cổ đông lớn của công ty. Sở hữu 6% cổ phiếu có quyền biểu quyết là cổ đông lớn (từ 5% trở lên, khoản 18 Điều 4 Luật Chứng khoán), nên bà M không đủ tiêu chuẩn thành viên độc lập dù bản thân không có cổ phần; việc HĐQT giới thiệu ứng viên không thay đổi tiêu chuẩn.',
  'Khoản 1 Điều 275 Nghị định 155/2020/NĐ-CP; điểm c khoản 2 Điều 155 Luật Doanh nghiệp 2020; khoản 18 Điều 4 Luật Chứng khoán',
  'Thành viên Hội đồng quản trị phải đáp ứng các tiêu chuẩn và điều kiện theo quy định tại khoản 1, khoản 2 Điều 155 Luật Doanh nghiệp và Điều lệ công ty.', N155)

L('Sở hữu nước ngoài', 2,
  'Quỹ đầu tư nước ngoài F muốn trực tiếp mua cổ phiếu niêm yết trên thị trường chứng khoán Việt Nam (không ủy thác vốn cho công ty quản lý quỹ). Theo Nghị định 155/2020/NĐ-CP (sửa đổi bởi Nghị định 245/2025/NĐ-CP), F phải thực hiện thủ tục mã số giao dịch chứng khoán như thế nào?',
  ['Đăng ký tại thành viên lưu ký để thành viên lưu ký đăng ký với VSDC trước khi đầu tư',
   'Nộp hồ sơ đề nghị cấp mã số giao dịch trực tiếp tại Ủy ban Chứng khoán Nhà nước',
   'Không cần mã số giao dịch nếu mở tài khoản tại công ty chứng khoán có môi giới',
   'Đăng ký mã số giao dịch tại Sở giao dịch chứng khoán nơi dự kiến mua cổ phiếu'],
  'Khoản 2 Điều 138 NĐ 155 (sửa đổi bởi khoản 55 Điều 1 NĐ 245/2025): nhà đầu tư nước ngoài trực tiếp đầu tư phải đăng ký mã số giao dịch chứng khoán tại thành viên lưu ký để thành viên lưu ký đăng ký với VSDC trước khi thực hiện hoạt động đầu tư (văn bản gốc quy định đăng ký với VSDC). Nếu đầu tư gián tiếp bằng cách ủy thác vốn cho công ty quản lý quỹ thì nhà đầu tư nước ngoài không phải đăng ký mã số giao dịch; công ty quản lý quỹ nhận ủy thác đăng ký.',
  'Khoản 2 Điều 138 Nghị định 155/2020/NĐ-CP (sửa đổi bởi khoản 55 Điều 1 Nghị định 245/2025/NĐ-CP)',
  'nhà đầu tư nước ngoài phải đăng ký mã số giao dịch chứng khoán tại thành viên lưu ký để thành viên lưu ký thực hiện đăng ký với Tổng công ty lưu ký và bù trừ chứng khoán Việt Nam trước khi thực hiện các hoạt động đầu tư.', N245)

# ============================ CƠ BẢN (CB) ============================
TP_QL = 'Quản lý, giám sát thị trường chứng khoán'
TP_TQ = 'Tổng quan về thị trường chứng khoán'
add('CM', 'CB', TP_QL, 2,
    'Giám đốc công ty TNHH đầu tư M (pháp nhân thương mại) nhận từ người nội bộ của công ty niêm yết N thông tin chưa công bố về việc N sắp trúng một hợp đồng lớn, rồi quyết định dùng vốn của M mua cổ phiếu N trước khi thông tin được công bố, mang lại khoản lợi bất chính rất lớn cho M. Theo Bộ luật Hình sự 2015 (sửa đổi 2017), nhận định nào đúng?',
    ['M có thể bị truy cứu trách nhiệm hình sự về tội sử dụng thông tin nội bộ nếu đủ yếu tố cấu thành',
     'Chỉ cá nhân Giám đốc bị truy cứu trách nhiệm hình sự, còn M chỉ bị xử phạt hành chính',
     'M chỉ có thể bị truy cứu trách nhiệm hình sự về tội thao túng thị trường chứng khoán',
     'M chỉ bị truy cứu trách nhiệm hình sự sau khi người đại diện theo pháp luật đã bị kết án'],
    'Điều 76 Bộ luật Hình sự liệt kê các tội pháp nhân thương mại phải chịu trách nhiệm hình sự, trong đó có các tội về chứng khoán tại Điều 209 (cố ý công bố thông tin sai lệch hoặc che giấu thông tin), Điều 210 (sử dụng thông tin nội bộ để mua bán chứng khoán) và Điều 211 (thao túng thị trường chứng khoán). Hành vi nhân danh, vì lợi ích và theo quyết định của người điều hành pháp nhân đáp ứng điều kiện tại Điều 75; trách nhiệm hình sự của pháp nhân không loại trừ trách nhiệm của cá nhân và không phụ thuộc việc cá nhân bị kết án trước. Điều 132 Luật Chứng khoán: tùy tính chất, mức độ, vi phạm bị xử phạt hành chính hoặc truy cứu trách nhiệm hình sự.',
    'Điều 75, 76, 210 Bộ luật Hình sự 2015 (sửa đổi, bổ sung 2017); Điều 132 Luật Chứng khoán 2019')

add('CM', 'CB', TP_QL, 1,
    'Ngày 05/10/2026, ông T nhận được quyết định xử phạt vi phạm hành chính trong lĩnh vực chứng khoán và không đồng ý với quyết định này. Theo Luật Khiếu nại, nếu không có trở ngại khách quan, thời hiệu để ông T khiếu nại lần đầu là:',
    ['90 ngày kể từ ngày nhận được quyết định', '30 ngày kể từ ngày nhận được quyết định',
     '45 ngày kể từ ngày nhận được quyết định', '60 ngày kể từ ngày nhận được quyết định'],
    'Quyết định xử phạt vi phạm hành chính bị khiếu nại theo pháp luật về khiếu nại (Luật Xử lý vi phạm hành chính). Điều 9 Luật Khiếu nại 2011: thời hiệu khiếu nại là 90 ngày kể từ ngày nhận được hoặc biết được quyết định hành chính; thời gian có trở ngại khách quan (ốm đau, thiên tai…) không tính vào thời hiệu. Các mốc 30, 45, 60 ngày là thời hạn giải quyết khiếu nại, không phải thời hiệu khiếu nại.',
    'Điều 9 Luật Khiếu nại 2011; Luật Xử lý vi phạm hành chính 2012 (quyền khiếu nại quyết định xử phạt)')

# giá tham chiếu UPCoM = bình quân gia quyền giá khớp lệnh liên tục ngày liền trước (giả định quy chế)
trades = [(4000, 24600), (1000, 25100), (5000, 24300)]   # theo thời gian, lệnh cuối 24.300
pt = (20000, 26000)                                      # giao dịch thỏa thuận (không tính)
wavg = sum(q * p for q, p in trades) / sum(q for q, _ in trades)
with_pt = (sum(q * p for q, p in trades) + pt[0] * pt[1]) / (sum(q for q, _ in trades) + pt[0])
simple = round(sum(p for _, p in trades) / 3, -2)
assert wavg == 24500 and with_pt == 25500 and simple == 24700
add('CM', 'CB', 'Thị trường chứng khoán thứ cấp', 3,
    'Giả định quy chế: giá tham chiếu của cổ phiếu đăng ký giao dịch trên UPCoM là bình quân gia quyền của các giá giao dịch thực hiện theo phương thức khớp lệnh liên tục của ngày giao dịch liền trước (không tính giao dịch thỏa thuận; kết quả đã là bội số bước giá). Ngày T, cổ phiếu U có các giao dịch theo thứ tự thời gian: khớp lệnh 4.000 cp giá 24.600 đ; khớp lệnh 1.000 cp giá 25.100 đ; thỏa thuận 20.000 cp giá 26.000 đ; khớp lệnh 5.000 cp giá 24.300 đ. Giá tham chiếu của U ngày T+1 là:',
    ['24.500 đồng', '24.300 đồng', '25.500 đồng', '24.700 đồng'],
    f'Chỉ tính các giao dịch khớp lệnh liên tục: (4.000 × 24.600 + 1.000 × 25.100 + 5.000 × 24.300) / 10.000 = {vn(sum(q * p for q, p in trades))} / 10.000 = {vn(wavg)} đồng. Lấy giá khớp cuối cùng ra 24.300 đồng (cách xác định của HOSE/HNX là giá đóng cửa); gộp cả giao dịch thỏa thuận ra {vn(with_pt)} đồng; lấy bình quân giản đơn ba mức giá ra xấp xỉ {vn(simple)} đồng.',
    'Giả định quy chế nêu trong đề (cách xác định giá tham chiếu cổ phiếu UPCoM theo Quy chế giao dịch của SGDCK trước khi chuyển sang hệ thống giao dịch mới)')

add('CM', 'CB', TP_TQ, 1,
    'Theo giáo trình, trường hợp nào sau đây là luân chuyển vốn qua kênh tài chính GIÁN TIẾP?',
    ['Hộ gia đình gửi tiết kiệm ngân hàng, ngân hàng dùng tiền đó cho doanh nghiệp vay',
     'Nhà đầu tư cá nhân mua cổ phiếu do công ty phát hành trong đợt chào bán lần đầu',
     'Nhà đầu tư cá nhân mua trái phiếu do doanh nghiệp chào bán ra công chúng',
     'Doanh nghiệp bán thương phiếu trực tiếp cho một doanh nghiệp khác để vay vốn'],
    'Kênh tài chính gián tiếp: vốn đi từ người thừa vốn đến người thiếu vốn qua trung gian tài chính (ngân hàng huy động tiền gửi rồi cho vay, người gửi tiền không có quyền đòi trực tiếp đối với doanh nghiệp vay). Kênh trực tiếp: người thiếu vốn phát hành chứng khoán (cổ phiếu, trái phiếu, thương phiếu) bán thẳng cho người có vốn; thị trường chứng khoán, kể cả Sở giao dịch chứng khoán và thị trường sơ cấp, thuộc kênh tài chính trực tiếp.',
    'Giáo trình Cơ bản về chứng khoán (UBCKNN/SRTC) – Thị trường tài chính: kênh dẫn vốn trực tiếp và gián tiếp')

add('CM', 'CB', 'Công ty chứng khoán', 2,
    'Theo quy định hiện hành (tháng 11/2026), việc trích lập quỹ dự trữ bổ sung vốn điều lệ và quỹ dự phòng tài chính, rủi ro nghiệp vụ từ lợi nhuận sau thuế của công ty chứng khoán được thực hiện như thế nào?',
    ['Không còn tỷ lệ bắt buộc; công ty quyết định theo Điều lệ và nghị quyết ĐHĐCĐ',
     'Bắt buộc trích 5% LNST cho mỗi quỹ đến khi số dư mỗi quỹ bằng 10% vốn điều lệ',
     'Bắt buộc trích 10% LNST cho mỗi quỹ đến khi số dư mỗi quỹ bằng 20% vốn điều lệ',
     'Bắt buộc trích theo tỷ lệ do Ủy ban Chứng khoán Nhà nước ấn định từng năm'],
    'Mức trích bắt buộc 5% lợi nhuận sau thuế cho mỗi quỹ đến khi bằng 10% vốn điều lệ thuộc Thông tư 146/2014/TT-BTC; thông tư này đã bị bãi bỏ bởi Thông tư 114/2021/TT-BTC (hiệu lực 01/02/2022). Từ đó việc phân phối lợi nhuận, lập các quỹ thuộc vốn chủ sở hữu do công ty quyết định theo Luật Doanh nghiệp, Điều lệ và nghị quyết Đại hội đồng cổ đông. Phụ lục vốn khả dụng tại Thông tư 102/2025/TT-BTC (sửa TT 91/2020) cũng ghi "Quỹ dự trữ bổ sung vốn điều lệ (nếu có)".',
    'Thông tư 114/2021/TT-BTC bãi bỏ Thông tư 146/2014/TT-BTC; Phụ lục Thông tư 102/2025/TT-BTC sửa đổi Thông tư 91/2020/TT-BTC')

add('CM', 'CB', TP_TQ, 2,
    'Trình tự nào sau đây phản ánh đúng quá trình chuẩn bị và hình thành thị trường chứng khoán tập trung ở Việt Nam?',
    ['Thành lập UBCKNN (1996) → ban hành nghị định về chứng khoán (1998) → TTGDCK TP.HCM vận hành (2000)',
     'TTGDCK TP.HCM vận hành (1996) → thành lập UBCKNN (1998) → ban hành Luật Chứng khoán (2000)',
     'Ban hành Luật Chứng khoán (1996) → thành lập UBCKNN (1998) → TTGDCK TP.HCM vận hành (2000)',
     'TTGDCK Hà Nội vận hành (1998) → thành lập UBCKNN (2000) → ban hành Luật Chứng khoán (2006)'],
    'Việt Nam xây dựng khung pháp lý và cơ quan quản lý trước khi mở thị trường: UBCKNN thành lập theo Nghị định 75/CP ngày 28/11/1996; Nghị định 48/1998/NĐ-CP về chứng khoán và thị trường chứng khoán và quyết định thành lập hai Trung tâm giao dịch chứng khoán năm 1998; Trung tâm GDCK TP.HCM khai trương tháng 7/2000 (phiên giao dịch đầu tiên 28/7/2000); Trung tâm GDCK Hà Nội khai trương năm 2005; Luật Chứng khoán đầu tiên ban hành năm 2006 (hiệu lực 01/01/2007).',
    'Giáo trình Cơ bản về chứng khoán (UBCKNN/SRTC) – Lịch sử hình thành thị trường chứng khoán Việt Nam')

# ============================ PHÁI SINH (PS) ============================
add('CM', 'PS', 'Những vấn đề cơ bản về hợp đồng tương lai', 1,
    'Trên thị trường chứng khoán phái sinh tập trung, các điều khoản như quy mô hợp đồng, tháng đáo hạn, ngày giao dịch cuối cùng và phương thức thanh toán của hợp đồng tương lai được xác định như thế nào?',
    ['Được Sở giao dịch chuẩn hóa trong mẫu hợp đồng; các bên chỉ chọn giá và số hợp đồng',
     'Do bên mua và bên bán tự thỏa thuận cho từng giao dịch, tương tự hợp đồng kỳ hạn',
     'Do công ty chứng khoán thành viên ấn định riêng cho từng khách hàng của mình',
     'Do tổ chức bù trừ trung tâm quyết định sau khi giao dịch được khớp trên hệ thống'],
    'Hợp đồng tương lai là chứng khoán phái sinh niêm yết (khoản 12 Điều 4 Luật Chứng khoán). Để tạo thanh khoản và cho phép bù trừ tập trung, mọi điều khoản (tài sản cơ sở, quy mô, tháng đáo hạn, ngày giao dịch cuối cùng, phương thức thanh toán) được Sở giao dịch chuẩn hóa trong mẫu hợp đồng; nhà đầu tư chỉ quyết định giá đặt lệnh và số lượng hợp đồng. Hợp đồng kỳ hạn giao dịch thỏa thuận nên điều khoản do hai bên tự thỏa thuận.',
    'Giáo trình Chứng khoán phái sinh (UBCKNN/SRTC) – Đặc điểm hợp đồng tương lai: tiêu chuẩn hóa; khoản 12, 13 Điều 4 Luật Chứng khoán')

# ============================ MÔI GIỚI (MG) ============================
TP_XD = 'Xung đột lợi ích và giải quyết xung đột lợi ích trong hoạt động môi giới và tư vấn đầu tư chứng khoán'
TP_MG = 'Tổng quan về môi giới và tư vấn đầu tư chứng khoán'
add('CM', 'MG', TP_XD, 2,
    'Theo giáo trình, để kết luận nhân viên môi giới có hành vi giao dịch quá mức (churning) trên tài khoản của khách hàng, thường phải chứng minh đồng thời những yếu tố nào?',
    ['Môi giới kiểm soát lệnh trên tài khoản; giao dịch dày đặc vượt mục tiêu của khách hàng; động cơ thu phí',
     'Tài khoản bị lỗ; có sử dụng tiền vay ký quỹ; khách hàng đã gửi khiếu nại bằng văn bản cho công ty',
     'Khối lượng lớn trong thời gian dài; khách hàng tự đặt lệnh; mức phí thấp hơn mặt bằng thị trường',
     'Môi giới có chứng chỉ hành nghề; giao dịch cổ phiếu niêm yết; khách hàng là nhà đầu tư chuyên nghiệp'],
    'Giao dịch quá mức (churning) được xác định khi: người môi giới kiểm soát (quyết định) giao dịch trên tài khoản, tần suất và khối lượng giao dịch quá mức so với mục tiêu, khả năng tài chính của khách hàng trong thời gian ngắn, và mục đích chủ yếu là thu phí hoa hồng cho môi giới. Tài khoản lỗ hay có khiếu nại chưa đủ để kết luận; khách hàng tự đặt lệnh thì môi giới không kiểm soát tài khoản.',
    'Giáo trình Môi giới và tư vấn đầu tư chứng khoán (UBCKNN/SRTC) – Xung đột lợi ích: giao dịch quá mức (churning)')

add('CM', 'MG', TP_MG, 1,
    'Trong cơ cấu các bộ phận hỗ trợ (back office) của công ty môi giới chứng khoán theo giáo trình, bộ phận nào theo dõi và thực hiện cho khách hàng các quyền như nhận cổ tức, nhận cổ phiếu thưởng, đăng ký quyền mua cổ phiếu phát hành thêm?',
    ['Bộ phận quản lý thu nhập chứng khoán', 'Bộ phận bảo chứng (giao dịch ký quỹ)',
     'Bộ phận mua và bán chứng khoán', 'Bộ phận phân tích và nghiên cứu'],
    'Giáo trình mô tả các bộ phận nghiệp vụ hỗ trợ của công ty môi giới: bộ phận mua và bán (ghi chép, lên số liệu, xác nhận, hạch toán giao dịch), bộ phận bảo chứng (quản lý tài khoản ký quỹ), bộ phận thủ quỹ, bộ phận quản lý thu nhập chứng khoán (theo dõi, thu và phân bổ cổ tức, lãi, cổ phiếu thưởng, quyền mua cho khách hàng), bộ phận kế toán. Bộ phận phân tích là bộ phận nghiệp vụ hỗ trợ ra quyết định đầu tư, không xử lý quyền của khách hàng.',
    'Giáo trình Môi giới và tư vấn đầu tư chứng khoán (UBCKNN/SRTC) – Tổ chức hoạt động của công ty môi giới')

add('CM', 'MG', TP_MG, 2,
    'Công việc nào sau đây KHÔNG thuộc chức năng của bộ phận mua và bán (purchase and sales) trong công ty môi giới chứng khoán theo giáo trình?',
    ['Theo dõi tỷ lệ ký quỹ, thông báo gọi ký quỹ bổ sung cho khách hàng',
     'Ghi chép các giao dịch đã thực hiện trên tài khoản của khách hàng',
     'Tính toán số tiền thanh toán, phí và thuế của từng giao dịch',
     'Gửi xác nhận giao dịch cho khách hàng và hạch toán ghi sổ'],
    'Bộ phận mua và bán xử lý giao dịch sau khi khớp: ghi chép, lên số liệu (tính tiền, phí, thuế), xác nhận với khách hàng và hạch toán ghi sổ. Theo dõi tỷ lệ ký quỹ và gọi ký quỹ bổ sung là việc của bộ phận bảo chứng (giao dịch ký quỹ).',
    'Giáo trình Môi giới và tư vấn đầu tư chứng khoán (UBCKNN/SRTC) – Tổ chức hoạt động của công ty môi giới')

# ============================ PHÂN TÍCH (PT) ============================
TP_SL = 'Mức sinh lời và rủi ro'
TP_TQP = 'Tổng quan về phân tích và đầu tư'
Ep, sp, rf = 0.14, 0.25, 0.05
U = {A: Ep - 0.5 * A * sp ** 2 for A in (2, 4)}
assert round(U[2], 4) == 0.0775 and round(U[4], 4) == 0.015 and U[2] > rf > U[4]
add('CM', 'PT', TP_SL, 3,
    'Danh mục cổ phiếu P có lợi suất kỳ vọng 14%/năm, độ lệch chuẩn 25%; tín phiếu kho bạc có lãi suất phi rủi ro 5%/năm. Hai nhà đầu tư dùng hàm hữu dụng U = E(r) − 0,5 × A × σ², với hệ số e ngại rủi ro A lần lượt là 2 và 4. Nhận định nào đúng?',
    ['U = 7,75% với A = 2 và 1,50% với A = 4; chỉ người có A = 2 chọn P',
     'U = 7,75% với A = 2 và 1,50% với A = 4; chỉ người có A = 4 chọn P',
     'U = 1,50% với A = 2 và −11,00% với A = 4; cả hai người đều chọn tín phiếu',
     'U = 14,00% với cả A = 2 và A = 4; cả hai người đều chọn P vì 14% > 5%'],
    f'U(A = 2) = 14% − 0,5 × 2 × 0,25² = 14% − 6,25% = {vn(U[2] * 100, 2)}% > 5% nên chọn P; U(A = 4) = 14% − 12,5% = {vn(U[4] * 100, 2)}% < 5% nên chọn tín phiếu (tín phiếu không rủi ro có U = 5%). Hệ số e ngại rủi ro càng cao thì mức bù rủi ro đòi hỏi càng lớn, cùng một danh mục rủi ro trở nên kém hấp dẫn hơn. Quên hệ số 0,5 ra 1,50% và −11,00%; bỏ qua phần trừ rủi ro (chỉ so 14% với 5%) là không xét mức e ngại rủi ro.',
    'Hàm hữu dụng U = E(r) − ½Aσ²; mức độ e ngại rủi ro và mức bù rủi ro yêu cầu')
assert round((Ep - 2 * sp ** 2) * 100, 2) == 1.5 and round((Ep - 4 * sp ** 2) * 100, 2) == -11.0

rs = 0.075
rt = rs / (1 + rs)
assert round(rt * 100, 2) == 6.98 and round(rs / (1 - rs) * 100, 2) == 8.11 and round(rs * (1 - rs) * 100, 2) == 6.94
add('CM', 'PT', TP_TQP, 3,
    'Ngân hàng niêm yết lãi suất tiền gửi kỳ hạn 1 năm là 7,5%/năm, trả lãi cuối kỳ. Để công bằng về giá trị tiền tệ theo thời gian, nếu khách hàng chọn nhận toàn bộ tiền lãi ngay khi gửi tiền thì lãi suất trả trước tương đương là:',
    ['6,98%/năm', '7,50%/năm', '8,11%/năm', '6,94%/năm'],
    f'Gửi 1 đồng, cuối năm nhận 1,075 đồng. Nhận lãi trước với lãi suất d: nhận ngay d, cuối năm nhận 1 đồng gốc. Tương đương khi d = 0,075 / 1,075 = {vn(rt * 100, 2)}%. 8,11% là công thức ngược chiều (đổi lãi trả trước sang trả sau: d/(1 − d)); 6,94% là 7,5% × (1 − 7,5%).',
    'Lãi suất trả trước tương đương: d = r / (1 + r)')

add('CM', 'PT', 'Thị trường hiệu quả và tài chính hành vi', 2,
    'Nhiều nghiên cứu thực nghiệm cho thấy danh mục cổ phiếu có hệ số P/E thấp đạt lợi suất đã điều chỉnh theo rủi ro cao hơn danh mục cổ phiếu P/E cao trong dài hạn. Nếu hiện tượng này tồn tại bền vững, nó mâu thuẫn trực tiếp nhất với:',
    ['Giả thuyết thị trường hiệu quả dạng trung bình (bán mạnh)',
     'Giả thuyết thị trường hiệu quả chỉ ở dạng yếu',
     'Mô hình chiết khấu dòng cổ tức trong định giá',
     'Nguyên lý đa dạng hóa để giảm rủi ro phi hệ thống'],
    'P/E được tính từ giá và lợi nhuận trên báo cáo tài chính đã công bố, tức là thông tin công khai. Nếu chỉ cần lọc cổ phiếu P/E thấp mà vẫn có lợi suất vượt trội sau điều chỉnh rủi ro, thì giá chưa phản ánh hết thông tin công khai – trái với dạng trung bình (bán mạnh). Dạng yếu chỉ nói về thông tin giá, khối lượng quá khứ. Đây là một “hiện tượng bất thường” (anomaly) được giáo trình nêu cùng hiệu ứng quy mô, hiệu ứng tháng Giêng; tài chính hành vi giải thích bằng phản ứng thái quá của nhà đầu tư.',
    'Các hiện tượng bất thường của thị trường (hiệu ứng P/E thấp) và giả thuyết thị trường hiệu quả dạng trung bình')

gov, yx, yy = 3.2, 4.1, 6.0
sx, sy = round((yx - gov) * 100), round((yy - gov) * 100)
assert (sx, sy, sy - sx) == (90, 280, 190)
add('CM', 'PT', 'Phân tích và định giá trái phiếu', 2,
    'Cùng kỳ hạn 5 năm: trái phiếu Chính phủ có lợi suất đáo hạn 3,2%/năm; trái phiếu của doanh nghiệp X (xếp hạng AAA) 4,1%/năm; trái phiếu của doanh nghiệp Y (xếp hạng BBB) 6,0%/năm. Nhận định nào đúng về mức bù rủi ro tín dụng?',
    ['Mức bù của Y là 280 điểm cơ bản, cao hơn của X 190 điểm cơ bản',
     'Mức bù của Y là 190 điểm cơ bản, cao hơn của X 100 điểm cơ bản',
     'Mức bù của X là 410 điểm cơ bản, thấp hơn của Y 190 điểm cơ bản',
     'Mức bù của X và Y bằng nhau vì cùng kỳ hạn với trái phiếu Chính phủ'],
    f'Mức bù rủi ro tín dụng = lợi suất trái phiếu doanh nghiệp − lợi suất trái phiếu Chính phủ cùng kỳ hạn. X: 4,1% − 3,2% = {sx} điểm cơ bản; Y: 6,0% − 3,2% = {sy} điểm cơ bản; chênh lệch {sy - sx} điểm cơ bản. Xếp hạng tín nhiệm thấp hơn (BBB) nghĩa là rủi ro vỡ nợ cao hơn nên nhà đầu tư đòi hỏi mức bù cao hơn. 410 điểm là lấy cả lợi suất của X; 190 điểm cho Y là lấy chênh lệch giữa hai doanh nghiệp.',
    'Mức bù rủi ro tín dụng (credit spread) so với trái phiếu Chính phủ cùng kỳ hạn; xếp hạng tín nhiệm')

for r in (0.03, 0.08, 0.15):
    for n in range(2, 21):
        assert ((1 + r) ** n - 1) / r > n > (1 - (1 + r) ** -n) / r and (1 + r) ** -n < 1
assert 1.08 ** 4 < 4
add('CM', 'PT', TP_TQP, 2,
    'Với lãi suất mỗi kỳ r > 0 và số kỳ n ≥ 2, giá trị nào sau đây trong các bảng hệ số tài chính LUÔN lớn hơn n?',
    ['Hệ số giá trị tương lai của dòng tiền đều 1 đồng mỗi kỳ (FVIFA)',
     'Hệ số giá trị hiện tại của dòng tiền đều 1 đồng mỗi kỳ (PVIFA)',
     'Hệ số giá trị tương lai của khoản tiền 1 đồng (FVIF)',
     'Hệ số giá trị hiện tại của khoản tiền 1 đồng (PVIF)'],
    'FVIFA = [(1 + r)^n − 1]/r = 1 + (1 + r) + … + (1 + r)^(n−1): tổng n số hạng, từ số hạng thứ hai đều lớn hơn 1 nên FVIFA > n. PVIFA = [1 − (1 + r)^−n]/r là tổng n số hạng nhỏ hơn 1 nên PVIFA < n. PVIF = (1 + r)^−n < 1. FVIF = (1 + r)^n có thể nhỏ hơn n, ví dụ r = 8%, n = 4: 1,08⁴ ≈ 1,36 < 4.',
    'Hệ số giá trị tương lai, hiện tại của khoản tiền đơn và dòng tiền đều (FVIF, PVIF, FVIFA, PVIFA)')

add('CM', 'PT', TP_SL, 1,
    'Khoản đầu tư X chắc chắn đem lại lợi suất 7%/năm. Khoản đầu tư Y có lợi suất 7% hoặc 11% với xác suất bằng nhau và không bao giờ bị lỗ. Theo cách hiểu rủi ro trong lý thuyết danh mục hiện đại, nhận định nào đúng?',
    ['Y rủi ro hơn X, vì lợi suất của Y phân tán quanh giá trị kỳ vọng',
     'Y không có rủi ro, vì trong mọi tình huống Y đều mang lại lãi',
     'X rủi ro hơn Y, vì lợi suất kỳ vọng của X thấp hơn của Y',
     'X và Y có rủi ro như nhau, vì cả hai đều không bao giờ lỗ'],
    'Rủi ro là sự không chắc chắn của lợi suất thực tế so với lợi suất kỳ vọng, đo bằng phương sai, độ lệch chuẩn; không chỉ là khả năng thua lỗ. X có độ lệch chuẩn 0. Y có lợi suất kỳ vọng 9% và độ lệch chuẩn 2% (lệch ±2% quanh 9%) nên rủi ro hơn X, dù không bao giờ lỗ. Lợi suất kỳ vọng cao hơn là phần bù cho rủi ro cao hơn, không phải thước đo rủi ro.',
    'Khái niệm rủi ro: mức độ phân tán của lợi suất thực tế so với lợi suất kỳ vọng (phương sai, độ lệch chuẩn)')
assert (0.5 * 7 + 0.5 * 11) == 9 and (0.5 * (7 - 9) ** 2 + 0.5 * (11 - 9) ** 2) ** 0.5 == 2

add('CM', 'PT', TP_SL, 1,
    'Một nhà đầu tư ưa mạo hiểm dự báo thị trường cổ phiếu sắp tăng mạnh và muốn danh mục tăng nhiều nhất theo thị trường. Theo CAPM, nên ưu tiên chứng khoán nào?',
    ['Cổ phiếu có hệ số beta 1,4', 'Cổ phiếu có hệ số beta 1,0',
     'Cổ phiếu có hệ số beta 0,7', 'Trái phiếu Chính phủ (beta ≈ 0)'],
    'Beta đo độ nhạy của lợi suất chứng khoán với lợi suất thị trường. Khi thị trường tăng 10%, cổ phiếu beta 1,4 kỳ vọng tăng khoảng 14%, beta 1,0 khoảng 10%, beta 0,7 khoảng 7%. Cổ phiếu beta > 1 (cổ phiếu “tấn công”) phù hợp nhà đầu tư chấp nhận rủi ro cao; khi thị trường giảm, chúng cũng giảm mạnh hơn. Beta < 1 là cổ phiếu phòng thủ.',
    'Hệ số beta và rủi ro hệ thống; cổ phiếu tấn công, phòng thủ (CAPM)')

add('CM', 'PT', 'Phân tích kỹ thuật', 1,
    'Nhóm dữ liệu nào sau đây là đầu vào chủ yếu của phân tích kỹ thuật và thường ít được nhà phân tích cơ bản dùng khi ước tính giá trị nội tại của cổ phiếu?',
    ['Diễn biến giá và khối lượng giao dịch theo từng phiên trong quá khứ',
     'Báo cáo tài chính và các chỉ tiêu như EPS, ROE của doanh nghiệp',
     'Lãi suất, lạm phát và tốc độ tăng trưởng của nền kinh tế',
     'Vị thế cạnh tranh của doanh nghiệp và năng lực ban điều hành'],
    'Phân tích cơ bản ước tính giá trị nội tại từ yếu tố vĩ mô, ngành và doanh nghiệp (báo cáo tài chính, EPS, ROE, lợi thế cạnh tranh, quản trị). Phân tích kỹ thuật dựa trên dữ liệu thị trường – giá và khối lượng giao dịch quá khứ – với giả định giá phản ánh mọi thông tin và vận động theo xu hướng; nhà phân tích cơ bản ít dùng biểu đồ giá ngắn hạn để định giá.',
    'Phân biệt phân tích cơ bản và phân tích kỹ thuật')

# ============================ kiểm tra & ghi file ============================
n = len(Q)
rnd = random.Random(8)
while True:
    seq = [i % 4 for i in range(n)]
    rnd.shuffle(seq)
    if all(not (seq[i] == seq[i - 1] == seq[i - 2]) for i in range(2, n)):
        break
REF = re.compile(r'(\b[A-Da-d]\s*(và|,|&)\s*[A-Da-d]\b)|tất cả|không (có )?(phương án|đáp án|ý|câu) nào', re.I)
out = []
for k, (x, a) in enumerate(zip(Q, seq), 1):
    if x['quote']:
        assert len(x['quote']) <= 300, (k, len(x['quote']))
        text = K.doc_text(x['src'])
        assert text and (K.norm_ws(x['quote']) in text or K.loose(x['quote']) in K.loose(text)), (k, x['quote'][:60])
    assert not K.LETTER_IN_E.search(x['e']), (k, 'giải thích nhắc tên phương án')
    o = x['o'][1:]
    o.insert(a, x['o'][0])
    for s in o:
        assert not REF.search(s), s
    out.append({'id': f'C8-{k:03d}', 'part': x['part'], 'subject': x['subject'], 'topic': x['topic'], 'level': x['level'],
                'q': x['q'], 'o': o, 'a': a, 'e': x['e'], 'basis': x['basis'], 'quote': x['quote'], 'src': x['src'],
                'as_of': '2026-11'})

# chủ đề phải trùng chủ đề sẵn có của môn đó
bank = json.loads((ROOT / 'web/data/questions.json').read_text(encoding='utf-8'))
topics = {(q['subject'], q['topic']) for q in bank}
for r in out:
    assert (r['subject'], r['topic']) in topics, (r['id'], r['topic'])

# gần trùng với ngân hàng hiện có (q và q + phương án)
words = lambda s: set(re.findall(r'\w+', s.lower()))
old = []
for p in sorted(SRC.glob('*.json')):
    if p.name.startswith(('cm_', 'luat_')) and p.name != OUT.name:
        old += json.loads(p.read_text(encoding='utf-8'))
worst = (0, '', '')
for r in out:
    for y in old + [z for z in out if z['id'] != r['id']]:
        jq = len(words(r['q']) & words(y['q'])) / len(words(r['q']) | words(y['q']))
        a1, a2 = words(r['q'] + ' ' + ' '.join(r['o'])), words(y['q'] + ' ' + ' '.join(y['o']))
        j = max(jq, len(a1 & a2) / len(a1 | a2))
        if j > worst[0]: worst = (j, r['id'], y['id'])
        assert j <= 0.7, (r['id'], y['id'], j)

OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('ghi', OUT, len(out), 'câu')
print('môn', dict(Counter(r['subject'] for r in out)), '| mức độ', dict(sorted(Counter(r['level'] for r in out).items())))
print('đáp án', dict(sorted(Counter(r['a'] for r in out).items())), '| Jaccard lớn nhất %.2f %s~%s' % worst)
for r in out:
    Ls = [len(s) for s in r['o']]
    if max(Ls) > 1.5 * min(Ls) and min(Ls) > 15: print('độ dài lệch', r['id'], Ls)
    if Ls[r['a']] == max(Ls) and max(Ls) - sorted(Ls)[-2] > 10: print('đáp án dài hẳn', r['id'], Ls)
