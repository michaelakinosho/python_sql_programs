#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    leap_date = "12.09."
    reg_date = "13.09."

    if year <= 1917:
        if year%4 == 0:
            return(leap_date + str(year))
        else:
            return(reg_date + str(year))

    elif year >= 1919:
        if year%400 == 0 or (year%100 != 0 and year%4 == 0):
            return(leap_date + str(year))
        else:
            return(reg_date + str(year))

    else:
        return("26.09.1918")


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)
    print(result)

    #fptr.write(result + '\n')

    #fptr.close()
