def rep_char(char, rep) :
    print(char * rep)

def draw_line_string(str) :

    msg1 = f"Hello {str},"
    msg2 = "Welcome to Seoul."

    if len(msg1) > len(msg2) :
        nstr = len(msg1)
    else : nstr = len(msg2)

    rep_char('-', nstr)
    print(msg1)
    print(msg2)
    rep_char('-', nstr)

name = input("input his/her name : ")
draw_line_string(name)