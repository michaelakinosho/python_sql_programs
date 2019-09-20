#!/bin/python3

import os
import sys

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
	ttl = 0
	for i in ar:
		ttl += i
	return ttl


if __name__ == '__main__':
    fptr = open('C:\\Users\\Michael Akinosho\\github\\Capstone-Project-Ideas\\HackerRank\\simpleArraySum.txt', 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
