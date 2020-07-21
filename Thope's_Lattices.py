import scipy as sp
from numpy.lib.scimath import sqrt

A, P = float(input("Type the Area: ")), float(input("Type the Perimeter: "))

l = (P+sqrt(P**2-16*A))/4
w = A/l
TL = (l+1)*(A/l+1)
TL2 = A + P/2 +1
print(TL,TL2,l,w)
