def get_radius(prompt) :
    r = int(input(prompt))
    return r

def get_circle_area(r) :
    area = r * r * 3.14
    return area

input_radius = get_radius("넓이를 구하고자 하는 원의 반지름은? ")
result = get_circle_area(input_radius)
print(f"반지름이 {input_radius}인 원의 넓이 = {input_radius} * {input_radius} * 3.14 = {result}")