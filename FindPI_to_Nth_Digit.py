#My signature and contact details
#Written by: Michael Akinosho
#Email: michaelakinosho@moaadvisory.com

#Program is designed to return pi to the number of decimal places the user specifies
#Limiting the program to 100 decimal places

#importing the decimal library brings in the Decimal type which will allow
#us to get a very high level of precision
#see the Python documentation on Decimal fixed point and floating point arithmetic
#https://docs.python.org/2/library/decimal.html

#limiting the number of decimal places pi can be returned for
#even if user enters a number greater than 100
dec_limit = 20

from math import exp, expm1
from decimal import *
import os


def pi_nth_digit():

    print("PI is known as an irritational number.\nMeaning it can go to infinity.")
    print("This program will return a value of pi up to the number of digits you specify")
    mPI = Decimal(0)
    num_digits = 0

    try:
        num_digits = int(input("Number of decimal places for PI:"))

        if num_digits < 1:
            print('Please enter a number greater than zero')
        elif num_digits > dec_limit:
            num_digits = dec_limit

        getcontext().prec = num_digits
        mPI = Decimal(22)/Decimal(7)
        print(mPI)
        return (mPI)

    except ValueError:
        print('Oops enter a number')
        pi_nth_digit()

pi_nth_digit()
