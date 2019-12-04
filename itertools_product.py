from itertools import product

A = [int(x) for x in input().split(" ")]
B = [int(y) for y in input().split(" ")]

print(*product(A,B))
