# chatgpt 4. 과일 장바구니

class Fruit :
    def __init__(self, name, quantity) :
        self.name = name
        self.quantity = quantity
        
    def is_many(self) :
        return self.quantity >= 3
    
class Bag :
    def __init__(self) :
        self.items = []

    def add_fruit(self, fruit) :
        self.items.append(fruit)

    def show_many(self) :
        print("[출력]")
        for fruit in self.items :
            if fruit.is_many() :
                print(f"{fruit.name} : {fruit.quantity}개")

basket = Bag() 
input_fruit = input("과일 입력 (ex : 사과=2, 바나나=3) :")
entries = input_fruit.split(",")

for entry in entries :
    name, qty = entry.strip().split("=")  # 공백 제거 추가
    fruit = Fruit(name, int(qty))
    basket.add_fruit(fruit)

basket.show_many()


