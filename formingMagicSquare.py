#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):

    rep_cost = 0
    evens = [2,4,6,8]
    odds = [1,3,7,9]
    print(sum(s[0]))
    print(s)

    if s[1][1] != 5:
        rep_cost = abs(s[1][1] - 5)

    i = 0
    while i < len(s):
        while j < len(s[i]):
            if s[i][j] != evens:


            j += 2

        i += 2

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)
    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()
