# chatgpt 5. 식당 주문 시스템

class MenuItem :
    def __init__ (self, name, price) :
        self.name = name
        self.price = price
    
    def calc_price(self, quantity) :
        return self.price * quantity

class Menu :
    def __init__(self) :
        self.items = [] # 이름, 가격을 넣는 배열 생성자

    def add_item(self, item) : # item == 이름과 가격 둘 다 포함하는 형태
        self.items.append(item)

    def get_item(self, name) :
        for item in self.items :
            if item.name == name :
                return item
        return None

    def get_price(self, name) :
        for item in self.items : # 이름 가격이 들어갈 배열의 item을 하나씩 꺼내보자
            if item.name == name : # 인수의 name과 self.items 배열에서 하나씩 꺼낸 item의 이름이 같다면
                return item.price
        return None
        
    def show_menu(self) :
        print("[메뉴판]")
        for item in self.items :
            print(f"{item.name} : {item.price}원")

    def order_process(self, name, quantity) :
        item = self.get_item(name)
        if item is not None :
            return item.calc_price(quantity)
        else :
            return None


menu = Menu() # 빈 메뉴판 생성
menu.add_item(MenuItem("김밥", 3000))
menu.add_item(MenuItem("떡볶이", 4000))
menu.add_item(MenuItem("순대", 3500))
menu.add_item(MenuItem("라면", 3500))
menu.add_item(MenuItem("모둠 튀김", 2500))
menu.add_item(MenuItem("어묵", 2000))
menu.add_item(MenuItem("음료수", 1500))
menu.show_menu()

order_input = input("주문할 메뉴를 골라주세요 (ex. 김밥=1, 떡볶이=2, 어묵=3) : ").replace(" ", "").split(",")
print("[주문 내역]")
total = 0

for order in order_input :
    try :
        name, count = order.split("=")
        count = int(count)
        price = menu.order_process(name, count)
        if price is not None :
            print(f"{name} ({count}개) : {price}원")
            total += price
        else :
            print(f"{order}은(는) 없는 메뉴입니다.")
    except ValueError:
        print(f"입력 오류: '{order}' → 예: 김밥=2")

print(f"총 결제 금액은 {total}원입니다.")