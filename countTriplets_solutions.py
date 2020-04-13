#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r):
    counts = 0
    double = {}
    single = {}
    for val in reversed(arr):
        if(val*r in double):
            counts += double[val*r]
        if(val*r in single):
            if(val in double):
                double[val] += single[val*r]
            else:
                double[val] = single[val*r]
        if(val in single):
            single[val] += 1
        else:
            single[val] = 1
    print(counts)
    return counts

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    #fptr.write(str(ans) + '\n')

    #fptr.close()
