from collections import *

X = int(input())
N = Counter(list(map(int,input().split(" "))))
N = dict(N)
print(N)
xi = int(input())
for _ in range(0,xi):
    s = list(map(int,input().split(" ")))
