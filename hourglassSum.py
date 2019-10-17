#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    sum_list = []
    hour_sum = 0
    i = 0
    while i < len(arr)-2:
        j = 0
        while j < len(arr[i])-2:
            hour_sum = arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
            sum_list.append(hour_sum)

            j += 1
        i += 1
    print(max(sum_list))
    return(max(sum_list))

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    #fptr.write(str(result) + '\n')

    #fptr.close()
