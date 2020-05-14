#!/bin/python3

import os
import sys
from collections import defaultdict

#
# Complete the circularPalindromes function below.
#
def circularPalindromes(n, s):
    #
    # Write your code here.
    #

    letters_list = []
    index_list = []
    for i in range(0,26):
        letters_list.append([])

    i = 0
    for x in s:
        idx = int(ord(x)-97)
        letters_list[idx].append(s[i:len(s)].index(x)+i)
        i += 1

    i = 0
    for x in letters_list:
        if len(x) > 0:
            index_list.append(i)
        i += 1

    #print(index_list)
    print(letters_list)

    #This 1ST while loop will count the number of rotations of s
    i = 0
    while i < n:
        #This 2ND while loop will work on the letters
        j = 0
        maxlen = 1
        while j < len(index_list):
            prime_list = letters_list[index_list[j]]
            len_pl = len(prime_list)
            min_pl = prime_list[0]
            max_pl = prime_list[len_pl-1]
            sum_min_max = min_pl + max_pl
            dis_min_max = max_pl - min_pl + 1
            if dis_min_max <= maxlen:
                break

            k = 0
            while k < len_pl:
                if sum_min_max-prime_list[k] in prime_list:
                    print("okay prime list", prime_list)
                    k += 1
                else:
                    print(k, prime_list[k])
                    print("old prime list",prime_list)
                    prime_list = prime_list[k:len(prime_list)-k]
                    print("new prime list",prime_list)
                    len_pl = len(prime_list)
                    min_pl = prime_list[0]
                    max_pl = prime_list[len_pl-1]
                    sum_min_max = min_pl + max_pl
                    dis_min_max = max_pl - min_pl + 1
                    #break
                    k = 0
                    if dis_min_max <= maxlen:
                        break

            j += 1
            #print(prime_list)

        i += 1
    return maxlen

if __name__ == '__main__':
    py_input = open('py_input.txt','r')
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(py_input.readline())
    #n = int(input())

    s = list(py_input.readline().rstrip())
    #s = input()

    result = circularPalindromes(n, s)

    #fptr.write('\n'.join(map(str, result)))
    #fptr.write('\n')

    #fptr.close()
