#!/bin/python3

import math
import os
import random
import re
import sys
import copy
import time

# Complete the matrixRotation function below.
def matrixRotation(matrix, m, n, r):
    num_of_rings = min(m,n)/2
    matrix_string = ""
    new_m = 0
    new_n = 0
    new_m2 = 0
    matrix_copy = copy.deepcopy(matrix)
    #num_of_poses_ring = (max(m,n)*2) + ((min(m,n)-2)*2)

    i,j = 0,0
    i_copy, j_copy, q_copy = 0,0,0
    x = 0
    while x < num_of_rings:
        num_of_poses_ring = (max(m,n)*2) + ((min(m,n)-2)*2)
        i, j = x,x
        cur_value = matrix[i][j]
        q = 0
        while q < num_of_poses_ring:
            q_copy = ((q+r)%num_of_poses_ring)-1

            if q_copy < m-1:
                i_copy = i + r
                j_copy = 0
            elif q_copy < m - 1 + n - 1:
                i_copy = m - 1
                j_copy = j + r
            elif q_copy < m-1+n-1+m-1:
                i_copy = i + r - (n -1)
                j_copy = n - 1
            else:
                i_copy = 0
                j_copy = q_copy-m-n+2

            print("i is: ", i, "i_copy is: ", i_copy, "j is: ", j, "j_copy is: ", j_copy, "q is: ", q, "q_copy is: ", q_copy)
            matrix_copy[i_copy][j_copy] = cur_value

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

            cur_value = next_value

            q += 1

        m -= 2
        n -= 2
        x += 1

    print(matrix)
    print(matrix_copy)
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
