# Review cm_4.json (second pass)

Đã rà cả 40 câu. Đối chiếu từng quote/căn cứ với VBHN 24/2025 (Luật CK), VBHN 09/2026 (TT 121 hợp nhất TT 68/2024, TT 08/2026), NĐ 155 Điều 216 và các sửa đổi của NĐ 245/2025 (chỉ sửa điểm d khoản 5 Điều 216), TT 135/2025 (không thay thế nghĩa vụ báo cáo tại Điều 216 NĐ 155). Không đáp án nào sai theo văn bản hiện hành. Tính lại C4-014, 022, 030: đúng. C4-002 (môi giới độc lập/"hai đô la") và C4-003 (tư vấn gợi ý/tư vấn ủy quyền) dùng cách phân loại có trong giáo trình TTCK tiếng Việt → giữ nguyên nội dung. Đã kiểm tra trùng với cm_1, luat_1, luat_2 (Jaccard + difflib; 3 cặp difflib 0,62–0,71 chỉ giống phần mở đầu câu kiểu "Theo Thông tư 121…", nội dung khác nhau). Script: work_review_c4/fix.py, validate.py.

## Thay câu
- C4-015: trùng gần với C1-052 (cùng dạng "phương pháp tìm khách hàng được gọi là", 3/4 phương án giống nhau) và trùng phương án với C4-016 → thay bằng câu về tiêu chí sàng lọc khách hàng tiềm năng (nhu cầu, khả năng tài chính, quyền quyết định); giữ a = 3.

## Sửa nội dung, căn cứ
- C4-012: "quỹ thị trường tiền tệ khớp kỳ hạn 12 tháng" sai về bản chất, vì quỹ tiền tệ không có kỳ hạn → đáp án sửa thành "tiền gửi kỳ hạn 12 tháng hoặc trái phiếu Chính phủ đáo hạn sau 1 năm"; sửa giải thích; bỏ số chuyên đề trong basis.
- C4-020: quote không có chữ "ngay", nên không phân biệt được đáp án với phương án "03 ngày làm việc" → đổi sang đoạn liền mạch "Công ty chứng khoán phải thông báo kết quả thực hiện lệnh … đại diện ngay" (VBHN 09).
- C4-021: điểm b khoản 4 Điều 13 TT 121 (chia sẻ lỗ "để lôi kéo khách hàng") không đúng tình huống bù lỗ sau giao dịch → căn cứ đổi sang điểm b khoản 6 Điều 4 TT 121 và khoản 1 Điều 91 Luật; sửa giải thích và basis.
- C4-025: phương án "bán ngay Y trước khi khuyến nghị để tránh xung đột" còn có thể bảo vệ được (đã loại bỏ lợi ích) → thay bằng "mua thêm Y trước khi gửi khuyến nghị"; rút gọn đáp án (dài hơn hẳn); sửa giải thích.
- C4-039: basis ghi khoản 4 Điều 98 Luật nhưng giải thích lại dẫn khoản 6 Điều 12, hai bên không khớp → basis và giải thích ghi đủ cả hai; phương án A nói "đồng ý bằng văn bản", chi tiết không có trong đề → sửa thành "đã đồng ý cho sử dụng".
- C4-017: giải thích viết "thực hiện lệnh theo thời gian nhận lệnh", không đúng câu chữ khoản 4, 5 Điều 16 → sửa thành "nhanh chóng, chính xác và ghi nhận đúng thời gian nhận lệnh"; bỏ số chuyên đề trong basis.
- C4-022: giải thích phương án nhiễu 57 chỉ ghi "≈ 56,5" → ghi rõ là làm tròn lên 57; bỏ số chuyên đề trong basis.

## Cân độ dài phương án (đáp án dài hơn hẳn, dễ đoán)
- C4-004: rút gọn đáp án A (96 → 84 ký tự).
- C4-026: rút gọn đáp án B.
- C4-027: rút gọn đáp án A.
- C4-028: rút gọn đáp án D.
- C4-040: rút gọn đáp án D.

## Basis câu kỹ năng
Basis ghi số "Chuyên đề N" mà không kiểm chứng được: chủ đề xung đột lợi ích là chủ đề thứ 4 nhưng lại ghi "Chuyên đề 6". Đã bỏ số chuyên đề và giữ tên nội dung ở các câu sau:
- C4-002: bỏ số chuyên đề.
- C4-003: bỏ số chuyên đề.
- C4-006: bỏ số chuyên đề.
- C4-007: bỏ số chuyên đề.
- C4-010: bỏ số chuyên đề.
- C4-011: bỏ số chuyên đề.
- C4-013: bỏ số chuyên đề.
- C4-014: bỏ số chuyên đề.
- C4-016: bỏ số chuyên đề.
- C4-018: bỏ số chuyên đề.
- C4-023: bỏ số chuyên đề.
- C4-030: bỏ số chuyên đề.
