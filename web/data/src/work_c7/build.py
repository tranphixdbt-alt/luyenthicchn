"""Build cm_7.json (42 câu CB). Run: python3 -I build.py
Câu tính toán được tính lại ở đây và assert; trích dẫn được đối chiếu nguyên văn với văn bản nguồn."""
import json, re, random, unicodedata, datetime as dt
from pathlib import Path

ROOT = Path('/home/user/cchn_moi')
SRC = ROOT / 'web/data/src'
DOCS = ROOT / 'tai_lieu_phap_ly/van_ban_txt'
OUT = SRC / 'cm_7.json'
LAW = 'VBHN_24_VBHN-VPQH_2025_Luat_Chung_khoan_hop_nhat_Cong_bao.txt'
T96 = 'TT_96_2020_TT-BTC_Cong_bao.txt'
T121 = 'VBHN_09_VBHN-BTC_2026_TT121_68_08_hop_nhat.txt'
T98 = 'VBHN_04_VBHN-BTC_2026_TT98_136_hop_nhat.txt'
GT = 'Giáo trình Cơ bản về chứng khoán (UBCKNN/SRTC)'
LCK = 'Luật Chứng khoán 2019 (VBHN 24/VBHN-VPQH)'
TT96_NOTE = 'Thông tư 96/2020/TT-BTC (điều này không bị sửa đổi bởi TT 68/2024, TT 18/2025, TT 08/2026)'
TT121_H = 'Thông tư 121/2020/TT-BTC (VBHN 09/VBHN-BTC năm 2026)'
TT98_H = 'Thông tư 98/2020/TT-BTC (VBHN 04/VBHN-BTC năm 2026, hợp nhất TT 136/2025/TT-BTC)'
TP1 = 'Công ty quản lý quỹ và quỹ đầu tư chứng khoán'
TP2 = 'Quản lý, giám sát thị trường chứng khoán'
TP3 = 'Đạo đức nghề nghiệp trong hoạt động kinh doanh chứng khoán'
TP4 = 'Hệ thống đăng ký, lưu ký, bù trừ và thanh toán chứng khoán'
TP5 = 'Công bố thông tin trên thị trường chứng khoán'


def vn(x, d=0):
    return f"{x:,.{d}f}".replace(',', '#').replace('.', ',').replace('#', '.')


Q = []


def add(topic, lv, q, o, e, basis, quote='', src='', rank=None):
    """o[0] là đáp án đúng; rank = giá trị số của 4 phương án (để kiểm tra thứ hạng đáp án)."""
    assert len(o) == 4 and len(set(o)) == 4, o
    Q.append(dict(topic=topic, level=lv, q=q, o=o, e=e, basis=basis, quote=quote, src=src, rank=rank))


# ---------------- 1. Quỹ đầu tư ----------------
add(TP1, 1,
    'Theo Luật Chứng khoán, quỹ mở hình thành từ việc tiếp nhận, hoán đổi danh mục chứng khoán cơ cấu lấy chứng chỉ quỹ, có chứng chỉ quỹ được niêm yết và giao dịch trên hệ thống giao dịch chứng khoán niêm yết, được gọi là:',
    ['Quỹ hoán đổi danh mục (quỹ ETF)', 'Quỹ đóng có chứng chỉ quỹ niêm yết', 'Quỹ thành viên', 'Quỹ đầu tư bất động sản'],
    'Khoản 42 Điều 4 Luật Chứng khoán định nghĩa quỹ hoán đổi danh mục là quỹ mở hình thành từ việc hoán đổi danh mục chứng khoán cơ cấu lấy chứng chỉ quỹ, chứng chỉ quỹ được niêm yết. Quỹ đóng huy động vốn bằng tiền và không mua lại chứng chỉ quỹ theo yêu cầu; quỹ thành viên chỉ gồm 02–99 nhà đầu tư chuyên nghiệp, không chào bán ra công chúng; quỹ bất động sản đầu tư chủ yếu vào bất động sản.',
    'Khoản 42 Điều 4 ' + LCK,
    'Quỹ hoán đổi danh mục là quỹ mở hình thành từ việc tiếp nhận, hoán đổi danh mục chứng khoán cơ cấu lấy chứng chỉ quỹ. Chứng chỉ quỹ hoán đổi danh mục được niêm yết và giao dịch trên hệ thống giao dịch cho chứng khoán niêm yết.', LAW)

add(TP1, 1,
    'Xét theo cơ cấu tổ chức, quỹ đầu tư có thể là một pháp nhân, nhà đầu tư góp vốn trở thành cổ đông và bầu ra Hội đồng quản trị để giám sát việc đầu tư. Theo Luật Chứng khoán, mô hình quỹ này ở Việt Nam là:',
    ['Công ty đầu tư chứng khoán', 'Quỹ mở dạng hợp đồng', 'Quỹ thành viên góp vốn theo hợp đồng', 'Công ty quản lý quỹ đầu tư chứng khoán'],
    'Giáo trình phân loại quỹ theo cơ cấu tổ chức thành quỹ dạng công ty (quỹ là pháp nhân, nhà đầu tư là cổ đông) và quỹ dạng hợp đồng (quỹ không có tư cách pháp nhân, do công ty quản lý quỹ quản lý theo Điều lệ quỹ). Khoản 1 Điều 114 Luật Chứng khoán: công ty đầu tư chứng khoán là quỹ đầu tư chứng khoán tổ chức theo loại hình công ty cổ phần. Quỹ mở và quỹ thành viên (thành lập trên cơ sở hợp đồng góp vốn, Điều 113) là quỹ dạng hợp đồng; công ty quản lý quỹ là doanh nghiệp đi quản lý quỹ, không phải bản thân quỹ.',
    'Khoản 1 Điều 114 ' + LCK + '; ' + GT + ' – phân loại quỹ theo cơ cấu tổ chức',
    'Công ty đầu tư chứng khoán là quỹ đầu tư chứng khoán được tổ chức theo loại hình công ty cổ phần để đầu tư chứng khoán.', LAW)

add(TP1, 2,
    'Theo Luật Chứng khoán, ngân hàng giám sát của quỹ đại chúng có các nghĩa vụ sau đây, NGOẠI TRỪ:',
    ['Quyết định danh mục và thời điểm mua, bán tài sản cho quỹ đại chúng',
     'Lưu ký tài sản của quỹ, quản lý tách biệt với tài sản của chính ngân hàng',
     'Giám sát để bảo đảm công ty quản lý quỹ tuân thủ pháp luật và Điều lệ quỹ',
     'Báo cáo UBCKNN khi phát hiện công ty quản lý quỹ vi phạm pháp luật'],
    'Khoản 2 Điều 116: ngân hàng giám sát lưu ký và quản lý tách biệt tài sản quỹ; giám sát công ty quản lý quỹ; thu, chi, thanh toán, chuyển giao tài sản theo yêu cầu hợp pháp của công ty quản lý quỹ; xác nhận báo cáo; báo cáo UBCKNN khi phát hiện vi phạm. Quyết định đầu tư thuộc về công ty quản lý quỹ; ngân hàng giám sát chỉ thực hiện thanh toán, chuyển giao tài sản theo yêu cầu hợp pháp của công ty quản lý quỹ.',
    'Khoản 2 Điều 116 ' + LCK,
    'Thực hiện hoạt động thu, chi, thanh toán và chuyển giao tài sản liên quan đến hoạt động của quỹ đại chúng, công ty đầu tư chứng khoán theo yêu cầu hợp pháp của công ty quản lý quỹ đầu tư chứng khoán', LAW)

add(TP1, 2,
    'Ngân hàng thương mại H đang là ngân hàng giám sát của quỹ mở F do công ty quản lý quỹ M quản lý. Theo Luật Chứng khoán, việc nào sau đây H KHÔNG được thực hiện?',
    ['Mua lại từ quỹ F lô trái phiếu Chính phủ mà M quyết định bán',
     'Thu phí lưu ký, giám sát theo hợp đồng dịch vụ đã ký với M',
     'Xác nhận giá trị tài sản ròng trên một đơn vị quỹ do M xác định',
     'Thanh toán tiền mua cổ phiếu cho quỹ F theo yêu cầu hợp pháp của M'],
    'Khoản 2 Điều 117: ngân hàng giám sát (và thành viên HĐQT, người điều hành, nhân viên làm nhiệm vụ giám sát, bảo quản tài sản quỹ) không được là đối tác mua, bán trong giao dịch tài sản của quỹ đại chúng. Thu phí dịch vụ theo hợp đồng, xác nhận NAV (khoản 1 Điều 106) và thanh toán theo yêu cầu hợp pháp của công ty quản lý quỹ (điểm d khoản 2 Điều 116) là hoạt động bình thường của ngân hàng giám sát.',
    'Khoản 2 Điều 117 ' + LCK,
    'Ngân hàng giám sát, thành viên Hội đồng quản trị, người điều hành và nhân viên của ngân hàng giám sát làm nhiệm vụ giám sát hoạt động và bảo quản tài sản của quỹ đại chúng, công ty đầu tư chứng khoán không được là đối tác mua, bán trong giao dịch mua, bán tài sản của quỹ đại chúng', LAW)

add(TP1, 2,
    'Vào ngày định giá mua lại của quỹ mở Q, một cổ phiếu chiếm tỷ trọng lớn trong danh mục của quỹ bị đình chỉ giao dịch nên không thể xác định giá trị tài sản ròng của quỹ. Theo Luật Chứng khoán, công ty quản lý quỹ xử lý như thế nào?',
    ['Không phải mua lại chứng chỉ quỹ, báo cáo UBCKNN trong 24 giờ và tiếp tục mua lại khi sự kiện chấm dứt',
     'Vẫn phải mua lại theo NAV của kỳ định giá liền trước, sau đó điều chỉnh phần chênh lệch cho nhà đầu tư',
     'Được ngừng mua lại đến kỳ Đại hội nhà đầu tư thường niên gần nhất mà không phải báo cáo UBCKNN',
     'Phải giải thể quỹ mở và thanh lý toàn bộ danh mục để hoàn trả vốn cho nhà đầu tư'],
    'Điểm b khoản 2 Điều 111: công ty quản lý quỹ không phải mua lại chứng chỉ quỹ mở khi không thể xác định NAV vào ngày định giá mua lại do có quyết định đình chỉ giao dịch chứng khoán trong danh mục. Khoản 3 Điều 111: phải báo cáo UBCKNN trong 24 giờ kể từ khi xảy ra sự kiện và tiếp tục mua lại sau khi sự kiện chấm dứt. Luật không cho dùng NAV kỳ trước, không cho ngừng đến Đại hội nhà đầu tư và sự kiện này không phải căn cứ giải thể quỹ.',
    'Điểm b khoản 2, khoản 3 Điều 111 ' + LCK,
    'Công ty quản lý quỹ đầu tư chứng khoán phải báo cáo Ủy ban Chứng khoán Nhà nước trong thời hạn 24 giờ kể từ khi xảy ra một trong các sự kiện quy định tại khoản 2 Điều này và phải tiếp tục thực hiện việc mua lại chứng chỉ quỹ mở sau khi sự kiện này chấm dứt.', LAW)

# C7-006: mua chứng chỉ quỹ mở
from fractions import Fraction as Fr
A, NAV, f = 200_000_000, 15_625, Fr(15, 1000)
price = NAV * (1 + f)
trunc = lambda x: int(x * 100) / 100  # x là Fraction nên cắt chính xác
u_key = trunc(A / price)
u_nofee = trunc(A / NAV)
u_gross = trunc(A * (1 - f) / NAV)
u_twice = trunc(A * (1 - f) / price)
assert abs(price - 15_859.375) < 1e-9 and u_key == 12_610.83 and u_nofee == 12_800 and u_gross == 12_608 and u_twice == 12_421.67
add(TP1, 3,
    'Nhà đầu tư nộp 200.000.000 đồng để mua chứng chỉ quỹ mở P. Giá trị tài sản ròng trên một đơn vị quỹ tại ngày giao dịch là 15.625 đồng; giá dịch vụ phát hành bằng 1,5% giá trị tài sản ròng trên một đơn vị quỹ và được cộng vào giá bán. Số đơn vị quỹ nhà đầu tư nhận được (làm tròn xuống đến 2 chữ số thập phân) là:',
    [vn(u_key, 2) + ' đơn vị', vn(u_nofee, 2) + ' đơn vị', vn(u_gross, 2) + ' đơn vị', vn(u_twice, 2) + ' đơn vị'],
    'Theo khoản 2 Điều 34 TT 98/2020, giá bán = NAV/đơn vị + giá dịch vụ phát hành = 15.625 × (1 + 1,5%) = 15.859,375 đồng. Số đơn vị = 200.000.000 / 15.859,375 = 12.610,83. Lỗi thường gặp: bỏ qua giá dịch vụ (200.000.000 / 15.625 = 12.800,00); trừ phí vào số tiền rồi chia cho NAV (197.000.000 / 15.625 = 12.608,00 – sai cách tính đề cho); trừ phí hai lần (197.000.000 / 15.859,375 = 12.421,67).',
    'Khoản 2 Điều 34 ' + TT98_H,
    'Giá bán một đơn vị quỹ, là mức giá mà nhà đầu tư phải thanh toán cho công ty quản lý quỹ, bằng giá trị tài sản ròng trên một đơn vị quỹ tính tại ngày giao dịch chứng chỉ quỹ cộng với giá dịch vụ phát hành (nếu có).', T98,
    rank=[u_key, u_nofee, u_gross, u_twice])

# C7-007: chiết khấu quỹ đóng
TA, L, N, P, NAV_old = 1_260e9, 60e9, 80e6, 12_600, 1_150e9
nav = (TA - L) / N
d_key = (nav - P) / nav
d_old = (NAV_old / N - P) / (NAV_old / N)
d_byP = (nav - P) / P
d_TA = (TA / N - P) / (TA / N)
assert nav == 15_000 and round(d_key, 4) == 0.16 and round(d_old * 100, 2) == 12.35 and round(d_byP * 100, 2) == 19.05 and round(d_TA, 4) == 0.20
pct = lambda x: vn(x * 100, 2) + '%'
add(TP1, 3,
    'Quỹ đóng V có 80.000.000 chứng chỉ quỹ đang lưu hành. Kỳ định giá trước, quỹ công bố giá trị tài sản ròng 1.150 tỷ đồng. Tại ngày định giá gần nhất, quỹ có tổng giá trị tài sản 1.260 tỷ đồng và tổng nợ phải trả 60 tỷ đồng; giá đóng cửa chứng chỉ quỹ V trên Sở giao dịch cùng ngày là 12.600 đồng. Mức chiết khấu của giá thị trường so với NAV/chứng chỉ quỹ tại ngày định giá gần nhất là:',
    [pct(d_key), pct(d_old), pct(d_byP), pct(d_TA)],
    'NAV/chứng chỉ quỹ = (1.260 − 60) tỷ / 80 triệu = 15.000 đồng. Chiết khấu = (15.000 − 12.600) / 15.000 = 16,00%. Lỗi thường gặp: dùng NAV kỳ trước (1.150 tỷ / 80 triệu = 14.375 đồng → 12,35%); chia cho giá thị trường thay vì NAV (2.400 / 12.600 = 19,05%); quên trừ nợ phải trả (15.750 đồng → 20,00%). Giá chứng chỉ quỹ đóng do cung cầu trên thị trường quyết định nên có thể thấp hơn (chiết khấu) hoặc cao hơn (thặng dư) NAV.',
    GT + ' – NAV và chiết khấu/thặng dư của chứng chỉ quỹ đóng', rank=[d_key, d_old, d_byP, d_TA])

# C7-008: hoán đổi ETF
nav_u, px_etf, lots, lot, basket = 18_350, 18_420, 5, 100_000, 9_120_000_000
cash = nav_u * lots * lot - basket
cash_px = px_etf * lots * lot - basket
cash_1 = nav_u * lot - basket // lots
assert cash == 55_000_000 and cash_px == 90_000_000 and cash_1 == 11_000_000
add(TP1, 3,
    'Quỹ ETF E quy định 01 lô chứng chỉ quỹ gồm 100.000 chứng chỉ quỹ. Tại ngày giao dịch hoán đổi, NAV trên một chứng chỉ quỹ là 18.350 đồng, giá đóng cửa chứng chỉ quỹ E trên Sở giao dịch là 18.420 đồng. Thành viên lập quỹ nộp danh mục chứng khoán cơ cấu trị giá 9.120.000.000 đồng để nhận 05 lô chứng chỉ quỹ. Phần chênh lệch được xử lý như sau:',
    ['Thành viên lập quỹ nộp thêm 55.000.000 đồng bằng tiền cho quỹ',
     'Thành viên lập quỹ nộp thêm 90.000.000 đồng bằng tiền cho quỹ',
     'Thành viên lập quỹ nộp thêm 11.000.000 đồng bằng tiền cho quỹ',
     'Quỹ ETF hoàn trả cho thành viên lập quỹ 55.000.000 đồng'],
    'Giao dịch hoán đổi tính theo NAV, không theo giá thị trường. Giá trị 05 lô = 18.350 × 100.000 × 5 = 9.175.000.000 đồng, cao hơn giá trị danh mục nộp 55.000.000 đồng, nên theo điểm a khoản 4 Điều 43 TT 98/2020 (sửa đổi bởi TT 136/2025) thành viên lập quỹ thanh toán bổ sung phần chênh lệch bằng tiền. Lỗi thường gặp: dùng giá thị trường 18.420 (90 triệu); chỉ tính cho 01 lô (11 triệu); nhầm chiều thanh toán.',
    'Điểm a khoản 4 Điều 43 ' + TT98_H,
    'Khi hoán đổi danh mục chứng khoán cơ cấu lấy các lô chứng chỉ quỹ ETF, giá trị của danh mục chứng khoán cơ cấu thấp hơn giá trị tài sản ròng của các lô chứng chỉ quỹ ETF. Phần chênh lệch phát sinh được thành viên lập quỹ, nhà đầu tư thanh toán bổ sung bằng tiền', T98,
    rank=[cash, cash_px, cash_1, -cash])

# ---------------- 2. Quản lý, giám sát ----------------
add(TP2, 1,
    'Theo Luật Chứng khoán, cơ quan nào chịu trách nhiệm trước Chính phủ thực hiện quản lý nhà nước về chứng khoán và thị trường chứng khoán?',
    ['Bộ Tài chính', 'Ủy ban Chứng khoán Nhà nước', 'Ngân hàng Nhà nước Việt Nam', 'Sở giao dịch chứng khoán Việt Nam'],
    'Khoản 1, 2 Điều 8: Chính phủ thống nhất quản lý nhà nước; Bộ Tài chính chịu trách nhiệm trước Chính phủ thực hiện quản lý nhà nước về chứng khoán và TTCK. UBCKNN là cơ quan thuộc Bộ Tài chính, tham mưu, giúp Bộ trưởng (Điều 9); các bộ, ngành khác như Ngân hàng Nhà nước chỉ phối hợp trong phạm vi nhiệm vụ; Sở giao dịch chứng khoán là doanh nghiệp tổ chức thị trường giao dịch.',
    'Khoản 2 Điều 8 ' + LCK,
    'Bộ Tài chính chịu trách nhiệm trước Chính phủ thực hiện quản lý nhà nước về chứng khoán và thị trường chứng khoán', LAW)

add(TP2, 1,
    'Theo Luật Chứng khoán, Tổng giám đốc (Giám đốc) Sở giao dịch chứng khoán Việt Nam do ai phê chuẩn hoặc bổ nhiệm, miễn nhiệm?',
    ['Bộ trưởng Bộ Tài chính', 'Chủ tịch Ủy ban Chứng khoán Nhà nước', 'Thủ tướng Chính phủ', 'Đại hội đồng cổ đông của Sở giao dịch'],
    'Khoản 2 Điều 44: Chủ tịch Hội đồng thành viên hoặc Chủ tịch Hội đồng quản trị, Tổng giám đốc (Giám đốc) Sở giao dịch chứng khoán Việt Nam do Bộ trưởng Bộ Tài chính phê chuẩn hoặc bổ nhiệm, miễn nhiệm theo đề nghị của Hội đồng thành viên/Hội đồng quản trị Sở và ý kiến của Chủ tịch UBCKNN. Thủ tướng Chính phủ quyết định thành lập, mô hình hoạt động và cơ cấu tổ chức quản lý của Sở (Điều 43, khoản 1 Điều 44); Chủ tịch UBCKNN chỉ cho ý kiến.',
    'Khoản 2 Điều 44 ' + LCK,
    'Tổng giám đốc (Giám đốc) Sở giao dịch chứng khoán Việt Nam do Bộ trưởng Bộ Tài chính phê chuẩn hoặc bổ nhiệm, miễn nhiệm theo đề nghị của Hội đồng thành viên hoặc Hội đồng quản trị Sở giao dịch chứng khoán Việt Nam và ý kiến của Chủ tịch Ủy ban Chứng khoán Nhà nước.', LAW)

add(TP2, 1,
    'Theo Luật Chứng khoán, tổ chức, cá nhân có hành vi vi phạm pháp luật về chứng khoán và thị trường chứng khoán bị xử lý như thế nào?',
    ['Tùy tính chất, mức độ mà bị xử phạt hành chính hoặc truy cứu trách nhiệm hình sự; gây thiệt hại thì phải bồi thường',
     'Chỉ bị xử phạt vi phạm hành chính; việc bồi thường thiệt hại do các bên tự thỏa thuận, không do pháp luật quy định',
     'Chỉ bị Sở giao dịch chứng khoán xử lý theo quy chế thành viên, không áp dụng trách nhiệm hình sự',
     'Bị truy cứu trách nhiệm hình sự trong mọi trường hợp, không phân biệt tính chất, mức độ vi phạm'],
    'Khoản 1 Điều 132: tùy theo tính chất, mức độ vi phạm mà bị xử phạt hành chính hoặc bị truy cứu trách nhiệm hình sự; nếu gây thiệt hại thì phải bồi thường theo quy định của pháp luật. Sở giao dịch chỉ kiểm tra, xử lý vi phạm đối với thành viên, tổ chức niêm yết theo quy chế của Sở (điểm i khoản 1 Điều 46), không thay thế xử phạt hành chính hay hình sự.',
    'Khoản 1 Điều 132 ' + LCK,
    'tùy theo tính chất, mức độ vi phạm mà bị xử phạt hành chính hoặc bị truy cứu trách nhiệm hình sự; nếu gây thiệt hại thì phải bồi thường theo quy định của pháp luật.', LAW)

add(TP2, 1,
    'Theo Luật Chứng khoán, quy chế niêm yết chứng khoán và quy chế giao dịch chứng khoán của Sở giao dịch chứng khoán Việt Nam được ban hành như thế nào?',
    ['Sở giao dịch chứng khoán ban hành sau khi được Ủy ban Chứng khoán Nhà nước chấp thuận',
     'Bộ trưởng Bộ Tài chính trực tiếp ban hành dưới hình thức thông tư hướng dẫn',
     'Thủ tướng Chính phủ ban hành theo đề nghị của Hội đồng quản trị Sở giao dịch',
     'Sở giao dịch tự ban hành, chỉ cần báo cáo Bộ Tài chính sau khi áp dụng'],
    'Điểm a khoản 1 Điều 46: Sở giao dịch chứng khoán có quyền ban hành các quy chế về niêm yết, giao dịch, công bố thông tin, thành viên… sau khi được UBCKNN chấp thuận. Điểm d khoản 1 Điều 9 (sửa đổi bởi Luật 56/2024/QH15) giao UBCKNN chấp thuận các quy chế nghiệp vụ và có quyền yêu cầu Sở sửa đổi quy chế.',
    'Điểm a khoản 1 Điều 46 ' + LCK,
    'Ban hành các quy chế về niêm yết chứng khoán, giao dịch chứng khoán, công bố thông tin, thành viên của Sở giao dịch chứng khoán Việt Nam và các quy chế nghiệp vụ khác liên quan đến tổ chức và hoạt động thị trường giao dịch chứng khoán sau khi được Ủy ban Chứng khoán Nhà nước chấp thuận', LAW)

add(TP2, 2,
    'Giả sử Sở giao dịch chứng khoán Việt Nam dự kiến đưa vào vận hành một hệ thống giao dịch mới, đồng thời áp dụng một phương thức giao dịch mới. Theo Luật Chứng khoán, chủ thể có thẩm quyền chấp thuận các nội dung này là:',
    ['Ủy ban Chứng khoán Nhà nước', 'Hội đồng quản trị Sở giao dịch chứng khoán Việt Nam', 'Thủ tướng Chính phủ', 'Ngân hàng Nhà nước Việt Nam'],
    'Điểm đ khoản 1 Điều 9: UBCKNN chấp thuận việc đưa vào giao dịch các loại chứng khoán mới, thay đổi và áp dụng phương thức giao dịch mới, chấp thuận hệ thống giao dịch chứng khoán và đưa vào vận hành hệ thống giao dịch mới. Thủ tướng Chính phủ quyết định thành lập, mô hình hoạt động của Sở (khoản 2 Điều 43), không chấp thuận từng phương thức giao dịch; Hội đồng quản trị Sở không tự chấp thuận.',
    'Điểm đ khoản 1 Điều 9 ' + LCK,
    'Chấp thuận việc đưa vào giao dịch các loại chứng khoán mới, thay đổi và áp dụng phương thức giao dịch mới, chấp thuận hệ thống giao dịch chứng khoán và đưa vào vận hành hệ thống giao dịch chứng khoán mới', LAW)

add(TP2, 2,
    'Theo Luật Chứng khoán, biện pháp nào sau đây KHÔNG thuộc các biện pháp bảo đảm an ninh, an toàn thị trường chứng khoán?',
    ['Yêu cầu công ty chứng khoán dùng vốn tự doanh mua vào cổ phiếu để giữ giá',
     'Tạm ngừng, đình chỉ giao dịch đối với một hoặc một số chứng khoán niêm yết',
     'Phong tỏa tài khoản chứng khoán có liên quan đến hành vi vi phạm pháp luật',
     'Cấm đảm nhiệm chức vụ tại công ty chứng khoán do thực hiện hành vi bị cấm'],
    'Khoản 1 Điều 7 liệt kê các biện pháp: giám sát an ninh, an toàn thị trường; ứng phó sự cố; tạm ngừng, đình chỉ giao dịch một hoặc một số chứng khoán; tạm ngừng, đình chỉ hoạt động của Sở giao dịch, VSDC; cấm đảm nhiệm chức vụ, cấm hoạt động chứng khoán; phong tỏa tài khoản chứng khoán, yêu cầu phong tỏa tài khoản tiền liên quan đến vi phạm. Luật không có biện pháp buộc công ty chứng khoán mua vào để giữ giá.',
    'Khoản 1 Điều 7 ' + LCK,
    'Phong tỏa tài khoản chứng khoán, yêu cầu người có thẩm quyền phong tỏa tài khoản tiền có liên quan đến hành vi vi phạm pháp luật về chứng khoán và thị trường chứng khoán.', LAW)

add(TP2, 3,
    'Trong 10 phiên liên tiếp, nhà đầu tư K dùng tài khoản của chính mình liên tục đặt mua cổ phiếu X với khối lượng chi phối vào thời điểm đóng cửa thị trường, làm giá đóng cửa của X luôn cao hơn hẳn mức giá giao dịch trong ngày; K không tung tin hay bình luận gì về X. Theo Luật Chứng khoán (sửa đổi bởi Luật 56/2024/QH15), hành vi của K:',
    ['Là thao túng thị trường chứng khoán, vì mua liên tục với khối lượng chi phối lúc đóng cửa để thao túng giá',
     'Không vi phạm, vì K chỉ dùng tài khoản của chính mình và không đưa ra thông tin sai lệch',
     'Chỉ vi phạm nếu K đồng thời bán ra trong ngày mà không chuyển nhượng thực sự quyền sở hữu',
     'Là sử dụng thông tin nội bộ, vì K tác động đáng kể đến giá đóng cửa của cổ phiếu X'],
    'Điểm c khoản 49 Điều 4 (bổ sung bởi Luật 56/2024/QH15) xác định thao túng thị trường gồm hành vi liên tục mua hoặc bán chứng khoán với khối lượng chi phối vào thời điểm mở cửa hoặc đóng cửa thị trường nhằm thao túng giá; khoản 3 Điều 12 cấm hành vi thao túng. Hành vi này không đòi hỏi dùng tài khoản người khác hay tung tin; giao dịch không chuyển nhượng thực sự quyền sở hữu là một dạng thao túng khác (điểm b); K không sử dụng thông tin nội bộ.',
    'Điểm c khoản 49 Điều 4 và khoản 3 Điều 12 ' + LCK + ' (bổ sung, sửa đổi bởi Luật 56/2024/QH15)',
    'Liên tục mua hoặc bán chứng khoán với khối lượng chi phối vào thời điểm mở cửa hoặc đóng cửa thị trường nhằm thao túng giá chứng khoán', LAW)

add(TP2, 3,
    'Công ty TNHH tư vấn tài chính P không có giấy phép của UBCKNN, ký hợp đồng nhận tiền của nhiều cá nhân để trực tiếp quyết định mua, bán cổ phiếu niêm yết trên tài khoản do chính các cá nhân này đứng tên, hưởng phí bằng 20% lợi nhuận. Nhận định nào sau đây đúng theo Luật Chứng khoán?',
    ['P vi phạm điều cấm vì kinh doanh chứng khoán khi chưa được UBCKNN cấp giấy phép',
     'P không vi phạm nếu các cá nhân ủy thác đều là nhà đầu tư chứng khoán chuyên nghiệp',
     'P không vi phạm vì tài khoản giao dịch vẫn do chính khách hàng đứng tên tại công ty chứng khoán',
     'P chỉ vi phạm khi mức phí hưởng theo lợi nhuận vượt mức phí tối đa của các quỹ đại chúng'],
    'Quản lý danh mục đầu tư chứng khoán theo ủy thác (khoản 35 Điều 4) là nghiệp vụ kinh doanh chứng khoán của công ty quản lý quỹ được UBCKNN cấp phép (Điều 73). Khoản 4 Điều 12 nghiêm cấm thực hiện hoạt động kinh doanh chứng khoán khi chưa được UBCKNN cấp giấy phép. Việc tài khoản đứng tên khách hàng, khách hàng là nhà đầu tư chuyên nghiệp hay mức phí đều không làm hoạt động này trở nên hợp pháp.',
    'Khoản 4 Điều 12, khoản 35 Điều 4, Điều 73 ' + LCK,
    'Thực hiện hoạt động kinh doanh chứng khoán, cung cấp dịch vụ về chứng khoán khi chưa được Ủy ban Chứng khoán Nhà nước cấp giấy phép, cấp giấy chứng nhận hoặc chấp thuận.', LAW)

# ---------------- 3. Đạo đức nghề nghiệp ----------------
add(TP3, 1,
    'Theo Thông tư 121/2020/TT-BTC, ngoài tình hình tài chính, mục tiêu đầu tư và khả năng chấp nhận rủi ro, công ty chứng khoán cung cấp dịch vụ tư vấn đầu tư phải thu thập và quản lý thông tin nào khác về khách hàng?',
    ['Kinh nghiệm và hiểu biết về đầu tư của khách hàng',
     'Lịch sử quan hệ tín dụng của khách hàng tại các ngân hàng',
     'Danh mục chứng khoán của khách hàng tại công ty chứng khoán khác',
     'Nơi làm việc của người thân trong gia đình khách hàng'],
    'Khoản 2 Điều 24 TT 121/2020 yêu cầu thu thập, quản lý 04 nhóm thông tin: tình hình tài chính, mục tiêu đầu tư, khả năng chấp nhận rủi ro, kinh nghiệm và hiểu biết về đầu tư của khách hàng. Đây là cơ sở để tư vấn phù hợp (nguyên tắc “hiểu khách hàng”). Các thông tin còn lại không thuộc danh mục bắt buộc.',
    'Khoản 2 Điều 24 ' + TT121_H,
    'Công ty chứng khoán phải thu thập và quản lý thông tin về khách hàng, bao gồm: a) Tình hình tài chính của khách hàng; b) Mục tiêu đầu tư của khách hàng; c) Khả năng chấp nhận rủi ro của khách hàng; d) Kinh nghiệm và hiểu biết về đầu tư của khách hàng.', T121)

add(TP3, 2,
    'Bộ phận phân tích của công ty chứng khoán vừa hạ khuyến nghị đối với cổ phiếu Y từ “Mua” xuống “Bán”. Theo chuẩn mực đối xử công bằng với khách hàng, nhân viên môi giới nên làm gì?',
    ['Chờ công ty công bố chính thức, rồi chuyển khuyến nghị đồng thời cho mọi khách hàng phù hợp',
     'Gọi trước cho nhóm khách hàng VIP để họ kịp bán, sau đó mới gửi cho các khách hàng khác',
     'Chỉ báo cho những khách hàng đang nắm giữ nhiều cổ phiếu Y vì họ chịu ảnh hưởng lớn nhất',
     'Bán cổ phiếu Y trong tài khoản của mình trước, rồi mới thông báo khuyến nghị cho khách hàng'],
    'Chuẩn mực đối xử công bằng yêu cầu khi phổ biến khuyến nghị hoặc thay đổi khuyến nghị, người hành nghề phải chuyển thông tin cùng lúc tới mọi khách hàng phù hợp, không ưu tiên nhóm khách hàng lớn hay quen biết. Giao dịch cho tài khoản cá nhân trước khách hàng là đặt lợi ích bản thân lên trên lợi ích khách hàng (giao dịch trước khách hàng).',
    GT + ' – chuẩn mực đạo đức nghề nghiệp: đối xử công bằng với khách hàng')

add(TP3, 2,
    'Tại hội thảo thu hút khách hàng, nhân viên của công ty chứng khoán K tuyên bố: “Phương pháp phân tích của K chính xác và hiệu quả hơn hẳn mọi công ty chứng khoán khác”. Theo Thông tư 121/2020/TT-BTC, tuyên bố này:',
    ['Bị cấm, vì không được tuyên bố phương pháp phân tích của mình có giá trị cao hơn công ty khác',
     'Được phép, nếu K có số liệu nội bộ cho thấy tỷ lệ khuyến nghị đúng cao hơn bình quân ngành',
     'Được phép, vì đây là hoạt động tiếp thị thông thường, không gắn với mã chứng khoán cụ thể',
     'Chỉ bị cấm khi được đăng trên phương tiện thông tin đại chúng, không phải tại hội thảo'],
    'Điểm c khoản 6 Điều 4 TT 121/2020: khi cung cấp dịch vụ cho khách hàng, công ty chứng khoán không được trực tiếp hoặc gián tiếp quảng cáo, tuyên bố rằng nội dung, hiệu quả hoặc phương pháp phân tích của mình có giá trị cao hơn của công ty chứng khoán khác. Quy định không phân biệt hình thức, địa điểm tuyên bố hay việc công ty tự có số liệu so sánh.',
    'Điểm c khoản 6 Điều 4 ' + TT121_H,
    'Quảng cáo, tuyên bố rằng nội dung, hiệu quả, hoặc các phương pháp phân tích chứng khoán của mình có giá trị cao hơn của công ty chứng khoán khác', T121)

add(TP3, 2,
    'Chuyên viên phân tích A sao chép gần như nguyên văn số liệu và lập luận từ báo cáo của một công ty chứng khoán khác vào báo cáo phát hành dưới tên mình, không ghi nguồn. Theo Thông tư 121/2020/TT-BTC và chuẩn mực đạo đức nghề nghiệp, nhận định nào đúng?',
    ['Vi phạm, vì báo cáo phân tích phải ghi rõ nguồn trích dẫn số liệu và người chịu trách nhiệm nội dung',
     'Không vi phạm, vì báo cáo gốc đã công bố công khai nên không còn là thông tin cần bảo mật',
     'Không vi phạm, nếu khuyến nghị cuối cùng của A khác với khuyến nghị trong báo cáo gốc',
     'Chỉ vi phạm khi báo cáo được bán có thu phí, còn báo cáo gửi miễn phí thì được phép'],
    'Khoản 3 Điều 24 TT 121/2020: báo cáo phân tích, khuyến nghị đầu tư phải ghi rõ nguồn trích dẫn số liệu và tên người chịu trách nhiệm về nội dung. Về đạo đức, sử dụng sản phẩm trí tuệ của người khác như của mình là thiếu trung thực, gây hiểu nhầm cho khách hàng về nguồn gốc phân tích, bất kể báo cáo có thu phí hay không.',
    'Khoản 3 Điều 24 ' + TT121_H + '; ' + GT + ' – chuẩn mực trung thực',
    'Các báo cáo phân tích chứng khoán và thị trường, khuyến nghị đầu tư phải ghi rõ nguồn trích dẫn số liệu và tên người chịu trách nhiệm về nội dung báo cáo, khuyến nghị đầu tư chứng khoán.', T121)

add(TP3, 2,
    'Bà H, 68 tuổi, đã nghỉ hưu, cho biết mục tiêu là bảo toàn vốn và có thu nhập đều đặn, không chấp nhận thua lỗ lớn. Nhân viên tư vấn khuyến nghị bà dùng toàn bộ tiền tiết kiệm mua chứng quyền có bảo đảm vì “tỷ suất sinh lời cao, phí giao dịch ưu đãi”. Theo Thông tư 121/2020/TT-BTC, khuyến nghị này:',
    ['Vi phạm, vì tư vấn phải phù hợp với mục tiêu đầu tư và tình hình tài chính của khách hàng',
     'Hợp lệ, nếu bà H ký xác nhận đã đọc tài liệu giới thiệu sản phẩm chứng quyền',
     'Hợp lệ, vì quyết định đầu tư cuối cùng vẫn do bà H tự đưa ra và tự chịu trách nhiệm',
     'Chỉ vi phạm khi chứng quyền được khuyến nghị đáo hạn với giá trị bằng 0'],
    'Khoản 6 Điều 24 TT 121/2020: công ty chứng khoán phải tư vấn đầu tư phù hợp với mục tiêu đầu tư và tình hình tài chính của khách hàng. Chứng quyền có đòn bẩy, rủi ro mất toàn bộ khoản đầu tư, không phù hợp với khách hàng cần bảo toàn vốn. Chữ ký xác nhận đã đọc tài liệu hay việc khách hàng tự quyết định không miễn trừ nghĩa vụ tư vấn phù hợp.',
    'Khoản 6 Điều 24 ' + TT121_H,
    'Công ty chứng khoán phải tư vấn đầu tư phù hợp với mục tiêu đầu tư và tình hình tài chính của khách hàng và phải chịu trách nhiệm về kết quả phân tích và độ tin cậy của thông tin cung cấp cho khách hàng.', T121)

add(TP3, 2,
    'Chuyên viên phân tích C đang hoàn thiện báo cáo khuyến nghị “Bán” cổ phiếu Z. Bộ phận tư vấn tài chính doanh nghiệp của công ty, đang đàm phán hợp đồng tư vấn phát hành với Z, đề nghị C nâng khuyến nghị lên “Mua”. Cách xử lý phù hợp với chuẩn mực độc lập, khách quan là:',
    ['Giữ khuyến nghị theo kết quả phân tích và báo cáo việc bị gây áp lực cho bộ phận kiểm soát tuân thủ',
     'Nâng khuyến nghị lên “Mua” vì lợi ích chung của công ty quan trọng hơn ý kiến của cá nhân',
     'Trì hoãn phát hành báo cáo cho đến khi hợp đồng tư vấn với Z được ký kết xong',
     'Gửi bản nháp cho Z để Z quyết định nội dung khuyến nghị trước khi phát hành'],
    'Chuẩn mực độc lập, khách quan yêu cầu khuyến nghị phải phản ánh đúng kết quả phân tích, không bị chi phối bởi lợi ích của bộ phận tư vấn tài chính doanh nghiệp, bảo lãnh phát hành hay của tổ chức phát hành. Áp lực từ bộ phận khác là xung đột lợi ích cần được báo cáo cho bộ phận kiểm soát tuân thủ; trì hoãn báo cáo vì hợp đồng hoặc để tổ chức phát hành quyết định khuyến nghị đều làm mất tính khách quan.',
    GT + ' – chuẩn mực độc lập, khách quan trong phân tích và tư vấn đầu tư')

add(TP3, 3,
    'Anh T có chứng chỉ hành nghề môi giới chứng khoán, đang làm việc tại công ty chứng khoán A. Ngoài giờ, anh nhận tư vấn đầu tư chứng khoán cho một số nhà đầu tư theo hợp đồng do anh tự ký với tư cách cá nhân, thu phí trực tiếp vào tài khoản của mình, không thông qua A. Theo Luật Chứng khoán, nhận định nào đúng?',
    ['Vi phạm, vì người hành nghề chỉ được hành nghề với tư cách đại diện cho công ty nơi mình làm việc',
     'Không vi phạm, vì chứng chỉ hành nghề môi giới cho phép người sở hữu tư vấn đầu tư chứng khoán',
     'Không vi phạm, nếu anh T kê khai và nộp đầy đủ thuế thu nhập cá nhân đối với khoản phí',
     'Chỉ vi phạm khi các nhà đầu tư đó đồng thời có tài khoản giao dịch tại công ty chứng khoán A'],
    'Khoản 1 Điều 98: người được cấp chứng chỉ hành nghề chỉ được hành nghề với tư cách đại diện cho công ty chứng khoán, công ty quản lý quỹ, chi nhánh công ty nước ngoài tại Việt Nam hoặc công ty đầu tư chứng khoán; điểm c khoản 2 cấm vượt quá phạm vi ủy quyền của công ty. Chứng chỉ môi giới cho phép tư vấn đầu tư nhưng phải thực hiện nhân danh công ty; việc nộp thuế không thay đổi bản chất vi phạm.',
    'Khoản 1, điểm c khoản 2 Điều 98 ' + LCK,
    'Người được cấp chứng chỉ hành nghề chứng khoán chỉ được hành nghề chứng khoán với tư cách đại diện cho công ty chứng khoán hoặc công ty quản lý quỹ đầu tư chứng khoán', LAW)

add(TP3, 3,
    'Chuyên viên phân tích D tổng hợp báo cáo tài chính đã công bố của công ty niêm yết Q, số liệu xuất khẩu ngành do cơ quan thống kê công bố và quan sát trực tiếp lượng xe tải ra vào nhà máy của Q từ đường công cộng; từ đó kết luận doanh thu quý tới của Q sẽ giảm mạnh và đưa ra khuyến nghị bán. Nhận định nào sau đây đúng?',
    ['Được phép, vì kết luận được rút ra từ việc phân tích tổng hợp thông tin công khai và quan sát hợp pháp',
     'Vi phạm, vì kết luận về doanh thu chưa công bố của Q là thông tin nội bộ bị cấm sử dụng',
     'Vi phạm, vì chuyên viên phải xin ý kiến của Q trước khi đưa ra khuyến nghị bán cổ phiếu',
     'Chỉ được phép nếu D chờ đến sau ngày Q công bố báo cáo tài chính quý tới mới khuyến nghị'],
    'Khoản 44 Điều 4: thông tin nội bộ là thông tin liên quan đến tổ chức chưa được công bố mà nếu công bố có thể ảnh hưởng lớn đến giá. D không nhận thông tin chưa công bố nào từ Q hay người nội bộ; kết luận là sản phẩm phân tích của D dựa trên các mảnh thông tin công khai và quan sát hợp pháp, nên được sử dụng để khuyến nghị (cách tiếp cận “ghép mảnh thông tin” trong giáo trình đạo đức nghề nghiệp). Không có quy định buộc xin ý kiến tổ chức phát hành hay chờ báo cáo tài chính.',
    'Khoản 44 Điều 4 ' + LCK + '; ' + GT + ' – sử dụng thông tin trong phân tích, phân biệt với thông tin nội bộ',
    'Thông tin nội bộ là thông tin liên quan đến công ty đại chúng, tổ chức niêm yết, tổ chức đăng ký giao dịch, quỹ đại chúng, công ty đầu tư chứng khoán đại chúng chưa được công bố mà nếu được công bố có thể ảnh hưởng lớn đến giá chứng khoán của tổ chức này.', LAW)

# ---------------- 4. Đăng ký, lưu ký, bù trừ, thanh toán ----------------
add(TP4, 1,
    'Theo Luật Chứng khoán, chứng khoán của công ty đại chúng phải được lưu ký tập trung tại Tổng công ty lưu ký và bù trừ chứng khoán Việt Nam vào thời điểm nào?',
    ['Trước khi thực hiện giao dịch, trừ trường hợp khác theo quy định của Bộ trưởng Bộ Tài chính',
     'Trong thời hạn 30 ngày kể từ ngày chứng khoán được niêm yết lần đầu trên Sở giao dịch',
     'Sau khi hoàn tất đợt thanh toán giao dịch đầu tiên của chứng khoán đó trên hệ thống',
     'Chỉ khi cổ đông có yêu cầu bằng văn bản gửi tổ chức phát hành hoặc thành viên lưu ký'],
    'Khoản 1 Điều 62: chứng khoán của công ty đại chúng và chứng khoán niêm yết, đăng ký giao dịch phải được lưu ký tập trung tại VSDC trước khi thực hiện giao dịch, trừ trường hợp khác theo quy định của Bộ trưởng Bộ Tài chính. Đây là điều kiện để thanh toán chứng khoán bằng bút toán ghi sổ trên tài khoản lưu ký.',
    'Khoản 1 Điều 62 ' + LCK,
    'Chứng khoán của công ty đại chúng và chứng khoán của các tổ chức khác niêm yết, đăng ký giao dịch trên hệ thống giao dịch chứng khoán phải được lưu ký tập trung tại Tổng công ty lưu ký và bù trừ chứng khoán Việt Nam trước khi thực hiện giao dịch', LAW)

add(TP4, 1,
    'Theo Luật Chứng khoán, công ty chứng khoán được đăng ký hoạt động lưu ký chứng khoán khi:',
    ['Được cấp phép thực hiện nghiệp vụ môi giới chứng khoán',
     'Được cấp phép thực hiện nghiệp vụ tự doanh chứng khoán',
     'Có vốn điều lệ đã góp từ 1.000 tỷ đồng trở lên',
     'Hoạt động kinh doanh có lãi trong 02 năm gần nhất'],
    'Khoản 2 Điều 57: công ty chứng khoán được đăng ký hoạt động lưu ký chứng khoán khi được cấp phép nghiệp vụ môi giới chứng khoán. Điều kiện về tỷ lệ an toàn vốn, kinh doanh có lãi năm gần nhất áp dụng cho ngân hàng thương mại, chi nhánh ngân hàng nước ngoài (khoản 1 Điều 57).',
    'Khoản 2 Điều 57 ' + LCK,
    'Công ty chứng khoán được đăng ký hoạt động lưu ký chứng khoán khi được cấp phép thực hiện nghiệp vụ môi giới chứng khoán.', LAW)

add(TP4, 2,
    'Luật Chứng khoán quy định thanh toán giao dịch chứng khoán phải tuân thủ nguyên tắc chuyển giao chứng khoán đồng thời với thanh toán tiền (DVP). Nguyên tắc này chủ yếu nhằm loại trừ rủi ro nào?',
    ['Một bên đã giao chứng khoán hoặc đã trả tiền nhưng không nhận được phần đối ứng',
     'Giá chứng khoán biến động bất lợi trong khoảng thời gian từ khi khớp lệnh đến khi thanh toán',
     'Tổ chức phát hành chứng khoán mất khả năng thanh toán nợ gốc và lãi cho nhà đầu tư',
     'Hệ thống giao dịch của Sở giao dịch gặp sự cố kỹ thuật trong phiên khớp lệnh'],
    'Khoản 2 Điều 63: thanh toán chứng khoán thực hiện trên tài khoản lưu ký tại VSDC, thanh toán tiền qua ngân hàng thanh toán và phải chuyển giao chứng khoán đồng thời với thanh toán tiền. Theo giáo trình, DVP loại trừ rủi ro tiền gốc (một bên đã thực hiện nghĩa vụ mà không nhận được phần đối ứng); rủi ro biến động giá, rủi ro tín dụng của tổ chức phát hành và rủi ro sự cố hệ thống giao dịch không được loại trừ bởi DVP.',
    'Khoản 2 Điều 63 ' + LCK + '; ' + GT + ' – nguyên tắc DVP và rủi ro thanh toán',
    'thanh toán tiền giao dịch chứng khoán được thực hiện qua ngân hàng thanh toán và phải tuân thủ nguyên tắc chuyển giao chứng khoán đồng thời với thanh toán tiền.', LAW)

add(TP4, 2,
    'Thành viên lưu ký L thường xuyên vi phạm nghĩa vụ của thành viên lưu ký theo quy chế của Tổng công ty lưu ký và bù trừ chứng khoán Việt Nam (VSDC). Theo Luật Chứng khoán, biện pháp nào sau đây được áp dụng?',
    ['VSDC đình chỉ hoạt động lưu ký chứng khoán của L tối đa 90 ngày',
     'VSDC thu hồi ngay Giấy chứng nhận đăng ký hoạt động lưu ký của L',
     'UBCKNN đình chỉ hoạt động lưu ký chứng khoán của L tối đa 12 tháng',
     'Sở giao dịch chứng khoán hủy bỏ tư cách thành viên lưu ký của L'],
    'Điểm a khoản 1 Điều 60: VSDC đình chỉ hoạt động lưu ký của thành viên lưu ký tối đa 90 ngày khi thường xuyên vi phạm nghĩa vụ thành viên lưu ký. Giấy chứng nhận đăng ký hoạt động lưu ký do UBCKNN cấp và thu hồi (khoản 2 Điều 60), chẳng hạn khi hết thời hạn đình chỉ mà không khắc phục được vi phạm. Sở giao dịch không quản lý thành viên lưu ký.',
    'Điểm a khoản 1 Điều 60 ' + LCK,
    'Tổng công ty lưu ký và bù trừ chứng khoán Việt Nam đình chỉ hoạt động lưu ký chứng khoán của thành viên lưu ký tối đa là 90 ngày trong các trường hợp sau đây', LAW)

add(TP4, 2,
    'Một doanh nghiệp đề nghị Tổng công ty lưu ký và bù trừ chứng khoán Việt Nam (VSDC) cung cấp bản sao thông tin sở hữu chứng khoán của nhà đầu tư H để phục vụ việc đòi nợ, trong khi H không đồng ý. Theo Luật Chứng khoán, VSDC phải:',
    ['Từ chối, vì không có sự đồng ý của H và không phải yêu cầu của cơ quan có thẩm quyền',
     'Cung cấp, vì thông tin sở hữu chứng khoán đăng ký tập trung là thông tin công khai',
     'Cung cấp, nếu doanh nghiệp nộp đủ giá dịch vụ trích lục thông tin theo biểu phí',
     'Chuyển đề nghị cho thành viên lưu ký của H tự quyết định việc cung cấp thông tin'],
    'Điểm g khoản 2 Điều 55: VSDC có trách nhiệm bảo mật thông tin sở hữu của khách hàng, từ chối phong tỏa, cầm giữ, trích chuyển tài sản, trích lục, sao chép thông tin sở hữu chứng khoán của khách hàng mà không có sự đồng ý của khách hàng, trừ trường hợp theo yêu cầu của cơ quan có thẩm quyền hoặc của kiểm toán viên kiểm toán báo cáo tài chính theo quy định. Thành viên lưu ký cũng có nghĩa vụ bảo mật tương tự (điểm a khoản 3 Điều 56).',
    'Điểm g khoản 2 Điều 55 ' + LCK,
    'từ chối việc phong tỏa, cầm giữ, trích chuyển tài sản, trích lục, sao chép thông tin sở hữu chứng khoán của khách hàng mà không có sự đồng ý của khách hàng, trừ trường hợp theo yêu cầu của cơ quan có thẩm quyền', LAW)

add(TP4, 2,
    'Vào ngày thanh toán, thành viên lưu ký Z tạm thời mất khả năng thanh toán tiền cho các giao dịch mua chứng khoán của khách hàng. Theo Luật Chứng khoán, nguồn được sử dụng để thanh toán thay cho Z là:',
    ['Quỹ hỗ trợ thanh toán do các thành viên lưu ký đóng góp, do VSDC quản lý',
     'Tiền gửi giao dịch chứng khoán của các khách hàng khác đang có tại Z',
     'Quỹ bảo vệ nhà đầu tư do Sở giao dịch chứng khoán Việt Nam quản lý',
     'Vốn tự có của ngân hàng thanh toán theo hợp đồng ký với VSDC'],
    'Khoản 1, 2 Điều 66: quỹ hỗ trợ thanh toán hình thành từ đóng góp của các thành viên lưu ký để thanh toán thay khi thành viên lưu ký tạm thời mất khả năng thanh toán; quỹ do VSDC quản lý, tách biệt với tài sản của VSDC. Tiền của khách hàng là tài sản của khách hàng, không được dùng thanh toán nợ của thành viên (Điều 65); ngân hàng thanh toán chỉ cung cấp dịch vụ thanh toán tiền.',
    'Điều 66 ' + LCK,
    'Quỹ hỗ trợ thanh toán được hình thành từ sự đóng góp của các thành viên lưu ký để thanh toán thay cho thành viên lưu ký trong trường hợp thành viên lưu ký tạm thời mất khả năng thanh toán giao dịch chứng khoán.', LAW)

# C7-031: bù trừ đa phương tiền
trades = [('P', 'Q', 10), ('Q', 'R', 8), ('R', 'P', 6), ('P', 'R', 3)]  # (bên mua, bên bán, tỷ đồng)
net = {m: 0 for m in 'PQR'}
for b, s, v in trades:
    net[b] -= v; net[s] += v
gross = sum(v for *_, v in trades)
paid = -sum(x for x in net.values() if x < 0)
abs_net = sum(abs(x) for x in net.values())
saving = gross - paid
assert net == {'P': -7, 'Q': 2, 'R': 5} and gross == 27 and paid == 7 and abs_net == 14 and saving == 20
add(TP4, 3,
    'Giả định VSDC bù trừ đa phương ròng nghĩa vụ tiền theo từng thành viên trong cùng kỳ thanh toán (bỏ qua phí, thuế). Trong ngày T, khách hàng của thành viên P mua của khách hàng của Q 10 tỷ đồng; khách hàng của Q mua của khách hàng của R 8 tỷ đồng; khách hàng của R mua của khách hàng của P 6 tỷ đồng; khách hàng của P mua của khách hàng của R 3 tỷ đồng. So với thanh toán riêng từng giao dịch, tổng giá trị tiền phải chuyển giảm được nhờ bù trừ là:',
    ['20 tỷ đồng', '7 tỷ đồng', '13 tỷ đồng', '14 tỷ đồng'],
    'Thanh toán gộp: 10 + 8 + 6 + 3 = 27 tỷ đồng. Vị thế ròng: P phải trả 13 − 6 = 7 tỷ; Q nhận 10 − 8 = 2 tỷ; R nhận 11 − 6 = 5 tỷ. Sau bù trừ chỉ P chuyển 7 tỷ (bằng tổng số Q và R nhận). Giảm được 27 − 7 = 20 tỷ đồng. Lỗi thường gặp: nhầm với số tiền còn phải chuyển (7 tỷ); cộng giá trị tuyệt đối các vị thế ròng (14 tỷ) hoặc lấy 27 − 14 = 13 tỷ (tính cả phía nhận như phía chuyển).',
    GT + ' – bù trừ đa phương ròng trong thanh toán giao dịch chứng khoán',
    rank=[saving, paid, gross - abs_net, abs_net])

# C7-032: nghĩa vụ ròng chứng khoán và tiền của một thành viên
pa, pb = 25_000, 40_000
buy_a, sell_a, buy_b, sell_b = 120_000, 85_000, 15_000, 40_000
net_a, net_b = buy_a - sell_a, buy_b - sell_b
cash_net = (sell_a * pa + sell_b * pb) - (buy_a * pa + buy_b * pb)
cash_a_only = sell_a * pa - buy_a * pa
assert net_a == 35_000 and net_b == -25_000 and cash_net == 125_000_000 and cash_a_only == -875_000_000
add(TP4, 3,
    'Giả định VSDC bù trừ đa phương ròng nghĩa vụ chứng khoán theo từng mã và nghĩa vụ tiền theo từng thành viên (bỏ qua phí, thuế). Trong ngày T, khách hàng của thành viên lưu ký X mua 120.000 cổ phiếu AAA và bán 85.000 cổ phiếu AAA ở giá 25.000 đồng; mua 15.000 cổ phiếu BBB và bán 40.000 cổ phiếu BBB ở giá 40.000 đồng. Nghĩa vụ thanh toán ròng của X là:',
    ['Nhận 35.000 cổ phiếu AAA, giao 25.000 cổ phiếu BBB; nhận ròng 125 triệu đồng',
     'Nhận 35.000 cổ phiếu AAA, giao 25.000 cổ phiếu BBB; trả ròng 125 triệu đồng',
     'Nhận 35.000 cổ phiếu AAA, giao 25.000 cổ phiếu BBB; trả ròng 875 triệu đồng',
     'Nhận ròng 10.000 cổ phiếu (bù trừ chung hai mã); nhận ròng 125 triệu đồng'],
    'Chứng khoán bù trừ theo từng mã: AAA 120.000 − 85.000 = nhận 35.000; BBB 15.000 − 40.000 = giao 25.000 (không bù trừ chéo giữa hai mã). Tiền: phải trả 120.000 × 25.000 + 15.000 × 40.000 = 3.600 triệu; được nhận 85.000 × 25.000 + 40.000 × 40.000 = 3.725 triệu → nhận ròng 125 triệu đồng. Lỗi thường gặp: nhầm chiều tiền; chỉ tính tiền của mã AAA (trả 875 triệu); cộng chung số lượng hai mã.',
    GT + ' – bù trừ đa phương ròng chứng khoán và tiền')

# C7-033: thời hạn 12 tháng sau khi được cấp GCN lưu ký
d0 = dt.date(2026, 1, 15)
d_deadline = d0.replace(year=d0.year + 1)
assert d_deadline == dt.date(2027, 1, 15)
add(TP4, 3,
    'Ngày 15/01/2026, ngân hàng thương mại G được UBCKNN cấp Giấy chứng nhận đăng ký hoạt động lưu ký chứng khoán. Đến tháng 11/2026, G vẫn chưa làm thủ tục đăng ký thành viên lưu ký tại VSDC. Theo Luật Chứng khoán, nhận định nào đúng?',
    ['G còn hạn đến 15/01/2027 để đăng ký thành viên và hoạt động lưu ký; quá hạn sẽ bị UBCKNN thu hồi Giấy chứng nhận',
     'G đã quá hạn 06 tháng kể từ ngày được cấp Giấy chứng nhận nên bị VSDC đình chỉ hoạt động lưu ký 90 ngày',
     'G đã quá hạn 30 ngày kể từ ngày được cấp Giấy chứng nhận nên Giấy chứng nhận đương nhiên hết hiệu lực',
     'G không bị giới hạn thời gian, chỉ cần đăng ký thành viên trước khi nhận lưu ký cho khách hàng đầu tiên'],
    'Khoản 2 Điều 59: trong 12 tháng kể từ ngày được cấp Giấy chứng nhận, tổ chức phải đăng ký thành viên lưu ký tại VSDC và tiến hành hoạt động lưu ký; hạn của G là 15/01/2027. Điểm b khoản 2 Điều 60: UBCKNN thu hồi Giấy chứng nhận nếu không tiến hành hoạt động lưu ký trong thời hạn này. Biện pháp đình chỉ 90 ngày của VSDC chỉ áp dụng với thành viên lưu ký vi phạm nghĩa vụ.',
    'Khoản 2 Điều 59, điểm b khoản 2 Điều 60 ' + LCK,
    'Trong thời hạn 12 tháng kể từ ngày được cấp Giấy chứng nhận đăng ký hoạt động lưu ký chứng khoán, công ty chứng khoán, ngân hàng thương mại, chi nhánh ngân hàng nước ngoài phải làm thủ tục đăng ký thành viên lưu ký', LAW)

# ---------------- 5. Công bố thông tin ----------------
add(TP5, 1,
    'Theo Luật Chứng khoán, đối tượng nào sau đây KHÔNG thuộc đối tượng công bố thông tin?',
    ['Cá nhân sở hữu 3% cổ phiếu có quyền biểu quyết, không phải người nội bộ',
     'Cổ đông sáng lập trong thời gian bị hạn chế chuyển nhượng của công ty đại chúng',
     'Nhà đầu tư sở hữu từ 5% trở lên chứng chỉ quỹ của một quỹ đóng',
     'Tổng công ty lưu ký và bù trừ chứng khoán Việt Nam'],
    'Khoản 1 Điều 118 liệt kê đối tượng công bố thông tin: công ty đại chúng; tổ chức phát hành, niêm yết trái phiếu; công ty chứng khoán, công ty quản lý quỹ; Sở giao dịch chứng khoán, VSDC; cổ đông lớn (từ 5%), nhà đầu tư sở hữu từ 5% chứng chỉ quỹ đóng; cổ đông sáng lập trong thời gian bị hạn chế chuyển nhượng; người nội bộ và người có liên quan… Cá nhân sở hữu 3%, không phải người nội bộ hay người có liên quan, không thuộc diện này.',
    'Khoản 1 Điều 118 ' + LCK,
    'Cổ đông lớn, nhóm người có liên quan sở hữu từ 5% trở lên số cổ phiếu có quyền biểu quyết của công ty đại chúng; nhà đầu tư, nhóm người có liên quan sở hữu từ 5% trở lên chứng chỉ quỹ của quỹ đóng', LAW)

add(TP5, 1,
    'Theo Thông tư 96/2020/TT-BTC, trong thời hạn bao lâu kể từ ngày UBCKNN xác nhận hoàn tất việc đăng ký công ty đại chúng, công ty phải công bố về việc trở thành công ty đại chúng?',
    ['07 ngày', '24 giờ', '10 ngày', '30 ngày'],
    'Điều 9 TT 96/2020: trong thời hạn 07 ngày kể từ ngày UBCKNN xác nhận hoàn tất việc đăng ký công ty đại chúng, công ty phải công bố về việc trở thành công ty đại chúng kèm bản công bố thông tin trên trang thông tin điện tử của công ty và hệ thống công bố thông tin của UBCKNN.',
    'Điều 9 ' + TT96_NOTE,
    'Trong thời hạn 07 ngày kể từ ngày Ủy ban Chứng khoán Nhà nước xác nhận hoàn tất việc đăng ký công ty đại chúng theo quy định tại khoản 3 Điều 32 Luật Chứng khoán, công ty đại chúng có trách nhiệm công bố về việc trở thành công ty đại chúng', T96)

add(TP5, 1,
    'Theo Thông tư 96/2020/TT-BTC, đối tượng công bố thông tin được tạm hoãn công bố thông tin trong trường hợp nào?',
    ['Có lý do bất khả kháng như thiên tai, hỏa hoạn, chiến tranh, dịch bệnh',
     'Thông tin có thể làm giá cổ phiếu của công ty giảm mạnh trong ngắn hạn',
     'Người đại diện theo pháp luật của công ty đang công tác ở nước ngoài',
     'Công ty đang đàm phán một hợp đồng lớn nhưng chưa ký kết chính thức'],
    'Khoản 1 Điều 8 TT 96/2020: chỉ được tạm hoãn vì lý do bất khả kháng như thiên tai, hỏa hoạn, chiến tranh, dịch bệnh; phải báo cáo UBCKNN, Sở giao dịch ngay khi xảy ra sự kiện, đồng thời công bố việc tạm hoãn, và công bố đầy đủ ngay sau khi khắc phục. Khi người đại diện theo pháp luật vắng mặt, người được ủy quyền hoặc thành viên giữ chức vụ cao nhất của Ban Điều hành thực hiện công bố (Điều 6).',
    'Khoản 1 Điều 8 ' + TT96_NOTE,
    'Đối tượng công bố thông tin được tạm hoãn công bố thông tin trong trường hợp vì những lý do bất khả kháng như: Thiên tai, hỏa hoạn, chiến tranh, dịch bệnh', T96)

add(TP5, 2,
    'Theo Thông tư 96/2020/TT-BTC, sự kiện nào sau đây công ty đại chúng phải công bố thông tin bất thường trong thời hạn 24 giờ?',
    ['Hội đồng quản trị quyết định mức cổ tức, hình thức và thời gian trả cổ tức',
     'Công ty hoàn thành báo cáo tình hình quản trị công ty 06 tháng đầu năm',
     'Công ty hoàn thành báo cáo tài chính quý theo kỳ kế toán thông thường',
     'Công ty hoàn thành báo cáo thường niên của năm tài chính trước'],
    'Điểm đ khoản 1 Điều 11 TT 96/2020: quyết định về mức cổ tức, hình thức trả cổ tức, thời gian trả cổ tức là sự kiện công bố thông tin bất thường trong 24 giờ. Báo cáo tình hình quản trị (30 ngày từ khi kết thúc 06 tháng, Điều 10), báo cáo tài chính quý và báo cáo thường niên là thông tin định kỳ với thời hạn riêng.',
    'Điểm đ khoản 1 Điều 11 ' + TT96_NOTE,
    'Quyết định về mức cổ tức, hình thức trả cổ tức, thời gian trả cổ tức; quyết định tách, gộp cổ phiếu', T96)

add(TP5, 2,
    'Theo Thông tư 96/2020/TT-BTC, thông tin công bố định kỳ của công ty đại chúng phải được lưu giữ dưới dạng văn bản (nếu có) và dữ liệu điện tử tối thiểu bao lâu, và phải truy cập được trên trang thông tin điện tử của công ty tối thiểu bao lâu?',
    ['10 năm và 05 năm', '05 năm và 03 năm', '10 năm và 10 năm', '20 năm và 05 năm'],
    'Điểm a khoản 5 Điều 4 TT 96/2020: thông tin định kỳ, thông tin về việc đăng ký công ty đại chúng lưu giữ dạng văn bản (nếu có) và dữ liệu điện tử tối thiểu 10 năm, đồng thời lưu giữ và truy cập được trên trang thông tin điện tử tối thiểu 05 năm. Thông tin bất thường, theo yêu cầu: truy cập được trên trang thông tin điện tử tối thiểu 05 năm (điểm b).',
    'Điểm a khoản 5 Điều 4 ' + TT96_NOTE,
    'Các thông tin công bố định kỳ, thông tin về việc đăng ký công ty đại chúng phải được lưu giữ dưới dạng văn bản (nếu có) và dữ liệu điện tử tối thiểu 10 năm. Các thông tin này phải được lưu giữ và truy cập được trên trang thông tin điện tử của đối tượng công bố thông tin tối thiểu là 05 năm', T96)

add(TP5, 2,
    'Ngày 02/11/2026, công ty niêm yết R thay đổi người được ủy quyền công bố thông tin, việc ủy quyền mới có hiệu lực ngay trong ngày. Theo Thông tư 96/2020/TT-BTC, R phải báo cáo thông tin về người thực hiện công bố thông tin cho UBCKNN và Sở giao dịch chứng khoán trong thời hạn:',
    ['24 giờ kể từ khi việc ủy quyền có hiệu lực',
     '03 ngày làm việc kể từ ngày ký giấy ủy quyền',
     '05 ngày làm việc kể từ khi ủy quyền có hiệu lực',
     '10 ngày kể từ ngày Hội đồng quản trị quyết định'],
    'Điểm b khoản 1 Điều 6 TT 96/2020: tổ chức phải báo cáo, báo cáo lại thông tin về người thực hiện công bố thông tin (kèm Giấy ủy quyền, Bản cung cấp thông tin) trong 24 giờ kể từ khi việc chỉ định, ủy quyền hoặc thay đổi người thực hiện công bố thông tin có hiệu lực.',
    'Điểm b khoản 1 Điều 6 ' + TT96_NOTE,
    'Tổ chức phải báo cáo, báo cáo lại thông tin về người thực hiện công bố thông tin cho Ủy ban Chứng khoán Nhà nước và Sở giao dịch chứng khoán trong thời hạn 24 giờ kể từ khi việc chỉ định, ủy quyền hoặc thay đổi người thực hiện công bố thông tin có hiệu lực.', T96)

add(TP5, 2,
    'Theo Thông tư 96/2020/TT-BTC, tổ chức niêm yết cổ phiếu phải thực hiện công bố thông tin, báo cáo trên những phương tiện nào?',
    ['Trang thông tin điện tử của công ty, hệ thống công bố thông tin của UBCKNN và phương tiện của Sở giao dịch',
     'Trang thông tin điện tử của công ty và một tờ báo in phát hành toàn quốc trong 03 số liên tiếp',
     'Hệ thống công bố thông tin của UBCKNN và trang thông tin điện tử của VSDC',
     'Chỉ trang thông tin điện tử của Sở giao dịch nơi niêm yết, không cần trang của công ty'],
    'Khoản 4 Điều 7 TT 96/2020: tổ chức niêm yết cổ phiếu công bố thông tin trên các phương tiện tại điểm a, b, c khoản 1, tức trang thông tin điện tử của tổ chức, hệ thống công bố thông tin của UBCKNN và trang thông tin điện tử (phương tiện công bố thông tin) của Sở giao dịch chứng khoán. Trang của VSDC dành cho VSDC tự công bố (khoản 6); báo in chỉ là phương tiện thông tin đại chúng khác (điểm đ khoản 1), không bắt buộc.',
    'Khoản 1, khoản 4 Điều 7 ' + TT96_NOTE,
    'Tổ chức niêm yết cổ phiếu, tổ chức niêm yết trái phiếu doanh nghiệp, tổ chức đăng ký giao dịch, công ty chứng khoán thành viên, quỹ đại chúng niêm yết, công ty đầu tư chứng khoán đại chúng thực hiện công bố thông tin, báo cáo trên các phương tiện quy định tại điểm a, b và c khoản 1 Điều này.', T96)

# C7-041: ngày muộn nhất công bố ngày ĐKCC
dkcc = dt.date(2026, 11, 26)
def minus_workdays(d, n):
    while n:
        d -= dt.timedelta(days=1)
        if d.weekday() < 5: n -= 1
    return d
k_date = dkcc - dt.timedelta(days=10)
d_20 = dkcc - dt.timedelta(days=20)
d_10wd = minus_workdays(dkcc, 10)
d_5wd = minus_workdays(dkcc, 5)
assert dkcc.weekday() == 3 and k_date == dt.date(2026, 11, 16) and d_20 == dt.date(2026, 11, 6) and d_10wd == dt.date(2026, 11, 12) and d_5wd == dt.date(2026, 11, 19)
TH = ['Thứ Hai', 'Thứ Ba', 'Thứ Tư', 'Thứ Năm', 'Thứ Sáu', 'Thứ Bảy', 'Chủ nhật']
fd = lambda d: f'{TH[d.weekday()]}, {d.day:02d}/{d.month:02d}/{d.year}'
add(TP5, 3,
    'Hội đồng quản trị công ty niêm yết S quyết định trả cổ tức bằng tiền, ngày đăng ký cuối cùng dự kiến là Thứ Năm, 26/11/2026 (không nhằm mục đích họp Đại hội đồng cổ đông). Coi thời hạn “tối thiểu n ngày trước” là ngày đăng ký cuối cùng trừ đi n ngày dương lịch. Theo Thông tư 96/2020/TT-BTC, ngày muộn nhất S phải công bố thông tin về ngày đăng ký cuối cùng dự kiến là:',
    [fd(k_date), fd(d_20), fd(d_10wd), fd(d_5wd)],
    'Điểm a khoản 4 Điều 11 TT 96/2020: công bố ngày đăng ký cuối cùng dự kiến thực hiện quyền cho cổ đông hiện hữu tối thiểu 10 ngày trước ngày đăng ký cuối cùng dự kiến → 26/11 − 10 ngày = 16/11/2026. Mốc 20 ngày (06/11) chỉ áp dụng khi ngày đăng ký cuối cùng để tham dự họp Đại hội đồng cổ đông (điểm b). Tính theo ngày làm việc là sai (10 ngày làm việc → 12/11; 05 ngày làm việc → 19/11).',
    'Điểm a khoản 4 Điều 11 ' + TT96_NOTE,
    'Công ty đại chúng công bố thông tin về ngày đăng ký cuối cùng dự kiến thực hiện quyền cho cổ đông hiện hữu tối thiểu 10 ngày trước ngày đăng ký cuối cùng dự kiến, trừ trường hợp quy định tại điểm b khoản này', T96,
    rank=[k_date.toordinal(), d_20.toordinal(), d_10wd.toordinal(), d_5wd.toordinal()])

assert dt.date(2026, 11, 15).weekday() == 6
add(TP5, 3,
    'Chủ nhật, 15/11/2026, công ty niêm yết V nhận được quyết định khởi tố đối với Tổng giám đốc của công ty (sự kiện phải công bố thông tin bất thường trong 24 giờ). Theo Thông tư 96/2020/TT-BTC, V phải thực hiện như thế nào?',
    ['Công bố trên trang thông tin điện tử của công ty, rồi thực hiện đầy đủ nghĩa vụ công bố vào Thứ Hai, 16/11/2026',
     'Chưa phải công bố gì; chỉ công bố trên mọi phương tiện trong 24 giờ kể từ đầu giờ làm việc Thứ Hai',
     'Phải công bố đồng thời trên trang của công ty, UBCKNN và Sở giao dịch ngay trong ngày Chủ nhật',
     'Được tạm hoãn công bố vì sự kiện phát sinh vào ngày nghỉ, cho đến khi có kết luận điều tra'],
    'Điểm n khoản 1 Điều 11: nhận quyết định khởi tố người nội bộ phải công bố bất thường trong 24 giờ. Khoản 7 Điều 7: nếu nghĩa vụ phát sinh vào ngày nghỉ, ngày lễ, tổ chức niêm yết (đối tượng tại khoản 4) công bố trên trang thông tin điện tử của mình (điểm a khoản 1) và thực hiện đầy đủ nghĩa vụ vào ngày làm việc liền sau. Ngày nghỉ không phải lý do bất khả kháng để tạm hoãn (Điều 8).',
    'Khoản 7 Điều 7, điểm n khoản 1 Điều 11 ' + TT96_NOTE,
    'đối tượng nêu tại khoản 3 và khoản 4 Điều này thực hiện công bố thông tin trên phương tiện quy định tại điểm a khoản 1 Điều này và thực hiện đầy đủ nghĩa vụ công bố thông tin theo quy định pháp luật vào ngày làm việc liền sau ngày nghỉ, ngày lễ.', T96)


# ---------------- kiểm tra & ghi file ----------------
def norm_ws(s):
    return re.sub(r'\s+', ' ', unicodedata.normalize('NFC', s)).strip()


_cache = {}
def doc(name):
    if name not in _cache:
        raw = (DOCS / name).read_text(encoding='utf-8')
        clean = '\n'.join(l for l in raw.splitlines() if not re.search(r'CÔNG BÁO/Số|^\s*\d{1,4}\s*$', l))
        _cache[name] = norm_ws(clean)
    return _cache[name]


assert len(Q) == 42, len(Q)
# vị trí đáp án: chia đều, không lặp quá 2 lần liên tiếp
rnd = random.Random(7)
while True:
    seq = [i % 4 for i in range(42)]
    rnd.shuffle(seq)
    if all(not (seq[i] == seq[i - 1] == seq[i - 2]) for i in range(2, 42)):
        break
out, ranks = [], []
for n, (x, a) in enumerate(zip(Q, seq), 1):
    if x['quote']:
        assert len(x['quote']) <= 300, (n, len(x['quote']))
        assert norm_ws(x['quote']) in doc(x['src']), (n, x['quote'][:60])
    if x['rank']:
        ranks.append(sorted(x['rank']).index(x['rank'][0]) + 1)
    o = x['o'][1:]
    o.insert(a, x['o'][0])
    for s in o:
        assert not re.search(r'(\b[A-Da-d]\s*(và|,|&)\s*[A-Da-d]\b)|tất cả|không (có )?(phương án|đáp án|ý|câu) nào', s, re.I), s
    out.append({'id': f'C7-{n:03d}', 'part': 'CM', 'subject': 'CB', 'topic': x['topic'], 'level': x['level'],
                'q': x['q'], 'o': o, 'a': a, 'e': x['e'], 'basis': x['basis'], 'quote': x['quote'], 'src': x['src'],
                'as_of': '2026-11'})

# gần trùng với ngân hàng câu hỏi hiện có (q và q+phương án)
words = lambda s: set(re.findall(r'\w+', s.lower()))
old = []
for f in sorted(SRC.glob('*.json')):
    if f.name.startswith(('cm_', 'luat_')) and f.name != 'cm_7.json':
        old += json.loads(f.read_text(encoding='utf-8'))
worst = (0, '', '')
for r in out:
    for y in old + [z for z in out if z['id'] != r['id']]:
        jq = len(words(r['q']) & words(y['q'])) / len(words(r['q']) | words(y['q']))
        a1, a2 = words(r['q'] + ' ' + ' '.join(r['o'])), words(y['q'] + ' ' + ' '.join(y['o']))
        j = max(jq, len(a1 & a2) / len(a1 | a2))
        if j > worst[0]: worst = (j, r['id'], y['id'])
        assert j <= 0.7, (r['id'], y['id'], j)

OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
from collections import Counter as C
print('ghi', OUT, len(out), 'câu')
print('chủ đề', dict(C(r['topic'][:30] for r in out)))
print('mức độ', dict(sorted(C(r['level'] for r in out).items())), '| theo chủ đề',
      {t[:12]: dict(sorted(C(r['level'] for r in out if r['topic'] == t).items())) for t in [TP1, TP2, TP3, TP4, TP5]})
print('đáp án', dict(sorted(C(r['a'] for r in out).items())), '| có trích dẫn', sum(bool(r['quote']) for r in out))
print('thứ hạng đáp án số', ranks, '| Jaccard lớn nhất %.2f %s~%s' % worst)
for r in out:
    L = [len(s) for s in r['o']]
    if max(L) > 1.5 * min(L) and min(L) > 15: print('độ dài lệch', r['id'], L)
    if L[r['a']] == max(L) and max(L) - sorted(L)[-2] > 10: print('đáp án dài hẳn', r['id'], L)
