#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    a.sort()
    counter_max = 0
    counter_cur = 0

    i = 0
    while i < len(a):
        j = 0
        counter_cur = 0
        while j < len(a):
            if a[i]-a[j] == 0 or a[i]-a[j] == -1:
                counter_cur += 1
            j += 1
            if counter_cur > counter_max:
                counter_max = counter_cur
        i += 1

    #print("This is counter max:",counter_max)

    #print(a)
    return(counter_max)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)
    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()
