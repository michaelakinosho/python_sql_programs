e = input()
e_s = set(map(int, input().split()))
f = input()
f_s = set(map(int, input().split()))

u_s = e_s.intersection(f_s)

print(len(u_s))
