while True:
    x = int(input('Please Input the 1st No,: '))
    y = int(input('Please Input the 2nd No,: '))
    if x > y:
        z = x
        w = y
    else:
        z = y
        w = x
    tama = True

    while tama:
            if z % 2 == 0 and w % 2 == 0:
                if z % w == 0:
                    print(f'The LCM is {z}')
                    break
                for i in range(1,w):
                    v = z*i
                    if v % z == 0 and v % w == 0:
                        print(f'The LCMs is {v}')
                        tama = False
                        break
                
                            
            else:
                print(f'The LCM is {(x*y)}')
                break
