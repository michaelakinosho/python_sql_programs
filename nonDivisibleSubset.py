#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s, i):
    # Write your code here

    #s.sort()
    my_list = list()
    j = 0
    print(s)
    while j < i+ 1:
        my_list.append(s[j])
        j += 1

    j = i + 1
    while j < len(s):
        if (s[i]+s[j])%k != 0:
            my_list.append(s[j])
        j += 1

    return(k,my_list,i)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    i = 0

    ans = nonDivisibleSubset(k, s, i)
    while i < len(ans[1]):
        print(ans[1])
        ans = nonDivisibleSubset(k,ans[1],i)
        i += 1
    print(ans)
    #print(result)

    #fptr.write(str(result) + '\n')
    #fptr.close()
