#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    cost_counter = 0
    cc_s_sublist_one = 0
    cc_s_sublist_two = 0
    even_nums = [2,4,6,8]
    number_difference = 7
    even_digit = 0
    s_sublist = []
    s_sublist_i_value = 0
    s_i_value = 0

    MagicSquares = [
                    [[8,3,4],[1,5,9],[6,7,2]],
                    [[8,1,6],[3,5,7],[4,9,2]],
                    [[6,1,8],[7,5,3],[2,9,4]],
                    [[6,7,2],[1,5,9],[8,3,4]],
                    [[4,9,2],[3,5,7],[8,1,6]],
                    [[4,3,8],[9,5,1],[2,7,6]],
                    [[2,7,6],[9,5,1],[4,3,8]],
                    [[2,9,4],[9,5,1],[4,3,8]]]

    if s[0][0]%2 != 0:
        for n in even_nums:
            if abs(s[0][0]-n) == 1:
                even_digit = n
                #number_difference = 1
                break
            elif abs(s[0][0]-n) < number_difference:
                even_digit = n
                #number_difference = abs(s[0][0]-n)
        s[0][0] = even_digit
        #cost_counter += number_difference
    else:
        even_digit = s[0][0]

    n = 0
    while n < len(MagicSquares):
        if MagicSquares[n][0][0] == even_digit:
            s_sublist.append(MagicSquares[n])
            s_sublist.append(MagicSquares[n+1])
        n += 2

    k = 0
    while k < 2:
        i = 0
        #print(s_sublist[k])
        while i < len(s_sublist[k]):
            j = 0
            while j < len(s_sublist[k]):
                s_sublist_i_value = s_sublist[k][i][j]
                s_i_value = s[i][j]
                if s_sublist_i_value != s_i_value:
                    if k == 0:
                        cc_s_sublist_one += abs(s_sublist_i_value-s_i_value)
                    elif k == 1:
                        cc_s_sublist_two += abs(s_sublist_i_value-s_i_value)
                j += 1
            i += 1
        k += 1

    print("cost counter one: ", cc_s_sublist_one)
    print("cost counter two: ", cc_s_sublist_two)

    if cc_s_sublist_one <= cc_s_sublist_two:
        return(cc_s_sublist_one)
    else:
        return(cc_s_sublist_two)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)
    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()
