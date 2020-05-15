# 18. 이번에 여러분이 작성해야 하는 클래스는 MaxLimitCalculator 클래스이다. 
#     MaxLimitCalculator 클래스는 객체변수 value가 100이상의 값은 가질 수 없도록 제한하는 클래스이다. 
#     즉, 다음과 같이 동작해야 한다.

class Calculator:
    def __init__(self):
        self.value = 0
    def add(self, val):
        self.value += val

class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val 
        if self.value > 100:
            self.value = 100
            return self.value
        else:
            return self.value

cal = MaxLimitCalculator()
cal.add(50) #50더하기
cal.add(60) #60더하기

print(cal.value) 