# chatgpt 1. 외부 파일 텍스트에서 숫자 읽어와 리스트에 넣고 평균 구하기

def read_file() :
    file = open("number.txt", "r")
    lines = file.readlines() # 괄호 필수
    lst = []
    for i in lines : # i는 문자열이니까 int 필수
        num = int(i.strip())
        lst.append(num)
    file.close() # 괄호 필수
    return lst

def get_average(l) :
    
    k = 0

    for i in range(len(l)) :
        k += l[i] # 리스트를 더해야함 k + l[0] / k + l[1] ...
    return k / len(l)

lst = read_file()
print(f"입력된 숫자 목록 : {lst}")
ave = get_average(lst)
print(f"평균 : {ave:.2f}")

# chatgpt 2. 문자열을 받아 단어별 길이 출력하는 함수 만들기
# split은 자동으로 공백을 기준으로 문자열 나눔 / () 인수로 구분자 지정 가능, split 실행 시 라스트에 나눠서 저장

def get_str() :
    s = input("문자열을 입력하세요 : ").split()

    dic = {}

    for i in range(len(s)) :
        k = len(s[i]) # i는 변수 / s는 리스트 그 자체 = s[i] == s[0], s[1] ...
        dic[s[i]] = k
    return dic

res = get_str()
for key in res :
    print(f"{key} : {res[key]}") # .keys, .vaiues는 함수가 아니라 속성이기 때문에 ()
# 딕셔너리의 실행 방식의 특이성 딕셔너리 요소 추가 방법 dic[key] = value 딕셔너리는 리스트와 다르게 반복문에서 그냥 하나씩 꺼내줌
# key = dic의 키 값 / dic[key] = dic의 value 값

# chatgpt 3. 홀수만 골라서 새로운 리스트 만들기

def only_odd() :
    num_lst = input("정수를 입력하세요 : ").split(",")

    odd_lst = []

    for i in range(len(num_lst)) :
        if int(num_lst[i]) % 2 == 1 : # input함수는 '문자열'만을 반환하기 때문에 int() 필수
            odd_lst.append(num_lst[i])
    return odd_lst

result = only_odd()
print(f"홀수 목록 : {result}")


# chatgpt 3. 홀수만 더하기

def only_even() :
    num_lst = input("정수를 입력하세요 : ").split(",")

    even_lst = []

    for i in range(len(num_lst)) :
        if int(even_lst[i]) % 2 == 0 :
            even_lst.appendint((num_lst[i]))
    return even_lst

result_even_lst = only_even()
k = 0
for i in range(len(result_even_lst)) :
    k += result_even_lst[i]
print(f"짝수의 합 : [{k}]")