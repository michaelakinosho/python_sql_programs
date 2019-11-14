#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    my_lst = [0] * (n+1)

    for x in range(1,n+1):
        for y in queries:
            for z in range(y[0],y[1]+1):
                print(z, y[2])
            #print(y)
        #print(x)


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
