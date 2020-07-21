import math as m

while True:
    r = int(input("Factors of n: "))

    t = m.atan(-r/2)+3*m.pi/4
    a = (r*m.sqrt(2))/2*m.cos(t)
    a1= (r/m.sqrt(2))/m.cos(t)
    c = 2*a1*m.sin((m.pi-2*t)/2)
    Ap = ((m.pi-2*t)*a1**2)/2
    At1 = r**2/2
    At2 = (c*m.sin(t)*a1)/2
    Ac = Ap-At2
    A = At1-Ac
    rat=Ac/A

    print(f't:{t}')
    print(f'a:{a1}')
    print(f'Ap:{Ap}')
    print(f'At2:{At2}')
    print(f'Ac:{Ac}')
    print(f'{A}')
    print(rat)
