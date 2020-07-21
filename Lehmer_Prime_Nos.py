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
print(prime_id2)
while True:
    primenth = int(input('Prime Nos: '))
    unprime = []
    if prime_id2(primenth) == True and primenth%5!=0 or primenth == 5:  
        prime_nos.append(primenth)
        print(f'{primenth} is a Prime!')        
    else:
        print(f'{primenth} iis not a Prime :(')

           

           
 


            

            
    
                



#while True:
    
    #pr_input = int(input('Prime Nos.: '))

    

    #result = 2**prime -1

    #print(result)
4
                  
