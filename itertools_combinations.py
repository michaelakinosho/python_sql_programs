from itertools import combinations

A,B = input().split(" ")
A = list(A)
A.sort()
B = int(B)
for y in range(1,B+1):
    for x in combinations(A,y):
        print("".join(x))
