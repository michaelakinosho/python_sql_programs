#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    L = len(s)
    xr1 = round(L**0.5,1)
    xr0 = round(xr1)

    if xr1 == xr0:
        row = xr0
        col = row
    elif xr1 > xr0:
        row = xr0
        col = row + 1
    else:
        col = xr0
        row = col - 1

    t = ""
    i = 0
    while i < col:
        j = 0
        while i + (col*j) < L:
            idx = i + (col*j)
            t += str((s[idx]))
            j += 1
        t += " "
        i += 1
    #print(t)
    return(t)

if __name__ == '__main__':
    py_input = open('py_input.txt')
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = py_input.readline().rstrip()
    #s = input()

    result = encryption(s)
    print(result)

    #fptr.write(result + '\n')

    #fptr.close()
