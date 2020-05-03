#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict


# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):

    d_rows = defaultdict(list)
    d_cols = defaultdict(list)
    for r,c in obstacles:
        d_rows[r].append(c)
        d_cols[c].append(r)
        d_rows[r].sort()
        d_cols[c].sort()

    #print(min(d_rows.keys()))
    #print(d_cols)

    #print("Queen's position: ",r_q, c_q)

    q_m = 0 #Queen's movement
    #Queen's movement straight down
    st_down = r_q - 1
    #print("straight down: ", st_down)
    q_m += st_down

    #Queen's movement straight left
    st_left = c_q - 1
    #print("straight left:",st_left)
    q_m += st_left

    #Queen's movement straight up
    st_up = n - r_q
    #print("straight up: ", st_up)
    q_m += st_up

    #Queen's movement straight right
    st_right = n - c_q
    #print("straight right: ",st_right)
    q_m += st_right

    #Queen's movement diagonal left down
    diag_left_down = (st_left,st_down)[st_down<=st_left]
    #print("diagonal left down: ",diag_left_down)
    q_m += diag_left_down

    #Queen's movement diagonal left up
    diag_left_up = (st_up,st_left)[st_left<=st_up]
    #print("diagonal left up: ",diag_left_up)
    q_m += diag_left_up

    #Queen's movement diagonal right up
    diag_right_up = (st_right,st_up)[st_up<=st_right]
    #print("diagonal right up: ",diag_right_up)
    q_m += diag_right_up

    #Queen's movement diagonal right down
    diag_right_down = (st_down,st_right)[st_right<=st_down]
    #print("diagonal right down: ",diag_right_down)
    q_m += diag_right_down

    #print(q_m)

    #Queen's movement blocked straight up or straight down
    if c_q in d_cols.keys():
        tmp_list = d_cols.get(c_q)
        #print(tmp_list)
        #Blocked straight down
        i = 0
        temp = 0
        while i < len(tmp_list):
            if tmp_list[i] < r_q:
                temp = tmp_list[i]
                #print("Blocked straight down:",tmp_list[i], c_q, temp)
            else:
                break
            i += 1
        if temp != 0:
            q_m -= temp

        #Blocked straight up
        i = len(tmp_list)-1
        temp = 0
        while i > -1:
            if tmp_list[i] > r_q:
                temp = tmp_list[i]
                #print("Blocked straight up:",tmp_list[i], c_q, n-temp+1)
            else:
                break
            i -= 1
        if temp != 0:
            q_m -= (n-temp+1)

    #Queen's movement blocked straight left or straight right
    if r_q in d_rows.keys():
        tmp_list = d_rows.get(r_q)
        #print(tmp_list)
        #Blocked straight left
        i = 0
        temp = 0
        while i < len(tmp_list):
            if tmp_list[i] < c_q:
                temp = tmp_list[i]
                #print("Blocked straight left:",r_q, tmp_list[i], temp)
            else:
                break
            i += 1
        if temp != 0:
            q_m -= temp

        #Blocked straight right
        i = len(tmp_list)-1
        temp = 0
        while i > -1:
            if tmp_list[i] > c_q:
                temp = tmp_list[i]
                #print("Blocked straight right:",r_q, tmp_list[i], n-temp+1)
            else:
                break
            i -= 1
        if temp != 0:
            q_m -= (n-temp+1)

    #Blocked diagonal left down
    i = 1
    while i < diag_left_down+1:
        r_temp = r_q-i
        if r_temp in d_rows.keys():
            c_temp = c_q-i
            if c_temp in d_rows[r_temp]:
                temp = diag_left_down - i + 1
                #print("Blocked diagonal left down:", r_temp, c_temp, temp)
                q_m -= temp
                break
        i += 1

    #Blocked diagonal left up
    i = 1
    while i < diag_left_up+1:
        r_temp = r_q+i
        if r_temp in d_rows.keys():
            c_temp = c_q-i
            if c_temp in d_rows[r_temp]:
                temp = diag_left_up - i + 1
                #print("Blocked diagonal left up:",r_temp, c_temp, temp)
                q_m -= temp
                break
        i += 1

    #Blocked diagonal right up
    i = 1
    while i < diag_right_up+1:
        r_temp = r_q+i
        if r_temp in d_rows.keys():
            c_temp = c_q+i
            if c_temp in d_rows[r_temp]:
                temp = diag_right_up - i + 1
                #print("Blocked diagonal right up:",r_temp, c_temp, temp)
                q_m -= temp
                break
        i += 1

    #Blocked diagonal right down
    i = 1
    while i < diag_right_down+1:
        r_temp = r_q-i
        if r_temp in d_rows.keys():
            c_temp = c_q+i
            if c_temp in d_rows[r_temp]:
                temp = diag_right_down - i + 1
                #print("Blocked diagonal right down:",r_temp, c_temp, temp)
                q_m -= temp
                break
        i += 1

    return(q_m)

if __name__ == '__main__':
    py_input = open('py_input.txt','r')

    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = py_input.readline().split()
    #nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = py_input.readline().split()
    #r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = set()

    for _ in range(k):

        obstacles.add(tuple(map(int, py_input.readline().rstrip().split())))
        #obstacles.add(tuple(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)
    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()
