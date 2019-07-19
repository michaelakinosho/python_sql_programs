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

#max number of decimal places returned value will have
dec_limit = 20

from math import exp, expm1
from decimal import *

def e_nth_digit():

    print("E is known as an irritational number.\nMeaning it can go to infinity.")
    print("This program will return a value for E of an entered number and up to the number of digits you specify")
    mExp = Decimal(0)

    try:
        x = int(input("Find the exponent of this value: "))
        num_digits = int(input("Number of decimal places for {}: ".format(x)))

        if num_digits < 1:
            print('Please enter a number greater than zero')
        elif num_digits > dec_limit:
            num_digits = dec_limit

        getcontext().prec = dec_limit
        mExp = Decimal(exp(x))*Decimal(1)
        mExp = round(mExp,num_digits)

        print(mExp)
        return mExp

    except Exception:

        print('Hmm...Something went wrong, try a smaller value\nfor the exponent ')
        e_nth_digit()

e_nth_digit()
