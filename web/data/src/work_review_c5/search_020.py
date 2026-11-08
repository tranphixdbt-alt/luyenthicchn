import math
def ceil_t(x,t): return math.ceil(x/t-1e-12)*t
def floor_t(x,t): return math.floor(x/t)*t
res=[]
for p0,tick in [(p,50) for p in range(15000,50000,50)]+[(p,100) for p in range(50000,99901,100)]:
    for f in (0.0015,0.002,0.0025):
        t=0.001
        ex=p0*(1+f)/(1-f-t)
        key=ceil_t(ex,tick); bo=ceil_t(p0*(1+f),tick); nt=ceil_t(p0*(1+f)/(1-f),tick); dn=floor_t(ex,tick)
        if len({key,bo,nt,dn})==4 and bo<nt<dn<key: res.append((p0,tick,f,round(ex,2),bo,nt,dn,key))
print(len(res))
for r in res: print(r)
