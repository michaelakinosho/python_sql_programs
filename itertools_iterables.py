from itertools import permutations
from itertools import combinations

A = input()
s = input().replace(" ","")
a = s.replace("a","")
B = int(input())

#Better solution
x = (len([*combinations(s,B)]))
y = (len([*combinations(a,B)]))
print('{:.3f}'.format((float(x-y))/x))

#alternative solution not as efficient and may sometimes have runtime errors
x = float(len([*permutations(s,B)]))
y = float(len([*permutations(a,B)]))
print('{:.3f}'.format((x-y)/x))
