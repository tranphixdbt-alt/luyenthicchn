# Applies the second-pass review edits to cm_9.json (idempotent: always starts from cm_9.orig.json).
import json
from pathlib import Path

HERE = Path(__file__).parent
d = json.loads((HERE / 'cm_9.orig.json').read_text(encoding='utf-8'))
Q = {q['id']: q for q in d}
PT = 'Giáo trình Phân tích và đầu tư chứng khoán (UBCKNN/SRTC) – '
MG = 'Giáo trình Môi giới và tư vấn đầu tư chứng khoán (UBCKNN/SRTC) – '

def put(i, **kw):
    Q[i].update(kw)

# duplicate of C2-011 (SML over/undervaluation) -> infer E(Rm) from two correctly priced stocks
put('C9-008', level=3,
    q='Theo CAPM, hai cổ phiếu A và B đều đang được định giá hợp lý (nằm đúng trên đường SML). Cổ phiếu A có beta 0,8 và lợi suất kỳ vọng 10,0%; cổ phiếu B có beta 1,4 và lợi suất kỳ vọng 14,2%. Lợi suất kỳ vọng của danh mục thị trường là bao nhiêu?',
    o=['11,40%', '7,00%', '12,10%', '12,50%'], a=0,
    e='Hai cổ phiếu cùng nằm trên SML nên độ dốc SML (mức bù rủi ro thị trường) = (14,2% − 10,0%)/(1,4 − 0,8) = 7,00%; Rf = 10,0% − 0,8 × 7,00% = 4,40%. Danh mục thị trường có beta bằng 1 ⇒ E(Rm) = 4,40% + 7,00% = 11,40%. Lỗi thường gặp: coi độ dốc SML là lợi suất thị trường (7,00%), lấy bình quân giản đơn lợi suất hai cổ phiếu (12,10%), lấy lợi suất chia beta (10,0%/0,8 = 12,50%).',
    basis=PT + 'Đường thị trường chứng khoán (SML): tung độ gốc Rf, độ dốc E(Rm) − Rf')

# duplicate of C2-008 (two-asset sigma) -> N-stock equally weighted portfolio
put('C9-010', level=3,
    q='Danh mục gồm 25 cổ phiếu với tỷ trọng bằng nhau. Mỗi cổ phiếu có độ lệch chuẩn lợi suất 40%; hiệp phương sai giữa lợi suất của hai cổ phiếu bất kỳ đều bằng 0,04. Độ lệch chuẩn của danh mục là bao nhiêu?',
    o=['40,00%', '20,00%', '21,17%', '8,00%'], a=2,
    e='Với N cổ phiếu tỷ trọng 1/N: σp² = σ²/N + (1 − 1/N) × Cov = 0,16/25 + 0,96 × 0,04 = 0,0064 + 0,0384 = 0,0448 ⇒ σp = 21,17%. Phần σ²/N (rủi ro riêng) giảm dần khi N tăng; phần hiệp phương sai là rủi ro hệ thống không đa dạng hóa được, nên σp chỉ tiến về √0,04 = 20,00%. Lỗi thường gặp: chỉ giữ phần hiệp phương sai (20,00%), bỏ qua hiệp phương sai (√0,0064 = 8,00%), coi như không có lợi ích đa dạng hóa (40,00%).',
    basis=PT + 'Đa dạng hóa danh mục N tài sản tỷ trọng bằng nhau: σp² = σ²/N + (1 − 1/N) × Cov')

put('C9-011', level=3,
    e='Beta tài sản phi rủi ro bằng 0. βp = 0,3 × 1,4 + 0,2 × 0,9 + 0,5 × 0 = 0,42 + 0,18 = 0,60. Lỗi thường gặp: chỉ tính trên phần cổ phiếu 500 triệu đồng ((0,42 + 0,18)/0,5 = 1,20), bình quân giản đơn ba tài sản (0,77) hoặc hai cổ phiếu (1,15).')

# same angle as C3-080 (number of contracts) -> outcome of the hedge
put('C9-014',
    q='Quỹ nắm giữ danh mục cổ phiếu trị giá 20 tỷ đồng, beta 1,1 so với chỉ số VN30, đã bán 169 hợp đồng tương lai chỉ số VN30 ở mức 1.300 điểm (hệ số nhân 100.000 đồng/điểm) để phòng ngừa rủi ro thị trường. Sau đó chỉ số VN30 giảm 5%, giá hợp đồng tương lai cũng giảm 5% về 1.235 điểm và danh mục biến động đúng theo beta. Quỹ đóng vị thế hợp đồng tương lai; bỏ qua cổ tức, phí và chi phí ký quỹ. Kết quả ròng của danh mục cộng vị thế hợp đồng tương lai xấp xỉ là',
    o=['Lỗ 1.100,0 triệu đồng', 'Lãi 98,5 triệu đồng', 'Lỗ 2.198,5 triệu đồng', 'Lỗ 1,5 triệu đồng'], a=3,
    e='Danh mục: 20 tỷ × 1,1 × (−5%) = −1.100 triệu đồng. Vị thế bán hợp đồng tương lai: 169 × (1.300 − 1.235) × 100.000 = +1.098,5 triệu đồng. Kết quả ròng = −1.100 + 1.098,5 = −1,5 triệu đồng ≈ 0: phòng ngừa đưa beta về xấp xỉ 0 nên lãi/lỗ do thị trường gần như được bù trừ (phần lệch nhỏ do làm tròn số hợp đồng 1,1 × 20 tỷ/130 triệu = 169,2). Lỗi thường gặp: chỉ tính danh mục (lỗ 1.100,0 triệu), bỏ qua beta khi tính lỗ danh mục (−1.000 + 1.098,5 = lãi 98,5 triệu), nhầm chiều vị thế như khi mua hợp đồng tương lai (lỗ 2.198,5 triệu).',
    basis=PT + 'Phòng ngừa rủi ro hệ thống bằng hợp đồng tương lai chỉ số: kết quả của danh mục đã phòng ngừa')

# distractor 5,45 did not match the stated mistake (0,6 x 1,06/0,11 = 5,78)
put('C9-018', level=3,
    o=['12,72 lần', '12,00 lần', '5,78 lần', '8,48 lần'],
    e='P0 = D0(1 + g)/(r − g) ⇒ P0/E0 = tỷ lệ chi trả × (1 + g)/(r − g) = 0,6 × 1,06/0,05 = 12,72 lần. 12,00 lần là P/E tính trên EPS năm tới (P0/E1 = 0,6/0,05); 5,78 lần là quên trừ g ở mẫu số (0,6 × 1,06/0,11); 8,48 lần là dùng nhầm tỷ lệ giữ lại 40% (0,4 × 1,06/0,05).')

# exact duplicate of C5-028 (c > CY > YTM) -> realized yield / reinvestment risk
put('C9-021', level=3,
    q='Nhà đầu tư mua trái phiếu mệnh giá 100.000 đồng, coupon 10%/năm trả cuối mỗi năm, còn đúng 2 năm đến hạn, với giá bằng mệnh giá (YTM = 10%/năm) và nắm giữ đến ngày đáo hạn. Coupon năm thứ nhất chỉ tái đầu tư được với lãi suất 6%/năm cho đến ngày đáo hạn. Lợi suất bình quân năm thực tế đạt được (lãi kép) của khoản đầu tư là',
    o=['10,00%', '9,82%', '10,30%', '9,54%'], a=1,
    e='Giá trị cuối năm 2 = 10.000 × 1,06 + 110.000 = 120.600 đồng. Lợi suất thực tế = (120.600/100.000)^(1/2) − 1 = 9,82%, thấp hơn YTM vì coupon được tái đầu tư ở lãi suất thấp hơn YTM (rủi ro tái đầu tư). YTM chỉ đạt được khi nắm giữ đến hạn và mọi coupon được tái đầu tư đúng bằng YTM. Lỗi thường gặp: cho rằng luôn đạt YTM (10,00%), lấy lãi đơn bình quân 20.600/2/100.000 (10,30%), bỏ qua tiền lãi tái đầu tư ((120.000/100.000)^(1/2) − 1 = 9,54%).',
    basis=PT + 'Lợi suất đáo hạn, giả định tái đầu tư coupon và rủi ro tái đầu tư')

put('C9-029', level=3,
    q='Giả sử được phép bán khống. ' + Q['C9-029']['q'])

# same angle as C1-063 (margin-call trigger without interest) -> trigger with accrued interest
put('C9-036',
    q='Khách hàng mua 20.000 cổ phiếu giá 25.000 đồng bằng giao dịch ký quỹ: tự có 50%, vay công ty chứng khoán 50% với lãi suất 13%/năm (lãi đơn, số ngày thực tế/365, lãi cộng dồn vào dư nợ). Giả sử hợp đồng quy định tỷ lệ ký quỹ = (Giá trị chứng khoán − Dư nợ)/Giá trị chứng khoán và tỷ lệ duy trì 30%. Bỏ qua phí; tại ngày thứ 146 kể từ khi vay, tài khoản bị gọi ký quỹ nếu giá cổ phiếu thấp hơn mức xấp xỉ',
    o=['18.786 đồng', '17.857 đồng', '19.714 đồng', '20.000 đồng'], a=0,
    e='Lãi cộng dồn = 250 triệu × 13% × 146/365 = 13 triệu đồng ⇒ dư nợ = 263 triệu đồng. Gọi ký quỹ khi (20.000P − 263.000.000)/(20.000P) = 30% ⇒ P = 263.000.000/(0,7 × 20.000) = 18.786 đồng. Lãi vay làm dư nợ tăng nên ngưỡng giá gọi ký quỹ cao dần theo thời gian. Lỗi thường gặp: bỏ qua lãi (250.000.000/14.000 = 17.857), tính lãi trên toàn bộ giá trị mua 500 triệu đồng (276.000.000/14.000 = 19.714), lấy giá mua giảm đúng chênh lệch tỷ lệ 50% − 30% (20.000).',
    basis=MG + 'Giá gọi ký quỹ khi dư nợ gồm cả lãi vay cộng dồn')

# calculation items: level 3 per SCHEMA (3 = Vận dụng/tính toán), as in the rest of the bank
for i in ['C9-003', 'C9-006', 'C9-022', 'C9-031', 'C9-032', 'C9-040']:
    put(i, level=3)

(HERE.parent / 'cm_9.json').write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding='utf-8')
print('written', len(d))
