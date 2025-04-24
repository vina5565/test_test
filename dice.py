import random

def run_lotto() :
    nums = random.sample(range(1, 46), 6) # random.sample(p, k) = p에서 k개의 요소를 뽑아 리스트로 반환하는 함수
    return nums 

def roll_dice() :
    nums = random.sample(range(1, 7), 2)
    return nums

if __name__ == '__main__' :
    run_lotto()
    roll_dice()