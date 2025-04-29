# 쇼핑몰 장바구니 시뮬레이션 

shopping_bag = {} # 장바구니 딕셔너리

print("[구입]")
while True :
    item = input("상품명? ")
    if item == "" :
        break
    pcs = input("수량은? ")
    shopping_bag[item] = pcs
    print(f"장바구니에 {item}이(가) {pcs}개 담겼습니다.")


print(f">>> 장바구니 보기 : {shopping_bag}")

print("[검색]")
search = input("장바구니에서 확인하고자 하는 상품은? ")
key = shopping_bag.get(search)
print(f"{search}(은)는 {key}개 담겨 있습니다.")