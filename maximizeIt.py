#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import accumulate
from itertools import repeat

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    chk_s = "Bon Appetit"
    chk = b - int((sum(bill)-bill[k])/2)
    #print(chk)

    if chk != 0:
        chk_s = chk

    print(chk_s)

if __name__ == '__main__':
    k,m = map(int, input().split(" "))

    for i in range(k):
        num_lst = list(map(int, input().rstrip().split()))
        num_lst.pop(0)

        test = list(map(pow,num_lst, repeat(2)))

        test1 = list(map(mod,text, repeat(2)))

    print(test)
    print(num_lst)
