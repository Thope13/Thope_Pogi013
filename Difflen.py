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
    primenth = int(input('Nth Prime: '))+1
    takbo = 100
    prime_nos = [2]
    c = 1
    h = 1
    unprime = []
    diffp1 = []
    diffp2 = []
    while primenth != len(prime_nos):
        c+=2
        h+=2
        if h < 10:
            if primenth == 1:
                print('1 1')
                prime_nos.append(1)
            elif prime_id(c) == True and c%5!=0 or c == 5:  
                if not c%13==0 and not c%7==0 and not c%3==0 and not c%11==00 or c==13 or c==3 or c == 7 or c == 11:
                    prime_nos.append(c)
                    print(f'{len(prime_nos)+1} {c}')        
                else:
                    unprime.append(c)
                        
        else:
            h+=-10
            diffp1.append(len(prime_nos))
            

    
    print(diffp1)
    print(diffp2)
        
    print(f'The Rrime No. is {prime_nos[primenth-1]}')
    print(unprime)

            

            
    
                



#while True:
    
    #pr_input = int(input('Prime Nos.: '))

    

    #result = 2**prime -1

    #print(result)
4
                  
