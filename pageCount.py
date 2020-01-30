#!/bin/python3

import os
import sys
from decimal import *

#
# Complete the pageCount function below.
#
def pageCount(n, p):

    if n%2 != 0:
        n = n - 1

    if p%2 != 0:
        p = p - 1

    y = (p)/2

    if (n-p)/2 < y:
        y = (n-p)/2

    #print(y)

    return int(round(y,0))

    #
    # Write your code here.
    #

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)
    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()
