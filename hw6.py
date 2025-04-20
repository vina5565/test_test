
for j in range(2) :
    for k in range(9) :
        for i in range(4) :
            dan = i + 2 + (j * 4)
            print(f"{dan} x {k+1} = {dan*(k+1):2}", end = '   ')
        print()
    print()