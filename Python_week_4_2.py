import dice

dice_num = dice.roll_dice()
print("주사위 2번 던지기 :", end = ' ')
for num in dice_num :
    print(num, end = ' ')
print()

lotto_num = dice.run_lotto()
print("로또 번호 6개 : ")
for num in lotto_num :
    print(num, end = ' ')