from math import sqrt
# C3-010 new WACC
E,D,Eb=700,300,250;rE,rD,t=.14,.09,.2
print('010', E/(E+D)*rE+D/(E+D)*rD*(1-t), Eb/(Eb+D)*rE+D/(Eb+D)*rD*(1-t), E/(E+D)*rE+D/(E+D)*rD, (rE+rD*(1-t))/2)
# C3-012 new
D1=1800*1.05;print('012',D1/(36000*.96)+.05,D1/36000+.05,1800/(36000*.96)+.05,1800/36000+.05)
# C3-021 residual dividend
NI,cap=200,250;print('021',NI-.6*cap,NI-.4*cap,NI-cap,.6*cap)
# C3-039 min variance weight
sA,sB,r=.20,.10,.3
w=(sB**2-r*sA*sB)/(sA**2+sB**2-2*r*sA*sB);print('039',w,sB**2/(sA**2+sB**2),sB/(sA+sB),1-w)
v=lambda w:w*w*sA*sA+(1-w)**2*sB*sB+2*w*(1-w)*r*sA*sB
print('  check min', v(w)<v(w+.001) and v(w)<v(w-.001), sqrt(v(w)))
# C3-040 new
er=(54000+1500-50000)/50000;req=.05+1.1*(.12-.05);print('040',er,req,1.1*.12,1.1*.07,(54000-50000)/50000)
# C3-050 HPR
P0=8/1.1+8/1.1**2+108/1.1**3;P1=8/1.09+108/1.09**2;P1u=8/1.1+108/1.1**2
print('050',P0,P1,(P1+8-P0)/P0,(P1-P0)/P0,8/P0,(P1u+8-P0)/P0)
# C3-051 portfolio MD
V=[40,60,100];M=[2,5,8];md=sum(a*b for a,b in zip(V,M))/sum(V)
print('051',md,-md*.005*200,-sum(M)/3*.005*200,-md*.01*200,-md*.0005*200)
# C3-063 CV
p=[.25,.5,.25];x=[30,12,-10];Er=sum(a*b for a,b in zip(p,x));sd=sqrt(sum(a*(b-Er)**2 for a,b in zip(p,x)))
raw=sqrt(sum(a*b*b for a,b in zip(p,x)));m=sum(x)/3;eq=sqrt(sum((b-m)**2 for b in x)/3)
print('063',Er,sd,sd/Er,Er/sd,raw/Er,eq/Er,sd*sd)
# C3-084 new
pay=(49800-45000)/2;print('084',(pay-1200)*20000,(4800-1200)*20000,pay*20000,(pay-600)*20000)
