from math import *
AB = int(input())
BC = int(input())

x = atan(AB/BC)

x = round(degrees(x),0)
x = str(int(x)) + u"\u00b0"
print(x)
