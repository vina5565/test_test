# 파이썬 프로그래밍 2주차
# print("Hello"); print("World!")

# print("2 + 3 =", 2 + 3)

# help('keywords')

"""
def show_message() :
    print("Hello World!")
    print("Good Job!")
print("Start")
show_message()
print("Finish")
"""

"""
Num_Student = '백명'
print(Num_Student)
print(type(Num_Student))
"""

"""
a = 'abc'
print(id(a))
"""


"""
def show_message(name) :
    print("Hello!", name, "님, 환영합니다.")
print("시작")
show_message('손흥민')
print("끝")
"""

"""def show_message(msg, name, finish) :
    print(msg, name, '님', finish)
print("시작")
show_message('환영합니다.', '손흥민', '안녕히 가세요.')
print("끝")"""

"""
def show_message(msg, name, finish) :
    print(msg, name, '님', finish)

print("시작")
show_message(msg = "환영합니다.", name = "손흥민", finish = "좋은 시간 보내세요.")
show_message(name = "박지성", finish = "좋은 시간 보내세요.", msg = "환영합니다.")
print("끝")"
"""

"""
def show_message(msg = "환영합니다.", name = "모험가", finish = "좋은 시간 보내세요.") :
    print(msg, name, '님', finish)

print("시작")
show_message(msg = "다시 방문해주셨군요.", name = "손흥민")
show_message(name = "박지성")
show_message()
show_message(finish = "당신의 이름은 무엇인가요.")
print("끝")
"""

"""
print("Life", "is", "too", "short", sep = ', ')
print("You need Python" )

print("Life is too short", end = ' ')
print("You need Python" )
"""


"""def show_message() :
    print("Hello!")
    return("Good bye!")

result = show_message()
print(result)"""


"""print("당신의 이름은? ", end = "")
name = input()
print("환영합니다", name, "님")

name = input("당신의 이름은? ")
print("환영합니다", name, "님")"""

"""
def make_message(name) :
    msg = "환영합니다. " + name
    print(msg)

print("Start")
input_name = input("당신의 이름은? ")
make_message(input_name)
print("Finish")
"""

"""
def make_message() :
    name = input("당신의 이름은? ")
    msg = "반가워요 " + name
    return(msg + " 님 좋은 시간 보내세요.")

print("Start")
result = make_message()
print(result)
print("Finish")
"""

"""
def make_message(name) :
    msg = "반가워요 " + name
    return msg

print("Start")
input_name = input("당신의 이름은? ")
result = make_message(input_name)
print(result)
print("Finish")
"""