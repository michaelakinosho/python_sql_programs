#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q,n):
    cnt,pos,org = list(range(1,n+1)),list(range(1,n+1)),list(range(1,n+1))
    print(cnt)
    print(pos)
    print(org)

    invalid = 0
    ans = 0
    for i in range(n):
        if invalid:
            break

        oldp = pos[q[i]]
        print("oldp: ",oldp, "arr[i]: ", q[i])

        newp = i + 1

        while oldp != newp:

            ans += 1

            cnt[org[oldp+1]] += 1

            if cnt[org[oldp + 1]] > 2:
                invalid = 1
                break

            org[oldp],org[oldp+1] = org[oldp+1],org[oldp]

            pos[org[oldp]] = oldp
            pos[org[oldp+1]] = oldp + 1
            print("oldp: ", oldp, "newp: ", newp)
            oldp += 1

    if invalid:
        ans = "Too chaotic"

    print(ans)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q,n)
