# 사용자로부터 입력받은 정수값에 대해 별표로 그림그리기
# 핵심 : 반복문, 공백/별 제어

#1. 기본 삼각형

def left_triangle() :
    n = int(input("높이 입력 : "))

    for i in range(1, n + 1) :
        print("*" * i)

left_triangle() # 공백 제어 x, 반복문으로만 구성

def right_triangle() :
    n = int(input("높이 입력 : "))

    for i in range(1, n + 1) :
        print(" " * (n - i) + "*" * i)

right_triangle()

def pyramid() :
    n = int(input("높이 입력 : "))

    for i in range(1, n + 1) :
        print(" " * (n - i) + "*" * (2*i - 1))

pyramid()

def diamond() :
    n =int(input("높이 입력 : "))

    for i in range(1, n // 2 + 2):
        print(" " * (n // 2 - i + 1) + "*" * (2 * i - 1))

    for i in range(n // 2, 0, -1):
        print(" " * (n // 2 - i + 1) + "*" * (2 * i - 1))

diamond()

def hourglass() :
    n =int(input("높이 입력 : "))

    for i in range(n // 2 + 1, 0, -1):  
        print(" " * (n // 2 - i + 1) + "*" * (2 * i - 1))

    for i in range(2, n // 2 + 2):
        print(" " * (n // 2 - i + 1) + "*" * (2 * i - 1))

hourglass()