#!/usr/bin/env bash
# Chuyển một file sang Markdown: to_md.sh <file> <file_ra.md>
# PDF: lấy chữ theo từng trang (pdftotext); trang không có chữ (ảnh scan) thì OCR tiếng Việt bằng tesseract.
# File khác (docx, pptx, xlsx, html…): markitdown.
set -euo pipefail
in="$1"; out="$2"
case "${in,,}" in
  *.pdf)
    n=$(pdfinfo "$in" | awk '/^Pages:/{print $2}')
    tmp=$(mktemp -d); trap 'rm -rf "$tmp"' EXIT
    : > "$out"
    for ((p=1; p<=n; p++)); do
      txt=$(pdftotext -f $p -l $p -layout "$in" - | sed 's/[[:space:]]*$//' | cat -s)
      if [ "$(printf %s "$txt" | tr -d '[:space:]' | wc -c)" -lt 20 ]; then
        pdftoppm -f $p -l $p -r 250 -gray -png "$in" "$tmp/p"
        txt=$(tesseract "$(ls "$tmp"/p*.png)" - -l vie --psm 6 2>/dev/null | sed 's/[[:space:]]*$//' | cat -s); rm -f "$tmp"/p*.png
        printf '## Trang %d (OCR)\n\n%s\n\n' $p "$txt" >> "$out"
      else
        printf '## Trang %d\n\n%s\n\n' $p "$txt" >> "$out"
      fi
    done ;;
  *) markitdown "$in" > "$out" ;;
esac
echo "$out: $(wc -l < "$out") dòng"
