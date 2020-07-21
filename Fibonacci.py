while True:                
    x = 0
    y = 1
    i = 0
    terms = int(input('Type the Range more than 3: '))
    terms += -3
    while i < terms:
        z = x+y
        print(z)
        w =y+z
        print(w)
        x =z+w
        print(x)
        y =w+x
        print(y)
        i+=1
        
