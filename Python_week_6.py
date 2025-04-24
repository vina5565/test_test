"""
num = int(input("정수를 입력하세요 : "))

if num == 0 :
    print(f"{num}은(는) '0'입니다.")

elif num > 0 and num % 2 == 0 :
    print(f"{num}은(는) 양수인 짝수입니다.")
elif num < 0 and num % 2 == 0 :
    print(f"{num}은(는) 음수인 짝수입니다.")
elif num > 0 and num % 2 == 1 :
    print(f"{num}은(는) 양수인 홀수입니다.")     
else :
    print(f"{num}은(는) 음수인 홀수입니다.")
"""
# 학점 판별기
"""
def get_grade(n) :
    if n >= 90 :
        return 'A'
    elif n >= 80 :
        return 'B'
    elif n >= 70 :
        return 'C'
    elif n >= 60 :
        return 'D'
    else :
        return 'F'

score = int(input("학생의 점수를 입력하세요 : "))

grade = get_grade(score)

print(f"{score}점이므로 '{grade}'입니다.")
"""

"""
def get_year(n) :
    if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0) :
        return True
    else :
        return False

year = int(input("연도를 입력하세요 : "))

print(f"{year}년은", end = ' ')
      
if get_year(year) :
    print("윤년입니다.")
else :
    print("평년입니다.")
"""

"""def get_year(y) :
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0) :
        return True
    else :
        return False
    
def month_days(y, m) :
    if get_year(y) and m == 2 :
        return 29
    elif m == 2 :
        return 28
    elif m in [4, 6, 5, 9, 11] :
        return 30
    else :
        return 31

        
year = int(input("연도? "))
month = int(input("월? "))

result = month_days(year, month)

if month < 1 or month > 12 :
    print("월은 1부터 12 사이의 숫자여야 합니다.")
else :
    print(f"{year}년 {month}월은 {result}일까지 있습니다.")
"""


"""
def input_age(prompt) :
    age = int(input(prompt))
    if age >= 0 and age <= 120 :
        return age
    else : 
        return -1

def is_adult(age) :
    if age >= 19 :
        return True
    else :
        return False
    
age = input_age("나이? ")

if age == -1 :
    print("오류: 유효하지 않은 나이가 입력되어 판별할 수 없습니다!")
elif is_adult(age) :
    print("당신은 성인입니다.")
else :
    print("당신은 성인이 아닙니다.")
"""

"""
def find_char_type(ch) :
    if '0' <= ch <= '9' :
        return "숫자 문자"
    elif 'A' <= ch <= 'Z' or 'a' <= ch <= 'z' :
        return "알파벳 문자"
    elif ch == " " :
        return "공백 문자"
    else :
        return "기타"

char = input("문자를 하나 입력해주세요 : ")

res = find_char_type(char)

if len(char) != 1 :
    print("오류: 유효하지 않은 문자가 입력되어 판별할 수 없습니다!")
else :
    print(f"{res}를 입력했습니다.")
"""
