A_set = set(map(int,input().split()))

sub_set = set()
for x in range(int(input())):
    T_set = set(map(int, input().split()))
    sub_set = sub_set.union(T_set)

print(A_set.issuperset(sub_set))
