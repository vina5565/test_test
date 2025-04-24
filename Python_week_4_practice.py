import exchange_currency as EC

rate = int(input("$1에 대한 오늘의 환율은? "))
EC.set_rate(rate) # 사용자에게 환율을 입력받아 set.rate의 parameter에 입력

dollar = int(input("원화로 환전할 달러의 액수는 ? "))
print(dollar, "달러는", EC.to_won(dollar), "원입니다.")

won = int(input("달러로 환전할 원의 액수는 ? "))
print(won, "원은", EC.to_dollar(won), "달러입니다.")