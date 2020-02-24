n = int(input())
s = set(map(int, input().split()))
nc = int(input())

for i in range(nc):
    str = list(input().split())
    s0 = str[0]

    if s0 == "remove" or s0 == "discard":
        s1 = int(str[1])
        s.discard(s1)
    elif s0 == "pop":
        s.pop()

print(sum(s))
