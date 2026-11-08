---
name: chuyen-md
description: Chuyển file Word (.docx), PDF (kể cả PDF scan, OCR tiếng Việt), PowerPoint, Excel, HTML sang Markdown (.md). Dùng khi người dùng gửi file tài liệu/bộ câu hỏi/slide bài giảng và muốn "chuyển thành md", "đọc file word/pdf", "convert sang markdown".
---

# Chuyển file sang .md

Chạy cho từng file: `bash .claude/skills/chuyen-md/to_md.sh "<file>" "<thư mục ra>/<tên>.md"`
- PDF: lấy chữ từng trang bằng `pdftotext -layout` (giữ bố cục slide, có tiêu đề "## Trang N"); trang là ảnh scan thì tự OCR tiếng Việt bằng tesseract ("## Trang N (OCR)").
- File khác: `markitdown`.

Cài một lần nếu thiếu:
- markitdown: `$(head -1 "$(which markitdown)" | sed 's/^#!//') -m pip install -q 'markitdown[docx,pdf,pptx,xlsx]'` (không có markitdown: `pip install 'markitdown[docx,pdf,pptx,xlsx]'`).
- OCR: `apt-get install -y tesseract-ocr tesseract-ocr-vie` (pdftotext/pdftoppm có trong poppler-utils).

Sau khi chuyển:
- Đặt tên .md ngắn, không dấu, theo nội dung (vd. `3_xung_dot_loi_ich.md`); mở vài chục dòng đầu để kiểm tra; báo người dùng số dòng, trang nào phải OCR.
- Word: danh sách đánh số tự động ra `1. 2. 3. 4.` (tương ứng A B C D); chữ **đậm** hoặc ✅ thường là đáp án.
- Chữ OCR có thể sai dấu/số: đối chiếu với PDF (Read tool, tham số pages) trước khi dùng số liệu.
- Tài liệu của bên thứ ba để trong `soat_xet/` (đã bị .gitignore), không đưa lên kho mã công khai.
