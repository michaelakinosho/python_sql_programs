#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    #
    i = 0
    j = len(drives)-1
    if min(keyboards) >= b or min(drives) >= b:
        return(-1)
    else:
        b_max = 0
        while i < len(keyboards):
            j = len(drives)-1
            while j > -1:
                if keyboards[i]+drives[j] > b_max and keyboards[i] + drives[j] <= b:
                    b_max = keyboards[i] + drives[j]
                if b_max == b:
                    return(b)

                j -= 1
            i += 1
    if b_max <= b and b_max != 0:
        return(b_max)
    else:
        return(-1)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = sorted(list(set(map(int, input().split(" ")))))
    #print(keyboards)

    drives = sorted(list(set(map(int, input().split(" ")))))
    #print(drives)

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)
    print(moneySpent)

    #fptr.write(str(moneySpent) + '\n')

    #fptr.close()
