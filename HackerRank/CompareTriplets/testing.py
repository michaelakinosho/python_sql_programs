#!/bin/python3

import os
import sys

#
# Complete the bendersPlay function below.
#
def bendersPlay(n, paths, query):
    #
    # Write your code here.
    #

    big_list = set(range(1,n+1))
    #print(big_list)

    u_list = set()
    for u in paths:
        u_list.add(u[0])

    v_list = set()
    for v in paths:
        v_list.add(v[1])

    ep_only_list = big_list.difference(u_list)
    bp_only_list = big_list.difference(v_list)

    #print(bp_only_list)
    #print(ep_only_list)

    u_list = list(u_list)

    u_count_list = list("1"*len(u_list))

    #print(u_list)

    #print(u_count_list)

    i = 0
    while i < len(u_list):
        if u_list[i] not in ep_only_list:
        #if u_list[i] not in ep_only_list and u_list[i] == 4:
            my_count = v_count(i, paths, u_list, ep_only_list)
        else:
            my_count = 0
        print(my_count)
        #u_count_list[i] = v_count(paths)

        i += 1
    #print(u_count_list)

def v_count(i, paths, u_list, ep_only_list):

    x = 0
    n_count = 1
    my_lst = [u_list[i]]

    #print(my_lst)
    while x < len(paths):
        j = 0
        while j < len(paths):
            if paths[x][1] == paths[j][0]:


            j += 1
        x += 1
    return(my_lst, n_count)
    #return(n_count)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    paths = []

    for _ in range(m):
        paths.append(list(map(int, input().rstrip().split())))

    q = int(input())

    for q_itr in range(q):
        query_count = int(input())

        query = list(map(int, input().rstrip().split()))

        result = bendersPlay(n, paths, query)

        #fptr.write(result + '\n')

    #fptr.close()
