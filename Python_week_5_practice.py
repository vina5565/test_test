"""
def introduce(name, grade) :
    return f"{name[1:]}은 내년에 {int(grade) + 1}학년입니다." 


name = input("이름? ")
grade = input("학년? ")
res = introduce(name, grade)
print(res)
"""
def rep_char(char, rep) :
    print(char * rep)

# rep_char('=', 5)

def draw_line_string(str) :
    rep_char('-', (len(str) * 2) + 4)
    print(f"  {str}")
    rep_char('-', (len(str) * 2) + 4)

draw_line_string('안녕하세요')
