from itertools import combinations_with_replacement

A,B = input().split(" ")
A = list(A)
A.sort()
B = int(B)
#print(A)
#print(B)
#lst = [(*permutations(A,B))]
#print(lst)
y = ""
for x in combinations_with_replacement(A,B):
    #print(type(x))
    print(tuple(''.join(x)))

print(" ")
#Alternate implementation
A,B = input().split()
print(*(tuple(''.join(i)) for i in combinations_with_replacement(sorted(A),int(B))),sep = " ")
