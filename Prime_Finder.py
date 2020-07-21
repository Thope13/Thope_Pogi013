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
    primenth = int(input('Prime Nos: '))
    takbo = 100
    prime_nos = []
    c = 0
    unprime = []
    
    if (prime_id(primenth)-1)%primenth == 0:
        print('It is a Prime!')
    else:
        print('Not a Prime:(')

            

            
    
                



#while True:
    
    #pr_input = int(input('Prime Nos.: '))

    

    #result = 2**prime -1

    #print(result)
4
                  
