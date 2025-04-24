exchange_rate = 0 # 환율을 저장하는 전역변수

def set_rate(won) : 
    global exchange_rate
    exchange_rate = won # 1달러에 대한 '원화 값'을 입력받아 exchange_rate를 설정하는 함수

def get_rate() : 
    return exchange_rate # set_rate 함수로 설정한 환율을 반환하는 함수 / 모듈화했을 떄 함수의 분할 

def to_dollar(won) :
    return won / exchange_rate # 원화 → 달러 값 반환

def to_won(dollar) :
    return dollar * exchange_rate # 달러 → 원화 값 반환

# 함수 테스크 코드 / 리터럴을 이용해 각 함수 1회씩 호출
def main() :
    print("### 환율 변환 모듈 테스트 ###")
    set_rate(1435)
    print("오늘의 환율 :", get_rate())
    print("10,000원 = ", to_dollar(10000), "달러")
    print("10 달러 = ", to_won(10), "원")

#메인 모듈로 실행된 경우메나 실행되도록 처리
if __name__ == '__main__' :
    main()