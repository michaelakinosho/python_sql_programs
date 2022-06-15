n = int(input())
g = [[] for _ in range(2*n)]

for _ in range(n):
    u, v = map(int, input().split())
    u, v = u-1, v-1
    g[u].append(v)
    g[v].append(u)
print(g)

a = 2*n
b = 0
d = [True for _ in range(2*n)]
for v in range(2*n):
    if d[v]:
        s = [v]
        d[v] = False
        c = 0
        while len(s) > 0:
            x = s.pop()
            c += 1
            for y in g[x]:
                if d[y]:
                    s.append(y)
                    d[y] = False
        if c > 1:
            a = min(a, c)
            b = max(b, c)

print(a, b)