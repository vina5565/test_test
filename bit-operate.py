"""
연산자	설명
&	비트 AND 연산
`	`
^	비트 XOR 연산
~	비트 NOT 연산
<<	왼쪽 시프트 연산 (비트 이동)
>>	오른쪽 시프트 연산 (비트 이동)

a = 0b1010  # 10 (이진수 1010)
b = 0b1100  # 12 (이진수 1100)

result = a & b  # AND 연산
print(bin(result))  # 출력: 0b1000

a = 0b1010  # 10
b = 0b1100  # 12

result = a | b  # OR 연산
print(bin(result))  # 출력: 0b1110

a = 0b1010  # 10
b = 0b1100  # 12

result = a ^ b  # XOR 연산
print(bin(result))  # 출력: 0b0110

a = 0b1010  # 10

result = ~a  # NOT 연산
print(bin(result))  # 출력: -0b1011

a = 0b1010  # 10

result = a << 2  # 왼쪽으로 2비트 시프트
print(bin(result))  # 출력: 0b101000 # 2배씩 증가하는 효과

a = 0b1010  # 10

result = a >> 2  # 오른쪽으로 2비트 시프트
print(bin(result))  # 출력: 0b10 # 반으로 나누는 효과
"""