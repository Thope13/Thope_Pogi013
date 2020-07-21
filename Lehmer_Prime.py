from math import sqrt
def prime_id2(terms):
    n1 = 4
    l = 0
    int(terms)
    lehmer = []
    while l < terms:
        l+=1
        nth = n1**2 - 2
        n1 = nth
        lehmer.append(nth)
    mod = (lehmer[(round(sqrt(terms)))-3])%terms
    if mod == 0:
        return True
    else:
        False
while True:
    primenth = int(input('Nth Prime: '))
    prime_nos = []
    c = 1
    unprime = []
    while primenth != len(prime_nos):
        c+=2
        if primenth == 1:
            print('1 1')
            prime_nos.append(1)
        elif prime_id2(c) == True and c%5!=0 or c == 5:  
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
                  
