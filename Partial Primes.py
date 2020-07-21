import pickle
i = 7
p = [7]

while True:
    ilan = int(input("Ilan: "))
    for u in range(ilan):
        i+=4
        p.append(i)
        i+=2
        p.append(i)
        i+=4
        p.append(i)
        i+=2
        p.append(i)
        i+=4
        p.append(i)
        i+=6
        p.append(i)
        i+=2
        p.append(i)
        i+=6
        p.append(i)

    pickle.dump(p,open("Partial_Primes.txt", "wb"))

    print(f'{p[len(p)-1]} is the {len(p)}th Partial Primes')
