#11. 1부터 1000까지의 자연수 중 3의 배수의 합을 구하세요.

total = 0
for n in range(1, 1001):
    if(n % 3 == 0):
        total += n
print(total)