#16. 입력으로 들어오는 모든 수의 평균값을 계산해 주는 함수를 작성해 보자.
#    (단, 입력으로 들어오는 수의 갯수는 정해져 있지 않다.)

def avg(*args):
    result = 0
    for i in args:
        result += i
    return result / len(args)

print(avg(1,3))
