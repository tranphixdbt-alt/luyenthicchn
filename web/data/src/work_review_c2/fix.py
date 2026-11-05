import json
P='/home/user/cchn_moi/web/data/src/cm_2.json'
raw=open(P,encoding='utf-8').read()
D=json.loads(raw); X={x['id']:x for x in D}
def opt(i,k,old,new):
    assert X[i]['o'][k]==old,(i,k,X[i]['o'][k]); X[i]['o'][k]=new
def rep(i,f,old,new):
    assert old in X[i][f],(i,f); X[i][f]=X[i][f].replace(old,new)

# C2-009: key was the only option without "Chỉ khi" (test-wise cue)
opt('C2-009',2,"Hệ số tương quan giữa hai cổ phiếu nhỏ hơn +1","Khi hệ số tương quan giữa hai cổ phiếu nhỏ hơn +1, kể cả khi dương")
# C2-010: key much longer than distractors; Rf constancy not stated
rep('C2-010','q',"lãi suất phi rủi ro dương và mức bù rủi ro thị trường không đổi","lãi suất phi rủi ro (dương) và mức bù rủi ro thị trường không đổi")
X['C2-010']['o']=["Mức bù rủi ro và lợi suất yêu cầu của cổ phiếu đều tăng đúng gấp đôi",
 "Mức bù rủi ro thị trường tăng gấp đôi, lợi suất yêu cầu của cổ phiếu không đổi",
 "Mức bù rủi ro của cổ phiếu tăng gấp đôi, lợi suất yêu cầu tăng chưa tới gấp đôi",
 "Rủi ro phi hệ thống tăng gấp đôi, lợi suất yêu cầu tăng chưa tới gấp đôi"]
# C2-022: key longest option
opt('C2-022',0,"Chỉ số giá cổ phiếu trên thị trường chứng khoán","Chỉ số giá cổ phiếu (như VN-Index)")
# C2-023: key listed 3 sectors vs 2 in distractors
opt('C2-023',2,"Hàng tiêu dùng thiết yếu, dược phẩm, điện nước","Hàng tiêu dùng thiết yếu và dược phẩm")
rep('C2-023','e',"Nhu cầu hàng thiết yếu, thuốc, điện nước ít co giãn","Nhu cầu hàng thiết yếu, thuốc (tương tự điện, nước) ít co giãn")
# C2-029: key longest option
opt('C2-029',1,"Nhà đầu tư kỳ vọng tăng trưởng lợi nhuận của A cao hơn hoặc rủi ro của A thấp hơn","Kỳ vọng tăng trưởng lợi nhuận của A cao hơn hoặc rủi ro của A thấp hơn")
# C2-056: "mua cổ phiếu" could be trading securities (operating CF under VAS 24)
opt('C2-056',1,"Tiền chi mua cổ phiếu của doanh nghiệp khác","Tiền chi góp vốn đầu tư vào doanh nghiệp khác")
rep('C2-056','e',"Mua cổ phiếu doanh nghiệp khác, mua TSCĐ thuộc hoạt động đầu tư","Góp vốn đầu tư vào đơn vị khác, mua TSCĐ thuộc hoạt động đầu tư")
# C2-058: key longest option
opt('C2-058',1,"Ghi số âm, điều chỉnh giảm hàng tồn kho trong tài sản ngắn hạn","Ghi số âm, làm giảm khoản mục hàng tồn kho")
# C2-059: TT200 allows lump-sum recognition of multi-year prepaid rent under strict conditions -> rule out; key longest
rep('C2-059','q',"trong 3 năm (01/01/N – 31/12/N+2).","trong 3 năm (01/01/N – 31/12/N+2); hợp đồng cho phép bên thuê hủy ngang và nhận lại tiền thuê của thời gian chưa sử dụng.")
X['C2-059']['o']=["Ghi nhận doanh thu 360 triệu vì toàn bộ tiền thuê đã được thu trong năm N",
 "Ghi nhận doanh thu 120 triệu; 240 triệu còn lại là doanh thu chưa thực hiện",
 "Ghi nhận doanh thu 120 triệu; 240 triệu còn lại ghi tăng vốn chủ sở hữu",
 "Ghi nhận doanh thu 120 triệu; 240 triệu còn lại ghi giảm phải thu khách hàng"]
rep('C2-059','e',"là doanh thu chưa thực hiện, một khoản nợ phải trả.","là doanh thu chưa thực hiện, một khoản nợ phải trả. Do bên thuê được hủy ngang và nhận lại tiền, không đủ điều kiện ghi nhận một lần toàn bộ số tiền nhận trước.")
# C2-060: key far shorter than distractors
opt('C2-060',0,"Doanh thu thuần trừ giá vốn hàng bán","Doanh thu thuần về bán hàng và cung cấp dịch vụ trừ giá vốn hàng bán")
# C2-070: 30.000/(1.200 tỷ/65 triệu) = 1,625 -> rounds half-up to 1,63
opt('C2-070',0,"1,62 lần","1,63 lần")
rep('C2-070','e',"tính cả cổ phiếu quỹ (1,62)","tính cả cổ phiếu quỹ (1,625 ≈ 1,63)")
# C2-077: key (2 items, 39 chars) vs single-item distractors (12–19 chars)
opt('C2-077',2,"Vay ngân hàng và vốn góp của chủ sở hữu","Vay ngân hàng")
# C2-082: key longest option
opt('C2-082',1,"Chi phí khấu hao giảm làm lợi nhuận kế toán tăng, dòng tiền thực không được cải thiện","Khấu hao giảm, lợi nhuận kế toán tăng nhưng dòng tiền không được cải thiện")
# C2-090: key longest option
opt('C2-090',0,"Tài sản ngắn hạn của R tập trung lớn vào hàng tồn kho; thanh khoản yếu nếu tồn kho khó bán","Tài sản ngắn hạn của R chủ yếu là hàng tồn kho, thanh khoản thực tế yếu")

out=json.dumps(D,ensure_ascii=False,indent=1)
open(P,'w',encoding='utf-8').write(out+('\n' if raw.endswith('\n') else ''))
print('written')
