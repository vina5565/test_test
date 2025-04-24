"""def make_message() :
    name = input("당신의 이름은? ")
    msg = print("환영합니다.", name, "님")

print("Start")
make_message()
print("Finish")"""


"""def make_message(name) :
    msg = print("환영합니다.", name, "님")

print("Start")
imput_name = input("당신의 이름은? ")
make_message(imput_name)
print("Finish")"""

"""def make_message() :
    name = input("당신의 이름은? ")
    msg = "환영합니다. " + name + " 님"
    return msg

print("Start")
print('배고픈', make_message())
print("Finish")"""

def make_message(name) :
    msg = "환영합니다. " + name + " 님"
    return msg

print("Start")
input_name=input("당신의 이름을 입력해주세요. ")
result=make_message(input_name)
print(result)
print("Finish")