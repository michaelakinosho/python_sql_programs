import math
import os
import random
import re
import sys

def tempfunc(queries):
    return True

if __name__ == '__main__':
    file_path = "C:\\Users\\micha\\Documents\\GitHub\\python_sql_programs\\testing.txt"
    fptr = open(file_path, 'w')

    n = int(input().strip())
    queries = []

    for _ in range(n):
        queries.append(input().rstrip().split())
        
    result = tempfunc(queries)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()