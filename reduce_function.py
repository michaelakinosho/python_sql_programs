from fractions import Fraction
from functools import reduce

def product(fracs):
    #print(fracs)
    #print(fracs[0]*fracs[1])
    t = reduce(lambda x,y:x*y, fracs)
    #print("answer:",m)
    #print(m.numerator, m.denominator)
    return(t.numerator, t.denominator)

    #t = # complete this line with a reduce statement
    #return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)
