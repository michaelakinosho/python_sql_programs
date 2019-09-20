#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the timeInWords function below.
def timeInWords(h, m):
	every15 = {0:"o' clock", 15:"quarter past", 30:"half past", 45:"quarter to"}
	upto19 = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen"}
	from20up = {20:"twenty", 30:"thirty", 40:"forty", 50:"fifty"}

	m_str = ""
	h_str = ""

	m_int = int(m)
	h_int = int(h)

	if m_int > 30:
		if h_int == 12:
			h_int = 1
		else:
			h_int += 1


	if m_int in every15:
		m_str = every15.get(m_int)
	else:
		if m_int > 30:
			m_int = 60 - m_int
			m_str = "twenty " + str(upto19.get(int(m_int%10))) + " minutes to"
		else:
			m_str = "twenty " + str(upto19.get(int(m_int%10))) + " minutes to"


	elif m_int > 19:
		m_str = str(from20up.get(int(m_int/10)*10)) + " " + str(upto19.get(int(m_int%10))) + " minutes"
	else:
		m_str = upto19.get(m_int)

	#if m > 30:
	#	h += 1
	print(m_str)


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    #fptr.write(result + '\n')

    #fptr.close()
