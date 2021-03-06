#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    max_num = 0

    for y in queries:
        max_num += y[2]

    my_lst = [0] * (n+1)

    for y in queries:
        for i in range(y[0],y[1]+1):
            my_lst[i] += y[2]
            #print(i)

    #print(my_lst)
    return(max(my_lst))

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
