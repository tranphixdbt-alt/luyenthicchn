import json
P='/home/user/cchn_moi/web/data/src/cm_3.json'
d=json.load(open(P,encoding='utf-8')); I={x['id']:x for x in d}
SRTC='Giáo trình SRTC (khung chương trình)'
def setopt(i,k,v):
    I[i]['o'][k]=v
def rep(i,**kw):
    x=I[i]; x.update(kw)
    if 'quote' not in kw and kw.get('src')==SRTC: x['quote']=''

# --- option-length balancing / wording ---
setopt('C3-001',1,'Tối đa hóa giá trị tài sản của cổ đông, thể hiện qua giá cổ phiếu')
setopt('C3-002',1,'Chi phí kiểm toán độc lập và thưởng cổ phiếu để giám sát, ràng buộc ban điều hành')
setopt('C3-009',2,'Chọn theo NPV, vì NPV đo trực tiếp giá trị tăng thêm cho cổ đông')
setopt('C3-011',1,'Là chi phí cơ hội, bằng tỷ suất sinh lời mà cổ đông đòi hỏi trên vốn cổ phần')
setopt('C3-011',3,'Cao hơn chi phí sử dụng vốn cổ phiếu mới vì đã chịu thuế TNDN')
setopt('C3-019',3,'Cổ tức hiện tại ít rủi ro hơn lãi vốn kỳ vọng nên tỷ lệ chi trả cao có thể làm tăng giá trị doanh nghiệp')
setopt('C3-020',1,'Làm giảm hệ số nợ trên vốn chủ sở hữu của doanh nghiệp sau khi mua lại')
setopt('C3-020',2,'Làm tăng tổng vốn chủ sở hữu và giá trị sổ sách của doanh nghiệp')
setopt('C3-020',3,'Phát tín hiệu cổ phiếu bị định giá thấp, không tạo kỳ vọng phải duy trì mức chi trả hằng năm')
setopt('C3-030',3,'Xác định giá chào bán và phân bổ cổ phiếu dựa trên nhu cầu đặt mua của nhà đầu tư')
setopt('C3-036',0,'Nhà đầu tư muốn thoái vốn phải bán chứng chỉ quỹ trên thị trường, giá có thể lệch khỏi NAV')
setopt('C3-056',0,'Thanh khoản thấp, khó định giá, tương quan thấp với cổ phiếu và trái phiếu truyền thống')
setopt('C3-062',0,'Rủi ro phi hệ thống (rủi ro đặc thù doanh nghiệp)')
setopt('C3-062',1,'Rủi ro hệ thống (rủi ro chung của thị trường)')
setopt('C3-073',3,'Chỉ nhằm mục đích phòng ngừa rủi ro cho danh mục của quỹ')
setopt('C3-074',1,'Vị thế tối đa của chứng khoán phái sinh mà nhà đầu tư được quyền nắm giữ tại một thời điểm')
setopt('C3-081',0,'Chỉ số VN30 có thể giảm mạnh trong suốt thời gian thực hiện phòng vệ')
setopt('C3-081',2,'Chênh lệch giữa giá giao ngay và giá HĐTL khi đóng vị thế biến động khó dự đoán')
setopt('C3-081',3,'Bên đối ứng của HĐTL có thể mất khả năng thanh toán khi đáo hạn')

# --- C3-057: 65% threshold applies to the issuer whose securities the REIT invests in ---
rep('C3-057',
 q='Theo định nghĩa quỹ đầu tư bất động sản tại Luật Chứng khoán, quỹ đầu tư chủ yếu vào bất động sản và chứng khoán của tổ chức kinh doanh bất động sản đáp ứng ngưỡng doanh thu nhất định. Công ty X có doanh thu từ việc sở hữu và kinh doanh bất động sản chiếm 60% tổng doanh thu trên báo cáo tài chính năm gần nhất. Nhận định nào sau đây đúng?',
 o=['Chứng khoán của X đạt tiêu chí vì ngưỡng tối thiểu là 50% tổng doanh thu',
    'Chứng khoán của X đạt tiêu chí vì ngưỡng tối thiểu là 51% tổng doanh thu',
    'Chứng khoán của X chưa đạt tiêu chí vì ngưỡng tối thiểu là 65% tổng doanh thu',
    'Luật không đặt ngưỡng doanh thu, chỉ xét ngành nghề đăng ký kinh doanh của X'],
 a=2,
 e='Khoản 43 Điều 4: quỹ đầu tư bất động sản đầu tư chủ yếu vào bất động sản và chứng khoán của tổ chức kinh doanh bất động sản có doanh thu từ sở hữu, kinh doanh bất động sản tối thiểu 65% tổng doanh thu tính trên báo cáo tài chính năm gần nhất; X mới đạt 60% nên chứng khoán của X chưa thuộc nhóm tài sản này.',
 quote='Quỹ đầu tư bất động sản là quỹ đầu tư chứng khoán được đầu tư chủ yếu vào bất động sản và chứng khoán của tổ chức phát hành là tổ chức kinh doanh bất động sản có doanh thu từ việc sở hữu và kinh doanh bất động sản tối thiểu là 65% tổng doanh thu tính trên báo cáo tài chính năm gần nhất.')

# --- replacements of near-duplicates of cm_1 / cm_2 items ---
rep('C3-010',
 q='Doanh nghiệp có vốn chủ sở hữu giá trị sổ sách 250 tỷ đồng, giá trị thị trường 700 tỷ đồng; nợ vay có giá trị sổ sách và giá trị thị trường đều là 300 tỷ đồng. Chi phí vốn chủ sở hữu 14%, lãi suất vay trước thuế 9%, thuế suất thuế TNDN 20%. WACC tính theo trọng số giá trị thị trường là bao nhiêu?',
 o=['10,29%','10,60%','11,96%','12,50%'], a=2,
 e='Trọng số thị trường: E = 700/1.000 = 70%, D = 300/1.000 = 30%. Chi phí nợ sau thuế = 9% × (1 − 20%) = 7,2%. WACC = 70% × 14% + 30% × 7,2% = 9,80% + 2,16% = 11,96%. Dùng trọng số sổ sách (250/550 và 300/550) cho 10,29%; bình quân giản đơn (14% + 7,2%)/2 cho 10,60%; bỏ qua lá chắn thuế lãi vay cho 12,50%.')
rep('C3-021',
 q='Công ty P có lợi nhuận sau thuế năm nay 200 tỷ đồng, ngân sách vốn đầu tư năm tới 250 tỷ đồng và duy trì cơ cấu vốn mục tiêu 60% vốn chủ sở hữu, 40% nợ vay. Nếu P áp dụng chính sách cổ tức thặng dư (residual dividend policy), tổng cổ tức chi trả năm nay là bao nhiêu?',
 o=['0 tỷ đồng','50 tỷ đồng','100 tỷ đồng','150 tỷ đồng'], a=1,
 e='Phần vốn chủ sở hữu cần cho ngân sách đầu tư = 60% × 250 = 150 tỷ đồng, được tài trợ trước bằng lợi nhuận giữ lại. Cổ tức thặng dư = 200 − 150 = 50 tỷ đồng (tỷ lệ chi trả 25%). Dùng nhầm tỷ trọng nợ 40% cho 100 tỷ; coi toàn bộ vốn đầu tư phải lấy từ lợi nhuận (200 < 250) cho 0; nhầm phần vốn chủ sở hữu cần giữ lại là cổ tức cho 150 tỷ.',
 basis='Chính sách cổ tức thặng dư: Cổ tức = LNST − Tỷ trọng VCSH mục tiêu × Ngân sách vốn đầu tư', src=SRTC)
rep('C3-039',
 q='Cổ phiếu A có độ lệch chuẩn 20%, cổ phiếu B có độ lệch chuẩn 10%, hệ số tương quan giữa A và B là 0,3. Tỷ trọng cổ phiếu A trong danh mục có phương sai nhỏ nhất (chỉ gồm A và B, không bán khống) xấp xỉ bao nhiêu?',
 o=['10,5%','20,0%','33,3%','89,5%'], a=0,
 e='wA = (σB² − ρσAσB)/(σA² + σB² − 2ρσAσB) = (0,01 − 0,3 × 0,2 × 0,1)/(0,04 + 0,01 − 2 × 0,3 × 0,2 × 0,1) = 0,004/0,038 ≈ 10,5% (wB ≈ 89,5%; σp nhỏ nhất ≈ 9,79% < σB). Bỏ qua tương quan (ρ = 0) cho σB²/(σA² + σB²) = 20,0%; tỷ trọng theo nghịch đảo độ lệch chuẩn σB/(σA + σB) cho 33,3%; 89,5% là tỷ trọng của B.',
 basis='Danh mục phương sai nhỏ nhất hai tài sản: wA = (σB² − ρσAσB)/(σA² + σB² − 2ρσAσB)', src=SRTC)
rep('C3-040',
 q='Cổ phiếu K đang có giá 50.000 đ; chuyên viên phân tích dự báo sau 1 năm giá K đạt 54.000 đ và K trả cổ tức 1.500 đ/cp. Lãi suất phi rủi ro 5%/năm, lợi suất kỳ vọng của danh mục thị trường 12%/năm, beta của K là 1,1. Theo CAPM, tỷ suất sinh lời yêu cầu của K và khuyến nghị phù hợp là:',
 o=['12,7%; K bị định giá cao (nằm dưới SML), nên bán',
    '12,7%; K bị định giá thấp (nằm trên SML), nên mua',
    '13,2%; K bị định giá cao (nằm dưới SML), nên bán',
    '7,7%; K bị định giá thấp (nằm trên SML), nên mua'], a=0,
 e='Lợi suất kỳ vọng dự báo = (54.000 − 50.000 + 1.500)/50.000 = 11,0%. Lợi suất yêu cầu = 5% + 1,1 × (12% − 5%) = 12,7%. 11,0% < 12,7% → K nằm dưới SML (alpha âm), bị định giá cao → nên bán. 13,2% là lỗi nhân beta với cả lợi suất thị trường; 7,7% là quên cộng lãi suất phi rủi ro.',
 basis='CAPM: E(Ri) = rf + βi[E(Rm) − rf]; so sánh lợi suất dự báo với SML', src=SRTC)
rep('C3-050',
 q='Quỹ mua trái phiếu kỳ hạn 3 năm, mệnh giá 100, lãi suất coupon 8%/năm trả cuối mỗi năm, với lợi suất đáo hạn 10%/năm. Sau 1 năm, ngay sau khi nhận coupon, lợi suất đáo hạn của trái phiếu giảm xuống 9%/năm và quỹ bán trái phiếu. Tỷ suất sinh lời trong thời gian nắm giữ 1 năm của quỹ xấp xỉ bao nhiêu?',
 o=['3,38%','8,42%','10,00%','11,80%'], a=3,
 e='Giá mua P0 = 8/1,1 + 8/1,1² + 108/1,1³ = 95,03. Giá bán (còn 2 năm, YTM 9%) P1 = 8/1,09 + 108/1,09² = 98,24. HPR = (98,24 − 95,03 + 8)/95,03 ≈ 11,80%. Bỏ qua coupon cho 3,38%; chỉ tính lợi suất hiện hành 8/95,03 cho 8,42%; giả định lợi suất không đổi (bằng YTM ban đầu) cho 10,00%.',
 basis='Tỷ suất sinh lời nắm giữ trái phiếu: HPR = (P1 − P0 + Coupon)/P0; định giá trái phiếu theo YTM', src=SRTC)
rep('C3-051',
 q='Danh mục trái phiếu gồm: 40 tỷ đồng trái phiếu X (duration điều chỉnh 2,0), 60 tỷ đồng trái phiếu Y (duration điều chỉnh 5,0) và 100 tỷ đồng trái phiếu Z (duration điều chỉnh 8,0), tính theo giá thị trường. Nếu lợi suất của tất cả trái phiếu cùng tăng 50 điểm cơ bản, bỏ qua độ lồi, giá trị danh mục thay đổi xấp xỉ bao nhiêu?',
 o=['−0,59 tỷ đồng','−5,00 tỷ đồng','−5,90 tỷ đồng','−11,80 tỷ đồng'], a=2,
 e='Duration điều chỉnh danh mục = (40 × 2 + 60 × 5 + 100 × 8)/200 = 5,9. ΔV ≈ −Dmod × Δy × V = −5,9 × 0,005 × 200 = −5,90 tỷ đồng. Bình quân giản đơn duration (5,0) cho −5,00 tỷ; coi 50 điểm cơ bản là 1% cho −11,80 tỷ; coi 50 điểm cơ bản là 0,05% cho −0,59 tỷ.',
 basis='Duration danh mục = bình quân gia quyền theo giá trị thị trường; ΔV ≈ −Dmod·Δy·V', src=SRTC)
rep('C3-063',
 q='Lợi suất một năm của cổ phiếu T theo các kịch bản: tăng trưởng (xác suất 25%) +30%; bình thường (xác suất 50%) +12%; suy thoái (xác suất 25%) −10%. Hệ số biến thiên (CV = độ lệch chuẩn/lợi suất kỳ vọng) của T xấp xỉ bao nhiêu?',
 o=['0,78','1,29','1,49','1,63'], a=1,
 e='E(R) = 0,25 × 30 + 0,5 × 12 + 0,25 × (−10) = 11%. σ² = 0,25 × 19² + 0,5 × 1² + 0,25 × (−21)² = 90,25 + 0,5 + 110,25 = 201 → σ ≈ 14,18%. CV = 14,18/11 ≈ 1,29 (mỗi đơn vị lợi suất kỳ vọng gánh 1,29 đơn vị rủi ro). Đảo tỷ số cho 0,78; bỏ qua xác suất (bình quân giản đơn, σ ≈ 16,36%) cho 1,49; không trừ lợi suất kỳ vọng khi tính σ (17,94%) cho 1,63.',
 basis='Lợi suất kỳ vọng, độ lệch chuẩn theo kịch bản và hệ số biến thiên CV = σ/E(R)', src=SRTC)
rep('C3-083',
 q='Nhà đầu tư mua chứng quyền có bảo đảm loại mua với giá P (đồng/chứng quyền), giá thực hiện K, tỷ lệ chuyển đổi n:1 (n chứng quyền tương ứng 1 chứng khoán cơ sở). Bỏ qua thuế, phí, nếu nắm giữ đến đáo hạn thì giá hòa vốn của chứng khoán cơ sở được xác định bằng:',
 o=['K + P/n','K + P × n','K − P × n','K + P'], a=1,
 e='Khi đáo hạn mỗi chứng quyền mua nhận (S − K)/n; hòa vốn khi (S − K)/n = P ⇒ S = K + P × n. Ví dụ K = 25.000 đ, P = 1.000 đ, n = 2 thì giá hòa vốn là 27.000 đ. K + P/n là chia nhầm cho tỷ lệ chuyển đổi; K − P × n là giá hòa vốn của chứng quyền bán; K + P bỏ qua tỷ lệ chuyển đổi.',
 basis='Giá hòa vốn chứng quyền mua = Giá thực hiện + Giá chứng quyền × Tỷ lệ chuyển đổi', src=SRTC)
rep('C3-084',
 q='Nhà đầu tư mua 20.000 chứng quyền mua (kiểu châu Âu, thanh toán bằng tiền) với giá 1.200 đ/chứng quyền; tỷ lệ chuyển đổi 2:1 (2 chứng quyền tương ứng 1 cổ phiếu cơ sở), giá thực hiện 45.000 đ. Giá thanh toán tại ngày đáo hạn là 49.800 đ. Lợi nhuận của nhà đầu tư (bỏ qua thuế, phí) là bao nhiêu?',
 o=['24.000.000 đ','36.000.000 đ','48.000.000 đ','72.000.000 đ'], a=0,
 e='Khoản thanh toán mỗi chứng quyền = (49.800 − 45.000)/2 = 2.400 đ; lợi nhuận = (2.400 − 1.200) × 20.000 = 24.000.000 đ. Quên tỷ lệ chuyển đổi cho 72.000.000 đ; chưa trừ giá mua cho 48.000.000 đ; chia cả giá mua cho tỷ lệ chuyển đổi cho 36.000.000 đ.')
open(P,'w',encoding='utf-8').write(json.dumps(d,ensure_ascii=False,indent=1))
