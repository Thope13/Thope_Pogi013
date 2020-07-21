import pickle
p_primes = pickle.load(open("Partial_Primes.txt", "rb"))

def qt(q):
    if q%3==0:
        q+=-2
        if q%3==0:
            q+=-2
    elif q%2==0:
        q+=-1
        return print("It's obviously divisible bt 2!")
    elif q%5==0:
        return print("It's obviously divisible bt 5!")
    else:
        return q


while True:
    ilan = input("n or nth or f: ")
    if ilan == 'nth':    
        th = int(input("Nth Partial Primes: "))
        print(f"{p_primes[th-2]} is the {th}th Partial Prime Number")

    elif ilan == 'n':
        th = int(input("N of Partial Primes: "))

        try:
            n = p_primes.index(th)+2
            print(f"{th} is the {n}th Partial Prime Number")
        except:
            print("This is not a Partial Prime Number")
    elif ilan == 'f':
        th = int(input("Find the Nearest P: "))
        q = th
        while q%5==0 or q%2==0 or q%3==0:
            q+=-1
        else:    
            print(f" Your P is {q}")
        
    else:
        print("Invalid Input")
    
