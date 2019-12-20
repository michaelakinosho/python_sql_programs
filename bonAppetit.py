#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    chk_s = "Bon Appetit"
    chk = b - int((sum(bill)-bill[k])/2)
    #print(chk)

    if chk != 0:
        chk_s = chk

    print(chk_s)

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
