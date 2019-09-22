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
	time_str = ""

	m_plu = "minute"

	m_int = int(m)
	h_int = int(h)

	if m_int > 30:
		if h_int == 12:
			h_int = 1
		else:
			h_int += 1
	h_str = upto19.get(h_int)

	if m_int in every15:
		m_str = every15.get(m_int)
	else:
		if m_int > 30:
			m_int = 60 - m_int
			m_plu = m_plu + "s" if m_int > 1 else m_plu
			if m_int > 20:
				m_str = "twenty " + str(upto19.get(int(m_int%10))) + " " + m_plu + " to"
			else:
				m_str = str(upto19.get(m_int)) + " " + m_plu + " to"
		else:
			m_plu = m_plu + "s" if m_int > 1 else m_plu
			if m_int > 20:
				m_str = "twenty " + str(upto19.get(int(m_int%10))) + " " + m_plu + " past"
			else:
				m_str = str(upto19.get(m_int)) + " " + m_plu + " past"
	#print(type(m))
	if m == 00:
		time_str = h_str + " " + m_str
	else:
		time_str = m_str + " " + h_str
	print(time_str)
	return(time_str)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    #fptr.write(result + '\n')

    #fptr.close()
