#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    a_counter = 0
    s_set = set(s)
    if 'a' not in s_set:
        a_counter = 0

    else:
        if len(s) == 1:
            a_counter = n
        else:
            i = int(n/len(s))
            a_counter = i * s.count('a')

            a_counter += s[0:n%len(s)].count('a')
    print(a_counter)
    return(a_counter)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    #fptr.write(str(result) + '\n')

    #fptr.close()
