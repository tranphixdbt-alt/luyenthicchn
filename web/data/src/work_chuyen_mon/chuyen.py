"""Môn Pháp luật không có bài tập tính toán (người dùng xác nhận sau khi thi 11/2026):
câu Luật có đáp án là con số phải tính → chuyển sang môn có bài tập; câu tính ngày/mức phạt → viết lại thành câu hỏi thời hạn/mức phạt (vẫn là Luật).
Giữ nguyên mã câu để không mất tiến độ người học. Chạy: python3 -I chuyen.py"""
import json
from pathlib import Path
SRC = Path(__file__).resolve().parent.parent
CB_CTCK, CB_QUY = "Công ty chứng khoán", "Công ty quản lý quỹ và quỹ đầu tư chứng khoán"
MOVE = {
    "L1-026": ("BL", "Bảo lãnh phát hành chứng khoán"), "L2-052": ("BL", "Bảo lãnh phát hành chứng khoán"),
    "L2-003": ("BL", "Tài trợ vốn cho hoạt động của doanh nghiệp"), "L2-005": ("BL", "Tài trợ vốn cho hoạt động của doanh nghiệp"),
    "L2-013": ("BL", "Tài trợ vốn cho hoạt động của doanh nghiệp"), "L5-013": ("BL", "Chính sách cổ tức và mua lại cổ phiếu của doanh nghiệp"),
    "L5-025": ("BL", "Tái cấu trúc doanh nghiệp, sáp nhập và mua lại doanh nghiệp"), "L5-026": ("BL", "Tái cấu trúc doanh nghiệp, sáp nhập và mua lại doanh nghiệp"),
    "L2-020": ("CB", "Thị trường chứng khoán thứ cấp"),
    "L2-030": ("CB", CB_CTCK), "L2-050": ("CB", CB_CTCK), "L2-055": ("CB", CB_CTCK), "L2-061": ("CB", CB_CTCK), "L2-065": ("CB", CB_CTCK),
    "L1-080": ("CB", CB_QUY), "L2-080": ("CB", CB_QUY), "L4-005": ("CB", CB_QUY),
    "L3-030": ("CB", "Hệ thống đăng ký, lưu ký, bù trừ và thanh toán chứng khoán"),
    "L3-010": ("MG", "Giao dịch cổ phiếu trên thị trường chứng khoán"),
}
REWRITE = {
    "C8-005": dict(level=1,
        q="Theo Nghị định 155/2020/NĐ-CP, công ty đại chúng phải đăng ký cổ phiếu tại Tổng công ty lưu ký và bù trừ chứng khoán Việt Nam trong thời hạn nào?",
        o=["15 ngày kể từ ngày UBCKNN xác nhận hoàn tất đăng ký công ty đại chúng", "30 ngày kể từ ngày UBCKNN xác nhận hoàn tất đăng ký công ty đại chúng",
           "15 ngày kể từ ngày nộp hồ sơ đăng ký công ty đại chúng cho UBCKNN", "01 năm kể từ ngày trở thành công ty đại chúng"], a=0,
        e="Khoản 4 Điều 149 NĐ 155/2020 (NĐ 245/2025 chỉ bổ sung khoản 3a, 3b, 4a, không sửa khoản 4): 15 ngày kể từ ngày UBCKNN xác nhận hoàn tất việc đăng ký công ty đại chúng. 30 ngày là thời hạn đăng ký giao dịch cổ phiếu trên hệ thống giao dịch chứng khoán chưa niêm yết (điểm d khoản 1 Điều 34 Luật Chứng khoán); 01 năm không đăng ký tại VSDC là căn cứ hủy tư cách công ty đại chúng (Điều 38 Luật Chứng khoán)."),
    "L5-002": dict(level=1,
        q="Theo Nghị định 155/2020/NĐ-CP, tổ chức phát hành phải hoàn thành đợt chào bán cổ phiếu riêng lẻ trong thời hạn nào kể từ ngày UBCKNN có văn bản chấp thuận?",
        o=["90 ngày", "60 ngày", "90 ngày, được gia hạn thêm tối đa 30 ngày", "30 ngày"], a=0,
        e="Khoản 3 Điều 48 NĐ 155/2020 (NĐ 245/2025 không sửa điều này): hoàn thành đợt chào bán cổ phiếu riêng lẻ trong 90 ngày kể từ ngày UBCKNN có văn bản chấp thuận; Điều 48 không có cơ chế gia hạn 30 ngày như chào bán ra công chúng (khoản 4 Điều 26 Luật Chứng khoán). Trong 10 ngày kể từ ngày kết thúc đợt chào bán, tổ chức phát hành gửi báo cáo kết quả kèm xác nhận của ngân hàng nơi mở tài khoản phong tỏa."),
    "C8-003": dict(level=1,
        q="Theo Thông tư 96/2020/TT-BTC, công ty đại chúng phải công bố thông tin về ngày đăng ký cuối cùng dự kiến để cổ đông hiện hữu tham dự họp Đại hội đồng cổ đông tối thiểu bao nhiêu ngày trước ngày đăng ký cuối cùng dự kiến?",
        o=["20 ngày", "10 ngày", "21 ngày", "15 ngày"], a=0,
        e="Điểm b khoản 4 Điều 11 TT 96/2020: tối thiểu 20 ngày trước ngày đăng ký cuối cùng dự kiến khi thực hiện quyền tham dự họp ĐHĐCĐ. Mốc 10 ngày áp dụng cho các quyền khác như nhận cổ tức (điểm a); 21 ngày là thời hạn đăng tài liệu họp ĐHĐCĐ thường niên trước ngày khai mạc, không tính theo ngày đăng ký cuối cùng."),
    "L2-073": dict(level=1,
        q="Theo Thông tư 96/2020/TT-BTC, tổ chức niêm yết cổ phiếu là công ty mẹ của tổ chức khác, không thực hiện soát xét báo cáo tài chính quý, phải công bố báo cáo tài chính quý trong thời hạn nào?",
        o=["30 ngày kể từ ngày kết thúc quý", "20 ngày kể từ ngày kết thúc quý", "45 ngày kể từ ngày kết thúc quý", "05 ngày kể từ ngày ký báo cáo, tối đa 45 ngày"], a=0,
        e="Điểm c khoản 3 Điều 14 TT 96/2020: báo cáo tài chính quý công bố trong 20 ngày kể từ ngày kết thúc quý; công ty mẹ hoặc đơn vị kế toán cấp trên có đơn vị kế toán trực thuộc tổ chức bộ máy kế toán riêng được 30 ngày. Mốc 05 ngày kể từ ngày tổ chức kiểm toán ký báo cáo soát xét, tối đa 45 ngày kể từ ngày kết thúc quý, chỉ áp dụng cho báo cáo tài chính quý đã được soát xét."),
    "L1-094": dict(level=2,
        q="Theo Điều 132 Luật Chứng khoán, cá nhân thực hiện hành vi thao túng thị trường chứng khoán có khoản thu trái pháp luật (mức phạt tính theo khoản thu cao hơn 1,5 tỷ đồng) thì mức phạt tiền tối đa là:",
        o=["05 lần khoản thu trái pháp luật", "10 lần khoản thu trái pháp luật", "02 lần khoản thu trái pháp luật", "1,5 tỷ đồng"], a=0,
        e="Khoản 3 Điều 132: với hành vi tại khoản 2, 3 Điều 12 (sử dụng thông tin nội bộ, thao túng) mức phạt tối đa là 10 lần khoản thu trái pháp luật; không có khoản thu hoặc mức tính theo khoản thu thấp hơn mức tại khoản 4 (03 tỷ đồng) thì áp dụng 03 tỷ đồng. Khoản 5: các mức này áp dụng cho tổ chức, cá nhân tối đa bằng một phần hai, tức 05 lần khoản thu trái pháp luật (hoặc 1,5 tỷ đồng). 10 lần là mức của tổ chức."),
}
moved, rewritten = [], []
for f in sorted(SRC.glob("*.json")):
    if f.name in ("so_lieu.json", "thay_doi.json"): continue
    qs = json.loads(f.read_text(encoding="utf-8")); changed = False
    for x in qs:
        if x["id"] in MOVE:
            x["subject"], x["topic"] = MOVE[x["id"]]; x["part"] = "CM"; moved.append(x["id"]); changed = True
        if x["id"] in REWRITE:
            x.update(REWRITE[x["id"]]); rewritten.append(x["id"]); changed = True
    if changed: f.write_text(json.dumps(qs, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
assert sorted(moved) == sorted(MOVE) and sorted(rewritten) == sorted(REWRITE), (set(MOVE) - set(moved), set(REWRITE) - set(rewritten))
print("chuyển môn:", len(moved), "· viết lại:", len(rewritten))
