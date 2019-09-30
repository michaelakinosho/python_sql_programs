#!/bin/python3

import math
import os
import random
import re
import sys
import time

# Complete the matrixRotation function below.
def matrixRotation(matrix, m, n, r):
    num_of_rings = min(m,n)/2
    matrix_string = ""
    new_m = 0
    new_n = 0
    new_m2 = 0
    #num_of_poses_ring = (max(m,n)*2) + ((min(m,n)-2)*2)

    i,j = 0,0
    x = 0
    while x < num_of_rings:

        z = 0
        while z < r:
            q = 0
            i, j = x,x
            num_of_poses_ring = (max(m,n)*2) + ((min(m,n)-2)*2)
            cur_value = matrix[i][j]
            while q < num_of_poses_ring:

                if (q) < (m-1):
                    i += 1
                elif (q) < (m-1+n-1):
                    j += 1
                elif (q) < (m-1+n-1+m-1):
                    i -= 1
                else:
                    j -= 1

                #print("In ring: {}, rotation: {}, future position is {},{} of value {}, position counter: {}".format(x,z,i,j,cur_value,q+1))
                next_value = matrix[i][j]
                matrix[i][j] = cur_value
                cur_value = next_value

                q += 1

            z += 1
        m -= 2
        n -= 2
        x += 1

    #print(matrix)
    #print(i, j)

    i = 0
    while i < len(matrix):
        j = 0
        matrix_string = ""
        while j < len(matrix[i]):
            matrix_string += (str(matrix[i][j]) + " ")
            j += 1
        print(matrix_string)
        i += 1

if __name__ == '__main__':
    mnr = input().rstrip().split()

    m = int(mnr[0])

    n = int(mnr[1])

    r = int(mnr[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, m, n, r)
