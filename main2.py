#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(n, c):
    jumps_counter = 0
    i = 0
    while i < n-2:
        if c[i + 2] == 0:
            jumps_counter += 1
            i += 2
        elif c[i + 1] == 0:
            jumps_counter += 1
            i += 1
        else:
            i += 1
    if i < n - 1:
        jumps_counter += 1

    #print(i)
    print(jumps_counter)
    return(jumps_counter)



if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(n, c)

    #fptr.write(str(result) + '\n')

    #fptr.close()
