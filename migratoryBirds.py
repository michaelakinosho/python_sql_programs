#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    bird_count = 0
    max_count = 0
    for n in range(1,6):
        bird_count = arr.count(n)
        if bird_count > max_count:
            max_count = bird_count
            num = n
    return num

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)
    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()
