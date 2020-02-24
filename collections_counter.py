from collections import *

X = int(input())
N = Counter(list(map(int,input().split(" "))))
N = dict(N)
#print(N)
earnings = 0
xi = int(input())
for _ in range(0,xi):
    s = list(map(int,input().split(" ")))
    temp = N.get(s[0])
    if temp != None and temp > 0:
        earnings += s[1]
        N.update({s[0]:temp-1})
        #print(N.get(s[0]))
print(earnings)
