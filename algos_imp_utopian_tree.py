#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(n):
    H = 1

    for i in range(0,n):
        #print(i, i%2, H)
        if i%2 == 0:
            H = H*2
        else:
            H += 1
    return(H)

if __name__ == '__main__':
    py_input = open('py_input.txt')
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(py_input.readline())
    #t = int(input())

    for t_itr in range(t):
        n = int(py_input.readline())
        #n = int(input())

        result = utopianTree(n)
        print(result)

        #fptr.write(str(result) + '\n')

    #fptr.close()
