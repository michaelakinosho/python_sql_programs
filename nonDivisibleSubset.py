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

def nonDivisibleSubset(k, s):
    # Write your code here
    if k == 1:
        return(1)

    from itertools import combinations

    s = list(set(s))
    #print("Set: ",s)
    max_len = []
    i = len(s)
    while i > -1:
        if len(max_len) >= i:
            return(len(max_len))

        s_subset = combinations(s, i)
        for n in s_subset:
            #print("S_subset:",n)
            s_subset_combos = combinations(n,2)
            for m in s_subset_combos:
                if sum(m)%k != 0:
                    if len(n) > len(max_len):
                        max_len = n
                else:
                    if n == max_len:
                        max_len = []
                        break

                #print("S_subset: ", n, "S_subset_combos:", m, sum(m)%k)

        i -= 1
    print(len(max_len))
    return(len(max_len))

if __name__ == '__main__':
    fptr = open('py_output.txt', 'w')
    py_input = open('py_input.txt','r')

    first_multiple_input = list(map(int, py_input.readline().split(" ")))
    s = list(map(int, py_input.readline().split(" ")))

    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    #s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
