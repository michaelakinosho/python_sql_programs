#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    counter_cur = 0
    counter_max = 0
    queries.sort()

    max_num = 0
    for y in queries:
        max_num += y[2]
    print(max_num)

    for n in range(1,n+1):
        for x in queries:
            if n >= x[0] and n <= x[1]:
                counter_cur += x[2]
        if counter_cur >= max_num:
            return(counter_cur)
        if counter_cur > counter_max:
            counter_max = counter_cur
        counter_cur = 0

            #print(y)
        #print(x)
    return(counter_max)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)
    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()
