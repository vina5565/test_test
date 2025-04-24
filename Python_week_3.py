"""def show_division(n1, n2) :
    quotient = n1 // n2
    remainder = n1 % n2
    
    print("몫 =", quotient)
    print("나머지 =", remainder)

n1 = int(input("피젯수를 정수로 입력해주세요 :"))
n2 = int(input("젯수를 정수로 입력해주세요 :"))

show_division(n1, n2)"""

"""
def show_change(money) :
    
    n10000 = money // 10000
    money %= 10000 # money = money % 10000

    n5000 = money // 5000
    money %= 5000

    n1000 = money // 1000
    money %= 1000

    n500 = money // 500
    money %= 500

    n100 = money // 100

    print("> 10000원권", n10000, "장")
    print("> 5000원권", n5000, "장")
    print("> 1000원권", n1000, "장")
    print("> 500원권", n500, "장")
    print("> 100원권", n100, "장")


total_cost = int(input("고객이 구매한 물품의 총 가격 :"))
payment = int(input("고객으로부터 받은 돈 : "))
change = payment - total_cost
print("잔돈 :", change, "원")
show_change(change)
"""

"""
def fahrenheit_to_celsius(fahrenheit) :
    
    celsius = 5/9*(fahrenheit-32)
    return celsius

def get_real(msg) :

    message = float(input(msg))
    return message

temper1 = get_real("변환하고자 하는 화씨온도? ")
temper2 = fahrenheit_to_celsius(temper1)
print("화씨", temper2, "도는 섭씨", temper1, "도")
"""

"""def convert_time(second) :
    sec = second

    hour = sec // 3600
    hour %= 60

    minute = sec // 60
    minute %= 60

    print(hour,"시간", minute,"분", sec,"초이다.")


def get_real(msg) :
    message = int(input(msg))
    return message

time1 = get_real("변환하고자 하는 시간(초)? ")
time2 = convert_time(time1)
convert_time(second)"""


def set_all_bits(N) :
    
    setting1 = 2**N-1
    setting2 = bin((2**N)-1)
    return  setting1, setting2

def get_integer(msg) :
    message = int(input(msg))
    return message

bit = get_integer("설정할 비트 수는? ")
set_1, set_2 = set_all_bits(bit)
print("8 비트를 모두 1로 설정한 수는", set_1, set_2, "이다.")

