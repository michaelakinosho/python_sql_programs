#Program is designed to return pi to the number of decimal places the user specifies
#Limiting the program to 100 decimal places

#importing the decimal library brings in the Decimal type which will allow
#us to get a very high level of precision
#see the Python documentation on Decimal fixed point and floating point arithmetic
#https://docs.python.org/2/library/decimal.html

from math import exp, expm1


print("PI is known as an irritational number.\nMeaning it can go to infinity.")
print("This program will return a value of pi up to the number of digits you specify")

num_digits = input("Number of decimal places for PI:")
print(num_digits)
