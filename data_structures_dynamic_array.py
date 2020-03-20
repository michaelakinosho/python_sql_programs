#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    lastAnswer = 0
    seqList = [[] for j in range(n)]

    for q in queries:
        #print(q)
        seq = (q[1]^lastAnswer)%n
        if q[0] == 1:
            #print(seq)
            #print(q[2])
            seqList[seq].append(q[2])
            #print(seqList)
        else:
            lastAnswer = seqList[seq][(q[2]%len(seqList[seq]))]
            print(lastAnswer)

    #print(seqList)
    return 0
    # Write your code here

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    #fptr.write('\n'.join(map(str, result)))
    #fptr.write('\n')

    #fptr.close()
