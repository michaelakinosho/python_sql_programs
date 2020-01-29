#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    s_list = list(s.split(" "))
    print(s_list)
    x = 0
    while x < len(s_list):
        s_list[x] = s_list[x].capitalize()

        x += 1


    return(" ".join(s_list))

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)
    print(result)

    #fptr.write(result + '\n')

    #fptr.close()
