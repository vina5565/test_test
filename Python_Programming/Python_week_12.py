import os
import pickle

num1 = 1
name1 = '이수빈'
num2 = 2
name2 = '김철수'
num3 = 3
name3 = '김민지'


filename = 'example.txt'
lines = []
if os.path.exists(filename) :
    with open('example.txt', 'w') as file :
        file.write(f"{num1}. {name1}\n")
        file.write(f"{num2}. {name2}\n")
        file.write(f"{num3}. {name3}")
        print("파일 열어 쓰고 닫기 완료")
    with open('example.txt', 'r') as file :
        for line in file :
            lines.append(line.strip())
else :
    print(f"{filename}은 존재하지 않습니다.")
print(lines)

filepath = 'example.bin'

def save_data(num, name, height, scores) :
    with open(filepath, 'wb') as file :
        pickle.dump(num, file)
        pickle.dump(name, file)
        pickle.dump(height, file)
        pickle.dump(scores, file)

def load_data() :
    with open(filepath, 'rb') as file :
        num = pickle.load(file)
        name = pickle.load(file)
        height = pickle.load(file)
        scores = pickle.load(file)

    return num, name, height, scores

num, name, height = 123, '홍길동', 185
scores = {'mid': 90, 'fin': 95, 'rep': 10, 'att': 10}

save_data(num, name, height, scores)
r_num, r_name, r_height, r_scores = load_data()

print(r_num)
print(r_name)
print(r_height)
print(r_scores)