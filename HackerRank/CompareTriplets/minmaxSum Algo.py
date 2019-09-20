#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    int_list = []
    i = 0
    int_list.append(arr[i])
    #print(arr)
    i = 1
    while i < len(arr):
        if arr[i] >= int_list[-1]:
            #print("Inside if: {}".format(arr[i]))
            int_list.append(arr[i])
        elif arr[i] <= int_list[0]:
            #print("elif: {}".format(arr[i]))
            int_list.insert(0, arr[i])
        else:
            j = 0
            while j < len(int_list):
                if arr[i] > int_list[j] and arr[i] < int_list[j+1]:
                    int_list.insert(j+1, arr[i])
                j += 1
        i += 1

    print(int_list)

    i = 0
    min_val = 0
    while i < len(int_list) - 1:
        min_val += int_list[i]
        i += 1

    i = 1
    max_val = 0
    while i < len(int_list):
        max_val += int_list[i]
        i += 1

    print("{} {}".format(min_val, max_val))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
