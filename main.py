#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
#s is array of n integers
#d is the day of birthday
#m is the month of birthday
#m is number of elements that must equal d
def birthday(s, d, m):
    i = 0
    i_sum = 0
    i_count = 0

    while i < len(s):
        j = 0
        temp_i = i
        i_sum = 0
        while j < m:
            i_sum += s[temp_i]
            temp_i += 1
            j += 1
        if i_sum == d:
            i_count += 1
        i += 1
    return(i_count)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    #fptr.write(str(result) + '\n')

    #fptr.close()
