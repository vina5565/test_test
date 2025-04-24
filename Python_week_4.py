from calc_area import get_circle_area as getCA
from calc_area import get_circle_circum as getCC
from calc_area import get_rect_area as getRA

r = 10
w, h = 6, 4

print(f"원의 둘레 : {getCC(r):.1f}")
print(f"원의 넓이 : {getCA(r):.1f}")
print(f"직사각형의 넓이 : {getRA(w, h)}")