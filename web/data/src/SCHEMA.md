# Định dạng câu hỏi (mỗi file là một mảng JSON)

```json
{
  "id": "L1-001",
  "part": "LUAT",            // "LUAT" hoặc "CM"
  "subject": "LU",           // LU | CB | PT | MG | BC | BL | QU | PS
  "topic": "Chào bán chứng khoán ra công chúng",
  "level": 2,                // 1 = Nhớ, 2 = Hiểu, 3 = Vận dụng/tính toán
  "q": "Câu hỏi…",
  "o": ["A", "B", "C", "D"], // đúng 4 phương án
  "a": 1,                    // chỉ số đáp án đúng (0–3), MỘT đáp án
  "e": "Giải thích ngắn, có bước tính nếu là bài tính",
  "basis": "Điều 15 khoản 1 điểm a Luật Chứng khoán 2019 (sửa đổi bởi Luật 56/2024/QH15)",
  "quote": "Trích nguyên văn ≤ 300 ký tự từ văn bản (bắt buộc với câu Luật)",
  "src": "VBHN_24_VBHN-VPQH_2025_Luat_Chung_khoan_hop_nhat_Cong_bao.txt",
  "as_of": "2026-11"
}
```

Quy tắc:
- Một đáp án đúng duy nhất; không dùng "Tất cả các phương án trên", "A và B", "Không phương án nào" hay bất kỳ phương án tham chiếu phương án khác.
- Phương án nhiễu hợp lý (số gần đúng, quy định cũ, cơ quan khác…), độ dài các phương án tương đương nhau.
- Câu phủ định viết HOA chữ KHÔNG / NGOẠI TRỪ.
- Câu Luật: đúng theo văn bản hiện hành tháng 11/2026; nếu điều đã bị sửa (Luật 56/2024, NĐ 245/2025, TT 102/2025, TT 136/2025, TT 08/2026, NĐ 306/2025, TT 135/2025) thì dùng nội dung mới và ghi rõ văn bản sửa trong "basis". "quote" phải trích đúng nguyên văn từ file trong "src" (để máy kiểm tra được).
- Câu tính toán: tự tính lại bằng Python; đáp án nhiễu lấy từ lỗi tính thường gặp.
