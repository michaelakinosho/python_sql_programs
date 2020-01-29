from itertools import repeat

my_list = [5,7,8,9,10,501]
fkey = lambda x : x**2%1000
num_list = list(map(fkey,my_list))

print(num_list)
