# Soát chéo cm_14.json (C14-001 → C14-027), 08/11/2026

Người soát: agent soát chéo thứ hai (vai trò giảng viên thị trường trái phiếu và pháp luật chứng khoán, CFA). Mốc pháp lý: tháng 11/2026.
Công cụ: `work_review_c14/calc.py` (tính lại bằng Python, có assert), `check_quotes.py` (kiểm trích dẫn của cả câu CM, vì `kiem_tra.py` chỉ kiểm câu LUAT), `dup.py` (dò trùng với `questions.json`), `apply_review.py` (áp dụng sửa; chạy lại từ `cm_14_before_review.json`). `python3 -I web/tools/kiem_tra.py` → OK, 905 câu (không còn lỗi chặn; cảnh báo duy nhất C2-085 ~ C2-086 không thuộc C14).

## Kiểm văn bản hiện hành

- NĐ 95/2018: các điều câu hỏi dựa vào (3, 15, 17, 18, 20, 21, 22, 23, 26, 27) đã đối chiếu với NĐ 83/2023 (hiệu lực 15/01/2024) và NĐ 84/2026 (hiệu lực 25/3/2026). NĐ 84/2026 Điều 4 chỉ sửa khoản 2 Điều 21, khoản 1 Điều 30, khoản 7 Điều 36 và bãi bỏ Điều 39 NĐ 95. NĐ 83/2023 còn **bãi bỏ khoản 3 Điều 3 (định nghĩa đấu thầu đa giá)**; người viết bỏ sót, đã sửa C14-003.
- NĐ 84/2026 là bản quét: đã tải lại PDF gốc (datafiles.chinhphu.vn, 84-ndcp.signed.pdf), dựng ảnh trang 13–14 và đối chiếu: câu trích ở C14-009 khớp nguyên văn ảnh trang 13. Lời dẫn của NĐ 84 ghi Luật Quản lý nợ công đã sửa bởi Luật 141/2025/QH15; danh mục điều sửa của Luật 141 không đụng thẩm quyền về công trái xây dựng Tổ quốc (C14-008 giữ nguyên).
- TT 30/2019: vẫn còn hiệu lực tháng 11/2026; dự thảo thông tư thay thế (Thời báo Tài chính 22/8 và 08/10/2026) chưa ban hành. Nếu ban hành, soát lại C14-010 → C14-016, C14-026.
- NĐ 155/2020 Điều 97, 99: không bị NĐ 245/2025 sửa. NĐ 200/2026 (hiệu lực 05/6/2026) Điều 9, 20, 21, 30: khớp các câu C14-017 → C14-020.
- Không câu nào khẳng định giờ giao dịch, lô, T+n hay kỳ hạn repo của Sở như quy định hiện hành; ngày nghỉ (C14-018), tỷ lệ phòng ngừa rủi ro và giá (C14-006), cách phân bổ mức lãi suất cuối (C14-002) đều là giả định trong đề.

## Tính lại (calc.py)

| Câu | Kết quả | Ghi chú |
|---|---|---|
| C14-002 | Không cạnh tranh cắt còn 600 tỷ (30% × 2.000); cạnh tranh 1.400 tỷ: 300 + 500 + 400 + 200 ở 3,20%; mức 3,35% > trần 3,30% bị loại; đơn giá → 3,20%, 200 tỷ | Đúng. Nhiễu: không cắt 30% (3,15%; 400), bình quân gia quyền 3,1179% ≈ 3,12%, phân bổ đủ 600 |
| C14-006 | Đã đổi số liệu: 1.500.000 × 102.400 × 1,04 = 159.744.000.000 | Đáp án nay đứng thứ 3/4 theo giá trị (trước đây 4 câu tính đều có đáp án lớn nhất) |
| C14-014 | 200.000 × 100.000 × 4,2% = 840.000.000; lượt 2: 10/3/2027 + 30 ngày = 09/4/2027 (thứ Sáu); hạn hoàn lãi ngoài hệ thống: 5 ngày làm việc sau 25/3/2027 (thứ Năm) = 01/4/2027 | Đúng; 30/365 × 840 triệu = 69.041.096 (nhiễu). Giỗ Tổ 2027 rơi khoảng 16/4, không ảnh hưởng |
| C14-018 | 15 ngày làm việc sau 17/12/2026 (thứ Năm), nghỉ T7, CN, 01/01/2027 (thứ Sáu) → 08/01/2027 | Đúng. Đã thay nhiễu 24/12 bằng 15/01/2027 (cộng 05 ngày của Sở) để đáp án không phải ngày muộn nhất |

## Sửa từng câu

| Câu | Kết luận | Sửa |
|---|---|---|
| C14-001 | Đúng | Thêm điểm a khoản 1 Điều 27 NĐ 95 (nhà tạo lập thị trường là đối tượng duy nhất dự thầu) vào giải thích, căn cứ |
| C14-002 | Đúng | Giữ |
| C14-003 | Đúng đáp án, giải thích thiếu | Ghi rõ định nghĩa đấu thầu đa giá (khoản 3 Điều 3) đã bị bãi bỏ bởi khoản 1 Điều 2 NĐ 83/2023; cập nhật căn cứ |
| C14-004, 005 | Đúng | Giữ |
| C14-006 | Đúng nhưng đáp án là số lớn nhất | Đổi tỷ lệ giả định 3% → 4%, giá ghi rõ là giá dùng tính ký quỹ; phương án 153,6 / 156 / 159,744 / 160 tỷ (bỏ tỷ lệ, theo mệnh giá, đúng, chia 1 − 4%) |
| C14-007 | Đúng, đáp án ngắn nhất (lộ) | Viết lại 4 phương án cùng dạng, cùng độ dài |
| C14-008 | Đúng | Đưa đáp án lên vị trí 0; căn cứ ghi Điều 23 không bị sửa |
| C14-009 | Đúng, trích dẫn đã đối chiếu ảnh | Sửa giải thích: bản 2018 đã giao Thủ tướng phê duyệt; NĐ 84/2026 chỉ thay bộ phối hợp |
| C14-010 | Ý II trùng L3-017 (TVGD đặc biệt chỉ giao dịch cho chính mình) | Thay ý II bằng điều kiện CTCK làm TVGD thông thường (thành viên lưu ký, đủ 4 nghiệp vụ – điểm a, b khoản 1 Điều 6 TT 30; khoản 1 Điều 97 NĐ 155); đổi trích dẫn; đáp án vẫn “I và II” |
| C14-011 | Đúng | Giữ |
| C14-012 | Đúng | “Bộ Tài chính công nhận” → “lựa chọn” (đúng chữ khoản 1 Điều 3 NĐ 95) |
| C14-013 | Đúng | Giải thích không còn khẳng định cứng “không áp dụng khớp lệnh”; nêu khoản 1 Điều 16 TT 30 và quyền đổi phương thức khi UBCKNN chấp thuận |
| C14-014 | Đúng | Giải thích ghi hạn chót tính được 01/04/2027 |
| C14-015, 016, 017, 019 | Đúng | Giữ |
| C14-018 | Đúng | Đổi nhiễu (xem bảng tính) và giải thích |
| C14-020 | Đúng, đáp án dài nhất | Kéo dài hai phương án nhiễu cho cân |
| C14-021 | Đúng | Đáp án lên vị trí 0; Điều 98 Luật CK chỉ áp dụng nếu nhân viên là người hành nghề |
| C14-022 | Đúng | Giữ |
| C14-023 | Đúng đáp án; giải thích dẫn sai khoản 2 Điều 27 TT 121 (điều này nói bảo đảm nghĩa vụ cho bên thứ ba, còn tình huống là khoản vay của chính CTCK) | Bỏ dẫn khoản 2 Điều 27; căn cứ nay là khoản 4 Điều 4, điểm g khoản 4 Điều 13, điểm a khoản 1 Điều 18, khoản 1 Điều 26 TT 121, khoản 3 Điều 89 Luật CK |
| C14-024 | **Gần trùng C15-009** (cùng hỏi nhiệm vụ KSNB theo khoản 2 Điều 12; ý I, II của C14-024 chính là phương án nhiễu của C15-009) | Viết lại thành câu tình huống chọn trưởng bộ phận KSNB độc lập (khoản 4 Điều 12 TT 121: không là người có liên quan của Phó TGĐ…, không kiêm nhiệm, đủ hai chứng chỉ); trích dẫn điểm c khoản 4 Điều 12; căn cứ thêm điểm d khoản 46 Điều 4 Luật CK |
| C14-025 | Đúng | Giữ (L1-063 cùng khoản 1 Điều 91 nhưng hỏi vế cấm; C14-025 hỏi ngoại lệ thu nhập cố định) |
| C14-026 | Phương án 2 cũ (mua ở 101.500 = giá khách đặt) có thể cãi là “mức giá theo yêu cầu khách hàng” | Thay bằng nhiễu “tự doanh đặt trước nên được làm trước”; đề nêu tự doanh gửi yêu cầu sớm hơn vài phút; căn cứ thêm khoản 4 Điều 22 TT 121 |
| C14-027 | Đúng | Giữ |

Không xóa câu nào. Không sửa câu ngoài C14; không đụng cm_15.json.

## Trùng lặp

Đã dò `questions.json` (C1, C4, C5, C9, C10, C11, C13, C15, L1, L3, L5) theo các từ khóa đấu thầu, đơn giá, nhà tạo lập, repo, haircut, thỏa thuận điện tử, thành viên giao dịch, thừa kế, kiểm soát nội bộ, thu nhập cố định, ưu tiên lệnh. Ngoài C14-010 và C14-024 (đã sửa), không câu nào trùng ý chính; C14-019 gần L1-051 nhưng hỏi hệ thống TPDN riêng lẻ theo NĐ 200/2026.

## Điểm còn lưu ý

1. TT 30/2019 sắp bị thay: khi có thông tư mới, soát C14-010 → C14-016, C14-026.
2. C14-021, C14-022, C14-027 dựa trên cách phân nhóm và chuẩn mực trong bài giảng SRTC, không có văn bản để trích.
3. Danh mục điều sửa của Luật 141/2025 lấy từ bản tiếng Anh trên luatvietnam (chưa có file Công báo trong `van_ban_txt/`).
