#Solution from discussion board
# for t in range(int(input())):
#     input()
#     lst = list(map(int, input().split()))
#     l = len(lst)
#     i = 0
#     while i < l - 1 and lst[i] >= lst[i+1]:
#         print(lst[i])
#         i += 1
#     while i < l - 1 and lst[i] <= lst[i+1]:
#         print(lst[i])
#         i += 1
#     print ("Yes" if i == l - 1 else "No")

#Working on my own solution based on Deque
from collections import deque
for t in range(int(input())):
    icount = int(input())
    d = deque(list(map(int, input().split())))
    new_d = deque()
    i = 0
    while i < icount-1:
        if d[i] >= d[-1]:
            if d[i] >= d[i+1]:
                #print(i, d[i])
                new_d.append(d[i])
        else:
            if d[icount-1] >= d[icount-2]:
                #print(i, d[-1+i])
                new_d.append(d[-1+i])
        i += 1
    print("Yes" if len(new_d)+1 == len(d) else "No")
