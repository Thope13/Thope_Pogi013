import pickle
import math as m

while True:
    p_prime = pickle.load(open("Partial_Primes.txt", "rb"))
    r = int(input("Range: "))

    def rp(x):
        while x%5==0 or x%2==0 or x%3==0:
            x+=-1
        return x


    def P(p):
        x = p_prime[p-1]
        return x
    sm = []
    E = 0.26667
    t = 200
    d = 54
    mx = m.ceil(m.floor(m.sqrt(r))*E)
    print(f" mx: {mx} | {m.sqrt(r)}")
    root = int((m.floor(r/t))*d+((r%t)/t)*(d-2))
    print(f" root: {root}")
    for p in range(1,mx-1):
        #print(rp(int(r/P(p)))*E)
        exc = (m.ceil((rp(int(r/P(p)))*E)))-(p+1)
        sm.append(exc)
        #print(exc)
    Except = sum(sm)
    Total = root - sum(sm) + 2
    print(f" Total:{Total} with Exception of {Except}")
