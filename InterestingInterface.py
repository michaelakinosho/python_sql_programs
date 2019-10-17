class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        if n == 1:
            return(1)

        runningSum = 1 + n
        i = 2
        while i < n:
            if n%i == 0:
                runningSum += i
            i += 1
        return(runningSum)

n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)
