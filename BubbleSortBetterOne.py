#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here

swap_counter = 0
temp_int = 0
my_bool = True
i = 0
j = 0
while j < n:
    i = 0
    while i < n-1:
        if a[i]>a[i+1]:
            temp_int = a[i]
            a[i] = a[i+1]
            a[i+1] = temp_int
            print(a)
            swap_counter += 1
        i += 1
    j += 1

print("Array is sorted in",swap_counter, "swaps.")
print("First Element:", a[0])
print("Last Element:", a[-1])
