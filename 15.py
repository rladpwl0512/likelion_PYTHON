# 15. for문을 이용하여 A 학급의 평균 점수를 구해 보자.
#     A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]

A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]

sum = 0
for i in range(len(A)):
    sum += A[i]

avg = sum / len(A)
print(avg)
