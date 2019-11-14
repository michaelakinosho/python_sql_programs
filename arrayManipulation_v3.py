#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    max_num = 0
    counter_cur = 0
    counter_max = 0

    index_lst = set()
    for i in queries:
        index_lst = index_lst.union(range(i[0],i[1]+1))
    index_lst = list(index_lst)

    for y in queries:
        max_num += y[2]

    for x in index_lst:
        #print(x)
        for y in queries:
            if x >= y[0] and x <= y[1]:
                counter_cur += y[2]
        if counter_cur == max_num:
            
            return(counter_cur)
        elif counter_cur > counter_max:
            counter_max = counter_cur
        counter_cur = 0

    return(counter_max)





    #print(my_lst)
    #return(max(my_lst))

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)
    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()
