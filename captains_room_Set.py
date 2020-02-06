K = int(input())
my_list = list(map(int, input().split()))

my_set = set(my_list)

result = (sum(my_set)*K-sum(my_list))/(K-1)
print(int(result))
