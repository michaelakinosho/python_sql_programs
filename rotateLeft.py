#!/bin/python3

import math
import os
import random
import re
import sys
import copy

# Complete the rotLeft function below.
def rotLeft(a, d):
    a_copy = copy.deepcopy(a)
    a_len = len(a)
    i = 0
    while i < a_len:
        j = i - d
        if j >= 0:
            a_copy[j] = a[i]
        else:
            j *= -1
            j = a_len - (j%a_len)
            a_copy[j] = a[i]

        i += 1
    return(a_copy)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    #fptr.write(' '.join(map(str, result)))
    #fptr.write('\n')

    #fptr.close()
