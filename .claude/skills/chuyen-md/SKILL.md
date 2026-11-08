---
name: chuyen-md
description: Chuyển file Word (.docx), PDF, PowerPoint, Excel, HTML sang Markdown (.md) bằng markitdown của Microsoft. Dùng khi người dùng gửi file tài liệu/bộ câu hỏi và muốn "chuyển thành md", "đọc file word", "convert sang markdown".
---

# Chuyển file sang .md

1. Cài một lần (nếu `markitdown file.docx` báo thiếu gói):
   `$(head -1 "$(which markitdown)" | sed 's/^#!//') -m pip install -q 'markitdown[docx,pdf,pptx,xlsx]'`
   Không có markitdown: `pip install 'markitdown[docx,pdf,pptx,xlsx]'`.
2. Chuyển: `markitdown "<file>" > "<thư mục ra>/<tên>.md"`. Nhiều file thì lặp từng file.
3. Đặt tên .md ngắn, không dấu, theo nội dung (vd. `3_xung_dot_loi_ich.md`).
4. Mở lại vài chục dòng đầu để kiểm tra; báo người dùng số dòng mỗi file.

Lưu ý:
- Danh sách đánh số tự động trong Word ra thành `1. 2. 3. 4.` (tương ứng A B C D); chữ **đậm** hoặc dấu ✅ thường là đáp án được đánh dấu.
- PDF scan (ảnh chụp) không có lớp chữ thì markitdown ra rỗng: cần OCR, báo người dùng.
- Tài liệu của bên thứ ba để trong `soat_xet/` (đã bị .gitignore), không đưa lên kho mã công khai.
