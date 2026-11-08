# Review cm_9.json (second pass, 2026-11)

40 questions reviewed. Every number was recomputed independently in `work_review_c9/verify.py`, which asserts each key and each distractor against the file. Overlap with questions.json was checked in `work_review_c9/dups.py` plus keyword searches. The original file is backed up at `work_review_c9/cm_9.orig.json`; all edits are in `work_review_c9/edits.py`. All 40 original keys were arithmetically correct. Key rank among numeric options after the edits: smallest 5, 2nd 10, 3rd 9, largest 4.

C9-015 (put-call parity) was kept: C3-085 prices a put from parity, while C9-015 finds the arbitrage strategy and its profit when parity is violated. C9-011, C9-012 and C9-013 were kept: C3-048, C3-065 and C3-066 are QU items with no twist, while the C9 items test the risk-free asset in a portfolio beta, Sharpe and Treynor disagreeing, and a positive alpha despite a below-market return.

- C9-003: calculation item marked level 2 → level 3 (SCHEMA: 3 = vận dụng/tính toán, as in the rest of the bank).
- C9-006: calculation item marked level 2 → level 3.
- C9-008: same fact and angle as C2-011 (SML, over- or under-valued versus CAPM) → rewritten: two correctly priced stocks on the SML, find E(Rm) (slope 7%, Rf 4,4%, key 11,40%).
- C9-010: same angle as C2-008 (two-asset σp; only the covariance input differed) → rewritten: equally weighted 25-stock portfolio, σp² = σ²/N + (1 − 1/N)Cov, key 21,17%, with the 20% systematic floor as a distractor.
- C9-011: e said "600/500 = 1,20", which is unclear → now "(0,42 + 0,18)/0,5 = 1,20"; level 2 → 3.
- C9-014: same angle as C3-080 (number of index-futures contracts; C3-080's e already gives the full-hedge count) → rewritten as the outcome of the hedge: portfolio −1.100 triệu, futures +1.098,5 triệu, net loss ≈ 1,5 triệu.
- C9-018: distractor 5,45 did not match the error named in e (0,6 × 1,06/0,11 = 5,78) → distractor changed to 5,78 and e shows both distractor formulas; level 2 → 3.
- C9-021: exact duplicate of C5-028 (c > CY > YTM for a premium bond) → rewritten on reinvestment risk: realized compound yield when the coupon is reinvested at 6% (key 9,82%, versus YTM 10%); level 2 → 3.
- C9-022: calculation item marked level 2 → level 3.
- C9-029: stem did not say short selling is allowed → added "Giả sử được phép bán khống."; level 2 → 3.
- C9-031: calculation item marked level 2 → level 3.
- C9-032: calculation item marked level 2 → level 3.
- C9-036: same angle as C1-063 (margin-call trigger with interest ignored; only the % fall was asked instead of the price) → rewritten: margin-call price when accrued interest is added to the debt (13%/year, actual/365, 146 days, maintenance 30%; key 18.786 đồng).
- C9-040: calculation item marked level 2 → level 3.
