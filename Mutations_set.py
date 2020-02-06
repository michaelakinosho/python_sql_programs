A = int(input())
my_set = set(map(int,input().split()))

N = int(input())
for i in range(N):
    set_Ops = list(map(input().split()))
    sub_set = set(map(int, input().split()))

    if set_Ops[0] == "update":
        my_set.update(sub_set)
    elif set_Ops[0] == "intersection_update":
        my_set.intersection_update(sub_set)
    elif set_Ops[0] == "difference_update":
        my_set.difference_update(sub_set)
    elif set_Ops[0] == "symmetric_difference_update":
        my_set.symmetric_difference_update(sub_set)

print(sum(my_set))
