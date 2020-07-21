while True:
    year = int(input("Type the Year: "))

    leap = year%4

    if leap == 0:
        print('That year is a leap year!')
    else:
        print('It` a normal year')
