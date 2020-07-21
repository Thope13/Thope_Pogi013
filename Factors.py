import math as h


def Facno(m):
    sm = []
    r = h.floor(h.sqrt(m))
    for n in range(2,r+1):    
        t = h.floor(m/n)-n+1
        sm.append(t)
    return sum(sm)

