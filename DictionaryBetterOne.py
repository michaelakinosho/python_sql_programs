#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    phoneBook = {}
    nameOnly = []
    pB_dict = {}
    nameFound = "Not found"
    names_list = []
    ind = 0

    for _ in range(0,n):
        arr = list(map(str, input().rstrip().split()))
        pB_dict = {arr[0]:arr[1]}
        nameOnly.append(arr[0])
        phoneBook.update({arr[0]:arr[1]})

    #print(phoneBook)
    try:
        name = input()
        while name != "":
            names_list.append(name)
            name = input()
    except EOFError:
        name = ""

    for x in range(0,len(names_list)):
        if names_list[x] in phoneBook.keys():
            nameFound = names_list[x] + "=" + str(phoneBook[names_list[x]])
        else:
            nameFound = "Not found"
        print(nameFound)
