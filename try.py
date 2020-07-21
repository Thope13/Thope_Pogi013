def prime_id(terms):
    n1 = 1
    n2 = 3
    i = 0
    int(terms)
    lucas = [1,3]
    if terms > 1:
        while i < terms:
            nth = n1 + n2
            n1 = n2
            n2 = nth
            lucas.append(nth)
            i+=1
        if (lucas[terms-1]-1)%terms == 0:
            return True
        else:
            return False
    else:
        return False
while True:
    primenth = int(input('Nth Prime: '))
    takbo = 100
    prime_nos = []
    c = 0
    while primenth != len(prime_nos):
        c+=1
        if prime_id(c) == True:
            prime_nos.append(c)
    print(prime_nos)
    print(prime_nos[primenth-1])
            

            
    
                



#while True:
    
    #pr_input = int(input('Prime Nos.: '))

    

    #result = 2**prime -1

    #print(result)
4
                  
