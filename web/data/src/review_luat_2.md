# Review luat_2.json and so_lieu.json (second pass, 2026-11)

All 95 questions and 48 flashcards checked against the current text. Sources: NĐ 155 + NĐ 245 (Công báo); VBHN 09/2026 (TT 121); TT 91 + TT 102/2025; TT 96 against the consolidated VBHN 10/VBHN-BTC/2026 (web: Art 10, 11, 14, 31, 32 unamended); VBHN 04/2026 (TT 98); NĐ 158 + NĐ 306 (English); NĐ 156 + NĐ 128/2021 (Công báo PDF from the web) + NĐ 306. Web reading is saved in `tai_lieu_phap_ly/Web_TT96_hop_nhat_2026_va_ND128_2021_trich.md`. Checker: `work_review_l2/check.py` (all pass). Edits: `work_review_l2/apply_fixes.py`; originals: `work_review_l2/*.orig.json`. 13 questions changed (1 replaced), 0 deleted; 3 cards changed, 3 added. Keys changed: none, except the new L2-066 (key at index 0, same as before).

## luat_2.json
- L2-004: key = B + C combined and longest (89 vs 60–77 chars) → key and option B shortened (73/62).
- L2-006: stem said only "không có bảo lãnh … nhận mua toàn bộ", but Art 21.5 also exempts underwriting of the remainder → stem now says "nhận mua toàn bộ hoặc mua phần còn lại".
- L2-010: 60 bn of 500 bn charter capital is 12% before the offering but may fall below 10% after it (ambiguous base) → offering size set at 100 bn, unsubscribed 70 bn (14% before / 11.7% after); distractors lengthened (key was longest).
- L2-016: key longest (84 vs 70–76) → shortened.
- L2-019: key longest (82 vs 55–75) → shortened.
- L2-025: key longest (90 vs 69–74) → shortened; stem names NĐ 155.
- L2-037: key longest (85 vs 67–74) → reworded to match option C's form.
- L2-044: Art 293.4(b) adds up transactions over 12 months, and the stem did not rule out earlier deals with Q → stem states there were none; explanation covers the 12-month aggregation and why point c (≥51% shareholder) does not apply.
- L2-045: key much shorter than the distractors (41 vs 59–63) → lengthened.
- L2-066: the premise was wrong. The "25% for derivatives" note was in TT 91's original Appendix V (the fund-manager form); the securities-company form (Appendix VI) always used 20%. So TT 102 removed nothing for securities companies → replaced with a question on the cost items TT 102 added for deduction (point h, clause 2, Art 8 TT 91, added by clause 1, Art 5 TT 102); same topic/level, a = 0.
- L2-076: key longest (85 vs 57–63) → shortened.
- L2-092: (1) NĐ 128/2021 rewrote Art 35.1 (the cap is now "điểm b khoản 3 Điều 5"), so the NĐ 156 quote was no longer current text; (2) the stem did not say organisation or individual, and the 5× option is correct for individuals (Art 5.3) → stem now says an organisation; options now pair the multiple with its 3 bn floor; quote and basis from NĐ 128 (web note).
- L2-095: NĐ 128/2021 rewrote Art 6 ("thời điểm", not "ngày"), so the quote was outdated → options, quote and basis updated to the NĐ 128 text (web note); key unchanged.
- Verified, no change: L2-001–003, 005, 007–009, 011–015, 017–018, 020–024, 026–036, 038–043, 046–065, 067–075, 077–091, 093–094 (NĐ 156 Art 36.2 is not amended by NĐ 128 or NĐ 306).

## so_lieu.json
- Card 31 (re-sit): the window is 01 year *or* the next exam round (Art 213.6c, as amended by NĐ 245) → back now says so.
- Card 39 (operational risk): "TT 102 bỏ mức 25% cho CTCK có phái sinh" was wrong (see L2-066) → back states the max(25% of costs; 20% of minimum capital) rule only; basis names clause 2, Art 8 TT 102.
- Card 48 (NĐ 156 fines): NĐ 128 not cited, and the fine level holds only for organisations → front says organisation; back adds the 3 bn floor and "cá nhân: 1/2"; basis cites clauses 29–30, Art 1 NĐ 128.
- Added 3 exam cards from the UBCK notices (`UBCK_thong_bao_…md`): time per paper (120/150/180 min; 60/75/90 per part), pass mark (≥60% per part; no re-marking), fee (1.000.000 đ/thí sinh/loại chứng chỉ). The re-sit and the 30-day issuance were already on cards 31 and 30.
- Cards 1–30, 32–38, 40–47 verified, no change (card 47's 260% comes from the English NĐ 306, the only text available).

- L2-051: xóa khi gộp ngân hàng (trùng ý L1-025)