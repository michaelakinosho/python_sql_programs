#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    ar_set = {}
    #print(ar)
    #print(ar_set)
    counter = 0

    i = 0
    while i < len(ar):
        j = 0
        while j < len(ar):

            if i < j and (ar[i]+ar[j])%k == 0:
                #print(i,",",j, ar[i]+ar[j])
                counter += 1
            j += 1
        i += 1
    print(counter)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    #fptr.write(str(result) + '\n')

    #fptr.close()
