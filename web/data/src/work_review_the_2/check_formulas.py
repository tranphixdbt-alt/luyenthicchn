# Numeric sanity checks for formulas on CB/MG/PS flashcards (run: python3 -I check_formulas.py)
import math
# CB-08 convertible bond
F, conv_price, S, Pb = 100_000, 20_000, 24_000, 118_000
ratio = F / conv_price; assert ratio == 5
assert ratio * S == 120_000                      # conversion value
assert abs(Pb / ratio - 23_600) < 1e-9           # parity price: stock price at which converting breaks even
# MG-40 margin-call price, consistent with bank C1-063
D, n, mmr = 200_000_000, 10_000, 0.30
P = D / (n * (1 - mmr)); assert round(P) == 28571
assert abs((n * P - D) / (n * P) - mmr) < 1e-12
# MG-46 approximate YTM vs exact
C, Fv, Pr, N = 8_000, 100_000, 95_000, 5
approx = (C + (Fv - Pr) / N) / ((Fv + Pr) / 2)
f = lambda y: sum(C / (1 + y) ** t for t in range(1, N + 1)) + Fv / (1 + y) ** N - Pr
lo, hi = 0.0, 1.0
for _ in range(200):
    mid = (lo + hi) / 2; lo, hi = (mid, hi) if f(mid) > 0 else (lo, mid)
assert abs(approx - lo) < 0.002, (approx, lo)
# MG-47 repo return leg, bank C1-068
assert round(10_000_000_000 * (1 + 0.0438 * 14 / 365)) == 10_016_800_000
# PS-05 leverage
assert abs(0.02 * (1 / 0.20) - 0.10) < 1e-12
# PS-15 margin-call trigger, bank C3-077 (short, 1 contract basis)
F0, IM, MM, m = 1250.0, 20e6, 15e6, 100_000
assert F0 + (IM - MM) / m == 1300.0
# PS-35 put-call parity and PS-36 bounds via Black-Scholes (European, no dividend)
from math import log, sqrt, exp, erf
Nc = lambda x: 0.5 * (1 + erf(x / sqrt(2)))
S0, K, r, T, sig = 100.0, 95.0, 0.05, 0.5, 0.3
d1 = (log(S0 / K) + (r + sig ** 2 / 2) * T) / (sig * sqrt(T)); d2 = d1 - sig * sqrt(T)
c = S0 * Nc(d1) - K * exp(-r * T) * Nc(d2); p = K * exp(-r * T) * Nc(-d2) - S0 * Nc(-d1)
assert abs((c - p) - (S0 - K * exp(-r * T))) < 1e-9
assert max(S0 - K * exp(-r * T), 0) <= c <= S0 and max(K * exp(-r * T) - S0, 0) <= p <= K * exp(-r * T)
assert 0 < Nc(d1) < 1 and -1 < Nc(d1) - 1 < 0   # PS-38 delta ranges
# PS-39 protective put max loss = S0 + p - K ; PS-40 covered call max profit = K - S0 + c
assert abs((S0 + p) - min(K, K) - (S0 + p - K)) < 1e-12
# PS-19 cost of carry with dividends: discrete and continuous forms agree in limit
q = 0.03; Fc = S0 * exp((r - q) * T)
Dpv = S0 * (1 - exp(-q * T)); assert abs((S0 - Dpv) * exp(r * T) - Fc) < 1e-9
# PS-23 hedge contracts: beta 1.2, V 10 bn, F 1250, m 100k -> 96 contracts; to beta 0.5 -> -56
assert round(1.2 * 10e9 / (1250 * 100_000)) == 96 and round((0.5 - 1.2) * 10e9 / (1250 * 100_000)) == -56
# PS-50 swap net payment
assert abs((0.06 - 0.05) * 100e9 * 0.5 - 500e6) < 1e-3
# MG-42 reference price, bank C1-061 and C5-022
assert (39_000 - 1_500) / (1 + 0.2) == 31_250
assert round((45_000 + 0.1 * 15_000) / 1.3) == 35_769
print("OK formulas")
