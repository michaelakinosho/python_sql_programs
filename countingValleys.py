#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    runningSum = 0
    mountain = 0
    valley = 0
    steps_list = []
    print(s)

    i = 0
    while i < n:
        if len(steps_list) < 1:
            steps_list.append(s[i])
        elif s[i] == steps_list[-1]:
            steps_list.append(s[i])
        else:
            if len(steps_list) == 1:
                if s[i] == 'U':
                    valley += 1
                else:
                    mountain += 1
            steps_list.pop()


        i += 1
    print(mountain)
    print(valley)
    return(valley)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    #fptr.write(str(result) + '\n')

    #fptr.close()
