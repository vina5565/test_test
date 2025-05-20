import os
import pickle

filename = 'score.bin'

def input_score(lst) :
    count = 1
    while True :
        score = int(input(f"#{count}? "))
        if score < 0 :
            break
        lst.append(score)
        count += 1
    return lst

def save_data(score) :
    with open(filename, 'wb') as file :
        pickle.dump(score, file)

def load_data() :
    with open(filename, 'rb') as file :
        score = pickle.load(file)
    return score

def get_average(lst) :
    total = 0

    for i in lst :
        total += i

    return total / len(lst) if lst else 0

grade_lst = []


if os.path.exists(filename) :
    print("[파일 읽기]")
    print()
    print("[점수 출력]")
    grade_lst = load_data()
    print(f"개인 점수 :", end = ' ')
    for score in grade_lst :
        print(score, end = ' ')
    print()
    ave = get_average(grade_lst)
    print(f"평균 : {ave}")

else :
    print("[점수 입력]")
    input_score(grade_lst)
    print("[점수 출력]")
    print(f"개인 점수 :", end = ' ')
    for score in grade_lst :
        print(score, end = ' ')
    print()
    ave = get_average(grade_lst)
    print(f"평균 : {ave}")

save_data(grade_lst)