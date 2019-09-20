#Replace all ______ with rjust, ljust or center.

(n, m) = list(map(int, input().rstrip().split()))

i_list = list(map(int, input().rstrip().split()))

A_set = set(map(int, input().rstrip().split()))

B_set = set(map(int, input().rstrip().split()))

#print(n,m,i_list,A_set)

i = 0
happy_count = 0
while i < n:
    if i_list[i] in A_set:
        happy_count += 1
    elif i_list[i] in B_set:
        happy_count -= 1
    i += 1

print(happy_count)
