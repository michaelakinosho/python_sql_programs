#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    countSwaps = 0
    n = len(arr)
    #print(arr)

    for i in range(n-1,-1,-1):
        #print("i: ", i, "arr[i]: ", arr[i], "arr.index(i+1): ",arr.index(i+1) )
        if i != arr.index(i+1):
            arr[arr.index(i+1)] = arr[i]
            #arr[arr.index(i+1)],arr[i] = arr[i],arr[arr.index(i+1)]
            countSwaps += 1
        #print(arr)
    print(countSwaps)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    #fptr.write(str(res) + '\n')

    #fptr.close()
