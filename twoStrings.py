q = int(input())

for q_itr in range(q):
    s1 = input()

    s2 = input()
    sub_bool = "NO"
    i = 0
    while i < len(s1):
        if s1[i] in s2:
            sub_bool = "YES"
            break
        i += 1
    print(sub_bool)
