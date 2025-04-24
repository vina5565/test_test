"""
def divide_name(name) :
    lastName = name[0]
    firstName = name[1:]
    print("=" * 20)
    print("성 :", lastName)
    print("이름 :", firstName)
    print("=" * 20)


name = input("당신의 이름은? ")

res = divide_name(name)
"""

week = '금토일금토일금'
pos = week.find('금')
print(pos)
pos = week.find('금', 2)
print(pos)
pos = week.rfind('금')
print(pos)

msg = 'Life is too short, You need 파이썬'
res = msg.replace('파이썬', 'Python')
print(res)
print(msg)