
for j in range(2) :# j *= 0, 1 
    for k in range(9) : # k = 0 ~ 8
        for i in range(4) : # i = 0 ~ 3
            dan = 9 - ( i + j * 4)
            print(f"{dan} x {9-k} = {dan*(9-k):2}", end = '   ') # f"{식} = {값:2}"	출력 값을 두 자리 정렬로 예쁘게 맞춤
        print()
    print()