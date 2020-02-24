import itertools
from more_itertools import *
data = [1,2,3,6,5,4,4,2,5,3,6,1,6,5,3,2,4,1,2,5,1,4,3,6,8,4,3,1,5,6,2]

groups = []
uniquekeys = []
data = sorted(data)
for k, g in groupby(data, count()):
    groups.append(list(g))      # Store group iterator as a list
    uniquekeys.append(k)

print(groups)

keyfunc = lamb
