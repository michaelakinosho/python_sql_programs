
i = int(input())
n = list(map(int, input().split(" ")))

j = int(input())
m = list(map(int, input().split(" ")))

n = set(n)
m = set(m)

diff_lst = n.symmetric_difference(m)
diff_lst = sorted(list(diff_lst))

for i in diff_lst:
    print(i)

#diff_lst.add(m.difference(n))

#print(diff_lst)
