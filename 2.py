#2. 임의의 자연수를 입력하면 홀수인지 짝수인지 판별하세요. (if문 사용)

x = int(input("자연수를 입력하세요."))

if(x % 2 == 0):
    print("짝수")
else:
    print("홀수")