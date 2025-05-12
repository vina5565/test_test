def buy(bag) :

    print("[구입]")
    item = input("상품명 ? ")
    if item == "" :
        return False
    amount = input("수량 ? ")
    print(f"장바구니에 {item} {amount}개가 담겼습니다.")
    bag[item] = amount


def show(bag) :

    print(f"장바구니 보기 : {bag}")

def find(bag) :
    
    print("[검색]")
    find_item = input("장바구니에서 확인하고자 하는 상품은 ? ")
    if find_item in bag :
        print(f"{find_item}은(는) {bag[find_item]}개 담겨있습니다.")
    else :
        print(f"장바구니에 {find_item}은(는) 없습니다.")

shopping_bag = {}
while True :
    if buy(shopping_bag) == False :
        break
show(shopping_bag)
find(shopping_bag)