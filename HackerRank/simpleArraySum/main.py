#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    #print(min(b))

    int_lst = {min(b)}
    i = 0
    while i < len(b):
        if b[i]%min(b) != 0:
            int_lst.remove(min(b))
            break
        i += 1

    int_lst.add(max(a))
    i = 0
    while i < len(a):
        if a[-1]%a[i] != 0:
            int_lst.remove(max(a))
            break
        i += 1

    i = 0
    a_prod = 1
    while i < len(a):
        a_prod *= a[i]
        i += 1

    if a_prod != 1:
        int_lst.add(a_prod)

    i = 0
    f_num = min(int_lst)
    while f_num < max(int_lst):
        f_num = f_num * (i+1)
        #print(f_num)
        if f_num < max(int_lst):
            int_lst.add(f_num)
        i += 1

    i = len(int_lst)
    print(int_lst)
    print(i)
    return(i)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    #fptr.write(str(total) + '\n')

    #fptr.close()
