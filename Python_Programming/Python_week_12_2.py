import os

filename = 'readme.txt'
lines = []
count = 1

if os.path.exists(filename) :
    with open(filename, "r", encoding = 'utf8') as file :
        for line in file :
            lines.append(line.strip("\n"))

print(f"파일명 : {filename}")
for line in lines :
    print(f"{count} : {line}")
    count += 1