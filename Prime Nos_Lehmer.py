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
while True:
    primenth = int(input('Nth Prime: '))
    takbo = 100
    prime_nos = []
    c = -1
    unprime = []
    while primenth != len(prime_nos):
        c+=2
        
        if prime_id(c) == True and c%5!=0 or c == 5:  
            if not c%13==0 and not c%7==0 and not c%3==0 or c==13 or c==3 or c == 7:
                prime_nos.append(c)
                print(f'{len(prime_nos)+1} {c}')        
            else:
                unprime.append(c)
    print(f'The Rrime No. is {prime_nos[primenth-1]}')
    print(unprime)

            

            
    
                



#while True:
    
    #pr_input = int(input('Prime Nos.: '))

    

    #result = 2**prime -1

    #print(result)
4
                  
