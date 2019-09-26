#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the matrixRotation function below.
def matrixRotation(matrix, r, m, n):
    num_rings = min(m,n)/2
    beg_pos_tuple = (-1,-1)

    x = 0
    while x < num_rings:
        print("matrix ring: {}".format(x) )
        y = 0
        while y < r:
            print("matrix ring: {}, rotation: {}".format(x, y))
            i = 0 + y
            j = 0 + y
            beg_pos_tuple = tuple(i, j)
            matrix[i][j]


            y += 1


        x += 1

if __name__ == '__main__':
    mnr = input().rstrip().split()

    m = int(mnr[0])

    n = int(mnr[1])

    r = int(mnr[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r, m, n)
