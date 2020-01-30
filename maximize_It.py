from itertools import product
A,B = map(int,input().split(" "))

fkey = lambda x : x**2%B
big_list = []
max_num  = 0

for i in range(A):
    big_list.append(list(map(int,input().split(" "))))

for j in product(*big_list):
    print(j)
    
    print(sum(map(lambda x:x**2,j))%B)
    max_num = max(sum(map(lambda x:x**2,j))%B, max_num)

print(max_num)
#print(big_list)
#     num_list = list(map(fkey,my_list))
#     print((num_list))
#     print(max(num_list))
#     max_num += max(num_list)
#
# print(max_num)
