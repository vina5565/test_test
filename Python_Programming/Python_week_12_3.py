import os

def buy(bag) :
    print("[구입]")
    input_buy = input("상품명? ")
    if input_buy == '' :
        return False
    print(f"장바구니에 {input_buy}이(가) 담겼습니다.")
    bag.append(input_buy)

    filename = 'shoppingbag.txt'
    if os.path.exists(filename) :
        with open(filename, 'a', encoding='utf8') as file :
            file.write(f"{input_buy}\n")

def show(bag) :
    print(f">>> 장바구니 보기 : {bag}")

def load() :
    bag = []
    filename = 'shoppingbag.txt'
    if os.path.exists(filename) :
        with open(filename, 'r', emcoding='utf8') as file :
            for line in file :
                bag.append(line.strip('\n'))
        return bag

filename = 'shoppigbag.txt'   
if os.path.exists(filename) :
    print("[파일 읽기]")
    shopping_bag = load(filename)
    show()
else :
    shopping_bag = []

bag_list = []
while True :
    if buy(bag_list) == False :
        break    
show(bag_list)

