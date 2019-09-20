#!/bin/python3

import math
import os
import random
import re
import sys
from decimal import *

# Complete the plusMinus function below.
def plusMinus(arr, n):
    dec_limit = 10
    my_list = []
    my_list_count = []
    i = 0
    arr_elem = 0

    while i < n:
        arr_elem = arr[i]    
        if arr_elem not in my_list:
            my_list.append(arr_elem)
            my_list_count.append(1)
        else:
            i_elem = my_list.index(arr_elm)
            my_list_count.insert(my_list_count[i_elem]+1, i_elem) 

        i += 1


if __name__ == '__main__':
    n = int(input("Number of integers"))

    arr = list(map(int, input("Enter each integer separated by space").rstrip().split()))

    plusMinus(arr, n)
