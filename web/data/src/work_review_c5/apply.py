# Apply second-pass fixes to cm_5.json in place.
import json, sys
path = sys.argv[1]
d = json.load(open(path, encoding='utf-8'))
Q = {q['id']: q for q in d}

def reorder(qid, new_opts):
    q = Q[qid]; key = q['o'][q['a']]
    assert sorted(new_opts) == sorted(q['o']), qid
    q['o'] = new_opts; q['a'] = new_opts.index(key)

def setopts(qid, opts, key):
    Q[qid]['o'] = opts; Q[qid]['a'] = opts.index(key)

# --- reorder only (key position balance) ---
reorder('C5-001', ["MOK (Match or Kill)", "MAK (Match and Kill)", "ATC (At the Close)", "LO (Limit Order)"])
o = Q['C5-012']['o']; reorder('C5-012', [o[2], o[0], o[1], o[3]])
o = Q['C5-013']['o']; reorder('C5-013', [o[0], o[3], o[1], o[2]])
reorder('C5-028', ["YTM > CY > c", "c > CY > YTM", "CY > c > YTM", "c = CY = YTM"])

# --- C5-005: market order sweeps several levels ---
q = Q['C5-005']
q['o'][3] = "Không ghi giá cụ thể; lệnh mua khớp lần lượt từ giá bán thấp nhất, lệnh bán từ giá mua cao nhất"

# --- C5-006: stem assumption gave the answer away ---
q = Q['C5-006']
q['q'] = q['q'].replace("Giả định quy chế: trong phiên khớp lệnh liên tục, nhà đầu tư được hủy phần khối lượng chưa khớp của lệnh LO.",
                        "Giả định quy chế cho phép hủy lệnh LO trong phiên khớp lệnh liên tục.")
assert "cho phép hủy lệnh LO" in q['q']

# --- C5-014: state the reference-price adjustment as data ---
q = Q['C5-014']
q['q'] = q['q'].replace("Giả định: biên độ", "Giả định: giá tham chiếu ngày giao dịch không hưởng quyền được điều chỉnh theo cổ tức bằng tiền; biên độ")
assert "điều chỉnh theo cổ tức" in q['q']

# --- C5-015 / C5-016: state reference price and tie-break ---
q = Q['C5-015']
q['q'] = q['q'].replace("Cổ phiếu V, bước giá 100 đồng.", "Cổ phiếu V có giá tham chiếu 60.000 đồng, bước giá 100 đồng.")
q['q'] = q['q'].replace("giá mở cửa là mức giá đạt khối lượng khớp lớn nhất;",
                        "giá mở cửa là mức giá đạt khối lượng khớp lớn nhất (nếu nhiều mức giá cùng đạt thì chọn mức gần giá tham chiếu nhất);")
assert "60.000 đồng, bước" in q['q'] and "gần giá tham chiếu" in q['q']
q = Q['C5-016']
q['q'] = q['q'].replace("Sổ lệnh phiên khớp lệnh định kỳ đóng cửa của cổ phiếu P (đơn vị: cổ phiếu)",
                        "Cổ phiếu P có giá tham chiếu 41.000 đồng. Sổ lệnh phiên khớp lệnh định kỳ đóng cửa (đơn vị: cổ phiếu)")
q['q'] = q['q'].replace("Giả định giá đóng cửa là mức giá đạt khối lượng khớp lớn nhất;",
                        "Giả định giá đóng cửa là mức giá đạt khối lượng khớp lớn nhất (nếu nhiều mức giá cùng đạt thì chọn mức gần giá tham chiếu nhất);")
assert "41.000 đồng. Sổ" in q['q'] and "gần giá tham chiếu" in q['q']

# --- C5-019: two distractors were not board lots; explanation mislabeled 200.049.625 as "bỏ qua phí" ---
q = Q['C5-019']
q['q'] = ("Tài khoản của khách hàng có 200.000.000 đồng tiền mặt (không sử dụng giao dịch ký quỹ). Khách hàng muốn dùng tối đa số tiền này "
          "để mua cổ phiếu S giá 39.950 đồng: trước hết đặt lệnh lô chẵn với khối lượng lớn nhất có thể, số tiền còn lại đặt thêm một lệnh lô lẻ "
          "cùng mức giá. Giả định: lô chẵn là bội số của 100 cổ phiếu, lô lẻ từ 01 đến 99 cổ phiếu; phí môi giới 0,15% giá trị giao dịch, thu khi mua, "
          "áp dụng cho cả hai lệnh; cả hai lệnh đều được khớp hết. Tổng số cổ phiếu tối đa khách hàng mua được là:")
setopts('C5-019', ["4.900 cổ phiếu", "4.998 cổ phiếu", "5.000 cổ phiếu", "5.006 cổ phiếu"], "4.998 cổ phiếu")
q['e'] = ("Chi phí mua 1 cổ phiếu = 39.950 × 1,0015 = 40.009,925 đồng. Lô chẵn: 200.000.000 / 40.009,925 ≈ 4.998,8 → 4.900 cổ phiếu, hết 196.048.632,5 đồng; "
          "còn 3.951.367,5 đồng → lô lẻ 3.951.367,5 / 40.009,925 ≈ 98,8 → 98 cổ phiếu. Tổng 4.998 cổ phiếu (hết 199.969.605 đồng; thêm 1 cổ phiếu sẽ cần "
          "200.009.615 đồng, vượt số dư). 4.900 là quên đặt lệnh lô lẻ; 5.000 và 5.006 là bỏ qua phí (200.000.000 / 39.950 ≈ 5.006,3), trong khi mua 5.000 cổ phiếu "
          "thực tế cần 199.750.000 + 299.625 phí = 200.049.625 đồng.")
q['basis'] = "Sức mua = Tiền mặt / [Giá × (1 + tỷ lệ phí)], tách phần lô chẵn (bội số 100) và lô lẻ (dữ kiện nêu trong đề)"

# --- C5-020: distractor 24.120 was not a valid tick; new numbers give four valid-tick prices ---
q = Q['C5-020']
q['q'] = ("Nhà đầu tư mua cổ phiếu giá 31.200 đồng. Phí môi giới 0,15% giá trị giao dịch mỗi chiều; thuế thu nhập cá nhân 0,1% trên giá trị bán "
          "(giả định theo đề); bước giá 50 đồng. Giá bán thấp nhất (theo bước giá) để nhà đầu tư không bị lỗ là:")
setopts('C5-020', ["31.250 đồng", "31.300 đồng", "31.350 đồng", "31.400 đồng"], "31.350 đồng")
q['e'] = ("Điều kiện hòa vốn: P × (1 − 0,15% − 0,1%) ≥ 31.200 × (1 + 0,15%) = 31.246,8 → P ≥ 31.246,8 / 0,9975 ≈ 31.325,11 đồng → làm tròn lên theo bước giá 50 "
          "= 31.350 đồng (kiểm tra: 31.300 × 0,9975 = 31.221,75 < 31.246,8 nên vẫn lỗ). 31.250 là chỉ tính phí mua; 31.300 là bỏ qua thuế "
          "(31.246,8 / 0,9985 ≈ 31.293,7); 31.400 là tính nhầm thuế 0,1% cả ở chiều mua (31.200 × 1,0025 / 0,9975 ≈ 31.356,4).")

# --- C5-022: key rank variation ---
q = Q['C5-022']
setopts('C5-022', ["33.462 đồng", "34.615 đồng", "35.769 đồng", "37.500 đồng"], "35.769 đồng")
q['e'] = q['e'].replace("thiếu tỷ lệ quyền mua ở mẫu số (46.500 / 1,2 = 38.750)", "bỏ qua tiền nộp khi thực hiện quyền mua (45.000 / 1,3 ≈ 34.615)")
assert "34.615" in q['e']

# --- C5-024: key rank variation, day-count distractor ---
q = Q['C5-024']
setopts('C5-024', ["4,00%", "8,00%", "13,00%", "13,04%"], "13,04%")
q['e'] = ("Lãi vốn = 400.000.000 × 8% = 32.000.000 đồng; lãi vay = 200.000.000 × 12% × 90/365 = 5.917.808 đồng; lợi nhuận ròng = 26.082.192 đồng "
          "→ 26.082.192 / 200.000.000 = 13,04%. 13,00% là tính lãi vay theo 90/360 (6.000.000 đồng) thay vì số ngày thực tế/365 như đề nêu; "
          "8,00% là tỷ suất khi không dùng đòn bẩy; 4,00% là trừ lãi vay của cả năm (24.000.000 đồng). Nếu bỏ qua lãi vay sẽ được 16%.")

# --- C5-035: key rank variation (replace "cộng thay vì trừ" distractor) ---
q = Q['C5-035']
setopts('C5-035', ["100.606 đồng", "100.628 đồng", "100.645 đồng", "100.650 đồng"], "100.650 đồng")
q['e'] = ("Theo 30/360: số ngày = 4 tháng × 30 + (21 − 15) = 126 ngày; lãi cộng dồn = 100.000 × 8% × 126/360 = 2.800 đồng; giá sạch = 103.450 − 2.800 "
          "= 100.650 đồng. Lỗi thường gặp: dùng số ngày thực tế 128 ngày chia 365 (lãi 2.805,48 → 100.645) hoặc chia 360 (lãi 2.844,44 → 100.606); "
          "đếm cả ngày đầu và ngày cuối thành 127 ngày (lãi 2.822,22 → 100.628).")

# --- C5-038: settlement on coupon date stated; key rank variation ---
q = Q['C5-038']
q['q'] = q['q'].replace("còn 4 năm đến ngày đáo hạn", "vừa trả lãi và còn đúng 4 năm đến ngày đáo hạn")
assert "vừa trả lãi" in q['q']
setopts('C5-038', ["7,45%", "8,50%", "8,76%", "9,04%"], "8,76%")
q['e'] = q['e'].replace("13,40% là cộng toàn bộ chênh lệch 6.000 đồng vào thu nhập một năm.",
                        "8,50% là chia cho mệnh giá 100.000 thay vì giá bình quân 97.000.")
assert "8,50%" in q['e']

# --- C5-039: settlement date explicit ---
q = Q['C5-039']
q['q'] = q['q'].replace("kỳ trả lãi gần nhất vừa kết thúc.", "ngày thanh toán trùng ngày vừa trả lãi (không có lãi cộng dồn).")
assert "không có lãi cộng dồn" in q['q']

# --- C5-040: remove "xấp xỉ" (approximation methods would also qualify), settlement stated, key rank ---
q = Q['C5-040']
q['q'] = ("Trái phiếu mệnh giá 100.000 đồng, lãi suất coupon 7%/năm trả hằng năm, vừa trả lãi và còn đúng 3 năm đến ngày đáo hạn, đang giao dịch "
          "bằng mệnh giá (YTM = 7%). Nếu lợi suất đáo hạn tăng lên 8%/năm ngay sau đó, mức thay đổi giá trái phiếu tính theo giá trị hiện tại "
          "của dòng tiền (làm tròn 2 chữ số thập phân) là:")
setopts('C5-040', ["−3,00%", "−2,81%", "−2,67%", "−2,58%"], "−2,58%")
q['e'] = ("Giá mới = 7.000/1,08 + 7.000/1,08² + 107.000/1,08³ ≈ 97.422,90 đồng → thay đổi = (97.422,90 − 100.000)/100.000 ≈ −2,58%. "
          "−2,67% là lấy mức tăng giá khi lợi suất giảm xuống 6% (giá 102.673 đồng) rồi đổi dấu, bỏ qua tính bất đối xứng của giá; "
          "−2,81% là ước lượng bằng duration Macaulay (≈ 2,81 năm) × 1%, vừa không điều chỉnh duration vừa bỏ qua độ lồi; "
          "−3,00% là nhân kỳ hạn còn lại với mức tăng lợi suất.")

json.dump(d, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('ok')
