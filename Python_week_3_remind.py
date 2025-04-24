# 화씨온도를 입력받아 섭씨온도로 변환

"""def fahrenheit_to_celsius(fahrenheit) :
    cel = 5/9*(fahrenheit-32)
    return cel

def get_real(temper) :
    msg = float(input(temper))
    return msg

temper1 = get_real("변환하고자 하는 화씨온도? ")
temper2 = fahrenheit_to_celsius(temper1)
print("화씨", temper1, "도는 섭씨", temper2, "도")"""

# 초 단위의 시간을 입력받아 시 / 분 / 초로 변환
"""
def convert_time(sec) :

    ori_sec = sec

    hours = sec // 3600
    sec %= 3600

    minute = sec // 60
    sec %= 60

    print(ori_sec, "초는", hours, "시간", minute, "분", sec, "초이다.")

def get_integer(time) :
    value = int(input(time))
    return value

second = get_integer("변환하고자 하는 시간(초)? ")
convert_time(second)
"""

# n비트를 모두 1로 설정한 수를 10진수와 2진수로 표현

"""def set_all_bits(N) :
    decimal_value = (2**N-1)
    binary_value = bin(decimal_value)
    return decimal_value, binary_value

def get_integer(bit) :
    value = int(input(bit))
    return value

msg = get_integer("설정할 비트 수는? ")
decimal, binary = set_all_bits(msg)

print(msg, "비트를 모두 1로 설정한 수는", decimal, (binary), "이다.")"""