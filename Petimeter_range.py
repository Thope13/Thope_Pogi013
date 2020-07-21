from Traditional_Factor import Factor
def P(sq):
    Pt2 = lambda x : 2*f[x]+2*(f[-x-1]-(2))
    f = Factor(sq)
    Ps = []
    for x in range(1,int(len(f)/2)):
        P = Pt2(x)
        Ps.append(P)
    return Ps



none = []
one = []
n = int(input("Range: ").upper())
for mn in range(n):
    s = P(mn)
    if len(s) == 0:
        none.append(mn)
        p = []
    elif len(s)==1 and s[0]!=mn:
        one.append(s)

        print(f'{mn}|{s}')
