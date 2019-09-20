#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores, n):
	#print(scores)
	i = 0
	max_score = scores[i]
	min_score = scores[i]
	scores_list = []
	records_list = []
	max_set = set()
	min_set = set()
	while i < n:
		if i == 0:
			scores_list.append([i, scores[i],max_score,min_score])
		else:
			max_score = scores[i] if scores[i] > max_score else max_score
			min_score = scores[i] if scores[i] < min_score else min_score
			scores_list.append([i,scores[i],max_score,min_score])
			max_set.add(max_score) if max_score != scores[0] else max_set.add("-")
			min_set.add(min_score) if min_score != scores[0] else min_set.add("-")
		i += 1

		max_set.discard("-")
		min_set.discard("-")

	#print(scores_list)
	records_list.append(len(max_set))
	records_list.append(len(min_set))
	#print(records_list)
	return("{} {}".format(len(max_set), len(min_set)))


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores, n)

    #fptr.write(' '.join(map(str, result)))
    #fptr.write('\n')

    #fptr.close()
