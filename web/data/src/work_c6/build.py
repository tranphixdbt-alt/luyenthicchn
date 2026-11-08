"""Build cm_6.json (40 câu CB). Run: python3 -I build.py
Mọi số liệu tính lại ở đây và assert đáp án; trích dẫn được đối chiếu nguyên văn với văn bản gốc."""
import json, re, unicodedata, collections
from pathlib import Path

D = Path('/home/user/cchn_moi/web/data/src')
DOCS = Path('/home/user/cchn_moi/tai_lieu_phap_ly/van_ban_txt')
OUT = D / 'cm_6.json'
GT = 'Giáo trình Cơ bản về chứng khoán (UBCKNN/SRTC)'
LUAT = 'VBHN_24_VBHN-VPQH_2025_Luat_Chung_khoan_hop_nhat_Cong_bao.txt'
ND155 = 'ND_155_2020_ND-CP_Cong_bao_so_45-56_2021.txt'
ND245 = 'ND_245_2025_ND-CP_Cong_bao_so_1403-1408_2025.txt'
TT121 = 'VBHN_09_VBHN-BTC_2026_TT121_68_08_hop_nhat.txt'
TT91 = 'TT_91_2020_TT-BTC_Cong_bao.txt'
LCK = 'Luật Chứng khoán 2019 (VBHN 24/VBHN-VPQH năm 2025)'
T1 = 'Tổng quan về thị trường chứng khoán'
T2 = 'Các công cụ tài chính trên thị trường chứng khoán'
T3 = 'Thị trường chứng khoán sơ cấp'
T4 = 'Thị trường chứng khoán thứ cấp'
T5 = 'Công ty chứng khoán'


def vn(x, d=0):
    return f"{x:,.{d}f}".replace(',', '#').replace('.', ',').replace('#', '.')


Q = []
NUM = {}  # id -> giá trị đúng (để kiểm)


def add(topic, lv, q, o, e, basis, quote='', src='', pos=None, key=None, val=None):
    """o[0] là đáp án đúng. Câu số: key = giá trị số của 4 phương án (sắp tăng dần để thứ hạng đáp án thay đổi tự nhiên).
    Câu chữ: pos = vị trí đặt đáp án."""
    assert len(o) == 4 and len(set(o)) == 4, o
    if key is not None:
        assert len(set(key)) == 4 and key[0] == val
        order = sorted(range(4), key=lambda i: key[i])
        opts = [o[i] for i in order]
        a = order.index(0)
    else:
        opts = o[1:]; opts.insert(pos, o[0]); a = pos
    Q.append(dict(topic=topic, level=lv, q=q, o=opts, a=a, e=e, basis=basis, quote=quote, src=src))
    if val is not None:
        NUM[len(Q)] = (val, o[0])


# ======================= 1. Tổng quan =======================
add(T1, 1, 'Theo Luật Chứng khoán, “thị trường giao dịch chứng khoán” được hiểu là:',
    ['Địa điểm hoặc hình thức trao đổi thông tin để tập hợp lệnh mua, bán và giao dịch chứng khoán',
     'Hệ thống giao dịch cho chứng khoán niêm yết do Ủy ban Chứng khoán Nhà nước trực tiếp vận hành',
     'Nơi tổ chức phát hành chào bán chứng khoán lần đầu để huy động vốn từ các nhà đầu tư',
     'Mạng lưới các công ty chứng khoán thực hiện nghiệp vụ môi giới và tự doanh chứng khoán'],
    'Khoản 27 Điều 4 Luật Chứng khoán: thị trường giao dịch chứng khoán là địa điểm hoặc hình thức trao đổi thông tin để tập hợp lệnh mua, bán và giao dịch chứng khoán. Hệ thống giao dịch do Sở giao dịch chứng khoán Việt Nam và công ty con vận hành (không phải UBCKNN); nơi chào bán lần đầu là thị trường sơ cấp.',
    'Khoản 27 Điều 4 ' + LCK,
    'Thị trường giao dịch chứng khoán là địa điểm hoặc hình thức trao đổi thông tin để tập hợp lệnh mua, bán và giao dịch chứng khoán.', LUAT, pos=0)

add(T1, 1, 'Theo Luật Chứng khoán, tổ chức nào được phép tổ chức và vận hành thị trường giao dịch chứng khoán tại Việt Nam?',
    ['Chỉ Sở giao dịch chứng khoán Việt Nam và công ty con',
     'Ủy ban Chứng khoán Nhà nước và Sở giao dịch chứng khoán Việt Nam',
     'Sở giao dịch chứng khoán Việt Nam và các công ty chứng khoán thành viên',
     'Tổng công ty Lưu ký và Bù trừ chứng khoán Việt Nam'],
    'Khoản 2 Điều 42: ngoài Sở giao dịch chứng khoán Việt Nam và công ty con, không tổ chức, cá nhân nào được tổ chức và vận hành thị trường giao dịch chứng khoán. UBCKNN quản lý, giám sát; VSDC đăng ký, lưu ký, bù trừ, thanh toán; công ty chứng khoán chỉ là thành viên giao dịch.',
    'Khoản 2 Điều 42 ' + LCK,
    'Ngoài Sở giao dịch chứng khoán Việt Nam và công ty con, không tổ chức, cá nhân nào được phép tổ chức và vận hành thị trường giao dịch chứng khoán.', LUAT, pos=1)

add(T1, 1, 'Theo Luật Chứng khoán, chính sách khuyến khích tổ chức, cá nhân trong nước, nước ngoài tham gia đầu tư và hoạt động trên thị trường chứng khoán nhằm mục tiêu nào?',
    ['Huy động các nguồn vốn trung hạn và dài hạn cho đầu tư phát triển',
     'Huy động vốn ngắn hạn để bù đắp thiếu hụt thanh khoản của ngân hàng',
     'Ổn định tỷ giá và kiểm soát lạm phát thông qua mua bán chứng khoán',
     'Thay thế hoàn toàn kênh tín dụng ngân hàng trong tài trợ doanh nghiệp'],
    'Khoản 1 Điều 6 Luật Chứng khoán: Nhà nước khuyến khích, tạo điều kiện để tổ chức, cá nhân trong nước, nước ngoài tham gia thị trường chứng khoán nhằm huy động các nguồn vốn trung hạn và dài hạn cho đầu tư phát triển. Vốn ngắn hạn và điều hành tỷ giá, lạm phát thuộc thị trường tiền tệ và chính sách tiền tệ.',
    'Khoản 1 Điều 6 ' + LCK,
    'Nhà nước có chính sách khuyến khích, tạo điều kiện thuận lợi để tổ chức, cá nhân trong nước, nước ngoài tham gia đầu tư và hoạt động trên thị trường chứng khoán nhằm huy động các nguồn vốn trung hạn và dài hạn cho đầu tư phát triển.', LUAT, pos=2)

add(T1, 1, 'Theo Luật Chứng khoán, hoạt động về chứng khoán và thị trường chứng khoán bao gồm các hoạt động sau, NGOẠI TRỪ:',
    ['Nhận tiền gửi tiết kiệm và cấp tín dụng tiêu dùng cho cá nhân',
     'Chào bán, niêm yết, giao dịch và đầu tư chứng khoán',
     'Cung cấp dịch vụ về chứng khoán và công bố thông tin',
     'Kinh doanh chứng khoán và quản trị công ty đại chúng'],
    'Khoản 14 Điều 4 Luật Chứng khoán liệt kê: chào bán, niêm yết, giao dịch, kinh doanh, đầu tư chứng khoán, cung cấp dịch vụ về chứng khoán, công bố thông tin, quản trị công ty đại chúng và hoạt động khác theo Luật. Nhận tiền gửi, cấp tín dụng là hoạt động ngân hàng.',
    'Khoản 14 Điều 4 ' + LCK,
    'Hoạt động về chứng khoán và thị trường chứng khoán bao gồm hoạt động chào bán, niêm yết, giao dịch, kinh doanh, đầu tư chứng khoán, cung cấp dịch vụ về chứng khoán, công bố thông tin, quản trị công ty đại chúng và các hoạt động khác được quy định tại Luật này.', LUAT, pos=3)

add(T1, 2, 'Theo cách phân chia thị trường tài chính dựa vào thời hạn luân chuyển vốn, công cụ nào sau đây thuộc thị trường tiền tệ?',
    ['Tín phiếu Kho bạc kỳ hạn 91 ngày',
     'Trái phiếu Chính phủ kỳ hạn 10 năm',
     'Cổ phiếu phổ thông niêm yết trên HOSE',
     'Chứng chỉ quỹ đóng đang niêm yết'],
    'Thị trường tiền tệ giao dịch công cụ nợ ngắn hạn (thường dưới 1 năm) như tín phiếu kho bạc, thương phiếu, chứng chỉ tiền gửi ngắn hạn. Thị trường vốn, trong đó có thị trường chứng khoán, giao dịch công cụ trung và dài hạn: cổ phiếu, trái phiếu trung, dài hạn, chứng chỉ quỹ.',
    GT + ' – Vị trí của thị trường chứng khoán trong thị trường tài chính (thị trường tiền tệ và thị trường vốn)', pos=1)

add(T1, 2, 'Giáo trình chia các chủ thể tham gia thị trường chứng khoán thành: tổ chức phát hành, nhà đầu tư, tổ chức kinh doanh chứng khoán và tổ chức có liên quan. Chủ thể nào sau đây thuộc nhóm tổ chức có liên quan?',
    ['Tổng công ty Lưu ký và Bù trừ chứng khoán Việt Nam',
     'Công ty chứng khoán thực hiện môi giới và tự doanh',
     'Công ty quản lý quỹ đầu tư chứng khoán',
     'Doanh nghiệp phát hành trái phiếu ra công chúng'],
    'Tổ chức có liên quan gồm cơ quan quản lý nhà nước (UBCKNN), Sở giao dịch chứng khoán, tổ chức lưu ký và bù trừ, thanh toán (VSDC), hiệp hội nghề nghiệp, tổ chức xếp hạng tín nhiệm… Công ty chứng khoán, công ty quản lý quỹ là tổ chức kinh doanh chứng khoán; doanh nghiệp phát hành trái phiếu là tổ chức phát hành.',
    GT + ' – Các chủ thể tham gia thị trường chứng khoán', pos=0)

add(T1, 2, 'Tại Sở giao dịch chứng khoán, nhà đầu tư không trực tiếp mua bán với nhau mà phải đặt lệnh thông qua công ty chứng khoán thành viên. Đặc điểm này thể hiện nguyên tắc hoạt động nào của thị trường chứng khoán?',
    ['Nguyên tắc trung gian', 'Nguyên tắc công khai', 'Nguyên tắc đấu giá', 'Nguyên tắc tự chịu rủi ro'],
    'Giáo trình nêu các nguyên tắc hoạt động cơ bản của thị trường chứng khoán: công khai, trung gian, đấu giá. Nguyên tắc trung gian: giao dịch được thực hiện qua các trung gian là công ty chứng khoán thành viên. Nguyên tắc đấu giá nói về cách hình thành giá qua cạnh tranh giữa các lệnh; nguyên tắc công khai nói về thông tin.',
    GT + ' – Nguyên tắc hoạt động của thị trường chứng khoán (công khai, trung gian, đấu giá)', pos=3)

add(T1, 2, 'Giao dịch nào sau đây làm tăng nguồn vốn của chính công ty cổ phần X (tổ chức phát hành)?',
    ['X phát hành thêm cổ phiếu cho cổ đông hiện hữu thực hiện quyền mua',
     'Quỹ đầu tư mua cổ phiếu X qua hệ thống khớp lệnh của Sở giao dịch',
     'Cổ đông lớn của X bán thỏa thuận cổ phiếu X cho nhà đầu tư chiến lược',
     'Công ty chứng khoán tự doanh mua trái phiếu X đang niêm yết'],
    'Chỉ giao dịch trên thị trường sơ cấp (X phát hành chứng khoán mới) mới đem lại vốn cho X. Ba giao dịch còn lại diễn ra trên thị trường thứ cấp giữa các nhà đầu tư: tiền chuyển từ người mua sang người bán, không chảy vào X.',
    GT + ' – Phân loại thị trường theo quá trình luân chuyển vốn: thị trường sơ cấp và thứ cấp', pos=0)

# ======================= 2. Công cụ =======================
add(T2, 1, 'Theo Luật Chứng khoán, loại chứng khoán do công ty cổ phần phát hành nhằm mang lại cho cổ đông hiện hữu quyền được mua cổ phần mới theo điều kiện đã được xác định là:',
    ['Quyền mua cổ phần', 'Chứng quyền có bảo đảm', 'Chứng chỉ lưu ký', 'Cổ phiếu ưu đãi hoàn lại'],
    'Khoản 7 Điều 4 Luật Chứng khoán định nghĩa quyền mua cổ phần. Chứng quyền có bảo đảm do công ty chứng khoán phát hành; chứng chỉ lưu ký phát hành trên cơ sở chứng khoán của tổ chức Việt Nam; cổ phiếu ưu đãi hoàn lại là một loại cổ phần.',
    'Khoản 7 Điều 4 ' + LCK,
    'Quyền mua cổ phần là loại chứng khoán do công ty cổ phần phát hành nhằm mang lại cho cổ đông hiện hữu quyền được mua cổ phần mới theo điều kiện đã được xác định.', LUAT, pos=1)

add(T2, 1, 'Theo giáo trình và Luật Doanh nghiệp, cổ đông sở hữu cổ phần ưu đãi cổ tức thông thường KHÔNG có quyền nào sau đây?',
    ['Biểu quyết, dự họp Đại hội đồng cổ đông, đề cử người vào Hội đồng quản trị',
     'Nhận cổ tức theo mức ưu đãi đã được xác định trong điều kiện phát hành',
     'Nhận lại phần tài sản còn lại tương ứng khi công ty giải thể, phá sản',
     'Chuyển nhượng cổ phần ưu đãi cổ tức đang sở hữu cho người khác'],
    'Cổ phần ưu đãi cổ tức được trả cổ tức ở mức cao hơn hoặc ổn định hằng năm, được nhận lại tài sản còn lại khi giải thể, phá sản và được chuyển nhượng; đổi lại, cổ đông ưu đãi cổ tức không có quyền biểu quyết, dự họp Đại hội đồng cổ đông, đề cử người vào Hội đồng quản trị, Ban kiểm soát (trừ trường hợp nghị quyết làm thay đổi bất lợi quyền của họ).',
    GT + ' – Cổ phiếu ưu đãi; Điều 117 Luật Doanh nghiệp 2020', pos=3)

add(T2, 2, 'Theo Luật Chứng khoán, điểm khác biệt của chứng quyền (không phải chứng quyền có bảo đảm) so với chứng quyền có bảo đảm là chứng quyền:',
    ['Được phát hành cùng với trái phiếu hoặc cổ phiếu ưu đãi, cho quyền mua cổ phiếu phổ thông',
     'Do công ty chứng khoán phát hành và có tài sản bảo đảm cho nghĩa vụ thanh toán',
     'Cho phép người sở hữu nhận khoản chênh lệch giữa giá thực hiện và giá chứng khoán cơ sở',
     'Chỉ được phát hành riêng lẻ cho cổ đông hiện hữu theo tỷ lệ sở hữu cổ phần'],
    'Khoản 5 Điều 4: chứng quyền được phát hành cùng với trái phiếu hoặc cổ phiếu ưu đãi, cho người sở hữu quyền mua một số cổ phiếu phổ thông theo giá xác định trước trong thời gian xác định. Khoản 6 Điều 4: chứng quyền có bảo đảm do công ty chứng khoán phát hành, có tài sản bảo đảm, có thể là quyền mua, quyền bán hoặc nhận tiền chênh lệch.',
    'Khoản 5, khoản 6 Điều 4 ' + LCK,
    'Chứng quyền là loại chứng khoán được phát hành cùng với việc phát hành trái phiếu hoặc cổ phiếu ưu đãi, cho phép người sở hữu chứng quyền được quyền mua một số cổ phiếu phổ thông nhất định theo mức giá đã được xác định trước trong khoảng thời gian xác định.', LUAT, pos=3)

add(T2, 2, 'Nhà đầu tư nắm giữ chứng chỉ quỹ mở F do công ty quản lý quỹ M quản lý. Theo Luật Chứng khoán, chứng chỉ quỹ này xác nhận:',
    ['Quyền sở hữu của nhà đầu tư đối với một phần vốn góp của quỹ F',
     'Quyền sở hữu của nhà đầu tư đối với một phần vốn cổ phần của công ty M',
     'Quyền chủ nợ của nhà đầu tư đối với một phần nợ của quỹ F',
     'Quyền kiểm soát hằng ngày của nhà đầu tư đối với quyết định đầu tư của F'],
    'Khoản 4 Điều 4: chứng chỉ quỹ xác nhận quyền sở hữu của nhà đầu tư đối với một phần vốn góp của quỹ đầu tư chứng khoán – không phải cổ phần của công ty quản lý quỹ, cũng không phải trái quyền. Khoản 37 Điều 4 nêu rõ nhà đầu tư không có quyền kiểm soát hằng ngày đối với việc ra quyết định đầu tư của quỹ.',
    'Khoản 4, khoản 37 Điều 4 ' + LCK,
    'Chứng chỉ quỹ là loại chứng khoán xác nhận quyền sở hữu của nhà đầu tư đối với một phần vốn góp của quỹ đầu tư chứng khoán.', LUAT, pos=0)

add(T2, 2, 'Nhà đầu tư A mua của B một hợp đồng quyền chọn mua cổ phiếu X với giá thực hiện 50.000 đồng. Đến ngày đáo hạn, giá thị trường của X là 45.000 đồng. Theo Luật Chứng khoán và bản chất của hợp đồng quyền chọn, nhận định nào sau đây đúng?',
    ['A có quyền không thực hiện; nếu A yêu cầu thực hiện thì B có nghĩa vụ đáp ứng',
     'A bắt buộc phải mua X ở giá 50.000 đồng vì đã ký hợp đồng với B',
     'B có quyền yêu cầu A mua X ở giá 50.000 đồng để bù phần chênh lệch',
     'Hợp đồng tự động được thanh toán bù trừ theo giá thị trường 45.000 đồng'],
    'Khoản 11 Điều 4: hợp đồng quyền chọn xác nhận quyền của người mua và nghĩa vụ của người bán. Giá X (45.000) thấp hơn giá thực hiện (50.000) nên quyền chọn mua không có lợi; A (người mua quyền) có thể không thực hiện và chỉ mất phí quyền chọn; B (người bán quyền) chỉ có nghĩa vụ khi A thực hiện quyền.',
    'Khoản 11 Điều 4 ' + LCK,
    'Hợp đồng quyền chọn là loại chứng khoán phái sinh, xác nhận quyền của người mua và nghĩa vụ của người bán để thực hiện một trong các giao dịch sau đây:', LUAT, pos=0)

# L3 – trái phiếu chiết khấu
P0, F, n = 79_383, 100_000, 3
ytm = (F / P0) ** (1 / n) - 1
simple_p = (F - P0) / P0 / n
simple_f = (F - P0) / F / n
approx = (F - P0) / n / ((F + P0) / 2)
assert abs(ytm - 0.08) < 5e-5
vals = [ytm, simple_p, simple_f, approx]
add(T2, 3, 'Trái phiếu chiết khấu (không trả lãi định kỳ), mệnh giá 100.000 đồng, còn đúng 3 năm đến ngày đáo hạn, đang được giao dịch với giá 79.383 đồng. Lợi suất đáo hạn của trái phiếu (lãi kép hằng năm) xấp xỉ:',
    [vn(v * 100, 2) + '%/năm' for v in vals],
    f'YTM = (100.000 / 79.383)^(1/3) − 1 ≈ {vn(ytm*100,2)}%/năm. {vn(simple_p*100,2)}% là lãi đơn bình quân chia cho giá mua, {vn(simple_f*100,2)}% là lãi đơn chia cho mệnh giá, {vn(approx*100,2)}% là công thức gần đúng dùng giá bình quân – các cách này bỏ qua lãi kép.',
    GT + ' – Trái phiếu chiết khấu (zero-coupon) và lợi suất đáo hạn', key=[round(v, 6) for v in vals], val=round(ytm, 6))

# L3 – cổ phiếu ưu đãi tích lũy
n_pref, par, rate, pool = 2_000_000, 10_000, 0.09, 15e9
div_y = n_pref * par * rate
assert div_y == 1.8e9
key_rem = pool - 3 * div_y
vals = [key_rem, pool - div_y, pool - 2 * div_y, 3 * div_y]
assert key_rem == 9.6e9
add(T2, 3, 'Công ty cổ phần Q có 2.000.000 cổ phiếu ưu đãi cổ tức loại tích lũy (cổ tức ưu đãi chưa trả được cộng dồn sang các năm sau), mệnh giá 10.000 đồng, cổ tức ưu đãi 9%/năm tính trên mệnh giá. Q không trả cổ tức ưu đãi trong các năm 2024 và 2025. Năm 2026, Q dành 15 tỷ đồng để chia cổ tức. Số tiền tối đa còn lại để chia cho cổ đông phổ thông năm 2026 là:',
    [vn(v / 1e9, 1) + ' tỷ đồng' for v in vals],
    'Cổ tức ưu đãi mỗi năm = 2.000.000 × 10.000 × 9% = 1,8 tỷ đồng. Cổ phiếu ưu đãi tích lũy phải được trả đủ phần nợ 2024, 2025 và năm 2026 trước cổ đông phổ thông: 3 × 1,8 = 5,4 tỷ đồng. Còn lại cho cổ đông phổ thông: 15 − 5,4 = 9,6 tỷ đồng. 13,2 tỷ là cách tính như cổ phiếu ưu đãi không tích lũy; 5,4 tỷ là phần trả cho cổ đông ưu đãi.',
    GT + ' – Cổ phiếu ưu đãi cổ tức tích lũy và không tích lũy', key=vals, val=key_rem)

# L3 – giá chuyển đổi ngang giá
bond_px, ratio, stock_px = 115_000, 5, 21_000
parity = bond_px / ratio
assert parity == 23_000
vals = [parity, 100_000 / ratio, stock_px, stock_px * bond_px / 100_000]
add(T2, 3, 'Trái phiếu chuyển đổi mệnh giá 100.000 đồng, mỗi trái phiếu được chuyển đổi thành 5 cổ phiếu phổ thông. Giá thị trường hiện tại của trái phiếu là 115.000 đồng, của cổ phiếu là 21.000 đồng. Giá chuyển đổi ngang giá (mức giá cổ phiếu mà tại đó giá trị chuyển đổi bằng giá thị trường của trái phiếu) là:',
    [vn(v) + ' đồng' for v in vals],
    'Giá chuyển đổi ngang giá = giá thị trường trái phiếu / tỷ lệ chuyển đổi = 115.000 / 5 = 23.000 đồng. 20.000 đồng là giá chuyển đổi danh nghĩa (mệnh giá / tỷ lệ chuyển đổi). Giá trị chuyển đổi hiện tại = 5 × 21.000 = 105.000 đồng < 115.000 đồng, nên giá cổ phiếu phải tăng lên 23.000 đồng thì chuyển đổi mới hòa vốn.',
    GT + ' – Trái phiếu chuyển đổi: tỷ lệ chuyển đổi, giá trị chuyển đổi, giá chuyển đổi ngang giá', key=vals, val=parity)

# ======================= 3. Sơ cấp =======================
add(T3, 1, 'Khi công ty cổ phần chào bán cổ phiếu ra công chúng tại Việt Nam, mệnh giá mỗi cổ phiếu theo Luật Chứng khoán là:',
    ['10 nghìn đồng', '1 nghìn đồng', '100 nghìn đồng', '20 nghìn đồng'],
    'Khoản 2 Điều 13 Luật Chứng khoán: mệnh giá cổ phiếu, chứng chỉ quỹ chào bán ra công chúng là 10 nghìn đồng; mệnh giá trái phiếu chào bán ra công chúng là 100 nghìn đồng và bội số của 100 nghìn đồng.',
    'Khoản 2 Điều 13 ' + LCK,
    'Mệnh giá cổ phiếu, chứng chỉ quỹ chào bán ra công chúng là 10 nghìn đồng.', LUAT, pos=2)

add(T3, 1, 'Theo Luật Chứng khoán, tổ chức phát hành, tổ chức bảo lãnh phát hành hoặc tổ chức đại lý phải chuyển giao chứng khoán hoặc giấy chứng nhận quyền sở hữu chứng khoán cho người mua trong thời hạn bao lâu kể từ ngày kết thúc đợt chào bán ra công chúng?',
    ['30 ngày', '10 ngày', '45 ngày', '90 ngày'],
    'Khoản 6 Điều 26 Luật Chứng khoán quy định thời hạn 30 ngày kể từ ngày kết thúc đợt chào bán. 10 ngày là thời hạn báo cáo kết quả đợt chào bán cho UBCKNN (khoản 5); 90 ngày là thời hạn hoàn thành phân phối kể từ ngày Giấy chứng nhận đăng ký chào bán có hiệu lực (khoản 4).',
    'Khoản 6 Điều 26 ' + LCK,
    'Tổ chức phát hành, tổ chức bảo lãnh phát hành hoặc tổ chức đại lý phải chuyển giao chứng khoán hoặc giấy chứng nhận quyền sở hữu chứng khoán cho người mua trong thời hạn 30 ngày kể từ ngày kết thúc đợt chào bán.', LUAT, pos=3)

add(T3, 2, 'Công ty cổ phần M (chưa là công ty đại chúng) không phát hành thêm cổ phiếu; các cổ đông hiện hữu của M chào bán một phần cổ phiếu đang sở hữu ra công chúng lần đầu để M trở thành công ty đại chúng. Theo Nghị định 155/2020/NĐ-CP, đây là hình thức:',
    ['Chào bán lần đầu ra công chúng thông qua thay đổi cơ cấu sở hữu, không tăng vốn điều lệ',
     'Chào bán cổ phiếu lần đầu ra công chúng để huy động thêm vốn cho tổ chức phát hành',
     'Chào bán thêm cổ phiếu ra công chúng của công ty đại chúng cho cổ đông hiện hữu',
     'Chào bán cổ phiếu riêng lẻ của cổ đông cho các nhà đầu tư chứng khoán chuyên nghiệp'],
    'Điểm b khoản 1 Điều 10 Nghị định 155/2020/NĐ-CP: chào bán cổ phiếu lần đầu ra công chúng để trở thành công ty đại chúng thông qua thay đổi cơ cấu sở hữu, không làm tăng vốn điều lệ. Tiền thu được thuộc về cổ đông bán, không về M. Nếu M đồng thời phát hành cổ phiếu mới thì là hình thức kết hợp (điểm c).',
    'Điểm b khoản 1 Điều 10 Nghị định 155/2020/NĐ-CP (điều này không bị Nghị định 245/2025/NĐ-CP sửa đổi)',
    'Chào bán cổ phiếu lần đầu ra công chúng để trở thành công ty đại chúng thông qua thay đổi cơ cấu sở hữu nhưng không làm tăng vốn điều lệ của tổ chức phát hành;', ND155, pos=0)

add(T3, 2, 'Công ty chứng khoán K bảo lãnh phát hành cổ phiếu cho công ty X theo phương thức “tối thiểu – tối đa”, với mức tối thiểu 60% và mức tối đa 100% số cổ phiếu chào bán. Kết thúc thời hạn phân phối, K bán được 75% số cổ phiếu. Kết quả đợt phát hành là:',
    ['Đợt phát hành có hiệu lực với 75% số cổ phiếu; K không phải mua số còn lại',
     'Đợt phát hành bị hủy bỏ do không bán hết 100% số cổ phiếu chào bán',
     'K phải mua 25% số cổ phiếu còn lại theo giá chào bán đã công bố',
     'Đợt phát hành chỉ có hiệu lực với 60% số cổ phiếu; phần vượt bị hoàn tiền'],
    'Bảo lãnh “tối thiểu – tối đa” là biến thể của bảo lãnh cố gắng tối đa: tổ chức bảo lãnh không cam kết mua số còn lại. Nếu số bán được dưới mức tối thiểu, đợt phát hành bị hủy; nếu đạt từ mức tối thiểu trở lên (75% ≥ 60%), đợt phát hành có hiệu lực với số đã bán. Cam kết mua phần còn lại là đặc điểm của bảo lãnh cam kết chắc chắn.',
    GT + ' – Các phương thức bảo lãnh phát hành (cam kết chắc chắn, cố gắng tối đa, tất cả hoặc không, tối thiểu – tối đa)', pos=1)

add(T3, 2, 'Trong thời gian phân phối cổ phiếu chào bán ra công chúng, Hội đồng quản trị công ty Y muốn dùng ngay số tiền nhà đầu tư đã nộp mua cổ phiếu để thanh toán một khoản nợ đến hạn. Theo Luật Chứng khoán, việc này:',
    ['Không được; tiền mua phải nằm trong tài khoản phong tỏa đến khi hoàn tất đợt chào bán và báo cáo UBCKNN',
     'Được, nếu Hội đồng quản trị thông qua và công bố thông tin trong vòng 24 giờ kể từ khi sử dụng tiền',
     'Được, nếu số tiền sử dụng không vượt quá 50% số tiền đã thu được trên tài khoản của đợt chào bán',
     'Được, khi đã phân phối được tối thiểu 70% số cổ phiếu chào bán và có xác nhận của ngân hàng'],
    'Khoản 3 Điều 26 Luật Chứng khoán: tiền mua chứng khoán phải được chuyển vào tài khoản phong tỏa mở tại ngân hàng, chi nhánh ngân hàng nước ngoài cho đến khi hoàn tất đợt chào bán và báo cáo UBCKNN. Vì vậy Y không được sử dụng số tiền này trong thời gian phân phối.',
    'Khoản 3 Điều 26 ' + LCK,
    'Tiền mua chứng khoán phải được chuyển vào tài khoản phong tỏa mở tại ngân hàng, chi nhánh ngân hàng nước ngoài cho đến khi hoàn tất đợt chào bán và báo cáo Ủy ban Chứng khoán Nhà nước.', LUAT, pos=2)

# L3 – phân phối theo tỷ lệ
offer, subs, a_sub = 6_000_000, 9_600_000, 80_000
alloc = a_sub * offer / subs
assert alloc == 50_000
vals = [alloc, a_sub * 0.6, a_sub - alloc, a_sub]
add(T3, 3, 'Công ty Z chào bán ra công chúng 6.000.000 cổ phiếu. Tổng số cổ phiếu nhà đầu tư đăng ký mua hợp lệ (đã nộp đủ tiền) là 9.600.000 cổ phiếu, trong đó nhà đầu tư A đăng ký mua 80.000 cổ phiếu. Phân phối theo quy định của Luật Chứng khoán (bỏ qua làm tròn), số cổ phiếu A được mua là:',
    [vn(v) + ' cổ phiếu' for v in vals],
    'Khoản 2 Điều 26: khi đăng ký mua vượt số được phép phát hành, phải phân phối hết cho nhà đầu tư tương ứng với tỷ lệ đăng ký mua. Tỷ lệ phân phối = 6.000.000 / 9.600.000 = 62,5%; A được 80.000 × 62,5% = 50.000 cổ phiếu (30.000 cổ phiếu còn lại được hoàn tiền). 48.000 là dùng nhầm tỷ lệ 60%.',
    'Khoản 2 Điều 26 ' + LCK,
    'Trường hợp số lượng chứng khoán đăng ký mua vượt quá số lượng chứng khoán được phép phát hành thì tổ chức phát hành hoặc tổ chức bảo lãnh phát hành phải phân phối hết số chứng khoán được phép phát hành cho nhà đầu tư tương ứng với tỷ lệ đăng ký mua của từng nhà đầu tư.', LUAT,
    key=vals, val=alloc)

# L3 – đấu giá theo giá đặt mua
lot = 2_000_000
bids = [('A', 600_000, 25_500), ('B', 800_000, 25_200), ('C', 900_000, 25_000), ('D', 500_000, 24_800)]
left, proceeds = lot, 0
for _, qn, px in sorted(bids, key=lambda b: -b[2]):
    take = min(qn, left); proceeds += take * px; left -= take
assert left == 0 and proceeds == 50_460_000_000
vals = [proceeds, lot * 25_000, lot * 25_500, lot * 24_500]
add(T3, 3, 'Giả định quy chế đấu giá bán cổ phần lần đầu: xét lần lượt từ mức giá đặt mua cao nhất trở xuống; nhà đầu tư trúng giá thanh toán theo đúng mức giá mình đặt; tại mức giá cuối cùng nếu khối lượng đặt mua vượt số cổ phần còn lại thì phân bổ theo tỷ lệ. Số cổ phần chào bán là 2.000.000, giá khởi điểm 24.500 đồng. Các lệnh đặt mua hợp lệ: A 600.000 cổ phần giá 25.500 đồng; B 800.000 cổ phần giá 25.200 đồng; C 900.000 cổ phần giá 25.000 đồng; D 500.000 cổ phần giá 24.800 đồng. Tổng số tiền thu được từ đợt đấu giá là:',
    [vn(v / 1e9, 2) + ' tỷ đồng' for v in vals],
    'A trúng 600.000 × 25.500 = 15,3 tỷ; B trúng 800.000 × 25.200 = 20,16 tỷ; còn 600.000 cổ phần cho C ở giá 25.000 = 15,0 tỷ; D không trúng. Tổng = 50,46 tỷ đồng. 50,00 tỷ là tính theo một giá thống nhất 25.000 đồng (kiểu đấu giá Hà Lan), 49,00 tỷ là tính theo giá khởi điểm.',
    GT + ' – Phương thức đấu giá trong phát hành chứng khoán (đấu giá theo giá đặt mua và đấu giá theo giá thống nhất)', key=vals, val=proceeds)

# L3 – IPO kết hợp: pha loãng tỷ lệ sở hữu
sh0, s0, new, sold = 50_000_000, 40_000_000, 12_500_000, 7_500_000
own = (s0 - sold) / (sh0 + new)
assert abs(own - 0.52) < 1e-12
vals = [own, (s0 - sold) / sh0, s0 / (sh0 + new), (s0 - sold) / (sh0 + new + sold)]
add(T3, 3, 'Trước khi IPO, công ty cổ phần B có 50.000.000 cổ phiếu, trong đó cổ đông sáng lập S nắm 40.000.000 cổ phiếu. Trong đợt chào bán cổ phiếu lần đầu ra công chúng theo hình thức kết hợp, B phát hành mới 12.500.000 cổ phiếu và S chào bán 7.500.000 cổ phiếu đang sở hữu; toàn bộ được bán hết cho các nhà đầu tư khác. Tỷ lệ sở hữu của S sau đợt chào bán là:',
    [vn(v * 100, 2) + '%' for v in vals],
    'Sau IPO, tổng số cổ phiếu = 50 + 12,5 = 62,5 triệu (cổ phiếu S bán là cổ phiếu cũ nên không làm tăng tổng số); S còn 40 − 7,5 = 32,5 triệu. Tỷ lệ = 32,5 / 62,5 = 52%. 65% là quên cổ phiếu phát hành mới; 64% là quên phần S đã bán; 46,43% là cộng nhầm cổ phiếu S bán vào tổng số cổ phiếu.',
    GT + ' – Các hình thức chào bán lần đầu ra công chúng; điểm c khoản 1 Điều 10 Nghị định 155/2020/NĐ-CP (hình thức kết hợp)', key=vals, val=own)

# ======================= 4. Thứ cấp =======================
add(T4, 1, 'Theo Luật Chứng khoán, chứng khoán niêm yết, đăng ký giao dịch được tổ chức giao dịch theo các phương thức nào?',
    ['Khớp lệnh tập trung, giao dịch thỏa thuận và phương thức khác theo Quy chế giao dịch của Sở giao dịch',
     'Chỉ khớp lệnh tập trung trên hệ thống giao dịch của Sở giao dịch chứng khoán Việt Nam',
     'Khớp lệnh tập trung và thỏa thuận trực tiếp giữa nhà đầu tư, không cần qua công ty chứng khoán',
     'Đấu giá và đấu thầu do Tổng công ty Lưu ký và Bù trừ chứng khoán Việt Nam tổ chức'],
    'Khoản 1 Điều 50 Luật Chứng khoán: chứng khoán niêm yết, đăng ký giao dịch được giao dịch theo phương thức khớp lệnh tập trung, phương thức giao dịch thỏa thuận và phương thức khác quy định tại Quy chế giao dịch chứng khoán của Sở giao dịch chứng khoán Việt Nam (lệnh vẫn qua thành viên giao dịch).',
    'Khoản 1 Điều 50 ' + LCK,
    'Chứng khoán niêm yết, đăng ký giao dịch được tổ chức giao dịch theo phương thức khớp lệnh tập trung, phương thức giao dịch thỏa thuận và phương thức giao dịch khác quy định tại Quy chế giao dịch chứng khoán của Sở giao dịch chứng khoán Việt Nam.', LUAT, pos=3)

add(T4, 1, 'Theo Luật Chứng khoán, việc đưa chứng khoán vào giao dịch trên hệ thống giao dịch cho chứng khoán chưa niêm yết được gọi là:',
    ['Đăng ký giao dịch', 'Niêm yết chứng khoán', 'Lưu ký chứng khoán', 'Đăng ký chứng khoán'],
    'Khoản 25 Điều 4: đăng ký giao dịch là việc đưa chứng khoán vào giao dịch trên hệ thống giao dịch cho chứng khoán chưa niêm yết (hệ thống Upcom). Niêm yết là đưa chứng khoán đủ điều kiện vào hệ thống giao dịch cho chứng khoán niêm yết; đăng ký chứng khoán là ghi nhận thông tin về tổ chức phát hành, chứng khoán và người sở hữu tại VSDC.',
    'Khoản 24, 25, 33 Điều 4 ' + LCK,
    'Đăng ký giao dịch là việc đưa chứng khoán vào giao dịch trên hệ thống giao dịch cho chứng khoán chưa niêm yết.', LUAT, pos=0)

add(T4, 2, 'Cổ phiếu của công ty T bị hủy bỏ niêm yết bắt buộc trên Sở giao dịch chứng khoán, nhưng T vẫn là công ty đại chúng. Theo Nghị định 155/2020/NĐ-CP (sửa đổi bởi Nghị định 245/2025/NĐ-CP), cổ phiếu T được xử lý như thế nào?',
    ['SGDCK phối hợp với VSDC đăng ký giao dịch cổ phiếu T trên Upcom trong 07 ngày làm việc kể từ ngày hủy niêm yết có hiệu lực',
     'Cổ phiếu T chỉ được chuyển nhượng bên ngoài hệ thống giao dịch trong 12 tháng kể từ ngày hủy niêm yết có hiệu lực',
     'T phải làm thủ tục hủy tư cách công ty đại chúng và hủy đăng ký chứng khoán tại VSDC trong thời hạn 30 ngày',
     'T phải chờ tối thiểu 02 năm kể từ ngày hủy niêm yết mới được đăng ký giao dịch cổ phiếu trên hệ thống Upcom'],
    'Điểm b khoản 1 Điều 133 (sửa đổi bởi Nghị định 245/2025/NĐ-CP): công ty bị hủy bỏ niêm yết bắt buộc hoặc tự nguyện nhưng vẫn là công ty đại chúng thuộc đối tượng đăng ký giao dịch. Điểm b khoản 2 Điều 133: trong 07 ngày làm việc kể từ ngày hủy niêm yết có hiệu lực, SGDCK phối hợp VSDC đăng ký giao dịch cổ phiếu này trên Upcom.',
    'Điểm b khoản 1 (sửa đổi bởi khoản 52 Điều 1 Nghị định 245/2025/NĐ-CP) và điểm b khoản 2 Điều 133 Nghị định 155/2020/NĐ-CP',
    'Trong thời hạn 07 ngày làm việc kể từ ngày hủy bỏ niêm yết có hiệu lực, Sở giao dịch chứng khoán có trách nhiệm phối hợp với Tổng công ty lưu ký và bù trừ chứng khoán Việt Nam thực hiện đăng ký giao dịch đối với cổ phiếu của công ty bị hủy bỏ niêm yết;', ND155, pos=1)

add(T4, 2, 'Công ty cổ phần V chưa từng chào bán cổ phiếu ra công chúng (không phải doanh nghiệp cổ phần hóa); cổ phiếu V đã giao dịch trên hệ thống Upcom được 15 tháng và V đáp ứng các điều kiện tài chính để niêm yết. Theo Nghị định 155/2020/NĐ-CP, V đã đủ điều kiện về thời gian giao dịch trên Upcom để đăng ký niêm yết cổ phiếu chưa?',
    ['Chưa, vì phải giao dịch trên Upcom tối thiểu 02 năm',
     'Đủ, vì chỉ cần giao dịch trên Upcom tối thiểu 12 tháng',
     'Đủ, vì pháp luật không yêu cầu thời gian giao dịch trên Upcom',
     'Chưa, vì phải giao dịch trên Upcom tối thiểu 03 năm'],
    'Điểm b khoản 1 Điều 109 Nghị định 155/2020/NĐ-CP: tổ chức đăng ký niêm yết phải đã giao dịch trên hệ thống Upcom tối thiểu 02 năm, trừ trường hợp đã chào bán cổ phiếu ra công chúng hoặc là doanh nghiệp cổ phần hóa. V chưa thuộc trường hợp loại trừ và mới giao dịch 15 tháng nên chưa đủ.',
    'Điểm b khoản 1 Điều 109 Nghị định 155/2020/NĐ-CP (điểm này không bị Nghị định 245/2025/NĐ-CP sửa đổi)',
    'Đã được Đại hội đồng cổ đông thông qua việc niêm yết; đã giao dịch trên hệ thống giao dịch Upcom tối thiểu 02 năm, trừ trường hợp tổ chức đăng ký niêm yết đã chào bán cổ phiếu ra công chúng, doanh nghiệp cổ phần hóa;', ND155, pos=2)

add(T4, 2, 'Theo Nghị định 155/2020/NĐ-CP (Điều 111a bổ sung bởi Nghị định 245/2025/NĐ-CP), khi công ty cổ phần đăng ký niêm yết cổ phiếu đồng thời với chào bán cổ phiếu lần đầu ra công chúng, Sở giao dịch chứng khoán ra quyết định chấp thuận niêm yết sau đợt chào bán khi tổ chức đăng ký niêm yết đáp ứng nhóm điều kiện nào?',
    ['Giá trị vốn hóa, cơ cấu cổ đông không phải cổ đông lớn và cam kết nắm giữ cổ phiếu',
     'Vốn điều lệ đã góp từ 30 tỷ đồng và ROE năm liền trước năm đăng ký tối thiểu 5%',
     'Không bị xử lý vi phạm về hành vi bị nghiêm cấm trong thời hạn 02 năm gần nhất',
     'Có công ty chứng khoán tư vấn hồ sơ và Đại hội đồng cổ đông thông qua việc niêm yết'],
    'Theo Điều 111a: trong 30 ngày kể từ khi nhận hồ sơ hợp lệ, SGDCK thông báo việc đáp ứng điều kiện vốn điều lệ từ 30 tỷ đồng và các điểm c, e, g khoản 1 Điều 109 (ROE, lãi, không vi phạm, có CTCK tư vấn). Sau khi có kết quả chào bán và tài liệu bổ sung, SGDCK chấp thuận niêm yết nếu đáp ứng giá trị vốn hóa (điểm a), cơ cấu cổ đông không phải cổ đông lớn (điểm d) và cam kết nắm giữ (điểm đ) – những điều kiện chỉ xác định được sau đợt IPO.',
    'Khoản 2, khoản 5 Điều 111a Nghị định 155/2020/NĐ-CP (bổ sung bởi khoản 38 Điều 1 Nghị định 245/2025/NĐ-CP)',
    'trường hợp tổ chức đăng ký niêm yết đáp ứng điều kiện về giá trị vốn hóa theo quy định tại điểm a khoản 1 Điều 109 và các điều kiện quy định tại điểm d, đ khoản 1 Điều 109 Nghị định này, Sở giao dịch chứng khoán có quyết định chấp thuận niêm yết cổ phiếu.', ND245, pos=3)

# L3 – chỉ số vốn hóa điều chỉnh theo tỷ lệ tự do chuyển nhượng
stk = [('A', 200e6, 0.30, 50_000, 54_000), ('B', 80e6, 0.50, 40_000, 36_800), ('C', 40e6, 0.90, 25_000, 29_000)]
ff = 100 * sum(s * f * p1 for _, s, f, _, p1 in stk) / sum(s * f * p0 for _, s, f, p0, _ in stk)
full = 100 * sum(s * p1 for _, s, f, _, p1 in stk) / sum(s * p0 for _, s, f, p0, _ in stk)
eq = 100 * sum(p1 / p0 for *_, p0, p1 in stk) / 3
pw = 100 * sum(p1 for *_, p1 in stk) / sum(p0 for *_, p0, _ in stk)
assert abs(ff - 104.6545) < 1e-3
vals = [round(v, 2) for v in (ff, full, eq, pw)]
add(T4, 3, 'Một chỉ số giá cổ phiếu tính theo phương pháp giá trị vốn hóa điều chỉnh theo tỷ lệ cổ phiếu tự do chuyển nhượng (free-float), giá trị ngày gốc là 100 điểm. Rổ chỉ số gồm 3 cổ phiếu (số cổ phiếu lưu hành và tỷ lệ free-float không đổi từ ngày gốc): A – 200 triệu cổ phiếu, free-float 30%, giá ngày gốc 50.000 đồng, giá hiện tại 54.000 đồng; B – 80 triệu cổ phiếu, free-float 50%, giá ngày gốc 40.000 đồng, giá hiện tại 36.800 đồng; C – 40 triệu cổ phiếu, free-float 90%, giá ngày gốc 25.000 đồng, giá hiện tại 29.000 đồng. Giá trị hiện tại của chỉ số là:',
    [vn(v, 2) + ' điểm' for v in vals],
    f'Vốn hóa free-float ngày gốc = 60tr × 50.000 + 40tr × 40.000 + 36tr × 25.000 = 5.500 tỷ; hiện tại = 60tr × 54.000 + 40tr × 36.800 + 36tr × 29.000 = 5.756 tỷ. Chỉ số = 100 × 5.756 / 5.500 ≈ {vn(ff,2)} điểm. {vn(full,2)} là dùng toàn bộ vốn hóa (bỏ qua free-float); {vn(eq,2)} là bình quân giản đơn mức tăng giá; {vn(pw,2)} là chỉ số bình quân giá.',
    GT + ' – Chỉ số giá chứng khoán: phương pháp tính theo giá trị vốn hóa (có điều chỉnh free-float)', key=vals, val=round(ff, 2))

# L3 – điều chỉnh hệ số chia khi thêm cổ phiếu vào rổ
I0, cap0, cap_new, cap1, newend = 1_200, 2_400_000, 120_000, 2_583_000, 126_000
div0 = cap0 / I0
div1 = div0 * (cap0 + cap_new) / cap0
I1 = cap1 / div1
assert div0 == 2_000 and abs(div1 - 2_100) < 1e-9 and abs(I1 - 1_230) < 1e-9
vals = [round(v, 2) for v in (I1, cap1 / div0, (cap1 - newend) / div0, (cap1 - newend) / div1)]
add(T4, 3, 'Cuối ngày T, một chỉ số tính theo giá trị vốn hóa đạt 1.200 điểm, tổng giá trị vốn hóa của rổ là 2.400.000 tỷ đồng. Đầu ngày T+1, một cổ phiếu mới có giá trị vốn hóa 120.000 tỷ đồng được đưa vào rổ; hệ số chia được điều chỉnh để việc thêm cổ phiếu không làm thay đổi giá trị chỉ số. Cuối ngày T+1, tổng giá trị vốn hóa của rổ (gồm cả cổ phiếu mới, khi đó có vốn hóa 126.000 tỷ đồng) là 2.583.000 tỷ đồng. Giá trị chỉ số cuối ngày T+1 là:',
    [vn(v, 2) + ' điểm' for v in vals],
    'Hệ số chia cũ = 2.400.000 / 1.200 = 2.000. Hệ số chia mới = 2.000 × (2.400.000 + 120.000) / 2.400.000 = 2.100. Chỉ số cuối T+1 = 2.583.000 / 2.100 = 1.230,00 điểm. 1.291,50 là không điều chỉnh hệ số chia; 1.228,50 là loại cổ phiếu mới và giữ hệ số chia cũ; 1.170,00 là loại cổ phiếu mới nhưng dùng hệ số chia mới.',
    GT + ' – Chỉ số giá chứng khoán: điều chỉnh hệ số chia khi thay đổi cổ phiếu trong rổ', key=vals, val=round(I1, 2))

# L3 – chỉ số bình quân giá, tách cổ phiếu
p_old = [30, 45, 75]
d0 = 3
idx0 = sum(p_old) / d0
p_split = [30, 45, 75 / 3]
d1 = sum(p_split) / idx0
p_next = [33, 47, 23]
I_next = sum(p_next) / d1
assert idx0 == 50 and abs(d1 - 2) < 1e-12 and abs(I_next - 51.5) < 1e-12
undo = (33 + 47 + 23 * 3) / 3
eqw = idx0 * sum(n / o for n, o in zip(p_next, p_split)) / 3
vals = [round(v, 2) for v in (I_next, sum(p_next) / d0, undo, eqw)]
assert len(set(vals)) == 4
add(T4, 3, 'Một chỉ số bình quân giá (price-weighted) gồm 3 cổ phiếu X, Y, Z có giá lần lượt 30.000; 45.000 và 75.000 đồng; hệ số chia là 3, chỉ số được tính bằng tổng giá (đơn vị nghìn đồng) chia hệ số chia, hiện bằng 50,00 điểm. Z tách mỗi cổ phiếu thành 3 cổ phiếu; hệ số chia được điều chỉnh để việc tách không làm thay đổi chỉ số. Phiên tiếp theo, giá X, Y, Z lần lượt là 33.000; 47.000 và 23.000 đồng. Giá trị chỉ số là:',
    [vn(v, 2) + ' điểm' for v in vals],
    f'Sau tách, giá Z = 25 nghìn đồng; hệ số chia mới = (30 + 45 + 25) / 50 = 2. Chỉ số phiên sau = (33 + 47 + 23) / 2 = 51,50 điểm. {vn(vals[1],2)} là không điều chỉnh hệ số chia; {vn(vals[2],2)} là quy giá Z về trước khi tách và giữ hệ số chia cũ (sai vì phương pháp bình quân giá điều chỉnh hệ số chia, làm giảm tỷ trọng của Z); {vn(vals[3],2)} là bình quân giản đơn tỷ lệ thay đổi giá.',
    GT + ' – Chỉ số giá chứng khoán: phương pháp bình quân giá giản đơn và điều chỉnh hệ số chia khi tách cổ phiếu', key=vals, val=round(I_next, 2))

# ======================= 5. Công ty chứng khoán =======================
add(T5, 1, 'Theo Luật Chứng khoán, công ty chứng khoán phải chính thức hoạt động trong thời hạn bao lâu kể từ ngày được cấp Giấy phép thành lập và hoạt động kinh doanh chứng khoán?',
    ['12 tháng', '06 tháng', '30 ngày', '24 tháng'],
    'Khoản 1 Điều 84 Luật Chứng khoán: công ty chứng khoán phải chính thức hoạt động trong thời hạn 12 tháng kể từ ngày được cấp phép; không được kinh doanh chứng khoán trước ngày chính thức hoạt động và phải công bố thông tin hoạt động ít nhất 30 ngày trước ngày dự kiến chính thức hoạt động (Điều 83).',
    'Khoản 1 Điều 84 ' + LCK,
    'Công ty chứng khoán, công ty quản lý quỹ đầu tư chứng khoán, chi nhánh, văn phòng đại diện công ty chứng khoán, công ty quản lý quỹ nước ngoài tại Việt Nam phải chính thức hoạt động trong thời hạn 12 tháng kể từ ngày được cấp phép.', LUAT, pos=0)

add(T5, 1, 'Theo Thông tư 121/2020/TT-BTC (văn bản hợp nhất năm 2026), bộ phận kiểm soát nội bộ của công ty chứng khoán được thiết lập trực thuộc:',
    ['Ban Tổng giám đốc (Ban Giám đốc)', 'Hội đồng quản trị/Hội đồng thành viên', 'Ban kiểm soát của công ty', 'Đại hội đồng cổ đông công ty'],
    'Khoản 1 Điều 12 Thông tư 121/2020/TT-BTC: bộ phận kiểm soát nội bộ trực thuộc Ban Tổng giám đốc (Ban Giám đốc), gồm bộ máy, nhân sự độc lập, chuyên trách và quy trình; bố trí tối thiểu 01 nhân viên kiểm soát tuân thủ. Kiểm toán nội bộ thì đánh giá độc lập hệ thống kiểm soát nội bộ này.',
    'Khoản 1 Điều 12 Thông tư 121/2020/TT-BTC (VBHN 09/VBHN-BTC năm 2026)',
    'Công ty chứng khoán phải thiết lập bộ phận kiểm soát nội bộ trực thuộc Ban Tổng giám đốc (Ban Giám đốc). Hệ thống kiểm soát nội bộ bao gồm bộ máy, nhân sự độc lập và chuyên trách, quy trình.', TT121, pos=1)

add(T5, 2, 'Một tổ chức đề nghị cấp phép thành lập công ty chứng khoán với đúng hai nghiệp vụ kinh doanh. Theo Luật Chứng khoán, tổ hợp nghiệp vụ nào sau đây có thể được cấp phép?',
    ['Môi giới chứng khoán và tư vấn đầu tư chứng khoán',
     'Tự doanh chứng khoán và tư vấn đầu tư chứng khoán',
     'Môi giới chứng khoán và bảo lãnh phát hành chứng khoán',
     'Tự doanh chứng khoán và bảo lãnh phát hành chứng khoán'],
    'Khoản 2 Điều 72: chỉ được cấp phép tự doanh khi được cấp phép môi giới; khoản 3: chỉ được cấp phép bảo lãnh phát hành khi được cấp phép tự doanh. Vì vậy tự doanh phải đi kèm môi giới, bảo lãnh phải đi kèm cả tự doanh và môi giới; chỉ tổ hợp môi giới + tư vấn đầu tư hợp lệ.',
    'Khoản 2, khoản 3 Điều 72 ' + LCK,
    'Công ty chứng khoán chỉ được cấp phép thực hiện nghiệp vụ tự doanh chứng khoán khi được cấp phép thực hiện nghiệp vụ môi giới chứng khoán.', LUAT, pos=2)

add(T5, 2, 'Theo Thông tư 121/2020/TT-BTC (văn bản hợp nhất năm 2026), giao dịch nào sau đây của công ty chứng khoán KHÔNG được coi là tự doanh chứng khoán?',
    ['Mua, bán chứng khoán do sửa lỗi sau giao dịch',
     'Mua cổ phiếu niêm yết cho tài khoản của chính công ty',
     'Mua bán lại trái phiếu niêm yết trên tài khoản của công ty',
     'Bán chứng chỉ quỹ ETF trong danh mục đầu tư của công ty'],
    'Khoản 3 Điều 22 Thông tư 121/2020/TT-BTC: mua, bán chứng khoán do sửa lỗi sau giao dịch và mua, bán cổ phiếu của chính mình không được coi là tự doanh. Các giao dịch mua, bán chứng khoán cho chính công ty còn lại là tự doanh (khoản 30 Điều 4 Luật Chứng khoán).',
    'Khoản 3 Điều 22 Thông tư 121/2020/TT-BTC (VBHN 09/VBHN-BTC năm 2026)',
    'Các trường hợp sau không được coi là tự doanh chứng khoán: a) Mua, bán chứng khoán do sửa lỗi sau giao dịch; b) Mua, bán cổ phiếu của chính mình.', TT121, pos=3)

add(T5, 2, 'Công ty chứng khoán P đang nắm giữ 12% vốn điều lệ của công ty cổ phần Q. Theo Thông tư 121/2020/TT-BTC (văn bản hợp nhất năm 2026), P KHÔNG được cung cấp dịch vụ nào sau đây cho Q?',
    ['Tư vấn hồ sơ chào bán và niêm yết chứng khoán của Q',
     'Mở tài khoản và môi giới giao dịch chứng khoán cho Q',
     'Lưu ký chứng khoán cho Q với tư cách thành viên lưu ký',
     'Cung cấp dịch vụ giao dịch chứng khoán trực tuyến cho Q'],
    'Khoản 2 Điều 25 Thông tư 121/2020/TT-BTC: CTCK không được tư vấn chào bán, tư vấn niêm yết, tư vấn cổ phần hóa, tư vấn xác định giá trị doanh nghiệp cho công ty mà mình nắm giữ từ 10% trở lên vốn điều lệ (khoản 7 Điều 24 cũng cấm tư vấn đầu tư chứng khoán cho công ty này). Các dịch vụ môi giới, lưu ký, giao dịch trực tuyến không bị cấm.',
    'Khoản 2 Điều 25, khoản 7 Điều 24 Thông tư 121/2020/TT-BTC (VBHN 09/VBHN-BTC năm 2026)',
    'Công ty chứng khoán không được cung cấp dịch vụ tư vấn chào bán, tư vấn niêm yết chứng khoán, tư vấn cổ phần hóa, tư vấn xác định giá trị doanh nghiệp cho công ty mà mình nắm giữ từ 10% trở lên vốn điều lệ.', TT121, pos=0)

# L3 – vốn điều lệ tối thiểu khi bổ sung nghiệp vụ
cap = dict(mg=25, td=50, bl=165, tv=10)
cur = 40
need = sum(cap.values()) - cur
assert need == 210
vals = [need, cap['td'] + cap['bl'] - cur, cap['mg'] + cap['td'] + cap['bl'] - cur, cap['bl']]
add(T5, 3, 'Công ty chứng khoán H đang được cấp phép nghiệp vụ môi giới và tư vấn đầu tư chứng khoán, vốn điều lệ hiện tại 40 tỷ đồng. H muốn bổ sung đồng thời nghiệp vụ tự doanh và bảo lãnh phát hành chứng khoán. Theo Nghị định 155/2020/NĐ-CP, H phải tăng vốn điều lệ thêm tối thiểu:',
    [vn(v) + ' tỷ đồng' for v in vals],
    'Vốn điều lệ tối thiểu cho 4 nghiệp vụ = 25 + 50 + 165 + 10 = 250 tỷ đồng (khoản 4 Điều 175: tổng vốn tương ứng từng nghiệp vụ). H cần tăng thêm 250 − 40 = 210 tỷ đồng. 175 tỷ là chỉ cộng hai nghiệp vụ mới rồi trừ vốn hiện có; 200 tỷ là quên nghiệp vụ tư vấn; 165 tỷ chỉ là mức của nghiệp vụ bảo lãnh.',
    'Khoản 1, khoản 4 Điều 175 Nghị định 155/2020/NĐ-CP (điều này không bị Nghị định 245/2025/NĐ-CP sửa đổi)',
    'a) Môi giới chứng khoán: 25 tỷ đồng; b) Tự doanh chứng khoán: 50 tỷ đồng; c) Bảo lãnh phát hành chứng khoán: 165 tỷ đồng; d) Tư vấn đầu tư chứng khoán: 10 tỷ đồng.', ND155,
    key=vals, val=need)

# L3 – hạn chế đầu tư
vcsh, hold, out, px = 1_000e9, 500_000, 12_000_000, 60_000
lim20 = 0.20 * out - hold
lim15v = (0.15 * vcsh - hold * px) / px
add_max = min(lim20, lim15v)
assert add_max == 1_900_000 and lim15v == 2_000_000
vals = [add_max, lim15v, 0.20 * out, 0.15 * out - hold]
add(T5, 3, 'Công ty chứng khoán G có vốn chủ sở hữu 1.000 tỷ đồng, đang nắm giữ 500.000 cổ phiếu của công ty niêm yết X. X có 12.000.000 cổ phiếu đang lưu hành, giá thị trường 60.000 đồng/cổ phiếu (khoản đầu tư hiện tại vào X tính theo giá này). Giả định các hạn mức đầu tư khác của G chưa bị chạm tới. Theo Thông tư 121/2020/TT-BTC (văn bản hợp nhất năm 2026), số cổ phiếu X tối đa G có thể mua thêm là:',
    [vn(v) + ' cổ phiếu' for v in vals],
    'Hạn mức 1 (điểm c khoản 4 Điều 28): không quá 20% số cổ phiếu đang lưu hành của tổ chức niêm yết = 2.400.000 cổ phiếu → được mua thêm 1.900.000. Hạn mức 2 (điểm e): không quá 15% vốn chủ sở hữu vào một tổ chức = 150 tỷ đồng → (150 − 30) tỷ / 60.000 = 2.000.000 cổ phiếu. Lấy mức nhỏ hơn: 1.900.000 cổ phiếu. 1.300.000 là dùng nhầm hạn mức 15% áp dụng cho tổ chức chưa niêm yết.',
    'Điểm c, điểm e khoản 4 Điều 28 Thông tư 121/2020/TT-BTC (VBHN 09/VBHN-BTC năm 2026)',
    'Đầu tư quá 20% tổng số cổ phiếu, chứng chỉ quỹ đang lưu hành của một tổ chức niêm yết;', TT121,
    key=vals, val=add_max)

# L3 – tỷ lệ vốn khả dụng
vkd, rm, rt, rh = 540, 150, 60, 50
tot = rm + rt + rh
room = vkd / 1.8 - tot
assert tot == 260 and abs(room - 40) < 1e-9
vals = [room, vkd / 1.5 - tot, vkd / 1.8 - (rm + rt), (vkd / tot - 1.8) * tot]
assert abs(vals[2] - 90) < 1e-9 and abs(vals[3] - 72) < 1e-9
add(T5, 3, 'Công ty chứng khoán N có vốn khả dụng 540 tỷ đồng; giá trị rủi ro thị trường 150 tỷ đồng, giá trị rủi ro thanh toán 60 tỷ đồng, giá trị rủi ro hoạt động 50 tỷ đồng. Nếu N muốn duy trì tỷ lệ vốn khả dụng không thấp hơn 180% (vốn khả dụng không đổi), tổng giá trị rủi ro của N có thể tăng thêm tối đa là:',
    [vn(v) + ' tỷ đồng' for v in vals],
    'Tổng giá trị rủi ro = 150 + 60 + 50 = 260 tỷ đồng (tỷ lệ hiện tại ≈ 207,7%). Để tỷ lệ = vốn khả dụng / tổng giá trị rủi ro ≥ 180% thì tổng giá trị rủi ro ≤ 540 / 1,8 = 300 tỷ đồng → tăng thêm tối đa 40 tỷ đồng. 100 tỷ là dùng nhầm mốc 150%; 90 tỷ là quên rủi ro hoạt động; 72 tỷ là nhân chênh lệch tỷ lệ với tổng rủi ro hiện tại.',
    'Khoản 5, khoản 7 Điều 2 và khoản 1 Điều 11 Thông tư 91/2020/TT-BTC (các khoản này không bị Thông tư 102/2025/TT-BTC sửa đổi); mốc 180% là giả định của đề',
    'Tổng giá trị rủi ro là tổng các giá trị rủi ro thị trường, giá trị rủi ro thanh toán và giá trị rủi ro hoạt động.', TT91,
    key=vals, val=room)

# ======================= ghi file =======================
assert len(Q) == 40
out = []
for i, r in enumerate(Q, 1):
    out.append(dict(id=f'C6-{i:03d}', part='CM', subject='CB', topic=r['topic'], level=r['level'], q=r['q'], o=r['o'], a=r['a'],
                    e=r['e'], basis=r['basis'], quote=r['quote'], src=r['src'], as_of='2026-11'))
OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
json.dump({f'C6-{k:03d}': v for k, v in NUM.items()}, open(D / 'work_c6' / 'num_answers.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('written', len(out))
