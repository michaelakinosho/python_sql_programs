
A,B = map(int,input().split(" "))

fkey = lambda x : x**2%B
max_num = 0

for i in range(A):
    my_list = list(map(int,input().split(" ")))
    num_list = list(map(fkey,my_list))
    print((num_list))
    print(max(num_list))
    max_num += max(num_list)

print(max_num)
