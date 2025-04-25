def input_number(prompt) :
    n = 0
    while n <= 0 :
        n = int(input(prompt))
    
    return n

def display_multiplication(n) :

    i = 1
    while i <= 9 :
        print(f"{n} x {i} = {n * i:2d}")
        i += 1


n = input_number("양의 정수를 입력하시오 : ")
display_multiplication(n)   