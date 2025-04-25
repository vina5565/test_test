import random

nums = list(map(int, input("정수 5개를 입력하세요 : ").split()))
print("최댓값 :", max(nums))
print("최솟값 :", min(nums))
print("평균 : ", sum(nums) / len(nums))

# input() → 문자열 전체 입력 받기 (예: "3 9 2 8 4")
# .split() → 공백 기준으로 나눔 → ['3', '9', '2', '8', '4']
# map(int, ...) → 문자열을 int로 변환
# list(...) → 그 결과를 리스트로 변환 → [3, 9, 2, 8, 4]


num = [random.randint(1, 10) for _ in range(5)] # 중복 허용 / '_' 변수를 사용하지 않고 반복문 사용 
print("랜덤 정수 5개 (중복 허용) :", num)

number = random.sample(range(1, 101), 5)
print("랜덤 정수 5개 (중복 없이) :", number)