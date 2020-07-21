import math as m
import scipy as sci
from Traditional_Factor import Factor

def S(Pt):
    St = []
    g = lambda x:(Pt+4)/2-x
    for x in range(2,m.ceil(Pt/4)+1):
        y = g(x)
        St.append(int(x*y))
    return St

def P(sq):
    Pt2 = lambda x : 2*f[x]+2*(f[-x-1]-(2))
    f = Factor(sq)
    Ps = []
    for x in range(1,int((len(f)/2))):
        P = Pt2(x)
        Ps.append(P)
    return Ps


while True:
    mn = input("P or S: ").upper()
    if mn == 'P':
        sq = int(input("Petimeter of: "))
        a = m.sqrt(sq)+1
        s = P(sq)
        print(s)
        if m.sqrt(sq).is_integer()==True:
            t = 4*(a-1)
            print(f"Petimeters of {sq} are {t}")
        elif len(s) != 0 and m.sqrt(sq).is_integer()==False:
            print(f"Petimeters of {sq} are {s}")
            p = []
            for i in s:
                p.append(S(i))
            
            #print(f"Their Squares are {p}")
                
        else:
            print("There is No Petimeters :(")
        
    elif mn == 'S':
        Pt = int(input("Square of: "))
        p = S(Pt)
        print(f"Squares of {Pt} are {p}")
        s = []
        for i in p:
            s.append(P(i))
        print(f"Their Petimeters are {s}")
        
    

