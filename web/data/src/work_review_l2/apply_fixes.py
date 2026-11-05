# Second-pass review fixes to luat_2.json and so_lieu.json. ALREADY APPLIED (2026-11-04); not idempotent (pass 1
# appends 3 flashcards), so to redo: restore luat_2.orig.json / so_lieu.orig.json from this folder first, then run.
import json, pathlib
SRC = pathlib.Path('/home/user/cchn_moi/web/data/src')
MD = 'Web_TT96_hop_nhat_2026_va_ND128_2021_trich.md'

qs = json.loads((SRC / 'luat_2.json').read_text(encoding='utf-8'))
by = {x['id']: x for x in qs}

def setq(i, **kw):
    x = by['L2-%03d' % i]
    for k, v in kw.items():
        assert k in x, k
        x[k] = v

def opt(i, j, text):
    by['L2-%03d' % i]['o'][j] = text

setq(6, q='Theo Nghị định 155/2020/NĐ-CP, khi công ty đại chúng chào bán trái phiếu chuyển đổi ra công chúng mà không có tổ chức bảo lãnh phát hành cam kết nhận mua toàn bộ hoặc mua phần còn lại, điều kiện về quy mô đợt chào bán là:')

setq(10,
     q='Công ty đại chúng Z (vốn điều lệ 500 tỷ đồng) chào bán thêm 10 triệu cổ phiếu ra công chúng (tổng mệnh giá 100 tỷ đồng) cho cổ đông hiện hữu theo tỷ lệ sở hữu. Số cổ phiếu cổ đông không đăng ký mua có tổng mệnh giá 70 tỷ đồng; HĐQT dự kiến phân phối toàn bộ cho một nhà đầu tư tổ chức (nhà đầu tư này và người có liên quan chưa sở hữu cổ phiếu Z). Việc phân phối này:',
     e='70 tỷ đồng bằng 14% vốn điều lệ trước đợt chào bán và khoảng 11,7% vốn điều lệ sau đợt chào bán (600 tỷ đồng), cách tính nào cũng từ 10% trở lên → theo điểm b khoản 3 Điều 42, việc phân phối cho tổ chức, cá nhân và người có liên quan từ 10% vốn điều lệ trở lên (một đợt hoặc trong 12 tháng gần nhất) phải được ĐHĐCĐ thông qua.')

opt(16, 3, 'Bình quân giá tham chiếu 60 ngày giao dịch liền trước ngày gửi giấy đăng ký')
opt(19, 3, 'Không có nợ phải trả quá hạn trên 01 năm khi đăng ký niêm yết')
opt(25, 2, 'Trên 50% phiếu của cổ đông không phải cổ đông lớn; sau tối thiểu 02 năm')
setq(25, q='Theo Nghị định 155/2020/NĐ-CP, điều kiện để tổ chức niêm yết được hủy bỏ niêm yết cổ phiếu tự nguyện là:')
opt(37, 3, '30 ngày kể từ ngày kết quả thi được thông báo trên trang thông tin điện tử')

setq(44,
     q='Công ty đại chúng P (tổng tài sản theo BCTC gần nhất 2.000 tỷ đồng; Điều lệ không quy định tỷ lệ khác) dự kiến ký hợp đồng mua bán hàng hóa trị giá 600 tỷ đồng với cổ đông Q sở hữu 15% vốn cổ phần phổ thông; trong 12 tháng gần nhất P chưa có giao dịch nào khác với Q. Cấp có thẩm quyền chấp thuận giao dịch là:',
     e='600/2.000 = 30% < 35%, và không có giao dịch nào khác với Q trong 12 tháng để cộng dồn. Theo khoản 5 Điều 293 (sửa đổi bởi NĐ 245), HĐQT chấp thuận giao dịch tại điểm b khoản 4 (với cổ đông sở hữu trên 10% vốn cổ phần phổ thông...) có giá trị nhỏ hơn 35% tổng tài sản; giao dịch (hoặc tổng giao dịch trong 12 tháng) từ 35% trở lên mới thuộc thẩm quyền ĐHĐCĐ. Điểm c khoản 4 (trên 10%) chỉ áp dụng với cổ đông sở hữu từ 51%.')

opt(45, 1, 'Phải được Đại hội đồng cổ đông chấp thuận trước khi thực hiện')

setq(66,
     q='Theo Thông tư 91/2020/TT-BTC (sửa đổi, bổ sung bởi Thông tư 102/2025/TT-BTC), khoản nào sau đây được trừ ra khỏi tổng chi phí phát sinh trong kỳ khi xác định chi phí để tính rủi ro hoạt động của công ty chứng khoán?',
     o=['Chi phí chênh lệch do đánh giá lại phải trả chứng quyền đang lưu hành',
        'Chi phí tiền lương, phụ cấp trả cho người lao động của công ty',
        'Chi phí thuê trụ sở chính, chi nhánh và phòng giao dịch của công ty',
        'Chi phí thuê ngoài dịch vụ công nghệ thông tin và đường truyền'],
     a=0,
     e='Khoản 2 Điều 8 TT 91 (TT 102/2025 thay cụm từ "chi phí duy trì hoạt động" bằng "chi phí để tính rủi ro hoạt động" và bổ sung điểm h, i, k): chi phí để tính rủi ro hoạt động của CTCK = tổng chi phí phát sinh trong kỳ trừ khấu hao, chi phí/hoàn nhập dự phòng, chênh lệch giảm do đánh giá lại tài sản tài chính FVTPL, chi phí lãi vay và (bổ sung) chênh lệch do đánh giá lại phải trả chứng quyền đang lưu hành, chênh lệch tỷ giá chưa thực hiện, chi phí tài chính và chi phí không bằng tiền khác. Lương, thuê trụ sở, dịch vụ CNTT là chi phí hoạt động bằng tiền nên không được trừ.',
     basis='Điểm h khoản 2 Điều 8 Thông tư 91/2020/TT-BTC (bổ sung bởi khoản 1 Điều 5 Thông tư 102/2025/TT-BTC; cụm từ "chi phí để tính rủi ro hoạt động" theo khoản 2 Điều 8 Thông tư 102/2025/TT-BTC)',
     quote='Bổ sung điểm h, i, k vào sau điểm g khoản 2 như sau: “h) Chi phí chênh lệch do đánh giá lại phải trả chứng quyền đang lưu hành;',
     src='TT_102_2025_TT-BTC_sua_TT91.txt')

opt(76, 2, 'Phải CBTT trong 05 ngày làm việc sau giao dịch ngày T+3 do vượt ngưỡng 8%')

setq(92,
     q='Theo Nghị định 156/2020/NĐ-CP (sửa đổi bởi Nghị định 128/2021/NĐ-CP), một tổ chức có hành vi sử dụng thông tin nội bộ để mua, bán chứng khoán (chưa đến mức truy cứu trách nhiệm hình sự) bị phạt tiền ở mức nào?',
     o=['05 lần khoản thu trái pháp luật, không thấp hơn 1,5 tỷ đồng',
        '10 lần khoản thu trái pháp luật, không thấp hơn 3 tỷ đồng',
        '02 lần khoản thu trái pháp luật, không thấp hơn 3 tỷ đồng',
        '10 lần khoản thu trái pháp luật, tối đa không quá 3 tỷ đồng'],
     a=1,
     e='Khoản 1 Điều 35 (sửa đổi bởi khoản 29 Điều 1 NĐ 128/2021): phạt tiền 10 lần khoản thu trái pháp luật nhưng không thấp hơn mức phạt tiền tối đa tại điểm b khoản 3 Điều 5 (3 tỷ đồng đối với tổ chức); không có khoản thu trái pháp luật hoặc mức tính theo khoản thu thấp hơn thì phạt 3 tỷ đồng. Mức phạt Chương II áp dụng cho tổ chức; cá nhân vi phạm như tổ chức bị phạt bằng 1/2 (tức 05 lần, không thấp hơn 1,5 tỷ đồng). NĐ 306/2025 không sửa Điều 35.',
     basis='Khoản 1 Điều 35 Nghị định 156/2020/NĐ-CP (sửa đổi bởi khoản 29 Điều 1 Nghị định 128/2021/NĐ-CP); điểm b, c khoản 3 Điều 5 (sửa đổi bởi khoản 4 Điều 1 Nghị định 128/2021/NĐ-CP)',
     quote='Phạt tiền 10 lần khoản thu trái pháp luật nhưng không thấp hơn mức phạt tiền tối đa quy định tại điểm b khoản 3 Điều 5 Nghị định này đối với hành vi sử dụng thông tin nội bộ để mua, bán chứng khoán',
     src=MD)

setq(95,
     q='Theo Nghị định 156/2020/NĐ-CP (sửa đổi bởi Nghị định 128/2021/NĐ-CP), đối với hành vi vi phạm hành chính trong lĩnh vực chứng khoán đã kết thúc, thời hiệu xử phạt được tính từ thời điểm nào?',
     o=['Thời điểm người có thẩm quyền phát hiện hành vi vi phạm',
        'Thời điểm bắt đầu thực hiện hành vi vi phạm',
        'Thời điểm lập biên bản vi phạm hành chính',
        'Thời điểm chấm dứt hành vi vi phạm'],
     e='Khoản 2 Điều 6 (sửa đổi bởi khoản 5 Điều 1 NĐ 128/2021): hành vi đang thực hiện → thời hiệu tính từ thời điểm người có thẩm quyền thi hành công vụ phát hiện; hành vi đã kết thúc → tính từ thời điểm chấm dứt hành vi vi phạm. Khoản 3 Điều 6 xác định riêng thời điểm chấm dứt cho một số hành vi (ví dụ chậm công bố thông tin: ngày thực hiện công bố).',
     basis='Điểm b khoản 2 Điều 6 Nghị định 156/2020/NĐ-CP (sửa đổi bởi khoản 5 Điều 1 Nghị định 128/2021/NĐ-CP)',
     quote='Đối với hành vi vi phạm hành chính đã kết thúc thì thời hiệu được tính từ thời điểm chấm dứt hành vi vi phạm.',
     src=MD)

(SRC / 'luat_2.json').write_text(json.dumps(qs, ensure_ascii=False, indent=1), encoding='utf-8')

# flashcards
fc = json.loads((SRC / 'so_lieu.json').read_text(encoding='utf-8'))
def card(n, **kw):
    c = fc[n - 1]
    for k, v in kw.items():
        assert k in c, k
        c[k] = v
assert fc[30]['front'].startswith('CCHN: thời hạn thi lại')
card(31, back='Trong 01 năm từ ngày thông báo kết quả lần đầu hoặc kỳ thi gần nhất liền sau (quá hạn thi lại cả hai phần); 20 ngày')
assert fc[38]['front'].startswith('TT 91: giá trị rủi ro hoạt động')
card(39, back='Max (25% chi phí để tính rủi ro hoạt động trong 12 tháng liền kề; 20% vốn điều lệ tối thiểu cho các nghiệp vụ)',
     basis='Khoản 1 Điều 8 TT 91/2020/TT-BTC (cụm từ thay thế bởi khoản 2 Điều 8 TT 102/2025/TT-BTC)')
assert fc[47]['front'].startswith('NĐ 156:')
card(48, front='NĐ 156: phạt tiền tổ chức sử dụng thông tin nội bộ, thao túng; tước CCHN; đình chỉ CTCK',
     back='10 lần khoản thu trái pháp luật, không thấp hơn 3 tỷ đồng (cá nhân: 1/2); 18–24 tháng; 01–03 tháng',
     basis='Khoản 1 Điều 35, 36 NĐ 156/2020 (sửa đổi bởi khoản 29, 30 Điều 1 NĐ 128/2021/NĐ-CP); khoản 2 Điều 35, 36 NĐ 156/2020/NĐ-CP')
fc += [
    {'front': 'Thi sát hạch CCHN 2026: thời gian làm bài môi giới / phân tích tài chính / quản lý quỹ',
     'back': '120 / 150 / 180 phút (mỗi phần 60 / 75 / 90 phút)',
     'basis': 'Thông báo số 11 của Hội đồng thi sát hạch – UBCKNN (đợt III năm 2026)', 'topic': 'Chứng chỉ hành nghề chứng khoán'},
    {'front': 'Thi sát hạch CCHN từ 2026: điều kiện đạt; phúc khảo',
     'back': 'Đúng từ 60% câu hỏi trở lên ở mỗi phần (thi lại một phần: từ 60% phần thi lại); không phúc khảo bài thi trắc nghiệm trên máy tính',
     'basis': 'Thông báo số 01/TB-HĐTSH và số 09/TB-HĐTSH năm 2026 của Hội đồng thi sát hạch – UBCKNN', 'topic': 'Chứng chỉ hành nghề chứng khoán'},
    {'front': 'Chi phí dự thi sát hạch CCHN chứng khoán từ năm 2026',
     'back': '1.000.000 đồng/thí sinh/loại chứng chỉ (thi mới và thi lại)',
     'basis': 'Mục 5.1 Thông báo số 01/TB-HĐTSH năm 2026 của Hội đồng thi sát hạch – UBCKNN', 'topic': 'Chứng chỉ hành nghề chứng khoán'},
]
(SRC / 'so_lieu.json').write_text('[\n' + ',\n'.join(' ' + json.dumps(c, ensure_ascii=False) for c in fc) + '\n]\n', encoding='utf-8')
print('done', len(qs), len(fc))

# pass 2: option-length cues (run after pass 1; idempotent)
qs = json.loads((SRC / 'luat_2.json').read_text(encoding='utf-8'))
by = {x['id']: x for x in qs}
by['L2-004']['o'][0] = 'Moody’s, S&P, Fitch Ratings và doanh nghiệp XHTN được Bộ Tài chính cấp phép'
by['L2-004']['o'][1] = 'Chỉ các doanh nghiệp XHTN được Bộ Tài chính cấp Giấy chứng nhận'
by['L2-010']['o'][1:] = ['Do HĐQT quyết định vì nhà đầu tư chưa phải là cổ đông lớn của công ty',
                         'Chỉ cần báo cáo UBCKNN trước khi HĐQT thực hiện việc phân phối',
                         'Phải được Ban kiểm soát chấp thuận bằng văn bản trước khi phân phối']
by['L2-076']['o'][2] = 'Phải CBTT trong 05 ngày làm việc từ ngày T+3 do vượt ngưỡng 8%'
(SRC / 'luat_2.json').write_text(json.dumps(qs, ensure_ascii=False, indent=1), encoding='utf-8')
print('pass 2 done')
