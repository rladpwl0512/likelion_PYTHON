# 19.	문자열을 입력 받아 같은 문자가 연속적으로 반복되는 경우에 그 반복 횟수를 표시하여 문자열을 압축하여 표시해 보자.
#       입력 예시: aaabbcccccca
#       출력 예시: a3b2c6a1

message = input("문자열를 입력하세요.")

result = message[0]  
count  = 0

for st in message:
    if st == result[-1]:
        count += 1
    else:
        result += str(count) + st
        count = 1
result += str(count)

print(result)