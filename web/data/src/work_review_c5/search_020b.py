import math
def ceil_t(x,t): return math.ceil(x/t-1e-12)*t
for f in (0.0015,0.002,0.0025,0.003):
  for p0 in range(15000,49000,50):
    t=0.001; tick=50
    ex=p0*(1+f)/(1-f-t)
    K=ceil_t(ex,tick); E1=ceil_t(p0*(1+f),tick); E2=ceil_t(p0*(1+f)/(1-f),tick); E3=ceil_t(p0/(1-f-t),tick)
    E4=ceil_t(p0*(1+f+t)/(1-f-t),tick)
    s={K,E1,E2,E3}
    if len(s)==4 and K==max(s) and ex%50>12 and ex%50<38: print('A',f,p0,round(ex,2),E1,E2,E3,K)
    s={K,E1,E2,E4}
    if len(s)==4 and ex%50>12 and ex%50<38 and p0%100==0: print('B',f,p0,round(ex,2),E1,E2,K,E4)
