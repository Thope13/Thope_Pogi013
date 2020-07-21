def Factor(fct):
    factors = []

    for n in range(1,fct+1):
        if fct%n==0:
            factors.append(n)
    return factors
print(Factor(16))

