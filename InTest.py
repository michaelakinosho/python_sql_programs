import copy

list_my = [[1,2,3],[123,234,345],[98,87,76]]
list_copy = copy.deepcopy(list_my)

print(list_my)
print(list_copy)

list_my[0][0] = 999
list_copy[2][2] = 777

print(list_my)
print(list_copy)

list_copy[2][2] = 333
print(list_my)
print(list_copy)
