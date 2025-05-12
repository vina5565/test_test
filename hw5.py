# 리스트 생성 / 리스트 0부터 9까지 한글 '영' 부터 '구'에 대응
def read_single_digit(digits) :
    korean_digits = ['영', '일', '이', '삼', '사', '오', '육', '칠', '팔', '구']
    return korean_digits[digits]

def read_number(num) :

    hendreds = num // 100
    tens = ( num %  100 ) // 10
    ones = num % 10
    
    print(read_single_digit(hendreds), end = ' ')
    print(read_single_digit(tens), end = ' ')
    print(read_single_digit(ones))

if __name__ == "__main__" :
    num = int(input("세 자리 정수를 입력하세요.(ex : 345) "))
    if 100 <= num <= 999 :
        read_number(num)
    else :
        print("오류: 유효하지 않은 숫자가 입력되어 판별할 수 없습니다!")