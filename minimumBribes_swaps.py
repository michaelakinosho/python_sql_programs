#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q,n):
    cnt,pos,org = list([0]*(n+1)),list(range(n+1)),list(range(n+1))

    invalid = 0
    ans = 0
    for i in range(n-1,-1,-1):

        print("Top of For Loop:")
        print(cnt)
        print(pos)
        print(org)
        print("Middle of For Loop:")

        if invalid:
            break

        #Here we pass the queue, starting from the back position n-1
        oldp = pos[q[i]]
        print("oldp: ",oldp, "arr[i]: ", q[i])

        #Since we starting from the back (right side)
        #i will always be decreasing
        newp = i + 1
        print("newp: ",newp)

        while oldp != newp:

            ans += 1
            print("oldp: ",oldp)
            print("oldp+1", oldp+1)
            #print("org[oldp+1]: ",org[oldp+1])
            #print("cnt[org[oldp+1]]: ",cnt[org[oldp+1]])
            cnt[org[oldp+1]] += 1

            if cnt[org[oldp + 1]] > 2:
                invalid = 1
                break

            print("[oldp]: ", org[oldp], "org[oldp+1]: ", org[oldp+1], " = ", "org[oldp+1]: ", org[oldp+1],"[oldp]: ", org[oldp])
            org[oldp],org[oldp+1] = org[oldp+1],org[oldp]

            pos[org[oldp]] = oldp
            pos[org[oldp+1]] = oldp + 1
            print("oldp: ", oldp, "newp: ", newp)

            print(cnt)
            print(pos)
            print(org)
            print("Bottom of For Loop:\n")

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
