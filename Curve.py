import scipy.integrate as itg
from scipy.integrate import quad
from Factors import Facno
from Traditional_Factor import Factor
from scipy.misc import derivative
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

dip = []
#while True:
mm = int(input("Range of Curve: "))

for n in range(10,mm+10):
    x = sp.Symbol('x')
    r = (n/2)-2
    def f(x):
        return n/x
    
    #print(dp)

    def C(x,n):
        return (sp.sqrt(1+(sp.diff(n/x))**2))

    def P3(x,b):
        return 2*(b-2*x )+1

    def Pdiv(P,x):
        return ((P/2)+1)/x
    def LP(P,b):
        return sp.integrate(P,(x,0,sp.floor((b+1)/4))).evalf()

    fp2= (sp.diff(f(x))).subs(x,2)
    #c = quad(C,2,n/2,args=n)
    c = (sp.integrate(C(x,n),(x,2,n/2))).evalf()
    t = (sp.atan(-fp2)-(sp.pi/4)).evalf()
    #t = m.atan((4/r)+(m.pi/4))
    t1 = (sp.pi-(2*t)).evalf()
    #a = r*m.sqrt(2)/2*m.cos(t)
    
    a = (c/t1)
    
    arc = (2*a*sp.sin(t1/2)).evalf()
    #h = m.sqrt((a**2)-((r**2)/2))
    h = (sp.sin(t)*a).evalf()
    #t1 = (2*m.asin(r*m.sqrt(2)/2*a))
    Ap = t1*a**2/2
    At1 = (r**2)/2
    At2 = (h*arc)/2
    Ac = Ap-At2
    #A = (sp.integrate(f(x),(x,2,n/2))-2*r).evalf()
    A = (sp.integrate(f(x),(x,2,n/2))-2*r).evalf()
    P = r*2+c
    l = (P+sp.sqrt(P**2-16*A))/4
    w = A/l
    LPF = (l/2+1)*(w+1)
    rat = A/Ac
    ftr = Facno(n)
    rat2 = c/ftr
    pxc = (r-2)**2
    ch = ftr-pxc
    b = r
    
    AtP = LP(P3(x,b),b)
    if (b+1)%4!=0:
        Atp=AtP+1
        
    fans=Pdiv(P3(0,b),2)
    ky=ftr/fans
    kz=A/ftr
    
    

    
    

    
    
    dip.append(LPF)
ax = range(len(dip))
plt.plot(ax,(dip))
plt.show()

