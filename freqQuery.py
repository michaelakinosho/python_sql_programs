import math
import os
import random
import re
import sys

# Complete the freqQuery function below
def freqQuery(queries):
    return ["Testing","Tested"]

if __name__ == '__main__':
    file_path = "C:\\Users\\micha\\Documents\\GitHub\\python_sql_programs\\testing.txt"
    print(file_path)
    #fptr = open(file_path,'w')
    fptr = open(file_path,'w')

    q = int(input().strip())
    #q = 1
    #queries = []
    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()