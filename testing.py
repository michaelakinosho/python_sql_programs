from itertools import permutations
from itertools import combinations

A = input()
s = input().replace(" ","")
a = s.replace("a","")
B = int(input())

#print(A, B)
x = (len([*permutations(s,B)]))
y = (len([*permutations(a,B)]))
print(x,y)
print('{:.12f}'.format((float(x-y))/x))

x = (len([*combinations(s,B)]))
y = (len([*combinations(a,B)]))
print(x,y)
print('{:.12f}'.format((float(x-y))/x))


#print(float((len([*permutations(a,B)])-len([*permutations(a,B)]))/len([*permutations(s,B)])))
#1) Do regular permutations
#2) Do permutation but replace any characters that are 'a' with ''
#Divide 2) by 1)
