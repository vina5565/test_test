#calc_area.py
#도형의 넓이를 구하는 모듈듈

def get_circle_circum(radius) :
    return 3.14 * 2 * radius
#원의 둘레 구하기

def get_circle_area(radius) :
    return 3.14 * radius ** 2
#원의 넓이 구하기

def get_rect_area(width, height) :
    return width * height
#직사각형 넓이 구하기