"""Build cm_5.json (40 câu MG: giao dịch cổ phiếu, giao dịch trái phiếu). Run: python3 -I build.py
Mọi số liệu được tính lại ở đây; chk() đối chiếu với kết quả tính tay."""
import json, math, random, datetime

D = '/home/user/cchn_moi/web/data/src/'
OUT = D + 'cm_5.json'
GT = 'Giáo trình SRTC (khung chương trình)'
T1 = 'Giao dịch cổ phiếu trên thị trường chứng khoán'
T2 = 'Giao dịch trái phiếu trên thị trường chứng khoán'


def vn(x, d=0):
    s = f"{x:,.{d}f}".replace(',', '#').replace('.', ',').replace('#', '.')
    return s.replace('-', '−')


def pc(x, d=2, sign=False):
    s = vn(x * 100, d) + '%'
    return '+' + s if sign and x > 0 else s


def dong(x):
    return vn(x) + ' đồng'


def cp(x):
    return vn(x) + ' cổ phiếu'


def chk(v, hand, tol=1e-6):
    assert abs(v - hand) <= tol * max(1, abs(hand)), (v, hand)


Q = []


def add(topic, lv, q, o, e, basis, key=None, val=None):
    """o[0] là đáp án đúng. key: khóa sắp xếp tăng dần của 4 phương án (câu số); val: giá trị đúng."""
    assert len(o) == 4 and len(set(o)) == 4, o
    if key is not None:
        assert len(set(key)) == 4, key
    Q.append(dict(topic=topic, lv=lv, q=q, o=o, e=e, basis=basis, key=key, val=val))


def addn(topic, lv, q, vals, fmt, e, basis):
    add(topic, lv, q, [fmt(v) for v in vals], e, basis, key=list(vals), val=vals[0])


def tick(p):  # bước giá giả định trong đề (HOSE-style)
    return 10 if p < 10000 else 50 if p < 50000 else 100


def auction(bm, buys, sm, sells, prices):
    """Khớp định kỳ: (giá, KL mua cộng dồn, KL bán cộng dồn, KL khớp)."""
    out = []
    for p in prices:
        cb = bm + sum(q for pr, q in buys.items() if pr >= p)
        cs = sm + sum(q for pr, q in sells.items() if pr <= p)
        out.append((p, cb, cs, min(cb, cs)))
    return out


def bond_price(F, c, y, n, m=1):
    """c, y theo năm; n năm; m kỳ/năm."""
    cpn, r, N = F * c / m, y / m, int(n * m)
    return sum(cpn / (1 + r) ** t for t in range(1, N + 1)) + F / (1 + r) ** N


# =================== GIAO DỊCH CỔ PHIẾU: cấp độ 1 ===================
add(T1, 1,
    'Lệnh thị trường được thực hiện toàn bộ hoặc một phần ngay khi nhập vào hệ thống, phần khối lượng còn lại không thực hiện được bị hủy ngay sau khi so khớp, được gọi là lệnh:',
    ['MAK (Match and Kill)', 'MOK (Match or Kill)', 'ATC (At the Close)', 'LO (Limit Order)'],
    'Lệnh MAK có thể khớp toàn bộ hoặc một phần, phần chưa khớp bị hủy ngay. Lệnh MOK phải khớp toàn bộ ngay khi nhập, nếu không sẽ bị hủy toàn bộ. ATC là lệnh tại mức giá đóng cửa trong phiên định kỳ đóng cửa; LO là lệnh giới hạn, phần chưa khớp tiếp tục chờ trên sổ lệnh.',
    'Đặc điểm các loại lệnh thị trường MAK, MOK')
add(T1, 1,
    'Phương thức khớp lệnh định kỳ là phương thức giao dịch trong đó:',
    ['Các lệnh được tập hợp trong một khoảng thời gian và so khớp tại một thời điểm với một mức giá duy nhất',
     'Các lệnh được so khớp ngay khi nhập vào hệ thống, tại mức giá của lệnh đối ứng đang chờ trên sổ lệnh',
     'Bên mua và bên bán tự thỏa thuận khối lượng, giá rồi nhập kết quả giao dịch vào hệ thống của Sở',
     'Các lệnh được so khớp tại mức giá đóng cửa trong phiên giao dịch sau giờ, khi thị trường đã đóng cửa'],
    'Khớp lệnh định kỳ: lệnh được tích lũy trong phiên (ví dụ phiên mở cửa, đóng cửa) và so khớp một lần tại thời điểm kết thúc phiên theo một mức giá khớp duy nhất (thường là mức giá đạt khối lượng lớn nhất). Khớp ngay tại giá lệnh đối ứng đang chờ là khớp lệnh liên tục; tự thỏa thuận rồi nhập kết quả là giao dịch thỏa thuận; khớp tại giá đóng cửa sau giờ là phiên giao dịch sau giờ (lệnh PLO).',
    'Các phương thức giao dịch: khớp lệnh định kỳ, khớp lệnh liên tục, thỏa thuận')
add(T1, 1,
    'Nhà đầu tư muốn đặt lệnh bán cổ phiếu tại mức giá đóng cửa sẽ được xác định trong phiên khớp lệnh định kỳ đóng cửa, không cần ghi mức giá cụ thể. Loại lệnh phù hợp là:',
    ['Lệnh ATC', 'Lệnh ATO', 'Lệnh MAK', 'Lệnh MOK'],
    'Lệnh ATC (At The Close) là lệnh mua/bán tại mức giá đóng cửa, chỉ được nhập trong phiên khớp lệnh định kỳ đóng cửa và được ưu tiên trước lệnh LO khi so khớp. ATO dùng cho phiên định kỳ mở cửa; MAK, MOK là lệnh thị trường được thực hiện ngay trong phiên khớp lệnh liên tục.',
    'Đặc điểm lệnh ATC')
add(T1, 1,
    'Trong khớp lệnh tập trung tại Sở giao dịch chứng khoán, thứ tự ưu tiên khi so khớp các lệnh giới hạn được xác định theo nguyên tắc nào?',
    ['Ưu tiên về giá trước, sau đó đến ưu tiên về thời gian nhập lệnh',
     'Ưu tiên về thời gian nhập lệnh trước, sau đó đến ưu tiên về giá',
     'Ưu tiên lệnh có khối lượng lớn hơn, sau đó đến ưu tiên về giá',
     'Ưu tiên lệnh của nhà đầu tư tổ chức, sau đó đến ưu tiên về thời gian'],
    'Nguyên tắc ưu tiên: (1) về giá – lệnh mua giá cao hơn, lệnh bán giá thấp hơn được ưu tiên thực hiện trước; (2) về thời gian – cùng mức giá thì lệnh nhập vào hệ thống trước được ưu tiên. Khối lượng lệnh hay loại nhà đầu tư không phải là tiêu chí ưu tiên.',
    'Nguyên tắc khớp lệnh: ưu tiên về giá, ưu tiên về thời gian')
add(T1, 1,
    'Đặc điểm nào sau đây đúng với lệnh thị trường (như lệnh MP/MTL) trong phiên khớp lệnh liên tục?',
    ['Không ghi giá cụ thể; lệnh mua khớp tại giá bán thấp nhất, lệnh bán khớp tại giá mua cao nhất đang có',
     'Ghi giá cụ thể; chỉ được khớp tại mức giá đã ghi hoặc tốt hơn và có hiệu lực đến hết ngày giao dịch',
     'Chỉ được nhập trong phiên khớp lệnh định kỳ và được khớp tại một mức giá duy nhất của phiên đó',
     'Chỉ được khớp sau khi toàn bộ lệnh giới hạn đang chờ trên sổ lệnh đã được thực hiện xong'],
    'Lệnh thị trường không ghi giá, được thực hiện ngay tại mức giá tốt nhất của phía đối ứng (mua tại giá bán thấp nhất, bán tại giá mua cao nhất) và có thể quét qua nhiều mức giá; phần chưa khớp được xử lý theo quy chế (chuyển thành LO với MTL, hủy với MAK/MOK). Ghi giá cụ thể là đặc điểm của LO; khớp tại một mức giá duy nhất là đặc điểm của phiên định kỳ.',
    'Đặc điểm lệnh thị trường')

# =================== GIAO DỊCH CỔ PHIẾU: cấp độ 2 ===================
add(T1, 2,
    'Giả định quy chế: trong phiên khớp lệnh liên tục, nhà đầu tư được hủy phần khối lượng chưa khớp của lệnh LO. Lúc 9h20, khách hàng đặt lệnh LO mua 5.000 cổ phiếu và đến 9h40 đã khớp 2.000 cổ phiếu. Lúc 10h00 (vẫn trong phiên khớp lệnh liên tục), khách hàng yêu cầu hủy lệnh. Kết quả là:',
    ['2.000 cổ phiếu đã khớp vẫn có hiệu lực; 3.000 cổ phiếu chưa khớp bị hủy',
     'Toàn bộ 5.000 cổ phiếu bị hủy, kể cả 2.000 cổ phiếu đã được khớp',
     'Không được hủy vì lệnh đã được khớp một phần trên hệ thống giao dịch',
     '3.000 cổ phiếu chưa khớp chỉ bị hủy sau khi kết thúc phiên ATC'],
    'Phần đã khớp là giao dịch đã hoàn tất, phát sinh nghĩa vụ thanh toán và không thể hủy. Lệnh hủy chỉ có tác dụng với phần khối lượng còn chờ trên sổ lệnh (5.000 − 2.000 = 3.000 cổ phiếu) và có hiệu lực ngay khi được hệ thống chấp nhận.',
    'Nguyên tắc hủy lệnh: chỉ hủy được phần lệnh chưa khớp (dữ kiện nêu trong đề)')
add(T1, 2,
    'Trong phiên khớp lệnh định kỳ mở cửa, nhà đầu tư đặt lệnh LO mua giá 30.500 đồng; giá mở cửa được xác định là 30.200 đồng và lệnh được khớp toàn bộ. Giá thực hiện của lệnh này là:',
    ['30.200 đồng, là mức giá khớp chung của phiên định kỳ',
     '30.500 đồng, là mức giá nhà đầu tư đã ghi trên lệnh',
     '30.350 đồng, là bình quân của giá đặt và giá mở cửa',
     'Giá đặt của lệnh bán đối ứng nhập sớm nhất trong phiên'],
    'Trong khớp lệnh định kỳ, mọi lệnh được thực hiện tại một mức giá khớp duy nhất (giá mở cửa 30.200 đồng). Lệnh mua giá 30.500 đồng ≥ 30.200 đồng nên đủ điều kiện khớp và được thực hiện tại 30.200 đồng, không phải tại giá đặt. Khớp tại giá của lệnh đối ứng đang chờ là nguyên tắc của khớp lệnh liên tục.',
    'Nguyên tắc xác định giá thực hiện trong khớp lệnh định kỳ')
add(T1, 2,
    'Giả sử chu kỳ thanh toán giao dịch cổ phiếu là T+2 (tính theo ngày làm việc) và trong thời gian này không có ngày nghỉ lễ. Nhà đầu tư mua cổ phiếu được khớp lệnh vào thứ Năm (ngày T). Ngày thanh toán của giao dịch là:',
    ['Thứ Hai tuần kế tiếp', 'Thứ Bảy cùng tuần', 'Thứ Sáu cùng tuần', 'Thứ Ba tuần kế tiếp'],
    'T+2 là 02 ngày làm việc sau ngày giao dịch: T = thứ Năm, T+1 = thứ Sáu, T+2 = thứ Hai tuần kế tiếp (thứ Bảy, Chủ nhật không phải ngày làm việc). Thứ Bảy là đếm theo ngày lịch; thứ Sáu là T+1; thứ Ba tuần kế tiếp là T+3.',
    'Chu kỳ thanh toán T+2 tính theo ngày làm việc (dữ kiện nêu trong đề)')
add(T1, 2,
    'Giả định quy chế cho phép sửa giá lệnh LO đang chờ khớp. Theo nguyên tắc ưu tiên giá – thời gian, sau khi nhà đầu tư sửa giá, thứ tự ưu tiên về thời gian của lệnh được xác định:',
    ['Kể từ thời điểm lệnh sửa được hệ thống giao dịch chấp nhận',
     'Theo thời điểm nhập lệnh gốc ban đầu, không thay đổi gì',
     'Trước mọi lệnh khác đang chờ ở cùng mức giá mới đã sửa',
     'Sau mọi lệnh khác, kể cả các lệnh nhập sau thời điểm sửa'],
    'Sửa giá làm lệnh trở thành một lệnh mới ở mức giá mới, nên ưu tiên thời gian được tính lại từ thời điểm lệnh sửa được chấp nhận: lệnh xếp sau các lệnh đã chờ sẵn ở mức giá đó nhưng trước các lệnh nhập sau. Giữ ưu tiên theo lệnh gốc sẽ cho phép "chen hàng", trái nguyên tắc ưu tiên thời gian.',
    'Nguyên tắc ưu tiên giá – thời gian khi sửa lệnh (dữ kiện nêu trong đề)')
add(T1, 2,
    'Giả định quy chế cho phép lệnh MOK. Trong phiên khớp lệnh liên tục, phía bán trên sổ lệnh chỉ có: 3.000 cổ phiếu giá 20.000 đồng và 1.000 cổ phiếu giá 20.050 đồng. Nhà đầu tư nhập lệnh MOK mua 5.000 cổ phiếu. Kết quả là:',
    ['Lệnh bị hủy toàn bộ, không có cổ phiếu nào được khớp',
     'Khớp 4.000 cổ phiếu, 1.000 cổ phiếu còn lại bị hủy ngay',
     'Khớp 4.000 cổ phiếu, phần còn lại chuyển thành lệnh LO',
     'Khớp 3.000 cổ phiếu giá 20.000 đồng, phần còn lại chờ khớp'],
    'MOK (Match or Kill) phải được khớp toàn bộ ngay khi nhập, nếu không sẽ bị hủy toàn bộ. Phía bán chỉ có 3.000 + 1.000 = 4.000 < 5.000 cổ phiếu nên lệnh bị hủy, không phát sinh giao dịch. Khớp 4.000 cổ phiếu và hủy phần còn lại là cách xử lý của lệnh MAK; chuyển phần còn lại thành LO là cách xử lý của lệnh MTL.',
    'Đặc điểm lệnh MOK, MAK, MTL (dữ kiện nêu trong đề)')
add(T1, 2,
    'Giả định quy chế: đơn vị giao dịch lô chẵn là 100 cổ phiếu; lệnh lô lẻ (01–99 cổ phiếu) được giao dịch riêng, không nhập chung với lệnh lô chẵn. Nhà đầu tư sở hữu 2.375 cổ phiếu và muốn bán hết qua hệ thống giao dịch. Cách đặt lệnh phù hợp là:',
    ['Một lệnh lô chẵn 2.300 cổ phiếu và một lệnh lô lẻ 75 cổ phiếu',
     'Một lệnh duy nhất 2.375 cổ phiếu trên hệ thống giao dịch lô chẵn',
     'Một lệnh lô chẵn 2.000 cổ phiếu và một lệnh lô lẻ 375 cổ phiếu',
     'Một lệnh lô chẵn 2.400 cổ phiếu, phần vượt được hệ thống tự hủy'],
    'Khối lượng lô chẵn phải là bội số của 100: 2.300 cổ phiếu; phần còn lại 75 cổ phiếu (trong khoảng 01–99) đặt bằng lệnh lô lẻ. Lệnh 2.375 cổ phiếu không phải bội số của 100 nên không hợp lệ trên bảng lô chẵn; 375 cổ phiếu vượt giới hạn lô lẻ; lệnh bán 2.400 cổ phiếu vượt số dư chứng khoán nên bị từ chối.',
    'Đơn vị giao dịch lô chẵn, lô lẻ (dữ kiện nêu trong đề)')
add(T1, 2,
    'Trong giao dịch ký quỹ, khi tỷ lệ ký quỹ thực tế trên tài khoản của khách hàng giảm xuống dưới tỷ lệ ký quỹ duy trì, công ty chứng khoán sẽ:',
    ['Yêu cầu khách hàng bổ sung tài sản ký quỹ; quá hạn không bổ sung thì bán chứng khoán để thu hồi nợ',
     'Tự động nâng hạn mức cho vay để khách hàng tiếp tục mua thêm chứng khoán và bình quân giá vốn',
     'Ngừng tính lãi vay ký quỹ cho đến khi giá chứng khoán phục hồi lên trên mức giá lúc khách hàng mua',
     'Chuyển quyền sở hữu chứng khoán ký quỹ sang công ty chứng khoán theo giá tham chiếu của ngày đó'],
    'Khi tỷ lệ ký quỹ thực tế thấp hơn tỷ lệ duy trì, CTCK gọi ký quỹ bổ sung (margin call): khách hàng nộp thêm tiền, chứng khoán ký quỹ hoặc bán bớt chứng khoán để trả nợ. Nếu khách hàng không đáp ứng trong thời hạn theo hợp đồng, CTCK được bán chứng khoán ký quỹ (bán giải chấp) để thu hồi nợ vay. Nâng hạn mức cho vay khi tài khoản đang thiếu ký quỹ là trái nguyên tắc quản trị rủi ro.',
    'Cơ chế gọi ký quỹ bổ sung và xử lý tài khoản giao dịch ký quỹ')
add(T1, 2,
    'Khách hàng đặt lệnh LO mua 10.000 cổ phiếu giá 15.000 đồng; trong ngày chỉ khớp được 3.000 cổ phiếu, phần còn lại hết hiệu lực vào cuối ngày. Biểu phí môi giới tính theo tỷ lệ % trên giá trị giao dịch. Phí môi giới khách hàng phải trả được tính trên:',
    ['Giá trị 3.000 cổ phiếu đã được khớp lệnh',
     'Giá trị 10.000 cổ phiếu ghi trên lệnh đã đặt',
     'Giá trị 7.000 cổ phiếu không được khớp lệnh',
     'Số tiền khách hàng bị phong tỏa khi đặt lệnh'],
    'Phí môi giới chỉ phát sinh trên giá trị giao dịch được thực hiện: 3.000 × 15.000 = 45.000.000 đồng × tỷ lệ phí. Phần lệnh không khớp, hết hiệu lực không tạo ra giao dịch nên không bị thu phí; số tiền phong tỏa cho phần này được giải tỏa.',
    'Phí môi giới tính trên giá trị giao dịch được thực hiện')

# =================== GIAO DỊCH CỔ PHIẾU: cấp độ 3 ===================
# S1 – giá trần ngày GDKHQ cổ tức tiền
P0, DIV = 38500, 2000
ref = P0 - DIV
raw = ref * 1.07
ceil_ok = math.floor(raw / tick(raw)) * tick(raw)
chk(raw, 39055); chk(ceil_ok, 39050)
d_noadj = math.floor(P0 * 1.07 / 50) * 50            # 41.195 → 41.150
d_after = math.floor((P0 * 1.07 - DIV) / 50) * 50    # 39.195 → 39.150
d_up = math.ceil(raw / 50) * 50                      # 39.100
chk(d_noadj, 41150); chk(d_after, 39150); chk(d_up, 39100)
addn(T1, 3,
     'Cổ phiếu M có giá đóng cửa ngày giao dịch liền trước ngày giao dịch không hưởng quyền là 38.500 đồng; công ty trả cổ tức bằng tiền 2.000 đồng/cổ phiếu. Giả định: biên độ dao động giá ±7% so với giá tham chiếu; bước giá 50 đồng; giá trần được làm tròn xuống theo bước giá. Giá trần của cổ phiếu M vào ngày giao dịch không hưởng quyền là:',
     [ceil_ok, d_noadj, d_after, d_up], dong,
     'Giá tham chiếu điều chỉnh = 38.500 − 2.000 = 36.500 đồng. Giá trần = 36.500 × 1,07 = 39.055 → làm tròn xuống theo bước giá 50 = 39.050 đồng. Lỗi thường gặp: không điều chỉnh giá tham chiếu (38.500 × 1,07 = 41.195 → 41.150); tính giá trần trước rồi mới trừ cổ tức (41.195 − 2.000 = 39.195 → 39.150); làm tròn lên (39.100).',
     'Giá tham chiếu điều chỉnh khi trả cổ tức tiền = Giá đóng cửa − Cổ tức; Giá trần = Giá tham chiếu × (1 + biên độ), làm tròn theo bước giá (dữ kiện nêu trong đề)')

# S2 – khớp định kỳ mở cửa, tiêu chí phụ chọn giá
prices = [51800, 51900, 52000, 52100, 52200, 52300]
B2 = {52300: 2000, 52200: 2000, 52100: 1500, 52000: 1500, 51900: 2000, 51800: 1500}
S2 = {51800: 500, 51900: 500, 52000: 2000, 52100: 1500, 52200: 3000, 52300: 2000}
r = auction(1000, B2, 500, S2, prices)
mx = max(x[3] for x in r)
cand = [x for x in r if x[3] == mx]
best = min(cand, key=lambda x: (abs(x[0] - 52000), -x[0]))
assert [x[0] for x in cand] == [52100, 52200] and best[0] == 52100 and best[3] == 5000
assert [x[3] for x in r] == [1000, 1500, 3500, 5000, 5000, 3000]
assert r[3][1] == 6500 and r[2][3] == 3500
pv = lambda p, v: f'{vn(p)} đồng; {cp(v)}'
add(T1, 3,
    'Cổ phiếu N có giá tham chiếu 52.000 đồng, bước giá 100 đồng. Sổ lệnh phiên khớp lệnh định kỳ mở cửa (đơn vị: cổ phiếu) – Mua: ATO 1.000; giá 52.300: 2.000; 52.200: 2.000; 52.100: 1.500; 52.000: 1.500; 51.900: 2.000; 51.800: 1.500. Bán: ATO 500; giá 51.800: 500; 51.900: 500; 52.000: 2.000; 52.100: 1.500; 52.200: 3.000; 52.300: 2.000. Giả định nguyên tắc xác định giá: (1) đạt khối lượng khớp lớn nhất; (2) nếu nhiều mức giá thỏa mãn (1), chọn mức giá trùng hoặc gần nhất với giá tham chiếu; (3) nếu vẫn còn nhiều mức giá, chọn mức giá cao hơn; lệnh ATO được ưu tiên trước lệnh LO. Giá mở cửa và khối lượng khớp là:',
    [pv(52100, 5000), pv(52200, 5000), pv(52000, 3500), pv(52100, 6500)],
    'KL mua cộng dồn (từ giá cao xuống, cộng ATO) / KL bán cộng dồn (từ giá thấp lên, cộng ATO): 51.800: 11.500/1.000 → 1.000; 51.900: 10.000/1.500 → 1.500; 52.000: 8.000/3.500 → 3.500; 52.100: 6.500/5.000 → 5.000; 52.200: 5.000/8.000 → 5.000; 52.300: 3.000/10.000 → 3.000. Khối lượng lớn nhất 5.000 đạt tại 52.100 và 52.200; theo tiêu chí (2), 52.100 gần giá tham chiếu hơn → giá mở cửa 52.100 đồng, khớp 5.000 cổ phiếu. Chọn 52.200 là áp dụng tiêu chí (3) khi chưa xét tiêu chí (2); 6.500 là KL mua cộng dồn chứ không phải KL khớp; 52.000 là giá tham chiếu, chỉ khớp được 3.500 cổ phiếu.',
    'Khớp lệnh định kỳ: giá khớp đạt khối lượng lớn nhất, các tiêu chí phụ (dữ kiện nêu trong đề)',
    key=[52100.05, 52200.05, 52000.035, 52100.065], val=52100)

# S3 – khớp định kỳ đóng cửa, phân bổ theo thời gian
pr3 = [41000, 41100, 41200]
B3 = {41200: 2500, 41100: 4000, 41000: 3000}
S3 = {41000: 4000, 41100: 2000, 41200: 2000}


def alloc_K(bm, sm):
    rr = auction(bm, B3, sm, S3, pr3)
    p, _, _, v = max(rr, key=lambda x: x[3])
    left = v - bm                          # ATC mua trước
    for q in [2500, 2500]:                 # giá 41.200, rồi H (14h32) tại 41.100
        left -= min(q, left)
    return p, v, min(1500, left)


p3, v3, k3 = alloc_K(1500, 1000)
assert (p3, v3, k3) == (41100, 7000, 500)
assert alloc_K(0, 0) == (41100, 6000, 1000)   # bỏ sót lệnh ATC
addn(T1, 3,
     'Sổ lệnh phiên khớp lệnh định kỳ đóng cửa của cổ phiếu P (đơn vị: cổ phiếu) – Mua: ATC 1.500; giá 41.200: 2.500; giá 41.100: lệnh của nhà đầu tư H 2.500 (nhập lúc 14h32) và lệnh của nhà đầu tư K 1.500 (nhập lúc 14h35); giá 41.000: 3.000. Bán: ATC 1.000; giá 41.000: 4.000; 41.100: 2.000; 41.200: 2.000. Giả định giá đóng cửa là mức giá đạt khối lượng khớp lớn nhất; lệnh ATC được ưu tiên trước lệnh LO, sau đó ưu tiên về giá rồi về thời gian. Khối lượng cổ phiếu nhà đầu tư K được khớp là:',
     [k3, 1000, 1500, 0], cp,
     'KL mua/bán cộng dồn: 41.200: 4.000/9.000 → 4.000; 41.100: 8.000/7.000 → 7.000; 41.000: 11.000/5.000 → 5.000. Giá đóng cửa 41.100 đồng, khớp 7.000 cổ phiếu. Phân bổ phía mua: ATC 1.500 → còn 5.500; giá 41.200: 2.500 → còn 3.000; tại 41.100, H nhập trước được 2.500 → còn 500; K được khớp 500 cổ phiếu (1.000 cổ phiếu còn lại không khớp). Bỏ sót lệnh ATC (KL khớp chỉ 6.000) cho kết quả 1.000; cho rằng mọi lệnh tại giá khớp đều khớp đủ cho kết quả 1.500; cho rằng chỉ lệnh có giá tốt hơn giá khớp mới được thực hiện cho kết quả 0.',
     'Khớp lệnh định kỳ: ưu tiên lệnh ATC, ưu tiên giá, ưu tiên thời gian (dữ kiện nêu trong đề)')

# S4 – khớp liên tục quét nhiều mức giá
book = [(18450, 3000), (18500, 2000), (18550, 5000)]
lim, qty, val4, left = 18500, 7000, 0, 7000
for p, q in book:
    if p > lim or left == 0:
        break
    m = min(q, left); val4 += m * p; left -= m
assert left == 2000
chk(val4, 92350000)
addn(T1, 3,
     'Trong phiên khớp lệnh liên tục, phía bán trên sổ lệnh cổ phiếu Q đang có: 3.000 cổ phiếu giá 18.450 đồng; 2.000 cổ phiếu giá 18.500 đồng; 5.000 cổ phiếu giá 18.550 đồng (phía mua không có lệnh nào từ 18.450 đồng trở lên). Nhà đầu tư nhập lệnh LO mua 7.000 cổ phiếu giá 18.500 đồng. Giá trị khớp ngay của lệnh này (chưa tính phí) là:',
     [val4, 5000 * 18500, 3000 * 18450 + 2000 * 18500 + 2000 * 18550, 7000 * 18500], dong,
     'Lệnh mua LO 18.500 khớp lần lượt với các lệnh bán giá thấp nhất, tại giá của lệnh đang chờ: 3.000 × 18.450 = 55.350.000; 2.000 × 18.500 = 37.000.000. Không khớp mức 18.550 vì cao hơn giá giới hạn; 2.000 cổ phiếu còn lại chờ trên sổ lệnh tại 18.500. Giá trị khớp = 92.350.000 đồng. 92.500.000 là coi cả 5.000 cổ phiếu khớp tại 18.500; 129.450.000 là bỏ qua giới hạn giá; 129.500.000 là coi cả 7.000 cổ phiếu khớp tại giá đặt.',
     'Khớp lệnh liên tục: thực hiện tại giá của lệnh đối ứng đang chờ, trong giới hạn giá của lệnh LO')

# S5 – lệnh MP chuyển thành LO
ref5 = 32300
ceil5 = math.floor(ref5 * 1.07 / 50) * 50
chk(ceil5, 34550)
last = 32350
conv = min(last + tick(last), ceil5)
chk(conv, 32400)
addn(T1, 3,
     'Giả định quy chế: lệnh MP mua được khớp lần lượt với các mức giá bán tốt nhất; khi phía bán không còn lệnh đối ứng, phần còn lại chuyển thành lệnh LO mua với giá cao hơn một bước giá so với giá khớp cuối cùng (nếu giá khớp cuối cùng là giá trần thì chuyển thành LO tại giá trần). Cổ phiếu R có giá tham chiếu 32.300 đồng, biên độ ±7%, bước giá 50 đồng; phía bán trên sổ lệnh chỉ có 1.000 cổ phiếu giá 32.300 đồng và 1.500 cổ phiếu giá 32.350 đồng. Nhà đầu tư nhập lệnh MP mua 4.000 cổ phiếu. Phần chưa khớp được chuyển thành lệnh LO mua với giá:',
     [conv, 32350, 32300, ceil5], dong,
     'Lệnh MP mua khớp 1.000 cổ phiếu giá 32.300 và 1.500 cổ phiếu giá 32.350 (tổng 2.500). Phía bán hết lệnh, 1.500 cổ phiếu còn lại chuyển thành LO mua tại 32.350 + 50 = 32.400 đồng. Giá khớp cuối cùng chưa phải giá trần (32.300 × 1,07 = 34.561 → 34.550 đồng) nên không áp dụng giá trần. 32.350 là giá khớp cuối cùng; 32.300 là giá khớp đầu tiên.',
     'Xử lý phần chưa khớp của lệnh thị trường MP (dữ kiện nêu trong đề)')

# S6 – sức mua với phí, lô chẵn
cash, p6, f6 = 200_000_000, 39950, 0.0015
n_raw = cash / (p6 * (1 + f6))
n6 = int(n_raw // 100 * 100)
assert n6 == 4900 and 5000 * p6 * (1 + f6) > cash and 4900 * p6 * (1 + f6) <= cash
assert int(n_raw) == 4998 and int(cash / p6) == 5006
addn(T1, 3,
     'Tài khoản của khách hàng có 200.000.000 đồng tiền mặt (không sử dụng giao dịch ký quỹ). Khách hàng muốn mua cổ phiếu S giá 39.950 đồng; phí môi giới 0,15% giá trị giao dịch, thu khi mua; đơn vị giao dịch lô chẵn 100 cổ phiếu. Khối lượng tối đa khách hàng có thể đặt mua bằng lệnh lô chẵn là:',
     [n6, int(n_raw), int(cash / p6 // 100 * 100), int(cash / p6)], cp,
     'Chi phí mua 1 cổ phiếu = 39.950 × 1,0015 = 40.009,925 đồng. Số cổ phiếu tối đa = 200.000.000 / 40.009,925 ≈ 4.998,8 → làm tròn xuống bội số 100 = 4.900 cổ phiếu (cần 196.048.633 đồng). Mua 5.000 cổ phiếu (bỏ qua phí) cần 200.049.625 đồng, vượt số dư tiền; 4.998 và 5.006 không phải bội số của lô chẵn.',
     'Sức mua = Tiền mặt / [Giá × (1 + tỷ lệ phí)], làm tròn xuống theo lô chẵn')
chk(4900 * p6 * (1 + f6), 196048632.5); chk(5000 * p6 * (1 + f6), 200049625)

# S7 – giá bán hòa vốn
pb, fee7, tax = 24000, 0.002, 0.001
be = pb * (1 + fee7) / (1 - fee7 - tax)
chk(be, 24120.361083, 1e-9)
be_t = math.ceil(be / 50) * 50
assert be_t == 24150 and 24100 * (1 - fee7 - tax) < pb * (1 + fee7) <= 24150 * (1 - fee7 - tax)
d_buyfee = math.ceil(pb * (1 + fee7) / 50) * 50           # 24.050
d_notax = math.ceil(pb * (1 + fee7) / (1 - fee7) / 50) * 50  # 24.100
assert (d_buyfee, d_notax, int(be)) == (24050, 24100, 24120)
addn(T1, 3,
     'Nhà đầu tư mua cổ phiếu giá 24.000 đồng. Phí môi giới 0,2% giá trị giao dịch mỗi chiều; thuế thu nhập cá nhân 0,1% trên giá trị bán (giả định theo đề); bước giá 50 đồng. Giá bán thấp nhất (theo bước giá) để nhà đầu tư không bị lỗ là:',
     [be_t, d_buyfee, d_notax, int(be)], dong,
     'Điều kiện hòa vốn: P × (1 − 0,2% − 0,1%) ≥ 24.000 × (1 + 0,2%) = 24.048 → P ≥ 24.048 / 0,997 = 24.120,36 đồng → làm tròn lên theo bước giá 50 = 24.150 đồng. 24.050 chỉ tính phí mua; 24.100 bỏ qua thuế (24.048 / 0,998 = 24.096,2); 24.120 chưa làm tròn theo bước giá và vẫn thấp hơn mức hòa vốn.',
     'Giá hòa vốn = Giá mua × (1 + phí mua) / (1 − phí bán − thuế bán)')

# S8 – lãi đã thực hiện theo giá vốn bình quân gia quyền
f8, t8 = 0.0015, 0.001
cost = (2000 * 15200 + 3000 * 14600) * (1 + f8)
avg = cost / 5000
proceeds = 3000 * 15500 * (1 - f8 - t8)
pl = proceeds - 3000 * avg
chk(cost, 74311300); chk(avg, 14862.26); chk(proceeds, 46383750); chk(pl, 1796970)
pl_fifo = proceeds - (2000 * 15200 + 1000 * 14600) * (1 + f8)
pl_simple = proceeds - 3000 * (15200 + 14600) / 2 * (1 + f8)
pl_nofee = 3000 * (15500 - (2000 * 15200 + 3000 * 14600) / 5000)
chk(pl_fifo, 1316250); chk(pl_simple, 1616700); chk(pl_nofee, 1980000)
addn(T1, 3,
     'Nhà đầu tư mua 2.000 cổ phiếu giá 15.200 đồng, sau đó mua thêm 3.000 cổ phiếu cùng loại giá 14.600 đồng. Tiếp đó, nhà đầu tư bán 3.000 cổ phiếu giá 15.500 đồng. Phí môi giới 0,15% giá trị giao dịch mỗi chiều; thuế thu nhập cá nhân 0,1% trên giá trị bán (giả định theo đề). Tính theo giá vốn bình quân gia quyền (bao gồm phí mua), lãi đã thực hiện của lần bán này là:',
     [round(pl), round(pl_fifo), round(pl_simple), round(pl_nofee)], dong,
     'Tổng giá vốn = (2.000 × 15.200 + 3.000 × 14.600) × 1,0015 = 74.200.000 × 1,0015 = 74.311.300 đồng → giá vốn bình quân 14.862,26 đồng/cổ phiếu; giá vốn của 3.000 cổ phiếu bán = 44.586.780 đồng. Tiền thu ròng = 46.500.000 × (1 − 0,15% − 0,1%) = 46.383.750 đồng. Lãi đã thực hiện = 1.796.970 đồng. Lỗi thường gặp: dùng phương pháp nhập trước – xuất trước (1.316.250); bình quân giản đơn hai mức giá (1.616.700); bỏ qua phí và thuế (1.980.000).',
     'Lãi đã thực hiện = Tiền bán ròng − Số lượng bán × Giá vốn bình quân gia quyền')

# S9 – giá tham chiếu điều chỉnh: cổ phiếu thưởng + quyền mua
P9, I_th, I_mua, PR = 45000, 0.2, 0.1, 15000
ptc = (P9 + I_mua * PR) / (1 + I_th + I_mua)
chk(ptc, 35769.230769, 1e-9)
chk(13 * ptc, 10 * P9 + 1 * PR)  # bảo toàn giá trị: 10 cổ phiếu cũ + tiền mua 1 cổ phiếu = 13 cổ phiếu
addn(T1, 3,
     'Cổ phiếu T có giá đóng cửa ngày giao dịch liền trước ngày giao dịch không hưởng quyền là 45.000 đồng. Cùng ngày giao dịch không hưởng quyền, công ty thực hiện đồng thời: phát hành cổ phiếu thưởng tỷ lệ 10:2 (sở hữu 10 cổ phiếu được nhận thêm 2 cổ phiếu) và phát hành thêm cho cổ đông hiện hữu tỷ lệ 10:1 (sở hữu 10 cổ phiếu được mua 1 cổ phiếu mới) với giá 15.000 đồng/cổ phiếu. Giá tham chiếu điều chỉnh lý thuyết (làm tròn đến đồng) là:',
     [round(ptc), round(P9 / (1 + I_th)), round((P9 + I_mua * PR) / (1 + I_th)), round((P9 - I_mua * PR) / (1 + I_th + I_mua))], dong,
     'Ptc = (P + I_mua × Giá phát hành) / (1 + I_thưởng + I_mua) = (45.000 + 0,1 × 15.000) / (1 + 0,2 + 0,1) = 46.500 / 1,3 ≈ 35.769 đồng. Kiểm tra: 10 cổ phiếu cũ (450.000 đồng) cộng 15.000 đồng nộp mua thêm = 465.000 đồng cho 13 cổ phiếu → 35.769 đồng/cổ phiếu. Lỗi thường gặp: bỏ qua quyền mua (45.000 / 1,2 = 37.500); thiếu tỷ lệ quyền mua ở mẫu số (46.500 / 1,2 = 38.750); trừ thay vì cộng tiền mua ((45.000 − 1.500) / 1,3 ≈ 33.462).',
     'Ptc = (P + Σ Tỷ lệ quyền mua × Giá phát hành) / (1 + Σ Tỷ lệ phát hành thêm), tỷ lệ cổ phiếu thưởng có giá phát hành bằng 0')
assert [round(ptc), round(P9 / 1.2), round(46500 / 1.2), round(43500 / 1.3)] == [35769, 37500, 38750, 33462]

# S10 – nộp tiền khi bị gọi ký quỹ
n10, p_buy, p_now, mr = 25000, 32000, 22400, 0.35
debt = n10 * p_buy * 0.5
V = n10 * p_now
eq = V - debt
x10 = mr * V - eq                       # tiền nộp dùng để trả nợ: (V − (debt − X))/V = mr
assert abs((V - (debt - x10)) / V - mr) < 1e-12
chk(eq / V, 0.285714, 1e-5); chk(x10, 36_000_000)
x_asset = (mr * V - eq) / (1 - mr)      # coi tiền nộp là tài sản, không giảm nợ
x_init = 0.5 * V - eq
x_full = mr * V
chk(x_asset, 55384615.38, 1e-9); chk(x_init, 120_000_000); chk(x_full, 196_000_000)
addn(T1, 3,
     'Khách hàng mua 25.000 cổ phiếu giá 32.000 đồng bằng giao dịch ký quỹ: tự có 50%, vay công ty chứng khoán 50%. Hợp đồng quy định: tỷ lệ ký quỹ = (Giá trị chứng khoán − Dư nợ) / Giá trị chứng khoán; tỷ lệ duy trì 35%; khi bị gọi ký quỹ, khách hàng nộp tiền để trả bớt dư nợ, đưa tỷ lệ ký quỹ về đúng tỷ lệ duy trì. Bỏ qua lãi vay và phí. Khi giá cổ phiếu giảm còn 22.400 đồng, số tiền tối thiểu khách hàng phải nộp là:',
     [round(x10), round(x_asset), round(x_init), round(x_full)], dong,
     'Giá trị chứng khoán = 25.000 × 22.400 = 560.000.000 đồng; dư nợ = 400.000.000 đồng; vốn tự có còn lại = 160.000.000 đồng → tỷ lệ ký quỹ 28,57% < 35%. Nộp X để trả nợ: (560.000.000 − 400.000.000 + X) / 560.000.000 = 35% → X = 196.000.000 − 160.000.000 = 36.000.000 đồng. Lỗi thường gặp: coi tiền nộp là tài sản tăng thêm mà không giảm nợ (55.384.615); đưa tỷ lệ về mức ban đầu 50% (120.000.000); lấy cả mức vốn yêu cầu 35% × 560.000.000 (196.000.000).',
     'Tỷ lệ ký quỹ = (Giá trị chứng khoán − Dư nợ) / Giá trị chứng khoán (dữ kiện hợp đồng nêu trong đề)')

# S11 – tỷ suất lợi nhuận trên vốn tự có khi dùng đòn bẩy
gain = 400e6 * 0.08
interest = 200e6 * 0.12 * 90 / 365
roe = (gain - interest) / 200e6
chk(interest, 5917808.219, 1e-9); chk(roe, 0.130411, 1e-5)
addn(T1, 3,
     'Nhà đầu tư mua cổ phiếu trị giá 400.000.000 đồng, trong đó 200.000.000 đồng vốn tự có và 200.000.000 đồng vay ký quỹ với lãi suất 12%/năm (tính theo số ngày thực tế/365). Sau 90 ngày, nhà đầu tư bán toàn bộ khi giá cổ phiếu tăng 8%. Bỏ qua phí và thuế, tỷ suất lợi nhuận trên vốn tự có trong 90 ngày (làm tròn 2 chữ số thập phân) là:',
     [roe, gain / 200e6, 0.08, (gain - 200e6 * 0.12) / 200e6], pc,
     'Lãi vốn = 400.000.000 × 8% = 32.000.000 đồng; lãi vay = 200.000.000 × 12% × 90/365 = 5.917.808 đồng; lợi nhuận ròng = 26.082.192 đồng → 26.082.192 / 200.000.000 = 13,04%. 16,00% là bỏ qua lãi vay; 8,00% là tỷ suất khi không dùng đòn bẩy; 4,00% là trừ lãi vay của cả năm (24.000.000 đồng).',
     'Tỷ suất lợi nhuận trên vốn tự có = (Lãi vốn − Lãi vay) / Vốn tự có')

# =================== GIAO DỊCH TRÁI PHIẾU: cấp độ 1 ===================
add(T2, 1,
    'Giá sạch (clean price) của trái phiếu là:',
    ['Giá giao dịch không bao gồm phần lãi coupon cộng dồn kể từ ngày trả lãi gần nhất',
     'Giá giao dịch đã bao gồm phần lãi coupon cộng dồn tính đến ngày thanh toán',
     'Giá giao dịch sau khi đã trừ phí môi giới và thuế mà nhà đầu tư phải nộp',
     'Giá do tổ chức phát hành công bố khi chào bán trái phiếu lần đầu ra thị trường'],
    'Giá sạch = Giá bẩn − Lãi cộng dồn. Giá bẩn (giá thanh toán, dirty price) bao gồm lãi coupon cộng dồn từ ngày trả lãi gần nhất đến ngày thanh toán và là số tiền người mua thực trả. Giá sạch không liên quan đến phí, thuế hay giá phát hành.',
    'Giá sạch, giá bẩn và lãi cộng dồn của trái phiếu')
add(T2, 1,
    'Khi lãi suất thị trường tăng, các yếu tố khác không đổi, giá của trái phiếu trả lãi cố định đang lưu hành sẽ:',
    ['Giảm, vì dòng tiền cố định được chiết khấu ở lợi suất yêu cầu cao hơn',
     'Tăng, vì nhà đầu tư đòi hỏi mức lợi suất cao hơn đối với trái phiếu',
     'Không đổi, vì lãi suất coupon đã được cố định trong suốt kỳ hạn',
     'Không đổi cho đến khi tổ chức phát hành điều chỉnh lãi suất coupon'],
    'Giá trái phiếu là giá trị hiện tại của các khoản coupon và gốc cố định; lợi suất yêu cầu tăng thì các dòng tiền được chiết khấu mạnh hơn, giá giảm. Giá và lợi suất của trái phiếu biến động ngược chiều.',
    'Quan hệ ngược chiều giữa giá và lợi suất trái phiếu')
add(T2, 1,
    'Chỉ tiêu nào của trái phiếu chỉ so sánh tiền lãi coupon hằng năm với giá thị trường hiện tại, không tính đến khoản lãi hoặc lỗ vốn khi nắm giữ đến ngày đáo hạn?',
    ['Lợi suất hiện hành (current yield)', 'Lợi suất đáo hạn (YTM)',
     'Lợi suất thu hồi (yield to call)', 'Lãi suất danh nghĩa (coupon rate)'],
    'Lợi suất hiện hành = Coupon năm / Giá thị trường, bỏ qua chênh lệch giữa giá mua và mệnh giá nhận lại. YTM và lợi suất thu hồi tính cả coupon, lãi/lỗ vốn và giá trị thời gian của tiền; lãi suất coupon so sánh tiền lãi với mệnh giá chứ không phải với giá thị trường.',
    'Các thước đo lợi suất trái phiếu')

# =================== GIAO DỊCH TRÁI PHIẾU: cấp độ 2 ===================
add(T2, 2,
    'Một trái phiếu trả lãi cố định hằng năm đang được giao dịch cao hơn mệnh giá (trái phiếu có phụ trội). Quan hệ đúng giữa lãi suất coupon (c), lợi suất hiện hành (CY) và lợi suất đáo hạn (YTM) là:',
    ['c > CY > YTM', 'YTM > CY > c', 'c = CY = YTM', 'CY > c > YTM'],
    'Giá > mệnh giá ⇒ CY = Coupon/Giá < Coupon/Mệnh giá = c. YTM còn tính khoản lỗ vốn (giá mua cao hơn mệnh giá nhận lại khi đáo hạn) nên thấp hơn CY: c > CY > YTM. Thứ tự YTM > CY > c đúng với trái phiếu chiết khấu; ba chỉ tiêu bằng nhau khi giá bằng mệnh giá.',
    'Quan hệ giữa lãi suất coupon, lợi suất hiện hành và lợi suất đáo hạn')
add(T2, 2,
    'Nhà đầu tư mua trái phiếu vào giữa hai kỳ trả lãi và vẫn nắm giữ đến ngày trả lãi kế tiếp (giao dịch được thanh toán trước ngày chốt danh sách người sở hữu nhận lãi). Phát biểu nào sau đây đúng?',
    ['Người mua trả cho người bán phần lãi cộng dồn, sau đó nhận toàn bộ coupon của kỳ đó',
     'Người mua và người bán cùng nhận coupon từ tổ chức phát hành theo số ngày nắm giữ',
     'Người mua chỉ nhận phần coupon ứng với số ngày nắm giữ và không trả lãi cộng dồn',
     'Người bán nhận toàn bộ coupon của kỳ đó, người mua chỉ thanh toán theo giá sạch'],
    'Tổ chức phát hành trả toàn bộ coupon cho người có tên trong danh sách tại ngày chốt. Để bù cho người bán phần lãi của những ngày đã nắm giữ, người mua thanh toán giá bẩn = giá sạch + lãi cộng dồn; đến ngày trả lãi, người mua nhận toàn bộ coupon, nên phần lãi ròng của người mua đúng bằng lãi của số ngày mình nắm giữ.',
    'Mua trái phiếu giữa hai kỳ trả lãi: giá bẩn = giá sạch + lãi cộng dồn')
add(T2, 2,
    'Giả sử lợi suất thị trường không đổi trong suốt thời gian còn lại. Giá (giá sạch) của một trái phiếu trả lãi cố định đang giao dịch cao hơn mệnh giá sẽ thay đổi như thế nào khi tiến dần đến ngày đáo hạn?',
    ['Giảm dần và tiến về mệnh giá vào ngày đáo hạn',
     'Tăng dần do các khoản coupon được nhận sớm hơn',
     'Giữ nguyên ở mức hiện tại cho đến ngày đáo hạn',
     'Giảm xuống dưới mệnh giá rồi tăng lại khi đáo hạn'],
    'Khi đáo hạn, người nắm giữ chỉ nhận lại mệnh giá (cùng coupon cuối), nên giá của trái phiếu phụ trội giảm dần về mệnh giá vì số kỳ coupon cao hơn lợi suất thị trường còn lại ít dần; ngược lại, giá trái phiếu chiết khấu tăng dần về mệnh giá.',
    'Diễn biến giá trái phiếu theo thời gian khi lợi suất không đổi')
add(T2, 2,
    'Lý do chủ yếu khiến trái phiếu thường được yết giá theo giá sạch thay vì giá bẩn là:',
    ['Giá bẩn tăng dần theo lãi cộng dồn rồi giảm đột ngột sau ngày trả lãi, khó so sánh',
     'Giá sạch đã bao gồm phí và thuế nên phản ánh đúng chi phí thực tế của nhà đầu tư',
     'Giá sạch luôn bằng mệnh giá nên thuận tiện cho việc tính toán và thanh toán',
     'Người mua chỉ thanh toán giá sạch, lãi cộng dồn do tổ chức phát hành chi trả thay'],
    'Giá bẩn chứa lãi cộng dồn nên tăng đều theo thời gian và giảm mạnh ngay sau ngày trả lãi (dạng răng cưa) dù lợi suất thị trường không đổi. Yết giá sạch loại bỏ hiệu ứng này, giúp phản ánh đúng biến động giá do thay đổi lợi suất; khi thanh toán, người mua vẫn trả giá bẩn = giá sạch + lãi cộng dồn.',
    'Yết giá trái phiếu theo giá sạch')
add(T2, 2,
    'Giả định: trái phiếu Chính phủ niêm yết được giao dịch trên hệ thống giao dịch trái phiếu Chính phủ chuyên biệt tại Sở Giao dịch Chứng khoán Hà Nội theo phương thức thỏa thuận, gồm giao dịch mua bán thông thường (outright) và giao dịch mua bán lại (repo). Ngân hàng A bán trái phiếu Chính phủ cho công ty bảo hiểm B, đồng thời hai bên cam kết A sẽ mua lại đúng số trái phiếu này sau 14 ngày với giá xác định trước. Giao dịch này là:',
    ['Giao dịch mua bán lại (repo) theo phương thức thỏa thuận',
     'Giao dịch mua bán thông thường (outright) theo phương thức thỏa thuận',
     'Giao dịch khớp lệnh liên tục trên hệ thống giao dịch cổ phiếu',
     'Giao dịch hoán đổi lãi suất giữa hai tổ chức trên thị trường OTC'],
    'Giao dịch gồm hai vế: bán ngay và cam kết mua lại sau một thời hạn với giá xác định trước – đó là giao dịch mua bán lại (repo); về bản chất, A vay vốn ngắn hạn có bảo đảm bằng trái phiếu. Giao dịch outright chỉ chuyển quyền sở hữu một lần, không kèm cam kết mua lại.',
    'Giao dịch trái phiếu Chính phủ: mua bán thông thường và mua bán lại (dữ kiện nêu trong đề)')
add(T2, 2,
    'So với trái phiếu lãi suất cố định cùng kỳ hạn và cùng tổ chức phát hành, trái phiếu có lãi suất thả nổi (coupon điều chỉnh định kỳ theo lãi suất tham chiếu thị trường) có đặc điểm nào về giá?',
    ['Giá thường dao động gần mệnh giá quanh các ngày điều chỉnh lãi suất, rủi ro lãi suất thấp hơn',
     'Giá biến động mạnh hơn khi lãi suất thị trường thay đổi do dòng tiền không được cố định',
     'Giá luôn thấp hơn mệnh giá do nhà đầu tư không biết trước các khoản coupon tương lai',
     'Giá tăng khi lãi suất tham chiếu tăng và giảm khi lãi suất tham chiếu giảm tương ứng'],
    'Coupon của trái phiếu thả nổi được điều chỉnh theo lãi suất thị trường tại mỗi kỳ, nên tại ngày điều chỉnh giá trở về gần mệnh giá (nếu rủi ro tín dụng không đổi); rủi ro lãi suất chỉ còn trong khoảng thời gian giữa hai lần điều chỉnh, thấp hơn nhiều so với trái phiếu lãi suất cố định cùng kỳ hạn.',
    'Đặc điểm giá của trái phiếu lãi suất thả nổi')

# =================== GIAO DỊCH TRÁI PHIẾU: cấp độ 3 ===================
# B1 – coupon mỗi kỳ sau thuế
gross = 2500 * 100000 * 0.092 / 2
chk(gross, 11_500_000)
addn(T2, 3,
     'Nhà đầu tư cá nhân nắm giữ 2.500 trái phiếu doanh nghiệp niêm yết, mệnh giá 100.000 đồng, lãi suất coupon 9,2%/năm, trả lãi 6 tháng một lần. Giả định thuế thu nhập cá nhân 5% trên tiền lãi được khấu trừ khi chi trả. Số tiền lãi nhà đầu tư thực nhận mỗi kỳ là:',
     [round(gross * 0.95), round(gross), round(gross * 2 * 0.95), round(gross * 0.9)], dong,
     'Coupon mỗi kỳ = 2.500 × 100.000 × 9,2% / 2 = 11.500.000 đồng; thuế 5% = 575.000 đồng; thực nhận = 10.925.000 đồng. 11.500.000 là chưa trừ thuế; 21.850.000 là tiền lãi cả năm sau thuế; 10.350.000 là trừ thuế 10%.',
     'Coupon mỗi kỳ = Mệnh giá × Lãi suất coupon năm / Số kỳ trả lãi trong năm')
assert [round(gross * 0.95), round(gross * 1.9), round(gross * 0.9)] == [10925000, 21850000, 10350000]

# B2 – giá sạch từ giá bẩn, quy ước 30/360
d1, d2 = datetime.date(2026, 3, 15), datetime.date(2026, 7, 21)
days360 = (d2.year - d1.year) * 360 + (d2.month - d1.month) * 30 + (min(d2.day, 30) - min(d1.day, 30))
days_act = (d2 - d1).days
assert (days360, days_act) == (126, 128)
ai = 100000 * 0.08 * days360 / 360
clean = 103450 - ai
chk(ai, 2800); chk(clean, 100650)
addn(T2, 3,
     'Trái phiếu mệnh giá 100.000 đồng, lãi suất coupon 8%/năm, trả lãi hằng năm vào ngày 15/3. Nhà đầu tư mua trái phiếu với ngày thanh toán 21/7/2026, giá thanh toán (giá bẩn) 103.450 đồng/trái phiếu. Lãi cộng dồn tính theo quy ước 30/360 kể từ ngày trả lãi gần nhất 15/3/2026. Giá sạch của trái phiếu (làm tròn đến đồng) là:',
     [round(clean), round(103450 - 8000 * days_act / 365), round(103450 - 8000 * days360 / 365), round(103450 + ai)], dong,
     'Theo 30/360: số ngày = 4 tháng × 30 + (21 − 15) = 126 ngày; lãi cộng dồn = 100.000 × 8% × 126/360 = 2.800 đồng; giá sạch = 103.450 − 2.800 = 100.650 đồng. Lỗi thường gặp: dùng số ngày thực tế/365 (128 ngày, lãi 2.805,48 → 100.645); dùng 126 ngày nhưng chia 365 (lãi 2.761,64 → 100.688); cộng thay vì trừ lãi cộng dồn (106.250).',
     'Lãi cộng dồn = Mệnh giá × Lãi suất coupon × Số ngày (30/360) / 360; Giá sạch = Giá bẩn − Lãi cộng dồn')
assert [round(103450 - 8000 * 128 / 365), round(103450 - 8000 * 126 / 365)] == [100645, 100688]

# B3 – tiền thu ròng khi bán trái phiếu (phí, thuế)
dirty_tot = 5000 * (101500 + 1850)
net = dirty_tot * (1 - 0.001 - 0.001)
chk(dirty_tot, 516_750_000); chk(net, 515_716_500)
addn(T2, 3,
     'Nhà đầu tư cá nhân bán 5.000 trái phiếu doanh nghiệp niêm yết với giá sạch 101.500 đồng/trái phiếu; lãi cộng dồn đến ngày thanh toán là 1.850 đồng/trái phiếu. Giả định phí môi giới 0,1% và thuế thu nhập cá nhân 0,1% đều tính trên tổng giá trị thanh toán (giá bẩn). Số tiền ròng nhà đầu tư nhận được là:',
     [round(net), round(5000 * 101500 * 0.998), round(dirty_tot * 0.999), round(dirty_tot)], dong,
     'Giá trị thanh toán = 5.000 × (101.500 + 1.850) = 516.750.000 đồng; phí + thuế = 0,2% × 516.750.000 = 1.033.500 đồng; tiền ròng = 515.716.500 đồng. 506.485.000 là bỏ sót lãi cộng dồn (chỉ tính giá sạch); 516.233.250 là chỉ trừ phí, quên thuế; 516.750.000 là chưa trừ chi phí giao dịch.',
     'Tiền bán ròng = Số lượng × (Giá sạch + Lãi cộng dồn) × (1 − tỷ lệ phí − tỷ lệ thuế) (dữ kiện nêu trong đề)')
assert [round(5000 * 101500 * 0.998), round(dirty_tot * 0.999)] == [506485000, 516233250]

# B4 – giá từ lợi suất hiện hành
p4 = 7200 / 0.08
chk(p4, 90000)
addn(T2, 3,
     'Trái phiếu mệnh giá 100.000 đồng, lãi suất coupon 7,2%/năm, trả lãi hằng năm. Nếu lợi suất hiện hành của trái phiếu là 8%, giá thị trường của trái phiếu là:',
     [round(p4), round(100000 * (1 - 0.008)), round(107200 / 1.08), round(100000 * 0.08 / 0.072)], dong,
     'Lợi suất hiện hành = Coupon năm / Giá thị trường ⇒ Giá = 7.200 / 8% = 90.000 đồng; lợi suất hiện hành (8%) cao hơn lãi suất coupon (7,2%) nên giá thấp hơn mệnh giá. 111.111 là đảo tỷ lệ (100.000 × 8/7,2); 99.200 là chỉ trừ chênh lệch 0,8% mệnh giá; 99.259 là chiết khấu (100.000 + 7.200) một năm ở 8%.',
     'Lợi suất hiện hành = Coupon hằng năm / Giá thị trường')
assert [round(107200 / 1.08), round(100000 * 0.08 / 0.072)] == [99259, 111111]

# B5 – YTM gần đúng
ytm_a = (7000 + (100000 - 94000) / 4) / ((100000 + 94000) / 2)
chk(ytm_a, 8500 / 97000)
addn(T2, 3,
     'Trái phiếu mệnh giá 100.000 đồng, lãi suất coupon 7%/năm trả hằng năm, còn 4 năm đến ngày đáo hạn, giá thị trường 94.000 đồng. Sử dụng công thức gần đúng YTM ≈ [C + (F − P)/n] / [(F + P)/2], lợi suất đáo hạn xấp xỉ là:',
     [ytm_a, 7000 / 94000, 8500 / 94000, 13000 / 97000], pc,
     'YTM ≈ [7.000 + (100.000 − 94.000)/4] / [(100.000 + 94.000)/2] = 8.500 / 97.000 ≈ 8,76%. 7,45% là lợi suất hiện hành (7.000 / 94.000); 9,04% là chia cho giá 94.000 thay vì giá bình quân; 13,40% là cộng toàn bộ chênh lệch 6.000 đồng vào thu nhập một năm.',
     'Công thức YTM gần đúng: [C + (F − P)/n] / [(F + P)/2]')

# B6 – giá trái phiếu trả lãi nửa năm
p6b = bond_price(100000, 0.06, 0.08, 2, 2)
chk(p6b, 3000 * (1 - 1.04 ** -4) / 0.04 + 100000 / 1.04 ** 4)
chk(p6b, 96370.11, 1e-7)
ann = bond_price(100000, 0.06, 0.08, 2, 1)
nodisc = 4 * 3000 + 100000 / 1.04 ** 4
swap = bond_price(100000, 0.08, 0.06, 2, 2)
assert [round(p6b), round(ann), round(nodisc), round(swap)] == [96370, 96433, 97480, 103717]
addn(T2, 3,
     'Trái phiếu mệnh giá 100.000 đồng, lãi suất coupon 6%/năm, trả lãi 6 tháng một lần, còn đúng 2 năm đến ngày đáo hạn (vừa trả lãi). Lợi suất đáo hạn yêu cầu là 8%/năm, ghép lãi 6 tháng (4%/kỳ). Giá trái phiếu (làm tròn đến đồng) là:',
     [round(p6b), round(ann), round(nodisc), round(swap)], dong,
     'Mỗi kỳ coupon 3.000 đồng, 4 kỳ, lợi suất 4%/kỳ: P = 3.000 × [1 − 1,04^−4]/0,04 + 100.000/1,04^4 = 10.889,69 + 85.480,42 ≈ 96.370 đồng. 96.433 là tính như trả lãi hằng năm (6.000 đồng, chiết khấu 8%, 2 kỳ); 97.480 là không chiết khấu các khoản coupon; 103.717 là đảo lãi suất coupon và lợi suất.',
     'P = Σ (C/m)/(1 + y/m)^t + F/(1 + y/m)^(n×m)')

# B7 – thay đổi giá khi lợi suất tăng
p_up = bond_price(100000, 0.07, 0.08, 3)
p_dn = bond_price(100000, 0.07, 0.06, 3)
chg = p_up / 100000 - 1
chk(p_up, 97422.903, 1e-7); chk(p_dn, 102673.012, 1e-7)
addn(T2, 3,
     'Trái phiếu mệnh giá 100.000 đồng, lãi suất coupon 7%/năm trả hằng năm, còn đúng 3 năm đến ngày đáo hạn, đang giao dịch bằng mệnh giá (YTM = 7%). Nếu lợi suất đáo hạn tăng lên 8%/năm ngay sau đó, giá trái phiếu thay đổi xấp xỉ:',
     [chg, -0.03, -0.01, p_dn / 100000 - 1], lambda v: pc(v, 2, sign=True),
     'Giá mới = 7.000/1,08 + 7.000/1,08² + 107.000/1,08³ ≈ 97.423 đồng → thay đổi = (97.423 − 100.000)/100.000 ≈ −2,58%. Lợi suất tăng thì giá giảm; +2,67% là mức thay đổi nếu lợi suất giảm xuống 6% (giá 102.673 đồng); −3,00% là nhân kỳ hạn với mức tăng lợi suất; −1,00% là coi giá giảm đúng bằng mức tăng lợi suất.',
     'Giá trái phiếu là giá trị hiện tại của dòng tiền; giá và lợi suất biến động ngược chiều')

# ====================== sắp xếp đáp án và xuất ======================
assert len(Q) == 40, len(Q)
assert [sum(1 for x in Q if x['topic'] == t) for t in (T1, T2)] == [24, 16]
assert [sum(1 for x in Q if x['lv'] == l) for l in (1, 2, 3)] == [8, 14, 18]
cnt = [0, 0, 0, 0]
pos = [None] * len(Q)
for i, x in enumerate(Q):
    if x['key'] is not None:
        order = sorted(range(4), key=lambda k: x['key'][k])
        x['o'] = [x['o'][k] for k in order]
        pos[i] = order.index(0)
        cnt[pos[i]] += 1
target = [10, 10, 10, 10]
need = [t - c for t, c in zip(target, cnt)]
assert min(need) >= 0, (cnt, need)
free = [i for i in range(len(Q)) if pos[i] is None]
for seed in range(2026, 5000):  # seed đầu tiên không tạo chuỗi >= 4 đáp án trùng vị trí liên tiếp
    pool = [p for p in range(4) for _ in range(need[p])]
    random.Random(seed).shuffle(pool)
    trial = pos[:]
    for i, p in zip(free, pool):
        trial[i] = p
    if all(len(set(trial[k:k + 4])) > 1 for k in range(len(trial) - 3)):
        break
else:
    raise SystemExit('no seed')
for i in free:
    o = Q[i]['o'][1:]
    o.insert(trial[i], Q[i]['o'][0])
    Q[i]['o'] = o
pos = trial

out = []
for i, x in enumerate(Q):
    out.append({'id': f'C5-{i+1:03d}', 'part': 'CM', 'subject': 'MG', 'topic': x['topic'],
                'level': x['lv'], 'q': x['q'], 'o': x['o'], 'a': pos[i], 'e': x['e'],
                'basis': x['basis'], 'quote': '', 'src': GT, 'as_of': '2026-11'})
json.dump(out, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
nums = {}
for i, r in enumerate(out):
    if Q[i]['key'] is not None:
        assert sorted(Q[i]['key'])[r['a']] == Q[i]['key'][0], r['id']
        nums[r['id']] = [Q[i]['val'], r['o'][r['a']]]
json.dump(nums, open(D + 'work_c5/num_answers.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('wrote', len(out), 'seed', seed, 'numeric-sorted positions', cnt, 'final', [pos.count(k) for k in range(4)])
