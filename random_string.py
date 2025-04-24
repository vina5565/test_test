import random
import string

# 8개의 소문자를 랜덤으로 출력하는 함수

def random_string(length = 8) : # parameter에서 변수 선언, 고정의 의미
    chars = string.ascii_lowercase # cf. method, 문자열 내장 함수 (아스키코드 소문자 의미)
    return ''.join(random.choices(chars, k = length)) # ''.join() = parameter를 하나의 문자열로 이어붙이는 함수 ! 

k = random_string()
print(k)

# 길이를 사용자에게 입력 받고 대문자, 소문자, 숫자를 포함한 랜덤 문자열 출력 함수

def random_string_real() :
    length = int(input("문자열의 길이를 입력해주세요 : "))
    chars = string.ascii_letters + string.digits # 아스키코드 대문자 + 소문자 = letters, 숫자 = digits
    return ''.join(random.choices(chars, k = length))

j = random_string_real()
print(j)