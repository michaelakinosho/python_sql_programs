#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    my_lst = [0] * (n+1)

    for n in (queries):
        for i in range(n[0],n[1]+1):
            my_lst[i] += n[2]
            #print(i)

    print(my_lst)
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
