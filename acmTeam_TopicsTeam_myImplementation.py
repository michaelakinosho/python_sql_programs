#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the acmTeam function below.
def acmTeam(topic, n, m):
	# print(topic)
	# mystr = topic[0]
	# myit = iter(mystr)
	# for n in mystr:
	#     print(n)
	#     print(type(n))

	two_Pteams_list = list()
	tmate_i = list()
	tmate_x = list()

	my_count = 0
	max_topic = 0
	max_num_teams = 0
	y_sum = 0
	z_sum = 0

	i = 0
	while i < n-1:
		x = i + 1
		while x < n:
			#print(i, x)
			j = 0
			tmate_i = topic[i]
			tmate_x = topic[x]

			while j < m:
				if (int(tmate_i[j]) + int(tmate_x[j])) > 0:
					my_count += 1
				j += 1
			two_Pteams_list.append(my_count)
			my_count = 0
			#print(two_Pteams_list)

			x += 1
		i += 1
	#print(two_Pteams_list)

	max_topic = max(two_Pteams_list)
	max_num_teams = two_Pteams_list.count(max(two_Pteams_list))
	print(max_topic, max_num_teams)
	return(max_topic, max_num_teams)



if __name__ == '__main__':
	#fptr = open(os.environ['OUTPUT_PATH'], 'w')

	nm = input().split()

	n = int(nm[0])

	m = int(nm[1])

	topic = []

	for _ in range(n):
		topic_item = input()
		topic.append(topic_item)

	result = acmTeam(topic, n, m)

	#fptr.write('\n'.join(map(str, result)))
	#fptr.write('\n')

	#fptr.close()
