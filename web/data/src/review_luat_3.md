# Review luat_3.json (second pass, 2026-11-08)

All 35 L3 items checked against the current texts: TT 120 (VBHN 08/VBHN-BTC/2026), TT 119 (VBHN 45/VBHN-BTC/2025), TT 08/2026 (English SSC; the Vietnamese .txt is empty), NĐ 155 + NĐ 245, Luật CK (VBHN 102/VBHN-VPQH/2026). All 35 keys are correct under the current text. Every quote is verbatim. No L3 item duplicates another bank item (highest word overlap 0.59, L3-013 vs L2-034: margin lending 180% vs stock lending 220%). No stem or option copies slide wording (8-gram check: only statutory phrases match). Exchange rules (sessions, order types, bands, lots, T+n) are not asserted as current anywhere. Answer index in the source cycles 0–3; `kiem_tra.py` re-rotates it anyway. Edits: `scratchpad/work/apply.py`. 11 L3 items, C1-057 and L2-090 changed. No key changed, except C1-057, which was rewritten.

## luat_3.json
- L3-003: distractor D ("ủy quyền bằng lời nói") was implausible → replaced with a plausible one (via a domestic fund manager's account).
- L3-005: stem stated the session layout (morning continuous session, closing call, LO order) as fact. That is an exchange rule and may change with KRX → now stated as an assumption ("Giả định quy chế giao dịch của Sở…"). "Lệnh giới hạn" dropped; explanation says so.
- L3-006: NEGATIVE stem reworded into natural Vietnamese ("đều là ngoại lệ của quy định này, NGOẠI TRỪ").
- L3-016: basis now says Art 97 is not amended by NĐ 245.
- L3-017: key was much shorter than the distractors (39 vs 64–79) → options rebalanced (64–71); basis says Art 99 is not amended by NĐ 245.
- L3-018: src/basis moved to VBHN 102/VBHN-VPQH/2026 (Art 46, 49 unchanged); the quote matches.
- L3-021: src/basis moved to VBHN 102/VBHN-VPQH/2026 (Art 52.2, 53, 54.1 unchanged); the quote matches.
- L3-023: basis says Art 165 is not amended by NĐ 245.
- L3-024: basis says Art 166 is not amended by NĐ 245.
- L3-030: "thiếu chứng khoán cho một giao dịch có giá trị 2 tỷ" was ambiguous (whole trade or only the delayed part; Art 40h.4 uses the value of the delayed trade) → stem now gives "giá trị giao dịch lùi thanh toán là 2 tỷ đồng"; answer 200 million unchanged.
- L3-032: distractor C contradicted itself ("chia đều … theo tỷ lệ") → reworded; key reworded into natural Vietnamese.
- Verified, no change: L3-001, 002, 004, 007–015, 019, 020, 022, 025–029, 031, 033–035.

## Other files
- C1-057 (cm_1.json): asserted the HOSE reference-price rule (previous close) as current, with no current text behind it → rebased on cl. 3 Art 2 TT 120 (VBHN 08/2026): reference price = the price the Exchange sets as the basis for the ceiling/floor. Quote/src added; the explanation says how it is set (normally the previous close, adjusted for corporate actions) is an Exchange rule to check against the current regulation. a = 0.
- L2-090 (luat_2.json): rechecked against VBHN 16/VBHN-BTC/2026. Art 9.2(c) is unchanged (NĐ 306 only amended 9.2(d), 9.3(d) and repealed 9.2(g, h), 9.3(c)), so 1,200 bn is still the key; src/basis moved to the consolidated text.

## Part B: newer consolidations
- Downloaded: `VBHN_16_VBHN-BTC_2026_ND158_306_phai_sinh_hop_nhat.txt` (Công báo số 324 ngày 15/05/2026; docx from congbaocdn.chinhphu.vn, found through api-searchcongbao.chinhphu.vn; URL and date on line 1). `VBHN_102_VBHN-VPQH_2026_Luat_Chung_khoan_hop_nhat.txt` was already in van_ban_txt (line 1 has URL and date).
- (a) VBHN 102/VBHN-VPQH (22/04/2026) adds only Luật Phục hồi, phá sản 142/2025/QH15 (effective 01/03/2026) beyond Luật 56/2024.
- (b) Article-by-article diff against VBHN 24 (footnotes removed): the only change in substance is Art 96.3, where "pháp luật về phá sản" becomes "pháp luật về phục hồi, phá sản" (Art 86.5, Luật 142/2025). The rest is spelling only: hủy/huỷ in Art 38 and 125, hòa/hoà in Art 133. The VBHN header and signature block also changed.
- (c) No bank item cites Art 96, and none mentions Luật Phá sản. Of the 176 quotes with src VBHN 24, 175 occur verbatim in VBHN 102. The other, C8-001 (Art 133), differs only in hòa/hoà, so it is left on VBHN 24. Nothing is wrong.
- (d) L2-090: see above, still correct. All 8 bank quotes from the original NĐ 158 also occur verbatim in VBHN 16.
