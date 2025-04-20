# 입력된 금액을 동전으로 교환, 동전별 교환 개수 출력

def exchange(money) :

    m500 = money // 500
    money %= 500

    m100 = money // 100
    money %= 100

    m50 = money // 50
    money %= 50

    m10 = money // 10

    print("500원 동전의 개수: ", m500)
    print("100원 동전의 개수: ", m100)
    print("50원 동전의 개수: ", m50)
    print("10원 동전의 개수: ", m10)

def get_integer(prompt) :
    msg = int(input(prompt))
    return msg

step1 = get_integer("동전으로 교환하고자 하는 금액은? ")
exchange(step1)