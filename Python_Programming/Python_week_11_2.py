class Point :

    def __init__(self, x = 0, y = 0) :
        self.__x = x
        self.__y = y

    def show(self) :
        print(f"{self.__x}, {self.__y}")
        
    def setPoint(self, x, y) :
        self.__x = x
        self.__y = y

    def getPoint(self) :
        return (self.__x, self.__y)
        

def test() :
    p1 = Point()
    p2 = Point(2, 3)
    p1.show();
    p1.setPoint(10, 20); p1.show();
    p2.show();
    x, y = p2.getPoint()
    print(f'x={x}, y={y}')

# 주 프로그램부
if __name__ == '__main__':
    test()

class Time :
    def __init__(self, h = 0, m = 0) :
        self.__h = h
        self.__m = m

    def display(self) :
        print(f"{self.__h:02d}:{self.__m:02d}")

    def add(self, other) : 
        new_h = self.__h + other.__h
        new_m = self.__m + other.__m

        if new_m >= 60 :
            new_h += new_m // 60
            new_m %= 60
        
        return Time(new_h, new_m) # 새로운 객체 생성
        
    @staticmethod
    def isvalid(h, m) :
        return 0 <= h < 24 and 0 <= m <60
    # 정적메서드는 객체(self)와 무관하게 동작
    
def main():
    t1 = Time(9)
    t2 = Time(9, 30)
    t1.display()
    t2.display()
    later = t1.add(Time(1, 15))
    later.display()
    if Time.isvalid(25, 0):
        print('유효한 시각')
    else:
        print('유효하지 않은 시각')

# 주 프로그램부
if __name__ == '__main__':
    main()
