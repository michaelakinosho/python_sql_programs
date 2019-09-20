#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def num_prime_factors(n=1):

    #print("Let's find the Prime Factors")
    n_list = []
    #print(n_list)
    #print(type(n_list))

    prime_set = set()
    #print(type(prime_set))

    factors_list = []
    fmod = 0
    prime_num = 2
    x = 0

    while n != 1:
    	fmod = n % prime_num
    	if fmod == 0:
    		prime_set.add(prime_num)
    		factors_list.append(prime_num)
    		n = n / prime_num
    	else:
    		prime_num += 1
    		for y in prime_set:
    			if prime_num % y != 0:
    				break
    	#print(x)
    	x += 1

    #print(prime_set)
    #print(factors_list)

    i = 0
    j = 0
    factors_set = {1}
    f_num = 0
    while i < len(factors_list):
        f_num = factors_list[i]
        factors_set.add(f_num)
        j = 0

        while j < len(factors_list):
            if i != j:
                f_num = f_num * factors_list[j]
            factors_set.add(f_num)

            j += 1

        f_num = factors_list[i]
        j = len(factors_list) - 1
        while j > 0:
            #print(j)
            if i != j:
                f_num = f_num * factors_list[j]
            factors_set.add(f_num)

            j -= 1
        i += 1
    #print(factors_set)
    return(factors_set)

def getTotalX(a, b):
    # Write your code here
    #print(min(b))
    list_of_factors = list()
    b.sort()

    i = 0
    while i < len(b):
        list_of_factors.append(num_prime_factors(b[i]))
        i += 1
    #print(list_of_factors)

    i = 0
    net_factors = list_of_factors[i]
    if len(list_of_factors) > 1:
        i = 1
        while i < len(list_of_factors):
            net_factors = net_factors.intersection(list_of_factors[i])

            i += 1
    #print(net_factors)
    net_factors = list(net_factors)
    net_factors.sort()
    #print(net_factors)

    i = 0
    while i < len(a):
        j = 0
        while j < len(net_factors):
            #print(net_factors[j])
            #print(a[i])
            if net_factors[j]%a[i] != 0:
                net_factors.remove(net_factors[j])

            else:
                j += 1
        i += 1

    i = 0
    while i < len(a):
        j = 0
        while j < len(a):
            if a[i]%a[j] != 0 and a[i] > a[j]:
                if a[j] in net_factors:
                    net_factors.remove(a[j])
            j += 1
        i += 1

    #print(net_factors)
    #print(len(net_factors))
    return(len(net_factors))

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    #fptr.write(str(total) + '\n')

    #fptr.close()
