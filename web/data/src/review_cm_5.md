# Review cm_5.json (second pass, 2026-11)

40 questions reviewed. All numbers recomputed independently in `work_review_c5/verify.py` (incl. both auction books); structure and keys checked by `work_review_c5/validate.py`. Original backup: `work_review_c5/cm_5.orig.json`. All 40 original keys were correct; the changes below fix ambiguity, weak or invalid distractors and the key-rank pattern. After the changes, numeric key value-ranks are 5/5/5/3 (was 6/8/3/1) and `a` is 10/10/10/10.

- C5-001: key at the last position → options reordered (MAK now B).
- C5-005: key said a market buy order matches "at the lowest ask", but it sweeps several levels → "khớp lần lượt từ giá bán thấp nhất…".
- C5-006: stem assumption ("được hủy phần khối lượng chưa khớp") gave the answer away → now "quy chế cho phép hủy lệnh LO trong phiên liên tục".
- C5-012: key position → options reordered (key now A).
- C5-013: key position → options reordered (key now B).
- C5-014: relied on the ex-dividend reference adjustment without stating it → stem states that the reference price is adjusted for the cash dividend (band, tick and rounding were already given).
- C5-015: auction stem had no reference price and no tie-break → added a reference price of 60.000 and a "closest to reference" tie-break (max volume still unique at 60.100).
- C5-016: same gap → added a reference price of 41.000 and the tie-break (max volume unique at 41.100).
- C5-019: distractors 4.998/5.006 were not board lots (trivial to drop), and e called 200.049.625 "bỏ qua phí" (that figure includes the fee) → item reworked: max board lot plus an odd lot at the same price, key 4.998 (4.900 + 98); e corrected.
- C5-020: distractor 24.120 was not a valid tick → new numbers (buy 31.200, fee 0,15%) give four valid-tick prices; key 31.350; distractors are buy fee only, no tax, and tax also charged on the buy.
- C5-022: key rank → 38.750 replaced by 34.615 (rights payment ignored); key now 3rd of 4.
- C5-024: key rank → 16,00% replaced by 13,00% (90/360 instead of the stated actual/365); key now highest; e mentions the 16% error.
- C5-028: key position → options reordered (key now B).
- C5-035: key rank → 100.688 and 106.250 replaced by 100.606 (actual/360) and 100.628 (127 days, counting both ends); key now highest.
- C5-038: settlement not stated; key rank → "vừa trả lãi, còn đúng 4 năm"; 13,40% replaced by 8,50% (divided by face value).
- C5-039: settlement date implicit → states that settlement falls on the coupon date with no accrued interest.
- C5-040: "thay đổi xấp xỉ" made duration estimates arguable → asks for the exact PV change rounded to 2 decimals; settlement stated; +2,67%/−1,00% replaced by −2,81% (Macaulay × Δy) and −2,67% (sign-flipped fall case); key −2,58% now highest.
