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
    c = 0
    h = 0
    q = 0
    unprime = []
    diffp1 = [0]
    diffp2 = [4]
    diffp3 = []
    while primenth != len(prime_nos):
        c+=1
        h+=1
        q+=1
        if q < 100:
            if h < 10:
                if primenth == 1:
                    print('1 1')
                    prime_nos.append(1)
                elif prime_id(c) == True and c%5!=0 or c == 5:  
                    if not c%13==0 and not c%7==0 and not c%3==0 or c==13 or c==3 or c == 7:
                        prime_nos.append(c)
                        print(f'{len(prime_nos)} {c}')        
                    else:
                        unprime.append(c)
            
            
            else:
                h+=-10
                diffp1.append(len(prime_nos))
                sumdiffp1 = diffp1[len(diffp1)-1] - diffp1[len(diffp1)-2]
                diffp2.append(sumdiffp1)
                
        else:
            q+=-100
            diffp3.append(sum(diffp2))
            
    diffp2.pop(0)          
    print(diffp3)
    print(diffp2)
    #print(diffp3)
    print(f'The Rrime No. is {prime_nos[primenth-1]}')
    print(unprime)

            

            
    
                



#while True:
    
    #pr_input = int(input('Prime Nos.: '))

    

    #result = 2**prime -1

    #print(result)
4
                  
