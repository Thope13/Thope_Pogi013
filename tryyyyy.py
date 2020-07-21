from Traditional_Factor import Factor
import math as m




Pt = int(input("a"))
St = []
g = lambda x:(Pt+4)/2-x
for x in range(2,m.ceil(Pt/4)+1):
    y = g(x)
    if y%1==0:
        print(f'{x} | {y})')
    
        St.append(int(x*y))
print(St)
