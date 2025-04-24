"""
def input_age(prompt) :

    while True :
        try :
            age = int(input(prompt))
            if age >= 0 and age <= 120 :
                return age
            else : 
                print("오류: 유효하지 않은 나이가 입력되어 판별할 수 없습니다!")
        except ValueError :
            print("숫자를 입력해주세요!")

def is_adult(age) :
    if age >= 19 :
        return True
    else :
        return False
    
age = input_age("나이? ")

if is_adult(age) :
    print("당신은 성인입니다.")
else :
    print("당신은 성인이 아닙니다.")
"""

"""
def get_year(n) :
    if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0) :
        return True
    else :
        return False

while True :
    year = int(input("연도를 입력하세요 : "))


    print(f"{year}년은", end = ' ')
      
    if get_year(year) :
        print("윤년입니다.")
    else :
        print("평년입니다.")
    
    again = input("다른 연도도 확인하겠습니까? (Y/N) ")
    if again != "Y" and again != "y" :
        break
"""


"""
n = int(input("높이? "))
for i in range(1, n + 1) :
    for k in range(1, i + 1) :
        print(k, end = "")
    print()
"""

def display_triangle(h, ch = '*') :
    for i in range(1, h + 1) :
        draw_line(' ', h - 1)
        draw_line(ch, i)
        print()

def draw_line(ch, n) :
    for _ in range(n) :
        print(ch, end = ' ')

k = int(input("높이를 입력해주세요 : "))
display_triangle(k)