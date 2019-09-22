#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
	sticks_count = list()
	arr_temp = list()
	while len(arr) > 0:

		sticks_count.append(len(arr))
		min_stick = min(arr)

		x = 0
		while x < len(arr):
			arr[x] -= min_stick
			x += 1

		x = 0
		y = len(arr)
		while x < y:
			if arr[x] > 0:
				arr_temp.append(arr[x])
			x += 1

		arr = arr_temp
		arr_temp = list()

	#print(sticks_count)
	return(sticks_count)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    #fptr.write('\n'.join(map(str, result)))
    #fptr.write('\n')

    #fptr.close()
