import math
import os
import random
import re
import sys

#The function is expected to return an INTEGER_ARRAY.
#The function accepts 2D_INTEGER_ARRAY gb as parameter

def componentsInGraph(gb,n):
    a = 2*n
    b = 0
    d = [True for _ in range(2*n)]
    for  v in range(2*n):
        if d[v]:
            s = [v]
            d[v] = False
            c = 0
            while len(s) > 0:
                #print(f"s is:{s}")
                x = s.pop()
                c += 1
                for y in gb[x]:
                    print(f"here y is:{y} and x is {gb[x]}")
                    if d[y]:
                        s.append(y)
                        d[y] = False
            if c > 1:
                a = min(a, c)
                b = max(b, c)
    #print(a, b)
    #print(d)
    return [a, b]

if __name__ == '__main__':
    file_path = "C:\\Users\\micha\\Documents\\GitHub\\python_sql_programs\\testing.txt"
    fptr = open(file_path, 'w')

    n = int(input().strip())

    gb = [[] for _ in range(2*n)]
    #test_gb = [[] for _ in range(2*(n+0))]

    for _ in range(n):
        u, v = map(int, input().split())
        #test_gb[u].append(v)
        #test_gb[v].append(u)
        
        u, v = u-1, v-1
        gb[u].append(v)
        gb[v].append(u)
        #gb.append(list(map(int, input().rstrip().split())))
    print(gb)
    #print(test_gb)

    result = componentsInGraph(gb,n)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()