# 누진세 계산 if, elif

def electricity(prompt) :
    k = int(input(prompt))

    if k <= 100 :
        return k * 60
    elif k <= 200 :
        return (k - 100) * 125 + 6000
    else :
        return (k - 200) * 200 + 6000 + 12500
    
bill = electricity("전기 사용량을 입력해주세요 : ")
print(f"당신의 전기 요금은 총 {bill}원 입니다.")

# 주사위 시뮬레이션

import random

def roll_dice() :
    return random.randint(1,6) #랜덤 변수 범위

for i in range(10) : # for 변수 in range(시작, 끝, 단위)
    print(roll_dice())


# 디지털 도어락

def doorlock() :
    PWD = "#1234*"
    max_try = 5 # 시도횟수 제한 설정
    try_count = 0 # 시도횟수 변수 초기화

    while try_count < max_try : # 조건 : 시도횟수 초과 시 탈출
        user_input = input("비밀번호를 입력하세요 : ")

        if user_input == PWD :
            print("문이 열렸습니다. ")
            break # 문이 열렸다면 바로 탈출
        else :
            try_count += 1
            print(f"비밀번호가 틀렸습니다. 5회 실패 시 잠금 처리됩니다. {try_count}/{max_try}")
    print("도어락이 잠금 처리되었습니다.")

doorlock()

# 10진정수의 각 자릿수를 한글로 읽어주는 프로그램

def read_single_digit(digit) : # 정수 0~9를 입력받아 대응되는 한글을 리턴
    hangul_digits = ['영', '일', '이', '삼', '사', '오', '육', '칠', '팔', '구'] # 리스트 선언, 인덱스 0부터 대응
    return hangul_digits[digit] # 리스트 변수 반환

def read_number(num) :
    if num < 0 :
        print("마이너스", end = ' ')
        num = -num # 음수로 입력받은 숫자를 양수로 바꿔주기

    if num > 999 :
        print("세 자리 이하의 정수만 입력하세요.")
        return 0

    digits = list(str(num)) # 입력받은 숫자 문자열화, 리스트화
    for s in digits : # 리스트에 들어있는 숫자를 하나 씩 꺼내 함수(리스트)에 대응
        print(read_single_digit(int(s)), end = ' ') # 정수 → 문자열 → 리스트 → 반복 → 숫자로 변환 → 함수 호출 (인덱싱)

if __name__ == "__main__" : # 이 파일이 직접 실행될 때만 아래 코드 실행 / import했을 때 실행 제외
    num = int(input("세 자리 정수를 입력하세요.(ex : 345) "))
    if -999 <= num <= 999 :
        read_number(num)
    else :
        print("오류: 유효하지 않은 숫자가 입력되어 판별할 수 없습니다!")

# 문자열 카운트
week = "월화수목금금금"
n = week.count("금")
print (n)


