#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the climbingLeaderboard function below.
# Climbing The Leaderboard
def climbingLeaderboard(scores, alice):
    #print(scores)
    #print(alice)

    scores = sorted(set(scores),reverse=True)
    alice = list(Counter(alice).items())

    ans = list()

    i = 0
    j = len(scores)-1
    while i < len(alice):
        a,b = alice[i]
        
        while j > -1:
            if a < scores[j]:
                k = 0
                while k < b:
                    #print(j+2)
                    ans.append(j+2)
                    k += 1
                break
            elif a < scores[j-1] and a >= scores[j]:
                k = 0
                while k < b:
                    #print(j+1)
                    ans.append(j+1)
                    k += 1
                break
            elif a >= scores[0]:
                k = 0
                while k < b:
                    #print(1)
                    ans.append(1)
                    k += 1
                break
            j -= 1
        #print(alice[i])
        i += 1
    return(ans)

if __name__ == '__main__':
    fptr = open('py_output.txt', 'w')
    py_input = open('py_input.txt','r')

    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(py_input.readline())
    #scores_count = int(input())

    scores = list(map(int, py_input.readline().split(" ")))
    #scores = list(map(int, input().split(" ")))

    alice_count = int(py_input.readline())
    #alice_count = int(input())

    alice = list(map(int, py_input.readline().split(" ")))
    #alice = list(map(int, input().split(" ")))

    py_input.close()

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
