import scipy.integrate as itg
from scipy.misc import derivative
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
from Factors import Facno


def f(x):
    return n/x

def C(x,n):
    return (sp.sqrt(1+(sp.diff(n/x))**2))

def P3(x,b):
    return 2*(b-2*x )+1


dip = []
while True:
    n = int(input("Range of Curve: "))
#for n in range(10,10**m,10**(m)):
    x = sp.Symbol('x')
    r = (n/2)-2
    fp2 = (sp.diff(f(x))).subs(x,2)
    c = (sp.integrate(C(x,n),(x,2,n/2))).evalf()
    A = (sp.integrate(f(x),(x,2,n/2))-2*r).evalf()
    P = r*2+c
    l = (P+sp.sqrt(P**2-16*A))/4
    w = A/l
    LPF = (l/2+1)*(w+1)
    Fn = Facno(n)
    diff = LPF - Fn
    dip.append(diff)
    rat = diff/n
    print(diff)
    print(rat)
