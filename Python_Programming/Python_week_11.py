class Circle :

    __PI = 3.141592

    # 생성자
    def __init__(self, radius) :
        self.__radius = radius

    def get_circum_ference(self) :
        result = 2 * Circle.__PI  * self.__radius
        return result
    
    def get_area (self) :
        result = Circle.__PI  * self.__radius ** 2
        return result
    
    def setRadius(self, radius) :
        self.__radius = radius

    def getRadius(self) :
        return self.__radius
    
#객체 생성
small = Circle(1)
big = Circle(10)

#결과 출력
print(f"반지름 {small.getRadius()}인 원의 ", end = ' ')
print(f"둘레는 {small.get_circum_ference():.2f}이고 ", end = ' ')
print(f"넓이는 {small.get_area():.2f}이다.")

print(f"반지름 {big.getRadius()}인 원의 ", end = ' ')
print(f"둘레는 {big.get_circum_ference():.2f}이고 ", end = ' ')
print(f"넓이는 {big.get_area():.2f}이다.")

big.setRadius(100)
print(big.getRadius())