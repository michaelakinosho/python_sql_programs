#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the chocolateFeast function below.
def chocolateFeast(n, c, m):

	candy_count = int(n/c)
	n = candy_count
	while n >= m:
		candy_count += int(n/m)
		n = int(n/m) + int(n%m)
	#print(candy_count)
	return(candy_count)

def chocoRecursive(num_wrap, wraps_per_candy, candy_count):
	candy_count += int(num_wrap/wraps_per_candy)
	num_wrap = int(num_wrap/wraps_per_candy) + int(num_wrap%wraps_per_candy)
	#print(candy_count)
	#print(num_wrap)
	if num_wrap >= wraps_per_candy:
		chocoRecursive(num_wrap, wraps_per_candy,candy_count)
	if num_wrap == wraps_per_candy:
		candy_count += 1

	return(candy_count)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        ncm = input().split()

        n = int(ncm[0])

        c = int(ncm[1])

        m = int(ncm[2])

        result = chocolateFeast(n, c, m)

        #fptr.write(str(result) + '\n')

    #fptr.close()
