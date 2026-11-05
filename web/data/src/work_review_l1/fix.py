# Apply second-pass review fixes to luat_1.json and thay_doi.json in place.
# Usage: python3 -I fix.py   (idempotent: each edit asserts the old value or skips if already applied)
import json, pathlib

SRC = pathlib.Path(__file__).resolve().parent.parent
LUAT, TD = SRC / "luat_1.json", SRC / "thay_doi.json"


def load(p):
    return json.loads(p.read_text(encoding="utf-8"))


def save(p, d):
    p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


data = load(LUAT)
q = {x["id"]: x for x in data}


def setf(qid, field, new, old_contains=None):
    it = q[qid]
    if it[field] == new:
        return
    if old_contains is not None:
        cur = json.dumps(it[field], ensure_ascii=False)
        assert old_contains in cur, (qid, field, cur[:120])
    it[field] = new


# L1-007: key was the only "Trên …" option (cue); make the trên/từ threshold the real test
setf("L1-007", "o", ["Trên 50 tỷ đồng", "Từ 30 tỷ đồng trở lên", "Từ 100 tỷ đồng trở lên", "Trên 100 tỷ đồng"], "Từ 50 tỷ")
setf("L1-007", "a", 3)
setf("L1-007", "e", "Điểm b khoản 1 Điều 11: công ty có vốn điều lệ đã góp đạt trên 100 tỷ đồng hoặc tổ chức niêm yết, tổ chức đăng ký giao dịch là nhà đầu tư chứng khoán chuyên nghiệp. Ngưỡng là 'trên 100 tỷ đồng' (công ty có đúng 100 tỷ đồng chưa đạt), không phải 'từ 100 tỷ đồng trở lên'. Mốc 30 tỷ đồng là điều kiện vốn của công ty đại chúng/chào bán ra công chúng.", "Mốc 30")

# L1-010: bonds offered before 01/01/2026 stay under the old regime (Art 11.1 Law 56) -> pin the offering to 2026
setf("L1-010", "q", "Tháng 10/2026, bà M (nhà đầu tư chứng khoán chuyên nghiệp là cá nhân) muốn mua trái phiếu của một đợt chào bán trái phiếu doanh nghiệp riêng lẻ công bố thông tin trước đợt chào bán vào tháng 9/2026. Theo Luật Chứng khoán hiện hành, bà M được mua loại trái phiếu nào sau đây?", "phát hành riêng lẻ")
setf("L1-010", "e", "Từ 01/01/2026, khoản 1b Điều 11 (bổ sung bởi Luật 56/2024) chỉ cho phép nhà đầu tư chuyên nghiệp là cá nhân mua, giao dịch, chuyển nhượng trái phiếu doanh nghiệp riêng lẻ khi trái phiếu có xếp hạng tín nhiệm VÀ có tài sản bảo đảm hoặc có bảo lãnh thanh toán của tổ chức tín dụng. Nhà đầu tư chuyên nghiệp là tổ chức không bị giới hạn này (khoản 1a). Đợt chào bán ở đây công bố thông tin năm 2026 nên không thuộc trường hợp chuyển tiếp tại khoản 1 Điều 11 Luật 56/2024.", "khoản 1a).")

# L1-015: key (32 chars) much shorter than distractors
setf("L1-015", "o", ["Sử dụng thông tin nội bộ để giao dịch chứng khoán", "Hành vi hợp pháp vì thuộc quyền tự do bày tỏ ý kiến", "Chỉ vi phạm nghĩa vụ công bố thông tin của cổ đông lớn", "Thao túng thị trường chứng khoán, bị nghiêm cấm"], "Thao túng thị trường chứng khoán\"")

# L1-034: Art 31b applies to private offerings registered with the SSC; say so
setf("L1-034", "q", "Công ty đại chúng M đã kết thúc đợt chào bán trái phiếu riêng lẻ đã đăng ký với UBCKNN. Sau đó UBCKNN phát hiện hồ sơ có thông tin sai lệch gây thiệt hại cho nhà đầu tư và quyết định hủy bỏ đợt chào bán. Nghĩa vụ của M là:", "trái phiếu riêng lẻ. Sau")

# L1-036: stem did not say what N must "đáp ứng"
setf("L1-036", "q", "Công ty cổ phần N có vốn điều lệ đã góp 45 tỷ đồng; 300 cổ đông nhỏ (không phải cổ đông lớn) nắm 40% cổ phiếu có quyền biểu quyết. Báo cáo tài chính năm 2025 được kiểm toán cho thấy vốn chủ sở hữu của N chỉ còn 25 tỷ đồng do lỗ lũy kế. Tại tháng 11/2026, nhận định nào đúng về việc N có đáp ứng điều kiện công ty đại chúng theo điểm a khoản 1 Điều 32 Luật Chứng khoán?", "nhận định nào đúng?")
setf("L1-036", "e", "Tiêu chí vốn chủ sở hữu từ 30 tỷ đồng tại điểm a khoản 1 Điều 32 (Luật 56/2024) có hiệu lực từ 01/01/2026. N có VCSH 25 tỷ nên không đáp ứng; nếu N đang là công ty đại chúng thì theo khoản 2 Điều 38 phải báo cáo UBCKNN trong 15 ngày và sau 01 năm vẫn không đáp ứng thì bị xem xét hủy tư cách công ty đại chúng. Cơ cấu cổ đông chỉ yêu cầu tối thiểu 10%.", "theo Điều 38")

# L1-042: option A did not fit the stem "thì phải:"
setf("L1-042", "o", ["Buộc các cổ đông còn lại bán cổ phiếu theo giá do Hội đồng quản trị quyết định", "Làm thủ tục hủy tư cách công ty đại chúng trong 30 ngày kể từ ngày kết thúc chào mua", "Mua tiếp cổ phiếu của cổ đông còn lại trong 90 ngày theo giá thị trường tại thời điểm mua", "Mua tiếp cổ phiếu của cổ đông còn lại trong 30 ngày, giá và cách thanh toán như đợt chào mua"], "Được quyền buộc")

# L1-051: key (29 chars) much shorter than distractors
setf("L1-051", "o", ["Thành viên giao dịch thông thường như công ty chứng khoán", "Thành viên giao dịch đặc biệt của Sở giao dịch chứng khoán", "Thành viên lưu ký của Sở giao dịch chứng khoán", "Thành viên bù trừ của Sở giao dịch chứng khoán"], "Thành viên giao dịch như")

# L1-054: key (25 chars) much shorter than distractors
setf("L1-054", "o", ["Cho mọi nhà đầu tư mở tài khoản tại V", "Cho các công ty chứng khoán chưa là thành viên bù trừ", "Chỉ cho chính ngân hàng V, không cho khách hàng", "Cho khách hàng là tổ chức, không cho khách hàng cá nhân"], "Chỉ cho chính ngân hàng V\"")

# L1-064: option D much shorter than the three parallel options
setf("L1-064", "o", ["Thông qua phương án khắc phục, báo cáo UBCKNN trong 30 ngày; thời gian khắc phục tối đa 06 tháng", "Thông qua phương án khắc phục, báo cáo UBCKNN trong 15 ngày; thời gian khắc phục tối đa 03 tháng", "Thông qua phương án khắc phục, báo cáo UBCKNN trong 30 ngày; thời gian khắc phục tối đa 12 tháng", "Không phải lập phương án khắc phục; UBCKNN thu hồi ngay Giấy phép thành lập và hoạt động"], "Không cần khắc phục")

# L1-066 / L1-069: basis names the exact amending point
setf("L1-066", "basis", "Điểm c khoản 3, khoản 4 Điều 97 Luật Chứng khoán 2019; điểm a khoản 1 Điều 214 NĐ 155/2020/NĐ-CP (sửa đổi bởi khoản 74 Điều 1 NĐ 245/2025/NĐ-CP)", "Điều 214")
setf("L1-069", "basis", "Khoản 5a Điều 213 NĐ 155/2020/NĐ-CP (bổ sung bởi điểm d khoản 73 Điều 1 NĐ 245/2025/NĐ-CP); Thông báo kế hoạch thi sát hạch 2026 của UBCKNN", "bổ sung bởi khoản 73")

# L1-076: key (22 chars) far shorter than distractors -> use another listed equivalent of similar length
setf("L1-076", "o", ["Pháp luật về chứng khoán và thị trường chứng khoán", "Môi giới chứng khoán và tư vấn đầu tư chứng khoán", "Chứng khoán phái sinh và thị trường chứng khoán phái sinh", "Tư vấn tài chính và bảo lãnh phát hành chứng khoán"], "Quản lý quỹ và tài sản")
setf("L1-076", "e", "Khoản 1 Điều 4 TT 135/2025: CIIA hoặc CFA bậc II trở lên tương đương các chứng chỉ: Những vấn đề cơ bản về CK và TTCK; Phân tích và đầu tư CK; Phân tích BCTC doanh nghiệp; Quản lý quỹ và tài sản; Chứng khoán phái sinh và TTCK phái sinh. Không bao gồm Pháp luật, Môi giới – tư vấn, Tư vấn tài chính – bảo lãnh.", "Khoản 1 Điều 4")
setf("L1-076", "quote", "Chartered Financial Analyst (CFA) level II exam or higher is equivalent to certificates in: Basic issues of securities and the securities market, Securities analysis and investment, Corporate financial statement analysis, Fund and asset management, Derivatives and the derivatives market", "Fund and asset management\"")

# L1-083 / L1-084: key noticeably shorter than distractors
setf("L1-083", "o", ["Quỹ tiếp tục hoạt động vì chỉ giải thể khi NAV dưới 05 tỷ đồng", "Quỹ tự động chuyển đổi thành quỹ thành viên do cùng công ty quản lý", "Phải giải thể; triệu tập Đại hội nhà đầu tư trong 30 ngày kể từ ngày phát sinh", "Phải giải thể; triệu tập Đại hội nhà đầu tư 03 tháng trước ngày giải thể"], "trong 30 ngày\"")
setf("L1-084", "o", ["Lợi nhuận của quỹ năm liền trước năm đề nghị tăng vốn là số dương", "Giá trị tài sản ròng của quỹ tại kỳ định giá gần nhất tối thiểu 100 tỷ đồng", "Công ty quản lý quỹ không bị xử phạt VPHC về chứng khoán trong 02 năm gần nhất", "Phương án phát hành thêm chứng chỉ quỹ đóng được Đại hội nhà đầu tư thông qua"], "Giá trị tài sản ròng của quỹ tối thiểu 100 tỷ đồng")

# L1-085: key (100 chars) was the longest option
setf("L1-085", "o", ["Vốn góp tối thiểu 10 tỷ đồng, có từ 02 đến 99 thành viên là nhà đầu tư bất kỳ", "Vốn góp tối thiểu 50 tỷ đồng, từ 02 đến 99 thành viên, chỉ gồm NĐT chuyên nghiệp", "Vốn góp tối thiểu 50 tỷ đồng, có tối đa 100 thành viên, do 02 công ty quản lý quỹ cùng quản lý", "Vốn góp tối thiểu 50 tỷ đồng, tài sản lưu ký tại chính công ty quản lý quỹ"], "đều là nhà đầu tư")

# L1-087: "cổ phiếu quỹ" is not the statutory wording (Art 127.3a: "mua lại cổ phiếu của chính mình")
setf("L1-087", "o", ["Cổ đông lớn bán cổ phiếu qua phương thức giao dịch thỏa thuận trên sàn", "Cổ đông lớn là tổ chức nước ngoài mua thêm cổ phiếu qua hệ thống giao dịch", "Cổ đông lớn mua thêm cổ phiếu qua phương thức khớp lệnh tập trung trên sàn", "Thay đổi do công ty đại chúng mua lại cổ phiếu của chính mình hoặc phát hành thêm"], "cổ phiếu quỹ")

# L1-091: option A (30 chars) much shorter than the others
setf("L1-091", "o", ["Chỉ BCTC năm đã kiểm toán; BCTC bán niên, BCTC quý không bắt buộc", "BCTC năm và BCTC 06 tháng đều đã kiểm toán, không yêu cầu BCTC quý", "BCTC năm đã kiểm toán, BCTC 06 tháng đã được soát xét và BCTC quý", "BCTC quý đã được kiểm toán và BCTC năm đã được soát xét"], "Chỉ BCTC năm đã được kiểm toán\"")

# L1-093: garbled sentence in explanation
setf("L1-093", "e", "Khoản 4 Điều 132: mức phạt tiền tối đa đối với các hành vi vi phạm khác là 03 tỷ đồng. Theo khoản 5, mức này áp dụng cho tổ chức; cá nhân thực hiện cùng hành vi thì mức phạt tối đa bằng một phần hai (1,5 tỷ đồng).", "mức này áp dụng cho tổ chức, cá nhân")

save(LUAT, data)

# ---- thay_doi.json ----
td = load(TD)
T = {x["title"]: x for x in td}


def tset(title_start, field, new, old_contains):
    it = next(x for t, x in T.items() if t.startswith(title_start))
    if it[field] == new:
        return
    assert old_contains in it[field], (title_start, field, it[field][:120])
    it[field] = new


tset("Công ty đại chúng: bổ sung", "effective", "01/01/2026", "(tiêu chí")
tset("Công ty đại chúng: bổ sung", "what", "Trước đây công ty cổ phần là công ty đại chúng khi có vốn điều lệ đã góp từ 30 tỷ đồng và tối thiểu 10% cổ phiếu có quyền biểu quyết do ít nhất 100 nhà đầu tư không phải cổ đông lớn nắm giữ; nay phải có thêm vốn chủ sở hữu từ 30 tỷ đồng trở lên (tiêu chí này áp dụng từ 01/01/2026). Công ty đại chúng niêm yết/đăng ký giao dịch trước 01/01/2021 mà đến 01/01/2026 không đáp ứng thì bị hủy tư cách công ty đại chúng, trừ khi ĐHĐCĐ đã quyết định hủy tư cách trước ngày này.", "thì bị hủy tư cách công ty đại chúng.")
tset("Nhà đầu tư chứng khoán chuyên nghiệp", "effective", "01/01/2025", "(NĐT")
tset("Chào bán thêm để thực hiện dự án", "effective", "01/01/2025", "(Luật)")
tset("Chào bán thêm để thực hiện dự án", "what", "Trước đây đợt chào bán thêm cổ phiếu ra công chúng để thực hiện dự án phải bán được tối thiểu 70% số cổ phiếu dự kiến chào bán trong mọi trường hợp; nay loại trừ trường hợp chào bán cho cổ đông hiện hữu theo tỷ lệ sở hữu. NĐ 245/2025 (hiệu lực 11/09/2025) sửa tương ứng điểm b khoản 2 Điều 12 NĐ 155/2020.", "NĐ 245/2025 sửa")
tset("Thi sát hạch và cấp CCHN", "what", "Trước đây thi sát hạch và cấp CCHN là hai thủ tục, hồ sơ cấp CCHN phải kèm Phiếu lý lịch tư pháp; nay hồ sơ cấp CCHN đồng thời là hồ sơ dự thi, Phiếu lý lịch tư pháp được nộp trong 20 ngày kể từ ngày công bố kết quả, bài thi gồm 02 phần (pháp luật, chuyên môn), kết quả công bố trong 15 ngày kể từ ngày kết thúc đợt thi và quyết định cấp CCHN (giấy hoặc điện tử) trong 30 ngày kể từ ngày công bố kết quả. Thí sinh chưa đạt một phần được thi lại phần đó trong 01 năm (hoặc tại kỳ thi gần nhất liền sau) và khi đăng ký thi lại không phải nộp lại bằng đại học, chứng chỉ chuyên môn; quá hạn phải thi lại cả hai phần.", "quá hạn phải thi lại cả hai phần và")
tset("Trái phiếu chào bán ra công chúng", "effective", "11/09/2025", "(Luật)")
tset("Trái phiếu chào bán ra công chúng", "what", "Luật 56/2024 (hiệu lực 01/01/2025) yêu cầu doanh nghiệp chào bán trái phiếu ra công chúng đáp ứng quy định của Chính phủ về đại diện người sở hữu trái phiếu, hệ số nợ, giá trị phát hành trên VCSH và xếp hạng tín nhiệm. NĐ 245/2025 cụ thể hóa: tổ chức phát hành hoặc trái phiếu phải được xếp hạng tín nhiệm (trừ trái phiếu của TCTD hoặc được bảo lãnh thanh toán toàn bộ gốc, lãi), phải có đại diện người sở hữu trái phiếu và nợ phải trả (kể cả trái phiếu dự kiến phát hành) không quá 05 lần vốn chủ sở hữu, trừ DNNN, DN phát hành cho dự án bất động sản, TCTD, DN bảo hiểm, CTCK, CTQLQ.", "Luật 56/2024 yêu cầu")
save(TD, td)
print("fixes applied")
