#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the countTriplets function below.
def countTriplets(arr, r):
    temp_counter = 0
    max_count = 0
    total_count = 0

    cnt = Counter()
    for num in arr:
        if num == 1:
            cnt[num] += 1
        elif num%r == 0:
            cnt[num] += 1

    print(cnt)
    list_cnt = list(cnt.items())
    if len(cnt) == 1:

    elif len(cnt) == 2:

    elif len(cnt) > 2:
    i = 0
    while i < len(list_cnt)-2:
        max_count += max(cnt.get(list_cnt[i][0]),cnt.get(list_cnt[i+1][0]),cnt.get(list_cnt[i+2][0]))
        i += 1
    return(max_count)
    # print(list_cnt)
    #
    # for i in list_cnt:
    #     temp_count = 0
    #     max_count = 0
    #     j = i[0]
    #     while j < len(list_cnt):
    #         print(j)
    #         print(cnt.get(j))
    #         if pow(r,j) in cnt.keys():
    #             temp_counter +=1
    #             if max_count < cnt.get(j):
    #                 max_count = cnt.get(j)
    #             if temp_counter == 3:
    #                 total_count += max_count
    #                 break
    #
    #         j += 1
    # print(total_count)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)
    print(ans)

    #fptr.write(str(ans) + '\n')

    #fptr.close()
