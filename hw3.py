def get_discount() :
    discount = int(input("할인율은 ? ")) * 0.01
    return discount
 
 
def get_fixed_price(discount, product) :
    price = int(input(f"{product} 상품의 할인된 가격은? "))
    fixed_price = price * (1 / (1 - discount))
 
    return round(fixed_price)
 
discount = get_discount()
 
result1 = get_fixed_price(discount, "A")
result2 = get_fixed_price(discount, "B")
 
print(f"A 상품의 정가는 {result1}원입니다.")
print(f"B 상품의 정가는 {result2}원입니다.")